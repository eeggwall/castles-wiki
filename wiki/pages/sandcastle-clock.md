---
title: The sandcastle clock - dropping sand until the castle repeats, in the sink and tide models
category: Concepts
summary: Start a castle's sandpile at its identity configuration and drop one grain on the apex every tick; the pile returns to the identity after a whole number of ticks, the clock period. The period is the order of "one grain at the apex" in the castle's sandpile group, the least common denominator of a column of the inverse reduced Laplacian, and simulation agrees with that on every test castle. The clock runs in both models of sandpile-group. In the sink model (one sink cell, bottom-left) tree branches are transparent, so tree castles never tick, and the period depends on where the sink and the apex are (on the silver rectangle it can be 1, 3, 5 or 15, and a castle and its mirror image differ in 1,018 of 1,953 cases to 12 cells); the graph invariant is the clock spectrum over every (sink, grain) pair, which separates 62 of the 105 adjacency-cospectral groups (the 10-cell pair ticks 15 against 5) and 5 of the 17 Laplacian-cospectral groups. In the tide model (the whole bottom row as the sink) there is no sink to choose, the clock depends only on the castle's runs of raised columns, and a spike standing on the ground is a branch of the sink, so 6,611 castles with a nontrivial tide group still never tick. The tide removes the mirror dependence up to one tie-break: a castle and its mirror image have different tide periods in 204 of 1,953 cases to 12 cells, every one of them a castle with two or more tallest columns. Cospectral separation is the natural test for the sink clock, a graph invariant; the tide clock sees the skyline, and every cospectral group contains castles of different widths, so any tide count over the cells above the ground separates them all for that trivial reason. The fixed-apex tide clock, which counts no cells, separates 49 of the 105 adjacency-cospectral groups and none of the 17 Laplacian ones.
tags: [concept, castle, sandpile, critical-group, clock, period, identity-element, isospectral, laplacian, tree-castle, census, sink-model, tide-model, mirror-symmetry, sympy, verification, pedagogy]
sources: [project-euler-502-castle-factoring, rossin-2000-group-of-a-sandpile, dhar-ruelle-sen-verma-1995-algebraic-aspects]
created: 2026-09-26
updated: 2026-09-27
---

# The sandcastle clock - dropping sand until the castle repeats, in the sink and tide models

## The idea, without algebra

Play the sandpile game of [[sandpile-group](pages/sandpile-group.md)] on a castle. Start from the **identity**, the special recurrent configuration that changes nothing when added to another one. Then run a clock. Every tick, drop **one grain on the apex** (the top cell of the leftmost tallest column) and let the sand topple until it settles.

The pile keeps changing, but there are only finitely many recurrent configurations, so sooner or later it returns to the identity. The number of ticks that takes is the castle's **clock period**. The game needs a sink, and the two models of [[sandpile-group](pages/sandpile-group.md)] give two clocks:

| castle | sink model (bottom-left sink cell) | tide model (the ground is the sink) |
|---|---|---|
| 4-cycle `(2, 2)` | 4 | 3 |
| silver rectangle `(2, 2, 2)` | 15 | 8 |
| tall pair `(3, 3)` | 15 | 11 |
| any tree castle | 1 | 1 |

On a tree castle the grain just washes out and nothing changes, in either model.

## Why it repeats, and when

Adding a grain and stabilizing is addition in the sandpile group `K`. So ticking the clock `t` times adds `t` copies of "one grain at the apex" to the identity. The pile is back at the identity exactly when those `t` grains are equivalent to no grains, that is, when they can be toppled away completely. So, in either model:

```
clock period  =  order of "one grain at the apex" in K
              =  the least common denominator of the column of L̃⁻¹ belonging to the apex
```

where `L̃` is the Laplacian with the sink's rows and columns deleted: one row and column in the sink model, the whole bottom row in the tide model. `K` is `K_sink` or `K_tide` accordingly. The second line is how to compute it without simulating. `t` grains at `v` topple away exactly when `L̃⁻¹ (t·e_v)` has integer entries. Direct simulation and this formula agree on every castle tested, in both models.[^1] [^7] The period always divides the **exponent** of `K` (its largest cyclic factor), and it equals the group order `|K|` exactly when the apex grain generates the whole group. The same principle appears in the physics literature: a deterministic sandpile that always adds at one site cycles with the order of that site's addition operator, computed from its column of `Δ⁻¹`.[^11]

## Tree branches are transparent

Put a grain on a leaf, a cell with one neighbour. It can topple straight to that neighbour. So in the sandpile group, **a grain on a leaf is the same as a grain on its neighbour**, and by repeating the argument a grain anywhere on a tree branch is the same as a grain where the branch joins the rest of the castle. With the bottom-left sink cell, on `(2, 2, 3)` the spike's top cell and the cell it sits on both have order 5. On `(2, 2, 1, 1, 1)` every cell of the tail behaves like the cell where the tail starts (order 4).[^2]

This is the clock's version of "the 2×2 blocks hold the sand". A castle's clock only notices where the sink and the apex attach to its skeleton of `2 × 2` blocks. Tree castles have no skeleton, so their clock never ticks.

**Under the tide the ground is part of the tree.** A spike standing on the ground, a column whose neighbours are all height 1, is a branch that hangs from the sink itself. A grain anywhere on it is the same as a grain in the ground, so it washes out. So when the apex sits on such a spike the tide clock never ticks, however much sand the rest of the castle holds: `(3, 1, 2, 2)` has `K_tide = Z/3` and tide period 1.

## The sink clock depends on where the sink and the apex are

The sink clock is a property of a castle **plus two chosen cells**, not of the castle's graph alone. On `(2, 2, 2)`, a grain on the top-right cell has period 5, 3, 15, 15, 15 or 1 as the sink moves through the six cells.[^3] Even the convention "bottom-left sink cell, leftmost apex" is not symmetric. `(2, 3)` ticks with period 2 and its mirror image `(3, 2)` with period 4. Up to 12 cells, a castle and its mirror image have different periods in 1,018 of the 1,953 cases where they differ as castles.[^4]

**The sink clock spectrum.** To get something that depends only on the castle's graph, record the period for **every** choice of sink cell and grain cell. That multiset is the castle's **sink clock spectrum**. Isomorphic castles have the same sink clock spectrum, so it can be compared across castles the way eigenvalues are.

## The tide clock has no sink to choose

In the tide model the sink is the ground, so the only choice left is the apex. Three consequences:

- **The tide clock depends only on the runs.** Under the tide a castle falls apart into its runs of raised columns ([[sandpile-group](pages/sandpile-group.md)], Part 3), and `K_tide` is the product of the runs' groups. So the tide period is the order of the apex grain in the group of the apex's own run, and where the runs sit along the base does not matter.
- **The mirror dependence is down to one tie-break.** The ground is symmetric, so mirroring a castle mirrors its tide model exactly. Up to 12 cells, a castle and its mirror image have different tide periods in **204** of the 1,953 cases, against 1,018 in the sink model, and **every one of the 204** has two or more tallest columns. With a unique tallest column the apex is the same cell in both, and the tide clock is mirror-proof. The first examples are `(2, 1, 2, 2)`, whose leftmost apex tops a lone spike (period 1) while its mirror `(2, 2, 1, 2)` starts in the block run (period 3), and `(1, 2, 1, 2, 2)` (1 against 3).[^9]
- **The tide clock spectrum.** Recording the period of one grain at every cell above the ground gives the **tide clock spectrum**, with no sink and no apex to choose. It is mirror-invariant by the same symmetry. It is a property of the castle's shape, not of its graph: `(2, 2, 2)` and `(3, 3)` have the same graph but tide spectra `{4: 1, 8: 2}` and `{11: 4}`.

## What the census shows

Over all 33,150 castles with at most 16 cells (mirror images removed), with the leftmost apex and, in the sink model, the bottom-left sink cell:[^5] [^8]

| | sink model | tide model |
|---|---|---|
| tree castles (trivial group, period 1) | 6,963 | 6,963 |
| nontrivial group | 26,187 | 26,187 |
| … apex grain generates `K` (period `= |K|`) | 8,839 | 13,159 |
| … period equals the exponent of `K` | 10,915 | 15,286 |
| … period below the exponent | 15,272 | 10,901 |
| … period 1 anyway (nontrivial group) | 3,769 | 6,611 |
| most common periods | 4, 1, 2, 15, 5, 3, 209, 56 | 1, 3, 11, 8, 21, 29, 4, 41 |

In the sink model, period 1 with a nontrivial group happens when the sink cell and the apex hang off the same part of the block skeleton, as the transparency rule predicts. Under the tide it happens almost twice as often, because every spike standing on the ground is part of the sink's tree. The tide grain also generates its whole group more often (13,159 against 8,839), which fits tide groups being cyclic more often ([[sandpile-census](pages/sandpile-census.md)]); whether that is the whole reason has not been checked.

## Hearing cospectral castles

**The sink clock hears what the spectrum and the sink group cannot.** [[sandpile-census](pages/sandpile-census.md)] found that `K_sink` separates none of the cospectral groups of [[isospectral-castles](pages/isospectral-castles.md)]. The sink clock does:[^6]

| cospectral groups (to 16 cells) | number | separated by the sink clock (fixed sink cell and apex) | separated by the sink clock spectrum |
|---|---|---|---|
| same adjacency spectrum | 105 | 48 | **62** |
| same Laplacian spectrum | 17 | 3 | **5** |

- **The 10-cell pair.** The adjacency-cospectral pair `(1,1,1,2,3,2)` and `(1,1,2,2,3,1)` of [[hear-the-shape-seminar](pages/hear-the-shape-seminar.md)] has the same spectrum and the same group `K_sink = Z/15`. Its sink clocks tick **15** and **5** times, and its sink clock spectra differ: over the 90 (sink, grain) pairs, periods `1, 3, 5, 15` occur `14, 10, 14, 52` times against `10, 16, 18, 46`.
- **The smallest Laplacian-cospectral pair the sink clock spectrum separates** has 13 cells: `(1,1,1,2,3,1,1,2,1)` and `(1,2,1,2,6,1)`. Both have period 2 under the fixed convention, but over all 156 pairs their periods `1, 2, 4` occur `44, 28, 84` times against `42, 54, 60`. With the fixed convention alone, the first separated Laplacian pair has 15 cells (periods 4 and 2).

So, reading the period through the sink clock spectrum, the smallest castles whose period is not determined by their spectrum have 10 cells for the adjacency spectrum and 13 cells for the Laplacian spectrum.

**The tide clock is a shape invariant, so this is not its natural test.** Cospectral separation measures what a graph invariant hears beyond the spectrum. The tide clock sees the skyline itself, and every one of the 105 adjacency and 17 Laplacian cospectral groups contains castles of different widths, that is, with different numbers of ground cells. So the tide clock spectrum, which records one period per cell above the ground, separates all of them for that trivial reason, and that says nothing about sand. The fixed-apex tide period counts no cells, and it separates **49** of the 105 adjacency groups and **none** of the 17 Laplacian ones (11 of those are trees, which never tick in either model).[^10] The 10-cell pair is one it hears: both castles have `K_tide = Z/8`, but their tide clocks tick **4** and **8**, and their tide clock spectra are `{4: 2, 8: 2}` against `{4: 1, 8: 3}`.

The natural question for a tide invariant is the reverse one: which different castles does it confuse? Every tide statistic depends only on the multiset of runs of raised columns, so castles with the same runs, placed anywhere along the base, always share their tide clock.

## What this settles and what it opens

**Settled.**
- In both models the clock period is the order of the apex grain in `K`, computable as a least common denominator, and simulation agrees. Tree branches are transparent, and tree castles never tick.
- **Sink model.** The period depends on the sink cell and the apex. The sink clock spectrum removes that dependence and is a graph invariant. It separates 62 of 105 adjacency-cospectral groups and 5 of 17 Laplacian ones to 16 cells, where `K_sink` separates none.
- **Tide model.** There is no sink to choose, the period depends only on the apex's run of raised columns, and spikes standing on the ground belong to the sink's tree (6,611 castles with nontrivial `K_tide` and period 1). The tide clock removes the mirror dependence except for the choice among tied tallest columns: all 204 mirror disagreements to 12 cells come from ties, and the tide clock spectrum is mirror-invariant.

**Open.**
- **Sink model.** Which cospectral castles does the sink clock spectrum still fail to separate (43 adjacency and 12 Laplacian groups to 16 cells)? A finer sandpile invariant that separates them all to 16 cells is the sink avalanche profile on [[sandpile-identity](pages/sandpile-identity.md)].
- **Tide model.** Which different multisets of runs share a tide clock spectrum, and how far does the tide clock spectrum go toward recovering the runs? And a canonical tie-break: a tide clock built from every tallest column at once (the multiset of their periods, or one grain on each) would be mirror-proof by construction; what does it hear?

## Snippet

```python
import sympy as sp
from math import lcm
from collections import Counter

def cells_of(c):
    return [(i, j) for i, h in enumerate(c) for j in range(h)]

def sink_cells(c, model):                  # 'sink': the bottom-left cell; 'tide': the whole bottom row
    return {(0, 0)} if model == 'sink' else {(i, 0) for i in range(len(c))}

def board(c, sink):                        # sand-holding cells, their non-sink neighbours, full degrees
    S = set(cells_of(c))
    around = lambda v: [u for u in ((v[0]+1, v[1]), (v[0]-1, v[1]), (v[0], v[1]+1), (v[0], v[1]-1)) if u in S]
    live = [v for v in cells_of(c) if v not in sink]
    return live, {v: [u for u in around(v) if u not in sink] for v in live}, {v: len(around(v)) for v in live}

def apex(c):                               # top cell of the leftmost tallest column
    return (c.index(max(c)), max(c) - 1)

def stabilize(b, g):                       # topple until every cell holds fewer grains than neighbours
    live, nb, deg = b
    g = dict(g)
    while any(g[v] >= deg[v] for v in live):
        for v in live:
            if g[v] >= deg[v]:
                q = g[v] // deg[v]; g[v] -= q * deg[v]
                for u in nb[v]:
                    g[u] += q
    return g

def identity(b):                           # the recurrent identity: stab(2m - stab(2m)), m = fullest stable pile
    live, nb, deg = b
    m = {v: deg[v] - 1 for v in live}
    s = stabilize(b, {v: 2 * m[v] for v in live})
    return stabilize(b, {v: 2 * m[v] - s[v] for v in live})

def clock_by_simulation(c, model='sink'):  # ticks until the identity returns, one grain on the apex per tick
    b = board(c, sink_cells(c, model)); a = apex(c)
    if a not in b[0]:
        return 1
    e = identity(b); g, t = dict(e), 0
    while True:
        g[a] += 1; g = stabilize(b, g); t += 1
        if g == e:
            return t

def grain_orders(c, sink):                 # order in K of one grain at each non-sink cell: lcm of denominators of L~^-1 e_v
    live, nb, deg = board(c, sink)
    if not live:
        return {}
    pos = {v: k for k, v in enumerate(live)}
    L = sp.Matrix(len(live), len(live), lambda r, s: deg[live[r]] if r == s else -(live[s] in nb[live[r]]))
    Linv = L.inv()
    return {v: lcm(*[sp.fraction(x)[1] for x in Linv[:, pos[v]]]) for v in live}

def clock(c, model='sink'):                # the clock period, algebraically
    return grain_orders(c, sink_cells(c, model)).get(apex(c), 1)

def clock_spectrum(c, model='sink'):       # sink: every (sink cell, grain cell) pair, a graph invariant; tide: every cell above the ground
    if model == 'tide':
        orders = list(grain_orders(c, sink_cells(c, 'tide')).values())
    else:
        orders = [t for d in cells_of(c) for t in grain_orders(c, {d}).values()]
    return sorted(Counter(orders).items())
```

```
>>> [(c, clock_by_simulation(c), clock(c)) for c in [(2, 2), (2, 2, 2), (3, 3, 3), (1, 2, 1)]]
[((2, 2), 4, 4), ((2, 2, 2), 15, 15), ((3, 3, 3), 8, 8), ((1, 2, 1), 1, 1)]
>>> [(c, clock_by_simulation(c, 'tide'), clock(c, 'tide')) for c in [(2, 2), (2, 2, 2), (3, 3), (3, 3, 3), (1, 2, 1)]]
[((2, 2), 3, 3), ((2, 2, 2), 8, 8), ((3, 3), 11, 11), ((3, 3, 3), 95, 95), ((1, 2, 1), 1, 1)]
>>> A, B = (1, 1, 1, 2, 3, 2), (1, 1, 2, 2, 3, 1)
>>> clock(A), clock(B), clock(A, 'tide'), clock(B, 'tide')
(15, 5, 4, 8)
>>> clock_spectrum(A), clock_spectrum(B)
([(1, 14), (3, 10), (5, 14), (15, 52)], [(1, 10), (3, 16), (5, 18), (15, 46)])
>>> clock_spectrum(A, 'tide'), clock_spectrum(B, 'tide')
([(4, 2), (8, 2)], [(4, 1), (8, 3)])
>>> [grain_orders((2, 2, 2), {v}).get((2, 1), 1) for v in cells_of((2, 2, 2))]
[5, 3, 15, 15, 15, 1]
>>> grain_orders((2, 2, 3), {(0, 0)})[(2, 2)], grain_orders((2, 2, 3), {(0, 0)})[(2, 1)]
(5, 5)
>>> clock((2, 3)), clock((3, 2)), clock((2, 3), 'tide'), clock((3, 2), 'tide')
(2, 4, 3, 3)
>>> clock((2, 1, 2, 2), 'tide'), clock((2, 2, 1, 2), 'tide'), clock((3, 1, 2, 2), 'tide')
(1, 3, 1)
>>> clock_spectrum((2, 2, 2), 'tide'), clock_spectrum((3, 3), 'tide'), clock_spectrum((3, 2, 1, 2, 2, 1, 2, 3), 'tide')
([(4, 1), (8, 2)], [(11, 4)], [(3, 8)])
```

## Related Concepts

- [[sandpile-group](pages/sandpile-group.md)] - the game, the two models, the groups, and the runs of raised columns the tide clock depends on.
- [[sandpile-census](pages/sandpile-census.md)] - the groups of every castle to 16 cells in both models; `K_sink` separates no cospectral pair.
- [[isospectral-castles](pages/isospectral-castles.md)] / [[hear-the-shape-seminar](pages/hear-the-shape-seminar.md)] - the cospectral pairs the clock spectra are tested on.
- [[castle-graph](pages/castle-graph.md)] - tree castles, whose clock never ticks.
- [[sandpile-identity](pages/sandpile-identity.md)] - the identity the clock starts from, in both models, and the avalanche profiles.
- [[castle-avalanches](pages/castle-avalanches.md)] - dropping at random instead of on one cell.
- [[sandcastle-seminar](pages/sandcastle-seminar.md)] - the Sandcastles seminar, following the 16-cell silver castle `(3,2,1,2,2,1,2,3)` through both models.
- [[castle-eigenvalues-by-example](pages/castle-eigenvalues-by-example.md)] - the 10-cell isospectral pair worked by hand, whose sink clocks tick 15 and 5.
- [[castle-ring-invariant-factors](pages/castle-ring-invariant-factors.md)] - the same order-versus-exponent reading of a group from its Smith normal form: the mod-`p` period is `ord(x)`, which need not be the exponent.

## Appearances in Sources

- [[dhar-ruelle-sen-verma-1995-algebraic-aspects](pages/dhar-ruelle-sen-verma-1995-algebraic-aspects.md)] - the period of a deterministic sandpile as the order of one addition operator, and the toppling invariants built from `Δ⁻¹`.
- [[rossin-2000-group-of-a-sandpile](pages/rossin-2000-group-of-a-sandpile.md)] - the group operation (add, then stabilize) that makes the clock period an order in the group.
- [[project-euler-502-castle-factoring](pages/project-euler-502-castle-factoring.md)] - the castle definition behind the castle graph.

## Footnotes

[^1]: Verified by execution (Python 3.10, SymPy, 2026-09-26): in the sink model, `clock_by_simulation` (start at `stab(2m − stab(2m))`, add one grain at the apex, stabilize, count ticks to return) equals the least common denominator of `L̃⁻¹ e_apex` for `(2,2)`, `(2,2,2)`, `(1,2,1)`, `(3,3,3)`, `(2,2,2,2)`, `(1,1,1,2,3,2)`, `(1,1,2,2,3,1)`, `(2,2,1,2,2)` and `(2,3,3,2)` (periods 4, 15, 1, 8, 56, 15, 5, 4, 52); four of these are pinned in the Snippet. The identity formula and the equivalence "adding a grain = adding in `K`" are standard (https://en.wikipedia.org/wiki/Abelian_sandpile_model; also [[rossin-2000-group-of-a-sandpile](pages/rossin-2000-group-of-a-sandpile.md)] §2 L37-39, the group operation `u ⊕ v` as stabilized sum and the identity recipe).
[^2]: Verified by execution (Python 3.10, SymPy, 2026-09-26): with the bottom-left sink cell, grain orders on `(2,2,3)` are 15 at `(0,1)`, `(1,0)` and `(1,1)`, 3 at `(2,0)`, and 5 at both `(2,1)` and the spike top `(2,2)`; on `(2,2,1,1,1)` the tail cells `(2,0)`, `(3,0)`, `(4,0)` all have order 4, the same as `(1,0)` where the tail attaches.
[^3]: Verified by execution (Python 3.10, SymPy, 2026-09-26): `grain_orders((2,2,2), {d})` for each of the six sink cells, as pinned for the top-right cell; the full 6 × 6 table has entries 1, 3, 5 and 15.
[^4]: Verified by execution (Python 3.10, 2026-09-26): for every castle with at most 12 cells that is not its own mirror image (1,953 pairs), the fixed-convention sink period of the castle and of its mirror image differ in 1,018 cases, the first being `(2,3)` (2) against `(3,2)` (4).
[^5]: Verified by execution (Python 3.10, 2026-09-26): sink periods by exact rational inversion of `L̃` for all 33,150 castles of [[sandpile-census](pages/sandpile-census.md)] (about 5 minutes), compared with the group order and exponent from that census.
[^6]: Verified by execution (Python 3.10, 2026-09-26): for each castle in the 105 adjacency and 17 Laplacian cospectral groups to 16 cells, the fixed-convention sink period and the sink clock spectrum (orders of one grain at `v` with sink cell `d`, over all ordered pairs `d ≠ v`); groups counted as separated when their castles do not all agree. The 13-cell pair's spectra are `{1: 44, 2: 28, 4: 84}` and `{1: 42, 2: 54, 4: 60}`; the first fixed-convention separation among Laplacian groups is at 15 cells, `(1,1,1,1,2,2,1,2,3,1)` (4) against `(1,1,1,2,3,1,1,2,2,1)` (2).
[^7]: Verified by execution (Python 3.10, SymPy, 2026-09-26): in the tide model, `clock_by_simulation(c, 'tide')` equals the least common denominator of the apex column of the tide `L̃⁻¹` for `(2,2)`, `(2,2,2)`, `(3,3)`, `(3,3,3)`, `(2,2,2,2)`, `(1,1,1,2,3,2)`, `(1,1,2,2,3,1)`, `(2,2,1,2,2)`, `(2,3,3,2)`, `(1,2,1)`, `(3,2,1,2,2,1,2,3)`, `(2,3)` and `(3,2)` (periods 3, 8, 11, 95, 21, 4, 8, 3, 75, 1, 3, 3, 3); five are pinned in the Snippet.
[^8]: Verified by execution (Python 3.10, 2026-09-26): tide periods by exact rational solution of `L̃ x = e_apex` (bottom row deleted, full degrees kept) for all 33,150 castles, compared with the order and exponent of `K_tide` from the tide block matrix of [[sandpile-group](pages/sandpile-group.md)]; period 1 with nontrivial `K_tide` in 6,611 castles, among them `(3,1,2,2)` (`K_tide = Z/3`), as pinned.
[^9]: Verified by execution (Python 3.10, 2026-09-26): for the 1,953 castles with at most 12 cells that are not their own mirror image, the tide period with the leftmost apex differs from the mirror image's in 204 cases, none of them with a unique tallest column; the first by cell count are `(2,1,2,2)` (1) against `(2,2,1,2)` (3) and `(1,2,1,2,2)` (1) against its mirror (3), the first pinned. The tide clock spectrum of a castle equals its mirror image's on the first 400 of those pairs, as the symmetry of the ground requires.
[^10]: Verified by execution (Python 3.10, 2026-09-26): for the 105 adjacency and 17 Laplacian cospectral groups of [[sandpile-census](pages/sandpile-census.md)], taken with every skyline of every graph in the group, a group counts as separated when two castles with non-isomorphic graphs get different tide periods (leftmost apex); 49 adjacency and 0 Laplacian groups are separated. Every one of the 122 groups contains castles of two or more widths. The 10-cell pair's tide values are pinned in the Snippet.
[^11]: [[dhar-ruelle-sen-verma-1995-algebraic-aspects](pages/dhar-ruelle-sen-verma-1995-algebraic-aspects.md)] §7 Question 1 pp. 25-27, eqs. (7.1)-(7.3) - "the period of the cycle T_L is independent of the initial configuration"; "T_L is the order of the operator a(L+1, L+1) on the space R of recurrent configurations"; `T_L = (Det Δ)/M` with `M` the gcd of the centre column of `E = (Det Δ)Δ⁻¹`, and `T_L` dividing the largest elementary divisor. The paper's toppling invariants `Q_i = Σ_j (Δ⁻¹)_ij z_j mod 1` (§3 p. 6, eq. 3.3) are the reason a grain count `t e_v` topples away exactly when `L̃⁻¹ (t e_v)` is integral.
