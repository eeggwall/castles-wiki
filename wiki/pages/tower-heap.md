---
title: Tower (heap of pieces)
category: Concepts
summary: Towers on a base of length L with no height bound, given by column heights (c_1, …, c_L) ∈ N^L, counted by their blocks. The number T̂(L, b) with b blocks is finite, since a tower has at least as many blocks as its height, and Σ_b T̂(L, b) x^b = Σ_k N(L, k) x^{k−1}/(1 − x)^L with the Narayana numbers N(L, k), proved from the fixed point of the tower grammar's height map, the k-th term counting the towers with k − 1 descents (computed for L ≤ 7). A second sum, indexed by blocks, T̂(L, b) = Σ_i N(b, i) C(L + 1 + 2b − 2i, 2b), is proved by Cho, Huh, Nam and Sohn, its i-th term counting the towers with i plateaus higher than both neighbors. T̂(L, b) also counts the (L+1)-core partitions with b corners, and the castles of width L with b + 1 blocks. As a heap of unit cells the towers are N^L, with cell-count generating function 1/(1 − x)^L.
tags: [concept, tower, heap-of-pieces, viennot, narayana, castle]
sources: [project-euler-502-representations, project-euler-502-brute-force, cho-huh-nam-sohn-2022-bounded-free-motzkin-paths, bousquet-melou-fedou-1995-convex-polyominoes, oeis-encyclopedia]
created: 2026-09-13
updated: 2026-10-25
---

# Tower (heap of pieces)

## Towers with no height bound

Removing the bottom row of a castle of width `L` leaves towers on a base of length `L` ([[castle-polyomino](pages/castle-polyomino.md)]). Towers are given by their column heights `c = (c_1, …, c_L)` with every `c_i ≥ 0`, and their blocks are the maximal runs of columns in each row, so the block count is[^1]

```
blocks(c)  =  Σ_{i=1}^{L} max(0, c_i − c_{i−1}),        c_0 = 0.
```

The [[castle-counting-formula](pages/castle-counting-formula.md)] counts the towers of height at most `k`, `T(k, L) = (k+1)^L`. This page drops the height bound and counts the towers by blocks instead. *Example:* the towers `(1, 0, 2)` on a base of length 3 have `1 + 0 + 2 = 3` blocks, one in row 1 over the first column and two over the third.

Write `T̂(L, b)` for the number of towers on a base of length `L` with `b` blocks. The hat distinguishes it from the tower count `T(k, L)`, whose first argument is a height bound; the sources write `T(w, b)`. The number is finite: for every `j`, `blocks(c) ≥ Σ_{i≤j} max(0, c_i − c_{i−1}) ≥ c_j`, so towers with `b` blocks have height at most `b`. A castle has one block more than its towers, so `T̂(L, b)` is also the number of castles of width `L` with `b + 1` blocks, of any height.

## Block count and the Narayana numbers

With the [[narayana-numbers](pages/narayana-numbers.md)] `N(L, k) = (1/L) C(L, k) C(L, k−1)`,

```
Σ_{b≥0} T̂(L, b) x^b  =  Narayana_L(x) / (1 − x)^L,        Narayana_L(x)  =  Σ_{k=1}^{L} N(L, k) x^{k−1},
T̂(L, b)              =  Σ_{k=1}^{L} N(L, k) C(b + L − k, L − 1).
```

The `k`-th term counts the towers whose column heights have `k − 1` descents, positions `i` with `c_i > c_{i+1}`. The identity and this refinement agree with enumeration of all towers for `L ≤ 6`, `b ≤ 7`, and for `L = 7`, `b ≤ 6`.[^3] The identity is proved below; the refinement by descents is not proved on the wiki. Reversing a tower turns its descents into ascents, so the ascents have the same distribution.

*Proof of the identity.* In this proof `x` marks width and `y` blocks, so the identity reads `[x^L] E_∞(x, y) = Narayana_L(y)/(1 − y)^L`, where `E_∞(x, y) = Σ_{L,b} T̂(L, b) x^L y^b` is the generating function of the towers of every height. `E_∞` is the fixed point of the height map of the tower grammar ([[generalized-dyck-grammar](pages/generalized-dyck-grammar.md)], section *Counts*):

```
xy E_∞²  −  (1 − x)(1 − y) E_∞  +  (1 − y)  =  0.
```

Put `x = z(1 − y)` and divide by `−(1 − y)`: the function `F(z) = E_∞(z(1 − y), y)` satisfies `F = 1 + zF(1 + y(F − 1))`, which fixes its coefficients in `z` one at a time from `F(0) = 1`. A nonempty Dyck path is `U A D B` with Dyck paths `A` and `B`, and it has the peaks of `A` and of `B` and one more when `A` is empty, so the generating function `G(z, t)` of Dyck paths by semilength and peaks satisfies `G = 1 + z(t + G − 1)G`, and `1 + (G − 1)/t` at `t = y` satisfies the equation of `F`. So `F = 1 + (G(z, y) − 1)/y`, and since `N(L, k)` counts the Dyck paths of semilength `L` with `k` peaks, `[z^L] F = Narayana_L(y)`, which is the identity. The coefficient of `y^b` in `y^{k−1}/(1 − y)^L` is `C(b + L − k, L − 1)`, which gives the second line.[^2] The proof matches generating functions; it does not match the towers with `k − 1` descents to the Dyck paths with `k` peaks one by one.

*Example: `L = 2`.* The block count of `(c_1, c_2)` is `max(c_1, c_2)`, and `2b + 1` pairs have maximum `b`. The formula gives `N(2, 1) C(b + 1, 1) + N(2, 2) C(b, 1) = (b + 1) + b`: the `b + 1` towers with `c_1 ≤ c_2` have no descent, and the `b` with `c_1 > c_2` have one.

The rows `T̂(L, ·)` for `L = 2, 3, 4, 5` are `A005408`, `A005891`, `A063490` (with offset 1, so `T̂(4, b) = A063490(b + 1)`) and `A160747`; [[tower-narayana-polynomial](pages/tower-narayana-polynomial.md)] tabulates the rows to `L = 7`.[^4] By semi-perimeter, a castle of width `L` with `b + 1` blocks has semi-perimeter `L + b + 1`, so `T̂(L, b)` is the entry of `A271942`, the bargraphs by semi-perimeter and width, at semi-perimeter `L + b + 1` and width `L` ([[castle-perimeter](pages/castle-perimeter.md)]).[^5]

The binomial `C(b + L − k, L − 1)` is the count `C(a + n − r, n)` at `a = b + 1`, `n = L − 1` and `r = k` with which Bayer and Diaconis count the ways to cut a deck of `n` cards into `a` packets that produce a given permutation with `r` rising sequences, in their stars-and-bars proof of Worpitzky's identity ([[bayer-diaconis-1992-dovetail-shuffle](pages/bayer-diaconis-1992-dovetail-shuffle.md)]).[^6]

## The sum indexed by blocks

Cho, Huh, Nam and Sohn prove a second Narayana sum, with the Narayana index on the blocks instead of the base length ([[cho-huh-nam-sohn-2022-bounded-free-motzkin-paths](pages/cho-huh-nam-sohn-2022-bounded-free-motzkin-paths.md)]). For `b ≥ 1`,[^9]

```
T̂(L, b)  =  Σ_{i=1}^{min(b, ⌊(L+1)/2⌋)}  N(b, i) · C(L + 1 + 2b − 2i, 2b).
```

The tower word of a tower with `b` blocks has `b` up steps `U`, `b` down steps `D` and `L` flat steps `R`, and contains no `UD` and no `DU` ([[motzkin-castles](pages/motzkin-castles.md)] §1). Deleting the `R`s leaves a Dyck path with `b` up steps. If it has `i` peaks, it has `i − 1` valleys, and the tower word is recovered by putting the `L` flat steps into the `2b + 1` gaps of the Dyck path with at least one in each of the `2i − 1` gaps at a peak or a valley, which can be done in `C(L + 1 + 2b − 2i, 2b)` ways. So term `i` counts the towers with `i` plateaus higher than the columns on both sides, with height 0 outside the base. For `b ≥ 1` these are the bargraph peaks of Deutsch and Elizalde, not the peaks of [[castle-foata-transform](pages/castle-foata-transform.md)] ([[castle-notation](pages/castle-notation.md)]).[^10]

*Example: `L = 2`.* For `b ≥ 1` the sum has the single term `i = 1`, `N(b, 1) C(2b + 1, 2b) = 2b + 1`, and every tower `(c_1, c_2)` with `b ≥ 1` blocks has exactly one plateau higher than both sides: the higher column, or both columns when they are equal.

The same paper reads the towers as partitions. A partition `λ` is a `t`-core if none of its hook lengths is `t`, and its corners are its distinct part sizes. The towers on a base of length `L` with `b` blocks and height at most `k` correspond to the `(L+1)`-cores with `b` corners whose largest hook length `λ_1 + ℓ(λ) − 1` is below `k(L + 1)`. Column `j` of the tower is the number of first-column hook lengths congruent to `j` modulo `L + 1`. So `T̂(L, b)` is the number of `(L+1)`-cores with `b` corners.[^9][^10]

## Heap presentation

Viennot's heaps of pieces are a geometrical form of partially commutative monoids,[^7] and the towers are heaps of unit cells. With one unit cell per column as the piece `u_i`, and two pieces dependent exactly when they lie in the same column, pieces in different columns commute, the monoid of heaps is the free commutative monoid `N^L`, and a heap is a vector of column heights, so the heaps are the towers. Weighting each cell by `x`, the generating function of towers by cells is `Σ_c x^{c_1 + ⋯ + c_L} = 1/(1 − x)^L`, and the towers with `n` cells number `C(n + L − 1, L − 1)`. The Cartier-Foata inversion formula, which writes the inverse of a heap generating function as a signed sum over the trivial heaps (sets of pairwise independent pieces), gives `Σ_{S ⊆ {1, …, L}} (−x)^{|S|} = (1 − x)^L`.

The block count is not a statistic of this presentation. With intervals of columns as pieces, two intervals dependent when they share a column, the heaps are not the towers: at `L = 2` there are 8 heaps of two interval pieces, and 5 towers with two blocks ([[viennot-heap-tower](pages/viennot-heap-tower.md)]).

## Appearances in Sources

- [[project-euler-502-representations](pages/project-euler-502-representations.md)] - the castle as `U (towers) D`, with the bottom row as the outer `U … D`.
- [[cho-huh-nam-sohn-2022-bounded-free-motzkin-paths](pages/cho-huh-nam-sohn-2022-bounded-free-motzkin-paths.md)] - the sum indexed by blocks with its proof, and the towers as core partitions.

## Related Concepts

- [[narayana-numbers](pages/narayana-numbers.md)] - the coefficients of the numerator `Narayana_L(x)`.
- [[tower-narayana-polynomial](pages/tower-narayana-polynomial.md)] - the generating function of towers counted by blocks, and its rows in the OEIS.
- [[oeis-mining-pe502](pages/oeis-mining-pe502.md)] - the castle counts matched to OEIS entries, the tower block-count rows among them.
- [[castle-polyomino](pages/castle-polyomino.md)] - castles, which stand on towers with one block fewer.
- [[castle-counting-formula](pages/castle-counting-formula.md)] - the towers of height at most `k`, `T(k, L) = (k+1)^L`.
- [[signed-tower-count](pages/signed-tower-count.md)] - `P(k, L)`, the sum of `(−1)^{blocks}` over the towers of height at most `k`.
- [[tower-parity-sectors](pages/tower-parity-sectors.md)] - the signed transfer matrix of the towers, split by the parity of the last column.
- [[tower-recursion-master-class](pages/tower-recursion-master-class.md)] - a seminar on the tower count `T(k, L)` and the sign.
- [[viennot-heap-tower](pages/viennot-heap-tower.md)] - the heap presentation, Cartier-Foata inversion, and the interval-piece heaps that do not give the tower count.
- [[generalized-dyck-grammar](pages/generalized-dyck-grammar.md)] - the grammar of tower words, whose height map has `E_∞(x, y)` as fixed point, the start of the proof of the Narayana identity.
- [[tower-word-continued-fraction](pages/tower-word-continued-fraction.md)] - tower words counted by length, `A004149`, through a continued fraction.
- [[castle-foata-transform](pages/castle-foata-transform.md)] - the peaks of the towers, the maximal runs of columns with `c_i ≥ 1`, in bijection with the first columns of those runs.
- [[castle-perimeter](pages/castle-perimeter.md)] - the castles counted by semi-perimeter, which re-index `T̂(L, b)`.
- [[castle-conditional-entropy](pages/castle-conditional-entropy.md)] - the entropy of the block count of towers, used as a model for the block count of castles.
- [[prellberg-brak-1995-cluster-models](pages/prellberg-brak-1995-cluster-models.md)] - generating functions of the form `y(H(qx)/H(x) − 1)`, which for staircase polygons a bijection with heaps explains.[^8]

## Footnotes

[^1]: [[project-euler-502-brute-force](pages/project-euler-502-brute-force.md)] §"p_signed" L31-47 - "A new column of height b after a column of height a starts max(0, b - a) new runs, each contributing a factor of -1".
[^2]: Verified by execution (Python 3.11 with SymPy, 2026-10-25): the substitution `x = z(1 − y)` turns the fixed-point equation into `−(1 − y)(F − 1 − zF(1 + y(F − 1)))`; the coefficients of `x^L` in its power-series root equal `Narayana_L(y)/(1 − y)^L` for `L ≤ 10`, and their coefficients in `y` equal the enumeration of `T̂(L, b)` for `L ≤ 5`, `b ≤ 7`.
[^3]: Verified by execution (Python 3.11, 2026-10-16): `T̂(L, b)` and its refinement by the number of descents against enumeration of all towers in `{0, …, B}^L` (towers with `b ≤ B` blocks have height at most `B`), for `L ≤ 6`, `B = 7` and `L = 7`, `B = 6`.
[^4]: https://oeis.org/A005408, https://oeis.org/A005891, https://oeis.org/A063490, https://oeis.org/A160747 (read 2026-10-25) - A005408 "The odd numbers: a(n) = 2*n + 1.", offset 0; A005891 "Centered pentagonal numbers: (5n^2+5n+2)/2", offset 0; A063490 "a(n) = (2*n - 1)*(7*n^2 - 7*n + 6)/6.", offset 1, with the comment "a(n) is also the number of castle polyominoes of width 4 with n blocks, of any height"; A160747 "Expansion of (1 + 10*x + 20*x^2 + 10*x^3 + x^4)/(1-x)^5.", offset 0, with the comment "a(n) is also the number of castle polyominoes of width 5 with n + 1 blocks, of any height". Verified by execution (Python 3.11, 2026-10-25): the enumerated rows `T̂(2, b)` and `T̂(3, b)` for `b ≤ 15`, `T̂(4, b)` for `b ≤ 11` and `T̂(5, b)` for `b ≤ 8` equal these data at these offsets.
[^5]: https://oeis.org/A271942 (read 2026-10-16) - "Triangle read by rows: T(n,k) is the number of bargraphs of semiperimeter n having width k (n>=2, k>=1)"; its columns `k = 2, 3, 4, 5` begin `1, 3, 5, 7`, `1, 6, 16, 31`, `1, 10, 40, 105`, `1, 15, 85, 295`.
[^6]: raw/bayer-diaconis-1992-dovetail-shuffle.txt §3 proof of Theorem 3 p.301 L455-461 - "At least one cut must fall between each successive pair of rising sequences of n, but the remaining cuts can be located arbitrarily. Thus, the n cards form dividers creating n + 1 bins, into which the a - r spare cuts are allocated."
[^7]: [[bousquet-melou-fedou-1995-convex-polyominoes](pages/bousquet-melou-fedou-1995-convex-polyominoes.md)] §1 L207-209 - "The theory of heaps of pieces, introduced by Viennot, is a geometrical version of the theory of partially commutative monoids".
[^8]: [[prellberg-brak-1995-cluster-models](pages/prellberg-brak-1995-cluster-models.md)] §4 L770-778 - "both models have generating functions which can be expressed in the form G(x, y, q) = y(H(qx, y, q)/H(x, y, q) - 1) (4.14) where the function H satisfies a linear functional equation. In the case of staircase polygons, this structure can also be explained via a bijection with heaps".
[^9]: [[cho-huh-nam-sohn-2022-bounded-free-motzkin-paths](pages/cho-huh-nam-sohn-2022-bounded-free-motzkin-paths.md)] p.13 Theorem 3.3 L721-733 and p.14 Proposition 3.4 L785-801 [synthesis] - the `t`-cores with `m` corners and `h(1, 1) < kt` are in bijection with the cornerless Motzkin paths of length `2m + t − 1` with `t − 1` flat steps in the strip `0 ≤ y ≤ k`, and their number is `Σ_i N(m, i) C(t + 2m − 2i, 2m)`, proved by inserting the flat steps into a Dyck path "at least one flat steps at the positions of i peaks and i − 1 valleys"; here `t = L + 1` and `m = b`.
[^10]: Verified by execution (Python 3.10, 2026-10-17): `bin/python/bounded_t_cores.py`, run log `bin/python/bounded_t_cores-run.log`. The sum and its refinement by plateaus higher than both neighbors against enumeration of all towers for `L ≤ 6`, `b ≤ 7` and `L = 7`, `b ≤ 6`; the map from cores to towers as a bijection with blocks equal to corners for `L + 1 ≤ 6` and `k ≤ 3`.
