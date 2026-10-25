---
title: Viennot heaps of pieces on towers
category: Analyses
summary: Whether the block count of towers (skylines with no height bound on a base of length L) comes from Viennot heaps of pieces, as the cell count 1/(1 − x)^L does. Unit cells see only the cell count, and intervals stacked as a heap overcount (8 heaps of two pieces against 5 towers with two blocks at L = 2). Intervals that may only be nested or separated count towers exactly - sending [i, j] to the segment from vertex i − 1 to vertex j + 1 of an (L + 2)-gon turns a tower into a multiset of pairwise non-crossing diagonals, and the Narayana h-vector of the simplicial associahedron (Tzanaki) proves Σ_b T̂(L, b) x^b = Narayana_L(x)/(1 − x)^L for every L. A tower's descents are the right endpoints of its blocks, and with R(F) the longest diagonal of a triangulation F at each right endpoint, every set of non-crossing diagonals lies between R(F) and F for exactly one F, so the towers with b blocks and k − 1 descents number N(L, k) C(b + L − k, L − 1), the Narayana counterpart of Worpitzky's identity. The transfer matrix on the previous column height gives the same series as a matrix power.
tags: [analysis, tower, viennot, heap-of-pieces, commutation-monoid, trace-monoid, cartier-foata, transfer-matrix, narayana, associahedron, h-vector, noncrossing]
sources: [bousquet-melou-fedou-1995-convex-polyominoes, bayer-diaconis-1992-dovetail-shuffle, prellberg-brak-1995-cluster-models]
created: 2026-09-21
updated: 2026-10-25
---

# Viennot heaps of pieces on towers

## The question

Towers on a base of length `L` with no height bound are given by their column heights `c = (c_1, …, c_L)`, `c_i ≥ 0`, and their blocks are the maximal runs of columns with `c_i ≥ r` in each row `r` ([[tower-heap](pages/tower-heap.md)]). Write `T̂(L, b)` for the number of towers on a base of length `L` with `b` blocks; the hat separates it from the tower count `T(k, L)` ([[castle-notation](pages/castle-notation.md)]).

*Example.* At `L = 2` the towers with one block are `(1, 0)`, `(0, 1)` and `(1, 1)`, so `T̂(2, 1) = 3`.

[[tower-heap](pages/tower-heap.md)] reads towers as Viennot heaps of unit-cell pieces, and Cartier-Foata inversion gives their cell-count generating function `1/(1 − x)^L`. This page asks whether the block count comes from pieces in the same way. Unit cells do not see it, and intervals stacked as a heap overcount. Intervals that may only be nested or separated count towers exactly, and that gives the generating function by blocks for every `L` (Theorem 1) and its split by descents (Theorem 2).

## Unit cells see only the cell count

[[tower-heap](pages/tower-heap.md)] takes one piece `u_i` for each cell of column `i`, with `u_i` and `u_j` dependent exactly when `i = j`. The columns commute freely, so Cartier-Foata inversion gives the cell-count generating function `1/(1 − x)^L`.

A cell at row `r` and column `i` starts a new block exactly when `c_{i−1} < r` (with `c_0 = 0`), so whether it adds to the block count depends on the neighboring column. The block count

```
blocks(c)  =  c_1 + Σ_{i≥2} max(0, c_i − c_{i−1})
```

is not of the form `Σ_i f(c_i)`, so it is not a product of weights of the pieces, and the unit-cell Cartier-Foata inversion does not see it ([[castle-sign](pages/castle-sign.md)]).[^1]

## Interval heaps overcount

Take the pieces to be intervals `[i, j]` in `[1, L]`, with two intervals dependent when they share a column. The trivial heaps are the sets of pairwise disjoint intervals, and there are `C(L + k, 2k)` sets of `k` of them (stars and bars), so the Cartier-Foata series is `Σ_k (−1)^k C(L + k, 2k) x^k`. At `L = 2` this is `1 − 3x + x²`, whose inverse is

```
1 / (1 − 3x + x²)  =  1 + 3x + 8x² + 21x³ + 55x⁴ + …        (A001906)
```

while the towers on a base of length 2 number `T̂(2, b) = 2b + 1`: `1, 3, 5, 7, …` (A005408). The two agree at `x^0` and `x^1` and differ at `x²`, 8 heaps of two pieces against 5 towers with two blocks. A heap of intervals is not a tower in two ways: the pieces `[1, 1]` and `[2, 2]` side by side in one row are two pieces of the heap but one block `[1, 2]` of a tower, and the heap with `[1, 2]` above `[1, 1]` overhangs column 2 and is not a tower.[^2]

## Compatible blocks count towers

The blocks themselves are the right pieces, provided two of them may stand together only when they are nested or apart. Call two intervals of `[1, L]` **compatible** when one contains the other or at least one column separates them: `[i, j]` and `[i', j']` with `[i, j] ⊆ [i', j']`, `[i', j'] ⊆ [i, j]`, `j + 1 < i'` or `j' + 1 < i`.

**Lemma 1.** Listing the blocks is a bijection from the towers on a base of length `L` with `b` blocks to the multisets of `b` pairwise compatible intervals of `[1, L]`. The inverse gives column `i` the height `c_i`, the number of intervals of the multiset that contain `i`.

*Proof.* The blocks of row `r` are the maximal runs of the columns with `c_i ≥ r`. So two blocks of one row are separated by a column of height below `r`, and a block of a higher row lies inside a block of row `r`. If a block `B'` of a higher row is not inside a block `B` of row `r`, the block of row `r` that holds `B'` is separated from `B`, and so is `B'`. So the blocks are pairwise compatible, and column `i` lies in one block of each of its `c_i` rows.

Conversely, take a multiset of pairwise compatible intervals, with heights `c_i` as stated. Two intervals that share a column are nested, so the intervals containing any one column form a chain. Give each interval the depth `r` when it is the `r`-th interval of that chain counted from the outside, ordering equal copies one after another; the depth does not depend on the column chosen. Two intervals of the same depth are not nested, so they are separated, and the intervals of depth `r` cover exactly the columns with `c_i ≥ r`. So they are the maximal runs of those columns, the blocks of row `r`, and the tower with heights `c_i` has the given multiset as its blocks. ∎

**Lemma 2.** Label the vertices of a convex polygon `0, 1, …, L + 1` in order, and send the interval `[i, j]` to the segment from vertex `i − 1` to vertex `j + 1`. Two intervals are compatible exactly when their segments do not cross. The interval `[1, L]` goes to the edge from 0 to `L + 1`, and the other `L(L + 1)/2 − 1` intervals go one to one onto the `(L + 2)(L − 1)/2` diagonals.

*Proof.* Take `i ≤ i'`. If `i = i'` the intervals are nested. Otherwise they are incompatible exactly when `i' ≤ j + 1` and `j < j'`, the cases where they stand side by side or overlap, and that is exactly when the endpoints interleave, `i − 1 < i' − 1 < j + 1 < j' + 1`, so that the segments cross. The segment of `[i, j]` joins two vertices whose labels differ by `j − i + 2 ≥ 2`, which is a diagonal unless it is the edge from 0 to `L + 1`, and every such pair of vertices comes from one interval. ∎

Sets of pairwise non-crossing diagonals of the `(L + 2)`-gon form a simplicial complex `Δ_L`, whose largest faces are the triangulations, with `L − 1` diagonals each. Tzanaki identifies it with the boundary complex of the simplicial associahedron. Its **h-vector** `(h_0, …, h_d)`, with `d = L − 1`, is defined from the numbers `f_{i−1}` of faces with `i` diagonals by[^3]

```
Σ_{i=0}^{d} f_{i−1} (x − 1)^{d−i}  =  Σ_{i=0}^{d} h_i x^{d−i},
```

and Tzanaki proves `h_i = (1/(i + 1)) C(L − 1, i) C(L, i)`, which is `N(L, i + 1)` because `C(L, i + 1) = L C(L − 1, i)/(i + 1)`. Here `N(L, k) = (1/L) C(L, k) C(L, k − 1)` are the [[narayana-numbers](pages/narayana-numbers.md)] (A001263).[^3]

**Theorem 1.** For every `L ≥ 1`,

```
Σ_b T̂(L, b) x^b  =  Narayana_L(x) / (1 − x)^L,        Narayana_L(x)  =  Σ_{k=1}^{L} N(L, k) x^{k−1}.      (1)
```

*Proof.* By Lemmas 1 and 2, a tower with `b` blocks is a multiset of `b` pairwise non-crossing segments, each a diagonal of the `(L + 2)`-gon or the edge from 0 to `L + 1`, and the edge crosses nothing. A multiset whose set of distinct diagonals is the face `S` contributes `(x/(1 − x))^{|S|}`, each diagonal of `S` taken at least once, and the edge, taken any number of times, contributes `1/(1 − x)`. So

```
Σ_b T̂(L, b) x^b  =  (1/(1 − x)) Σ_{S ∈ Δ_L} (x/(1 − x))^{|S|}  =  (1/(1 − x)) Σ_{i=0}^{d} f_{i−1} (x/(1 − x))^i.
```

Replacing `x` by `1/x` in the definition of the h-vector and multiplying by `x^d` gives `Σ_i f_{i−1} (1 − x)^{d−i} x^i = Σ_i h_i x^i`, so the last sum is `Σ_i h_i x^i / (1 − x)^d`, and with `h_i = N(L, i + 1)` and `d = L − 1` the series is `Narayana_L(x)/(1 − x)^L`. At `L = 1` there is no diagonal and the series is `1/(1 − x)`, as Equation (1) says. ∎

In coefficients,

```
T̂(L, b)  =  Σ_{k=1}^{L} N(L, k) · C(b + L − k, L − 1).                         (2)
```

The rows of Equation (1) are `1/(1 − x)` at `L = 1` (one tower `(b)` with `b` blocks), `(1 + x)/(1 − x)²` at `L = 2` (`2b + 1`, A005408) and `(1 + 3x + x²)/(1 − x)³` at `L = 3` (`1, 6, 16, 31, 51, 76, …`, A005891), and `1 + 3x + x²` is row 3 of A001263.[^4]

*Example.* At `L = 2` the polygon is a square with vertices `0, 1, 2, 3`. The intervals `[1, 1]` and `[2, 2]` go to the two diagonals `(0, 2)` and `(1, 3)`, which cross, and `[1, 2]` goes to the edge `(0, 3)`. `Δ_2` is two points, with `f = (1, 2)` and `h = (1, 1)`, and the series is `(1 + x)/(1 − x)²`. The 5 towers with two blocks are `[1, 1]` twice, `[2, 2]` twice, `[1, 2]` twice, `[1, 1]` with `[1, 2]`, and `[2, 2]` with `[1, 2]`. The interval heaps of the section *Interval heaps overcount* have three more: `[1, 1]` beside `[2, 2]`, whose diagonals cross, and `[1, 2]` laid on `[1, 1]` or on `[2, 2]`, which overhang. A heap orders its pieces and lets incompatible ones stand together; the towers are the unordered multisets of compatible pieces.[^5]

## The transfer-matrix reading

Read a tower column by column with the height of the previous column as the state. The matrix `M_∞(x)` on the heights `0, 1, 2, …` with

```
M_∞(x)[a, b]  =  x^{max(0, b − a)}
```

records the `max(0, b − a)` blocks that a column of height `b` starts after a column of height `a`. It is the block-weighted tower matrix `M_k(t)` of [[castle-sign-kms-matrix](pages/castle-sign-kms-matrix.md)] with the height bound removed and `t = x`; its transpose at `x = −1`, restricted to the heights `0, …, k`, is the signed matrix `M̃_k` of [[tower-parity-sectors](pages/tower-parity-sectors.md)]. With `e_0` the start vector at height 0 and `𝟙` the all-ones vector, each tower is one walk of `L` steps from height 0, so

```
Σ_b T̂(L, b) x^b  =  e_0ᵀ M_∞(x)^L 𝟙,
```

and by Theorem 1 this matrix power has the closed form of Equation (1).

## Descents split Equation (2)

A descent of a tower is a position `i < L` with `c_i > c_{i+1}`. A descent at `i` is a block that ends at column `i`: the block of row `c_i` through column `i` ends there, and a block of row `r` that ends at `i < L` gives `c_{i+1} < r ≤ c_i`. So the descents of a tower are the distinct right ends `i < L` of its blocks, which in Lemma 2 are the distinct **right endpoints** `i + 1 ∈ {2, …, L}` of its diagonals, the larger label of each. The edge from 0 to `L + 1` has right endpoint `L + 1` and adds no descent.

For a triangulation `F` of the `(L + 2)`-gon, let `R(F)` hold, for each right endpoint `v ∈ {2, …, L}` of the diagonals of `F`, the longest diagonal of `F` that ends at `v`, the one with the smallest left endpoint.

**Lemma 3.** Every set `S` of pairwise non-crossing diagonals satisfies `R(F) ⊆ S ⊆ F` for exactly one triangulation `F`: the one that triangulates each region of `S` by the fan from its largest vertex.

*Proof.* The diagonals of `S` cut the polygon into regions. A region is a convex polygon with vertices `p_0 < p_1 < ⋯ < p_m`, and its side `(p_0, p_m)` is a diagonal of `S` or the edge from 0 to `L + 1`.

*Existence.* Triangulate each region by the diagonals `(p_a, p_m)`, `0 < a < m − 1`. They end at `p_m`, which is `L + 1` or the right endpoint of the diagonal `(p_0, p_m)` of `S`, and they are shorter than that diagonal. So the triangulation `F` has no right endpoint in `{2, …, L}` that `S` lacks, and at each one its longest diagonal is the longest diagonal of `S` there: `R(F) ⊆ S ⊆ F`.

*Uniqueness.* Let `F` be a triangulation with `R(F) ⊆ S ⊆ F`, and let `(p_a, p_b)` be a diagonal of `F` inside a region, with `b − a ≥ 2`. Suppose `b < m`. Then `2 ≤ p_b ≤ L`, so `R(F)` holds a diagonal `(u, p_b)` of `S` with `u ≤ p_a`. If `u < p_0`, it crosses the side `(p_0, p_m)`. If `p_0 ≤ u ≤ p_a`, the vertex `u` is a vertex of the region at least two places before `p_b`, or lies between two vertices of the region, and in both cases `(u, p_b)` runs from `p_b` into the interior of the region. A diagonal of `S` does neither, so `b = m`: every diagonal of `F` inside a region ends at its largest vertex, and `F` triangulates the region by that fan. ∎

**Theorem 2.** For every `L ≥ 1`, `b ≥ 0` and `1 ≤ k ≤ L`, the towers on a base of length `L` with `b` blocks and `k − 1` descents number `N(L, k) C(b + L − k, L − 1)`. So the descents split Equation (2) term by term.

*Proof.* By Lemmas 1 and 2, a tower with `b` blocks is a multiset of `b` segments, and by Lemma 3 its set `S` of distinct diagonals satisfies `R(F) ⊆ S ⊆ F` for exactly one triangulation `F`. The right endpoints of `S` in `{2, …, L}` are those of `F`, one for each diagonal of `R(F)`, so the tower has `|R(F)|` descents. For a triangulation `F` with `|R(F)| = k − 1`, the multisets of size `b` on the `L` segments of `F` and the edge that contain every diagonal of `R(F)` number `C(b − (k − 1) + L − 1, L − 1) = C(b + L − k, L − 1)`. It remains to count these triangulations. Lemma 3 splits the faces of `Δ_L` into the intervals between `R(F)` and `F`, so

```
Σ_{S ∈ Δ_L} y^{|S|}  =  Σ_F y^{|R(F)|} (1 + y)^{d − |R(F)|},        d = L − 1.
```

At `y = x/(1 − x)` the left side is `Σ_i h_i x^i / (1 − x)^d`, by the proof of Theorem 1, and the right side is `Σ_F x^{|R(F)|} / (1 − x)^d`. So the triangulations with `|R(F)| = i` number `h_i = N(L, i + 1)`, and those with `k − 1` right endpoints number `N(L, k)`. ∎

The counts agree with enumeration for `L ≤ 6`, `b ≤ 7` and for `L = 7`, `b ≤ 6`. Reversing a tower preserves its block count, since the total ascent from `c_0 = 0` equals the total descent to `c_{L+1} = 0`, and exchanges descents with ascents, so the ascents give the same distribution.[^4] Peaks do not split Equation (2) this way. With a peak a maximal run of equal columns higher than the columns on both sides, counting `c_0 = c_{L+1} = 0`, the 16 towers with two blocks at `L = 3` have one peak (15 of them) or two (1), while Equation (2) splits them 6, 9 and 1.[^6]

Equation (2) has the shape of Worpitzky's identity `a^n = Σ_r A(n, r) C(a + n − r, n)`, with `A(n, r)` the Eulerian numbers, under `a = b + 1`, `n = L − 1`, `r = k`: the binomial is the same and the Narayana numbers stand where the Eulerian numbers stand. Bayer and Diaconis prove that an `a`-shuffle of `n` cards gives a permutation with `r` rising sequences with probability `C(a + n − r, n)/a^n` by stars and bars: one cut between each pair of consecutive rising sequences is forced, and the `a − r` spare cuts go into `n + 1` bins. Summing over all permutations gives Worpitzky's identity ([[bayer-diaconis-1992-dovetail-shuffle](pages/bayer-diaconis-1992-dovetail-shuffle.md)]).[^7] Theorem 2 makes each term of Equation (2) a count of the same two-step kind. The `N(L, k)` choices are the triangulations `F` with `k − 1` right endpoints, the forced diagonals of `R(F)` take the place of the forced cuts, and the remaining `b − k + 1` blocks go, as the spare cuts do, into the `L` bins of the diagonals of `F` and the edge: `C(b + L − k, L − 1)` ways.[^8]

## Appearances in Sources

- [[bayer-diaconis-1992-dovetail-shuffle](pages/bayer-diaconis-1992-dovetail-shuffle.md)] - Worpitzky's identity from the probability of a permutation after an `a`-shuffle.
- [[bousquet-melou-fedou-1995-convex-polyominoes](pages/bousquet-melou-fedou-1995-convex-polyominoes.md)] - a bijection between parallelogram polyominoes and heaps of segments, which explains the quotient form of their generating functions.[^9]
- [[prellberg-brak-1995-cluster-models](pages/prellberg-brak-1995-cluster-models.md)] - the bar-graph equation (3.11) among the equations linearized by (4.2), and generating functions of the form `y(H(qx)/H(x) − 1)` with `H` satisfying a linear functional equation, a form explained for staircase polygons by a bijection with heaps.[^10]

## Related Concepts

- [[tower-heap](pages/tower-heap.md)] - towers with no height bound, the unit-cell heap and the cell count `1/(1 − x)^L`.
- [[narayana-numbers](pages/narayana-numbers.md)] - `N(L, k)`, the numerator of Equation (1), and its readings on Dyck paths and parallelogram polyominoes.
- [[castle-sign-kms-matrix](pages/castle-sign-kms-matrix.md)] - the block-weighted transfer matrix `M_k(t)` on the heights `0, …, k`.
- [[tower-parity-sectors](pages/tower-parity-sectors.md)] - the signed matrix `M̃_k` and the split of the signed tower count by the parity of the last column.
- [[generalized-dyck-grammar](pages/generalized-dyck-grammar.md)] - the grammar of tower words.
- [[stack-polyomino-gf](pages/stack-polyomino-gf.md)] - generating functions of stack polyominoes, unimodal skylines on a full base.
- [[sandpile-group](pages/sandpile-group.md)] - the series `1/(1 − 3x + x²)`, A001906, whose coefficients are the tide orders of the 2-wide ladders lying down.

## Footnotes

[^1]: [[project-euler-502-brute-force](pages/project-euler-502-brute-force.md)] `raw/project-euler-502-brute-force.wiki` §"Column-height encoding" L20-24 - "A block is a maximal horizontal run of columns at a given level, so #blocks = Σ_{r=1}^{h} #{runs of columns with c_i ≥ r} = c_1 + Σ_{i=2}^{w} max(0, c_i − c_{i−1})". The source states it for castles; the same count of runs row by row gives it for towers, whose columns may have height 0.
[^2]: Verified by execution (Python 3.11 with SymPy, 2026-10-16): the number of sets of `k` pairwise disjoint intervals in `[1, L]` equals `C(L + k, 2k)` for `L ≤ 5`, `k ≤ 3`; the series of `1/(1 − 3x + x²)`.
[^3]: https://arxiv.org/abs/math/0501100 (E. Tzanaki, "Polygon dissections and some generalizations of cluster complexes", arXiv:math/0501100v3, 2005; read 2026-10-25) p.1, p.2 Corollary 1.3 and p.3 Equation (1), with `m = 1` and `n = L` - "Consider the abstract simplicial complex ∆^m_{A_{n−1}} whose faces are the m-divisible dissections of an (mn + 2)-gon P. Precisely, the vertices of ∆^m_{A_{n−1}} are the diagonals which dissect P into an (mj + 2)-gon and an (m(n − j) + 2)-gon (1 ≤ j ≤ n − 1) and the faces are sets of diagonals of this type which are pairwise noncrossing"; "For m = 1 this simplicial complex is isomorphic to the boundary complex of the (n−1)-dimensional simplicial associahedron"; "Corollary 1.3. The i-th entry of the h-vector of ∆^m_W is equal to (1/(i+1)) C(n−1, i) C(mn, i), i = 0, . . . , n − 1, ... in the cases W = A_{n−1}"; "The f-vector determines the h-vector h(∆) = (h_0, h_1, . . . , h_d) through the formula Σ_{i=0}^{d} f_{i−1}(x − 1)^{d−i} = Σ_{i=0}^{d} h_i x^{d−i}."
[^4]: Verified by execution (Python 3.11, 2026-10-16), by enumeration of all towers on a base of length `L` with `b` blocks (heights at most `b`): `T̂(3, b) = 1, 6, 16, 31, 51, 76` for `b ≤ 5`; the descent and ascent refinements of Equation (2) for `L ≤ 6`, `b ≤ 7` and for `L = 7`, `b ≤ 6`.
[^5]: Verified by execution (Python 3.11, 2026-10-25): Lemma 1 as a count, the towers with `b` blocks against the multisets of `b` pairwise compatible intervals, for `L ≤ 5` and `b ≤ 5`; Lemma 2 for every pair of intervals of `[1, L]` and the count of diagonals, for `L ≤ 10`; the h-vector of `Δ_L` from its face numbers, equal to `N(L, k)` for `2 ≤ L ≤ 7`; the 5 towers with two blocks at `L = 2`.
[^6]: Verified by execution (Python 3.11, 2026-10-25), by enumeration of the towers by peaks: at `L = 3` the split by peaks differs from `N(3, k) C(b + 3 − k, 2)` for every `b` from 1 to 4, and it differs at `L = 4` and `L = 5` with `b ≤ 5` as well.
[^7]: [[bayer-diaconis-1992-dovetail-shuffle](pages/bayer-diaconis-1992-dovetail-shuffle.md)] `raw/bayer-diaconis-1992-dovetail-shuffle.txt` Theorem 3 and its proof [synthesis] L444-466, L497-505 - the probability of a permutation with `r` rising sequences after an `a`-shuffle is `C(a + n − r, n)/a^n`; the proof "emulate[s] the classical stars and bars argument": at least one cut between each pair of successive rising sequences, the `a − r` spare cuts in `n + 1` bins; summing over all permutations, with the Eulerian numbers counting permutations by rising sequences, gives "Worpitzky's identity".
[^8]: Verified by execution (Python 3.11, 2026-10-25): that the descents of a tower are the distinct right ends `i < L` of its blocks, for every tower with `L ≤ 5` and `b ≤ 5`; Lemma 3, each set of pairwise non-crossing diagonals lying between `R(F)` and `F` for exactly one triangulation `F`, which is the fan completion, for `L ≤ 6` (903 sets at `L = 6`); the triangulations with `k − 1` right endpoints in `{2, …, L}`, `N(L, k)` of them, for `L ≤ 7`.
[^9]: [[bousquet-melou-fedou-1995-convex-polyominoes](pages/bousquet-melou-fedou-1995-convex-polyominoes.md)] `raw/bousquet-melou-fedou-1995-convex-polyominoes.txt` L205-211 - "One approach is based on a bijection between parallelogram polyominoes and some heaps of segments ... The main advantage of this first method is that it provides a combinatorial explanation for the appearance of the quotients, and interpretations for their numerator and their denominator [7]."
[^10]: [[prellberg-brak-1995-cluster-models](pages/prellberg-brak-1995-cluster-models.md)] `raw/prellberg-brak-1995-partially-directed-cluster-models.txt` §4 L673-682, L771-778 - "the functional equations for bar-graph polygons, alternating bar-graph polygons, staircase polygons, and ZL walks can all be linearized"; "both models have generating functions which can be expressed in the form ... (4.14) where the function H satisfies a linear functional equation. In the case of staircase polygons, this structure can also be explained via a bijection with heaps".
