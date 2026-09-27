---
title: Sandpile census - every castle to 16 cells, in the sink and tide models
category: Analyses
summary: The sandpile group of every castle with at most 16 cells (33,150 castles, mirror images removed) in both models of sandpile-group - the sink model (one sink cell) and the tide model (the bottom row as the sink) - computed from the 2×2-block matrices and checked against the cospectral census of isospectral-castles. The 2×2 blocks' boundary cycles are an integer basis of the cycle lattice in every case tested (938 castles). In both models the trivial group occurs exactly on the 6,963 tree castles. Sink model - the commonest groups are Z/4 (one isolated block), Z/15 (two adjacent blocks), Z/56 and Z/209 (paths of three and four blocks); the group separates none of the 105 adjacency- and 17 Laplacian-cospectral groups, because cospectral castles always share their graph of blocks; the census refutes the "cyclic sandcastles" conjecture as stated, proves that every path-shaped cluster gives a cyclic group, and finds 921 castles with a non-path cluster and a cyclic group. Tide model - each sink group splits by how many blocks sit on the ground (Z/15 becomes Z/8 lying down or Z/11 standing up; Z/56 becomes Z/21, Z/29 or Z/41 as three, two or one of its blocks touch the ground), 2,254 of the 6,443 graphs realized by several skylines get different tide groups on different skylines, and the group is far more often cyclic (30,617 castles against 29,439): (3,3,3) is Z/95 under the tide but Z/8 × Z/24 in the sink model, while (4,4,4) goes the other way (Z/2415 against Z/13 × Z/91). The cyclic and distinct-group counts per cell count are OEIS novel candidates in both models.
tags: [analysis, castle, sandpile, critical-group, census, isospectral, laplacian, adjacency, smith-normal-form, cyclic-group, tree-castle, block-graph, sink-model, tide-model, numpy, sympy, verification]
sources: [project-euler-502-castle-factoring]
created: 2026-09-26
updated: 2026-09-26
---

# Sandpile census - every castle to 16 cells, in the sink and tide models

## The questions

This page answers questions about the sandpile group of a castle in both models of [[sandpile-group](pages/sandpile-group.md)]: `K_sink`, with one sink cell, and `K_tide`, with the whole bottom row as the sink.

1. Show that the `2 × 2` blocks give an integer basis of the castle's cycles.
2. Compute `K_sink` and `K_tide` for every castle up to 16 cells.
3. Find which isospectral pairs of [[isospectral-castles](pages/isospectral-castles.md)] the sink group separates, and the smallest pair with the same Laplacian spectrum but different sink groups.
4. Find what the tide group sees that the sink group does not.
5. Say which castles have a cyclic group, in each model.

Short answers: (1) yes, in every case tested; (2) done, 33,150 castles in each model; (3) none, and there is no such pair up to 16 cells, for a structural reason; (4) how high each block sits, so it tells apart castles with the same graph; (5) paths of blocks are cyclic in both models, and the tide model is cyclic far more often.

## Method

Each castle's groups are computed from its **block matrices**, one row per `2 × 2` block with `−1` for blocks sharing an edge. The diagonal is `4` for every block in the sink model, and `3` for a block on the ground and `4` above it in the tide model ([[sandpile-group](pages/sandpile-group.md)], Part 3, which proves the tide rule and checks it against the cell-side Laplacian on every castle to 16 cells). The group's structure comes from the Smith normal form, computed with a small integer routine that agrees with SymPy's on 400 random castles.[^1] For the spectra, castles are grouped by their rounded adjacency and Laplacian eigenvalues. Within a group, colour refinement (repeatedly relabelling each cell by its neighbours' labels) certifies that two castles are non-isomorphic. It reproduces the counts of [[isospectral-castles](pages/isospectral-castles.md)] exactly at every size (adjacency 2, 0, 10, 6, 18, 19, 50 and Laplacian 0, 1, 0, 2, 2, 5, 7 groups at 10 to 16 cells).[^2] The full run takes under a minute.

## 1. The 2×2 blocks are an integer basis of the cycles

Put the boundary loop of each `2 × 2` block as a column of the cycle matrix `C`. Its Smith normal form has every invariant factor equal to 1 on all 938 castles tested: every castle with blocks up to 11 cells, plus 300 random larger ones. So the block loops span the integer cycle lattice with no gaps: every integer cycle is an integer combination of block loops. With the rank count `cycle rank = number of blocks` from [[castle-graph](pages/castle-graph.md)], they are a basis.[^3] This is the sink model's cycle lattice; under the tide the ground blocks' loops become triangles through the ground, and the same blocks index the cycles.

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

The trivial column is the same in both models, because both groups are trivial exactly on tree castles ([[sandpile-group](pages/sandpile-group.md)], Part 3). It is OEIS A005683 term for term (`(A005251(n+2) + A000931(n+6))/2`, the palindromic tree castles being Padovan numbers). The cyclic and distinct-group columns match nothing in the OEIS in either model (searched 2026-09-26; [[castle-sequence-catalogue](pages/castle-sequence-catalogue.md)]).[^4]

### The commonest sink groups

The sink group depends only on how the blocks touch each other, so the third column is what to picture:[^4]

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

The path orders `4, 15, 56, 209, 780` are OEIS A001353, the 2-wide ladder sequence. The first non-cyclic groups appear at 9 cells: `(2, 2, 1, 2, 2)` with `Z/4 × Z/4`, and `(3, 3, 3)` with `Z/8 × Z/24`. At most three cyclic factors occur up to 16 cells, first at `(2, 2, 1, 2, 2, 1, 2, 2)` with `Z/4 × Z/4 × Z/4`. The largest group is `(4, 4, 4, 4)`'s `Z/4 × Z/112 × Z/224`, of order 100,352.

A **path of blocks** does not have to be straight. `(2, 2, 2, 2)` (three blocks in a row) and `(3, 3, 2)` (three blocks in an L) both give `Z/56`, because in both each block touches the next.

### The commonest tide groups

The tide group also records which blocks sit on the ground, so each sink group splits by how the blocks stand. Every row below comes from exactly one sink group:[^5]

| `K_tide` | castles (to 16 cells) | block arrangement | `K_sink` of the same castles | smallest castle |
|---|---|---|---|---|
| `Z/3` | 8,027 | one isolated block (always on the ground) | `Z/4` | `(2, 2)` |
| trivial | 6,963 | no blocks | trivial | `(1)` |
| `Z/8` | 3,773 | two blocks side by side, both on the ground | `Z/15` | `(2, 2, 2)` |
| `Z/11` | 2,212 | two blocks stacked, one on the ground | `Z/15` | `(3, 3)` |
| `Z/3 × Z/3` | 1,974 | two isolated blocks | `Z/4 × Z/4` | `(2, 2, 1, 2, 2)` |
| `Z/21` | 1,564 | three blocks in a row on the ground | `Z/56` | `(2, 2, 2, 2)` |
| `Z/29` | 1,173 | three blocks in an L, two on the ground | `Z/56` | `(2, 3, 3)` |
| `Z/24` | 1,043 | a pair on the ground plus an isolated block (`Z/8 × Z/3`) | `Z/60` | `(2, 2, 1, 2, 2, 2)` |
| `Z/41` | 591 | three blocks stacked, one on the ground | `Z/56` | `(4, 4)` |

A path of three blocks is `Z/56` in the sink model however it bends. Under the tide its order counts how many of its blocks touch the ground: 21 for three, 29 for two, 41 for one. The row of blocks lying down gives the even Fibonacci numbers `3, 8, 21, 55, 144` (A001906) and the column standing up gives `3, 11, 41, 153, 571` (A001835). The largest tide group to 16 cells is again `(4, 4, 4, 4)`'s, now cyclic, `Z/31529`. At most three cyclic factors occur, first at `(2, 2, 1, 2, 2, 1, 2, 2)` with `Z/3 × Z/3 × Z/3`.

## 3. What each group separates

**The sink group separates no cospectral pair.**

| cospectral groups (to 16 cells) | number | separated by `K_sink` |
|---|---|---|
| same adjacency spectrum | 105 | **0** |
| same Laplacian spectrum | 17 (11 of them all trees) | **0** |

The reason is visible in the data. In **every** one of the 122 cospectral groups, the castles have the **same graph of 2×2 blocks**. By [[sandpile-group](pages/sandpile-group.md)], the sink group is determined by that graph alone (it is `Z^r` modulo `4I − (block adjacency)`). So on these castles the sink group cannot see anything the spectrum does not.[^6] The 11-cell Laplacian pair of [[hear-the-shape-seminar](pages/hear-the-shape-seminar.md)] is two trees, both trivial, and the 10-cell adjacency pair has two adjacent blocks in both castles, both `Z/15`.

There is therefore no pair of castles with the same Laplacian spectrum and different sink groups up to 16 cells. Finding one would need two cospectral castles with different block graphs. None occur this small, and whether any exist at all is open.

**The tide group sees the skyline, not just the graph.** Up to 16 cells, 6,443 castle graphs (as far as colour refinement can tell) are realized by more than one skyline, and on 2,254 of them different skylines have different tide groups; the sink group never differs, since it depends only on the graph. The first example is the silver rectangle `(2, 2, 2)` (`Z/8`) against the tall pair `(3, 3)` (`Z/11`), the same `3 × 2` grid lying down and standing up.[^5]

For the same reason the tide group can split a cospectral group without hearing anything the spectrum misses. The 10-cell pair's own skylines `(1,1,1,2,3,2)` and `(1,1,2,2,3,1)` both have `K_tide = Z/8`, but `(1, 3, 5, 1)`, another skyline of the second graph, has `Z/11`. Counting a cospectral group as separated when two castles of different graphs have different tide groups, 23 of the 105 adjacency groups and none of the 17 Laplacian groups are separated to 16 cells.[^6] The question the tide model answers is about skylines: its group is a product over the castle's runs of raised columns, and it records how each run's blocks stand on the ground.

## 4. Cyclic sandcastles, in both models

**Sink model.** A natural guess is that `K_sink` is cyclic exactly when every cluster of blocks is a 2-wide ladder. The census refutes it. `(2, 2, 1, 2, 2)` has two 2-wide ladder clusters (single blocks) and group `Z/4 × Z/4`, which is not cyclic. Read with "ladder" as a horizontal row of blocks, it fails on 9,547 castles, starting with `(3, 3)`, a vertical 2-wide ladder with cyclic group `Z/15`.[^7]

What is true, in both models:

- **A path of blocks always gives a cyclic group.** The block matrix of a path is tridiagonal with `−1` beside the diagonal, whatever the diagonal entries are. Deleting its first row and last column leaves a triangular matrix with `−1` on the diagonal, of determinant `±1`. So the gcd of the `(r−1)`-minors is 1, and the group is cyclic. The census has no exceptions in either model.
- **Several clusters multiply.** A castle whose clusters are all paths has a cyclic group exactly when the clusters' orders are pairwise coprime. That is why two isolated blocks give `Z/4 × Z/4` (sink) or `Z/3 × Z/3` (tide), but a pair and a single block give `Z/15 × Z/4 = Z/60` (sink) or `Z/8 × Z/3 = Z/24` (tide).

Where the models differ is the non-path clusters:

| | sink model | tide model |
|---|---|---|
| castles with a non-path cluster and a cyclic group | 921, smallest `(2, 3, 3, 3)`, `Z/712` (11 cells) | 1,660, smallest `(3, 3, 3)`, `Z/95` (9 cells) |
| castles with one non-path cluster and a non-cyclic group | 837, smallest `(3, 3, 3)`, `Z/8 × Z/24` | 144, smallest `(2, 4, 4, 2)`, `Z/3 × Z/93` (12 cells) |
| cyclic in this model only | 168 castles, smallest `(2, 4, 4, 2)` (`Z/776` sink) | 1,346 castles, smallest `(3, 3, 3)` (`Z/95` tide) |

The ground's 3s break the symmetry that splits the sink group of the `2 × 2` square of blocks: `(3, 3, 3)` is `Z/8 × Z/24` in the sink model and `Z/95` under the tide. The effect also runs the other way. `(4, 4, 4)` is cyclic in the sink model (`Z/2415`) and splits under the tide (`Z/13 × Z/91`).[^7]

## What this settles and what it opens

**Settled (to 16 cells).**
- The block loops are an integer basis of the cycle lattice in every case tested.
- The census of both groups, with the tree castles (6,963, mirror images removed; [[tree-castle-by-area](pages/tree-castle-by-area.md)] counts them with mirrors kept) as the trivial ones in both models.
- Sink model: the group separates no cospectral pair, because cospectral castles always share their block graph.
- Tide model: each sink group splits by how many blocks touch the ground, and the tide group differs between skylines of the same graph on 2,254 of 6,443 graphs.
- Both models: path-shaped clusters give cyclic groups (proof above). The 2-wide-ladder guess for cyclicity is false in the sink model.

**Open.**
- Sink model: do two cospectral castles with different block graphs exist at any size? That is the only way the sink group could separate a cospectral pair. The spectrum already hears the number of blocks ([[hear-the-shape-seminar](pages/hear-the-shape-seminar.md)] Stop 2); the question is whether it hears how they touch.
- Sink model: which non-path clusters give cyclic groups? `(2, 3, 3, 3)` is cyclic and `(3, 3, 3)` is not.
- Tide model: which non-path clusters give cyclic groups under the tide? `(3, 3, 3)` is cyclic and `(4, 4, 4)` is not; the ground's 3s make cyclic groups much commoner, and a rule for when they do is open.
- Tide model: a closed form for the tide order of a run from how its blocks stand on the ground, generalizing the ladders (A001906 lying down, A001835 standing up).

The groups computed here feed the rest of the sandpile pages: the clock period is the order of one grain in the group ([[sandcastle-clock](pages/sandcastle-clock.md)]), the identity is its zero element ([[sandpile-identity](pages/sandpile-identity.md)]), and the random-dropping statistics use the same inverse reduced Laplacian ([[castle-avalanches](pages/castle-avalanches.md)]), each in both models.

## Snippet

A self-contained version of the census to 12 cells (2,142 castles, about two seconds). It reproduces the commonest groups in both models, the cospectral groups (12 adjacency and 1 Laplacian at this size), the finding that the sink group separates none, and the gallery values.

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

def wl_hash(c, rounds=8):                  # colour refinement: different hash => not isomorphic
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

- [[sandpile-group](pages/sandpile-group.md)] - the introduction: the game, the matrices, both models, and the block-matrix formulas this census uses.
- [[isospectral-castles](pages/isospectral-castles.md)] / [[hear-the-shape-seminar](pages/hear-the-shape-seminar.md)] - the cospectral groups tested here.
- [[castle-graph](pages/castle-graph.md)] - cycle rank as the number of 2×2 blocks, and tree castles.
- [[spectral-analysis](pages/spectral-analysis.md)] - the other castle spectra that might separate what the sink group cannot.
- [[sandcastle-clock](pages/sandcastle-clock.md)] - the clock spectrum, which separates cospectral castles the sink group cannot.
- [[sandpile-identity](pages/sandpile-identity.md)] - the avalanche profiles, one per model.
- [[sandcastle-seminar](pages/sandcastle-seminar.md)] - the Sandcastles seminar, following the 16-cell silver castle `(3,2,1,2,2,1,2,3)` through both models.
- [[castle-avalanches](pages/castle-avalanches.md)] - random dropping, which uses the same inverse reduced Laplacian.

## Appearances in Sources

- [[project-euler-502-castle-factoring](pages/project-euler-502-castle-factoring.md)] - the castle definition (column heights `≥ 1`) that makes "every castle with `n` cells" the compositions of `n`.

## Footnotes

[^1]: Verified by execution (Python 3.10, SymPy, 2026-09-26): a pure-Python Smith normal form by row and column operations returns the same nontrivial invariant factors as `sympy.matrices.normalforms.smith_normal_form` on the block matrices of 400 randomly chosen castles with at most 12 cells, and on the reduced Laplacians of 300 random castles to 16 cells in both models.
[^2]: Verified by execution (Python 3.10, NumPy, 2026-09-26): spectra rounded to 7 decimals, grouped by cell count, split by colour-refinement hash (8 rounds); the per-size counts of cospectral groups with at least two classes equal the table on [[isospectral-castles](pages/isospectral-castles.md)] (which used `networkx.is_isomorphic` and exact characteristic polynomials) at every `n ≤ 16`.
[^3]: Verified by execution (Python 3.10, SymPy, 2026-09-26): `smith_normal_form` of the edges-by-blocks cycle matrix `C` has all `r` invariant factors equal to 1 on every castle with blocks and at most 11 cells, and on 300 randomly chosen castles with 12 to 16 cells (938 castles in all).
[^4]: Verified by execution (Python 3.10, 2026-09-26): both groups from the block matrices for all 33,150 mirror-distinct castles with at most 16 cells; per-size counts of trivial, cyclic and distinct groups, the group frequencies, the smallest castle per group (by cell count, then lexicographically), and the extremes `(2,2,1,2,2,1,2,2)` and `(4,4,4,4)` in both models, as stated. The trivial sets of the two models coincide castle by castle. OEIS searched by terms on 2026-09-26: the trivial column matches A005683 through 26 cells; the two cyclic columns and the two distinct-group columns have no match. The 12-cell version is pinned in the Snippet.
[^5]: Verified by execution (Python 3.10, 2026-09-26): cross-tabulating `K_tide` against `K_sink` over all 33,150 castles, each tide group in the table occurs with exactly one sink group, and the sink groups `Z/15` and `Z/56` split as `3,773 + 2,212` and `1,564 + 1,173 + 591`. Castles grouped by cell count and colour-refinement hash: 6,443 hash classes hold more than one castle, and in 2,254 of them the castles' tide groups are not all equal (in none are their sink groups unequal); the first is `{(2,2,2), (3,3)}`.
[^6]: Verified by execution (Python 3.10, 2026-09-26): for each of the 105 adjacency and 17 Laplacian cospectral groups to 16 cells, all castles in the group have equal sink groups, and their block graphs (blocks as vertices, shared edges as edges) have equal colour-refinement hashes; 11 of the 17 Laplacian groups consist of tree castles only. For the tide group every skyline of every graph in each group was included; a group counts as separated when two castles from different colour-refinement classes have different tide groups: 23 adjacency groups (the first at 10 cells, through `(1,3,5,1)`) and 0 Laplacian groups.
[^7]: Verified by execution (Python 3.10, 2026-09-26): over the 16-cell census, "every block cluster lies in one row" disagrees with sink cyclicity on 9,547 castles (first `(3,3)`); no path-shaped cluster has a non-cyclic group in either model; "all clusters are paths with pairwise coprime orders" is sufficient for cyclicity in both models, and fails as a characterization on 921 castles (sink) and 1,660 castles (tide), all with a non-path cluster and a cyclic group, the smallest `(2,3,3,3)` (sink, `Z/712`) and `(3,3,3)` (tide, `Z/95`). Single non-path clusters with non-cyclic groups: 837 (sink, first `(3,3,3)`) and 144 (tide, first `(2,4,4,2)`, `Z/3 × Z/93`). Cyclic in one model only: 168 castles tide-non-cyclic but sink-cyclic (first `(2,4,4,2)`, `Z/776` sink), 1,346 sink-non-cyclic but tide-cyclic (first `(3,3,3)`); `(4,4,4)` is `Z/2415` (sink) and `Z/13 × Z/91` (tide).
