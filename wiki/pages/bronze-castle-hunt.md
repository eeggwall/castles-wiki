---
title: The bronze castle hunt - is (3 + sqrt 13)/2 ever a castle's spectral radius?
category: Analyses
summary: Searches for a castle whose graph (cells as dots, touching cells joined) has largest eigenvalue exactly the bronze ratio (3 + sqrt 13)/2 = 3.3028, the third metallic mean after golden and silver. An exact pruning rule - factor bronze times the identity minus the adjacency matrix one cell at a time and count negative pivots, which equals the number of eigenvalues above bronze - covers every skyline in twelve boxes from 22 wide x 3 tall to 5 wide x 32 tall, about 7.1 x 10^11 skylines counting box overlaps, about 150 times the earlier 4.87-million scan. No bronze castle: 55 distinct floating-point near-misses, the closest 2.3 x 10^-12 away, all ruled out by a nonzero integer determinant of A^2 - 3A - I. Two proofs close off the obvious constructions: no rectangle has bronze as any eigenvalue (averaging over the number field's symmetries leaves only 2.618 and 0.382), and no castle splits into two evenly connected groups whose neighbour counts give bronze (every such split needs a cell with 5 neighbours or a finite grid patch where every cell has 3), which is exactly how the 3 x 2 rectangle gets silver. Among all 28,251 castles up to 6 x 6, bronze is not even a lower eigenvalue. Near-misses are cheap because a dangling tower moves the radius by about 10^-11; an exact hit needs sqrt 13 in the characteristic polynomial, and nothing seen produces it.
tags: [analysis, castle, spectral, adjacency, spectral-radius, metallic-means, bronze-ratio, search, pruning, inertia, galois, equitable-partition, near-miss, implementation, verification]
sources: [project-euler-502-representations]
created: 2026-09-24
updated: 2026-09-24
---

# The bronze castle hunt - is (3 + sqrt 13)/2 ever a castle's spectral radius?

## The question in plain words

Draw a castle's cells as dots and join two dots with a line when their cells share an edge. That drawing is the castle's **graph**, and its **adjacency matrix** `A` has a 1 wherever two cells touch. The largest eigenvalue of `A` is the graph's **spectral radius**: a single number that grows as the shape gets more tightly connected. For any castle it lies strictly between 0 and 4, since no cell has more than 4 neighbours.

The **metallic means** are the numbers `(a + sqrt(a^2 + 4))/2` for `a = 1, 2, 3, ...`: golden `1.618`, silver `2.414`, bronze `(3 + sqrt 13)/2 = 3.3028`, then copper `4.236` and beyond ([[metallic-means](pages/metallic-means.md)]). [[castle-graph-spectral-radius](pages/castle-graph-spectral-radius.md)] found castles whose spectral radius is exactly golden (the six 4-cell paths) and exactly silver (36 castles, starting with the 3 x 2 rectangle), and showed copper and beyond are impossible because they exceed 4. Bronze sits below 4, and none of 4.87 million castles had it.

This page asks: **does any castle have spectral radius exactly bronze?** The answer found here: none in any box searched, which now covers about 150 times as many shapes, plus two proofs that rule out the two natural ways one could be built. The question stays open.

## Terms used on this page

- **Skyline** - the column heights of a castle, left to right, e.g. `(3,3)` is the 3-tall, 2-wide rectangle. Every skyline is a castle at its own height `h`; the graph only depends on the skyline.
- **Box** - all skylines at most `W` columns wide and `H` tall. "12 x 8" means width up to 12, height up to 8.
- **Near-miss** - a castle whose spectral radius agrees with bronze to about 8 or more decimal places without being equal.
- **Pivot** - the numbers on the diagonal when a symmetric matrix is factored as `L D L^T` (lower-triangular, diagonal, transpose), which is Gaussian elimination for symmetric matrices.
- **Characteristic polynomial** - `det(xI - A)`, whose roots are the eigenvalues. Bronze is a root of `x^2 - 3x - 1`, so bronze is an eigenvalue exactly when that quadratic divides the characteristic polynomial.

## The search rule: count negative pivots

A theorem of Sylvester (the law of inertia) says: factor the symmetric matrix `M = bronze * I - A` as `L D L^T`, and **the number of negative pivots equals the number of eigenvalues of `A` above bronze**. A zero pivot means bronze itself is an eigenvalue.

Order the cells column by column, bottom to top. Then every initial run of cells is itself a skyline (whole columns plus the bottom part of the current one), and adding a cell adds exactly one new pivot without changing the earlier ones. So the search grows a skyline one cell at a time:

```
for each new cell k (left neighbour and cell below are the only 1s in its row of A):
    d_k = pivot of M at k, computed from the previous rows (at most 2H of them)
    if d_k < 0:   stop - this skyline has an eigenvalue above bronze,
                  and so does every larger skyline containing it
    if d_k ~ 0:   record a candidate (bronze is, to rounding, the spectral radius)
    else:         keep going: taller column, or the next column
```

The stopping rule is exact, not a heuristic: a castle's graph is connected, and adding a cell to a connected graph strictly raises the spectral radius, so once one piece is above bronze every skyline containing it is too. That lets the search cover every skyline in a box while visiting only those whose spectral radius is below bronze. Each new pivot costs about `H^2` arithmetic steps, and the search runs at roughly 60 million skylines per second on one core.

Checked against the known answers first: with the target set to silver it returns exactly the silver castles of [[castle-graph-spectral-radius](pages/castle-graph-spectral-radius.md)] (all 14 up to 7 x 6, including `(3,3)`, `(1,2,3,1,2,3)` and `(2,1,6,2,1,3)`), and with golden and `phi^2` the known golden and `phi^2` castles.[^exec]

## What the search found

| box (widest x tallest) | skylines in the box | visited (spectral radius below bronze) | near-misses |
|---|---|---|---|
| 22 x 3 | 4.7 x 10^10 | 4.7 x 10^10 | 0 |
| 18 x 4 | 9.2 x 10^10 | 8.2 x 10^10 | 0 |
| 16 x 5 | 1.9 x 10^11 | 1.3 x 10^11 | 9 |
| 14 x 6 | 9.4 x 10^10 | 4.8 x 10^10 | 21 |
| 13 x 7 | 1.1 x 10^11 | 4.3 x 10^10 | 25 |
| 12 x 8 | 7.9 x 10^10 | 2.4 x 10^10 | 6 |
| 10 x 12 | 6.8 x 10^10 | 1.0 x 10^10 | 1 |
| 9 x 14 | 2.2 x 10^10 | 2.9 x 10^9 | 2 |
| 8 x 16 | 4.6 x 10^9 | 6.0 x 10^8 | 0 |
| 7 x 20 | 1.3 x 10^9 | 1.6 x 10^8 | 0 |
| 6 x 24 | 2.0 x 10^8 | 2.8 x 10^7 | 0 |
| 5 x 32 | 3.5 x 10^7 | 5.5 x 10^6 | 0 |

About `7.1 x 10^11` skylines in total, counting shapes that lie in more than one box. **No bronze castle.**

Every candidate was then settled exactly. Bronze is an eigenvalue of `A` exactly when `det(A^2 - 3A - I) = 0`, and that determinant is an integer, computed without rounding. For all 55 distinct near-misses it is nonzero (the smallest in size is `-132,311`), so none of them has bronze in its spectrum at all. The closest four:

```
(4,4,1,4,4,1,3,5,3,1,2,4,5,4,5,1)   51 cells   radius - bronze = +2.3e-12   det = 562,573,376
(4,5,2,2,2,6,4,2,5,6,3,4,4)         49 cells   radius - bronze = +4.8e-12   det = -16,457,361,649
(6,2,2,6,2,5,2,1,3,3,5,7,4)         48 cells   radius - bronze = +6.4e-12   det = 23,633,026,236
(5,4,1,4,4,1,3,5,3,1,2,4,5,4,5,1)   52 cells   radius - bronze = +7.0e-12   det = 35,446,316,688
```

## Why near-misses are cheap

One family of near-misses shows the mechanism. In `(1,1,k,1,1,1,4,1,6,5,6,3,2)`, a single tower of height `k` stands on the third column:

```
k = 4    radius - bronze = +1.6e-11
k = 5    +4.6e-11
k = 6    +4.9e-11
k = 7    +4.9e-11
```

The eigenvector for the top eigenvalue shrinks roughly geometrically along a thin dangling tower, so each extra cell on it moves the spectral radius by less than the one before. With thin appendages of different lengths in different places, a castle can land as close to bronze as you like. Near-misses at the `10^-11` level are therefore expected in any search of this size and are not evidence of anything. An exact hit is a different kind of event: `x^2 - 3x - 1` has to divide the characteristic polynomial, which needs `sqrt 13` to appear in the castle's spectrum.

A related check points the same way: among all 28,251 castles up to 6 wide and 6 tall (each shape counted once with its mirror image), **bronze is not even a lower eigenvalue** of any of them.

## Two constructions that provably cannot work

### Rectangles

The eigenvalues of an `m x n` rectangle are the sums `2cos(j pi/(m+1)) + 2cos(k pi/(n+1))`, one for each `1 <= j <= m`, `1 <= k <= n`. **None of them is ever bronze.**

The proof uses one fact about roots of unity. Write `2cos(j pi/(m+1)) = z + 1/z` with `z = e^{i j pi/(m+1)}`. The number `z` has some exact order `n1 >= 3`: `z^n1 = 1` for the first time at `n1`. Averaged over all roots of unity of that same exact order, `z + 1/z` comes to `2 mu(n1)/phi(n1)`. Here `phi(n)` counts the numbers from 1 to `n` sharing no factor with `n`, and `mu(n)` is `0` if `n` has a repeated prime factor, otherwise `+1` or `-1` for an even or odd number of prime factors.

Now suppose some rectangle eigenvalue equals bronze. Every symmetry of the field of roots of unity (every Galois automorphism) maps the equation to another true equation. Averaging over all of them:

- The left side averages to `2 mu(n1)/phi(n1) + 2 mu(n2)/phi(n2)`.
- The right side averages to `3/2`, because the symmetries send bronze to itself half the time and to its partner `(3 - sqrt 13)/2` the other half.

The largest possible values of `2 mu(n)/phi(n)` for `n >= 3` are `1` (at `n = 6`) and `1/2` (at `n = 10`); every other `n` gives at most `1/3`. So the only way to reach `3/2` is `n1 = 6, n2 = 10` (checked by machine for all orders below 2000, and forced by the size bound beyond). Order 6 gives `z + 1/z = 1`; order 10 gives `phi = 1.618` or `-1/phi = -0.618`. The sums are `2.618` and `0.382`. Neither is bronze. The same argument covers every eigenvalue of every rectangle, not just the largest.[^exec]

### Two evenly connected groups

Silver and golden castles have a simple explanation. Split the 3 x 2 rectangle's cells into corners and middles:

- every corner touches 1 corner and 1 middle
- every middle touches 2 corners and 1 middle

When every cell in a group has the same neighbour counts like this (an **equitable partition**), the small table of counts `[[1,1],[2,1]]` has the graph's spectral radius as its own largest eigenvalue. That table's characteristic polynomial is `x^2 - 2x - 1`, whose largest root is silver. The `phi^2` castle `(4,4)` works the same way with table `[[1,1],[1,2]]`, and the golden 4-cell path with `[[0,1],[1,1]]`.

**No castle can do this for bronze.** A table `[[a,b],[c,d]]` of whole-number counts gives bronze exactly when `a + d = 3` and `ad - bc = -1`. A cell in the first group then has `a + b` neighbours, a cell in the second `c + d`. The four possibilities:

| `a, d` | `b, c` | what the split would need |
|---|---|---|
| 0, 3 | 1, 1 | the second group forms a patch where every cell touches 3 others in its group |
| 3, 0 | 1, 1 | the first group forms such a patch |
| 1, 2 or 2, 1 | 1, 3 | some cells with 5 neighbours |
| 1, 2 or 2, 1 | 3, 1 | every cell in the castle has at least 3 neighbours |

A cell on a square grid has at most 4 neighbours. And any finite set of cells has a lowest-leftmost cell, with nothing to its left or below, so at most 2 neighbours in that set. Every row of the table is ruled out. A bronze castle, if one exists, has to get bronze from a split into three or more groups, or with no even split at all.

## Where this leaves the question

Settled here:

- no bronze castle in any of the twelve boxes above
- no rectangle has bronze as any eigenvalue
- no two-group even split gives bronze
- bronze is not an eigenvalue of any castle up to 6 x 6

Still open:

- whether any castle at all has spectral radius exactly bronze
- the sharper question behind it: whether any castle has `sqrt 13` anywhere in its spectrum

The near-miss mechanism shows a bigger search can only produce closer misses. The way forward is a reason why `x^2 - 3x - 1` never divides a castle's characteristic polynomial, or a construction with three or more even groups that forces it.

## Related Concepts

- [[castle-graph-spectral-radius](pages/castle-graph-spectral-radius.md)] - the golden and silver castles, the 4.87-million-castle scan, and why copper and beyond are impossible.
- [[metallic-means](pages/metallic-means.md)] - the golden, silver, bronze ladder.
- [[castle-graph](pages/castle-graph.md)] - the castle's cells as a graph.
- [[spectral-analysis](pages/spectral-analysis.md)] - the spectra attached to a castle.
- [[isospectral-castles](pages/isospectral-castles.md)] - different castles with the same spectrum, the other exact-coincidence hunt on castle graphs.

## Appearances in Sources

- [[project-euler-502-representations](pages/project-euler-502-representations.md)] - castles as skylines of column heights, the representation the search enumerates.

## Footnotes

[^exec]: Verified by execution (2026-09-24). Search: a C program compiled with `clang -O3`, factoring `bronze * I - A` one cell at a time in column-major, bottom-up order; it stops a branch when a pivot is below `10^-11` and records every pivot within `10^-8` of zero. The smallest recorded pivot in size was `3.7 x 10^-10`, so no branch was stopped for being close to zero, only for being negative. It was validated first on silver (14 castles up to 7 x 6, all pivots below `2 x 10^-13` in size), golden, and `phi^2`. Twelve boxes ran in parallel, from 0.7 s (5 x 32) to 1586 s (16 x 5). The 64 recorded candidates (55 distinct, since boxes overlap) were checked with NumPy `eigvalsh` and an exact SymPy fraction-free (Bareiss) determinant of `A^2 - 3A - I`: all nonzero. The census of bronze as any eigenvalue covered all 28,251 mirror-deduplicated skylines with `w, h <= 6` at tolerance `10^-8`. The rectangle average used SymPy `mobius` and `totient` for all orders below 2000, and a numerical check of every rectangle eigenvalue up to 300 x 300 (closest to bronze: `2.0 x 10^-8`, at 238 x 252). All quoted numbers are the programs' printed output.
