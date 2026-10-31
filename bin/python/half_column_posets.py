# The half-column of a rule I + N, N acyclic: the principal square root sum_k C(1/2, k) N^k, against
# the partial orders on the heights. Every DAG is a relabeling of a strictly upper-triangular N, and
# both properties survive relabeling, so each height h <= 7 is checked over all 2^(h(h-1)/2) patterns.
# Checks: the two sets per height; labeled counts by sum h!/e(N), e the linear extensions; the entry
# 1/2 - m/8 of the poset with a bottom, m middles and a top; the failing patterns at height 7.
# Pages: wiki/pages/fractional-width-and-height.md, wiki/pages/half-derivative-seminar.md.
from fractions import Fraction
from math import comb, factorial

import networkx as nx
import numpy as np

ok_all = True


def check(label, cond):
    global ok_all
    ok_all &= bool(cond)
    print(label, bool(cond))


COEF = [Fraction(1)]                       # C(1/2, k)
for k in range(1, 7):
    COEF.append(COEF[-1] * (Fraction(1, 2) - k + 1) / k)
SCALE = 1024                               # common denominator of C(1/2, k) for k <= 6
assert all((c * SCALE).denominator == 1 for c in COEF)


def patterns(h):                           # all strictly upper-triangular 0/1 matrices, as an (n, h, h) array
    pairs = [(i, j) for i in range(h) for j in range(i + 1, h)]
    n = 1 << len(pairs)
    bits = (np.arange(n)[:, None] >> np.arange(len(pairs))) & 1
    N = np.zeros((n, h, h), dtype=np.int64)
    for t, (i, j) in enumerate(pairs):
        N[:, i, j] = bits[:, t]
    return N


def scaled_root(N):                        # SCALE * sum_k C(1/2, k) N^k, exact in integers
    h = N.shape[1]
    eye = np.broadcast_to(np.eye(h, dtype=np.int64), N.shape)
    R, Nk = SCALE * eye.copy(), eye.copy()
    for k in range(1, h):
        Nk = Nk @ N
        R = R + int(COEF[k] * SCALE) * Nk
    return R


def extensions(N):                         # number of linear extensions of each pattern, by DP over subsets
    n, h, _ = N.shape
    pred = [(N[:, :, j] * (1 << np.arange(h))).sum(axis=1) for j in range(h)]
    f = np.zeros((1 << h, n), dtype=np.int64)
    f[0] = 1
    for S in range(1 << h):
        for j in range(h):
            if not S >> j & 1:
                f[S | 1 << j] += f[S] * ((pred[j] & ~S) == 0)
    return f[-1]


def labeled(N, mask):                      # labeled DAGs with the property: sum of h!/e(N) over the patterns
    e = extensions(N[mask])
    h = N.shape[1]
    total = sum(Fraction(factorial(h), x) for x in e.tolist())
    assert total.denominator == 1
    return int(total)


def dags(n):                               # labeled DAGs (Robinson's recurrence), for the A003024 column
    a = [1]
    for m in range(1, n + 1):
        a.append(sum((-1) ** (k + 1) * comb(m, k) * 2 ** (k * (m - k)) * a[m - k] for k in range(1, m + 1)))
    return a[n]


A001035 = [1, 1, 3, 19, 219, 4231, 130023, 6129859]        # oeis.org/A001035, read 2026-10-31
A003024 = [1, 1, 3, 25, 543, 29281, 3781503, 1138779265]   # oeis.org/A003024, read 2026-10-31

# [1] by height: posets, nonnegative roots, and the two differences
print('[1]  h   patterns   posets   nonneg roots   poset, negative root   nonneg root, not poset   '
      'labeled DAGs   labeled posets   labeled nonneg roots')
ok1, store = True, {}
for h in range(2, 8):
    N = patterns(h)
    R = scaled_root(N)
    nonneg = (R >= 0).all(axis=(1, 2))
    poset = ~(((N @ N) > 0) & (N == 0)).any(axis=(1, 2))
    lab_d = labeled(N, np.ones(len(N), dtype=bool)) if h <= 6 else dags(h)
    lab_p, lab_n = labeled(N, poset), labeled(N, nonneg)
    ok1 &= lab_d == dags(h) == A003024[h] and lab_p == A001035[h]
    ok1 &= not (nonneg & ~poset).any()
    ok1 &= (lab_n == lab_p) == (h <= 6)
    store[h] = (N, R, poset & ~nonneg)
    print(f'    {h}   {len(N):8d}   {poset.sum():6d}   {nonneg.sum():12d}   {(poset & ~nonneg).sum():20d}   '
          f'{(nonneg & ~poset).sum():22d}   {lab_d:12d}   {lab_p:14d}   {lab_n:20d}')
check('[1] h = 2..7: every rule I + N with a nonnegative principal root is a partial order; the two sets '
      'coincide for h <= 6 and differ at h = 7; labeled counts match A003024 and A001035:', ok1)

# [2] the poset with a bottom, m pairwise incomparable middles and a top: entry (bottom, top) = 1/2 - m/8
ok2 = True
for m in range(1, 6):
    h = m + 2
    N = np.zeros((1, h, h), dtype=np.int64)
    N[0, 0, 1:] = 1
    N[0, 1:h - 1, h - 1] = 1
    e = Fraction(int(scaled_root(N)[0, 0, h - 1]), SCALE)
    ok2 &= e == Fraction(1, 2) - Fraction(m, 8)
    print(f'    m = {m} (h = {h}): entry (1, {h}) = {e}')
check('[2] bottom, m middles, top: the root entry from bottom to top is 1/2 - m/8, negative from m = 5 (h = 7):', ok2)

# [3] the failing patterns at height 7, up to isomorphism
N, R, bad = store[7]
graphs = []
for x in np.where(bad)[0]:
    g = nx.DiGraph([(i + 1, j + 1) for i in range(7) for j in range(7) if N[x, i, j]])
    g.add_nodes_from(range(1, 8))
    if not any(nx.is_isomorphic(g, f) for f, _ in graphs):
        graphs.append((g, Fraction(int(R[x].min()), SCALE)))
for g, mn in graphs:
    cover = nx.transitive_reduction(g)
    print(f'    covering relations {sorted(cover.edges())}; most negative root entry {mn}')
check(f'[3] h = 7: the {bad.sum()} failing patterns are {len(graphs)} posets up to isomorphism, each with a pair '
      'a < c joined through at least five middles:', all(
          any(len([b for b in g.nodes if g.has_edge(a, b) and g.has_edge(b, c)]) >= 5 for a, c in g.edges)
          for g, _ in graphs))

print('all checks passed:', ok_all)
