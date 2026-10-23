# Towers of width w by blocks vs. (w+1)-core partitions by corners (Cho-Huh-Nam-Sohn, arXiv:2205.15554,
# Thm 3.3 and Prop 3.4), the Narayana-numerator formula, A160747, A063490, A005891,
# A005408, A271942, and the A001263 castle formula for every width from Deutsch-Elizalde's equation.
# Drafts: raw/oeis-pe502/xrefs/A160747-tower.md, A063490-, A005891-, A005408-, A001263-tower.md.  Needs sympy; A271942 b-file path as argv[1] (optional).
import sys
from itertools import product
from math import comb
import sympy as sp

def N(n, k):  # Narayana number, A001263; N(n, k) = 0 outside 1 <= k <= n
    return comb(n, k) * comb(n, k - 1) // n if 1 <= k <= n else 0

def blocks(c):  # tower blocks: c_1 + Sum_{i>=2} max(0, c_i - c_{i-1})
    return c[0] + sum(max(0, b - a) for a, b in zip(c, c[1:]))

def towers(w, B):  # counts by blocks b = 0..B (heights never exceed the block count)
    t = [0] * (B + 1)
    for c in product(range(B + 1), repeat=w):
        b = blocks(c)
        if b <= B: t[b] += 1
    return t

narayana_form = lambda w, b: sum(N(w, k) * comb(b + w - k, w - 1) for k in range(1, w + 1))
cc = lambda t, m: sum(N(m, i) * comb(t + 2 * m - 2 * i, 2 * m) for i in range(1, min(m, t // 2) + 1))  # Prop 3.4, m >= 1

# 1. towers == Narayana-numerator formula == cc(w+1, b)
for w, B in [(1, 12), (2, 12), (3, 12), (4, 12), (5, 12), (6, 9)]:
    t = towers(w, B)
    assert t == [narayana_form(w, b) for b in range(B + 1)], w
    assert t[1:] == [cc(w + 1, b) for b in range(1, B + 1)], w
    print(f"w={w}: towers by blocks b<={B} == Narayana form == cc({w+1}, b): {t[:8]} ...")

# 2. entry data == castles of width t-1 by blocks == Narayana form; closed form == cc(t, m) symbolically.
#    data[j] is the term for j corners and j + 1 castle blocks (A160747 offset 0, A063490 offset 1).
m = sp.symbols('m')
ENTRIES = {  # name: (t, data from the entry, closed form in the number of corners m)
    'A160747': (6, [1, 15, 85, 295, 771, 1681, 3235, 5685, 9325, 14491, 21561, 30955, 43135, 58605, 77911,
                    101641, 130425, 164935, 205885, 254031, 310171, 375145, 449835, 535165, 632101, 741651,
                    864865, 1002835, 1156695, 1327621, 1516831, 1725585, 1955185, 2206975],
                1 + sp.Rational(7, 4) * m * (m + 1) * (m**2 + m + 2)),                       # Mathar, n = m
    'A063490': (5, [1, 10, 40, 105, 219, 396, 650, 995, 1445, 2014, 2716, 3565, 4575, 5760, 7134, 8711,
                    10505, 12530, 14800, 17329, 20131, 23220, 26610, 30315, 34349, 38726, 43460, 48565,
                    54055, 59944, 66246, 72975, 80145, 87770, 95864, 104441, 113515, 123100, 133210,
                    143859, 155061],
                (2 * (m + 1) - 1) * (7 * (m + 1)**2 - 7 * (m + 1) + 6) / 6),                  # the name, n = m + 1
    'A005891': (4, [1, 6, 16, 31, 51, 76, 106, 141, 181, 226, 276, 331, 391, 456, 526, 601, 681, 766, 856,
                    951, 1051, 1156, 1266, 1381, 1501, 1626, 1756, 1891, 2031, 2176, 2326, 2481, 2641,
                    2806, 2976, 3151, 3331, 3516, 3706, 3901, 4101, 4306, 4516, 4731, 4951, 5176, 5406],
                (5 * m**2 + 5 * m + 2) / 2),                                                  # the name, n = m
    'A005408': (3, list(range(1, 132, 2)), 2 * m + 1),                                        # n = m
}
Nm = lambda i: sp.binomial(m, i) * sp.binomial(m, i - 1) / m
for name, (t, data, closed) in ENTRIES.items():
    w = t - 1
    castles = [0] * 14  # castles of width w (column heights >= 1) by blocks; blocks = c(1) + rises
    for c in product(range(1, 14), repeat=w):
        b = blocks(c)
        if b <= 13: castles[b] += 1
    assert castles[1:] == data[:13] == towers(w, 12), name
    assert data == [narayana_form(w, j) for j in range(len(data))], name
    assert data[1:] == [cc(t, j) for j in range(1, len(data))], name
    cct = sum(Nm(i) * sp.binomial(t + 2 * m - 2 * i, 2 * m) for i in range(1, t // 2 + 1))
    assert sp.simplify(sp.expand_func(cct) - closed) == 0, name
    print(f"{name}: data == castles of width {w} with j+1 blocks == towers for j<=12; == Narayana form and"
          f" cc({t}, j) for all {len(data)} terms; cc({t}, m) == closed form symbolically")

# 3. t-cores with m corners by direct enumeration of partitions (corners = distinct parts)
def partitions(n, mx=None):
    if mx is None: mx = n
    if n == 0: yield (); return
    for k in range(min(n, mx), 0, -1):
        for p in partitions(n - k, k): yield (k,) + p

def hooks(p):
    conj = [sum(1 for x in p if x > j) for j in range(p[0])] if p else []
    return [p[i] - j - 1 + conj[j] - i - 1 + 1 for i in range(len(p)) for j in range(p[i])]

S, M = 60, 3
count = {name: [0] * (M + 1) for name in ENTRIES}
biggest = {name: [0] * (M + 1) for name in ENTRIES}
for n in range(S + 1):
    for p in partitions(n):
        k = len(set(p))
        if k > M: continue
        hs = set(hooks(p))
        for name, (t, _, _) in ENTRIES.items():
            if t not in hs:
                count[name][k] += 1; biggest[name][k] = max(biggest[name][k], n)
for name, (t, data, _) in ENTRIES.items():
    assert count[name] == data[:M + 1], (name, count[name])
    print(f"{t}-cores with m corners, m<={M}, all sizes <= {S}: {count[name]} (largest sizes {biggest[name]}) == {name}")

# 4. data[j] == A271942(t + j, t - 1): a castle is a bargraph, semiperimeter = width + blocks = (t-1) + (j+1)
if len(sys.argv) > 1:
    T = {}
    rows = [tuple(map(int, l.split())) for l in open(sys.argv[1]) if l.strip() and not l.startswith('#')]
    vals, i, s = [v for _, v in rows], 0, 2
    while i + s - 1 <= len(vals):  # row s (s >= 2) has s - 1 entries, k = 1..s-1
        for k in range(1, s): T[(s, k)] = vals[i + k - 1]
        i += s - 1; s += 1
    for name, (t, data, _) in ENTRIES.items():
        assert all(T[(t + j, t - 1)] == data[j] for j in range(len(data))), name
        print(f"{name}: term j == A271942({t} + j, {t - 1}) for all {len(data)} terms")
    # the A001263 formula line: Sum_k N(n,k) C(m+n-k-1, n-1) == A271942(n+m, n), every b-file term
    assert all(narayana_form(n, s - n - 1) == v for (s, n), v in T.items())  # m blocks = tower with m - 1
    print(f"A001263: Sum_k N(n,k) C(m+n-k-1, n-1) == A271942(n+m, n) for all {len(T)} b-file terms (n+m <= {max(s for s, _ in T)})")

# 5. A001263: castles of width w by blocks have g.f. Sum_k N(w,k) y^k / (1-y)^w for every w.
#    Deutsch-Elizalde: the castle (bargraph) g.f. B(x, y), x width, y blocks, solves x B^2 - (1-x-y-xy) B + xy = 0.
#    Dyck paths by semilength u and peaks t: C = 1 + u C (C - 1 + t), with C - 1 = Sum_w u^w Sum_k N(w,k) t^k.
#    With u = x/(1-y), t = y and F = C - 1 the Dyck equation is (1-y) F = x (F+1)(F+y), the same quadratic.
x, y, F = sp.symbols('x y F')
assert sp.expand(x * F**2 - (1 - x - y - x * y) * F + x * y - (x * (F + 1) * (F + y) - (1 - y) * F)) == 0
W = 8
B = sp.Integer(0)
for _ in range(W + 1):  # power-series solution in x of (1-y) B = x (B^2 + (1+y) B + y), truncated at x^W
    B = sp.series(sp.expand(x * (B**2 + (1 + y) * B + y) / (1 - y)), x, 0, W + 1).removeO()
for w in range(1, W + 1):
    assert sp.simplify(B.coeff(x, w) - sum(N(w, k) * y**k for k in range(1, w + 1)) / (1 - y)**w) == 0, w
print(f"A001263: Deutsch-Elizalde equation == Dyck-by-peaks equation at u = x/(1-y); "
      f"[x^w] B = Sum_k N(w,k) y^k/(1-y)^w for w <= {W}")
