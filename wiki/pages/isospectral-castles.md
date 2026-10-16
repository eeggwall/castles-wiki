---
title: Isospectral castles - hearing the shape of a castle
category: Analyses
summary: Kac's question "can one hear the shape of a drum?" asked of castles - does the adjacency or the Laplacian spectrum of the castle graph determine the graph? An exhaustive search over all 65,535 castles with at most 16 cells (33,150 up to mirror image), with exact characteristic polynomials and exact isomorphism tests, finds the smallest castles with non-isomorphic graphs and the same adjacency spectrum at 10 cells, the same Laplacian spectrum at 11 cells (two tree castles), and both at 16 cells; there are 105 adjacency groups and 17 Laplacian groups in all. The 36 castles silver by spectrum of the large spectral-radius scan form 22 graphs, no two cospectral. The two 10-cell castles have the same Ihara zeta function, since they have the same 2-core.
tags: [analysis, castle, spectral, isospectral, adjacency, laplacian, kac, sunada, schwenk, trace-formula, tree, numpy, sympy, networkx, verification]
sources: [project-euler-502-castle-factoring]
created: 2026-09-16
updated: 2026-10-16
---

# Isospectral castles - hearing the shape of a castle

## Kac's question, asked of castles

Kac asked whether the frequencies of a drum, the eigenvalues of the Laplace operator on a plane domain, determine its shape; Gordon, Webb and Wolpert answered no in 1992 with a pair of nonisometric simply connected plane domains with the same Dirichlet and the same Neumann spectra, constructed by an extension of Sunada's theorem (section *Why cospectral graphs exist*). Some things are determined: Weyl proved that the spectrum determines the area of a plane domain.[^1]

The castle version replaces the drum by the castle graph, with the cells as vertices and an edge between two cells that share a side ([[castle-graph](pages/castle-graph.md)]). Two matrices are attached to it: the adjacency matrix `A`, and the Laplacian `L = D − A`, with `D` the diagonal matrix of degrees. Two castles are **cospectral** (or **isospectral**) for `A` or for `L` when the matrix has the same eigenvalues, with multiplicities, for both. The question is whether the spectrum determines the castle graph up to isomorphism. Mirror images and castles with isomorphic graphs count as the same. This page answers it by exhaustive search over every castle with at most 16 cells, for both matrices.

## Method

A castle with `n` cells is a composition of `n`, its column heights in order, so there are `2^{n−1}` castles with `n` cells and `2^16 − 1 = 65,535` with at most 16, 33,150 up to mirror image. For each `n`, the castles are grouped by their spectrum rounded to 7 decimals, each group is split into isomorphism classes with `networkx.is_isomorphic`, and every group with two or more classes is confirmed by the exact integer characteristic polynomial (SymPy).[^2]

```python
def compositions(n):
    if n == 0: yield (); return
    for first in range(1, n+1):
        for rest in compositions(n-first): yield (first,) + rest

def adj_np(c):
    cells = [(i, j) for i, h in enumerate(c) for j in range(h)]; idx = {cell: k for k, cell in enumerate(cells)}
    A = np.zeros((len(cells), len(cells)))
    for (i, j), u in idx.items():
        for nb in ((i+1, j), (i, j+1)):
            if nb in idx: A[u, idx[nb]] = A[idx[nb], u] = 1
    return A

groups = defaultdict(list)
for c in compositions(n):
    if c[::-1] < c: continue                                   # mirror images are the same castle
    A = adj_np(c); Mx = np.diag(A.sum(1)) - A if laplacian else A
    groups[tuple(np.round(np.linalg.eigvalsh(Mx), 7))].append(c)
# then: split each group into networkx isomorphism classes; keep groups with >= 2 classes
#       whose exact sympy characteristic polynomials agree
```

## Results

| cells `n` | adjacency groups | Laplacian groups |
|---|---|---|
| 1 - 9 | 0 | 0 |
| 10 | **2** | 0 |
| 11 | 0 | **1** |
| 12 | 10 | 0 |
| 13 | 6 | 2 |
| 14 | 18 | 2 |
| 15 | 19 | 5 |
| 16 | 50 | 7 |
| total | 105 | 17 |

A group is a set of at least two pairwise non-isomorphic castle graphs with the same spectrum. Several skylines can have the same graph, and the lists in this section give every skyline, up to mirror image, of each isomorphism class.[^2]

### The smallest adjacency-cospectral castles: 10 cells

```
class A: (1,1,1,2,3,2), (2,1,2,3,2)        class B: (1,1,2,2,3,1), (1,3,2,4), (1,3,5,1)
....#.                                      ....#.
...###                                      ..###.
######                                      ######
```

The common characteristic polynomial is `x¹⁰ − 11x⁸ + 34x⁶ − 36x⁴ + 12x²`, with spectral radius `2.5832`. Both castles drawn contain a `3 × 2` rectangle of cells with one cell on top. In `A` the extra cell stands on the middle column of the rectangle, which gives a cell four neighbors; in `B` it stands on an end column, and no cell has four neighbors. So the graphs are not isomorphic, and every adjacency eigenvalue agrees. The second 10-cell group is `(1,1,2,1,2,3), (1,3,1,2,3)` against `(1,2,1,1,2,2,1), (1,2,1,1,3,2)`, with polynomial `x¹⁰ − 10x⁸ + 30x⁶ − 28x⁴ + 7x²`.[^2]

### The smallest Laplacian-cospectral castles: 11 cells, two trees

```
class A: (1,1,1,2,1,1,2,1,1) and five more skylines      class B: (1,1,3,1,1,1,2,1)
...#..#..                                                 ..#.....
#########                                                 ..#...#.
                                                          ########
```

The common Laplacian characteristic polynomial is `x¹¹ − 20x¹⁰ + 169x⁹ − 788x⁸ + 2223x⁷ − 3916x⁶ + 4295x⁵ − 2838x⁴ + 1051x³ − 188x² + 11x`.[^2]

**Both are tree castles.** A castle graph is a tree exactly when no two neighboring columns both have height at least 2, since a filled `2 × 2` square is a 4-cycle ([[castle-graph](pages/castle-graph.md)]). `A` is a row of 9 cells with one cell above the columns 4 and 7; `B` is a row of 8 cells with two cells above column 3 and one above column 7. Both have 11 vertices and 10 edges.

**What the Laplacian spectrum determines.**

- The multiplicity of the eigenvalue 0 is the number of connected components, here 1 (Brouwer and Haemers, Proposition 1.3.7).[^3]
- `trace L = Σ_v d_v = 2|E| = 20`, the negative of the coefficient of `x¹⁰`, so the number of edges, and `trace L² = Σ_v d_v (d_v + 1)`, so the sum of the squared degrees.
- The number of spanning trees, which is any cofactor of `L` (Proposition 1.3.4), here 1.[^3]

Both trees have the same degree sequence, `3, 3, 2, 2, 2, 2, 2, 1, 1, 1, 1`, and the difference is in how the cells of degree 3 sit. In `A` each of the two cells of degree 3 has one neighbor of degree 1. In `B` one cell of degree 3, at the foot of the single spike, has two neighbors of degree 1, and the other, at the foot of the two-cell spike, has none.[^2]

**Six skylines, one graph.** Class `A` has six skylines with the same graph: `(1,1,1,2,1,1,2,1,1)`, `(1,1,1,2,1,1,3,1)`, `(1,1,2,1,1,2,1,2)`, `(1,1,2,1,1,4,1)`, `(1,3,1,1,2,1,2)` and `(1,3,1,1,4,1)`. Each is a path with two pendant paths, laid out differently over the columns. Class `B` has one skyline with 11 cells.

### Cospectral for both matrices: 16 cells

The first castles with the same adjacency and the same Laplacian spectrum have 16 cells. There is one such group, again two tree castles, for example `(1,1,1,1,2,1,1,3,1,2,1,1)` and `(1,1,1,1,3,1,2,1,1,2,1,1)`, with eight skylines in each class.[^2]

## Why cospectral graphs exist

**The trace formula.** The entry `(u, v)` of `Aⁿ` counts the walks of length `n` from `u` to `v`, so `trace Aⁿ` counts the closed walks of length `n`, and it is the sum of the `n`-th powers of the eigenvalues. Two castles are adjacency-cospectral exactly when they have the same number of closed walks of every length.

**Trees.** Schwenk proved that the proportion of trees on `n` vertices that are determined by their adjacency spectrum tends to 0 as `n → ∞`. McKay showed that the same holds when the cospectral trees are also required to have cospectral line graphs.[^4] For a tree, cospectral line graphs mean the same Laplacian spectrum: a tree is bipartite, so `L = D − A` is similar to `D + A = BBᵀ`, with `B` the vertex-edge incidence matrix, while `BᵀB = A(L(G)) + 2I`, and `BBᵀ` and `BᵀB` have the same nonzero eigenvalues (McKay, Theorem 3.1(ii)).[^4] These theorems concern trees in general, of which the tree castles are a small family, and they do not produce the castle pairs.

**Sunada's theorem.** Let a finite group `G` act by isometries on a Riemannian manifold `M`, and let `H` and `K` be subgroups that act freely and are almost conjugate: there is a bijection `f : H → K` with `f(h)` conjugate to `h` in `G` for every `h`. Then the quotients `H\M` and `K\M` are isospectral. Gordon, Webb and Wolpert used an extension of this theorem for their plane domains.[^1] Choosing conjugate subgroups gives isometric quotients, so the construction needs almost conjugate subgroups that are not conjugate.

## The castles silver by spectrum are not cospectral

A castle is silver by spectrum when its castle graph has spectral radius `1 + √2`. The scan of [[castle-graph-spectral-radius](pages/castle-graph-spectral-radius.md)], over all castles with `w ≤ 8` and `h ≤ 7`, with `w = 9` and `h ≤ 5`, and with `w = 10` and `h ≤ 4`, finds 36 of them up to mirror image, with 6 to 20 cells. They have 22 distinct graphs: for example `(2, 2, 2)` and `(3, 3)` are both the `3 × 2` rectangle. No two of the 22 graphs have the same adjacency spectrum or the same Laplacian spectrum.[^5]

## Summary

- The smallest castles with non-isomorphic graphs and the same spectrum have **10 cells** for the adjacency matrix, **11 cells** for the Laplacian, and **16 cells** for both.
- Through 16 cells there are 105 adjacency groups and 17 Laplacian groups, 50 and 7 of them at 16 cells, so the spectrum does not determine the castle graph.
- The **Ihara zeta function** `ζ(u) = ∏_{[γ]} (1 − u^{|γ|})^{−1}`, over the classes of prime closed walks without backtracking and without tails ([[spectral-analysis](pages/spectral-analysis.md)], section 5), does not separate either smallest pair. A closed walk without backtracking and without tail never enters a pendant tree, so `ζ` depends only on the 2-core, the subgraph left after repeatedly deleting vertices of degree 1. The 2-core of both 10-cell castles is the `3 × 2` rectangle, so they have the same zeta function, and both 11-cell tree castles have `ζ = 1`.[^6]
- **Sandpile invariants.** Through 16 cells the sink-model sandpile group separates none of the 122 groups, since the castles in each share their graph of `2 × 2` blocks ([[sandpile-census](pages/sandpile-census.md)]); the sink clock spectrum separates 62 of the 105 adjacency groups and 5 of the 17 Laplacian groups ([[sandcastle-clock](pages/sandcastle-clock.md)]); and the sink avalanche profile separates all of them ([[sandpile-identity](pages/sandpile-identity.md)]).
- **The skyline DFT.** The discrete Fourier transform of the skyline is invertible, so it separates every pair. Its magnitudes do not change under a cyclic shift of the columns or under the mirror image, and they miss exactly those: through 16 cells, 44 adjacency-cospectral and 4 Laplacian-cospectral pairs are cyclic shifts of each other or of the mirror image, the smallest being `(1,2,1,1,3,2)` and `(1,1,2,1,2,3)` from the second 10-cell group ([[spectral-analysis](pages/spectral-analysis.md)], section 3).

## Appearances in Sources

- [[project-euler-502-castle-factoring](pages/project-euler-502-castle-factoring.md)] - the castle given by its column heights, each at least 1, so the castles with `n` cells are the compositions of `n`.

## Related Concepts

- [[hear-the-shape-seminar](pages/hear-the-shape-seminar.md)] - a seminar on what the spectrum of a castle graph determines, with a snippet that finds the 10-cell and 11-cell pairs.
- [[castle-eigenvalues-by-example](pages/castle-eigenvalues-by-example.md)] - small castles worked by hand, including the 10-cell pair.
- [[castle-classification-spectrum](pages/castle-classification-spectrum.md)] - the spectral types of castles, of which isospectral pairs are one.
- [[castle-graph-spectral-radius](pages/castle-graph-spectral-radius.md)] - the spectral radii of castle graphs and the scan that finds the castles silver by spectrum.
- [[castle-graph](pages/castle-graph.md)] - the castle graph and the tree castles.
- [[spectral-analysis](pages/spectral-analysis.md)] - the Laplacian, the Ihara zeta function and the skyline DFT.
- [[levy-flights](pages/levy-flights.md)] - the fractional Laplacian `L^α`; its heat traces are functions of the Laplacian spectrum, but its local return probabilities separate the 11-cell pair.
- [[castle-snippets](pages/castle-snippets.md)] - `castle_graph_radius` and the adjacency and Laplacian matrices of a castle.
- [[castle-representations](pages/castle-representations.md)] - the skyline encoding the search runs on.
- [[sandpile-group](pages/sandpile-group.md)] - the sandpile groups of a castle in the sink and tide models; the 10-cell castles have `Z/15` and `Z/8`, and the 11-cell tree castles the trivial group in both.
- [[sandpile-census](pages/sandpile-census.md)] - the sandpile groups of every castle with at most 16 cells, and which cospectral groups they separate.
- [[sandcastle-clock](pages/sandcastle-clock.md)] - the clock periods, whose sink spectrum separates 62 adjacency and 5 Laplacian groups.
- [[sandpile-identity](pages/sandpile-identity.md)] - the identity configurations, whose sink avalanche profile separates every group.

## Footnotes

[^1]: https://arxiv.org/pdf/math/9207215 (C. Gordon, D. L. Webb and S. Wolpert, "One cannot hear the shape of a drum", *Bull. Amer. Math. Soc.* 27 (1992) 134-138, read 2026-10-16) - abstract and §1, p.1: "We use an extension of Sunada's theorem to construct a nonisometric pair of isospectral simply connected domains in the Euclidean plane, thus answering negatively Kac's question", "a pair of nonisometric simply connected plane domains that have both the same Dirichlet spectra and the same Neumann spectra"; p.2: "Weyl's proof [23] that the area of a plane domain is determined by the spectrum"; §2, p.2: "Theorem (Sunada). Let M be a Riemannian manifold upon which a finite group G acts by isometries; let H and K be subgroups of G that act freely. Suppose that H and K are almost conjugate, i.e., there is a bijection f : H → K carrying every element h of H to an element f(h) of K that is conjugate in G to h. Then the quotient manifolds M1 = H\M and M2 = K\M are isospectral." and "Choosing conjugate subgroups in the above theorem yields isometric manifolds". Kac's paper, "Can one hear the shape of a drum?", *Amer. Math. Monthly* 73 (1966) 1-23, is cited through this paper's reference [16].
[^2]: Verified by execution (Python 3.11, NumPy 1.26, SymPy 1.14, networkx 3.4.2, 2026-10-16): all compositions of `n ≤ 16`, mirror images removed (33,150 castles), grouped by spectrum rounded to 7 decimals, split into isomorphism classes by `networkx.is_isomorphic`, and confirmed by equal exact characteristic polynomials; the per-`n` counts of the table, the skylines of the 10-cell, 11-cell and 16-cell groups, both 10-cell polynomials and the 11-cell Laplacian polynomial; the degree sequences and the neighbors of the cells of degree 3 in the 11-cell pair.
[^3]: https://aeb.win.tue.nl/2WF02/spectra.pdf (A. E. Brouwer and W. H. Haemers, *Spectra of Graphs*, monograph version of February 1, 2011, read 2026-10-16) - Proposition 1.3.4, p.5, the number of spanning trees is any cofactor of the Laplace matrix, "known as the Matrix-Tree Theorem"; Proposition 1.3.7, p.7: "The multiplicity of 0 as a Laplace eigenvalue of an undirected graph Γ equals the number of connected components of Γ."
[^4]: https://users.cecs.anu.edu.au/~bdm/papers/SpectralTrees.pdf (B. D. McKay, "On the spectral characterisation of trees", *Ars Combinatoria* 3 (1977) 219-232, read 2026-10-16) - §1, p.219: "A.J. Schwenk [11] has proved that \"hardly any\" tree is thus characterised; the proportion dropping to zero as the number of vertices increases", and "we may also require the trees to have cospectral linegraphs and cospectral distance matrices"; Theorem 3.1, p.222: "Let B be the incidence matrix of G. Then B'B = A(L(G)) + 2I and BB' = A(G) + Δ(G)". Schwenk's paper, "Almost all trees are cospectral", in *New Directions in the Theory of Graphs* (1973) 275-307, is cited through McKay's reference [11].
[^5]: Verified by execution (Python 3.11, NumPy, networkx 3.4.2, 2026-10-16): the 36 skylines listed on castle-graph-spectral-radius all have spectral radius `1 + √2` to `10⁻⁹`; grouped by cell count and rounded adjacency spectrum, and separately by Laplacian spectrum, every group with two or more skylines consists of isomorphic graphs, and the skylines form 22 isomorphism classes.
[^6]: Verified by execution (Python 3.11, 2026-10-16): the 2-core of both `(1,1,1,2,3,2)` and `(1,1,2,2,3,1)` is the six cells of a `3 × 2` rectangle; the traces of the powers of the non-backtracking edge matrix, which count the closed walks without backtracking and without tails, agree for the two castles and for `(3, 3)` up to length 16 (`0, 0, 0, 16, 0, 12, 0, 32, …`), and vanish for both 11-cell tree castles.
