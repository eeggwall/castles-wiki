# Feistel ciphers on castles: Black-Rogaway (2002) generalized Feistel and cycle walking, Morris-Rogaway-Stegers (2009) Thorp shuffle.
# Checks the column-half reading of the generalized-Feistel cipher, cycle walking from the skylines onto the castles of
# height h, the cost of the walk, both papers' security bounds at the Project Euler size (w, h) = (13, 10), and the Thorp/Feistel identity.
# Symbols as on the wiki: N the domain size, N' the larger domain, N_left and N_right the two half sizes (the paper's a and b),
# nu the number of queries, t the number of rounds, r the pass parameter of Morris-Rogaway-Stegers.
import random
from itertools import permutations, product
from math import ceil, factorial, isqrt, log2

import numpy as np
from scipy.sparse import csr_matrix

ok_all = True
random.seed(502)


def check(label, cond):
    global ok_all
    ok_all &= bool(cond)
    print(label, bool(cond))


def to_int(c, h):                          # skyline -> integer, column 1 the least significant base-h digit
    return sum((ci - 1) * h ** i for i, ci in enumerate(c))


def to_sky(m, h, w):
    return tuple(m // h ** i % h + 1 for i in range(w))


def is_castle(c, h):                       # castle of height h: some column reaches h
    return max(c) == h


def A(w, h):                               # the number of castles of width w and height h
    return h ** w - (h - 1) ** w


def fe(m, n1, n2, fs):                     # Black-Rogaway Fig. 3, fe[R, a, b] with a = n1, b = n2
    L, R = m % n1, m // n1
    for j, f in enumerate(fs, start=1):
        tmp = (L + f(R)) % (n1 if j % 2 else n2)
        L, R = R, tmp
    return n1 * L + R if len(fs) % 2 else n1 * R + L


def fe_inv(m, n1, n2, fs):
    if len(fs) % 2:
        R, L = m % n1, m // n1
    else:
        L, R = m % n1, m // n1
    for j in range(len(fs), 0, -1):
        tmp = (R - fs[j - 1](L)) % (n1 if j % 2 else n2)
        R, L = L, tmp
    return n1 * R + L


def random_fn(size_in, top):
    table = [random.randrange(top) for _ in range(size_in)]
    return lambda x: table[x]


def cycles(perm):                          # perm: dict point -> image
    seen, out = set(), []
    for s in perm:
        if s in seen:
            continue
        cyc, x = [], s
        while x not in seen:
            seen.add(x)
            cyc.append(x)
            x = perm[x]
        out.append(cyc)
    return out


def canon(cycs):                           # cycles as a set of rotation-normalized tuples
    out = set()
    for c in cycs:
        if c:
            i = c.index(min(c))
            out.add(tuple(c[i:] + c[:i]))
    return out


# [1] the generalized-Feistel cipher on the skylines {1, ..., h}^w, split into its column halves
print("[1] Fe[t, N_left, N_right] with N_left = h^ceil(w/2), N_right = h^floor(w/2) on the skylines {1, ..., h}^w, t = 3, 4, 5")
good = True
for (w, h) in [(4, 3), (5, 3), (6, 2), (5, 4), (7, 2)]:
    n1, n2 = h ** ceil(w / 2), h ** (w // 2)
    for m in range(h ** w):
        c = to_sky(m, h, w)
        good &= to_sky(m % n1, h, ceil(w / 2)) == c[:ceil(w / 2)] and to_sky(m // n1, h, w // 2) == c[ceil(w / 2):]
    for R in (3, 4, 5):
        fs = [random_fn(max(n1, n2), 2 ** 20) for _ in range(R)]
        img = [fe(m, n1, n2, fs) for m in range(h ** w)]
        good &= sorted(img) == list(range(h ** w)) and all(fe_inv(img[m], n1, n2, fs) == m for m in range(h ** w))
check("    (w, h) = (4, 3), (5, 3), (6, 2), (5, 4), (7, 2): m mod N_left is the first ceil(w/2) columns, floor(m/N_left) the rest; fe is a permutation of [0, h^w - 1] inverted by fe^-1:", good)

# [2] cycle walking onto the castles of height h
print("[2] cycle walking from Fe onto the castles of height h")
good = True
for (w, h) in [(4, 3), (5, 3), (6, 2), (5, 4)]:
    n1, n2 = h ** ceil(w / 2), h ** (w // 2)
    fs = [random_fn(max(n1, n2), 2 ** 20) for _ in range(4)]
    E = {m: fe(m, n1, n2, fs) for m in range(h ** w)}
    V = {m for m in range(h ** w) if is_castle(to_sky(m, h, w), h)}
    Cy = {}
    for m in V:
        x = E[m]
        while x not in V:
            x = E[x]
        Cy[m] = x
    good &= sorted(Cy.values()) == sorted(V)
    erased = [[x for x in cyc if x in V] for cyc in cycles(E)]
    good &= canon(cycles(Cy)) == canon(erased)
check("    (w, h) = (4, 3), (5, 3), (6, 2), (5, 4), t = 4: the walk is a permutation of the castles of height h whose cycles are the cycles of Fe with the other skylines erased:", good)

# [3] Black-Rogaway Theorem 1: every permutation of the domain arises equally often
print("[3] induced permutations of an N-point domain inside an N'-point set (u = N', k = N below)")
good = True
for u, k in [(6, 3), (7, 4), (6, 2)]:
    counts = {}
    for p in permutations(range(u)):
        ind = []
        for m in range(k):
            x = p[m]
            while x >= k:
                x = p[x]
            ind.append(x)
        counts[tuple(ind)] = counts.get(tuple(ind), 0) + 1
    good &= len(counts) == factorial(k) and set(counts.values()) == {factorial(u) // factorial(k)}
    print(f"    u = {u}, k = {k}: {len(counts)} permutations, each from {sorted(set(counts.values()))} of the {factorial(u)}")
check("    every permutation of the domain arises from exactly u!/k! permutations:", good)

# [4] the length of a walk
print("[4] walk lengths")
good = True
for u, k in [(6, 3), (7, 4), (7, 2)]:
    tot = 0
    for p in permutations(range(u)):
        for m in range(k):
            x, steps = p[m], 1
            while x >= k:
                x, steps = p[x], steps + 1
            tot += steps
    mean = tot / (factorial(u) * k)
    good &= abs(mean - (u + 1) / (k + 1)) < 1e-12
    print(f"    u = {u}, k = {k}: mean calls over all permutations and starts {mean:.6f}, (u + 1)/(k + 1) = {(u + 1) / (k + 1):.6f}")
for (w, h) in [(5, 3), (6, 3), (5, 4)]:
    n1, n2 = h ** ceil(w / 2), h ** (w // 2)
    fs = [random_fn(max(n1, n2), 2 ** 20) for _ in range(4)]
    E = {m: fe(m, n1, n2, fs) for m in range(h ** w)}
    V = {m for m in range(h ** w) if is_castle(to_sky(m, h, w), h)}
    tot = 0
    for m in V:
        x, steps = E[m], 1
        while x not in V:
            x, steps = E[x], steps + 1
        tot += steps
    on = sum(len(c) for c in cycles(E) if any(x in V for x in c))
    good &= tot == on <= h ** w
check("    for the uniform permutation the mean is (u + 1)/(k + 1); for any one permutation the walks from the castles cover each cycle meeting them exactly once:", good)

# [5] the castle counts and the cost of the walk
print("[5] A(w, h) = h^w - (h - 1)^w and the cost of walking from the h^w skylines onto the castles of height h")
good = True
for (w, h) in [(10, 2), (8, 3), (7, 4), (6, 5)]:
    good &= sum(1 for c in product(range(1, h + 1), repeat=w) if is_castle(c, h)) == A(w, h)
check("    A(w, h) agrees with enumeration at (10, 2), (8, 3), (7, 4), (6, 5):", good)
for (w, h) in [(10, 2), (8, 3), (7, 4), (6, 5), (13, 10)]:
    print(f"    (w, h) = ({w}, {h}): h^w = {h ** w}, A = {A(w, h)}, share {A(w, h) / h ** w:.4f}, expected calls (h^w + 1)/(A + 1) = {(h ** w + 1) / (A(w, h) + 1):.4f}")

# [6] Black-Rogaway Theorem 2 at (13, 10)
print("[6] Theorem 2 (PRP form) at (w, h) = (13, 10), n = 64")
N = A(13, 10)
n = 64


def br_bound(nu, n1, n2, surplus):
    return ((nu + surplus) ** 2 + nu ** 2) / 2 ** (n + 1) * (ceil(2 ** n / n1) + ceil(2 ** n / n2))


def nu_half(n1, n2, surplus):
    lo, hi = 0, 10 ** 15
    while hi - lo > 1:
        mid = (lo + hi) // 2
        lo, hi = (mid, hi) if br_bound(mid, n1, n2, surplus) <= 0.5 else (lo, mid)
    return lo


nu_a = nu_half(10 ** 7, 10 ** 6, 0)
print(f"    (a) all skylines, N_left = 10^7, N_right = 10^6, no surplus: bound <= 1/2 up to nu = {nu_a} (2^{log2(nu_a):.2f})")
s_b = 10 ** 13 - N
print(f"    (b) the castles of height 10 inside [0, 10^13 - 1] directly: surplus {s_b}, bound at nu = 1 is {br_bound(1, 10 ** 7, 10 ** 6, s_b):.3e}")
r = isqrt(N - 1) + 1
s_sq = r * r - N
print(f"    (c) the castles ranked, N_left = N_right = ceil(sqrt(A)) = {r}: surplus {s_sq}, bound at nu = 1 is {br_bound(1, r, r, s_sq):.3e}")
s_c, a_c = min((a * (-(-N // a)) - N, a) for a in range(r - 200000, r + 1))
b_c = -(-N // a_c)
nu_c = nu_half(a_c, b_c, s_c)
print(f"    (d) the castles ranked, N_left = {a_c}, N_right = {b_c} (least surplus for N_left within 200000 below sqrt(A)): surplus {s_c}, bound <= 1/2 up to nu = {nu_c} (2^{log2(nu_c):.2f})")
ex = br_bound(0, 185360, 185368, 185360 * 185368 - 2 ** 35)
print(f"    (e) the paper's example k = 2^35, a = 185360, b = 185368: ab - k = {185360 * 185368 - 2 ** 35}, bound at nu = 0 is {ex:.0f}")
check("    (a) and (d) top out between 2^9 and 2^10 queries; (b), (c) and (e) exceed 1:",
      600 < nu_a < 900 and 600 < nu_c < 900 and br_bound(1, 10 ** 7, 10 ** 6, s_b) > 1 and br_bound(1, r, r, s_sq) > 1 and ex > 1)

# [7] the Thorp shuffle is maximally unbalanced Feistel at N = 2^n
print("[7] Thorp round vs maximally unbalanced Feistel")
good = True
for nb in range(2, 9):
    Nn = 2 ** nb
    coin = [random.randrange(2) for _ in range(Nn // 2)]
    for x in range(Nn):
        thorp = 2 * x + coin[x] if x < Nn // 2 else 2 * (x - Nn // 2) + 1 - coin[x - Nn // 2]
        top, low = x >> (nb - 1), x & (Nn // 2 - 1)
        good &= thorp == (low << 1) | (top ^ coin[low])
check("    for n = 2..8 the Thorp move equals the Feistel round that moves the first bit to the end and flips it when f of the other n - 1 bits is 1:", good)

# [8] Morris-Rogaway-Stegers Theorem 1 against the exact projected chain, N = 64, nu = 2
print("[8] Theorem 1 at N = 64 (n = 6), two cards: exact worst-case total variation after r(2n - 1) rounds")
nb, Nn = 6, 64
H = Nn // 2
states = [(a, b) for a in range(Nn) for b in range(Nn) if a != b]
idx = {s: i for i, s in enumerate(states)}
rows, cols, vals = [], [], []
for (a, b), i in idx.items():
    xa, xb, ba, bb = a % H, b % H, a // H, b // H
    if xa == xb:
        for c in (0, 1):
            rows.append(i); cols.append(idx[(2 * xa + (c ^ ba), 2 * xb + (c ^ bb))]); vals.append(0.5)
    else:
        for ca in (0, 1):
            for cb in (0, 1):
                rows.append(i); cols.append(idx[(2 * xa + (ca ^ ba), 2 * xb + (cb ^ bb))]); vals.append(0.25)
P = csr_matrix((vals, (rows, cols)), shape=(len(states), len(states)))
D = np.eye(len(states))
good, t = True, 0
for rr in range(1, 5):
    while t < rr * (2 * nb - 1):
        D = (P.T @ D.T).T
        t += 1
    tv = 0.5 * np.abs(D - 1 / len(states)).sum(axis=1).max()
    bound = 2 / (rr + 1) * (4 * nb * 2 / Nn) ** rr
    good &= tv <= bound
    print(f"    r = {rr}, {t} rounds: exact {tv:.3e}, bound {bound:.3e}")
check("    the exact distance stays below the bound:", good)

# [9] Theorem 5 (CCA) at (w, h) = (13, 10)
print("[9] Theorem 5: the query count at CCA advantage 1/2 with 16 passes (16n rounds, r = floor(16n/(4n - 2)))")


def lg_nu_cca(nb, passes):
    rr = (passes * nb) // (4 * nb - 2)
    # (2 nu/(r + 1)) (4 n nu / 2^n)^r = 1/2
    return (log2((rr + 1) / 4) + rr * nb - rr * log2(4 * nb)) / (rr + 1), rr


l40, r40 = lg_nu_cca(40, 16)
l43, r43 = lg_nu_cca(43, 16)
print(f"    N = 2^40: r = {r40}, lg nu = {l40:.2f};  N = 2^43: r = {r43}, lg nu = {l43:.2f}")
print(f"    the castles of height 10 ranked into [0, 2^43): 2^43 / A(13, 10) = {2 ** 43 / N:.4f}, expected calls (2^43 + 1)/(A + 1) = {(2 ** 43 + 1) / (N + 1):.4f}")
print(f"    against the column halves of [6](a): lg nu {l43:.2f} - {log2(nu_a):.2f} = {l43 - log2(nu_a):.2f}")
check("    N = 2^40 gives 2^26.2 (the paper's example); N = 2^43 gives about 2^28.5, and 2^42 < A(13, 10) <= 2^43:",
      abs(l40 - 26.2) < 0.05 and 28.4 < l43 < 28.6 and 2 ** 42 < N <= 2 ** 43)

print("ALL OK" if ok_all else "SOMETHING FAILED")
