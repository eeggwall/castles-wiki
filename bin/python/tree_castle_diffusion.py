# Diffusion on tree castles: the graph of a tree castle is a comb, its bottom row the backbone and the
# cells above row 1 of each column a tooth. The walk is the simple random walk on the castle graph.
# Checks: the comb structure and blocks = 1 + n - w; the stationary walk and the backbone rate
# (w - 1)/(n - 1); the reduced horizontal walk; msd(t) = E hor(t) away from the end columns; the
# battlement (1, h, 1, h, ...): the window 4 sqrt(2t/pi), the rate 2/(h + 1) and the crossover; the
# method against the combs of Mendez et al., Pach-Tardos and Yuste et al.; one graph, six rates.
# Page: wiki/pages/tree-castle-diffusion.md.
from fractions import Fraction
from itertools import product
from math import log, pi, sqrt
import random

import networkx as nx
import numpy as np

ok_all = True


def check(label, cond):
    global ok_all
    ok_all &= bool(cond)
    print(label, bool(cond))


def cells_of(c):
    return [(i, j) for i in range(1, len(c) + 1) for j in range(1, c[i - 1] + 1)]


def edges_of(c):
    E = []
    for i in range(1, len(c) + 1):
        E += [((i, j), (i, j + 1)) for j in range(1, c[i - 1])]
        if i < len(c):
            E += [((i, j), (i + 1, j)) for j in range(1, min(c[i - 1], c[i]) + 1)]
    return E


def blocks(c):
    return c[0] + sum(max(0, c[i] - c[i - 1]) for i in range(1, len(c)))


def is_tree(c):
    return all(not (c[i] >= 2 and c[i + 1] >= 2) for i in range(len(c) - 1))


def nbrs(c):
    N = {v: [] for v in cells_of(c)}
    for u, v in edges_of(c):
        N[u].append(v)
        N[v].append(u)
    return N


def tree_castles(wmax, hmax):
    for w in range(1, wmax + 1):
        for h in range(1, hmax + 1):
            for c in product(range(1, h + 1), repeat=w):
                if max(c) == h and is_tree(c):
                    yield c


# [1] the comb: edges of a tree castle = backbone edges + tooth edges; blocks = 1 + n - w
n_tree = n_other = 0
ok1 = True
for w in range(1, 9):
    for h in range(1, 6):
        for c in product(range(1, h + 1), repeat=w):
            if max(c) != h:
                continue
            V, E = cells_of(c), set(edges_of(c))
            comb_E = {((i, 1), (i + 1, 1)) for i in range(1, w)} | \
                     {((i, j), (i, j + 1)) for i in range(1, w + 1) for j in range(1, c[i - 1])}
            squares = sum(max(0, min(c[i], c[i + 1]) - 1) for i in range(w - 1))
            if is_tree(c):
                n_tree += 1
                ok1 &= E == comb_E and len(E) == len(V) - 1 and blocks(c) == 1 + len(V) - w
            else:
                n_other += 1
                ok1 &= comb_E < E and len(E) - len(V) + 1 == squares > 0
check(f'[1] w <= 8, h <= 5: the graph of each of the {n_tree} tree castles is its comb (bottom row and '
      f'columns), with blocks = 1 + n - w; each of the {n_other} other castles has the comb as a proper '
      f'spanning tree, with one extra edge per 2 x 2 square:', ok1)


# [2] the stationary walk: pi(v) = d(v)/(2(n - 1)); each step from pi is horizontal with probability
#     rate(c) = (w - 1)/(n - 1) = (w - 1)/(w + b - 2), so E_pi hor(t) = t rate(c) for every t
ok2, n2 = True, 0
for c in tree_castles(7, 4):
    N = nbrs(c)
    n, w = len(N), len(c)
    pi_ = {v: Fraction(len(N[v]), 2 * (n - 1)) for v in N} if n > 1 else {v: Fraction(1) for v in N}
    if n > 1:
        ok2 &= all(sum(pi_[u] / len(N[u]) for u in N[v]) == pi_[v] for v in N)
        p_hor = sum(pi_[v] * Fraction(sum(1 for u in N[v] if u[1] == v[1] == 1 and u[0] != v[0]), len(N[v]))
                    for v in N)
        ok2 &= p_hor == Fraction(w - 1, n - 1) == Fraction(w - 1, w + blocks(c) - 2)
    n2 += 1
check(f'[2] the {n2} tree castles with w <= 7, h <= 4: pi(v) = d(v)/(2(n - 1)) is stationary, and a step from '
      f'pi is horizontal with probability (w - 1)/(n - 1) = (w - 1)/(w + b - 2):', ok2)


def walk_matrix(c):
    """Transition matrix P, the horizontal-step probability r(v) of each cell, the cells, their columns."""
    N = nbrs(c)
    V = sorted(N)
    idx = {v: k for k, v in enumerate(V)}
    P = np.zeros((len(V), len(V)))
    r = np.zeros(len(V))
    for v in V:
        for u in N[v]:
            P[idx[v], idx[u]] = 1 / len(N[v])
        r[idx[v]] = sum(1 for u in N[v] if u[0] != v[0]) / len(N[v])
    return P, r, V, idx


def expected_hor(W_sym_inputs, start, r, ts):
    """E[hor(t)] = sum_{s < t} e_start P^s r for a reversible P = D^-1 W, by the spectrum of D^-1/2 W D^-1/2."""
    W = W_sym_inputs
    d = W.sum(axis=1)
    S = W / np.sqrt(np.outer(d, d))
    lam, U = np.linalg.eigh(S)
    left = U[start, :] / np.sqrt(d[start])
    right = U.T @ (np.sqrt(d) * r)
    coef = left * right
    near1 = np.abs(lam - 1) < 1e-14
    lm, sgn, mag = lam[~near1], np.sign(lam[~near1]), np.abs(lam[~near1])
    out = []
    for t in ts:
        g = np.empty_like(lam)
        g[near1] = t
        with np.errstate(divide='ignore'):
            lt = sgn ** (t % 2) * np.exp(t * np.log(mag))  # lambda^t, with 0^t = 0
        g[~near1] = (1 - lt) / (1 - lm)
        out.append(float(coef @ g))
    return out


def sqrt_slope(E, ts):
    """(E(t_2) - E(t_1))/(sqrt t_2 - sqrt t_1) for consecutive times: the coefficient of sqrt t."""
    return [(E[k + 1] - E[k]) / (sqrt(ts[k + 1]) - sqrt(ts[k])) for k in range(len(ts) - 1)]


# the long-run fraction from a backbone start is the same rate
ok2b = True
for c in [(1, 3, 1, 1, 4, 1), (2, 1, 2, 1, 2), (1, 1, 1, 2, 1, 1, 2, 1, 1), (5, 1, 1, 3, 1, 2, 1, 1, 4)]:
    N = nbrs(c)
    V = sorted(N)
    idx = {v: k for k, v in enumerate(V)}
    Wm = np.zeros((len(V), len(V)))
    for u, v in edges_of(c):
        Wm[idx[u], idx[v]] = Wm[idx[v], idx[u]] = 1
    _, r, _, _ = walk_matrix(c)
    t = 10 ** 7
    frac = expected_hor(Wm, idx[(1, 1)], r, [t])[0] / t
    ok2b &= abs(frac - (len(c) - 1) / (len(V) - 1)) < 1e-5
    print(f'    {c}: E hor(10^7)/10^7 from cell (1, 1) = {frac:.7f}, (w - 1)/(n - 1) = {(len(c) - 1) / (len(V) - 1):.7f}')
check('[2] from the bottom-left cell, E hor(t)/t at t = 10^7 equals (w - 1)/(n - 1) to 10^-5 on four castles:', ok2b)


# [3] the reduced horizontal walk: from the foot of column i the next horizontal step goes right with
#     probability 1/2 for 1 < i < w, 1 at i = 1 and 0 at i = w (exact, absorbing the horizontal steps)
def next_right(c):
    N = nbrs(c)
    w = len(c)
    res = {}
    for i0 in range(1, w + 1):
        # unknowns: f(v) for v in column i0 = P(next horizontal step is to the right | at v)
        col = [(i0, j) for j in range(1, c[i0 - 1] + 1)]
        k = len(col)
        A = [[Fraction(0)] * k for _ in range(k)]
        b = [Fraction(0)] * k
        for a, v in enumerate(col):
            A[a][a] = Fraction(1)
            for u in N[v]:
                q = Fraction(1, len(N[v]))
                if u[0] == i0:
                    A[a][col.index(u)] -= q
                elif u[0] == i0 + 1:
                    b[a] += q
        for p_ in range(k):  # Gauss-Jordan
            piv = next(rr for rr in range(p_, k) if A[rr][p_] != 0)
            A[p_], A[piv], b[p_], b[piv] = A[piv], A[p_], b[piv], b[p_]
            for rr in range(k):
                if rr != p_ and A[rr][p_] != 0:
                    m = A[rr][p_] / A[p_][p_]
                    A[rr] = [x - m * y for x, y in zip(A[rr], A[p_])]
                    b[rr] -= m * b[p_]
        res[i0] = b[0] / A[0][0]
    return res


ok3, n3 = True, 0
for c in tree_castles(7, 4):
    w = len(c)
    if w < 2:
        continue
    f = next_right(c)
    ok3 &= f[1] == 1 and f[w] == 0 and all(f[i] == Fraction(1, 2) for i in range(2, w))
    n3 += 1
check(f'[3] the {n3} tree castles with 2 <= w <= 7, h <= 4: from column i the next horizontal step is to the '
      f'right with probability 1/2 inside, 1 at column 1 and 0 at column w:', ok3)


# [4] msd(t) = E hor(t), exactly, for t up to the distance d from the start column to the nearer end
def exact_moments(c, start, T):
    N = nbrs(c)
    dist = {start: Fraction(1)}
    Ehor, out = Fraction(0), []
    for t in range(1, T + 1):
        new = {}
        for v, p in dist.items():
            for u in N[v]:
                q = p / len(N[v])
                new[u] = new.get(u, 0) + q
                if u[0] != v[0]:
                    Ehor += q
        dist = new
        msd = sum(p * (v[0] - start[0]) ** 2 for v, p in dist.items())
        out.append((t, msd, Ehor))
    return out


random.seed(502)
ok4, fails_after = True, []
for _ in range(8):
    w = 13
    c = [1] * w
    for i in range(0, w, 2):
        c[i] = random.choice([1, 2, 3, 4, 5])
    c = tuple(c)
    i0 = 7
    d = min(i0 - 1, w - i0)
    res = exact_moments(c, (i0, 1), d + 4)
    ok4 &= all(m == e for t, m, e in res if t <= d)
    fails_after.append(next((t for t, m, e in res if m != e), None))
check(f'[4] eight tree castles of width 13 from the foot of column 7 (d = 6): msd(t) = E hor(t) exactly for '
      f't <= 6; first t with msd(t) != E hor(t): {fails_after}:', ok4)


# [5] the battlement (1, h, 1, h, ...), extended in both directions: one period is the path
#     a - b_0 - b_1 - ... - b_{h-1}, with a the height-1 cell, b_0 the foot of the tall column (two
#     horizontal edges to a) and b_1..b_{h-1} its tooth; msd(t) = E hor(t) for every t
def battlement_W(h):
    W = np.zeros((h + 1, h + 1))
    W[0, 1] = W[1, 0] = 2
    for k in range(1, h):
        W[k, k + 1] = W[k + 1, k] = 1
    r = np.zeros(h + 1)
    r[0], r[1] = 1, 2 / 3
    return W, r


def battlement_moments(h, T):
    """E[X_t^2] and E[hor(t)] on the extended battlement from cell a, by dynamic programming in floats."""
    W, r = battlement_W(h)
    P = W / W.sum(axis=1, keepdims=True)
    # state (cell, displacement); horizontal steps: a -> b0 moves +-1, b0 -> a moves +-1
    M = np.zeros((h + 1, 2 * T + 3))
    M[0, T + 1] = 1
    Ehor, out = 0.0, []
    for t in range(1, T + 1):
        new = np.zeros_like(M)
        new[1, 1:] += 0.5 * M[0, :-1]; new[1, :-1] += 0.5 * M[0, 1:]
        new[0, 1:] += (1 / 3) * M[1, :-1]; new[0, :-1] += (1 / 3) * M[1, 1:]
        Ehor += M[0].sum() + (2 / 3) * M[1].sum()
        if h >= 2:
            new[2] += (1 / 3) * M[1]
            for k in range(2, h + 1):
                if k + 1 <= h:
                    new[k + 1] += P[k, k + 1] * M[k]
                new[k - 1] += P[k, k - 1] * M[k]
        M = new
        x = np.arange(-T - 1, T + 2)
        out.append((t, float((M.sum(axis=0) * x ** 2).sum()), Ehor))
    return out


ok5 = True
for h in [2, 3, 7]:
    res = battlement_moments(h, 300)
    ok5 &= all(abs(m - e) < 1e-9 * max(1, e) for _, m, e in res)
check('[5] extended battlements h = 2, 3, 7, t <= 300: E[X_t^2] = E hor(t) to 10^-9:', ok5)

C_win = 4 * sqrt(2 / pi)
ok5b = True
for h in [11, 101, 1001]:
    W, r = battlement_W(h)
    ts = [10 ** k for k in range(1, 10)]
    E = expected_hor(W, 0, r, ts)
    Ep = expected_hor(W, 0, r, [int(t * 1.1) for t in ts])
    Em = expected_hor(W, 0, r, [int(t / 1.1) for t in ts])
    tx = 8 * (h + 1) ** 2 / pi
    print(f'[5] battlement h = {h}: crossover 8(h + 1)^2/pi = {tx:.4g}; rate 2/(h + 1) = {2 / (h + 1):.6f}')
    print('      t        E hor(t)      local exponent   E hor/sqrt(t)   E hor/t     E hor/(4 sqrt(2t/pi))   E hor (h + 1)/(2t)')
    for t, e, ep, em in zip(ts, E, Ep, Em):
        gam = (log(ep) - log(em)) / (log(int(t * 1.1)) - log(int(t / 1.1)))
        print(f'    10^{round(log(t, 10))}  {e:14.6g}  {gam:10.4f}      {e / sqrt(t):10.5f}    {e / t:10.6f}'
              f'    {e / (4 * sqrt(2 * t / pi)):10.4f}            {e * (h + 1) / (2 * t):10.4f}')
    ok5b &= abs(E[-1] / ts[-1] - 2 / (h + 1)) < 1e-3 * 2 / (h + 1) if h <= 101 else True
print(f'    4 sqrt(2/pi) = {C_win:.5f}')
for h in [101, 1001, 2001]:
    W, r = battlement_W(h)
    tx = 8 * (h + 1) ** 2 / pi
    e, ep, em = expected_hor(W, 0, r, [round(tx), round(tx * 1.1), round(tx / 1.1)])
    gam = (log(ep) - log(em)) / (log(round(tx * 1.1)) - log(round(tx / 1.1)))
    print(f'[5] h = {h}: at t = 8(h + 1)^2/pi = {round(tx)}, E hor(t) = {e:.6g} against the asymptotes '
          f'{C_win * sqrt(tx):.6g} = {2 * tx / (h + 1):.6g} (ratio {e / (C_win * sqrt(tx)):.4f}), local exponent {gam:.4f}')
W, r = battlement_W(2001)
ts = [10 ** 3, 10 ** 4, 10 ** 5]
E = expected_hor(W, 0, r, ts)
sl = sqrt_slope(E, ts)
ok5b &= abs(sl[-1] - C_win) < 0.005
print('[5] battlement h = 2001: E hor(t)/sqrt(t) at t = 10^3, 10^4, 10^5:', [round(e / sqrt(t), 5) for e, t in zip(E, ts)],
      '; slopes in sqrt(t) between them:', [round(s, 5) for s in sl],
      '; E hor(t) - 4 sqrt(2t/pi):', [round(e - C_win * sqrt(t), 3) for e, t in zip(E, ts)])
check('[5] E hor(t)/t -> 2/(h + 1) at t = 10^9 for h = 11, 101, and the slope of E hor(t) in sqrt(t) between '
      't = 10^4 and 10^5 within 0.005 of 4 sqrt(2/pi) at h = 2001:', ok5b)


# [6] the same machinery on the combs of the sources: two-sided teeth of N cells at every backbone site
#     (Mendez et al., q = 1/2: x^2 = t/(1 + 2N); Pach-Tardos and Mendez et al., N = infinity:
#     E a ~ sqrt(2/pi) sqrt(t)); one-sided teeth of l cells at every site (Yuste et al., theta = 1/3 and a
#     walker that steps back at the end of a tooth: x^2 = t/(1 + l))
def two_sided_W(N_):
    # one period: backbone cell 0 (self-loop of weight 2 for its two horizontal edges), teeth folded:
    # the up and down teeth are mirror images, so fold them into one path of N cells with weight 2
    W = np.zeros((N_ + 1, N_ + 1))
    W[0, 0] = 2
    W[0, 1] = W[1, 0] = 2
    for k in range(1, N_):
        W[k, k + 1] = W[k + 1, k] = 2
    r = np.zeros(N_ + 1)
    r[0] = 0.5
    return W, r


def one_sided_W(l):
    W = np.zeros((l + 1, l + 1))
    W[0, 0] = 2
    W[0, 1] = W[1, 0] = 1
    for k in range(1, l):
        W[k, k + 1] = W[k + 1, k] = 1
    r = np.zeros(l + 1)
    r[0] = 2 / 3
    return W, r


def expected_hor_loops(W, start, r, ts):
    # a self-loop of weight 2 stands for the two horizontal edges of one period: d(v) counts it twice
    d = W.sum(axis=1)
    return expected_hor(W, start, r, ts)


ok6 = True
for N_ in [2, 3, 6, 20]:
    W, r = two_sided_W(N_)
    t = 10 ** 8
    e = expected_hor_loops(W, 0, r, [t])[0] / t
    ok6 &= abs(e - 1 / (1 + 2 * N_)) < 1e-6
    print(f'    two-sided teeth N = {N_}: E hor(t)/t = {e:.8f}, 1/(1 + 2N) = 2 D (Mendez (3.3), (3.7)) = {1 / (1 + 2 * N_):.8f}')
for l in [1, 2, 5, 30]:
    W, r = one_sided_W(l)
    t = 10 ** 8
    e = expected_hor_loops(W, 0, r, [t])[0] / t
    ok6 &= abs(e - 1 / (1 + l)) < 1e-6
    print(f'    one-sided teeth l = {l}: E hor(t)/t = {e:.8f}, 1/(1 + l) (Yuste (24)-(26), theta = 1/3, t_R = 2l) = {1 / (1 + l):.8f}')
W, r = two_sided_W(4000)
ts = [10 ** 3, 10 ** 4, 10 ** 5]
E = expected_hor_loops(W, 0, r, ts)
sl = sqrt_slope(E, ts)
ok6 &= abs(sl[-1] - sqrt(2 / pi)) < 0.002
print('    two-sided teeth N = 4000: E hor(t)/sqrt(t) at 10^3, 10^4, 10^5 =',
      [round(e / sqrt(t), 5) for e, t in zip(E, ts)], '; slopes in sqrt(t):', [round(s, 5) for s in sl],
      f'; sqrt(2/pi) = {sqrt(2 / pi):.5f}')
check('[6] the backbone fraction reproduces the coefficients of Mendez et al. and Yuste et al., and the '
      'window constant sqrt(2/pi) of Pach-Tardos and Mendez et al.:', ok6)


# [7] one graph, six skylines: the class A of isospectral-castles, and B
A6 = [(1, 1, 1, 2, 1, 1, 2, 1, 1), (1, 1, 1, 2, 1, 1, 3, 1), (1, 1, 2, 1, 1, 2, 1, 2), (1, 1, 2, 1, 1, 4, 1),
      (1, 3, 1, 1, 2, 1, 2), (1, 3, 1, 1, 4, 1)]
B = (1, 1, 3, 1, 1, 1, 2, 1)
G = [nx.Graph(edges_of(c)) for c in A6]
ok7 = all(nx.is_isomorphic(G[0], g) for g in G) and not nx.is_isomorphic(G[0], nx.Graph(edges_of(B)))
ok7 &= all(is_tree(c) for c in A6 + [B])
rates = [Fraction(len(c) - 1, len(cells_of(c)) - 1) for c in A6]
print('[7] class A: widths', [len(c) for c in A6], 'rates', [str(x) for x in rates],
      '; B: width', len(B), 'rate', Fraction(len(B) - 1, len(cells_of(B)) - 1))
check('[7] the six skylines of class A have one graph, not that of B, and rates 4/5, 7/10, 7/10, 3/5, 3/5, 1/2:',
      ok7 and rates == [Fraction(4, 5), Fraction(7, 10), Fraction(7, 10), Fraction(3, 5), Fraction(3, 5), Fraction(1, 2)])

print('all checks passed:', ok_all)
