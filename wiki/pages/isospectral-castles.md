---
title: Isospectral castles - hearing the shape of a castle
category: Analyses
summary: The castle version of Kac's "Can one hear the shape of a drum?" - does the Laplacian spectrum of a castle's polyomino graph determine the castle up to isomorphism? Exhaustive search over every castle with at most 16 cells (65,534 skylines mirror-deduped, exact integer characteristic polynomials, isomorphism by networkx). Smallest non-isomorphic castles with the same adjacency spectrum: 10 cells; same Laplacian spectrum: 11 cells (two trees, exemplifying Schwenk's theorem); same for both: 16 cells. Sunada's construction and the trace formula frame the general theory; no two of the 36 silver-spectrum castles are isospectral.
tags: [analysis, castle, spectral, isospectral, adjacency, laplacian, axis-9, kac, sunada, schwenk, trace-formula, tree, numpy, sympy, networkx, verification, pedagogy]
sources: [project-euler-502-castle-factoring]
created: 2026-09-16
updated: 2026-09-26
---

# Isospectral castles - hearing the shape of a castle

## Kac's question, in the castle setting

Mark Kac, "Can one hear the shape of a drum?" (American Mathematical Monthly, 1966), asked whether the vibration frequencies of a membrane determine its shape up to congruence. The frequencies are the eigenvalues of the Laplacian on the membrane, so the question is: does the spectrum of the Laplacian determine the domain? For 26 years the answer was unknown. Gordon, Webb, and Wolpert answered *no* in 1992 by exhibiting two L-shaped polygons with identical Laplacian spectra and non-congruent shapes. Some things you *can* hear: the area of the drum, the length of its boundary, the number of holes (Weyl asymptotics; Kac's own heat-trace computation). Shape itself is not among them.

The castle version replaces the membrane with the castle's polyomino graph of [[castle-classification-spectrum](pages/castle-classification-spectrum.md)] Axis 9 - filled cells as vertices, orthogonal neighbors as edges - and the Laplacian on a function space with the combinatorial Laplacian `L = D − A` on `R^n`, where `D` is the diagonal degree matrix and `A` is the adjacency matrix. Two castles are **isospectral** when these two matrices share their eigenvalue multiset; the castle version of Kac's question is whether the spectrum determines the castle up to graph isomorphism. Schwenk (1973) already proved that almost every tree has a non-isomorphic cospectral mate, so the answer is *no* in the strongest possible way for graphs; the interesting number is how small a counterexample can be. This page runs the exhaustive search and finds it, for the adjacency operator and for the combinatorial Laplacian, over every castle with at most 16 cells.

## Method

A castle with `n` cells is a composition of `n` (column heights `≥ 1`), so "every castle with at most 16 cells" is `2^16 − 1 = 65,535` skylines regardless of width and height - cheap. For each cell count: enumerate compositions, drop mirror images, compute the spectrum with NumPy, group by the rounded spectrum, split each group into isomorphism classes with `networkx.is_isomorphic`, and confirm every surviving group with the **exact integer characteristic polynomial** (SymPy) so that no floating-point coincidence is counted.[^1]

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
    if c[::-1] < c: continue                                   # mirror dedupe
    A = adj_np(c); Mx = np.diag(A.sum(1)) - A if laplacian else A
    groups[tuple(np.round(np.linalg.eigvalsh(Mx), 7))].append(c)
# then: split each group into networkx isomorphism classes; keep groups with >= 2 classes
#       whose exact sympy charpolys agree
```

## Results

| cells `n` | adjacency-isospectral groups | Laplacian-isospectral groups |
|---|---|---|
| 1 - 9 | 0 | 0 |
| 10 | **2** | 0 |
| 11 | 0 | **1** |
| 12 | 10 | 0 |
| 13 | 6 | 2 |
| 14 | 18 | 2 |
| 15 | 19 | 5 |
| 16 | 50 | 7 |

A "group" is a set of at least two pairwise non-isomorphic castle graphs with identical spectrum; several skylines can realize the same graph, and the lists below show every skyline (up to mirror) in each isomorphism class.

### The smallest adjacency-isospectral castles: 10 cells

```
class A: (1,1,1,2,3,2), (2,1,2,3,2)        class B: (1,1,2,2,3,1), (1,3,2,4), (1,3,5,1)
....#.                                      ....#.
...###                                      ..###.
######                                      ######
```

Common characteristic polynomial `x¹⁰ − 11x⁸ + 34x⁶ − 36x⁴ + 12x²`, spectral radius `2.5832`. Both are 10-cell castles containing a `2×2` block; the two graphs are not isomorphic (A has a vertex of degree 4, B does not - the `2×2` blocks sit differently), yet every adjacency eigenvalue agrees. The second 10-cell group is `(1,1,2,1,2,3), (1,3,1,2,3)` versus `(1,2,1,1,2,2,1), (1,2,1,1,3,2)` with polynomial `x¹⁰ − 10x⁸ + 30x⁶ − 28x⁴ + 7x²`.[^1]

### The smallest Laplacian-isospectral castles: 11 cells (two trees)

```
class A: (1,1,1,2,1,1,2,1,1) and five more skylines      class B: (1,1,3,1,1,1,2,1)
...#..#..                                                 ..#.....
#########                                                 ..#...#.
                                                          ########
```

Common Laplacian characteristic polynomial `x¹¹ − 20x¹⁰ + 169x⁹ − 788x⁸ + 2223x⁷ − 3916x⁶ + 4295x⁵ − 2838x⁴ + 1051x³ − 188x² + 11x`.[^1]

**Both are trees.** A *tree* is a connected graph with no cycles, equivalently `n` vertices and `n − 1` edges. A castle graph is a tree exactly when no two horizontally adjacent columns both have height at least 2: a `2 × 2` block would close a 4-cycle. `A` is a horizontal row of 9 cells with two 1-cell spikes above positions 4 and 7. `B` is a row of 8 cells with a 2-cell spike above position 3 and a 1-cell spike above position 7. Both are connected, both have 11 vertices and 10 edges, neither has a cycle. Different shapes, same Laplacian spectrum.

**What the spectrum sees and what it misses.** From `L = D − A` one reads off:

- `0` is always an eigenvalue; its multiplicity is the number of connected components (here 1).
- `trace(L) = 2·|E| = 20`, so the graph has 10 edges (visible in the coefficient of `x¹⁰`).
- The number of spanning trees is any cofactor of `L`; for a tree this is 1, and both castles are trees.
- The smallest nonzero eigenvalue (the *algebraic connectivity*, Fiedler's number) measures how well-connected the graph is; both castles have the same value.

What the spectrum does *not* see is the local branching pattern. `A` has two degree-3 vertices, each adjacent to a single leaf. `B` has one degree-3 vertex adjacent to a leaf and one adjacent to a two-cell path. That difference is invisible to `L`'s eigenvalues. Schwenk's 1973 theorem says this is generic among trees: almost every tree has a Laplacian-cospectral mate, so the failure of Kac's question for graphs is not exotic. The castle setting reaches it at 11 cells.

**Six skylines, one graph.** The `A` class has six skylines because the same underlying graph is realized by six different castle shapes: `(1,1,1,2,1,1,2,1,1)`, `(1,1,1,2,1,1,3,1)`, `(1,1,2,1,1,2,1,2)`, `(1,1,2,1,1,4,1)`, `(1,3,1,1,2,1,2)`, `(1,3,1,1,4,1)`. Trees with a horizontal spine and two pendant paths, drawn as castles with the pendants distributed differently over the columns. Class `B` has only one skyline in this size.

### Isospectral for both operators: 16 cells

The first castles that agree in *both* the adjacency and the Laplacian spectrum have 16 cells; there is one such group, again a pair of trees, e.g. `(1,1,1,1,2,1,1,3,1,2,1,1)` versus `(1,1,1,1,3,1,2,1,1,2,1,1)` (eight skylines in each class).[^1]

### Why cospectral pairs exist: Sunada, Schwenk, and the trace formula

Two structural reasons account for every isospectral pair on this page.

**Sunada-style construction (Toshikazu Sunada, 1985).** A general recipe for producing pairs of Riemannian manifolds, and later graphs, with identical Laplacian spectra but not isometric. Take a group `G` acting freely on a space `X`, and two subgroups `H_1, H_2` of `G` that are *almost conjugate*: every conjugacy class of `G` meets `H_1` and `H_2` in the same number of elements, though `H_1` and `H_2` are themselves not conjugate. Then the quotients `X/H_1` and `X/H_2` are isospectral but not isometric. Gordon, Webb, and Wolpert used it in 1992 to build the first isospectral planar drums (two L-shaped polygons with the same spectrum and different shapes), settling Kac's question. The graph version, mostly due to Robert Brooks and Hyman Bass, produces isospectral graphs from a covering of a base graph by two almost-conjugate subgroups. A Sunada-type explanation of the 10-cell adjacency pair on this page would be a common cover: a small graph that both `(1,1,1,2,3,2)` and `(1,1,2,2,3,1)` project onto with matching closed-walk counts. That has not been written down; it is the natural next step and open on IDEAS.

**The trace formula, and why closed walks are the invariant.** The trace of `Aᴸ` counts closed walks of length `L` in the graph, so a shared adjacency spectrum is the same thing as matching closed-walk counts at every length. Two castles are adjacency-cospectral iff they have the same number of closed walks of each length. For the Laplacian, `L = D − A`, the trace of `Lᴸ` mixes walk counts with degree information; Laplacian-cospectral castles have the same walk counts weighted by the degree sequence at each visited vertex.

**Schwenk's theorem (1973).** *Almost every tree has a non-isomorphic cospectral mate.* Precisely, the fraction of trees on `n` vertices that have a cospectral mate tends to 1 as `n → ∞`. So finding a Laplacian-cospectral pair *among trees* is not the exotic case, it is the generic case. This is why the smallest castle Laplacian-isospectral pair turns out to be trees: the same phenomenon that makes tree cospectrality easy makes it easy in the castle setting too.

The three ingredients divide the pairs on this page cleanly. Sunada explains the *existence* of adjacency-cospectral pairs with cycles (the 10-cell pair, and the 50 adjacency groups at 16 cells). Schwenk explains the tree pairs (the 11-cell Laplacian pair, and the growing collection at 12+). The trace formula is the tool that turns either of these into an executable check.

### Silver-spectrum castles are not isospectral to each other

The spectral-radius census on [[castle-graph-spectral-radius](pages/castle-graph-spectral-radius.md)] found 36 castles with adjacency spectral radius `1 + √2` (all `w ≤ 8, h ≤ 7`; `w = 9, h ≤ 5`; `w = 10, h ≤ 4`), with 6 to 20 cells. Grouping them by cell count and full spectrum finds **no** two non-isomorphic silver castles with the same spectrum: sharing the top eigenvalue never extends to the whole spectrum in this range.[^2]

## What this settles and what it opens

- The seminar number: **10 cells** (adjacency), **11 cells** (Laplacian), **16 cells** (both). Each with a two-line drawing.
- Isospectral pairs are common from 12 cells on (50 adjacency groups at 16 cells), so "spectrum determines the castle" fails badly. The spectrum is an Axis 9 *invariant*, not a *classifier*.
- The 11-cell Laplacian pair is the smallest castle instance of Schwenk's theorem; the 10-cell adjacency pair is the smallest castle instance of Sunada's phenomenon and is a candidate for an explicit common cover.
- Open: the growth rate of the number of isospectral groups with `n`; whether the Ihara zeta or the skyline discrete Fourier transform (DFT) separates the pairs found here; a Sunada-type construction (common cover, almost-conjugate subgroups) explaining the 10-cell adjacency pair; and whether Schwenk's asymptotic density theorem has a quantitative castle analogue.

## Appearances in Sources

- [[project-euler-502-castle-factoring](pages/project-euler-502-castle-factoring.md)] - the castle definition (column heights `≥ 1`, i.e. compositions) that makes "all castles with `n` cells" enumerable.

## Related Concepts

- [[spectral-analysis](pages/spectral-analysis.md)] - method 4 (combinatorial Laplacian) and the isospectral hunt this page runs.
- [[levy-flights](pages/levy-flights.md)] - the fractional Laplacian `L^α` on the castle graph and the local return probability at a named cell as a non-spectral separator of the 11-cell Laplacian-isospectral tree pair here (fails as a spectral invariant, works as a local one).
- [[castle-classification-spectrum](pages/castle-classification-spectrum.md)] - Axis 9; isospectral pair is the pair predicate there.
- [[castle-graph-spectral-radius](pages/castle-graph-spectral-radius.md)] - the single-eigenvalue census (golden, silver, φ² castles) and the silver list checked here.
- [[castle-snippets](pages/castle-snippets.md)] - `compositions`, `castle_graph_radius`, and the spectrum-hashing loop.
- [[castle-graph](pages/castle-graph.md)] - the graph the spectrum lives on; the 11-cell Laplacian-isospectral pair is a pair of **tree castles** in the sense named there.
- [[castle-representations](pages/castle-representations.md)] - the skyline encoding the enumeration runs on.
- [[aocp-generating-permutations-tuples](pages/aocp-generating-permutations-tuples.md)] - the 65,534-skyline sweep is Knuth's Algorithm M (mixed-radix enumeration of `{1..h}^w`) with a cell-count filter.
- [[castle-compression](pages/castle-compression.md)] - a spectrum is a lossy code for a castle; the isospectral pairs found here are its collisions, and their sizes (10 / 11 / 16 cells) are where spectral compression first loses information.
- [[castle-eigenvalues-by-example](pages/castle-eigenvalues-by-example.md)] - the from-scratch pedagogy that works out the 10-cell adjacency-isospectral pair by hand as its "two shapes, same spectrum" section.
- [[hear-the-shape-seminar](pages/hear-the-shape-seminar.md)] - the classroom version: what the spectrum hears, and the 10- and 11-cell pairs reproduced by one runnable search.
- [[sandpile-group](pages/sandpile-group.md)] - the sandpile group of each castle; both small cospectral pairs have equal groups (Z/15 and trivial).
- [[sandpile-census](pages/sandpile-census.md)] - the sandpile group of every castle in this page's census; it separates none of the cospectral groups, because each shares its block graph.
- [[sandcastle-clock](pages/sandcastle-clock.md)] - the clock spectrum separates 62 of this page's 105 adjacency-cospectral groups and 5 of its 17 Laplacian ones.
- [[sandpile-identity](pages/sandpile-identity.md)] - the avalanche profile separates every cospectral group on this page to 16 cells.


## Footnotes

[^1]: Verified by execution (NumPy, SymPy 1.14, networkx 3.4.2): all compositions of `n ≤ 16` with mirror dedupe (`c[::-1] < c` skipped), spectra rounded to 7 decimals for grouping, isomorphism classes by `networkx.is_isomorphic`, and exact `Matrix.charpoly` over the integers equal across classes for every group counted. Total 11 s. The per-`n` counts and the smallest groups' skylines and polynomials are as printed by the run.

[^2]: From the spectral-radius scan on [[castle-graph-spectral-radius](pages/castle-graph-spectral-radius.md)] (4,868,525 mirror-deduped castles): the 36 castles with spectral radius within `10⁻⁸` of `1 + √2`, grouped by cell count and rounded spectrum; every group with two or more skylines consisted of isomorphic graphs.
