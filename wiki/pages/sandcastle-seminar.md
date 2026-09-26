---
title: Sandcastles seminar - one silver castle, grain by grain
category: Concepts
summary: The seminar walk-through for the "Sandcastles" arc, following one castle, the 16-cell silver castle (3,2,1,2,2,1,2,3), through the whole sandpile story. One grain on its left tower sets off a 16-toppling avalanche that sweeps the castle left to right and loses 2 grains to the drain. Its 64 recurrent piles form the group Z/4 × Z/4 × Z/4, read straight off its three separate 2×2 blocks (the silver rectangle's two touching blocks give Z/15 instead), and any castle with three separate blocks has the same group, which is why the sandpile group hears nothing the spectrum misses. Its clock ticks 4, with a clock spectrum of periods 1, 2, 4 occurring 16, 48, 176 times. Its identity, in both drain models, has empty tower tops (tree branches are transparent). Under the tide it barely avalanches (mean 1.667 topplings, never more than 4); with a single drain cell the mean is 32.1 and avalanches reach 149. One runnable block pins every value.
tags: [concept, castle, seminar, pedagogy, teaching, sandpile, silver-ratio, critical-group, identity-element, clock, avalanche, tide, isospectral]
sources: [project-euler-502-castle-factoring]
created: 2026-09-26
updated: 2026-09-26
---

# Sandcastles seminar - one silver castle, grain by grain

**Thesis.** Pour sand on a castle, one grain at a time, and a rich mathematical object appears: a finite group, a clock, an identity pile, and avalanches of every size. All of it is controlled by the castle's `2 × 2` blocks and by where the sand drains. This seminar follows a single castle through the whole story.

**The castle.**

```
#......#
##.##.##          (3, 2, 1, 2, 2, 1, 2, 3):  16 cells, three separate 2×2 blocks
########
```

It is a **silver castle**: the largest eigenvalue of its graph is `1 + √2`, the same as the `3 × 2` silver rectangle's ([[castle-graph-spectral-radius](pages/castle-graph-spectral-radius.md)]). It is also its own mirror image, so choices like "the leftmost apex" cause no ambiguity.

**Format.** About 60 minutes, seven stops. Every value quoted is pinned by the Snippet block at the end. The research pages behind the stops are [[sandpile-group](pages/sandpile-group.md)], [[sandpile-census](pages/sandpile-census.md)], [[sandcastle-clock](pages/sandcastle-clock.md)], [[sandpile-identity](pages/sandpile-identity.md)] and [[castle-avalanches](pages/castle-avalanches.md)].

## Stop 1 - the game

Each cell is a bowl whose capacity is its number of neighbours. A bowl that reaches capacity **topples**, sending one grain to each neighbour. A neighbour always accepts, even if it then topples too. Grains leave only through the **drain**, here the bottom-left cell. The tower tops have a single neighbour, so they hold nothing: one grain there topples at once.

Start from the fullest stable pile (every bowl one grain short) and drop one grain on the left tower's top:

```
                 top row    middle     bottom row
start            0......0   21.11.12   ~2122121
drop on (0,2)    1......0   21.11.12   ~2122121
topple (0,2)     0......0   31.11.12   ~2122121
topple (0,1)     1......0   02.11.12   ~2122121     <- one grain into the drain
topple (0,2)     0......0   12.11.12   ~2122121
topple (1,1)     0......0   20.11.12   ~3122121
topple (1,0)     0......0   21.11.12   ~0222121     <- another into the drain
topple (2,0)     0......0   21.11.12   ~1032121
topple (3,0)     0......0   21.21.12   ~1103121
topple (3,1)     0......0   21.02.12   ~1113121
topple (4,0)     0......0   21.03.12   ~1120221
topple (4,1)     0......0   21.11.12   ~1121221
topple (5,0)     0......0   21.11.12   ~1122031
topple (6,0)     0......0   21.11.22   ~1122102
topple (6,1)     0......0   21.11.03   ~1122112
topple (7,0)     0......0   21.11.04   ~1122120
topple (7,1)     0......1   21.11.11   ~1122121
topple (7,2)     0......0   21.11.12   ~1122121     settled
```

One grain, **16 topplings**, a wave that crosses the whole castle and ends on the far tower's top. Two grains leave through the drain, both from its neighbours `(0,1)` and `(1,0)`.[^1]

*Idea:* local rules, global effects. A grain's consequences depend on the whole pile.

## Stop 2 - the sand forms a group

Keep dropping grains. Some piles never come back; the ones that keep recurring are the **recurrent** piles, and this castle has exactly **64**. Adding two recurrent piles and toppling gives another, so they form a group, the **sandpile group**, of order 64: the castle's number of spanning trees.

Its structure can be read off the `2 × 2` blocks. For a castle, the group is `Z^r` modulo a small **block matrix**, one row per block, with `4` on the diagonal and `−1` for each pair of blocks sharing an edge ([[sandpile-group](pages/sandpile-group.md)], Part 3). This castle's three blocks are separate, so the block matrix is `4I`:

```
[4 0 0]
[0 4 0]      →      K  =  Z/4 × Z/4 × Z/4
[0 0 4]
```

Each separate block holds its own `Z/4` of sand. Compare the silver rectangle `(2, 2, 2)`, whose two blocks touch: its block matrix `[[4, −1], [−1, 4]]` gives one bigger cyclic group, `Z/15`.[^2]

*Idea:* the sand lives in the 2×2 blocks. Separate blocks multiply, and touching blocks merge into one larger cyclic factor.

## Stop 3 - what the group cannot hear

The block matrix depends only on how the blocks touch each other. So **any** castle with three separate blocks has the same group. `(2, 2, 1, 2, 2, 1, 2, 2)` has no towers and a different spectrum, yet its group is also `Z/4 × Z/4 × Z/4`.

That is also why the sandpile group separates no cospectral pair. Across every castle up to 16 cells, castles with the same spectrum always have the same block arrangement, so they always have the same group ([[sandpile-census](pages/sandpile-census.md)]). To hear more, we have to watch the sand move.[^2]

## Stop 4 - the clock

Start at the **identity** pile (Stop 5) and drop one grain on the left tower's top every tick. The pile returns to the identity after **4** ticks. That is the order of "one grain on the apex" in the group, the largest order any element of `Z/4 × Z/4 × Z/4` can have.

The period depends on which cell is the drain and where the grain lands. Recording it for every drain cell and every grain cell (240 pairs) gives the castle's **clock spectrum**: periods `1, 2, 4` occur `16, 48, 176` times. The clock spectrum depends only on the castle's graph, and unlike the group it separates many cospectral castles ([[sandcastle-clock](pages/sandcastle-clock.md)]).[^3]

*Idea:* an element of a finite group has an order, and an order is a clock.

## Stop 5 - the identity

The identity is the recurrent pile that acts like zero: add it to any recurrent pile, topple, and nothing changes. It is `stab(2m − stab(2m))`, where `m` is the fullest stable pile ([[sandpile-identity](pages/sandpile-identity.md)]):

```
one drain cell (bottom-left)     tide (whole bottom row)
0......0                         0......0
11.10.12                         11.11.11
~2122121                         ~~~~~~~~
```

Both have empty tower tops. A grain on a tower top can always topple down into the block below, so in the group it is the same as a grain on that block. Tree branches are transparent: the towers add shape but no sand. Under the tide the identity is almost trivially regular, and with a single drain it is irregular.[^4]

## Stop 6 - avalanches, and where the drain is

Now drop grains at **random** cells, starting from the identity. By Dhar's theorem the average avalanche size is exact: the average entry of the inverse Laplacian ([[castle-avalanches](pages/castle-avalanches.md)]).

| drain | mean topplings per grain (exact) | simulated mean (20,000 drops) | largest avalanche |
|---|---|---|---|
| tide (whole bottom row) | 1.667 | 1.66 | 4 |
| one cell (bottom-left) | 32.133 | 32.06 | 149 |

The castle is only 3 high, so under the tide sand reaches the ground almost at once, and nothing ever avalanches far. With a single drain every grain must cross the castle to escape, as in Stop 1, and the mean rises twentyfold. The tide mean, 1.667, is just below this castle's column-by-column prediction of 1.75, because its raised columns are not all the same height ([[castle-avalanches](pages/castle-avalanches.md)], the inequality).[^5]

*Idea:* the same castle can be calm or explosive depending on one modelling choice, where the sand leaves.

## Stop 7 - what the silver castle taught

| stop | measurement | value for `(3,2,1,2,2,1,2,3)` |
|---|---|---|
| 1 | one grain on the full pile | 16 topplings, 2 grains lost |
| 2 | recurrent piles, group | 64, `Z/4 × Z/4 × Z/4` from `4I` |
| 3 | group of any castle with three separate blocks | the same `Z/4 × Z/4 × Z/4` |
| 4 | clock, clock spectrum | 4; periods `1, 2, 4` × `16, 48, 176` |
| 5 | identity | tower tops empty, in both drain models |
| 6 | mean avalanche, tide vs one drain | 1.667 vs 32.133 |

The silver rectangle `(2, 2, 2)` shares this castle's spectral radius but not its sand. Its two blocks touch and give `Z/15`, its clock ticks 15, and it has no towers. Same "silver" loudest note, different sandcastle.

## Exercises for the room

1. In the Stop 1 trace, the wave reaches the middle block only through `(2,0)`. Why is that cell the only link, and which cell plays the same role between the middle and right blocks?
2. Write down the block matrix of `(3, 3, 3)`, a `2 × 2` square of blocks, and check that its group is `Z/8 × Z/24`.
3. Explain why every tower top holds 0 grains in every recurrent pile.
4. Find a castle whose tide mean equals its column prediction and one where it falls short. Which runs of columns decide it?
5. (Open.) Is the avalanche profile of [[sandpile-identity](pages/sandpile-identity.md)] a complete fingerprint of castle graphs?

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

def board(c, drains):                      # sand-holding cells, their non-drain neighbours, full degrees
    S = set(cells_of(c))
    around = lambda v: [u for u in ((v[0]+1, v[1]), (v[0]-1, v[1]), (v[0], v[1]+1), (v[0], v[1]-1)) if u in S]
    live = [v for v in cells_of(c) if v not in drains]
    return live, {v: [u for u in around(v) if u not in drains] for v in live}, {v: len(around(v)) for v in live}

ONE_CELL, TIDE = {(0, 0)}, {(i, 0) for i in range(len(C))}

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

def draw(c, g):                            # top row first; drains '~'
    return [''.join('.' if j >= h else str(g[(i, j)]) if (i, j) in g else '~' for i, h in enumerate(c))
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

def block_matrix(c):                       # one row per 2x2 block: 4 on the diagonal, -1 for blocks sharing an edge
    B = [(i, j) for i in range(len(c) - 1) for j in range(min(c[i], c[i+1]) - 1)]
    return sp.Matrix(len(B), len(B), lambda a, b: 4 if a == b else
                     -1 if abs(B[a][0] - B[b][0]) + abs(B[a][1] - B[b][1]) == 1 else 0)

def group(M):                              # nontrivial invariant factors of Z^r / M
    S = smith_normal_form(M, domain=ZZ)
    return [abs(S[i, i]) for i in range(M.rows) if abs(S[i, i]) != 1]

def reduced_laplacian(b):
    live, nb, deg = b
    pos = {v: k for k, v in enumerate(live)}
    return sp.Matrix(len(live), len(live), lambda r, s: deg[live[r]] if r == s else -(live[s] in nb[live[r]]))

def grain_orders(c, drain):                # order of one grain at each cell: lcm of denominators of a column of L~^-1
    b = board(c, {drain}); Linv = reduced_laplacian(b).inv()
    return {v: lcm(*[sp.fraction(x)[1] for x in Linv[:, k]]) for k, v in enumerate(b[0])}

def mean_avalanche(b):                     # Dhar: average of all entries of L~^-1, per drop cell
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
>>> b = board(C, ONE_CELL); live, nb, deg = b
>>> full = {v: deg[v] - 1 for v in live}; full[(0, 2)] += 1
>>> settled, n, lost, steps = stabilize(b, full, trace=True)
>>> n, lost, draw(C, settled)
(16, 2, ['0......0', '21.11.12', '~1122121'])
>>> recurrent_count(b), block_matrix(C), group(block_matrix(C))
(64, Matrix([
[4, 0, 0],
[0, 4, 0],
[0, 0, 4]]), [4, 4, 4])
>>> group(block_matrix((2, 2, 2))), group(block_matrix((2, 2, 1, 2, 2, 1, 2, 2)))
([15], [4, 4, 4])
>>> draw(C, identity(b)), draw(C, identity(board(C, TIDE)))
(['0......0', '11.10.12', '~2122121'], ['0......0', '11.11.11', '~~~~~~~~'])
>>> grain_orders(C, (0, 0))[(0, 2)], sorted(Counter(t for d in cells_of(C) for t in grain_orders(C, d).values()).items())
(4, [(1, 16), (2, 48), (4, 176)])
>>> round(float(mean_avalanche(board(C, TIDE))), 3), round(float(mean_avalanche(board(C, ONE_CELL))), 3)
(1.667, 32.133)
>>> tide, one = random_drops(board(C, TIDE), 20000), random_drops(board(C, ONE_CELL), 20000)
>>> round(float(tide.mean()), 2), int(tide.max()), round(float(one.mean()), 2), int(one.max())
(1.66, 4, 32.06, 149)
```

## Related Concepts

- [[sandpile-group](pages/sandpile-group.md)] - the game, the matrices, and the 2×2-block picture (Stops 1-2).
- [[sandpile-census](pages/sandpile-census.md)] - every castle's group, and why it separates no cospectral pair (Stop 3).
- [[sandcastle-clock](pages/sandcastle-clock.md)] - the clock and the clock spectrum (Stop 4).
- [[sandpile-identity](pages/sandpile-identity.md)] - the identity and the avalanche profile (Stop 5).
- [[castle-avalanches](pages/castle-avalanches.md)] - random dropping, Dhar's theorem, and the tide inequality (Stop 6).
- [[castle-graph-spectral-radius](pages/castle-graph-spectral-radius.md)] - the silver castles.
- [[hear-the-shape-seminar](pages/hear-the-shape-seminar.md)] / [[one-bit-seminar](pages/one-bit-seminar.md)] / [[hardin-identity-seminar](pages/hardin-identity-seminar.md)] / [[oeis-mining-seminar](pages/oeis-mining-seminar.md)] / [[castle-fibers-char-2-walkthrough](pages/castle-fibers-char-2-walkthrough.md)] / [[tower-recursion-master-class](pages/tower-recursion-master-class.md)] - the other seminar pages.

## Appearances in Sources

- [[project-euler-502-castle-factoring](pages/project-euler-502-castle-factoring.md)] - the castle definition behind the castle graph.

## Footnotes

[^1]: Verified by execution (Python 3.10, 2026-09-26): `stabilize` on the fullest stable pile plus one grain at `(0,2)`, toppling the first unstable cell in the order of `cells_of(C)` each step, gives the listed sequence of 16 topplings and 2 grains absorbed, ending at the pinned pile.
[^2]: Verified by execution (Python 3.10, SymPy, 2026-09-26): `recurrent_count` (breadth-first search from the fullest stable pile, adding one grain at a time and stabilizing) finds 64 recurrent piles; the block matrix of `C` is `4I` with Smith normal form factors `4, 4, 4`; `(2, 2, 2)` gives `15` and `(2, 2, 1, 2, 2, 1, 2, 2)` gives `4, 4, 4`. The cospectral statement is the census result of [[sandpile-census](pages/sandpile-census.md)].
[^3]: Verified by execution (Python 3.10, SymPy, 2026-09-26): with the bottom-left drain the grain at `(0,2)` has order 4 (least common denominator of its column of `L̃⁻¹`); over all 16 drain cells and 15 grain cells each, orders `1, 2, 4` occur `16, 48, 176` times.
[^4]: Verified by execution (Python 3.10, 2026-09-26): identities by `stab(2m − stab(2m))` in both drain models, as pinned; that they act as zero is checked for this construction on [[sandpile-identity](pages/sandpile-identity.md)].
[^5]: Verified by execution (Python 3.10, NumPy, 2026-09-26): exact means from the inverse reduced Laplacian (1.667 tide, 32.133 one drain); 20,000 random drops from the identity with seed 2 give means 1.66 and 32.06 and largest avalanches 4 and 149; the column prediction `Σ (h−1)h(2h−1)/6 / Σ (h−1)` is 1.75.
