---
title: The sandpile identity of a castle - the pile that acts like zero, in the sink and tide models
category: Concepts
summary: Every castle's sandpile group has an identity element, the one recurrent pile that changes nothing when added to another and then stabilized, and each of the two models of sandpile-group has its own. It is found by the same two-line recipe in both, stab(2m − stab(2m)) with m the fullest stable pile, and on a tree castle it is simply the fullest stable pile. Drawn for the golden path, the silver rectangle, the 10-cell isospectral pair and a 6×6 square in both models. In the sink model (one sink cell, bottom-left) the identity is irregular and depends on where the sink is: (2,2,2) and (3,3) have the same graph but different identities. In the tide model (the whole bottom row as the sink) it is strikingly regular: every rectangle at least 2 wide has 1 grain on each top cell and 2 everywhere below (checked to 12×12), and it depends only on the castle's runs of raised columns. One grain dropped on the apex of the 10-cell pair's identity sets off 57 topplings in one castle and 1 in the other in the sink model, and 1 in both under the tide. Each model has an avalanche profile, the topplings caused by one grain on each cell starting from the identity. The sink profile, taken over every sink cell, depends only on the castle's graph and separates all 105 adjacency- and all 17 Laplacian-cospectral groups to 16 cells, with no two castles that colour refinement proves non-isomorphic sharing a profile up to 13 cells. The tide profile depends only on the castle's runs and is far from complete: (2,3) and (2,2,2) already share it, and the 1,056 castles with 12 cells have only 209 tide profiles. Cospectral groups are no test for it, since every one contains skylines of different widths. The tide washes away most of the shape.
tags: [concept, castle, sandpile, identity-element, recurrent-configuration, avalanche, isospectral, laplacian, tree-castle, sink-model, tide-model, census, verification, pedagogy]
sources: [project-euler-502-castle-factoring, rossin-2000-group-of-a-sandpile, dhar-ruelle-sen-verma-1995-algebraic-aspects]
created: 2026-09-26
updated: 2026-09-27
---

# The sandpile identity of a castle - the pile that acts like zero, in the sink and tide models

## What the identity is

In the sandpile game of [[sandpile-group](pages/sandpile-group.md)], the recurrent piles form a group: add two piles cell by cell, then let the sand topple. Every group has a zero, and here it is a pile of sand. The **identity** is the recurrent pile `e` with a special property: add it to any recurrent pile, stabilize, and you get that same pile back. It is also where the [[sandcastle-clock](pages/sandcastle-clock.md)] starts ticking.

The identity is not the empty pile. The empty pile is not recurrent (it never comes back once sand has been added), so it is not in the group. The identity is a specific, usually nonzero, arrangement of grains.

**How to find it.** Let `m` be the **fullest stable pile**, every cell one grain short of toppling. Then

```
e  =  stab( 2m − stab(2m) )
```

Double the fullest pile, let it topple, subtract the result from `2m`, and let that topple too.[^1] The recipe is the same in both models; only the sink changes. For a **tree castle** there is nothing to compute in either model: its group is trivial, so its only recurrent pile, the fullest stable one, is the identity. The vertical golden path `(4)` has identity `1, 1, 0` from the bottom up in both models.

## The two models

[[sandpile-group](pages/sandpile-group.md)] defines both, and this page treats each in turn:

- the **sink model**: one sink cell, the bottom-left cell, as on the other sandpile pages;
- the **tide model**: the whole bottom row is the sink, so the ground absorbs sand all along the castle's base.

In the drawings below the top row is printed first, `~` marks sink cells, and `.` is empty sky.[^2]

| castle | sink model (bottom-left sink) | tide model (whole bottom row) |
|---|---|---|
| golden path `(4)` (vertical) | `0 / 1 / 1 / ~` | `0 / 1 / 1 / ~` |
| silver rectangle `(2, 2, 2)` | `101 / ~21` | `111 / ~~~` |
| `(3, 3)` (same graph as `(2, 2, 2)`) | `11 / 20 / ~1` | `11 / 22 / ~~` |
| 10-cell pair, A = `(1,1,1,2,3,2)` | `....0. / ...130 / ~11221` | `....0. / ...111 / ~~~~~~` |
| 10-cell pair, B = `(1,1,2,2,3,1)` | `....0. / ..121. / ~12120` | `....0. / ..111. / ~~~~~~` |

## The identity in the sink model

**The identity is irregular and depends on the sink.** `(2, 2, 2)` and `(3, 3)` are the same graph (a `3 × 2` grid, lying down or standing up) with the same group `K_sink = Z/15`. Their identities differ only because the bottom-left cell sits in a different place in the grid. On a `6 × 6` square the sink-model identity is already a scattered mix of 0s to 3s, the beginning of the intricate patterns sandpile identities are known for on large grids. (The fractal identities drawn by Dhar, Ruelle, Sen and Verma live on the open-boundary grid, which for a castle is the dual, one site per `2 × 2` block; they are not the cell-level identities on this page.)[^7]

The `6 × 6` sink-model identity:

```
021220
113202
123222
222331
222212
~22110
```

**One grain on the apex.** Start at the identity and drop one grain on the apex (the top cell of the leftmost tallest column). For the 10-cell isospectral pair of [[hear-the-shape-seminar](pages/hear-the-shape-seminar.md)], the grain sets off **57 topplings** in `A` and **1** in `B`. The two castles have the same eigenvalues and the same sink group `Z/15`, but the sand behaves completely differently. On the silver castle `(3, 2, 1, 2, 2, 1, 2, 3)` of [[sandcastle-seminar](pages/sandcastle-seminar.md)] the apex grain causes 1 toppling: the tower top passes it down and the block below absorbs it.[^2]

## The identity in the tide model

**The identity is strikingly regular.** Every rectangle at least 2 wide has identity **1 on each top-row cell and 2 on every cell below it**, checked for every rectangle from `2 × 2` to `12 × 12`.[^3] The `6 × 6` square:

```
111111
222222
222222
222222
222222
~~~~~~
```

A single column `(h)` is a tree under the tide as well, so its identity is the fullest stable pile, `1, …, 1, 0` from the bottom up.

**The identity is a property of the shape.** The ground is a canonical sink, so there is no arbitrary choice of cell. More than that, the tide splits a castle into its **runs of raised columns**, the maximal runs of adjacent columns of height at least 2 ([[sandpile-group](pages/sandpile-group.md)], Part 3). Runs never exchange sand, so the tide identity is the identity of each run, side by side, and castles with the same runs have the same tide identity whatever lies between them.

**One grain on the apex.** Under the tide the apex grain causes **1 toppling** in both castles of the 10-cell pair, and 1 on the silver castle: every tower top passes the grain down to a cell that can hold it. The 57-against-1 contrast is a sink-model effect.[^2]

## Avalanche profiles: what each identity hears

A single sink cell or a single drop cell makes a measurement depend on that choice. The fair comparison uses **every** choice the model allows. Each model has an **avalanche profile**, the number of topplings caused by one grain on each cell, starting from the identity:

- the **sink avalanche profile** takes every sink cell and every drop cell, starting from each sink cell's identity. It depends only on the castle's graph;
- the **tide avalanche profile** takes every drop cell above the ground, starting from the tide identity, as a sorted list. It depends only on the castle's runs, so it is a property of the shape, not the graph.

### The sink profile against the cospectral castles

Tested on every cospectral group of [[isospectral-castles](pages/isospectral-castles.md)] to 16 cells, alongside the sandpile group and clock spectrum from [[sandpile-census](pages/sandpile-census.md)] and [[sandcastle-clock](pages/sandcastle-clock.md)] and the identity's grain totals over every sink cell:[^4]

| sink-model invariant (graph invariants) | adjacency-cospectral groups separated (of 105) | Laplacian-cospectral groups separated (of 17) |
|---|---|---|
| sink group | 0 | 0 |
| clock spectrum | 62 | 5 |
| identity grain totals, every sink cell | 54 | 5 |
| **sink avalanche profile** | **105 (all)** | **17 (all)** |

The sink avalanche profile separates **every** cospectral group to 16 cells, including the 11-cell Laplacian pair of trees, which local return probabilities also separate ([[levy-flights](pages/levy-flights.md)]). There the sink group is trivial and the identity is just the fullest stable pile, yet the avalanches still differ. Going further, up to 13 cells no two castles that colour refinement proves non-isomorphic share a sink avalanche profile.[^5] At these sizes the sink avalanche profile behaves like a complete fingerprint of the castle graph, which neither the spectrum nor the sink group is.

### The tide profile: what it confuses

Cospectral separation is the test for graph invariants, and every sink-model invariant above is one. Tide invariants are not: they see the skyline, not just the graph. Every one of the 105 adjacency and 17 Laplacian cospectral groups contains skylines of different widths across its graph classes, so any tide count, which counts the cells above the ground, "separates" all of them for a trivial reason.[^4] That says nothing about the tide identity or the tide profile. The right tide question is what they confuse.

**The tide washes away most of the shape.** For a shape invariant the completeness question is about runs: does the tide profile determine which runs a castle has? It does not, by a wide margin. `(2, 3)` and `(2, 2, 2)`, one run each with three raised cells, already share the tide profile `0, 1, 1`. The 1,056 castles with 12 cells have only 209 distinct tide profiles, and the 2,080 with 13 cells have 336.[^6] The sink profile, over every sink cell, had no collision at all up to 13 cells.

## What this settles and what it opens

**Settled.**
- The identity is `stab(2m − stab(2m))` in both models, and on a tree castle it is the fullest stable pile in both.
- Sink model: the identity is irregular and depends on the sink cell. The sink avalanche profile separates every cospectral group to 16 cells, and no counterexample to its completeness appears up to 13 cells. This answers the clock page's open question "what the clock spectrum cannot hear" at these sizes.
- Tide model: the identity is regular, every rectangle at least 2 wide has 1 on its top row and 2 below (checked to `12 × 12`), and it depends only on the castle's runs of raised columns. Cospectral separation is not a test for tide invariants (every cospectral group mixes widths); the tide profile is far from complete on runs.

**Open.**
- Sink model: is the sink avalanche profile a complete invariant of castle graphs, or do two non-isomorphic castles share one at some larger size?
- Tide model: prove the rectangle pattern for all rectangles, and describe the tide identity of a general run beyond rectangles.
- Tide model: which finer tide invariant is complete on runs? The sorted profile throws away where each toppling count occurs; keeping positions within each run is the natural next candidate.

## Snippet

```python
def sand_board(c, sinks):                  # cells that hold sand, their non-sink neighbours, full degrees
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

- [[sandpile-group](pages/sandpile-group.md)] - the game, the two models, and the runs of raised columns under the tide.
- [[sandcastle-clock](pages/sandcastle-clock.md)] - the clock that starts at the identity; its open question about what the clock spectrum cannot hear is answered here to 16 cells.
- [[sandpile-census](pages/sandpile-census.md)] - the sandpile group of every castle in both models.
- [[isospectral-castles](pages/isospectral-castles.md)] / [[hear-the-shape-seminar](pages/hear-the-shape-seminar.md)] - the cospectral pairs.
- [[castle-graph](pages/castle-graph.md)] - tree castles, whose identity is their fullest stable pile in both models.
- [[castle-avalanches](pages/castle-avalanches.md)] - random dropping from the identity in both models.
- [[sandcastle-seminar](pages/sandcastle-seminar.md)] - the Sandcastles seminar, following the 16-cell silver castle `(3,2,1,2,2,1,2,3)` through both models.
- [[castle-eigenvalues-by-example](pages/castle-eigenvalues-by-example.md)] - the 10-cell isospectral pair worked by hand, 57 against 1 apex topplings in the sink model.

## Appearances in Sources

- [[dhar-ruelle-sen-verma-1995-algebraic-aspects](pages/dhar-ruelle-sen-verma-1995-algebraic-aspects.md)] - the identity as the recurrent configuration with all toppling invariants zero, and its fractal patterns on square grids (the dual of a castle, not its cells).
- [[rossin-2000-group-of-a-sandpile](pages/rossin-2000-group-of-a-sandpile.md)] - the identity `δ ⊕ (δ ⊕ δ)‾` from the fullest stable pile, and the unexplained fractal patterns of the identity on large grids.
- [[project-euler-502-castle-factoring](pages/project-euler-502-castle-factoring.md)] - the castle definition behind the castle graph.

## Footnotes

[^1]: https://en.wikipedia.org/wiki/Abelian_sandpile_model - the identity element of the sandpile group, its computation from the maximal stable configuration, and the fact that recurrent configurations (not the empty one) form the group. The same recipe is in [[rossin-2000-group-of-a-sandpile](pages/rossin-2000-group-of-a-sandpile.md)] §2 L33, L39 - "The simplest example of a recurrent configuration is δ = (d_1 − 1, ..., d_{n−1} − 1, 0)"; "Then the identity of the sandpile group is Id = δ ⊕ (δ ⊕ δ)‾", with `ū = δ − u`, which is `stab(2m − stab(2m))` for `m = δ`.
[^2]: Verified by execution (Python 3.10, 2026-09-26): identities computed by `stab(2m − stab(2m))` for each castle in both models; each passes `acts_as_zero` (adding it to the recurrent pile `stab(deg)` returns that pile). The drawings, the tide `6 × 6` identity, and the apex avalanches (apex cell `(4, 2)` for `A` and `B`, `(0, 2)` for the silver castle; 57, 1, 1 in the sink model and 1, 1, 1 under the tide) are pinned in the Snippet; the `6 × 6` sink-model pattern comes from the same `identity` function.
[^3]: Verified by execution (Python 3.10, 2026-09-26): for every `w × h` rectangle with `2 ≤ w ≤ 12` and `2 ≤ h ≤ 12`, the tide identity equals 1 on row `h − 1` and 2 on rows `1 … h − 2`; the single column `(5)` has tide identity `1, 1, 1, 0` from the bottom up.
[^4]: Verified by execution (Python 3.10, 2026-09-26): for the 105 adjacency and 17 Laplacian cospectral groups of [[sandpile-census](pages/sandpile-census.md)], each castle's identity grain totals over every sink cell and sink avalanche profile (topplings from one grain on each non-sink cell, starting at each sink cell's identity); a group counts as separated when its castles do not all agree. For the width statement every skyline of every graph class was kept: in all 105 adjacency and 17 Laplacian groups, two castles from different classes have different widths. The sink avalanche profile separates both 10-cell adjacency groups and the 11-cell Laplacian tree pair.
[^5]: Verified by execution (Python 3.10, 2026-09-26): for every castle with at most 13 cells (mirror images removed), castles grouped by sink avalanche profile; within each group every castle has the same colour-refinement hash (8 rounds), so no profile is shared by castles that colour refinement proves non-isomorphic. At 12 and 13 cells there are 321 and 625 distinct sink profiles among 1,056 and 2,080 castles; castles sharing a profile are different skylines of the same graph as far as colour refinement can tell. About 40 seconds to 13 cells.
[^6]: Verified by execution (Python 3.10, 2026-09-26): tide avalanche profiles for every castle with 12 and 13 cells (mirror images removed), 209 and 336 distinct; grouping castles by their multiset of runs (each run taken up to mirror image), the tide group and tide profile depend only on the runs for every castle to 12 cells, and two different run multisets share a tide profile from 3 raised cells on (`(2, 3)` and `(2, 2, 2)`, pinned in the Snippet).
[^7]: [[dhar-ruelle-sen-verma-1995-algebraic-aspects](pages/dhar-ruelle-sen-verma-1995-algebraic-aspects.md)] §7 Question 2 pp. 28-30 and Appendix C pp. 35-36 - "The identity configuration shows complicated fractal structures", on `L × L` square lattices with open boundaries on all four sides; the dual-grid reading is the wiki's.
