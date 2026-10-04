---
title: The castle graph - bridge to graph theory
category: Concepts
summary: Every castle carries a graph - filled cells as vertices, orthogonal neighbors as edges. Basic invariants (|V| = area, cycle rank = number of 2×2 filled blocks, bipartite, planar, subgraph of Z^2, max degree 4) are read straight off the skyline. Named castle types from graph properties: **tree castle** (no 2×2 filled block), golden-, silver-, φ²-spectrum, isospectral pairs, Ramanujan. Tree-castle counts by width and height are Fibonacci at h = 2, Jacobsthal at h = 3, and the k-Fibonacci family A006130, A006131, … above; the growth constant is (1 + √(4h − 3))/2.
tags: [concept, castle, graph, polyomino, spectral, adjacency, laplacian, tree, bipartite, planar, cycle-rank, fibonacci, jacobsthal, oeis, bridge, pedagogy]
sources: [project-euler-502-castle-factoring]
created: 2026-09-17
updated: 2026-10-04
---

# The castle graph - bridge to graph theory

## Definition

Fix a castle with skyline `c = (c_1, …, c_w)`, `c_i ≥ 1`. Its **castle graph** `G_c` has

- **vertices** = the filled cells `(i, j)` with `1 ≤ i ≤ w` and `1 ≤ j ≤ c_i`,
- **edges** = pairs of cells sharing a unit side, i.e. `(i, j) ↔ (i, j+1)` (vertical, within a column) and `(i, j) ↔ (i+1, j)` (horizontal, between columns) whenever both endpoints are filled.

That is the whole definition. Six examples from around the wiki:

```
(4)          (1,1,1,1)      (3,3)          (2,2,2)             (1,3,2,3,1)      (1,1,2,1,1,2,1,1)
#             ####          ##             ###                                  
#                           ##             ###                 .#.#.
#                           ##                                 .###.            ...#..#..
#                                                              #####            #########
```

## Basic invariants, read off the skyline

The basic invariants of `G_c` are small formulas in `c`.[^1]

| invariant | formula |
|---|---|
| vertex count `\|V\|` | area = `Σ c_i` |
| vertical edges (within columns) | `Σ (c_i − 1) = |V| − w` |
| horizontal edges (between columns) | `Σ_{i < w} min(c_i, c_{i+1})` |
| edge count `\|E\|` | `\|V\| − w + Σ_{i < w} min(c_i, c_{i+1})` |
| number of 2×2 filled blocks | `Σ_{i < w} max(0, min(c_i, c_{i+1}) − 1)` |
| cycle rank `\|E\| − \|V\| + 1` (first Betti number) | **= number of 2×2 filled blocks** |
| max degree `Δ` | at most 4 |
| bipartite? | always (color `(i, j)` by parity of `i + j`) |
| planar? | always (drawn on `Z²` with no crossings) |

**Cycle rank.** `G_c` is a planar graph whose bounded faces in the grid embedding are exactly the fully-filled unit squares; each such square contributes one independent cycle, and the total is `|E| − |V| + 1` by Euler. Verified for every castle with `w ≤ 4, h ≤ 4`.[^1] The block loops are also an integer basis of the cycle lattice on all 938 castles tested ([[sandpile-census](pages/sandpile-census.md)] §1), which is why the sandpile group can be read off the blocks ([[sandpile-group](pages/sandpile-group.md)] Part 3).

**A castle graph is a tree iff it has no 2×2 filled block**, equivalently, no two horizontally adjacent columns both have height at least 2.

## Named castle types from graph properties

The castle graph turns each Axis 9 predicate on [[castle-classification-spectrum](pages/castle-classification-spectrum.md)] into a graph property:

| type | graph condition | wiki page |
|---|---|---|
| **Tree castle** | `G_c` is a tree; no 2×2 filled block | this page (section below), Axis 9 |
| **Golden-spectrum castle** | adjacency spectral radius = `φ` | [[castle-graph-spectral-radius](pages/castle-graph-spectral-radius.md)] |
| **Silver-spectrum castle** | adjacency spectral radius = `1 + √2` | [[castle-graph-spectral-radius](pages/castle-graph-spectral-radius.md)] |
| **φ²-spectrum castle** | adjacency spectral radius = `φ² = (3+√5)/2` | [[castle-graph-spectral-radius](pages/castle-graph-spectral-radius.md)] |
| **Isospectral pair** | two non-isomorphic castles with equal adjacency or Laplacian spectrum | [[isospectral-castles](pages/isospectral-castles.md)] |
| **Ramanujan castle** | every eigenvalue other than `±λ_1` has modulus `≤ ρ(T)`, the spectral radius of the castle graph's universal covering tree (Greenberg's definition for irregular graphs); trivially true for tree castles | [[castle-classification-spectrum](pages/castle-classification-spectrum.md)] Axis 9 |

Sparse-spectrum, low-pass / high-pass and Ihara-Ramanujan types are defined on Axis 9 without members; populating them needs the skyline discrete Fourier transform (DFT) and the Ihara zeta.

## Tree castles

A **tree castle** is a castle whose graph is a tree: connected, `|V| = |E| + 1`, no cycles. Equivalent to "no 2×2 filled block" and to "no two horizontally adjacent columns both `≥ 2`." Small examples:

- `(1, 1, 1, …, 1)` for any `w`, drawn as a horizontal path `P_w`.
- `(h)` for any `h ≥ 1`, drawn as a vertical path `P_h`.
- `(2, 1, 2, 1, 2)`, three vertical 2-spikes on a common base.
- `(1, 3, 1)`, a T-shape.
- `(1, 1, 1, 2, 1, 1, 2, 1, 1)`, the 11-cell tree from the isospectral pair on [[isospectral-castles](pages/isospectral-castles.md)].

Non-examples: `(2, 2)`, `(3, 3)`, `(1, 2, 3, 1, 2, 3)` all contain `2×2` blocks and are therefore not trees.

A tree castle has exactly one spanning tree, so its sandpile group is trivial in both the sink and the tide model, and the identity is the fullest stable pile. Up to 16 cells there are 6,963 tree castles, mirror images removed ([[sandpile-census](pages/sandpile-census.md)], [[sandpile-identity](pages/sandpile-identity.md)]).

### Counting tree castles: Fibonacci, Jacobsthal, and the k-Fibonacci family

Fix a height bound `h`. Let `T_h(w)` be the number of skylines `(c_1, …, c_w) ∈ {1, …, h}^w` in which no two adjacent columns both have height `≥ 2`. Split by whether the last column is "short" (`c_w = 1`) or "tall" (`c_w ≥ 2`, `h − 1` choices):

```
T_h(w+2)  =  T_h(w+1)  +  (h − 1) · T_h(w),        T_h(0) = 1,   T_h(1) = h.
```

Characteristic polynomial `x² − x − (h − 1)`, growth constant

```
ρ(h)  =  (1 + √(4h − 3)) / 2.
```

| `h` | `T_h(w)`, `w = 0..9` | growth `ρ(h)` | Online Encyclopedia of Integer Sequences (OEIS) | recurrence |
|---|---|---|---|---|
| 1 | `1, 1, 1, 1, 1, 1, 1, 1, 1, 1` | `1` | (constant) | trivial |
| 2 | `0, 1, 2, 4, 7, 12, 20, 33, 54, 88` | **`φ`** (golden, `δ_1`) | **A000071** (`F_{w+2} − 1`, the term `A000071(w+2)`) | `a(n) = a(n−1) + a(n−2) + 1` |
| 3 | `1, 3, 5, 11, 21, 43, 85, 171, 341, 683` | `2` (integer) | **A001045** (Jacobsthal, `T_3(w) = J_{w+2}`) | `a(n) = a(n−1) + 2 a(n−2)` |
| 4 | `1, 4, 7, 19, 40, 97, 217, 508, 1159, 2683` | `(1 + √13)/2 = 2.303` | **A006130** (`T_4(w) = a(w+1)`) | `a(n) = a(n−1) + 3 a(n−2)` |
| 5 | `1, 5, 9, 29, 65, 181, 441, 1165, 2929, 7589` | `(1 + √17)/2 = 2.562` | **A006131** | `a(n) = a(n−1) + 4 a(n−2)` |

The `h = 2` row counts the tree castles of height 2 (some column reaches height 2), the Fibonacci castles; the rows `h ≥ 3` are `T_h(w)`. All OEIS numbers verified offset-exact.[^2]

- **The `h = 2` row is Fibonacci minus one.** The tree castles of height 2 are the Fibonacci castles ([[fibonacci-castle](pages/fibonacci-castle.md)]), `F_{w+2} − 1` of width `w`, a castle interpretation of `A000071`. It sits next to the prime-castle count `F_{n−1}` on [[prime-castles](pages/prime-castles.md)] as another point where Fibonacci enters the castle count, and it puts the tree-castle family on rung 1 of the [[metallic-means](pages/metallic-means.md)] ladder ([[castle-classification](pages/castle-classification.md)] Axis 8: tree castles of height 2 are a **golden width growth castle**).
- **The `h = 3` slice is Jacobsthal**, a castle interpretation of `A001045`. Heights 4 and 5 give `A006130` and `A006131`, and every height `h` gives a member of the "`k`-Fibonacci" family `a(n) = a(n−1) + k · a(n−2)` with `k = h − 1`. None of these growth constants for `h ≥ 3` is a metallic mean, so tree castles trace out a distinct algebraic family from the metallic one, indexed by `h`.

The area-graded (q-analogue) count is worked out on [[tree-castle-by-area](pages/tree-castle-by-area.md)]: the bivariate generating function (GF) is `T_h(x, q) = (1 + P_h(q) x)/(1 − q x − q P_h(q) x²)`, summing over widths gives one C-finite sequence per height, and each hits a named OEIS sequence - at `h = 2` the tree castles of height 2 with area `A` number `A000930(A + 1) − 1` (Narayana's cows minus one), the term `A077868(A − 2)` (supergolden growth), `h = 3` is A006498 (golden growth via factorization), `h = 4` is A000570 (tournaments), `h → ∞` is A005251 (plastic squared, a second castle interpretation).

## Bipartiteness, planarity, treewidth: what the castle graph inherits

- **Bipartite.** Color `(i, j)` by the parity of `i + j`. Adjacent cells differ in exactly one coordinate by 1, so they get opposite colors. Consequence: the adjacency spectrum is symmetric about 0. Every eigenvalue `λ` is paired with `−λ`, which is visible in every exact characteristic polynomial on [[castle-graph-spectral-radius](pages/castle-graph-spectral-radius.md)] (e.g. `(x² − x − 1)(x² + x − 1)` for `P_4`).
- **Planar and subgraph of `Z²`.** Every castle graph embeds in the square lattice with unit edges, so planar-graph results apply: Euler's formula (used above) and planar separators.
- **Bounded pathwidth.** A castle graph is a subgraph of the `w × h` grid, so its pathwidth is at most `min(w, h)`, and bounded-treewidth algorithms run in polynomial time on castles with `min(w, h)` fixed.

## Graph theory on castles

- **Spectral graph theory.** Adjacency, Laplacian, normalized Laplacian, signless Laplacian, and Ihara zeta all live on `G_c`. See [[spectral-analysis](pages/spectral-analysis.md)] for the methods and [[castle-graph-spectral-radius](pages/castle-graph-spectral-radius.md)] / [[isospectral-castles](pages/isospectral-castles.md)] for two settled applications.
- **Extremal graph theory.** The maximum spectral radius of a castle graph with `n` cells is a Turán-type problem.
- **Algebraic graph theory.** Because `G_c` is bipartite and planar, Kasteleyn's method counts its perfect matchings (dimer coverings). Planarity also gives the critical group through the planar dual, whose vertices are the `2 × 2` blocks ([[sandpile-group](pages/sandpile-group.md)]); the dual-graph theorem is Cori and Rossin's, reached on the wiki through [[rossin-2000-group-of-a-sandpile](pages/rossin-2000-group-of-a-sandpile.md)].
- **Random graphs.** Random castles under any of the wiki's ensembles ([[spectral-analysis](pages/spectral-analysis.md)] method 2, Lindstrom-Gessel-Viennot (LGV) kernel) become a random-graph model whose spectra can be sampled.
- **Sunada theory** (see [[isospectral-castles](pages/isospectral-castles.md)]) for common covers and the "hear the shape" question.

The [[castle-graph-spectral-radius](pages/castle-graph-spectral-radius.md)], [[isospectral-castles](pages/isospectral-castles.md)], [[ramanujan-castles](pages/ramanujan-castles.md)], the sandpile pages from [[sandpile-group](pages/sandpile-group.md)] on, and the tree-castle count above are the pages that use the castle graph.

## Snippet index

Filed on [[castle-snippets](pages/castle-snippets.md)]:

```python
def castle_graph(c):
    """Adjacency matrix of the castle graph as a NumPy array."""
    cells = [(i, j) for i, h in enumerate(c) for j in range(h)]
    idx = {cell: n for n, cell in enumerate(cells)}
    A = np.zeros((len(cells), len(cells)))
    for (i, j), u in idx.items():
        for nb in ((i+1, j), (i, j+1)):
            if nb in idx: A[u, idx[nb]] = A[idx[nb], u] = 1
    return A

def is_tree_castle(c):
    """True iff G_c is a tree - equivalently, no 2x2 filled block."""
    return all(not (c[i] >= 2 and c[i+1] >= 2) for i in range(len(c)-1))

def cycle_rank(c):
    """|E| - |V| + 1 = number of 2x2 filled blocks in the castle."""
    return sum(max(0, min(c[i], c[i+1]) - 1) for i in range(len(c)-1))
```

## Appearances in Sources

- [[project-euler-502-castle-factoring](pages/project-euler-502-castle-factoring.md)] - the castle definition (skyline, filled-cell picture) that this graph reads off.

## Related Concepts

- [[castle-classification-spectrum](pages/castle-classification-spectrum.md)] - Axis 9 is spectral predicates on this graph.
- [[castle-graph-spectral-radius](pages/castle-graph-spectral-radius.md)] - single-eigenvalue types on this graph (golden, silver, φ²).
- [[isospectral-castles](pages/isospectral-castles.md)] - Kac's question on this graph; the smallest Laplacian-isospectral pair is a pair of tree castles.
- [[spectral-analysis](pages/spectral-analysis.md)] - the methods hub for spectra on this graph.
- [[castle-polyomino](pages/castle-polyomino.md)] - the underlying object, dropping the graph reading.
- [[castle-representations](pages/castle-representations.md)] - other encodings; the castle graph is a further encoding, into `Z²`-subgraphs.
- [[castle-by-area](pages/castle-by-area.md)] - `|V|` is area; the graph reading dualizes area-graded questions into vertex-graded ones.
- [[castle-classification-growth](pages/castle-classification-growth.md)] Axis 8 - the tree-castle golden growth constant sits on rung 1 of the metallic ladder for height 2.
- [[metallic-means](pages/metallic-means.md)] - the tree-castle `h = 2` growth `φ` lands here.
- [[castle-snippets](pages/castle-snippets.md)] - `castle_graph`, `is_tree_castle`, `cycle_rank`.
- [[unique-tournament](pages/unique-tournament.md)] - the wiki's other graph-theoretic object (complete oriented graphs, where castle graphs are sparse bipartite grids); the two meet at `A000570`, the `h = 4` tree-castle count by area.
- [[castle-eigenvalues-by-example](pages/castle-eigenvalues-by-example.md)] - the from-scratch pedagogy that computes by hand the small golden / silver / `φ²`-spectrum castles this page's Named-castle-types table tabulates.
- [[hear-the-shape-seminar](pages/hear-the-shape-seminar.md)] - the seminar built on this graph: what its spectrum hears and the smallest failures.
- [[sandpile-group](pages/sandpile-group.md)] - the sandpile group: the 2×2 blocks that make the cycle rank also hold all the sand; tree castles hold none.
- [[sandpile-census](pages/sandpile-census.md)] - the census of sandpile groups; 6,963 of the 33,150 castles to 16 cells are tree castles with trivial group.
- [[castle-avalanches](pages/castle-avalanches.md)] - battlements and rectangles have the same mean avalanche; the 2×2 blocks set the tail.
- [[rossin-2000-group-of-a-sandpile](pages/rossin-2000-group-of-a-sandpile.md)] - source for the sandpile group of a graph, its sink independence, and the dual-graph theorem the block matrices rest on.

## Footnotes

[^1]: Verified by execution (Python 3.11, NumPy, SymPy 1.14): for every castle skyline with `w ≤ 4` and `h ≤ 4` (`max c = h`), `|E| − |V| + 1` equals `Σ_{i<w} max(0, min(c_i, c_{i+1}) − 1)` (the count of 2×2 filled blocks). Basic invariants recomputed against direct enumeration.

[^2]: Verified against OEIS (fetched 2026-09-17): tree-castle counts `T_h(w)` for `w = 0..11` compared to https://oeis.org/A001045 (Jacobsthal) at `h = 3`, https://oeis.org/A006130 (`a(n) = a(n-1) + 3 a(n-2)`) at `h = 4`, https://oeis.org/A006131 (`a(n) = a(n-1) + 4 a(n-2)`) at `h = 5`. All offset-exact. The `h = 2` row, the tree castles of height 2, verified 2026-10-04 by brute force for `w = 0..10` against https://oeis.org/A000071 (offset 1, data `0, 0, 1, 2, 4, 7, 12, 20, 33, 54, 88, 143`), the term `A000071(w+2)`. Growth constants `(1 + √(4h − 3))/2` verified numerically as `ρ(h) = 1, φ, 2, 2.303, 2.562, 2.791` for `h = 1..6`.
