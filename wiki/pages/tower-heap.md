---
title: Tower (heap of pieces)
category: Concepts
summary: Towers on a base of length L with no height bound, given by column heights (c_1, …, c_L) ∈ N^L, counted by their blocks. The number T̂(L, b) with b blocks is finite, since a tower has at least as many blocks as its height, and Σ_b T̂(L, b) x^b = Σ_k N(L, k) x^{k−1}/(1 − x)^L with the Narayana numbers N(L, k), the k-th term counting the towers with k − 1 descents (both computed for L ≤ 7). T̂(L, b) is also the number of castles of width L with b + 1 blocks. As a heap of unit cells the towers are N^L, with cell-count generating function 1/(1 − x)^L.
tags: [concept, tower, heap-of-pieces, viennot, narayana, castle]
sources: [oeis-mining-pe502, tower-narayana-polynomial, project-euler-502-representations]
created: 2026-09-13
updated: 2026-10-16
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

With the [[narayana-numbers](pages/narayana-numbers.md)] `N(L, k) = (1/L) C(L, k) C(L, k−1)`,[^2]

```
Σ_{b≥0} T̂(L, b) x^b  =  Narayana_L(x) / (1 − x)^L,        Narayana_L(x)  =  Σ_{k=1}^{L} N(L, k) x^{k−1},
T̂(L, b)              =  Σ_{k=1}^{L} N(L, k) C(b + L − k, L − 1).
```

The `k`-th term counts the towers whose column heights have `k − 1` descents, positions `i` with `c_i > c_{i+1}`. Both statements agree with enumeration of all towers for `L ≤ 6`, `b ≤ 7`, and for `L = 7`, `b ≤ 6`; neither is proved on the wiki.[^3] Reversing a tower turns its descents into ascents, so the ascents have the same distribution.

*Example: `L = 2`.* The block count of `(c_1, c_2)` is `max(c_1, c_2)`, and `2b + 1` pairs have maximum `b`. The formula gives `N(2, 1) C(b + 1, 1) + N(2, 2) C(b, 1) = (b + 1) + b`: the `b + 1` towers with `c_1 ≤ c_2` have no descent, and the `b` with `c_1 > c_2` have one.

The rows `T̂(L, ·)` for `L = 2, 3, 4, 5` are `A005408`, `A005891`, `A063490` (with offset 1, so `T̂(4, b) = A063490(b + 1)`) and `A160747`; [[tower-narayana-polynomial](pages/tower-narayana-polynomial.md)] tabulates the rows to `L = 7`.[^4] By semi-perimeter, a castle of width `L` with `b + 1` blocks has semi-perimeter `L + b + 1`, so `T̂(L, b)` is the entry of `A271942`, the bargraphs by semi-perimeter and width, at semi-perimeter `L + b + 1` and width `L` ([[castle-perimeter](pages/castle-perimeter.md)]).[^5]

The binomial `C(b + L − k, L − 1)` is the count `C(a + n − r, n)` at `a = b + 1`, `n = L − 1` and `r = k` with which Bayer and Diaconis count the ways to cut a deck of `n` cards into `a` packets that produce a given permutation with `r` rising sequences, in their stars-and-bars proof of Worpitzky's identity ([[bayer-diaconis-1992-dovetail-shuffle](pages/bayer-diaconis-1992-dovetail-shuffle.md)]).[^6]

## Heap presentation

The source calls the towers Viennot's "heap of pieces" of unit-height segments.[^7] With one unit cell per column as the piece `u_i`, and two pieces dependent exactly when they lie in the same column, pieces in different columns commute, the monoid of heaps is the free commutative monoid `N^L`, and a heap is a vector of column heights, so the heaps are the towers. Weighting each cell by `x`, the generating function of towers by cells is `Σ_c x^{c_1 + ⋯ + c_L} = 1/(1 − x)^L`, and the towers with `n` cells number `C(n + L − 1, L − 1)`. The Cartier-Foata inversion formula, which writes the inverse of a heap generating function as a signed sum over the trivial heaps (sets of pairwise independent pieces), gives `Σ_{S ⊆ {1, …, L}} (−x)^{|S|} = (1 − x)^L`.

The block count is not a statistic of this presentation. With intervals of columns as pieces, two intervals dependent when they share a column, the heaps are not the towers: at `L = 2` there are 8 heaps of two interval pieces, and 5 towers with two blocks ([[viennot-heap-tower](pages/viennot-heap-tower.md)]).

## Appearances in Sources

- [[tower-narayana-polynomial](pages/tower-narayana-polynomial.md)] - the generating function of towers counted by blocks, and its rows in the OEIS.
- [[oeis-mining-pe502](pages/oeis-mining-pe502.md)] - the mining pass in which the towers were counted by blocks.
- [[project-euler-502-representations](pages/project-euler-502-representations.md)] - the castle as `U (towers) D`, with the bottom row as the outer `U … D`.

## Related Concepts

- [[narayana-numbers](pages/narayana-numbers.md)] - the coefficients of the numerator `Narayana_L(x)`.
- [[castle-polyomino](pages/castle-polyomino.md)] - castles, which stand on towers with one block fewer.
- [[castle-counting-formula](pages/castle-counting-formula.md)] - the towers of height at most `k`, `T(k, L) = (k+1)^L`.
- [[signed-tower-count](pages/signed-tower-count.md)] - `P(k, L)`, the sum of `(−1)^{blocks}` over the towers of height at most `k`.
- [[tower-parity-sectors](pages/tower-parity-sectors.md)] - the signed transfer matrix of the towers, split by the parity of the last column.
- [[tower-recursion-master-class](pages/tower-recursion-master-class.md)] - a seminar on the tower count `T(k, L)` and the sign.
- [[viennot-heap-tower](pages/viennot-heap-tower.md)] - the heap presentation, Cartier-Foata inversion, and the interval-piece heaps that do not give the tower count.
- [[generalized-dyck-grammar](pages/generalized-dyck-grammar.md)] - the grammar of tower words.
- [[tower-word-continued-fraction](pages/tower-word-continued-fraction.md)] - tower words counted by length, `A004149`, through a continued fraction.
- [[castle-foata-transform](pages/castle-foata-transform.md)] - the peaks of the towers, the maximal runs of columns with `c_i ≥ 1`, in bijection with the first columns of those runs.
- [[castle-perimeter](pages/castle-perimeter.md)] - the castles counted by semi-perimeter, which re-index `T̂(L, b)`.
- [[castle-conditional-entropy](pages/castle-conditional-entropy.md)] - the entropy of the block count of towers, used as a model for the block count of castles.
- [[prellberg-brak-1995-cluster-models](pages/prellberg-brak-1995-cluster-models.md)] - generating functions of the form `y(H(qx)/H(x) − 1)`, which for staircase polygons a bijection with heaps explains.[^8]

## Footnotes

[^1]: `raw/oeis-pe502/crosslink-avenues.md` §"Tier 2" L36-37 - "A **tower** of width w is column heights `c_1..c_w >= 0` (no full-bottom-row, no max-height, no parity). Blocks are maximal horizontal runs, `#blocks = c_1 + sum max(0, c_i − c_{i−1})`."
[^2]: `raw/oeis-pe502/crosslink-avenues.md` §"Tier 2" L41-47 - "Result (verified for w = 1..7 against brute force): T(w,b) = # towers of width w with exactly b blocks = sum_{k=1..w} Narayana(w,k) * C(b + w − k, w − 1) (Narayana-polynomial g.f.) g.f. = (Narayana_w(x)) / (1 − x)^w".
[^3]: Verified by execution (Python 3.11, 2026-10-16): `T̂(L, b)` and its refinement by the number of descents against enumeration of all towers in `{0, …, B}^L` (towers with `b ≤ B` blocks have height at most `B`), for `L ≤ 6`, `B = 7` and `L = 7`, `B = 6`.
[^4]: `raw/oeis-pe502/crosslink-avenues.md` §"Tier 2" L49-56 - the table of `T(w, b)` for `w = 2, …, 7` with "A005408 (odd numbers)", "A005891 (centered pentagonal)", "A063490", "A160747"; offsets checked on oeis.org (2026-10-16): `A005408`, `A005891`, `A160747` have offset 0 and `A063490` offset 1, with g.f. `x(1+x)(1+5x+x^2)/(1-x)^4`.
[^5]: https://oeis.org/A271942 (read 2026-10-16) - "Triangle read by rows: T(n,k) is the number of bargraphs of semiperimeter n having width k (n>=2, k>=1)"; its columns `k = 2, 3, 4, 5` begin `1, 3, 5, 7`, `1, 6, 16, 31`, `1, 10, 40, 105`, `1, 15, 85, 295`.
[^6]: raw/bayer-diaconis-1992-dovetail-shuffle.txt §3 proof of Theorem 3 p.301 L455-461 - "At least one cut must fall between each successive pair of rising sequences of n, but the remaining cuts can be located arbitrarily. Thus, the n cards form dividers creating n + 1 bins, into which the a - r spare cuts are allocated."
[^7]: `raw/oeis-pe502/crosslink-avenues.md` §"Tier 2" L38-39 - "This is Viennot's \"heap of pieces\": stack unit-height segments on w columns, each segment resting on the one below, segments in the same row separated by a gap."
[^8]: [[prellberg-brak-1995-cluster-models](pages/prellberg-brak-1995-cluster-models.md)] §4 L770-778 - "both models have generating functions which can be expressed in the form G(x, y, q) = y(H(qx, y, q)/H(x, y, q) - 1) (4.14) where the function H satisfies a linear functional equation. In the case of staircase polygons, this structure can also be explained via a bijection with heaps".
