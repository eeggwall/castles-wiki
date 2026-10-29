# Totient castles: neighboring columns have coprime heights. The coprimality matrix M_h, the
# counts by width and height, the Fibonacci castles at height 2 and the Pell-Lucas strips at height
# 3, the characteristic polynomials for h <= 8, and the Euler product: the largest eigenvalue of M_h
# is Lambda h + O(h^(1/2 + eps)), with eigenvector v_a = prod_{p | a} x_p, x_p^2 + (p - 1) x_p = p - 1.
# Page: wiki/pages/totient-castles.md.
from itertools import product
from math import gcd, sqrt, isqrt
import mpmath
import sympy as sp

A001333 = [1, 1, 3, 7, 17, 41, 99, 239, 577, 1393, 3363, 8119, 19601, 47321, 114243, 275807]  # offset 0
A000071 = [0, 0, 1, 2, 4, 7, 12, 20, 33, 54, 88, 143, 232, 376, 609, 986, 1596, 2583, 4180, 6764]  # offset 1


def blocks(c):
    return sum(max(0, b - a) for a, b in zip((0,) + c, c))


def strips(h, W, sign=False):
    """Skylines in {1..h}^w with coprime neighbors, w = 1..W; with sign, weighted by (-1)^blocks."""
    if h == 0:
        return [0] * W
    v = [(-1) ** a if sign else 1 for a in range(1, h + 1)]
    out = [sum(v)]
    for _ in range(W - 1):
        v = [sum(v[a - 1] * ((-1) ** max(0, b - a) if sign else 1) for a in range(1, h + 1) if gcd(a, b) == 1)
             for b in range(1, h + 1)]
        out.append(sum(v))
    return out


def castles(h, W, sign=False):
    return [s - t for s, t in zip(strips(h, W, sign), strips(h - 1, W, sign))]


def primes_upto(n):
    s = bytearray([1]) * (n + 1)
    s[0] = s[1] = 0
    for i in range(2, isqrt(n) + 1):
        if s[i]:
            s[i * i::i] = bytearray(len(s[i * i::i]))
    return [i for i in range(n + 1) if s[i]]


def x_p(p):
    return (-(p - 1) + sqrt((p - 1) ** 2 + 4 * (p - 1))) / 2


def prime_factors(n):
    out, d = [], 2
    while d * d <= n:
        if n % d == 0:
            out.append(d)
            while n % d == 0:
                n //= d
        d += 1
    if n > 1:
        out.append(n)
    return out


def v(a):
    r = 1.0
    for p in prime_factors(a):
        r *= x_p(p)
    return r


# [1] counts
ok = True
for w in range(1, 8):
    for h in range(1, 7):
        n = sum(1 for c in product(range(1, h + 1), repeat=w)
                if max(c) == h and all(gcd(a, b) == 1 for a, b in zip(c, c[1:])))
        ok &= n == castles(h, w)[-1]
print(f"[1] totient castles by the transfer matrix = brute force, w <= 7, h <= 6: {ok}")
for h in range(2, 7):
    print(f"[1] h = {h}: A_totient(w, h), w = 1..10: {castles(h, 10)}")
fib = [0, 1]
while len(fib) < 30:
    fib.append(fib[-1] + fib[-2])
ok = castles(2, 20) == [fib[w + 2] - 1 for w in range(1, 21)]
ok &= castles(2, 18) == [A000071[w + 1] for w in range(1, 19)]
print(f"[1] height 2: F_(w+2) - 1 = A000071(w + 2), the Fibonacci castles, w <= 20: {ok}")
s3 = strips(3, 14)
smooth = []
vv = [1, 1, 1]
for w in range(1, 15):
    smooth.append(sum(vv))
    vv = [vv[0] + vv[1], vv[0] + vv[1] + vv[2], vv[1] + vv[2]]
ok = s3 == [A001333[w + 1] for w in range(1, 15)] == smooth
ok &= castles(3, 14) == [A001333[w + 1] - fib[w + 2] for w in range(1, 15)]
print(f"[1] height 3: the strips number A001333(w + 1), as the 1-smooth strips on {{1, 2, 3}} do, "
      f"and the castles A001333(w + 1) - F_(w+2), w <= 14: {ok}")

# [2] characteristic polynomials
x = sp.symbols('x')
for h in range(2, 9):
    m = sp.Matrix(h, h, lambda i, j: 1 if gcd(i + 1, j + 1) == 1 else 0)
    cp = m.charpoly(x).as_expr()
    r = max(sp.Poly(cp, x).nroots(n=15), key=lambda z: sp.re(z))
    print(f"[2] h = {h}: char poly {sp.factor(cp)}, largest eigenvalue {sp.N(r, 8)}")
m3 = sp.Matrix(3, 3, lambda i, j: 1 if gcd(i + 1, j + 1) == 1 else 0)
s3m = sp.Matrix([[1, 1, 0], [1, 1, 1], [0, 1, 1]])
ok = m3 * sp.Matrix([0, 1, -1]) == -sp.Matrix([0, 1, -1]) and s3m * sp.Matrix([1, 0, -1]) == sp.Matrix([1, 0, -1])
print(f"[2] height 3: (0, 1, -1) is the eigenvector of M_3 for -1, (1, 0, -1) that of the 1-smooth "
      f"matrix for 1, both orthogonal to the all-ones vector: {ok}")

# [3] the constant
mpmath.mp.dps = 30
lam = 6 / mpmath.pi ** 2
for p in primes_upto(10 ** 6):
    xp = (-(p - 1) + mpmath.sqrt(mpmath.mpf(p - 1) ** 2 + 4 * (p - 1))) / 2
    lam *= (1 - (1 - xp) / p) / (1 - mpmath.mpf(1) / p ** 2)
print(f"[3] Lambda = (6/pi^2) prod_p (1 - (1 - x_p)/p)/(1 - 1/p^2), primes < 10^6: {mpmath.nstr(lam, 15)}")
print(f"[3] x_2 = {x_p(2):.12f}, 1/phi = {2 / (1 + sqrt(5)):.12f}; x_3 = {x_p(3):.12f} = sqrt 3 - 1 "
      f"= {sqrt(3) - 1:.12f}")
ok = all(abs((p - 1) / (p - 1 + x_p(p)) - x_p(p)) < 1e-12 for p in primes_upto(1000))
ok &= all(x_p(p) < x_p(q) for p, q in zip(primes_upto(1000), primes_upto(1000)[1:]))
ok &= all(1 - x_p(p) <= 1 / (p - 1) for p in primes_upto(1000))
print(f"[3] (p - 1)/(p - 1 + x_p) = x_p, x_p increasing, 1 - x_p <= 1/(p - 1), p < 1000: {ok}")
LAM = float(lam)

# [4] the lemma: row sums against the eigenvector
ok = True
for n in range(1, 3001):
    g_sum = 0.0
    for d in range(1, n + 1):
        if n % d == 0 and all(d % (q * q) for q in range(2, isqrt(d) + 1)):
            g = 1.0
            for p in prime_factors(d):
                g *= x_p(p) - 1
            g_sum += g
    ok &= abs(g_sum - v(n)) < 1e-9
print(f"[4] v = 1 * g with g(p) = x_p - 1 on squarefree numbers, n <= 3000: {ok}")
worst = 0.0
for h in (50, 100, 200, 400):
    vs = [v(a) for a in range(1, h + 1)]
    for a in range(1, h + 1):
        sa = sum(vs[b - 1] for b in range(1, h + 1) if gcd(a, b) == 1)
        bound = 8 * 2 ** len(prime_factors(a)) * sqrt(h)
        worst = max(worst, abs(sa - LAM * h * vs[a - 1]) / bound)
print(f"[4] |(M_h v)_a - Lambda h v_a| <= 8 2^omega(a) sqrt(h) for every a <= h, h = 50, 100, 200, 400: "
      f"{worst <= 1}, largest ratio to the bound {worst:.4f}")


# [5] the largest eigenvalue
def collatz_and_rho(h, iters=60):
    rows = [[b for b in range(h) if gcd(a + 1, b + 1) == 1] for a in range(h)]
    vs = [v(a) for a in range(1, h + 1)]
    q = [sum(vs[b] for b in r) / (h * vs[a]) for a, r in enumerate(rows)]
    u = vs[:]
    for _ in range(iters):
        nu = [sum(u[b] for b in r) for r in rows]
        s = sqrt(sum(t * t for t in nu))
        u = [t / s for t in nu]
    mu = [sum(u[b] for b in r) for r in rows]
    rq = sum(s * t for s, t in zip(u, mu))
    resid = sqrt(sum((s - rq * t) ** 2 for s, t in zip(mu, u)))
    avg = sum(len(r) for r in rows) / h
    return min(q), max(q), rq / h, resid / h, avg / h


for h in (100, 400, 1600):
    lo, hi, r, res, avg = collatz_and_rho(h)
    print(f"[5] h = {h}: Collatz-Wielandt bounds {lo:.6f} <= rho/h <= {hi:.6f}; rho/h = {r:.7f} "
          f"(residual {res:.1e}); average row sum / h = {avg:.6f}; Lambda = {LAM:.7f}")
print(f"[5] 6/pi^2 = {6 / float(mpmath.pi) ** 2:.6f}")

# [6] the parity
for h in range(2, 7):
    a, s = castles(h, 10), castles(h, 10, sign=True)
    m = sp.Matrix(h, h, lambda i, j: (1 if gcd(i + 1, j + 1) == 1 else 0) * (-1) ** max(0, j - i))
    cp = m.charpoly(x).as_expr()
    rad = max(abs(complex(z)) for z in sp.Poly(cp, x).nroots(n=15))
    print(f"[6] h = {h}: even-block {[(p + q) // 2 for p, q in zip(a, s)]}; signed {s}; "
          f"signed char poly {sp.factor(cp)}, spectral radius {rad:.6f}")
ok = True
for w in range(1, 7):
    for h in range(1, 6):
        sg = sum((-1) ** blocks(c) for c in product(range(1, h + 1), repeat=w)
                 if max(c) == h and all(gcd(p, q) == 1 for p, q in zip(c, c[1:])))
        ok &= sg == castles(h, w, sign=True)[-1]
print(f"[6] the signed transfer matrix = brute force, w <= 6, h <= 5: {ok}")

# [7] by area: the compositions with coprime neighboring parts (A167606), and the strips by width
A167606 = [1, 1, 2, 4, 7, 14, 25, 48, 90, 168, 316, 594, 1116, 2096, 3935, 7388, 13877, 26061, 48944,
           91919, 172623, 324188, 608827, 1143390, 2147309, 4032677, 7573426, 14223008, 26711028,
           50163722, 94208254]  # offset 0, b-file read 2026-10-28
N = 200
count = [[0] * (N + 1) for _ in range(N + 1)]      # count[n][p]: castles of area n, first column p
signed = [[0] * (N + 1) for _ in range(N + 1)]     # the same weighted by (-1)^(blocks - first column)
for n in range(1, N + 1):
    for p in range(1, n + 1):
        if p == n:
            count[n][p], signed[n][p] = 1, 1
            continue
        for q in range(1, n - p + 1):
            if gcd(p, q) == 1:
                count[n][p] += count[n - p][q]
                signed[n][p] += (-1) ** max(0, q - p) * signed[n - p][q]
by_area = [sum(count[n][1:]) for n in range(N + 1)]
s_area = [sum((-1) ** p * signed[n][p] for p in range(1, n + 1)) for n in range(N + 1)]
ok = by_area[1:31] == A167606[1:31]
brute = []
for n in range(1, 13):
    tot, sg = 0, 0
    def rec(rem, last, acc, bl):
        global tot, sg
        if rem == 0:
            tot += 1
            sg += (-1) ** bl
            return
        for q in range(1, rem + 1):
            if last == 0 or gcd(last, q) == 1:
                rec(rem - q, q, acc + [q], bl + max(0, q - last))
    rec(n, 0, [], 0)
    brute.append((tot, sg))
ok &= [b[0] for b in brute] == by_area[1:13] and [b[1] for b in brute] == s_area[1:13]
print(f"[7] totient castles of area n = A167606(n), n <= 30, and with the signed count against brute force "
      f"for n <= 12: {ok}")
print(f"[7] by area, n = 1..16: {by_area[1:17]}")
print(f"[7] signed by area, n = 1..16: {s_area[1:17]}")
print(f"[7] even-block by area, n = 1..16: {[(a + s) // 2 for a, s in zip(by_area[1:17], s_area[1:17])]}")
print(f"[7] a(200)/a(199) = {by_area[200] / by_area[199]:.13f}, against Kotesovec's d = 1.8780154065731862")
for h in range(2, 8):
    print(f"[7] strips with coprime neighbors on 1..{h}, w = 1..10: {strips(h, 10)}")
