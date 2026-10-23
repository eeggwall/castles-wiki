# Column generating functions of A283595 (Motzkin prefixes of length n and height k):
# Sum_n T(n,k) z^n = z^k/(R_k R_{k+1}), R_{2j} = P_j - z P_{j-1}, R_{2j+1} = P_{j+1} - z^2 P_{j-1},
# P_k the polynomials of A097862 (P_{-1} = 0, P_0 = 1, P_k = (1-z) P_{k-1} - z^2 P_{k-2}).
# Also R_k = Prod_{i <= k odd} (1 - (1 + 2cos(i pi/(k+1))) z), and the steps of the proof.
# Draft: raw/oeis-pe502/xrefs/A283595-column-gf.md.  Needs mpmath; A283595 b-file path as argv[1] (optional).
import sys
from mpmath import mp, mpf, cos, sin, pi

N = 140  # rows 0..N, as in the b-file
K = 40   # range for the polynomial and eigenvector checks

def mul(a, b):
    c = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i + j] += x * y
    return c

def add(a, b):
    n = max(len(a), len(b))
    return [(a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0) for i in range(n)]

def scale(a, s, shift=0):
    return [0] * shift + [s * x for x in a]

def trim(a):
    while len(a) > 1 and a[-1] == 0:
        a = a[:-1]
    return a

def series_div(num, den, n):  # first n coefficients of num/den, den[0] = 1
    assert den[0] == 1
    out = []
    for m in range(n):
        v = (num[m] if m < len(num) else 0) - sum(den[j] * out[m - j] for j in range(1, min(m, len(den) - 1) + 1))
        out.append(v)
    return out

def poly_divmod(a, b):  # exact division over the integers when possible; b[0] = 1 is not needed
    a = trim(a[:]); b = trim(b)
    q = [0] * max(1, len(a) - len(b) + 1)
    while len(a) >= len(b) and any(a):
        s, d = a[-1] // b[-1], len(a) - len(b)
        assert s * b[-1] == a[-1]
        q[d] = s
        a = trim(add(a, scale(b, -s, d)))
    return q, a

P = {-1: [0], 0: [1], 1: [1, -1]}
for k in range(2, 2 * N + 4):
    P[k] = add(mul([1, -1], P[k - 1]), scale(P[k - 2], -1, 2))

def R(k):
    j = k // 2
    return trim(add(P[j], scale(P[j - 1], -1, 1))) if k % 2 == 0 else trim(add(P[j + 1], scale(P[j - 1], -1, 2)))

# 1. Brute force: Motzkin prefixes by (length, height), dynamic program over (current level, maximum level)
T = [[0] * (n + 1) for n in range(N + 1)]
state = {(0, 0): 1}
for n in range(N + 1):
    for (y, m), c in state.items():
        T[n][m] += c
    nxt = {}
    for (y, m), c in state.items():
        for d in (-1, 0, 1):
            if y + d >= 0:
                key = (y + d, max(m, y + d))
                nxt[key] = nxt.get(key, 0) + c
    state = nxt
print(f"brute force: rows 0..{N}; rows 0..5 = {T[:6]}")

if len(sys.argv) > 1:
    b = [int(l.split()[1]) for l in open(sys.argv[1]) if l.strip() and not l.startswith('#')]
    flat = [t for row in T for t in row]
    assert b == flat, "b-file differs from brute force"
    print(f"b-file: all {len(b)} terms (rows 0..{N}) == brute force")

# 2. The column g.f. z^k/(R_k R_{k+1}) against the brute-force columns, every k <= N
for k in range(N + 1):
    col = series_div([1], mul(R(k), R(k + 1)), N - k + 1)
    assert col == [T[n][k] for n in range(k, N + 1)], k
    assert len(R(k)) - 1 == (k + 1) // 2, k  # deg R_k = ceil(k/2)
print(f"column g.f. z^k/(R_k R_(k+1)) == columns k = 0..{N}, rows up to {N}; deg R_k = ceil(k/2)")

# 3. Prefixes of height at most k: g.f. Sum_{j=0..k} z^j P_{k-j} / P_{k+1}; it reduces to a proper fraction over R_{k+1}
for k in range(K + 1):
    num = [0]
    for j in range(k + 1):
        num = add(num, scale(P[k - j], 1, j))
    cum = [sum(T[n][:k + 1]) for n in range(N + 1)]
    assert series_div(num, P[k + 1], N + 1) == cum, k
    cof, r = poly_divmod(P[k + 1], R(k + 1))
    assert r == [0], k
    Nk, r = poly_divmod(num, cof)
    assert r == [0] and len(trim(Nk)) - 1 < len(R(k + 1)) - 1, k
print(f"height <= k: Sum z^j P_(k-j)/P_(k+1) == brute force, and reduces to N_k/R_(k+1), deg N_k < deg R_(k+1), k <= {K}")

# 4. The factorizations P_{2j+1} = P_j R_{2j+1}, P_{2j} = R_{2j} (P_j + z P_{j-1})
for j in range(K + 1):
    assert trim(P[2 * j + 1]) == trim(mul(P[j], R(2 * j + 1))), j
    assert trim(P[2 * j]) == trim(mul(R(2 * j), add(P[j], scale(P[j - 1], 1, 1)))), j
print(f"P_(2j+1) = P_j R_(2j+1) and P_(2j) = R_(2j) (P_j + z P_(j-1)), j <= {K}")

# 5. R_k = Prod_{i <= k odd} (1 - (1 + 2cos(i pi/(k+1))) z), P_k the same product over all i <= k;
#    eigenvectors sin(i j pi/(k+2)), j = 1..k+1, sum to 0 for even i and not for odd i; no odd i gives eigenvalue 0
mp.dps = 50
def prod(k, odd_only):
    p = [mpf(1)]
    for i in range(1, k + 1):
        if not odd_only or i % 2:
            lam = 1 + 2 * cos(i * pi / (k + 1))
            p = [(p[t] if t < len(p) else 0) - (lam * p[t - 1] if t >= 1 else 0) for t in range(len(p) + 1)]
    return p
for k in range(1, K + 1):
    for odd_only, target in ((True, R(k)), (False, trim(P[k]))):
        p = prod(k, odd_only)
        while len(p) > len(target) and abs(p[-1]) < mpf(10) ** -40:
            p = p[:-1]
        assert len(p) == len(target) and all(abs(p[t] - target[t]) < mpf(10) ** -35 for t in range(len(p))), (k, odd_only)
    for i in range(1, k + 2):
        s = sum(sin(i * j * pi / (k + 2)) for j in range(1, k + 2))
        assert (abs(s) < mpf(10) ** -40) == (i % 2 == 0), (k, i)
        if i % 2:
            assert abs(1 + 2 * cos(i * pi / (k + 2))) > mpf(10) ** -40, (k, i)
print(f"R_k == product over odd i, P_k == product over all i, k <= {K}; eigenvector sums 0 exactly at even i; odd-i eigenvalues nonzero")

# 6. Column 2 is A094706(n-1): g.f. x/((1-2x-x^2)(1-2x))
a094706 = series_div([0, 1], mul([1, -2, -1], [1, -2]), N)
assert [T[n][2] for n in range(2, N + 1)] == a094706[1:N], "column 2"
print(f"column 2: T(n,2) == A094706(n-1) for n = 2..{N}")

# 7. The draft's Python program (walks on {0..k}, height at most k minus height at most k-1) against the brute force
def H(n, k):
    v = [1] + [0]*k
    for _ in range(n): v = [(v[j-1] if j else 0) + v[j] + (v[j+1] if j < k else 0) for j in range(k+1)]
    return sum(v)
def T_prog(n, k): return H(n, k) - H(n, k-1) if k else 1
assert all(T_prog(n, k) == T[n][k] for n in range(N + 1) for k in range(n + 1))
print(f"Python program: T(n,k) == brute force for rows 0..{N}")
