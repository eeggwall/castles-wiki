---
title: Hear the shape of a castle - seminar
category: Concepts
summary: A seminar on Kac's drum question asked of castles, organized as a list of what a spectrum determines and what it does not. A castle becomes a graph, its cells joined when they share a side, with an adjacency and a Laplacian spectrum. Worked by hand on the 4-cell path (golden by spectrum), the 4-cycle and the 3 × 2 rectangle (silver by spectrum), the spectrum determines the number of cells, the number of edges and hence of filled 2 × 2 squares, bipartiteness, and (Laplacian) connectivity and the number of spanning trees. It first fails at 10 cells, where (1,1,1,2,3,2) and (1,1,2,2,3,1) share every adjacency eigenvalue and 15 spanning trees but have different degree sequences, which the Laplacian detects. The Laplacian first fails at 11 cells, on two tree castles with the same degree sequence that the diagonal of L³ separates, and both fail together at 16 cells. The Ihara zeta function separates neither smallest pair, since it depends only on the 2-core; the skyline DFT and the sink-model sandpile clock separate the 10-cell pair. One snippet reproduces both smallest pairs by exhaustive search.
tags: [concept, castle, seminar, pedagogy, teaching, spectral, isospectral, adjacency, laplacian, kac, schwenk, sunada, trace-formula, matrix-tree-theorem, tree-castle, golden-ratio, silver-ratio]
sources: [project-euler-502-castle-factoring]
created: 2026-09-26
updated: 2026-10-16
---

# Hear the shape of a castle - seminar

**Thesis.** Kac asked whether the frequencies of a drum, the eigenvalues of the Laplace operator on a plane domain, determine its shape, and Gordon, Webb and Wolpert showed in 1992 that they do not.[^4] Ask the same of a castle: turn it into a graph and take its eigenvalues. The answer is a list. The spectrum determines the number of cells, the number of edges, the number of filled `2 × 2` squares and, for the Laplacian, the number of spanning trees. It first fails to determine the castle graph at **10 cells** for the adjacency spectrum, at **11 cells** for the Laplacian, and at **16 cells** for both at once.

**Structure.** Eight stops, 0 to 7. The Snippet at the end prints every value quoted and reruns the exhaustive search for the smallest pairs. The research pages behind it are [[isospectral-castles](pages/isospectral-castles.md)] (the search through 16 cells), [[castle-graph](pages/castle-graph.md)], [[castle-graph-spectral-radius](pages/castle-graph-spectral-radius.md)] and [[spectral-analysis](pages/spectral-analysis.md)]. [[castle-eigenvalues-by-example](pages/castle-eigenvalues-by-example.md)] works Stop 1 more slowly.

## Stop 0 - a castle is a graph

A castle is a skyline of column heights `(c_1, …, c_w)`, each at least 1 ([[project-euler-502-castle-factoring](pages/project-euler-502-castle-factoring.md)]). Its castle graph has one vertex per cell and one edge per pair of cells that share a side ([[castle-graph](pages/castle-graph.md)]). Two matrices are attached to it:

- the **adjacency matrix** `A`, with `A[u, v] = 1` for neighboring cells;
- the **Laplacian** `L = D − A`, where `D` holds each cell's number of neighbors, its degree.

Their eigenvalues are the castle's spectra. A spectrum **hears the shape** when two castles with the same spectrum always have isomorphic graphs. Mirror images count as the same castle.

*Idea:* Kac's question needs only a matrix attached to a shape, so it can be asked of any combinatorial object.

## Stop 1 - three spectra by hand

| castle | graph | characteristic polynomial of `A` | spectral radius |
|---|---|---|---|
| `(1, 1, 1, 1)` | path on 4 cells | `(x² − x − 1)(x² + x − 1)` | `φ = (1 + √5)/2`: golden by spectrum |
| `(2, 2)` | 4-cycle | `x²(x − 2)(x + 2)` | `2` |
| `(2, 2, 2)` | `3 × 2` rectangle | `(x − 1)(x + 1)(x² − 2x − 1)(x² + 2x − 1)` | `1 + √2`: silver by spectrum |

A castle is golden by spectrum when its castle graph has spectral radius `φ`, and silver by spectrum at `1 + √2` ([[castle-graph-spectral-radius](pages/castle-graph-spectral-radius.md)]). Multiplied out, each polynomial has only even powers of `x` (`x⁴ − 3x² + 1`, `x⁴ − 4x²`, `x⁶ − 7x⁴ + 7x² − 1`), so every eigenvalue `λ` comes with `−λ`; Stop 2 shows this holds for every castle.[^1]

*Idea:* compute small cases completely before asking general questions.

## Stop 2 - what the spectrum always determines

The **trace formula** makes this systematic. `trace(Aᵏ)` counts the closed walks of length `k`, and it is the sum of the `k`-th powers of the eigenvalues, so equal spectra mean equal numbers of closed walks of every length. For small `k`:

- `k = 0`: the number of cells.
- `k = 2`: twice the number of **edges**. With the number of cells this gives the cycle rank `|E| − |V| + 1`, which for a castle is the number of filled **`2 × 2` squares** ([[castle-graph](pages/castle-graph.md)]). The spectrum hears how many `2 × 2` squares a castle has.
- `k` odd: always 0, because the castle graph is **bipartite**: coloring the cells like a chessboard gives neighboring cells opposite colors. That is the `λ ↔ −λ` symmetry of Stop 1.

The Laplacian determines more:

- the multiplicity of the eigenvalue 0 is the number of **connected components**, 1 for a castle (Brouwer and Haemers, Proposition 1.3.7);
- by the matrix-tree theorem the number of **spanning trees** is any cofactor of `L` (Proposition 1.3.4), so it is determined by the spectrum.[^5] The 4-cycle `(2, 2)` has 4 spanning trees, the `3 × 2` rectangle has 15, and a tree castle has 1.[^1] The number of spanning trees is also the order of the castle's sandpile group in the sink model ([[sandpile-group](pages/sandpile-group.md)]).

*Idea:* a spectrum is a list of numbers, and its power sums count objects that can be named.

## Stop 3 - the first failure: 10 cells, adjacency

Search every castle, smallest first, for two non-isomorphic castle graphs with the same adjacency spectrum. The first pair has **10 cells**:

```
A = (1,1,1,2,3,2)            B = (1,1,2,2,3,1)
....#.                       ....#.
...###                       ..###.
######                       ######
```

Both have characteristic polynomial `x¹⁰ − 11x⁸ + 34x⁶ − 36x⁴ + 12x²`. They agree on everything in Stop 2: 10 cells, 11 edges, two `2 × 2` squares, the traces `22, 0, 106` of `A², A³, A⁴`, and 15 spanning trees each, so both have the sandpile group `Z/15` in the sink model ([[sandpile-census](pages/sandpile-census.md)]). Yet the graphs differ. `A` has a cell with **four** neighbors, the second cell of its tallest column, with filled cells to the left, right, above and below, while no cell of `B` has more than three:[^2]

```
degrees(A) = 4, 3, 3, 2, 2, 2, 2, 2, 1, 1
degrees(B) = 3, 3, 3, 3, 3, 2, 2, 1, 1, 1
```

**The adjacency spectrum does not determine the degree sequence.** The Laplacian separates these two: their Laplacian polynomials differ.

*Idea:* to show that a spectrum misses something, find two objects that differ in it and agree in everything the spectrum determines.

## Stop 4 - the Laplacian's first failure: 11 cells, two trees

The Laplacian first fails at **11 cells**, on two **tree castles**, castles with no filled `2 × 2` square, whose graphs have no cycles:

```
S = (1,1,1,2,1,1,2,1,1)            T = (1,1,3,1,1,1,2,1)
...#..#..                          ..#.....
#########                          ..#...#.
                                   ########
```

They have the same Laplacian spectrum, the same degree sequence, and one spanning tree each. `S` has two single-cell spikes on a row of 9 cells, and `T` has a two-cell spike and a single-cell spike on a row of 8. The diagonals of `L` and `L²` agree as multisets, since the diagonal entries are `d_v` and `d_v(d_v + 1)` and the degree sequences agree; the diagonal of `L³` is the first that differs.[^3] [[levy-flights](pages/levy-flights.md)] separates the pair in continuous time: the local return probabilities of the fractional walk (`0 < α ≤ 1`) at single cells differ, while every heat trace, a function of the spectrum, agrees.

*Idea:* traces are spectral and diagonals are not; the diagonals separate what the spectrum misses.

## Stop 5 - both at once: 16 cells

The first castles with **both** the same adjacency and the same Laplacian spectrum have 16 cells, again two tree castles, for example `(1,1,1,1,2,1,1,3,1,2,1,1)` and `(1,1,1,1,3,1,2,1,1,2,1,1)`. From 12 cells on, cospectral pairs are common: there are 50 adjacency groups at 16 cells alone ([[isospectral-castles](pages/isospectral-castles.md)], section *Results*). So the spectrum is an invariant of the castle that does not determine it, one of the spectral types of [[castle-classification-spectrum](pages/castle-classification-spectrum.md)].

## Stop 6 - why pairs exist

Two theorems explain why cospectral graphs are common ([[isospectral-castles](pages/isospectral-castles.md)], section *Why cospectral graphs exist*):

- **Schwenk: most trees have a cospectral mate.** The proportion of trees on `n` vertices determined by their adjacency spectrum tends to 0, and McKay showed that the cospectral mates can be chosen with cospectral line graphs, which for trees means the same Laplacian spectrum.[^6]
- **Sunada: almost conjugate subgroups.** If a finite group `G` acts by isometries on a manifold and two subgroups `H`, `K` act freely and are almost conjugate, with a bijection `H → K` that sends each element to a conjugate, then the quotients by `H` and by `K` are isospectral. Gordon, Webb and Wolpert answered Kac with an extension of this theorem.[^4]

*Idea:* these theorems show that cospectral pairs are common among trees and manifolds; they do not say which castles form the pairs.

## Stop 7 - separating more

Ways to separate what the eigenvalues do not:

- **Diagonals** (Stop 4): the diagonals of powers of `L`, or of a heat kernel, cell by cell.
- **The skyline DFT**, the Fourier transform of the sequence of column heights, rather than of the graph ([[spectral-analysis](pages/spectral-analysis.md)], section 3). It is invertible, so it separates every pair; even its magnitudes differ on the 10-cell pair (`10, 3, 1, 0, 1, 3` against `10, 2.65, 1, 2, 1, 2.65`).[^3]
- **Sandpiles** in the sink model, with one sink cell. The sink sandpile group depends only on the graph of `2 × 2` squares, which cospectral castles in the census always share, but the sink clock ticks 15 and 5 on the 10-cell pair and its clock spectrum separates 62 of the 105 adjacency groups and 5 of the 17 Laplacian groups through 16 cells ([[sandcastle-clock](pages/sandcastle-clock.md)]), and the avalanche profile separates all of them ([[sandpile-identity](pages/sandpile-identity.md)]).

The **Ihara zeta function**, which counts closed walks without backtracking and without tails ([[spectral-analysis](pages/spectral-analysis.md)], section 5), separates neither smallest pair. Such a walk never enters a pendant tree, so the zeta function depends only on the 2-core, the subgraph left after repeatedly deleting cells with one neighbor. The 2-core of both 10-cell castles is the `3 × 2` rectangle, and a tree castle has zeta function 1.[^3]

## Summary table

| invariant | determines | does not determine | smallest failure |
|---|---|---|---|
| adjacency spectrum | cells, edges, number of `2 × 2` squares, bipartite symmetry, spectral radius | degree sequence | 10 cells: `(1,1,1,2,3,2)` and `(1,1,2,2,3,1)` |
| Laplacian spectrum | cells, edges, connectivity, spanning trees, `Σ d_v²` | how the branches of a tree sit | 11 cells: `(1,1,1,2,1,1,2,1,1)` and `(1,1,3,1,1,1,2,1)` |
| both spectra | everything either spectrum determines | the castle graph | 16 cells: two tree castles |
| Ihara zeta function | the 2-core | anything outside the 2-core | separates neither the 10-cell nor the 11-cell pair |
| diagonals of `Lᵏ` (not spectral) | separate both smallest pairs | - | - |
| sink clock spectrum (not spectral) | separates 62 of 105 adjacency and 5 of 17 Laplacian groups through 16 cells | tree castles (trivial group) | - |
| sink avalanche profile (not spectral) | separates every cospectral group through 16 cells | none found | - |

## Snippet

One block reproduces every number on this page, including the two exhaustive searches over every castle with at most 11 cells, mirror images removed. Non-isomorphism is certified by color refinement: two graphs with different refined color histograms are not isomorphic. [[isospectral-castles](pages/isospectral-castles.md)] runs the 16-cell search with an exact isomorphism test.

```python
import sympy as sp, numpy as np
from collections import defaultdict
x = sp.symbols('x')

def adj(c):                                # castle graph: cells, edges between cells that share a side
    cs = [(i, j) for i, h in enumerate(c) for j in range(h)]
    idx = {v: k for k, v in enumerate(cs)}
    A = sp.zeros(len(cs))
    for (i, j), u in idx.items():
        for nb in ((i+1, j), (i, j+1)):
            if nb in idx:
                A[u, idx[nb]] = A[idx[nb], u] = 1
    return A

def lap(c):                                # Laplacian L = D - A
    A = adj(c)
    return sp.diag(*[sum(A.row(i)) for i in range(A.rows)]) - A

charpoly = lambda M: sp.expand(M.charpoly(x).as_expr())
degrees = lambda c: sorted((int(sum(adj(c).row(i))) for i in range(sum(c))), reverse=True)
spanning_trees = lambda c: lap(c)[1:, 1:].det()                  # the matrix-tree theorem
local_walks = lambda M, k: sorted((M**k)[i, i] for i in range(M.rows))

def wl_hash(c, rounds=6):                  # color refinement: different hash => not isomorphic
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

## Exercises

1. Find the cell with four neighbors in `A = (1,1,1,2,3,2)`, and check that no cell of `B = (1,1,2,2,3,1)` has four neighbors although `B` has the same number of `2 × 2` squares.
2. Explain from the chessboard coloring why `trace(A³) = 0` for every castle.
3. Count the spanning trees of `(2, 2)` (4) and of `(2, 2, 2)` (15) by hand, and check them against `spanning_trees`.
4. Why do two Laplacian-cospectral castles have the same number of `2 × 2` squares? (Use `trace(L)`.)
5. Delete the cells with one neighbor from `A` and from `B` until none is left, and check that both leave the `3 × 2` rectangle. Conclude that `A` and `B` have the same Ihara zeta function.

## Appearances in Sources

- [[project-euler-502-castle-factoring](pages/project-euler-502-castle-factoring.md)] - the castle given by its column heights, each at least 1, so the castles with `n` cells form a finite list.

## Related Concepts

- [[isospectral-castles](pages/isospectral-castles.md)] - the exhaustive search through 16 cells; this page is its seminar version.
- [[castle-graph](pages/castle-graph.md)] - the castle graph, its invariants, and the tree castles.
- [[castle-graph-spectral-radius](pages/castle-graph-spectral-radius.md)] - the castles golden and silver by spectrum, and the spectral-radius scan.
- [[castle-eigenvalues-by-example](pages/castle-eigenvalues-by-example.md)] - the castles of Stop 1 and the 10-cell pair worked by hand.
- [[spectral-analysis](pages/spectral-analysis.md)] - the spectra computed for castles and what each decides.
- [[levy-flights](pages/levy-flights.md)] - the local return probabilities that separate the 11-cell pair.
- [[castle-classification-spectrum](pages/castle-classification-spectrum.md)] - the spectral types of castles.
- [[sandpile-group](pages/sandpile-group.md)] - the sandpile group in the sink and tide models, built from the Laplacian; neither separates the 10-cell or the 11-cell pair.
- [[sandpile-census](pages/sandpile-census.md)] - the sandpile groups through 16 cells: the sink group separates no cospectral group; the tide group, which depends on how the blocks stand, separates 23 of the 105 adjacency groups.
- [[sandcastle-clock](pages/sandcastle-clock.md)] - the clock periods; on the 10-cell pair the sink clocks tick 15 and 5, the tide clocks 4 and 8.
- [[sandpile-identity](pages/sandpile-identity.md)] - one grain on the apex of the identity of the 10-cell pair: 57 topplings against 1.
- [[sandcastle-seminar](pages/sandcastle-seminar.md)] - a seminar following the 16-cell castle `(3,2,1,2,2,1,2,3)`, silver by spectrum, through its sandpile group, clock, identity and avalanches.
- [[castle-avalanches](pages/castle-avalanches.md)] - random grain drops on castles; the mean avalanche size is given by the reduced Laplacian, and the `2 × 2` squares change the tail of the distribution.
- [[hardin-identity-seminar](pages/hardin-identity-seminar.md)], [[castle-fibers-char-2-walkthrough](pages/castle-fibers-char-2-walkthrough.md)], [[tower-recursion-master-class](pages/tower-recursion-master-class.md)], [[oeis-mining-seminar](pages/oeis-mining-seminar.md)], [[one-bit-seminar](pages/one-bit-seminar.md)], [[q-thread-seminar](pages/q-thread-seminar.md)], [[pell-castle-strip](pages/pell-castle-strip.md)], [[castle-cryptography](pages/castle-cryptography.md)] and [[song-as-castle](pages/song-as-castle.md)] - the other seminar pages.

## Footnotes

[^1]: Verified by execution (Python 3.11, SymPy 1.14, 2026-10-16): the three factored characteristic polynomials and the spanning-tree counts 4 and 15, printed by the Snippet (`spanning_trees` is the `(1, 1)` cofactor of `L`).
[^2]: Verified by execution (Python 3.11, SymPy, NumPy, 2026-10-16): `smallest_pair('adjacency')` returns the 10-cell pair as the first non-isomorphic cospectral pair over every castle with at most 10 cells, mirror images removed; the traces `22, 0, 106`, the spanning trees `15, 15`, the degree sequences and the unequal Laplacian polynomials as printed. The pair agrees with the networkx-certified search of isospectral-castles, and both castles have the sink sandpile group `Z/15` by Smith normal form.
[^3]: Verified by execution (Python 3.11, SymPy, NumPy, 2026-10-16): `smallest_pair('laplacian')` returns the 11-cell tree pair, with equal Laplacian polynomials and degree sequences, one spanning tree each, equal sorted diagonals of `L²` and unequal sorted diagonals of `L³`; the DFT magnitudes of `(1,1,1,2,3,2)` and `(1,1,2,2,3,1)`; the 2-core of both 10-cell castles is the `3 × 2` rectangle, and the traces of the powers of the non-backtracking edge matrix agree for the two castles up to length 16 and vanish for the two tree castles; the sink clock periods 15 and 5 and the tide periods 4 and 8, as the least common denominators of the apex column of `L̃⁻¹`.
[^4]: https://arxiv.org/pdf/math/9207215 (C. Gordon, D. L. Webb and S. Wolpert, "One cannot hear the shape of a drum", *Bull. Amer. Math. Soc.* 27 (1992) 134-138, read 2026-10-16) - abstract, p.1: "We use an extension of Sunada's theorem to construct a nonisometric pair of isospectral simply connected domains in the Euclidean plane, thus answering negatively Kac's question, \"can one hear the shape of a drum?\""; §2, p.2: "Theorem (Sunada). Let M be a Riemannian manifold upon which a finite group G acts by isometries; let H and K be subgroups of G that act freely. Suppose that H and K are almost conjugate ... Then the quotient manifolds M1 = H\M and M2 = K\M are isospectral." Kac's paper (*Amer. Math. Monthly* 73 (1966) 1-23) is cited through its reference [16].
[^5]: https://aeb.win.tue.nl/2WF02/spectra.pdf (A. E. Brouwer and W. H. Haemers, *Spectra of Graphs*, monograph version of February 1, 2011, read 2026-10-16) - Proposition 1.3.4, p.5, the number of spanning trees is any cofactor of the Laplace matrix, "known as the Matrix-Tree Theorem"; Proposition 1.3.7, p.7: "The multiplicity of 0 as a Laplace eigenvalue of an undirected graph Γ equals the number of connected components of Γ."
[^6]: https://users.cecs.anu.edu.au/~bdm/papers/SpectralTrees.pdf (B. D. McKay, "On the spectral characterisation of trees", *Ars Combinatoria* 3 (1977) 219-232, read 2026-10-16) - §1, p.219: "A.J. Schwenk [11] has proved that \"hardly any\" tree is thus characterised; the proportion dropping to zero as the number of vertices increases", and "we may also require the trees to have cospectral linegraphs"; Theorem 3.1, p.222, `B'B = A(L(G)) + 2I` and `BB' = A(G) + Δ(G)` for the incidence matrix `B`. Schwenk's paper (*New Directions in the Theory of Graphs* (1973) 275-307) is cited through McKay's reference [11].
