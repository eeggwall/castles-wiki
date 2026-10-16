---
title: Ramanujan castles
category: Concepts
summary: A castle is Ramanujan when the second-largest adjacency eigenvalue λ_2 of its castle graph is at most ρ(T), the spectral radius of the universal covering tree, the bipartite form of the Ramanujan condition for irregular graphs. The page computes ρ(T) by an edge-cavity method, checks it on graphs with known ρ(T), and sweeps every castle with at most 22 cells. Every castle with at most 14 cells is Ramanujan; the smallest non-Ramanujan castles have 15 cells (one graph: two 2 × 3 rectangles joined by a path of three cells, λ_2/ρ(T) = 1.0003); the smallest non-Ramanujan rectangle is the 2 × 14 ladder (14, 14) at 28 cells.
tags: [concept, castle, spectral, ramanujan, universal-cover, alon-boppana, cavity-method, non-backtracking, expander, computation, worked-example]
sources: [project-euler-502-brute-force]
created: 2026-09-19
updated: 2026-10-16
---

# Ramanujan castles

For a finite connected graph `G`, Hall, Puder and Sawin write `λ(G)` for the largest absolute value of a non-trivial adjacency eigenvalue and `ρ(T)` for the spectral radius of the universal covering tree `T` of `G`; the graphs with `λ(G) ≤ ρ(T)` are the Ramanujan graphs, a name they take from Lubotzky, Phillips and Sarnak.[^hps] This page applies the bipartite form of that condition to castle graphs, computes `ρ(T)` on small castles, sweeps every castle with at most 22 cells, and finds **the smallest non-Ramanujan castles at 15 cells** (one graph: two `2 × 3` rectangles joined by a path of three cells) and **the smallest non-Ramanujan rectangle, the `2 × 14` ladder `(14, 14)` at 28 cells**. Every value below was computed with the programs on this page.[^exec]

## What the definition asks

Let `A(G)` be the adjacency matrix of `G`, with eigenvalues `λ_n ≤ ⋯ ≤ λ_2 ≤ λ_1`, and `λ(G) = max(λ_2, −λ_n)`. The universal covering tree `T` is the tree of non-backtracking walks in `G` from a fixed vertex; its adjacency operator acts on `ℓ²(V(T))`, and its spectral radius `ρ(T)` is `2√(k − 1)` when `G` is `k`-regular.[^hps]

**Greenberg's theorem.** For a tree `T` with finite quotients, every finite graph `G` with `n` vertices covered by `T` has `λ(G) ≥ ρ(T) − o_n(1)`, the `o_n(1)` depending only on `T`; restricted to regular graphs, this is the Alon-Boppana bound.[^hps] So `ρ(T)` is the smallest value that `λ(G)` can approach in the family of graphs covered by `T`, and the Ramanujan graphs reach it.

**The bipartite form.** A bipartite graph has `λ_n = −λ_1`, so `λ(G) = λ_1`, and Hall, Puder and Sawin call a bipartite graph **bipartite-Ramanujan** when `λ_2, …, λ_{n−1}` lie in `[−ρ(T), ρ(T)]`.[^hps] A castle graph is bipartite (color cell `(i, j)` by `(i + j) mod 2`; every edge joins opposite colors), so its spectrum is symmetric about 0, and a **Ramanujan castle** is a castle whose graph satisfies

```
λ_2  ≤  ρ(T).
```

**Regular castles.** Only four castle graphs are regular. The leftmost cell of the top row has no neighbor above it and none to its left, so it has at most two neighbors, and a regular castle graph has degree at most 2: a path or a cycle. A path with more than two cells has ends of degree 1 and middle cells of degree 2, and the only cycle among castle graphs is the `2 × 2` square, so the regular castles are `(1)` (the path `P_1`), `(1, 1)` and `(2)` (both `P_2`) and `(2, 2)` (the cycle `C_4`). For every other castle `ρ(T)` is computed for its own covering tree.

## The universal covering tree of a castle

The universal cover `T` is built by unfolding from a root: from a vertex of the current tree, add a child for every neighbor of the corresponding cell of `G` except the one just came from. Every vertex of `T` has the same degree as its cell, and no cycle of `G` closes in `T`.

- **Trees cover themselves.** If `G` is a tree, `T = G` and `ρ(T) = λ_1(G) ≥ λ_2(G)`, so every tree castle is Ramanujan. The condition restricts only the castles with a cycle, which are the castles with a `2 × 2` block of cells ([[castle-graph](pages/castle-graph.md)]).
- **`ρ(T) ≤ 2√(Δ − 1)`.** A tree of maximum degree `Δ` is a subgraph of the `Δ`-regular tree, and the spectral radius of a nonnegative operator does not increase on passing to a subgraph, so `ρ(T) ≤ 2√(Δ − 1)`: at most `2√3 = 3.464` for a castle with a cell of degree 4, and at most `2√2 = 2.828` for a castle whose cells all have degree at most 3.
- **`ρ(T) ≥ 2` for a castle with a cycle.** Its covering tree contains a bi-infinite path, whose spectral radius is 2.

## Two methods to compute ρ(T)

**Method A (truncated ball).** Unfold `T` from a root to depth `D`. The truncated tree is a finite subtree of `T`, so its largest eigenvalue is a lower bound for `ρ(T)`, and it increases to `ρ(T)` as `D` grows. The truncated tree has up to `Δ(Δ − 1)^{D−1}` vertices, so this serves as a cross-check on small depths.

**Method B (edge cavity).** For each directed edge `u → v` of `G`, the cavity values satisfy

```
x_{u→v}(z)  =  1 / (z − Σ_{w ~ v, w ≠ u} x_{v→w}(z)).
```

Iterated from `x = 0`, this map increases monotonically. It converges exactly when a positive fixed point exists, which gives a positive eigenfunction of the cover at eigenvalue `z`, so `z ≥ ρ(T)`; for `z < ρ(T)` some denominator becomes nonpositive. Bisecting on `z` gives `ρ(T)` to within the bisection width.[^exec]

```python
import numpy as np, networkx as nx

def rho_cover(G, tol=1e-10, max_iter=20000):
    """Cover-tree spectral radius rho(T) by the edge-cavity iteration and bisection."""
    E = list(G.edges())
    if not E: return 0.0
    dedges = [(u, v) for u, v in E] + [(v, u) for u, v in E]
    idx = {e: i for i, e in enumerate(dedges)}
    children = [
        [idx[(v, w)] for w in G.neighbors(v) if w != u]
        for (u, v) in dedges
    ]
    n = len(dedges)
    Delta = max(dict(G.degree()).values())
    z_hi = 2.0 * np.sqrt(max(Delta - 1, 1)) + 0.5     # the bound 2*sqrt(Delta - 1), plus slack
    z_lo = 1e-6
    def converges(z):
        x = np.full(n, 1.0 / max(z, 0.5))
        for _ in range(max_iter):
            s = np.array([x[children[i]].sum() if children[i] else 0.0 for i in range(n)])
            denom = z - s
            if np.any(denom <= 0): return False
            new = 1.0 / denom
            if np.max(np.abs(new - x)) < tol: return True
            x = new
        return False
    for _ in range(40):
        mid = 0.5 * (z_lo + z_hi)
        if converges(mid): z_hi = mid
        else: z_lo = mid
        if z_hi - z_lo < 1e-8: break
    return z_hi
```

### Check against graphs with known ρ(T)

The `k`-regular tree has `ρ = 2√(k − 1)` and the `(k, ℓ)`-biregular tree has `ρ = √(k − 1) + √(ℓ − 1)`.[^hps]

| graph | `ρ(T)` | `rho_cover` |
|---|---|---|
| `C_4` (2-regular) | `2` | `2.0000000` |
| `K_4` (3-regular) | `2√2 = 2.8284271` | `2.8284272` |
| `K_5` (4-regular) | `2√3 = 3.4641016` | `3.4641017` |
| Petersen graph (3-regular) | `2√2 = 2.8284271` | `2.8284272` |
| `K_{3,4}` ((3, 4)-biregular) | `√2 + √3 = 3.1462644` | `3.1462644` |
| `K_{2,3}` ((2, 3)-biregular) | `1 + √2 = 2.4142136` | `2.4142136` |

Every value of `rho_cover` exceeds the exact one by less than `5 × 10⁻⁸`. On `(14, 14)`, rooted at the sixth cell of the first column, the truncated ball at depths 3, 5, 7, 9 gives `2.4495, 2.6286, 2.7008, 2.7365`, below the cavity value `2.8139`.

## Small worked cases

### `(2, 2)`, the 4-cycle

The graph is `C_4`, with eigenvalues `2, 0, 0, −2`. Its cover is the bi-infinite path, `ρ(T) = 2`, and `λ_2 = 0 ≤ 2`. **Ramanujan.**

### `(2, 2, 2)`, the `3 × 2` rectangle

The graph is the product `P_3 × P_2`, whose eigenvalues are the sums `2cos(iπ/4) + 2cos(jπ/3)`:

```
√2 + 1,  1,  √2 − 1,  −(√2 − 1),  −1,  −(√2 + 1).
```

So `λ_1 = 1 + √2 = 2.4142` and `λ_2 = 1`, and the cavity method gives `ρ(T) = 2.3892`. The four corner cells have degree 2 and the two middle cells degree 3, but each color class contains cells of both degrees, so the graph is not `(2, 3)`-biregular, and `ρ(T)` is below the biregular value `1 + √2`. `λ_2 = 1 ≤ 2.3892`. **Ramanujan.**

### `(4, 4)`, the `2 × 4` rectangle

The graph is `P_2 × P_4`, with `λ_1 = 1 + φ = φ² = 2.6180` and `λ_2 = φ = 1.6180`, where `φ` is the golden ratio, and `ρ(T) = 2.5653`. `1.6180 ≤ 2.5653`. **Ramanujan.**

## The census to 22 cells

The sweep covers every castle with at most 22 cells, mirror images removed. Tree castles are Ramanujan, and so is every castle with a cycle and `λ_2 ≤ 2`, since then `λ_2 ≤ 2 ≤ ρ(T)`; for the others one cavity test at `z = λ_2` decides the inequality.[^exec] **Every castle with at most 14 cells is Ramanujan, and the first failures have 15 cells.**

| cells | non-tree castles | with `λ_2 > 2` | non-Ramanujan |
|---|---|---|---|
| 4 | 1 | 0 | 0 |
| 5 | 2 | 0 | 0 |
| 6 | 7 | 0 | 0 |
| 7 | 14 | 0 | 0 |
| 8 | 35 | 0 | 0 |
| 9 | 73 | 0 | 0 |
| 10 | 164 | 4 | 0 |
| 11 | 342 | 22 | 0 |
| 12 | 734 | 97 | 0 |
| 13 | 1,521 | 329 | 0 |
| 14 | 3,187 | 1,107 | 0 |
| 15 | 6,559 | 3,164 | 3 |
| 16 | 13,548 | 8,068 | 3 |
| 17 | 27,713 | 19,193 | 22 |
| 18 | 56,721 | 44,041 | 75 |
| 19 | 115,442 | 97,822 | 271 |
| 20 | 234,821 | 211,284 | 844 |
| 21 | 476,010 | 445,095 | 2,432 |
| 22 | 964,055 | 923,933 | 6,836 |

**The smallest failures.** The three 15-cell failures `(3, 3, 1, 1, 1, 3, 3)`, `(2, 2, 2, 1, 1, 1, 2, 2, 2)` and `(2, 2, 2, 1, 1, 1, 3, 3)` are one graph: two `2 × 3` rectangles joined at corners by a path of three cells, with cycle rank 4. It has `λ_1 = 2.50719`, `λ_2 = 2.47367` and `ρ(T) = 2.47288`, a ratio of `1.0003`. The three 16-cell failures are the same shape with a path of four cells. Two `3 × 3` squares joined by one column of height 1, `(3, 3, 3, 1, 3, 3, 3)` at 19 cells, fail with ratio `1.018`.

## The 2 × h ladders

Among rectangles, the `2 × h` family fails first. The rectangle `(h, h)` has the ladder graph `P_2 × P_h`:

| skyline | cells | `λ_1` | `λ_2` | `ρ(T)` | ratio | Ramanujan? |
|---|---|---|---|---|---|---|
| `(10, 10)` | 20 | 2.91899 | 2.68251 | 2.79359 | 0.960 | yes |
| `(11, 11)` | 22 | 2.93185 | 2.73205 | 2.80106 | 0.975 | yes |
| `(12, 12)` | 24 | 2.94188 | 2.77091 | 2.80658 | 0.987 | yes |
| `(13, 13)` | 26 | 2.94986 | 2.80194 | 2.81074 | 0.997 | yes |
| **`(14, 14)`** | **28** | **2.95630** | **2.82709** | **2.81393** | **1.005** | **no** |
| `(15, 15)` | 30 | 2.96157 | 2.84776 | 2.81641 | 1.011 | no |
| `(16, 16)` | 32 | 2.96595 | 2.86494 | 2.81838 | 1.017 | no |

The `2 × 14` rectangle `(14, 14)` is the smallest non-Ramanujan rectangle. Its graph is the 14-rung ladder, whose sandpile group is cyclic of order `A001353(14) = 29,354,524` in the sink model and `A001835(14) = 21,489,003` in the tide model ([[sandpile-group](pages/sandpile-group.md)]). Its second-largest eigenvalue is `λ_2 = 1 + 2cos(2π/15) = 2.82709`, and `ρ(T) = 2.81393`, so `λ_2 > ρ(T)` by about `0.013`. Among castles that are not rectangles, `(2, 12, 12)` at 26 cells fails with ratio `1.001`.

The ladder `P_2 × P_h` has `λ_2 = 1 + 2cos(2π/(h + 1))`, which tends to 3 as `h` grows, while its covering tree has maximum degree 3, so `ρ(T) < 2√2 = 2.828`. So `λ_2` passes `ρ(T)` for large `h`, and the crossing is at `h = 14`.

## Rectangles

The rectangle `(h, h, …, h)` with `w` columns has the graph `P_w × P_h`, so the `w × h` and `h × w` rectangles have the same graph. Its spectrum comes from the product formula, and `ρ(T)` from the cavity method. For each width, the first height `h ≥ w` at which the rectangle fails, for `h ≤ 16`:

| width `w` | first failing `h` | cells | `λ_2` | `ρ(T)` | ratio |
|---|---|---|---|---|---|
| 2 | 14 | 28 | 2.8271 | 2.8139 | 1.005 |
| 3 | 11 | 33 | 3.1463 | 3.1099 | 1.012 |
| 4 | 10 | 40 | 3.3005 | 3.2477 | 1.016 |
| 5 | 9 | 45 | 3.3501 | 3.3141 | 1.011 |
| 6 | 9 | 54 | 3.4200 | 3.3559 | 1.019 |
| 7 | 8 | 56 | 3.3798 | 3.3702 | 1.003 |
| 8 | 8 | 64 | 3.4115 | 3.3862 | 1.007 |

For `2 ≤ w ≤ 8` and `w ≤ h ≤ 16` the ratio increases with `h`, so each width fails from its threshold on. Along the diagonal `w = h` the ratios are `0.516, 0.732, 0.850, 0.923, 0.973` for `3 × 3` to `7 × 7`, then `1.007` at `8 × 8`, the first failing square, and `1.033, 1.053` at `9 × 9` and `10 × 10`. The cell count alone does not decide: at 40 cells the `4 × 10` rectangle fails while the `5 × 8` rectangle is Ramanujan (ratio `0.988`).

## Crenellated castles

The crenellated castles of [[castle-classification-shape](pages/castle-classification-shape.md)] alternate two heights `a` and `h`. With `a = 1` no two neighboring columns both have height at least 2, so these are tree castles, Ramanujan with `ρ(T) = λ_1`; two of them with 13 columns:

| skyline | `λ_1` | `λ_2` | `ρ(T)` | ratio |
|---|---|---|---|---|
| `(5, 1, 5, 1, …, 5)`, 13 columns | 2.2685 | 2.1599 | 2.2685 | 0.9521 |
| `(3, 1, 3, 1, …, 3)`, 13 columns | 2.2470 | 2.1284 | 2.2470 | 0.9472 |

With `a ≥ 2` they have cycles, and the census covers them up to 22 cells.

## The non-backtracking matrix

The **non-backtracking matrix** `B` of `G` acts on directed edges, with `B_{(u→v), (v→w)} = 1` when `w ≠ u` and 0 otherwise; the cavity equation runs on the same directed edges. For a `d`-regular graph every directed edge has `d − 1` successors, so `B` has spectral radius `d − 1` and `ρ(T) = 2√(d − 1)` is twice its square root. For irregular castles the two are not related this way: at `(14, 14)` the spectral radius of `B` is `1.9299`, twice its square root is `2.7784`, and `ρ(T) = 2.8139`.

## Reproduce

The program for a single castle; the census adds the filter `λ_2 > 2` and one cavity test at `z = λ_2`.[^exec]

```python
import numpy as np, networkx as nx

def castle_graph(c):
    """Castle graph of skyline c: cells as vertices, edges between cells that share a side."""
    G = nx.Graph()
    cells = [(i, j) for i, h in enumerate(c) for j in range(h)]
    G.add_nodes_from(cells)
    S = set(cells)
    for (i, j) in cells:
        for nb in ((i + 1, j), (i, j + 1)):
            if nb in S: G.add_edge((i, j), nb)
    return G

# `rho_cover` as above.

def ramanujan_status(c):
    G = castle_graph(c)
    if G.number_of_edges() == G.number_of_nodes() - 1:
        return "trivially yes (tree; rho(T) = lam_1)"
    A = nx.to_numpy_array(G)
    sp = sorted(np.linalg.eigvalsh(A).tolist(), reverse=True)
    lam1, lam2 = sp[0], sp[1]
    rT = rho_cover(G)
    return {"lam_1": lam1, "lam_2": lam2, "rho_T": rT,
            "ratio": lam2 / rT, "ramanujan": lam2 <= rT + 1e-6}
```

With `rho_cover` from the section *Two methods to compute ρ(T)*, `ramanujan_status((14, 14))` returns

```
{"lam_1": 2.9562952, "lam_2": 2.8270909, "rho_T": 2.8139274,
 "ratio": 1.0046780, "ramanujan": False}
```

## Appearances in Sources

- [[project-euler-502-brute-force](pages/project-euler-502-brute-force.md)] - the skyline encoding of a castle, `c_1, …, c_w` with `max c = h`, that the census enumerates.

## Related Concepts

- [[castle-classification-spectrum](pages/castle-classification-spectrum.md)] - the classification of castles by spectrum, where Ramanujan castles are one of the spectral types.
- [[castle-graph](pages/castle-graph.md)] - the castle graph and its invariants: bipartite, planar, maximum degree 4, cycle rank equal to the number of `2 × 2` blocks.
- [[castle-graph-spectral-radius](pages/castle-graph-spectral-radius.md)] - the castles golden and silver by spectrum and those with spectral radius `φ²`.
- [[isospectral-castles](pages/isospectral-castles.md)] - castles with the same adjacency or Laplacian spectrum, the smallest pair at 10 cells.
- [[castle-eigenvalues-by-example](pages/castle-eigenvalues-by-example.md)] - the adjacency spectra of small castles worked by hand.
- [[spectral-analysis](pages/spectral-analysis.md)] - the castle spectra, with the definition of the Ihara zeta function.
- [[castle-snippets](pages/castle-snippets.md)] - `castle_graph` and `castle_graph_radius`.
- [[hardy-ramanujan-castle](pages/hardy-ramanujan-castle.md)] - the taxicab number 1729 as a castle count (`A^e(6, 4) = 1729`) and as a castle; its digit castle `(1, 7, 2, 9)` is Ramanujan in the sense of this page (`λ_2 = 1.898 ≤ ρ(T) = 2.576`).

## Footnotes

[^hps]: https://arxiv.org/pdf/1506.02335 (C. Hall, D. Puder and W. F. Sawin, *Ramanujan coverings of graphs*, read 2026-10-16) - §1.1 p.2: "Denote by λ(G) the largest absolute value of a non-trivial eigenvalue, namely λ(G) = max(λ2, −λn)", "Let ρ(G) be the spectral radius of the universal covering tree of G. For instance, if G is k-regular then ρ(G) = 2√(k−1)", "Following [LPS88, HLW06] they are called Ramanujan graphs", and the bipartite case "λn−1, λn−2, ..., λ2 ∈ [−ρ(G), ρ(G)]. We call a bipartite graph with this property a bipartite-Ramanujan graph"; §2.1 p.12: "Let ρ(T) be the spectral radius of T", "acting on ℓ2(V(T))", Theorem 2.1 (in Cioabă's version, after Greenberg) "λ(G) ≥ ρ − o_n(1) (with the o_n(1) term depending only on T)", and "The last statement of the theorem, restricted to regular graphs, is due to Alon-Boppana"; p.14 footnote 13: "In general, the spectral radius of the (k,ℓ)-biregular tree is √(k−1) + √(ℓ−1)."
[^exec]: Verified by execution (Python 3.11, NumPy, NetworkX; 2026-09-28, rerun 2026-10-16). The cavity map `x → 1/(z − Cx)` on directed edges, iterated from `x = 0`, increases monotonically; it converges exactly when a positive fixed point exists, which gives a positive eigenfunction of the cover at eigenvalue `z` (so `z ≥ ρ(T)`), and it reaches a nonpositive denominator when `z < ρ(T)`. Precise values of `ρ(T)` by bisection on that test to width `10⁻⁸`; `rho_cover` as printed agrees with the exact values of the check table to `5 × 10⁻⁸`. Census: every composition of `n ≤ 22` with mirror images removed; tree castles skipped; castles with a cycle and `λ_2 ≤ 2 + 10⁻⁹` skipped (castles with `λ_2 = 2` exactly are Ramanujan, since `ρ(T) ≥ 2`); for the rest one cavity test at `z = λ_2` (up to 60,000 iterations, tolerance `10⁻¹¹`), with no undetermined cases. The 15-cell failures rechecked by bisection and by truncated balls rooted at the corner cell `(0, 0)` (`2.379, 2.420, 2.439` at depths 6, 9, 12). The rectangles `2 ≤ w ≤ 8`, `w ≤ h ≤ 16`, the squares to `10 × 10`, the ladder table, `(2, 12, 12)`, `(3, 3, 3, 1, 3, 3, 3)`, the crenellated castles and `(1, 7, 2, 9)` by bisection; the spectral radius of `B` from its eigenvalues; the sandpile orders of `(14, 14)` as determinants of the reduced Laplacians.
