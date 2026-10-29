---
title: Sandcastles seminar - one castle, grain by grain, in the sink and tide models
category: Concepts
summary: A seminar following the 16-cell castle (3,2,1,2,2,1,2,3), silver by spectrum (castle-graph spectral radius 1 + √2), through its sandpile group, clock, identity and avalanches in the sink model (one sink cell, the bottom-left cell) and the tide model (the whole bottom row as the sink). One grain on the left tower of the fullest stable configuration causes 16 topplings in the sink model and 4 in the tide model, losing 2 grains to the sink in each. Its three separate 2×2 blocks give the block matrix 4I in the sink model and 3I in the tide model, since all three stand on the bottom row, so its groups are Z/4 × Z/4 × Z/4 (64 recurrent configurations) and Z/3 × Z/3 × Z/3 (27). Its clock ticks 4 in the sink model, with orders 1, 2, 4 occurring 16, 48, 176 times over all 240 (sink, grain) pairs, and 3 in the tide model, on every one of its 8 raised cells. Both identities have empty tower tops. The mean avalanche is 1.667 topplings in the tide model (never more than 4 in 20,000 drops) and 32.133 in the sink model (up to 149).
tags: [concept, castle, seminar, pedagogy, teaching, sandpile, silver-ratio, critical-group, identity-element, clock, avalanche, sink-model, tide-model, isospectral]
sources: [project-euler-502-castle-factoring, rossin-2000-group-of-a-sandpile, dhar-ruelle-sen-verma-1995-algebraic-aspects, dhar-1990-self-organized-critical-sandpile, bak-tang-wiesenfeld-1988-self-organized-criticality]
created: 2026-09-26
updated: 2026-10-29
---

# Sandcastles seminar - one castle, grain by grain, in the sink and tide models

**Thesis.** Adding sand to a castle one grain at a time gives a finite group, a clock, an identity configuration, and avalanches. The castle's `2 × 2` blocks and the choice of sink determine all four. With one sink cell or with the whole bottom row as the sink, the same castle has two sets of invariants. This seminar follows one castle through both.

**Structure.** Seven stops, 0 to 6. The Snippet at the end computes every value quoted. The pages behind the stops are [[sandpile-group](pages/sandpile-group.md)], [[sandpile-census](pages/sandpile-census.md)], [[sandcastle-clock](pages/sandcastle-clock.md)], [[sandpile-identity](pages/sandpile-identity.md)] and [[castle-avalanches](pages/castle-avalanches.md)], each of which treats both models.

## Stop 0 - the castle, and the two models

```
#......#
##.##.##          (3, 2, 1, 2, 2, 1, 2, 3):  16 cells, three separate 2×2 blocks, all on the bottom row
########
```

The castle graph has spectral radius `1 + √2`, like the rectangle `(2, 2, 2)`, so both castles are silver by spectrum ([[castle-graph-spectral-radius](pages/castle-graph-spectral-radius.md)]). The castle is its own mirror image, so "the leftmost apex" and "the rightmost apex" are mirror cells.

The two models ([[sandpile-group](pages/sandpile-group.md)], Part 1):

| | sink model | tide model |
|---|---|---|
| the sink | one cell, the bottom-left cell, drawn `S` | the whole bottom row, drawn `~` |
| the graph behind the model | the castle graph | the castle graph with the bottom row merged into one vertex |
| the cells outside the sink | one connected set | three runs of raised columns, `(3, 2)`, `(2, 2)` and `(2, 3)`, with no edges between them |

*Idea:* the choice of sink fixes the graph on which every invariant of Stops 1 to 6 is computed.

## Stop 1 - the game

A cell topples when it holds at least as many grains as it has neighbors, and sends one grain to each neighbor; grains sent to the sink vanish ([[sandpile-group](pages/sandpile-group.md)]). A tower top has one neighbor, so one grain there topples at once.

Start from the fullest stable configuration, every cell one grain short of toppling, and drop one grain on the top of the left tower, `(0, 2)`. Each step topples the first unstable cell in the order of the Snippet's `cells_of`.

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

One grain causes **16 topplings**, which cross the whole castle and end at the top of the right tower. Two grains enter the sink, from its neighbors `(0,1)` and `(1,0)`.[^1]

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

The same grain causes **4 topplings**, all in the left run. Two grains enter the sink again, from the cells `(0,1)` and `(1,1)` of row 1.[^1]

*Idea:* the same grain causes 16 topplings in the sink model and 4 in the tide model.

## Stop 2 - the sand forms a group

The **recurrent** configurations are the stable configurations that recur as grains are added. With "add, then stabilize" they form the **sandpile group**, whose order is the number of spanning trees of the graph behind the model.

The group can be read off the `2 × 2` blocks ([[sandpile-group](pages/sandpile-group.md)], Part 3): it is `Z^r` modulo the **block matrix**, with one row per block, `−1` for each pair of blocks sharing an edge, and on the diagonal `4` in the sink model; in the tide model the diagonal is `3` for a block on the bottom row and `4` for a block above it. This castle's three blocks are separate and all on the bottom row:

```
sink model                          tide model
[4 0 0]                             [3 0 0]
[0 4 0]   →  Z/4 × Z/4 × Z/4        [0 3 0]   →  Z/3 × Z/3 × Z/3
[0 0 4]      64 recurrent           [0 0 3]      27 recurrent
```

The rectangle `(2, 2, 2)` has two blocks sharing an edge, and its block matrices `[[4, −1], [−1, 4]]` and `[[3, −1], [−1, 3]]` give `Z/15` in the sink model and `Z/8` in the tide model.[^2]

*Idea:* separate blocks give a direct product of groups, and blocks sharing edges give one group for the cluster. A path of blocks gives a cyclic group in both models ([[sandpile-census](pages/sandpile-census.md)]); other clusters can split, differently in the two models: the `2 × 2` square of blocks `(3, 3, 3)` has `Z/8 × Z/24` in the sink model and `Z/95` in the tide model.

## Stop 3 - what each group separates

**Sink model.** The sink block matrix depends only on which blocks share edges. So every castle with three separate blocks has the sink group `Z/4 × Z/4 × Z/4`, the 14-cell castle `(2, 2, 1, 2, 2, 1, 2, 2)` among them. Across all castles with at most 16 cells, castles with the same adjacency or Laplacian spectrum always have the same sink group ([[sandpile-census](pages/sandpile-census.md)]).

**Tide model.** The tide block matrix also records which blocks stand on the bottom row. `(2, 2, 1, 2, 2, 1, 2, 2)` still has the tide group `Z/3 × Z/3 × Z/3`, but the rectangle `(2, 2, 2)` and `(3, 3)`, the same graph lying down and standing up, have the sink group `Z/15` in both cases and the tide groups `Z/8` and `Z/11`. The tide group does not change when a run of raised columns slides along the bottom row or two runs swap.[^2]

*Idea:* the sink group is a graph invariant and cannot separate two castles with the same graph; the tide group depends on how the castle stands on the bottom row and can.

## Stop 4 - the clock

Start at the **identity** (Stop 5) and drop one grain on the top of the left tower every tick. The configuration returns to the identity after a number of ticks, the **clock period**, which is the order of one grain at the apex in the group ([[sandcastle-clock](pages/sandcastle-clock.md)]).

| | sink model | tide model |
|---|---|---|
| clock period | **4**, the largest order in `Z/4 × Z/4 × Z/4` | **3**, the largest order in `Z/3 × Z/3 × Z/3` |
| clock spectrum | over every sink cell and grain cell (240 pairs): orders `1, 2, 4` occur `16, 48, 176` times | over every cell above the bottom row (8 cells): order `3` every time |
| what it depends on | the clock spectrum depends only on the castle graph; the fixed-sink period depends on the sink cell | the castle's runs of raised columns |

The sink clock spectrum separates 62 of the 105 adjacency-cospectral groups of castles to 16 cells, where the sink group separates none. In the tide model every raised cell of this castle has order 3: each block is a `Z/3`, and by the branch lemma of [[sandcastle-clock](pages/sandcastle-clock.md)] a grain on a tower equals a grain on the block cell below it.[^3]

*Idea:* the clock period is the order of a group element.

## Stop 5 - the identity

The identity is the recurrent configuration that acts as zero: added to any recurrent configuration and stabilized, it returns that configuration. It is `stab(2m − stab(2m))`, where `m` is the fullest stable configuration ([[sandpile-identity](pages/sandpile-identity.md)]):

```
sink model (sink S)              tide model (sink ~)
0......0                         0......0
11.10.12                         11.11.11
S2122121                         ~~~~~~~~
```

Both have empty tower tops: a tower top has one neighbor, so it is stable only when empty. In the tide model the identity has one grain on every cell of row 1; in the sink model it varies from cell to cell. One grain dropped on the apex of either identity causes one toppling.[^4]

## Stop 6 - avalanches

Now drop grains on **random** cells, starting from the identity. By Dhar's theorem the mean avalanche size is the sum of the entries of the inverse reduced Laplacian divided by the number of cells outside the sink ([[castle-avalanches](pages/castle-avalanches.md)]).

| model | mean topplings per grain (exact) | simulated mean (20,000 drops) | largest avalanche |
|---|---|---|---|
| tide (bottom row) | 1.667 | 1.66 | 4 |
| sink (bottom-left cell) | 32.133 | 32.06 | 149 |

The castle has height 3, so in the tide model every raised cell is at most two cells from the sink. The sink-model mean is about 19 times the tide-model mean. The tide mean, 1.667, is below this castle's column prediction of 1.75, the mean of `j(2h − 1 − j)/2` over the raised cells of each column taken separately. On [[castle-avalanches](pages/castle-avalanches.md)], every castle with at most 12 cells has tide mean at most its column prediction, with equality exactly when every run of raised columns has constant height; here the outer runs `(3, 2)` and `(2, 3)` do not.[^5]

*Idea:* with one sink cell the mean avalanche of this castle is about 19 times its tide-model value.

## Summary table

| stop | measurement | sink model | tide model |
|---|---|---|---|
| 1 | one grain on the fullest stable configuration | 16 topplings, 2 grains lost | 4 topplings, 2 grains lost |
| 2 | recurrent configurations, group | 64, `Z/4 × Z/4 × Z/4` from `4I` | 27, `Z/3 × Z/3 × Z/3` from `3I` |
| 3 | what the group records | which blocks share edges | which blocks share edges, and which stand on the bottom row |
| 4 | clock, clock spectrum | 4; orders `1, 2, 4` × `16, 48, 176` | 3; order `3` on all 8 raised cells |
| 5 | identity | empty tower tops, uneven | empty tower tops, one grain on every cell of row 1 |
| 6 | mean avalanche, largest | 32.133, 149 | 1.667, 4 |

The rectangle `(2, 2, 2)` has the same spectral radius as this castle and different sandpile invariants in both models: its two blocks share an edge and give `Z/15` (sink) and `Z/8` (tide), its clocks tick 15 and 8, and it has no towers.

## Snippet

```python
import numpy as np, sympy as sp, random
from math import lcm
from collections import Counter
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ

C = (3, 2, 1, 2, 2, 1, 2, 3)                # the castle of this seminar

def cells_of(c):
    return [(i, j) for i, h in enumerate(c) for j in range(h)]

def board(c, sinks):                       # sand-holding cells, their non-sink neighbors, full degrees
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

## Exercises

1. In the sink-model trace of Stop 1, the topplings reach the middle block only through `(2,0)`. Why is that cell the only link, and why is there no such link in the tide model?
2. Write down the block matrix of `(3, 3, 3)`, a `2 × 2` square of blocks, in both models, and check that the groups are `Z/8 × Z/24` (sink) and `Z/95` (tide).
3. Show that every tower top holds 0 grains in every stable configuration, in both models.
4. Find a castle whose tide mean equals its column prediction and one where it falls short. Which runs of columns decide it?
5. Why does every raised cell of this castle have order 3 in the tide model? Find a castle with two raised cells of different orders in the tide model.

## Appearances in Sources

- [[bak-tang-wiesenfeld-1988-self-organized-criticality](pages/bak-tang-wiesenfeld-1988-self-organized-criticality.md)] - the random-dropping experiment of Stop 6.
- [[dhar-1990-self-organized-critical-sandpile](pages/dhar-1990-self-organized-critical-sandpile.md)] - the abelian property, the group of `det L̃` recurrent configurations, and the mean avalanche from `G = L̃⁻¹`.
- [[dhar-ruelle-sen-verma-1995-algebraic-aspects](pages/dhar-ruelle-sen-verma-1995-algebraic-aspects.md)] - the group as `Z^n` modulo the toppling matrix, with `|K| = det Δ`, behind Stops 2 to 4.
- [[rossin-2000-group-of-a-sandpile](pages/rossin-2000-group-of-a-sandpile.md)] - the sandpile group, its independence of the sink cell, and the identity recipe of Stop 5.
- [[project-euler-502-castle-factoring](pages/project-euler-502-castle-factoring.md)] - the castle definition behind the castle graph.

## Related Concepts

- [[sandpile-group](pages/sandpile-group.md)] - the sandpile, the two models, the matrices, and the block matrix with its tide diagonal (Stops 0 to 2).
- [[sandpile-census](pages/sandpile-census.md)] - the groups of every castle to 16 cells in both models, and what each separates (Stop 3).
- [[sandcastle-clock](pages/sandcastle-clock.md)] - the clock, the clock spectrum and the branch lemma (Stop 4).
- [[sandpile-identity](pages/sandpile-identity.md)] - the identity and the avalanche profiles (Stop 5).
- [[castle-avalanches](pages/castle-avalanches.md)] - random dropping, Dhar's theorem, and the tide inequality (Stop 6).
- [[castle-graph-spectral-radius](pages/castle-graph-spectral-radius.md)] - the castles silver by spectrum, this one among them.
- [[hear-the-shape-seminar](pages/hear-the-shape-seminar.md)], [[one-bit-seminar](pages/one-bit-seminar.md)], [[hardin-identity-seminar](pages/hardin-identity-seminar.md)], [[oeis-mining-seminar](pages/oeis-mining-seminar.md)], [[castle-fibers-char-2-walkthrough](pages/castle-fibers-char-2-walkthrough.md)], [[tower-recursion-master-class](pages/tower-recursion-master-class.md)], [[q-thread-seminar](pages/q-thread-seminar.md)], [[half-derivative-seminar](pages/half-derivative-seminar.md)], [[pell-castle-strip](pages/pell-castle-strip.md)], [[castle-cryptography](pages/castle-cryptography.md)], [[song-as-castle](pages/song-as-castle.md)] - the other seminar pages.

## Footnotes

[^1]: Verified by execution (Python 3.11, 2026-10-16): `stabilize` on the fullest stable configuration plus one grain at `(0,2)`, toppling the first unstable cell in the order of `cells_of(C)` at each step, gives the listed sequences: 16 topplings and 2 grains into the sink in the sink model; 4 topplings `(0,2), (0,1), (0,2), (1,1)` and 2 grains into the sink in the tide model; the final configurations are as pinned.
[^2]: Verified by execution (Python 3.11, SymPy, 2026-10-16): `recurrent_count` (breadth-first search from the fullest stable configuration, adding one grain at a time and stabilizing) finds 64 recurrent configurations in the sink model and 27 in the tide model; the block matrices of `C` are `4I` and `3I` with Smith normal form factors `4, 4, 4` and `3, 3, 3`; `(2, 2, 2)` gives `15` and `8`, `(3, 3)` gives `15` and `11`, `(2, 2, 1, 2, 2, 1, 2, 2)` gives `4, 4, 4` and `3, 3, 3`, and `(3, 3, 3)` gives `8, 24` and `95`. The cospectral statement is the census result of [[sandpile-census](pages/sandpile-census.md)].
[^3]: Verified by execution (Python 3.11, SymPy, 2026-10-16): in the sink model the grain at `(0,2)` has order 4 (the least common denominator of its column of `L̃⁻¹`), and over all 16 sink cells and 15 grain cells each, orders `1, 2, 4` occur `16, 48, 176` times; in the tide model all 8 cells above the bottom row have order 3. The castle graph's characteristic polynomial is divisible by `x² − 2x − 1` and has largest root `1 + √2`.
[^4]: Verified by execution (Python 3.11, 2026-10-16): identities by `stab(2m − stab(2m))` in both models, as pinned; one grain added at `(0,2)` to either identity causes one toppling; that these identities act as zero is checked on [[sandpile-identity](pages/sandpile-identity.md)].
[^5]: Verified by execution (Python 3.11, NumPy, 2026-10-16): exact means from the inverse reduced Laplacian (1.667 tide, 32.133 sink); 20,000 random drops from the identity with seed 2 give means 1.66 and 32.06 and largest avalanches 4 and 149; the column prediction `Σ (h−1)h(2h−1)/6 / Σ (h−1)` is 1.75.
