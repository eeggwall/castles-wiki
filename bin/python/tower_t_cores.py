# Towers of width w by blocks vs. (w+1)-core partitions by corners (Cho-Huh-Nam-Sohn, arXiv:2205.15554,
# Thm 3.3 and Prop 3.4), the Narayana-numerator formula, A160747 and A271942.
# Drafts: raw/oeis-pe502/xrefs/A160747-tower.md.  Needs sympy; A271942 b-file path as argv[1] (optional).
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

# 2. A160747 (data from the entry) == towers of width 5; closed form == cc(6, m) symbolically
A160747 = [1, 15, 85, 295, 771, 1681, 3235, 5685, 9325, 14491, 21561, 30955, 43135, 58605, 77911, 101641,
           130425, 164935, 205885, 254031, 310171, 375145, 449835, 535165, 632101, 741651, 864865, 1002835,
           1156695, 1327621, 1516831, 1725585, 1955185, 2206975]
assert towers(5, 12) == A160747[:13]
castles5 = [0] * 14  # castles of width 5 (column heights >= 1) by blocks; blocks = h(1) + rises
for h in product(range(1, 14), repeat=5):
    b = blocks(h)
    if b <= 13: castles5[b] += 1
assert castles5[1:] == A160747[:13]
assert A160747 == [narayana_form(5, n) for n in range(len(A160747))]
m = sp.symbols('m')
Nm = lambda i: sp.binomial(m, i) * sp.binomial(m, i - 1) / m
cc6 = sum(Nm(i) * sp.binomial(6 + 2 * m - 2 * i, 2 * m) for i in (1, 2, 3))
closed = 1 + sp.Rational(7, 4) * m * (m + 1) * (m**2 + m + 2)
assert sp.simplify(sp.expand_func(cc6) - closed) == 0
print("A160747: data == towers(5) for n<=12 == castles of width 5 with n+1 blocks for n<=12 == Narayana form for all 34 terms;"
      " cc(6, m) == 1 + 7m(m+1)(m^2+m+2)/4")

# 3. 6-cores with m corners by direct enumeration of partitions (corners = distinct parts)
def partitions(n, mx=None):
    if mx is None: mx = n
    if n == 0: yield (); return
    for k in range(min(n, mx), 0, -1):
        for p in partitions(n - k, k): yield (k,) + p

def hooks(p):
    conj = [sum(1 for x in p if x > j) for j in range(p[0])] if p else []
    return [p[i] - j - 1 + conj[j] - i - 1 + 1 for i in range(len(p)) for j in range(p[i])]

S, M = 60, 3
count, biggest = [0] * (M + 1), [0] * (M + 1)
for n in range(S + 1):
    for p in partitions(n):
        k = len(set(p))
        if k <= M and 6 not in hooks(p):
            count[k] += 1; biggest[k] = max(biggest[k], n)
assert count == A160747[:M + 1], count
print(f"6-cores with m corners, m<={M}, all sizes <= {S}: {count} (largest sizes {biggest}) == A160747")

# 4. A160747(n) == A271942(n+6, 5): bargraphs of width 5 and semiperimeter n+6 (heights c_i + 1)
if len(sys.argv) > 1:
    T = {}
    rows = [tuple(map(int, l.split())) for l in open(sys.argv[1]) if l.strip() and not l.startswith('#')]
    vals, i, s = [v for _, v in rows], 0, 2
    while i + s - 1 <= len(vals):  # row s (s >= 2) has s - 1 entries, k = 1..s-1
        for k in range(1, s): T[(s, k)] = vals[i + k - 1]
        i += s - 1; s += 1
    assert all(T[(n + 6, 5)] == A160747[n] for n in range(len(A160747)))
    print(f"A271942(n+6, 5) == A160747(n) for n < {len(A160747)}")
