# Keystone castles: triangle castles with no overhang (each down triangle held by the two up triangles beside it), and every count on the page.
# Page: wiki/pages/keystone-castles.md.  Cell (x, r), r >= 1; up iff x = r - 1 mod 2; up (x, r) spans [x, x + 2] with apex (x + 1, r), down (x, r) has top edge [x, x + 2] at y = r.
import itertools
from collections import Counter
from math import comb


def is_up(x, r):
    return (x - (r - 1)) % 2 == 0


def keystone_castles(w):
    """Every keystone castle of width w, as a list of rows (sets of positions x); row 1 is U D U ... U."""
    out = []

    def rec(rows):
        out.append([set(r) for r in rows])
        r, row = len(rows), rows[-1]
        downs = sorted(x for x in row if not is_up(x, r))
        for k in range(1, len(downs) + 1):
            for ups in itertools.combinations(downs, k):
                uset = set(ups)
                free = [x + 1 for x in ups if x + 2 in uset]
                for m in range(1 << len(free)):
                    rec(rows + [uset | {d for j, d in enumerate(free) if m >> j & 1}])
    rec([set(range(2 * w - 1))])
    return out


def runs(s):
    s = sorted(s)
    return sum(1 for j, x in enumerate(s) if j == 0 or s[j - 1] != x - 1)


def outline(rows, w):
    """The top boundary as a word in u, d, h (h a flat step of length 2)."""
    y = [0] * (2 * w + 1)
    for r, row in enumerate(rows, start=1):
        for x in row:
            pts = {x: r - 1, x + 1: r, x + 2: r - 1} if is_up(x, r) else {x: r, x + 1: r, x + 2: r}
            for X, v in pts.items():
                y[X] = max(y[X], v)
    word, i = '', 0
    while i < 2 * w:
        step = y[i + 1] - y[i]
        if step:
            word, i = word + ('u' if step > 0 else 'd'), i + 1
        else:
            assert y[i + 2] == y[i]
            word, i = word + 'h', i + 2
    return word


def schroder(n):
    out = []

    def rec(word, lvl, length):
        if length == 2 * n:
            if lvl == 0:
                out.append(word)
            return
        if length + 2 <= 2 * n:
            rec(word + 'h', lvl, length + 2)
        rec(word + 'u', lvl + 1, length + 1)
        if lvl:
            rec(word + 'd', lvl - 1, length + 1)
    rec('', 0, 0)
    return out


def height(word):
    lvl = top = 0
    for c in word:
        lvl += {'u': 1, 'd': -1, 'h': 0}[c]
        top = max(top, lvl)
    return top


def area(word):
    """Area under a u/d/h path in unit triangles."""
    lvl, twice = 0, 0
    for c in word:
        if c == 'u':
            twice += 2 * lvl + 1
            lvl += 1
        elif c == 'd':
            lvl -= 1
            twice += 2 * lvl + 1
        else:
            twice += 4 * lvl
    return twice // 2


def schroder_stats(n):
    """Counter {(height, ups): large Schroder paths of semilength n}, by a sweep over half-steps."""
    layers = [Counter() for _ in range(2 * n + 1)]
    layers[0][(0, 0, 0)] = 1                            # (level, max, ups)
    for L in range(2 * n):
        for (l, m, u), v in layers[L].items():
            if L + 2 <= 2 * n:
                layers[L + 2][(l, m, u)] += v
            layers[L + 1][(l + 1, max(m, l + 1), u + 1)] += v
            if l:
                layers[L + 1][(l - 1, m, u)] += v
    return Counter({(m, u): v for (l, m, u), v in layers[2 * n].items() if l == 0})


def castle_stats(w):
    """Counter {(height, blocks): keystone castles of width w}: height and ups of u P d."""
    return Counter({(m + 1, u + 1): v for (m, u), v in schroder_stats(w - 1).items()})


def cells_series(N):
    """Keystone castles by cells, n = 0..N: the outlines u P d by area, swept in order of area."""
    out, st = [0] * (N + 1), Counter({(1, 1): 1})      # after the first u: (level, area in half-triangles)
    for a in range(1, 2 * N + 1):
        for l in range(1, N + 2):
            v = st.pop((l, a), 0)
            if not v:
                continue
            for key in ((l + 1, a + 2 * l + 1), (l, a + 4 * l)) + (((l - 1, a + 2 * l - 1),) if l > 1 else ()):
                if key[1] <= 2 * N:
                    st[key] += v
            if l == 1 and (a + 1) // 2 <= N:
                out[(a + 1) // 2] += v               # the final d, back to level 0
    return out


# Power series with integer coefficients, truncated at x^N.
def smul(a, b, N):
    out = [0] * (N + 1)
    for i, u in enumerate(a[:N + 1]):
        if u:
            for j, v in enumerate(b[:N + 1 - i]):
                out[i + j] += u * v
    return out


def sinv(a, N):
    """1/a, a[0] = +-1."""
    out = [0] * (N + 1)
    for n in range(N + 1):
        out[n] = ((1 if n == 0 else 0) - sum(a[j] * out[n - j] for j in range(1, min(n, len(a) - 1) + 1))) // a[0]
    return out


def mono(c, e, N):
    s = [0] * (N + 1)
    if e <= N:
        s[e] = c
    return s


def bala_large(N):
    """Bala's continued fraction (2) of the large-type note at b = q, u = d = 1: 1/(1 - q^2 - q^3/(1 - q^4 - q^5/(...)))."""
    f = [1] + [0] * N
    for j in range(N, -1, -1):
        g = [(1 if i == 0 else 0) - mono(1, 2 * j + 2, N)[i] - smul(mono(1, 2 * j + 3, N), f, N)[i] for i in range(N + 1)]
        f = sinv(g, N)
    return f


def bala_small(N):
    """Bala's continued fraction (8) of the main note at u = d = 1: 1/(1 - q/(1 - q^2 - q^3/(1 - q^4 - ...)))."""
    qf = smul(mono(1, 1, N), bala_large(N), N)
    return sinv([(1 if i == 0 else 0) - qf[i] for i in range(N + 1)], N)


def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def motzkin(n):
    st = Counter({0: 1})
    for _ in range(n):
        nxt = Counter()
        for l, v in st.items():
            nxt[l + 1] += v
            nxt[l] += v
            if l:
                nxt[l - 1] += v
        st = nxt
    return st[0]


def D_poly(k, N):
    """D_k(x) = (1 - (-x)^(k+2))/(1 + x), as a coefficient list."""
    return [(-1) ** i for i in range(k + 2)] + [0] * max(0, N - k - 1)


if __name__ == '__main__':
    W = 6
    walls = {w: keystone_castles(w) for w in range(1, W + 1)}

    # [1] The outline is u P d with P a large Schroder path of semilength w - 1; height, blocks, cells.
    ok = True
    for w, L in walls.items():
        words = [outline(c, w) for c in L]
        ok &= sorted(words) == sorted('u' + p + 'd' for p in schroder(w - 1)) and len(set(words)) == len(words)
        ok &= all(height(wd) == len(c) and wd.count('u') == sum(runs(r) for r in c) and area(wd) == sum(len(r) for r in c)
                  for wd, c in zip(words, L))
    print(f"[1] the outline of a keystone castle of width w is u P d, P running once over the large Schroder paths of semilength w - 1; the castle's height is the path's height, its blocks the up-steps, its cells the area under the path; w <= {W}: {ok}")

    # [2] Without its bottom up triangles, a keystone castle is a stack of large Schroder type on w - 1 down triangles.
    ok = True
    for w, L in walls.items():
        for c in L:
            base_ups = {x for x in c[0] if is_up(x, 1)}
            ok &= len(base_ups) == w and c[0] - base_ups == {x for x in range(2 * w - 1) if not is_up(x, 1)}
    N = 60
    big_cells = cells_series(200)
    cells = big_cells[:N + 1]
    A = bala_large(N)
    print(f"[2] the bottom row is w up triangles and the w - 1 down triangles between them, w <= {W}: {ok}; keystone castles by cells = q * (Bala's large-type fraction at b = q, u = d = 1), n <= {N}: {cells == [0] + A[:N]}")

    # [3] By width, blocks, height, height 2, and width + blocks.
    WD = 14
    ok_r = ok_b = ok_2 = True
    for w in range(1, WD + 1):
        c = castle_stats(w)
        if w <= W:
            ok_r &= Counter((len(x), sum(runs(r) for r in x)) for x in walls[w]) == c
        byb = Counter()
        for (h, b), v in c.items():
            byb[b] += v
        ok_b &= all(byb[b] == comb(w - 1 + b - 1, w - 1) * comb(w - 1, b - 1) // b for b in range(1, w + 1))
        ok_2 &= sum(v for (h, b), v in c.items() if h == 2) == (fib(2 * w - 1) - 1 if w >= 2 else 0)
    big = [sum(castle_stats(w).values()) for w in range(1, WD + 1)]
    S = 20
    bys = Counter()
    for w in range(1, S):
        for (h, b), v in castle_stats(w).items():
            if w + b <= S:
                bys[w + b] += v
    print(f"[3] the Schroder sweep agrees with brute force by (height, blocks), w <= {W}: {ok_r}; by width, w = 1..{WD}: {big}; by blocks T(w - 1, b - 1) = C(w + b - 2, w - 1) C(w - 1, b - 1)/b (A088617): {ok_b}; height 2 = F_(2w-1) - 1: {ok_2}; by w + blocks = M_(s-2), s = 2..{S}: {all(bys[s] == motzkin(s - 2) for s in range(2, S + 1))}")

    # [4] Cells: A393774(n - 1), and the triangle stacks of A224704 as rows of keystone castles.
    a393774 = [1, 0, 1, 1, 1, 2, 2, 4, 5, 7, 11, 15, 23, 32, 48, 70, 101, 149, 216, 318, 463, 677, 991]
    a224704 = [1, 1, 1, 2, 4, 7, 13, 24, 45, 84, 156, 291, 543, 1013, 1889, 3524, 6575, 12266, 22883]
    stacks = sinv([1] + [-c for c in cells[1:]], N)
    print(f"[4] keystone castles by cells, n = 1..30: {cells[1:31]}; = A393774(n - 1) (OEIS data): {cells[1:24] == a393774}; 1/(1 - K(q)) = A224704 (OEIS data): {stacks[:19] == a224704}; = Bala's fraction (8) at u = d = 1, n <= {N}: {stacks == bala_small(N)}")

    # [5] The 60-degree rows: compositions with b_1 = 1 and 2 <= b_(i+1) <= b_i + 1 + (b_i mod 2).
    ok = True
    for w, L in walls.items():
        comps = set()
        for c in L:
            cellset = {(x, r) for r, row in enumerate(c, start=1) for x in row}
            b = []
            for m in range(w):
                k = 0
                while (2 * m + k // 2 + k % 2, k // 2 + 1) in cellset:
                    k += 1
                b.append(k)
            ok &= sum(b) == len(cellset)
            comps.add(tuple(reversed(b)))
        rule = {(1,)}
        for _ in range(w - 1):
            rule = {s + (t,) for s in rule for t in range(2, s[-1] + 2 + s[-1] % 2)}
        ok &= comps == rule and len(comps) == len(L)
    print(f"[5] read along the 60-degree rows, right to left, a keystone castle of width w is a composition (b_1, ..., b_w) of its cells with b_1 = 1 and 2 <= b_(i+1) <= b_i + 1 + (b_i mod 2), each once, w <= {W}: {ok}")

    # [6] The up triangles form a brick-wall castle; the free down triangles double the count.
    ok = True
    for w, L in walls.items():
        image = Counter()
        for c in L:
            bricks = tuple(frozenset((x - (r - 1)) // 2 for x in row if is_up(x, r)) for r, row in enumerate(c, start=1))
            ok &= all(all(i in bricks[t - 1] and i + 1 in bricks[t - 1] for i in bricks[t]) for t in range(1, len(bricks)))
            image[bricks] += 1
        for bricks, v in image.items():
            free = sum(1 for t in range(1, len(bricks)) for i in bricks[t] if i + 1 in bricks[t]
                       and not (t + 1 < len(bricks) and i in bricks[t + 1]))
            ok &= v == 2 ** free
        ok &= len(image) == comb(2 * w, w) // (w + 1)
    print(f"[6] the up triangles of a keystone castle of width w, brick i of row t over bricks i and i + 1 of row t - 1, are a brick-wall castle of width w, each reached 2^f times, f the pairs of neighboring up triangles above the bottom row with no up triangle on the down triangle between them; all C_w brick-wall castles are reached; w <= {W}: {ok}")

    # [7] Parity: the signed count over all heights is 0 for w >= 2, by the involution on the first flat step or peak of P.
    sig = [sum(v * (-1) ** b for (h, b), v in castle_stats(w).items()) for w in range(1, WD + 1)]

    def toggle(p):
        for i, c in enumerate(p):
            if c == 'h':
                return p[:i] + 'ud' + p[i + 1:]
            if c == 'u' and p[i + 1] == 'd':
                return p[:i] + 'h' + p[i + 2:]
        return None
    ok = True
    for n in range(1, 9):
        for p in schroder(n):
            q = toggle(p)
            ok &= q is not None and toggle(q) == p and abs(q.count('u') - p.count('u')) == 1
    ok_c = True
    for w, L in walls.items():
        if w >= 2:
            for c in L:
                wd = outline(c, w)
                ok_c &= abs(sum(len(r) for r in c) - area('u' + toggle(wd[1:-1]) + 'd')) == 1
    print(f"[7] S_key(w) = sum of (-1)^blocks, w = 1..{WD}: {sig}; swapping the first flat step or peak of P (h <-> ud) is an involution that changes the up-steps by 1, n <= 8: {ok}; on the castle the swap adds or removes one up triangle, cells changing by 1, w <= {W}: {ok_c}")

    # [8] Signed counts at height at most h: -x D_(h-2)/D_(h-1), D_k = (1 - (-x)^(k+2))/(1 + x), periodic with period 2(h + 1).
    NW = 40
    ok = ok_p = True
    for h in range(1, 9):
        series = [0] + [sum(v * (-1) ** b for (hh, b), v in castle_stats(w).items() if hh <= h) for w in range(1, NW + 1)]
        num = [0] + [-c for c in (D_poly(h - 2, NW) if h >= 2 else [1] + [0] * NW)][:NW]
        gf = smul(num, sinv(D_poly(h - 1, NW), NW), NW)
        ok &= gf == series
        ok_p &= all(series[w] == series[w + 2 * (h + 1)] for w in range(1, NW + 1 - 2 * (h + 1)))
    print(f"[8] the signed keystone castles of height at most h have g.f. -x D_(h-2)(x)/D_(h-1)(x), D_k = (1 - (-x)^(k+2))/(1 + x), D_(-1) = 1, h <= 8, w <= {NW}: {ok}; periodic in w with period 2(h + 1): {ok_p}")

    # [9] Tables: A_key, A^e_key and S_key at fixed height.
    for name, f in (('A_key', lambda c, h: sum(v for (m, b), v in c.items() if m == h)),
                    ('A^e_key', lambda c, h: sum(v for (m, b), v in c.items() if m == h and b % 2 == 0)),
                    ('S_key', lambda c, h: sum(v * (-1) ** b for (m, b), v in c.items() if m == h))):
        for h in range(1, 7):
            print(f"[9] {name}(w, {h}), w = 1..{WD}: {[f(castle_stats(w), h) for w in range(1, WD + 1)]}")
    e2 = [sum(v for (m, b), v in castle_stats(w).items() if m == 2 and b % 2 == 0) for w in range(2, 25)]
    s2 = [sum(v * (-1) ** b for (m, b), v in castle_stats(w).items() if m == 2) for w in range(2, 25)]
    print(f"[9] A^e_key(w, 2) = (F_(2w-1) - 1 + S_key(w, 2))/2, w = 2..24: {e2 == [(fib(2 * w - 1) - 1 + s) // 2 for w, s in zip(range(2, 25), s2)]}")

    # [10] Growth by cells: the smallest positive zero of N(q) = sum (-1)^n q^(2n^2+n)/((1-q^2)...(1-q^(2n)))^2.
    def Nq(q):
        tot, prod = 0.0, 1.0
        for n in range(0, 40):
            if n:
                prod *= (1 - q ** (2 * n)) ** 2
            tot += (-1) ** n * q ** (2 * n * n + n) / prod
        return tot
    lo, hi = 0.5, 0.9
    assert Nq(lo) > 0 > Nq(hi)
    for _ in range(200):
        mid = (lo + hi) / 2
        lo, hi = (mid, hi) if Nq(mid) > 0 else (lo, mid)
    print(f"[10] smallest positive zero of N(q): y_0 = {lo:.12f}, 1/y_0 = {1 / lo:.10f}; ratios of keystone castles with n + 1 and n cells at n = 99, 149, 199: {big_cells[100] / big_cells[99]:.8f}, {big_cells[150] / big_cells[149]:.8f}, {big_cells[200] / big_cells[199]:.8f}")
