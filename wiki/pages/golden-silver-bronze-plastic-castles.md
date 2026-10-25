---
title: Golden, silver, bronze and plastic growth of castles
category: Analyses
summary: The four constants golden φ, silver 1 + √2, bronze (3 + √13)/2 and plastic ψ (real root of x³ = x + 1) side by side on every axis where a castle family or a single castle can carry a growth constant or spectral radius - width, area, semi-perimeter, adjacency spectrum, the signed transfer matrix. All four are width growth constants. By area only golden and plastic can occur, because every class of castles grows at most 2 by area. By adjacency spectrum plastic cannot occur, because ψ has complex conjugates and a graph's eigenvalues are real. New plastic families, each counted exactly by the Padovan numbers A000931 like the existing maximal castles - the (1, 2)-RLL castles by width, the ridge castles of height 2 by area, and the height-3 rule 1 → 2 → 3 → {1, 2} by width. At height 2 one table shows all three gradings - all castles, Fibonacci castles and ridge castles by width, area and semi-perimeter - with golden, plastic, supergolden and ψ² as the entries. φ and ψ are the smallest width growth constants above 1 at heights 2 and 3.
tags: [analysis, castle, metallic-means, golden-ratio, silver-ratio, bronze, plastic-number, padovan, growth-constant, width, area, semi-perimeter, spectral-radius, run-length-limited, ridge-castle, classification, totally-real, oeis, sympy, verification]
sources: [project-euler-502]
created: 2026-10-10
updated: 2026-10-25
---

# Golden, silver, bronze and plastic growth of castles

## The question

"Golden castle" means nothing until it says what is golden. A **family** of castles can grow at the golden rate when counted by width, by area or by semi-perimeter, and a **single** castle can have the golden mean as the largest eigenvalue of its cell graph. These are different statements about different objects, and a constant can be possible on one axis and impossible on another. This page puts four constants side by side on each axis:

| constant | value | minimal polynomial | other roots |
|---|---|---|---|
| golden `φ = δ_1` | `1.6180` | `x² − x − 1` | `−0.618` |
| silver `δ_2 = 1 + √2` | `2.4142` | `x² − 2x − 1` | `−0.414` |
| bronze `δ_3 = (3 + √13)/2` | `3.3028` | `x² − 3x − 1` | `−0.303` |
| plastic `ψ` | `1.3247` | `x³ − x − 1` | `−0.662 ± 0.562i` |

The first three are the metallic means ([[metallic-means](pages/metallic-means.md)]); `ψ` is the real root of `x³ = x + 1` ([[plastic-number](pages/plastic-number.md)]). All four are algebraic integers greater than 1 whose other roots lie inside the unit circle. The difference that matters below is that the metallic means have real conjugates and `ψ` does not.

## Terms used on this page

- **`c` by a size** - a family of castles is `c` by width, by area or by semi-perimeter when its count, graded by that size, grows like `c^n` ([[castle-classification-growth](pages/castle-classification-growth.md)]). The size `n` is one of:
  - **width** `w`, at a fixed height `h`;
  - **area**, the number of cells `c_1 + ⋯ + c_w`;
  - **semi-perimeter** `s = w + #blocks`, half the perimeter of the castle polygon ([[castle-perimeter](pages/castle-perimeter.md)]). Reading left to right, the block count adds `max(0, c_i − c_{i−1})` at each column (with `c_0 = 0`), so a column of height `b` after one of height `a` adds `1 + max(0, b − a)` to `s`.
- **Spectrum castle** - a single castle whose cell graph (cells joined when they share an edge) has the constant as its largest adjacency eigenvalue ([[castle-classification-spectrum](pages/castle-classification-spectrum.md)]).
- **Rule** - a 0/1 table saying which column height may follow which ([[castle-strip](pages/castle-strip.md)]); written `a → {b, …}`.

## The grid

| axis | golden | silver | bronze | plastic |
|---|---|---|---|---|
| width | Fibonacci castles; ridge castles, `h = 2` | Pell castles; ridge castles, `h = 3` | ridge castles, `h = 4` | maximal castles; **`(1, 2)`-RLL castles; the rule `1 → 2 → 3 → {1, 2}`, `h = 3`** |
| area | all castles of height 2; prime castles | **impossible** | **impossible** | **ridge castles, `h = 2`**; palindromic tree castles; prime castles of height 3 |
| semi-perimeter | castles with every column 1 or 3 | **a height-5 rule (601 of `2^25`)** | **impossible below height 22**; open | **every column 1 or 9**; a height-3 rule |
| adjacency spectrum | the six 4-cell paths | 36 castles up to mirror image | open | **impossible** |
| signed transfer matrix of Project Euler 502 (PE 502) | never | never | never | `2ψ²` at tower height `k = 6` |

Bold entries are new on this page. The sections below give each entry its rule, an example and its count.

## Width

| constant | family | rule | example | count at width `w` |
|---|---|---|---|---|
| golden | Fibonacci castles ([[fibonacci-castle](pages/fibonacci-castle.md)]) | height 2, no two adjacent height-2 columns | `(2, 1, 2, 1, 1)` | `F_{w+2} − 1` |
| golden | ridge castles of height 2 ([[ridge-castle](pages/ridge-castle.md)]) | height 2, no two adjacent height-1 columns | `(2, 1, 2, 2, 1)` | `F_{w+2}` (`w ≥ 2`) |
| silver | Pell castles ([[pell-castle](pages/pell-castle.md)]) | first column 1, neighbors differ by at most 1, reaches 3 | `(1, 2, 3, 2)` | `P⋆_w − 2^{w−1}` |
| silver | ridge castles of height 3 | neighbors differ unless both are 3 | `(1, 3, 3, 2)` | `1, 5, 15, 39, 97, …` |
| bronze | ridge castles of height 4 | neighbors differ unless both are 4 | `(4, 4, 1, 3)` | `1, 7, 31, 118, 421, …` |
| plastic | maximal castles ([[fibonacci-castles-sub-families](pages/fibonacci-castles-sub-families.md)]) | height 2, height-2 columns separated by one or two height-1 columns, at most one height-1 column at each end | `(2, 1, 1, 2, 1)` | `A000931(w + 6)` |
| **plastic** | **`(1, 2)`-RLL castles** | height 2, height-2 columns separated by one or two height-1 columns, at most two height-1 columns at each end | `(2, 1, 2, 1, 1, 2)` | `A000931(w + 8)` (`w ≥ 3`) |
| **plastic** | **the rule `1 → 2 → 3 → {1, 2}`** | height 3, each column one higher than the last, except after a 3, which drops to 1 or 2 | `(1, 2, 3, 2, 3, 1, 2, 3)` | `A000931(w + 4)` with first column 1 (`w ≥ 3`) |

**The `(1, 2)`-RLL castles.** In the run-length-limited family of [[fibonacci-castles-sub-families](pages/fibonacci-castles-sub-families.md)], a `(d, k)`-RLL castle is a Fibonacci castle whose tower (the 0/1 row of height-2 positions) has runs of 0s of length at least `d` between 1s and at most `k` everywhere. Golden is `(1, ∞)`, all Fibonacci castles, and supergolden is `(1, 3)`. At `(1, 2)` the Marcus-Roth-Siegel growth equation `z^{k+2} − z^{k+1} − z^{k−d+1} + 1 = 0` is `z⁴ − z³ − z² + 1 = (z − 1)(z³ − z − 1)`, whose largest root is `ψ`.[^mrs] These are the maximal castles of [[fibonacci-castles-sub-families](pages/fibonacci-castles-sub-families.md)] (gaps 1 or 2, end runs at most 1, the maximal independent sets of the path) with the end runs allowed to reach 2. The counts by width are `1, 2, 4, 5, 7, 9, 12, 16, 21, 28, 37, 49, …`, the Padovan numbers `A000931(w + 8)` from `w = 3` on, two steps ahead of the maximal castles' `A000931(w + 6)`; `(2, 1, 1, 1, 2)` is neither (a gap of three).[^exec]

**The rule `1 → 2 → 3 → {1, 2}`.** Its table has two cycles, `1 → 2 → 3 → 1` of length 3 and `2 → 3 → 2` of length 2, so its characteristic polynomial is `x³ − x − 1`. Started at height 1 and required to reach 3, it gives `0, 0, 1, 2, 2, 3, 4, 5, 7, 9, 12, …` castles, the Padovan numbers `A000931(w + 4)`; with any first column it gives `1, 3, 5, 7, 9, 12, 16, …`, which is `A000931(w + 9)` from `w = 3` on.[^exec] `(1, 2, 3, 3)` is not one (3 cannot follow 3).

**Smallest constants.** On [[area-growth-census](pages/area-growth-census.md)] it is proved that every 0/1 table on `n` states whose growth exceeds 1 grows at least at the largest root of `x^n − x − 1`. A width rule at height `h` is a table on `h` states, so the smallest width growth constant above 1 at height `h` is the root of `x^h = x + 1`: the lemma bounds it from below, and the rule `1 → 2 → ⋯ → h → 1` with the extra step `h → 2`, with characteristic polynomial `x^h − x − 1`, attains it.[^exec] Golden at height 2 and plastic at height 3, where this is the rule above, are the first two entries of that sequence.

**Minimum heights.** Golden first appears at height 2, silver and plastic at 3, bronze at 4 ([[quadratic-min-height](pages/quadratic-min-height.md)], [[reachable-field-census](pages/reachable-field-census.md)]).

## Area

**No family of castles is silver or bronze by area.** A castle of area `n` is a composition of `n` (its column heights in order), so there are `2^{n−1}` castles of area `n` in all, and every family of castles grows at most 2 by area. Silver `2.414` and bronze `3.303` exceed 2. Golden and plastic, both below 2, occur:

| constant | family | rule | example | count at area `A` |
|---|---|---|---|---|
| golden | all castles of height 2 ([[castles-of-height-h-by-area](pages/castles-of-height-h-by-area.md)]) | columns 1 and 2, some 2 | `(1, 2, 1)` | `F_{A+1} − 1` |
| golden | prime castles ([[prime-castles](pages/prime-castles.md)]) | no column of height 1 | `(2, 3)` | `F_{A−1}` |
| **plastic** | **ridge castles of height 2** | no two adjacent height-1 columns, some 2 | `(2, 1, 2, 2, 1)`, area 8 | `A000931(A + 5)` (`A ≥ 2`) |
| plastic | palindromic tree castles ([[castle-sequence-catalogue](pages/castle-sequence-catalogue.md)]) | no two adjacent columns both of height 2 or more (no `2 × 2` block), and the same read backwards | `(3, 1, 3)` | `A000931(A + 6)` |
| plastic | prime castles of height 3 ([[prime-castles](pages/prime-castles.md)]) | columns 2 and 3, some 3 | `(2, 3, 2)` | growth `ψ` |

The ridge castles of height 2 are golden by width and plastic by area. Their area generating function has denominator `1 − x² − x³`: a castle is a sequence of the blocks `2` (area 2) and `2 1` (area 3), ending in either, with a leading `1` allowed, which is the Padovan recurrence `a(A) = a(A − 2) + a(A − 3)`.[^exec]

## Semi-perimeter

| constant | family | example | count at semi-perimeter `s` |
|---|---|---|---|
| **golden** | **castles of height 3 with every column 1 or 3** | `(3, 1, 1, 3)`, `s = 4 + 3 + 2 = 9` | `A130578(s − 1)` |
| **plastic** | **the rule `1 → 2`, `2 → {2, 3}`, `3 → 1`, height 3** | `(1, 2, 2, 3, 1, 2)`, `s = 10` | growth `ψ` |
| `ψ²` | all castles of height 2 | `(1, 2, 1)`, `s = 5` | `A077855(s − 3)` |
| **silver** | **height 5, no 1 next to a 2, no 4 next to a 5** | `(3, 5, 3, 1, 4)`, `s = 13` | growth `1 + √2` |
| **plastic** | **height 9, every column 1 or 9** | `(1, 9, 1)`, `s = 12` | growth `ψ` |

The denominators, with `x` marking semi-perimeter, are `(1 − x − x²)(1 − x + x²)` for the `{1, 3}` castles, `(1 − x² − x³)(1 − x + x²)` for the plastic rule, and `1 − 2x + x² − x³` (reversed, `x³ − 2x² + x − 1`, the minimal polynomial of `ψ²`) for all castles of height 2.[^exec] The `{1, 3}` count is the OEIS's count of possible crossword rows, "1, 3, 6, 10, 16, 26, 43, …".[^a130578]

An exhaustive check of all rules through height 4 (65,536 tables at height 4) finds golden at height 3 (26 rules) and plastic at height 3 (10 rules), and no silver or bronze.[^census] The full census is on [[semi-perimeter-growth-census](pages/semi-perimeter-growth-census.md)]: silver semi-perimeter growth first appears at height 5, in 601 rules; castles with every column one of two heights 8 apart grow at plastic by semi-perimeter; and no family of castles of height at most 21 has bronze semi-perimeter growth, because all castles of height 21 grow at only `3.3002` by semi-perimeter.

## Adjacency spectrum

| constant | castles | status |
|---|---|---|
| golden | the six 4-cell castles `(4)`, `(1, 3)`, `(3, 1)`, `(1, 1, 2)`, `(2, 1, 1)`, `(1, 1, 1, 1)`, all the path `P_4` | complete (Smith's theorem) |
| silver | the `3 × 2` rectangle, `(1, 2, 3, 1, 2, 3)` and others; 36 up to mirror image to width 10 | known members |
| bronze | none in about `7.1 × 10^11` skylines searched; no split into five or fewer evenly connected groups can give it | open ([[bronze-castle-hunt](pages/bronze-castle-hunt.md)]) |
| **plastic** | none | **impossible** |

**No castle, and no graph at all, has spectral radius `ψ`.** A graph's adjacency matrix is a symmetric integer matrix, so all its eigenvalues are real. If `ψ` were one, its minimal polynomial `x³ − x − 1` would divide the characteristic polynomial, and the two complex roots `−0.662 ± 0.562i` would be eigenvalues too. The same argument excludes every cubic constant on the wiki: `ψ²`, supergolden and tribonacci all have complex conjugates (the discriminants of `x³ − x − 1`, `x³ − 2x² + x − 1` and `x³ − x² − 1` are `−23`, `−23` and `−31`).[^exec] The metallic means have real conjugates, so the argument does not touch them; `δ_4` and above are excluded instead by the maximum degree 4 of a castle graph ([[castle-classification-spectrum](pages/castle-classification-spectrum.md)]).

`ψ` does occur as the largest eigenvalue of a non-symmetric 0/1 table: the width rule above. A plastic constant needs a directed operator.

## The signed transfer matrix

The PE 502 signed tower count has transfer matrices whose eigenvalues are twice algebraic units ([[castle-graph-spectral-radius](pages/castle-graph-spectral-radius.md)]); none of golden, silver or bronze is ever one. Plastic enters through its square: at tower height `k = 6` the dominant eigenvalue is `ρ_6 = 2ψ²` ([[plastic-number](pages/plastic-number.md)]). On this axis plastic is the only one of the four present.

## Height 2, three gradings

At height 2 the three gradings can be compared on one set of families:

| family (height 2) | width | area | semi-perimeter |
|---|---|---|---|
| all castles | `2` (`2^w − 1`) | golden (`F_{A+1} − 1`) | `ψ²` (`A077855(s − 3)`) |
| Fibonacci castles: no two adjacent 2s | golden (`F_{w+2} − 1`) | supergolden ([[tree-castle-by-area](pages/tree-castle-by-area.md)]) | supergolden |
| ridge castles: no two adjacent 1s | golden (`F_{w+2}`) | plastic (`A000931(A + 5)`) | supergolden |

Banning `11` and banning `22` give the same growth by width, since exchanging the heights 1 and 2 swaps the two families (up to the flat row), and the same growth by semi-perimeter (both denominators are `1 − x − x³`), but different growth by area: `ψ` for the ridge castles against supergolden for the Fibonacci castles.

## Parallels

- **Width realizes all four; area and spectrum split them.** By area only constants below 2 can occur (golden, plastic); by adjacency spectrum only totally real ones can (golden, silver, bronze open). Golden is the one constant present on every axis except the signed transfer matrix.
- **Padovan for plastic, as Fibonacci for golden.** Every plastic family here - the maximal castles, the palindromic tree castles and the three new ones - is counted exactly by the Padovan numbers A000931, shifted ([[padovan-families](pages/padovan-families.md)] explains the shared core and gives the bijections), as the golden families are counted by the Fibonacci numbers. The silver Pell castles are counted by the Pell numbers less `2^{w−1}`, and the bronze ridge strips by A003688, not the bronze metallic sequence A006190 ([[proper-castle-projection](pages/proper-castle-projection.md)]).
- **Smallest versus largest.** At height 2, golden is the largest area growth constant (all castles) and plastic the smallest above 1 (the ridge rule). By width at height 3, plastic is the smallest constant above 1, and the rule realizing it is the cycle `1 → 2 → 3 → 1` with one extra step.
- **One family, two constants.** The ridge castles of height 2 are golden by width and plastic by area.

## Related Concepts

- [[metallic-means](pages/metallic-means.md)] - golden, silver, bronze and the higher rungs `δ_a`.
- [[plastic-number](pages/plastic-number.md)] - `ψ`, `ψ²` and `2ψ²` in the castle.
- [[castle-classification-growth](pages/castle-classification-growth.md)] - the growth-castle naming convention and catalogue.
- [[castle-classification-spectrum](pages/castle-classification-spectrum.md)] - spectrum castles and Smith's theorem.
- [[fibonacci-castles-sub-families](pages/fibonacci-castles-sub-families.md)] - the run-length-limited castles.
- [[ridge-castle](pages/ridge-castle.md)] - the ridge rule, golden by width at height 2.
- [[area-growth-census](pages/area-growth-census.md)] - the area census and the smallest-growth lemma.
- [[castle-perimeter](pages/castle-perimeter.md)] - the semi-perimeter grading.
- [[semi-perimeter-growth-census](pages/semi-perimeter-growth-census.md)] - every growth constant by semi-perimeter through height 4, silver at height 5, the bronze bound.

## Footnotes

[^mrs]: https://ronny.cswp.cs.technion.ac.il/wp-content/uploads/sites/54/2016/05/chapters1-9.pdf (B. H. Marcus, R. M. Roth, P. H. Siegel, "An Introduction to Coding for Constrained Systems", lecture notes, October 2001) p.74 Example 3.3 - for `0 ≤ d ≤ k < ∞`, "λ(A_G(d,k)) is the largest positive solution of the equation z^{k+2} − z^{k+1} − z^{k−d+1} + 1 = 0". The factorization at `(d, k) = (1, 2)` and the capacity `log₂ ψ = 0.4057` are computed here.
[^exec]: Verified by execution (Python 3.10, SymPy, 2026-10-10). Counts by brute force and by transfer matrix: `(1, 2)`-RLL castles for `w ≤ 18` (`1, 2, 4, 5, 7, 9, 12, 16, 21, 28, 37, 49, 65, 86, 114, 151, 200, 265`, equal to `A000931(w + 8)` for `3 ≤ w ≤ 18`); ridge castles of height 2 by area for `A ≤ 25` (`0, 1, 2, 2, 3, 4, 5, 7, 9, 12, …, 816`, equal to `A000931(A + 5)` for `2 ≤ A ≤ 25`); the rule `1 → 2 → 3 → {1, 2}` for `w ≤ 24`, first column 1 (`0, 0, 1, 2, 2, 3, …, 465`, equal to `A000931(w + 4)` for `3 ≤ w ≤ 24`) and any first column (`1, 3, 5, 7, 9, 12, …, 1897`); palindromic tree castles by area for `A ≤ 17` (`1, 2, 2, 3, 4, 5, 7, 9, 12, 16, 21, 28, 37, 49, 65, 86, 114`, equal to `A000931(A + 6)`); Padovan values from https://oeis.org/A000931/b000931.txt (offset 0, `1, 0, 0, 1, 0, 1, 1, 1, 2, 2, 3, 4, 5, 7, 9, 12, …`). Exact denominators: width `det(xI − R)` gives `x³ − x − 1` for `1 → 2 → 3 → {1, 2}` and `x² − x − 1` for the height-2 ridge rule; area `det(I − R·diag(x, x²))` gives `1 − x² − x³` for the height-2 ridge rule; semi-perimeter `det(I − M)` with `M[a][b] = x^{1 + max(0, b − a)}` gives `1 − 2x + x² − x³` (all of height 2), `1 − x − x³` (height-2 ridge and Fibonacci rules), `(1 − x − x²)(1 − x + x²)` (columns 1 or 3) and `(1 − x² − x³)(1 − x + x²)` (`1 → 2`, `2 → {2, 3}`, `3 → 1`), signs normalized. Discriminants by `sp.discriminant`: `−23`, `−23`, `−31`. Semi-perimeter counts by brute force for `s ≤ 18`: all castles of height 2 `0, 1, 3, 6, 11, 20, 36, 64, 113, 199, 350, 615, 1080, 1896, 3328, 5841, 10251` (`s = 2..18`), columns 1 or 3 `0, 0, 1, 3, 6, 10, 16, 26, 43, 71, 116, 188, 304, 492, 797, 1291, 2090`. The rule `1 → 2 → ⋯ → h → 1` with the extra step `h → 2` has characteristic polynomial `x^h − x − 1` for `h = 2..8` (SymPy, 2026-10-25).
[^census]: Verified by execution (Python 3.10, NumPy, 2026-10-10): for every 0/1 rule on `h ≤ 4` heights, the semi-perimeter growth `1/x*`, with `x*` found by bisection on the spectral radius of `M(x)[a][b] = A[a][b] · x^{1 + max(0, b − a)}` (60 halvings), compared with each constant to `10^{−7}`. Height 2: `ψ²` once (the all-ones rule). Height 3: golden 26, plastic 10, `ψ²` 36. Height 4: golden 3,669, plastic 1,940, `ψ²` 3,092. Silver and bronze: none at any height `≤ 4`. Exact rational checks of the named rules are in [^exec].
[^a130578]: https://oeis.org/A130578 (fetched 2026-10-10) - "Number of different possible rows (or columns) in an n X n crossword puzzle."; offset 1, data `0, 0, 1, 3, 6, 10, 16, 26, 43, 71, 116, 188, 304, 492, 797, 1291, 2090, …`; o.g.f. `x^3/((-1+x)*(x^2+x-1)*(x^2-x+1))`. A077855 (fetched 2026-10-10): "Expansion of 1/((1-2*x+x^2-x^3)*(1-x))", offset 0, data `1, 3, 6, 11, 20, 36, 64, 113, 199, 350, 615, 1080, 1896, 3328, 5841, 10251, …`.
