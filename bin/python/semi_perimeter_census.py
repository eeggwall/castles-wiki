# Castle strips counted by semi-perimeter s = width + blocks: growth constants and their first heights.
# Page: wiki/pages/semi-perimeter-growth-census.md.  Needs numpy, sympy, mpmath.
# A rule is an h x h 0/1 table (a -> b allowed).  A step from height a to height b adds 1 + max(0, b - a)
# to s, so the strip denominator is det(I - M(x)) with M[a][b] = A[a][b] * x^(1 + max(0, b - a)), and the
# growth constant is 1/x* for the smallest positive root x*.
import itertools, time, numpy as np, sympy as sp, mpmath as mp

x, z = sp.symbols('x z')
W = lambda h: np.array([[1 + max(0, b - a) for b in range(h)] for a in range(h)], float)

def growth(A):
    """1/x* by bisection on the spectral radius of M(x) (increasing in x)."""
    A = np.array(A, float); Wh = W(len(A)); rho = lambda M: max(abs(np.linalg.eigvals(M)))
    if rho(A) <= 1 + 1e-12: return 1.0
    lo, hi = 0.0, 1.0
    for _ in range(64):
        m = (lo + hi) / 2
        lo, hi = (m, hi) if rho(A * m ** Wh) < 1 else (lo, m)
    return 1 / lo

def denominator(A):
    h = len(A)
    M = sp.Matrix(h, h, lambda a, b: A[a][b] * x ** (1 + max(0, b - a)))
    return sp.Poly(sp.expand((sp.eye(h) - M).det(method='berkowitz')), x)

def census(hmax):
    """Exact: every rule up to height hmax, distinct denominators, new growth constants per height."""
    seen = set()
    for h in range(1, hmax + 1):
        dens = {}
        for bits in itertools.product((0, 1), repeat=h * h):
            D = denominator([bits[i * h:(i + 1) * h] for i in range(h)]); dens[tuple(D.all_coeffs())] = D
        new = []
        for D in dens.values():
            best = None
            for f, _ in sp.factor_list(D.as_expr())[1]:
                P = sp.Poly(f, x)
                for r in P.real_roots():
                    if float(r) > 0 and (best is None or float(r) < best[0]): best = (float(r), P)
            if best is None: continue
            mp_ = sp.Poly(sp.primitive(sp.expand(z ** best[1].degree() * best[1].as_expr().subs(x, 1 / z)))[1], z)
            key = (tuple(mp_.all_coeffs()), round(1 / best[0], 9))
            if key not in seen: seen.add(key); new.append((1 / best[0], mp_.degree(), mp_.as_expr()))
        new.sort(); degs = {}
        for _, d, _ in new: degs[d] = degs.get(d, 0) + 1
        print(f'h={h}: {len(dens)} distinct denominators, {len(new)} new constants, degrees {dict(sorted(degs.items()))}; '
              f'smallest new {new[0][0]:.6f} ({new[0][2]}), largest {new[-1][0]:.6f}', flush=True)

def ceiling(H):
    """All castles of exact height h: the largest growth at height h; any family of height <= h grows no faster."""
    for h in range(2, H + 1): print(f'  all castles of height {h}: {growth(np.ones((h, h))):.6f}')
    mp.mp.dps = 50; x0 = 2 / (3 + mp.sqrt(13))
    for h in (21, 22):
        M = mp.matrix(h, h)
        for a in range(h):
            for b in range(h): M[a, b] = x0 ** (1 + max(0, b - a))
        print(f'  spectral radius of M(1/bronze), all castles of height {h}: {mp.nstr(max(abs(e) for e in mp.eig(M)[0]), 15)}')

def search(h, target):
    """Numeric scan of all 2^(h*h) rules for growth exactly `target`, then exact confirmation."""
    x0 = 1 / target; X = x0 ** W(h); bits = np.arange(h * h, dtype=np.int64); cand = []
    for start in range(0, 1 << (h * h), 1 << 20):
        m = np.arange(start, min(start + (1 << 20), 1 << (h * h)), dtype=np.int64)
        A = ((m[:, None] >> bits) & 1).astype(float).reshape(-1, h, h)
        rho = np.abs(np.linalg.eigvals(A * X)).max(axis=1)
        cand += [int(m[s]) for s in np.nonzero(abs(rho - 1) < 1e-7)[0]]
    return cand

def silver_exact(masks, h):
    q0 = sp.Poly(1 - 2 * x - x ** 2, x); cut = sp.Rational(41421356, 10 ** 8)   # sqrt 2 - 1 = 0.414213562...
    good = []
    for m in masks:
        A = [[(m >> (a * h + b)) & 1 for b in range(h)] for a in range(h)]
        D = denominator(A); q, r = sp.div(D, q0)
        if r.is_zero and D.count_roots(0, cut) == 0: good.append(A)
    return good

if __name__ == '__main__':
    t = time.time()
    print('ceiling (all castles of exact height h):'); ceiling(22)
    print('two-height castles {a, a + d}: denominators')
    for d in (1, 2, 3, 4, 8):
        S = (1, 1 + d); M = sp.Matrix(2, 2, lambda i, j: x ** (1 + max(0, S[j] - S[i])))
        print(f'  d = {d}: {sp.factor((sp.eye(2) - M).det())}')
    print('silver rules at height 4:', len(search(4, 1 + 2 ** .5)))
    c5 = search(5, 1 + 2 ** .5); g5 = silver_exact(c5, 5)
    print(f'silver at height 5: {len(c5)} numeric candidates, {len(g5)} confirmed exactly')
    forb = {(1, 2), (2, 1), (4, 5), (5, 4)}
    A = [[0 if (a + 1, b + 1) in forb else 1 for b in range(5)] for a in range(5)]
    print('  rule "no 1 next to 2, no 4 next to 5" in the confirmed list:', A in g5, '; denominator', sp.factor(denominator(A).as_expr()))
    cnt = {}
    def rec(c, s):
        if 5 in c: cnt[s] = cnt.get(s, 0) + 1
        for b in range(1, 6):
            if c and (c[-1], b) in forb: continue
            ns = s + 1 + max(0, b - (c[-1] if c else 0))
            if ns <= 16: rec(c + (b,), ns)
    rec((), 0)
    print('  its castles of exact height 5 by semi-perimeter s = 6..16:', [cnt.get(s, 0) for s in range(6, 17)])
    print('census:'); census(4)
    print(f'total {time.time() - t:.0f} s')
