# City-building castles: castles with a ground column c_0 = 0 in front in which every column sees
# exactly c_j of the columns before it, under the visibility rule of the city-building sequence
# A400000 (an earlier top is seen when every top between is on or below the segment joining them).
# Checks: A400000's data field from the lowest-choice rule; the flat and wall steps of the
# finiteness proof; the width bound; the cut at the columns of height h against a direct search;
# the counts by height, width and block parity for h <= 5; the relation to valleys.
# Page: wiki/pages/city-building-castles.md.  OEIS data below: the data field of A400000, read 2026-10-25.
import sys
from math import factorial
from collections import Counter, defaultdict

A400000 = [0, 1, 1, 2, 1, 2, 1, 3, 1, 2, 1, 3, 1, 2, 1, 10, 1, 2, 2, 3, 1, 3, 1, 4, 1, 2, 4, 1, 2, 2, 1, 10, 1,
           2, 2, 3, 1, 3, 1, 4, 1, 2, 4, 1, 2, 2, 1, 11, 1, 2, 2, 3, 2, 3, 1, 4, 1, 2, 4, 1, 2, 2, 1, 10, 1, 2,
           2, 3, 1, 3, 1, 4, 1, 2, 4, 1, 2, 2, 1, 11, 1, 2, 2, 3]


def seen(prefix, k):
    """How many of the columns in prefix (positions 0..j-1) the top (j, k) sees."""
    j, c, dx0, dy0 = len(prefix), 0, 0, 0
    for dx in range(1, j + 1):
        dy = prefix[j - dx] - k
        if dx0 * dy >= dx * dy0:          # slope at least the steepest one so far: on or below the segment
            c += 1
            dx0, dy0 = dx, dy
    return c


def sees(prefix, i, k):
    """Does the top (len(prefix), k) see the column i of prefix?"""
    j = len(prefix)
    return all((prefix[m] - prefix[i]) * (j - i) <= (k - prefix[i]) * (m - i) for m in range(i + 1, j))


def blocks(sky):
    return sum(max(0, b - a) for a, b in zip([0] + list(sky), sky))


def valleys(c):
    out = []
    for i in range(len(c)):
        for j in range(i + 2, len(c)):
            if max(c[i + 1:j]) < min(c[i], c[j]):
                out.append((i, j))
    return out


def castles(hmax, wmax=10 ** 9):
    """Every city-building castle of height <= hmax and width <= wmax, as skylines."""
    stack = [[0]]
    while stack:
        pre = stack.pop()
        if len(pre) > 1:
            yield pre[1:]
        if len(pre) - 1 == wmax:
            continue
        for k in range(1, min(hmax, len(pre)) + 1):
            if seen(pre, k) == k:
                stack.append(pre + [k])


# [1] A400000 from the lowest-choice rule; its prefixes are city-building castles
a = []
while len(a) < len(A400000):
    k = 0
    while seen(a, k) != k:
        k += 1
    a.append(k)
ok1 = a == A400000 and all(x >= 1 for x in a[1:]) and all(seen(a[:j], a[j]) == a[j] for j in range(1, len(a)))
dead = all(seen(a[:15], k) != k for k in range(0, 10))
print("[1] the lowest-choice rule gives A400000's data field (%d terms), every term after the first is >= 1, "
      "and every a(2..w+1) is a city-building castle: %s; C_14 = %s has no legal next column of height 0..9: %s"
      % (len(A400000), ok1, a[1:15], dead))

# [2] counts by width over all heights
byw = Counter(len(s) for s in castles(14, 14))
print("[2] city-building castles of width w, all heights, w = 1..14:", [byw[w] for w in range(1, 15)])

# [3] and [6], one pass over every castle of height <= 4 (also the direct counts for [4])
def left_partners(c):
    """For each column, how many earlier columns it sees horizontally (every column between lower
    than both): its left neighbor plus the left walls of the valleys it closes."""
    stack, out = [], []
    for x in c:
        n = 0
        while stack and stack[-1] < x:
            stack.pop(); n += 1
        if stack:
            n += 1
            if stack[-1] == x:
                stack.pop()
        stack.append(x); out.append(n)
    return out


ok3 = ok6 = True
direct = Counter()
for s in castles(4):
    h = max(s)
    direct[(len(s), h, blocks(s) % 2)] += 1
    if s.count(h) > h + 1: ok3 = False
    for m in range(1, h):                          # runs of heights <= m right after a column taller than m
        n = None
        for x in s:
            if x > m: n = 0
            elif n is not None and x == m:
                n += 1
                if n > m: ok3 = False
    if any(x < p for x, p in zip(s, left_partners(s))): ok6 = False
print("[3] at most h + 1 columns of height h, and at most m columns of height m in a run of heights <= m "
      "that follows a taller column; every castle of height <= 4:", ok3)

# [4] the cut at the columns of height h
def runs(m, start, H):
    """Runs of heights <= m after `start` ([0] the ground, [H] a column of height H) in which every
    column sees exactly its height; yields (length, columns seen from height H at the end, not counting
    a wall, parity of the rise sum up to and including a column of height H placed after the run)."""
    stack = [list(start)]
    while stack:
        pre = stack.pop()
        run = pre[len(start):]
        vis = seen(pre, H) - (1 if start[0] > 0 else 0)
        rise = blocks(run) if start[0] == 0 else blocks(run) - (run[0] if run else 0)
        last = run[-1] if run else start[0]
        yield len(run), vis, (rise + H - last) % 2, rise % 2
        for k in range(1, m + 1):
            if seen(pre, k) == k:
                stack.append(pre + [k])


def mul(P, Q):
    R = Counter()
    for (w1, p1), x in P.items():
        for (w2, p2), y in Q.items():
            R[(w1 + w2, (p1 + p2) % 2)] += x * y
    return R


def cut(h):
    """Counter {(width, block parity): city-building castles of height h} from the cut."""
    g, wall, fin = defaultdict(Counter), defaultdict(Counter), Counter()
    for L, vis, par, _ in runs(h - 1, [0], h):
        g[vis][(L, par)] += 1
    for L, vis, par, rpar in runs(h - 1, [h], h):
        wall[vis][(L, par)] += 1
        fin[(L, rpar)] += 1
    one = Counter({(1, 0): 1})
    total, chain = Counter(), mul(g[h], one)          # the first column of height h sees exactly h
    for t in range(1, h + 2):
        if t > 1:                                     # the t-th sees t - 1 earlier ones and h - t + 1 of its run
            chain = mul(mul(chain, wall[h - t + 1]), one)
        if not chain:
            break
        total.update(mul(chain, fin))
    return total


direct5 = Counter((len(s), blocks(s) % 2) for s in castles(5, 22) if max(s) == 5)
T = {h: cut(h) for h in range(1, 6)}
ok4 = all(T[h][(w, p)] == direct[(w, h, p)] for h in range(1, 5) for w in range(1, 61) for p in (0, 1))
ok4 &= all(T[5][(w, p)] == direct5[(w, p)] for w in range(1, 23) for p in (0, 1))
print("[4] the cut agrees with the direct search, by width and block parity: every width for h <= 4, w <= 22 for h = 5:", ok4)
nfirst = sum(1 for _ in runs(4, [0], 5)); nwall = sum(1 for _ in runs(4, [5], 5))
print("[4] at h = 5 the cut uses %d first runs (the city-building castles of height <= 4 and the empty run) and %d walled runs" % (nfirst, nwall))
for h in range(1, 6):
    tot = sum(T[h].values()); ev = sum(n for (w, p), n in T[h].items() if p == 0)
    W = max(w for w, p in T[h])
    print("[4] h = %d: %d castles, %d even-block, %d odd-block, widest %d, bound 2! + ... + (h+1)! = %d"
          % (h, tot, ev, tot - ev, W, sum(factorial(k + 1) for k in range(1, h + 1))))
for h in range(2, 6):
    W = max(w for w, p in T[h])
    print("[4] h = %d by width w = 1..%d, (even, odd):" % (h, W), [(T[h][(w, 0)], T[h][(w, 1)]) for w in range(1, W + 1)])

# [5] the wall is not always seen: the widest castles of height 3 end in 3, 1, 2, 2, 1
widest3 = [s for s in castles(3) if max(s) == 3 and len(s) == 18]
ok5 = all(s[-5:] == [3, 1, 2, 2, 1] and not sees([0] + s[:-1], len(s) - 4, 1) for s in widest3)
print("[5] the %d widest castles of height 3 end in 3, 1, 2, 2, 1, and the last column does not see the 3: %s" % (len(widest3), ok5))

# [6] valleys: column j sees its left neighbor and the left wall of every valley it closes
ok6v = all(left_partners(c) == [(1 if j else 0) + sum(1 for (i, jj) in valleys(c) if jj == j) for j in range(len(c))]
           for c in castles(3))
print("[6] c_j >= 1 + (valleys with right wall j), so area >= w + valleys, every castle of height <= 4: %s "
      "(the linear-time partner count matches the valley list on every castle of height <= 3: %s)" % (ok6, ok6v))

# [7] the examples on the page
def city(c):
    pre = [0] + list(c)
    return all(seen(pre[:j], pre[j]) == pre[j] for j in range(1, len(pre)))
w7 = [s for s in castles(2) if max(s) == 2 and len(s) == 7]
ok7 = city((1, 2)) and city((1, 1, 2, 1, 2, 2, 1)) and not city((1, 1, 1)) and w7 == [[1, 1, 2, 1, 2, 2, 1]]
print("[7] (1, 2) and (1, 1, 2, 1, 2, 2, 1) are city-building, (1, 1, 1) is not, and (1, 1, 2, 1, 2, 2, 1) is the only one of height 2 and width 7:", ok7)
