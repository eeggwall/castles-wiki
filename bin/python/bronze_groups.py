# Even-group splits that could give a bronze castle: enumerate, filter, SAT-test.
# Needs numpy and python-sat (pip install python-sat).
import itertools, numpy as np
from fractions import Fraction
from multiprocessing import Pool
from pysat.solvers import Cadical153

BRONZE = (3 + 13 ** 0.5) / 2

def tables(k):
    """k x k neighbor-count tables in peeling order with largest eigenvalue bronze,
    irreducible and with consistent group sizes."""
    def rows(i):  # row i: sum over columns i..k-1 at most 2, total at most 4
        return [pre + suf for suf in itertools.product(range(3), repeat=k - i) if sum(suf) <= 2
                for pre in itertools.product(range(5), repeat=i) if sum(pre) + sum(suf) <= 4]
    opts = [np.array(rows(i)) for i in range(k)]
    last = np.array(list(itertools.product(range(len(opts[-2])), range(len(opts[-1])))))
    out = []
    for head in itertools.product(*[range(len(o)) for o in opts[:-2]]):
        H = np.array([opts[i][h] for i, h in enumerate(head)]).reshape(k - 2, k)
        if any((H[a][b] > 0) != (H[b][a] > 0) for a in range(k - 2) for b in range(k - 2)):
            continue
        B = np.empty((len(last), k, k)); B[:, :k - 2] = H
        B[:, k - 2] = opts[-2][last[:, 0]]; B[:, k - 1] = opts[-1][last[:, 1]]
        rho = np.abs(np.linalg.eigvals(B)).max(axis=1)
        out += [B[s].astype(int).tolist() for s in np.nonzero(abs(rho - BRONZE) < 1e-8)[0]]
    return [Q for Q in out if irreducible(Q) and sizes_consistent(Q)]

def irreducible(Q):
    n = len(Q); R = (np.array(Q) > 0).astype(int) + np.eye(n, dtype=int)
    return (np.linalg.matrix_power(R, n) > 0).all()

def sizes_consistent(Q):  # positive n_i with n_i q_ij = n_j q_ji
    n = len(Q)
    if any((Q[i][j] > 0) != (Q[j][i] > 0) for i in range(n) for j in range(n)): return False
    size = [None] * n; size[0] = Fraction(1); stack = [0]
    while stack:
        i = stack.pop()
        for j in range(n):
            if i != j and Q[i][j] > 0:
                s = size[i] * Q[i][j] / Q[j][i]
                if size[j] is None: size[j] = s; stack.append(j)
                elif size[j] != s: return False
    return True

def fits(Q, g, R, castle=False, box=None):
    """Local fit: can a (2R+1)^2 patch centered on a group-g cell be labeled (0 = empty, 1..k = group)
    so every inner cell has the neighbor counts of its row?  box=N instead asks for a whole finite
    N x N shape with every group present."""
    k = len(Q); L = k + 1
    if box: cells = [(x, y) for x in range(box) for y in range(box)]
    else:   cells = [(x, y) for x in range(-R, R + 1) for y in range(-R, R + 1)]
    cs = set(cells); var = {}
    v = lambda c, l: var.setdefault((c, l), len(var) + 1)
    S = Cadical153()
    for c in cells:
        S.add_clause([v(c, l) for l in range(L)])
        for a, b in itertools.combinations(range(L), 2): S.add_clause([-v(c, a), -v(c, b)])
    want = [[4 - sum(r)] + list(r) for r in Q]
    if box:
        for gg in range(k): S.add_clause([v(c, gg + 1) for c in cells])
        checked = cells
    else:
        S.add_clause([v((0, 0), g + 1)])
        checked = [c for c in cells if abs(c[0]) < R and abs(c[1]) < R]
    for c in checked:
        nb = [n for n in [(c[0] + 1, c[1]), (c[0] - 1, c[1]), (c[0], c[1] + 1), (c[0], c[1] - 1)] if n in cs]
        for gg in range(k):
            for t in itertools.product(range(L), repeat=len(nb)):
                cnt = [4 - len(nb)] + [0] * k
                for l in t: cnt[l] += 1
                if cnt != want[gg]: S.add_clause([-v(c, gg + 1)] + [-v(n, l) for n, l in zip(nb, t)])
    if castle:  # one base row (or below the patch); nothing under it; a cell over an empty one sits on it
        ys = sorted({y for _, y in cells}); base = {y: len(var) + 1 + i for i, y in enumerate(ys + ['below'])}
        S.add_clause(list(base.values()))
        for a, b in itertools.combinations(base.values(), 2): S.add_clause([-a, -b])
        for (x, y) in cells:
            if (x, y - 1) in cs: S.add_clause([v((x, y), 0), -v((x, y - 1), 0), base[y]])
            for b in ys:
                if y < b: S.add_clause([-base[b], v((x, y), 0)])
    r = S.solve(); S.delete(); return r

def first_failing_group(args):
    Q, R, castle = args
    return next((g for g in range(len(Q)) if not fits(Q, g, R, castle)), None)

if __name__ == '__main__':
    for name, Q in [('golden', [[0, 1], [1, 1]]), ('silver', [[1, 1], [2, 1]]), ('phi^2', [[1, 1], [1, 2]])]:
        print(name, all(fits(Q, g, 4, c) for g in range(2) for c in (False, True)))
    with Pool(8) as pool:
        for k in (2, 3, 4, 5):
            T = tables(k)
            grid = pool.map(first_failing_group, [(Q, 3, False) for Q in T])
            left = [Q for Q, g in zip(T, grid) if g is None]
            cast = pool.map(first_failing_group, [(Q, 3, True) for Q in left])
            print(f'k={k}: {len(T)} tables, {len(left)} fit the grid at R=3, '
                  f'{sum(g is None for g in cast)} fit as castles')
            if left:
                print('  finite shapes up to 12 x 12:',
                      any(fits(Q, None, None, box=N) for Q in left for N in (6, 8, 10, 12)))
