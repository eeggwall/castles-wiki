# The parity of A^e(w, h), the number of even-block castles of width w and height h: the mirror
# keeps the block count, a palindrome has the parity of its middle column, and so for w >= 3
# A^e(w, h) is congruent to floor((h - 1)/2) mod 2. Also the palindromic castles of each cell and
# their even-block count. Pages: wiki/pages/mod-p-observatory.md (section "Modulo 2"),
# wiki/pages/castle-classification-shape.md (the palindromic type), wiki/pages/castle-sign.md,
# wiki/pages/castle-counting-function.md.
from itertools import product


def blocks(c):
    """Total ascent of the skyline from height 0: the block count."""
    return sum(max(0, b - a) for a, b in zip((0,) + c, c))


def signed_strips(h, W):
    """sum of (-1)^blocks over the skylines in {1..h}^w, for w = 1..W, by the transfer matrix."""
    if h == 0:
        return [0] * W
    v = [(-1) ** a for a in range(1, h + 1)]
    out = [sum(v)]
    for _ in range(2, W + 1):
        n = [0] * h
        tot, pre, alt = sum(v), 0, 0
        for b in range(h):                         # column height b + 1
            n[b] = (tot - pre) + (-1) ** b * alt   # from a >= b: no rise; from a < b: rise b - a
            alt += v[b] * (-1) ** b
            pre += v[b]
        v = n
        out.append(sum(v))
    return out


def even_count(W, H):
    """A^e(w, h) for 1 <= w <= W, 1 <= h <= H, as (A + S)/2."""
    table = {}
    for h in range(1, H + 1):
        s, t = signed_strips(h, W), signed_strips(h - 1, W)
        for w in range(1, W + 1):
            table[(w, h)] = (h ** w - (h - 1) ** w + s[w - 1] - t[w - 1]) // 2
    return table


# [1] the parity law against the exact counts
W = H = 60
Ae = even_count(W, H)
assert Ae[(4, 2)] == 10 and Ae[(13, 10)] == 3729050610636 and Ae[(10, 13)] == 37959702514
bad = [(w, h) for (w, h), x in Ae.items() if w >= 3 and x % 2 != ((h - 1) // 2) % 2]
small = [(w, h) for (w, h), x in Ae.items() if w <= 2 and x % 2 != (1 if h % 2 == 0 else 0)]
print(f"[1] A^e(w, h) = floor((h-1)/2) mod 2 for 3 <= w <= {W}, 1 <= h <= {H}: {not bad}")
print(f"[1] A^e(w, h) = 1 mod 2 exactly for even h, at w = 1, 2 and 1 <= h <= {H}: {not small}")
print("[1] Project Euler checkpoints A^e(4, 2) = 10, A^e(13, 10) = 3729050610636,"
      " A^e(10, 13) = 37959702514 reproduced; all three even")
for h in range(1, 13):
    print(f"[1] h = {h:2d}: A^e(w, h) mod 2 for w = 1..12:",
          ''.join(str(Ae[(w, h)] % 2) for w in range(1, 13)))

# [2] the mirror keeps the block count; palindromes and their parity, by enumeration
for h in range(1, 6):
    for w in range(1, 8):
        if h ** w > 200000:
            continue
        castles = [c for c in product(range(1, h + 1), repeat=w) if max(c) == h]
        assert all(blocks(c) == blocks(c[::-1]) for c in castles)
        pal = [c for c in castles if c == c[::-1]]
        k = (w + 1) // 2                                   # ceil(w/2)
        assert len(pal) == h ** k - (h - 1) ** k
        assert all(blocks(c) % 2 == c[k - 1] % 2 for c in pal)
        even_pal = sum(1 for c in pal if blocks(c) % 2 == 0)
        assert even_pal == (h // 2) * h ** (k - 1) - ((h - 1) // 2) * (h - 1) ** (k - 1)
        even = sum(1 for c in castles if blocks(c) % 2 == 0)
        assert even % 2 == even_pal % 2 and even == Ae[(w, h)]
print("[2] for every castle with h <= 5, w <= 7 (h^w <= 200000): the mirror keeps the block count;"
      " the palindromic castles number h^ceil(w/2) - (h-1)^ceil(w/2); a palindrome's block count"
      " has the parity of its middle column; the even-block palindromes number"
      " floor(h/2) h^(ceil(w/2)-1) - floor((h-1)/2) (h-1)^(ceil(w/2)-1); and A^e(w, h) has the"
      " parity of the even-block palindromes")

# [3] the three Project Euler 502 targets
for w, h in ((10 ** 12, 100), (10 ** 4, 10 ** 4), (100, 10 ** 12)):
    print(f"[3] A^e({w}, {h}): h mod 4 = {h % 4}, so A^e is", "odd" if ((h - 1) // 2) % 2 else "even")
