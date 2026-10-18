# Tree skylines and tree castles counted by width and area: Equations (1)-(4), the height-2 triangle,
# Tables 1 and 2 with their OEIS shifts, denominators and growth constants by area, the composition,
# bit-string and 010-avoiding bijections, and the castles of height 2 with tower spacing at least 2.
# Page: wiki/pages/tree-castle-by-area.md.  Needs sympy.  OEIS data below: the full data field of each entry, read 2026-10-17.
from itertools import product
from math import comb
import sympy as sp

q, x = sp.symbols('q x')
OEIS = {  # A-number: (offset, data)
    'A000930': (0, [1, 1, 1, 2, 3, 4, 6, 9, 13, 19, 28, 41, 60, 88, 129, 189, 277, 406, 595, 872, 1278, 1873, 2745, 4023, 5896, 8641, 12664, 18560, 27201, 39865, 58425, 85626, 125491, 183916, 269542, 395033, 578949, 848491, 1243524, 1822473, 2670964, 3914488, 5736961, 8407925]),
    'A006498': (0, [1, 1, 1, 2, 4, 6, 9, 15, 25, 40, 64, 104, 169, 273, 441, 714, 1156, 1870, 3025, 4895, 7921, 12816, 20736, 33552, 54289, 87841, 142129, 229970, 372100, 602070, 974169, 1576239, 2550409, 4126648, 6677056, 10803704, 17480761, 28284465, 45765225, 74049690, 119814916]),
    'A000570': (1, [1, 1, 2, 4, 7, 11, 18, 31, 53, 89, 149, 251, 424, 715, 1204, 2028, 3418, 5761, 9708, 16358, 27565, 46452, 78279, 131910, 222285, 374581, 631222, 1063696, 1792472, 3020560, 5090059, 8577449, 14454177, 24357268, 41045336, 69167021, 116555915]),
    'A079816': (0, [1, 1, 1, 2, 4, 7, 12, 20, 34, 59, 102, 175, 300, 515, 885, 1521, 2613, 4488, 7709, 13243, 22750, 39081, 67134, 115324, 198107, 340315, 584604, 1004250, 1725130, 2963480, 5090756, 8745055, 15022519, 25806135, 44330556, 76152366, 130816831]),
    'A189593': (1, [1, 1, 2, 4, 7, 12, 21, 36, 62, 108, 188, 326, 565, 980, 1700, 2949, 5116, 8875, 15395, 26705, 46325, 80360, 139400, 241816, 419476, 727661, 1262267, 2189644, 3798357, 6588977, 11429841, 19827246, 34394152, 59663238, 103497303, 179535876]),
    'A189600': (1, [1, 1, 2, 4, 7, 12, 21, 37, 64, 111, 194, 339, 591, 1030, 1796, 3132, 5461, 9522, 16604, 28953, 50485, 88030, 153498, 267655, 466710, 813802, 1419027, 2474358, 4314538, 7523260, 13118310, 22874400, 39886095, 69549390, 121273283, 211464244]),
    'A005251': (0, [0, 1, 1, 1, 2, 4, 7, 12, 21, 37, 65, 114, 200, 351, 616, 1081, 1897, 3329, 5842, 10252, 17991, 31572, 55405, 97229, 170625, 299426, 525456, 922111, 1618192, 2839729, 4983377, 8745217, 15346786, 26931732, 47261895, 82938844, 145547525, 255418101, 448227521]),
    'A077868': (0, [1, 2, 3, 5, 8, 12, 18, 27, 40, 59, 87, 128, 188, 276, 405, 594, 871, 1277, 1872, 2744, 4022, 5895, 8640, 12663, 18559, 27200, 39864, 58424, 85625, 125490, 183915, 269541, 395032, 578948, 848490, 1243523, 1822472, 2670963, 3914487, 5736960, 8407924, 12322412]),
    'A000071': (1, [0, 0, 1, 2, 4, 7, 12, 20, 33, 54, 88, 143, 232, 376, 609, 986, 1596, 2583, 4180, 6764, 10945, 17710, 28656, 46367, 75024, 121392, 196417, 317810, 514228, 832039, 1346268, 2178308, 3524577, 5702886, 9227464, 14930351, 24157816, 39088168, 63245985, 102334154]),
    'A001045': (0, [0, 1, 1, 3, 5, 11, 21, 43, 85, 171, 341, 683, 1365, 2731, 5461, 10923, 21845, 43691, 87381, 174763, 349525, 699051, 1398101, 2796203, 5592405, 11184811, 22369621, 44739243, 89478485, 178956971, 357913941, 715827883, 1431655765, 2863311531, 5726623061, 11453246123]),
    'A006130': (0, [1, 1, 4, 7, 19, 40, 97, 217, 508, 1159, 2683, 6160, 14209, 32689, 75316, 173383, 399331, 919480, 2117473, 4875913, 11228332, 25856071, 59541067, 137109280, 315732481, 727060321, 1674257764, 3855438727, 8878212019, 20444528200, 47079164257, 108412748857, 249650241628]),
    'A006131': (0, [1, 1, 5, 9, 29, 65, 181, 441, 1165, 2929, 7589, 19305, 49661, 126881, 325525, 833049, 2135149, 5467345, 14007941, 35877321, 91909085, 235418369, 603054709, 1544728185, 3956947021, 10135859761, 25963647845, 66507086889, 170361678269]),
}
def a(name, n):
    off, data = OEIS[name]
    return data[n - off]
def fib(n):
    f = [0, 1]
    while len(f) <= n: f.append(f[-1] + f[-2])
    return f[n]
INF = 10**9

def tree(c): return all(min(u, v) < 2 for u, v in zip(c, c[1:]))
def comps(n, parts=None):
    if n == 0: yield (); return
    for k in range(1, n + 1):
        if parts is None or k in parts:
            for r in comps(n - k, parts): yield (k,) + r
def P(h): return sum(q**i for i in range(2, h + 1)) if h < INF else q**2 / (1 - q)

# [1] Equation (1) by width, Equation (2), and the counts at q = 1
for h in (2, 3, 4, 5):
    gf = sp.series((1 + P(h) * x) / (1 - q * x - q * P(h) * x**2), x, 0, 8).removeO()
    T = [sp.expand(gf.coeff(x, w)) for w in range(8)]
    for w in range(8):
        enum = sum(q**sum(c) for c in product(range(1, h + 1), repeat=w) if tree(c)) if w else sp.Integer(1)
        assert sp.expand(T[w] - enum) == 0, (h, w)
    assert sp.expand(T[1] - (q + P(h))) == 0
    assert all(sp.expand(T[w] - q * T[w - 1] - q * P(h) * T[w - 2]) == 0 for w in range(2, 8))
    T1 = [sum(1 for c in product(range(1, h + 1), repeat=w) if tree(c)) for w in range(13)]
    ref = {2: [fib(w + 2) for w in range(13)], 3: [a('A001045', w + 2) for w in range(13)],
           4: [a('A006130', w + 1) for w in range(13)], 5: [a('A006131', w + 1) for w in range(13)]}[h]
    assert T1 == ref, h
print("[1] Equation (1) = enumeration for w <= 7, h = 2..5; Equation (2) for w <= 7; at q = 1, w <= 12:"
      " F(w+2), A001045(w+2), A006130(w+1), A006131(w+1): True")

# [2] the height-2 triangle
for w in range(1, 12):
    sk = [c for c in product((1, 2), repeat=w) if tree(c) and max(c) == 2]
    for t in range(1, w + 1):
        assert sum(1 for c in sk if sum(c) - w == t) == comb(w - t + 1, t), (w, t)
    assert len(sk) == fib(w + 2) - 1 == a('A000071', w + 2), w
print("[2] tree castles of height 2: C(w - t + 1, t) and row sums F(w+2) - 1 = A000071(w+2), w <= 11: True")

# [3] Tables 1 and 2
def by_area(h, N):  # coefficient of q^A in G_h, A = 0..N: compositions of A + 1 into {1, 3, ..., h + 1}
    c = [1] + [0] * (N + 1)
    for n in range(1, N + 2):
        c[n] = c[n - 1] + sum(c[n - p] for p in range(3, min(h + 1, n) + 1))
    return [c[A + 1] for A in range(N + 1)]
TABLE1 = {2: [1, 2, 3, 4, 6, 9, 13, 19, 28, 41, 60, 88, 129, 189], 3: [1, 2, 4, 6, 9, 15, 25, 40, 64, 104, 169, 273, 441, 714],
          4: [1, 2, 4, 7, 11, 18, 31, 53, 89, 149, 251, 424, 715, 1204], 5: [1, 2, 4, 7, 12, 20, 34, 59, 102, 175, 300, 515, 885, 1521],
          6: [1, 2, 4, 7, 12, 21, 36, 62, 108, 188, 326, 565, 980, 1700], 7: [1, 2, 4, 7, 12, 21, 37, 64, 111, 194, 339, 591, 1030, 1796],
          8: [1, 2, 4, 7, 12, 21, 37, 65, 113, 197, 345, 604, 1056, 1846], INF: [1, 2, 4, 7, 12, 21, 37, 65, 114, 200, 351, 616, 1081, 1897]}
SHIFT = {2: ('A000930', 1), 3: ('A006498', 1), 4: ('A000570', 1), 5: ('A079816', 1), 6: ('A189593', 1), 7: ('A189600', 1), INF: ('A005251', 2)}
TABLE2 = {2: [0, 1, 2, 3, 5, 8, 12, 18, 27, 40, 59, 87, 128, 188], 3: [0, 0, 1, 2, 3, 6, 12, 21, 36, 63, 109, 185, 312, 525],
          4: [0, 0, 0, 1, 2, 3, 6, 13, 25, 45, 82, 151, 274, 490]}
sky = {A: [c for c in comps(A) if tree(c)] for A in range(1, 13)}
growth = {}
for h, row in TABLE1.items():
    G = sp.cancel((1 + P(h)) / (1 - q - q * P(h)))
    ser = sp.series(G, q, 0, 15).removeO()
    assert [int(ser.coeff(q, A)) for A in range(1, 15)] == row == by_area(h if h < INF else 60, 14)[1:], h
    assert [sum(1 for c in sky[A] if max(c) <= h) for A in range(1, 13)] == row[:12], h
    if h in SHIFT:
        name, s = SHIFT[h]; off, data = OEIS[name]
        N = len(data) - 1 + off - s
        assert by_area(h if h < INF else N + 2, N)[max(0, off - s):] == [a(name, A + s) for A in range(max(0, off - s), N + 1)], h
    den = sp.Poly(sp.fraction(G)[1], q); d = den.degree()
    rev = sp.Poly(sp.expand(q**d * den.as_expr().subs(q, 1 / q)), q)
    rev = rev if rev.LC() > 0 else -rev
    g = max(rev.nroots(n=15), key=abs)
    carrier = [f for f, e in sp.factor_list(rev.as_expr())[1] if abs(sp.N(f.subs(q, g), 30)) < 1e-12]
    growth[h] = g
    print(f"[3] h={'inf' if h == INF else h}: Table 1 row = Eq. (3) (A <= 14) = enumeration (A <= 12) = OEIS at its shift: True;"
          f" reversed denominator {sp.factor(rev.as_expr())}, growth constant by area {sp.N(g, 10)},"
          f" irreducible factor of degree {sp.degree(carrier[0], q)}")
hs = sorted(growth)
assert all(growth[u] < growth[v] for u, v in zip(hs, hs[1:]))
print("[3] growth constants by area increase with h: True")
for h, row in TABLE2.items():
    assert [sum(1 for c in sky[A] if max(c) == h) for A in range(1, 13)] == row[:12]
    assert [u - v for u, v in zip(TABLE1[h], TABLE1[h - 1] if h > 2 else [1] * 14)] == row
assert all(TABLE2[2][A - 1] == a('A077868', A - 2) == a('A000930', A + 1) - 1 for A in range(2, 15))
assert all(a('A006498', 2 * n) == fib(n + 1)**2 and a('A006498', 2 * n - 1) == fib(n + 1) * fib(n) for n in range(1, 10))
print("[3] Table 2 = enumeration (A <= 12) and differences of Table 1 rows; A077868(A - 2) = A000930(A + 1) - 1;"
      " A006498(2n) = F(n+1)^2, A006498(2n - 1) = F(n+1) F(n), n <= 9: True")

# [4] the bijections
def to_comp(c):
    aug = [1] + list(c); parts = []; i = 0
    while i < len(aug):
        if i + 1 < len(aug) and aug[i] == 1 and aug[i + 1] >= 2:
            parts.append(1 + aug[i + 1]); i += 2
        else:
            parts.append(aug[i]); i += 1
    return tuple(parts)
def from_comp(parts):
    aug = []
    for p in parts: aug += [1] if p == 1 else [1, p - 1]
    return tuple(aug[1:])
for h in range(2, 7):
    for A in range(1, 13):
        src = [c for c in sky[A] if max(c) <= h]
        img = {to_comp(c) for c in src}
        tgt = set(comps(A + 1, {1} | set(range(3, h + 2))))
        assert img == tgt and len(img) == len(src) and all(from_comp(to_comp(c)) == c for c in src), (h, A)
def to_bits(c): return ''.join('0' if v == 1 else '1' * v for v in c)
for h in (2, 3, 4, 5, INF):
    for n in range(1, 14):
        src = [c for c in comps(n) if tree(c) and max(c) <= h]
        tgt = {s for s in (''.join(b) for b in product('01', repeat=n))
               if all(2 <= len(r) <= h for r in s.split('0') if r)}
        assert {to_bits(c) for c in src} == tgt and len(src) == len(tgt), (h, n)
def to_010(c): return '1'.join('0' * (v - 1) for v in c)
for A in range(1, 13):
    img = [to_010(c) for c in sky[A]]
    tgt = {s for s in (''.join(b) for b in product('01', repeat=A - 1)) if '010' not in s}
    assert set(img) == tgt and len(img) == len(tgt), A
print("[4] composition map onto {1, 3, ..., h+1} with inverse (2 <= h <= 6, A <= 12); bit strings with runs of ones"
      " of length 2..h (h = 2..5 and unrestricted, n <= 13); strings of length A - 1 avoiding 010 (A <= 12): True")

# [5] castles of height 2 with tower spacing at least 2: every run of height-1 columns between two
#     height-2 columns has length at least 2
for w in range(1, 15):
    cnt = sum(1 for c in product((1, 2), repeat=w) if 2 in c
              and all(j - i == 1 or j - i >= 3 for i, j in zip([k for k in range(w) if c[k] == 2], [k for k in range(w) if c[k] == 2][1:])))
    assert cnt == a('A005251', w + 3) - 1, w
print("[5] castles of height 2 with tower spacing at least 2 = A005251(w + 3) - 1, w <= 14: True")

# [6] the tournament recurrence: A000570's characteristic polynomial is the h = 4 reversed denominator
assert all(a('A000570', n) == a('A000570', n - 1) + a('A000570', n - 3) + a('A000570', n - 4) + a('A000570', n - 5) for n in range(6, 24))
print("[6] A000570(n) = A000570(n-1) + A000570(n-3) + A000570(n-4) + A000570(n-5) for 6 <= n <= 23, growth", sp.N(growth[4], 10), ": True")
