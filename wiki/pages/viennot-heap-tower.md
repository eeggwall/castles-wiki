---
title: Viennot heaps of pieces on towers
category: Analyses
summary: Towers with no height bound on a base of length L, read as Viennot heaps of unit-cell pieces, give the cell-count generating function 1/(1 − x)^L by Cartier-Foata inversion. The block count is not additive over unit-cell pieces, and the heaps of interval pieces do not count towers (8 heaps of two pieces against 5 towers with two blocks at L = 2). A transfer matrix on the previous column height gives the block-count identity Σ_b T̂(L, b) x^b = Narayana_L(x)/(1 − x)^L, proved on the tower-heap page, and the Narayana number N(L, k) times C(b + L − k, L − 1) counts the towers with b blocks and k − 1 descents (computed for L ≤ 7).
tags: [analysis, tower, viennot, heap-of-pieces, commutation-monoid, trace-monoid, cartier-foata, transfer-matrix, narayana]
sources: [tower-narayana-polynomial, bousquet-melou-fedou-1995-convex-polyominoes, bayer-diaconis-1992-dovetail-shuffle, prellberg-brak-1995-cluster-models]
created: 2026-09-21
updated: 2026-10-25
---

# Viennot heaps of pieces on towers

## Setup

Towers on a base of length `L` with no height bound are given by their column heights `c = (c_1, …, c_L)`, `c_i ≥ 0`, and their blocks are the maximal runs of columns with `c_i ≥ r` in each row `r` ([[tower-heap](pages/tower-heap.md)]). [[tower-heap](pages/tower-heap.md)] reads them as Viennot heaps of unit-cell pieces `u_1, …, u_L`, one piece per cell of column `i`, with `u_i` and `u_j` dependent exactly when `i = j`. The columns commute freely, so Cartier-Foata inversion gives the cell-count generating function `1/(1 − x)^L`. This page treats the block count. Write `T̂(L, b)` for the number of towers on a base of length `L` with `b` blocks; the hat separates it from the tower count `T(k, L)` ([[castle-notation](pages/castle-notation.md)]).

*Example.* At `L = 2` the towers with one block are `(1, 0)`, `(0, 1)` and `(1, 1)`, so `T̂(2, 1) = 3`.

## Block count is not additive over unit-cell pieces

A cell at row `r` and column `i` starts a new block exactly when `c_{i−1} < r` (with `c_0 = 0`), so whether it adds to the block count depends on the neighboring column. The block count

```
blocks(c)  =  c_1 + Σ_{i≥2} max(0, c_i − c_{i−1})
```

is not of the form `Σ_i f(c_i)`, so it is not a product of weights of the pieces, and the unit-cell Cartier-Foata inversion does not see it ([[castle-sign](pages/castle-sign.md)]).[^1]

**Interval pieces do not count towers.** Take the pieces to be intervals `[i, j]` in `[1, L]`, with two intervals dependent when they share a column. The trivial heaps are the sets of pairwise disjoint intervals, and there are `C(L + k, 2k)` sets of `k` of them (stars and bars), so the Cartier-Foata series is `Σ_k (−1)^k C(L + k, 2k) x^k`. At `L = 2` this is `1 − 3x + x²`, whose inverse is

```
1 / (1 − 3x + x²)  =  1 + 3x + 8x² + 21x³ + 55x⁴ + …        (A001906)
```

while the towers on a base of length 2 number `T̂(2, b) = 2b + 1`: `1, 3, 5, 7, …` (A005408). The two agree at `x^0` and `x^1` and differ at `x²`, 8 heaps of two pieces against 5 towers with two blocks. A heap of intervals is not a tower in two ways: the pieces `[1, 1]` and `[2, 2]` side by side in one row are two pieces of the heap but one block `[1, 2]` of a tower, and the heap with `[1, 2]` above `[1, 1]` overhangs column 2 and is not a tower.[^2]

## The transfer-matrix reading

Read a tower column by column with the height of the previous column as the state. The matrix `M_∞(x)` on the heights `0, 1, 2, …` with

```
M_∞(x)[a, b]  =  x^{max(0, b − a)}
```

records the `max(0, b − a)` blocks that a column of height `b` starts after a column of height `a`. It is the block-weighted tower matrix `M_k(t)` of [[castle-sign-kms-matrix](pages/castle-sign-kms-matrix.md)] with the height bound removed and `t = x`; its transpose at `x = −1`, restricted to the heights `0, …, k`, is the signed matrix `M̃_k` of [[tower-parity-sectors](pages/tower-parity-sectors.md)]. With `e_0` the start vector at height 0 and `𝟙` the all-ones vector,

```
Σ_b T̂(L, b) x^b  =  e_0ᵀ M_∞(x)^L 𝟙  =  Narayana_L(x) / (1 − x)^L,        Narayana_L(x)  =  Σ_{k=1}^{L} N(L, k) x^{k−1},      (1)
```

with `N(L, k) = (1/L) C(L, k) C(L, k − 1)` the [[narayana-numbers](pages/narayana-numbers.md)] (A001263). Equation (1) is the identity of [[tower-narayana-polynomial](pages/tower-narayana-polynomial.md)], computed there for `L ≤ 7`,[^3] and proved for every `L` on [[tower-heap](pages/tower-heap.md)] from the fixed point of the tower grammar's height map. In coefficients,

```
T̂(L, b)  =  Σ_{k=1}^{L} N(L, k) · C(b + L − k, L − 1).                         (2)
```

The rows of Equation (1) are `1/(1 − x)` at `L = 1` (one tower `(b)` with `b` blocks), `(1 + x)/(1 − x)²` at `L = 2` (`2b + 1`, A005408) and `(1 + 3x + x²)/(1 − x)³` at `L = 3` (`1, 6, 16, 31, 51, 76, …`, A005891), and `1 + 3x + x²` is row 3 of A001263.[^4]

## Descents factor Equation (2)

A descent of a tower is a position `i < L` with `c_i > c_{i+1}`. The towers on a base of length `L` with `b` blocks and `k − 1` descents number exactly `N(L, k) C(b + L − k, L − 1)`, so the descents split Equation (2) term by term (computed for `L ≤ 6`, `b ≤ 7` and for `L = 7`, `b ≤ 6`). Reversing a tower preserves its block count, since the total ascent from `c_0 = 0` equals the total descent to `c_{L+1} = 0`, and exchanges descents with ascents, so the ascents give the same distribution.[^4] The number of peaks does not factor Equation (2) this way; the source states the identity at the level of generating functions for that reason.[^5]

Equation (2) has the shape of Worpitzky's identity `a^n = Σ_r A(n, r) C(a + n − r, n)`, with `A(n, r)` the Eulerian numbers, under `a = b + 1`, `n = L − 1`, `r = k`: the binomial is the same and the Narayana numbers stand where the Eulerian numbers stand. Bayer and Diaconis prove that an `a`-shuffle of `n` cards gives a permutation with `r` rising sequences with probability `C(a + n − r, n)/a^n` by stars and bars: one cut between each pair of consecutive rising sequences is forced, and the `a − r` spare cuts go into `n + 1` bins. Summing over all permutations gives Worpitzky's identity ([[bayer-diaconis-1992-dovetail-shuffle](pages/bayer-diaconis-1992-dovetail-shuffle.md)]).[^6] Each term of Equation (2) is a count of the same two-step kind: `N(L, k)` choices, then a weak composition of `b − k + 1` into `L` parts, `C(b + L − k, L − 1)` of them.

## Appearances in Sources

- [[tower-narayana-polynomial](pages/tower-narayana-polynomial.md)] - Equation (1) for `L ≤ 7`, the tower definition, and the statement that the identity is not a peaks bijection.
- [[bayer-diaconis-1992-dovetail-shuffle](pages/bayer-diaconis-1992-dovetail-shuffle.md)] - Worpitzky's identity from the probability of a permutation after an `a`-shuffle.
- [[bousquet-melou-fedou-1995-convex-polyominoes](pages/bousquet-melou-fedou-1995-convex-polyominoes.md)] - a bijection between parallelogram polyominoes and heaps of segments, which explains the quotient form of their generating functions.[^7]
- [[prellberg-brak-1995-cluster-models](pages/prellberg-brak-1995-cluster-models.md)] - the bar-graph equation (3.11) among the equations linearized by (4.2), and generating functions of the form `y(H(qx)/H(x) − 1)` with `H` satisfying a linear functional equation, a form explained for staircase polygons by a bijection with heaps.[^8]

## Related Concepts

- [[tower-heap](pages/tower-heap.md)] - towers with no height bound, the unit-cell heap and the cell count `1/(1 − x)^L`.
- [[narayana-numbers](pages/narayana-numbers.md)] - `N(L, k)`, the numerator of Equation (1), and its readings on Dyck paths and parallelogram polyominoes.
- [[castle-sign-kms-matrix](pages/castle-sign-kms-matrix.md)] - the block-weighted transfer matrix `M_k(t)` on the heights `0, …, k`.
- [[tower-parity-sectors](pages/tower-parity-sectors.md)] - the signed matrix `M̃_k` and the split of the signed tower count by the parity of the last column.
- [[generalized-dyck-grammar](pages/generalized-dyck-grammar.md)] - the grammar of tower words.
- [[stack-polyomino-gf](pages/stack-polyomino-gf.md)] - generating functions of stack polyominoes, unimodal skylines on a full base.
- [[sandpile-group](pages/sandpile-group.md)] - the series `1/(1 − 3x + x²)`, A001906, whose coefficients are the tide orders of the 2-wide ladders lying down.

## Footnotes

[^1]: [[tower-narayana-polynomial](pages/tower-narayana-polynomial.md)] `raw/oeis-pe502/xrefs/A001263-tower.md` §"The tower object (self-contained definition)" L29-34 - "each block is a horizontal segment of adjacent cells at some height, every block rests on the floor or on the block directly below it (nothing floats or overhangs), and two blocks in the same row are separated by at least one empty cell ... its number of blocks is the number of maximal horizontal runs, c_1 + Sum_{i=2..w} max(0, c_i - c_{i-1})."
[^2]: Verified by execution (Python 3.11 with SymPy, 2026-10-16): the number of sets of `k` pairwise disjoint intervals in `[1, L]` equals `C(L + k, 2k)` for `L ≤ 5`, `k ≤ 3`; the series of `1/(1 − 3x + x²)`.
[^3]: [[tower-narayana-polynomial](pages/tower-narayana-polynomial.md)] `raw/oeis-pe502/xrefs/A001263-tower.md` §"Identity (verified)" L14-21 - "A tower of width w has, by number of blocks, the generating function sum_b (number of towers of width w with b blocks) x^b = ( sum_{k=1..w} N(w,k) x^{k-1} ) / (1 - x)^w. Equivalently, the number of towers of width w with exactly b blocks is sum_{k=1..w} N(w,k) * C(b + w - k, w - 1)."
[^4]: Verified by execution (Python 3.11, 2026-10-16), by enumeration of all towers on a base of length `L` with `b` blocks (heights at most `b`): `T̂(3, b) = 1, 6, 16, 31, 51, 76` for `b ≤ 5`; the descent and ascent refinements of Equation (2) for `L ≤ 6`, `b ≤ 7` and for `L = 7`, `b ≤ 6`.
[^5]: [[tower-narayana-polynomial](pages/tower-narayana-polynomial.md)] `raw/oeis-pe502/xrefs/A001263-tower.md` §"Identity (verified)" L24-25 - "It is a generating-function identity, not a 'peaks' bijection: a direct peaks refinement was tested and does not factor this way, so do not state a peaks interpretation."
[^6]: [[bayer-diaconis-1992-dovetail-shuffle](pages/bayer-diaconis-1992-dovetail-shuffle.md)] `raw/bayer-diaconis-1992-dovetail-shuffle.txt` Theorem 3 and its proof [synthesis] L444-466, L497-505 - the probability of a permutation with `r` rising sequences after an `a`-shuffle is `C(a + n − r, n)/a^n`; the proof "emulate[s] the classical stars and bars argument": at least one cut between each pair of successive rising sequences, the `a − r` spare cuts in `n + 1` bins; summing over all permutations, with the Eulerian numbers counting permutations by rising sequences, gives "Worpitzky's identity".
[^7]: [[bousquet-melou-fedou-1995-convex-polyominoes](pages/bousquet-melou-fedou-1995-convex-polyominoes.md)] `raw/bousquet-melou-fedou-1995-convex-polyominoes.txt` L205-211 - "One approach is based on a bijection between parallelogram polyominoes and some heaps of segments ... The main advantage of this first method is that it provides a combinatorial explanation for the appearance of the quotients, and interpretations for their numerator and their denominator [7]."
[^8]: [[prellberg-brak-1995-cluster-models](pages/prellberg-brak-1995-cluster-models.md)] `raw/prellberg-brak-1995-partially-directed-cluster-models.txt` §4 L673-682, L771-778 - "the functional equations for bar-graph polygons, alternating bar-graph polygons, staircase polygons, and ZL walks can all be linearized"; "both models have generating functions which can be expressed in the form ... (4.14) where the function H satisfies a linear functional equation. In the case of staircase polygons, this structure can also be explained via a bijection with heaps".
