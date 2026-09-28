---
title: Sandpile groups of castles - sand, cycles, and 2×2 blocks, in the sink and tide models
category: Concepts
summary: An introduction to the sandpile group (also called the critical group or Jacobian) of a castle, in two models that differ only in where the sand leaves. Grains sit on cells; a cell holding at least as many grains as it has neighbours topples, sending one grain to each; grains that reach the sink vanish. In the sink model the sink is one cell (the bottom-left cell on these pages), and the group does not depend on which cell it is; in the tide model the sink is the whole bottom row, the ground. The configurations that keep coming back as sand is added form a finite group whose size is the number of spanning trees, Z^n modulo the reduced Laplacian, and the Laplacian factors through the boundary matrix as L = ∂∂ᵀ. Because castles are planar the group can be read off a small matrix with one row per 2×2 block and −1 for each pair of blocks sharing an edge. The diagonal is where the models differ: 4 for every block in the sink model, but 3 for a block sitting on the ground and 4 above it in the tide model, because merging the bottom row turns each ground block's 4-cycle into a triangle (argued from planar duality, checked on all 33,150 castles to 16 cells). So the sink group depends only on how the blocks touch, while the tide group also depends on how high they sit - (2,2,2) and (3,3) have the same graph and the same sink group Z/15, but tide groups Z/8 and Z/11 - and the tide model splits a castle into its runs of raised columns. Both models give the trivial group exactly on tree castles. The horizontal ladders give A001353 (sink) and the even Fibonacci numbers A001906 (tide); the vertical ladders give A001353 (sink) and A001835 (tide). A runnable block reproduces every example in both models.
tags: [concept, castle, sandpile, abelian-sandpile, critical-group, chip-firing, laplacian, boundary-matrix, cycle-space, spanning-trees, smith-normal-form, tree-castle, planar-dual, sink-model, tide-model, pedagogy]
sources: [project-euler-502-castle-factoring, rossin-2000-group-of-a-sandpile, dhar-ruelle-sen-verma-1995-algebraic-aspects, dhar-1990-self-organized-critical-sandpile, chau-cheng-1991-deterministic-soc-sandpile, bak-tang-wiesenfeld-1988-self-organized-criticality]
created: 2026-09-26
updated: 2026-09-28
---

# Sandpile groups of castles - sand, cycles, and 2×2 blocks, in the sink and tide models

This page introduces the **sandpile group** of a castle for readers who have not met it before. It starts with a game you can play on paper, then connects the game to matrices the wiki already uses: the Laplacian of [[hear-the-shape-seminar](pages/hear-the-shape-seminar.md)], the boundary matrix, and the cycles of [[castle-graph](pages/castle-graph.md)]. The game needs a place where sand leaves the castle, and there are two natural choices, the **sink model** and the **tide model**. Every result on this page is stated for both, because the two models see different cycles and so different groups. Part 3 shows that the group is determined by the castle's 2×2 blocks, and under the tide also by how high each block sits.

## Part 1 - the game, and the two models

Take a castle and its graph: one vertex per filled cell, one edge per pair of cells that share a side ([[castle-graph](pages/castle-graph.md)]). Some cells form the **sink**, where sand leaves.

- **Sand.** Put a whole number of grains on every cell outside the sink. That is a *configuration*.
- **Toppling.** A cell that holds at least as many grains as it has neighbours is unstable. It **topples**: it sends one grain to each neighbour. Grains that reach the sink disappear.
- **Stabilizing.** Keep toppling until no cell is unstable. Because the sink removes sand, this always stops, and the final configuration does not depend on the order of the topplings. That is why the model is called **abelian**.[^1] Dhar proved it in 1990 for any toppling matrix of this kind: two unstable cells can be toppled in either order, and toppling commutes with adding a grain, so the operators "add a grain at `v`, then stabilize" commute.[^2]

**Two models.** They differ only in which cells form the sink.

| | sink model | tide model |
|---|---|---|
| the sink | one cell; on these pages the bottom-left cell | the whole bottom row, the ground |
| where sand leaves | only through that one cell's neighbours | from every cell standing on the ground |
| the graph behind it | the castle graph itself | the castle graph with the bottom row merged into one vertex |
| does a choice matter? | the group does not depend on which cell is the sink; clocks and identities do | no choice: the ground is canonical |

A cell keeps its full number of neighbours in both models, so a cell standing on the ground still needs as many grains to topple as before, and in the tide model one of those grains falls into the ground.

**Add sand forever.** Drop grains on cells one at a time, stabilizing after each drop. Some stable configurations appear only near the start and never come back. The others, the **recurrent** configurations, keep coming back no matter how long you play. In the long run every recurrent configuration is equally likely, and the others (the transients) never occur.[^3]

**The recurrent configurations form a group.** Add two recurrent configurations cell by cell and stabilize: the result is recurrent again. This operation has an identity element and inverses, so the recurrent configurations form a finite abelian group, the **sandpile group** `K`. It is also called the critical group or the Jacobian of the graph. Its size is the **number of spanning trees** of the graph behind the model.[^1] Write `K_sink` and `K_tide` for the two groups of the same castle.

### Worked example: the 4-cycle `(2, 2)` in both models

**Sink model.** `(2, 2)` is a `2 × 2` square of four cells, each with two neighbours. Make the bottom-left cell the sink. The other three cells are stable with 0 or 1 grain each, so there are `2³ = 8` stable configurations. Exactly **4** of them are recurrent: the ones with **at most one empty cell**.

```
recurrent (grains on top-left, bottom-right, top-right):   (0,1,1)  (1,0,1)  (1,1,0)  (1,1,1)
transient:                                                 (0,0,0)  (1,0,0)  (0,1,0)  (0,0,1)
```

Four recurrent configurations means `K_sink = Z/4`, and the square has 4 spanning trees (delete any one of its 4 edges). The identity element is `(1, 1, 0)`: one grain on each cell next to the sink and none on the far corner. Adding it to any recurrent configuration and stabilizing gives that configuration back.[^4]

**Tide model.** Now the whole bottom row is the ground. Only the two top cells hold sand, and each has two neighbours: the other top cell, and the ground below it. Each holds 0 or 1 grain, so there are 4 stable configurations, and exactly **3** are recurrent: every one except the empty pile.

```
recurrent (grains on top-left, top-right):   (0,1)  (1,0)  (1,1)
transient:                                   (0,0)
```

So `K_tide = Z/3`. The graph behind the tide model is a triangle (the two top cells and the ground), which has 3 spanning trees. The identity is the full pile `(1, 1)`.[^4]

### Worked example: one avalanche on the silver rectangle `(2, 2, 2)`

The sand in this game does not behave like physical sand. There is no gravity and there are no columns: every cell is a bowl, and "neighbour" means a cell that shares a side in any direction. Three rules settle every question about where a grain goes:

- **A bowl's capacity is its number of neighbours.** It tips over when it holds that many grains.
- **A neighbour always accepts a grain.** If that makes it overflow, it tips over in turn. That chain reaction is an **avalanche**.
- **Grains leave the castle only through the sink.** Any grain sent to the sink is removed, and the sink never tips. Without a sink the total amount of sand would never change, and an overfull pile would topple forever.

Label the six cells of the `3 × 2` rectangle:

```
top     TL  TM  TR            corners TL, TR, BL, BR have 2 neighbours;  TM, BM have 3
bottom  BL  BM  BR
```

**Sink model, sink `BL`.** Start from the fullest stable pile, each bowl one grain short of tipping, and drop one grain on `TR`:

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
topple BR    top [1 2 1]   bottom [S 1 0]   settled
```

One grain triggers 11 topplings. Sand moves right, left, up and down, and 3 grains leave through the sink: `7 + 1 = 8` grains before the avalanche, `5` after. Only `TL` and `BM` ever feed the sink, because they are its neighbours. Toppling the unstable cells in a different order ends in the same settled pile, which is the abelian property.[^5] Keep dropping grains and the pile eventually cycles through exactly 15 recurrent configurations, one for each spanning tree of the `3 × 2` grid. That is the group `K_sink = Z/15` of the silver rectangle in the gallery below.

**Tide model.** The bottom row is now the ground, so only the top row holds sand, with capacities 2, 3, 2. The same drop on `TR` of the fullest pile:

```
start        top [1 2 1]   bottom [~ ~ ~]
drop on TR   top [1 2 2]
topple TR    top [1 3 0]   <- one grain into the ground
topple TM    top [2 0 1]   <- another
topple TL    top [0 1 1]   <- a third          settled
```

Three topplings, and every one of them loses a grain, because every top cell stands on the ground. The pile cycles through 8 recurrent configurations: `K_tide = Z/8`.[^5]

## Part 2 - the matrices behind the game

**Toppling is subtracting a column of the Laplacian.** When cell `v` topples it loses `deg(v)` grains and each neighbour gains one. That is subtracting column `v` of the Laplacian `L = D − A` ([[hear-the-shape-seminar](pages/hear-the-shape-seminar.md)], Stop 0) from the configuration. So two configurations that differ by topplings are the same element of

```
K  =  Z^m / L̃ Z^m          (L̃ = L with the sink's rows and columns deleted)
```

In the sink model `L̃` deletes one row and column. In the tide model it deletes the whole bottom row, and each remaining cell keeps its full degree on the diagonal, which is the reduced Laplacian of the castle graph with the bottom row merged into one vertex. Either way this is a finite abelian group of order `det L̃`, the number of spanning trees of the graph behind the model by Kirchhoff's matrix-tree theorem. Its structure, a product of cyclic groups `Z/d_1 × Z/d_2 × …`, is read off the **Smith normal form** of `L̃`, the same tool [[castle-ring-invariant-factors](pages/castle-ring-invariant-factors.md)] uses for unit groups.[^1] [^6]

This is Dhar's presentation, in either model. Adding `deg(v)` grains at `v` forces one toppling, so the grain operators satisfy `∏_u a_u^{L̃_vu} = 1`, and two configurations are equivalent exactly when they differ by an integer combination of the rows of `L̃`. He counted the recurrent configurations as `det L̃`.[^7]

**Entropy.** Since every recurrent configuration is equally likely, the steady state's entropy is `ln det L̃ = ln |K|` (Dhar writes `S`; the wiki keeps `S(w, h)` for the parity term).[^8] Tree castles have entropy 0 in both models. For large rectangles the entropy per cell tends to Dhar's square-lattice value `(2π)⁻² ∫∫ ln(4 − 2cos θ − 2cos φ) dθ dφ = 1.16624…` (numerically 4 × (Catalan's constant)/π). `ln det L̃ / cells` is `0.984, 1.076, 1.121, 1.136` for `10 × 10` to `60 × 60` in the sink model (corner sink cell), and `1.050, 1.108, 1.137, 1.147` for the same numbers of cells above the ground in the tide model.[^9]

**What Dhar's paper does and does not give.** It contains a test for recurrence by *forbidden subconfigurations*: sets of cells in which every cell holds fewer grains (counting from 0, as on this page) than it has neighbours inside the set. Start from all the cells and repeatedly delete the ones that break this condition; either a forbidden set is left, or the set empties and the configuration passes. That is the burning test. Dhar proves only that recurrent configurations pass it; the converse he leaves unproved, and the bijection between recurrent configurations and spanning trees is later work, not in his paper.[^10]

**Deterministic sandcastles.** Chau and Cheng call a sandpile *completely deterministic* when every grain acts the same on the recurrent configurations, so only the number of grains added matters, not where they land; the recurrent set is then cyclic, and they classify the toppling matrices that do this.[^11] For castles the answer is short: **a castle sandpile is deterministic exactly when its group is trivial**, in both models. If every grain is the same element `g` of `K`, toppling a cell `v` gives `s(v)·g = 0`, where `s(v)` is the number of sink edges at `v`. Every cell next to the sink, whether the sink is one cell or the ground, has exactly one sink edge, so `g = 0` (own argument). Among castles with at most 12 cells, none with a nontrivial group is deterministic in either model.[^12] So the tree castles, whose groups are trivial in both models, are the deterministic ones. A nontrivial deterministic sandpile needs the sink-edge counts `s(v)` of the cells next to the sink to share a factor greater than 1, and every castle has a cell with `s(v) = 1`.

**The Laplacian factors through the boundary matrix.** Give every edge a direction. The **boundary matrix** `∂` has one row per cell and one column per edge, with `+1` at the edge's tail and `−1` at its head. It records which cells each edge joins. Then

```
L  =  ∂ ∂ᵀ
```

because `(∂∂ᵀ)[u, u]` counts the edges at `u`, and `(∂∂ᵀ)[u, v] = −1` when an edge joins `u` and `v`.[^13]

## Part 3 - cycles and the 2×2 blocks

**Cycles are the kernel of `∂`.** A combination of edges (each with an integer coefficient) whose boundary is zero goes around closed loops: every cell is entered as often as it is left. These combinations form the **cycle space**, the kernel of `∂`. Its dimension is the **cycle rank** `|E| − |V| + 1`.

**For a castle, the cycles are generated by the 2×2 blocks.** A castle graph is a piece of the square grid with no holes, so its only "faces" are the filled `2 × 2` blocks. Going once around a block's four edges is a cycle, and the blocks' cycles form a basis of all cycles. The cycle rank is the number of `2 × 2` blocks ([[castle-graph](pages/castle-graph.md)]). Put these basis cycles as the columns of the **cycle matrix** `C`, one column per block. Then `∂C = 0`.

**The block matrix, sink model.** The Gram matrix `CᵀC` compares the block cycles with each other. Each block's cycle has four edges, and two blocks that share an edge traverse it in opposite directions:

```
CᵀC[a, a]  =  4          CᵀC[a, b]  =  −1  if blocks a and b share an edge,   0 otherwise
```

For a planar graph like a castle, this small matrix, **one row per 2×2 block**, carries the whole sandpile group:

```
K_sink  =  Z^r / (CᵀC) Z^r          (r = number of 2×2 blocks)
```

It is the sandpile group of the planar dual graph, whose vertices are the blocks and the outer face. The `3 × 3` castle `(3, 3, 3)` shows it from both sides: its dual is a `2 × 2` grid of blocks with each corner block meeting the outer face along two edges, which Rossin's seminar works directly and finds `Z/24 × Z/8`, the group the cells give here. This was checked against the cell-side formula on all 1,023 castles with up to 10 cells, mirror images counted separately (558 up to mirror image).[^14] So **the 2×2 blocks determine the group**. A castle with no `2 × 2` block has no cycles, a single spanning tree, and a trivial group. The sink group depends only on how the blocks touch each other; the towers and spikes around them, and the choice of sink cell, do not change it.

**The tide changes the cycles.** Merging the bottom row into one vertex collapses the bottom edge of every block that sits on the ground. Such a block's cycle, which went around four edges, now goes around three: two cells in row 1 and the ground. Blocks higher up keep their four edges. So the tide model's block matrix has the same `−1` pattern, with a different diagonal:

```
tide block matrix[a, a]  =  3  if block a sits on the ground (rows 0 and 1),   4  otherwise
K_tide  =  Z^r / (tide block matrix) Z^r
```

**Why 3.** Merging the bottom row contracts its horizontal edges. In a plane graph, contracting an edge is the same as deleting the matching edge of the dual graph. The dual edge of a bottom-row edge joins the block above it, if there is one, to the outer face. So a ground block loses one of its four dual edges, and nothing else in the dual changes. The sandpile group of a plane graph is that of its dual (Cori and Rossin), so the tide group is the dual's group with those edges gone, which is the matrix above. (The argument is assembled here from those two standard facts; the formula also agrees with the cell-side computation on all 33,150 castles with at most 16 cells.)[^15]

**The tide group depends on how high the blocks sit.** The sink block matrix depends only on the graph of blocks. The tide block matrix also records which blocks touch the ground, so two castles with the same graph can have different tide groups. The silver rectangle `(2, 2, 2)` and the tall pair `(3, 3)` are the same `3 × 2` grid, lying down and standing up. Both have `K_sink = Z/15`. Lying down, both blocks sit on the ground, `[[3, −1], [−1, 3]]`, and `K_tide = Z/8`; standing up, only the lower one does, `[[3, −1], [−1, 4]]`, and `K_tide = Z/11`.

**The tide splits a castle into runs.** Under the tide the bottom row is gone, and what stands on it falls apart into its **runs of raised columns**, the maximal runs of adjacent columns of height at least 2. Two runs separated by a height-1 column never exchange sand, so the tide group is the product of the runs' groups, and two castles with the same runs (in any order, any distance apart, each run either way round) have the same tide model.

**Trivial in both models exactly for tree castles.** A castle with no `2 × 2` block is a tree, and its raised columns are separate spikes each touching the ground once, so both graphs are trees and both groups are trivial. A castle with a block has a cycle in both graphs (a 4-cycle, or a triangle through the ground), hence at least 3 spanning trees and a nontrivial group in both.

## Part 4 - the castle gallery

| castle | kind of castle | 2×2 blocks | block arrangement | `K_sink` | `K_tide` |
|---|---|---|---|---|---|
| `(1,1,1,1)`, `(1,2,1)`, `(1,2,1,3,1)` | tree castles: golden path, spike, battlement | 0 | - | trivial | trivial |
| `(2, 2)` | the 4-cycle | 1 | one block, on the ground | `Z/4` | `Z/3` |
| `(2, 2, 2)` | silver rectangle `3 × 2` | 2 | two side by side, on the ground | `Z/15` | `Z/8` |
| `(3, 3)` | tall pair (same graph as `(2, 2, 2)`) | 2 | two stacked, one on the ground | `Z/15` | `Z/11` |
| `(1, 2, 3, 2, 1)` | staircase | 2 | two side by side, on the ground | `Z/15` | `Z/8` |
| `(1,1,1,2,3,2)`, `(1,1,2,2,3,1)` | the 10-cell isospectral pair | 2 | two side by side, on the ground | `Z/15` | `Z/8` |
| `(2, 2, 2, 2)`, `(2, 2, 2, 2, 2)` | 2-wide ladders lying down | 3, 4 | a row of blocks, on the ground | `Z/56`, `Z/209` | `Z/21`, `Z/55` |
| `(2, 2, 1, 2, 2)` | two separated squares | 2 | two apart | `Z/4 × Z/4` | `Z/3 × Z/3` |
| `(3, 3, 3)` | `3 × 3` square | 4 | a `2 × 2` square of blocks | `Z/8 × Z/24` | `Z/95` |
| `(2, 3, 3, 2)` | a hill | 4 | a T of blocks | `Z/4 × Z/52` | `Z/75` |

**The prototype: the ladder.** A 2-wide ladder has a single path of blocks, so its block matrix is tridiagonal with `−1` beside the diagonal, and its group is cyclic in both models. In the sink model the diagonal is all 4s whichever way the ladder stands, and the orders are `4, 15, 56, 209, …` (OEIS A001353, `a(n) = 4a(n−1) − a(n−2)`). Under the tide the orientation matters:

| 2-wide ladder | `K_sink` orders | `K_tide` orders | tide OEIS |
|---|---|---|---|
| lying down, `(2, …, 2)` of width `w` | `4, 15, 56, 209, 780` (A001353(w)) | `3, 8, 21, 55, 144` (every block on the ground: all 3s) | A001906(w) `= F(2w)`, the even Fibonacci numbers |
| standing up, `(h, h)` | `4, 15, 56, 209, 780` (A001353(h)) | `3, 11, 41, 153, 571` (one ground block, then 4s) | A001835(h) |

Picture any castle as its skeleton of `2 × 2` blocks. In the sink model, separated groups of blocks contribute independent factors (two isolated squares give `Z/4 × Z/4`), a row of `r` blocks contributes one cyclic group of that ladder order, and denser arrangements can split: the `2 × 2` square of blocks in `(3, 3, 3)` and the T in `(2, 3, 3, 2)` each give two cyclic factors. Not every dense cluster splits: `(2, 3, 3, 3)` has a `2 × 2` square of blocks plus one more, and a cyclic group `Z/712` ([[sandpile-census](pages/sandpile-census.md)]). Under the tide the same two dense castles are cyclic, `Z/95` and `Z/75`.

**The square castles, from the dual side.** The sink block matrix of the `(L+1) × (L+1)` castle is the discrete Laplacian of an `L × L` grid with open boundaries on all four sides, the matrix Dhar, Ruelle, Sen and Verma studied. Their groups for `L = 2` to 5, `Z/24 × Z/8`, `Z/224 × Z/112 × Z/4`, `Z/6600 × Z/1320 × Z/8 × Z/8` and `Z/102960 × Z/102960 × Z/48 × Z/16 × Z/4`, are exactly the sink groups of the square castles `(3,3,3)` to `(6,6,6,6,6,6)`, and their proof that the `L × L` grid's group has exactly `L` cyclic factors says the same of the `(L+1) × (L+1)` castle. Their `L × 2` strip is the height-3 castle `(3, …, 3)`, whose sink group they solve exactly ([[sandpile-census](pages/sandpile-census.md)]).[^16]

**What this means for the isospectral pairs.** The 10-cell adjacency-isospectral pair of [[hear-the-shape-seminar](pages/hear-the-shape-seminar.md)] has the same group in both models, `Z/15` and `Z/8`, because both castles have two side-by-side blocks on the ground. The 11-cell Laplacian-isospectral pair are trees, so both groups are trivial in both models. [[sandpile-census](pages/sandpile-census.md)] checks every castle to 16 cells: the sink group separates no cospectral pair, because the cospectral castles there all share their graph of blocks, while the tide group separates 23 of the 105 adjacency-cospectral groups (two castles of different graphs with different tide groups), because it also depends on which blocks sit on the ground.

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

def board(c, model):                       # sand-holding cells, their non-sink neighbours, full degrees
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
>>> stabilize(b, pile)                                  # the avalanche above: cells BL, TL, BM, TM, BR, TR
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

- [[castle-graph](pages/castle-graph.md)] - the graph, its cycle rank (the number of 2×2 blocks), and tree castles.
- [[hear-the-shape-seminar](pages/hear-the-shape-seminar.md)] / [[isospectral-castles](pages/isospectral-castles.md)] - the Laplacian and the cospectral pairs the sandpile groups are tested against.
- [[castle-ring-invariant-factors](pages/castle-ring-invariant-factors.md)] - the other place the wiki reads a finite abelian group off a Smith normal form.
- [[castle-graph-spectral-radius](pages/castle-graph-spectral-radius.md)] - the golden and silver castles of the gallery.
- [[spectral-analysis](pages/spectral-analysis.md)] - method 4 (the Laplacian) and method 5 (the Ihara zeta), which also sees the spanning-tree count.
- [[sandpile-census](pages/sandpile-census.md)] - the census in both models: every castle to 16 cells, and what each group separates.
- [[sandcastle-clock](pages/sandcastle-clock.md)] - the clock in both models: drop one grain per tick and count ticks until the identity returns.
- [[sandpile-identity](pages/sandpile-identity.md)] - the identity element in both models, and the avalanche profiles.
- [[castle-avalanches](pages/castle-avalanches.md)] - dropping sand at random in both models: exact mean avalanche sizes and tails.
- [[sandcastle-seminar](pages/sandcastle-seminar.md)] - the Sandcastles seminar, following the 16-cell silver castle `(3,2,1,2,2,1,2,3)` through both models.
- [[castle-eigenvalues-by-example](pages/castle-eigenvalues-by-example.md)] - the 10-cell isospectral pair worked by hand; both castles have `K_sink = Z/15`.
- [[ramanujan-castles](pages/ramanujan-castles.md)] - the 2-wide ladder again: the 14-rung ladder `(14, 14)` is the smallest non-Ramanujan rectangle.
- [[viennot-heap-tower](pages/viennot-heap-tower.md)] - the tide ladder orders `3, 8, 21, 55, …` (A001906) are the Cartier-Foata reciprocal `1/(1 − 3x + x²)` of the interval-piece heap there.

## Appearances in Sources

- [[bak-tang-wiesenfeld-1988-self-organized-criticality](pages/bak-tang-wiesenfeld-1988-self-organized-criticality.md)] - the toppling rule and random dropping on the square lattice that the castle game adapts to the castle graph.
- [[chau-cheng-1991-deterministic-soc-sandpile](pages/chau-cheng-1991-deterministic-soc-sandpile.md)] - completely deterministic steady states and their classification; for castles, deterministic iff trivial, in both models.
- [[dhar-1990-self-organized-critical-sandpile](pages/dhar-1990-self-organized-critical-sandpile.md)] - the abelian property, the uniform steady state on recurrent configurations, the presentation `Z^N / Z^N Δ` with `det Δ` elements, the entropy `ln det Δ`, and the forbidden-subconfiguration test.
- [[dhar-ruelle-sen-verma-1995-algebraic-aspects](pages/dhar-ruelle-sen-verma-1995-algebraic-aspects.md)] - the Smith-normal-form structure and `|G| = det Δ`, and the groups and rank of the open-boundary grids that are the duals of the square and height-3 castles.
- [[rossin-2000-group-of-a-sandpile](pages/rossin-2000-group-of-a-sandpile.md)] - sink independence, the identity recipe, the dual-graph theorem via its reference to Cori and Rossin, and the `2 × 2` grid example that is the dual of `(3, 3, 3)`.
- [[project-euler-502-castle-factoring](pages/project-euler-502-castle-factoring.md)] - the castle definition (column heights `≥ 1`) behind the castle graph.

## Footnotes

[^1]: https://en.wikipedia.org/wiki/Abelian_sandpile_model - toppling at the degree, a sink vertex, order-independence of stabilization (the abelian property), recurrent configurations forming the sandpile group under addition followed by stabilization, its presentation as `Z^{n−1}` modulo the reduced Laplacian, its order equal to the number of spanning trees (Kirchhoff's matrix-tree theorem, and a bijection between recurrent configurations and spanning trees), and its independence of the choice of sink vertex. Sink independence and the group of recurrent configurations are also in [[rossin-2000-group-of-a-sandpile](pages/rossin-2000-group-of-a-sandpile.md)] §2 L37 - "the group structure does not depend on the sink choice in the graph G".
[^2]: [[dhar-1990-self-organized-critical-sandpile](pages/dhar-1990-self-organized-critical-sandpile.md)] p.1614 L104-137 [synthesis] - two critical sites give the same configuration in either toppling order, toppling commutes with adding a particle, so `a_i a_j C = a_j a_i C` for all `i, j` (eq. 5).
[^3]: [[dhar-1990-self-organized-critical-sandpile](pages/dhar-1990-self-organized-critical-sandpile.md)] p.1614 L85-101 [synthesis] - "all nonrecurrent configurations are transients, and have zero probability of occurrence in the SOC state"; "only recurrent configurations have a nonzero probability of occurrence, and this nonzero value is the same for all recurrent configurations."
[^4]: Verified by execution (Python 3.10, SymPy, 2026-09-26): `recurrent((2, 2))` is the four configurations listed and `recurrent((2, 2), 'tide')` the three listed; `det L̃ = 4` (sink) and 3 (tide); the identities `stab(2·c_max − stab(2·c_max))` are `(1, 1, 0)` (sink) and `(1, 1)` (tide).
[^5]: Verified by execution (Python 3.10, 2026-09-26): the sink trace topples one unstable cell at a time (first unstable cell in the order BL, TL, BM, TM, BR, TR) from `TL=1, TM=2, TR=1, BM=2, BR=1` plus one grain on `TR`, and settles at `TL=1, TM=2, TR=1, BM=1, BR=0` after 11 topplings with 3 grains absorbed; the Snippet's `stabilize`, which topples every unstable cell in each sweep, reaches the same pile, as pinned. The tide trace from `TL=1, TM=2, TR=1` plus one grain on `TR` settles at `TL=0, TM=1, TR=1` after 3 topplings with 3 grains absorbed; `recurrent((2, 2, 2), 'tide')` has 8 elements, as pinned.
[^6]: [[dhar-ruelle-sen-verma-1995-algebraic-aspects](pages/dhar-ruelle-sen-verma-1995-algebraic-aspects.md)] §2-3 pp. 4-10 [synthesis] - `|G| = |R| = Det Δ` (2.4), and the structure `G = Z_{d_1} × … × Z_{d_g}` from the Smith decomposition `Δ = ADB` of the toppling matrix (3.9)-(3.17).
[^7]: [[dhar-1990-self-organized-critical-sandpile](pages/dhar-1990-self-organized-critical-sandpile.md)] pp.1614-1615 L102-172, L199-220 [synthesis] - adding `Δ_ii` particles at `i` gives `∏_j a_j^{Δ_ij} = 1` (eqs. 8-9); equivalent configurations differ by `Σ_j r_j Δ_ij` (eq. 17); `N_R = Det Δ` (eq. 13). For a castle, `Δ = L̃` of the model.
[^8]: [[dhar-1990-self-organized-critical-sandpile](pages/dhar-1990-self-organized-critical-sandpile.md)] p.1615 L173-177 - "Since all these configurations occur with equal probability in the SOC state, the entropy of the SOC state S is given by S = ln Det Δ" (eq. 14).
[^9]: Verified by execution (NumPy, SciPy, 2026-09-27): the double integral of eq. 16 of [[dhar-1990-self-organized-critical-sandpile](pages/dhar-1990-self-organized-critical-sandpile.md)] evaluates to `1.166244`, equal to `4 × 0.915966/π`; `slogdet` of the reduced Laplacian of `ℓ × ℓ` rectangles with the corner cell as the sink, and of `ℓ × ℓ` cells above the ground in the tide model, for `ℓ = 10, 20, 40, 60`.
[^10]: [[dhar-1990-self-organized-critical-sandpile](pages/dhar-1990-self-organized-critical-sandpile.md)] p.1615 L191-214 [synthesis] - forbidden subconfigurations (eq. 18) and the recursive deletion test; "all recurrent configurations are allowed. The converse statement appears quite plausible, though a strict proof is lacking."
[^11]: [[chau-cheng-1991-deterministic-soc-sandpile](pages/chau-cheng-1991-deterministic-soc-sandpile.md)] p.104-105 L99-111, L173-174 [synthesis] - completely deterministic means `a_i|_R = a_j|_R` for all `i, j` (eq. 5), the evolution depending "only on the total number of particles added"; then "R is isomorphic to the group Z_{n+1}", and eq. 13 gives the fundamental toppling rules that are deterministic.
[^12]: Verified by execution (Python 3.10, exact rational arithmetic, 2026-09-27): for every mirror-distinct castle with at most 12 cells, in the sink model (bottom-left sink cell) and in the tide model (castles of height at least 2), the grain classes `L̃⁻¹ e_v` agree modulo integers for all cells `v` only when `L̃⁻¹` is integral (trivial group): 769 trivial and 1,372 nontrivial castles in the sink model, 758 and 1,372 in the tide model, and no nontrivial deterministic one.
[^13]: Verified by execution (Python 3.10, SymPy, 2026-09-26): `laplacian(c) == boundary(c)·boundary(c)ᵀ` and `boundary(c)·cycle_matrix(c) = 0` for `c = (3, 3, 3)`, as pinned; the identity `L = ∂∂ᵀ` is the standard factorization of the graph Laplacian through the oriented incidence matrix.
[^14]: Verified by execution (Python 3.10, SymPy, 2026-09-26): for every castle with at most 10 cells (1,023 compositions), the invariant factors of the reduced Laplacian equal those of the block matrix with `4` on the diagonal and `−1` for edge-sharing blocks; `CᵀC` equals that block matrix for `(3, 3, 3)` as pinned. On 300 random castles to 16 cells the group is the same for every choice of sink cell. The underlying fact, that the sandpile group of a connected plane graph equals that of its dual, is Cori and Rossin's theorem (European J. Combin. 21 (2000) 447-459), known here through [[rossin-2000-group-of-a-sandpile](pages/rossin-2000-group-of-a-sandpile.md)] (reference [5], L106) and the paper's published abstract, "the sandpile group of planar graph is isomorphic to that of its dual" (https://www.researchgate.net/publication/222032277); the paper itself has not been read. An example from the literature: [[rossin-2000-group-of-a-sandpile](pages/rossin-2000-group-of-a-sandpile.md)] §4 L92-94 gives the group of the `2 × 2` grid with each cell joined twice to the sink, the dual of `(3, 3, 3)`, as "the product of two cyclic group of orders 24 and 8", of order 192, matching `Z/8 × Z/24` and the 192 recurrent piles pinned here.
[^15]: Verified by execution (Python 3.10, 2026-09-26): for all 33,150 mirror-distinct castles with at most 16 cells, the invariant factors of the tide model's reduced Laplacian (bottom row deleted, full degrees kept) equal those of the tide block matrix (3 for blocks with lower-left cell in row 0, 4 otherwise, −1 for edge-sharing blocks); an integer Smith normal form routine used for the sweep agrees with SymPy's on 300 random castles in both models. The ladder orders are pinned in the Snippet and match OEIS A001906 and A001835 (fetched 2026-09-26). The planar-dual argument in the text combines two facts, contraction in a plane graph is deletion in its dual (standard) and Cori-Rossin duality (known through the sources of [^14], paper not read), and is the page's own assembly of them.
[^16]: [[dhar-ruelle-sen-verma-1995-algebraic-aspects](pages/dhar-ruelle-sen-verma-1995-algebraic-aspects.md)] §3 p. 6 and §4 p. 12, eqs. (4.6a-d) and (4.7) - the Laplacian with `Δ_ii = 4` "implies open boundary conditions on all four boundaries of the rectangle"; the four groups as quoted; "g = L, for L_1 = L_2 = L". Verified by execution (Python 3.10, 2026-09-27): the sink groups of `(3,3,3)`, `(4,4,4,4)`, `(5,5,5,5,5)` and `(6,6,6,6,6,6)` from the cell-side Laplacian are those four groups, with 2, 3, 4 and 5 cyclic factors.
