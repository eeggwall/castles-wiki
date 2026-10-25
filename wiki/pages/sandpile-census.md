---
title: Sandpile census - every castle to 16 cells, in the sink and tide models
category: Analyses
summary: The sandpile groups of the 33,150 castles with at most 16 cells (mirror images removed), in the sink model (one sink cell) and the tide model (the bottom row as the sink) of sandpile-group, computed from the 2×2-block matrices and checked against the cell-side reduced Laplacian. The 2×2 blocks' cycles are an integer basis of the cycle lattice of every castle with blocks, in both models. Both groups are trivial exactly on the 6,963 tree castles (A005683). In the sink model the commonest groups are Z/4 (one block), Z/15 (two adjacent blocks), Z/56 and Z/209 (paths of three and four blocks); the sink group separates none of the 105 adjacency-cospectral and 17 Laplacian-cospectral groups, because the castles in each share their graph of blocks. In the tide model each sink group splits by how many blocks sit on the bottom row (Z/15 into Z/8 and Z/11; Z/56 into Z/21, Z/29 and Z/41), the tide group differs between skylines of the same graph on 2,254 of the 6,443 graphs with several skylines, and it separates 23 of the 105 adjacency-cospectral groups. A path of blocks gives a cyclic group in both models; 29,439 castles have a cyclic sink group and 30,617 a cyclic tide group; (3, 3, 3) is Z/8 × Z/24 in the sink model and Z/95 in the tide model, and (4, 4, 4) is Z/2415 and Z/13 × Z/91.
tags: [analysis, castle, sandpile, critical-group, census, isospectral, laplacian, adjacency, smith-normal-form, cyclic-group, tree-castle, block-graph, sink-model, tide-model, numpy, sympy, verification]
sources: [rossin-2000-group-of-a-sandpile, dhar-ruelle-sen-verma-1995-algebraic-aspects, dhar-1990-self-organized-critical-sandpile, chau-cheng-1991-deterministic-soc-sandpile, project-euler-502-castle-factoring]
created: 2026-09-26
updated: 2026-10-25
---

# Sandpile census - every castle to 16 cells, in the sink and tide models

This page computes the sandpile groups `K_sink` and `K_tide` of every castle with at most 16 cells, in the two models of [[sandpile-group](pages/sandpile-group.md)]: the sink model, with one sink cell, and the tide model, with the whole bottom row as the sink. The results:

1. The `2 × 2` blocks give an integer basis of the cycle lattice of every castle with blocks, in both models: [[castle-graph](pages/castle-graph.md)] proves it, and section 1 checks it to 16 cells.
2. The groups of all 33,150 castles, mirror images removed, in both models (section 2).
3. The sink group separates none of the cospectral groups of [[isospectral-castles](pages/isospectral-castles.md)], because the castles in each share their graph of blocks; the tide group, which also depends on which blocks sit on the bottom row, separates 23 of them (section 3).
4. A path of blocks gives a cyclic group in both models, and the tide group is cyclic more often (section 4).

## Method

Each castle's groups are computed from its **block matrices**, one row per `2 × 2` block with `−1` for blocks sharing an edge, and on the diagonal 4 for every block in the sink model, and 3 for a block on the bottom row and 4 above it in the tide model ([[sandpile-group](pages/sandpile-group.md)], Part 3, Equations (4) and (5)). The invariant factors come from the Smith normal form, computed with an integer routine that agrees with SymPy's on random matrices. The groups from the block matrices equal those from the cell-side reduced Laplacian `L̃` on all 33,150 castles, in both models.[^1] For the spectra, castles are grouped by their adjacency and Laplacian eigenvalues rounded to 7 decimals, and the castles in a group are sorted into isomorphism classes by an exact graph-isomorphism test. This reproduces the counts of cospectral groups of [[isospectral-castles](pages/isospectral-castles.md)] at every size: 2, 0, 10, 6, 18, 19 and 50 adjacency-cospectral groups and 0, 1, 0, 2, 2, 5 and 7 Laplacian-cospectral groups at 10 to 16 cells.[^2]

## 1. The 2×2 blocks are an integer basis of the cycles

Put the boundary cycle of each `2 × 2` block as a column of the cycle matrix `C`, with one row per edge. For all 26,187 castles with at most 16 cells that have a block, the Smith normal form of `C` has every invariant factor equal to 1, so every integer cycle is an integer combination of block cycles. With the rank count `cycle rank = number of blocks` of [[castle-graph](pages/castle-graph.md)], the block cycles are a basis of the cycle lattice. The same holds in the tide model, where the cycle of a block on the bottom row is the triangle through the merged bottom row and the other blocks keep their 4-cycles.[^3] [[castle-graph](pages/castle-graph.md)] proves both for every castle, from the spanning tree formed by the columns and the bottom row.

## 2. The census, in both models

| cells | castles | trivial group (tree castles, both models) | cyclic `K_sink` | distinct `K_sink` | cyclic `K_tide` | distinct `K_tide` |
|---|---|---|---|---|---|---|
| 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| 2 | 2 | 2 | 2 | 1 | 2 | 1 |
| 3 | 3 | 3 | 3 | 1 | 3 | 1 |
| 4 | 6 | 5 | 6 | 2 | 6 | 2 |
| 5 | 10 | 8 | 10 | 2 | 10 | 2 |
| 6 | 20 | 13 | 20 | 3 | 20 | 4 |
| 7 | 36 | 22 | 36 | 3 | 36 | 4 |
| 8 | 72 | 37 | 72 | 4 | 72 | 7 |
| 9 | 136 | 63 | 134 | 6 | 135 | 9 |
| 10 | 272 | 108 | 264 | 8 | 268 | 14 |
| 11 | 528 | 186 | 503 | 10 | 513 | 18 |
| 12 | 1,056 | 322 | 997 | 13 | 1,015 | 27 |
| 13 | 2,080 | 559 | 1,933 | 18 | 1,975 | 38 |
| 14 | 4,160 | 973 | 3,791 | 25 | 3,902 | 56 |
| 15 | 8,256 | 1,697 | 7,338 | 34 | 7,631 | 78 |
| 16 | 16,512 | 2,964 | 14,329 | 48 | 15,028 | 113 |
| **1-16** | **33,150** | **6,963** | **29,439** | | **30,617** | |

Every entry agrees with a recomputation from the block matrices.[^4] The trivial column is the same in both models, because both groups are trivial exactly on the tree castles ([[sandpile-group](pages/sandpile-group.md)], Part 3). It is `A005683` term for term: the tree castles of `n` cells number `A005251(n+2)`, the palindromic ones are the Padovan numbers `A000931(n+6)`, and the castles up to mirror image number `(A005251(n+2) + A000931(n+6))/2` by Burnside's lemma ([[castle-graph](pages/castle-graph.md)], section *Up to mirror image*).[^4]

### The commonest sink groups

The sink group depends only on how the blocks touch each other, so the arrangement column describes every castle in the row:[^4]

| `K_sink` | castles (to 16 cells) | block arrangement | smallest castle |
|---|---|---|---|
| `Z/4` | 8,027 | one isolated block | `(2, 2)` |
| trivial | 6,963 | no blocks (a tree castle) | `(1)` |
| `Z/15` | 5,985 | two blocks sharing an edge | `(2, 2, 2)` |
| `Z/56` | 3,328 | three blocks in a path | `(2, 2, 2, 2)` |
| `Z/4 × Z/4` | 1,974 | two isolated blocks | `(2, 2, 1, 2, 2)` |
| `Z/60` | 1,762 | a pair plus an isolated block (`Z/15 × Z/4`) | `(2, 2, 1, 2, 2, 2)` |
| `Z/209` | 1,606 | four blocks in a path | `(2, 2, 2, 2, 2)` |
| `Z/780` | 569 | five blocks in a path | `(2, 2, 2, 2, 2, 2)` |

The smallest castle of each group is the first by number of cells, then lexicographically. The path orders `4, 15, 56, 209, 780` are `A001353`, the orders of the 2-wide ladders. The first non-cyclic groups occur at 9 cells, `Z/4 × Z/4` for `(2, 2, 1, 2, 2)` and `Z/8 × Z/24` for `(3, 3, 3)`. Up to 16 cells a group has at most three cyclic factors, first `Z/4 × Z/4 × Z/4` for `(2, 2, 1, 2, 2, 1, 2, 2)`. The largest group is `Z/4 × Z/112 × Z/224`, of order 100,352, for `(4, 4, 4, 4)`.

**Square and height-3 castles, from the dual side.** The sink block matrix of the `(L+1) × (L+1)` castle is the Laplacian of an `L × L` grid with open boundaries, and Dhar, Ruelle, Sen and Verma show, with a sketched proof, that its group has exactly `L` cyclic factors, as the census finds for `(3, 3, 3)` (2 factors) and `(4, 4, 4, 4)` (3 factors). Their groups for `L = 4` and `L = 5`, beyond the census, are those of the castles `(5, 5, 5, 5, 5)` and `(6, 6, 6, 6, 6, 6)` ([[sandpile-group](pages/sandpile-group.md)], Part 4). Their `L × 2` strip is the castle `(3, …, 3)` of height 3 and width `w = L + 1`, with sink group `Z/d_1 × Z/d_2`, where

```
d_2  =  gcd(m_w, n_w),        d_1  =  m_w n_w / d_2,
```

`m_w = F_{2w}` are the even-indexed Fibonacci numbers and `n_w = A004254(w)`, with `n_{w+1} = 5n_w − n_{w−1}`. The formula agrees with the census at every width from 2 to 16. Since `m_w` is also the tide order of the ladder `(2, …, 2)` of width `w`, the sink order of the height-3 castle factors across the models, `|K_sink((3, …, 3))| = |K_tide((2, …, 2))| · A004254(w)`; at `w = 3`, `192 = 8 · 24`. The paper proves that `d_2 > 1`, so that the group is not cyclic, whenever 3 divides `w`, and calls this the only result it could establish about `d_2`, which behaves irregularly. Up to width 16 the group is non-cyclic at `w = 3, 6, 7, 9, 10, 12, 14, 15`.[^5]

A **path of blocks** need not be straight. `(2, 2, 2, 2)`, three blocks in a row, and `(3, 3, 2)`, three blocks in an L, both have `K_sink = Z/56`, because in both each block shares an edge with the next.

### The commonest tide groups

The tide group also records which blocks sit on the bottom row, so each sink group splits by how the blocks stand. Each tide group in the table occurs with exactly one sink group:[^6]

| `K_tide` | castles (to 16 cells) | block arrangement | `K_sink` of the same castles | smallest castle |
|---|---|---|---|---|
| `Z/3` | 8,027 | one isolated block (always on the bottom row) | `Z/4` | `(2, 2)` |
| trivial | 6,963 | no blocks | trivial | `(1)` |
| `Z/8` | 3,773 | two blocks side by side, both on the bottom row | `Z/15` | `(2, 2, 2)` |
| `Z/11` | 2,212 | two blocks stacked, one on the bottom row | `Z/15` | `(3, 3)` |
| `Z/3 × Z/3` | 1,974 | two isolated blocks | `Z/4 × Z/4` | `(2, 2, 1, 2, 2)` |
| `Z/21` | 1,564 | three blocks in a row on the bottom row | `Z/56` | `(2, 2, 2, 2)` |
| `Z/29` | 1,173 | three blocks in an L, two on the bottom row | `Z/56` | `(2, 3, 3)` |
| `Z/24` | 1,043 | a pair on the bottom row plus an isolated block (`Z/8 × Z/3`) | `Z/60` | `(2, 2, 1, 2, 2, 2)` |
| `Z/33` | 719 | a stacked pair plus an isolated block (`Z/11 × Z/3`) | `Z/60` | `(2, 2, 1, 3, 3)` |
| `Z/55` | 595 | four blocks in a row on the bottom row | `Z/209` | `(2, 2, 2, 2, 2)` |
| `Z/41` | 591 | three blocks stacked, one on the bottom row | `Z/56` | `(4, 4)` |

A path of three blocks has `K_sink = Z/56` however it bends. In the tide model its order depends on how many of its blocks sit on the bottom row: 21 for three, 29 for two, 41 for one. The row of blocks lying down gives the orders `3, 8, 21, 55, 144` (`A001906`) and the column standing up gives `3, 11, 41, 153, 571` (`A001835`). The largest tide group to 16 cells is again that of `(4, 4, 4, 4)`, now cyclic, `Z/31529`. A tide group has at most three cyclic factors, first `Z/3 × Z/3 × Z/3` for `(2, 2, 1, 2, 2, 1, 2, 2)`.

## 3. What each group separates

**The sink group separates no cospectral group.**

| cospectral groups (to 16 cells) | number | separated by `K_sink` |
|---|---|---|
| same adjacency spectrum | 105 | **0** |
| same Laplacian spectrum | 17 (11 of them of tree castles only) | **0** |

In every one of the 122 cospectral groups, the castles have isomorphic **graphs of 2×2 blocks**, with blocks as vertices joined when they share an edge. By [[sandpile-group](pages/sandpile-group.md)] the sink group is determined by that graph (Equation (4)), so on these castles it distinguishes nothing the spectrum does not.[^7] The 11-cell Laplacian-cospectral pair of [[hear-the-shape-seminar](pages/hear-the-shape-seminar.md)] is two tree castles, both with trivial groups, and the 10-cell adjacency-cospectral pair has two adjacent blocks in both castles, both with `K_sink = Z/15`. A pair of castles with the same Laplacian spectrum and different sink groups would need different block graphs, and none occurs up to 16 cells.

**The tide group depends on the skyline as well as the graph.** Up to 16 cells, 6,443 castle graphs are the graph of more than one skyline, and for 2,254 of them different skylines have different tide groups; the sink group never differs, since it depends only on the graph. The first example is the rectangle `(2, 2, 2)`, with `K_tide = Z/8`, against `(3, 3)`, with `Z/11`: the same `3 × 2` grid lying down and standing up.[^6]

So the tide group can separate a cospectral group through its other skylines. The 10-cell pair's own skylines `(1, 1, 1, 2, 3, 2)` and `(1, 1, 2, 2, 3, 1)` both have `K_tide = Z/8`, but `(1, 3, 5, 1)`, another skyline with the graph of `(1, 1, 2, 2, 3, 1)`, has `Z/11`. Counting a cospectral group as separated when two skylines of different graphs in it have different tide groups, 23 of the 105 adjacency-cospectral groups and none of the 17 Laplacian-cospectral groups are separated up to 16 cells.[^7] The tide group is the product of the groups of the castle's runs of raised columns, and each records how its blocks stand on the bottom row.

## 4. Cyclic groups, in both models

**Sink model.** The shape of the clusters, the connected components of the graph of blocks, does not decide cyclicity on its own. `(2, 2, 1, 2, 2)` has two clusters of one block each and the non-cyclic group `Z/4 × Z/4`. Taking a ladder cluster to mean a cluster whose blocks all lie in one row, the condition "every cluster is a ladder" disagrees with cyclicity on 9,547 castles, the first being `(3, 3)`, a vertical 2-wide ladder with the cyclic group `Z/15`.[^8]

In both models:

- **A path of blocks gives a cyclic group.** Ordered along the path, the block matrix is tridiagonal with `−1` beside the diagonal, whatever the diagonal entries. Deleting its first row and last column leaves an upper triangular matrix with `−1` on the diagonal, of determinant `±1`. So the greatest common divisor of the `(r−1) × (r−1)` minors is 1, and the group is cyclic.
- **Clusters multiply.** The block matrix is block diagonal over the clusters, so the group is the product of the clusters' groups. A castle whose clusters are all paths therefore has a cyclic group exactly when the clusters' orders are pairwise coprime: two isolated blocks give `Z/4 × Z/4` (sink) or `Z/3 × Z/3` (tide), but a pair and a single block give `Z/15 × Z/4 = Z/60` (sink) or `Z/8 × Z/3 = Z/24` (tide).

The models differ on the clusters that are not paths:[^8]

| | sink model | tide model |
|---|---|---|
| castles with a non-path cluster and a cyclic group | 921, smallest `(2, 3, 3, 3)`, `Z/712` (11 cells) | 1,660, smallest `(3, 3, 3)`, `Z/95` (9 cells) |
| castles whose blocks form one cluster, not a path, with a non-cyclic group | 837, smallest `(3, 3, 3)`, `Z/8 × Z/24` | 144, smallest `(2, 4, 4, 2)`, `Z/3 × Z/93` (12 cells) |
| castles cyclic in this model only | 168, smallest `(2, 4, 4, 2)` (`Z/776` in the sink model) | 1,346, smallest `(3, 3, 3)` (`Z/95` in the tide model) |

`(3, 3, 3)` has `K_sink = Z/8 × Z/24` and `K_tide = Z/95`, and `(4, 4, 4)` goes the other way, with `K_sink = Z/2415` and `K_tide = Z/13 × Z/91`.[^8]

**Cyclic is not deterministic.** Chau and Cheng's completely deterministic sandpiles, in which every grain acts the same way, have cyclic groups. A castle sandpile is completely deterministic only when its group is trivial, in both models, because some cell has exactly one edge to the sink ([[sandpile-group](pages/sandpile-group.md)], Part 2, Proposition; [[chau-cheng-1991-deterministic-soc-sandpile](pages/chau-cheng-1991-deterministic-soc-sandpile.md)]).

## Snippet

A self-contained version of the census to 12 cells (2,142 castles). It reproduces the commonest groups in both models, the cospectral groups at this size (12 adjacency and 1 Laplacian), the fact that the sink group separates none of them, and the groups of the examples on this page. It separates castles by color refinement, which certifies non-isomorphism; the census itself also tests isomorphism exactly.

```python
import numpy as np, sympy as sp
from collections import defaultdict, Counter
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ

def compositions(n):
    if n == 0:
        yield (); return
    for f in range(1, n + 1):
        for r in compositions(n - f):
            yield (f,) + r

def castles_up_to(n):                      # every castle with at most n cells, mirror images removed
    return [c for m in range(1, n + 1) for c in compositions(m) if not c[::-1] < c]

def blocks(c):                             # 2x2 blocks, by lower-left cell
    return [(i, j) for i in range(len(c) - 1) for j in range(min(c[i], c[i+1]) - 1)]

def block_matrix(c, model='sink'):         # -1 for blocks sharing an edge; 4 on the diagonal, 3 for ground blocks under the tide
    B = blocks(c); pos = {b: k for k, b in enumerate(B)}
    M = sp.zeros(len(B))
    for k, (i, j) in enumerate(B):
        M[k, k] = 3 if model == 'tide' and j == 0 else 4
        for nb in ((i+1, j), (i-1, j), (i, j+1), (i, j-1)):
            if nb in pos:
                M[k, pos[nb]] = -1
    return M

def sandpile_group(c, model='sink'):       # nontrivial invariant factors of Z^r / block_matrix
    if not blocks(c):
        return ()
    S = smith_normal_form(block_matrix(c, model), domain=ZZ)
    return tuple(abs(S[i, i]) for i in range(S.rows) if abs(S[i, i]) != 1)

def castle_adjacency(c):
    cells = [(i, j) for i, h in enumerate(c) for j in range(h)]
    idx = {v: k for k, v in enumerate(cells)}
    A = np.zeros((len(cells), len(cells)))
    for (i, j), u in idx.items():
        for nb in ((i+1, j), (i, j+1)):
            if nb in idx:
                A[u, idx[nb]] = A[idx[nb], u] = 1
    return A

def wl_hash(c, rounds=8):                  # color refinement: different hash => not isomorphic
    A = castle_adjacency(c)
    nb = [list(np.nonzero(A[i])[0]) for i in range(len(A))]
    col = [len(v) for v in nb]
    for _ in range(rounds):
        col = [hash((col[i], tuple(sorted(col[j] for j in nb[i])))) for i in range(len(A))]
    return tuple(sorted(col))

def cospectral_groups(castles, operator):  # sets of non-isomorphic castles sharing a spectrum
    groups = defaultdict(list)
    for c in castles:
        A = castle_adjacency(c)
        M = A if operator == 'adjacency' else np.diag(A.sum(1)) - A
        groups[(sum(c), tuple(np.round(np.linalg.eigvalsh(M), 7)))].append(c)
    out = []
    for cs in groups.values():
        classes = {}
        for c in cs:
            classes.setdefault(wl_hash(c), c)
        if len(classes) >= 2:
            out.append(list(classes.values()))
    return out
```

```
>>> cs = castles_up_to(12); len(cs)
2142
>>> K = {c: sandpile_group(c) for c in cs}; T = {c: sandpile_group(c, 'tide') for c in cs}
>>> Counter(K.values()).most_common(6)
[((), 770), ((4,), 591), ((15,), 402), ((56,), 187), ((209,), 61), ((4, 4), 59)]
>>> Counter(T.values()).most_common(6)
[((), 770), ((3,), 591), ((8,), 251), ((11,), 151), ((21,), 82), ((29,), 69)]
>>> adj, lap = cospectral_groups(cs, 'adjacency'), cospectral_groups(cs, 'laplacian')
>>> len(adj), len(lap), sum(len({K[c] for c in g}) > 1 for g in adj + lap)
(12, 1, 0)
>>> sandpile_group((2, 2, 1, 2, 2)), sandpile_group((2, 2, 2, 1, 2, 2)), sandpile_group((3, 3, 3)), sandpile_group((2, 3, 3, 3))
((4, 4), (60,), (8, 24), (712,))
>>> sandpile_group((2, 2, 2), 'tide'), sandpile_group((3, 3), 'tide'), sandpile_group((3, 3, 3), 'tide'), sandpile_group((2, 4, 4, 2), 'tide')
((8,), (11,), (95,), (3, 93))
>>> [sandpile_group(c, 'tide') for c in [(2, 2, 2, 2), (2, 3, 3), (4, 4)]], sandpile_group((3, 3, 2))
([(21,), (29,), (41,)], (56,))
```

## Related Concepts

- [[sandpile-group](pages/sandpile-group.md)] - the sandpile, the two models, the reduced Laplacian, and the block matrices this census uses.
- [[isospectral-castles](pages/isospectral-castles.md)] and [[hear-the-shape-seminar](pages/hear-the-shape-seminar.md)] - the cospectral groups tested here.
- [[castle-graph](pages/castle-graph.md)] - the cycle rank as the number of `2 × 2` blocks, the proof that the block cycles are an integer basis of the cycle lattice, and the tree castles, counted up to mirror image.
- [[sandcastle-clock](pages/sandcastle-clock.md)] - the clock, the order of one grain at the apex, which separates cospectral castles that the sink group does not.
- [[sandpile-identity](pages/sandpile-identity.md)] - the identity element, the zero of the group, in both models.
- [[castle-avalanches](pages/castle-avalanches.md)] - random dropping in both models, computed from the same inverse reduced Laplacian.
- [[sandcastle-seminar](pages/sandcastle-seminar.md)] - a seminar following the 16-cell castle `(3, 2, 1, 2, 2, 1, 2, 3)`, silver by spectrum, through both models.
- [[spectral-analysis](pages/spectral-analysis.md)] - the other spectra of castles.
- [[castle-sequence-catalogue](pages/castle-sequence-catalogue.md)] - the census columns.

## Appearances in Sources

- [[dhar-1990-self-organized-critical-sandpile](pages/dhar-1990-self-organized-critical-sandpile.md)] - the count `det Δ` of recurrent configurations, tabulated here as `|K|` in both models; its logarithm `ln det Δ` is the entropy of the steady state, 0 for the 6,963 tree castles.
- [[dhar-ruelle-sen-verma-1995-algebraic-aspects](pages/dhar-ruelle-sen-verma-1995-algebraic-aspects.md)] - the number of cyclic factors of the square castles' sink groups and the exact sink group of the height-3 castles, through the open-boundary grids that are their duals.
- [[rossin-2000-group-of-a-sandpile](pages/rossin-2000-group-of-a-sandpile.md)] - the reference to Cori and Rossin's paper on the sandpile groups of dual graphs, and the group of the `2 × 2` grid, the dual of `(3, 3, 3)`.
- [[chau-cheng-1991-deterministic-soc-sandpile](pages/chau-cheng-1991-deterministic-soc-sandpile.md)] - completely deterministic steady states, a stronger property than a cyclic group.
- [[project-euler-502-castle-factoring](pages/project-euler-502-castle-factoring.md)] - the castle definition (column heights `≥ 1`) that makes the castles of `n` cells the compositions of `n`.

## Footnotes

[^1]: Verified by execution (Python 3.11, 2026-10-16): an integer Smith normal form routine agrees with `sympy.matrices.normalforms.smith_normal_form` on 300 random integer matrices; for all 33,150 castles with at most 16 cells, mirror images removed, the invariant factors of the block matrices equal those of the cell-side reduced Laplacian (bottom-left sink cell in the sink model; bottom row deleted, full degrees kept, in the tide model).
[^2]: Verified by execution (Python 3.11, NumPy, NetworkX 3.4, 2026-10-16): spectra rounded to 7 decimals, grouped by cell count, and split into isomorphism classes with `networkx.is_isomorphic`; the per-size counts of groups with at least two classes equal the table on [[isospectral-castles](pages/isospectral-castles.md)] at every `n ≤ 16`.
[^3]: Verified by execution (Python 3.11, 2026-10-16): for all 26,187 castles with at most 16 cells that have a `2 × 2` block, in both models (in the tide model, the cells above the bottom row and one vertex for the bottom row, each cell of row 2 joined to it), the cycle rank `|E| − |V| + 1` equals the number of blocks and the edges-by-blocks matrix of the block cycles has `r` invariant factors, all equal to 1.
[^4]: Verified by execution (Python 3.11, 2026-10-16): both groups from the block matrices for all 33,150 castles; the per-size counts of trivial, cyclic and distinct groups; the group frequencies and the smallest castle of each group; the castles with three cyclic factors and the largest groups, as stated; the trivial sets of the two models coincide. The trivial column, `(A005251(n+2) + A000931(n+6))/2`, and the palindromic tree castles `A000931(n+6)` recomputed for `n ≤ 16`; `A005683` checked on oeis.org.
[^5]: [[dhar-ruelle-sen-verma-1995-algebraic-aspects](pages/dhar-ruelle-sen-verma-1995-algebraic-aspects.md)] §4 p.12 eq. (4.7) (the number `g = L` of cyclic factors of the `L × L` grid, with "The idea of the proof") and Appendix A pp.32-33, eqs. (A8), (A16) and Table II (the `L × 2` strip: "d_1 = m_{L+1} n_{L+1}/d_2, d_2 = gcd(m_{L+1}, n_{L+1})", "One may note that m_x are precisely the even terms in the standard Fibonacci sequence", "The only result we could firmly establish follows from the double inequality (4.12): d_2 > 1 if L + 1 is divisible by 3, so in that case, G is not cyclic"). Verified by execution (Python 3.11, 2026-10-16): the formula equals the sink group of `(3,)*w` for `2 ≤ w ≤ 16`, with the non-cyclic widths as listed, and `|K_tide((2,)*w)| = F_{2w}`; `A004254` and `A001906` checked on oeis.org.
[^6]: Verified by execution (Python 3.11, NetworkX 3.4, 2026-10-16): cross-tabulating `K_tide` against `K_sink` over all 33,150 castles, each tide group in the table occurs with exactly one sink group, and the sink groups `Z/15` and `Z/56` split as `3,773 + 2,212` and `1,564 + 1,173 + 591`. Sorting the castles of each size into isomorphism classes of their graphs with `networkx.is_isomorphic`: 6,443 classes contain more than one castle, in 2,254 of them the tide groups are not all equal, and in none are the sink groups unequal; the first is `{(2, 2, 2), (3, 3)}`.
[^7]: Verified by execution (Python 3.11, NetworkX 3.4, 2026-10-16): in each of the 105 adjacency-cospectral and 17 Laplacian-cospectral groups to 16 cells, all castles have equal sink groups and isomorphic block graphs; 11 of the 17 Laplacian groups consist of tree castles only. For the tide group every skyline of every graph in each cospectral group was included; a group counts as separated when two skylines of different graphs have different tide groups: 23 adjacency-cospectral groups, the first at 10 cells, and no Laplacian-cospectral group.
[^8]: Verified by execution (Python 3.11, 2026-10-16): over the census, the condition "every cluster lies in one row" disagrees with sink cyclicity on 9,547 castles, the first `(3, 3)`; for every castle whose clusters are all paths, in both models, the group is cyclic exactly when the cluster orders are pairwise coprime; the counts and smallest castles in the table, and the groups of `(3, 3, 3)` and `(4, 4, 4)`, as stated.
