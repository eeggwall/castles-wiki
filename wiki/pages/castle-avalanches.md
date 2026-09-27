---
title: Avalanches on castles - Bak-Tang-Wiesenfeld sand in the sink and tide models
category: Analyses
summary: The original self-organized-criticality sandpile (Bak, Tang and Wiesenfeld, 1987) run on castles in both models of sandpile-group, starting from the identity and dropping grains on random cells - the tide model, where the whole bottom row is the sink, and the sink model, where the only sink is the bottom-left cell. Dhar's theorem makes the mean avalanche size exact in both (the average of the solution of L̃x = 1), and simulation agrees to within 0.3%. Under the tide the mean depends only on height for rectangles and battlements - exactly h(2h−1)/6, the value for a single column - so a 10×10 rectangle full of 2×2 blocks and a battlement with none both average 31.67 topplings per grain; for every castle up to 12 cells (2,130 castles) the tide mean is at most the column-by-column prediction, with equality exactly when every run of adjacent columns rising above the base has constant height; and the 2×2 blocks change only the tail (a 20×20 rectangle reaches 3,701 topplings with a size density falling like s^(−0.93), a battlement of height-20 spikes never exceeds 190). The sink model reverses this. A single column is the same in both models, but the sink-model mean grows with width as well as height (symmetric under turning a rectangle on its side), and the 2×2 blocks lower it by giving sand parallel routes to the corner: the 20×20 rectangle averages 692.0 topplings and the height-20 battlement 1,520.9, against 130 for both under the tide. The rectangle keeps a heavy tail (largest 21,248, slope about −0.98 on [10, 1000]); the battlement has none - every grain crosses the base, every drop topples at least 200 times, and the upper half of all avalanches fits between 1,655 and 2,280.
tags: [analysis, castle, sandpile, avalanche, self-organized-criticality, bak-tang-wiesenfeld, dhar, green-function, laplacian, sink-model, tide-model, battlement, rectangle, heavy-tail, numpy, simulation, verification]
sources: [project-euler-502-castle-factoring, rossin-2000-group-of-a-sandpile, dhar-ruelle-sen-verma-1995-algebraic-aspects]
created: 2026-09-26
updated: 2026-09-27
---

# Avalanches on castles - Bak-Tang-Wiesenfeld sand in the sink and tide models

## The experiment

In 1987 Bak, Tang and Wiesenfeld dropped sand, one grain at a time, on random cells of a large grid, using the toppling rule of [[sandpile-group](pages/sandpile-group.md)]. They found that the pile organizes itself into a critical state: most grains cause no avalanche or a small one, but avalanches of every size occur, with a size distribution close to a power law. They called this **self-organized criticality**.[^1]

Here the grid is a castle, and the experiment is run in both models of [[sandpile-group](pages/sandpile-group.md)]:

- the **tide model**: the sink is the whole bottom row, so sand leaves through the ground wherever a cell stands on it;
- the **sink model**: the sink is one cell, the bottom-left cell, so every grain that leaves must reach that corner.

In both, the pile starts at its identity ([[sandpile-identity](pages/sandpile-identity.md)]), which is already recurrent, so no warm-up is needed. Each drop lands on a uniformly random cell outside the sink, and the page records two numbers for each avalanche:

- its **size**, the number of topplings it causes;
- its **duration**, the number of rounds, where one round topples everything that is unstable at once.

The questions: how do ladders, rectangles and battlements compare, does the block count (the castle's horizontal blocks, as in Project Euler 502) or the number of `2 × 2` blocks set the largest avalanches, and how much of the answer depends on where the sand leaves?

## The mean avalanche is exact, in both models

A theorem of Dhar makes the average avalanche size computable without simulation. In the long run, the expected number of topplings at cell `u` caused by a grain dropped at cell `v` is the `(v, u)` entry of `L̃⁻¹`, the inverse of the Laplacian with the sink removed.[^2] Averaging over a uniformly random drop cell,

```
mean avalanche size  =  (1/n) · (sum of all entries of L̃⁻¹)  =  average of x,  where  L̃ x = 1
```

The formula is the same in both models; only `L̃` changes (one row and column deleted in the sink model, the whole bottom row in the tide model). Simulation agrees with it to within 0.3% on every shape tested in both models.[^3]

**A single column is the same in both models.** A column of height `h` is a path hanging from its bottom cell, and that bottom cell is the sink either way. So its mean is `h(2h − 1)/6` in both models: 1 at `h = 2`, 2.5 at `h = 3`, 11 at `h = 6`, 31.67 at `h = 10`. A horizontal path `(1, 1, …, 1)` of `n` cells is the same path lying down, with the sink at its end, and in the sink model it has the same mean `n(2n − 1)/6`. (Under the tide a horizontal path is entirely ground and holds no sand.)[^4]

## Tide model

### Height alone sets the mean for rectangles and battlements

For a `w × h` rectangle, and for a **battlement** of height-`h` spikes separated by single cells, the tide mean avalanche is

```
mean  =  h (2h − 1) / 6
```

for every width. That is exactly the value for a single column of height `h`: 1 for ladders (`h = 2`), 2.5 at `h = 3`, 11 at `h = 6`, 31.67 at `h = 10`, 130 at `h = 20`.[^5]

**Why.** In a rectangle every column looks the same, so the solution `x` of `L̃x = 1` depends only on the row. The sideways terms then cancel, and what remains is the equation for one vertical path hanging from the ground. Its solution is `x(j) = j(2h − 1 − j)/2` at height `j`, and its average over `j = 1 … h − 1` is `h(2h − 1)/6`. A battlement is the same path repeated, because its spikes never touch above the ground. So a `10 × 10` rectangle, packed with `2 × 2` blocks, and a battlement of height-10 spikes, with none, have the **same mean avalanche**.

**General castles.** Joining columns of different heights lowers the mean. For every castle with at most 12 cells (2,130 castles), the tide mean is **at most** the column-by-column prediction (each column treated as its own path), with equality **exactly** when every run of adjacent columns rising above the base has constant height.[^6] For example, `(3, 5, 2, 2, 6, 4)` averages 5.77 topplings against a column prediction of 6.63.

### The 2×2 blocks change the tail, not the mean

Two castles with the same tide mean can avalanche completely differently. From 60,000 random drops each:[^7]

| tide model | 20×20 rectangle | battlement of height-20 spikes |
|---|---|---|
| mean size | 130.3 | 130.4 |
| median size (drops that topple) | 47 | 145 |
| 99th percentile | 2,408 | 190 |
| largest avalanche | 3,701 | 190 |
| drops with size `≥ 200` | 15.5% | none |
| longest duration (rounds) | 601 | 37 |
| log-log slope of the size density on `[10, 1000]` | about `−0.93` | flat |

In the battlement each spike is a separate path, so an avalanche can never be bigger than one spike's worth. The largest observed are 45, 66 and 190 topplings at heights 10, 12 and 20, which is `(h − 1)h/2`. In the rectangle the `2 × 2` blocks tie the columns together, so sand spreads sideways and the largest avalanches grow with the rectangle's area: 447 at `10 × 10`, over 3,500 at `20 × 20`. The size density looks like a power law over two decades, the Bak-Tang-Wiesenfeld signature. These castles are small, though, and the slope is an estimate over a finite range, not an exponent.

**Tide answer.** Neither the block count nor the `2 × 2` count sets the *mean*: height does. The `2 × 2` count (more exactly, how the columns are joined above the base) sets the *tail* and the size of the largest avalanches.

## Sink model

### Width matters, and the blocks lower the mean

With a single sink cell every grain that leaves must travel to the bottom-left corner, so the mean now grows with the width as well as the height. Exact sink-model means for rectangles `(h,)*w`:[^8]

| `h` \ `w` | 1 | 2 | 4 | 8 | 10 |
|---|---|---|---|---|---|
| 2 | 1.0 | 1.667 | 5.673 | 21.79 | 33.853 |
| 3 | 2.5 | 3.32 | 8.446 | 27.101 | 40.437 |
| 6 | 11.0 | 12.396 | 21.903 | 52.572 | 72.156 |
| 10 | 31.667 | 33.853 | 49.436 | 99.328 | 129.909 |

The table is symmetric under turning the rectangle on its side: `(h,)*w` and `(w,)*h` are the same graph, and the corner sink goes to a corner, so `2 × 10` and `10 × 2` both average 33.853. The first column is the single-column value `h(2h − 1)/6`, which the tide model gives for every width.

Battlements `(1, h)*w` (`w` spikes of height `h`, `2w` columns in all), sink model:[^8]

| `h` \ `w` | 1 | 2 | 4 | 8 |
|---|---|---|---|---|
| 3 | 4.667 | 12.0 | 43.2 | 169.806 |
| 6 | 15.167 | 28.0 | 82.963 | 305.455 |
| 10 | 38.5 | 58.667 | 145.302 | 495.632 |

**The sink model reverses the tide finding.** Under the tide the `2 × 2` blocks leave the mean alone. With one sink cell they lower it, because they give the sand many parallel routes to the corner, while a battlement, a tree, has exactly one route: along its base. The `20 × 20` rectangle averages **692.0** topplings per grain and the battlement of height-20 spikes `(1, 20)*10` **1,520.9**, more than twice as much, against 130.0 for both under the tide.[^8]

Whether a column-style inequality holds in the sink model, and what would play the role of the column prediction, is not known.

### The tails

From 60,000 random drops each (seed 5), starting at the sink-model identity:[^9]

| sink model | 20×20 rectangle | battlement of height-20 spikes |
|---|---|---|
| mean size | 692.3 | 1,520.6 |
| median size (drops that topple) | 132 | 1,655 |
| 99th percentile | 11,650 | 2,277 |
| largest avalanche | 21,248 | 2,280 |
| drops with size `≥ 200` | 22.6% | 100% |
| longest duration (rounds) | 2,848 | 75 |
| log-log slope of the size density on `[10, 1000]` | about `−0.98` | none (the upper half of all sizes lies in `[1655, 2280]`) |

The rectangle keeps a heavy tail, its largest avalanche about six times larger than under the tide (21,248 against 3,701), with a density slope close to the tide value. The battlement has no tail at all: every grain that sets off an avalanche has to push sand along the whole base to the corner, so every avalanche is large (all at least 200 topplings, 78% above 1,000) and the upper half of them lies between 1,655 and 2,280. On 20,000 drops, the `10 × 10` rectangle averages 129.8 with a largest avalanche of 2,697 over 534 rounds, and the battlement `(1, 10)*10` averages 757.5 with a largest of 1,135.[^9]

**Sink answer.** Width and the number of routes to the corner set the *mean*, and the `2 × 2` blocks lower it. The blocks still produce the heavy tail; a castle without them avalanches a lot, but never much more than its typical avalanche.

## The two models side by side

| shape | tide mean | sink mean | tide largest (drops) | sink largest (drops) |
|---|---|---|---|---|
| single column, height 10 | 31.667 | 31.667 | - | - |
| `10 × 10` rectangle | 31.667 | 129.909 | 447 (20,000) | 2,697 (20,000) |
| `20 × 20` rectangle | 130.0 | 692.017 | 3,701 (60,000) | 21,248 (60,000) |
| battlement `(1, 20)*10` | 130.0 | 1,520.909 | 190 (60,000) | 2,280 (60,000) |

(Exact means; largest avalanches from the simulations of [^3], [^7] and [^9].) The one modelling choice, where the sand leaves, decides whether the `2 × 2` blocks matter for the mean at all.

## What this settles and what it opens

**Settled.**
- The mean avalanche size is exact (Dhar) in both models, and simulation confirms it.
- A single column has mean `h(2h − 1)/6` in both models.
- Tide model: rectangles and battlements have mean `h(2h − 1)/6`, depending on height alone. Every castle to 12 cells has mean at most its column prediction, with equality exactly when each run of raised columns has constant height. The `2 × 2` blocks set the tail, not the mean; same-mean castles can differ by a factor of 20 in their largest avalanche.
- Sink model: the mean depends on width and height, is symmetric under turning a rectangle on its side, and is lowered by the `2 × 2` blocks (battlement 1,520.9 against rectangle 692.0 at height 20). The rectangle keeps a heavy tail; the battlement's avalanches are all large and tightly bunched below 2,280.

**Open, tide model.**
- Prove the inequality and its equality case for all castles.
- How the rectangle's largest avalanche and tail slope scale with width and height, and whether a genuine exponent emerges for large castles with the sink only at the bottom. The usual square-grid setting lets sand leave through all four sides, as in the grids of [^10].

**Open, sink model.**
- A closed form for the rectangle mean in `w` and `h`, and for the battlement mean.
- How the rectangle's tail scales with size, and whether its slope converges to the tide value.
- Whether the battlement's size distribution has a limit shape as the spikes and the base grow.

**Open, both.** Whether duration and size are related by a power law.

## Snippet

```python
import numpy as np, random

def board(c, model):                       # sand-holding cells; 'sink': bottom-left cell is the sink, 'tide': the bottom row
    cells = [(i, j) for i, h in enumerate(c) for j in range(h)]
    S = set(cells)
    live = [v for v in cells if (v != (0, 0) if model == 'sink' else v[1] > 0)]
    idx = {v: k for k, v in enumerate(live)}
    around = lambda v: ((v[0]+1, v[1]), (v[0]-1, v[1]), (v[0], v[1]+1), (v[0], v[1]-1))
    deg = np.array([sum(u in S for u in around(v)) for v in live])
    nb = [[idx[u] for u in around(v) if u in idx] for v in live]
    return live, deg, nb

def mean_avalanche_exact(c, model='tide'): # Dhar: average over drop cells of the row sums of L~^-1
    live, deg, nb = board(c, model)
    L = np.diag(deg.astype(float))
    for k, ns in enumerate(nb):
        for u in ns:
            L[k, u] -= 1
    return np.linalg.inv(L).sum() / len(live)

def column_prediction(c):                  # tide: each column on its own, a path of height h averages h(2h-1)/6
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

def drop_sand(c, drops, model='tide', seed=1):   # start at the identity, drop grains at random cells
    live, deg, nb = board(c, model)
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
>>> [round(float(mean_avalanche_exact(c, 'sink')), 3) for c in [(10,), (1,) * 10, (2,) * 10, (10,) * 2]]
[31.667, 31.667, 33.853, 33.853]
>>> round(float(mean_avalanche_exact((20,) * 20, 'sink')), 3), round(float(mean_avalanche_exact((1, 20) * 10, 'sink')), 3)
(692.017, 1520.909)
>>> r, b = drop_sand((6,) * 6, 5000, 'sink'), drop_sand((1, 6) * 3, 5000, 'sink')
>>> round(float(mean_avalanche_exact((6,) * 6, 'sink')), 3), round(float(r[:, 0].mean()), 1), int(r[:, 0].max())
(35.726, 35.9, 369)
>>> round(float(mean_avalanche_exact((1, 6) * 3, 'sink')), 3), round(float(b[:, 0].mean()), 1), int(b[:, 0].max())
(50.75, 51.0, 75)
```

Under the tide the `12 × 12` rectangle and the battlement of height-12 spikes both average about 46 topplings (exact: `12·23/6 = 46`); the rectangle's largest avalanche is 754 topplings over 193 rounds, the battlement's 66 over 21. In the sink model a single column and a horizontal path of 10 cells both average 31.667, the `2 × 10` and `10 × 2` rectangles both 33.853, and on `6 × 6` the battlement `(1, 6)*3` averages more than the rectangle (50.75 against 35.73) while the rectangle has the larger avalanches.

## Related Concepts

- [[sandpile-group](pages/sandpile-group.md)] - the game, the toppling rule, and the sink and tide models.
- [[sandpile-identity](pages/sandpile-identity.md)] - the identity the dropping starts from, in both models, and the single-grain avalanche profiles.
- [[sandcastle-clock](pages/sandcastle-clock.md)] - dropping always on the same cell instead of at random.
- [[sandpile-census](pages/sandpile-census.md)] - the sandpile groups of every castle to 16 cells.
- [[castle-graph](pages/castle-graph.md)] - tree castles and battlements, and the `2 × 2` blocks that tie columns together.
- [[levy-flights](pages/levy-flights.md)] - the inverse reduced Laplacian as a grounded effective-resistance matrix, and another power-law tail on castles.
- [[sandcastle-seminar](pages/sandcastle-seminar.md)] - the Sandcastles seminar, following the 16-cell silver castle `(3,2,1,2,2,1,2,3)` through the whole sandpile story.

## Appearances in Sources

- [[dhar-ruelle-sen-verma-1995-algebraic-aspects](pages/dhar-ruelle-sen-verma-1995-algebraic-aspects.md)] - Dhar's steady-state results (commuting addition operators, equally likely recurrent configurations) as summarized in its §2.
- [[rossin-2000-group-of-a-sandpile](pages/rossin-2000-group-of-a-sandpile.md)] - the route to Bak-Tang-Wiesenfeld (1987) and Dhar (1990), both cited here without having been read.
- [[project-euler-502-castle-factoring](pages/project-euler-502-castle-factoring.md)] - the castle definition behind the castle graph.

## Footnotes

[^1]: P. Bak, C. Tang and K. Wiesenfeld, "Self-organized criticality: An explanation of the 1/f noise", Physical Review Letters 59 (1987) 381 - not read; known through [[rossin-2000-group-of-a-sandpile](pages/rossin-2000-group-of-a-sandpile.md)] (reference [1], L98, and L23 for the model's introduction in 1987) and the summary at https://en.wikipedia.org/wiki/Abelian_sandpile_model (the Bak-Tang-Wiesenfeld model, random grain addition, and power-law avalanche statistics on large grids).
[^2]: D. Dhar, "Self-organized critical state of sandpile automaton models", Physical Review Letters 64 (1990) 1613 - not read (bibliographic data from [[rossin-2000-group-of-a-sandpile](pages/rossin-2000-group-of-a-sandpile.md)] reference [10], L116); its steady-state facts as summarized in [[dhar-ruelle-sen-verma-1995-algebraic-aspects](pages/dhar-ruelle-sen-verma-1995-algebraic-aspects.md)] §2 pp. 4-5 (read): the addition operators commute, and the recurrent configurations "in the steady state ... occur with equal probability", which is what makes averaging over the recurrent piles meaningful; the Green-function result as it is standardly stated: in the stationary state of the abelian sandpile, the expected number of topplings at site `j` caused by adding a grain at site `i` is `(Δ⁻¹)_{ij}`, the inverse of the reduced Laplacian. The statement is checked against simulation here in [^3].
[^3]: Verified by execution (Python 3.10, NumPy, 2026-09-26): tide model, 20,000 uniformly random drops starting from the identity on `(2,)*20`, `(10,)*10`, `(20,)*20`, `(1,10)*10`, `(3,)*20`, `(6,)*40` give simulated means 1.000, 31.571, 129.875, 31.584, 2.497, 11.002 against exact means 1.000, 31.667, 130.000, 31.667, 2.500, 11.000. Sink model, 60,000 drops on `(20,)*20` and `(1,20)*10` give 692.3 and 1,520.6 against exact 692.017 and 1,520.909; 20,000 drops on `(10,)*10` and `(1,10)*10` give 129.8 and 757.5 against 129.909 and 758.899; 20,000 drops on the seminar castle `(3,2,1,2,2,1,2,3)` give 32.1 against 32.133.
[^4]: Verified by execution (Python 3.10, NumPy, 2026-09-26): `mean_avalanche_exact((h,), 'sink') = mean_avalanche_exact((h,), 'tide') = h(2h − 1)/6` for `h = 2, 3, 6, 10`, and `mean_avalanche_exact((1,)*n, 'sink') = n(2n − 1)/6` for `n = 2, 5, 10`; the height-10 and 10-cell cases are pinned in the Snippet.
[^5]: Verified by execution (Python 3.10, NumPy, 2026-09-26): `mean_avalanche_exact` (tide) equals `h(2h − 1)/6` to `10⁻⁹` for every rectangle `(h,)*w` and every battlement `(1, h)*w` with `2 ≤ h ≤ 12`, `1 ≤ w ≤ 8`.
[^6]: Verified by execution (Python 3.10, NumPy, 2026-09-26): for all 2,130 mirror-distinct castles with at most 12 cells and height at least 2, the tide `mean_avalanche_exact(c) ≤ column_prediction(c) + 10⁻⁹`, with equality (to `10⁻⁹`) in 1,129 cases, exactly those in which every maximal run of adjacent columns of height at least 2 has constant height.
[^7]: Verified by execution (Python 3.10, NumPy, 2026-09-26): tide model, 60,000 random drops (seed 5) from the identity of `(20,)*20` and `(1,20)*10`; median and 99th percentile over drops with size `> 0`; slope from a least-squares fit of log density against log size in 10 logarithmic bins on `[10, 1000]`. The battlement maxima 45, 66, 190 at heights 10, 12, 20 are from the runs of [^3], the Snippet and this footnote; the `10 × 10` rectangle maximum 447 is from [^3]. The `12 × 12` comparison is pinned in the Snippet.
[^8]: Verified by execution (Python 3.10, NumPy, 2026-09-26): sink-model `mean_avalanche_exact` (sink at the bottom-left cell) for `(h,)*w` with `h ∈ {2, 3, 6, 10}`, `w ∈ {1, 2, 4, 8, 10}`, for `(1, h)*w` with `h ∈ {3, 6, 10}`, `w ∈ {1, 2, 4, 8}`, and for `(20,)*20` and `(1,20)*10`, as tabulated; `(2,)*10` and `(10,)*2`, `(20,)*20` and `(1,20)*10` are pinned in the Snippet.
[^9]: Verified by execution (Python 3.10, NumPy, 2026-09-26): sink model, 60,000 random drops (seed 5) from the sink-model identity of `(20,)*20` and `(1,20)*10`, and 20,000 drops (seed 5) on `(10,)*10` and `(1,10)*10`; median and 99th percentile over drops with size `> 0`; slope fitted as in [^7] (on the battlement the fit over `[10, 1000]` has little data: every drop topples at least 200 times and 78% exceed 1,000). A 5,000-drop version on `6 × 6` is pinned in the Snippet.
[^10]: [[rossin-2000-group-of-a-sandpile](pages/rossin-2000-group-of-a-sandpile.md)] §1 L25 and §4 L92 - "Figure 1: Multi-graph corresponding to the 4 × 4 grid"; "the 2 × 2 grid consisting of 4 cells, each connected twice to the sink": boundary cells are joined to the sink once per missing neighbour, so sand leaves through every side.
