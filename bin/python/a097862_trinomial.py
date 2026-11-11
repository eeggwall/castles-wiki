# 1-smooth castles of width w and height h with both end columns at height 1, by trinomial coefficients.
# The count is A097862(w - 1, h - 1), the Motzkin paths of length w - 1 and height h - 1, and for h >= 2
#   count(w, h) = tri(w-1, 2h-2) - 3 tri(w-1, 2h) + 3 tri(w-1, 2h+2) - tri(w-1, 2h+4)    (w <= 4h - 2),
# with tri(n, d) = [t^d](1/t + 1 + t)^n = A027907(n, n + d).  At w = 4h - 1 the right side is 1 short.
# Optional argv[1]: the A097862 b-file (https://oeis.org/A097862/b097862.txt).
import sys

W = 141  # widths 1..W, so path lengths n = w - 1 up to 140

# trinomial rows: tri_rows[n][n + d] = tri(n, d)
tri_rows = [[1]]
for n in range(1, W + 8):
    prev = tri_rows[-1]
    row = [0] * (2 * n + 1)
    for i, c in enumerate(prev):
        row[i] += c; row[i + 1] += c; row[i + 2] += c
    tri_rows.append(row)

def tri(n, d):
    d = abs(d)
    return tri_rows[n][n + d] if d <= n else 0

# [1] The castles from the definition: c_1 = c_w = 1, |c_{i+1} - c_i| <= 1, c_i >= 1, height = max c_i.
#     Dynamic program over (current height, maximum so far); count[w][h].
count = [[0] * (W + 2) for _ in range(W + 1)]
state = {(1, 1): 1}
for w in range(1, W + 1):
    for (c, m), v in state.items():
        if c == 1:
            count[w][m] += v
    nxt = {}
    for (c, m), v in state.items():
        for b in (c - 1, c, c + 1):
            if b >= 1:
                key = (b, max(m, b))
                nxt[key] = nxt.get(key, 0) + v
    state = nxt
print(f"[1] castles with c_1 = c_w = 1 by (w, h), w <= {W}; w = 5: {count[5][1:4]}, w = 7: {count[7][1:5]}")

if len(sys.argv) > 1:
    b = [int(l.split()[1]) for l in open(sys.argv[1]) if l.strip() and not l.startswith('#')]
    flat, n = [], 0
    while len(flat) < len(b) and n + 1 <= W:
        flat += [count[n + 1][k + 1] for k in range(n // 2 + 1)]
        n += 1
    m = min(len(flat), len(b))
    assert b[:m] == flat[:m], "b-file differs"
    print(f"    A097862 b-file: first {m} terms (rows 0..{n - 1}) == count(n + 1, k + 1)")

# [2] The four-term formula for h >= 2, w <= 4h - 2 (it is 0 for w < 2h - 1)
def four(w, h):
    n = w - 1
    return tri(n, 2*h - 2) - 3 * tri(n, 2*h) + 3 * tri(n, 2*h + 2) - tri(n, 2*h + 4)
checked = 0
for h in range(2, W + 1):
    for w in range(1, min(W, 4 * h - 2) + 1):
        assert four(w, h) == count[w][h], (w, h)
        checked += 1
print(f"[2] four-term formula == count for 2 <= h, w <= min({W}, 4h - 2): {checked} pairs (w, h)")

# [3] At w = 4h - 1 the count exceeds the formula by exactly 1
hs = [h for h in range(2, W + 1) if 4 * h - 1 <= W]
assert all(count[4*h - 1][h] - four(4*h - 1, h) == 1 for h in hs)
print(f"[3] count(4h - 1, h) - formula = 1 for h = 2..{hs[-1]}")

# [4] Method of images: strips on {1..H} with both ends at height 1 (not required to reach H) number
#     Sum_j [tri(w-1, 2j(H+1)) - tri(w-1, 2j(H+1) + 2)], against a transfer-matrix count
for H in range(1, 40):
    v = [1] + [0] * (H - 1)  # v[i] = walks ending at height i + 1
    for w in range(1, W + 1):
        if w > 1:
            v = [(v[i-1] if i else 0) + v[i] + (v[i+1] if i < H - 1 else 0) for i in range(H)]
        n, P = w - 1, 2 * (H + 1)
        images = sum(tri(n, j * P) - tri(n, j * P + 2) for j in range(-(n // P) - 1, n // P + 2))
        assert images == v[0], (H, w)
print(f"[4] image sum == pinned strips on {{1..H}}, H <= 39, w <= {W}")
