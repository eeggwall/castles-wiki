---
title: Castle eigenvalues by example
category: Concepts
summary: Small castles worked by hand - draw the castle, number the cells, write the adjacency matrix of the castle graph, factor the characteristic polynomial, read off the eigenvalues and what they count in walks. Covers the castles with at most four cells, the six castles golden by spectrum (graph P_4), the 3 × 2 rectangle, silver by spectrum, three one-cell changes, the smallest pair of castles with non-isomorphic graphs and the same adjacency spectrum (10 cells), and the 4 × 2 rectangle with spectral radius φ². Also separates the four matrices whose eigenvalues appear on the wiki - adjacency, Laplacian, transfer matrix and char_k.
tags: [concept, castle, eigenvalue, spectral, adjacency-matrix, pedagogy, worked-example, tutorial]
sources: [project-euler-502-brute-force, oeis-mining-pe502]
created: 2026-09-19
updated: 2026-10-22
---

# Castle eigenvalues by example

Eigenvalues appear on many castle pages, among them [[castle-graph-spectral-radius](pages/castle-graph-spectral-radius.md)], [[spectral-analysis](pages/spectral-analysis.md)], [[eigenvalue-continued-fractions](pages/eigenvalue-continued-fractions.md)], [[castle-eigenvalue-oeis-crosswalk](pages/castle-eigenvalue-oeis-crosswalk.md)] and [[isospectral-castles](pages/isospectral-castles.md)], and they are eigenvalues of different matrices. This page names the four matrices and then works small castles by hand, from the drawing to the spectrum.

## Four matrices

- **The adjacency matrix `A`** of the castle graph, with one vertex per cell and an edge between two cells that share a side ([[castle-graph](pages/castle-graph.md)]). The castle graph is connected, its largest eigenvalue `λ_1(A)` is its spectral radius, and the number of walks of length `n` grows like `λ_1^n`. Every cell has at most four neighbors, and every castle graph has spectral radius below 4 ([[castle-graph-spectral-radius](pages/castle-graph-spectral-radius.md)]).
- **The Laplacian `L = D − A`**, with `D` the diagonal matrix of degrees. Its eigenvalues are at least 0, and 0 has multiplicity equal to the number of connected components, so 1 for a castle (Brouwer and Haemers, Proposition 1.3.7). The second-smallest eigenvalue, the algebraic connectivity, is positive exactly when the graph is connected (§1.7), and by the matrix-tree theorem every cofactor of `L` is the number of spanning trees (Proposition 1.3.4).[^3]
- **The transfer matrix `M`** of a family of castles defined by a rule on neighboring columns: the 0/1 matrix on the heights `1, …, h` with `M[a][b] = 1` when a column of height `a` may be followed by one of height `b`. Its largest eigenvalue is the growth constant of the family by width ([[castle-strip](pages/castle-strip.md)], [[castle-classification-growth](pages/castle-classification-growth.md)]).
- **The polynomial `char_k(λ)`** of the linear recurrence of the signed tower count `P(k, ·)` in the base length ([[signed-tower-count](pages/signed-tower-count.md)]). Its roots are not the eigenvalues of any castle graph. In the other direction, at fixed base length `L`, the recurrence of `P(·, L)` in `k` has only the roots `±1`, with characteristic polynomial `(λ + 1)^L (λ − 1)^{L−2}` for `4 ≤ L ≤ 12` (computed, [[signed-tower-k-direction](pages/signed-tower-k-direction.md)]).

The four are unrelated matrices, and the same number can come from two of them for different reasons. The castle `(1, 1, 2)` is golden by spectrum, since its castle graph is the path `P_4`, whose spectral radius is the golden mean `φ` (section *The six castles golden by spectrum*). It is also a Fibonacci castle, a castle of height 2 with no two neighboring columns of height 2, and the Fibonacci castles are golden by width, since their rule has transfer matrix `[[1, 1], [1, 0]]` ([[castle-classification-growth](pages/castle-classification-growth.md)]). The two `φ`s are eigenvalues of a `4 × 4` and of a `2 × 2` matrix that have nothing to do with each other.

The rest of the page is about the adjacency matrix unless it says otherwise.

## The recipe

1. Draw the castle, one square per cell, at positions `(i, j)` for column `i` and height `j`, both counted from 0.
2. Number the cells `v_0, v_1, …` column by column, bottom to top.
3. Write the adjacency matrix: `A[u, v] = 1` when the cells `u` and `v` share a side, otherwise 0. `A` is symmetric with zero diagonal.
4. Compute the characteristic polynomial `p_A(λ) = det(λI − A)`, factor it, and read off the eigenvalues.

Every matrix, polynomial and walk count on this page was computed with SymPy.[^1]

### `(1)`: one cell

```
■
```

One vertex, no edges: `A = [0]`, `p_A(λ) = λ`, eigenvalue 0. There are no walks of positive length.

### `(2)` and `(1, 1)`: two cells

```
(2)      (1, 1)
■
■        ■ ■
```

Both are the path `P_2`, with

```
A  =  [[0, 1],
       [1, 0]],          p_A(λ)  =  λ² − 1  =  (λ − 1)(λ + 1).
```

The eigenvalues are `1` and `−1`. From each cell there is exactly one walk of each length, so the number of walks of length `n` is 2 for every `n`: the spectral radius 1 means no growth. The two castles have the same graph, so they have the same spectrum; the spectrum is a property of the graph, not of the drawing.

### `(1, 2)` and `(1, 1, 1)`: three cells

```
(1, 2)      (1, 1, 1)
  ■
■ ■         ■ ■ ■
```

Both are the path `P_3`. Numbering `(1, 2)` as `v_0 = (0, 0)`, `v_1 = (1, 0)`, `v_2 = (1, 1)`:

```
A  =  [[0, 1, 0],
       [1, 0, 1],
       [0, 1, 0]],          p_A(λ)  =  λ³ − 2λ  =  λ(λ² − 2).
```

The eigenvalues are `0, √2, −√2`, and the spectral radius is `√2 = 1.414…`. A walk alternates between the middle cell, with two ways on, and an end cell, with one way on, so the number of walks from the middle cell doubles every two steps: 2, 2, 4, 4 for the lengths 1, 2, 3, 4, a factor `√2` per step.

### `(2, 2)`: the 4-cycle

```
■ ■
■ ■
```

The four cells of a `2 × 2` square, each with two neighbors, form the 4-cycle `C_4`. With `v_0 = (0, 0)`, `v_1 = (0, 1)`, `v_2 = (1, 0)`, `v_3 = (1, 1)`:

```
A  =  [[0, 1, 1, 0],
       [1, 0, 0, 1],
       [1, 0, 0, 1],
       [0, 1, 1, 0]],          p_A(λ)  =  λ⁴ − 4λ²  =  λ²(λ − 2)(λ + 2).
```

The eigenvalues are `2, 0, 0, −2`. The graph is regular of degree 2, so 2 is its largest eigenvalue (Brouwer and Haemers, Proposition 1.3.8), and there are `4·2^n` walks of length `n`: four starting cells and two choices per step. Coloring the cells like a chessboard gives neighboring cells opposite colors, so the graph is bipartite and its spectrum is symmetric about 0 (Proposition 3.4.1).[^3]

### `(1, 2, 1)`: the star

```
  ■
■ ■ ■
```

The middle column has height 2 and the outer columns height 1. The cell `(1, 0)` has three neighbors and the other three cells one each: the star `K_{1,3}`. With `v_0 = (0, 0)`, `v_1 = (1, 0)`, `v_2 = (1, 1)`, `v_3 = (2, 0)`:

```
A  =  [[0, 1, 0, 0],
       [1, 0, 1, 1],
       [0, 1, 0, 0],
       [0, 1, 0, 0]],          p_A(λ)  =  λ⁴ − 3λ²  =  λ²(λ² − 3).
```

The eigenvalues are `0, 0, √3, −√3`. A walk alternates between the center, with three ways on, and a leaf, with one, so the number of walks grows by a factor 3 every two steps, `√3` per step.

### `(2, 1, 2)`: the path on five cells

```
■   ■
■ ■ ■
```

With `v_0 = (0, 0)`, `v_1 = (0, 1)`, `v_2 = (1, 0)`, `v_3 = (2, 0)`, `v_4 = (2, 1)`:

```
A  =  [[0, 1, 1, 0, 0],
       [1, 0, 0, 0, 0],
       [1, 0, 0, 1, 0],
       [0, 0, 1, 0, 1],
       [0, 0, 0, 1, 0]],          p_A(λ)  =  λ⁵ − 4λ³ + 3λ  =  λ(λ − 1)(λ + 1)(λ² − 3).
```

The graph is the path `P_5`, `v_1 − v_0 − v_2 − v_3 − v_4`, with eigenvalues `√3, 1, 0, −1, −√3`. Its spectral radius `√3` equals that of the star `(1, 2, 1)`, while the other eigenvalues differ (`K_{1,3}` has `0` twice, `P_5` has `±1` and a single `0`). The spectral radius alone does not determine the graph.

### The six castles golden by spectrum

```
(4)    (1, 3)    (3, 1)    (1, 1, 2)    (2, 1, 1)    (1, 1, 1, 1)
■
■        ■       ■
■        ■       ■             ■        ■
■      ■ ■       ■ ■       ■ ■ ■        ■ ■ ■        ■ ■ ■ ■
```

All six have the path `P_4` as their graph, with

```
p_A(λ)  =  λ⁴ − 3λ² + 1  =  (λ² − λ − 1)(λ² + λ − 1).
```

The first factor has the roots `φ = (1 + √5)/2` and `−1/φ`, the second `−φ` and `1/φ`. The spectral radius is the golden mean `φ = 1.618…`, so these six castles are **golden by spectrum**. A castle with at most three cells has spectral radius 0, 1 or `√2`. Of the eight castles with four cells, these six have the graph `P_4`, and the other two are the 4-cycle `(2, 2)` and the star `(1, 2, 1)`. No castle of any other size is golden by spectrum ([[castle-classification-spectrum](pages/castle-classification-spectrum.md)], the section *Castles golden and silver by spectrum*).

### `(2, 2, 2)`: the 3 × 2 rectangle

```
■ ■ ■
■ ■ ■
```

The graph is the Cartesian product `P_3 □ P_2`. The eigenvalues of a Cartesian product are the sums `μ + ν` of an eigenvalue `μ` of one factor and `ν` of the other (Brouwer and Haemers, §1.4.6), and the path `P_n` has the eigenvalues `2cos(πj/(n + 1))` (§1.4.4):[^3]

```
P_3:            √2, 0, −√2
P_2:            1, −1
P_3 □ P_2:      √2 + 1, √2 − 1, 1, −1, −(√2 − 1), −(√2 + 1)

p_A(λ)  =  (λ − 1)(λ + 1)(λ² − 2λ − 1)(λ² + 2λ − 1).
```

The spectral radius is the silver mean `δ_2 = 1 + √2 = 2.414…`, the root of `λ² − 2λ − 1`, so the rectangle is **silver by spectrum**. So is the 12-cell castle `(1, 2, 3, 1, 2, 3)`: its characteristic polynomial is `λ²(λ − 1)(λ + 1)(λ² − 2λ − 1)(λ² + 2λ − 1)(λ⁴ − 6λ² + 6)`, with largest root `1 + √2`. Among the 4,868,525 castles up to mirror image scanned on [[castle-graph-spectral-radius](pages/castle-graph-spectral-radius.md)], 36 are silver by spectrum.[^1]

## Three one-cell changes

**`(1, 1, 1)` to `(1, 1, 2)`.** One cell on top of the last column turns the graph `P_3` into `P_4`, and the spectral radius rises from `√2 = 1.414` to `φ = 1.618`: the castle becomes golden by spectrum.

**`(1, 1, 1, 1)` to `(2, 1, 1, 1)`.** One cell on top of the first column gives the path `P_5`, `v_1 − v_0 − v_2 − v_3 − v_4`, so the spectral radius rises from `φ` to `2cos(π/6) = √3 = 1.732`, and the castle is no longer golden by spectrum.[^1]

**`(2, 2)` to `(2, 2, 1)`.** One cell in a new column gives the 4-cycle with one pendant cell, with `p_A(λ) = λ(λ⁴ − 5λ² + 2)` and spectral radius `2.1358`. The largest eigenvalue of a connected graph increases strictly when a vertex or an edge is added (Brouwer and Haemers, Proposition 3.1.1), so it rises from 2.[^3]

## Two castles with the same spectrum

Castles with isomorphic graphs, such as the six castles golden by spectrum, have the same spectrum because the spectrum is a property of the graph. The question is whether castles with non-isomorphic graphs can share a spectrum. For graphs in general they can, and the smallest such pair has 5 vertices: the star `K_{1,4}` and the 4-cycle with an isolated vertex, `C_4 + K_1`, both with characteristic polynomial `λ⁵ − 4λ³` (Brouwer and Haemers, §1.3.7; McKay, §1).[^3][^4] Castle graphs are connected, and the smallest castles with non-isomorphic graphs and the same adjacency spectrum have 10 cells:[^2]

```
(1, 1, 1, 2, 3, 2)        (1, 1, 2, 2, 3, 1)
        ■                         ■
      ■ ■ ■                   ■ ■ ■
■ ■ ■ ■ ■ ■               ■ ■ ■ ■ ■ ■
```

Both have width 6, height 3 and 10 cells, and both contain a `3 × 2` rectangle of cells with one cell on top. In the first the extra cell stands on the middle column of the rectangle, which gives its cell `(4, 1)` four neighbors; in the second it stands on an end column, and no cell has four neighbors. So the graphs are not isomorphic, and yet both have

```
p_A(λ)  =  λ¹⁰ − 11λ⁸ + 34λ⁶ − 36λ⁴ + 12λ²,
```

with the eigenvalues `±2.583181`, `±1.627286`, `±1`, `±0.824085` and `0` twice. The same spectrum means the same number of closed walks of every length: `trace Aⁿ = 0, 22, 0, 106, 0, 634` for `n = 1, …, 6`. The total numbers of walks `𝟙ᵀAⁿ𝟙` differ, `138` against `142` at `n = 3`, since they also depend on the eigenvectors.

[[isospectral-castles](pages/isospectral-castles.md)] finds all such pairs through 16 cells. Sandpile invariants separate this pair. Both castles have the sandpile group `Z/15` in the sink model and `Z/8` in the tide model ([[sandpile-group](pages/sandpile-group.md)]), but their sink-model clocks tick 15 and 5 times ([[sandcastle-clock](pages/sandcastle-clock.md)]), and one grain on the apex of the identity sets off 57 topplings in the first and 1 in the second ([[sandpile-identity](pages/sandpile-identity.md)]).

## The 4 × 2 rectangle: spectral radius φ²

The castle `(4, 4)` has 8 cells and the graph `P_4 □ P_2`, with

```
p_A(λ)  =  (λ² − 3λ + 1)(λ² − λ − 1)(λ² + λ − 1)(λ² + 3λ + 1).
```

The middle factors are those of `P_4`. The factor `λ² − 3λ + 1` has the roots `φ² = (3 + √5)/2` and `1/φ²`, so the spectral radius is `φ² = 1 + φ = 2.618…`, the sum of the spectral radii `φ` of `P_4` and `1` of `P_2`.

The leading eigenvalue shows in walk counts. The numbers of walks of length `n = 1, …, 7` in `P_4` are `𝟙ᵀAⁿ𝟙 = 6, 10, 16, 26, 42, 68, 110`, and the ratios `10/6 = 1.667`, `16/10 = 1.6`, `26/16 = 1.625`, `42/26 = 1.615`, …, `110/68 = 1.6176` approach `φ = 1.61803…`.[^1]

The 10-cell castle `(1, 3, 2, 3, 1)` also has spectral radius `φ²`: its characteristic polynomial is `(λ − 1)(λ + 1)(λ² − 3λ + 1)(λ² − λ − 1)(λ² + λ − 1)(λ² + 3λ + 1)`. The scan on [[castle-graph-spectral-radius](pages/castle-graph-spectral-radius.md)] finds 11 castles up to mirror image with spectral radius `φ²`.

## Transfer matrices

A transfer matrix belongs to a family of castles, not to one castle: its states are the column heights `1, …, h`, and its largest eigenvalue is the growth constant of the family by width ([[castle-strip](pages/castle-strip.md)]). The numbers `φ` and `1 + √2` appear there too: the Fibonacci castles are golden by width, and the anchored 1-smooth strips on the heights `{1, 2, 3}`, counted by the Pell numbers, are silver by width ([[pell-castle-strip](pages/pell-castle-strip.md)]).

## The roots of char_k

The characteristic polynomial `char_k` of the recurrence of `P(k, ·)` has degree `k + 1`. For odd `k ≤ 31` it is irreducible over the rationals, and for even `k` it splits into two factors by the parity of the last column ([[tower-parity-sectors](pages/tower-parity-sectors.md)]). The largest root of `char_6` is `2ψ²`, twice the square of the plastic number `ψ` ([[signed-tower-count](pages/signed-tower-count.md)], [[castle-eigenvalue-oeis-crosswalk](pages/castle-eigenvalue-oeis-crosswalk.md)], Part 4). [[generating-function-gallery](pages/generating-function-gallery.md)] tabulates `char_k` and its roots.

## Appearances in Sources

- [[project-euler-502-brute-force](pages/project-euler-502-brute-force.md)] - the skyline model of a castle that the examples use.
- [[oeis-mining-pe502](pages/oeis-mining-pe502.md)] - the characteristic polynomials `char_k` of the signed tower count.

## Related Concepts

- [[castle-polyomino](pages/castle-polyomino.md)] - the castle definition.
- [[castle-graph](pages/castle-graph.md)] - the castle graph and its invariants.
- [[castle-graph-spectral-radius](pages/castle-graph-spectral-radius.md)] - the spectral radii of castle graphs: the six castles golden by spectrum, the 36 silver by spectrum and the 11 with spectral radius `φ²` in the scan.
- [[castle-classification-spectrum](pages/castle-classification-spectrum.md)] - the spectral types, and the proof that only the six castles with graph `P_4` are golden by spectrum.
- [[isospectral-castles](pages/isospectral-castles.md)] - all castles through 16 cells with non-isomorphic graphs and the same adjacency or Laplacian spectrum.
- [[hear-the-shape-seminar](pages/hear-the-shape-seminar.md)] - a seminar on what the spectrum of a castle graph determines.
- [[castle-strip](pages/castle-strip.md)] - transfer matrices of families of castles.
- [[spectral-analysis](pages/spectral-analysis.md)] - the spectra computed for castles and what each decides.
- [[eigenvalue-continued-fractions](pages/eigenvalue-continued-fractions.md)] - the continued fractions of quadratic eigenvalues such as `1 + √2`.
- [[castle-eigenvalue-oeis-crosswalk](pages/castle-eigenvalue-oeis-crosswalk.md)] - the convergents of castle eigenvalues against the OEIS.
- [[signed-tower-k-direction](pages/signed-tower-k-direction.md)] and [[generating-function-gallery](pages/generating-function-gallery.md)] - the eigenvalues of the recurrences of `P(k, L)` in `k` and in `L`.
- [[metallic-means](pages/metallic-means.md)] - de Spinadel's metallic means, among them `φ` and `1 + √2`.
- [[castle-snippets](pages/castle-snippets.md)] - the `castle_graph` and `castle_graph_radius` snippets.
- [[sandpile-group](pages/sandpile-group.md)], [[sandcastle-clock](pages/sandcastle-clock.md)] and [[sandpile-identity](pages/sandpile-identity.md)] - the sandpile invariants that separate the 10-cell pair.

## Footnotes

[^1]: Verified by execution (Python 3.11, SymPy 1.14, 2026-10-16): the adjacency matrices and factored characteristic polynomials of `(1)`, `(2)`, `(1, 1)`, `(1, 2)`, `(1, 1, 1)`, `(2, 2)`, `(1, 2, 1)`, `(2, 1, 2)`, `(2, 1, 1, 1)`, the six 4-cell paths, `(2, 2, 2)`, `(1, 2, 3, 1, 2, 3)`, `(2, 2, 1)`, `(4, 4)` and `(1, 3, 2, 3, 1)`; the spectral radius `2.135779…` of `(2, 2, 1)`; the walk counts `𝟙ᵀAⁿ𝟙` of `P_4` for `n ≤ 7`. The counts 36 and 11 are those of the scan on castle-graph-spectral-radius.
[^2]: Verified by execution (Python 3.11, NumPy, SymPy, networkx 3.4.2, 2026-10-16): among all castles with at most 10 cells, mirror images removed, `(1, 1, 1, 2, 3, 2)` and `(1, 1, 2, 2, 3, 1)` are in the first group of non-isomorphic castle graphs with the same exact characteristic polynomial; their eigenvalues, `trace Aⁿ` for `n ≤ 6`, `𝟙ᵀA³𝟙 = 138, 142`, degree sequences, and the sandpile groups `Z/15` (sink at the bottom-left cell) and `Z/8` (tide) by Smith normal form.
[^3]: https://aeb.win.tue.nl/2WF02/spectra.pdf (A. E. Brouwer and W. H. Haemers, *Spectra of Graphs*, monograph version of February 1, 2011, read 2026-10-16) - Proposition 1.3.4, p.5 (the number of spanning trees is any cofactor of `L`, "known as the Matrix-Tree Theorem"); §1.3.7, p.7: "Proposition 1.3.7 The multiplicity of 0 as a Laplace eigenvalue of an undirected graph Γ equals the number of connected components of Γ", "Proposition 1.3.8 Let the undirected graph Γ be regular of valency k. Then k is the largest eigenvalue of Γ", and "both K1,4 and K1 +C4 have spectrum 2^1, 0^3, (−2)^1"; §1.4.4, p.9: the path `P_n` has spectrum "2 cos(π j/(n + 1)) (j = 1, . . . , n)"; §1.4.6, p.10: for a Cartesian product, "w(x,y) = u_x v_y is an eigenvector ... with ordinary or Laplace eigenvalue θ + η"; §1.7, p.13: "µ2(Γ) ≥ 0, with equality if and only if Γ is disconnected"; Proposition 3.1.1, p.33: for a connected graph, "(iii) The value θ0(Γ) decreases when vertices or edges are removed"; Proposition 3.4.1(i), p.38: "A graph Γ is bipartite if and only if for each eigenvalue θ of Γ, −θ is also an eigenvalue".
[^4]: https://users.cecs.anu.edu.au/~bdm/papers/SpectralTrees.pdf (B. D. McKay, "On the spectral characterisation of trees", *Ars Combinatoria* 3 (1977) 219-232, read 2026-10-16) - §1, p.219: "the smallest pair of \"cospectral\" graphs having only 5 vertices [2]", reference [2] being Collatz and Sinogowitz, "Spektren endlicher Grafen" (1957).
