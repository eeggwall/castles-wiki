---
title: Brick-wall castles
category: Concepts
summary: A brick-wall castle is a castle on the hexagonal tiling {6,3} read as a brick wall in running bond - a bottom row of w bricks, every brick above resting on both bricks below it, the blocks being the maximal runs of bricks in a row. They are the fountains of coins of Odlyzko and Wilf. Shifting row t by t places, along the slants of Thomas and May, turns a brick-wall castle into a square-grid castle whose first column has height 1 and whose columns rise by at most 1, a 1-histogram, with the same rows, blocks, height and cells; mirrored, these are the castles that drop by at most 1 and end at height 1. The levels after the up-steps of a Dyck path are the same skylines, with height the path's height and blocks w + 1 − peaks. So the brick-wall castles of width w number C_w, by height they are A080936, by blocks the Narayana numbers, by w + blocks A004148, by cells the fountains A005169 with Odlyzko and Wilf's continued fraction. The signed count Σ(−1)^blocks is 0 at even width and (−1)^((w+1)/2) C_((w−1)/2) at odd width, so the even-block ones are A071688. At height 2 there are 2^(w−1) − 1, Σ C(w, 4k+2) (A038505) of them even-block. The block fountains, one block per row, are the convex members, F_(2w−1) of them, and the mirrored Euler castles are the walls whose rows end at the right edge.
tags: [concept, castle, brick-wall-castle, hexagonal-tiling, fountain-of-coins, histogram, shear, dyck-path, catalan, narayana, parity, block-fountain, continued-fraction]
sources: [endicott-may-shacklette-2018-stacks-of-spheres, thomas-may-2022-mountain-counting, paule-prodinger-2003-fountains-histograms-q-identities]
created: 2026-10-29
updated: 2026-10-29
---

# Brick-wall castles

The hexagonal tiling `{6,3}`, in which every cell is a hexagon and three hexagons meet at each vertex, falls into rows of hexagons when one family of its edges is vertical. Each hexagon touches two hexagons in its row, two in the row below and two in the row above, and read as bricks the rows are a wall laid in running bond, each brick centered over a joint of the row below. A castle needs a base row, an up direction, rows and a support rule, and on the brick wall the rule "no overhang" says that a brick rests on both bricks below it.

## Definition

A **brick-wall castle** of width `w` is a set of bricks on the brick wall with

- a full bottom row of `w` bricks, and
- every brick above the bottom row resting on both bricks below it.

Number the rows `t = 0, 1, …` from the bottom, and the bricks of row `t` as `0, …, w − 1 − t`, so that brick `i` of row `t` rests on bricks `i` and `i + 1` of row `t − 1`. The **blocks** are the maximal runs of bricks in a row, the **height** `h` is the number of rows, and the **cells** are the bricks. A run of `m` bricks carries at most `m − 1` bricks above it, so the height is at most `w`. `A_brick(w, h)` counts the brick-wall castles of width `w` and height `h`, `A^e_brick` and `A^o_brick` its even-block and odd-block parts, and `S_brick(w, h) = A^e_brick(w, h) − A^o_brick(w, h)` its signed count; without `h` they run over all heights.

*Example.* A brick-wall castle of width 5 and height 3, with 4 blocks (one in row 0, two in row 1, one in row 2) and 9 cells:

```
row 2        [##]
row 1      [##][##]    [##]
row 0    [##][##][##][##][##]
```

*All brick-wall castles of width 3.* There are five, with heights 1, 2, 2, 2, 3 and blocks 1, 2, 2, 2, 3:

```
(a)                    (b)                    (c)                    (d)                    (e)
                                                                                                [##]
                         [##]                       [##]               [##][##]               [##][##]
[##][##][##]           [##][##][##]           [##][##][##]           [##][##][##]           [##][##][##]
```

A brick-wall castle is a fountain of coins: an `(n, w)` fountain is `n` coins whose bottom row is `w` contiguous coins, every coin in a higher row resting on two coins of the row below ([[endicott-may-shacklette-2018-stacks-of-spheres](pages/endicott-may-shacklette-2018-stacks-of-spheres.md)], [[thomas-may-2022-mountain-counting](pages/thomas-may-2022-mountain-counting.md)]).[^em-def][^tm-def]

## The shear onto the 1-histograms

**Proposition (the shear).** Shift row `t` of a brick-wall castle `t` places to the right, so that brick `i` of row `t` lands in column `i + t + 1`, and let `s_k` be the number of bricks in column `k`, `k = 1, …, w`. Then `(s_1, …, s_w)` is a square-grid skyline with

```
s_1 = 1,    s_{k+1} ≤ s_k + 1   (1 ≤ k < w),
```

a **1-histogram**, and every 1-histogram of width `w` comes from exactly one brick-wall castle of width `w`. Row `t` of the castle becomes row `t + 1` of the skyline, shifted, so the castle and its skyline have the same height, the same blocks in every row, and the same number of cells.

*Proof.* Brick `i` of row `t` lands in column `k = i + t + 1` and rests on bricks `i` and `i + 1` of row `t − 1`, which land in columns `k − 1` and `k`. So a column holds a brick in row `t` only if it holds one in row `t − 1`, and the bricks of a column form a stack from the bottom: the sheared castle is a skyline. The support in column `k − 1` says `s_{k−1} ≥ s_k − 1`, and a brick of row `t ≥ 1` lands in column `i + t + 1 ≥ 2`, so the leftmost column holds only its bottom brick and `s_1 = 1`. Conversely, a skyline with these two properties shifts back to a set of bricks whose every brick above the bottom row has both supports. A row moves as a whole, so its runs, and with them the blocks, are kept.

These are the slants of Thomas and May, who cut a fountain into its diagonals and prove that the slant heights `⟨s_1, …, s_w⟩` describe a fountain exactly when `s_1 = 1` and `s_{k−1} ≥ s_k − 1`.[^tm-slant] Paule and Prodinger call these sequences the 1-histograms and state, after Merlini and Sprugnoli, that counting fountains by coins is counting 1-histograms by area.[^pp-hist] The shear keeps rows and blocks, checked brick by brick for `w ≤ 10`.[^exec]

The example of width 5 shears to the skyline `(1, 2, 3, 1, 2)`:

```
row 3   .  .  #  .  .
row 2   .  #  #  .  #
row 1   #  #  #  #  #
```

again 4 blocks and 9 cells, and the five castles of width 3 shear to `(1, 1, 1)`, `(1, 2, 1)`, `(1, 1, 2)`, `(1, 2, 2)` and `(1, 2, 3)`.

**The mirror.** Reversed, a 1-histogram is a castle that drops by at most 1 from each column to the next and ends at height 1: `(1, 2, 3, 1, 2)` becomes `(2, 1, 3, 2, 1)`. Those castles are on [[motzkin-castles](pages/motzkin-castles.md)], in the section *Relatives in the semi-perimeter grading*, and in [[castle-sequence-catalog](pages/castle-sequence-catalog.md)], counted by `C_w` by width and by A004148 by semi-perimeter. So the brick-wall castles are those square-grid castles, sheared and mirrored, and every count of the brick wall below is a count of them.

## Dyck paths

**Proposition (up-step levels).** For a Dyck path of semilength `w`, let `s_k` be the level reached by its `k`-th up-step. Then `(s_1, …, s_w)` is a 1-histogram, every 1-histogram of width `w` arises from exactly one Dyck path, the height of the path is `max s_k`, and the number of blocks of the skyline is `w + 1 − p`, with `p` the number of peaks `UD` of the path.

*Proof.* The first up-step reaches level 1. Between two up-steps the path takes some number `d ≥ 0` of down-steps, so `s_{k+1} = s_k − d + 1 ≤ s_k + 1`, and `s_{k+1} ≥ 1` because the path stays at level 0 or above. Conversely the `s_k` fix the number of down-steps between up-steps, and the path closes with down-steps to level 0. A path reaches its highest level at the end of an up-step, so its height is `max s_k`. The blocks of a skyline number `s_1 + Σ_k max(0, s_{k+1} − s_k)` ([[castle-polyomino](pages/castle-polyomino.md)]), here `1 + #{k : s_{k+1} = s_k + 1}`, and `s_{k+1} = s_k + 1` exactly when up-steps `k` and `k + 1` are neighbors, a factor `UU`. A path with `w` up-steps in `p` runs, each run ending in a peak, has `w − p` factors `UU`, so the skyline has `w + 1 − p` blocks.

Checked for `w ≤ 12`.[^exec] With the shear, the brick-wall castles of width `w`, height `h` and `b` blocks are in bijection with the Dyck paths of semilength `w`, height `h` and `w + 1 − b` peaks. The example of width 3 pairs `(1, 1, 1)` with `UDUDUD` (3 peaks, 1 block) and `(1, 2, 3)` with `UUUDDD` (1 peak, 3 blocks).

## Counts

| brick-wall castles counted by | count | OEIS | from |
|---|---|---|---|
| width `w` | `C_w` | A000108 | the Catalan count of fountains by bottom row[^em-cat]; the shear |
| width and height | the Dyck paths of semilength `w` and height `h` | A080936 | up-step levels |
| width and blocks `b` | `N(w, w + 1 − b) = N(w, b)`, the Narayana numbers | A001263 | up-step levels, and the symmetry `N(w, k) = N(w, w + 1 − k)` |
| semi-perimeter `s = w + b` | `A004148(s − 1)`, the peakless Motzkin paths | A004148 | the shear and [[motzkin-castles](pages/motzkin-castles.md)] |
| cells `n` | the fountains of `n` coins | A005169 | the continued fraction below |
| width, one block per row | `F_{2w−1}` | A001519 | the block fountains below |

Each row agrees with a column sweep over the 1-histograms, which agrees with brute-force enumeration of the walls for `w ≤ 10`: width, height and blocks for `w ≤ 16`, semi-perimeter for `s ≤ 16`, cells for `n ≤ 18`.[^exec] The Dyck paths of semilength `w` with `p` peaks number `N(w, p)` ([[narayana-numbers](pages/narayana-numbers.md)]), so by the up-step proposition the castles with `b` blocks number `N(w, w + 1 − b)`, which the symmetry `N(w, k) = N(w, w + 1 − k)` turns into `N(w, b)`.

**Cells.** Endicott, May and Shacklette state Odlyzko and Wilf's continued fraction for the fountains by coins `x` and bottom row `y`,[^em-cf]

```
Σ_{castles} x^{cells} y^{w}  =  1 / (1 − xy / (1 − x²y / (1 − x³y / (1 − ⋯)))),
```

whose coefficients agree with the brick-wall castles by cells and width for up to 18 cells. At `y = 1` it counts the castles by cells, `1, 1, 2, 3, 5, 9, 15, 26, 45, 78, …` from one cell, the fountains of `n` coins, A005169, and Paule and Prodinger's quotient of q-series gives the same series, `Σ_k (−1)^k q^{k(k+1)}/(q)_k` over `Σ_k (−1)^k q^{k²}/(q)_k`, with `(q)_k = (1 − q)⋯(1 − q^k)` ([[paule-prodinger-2003-fountains-histograms-q-identities](pages/paule-prodinger-2003-fountains-histograms-q-identities.md)]).[^exec]

## Parity

**Proposition (signed count over all heights).**

```
S_brick(w)  =  Σ_{castles of width w} (−1)^{blocks}  =  0                            for even w,
                                                       (−1)^{(w+1)/2} C_{(w−1)/2}      for odd w,
```

so the even-block brick-wall castles of width `w` number `A^e_brick(w) = (C_w + S_brick(w))/2`, which is `C_w/2` for even `w` and `(C_w + (−1)^{(w+1)/2} C_{(w−1)/2})/2` for odd `w`: `0, 1, 3, 7, 20, 66, 217, 715, 2424, 8398, …`, the plane trees with an even number of leaves, A071688.

*Proof.* By the up-step proposition, `(−1)^{blocks} = (−1)^{w+1} (−1)^{p}` for the Dyck path with `p` peaks. Let `D(x, t)` count the Dyck paths by semilength and peaks. Splitting a nonempty path at its first return to level 0 as `U P D Q`, the factor `U P D` has the peaks of `P`, or one peak when `P` is empty, so `D = 1 + x D (D − 1 + t)`. At `t = −1`, `x D² − (1 + 2x) D + 1 = 0`, and the root that is a power series is

```
D(x, −1)  =  ((1 + 2x) − √(1 + 4x²)) / (2x)  =  1 − Σ_{m≥0} (−1)^m C_m x^{2m+1},
```

from `√(1 − 4z) = 1 − 2 Σ_m C_m z^{m+1}` at `z = −x²`. So `Σ_p (−1)^p` over the paths of semilength `w` is 0 for even `w ≥ 2` and `−(−1)^m C_m` for `w = 2m + 1`, and `S_brick(w) = (−1)^{w+1}` times it.

The values agree with enumeration and with the OEIS data of A071688 for `w ≤ 16`.[^exec] For even `w` the symmetry of the Narayana numbers already splits the castles in half, since `b` and `w + 1 − b` have opposite parity.

**Fixed height.** The brick-wall version of the Project Euler 502 count is `A^e_brick(w, h)`. A brick-wall castle of height 2 shears to a skyline of 1s and 2s with `s_1 = 1`, any string of heights after the first column, and its blocks are 1 plus the number of runs of 2s. A binary string of length `w − 1` with `j` runs of 2s is fixed by the `2j` places where the runs start and end among `w` places, so

```
A_brick(w, 2)  =  2^{w−1} − 1,
A^e_brick(w, 2)  =  Σ_{j odd} C(w, 2j)  =  Σ_k C(w, 4k + 2),
```

the sum of every fourth entry of row `w` of Pascal's triangle from `C(w, 2)`, A038505(`w`), and `S_brick(w, 2)` is A077860(`w − 2`), the coefficients of `1/((1 − 2x + 2x²)(1 − x))`.[^exec] At greater heights a column sweep over the 1-histograms that keeps the height and the block count gives the even-block counts:

| `A^e_brick(w, h)` | `w = 1` | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `h = 1` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 2 | 0 | 1 | 3 | 6 | 10 | 16 | 28 | 56 | 120 | 256 | 528 | 1056 |
| 3 | 0 | 0 | 0 | 0 | 3 | 21 | 84 | 257 | 695 | 1826 | 4869 | 13153 |
| 4 | 0 | 0 | 0 | 1 | 7 | 28 | 87 | 258 | 825 | 2787 | 9318 | 30158 |
| 5 | 0 | 0 | 0 | 0 | 0 | 0 | 7 | 77 | 465 | 2092 | 8126 | 29755 |
| 6 | 0 | 0 | 0 | 0 | 0 | 1 | 11 | 66 | 293 | 1151 | 4521 | 18318 |

and the signed counts:

| `S_brick(w, h)` | `w = 1` | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `h = 1` | −1 | −1 | −1 | −1 | −1 | −1 | −1 | −1 | −1 | −1 | −1 | −1 |
| 2 | 0 | 1 | 3 | 5 | 5 | 1 | −7 | −15 | −15 | 1 | 33 | 65 |
| 3 | 0 | 0 | −1 | −5 | −12 | −15 | −1 | 32 | 49 | −17 | −184 | −303 |
| 4 | 0 | 0 | 0 | 1 | 7 | 23 | 42 | 32 | −34 | −87 | 57 | 399 |
| 5 | 0 | 0 | 0 | 0 | −1 | −9 | −38 | −93 | −123 | −15 | 235 | 286 |
| 6 | 0 | 0 | 0 | 0 | 0 | 1 | 11 | 57 | 176 | 327 | 264 | −302 |

The entries for `w ≤ 10` agree with brute-force enumeration of the walls, and those for `w = 11, 12` come from the sweep.[^exec] At `w = h` the only castle is the pyramid, with `h` blocks, which is why the diagonal alternates between 0 and 1.

## Sub-families

- **Block fountains.** The brick-wall castles with one block per row are the block fountains of Wilf, with generating function `(1 − 2y)/(1 − 3y + y²)` by width.[^em-block] One block per row means `h` blocks at height `h`, so the shear sends them to the convex 1-histograms, the unimodal ones, in the sense of [[convex-castle](pages/convex-castle.md)]. They number `F_{2w−1}`, `1, 2, 5, 13, 34, 89, …`, also `Σ_ℓ C(w + ℓ − 1, w − ℓ − 1)`.[^exec]
- **Euler castles.** The Euler castles of [[euler-castles](pages/euler-castles.md)] fall by 0 or 1 at each step and end at height 1, so their mirror images are the 1-histograms that rise by 0 or 1 at each step. Sheared back, they are the brick-wall castles whose every row is one block ending at the right end of its row, `2^{w−1}` of width `w`, each row strictly shorter than the one below; their row lengths are a partition of the cells into distinct parts with largest part `w`.[^exec]

## Appearances in Sources

- [[endicott-may-shacklette-2018-stacks-of-spheres](pages/endicott-may-shacklette-2018-stacks-of-spheres.md)] - the fountains, their Catalan count by bottom row, Odlyzko and Wilf's continued fraction, Wilf's block fountains, and the split at the first missing coin.
- [[thomas-may-2022-mountain-counting](pages/thomas-may-2022-mountain-counting.md)] - the slants, the shear of this page, and the fountains by width and last slant.
- [[paule-prodinger-2003-fountains-histograms-q-identities](pages/paule-prodinger-2003-fountains-histograms-q-identities.md)] - the 1-histograms and the fountains by coins as a quotient of q-series.

## Related Concepts

- [[castle-polyomino](pages/castle-polyomino.md)] - the castles on the square grid, the skylines the shear produces.
- [[motzkin-castles](pages/motzkin-castles.md)] - the castles that drop by at most 1 and end at height 1, the mirror images of the 1-histograms.
- [[catalan-numbers](pages/catalan-numbers.md)], [[narayana-numbers](pages/narayana-numbers.md)], [[dyck-words](pages/dyck-words.md)] - the brick-wall castles by width and by blocks, and the Dyck paths of the up-step levels.
- [[convex-castle](pages/convex-castle.md)], [[euler-castles](pages/euler-castles.md)] - the block fountains and the right-flush walls.
- [[castle-sign](pages/castle-sign.md)] - the signed count `S` and the parity split on the square grid.

## Footnotes

[^em-def]: [[endicott-may-shacklette-2018-stacks-of-spheres](pages/endicott-may-shacklette-2018-stacks-of-spheres.md)] §1 p.867 L35-L37 - "An (n, k) fountain is an arrangement of n coins into rows so that the bottom row consists of k contiguous coins and each coin in higher rows sits on two coins in the row beneath it."
[^tm-def]: [[thomas-may-2022-mountain-counting](pages/thomas-may-2022-mountain-counting.md)] §1 p.71 L50-L54 - "An (n, w) fountain of coins is an arrangement of n identical coins subject to two rules: the bottom row must consist of w contiguous coins, and the coins in higher rows must satisfy the gravity rule that each coin has to rest on two coins in the row immediately below. The number of coins in the bottom row of a fountain is called its width."
[^tm-slant]: [[thomas-may-2022-mountain-counting](pages/thomas-may-2022-mountain-counting.md)] §2 pp.72-73 L134-L157 [synthesis] - "it often is more fruitful instead to slice them diagonally into slants"; "We say the k th slant of a fountain is the set of all coins with constant position k in the rows."; a slant has no gaps, so a fountain is the `w`-tuple of its slant heights; "a sequence hs1 , . . . , sw i of positive integers represents a fountain if and only if" `s_1 = 1` and `s_{k−1} ≥ s_k − 1` for `1 < k ≤ w`.
[^pp-hist]: [[paule-prodinger-2003-fountains-histograms-q-identities](pages/paule-prodinger-2003-fountains-histograms-q-identities.md)] §1 p.101 L31-L38 - "Merlini and Sprugnoli [6] discuss fountains and histograms"; "A p-histogram is a sequence of columns in which the height of the ( j + 1)st column is at most k + p, if k is the height of column j; the first column has height r, with 1 ≤ r ≤ p."; "It can be shown that the enumeration of coins in a fountain is equivalent with the enumeration of 1-histograms."
[^em-cat]: [[endicott-may-shacklette-2018-stacks-of-spheres](pages/endicott-may-shacklette-2018-stacks-of-spheres.md)] §1 p.867 L54-L59 - "If the fountains are enumerated only by the number of coins in the bottom row"; "It is straightforward from (1) that the generating function satisfies G(y)− yG 2 (y) = 1, and so the gk are the Catalan numbers."
[^em-cf]: [[endicott-may-shacklette-2018-stacks-of-spheres](pages/endicott-may-shacklette-2018-stacks-of-spheres.md)] §1 p.867 L35-L53 [synthesis] - "Odlyzko and Wilf [1988] analyzed fountains of coins"; "their main result was that the bivariate generating function F(x, y) = n,k f n,k x n y k was the continued fraction" (1), `1/(1 − xy/(1 − x²y/(1 − x³y/⋯)))`, with `x` marking the coins and `y` the coins of the bottom row.
[^em-block]: [[endicott-may-shacklette-2018-stacks-of-spheres](pages/endicott-may-shacklette-2018-stacks-of-spheres.md)] §1 p.867 L59-L65 - "Wilf [2006, Example 2.12] also considered a restricted class of “block” fountains having the property that each row must be a contiguous block of coins. If bk is the number of block fountains with k coins in the bottom row, then B(y) = k bk y k turns out to be (1 − 2x)/(1 − 3x + x 2 ), which is the generating function for the Fibonacci numbers with odd indices."
[^exec]: Verified by execution (Python 3.11, 2026-10-29): `bin/python/brick_wall_castles.py`, run log `bin/python/brick_wall_castles-run.log`. Item [1], the shear of every brick-wall castle of width `w ≤ 10` onto the 1-histograms, a bijection keeping rows, height, blocks and cells, and their mirror images; [2], the counts by width, height and blocks for `w ≤ 16` against `C_w`, the Dyck paths by height and `N(w, k)`, and the column sweep against brute force for `w ≤ 10`; [3], the even-block counts against A071688 and the closed form for `w ≤ 16`; [4], the semi-perimeter grading against the peakless Motzkin paths for `s ≤ 16`; [5], the counts by cells and by cells and width against A005169 and the continued fraction for up to 18 cells; [6], Paule and Prodinger's quotient at `p = 2` against the 1-histograms by area; [7], the block fountains against `F_{2w−1}`, the generating function and the binomial sum for `w ≤ 14`; [9], the up-step levels of the Dyck paths for `w ≤ 12`; [10], the signed count for `w ≤ 16`; [11], the Euler castles for `w ≤ 10`; [12], the tables of `A_brick`, `A^e_brick` and `S_brick` for `h ≤ 6`, `w ≤ 14`, and the height-2 formulas for `w ≤ 24`.
