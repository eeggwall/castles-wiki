---
title: Ramanujan castles
category: Concepts
summary: The spectral-graph-theoretic Ramanujan condition for irregular graphs, applied to castle polyomino graphs. Greenberg's universal-cover formulation, an executable edge-cavity method for computing the cover-tree spectral radius rho(T), verification on known graphs, and an exhaustive census to 22 cells - every castle with at most 14 cells is Ramanujan; the smallest non-Ramanujan castles have 15 cells (two 2x3 blocks joined by a path of three cells, lam_2/rho(T) = 1.0003); the smallest non-Ramanujan rectangle is the 2x14 ladder at 28 cells.
tags: [concept, castle, spectral, ramanujan, universal-cover, alon-boppana, cavity-method, non-backtracking, expander, computation, worked-example]
sources: [oeis-mining-pe502, project-euler-502-brute-force]
created: 2026-09-19
updated: 2026-09-28
---

# Ramanujan castles

A Ramanujan graph is one whose adjacency spectrum is as compressed as any infinite family of graphs at its size and degree can achieve - the graph-theoretic analogue of "optimally expanding" or "optimally mixing". The definition originally applies to `d`-regular graphs (Lubotzky-Phillips-Sarnak, Margulis, 1988): every eigenvalue other than `±d` has absolute value at most `2*sqrt(d - 1)`. Only four castle graphs are regular, so the regular definition says almost nothing about castles; the generalization used here is Greenberg's, via the spectral radius `rho(T)` of the universal covering tree. This page states that definition, computes `rho(T)` on small castles, sweeps every castle with at most 22 cells for Ramanujan status, and finds **the smallest non-Ramanujan castles at 15 cells** (one graph: two `2 x 3` blocks joined by a path of three cells) and **the smallest non-Ramanujan rectangle, the 2x14 ladder `(14, 14)` at 28 cells**.

Every value below was computed with the programs on this page; the census method is in the execution footnote.[^exec]

## What the definition asks

For a graph `G`, let `A(G)` be its adjacency matrix and let `T` be its universal covering tree - the infinite tree obtained by unfolding `G` locally at every vertex. `T` is a tree because a cover of `G` has no cycles; `A(T)` acts on `l^2(V(T))` and has a spectral radius `rho(T)`. For a `d`-regular graph `G`, `T` is the infinite `d`-regular tree and `rho(T) = 2*sqrt(d - 1)`.

**Alon-Boppana** (1986). For any infinite family of finite `d`-regular graphs `G_n` with `|V(G_n)| -> infty`, the second-largest eigenvalue satisfies

```
lam_2(G_n) >= 2*sqrt(d - 1) - o(1).
```

So `2*sqrt(d - 1)` is the asymptotic floor no infinite family beats. A `d`-regular Ramanujan graph is one that hits this floor exactly:

```
|lam| <= 2*sqrt(d - 1)     for every eigenvalue lam of A(G) other than +d and -d.
```

**Greenberg's extension (irregular graphs).** For a general finite graph `G` with universal cover `T`, Greenberg proved the asymptotic version - infinite families of finite graphs sharing a fixed universal cover `T` satisfy `lam(G_n) >= rho(T) - o(1)`, where `lam(G) = max{|lam| : lam eigenvalue of A(G) except +lam_1 and, if G is bipartite, -lam_1}`. A finite `G` is **Ramanujan** iff every non-trivial eigenvalue is bounded by `rho(T)`:

```
|lam| <= rho(T)     for every non-trivial eigenvalue lam of A(G).
```

Castle graphs are **bipartite** (color cells by `(i + j) mod 2`; every adjacency edge connects opposite colors), so the spectrum is symmetric about `0` and `lam_n = -lam_1`. The bipartite-Ramanujan form of the condition reduces to a single inequality:

```
lam_2(G)  <=  rho(T).
```

**Why the d-regular version covers only four castles.** A castle graph is `d`-regular iff every cell has the same number of orthogonal neighbours. The leftmost cell of the top row has at most two neighbours (its column-neighbour below and its row-neighbour to the right), so a regular castle has max degree at most 2, i.e. is a path or cycle. A path longer than two cells has ends of degree 1 and middle cells of degree 2, so the full list is `(1)` (`P_1`), `(1, 1)` and `(2)` (both `P_2`), and `(2, 2)` (`C_4`). Everything else is irregular, and only the Greenberg form applies.

## The universal covering tree of a castle

Concretely, the universal cover `T` of a graph `G` is built by unfolding at any root: at each step, from a vertex `v` in the current cover, walk to every neighbour of the corresponding vertex in `G` **except** the one we came from, and adjoin those as new leaves. Iterating gives a tree in which the local `d(v)`-star at every vertex matches the local star in `G`, but no cycle in `G` ever closes.

Two observations shape every computation below.

- **Trees cover themselves.** If `G` is a tree, `T = G` and `rho(T) = lam_1(G)`. Trees are automatically Ramanujan because `lam_1 >= lam_2` and `rho(T) = lam_1`. The Ramanujan predicate has content only on castles with a cycle (i.e. positive **cycle rank** `|E| - |V| + 1`, equivalently at least one `2 x 2` filled block - see [[castle-graph](pages/castle-graph.md)]).
- **`rho(T) <= 2*sqrt(Delta - 1)`.** A tree of maximum degree `Delta` has spectral radius at most that of the `Delta`-regular tree, so `rho(T) <= 2*sqrt(Delta - 1)`. For castles this bounds `rho(T)` above: at most `2*sqrt(3) ~= 3.464` for castles containing an interior cell (degree 4), at most `2*sqrt(2) ~= 2.828` for boundary-only castles.

## Two methods to compute rho(T)

**Method A (truncated ball).** Unfold `T` from a root to depth `D`. The truncated tree is a finite graph; its adjacency spectral radius is a lower bound for `rho(T)` and increases monotonically to `rho(T)` as `D -> infty`. Simple to implement, but the truncated tree has up to `Delta * (Delta - 1)^(D - 1)` vertices, so `D = 10` on a degree-4 graph already gives on the order of `10^5` nodes. Useful as a cross-check on small graphs, not as a workhorse.

**Method B (edge-cavity fixed-point).** For each directed edge `(u -> v)` in `G`, define the "branch contribution"

```
x_{u->v}(z)  =  1  /  (z - sum_{w ~ v, w != u} x_{v->w}(z)).
```

This is the standard cavity / belief-propagation equation for the resolvent of `A(T)` at spectral parameter `z`. It has a positive real solution for `z > rho(T)` and no positive real solution for `z < rho(T)`; the critical `z` at which the fixed point transitions is `rho(T)` itself. Bisecting on `z` and running the fixed-point iteration at each `z` gives `rho(T)` to full floating-point precision in `O(|E|)` work per bisection step. Both methods agree on every example below.

The full code:

```python
import numpy as np, networkx as nx

def rho_cover(G, tol=1e-8, max_iter=1500):
    """Cover-tree spectral radius rho(T) by edge-cavity fixed-point."""
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
    z_hi = 2.0 * np.sqrt(max(Delta - 1, 1)) + 0.5     # Grover-Hoory ceiling + slack
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

### Verification against known cases

| graph | true `rho(T)` | cavity estimate |
|---|---|---|
| `C_4` (2-regular) | `2` | `2.0000002` |
| `K_4` (3-regular) | `2*sqrt(2) = 2.8284271` | `2.8284273` |
| `K_5` (4-regular) | `2*sqrt(3) = 3.4641016` | `3.4641018` |
| Petersen (3-regular) | `2*sqrt(2) = 2.8284271` | `2.8284273` |
| `K_{3,4}` biregular | `sqrt(2) + sqrt(3) = 3.1462644` | `3.1462646` |
| `K_{2,3}` biregular | `1 + sqrt(2) = 2.4142136` | `2.4142138` |

Every case agrees to within `3 x 10^-7`. On `(14, 14)` (the 28-cell rectangle below) the truncated-ball estimate at depths 3, 5, 7, 9 gives `2.4495, 2.6286, 2.7008, 2.7365`, monotonically approaching the cavity value `2.8139`.

## Small worked cases

### `(2, 2)` - the 4-cycle

Four cells, adjacency graph `C_4`. Every cell has degree 2. `A(G)` has eigenvalues `2, 0, 0, -2`. The universal cover is the 2-regular tree (the infinite path), `rho(T) = 2`. The non-trivial eigenvalues are `0, 0`, both bounded by `rho(T) = 2`. **Ramanujan**, trivially. (Regular, so the standard `d`-regular definition also applies and gives the same answer.)

### `(2, 2, 2)` - the `3 x 2` rectangle

Six cells arranged as `P_3 * P_2`. The adjacency spectrum has closed form `2 cos(i pi / (w + 1)) + 2 cos(j pi / (h + 1))`:

```
sqrt(2) + 1,  1,  sqrt(2) - 1,  -(sqrt(2) - 1),  -1,  -(sqrt(2) + 1).
```

So `lam_1 = 1 + sqrt(2) = 2.4142`, `lam_2 = 1`. The cavity method gives `rho(T) = 2.3892`. The graph is irregular: four corner cells of degree 2 and two interior-column cells of degree 3. The Kesten-McKay biregular formula would give `sqrt(1) + sqrt(2) = 2.4142` if the graph were `(2, 3)`-biregular, but it is not: the degrees are not constant on the bipartition classes, and `rho(T)` is smaller.

Ramanujan condition: `lam_2 = 1 <= 2.3892 = rho(T)`. **Yes.**

### `(4, 4)` - the `2 x 4` rectangle

Eight cells, `P_2 * P_4`, closed-form spectrum. `lam_1 = phi^2 = 2.6180`, `lam_2 = phi = 1.6180`, `rho(T) = 2.5653`. Ramanujan: `1.6180 <= 2.5653`. **Yes.**

## The census to 22 cells

An exhaustive sweep over every castle with at most 22 cells (every composition, mirror images removed) finds that **every castle with at most 14 cells is Ramanujan, and the first failures have 15 cells**. Only non-tree castles with `lam_2 > 2` need testing: a castle graph with a cycle has a bi-infinite path in its universal cover, so `rho(T) >= 2`, and the cavity iteration at `z = lam_2` then decides the inequality.[^exec]

| cells | non-tree castles | with `lam_2 > 2` | non-Ramanujan |
|---|---|---|---|
| 4 | 1 | 0 | 0 |
| 5 | 2 | 0 | 0 |
| 6 | 7 | 0 | 0 |
| 7 | 14 | 0 | 0 |
| 8 | 35 | 0 | 0 |
| 9 | 73 | 0 | 0 |
| 10 | 164 | 6 | 0 |
| 11 | 342 | 22 | 0 |
| 12 | 734 | 97 | 0 |
| 13 | 1,521 | 335 | 0 |
| 14 | 3,187 | 1,117 | 0 |
| 15 | 6,559 | 3,168 | 3 |
| 16 | 13,548 | 8,072 | 3 |
| 17 | 27,713 | 19,210 | 22 |
| 18 | 56,721 | 44,120 | 75 |
| 19 | 115,442 | 98,031 | 271 |
| 20 | 234,821 | 211,405 | 844 |
| 21 | 476,010 | 445,228 | 2,432 |
| 22 | 964,055 | 924,048 | 6,836 |


**The smallest failures.** The three 15-cell failures `(3, 3, 1, 1, 1, 3, 3)`, `(2, 2, 2, 1, 1, 1, 2, 2, 2)` and `(2, 2, 2, 1, 1, 1, 3, 3)` are one graph: two `2 x 3` blocks joined at corners by a path of three cells. Its `lam_1 = 2.50719`, `lam_2 = 2.47367` and `rho(T) = 2.47288`, a ratio of `1.0003`. `lam_2` is close to `lam_1` because the two blocks are joined only by the path, and the long path of degree-2 cells keeps `rho(T)` below `lam_2`. The 16-cell failures are the same shape with a four-cell path. Two `3 x 3` blocks joined by one height-1 column, `(3, 3, 3, 1, 3, 3, 3)` at 19 cells, fail with ratio `1.018`.

## The 2 x h ladders

Among rectangles the transition happens first in the `2 x h` family. As `h` grows, the rectangle `(h, h)` (two columns each of height `h`, a ladder graph) closes the Ramanujan gap:

| skyline | area | `lam_1` | `lam_2` | `rho(T)` | ratio | Ramanujan? |
|---|---|---|---|---|---|---|
| `(10, 10)` | 20 | 2.91899 | 2.68251 | 2.79360 | 0.960 | yes |
| `(11, 11)` | 22 | 2.93185 | 2.73205 | 2.80107 | 0.975 | yes |
| `(12, 12)` | 24 | 2.94188 | 2.77091 | 2.80659 | 0.987 | yes |
| `(13, 13)` | 26 | 2.94986 | 2.80194 | 2.81074 | 0.997 | yes |
| **`(14, 14)`** | **28** | **2.95630** | **2.82709** | **2.81393** | **1.005** | **no** |
| `(15, 15)` | 30 | 2.96157 | 2.84776 | 2.81641 | 1.011 | no |
| `(16, 16)` | 32 | 2.96595 | 2.86494 | 2.81838 | 1.017 | no |

The 2x14 rectangle `(14, 14)` is the smallest non-Ramanujan rectangle. Its graph is the 14-rung ladder, whose sandpile group is cyclic of order A001353(14) = 29,354,524 in the sink model and A001835(14) = 21,489,003 in the tide model ([[sandpile-group](pages/sandpile-group.md)]). Its second-largest adjacency eigenvalue is `lam_2 = 1 + 2 cos(2 pi / 15) = 2.82709`, and the cover-tree spectral radius is `rho(T) = 2.81393`, so `lam_2 > rho(T)` by about `0.013`. Smaller non-rectangular castles fail earlier (the census above, from 15 cells); a search over castles with two adjacent columns of height at least 8 finds `(2, 12, 12)` at 26 cells failing with ratio `1.001`.

**Independent confirmation.** The truncated-ball estimate for `(14, 14)` at depth 9 gives `rho(T)_9 = 2.7365`, still increasing toward the cavity value 2.8139. Whichever method one uses, `lam_2 = 2.8271` sits strictly above.

**Where the failure comes from.** The `2 x h` rectangle's adjacency graph is `P_h x P_2`, the ladder graph. Its spectrum has `lam_2 = 1 + 2 cos(2 pi / (h + 1))`, which approaches `3` as `h -> infty`. The universal covering tree has maximum degree 3 (the ladder's corners have degree 2 and every other cell degree 3), so its spectral radius stays below `2*sqrt(2) ~= 2.828`, and eventually `lam_2` overtakes `rho(T)`. The crossover happens at `h = 14`.

## The boxcastle census

Fixing `c = (h, h, ..., h)` with `w` columns (the `w x h` rectangle), the adjacency spectrum is exact from the product formula and `rho(T)` comes from the cavity code above. The graph is `P_w x P_h`, so `w x h` and `h x w` are the same graph. For each width, the first height `h >= w` at which the rectangle fails, computed for `h <= 16`:

| width `w` | first failing `h` | cells | `lam_2` | `rho(T)` | ratio |
|---|---|---|---|---|---|
| 2 | 14 | 28 | 2.8271 | 2.8139 | 1.005 |
| 3 | 11 | 33 | 3.1463 | 3.1099 | 1.012 |
| 4 | 10 | 40 | 3.3005 | 3.2477 | 1.016 |
| 5 | 9 | 45 | 3.3501 | 3.3141 | 1.011 |
| 6 | 9 | 54 | 3.4200 | 3.3559 | 1.019 |
| 7 | 8 | 56 | 3.3798 | 3.3702 | 1.003 |
| 8 | 8 | 64 | 3.4115 | 3.3862 | 1.007 |

In this range the ratio grows with `h` at every width, so each width fails from its threshold on. Along the diagonal `w = h` the ratios are `0.516, 0.732, 0.850, 0.923, 0.973` for `3 x 3` to `7 x 7`, then `1.007` at `8 x 8` (the first failing square) and `1.033, 1.053` at `9 x 9, 10 x 10`. Cell count alone does not decide: at 40 cells `4 x 10` fails while `5 x 8` is Ramanujan (ratio `0.988`).

## Crenellated castles

The **crenellated** type ([[castle-classification-shape](pages/castle-classification-shape.md)] Axis 7) alternates heights `(h, 1, h, 1, ...)`. No two adjacent columns both have height at least 2, so every crenellated castle is a tree castle and is Ramanujan for the reason above (`rho(T) = lam_1`):

| skyline | `lam_1` | `lam_2` | `rho(T)` | ratio |
|---|---|---|---|---|
| `cren w=13, h=5` | 2.2685 | 2.1599 | 2.2685 | 0.9521 |
| `cren w=13, h=3` | 2.2470 | 2.1284 | 2.2470 | 0.9472 |

## The Ihara / non-backtracking view

For every graph `G` there is an operator `B` on directed edges - the **non-backtracking matrix** - with `B_{(u->v), (v'->w)} = 1` if `v = v'` and `u != w`, else 0. The poles of the Ihara zeta function are the reciprocals of the eigenvalues of `B`, and the cavity equation above runs on the same directed edges. For a `d`-regular graph, `B` has spectral radius `d - 1`, `rho(T) = 2*sqrt(d - 1)`, and the Ihara-Ramanujan condition (every non-trivial eigenvalue of `B` has modulus at most `sqrt(d - 1)`) is equivalent to the adjacency one. For irregular castles `rho(T)` is not a simple function of the spectral radius `rho_B` of `B`: at `(14, 14)`, `rho_B = 1.9299`, `2*sqrt(rho_B) = 2.7785` and `rho(T) = 2.8139`. How Ihara-Ramanujan and adjacency-Ramanujan compare on castles is not worked out here.

## Open questions

1. **Rectangles as `h` grows.** Every `2 x h` rectangle with `14 <= h <= 16` fails, and every `3 x h` with `11 <= h <= 16`. Do *all* rectangles beyond some size fail, or does some family with both sides large stay Ramanujan? The 8x8 boxcastle is the first square boxcastle to fail.
2. **Asymptotic proportion.** As the cell count grows, what fraction of castles are Ramanujan? For random `d`-regular graphs, most are Ramanujan-close (Friedman 2003). In the census the non-Ramanujan fraction of non-tree castles grows from `3/6,559` at 15 cells to `6,836/964,055` at 22 cells, and the smallest failures have cycle rank 4 (two `2 x 3` blocks joined by a path).
3. **Explicit Ramanujan families among non-tree castles.** Are there infinite families of non-tree castles all of which are Ramanujan, a construction analogous to Lubotzky-Phillips-Sarnak and Margulis for castle graphs? (The crenellated castles are trees, so they do not count.)
4. **Saturating families.** For a family with a fixed universal cover, Greenberg's inequality says `lam_2` cannot stay much below `rho(T)`; whether some concrete castle family has `lam_2 - rho(T) -> 0` is open. The `2 x h` family overshoots: `lam_2 -> 3` while `rho(T)` stays below `2*sqrt(2)`.

## Reproduce

The Python program for a single castle (the census adds the `lam_2 > 2` filter and one cavity test at `z = lam_2`, footnote):

```python
import numpy as np, networkx as nx

def castle_graph(c):
    """Polyomino graph of skyline c."""
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
    A = nx.adjacency_matrix(G).astype(float).todense()
    sp = sorted(np.linalg.eigvalsh(A).tolist(), reverse=True)
    lam1, lam2 = sp[0], sp[1]
    rT = rho_cover(G)
    return {"lam_1": lam1, "lam_2": lam2, "rho_T": rT,
            "ratio": lam2 / rT, "ramanujan": lam2 <= rT + 1e-6}
```

Copy `rho_cover` from the "Two methods" section above; then `ramanujan_status((14, 14))` returns

```
{"lam_1": 2.9562952, "lam_2": 2.8270909, "rho_T": 2.8139278,
 "ratio": 1.0046778, "ramanujan": False}
```

## Appearances in Sources

- [[oeis-mining-pe502](pages/oeis-mining-pe502.md)] - the systematic OEIS-mining apparatus behind the spectral-radius census.
- [[project-euler-502-brute-force](pages/project-euler-502-brute-force.md)] - the brute-enumeration primitives the sweep is built on.

## Related Concepts

- [[castle-classification-spectrum](pages/castle-classification-spectrum.md)] - the parent classification page, where the Ramanujan predicate is one of several single-castle spectral predicates.
- [[castle-graph](pages/castle-graph.md)] - the polyomino graph and its basic invariants (bipartite, planar, max degree 4, cycle rank).
- [[castle-graph-spectral-radius](pages/castle-graph-spectral-radius.md)] - the census of adjacency-spectral-radius types (golden, silver, `phi^2`) and the Smith / Dynkin argument that closes the golden-spectrum list.
- [[isospectral-castles](pages/isospectral-castles.md)] - other single-castle spectral phenomena; isospectral pairs from 10 cells up.
- [[castle-eigenvalues-by-example](pages/castle-eigenvalues-by-example.md)] - the pedagogy page walking through small-castle adjacency spectra by hand.
- [[spectral-analysis](pages/spectral-analysis.md)] - the methods hub; the Ihara-zeta / non-backtracking side of this page's construction lives there.
- [[castle-snippets](pages/castle-snippets.md)] - `castle_graph`, `castle_graph_radius`, and related primitives; the `rho_cover` function on this page fits alongside them.
- [[hardy-ramanujan-castle](pages/hardy-ramanujan-castle.md)] - the other Ramanujan page: the taxicab number 1729 as a castle count (`F(6,4) = 1729`) and as a castle; its digit castle `(1, 7, 2, 9)` is Ramanujan in this page's spectral sense (`lam_2 = 1.898 <= rho(T) = 2.576`).

[^exec]: Verified by execution (2026-09-28, Python 3, NumPy): the cavity map `x -> 1/(z - Cx)` on directed edges, iterated from `x = 0`, increases monotonically; it converges exactly when a positive fixed point exists, which gives a positive eigenfunction of the cover at eigenvalue `z` (so `z >= rho(T)`), and it reaches a nonpositive denominator when `z < rho(T)`. `rho(T)` by bisection on that test (widths `<= 3e-5`). Census: every composition of `n <= 22` with mirror images removed; tree castles skipped (`rho(T) = lam_1`); castles with `lam_2 <= 2` skipped (`rho(T) >= 2` for a graph with a cycle); for the rest one cavity test at `z = lam_2`, with no undetermined cases. The 15-cell failures re-checked by bisection and by truncated-ball lower bounds (`2.379, 2.420, 2.439` at depths 6, 9, 12, increasing toward the cavity value `2.4729`). Rectangles `w <= h <= 16` and the ladder table by bisection. Non-backtracking spectral radii from the eigenvalues of the directed-edge matrix.
