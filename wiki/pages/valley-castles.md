---
title: Valleys and valley castles
category: Concepts
summary: A valley of a castle is a pair of columns i < j − 1 with every column between them lower than both; its depth is min(c_i, c_j) minus the tallest column between. A castle of height h has h plus the total depth of its valleys as its block count, so the Project Euler 502 parity is the parity of h plus the total depth; the convex core lies above each column by the depths of the valleys over it; valleys never cross, a castle has at most w − 2 of them, and it has none exactly when it is convex. A valley castle has exactly one valley, and the valley castles of width w and height h number (h − 1)² C(w + 2h − 3, 2h); the even-block ones number C(h, 2) C(w + 2h − 3, 2h) at odd h and C(h − 1, 2) C(w + 2h − 3, 2h) at even h. A k-valley castle has exactly k valleys; at height 2 these number C(w + 1, 2k + 2).
tags: [concept, castle, valley, valley-castle, k-valley-castle, convex-castle, convex-core, block-count, parity, rule-3, horizontal-visibility, tower-word, binomial, verification]
sources: [project-euler-502-brute-force]
created: 2026-10-25
updated: 2026-10-25
---

# Valleys and valley castles

## Definition

A castle of width `w` and height `h` is a skyline `(c_1, …, c_w)` with `1 ≤ c_i ≤ h` and some `c_i = h` ([[castle-polyomino](pages/castle-polyomino.md)]).

A **valley** of a castle is a pair of columns `i < j − 1` such that every column between them is lower than both: `c_l < min(c_i, c_j)` for `i < l < j`. Columns `i` and `j` are its **walls**. The **floor** of the valley is the tallest column between the walls, `floor(i, j) = max(c_{i+1}, …, c_{j−1})`; its **depth** is `depth(i, j) = min(c_i, c_j) − floor(i, j)`, at least 1; and its **span** is `j − i − 1`, the number of columns between the walls. `val(c)` is the number of valleys of the castle `c`.

- A **valley castle** has exactly one valley.
- A **k-valley castle** has exactly `k` valleys. The 1-valley castles are the valley castles, and the 0-valley castles are the convex castles (section *Three identities*).

*Examples.* The castle `(2, 1, 1, 3, 2)` has one valley, with walls 1 and 4, floor 1, depth 1 and span 2, so it is a valley castle. The castle `(3, 1, 2, 1, 3)` has three valleys, each of depth 1: walls 1 and 3, walls 3 and 5, and walls 1 and 5, whose floor is the column of height 2. The castle `(2, 1, 3, 3, 1, 1, 2)` carried through [[q-thread-seminar](pages/q-thread-seminar.md)] is a 2-valley castle, with walls 1 and 3 and walls 4 and 7.

**A valley is a gap between blocks, followed up the rows.** In row `r` the blocks are the maximal runs of columns with `c_l ≥ r`,[^bf] and Project Euler 502 requires a unit of space between neighboring blocks of a row.[^pe] A run of empty cells in row `r` between two blocks covers columns `i + 1, …, j − 1` with `c_i ≥ r`, `c_j ≥ r` and every column between below `r`, so `(i, j)` is a valley. Conversely a valley `(i, j)` has a gap over exactly columns `i + 1, …, j − 1` in the rows `r` with `floor(i, j) < r ≤ min(c_i, c_j)`, which are `depth(i, j)` rows. So the gaps of the castle, row by row, are the valleys counted with their depths. In particular a castle has tower spacing at least `g` ([[tower-spacing-castles](pages/tower-spacing-castles.md)]) exactly when every valley has span at least `g`.

**Other valleys and the vee castles.** The valley `DU` of a Dyck or Motzkin path is a different object: a factor of a word, which a castle's tower word never contains ([[tower-word-language](pages/tower-word-language.md)]). The vee castles, which weakly decrease and then weakly increase ([[castle-by-area](pages/castle-by-area.md)]), are a shape type and can have many valleys: `(3, 2, 1, 2, 3)` has two, with walls 2 and 4 and walls 1 and 5.

## Notation used on this page

| symbol | meaning |
|---|---|
| `floor(i, j)`, `depth(i, j)` | the tallest column between the walls of the valley `(i, j)`, and `min(c_i, c_j) − floor(i, j)` |
| `val(c)` | the number of valleys of the castle `c` |
| `A_valley(w, h)`, `A^e_valley`, `A^o_valley`, `S_valley` | the valley castles of width `w` and height `h`; the even-block and odd-block ones; `A^e_valley − A^o_valley` |
| `A_{k-valley}(w, h)` | the k-valley castles of width `w` and height `h` |
| `f` | in the proof of the theorem, the height of the floor |
| `d` | a depth, from 1 to `h − 1`, in the section *Depth and parity* |

## Three identities

**Blocks.** A castle of height `h` has

```
blocks(c)  =  h  +  Σ depth(i, j)          (sum over the valleys of c)
```

*Proof.* Each row `r` with `1 ≤ r ≤ h` holds at least one cell, so it has one block more than it has gaps between blocks. By the row reading above, the valley `(i, j)` has a gap in exactly `depth(i, j)` rows. Adding over the rows gives the identity.[^exec1]

So the block count is even, the Project Euler 502 condition, exactly when `h` plus the total depth is even. A castle has the fewest blocks, `h`, exactly when it has no valley, and these are the convex castles, the castles of height `h` with `h` blocks ([[convex-castle](pages/convex-castle.md)]).

**Convex core.** With `core(c)_l = min(max(c_1, …, c_l), max(c_l, …, c_w))` the convex core of [[convex-core](pages/convex-core.md)], every column `l` has

```
core(c)_l − c_l  =  Σ depth(i, j)          (sum over the valleys with i < l < j)
```

*Proof.* Column `l` is empty in row `r` and lies in a gap of that row exactly when `c_l < r` and there are columns of height at least `r` on both sides of `l`, that is, when `c_l < r ≤ core(c)_l`. Each such gap belongs to one valley over column `l`, and each valley over column `l` has a gap there in `depth(i, j)` rows. Adding over the columns, the cells between a castle and its convex core number the sum of `depth(i, j) × span` over the valleys.[^exec1]

**Nesting.** Two valleys never cross. If `i < i′ < j < j′` with `(i, j)` and `(i′, j′)` both valleys, then `c_{i′} < c_j`, because `i′` lies between the walls `i` and `j`, and `c_j < c_{i′}`, because `j` lies between `i′` and `j′`. So any two valleys are disjoint, possibly sharing a wall, or one lies inside the other. Gutin, Mansour and Severini (2011) call a pair of positions of a word **visible** when every letter between them is smaller than both, so neighboring positions always form a visible pair.[^gms-def] The valleys of a castle are its visible pairs of positions that are not neighbors, so the castle has `(w − 1) + val(c)` visible pairs. Their bound of `2n − 3` edges for a horizontal visibility graph on `n` vertices, whose edges are the visible pairs,[^gms-max] gives `val(c) ≤ w − 2` for `w ≥ 2`.[^exec1] They also give the generating function of the words over `{1, …, k}` by visible pairs,[^gms-gf] and the castles of height `h` are the words over `{1, …, h}` that use the letter `h`.

## Valley castles

**Theorem.** For `w ≥ 1` and `h ≥ 1`, the valley castles of width `w` and height `h` number

```
A_valley(w, h)  =  (h − 1)² · C(w + 2h − 3, 2h).
```

The count is 0 at `h = 1` and for `w ≤ 2`. Its first values, from `w = 3`:[^exec2]

| `h` | `A_valley(w, h)`, `w = 3, 4, 5, 6, 7, 8` | formula |
|---|---|---|
| 2 | `1, 5, 15, 35, 70, 126` | `C(w + 1, 4)` |
| 3 | `4, 28, 112, 336, 840, 1848` | `4 C(w + 3, 6)` |
| 4 | `9, 81, 405, 1485, 4455, 11583` | `9 C(w + 5, 8)` |

The proof has two lemmas about the shape of a valley castle and a count of its tower words.

**Lemma 1 (flat floor).** If `(i, j)` is the only valley of a castle, every column between its walls has the same height.

*Proof.* Let `M` be the tallest height between the walls. If the column `i + 1` is lower than `M`, let `p` be the leftmost column between the walls with height `M`; every column between `i` and `p` is lower than `M`, and `M < c_i`, so `(i, p)` is a second valley. In the same way the column `j − 1` has height `M`. If some column between the walls is lower than `M`, the nearest columns of height `M` on its two sides, with only lower columns between them, form a second valley.

**Lemma 2 (shape).** For two columns `i < j − 1`, call `(c_1, …, c_i)` the left part and `(c_j, …, c_w)` the right part. A castle has exactly one valley if and only if it has two columns `i < j − 1` with all of the following:

- every column between `i` and `j` has the same height `f`, with `f < min(c_i, c_j)`;
- the left part and the right part are unimodal, rising weakly to their maximum and then falling weakly;
- either `c_i ≥ c_j` and the right part is weakly decreasing (case A), or `c_i ≤ c_j` and the left part is weakly increasing (case B).

Its valley is then `(i, j)`. This is the construction rule of the type: a flat-floored dip between two walls, with the side of the lower wall falling away from it.

*Proof that one valley forces the shape.* The floor is flat by Lemma 1. A valley inside the left part or inside the right part would be a second valley, so both parts are unimodal, which for a skyline means having no valley. If `c_i > c_j` and the right part is not weakly decreasing, then it begins with columns of height `c_j` followed by a taller column `q`; every column between `i` and `q` is at most `c_j`, which is below both `c_i` and `c_q`, so `(i, q)` is a second valley. The case `c_i < c_j` is the mirror image. If `c_i = c_j = m` and neither case holds, then the left part has a column taller than `m` and so does the right part; the last such column of the left part and the first such column of the right part have only columns of height at most `m` between them, so they form a second valley.

*Proof that the shape has one valley.* The two parts contain no valley, since they are unimodal, and no valley has a wall on the flat floor, since the floor columns are equal and lower than the walls. Any other valley `(p, q)` has `p ≤ i` and `q ≥ j` and contains a wall of `(i, j)` between its own walls. In case A, if `q > j` then `c_q ≤ c_j`, and if `q = j` then `p < i` and `c_i ≥ c_j`; either way a column between `p` and `q` is not lower than `min(c_p, c_q)`. Case B is the mirror image.[^exec3]

**Counting tower words.** The tower word of a castle writes its towers, the castle lowered by one row, as a word in `U` (up one row), `R` (one column) and `D` (down one row), with one `R` per column at the column's tower height, starting and ending at height 0, and the castle is recovered from the heights at which the `R`s stand ([[tower-word-language](pages/tower-word-language.md)]). The castle `(2, 1, 3)` has the tower word `URDRUURDD`. Fixing the letters `U` and `D` and choosing where the `R`s go counts castles.

*Warm-up.* A convex castle of height `h` has the letters `U^{h−1}` followed by `D^{h−1}`. Its `w` letters `R` go into the `2h − 1` slots before, between and after these letters, with at least one in the slot between the last `U` and the first `D`, the columns of height `h`. That gives `C(w + 2h − 3, w − 1)` castles, the count of [[convex-castle-binomial-identity](pages/convex-castle-binomial-identity.md)].

*Case A, with the floor height `f` and the right wall `c_j` fixed, `1 ≤ f < c_j ≤ h`.* The castle's tallest column lies in the left part, and the letters are, in order, `U^{h−1}` (the rise to the top in the left part), `D^{h−f}` (the fall to the floor), `U^{c_j−f}` (the rise to the right wall) and `D^{c_j−1}` (the fall through the right part). The `R`s are placed with these rules:

- at least one `R` right after `U^{h−1}`: the columns of height `h`;
- at least one `R` right after `D^{h−f}`: the floor;
- at least one `R` right after `U^{c_j−f}`: the right wall;
- no `R` between the letters of `U^{c_j−f}`, since the floor is flat and the right wall is the first column after it;
- no `R` between the last `c_j − f` letters of `D^{h−f}`. The left wall is the last `R` before the floor, so this rule says that at least `c_j − f` falls follow it, which is `c_i ≥ c_j`.

Every slot at a change of direction then holds an `R`, so these are tower words. Each gives a castle of case A: the left part rises and then falls, the floor is flat at height `f`, below `c_j ≤ c_i`, and the right part is weakly decreasing because only `D`s follow the right wall. The castle fixes `f` and `c_j`, so each castle of case A is counted once. The word has `(h − 1) + (h − f) + (c_j − f) + (c_j − 1)` letters `U` and `D` and one slot more than that; `2(c_j − f − 1)` of the slots stay empty, which leaves `2h + 1` slots for any `f` and `c_j`. Placing `w` letters `R` into `2h + 1` slots, three of them nonempty, can be done in `C(w + 2h − 3, 2h)` ways. There are `C(h, 2)` pairs `(f, c_j)`, so case A has `C(h, 2) C(w + 2h − 3, 2h)` castles.

*Case B* is the mirror image of case A and has as many castles.

*Both cases.* A castle in both cases has `c_i = c_j`, its left part weakly increasing and its right part weakly decreasing, so its tallest column is a wall and `c_i = c_j = h`. These are exactly the castles of case A with `c_j = h`, since `c_j = h` forces `c_i = h` and leaves no `R` among the falls `D^{h−f}`. So `(h − 1) C(w + 2h − 3, 2h)` castles are in both cases, and

```
A_valley(w, h)  =  [ 2 C(h, 2) − (h − 1) ] · C(w + 2h − 3, 2h)  =  (h − 1)² · C(w + 2h − 3, 2h).   ∎
```

The case count checks against enumeration: `C(w + 2h − 3, 2h)` for each pair `(f, c_j)` of case A, and `(h − 1) C(w + 2h − 3, 2h)` castles in both cases, exactly those of case A with `c_j = h`.[^exec4]

### Depth and parity

In case A the depth of the valley is `c_j − f`, and in case B it is `c_i − f`. For a depth `d` with `1 ≤ d ≤ h − 1`, `h − d` pairs `(f, c_j)` of case A have `c_j − f = d`, as many pairs of case B have depth `d`, and the pair `(h − d, h)` is in both. Each pair gives `C(w + 2h − 3, 2h)` castles, so the valley castles of depth `d` number

```
(2h − 1 − 2d) · C(w + 2h − 3, 2h).
```

By the block identity a valley castle of depth `d` has `h + d` blocks, so it has an even block count exactly when `d` and `h` have the same parity. Adding `2h − 1 − 2d` over those depths gives the even-block and odd-block valley castles, the even-block ones being those that Project Euler 502 counts:[^exec5]

| | `h` odd | `h` even |
|---|---|---|
| `A^e_valley(w, h)` | `C(h, 2) C(w + 2h − 3, 2h)` | `C(h − 1, 2) C(w + 2h − 3, 2h)` |
| `A^o_valley(w, h)` | `C(h − 1, 2) C(w + 2h − 3, 2h)` | `C(h, 2) C(w + 2h − 3, 2h)` |

So `S_valley(w, h) = (−1)^{h+1} (h − 1) C(w + 2h − 3, 2h)`.

By the block identity the castles of height `h` with `h + 1` blocks are the valley castles of depth 1, which number `(2h − 3) C(w + 2h − 3, 2h)`. This is the `h + 1` column of the width-height-blocks table on [[odd-castles-and-block-tables](pages/odd-castles-and-block-tables.md)]. The castles with `h + 2` blocks are the valley castles of depth 2, `(2h − 5) C(w + 2h − 3, 2h)` of them, which is the first term of that table's `h + 2` column, together with the 2-valley castles whose two valleys both have depth 1.[^exec6]

## k-valley castles

- **No valley.** The 0-valley castles are the convex castles, `C(w + 2h − 3, w − 1)` of them.
- **Height 2.** Every valley of a castle of height 2 has two walls of height 2, floor 1 and depth 1, so a castle of height 2 with `k` valleys has `k + 1` maximal runs of columns of height 2 and `2 + k` blocks. The runs are fixed by their `2k + 2` ends among the `w + 1` places before, between and after the columns, so `A_{k-valley}(w, 2) = C(w + 1, 2k + 2)`.[^exec7]
- **Height 3, two valleys.** `A_{2-valley}(w, 3) = 12 C(w + 3, 8) + 2 C(w + 3, 7)` for `3 ≤ w ≤ 16`, by computation; there is no proof yet.[^exec7]

The castles of height 3 and 4 by number of valleys, for `w = 3, …, 8`:[^exec7]

| `w` | height 3, `k = 0, 1, …` | height 4, `k = 0, 1, …` |
|---|---|---|
| 3 | `15, 4` | `28, 9` |
| 4 | `35, 28, 2` | `84, 81, 10` |
| 5 | `70, 112, 28, 1` | `210, 405, 155, 11` |
| 6 | `126, 336, 180, 23` | `462, 1485, 1155, 255, 10` |
| 7 | `210, 840, 780, 218, 11` | `924, 4455, 5830, 2622, 358, 8` |
| 8 | `330, 1848, 2640, 1298, 185, 4` | `1716, 11583, 22880, 17342, 5004, 446, 4` |

## Related Concepts

- [[convex-castle](pages/convex-castle.md)] - the 0-valley castles, the castles of height `h` with `h` blocks.
- [[convex-core](pages/convex-core.md)] - the smallest convex skyline above a castle, which lies above each column by the depths of the valleys over it.
- [[odd-castles-and-block-tables](pages/odd-castles-and-block-tables.md)] - the castles counted by width, height and blocks, whose `h + 1` column the theorem gives.
- [[tower-word-language](pages/tower-word-language.md)] - the tower word used in the count.
- [[tower-spacing-castles](pages/tower-spacing-castles.md)] - the castles whose valleys all have span at least `g`.
- [[castle-by-area](pages/castle-by-area.md)] - the vee castles, whose valleys all nest.
- [[castle-classification-shape](pages/castle-classification-shape.md)] - the catalogue entries for the valley and k-valley castles.
- [[castle-notation](pages/castle-notation.md)] - the valley symbols and the other meanings of "valley" on the wiki.

## Footnotes

[^pe]: https://projecteuler.net/problem=502 (read 2026-10-25) - "Any two neighboring blocks on the same row have at least one unit of space between them."
[^bf]: [[project-euler-502-brute-force](pages/project-euler-502-brute-force.md)] §"Column-height encoding" L20-27 - "A block is a maximal horizontal run of columns at a given level", and "two runs at the same level are always separated by a strictly lower column."
[^gms-def]: https://arxiv.org/pdf/1010.1850 p.3 §V Definition 11 - "We say that the pair (x_i, x_j) with i + 1 ≤ j is visible if x_{i+1}, x_{i+2}, . . . , x_{j−1} < min{x_i, x_j}. Clearly, (x_i, x_{i+1}) is a visible pair."
[^gms-max]: https://arxiv.org/pdf/1010.1850 p.3 §IV Corollary 9 and §V Theorem 12 - "The maximum number of edges in an HVG on n vertices is 2n − 3 and the graph is maximal outerplanar", and "each edge {i, j} in the graph G corresponds to visible pair (x_i, x_j)".
[^gms-gf]: https://arxiv.org/pdf/1010.1850 p.3-4 §V Definition 14 and Theorem 16 [synthesis] - `F_k(x, q)`, the generating function of the words in `[k]^n` by the number of visible pairs, built by cutting each word at the occurrences of its largest letter `k` (Lemma 15) and given as a product formula in Theorem 16.
[^exec1]: Verified by execution (Python 3.10, 2026-10-25): `bin/python/valley_castles.py` item [1], run log `bin/python/valley_castles-run.log`. For every castle with `w ≤ 9` and `h ≤ 5`: the block identity; the convex-core identity at every column and its sum `Σ depth × span`; no two valleys crossing; at most `w − 2` valleys, and none exactly for the unimodal castles; and `(w − 1) + val(c)` visible pairs.
[^exec2]: Verified by execution (Python 3.10, 2026-10-25): `bin/python/valley_castles.py` items [2] and [4], run log `bin/python/valley_castles-run.log`. The theorem for `1 ≤ w ≤ 16` and `1 ≤ h ≤ 7` by a left-to-right scan whose state is the stack of columns that can still be a left wall, and the scan against brute force for `w ≤ 9`, `h ≤ 5`.
[^exec3]: Verified by execution (Python 3.10, 2026-10-25): `bin/python/valley_castles.py` item [3], run log `bin/python/valley_castles-run.log`. For every castle with `w ≤ 9` and `h ≤ 5`: it has exactly one valley if and only if exactly one pair of columns meets the three conditions of Lemma 2, and that pair is the valley.
[^exec4]: Verified by execution (Python 3.10, 2026-10-25): `bin/python/valley_castles.py` item [5], run log `bin/python/valley_castles-run.log`, for every castle with `w ≤ 9` and `h ≤ 5`.
[^exec5]: Verified by execution (Python 3.10, 2026-10-25): `bin/python/valley_castles.py` item [6], run log `bin/python/valley_castles-run.log`. The depth counts by brute force for `w ≤ 9`, `h ≤ 5`; the even-block and odd-block counts and `S_valley` by brute force there and by the scan for `w ≤ 16`, `h ≤ 7`.
[^exec6]: Verified by execution (Python 3.10, 2026-10-25): `bin/python/valley_castles.py` item [7], run log `bin/python/valley_castles-run.log`. For every castle with `w ≤ 9` and `2 ≤ h ≤ 5`: the castles with `h + 1` blocks are the valley castles of depth 1; the castles with `h + 2` blocks number `(2h − 5) C(N, 2h) + 2(2h − 5) C(N, 2h + 1) + (2h + 1)(h − 2) C(N, 2h + 2)` with `N = w + 2h − 3` (for `h ≥ 3`), and the valley castles of depth 2 among them `(2h − 5) C(N, 2h)`.
[^exec7]: Verified by execution (Python 3.10, 2026-10-25): `bin/python/valley_castles.py` item [8], run log `bin/python/valley_castles-run.log`. The 0-valley count for `w ≤ 16`, `h ≤ 7`; the height-2 count `C(w + 1, 2k + 2)` for `w ≤ 18`; the height-3 2-valley formula for `w ≤ 16`; and the table, all by the scan.
