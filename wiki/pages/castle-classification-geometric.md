---
title: Castle classification - geometric types
category: Concepts
summary: The 42 shape-based castle types (7 base, 35 proposed) as skyline predicates on individual castles, grouped into Axes 1-7 - convexity, rate of change, path-like, symmetry, extremum, parity/area, value patterns - with each type's wiki home and count status.
tags: [concept, castle, classification, taxonomy, skyline, geometric, unimodal, ferrers, dyck-path, motzkin-path, rainbow, hook]
sources: [castle-classification]
created: 2026-09-19
updated: 2026-09-19
---

# Castle classification - geometric types

A **geometric** castle type is a predicate on the shape of one castle, read off its skyline `(c_1, …, c_w)` ([[castle-classification](pages/castle-classification.md)] for the framing, [[castle-polyomino](pages/castle-polyomino.md)] for the object). Every castle is column-convex and bottom-aligned already, so each type below is a further restriction on the skyline.[^1] This page is the catalogue: the 7 base types from the polyomino literature and the 35 proposed types, grouped into seven structural axes, each tied to the wiki thread that already touches it and marked as counted, candidate, or open. The non-geometric techniques (growth type of a class, spectrum of the castle graph, description length) are on [[castle-classification-non-geometric](pages/castle-classification-non-geometric.md)].

## The base 7 types and their wiki homes

The base types are all standard polyomino / composition families. Each corresponds to an existing wiki thread:[^2]

| Type | Definition (skyline predicate) | Wiki home | Count status |
|---|---|---|---|
| **Column-convex** | (automatic for castles) | [[column-convex-polyomino](pages/column-convex-polyomino.md)] | matches all castles; `A(w,h) = h^w − (h−1)^w` |
| **Unimodal** | `c_1 ≤ … ≤ c_p ≥ … ≥ c_w` | [[convex-castle](pages/convex-castle.md)] | `C(2h+w−3, w−1)` via [[convex-castle-binomial-identity](pages/convex-castle-binomial-identity.md)] |
| **Ferrers** | `c_1 ≥ c_2 ≥ … ≥ c_w` (weakly decreasing) | [[polyominoes](pages/polyominoes.md)], [[column-convex-polygon-enumeration](pages/column-convex-polygon-enumeration.md)] | classical; by area = partition GF; q-Catalan / q-Bessel refinement |
| **Staircase** | Ferrers with all `c_i` distinct | [[polyominoes](pages/polyominoes.md)] | classical (distinct-parts partitions) |
| **Parallelogram** | anti-diagonal sections connected | [[column-convex-polygon-enumeration](pages/column-convex-polygon-enumeration.md)] | classical (Bousquet-Mélou) |
| **Directed** | every cell reachable from `(1,1)` by east/north | [[polyominoes](pages/polyominoes.md)] | classical (directed polyominoes) |
| **m-disparate** | `|c_{i+1} − c_i| ≥ m` for all `i` | **not yet on the wiki** | open |

The first 6 rows tie the castle taxonomy directly to the polyomino literature. **m-disparate** is the one base type without an existing wiki thread - a natural target for the "gap-rule variations" idea on `IDEAS.md`; its horizontal-gap cousin is already counted on [[tower-spacing-castles](pages/tower-spacing-castles.md)].

## The 35 proposed types, grouped by structural axis

The proposed types cluster into seven structural axes, some of which the wiki has counts for.[^3]

### Axis 1: Convexity / modality

Types 1-6 and 30-31 restrict the shape of the skyline's local extrema:

| Type | Predicate | Wiki tie |
|---|---|---|
| **Convex (row-convex)** | every row is one contiguous run | equals unimodal for castles ([[convex-castle](pages/convex-castle.md)]); front/middle/back U/R/D form on [[project-euler-502-representations](pages/project-euler-502-representations.md)] |
| **Reverse Ferrers** | `c_1 ≤ … ≤ c_w` (weakly increasing) | Ferrers's mirror; same count by symmetry |
| **Strictly unimodal** | strict rise, one peak, strict fall | strengthens unimodal; count is a sub-count of [[convex-castle](pages/convex-castle.md)] |
| **Bimodal** | exactly two local maxima | *open* - natural refinement, no wiki count yet |
| **k-modal** | at most `k` local maxima | *open* - unimodal is `k=1`; parameterized family |
| **Anti-unimodal (V-shaped)** | weakly decrease then weakly increase | the "valley" family; on [[castle-by-area](pages/castle-by-area.md)] as valley castles, area-OEIS A332578; the [[convex-castle-binomial-identity](pages/convex-castle-binomial-identity.md)] valley bijection is an open thread |
| **Convex-skyline** | `c_{i−1} − 2c_i + c_{i+1} ≥ 0` (discrete convex) | *open* - a stronger sub-family of anti-unimodal |
| **Concave-skyline** | `c_{i−1} − 2c_i + c_{i+1} ≤ 0` (discrete concave) | *open* - a stronger sub-family of unimodal |

**Where the wiki already has counts:** unimodal and (by symmetry) reverse Ferrers, via the [[convex-castle-binomial-identity](pages/convex-castle-binomial-identity.md)]; anti-unimodal (valley) by area on [[castle-by-area](pages/castle-by-area.md)]. **Where the wiki has candidate counts but not proofs:** the convex⟺valley bijection.

**Convexity fixes the block count.** A convex castle of height `h` has exactly `h` blocks, one per row, and convex castles are exactly the minimum-block castles.[^4] So the Project Euler 502 (PE 502) parity clause is not independent of this axis: every convex castle has the block parity of `h`, and the even-block projector of [[castle-sign](pages/castle-sign.md)] keeps all of them or none.

### Axis 2: Rate of change (Lipschitz)

Types 7, 8, 9 and the base m-disparate:

| Type | Predicate | Wiki tie |
|---|---|---|
| **Plateau-free** | `c_i ≠ c_{i+1}` for all `i` | the plateau-free-except-ceiling variant realizes the whole metallic ladder ([[metallic-strip-realizability](pages/metallic-strip-realizability.md)]); the strict version is open |
| **m-smooth (Lipschitz)** | `|c_{i+1} − c_i| ≤ m` | at `m = 1` this is the **Motzkin-path** predicate without its endpoint condition (Axis 3); the 1-smooth strip over heights `≤ 3` is the silver realization on [[metallic-strip-realizability](pages/metallic-strip-realizability.md)] and, anchored at height 1, the [[pell-castle-strip](pages/pell-castle-strip.md)] |
| **Zigzag** | differences alternate in sign | *open* - a strong plateau-free variant |
| **m-disparate** | `|c_{i+1} − c_i| ≥ m` | *open* - the "no small step" restriction |

**Where the wiki already has counts:** 1-smooth strips at bounded height, by transfer matrix ([[metallic-strip-realizability](pages/metallic-strip-realizability.md)]: companion Pell A001333 over heights `≤ 3`, Pell A000129 when anchored at height 1). A 1-smooth castle is not a Motzkin path unless its skyline also starts and ends at height 1, so 1-smooth counts are strip counts, not Motzkin numbers. The tower word A004149 ([[tower-word-continued-fraction](pages/tower-word-continued-fraction.md)]) is the 1-smooth-with-no-UD-no-DU refinement. **Open:** the full m-smooth family for `m ≥ 2`, and m-disparate for any `m`. **A distinct horizontal-gap axis is counted:** [[tower-spacing-castles](pages/tower-spacing-castles.md)] requires every valley between raised regions to be `≥ g` columns wide - a same-row spacing rule rather than a same-column-difference rule - counted by a column-sweep transfer matrix, with growth constants through `ψ²` (h=2, g=2) and `φ` (h=2, g=3) and a non-metallic zoo for `h ≥ 3`.

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
| **Palindromic** | `c_i = c_{w+1−i}` | *open* - a natural symmetry restriction |
| **Centrally symmetric** | `c_i + c_{w+1−i} = h + 1` (180° rotation inside bounding box) | *open* |
| **Self-conjugate** | `c_i = #{j : c_j ≥ i}` (transpose invariance) | *open* - classical partition-conjugation, would require `w = h` |

**Open across the board.** The self-conjugate type is particularly interesting because it forces `w = h` and interacts with the wiki's Fibonacci-in-prime-castle count `2^{n−1} − F_{n−1}` on [[castle-by-area](pages/castle-by-area.md)].

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

**Rainbow castles are the natural bridge to [[permutation-cycle-castle-analogy](pages/permutation-cycle-castle-analogy.md)]:** they are, by definition, in bijection with permutations of `{1, …, h}` - so the wiki's cycle-count / Foata / streak triad ([[castles-as-upgraded-cycle-count](pages/castles-as-upgraded-cycle-count.md)]) applies to them directly, not by upgrade. Rainbow castles are the "n! degenerate case" of the castle machinery.

### Axis 6: Parity and area

Types 10, 17, 18, 32:

| Type | Predicate | Wiki tie |
|---|---|---|
| **Alternating parity** | `c_i` alternates odd/even | *open* |
| **Even-area** | `∑ c_i ≡ 0 (mod 2)` | [[castle-by-area](pages/castle-by-area.md)] parity split |
| **Even-peak** | number of local maxima is even | [[castle-sign](pages/castle-sign.md)] sibling; peak count is on [[castle-foata-transform](pages/castle-foata-transform.md)]; the block ≠ peak distinction is spelled out on [[pe502-castle-cycle-permutations](pages/pe502-castle-cycle-permutations.md)] |
| **Triangular-area** | `∑ c_i = n(n+1)/2` | *open* - a curiosity restriction |

**The even-peak type is worth flagging.** The [[castle-sign](pages/castle-sign.md)] is `(−1)^blocks`, not `(−1)^peaks`; even-peak is a different parity constraint that the wiki hasn't investigated. The [[castle-foata-transform](pages/castle-foata-transform.md)] identifies `#peaks = #records`, so even-peak is "even-records" - a permutation-statistic parity condition.

### Axis 7: Value patterns

Types 19, 20, 22, 23, 25, 28, 29, 34:

| Type | Predicate | Wiki tie |
|---|---|---|
| **Equal-block** | all maximal horizontal blocks have the same length | *open* - heavy structure |
| **Two-level** | exactly two distinct height values | at `h = 2` this is every castle (`A(w,2) = 2^w − 1`); the height-2 tree castles ([[castle-graph](pages/castle-graph.md)]) are its Fibonacci sub-family |
| **Crenellated** | heights alternate `{a, h}` (battlements) | *open* - very restricted two-level; the two-atom skyline-DFT case on [[spectral-analysis](pages/spectral-analysis.md)] |
| **Moated** | `c_1 = c_w = 1`, all interior `≥ 2` | *open* |
| **Fence-post** | `c_i = 1` for all even `i` | *open* |
| **Linear** | `c_i = a + (i−1)d` (arithmetic progression) | *open* - count is `O(h)` or `O(wh)` depending on parameters |
| **Prime-top** | `h` is prime | trivial family: all castles with prime `h` |
| **Integer-mean** | `w | ∑ c_i` | *open* |

## Open geometric threads

In rough order of tractability:

1. **k-modal** for `k ≥ 2` - a parametric family whose `k = 1` case is [[convex-castle](pages/convex-castle.md)] (binomial); `k = 2, 3, …` are genuinely open with no candidate closed form.
2. **m-smooth / m-disparate** for `m ≥ 2` - a paired family; `m = 1` smooth is the strip-counted case above.
3. **Symmetry types** (palindromic, centrally symmetric, self-conjugate) - untouched.
4. **Rainbow** - direct permutation-classification tie, immediate seminar target for the [[castles-as-upgraded-cycle-count](pages/castles-as-upgraded-cycle-count.md)] triad.
5. **Even-peak** - parity via peak count rather than block count; genuinely different from [[castle-sign](pages/castle-sign.md)]'s `(−1)^blocks`.
6. **Dyck- and Motzkin-path castles at fixed height** - the A080936 / A097862 columns as castle counts; which other geometric types have a bounded-height rational GF of the same Chebyshev-quotient shape?

## Related Concepts

- [[castle-classification](pages/castle-classification.md)] - the hub: framing, the geometric / non-geometric split, and the consolidated open-thread list.
- [[castle-classification-non-geometric](pages/castle-classification-non-geometric.md)] - growth-type, spectral, and compressibility classification.
- [[castle-polyomino](pages/castle-polyomino.md)] / [[castle-representations](pages/castle-representations.md)] - the base object and the skyline encoding the predicates read.
- [[convex-castle](pages/convex-castle.md)] / [[convex-castle-binomial-identity](pages/convex-castle-binomial-identity.md)] - the unimodal (row-convex) type.
- [[polyominoes](pages/polyominoes.md)] / [[column-convex-polyomino](pages/column-convex-polyomino.md)] / [[column-convex-polygon-enumeration](pages/column-convex-polygon-enumeration.md)] - the base-type home literature.
- [[stack-polyomino-gf](pages/stack-polyomino-gf.md)] - the unimodal-skyline (single-peak) family from Analytic Combinatorics (AC) Ex. I.8.
- [[dyck-words](pages/dyck-words.md)] / [[motzkin-numbers](pages/motzkin-numbers.md)] / [[tower-word-continued-fraction](pages/tower-word-continued-fraction.md)] - the path-like types and their run-constrained refinement.
- [[castle-by-area](pages/castle-by-area.md)] - where several types (even-area, valley) are counted.
- [[castle-sign](pages/castle-sign.md)] / [[castle-foata-transform](pages/castle-foata-transform.md)] - the parity / peak-count / record statistics several types predicate on.
- [[castles-as-upgraded-cycle-count](pages/castles-as-upgraded-cycle-count.md)] - the framework the rainbow type maps onto directly.
- [[castle-snippets](pages/castle-snippets.md)] - tested Python one-liners for each predicate on this page.
- [[aocp-permutations](pages/aocp-permutations.md)] / [[aocp-combinatorics](pages/aocp-combinatorics.md)] - the rainbow type's count `h!` and its Mahonian inversion grading.
- [[castle-compression](pages/castle-compression.md)] - the description-length axis that cross-cuts these shape axes.

## Footnotes

[^1]: raw/castle-types.wiki L1-L9 - "A castle on a w × h grid is determined by its skyline, the sequence of column heights c_1, c_2, …, c_w with 1 ≤ c_i ≤ h and max_i c_i = h. (Problem 502 also requires an even number of blocks; the types below mostly ignore, or independently re-impose, that parity rule.) Every castle is automatically column-convex and bottom-aligned, so each type is a further restriction on the skyline." (Source: https://charlesreid1.com/wiki/Project_Euler/502/Castle_Types, fetched 2026-09-15.)
[^2]: raw/castle-types.wiki §"Base types" L11-L19 - the 7 base types: column-convex, unimodal (`c_1 ≤ … ≤ c_p ≥ … ≥ c_w`), directed (every cell reachable from bottom-left by east/north path), parallelogram (perpendicular-to-main-diagonal sections are connected), Ferrers (`c_1 ≥ … ≥ c_w`), staircase (Ferrers with strict inequality - all distinct heights), m-disparate (`|c_{i+1} − c_i| ≥ m`).
[^3]: raw/castle-types.wiki §"Proposed additional types" L21-L57 - the 35 proposed types, numbered 1-35: convex/row-convex, reverse Ferrers, strictly unimodal, bimodal, k-modal, anti-unimodal (V-shaped), plateau-free, m-smooth (Lipschitz), zigzag, alternating parity, palindromic, centrally symmetric, Dyck-path (`c_1 = c_w = 1`, all `c_i ≥ 1`, `|c_{i+1} − c_i| = 1`), Motzkin-path ("like a Dyck-path castle but allowing flat steps: `|c_{i+1} − c_i| ≤ 1`"), flat-top, single-summit, even-area, even-peak, equal-block, two-level, self-conjugate, crenellated, moated, rainbow, hook (`c_1 = h` and `c_i = 1` for `i ≥ 2`), twin-peak, single-valley, fence-post, linear, convex-skyline (second differences ≥ 0), concave-skyline (≤ 0), triangular-area, prime-top, integer-mean, boxcastle.
[^4]: [[oeis-mining-pe502](pages/oeis-mining-pe502.md)] `binomial-vandermonde-identity.md` §1 L25-33 - "#blocks >= max(c) = h, with equality iff the profile is unimodal ... a convex castle of height h has exactly h blocks, and convex castles are exactly the minimum-block castles".
[^5]: https://oeis.org/A080936 - "Triangle read by rows: T(n,k) is the number of Dyck paths of semilength n and height k (1 <= k <= n)"; data begins 1; 1, 1; 1, 3, 1; 1, 7, 5, 1; 1, 15, 18, 7, 1.
[^6]: https://oeis.org/A080934 - "Square array read by antidiagonals of number of Catalan paths (nonnegative, starting and ending at 0, step +-1) of 2n steps with all values less than k"; the bounded-height Dyck counts whose GF is a ratio of consecutive Chebyshev-type polynomials.
[^7]: https://oeis.org/A097862 - "Triangle read by rows: T(n,k) is the number of Motzkin paths of length n and height k (n>=0, k>=0)"; data begins 1; 1; 1, 1; 1, 3; 1, 7, 1; 1, 15, 5; 1, 31, 18, 1.
