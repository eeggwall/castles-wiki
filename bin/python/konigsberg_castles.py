# Königsberg castles: the castle graph with one ground vertex joined to every bottom cell.
# The parity of each degree from the neighboring column heights; the castles whose every degree
# is even are the double staircases (1, ..., k, k, ..., 1); the castles with exactly two odd
# vertices (one open stroke) are finitely many at each height, h^2 + 3h - 2 of them at odd widths.
# Page: wiki/pages/konigsberg-castles.md.  Columns are 1-based, c_0 = c_{w+1} = 0 is the ground.
from itertools import product
from collections import Counter, defaultdict
from fractions import Fraction


def blocks(c):
    return sum(max(0, b - a) for a, b in zip((0,) + c, c))


def odd_vertices(c):
    """Odd-degree vertices of the castle graph with its ground, from an explicit adjacency list."""
    cells = {(i, r) for i in range(1, len(c) + 1) for r in range(1, c[i - 1] + 1)}
    deg = Counter()
    for (i, r) in cells:
        for (j, s) in ((i + 1, r), (i, r + 1)):
            if (j, s) in cells:
                deg[(i, r)] += 1
                deg[(j, s)] += 1
        if r == 1:
            deg[(i, r)] += 1
            deg['ground'] += 1
    return sorted((v for v in deg if deg[v] % 2), key=str)


def defect(a, x, b):
    """Odd cells of a column of height x between columns of heights a and b."""
    return abs(min(a, x - 1) - min(b, x - 1)) + (1 if (a >= x) == (b >= x) else 0)


def odd_count(c):
    e = (0,) + c + (0,)
    return sum(defect(e[i - 1], e[i], e[i + 1]) for i in range(1, len(c) + 1)) + len(c) % 2


def dp_counts(w, H, target):
    """Skylines in {1..H}^w with exactly `target` odd vertices, by parity of blocks: {0: even, 1: odd}."""
    st = defaultdict(int)                          # (previous height, current height, odd so far, blocks mod 2)
    for x in range(1, H + 1):
        st[(0, x, w % 2, x % 2)] += 1
    for _ in range(w - 1):
        ns = defaultdict(int)
        for (a, x, o, p), n in st.items():
            for b in range(1, H + 1):
                oo = o + defect(a, x, b)
                if oo <= target:
                    ns[(x, b, oo, (p + max(0, b - x)) % 2)] += n
        st = ns
    out = Counter()
    for (a, x, o, p), n in st.items():
        if o + defect(a, x, 0) == target:
            out[p] += n
    return out


def cell_counts(w, h, target):
    """Castles of width w and height h with exactly `target` odd vertices, by block parity."""
    hi, lo = dp_counts(w, h, target), (dp_counts(w, h - 1, target) if h > 1 else Counter())
    return Counter({p: hi[p] - lo[p] for p in (0, 1)})


def odd_width_families(h):
    """The open-stroke castles of odd width and height h, family by family (the theorem on the page)."""
    fam = defaultdict(list)
    up, down = lambda p, q: list(range(p, q + 1)), lambda p, q: list(range(p, q - 1, -1))
    fam['dip, two ramps'].append(up(1, h) + [h] + down(h, 1))
    for x in range(1, h):
        fam['dip, ramp and hill'].append(up(1, x) + [x] + up(x + 1, h) + down(h, 1))
        fam['dip, ramp and hill'].append(up(1, h) + down(h, x + 1) + [x] + down(x, 1))
    for p in range(1, h + 1):
        for q in range(1, h + 1):
            if max(p, q) != h:
                continue
            for x in range(1, min(p, q)):
                fam['dip, two hills'].append(up(1, p) + down(p, x + 1) + [x] + up(x + 1, q) + down(q, 1))
    for p in range(0, h):
        fam['spike'].append(up(1, p) + [h] + down(p, 1))
    if h >= 2:
        s = up(1, h - 2) + [h] + down(h, 1)
        fam['step of 2'] += [s, s[::-1]]
    for p in range(0, h - 2):
        s = up(1, p) + [p + 2] + up(p + 3, h) + down(h, 1)
        fam['step of 2'] += [s, s[::-1]]
    return {k: [tuple(c) for c in v] for k, v in fam.items()}


def gen(h, target=2):
    """Every castle of height h with exactly `target` odd vertices, by depth-first search."""
    out = []

    def rec(c, o):
        if c:
            a = c[-2] if len(c) >= 2 else 0
            if o + defect(a, c[-1], 0) + len(c) % 2 == target and max(c) == h:
                out.append(c)
        if len(c) >= 6 * h + 2:
            return
        for y in range(1, h + 1):
            oo = o + (defect(c[-2] if len(c) >= 2 else 0, c[-1], y) if c else 0)
            if oo <= target:
                rec(c + (y,), oo)
    rec((), 0)
    return out


def fit(ys, deg):
    """Polynomial of degree deg through (1, ys[0]), (2, ys[1]), ..., checked on every point."""
    n = deg + 1
    A = [[Fraction(x) ** k for k in range(n)] for x in range(1, n + 1)]
    b = [Fraction(y) for y in ys[:n]]
    for i in range(n):
        for r in range(n):
            if r != i and A[r][i]:
                f = A[r][i] / A[i][i]
                A[r] = [u - f * v for u, v in zip(A[r], A[i])]
                b[r] -= f * b[i]
    co = [b[i] / A[i][i] for i in range(n)]
    ok = all(sum(co[k] * x ** k for k in range(n)) == y for x, y in zip(range(1, len(ys) + 1), ys))
    return co, ok


# [1] the parity of each degree
ok = True
for w in range(1, 8):
    for h in range(1, 6):
        for c in product(range(1, h + 1), repeat=w):
            if max(c) == h:
                ok &= len(odd_vertices(c)) == odd_count(c)
print(f"[1] odd vertices of the castle graph with its ground = sum over columns of "
      f"|min(a, x-1) - min(b, x-1)| + [(a >= x) = (b >= x)], plus 1 for odd w; all castles w <= 7, h <= 5: {ok}")
ex = (1, 2, 2, 1)
print(f"[1] example {ex}: odd vertices {odd_vertices(ex)}")
ex = (1, 1, 1, 1)
print(f"[1] example {ex}: odd vertices {odd_vertices(ex)}")

# [2] the Königsberg castles
ok = True
for w in range(1, 9):
    for h in range(1, 6):
        found = [c for c in product(range(1, h + 1), repeat=w) if max(c) == h and not odd_vertices(c)]
        want = [tuple(range(1, h + 1)) + tuple(range(h, 0, -1))] if w == 2 * h else []
        ok &= found == want
for w in range(1, 31):
    for h in range(1, 16):
        n = sum(cell_counts(w, h, 0).values())
        ok &= n == (1 if w == 2 * h else 0)
print(f"[2] every degree even exactly for (1, ..., k, k, ..., 1): brute force w <= 8, h <= 5, "
      f"and the column scan w <= 30, h <= 15: {ok}")

# [3] open strokes: brute force against the column scan
ok = True
for w in range(1, 9):
    for h in range(1, 6):
        if h ** w > 400000:
            continue
        cnt = Counter()
        for c in product(range(1, h + 1), repeat=w):
            if max(c) == h and len(odd_vertices(c)) == 2:
                cnt[blocks(c) % 2] += 1
        ok &= cnt == +cell_counts(w, h, 2)
print(f"[3] castles with exactly two odd vertices, by block parity: brute force = column scan, "
      f"w <= 8, h <= 5, h^w <= 400000: {ok}")

# [4] the open-stroke castles of each height
H = 12
tot, odd_w, even_w, even_b, maxw, rows = [], [], [], [], [], {}
for h in range(1, H + 1):
    row = [cell_counts(w, h, 2) for w in range(1, 6 * h + 4)]
    rows[h] = [sum(r.values()) for r in row]
    tot.append(sum(rows[h]))
    odd_w.append(sum(rows[h][0::2]))
    even_w.append(sum(rows[h][1::2]))
    even_b.append(sum(r[0] for r in row))
    maxw.append(max(w for w in range(1, 6 * h + 4) if rows[h][w - 1]))
print(f"[4] h = 1..{H}: open-stroke castles {tot}")
print(f"[4] odd widths {odd_w}; even widths {even_w}")
print(f"[4] even-block {even_b}; odd-block {[t - e for t, e in zip(tot, even_b)]}")
print(f"[4] widest {maxw} = 6h - 2: {maxw == [6 * h - 2 for h in range(1, H + 1)]}")
for name, ys in (('total', tot), ('odd widths', odd_w), ('even widths', even_w)):
    co, good = fit(ys, 4)
    print(f"[4] {name}: polynomial coefficients of h^0..h^4 {[str(x) for x in co]}, fits h <= {H}: {good}")
ok = all(rows[h][2 * m - 1] == m * (m + 1) for h in range(1, H + 1) for m in range(1, h - 1))
ok &= all(rows[h][2 * m] == 1 for h in range(1, H + 1) for m in range(0, h - 1))
ok &= all(rows[h][2 * h - 3] == 3 * (h - 1) ** 2 for h in range(2, H + 1))
ok &= all(rows[h][2 * h - 1] == (5 * h - 4) * (h - 1) for h in range(1, H + 1))
print(f"[4] width 2m <= 2h - 4: m(m + 1); odd width <= 2h - 3: 1; width 2h - 2: 3(h - 1)^2; "
      f"width 2h: (5h - 4)(h - 1); h <= {H}: {ok}")
for h in (2, 3):
    print(f"[4] h = {h}, by width w = 1..{6 * h - 2}: {rows[h][:6 * h - 2]}")
for h in range(1, 8):
    wide = [c for c in gen(h) if len(c) == 6 * h - 2]
    k = tuple(range(1, h + 1)) + tuple(range(h, 1, -1))
    print(f"[4] h = {h}: the only open-stroke castle of width 6h - 2 is three double staircases "
          f"sharing their end columns: {wide == [k + k + k + (1,)]}")

# [5] the odd-width theorem, family by family
ok = True
for h in range(1, 8):
    fam = odd_width_families(h)
    allc = [c for v in fam.values() for c in v]
    found = sorted(c for c in gen(h) if len(c) % 2)
    ok &= sorted(allc) == found and len(set(allc)) == len(allc) == h * h + 3 * h - 2
ok &= all(odd_w[h - 1] == h * h + 3 * h - 2 for h in range(1, H + 1))
print(f"[5] the odd-width open-stroke castles are the five families, h^2 + 3h - 2 in all: "
      f"as sets for h <= 7, as counts for h <= {H}: {ok}")
fam = odd_width_families(4)
print(f"[5] h = 4: family sizes {{{', '.join(f'{k}: {len(v)}' for k, v in fam.items())}}}")
ok = True
widths = True
for h in range(1, 8):
    fam = odd_width_families(h)
    for k, v in fam.items():
        for c in v:
            ok &= blocks(c) == h or k == 'dip, two hills'
    ok &= all(blocks(up_down) == h + min(p, q) - x for (p, q, x, up_down) in
              [(p, q, x, tuple(list(range(1, p + 1)) + list(range(p, x, -1)) + [x] + list(range(x + 1, q + 1))
                + list(range(q, 0, -1))))
               for p in range(1, h + 1) for q in range(1, h + 1) if max(p, q) == h for x in range(1, min(p, q))])
    g = lambda k: fam.get(k, [])
    widths &= {len(c) for c in g('dip, two ramps') + g('dip, ramp and hill')} <= {2 * h + 1}
    widths &= {len(c) for c in g('step of 2')} <= {2 * h - 1}
    widths &= sorted(len(c) for c in g('spike')) == list(range(1, 2 * h, 2))
    widths &= {len(c) for c in g('dip, two hills')} == set(range(2 * h + 3, 4 * h, 2))
print(f"[5] blocks: h outside the dips between two hills, h + min(p, q) - x on them, h <= 7: {ok}")
print(f"[5] widths: 2h + 1 for the dips between ramps or a ramp and a hill, 2h - 1 for the steps of 2, "
      f"1, 3, ..., 2h - 1 for the spikes, 2h + 3, ..., 4h - 1 for the dips between two hills, h <= 7: {widths}")
