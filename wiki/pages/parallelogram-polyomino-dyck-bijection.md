---
title: Parallelogram polyomino - Dyck word bijection (β)
category: Concepts
summary: Delest and Viennot's bijection β sends a Dyck word of length 2n with k peaks to a parallelogram polyomino of perimeter 2n + 2 and width k, whose column heights are the peak heights and whose column overlaps are the trough heights (the level of the trough's low point plus one). Area is the sum of the peak heights, so β carries parallelogram polyominoes by area (A006958) onto Dyck words by the sum of their peak heights, and the Narayana count by width onto the count by peaks. Given the peak heights a_1, …, a_k, each trough height ranges independently over 1, …, min(a_i, a_{i+1}), which is the kernel min{m, n} of Klarner and Rivest.
tags: [concept, bijection, dyck-words, parallelogram-polyomino, area, q-catalan, narayana, peaks, q-analog]
sources: [algebraic-languages-and-polyominoes-enumeration]
created: 2026-09-22
updated: 2026-10-16
---

# Parallelogram polyomino - Dyck word bijection (β)

## The bijection

A **parallelogram polyomino** is a polyomino whose boundary consists of two lattice paths of North and East steps with the same endpoints that meet only at those endpoints; equivalently, every line perpendicular to the main diagonal meets it in one segment.[^1] Column by column, its columns `[b_1, t_1], …, [b_k, t_k]` have weakly increasing bottoms and tops, and consecutive columns share at least one row. Those of perimeter `2n + 2` number the Catalan number `C_n`.[^2]

A Dyck word of length `2n` in the letters `x` (up) and `x̄` (down) is read as a path from level 0. Its **peaks** are the factors `x x̄` and its **troughs** the factors `x̄ x`; a word with `k` peaks has `k − 1` troughs. Write `a_i` for the level at the top of the `i`-th peak. The paper defines the height of the trough in `w = f x̄ x g` as `δ(f)`, the level after `f`, which is one more than the level of the trough's low point; write `b_i` for the height of the `i`-th trough. Then `1 ≤ b_i ≤ min(a_i, a_{i+1})`.[^3]

β builds `k` columns of `a_1, …, a_k` cells and glues column `i + 1` to the right of column `i` so that its bottom `b_i` cells lie against the top `b_i` cells of column `i`. The result `β(w)` is a parallelogram polyomino whose consecutive columns share exactly `b_i` rows. Its perimeter is `Σ_i (2 + 2a_i − b_i − b_{i−1})` with `b_0 = b_k = 0`, which is `2n + 2`.[^4] The inverse μ reads the column heights `a_i` and the overlaps `b_i` of a parallelogram polyomino and writes the Dyck word that climbs `a_1` to the first peak, descends `1 + a_i − b_i` and climbs `1 + a_{i+1} − b_i` between peaks `i` and `i + 1`, and descends `a_k` after the last peak.[^5]

*Example.* The word `x x̄ x x x̄ x̄` has peaks at levels 1 and 2 and one trough, whose low point is at level 0, so `b_1 = 1`. β gives a column of 1 cell and a column of 2 cells sharing their bottom row: the L-tromino with its foot on the left, of area `1 + 2 = 3`, width 2 and perimeter `8 = 6 + 2`.

The statistics carried across:[^6]

| parallelogram polyomino | Dyck word |
|---|---|
| perimeter `2n + 2` | length `2n` |
| **area** | **sum of peak heights** `Σ a_i` |
| width (number of columns) | number of peaks `k` |
| column heights, overlaps of consecutive columns | peak heights, trough heights |
| heights `l`, `r` of the first and last columns (the paper's legs) | lengths of the first run of `x` and the last run of `x̄` |

The parallelogram polyominoes of perimeter `2n + 2` and width `k` number `(1/n) C(n, k) C(n, k − 1)`, the Narayana number `N(n, k)`. Delest and Viennot obtain it as a `2 × 2` Gessel-Viennot binomial determinant, and through β it gives Kreweras's count of the Dyck words with `k` peaks.[^7] By André's reflection principle, the Dyck words of length `2n` whose first run of `x` has length `i` and whose last run of `x̄` has length `j` number `C(2n − i − j − 2, n − j − 1) − C(2n − i − j − 2, n − 1)` for `(i, j) ≠ (n, n)`; the one word `x^n x̄^n` is the exception.[^8] β also has a description through binary trees, by the prefix and symmetric orders and the right heights of vertices, which Delest and Viennot attribute to Viennot.[^9]

The older bijection γ goes through 2-colored Motzkin words: it reads the two boundary paths in step across anti-diagonals, records the pair of step types in the letters `x, x̄, b, r`, and inflates by `h(x) = xx`, `h(x̄) = x̄x̄`, `h(b) = xx̄`, `h(r) = x̄x`.[^10] It is a bijection onto the Dyck words but does not carry the area, and the paper introduces β because gluing pieces coded by γ would give non-algebraic languages for convex polyominoes.[^11]

Every claim of this section was checked on all Dyck words of length at most 14.[^12]

## The kernel min{m, n}

**Proposition.** The Dyck words of any length with peak heights `a_1, …, a_k` number `Π_{i=1}^{k−1} min(a_i, a_{i+1})`, and so do the parallelogram polyominoes with column heights `a_1, …, a_k`.

*Proof.* Gluing column `i + 1` to column `i` with an overlap `b_i` gives a parallelogram polyomino for every `b_i` in `1, …, min(a_i, a_{i+1})`, and every parallelogram polyomino with these column heights arises once, so the overlaps range independently over these values. β is a bijection that keeps the column heights as peak heights.

For example, the peak heights `3, 3` give the three words `x³x̄xx̄³`, `x³x̄²x²x̄³` and `x³x̄³x³x̄³`, with `b_1 = 3, 2, 1`, and the three polyominoes made of two columns of 3 cells sharing 3, 2 or 1 rows. Klarner and Rivest count parallelograms by rows with the kernel `f(m, n) = min{m, n}`, the number of ways to place a row of `n` cells on a row of `m` cells ([[klarner-rivest-1974-convex-n-ominoes](pages/klarner-rivest-1974-convex-n-ominoes.md)]); the Proposition is the same count by columns. Summing `Π min(a_i, a_{i+1})` over the compositions of `n` gives the parallelogram polyominoes of area `n`, A006958(n): `1, 2, 4, 9, 20, 46, 105, …`, through `n = 20`.[^12] Bousquet-Mélou and Fédou give their generating function by width, height and area as `y J_1/J_0` ([[bousquet-melou-fedou-1995-convex-polyominoes](pages/bousquet-melou-fedou-1995-convex-polyominoes.md)]).

## Castle relevance

- **Area as a word statistic.** Through β, the Pólya-Gessel q-Catalan numbers of [[q-catalan-numbers](pages/q-catalan-numbers.md)], the parallelogram polyominoes by area, are the Dyck words graded by the sum of their peak heights. [[castle-q-bessel-closed-form](pages/castle-q-bessel-closed-form.md)] writes the castles by width, blocks and area through the same parallelogram series.
- **Narayana numbers.** `N(L, k)` counts the parallelogram polyominoes of semi-perimeter `L + 1` and width `k`, the Dyck words of length `2L` with `k` peaks, and appears in the tower count by blocks `T̂(L, b) = Σ_k N(L, k) C(b + L − k, L − 1)`, whose `k`-th term counts the towers with `k − 1` descents (computed; [[narayana-numbers](pages/narayana-numbers.md)], [[tower-narayana-polynomial](pages/tower-narayana-polynomial.md)]).
- **Parallelograms and convex castles.** The convex castles are the stack polyominoes, which Delest and Viennot code by Fibonacci words, while the middle piece of a convex polyomino is a parallelogram coded through β ([[algebraic-languages-and-polyominoes-enumeration](pages/algebraic-languages-and-polyominoes-enumeration.md)], [[convex-polyomino](pages/convex-polyomino.md)]).

## Appearances in Sources

- [[algebraic-languages-and-polyominoes-enumeration](pages/algebraic-languages-and-polyominoes-enumeration.md)] - §4: the definitions of β and μ, Proposition 4.1 and Remarks 4.2-4.5; β codes the middle piece of a convex polyomino.

## Related Concepts

- [[dyck-words](pages/dyck-words.md)] - the domain of β; area here is the sum of the peak heights, not the number of inversions.
- [[q-catalan-numbers](pages/q-catalan-numbers.md)] - the parallelogram polyominoes by area, the count that β makes a word statistic.
- [[narayana-numbers](pages/narayana-numbers.md)], [[tower-narayana-polynomial](pages/tower-narayana-polynomial.md)] - width and number of peaks, and the tower count by blocks.
- [[catalan-numbers](pages/catalan-numbers.md)], [[motzkin-numbers](pages/motzkin-numbers.md)] - the Catalan count, and the 2-colored Motzkin words of γ.
- [[steep-polyominoes-q-motzkin-bessel](pages/steep-polyominoes-q-motzkin-bessel.md)] - the steep parallelogram polyominoes, whose generating function by width, perimeter and area is a quotient of two q-Bessel functions.
- [[column-convex-polygon-enumeration](pages/column-convex-polygon-enumeration.md)] - the parallelogram polyominoes by area and perimeter through the add-a-column method (Theorem 3.2).
- [[prellberg-brak-1995-cluster-models](pages/prellberg-brak-1995-cluster-models.md)] - the staircase (parallelogram) polygons from the quadratic equation (3.14), linearized by `G = α H(qx)/H(x) − b(x)` (4.2).
- [[stack-polyomino-gf](pages/stack-polyomino-gf.md)] - the stack polyominoes, the end pieces of the convex polyominoes.
- [[klarner-rivest-1974-convex-n-ominoes](pages/klarner-rivest-1974-convex-n-ominoes.md)] - the parallelograms by area through the kernel `min{m, n}` and the q-series (19); [[bender-1974-convex-n-ominoes](pages/bender-1974-convex-n-ominoes.md)] - the same count as `P_1/(1 − P_2)`.
- [[bousquet-melou-fedou-1995-convex-polyominoes](pages/bousquet-melou-fedou-1995-convex-polyominoes.md)] - the generating function `y J_1/J_0` by width, height and area.

## Footnotes

[^1]: [[algebraic-languages-and-polyominoes-enumeration](pages/algebraic-languages-and-polyominoes-enumeration.md)] p.178 - "a parallelogram polyomino is a polyomino such that the intersection with every line perpendicular to the main diagonal is a connected segment. It can also be characterized with the border formed with two paths, having only East and North elementary steps, having the same initial and final points, and being disjoint except at the extreme points." (The paper's PDF is not on disk; this and the following quotations are from its source page.)
[^2]: [[algebraic-languages-and-polyominoes-enumeration](pages/algebraic-languages-and-polyominoes-enumeration.md)] p.180 Lemma 3.1 - "The number of parallelogram polyominoes with perimeter 2n+2 is the Catalan number C_n = [1/(n+1)]C(2n,n)."
[^3]: [[algebraic-languages-and-polyominoes-enumeration](pages/algebraic-languages-and-polyominoes-enumeration.md)] p.182 §4 (19)-(21) [synthesis] - peaks `xx̄`, troughs `x̄x`, peak height `1 + δ(f)`, trough height `δ(f)` with `δ(f) = |f|_x − |f|_x̄`, sequences `a(w), b(w)` satisfying `1 ≤ b_i ≤ a_i` and `1 ≤ b_i ≤ a_{i+1}`.
[^4]: [[algebraic-languages-and-polyominoes-enumeration](pages/algebraic-languages-and-polyominoes-enumeration.md)] pp.182-183 §4, Fig. 8, (22) [synthesis] - strips of `a_i` cells glued so "the first b_i cells of the (i+1)st strip are 'glued' to the last b_i cells of the ith strip"; perimeter `Σ (2 + 2a_i − b_i − b_{i−1})`, "equal to the length of the Dyck word w, increased by 2."
[^5]: [[algebraic-languages-and-polyominoes-enumeration](pages/algebraic-languages-and-polyominoes-enumeration.md)] p.183 (23) [synthesis] - μ: `a_i` the cells of the `i`-th strip, `b_i` the common border of strips `i` and `i + 1`, and the word `u_1 v_1 ⋯ u_k v_k` with `u_i` a run of `x` and `v_i` a run of `x̄`. The run lengths stated here reconstruct every Dyck word of length at most 14 from its peak and trough heights.[^12]
[^6]: [[algebraic-languages-and-polyominoes-enumeration](pages/algebraic-languages-and-polyominoes-enumeration.md)] p.183 Prop 4.1 and Remark 4.2 [synthesis] - "The area of P is the sum of the height of the peaks"; the double distribution `(l, r)` of the legs is the same for polyominoes and Dyck words; width = number of strips = number of peaks by construction.
[^7]: [[algebraic-languages-and-polyominoes-enumeration](pages/algebraic-languages-and-polyominoes-enumeration.md)] p.184 Remark 4.4 - "the number b_{n,k} of parallelogram polyominoes with perimeter 2n+2 and width k is given by the 2 × 2 determinant ... equal to (1/n)C(n,k)C(n,k-1) and using Proposition 4.1, we deduce the well-known formula for the number of Dyck words of length 2n having k peaks (see, for example, Kreweras [22])."
[^8]: [[algebraic-languages-and-polyominoes-enumeration](pages/algebraic-languages-and-polyominoes-enumeration.md)] pp.183-184 Remark 4.3 eq (24) - "Using the classical 'André's reflexion principle' ... a_{n,i,j} = C(2n-i-j-2, n-j-1) - C(2n-i-j-2, n-1)." The exception at `(i, j) = (n, n)` is from the enumeration.[^12]
[^9]: [[algebraic-languages-and-polyominoes-enumeration](pages/algebraic-languages-and-polyominoes-enumeration.md)] pp.184-185 Remark 4.5, Fig. 9 [synthesis] - β re-described through the complete binary tree of the reversed Dyck word, prefix and symmetric order, and right heights; "It can be proved that this map w → P is a bijection, identical to β," with reference to Viennot [41].
[^10]: [[algebraic-languages-and-polyominoes-enumeration](pages/algebraic-languages-and-polyominoes-enumeration.md)] p.179 (14)-(15) - the lockstep word over `{x, x̄, b, r}` between the lines Δ_i and Δ_{i+1}, "w is a 2-colored Motzkin word," and "h(x) = xx, h(x̄) = x̄x̄, h(b) = xx̄, h(r) = x̄x."
[^11]: [[algebraic-languages-and-polyominoes-enumeration](pages/algebraic-languages-and-polyominoes-enumeration.md)] p.181 - "with the above coding γ between parallelogram polyominoes and Dyck words, this 'gluing' process would lead to non-algebraic languages ... We are going to give a more elaborate bijection between parallelogram polyominoes and Dyck words, which will fit very well with our 'gluing' problem."
[^12]: Verified by execution (Python 3.11, 2026-10-16): for every Dyck word of length `2n ≤ 14`, β gives a parallelogram polyomino with area `Σ a_i`, width `k` and perimeter `2n + 2`, β is a bijection onto the parallelogram polyominoes of semi-perimeter `n + 1` (enumerated by columns), `1 ≤ b_i ≤ min(a_i, a_{i+1})`, the width counts are `N(n, k)`, the run lengths of μ reconstruct the word, and the reflection-principle formula holds for all `(i, j) ≠ (n, n)`; `Σ Π min(a_i, a_{i+1})` over compositions gives A006958 through `n = 20`, ending at 5526198 (OEIS data checked 2026-10-16).
