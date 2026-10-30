# Brick-wall castles (each brick on both bricks below), their shear onto the 1-histograms, and every count on the page.
# Page: wiki/pages/brick-wall-castles.md.  Rows are 0-based from the bottom; brick i of row t sits on bricks i, i + 1 of row t - 1.
from math import comb
from functools import lru_cache
from collections import Counter, defaultdict


def brick_walls(w):
    """Every brick-wall castle of width w, as a tuple of rows, each row a frozenset of brick indices."""
    out = []

    def rec(rows):
        out.append(tuple(rows))
        top, n = rows[-1], w - len(rows)
        slots = [i for i in range(n) if i in top and i + 1 in top]
        for mask in range(1, 1 << len(slots)):
            rec(rows + [frozenset(s for j, s in enumerate(slots) if mask >> j & 1)])
    rec([frozenset(range(w))])
    return out


def runs(cells):
    s = sorted(cells)
    return sum(1 for j, x in enumerate(s) if j == 0 or s[j - 1] != x - 1)


def wall_stats(rows):
    return len(rows), sum(runs(r) for r in rows), sum(len(r) for r in rows)


def shear(rows, w):
    """Slant heights: column k of the sheared castle holds brick k - t of row t."""
    s = [0] * w
    for t, r in enumerate(rows):
        for i in r:
            s[i + t] += 1
    return tuple(s)


def blocks(c):
    return sum(max(0, b - a) for a, b in zip((0,) + c, c))


def histograms(w):
    """The 1-histograms of width w: s_1 = 1, s_{k+1} <= s_k + 1."""
    out = [(1,)]
    for _ in range(w - 1):
        out = [s + (b,) for s in out for b in range(1, s[-1] + 2)]
    return out


@lru_cache(maxsize=None)
def hist_dp(w):
    """Counter {(height, blocks): 1-histograms of width w}, by a column sweep."""
    st = Counter({(1, 1, 1): 1})                       # (last, max, blocks)
    for _ in range(w - 1):
        nxt = Counter()
        for (a, m, b), v in st.items():
            for c in range(1, a + 2):
                nxt[(c, max(m, c), b + max(0, c - a))] += v
        st = nxt
    out = Counter()
    for (a, m, b), v in st.items():
        out[(m, b)] += v
    return out


def hist_by_cells(N):
    """Counter {(cells, width): 1-histograms} for cells <= N, by a column sweep."""
    out, st = Counter(), Counter({(1, 1): 1})          # (last, cells)
    for w in range(1, N + 1):
        for (a, n), v in st.items():
            out[(n, w)] += v
        nxt = Counter()
        for (a, n), v in st.items():
            for c in range(1, a + 2):
                if n + c <= N:
                    nxt[(c, n + c)] += v
        st = nxt
    return out


def dyck_by_height(n):
    st = Counter({(0, 0): 1})                          # (level, max)
    for _ in range(2 * n):
        nxt = Counter()
        for (l, m), v in st.items():
            nxt[(l + 1, max(m, l + 1))] += v
            if l:
                nxt[(l - 1, m)] += v
        st = nxt
    return Counter({m: v for (l, m), v in st.items() if l == 0})


def dyck_paths(n):
    out = ['']
    for _ in range(2 * n):
        out = [d + c for d in out for c in 'UD'
               if (c == 'U' and d.count('U') < n) or (c == 'D' and d.count('U') > d.count('D'))]
    return out


def up_levels(d):
    """The level reached by each up-step of a Dyck path."""
    level, out = 0, []
    for c in d:
        level += 1 if c == 'U' else -1
        if c == 'U':
            out.append(level)
    return tuple(out)


def catalan(n):
    return comb(2 * n, n) // (n + 1)


def narayana(n, k):
    return comb(n, k) * comb(n, k - 1) // n


def peakless_motzkin(n):
    """Motzkin paths of length n with no UD factor (A004148)."""
    st = Counter({(0, ''): 1})
    for _ in range(n):
        nxt = Counter()
        for (l, last), v in st.items():
            nxt[(l + 1, 'U')] += v
            nxt[(l, 'H')] += v
            if l and last != 'U':
                nxt[(l - 1, 'D')] += v
        st = nxt
    return sum(v for (l, _), v in st.items() if l == 0)


# Power series in x (and y) as dicts {(n, k): coefficient}, truncated at x^N.
def smul(a, b, N):
    out = defaultdict(int)
    for (n1, k1), u in a.items():
        for (n2, k2), v in b.items():
            if n1 + n2 <= N:
                out[(n1 + n2, k1 + k2)] += u * v
    return dict(out)


def sinv_one_minus(g, N):
    """1/(1 - g) for g with no constant term."""
    out, power = {(0, 0): 1}, {(0, 0): 1}
    for _ in range(N):
        power = smul(power, g, N)
        if not power:
            break
        for key, v in power.items():
            out[key] = out.get(key, 0) + v
    return out


def odlyzko_wilf(N):
    """F(x, y) = 1/(1 - xy/(1 - x^2 y/(1 - x^3 y/ ...))), x marks coins, y the bottom row."""
    f = {(0, 0): 1}
    for j in range(N, 0, -1):
        f = sinv_one_minus(smul({(j, 1): 1}, f, N), N)
    return f


# Univariate q-series as integer lists of length N + 1.
def qmul(a, b, N):
    out = [0] * (N + 1)
    for i, u in enumerate(a):
        if u:
            for j, v in enumerate(b[:N + 1 - i]):
                out[i + j] += u * v
    return out


def qdiv(a, b, N):
    """a/b, b[0] = 1."""
    out = [0] * (N + 1)
    for n in range(N + 1):
        out[n] = a[n] - sum(b[j] * out[n - j] for j in range(1, n + 1))
    return out


def inv_qpoch(k, N):
    """1/((1 - q)(1 - q^2)...(1 - q^k))."""
    out = [1] + [0] * N
    for j in range(1, k + 1):
        out = [sum(out[n - j * m] for m in range(n // j + 1)) for n in range(N + 1)]
    return out


def pp_quotient(p, N):
    """Paule and Prodinger's displayed quotient: sum (-1)^k q^{p C(k+1,2)}/(q)_k over sum (-1)^k q^{k + p C(k,2)}/(q)_k."""
    E, D = [0] * (N + 1), [0] * (N + 1)
    for k in range(N + 1):
        for target, e in ((E, p * k * (k + 1) // 2), (D, k + p * k * (k - 1) // 2)):
            if e <= N:
                ser = inv_qpoch(k, N - e)
                for n, v in enumerate(ser):
                    target[e + n] += (-1) ** k * v
    return qdiv(E, D, N)


def histograms_by_area(r, N):
    """r-histograms by area, n = 1..N: first column 1..r, each column at most r above the one before."""
    cnt = [0] * (N + 1)

    def rec(last, area):
        cnt[area] += 1
        for b in range(1, last + r + 1):
            if area + b <= N:
                rec(b, area + b)
    for a in range(1, r + 1):
        if a <= N:
            rec(a, a)
    return cnt


def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


if __name__ == '__main__':
    W = 10
    walls = {w: brick_walls(w) for w in range(1, W + 1)}

    # [1] The shear: a bijection onto the 1-histograms that keeps rows, height, blocks and cells.
    ok = True
    for w, L in walls.items():
        image = {}
        for rows in L:
            s = shear(rows, w)
            h, b, n = wall_stats(rows)
            same_rows = all({i + t for i in r} == {k for k in range(w) if s[k] >= t + 1} for t, r in enumerate(rows))
            ok &= same_rows and (max(s), blocks(s), sum(s)) == (h, b, n) and s not in image
            image[s] = rows
        ok &= set(image) == set(histograms(w))
        mirror = {s[::-1] for s in image}
        ok &= all(c[-1] == 1 and all(c[i + 1] >= c[i] - 1 for i in range(w - 1)) for c in mirror)
    print(f"[1] the shear is a bijection from the brick-wall castles of width w onto the 1-histograms of width w, row t of the wall becoming row t of the histogram shifted t places, so height, blocks and cells agree; the mirror images drop by at most 1 and end at height 1; w <= {W}: {ok}")

    # [2] Counts by width, height and blocks.
    WD = 16
    ok_w = ok_h = ok_b = True
    for w in range(1, WD + 1):
        d = hist_dp(w)
        if w <= W:
            ok_w &= Counter(wall_stats(r)[:2] for r in walls[w]) == d
        byh, byb = Counter(), Counter()
        for (h, b), v in d.items():
            byh[h] += v
            byb[b] += v
        ok_h &= byh == dyck_by_height(w)
        ok_b &= all(byb[k] == narayana(w, k) for k in range(1, w + 1)) and sum(byb.values()) == catalan(w)
    print(f"[2] the column sweep agrees with brute force on the walls by (height, blocks), w <= {W}: {ok_w}; by width C_w and by blocks N(w, k), w <= {WD}: {ok_b}; by height the Dyck paths of semilength w and height h (A080936), w <= {WD}: {ok_h}")

    # [3] Even blocks: A071688 and the closed form.
    a071688 = [0, 1, 3, 7, 20, 66, 217, 715, 2424, 8398, 29414, 104006, 371384, 1337220, 4847637, 17678835]
    even = [sum(v for (h, b), v in hist_dp(w).items() if b % 2 == 0) for w in range(1, WD + 1)]

    def closed(w):
        return catalan(w) // 2 if w % 2 == 0 else (catalan(w) + (-1) ** ((w + 1) // 2) * catalan((w - 1) // 2)) // 2
    print(f"[3] even-block brick-wall castles, w = 1..{WD}: {even}; = A071688(w) (OEIS data, 2026-10-29): {even == a071688}; = C_w/2 (w even), (C_w + (-1)^((w+1)/2) C_((w-1)/2))/2 (w odd): {even == [closed(w) for w in range(1, WD + 1)]}")

    # [4] Semi-perimeter s = w + blocks: A004148(s - 1).
    S = 16
    by_s = Counter()
    for w in range(1, S):
        for (h, b), v in hist_dp(w).items():
            if w + b <= S:
                by_s[w + b] += v
    print(f"[4] brick-wall castles by w + blocks, s = 2..{S}: {[by_s[s] for s in range(2, S + 1)]}; = A004148(s - 1), the peakless Motzkin paths of length s - 1: {all(by_s[s] == peakless_motzkin(s - 1) for s in range(2, S + 1))}")

    # [5] Cells: the fountains of coins, A005169, and Odlyzko and Wilf's continued fraction in coins and bottom row.
    N = 18
    by_nw = hist_by_cells(N)
    for w in range(1, W + 1):
        assert Counter((wall_stats(r)[2], w) for r in walls[w] if wall_stats(r)[2] <= N) == Counter({k: v for k, v in by_nw.items() if k[1] == w})
    a005169 = [1, 1, 1, 2, 3, 5, 9, 15, 26, 45, 78, 135, 234, 406, 704, 1222, 2120, 3679, 6385]
    by_n = [1] + [sum(v for (n, w), v in by_nw.items() if n == m) for m in range(1, N + 1)]
    cf = odlyzko_wilf(N)
    print(f"[5] brick-wall castles by cells n = 0..{N} (the empty wall at n = 0): {by_n}; = A005169 (OEIS data): {by_n == a005169}; by (cells, width) = [x^n y^w] of 1/(1 - xy/(1 - x^2 y/(1 - x^3 y/ ...))), n <= {N}: {all(cf.get(k, 0) == by_nw.get(k, 0) for k in set(cf) | set(by_nw) if k != (0, 0))}")

    # [6] Paule and Prodinger's displayed quotient at p counts the (p - 1)-histograms by area.
    NP = 16
    res = []
    for p in (2, 3, 4):
        quo, hist = pp_quotient(p, NP), histograms_by_area(p - 1, NP)
        res.append(quo[1:] == hist[1:] and quo[0] == 1)
    print(f"[6] sum (-1)^k q^(p C(k+1,2))/(q)_k / sum (-1)^k q^(k + p C(k,2))/(q)_k = 1 + the (p - 1)-histograms by area, p = 2, 3, 4, area <= {NP}: {res}; at p = 2, {pp_quotient(2, 12)}; at p = 1 the quotient is 1: {pp_quotient(1, 12) == [1] + [0] * 12}")

    # [7] Block fountains (one block per row) = convex 1-histograms = F_{2w-1}.
    WB = 14
    bf = [sum(1 for s in histograms(w) if blocks(s) == max(s)) for w in range(1, WB + 1)]
    bf_walls = [sum(1 for r in walls[w] if all(runs(x) == 1 for x in r)) for w in range(1, W + 1)]
    gf = qdiv([1, -2] + [0] * (WB - 1), [1, -3, 1] + [0] * (WB - 2), WB)
    print(f"[7] block fountains of width w = 1..{WB}: {bf}; = the walls with one block per row, w <= {W}: {bf[:W] == bf_walls}; = F_(2w-1): {bf == [fib(2 * w - 1) for w in range(1, WB + 1)]}; = [y^w] (1 - 2y)/(1 - 3y + y^2): {bf == gf[1:]}; = sum_l C(w + l - 1, w - l - 1): {bf == [sum(comb(w + l - 1, w - l - 1) for l in range(w)) for w in range(1, WB + 1)]}")

    # [8] Thomas and May's table: fountains of width w with s coins on the rightmost slant.
    table = {w: Counter(s[-1] for s in histograms(w)) for w in range(1, 9)}
    tm = {1: [1, 0, 0, 0, 0, 0], 2: [1, 1, 0, 0, 0, 0], 3: [2, 2, 1, 0, 0, 0], 4: [5, 5, 3, 1, 0, 0], 5: [14, 14, 9, 4, 1, 0], 6: [42, 42, 28, 14, 5, 1]}
    print(f"[8] f_(w,s) = 1-histograms of width w with last column s agrees with Thomas and May's table, w <= 6: {all([table[w][s] for s in range(1, 7)] == tm[w] for w in tm)}; f_(w,s) = (s/w) C(2w - s - 1, w - s), w <= 8: {all(table[w][s] * w == s * comb(2 * w - s - 1, w - s) for w in table for s in range(1, w + 1))}")

    # [9] Dyck paths: the levels after the up-steps form a 1-histogram; height = max, blocks = w + 1 - peaks.
    WY = 12
    ok = True
    for w in range(1, WY + 1):
        L = dyck_paths(w)
        image = {up_levels(d): d for d in L}
        ok &= len(image) == len(L) == catalan(w) and set(image) == set(histograms(w))
        for t, d in image.items():
            ok &= max(t) == max(up_levels(d)) and blocks(t) == w + 1 - d.count('UD')
    print(f"[9] s_k = the level after the k-th up-step is a bijection from the Dyck paths of semilength w onto the 1-histograms of width w, with height = path height and blocks = w + 1 - peaks, w <= {WY}: {ok}")

    # [10] The signed count over all heights.
    sig = [sum(v * (-1) ** b for (h, b), v in hist_dp(w).items()) for w in range(1, WD + 1)]
    print(f"[10] S_brick(w) = sum of (-1)^blocks, w = 1..{WD}: {sig}; = 0 (w even), (-1)^((w+1)/2) C_((w-1)/2) (w odd): {sig == [0 if w % 2 == 0 else (-1) ** ((w + 1) // 2) * catalan((w - 1) // 2) for w in range(1, WD + 1)]}")

    # [11] Fixed height: A_brick(w, h), A^e_brick(w, h) and S_brick(w, h).
    WH, H = 14, 6
    for name, f in (('A_brick', lambda d, h: sum(v for (m, b), v in d.items() if m == h)),
                    ('A^e_brick', lambda d, h: sum(v for (m, b), v in d.items() if m == h and b % 2 == 0)),
                    ('S_brick', lambda d, h: sum(v * (-1) ** b for (m, b), v in d.items() if m == h))):
        for h in range(1, H + 1):
            print(f"[11] {name}(w, {h}), w = 1..{WH}: {[f(hist_dp(w), h) for w in range(1, WH + 1)]}")
    W2 = 24
    a2 = [sum(v for (m, b), v in hist_dp(w).items() if m == 2) for w in range(2, W2 + 1)]
    e2 = [sum(v for (m, b), v in hist_dp(w).items() if m == 2 and b % 2 == 0) for w in range(2, W2 + 1)]
    s2 = [sum(v * (-1) ** b for (m, b), v in hist_dp(w).items() if m == 2) for w in range(2, W2 + 1)]
    a077860 = qdiv([1] + [0] * W2, qmul([1, -2, 2] + [0] * (W2 - 2), [1, -1] + [0] * (W2 - 1), W2), W2)
    print(f"[11] height 2, w = 2..{W2}: A_brick(w, 2) = 2^(w-1) - 1: {a2 == [2 ** (w - 1) - 1 for w in range(2, W2 + 1)]}; A^e_brick(w, 2) = sum_k C(w, 4k + 2) (A038505(w)): {e2 == [sum(comb(w, 4 * k + 2) for k in range(w)) for w in range(2, W2 + 1)]}; S_brick(w, 2) = [x^(w-2)] 1/((1 - 2x + 2x^2)(1 - x)) (A077860(w - 2)): {s2 == a077860[:W2 - 1]}")
