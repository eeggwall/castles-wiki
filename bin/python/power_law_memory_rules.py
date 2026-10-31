# The power-law memory rule |sum_{k<K} (-1)^k C(alpha, k) c_{n-k}| <= 1 on the heights {1, ..., h}: does
# the growth constant at h = 3 equal the one at h = 2? The transfer graph on windows of K - 1 columns is
# split into strongly connected components, and the Perron root is the largest over them.
# Checks: alpha = 1/2, 3/4, 9/10 and 3 <= K <= 10; the components containing height 3 against the table.
# Page: wiki/pages/power-law-memory-rules.md.
from fractions import Fraction
from itertools import product

import numpy as np

ok_all = True


def check(label, cond):
    global ok_all
    ok_all &= bool(cond)
    print(label, bool(cond))


def weights(alpha, K):                     # (-1)^k C(alpha, k), exact
    w = [Fraction(1)]
    for k in range(1, K):
        w.append(w[-1] * (k - 1 - alpha) / k)
    return w


def graph(alpha, K, h):                    # state = window of K - 1 columns, indexed in base h
    w, n = weights(alpha, K), h ** (K - 1)
    adj = [[] for _ in range(n)]
    for idx, win in enumerate(product(range(1, h + 1), repeat=K)):
        if abs(sum(w[k] * win[K - 1 - k] for k in range(K))) <= 1:
            adj[idx // h].append(idx % n)
    return adj


def sccs(adj):                             # iterative Tarjan
    n, index, low, on, st, out, c = len(adj), [-1] * len(adj), [0] * len(adj), [False] * len(adj), [], [], 0
    for root in range(n):
        if index[root] >= 0:
            continue
        work = [(root, 0)]
        index[root] = low[root] = c; c += 1; st.append(root); on[root] = True
        while work:
            v, i = work[-1]
            if i < len(adj[v]):
                work[-1] = (v, i + 1)
                u = adj[v][i]
                if index[u] < 0:
                    index[u] = low[u] = c; c += 1; st.append(u); on[u] = True
                    work.append((u, 0))
                elif on[u]:
                    low[v] = min(low[v], index[u])
            else:
                work.pop()
                if work:
                    low[work[-1][0]] = min(low[work[-1][0]], low[v])
                if low[v] == index[v]:
                    comp = []
                    while True:
                        u = st.pop(); on[u] = False; comp.append(u)
                        if u == v:
                            break
                    out.append(comp)
    return out


def perron(adj, comp):                     # spectral radius of the component's adjacency matrix
    pos = {v: i for i, v in enumerate(comp)}
    m = len(comp)
    if m == 1:
        return 1.0 if comp[0] in adj[comp[0]] else 0.0
    rows = [pos[v] for v in comp for u in adj[v] if u in pos]
    cols = [pos[u] for v in comp for u in adj[v] if u in pos]
    if m <= 1500:
        A = np.zeros((m, m))
        np.add.at(A, (rows, cols), 1.0)
        return float(max(abs(np.linalg.eigvals(A))))
    rows, cols, x, lam = np.array(rows), np.array(cols), np.ones(m), 0.0
    for _ in range(20000):                 # A + I is irreducible and aperiodic on a component
        y = np.bincount(rows, weights=x[cols], minlength=m) + x
        new = y.sum() / x.sum()
        x = y / y.max()
        if abs(new - lam) < 1e-13:
            break
        lam = new
    return new - 1


def has3(v, K, h=3):
    return any((v // h ** j) % h == 2 for j in range(K - 1))


TABLE = {(Fraction(3, 4), 6): 1.3247, (Fraction(3, 4), 7): 1.4656, (Fraction(3, 4), 8): 1.6013,
         (Fraction(9, 10), 5): 1.4656, (Fraction(9, 10), 6): 1.6180, (Fraction(9, 10), 7): 1.6180, (Fraction(9, 10), 8): 1.6536}
ok1, ok2 = True, True
for alpha in (Fraction(1, 2), Fraction(3, 4), Fraction(9, 10)):
    line = []
    for K in range(3, 11):
        a2, a3 = graph(alpha, K, 2), graph(alpha, K, 3)
        r2 = max(perron(a2, c) for c in sccs(a2))
        comps = sccs(a3)
        r12 = max([perron(a3, c) for c in comps if not any(has3(v, K) for v in c)] or [0.0])
        r3 = max([perron(a3, c) for c in comps if any(has3(v, K) for v in c)] or [0.0])
        ok1 &= abs(r12 - r2) < 1e-9 and r3 <= r2 + 1e-9
        if (alpha, K) in TABLE:
            ok2 &= abs(r3 - TABLE[(alpha, K)]) < 5e-5
        line.append(f'K = {K}: {r2:.4f} (height 3 components {r3:.4f})')
    print(f'    alpha = {alpha}: ' + '; '.join(line))
check('[1] alpha = 1/2, 3/4, 9/10 and 3 <= K <= 10: the growth constant at h = 3 equals the one at h = 2, every '
      'component containing height 3 having Perron root at most the h = 2 value:', ok1)
check('[2] the largest Perron roots of the components containing height 3 match the table on the page:', ok2)

print('all checks passed:', ok_all)
