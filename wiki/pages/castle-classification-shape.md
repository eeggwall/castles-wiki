---
title: Castle classification - shape types
category: Concepts
summary: The 41 shape types of castles taken from the Castle Types source, 7 base types and 34 proposed ones, as predicates on the skyline (c_1, …, c_w), each with an example skyline, plus the ridge, hoodoo, monadnock, valley, k-valley, city-building and zig-zag types. Seven axes - convexity and modality, rate of change, path-like, symmetry, extremum, parity and area, value patterns - with the wiki page and the count of each type where one is known.
tags: [concept, castle, classification, taxonomy, skyline, geometric, unimodal, ferrers, dyck-path, motzkin-path, rainbow, hook, ridge-castle, hoodoo-castle, monadnock-castle, distinct-parts]
sources: [castle-classification, aocp-generating-partitions, cho-huh-nam-sohn-2022-bounded-free-motzkin-paths, project-euler-502-representations, oeis-encyclopedia]
created: 2026-09-19
updated: 2026-10-28
---

# Castle classification - shape types

A **shape type** is a predicate on the skyline `(c_1, …, c_w)` of one castle of width `w` and height `h` ([[castle-polyomino](pages/castle-polyomino.md)], and [[castle-classification](pages/castle-classification.md)] for the other kinds of type). Every castle is column-convex and has a full bottom row, so each type is a further restriction on the skyline.[^1] The Castle Types source lists 7 base types from the polyomino literature and 35 proposed types; this page groups 41 of them into seven axes, gives each a construction rule and an example skyline, and records the wiki page and the count where they exist. Six further types, the ridge, hoodoo, monadnock, valley, k-valley, city-building and zig-zag castles, are not among the 42 of the source.

## The 7 base types

The base types are polyomino and composition families:[^2]

| type | predicate | example | wiki page | count for castles |
|---|---|---|---|---|
| **Column-convex** | each column is one vertical run | `(1, 3, 2, 3, 1)` | [[column-convex-polyomino](pages/column-convex-polyomino.md)] | every castle; `A(w, h) = h^w − (h−1)^w` |
| **Unimodal** | `c_1 ≤ … ≤ c_p ≥ … ≥ c_w` for some `p` | `(1, 2, 3, 3, 2)` | [[convex-castle](pages/convex-castle.md)] | `C(2h + w − 3, w − 1)` ([[convex-castle-binomial-identity](pages/convex-castle-binomial-identity.md)]) |
| **Ferrers** | `c_1 ≥ c_2 ≥ … ≥ c_w` | `(3, 2, 2, 1)` | [[polyominoes](pages/polyominoes.md)], [[column-convex-polygon-enumeration](pages/column-convex-polygon-enumeration.md)] | `C(w + h − 2, w − 1)`, and by area `q^{h+w−1} [w + h − 2, w − 1]_q` |
| **Staircase** | Ferrers with all `c_i` distinct | `(4, 3, 1)` | [[polyominoes](pages/polyominoes.md)] | `C(h − 1, w − 1)` |
| **Parallelogram** | the cells on each line `i + j = const` form one run | `(1, 2, 2, 3)` | [[column-convex-polygon-enumeration](pages/column-convex-polygon-enumeration.md)] | open |
| **Directed** | every cell is reached from the bottom-left cell by steps east and north | `(1, 3, 2, 3, 1)` | [[polyominoes](pages/polyominoes.md)] | every castle |
| **m-disparate** | `\|c_{i+1} − c_i\| ≥ m` | `(1, 3, 1, 4)`, `m = 2` | | open |

A Ferrers castle has `c_1 = h`, and lowering the other `w − 1` columns by one leaves a partition in a `(w − 1) × (h − 1)` box, so the Ferrers castles number `C(w + h − 2, w − 1)`, with the area generating function from Cauchy's Theorem C ([[aocp-generating-partitions](pages/aocp-generating-partitions.md)]; checked for `w ≤ 6`, `h ≤ 5`). A staircase castle is a choice of `w − 1` distinct heights below `h`. Every castle is directed: walk east along row 1 to the column of the cell, then north up the column. Every weakly increasing skyline is a parallelogram castle, since `i + c_i` then increases with `i`, so the cells on the line `i + j = s` are those with `s − c_i < i ≤ s`, an interval; the skyline `(3, 1, 1)` is not one, since the line through its cells `(1, 3)` and `(3, 1)` misses the cell `(2, 2)`. The horizontal counterpart of m-disparate, a minimum width for the valleys between raised regions, is counted on [[tower-spacing-castles](pages/tower-spacing-castles.md)].

## The 34 proposed types, by axis

The proposed types fall into seven axes.[^3]

### Axis 1: Convexity and modality

Types 1 to 6, 30 and 31 restrict the local extrema of the skyline, and the hoodoo and monadnock types restrict how the steps change along each side of a unimodal skyline. The valley and k-valley types count the valleys, the pairs of columns `i < j − 1` with every column between them lower than both. A local maximum is a maximal run of equal columns higher than both neighbors, with height 0 outside the castle.

| type | predicate | example | wiki page and count |
|---|---|---|---|
| **Convex (row-convex)** | every row is one run | `(1, 2, 3, 3, 2)` | the unimodal castles ([[convex-castle](pages/convex-castle.md)]); their step words are on [[project-euler-502-representations](pages/project-euler-502-representations.md)] |
| **Reverse Ferrers** | `c_1 ≤ … ≤ c_w` | `(1, 2, 2, 3)` | the mirror images of the Ferrers castles; by width `x` and blocks `y`, `xy/(1 − x − y)` ([[deutsch-elizalde-2016-bargraphs-cornerless-motzkin](pages/deutsch-elizalde-2016-bargraphs-cornerless-motzkin.md)] §3.4) |
| **Strictly unimodal** | strictly increasing to one column, then strictly decreasing | `(1, 3, 4, 2)` | a subset of the unimodal castles; open |
| **Bimodal** | exactly two local maxima | `(1, 3, 1, 2, 1)` | open |
| **k-modal** | at most `k` local maxima | `(1, 2, 1, 3, 1, 2, 1)`, `k = 3` | open; `k = 1` is unimodal |
| **Vee (V-shaped)** | weakly decreasing, then weakly increasing | `(3, 1, 1, 2)` | the vee castles, by area `A332578` ([[castle-by-area](pages/castle-by-area.md)]) |
| **Convex-skyline** | `c_{i−1} − 2c_i + c_{i+1} ≥ 0` | `(3, 1, 1, 2)` | open; a subset of vee |
| **Concave-skyline** | `c_{i−1} − 2c_i + c_{i+1} ≤ 0` | `(1, 3, 4, 4, 3)` | open; a subset of unimodal |
| **Hoodoo** | unimodal; the rising steps strictly increase and the drops strictly decrease | `(2, 3, 6, 16, 35, 35, 25, 18, 14, 12)` | counted at every `(w, h)` (paragraph *Hoodoo and monadnock castles*) |
| **Monadnock** | unimodal; the rising steps strictly decrease and the drops strictly increase | `(2, 21, 31, 34, 35, 35, 33, 29, 22, 12)` | as many as hoodoo castles at every `(w, h)` (paragraph *Hoodoo and monadnock castles*) |
| **Valley** | exactly one valley: a flat floor between two walls `i < j − 1`, unimodal on each side, with the side of the lower wall falling away from the floor (`c_i ≥ c_j` and `c_j, …, c_w` weakly decreasing, or `c_i ≤ c_j` and `c_1, …, c_i` weakly increasing) | `(2, 1, 1, 3, 2)` | `(h − 1)² C(w + 2h − 3, 2h)`, with `blocks = h + depth` ([[valley-castles](pages/valley-castles.md)]) |
| **k-valley** | exactly `k` valleys | `(2, 1, 3, 3, 1, 1, 2)`, `k = 2` | `k = 0` is convex, `k = 1` is valley; `C(w + 1, 2k + 2)` at height 2 ([[valley-castles](pages/valley-castles.md)]) |

The unimodal and reverse Ferrers castles are counted by the [[convex-castle-binomial-identity](pages/convex-castle-binomial-identity.md)], the vee castles by area on [[castle-by-area](pages/castle-by-area.md)], and the hoodoo and monadnock castles in the paragraph *Hoodoo and monadnock castles*. The convex and vee castles are equinumerous in every `(w, h)` cell, by the **band reflection** `c_i ↦ max(c) + min(c) − c_i`. It keeps the tallest and the shortest column heights, so it maps the castles of width `w` and height `h` to themselves; it reverses the order of the heights, so it turns a skyline that falls weakly and then rises weakly into one that rises weakly and then falls weakly; and it is its own inverse. So it is a bijection from the vee castles onto the convex castles of each cell.[^11] It does not keep the area: the vee castle `(2, 1, 2)`, of area 5, goes to the convex castle `(1, 2, 1)`, of area 4, and by area the two families differ ([[q-thread-seminar](pages/q-thread-seminar.md)], Stop 2).

**Convexity fixes the block count.** A convex castle of height `h` has exactly `h` blocks, one per row, and the convex castles are exactly the castles of height `h` with `h` blocks, the fewest possible ([[convex-castle](pages/convex-castle.md)], section *Block count*).[^4] So the convex castles all have an even number of blocks when `h` is even and an odd number when `h` is odd.

**Hoodoo and monadnock castles.** A hoodoo or monadnock castle has height `h ≥ 2` and three parts, read left to right: a **rising side** of at least one column below `h`, a **summit** of one or more columns of height `h`, and a **falling side** of at least one column below `h`. The steps of a side are the height changes `c_{i+1} − c_i` from its first column up to the summit, or from the summit down to its last column. The step onto the summit and the step off it belong to their sides, every step on a side is nonzero, and the only zero steps are inside the summit. [[hoodoo-monadnock-castles](pages/hoodoo-monadnock-castles.md)] gives the generation by the Hindenburg algorithm, the side counts, and growth.

- **Hoodoo castle.** The rising steps strictly increase and the drops strictly decrease, so each side is discrete-convex. In the example, of height 35 and width 10, the rising steps are `1, 3, 10, 19` and the drops `10, 7, 4, 2`.
- **Monadnock castle.** The rising steps strictly decrease and the drops strictly increase, so the whole skyline is discrete-concave. In the example, of height 35 and width 10, the rising steps are `19, 10, 3, 1` and the drops `2, 4, 7, 10`.
- **Relation to the convex-skyline and concave-skyline types.** A convex-skyline castle is a vee castle, while a hoodoo is discrete-convex on each side but not at the summit. The monadnock castles are the concave-skyline castles with both sides present and strictly monotone steps.
- **Sides are partitions into distinct parts.** The steps of one side are distinct positive integers, and their sum is `h` minus the height of the side's outer column, a number from 1 to `h − 1`. Read as a set, a side is a partition into distinct parts of an integer in `1, …, h − 1`, and each such partition gives exactly one hoodoo side (steps in increasing order) and one monadnock side (decreasing order). A side with `m` steps needs a rise of at least `1 + 2 + ⋯ + m = m(m+1)/2`, so a side has at most 1 column at `h = 2, 3`, 2 at `h = 4, …, 6`, and 3 at `h = 7, …, 10`.
- **Step reversal.** Reversing the order of the steps on each side turns a hoodoo castle into a monadnock castle with the same `w`, `h`, end columns, side lengths and summit length; the two examples are such a pair. The hoodoo castle has the smaller area, 166 against 254 in the example, since its sides lie below the chord between their ends and the monadnock's above it.
- **Count.** The two sides are chosen independently and the summit takes the remaining width, so the count at width `w` is the number of ordered pairs of partitions into distinct parts, of integers in `1, …, h − 1`, whose numbers of parts add to at most `w − 1`. By width `w = 3, 4, 5, …`, the hoodoo castles, and equally the monadnock castles, number:

```
h = 2:   1,   1,   1, …
h = 3:   4,   4,   4, …
h = 4:   9,  15,  16,  16, …
h = 5:  16,  32,  36,  36, …
h = 6:  25,  65,  81,  81, …
h = 7:  36, 108, 156, 168, 169, 169, …
```

  Every entry agrees with brute-force enumeration, which also confirms the step-reversal bijection.[^5] At `w = 3` the count is `(h − 1)²`, one column on each side. Once `w` exceeds twice the longest possible side, every pair of sides fits and the count is constant: the square of the number of partitions into distinct parts of the integers `1, …, h − 1`, that is, of the sum of `A000009` over `1, …, h − 1`.[^6] By `h = 2, 3, …, 15`: `1, 4, 16, 36, 81, 169, 324, 576, 1024, 1764, 2916, 4761, 7569, 11881`.
- **Growth.** By width at fixed `h` the count is eventually constant. By height, the eventual count grows like the square of a sum of distinct-part partition numbers, slower than any exponential.
- **Blocks.** Both families are unimodal, so every member has `h` blocks: all are even-block castles when `h` is even, and none when `h` is odd.

### Axis 2: Rate of change

Types 7, 8 and 9, the base type m-disparate, the ridge type and the zig-zag type:

| type | predicate | example | wiki page and count |
|---|---|---|---|
| **Plateau-free** | `c_i ≠ c_{i+1}` | `(1, 3, 2, 3, 1)` | the skylines in `{1, …, h}^w` number `h(h−1)^{w−1}`, so the castles number `h(h−1)^{w−1} − (h−1)(h−2)^{w−1}`, growth `h − 1` by width |
| **Ridge** | `c_i ≠ c_{i+1}` unless `c_i = c_{i+1} = h` | `(3, 1, 3, 4, 4, 1, 4, 4, 1, 4, 2, 1)` | `𝟙ᵀ R_h^{w−1} 𝟙 − (h−1)(h−2)^{w−1}`, growth `δ_{h−1}` by width (paragraph *Ridge castles*) |
| **m-smooth** | `\|c_{i+1} − c_i\| ≤ m` | `(1, 2, 2, 3, 2)`, `m = 1` | [[1-smooth-castles](pages/1-smooth-castles.md)], [[m-smooth-castles](pages/m-smooth-castles.md)] |
| **Zig-zag** | `\|c_{i+1} − c_i\| = 1`: the 1-smooth and plateau-free predicates together | `(1, 2, 3, 2)` | [[zig-zag-castles](pages/zig-zag-castles.md)]: their step bits are the `(h − 1)`-balanced strings of length `w − 1`, A027383, A027557, A027559, A027560 at `h = 3, …, 6`; growth `2cos(π/(h+1))` by width, golden by width at `h = 4` |
| **Zigzag** | the differences `c_{i+1} − c_i` alternate in sign | `(1, 3, 2, 3, 1)` | open; not the zig-zag type of the row above, whose differences are all `±1` |
| **m-disparate** | `\|c_{i+1} − c_i\| ≥ m` | `(1, 3, 1, 4)`, `m = 2` | open |

**m-smooth castles.** At `m = 1` the predicate is the Motzkin-path predicate of the path-like types (Axis 3) without its condition on the end columns. The 1-smooth strips on the heights `{1, 2, 3}`, which need not reach height 3 and so are strips, not castles, number `A001333(w + 1)` and are silver by width ([[metallic-strip-realizability](pages/metallic-strip-realizability.md)]); with first column at height 1 they number the Pell numbers `P⋆_w`, and those that reach height 3 are the Pell castles ([[pell-castle-strip](pages/pell-castle-strip.md)], [[pell-castle](pages/pell-castle.md)]). At every height `h`, the 1-smooth castles with first column at height 1 have the generating function `x^h/(η_h η_{h−1})` and are column `h − 1` of `A283595`, the Motzkin prefixes by length and height ([[1-smooth-castles](pages/1-smooth-castles.md)]). They are Motzkin paths only when the last column also has height 1. The m-smooth castles for `m ≥ 2` are on [[m-smooth-castles](pages/m-smooth-castles.md)]: the smallest width is `⌈(h − 1)/m⌉ + 1`, the recurrence in `w` has order at most `h`, and at `h ≤ m + 1` every castle is m-smooth.

The tower words of [[tower-word-continued-fraction](pages/tower-word-continued-fraction.md)], `A004149`, are a different object: Motzkin paths with no factor `UD` or `DU`, counted by word length, which are the words of towers of any height.

**Ridge castles.** A **ridge castle** of height `h` ([[ridge-castle](pages/ridge-castle.md)]) has neighboring columns of different heights unless both have height `h`. So equal neighbors occur only at height `h`; below it the skyline steps up or down at every column, and all heights `1, …, h` may occur. To build one, pick `c_1`, give each next column any height other than the current one, or `h` again when the current one is `h`, and keep the skylines in which some column reaches `h`. The example has height 4 and width 12.

- **Transfer matrix.** `R_h = J − D`, with `J` the `h × h` all-ones matrix and `D = diag(1, …, 1, 0)`: entry `(a, b)` is 1 when `a ≠ b` or `a = b = h`. Its characteristic polynomial is `(x + 1)^{h−2}(x² − (h − 1)x − 1)`.
- **Count.** `𝟙ᵀ R_h^{w−1} 𝟙 − (h−1)(h−2)^{w−1}` ridge castles of width `w` and height `h`; the subtracted term counts the plateau-free skylines that do not reach `h`. By width `w = 1, …, 7`: `1, 3, 5, 8, 13, 21, 34` at `h = 2`; `1, 5, 15, 39, 97, 237, 575` at `h = 3`; `1, 7, 31, 118, 421, 1453, 4924` at `h = 4`. Every entry agrees with brute-force enumeration for `w ≤ 6`.[^5]
- **Growth.** Like `δ_{h−1}^w` ([[metallic-means](pages/metallic-means.md)]): golden at `h = 2`, silver at `h = 3`, bronze at `h = 4`, `δ_4` at `h = 5`, `δ_5` at `h = 6` ([[metallic-strip-realizability](pages/metallic-strip-realizability.md)]).
- **Fibonacci castles.** At `h = 2` the rule forbids two neighboring columns of height 1. Exchanging the heights 1 and 2 turns a ridge castle of height 2 into a skyline with no two neighboring 2s: a **Fibonacci castle**, a castle of height 2 with no two neighboring columns of height 2, which is the tree castle of height 2 of [[castle-graph](pages/castle-graph.md)] ([[fibonacci-castle](pages/fibonacci-castle.md)]); or the all-1 row, which comes from the all-2 castle. So for `w ≥ 2` there are `F_{w+2}` ridge castles of height 2 and `F_{w+2} − 1` Fibonacci castles. Counted with `q` marking area, the Fibonacci castles are the q-Fibonacci castles ([[q-fibonacci-castle](pages/q-fibonacci-castle.md)]). Conditions on the row of height-2 columns give sub-families: the Fibonacci-word castles (`w + 1` from `w = 3`), the balanced castles (`A005598(w)/2`), the maximal castles (Padovan), the spaced castles (Narayana's cows) and the `(d, k)`-RLL castles ([[fibonacci-castles-sub-families](pages/fibonacci-castles-sub-families.md)]).
- **Not crenellated.** The crenellated type of the value patterns (Axis 7) alternates between two heights, `(a, h, a, h, …)`; ridge castles may use every height and may repeat `h`.
- **Code.** `ridge_R`, `ridge_count` (strip counts) and `proper_even` (even-block ridge castles) on [[castle-snippets-strips](pages/castle-snippets-strips.md)].

### Axis 3: Path-like types

Types 13 and 14 identify the skyline with a lattice path:

| type | predicate | example | wiki page |
|---|---|---|---|
| **Dyck-path** | `c_1 = c_w = 1`, `\|c_{i+1} − c_i\| = 1` | `(1, 2, 1, 2, 3, 2, 1)` | [[dyck-words](pages/dyck-words.md)], [[catalan-numbers](pages/catalan-numbers.md)]; the zig-zag castles with both end columns at height 1 ([[zig-zag-castles](pages/zig-zag-castles.md)]) |
| **Motzkin-path** | `c_1 = c_w = 1`, `\|c_{i+1} − c_i\| ≤ 1` | `(1, 2, 2, 3, 2, 1)` | [[motzkin-numbers](pages/motzkin-numbers.md)]; without the condition on the end columns, the 1-smooth type of the rate-of-change types (Axis 2) |

**The counts carry a condition on the ends and on the height.** Lowering every column by one turns a Dyck-path castle into a Dyck path of `w − 1` steps, so `w` is odd and the semilength is `n = (w − 1)/2`; since the castle has height `h`, the path has height `h − 1`. The Catalan number `C_n` counts the Dyck-path castles only after summing over `h`. At fixed `(w, h)` the count is the triangle `A080936`, the Dyck paths of semilength `n` and height `k = h − 1`,[^7] and at height at most `h` it is `A080934`, whose generating function is a ratio of Chebyshev-type polynomials.[^8] In the same way, at fixed `(w, h)` the Motzkin-path castles are `A097862`, the Motzkin paths of length `n = w − 1` and height `k = h − 1`,[^9] and only the sum over `h` is the Motzkin number `M_{w−1}`. Every entry of the tables agrees with brute-force enumeration:[^5]

```
Dyck-path castles, rows w = 1, 3, 5, 7, 9, columns h = 1..5, then the row sum
w=1:  1 . . . .   1
w=3:  . 1 . . .   1
w=5:  . 1 1 . .   2
w=7:  . 1 3 1 .   5        (A080936 row n=3: 1, 3, 1)
w=9:  . 1 7 5 1   14       (A080936 row n=4: 1, 7, 5, 1)

Motzkin-path castles, rows w = 1..9, columns h = 1..5, then the row sum
w=1:  1 .   .   .  .   1
w=2:  1 .   .   .  .   1
w=3:  1 1   .   .  .   2
w=4:  1 3   .   .  .   4
w=5:  1 7   1   .  .   9
w=6:  1 15  5   .  .   21
w=7:  1 31  18  1  .   51      (A097862 row n=6: 1, 31, 18, 1)
w=8:  1 63  56  7  .   127
w=9:  1 127 161 33 1   323     (A097862 row n=8: 1, 127, 161, 33, 1)
```

The `h = 2` Motzkin column is `2^{w−2} − 1`: a Motzkin-path castle of height 2 is a nonempty set of raised interior columns. The `h = 2` Dyck column is 1: the only Dyck-path castle of height 2 at odd `w` is the skyline `(1, 2, 1, 2, …, 1)`. The predicates are `is_dyck_path` and `is_motzkin_path` on [[castle-snippets](pages/castle-snippets.md)].

### Axis 4: Symmetry

Types 11, 12 and 21:

| type | predicate | example | wiki page and count |
|---|---|---|---|
| **Palindromic** | `c_i = c_{w+1−i}` | `(1, 3, 2, 3, 1)` | by width and blocks, the symmetric-bargraph generating function of [[deutsch-elizalde-2016-bargraphs-cornerless-motzkin](pages/deutsch-elizalde-2016-bargraphs-cornerless-motzkin.md)] §4.1, and over all heights the closed sum of [[cho-huh-nam-sohn-2022-bounded-free-motzkin-paths](pages/cho-huh-nam-sohn-2022-bounded-free-motzkin-paths.md)] for `T̂_pal(w, b − 1)`, the number of palindromic towers on a base of length `w` with `b − 1` blocks, which counts the palindromic castles of width `w` with `b` blocks[^10]; by semi-perimeter `A273905`, `1, 2, 3, 5, 9, 15, 27, 46, 83, …`; at fixed `(w, h)`, `h^{⌈w/2⌉} − (h−1)^{⌈w/2⌉}`, of which `⌊h/2⌋·h^{⌈w/2⌉−1} − ⌊(h−1)/2⌋·(h−1)^{⌈w/2⌉−1}` are even-block, since a palindrome has the parity of its middle column; this decides the parity of `A^e(w, h)` ([[mod-p-observatory](pages/mod-p-observatory.md)], section *Modulo 2*)[^12] |
| **Centrally symmetric** | `c_i + c_{w+1−i} = h + 1` | `(1, 2, 3)` | open |
| **Self-conjugate** | `c_i = #{j : c_j ≥ i}` | `(3, 2, 1)` | open; requires `w = h` |

A self-conjugate skyline is a partition equal to its conjugate, so it is weakly decreasing with `c_1 = w`, and `c_1 = h`.

### Axis 5: Extremum constraints

Types 15, 16, 24, 25, 26 and 35:

| type | predicate | example | wiki page and count |
|---|---|---|---|
| **Flat-top** | `h` occurs in two neighboring columns | `(1, 3, 3, 2)` | open |
| **Single-summit** | `h` occurs in exactly one column | `(1, 3, 2, 2)` | open |
| **Twin-peak** | `h` occurs in exactly two columns | `(3, 1, 3)` | open |
| **Rainbow** | `w = h`, and the heights are a permutation of `{1, …, h}` | `(2, 3, 1)` | `h!` castles ([[aocp-permutations](pages/aocp-permutations.md)]); by inversions of the skyline, the Mahonian numbers `A008302` ([[aocp-combinatorics](pages/aocp-combinatorics.md)]) |
| **Boxcastle** | `c_i = h` for all `i` | `(2, 2, 2)` | 1 |
| **Hook** | `c_1 = h`, `c_i = 1` for `i ≥ 2` | `(3, 1, 1, 1)` | 1 at every `(w, h)`, since the predicate fixes every column |

The rainbow castles correspond to the permutations of `{1, …, h}`, so the cycle count, the Foata transform and the streak factorization of [[castles-as-upgraded-cycle-count](pages/castles-as-upgraded-cycle-count.md)] apply to them ([[permutation-cycle-castle-analogy](pages/permutation-cycle-castle-analogy.md)]).

### Axis 6: Parity and area

Types 10, 17, 18 and 32:

| type | predicate | example | wiki page and count |
|---|---|---|---|
| **Alternating parity** | consecutive `c_i` have opposite parity | `(1, 2, 3, 4)` | open |
| **Even-area** | `Σ c_i ≡ 0 (mod 2)` | `(1, 3, 2)` | counted by area, with its parity split, on [[castle-by-area](pages/castle-by-area.md)] |
| **Even-peak** | the number of local maxima is even | `(1, 3, 1, 2, 1)` | open |
| **Triangular-area** | `Σ c_i = n(n+1)/2` for some `n` | `(1, 2, 3)` | open |

The even-peak condition is a parity of the number of local maxima, not of the block count `blocks(c)` of [[castle-sign](pages/castle-sign.md)]. The peaks of [[castle-foata-transform](pages/castle-foata-transform.md)] are a third statistic, the maximal runs of columns of height at least 2: the skyline `(2, 3, 2, 3, 2)` has one such run and two local maxima.

### Axis 7: Value patterns

Types 19, 20, 22, 23, 28, 29, 33 and 34, and the city-building type:

| type | predicate | example | wiki page and count |
|---|---|---|---|
| **Equal-block** | all blocks have the same length | `(2, 2, 2)` | open |
| **Two-level** | exactly two distinct heights | `(1, 2, 2, 1, 2)` | at `h = 2`, every castle but the skyline `(2, …, 2)`: `2^w − 2`; the Fibonacci castles ([[castle-graph](pages/castle-graph.md)]) are a subset |
| **Crenellated** | `c_i ∈ {a, h}` and `c_i ≠ c_{i+1}`: `(a, h, a, h, …)` | `(2, 4, 2, 4)` | open; at even width its discrete Fourier transform is supported on the frequencies `0` and `w/2` ([[spectral-analysis](pages/spectral-analysis.md)]) |
| **Moated** | `c_1 = c_w = 1`, and every other `c_i ≥ 2` | `(1, 2, 3, 2, 1)` | open |
| **Fence-post** | `c_i = 1` for every even `i` | `(3, 1, 2, 1, 3)` | open |
| **Linear** | `c_i = a + (i − 1)d` | `(1, 3, 5)` | `2⌊(h−1)/(w−1)⌋ + 1` castles for `w ≥ 2` |
| **Prime-top** | `h` is prime | `(1, 3, 2)` | every castle of prime height |
| **Integer-mean** | `w` divides `Σ c_i` | `(1, 3, 2)` | open |
| **City-building** | with the ground `c_0 = 0` in front, every column sees exactly `c_j` of the columns `0, …, j − 1`, a top seeing an earlier one when every top between is on or below the segment joining them (the rule of the city-building sequence A400000) | `(1, 1, 2, 1, 2, 2, 1)` | finitely many at each height, `2, 12, 600, 965952, 31776964193520` for `h = 1, …, 5`; the prefixes of A400000 are members ([[city-building-castles](pages/city-building-castles.md)]) |

For `w ≥ 2`, a linear castle with `d = 0` is the boxcastle; one with `d > 0` has `c_w = h` and `c_1 = h − (w − 1)d ≥ 1`, so `d ≤ (h − 1)/(w − 1)`, and `d < 0` is its mirror image. So the linear castles number `2⌊(h−1)/(w−1)⌋ + 1`, which agrees with brute-force enumeration for `2 ≤ w ≤ 6`, `h ≤ 8`.[^5]

## Related Concepts

- [[castle-classification](pages/castle-classification.md)] - the classification as a whole, and the kinds of type that are not shape types.
- [[castle-classification-spectrum](pages/castle-classification-spectrum.md)] - types by the spectrum of the castle graph; [[castle-classification-growth](pages/castle-classification-growth.md)] - families by growth.
- [[castle-polyomino](pages/castle-polyomino.md)], [[castle-representations](pages/castle-representations.md)] - the castle and the skyline encoding the predicates read.
- [[convex-castle](pages/convex-castle.md)], [[convex-castle-binomial-identity](pages/convex-castle-binomial-identity.md)] - the unimodal castles and their count.
- [[polyominoes](pages/polyominoes.md)], [[column-convex-polyomino](pages/column-convex-polyomino.md)], [[column-convex-polygon-enumeration](pages/column-convex-polygon-enumeration.md)] - the polyomino families of the base types.
- [[stack-polyomino-gf](pages/stack-polyomino-gf.md)] - the unimodal skylines counted by area, Analytic Combinatorics Exercise I.8.
- [[dyck-words](pages/dyck-words.md)], [[motzkin-numbers](pages/motzkin-numbers.md)], [[tower-word-continued-fraction](pages/tower-word-continued-fraction.md)] - the path-like types and the tower words.
- [[castle-by-area](pages/castle-by-area.md)] - the even-area and vee castles counted by area.
- [[castle-sign](pages/castle-sign.md)], [[castle-foata-transform](pages/castle-foata-transform.md)] - the block count and the peaks.
- [[castles-as-upgraded-cycle-count](pages/castles-as-upgraded-cycle-count.md)] - the permutation constructions that apply to rainbow castles.
- [[castle-snippets](pages/castle-snippets.md)] - Python predicates for the types on this page.
- [[hoodoo-monadnock-castles](pages/hoodoo-monadnock-castles.md)] - the hoodoo and monadnock castles in full.
- [[aocp-permutations](pages/aocp-permutations.md)], [[aocp-combinatorics](pages/aocp-combinatorics.md)] - the count `h!` of the rainbow castles and its grading by inversions.
- [[castle-compression](pages/castle-compression.md)] - how short a description of a castle can be.
- [[tower-parity-sectors](pages/tower-parity-sectors.md)] - for `k ≡ 2 (mod 4)` the even sector of `P(k, L)` is `2^L` times a Hardin word count (`A005251`, `A202882`, `A203094`, `A203184`); the case `g = 2` of [[tower-spacing-castles](pages/tower-spacing-castles.md)] reaches the same words.

## Footnotes

[^1]: raw/castle-types.wiki L3-9 - "A castle on a w × h grid is determined by its skyline, the sequence of column heights c_1, c_2, …, c_w with 1 ≤ c_i ≤ h and max_i c_i = h. (Problem 502 also requires an even number of blocks; the types below mostly ignore, or independently re-impose, that parity rule.) Every castle is automatically column-convex and bottom-aligned, so each type is a further restriction on the skyline." (Source: https://charlesreid1.com/wiki/Project_Euler/502/Castle_Types, fetched 2026-09-15.)
[^2]: raw/castle-types.wiki §"Base types" L11-19 [synthesis] - the 7 base types: column-convex, unimodal (`c_1 ≤ … ≤ c_p ≥ … ≥ c_w`), directed (every cell reachable from the bottom-left base cell by an east/north path), parallelogram (the intersection with every line perpendicular to the main diagonal is a connected segment), Ferrers (`c_1 ≥ … ≥ c_w`), staircase (a Ferrers castle whose column heights are all distinct), m-disparate (`|c_{i+1} − c_i| ≥ m`).
[^3]: raw/castle-types.wiki §"Proposed additional types" L21-57 [synthesis] - the 35 proposed types, numbered 1 to 35: convex (row-convex), reverse Ferrers, strictly unimodal, bimodal, k-modal, anti-unimodal (V-shaped), plateau-free, m-smooth (Lipschitz), zigzag, alternating parity, palindromic, centrally symmetric, Dyck-path, Motzkin-path, flat-top, single-summit, even-area, even-peak, equal-block, two-level, self-conjugate, crenellated, moated, rainbow, hook, twin-peak, single-valley, fence-post, linear, convex-skyline, concave-skyline, triangular-area, prime-top, integer-mean, boxcastle.
[^4]: [[project-euler-502-representations](pages/project-euler-502-representations.md)] §"Steps-Based Approach" L88-90, §"The tower word" L229, §"Step 1 Bare Minimum String" L153 [synthesis] - the word of a convex castle has a front of `U` and `R` steps with "No D steps" and a back of `D` and `R` steps with "No U steps", so it has one `U` per row; "blocks in the tower = number of D's = number of U's"; and "The bare minimum string consists of the minimum number of Us and Ds that the castle is required to have", `h` of each at height `h`. Verified by execution (Python 3.11, 2026-10-25): every skyline of height `h` has at least `h` blocks, with equality exactly when it is unimodal, for `w ≤ 8`, `h ≤ 6` with `h^w ≤ 400000`.
[^5]: Verified by execution (Python 3.11, 2026-10-16): every example skyline against its predicate; the hoodoo and monadnock counts for `h ≤ 7` and `w ≤ 8` (`h^w ≤ 6·10^6`), equal for the two families; the eventual counts as squares of partial sums of `A000009`; the ridge counts for `h ≤ 4`, `w ≤ 6` against `𝟙ᵀ R_h^{w−1} 𝟙 − (h−1)(h−2)^{w−1}`; the plateau-free count, the Ferrers count and its area generating function, and the staircase count for `w ≤ 6`, `h ≤ 5`; the two-level count at `h = 2` for `w ≤ 6`; the Dyck-path and Motzkin-path tables; the palindromic castles by semi-perimeter to 10; the linear count for `2 ≤ w ≤ 6`, `h ≤ 8`; the parallelogram condition for every weakly increasing skyline with `w ≤ 5`, `h ≤ 4`; every castle with `w ≤ 5`, `h ≤ 4` directed.
[^6]: https://oeis.org/A000009 - "Expansion of Product_{m >= 1} (1 + x^m); number of partitions of n into distinct parts; number of partitions of n into odd parts"; data begins 1, 1, 1, 2, 2, 3, 4, 5, 6, 8, 10, 12, 15, 18.
[^7]: https://oeis.org/A080936 (read 2026-10-16) - "Triangle read by rows: T(n,k) is the number of Dyck paths of semilength n and height k (1 <= k <= n)"; data begins 1; 1, 1; 1, 3, 1; 1, 7, 5, 1; 1, 15, 18, 7, 1.
[^8]: https://oeis.org/A080934 (read 2026-10-16) - "Square array read by antidiagonals of number of Catalan paths (nonnegative, starting and ending at 0, step +-1) of 2n steps with all values less than or equal to k".
[^9]: https://oeis.org/A097862 (read 2026-10-16) - "Triangle read by rows: T(n,k) is the number of Motzkin paths of length n and height k (n>=0, k>=0)"; data begins 1; 1; 1, 1; 1, 3; 1, 7, 1; 1, 15, 5; 1, 31, 18, 1.
[^10]: [[cho-huh-nam-sohn-2022-bounded-free-motzkin-paths](pages/cho-huh-nam-sohn-2022-bounded-free-motzkin-paths.md)] p.17 Proposition 3.8 L965-974 [synthesis] - `scc(t, m)`, the number of self-conjugate `t`-cores with `m` corners, which Theorem 3.7 puts in bijection with the cornerless symmetric Motzkin paths with `t − 1` flat steps, the tower words of the palindromic towers on a base of length `t − 1` with `m` blocks; so the palindromic castles of width `w` with `b` blocks number `T̂_pal(w, b − 1) = scc(w + 1, b − 1)` (checked by enumeration in `bin/python/bounded_t_cores.py`, run log `bin/python/bounded_t_cores-run.log`).
[^11]: Verified by execution (Python 3.10, 2026-10-28): the band reflection maps the vee castles of width `w` and height `h` one-to-one onto the convex castles of the same cell, in all 42 cells with `w ≤ 7`, `h ≤ 6` and `h^w ≤ 300000`.
[^12]: Verified by execution (Python 3.10, 2026-10-28): `bin/python/even_count_parity.py` item [2], run log `bin/python/even_count_parity-run.log`. For every castle with `h ≤ 5`, `w ≤ 7` and `h^w ≤ 200000`: the palindromic castles number `h^{⌈w/2⌉} − (h−1)^{⌈w/2⌉}`, a palindrome's block count has the parity of its middle column, and the even-block palindromes number `⌊h/2⌋·h^{⌈w/2⌉−1} − ⌊(h−1)/2⌋·(h−1)^{⌈w/2⌉−1}`.
