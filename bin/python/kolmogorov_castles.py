# Kolmogorov castles: the castles of the two-sample Kolmogorov-Smirnov test with two samples of n
# values each. Column i of the merged order has height 1 + |a_i - b_i|, with a_i and b_i the values
# of the first (X) and second (Y) sample among the first i - 1, and each peak carries the sample
# that is ahead on it. Checks: the examples; the bijection with the Dyck-path castles marked peak by
# peak; the count of the castles of height h by reflection, by the path matrix and by cosines; the
# height table; the OEIS entries; the block count; the one-sided count; Kolmogorov's limit law; the
# growth; Kolmogorov's 1933 table and recursion; Korolyuk's 1955 first-passage count.
# Page: wiki/pages/kolmogorov-castles.md.  OEIS data below: the data fields, read 2026-10-28.
import math
import random
from itertools import combinations
from fractions import Fraction

OEIS = {
    'A000984': (0, [1, 2, 6, 20, 70, 252, 924, 3432, 12870, 48620, 184756, 705432, 2704156, 10400600,
                    40116600, 155117520, 601080390, 2333606220, 9075135300, 35345263800, 137846528820,
                    538257874440, 2104098963720, 8233430727600, 32247603683100, 126410606437752,
                    495918532948104, 1946939425648112]),
    'A000079': (0, [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536,
                    131072, 262144, 524288, 1048576, 2097152, 4194304, 8388608, 16777216, 33554432,
                    67108864, 134217728, 268435456, 536870912, 1073741824, 2147483648, 4294967296,
                    8589934592, 17179869184]),
    'A056182': (0, [0, 2, 10, 38, 130, 422, 1330, 4118, 12610, 38342, 116050, 350198, 1054690, 3172262,
                    9533170, 28632278, 85962370, 258018182, 774316690, 2323474358, 6971471650,
                    20916512102, 62753730610, 188269580438, 564825518530, 1694510110022, 5083597438930,
                    15250926534518, 45753048039010]),
    'A000108': (0, [1, 1, 2, 5, 14, 42, 132, 429, 1430, 4862, 16796, 58786, 208012, 742900, 2674440,
                    9694845, 35357670, 129644790, 477638700, 1767263190, 6564120420, 24466267020,
                    91482563640, 343059613650, 1289904147324, 4861946401452, 18367353072152,
                    69533550916004, 263747951750360, 1002242216651368, 3814986502092304]),
    'A080936': (1, [1, 1, 1, 1, 3, 1, 1, 7, 5, 1, 1, 15, 18, 7, 1, 1, 31, 57, 33, 9, 1, 1, 63, 169, 132,
                    52, 11, 1, 1, 127, 482, 484, 247, 75, 13, 1, 1, 255, 1341, 1684, 1053, 410, 102, 15,
                    1, 1, 511, 3669, 5661, 4199, 1975, 629, 133, 17, 1, 1, 1023, 9922, 18579, 16017,
                    8778, 3366, 912, 168, 19, 1]),
}


def binom(n, k):
    return math.comb(n, k) if 0 <= k <= n else 0


def blocks(c):
    """The block count c_1 + sum max(0, c_i - c_{i-1}): the total ascent from height 0."""
    return sum(max(0, b - a) for a, b in zip((0,) + c, c))


def kolmogorov_castle(word):
    """The skyline and the peak marks of a merged order, a word in X and Y."""
    a = b = 0
    c, marks = [1], []
    for ch in word:
        a, b = (a + 1, b) if ch == 'X' else (a, b + 1)
        if c[-1] == 1 and a != b:
            marks.append('X' if a > b else 'Y')
        c.append(1 + abs(a - b))
    return tuple(c), tuple(marks)


def peaks(c):
    """Maximal runs of columns of height >= 2, as (start, end) index pairs."""
    runs, start = [], None
    for i, x in enumerate(c + (1,)):
        if x >= 2 and start is None:
            start = i
        if x < 2 and start is not None:
            runs.append((start, i - 1))
            start = None
    return runs


def draw(c, marks):
    """Rows of the castle from the top: the bottom row '#', each peak cell its mark."""
    owner = [None] * len(c)
    for (s, e), m in zip(peaks(c), marks):
        for i in range(s, e + 1):
            owner[i] = m
    rows = []
    for r in range(max(c), 0, -1):
        rows.append(' '.join(('#' if r == 1 else owner[i]) if c[i] >= r else '.'
                             for i in range(len(c))))
    return rows


def words(n):
    for pos in combinations(range(2 * n), n):
        w = ['Y'] * (2 * n)
        for p in pos:
            w[p] = 'X'
        yield ''.join(w)


def at_most(n, h):
    """Kolmogorov castles of width 2n + 1 and height at most h, by reflection: sum_k (-1)^k C(2n, n + kh)."""
    if h <= 0:
        return 0
    return sum((-1) ** abs(k) * binom(2 * n, n + k * h) for k in range(-(n // h) - 1, n // h + 2))


def at_most_lemma(n, h):
    """Lutsenko-Marinich-Matsak Lemma 2.2 with c = h: C(2n, n) - 2 sum_{i=1}^{[n/h]} (-1)^{i-1} C(2n, n - ih)."""
    return math.comb(2 * n, n) - 2 * sum((-1) ** (i - 1) * math.comb(2 * n, n - i * h)
                                         for i in range(1, n // h + 1))


def at_most_matrix(n, h):
    """[A_path^{2n}] at the middle vertex of the path on 2h - 1 heights."""
    if h <= 0:
        return 0
    m = 2 * h - 1
    v = [0] * m
    v[h - 1] = 1
    for _ in range(2 * n):
        v = [(v[i - 1] if i > 0 else 0) + (v[i + 1] if i < m - 1 else 0) for i in range(m)]
    return v[h - 1]


def at_most_cos(n, h):
    """(1/h) sum_{j=0}^{h-1} (2 + 2cos((2j+1) pi/h))^n, in floating point."""
    if h <= 0:
        return 0.0
    return sum((2 + 2 * math.cos((2 * j + 1) * math.pi / h)) ** n for j in range(h)) / h


def A_kol(n, h):
    """Kolmogorov castles of width 2n + 1 and height h: Equation (2) of the page, for h >= 2."""
    if h <= 1:
        return 1 if (h == 1 and n == 0) else 0
    return sum((-1) ** abs(k) * (binom(2 * n, n + k * h) - binom(2 * n, n + k * (h - 1)))
               for k in range(-n - 1, n + 2))


def K_star(x, terms=200):
    """Kolmogorov's distribution 1 - 2 sum_{k>=1} (-1)^{k-1} exp(-2 k^2 x^2)."""
    return 1 - 2 * sum((-1) ** (k - 1) * math.exp(-2 * k * k * x * x) for k in range(1, terms))


def log_ratio(n, j):
    """ln C(2n, n - j)/C(2n, n)."""
    return (2 * math.lgamma(n + 1) - math.lgamma(n - j + 1) - math.lgamma(n + j + 1))


def share_at_most(n, h):
    """Share of the Kolmogorov castles of width 2n + 1 with height at most h, in floating point."""
    return 1 - 2 * sum((-1) ** (i - 1) * math.exp(log_ratio(n, i * h)) for i in range(1, n // h + 1))


# [1] the example XXYYYX
c, marks = kolmogorov_castle('XXYYYX')
assert c == (1, 2, 3, 2, 1, 2, 1) and marks == ('X', 'Y')
print(f"[1] XXYYYX -> skyline {c}, height {max(c)}, peak marks {marks}, D = {Fraction(max(c) - 1, 3)},"
      f" blocks {blocks(c)}")
for row in draw(c, marks):
    print("[1]   " + row)
tall = sum(1 for w in words(3) if max(kolmogorov_castle(w)[0]) >= 3)
print(f"[1] Kolmogorov castles of width 7 at least as tall as XXYYYX: {tall} of {math.comb(6, 3)},"
      f" share {Fraction(tall, math.comb(6, 3))}")

# [2] the six Kolmogorov castles of width 5
for w in words(2):
    c, marks = kolmogorov_castle(w)
    print(f"[2] {w} -> {c}, marks {marks}, height {max(c)}, D = {Fraction(max(c) - 1, 2)}: "
          + ' / '.join(draw(c, marks)))

# [3] the bijection with marked Dyck-path castles, the block count, the forms of the height-h count
N = 9
for n in range(1, N + 1):
    seen, per_skyline, hist = set(), {}, {}
    for w in words(n):
        c, marks = kolmogorov_castle(w)
        assert c[0] == c[-1] == 1 and all(abs(x - y) == 1 for x, y in zip(c, c[1:]))  # Dyck-path castle
        assert len(marks) == len(peaks(c)) and blocks(c) == n + 1
        assert (c, marks) not in seen
        seen.add((c, marks))
        per_skyline[c] = per_skyline.get(c, 0) + 1
        hist[max(c)] = hist.get(max(c), 0) + 1
    assert all(k == 2 ** len(peaks(c)) for c, k in per_skyline.items())
    for h in range(1, n + 3):
        assert hist.get(h, 0) == A_kol(n, h)
        assert sum(hist.get(g, 0) for g in range(1, h + 1)) == at_most(n, h) == at_most_lemma(n, h)
print(f"[3] n = 1..{N}: every merged order gives a Dyck-path castle of width 2n + 1 with one mark per peak,"
      " distinct orders give distinct marked castles, each skyline carries 2^peaks of them, every one has"
      " n + 1 blocks, the castles of height h number Equation (2), and those of height at most h"
      " number the reflection sum and Lemma 2.2")
for n in range(1, 40):
    for h in range(2, n + 3):
        assert A_kol(n, h) == at_most(n, h) - at_most(n, h - 1)
        assert at_most(n, h) == at_most_lemma(n, h) == at_most_matrix(n, h)
        if h <= 12 and n <= 20:
            assert round(at_most_cos(n, h) - at_most_cos(n, h - 1)) == A_kol(n, h)
print("[3] for n < 40: Equation (2) = the difference of the reflection sums = the difference of the"
      " path-matrix entries; Equation (3), the cosine form, for n <= 20, h <= 12")

# [4] the height table
for n in range(1, 9):
    row = [A_kol(n, h) for h in range(2, n + 2)]
    assert sum(row) == math.comb(2 * n, n)
    print(f"[4] w = {2 * n + 1:2d}: A_Kol(w, h) for h = 2..{n + 1}: {row}, total C({2 * n}, {n}) = {sum(row)}")
print("[4] n = 4, the reflection terms: height at most 2, 3, 4, 5 =",
      [at_most(4, h) for h in (2, 3, 4, 5)])

# [5] the OEIS entries, term by term over the data field
off, data = OEIS['A000984']
assert all(sum(A_kol(off + i, h) for h in range(1, off + i + 2)) == t for i, t in enumerate(data))
print(f"[5] sum over h of A_Kol(2n + 1, h) = A000984(n) on all {len(data)} terms")
off, data = OEIS['A000079']
assert all(A_kol(i, 2) == t for i, t in enumerate(data) if i >= 1)
print(f"[5] A_Kol(2n + 1, 2) = A000079(n) = 2^n for n >= 1, on all {len(data) - 1} terms from n = 1")
off, data = OEIS['A056182']
assert all(A_kol(i + 1, 3) == t for i, t in enumerate(data))
assert all(A_kol(n, 3) == 2 * (3 ** (n - 1) - 2 ** (n - 1)) for n in range(1, 60))
print(f"[5] A_Kol(2n + 1, 3) = A056182(n - 1) = 2(3^(n-1) - 2^(n-1)) on all {len(data)} terms")
off, data = OEIS['A080936']
tri, k = {}, 0
for n in range(1, 12):
    for j in range(1, n + 1):
        if k < len(data):
            tri[(n, j)] = data[k]
            k += 1
for n in range(1, 10):
    dyck = {}
    for w in words(n):
        c, _ = kolmogorov_castle(w)
        dyck.setdefault(max(c), set()).add(c)
    assert all(len(dyck.get(j + 1, ())) == tri[(n, j)] for j in range(1, n + 1) if (n, j) in tri)
print("[5] the skylines of height h at width 2n + 1 number A080936(n, h - 1), n = 1..9")

# [6] one sample ahead: the X peaks of height at most h
off, data = OEIS['A000108']
assert all(math.comb(2 * n, n) - binom(2 * n, n - 1) == t for n, t in enumerate(data))
print(f"[6] no peak marked X: C(2n, n) - C(2n, n - 1) = A000108(n) on all {len(data)} terms")
for n in range(1, N + 1):
    for h in range(1, n + 2):
        cnt = 0
        for w in words(n):
            c, marks = kolmogorov_castle(w)
            if all(max(c[s:e + 1]) <= h for (s, e), m in zip(peaks(c), marks) if m == 'X'):
                cnt += 1
        assert cnt == math.comb(2 * n, n) - binom(2 * n, n - h)
print(f"[6] n = 1..{N}: the Kolmogorov castles whose X peaks all have height at most h number"
      " C(2n, n) - C(2n, n - h) (Lemma 2.1 with c = h)")

# [7] Kolmogorov's limit law
lo, hi = 1.0, 2.0
for _ in range(100):
    mid = (lo + hi) / 2
    lo, hi = (mid, hi) if K_star(mid) < 0.95 else (lo, mid)
print(f"[7] K*(1.36) = {K_star(1.36):.5f}; K*(x) = 0.95 at x = {lo:.5f}")
n = 200000
h = 1 + math.floor(1.36 * math.sqrt(2 * n))
print(f"[7] n = {n}: height at most 1 + 1.36 sqrt(w - 1) means h <= {h}; share {share_at_most(n, h):.5f}")
for n in (5, 10, 20, 50, 100, 1000, 10000):
    if n <= 1000:
        exact = next(hh for hh in range(1, n + 2)
                     if Fraction(at_most(n, hh), math.comb(2 * n, n)) >= Fraction(95, 100))
    else:
        exact = next(hh for hh in range(1, n + 2) if share_at_most(n, hh) >= 0.95)
    print(f"[7] w = {2 * n + 1}: the smallest h with at least 95% of the Kolmogorov castles of height at most h"
          f" is {exact} (share {share_at_most(n, exact):.5f}); 1 + {lo:.3f} sqrt(w - 1) = {1 + lo * math.sqrt(2 * n):.2f}")
for hh in (13, 14):
    print(f"[7] w = 101: share of height at most {hh} = {float(Fraction(at_most(50, hh), math.comb(100, 50))):.5f}")
for n in (1000, 100000):
    for xx in (0.5, 1.0, 1.5):
        h = 1 + math.floor(xx * math.sqrt(2 * n))
        print(f"[7] w = {2 * n + 1}, x = {xx}: share of height <= {h} is {share_at_most(n, h):.5f};"
              f" K*({xx}) = {K_star(xx):.5f}")

# [8] growth by width
for h in range(2, 9):
    n = 4000
    r = float(Fraction(A_kol(n + 1, h), A_kol(n, h)))
    print(f"[8] h = {h}: A_Kol(w + 2, h)/A_Kol(w, h) at w = {2 * n + 1}: {r:.12f}; 2 + 2cos(pi/h) ="
          f" {2 + 2 * math.cos(math.pi / h):.12f}; growth by width 2cos(pi/(2h)) = {2 * math.cos(math.pi / (2 * h)):.5f}")

# [9] the even-block counts
for n in range(1, 9):
    even = sum(1 for w in words(n) if blocks(kolmogorov_castle(w)[0]) % 2 == 0)
    assert even == (math.comb(2 * n, n) if n % 2 == 1 else 0)
print("[9] n = 1..8: A^e_Kol(2n + 1) = C(2n, n) for odd n and 0 for even n")

# [10] catalogue rows
print("[10] catalogue rows: A_Kol(2n + 1, 4) for n = 1..10:", [A_kol(n, 4) for n in range(1, 11)])
print("[10] catalogue rows: A^e_Kol(2n + 1) for n = 0..9:", [math.comb(2 * n, n) if n % 2 else 0 for n in range(10)])

# [11] Kolmogorov 1933, p. 84: the table of Phi(lambda) computed by N. Kozhevnikov, against K*
table = {0.0: '0.0000', 0.2: '0.0000', 0.4: '0.0028', 0.6: '0.1357', 0.8: '0.4558', 1.0: '0.7300',
         1.2: '0.8877', 1.4: '0.9603', 1.6: '0.9880', 1.8: '0.9969', 2.0: '0.99932', 2.2: '0.99986',
         2.4: '0.999973', 2.6: '0.9999964', 2.8: '0.99999966'}
for lam, s in table.items():
    digits = len(s.split('.')[1])
    val = K_star(lam) if lam > 0 else 0.0
    trunc = math.floor(val * 10 ** digits) / 10 ** digits
    if lam <= 2.0:
        assert f"{trunc:.{digits}f}" == s, (lam, val, s)
    else:
        print(f"[11] lambda = {lam}: printed {s}, series K* = {val:.{digits + 1}f}")
print("[11] Kolmogorov 1933 table: the 11 values of Phi(lambda) for lambda = 0.0..2.0 are K*(lambda)"
      " truncated to the printed digits")
print(f"[11] K*(0.83) = {K_star(0.83):.4f}; small-lambda form sqrt(2 pi)/lambda exp(-pi^2/(8 lambda^2)) at 0.6 ="
      f" {math.sqrt(2 * math.pi) / 0.6 * math.exp(-math.pi ** 2 / (8 * 0.36)):.4f}, K*(0.6) = {K_star(0.6):.4f};"
      f" 1 - K*(2.4) = {1 - K_star(2.4):.1e}")


# [12] Kolmogorov 1933, eqs. [13]-[17]: Phi_n(mu/sqrt n) = n!/n^n e^n R_{0n}, with R_{00} = 1,
# R_{i0} = 0 (i != 0), R_{ik} = 0 for |i| >= mu, R_{i,k+1} = sum_j R_{jk} e^{-1}/(i - j + 1)!
def kolmogorov_recursion(n, mu):
    R = {0: 1.0}
    for _ in range(n):
        new = {}
        for i in range(-mu + 1, mu):
            s = sum(r * math.exp(-1) / math.factorial(i - j + 1) for j, r in R.items() if i - j + 1 >= 0)
            if s:
                new[i] = s
        R = new
    return math.exp(math.lgamma(n + 1) - n * math.log(n) + n) * R.get(0, 0.0)


def mc_D(n, d, trials, rng):
    """Monte Carlo P(sup |F_n(x) - x| < d) for n uniform values."""
    hits = 0
    for _ in range(trials):
        u = sorted(rng.random() for _ in range(n))
        D = max(max((i + 1) / n - x, x - i / n) for i, x in enumerate(u))
        hits += D < d
    return hits / trials


rng = random.Random(1933)
for n, mu in [(5, 2), (10, 3), (16, 4)]:
    rec = kolmogorov_recursion(n, mu)
    mc = mc_D(n, mu / n, 200000, rng)
    assert abs(rec - mc) < 0.005, (n, mu, rec, mc)
    print(f"[12] n = {n}, mu = {mu}: Kolmogorov's recursion gives P(D < {mu}/{n}) = {rec:.4f};"
          f" Monte Carlo (200000 samples) {mc:.4f}")
for mu in (5, 10, 20, 40):
    print(f"[12] lambda = 1, n = {mu * mu}: recursion {kolmogorov_recursion(mu * mu, mu):.4f}, K*(1) = {K_star(1):.4f}")


# [13] Korolyuk 1955, Theorem 1 and eq. (4): merged orders of n values X and m = pn values Y, the lead
# b - p a (+1 per Y, -p per X); the orders whose lead reaches c number
# sum_{k = c (mod p+1)} (c/k) C(k, (k-c)/(p+1)) C(N-k, n - (k-c)/(p+1)), N = n + m.
def korolyuk_reach(n, p, c):
    N = n + p * n
    tot = Fraction(0)
    for k in range(c, N + 1):
        if (k - c) % (p + 1) == 0:
            d = (k - c) // (p + 1)
            tot += Fraction(c, k) * binom(k, d) * binom(N - k, n - d)
    return tot


for p in (1, 2, 3):
    for n in range(1, 7 if p > 1 else 9):
        m = p * n
        N = n + m
        reach = {}
        for pos in combinations(range(N), n):
            S, top = 0, 0
            ps = set(pos)
            for t in range(N):
                S += -p if t in ps else 1
                top = max(top, S)
            for c in range(1, top + 1):
                reach[c] = reach.get(c, 0) + 1
        for c in range(1, m + 1):
            assert korolyuk_reach(n, p, c) == reach.get(c, 0), (p, n, c)
            if p == 1:
                assert korolyuk_reach(n, 1, c) == binom(2 * n, n - c)
print("[13] Korolyuk 1955, eq. (4): the first-passage sum equals the number of merged orders whose lead"
      " reaches c, by enumeration for p = 1 (n <= 8), p = 2, 3 (n <= 6); at p = 1 it is C(2n, n - c)")
