---
title: Parallelogram polyomino - Dyck word bijection (β)
category: Concepts
summary: Delest-Viennot's β reads a Dyck word's peak heights as column heights and its trough heights as column overlaps, giving a bijection from Dyck words of length 2n onto parallelogram polyominoes of perimeter 2n+2 with area = sum of peak heights and width = number of peaks. It is the area-preserving bijection behind the Pólya/Gessel q-Catalan and a bijective Narayana.
tags: [concept, bijection, dyck-words, parallelogram-polyomino, area, q-catalan, narayana, peaks, q-analog]
sources: [algebraic-languages-and-polyominoes-enumeration]
created: 2026-09-22
updated: 2026-09-22
---

# Parallelogram polyomino - Dyck word bijection (β)

## Description

A **parallelogram polyomino** has a boundary made of two North/East lattice paths with the same endpoints that meet only at those endpoints. Equivalently, every line perpendicular to the main diagonal meets it in one segment.[^1] Those with perimeter `2n+2` are counted by the Catalan number `C_n`.[^2]

Delest and Viennot's bijection β goes through the Dyck word's **peaks** (factors `xx̄`) and **troughs** (factors `x̄x`). Suppose a Dyck word `w` of length `2n` has `k` peaks. It then has `k-1` troughs. Let `a_i` be the height of the `i`th peak (the level the path reaches) and `b_i` the height of the `i`th trough. The paper defines trough height as `δ(f)` for `w = f x̄ x g`, which is one more than the level of the path's low point. These satisfy `1 ≤ b_i ≤ a_i` and `b_i ≤ a_{i+1}`.[^3] Build `k` vertical strips of `a_1, ..., a_k` cells. Glue strip `i+1` to the right of strip `i` so that its bottom `b_i` cells sit against the top `b_i` cells of strip `i`. The result is a parallelogram polyomino `β(w)`, with perimeter `Σ_i (2 + 2a_i - b_i - b_{i-1})` (`b_0 = b_k = 0`), which equals `|w| + 2`.[^4] The inverse μ reads a polyomino's column heights `a_i` and adjacent-column contacts `b_i`. It writes `w = u_1 v_1 ... u_k v_k`, where each `u_i` is a run of `x` climbing to level `a_i` and each `v_i` is a run of `x̄` descending to the next trough. So between peaks `i` and `i+1` the path descends `1 + a_i - b_i` and climbs `1 + a_{i+1} - b_i`.[^5]

The statistics carried across:[^6]

| polyomino | Dyck word |
|---|---|
| perimeter `2n+2` | length `2n` |
| **area** | **sum of peak heights** `Σ a_i` |
| width (number of columns) | number of peaks `k` |
| column heights / contacts | peak heights / trough heights |
| legs `l = |W W'|`, `r = |E E'|` | longest initial `x`-run, longest final `x̄`-run |

Width-`k` parallelogram polyominoes of perimeter `2n+2` number `(1/n)C(n,k)C(n,k-1)`, the Narayana number `N(n,k)`. Delest and Viennot obtain this as a 2 × 2 Gessel-Viennot binomial determinant, and it transfers through β to Kreweras's count of Dyck words with `k` peaks.[^7] The legs have the joint distribution `a_{n,i,j} = C(2n-i-j-2, n-j-1) - C(2n-i-j-2, n-1)`, by André's reflection principle.[^8] β also has a binary-tree description, through the prefix and symmetric orders and the "right height" of vertices, which Delest and Viennot attribute to Viennot's up-down-sequence work.[^9] The older bijection γ goes through 2-colored Motzkin words. It reads the two boundary paths in lockstep across anti-diagonals and records the pair of step types (`x, x̄, b, r`), then inflates by `h(x)=xx, h(x̄)=x̄x̄, h(b)=xx̄, h(r)=x̄x`.[^10] γ preserves the Catalan count but not the area, and it does not fit the gluing needed for convex polyominoes. That is why β was introduced.[^11]

**Verified during ingest:** brute-force enumeration of parallelogram polyominoes by column intervals matches the joint distribution (Σ peak heights, #peaks) over Dyck words of length `2n` exactly, for `n = 1..7` (totals 1, 2, 5, 14, 42, 132, 429).

## Castle relevance

- **The Q Department's area-preserving bijection.** β turns area, a two-dimensional statistic, into a word statistic. So the Pólya/Gessel q-Catalan of [[q-catalan-numbers](pages/q-catalan-numbers.md)] ("parallelogram polyominoes by area") is the same as Dyck words graded by Σ peak heights. It is the "bijections that keep the area" crossover (Q/R), done in 1984 for the neighboring class.
- **Column heights as peaks.** For a castle, the skyline `c_1..c_w` is the whole shape and each block sits on its parent. In β, the parallelogram's column heights are the peak heights and the column overlaps are the trough heights. Both encodings read a column-convex polyomino column by column as one number per column plus one contact per adjacent pair. This parallel is own reasoning, not the paper's.
- **A bijective Narayana.** The tower block-count identity `T(w,b) = Σ_k N(w,k) C(b+w-k, w-1)` on [[tower-narayana-polynomial](pages/tower-narayana-polynomial.md)] is refined by descents, not peaks: towers with `k-1` descents give the `k`-th term (verified `w, b ≤ 7`, [[narayana-numbers](pages/narayana-numbers.md)]). Via β, `N(w,k)` also counts width-`k` parallelogram polyominoes of semi-perimeter `w+1`, so a bijection that sends tower descents to parallelogram width, plus a weak composition, would explain the identity.
- **Contrast with the convex-castle binomial.** Parallelogram polyominoes are Catalan because their two boundary paths are coupled by non-crossing. Convex castles are binomial because the castle has one free boundary path over a flat base. This is the same divide described on [[convex-castle-binomial-identity](pages/convex-castle-binomial-identity.md)].

## Appearances in Sources

- [[algebraic-languages-and-polyominoes-enumeration](pages/algebraic-languages-and-polyominoes-enumeration.md)]: §4 defines β and μ, with Prop 4.1 and Remarks 4.2-4.5. It is the middle piece of the convex-polyomino coding.

## Related Concepts

- [[dyck-words](pages/dyck-words.md)]: the domain. Area here is the Σ-peak-heights statistic, not the inversion number.
- [[q-catalan-numbers](pages/q-catalan-numbers.md)]: the area-graded count this bijection makes a word statistic.
- [[narayana-numbers](pages/narayana-numbers.md)], [[tower-narayana-polynomial](pages/tower-narayana-polynomial.md)]: width = peaks.
- [[catalan-numbers](pages/catalan-numbers.md)], [[motzkin-numbers](pages/motzkin-numbers.md)]: the counts, and the 2-colored Motzkin route γ.
- [[steep-polyominoes-q-motzkin-bessel](pages/steep-polyominoes-q-motzkin-bessel.md)]: the steep sub-family of parallelogram polyominoes, where the area GF is a q-Bessel ratio.
- [[column-convex-polygon-enumeration](pages/column-convex-polygon-enumeration.md)]: parallelograms by area and perimeter through the add-a-column method.
- [[stack-polyomino-gf](pages/stack-polyomino-gf.md)]: the other trisection piece (stacks = convex castles).

## Footnotes

[^1]: [[algebraic-languages-and-polyominoes-enumeration](pages/algebraic-languages-and-polyominoes-enumeration.md)] p.178 - "a parallelogram polyomino is a polyomino such that the intersection with every line perpendicular to the main diagonal is a connected segment. It can also be characterized with the border formed with two paths, having only East and North elementary steps, having the same initial and final points, and being disjoint except at the extreme points."
[^2]: [[algebraic-languages-and-polyominoes-enumeration](pages/algebraic-languages-and-polyominoes-enumeration.md)] p.180 Lemma 3.1 - "The number of parallelogram polyominoes with perimeter 2n+2 is the Catalan number C_n = [1/(n+1)]C(2n,n)."
[^3]: [[algebraic-languages-and-polyominoes-enumeration](pages/algebraic-languages-and-polyominoes-enumeration.md)] p.182 §4 (19)-(21) [synthesis] - peaks `xx̄`, troughs `x̄x`, peak height `1 + δ(f)`, trough height `δ(f)` with `δ(f) = |f|_x - |f|_x̄`, sequences `a(w), b(w)` satisfying `1 ≤ b_i ≤ a_i` and `1 ≤ b_i ≤ a_{i+1}`.
[^4]: [[algebraic-languages-and-polyominoes-enumeration](pages/algebraic-languages-and-polyominoes-enumeration.md)] pp.182-183 §4, Fig. 8, (22) [synthesis] - strips of `a_i` cells glued so "the first b_i cells of the (i+1)st strip are 'glued' to the last b_i cells of the ith strip"; perimeter `Σ (2 + 2a_i - b_i - b_{i-1})`, "equal to the length of the Dyck word w, increased by 2."
[^5]: [[algebraic-languages-and-polyominoes-enumeration](pages/algebraic-languages-and-polyominoes-enumeration.md)] p.183 (23) [synthesis] - μ: `a_i` = cells of the ith strip, `b_i` = the common border of strips i and i+1, and `u_i = x^{1+a_i-b_{i-1}}`, `v_i = x̄^{1+a_i-b_i}` (read with the trough-height convention of (19); the run lengths in the text above are derived from that convention during ingest).
[^6]: [[algebraic-languages-and-polyominoes-enumeration](pages/algebraic-languages-and-polyominoes-enumeration.md)] p.183 Prop 4.1 and Remark 4.2 [synthesis] - "The area of P is the sum of the height of the peaks"; the double distribution (l, r) of the legs is the same for polyominoes and Dyck words; width = number of strips = number of peaks by construction.
[^7]: [[algebraic-languages-and-polyominoes-enumeration](pages/algebraic-languages-and-polyominoes-enumeration.md)] p.184 Remark 4.4 - "the number b_{n,k} of parallelogram polyominoes with perimeter 2n+2 and width k is given by the 2 × 2 determinant ... equal to (1/n)C(n,k)C(n,k-1) and using Proposition 4.1, we deduce the well-known formula for the number of Dyck words of length 2n having k peaks (see, for example, Kreweras [22])."
[^8]: [[algebraic-languages-and-polyominoes-enumeration](pages/algebraic-languages-and-polyominoes-enumeration.md)] pp.183-184 Remark 4.3 eq (24) - "Using the classical 'André's reflexion principle' ... a_{n,i,j} = C(2n-i-j-2, n-j-1) - C(2n-i-j-2, n-1)."
[^9]: [[algebraic-languages-and-polyominoes-enumeration](pages/algebraic-languages-and-polyominoes-enumeration.md)] pp.184-185 Remark 4.5, Fig. 9 [synthesis] - β re-described through the complete binary tree of the reversed Dyck word, prefix and symmetric order, and right heights; "It can be proved that this map w → P is a bijection, identical to β," with reference to Viennot [41].
[^10]: [[algebraic-languages-and-polyominoes-enumeration](pages/algebraic-languages-and-polyominoes-enumeration.md)] p.179 (14)-(15) - the lockstep word over `{x, x̄, b, r}` between the lines Δ_i and Δ_{i+1}, "w is a 2-colored Motzkin word," and "h(x) = xx, h(x̄) = x̄x̄, h(b) = xx̄, h(r) = x̄x."
[^11]: [[algebraic-languages-and-polyominoes-enumeration](pages/algebraic-languages-and-polyominoes-enumeration.md)] p.181 - "with the above coding γ between parallelogram polyominoes and Dyck words, this 'gluing' process would lead to non-algebraic languages ... We are going to give a more elaborate bijection between parallelogram polyominoes and Dyck words, which will fit very well with our 'gluing' problem."
