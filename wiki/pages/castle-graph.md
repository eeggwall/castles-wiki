---
title: The castle graph - bridge to graph theory
category: Concepts
summary: The castle graph of a castle has its cells as vertices and an edge between cells that share a side. It is connected, bipartite and planar, with at most 4 neighbors per cell, and its cycle rank is the number of 2×2 squares of cells. It is a tree exactly when no two neighboring columns both have height at least 2; these tree castles number F_{w+2} − 1 at height 2, and the tree skylines of height at most h satisfy T_h(w+2) = T_h(w+1) + (h−1)T_h(w), Jacobsthal at h = 3, so the tree castles of height h grow like σ_1^{h−1} = (1 + √(4h−3))/2 by width.
tags: [concept, castle, graph, polyomino, spectral, adjacency, laplacian, tree, bipartite, planar, cycle-rank, fibonacci, jacobsthal, oeis, bridge, pedagogy]
sources: [project-euler-502-brute-force, rossin-2000-group-of-a-sandpile]
created: 2026-09-17
updated: 2026-10-16
---

# The castle graph - bridge to graph theory

## Definition

Let `c = (c_1, …, c_w)` be the skyline of a castle ([[castle-polyomino](pages/castle-polyomino.md)]). Its **castle graph** `G_c` has

- as vertices the cells `(i, j)` with `1 ≤ i ≤ w` and `1 ≤ j ≤ c_i`, column `i` and row `j`;
- as edges the pairs of cells that share a side: `(i, j)` and `(i, j+1)` in one column, and `(i, j)` and `(i+1, j)` in neighboring columns, whenever both cells are in the castle.

Six castles, drawn row by row from the top with `#` for a cell:

```
(4)     (1,1,1,1)    (3,3)    (2,2,2)    (1,3,2,3,1)    (1,1,2,1,1,2,1,1)
#
#                    ##                  .#.#.
#                    ##       ###        .###.          ..#..#..
#       ####         ##       ###        #####          ########
```

The skylines `(4)` and `(1, 1, 1, 1)` have the path on 4 vertices as their graph. `(3, 3)` and `(2, 2, 2)` have 6 cells, 7 edges and two `2 × 2` squares. `(1, 3, 2, 3, 1)` has 10 cells, 11 edges and two `2 × 2` squares, and `(1, 1, 2, 1, 1, 2, 1, 1)` has 10 cells, 9 edges and none.[^1]

## Invariants of the skyline

| invariant | value |
|---|---|
| vertices `\|V\|` | the area `Σ c_i` |
| edges within columns | `Σ_i (c_i − 1) = \|V\| − w` |
| edges between columns | `Σ_{i<w} min(c_i, c_{i+1})` |
| `2 × 2` squares of cells | `Σ_{i<w} (min(c_i, c_{i+1}) − 1)` |
| cycle rank `\|E\| − \|V\| + 1` | the number of `2 × 2` squares |
| largest degree | at most 4 |

The graph is connected, since every column stands on row 1, which is a path. So its cycle rank, the number of independent cycles, is `|E| − |V| + 1`. Adding the two kinds of edges, `|E| − |V| + 1 = Σ_{i<w} min(c_i, c_{i+1}) − (w − 1) = Σ_{i<w} (min(c_i, c_{i+1}) − 1)`, the number of `2 × 2` squares, since two neighboring columns share `min(c_i, c_{i+1}) − 1` of them.

The graph is **bipartite**: coloring `(i, j)` by the parity of `i + j` gives neighboring cells opposite colors. So its adjacency spectrum is symmetric about 0; the path on 4 vertices has characteristic polynomial `x⁴ − 3x² + 1 = (x² − x − 1)(x² + x − 1)`. The graph is **planar**, drawn in the square lattice with unit edges, and it is a subgraph of the `w × h` grid graph, so its pathwidth is at most `min(w, h)`.

For the castles with at most 11 cells, and 300 larger ones, the boundary cycles of the `2 × 2` squares form a basis of the integer cycle lattice ([[sandpile-census](pages/sandpile-census.md)]), and [[sandpile-group](pages/sandpile-group.md)] computes the sandpile group from them.

## Tree castles

A **tree castle** is a castle whose graph is a tree. Since the graph is connected, this holds exactly when the cycle rank is 0: when there is no `2 × 2` square of cells, that is, when no two neighboring columns both have height at least 2. Examples are the skyline `(1, 1, …, 1)`, a horizontal path; the skyline `(h)`, a vertical path; `(2, 1, 2, 1, 2)`; `(1, 3, 1)`; and the 11-cell skyline `(1, 1, 1, 2, 1, 1, 2, 1, 1)` of [[isospectral-castles](pages/isospectral-castles.md)]. The skylines `(2, 2)`, `(3, 3)` and `(1, 2, 3, 1, 2, 3)` are not tree castles.

A tree castle has exactly one spanning tree, so its sandpile group is trivial in both the sink model and the tide model of [[sandpile-group](pages/sandpile-group.md)]; in the tide model the bottom row is contracted to one sink, which leaves a tree. The castles with at most 16 cells number 33,150 up to mirror image, and 6,963 of them are tree castles ([[sandpile-census](pages/sandpile-census.md)]).[^2]

### Counting tree castles by width

Let `T_h(w)` be the number of **tree skylines** of width `w` and height at most `h`: skylines in `{1, …, h}^w` in which no two neighboring columns both have height at least 2. A tree skyline need not reach height `h`, so it is not a castle of height `h`. Splitting by the last column, which has height 1 or is one of the `h − 1` taller heights after a column of height 1,

```
T_h(w+2)  =  T_h(w+1)  +  (h − 1)·T_h(w),        T_h(0) = 1,   T_h(1) = h.        (1)
```

The tree castles of width `w` and height `h` are the tree skylines of height at most `h` that are not of height at most `h − 1`, so they number

```
A_tree(w, h)  =  T_h(w) − T_{h−1}(w).                                              (2)
```

The characteristic polynomial of Equation (1) is `x² − x − (h − 1)`, whose larger root is

```
σ_1^{h−1}  =  (1 + √(4h − 3)) / 2,
```

de Spinadel's metallic mean with `p = 1` and `q = h − 1` ([[de-spinadel-1999-family-of-metallic-means](pages/de-spinadel-1999-family-of-metallic-means.md)], [[metallic-means](pages/metallic-means.md)]). For `h ≥ 2` it exceeds `σ_1^{h−2}`, so `A_tree(w, h)` grows like `(σ_1^{h−1})^w` too: the tree castles of heights 2, 3 and 4 are golden (`φ`), copper (`2`) and nickel (`(1 + √13)/2`) by width.

| `h` | `T_h(w)` for `w = 0, 1, …, 9` | OEIS | `σ_1^{h−1}` |
|---|---|---|---|
| 1 | `1, 1, 1, 1, 1, 1, 1, 1, 1, 1` | | `1` |
| 2 | `1, 2, 3, 5, 8, 13, 21, 34, 55, 89` | Fibonacci, `F_{w+2}` | `φ = 1.618…` |
| 3 | `1, 3, 5, 11, 21, 43, 85, 171, 341, 683` | Jacobsthal, `A001045(w+2)` | `2` |
| 4 | `1, 4, 7, 19, 40, 97, 217, 508, 1159, 2683` | `A006130(w+1)` | `(1 + √13)/2 = 2.303…` |
| 5 | `1, 5, 9, 29, 65, 181, 441, 1165, 2929, 7589` | `A006131(w+1)` | `(1 + √17)/2 = 2.562…` |

| `h` | `A_tree(w, h)` for `w = 0, 1, …, 8` |
|---|---|
| 2 | `0, 1, 2, 4, 7, 12, 20, 33, 54` |
| 3 | `0, 1, 2, 6, 13, 30, 64, 137, 286` |
| 4 | `0, 1, 2, 8, 19, 54, 132, 337, 818` |

Every entry agrees with brute-force enumeration.[^3] At height 2, `T_1(w) = 1`, so `A_tree(w, 2) = F_{w+2} − 1 = A000071(w+2)`: these are the Fibonacci castles, the castles of height 2 with no two neighboring columns of height 2 ([[fibonacci-castle](pages/fibonacci-castle.md)]). The sequences `A006130` and `A006131` satisfy `a(n) = a(n−1) + 3a(n−2)` and `a(n) = a(n−1) + 4a(n−2)`, the cases `h = 4` and `h = 5` of Equation (1).

[[tree-castle-by-area](pages/tree-castle-by-area.md)] counts the tree skylines by area. With `q` marking area, `x` marking width and `P_h(q) = q² + q³ + ⋯ + q^h`, their generating function is `(1 + P_h(q)x)/(1 − qx − qP_h(q)x²)`, since a tree skyline is a sequence of columns of height 1, each followed or not by one taller column. At `x = 1`, the tree castles of height 2 counted by area are `A077868`, one less than Narayana's cows `A000930`; the tree skylines of height at most 3 and 4 are `A006498` and `A000570`; and the tree skylines of any height are `A005251`.[^4]

## Spectral types

The spectral types of [[castle-classification-spectrum](pages/castle-classification-spectrum.md)] are properties of the castle graph:

| type | condition on `G_c` | page |
|---|---|---|
| tree castle | `G_c` is a tree | this page, section *Tree castles* |
| golden by spectrum | the largest adjacency eigenvalue is the golden ratio `φ = (1 + √5)/2`; the castle `(1, 1, 1, 1)` is one | [[castle-graph-spectral-radius](pages/castle-graph-spectral-radius.md)] |
| silver by spectrum | the largest adjacency eigenvalue is the silver ratio `1 + √2`; the castle `(2, 2, 2)` is one | [[castle-graph-spectral-radius](pages/castle-graph-spectral-radius.md)] |
| spectral radius `φ²` | the largest adjacency eigenvalue is `φ² = (3 + √5)/2` | [[castle-graph-spectral-radius](pages/castle-graph-spectral-radius.md)] |
| isospectral pair | two castles with non-isomorphic graphs and the same adjacency or Laplacian spectrum | [[isospectral-castles](pages/isospectral-castles.md)] |
| Ramanujan castle | every adjacency eigenvalue other than `±λ_1` has modulus at most `ρ(T)`, the spectral radius of the universal covering tree of `G_c` (Greenberg's condition for irregular graphs) | [[ramanujan-castles](pages/ramanujan-castles.md)] |

Here `λ_1` is the largest adjacency eigenvalue. A finite tree is its own universal cover, so every tree castle is a Ramanujan castle.

The graph is planar, so Kasteleyn's method counts its perfect matchings, and the sandpile group can be computed from the planar dual, whose bounded faces are the `2 × 2` squares; the dual-graph theorem is Cori and Rossin's ([[rossin-2000-group-of-a-sandpile](pages/rossin-2000-group-of-a-sandpile.md)]).

## Snippet

Filed on [[castle-snippets](pages/castle-snippets.md)]:

```python
import numpy as np

def castle_graph(c):
    """Adjacency matrix of the castle graph as a NumPy array."""
    cells = [(i, j) for i, h in enumerate(c) for j in range(h)]
    idx = {cell: n for n, cell in enumerate(cells)}
    A = np.zeros((len(cells), len(cells)))
    for (i, j), u in idx.items():
        for nb in ((i+1, j), (i, j+1)):
            if nb in idx: A[u, idx[nb]] = A[idx[nb], u] = 1
    return A

def is_tree_castle(c):
    """True iff G_c is a tree - equivalently, no 2x2 square of cells."""
    return all(not (c[i] >= 2 and c[i+1] >= 2) for i in range(len(c)-1))

def cycle_rank(c):
    """|E| - |V| + 1 = number of 2x2 squares of cells in the castle."""
    return sum(max(0, min(c[i], c[i+1]) - 1) for i in range(len(c)-1))
```

## Appearances in Sources

- [[project-euler-502-brute-force](pages/project-euler-502-brute-force.md)] - the skyline encoding of a castle, whose cells are the vertices of the castle graph.
- [[rossin-2000-group-of-a-sandpile](pages/rossin-2000-group-of-a-sandpile.md)] - the sandpile group of a graph and the dual-graph theorem.

## Related Concepts

- [[castle-classification-spectrum](pages/castle-classification-spectrum.md)] - the classification of castles by the spectrum of the castle graph.
- [[castle-graph-spectral-radius](pages/castle-graph-spectral-radius.md)] - the castles whose graph has spectral radius `φ`, `1 + √2` or `φ²`.
- [[isospectral-castles](pages/isospectral-castles.md)] - non-isomorphic castle graphs with the same spectrum; the smallest Laplacian pair is two tree castles with 11 cells.
- [[ramanujan-castles](pages/ramanujan-castles.md)] - Greenberg's Ramanujan condition on castle graphs, with a census to 22 cells.
- [[castle-eigenvalues-by-example](pages/castle-eigenvalues-by-example.md)] - the adjacency matrices and characteristic polynomials of small castle graphs, worked by hand.
- [[hear-the-shape-seminar](pages/hear-the-shape-seminar.md)] - a seminar on what the spectrum of the castle graph determines.
- [[spectral-analysis](pages/spectral-analysis.md)] - the spectral methods used on castle graphs.
- [[sandpile-group](pages/sandpile-group.md)] - the sandpile group of the castle graph, computed from its `2 × 2` squares; trivial for tree castles.
- [[sandpile-census](pages/sandpile-census.md)] - the sandpile groups of the 33,150 castles with at most 16 cells, up to mirror image.
- [[castle-avalanches](pages/castle-avalanches.md)] - avalanches on the castle graph; in the tide model, rectangles and battlements of the same height have the same mean avalanche, and the `2 × 2` squares change only the tail.
- [[tree-castle-by-area](pages/tree-castle-by-area.md)] - the tree skylines counted by area.
- [[unique-tournament](pages/unique-tournament.md)] - tournaments determined by their score vectors, counted by `A000570`, the tree skylines of height at most 4 by area.
- [[castle-classification-growth](pages/castle-classification-growth.md)] - families of castles by their growth by width, among them the tree castles.
- [[metallic-means](pages/metallic-means.md)] - the growth `σ_1^{h−1}` of the tree castles of height `h`.
- [[castle-by-area](pages/castle-by-area.md)] - castles counted by area, the number of vertices of the castle graph.
- [[castle-representations](pages/castle-representations.md)] - the other encodings of a castle.
- [[castle-snippets](pages/castle-snippets.md)] - `castle_graph`, `is_tree_castle`, `cycle_rank`.

## Footnotes

[^1]: Verified by execution (Python 3.11, 2026-10-16): the drawings and the counts of cells, edges and `2 × 2` squares of the six examples, from the formulas of the section *Invariants of the skyline*.
[^2]: Verified by execution (Python 3.11, 2026-10-16): the compositions of `n ≤ 16` number 33,150 up to reversal, and 6,963 of these classes have no two neighboring parts at least 2.
[^3]: Verified by execution (Python 3.11, 2026-10-16): `T_h(w)` for `h ≤ 3`, `w ≤ 9` and `h = 4, 5`, `w ≤ 7` by enumeration of all skylines, and for `w = 8, 9` from Equation (1); `A_tree(w, h)` from Equation (2) against enumeration for `w ≤ 8` at `h = 2, 3` and `w ≤ 7` at `h = 4`, and at `w = 8` from Equation (1). https://oeis.org/A001045, https://oeis.org/A006130, https://oeis.org/A006131, https://oeis.org/A000071 (read 2026-09-17 and 2026-10-04): the offsets of the table.
[^4]: Verified by execution (Python 3.11, 2026-10-16): the counts by area `n ≤ 14` of the tree castles of height 2 (`0, 1, 2, 3, 5, 8, 12, …`), and of the tree skylines of height at most 3, at most 4 and of any height, against the data of https://oeis.org/A077868, https://oeis.org/A000930, https://oeis.org/A006498, https://oeis.org/A000570 and https://oeis.org/A005251 (read 2026-10-16).
