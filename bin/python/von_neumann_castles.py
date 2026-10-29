# Von Neumann castles: the castle of a set is a bottom block carrying the castles of its members,
# one empty column between neighbors; vN(n) is the castle of the von Neumann ordinal n = {0, ..., n-1}.
# Checks: the examples; width, height, area and columns of vN(n); its blocks row by row (the binomial
# tree); the castles of plane trees are the alternating castles of odd width, counted by blocks by the
# Catalan numbers; the castles of hereditarily finite sets by blocks (A004111); the Ackermann castles
# ack(m) of the natural numbers: blocks, width, height, parity (A372325), against the OEIS.
# Page: wiki/pages/von-neumann-castles.md.  OEIS data below: the data fields, read 2026-10-28.
import sys
from functools import lru_cache, cmp_to_key
from math import comb

sys.setrecursionlimit(10000)

OEIS = {  # A-number: (offset, data field)
    'A000079': (0, [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536]),
    'A000108': (0, [1, 1, 2, 5, 14, 42, 132, 429, 1430, 4862, 16796, 58786, 208012, 742900]),
    'A000225': (0, [0, 1, 3, 7, 15, 31, 63, 127, 255, 511, 1023, 2047, 4095, 8191, 16383, 32767, 65535]),
    'A000120': (0, [0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2, 3, 2, 3, 3, 4, 1, 2, 2, 3, 2, 3, 3, 4, 2, 3, 3, 4, 3, 4,
                    4, 5, 1, 2, 2, 3, 2, 3, 3, 4, 2, 3, 3, 4, 3, 4, 4, 5, 2, 3, 3, 4, 3, 4, 4, 5, 3, 4, 4, 5,
                    4, 5, 5, 6, 1, 2, 2, 3, 2, 3, 3, 4, 2, 3, 3, 4, 3, 4, 4, 5, 2, 3, 3, 4, 3, 4, 4, 5, 3, 4,
                    4, 5, 4, 5, 5, 6, 2, 3, 3, 4, 3, 4, 4, 5, 3]),
    'A001511': (1, [1, 2, 1, 3, 1, 2, 1, 4, 1, 2, 1, 3, 1, 2, 1, 5, 1, 2, 1, 3, 1, 2, 1, 4, 1, 2, 1, 3, 1, 2,
                    1, 6, 1, 2, 1, 3, 1, 2, 1, 4, 1, 2, 1, 3, 1, 2, 1, 5, 1, 2, 1, 3, 1, 2, 1, 4, 1, 2, 1, 3,
                    1, 2, 1, 7, 1, 2, 1, 3, 1, 2, 1, 4, 1, 2, 1, 3, 1, 2, 1, 5, 1, 2, 1, 3, 1, 2, 1, 4, 1, 2,
                    1, 3, 1, 2, 1, 6, 1, 2, 1, 3, 1, 2, 1, 4, 1]),
    'A004111': (0, [0, 1, 1, 1, 2, 3, 6, 12, 25, 52, 113, 247, 548, 1226, 2770, 6299]),
    'A010096': (1, [1, 2, 2] + [3] * 12 + [4] * 64),
    'A014221': (-1, [0, 1, 2, 4, 16, 65536]),
    'A033922': (0, [1, 1, 1, 2, 1, 2, 2, 3, 2, 3, 3, 4, 3, 4, 4, 5, 1, 2, 2, 3, 2, 3, 3, 4, 3, 4, 4, 5, 4, 5,
                    5, 6, 2, 3, 3, 4, 3, 4, 4, 5, 4, 5, 5, 6, 5, 6, 6, 7, 3, 4, 4, 5, 4, 5, 5, 6, 5, 6, 6, 7,
                    6, 7, 7, 8, 2, 3, 3, 4, 3, 4, 4, 5, 4, 5, 5, 6, 5, 6, 6, 7, 3, 4, 4, 5, 4, 5]),
    'A034797': (0, [0, 1, 3, 11, 2059]),
    'A057711': (0, [0, 1, 2, 6, 16, 40, 96, 224, 512, 1152, 2560, 5632, 12288, 26624, 57344, 122880, 262144]),
    'A116549': (0, [1, 2, 3, 4, 4, 5, 6, 7, 5, 6, 7, 8, 8, 9, 10, 11, 5, 6, 7, 8, 8, 9, 10, 11, 9, 10, 11, 12,
                    12, 13, 14, 15, 6, 7, 8, 9, 9, 10, 11, 12, 10, 11, 12, 13, 13, 14, 15, 16, 10, 11, 12, 13,
                    13, 14, 15, 16, 14, 15, 16, 17, 17, 18, 19, 20]),
    'A230864': (1, [0, 1, 2, 2] + [3] * 12 + [4] * 64),
    'A372325': (1, [0, 2, 5, 7, 8, 10, 13, 15, 16, 18, 21, 23, 24, 26, 29, 31, 33, 35, 36, 38, 41, 43, 44, 46, 49,
                    51, 52, 54, 57, 59, 60, 62, 64, 66, 69, 71, 72, 74, 77, 79, 80, 82, 85, 87, 88, 90, 93, 95,
                    97, 99, 100, 102, 105, 107, 108, 110, 113, 115, 116, 118, 121, 123, 124]),
}


def oeis(anum, n):
    off, data = OEIS[anum]
    return data[n - off]


def oeis_range(anum):
    off, data = OEIS[anum]
    return range(off, off + len(data))


# ---------------------------------------------------------------- castles, trees, skylines

def castle_of_tree(t):
    """Plane tree t (tuple of child trees) -> skyline: a bottom block carrying the children's castles."""
    if not t:
        return (1,)
    cols = []
    for j, ch in enumerate(t):
        if j:
            cols.append(0)
        cols.extend(castle_of_tree(ch))
    return tuple(c + 1 for c in cols)


def blocks(c):
    return c[0] + sum(max(0, c[i] - c[i - 1]) for i in range(1, len(c)))


def runs(c, r, lo=0, hi=None):
    """Maximal runs of columns of height >= r in c[lo:hi], as (start, end) pairs, end exclusive."""
    hi = len(c) if hi is None else hi
    out, i = [], lo
    while i < hi:
        if c[i] >= r:
            j = i
            while j < hi and c[j] >= r:
                j += 1
            out.append((i, j))
            i = j
        else:
            i += 1
    return out


def block_tree(c, r=1, lo=0, hi=None):
    """The tree of blocks of a castle: each block's children are the blocks standing on it."""
    hi = len(c) if hi is None else hi
    return tuple(block_tree(c, r + 1, a, b) for a, b in runs(c, r + 1, lo, hi))


def alternating(c):
    """Odd width, and c_1 > c_2 < c_3 > ... < c_w (width 1 included)."""
    w = len(c)
    return w % 2 == 1 and all((c[i] > c[i + 1]) if i % 2 == 0 else (c[i] < c[i + 1]) for i in range(w - 1))


def nodes(t):
    return 1 + sum(nodes(ch) for ch in t)


def leaves(t):
    return 1 if not t else sum(leaves(ch) for ch in t)


def depth(t):
    return 0 if not t else 1 + max(depth(ch) for ch in t)


def canon(t):
    return tuple(sorted(canon(ch) for ch in t))


def vN_tree(n):
    return tuple(vN_tree(k) for k in range(n))


@lru_cache(None)
def vN(n):
    return castle_of_tree(vN_tree(n))


def s2(i):
    return bin(i).count('1')


def draw(c, labels=None):
    h = max(c)
    rows = []
    for r in range(h, 0, -1):
        if labels is None:
            rows.append(' '.join('#' if x >= r else '.' for x in c))
        else:
            rows.append(' '.join(labels[r - 1][i] if c[i] >= r else '.' for i in range(len(c))))
    return rows


def label_grid(t, name):
    """Cell labels: each cell shows name(subtree) of the block it belongs to."""
    c = castle_of_tree(t)
    grid = [['.'] * len(c) for _ in range(max(c))]

    def fill(t, r, lo):
        w = len(castle_of_tree(t))
        for i in range(lo, lo + w):
            grid[r][i] = name(t)
        x = lo
        for ch in t:
            fill(ch, r + 1, x)
            x += len(castle_of_tree(ch)) + 1
    fill(t, 0, 0)
    return c, grid


ok_all = True


def check(label, cond):
    global ok_all
    ok_all &= bool(cond)
    print(label, bool(cond))


# ---------------------------------------------------------------- [1] examples

print('[1] the von Neumann castles vN(0), ..., vN(4):')
for n in range(5):
    print(f'    vN({n}) = {vN(n)}')
for n in range(4):
    print(f'    vN({n}):', ' | '.join(draw(vN(n))))
ordinal_name = {canon(vN_tree(k)): str(k) for k in range(6)}
c3, g3 = label_grid(vN_tree(3), lambda t: ordinal_name[canon(t)])
print('    vN(3), each cell labeled by the ordinal of its block:')
for row in draw(c3, g3):
    print('       ', row)
check('[1] vN(2) = (2, 1, 3) and vN(3) = (2, 1, 3, 1, 3, 2, 4):', vN(2) == (2, 1, 3) and vN(3) == (2, 1, 3, 1, 3, 2, 4))
check('[1] vN(n+1) = vN(n), (1), vN(n) raised by one, for n = 1..12:',
      all(vN(n + 1) == vN(n) + (1,) + tuple(x + 1 for x in vN(n)) for n in range(1, 13)))
check('[1] vN(n) is a prefix of vN(n+1), n = 1..12; vN(0) = (1) is not a prefix of vN(1) = (2):',
      all(vN(n + 1)[:len(vN(n))] == vN(n) for n in range(1, 13)) and vN(1)[:1] != vN(0))

# ---------------------------------------------------------------- [2] width, height, area, columns

N2 = 14
check(f'[2] width 2^n - 1 = A000225(n), height n + 1, for n = 1..{N2}:',
      all(len(vN(n)) == 2 ** n - 1 == oeis('A000225', n) and max(vN(n)) == n + 1 for n in range(1, N2 + 1)))
check(f'[2] area (n+1) 2^(n-1) for n = 1..{N2}, and area = A057711(n + 1) for n = 0..{N2}:',
      all(sum(vN(n)) == (n + 1) * 2 ** (n - 1) for n in range(1, N2 + 1))
      and all(sum(vN(n)) == oeis('A057711', n + 1) for n in range(0, N2 + 1)))
print('[2] areas n = 0..10:', [sum(vN(n)) for n in range(11)])
check(f'[2] column i of vN(n) is s2(i) + (i mod 2), i = 1..2^n - 1, n = 1..{N2}:',
      all(vN(n)[i - 1] == s2(i) + i % 2 for n in range(1, N2 + 1) for i in range(1, 2 ** n)))
c = vN(7)
check('[2] vN(7): even columns c_(2j) = A000120(j), odd columns c_(2j+1) = A000120(j) + 2:',
      all(c[2 * j - 1] == oeis('A000120', j) for j in range(1, 64))
      and all(c[2 * j] == oeis('A000120', j) + 2 for j in range(0, 64)))
def v2(x):
    return (x & -x).bit_length() - 1


check('[2] vN(n): c_1 = 2, rise c_(2j+1) - c_(2j) = 2, fall c_(2j-1) - c_(2j) = A001511(j), j = 1..2^(n-1) - 1, n = 1..7:',
      all(vN(n)[0] == 2
          and all(vN(n)[2 * j] - vN(n)[2 * j - 1] == 2 for j in range(1, 2 ** (n - 1)))
          and all(vN(n)[2 * j - 2] - vN(n)[2 * j - 1] == oeis('A001511', j) for j in range(1, 2 ** (n - 1)))
          for n in range(1, 8)))
check(f'[2] the same with the fall 1 + v2(j), the 2-adic valuation of 2j, n = 1..{N2}:',
      all(vN(n)[0] == 2
          and all(vN(n)[2 * j] - vN(n)[2 * j - 1] == 2 for j in range(1, 2 ** (n - 1)))
          and all(vN(n)[2 * j - 2] - vN(n)[2 * j - 1] == 1 + v2(j) for j in range(1, 2 ** (n - 1)))
          for n in range(1, N2 + 1)))
print('[2] the first 31 columns:', vN(5))

# ---------------------------------------------------------------- [3] blocks: the binomial tree


def binomial_tree(k):
    return tuple(binomial_tree(j) for j in range(k - 1, -1, -1))


check('[3] the membership tree of n is the binomial tree B_n (unordered), n = 0..10:',
      all(canon(vN_tree(n)) == canon(binomial_tree(n)) for n in range(11)))
check(f'[3] row d + 1 of vN(n) has C(n, d) blocks, d = 0..n, n = 0..{N2}:',
      all(len(runs(vN(n), d + 1)) == comb(n, d) for n in range(N2 + 1) for d in range(n + 1)))
check(f'[3] blocks(vN(n)) = 2^n = A000079(n) by the column formula, n = 0..{N2}:',
      all(blocks(vN(n)) == 2 ** n == oeis('A000079', n) for n in range(N2 + 1)))
print('[3] blocks by row, n = 0..5:', [[len(runs(vN(n), r)) for r in range(1, n + 2)] for n in range(6)])
print('[3] parity: vN(0) has 1 block; vN(n), n >= 1, has 2^n blocks, even')

# ---------------------------------------------------------------- [4] castles of plane trees


@lru_cache(None)
def forests(k):
    """Sequences of plane trees with k nodes in total."""
    if k == 0:
        return [()]
    out = []
    for first in range(1, k + 1):
        for t in plane_trees(first):
            for rest in forests(k - first):
                out.append((t,) + rest)
    return out


@lru_cache(None)
def plane_trees(n):
    return list(forests(n - 1))


B4 = 10
ok_shape = ok_inv = ok_stats = True
count = {}
for b in range(1, B4 + 1):
    cs = set()
    for t in plane_trees(b):
        c = castle_of_tree(t)
        cs.add(c)
        ok_shape &= alternating(c)
        ok_inv &= block_tree(c) == t
        ok_stats &= len(c) == 2 * leaves(t) - 1 and max(c) == depth(t) + 1 and blocks(c) == b
    count[b] = len(cs)
check(f'[4] every plane tree with at most {B4} nodes has an alternating castle of odd width:', ok_shape)
check(f'[4] width = 2 leaves - 1, height = depth + 1, blocks = nodes, for the same trees:', ok_stats)
check(f'[4] the block tree of castle(t) is t, for the same trees:', ok_inv)
check(f'[4] distinct castles of plane trees with b nodes = A000108(b - 1), b = 1..{B4}:',
      all(count[b] == oeis('A000108', b - 1) for b in range(1, B4 + 1)))
print('[4] castles of plane trees by blocks:', [count[b] for b in range(1, B4 + 1)])


def all_skylines(w, h):
    if w == 0:
        yield ()
        return
    for rest in all_skylines(w - 1, h):
        for x in range(1, h + 1):
            yield rest + (x,)


ok_conv, n_alt = True, 0
for w in range(1, 10, 2):
    for c in all_skylines(w, 5):
        if alternating(c):
            n_alt += 1
            ok_conv &= castle_of_tree(block_tree(c)) == c
check(f'[4] every alternating skyline of odd width <= 9 on heights 1..5 ({n_alt} of them) is the castle of its block tree:', ok_conv)


def alternating_by_blocks(b):
    """Alternating castles of odd width with exactly b blocks (their height is at most b)."""
    found = []

    def grow(c, part):
        if len(c) % 2 == 1 and part == b:
            found.append(tuple(c))
            return
        if len(c) % 2 == 1:      # next column lower
            for x in range(1, c[-1]):
                grow(c + [x], part)
        else:                     # next column higher
            for x in range(c[-1] + 1, b + 1):
                if part + x - c[-1] <= b:
                    grow(c + [x], part + x - c[-1])
    for x in range(1, b + 1):
        grow([x], x)
    return found


check('[4] alternating castles of odd width with b blocks, enumerated directly, = A000108(b - 1), b = 1..8:',
      all(len(alternating_by_blocks(b)) == oeis('A000108', b - 1) for b in range(1, 9)))

# ---------------------------------------------------------------- [5] castles of hereditarily finite sets


@lru_cache(None)
def code_cmp(x, y):
    """Compare Ackermann codes without computing them: the larger set holds the larger element of x ^ y."""
    if x == y:
        return 0
    z = max(x ^ y, key=cmp_to_key(code_cmp))
    return 1 if z in x else -1


def ordered(x):
    return sorted(x, key=cmp_to_key(code_cmp))


def set_tree(x):
    """The membership tree of x, members in increasing Ackermann code."""
    return tuple(set_tree(y) for y in ordered(x))


def set_nodes(x):
    return 1 + sum(set_nodes(y) for y in x)


N5 = 13
by_size = {1: [frozenset()]}
pool = [frozenset()]
for n in range(2, N5 + 1):
    out = []

    def dfs(i, left, chosen):
        if left == 0:
            out.append(frozenset(chosen))
            return
        for j in range(i, len(pool)):
            s = set_nodes(pool[j])
            if s > left:
                break
            dfs(j + 1, left - s, chosen + [pool[j]])
    dfs(0, n - 1, [])
    by_size[n] = out
    pool = sorted(pool + out, key=set_nodes)
check(f'[5] hereditarily finite sets with b nodes = A004111(b), b = 1..{N5}:',
      all(len(by_size[b]) == oeis('A004111', b) for b in range(1, N5 + 1)))
ok_dist = ok_stats5 = ok_order = True
for b in range(1, N5 + 1):
    cs = set()
    for x in by_size[b]:
        t = set_tree(x)
        c = castle_of_tree(t)
        cs.add(c)
        ok_stats5 &= blocks(c) == b and len(c) == 2 * leaves(t) - 1 and alternating(c)
        if b <= 10:
            rev = castle_of_tree(tuple(reversed(t)))
            ok_order &= len(rev) == len(c) and max(rev) == max(c) and blocks(rev) == blocks(c) and sum(rev) == sum(c)
    ok_dist &= len(cs) == len(by_size[b])
check(f'[5] the castles of distinct sets are distinct (members in increasing code), b = 1..{N5}:', ok_dist)
check(f'[5] blocks = nodes, width = 2 leaves - 1, alternating, for the same sets:', ok_stats5)
check('[5] width, height, blocks and area unchanged when the members of the root are reversed, b <= 10:', ok_order)
print('[5] castles of hereditarily finite sets by blocks:', [len(by_size[b]) for b in range(1, N5 + 1)])

# ---------------------------------------------------------------- [6] Ackermann castles of the natural numbers


def bits(m):
    return [k for k in range(m.bit_length()) if m >> k & 1]


@lru_cache(None)
def ack(m):
    """The castle of the set with Ackermann code m: members are the k with bit k of m set, in increasing k."""
    if m == 0:
        return (1,)
    cols = []
    for j, k in enumerate(bits(m)):
        if j:
            cols.append(0)
        cols.extend(ack(k))
    return tuple(x + 1 for x in cols)


@lru_cache(None)
def rank(m):
    return 0 if m == 0 else 1 + rank(m.bit_length() - 1)


M6 = 2 ** 16
print('[6] the Ackermann castles ack(m), m = 0..15:')
for m in range(16):
    c = ack(m)
    print(f'    m = {m:2d} = {m:04b}  members {bits(m)}  skyline {c}  width {len(c)}  height {max(c)}  blocks {blocks(c)}')
check('[6] blocks(ack(m)) = A116549(m) on the data field:', all(blocks(ack(m)) == oeis('A116549', m) for m in oeis_range('A116549')))
check(f'[6] blocks(ack(m)) = 1 + sum of blocks(ack(k)) over the bits k of m, and A116549 recursion a(m + 2^n) = a(n) + a(m), m < 2^16:',
      all(blocks(ack(m)) == 1 + sum(blocks(ack(k)) for k in bits(m)) for m in range(M6))
      and all(blocks(ack(m + 2 ** n)) == blocks(ack(n)) + blocks(ack(m)) for n in range(16) for m in range(2 ** n) if m + 2 ** n < M6))
check('[6] width(ack(m)) = 2 A033922(m) - 1 on the data field:', all(len(ack(m)) == 2 * oeis('A033922', m) - 1 for m in oeis_range('A033922')))
check('[6] (width + 1)/2 = A033922 definition: 1 at m = 0, else the sum over the bits k of m, m < 2^16:',
      all((len(ack(m)) + 1) // 2 == (1 if m == 0 else sum((len(ack(k)) + 1) // 2 for k in bits(m))) for m in range(M6)))
check('[6] height(ack(m)) = 1 + A010096(m) (m >= 1) and 1 + A230864(m + 1) on the data fields:',
      all(max(ack(m)) == 1 + oeis('A010096', m) for m in oeis_range('A010096'))
      and all(max(ack(m)) == 1 + oeis('A230864', m + 1) for m in range(0, 80)))
check('[6] height(ack(m)) = 1 + rank(m), rank(0) = 0, rank(m) = 1 + rank(floor(log2 m)), m < 2^16:',
      all(max(ack(m)) == 1 + rank(m) for m in range(M6)))
check('[6] height(ack(m)) = h exactly when A014221(h - 2) <= m < A014221(h - 1), m < 2^16 and m = 65536:',
      all(oeis('A014221', max(ack(m)) - 2) <= m < oeis('A014221', max(ack(m)) - 1) for m in list(range(M6)))
      and max(ack(65536)) == 6)
check('[6] width(ack(m)) = 1 exactly for m in {0, 1, 2, 4, 16} below 2^16 (A014221), and ack(65536) = (6):',
      [m for m in range(M6) if len(ack(m)) == 1] == [0, 1, 2, 4, 16] and ack(65536) == (6,))
check('[6] vN(n) = ack(A034797(n)), n = 0..4:', all(vN(n) == ack(oeis('A034797', n)) for n in range(5)))
check('[6] A034797(n + 1) = A034797(n) + 2^A034797(n), the code of n + 1 = n u {n}:',
      all(oeis('A034797', n + 1) == oeis('A034797', n) + 2 ** oeis('A034797', n) for n in range(4)))
even = [m for m in range(64) if blocks(ack(m)) % 2 == 0]
print('[6] m < 64 with an even-block castle ack(m):', even)
check('[6] blocks(ack(m)) = 1 + #{bits k of m with blocks(ack(k)) odd} mod 2, m < 2^16:',
      all(blocks(ack(m)) % 2 == (1 + sum(blocks(ack(k)) % 2 for k in bits(m))) % 2 for m in range(M6)))
odd = [m for m in range(M6) if blocks(ack(m)) % 2 == 1]


def a372325(n_max):
    """The entry's rule: k is a term when an even number of the 1s of k sit at positions that are terms."""
    terms, mask = [], 0
    for k in range(n_max):
        if bin(k & mask).count('1') % 2 == 0:
            terms.append(k)
            mask |= 1 << k
    return terms


check('[6] the m with an odd-block castle ack(m) = A372325(n), n >= 1, on the data field and by its rule for m < 2^16:',
      odd[:len(OEIS['A372325'][1])] == OEIS['A372325'][1] and odd == a372325(M6))
check('[6] A372325 example: 118 = 2^6 + 2^5 + 2^4 + 2^2 + 2^1 has an odd-block castle; 8192 = 2^13 does not:',
      blocks(ack(118)) % 2 == 1 and blocks(ack(8192)) % 2 == 0)
check('[6] the m with an odd-block castle are the m with A116549(m) odd, on the data field:',
      all((m in odd) == (oeis('A116549', m) % 2 == 1) for m in oeis_range('A116549')))
print('[6] areas m = 0..15:', [sum(ack(m)) for m in range(16)])

print('all checks passed:', ok_all)
