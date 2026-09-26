---
title: The sandpile identity of a castle - the pile that acts like zero
category: Concepts
summary: Every castle's sandpile group has an identity element, the one recurrent pile that changes nothing when added to another and then stabilized. It is found by a two-line recipe, stab(2m − stab(2m)) with m the fullest stable pile, and on a tree castle it is simply the fullest stable pile. Drawn for the golden path, the silver rectangle, the 10-cell isospectral pair and a 6×6 square in two drain models. With a single drain cell the identity is irregular and depends on where the drain is: (2,2,2) and (3,3) have the same graph but different identities. With the whole bottom row as the drain (the tide) it is strikingly regular: every rectangle at least 2 wide has 1 grain on each top cell and 2 everywhere below. One grain dropped on the apex of the 10-cell pair's identity sets off 57 topplings in one castle and 1 in the other. The avalanche profile - topplings caused by one grain on every cell, from every drain's identity - depends only on the castle's graph and separates all 105 adjacency- and all 17 Laplacian-cospectral groups to 16 cells, including the 11-cell tree pair. No two castles that colour refinement proves non-isomorphic share a profile up to 13 cells.
tags: [concept, castle, sandpile, identity-element, recurrent-configuration, avalanche, isospectral, laplacian, tree-castle, tide, census, verification, pedagogy]
sources: [project-euler-502-castle-factoring]
created: 2026-09-26
updated: 2026-09-26
---

# The sandpile identity of a castle - the pile that acts like zero

## What the identity is

In the sandpile game of [[sandpile-group](pages/sandpile-group.md)], the recurrent piles form a group: add two piles cell by cell, then let the sand topple. Every group has a zero, and here it is a pile of sand. The **identity** is the recurrent pile `e` with a special property: add it to any recurrent pile, stabilize, and you get that same pile back. It is also where the [[sandcastle-clock](pages/sandcastle-clock.md)] starts ticking.

The identity is not the empty pile. The empty pile is not recurrent (it never comes back once sand has been added), so it is not in the group. The identity is a specific, usually nonzero, arrangement of grains.

**How to find it.** Let `m` be the **fullest stable pile**, every cell one grain short of toppling. Then

```
e  =  stab( 2m − stab(2m) )
```

Double the fullest pile, let it topple, subtract the result from `2m`, and let that topple too.[^1] The recipe works for any choice of drain. For a **tree castle** there is nothing to compute: its group is trivial, so its only recurrent pile, the fullest stable one, is the identity. The vertical golden path `(4)` has identity `1, 1, 0` from the bottom up.

## Two ways to drain the sand

Where the sand leaves changes the identity, so this page draws both models from [[sandpile-group](pages/sandpile-group.md)]:

- **one drain cell**, the bottom-left cell, as on the other sandpile pages;
- **the tide**: the whole bottom row is the drain, so the ground absorbs sand all along the castle's base.

In the drawings below the top row is printed first, `~` marks drain cells, and `.` is empty sky.[^2]

| castle | one drain cell (bottom-left) | tide (whole bottom row) |
|---|---|---|
| golden path `(4)` (vertical) | `0 / 1 / 1 / ~` | `0 / 1 / 1 / ~` |
| silver rectangle `(2, 2, 2)` | `101 / ~21` | `111 / ~~~` |
| `(3, 3)` (same graph as `(2, 2, 2)`) | `11 / 20 / ~1` | `11 / 22 / ~~` |
| 10-cell pair, A = `(1,1,1,2,3,2)` | `....0. / ...130 / ~11221` | `....0. / ...111 / ~~~~~~` |
| 10-cell pair, B = `(1,1,2,2,3,1)` | `....0. / ..121. / ~12120` | `....0. / ..111. / ~~~~~~` |

**With one drain cell the identity is irregular and depends on the drain.** `(2, 2, 2)` and `(3, 3)` are the same graph (a `3 × 2` grid, lying down or standing up) with the same group `Z/15`. Their identities differ only because the bottom-left cell sits in a different place in the grid. On a `6 × 6` square the one-drain identity is already a scattered mix of 0s to 3s, the beginning of the intricate patterns sandpile identities are known for on large grids:

```
021220
113202
123222
222331
222212
~22110
```

**With the tide the identity is strikingly regular.** Every rectangle at least 2 wide has identity **1 on each top-row cell and 2 on every cell below it**, checked for all rectangles from `2 × 2` to `7 × 7`.[^3] The `6 × 6` square:

```
111111
222222
222222
222222
222222
~~~~~~
```

The tide also makes the identity a property of the castle's shape, since the bottom row is a canonical drain, with no arbitrary choice of cell.

## One grain on the apex

Start at the identity and drop one grain on the apex (the top cell of the leftmost tallest column). How big is the avalanche? For the 10-cell isospectral pair of [[hear-the-shape-seminar](pages/hear-the-shape-seminar.md)], with one drain cell, the grain sets off **57 topplings** in `A` and **1** in `B`. The two castles have the same eigenvalues and the same sandpile group `Z/15`, but the sand behaves completely differently.[^2]

## Does the identity hear more than the spectrum?

A single drain cell or a single drop cell makes a measurement depend on that choice. The fair comparison uses **every** choice. The **avalanche profile** of a castle records the number of topplings caused by one grain on each cell, starting from the identity for each possible drain cell. It depends only on the castle's graph. Tested on every cospectral group of [[isospectral-castles](pages/isospectral-castles.md)] to 16 cells, alongside two tide measurements (which depend on the shape) and the sandpile group and clock spectrum from [[sandpile-census](pages/sandpile-census.md)] and [[sandcastle-clock](pages/sandcastle-clock.md)]:[^4]

| invariant | adjacency-cospectral groups separated (of 105) | Laplacian-cospectral groups separated (of 17) |
|---|---|---|
| sandpile group | 0 | 0 |
| clock spectrum | 62 | 5 |
| identity grain totals, every drain cell | 54 | 5 |
| tide identity (sorted grain counts) | 90 | 13 |
| **avalanche profile** | **105 (all)** | **17 (all)** |

The avalanche profile separates **every** cospectral group to 16 cells, including the 11-cell Laplacian pair of trees. There the sandpile group is trivial and the identity is just the fullest stable pile, yet the avalanches still differ. Going further, up to 13 cells no two castles that colour refinement proves non-isomorphic share an avalanche profile.[^5] At these sizes the avalanche profile behaves like a complete fingerprint of the castle graph, which neither the spectrum nor the sandpile group is.

## What this settles and what it opens

**Settled.**
- The identity is `stab(2m − stab(2m))`, and on a tree castle it is the fullest stable pile.
- With one drain cell it is irregular and drain-dependent. With the tide it is regular, and every rectangle at least 2 wide has 1 on its top row and 2 below (checked to `7 × 7`).
- The avalanche profile separates every cospectral group to 16 cells. This answers the clock page's open question "what the clock spectrum cannot hear" at these sizes, and no counterexample to completeness appears up to 13 cells.

**Open.**
- Prove the tide-identity pattern for all rectangles, and describe the tide identity of a general castle.
- Is the avalanche profile a complete invariant of castle graphs, or do two non-isomorphic castles share one at some larger size?
- The avalanche statistics under random dropping (Bak-Tang-Wiesenfeld): [[castle-avalanches](pages/castle-avalanches.md)].

## Snippet

```python
def sand_board(c, drains):                 # cells that hold sand, their non-drain neighbours, full degrees
    cells = [(i, j) for i, h in enumerate(c) for j in range(h)]
    S = set(cells)
    def nbs(v):
        i, j = v
        return [u for u in ((i+1, j), (i-1, j), (i, j+1), (i, j-1)) if u in S]
    live = [v for v in cells if v not in drains]
    return live, {v: [u for u in nbs(v) if u not in drains] for v in live}, {v: len(nbs(v)) for v in live}

def cell_drain(c):  return {(0, 0)}                                   # the bottom-left cell
def tide(c):        return {(i, 0) for i in range(len(c))}            # the whole bottom row

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

def identity(c, drains):                   # stab(2m - stab(2m)), m = the fullest stable pile
    board = sand_board(c, drains)
    live, nb, deg = board
    m = {v: deg[v] - 1 for v in live}
    s, _ = stabilize(board, {v: 2 * m[v] for v in live})
    return stabilize(board, {v: 2 * m[v] - s[v] for v in live})[0]

def draw(c, e):                            # top row first; drain cells drawn as '~'
    return [''.join('.' if j >= h else str(e[(i, j)]) if (i, j) in e else '~' for i, h in enumerate(c))
            for j in range(max(c) - 1, -1, -1)]

def acts_as_zero(c, drains):               # adding the identity to a recurrent pile changes nothing
    board = sand_board(c, drains); live, nb, deg = board
    r, _ = stabilize(board, {v: deg[v] for v in live})                 # a recurrent pile
    return stabilize(board, {v: r[v] + identity(c, drains)[v] for v in live})[0] == r

def avalanche(c, drains, v):               # topplings caused by one grain at v, starting from the identity
    board = sand_board(c, drains); e = identity(c, drains); e[v] += 1
    return stabilize(board, e)[1]

def avalanche_profile(c):                  # every drain cell, every drop cell: depends only on the graph
    cells = [(i, j) for i, h in enumerate(c) for j in range(h)]
    return sorted(avalanche(c, {d}, v) for d in cells for v in cells if v != d)
```

```
>>> draw((2, 2, 2), identity((2, 2, 2), cell_drain((2, 2, 2)))), draw((2, 2, 2), identity((2, 2, 2), tide((2, 2, 2))))
(['101', '~21'], ['111', '~~~'])
>>> draw((3, 3), identity((3, 3), cell_drain((3, 3)))), draw((3, 3), identity((3, 3), tide((3, 3))))
(['11', '20', '~1'], ['11', '22', '~~'])
>>> draw((4,), identity((4,), cell_drain((4,))))                        # a tree: the identity is the fullest stable pile
['0', '1', '1', '~']
>>> A, B = (1, 1, 1, 2, 3, 2), (1, 1, 2, 2, 3, 1)
>>> draw(A, identity(A, cell_drain(A))), draw(B, identity(B, cell_drain(B)))
(['....0.', '...130', '~11221'], ['....0.', '..121.', '~12120'])
>>> avalanche(A, cell_drain(A), (4, 2)), avalanche(B, cell_drain(B), (4, 2))
(57, 1)
>>> all(acts_as_zero(c, d(c)) for c in [(2, 2, 2), (3, 3), A, B, (6,) * 6] for d in (cell_drain, tide))
True
>>> draw((6,) * 6, identity((6,) * 6, tide((6,) * 6)))
['111111', '222222', '222222', '222222', '222222', '~~~~~~']
>>> S, T = (1, 1, 1, 2, 1, 1, 2, 1, 1), (1, 1, 3, 1, 1, 1, 2, 1)
>>> avalanche_profile(S) == avalanche_profile(T), avalanche_profile(A) == avalanche_profile(B)
(False, False)
```

## Related Concepts

- [[sandpile-group](pages/sandpile-group.md)] - the game, the group, and the tide variant.
- [[sandcastle-clock](pages/sandcastle-clock.md)] - the clock that starts at the identity; its open question about what the clock spectrum cannot hear is answered here to 16 cells.
- [[sandpile-census](pages/sandpile-census.md)] - the sandpile group of every castle, which separates no cospectral pair.
- [[isospectral-castles](pages/isospectral-castles.md)] / [[hear-the-shape-seminar](pages/hear-the-shape-seminar.md)] - the cospectral pairs.
- [[castle-graph](pages/castle-graph.md)] - tree castles, whose identity is their fullest stable pile.
- [[castle-avalanches](pages/castle-avalanches.md)] - random dropping from the identity: the mean avalanche depends only on height for rectangles and battlements.


## Appearances in Sources

- [[project-euler-502-castle-factoring](pages/project-euler-502-castle-factoring.md)] - the castle definition behind the castle graph.

## Footnotes

[^1]: https://en.wikipedia.org/wiki/Abelian_sandpile_model - the identity element of the sandpile group, its computation from the maximal stable configuration, and the fact that recurrent configurations (not the empty one) form the group.
[^2]: Verified by execution (Python 3.10, 2026-09-26): identities computed by `stab(2m − stab(2m))` for each castle and drain model; each passes `acts_as_zero` (adding it to the recurrent pile `stab(deg)` returns that pile). The drawings, the `6 × 6` one-drain identity, and the apex avalanches `57` and `1` (apex cell `(4, 2)` in both castles) are pinned in the Snippet except the `6 × 6` one-drain pattern, which comes from the same `identity` function.
[^3]: Verified by execution (Python 3.10, 2026-09-26): for every `w × h` rectangle with `2 ≤ w ≤ 7` and `2 ≤ h ≤ 7`, the tide identity equals 1 on row `h − 1` and 2 on rows `1 … h − 2`.
[^4]: Verified by execution (Python 3.10, 2026-09-26): for the 105 adjacency and 17 Laplacian cospectral groups of [[sandpile-census](pages/sandpile-census.md)], each castle's identity grain totals over every drain cell, tide identity (sorted grain counts) and avalanche profile (topplings from one grain on each non-drain cell, starting at each drain cell's identity); a group counts as separated when its castles do not all agree. The first groups separated by the tide identity are at 10 cells (adjacency) and 11 cells (Laplacian); the avalanche profile separates both 10-cell adjacency groups and the 11-cell Laplacian tree pair.
[^5]: Verified by execution (Python 3.10, 2026-09-26): for every castle with at most 13 cells (mirror images removed), castles grouped by avalanche profile; within each group every castle has the same colour-refinement hash (8 rounds), so no profile is shared by castles that colour refinement proves non-isomorphic. At 12 and 13 cells there are 321 and 625 distinct profiles among 1,056 and 2,080 castles; castles sharing a profile are different skylines of the same graph as far as colour refinement can tell. About 40 seconds to 13 cells.
