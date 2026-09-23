---
title: Viennot heaps of pieces on the tower
category: Analyses
summary: The tower as a Viennot heap of pieces over w free columns, its trace-monoid presentation, the Cartier-Foata inversion recovering `1/(1-x)^w` for cell count, and the transfer-matrix reading that produces `Narayana_w(x)/(1-x)^w` for block count. Also identifies where the naive block-piece basis (intervals in `[1,w]`, dependency = shared column) fails to reproduce the tower count, and what a heap-theoretic proof of the Narayana numerator would have to supply.
tags: [analysis, tower, viennot, heap-of-pieces, commutation-monoid, trace-monoid, cartier-foata, transfer-matrix, narayana]
sources: [tower-narayana-polynomial, bousquet-melou-fedou-1995-convex-polyominoes]
created: 2026-09-21
updated: 2026-09-22
---

# Viennot heaps of pieces on the tower

## The thread

[[tower-heap](pages/tower-heap.md)] names the tower as Viennot's "heap of pieces" with piece basis `B = {u_1, …, u_w}`, diagonal dependency `u_i R u_j iff i = j`, and cell-count identity `C_w(x) = 1/(1-x)^w` from Cartier-Foata inversion (tautological here because the columns already commute freely). This page picks up where that setup ends: what happens when the *block* count enters, why the naive heap-of-block-pieces recipe fails, and how the finite-state transfer matrix Viennot's framework promotes recovers the block-count Narayana identity of [[tower-narayana-polynomial](pages/tower-narayana-polynomial.md)].

## Block count is not a piece-additive statistic

The block count of a tower is not a piece-additive statistic under the basis `B`. A segment at `(row r, column i)` contributes to a *new* block if `c_{i-1} < r` and to an *existing* block otherwise, and this decision depends on the height at column `i-1` (the [[castle-foata-transform](pages/castle-foata-transform.md)] "positive-run" reading of blocks).[^3] Concretely, `blocks(c) = c_1 + Sum_{i>=2} max(0, c_i - c_{i-1})` is not of the form `Sum_i f(c_i)`, so it does not factor as `Prod_i` (weight of piece at column `i`), and the Cartier-Foata setup above cannot see it.

Two natural attempts to bring block count into the piece structure:

- **Coarsen the piece basis to horizontal-run intervals.** Take pieces to be intervals `[i,j]` in `[1,w]` at some row, with `[i,j] R [i',j']` iff `[i,j] cap [i',j'] != empty`. Trivial heaps are then sets of pairwise column-disjoint intervals; a standard stars-and-bars gives `C(w+k, 2k)` such sets of size `k`, so the Cartier-Foata sum is `Sum_k (-1)^k C(w+k, 2k) x^k`. At `w = 2` this is `1 - 3x + x^2`, whose inverse `1 + 3x + 8x^2 + 21x^3 + ...` is the Fibonacci bisection A001906, *not* the tower row `1, 3, 5, 7, ...` (A005408). The mismatch is that Viennot's abstract heap of intervals is not the tower: pieces `[1,1]` and `[2,2]` at the same row merge into the block `[1,2]` in a tower but stay two pieces in the heap, and heaps like `[1,2]` on top of `[1,1]` (where the wider piece has no support in column 2) count in the heap monoid but do not lift to any tower. So the interval-piece basis is *too generous* on both sides at once.

- **Refine the weighting under the unit-segment basis.** Keep `B = {u_1, ..., u_w}` and let a piece at column `i` carry weight `x^{[i is a block-start position for this piece]}`. This makes the weight a function of the *state* at column `i-1`, not just the piece itself - which is exactly the finite-state transfer matrix reading below.

## The transfer-matrix reading

Read a tower column by column with state `= previous column height`. The transfer matrix `M` on state space `N` has entries

```
M[a, b]  =  x^{max(0, b - a)}
```

so one step from height `a` to height `b` picks up `max(0, b - a)` new block-starts, weighted by `x`. With `c_0 = 0` (a boundary term making `max(0, c_1 - c_0) = c_1`) and no constraint on `c_w`,

```
T_w(x)  =  Sum_b T(w,b) x^b  =  e_0^T . M^w . 1
```

where `e_0` is the "start at height 0" indicator vector and `1` is the all-ones vector on state space. The block-count formula is the descent-count formula of the tower (with `c_0 = 0`) and matches the definition on [[tower-heap](pages/tower-heap.md)].[^4]

This is the same finite-state DP as the signed transfer matrix `M_signed[a,b] = 1` if `a <= b` and `(-1)^{a-b}` otherwise, of [[tower-parity-sectors](pages/tower-parity-sectors.md)], with two differences: heights are unbounded here (state space `N`, not `{0..k}`), and the weight is `x^{max(0, b-a)}` rather than the sign `(-1)^{max(0, a-b)}`. The unbounded matrix admits a kernel-method / [[symbolic-method](pages/symbolic-method.md)] extraction that produces a rational GF, and the extraction verified column by column against brute force for `w = 1..7` gives the [[tower-narayana-polynomial](pages/tower-narayana-polynomial.md)] identity:[^5]

```
T_w(x)  =  Narayana_w(x) / (1 - x)^w
Narayana_w(x)  =  Sum_{k=1..w} N(w,k) x^{k-1}          N(w,k) = (1/w) C(w,k) C(w,k-1)
```

with `N(w,k)` the [[narayana-numbers](pages/narayana-numbers.md)] (A001263).[^5]

## What the Narayana factorization actually says

The `(1 - x)^w` denominator is the Cartier-Foata cell-count denominator from § "Cell count via Cartier-Foata inversion". Reading the identity that way,

```
T_w(x) . (1 - x)^w  =  Narayana_w(x)          (a polynomial in x, degree w - 1)
```

says the block-count GF is obtained from the cell-count GF `1/(1-x)^w` by *replacing the constant-1 numerator with the Narayana polynomial*. Combinatorially the coefficient version reads

```
T(w,b)  =  Sum_{k=1..w} N(w,k) . C(b + w - k, w - 1)
```

as "pick `k in {1..w}` in `N(w,k)` ways, then a weak composition of `b - k + 1` into `w` parts in `C(b+w-k, w-1)` ways".[^5] An explicit peaks refinement was tested and does not factor the tower this way, which is why the A001263 cross-reference draft states the identity at the level of generating functions rather than as a peaks bijection.[^6] The statistic that does factor it is descents. `k - 1` is the number of **descents** of the height sequence (positions `i` with `c_i > c_{i+1}`): towers of width `w` with `b` blocks and `k - 1` descents number exactly `N(w,k) C(b+w-k, w-1)`. By the reversal symmetry, ascents give the same distribution. This was verified by brute force over all height vectors for `w ≤ 7`, `b ≤ 7`, during the second pass on [[algebraic-languages-and-polyominoes-enumeration](pages/algebraic-languages-and-polyominoes-enumeration.md)]. No proof is written yet. One reading (own reasoning) is that `Narayana_w(x)/(1-x)^w` has the "h-polynomial over `(1-x)^w`" shape, with descents in the role they play for Eulerian numbers in Worpitzky's identity.

The heap-theoretic content of the Narayana numerator is therefore what a proof would have to supply: a labelling of trace-monoid elements (or of Cartier-Foata trivial heaps) whose signed count over the tower's dependency structure produces `Sum_k N(w,k) x^{k-1}`. The direct interval-piece attempt above already shows this is not a matter of choosing "the obvious" piece basis - some non-trivial refinement of either the pieces or their weights is required.

## The commutation-monoid thread

Two concrete directions the trace-monoid framing suggests:

- **Path-graph dependency.** Replace the diagonal dependency `u_i R u_j iff i = j` with the path-graph dependency `u_i R u_j iff |i - j| <= 1` and weight pieces by an extra variable `y` that tracks *horizontal adjacency of segments in the same row* (the merger event that the interval-heap attempt got wrong). The trivial heaps are then the independent sets of the path `P_w`, of which there are `F_{w+2}` (Fibonacci), and the Cartier-Foata sum takes the Fibonacci-shape `Sum_k (-1)^k C(w-k, k) x^k y^0` on the `y = 0` slice. Whether the resulting bivariate GF specializes on some `y`-slice to `Narayana_w(x) / (1-x)^w` is the concrete calculation this framing invites, and would be the commutation-monoid derivation of the Narayana numerator that closes the [[tower-heap](pages/tower-heap.md)] thread.

- **The commutant of `M`.** The signed transfer matrix of [[tower-parity-sectors](pages/tower-parity-sectors.md)] has a two-element commutant `<JD>` (reflect heights, flip odd-height signs) that produces the parity-sector factorization of the signed characteristic polynomial `char_k`. The unsigned block-count matrix `M` above has its own commutant, and any combinatorial symmetry of the block-count GF (row reversal, tower reflection, cell/block statistics interchange) is a matrix in this commutant. Identifying them is one route into the sector structure a Viennot-style proof of the Narayana factorization would predict, and connects this page to the "Full commutant of `M_k`" open item in the E Department.

Both are open items on the [[tower-heap](pages/tower-heap.md)] thread; this page has done the setup, not the closing.

## Verification

Cell-count GF at small `w`, matching multichoose `C(n + w - 1, w - 1)`:

```
w=1:  1/(1-x)      = 1 + x + x^2 + ...              [C(n,0) = 1: unique tower per cell count]
w=2:  1/(1-x)^2    = 1 + 2x + 3x^2 + 4x^3 + ...     [C(n+1, 1) = n + 1: partitions of n into 2 heights]
```

Block-count GF at small `w`, from the tower-narayana identity of [[tower-narayana-polynomial](pages/tower-narayana-polynomial.md)]:

```
w=1:  1/(1-x)                                       T(1,b) = 1               [one tower per b: c_1 = b]
w=2:  (1 + x)/(1-x)^2                               T(2,b) = 2b + 1          [odd numbers, A005408]
w=3:  (1 + 3x + x^2)/(1-x)^3                        T(3,b) = ...             [A005891, centered pentagonal]
```

The Narayana polynomial `1 + 3x + x^2 = N(3,1) + N(3,2) x + N(3,3) x^2` matches row 3 of A001263: `1, 3, 1`. Full width-row table (w = 2..7 including the new-for-OEIS rows w = 6, 7) is on [[tower-narayana-polynomial](pages/tower-narayana-polynomial.md)].

Interval-piece Cartier-Foata sum (framework that fails), at `w = 2`:

```
Sum_k (-1)^k C(2+k, 2k) x^k  =  1 - 3x + x^2
1 / (1 - 3x + x^2)           =  1 + 3x + 8x^2 + 21x^3 + ...        (Fibonacci bisection, A001906)
tower row w=2                =  1, 3, 5, 7, 9, ...                  (odd numbers, A005408)
```

matches at `x^0, x^1` and diverges at `x^2`: the interval-heap has `8` at `x^2` (correctly enumerating abstract heaps of 2 non-overlapping-column-compatible intervals) whereas the tower has `5`.

## Appearances in Sources

- [[tower-narayana-polynomial](pages/tower-narayana-polynomial.md)] - the block-count identity `T_w(x) = Narayana_w(x)/(1-x)^w`, verified `w = 1..7`, and the Viennot heap-of-pieces framing of the tower.

## Related Concepts

- [[tower-heap](pages/tower-heap.md)] - the object being counted, and the thread this page walks.
- [[narayana-numbers](pages/narayana-numbers.md)] - the numerator of the block-count GF.
- [[tower-parity-sectors](pages/tower-parity-sectors.md)] - the signed transfer matrix and its commutant, the parity-sector sibling of the commutation-monoid thread.
- [[generalized-dyck-grammar](pages/generalized-dyck-grammar.md)] - the tower-word grammar the transfer matrix reads out.
- [[castle-foata-transform](pages/castle-foata-transform.md)] - blocks as maximal positive runs; the peak / record dictionary the block-start weighting realizes.
- [[symbolic-method](pages/symbolic-method.md)] - the analytic-combinatorics framework the transfer-matrix extraction sits in.
- [[stack-polyomino-gf](pages/stack-polyomino-gf.md)] - Bousquet-Melou stack-polyomino generating functions, the polyomino cousin of this construction.
- [[bousquet-melou-fedou-1995-convex-polyominoes](pages/bousquet-melou-fedou-1995-convex-polyominoes.md)] - parallelogram polyominoes as heaps of segments, the heap explanation of their `J_1/J_0` quotient form.

## Footnotes

[^3]: [[tower-narayana-polynomial](pages/tower-narayana-polynomial.md)] `raw/oeis-pe502/xrefs/A001263-tower.md` §"The tower object (self-contained definition)" L29-34 - "each block is a horizontal segment of adjacent cells at some height, every block rests on the floor or on the block directly below it (nothing floats or overhangs), and two blocks in the same row are separated by at least one empty cell ... its number of blocks is the number of maximal horizontal runs, c_1 + Sum_{i=2..w} max(0, c_i - c_{i-1})."

[^4]: [[tower-narayana-polynomial](pages/tower-narayana-polynomial.md)] `raw/oeis-pe502/xrefs/A001263-tower.md` §"The tower object (self-contained definition)" L34 - the descent-count block formula the transfer matrix `M[a,b] = x^{max(0,b-a)}` implements column-by-column; verified column-by-column against `python3 tower.py` for `w = 1..7` on the same raw file §"Identity (verified)" L23.

[^5]: [[tower-narayana-polynomial](pages/tower-narayana-polynomial.md)] `raw/oeis-pe502/xrefs/A001263-tower.md` §"Identity (verified)" L14-21 - "A tower of width w has, by number of blocks, the generating function sum_b (number of towers of width w with b blocks) x^b = ( sum_{k=1..w} N(w,k) x^{k-1} ) / (1 - x)^w. Equivalently, the number of towers of width w with exactly b blocks is sum_{k=1..w} N(w,k) * C(b + w - k, w - 1). This is verified for w = 1..7 by python3 tower.py (DP == closed form == brute force)."

[^6]: [[tower-narayana-polynomial](pages/tower-narayana-polynomial.md)] `raw/oeis-pe502/xrefs/A001263-tower.md` §"Identity (verified)" L24-25 - "It is a generating-function identity, not a 'peaks' bijection: a direct peaks refinement was tested and does not factor this way, so do not state a peaks interpretation."
