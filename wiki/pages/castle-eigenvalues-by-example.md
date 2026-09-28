---
title: Castle eigenvalues by example
category: Concepts
summary: A pedagogy tour of eigenvalues that appear on the castle wiki. Small castles worked out end to end - draw the polyomino, write the adjacency matrix, factor the characteristic polynomial, read off the eigenvalues - with the walk-count reading of each spectrum. Includes one-cell changes that move a castle onto or off the golden-spectrum list, and two non-isomorphic castles with the same eigenvalues.
tags: [concept, castle, eigenvalue, spectral, adjacency-matrix, pedagogy, worked-example, tutorial]
sources: [project-euler-502-brute-force, oeis-mining-pe502]
created: 2026-09-19
updated: 2026-09-28
---

# Castle eigenvalues by example

Eigenvalues appear on the castle wiki in many places - [[castle-graph-spectral-radius](pages/castle-graph-spectral-radius.md)], [[spectral-analysis](pages/spectral-analysis.md)], [[eigenvalue-continued-fractions](pages/eigenvalue-continued-fractions.md)], [[castle-eigenvalue-oeis-crosswalk](pages/castle-eigenvalue-oeis-crosswalk.md)], [[isospectral-castles](pages/isospectral-castles.md)] - and each of those pages assumes the reader already knows which "eigenvalue" is meant in its context. This page works small castles by hand, from drawing the object to reading off the spectrum, with the meaning of each calculation stated after it.

## What "eigenvalue" means here

The wiki lays four different operators on a castle. Each one gives its own eigenvalues; each set of eigenvalues means a different thing physically.

- **Adjacency matrix `A`** of the castle's polyomino graph (one vertex per filled cell, an edge between orthogonally adjacent cells). Eigenvalues live in `[−4, 4]` because every cell has at most four neighbours. The largest eigenvalue `λ_1(A)` is the **spectral radius**; asymptotically, the number of length-`n` walks through the graph grows like `λ_1^n`. This is the object [[castle-graph-spectral-radius](pages/castle-graph-spectral-radius.md)] catalogues.
- **Combinatorial Laplacian `L = D − A`**, where `D` is the diagonal degree matrix. Eigenvalues are `≥ 0`, the smallest is always `0` (a constant is in the kernel), and the second-smallest - the *spectral gap* - controls connectivity, mixing time, and how easy the graph is to disconnect.
- **Transfer matrix `T`** of a *class* of castles under a neighbour rule (the class's `h × h` 0/1 matrix, rows and columns indexed by column heights `1..h`). Its Perron root - largest real eigenvalue - is the **growth constant** of the class's width-graded count. This is one castle rule producing one Perron root; see [[castle-strip](pages/castle-strip.md)] for the full story and [[castle-classification-growth](pages/castle-classification-growth.md)] Axis 8 for the classification of what growth constants arise.
- **The `char_k(λ)` characteristic polynomial** of the signed-tower recurrence at fixed height bound `k`. Its roots are the eigenvalues of the count sequence `P(k, ·)` itself as an L-recurrence. Listed in [[generating-function-gallery](pages/generating-function-gallery.md)]; the k-direction of the same object collapses to `±1` on [[signed-tower-k-direction](pages/signed-tower-k-direction.md)].

**These four are different things.** A castle can be a *golden-spectrum castle* (its adjacency spectral radius is `φ`) and yet its class's transfer matrix has an entirely different Perron root, and the recurrence its counts satisfy has yet another spectrum. "The castle's eigenvalues" always needs an operator.

Everything in the rest of this page is about the **adjacency matrix** unless it says otherwise. That is the operator whose smallest examples can be computed by hand.

## Tiny castles, computed by hand

The recipe is the same every time.

1. **Draw the polyomino** - one square per filled cell, at positions `(i, j)` for column `i`, height `j`.
2. **List the cells** and number them `0, 1, 2, …` in a fixed order (below: column-major, `(0, 0), (0, 1), …, (1, 0), (1, 1), …`).
3. **Write the adjacency matrix** `A`: an entry `A[u, v] = 1` if the cells `u, v` are orthogonally adjacent (share an edge), otherwise `0`. `A` is symmetric with `0`s on the diagonal.
4. **Compute the characteristic polynomial** `p_A(λ) = det(λ I − A)`.
5. **Factor** and read off the eigenvalues.

Below, every skyline `c` gives a castle. The adjacency matrix is written row by row for readability, and every polynomial and radical was computed with SymPy.[^1]

### `(1)` - one cell

```
  ■
```

One vertex, no edges. `A = [0]`, `p_A(λ) = λ`, single eigenvalue `0`. There are no walks of positive length.

### `(2)` and `(1, 1)` - two cells

```
(2)         (1, 1)
  ■
  ■           ■ ■
```

Both have two cells and one edge. Both are the path graph `P_2` as an abstract graph. Adjacency matrix

```
A  =  [[0, 1],
       [1, 0]]
```

Characteristic polynomial `p_A(λ) = λ² − 1 = (λ − 1)(λ + 1)`. Eigenvalues `1` and `−1`.

**What the `+1` means.** The number of walks of length `n` between the two vertices is `1` when `n` is odd, `0` when `n` is even; walks that return to their start are the opposite parity. Both counts are combinations of `1^n` and `(−1)^n`. The spectral radius `1` says the total walk count stays bounded: it is `2` for every `n`.

**Two castles, one spectrum.** `(2)` (stack of two) and `(1, 1)` (row of two) are indistinguishable to the adjacency spectrum. This will keep happening: the spectrum sees the abstract graph, not the drawing.

### `(1, 2)` and `(1, 1, 1)` - three cells

```
(1, 2)         (1, 1, 1)
    ■
  ■ ■            ■ ■ ■
```

Three cells, two edges, both are `P_3`. Numbering `(1, 2)` as `v_0 = (0, 0), v_1 = (1, 0), v_2 = (1, 1)`:

```
A  =  [[0, 1, 0],
       [1, 0, 1],
       [0, 1, 0]]
```

Characteristic polynomial `p_A(λ) = λ³ − 2λ = λ (λ² − 2)`. Eigenvalues `0, √2, −√2`; spectral radius `√2 ≈ 1.414`.

**What the `√2` means.** The number of walks of length `n` grows like `(√2)^n = 2^{n/2}`. Verifiable by hand: from the middle vertex `v_1` there are 2 walks of length 1 (to `v_0` or `v_2`), 2 of length 2 (each must return), 4 of length 3 and 4 of length 4. A walk alternates between the middle (two choices) and an endpoint (one choice), so the count doubles every two steps, a factor `√2` per step.

### `(2, 2)` - the four-cycle

```
  ■ ■
  ■ ■
```

Four cells in a `2 × 2` block. Every cell has two neighbours; the graph is the 4-cycle `C_4`:

```
A  =  [[0, 1, 1, 0],
       [1, 0, 0, 1],
       [1, 0, 0, 1],
       [0, 1, 1, 0]]
```

Characteristic polynomial `p_A(λ) = λ⁴ − 4λ² = λ²(λ − 2)(λ + 2)`. Eigenvalues `2, 0, 0, −2`; spectral radius `2`.

**What the `2` means.** The graph is 2-regular (every vertex has degree 2). There are `4 · 2^n` walks of length `n` (four starting cells, two choices per step). When a graph is `d`-regular, `d` is always an eigenvalue and always the spectral radius; here `d = 2`.

**Bipartite symmetry.** `C_4` is 2-colourable (checkerboard), which makes its spectrum symmetric about `0`; bipartite adjacency spectra always are. The double `0` is particular to `C_4`.

### `(1, 2, 1)` - the star

```
    ■
  ■ ■ ■
```

Four cells: the middle-column has height 2, the outer columns height 1. The central cell `(1, 0)` has three neighbours; the other three cells each have exactly one. That is the star `K_{1, 3}` on four vertices:

```
A  =  [[0, 1, 0, 0],
       [1, 0, 1, 1],
       [0, 1, 0, 0],
       [0, 1, 0, 0]]
```

(numbering `v_0 = (0, 0), v_1 = (1, 0), v_2 = (1, 1), v_3 = (2, 0)`). Characteristic polynomial `p_A(λ) = λ⁴ − 3λ² = λ² (λ² − 3)`. Eigenvalues `0, 0, √3, −√3`; spectral radius `√3 ≈ 1.732`.

**What the `√3` means.** A walk alternates between the centre and a leaf: three choices leaving the centre, one returning, so the count grows by a factor 3 every two steps, `√3` per step.

**Two similar shapes, different graphs.** `(1, 2, 1)` and `(2, 1, 2)` (next) are both three columns with alternating heights, but their adjacency graphs differ.

### `(2, 1, 2)` - the five-path

```
  ■   ■
  ■ ■ ■
```

Five cells. The middle column is shorter, so the two "peaks" only connect through the base. Numbering `v_0 = (0, 0), v_1 = (0, 1), v_2 = (1, 0), v_3 = (2, 0), v_4 = (2, 1)`:

```
A  =  [[0, 1, 1, 0, 0],
       [1, 0, 0, 0, 0],
       [1, 0, 0, 1, 0],
       [0, 0, 1, 0, 1],
       [0, 0, 0, 1, 0]]
```

The abstract graph is `P_5` (a path with five vertices), reading `v_1 - v_0 - v_2 - v_3 - v_4`. Characteristic polynomial `p_A(λ) = λ (λ − 1)(λ + 1)(λ² − 3) = λ⁵ − 4λ³ + 3λ`. Eigenvalues `√3, 1, 0, −1, −√3`; spectral radius `√3`.

**Same radius as `(1, 2, 1)`, different castle, different graph.** `K_{1, 3}` and `P_5` both have spectral radius `√3`; the smaller eigenvalues distinguish them (`K_{1, 3}` has a double `0`; `P_5` has `±1` and a simple `0`). This is the caveat with reading only the leading eigenvalue: it is a coarse invariant.

### `(1, 1, 1, 1)` and its five siblings - the golden four-path

```
  ■ ■ ■ ■
```

Four cells in a row. Adjacency graph `P_4`. Characteristic polynomial factors as

```
p_A(λ)  =  (λ² − λ − 1)(λ² + λ − 1).
```

The first factor has roots `(1 ± √5) / 2 = φ, −1/φ`; the second has roots `−φ, 1/φ`. Eigenvalues `φ, 1/φ, −1/φ, −φ`, with spectral radius **`φ = (1 + √5) / 2 ≈ 1.618` - the golden ratio**.

**Five other castles have the same spectrum.** `(4)`, `(1, 3)`, `(3, 1)`, `(1, 1, 2)`, `(2, 1, 1)` all draw as different pictures on the grid but their adjacency graphs are all `P_4`:[^1]

```
(4)    (1, 3)    (3, 1)    (1, 1, 2)    (2, 1, 1)    (1, 1, 1, 1)
■
■        ■       ■
■        ■       ■             ■        ■
■      ■ ■       ■ ■       ■ ■ ■        ■ ■ ■        ■ ■ ■ ■
```

All six are **golden-spectrum castles**; no castle at fewer than four cells can be, and among four-cell castles these are exactly the ones whose graph is `P_4` (rather than `C_4` or the star `K_{1, 3}`). By Smith's theorem no other castle of any size has spectral radius `φ` ([[castle-graph-spectral-radius](pages/castle-graph-spectral-radius.md)]).

### `(2, 2, 2)` and the silver rectangle

```
  ■ ■ ■
  ■ ■ ■
```

The `3 × 2` rectangle. Six cells, adjacency graph is the Cartesian product `P_3 × P_2`. Eigenvalues of a Cartesian product are all sums `μ_i + ν_j` of the factors' eigenvalues:

```
P_3 eigenvalues:  √2, 0, −√2
P_2 eigenvalues:  1, −1
so P_3 × P_2:     √2 + 1, √2 − 1, 1, −1, −(√2 − 1), −(√2 + 1).
```

Spectral radius **`1 + √2 ≈ 2.414` - the silver ratio**. The characteristic polynomial factors correspondingly:

```
p_A(λ)  =  (λ − 1)(λ + 1)(λ² − 2λ − 1)(λ² + 2λ − 1).
```

The factor `λ² − 2λ − 1` is the silver-ratio polynomial, root `1 + √2`.

**A second silver-spectrum castle.** `(1, 2, 3, 1, 2, 3)` at 12 cells has a different shape; its 12th-degree characteristic polynomial contains the silver factor `λ² − 2λ − 1` and its spectral radius is `1 + √2`, so it is also a silver-spectrum castle.[^1]

## Three one-cell changes

**Tweak 1: `(1, 1, 1) → (1, 1, 2)`.** Add one cell on top of the last column. The graph goes from `P_3` (radius `√2`) to `P_4` (radius `φ`). A single cell moves the spectral radius from `1.414` to `1.618` and puts the castle on the golden-spectrum list.

**Tweak 2: `(1, 1, 1, 1) → (2, 1, 1, 1)`.** Add one cell on top of the first column. The graph is still a path (now `v_1 - v_0 - v_2 - v_3 - v_4`), still `P_5` as an abstract graph, so the spectrum jumps from the `P_4` spectrum (radius `φ`) to the `P_5` spectrum (radius `2 cos(π / 6) = √3 ≈ 1.732`). The castle leaves the golden list.[^1]

**Tweak 3: `(2, 2) → (2, 2, 1)`.** Add one cell in a new column. The graph was `C_4` (radius `2`); now it is a 4-cycle with a pendant leaf, 5 cells, characteristic polynomial `λ(λ⁴ − 5λ² + 2)`, and the spectral radius rises to about `2.136`. Adding a vertex can only raise the spectral radius, since the old graph is a subgraph of the new one, and the graph is no longer regular.

## Two castles, same spectrum, different shapes

There are two levels of "same spectrum" on the wiki.

**Trivial level: same abstract graph.** The six four-cell golden castles above all draw as `P_4`, so they trivially share every eigenvalue. Different-looking pictures, isomorphic graphs. The spectrum cannot distinguish castles whose graphs are isomorphic, because the spectrum is a graph invariant.

**Non-trivial level: non-isomorphic graphs with the same spectrum.** Two castles that draw differently, are *not* isomorphic as graphs, and yet share every eigenvalue. These are **isospectral pairs**. The smallest such pair on the castle wiki has 10 cells:[^2]

```
(1, 1, 1, 2, 3, 2)        (1, 1, 2, 2, 3, 1)
        ■                         ■
      ■ ■ ■                   ■ ■ ■
■ ■ ■ ■ ■ ■               ■ ■ ■ ■ ■ ■
```

Both are castles of width 6, height 3, 10 cells. Neither is a graph-isomorphic copy of the other. Both hold a `2 × 3` rectangle of cells (two `2 × 2` blocks sharing an edge) with a one-cell tower on top, but the first castle's tower stands on the middle column of the rectangle, giving a cell of degree 4, and the second's stands on an end column. And yet both have the same 10 eigenvalues:

```
±2.583181, ±1.627286, ±1.000000, ±0.824085, and 0 with multiplicity 2.
```

Same characteristic polynomial, so the two castles have the same number of closed walks of every length (`trace Aⁿ`: `0, 22, 0, 106, 0, 634, …`). The total walk counts `1ᵀAⁿ1` differ (`138` against `142` at `n = 3`), because they also depend on the eigenvectors.

The smallest cospectral pair in general graph theory has 5 vertices (`K_{1, 4}` and `C_4 ∪ K_1`); castles are more constrained, and 10 cells is the smallest castle pair. See [[isospectral-castles](pages/isospectral-castles.md)] for the census, exhaustive to 16 cells. Sandpile invariants separate this pair: both castles have the sink-model sandpile group `Z/15` and the tide-model group `Z/8` ([[sandpile-group](pages/sandpile-group.md)]), but their sink-model clocks tick 15 and 5 ([[sandcastle-clock](pages/sandcastle-clock.md)]), and one grain on the apex of the identity sets off 57 topplings in one and 1 in the other ([[sandpile-identity](pages/sandpile-identity.md)]).

## Scaling up: what stays and what changes

Take the `4 × 2` rectangle `(4, 4)` - 8 cells, `P_4 × P_2`. Characteristic polynomial

```
p_A(λ)  =  (λ² − 3λ + 1)(λ² − λ − 1)(λ² + λ − 1)(λ² + 3λ + 1).
```

The factors `λ² − λ − 1` and `λ² + λ − 1` are the same golden factors as in `P_4`; the new factors `λ² − 3λ + 1` and `λ² + 3λ + 1` have roots `(3 ± √5) / 2 = φ², 1/φ²` and the negatives. Spectral radius **`φ² = (3 + √5) / 2 ≈ 2.618`** - the square of the golden ratio.

**Verify by counting walks.** The number of length-`n` walks in `P_4` (from any vertex to any vertex) is `1^ᵀ A^n 1` where `A` is the `P_4` adjacency matrix. For `n = 1, 2, 3, …, 7`, that sequence is `6, 10, 16, 26, 42, 68, 110`.[^1] Each term is roughly `φ` times the previous: `10/6 = 1.667`, `16/10 = 1.6`, `26/16 = 1.625`, `42/26 = 1.615`, and the ratio converges to `φ = 1.61803…`. That is the leading eigenvalue showing up in a count that can be done by hand.

**A second `φ²`-spectrum castle.** `(1, 3, 2, 3, 1)` at 10 cells. Different shape, entirely different picture - a symmetric silhouette rising and falling - but its 10th-degree characteristic polynomial contains `(λ² − 3λ + 1)(λ² + 3λ + 1)` and its spectral radius is `φ²`, the same asymptotic walk-count growth rate.

## The transfer-matrix picture, in one paragraph

Everything above is about the adjacency matrix of *one* castle. A different sense of "castle eigenvalue" - the Perron root of a *class's* transfer matrix - shows up when the object of study is not one castle but a rule that generates infinitely many, one per width. That story is on [[castle-strip](pages/castle-strip.md)]: the states of the matrix are the column heights, one row and column per height in `1..h`, and the Perron root is the growth constant of the class's width-graded count. The numbers `φ` and `1 + √2` show up there too, from a different operator: a class's transfer matrix and one castle's adjacency matrix are unrelated matrices that happen to share these values.

## Higher-degree eigenvalues in counting

The last sense of "castle eigenvalue" is the roots of the characteristic polynomials `char_k(λ)` that come out of the counting recurrence for `P(k, L)`. These are typically **irrational and higher-degree** - cubic, quartic, quintic - because the recurrence is order `k + 1`. The dominant root of `char_6` is `2ψ²`, twice the square of the plastic number; it is treated on [[castle-eigenvalue-oeis-crosswalk](pages/castle-eigenvalue-oeis-crosswalk.md)] Part 4. The table of `char_k` and its roots is on [[generating-function-gallery](pages/generating-function-gallery.md)]. The k-direction of `P(·, L)`, going the other way, collapses to eigenvalues `±1` on [[signed-tower-k-direction](pages/signed-tower-k-direction.md)].

## Appearances in Sources

- [[project-euler-502-brute-force](pages/project-euler-502-brute-force.md)] - the column-height (skyline) castle model the examples use.
- [[oeis-mining-pe502](pages/oeis-mining-pe502.md)] - the `P(k, ·)` characteristic polynomials behind the counting-recurrence eigenvalues in the last section.

## Related Concepts

- [[castle-polyomino](pages/castle-polyomino.md)] - the object every castle here is one of.
- [[castle-graph](pages/castle-graph.md)] - the adjacency graph the page's whole first half operates on.
- [[castle-graph-spectral-radius](pages/castle-graph-spectral-radius.md)] - the Axis-9 census whose named types (golden-spectrum, silver-spectrum, `φ²`-spectrum) are the results this page's small examples land on.
- [[isospectral-castles](pages/isospectral-castles.md)] - the isospectral pair worked here in detail.
- [[castle-strip](pages/castle-strip.md)] - the transfer-matrix picture the single-paragraph aside points at.
- [[spectral-analysis](pages/spectral-analysis.md)] - the toolkit hub naming five spectra on a castle; this page treats the adjacency one.
- [[eigenvalue-continued-fractions](pages/eigenvalue-continued-fractions.md)] - what happens when an eigenvalue is a quadratic irrational and one asks about its continued fraction.
- [[castle-eigenvalue-oeis-crosswalk](pages/castle-eigenvalue-oeis-crosswalk.md)] - the OEIS entries the convergents of the eigenvalues on this page reach.
- [[signed-tower-k-direction](pages/signed-tower-k-direction.md)] / [[generating-function-gallery](pages/generating-function-gallery.md)] - the counting-recurrence eigenvalues left out of the adjacency story.
- [[metallic-means](pages/metallic-means.md)] - the family the growth constants `φ`, `1 + √2`, `(3 + √13) / 2` etc. belong to.
- [[castle-snippets](pages/castle-snippets.md)] - the `castle_graph` and `castle_graph_radius` snippets used to run every computation on this page.
- [[hear-the-shape-seminar](pages/hear-the-shape-seminar.md)] - the seminar this page's worked examples lead into.
- [[sandpile-group](pages/sandpile-group.md)] / [[sandcastle-clock](pages/sandcastle-clock.md)] / [[sandpile-identity](pages/sandpile-identity.md)] - the sink-model sandpile invariants of the 10-cell pair: same group `Z/15`, clocks 15 and 5, apex avalanches 57 and 1.

## Footnotes

[^1]: Every adjacency matrix, characteristic polynomial, eigenvalue, and walk-count sequence on this page was produced by SymPy on 2026-09-19 from the skyline. In particular: `p_A(λ)` for `c = (1, 1, 1, 1), (1, 1, 2), (1, 3), (3, 1), (2, 1, 1), (4)` all factor as `(λ² − λ − 1)(λ² + λ − 1)`, matching the golden-spectrum-castle list on [[castle-graph-spectral-radius](pages/castle-graph-spectral-radius.md)]; `p_A(λ)` for `(2, 2, 2)` and `(1, 2, 3, 1, 2, 3)` both contain the factor `λ² − 2λ − 1` (silver ratio); `p_A(λ)` for `(4, 4)` and `(1, 3, 2, 3, 1)` both contain the factor `λ² − 3λ + 1` (`φ²`). The `P_4` walk-count sequence `6, 10, 16, 26, 42, 68, 110` is `1^ᵀ A^n 1` for `n = 1..7` with `A` the `4 × 4` `P_4` adjacency matrix, and `110 / 68 = 1.6176…` converges to `φ`.
[^2]: [[isospectral-castles](pages/isospectral-castles.md)] - the smallest adjacency-isospectral castle pair `(1, 1, 1, 2, 3, 2)` and `(1, 1, 2, 2, 3, 1)`; both have 10 cells and share the 10-eigenvalue spectrum `±2.583181, ±1.627286, ±1.000000, ±0.824085, 0, 0`. Re-verified by direct enumeration during writing of this page.
