# Hilbert castles: castles in which neighboring columns never differ in height by exactly 1, the rule
# J - A_path, which allows exactly the neighbor pairs that the zig-zag rule A_path forbids.
# Checks: the Hilbert duality G_M(x) G_{J-M}(-x) = 1 on every rule of height at most 4 and on random rules of
# heights 5 to 7, by width and by width and area, and the pairing of cuts behind it; the examples on the page;
# the Hilbert strips against the OEIS; the Hilbert castles by count, closed form, generating function, growth
# and block parity; the path on four heights against its complement; the m-disparate castles, the dual of the
# (m - 1)-smooth rule; the tree skylines, the dual of the strips whose columns all have height at least 2.
# Page: wiki/pages/hilbert-castles.md.  OEIS data below: the data fields, read 2026-10-28.
import math
import random
from itertools import permutations, product
import mpmath
import numpy as np
import sympy as sp

OEIS = {
    'A083318': (0, [1, 3, 5, 9, 17, 33, 65, 129, 257, 513, 1025, 2049, 4097, 8193, 16385, 32769, 65537,
                131073, 262145, 524289, 1048577, 2097153, 4194305, 8388609, 16777217, 33554433, 67108865,
                134217729, 268435457, 536870913, 1073741825, 2147483649]),
    'A126358': (0, [1, 4, 10, 26, 68, 178, 466, 1220, 3194, 8362, 21892, 57314, 150050, 392836, 1028458,
                2692538, 7049156, 18454930, 48315634, 126491972, 331160282, 866988874, 2269806340, 5942430146,
                15557484098, 40730022148, 106632582346, 279167724890, 730870592324]),
    'A287804': (0, [1, 5, 17, 59, 205, 713, 2481, 8635, 30057, 104629, 364225, 1267923, 4413861, 15365465,
                53490097, 186209299, 648230545, 2256616133, 7855718641, 27347281995, 95201200637,
                331413874569, 1153716087665, 4016309864843, 13981555011321, 48672509644725]),
    'A287806': (0, [1, 6, 26, 114, 500, 2194, 9628, 42252, 185422, 813722, 3571010, 15671340, 68773514,
                301811860, 1324498252, 5812546998, 25508302906, 111942925778, 491260382084, 2155891150146,
                9461106209228, 41519967599596, 182209952129086, 799626506818554, 3509152727035810]),
    'A287808': (0, [1, 7, 37, 197, 1049, 5587, 29757, 158491, 844153, 4496123, 23947233, 127547675, 679344041,
                3618320227, 19271886609, 102645866251, 546712113769, 2911896468083, 15509334488577,
                82605772190267, 439974623297369, 2343391557436483, 12481365289466289]),
    'A287812': (0, [1, 8, 50, 314, 1972, 12386, 77796, 488636, 3069120, 19277130, 121079578, 760500364,
                4776699874, 30002433636, 188445170924, 1183623397912, 7434334035874, 46695023649050,
                293291264969380, 1842161313673506, 11570608166423524, 72674945645197500]),
    'A287816': (0, [1, 9, 65, 471, 3413, 24733, 179233, 1298853, 9412437, 68209395, 494295113, 3582023557,
                25957960001, 188110345129, 1363185009337, 9878634630295, 71587804656589, 518777540353453,
                3759441118026705, 27243657291488469, 197427447142906157, 1430703538380753875]),
    'A287825': (0, [1, 10, 82, 674, 5540, 45538, 374316, 3076828, 25291120, 207889674, 1708825732,
                14046322404, 115458919774, 949057110644, 7801124426174, 64124215108032, 527092600834054,
                4332631742719370, 35613662169258228, 292739611493034596, 2406281042646218328]),
    'A287832': (0, [1, 11, 101, 929, 8545, 78599, 722973, 6650087, 61169169, 562649373, 5175390189,
                47604538285, 437878494689, 4027716327495, 37047945974857, 340776308298291, 3134546038698889,
                28832341420057365, 265207115001514409, 2439441626426418609, 22438596523731989473]),
    'A000225': (0, [0, 1, 3, 7, 15, 31, 63, 127, 255, 511, 1023, 2047, 4095, 8191, 16383, 32767, 65535,
                131071, 262143, 524287, 1048575, 2097151, 4194303, 8388607, 16777215, 33554431, 67108863,
                134217727, 268435455, 536870911, 1073741823, 2147483647, 4294967295, 8589934591]),
    'A019274': (1, [0, 0, 2, 4, 8, 14, 24, 40, 66, 108, 176, 286, 464, 752, 1218, 1972, 3192, 5166, 8360,
                13528, 21890, 35420, 57312, 92734, 150048, 242784, 392834, 635620, 1028456, 1664078, 2692536,
                4356616, 7049154, 11405772, 18454928, 29860702, 48315632]),
}


def rule(h, allow):
    """The 0/1 rule matrix on the heights 1..h: entry (a, b) is 1 when allow(a, b)."""
    return [[1 if allow(a, b) else 0 for b in range(1, h + 1)] for a in range(1, h + 1)]


def dual(M):
    return [[1 - e for e in row] for row in M]


def strip_series(M, D):
    """N_M(0..D): the strips of width w under the rule M, with the empty strip at w = 0."""
    h = len(M)
    out = [1]
    v = [1] * h
    for w in range(1, D + 1):
        out.append(sum(v))
        v = [sum(v[a] * M[a][b] for a in range(h)) for b in range(h)]
    return out


def poly_add(p, r):
    n = max(len(p), len(r))
    return [(p[i] if i < len(p) else 0) + (r[i] if i < len(r) else 0) for i in range(n)]


def poly_mul(p, r):
    out = [0] * (len(p) + len(r) - 1)
    for i, a in enumerate(p):
        if a:
            for j, b in enumerate(r):
                out[i + j] += a * b
    return out


def poly_trim(p):
    while len(p) > 1 and p[-1] == 0:
        p = p[:-1]
    return p


def area_series(M, D):
    """The strips of M by width (index) and area (a polynomial in q), the empty strip included."""
    h = len(M)
    out = [[1]]
    v = [[0] * a + [1] for a in range(1, h + 1)]          # a column of height a has weight q^a
    for w in range(1, D + 1):
        tot = [0]
        for p in v:
            tot = poly_add(tot, p)
        out.append(poly_trim(tot))
        nv = []
        for b in range(h):
            acc = [0]
            for a in range(h):
                if M[a][b]:
                    acc = poly_add(acc, v[a])
            nv.append([0] * (b + 1) + acc)
        v = nv
    return out


def dual_product_is_one(G, H):
    """True when G(x) H(-x) = 1 up to x^D, for integer series G and H."""
    D = len(G) - 1
    return all(sum(G[i] * H[n - i] * (-1) ** (n - i) for i in range(n + 1)) == (1 if n == 0 else 0)
               for n in range(D + 1))


def dual_product_is_one_area(G, H):
    D = len(G) - 1
    for n in range(D + 1):
        acc = [0]
        for i in range(n + 1):
            term = poly_mul(G[i], H[n - i])
            if (n - i) % 2:
                term = [-t for t in term]
            acc = poly_add(acc, term)
        if poly_trim(acc) != ([1] if n == 0 else [0]):
            return False
    return True


def is_strip(c, M):
    return all(M[c[i] - 1][c[i + 1] - 1] for i in range(len(c) - 1))


def blocks(c):
    return c[0] + sum(max(0, c[i] - c[i - 1]) for i in range(1, len(c)))


def draw(c):
    h = max(c)
    return ' '.join(''.join('#' if ci >= r else '.' for ci in c) for r in range(h, 0, -1))


def hilbert(h):
    return rule(h, lambda a, b: abs(a - b) != 1)


def zigzag(h):
    return rule(h, lambda a, b: abs(a - b) == 1)


def smooth(h, m):
    return rule(h, lambda a, b: abs(a - b) <= m)


def disparate(h, m):
    return rule(h, lambda a, b: abs(a - b) >= m)


def castle_counts(make, h, W):
    """Castles of height h (strips on 1..h minus strips on 1..h-1), widths 1..W."""
    top = strip_series(make(h), W)
    low = strip_series(make(h - 1), W) if h > 1 else [1] + [0] * W
    return [top[w] - low[w] for w in range(1, W + 1)]


def brute_castles(M, w, h):
    return sum(1 for c in product(range(1, h + 1), repeat=w) if max(c) == h and is_strip(c, M))


def parity_counts(M, h, W):
    """Even-block and odd-block castles of height h under M (restricted to 1..h-1 below), widths 1..W:
    a transfer count with the block sign (-1)^c_1 and (-1)^max(0, b - a) per step."""
    def signed_and_all(Mh, hh, sign):
        out = []
        v = [(sign ** a) for a in range(1, hh + 1)]
        for w in range(1, W + 1):
            out.append(sum(v))
            v = [sum(v[a] * Mh[a][b] * sign ** max(0, b - a) for a in range(hh)) for b in range(hh)]
        return out
    sub = [row[:h - 1] for row in M[:h - 1]]
    A = [x - y for x, y in zip(signed_and_all(M, h, 1), signed_and_all(sub, h - 1, 1) if h > 1 else [0] * W)]
    S = [x - y for x, y in zip(signed_and_all(M, h, -1), signed_and_all(sub, h - 1, -1) if h > 1 else [0] * W)]
    return [(a + s) // 2 for a, s in zip(A, S)], [(a - s) // 2 for a, s in zip(A, S)]


def gf(M):
    """The rational function G_M(x) = 1 + x 1^T (I - xM)^{-1} 1, as N(x)/det(I - xM) with N of degree <= h:
    N is the strip series times det(I - xM), checked to vanish from x^(h+1) to x^(3h)."""
    h = len(M)
    det = sp.Poly(sp.expand(x ** h * sp.Matrix(M).charpoly(x).as_expr().subs(x, 1 / x)), x)
    s = strip_series(M, 3 * h)
    prod_ = sp.Poly(sum(c * x ** i for i, c in enumerate(s)), x) * det
    coeffs = [prod_.coeff_monomial(x ** i) for i in range(3 * h + 1)]
    assert all(c == 0 for c in coeffs[h + 1:3 * h + 1])
    return sp.cancel(sum(c * x ** i for i, c in enumerate(coeffs[:h + 1])) / det.as_expr())


x = sp.symbols('x')
q = sp.symbols('q')
F = [0, 1]
for _ in range(200):
    F.append(F[-1] + F[-2])
random.seed(20261028)


# [1] Hilbert duality G_M(x) G_{J-M}(-x) = 1.
D = 10
total = ok = 0
for h in range(1, 5):
    n = h * h
    series = {}
    for mask in range(1 << n):
        M = [[(mask >> (a * h + b)) & 1 for b in range(h)] for a in range(h)]
        series[mask] = strip_series(M, D if h < 4 else 8)
    full = (1 << n) - 1
    for mask in range(1 << n):
        total += 1
        ok += dual_product_is_one(series[mask], series[full ^ mask])
print(f'[1] G_M(x) G_(J-M)(-x) = 1 up to x^10 (x^8 at h = 4), every rule with h <= 4: {ok == total}, {total} rules')
for h, trials, D in ((5, 300, 14), (6, 300, 14), (7, 300, 12)):
    good = 0
    for _ in range(trials):
        M = [[random.randint(0, 1) for _ in range(h)] for _ in range(h)]
        good += dual_product_is_one(strip_series(M, D), strip_series(dual(M), D))
    print(f'[1] random rules of height {h}, up to x^{D}: {good} of {trials}')
total = ok = 0
for h in range(1, 4):
    n = h * h
    for mask in range(1 << n):
        M = [[(mask >> (a * h + b)) & 1 for b in range(h)] for a in range(h)]
        total += 1
        ok += dual_product_is_one_area(area_series(M, 8), area_series(dual(M), 8))
good = 0
for h in (4, 5):
    for _ in range(100):
        M = [[random.randint(0, 1) for _ in range(h)] for _ in range(h)]
        good += dual_product_is_one_area(area_series(M, 7), area_series(dual(M), 7))
print(f'[1] by width and area (q^a for a column of height a): every rule with h <= 3 up to x^8: {ok == total}, '
      f'{total} rules; 100 random rules at h = 4 and at h = 5 up to x^7: {good} of 200')
# the pairing: for a word c, the cuts k with c[:k] a strip of J - M and c[k:] a strip of M come in adjacent pairs
good = cases = 0
for h in (2, 3, 4):
    for _ in range(40):
        M = [[random.randint(0, 1) for _ in range(h)] for _ in range(h)]
        N = dual(M)
        for w in range(1, 7):
            for c in product(range(1, h + 1), repeat=w):
                cuts = [k for k in range(w + 1) if is_strip(c[:k], N) and is_strip(c[k:], M)]
                cases += 1
                good += (len(cuts) in (0, 2)) and (len(cuts) == 0 or cuts[1] == cuts[0] + 1)
print(f'[1] the valid cuts of every word of length 1..6 under 120 random rules (h = 2, 3, 4) are none or two '
      f'neighboring cuts: {good == cases}, {cases} words')
G2, H2 = strip_series(rule(2, lambda a, b: True), 10), strip_series(rule(2, lambda a, b: False), 10)
print('[1] h = 2: every pair allowed', G2[:6], '= 2^w; no pair allowed', H2[:6], '; dual:', dual_product_is_one(G2, H2))
for h in range(2, 9):
    assert sp.simplify(gf(rule(h, lambda a, b: a != b)) - (1 + x) / (1 - (h - 1) * x)) == 0
    assert sp.simplify(gf(rule(h, lambda a, b: a == b)) - (1 + h * x / (1 - x))) == 0
print('[1] plateau-free J - I: (1 + x)/(1 - (h-1)x); constant I: 1 + hx/(1 - x), h = 2..8: True')


# [2] Examples.
c = (1, 3, 3, 1, 4)
print('[2]', c, 'is a Hilbert castle of height 4:', is_strip(c, hilbert(4)) and max(c) == 4,
      ' blocks', blocks(c), ' ', draw(c))
print('[2] (1, 2, 4) is not:', not is_strip((1, 2, 4), hilbert(4)))
two = [c for c in product(range(1, 5), repeat=2) if max(c) == 4 and is_strip(c, hilbert(4))]
print('[2] the Hilbert castles of width 2 and height 4:', two, 'blocks', [blocks(c) for c in two])
for c in two:
    print('     ', c, draw(c))
three = [c for c in product(range(1, 4), repeat=3) if max(c) == 3 and is_strip(c, hilbert(3))]
print('[2] the Hilbert castles of width 3 and height 3:', three, 'blocks', [blocks(c) for c in three])


# [3] Hilbert strips and castles: counts, the OEIS, closed forms, generating functions.
for a, h in (('A083318', 3), ('A126358', 4), ('A287804', 5), ('A287806', 6), ('A287808', 7), ('A287812', 8),
             ('A287816', 9), ('A287825', 10), ('A287832', 11)):
    off, data = OEIS[a]
    s = strip_series(hilbert(h), off + len(data) - 1)
    print(f'[3] {a}(n) = Hilbert strips of width n on the heights 1..{h}, n >= {off}:',
          s[off:] == data, f'{len(data)} terms')
table = {}
for h in range(2, 8):
    table[h] = castle_counts(hilbert, h, 12)
    bf = all(brute_castles(hilbert(h), w, h) == table[h][w - 1] for w in range(1, 13) if h ** w <= 3 * 10 ** 6)
    print(f'[3] A_hilbert(w, {h}), w = 1..12:', table[h], ' brute force where h^w <= 3e6:', bf)
W = 60
print('[3] h = 2: 1 for every w; h = 3: 2^w - 1; h = 4: 2F_(2w+1) - 2^w - 1, w <= 60:',
      castle_counts(hilbert, 2, W) == [1] * W,
      castle_counts(hilbert, 3, W) == [2 ** w - 1 for w in range(1, W + 1)],
      castle_counts(hilbert, 4, W) == [2 * F[2 * w + 1] - 2 ** w - 1 for w in range(1, W + 1)])
print('[3] A000225(w) = A_hilbert(w, 3), w >= 1:', OEIS['A000225'][1][1:] == castle_counts(hilbert, 3, 33))
print('[3] hstrips(w, 4) = 2F_(2w+1) for w >= 1, w <= 60:',
      strip_series(hilbert(4), W)[1:] == [2 * F[2 * w + 1] for w in range(1, W + 1)])
for h in range(2, 9):
    Gh, Zh = gf(hilbert(h)), gf(zigzag(h))
    assert sp.simplify(Gh * Zh.subs(x, -x) - 1) == 0
    if h <= 6:
        print(f'[3] h = {h}: Z_h(x) =', sp.factor(Zh), '  sum hstrips(w, h) x^w = 1/Z_h(-x) =', sp.factor(Gh))
print('[3] sum hstrips(w, h) x^w = 1/Z_h(-x) as rational functions, h = 2..8: True')
for h in range(2, 9):
    den = sp.denom(sp.factor(gf(hilbert(h))))
    assert sp.degree(den, x) <= (h + 1) // 2
print('[3] the reduced denominator of the Hilbert strip series has degree <= ceil(h/2), h = 2..8: True')


# [4] Height 4: the path on four heights is its own complement.
sigma = {1: 3, 2: 1, 3: 4, 4: 2}
P = sp.zeros(4, 4)
for a, b in sigma.items():
    P[b - 1, a - 1] = 1
I4, J4, A4 = sp.eye(4), sp.ones(4, 4), sp.Matrix(zigzag(4))
print('[4] sigma = (1->3, 2->1, 3->4, 4->2): sigma(I + A_path) = J - A_path:', P * (I4 + A4) * P.T == J4 - A4,
      '; sigma(A_path) = J - I - A_path:', P * A4 * P.T == J4 - I4 - A4)
print('[4] charpoly of I + A_path and of J - A_path on 4 heights:', sp.factor((I4 + A4).charpoly(x).as_expr()), '|',
      sp.factor((J4 - A4).charpoly(x).as_expr()))
selfcomp = []
for h in range(2, 9):
    A = zigzag(h)
    comp = [[0 if a == b else 1 - A[a][b] for b in range(h)] for a in range(h)]
    if any(all(A[a][b] == comp[p[a]][p[b]] for a in range(h) for b in range(h)) for p in permutations(range(h))):
        selfcomp.append(h)
print('[4] heights h = 2..8 at which a relabeling maps the path onto its complement:', selfcomp)
sm = strip_series(smooth(4, 1), 30)
print('[4] free 1-smooth strips on 4 heights = Hilbert strips on 4 heights = A126358, w <= 28:',
      sm == strip_series(hilbert(4), 30), sm[:29] == OEIS['A126358'][1])
print('[4] zig-zag strips on 4 heights = 2-disparate strips on 4 heights = 2F_(w+2), w = 1..30:',
      strip_series(zigzag(4), 30) == strip_series(disparate(4, 2), 30),
      strip_series(zigzag(4), 30)[1:] == [2 * F[w + 2] for w in range(1, 31)])
uses3 = [sum(1 for c in product(range(1, 5), repeat=w) if 3 in c and is_strip(c, smooth(4, 1))) for w in range(1, 9)]
print('[4] free 1-smooth strips on 4 heights that use height 3, w = 1..8:', uses3, '= A_hilbert(w, 4):',
      uses3 == table[4][:8])


# [5] Growth by width.
for h in range(2, 13):
    M = hilbert(h)
    ev = np.linalg.eigvals(np.array(M, dtype=float))
    rho = max(ev.real)
    cp = sp.factor(sp.Matrix(M).charpoly(x).as_expr())
    mp = next(f for f, _ in sp.factor_list(sp.Matrix(M).charpoly(x).as_expr())[1]
              if any(abs(complex(r) - rho) < 1e-8 for r in sp.Poly(f, x).nroots()))
    anti = sorted(-2 * math.cos(math.pi * k / (h + 1)) for k in range(2, h + 1, 2))
    # antisymmetric vectors under the flip a <-> h + 1 - a
    basis = [[(1 if i == j else 0) - (1 if i == h - 1 - j else 0) for i in range(h)] for j in range(h // 2)]
    Bm = np.array(basis, dtype=float).T
    Mm = np.array(M, dtype=float)
    restricted = np.linalg.lstsq(Bm, Mm @ Bm, rcond=None)[0]
    anti_ok = np.allclose(sorted(np.linalg.eigvals(restricted).real), anti) if h >= 2 else True
    big = castle_counts(hilbert, h, 401)
    ratio = mpmath.mpf(big[400]) / big[399]
    print(f'[5] h = {h:2d}: rho = {rho:.10f}, minimal polynomial {mp}, degree {sp.degree(mp, x)};'
          f' h - 2 + 2/h <= rho <= h - 1: {h - 2 + 2 / h <= rho + 1e-12 and rho <= h - 1 + 1e-12};'
          f' A(401)/A(400) - rho = {float(ratio - rho):.1e}; antisymmetric part -2cos(pi k/(h+1)), k even: {anti_ok}')
    if h <= 6:
        print('      characteristic polynomial', cp)


# [6] Blocks and parity.
for h in range(2, 8):
    E, O = parity_counts(hilbert(h), h, 12)
    bf_ok = True
    for w in range(1, 13):
        if h ** w > 2 * 10 ** 6:
            continue
        e = o = 0
        for c in product(range(1, h + 1), repeat=w):
            if max(c) == h and is_strip(c, hilbert(h)):
                if blocks(c) % 2:
                    o += 1
                else:
                    e += 1
        bf_ok &= (e, o) == (E[w - 1], O[w - 1])
    print(f'[6] h = {h}: A^e', E, ' A^o', O, ' brute force where h^w <= 2e6:', bf_ok)
E3, O3 = parity_counts(hilbert(3), 3, 30)
print('[6] h = 3: no even-block Hilbert castle for w <= 30:', E3 == [0] * 30)


# [7] The m-disparate castles, the dual of the (m - 1)-smooth rule.
for m in range(1, 6):
    for h in range(1, 10):
        assert dual(smooth(h, m - 1)) == disparate(h, m)
        assert dual_product_is_one(strip_series(disparate(h, m), 20), strip_series(smooth(h, m - 1), 20))
print('[7] J - (band m-1) = the m-disparate rule, and the duality, m = 1..5, h = 1..9, up to x^20: True')
for m in (2, 3, 4):
    for h in range(m + 1, 9):
        A = castle_counts(lambda hh: disparate(hh, m), h, 12)
        bf = all(brute_castles(disparate(h, m), w, h) == A[w - 1] for w in range(1, 13) if h ** w <= 2 * 10 ** 6)
        print(f'[7] A_{m}-disp(w, {h}), w = 1..12:', A, ' brute force where h^w <= 2e6:', bf)
for h in (4, 5, 6):
    E, O = parity_counts(disparate(h, 2), h, 12)
    bf_ok = True
    for w in range(1, 13):
        if h ** w > 2 * 10 ** 6:
            continue
        cs = [c for c in product(range(1, h + 1), repeat=w) if max(c) == h and is_strip(c, disparate(h, 2))]
        bf_ok &= (sum(1 for c in cs if blocks(c) % 2 == 0), sum(1 for c in cs if blocks(c) % 2)) == (E[w - 1], O[w - 1])
    print(f'[7] 2-disparate castles of height {h}: A^e', E, ' A^o', O, ' brute force where h^w <= 2e6:', bf_ok)
diag = all(castle_counts(lambda hh: disparate(hh, m), m + 2, 30)[1:] == [2 * (F[w + 2] - 1) for w in range(2, 31)]
           for m in range(2, 10))
near = all(castle_counts(lambda hh: disparate(hh, m), m + 1, 30)[1:] == [2] * 29 for m in range(2, 10))
low = all(castle_counts(lambda hh: disparate(hh, m), h, 30)[1:] == [0] * 29 for m in range(2, 10) for h in range(2, m + 1))
print('[7] h = m + 2: 2(F_(w+2) - 1) for w = 2..30; h = m + 1: 2; 2 <= h <= m: 0; m = 2..9:', diag, near, low)
off, data = OEIS['A019274']
print('[7] A019274(w + 2) = 2(F_(w+2) - 1):', all(data[n - off] == 2 * F[n] - 2 for n in range(off, off + len(data))),
      f'{len(data)} terms')
t = sp.symbols('t')
for k in range(2, 9):
    U = lambda n: sp.chebyshevu(n, t)
    sw = 1 + x * (k - (3 * k + 2) * x) / (1 - 3 * x) ** 2 + 2 * x ** 2 * (1 + U(k - 1)) / ((1 - 3 * x) ** 2 * U(k))
    sw = sp.cancel(sw.subs(t, (1 - x) / (2 * x)))
    assert sp.simplify(sw - gf(smooth(k, 1))) == 0
    assert sp.simplify(gf(disparate(k, 2)) * sw.subs(x, -x) - 1) == 0
print('[7] Knopfmacher-Mansour-Munagi-Prodinger Theorem 2.2 = the free 1-smooth strip series, and the 2-disparate '
      'strip series = 1/sw_h(-x), h = 2..8: True')
for h in range(2, 10):
    assert [[disparate(h, 2)[a][b] - hilbert(h)[a][b] + (a == b) for b in range(h)] for a in range(h)] == \
        [[0] * h for _ in range(h)]
print('[7] the 2-disparate rule is J - I - A_path, the Hilbert rule minus I, h = 2..9: True')
for h in range(4, 10):
    rho = max(np.linalg.eigvals(np.array(disparate(h, 2), dtype=float)).real)
    rho_h = max(np.linalg.eigvals(np.array(hilbert(h), dtype=float)).real)
    print(f'[7] growth of the 2-disparate castles of height {h}: {rho:.10f} = rho(J - A_path) - 1: '
          f'{abs(rho - rho_h + 1) < 1e-9}')


# [8] The tree skylines, the dual of the strips with every column at height at least 2.
for h in range(2, 8):
    tree = rule(h, lambda a, b: a == 1 or b == 1)
    tall = dual(tree)
    Ph = sum(q ** a for a in range(2, h + 1))
    G_tall = 1 + q * x + Ph * x / (1 - Ph * x)
    assert sp.simplify(sp.cancel(1 / G_tall.subs(x, -x)) - (1 + Ph * x) / (1 - q * x - q * Ph * x ** 2)) == 0
    ser = area_series(tree, 8)
    target = sp.series((1 + Ph * x) / (1 - q * x - q * Ph * x ** 2), x, 0, 9).removeO()
    assert all(sp.expand(target.coeff(x, w) - sum(cf * q ** i for i, cf in enumerate(ser[w]))) == 0 for w in range(9))
    assert sp.simplify(gf(tree) - (1 + (h - 1) * x) / (1 - x - (h - 1) * x ** 2)) == 0
print('[8] tree skylines: 1/G_tall(-x, q) = (1 + P_h(q)x)/(1 - qx - qP_h(q)x^2), equal to the area-width series '
      'up to x^8, and at q = 1 (1 + (h-1)x)/(1 - x - (h-1)x^2), h = 2..7: True')
print('[8] T_h(w), w = 0..9:', {h: strip_series(rule(h, lambda a, b: a == 1 or b == 1), 9) for h in (2, 3, 4)})
