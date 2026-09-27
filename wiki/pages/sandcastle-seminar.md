---
title: Sandcastles seminar - one silver castle, grain by grain, in the sink and tide models
category: Concepts
summary: The seminar walk-through for the "Sandcastles" arc, following one castle, the 16-cell silver castle (3,2,1,2,2,1,2,3), through the whole sandpile story in two models that differ only in where the sand leaves - the sink model (one sink cell, the bottom-left cell) and the tide model (the whole bottom row, the ground). One grain on its left tower sets off a 16-toppling wave across the castle in the sink model, losing 2 grains to the sink, but only 4 topplings under the tide, where the ground swallows sand everywhere. Its recurrent piles form Z/4 × Z/4 × Z/4 (64 piles) in the sink model and Z/3 × Z/3 × Z/3 (27 piles) under the tide, read straight off its three separate 2×2 blocks: the block matrix is 4I in the sink model and 3I under the tide, because every block sits on the ground. The sink group depends only on how the blocks touch, which is why on every castle up to 16 cells it hears nothing the spectrum misses; the tide group also sees how high the blocks stand, so it tells the silver rectangle lying down (Z/8) from standing up (Z/11). Its clock ticks 4 in the sink model, with a clock spectrum of periods 1, 2, 4 occurring 16, 48, 176 times over every sink and grain cell, and 3 under the tide, on every one of its 8 raised cells. Its identity has empty tower tops in both models. Under the tide it barely avalanches (mean 1.667 topplings, never more than 4); in the sink model the mean is 32.1 and avalanches reach 149. One runnable block pins every value in both models.
tags: [concept, castle, seminar, pedagogy, teaching, sandpile, silver-ratio, critical-group, identity-element, clock, avalanche, sink-model, tide-model, isospectral]
sources: [project-euler-502-castle-factoring, rossin-2000-group-of-a-sandpile, dhar-ruelle-sen-verma-1995-algebraic-aspects]
created: 2026-09-26
updated: 2026-09-27
---

# Sandcastles seminar - one silver castle, grain by grain, in the sink and tide models

**Thesis.** Pour sand on a castle, one grain at a time, and a rich mathematical object appears: a finite group, a clock, an identity pile, and avalanches of every size. All of it is controlled by the castle's `2 × 2` blocks and by where the sand leaves. There are two natural places for it to leave, one sink cell or the whole ground, and they give two different theories of the same castle. This seminar follows a single castle through the whole story in both, side by side.

**Format.** About 60 minutes, seven stops. Every value quoted is pinned by the Snippet block at the end. The research pages behind the stops are [[sandpile-group](pages/sandpile-group.md)], [[sandpile-census](pages/sandpile-census.md)], [[sandcastle-clock](pages/sandcastle-clock.md)], [[sandpile-identity](pages/sandpile-identity.md)] and [[castle-avalanches](pages/castle-avalanches.md)], each of which treats both models.

## Stop 0 - the castle, and the two models

```
#......#
##.##.##          (3, 2, 1, 2, 2, 1, 2, 3):  16 cells, three separate 2×2 blocks, all on the ground
########
```

It is a **silver castle**: the largest eigenvalue of its graph is `1 + √2`, the same as the `3 × 2` silver rectangle's ([[castle-graph-spectral-radius](pages/castle-graph-spectral-radius.md)]). It is also its own mirror image, so choices like "the leftmost apex" cause no ambiguity.

The two models ([[sandpile-group](pages/sandpile-group.md)], Part 1):

| | sink model | tide model |
|---|---|---|
| where sand leaves | one sink cell, the bottom-left cell, drawn `S` | the whole bottom row, the ground, drawn `~` |
| what the castle becomes | the castle graph | the castle with its bottom row merged into one vertex |
| what this castle looks like to the sand | one connected castle | three separate runs of raised columns, `(3, 2)`, `(2, 2)` and `(2, 3)`, each standing on the ground |

*Idea:* one well-chosen castle can carry the whole theory, and where the sand leaves decides which theory.

## Stop 1 - the game

Each cell is a bowl whose capacity is its number of neighbours. A bowl that reaches capacity **topples**, sending one grain to each neighbour. A neighbour always accepts, even if it then topples too. Grains leave only through the sink. The tower tops have a single neighbour, so they hold nothing: one grain there topples at once.

Start from the fullest stable pile (every bowl one grain short) and drop one grain on the left tower's top.

**Sink model.**

```
                 top row    middle     bottom row
start            0......0   21.11.12   S2122121
drop on (0,2)    1......0   21.11.12   S2122121
topple (0,2)     0......0   31.11.12   S2122121
topple (0,1)     1......0   02.11.12   S2122121     <- one grain into the sink
topple (0,2)     0......0   12.11.12   S2122121
topple (1,1)     0......0   20.11.12   S3122121
topple (1,0)     0......0   21.11.12   S0222121     <- another into the sink
topple (2,0)     0......0   21.11.12   S1032121
topple (3,0)     0......0   21.21.12   S1103121
topple (3,1)     0......0   21.02.12   S1113121
topple (4,0)     0......0   21.03.12   S1120221
topple (4,1)     0......0   21.11.12   S1121221
topple (5,0)     0......0   21.11.12   S1122031
topple (6,0)     0......0   21.11.22   S1122102
topple (6,1)     0......0   21.11.03   S1122112
topple (7,0)     0......0   21.11.04   S1122120
topple (7,1)     0......1   21.11.11   S1122121
topple (7,2)     0......0   21.11.12   S1122121     settled
```

One grain, **16 topplings**, a wave that crosses the whole castle and ends on the far tower's top. Two grains leave through the sink, both from its neighbours `(0,1)` and `(1,0)`.[^1]

**Tide model.**

```
                 top row    middle     bottom row
start            0......0   21.11.12   ~~~~~~~~
drop on (0,2)    1......0   21.11.12   ~~~~~~~~
topple (0,2)     0......0   31.11.12   ~~~~~~~~
topple (0,1)     1......0   02.11.12   ~~~~~~~~     <- one grain into the ground
topple (0,2)     0......0   12.11.12   ~~~~~~~~
topple (1,1)     0......0   20.11.12   ~~~~~~~~     <- another          settled
```

The same grain, **4 topplings**, and the wave never leaves the left run. Two grains are lost again, but now straight into the ground below the cells that toppled.[^1]

*Idea:* local rules, global effects, and the global effects depend on where the sand can leave.

## Stop 2 - the sand forms a group

Keep dropping grains. Some piles never come back; the ones that keep recurring are the **recurrent** piles. They form a group, the **sandpile group**, whose order is the number of spanning trees of the graph behind the model.

Its structure can be read off the `2 × 2` blocks ([[sandpile-group](pages/sandpile-group.md)], Part 3): the group is `Z^r` modulo a small **block matrix**, one row per block, with `−1` for each pair of blocks sharing an edge. The diagonal is `4` in the sink model. Under the tide it is `3` for a block sitting on the ground, whose cycle has become a triangle through the ground, and `4` above. This castle's three blocks are separate and all sit on the ground:

```
sink model                          tide model
[4 0 0]                             [3 0 0]
[0 4 0]   →  Z/4 × Z/4 × Z/4        [0 3 0]   →  Z/3 × Z/3 × Z/3
[0 0 4]      64 recurrent piles     [0 0 3]      27 recurrent piles
```

Each separate block holds its own `Z/4` of sand in the sink model and its own `Z/3` under the tide. Compare the silver rectangle `(2, 2, 2)`, whose two blocks touch: its block matrix gives one bigger cyclic group, `Z/15` in the sink model (`[[4, −1], [−1, 4]]`) and `Z/8` under the tide (`[[3, −1], [−1, 3]]`).[^2]

*Idea:* the sand lives in the 2×2 blocks. Separate blocks multiply, and touching blocks merge into a bigger group. A path of touching blocks always gives one cyclic factor, in both models; denser clusters can split, and the models disagree on which: the `2 × 2` square of blocks `(3, 3, 3)` is `Z/8 × Z/24` in the sink model but `Z/95` under the tide ([[sandpile-census](pages/sandpile-census.md)]).

## Stop 3 - what each group can and cannot hear

**Sink model.** The block matrix depends only on how the blocks touch each other. So **any** castle with three separate blocks has the same sink group. `(2, 2, 1, 2, 2, 1, 2, 2)` has no towers and a different spectrum, yet its sink group is also `Z/4 × Z/4 × Z/4`. That is also why the sink group separates no cospectral pair: across every castle up to 16 cells, castles with the same spectrum always have the same block arrangement, so they always have the same sink group ([[sandpile-census](pages/sandpile-census.md)]).

**Tide model.** The tide block matrix also records which blocks touch the ground, so the tide group hears something the sink group cannot: how the blocks stand. `(2, 2, 1, 2, 2, 1, 2, 2)` still matches this castle (three separate ground blocks, `Z/3 × Z/3 × Z/3`), but the silver rectangle `(2, 2, 2)` and the tall pair `(3, 3)`, the same graph lying down and standing up, have the same sink group `Z/15` and different tide groups, `Z/8` and `Z/11`. What the tide cannot hear is where the runs of raised columns sit along the ground: sliding a run, or swapping two runs, changes nothing.[^2]

*Idea:* a graph invariant cannot tell a shape from its rotation; the ground can.

## Stop 4 - the clock

Start at the **identity** pile (Stop 5) and drop one grain on the left tower's top every tick. The pile returns to the identity after a whole number of ticks, the **clock period**: the order of "one grain on the apex" in the group ([[sandcastle-clock](pages/sandcastle-clock.md)]).

| | sink model | tide model |
|---|---|---|
| clock period | **4**, the largest order in `Z/4 × Z/4 × Z/4` | **3**, the largest order in `Z/3 × Z/3 × Z/3` |
| clock spectrum | over every sink cell and grain cell (240 pairs): periods `1, 2, 4` occur `16, 48, 176` times | over every cell above the ground (8 cells): period `3` every time |
| what it depends on | the castle's graph (the spectrum); the fixed-sink period depends on where the sink is | the castle's shape; there is no sink to choose |

In the sink model the clock spectrum is a graph invariant, and unlike the group it separates many cospectral castles (62 of the 105 adjacency-cospectral groups to 16 cells). Under the tide every raised cell of this castle ticks 3: each separate block is a `Z/3`, and a grain anywhere on a tower is the same as a grain on the block below it.[^3]

*Idea:* an element of a finite group has an order, and an order is a clock.

## Stop 5 - the identity

The identity is the recurrent pile that acts like zero: add it to any recurrent pile, topple, and nothing changes. It is `stab(2m − stab(2m))`, where `m` is the fullest stable pile ([[sandpile-identity](pages/sandpile-identity.md)]):

```
sink model (sink S)              tide model (ground ~)
0......0                         0......0
11.10.12                         11.11.11
S2122121                         ~~~~~~~~
```

Both have empty tower tops. A grain on a tower top can always topple down into the block below, so in the group it is the same as a grain on that block. Tree branches are transparent: the towers add shape but no sand. Under the tide the identity is almost trivially regular, and in the sink model it is irregular. One grain dropped on the apex of either identity topples once and settles.[^4]

## Stop 6 - avalanches, and where the sand leaves

Now drop grains at **random** cells, starting from the identity. By Dhar's theorem the average avalanche size is exact: the average row sum of the inverse reduced Laplacian, that is, the total of its entries divided by the number of cells ([[castle-avalanches](pages/castle-avalanches.md)]).

| model | mean topplings per grain (exact) | simulated mean (20,000 drops) | largest avalanche |
|---|---|---|---|
| tide (the ground) | 1.667 | 1.66 | 4 |
| sink (bottom-left cell) | 32.133 | 32.06 | 149 |

The castle is only 3 high, so under the tide sand reaches the ground almost at once, and nothing ever avalanches far. In the sink model every grain must cross the castle to escape, as in Stop 1, and the mean rises twentyfold. The tide mean, 1.667, is just below this castle's column-by-column prediction of 1.75. The prediction is exact only when every run of adjacent columns rising above the base has constant height, and here the outer runs `(3, 2)` and `(2, 3)` do not. On [[castle-avalanches](pages/castle-avalanches.md)] the tide mean never exceeds the prediction on any castle up to 12 cells; for larger castles, this one included, the inequality is conjectured. No such prediction is known in the sink model, where the mean depends on width as well as height and the `2 × 2` blocks lower it by giving sand more routes to the sink.[^5]

*Idea:* the same castle can be calm or explosive depending on one modelling choice, where the sand leaves.

## The board

| stop | measurement | sink model | tide model |
|---|---|---|---|
| 1 | one grain on the full pile | 16 topplings, 2 grains lost | 4 topplings, 2 grains lost |
| 2 | recurrent piles, group | 64, `Z/4 × Z/4 × Z/4` from `4I` | 27, `Z/3 × Z/3 × Z/3` from `3I` |
| 3 | what the group hears | how the blocks touch | how the blocks touch and how they stand on the ground |
| 4 | clock, clock spectrum | 4; periods `1, 2, 4` × `16, 48, 176` | 3; period `3` on all 8 raised cells |
| 5 | identity | tower tops empty, irregular | tower tops empty, regular |
| 6 | mean avalanche, largest | 32.133, 149 | 1.667, 4 |

The silver rectangle `(2, 2, 2)` shares this castle's spectral radius but not its sand. Its two blocks touch and give `Z/15` (sink) and `Z/8` (tide), its clocks tick 15 and 8, and it has no towers. Same "silver" loudest note, different sandcastle in either model.

## Snippet

```python
import numpy as np, sympy as sp, random
from math import lcm
from collections import Counter
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ

C = (3, 2, 1, 2, 2, 1, 2, 3)                # the silver castle of this seminar

def cells_of(c):
    return [(i, j) for i, h in enumerate(c) for j in range(h)]

def board(c, sinks):                       # sand-holding cells, their non-sink neighbours, full degrees
    S = set(cells_of(c))
    around = lambda v: [u for u in ((v[0]+1, v[1]), (v[0]-1, v[1]), (v[0], v[1]+1), (v[0], v[1]-1)) if u in S]
    live = [v for v in cells_of(c) if v not in sinks]
    return live, {v: [u for u in around(v) if u not in sinks] for v in live}, {v: len(around(v)) for v in live}

SINK, TIDE = {(0, 0)}, {(i, 0) for i in range(len(C))}   # the sink model's sink cell; the tide model's ground

def stabilize(b, g, trace=False):          # topple one unstable cell at a time; returns pile, topplings, grains lost
    live, nb, deg = b
    g, n, lost, steps = dict(g), 0, 0, []
    while True:
        un = [v for v in live if g[v] >= deg[v]]
        if not un:
            return (g, n, lost, steps) if trace else (g, n, lost)
        v = un[0]; g[v] -= deg[v]; n += 1; lost += deg[v] - len(nb[v])
        for u in nb[v]:
            g[u] += 1
        steps.append(v)

def identity(b):                           # stab(2m - stab(2m)), m = the fullest stable pile
    live, nb, deg = b
    m = {v: deg[v] - 1 for v in live}
    s = stabilize(b, {v: 2 * m[v] for v in live})[0]
    return stabilize(b, {v: 2 * m[v] - s[v] for v in live})[0]

def draw(c, g, sink_mark):                 # top row first; sink cells drawn with sink_mark
    return [''.join('.' if j >= h else str(g[(i, j)]) if (i, j) in g else sink_mark for i, h in enumerate(c))
            for j in range(max(c) - 1, -1, -1)]

def recurrent_count(b):                    # piles that recur as sand is added
    live, nb, deg = b
    top = tuple(deg[v] - 1 for v in live)
    seen, todo = {top}, [top]
    while todo:
        x = todo.pop()
        for k in range(len(live)):
            y = list(x); y[k] += 1
            y = stabilize(b, dict(zip(live, y)))[0]
            y = tuple(y[v] for v in live)
            if y not in seen:
                seen.add(y); todo.append(y)
    return len(seen)

def block_matrix(c, tide=False):           # one row per 2x2 block: -1 for blocks sharing an edge; 4 on the diagonal, 3 for ground blocks under the tide
    B = [(i, j) for i in range(len(c) - 1) for j in range(min(c[i], c[i+1]) - 1)]
    return sp.Matrix(len(B), len(B), lambda a, b: (3 if tide and B[a][1] == 0 else 4) if a == b else
                     -1 if abs(B[a][0] - B[b][0]) + abs(B[a][1] - B[b][1]) == 1 else 0)

def group(M):                              # nontrivial invariant factors of Z^r / M
    S = smith_normal_form(M, domain=ZZ)
    return [abs(S[i, i]) for i in range(M.rows) if abs(S[i, i]) != 1]

def reduced_laplacian(b):
    live, nb, deg = b
    return sp.Matrix(len(live), len(live), lambda r, s: deg[live[r]] if r == s else -(live[s] in nb[live[r]]))

def grain_orders(c, sinks):                # order of one grain at each cell: lcm of denominators of a column of L~^-1
    b = board(c, sinks); Linv = reduced_laplacian(b).inv()
    return {v: lcm(*[sp.fraction(x)[1] for x in Linv[:, k]]) for k, v in enumerate(b[0])}

def mean_avalanche(b):                     # Dhar: sum of all entries of L~^-1 over the number of cells
    Linv = np.linalg.inv(np.array(reduced_laplacian(b).tolist(), dtype=float))
    return Linv.sum() / Linv.shape[0]

def random_drops(b, drops, seed=2):        # from the identity; returns the topplings of each drop
    live = b[0]; g = identity(b); rng = random.Random(seed); out = []
    for _ in range(drops):
        v = live[rng.randrange(len(live))]; g[v] += 1
        g, n, _ = stabilize(b, g); out.append(n)
    return np.array(out)
```

```
>>> b = board(C, SINK); live, nb, deg = b
>>> full = {v: deg[v] - 1 for v in live}; full[(0, 2)] += 1
>>> settled, n, lost, steps = stabilize(b, full, trace=True)
>>> n, lost, draw(C, settled, 'S')
(16, 2, ['0......0', '21.11.12', 'S1122121'])
>>> t = board(C, TIDE); full = {v: t[2][v] - 1 for v in t[0]}; full[(0, 2)] += 1
>>> settled, n, lost, steps = stabilize(t, full, trace=True)
>>> n, lost, steps, draw(C, settled, '~')
(4, 2, [(0, 2), (0, 1), (0, 2), (1, 1)], ['0......0', '20.11.12', '~~~~~~~~'])
>>> recurrent_count(b), recurrent_count(t), group(block_matrix(C)), group(block_matrix(C, tide=True))
(64, 27, [4, 4, 4], [3, 3, 3])
>>> group(block_matrix((2, 2, 2))), group(block_matrix((2, 2, 2), tide=True)), group(block_matrix((3, 3), tide=True))
([15], [8], [11])
>>> group(block_matrix((2, 2, 1, 2, 2, 1, 2, 2))), group(block_matrix((2, 2, 1, 2, 2, 1, 2, 2), tide=True))
([4, 4, 4], [3, 3, 3])
>>> draw(C, identity(b), 'S'), draw(C, identity(t), '~')
(['0......0', '11.10.12', 'S2122121'], ['0......0', '11.11.11', '~~~~~~~~'])
>>> grain_orders(C, SINK)[(0, 2)], sorted(Counter(o for d in cells_of(C) for o in grain_orders(C, {d}).values()).items())
(4, [(1, 16), (2, 48), (4, 176)])
>>> grain_orders(C, TIDE)[(0, 2)], sorted(Counter(grain_orders(C, TIDE).values()).items())
(3, [(3, 8)])
>>> [stabilize(x, {v: identity(x)[v] + (v == (0, 2)) for v in x[0]})[1] for x in (b, t)]
[1, 1]
>>> round(float(mean_avalanche(t)), 3), round(float(mean_avalanche(b)), 3)
(1.667, 32.133)
>>> tide, one = random_drops(t, 20000), random_drops(b, 20000)
>>> round(float(tide.mean()), 2), int(tide.max()), round(float(one.mean()), 2), int(one.max())
(1.66, 4, 32.06, 149)
```

## Exercises for the room

1. In the sink-model Stop 1 trace, the wave reaches the middle block only through `(2,0)`. Why is that cell the only link, and why does no such link exist under the tide?
2. Write down the block matrix of `(3, 3, 3)`, a `2 × 2` square of blocks, in both models, and check that the groups are `Z/8 × Z/24` (sink) and `Z/95` (tide).
3. Explain why every tower top holds 0 grains in every recurrent pile, in both models.
4. Find a castle whose tide mean equals its column prediction and one where it falls short. Which runs of columns decide it?
5. Why does every raised cell of this castle tick 3 under the tide? Find a castle where two raised cells tick at different periods under the tide.
6. (Open.) Is the sink avalanche profile of [[sandpile-identity](pages/sandpile-identity.md)] a complete fingerprint of castle graphs?

## What is still open

**Sink model.**
- whether the sink avalanche profile is a complete invariant of castle graphs ([[sandpile-identity](pages/sandpile-identity.md)]; no counterexample up to 13 cells);
- whether two cospectral castles can have different block graphs, the only way the sink group could separate them ([[sandpile-census](pages/sandpile-census.md)]);
- which clusters of blocks that are not paths still give a cyclic sink group (`(2, 3, 3, 3)` does, `(3, 3, 3)` does not);
- a closed form for the mean avalanche of a rectangle, which depends on width and height ([[castle-avalanches](pages/castle-avalanches.md)]).

**Tide model.**
- a proof that the tide mean never exceeds the column prediction, checked to 12 cells ([[castle-avalanches](pages/castle-avalanches.md)]);
- the tide identity of a general run, beyond the rectangle pattern ([[sandpile-identity](pages/sandpile-identity.md)]);
- which non-path clusters give a cyclic tide group (`(3, 3, 3)` does, `(4, 4, 4)` does not) ([[sandpile-census](pages/sandpile-census.md)]);
- which tide invariant, finer than the sorted avalanche profile, recovers a castle's runs of raised columns ([[sandpile-identity](pages/sandpile-identity.md)]).

## Appearances in Sources

- [[dhar-ruelle-sen-verma-1995-algebraic-aspects](pages/dhar-ruelle-sen-verma-1995-algebraic-aspects.md)] - the sink-model algebra (Smith normal form, `|K| = det Δ`) behind Stops 2-4.
- [[rossin-2000-group-of-a-sandpile](pages/rossin-2000-group-of-a-sandpile.md)] - the sandpile group, its sink independence and the identity recipe the seminar uses in both models.
- [[project-euler-502-castle-factoring](pages/project-euler-502-castle-factoring.md)] - the castle definition behind the castle graph.

## Related Concepts

- [[sandpile-group](pages/sandpile-group.md)] - the game, the two models, the matrices, and the 2×2-block picture with its tide diagonal (Stops 0-2).
- [[sandpile-census](pages/sandpile-census.md)] - every castle's group in both models, and what each separates (Stop 3).
- [[sandcastle-clock](pages/sandcastle-clock.md)] - the clock and the clock spectrum in both models (Stop 4).
- [[sandpile-identity](pages/sandpile-identity.md)] - the identity and the avalanche profiles (Stop 5).
- [[castle-avalanches](pages/castle-avalanches.md)] - random dropping, Dhar's theorem, and the tide inequality (Stop 6).
- [[castle-graph-spectral-radius](pages/castle-graph-spectral-radius.md)] - the silver castles.
- [[hear-the-shape-seminar](pages/hear-the-shape-seminar.md)] / [[one-bit-seminar](pages/one-bit-seminar.md)] / [[hardin-identity-seminar](pages/hardin-identity-seminar.md)] / [[oeis-mining-seminar](pages/oeis-mining-seminar.md)] / [[castle-fibers-char-2-walkthrough](pages/castle-fibers-char-2-walkthrough.md)] / [[tower-recursion-master-class](pages/tower-recursion-master-class.md)] - the other seminar pages.
- [[pell-castle-strip](pages/pell-castle-strip.md)] / [[castle-cryptography](pages/castle-cryptography.md)] / [[song-as-castle](pages/song-as-castle.md)] - the seminar pages of the silver-ratio strip, the castle cryptography series and Beethoven's Ninth at every scale.

## Footnotes

[^1]: Verified by execution (Python 3.10, 2026-09-26): `stabilize` on the fullest stable pile plus one grain at `(0,2)`, toppling the first unstable cell in the order of `cells_of(C)` each step, gives the listed sequences: 16 topplings and 2 grains absorbed in the sink model, and 4 topplings `(0,2), (0,1), (0,2), (1,1)` and 2 grains absorbed in the tide model, ending at the pinned piles.
[^2]: Verified by execution (Python 3.10, SymPy, 2026-09-26): `recurrent_count` (breadth-first search from the fullest stable pile, adding one grain at a time and stabilizing) finds 64 recurrent piles in the sink model and 27 in the tide model; the block matrices of `C` are `4I` and `3I` with Smith normal form factors `4, 4, 4` and `3, 3, 3`; `(2, 2, 2)` gives `15` and `8`, `(3, 3)` gives `11` under the tide, and `(2, 2, 1, 2, 2, 1, 2, 2)` gives `4, 4, 4` and `3, 3, 3`. The cospectral statement is the census result of [[sandpile-census](pages/sandpile-census.md)].
[^3]: Verified by execution (Python 3.10, SymPy, 2026-09-26): in the sink model the grain at `(0,2)` has order 4 (least common denominator of its column of `L̃⁻¹`), and over all 16 sink cells and 15 grain cells each, orders `1, 2, 4` occur `16, 48, 176` times; under the tide all 8 cells above the ground have order 3.
[^4]: Verified by execution (Python 3.10, 2026-09-26): identities by `stab(2m − stab(2m))` in both models, as pinned; one grain added at `(0,2)` to either identity causes one toppling; that the identities act as zero is checked for this construction on [[sandpile-identity](pages/sandpile-identity.md)].
[^5]: Verified by execution (Python 3.10, NumPy, 2026-09-26): exact means from the inverse reduced Laplacian (1.667 tide, 32.133 sink); 20,000 random drops from the identity with seed 2 give means 1.66 and 32.06 and largest avalanches 4 and 149; the column prediction `Σ (h−1)h(2h−1)/6 / Σ (h−1)` is 1.75.
