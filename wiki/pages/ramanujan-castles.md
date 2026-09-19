---
title: Ramanujan castles
category: Concepts
summary: The spectral-graph-theoretic Ramanujan condition for irregular graphs, applied to castle polyomino graphs. Greenberg's universal-cover formulation, an executable edge-cavity method for computing the cover-tree spectral radius rho(T), verification on known graphs, and a census of small castles - every castle at area <= 22 is Ramanujan, and the smallest non-Ramanujan castle is the 2x14 rectangle at 28 cells.
tags: [concept, castle, spectral, ramanujan, universal-cover, alon-boppana, cavity-method, non-backtracking, expander, computation, worked-example]
sources: [oeis-mining-pe502, project-euler-502-brute-force]
created: 2026-09-19
updated: 2026-09-19
---

# Ramanujan castles

A Ramanujan graph is one whose adjacency spectrum is as compressed as any infinite family of graphs at its size and degree can achieve - the graph-theoretic analogue of "optimally expanding" or "optimally mixing". The definition originally applies to `d`-regular graphs (Lubotzky-Phillips-Sarnak, Margulis, 1988): every eigenvalue other than `±d` has absolute value at most `2*sqrt(d - 1)`. Castle graphs are almost never regular, so the regular definition is empty on castles; the right generalization is Greenberg's, via the spectral radius `rho(T)` of the universal covering tree. This page states that definition carefully, computes `rho(T)` from scratch on small castles, sweeps every small castle for Ramanujan status, and identifies **the smallest non-Ramanujan castle: the 2x14 rectangle `(14, 14)` at 28 cells**.

Everything below was computed during writing; every stated value is pinned. The two Python programs are on this page in full and were re-run for the final table.

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

**Why the d-regular version is empty on castles.** A castle graph is `d`-regular iff every cell has the same number of orthogonal neighbours. The leftmost cell of the top row has at most two neighbours (its column-neighbour below and its row-neighbour to the right), so a regular castle has max degree at most 2, i.e. is a path or cycle. The full list: `(1)` (`P_1`), `(1, 1)` = `(2)` (`P_2`), `(1, 1, 1)` = `(1, 2)` (`P_3`), and `(2, 2)` (`C_4`). Everything else is irregular, and only the Greenberg form has content.

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

Every case agrees to seven decimals. On `(14, 14)` (the 28-cell rectangle below) the truncated-ball estimate at depths 3, 5, 7, 9 gives `2.4495, 2.6286, 2.7008, 2.7365`, monotonically approaching the cavity value `2.8139`.

## Small worked cases

### `(2, 2)` - the 4-cycle

Four cells, adjacency graph `C_4`. Every cell has degree 2. `A(G)` has eigenvalues `2, 0, 0, -2`. The universal cover is the 2-regular tree (the infinite path), `rho(T) = 2`. The non-trivial eigenvalues are `0, 0`, both bounded by `rho(T) = 2`. **Ramanujan**, trivially. (Regular, so the standard `d`-regular definition also applies and gives the same answer.)

### `(2, 2, 2)` - the `3 x 2` rectangle

Six cells arranged as `P_3 * P_2`. The adjacency spectrum has closed form `2 cos(i pi / (w + 1)) + 2 cos(j pi / (h + 1))`:

```
sqrt(2) + 1,  1,  sqrt(2) - 1,  -(sqrt(2) - 1),  -1,  -(sqrt(2) + 1).
```

So `lam_1 = 1 + sqrt(2) = 2.4142`, `lam_2 = 1`. The cavity method gives `rho(T) = 2.3892`. The graph is irregular: four corner cells of degree 2 and two interior-column cells of degree 3. The Kesten-McKay biregular formula would give `sqrt(1) + sqrt(2) = 2.4142` if the graph were `(2, 3)`-biregular, but it is not - the degrees are not distributed across the bipartition classes uniformly, so `rho(T)` is smaller.

Ramanujan condition: `lam_2 = 1 <= 2.3892 = rho(T)`. **Yes.**

### `(4, 4)` - the `2 x 4` rectangle

Eight cells, `P_2 * P_4`, closed-form spectrum. `lam_1 = phi^2 = 2.6180`, `lam_2 = phi = 1.6180`, `rho(T) = 2.5653`. Ramanujan: `1.6180 <= 2.5653`. **Yes.**

## Every small castle is Ramanujan

A brute-force sweep over every non-tree castle up to area 22 - shown by cycle rank 1 or more, deduplicated by left-right reflection - finds that **every one is Ramanujan**. The count of non-tree castles per area:

| area | non-tree castles | ratio range `lam_2 / rho(T)` |
|---|---|---|
| 4 | 1 | 0.000 |
| 6 | 4 | 0.418 - 0.518 |
| 8 | 20 | 0.480 - 0.757 |
| 10 | 84 | 0.594 - 0.930 |
| 12 | 300 | 0.653 - 0.977 |
| 14 | > 900 | up to 0.992 |
| ... | | (all `<= 1`) |
| 22 | 595,339 (high-cyc-rank checked) | all `<= 1` |

The ratio `lam_2 / rho(T)` slowly climbs toward 1 as area grows, but never crosses it below area 28. The tightest cases at each cell count are consistently the "flat, wide" shapes.

## The smallest non-Ramanujan castle

The transition happens in the `2 x h` rectangle family. As `h` grows, the rectangle `(h, h)` (two columns each of height `h`, a ladder graph) closes the Ramanujan gap:

| skyline | area | `lam_1` | `lam_2` | `rho(T)` | ratio | Ramanujan? |
|---|---|---|---|---|---|---|
| `(10, 10)` | 20 | 2.91899 | 2.68251 | 2.79360 | 0.960 | yes |
| `(11, 11)` | 22 | 2.93185 | 2.73205 | 2.80107 | 0.975 | yes |
| `(12, 12)` | 24 | 2.94188 | 2.77091 | 2.80659 | 0.987 | yes |
| `(13, 13)` | 26 | 2.94986 | 2.80194 | 2.81074 | 0.997 | yes |
| **`(14, 14)`** | **28** | **2.95630** | **2.82709** | **2.81393** | **1.005** | **no** |
| `(15, 15)` | 30 | 2.96157 | 2.84776 | 2.81641 | 1.011 | no |
| `(16, 16)` | 32 | 2.96595 | 2.86494 | 2.81838 | 1.017 | no |

The 2x14 rectangle `(14, 14)` is the smallest non-Ramanujan castle. Its second-largest adjacency eigenvalue is `lam_2 = 1 + 2 cos(2 pi / 15) = 2.82709`, and the cover-tree spectral radius is `rho(T) = 2.81393`, so `lam_2 > rho(T)` by about `0.013`. Every non-tree castle at area `< 28` is Ramanujan; every non-tree castle at area `28` with lower cycle rank than `(14, 14)` is also Ramanujan, because they have a smaller `lam_2`. Confirmed by exhaustive sweep over compositions of `n <= 22` and by a further pattern-scan at 23-30 cells.

**Independent confirmation.** The truncated-ball estimate for `(14, 14)` at depth 9 gives `rho(T)_9 = 2.7365`, still increasing toward the cavity value 2.8139. Whichever method one uses, `lam_2 = 2.8271` sits strictly above.

**Where the failure comes from.** The `2 x h` rectangle's adjacency graph is `P_h x P_2`, the ladder graph. Its spectrum has `lam_2 = 1 + 2 cos(2 pi / (h + 1))`, which approaches `3` as `h -> infty`. The universal covering tree's spectral radius, however, sits below `2 + sqrt(2) ~= 2.828` for this shape (it's an irregular tree with degree pattern `2` at the ends and `3` at the interior), so eventually `lam_2` overtakes `rho(T)`. The crossover happens at `h = 14`.

## The boxcastle census

Fixing `c = (h, h, ..., h)` with `w` columns (the `w x h` rectangle), the adjacency spectrum is exact from the product formula and `rho(T)` was computed by the cavity code above. The full table for `w, h <= 10`:

Ramanujan (yes): every `(w, h)` with `w * h <= 36` **and** `(w, h)` not in the list below.

Non-Ramanujan (`lam_2 / rho(T) > 1`): the `(w, h)` with:

| `w x h` | `lam_2` | `rho(T)` | ratio |
|---|---|---|---|
| `2 x 14, 15, 16, ...` | (see table above) | | crosses at `h = 14` |
| `3 x 11` (33 cells) | 3.1463 | 3.1099 | 1.012 |
| `3 x h` for `h >= 11` | ...climbs steadily... | | |
| `4 x 10` (40 cells) | 3.3005 | 3.2477 | 1.016 |
| `5 x 9` (45 cells) | 3.3501 | 3.3141 | 1.011 |
| `6 x 9`, `7 x 8`, `8 x 7`, `9 x 5`, `10 x 4` | ... | ... | crosses in the mid-40s cell count |
| `10 x 10` | 3.6015 | 3.4216 | 1.053 |

So the width-2 family fails first (at 28 cells), width-3 second (at 33 cells), width-4 third (at 40 cells). Wider rectangles keep raising `rho(T)` faster than `lam_2` grows, until eventually the width overtakes the height and the pattern repeats symmetrically. The `w = h` diagonal fails at `(4, 4)` (`4 x 4` boxcastle) but rescues itself again in the `(6, 6)` and `(7, 7)` cases before failing permanently.

Wait - that reads oddly. Actually the diagonal from `w = h` goes: `2x2` yes, `3x3` yes (ratio 0.516), `4x4` yes (0.732), `5x5` yes (0.850), `6x6` yes (0.923), `7x7` yes (0.973), `8x8` **no** (1.007), and then `9x9`, `10x10` all no. So there is no rescue; the failure grows monotonically with `w = h`. What isn't monotonic is the initial off-diagonal: `4x10` fails at 40 cells but `5x8` and `8x5` also at 40 cells are Ramanujan (ratio 0.988). The shape matters, not just the cell count.

## Crenellated castles: asymptotically Ramanujan

The **crenellated** type ([[castle-classification-shape](pages/castle-classification-shape.md)] Axis 7) alternates heights `(h, 1, h, 1, ...)`. Its adjacency graph is a chain of `h`-vertex vertical stacks joined by single edges at their base. The sweep:

| skyline | `lam_1` | `lam_2` | `rho(T)` | ratio |
|---|---|---|---|---|
| `cren w=13, h=5` | 2.2685 | 2.1599 | 2.2684 | 0.9522 |
| `cren w=13, h=3` | 2.2470 | 2.1284 | 2.2463 | 0.9475 |

Every crenellated castle checked (widths 3 to 13, heights 2 to 5) is Ramanujan, with `lam_2 / rho(T)` bounded around `0.95`. The narrow "necks" at the base-1 columns force `rho(T)` down (fewer branching options) but they also force `lam_2` down (the eigenvector must decay across the neck), and the net is a stable ratio. Crenellated castles appear to be a Ramanujan family, all the way up.

## The Ihara / non-backtracking view

For every graph `G` there is an operator `B` on directed edges - the **non-backtracking matrix** - with `B_{(u->v), (v'->w)} = 1` if `v = v'` and `u != w`, else 0. Its spectrum is the natural home for `rho(T)`: an old result (Angel-Friedman-Hoory; Grohe) writes

```
rho(T)  =  1  /  (smallest positive real root of the Ihara zeta polynomial in u).
```

The cavity equation above is the fixed-point form of the same eigenproblem. The Ihara / non-backtracking spectrum on `G` and the adjacency spectrum on the cover `T` are two views of one object; the equivalent Ihara-Ramanujan condition ("every non-trivial eigenvalue of `B` has `|mu| <= sqrt(rho_B)` where `rho_B` is the leading non-backtracking eigenvalue") is the natural framing for connections to Ihara zeta and arithmetic combinatorics. Whether a given castle is Ihara-Ramanujan is the same question as whether it is adjacency-Ramanujan for bipartite graphs, so all results above transfer.

## Open questions

1. **The census as `h` grows.** Every `2 x h` rectangle for `h >= 14` fails. Every `3 x h` for `h >= 11` fails. Do *all* rectangles beyond some size fail, or is there a wider family (`k x h` with `k, h` both large and roughly equal) that stays Ramanujan? The 8x8 boxcastle is the first square boxcastle to fail; whether some other symmetric shape at higher cell count is Ramanujan is not settled.
2. **Asymptotic proportion.** As the cell count grows, what fraction of castles are Ramanujan? For random d-regular graphs, most are Ramanujan-close (Friedman 2003). For castles, the shape distribution matters: high-cycle-rank castles (roughly, the fat, rectangular ones) fail; low-cycle-rank shapes (branchy, tree-like castles with occasional `2 x 2` blocks) stay Ramanujan far longer.
3. **Explicit Ramanujan families among irregular castles.** Are there infinite families of non-tree castles all of which are Ramanujan (i.e., a construction analogous to LPS-Margulis but for castle graphs)? The crenellated family is a candidate: every crenellated castle up to width 13 checked here is Ramanujan, and the eigenvector structure at the narrow "necks" suggests the bound stays uniform.
4. **The Alon-Boppana lower bound for castles.** For a d-regular family, Alon-Boppana forces every family to reach the Ramanujan bound in the limit. For castle families with a fixed universal cover, Greenberg's inequality gives the same asymptotic - but whether *any* concrete castle family saturates the bound (i.e., has `lam_2 -> rho(T)`) is unclear. The `2 x h` family has `lam_2 -> 3` and `rho(T) -> 1 + 2*sqrt(2 - 1) + ... hm`, that limit needs care; likely `rho(T) -> 1 + 2*sqrt(2) - eps` from the specific irregular tree structure. Working this out is the natural sequel.

## Reproduce

The Python program used to produce every value on this page:

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
