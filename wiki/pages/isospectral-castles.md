---
title: Isospectral castles - hearing the shape of a castle
category: Analyses
summary: Exhaustive search over every castle with at most 16 cells (all widths and heights; 65,534 skylines, mirror-deduped), exact integer characteristic polynomials, isomorphism tested with networkx. Smallest non-isomorphic castles with the same adjacency spectrum have 10 cells (two groups); with the same Laplacian spectrum, 11 cells (a pair of trees); isospectral for both operators, 16 cells. Counts by cell count are tabulated. No two of the 36 silver-spectrum castles up to width 8 are isospectral.
tags: [analysis, castle, spectral, isospectral, adjacency, laplacian, axis-9, kac, numpy, sympy, networkx, verification]
sources: [project-euler-502-castle-factoring]
created: 2026-09-16
updated: 2026-09-16
---

# Isospectral castles - hearing the shape of a castle

## The question

Kac asked whether one can hear the shape of a drum. For castles the drum is the polyomino graph of [[castle-classification](pages/castle-classification.md)] Axis 9 - filled cells as vertices, orthogonal neighbors as edges - and the question is whether two non-isomorphic castles can share a spectrum. [[spectral-analysis](pages/spectral-analysis.md)] predicted that pairs exist and asked how small the smallest is. This page answers it exactly, for the adjacency matrix and for the combinatorial Laplacian `L = D − A`.

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

### The smallest Laplacian-isospectral castles: 11 cells

```
class A: (1,1,1,2,1,1,2,1,1) and five more skylines      class B: (1,1,3,1,1,1,2,1)
...#..#..                                                 ..#.....
#########                                                 ..#...#.
                                                          ########
```

Common Laplacian characteristic polynomial `x¹¹ − 20x¹⁰ + 169x⁹ − 788x⁸ + 2223x⁷ − 3916x⁶ + 4295x⁵ − 2838x⁴ + 1051x³ − 188x² + 11x`. Both castles are **trees** (no two adjacent columns of height `≥ 2`, so no 4-cycles): a 9-cell base with two pendant cells, versus an 8-cell base with a 2-cell spike and a 1-cell spike. Laplacian cospectrality among trees is the classical situation (Schwenk: almost every tree has a cospectral mate), and the castle setting reproduces it at 11 cells.[^1]

### Isospectral for both operators: 16 cells

The first castles that agree in *both* the adjacency and the Laplacian spectrum have 16 cells; there is one such group, again a pair of trees, e.g. `(1,1,1,1,2,1,1,3,1,2,1,1)` versus `(1,1,1,1,3,1,2,1,1,2,1,1)` (eight skylines in each class).[^1]

### Silver-spectrum castles are not isospectral to each other

The spectral-radius census on [[castle-graph-spectral-radius](pages/castle-graph-spectral-radius.md)] found 36 castles with adjacency spectral radius `1 + √2` (all `w ≤ 8, h ≤ 7`; `w = 9, h ≤ 5`; `w = 10, h ≤ 4`), with 6 to 20 cells. Grouping them by cell count and full spectrum finds **no** two non-isomorphic silver castles with the same spectrum: sharing the top eigenvalue never extends to the whole spectrum in this range.[^2]

## What this settles and what it opens

- The seminar number: **10 cells** (adjacency), **11 cells** (Laplacian), **16 cells** (both). Each with a two-line drawing.
- Isospectral pairs are common from 12 cells on (50 adjacency groups at 16 cells), so "spectrum determines the castle" fails badly; the spectrum is an Axis 9 *invariant*, not a *classifier*.
- Open: the growth rate of the number of isospectral groups with `n`; whether the Ihara zeta or the skyline DFT separates the pairs found here; and whether a Sunada-type construction explains the 10-cell adjacency pair (both contain a `2×2` block with a 3-column attached).

## Appearances in Sources

- [[project-euler-502-castle-factoring](pages/project-euler-502-castle-factoring.md)] - the castle definition (column heights `≥ 1`, i.e. compositions) that makes "all castles with `n` cells" enumerable.

## Related Concepts

- [[spectral-analysis](pages/spectral-analysis.md)] - method 4 (combinatorial Laplacian) and the isospectral hunt this page runs.
- [[castle-classification](pages/castle-classification.md)] - Axis 9; isospectral pair is the pair predicate there.
- [[castle-graph-spectral-radius](pages/castle-graph-spectral-radius.md)] - the single-eigenvalue census (golden, silver, φ² castles) and the silver list checked here.
- [[castle-snippets](pages/castle-snippets.md)] - `compositions`, `castle_graph_radius`, and the spectrum-hashing loop.
- [[castle-representations](pages/castle-representations.md)] - the skyline encoding the enumeration runs on.

## Footnotes

[^1]: Verified by execution (NumPy, SymPy 1.14, networkx 3.4.2): all compositions of `n ≤ 16` with mirror dedupe (`c[::-1] < c` skipped), spectra rounded to 7 decimals for grouping, isomorphism classes by `networkx.is_isomorphic`, and exact `Matrix.charpoly` over the integers equal across classes for every group counted. Total 11 s. The per-`n` counts and the smallest groups' skylines and polynomials are as printed by the run.

[^2]: From the spectral-radius scan on [[castle-graph-spectral-radius](pages/castle-graph-spectral-radius.md)] (4,868,525 mirror-deduped castles): the 36 castles with spectral radius within `10⁻⁸` of `1 + √2`, grouped by cell count and rounded spectrum; every group with two or more skylines consisted of isomorphic graphs.
