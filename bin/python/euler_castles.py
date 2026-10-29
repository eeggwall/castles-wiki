# Euler castles: the castles whose heights fall by 0 or 1 at each step and end at height 1.
# Their rows are the partitions into distinct parts (A000009), their block count is the number
# of parts, so the signed count by area is Euler's pentagonal series (A010815); Franklin's
# involution as a castle move on the summit and the slope, which keeps the area and the
# semi-perimeter, flips the block parity, and leaves one pentagonal castle at each pentagonal area.
# Page: wiki/pages/euler-castles.md.  Columns are 0-based here.
from itertools import product
from math import comb
from collections import Counter

# OEIS data, offset 0 (read 2026-10-28).
A000009 = [1, 1, 1, 2, 2, 3, 4, 5, 6, 8, 10, 12, 15, 18, 22, 27, 32, 38, 46, 54, 64, 76, 89, 104, 122]
A010815 = [1, -1, -1, 0, 0, 1, 0, 1, 0, 0, 0, 0, -1, 0, 0, -1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0]
A067661 = [1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 5, 6, 7, 9, 11, 13, 16, 19, 23, 27, 32, 38, 45, 52, 61, 71, 83]
A067659 = [0, 1, 1, 1, 1, 1, 2, 2, 3, 4, 5, 6, 8, 9, 11, 14, 16, 19, 23, 27, 32, 38, 44, 52, 61, 71, 82]
A000045 = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765]
A010892 = [1, 1, 0, -1, -1, 0, 1, 1, 0, -1, -1, 0, 1, 1, 0, -1, -1, 0, 1, 1, 0, -1, -1, 0, 1, 1, 0, -1, -1]


def blocks(c):
    return sum(max(0, b - a) for a, b in zip((0,) + c, c))


def is_euler(c):
    return c[-1] == 1 and all(a - b in (0, 1) for a, b in zip(c, c[1:]))


def rows(c):
    """Row lengths, bottom row first."""
    return tuple(sum(1 for x in c if x >= r) for r in range(1, max(c) + 1))


def from_rows(lam):
    """The skyline whose row r has length lam[r - 1], rows left-aligned."""
    return tuple(sum(1 for l in lam if l >= j) for j in range(1, lam[0] + 1))


def distinct_partitions(n, top=None):
    """Partitions of n into distinct parts, largest first."""
    top = n if top is None else top
    if n == 0:
        yield ()
        return
    for p in range(min(n, top), 0, -1):
        for rest in distinct_partitions(n - p, p - 1):
            yield (p,) + rest


def euler_by_area(n):
    return [from_rows(lam) for lam in distinct_partitions(n)]


def series(n, sign):
    """Coefficients of prod_{k >= 1} (1 + sign q^k) up to q^n."""
    a = [1] + [0] * n
    for k in range(1, n + 1):
        for m in range(n, k - 1, -1):
            a[m] += sign * a[m - k]
    return a


def summit_slope(c):
    """s = the number of columns of height h, sigma = the length of the final run (m, m - 1, ..., 1)."""
    h, w = c[0], len(c)
    s = sum(1 for x in c if x == h)
    sigma = 1
    while sigma < w and c[w - 1 - sigma] == sigma + 1:
        sigma += 1
    return s, sigma


def franklin(c):
    """Franklin's move on an Euler castle; None on the pentagonal castles."""
    h, w = c[0], len(c)
    s, sigma = summit_slope(c)
    if sigma == h and s in (h, h + 1):
        return None
    d = list(c) + [0]
    if s <= sigma:                                 # summit row onto the diagonal: lower the summit,
        for i in range(s):                         # raise the last s - 1 columns, add a column of height 1
            d[i] -= 1
            d[w - i] += 1
    else:                                          # diagonal onto a new summit row: lower the last
        for i in range(sigma):                     # sigma columns, raise the first sigma
            d[i] += 1
            d[w - 1 - i] -= 1
    return tuple(x for x in d if x > 0)


def franklin_partition(parts):
    """Franklin's rule as he states it, on a partition written in ascending order."""
    p = list(parts)
    r, n = p[0], 1
    while n < len(p) and p[-n - 1] == p[-n] - 1:
        n += 1
    if n == len(p) and r in (n, n + 1):
        return None
    if r <= n:
        q = p[1:]
        for i in range(len(q) - r, len(q)):
            q[i] += 1
        return tuple(q)
    q = p[:]
    for i in range(len(q) - n, len(q)):
        q[i] -= 1
    return tuple([n] + q)


def pentagonal(k, plus):
    """The unmatched castle at area k(3k - 1)/2 (plus = False) or k(3k + 1)/2 (plus = True)."""
    return tuple([k] * (k + (1 if plus else 0)) + list(range(k - 1, 0, -1)))


N = 40

# [1] definition, rows, area
ok = True
for w in range(1, 9):
    for h in range(1, 6):
        for c in product(range(1, h + 1), repeat=w):
            if max(c) != h or not is_euler(c):
                continue
            lam = rows(c)
            ok &= all(a > b for a, b in zip(lam, lam[1:])) and from_rows(lam) == c
            ok &= blocks(c) == h == len(lam) and lam[0] == w and sum(c) == sum(lam)
for n in range(1, N + 1):
    cs = euler_by_area(n)
    ok &= len(set(cs)) == len(cs) and all(is_euler(c) and sum(c) == n for c in cs)
print(f"[1] every Euler castle with w <= 8, h <= 5 has distinct row lengths, rows = its h blocks, bottom row = w; "
      f"row lengths <-> distinct-part partitions, one-to-one onto Euler castles of area n <= {N}: {ok}")
ex = (3, 3, 2, 1, 1)
print(f"[1] example {ex}: rows {rows(ex)}, blocks {blocks(ex)}, area {sum(ex)}")

# [2] counts by area, by cell, by width, by semi-perimeter
by_area = [1] + [len(euler_by_area(n)) for n in range(1, N + 1)]
ok = by_area == series(N, +1) and by_area[:len(A000009)] == A000009
print(f"[2] Euler castles of area n = prod (1 + q^k) = A000009(n), n <= {N}: {ok}")
print(f"[2] by area, n = 1..16: {by_area[1:17]}")
ok = True
cells = Counter()
for w in range(1, 9):
    for h in range(1, 6):
        cnt = sum(1 for c in product(range(1, h + 1), repeat=w) if max(c) == h and is_euler(c))
        ok &= cnt == comb(w - 1, h - 1)
for n in range(1, N + 1):
    for c in euler_by_area(n):
        cells[(len(c), c[0])] += 1
ok &= all(cells[(w, h)] == comb(w - 1, h - 1) for w in range(1, 10) for h in range(1, 10)
          if w * (w + 1) // 2 <= N)
print(f"[2] A_Euler(w, h) = C(w - 1, h - 1): brute force over all skylines w <= 8, h <= 5, "
      f"and from the area lists for w(w + 1)/2 <= {N}: {ok}")
fib = [0, 1]
while len(fib) < 30:
    fib.append(fib[-1] + fib[-2])
ok = all(sum(comb(s - h - 1, h - 1) for h in range(1, s) if s - h >= 1) == fib[s - 1] for s in range(2, 28))
semi = Counter()
for n in range(1, N + 1):
    for c in euler_by_area(n):
        semi[len(c) + blocks(c)] += 1
ok &= all(semi[s] == fib[s - 1] for s in range(2, 10)) and fib[:len(A000045)] == A000045
print(f"[2] by width 2^(w-1) (sum of the cell counts); by semi-perimeter s = w + h: F(s - 1), "
      f"s <= 27 from the cell counts and s <= 9 from the castles: {ok}")

# [3] the parity: Euler's pentagonal series
signed = [0] * (N + 1)
even = [0] * (N + 1)
odd = [0] * (N + 1)
for n in range(1, N + 1):
    for c in euler_by_area(n):
        if blocks(c) % 2 == 0:
            even[n] += 1
        else:
            odd[n] += 1
    signed[n] = even[n] - odd[n]
pent = {}
for k in range(1, 10):
    pent[k * (3 * k - 1) // 2] = (-1) ** k
    pent[k * (3 * k + 1) // 2] = (-1) ** k
ok = all(signed[n] == pent.get(n, 0) for n in range(1, N + 1))
ok &= signed[1:] == series(N, -1)[1:] and signed[1:len(A010815)] == A010815[1:N + 1][:len(A010815) - 1]
print(f"[3] even - odd Euler castles of area n = (-1)^k at n = k(3k +- 1)/2, 0 otherwise, "
      f"= prod (1 - q^k) = A010815(n), n <= {N}: {ok}")
ok = even[1:27] == A067661[1:27] and odd[1:27] == A067659[1:27]
print(f"[3] even-block = A067661(n), odd-block = A067659(n), n <= 26: {ok}")
print(f"[3] even-block by area, n = 1..16: {even[1:17]}")
print(f"[3] odd-block by area,  n = 1..16: {odd[1:17]}")

# [4] Franklin's move on the skyline
ok = True
unmatched = {}
for n in range(1, N + 1):
    for c in euler_by_area(n):
        d = franklin(c)
        if d is None:
            unmatched.setdefault(n, []).append(c)
            continue
        ok &= is_euler(d) and sum(d) == n and franklin(d) == c and d != c
        ok &= (blocks(d) - blocks(c)) in (1, -1) and len(d) + blocks(d) == len(c) + blocks(c)
        lam = rows(c)
        ok &= franklin_partition(lam[::-1]) == rows(d)[::-1]
ok &= set(unmatched) == set(pent) & set(range(1, N + 1))
ok &= all(len(v) == 1 for v in unmatched.values())
ok &= all(unmatched[k * (3 * k - 1) // 2] == [pentagonal(k, False)] for k in range(1, 6))
ok &= all(unmatched[k * (3 * k + 1) // 2] == [pentagonal(k, True)] for k in range(1, 5))
print(f"[4] the move maps Euler castles to Euler castles of the same area, is its own inverse, changes the height "
      f"by 1, keeps w + blocks, and is Franklin's rule on the rows (ascending); undefined exactly once at each "
      f"pentagonal area, on (k^k, k-1, ..., 1) and (k^(k+1), k-1, ..., 1); n <= {N}: {ok}")
for parts in [(2, 3, 4, 6, 7), (3, 5, 8, 9), (3, 4, 5, 6), (6, 7, 8, 9), (4, 5, 6, 7), (5, 6, 7, 8)]:
    image = franklin_partition(parts)
    c = from_rows(parts[::-1])
    d = franklin(c)
    print(f"[4] Franklin's example {''.join(map(str, parts))} -> "
          f"{''.join(map(str, image)) if image else 'none'}; castle {c} -> {d}")
for c in [(3, 3, 2, 1, 1), (2, 2, 2, 1)]:
    print(f"[4] summit and slope of {c}: (s, sigma) = {summit_slope(c)}; move -> {franklin(c)}")

# [5] the signed count by area and semi-perimeter (Chapman 2000, Equation (7))
ok = True
for n in range(1, N + 1):
    by_s = Counter()
    for c in euler_by_area(n):
        by_s[len(c) + blocks(c)] += (-1) ** blocks(c)
    want = Counter()
    for k in range(1, 10):
        if k * (3 * k - 1) // 2 == n:
            want[3 * k - 1] += (-1) ** k
        if k * (3 * k + 1) // 2 == n:
            want[3 * k] += (-1) ** k
    ok &= +by_s == +want
print(f"[5] sum over Euler castles of (-1)^blocks x^(w + blocks) q^area = "
      f"sum_k (-1)^k (x^(3k-1) q^(k(3k-1)/2) + x^(3k) q^(k(3k+1)/2)), n <= {N}: {ok}")
signed_s = [sum((-1) ** h * comb(s - h - 1, h - 1) for h in range(1, s) if s - h >= 1) for s in range(2, 20)]
print(f"[5] signed Euler castles by semi-perimeter, s = 2..19: {signed_s}")
print(f"[5] = -A010892(s - 2), the coefficients of -t^2/(1 - t + t^2), s = 2..19: "
      f"{signed_s == [-x for x in A010892[:18]]}")

# [6] transposes of staircase castles
ok = True
for w in range(1, 9):
    for h in range(1, 6):
        for c in product(range(1, h + 1), repeat=w):
            if max(c) != h:
                continue
            t = rows(c)
            stair = all(a > b for a, b in zip(c, c[1:]))
            if all(a >= b for a, b in zip(c, c[1:])):
                ok &= is_euler(c) == all(a > b for a, b in zip(t, t[1:]))
            if stair:
                ok &= is_euler(rows(c)) and len(rows(c)) == h and max(rows(c)) == w
print(f"[6] transposing (reading the rows as columns) maps the staircase castles of width w and height h onto "
      f"the Euler castles of width h and height w, w <= 8, h <= 5: {ok}")
