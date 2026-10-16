---
title: The sandcastle clock - dropping sand until the castle repeats, in the sink and tide models
category: Concepts
summary: Start a castle's sandpile at its identity configuration and drop one grain on the apex, the top cell of the leftmost tallest column, every tick; the pile returns to the identity after a number of ticks, the clock period, which is the order of one grain at the apex in the sandpile group, the least common denominator of a column of the inverse reduced Laplacian. In the sink model (one sink cell, here the bottom-left cell) a grain anywhere on a tree branch equals a grain where the branch attaches, so tree castles never tick, and the period depends on the sink and the apex (a castle and its mirror image differ in 1,018 of 1,953 cases to 12 cells). The sink clock spectrum, the periods over every (sink, grain) pair, depends only on the castle graph and separates 62 of the 105 adjacency- and 5 of the 17 Laplacian-cospectral groups to 16 cells. In the tide model (the whole bottom row as the sink) the clock depends only on the runs of raised columns; all 6,611 castles to 16 cells with a nontrivial tide group and tide period 1 have their apex on a column standing alone on the bottom row; a castle and its mirror image differ in 204 of 1,953 cases to 12 cells, each with two or more tallest columns.
tags: [concept, castle, sandpile, critical-group, clock, period, identity-element, isospectral, laplacian, tree-castle, census, sink-model, tide-model, mirror-symmetry, sympy, verification, pedagogy]
sources: [project-euler-502-castle-factoring, rossin-2000-group-of-a-sandpile, dhar-ruelle-sen-verma-1995-algebraic-aspects, dhar-1990-self-organized-critical-sandpile]
created: 2026-09-26
updated: 2026-10-16
---

# The sandcastle clock - dropping sand until the castle repeats, in the sink and tide models

## The clock

Play the sandpile of [[sandpile-group](pages/sandpile-group.md)] on a castle. Start from the **identity** ([[sandpile-identity](pages/sandpile-identity.md)]), and at every tick drop **one grain on the apex**, the top cell of the leftmost tallest column, and stabilize.

The recurrent configurations are finitely many, so the pile returns to the identity. The number of ticks it takes is the castle's **clock period**. The two models of [[sandpile-group](pages/sandpile-group.md)] give two clocks:[^1]

| castle | sink model (bottom-left sink cell) | tide model (bottom row as the sink) |
|---|---|---|
| 4-cycle `(2, 2)` | 4 | 3 |
| rectangle `(2, 2, 2)`, silver by spectrum (castle-graph spectral radius `1 + √2`) | 15 | 8 |
| `(3, 3)`, the same graph standing up | 3 | 11 |
| any tree castle | 1 | 1 |

On a tree castle, a castle with no `2 × 2` block of cells, the sandpile group is trivial in both models, so the pile never leaves the identity.

## The period is an order in the group

Adding a grain and stabilizing is addition in the sandpile group `K` ([[sandpile-group](pages/sandpile-group.md)]). So `t` ticks add `t` copies of the class of one grain at the apex, and the pile is back at the identity exactly when `t` grains at the apex topple away completely, that is, when `L̃⁻¹ (t·e_apex)` is an integer vector. Here `L̃` is the reduced Laplacian: one row and column deleted in the sink model, the whole bottom row in the tide model. So, in either model,

```
clock period  =  order of one grain at the apex in K
              =  the least common denominator of the column of L̃⁻¹ belonging to the apex
```

This is Dhar's description of the grain operators as phases, `a_j = exp(iφ_j)` with `φ = 2π Δ⁻¹ n` for integer vectors `n`, applied to the reduced Laplacian `Δ = L̃`.[^2] Simulation and the formula agree on every castle tested in both models.[^1] The period divides the **exponent** of `K`, its largest invariant factor, and equals the order `|K|` exactly when one grain at the apex generates `K`. Dhar, Ruelle, Sen and Verma state the same principle for a deterministic sandpile that always adds at one site: its period is the order of that site's addition operator.[^3]

## Tree branches

**Lemma.** Let `r` be a cell, and let `T` be a set of cells, none of them in the sink, such that `T ∪ {r}` induces a tree in the castle graph and no cell of `T` has a neighbor outside `T ∪ {r}`. Then in `K` one grain at any cell of `T` equals one grain at `r`; if `r` is a sink cell, it equals zero.

*Proof.* Root the tree at `r` and show, from the leaves up, that a grain at a cell `x` of `T` equals a grain at its parent `p`. If `x` has degree `d`, toppling `x` shows that `d` grains at `x` equal one grain at `p` plus one grain at each of its `d − 1` children; by the inductive step each child's grain equals a grain at `x`, so `d` grains at `x` equal one at `p` and `d − 1` at `x`.

With the bottom-left sink cell, on `(2, 2, 3)` the top cell `(2, 2)` and the cell `(2, 1)` below it both have order 5; on `(2, 2, 1, 1, 1)` the cells `(2, 0)`, `(3, 0)`, `(4, 0)` all have order 4, the order at `(1, 0)`, where they attach.[^4] In a tree castle every cell lies in a branch attached to the sink, so every grain is zero in `K`.

**In the tide model the bottom row is the sink.** A column whose neighbors have height at most 1 stands alone on the bottom row, and its raised cells form a branch attached to the sink. So when the apex tops such a column, the tide period is 1: `(3, 1, 2, 2)` has `K_tide = Z/3` and tide period 1.[^4]

## The sink clock depends on the sink and the apex

The sink-model period depends on the castle and on two chosen cells. On `(2, 2, 2)`, one grain at the top-right cell has order 5, 3, 15, 15, 15 as the sink moves through the other five cells.[^5] The convention "bottom-left sink cell, leftmost apex" is not mirror-symmetric: `(2, 3)` ticks with period 2 and its mirror image `(3, 2)` with period 4. Up to 12 cells, a castle and its mirror image have different periods in 1,018 of the 1,953 pairs of castles that are not their own mirror image.[^6]

**The sink clock spectrum** of a castle is the multiset of orders of one grain at `v` with sink cell `d`, over every ordered pair of cells `d ≠ v`. It depends only on the castle's graph.

## The tide clock

In the tide model the only choice is the apex.

- **The tide clock depends only on the runs.** The runs of raised columns are the maximal runs of adjacent columns of height at least 2. In the tide model they exchange no sand, and `K_tide` is the product of the runs' groups ([[sandpile-group](pages/sandpile-group.md)], Part 3). So the tide period is the order of the apex grain in the group of the apex's run.
- **Mirror images.** Mirroring a castle mirrors its tide model. Up to 12 cells, a castle and its mirror image have different tide periods in **204** of the 1,953 pairs, against 1,018 in the sink model, and each of the 204 has two or more tallest columns, so that the leftmost apex of the castle and of its mirror image are different cells. The first are `(2, 1, 2, 2)`, whose leftmost apex tops a column standing alone (period 1), against `(2, 2, 1, 2)` (period 3), and `(1, 2, 1, 2, 2)` (1 against 3).[^7]
- **The tide clock spectrum** is the multiset of orders of one grain at each cell above the bottom row. It equals the mirror image's spectrum on all 1,953 pairs to 12 cells, it depends only on the multiset of runs (each run up to mirror image, computed to 12 cells), and it is not a graph invariant: `(2, 2, 2)` and `(3, 3)` have the same graph and tide spectra `{4: 1, 8: 2}` and `{11: 4}`.[^7]

## The census

Over all 33,150 castles with at most 16 cells (mirror images removed), with the leftmost apex and, in the sink model, the bottom-left sink cell:[^8]

| | sink model | tide model |
|---|---|---|
| tree castles (trivial group, period 1) | 6,963 | 6,963 |
| nontrivial group | 26,187 | 26,187 |
| … apex grain generates `K` (period `= |K|`) | 8,839 | 13,159 |
| … period equals the exponent of `K` | 10,915 | 15,286 |
| … period below the exponent | 15,272 | 10,901 |
| … period 1 | 3,769 | 6,611 |
| most common periods (nontrivial group) | 4, 1, 2, 15, 5, 3, 209, 56 | 1, 3, 11, 8, 21, 29, 4, 41 |

In all 6,611 tide-model castles with a nontrivial group and period 1, the apex tops a column standing alone on the bottom row, as in the section *Tree branches*.

## Separating cospectral castles

[[sandpile-census](pages/sandpile-census.md)] finds that the sink group separates none of the cospectral groups of [[isospectral-castles](pages/isospectral-castles.md)]. On the 105 adjacency and 17 Laplacian cospectral groups to 16 cells, with every skyline of every graph in each group, a group counts as separated when two castles with non-isomorphic graphs get different values:[^9]

| cospectral groups (to 16 cells) | number | separated by the fixed-convention sink period | separated by the sink clock spectrum |
|---|---|---|---|
| same adjacency spectrum | 105 | 57 | **62** |
| same Laplacian spectrum | 17 | 4 | **5** |

The fixed-convention period is not a graph invariant: skylines of the same graph can tick differently, and the sink clock spectrum removes that dependence.

- **The 10-cell pair.** The adjacency-cospectral pair `(1,1,1,2,3,2)` and `(1,1,2,2,3,1)` of [[hear-the-shape-seminar](pages/hear-the-shape-seminar.md)] has the same spectrum and the same group `K_sink = Z/15`. Its sink clocks tick **15** and **5**, and over the 90 (sink, grain) pairs the orders `1, 3, 5, 15` occur `14, 10, 14, 52` times against `10, 16, 18, 46`.
- **The 13-cell Laplacian pair** `(1,1,1,2,3,1,1,2,1)` and `(1,2,1,2,6,1)` is the smallest Laplacian-cospectral group the sink clock spectrum separates: over all 156 pairs the orders `1, 2, 4` occur `44, 28, 84` times against `42, 54, 60`. Both skylines tick 2 under the fixed convention; the other skylines of the first graph, `(1,2,1,1,3,2,1,2)` and `(1,2,1,1,5,2,1)`, tick 4.

The smallest cospectral castles that the sink clock spectrum separates have 10 cells for the adjacency spectrum and 13 cells for the Laplacian spectrum.

**The tide clock.** Every one of the 122 cospectral groups contains castles of different widths across its graphs, so the tide clock spectrum, one order per cell above the bottom row, differs within every group. The fixed-apex tide period separates **49** of the 105 adjacency groups and **none** of the 17 Laplacian groups; 11 of the Laplacian groups consist of tree castles, which never tick.[^9] On the 10-cell pair both castles have `K_tide = Z/8`, their tide clocks tick **4** and **8**, and their tide clock spectra are `{4: 2, 8: 2}` and `{4: 1, 8: 3}`.

[[sandpile-identity](pages/sandpile-identity.md)] gives a sink-model invariant that separates all 122 groups, the sink avalanche profile.

## Snippet

```python
import sympy as sp
from math import lcm
from collections import Counter

def cells_of(c):
    return [(i, j) for i, h in enumerate(c) for j in range(h)]

def sink_cells(c, model):                  # 'sink': the bottom-left cell; 'tide': the whole bottom row
    return {(0, 0)} if model == 'sink' else {(i, 0) for i in range(len(c))}

def board(c, sink):                        # sand-holding cells, their non-sink neighbors, full degrees
    S = set(cells_of(c))
    around = lambda v: [u for u in ((v[0]+1, v[1]), (v[0]-1, v[1]), (v[0], v[1]+1), (v[0], v[1]-1)) if u in S]
    live = [v for v in cells_of(c) if v not in sink]
    return live, {v: [u for u in around(v) if u not in sink] for v in live}, {v: len(around(v)) for v in live}

def apex(c):                               # top cell of the leftmost tallest column
    return (c.index(max(c)), max(c) - 1)

def stabilize(b, g):                       # topple until every cell holds fewer grains than neighbors
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

- [[sandpile-group](pages/sandpile-group.md)] - the sandpile, the two models, the groups, and the runs of raised columns the tide clock depends on.
- [[sandpile-census](pages/sandpile-census.md)] - the groups of every castle to 16 cells in both models; the sink group separates no cospectral group.
- [[isospectral-castles](pages/isospectral-castles.md)] - the cospectral castles the clock spectra are tested on; [[hear-the-shape-seminar](pages/hear-the-shape-seminar.md)] - a seminar built on them.
- [[castle-graph](pages/castle-graph.md)] - tree castles, whose clock never ticks.
- [[sandpile-identity](pages/sandpile-identity.md)] - the identity the clock starts from, and the avalanche profiles.
- [[castle-avalanches](pages/castle-avalanches.md)] - grains dropped on random cells instead of on one cell.
- [[sandcastle-seminar](pages/sandcastle-seminar.md)] - the castle `(3,2,1,2,2,1,2,3)` followed through both models.
- [[castle-eigenvalues-by-example](pages/castle-eigenvalues-by-example.md)] - the 10-cell cospectral pair worked by hand, whose sink clocks tick 15 and 5.
- [[castle-ring-invariant-factors](pages/castle-ring-invariant-factors.md)] - the order of one element against the exponent of a group read from its invariant factors, for the unit groups `F_p[x]/(char_k)`.

## Appearances in Sources

- [[dhar-1990-self-organized-critical-sandpile](pages/dhar-1990-self-organized-critical-sandpile.md)] - the grain operators as phases `φ = 2πΔ⁻¹n`, from which the period formula follows.
- [[dhar-ruelle-sen-verma-1995-algebraic-aspects](pages/dhar-ruelle-sen-verma-1995-algebraic-aspects.md)] - the period of a deterministic sandpile as the order of one addition operator, and the toppling invariants built from `Δ⁻¹`.
- [[rossin-2000-group-of-a-sandpile](pages/rossin-2000-group-of-a-sandpile.md)] - the group operation, add and then stabilize, that makes the period an order in the group.
- [[project-euler-502-castle-factoring](pages/project-euler-502-castle-factoring.md)] - the castle definition behind the castle graph.

## Footnotes

[^1]: Verified by execution (Python 3.11, 2026-10-16): `clock_by_simulation` (start at `stab(2m − stab(2m))`, add one grain at the apex, stabilize, count the ticks back to the identity) equals the least common denominator of `L̃⁻¹ e_apex` in the sink model for `(2,2)`, `(2,2,2)`, `(1,2,1)`, `(3,3,3)`, `(2,2,2,2)`, `(1,1,1,2,3,2)`, `(1,1,2,2,3,1)`, `(2,2,1,2,2)`, `(2,3,3,2)` (periods 4, 15, 1, 8, 56, 15, 5, 4, 52), and in the tide model for `(2,2)`, `(2,2,2)`, `(3,3)`, `(3,3,3)`, `(2,2,2,2)`, `(1,1,1,2,3,2)`, `(1,1,2,2,3,1)`, `(2,2,1,2,2)`, `(2,3,3,2)`, `(1,2,1)`, `(3,2,1,2,2,1,2,3)`, `(2,3)`, `(3,2)` (periods 3, 8, 11, 95, 21, 4, 8, 3, 75, 1, 3, 3, 3); the table and several of these are pinned in the Snippet. The group operation is Rossin's, [[rossin-2000-group-of-a-sandpile](pages/rossin-2000-group-of-a-sandpile.md)] §2 L37 - "u ⊕ v = (u+v)^".
[^2]: [[dhar-1990-self-organized-critical-sandpile](pages/dhar-1990-self-organized-critical-sandpile.md)] p.1614 L126-156 [synthesis] - since the `a_j` commute, the representations of the operator algebra are one-dimensional, `a_j = exp(iφ_j)` (eq. 10), with `Σ_j Δ_ij φ_j = 2πn_i` and `φ_i = 2π Σ_j [Δ⁻¹]_ij n_j` (eqs. 11-12, read from the page image); `Δ = L̃` is symmetric for a castle, so rows and columns agree.
[^3]: [[dhar-ruelle-sen-verma-1995-algebraic-aspects](pages/dhar-ruelle-sen-verma-1995-algebraic-aspects.md)] §7 Question 1 pp. 25-27, eqs. (7.1)-(7.3) - "the period of the cycle T_L is independent of the initial configuration"; "T_L is the order of the operator a(L+1, L+1) on the space R of recurrent configurations"; `T_L = (Det Δ)/M` with `M` the gcd of the central column of `E = (Det Δ)Δ⁻¹`, and `T_L` dividing the largest elementary divisor. The toppling invariants `Q_i = Σ_j (Δ⁻¹)_ij z_j mod 1` (§3 p. 6, eq. 3.3) vanish on `t e_v` exactly when `L̃⁻¹ (t e_v)` is integral.
[^4]: Verified by execution (Python 3.11, 2026-10-16): with the bottom-left sink cell, the orders on `(2,2,3)` are 15 at `(0,1)`, `(1,0)`, `(1,1)`, 3 at `(2,0)`, and 5 at `(2,1)` and `(2,2)`; on `(2,2,1,1,1)` the cells `(2,0)`, `(3,0)`, `(4,0)` and `(1,0)` all have order 4; `(3,1,2,2)` has `|K_tide| = 3` and tide period 1.
[^5]: Verified by execution (Python 3.11, 2026-10-16): the order of one grain at `(2,1)` on `(2,2,2)` with the sink at `(0,0)`, `(0,1)`, `(1,0)`, `(1,1)`, `(2,0)`: 5, 3, 15, 15, 15 (pinned in the Snippet); all 30 (sink, grain) orders on `(2,2,2)` lie in `{3, 5, 15}`.
[^6]: Verified by execution (Python 3.11, 2026-10-16): for the 1,953 castles with at most 12 cells that are not their own mirror image, the fixed-convention sink periods of the castle and its mirror image differ in 1,018 cases, the first `(2,3)` (2) against `(3,2)` (4).
[^7]: Verified by execution (Python 3.11, 2026-10-16): for the same 1,953 pairs, the tide periods with the leftmost apex differ in 204 cases, none with a unique tallest column, the first by cell count `(2,1,2,2)` (1) against `(2,2,1,2)` (3) and `(1,2,1,2,2)` (1) against `(2,2,1,2,1)` (3); the tide clock spectra of a castle and its mirror image agree on all 1,953 pairs; grouping the castles with at most 12 cells by their multiset of runs, each up to mirror image, every group has one tide clock spectrum.
[^8]: Verified by execution (Python 3.11, 2026-10-16): exact integer adjugates of `L̃` for all 33,150 castles in both models; the order of one grain at `v` is `det L̃ / gcd(det L̃, column v of the adjugate)`, the exponent is the least common multiple of these orders, and `|K| = det L̃`; every count in the table; the 6,611 tide castles with period 1 and nontrivial group, each with its apex on a column whose neighbors have height at most 1.
[^9]: Verified by execution (Python 3.11, NumPy, networkx, 2026-10-16): the 105 adjacency and 17 Laplacian cospectral groups to 16 cells (exact isomorphism tests within each spectral group, exact characteristic polynomials), with all 1,128 of their castles; for each castle the fixed-convention sink period, the sink clock spectrum and the fixed-apex tide period. The sink clock spectrum is equal on castles with the same graph; the fixed-convention periods are not. The orders of the 10-cell and 13-cell pairs are as stated; 11 of the 17 Laplacian groups consist of tree castles; in every group two castles with different graphs have different widths.
