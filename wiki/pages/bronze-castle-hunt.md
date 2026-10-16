---
title: The bronze-by-spectrum search - castle graphs with spectral radius (3 + √13)/2
category: Analyses
summary: A search for a castle that is bronze by spectrum, one whose castle graph has largest adjacency eigenvalue exactly the bronze mean δ_3 = (3 + √13)/2 = 3.3028. Factoring δ_3·I − A one cell at a time and counting negative pivots, which by Sylvester's law of inertia counts the eigenvalues above δ_3, prunes a search over every skyline in twelve boxes from 22 wide x 3 tall to 5 wide x 32 tall, about 7.1 x 10^11 skylines counting box overlaps. None is bronze by spectrum. The 55 distinct floating-point near-misses, the closest 2.3 x 10^-12 above δ_3, all have a nonzero integer determinant det(A^2 − 3A − I), so δ_3 is not an eigenvalue of any of them. Two constructions are ruled out by proof: no rectangle has δ_3 as an eigenvalue (averaging over the Galois group of a cyclotomic field leaves only 2.618 and 0.382), and no castle graph has an equitable partition into two groups with quotient eigenvalue δ_3, the way the 3 x 2 rectangle is silver by spectrum. An exhaustive search over quotient matrices, with a SAT solver for a local test on 7 x 7 patches of the grid, extends the second to equitable partitions into three, four or five groups. Among the 28,251 castles up to 6 x 6 (one per mirror pair), no eigenvalue is within 4.5 x 10^-5 of δ_3.
tags: [analysis, castle, spectral, adjacency, spectral-radius, metallic-means, bronze-ratio, search, pruning, inertia, galois, equitable-partition, near-miss, implementation, verification]
sources: [project-euler-502-representations]
created: 2026-09-24
updated: 2026-10-16
---

# The bronze-by-spectrum search - castle graphs with spectral radius (3 + √13)/2

## The question

The **castle graph** has the cells of a castle as vertices, with two cells joined when they share an edge ([[castle-graph](pages/castle-graph.md)]). Its adjacency matrix `A` has a 1 wherever two cells touch, and the largest eigenvalue of `A` is the graph's **spectral radius**. Every cell has at most 4 neighbors, and no castle graph is 4-regular, so the spectral radius of a castle graph lies in `[0, 4)` ([[castle-graph-spectral-radius](pages/castle-graph-spectral-radius.md)]).

The metallic means `δ_a = σ_a^1 = (a + √(a² + 4))/2` are golden `δ_1 = 1.618`, silver `δ_2 = 2.414`, bronze `δ_3 = (3 + √13)/2 = 3.3028`, then `δ_4 = 4.236` and beyond ([[metallic-means](pages/metallic-means.md)]). A castle is **golden by spectrum** when its castle graph has spectral radius `δ_1`, **silver by spectrum** at `δ_2` ([[castle-classification-spectrum](pages/castle-classification-spectrum.md)]), and, on this page, **bronze by spectrum** at `δ_3`. The six 4-cell castles whose graph is the path `P_4` are golden by spectrum; in a scan of 4,868,525 castles up to mirror image, 36 are silver by spectrum, the 3 x 2 rectangle among them, and none is bronze by spectrum; and no castle has spectral radius `δ_4` or larger, since these exceed 4 ([[castle-graph-spectral-radius](pages/castle-graph-spectral-radius.md)]).

This page searches a far larger set of skylines for a castle bronze by spectrum and finds none; it also proves that two natural constructions cannot give one, and by a computer search excludes equitable partitions into at most five groups.

## Terms used on this page

- **Skyline** - the column heights of a castle, left to right; the skyline `(3, 3)` is the rectangle 2 columns wide and 3 tall. Every skyline is a castle of height its tallest column, and the castle graph depends only on the skyline.
- **Box** - all skylines at most `W` columns wide and `H` tall. "12 x 8" means width at most 12 and height at most 8.
- **Near-miss** - a skyline whose spectral radius agrees with `δ_3` to 8 or more decimal places without being equal to it.
- **Pivot** - a diagonal entry `d_k` when a symmetric matrix is factored as `L D Lᵀ`, with `L` lower triangular with unit diagonal and `D` diagonal; this is Gaussian elimination for symmetric matrices.
- **Characteristic polynomial** - `det(xI − A)`, whose roots are the eigenvalues. `δ_3` is a root of `x² − 3x − 1`, so `δ_3` is an eigenvalue of `A` exactly when `x² − 3x − 1` divides the characteristic polynomial, that is, when the integer `det(A² − 3A − I)` is 0.

## The search rule: count negative pivots

Sylvester's law of inertia states that a real symmetric matrix `M = L D Lᵀ` and the diagonal matrix `D` have the same numbers of positive, negative and zero eigenvalues. Applied to `M = δ_3·I − A`, it says that **the number of negative pivots equals the number of eigenvalues of `A` above `δ_3`**, and a zero pivot means `δ_3` itself is an eigenvalue.

Order the cells column by column, bottom to top. Then every initial run of cells is itself a skyline (whole columns plus the bottom part of the current column), and adding a cell adds one new pivot without changing the earlier ones. The search grows a skyline one cell at a time:

```
for each new cell k (its left neighbor and the cell below are the only 1s in its row of A):
    d_k = pivot of M at k, computed from the previous rows (at most 2H of them)
    if d_k < 0:   stop - this skyline has an eigenvalue above δ_3,
                  and so does every larger skyline containing it
    if d_k ~ 0:   record a candidate
    else:         continue with a taller column or the next column
```

The stopping rule is exact. An initial run of cells is an induced subgraph of every skyline that extends it, and by eigenvalue interlacing an induced subgraph has at most as many eigenvalues above `δ_3` as the whole graph. So the search covers every skyline in a box while visiting only those with spectral radius below `δ_3`.

With the target set to `δ_2` the search returns exactly the 14 skylines up to 7 x 6 that are silver by spectrum, among them `(3, 3)`, `(2, 2, 2)`, `(1, 2, 3, 1, 2, 3)` and `(2, 1, 6, 2, 1, 3)`; with the targets `δ_1` and `φ²` it returns the known castles of those radii.[^exec]

## What the search found

| box (widest x tallest) | skylines in the box | visited (spectral radius below `δ_3`) | near-misses |
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

The box `W x H` holds `H + H² + ⋯ + H^W` skylines, about `7.1 x 10^11` in all, counting skylines that lie in more than one box. **None is bronze by spectrum.**

Every candidate was settled exactly by the integer `det(A² − 3A − I)`. For all 55 distinct near-misses it is nonzero (the smallest in absolute value is `−132,311`), so `δ_3` is not an eigenvalue of any of them. The closest four:

```
(4,4,1,4,4,1,3,5,3,1,2,4,5,4,5,1)   51 cells   radius − δ_3 = +2.3e-12   det = 562,573,376
(4,5,2,2,2,6,4,2,5,6,3,4,4)         49 cells   radius − δ_3 = +4.8e-12   det = −16,457,361,649
(6,2,2,6,2,5,2,1,3,3,5,7,4)         48 cells   radius − δ_3 = +6.4e-12   det = 23,633,026,236
(5,4,1,4,4,1,3,5,3,1,2,4,5,4,5,1)   52 cells   radius − δ_3 = +7.0e-12   det = 35,446,316,688
```

## How a tower moves the radius

In the skyline `(1, 1, k, 1, 1, 1, 4, 1, 6, 5, 6, 3, 2)` a tower of height `k` stands on the third column:

```
k = 3    radius − δ_3 = −2.4e-10
k = 4                   +1.6e-11
k = 5                   +4.6e-11
k = 6                   +4.9e-11
k = 7                   +4.9e-11
```

The radius increases with `k` and converges. Each extra cell multiplies the increase by about `0.114` (the increases are `2.6 x 10^-10`, `3.0 x 10^-11`, `3.4 x 10^-12`, `3.8 x 10^-13`), which is `r²` for the smaller root `r` of `x² − ρx + 1` at `ρ = δ_3`: along a hanging path the Perron eigenvector satisfies `x_{j+1} = ρ x_j − x_{j−1}` and decays by the factor `r` per cell. So appendages of different lengths move the radius by amounts down to `10^-11` and below. A castle is bronze by spectrum only if `x² − 3x − 1` divides its characteristic polynomial, which no near-miss satisfies.

Among all 28,251 castles up to 6 wide and 6 tall, one per mirror pair, no eigenvalue of any castle graph lies within `4.5 x 10^-5` of `δ_3`; the closest is an eigenvalue of `(4, 3, 4, 6, 3, 4)`.[^exec]

## Two constructions that cannot give δ_3

### Rectangles

The eigenvalues of the `m x n` rectangle are the sums `2cos(jπ/(m+1)) + 2cos(kπ/(n+1))` with `1 ≤ j ≤ m`, `1 ≤ k ≤ n`.

**Proposition.** No eigenvalue of any rectangle equals `δ_3`.

*Proof.* Write `2cos(jπ/(m+1)) = z + 1/z` with `z = e^{ijπ/(m+1)}`, a root of unity of some exact order `r ≥ 3` (it is not `±1`), and write the second term as `y + 1/y` with `y` of exact order `s ≥ 3`. The primitive `r`-th roots of unity sum to the Möbius value `μ(r)` (which is 0 if `r` has a repeated prime factor, and `+1` or `−1` for an even or odd number of prime factors), so the average of `z + 1/z` over them is `2μ(r)/tot(r)`, with `tot(r)` the number of integers in `1..r` coprime to `r`. Suppose `z + 1/z + y + 1/y = δ_3`. Then `δ_3` lies in a cyclotomic field `Q(ζ_N)`, and every automorphism of that field maps the equation to another true one. Averaging over all of them, `z` and `y` run uniformly over the primitive roots of orders `r` and `s`, and `δ_3` goes to itself and to its conjugate `(3 − √13)/2` equally often, so

```
2μ(r)/tot(r) + 2μ(s)/tot(s)  =  3/2.
```

If `tot(n) ≥ 6`, then `|2μ(n)/tot(n)| ≤ 1/3`. The orders `n ≥ 3` with `tot(n) < 6` are `3, 4, 5, 6, 8, 10, 12`, with values `2μ(n)/tot(n) = −1, 0, −1/2, 1, 0, 1/2, 0`. Two values summing to `3/2` must therefore be `1` and `1/2`, so `{r, s} = {6, 10}`. Order 6 gives `z + 1/z = 1`, and order 10 gives `φ` or `−1/φ`, so the eigenvalue is `1 + φ = 2.618` or `1 − 1/φ = 0.382`, not `δ_3`. ∎

A direct check of every rectangle eigenvalue up to 300 x 300 agrees: the closest to `δ_3` is `2.0 x 10^-8` away, at 238 x 252.[^exec]

### Two groups with equal neighbor counts

A partition of the cells into groups is **equitable** when, for any two groups `X` and `Y`, every cell in `X` has the same number of neighbors in `Y`. The table of those counts, the quotient matrix, then has the spectral radius of the graph as its own largest eigenvalue. The 3 x 2 rectangle `(3, 3)` with its four corners and two middle cells is an example:

- every corner touches 1 corner and 1 middle cell;
- every middle cell touches 2 corners and 1 middle cell.

The quotient `[[1, 1], [2, 1]]` has characteristic polynomial `x² − 2x − 1`, whose largest root is `δ_2`, so `(3, 3)` is silver by spectrum. The castle `(4, 4)` has the quotient `[[1, 1], [1, 2]]` and spectral radius `φ²`, and the path `P_4` has `[[0, 1], [1, 1]]` and `φ`.

**Proposition.** No castle graph has an equitable partition into two groups whose quotient has largest eigenvalue `δ_3`.

*Proof.* A quotient `[[a, b], [c, d]]` with nonnegative integer entries has largest eigenvalue `δ_3` exactly when `a + d = 3` and `ad − bc = −1`, with `b, c ≥ 1` since the graph is connected. A cell of the first group has `a + b` neighbors and a cell of the second `c + d`. The possible tables:

| `a, d` | `b, c` | what the partition would need |
|---|---|---|
| 0, 3 | 1, 1 | a set of cells (the second group) in which every cell has 3 neighbors in the set |
| 3, 0 | 1, 1 | the same for the first group |
| 1, 2 | 1, 3 | cells of the second group with 5 neighbors |
| 2, 1 | 3, 1 | cells of the first group with 5 neighbors |
| 1, 2 | 3, 1 | every cell of the castle with at least 3 neighbors |
| 2, 1 | 1, 3 | every cell of the castle with at least 3 neighbors |

A cell has at most 4 neighbors. In any finite set of cells, the leftmost cell of the lowest row has no neighbor in the set below it or to its left, so it has at most 2 neighbors in the set. Every row of the table is ruled out. ∎

### Three, four and five groups with equal neighbor counts

For an equitable partition into `k` groups, write `Q = (q_ij)` for the quotient matrix: every cell of group `i` has `q_ij` neighbors in group `j`. The largest eigenvalue of `Q` is the spectral radius of the castle graph, so a castle bronze by spectrum with such a partition gives a quotient with largest eigenvalue `δ_3`. Three conditions restrict `Q`:

- **Degree.** Every row of `Q` sums to at most 4.
- **Corners.** The groups can be ordered so that a cell of each group has at most 2 neighbors in its own group and the groups after it. In any union of groups, the leftmost cell of the lowest row has at most 2 neighbors in the union, and by equitability so has every cell of its group; take that group first among the remaining ones and repeat.
- **Local fit.** Around any cell, the groups of the nearby cells match `Q` at every cell whose four neighbors are all nearby.

The quotient of a connected castle graph is irreducible, and the group sizes `n_i > 0` satisfy `n_i q_ij = n_j q_ji`, so `q_ij > 0` exactly when `q_ji > 0`. An exhaustive search over the integer matrices satisfying these conditions, followed by the local-fit test, gives:[^groups]

| groups | quotients with largest eigenvalue `δ_3` satisfying the degree and corner conditions | of those, passing the local fit |
|---|---|---|
| 2 | 0 | - |
| 3 | 0 | - |
| 4 | 36 | 0 |
| 5 | 390 | 6 as sets of grid cells, 0 as castles |

The local-fit test asks a SAT solver whether a 7 x 7 patch of the grid, centered on a cell of a given group, can be labeled with groups and empty squares so that every cell of the inner 5 x 5 has the neighbor counts its row of `Q` prescribes. Each of the 36 quotients with four groups, and 384 of the 390 with five, has a group with no such patch. A castle with that partition would supply the patch, so none of these quotients comes from a castle, or from any finite or infinite set of grid cells. The other six quotients with five groups have patches up to 11 x 11 as sets of grid cells, but none once the castle condition is added (every column rises from one base row without gaps): in each, some group has no 7 x 7 patch. None of the six is realized by a finite set of cells in a box up to 12 x 12. The golden, silver and `φ²` quotients above pass the test for every group, with and without the castle condition.

*Example.* One of the 36 quotients with four groups has rows `(0, 1, 0, 0)`, `(1, 0, 2, 0)`, `(0, 3, 0, 1)`, `(0, 0, 3, 1)` and characteristic polynomial `(x − 1)(x + 3)(x² − 3x − 1)`. A cell of group 4 has three neighbors in group 3 and one in group 4, and a cell of group 3 has three in group 2 and one in group 4. Let `X` be a cell of group 4 and, by symmetry of the grid, `Y` its neighbor of group 4 to its right. The cell `U` above `X` is in group 3, and its group-4 neighbor is `X`, so its other three neighbors are in group 2, among them the cell above `Y`. That cell is also a neighbor of `Y` other than `X`, so it is in group 3. No cell is in both groups.

So a castle bronze by spectrum has no equitable partition into five or fewer groups.

## Results

- No skyline in the twelve boxes is bronze by spectrum, and `δ_3` is not an eigenvalue of any of the 55 near-misses.
- No rectangle has `δ_3` as an eigenvalue.
- No equitable partition into two groups gives `δ_3`, and by an exhaustive search with a SAT solver, none into three, four or five groups.
- No castle up to 6 x 6 has an eigenvalue within `4.5 x 10^-5` of `δ_3`.

Whether some larger castle is bronze by spectrum is not settled by these results.

## Related Concepts

- [[castle-graph-spectral-radius](pages/castle-graph-spectral-radius.md)] - the castles golden and silver by spectrum, the scan of 4,868,525 castles up to mirror image, and the bound 4 that excludes `δ_4` and beyond.
- [[castle-classification-spectrum](pages/castle-classification-spectrum.md)] - the predicates golden and silver by spectrum.
- [[metallic-means](pages/metallic-means.md)] - de Spinadel's metallic means, with `δ_3 = σ_3^1` the bronze mean.
- [[castle-graph](pages/castle-graph.md)] - the castle graph.
- [[spectral-analysis](pages/spectral-analysis.md)] - the spectra attached to a castle.
- [[isospectral-castles](pages/isospectral-castles.md)] - castles with non-isomorphic graphs and equal spectra.

## Appearances in Sources

- [[project-euler-502-representations](pages/project-euler-502-representations.md)] - castles as skylines of column heights, the representation the search enumerates.

## Footnotes

[^exec]: Verified by execution (2026-09-24). Search: a C program factoring `δ_3·I − A` one cell at a time in column-major, bottom-up order; it stops a branch when a pivot is below `10^-11` and records every pivot within `10^-8` of zero. The smallest recorded pivot in absolute value was `3.7 x 10^-10`, so no branch was stopped for being close to zero. It was validated on `δ_2` (14 skylines up to 7 x 6, all pivots below `2 x 10^-13` in absolute value), `δ_1` and `φ²`. The 64 recorded candidates (55 distinct, since boxes overlap) were checked with NumPy `eigvalsh` and an exact SymPy fraction-free (Bareiss) determinant of `A² − 3A − I`: all nonzero. Rechecked (Python 3.11 with NumPy, SymPy and mpmath, 2026-10-16): the four closest near-misses (radius − `δ_3` to 40 digits, and their determinants), the tower family for `k = 3..9`, the 14 skylines up to 7 x 6 silver by spectrum, the 28,251 mirror classes up to 6 x 6 (closest eigenvalue to `δ_3` at distance `4.48 x 10^-5`), every rectangle eigenvalue up to 300 x 300, the values `2μ(n)/tot(n)` for `n < 2000`, and the box sizes `H + ⋯ + H^W`. The search over the twelve boxes was not rerun.
[^groups]: Verified by execution (Python 3 with NumPy and python-sat, CaDiCaL 1.5.3, 2026-10-10), script `bin/python/bronze_groups.py`, run log `bin/python/bronze_groups-run.log`. Quotients: every `k x k` matrix of nonnegative integers for `k = 2, …, 5` in the corner order (row `i` sums to at most 2 over columns `i, …, k` and to at most 4 in all), batched through `numpy.linalg.eigvals`, keeping largest eigenvalue modulus within `10^-8` of `δ_3`, then irreducible and with consistent group sizes: none at `k = 2`; none at `k = 3` (24 before the corner condition, counting relabelings); 36 of 1,808,625 at `k = 4`; 390 of 1,093,062,600 at `k = 5`. Local fit: a `(2R + 1) x (2R + 1)` window, one label per cell (empty or a group), the center fixed to group `g`, and a clause ruling out each forbidden assignment of the four neighbors of every inner cell; castle condition: a base-row variable, every cell below the base empty, and a nonempty cell above an empty one only on the base row. At `R = 3`, all 36 four-group and 384 five-group quotients have a failing group; the other six fit for every group at `R = 3, 4, 5` without the castle condition and fail with it at `R = 3, 4, 5`. Finite search in an `N x N` box with every cell constrained and every group present: no solution for the six at `N = 6, 8, 10, 12`. Controls `[[0, 1], [1, 1]]` (`φ`), `[[1, 1], [2, 1]]` (`δ_2`) and `[[1, 1], [1, 2]]` (`φ²`) fit for every group at `R = 4`, with and without the castle condition. The characteristic polynomial of the example quotient rechecked with SymPy (2026-10-16).
