# Valleys of castles: the block and convex-core identities, non-crossing and the bound w - 2,
# the shape lemma for valley castles, the count (h - 1)^2 C(w + 2h - 3, 2h) with its case split,
# depth split and parity split, the h + 1 and h + 2 block columns, and the k-valley tables.
# Page: wiki/pages/valley-castles.md.  A valley is a pair of columns i < j - 1 with every column
# between them lower than both; columns are 0-based here.
from itertools import product
from math import comb
from collections import Counter, defaultdict


def valleys(c):
    """(i, j, depth, span) for every valley of c."""
    w, out = len(c), []
    for i in range(w):
        top = -1                                   # tallest column strictly between i and j
        for j in range(i + 1, w):
            if j >= i + 2 and top < min(c[i], c[j]):
                out.append((i, j, min(c[i], c[j]) - top, j - i - 1))
            top = max(top, c[j])
            if top >= c[i]:
                break
    return out


def blocks(c):
    return sum(max(0, b - a) for a, b in zip((0,) + c, c))


def core(c):
    return [min(max(c[:i + 1]), max(c[i:])) for i in range(len(c))]


def unimodal(x):
    p = x.index(max(x))
    return all(x[t] <= x[t + 1] for t in range(p)) and all(x[t] >= x[t + 1] for t in range(p, len(x) - 1))


def inc(x):
    return all(x[t] <= x[t + 1] for t in range(len(x) - 1))


def dec(x):
    return all(x[t] >= x[t + 1] for t in range(len(x) - 1))


def shape_walls(c):
    """Wall pairs (i, j) meeting the conditions of the shape lemma."""
    w, out = len(c), []
    for i in range(w):
        for j in range(i + 2, w):
            mid = c[i + 1:j]
            if len(set(mid)) == 1 and mid[0] < min(c[i], c[j]) and unimodal(c[:i + 1]) and unimodal(c[j:]):
                if (c[i] >= c[j] and dec(c[j:])) or (c[i] <= c[j] and inc(c[:i + 1])):
                    out.append((i, j))
    return out


def scan(w, h):
    """Counter {(k, parity of blocks): castles of width w and height h with k valleys}.
    State: the stack of columns that can still be the left wall of a valley, as
    (height, a lower column follows it), the parity of the blocks so far, and whether h is reached."""
    states = {((), 0, False): Counter({0: 1})}
    for _ in range(w):
        new = defaultdict(Counter)
        for (stack, par, hit), poly in states.items():
            last = stack[-1][0] if stack else 0
            for x in range(1, h + 1):
                st, add = list(stack), 0
                while st and st[-1][0] < x:
                    add += st[-1][1]
                    st.pop()
                if st:
                    add += st[-1][1]
                    if st[-1][0] == x:
                        st.pop()
                if st:
                    st[-1] = (st[-1][0], 1)
                st.append((x, 0))
                key = (tuple(st), (par + max(0, x - last)) % 2, hit or x == h)
                for k, n in poly.items():
                    new[key][k + add] += n
        states = new
    out = Counter()
    for (stack, par, hit), poly in states.items():
        if hit:
            for k, n in poly.items():
                out[(k, par)] += n
    return out


def by_k(t):
    out = Counter()
    for (k, _), n in t.items():
        out[k] += n
    return out


C = lambda w, h: comb(w + 2 * h - 3, 2 * h) if w + 2 * h - 3 >= 0 else 0

# [1]-[3] and [5]-[7]: every castle with w <= 9, h <= 5, by brute force
ok = {n: True for n in (1, 2, 3, 5, 6, 7)}
for w in range(1, 10):
    for h in range(1, 6):
        valley, depth, caseA, both = Counter(), Counter(), Counter(), 0
        par, col_h1, col_h2, col_h2_split = Counter(), 0, 0, Counter()
        bf = Counter()
        for c in product(range(1, h + 1), repeat=w):
            if max(c) != h:
                continue
            V = valleys(c)
            u = core(c)
            # [1] identities
            if blocks(c) != h + sum(v[2] for v in V): ok[1] = False
            if [u[l] - c[l] for l in range(w)] != [sum(v[2] for v in V if v[0] < l < v[1]) for l in range(w)]: ok[1] = False
            if sum(u) - sum(c) != sum(v[2] * v[3] for v in V): ok[1] = False
            if any(a[0] < b[0] < a[1] < b[1] for a in V for b in V): ok[1] = False
            if len(V) > max(w - 2, 0) or (len(V) == 0) != unimodal(list(c)): ok[1] = False
            vis = sum(1 for i in range(w) for j in range(i + 1, w) if all(c[m] < min(c[i], c[j]) for m in range(i + 1, j)))
            if vis != (w - 1) + len(V): ok[1] = False
            # [3] shape lemma: one valley iff exactly one wall pair meets the conditions, and it is the valley
            S = shape_walls(c)
            if (len(V) == 1) != (len(S) == 1) or len(S) > 1 or (len(V) == 1 and S[0] != V[0][:2]): ok[3] = False
            # [7] the h + 1 and h + 2 block columns
            b = blocks(c)
            bf[(len(V), b % 2)] += 1
            if b == h + 1:
                col_h1 += 1
                if not (len(V) == 1 and V[0][2] == 1): ok[7] = False
            if b == h + 2:
                col_h2 += 1
                col_h2_split['one valley of depth 2' if len(V) == 1 else 'two valleys of depth 1'] += 1
            if len(V) == 1:
                i, j, d, _ = V[0]
                valley[(w, h)] += 1
                depth[d] += 1
                par[b % 2] += 1
                if c[i] >= c[j] and dec(c[j:]): caseA[(c[i + 1], c[j])] += 1
                inA, inB = c[i] >= c[j] and dec(c[j:]), c[i] <= c[j] and inc(c[:i + 1])
                if inA and inB: both += 1
                if (inA and c[j] == h) != (inA and inB): ok[5] = False
        n = C(w, h)
        # [5] case (A): C(w + 2h - 3, 2h) for each floor f < right wall c_j; the overlap (h - 1) of those
        if any(caseA[(f, r)] != n for f in range(1, h) for r in range(f + 1, h + 1)) or both != (h - 1) * n: ok[5] = False
        # [6] depth split and parity split
        if any(depth[d] != (2 * h - 1 - 2 * d) * n for d in range(1, h)): ok[6] = False
        ev, od = (comb(h, 2), comb(h - 1, 2)) if h % 2 else (comb(h - 1, 2), comb(h, 2))
        if (par[0], par[1]) != (ev * n, od * n): ok[6] = False
        if h >= 2 and col_h1 != (2 * h - 3) * n: ok[7] = False
        if h >= 3 and (col_h2_split['one valley of depth 2'] != (2 * h - 5) * n or
                       col_h2 != (2 * h - 5) * n + 2 * (2 * h - 5) * comb(w + 2 * h - 3, 2 * h + 1) + (2 * h + 1) * (h - 2) * comb(w + 2 * h - 3, 2 * h + 2)):
            ok[7] = False
        # [2] the scan agrees with brute force
        if bf != scan(w, h): ok[2] = False
print("[1] blocks = h + total depth; core - c = sum of depths over the valleys above each column; core area - area = sum of depth x span;"
      " no two valleys cross; at most w - 2 valleys, none iff unimodal; horizontally visible pairs = (w - 1) + valleys; all castles w <= 9, h <= 5:", ok[1])
print("[2] the stack scan agrees with brute force (valleys and block parity), w <= 9, h <= 5:", ok[2])
print("[3] shape lemma: exactly one valley iff exactly one wall pair has a flat floor below both walls, unimodal sides,"
      " and (c_i >= c_j, right side weakly decreasing) or (c_i <= c_j, left side weakly increasing); w <= 9, h <= 5:", ok[3])

# [4] the count, by the scan
ok4 = all(by_k(scan(w, h))[1] == (h - 1) ** 2 * C(w, h) for w in range(1, 17) for h in range(1, 8))
print("[4] valley castles = (h - 1)^2 C(w + 2h - 3, 2h), 1 <= w <= 16, 1 <= h <= 7:", ok4)
print("[5] case (A) gives C(w + 2h - 3, 2h) for each 1 <= f < c_j <= h, and its castles with c_j = h are the overlap, (h - 1) C(w + 2h - 3, 2h); w <= 9, h <= 5:", ok[5])
print("[6] depth d: (2h - 1 - 2d) C(w + 2h - 3, 2h); even-block C(h, 2) or C(h - 1, 2) times C(w + 2h - 3, 2h) as h is odd or even, odd-block the other; w <= 9, h <= 5:", ok[6])
ok6 = True
for w in range(1, 17):
    for h in range(1, 8):
        t, n = scan(w, h), C(w, h)
        ev, od = (comb(h, 2), comb(h - 1, 2)) if h % 2 else (comb(h - 1, 2), comb(h, 2))
        if (t[(1, 0)], t[(1, 1)]) != (ev * n, od * n) or t[(1, 0)] - t[(1, 1)] != (-1) ** (h + 1) * (h - 1) * n:
            ok6 = False
print("[6] parity split and S_valley = (-1)^(h+1) (h - 1) C(w + 2h - 3, 2h) by the scan, w <= 16, h <= 7:", ok6)
print("[7] the castles with h + 1 blocks are the valley castles of depth 1, (2h - 3) C(w + 2h - 3, 2h); those with h + 2 blocks are the valley castles of depth 2,"
      " (2h - 5) C(w + 2h - 3, 2h), and the 2-valley castles with both depths 1; w <= 9, 2 <= h <= 5:", ok[7])

# [8] k-valley castles
ok8 = all(by_k(scan(w, h))[0] == comb(w + 2 * h - 3, w - 1) for w in range(1, 17) for h in range(1, 8))
ok8 &= all(by_k(scan(w, 2))[k] == comb(w + 1, 2 * k + 2) for w in range(1, 19) for k in range(0, w))
ok8h3 = all(by_k(scan(w, 3))[2] == 12 * comb(w + 3, 8) + 2 * comb(w + 3, 7) for w in range(1, 17))
print("[8] 0 valleys: C(w + 2h - 3, w - 1), w <= 16, h <= 7; height 2, k valleys: C(w + 1, 2k + 2), w <= 18:", ok8)
print("[8] height 3, 2 valleys: 12 C(w + 3, 8) + 2 C(w + 3, 7), w <= 16:", ok8h3)
for h in (3, 4):
    for w in range(3, 9):
        t = by_k(scan(w, h))
        print("[8] h = %d, w = %d, castles by number of valleys k = 0, 1, ...:" % (h, w), [t[k] for k in range(max(t) + 1)])
