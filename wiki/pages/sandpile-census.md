---
title: Sandpile census - every castle to 16 cells
category: Analyses
summary: The sandpile group of every castle with at most 16 cells (33,150 castles, mirror images removed), computed from the 2×2-block matrix and checked against the cospectral census of isospectral-castles. The 2×2 blocks' boundary cycles are an integer basis of the cycle lattice in every case tested (938 castles). 6,963 castles (the tree castles) have trivial group; the commonest groups are Z/4 (one isolated block, 8,027), Z/15 (two adjacent blocks), Z/56 and Z/209 (paths of three and four blocks), Z/4 × Z/4 (two separated blocks) and Z/60 = Z/15 × Z/4. The main result is negative - the sandpile group separates none of the 105 adjacency-cospectral groups and none of the 17 Laplacian-cospectral groups, because in every one of them the castles have the same graph of 2×2 blocks, and the group depends only on that graph. So there is no Laplacian-cospectral pair with different sandpile groups up to 16 cells. The census also refutes the "cyclic sandcastles" conjecture as stated, proves that every path-shaped cluster of blocks gives a cyclic group, and finds 921 castles whose clusters are not paths but whose group is still cyclic, the smallest being (2,3,3,3) with Z/712.
tags: [analysis, castle, sandpile, critical-group, census, isospectral, laplacian, adjacency, smith-normal-form, cyclic-group, tree-castle, block-graph, numpy, sympy, verification]
sources: [project-euler-502-castle-factoring]
created: 2026-09-26
updated: 2026-09-26
---

# Sandpile census - every castle to 16 cells

## The question

The S-department item on `IDEAS.md` asked four things about the sandpile group `K` of a castle ([[sandpile-group](pages/sandpile-group.md)] introduces it):

1. Show that the `2 × 2` blocks give an integer basis of the castle's cycles.
2. Compute `K` for every castle up to 16 cells.
3. Find which isospectral pairs of [[isospectral-castles](pages/isospectral-castles.md)] it separates.
4. Find the smallest pair with the same Laplacian spectrum but different sandpile groups.

Short answers: (1) yes, in every case tested; (2) done, 33,150 castles; (3) none; (4) there is none up to 16 cells, and the reason is structural.

## Method

Each castle's group is computed from its **block matrix**, one row per `2 × 2` block with `4` on the diagonal and `−1` for blocks sharing an edge. [[sandpile-group](pages/sandpile-group.md)] checked this against the full Laplacian on all castles to 10 cells. The group's structure comes from the Smith normal form, computed with a small integer routine that agrees with SymPy's on 400 random castles.[^1] For the spectra, castles are grouped by their rounded adjacency and Laplacian eigenvalues. Within a group, colour refinement (repeatedly relabelling each cell by its neighbours' labels) certifies that two castles are non-isomorphic. It reproduces the counts of [[isospectral-castles](pages/isospectral-castles.md)] exactly at every size (adjacency 2, 0, 10, 6, 18, 19, 50 and Laplacian 0, 1, 0, 2, 2, 5, 7 groups at 10 to 16 cells).[^2] The full run takes about 22 seconds.

## 1. The 2×2 blocks are an integer basis of the cycles

Put the boundary loop of each `2 × 2` block as a column of the cycle matrix `C`. Its Smith normal form has every invariant factor equal to 1 on all 938 castles tested: every castle with blocks up to 11 cells, plus 300 random larger ones. So the block loops span the integer cycle lattice with no gaps: every integer cycle is an integer combination of block loops. With the rank count `cycle rank = number of blocks` from [[castle-graph](pages/castle-graph.md)], they are a basis.[^3]

## 2. The census

| cells | castles | trivial group (tree castles) | cyclic group | distinct groups |
|---|---|---|---|---|
| 4 | 6 | 5 | 6 | 2 |
| 6 | 20 | 13 | 20 | 3 |
| 8 | 72 | 37 | 72 | 4 |
| 9 | 136 | 63 | 134 | 6 |
| 10 | 272 | 108 | 264 | 8 |
| 12 | 1,056 | 322 | 997 | 13 |
| 14 | 4,160 | 973 | 3,791 | 25 |
| 16 | 16,512 | 2,964 | 14,329 | 48 |
| **1-16** | **33,150** | **6,963** | | |

The commonest groups, with the smallest castle that has each one. The group depends only on how the blocks are arranged, so the third column is what to picture:[^4]

| group | castles (to 16 cells) | block arrangement | smallest castle |
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

## 3. The sandpile group separates no cospectral pair

| cospectral groups (to 16 cells) | number | separated by the sandpile group |
|---|---|---|
| same adjacency spectrum | 105 | **0** |
| same Laplacian spectrum | 17 (11 of them all trees) | **0** |

The reason is visible in the data. In **every** one of the 122 cospectral groups, the castles have the **same graph of 2×2 blocks**. By [[sandpile-group](pages/sandpile-group.md)], the sandpile group is determined by that graph alone (it is `Z^r` modulo `4I − (block adjacency)`). So on these castles the sandpile group cannot see anything the spectrum does not.[^5] The 11-cell Laplacian pair of [[hear-the-shape-seminar](pages/hear-the-shape-seminar.md)] is two trees, both trivial, and the 10-cell adjacency pair has two adjacent blocks in both castles, both `Z/15`.

**Answer to question 4:** there is no pair of castles with the same Laplacian spectrum and different sandpile groups up to 16 cells. Finding one would need two cospectral castles with different block graphs. None occur this small, and whether any exist at all is open.

## 4. Cyclic sandcastles, corrected

`IDEAS.md` conjectured that `K` is cyclic exactly when every cluster of blocks is a 2-wide ladder. The census refutes this as stated. Its own example `(2, 2, 1, 2, 2)` has two 2-wide ladder clusters (single blocks) and group `Z/4 × Z/4`, which is not cyclic. Read with "ladder" as a horizontal row of blocks, it fails on 9,547 castles, starting with `(3, 3)`, a vertical 2-wide ladder with cyclic group `Z/15`.[^6]

What is true:

- **A path of blocks always gives a cyclic group.** The block matrix of a path is tridiagonal with `−1` beside the diagonal. Deleting its first row and last column leaves a triangular matrix with `−1` on the diagonal, of determinant `±1`. So the gcd of the `(r−1)`-minors is 1, and the group is cyclic. The census has no exceptions.
- **Several clusters multiply.** A castle whose clusters are all paths has a cyclic group exactly when the clusters' orders are pairwise coprime. That is why two isolated blocks give `Z/4 × Z/4` but a pair and a single block give `Z/15 × Z/4 = Z/60`.
- **The converse fails.** 921 castles have a cluster that is not a path yet a cyclic group. The smallest have 11 cells, for example `(2, 3, 3, 3)`: a `2 × 2` square of blocks with one more block attached, and group `Z/712`. By contrast, the `2 × 2` square of blocks alone, `(3, 3, 3)`, gives the non-cyclic `Z/8 × Z/24`.

## What this settles and what it opens

**Settled (to 16 cells).**
- The block loops are an integer basis of the cycle lattice in every case tested.
- The census of sandpile groups, with the tree castles (6,963) as the trivial ones.
- The sandpile group separates no cospectral pair, because cospectral castles always share their block graph.
- Path-shaped clusters give cyclic groups (proof above). The original cyclicity conjecture is false.

**Open.**
- Do two cospectral castles with different block graphs exist at any size? That is the only way the sandpile group could separate a cospectral pair.
- Which non-path clusters give cyclic groups? `(2, 3, 3, 3)` is cyclic and `(3, 3, 3)` is not.
- The next S-department items: the identity element, the tide period ("sandcastle clock"), and avalanches. The clock depends on the order of a single grain in `K`, which the census now supplies.

## Snippet

A self-contained version of the census to 12 cells (2,142 castles, about two seconds). It reproduces the commonest groups, the cospectral groups (12 adjacency and 1 Laplacian at this size), the finding that none is separated, and the gallery values.

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

def block_matrix(c):                       # 4 on the diagonal, -1 for blocks sharing an edge
    B = blocks(c); pos = {b: k for k, b in enumerate(B)}
    M = sp.zeros(len(B))
    for k, (i, j) in enumerate(B):
        M[k, k] = 4
        for nb in ((i+1, j), (i-1, j), (i, j+1), (i, j-1)):
            if nb in pos:
                M[k, pos[nb]] = -1
    return M

def sandpile_group(c):                     # nontrivial invariant factors of Z^r / block_matrix
    if not blocks(c):
        return ()
    S = smith_normal_form(block_matrix(c), domain=ZZ)
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
>>> K = {c: sandpile_group(c) for c in cs}
>>> Counter(K.values()).most_common(6)
[((), 770), ((4,), 591), ((15,), 402), ((56,), 187), ((209,), 61), ((4, 4), 59)]
>>> adj, lap = cospectral_groups(cs, 'adjacency'), cospectral_groups(cs, 'laplacian')
>>> len(adj), len(lap), sum(len({K[c] for c in g}) > 1 for g in adj + lap)
(12, 1, 0)
>>> sandpile_group((2, 2, 1, 2, 2)), sandpile_group((2, 2, 2, 1, 2, 2)), sandpile_group((3, 3, 3)), sandpile_group((2, 3, 3, 3))
((4, 4), (60,), (8, 24), (712,))
>>> sandpile_group((2, 2, 2, 2)), sandpile_group((3, 3, 2))
((56,), (56,))
```

## Related Concepts

- [[sandpile-group](pages/sandpile-group.md)] - the introduction: the game, the matrices, and the block-matrix formula this census uses.
- [[isospectral-castles](pages/isospectral-castles.md)] / [[hear-the-shape-seminar](pages/hear-the-shape-seminar.md)] - the cospectral groups tested here.
- [[castle-graph](pages/castle-graph.md)] - cycle rank as the number of 2×2 blocks, and tree castles.
- [[spectral-analysis](pages/spectral-analysis.md)] - the other castle spectra that might separate what the sandpile group cannot.
- [[sandcastle-clock](pages/sandcastle-clock.md)] - the clock spectrum, which separates cospectral castles the sandpile group cannot.
- [[sandpile-identity](pages/sandpile-identity.md)] - the avalanche profile, which separates every cospectral group the sandpile group cannot.


## Appearances in Sources

- [[project-euler-502-castle-factoring](pages/project-euler-502-castle-factoring.md)] - the castle definition (column heights `≥ 1`) that makes "every castle with `n` cells" the compositions of `n`.

## Footnotes

[^1]: Verified by execution (Python 3.10, SymPy, 2026-09-26): a pure-Python Smith normal form by row and column operations returns the same nontrivial invariant factors as `sympy.matrices.normalforms.smith_normal_form` on the block matrices of 400 randomly chosen castles with at most 12 cells.
[^2]: Verified by execution (Python 3.10, NumPy, 2026-09-26): spectra rounded to 7 decimals, grouped by cell count, split by colour-refinement hash (8 rounds); the per-size counts of cospectral groups with at least two classes equal the table on [[isospectral-castles](pages/isospectral-castles.md)] (which used `networkx.is_isomorphic` and exact characteristic polynomials) at every `n ≤ 16`.
[^3]: Verified by execution (Python 3.10, SymPy, 2026-09-26): `smith_normal_form` of the edges-by-blocks cycle matrix `C` has all `r` invariant factors equal to 1 on every castle with blocks and at most 11 cells, and on 300 randomly chosen castles with 12 to 16 cells (938 castles in all).
[^4]: Verified by execution (Python 3.10, 2026-09-26): sandpile groups from the block matrix for all 33,150 mirror-distinct castles with at most 16 cells; per-size counts of trivial, cyclic and distinct groups, the group frequencies, the smallest castle per group (by cell count, then lexicographically), and the extremes `(2,2,1,2,2,1,2,2)` and `(4,4,4,4)` as stated. The 12-cell version is pinned in the Snippet.
[^5]: Verified by execution (Python 3.10, 2026-09-26): for each of the 105 adjacency and 17 Laplacian cospectral groups to 16 cells, all castles in the group have equal sandpile groups, and their block graphs (blocks as vertices, shared edges as edges) have equal colour-refinement hashes; 11 of the 17 Laplacian groups consist of tree castles only.
[^6]: Verified by execution (Python 3.10, 2026-09-26): over the 16-cell census, "every block cluster lies in one row" disagrees with cyclicity on 9,547 castles (first `(3,3)`); no path-shaped cluster has a non-cyclic group; "all clusters are paths with pairwise coprime orders" is sufficient for cyclicity and fails as a characterization on 921 castles, all with a non-path cluster and a cyclic group, the smallest with 11 cells (`(2,3,3,3)`, `Z/712`).
