---
title: Avalanches on castles - Bak-Tang-Wiesenfeld sand, ground as the drain
category: Analyses
summary: The original self-organized-criticality sandpile (Bak, Tang and Wiesenfeld, 1987) run on castles, with the bottom row as the drain (the tide), starting from the identity and dropping grains on random cells. Dhar's theorem makes the mean avalanche size exact - the average of the solution of L̃x = 1 - and simulation agrees to within 0.3% on every shape tested. The mean depends only on height for rectangles and battlements - exactly h(2h−1)/6, the value for a single column - so a 10×10 rectangle full of 2×2 blocks and a battlement with none both average 31.67 topplings per grain. For every castle up to 12 cells (2,130 castles), the mean is at most the column-by-column prediction, with equality exactly when every run of adjacent columns rising above the base has constant height. What the 2×2 blocks change is the tail: a 20×20 rectangle and a battlement of height-20 spikes both average about 130 topplings, but the rectangle's largest avalanches reach 3,701 topplings and 601 rounds with a size density falling like s^(−0.93), while the battlement never exceeds 190. The drain matters too: with a single drain cell a 10×10 square averages 129.9 topplings, four times the tide's 31.7.
tags: [analysis, castle, sandpile, avalanche, self-organized-criticality, bak-tang-wiesenfeld, dhar, green-function, laplacian, tide, battlement, rectangle, heavy-tail, numpy, simulation, verification]
sources: [project-euler-502-castle-factoring]
created: 2026-09-26
updated: 2026-09-26
---

# Avalanches on castles - Bak-Tang-Wiesenfeld sand, ground as the drain

## The experiment

In 1987 Bak, Tang and Wiesenfeld dropped sand, one grain at a time, on random cells of a large grid, using the toppling rule of [[sandpile-group](pages/sandpile-group.md)]. They found that the pile organizes itself into a critical state: most grains cause no avalanche or a small one, but avalanches of every size occur, with a size distribution close to a power law. They called this **self-organized criticality**.[^1]

Here the grid is a castle. The drain is the **tide**, the whole bottom row, so sand leaves only through the ground ([[sandpile-group](pages/sandpile-group.md)], the tide variant). The pile starts at its identity ([[sandpile-identity](pages/sandpile-identity.md)]), which is already recurrent, so no warm-up is needed. Each drop lands on a uniformly random cell above the ground, and the page records two numbers for each avalanche:

- its **size**, the number of topplings it causes;
- its **duration**, the number of rounds, where one round topples everything that is unstable at once.

The item on `IDEAS.md` asked how ladders, rectangles and battlements compare, and whether the block count or the number of `2 × 2` blocks sets the largest avalanches.

## The mean avalanche is exact

A theorem of Dhar makes the average avalanche size computable without simulation. In the long run, the expected number of topplings at cell `u` caused by a grain dropped at cell `v` is the `(v, u)` entry of `L̃⁻¹`, the inverse of the Laplacian with the drain removed.[^2] Averaging over a uniformly random drop cell,

```
mean avalanche size  =  (1/n) · (sum of all entries of L̃⁻¹)  =  average of x,  where  L̃ x = 1
```

Simulation agrees with this to within 0.3% on every shape tested: 20,000 random drops each on ladders, rectangles up to `20 × 20` and battlements.[^3]

## Height alone sets the mean for rectangles and battlements

For a `w × h` rectangle, and for a **battlement** of height-`h` spikes separated by single cells, the mean avalanche is

```
mean  =  h (2h − 1) / 6
```

for every width. That is exactly the value for a single column of height `h`: 1 for ladders (`h = 2`), 2.5 at `h = 3`, 11 at `h = 6`, 31.67 at `h = 10`, 130 at `h = 20`.[^4]

**Why.** In a rectangle every column looks the same, so the solution `x` of `L̃x = 1` depends only on the row. The sideways terms then cancel, and what remains is the equation for one vertical path hanging from the ground. Its solution is `x(j) = j(2h − 1 − j)/2` at height `j`, and its average over `j = 1 … h − 1` is `h(2h − 1)/6`. A battlement is the same path repeated, because its spikes never touch above the ground. So a `10 × 10` rectangle, packed with `2 × 2` blocks, and a battlement of height-10 spikes, with none, have the **same mean avalanche**.

**General castles.** Joining columns of different heights lowers the mean. For every castle with at most 12 cells (2,130 castles), the mean is **at most** the column-by-column prediction (each column treated as its own path), with equality **exactly** when every run of adjacent columns rising above the base has constant height.[^5] For example, `(3, 5, 2, 2, 6, 4)` averages 5.77 topplings against a column prediction of 6.63.

## The 2×2 blocks change the tail, not the mean

Two castles with the same mean can avalanche completely differently. From 60,000 random drops each:[^6]

| | 20×20 rectangle | battlement of height-20 spikes |
|---|---|---|
| mean size | 130.3 | 130.4 |
| median size (drops that topple) | 47 | 145 |
| 99th percentile | 2,408 | 190 |
| largest avalanche | 3,701 | 190 |
| drops with size `≥ 200` | 15.5% | none |
| longest duration (rounds) | 601 | 37 |
| log-log slope of the size density on `[10, 1000]` | about `−0.93` | flat |

In the battlement each spike is a separate path, so an avalanche can never be bigger than one spike's worth. The largest observed are 45, 66 and 190 topplings at heights 10, 12 and 20, which is `(h − 1)h/2`. In the rectangle the `2 × 2` blocks tie the columns together, so sand spreads sideways and the largest avalanches grow with the rectangle's area: 447 at `10 × 10`, over 3,500 at `20 × 20`. The size density looks like a power law over two decades, the Bak-Tang-Wiesenfeld signature. These castles are small, though, and the slope is an estimate over a finite range, not an exponent.

**Answer to the `IDEAS.md` question.** Neither the block count nor the `2 × 2` count sets the *mean*: height does. The `2 × 2` count (more exactly, how the columns are joined above the base) sets the *tail* and the size of the largest avalanches.

## Where the drain is matters

With a single drain cell (bottom-left) instead of the tide, sand has only one way out. A `10 × 10` square then averages **129.9** topplings per grain, four times the tide's **31.7**.[^7]

## What this settles and what it opens

**Settled.**
- The mean avalanche size is exact (Dhar), and simulation confirms it.
- Under the tide, rectangles and battlements have mean `h(2h − 1)/6`, depending on height alone.
- Every castle to 12 cells has mean at most its column prediction, with equality exactly when each run of raised columns has constant height.
- The `2 × 2` blocks set the tail, not the mean. Same-mean castles can differ by a factor of 20 in their largest avalanche.

**Open.**
- Prove the inequality and its equality case for all castles.
- How the rectangle's largest avalanche and tail slope scale with width and height, and whether a genuine exponent emerges for large castles with the drain only at the bottom. The classic results assume drains on all four sides.
- Avalanche statistics with a single drain cell, and whether duration and size are related by a power law here.
- Arc 14's seminar walk-through, built on this page and the other sandpile pages, is [[sandcastle-seminar](pages/sandcastle-seminar.md)].

## Snippet

```python
import numpy as np, random

def tide_board(c):                         # cells above the bottom row; the bottom row is the drain
    cells = [(i, j) for i, h in enumerate(c) for j in range(h)]
    S = set(cells)
    live = [v for v in cells if v[1] > 0]
    idx = {v: k for k, v in enumerate(live)}
    around = lambda v: ((v[0]+1, v[1]), (v[0]-1, v[1]), (v[0], v[1]+1), (v[0], v[1]-1))
    deg = np.array([sum(u in S for u in around(v)) for v in live])
    nb = [[idx[u] for u in around(v) if u in idx] for v in live]
    return live, deg, nb

def mean_avalanche_exact(c):               # Dhar: average over drop cells of the row sums of L~^-1
    live, deg, nb = tide_board(c)
    L = np.diag(deg.astype(float))
    for k, ns in enumerate(nb):
        for u in ns:
            L[k, u] -= 1
    return np.linalg.inv(L).sum() / len(live)

def column_prediction(c):                  # each column on its own: a path of height h averages h(2h-1)/6
    cells = sum(h - 1 for h in c)
    return sum((h - 1) * h * (2 * h - 1) / 6 for h in c) / cells

def topple(g, deg, nb, start):             # one avalanche: returns (topplings, rounds)
    size, rounds, frontier = 0, 0, [start]
    while frontier:
        rounds += 1; nxt = []
        for x in frontier:
            if g[x] >= deg[x]:
                q = g[x] // deg[x]; g[x] -= q * deg[x]; size += q
                for u in nb[x]:
                    g[u] += q
                    if g[u] >= deg[u]:
                        nxt.append(u)
        frontier = list(set(nxt))
    return size, rounds

def identity(deg, nb):                     # stab(2m - stab(2m)), m = the fullest stable pile
    def stab(g):
        g = g.copy()
        for v in range(len(g)):
            topple(g, deg, nb, v)
        while any(g[v] >= deg[v] for v in range(len(g))):
            for v in range(len(g)):
                topple(g, deg, nb, v)
        return g
    m = deg - 1
    return stab(2 * m - stab(2 * m))

def drop_sand(c, drops, seed=1):           # start at the identity, drop grains at random cells
    live, deg, nb = tide_board(c)
    g, rng, out = identity(deg, nb), random.Random(seed), []
    for _ in range(drops):
        v = rng.randrange(len(live)); g[v] += 1
        out.append(topple(g, deg, nb, v))
    return np.array(out)
```

```
>>> [round(float(mean_avalanche_exact((h,) * 8)), 3) for h in (2, 3, 6, 10)], [round(h * (2*h - 1) / 6, 3) for h in (2, 3, 6, 10)]
([1.0, 2.5, 11.0, 31.667], [1.0, 2.5, 11.0, 31.667])
>>> round(float(mean_avalanche_exact((1, 10) * 5)), 3)
31.667
>>> c = (3, 5, 2, 2, 6, 4)
>>> round(float(mean_avalanche_exact(c)), 3), round(column_prediction(c), 3)
(5.767, 6.625)
>>> rect, batt = drop_sand((12,) * 12, 20000), drop_sand((1, 12) * 6, 20000)
>>> round(float(rect[:, 0].mean()), 1), round(float(batt[:, 0].mean()), 1), round(12 * 23 / 6, 1)
(45.8, 46.0, 46.0)
>>> int(rect[:, 0].max()), int(batt[:, 0].max()), int(rect[:, 1].max()), int(batt[:, 1].max())
(754, 66, 193, 21)
```

The `12 × 12` rectangle and the battlement of height-12 spikes both average about 46 topplings (exact: `12·23/6 = 46`). The rectangle's largest avalanche is 754 topplings over 193 rounds, the battlement's 66 over 21.

## Related Concepts

- [[sandpile-group](pages/sandpile-group.md)] - the game, the toppling rule, and the tide variant.
- [[sandpile-identity](pages/sandpile-identity.md)] - the identity the dropping starts from, and the single-grain avalanche profile.
- [[sandcastle-clock](pages/sandcastle-clock.md)] - dropping always on the same cell instead of at random.
- [[sandpile-census](pages/sandpile-census.md)] - the sandpile group of every castle to 16 cells.
- [[castle-graph](pages/castle-graph.md)] - tree castles and battlements, and the `2 × 2` blocks that tie columns together.
- [[sandcastle-seminar](pages/sandcastle-seminar.md)] - the Sandcastles seminar, following the 16-cell silver castle `(3,2,1,2,2,1,2,3)` through the whole sandpile story.


## Appearances in Sources

- [[project-euler-502-castle-factoring](pages/project-euler-502-castle-factoring.md)] - the castle definition behind the castle graph.

## Footnotes

[^1]: P. Bak, C. Tang and K. Wiesenfeld, "Self-organized criticality: An explanation of the 1/f noise", Physical Review Letters 59 (1987) 381; summarized at https://en.wikipedia.org/wiki/Abelian_sandpile_model (the Bak-Tang-Wiesenfeld model, random grain addition, and power-law avalanche statistics on large grids).
[^2]: D. Dhar, "Self-organized critical state of sandpile automaton models", Physical Review Letters 64 (1990) 1613: in the stationary state of the abelian sandpile, the expected number of topplings at site `j` caused by adding a grain at site `i` is `(Δ⁻¹)_{ij}`, the inverse of the reduced Laplacian. The statement is checked against simulation here in [^3].
[^3]: Verified by execution (Python 3.10, NumPy, 2026-09-26): 20,000 uniformly random drops starting from the tide identity on `(2,)*20`, `(10,)*10`, `(20,)*20`, `(1,10)*10`, `(3,)*20`, `(6,)*40` give simulated means 1.000, 31.571, 129.875, 31.584, 2.497, 11.002 against exact means 1.000, 31.667, 130.000, 31.667, 2.500, 11.000.
[^4]: Verified by execution (Python 3.10, NumPy, 2026-09-26): `mean_avalanche_exact` equals `h(2h − 1)/6` to `10⁻⁹` for every rectangle `(h,)*w` and every battlement `(1, h)*w` with `2 ≤ h ≤ 12`, `1 ≤ w ≤ 8`.
[^5]: Verified by execution (Python 3.10, NumPy, 2026-09-26): for all 2,130 mirror-distinct castles with at most 12 cells and height at least 2, `mean_avalanche_exact(c) ≤ column_prediction(c) + 10⁻⁹`, with equality (to `10⁻⁹`) in 1,129 cases, exactly those in which every maximal run of adjacent columns of height at least 2 has constant height.
[^6]: Verified by execution (Python 3.10, NumPy, 2026-09-26): 60,000 random drops (seed 5) from the tide identity of `(20,)*20` and `(1,20)*10`; median and 99th percentile over drops with size `> 0`; slope from a least-squares fit of log density against log size in 10 logarithmic bins on `[10, 1000]`. The battlement maxima 45, 66, 190 at heights 10, 12, 20 are from the runs of [^3], the Snippet and this footnote; the `10 × 10` rectangle maximum 447 is from [^3]. The `12 × 12` comparison is pinned in the Snippet.
[^7]: Verified by execution (Python 3.10, NumPy, 2026-09-26): the exact mean with the single bottom-left drain cell on `(10,)*10` is 129.9, against 31.7 for the tide.
