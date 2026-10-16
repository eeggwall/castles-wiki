---
title: The sandpile identity of a castle - the pile that acts like zero, in the sink and tide models
category: Concepts
summary: The identity element of a castle's sandpile group, in the sink model (one sink cell, here the bottom-left cell) and the tide model (the whole bottom row as the sink) of sandpile-group, computed by Rossin's recipe stab(2m − stab(2m)) with m the fullest stable pile; on a tree castle it is the fullest stable pile itself. In the sink model the identity depends on the sink cell (on the rectangle (2, 2, 2), sink at a corner or in the middle of the bottom row gives different identities). In the tide model every rectangle at least 2 wide has identity 1 on each top-row cell and 2 below (computed for 2 ≤ w, h ≤ 12), and the identity depends only on the castle's runs of raised columns. The sink avalanche profile, the topplings caused by one grain on each cell from the identity over every choice of sink cell, separates all 105 adjacency- and 17 Laplacian-cospectral groups to 16 cells, and up to 13 cells two castles share it exactly when their graphs are isomorphic. The tide avalanche profile depends only on the runs; the 1,056 castles with 12 cells have 209 tide profiles.
tags: [concept, castle, sandpile, identity-element, recurrent-configuration, avalanche, isospectral, laplacian, tree-castle, sink-model, tide-model, census, verification, pedagogy]
sources: [project-euler-502-castle-factoring, rossin-2000-group-of-a-sandpile, dhar-ruelle-sen-verma-1995-algebraic-aspects]
created: 2026-09-26
updated: 2026-10-16
---

# The sandpile identity of a castle - the pile that acts like zero, in the sink and tide models

## What the identity is

The recurrent configurations of the sandpile on a castle form a group under "add cell by cell, then stabilize" ([[sandpile-group](pages/sandpile-group.md)]). Its **identity** is the recurrent configuration `e` such that adding `e` to any recurrent configuration and stabilizing returns that configuration. The [[sandcastle-clock](pages/sandcastle-clock.md)] starts at it.

The identity is not the empty configuration: no addition of sand followed by stabilization returns to the empty configuration, so it is not recurrent.

**Computing it.** Let `m` be the **fullest stable configuration**, with every cell one grain short of toppling. Rossin writes `δ` for `m`, `ū = δ − u`, and gives the identity as `δ ⊕ (δ ⊕ δ)‾`, which is[^1]

```
e  =  stab( 2m − stab(2m) )
```

The recipe is the same in both models; only the sink changes. A **tree castle**, a castle with no `2 × 2` block of cells, has a trivial group in both models ([[sandpile-group](pages/sandpile-group.md)], the Proposition in Part 3), so its only recurrent configuration, the fullest stable one, is the identity. The column `(4)` has identity `1, 1, 0` from the bottom up in both models.

## The two models

[[sandpile-group](pages/sandpile-group.md)] defines both:

- the **sink model**: one sink cell, here the bottom-left cell;
- the **tide model**: the whole bottom row is the sink.

In the drawings the top row is printed first, `~` marks sink cells, and `.` is empty space.[^2]

| castle | sink model (bottom-left sink) | tide model (whole bottom row) |
|---|---|---|
| column `(4)`, golden by spectrum (castle-graph spectral radius `φ`) | `0 / 1 / 1 / ~` | `0 / 1 / 1 / ~` |
| rectangle `(2, 2, 2)`, silver by spectrum (spectral radius `1 + √2`) | `101 / ~21` | `111 / ~~~` |
| `(3, 3)`, the same graph as `(2, 2, 2)` | `11 / 20 / ~1` | `11 / 22 / ~~` |
| 10-cell pair, A = `(1,1,1,2,3,2)` | `....0. / ...130 / ~11221` | `....0. / ...111 / ~~~~~~` |
| 10-cell pair, B = `(1,1,2,2,3,1)` | `....0. / ..121. / ~12120` | `....0. / ..111. / ~~~~~~` |

## The identity in the sink model

**The identity depends on the sink cell.** On `(2, 2, 2)` with the sink at the bottom-left corner the identity is `101 / ~21`; with the sink at the middle of the bottom row it is `121 / 0~0`. The group is `Z/15` in both cases, since the sandpile group does not depend on the sink.[^2] `(3, 3)` is `(2, 2, 2)` turned on its side, which maps the bottom-left corner of one onto the bottom-left corner of the other, and its identity `11 / 20 / ~1` is the transposed drawing of `101 / ~21`.

On a `6 × 6` square the sink-model identity takes the values 0 to 3 without a visible pattern:

```
021220
113202
123222
222331
222212
~22110
```

Dhar, Ruelle, Sen and Verma draw fractal identity configurations on `L × L` grids with open boundaries on all four sides.[^3] For a castle that grid is the dual one, with one site per `2 × 2` block: the sink block matrix of the `(L + 1) × (L + 1)` castle is the Laplacian of the open-boundary `L × L` grid ([[sandpile-group](pages/sandpile-group.md)]). Their pictures therefore show configurations on the blocks, not the cell-level identities of this page.

**One grain on the apex.** Start at the identity and drop one grain on the apex, the top cell of the leftmost tallest column. On the 10-cell adjacency-cospectral pair of [[hear-the-shape-seminar](pages/hear-the-shape-seminar.md)] the grain causes **57 topplings** in `A` and **1** in `B`. The two castles have the same adjacency spectrum and the same sink group `Z/15`. On the castle `(3, 2, 1, 2, 2, 1, 2, 3)` of [[sandcastle-seminar](pages/sandcastle-seminar.md)] the apex grain causes 1 toppling: the apex topples once and no other cell does.[^2]

## The identity in the tide model

**Rectangles.** Every rectangle at least 2 wide has tide identity **1 on each top-row cell and 2 on every cell below it, above the ground**, computed for every rectangle from `2 × 2` to `12 × 12`.[^4] The `6 × 6` square:

```
111111
222222
222222
222222
222222
~~~~~~
```

A single column `(h)` is a tree in the tide model as well, so its identity is the fullest stable configuration, `1, …, 1, 0` from the bottom up.

**The identity depends only on the runs.** The sink is the whole bottom row, so no cell has to be chosen. The **runs of raised columns** are the maximal runs of adjacent columns of height at least 2 ([[sandpile-group](pages/sandpile-group.md)], Part 3). Two cells in different runs are never neighbors, so no grain passes between runs, and the tide identity is the identity of each run, side by side. Castles with the same runs have the same tide identity on them, wherever the runs stand along the bottom row.

**One grain on the apex.** In the tide model the apex grain causes **1 toppling** in both castles of the 10-cell pair, and 1 on `(3, 2, 1, 2, 2, 1, 2, 3)`: in each, the apex topples once and no other cell does.[^2]

## Avalanche profiles

A measurement made with one sink cell or one drop cell depends on that choice. Each model has an **avalanche profile** that makes every choice the model allows: the number of topplings caused by one grain on each cell, starting from the identity.

- The **sink avalanche profile** is the sorted list of these counts over every sink cell `d` and every drop cell `v ≠ d`, starting from the identity for `d`. It depends only on the castle's graph.
- The **tide avalanche profile** is the sorted list over every cell above the bottom row, starting from the tide identity. It depends only on the castle's runs.

### The sink profile on the cospectral castles

On every cospectral group of [[isospectral-castles](pages/isospectral-castles.md)] to 16 cells, with every skyline of every graph in the group, a group counts as separated by an invariant when two castles in it get different values:[^5]

| sink-model invariant (each depends only on the graph) | adjacency-cospectral groups separated (of 105) | Laplacian-cospectral groups separated (of 17) |
|---|---|---|
| sink group | 0 | 0 |
| sink clock spectrum ([[sandcastle-clock](pages/sandcastle-clock.md)]) | 62 | 5 |
| total grains of the identity, for every sink cell | 54 | 5 |
| **sink avalanche profile** | **105 (all)** | **17 (all)** |

The sink avalanche profile separates every cospectral group to 16 cells, including the 11-cell pair of Laplacian-cospectral trees `(1,1,1,2,1,1,2,1,1)` and `(1,1,3,1,1,1,2,1)`. Both are trees, so their sink groups are trivial and their identities are their fullest stable configurations, and the avalanches still differ.

**Up to 13 cells the sink profile determines the graph.** For castles with at most 13 cells, two castles have the same sink avalanche profile exactly when their castle graphs are isomorphic: the 1,056 castles with 12 cells have 321 graphs and 321 profiles, and the 2,080 with 13 cells have 625 graphs and 625 profiles.[^6] The adjacency and Laplacian spectra and the sink group do not determine the graph at these sizes.

### The tide profile

Cospectral groups are not a test for tide invariants. Every one of the 105 adjacency and 17 Laplacian cospectral groups contains castles of different widths across its graphs, so any tide count over the cells above the bottom row differs within it.[^5] What matters for a tide invariant is which castles it fails to tell apart.

The tide avalanche profile depends only on the runs, and it does not determine them. `(2, 3)` and `(2, 2, 2)`, one run each with three raised cells, have the same tide profile `0, 1, 1`. The 1,056 castles with 12 cells have 209 distinct tide profiles, and the 2,080 with 13 cells have 336.[^7]

## Snippet

```python
def sand_board(c, sinks):                  # cells that hold sand, their non-sink neighbors, full degrees
    cells = [(i, j) for i, h in enumerate(c) for j in range(h)]
    S = set(cells)
    def nbs(v):
        i, j = v
        return [u for u in ((i+1, j), (i-1, j), (i, j+1), (i, j-1)) if u in S]
    live = [v for v in cells if v not in sinks]
    return live, {v: [u for u in nbs(v) if u not in sinks] for v in live}, {v: len(nbs(v)) for v in live}

def sink_cell(c):   return {(0, 0)}                                   # sink model: the bottom-left cell
def tide(c):        return {(i, 0) for i in range(len(c))}            # tide model: the whole bottom row

def stabilize(board, g):                   # returns the settled pile and the number of topplings
    live, nb, deg = board
    g, topples = dict(g), 0
    while any(g[v] >= deg[v] for v in live):
        for v in live:
            if g[v] >= deg[v]:
                q = g[v] // deg[v]; g[v] -= q * deg[v]; topples += q
                for u in nb[v]:
                    g[u] += q
    return g, topples

def identity(c, sinks):                    # stab(2m - stab(2m)), m = the fullest stable pile
    board = sand_board(c, sinks)
    live, nb, deg = board
    m = {v: deg[v] - 1 for v in live}
    s, _ = stabilize(board, {v: 2 * m[v] for v in live})
    return stabilize(board, {v: 2 * m[v] - s[v] for v in live})[0]

def draw(c, e):                            # top row first; sink cells drawn as '~'
    return [''.join('.' if j >= h else str(e[(i, j)]) if (i, j) in e else '~' for i, h in enumerate(c))
            for j in range(max(c) - 1, -1, -1)]

def acts_as_zero(c, sinks):                # adding the identity to a recurrent pile changes nothing
    board = sand_board(c, sinks); live, nb, deg = board
    r, _ = stabilize(board, {v: deg[v] for v in live})                 # a recurrent pile
    return stabilize(board, {v: r[v] + identity(c, sinks)[v] for v in live})[0] == r

def avalanche(c, sinks, v):                # topplings caused by one grain at v, starting from the identity
    board = sand_board(c, sinks); e = identity(c, sinks); e[v] += 1
    return stabilize(board, e)[1]

def apex(c):                               # top cell of the leftmost tallest column
    return (c.index(max(c)), max(c) - 1)

def sink_profile(c):                       # sink model: every sink cell, every drop cell; depends only on the graph
    cells = [(i, j) for i, h in enumerate(c) for j in range(h)]
    return sorted(avalanche(c, {d}, v) for d in cells for v in cells if v != d)

def tide_profile(c):                       # tide model: every drop cell above the ground; depends only on the runs
    return sorted(avalanche(c, tide(c), v) for v in sand_board(c, tide(c))[0])
```

```
>>> draw((2, 2, 2), identity((2, 2, 2), sink_cell((2, 2, 2)))), draw((2, 2, 2), identity((2, 2, 2), tide((2, 2, 2))))
(['101', '~21'], ['111', '~~~'])
>>> draw((3, 3), identity((3, 3), sink_cell((3, 3)))), draw((3, 3), identity((3, 3), tide((3, 3))))
(['11', '20', '~1'], ['11', '22', '~~'])
>>> draw((4,), identity((4,), sink_cell((4,)))), draw((4,), identity((4,), tide((4,))))    # a tree: the fullest stable pile
(['0', '1', '1', '~'], ['0', '1', '1', '~'])
>>> A, B, C = (1, 1, 1, 2, 3, 2), (1, 1, 2, 2, 3, 1), (3, 2, 1, 2, 2, 1, 2, 3)
>>> draw(A, identity(A, sink_cell(A))), draw(B, identity(B, sink_cell(B)))
(['....0.', '...130', '~11221'], ['....0.', '..121.', '~12120'])
>>> [(avalanche(c, sink_cell(c), apex(c)), avalanche(c, tide(c), apex(c))) for c in (A, B, C)]
[(57, 1), (1, 1), (1, 1)]
>>> all(acts_as_zero(c, d(c)) for c in [(2, 2, 2), (3, 3), A, B, (6,) * 6] for d in (sink_cell, tide))
True
>>> draw((6,) * 6, identity((6,) * 6, tide((6,) * 6)))
['111111', '222222', '222222', '222222', '222222', '~~~~~~']
>>> S, T = (1, 1, 1, 2, 1, 1, 2, 1, 1), (1, 1, 3, 1, 1, 1, 2, 1)
>>> sink_profile(S) == sink_profile(T), sink_profile(A) == sink_profile(B)
(False, False)
>>> tide_profile((2, 3)), tide_profile((2, 2, 2)), tide_profile((1, 1, 2, 2)) == tide_profile((1, 2, 2, 1))
([0, 1, 1], [0, 1, 1], True)
```

## Related Concepts

- [[sandpile-group](pages/sandpile-group.md)] - the sandpile, the two models, the groups, and the runs of raised columns in the tide model.
- [[sandcastle-clock](pages/sandcastle-clock.md)] - the clock that starts at the identity, and the sink clock spectrum, which separates 62 of the 105 adjacency-cospectral groups.
- [[sandpile-census](pages/sandpile-census.md)] - the sandpile groups of every castle to 16 cells in both models.
- [[isospectral-castles](pages/isospectral-castles.md)] - the adjacency- and Laplacian-cospectral castles to 16 cells; [[hear-the-shape-seminar](pages/hear-the-shape-seminar.md)] - a seminar built on them.
- [[castle-graph](pages/castle-graph.md)] - tree castles, whose identity is their fullest stable configuration in both models.
- [[castle-avalanches](pages/castle-avalanches.md)] - grains dropped on random cells from the identity, in both models.
- [[sandcastle-seminar](pages/sandcastle-seminar.md)] - the castle `(3,2,1,2,2,1,2,3)` followed through both models.
- [[castle-eigenvalues-by-example](pages/castle-eigenvalues-by-example.md)] - the 10-cell cospectral pair worked by hand, with its 57 and 1 apex topplings in the sink model.

## Appearances in Sources

- [[rossin-2000-group-of-a-sandpile](pages/rossin-2000-group-of-a-sandpile.md)] - the identity `δ ⊕ (δ ⊕ δ)‾` from the fullest stable configuration `δ`, and the remark that the identity "presents fractal aspects that we are not able yet to explain".
- [[dhar-ruelle-sen-verma-1995-algebraic-aspects](pages/dhar-ruelle-sen-verma-1995-algebraic-aspects.md)] - the identity as the recurrent configuration whose toppling invariants all vanish, and its fractal patterns on open-boundary square grids.
- [[project-euler-502-castle-factoring](pages/project-euler-502-castle-factoring.md)] - the castle definition behind the castle graph.

## Footnotes

[^1]: [[rossin-2000-group-of-a-sandpile](pages/rossin-2000-group-of-a-sandpile.md)] §2 L33, L37-39 - "The simplest example of a recurrent configuration is δ = (d_1 − 1, d_2 − 1, ..., d_{n−1} − 1, 0)"; "u ⊕ v = (u+v)^"; "We denote ū the recurrent configuration (d_1 − 1 − u_1, d_2 − 1 − u_2, ..., d_{n−1} − 1 − u_{n−1}, 0). Then the identity of the sandpile group is Id = δ ⊕ (δ ⊕ δ)‾". With `δ = m`, `δ ⊕ δ = stab(2m)` and `δ ⊕ (m − stab(2m)) = stab(2m − stab(2m))`.
[^2]: Verified by execution (Python 3.11, 2026-10-16): identities by `stab(2m − stab(2m))` for each castle in both models, each acting as zero on the recurrent configuration `stab(deg)`; the drawings, the `(2, 2, 2)` identities for the sink at `(0, 0)` and at `(1, 0)`, the `6 × 6` identities, and the apex avalanches (apex `(4, 2)` for `A` and `B`, `(0, 2)` for `(3,2,1,2,2,1,2,3)`: 57, 1, 1 in the sink model and 1, 1, 1 in the tide model). Several are pinned in the Snippet.
[^3]: [[dhar-ruelle-sen-verma-1995-algebraic-aspects](pages/dhar-ruelle-sen-verma-1995-algebraic-aspects.md)] §7 Question 2 pp. 28-30 and Appendix C pp. 35-36 - "The identity configuration shows complicated fractal structures", on `L × L` square lattices with open boundaries on all four sides.
[^4]: Verified by execution (Python 3.11, 2026-10-16): for every `w × h` rectangle with `2 ≤ w ≤ 12` and `2 ≤ h ≤ 12`, the tide identity is 1 on row `h − 1` and 2 on rows `1, …, h − 2`; the column `(5)` has tide identity `1, 1, 1, 0` from the bottom up.
[^5]: Verified by execution (Python 3.11, NumPy, networkx, 2026-10-16): all 33,150 castles with at most 16 cells (mirror images removed) grouped by adjacency and by Laplacian spectrum, each group split into graph classes by exact isomorphism tests, every group confirmed by exact characteristic polynomials: 105 adjacency and 17 Laplacian groups with two or more graphs. For each of their 1,128 castles: the sink group, the sink clock spectrum, the total grains of the identity for every sink cell, and the sink avalanche profile, each equal on castles with the same graph; separated counts as tabulated. In every group two castles with different graphs have different widths.
[^6]: Verified by execution (Python 3.11, networkx, 2026-10-16): the sink avalanche profiles of all castles with at most 13 cells (mirror images removed); castles grouped by profile, and every pair in a group tested for graph isomorphism exactly: no two castles with non-isomorphic graphs share a profile; 321 profiles and 321 graph classes among the 1,056 castles with 12 cells, 625 and 625 among the 2,080 with 13.
[^7]: Verified by execution (Python 3.11, 2026-10-16): tide avalanche profiles of every castle with 12 and 13 cells (mirror images removed), 209 and 336 distinct; grouping all castles with at most 12 cells by their multiset of runs, each run taken up to mirror image, every group has a single tide profile; `(2, 3)` and `(2, 2, 2)` share `0, 1, 1` (pinned in the Snippet).
