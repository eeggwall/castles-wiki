---
title: The sandcastle clock - dropping sand until the castle repeats
category: Concepts
summary: Start a castle's sandpile at its identity configuration and drop one grain on the apex every tick; the pile returns to the identity after a whole number of ticks, the clock period. The period is the order of "one grain at the apex" in the castle's sandpile group, the least common denominator of a column of the inverse reduced Laplacian, and simulation agrees with that on every test castle. Tree branches are transparent - a grain anywhere on a branch acts like a grain where the branch attaches - so tree castles never tick (period 1). The period depends on where the drain and the apex are, not just on the castle's graph (on the silver rectangle it can be 1, 3, 5 or 15, and a castle and its mirror image differ in 1,018 of 1,953 cases to 12 cells). Over all 33,150 castles to 16 cells the apex grain generates the whole group only 8,839 times out of 26,187. The graph invariant is the clock spectrum, the periods of every (drain, grain) pair, and it hears what the Laplacian spectrum and the sandpile group cannot. It separates 62 of the 105 adjacency-cospectral groups (the 10-cell pair ticks 15 against 5) and 5 of the 17 Laplacian-cospectral groups, the smallest at 13 cells.
tags: [concept, castle, sandpile, critical-group, clock, period, identity-element, isospectral, laplacian, tree-castle, census, sympy, verification, pedagogy]
sources: [project-euler-502-castle-factoring]
created: 2026-09-26
updated: 2026-09-26
---

# The sandcastle clock - dropping sand until the castle repeats

## The idea, without algebra

Play the sandpile game of [[sandpile-group](pages/sandpile-group.md)] on a castle, with the bottom-left cell as the drain. Start from the **identity**, the special recurrent configuration that changes nothing when added to another one. Then run a clock. Every tick, drop **one grain on the apex** (the top cell of the leftmost tallest column) and let the sand topple until it settles.

The pile keeps changing, but there are only finitely many recurrent configurations, so sooner or later it returns to the identity. The number of ticks that takes is the castle's **clock period**. On the 4-cycle `(2, 2)` it is 4. On the silver rectangle `(2, 2, 2)` it is 15. On any tree castle it is 1: the grain just washes out and nothing changes.

## Why it repeats, and when

Adding a grain and stabilizing is addition in the sandpile group `K`. So ticking the clock `t` times adds `t` copies of "one grain at the apex" to the identity. The pile is back at the identity exactly when those `t` grains are equivalent to no grains, that is, when they can be toppled away completely. So:

```
clock period  =  order of "one grain at the apex" in K
              =  the least common denominator of the column of L̃⁻¹ belonging to the apex
```

where `L̃` is the Laplacian with the drain's row and column deleted. The second line is how to compute it without simulating. `t` grains at `v` topple away exactly when `L̃⁻¹ (t·e_v)` has integer entries. Direct simulation and this formula agree on every castle tested.[^1] The period always divides the **exponent** of `K` (its largest cyclic factor), and it equals the group order `|K|` exactly when the apex grain generates the whole group.

## Tree branches are transparent

Put a grain on a leaf, a cell with one neighbour. It can topple straight to that neighbour. So in the sandpile group, **a grain on a leaf is the same as a grain on its neighbour**, and by repeating the argument a grain anywhere on a tree branch is the same as a grain where the branch joins the rest of the castle. On `(2, 2, 3)` the spike's top cell and the cell it sits on both have order 5. On `(2, 2, 1, 1, 1)` every cell of the tail behaves like the cell where the tail starts (order 4).[^2]

This is the clock's version of "the 2×2 blocks hold the sand". A castle's clock only notices where the drain and the apex attach to its skeleton of `2 × 2` blocks. Tree castles have no skeleton, so their clock never ticks.

## The period depends on where you put the drain and the apex

The clock is a property of a castle **plus two chosen cells**, not of the castle's graph alone. On `(2, 2, 2)`, a grain on the top-right cell has period 5, 3, 15, 15, 15 or 1 as the drain moves through the six cells.[^3] Even the convention "bottom-left drain, leftmost apex" is not symmetric. `(2, 3)` ticks with period 2 and its mirror image `(3, 2)` with period 4. Up to 12 cells, a castle and its mirror image have different periods in 1,018 of the 1,953 cases where they differ as castles.[^4]

**The clock spectrum.** To get something that depends only on the castle, record the period for **every** choice of drain and grain cell. That multiset is the castle's **clock spectrum**. Isomorphic castles have the same clock spectrum, so it can be compared across castles the way eigenvalues are.

## What the census shows

Over all 33,150 castles with at most 16 cells (mirror images removed), with the bottom-left drain and leftmost apex:[^5]

| | castles |
|---|---|
| tree castles (trivial group, period 1) | 6,963 |
| nontrivial group | 26,187 |
| … apex grain generates `K` (period `= |K|`) | 8,839 |
| … period equals the exponent of `K` | 10,915 |
| … period below the exponent | 15,272 |

The most common periods are 4, 1, 2, 15, 5, 3, 209, 56. Period 1 with a nontrivial group (3,769 castles) happens when the drain and the apex hang off the same part of the block skeleton, as the transparency rule predicts.

**The clock hears what the spectrum and the sandpile group cannot.** [[sandpile-census](pages/sandpile-census.md)] found that the sandpile group separates none of the cospectral groups of [[isospectral-castles](pages/isospectral-castles.md)]. The clock does:[^6]

| cospectral groups (to 16 cells) | number | separated by the clock (fixed drain and apex) | separated by the clock spectrum |
|---|---|---|---|
| same adjacency spectrum | 105 | 48 | **62** |
| same Laplacian spectrum | 17 | 3 | **5** |

- **The 10-cell pair.** The adjacency-cospectral pair `(1,1,1,2,3,2)` and `(1,1,2,2,3,1)` of [[hear-the-shape-seminar](pages/hear-the-shape-seminar.md)] has the same spectrum and the same group `Z/15`. Its clocks tick **15** and **5** times, and its clock spectra differ: over the 90 (drain, grain) pairs, periods `1, 3, 5, 15` occur `14, 10, 14, 52` times against `10, 16, 18, 46`.
- **The smallest Laplacian-cospectral pair the clock spectrum separates** has 13 cells: `(1,1,1,2,3,1,1,2,1)` and `(1,2,1,2,6,1)`. Both have period 2 under the fixed convention, but over all 156 pairs their periods `1, 2, 4` occur `44, 28, 84` times against `42, 54, 60`. With the fixed convention alone, the first separated Laplacian pair has 15 cells (periods 4 and 2).

So the answer to the `IDEAS.md` question "the smallest castle whose period is not determined by its spectrum" is 10 cells for the adjacency spectrum and 13 cells for the Laplacian spectrum, using the clock spectrum.

## What this settles and what it opens

**Settled.**
- The clock period is the order of the apex grain in `K`, computable as a least common denominator. Tree branches are transparent, and tree castles never tick.
- The period depends on the drain and the apex. The clock spectrum removes that dependence and is a graph invariant.
- The clock spectrum separates 62 of 105 adjacency-cospectral groups and 5 of 17 Laplacian ones to 16 cells, where the sandpile group separates none.

**Open.**
- Which cospectral castles does the clock spectrum still fail to separate (43 adjacency and 12 Laplacian groups to 16 cells)? A finer sandpile invariant that separates them all to 16 cells is the avalanche profile on [[sandpile-identity](pages/sandpile-identity.md)].
- A canonical "tide" clock: merge the bottom row into one drain ([[sandpile-group](pages/sandpile-group.md)], the tide variant) and drop on every top cell. Does it remove the mirror dependence?
- The identity element itself and the avalanches each tick causes, the remaining S-department items.

## Snippet

```python
import sympy as sp
from math import lcm
from collections import Counter

def castle_graph(c):                       # cells (column, row) and each cell's neighbours
    cells = [(i, j) for i, h in enumerate(c) for j in range(h)]
    idx = {v: k for k, v in enumerate(cells)}
    nbrs = [[] for _ in cells]
    for (i, j), u in idx.items():
        for nb in ((i+1, j), (i, j+1)):
            if nb in idx:
                nbrs[u].append(idx[nb]); nbrs[idx[nb]].append(u)
    return cells, idx, nbrs

def apex(c):                               # top cell of the leftmost tallest column
    return (c.index(max(c)), max(c) - 1)

def stabilize(nbrs, g, drain=0):           # topple until every cell holds fewer grains than neighbours
    g = list(g)
    while any(g[v] >= len(nbrs[v]) for v in range(len(g)) if v != drain):
        for v in range(len(g)):
            if v != drain and g[v] >= len(nbrs[v]):
                q = g[v] // len(nbrs[v]); g[v] -= q * len(nbrs[v])
                for u in nbrs[v]:
                    g[u] += q
        g[drain] = 0
    g[drain] = 0
    return g

def identity(nbrs, drain=0):               # the recurrent identity: stab(2m - stab(2m)), m = fullest stable pile
    m = [0 if v == drain else len(nbrs[v]) - 1 for v in range(len(nbrs))]
    s = stabilize(nbrs, [2 * x for x in m], drain)
    return stabilize(nbrs, [2 * a - b for a, b in zip(m, s)], drain)

def clock_by_simulation(c, drain=0):       # ticks until the identity returns, one grain on the apex per tick
    cells, idx, nbrs = castle_graph(c)
    a, e = idx[apex(c)], identity(nbrs, drain)
    g, t = list(e), 0
    while True:
        g[a] += 1; g = stabilize(nbrs, g, drain); t += 1
        if g == e:
            return t

def grain_orders(c, drain=0):              # order in K of one grain at each cell: lcm of denominators of L~^-1 e_v
    cells, idx, nbrs = castle_graph(c)
    keep = [v for v in range(len(cells)) if v != drain]
    pos = {v: k for k, v in enumerate(keep)}
    L = sp.zeros(len(keep))
    for v in keep:
        L[pos[v], pos[v]] = len(nbrs[v])
        for u in nbrs[v]:
            if u != drain:
                L[pos[v], pos[u]] -= 1
    Linv = L.inv()
    return {cells[v]: lcm(*[sp.fraction(x)[1] for x in Linv[:, pos[v]]]) for v in keep}

def clock(c, drain=0):                     # the clock period, algebraically
    return grain_orders(c, drain)[apex(c)] if apex(c) != castle_graph(c)[0][drain] else 1

def clock_spectrum(c):                     # periods over every (drain, grain cell) pair: depends only on the graph
    cells = castle_graph(c)[0]
    return sorted(Counter(t for d in range(len(cells)) for t in grain_orders(c, d).values()).items())
```

```
>>> [(c, clock_by_simulation(c), clock(c)) for c in [(2, 2), (2, 2, 2), (3, 3, 3), (1, 2, 1)]]
[((2, 2), 4, 4), ((2, 2, 2), 15, 15), ((3, 3, 3), 8, 8), ((1, 2, 1), 1, 1)]
>>> A, B = (1, 1, 1, 2, 3, 2), (1, 1, 2, 2, 3, 1)
>>> clock(A), clock(B)
(15, 5)
>>> clock_spectrum(A), clock_spectrum(B)
([(1, 14), (3, 10), (5, 14), (15, 52)], [(1, 10), (3, 16), (5, 18), (15, 46)])
>>> [grain_orders((2, 2, 2), d).get((2, 1), 1) for d in range(6)]
[5, 3, 15, 15, 15, 1]
>>> grain_orders((2, 2, 3))[(2, 2)], grain_orders((2, 2, 3))[(2, 1)]
(5, 5)
>>> clock((2, 3)), clock((3, 2))
(2, 4)
```

## Related Concepts

- [[sandpile-group](pages/sandpile-group.md)] - the game, the group, and the identity element this clock starts from.
- [[sandpile-census](pages/sandpile-census.md)] - the group of every castle to 16 cells, which separates no cospectral pair.
- [[isospectral-castles](pages/isospectral-castles.md)] / [[hear-the-shape-seminar](pages/hear-the-shape-seminar.md)] - the cospectral pairs the clock spectrum separates.
- [[castle-graph](pages/castle-graph.md)] - tree castles, whose clock never ticks.
- [[sandpile-identity](pages/sandpile-identity.md)] - the identity the clock starts from, and the avalanche profile, which separates every cospectral group to 16 cells.
- [[castle-avalanches](pages/castle-avalanches.md)] - dropping at random instead of on one cell.
- [[sandcastle-seminar](pages/sandcastle-seminar.md)] - the Sandcastles seminar, following the 16-cell silver castle `(3,2,1,2,2,1,2,3)` through the whole sandpile story.


## Appearances in Sources

- [[project-euler-502-castle-factoring](pages/project-euler-502-castle-factoring.md)] - the castle definition behind the castle graph.

## Footnotes

[^1]: Verified by execution (Python 3.10, SymPy, 2026-09-26): `clock_by_simulation` (start at `stab(2m − stab(2m))`, add one grain at the apex, stabilize, count ticks to return) equals the least common denominator of `L̃⁻¹ e_apex` for `(2,2)`, `(2,2,2)`, `(1,2,1)`, `(3,3,3)`, `(2,2,2,2)`, `(1,1,1,2,3,2)`, `(1,1,2,2,3,1)`, `(2,2,1,2,2)` and `(2,3,3,2)` (periods 4, 15, 1, 8, 56, 15, 5, 4, 52); four of these are pinned in the Snippet. The identity formula and the equivalence "adding a grain = adding in `K`" are standard (https://en.wikipedia.org/wiki/Abelian_sandpile_model).
[^2]: Verified by execution (Python 3.10, SymPy, 2026-09-26): with the bottom-left drain, grain orders on `(2,2,3)` are 15 at `(0,1)`, `(1,0)` and `(1,1)`, 3 at `(2,0)`, and 5 at both `(2,1)` and the spike top `(2,2)`; on `(2,2,1,1,1)` the tail cells `(2,0)`, `(3,0)`, `(4,0)` all have order 4, the same as `(1,0)` where the tail attaches.
[^3]: Verified by execution (Python 3.10, SymPy, 2026-09-26): `grain_orders((2,2,2), d)` for each of the six drains, as pinned for the top-right cell; the full 6 × 6 table has entries 1, 3, 5 and 15.
[^4]: Verified by execution (Python 3.10, 2026-09-26): for every castle with at most 12 cells that is not its own mirror image (1,953 pairs), the fixed-convention period of the castle and of its mirror image differ in 1,018 cases, the first being `(2,3)` (2) against `(3,2)` (4).
[^5]: Verified by execution (Python 3.10, 2026-09-26): periods by exact rational inversion of `L̃` for all 33,150 castles of [[sandpile-census](pages/sandpile-census.md)] (about 5 minutes), compared with the group order and exponent from that census.
[^6]: Verified by execution (Python 3.10, 2026-09-26): for each castle in the 105 adjacency and 17 Laplacian cospectral groups to 16 cells, the fixed-convention period and the clock spectrum (orders of one grain at `v` with drain `d`, over all ordered pairs `d ≠ v`); groups counted as separated when their castles do not all agree. The 13-cell pair's spectra are `{1: 44, 2: 28, 4: 84}` and `{1: 42, 2: 54, 4: 60}`; the first fixed-convention separation among Laplacian groups is at 15 cells, `(1,1,1,1,2,2,1,2,3,1)` (4) against `(1,1,1,2,3,1,1,2,2,1)` (2).
