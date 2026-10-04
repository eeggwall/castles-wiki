---
title: Castle classification - shape types
category: Concepts
summary: The 42 shape-based castle types as skyline predicates on individual castles, plus the wiki-named ridge, hoodoo, and monadnock types. Seven axes: convexity/modality, rate of change, path-like, symmetry, extremum, parity/area, value patterns. Each type gets its wiki home and count status.
tags: [concept, castle, classification, taxonomy, skyline, geometric, unimodal, ferrers, dyck-path, motzkin-path, rainbow, hook, ridge-castle, hoodoo-castle, monadnock-castle, distinct-parts]
sources: [castle-classification, aocp-generating-partitions]
created: 2026-09-19
updated: 2026-10-04
---

# Castle classification - shape types

A **geometric** castle type is a predicate on the shape of one castle, read off its skyline `(c_1, …, c_w)` ([[castle-classification](pages/castle-classification.md)] for the framing, [[castle-polyomino](pages/castle-polyomino.md)] for the object). Every castle is column-convex and bottom-aligned already, so each type below is a further restriction on the skyline.[^1] This page is the catalogue: the 7 base types from the polyomino literature and the 35 proposed types, grouped into seven structural axes, each tied to the wiki thread that already touches it and marked as counted, candidate, or open. The non-geometric techniques (growth type of a class, spectrum of the castle graph, description length) are on [[castle-classification](pages/castle-classification.md)].

## The base 7 types and their wiki homes

The base types are all standard polyomino / composition families. Each corresponds to an existing wiki thread:[^2]

| Type | Definition (skyline predicate) | Wiki home | Count status |
|---|---|---|---|
| **Column-convex** | (automatic for castles) | [[column-convex-polyomino](pages/column-convex-polyomino.md)] | matches all castles; `A(w,h) = h^w − (h−1)^w` |
| **Unimodal** | `c_1 ≤ … ≤ c_p ≥ … ≥ c_w` | [[convex-castle](pages/convex-castle.md)] | `C(2h+w−3, w−1)` via [[convex-castle-binomial-identity](pages/convex-castle-binomial-identity.md)] |
| **Ferrers** | `c_1 ≥ c_2 ≥ … ≥ c_w` (weakly decreasing) | [[polyominoes](pages/polyominoes.md)], [[column-convex-polygon-enumeration](pages/column-convex-polygon-enumeration.md)] | classical; by area = partition GF; q-Catalan / q-Bessel refinement; in a fixed `(w, h)` cell, `C(w + h − 2, w − 1)` castles, by area `q^{h+w−1} [w + h − 2, w − 1]_q` (lower the last `w − 1` columns by one: a partition in a `(w − 1) × (h − 1)` box, Cauchy's Theorem C in [[aocp-generating-partitions](pages/aocp-generating-partitions.md)]; checked for `w ≤ 6`, `h ≤ 5`) |
| **Staircase** | Ferrers with all `c_i` distinct | [[polyominoes](pages/polyominoes.md)] | classical (distinct-parts partitions) |
| **Parallelogram** | anti-diagonal sections connected | [[column-convex-polygon-enumeration](pages/column-convex-polygon-enumeration.md)] | classical (Bousquet-Mélou) |
| **Directed** | every cell reachable from `(1,1)` by east/north | [[polyominoes](pages/polyominoes.md)] | classical (directed polyominoes) |
| **m-disparate** | `|c_{i+1} − c_i| ≥ m` for all `i` | no wiki page | open |

The first 6 rows tie the castle taxonomy directly to the polyomino literature. **m-disparate** is the one base type without a wiki page; its horizontal-gap counterpart is counted on [[tower-spacing-castles](pages/tower-spacing-castles.md)].

## The 35 proposed types, grouped by structural axis

The proposed types cluster into seven structural axes, some of which the wiki has counts for.[^3]

### Axis 1: Convexity / modality

Types 1-6 and 30-31 restrict the shape of the skyline's local extrema, and the wiki-named hoodoo and monadnock types restrict how the steps change along each side of a unimodal skyline:

| Type | Predicate | Wiki tie |
|---|---|---|
| **Convex (row-convex)** | every row is one contiguous run | equals unimodal for castles ([[convex-castle](pages/convex-castle.md)]); front/middle/back U/R/D form on [[project-euler-502-representations](pages/project-euler-502-representations.md)] |
| **Reverse Ferrers** | `c_1 ≤ … ≤ c_w` (weakly increasing) | Ferrers's mirror; same count by symmetry; by width `x` and blocks `y` the GF is `xy/(1 − x − y)` ([[deutsch-elizalde-2016-bargraphs-cornerless-motzkin](pages/deutsch-elizalde-2016-bargraphs-cornerless-motzkin.md)] §3.4, checked by brute force) |
| **Strictly unimodal** | strict rise, one peak, strict fall | strengthens unimodal; count is a sub-count of [[convex-castle](pages/convex-castle.md)] |
| **Bimodal** | exactly two local maxima | *open* |
| **k-modal** | at most `k` local maxima | *open* - unimodal is `k=1`; parameterized family |
| **Anti-unimodal (V-shaped)** | weakly decrease then weakly increase | the "valley" family; on [[castle-by-area](pages/castle-by-area.md)] as valley castles, area-OEIS A332578; the [[convex-castle-binomial-identity](pages/convex-castle-binomial-identity.md)] valley bijection is an open thread |
| **Convex-skyline** | `c_{i−1} − 2c_i + c_{i+1} ≥ 0` (discrete convex) | *open* - a stronger sub-family of anti-unimodal |
| **Concave-skyline** | `c_{i−1} − 2c_i + c_{i+1} ≤ 0` (discrete concave) | *open* - a stronger sub-family of unimodal; the monadnock type is its strict sub-family with both sides present |
| **Hoodoo** (wiki-named, not one of the 35) | unimodal; rising steps strictly increase, falling drops strictly decrease | counted at every `(w, h)` by distinct-part partitions; see **Hoodoo and monadnock castles** below |
| **Monadnock** (wiki-named, not one of the 35) | unimodal; rising steps strictly decrease, falling drops strictly increase | equinumerous with hoodoo castles in every `(w, h)` cell, by step reversal; see below |

**Where the wiki already has counts:** unimodal and (by symmetry) reverse Ferrers, via the [[convex-castle-binomial-identity](pages/convex-castle-binomial-identity.md)]; anti-unimodal (valley) by area on [[castle-by-area](pages/castle-by-area.md)]; hoodoo and monadnock by `(w, h)` (below). **Open:** an explicit convex ⟺ valley bijection (the two classes are equinumerous in every `(w, h)` cell).

**Hoodoo and monadnock castles.** Generation by the Hindenburg algorithm, the side counts, and growth on all three axes are on [[hoodoo-monadnock-castles](pages/hoodoo-monadnock-castles.md)]. Both are castles of exact height `h ≥ 2` with three parts, read left to right: a **rising side** of at least one column below `h`, a **summit** of one or more columns of height `h`, and a **falling side** of at least one column below `h`. A side's steps are the height changes `c_{i+1} − c_i` from its first column up to the summit (rising side) or from the summit down to its last column (falling side). The step onto the summit and the step off it belong to their sides, every step on a side is nonzero, and the only zero steps are inside the summit.

- **Hoodoo castle.** The rising steps strictly increase and the falling drops strictly decrease in size: the skyline climbs faster and faster, then falls steeply and levels off. Each side is discrete-convex, with one concave bend at the summit. Example, `h = 35`, `w = 10`: `(2, 3, 6, 16, 35, 35, 25, 18, 14, 12)`, with rising steps `1, 3, 10, 19` and drops `10, 7, 4, 2`.
- **Monadnock castle.** The rising steps strictly decrease and the falling drops strictly increase: the skyline climbs fast and slows into the summit, then falls slowly and steepens. The whole skyline is discrete-concave. Example, `h = 35`, `w = 10`: `(2, 21, 31, 34, 35, 35, 33, 29, 22, 12)`, with rising steps `19, 10, 3, 1` and drops `2, 4, 7, 10`.
- **Not the convex-skyline type.** Convex-skyline (`c_{i−1} − 2c_i + c_{i+1} ≥ 0` everywhere) forces a valley; a hoodoo is convex on each side but not at the summit. The monadnock type is the strict, two-sided part of concave-skyline: dropping strictness (equal consecutive steps allowed) gives concave-skyline castles with both sides present.
- **Sides are distinct-part partitions.** The steps of one side are distinct positive integers, and their sum is `h` minus the side's outer column, a number from `1` to `h − 1`. Read as a set, a side is a partition into distinct parts of an integer in `1, …, h − 1`, and conversely each such partition gives exactly one hoodoo side (steps in increasing order) and one monadnock side (decreasing order). A side with three steps needs a rise of at least `1 + 2 + 3 = 6`, so the number of columns on one side is at most the largest integer whose triangular number is at most `h − 1`: 1 at `h = 2, 3`, 2 at `h = 4, …, 6`, 3 at `h = 7, …, 10`.
- **Step-reversal bijection.** Reversing the order of the steps on each side (rotating each side 180° inside its own bounding box) turns a hoodoo into a monadnock with the same `w`, `h`, end columns, side lengths, and summit length. The two examples above are such a pair. The hoodoo always has the smaller area (166 against 254 in the example): its sides lie below the chord between their ends, the monadnock's above it.
- **Count.** The two sides are chosen independently and the summit takes the remaining width, so the count at width `w` is the number of ordered pairs of distinct-part partitions (sums in `1, …, h − 1`) whose numbers of parts add to at most `w − 1`. Hoodoo castles, and equally monadnock castles, by width `w = 3, 4, 5, …` (checked by brute force, with the bijection, for `h ≤ 7`):

```
h = 2:   1,   1,   1, …
h = 3:   4,   4,   4, …
h = 4:   9,  15,  16,  16, …
h = 5:  16,  32,  36,  36, …
h = 6:  25,  65,  81,  81, …
h = 7:  36, 108, 156, 168, 169, 169, …
```

At `w = 3` the count is `(h − 1)²` (one free column on each side). Once `w` exceeds twice the longest possible side, every pair of sides fits and the count stops changing: it is the square of the number of distinct-part partitions of `1, …, h − 1`, that is, of the sum of OEIS A000009[^8] over `1, …, h − 1`. By `h = 2, 3, …, 15`: `1, 4, 16, 36, 81, 169, 324, 576, 1024, 1764, 2916, 4761, 7569, 11881`.

- **Growth.** By width at fixed `h` the count is eventually constant, so neither family has a width growth constant above 1 and neither sits on the metallic ladder of [[castle-classification-growth](pages/castle-classification-growth.md)]. By height, the count grows at the subexponential rate of the distinct-part partition numbers.
- **Parity.** Both families are unimodal, so every member has exactly `h` blocks; the PE 502 even-block clause keeps all of them when `h` is even and none when `h` is odd.

**Convexity fixes the block count.** A convex castle of height `h` has exactly `h` blocks, one per row, and convex castles are exactly the minimum-block castles.[^4] So on this axis the Project Euler 502 (PE 502) parity clause is decided by `h`: every convex castle has the block parity of `h`, and the even-block projector of [[castle-sign](pages/castle-sign.md)] keeps all of them (`h` even) or none (`h` odd).

### Axis 2: Rate of change (Lipschitz)

Types 7, 8, 9, the base m-disparate, and the wiki-named ridge type:

| Type | Predicate | Wiki tie |
|---|---|---|
| **Plateau-free** | `c_i ≠ c_{i+1}` for all `i` | elementary: `h(h−1)^{w−1}` skylines of height `≤ h`, so `h(h−1)^{w−1} − (h−1)(h−2)^{w−1}` castles, growth `h − 1`; its ridge variant (next row) realizes the whole metallic ladder |
| **Ridge** (wiki-named, not one of the 35) | `c_i ≠ c_{i+1}` unless `c_i = c_{i+1} = h` | counted: `𝟙ᵀR_h^{w−1}𝟙 − (h−1)(h−2)^{w−1}` castles with `R_h = J − D`, growth the metallic mean `δ_{h−1}` ([[metallic-strip-realizability](pages/metallic-strip-realizability.md)]); see **Ridge castles** below |
| **m-smooth (Lipschitz)** | `|c_{i+1} − c_i| ≤ m` | at `m = 1` this is the **Motzkin-path** predicate without its endpoint condition (Axis 3); the 1-smooth strip over heights `≤ 3` is the silver realization on [[metallic-strip-realizability](pages/metallic-strip-realizability.md)] and, anchored at height 1, the [[pell-castle-strip](pages/pell-castle-strip.md)], whose strips that reach height 3 are the Pell castles ([[pell-castle](pages/pell-castle.md)]) |
| **Zigzag** | differences alternate in sign | *open* - a strong plateau-free variant |
| **m-disparate** | `|c_{i+1} − c_i| ≥ m` | *open* - the "no small step" restriction |

**Where the wiki already has counts:** 1-smooth strips at bounded height, by transfer matrix ([[metallic-strip-realizability](pages/metallic-strip-realizability.md)]: Pell-Lucas A001333 over heights `≤ 3`, Pell A000129 when anchored at height 1). A 1-smooth castle is not a Motzkin path unless its skyline also starts and ends at height 1, so 1-smooth counts are strip counts, not Motzkin numbers. The tower word A004149 ([[tower-word-continued-fraction](pages/tower-word-continued-fraction.md)]) is a different object: Motzkin paths with no `UD` or `DU` factor, counted by word length, which as skylines are unrestricted towers. **Open:** the full m-smooth family for `m ≥ 2`, and m-disparate for any `m`. **A distinct horizontal-gap axis is counted:** [[tower-spacing-castles](pages/tower-spacing-castles.md)] requires every valley between raised regions to be `≥ g` columns wide - a same-row spacing rule rather than a same-column-difference rule - counted by a column-sweep transfer matrix, with growth constants through `ψ²` (h=2, g=2) and `φ` (h=2, g=3) and a non-metallic zoo for `h ≥ 3`.

**Ridge castles.** A **ridge castle** ([[ridge-castle](pages/ridge-castle.md)]) is a castle of exact height `h` in which neighbouring columns differ in height unless both reach the ceiling `h`. Flat runs occur only at the ceiling; below it the skyline steps up or down at every column, and all heights `1, …, h` may occur. To build one, pick `c_1`, then give each next column any height other than the current one, or `h` again when the current one is `h`; keep the skylines in which some column reaches `h`. Example, `h = 4`, `w = 12`: `(3, 1, 3, 4, 4, 1, 4, 4, 1, 4, 2, 1)`.

- **Transfer matrix.** `R_h = J − D`, with `J` the `h × h` all-ones matrix and `D = diag(1, …, 1, 0)`: entry `(a, b)` is 1 when `a ≠ b` or `a = b = h`. Its characteristic polynomial is `(x + 1)^{h−2}(x² − (h − 1)x − 1)`.
- **Count.** `𝟙ᵀR_h^{w−1}𝟙 − (h−1)(h−2)^{w−1}` ridge castles of width `w` and exact height `h`; the subtracted term is the plateau-free skylines that never reach `h`. By width `w = 1, …, 7`: `h = 2`: `1, 3, 5, 8, 13, 21, 34`; `h = 3`: `1, 5, 15, 39, 97, 237, 575`; `h = 4`: `1, 7, 31, 118, 421, 1453, 4924` (checked by brute force).
- **Growth.** Like `δ_{h−1}^w`: golden at `h = 2`, silver at `h = 3`, bronze at `h = 4`, copper at `h = 5`, nickel at `h = 6`. Each rung is a `<metal>` width growth castle of [[castle-classification-growth](pages/castle-classification-growth.md)] Axis 8, and for bronze and above the ridge rule is the only known realization ([[metallic-strip-realizability](pages/metallic-strip-realizability.md)]).
- **Fibonacci castles.** At `h = 2` the rule forbids two adjacent columns of height 1. Exchanging the heights 1 and 2 turns a ridge castle into a skyline with no two adjacent 2s: a **Fibonacci castle** ([[fibonacci-castle](pages/fibonacci-castle.md)]; exact height 2, no two adjacent height-2 columns; the tree castles of [[castle-graph](pages/castle-graph.md)] at exact height 2), or the all-1 row, which comes from the all-2 castle. So for `w ≥ 2` there are `F_{w+2}` ridge castles of exact height 2 and `F_{w+2} − 1` Fibonacci castles. Counted with `q` marking area, the Fibonacci castles are the q-Fibonacci castles ([[q-fibonacci-castle](pages/q-fibonacci-castle.md)]). Rules on the tower cut out sub-families, among them the Fibonacci-word castles (tower a factor of the Fibonacci word, `w + 1` from `w = 3`) the balanced castles (`A005598(w)/2`), and the gap-length families, maximal castles (Padovan), spaced castles (Narayana's cows) and `(d, k)`-RLL castles: [[fibonacci-castles-sub-families](pages/fibonacci-castles-sub-families.md)].
- **Not crenellated.** The crenellated type of Axis 7 is the strict period-2 skyline `(a, h, a, h, …)`; ridge castles may use every height and may repeat `h`.
- **Code.** `ridge_R`, `ridge_count` (free-height strip counts) and `proper_even` (even-block ridge castles) on [[castle-snippets-strips](pages/castle-snippets-strips.md)].

### Axis 3: Path-like restrictions

Types 13 and 14 identify the skyline with a classical lattice path:

| Type | Predicate | Wiki tie |
|---|---|---|
| **Dyck-path** | `c_1 = c_w = 1`, `|c_{i+1} − c_i| = 1` | [[dyck-words](pages/dyck-words.md)], [[catalan-numbers](pages/catalan-numbers.md)] |
| **Motzkin-path** | `c_1 = c_w = 1`, `|c_{i+1} − c_i| ≤ 1` (flat steps allowed) | [[motzkin-numbers](pages/motzkin-numbers.md)]; drop the endpoint condition and this is the 1-smooth type of Axis 2 |

**The counts carry an endpoint and a height condition.** Shifting heights down by one turns a Dyck-path skyline into a Dyck path of `w − 1` steps, so `w` is odd and the semilength is `n = (w − 1)/2`; and because a castle attains its height `h`, the path's maximum height is exactly `h − 1`. The Catalan number `C_n` counts Dyck-path castles only after summing over `h`. At fixed `(w, h)` the count is the height-refined triangle A080936, "Dyck paths of semilength `n` and height `k`" with `k = h − 1`,[^5] and at height at most `h` it is the bounded-height count A080934, whose GF is a ratio of Chebyshev-type polynomials rather than the algebraic Catalan GF.[^6] The same holds for Motzkin: at fixed `(w, h)` the count is A097862, "Motzkin paths of length `n` and height `k`" with `n = w − 1`, `k = h − 1`,[^7] and only the sum over `h` is the Motzkin number `M_{w−1}`. Checked by enumeration for `w ≤ 9`, `h ≤ 5`:

```
Dyck-path castles, rows w = 1,3,5,7,9, columns h = 1..5, then the row sum
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

The `h = 2` Motzkin column is `2^{w−2} − 1`: a height-2 Motzkin-path castle is any nonempty pattern of raised interior columns. The `h = 2` Dyck column is 1: the only Dyck-path castle of height 2 at odd `w` is the alternating `(1,2,1,2,…,1)`. The predicates are implemented as `is_dyck_path` and `is_motzkin_path` on [[castle-snippets](pages/castle-snippets.md)].

### Axis 4: Symmetry

Types 11, 12, 21 impose symmetry on the skyline:

| Type | Predicate | Wiki tie |
|---|---|---|
| **Palindromic** | `c_i = c_{w+1−i}` | counted by width and blocks: the symmetric-bargraph GF of [[deutsch-elizalde-2016-bargraphs-cornerless-motzkin](pages/deutsch-elizalde-2016-bargraphs-cornerless-motzkin.md)] §4.1, built from cornerless Motzkin prefixes; by semi-perimeter A273905, `1, 2, 3, 5, 9, 15, 27, 46, 83` (checked by brute force); fixed `(w, h)` still open |
| **Centrally symmetric** | `c_i + c_{w+1−i} = h + 1` (180° rotation inside bounding box) | *open* |
| **Self-conjugate** | `c_i = #{j : c_j ≥ i}` (transpose invariance) | *open* - classical partition-conjugation, would require `w = h` |

**Open apart from the palindromic GF.** The self-conjugate type forces `w = h`.

### Axis 5: Value / extremum constraints

Types 15, 16, 24, 26, 27, 33, 35, and a few others restrict where extremes occur:

| Type | Predicate | Wiki tie |
|---|---|---|
| **Flat-top** | `h` attained in ≥ 2 consecutive columns | *open* |
| **Single-summit** | `h` attained in exactly one column | *open* - matches strictly-unimodal at the peak |
| **Twin-peak** | `h` attained in exactly two columns | *open* |
| **Single-valley** | height 1 attained in exactly one column | *open* - dual to single-summit |
| **Rainbow** | `w = h`, heights a permutation of `{1, …, h}` | exactly `h!` castles ([[aocp-permutations](pages/aocp-permutations.md)]); graded by skyline inversions they are the Mahonian numbers A008302 ([[aocp-combinatorics](pages/aocp-combinatorics.md)]); direct link to permutation-based combinatorics ([[permutation-cycle-castle-analogy](pages/permutation-cycle-castle-analogy.md)]) |
| **Boxcastle** | `c_i = h` for all `i` | trivial: count is `1` |
| **Hook** | `c_1 = h`, `c_i = 1` for `i ≥ 2` | Young-diagram hook; count is `1` at every `(w, h)`, since the predicate fixes every column. Admitting the mirror `c_w = h` gives 2; letting the tower stand in any column gives `w` |

**Rainbow castles and permutations.** Rainbow castles are in bijection with permutations of `{1, …, h}` ([[permutation-cycle-castle-analogy](pages/permutation-cycle-castle-analogy.md)]), so the cycle-count / Foata / streak triad of [[castles-as-upgraded-cycle-count](pages/castles-as-upgraded-cycle-count.md)] applies to them without modification.

### Axis 6: Parity and area

Types 10, 17, 18, 32:

| Type | Predicate | Wiki tie |
|---|---|---|
| **Alternating parity** | `c_i` alternates odd/even | *open* |
| **Even-area** | `∑ c_i ≡ 0 (mod 2)` | [[castle-by-area](pages/castle-by-area.md)] parity split |
| **Even-peak** | number of local maxima is even | a second parity statistic beside [[castle-sign](pages/castle-sign.md)]'s `(−1)^blocks`; *open* |
| **Triangular-area** | `∑ c_i = n(n+1)/2` | *open* |

**Even-peak.** The [[castle-sign](pages/castle-sign.md)] is `(−1)^blocks`; even-peak is a parity constraint on the number of local maxima of the skyline, and the wiki has no count for it. The "peaks" of [[castle-foata-transform](pages/castle-foata-transform.md)] and [[permutation-cycle-castle-analogy](pages/permutation-cycle-castle-analogy.md)] are a different statistic, the excursions above the base (maximal runs of columns of height at least 2): `(2, 3, 2, 3, 2)` has one excursion and two local maxima.

### Axis 7: Value patterns

Types 19, 20, 22, 23, 25, 28, 29, 34:

| Type | Predicate | Wiki tie |
|---|---|---|
| **Equal-block** | all maximal horizontal blocks have the same length | *open* - heavy structure |
| **Two-level** | exactly two distinct height values | at `h = 2` this is every castle except the all-2 rectangle (`2^w − 2`); the height-2 tree castles ([[castle-graph](pages/castle-graph.md)]) are a Fibonacci-counted sub-family |
| **Crenellated** | `c_i ∈ {a, h}` with `c_i ≠ c_{i+1}`: period 2, `(a, h, a, h, …)` (battlements); not the ridge castles of Axis 2 | *open* - very restricted two-level; at even width, the two-atom skyline-DFT case (support `{0, w/2}`) on [[spectral-analysis](pages/spectral-analysis.md)] |
| **Moated** | `c_1 = c_w = 1`, all interior `≥ 2` | *open* |
| **Fence-post** | `c_i = 1` for all even `i` | *open* |
| **Linear** | `c_i = a + (i−1)d` (arithmetic progression) | elementary: `2⌊(h−1)/(w−1)⌋ + 1` castles for `w ≥ 2` |
| **Prime-top** | `h` is prime | trivial family: all castles with prime `h` |
| **Integer-mean** | `w | ∑ c_i` | *open* |

## Open geometric threads

In rough order of tractability:

1. **k-modal** for `k ≥ 2` - a parametric family whose `k = 1` case is [[convex-castle](pages/convex-castle.md)] (binomial); `k = 2, 3, …` are open.
2. **m-smooth / m-disparate** for `m ≥ 2` - a paired family; `m = 1` smooth is the strip-counted case above.
3. **Symmetry types** (palindromic, centrally symmetric, self-conjugate) - palindromic has a GF by width and blocks ([[deutsch-elizalde-2016-bargraphs-cornerless-motzkin](pages/deutsch-elizalde-2016-bargraphs-cornerless-motzkin.md)]); its `(w, h)` table, its parity split, and the other two types are untouched.
4. **Rainbow** - skylines that are permutations of `{1, …, h}`, tied to the [[castles-as-upgraded-cycle-count](pages/castles-as-upgraded-cycle-count.md)] triad.
5. **Even-peak** - parity of the number of local maxima rather than of the block count ([[castle-sign](pages/castle-sign.md)]).
6. **Dyck- and Motzkin-path castles at fixed height** - the A080936 / A097862 columns as castle counts; which other geometric types have a bounded-height rational GF of the same Chebyshev-quotient shape?

## Related Concepts

- [[castle-classification](pages/castle-classification.md)] - the hub: framing, the geometric / non-geometric split, and the consolidated open-thread list.
- [[castle-classification-spectrum](pages/castle-classification-spectrum.md)] - spectral types; [[castle-classification-growth](pages/castle-classification-growth.md)] - growth types.
- [[castle-polyomino](pages/castle-polyomino.md)] / [[castle-representations](pages/castle-representations.md)] - the base object and the skyline encoding the predicates read.
- [[convex-castle](pages/convex-castle.md)] / [[convex-castle-binomial-identity](pages/convex-castle-binomial-identity.md)] - the unimodal (row-convex) type.
- [[polyominoes](pages/polyominoes.md)] / [[column-convex-polyomino](pages/column-convex-polyomino.md)] / [[column-convex-polygon-enumeration](pages/column-convex-polygon-enumeration.md)] - the base-type home literature.
- [[stack-polyomino-gf](pages/stack-polyomino-gf.md)] - the unimodal-skyline family from Analytic Combinatorics (AC) Ex. I.8.
- [[dyck-words](pages/dyck-words.md)] / [[motzkin-numbers](pages/motzkin-numbers.md)] / [[tower-word-continued-fraction](pages/tower-word-continued-fraction.md)] - the path-like types and their run-constrained refinement.
- [[castle-by-area](pages/castle-by-area.md)] - where several types (even-area, valley) are counted.
- [[castle-sign](pages/castle-sign.md)] / [[castle-foata-transform](pages/castle-foata-transform.md)] - the parity / peak-count / record statistics several types predicate on.
- [[castles-as-upgraded-cycle-count](pages/castles-as-upgraded-cycle-count.md)] - the framework the rainbow type maps onto directly.
- [[castle-snippets](pages/castle-snippets.md)] - short tested Python snippets for the predicates on this page.
- [[hoodoo-monadnock-castles](pages/hoodoo-monadnock-castles.md)] - the hoodoo and monadnock types in full: sides as partitions into distinct parts, the Hindenburg-algorithm generator, counts and growth.
- [[aocp-permutations](pages/aocp-permutations.md)] / [[aocp-combinatorics](pages/aocp-combinatorics.md)] - the rainbow type's count `h!` and its Mahonian inversion grading.
- [[castle-compression](pages/castle-compression.md)] - the description-length axis that cross-cuts these shape axes.
- [[tower-parity-sectors](pages/tower-parity-sectors.md)] - a second castle route to Axis 2's Hardin family (A005251, A202882, A203094, A203184): the even sector for `k ≡ 2 (mod 4)` is `2^L` times a Hardin word count, complementing the tower-spacing route.

## Footnotes

[^1]: raw/castle-types.wiki L1-L9 - "A castle on a w × h grid is determined by its skyline, the sequence of column heights c_1, c_2, …, c_w with 1 ≤ c_i ≤ h and max_i c_i = h. (Problem 502 also requires an even number of blocks; the types below mostly ignore, or independently re-impose, that parity rule.) Every castle is automatically column-convex and bottom-aligned, so each type is a further restriction on the skyline." (Source: https://charlesreid1.com/wiki/Project_Euler/502/Castle_Types, fetched 2026-09-15.)
[^2]: raw/castle-types.wiki §"Base types" L11-L19 - the 7 base types: column-convex, unimodal (`c_1 ≤ … ≤ c_p ≥ … ≥ c_w`), directed (every cell reachable from bottom-left by east/north path), parallelogram (perpendicular-to-main-diagonal sections are connected), Ferrers (`c_1 ≥ … ≥ c_w`), staircase (Ferrers with strict inequality - all distinct heights), m-disparate (`|c_{i+1} − c_i| ≥ m`).
[^3]: raw/castle-types.wiki §"Proposed additional types" L21-L57 - the 35 proposed types, numbered 1-35: convex/row-convex, reverse Ferrers, strictly unimodal, bimodal, k-modal, anti-unimodal (V-shaped), plateau-free, m-smooth (Lipschitz), zigzag, alternating parity, palindromic, centrally symmetric, Dyck-path (`c_1 = c_w = 1`, all `c_i ≥ 1`, `|c_{i+1} − c_i| = 1`), Motzkin-path ("like a Dyck-path castle but allowing flat steps: `|c_{i+1} − c_i| ≤ 1`"), flat-top, single-summit, even-area, even-peak, equal-block, two-level, self-conjugate, crenellated, moated, rainbow, hook (`c_1 = h` and `c_i = 1` for `i ≥ 2`), twin-peak, single-valley, fence-post, linear, convex-skyline (second differences ≥ 0), concave-skyline (≤ 0), triangular-area, prime-top, integer-mean, boxcastle.
[^4]: [[oeis-mining-pe502](pages/oeis-mining-pe502.md)] `binomial-vandermonde-identity.md` §1 L25-33 - "#blocks >= max(c) = h, with equality iff the profile is unimodal ... a convex castle of height h has exactly h blocks, and convex castles are exactly the minimum-block castles".
[^5]: https://oeis.org/A080936 - "Triangle read by rows: T(n,k) is the number of Dyck paths of semilength n and height k (1 <= k <= n)"; data begins 1; 1, 1; 1, 3, 1; 1, 7, 5, 1; 1, 15, 18, 7, 1.
[^6]: https://oeis.org/A080934 - "Square array read by antidiagonals of number of Catalan paths (nonnegative, starting and ending at 0, step +-1) of 2n steps with all values less than k"; the bounded-height Dyck counts whose GF is a ratio of consecutive Chebyshev-type polynomials.
[^7]: https://oeis.org/A097862 - "Triangle read by rows: T(n,k) is the number of Motzkin paths of length n and height k (n>=0, k>=0)"; data begins 1; 1; 1, 1; 1, 3; 1, 7, 1; 1, 15, 5; 1, 31, 18, 1.
[^8]: https://oeis.org/A000009 - "Expansion of Product_{m >= 1} (1 + x^m); number of partitions of n into distinct parts; number of partitions of n into odd parts"; data begins 1, 1, 1, 2, 2, 3, 4, 5, 6, 8, 10, 12, 15, 18.
