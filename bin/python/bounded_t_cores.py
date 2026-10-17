# Towers and castles vs t-core partitions (Cho-Huh-Nam-Sohn, arXiv:2205.15554, Thm 3.3, Prop 3.4,
# Thm 3.7, Prop 3.8): the map from a core to a tower, the height bound vs the largest hook length,
# the Narayana sum indexed by blocks and its refinement by bargraph peaks, the palindromic towers,
# and A^e(w, h) as a count of cores.
# Pages: wiki/pages/cho-huh-nam-sohn-2022-bounded-free-motzkin-paths.md, tower-heap.md,
# narayana-numbers.md, castle-classification-shape.md.
from itertools import product
from math import comb
from collections import Counter

def N(n, k):  # Narayana number; 0 outside 1 <= k <= n
    return comb(n, k) * comb(n, k - 1) // n if 1 <= k <= n else 0

def blocks(c):  # tower blocks, c_0 = 0
    return sum(max(0, b - a) for a, b in zip((0,) + tuple(c), c))

def bargraph_peaks(c):  # plateaus strictly higher than both neighbors, height 0 outside the base
    runs = [x for i, x in enumerate(c) if i == 0 or c[i - 1] != x]
    runs = [0] + runs + [0]
    return sum(1 for a, x, b in zip(runs, runs[1:], runs[2:]) if x > a and x > b)

def narayana_by_blocks(L, b, i=None):  # Prop 3.4 with t = L + 1, m = b; term i alone if given
    if b == 0: return 1 if i in (None, 0) else 0
    terms = {j: N(b, j) * comb(L + 1 + 2 * b - 2 * j, 2 * b) for j in range(1, b + 1)}
    return sum(terms.values()) if i is None else terms.get(i, 0)

def palindromic_by_blocks(L, b):  # Prop 3.8 with t = L + 1, m = b
    if b == 0: return 1
    h = (L + 1) // 2
    return sum(comb((b - 1) // 2, (i - 1) // 2) * comb(b // 2, i // 2) * comb(h + b - i, b)
               for i in range(1, min(b, h) + 1))

# 1. towers by blocks: the Narayana sum indexed by blocks, its bargraph-peak refinement, palindromes
for L, B in [(1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 6)]:
    by_b, by_bi, pal = Counter(), Counter(), Counter()
    for c in product(range(B + 1), repeat=L):
        b = blocks(c)
        if b > B: continue
        by_b[b] += 1
        by_bi[b, bargraph_peaks(c)] += 1
        if c == c[::-1]: pal[b] += 1
    assert all(by_b[b] == narayana_by_blocks(L, b) for b in range(B + 1)), L
    assert all(by_bi[b, i] == narayana_by_blocks(L, b, i) for b in range(B + 1) for i in range(b + 1)), L
    assert all(pal[b] == palindromic_by_blocks(L, b) for b in range(B + 1)), L
    print(f"L={L}, b<={B}: T^ = sum_i N(b,i) C(L+1+2b-2i, 2b), term i = towers with i bargraph peaks,"
          f" palindromic = Prop 3.8: True;  T^ = {[by_b[b] for b in range(B + 1)]}, pal = {[pal[b] for b in range(B + 1)]}")

# 2. doubling the middle column: palindromic towers on odd L -> L + 1, blocks and height kept
for L in (1, 3, 5):
    for B in range(6):
        src = [c for c in product(range(B + 1), repeat=L) if c == c[::-1] and blocks(c) == B]
        img = {c[:L // 2 + 1] + c[L // 2:] for c in src}
        tgt = {c for c in product(range(B + 1), repeat=L + 1) if c == c[::-1] and blocks(c) == B}
        assert img == tgt and len(img) == len(src) and all(max(d) == max(c) for c, d in zip(src, (c[:L // 2 + 1] + c[L // 2:] for c in src)))
print("doubling the middle column: palindromic towers L -> L + 1 (L = 1, 3, 5, b <= 5) bijective, blocks and height kept: True")

# 3. t-cores: partitions with largest hook lambda_1 + len - 1 < K
def partitions_largest_hook_below(K):
    out = [()]
    def rec(prefix, maxpart):
        for p in range(min(maxpart, K), 0, -1):
            lam = prefix + (p,)
            if lam[0] + len(lam) - 1 >= K: continue
            out.append(lam)
            rec(lam, p)
    rec((), K)
    return out

def conjugate(lam): return tuple(sum(1 for x in lam if x > j) for j in range(lam[0])) if lam else ()
def hooks(lam):
    conj = conjugate(lam)
    return [(lam[i] - j - 1) + (conj[j] - i - 1) + 1 for i in range(len(lam)) for j in range(lam[i])]
def first_column_hooks(lam): return [lam[i] + (len(lam) - i - 1) for i in range(len(lam))]
def is_core(lam, t): return t not in hooks(lam)
def corners(lam): return len(set(lam))
def core_to_tower(lam, t):  # c_j = number of first-column hook lengths congruent to j mod t
    hs = first_column_hooks(lam)
    assert all(x % t for x in hs)
    return tuple(sum(1 for x in hs if x % t == j) for j in range(1, t))

for t in range(2, 7):
    L = t - 1
    for k in range(0, 4):
        cores = [lam for lam in partitions_largest_hook_below(k * t) if is_core(lam, t)] if k else [()]
        image = [core_to_tower(lam, t) for lam in cores]
        towers = [c for c in product(range(k + 1), repeat=L)]
        assert sorted(image) == sorted(towers), (t, k)                       # bijection onto towers of height <= k
        assert all(blocks(core_to_tower(lam, t)) == corners(lam) for lam in cores)   # blocks = corners
        # self-conjugate cores and palindromic towers: equal counts by corners / blocks (Thm 3.7 is a
        # different bijection; the residue map does not send conjugation to reversal)
        sc = Counter(corners(lam) for lam in cores if lam == conjugate(lam))
        assert sc == Counter(blocks(c) for c in towers if c == c[::-1]), (t, k)
    print(f"t={t}: core -> tower (residue counts of first-column hooks) is a bijection from t-cores with"
          f" largest hook < k t onto towers of height <= k, blocks = corners; self-conjugate cores by corners"
          f" = palindromic towers by blocks, k <= 3: True")
print("the residue map does not restrict: self-conjugate 3-core (1) ->", core_to_tower((1,), 3))
print("example: (4,4,2,2) is a 4-core:", is_core((4, 4, 2, 2), 4), " tower", core_to_tower((4, 4, 2, 2), 4),
      " first-column hooks", first_column_hooks((4, 4, 2, 2)), " corners", corners((4, 4, 2, 2)))

# 4. A^e(w, h) and A(w, h) as counts of (w + 1)-cores with largest hook in [(h-2)(w+1), (h-1)(w+1))
def castle_blocks(c): return blocks(c)  # same formula with c_i >= 1
for w in range(1, 6):
    t = w + 1
    for h in range(2, 5):
        sk = [c for c in product(range(1, h + 1), repeat=w) if max(c) == h]
        win = [lam for lam in partitions_largest_hook_below((h - 1) * t)
               if lam and is_core(lam, t) and lam[0] + len(lam) - 1 >= (h - 2) * t]
        Ae = sum(1 for c in sk if castle_blocks(c) % 2 == 0)
        assert len(sk) == len(win) and Ae == sum(1 for lam in win if corners(lam) % 2 == 1), (w, h)
        pal = [c for c in sk if c == c[::-1]]
        scw = [lam for lam in win if lam == conjugate(lam)]
        assert len(pal) == len(scw) and sum(1 for c in pal if castle_blocks(c) % 2 == 0) == sum(1 for lam in scw if corners(lam) % 2 == 1)
    print(f"w={w}, h=2..4: A(w,h) = nonempty (w+1)-cores in the window, A^e(w,h) = those with odd corners,"
          f" palindromic = self-conjugate: True; A^e(w,2..4) = {[sum(1 for c in product(range(1, h + 1), repeat=w) if max(c) == h and castle_blocks(c) % 2 == 0) for h in range(2, 5)]}")

# 5. the paper's Tables 1 and 2
print("Table 1, t = 2..6:", [[narayana_by_blocks(t - 1, m) for m in range(1, 9)] for t in range(2, 7)])
print("Table 2, t = 2, 4, 6, 8, 10:", [[palindromic_by_blocks(t - 1, m) for m in range(1, 9)] for t in (2, 4, 6, 8, 10)])
