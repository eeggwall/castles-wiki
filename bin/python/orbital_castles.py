# Orbital castles: the castles that repeat a period of N distinct heights from the first column, width >= 2N.
# Checks the counts, A001339, the rise per period, the block count, and the overlaps with other families and shape types.
from collections import Counter
from itertools import combinations, permutations, product
from math import comb, factorial, lcm

ok_all = True


def check(label, cond):
    global ok_all
    ok_all &= bool(cond)
    print(label, bool(cond))


def order(c):                              # the order N of an orbital castle, or None
    for N in range(1, len(c) // 2 + 1):
        if len(set(c[:N])) == N and all(c[i + N] == c[i] for i in range(len(c) - N)):
            return N
    return None


def blocks(c):
    return c[0] + sum(max(0, c[i] - c[i - 1]) for i in range(1, len(c)))


def rise(per):                             # the cyclic rise of a period, the step back to the start included
    return sum(max(0, per[(i + 1) % len(per)] - per[i]) for i in range(len(per)))


def orbitals(w, h):                        # every orbital castle of width w and height h, from its period
    for N in range(1, min(h, w // 2) + 1):
        for rest in combinations(range(1, h), N - 1):
            for per in permutations(rest + (h,)):
                yield N, per, tuple(per[i % N] for i in range(w))


def by_order(w, h, N):
    return comb(h - 1, N - 1) * factorial(N) if 1 <= N <= h and w >= 2 * N else 0


def zigzag_type(c):                        # the differences alternate in sign
    d = [b - a for a, b in zip(c, c[1:])]
    return all(x != 0 for x in d) and all(x * y < 0 for x, y in zip(d, d[1:]))


def alt_period(per):                       # the cyclic steps of the period alternate in sign
    N = len(per)
    d = [per[(i + 1) % N] - per[i] for i in range(N)]
    return N >= 2 and N % 2 == 0 and all(d[i] * d[(i + 1) % N] < 0 for i in range(N))


# [1] brute force over every castle: the orbital ones are the ones built from a period, C(h - 1, N - 1) N! of order N
ok1 = True
for h, wmax in [(1, 10), (2, 10), (3, 10), (4, 10), (5, 8)]:
    for w in range(2, wmax + 1):
        brute = Counter(order(c) for c in product(range(1, h + 1), repeat=w) if max(c) == h)
        built = Counter(N for N, _, _ in orbitals(w, h))
        ok1 &= all(brute[N] == built[N] == by_order(w, h, N) for N in range(1, h + 1))
        ok1 &= len(set(c for _, _, c in orbitals(w, h))) == sum(built.values())
check('[1] every castle with h <= 4, w <= 10 and h = 5, w <= 8: the orbital castles of order N number C(h - 1, N - 1) N! '
      'when w >= 2N, and each comes from exactly one period:', ok1)

# [2] the total at width w >= 2h is A001339(h - 1) = sum_k (k + 1)! C(h - 1, k); the period is an arrangement containing h
A001339 = [1, 3, 11, 49, 261, 1631, 11743, 95901, 876809]                  # oeis.org/A001339, read 2026-10-31
tot = [sum(by_order(2 * h, h, N) for N in range(1, h + 1)) for h in range(1, 10)]
arr = [sum(1 for k in range(1, h + 1) for s in permutations(range(1, h + 1), k) if 1 in s) for h in range(1, 7)]
print('    A_orbital(w, h) for w >= 2h, h = 1..9:', tot)
print('    arrangements of {1, ..., h} containing 1, h = 1..6:', arr)
check('[2] A_orbital(w, h) = A001339(h - 1) for w >= 2h, h <= 9, and equals the arrangements of {1, ..., h} containing 1:',
      tot == A001339 and arr == tot[:6] and all(t == sum(factorial(k + 1) * comb(h - 1, k) for k in range(h)) for h, t in zip(range(1, 10), tot)))

# [3] the rise per period: max - min <= rise <= (top floor(N/2)) - (bottom floor(N/2)), with 2^(N-2) cyclic orders at the minimum
ok3 = True
for S in (s for r in range(2, 8) for s in combinations(range(1, 9), r)):
    N, top = len(S), max(S)
    rs = [rise((top,) + p) for p in permutations([x for x in S if x != top])]
    srt = sorted(S)
    ok3 &= min(rs) == srt[-1] - srt[0] and max(rs) == sum(srt[-(N // 2):]) - sum(srt[:N // 2]) and rs.count(min(rs)) == 2 ** (N - 2)
check('[3] every set of 2 to 7 heights from {1, ..., 8}: over its cyclic orders the rise runs from max - min to the top half '
      'minus the bottom half, and 2^(N - 2) cyclic orders reach the minimum:', ok3)
mm = [(N - 1, N * N // 4) for N in range(2, 8)]
check(f'    on the heights 1..N, N = 2..7, the minimum and maximum are N - 1 and floor(N^2/4): {mm}',
      all(min(rise((N,) + p) for p in permutations(range(1, N))) == a and max(rise((N,) + p) for p in permutations(range(1, N))) == b
          for N, (a, b) in zip(range(2, 8), mm)))
ex = (8, 1, 7, 2, 6, 3, 5)
rs = [rise((8,) + p) for p in permutations([1, 2, 3, 5, 6, 7])]
c21 = ex * 3
check(f'    (8, 1, 7, 2, 6, 3, 5) repeated to width 21: order {order(c21)}, rise {rise(ex)}, the largest of the 720 cyclic orders '
      f'of its heights ({rs.count(max(rs))} reach it), blocks {blocks(c21)}:', order(c21) == 7 and rise(ex) == max(rs) == 15 and blocks(c21) == 50)

# [4] the block count: w - 1 = qN + t steps give c_1 + q rise + (the rises of the first t steps); c_w + r rise for r whole periods from h
ok4 = True
for h in range(1, 6):
    for w in range(2, 13):
        for N, per, c in orbitals(w, h):
            q, t = divmod(w - 1, N)
            ok4 &= blocks(c) == c[0] + q * rise(per) + sum(max(0, c[i + 1] - c[i]) for i in range(t))
            if c[0] == h and w % N == 0:
                ok4 &= blocks(c) == c[-1] + (w // N) * rise(per)
check('[4] every orbital castle with h <= 5, w <= 12: blocks = c_1 + q rise + the rises of the first t steps, with '
      'w - 1 = qN + t, and blocks = c_w + r rise for r whole periods starting at height h:', ok4)

# [5] tree castles: the orbital tree castles are the two battlements (and (1, ..., 1) at h = 1)
ok5 = True
for h in range(1, 6):
    for w in range(2, 11):
        trees = sorted(c for _, _, c in orbitals(w, h) if all(min(a, b) == 1 for a, b in zip(c, c[1:])))
        want = [tuple(1 for _ in range(w))] if h == 1 else ([] if w < 4 else sorted([tuple((1, h)[i % 2] for i in range(w)), tuple((h, 1)[i % 2] for i in range(w))]))
        ok5 &= trees == want
check('[5] h <= 5, w <= 10: the orbital tree castles are (1, h, 1, h, ...) and (h, 1, h, 1, ...) for w >= 4, and (1, ..., 1) at h = 1:', ok5)

# [6] the gluing monoid: an orbital castle begins and ends at 1 iff c_1 = 1 and N divides w - 1; it is then k = (w - 1)/N >= 2
#     glued copies of the prime castle (c_1, ..., c_N, 1), C(h - 2, N - 2) (N - 1)! of order N >= 2, with blocks - 1 = k rise
ok6 = True
for h in range(2, 6):
    for w in range(4, 13):
        cnt = Counter()
        for N, per, c in orbitals(w, h):
            if c[0] == 1 and c[-1] == 1:
                cnt[N] += 1
                k = (w - 1) // N
                prime = per + (1,)
                glued = prime + sum((prime[1:] for _ in range(k - 1)), ())
                ok6 &= (w - 1) % N == 0 and k >= 2 and c == glued and 1 not in prime[1:-1] and blocks(c) - 1 == k * rise(per)
                ok6 &= (-1) ** (blocks(c) - 1) == ((-1) ** (blocks(prime) - 1)) ** k
        want = {N: comb(h - 2, N - 2) * factorial(N - 1) for N in range(2, min(h, w // 2) + 1) if (w - 1) % N == 0 and (w - 1) // N >= 2}
        ok6 &= dict(cnt) == want
check('[6] 2 <= h <= 5, 4 <= w <= 12: the orbital castles that begin and end at height 1 are the k-fold gluings, k = (w - 1)/N >= 2, '
      'of the prime castles (1, a_2, ..., a_N, 1) with distinct a_i, C(h - 2, N - 2) (N - 1)! of order N; blocks - 1 = k rise, '
      'and the sign is the prime\'s sign to the power k:', ok6)

# [7] the even-block orbital castles: each castle's parity depends on (w - 1) mod 2N, so the count repeats with period 2 lcm(1..h)
table = {h: [sum(1 for _, _, c in orbitals(w, h) if blocks(c) % 2 == 0) for w in range(2, 13)] for h in range(1, 7)}
for h, row in table.items():
    print(f'    h = {h}: A^e_orbital(w, h), w = 2..12: {row}')
ok7 = True
for h in range(1, 6):
    P = 2 * lcm(*range(1, h + 1))
    seq = [sum(1 for _, _, c in orbitals(w, h) if blocks(c) % 2 == 0) for w in range(2 * h, 2 * h + 2 * P)]
    ok7 &= all(seq[i] == seq[i + P] for i in range(P))
    if h in (2, 3):                        # the shortest period is 4 at these heights
        ok7 &= all(seq[i] == seq[i + 4] for i in range(2 * P - 4)) and any(seq[i] != seq[i + 2] for i in range(2 * P - 2))
check('[7] h <= 5: from w = 2h on, A^e_orbital(w, h) repeats with period 2 lcm(1, ..., h), checked over two periods, '
      'and with shortest period 4 at h = 2 and 3:', ok7)

# [8] shape types: plateau-free, zig-zag, Zigzag, alternating, palindromic, two-level, fence-post, moated
ok8 = True
for h in range(1, 6):
    for w in range(2, 11):
        for N, per, c in orbitals(w, h):
            ok8 &= all(a != b for a, b in zip(c, c[1:])) == (N >= 2)
            ok8 &= all(abs(a - b) == 1 for a, b in zip(c, c[1:])) == (N == 2 and set(per) == {h - 1, h})
            ok8 &= zigzag_type(c) == alt_period(per)
            ok8 &= (w % 2 == 1 and c[0] > c[1] and zigzag_type(c)) == (w % 2 == 1 and alt_period(per) and per[0] > per[1])
            ok8 &= (c == c[::-1]) == (N == 1 or (N == 2 and w % 2 == 1))
            ok8 &= (len(set(c)) == 2) == (N == 2)
            ok8 &= all(c[i] == 1 for i in range(1, w, 2)) == (h == 1 or (N == 2 and per == (h, 1)))
            ok8 &= (c[0] == 1 and c[-1] == 1 and all(x >= 2 for x in c[1:-1])) == (c == (1, 1))
check('[8] every orbital castle with h <= 5, w <= 10: plateau-free iff N >= 2; zig-zag iff N = 2 on {h - 1, h}; Zigzag iff its '
      'period alternates around the cycle (so N is even); an alternating castle (odd width, a fall first) iff in addition the '
      'period starts on a fall; palindromic iff N = 1 or N = 2 at odd width; two-level iff N = 2; fence-post iff (h, 1, h, 1, ...) '
      'or h = 1; moated only (1, 1):', ok8)

# [9] the alternating periods: A000182(m) cyclic orders of 2m heights, so C(h - 1, 2m - 1) 2m A000182(m) Zigzag orbital castles of order 2m,
#     half of them starting on a fall
A000182 = [1, 2, 16, 272]                                                  # oeis.org/A000182, read 2026-10-31
alt = [sum(1 for p in permutations(range(1, 2 * m)) if alt_period((2 * m,) + p)) for m in range(1, 5)]
ok9 = alt == A000182
for h in range(1, 6):
    for w in range(2, 11):
        cnt = Counter(N for N, per, c in orbitals(w, h) if zigzag_type(c))
        ok9 &= all(cnt[N] == (comb(h - 1, N - 1) * N * A000182[N // 2 - 1] if N % 2 == 0 and w >= 2 * N else 0) for N in range(1, h + 1))
        alc = Counter(N for N, per, c in orbitals(w, h) if w % 2 == 1 and c[0] > c[1] and zigzag_type(c))  # alternating castles
        ok9 &= all(alc[N] == (comb(h - 1, N - 1) * (N // 2) * A000182[N // 2 - 1] if N % 2 == 0 and w % 2 == 1 and w >= 2 * N else 0) for N in range(1, h + 1))
for S in (s for r in (2, 4, 6) for s in combinations(range(1, 9), r)):   # at even order the largest rise: alternating, the top half above
    pers = [(S[-1],) + p for p in permutations(S[:-1])]
    best = max(rise(p) for p in pers)
    peaks = lambda p: {p[i] for i in range(len(p)) if p[i] > p[i - 1] and p[i] > p[(i + 1) % len(p)]}
    ok9 &= all((rise(p) == best) == (alt_period(p) and peaks(p) == set(S[len(S) // 2:])) for p in pers)
ex4 = sorted(c for N, per, c in orbitals(9, 4) if N == 4 and c[0] > c[1] and zigzag_type(c))
ok9 &= ex4 == sorted([(4, 1, 3, 2) * 2 + (4,), (4, 2, 3, 1) * 2 + (4,), (3, 1, 4, 2) * 2 + (3,), (3, 2, 4, 1) * 2 + (3,)])
ok9 &= Counter(N for N, per, c in orbitals(9, 4) if c[0] > c[1] and zigzag_type(c)) == Counter({2: 3, 4: 4})
print('    alternating cyclic orders of 2, 4, 6, 8 heights:', alt)
print('    the alternating orbital castles of order 4 at w = 9, h = 4:', ex4)
check('[9] the alternating cyclic orders of 2m heights are A000182(m) for m <= 4; the Zigzag orbital castles of order 2m number '
      'C(h - 1, 2m - 1) 2m A000182(m) for h <= 5, w <= 10, and the alternating ones C(h - 1, 2m - 1) m A000182(m) at odd width; '
      'and for every set of 2, 4 or 6 heights from {1, ..., 8}, the periods of largest rise are the alternating ones whose '
      'heights above both neighbors are the top half; at w = 9, h = 4, three alternating orbital castles of order 2 and the four listed of order 4:', ok9)

# [10] up to the starting column, an orbital castle of width w >= 2h is a cyclic order: A000522(h - 1) of them
A000522 = [1, 2, 5, 16, 65, 326, 1957, 13700]                              # oeis.org/A000522, read 2026-10-31
cyc = [sum(comb(h - 1, N - 1) * factorial(N - 1) for N in range(1, h + 1)) for h in range(1, 9)]
ok10 = cyc == A000522
for h in range(1, 7):
    classes = {min(per[i:] + per[:i] for i in range(N)) for N, per, c in orbitals(2 * h, h)}
    ok10 &= len(classes) == cyc[h - 1]
check('[10] the orbital castles of width w >= 2h up to the rotation of their period number A000522(h - 1) for h <= 8, '
      'and by grouping the periods for h <= 6:', ok10)

# [11] the moated castles, (1, X, 1) with no height 1 in X, are the prime castles: A(w - 2, h - 1) of them for w >= 3
ok11 = True
for h in range(2, 6):
    for w in range(3, 11):
        n = sum(1 for c in product(range(1, h + 1), repeat=w) if max(c) == h and c[0] == 1 and c[-1] == 1 and all(x >= 2 for x in c[1:-1]))
        ok11 &= n == (h - 1) ** (w - 2) - (h - 2) ** (w - 2)
check('[11] 2 <= h <= 5, 3 <= w <= 10: the moated castles number (h - 1)^(w - 2) - (h - 2)^(w - 2) = A(w - 2, h - 1):', ok11)

print('all checks passed:', ok_all)
