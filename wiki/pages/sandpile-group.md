---
title: Sandpile groups of castles - sand, cycles, and 2×2 blocks
category: Concepts
summary: An introduction to the sandpile group (also called the critical group or Jacobian) of a castle graph, starting from the game and ending at the linear algebra. Grains sit on cells; a cell holding at least as many grains as it has neighbours topples, sending one grain to each; one cell is a drain where grains vanish. The configurations that keep coming back as sand is added form a finite group whose size is the number of spanning trees. In matrix terms it is Z^n modulo the reduced Laplacian, and the Laplacian factors through the boundary matrix as L = ∂∂ᵀ. The cycles of the castle graph (the kernel of ∂) have the castle's 2×2 blocks as a basis, and because castles are planar the group can be read off a much smaller matrix, one row per 2×2 block, with 4 on the diagonal and −1 for each pair of blocks sharing an edge (checked on all 1,023 castles up to 10 cells). So the 2×2 blocks hold the sand. Tree castles (golden paths, battlements) hold none, the 4-cycle (2,2) gives Z/4, the silver rectangle (2,2,2) and any castle with two side-by-side blocks give Z/15, the 2-wide ladders give Z/4, Z/15, Z/56, Z/209, …, and (3,3,3) gives Z/8 × Z/24. A runnable block reproduces every example.
tags: [concept, castle, sandpile, abelian-sandpile, critical-group, chip-firing, laplacian, boundary-matrix, cycle-space, spanning-trees, smith-normal-form, tree-castle, planar-dual, pedagogy]
sources: [project-euler-502-castle-factoring]
created: 2026-09-26
updated: 2026-09-26
---

# Sandpile groups of castles - sand, cycles, and 2×2 blocks

This page introduces the **sandpile group** of a castle for readers who have not met it before. It starts with a game you can play on paper, then connects the game to matrices the wiki already uses: the Laplacian of [[hear-the-shape-seminar](pages/hear-the-shape-seminar.md)], the boundary matrix, and the cycles of [[castle-graph](pages/castle-graph.md)]. The one picture to keep is at the end of Part 3: **a castle's sand lives in its 2×2 blocks**.

## Part 1 - the game

Take a castle and its graph: one vertex per filled cell, one edge per pair of cells that share a side ([[castle-graph](pages/castle-graph.md)]). Pick one cell as the **drain**. In this page it is always the bottom-left cell, but any cell works.

- **Sand.** Put a whole number of grains on every other cell. That is a *configuration*.
- **Toppling.** A cell that holds at least as many grains as it has neighbours is unstable. It **topples**: it sends one grain to each neighbour. Grains that reach the drain disappear.
- **Stabilizing.** Keep toppling until no cell is unstable. Because the drain removes sand, this always stops, and the final configuration does not depend on the order of the topplings. That is why the model is called **abelian**.[^1]

**Add sand forever.** Drop grains on cells one at a time, stabilizing after each drop. Some stable configurations appear only near the start and never come back. The others, the **recurrent** configurations, keep coming back no matter how long you play.

**The recurrent configurations form a group.** Add two recurrent configurations cell by cell and stabilize: the result is recurrent again. This operation has an identity element and inverses, so the recurrent configurations form a finite abelian group, the **sandpile group** `K(G)`. It is also called the critical group or the Jacobian of the graph. Its size is the **number of spanning trees** of the graph, and it does not depend on which cell is the drain.[^1]

### Worked example: the 4-cycle `(2, 2)`

`(2, 2)` is a `2 × 2` square of four cells, each with two neighbours. Make the bottom-left cell the drain. The other three cells are stable with 0 or 1 grain each, so there are `2³ = 8` stable configurations. Exactly **4** of them are recurrent: the ones with **at most one empty cell**.

```
recurrent (grains on top-left, bottom-right, top-right):   (0,1,1)  (1,0,1)  (1,1,0)  (1,1,1)
transient:                                                 (0,0,0)  (1,0,0)  (0,1,0)  (0,0,1)
```

Four recurrent configurations means `K = Z/4`, and the square has 4 spanning trees (delete any one of its 4 edges). The identity element is `(1, 1, 0)`: one grain on each cell next to the drain and none on the far corner. Adding it to any recurrent configuration and stabilizing gives that configuration back.[^2]

## Part 2 - the matrices behind the game

**Toppling is subtracting a column of the Laplacian.** When cell `v` topples it loses `deg(v)` grains and each neighbour gains one. That is subtracting column `v` of the Laplacian `L = D − A` ([[hear-the-shape-seminar](pages/hear-the-shape-seminar.md)], Stop 0) from the configuration. So two configurations that differ by topplings are the same element of

```
K(G)  =  Z^{n−1} / L̃ Z^{n−1}          (L̃ = L with the drain's row and column deleted)
```

This is a finite abelian group of order `det L̃`, the number of spanning trees by Kirchhoff's matrix-tree theorem. Its structure, a product of cyclic groups `Z/d_1 × Z/d_2 × …`, is read off the **Smith normal form** of `L̃`, the same tool [[castle-ring-invariant-factors](pages/castle-ring-invariant-factors.md)] uses for unit groups.[^1]

**The Laplacian factors through the boundary matrix.** Give every edge a direction. The **boundary matrix** `∂` has one row per cell and one column per edge, with `+1` at the edge's tail and `−1` at its head. It records which cells each edge joins. Then

```
L  =  ∂ ∂ᵀ
```

because `(∂∂ᵀ)[u, u]` counts the edges at `u`, and `(∂∂ᵀ)[u, v] = −1` when an edge joins `u` and `v`.[^3]

## Part 3 - cycles, and why the 2×2 blocks hold the sand

**Cycles are the kernel of `∂`.** A combination of edges (each with an integer coefficient) whose boundary is zero goes around closed loops: every cell is entered as often as it is left. These combinations form the **cycle space**, the kernel of `∂`. Its dimension is the **cycle rank** `|E| − |V| + 1`.

**For a castle, the cycles are generated by the 2×2 blocks.** A castle graph is a piece of the square grid with no holes, so its only "faces" are the filled `2 × 2` blocks. Going once around a block's four edges is a cycle, and the blocks' cycles form a basis of all cycles. The cycle rank is the number of `2 × 2` blocks ([[castle-graph](pages/castle-graph.md)]). Put these basis cycles as the columns of the **cycle matrix** `C`, one column per block. Then `∂C = 0`.

**The block matrix.** The Gram matrix `CᵀC` compares the block cycles with each other. Each block's cycle has four edges, and two blocks that share an edge traverse it in opposite directions:

```
CᵀC[a, a]  =  4          CᵀC[a, b]  =  −1  if blocks a and b share an edge,   0 otherwise
```

For a planar graph like a castle, this small matrix, **one row per 2×2 block**, carries the whole sandpile group:

```
K(castle)  =  Z^r / (CᵀC) Z^r          (r = number of 2×2 blocks)
```

It is the sandpile group of the planar dual graph, whose vertices are the blocks. This was checked against the cell-side formula on all 1,023 castles with up to 10 cells.[^4] So **the 2×2 blocks hold the sand**. A castle with no `2 × 2` block has no cycles, a single spanning tree, and a trivial group: sand washes straight out. A castle's sandpile group depends only on how its blocks are arranged, not on the towers and spikes around them.

## Part 4 - the castle gallery

| castle | kind of castle | 2×2 blocks | block arrangement | sandpile group |
|---|---|---|---|---|
| `(1,1,1,1)`, `(1,2,1)`, `(1,2,1,3,1)` | tree castles: golden path, spike, battlement | 0 | - | trivial |
| `(2, 2)` | the 4-cycle | 1 | one block | `Z/4` |
| `(2, 2, 2)` | silver rectangle `3 × 2` | 2 | two side by side | `Z/15` |
| `(3, 3)`, `(1, 2, 3, 2, 1)` | tall pair, staircase | 2 | two sharing an edge | `Z/15` |
| `(1,1,1,2,3,2)`, `(1,1,2,2,3,1)` | the 10-cell isospectral pair | 2 | two sharing an edge | `Z/15` |
| `(2, 2, 2, 2)`, `(2, 2, 2, 2, 2)` | 2-wide ladders | 3, 4 | a row of blocks | `Z/56`, `Z/209` |
| `(2, 2, 1, 2, 2)` | two separated squares | 2 | two apart | `Z/4 × Z/4` |
| `(3, 3, 3)` | `3 × 3` square | 4 | a `2 × 2` square of blocks | `Z/8 × Z/24` |
| `(2, 3, 3, 2)` | a hill | 4 | a T of blocks | `Z/4 × Z/52` |

**The prototype: the ladder.** A 2-wide ladder `(2, 2, …, 2)` has a single row of blocks, so its block matrix is tridiagonal, with `4` on the diagonal and `−1` beside it. The group is cyclic, of order `4, 15, 56, 209, …` (OEIS A001353, `a(n) = 4a(n−1) − a(n−2)`). Picture any castle as its skeleton of `2 × 2` blocks. Separated groups of blocks contribute independent factors (two isolated squares give `Z/4 × Z/4`), a row of `r` blocks contributes one cyclic group of that ladder order, and denser arrangements such as the `2 × 2` square of blocks in `(3, 3, 3)` or the T in `(2, 3, 3, 2)` split into two cyclic factors.

**What this means for the isospectral pairs.** The 10-cell adjacency-isospectral pair of [[hear-the-shape-seminar](pages/hear-the-shape-seminar.md)] has the same sandpile group, `Z/15`, because both castles have two side-by-side blocks. The 11-cell Laplacian-isospectral pair are trees, so both groups are trivial. On these two pairs the sandpile group separates nothing. [[sandpile-census](pages/sandpile-census.md)] checks every castle to 16 cells: it separates no cospectral pair at all, because cospectral castles there always share their graph of 2×2 blocks.

## A variant: the bottom row as the tide

Some `IDEAS.md` items describe the base row as the sink, as if the ground were the tide that washes sand away. That is a different graph: the whole bottom row is merged into a single drain. It gives a different group, for example `Z/3` for `(2, 2)` instead of `Z/4`, and `Z/8` for `(2, 2, 2)` instead of `Z/15`. Everything on this page uses the castle graph itself with one cell as the drain, whose group does not depend on the choice of drain cell.[^5]

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

def invariant_factors(M):                  # the group Z^n / M Z^n, as its nontrivial cyclic factors
    if M.rows == 0:
        return []
    S = smith_normal_form(M, domain=ZZ)
    return [abs(S[i, i]) for i in range(M.rows) if abs(S[i, i]) != 1]

def sandpile_group(c):                     # from the cells: reduced Laplacian (drop the drain cell)
    return invariant_factors(laplacian(c)[1:, 1:])

def sandpile_group_from_blocks(c):         # from the 2x2 blocks: Gram matrix of the cycle basis
    C = cycle_matrix(c)
    return invariant_factors(C.T * C)

def stabilize(c, grains, drain=0):         # topple every cell holding >= its degree, until none does
    cells, _, edges = castle_graph(c)
    nbrs = [[] for _ in cells]
    for u, v in edges:
        nbrs[u].append(v); nbrs[v].append(u)
    g = list(grains)
    while any(g[v] >= len(nbrs[v]) for v in range(len(g)) if v != drain):
        for v in range(len(g)):
            if v != drain and g[v] >= len(nbrs[v]):
                g[v] -= len(nbrs[v])
                for u in nbrs[v]:
                    g[u] += 1
        g[drain] = 0
    g[drain] = 0
    return tuple(g)

def recurrent(c, drain=0):                 # configurations reachable again and again by adding sand
    cells, _, edges = castle_graph(c)
    deg = [sum(v in e for e in edges) for v in range(len(cells))]
    top = tuple(0 if v == drain else deg[v] - 1 for v in range(len(cells)))
    seen, todo = {top}, [top]
    while todo:
        x = todo.pop()
        for v in range(len(cells)):
            if v != drain:
                y = stabilize(c, x[:v] + (x[v] + 1,) + x[v+1:], drain)
                if y not in seen:
                    seen.add(y); todo.append(y)
    return seen
```

```
>>> castle_graph((2, 2))[0]
[(0, 0), (0, 1), (1, 0), (1, 1)]
>>> sorted(recurrent((2, 2)))
[(0, 0, 1, 1), (0, 1, 0, 1), (0, 1, 1, 0), (0, 1, 1, 1)]
>>> sandpile_group((2, 2)), laplacian((2, 2))[1:, 1:].det()
([4], 4)
>>> c = (3, 3, 3)
>>> laplacian(c) == boundary(c) * boundary(c).T, (boundary(c) * cycle_matrix(c)).is_zero_matrix
(True, True)
>>> cycle_matrix(c).T * cycle_matrix(c)
Matrix([
[ 4, -1, -1,  0],
[-1,  4,  0, -1],
[-1,  0,  4, -1],
[ 0, -1, -1,  4]])
>>> sandpile_group(c), sandpile_group_from_blocks(c), len(recurrent(c))
([8, 24], [8, 24], 192)
>>> [(c, len(blocks(c)), sandpile_group_from_blocks(c)) for c in [(1, 2, 1, 3, 1), (2, 2), (2, 2, 2), (2, 2, 2, 2), (2, 2, 1, 2, 2), (2, 3, 3, 2)]]
[((1, 2, 1, 3, 1), 0, []), ((2, 2), 1, [4]), ((2, 2, 2), 2, [15]), ((2, 2, 2, 2), 3, [56]), ((2, 2, 1, 2, 2), 2, [4, 4]), ((2, 3, 3, 2), 4, [4, 52])]
>>> [sandpile_group(c) for c in [(3, 3), (1, 2, 3, 2, 1), (1, 1, 1, 2, 3, 2), (1, 1, 2, 2, 3, 1)]]
[[15], [15], [15], [15]]
```

In the recurrent tuples the positions are the cells in the order `castle_graph` lists them: the drain `(0,0)` first, which always holds 0, then top-left `(0,1)`, bottom-right `(1,0)` and top-right `(1,1)`.

## Related Concepts

- [[castle-graph](pages/castle-graph.md)] - the graph, its cycle rank (the number of 2×2 blocks), and tree castles.
- [[hear-the-shape-seminar](pages/hear-the-shape-seminar.md)] / [[isospectral-castles](pages/isospectral-castles.md)] - the Laplacian and the cospectral pairs the sandpile group is tested against.
- [[castle-ring-invariant-factors](pages/castle-ring-invariant-factors.md)] - the other place the wiki reads a finite abelian group off a Smith normal form.
- [[castle-graph-spectral-radius](pages/castle-graph-spectral-radius.md)] - the golden and silver castles of the gallery.
- [[spectral-analysis](pages/spectral-analysis.md)] - method 4 (the Laplacian) and method 5 (the Ihara zeta), which also sees the spanning-tree count.
- [[sandpile-census](pages/sandpile-census.md)] - the census: every castle to 16 cells, and why the group separates no cospectral pair.
- [[sandcastle-clock](pages/sandcastle-clock.md)] - the clock: drop one grain per tick and count ticks until the identity returns.


## Appearances in Sources

- [[project-euler-502-castle-factoring](pages/project-euler-502-castle-factoring.md)] - the castle definition (column heights `≥ 1`) behind the castle graph.

## Footnotes

[^1]: https://en.wikipedia.org/wiki/Abelian_sandpile_model - toppling at the degree, a sink vertex, order-independence of stabilization (the abelian property), recurrent configurations forming the sandpile group under addition followed by stabilization, its presentation as `Z^{n−1}` modulo the reduced Laplacian, and its order equal to the number of spanning trees (Kirchhoff's matrix-tree theorem, with Dhar's burning bijection between recurrent configurations and spanning trees).
[^2]: Verified by execution (Python 3.10, SymPy, 2026-09-26): `recurrent((2, 2))` is the four configurations listed; `det L̃ = 4`; the identity `stab(2·c_max − stab(2·c_max))` evaluates to one grain on each of the drain's two neighbours and none on the far corner.
[^3]: Verified by execution (Python 3.10, SymPy, 2026-09-26): `laplacian(c) == boundary(c)·boundary(c)ᵀ` and `boundary(c)·cycle_matrix(c) = 0` for `c = (3, 3, 3)`, as pinned; the identity `L = ∂∂ᵀ` is the standard factorization of the graph Laplacian through the oriented incidence matrix.
[^4]: Verified by execution (Python 3.10, SymPy, 2026-09-26): for every castle with at most 10 cells (1,023 compositions), the invariant factors of the reduced Laplacian equal those of the block matrix with `4` on the diagonal and `−1` for edge-sharing blocks; `CᵀC` equals that block matrix for `(3, 3, 3)` as pinned. The underlying fact, that the sandpile group of a connected plane graph equals that of its dual, is standard (Cori and Rossin, 2000).
[^5]: Verified by execution (Python 3.10, SymPy, 2026-09-26): merging all bottom-row cells into one drain gives invariant factors `[3]` for `(2, 2)`, `[8]` for `(2, 2, 2)`, `[95]` for `(3, 3, 3)`, and the trivial group for `(1, 2, 1)`.
