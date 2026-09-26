---
title: Hear the shape of a castle - seminar
category: Concepts
summary: The seminar walk-through for the "Hear the shape of a castle" arc - Kac's drum question asked of castles, organized as a list of what a spectrum can and cannot hear. A castle becomes a graph (cells, orthogonal neighbors); its adjacency and Laplacian eigenvalues are the "notes". Worked by hand on the golden path, the 4-cycle and the silver 3×2 rectangle, the spectrum hears the area, the number of edges and hence the number of 2×2 blocks, bipartiteness, and (Laplacian) connectivity and the number of spanning trees. It fails first at 10 cells - (1,1,1,2,3,2) and (1,1,2,2,3,1) share every adjacency eigenvalue, trace and spanning-tree count (15) but have different degree sequences, and the Laplacian hears the difference. The Laplacian fails first at 11 cells, on two trees with identical degree sequences, separated only by per-cell closed-walk counts at length 3. Both operators fail together at 16 cells. Schwenk (trees) and Sunada (covers) explain why; a Sunada cover for the 10-cell pair, Ihara zeta and the skyline DFT are open. One runnable block reproduces both smallest pairs by exhaustive search.
tags: [concept, castle, seminar, pedagogy, teaching, spectral, isospectral, adjacency, laplacian, kac, schwenk, sunada, trace-formula, matrix-tree-theorem, tree-castle, golden-ratio, silver-ratio]
sources: [project-euler-502-castle-factoring]
created: 2026-09-26
updated: 2026-09-26
---

# Hear the shape of a castle - seminar

**Thesis.** In 1966 Mark Kac asked whether you can hear the shape of a drum, that is, whether a membrane's vibration frequencies determine its shape. Ask the same of a castle: turn it into a graph and take its eigenvalues. The answer is a list. The spectrum hears the area, the number of edges, the number of `2 × 2` blocks and (with the Laplacian) the number of spanning trees. It first fails to hear the shape at **10 cells** for the adjacency spectrum, at **11 cells** for the Laplacian, and at **16 cells** for both at once. The seminar builds that list one stop at a time and ends on the two drawings.

**Format.** About 60 minutes at one blackboard, seven stops. Every value quoted is pinned by the Snippet block at the end, which also re-runs the exhaustive search for the smallest pairs. The research pages behind it are [[isospectral-castles](pages/isospectral-castles.md)] (the search through 16 cells), [[castle-graph](pages/castle-graph.md)], [[castle-graph-spectral-radius](pages/castle-graph-spectral-radius.md)] and the methods hub [[spectral-analysis](pages/spectral-analysis.md)]. [[castle-eigenvalues-by-example](pages/castle-eigenvalues-by-example.md)] is the slower from-scratch version of Stop 1.

## Stop 0 - a castle is a graph

A castle is a skyline of column heights `(c_1, …, c_w)`, each at least 1 ([[project-euler-502-castle-factoring](pages/project-euler-502-castle-factoring.md)]). Make it a graph: one vertex per filled cell, one edge per pair of cells that share a side ([[castle-graph](pages/castle-graph.md)]). Two matrices then carry "notes":

- the **adjacency matrix** `A`, with `A[u, v] = 1` for neighboring cells;
- the **Laplacian** `L = D − A`, where `D` holds each cell's number of neighbors (its degree).

Their eigenvalues are the castle's spectrum. **Hearing the shape** means that two castles with the same spectrum must have the same graph. (Mirror images count as the same castle.)

*Idea:* Kac's question needs only a matrix attached to a shape, so it can be asked of any combinatorial object.

## Stop 1 - three castles, heard by hand

| castle | graph | characteristic polynomial of `A` | loudest note (spectral radius) |
|---|---|---|---|
| `(1, 1, 1, 1)` | path on 4 cells | `(x² − x − 1)(x² + x − 1)` | `φ = (1 + √5)/2`, golden |
| `(2, 2)` | 4-cycle | `x²(x − 2)(x + 2)` | `2` |
| `(2, 2, 2)` | `3 × 2` grid | `(x − 1)(x + 1)(x² − 2x − 1)(x² + 2x − 1)` | `1 + √2`, silver |

The golden and silver ratios show up as the loudest notes of the smallest paths and rectangles ([[castle-graph-spectral-radius](pages/castle-graph-spectral-radius.md)]). Multiplied out, each polynomial has only even powers of `x` (`x⁴ − 3x² + 1`, `x⁴ − 4x²`, `x⁶ − 7x⁴ + 7x² − 1`), so every eigenvalue `λ` comes with `−λ`. That symmetry is the first thing you can hear.[^1]

*Idea:* compute small cases completely before asking general questions.

## Stop 2 - what the spectrum always hears

The **trace formula** makes this systematic. `trace(Aᵏ)` is the number of closed walks of length `k`, and it is the sum of the `k`-th powers of the eigenvalues, so equal spectra mean equal closed-walk counts at every length. Reading off small `k`:

- `k = 0`: the number of cells, so the **area**.
- `k = 2`: twice the number of **edges**. With the area this gives the cycle rank `|E| − |V| + 1`, which for a castle is exactly the number of filled **`2 × 2` blocks** ([[castle-graph](pages/castle-graph.md)]). You can hear how many `2 × 2` blocks a castle has.
- `k` odd: always 0, because the castle graph is **bipartite** (color cells like a chessboard). That is the `λ ↔ −λ` symmetry of Stop 1.

The Laplacian hears more:

- the number of zero eigenvalues is the number of **connected pieces** (1 for a castle);
- by Kirchhoff's matrix-tree theorem, the number of **spanning trees** is any cofactor of `L`, so it is determined by the spectrum. The 4-cycle `(2, 2)` has 4 spanning trees, the `3 × 2` grid has 15, and a tree castle has 1.[^1]

*Idea:* a spectrum is a list of numbers, and its power sums are counts of objects you can name.

## Stop 3 - the first failure: 10 cells, adjacency

Search every castle, smallest first, for two non-isomorphic castles with the same adjacency spectrum. The first hit is at **10 cells**:

```
A = (1,1,1,2,3,2)            B = (1,1,2,2,3,1)
....#.                       ....#.
...###                       ..###.
######                       ######
```

Both have characteristic polynomial `x¹⁰ − 11x⁸ + 34x⁶ − 36x⁴ + 12x²`. They agree on everything Stop 2 lists: area 10, 11 edges, two `2 × 2` blocks, the traces `22, 0, 106` of `A², A³, A⁴`, and even 15 spanning trees each. Yet they are different graphs. `A` has a cell with **four** neighbors (the second cell up in its tallest column, with filled cells left, right, above and below), while no cell of `B` has more than three:[^2]

```
degrees(A) = 4, 3, 3, 2, 2, 2, 2, 2, 1, 1
degrees(B) = 3, 3, 3, 3, 3, 2, 2, 1, 1, 1
```

**The adjacency spectrum cannot hear the degree sequence.** The Laplacian can tell these two apart: their Laplacian polynomials differ.

*Idea:* to show a spectrum misses something, find two objects that differ in it and agree in everything the spectrum hears.

## Stop 4 - the Laplacian's first failure: 11 cells, two trees

The Laplacian first fails at **11 cells**, on two **tree castles** (no `2 × 2` block, so no cycles):

```
S = (1,1,1,2,1,1,2,1,1)            T = (1,1,3,1,1,1,2,1)
...#..#..                          ..#.....
#########                          ..#...#.
                                   ########
```

Same Laplacian spectrum, the same degree sequence, and one spanning tree each. What differs is the branching. `S` has two single-cell spikes on a row of 9, and `T` has a two-cell spike and a single-cell spike on a row of 8. Even the per-cell counts of closed walks of length 2 agree. The first local statistic that separates them is the multiset of per-cell closed-walk counts at length 3, the diagonal of `L³`.[^3] [[levy-flights](pages/levy-flights.md)] finds the same separation in continuous time: local return probabilities at single cells tell the pair apart, although every global heat trace agrees.

*Idea:* global sums (traces) are spectral. Local diagonals are not, and they hear what the spectrum misses.

## Stop 5 - both at once: 16 cells

The first castles that share **both** the adjacency and the Laplacian spectrum have 16 cells, again a pair of trees, for example `(1,1,1,1,2,1,1,3,1,2,1,1)` and `(1,1,1,1,3,1,2,1,1,2,1,1)`. From 12 cells on, cospectral pairs are common: 50 adjacency groups at 16 cells alone ([[isospectral-castles](pages/isospectral-castles.md)], Results).

So the spectrum is a castle **invariant**, not a **classifier**. In the wiki's classification it is the Axis 9 data, which sorts castles but does not name them ([[castle-classification-spectrum](pages/castle-classification-spectrum.md)]).

## Stop 6 - why pairs exist

Two classical reasons cover every pair above ([[isospectral-castles](pages/isospectral-castles.md)], "Why cospectral pairs exist"):

- **Schwenk (1973): almost every tree has a cospectral mate.** The fraction of trees on `n` vertices with a non-isomorphic cospectral partner tends to 1. So the 11-cell Laplacian pair being two trees is the generic case, not bad luck.
- **Sunada (1985): covers and almost-conjugate subgroups.** Two quotients of one space by "almost conjugate" subgroups have the same spectrum. Gordon, Webb and Wolpert used this in 1992 to answer Kac with two planar drums. A Sunada-style explanation of the 10-cell pair would be a small graph covering both `A` and `B` with matching walk counts. **Nobody has written one down.**

*Idea:* an isospectral pair is a coincidence until a construction explains it. Schwenk explains the trees, and Sunada is the candidate for the pairs with cycles.

## Stop 7 - hearing more

Three ways to separate what the eigenvalues cannot, each an open thread in the S Department of `IDEAS.md`:

- **Local spectra** (Stop 4): diagonals of powers or of the heat kernel, cell by cell.
- **The Ihara zeta function**, which counts non-backtracking closed walks, a finer invariant than the spectrum for graphs with cycles ([[spectral-analysis](pages/spectral-analysis.md)] §5).
- **The skyline DFT**, the Fourier transform of the height sequence itself rather than of the graph ([[spectral-analysis](pages/spectral-analysis.md)] §3).

Whether Ihara or the DFT separates the 10-cell pair is not yet known.

## The board

| operator | hears | cannot hear | smallest failure |
|---|---|---|---|
| adjacency `A` | area, edges, number of `2 × 2` blocks, bipartite symmetry, spectral radius | degree sequence | 10 cells: `(1,1,1,2,3,2)` / `(1,1,2,2,3,1)` |
| Laplacian `L = D − A` | area, edges, connectivity, spanning trees, `Σ deg²` | branching of trees | 11 cells: `(1,1,1,2,1,1,2,1,1)` / `(1,1,3,1,1,1,2,1)` |
| both | all of the above | the shape | 16 cells: a pair of trees |
| per-cell walk counts (not spectral) | separates both small pairs | - | - |

## Snippet

One block reproduces every number above, including the two exhaustive searches (every castle of up to 11 cells, mirror images removed). Non-isomorphism is certified by colour refinement: two graphs with different refined colour histograms cannot be isomorphic. [[isospectral-castles](pages/isospectral-castles.md)] ran the full 16-cell search with an exact isomorphism test.

```python
import sympy as sp, numpy as np
from collections import defaultdict
x = sp.symbols('x')

def adj(c):                                # castle graph: filled cells, orthogonal neighbors
    cs = [(i, j) for i, h in enumerate(c) for j in range(h)]
    idx = {v: k for k, v in enumerate(cs)}
    A = sp.zeros(len(cs))
    for (i, j), u in idx.items():
        for nb in ((i+1, j), (i, j+1)):
            if nb in idx:
                A[u, idx[nb]] = A[idx[nb], u] = 1
    return A

def lap(c):                                # combinatorial Laplacian L = D - A
    A = adj(c)
    return sp.diag(*[sum(A.row(i)) for i in range(A.rows)]) - A

charpoly = lambda M: sp.expand(M.charpoly(x).as_expr())
degrees = lambda c: sorted((int(sum(adj(c).row(i))) for i in range(sum(c))), reverse=True)
spanning_trees = lambda c: lap(c)[1:, 1:].det()                  # Kirchhoff's matrix-tree theorem
local_walks = lambda M, k: sorted((M**k)[i, i] for i in range(M.rows))

def wl_hash(c, rounds=6):                  # colour refinement: different hash => not isomorphic
    A = adj(c); n = A.rows
    nb = [list(j for j in range(n) if A[i, j]) for i in range(n)]
    col = [len(v) for v in nb]
    for _ in range(rounds):
        col = [hash((col[i], tuple(sorted(col[j] for j in nb[i])))) for i in range(n)]
    return tuple(sorted(col))

def compositions(n):
    if n == 0:
        yield (); return
    for f in range(1, n+1):
        for r in compositions(n - f):
            yield (f,) + r

def smallest_pair(op):                     # first cell count with two non-isomorphic cospectral castles
    for n in range(1, 12):
        groups = defaultdict(list)
        for c in compositions(n):
            if c[::-1] < c:
                continue                   # mirror images are the same castle
            A = np.array(adj(c).tolist(), dtype=float)
            M = A if op == 'adjacency' else np.diag(A.sum(1)) - A
            groups[tuple(np.round(np.linalg.eigvalsh(M), 7))].append(c)
        for castles in groups.values():
            classes = {}
            for c in castles:
                classes.setdefault(wl_hash(c), c)
            if len(classes) >= 2:
                return n, list(classes.values())
```

```
>>> [sp.factor(charpoly(adj(c))) for c in [(1, 1, 1, 1), (2, 2), (2, 2, 2)]]
[(x**2 - x - 1)*(x**2 + x - 1), x**2*(x - 2)*(x + 2), (x - 1)*(x + 1)*(x**2 - 2*x - 1)*(x**2 + 2*x - 1)]
>>> spanning_trees((2, 2)), spanning_trees((2, 2, 2))
(4, 15)
>>> smallest_pair('adjacency')
(10, [(1, 1, 1, 2, 3, 2), (1, 1, 2, 2, 3, 1)])
>>> A, B = (1, 1, 1, 2, 3, 2), (1, 1, 2, 2, 3, 1)
>>> charpoly(adj(A)) == charpoly(adj(B)), charpoly(adj(A))
(True, x**10 - 11*x**8 + 34*x**6 - 36*x**4 + 12*x**2)
>>> [((adj(A)**k).trace(), (adj(B)**k).trace()) for k in (2, 3, 4)], (spanning_trees(A), spanning_trees(B))
([(22, 22), (0, 0), (106, 106)], (15, 15))
>>> degrees(A), degrees(B)
([4, 3, 3, 2, 2, 2, 2, 2, 1, 1], [3, 3, 3, 3, 3, 2, 2, 1, 1, 1])
>>> charpoly(lap(A)) == charpoly(lap(B))
False
>>> smallest_pair('laplacian')
(11, [(1, 1, 1, 2, 1, 1, 2, 1, 1), (1, 1, 3, 1, 1, 1, 2, 1)])
>>> S, T = (1, 1, 1, 2, 1, 1, 2, 1, 1), (1, 1, 3, 1, 1, 1, 2, 1)
>>> charpoly(lap(S)) == charpoly(lap(T)), degrees(S) == degrees(T), spanning_trees(S), spanning_trees(T)
(True, True, 1, 1)
>>> local_walks(lap(S), 2) == local_walks(lap(T), 2), local_walks(lap(S), 3) == local_walks(lap(T), 3)
(True, False)
```

## Exercises for the room

1. Find the degree-4 cell of `A = (1,1,1,2,3,2)` in the drawing, and check that no cell of `B` has four neighbors even though `B` has the same number of `2 × 2` blocks.
2. Explain from the chessboard coloring why `trace(A³) = 0` for every castle.
3. Count the spanning trees of `(2, 2)` by hand (4) and of `(2, 2, 2)` (15), and check them against `spanning_trees`.
4. Why must two Laplacian-cospectral castles have the same number of `2 × 2` blocks? (Use `trace(L)`.)
5. (Open.) Find a common cover, in Sunada's sense, for the 10-cell pair `A`, `B`.

## What is still open

These are the S-department items feeding Arc 4 in `IDEAS.md`:
- a Sunada-type construction for the 10-cell adjacency pair;
- whether the Ihara zeta function or the skyline DFT separates the cospectral pairs;
- the bronze spectral-radius hunt ([[castle-graph-spectral-radius](pages/castle-graph-spectral-radius.md)]: no castle among 4.87 million has spectral radius `(3 + √13)/2`);
- the LGV kernel spectrum ([[spectral-analysis](pages/spectral-analysis.md)] §2).

## Appearances in Sources

- [[project-euler-502-castle-factoring](pages/project-euler-502-castle-factoring.md)] - the castle definition (column heights `≥ 1`) that makes "every castle with `n` cells" a finite list.

## Related Concepts

- [[isospectral-castles](pages/isospectral-castles.md)] - the exhaustive search through 16 cells; this page is its classroom version.
- [[castle-graph](pages/castle-graph.md)] - the graph, its invariants, and tree castles.
- [[castle-graph-spectral-radius](pages/castle-graph-spectral-radius.md)] - golden and silver castles, and the loudest-note census.
- [[castle-eigenvalues-by-example](pages/castle-eigenvalues-by-example.md)] - the slower from-scratch version of Stop 1.
- [[spectral-analysis](pages/spectral-analysis.md)] - the five spectra of a castle and the open separators.
- [[levy-flights](pages/levy-flights.md)] - local return probabilities that separate the 11-cell pair.
- [[castle-classification-spectrum](pages/castle-classification-spectrum.md)] - Axis 9, where the spectrum is an invariant.
- [[hardin-identity-seminar](pages/hardin-identity-seminar.md)] / [[castle-fibers-char-2-walkthrough](pages/castle-fibers-char-2-walkthrough.md)] / [[tower-recursion-master-class](pages/tower-recursion-master-class.md)] - the other seminar pages.
- [[oeis-mining-seminar](pages/oeis-mining-seminar.md)] - the seminar on OEIS mining as a research method.
- [[one-bit-seminar](pages/one-bit-seminar.md)] - the seminar on the parity clause as information.
- [[sandpile-group](pages/sandpile-group.md)] - the sandpile group, a finer relative of the Laplacian spectrum; it does not separate the 10- or 11-cell pairs.


## Footnotes

[^1]: Verified by execution (Python 3.10, SymPy, 2026-09-26): the three factored characteristic polynomials and the spanning-tree counts `4` and `15` are pinned in the Snippet (`spanning_trees` is the `(1,1)` cofactor of `L`).
[^2]: Verified by execution (Python 3.10, SymPy, NumPy, 2026-09-26): `smallest_pair('adjacency')` returns the 10-cell pair as the first cospectral non-isomorphic pair (every composition of `n ≤ 10`, mirror images removed, spectra rounded to 7 places and confirmed by exact characteristic polynomials for the pair); traces `22, 0, 106`, spanning trees `15, 15`, the degree sequences, and unequal Laplacian polynomials as pinned. The 10-cell count agrees with the networkx-certified search on [[isospectral-castles](pages/isospectral-castles.md)].
[^3]: Verified by execution (Python 3.10, SymPy, NumPy, 2026-09-26): `smallest_pair('laplacian')` returns the 11-cell tree pair; equal Laplacian polynomials, equal degree sequences, one spanning tree each, equal sorted diagonals of `L²`, and unequal sorted diagonals of `L³`, as pinned.
