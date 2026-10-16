---
title: Sandpile groups of castles - sand, cycles, and 2×2 blocks, in the sink and tide models
category: Concepts
summary: The sandpile group (also called the critical group) of a castle, in two models that differ only in where sand leaves. Grains sit on cells; a cell holding at least as many grains as it has neighbors topples, sending one grain to each; grains that reach the sink vanish. In the sink model the sink is one cell, and the group does not depend on which; in the tide model it is the whole bottom row. The recurrent configurations form a finite abelian group Z^{n_live}/L̃ Z^{n_live}, of order det L̃, the number of spanning trees, with L = ∂∂ᵀ for the boundary matrix ∂. The group is also Z^r modulo an r × r matrix with one row per 2×2 block, −1 for blocks sharing an edge, and on the diagonal 4 in the sink model, and 3 for a block on the bottom row and 4 above it in the tide model (checked against the cell-side computation on all 33,150 castles to 16 cells). So the sink group depends only on how the blocks touch, while the tide group also depends on which blocks sit on the bottom row: (2, 2, 2) and (3, 3) have the same graph and the sink group Z/15, but tide groups Z/8 and Z/11. Both groups are trivial exactly on the tree castles. The 2-wide ladders give A001353 in the sink model, and A001906 lying down and A001835 standing up in the tide model.
tags: [concept, castle, sandpile, abelian-sandpile, critical-group, chip-firing, laplacian, boundary-matrix, cycle-space, spanning-trees, smith-normal-form, tree-castle, planar-dual, sink-model, tide-model, pedagogy]
sources: [rossin-2000-group-of-a-sandpile, dhar-ruelle-sen-verma-1995-algebraic-aspects, dhar-1990-self-organized-critical-sandpile, chau-cheng-1991-deterministic-soc-sandpile, bak-tang-wiesenfeld-1988-self-organized-criticality, project-euler-502-castle-factoring]
created: 2026-09-26
updated: 2026-10-16
---

# Sandpile groups of castles - sand, cycles, and 2×2 blocks, in the sink and tide models

This page defines the **sandpile group** of a castle and computes it. Part 1 describes the sandpile on the castle graph ([[castle-graph](pages/castle-graph.md)]) in two models, the **sink model** and the **tide model**, which differ in where sand leaves the castle. Part 2 writes the group as a quotient of `Z^{n_live}` by the reduced Laplacian. Part 3 shows that the group is determined by the castle's `2 × 2` blocks, and in the tide model also by which of them sit on the bottom row. Part 4 lists the groups of small castles. Every result is stated for both models.

## Part 1 - the sandpile, in two models

The **castle graph** has one vertex per cell and one edge per pair of cells that share a side ([[castle-graph](pages/castle-graph.md)]). Some cells form the **sink**, where sand leaves.

- **Configuration.** A whole number of grains on every cell outside the sink.
- **Toppling.** A cell that holds at least as many grains as it has neighbors is unstable. It **topples**: it sends one grain to each neighbor. Grains sent to the sink disappear.
- **Stabilizing.** Topple unstable cells until none is left. Because the sink removes sand, this stops, and the final configuration does not depend on the order of the topplings: two unstable cells can be toppled in either order, and toppling commutes with adding a grain, so the operators `a_v`, "add a grain at `v`, then stabilize", commute. This is Dhar's abelian property, proved for any toppling matrix of this kind.[^1] A sequence of topplings started by one added grain is an **avalanche**.

**Two models.** They differ only in which cells form the sink.

| | sink model | tide model |
|---|---|---|
| the sink | one cell; on these pages the bottom-left cell | the whole bottom row |
| where sand leaves | through the sink cell's neighbors | through every cell of row 2 |
| the graph behind the model | the castle graph | the castle graph with the bottom row merged into one vertex |
| dependence on a choice | the group does not depend on which cell is the sink;[^2] the identity element and the clock do ([[sandpile-identity](pages/sandpile-identity.md)], [[sandcastle-clock](pages/sandcastle-clock.md)]) | none: the bottom row is fixed |

A cell keeps its full number of neighbors in both models, so a cell of row 2 topples at the same number of grains as before, and in the tide model one of the grains it sends falls into the sink.

**Recurrent configurations.** Drop grains on cells one at a time, stabilizing after each drop. The **recurrent** configurations are the stable configurations that occur again and again; the others, the transients, occur only finitely often. In the steady state every recurrent configuration has the same probability, and the transients have probability 0.[^3]

**The sandpile group.** The recurrent configurations, with the operation "add cell by cell, then stabilize", form a finite abelian group `K`, the **sandpile group**, also called the critical group.[^2] Write `K_sink` and `K_tide` for the two groups of the same castle. Its order is the number of spanning trees of the graph behind the model (Part 2).

### Worked example: the 4-cycle `(2, 2)` in both models

**Sink model.** `(2, 2)` is a `2 × 2` square of four cells, each with two neighbors. Make the bottom-left cell the sink. The other three cells are stable with 0 or 1 grain each, so there are `2³ = 8` stable configurations. Exactly **4** of them are recurrent, the ones with at most one empty cell:

```
recurrent (grains on top-left, bottom-right, top-right):   (0,1,1)  (1,0,1)  (1,1,0)  (1,1,1)
transient:                                                 (0,0,0)  (1,0,0)  (0,1,0)  (0,0,1)
```

So `K_sink = Z/4`, and the square has 4 spanning trees, one for each edge deleted. The identity element is `(1, 1, 0)`, one grain on each neighbor of the sink and none on the far corner: adding it to any recurrent configuration and stabilizing gives that configuration back.[^4]

**Tide model.** The bottom row is the sink. Only the two top cells hold sand, and each has two neighbors, the other top cell and the cell below it. Each holds 0 or 1 grain, so there are 4 stable configurations, and exactly **3** are recurrent, all but the empty one:

```
recurrent (grains on top-left, top-right):   (0,1)  (1,0)  (1,1)
transient:                                   (0,0)
```

So `K_tide = Z/3`. The graph behind the tide model is a triangle, the two top cells and the merged bottom row, which has 3 spanning trees. The identity is the full configuration `(1, 1)`.[^4]

### Worked example: one avalanche on the rectangle `(2, 2, 2)`

Label the six cells of the `3 × 2` rectangle:

```
top     TL  TM  TR            corners TL, TR, BL, BR have 2 neighbors;  TM, BM have 3
bottom  BL  BM  BR
```

**Sink model, sink `BL`.** Start from the fullest stable configuration, each cell one grain short of toppling, and drop one grain on `TR`. Topple the first unstable cell in the order `BL, TL, BM, TM, BR, TR` until none is left:

```
start        top [1 2 1]   bottom [S 2 1]
drop on TR   top [1 2 2]   bottom [S 2 1]
topple TR    top [1 3 0]   bottom [S 2 2]
topple TM    top [2 0 1]   bottom [S 3 2]
topple TL    top [0 1 1]   bottom [S 3 2]   <- one grain into the sink
topple BM    top [0 2 1]   bottom [S 0 3]   <- another into the sink
topple BR    top [0 2 2]   bottom [S 1 1]
topple TR    top [0 3 0]   bottom [S 1 2]
topple TM    top [1 0 1]   bottom [S 2 2]
topple BR    top [1 0 2]   bottom [S 3 0]
topple BM    top [1 1 2]   bottom [S 0 1]   <- a third into the sink
topple TR    top [1 2 0]   bottom [S 0 2]
topple BR    top [1 2 1]   bottom [S 1 0]   stable
```

One grain causes 11 topplings, and 3 grains leave through the sink: 8 grains after the drop, 5 at the end. Only `TL` and `BM`, the neighbors of the sink, send grains into it. Toppling in any other order ends at the same configuration.[^5] The castle has 15 recurrent configurations, one for each spanning tree of the `3 × 2` grid: `K_sink = Z/15`.

**Tide model.** The bottom row is the sink, so only the top row holds sand, and its cells topple at 2, 3 and 2 grains. The same drop on `TR` of the fullest stable configuration:

```
start        top [1 2 1]
drop on TR   top [1 2 2]
topple TR    top [1 3 0]   <- one grain into the sink
topple TM    top [2 0 1]   <- another
topple TL    top [0 1 1]   <- a third          stable
```

Each of the three topplings sends one grain into the sink, because each top cell stands on the bottom row. The castle has 8 recurrent configurations: `K_tide = Z/8`.[^5]

## Part 2 - the matrices behind the sandpile

**Toppling subtracts a row of the Laplacian.** The Laplacian of the castle graph is `L = D − A`, with `D` the diagonal matrix of degrees and `A` the adjacency matrix ([[hear-the-shape-seminar](pages/hear-the-shape-seminar.md)], Stop 0). When cell `v` topples it loses `deg(v)` grains and each neighbor gains one, which subtracts row `v` of `L` from the configuration. Let `L̃` be `L` with the rows and columns of the sink cells deleted, and let `n_live` be the number of cells outside the sink. Two configurations that differ by topplings are the same element of

```
K  =  Z^{n_live} / L̃ Z^{n_live}.                                                (1)
```

In the sink model `L̃` deletes one row and column, and `n_live` is the number of cells minus 1. In the tide model it deletes the bottom row, `n_live` is the number of cells minus the width, and every remaining cell keeps its full degree, so `L̃` is the Laplacian of the graph with the bottom row merged into one vertex, with that vertex's row and column deleted. By **Kirchhoff's matrix-tree theorem**, the determinant of a connected graph's Laplacian with one vertex's row and column deleted is the number of its spanning trees. So `K` is a finite abelian group of order `det L̃`, the number of spanning trees of the graph behind the model. Its structure as a product of cyclic groups `Z/d_1 × Z/d_2 × ⋯` is read off the **Smith normal form** of `L̃`, as on [[castle-ring-invariant-factors](pages/castle-ring-invariant-factors.md)].[^6]

This is Dhar's presentation in either model. Adding `deg(v)` grains at `v` forces one toppling, so the operators satisfy `∏_u a_u^{L̃_vu} = 1`, and two configurations are equivalent exactly when they differ by an integer combination of the rows of `L̃`. Dhar counts the recurrent configurations as `det L̃`.[^7]

**Entropy.** Since every recurrent configuration is equally likely, the entropy of the steady state is `ln det L̃ = ln |K|`.[^8] Dhar writes it `S`; the wiki writes `ln det L̃`, since `S(w, h)` is the signed castle count ([[castle-notation](pages/castle-notation.md)]). Tree castles have entropy 0 in both models. For the square lattice Dhar gives the entropy per site as the double integral `(2π)^{−2} ∫∫ ln(4 − 2cos θ − 2cos φ) dθ dφ = 1.16624…`, which equals `4G/π` with `G` Catalan's constant.[^9] On square castles, `ln det L̃` divided by the number of cells is:[^9]

| `ℓ` | sink model, `ℓ × ℓ` castle, corner sink | tide model, `ℓ × ℓ` cells above the bottom row |
|---|---|---|
| 10 | 0.984 | 1.050 |
| 20 | 1.076 | 1.108 |
| 40 | 1.121 | 1.137 |
| 60 | 1.136 | 1.147 |

**A test for recurrence.** Dhar defines a **forbidden subconfiguration** as a set of cells in which every cell holds fewer grains than it has neighbors inside the set, with grains counted from 0 as on this page. To test a configuration, start from the set of all cells and repeatedly delete the cells that violate this condition; either a forbidden subconfiguration is left, or the set empties and the configuration is called allowed. Dhar proves that every recurrent configuration is allowed and leaves the converse unproved.[^10]

**Deterministic sandpiles.** Chau and Cheng call a sandpile *completely deterministic* when every grain operator `a_v` acts the same way on the recurrent configurations, so that only the number of grains added matters; the group of recurrent configurations is then cyclic, and they classify the toppling matrices that have this property.[^11]

**Proposition.** A castle sandpile, in either model, is completely deterministic exactly when its group is trivial.

*Proof.* The group `K` is generated by the classes `e_v` of a grain at `v`. Suppose all `e_v` equal one element `g`. Toppling a cell `v` gives `deg(v)·e_v − Σ_{u ~ v, u ∉ sink} e_u = 0`, so `s(v)·g = 0`, where `s(v)` is the number of edges from `v` to the sink. A cell next to the sink cell, in the sink model, or a cell of row 2, in the tide model, has exactly one such edge, so `g = 0` and `K` is trivial. Conversely, if `K` is trivial every grain acts as the identity. ∎

By Part 3 the deterministic castles are therefore the tree castles, in both models.

**The Laplacian factors through the boundary matrix.** Give every edge a direction. The **boundary matrix** `∂` has one row per cell and one column per edge, with `+1` at the edge's tail and `−1` at its head. Then

```
L  =  ∂ ∂ᵀ,                                                                     (2)
```

because `(∂∂ᵀ)[u, u]` counts the edges at `u`, and `(∂∂ᵀ)[u, v] = −1` when an edge joins `u` and `v`.[^12]

## Part 3 - cycles and the 2×2 blocks

**Cycles are the kernel of `∂`.** An integer combination of edges whose boundary is zero enters every cell as often as it leaves it. These combinations form the **cycle lattice**, the kernel of `∂`, of rank equal to the **cycle rank** `|E| − |V| + 1`.

**For a castle, the cycles are generated by the 2×2 blocks.** A `2 × 2` block of cells is four cells joined in a 4-cycle, and going once around it is a cycle. A castle has no holes, so the bounded faces of its graph, drawn in the plane, are exactly its `2 × 2` blocks, and the cycle rank is the number `r` of blocks ([[castle-graph](pages/castle-graph.md)]). The `r` block cycles are an integer basis of the cycle lattice for every castle with at most 16 cells ([[sandpile-census](pages/sandpile-census.md)], section 1). Put them as the columns of the **cycle matrix** `C`, one column per block; then `∂C = 0`.

**The block matrix, sink model.** The Gram matrix `CᵀC` compares the block cycles. Each block's cycle has four edges, and two blocks that share an edge traverse it in opposite directions:

```
CᵀC[a, a]  =  4,         CᵀC[a, b]  =  −1  if blocks a and b share an edge,   0 otherwise.      (3)
```

This matrix, one row per `2 × 2` block, gives the sink group:

```
K_sink  =  Z^r / (CᵀC) Z^r.                                                     (4)
```

`CᵀC` is the reduced Laplacian of the planar dual graph, whose vertices are the blocks and the outer face, with the outer face as the sink. So Equation (4) says that the castle graph and its dual have isomorphic sandpile groups, and it agrees with Equation (1) on all 33,150 castles with at most 16 cells.[^13] The sandpile groups of dual graphs are the subject of a paper of Cori and Rossin, listed among Rossin's references.[^14] The castle `(3, 3, 3)` shows both sides. Its dual is the `2 × 2` grid of blocks with each corner block joined twice to the outer face, and Rossin quotes its group from Dhar, Ruelle, Sen and Verma as the product of cyclic groups of orders 24 and 8, which is `K_sink((3, 3, 3)) = Z/8 × Z/24`. A castle with no `2 × 2` block has no cycles, one spanning tree and a trivial group. The sink group depends only on the graph of blocks, in which two blocks are joined when they share an edge; the cells outside the blocks and the choice of sink cell do not change it.

**The tide changes the cycles.** Merging the bottom row into one vertex collapses the bottom edge of every block whose lower cells lie in the bottom row. Such a block's cycle, which went around four edges, now goes around three: its two cells in row 2 and the merged vertex. Blocks higher up keep their four edges. So the tide model's block matrix has the same `−1` entries, with a different diagonal:

```
tide block matrix[a, a]  =  3  if block a has its lower cells in the bottom row,  4  otherwise,
K_tide                   =  Z^r / (tide block matrix) Z^r.                       (5)
```

**Why 3.** Merging the bottom row contracts its horizontal edges. In a plane graph, contracting an edge is the same as deleting the corresponding edge of the dual graph. The dual edge of a bottom-row edge joins the block above it, if there is one, to the outer face, and is a loop at the outer face otherwise. So a block on the bottom row loses one of its four dual edges, and nothing else in the dual changes: the tide block matrix is the reduced Laplacian of the dual of the contracted graph, and Equation (5) is the same duality for the contracted graph. It agrees with Equation (1) on all 33,150 castles with at most 16 cells.[^13]

**The tide group depends on which blocks sit on the bottom row.** The sink block matrix depends only on the graph of blocks. The tide block matrix also records which blocks have their lower cells in the bottom row, so two castles with the same graph can have different tide groups. The rectangle `(2, 2, 2)` and the castle `(3, 3)` both have the `3 × 2` grid as their graph, lying down and standing up, and both have `K_sink = Z/15`. In `(2, 2, 2)` both blocks are on the bottom row, `[[3, −1], [−1, 3]]`, and `K_tide = Z/8`; in `(3, 3)` only the lower one is, `[[3, −1], [−1, 4]]`, and `K_tide = Z/11`.

**The tide splits a castle into runs.** A **run of raised columns** is a maximal run of adjacent columns of height at least 2. Distinct runs are separated by a column of height 1, so in the merged graph they share only the merged vertex, `L̃` is block diagonal, and the tide group is the product of the groups of the runs. Two castles with the same runs, in any order and each either way round, have the same tide group.

**Proposition.** Both groups of a castle are trivial exactly when the castle is a tree castle, a castle with no `2 × 2` block.

*Proof.* In a tree castle no two adjacent columns have height at least 2, since they would form a block with the bottom row; so the raised columns are separate vertical paths, each joined to the bottom row once, and both graphs are trees, with one spanning tree. A castle with a block has a cycle in both graphs, a 4-cycle or a triangle through the merged vertex, hence at least 3 spanning trees and a nontrivial group in both models. ∎

## Part 4 - the castle gallery

| castle | description | 2×2 blocks | block arrangement | `K_sink` | `K_tide` |
|---|---|---|---|---|---|
| `(1, 1, 1, 1)`, `(1, 2, 1)`, `(1, 2, 1, 3, 1)` | tree castles: a path, golden by spectrum (castle-graph spectral radius `φ`); one raised column; a battlement, raised columns separated by height-1 columns | 0 | - | trivial | trivial |
| `(2, 2)` | the 4-cycle | 1 | one block, on the bottom row | `Z/4` | `Z/3` |
| `(2, 2, 2)` | the `3 × 2` rectangle, silver by spectrum (spectral radius `1 + √2`) | 2 | side by side, both on the bottom row | `Z/15` | `Z/8` |
| `(3, 3)` | the same graph as `(2, 2, 2)`, standing up | 2 | stacked, one on the bottom row | `Z/15` | `Z/11` |
| `(1, 2, 3, 2, 1)` | a staircase up and down | 2 | side by side, both on the bottom row | `Z/15` | `Z/8` |
| `(1, 1, 1, 2, 3, 2)`, `(1, 1, 2, 2, 3, 1)` | the 10-cell adjacency-cospectral pair | 2 | side by side, both on the bottom row | `Z/15` | `Z/8` |
| `(2, 2, 2, 2)`, `(2, 2, 2, 2, 2)` | 2-wide ladders lying down | 3, 4 | a row of blocks on the bottom row | `Z/56`, `Z/209` | `Z/21`, `Z/55` |
| `(2, 2, 1, 2, 2)` | two separated squares | 2 | two apart | `Z/4 × Z/4` | `Z/3 × Z/3` |
| `(3, 3, 3)` | the `3 × 3` square | 4 | a `2 × 2` square of blocks | `Z/8 × Z/24` | `Z/95` |
| `(2, 3, 3, 2)` | a hill | 4 | a T of blocks | `Z/4 × Z/52` | `Z/75` |

Every group in the table was computed from Equation (1) in both models.[^15]

**2-wide ladders.** A 2-wide ladder has a single path of blocks, so its block matrix is tridiagonal with `−1` beside the diagonal, and its group is cyclic in both models ([[sandpile-census](pages/sandpile-census.md)], section 4). In the sink model the diagonal is all 4s whichever way the ladder stands, and the orders are `4, 15, 56, 209, …`, `A001353`, which satisfies `a(n) = 4a(n−1) − a(n−2)`. In the tide model the orientation matters:[^16]

| 2-wide ladder | `K_sink` orders | `K_tide` orders | OEIS, tide |
|---|---|---|---|
| lying down, `(2, …, 2)` of width `w` | `4, 15, 56, 209, 780` (`A001353(w)`) | `3, 8, 21, 55, 144` (every diagonal entry 3) | `A001906(w) = F_{2w}` |
| standing up, `(h, h)` | `4, 15, 56, 209, 780` (`A001353(h)`) | `3, 11, 41, 153, 571` (one 3, then 4s) | `A001835(h)` |

In the sink model, separated clusters of blocks contribute independent factors (two separated squares give `Z/4 × Z/4`), a row of `r` blocks contributes the cyclic group of the ladder order, and denser arrangements can split into several factors: the `2 × 2` square of blocks in `(3, 3, 3)` and the T in `(2, 3, 3, 2)` each give two. Not every dense cluster splits: `(2, 3, 3, 3)`, a `2 × 2` square of blocks plus one more, has `K_sink = Z/712` ([[sandpile-census](pages/sandpile-census.md)]). In the tide model `(3, 3, 3)` and `(2, 3, 3, 2)` are cyclic, `Z/95` and `Z/75`.

**The square castles, from the dual side.** The sink block matrix of the `(L+1) × (L+1)` castle is the Laplacian of an `L × L` grid with open boundaries on all four sides, the matrix Dhar, Ruelle, Sen and Verma study. Their groups for `L = 2` to 5, `Z/24 × Z/8`, `Z/224 × Z/112 × Z/4`, `Z/6600 × Z/1320 × Z/8 × Z/8` and `Z/102960 × Z/102960 × Z/48 × Z/16 × Z/4`, are the sink groups of the square castles `(3, 3, 3)` to `(6, 6, 6, 6, 6, 6)`. They show, with a sketched proof, that the group of the `L × L` grid has exactly `L` cyclic factors, so the same holds for the `(L+1) × (L+1)` castle. Their `L × 2` strip is the castle `(3, …, 3)` of height 3 and width `L + 1`, whose sink group they compute exactly ([[sandpile-census](pages/sandpile-census.md)]).[^17]

**The cospectral pairs.** The 10-cell adjacency-cospectral pair of [[hear-the-shape-seminar](pages/hear-the-shape-seminar.md)] has the same groups, `Z/15` and `Z/8`, because both castles have two blocks side by side on the bottom row. The 11-cell Laplacian-cospectral pair are tree castles, with trivial groups. [[sandpile-census](pages/sandpile-census.md)] checks every castle to 16 cells: the sink group separates no cospectral group, because the castles in each cospectral group share their graph of blocks, while the tide group separates 23 of the 105 adjacency-cospectral groups, because it also depends on which blocks sit on the bottom row.

## Snippet

```python
import sympy as sp
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ

def castle_graph(c):                       # cells (column, row) and edges between side-sharing cells
    cells = [(i, j) for i, h in enumerate(c) for j in range(h)]
    idx = {v: k for k, v in enumerate(cells)}
    edges = [(idx[(i, j)], idx[nb]) for (i, j) in cells for nb in ((i+1, j), (i, j+1)) if nb in idx]
    return cells, idx, edges

def boundary(c):                           # |cells| x |edges|: +1 at an edge's tail, -1 at its head
    cells, _, edges = castle_graph(c)
    D = sp.zeros(len(cells), len(edges))
    for e, (u, v) in enumerate(edges):
        D[u, e], D[v, e] = 1, -1
    return D

def laplacian(c):
    D = boundary(c)
    return D * D.T

def sink_cells(c, model):                  # 'sink': the bottom-left cell; 'tide': the whole bottom row
    return {(0, 0)} if model == 'sink' else {(i, 0) for i in range(len(c))}

def reduced_laplacian(c, model):           # delete the sink's rows and columns; degrees stay full
    cells, idx, _ = castle_graph(c)
    keep = [idx[v] for v in cells if v not in sink_cells(c, model)]
    return laplacian(c).extract(keep, keep)

def blocks(c):                             # 2x2 blocks, by lower-left cell
    return [(i, j) for i in range(len(c) - 1) for j in range(min(c[i], c[i+1]) - 1)]

def cycle_matrix(c):                       # |edges| x |blocks|: each block's four edges, counterclockwise
    cells, idx, edges = castle_graph(c)
    eid = {e: k for k, e in enumerate(edges)}
    C = sp.zeros(len(edges), len(blocks(c)))
    for b, (i, j) in enumerate(blocks(c)):
        loop = [(i, j), (i+1, j), (i+1, j+1), (i, j+1), (i, j)]
        for p, q in zip(loop, loop[1:]):
            u, v = idx[p], idx[q]
            if (u, v) in eid: C[eid[(u, v)], b] = 1
            else:             C[eid[(v, u)], b] = -1
    return C

def block_matrix(c, model):                # -1 for blocks sharing an edge; 4 on the diagonal, 3 for ground blocks under the tide
    B = blocks(c)
    return sp.Matrix(len(B), len(B), lambda a, b: (3 if model == 'tide' and B[a][1] == 0 else 4) if a == b else
                     -1 if abs(B[a][0] - B[b][0]) + abs(B[a][1] - B[b][1]) == 1 else 0)

def invariant_factors(M):                  # the group Z^n / M Z^n, as its nontrivial cyclic factors
    if M.rows == 0:
        return []
    S = smith_normal_form(M, domain=ZZ)
    return [abs(S[i, i]) for i in range(M.rows) if abs(S[i, i]) != 1]

def sandpile_group(c, model='sink'):       # from the cells
    return invariant_factors(reduced_laplacian(c, model))

def sandpile_group_from_blocks(c, model='sink'):   # from the 2x2 blocks
    return invariant_factors(block_matrix(c, model))

def board(c, model):                       # sand-holding cells, their non-sink neighbors, full degrees
    cells, idx, edges = castle_graph(c)
    sink = {idx[v] for v in sink_cells(c, model)}
    nbrs = {v: [] for v in range(len(cells))}
    for u, v in edges:
        nbrs[u].append(v); nbrs[v].append(u)
    live = [v for v in range(len(cells)) if v not in sink]
    return live, {v: [u for u in nbrs[v] if u not in sink] for v in live}, {v: len(nbrs[v]) for v in live}

def stabilize(b, g):                       # topple every cell holding >= its degree, until none does
    live, nb, deg = b
    g = dict(g)
    while any(g[v] >= deg[v] for v in live):
        for v in live:
            if g[v] >= deg[v]:
                g[v] -= deg[v]
                for u in nb[v]:
                    g[u] += 1
    return g

def recurrent(c, model='sink'):            # configurations reachable again and again by adding sand
    b = board(c, model); live, nb, deg = b
    top = tuple(deg[v] - 1 for v in live)
    seen, todo = {top}, [top]
    while todo:
        x = todo.pop()
        for k, v in enumerate(live):
            y = stabilize(b, {u: x[i] + (u == v) for i, u in enumerate(live)})
            y = tuple(y[u] for u in live)
            if y not in seen:
                seen.add(y); todo.append(y)
    return seen
```

```
>>> sorted(recurrent((2, 2))), sorted(recurrent((2, 2), 'tide'))
([(0, 1, 1), (1, 0, 1), (1, 1, 0), (1, 1, 1)], [(0, 1), (1, 0), (1, 1)])
>>> sandpile_group((2, 2)), sandpile_group((2, 2), 'tide'), reduced_laplacian((2, 2), 'sink').det()
([4], [3], 4)
>>> b = board((2, 2, 2), 'sink'); pile = {v: b[2][v] - 1 for v in b[0]}; pile[5] += 1
>>> stabilize(b, pile)                                  # the avalanche of the worked example; cells BL, TL, BM, TM, BR, TR
{1: 1, 2: 1, 3: 2, 4: 0, 5: 1}
>>> c = (3, 3, 3)
>>> laplacian(c) == boundary(c) * boundary(c).T, (boundary(c) * cycle_matrix(c)).is_zero_matrix
(True, True)
>>> cycle_matrix(c).T * cycle_matrix(c) == block_matrix(c, 'sink')
True
>>> sandpile_group(c), sandpile_group_from_blocks(c), len(recurrent(c))
([8, 24], [8, 24], 192)
>>> sandpile_group(c, 'tide'), sandpile_group_from_blocks(c, 'tide'), block_matrix(c, 'tide')
([95], [95], Matrix([
[ 3, -1, -1,  0],
[-1,  4,  0, -1],
[-1,  0,  3, -1],
[ 0, -1, -1,  4]]))
>>> [(c, sandpile_group_from_blocks(c), sandpile_group_from_blocks(c, 'tide')) for c in [(1, 2, 1, 3, 1), (2, 2, 2), (3, 3), (2, 2, 1, 2, 2), (2, 3, 3, 2)]]
[((1, 2, 1, 3, 1), [], []), ((2, 2, 2), [15], [8]), ((3, 3), [15], [11]), ((2, 2, 1, 2, 2), [4, 4], [3, 3]), ((2, 3, 3, 2), [4, 52], [75])]
>>> [sandpile_group_from_blocks((2,) * w, 'tide')[0] for w in range(2, 7)], [sandpile_group_from_blocks((h, h), 'tide')[0] for h in range(2, 7)]
([3, 8, 21, 55, 144], [3, 11, 41, 153, 571])
>>> len(recurrent((2, 2, 2), 'tide'))
8
```

In the recurrent tuples the positions are the non-sink cells in the order `castle_graph` lists them. For the sink model of `(2, 2)` that is top-left `(0,1)`, bottom-right `(1,0)` and top-right `(1,1)`; for the tide model it is top-left `(0,1)` and top-right `(1,1)`.

## Related Concepts

- [[castle-graph](pages/castle-graph.md)] - the castle graph, its cycle rank (the number of `2 × 2` blocks), and the tree castles.
- [[sandpile-census](pages/sandpile-census.md)] - both groups for every castle to 16 cells, the integer basis of the cycle lattice, and what each group separates.
- [[sandpile-identity](pages/sandpile-identity.md)] - the identity element in both models.
- [[sandcastle-clock](pages/sandcastle-clock.md)] - the clock in both models: the order of one grain at the apex in the group.
- [[castle-avalanches](pages/castle-avalanches.md)] - grains dropped at random in both models: mean avalanche sizes and their distributions.
- [[sandcastle-seminar](pages/sandcastle-seminar.md)] - a seminar following the 16-cell castle `(3, 2, 1, 2, 2, 1, 2, 3)`, silver by spectrum, through both models.
- [[hear-the-shape-seminar](pages/hear-the-shape-seminar.md)] and [[isospectral-castles](pages/isospectral-castles.md)] - the Laplacian of the castle graph and the cospectral pairs.
- [[spectral-analysis](pages/spectral-analysis.md)] - section 4, the Laplacian, whose cofactors count spanning trees.
- [[castle-graph-spectral-radius](pages/castle-graph-spectral-radius.md)] - the castles golden and silver by spectrum, such as `(1, 1, 1, 1)` and `(2, 2, 2)`.
- [[castle-ring-invariant-factors](pages/castle-ring-invariant-factors.md)] - the other finite abelian groups on the wiki read off a Smith normal form.
- [[castle-eigenvalues-by-example](pages/castle-eigenvalues-by-example.md)] - the 10-cell cospectral pair worked by hand.
- [[ramanujan-castles](pages/ramanujan-castles.md)] - the 2-wide ladder `(14, 14)`, the smallest rectangle that is not Ramanujan, and its sandpile groups.
- [[viennot-heap-tower](pages/viennot-heap-tower.md)] - the series `1/(1 − 3x + x²)`, `A001906`, whose coefficients are the tide orders of the 2-wide ladders lying down.
- [[castle-notation](pages/castle-notation.md)] - the sandpile symbols `L̃`, `n_live`, `K`, `a_v`.

## Appearances in Sources

- [[dhar-1990-self-organized-critical-sandpile](pages/dhar-1990-self-organized-critical-sandpile.md)] - the abelian property, the uniform steady state on the recurrent configurations, the presentation of the group by the toppling matrix with `det Δ` elements, the entropy `ln det Δ`, and the forbidden-subconfiguration test.
- [[dhar-ruelle-sen-verma-1995-algebraic-aspects](pages/dhar-ruelle-sen-verma-1995-algebraic-aspects.md)] - the order `det Δ` and the structure from the Smith normal form, and the groups of the open-boundary grids that are the duals of the square and height-3 castles.
- [[rossin-2000-group-of-a-sandpile](pages/rossin-2000-group-of-a-sandpile.md)] - the group of recurrent configurations, its independence of the sink, the reference to Cori and Rossin's paper on the sandpile groups of dual graphs, and the group of the `2 × 2` grid quoted from Dhar, Ruelle, Sen and Verma.
- [[chau-cheng-1991-deterministic-soc-sandpile](pages/chau-cheng-1991-deterministic-soc-sandpile.md)] - completely deterministic steady states and their classification.
- [[bak-tang-wiesenfeld-1988-self-organized-criticality](pages/bak-tang-wiesenfeld-1988-self-organized-criticality.md)] - the toppling rule and random dropping on the square lattice, which this page applies to the castle graph.
- [[project-euler-502-castle-factoring](pages/project-euler-502-castle-factoring.md)] - the castle definition (column heights `≥ 1`) behind the castle graph.

## Footnotes

[^1]: [[dhar-1990-self-organized-critical-sandpile](pages/dhar-1990-self-organized-critical-sandpile.md)] p.1614 L104-137 [synthesis] - two critical sites give the same configuration in either toppling order, and toppling commutes with adding a particle, so `a_i a_j C = a_j a_i C` for all `i, j` (eq. 5).
[^2]: [[rossin-2000-group-of-a-sandpile](pages/rossin-2000-group-of-a-sandpile.md)] §1 L9, §2 L37 and reference [3] L102 - "Dhar [9] showed that the set of recurrent configurations of this automaton has the structure of a finite abelian group"; "The set of recurrent configurations with the operation ⊕ is an abelian group G [8], ... and the group structure does not depend on the sink choice in the graph G"; Biggs, "Chip-firing and the critical group of a graph". The sink independence was also checked for every choice of sink cell on every castle with at most 12 cells (Python 3.11, 2026-10-16).
[^3]: [[dhar-1990-self-organized-critical-sandpile](pages/dhar-1990-self-organized-critical-sandpile.md)] p.1614 L85-101 [synthesis] - "all nonrecurrent configurations are transients, and have zero probability of occurrence in the SOC state"; "only recurrent configurations have a nonzero probability of occurrence, and this nonzero value is the same for all recurrent configurations."
[^4]: Verified by execution (Python 3.11, SymPy, 2026-10-16): `recurrent((2, 2))` and `recurrent((2, 2), 'tide')` are the configurations listed; `det L̃` is 4 (sink) and 3 (tide); adding `(1, 1, 0)` (sink) and `(1, 1)` (tide) to every recurrent configuration and stabilizing returns it.
[^5]: Verified by execution (Python 3.11, 2026-10-16): the sink trace, toppling the first unstable cell in the order `BL, TL, BM, TM, BR, TR`, has 11 topplings, absorbs 3 grains and ends at `TL = 1, TM = 2, TR = 1, BM = 1, BR = 0`, the configuration the Snippet's `stabilize` reaches by toppling every unstable cell in each sweep; the tide trace has 3 topplings, absorbs 3 grains and ends at `TL = 0, TM = 1, TR = 1`; the recurrent sets have 15 and 8 elements.
[^6]: [[dhar-ruelle-sen-verma-1995-algebraic-aspects](pages/dhar-ruelle-sen-verma-1995-algebraic-aspects.md)] p.5 eq. (2.4) and pp.7-10 eqs. (3.9)-(3.17) [synthesis] - `|G| = |R| = Det Δ`, and the structure `G = Z_{d_1} × … × Z_{d_g}` from the decomposition `Δ = ADB` of the toppling matrix with `A`, `B` integer matrices of determinant `±1` and `D` diagonal.
[^7]: [[dhar-1990-self-organized-critical-sandpile](pages/dhar-1990-self-organized-critical-sandpile.md)] pp.1614-1615 L102-124, L172, L199-220 [synthesis] - adding `Δ_ii` particles at `i` gives the relations `∏_j a_j^{Δ_ij} = 1` (eqs. 8-9); `N_R = Det Δ` (eq. 13); equivalent configurations differ by `Σ_j r_j Δ_ij` (eq. 17). For a castle, `Δ = L̃` of the model.
[^8]: [[dhar-1990-self-organized-critical-sandpile](pages/dhar-1990-self-organized-critical-sandpile.md)] p.1615 L173-177 - "Since all these configurations occur with equal probability in the SOC state, the entropy of the SOC state S is given by S = ln Det Δ" (eq. 14).
[^9]: [[dhar-1990-self-organized-critical-sandpile](pages/dhar-1990-self-organized-critical-sandpile.md)] p.1615 L186-197 [synthesis] - the entropy per site of the undirected nearest-neighbor model on the square lattice with free boundary conditions, eq. (16). Verified by execution (Python 3.11, mpmath and NumPy, 2026-10-16): the integral, after the inner integral `(1/2π)∫ ln(a − 2cos φ) dφ = ln((a + √(a² − 4))/2)`, is `1.16624361612327512`, equal to `4G/π` to 20 digits; `slogdet` of `L̃` for the `ℓ × ℓ` castle with corner sink, divided by `ℓ²`, and for the `ℓ × (ℓ + 1)` castle in the tide model, divided by the `ℓ²` cells above the bottom row, gives the table.
[^10]: [[dhar-1990-self-organized-critical-sandpile](pages/dhar-1990-self-organized-critical-sandpile.md)] p.1615 L172-189, L204-214, L224-236 [synthesis] - the recursive test on the set `T` of sites; the forbidden subconfiguration, eq. (18), with heights counted from 1; "all recurrent configurations are allowed. The converse statement appears quite plausible, though a strict proof is lacking."
[^11]: [[chau-cheng-1991-deterministic-soc-sandpile](pages/chau-cheng-1991-deterministic-soc-sandpile.md)] p.104-105 L99-110, L102, L116-124, L173-174 [synthesis] - completely deterministic means `a_i|_R = a_j|_R` for all `i, j` (eq. 5), the evolution depending "only on the total number of particles added"; "R is isomorphic to the group Z_{n+1}"; the fundamental toppling rules that are deterministic (eq. 13).
[^12]: Verified by execution (Python 3.11, SymPy, 2026-10-16): `laplacian(c) == boundary(c)·boundary(c)ᵀ` and `boundary(c)·cycle_matrix(c) = 0` for `c = (3, 3, 3)`, as in the Snippet.
[^13]: Verified by execution (Python 3.11, 2026-10-16): for all 33,150 castles with at most 16 cells, mirror images removed, the invariant factors of `L̃` (Equation (1)) equal those of the block matrices of Equations (4) and (5), in both models; `CᵀC` equals the sink block matrix for `(3, 3, 3)`, as in the Snippet. The integer Smith normal form routine used agrees with SymPy's on 300 random integer matrices.
[^14]: [[rossin-2000-group-of-a-sandpile](pages/rossin-2000-group-of-a-sandpile.md)] §4 L92 and reference [5] L106 - "Our second example is the 2 × 2 grid consisting of 4 cells, each connected twice to the sink. The sandpile group of this grid, computed for instance in [9], is the product of two cyclic group of orders 24 and 8"; reference [5], "Cori (Robert) and Rossin (Dominique). -- On the sandpile group of dual graphs. European Journal of Combinatorics, vol. 21, n°4, 2000, pp. 447--459." The same `2 × 2` grid is the example of determinant 192 of [[dhar-ruelle-sen-verma-1995-algebraic-aspects](pages/dhar-ruelle-sen-verma-1995-algebraic-aspects.md)], eq. (3.13), p.8.
[^15]: Verified by execution (Python 3.11, SymPy, 2026-10-16): every group in the table from the cell-side `L̃` in both models; the spectral radii `φ` of `(1, 1, 1, 1)` and `1 + √2` of `(2, 2, 2)` and of `(3, 2, 1, 2, 2, 1, 2, 3)`.
[^16]: Verified by execution (Python 3.11, 2026-10-16): the ladder orders, as in the Snippet; `A001353`, `A001906` and `A001835` checked on oeis.org at the offsets given.
[^17]: [[dhar-ruelle-sen-verma-1995-algebraic-aspects](pages/dhar-ruelle-sen-verma-1995-algebraic-aspects.md)] §3 p.6 and §4 p.12, eqs. (4.6a-d) and (4.7) - `Δ_ij = 4` on the diagonal "implies open boundary" conditions; the four groups as quoted; "This suggests, and it is in fact not difficult to prove, that for an L × L square g = L", followed by "The idea of the proof". Verified by execution (Python 3.11, 2026-10-16): the sink groups of `(3, 3, 3)`, `(4, 4, 4, 4)`, `(5, 5, 5, 5, 5)` and `(6, 6, 6, 6, 6, 6)` from the block matrices are those four groups.
