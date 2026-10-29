---
title: The castle graph - bridge to graph theory
category: Concepts
summary: The castle graph of a castle has its cells as vertices and an edge between cells that share a side. It is connected, bipartite and planar, with at most 4 neighbors per cell, and its cycle rank is the number of 2×2 squares of cells, whose boundary cycles are an integer basis of the cycle lattice of every castle, in the sink and tide models. It is a tree exactly when no two neighboring columns both have height at least 2; these tree castles number F_{w+2} − 1 at height 2, and the tree skylines of height at most h satisfy T_h(w+2) = T_h(w+1) + (h−1)T_h(w), Jacobsthal at h = 3, so the tree castles of height h grow like σ_1^{h−1} = (1 + √(4h−3))/2 by width. A tree castle with n cells has 1 + n − w blocks, so its even-block and odd-block counts differ by (−1)^h(1 − P_F(w)), of period 6 in the width at every height; up to mirror image, 6,963 of the 33,150 castles with at most 16 cells are tree castles.
tags: [concept, castle, graph, polyomino, spectral, adjacency, laplacian, tree, bipartite, planar, cycle-rank, fibonacci, jacobsthal, oeis, bridge, pedagogy, cycle-lattice, parity, burnside, padovan]
sources: [project-euler-502-brute-force, rossin-2000-group-of-a-sandpile]
created: 2026-09-17
updated: 2026-10-29
---

# The castle graph - bridge to graph theory

## Definition

Let `c = (c_1, …, c_w)` be the skyline of a castle ([[castle-polyomino](pages/castle-polyomino.md)]). Its **castle graph** `G_c` has

- as vertices the cells `(i, j)` with `1 ≤ i ≤ w` and `1 ≤ j ≤ c_i`, column `i` and row `j`;
- as edges the pairs of cells that share a side: `(i, j)` and `(i, j+1)` in one column, and `(i, j)` and `(i+1, j)` in neighboring columns, whenever both cells are in the castle.

Six castles, drawn row by row from the top with `#` for a cell:

```
(4)     (1,1,1,1)    (3,3)    (2,2,2)    (1,3,2,3,1)    (1,1,2,1,1,2,1,1)
#
#                    ##                  .#.#.
#                    ##       ###        .###.          ..#..#..
#       ####         ##       ###        #####          ########
```

The skylines `(4)` and `(1, 1, 1, 1)` have the path on 4 vertices as their graph. `(3, 3)` and `(2, 2, 2)` have 6 cells, 7 edges and two `2 × 2` squares. `(1, 3, 2, 3, 1)` has 10 cells, 11 edges and two `2 × 2` squares, and `(1, 1, 2, 1, 1, 2, 1, 1)` has 10 cells, 9 edges and none.[^1]

## Invariants of the skyline

| invariant | value |
|---|---|
| vertices `\|V\|` | the area `Σ c_i` |
| edges within columns | `Σ_i (c_i − 1) = \|V\| − w` |
| edges between columns | `Σ_{i<w} min(c_i, c_{i+1})` |
| `2 × 2` squares of cells | `Σ_{i<w} (min(c_i, c_{i+1}) − 1)` |
| cycle rank `\|E\| − \|V\| + 1` | the number of `2 × 2` squares |
| largest degree | at most 4 |

The graph is connected, since every column stands on row 1, which is a path. So its cycle rank, the number of independent cycles, is `|E| − |V| + 1`. Adding the two kinds of edges, `|E| − |V| + 1 = Σ_{i<w} min(c_i, c_{i+1}) − (w − 1) = Σ_{i<w} (min(c_i, c_{i+1}) − 1)`, the number of `2 × 2` squares, since two neighboring columns share `min(c_i, c_{i+1}) − 1` of them.

The graph is **bipartite**: coloring `(i, j)` by the parity of `i + j` gives neighboring cells opposite colors. So its adjacency spectrum is symmetric about 0; the path on 4 vertices has characteristic polynomial `x⁴ − 3x² + 1 = (x² − x − 1)(x² + x − 1)`. The graph is **planar**, drawn in the square lattice with unit edges, and it is a subgraph of the `w × h` grid graph, so its pathwidth is at most `min(w, h)`.

## Planarity and the cycle lattice

Every column stands on row 1, so a castle has no holes: a lattice point enclosed by a cycle of the drawing has a cell of that cycle above it in its column, and so is a cell itself. The bounded faces of the drawing are exactly the `2 × 2` squares, and Euler's formula `|V| − |E| + f = 2`, with `f` the number of faces including the unbounded one, gives the cycle rank `|E| − |V| + 1 = f − 1` as the number of squares a second time.

**The `2 × 2` squares are an integer basis of the cycles.** The **cycle lattice** of the graph is the set of integer flows on its edges, each edge given a direction, with net flow 0 at every cell. For `1 ≤ k < min(c_i, c_{i+1})`, let `Q_{i,k}` be the boundary cycle, run counterclockwise, of the square on the cells `(i, k)`, `(i+1, k)`, `(i, k+1)` and `(i+1, k+1)`. For every castle, the `Q_{i,k}` are an integer basis of the cycle lattice: every integer cycle is a combination of them with integer coefficients, in exactly one way.

*Proof.*

- *Comb.* The edges within columns and the edges of row 1 form a spanning tree `T`, a comb whose teeth are the columns: it reaches every cell and has `(|V| − w) + (w − 1) = |V| − 1` edges.
- *Rectangles.* The edges outside `T` are the edges `e_{i,j}` from `(i, j)` to `(i+1, j)` with `2 ≤ j ≤ min(c_i, c_{i+1})`, one for each square, the one along its top, which gives the cycle rank a third time. Adding `e_{i,j}` to `T` closes the boundary cycle `Z_{i,j}` of the rectangle of rows `1, …, j` over columns `i` and `i + 1`. Run counterclockwise, it is the sum of the squares below `e_{i,j}`, since each edge between two of them is run once in each direction:

  ```
  Z_{i,j}  =  Q_{i,1} + Q_{i,2} + ⋯ + Q_{i,j−1}.
  ```

- *Basis.* Let `z` be an integer cycle and `z_{i,j}` its flow along `e_{i,j}` in the direction `Z_{i,j}` runs it. Then `z − Σ z_{i,j} Z_{i,j}` is a cycle carried by `T`, and it is 0, since a nonzero flow on a tree has nonzero net flow at a leaf of its support. So the `Z_{i,j}` are an integer basis. The relation for `Z_{i,j}` and its inverse, `Q_{i,1} = Z_{i,2}` and `Q_{i,k} = Z_{i,k+1} − Z_{i,k}` for `k ≥ 2`, have integer coefficients, so the `Q_{i,k}` are an integer basis too.

The same proof works in the tide model of [[sandpile-group](pages/sandpile-group.md)], where the bottom row is merged into one sink `s` and the edges inside row 1 disappear. The edges within columns form the spanning tree, each column hanging from `s`; the edges outside it are again the `e_{i,j}`; and the cycle of a square on row 1 becomes the triangle through `s`, `(i, 2)` and `(i+1, 2)`, which takes the place of `Q_{i,1}` in the relation for `Z_{i,j}`. So the squares are an integer basis in both models, and [[sandpile-group](pages/sandpile-group.md)] computes the sandpile group from them; [[sandpile-census](pages/sandpile-census.md)] confirms it on every castle with at most 16 cells.[^2]

**The planar dual and matchings.** The graph is planar, so Kasteleyn's method counts its perfect matchings, and [[sandpile-group](pages/sandpile-group.md)] computes the sandpile group from the planar dual, which has a vertex for each `2 × 2` square and one for the outer face. For the castle `(3, 3, 3)` the dual is the `2 × 2` grid of [[rossin-2000-group-of-a-sandpile](pages/rossin-2000-group-of-a-sandpile.md)], each cell joined twice to the sink, and both have the group `Z/24 × Z/8`.

## Tree castles

A **tree castle** is a castle whose graph is a tree. Since the graph is connected, this holds exactly when the cycle rank is 0: when there is no `2 × 2` square of cells, that is, when no two neighboring columns both have height at least 2. Examples are the skyline `(1, 1, …, 1)`, a horizontal path; the skyline `(h)`, a vertical path; `(2, 1, 2, 1, 2)`; `(1, 3, 1)`; and the 11-cell skyline `(1, 1, 1, 2, 1, 1, 2, 1, 1)` of [[isospectral-castles](pages/isospectral-castles.md)]. The skylines `(2, 2)`, `(3, 3)` and `(1, 2, 3, 1, 2, 3)` are not tree castles.

A tree castle has exactly one spanning tree, so its sandpile group is trivial in both the sink model and the tide model of [[sandpile-group](pages/sandpile-group.md)]; in the tide model the bottom row is contracted to one sink, which leaves a tree.

### Counting tree castles by width

Let `T_h(w)` be the number of **tree skylines** of width `w` and height at most `h`: skylines in `{1, …, h}^w` in which no two neighboring columns both have height at least 2. A tree skyline need not reach height `h`, so it is not a castle of height `h`. Splitting by the last column, which has height 1 or is one of the `h − 1` taller heights after a column of height 1,

```
T_h(w+2)  =  T_h(w+1)  +  (h − 1)·T_h(w),        T_h(0) = 1,   T_h(1) = h.        (1)
```

The tree skylines are the strips of the rule that allows a pair of neighboring heights when one of them is 1. By the Hilbert duality of [[hilbert-castles](pages/hilbert-castles.md)] they are determined by the dual rule, whose strips have every column at height at least 2, and the duality gives their generating function `Σ_{w≥0} T_h(w) x^w = (1 + (h − 1)x)/(1 − x − (h − 1)x²)`, and, with `q` marking area, the generating function by area and width given below.

The tree castles of width `w` and height `h` are the tree skylines of height at most `h` that are not of height at most `h − 1`, so they number

```
A_tree(w, h)  =  T_h(w) − T_{h−1}(w).                                              (2)
```

The characteristic polynomial of Equation (1) is `x² − x − (h − 1)`, whose larger root is

```
σ_1^{h−1}  =  (1 + √(4h − 3)) / 2,
```

de Spinadel's metallic mean with `p = 1` and `q = h − 1` ([[de-spinadel-1999-family-of-metallic-means](pages/de-spinadel-1999-family-of-metallic-means.md)], [[metallic-means](pages/metallic-means.md)]). For `h ≥ 2` it exceeds `σ_1^{h−2}`, so `A_tree(w, h)` grows like `(σ_1^{h−1})^w` too: the tree castles of heights 2, 3 and 4 are golden (`φ`), copper (`2`) and nickel (`(1 + √13)/2`) by width.

| `h` | `T_h(w)` for `w = 0, 1, …, 9` | OEIS | `σ_1^{h−1}` |
|---|---|---|---|
| 1 | `1, 1, 1, 1, 1, 1, 1, 1, 1, 1` | | `1` |
| 2 | `1, 2, 3, 5, 8, 13, 21, 34, 55, 89` | Fibonacci, `F_{w+2}` | `φ = 1.618…` |
| 3 | `1, 3, 5, 11, 21, 43, 85, 171, 341, 683` | Jacobsthal, `A001045(w+2)` | `2` |
| 4 | `1, 4, 7, 19, 40, 97, 217, 508, 1159, 2683` | `A006130(w+1)` | `(1 + √13)/2 = 2.303…` |
| 5 | `1, 5, 9, 29, 65, 181, 441, 1165, 2929, 7589` | `A006131(w+1)` | `(1 + √17)/2 = 2.562…` |

| `h` | `A_tree(w, h)` for `w = 0, 1, …, 8` |
|---|---|
| 2 | `0, 1, 2, 4, 7, 12, 20, 33, 54` |
| 3 | `0, 1, 2, 6, 13, 30, 64, 137, 286` |
| 4 | `0, 1, 2, 8, 19, 54, 132, 337, 818` |

Every entry agrees with brute-force enumeration.[^3] At height 2, `T_1(w) = 1`, so `A_tree(w, 2) = F_{w+2} − 1 = A000071(w+2)`: these are the Fibonacci castles, the castles of height 2 with no two neighboring columns of height 2 ([[fibonacci-castle](pages/fibonacci-castle.md)]). The sequences `A006130` and `A006131` satisfy `a(n) = a(n−1) + 3a(n−2)` and `a(n) = a(n−1) + 4a(n−2)`, the cases `h = 4` and `h = 5` of Equation (1).

[[tree-castle-by-area](pages/tree-castle-by-area.md)] counts the tree skylines by area. With `q` marking area, `x` marking width and `P_h(q) = q² + q³ + ⋯ + q^h`, their generating function is `(1 + P_h(q)x)/(1 − qx − qP_h(q)x²)`, since a tree skyline is a sequence of columns of height 1, each followed or not by one taller column. At `x = 1`, the tree castles of height 2 counted by area are `A077868`, one less than Narayana's cows `A000930`; the tree skylines of height at most 3 and 4 are `A006498` and `A000570`; and the tree skylines of any height are `A005251`.[^4]

### Blocks and parity

Project Euler 502 counts the castles with an even number of blocks, the maximal horizontal runs of cells in each row ([[castle-notation](pages/castle-notation.md)]). The bottom row of a tree castle is one block, and every cell above it is a block by itself, since the neighbors of its column have height 1. So a tree castle with `n` cells and width `w` has

```
blocks  =  1 + n − w,                                                              (3)
```

and in the generating function of the tree skylines by area and width, setting `q = −1`, replacing `x` by `−x` and changing the sign gives the signed count `Σ (−1)^{blocks}` of the tree skylines of height at most `h` by width:

```
−(1 − P_h(−1)·x) / (1 − x + P_h(−1)·x²),        P_h(−1) = 1 for even h,  0 for odd h.
```

For odd `h` this is `−1/(1 − x)`, so the signed count is `−1` at every width. For even `h` it is `−(1 − x)/(1 − x + x²)`, minus the generating function of the signed Fibonacci tower count `P_F(w)` of [[fibonacci-castle](pages/fibonacci-castle.md)], of period 6. A pairing gives both. For odd `h`, pair the heights 2 and 3, 4 and 5, …, `h − 1` and `h`; for even `h`, pair 3 and 4, …, `h − 1` and `h`, and leave 2 unpaired. Moving the leftmost column whose height is paired to the other height of its pair changes the area by 1 and keeps the skyline a tree skyline, so by Equation (3) it matches tree skylines of opposite parity. What is left over is the flat row for odd `h`, and for even `h` the tree skylines whose columns all have height 1 or 2.

Subtracting the tree skylines of height at most `h − 1` leaves the tree castles of height `h`:

```
S_tree(w, h)  =  A^e_tree(w, h) − A^o_tree(w, h)  =  (−1)^h · (1 − P_F(w)),        h ≥ 2.        (4)
```

So at every height the even-block and odd-block tree castles differ by `1 − P_F(w) = 1, 2, 2, 1, 0, 0` for `w = 1, …, 6`, repeating with period 6; the even-block ones are ahead at even heights and the odd-block ones at odd heights. At `h = 2`, Equation (4) is the `S_Fib(w) = 1 − P_F(w)` of [[fibonacci-castle](pages/fibonacci-castle.md)]. The Project Euler count of the tree castles of height `h` is `A^e_tree(w, h) = (A_tree(w, h) + S_tree(w, h))/2`.

| `h` | count | `w = 1` | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|---|---|---|
| 2 | `A^e_tree` | 1 | 2 | 3 | 4 | 6 | 10 | 17 | 28 |
| 2 | `A^o_tree` | 0 | 0 | 1 | 3 | 6 | 10 | 16 | 26 |
| 3 | `A^e_tree` | 0 | 0 | 2 | 6 | 15 | 32 | 68 | 142 |
| 3 | `A^o_tree` | 1 | 2 | 4 | 7 | 15 | 32 | 69 | 144 |
| 4 | `A^e_tree` | 1 | 2 | 5 | 10 | 27 | 66 | 169 | 410 |
| 4 | `A^o_tree` | 0 | 0 | 3 | 9 | 27 | 66 | 168 | 408 |

Every entry agrees with brute-force enumeration.[^5]

The period belongs to the tree castles. Over all castles the signed count grows: `S(w, 2) = 1 − Re((1 + i)^{w+1})`, with `i² = −1`, grows like `2^{w/2}` ([[fibonacci-castle](pages/fibonacci-castle.md)]), and `S(w, 3) = −1, −5, −13, −23, −33, −51, −105, −243, −529` for `w = 1, …, 9`. The difference comes from Equation (3): the parity of a tree castle is a sum over its columns, which lets the tall heights cancel in pairs.

### Up to mirror image

Reversing a skyline gives its mirror image, which has the same castle graph. By Burnside's lemma for the two-element group of the identity and the reversal, a set of skylines closed under reversal has half as many mirror-image classes as its size plus its number of palindromes, the skylines equal to their mirror image. By area `n`:

- the skylines of area `n` are the compositions of `n`, `2^{n−1}` of them, and `2^{⌊n/2⌋}` are palindromes, the symmetric compositions `A016116`;
- the tree skylines of area `n` number `A005251(n + 2)`, and the palindromic ones `A000931(n + 6)`, Padovan numbers, with generating function `x(1 + x)²/(1 − x² − x³)` ([[padovan-families](pages/padovan-families.md)]).

So up to mirror image,

```
castles of area n       :  (2^{n−1} + 2^{⌊n/2⌋}) / 2,
tree castles of area n  :  (A005251(n + 2) + A000931(n + 6)) / 2.
```

The first is `A005418(n)`, the compositions of `n` up to direction. The second is `A005683(n + 2)`, the Twopins positions, whose OEIS entry gives the same formula, and it is the trivial-group column of [[sandpile-census](pages/sandpile-census.md)].

| skylines up to mirror image | area `n = 1, 2, …, 16` | `n ≤ 16` |
|---|---|---|
| all | `1, 2, 3, 6, 10, 20, 36, 72, 136, 272, 528, 1056, 2080, 4160, 8256, 16512` | 33,150 |
| tree | `1, 2, 3, 5, 8, 13, 22, 37, 63, 108, 186, 322, 559, 973, 1697, 2964` | 6,963 |

The sums are the 33,150 castles of [[sandpile-census](pages/sandpile-census.md)] and the 6,963 tree castles among them, the castles whose sandpile groups are trivial in both models. Every entry agrees with brute-force enumeration.[^6]

## Spectral types

The spectral types of [[castle-classification-spectrum](pages/castle-classification-spectrum.md)] are properties of the castle graph:

| type | condition on `G_c` | page |
|---|---|---|
| tree castle | `G_c` is a tree | this page, section *Tree castles* |
| golden by spectrum | the largest adjacency eigenvalue is the golden mean `φ = (1 + √5)/2`; the castle `(1, 1, 1, 1)` is one | [[castle-graph-spectral-radius](pages/castle-graph-spectral-radius.md)] |
| silver by spectrum | the largest adjacency eigenvalue is the silver mean `1 + √2`; the castle `(2, 2, 2)` is one | [[castle-graph-spectral-radius](pages/castle-graph-spectral-radius.md)] |
| spectral radius `φ²` | the largest adjacency eigenvalue is `φ² = (3 + √5)/2` | [[castle-graph-spectral-radius](pages/castle-graph-spectral-radius.md)] |
| isospectral pair | two castles with non-isomorphic graphs and the same adjacency or Laplacian spectrum | [[isospectral-castles](pages/isospectral-castles.md)] |
| Ramanujan castle | every adjacency eigenvalue other than `±λ_1` has modulus at most `ρ(T)`, the spectral radius of the universal covering tree of `G_c` (Greenberg's condition for irregular graphs) | [[ramanujan-castles](pages/ramanujan-castles.md)] |

Here `λ_1` is the largest adjacency eigenvalue. A finite tree is its own universal cover, so every tree castle is a Ramanujan castle.

## Snippet

Filed on [[castle-snippets](pages/castle-snippets.md)]:

```python
import numpy as np

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
    """True iff G_c is a tree - equivalently, no 2x2 square of cells."""
    return all(not (c[i] >= 2 and c[i+1] >= 2) for i in range(len(c)-1))

def cycle_rank(c):
    """|E| - |V| + 1 = number of 2x2 squares of cells in the castle."""
    return sum(max(0, min(c[i], c[i+1]) - 1) for i in range(len(c)-1))
```

## Appearances in Sources

- [[project-euler-502-brute-force](pages/project-euler-502-brute-force.md)] - the skyline encoding of a castle, whose cells are the vertices of the castle graph.
- [[rossin-2000-group-of-a-sandpile](pages/rossin-2000-group-of-a-sandpile.md)] - the sandpile group of a graph and the dual-graph theorem.

## Related Concepts

- [[konigsberg-castles](pages/konigsberg-castles.md)] - the castle graph with a ground vertex joined to the bottom row: the castles whose every degree is even, and those with exactly two odd vertices.
- [[castle-classification-spectrum](pages/castle-classification-spectrum.md)] - the classification of castles by the spectrum of the castle graph.
- [[castle-graph-spectral-radius](pages/castle-graph-spectral-radius.md)] - the castles whose graph has spectral radius `φ`, `1 + √2` or `φ²`.
- [[isospectral-castles](pages/isospectral-castles.md)] - non-isomorphic castle graphs with the same spectrum; the smallest Laplacian pair is two tree castles with 11 cells.
- [[ramanujan-castles](pages/ramanujan-castles.md)] - Greenberg's Ramanujan condition on castle graphs, with a census to 22 cells.
- [[castle-eigenvalues-by-example](pages/castle-eigenvalues-by-example.md)] - the adjacency matrices and characteristic polynomials of small castle graphs, worked by hand.
- [[hear-the-shape-seminar](pages/hear-the-shape-seminar.md)] - a seminar on what the spectrum of the castle graph determines.
- [[spectral-analysis](pages/spectral-analysis.md)] - the spectral methods used on castle graphs.
- [[sandpile-group](pages/sandpile-group.md)] - the sandpile group of the castle graph, computed from its `2 × 2` squares; trivial for tree castles.
- [[sandpile-census](pages/sandpile-census.md)] - the sandpile groups of the 33,150 castles with at most 16 cells, up to mirror image.
- [[castle-avalanches](pages/castle-avalanches.md)] - avalanches on the castle graph; in the tide model, rectangles and battlements of the same height have the same mean avalanche, and the `2 × 2` squares change only the tail.
- [[tree-castle-by-area](pages/tree-castle-by-area.md)] - the tree skylines counted by area.
- [[tree-castle-diffusion](pages/tree-castle-diffusion.md)] - the graph of a tree castle as a comb, the bottom row with a tooth on each column, and the simple random walk on it.
- [[hilbert-castles](pages/hilbert-castles.md)] - the Hilbert duality of strip rules, which gives the tree skylines by width and area from the strips with every column at height at least 2.
- [[fibonacci-castle](pages/fibonacci-castle.md)] - the tree castles of height 2, and the signed Fibonacci tower count `P_F(w)` that gives the parity of the tree castles at every height.
- [[padovan-families](pages/padovan-families.md)] - the palindromic tree castles by area, which give the tree castles up to mirror image.
- [[unique-tournament](pages/unique-tournament.md)] - tournaments determined by their score vectors, counted by `A000570`, the tree skylines of height at most 4 by area.
- [[castle-classification-growth](pages/castle-classification-growth.md)] - families of castles by their growth by width, among them the tree castles.
- [[metallic-means](pages/metallic-means.md)] - the growth `σ_1^{h−1}` of the tree castles of height `h`.
- [[castle-by-area](pages/castle-by-area.md)] - castles counted by area, the number of vertices of the castle graph.
- [[castle-representations](pages/castle-representations.md)] - the other encodings of a castle.
- [[castle-snippets](pages/castle-snippets.md)] - `castle_graph`, `is_tree_castle`, `cycle_rank`.

## Footnotes

[^1]: Verified by execution (Python 3.11, 2026-10-16): the drawings and the counts of cells, edges and `2 × 2` squares of the six examples, from the formulas of the section *Invariants of the skyline*.
[^2]: The proof is own reasoning, checked by execution (Python 3.11, 2026-10-25): for all 16,383 skylines with at most 14 cells, in both the castle graph and the tide model's merged graph, the number of `2 × 2` squares equals the cycle rank, and the square cycles restricted to the edges `e_{i,j}` form a matrix of determinant `±1`.
[^3]: Verified by execution (Python 3.11, 2026-10-16): `T_h(w)` for `h ≤ 3`, `w ≤ 9` and `h = 4, 5`, `w ≤ 7` by enumeration of all skylines, and for `w = 8, 9` from Equation (1); `A_tree(w, h)` from Equation (2) against enumeration for `w ≤ 8` at `h = 2, 3` and `w ≤ 7` at `h = 4`, and at `w = 8` from Equation (1). https://oeis.org/A001045, https://oeis.org/A006130, https://oeis.org/A006131, https://oeis.org/A000071 (read 2026-09-17 and 2026-10-04): the offsets of the table.
[^4]: Verified by execution (Python 3.11, 2026-10-16): the counts by area `n ≤ 14` of the tree castles of height 2 (`0, 1, 2, 3, 5, 8, 12, …`), and of the tree skylines of height at most 3, at most 4 and of any height, against the data of https://oeis.org/A077868, https://oeis.org/A000930, https://oeis.org/A006498, https://oeis.org/A000570 and https://oeis.org/A005251 (read 2026-10-16).
[^5]: The pairing argument is own reasoning, verified by execution (Python 3.11, 2026-10-25): Equation (3) on every tree castle with `h ≤ 5` and `w ≤ 8`; Equation (4) for `h = 2, …, 7` and `w = 1, …, 12` from a column-by-column transfer count, checked against brute force wherever `h^w ≤ 2·10^6`; the table and `S(w, 3)` by brute force over all skylines.
[^6]: Verified by execution (Python 3.11, 2026-10-25): for every `n ≤ 16`, the compositions of `n`, the palindromic ones, the compositions with no two neighboring parts at least 2 and the palindromic ones among those number `2^{n−1}`, `2^{⌊n/2⌋}`, `A005251(n + 2)` and `A000931(n + 6)`, and both formulas give the mirror-image classes counted directly, which sum to 33,150 and 6,963. https://oeis.org/A016116 (read 2026-10-25) - "Number of symmetric compositions of n"; https://oeis.org/A005251 and https://oeis.org/A000931 (read 2026-10-25): the data; https://oeis.org/A005418 (read 2026-10-25), offset 1 - "Also number of compositions of n up to direction"; https://oeis.org/A005683 (read 2026-10-25), offset 3 - "a(n) = (A005251(n) + A000931(n+4))/2".
