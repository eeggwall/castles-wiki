---
title: Avalanches on castles - Bak-Tang-Wiesenfeld sand in the sink and tide models
category: Analyses
summary: The self-organized-criticality sandpile of Bak, Tang and Wiesenfeld run on castles in both models of sandpile-group, the tide model (the whole bottom row as the sink) and the sink model (one sink cell, the bottom-left cell), starting from the identity and dropping grains on uniformly random cells. By Dhar's theorem the mean avalanche size is the average of the solution of L̃x = 1, and simulation agrees within 0.3%. In the tide model every rectangle and every battlement of height h has mean h(2h−1)/6 (proved), and every castle with at most 12 cells has mean at most the column-by-column value, with equality exactly when each run of raised columns has constant height (computed); the 2×2 blocks change the tail, not the mean (20×20 rectangle: largest avalanche 3,701 of 60,000; battlement of height 20: every avalanche at most 190 = 20·19/2, exactly). In the sink model the mean grows with width as well as height, and the battlement (1, 20)*10, a tree castle, averages 1,520.9 topplings against 692.0 for the 20×20 rectangle; the rectangle keeps a heavy tail (largest 21,248), while every grain on the battlement causes the same avalanche each time it lands on the same cell, between 209 and 2,280 topplings.
tags: [analysis, castle, sandpile, avalanche, self-organized-criticality, bak-tang-wiesenfeld, dhar, green-function, laplacian, sink-model, tide-model, battlement, rectangle, heavy-tail, numpy, simulation, verification]
sources: [project-euler-502-castle-factoring, rossin-2000-group-of-a-sandpile, dhar-ruelle-sen-verma-1995-algebraic-aspects, dhar-1990-self-organized-critical-sandpile, bak-tang-wiesenfeld-1988-self-organized-criticality]
created: 2026-09-26
updated: 2026-10-29
---

# Avalanches on castles - Bak-Tang-Wiesenfeld sand in the sink and tide models

## The experiment

Bak, Tang and Wiesenfeld added sand to random sites of a square grid, one grain at a time, with the toppling rule of [[sandpile-group](pages/sandpile-group.md)], and found that avalanches of every size occur, with a size distribution close to a power law. They called this **self-organized criticality**.[^1]

Here the grid is a castle, in both models of [[sandpile-group](pages/sandpile-group.md)]:

- the **tide model**: the sink is the whole bottom row;
- the **sink model**: the sink is one cell, the bottom-left cell.

In both, the pile starts at its identity ([[sandpile-identity](pages/sandpile-identity.md)]), which is recurrent. Each grain lands on a uniformly random cell outside the sink, and each avalanche has two numbers:

- its **size**, the number of topplings it causes;
- its **duration**, the number of rounds of the Snippet's `topple`, where each round topples, as often as they can, the cells made unstable by the previous round.

The shapes compared are rectangles `(h,)*w` and **battlements** `(1, h)*w`, `w` columns of height `h` each followed by a column of height 1. A battlement has no `2 × 2` block of cells, so it is a tree castle.

## The mean avalanche is exact

**Theorem (Dhar).** In the steady state, the expected number of topplings at cell `u` caused by a grain added at cell `v` is the `(v, u)` entry of `L̃⁻¹`, the inverse of the reduced Laplacian.[^2]

Averaging over a uniformly random drop cell gives

```
mean avalanche size  =  (1/n) · (sum of all entries of L̃⁻¹)  =  average of x,  where  L̃ x = 1,      (1)
```

with `n` the number of cells outside the sink. Only `L̃` differs between the models. Simulation agrees with Equation (1) to within 0.3% on every shape tested in both models, and averaging the topplings over all recurrent configurations reproduces `L̃⁻¹` entry by entry on small castles.[^3]

**A single column is the same in both models.** A column of height `h` is a path whose bottom cell is the sink in either model. The solution of `L̃x = 1` at height `j = 1, …, h − 1` above the bottom cell is

```
x(j)  =  j (2h − 1 − j) / 2,                                                         (2)
```

since `2x(j) − x(j − 1) − x(j + 1) = 1` for `j < h − 1`, with `x(0) = 0`, and `x(h − 1) − x(h − 2) = 1` at the top. Its average over `j` is `h(2h − 1)/6`: 1 at `h = 2`, 2.5 at `h = 3`, 11 at `h = 6`, 31.67 at `h = 10`. A horizontal path `(1, 1, …, 1)` of `n` cells is the same path lying down, and in the sink model it has mean `n(2n − 1)/6`. In the tide model a horizontal path is all sink and holds no sand.[^4]

## Tide model

### Rectangles and battlements: the mean depends on the height only

**Proposition.** In the tide model, every rectangle `(h,)*w` and every battlement `(1, h)*w` has mean avalanche size `h(2h − 1)/6`, the value of a single column.

*Proof.* In a rectangle, try `x` equal to Equation (2) on every column. A cell in row `j` with `1 ≤ j ≤ h − 2` has its two vertical neighbors and up to two side neighbors, and the side terms of `L̃x` cancel against the matching part of the degree, so the equation of the cell is the path equation `2x(j) − x(j − 1) − x(j + 1) = 1`; the same holds in the top row with `x(h − 1) − x(h − 2) = 1`. So `x` solves `L̃x = 1`, and its average is the column average. In a battlement the raised cells of different columns are not neighbors, so each column is a separate path standing on the bottom row.[^5]

So the `10 × 10` rectangle, made of `2 × 2` blocks, and the battlement `(1, 10)*10`, with none, both have mean 31.67.

**General castles.** For every castle with at most 12 cells and height at least 2 (2,130 castles, mirror images removed), the tide mean is **at most** the **column prediction**, the mean of Equation (2) taken over the raised cells of each column separately, with equality in 1,129 castles, **exactly** those in which every run of adjacent columns of height at least 2 has constant height.[^6] For example, `(3, 5, 2, 2, 6, 4)` averages 5.77 topplings against a column prediction of 6.63.

### The 2×2 blocks change the tail, not the mean

From 60,000 random drops each (seed 5):[^7]

| tide model | 20×20 rectangle | battlement `(1, 20)*10` |
|---|---|---|
| mean size | 130.3 | 130.4 |
| median size (drops that topple) | 47 | 145 |
| 99th percentile (drops that topple) | 2,409 | 190 |
| largest avalanche | 3,701 | 190 |
| drops with size `≥ 200` | 15.4% | none |
| longest duration (rounds) | 601 | 37 |
| log-log slope of the size density on `[10, 1000]` | about `−0.93` | no sizes above 190 |

**The battlement's avalanches are fixed.** A battlement is a tree castle, so its tide group is trivial and the identity is its only recurrent configuration ([[sandpile-group](pages/sandpile-group.md)], the Proposition in Part 3). Every grain therefore lands on the same configuration, and a grain on the cell at height `j` causes exactly `x(j) = j(2h − 1 − j)/2` topplings, Equation (2). The largest is `x(h − 1) = h(h − 1)/2`: 45, 66 and 190 at heights 10, 12 and 20, the largest values the simulations record. In the rectangle the `2 × 2` blocks join the columns, and the largest observed avalanches grow with the area: 447 at `10 × 10` on 20,000 drops, 3,701 at `20 × 20` on 60,000. The rectangle's size density has slope about `−0.93` on `[10, 1000]`, a fit over a finite range; Bak, Tang and Wiesenfeld report `τ ≈ 1.0` on a `50 × 50` square with sand lost at all four edges.[^8]

## Sink model

### Width matters

With one sink cell the mean depends on the width as well as the height. Exact sink-model means for rectangles `(h,)*w`:[^9]

| `h` \ `w` | 1 | 2 | 4 | 8 | 10 |
|---|---|---|---|---|---|
| 2 | 1.0 | 1.667 | 5.673 | 21.79 | 33.853 |
| 3 | 2.5 | 3.32 | 8.446 | 27.101 | 40.437 |
| 6 | 11.0 | 12.396 | 21.903 | 52.572 | 72.156 |
| 10 | 31.667 | 33.853 | 49.436 | 99.328 | 129.909 |

The table is symmetric: `(h,)*w` and `(w,)*h` are the same graph, and the corner sink goes to a corner, so `2 × 10` and `10 × 2` both average 33.853. The first column is the single-column value `h(2h − 1)/6`.

Battlements `(1, h)*w` (`w` columns of height `h`, `2w` columns in all), sink model:[^9]

| `h` \ `w` | 1 | 2 | 4 | 8 |
|---|---|---|---|---|
| 3 | 4.667 | 12.0 | 43.2 | 169.806 |
| 6 | 15.167 | 28.0 | 82.963 | 305.455 |
| 10 | 38.5 | 58.667 | 145.302 | 495.632 |

At height 20 the battlement `(1, 20)*10` averages **1,520.9** topplings per grain and the `20 × 20` rectangle **692.0**, against 130.0 for both in the tide model.[^9]

### The tails

From 60,000 random drops each (seed 5), starting at the sink-model identity:[^10]

| sink model | 20×20 rectangle | battlement `(1, 20)*10` |
|---|---|---|
| mean size | 692.3 | 1,520.6 |
| median size (drops that topple) | 132 | 1,655 |
| 99th percentile (drops that topple) | 11,650 | 2,277 |
| largest avalanche | 21,248 | 2,280 |
| drops with size `≥ 200` | 22.6% | 100% |
| longest duration (rounds) | 2,848 | 75 |
| log-log slope of the size density on `[10, 1000]` | about `−0.98` | not a power law: every size lies in `[209, 2280]` |

The rectangle keeps a heavy tail; its largest avalanche is about six times its tide-model value (21,248 against 3,701). The battlement is again a tree castle, so its sink group is trivial, its identity is its only recurrent configuration, and a grain on cell `v` always causes `Σ_u (L̃⁻¹)_{vu}` topplings. These row sums range from **209** to **2,280** over the 209 cells outside the sink, with median 1,655, and 77.5% of them exceed 1,000. On 20,000 drops, the `10 × 10` rectangle averages 129.8 with a largest avalanche of 2,697 over 534 rounds, and the battlement `(1, 10)*10` averages 757.5, with row sums from 109 to 1,135.[^10]

## The two models side by side

| shape | tide mean | sink mean | tide largest (drops) | sink largest (drops) |
|---|---|---|---|---|
| single column, height 10 | 31.667 | 31.667 | - | - |
| `10 × 10` rectangle | 31.667 | 129.909 | 447 (20,000) | 2,697 (20,000) |
| `20 × 20` rectangle | 130.0 | 692.017 | 3,701 (60,000) | 21,248 (60,000) |
| battlement `(1, 20)*10` | 130.0 | 1,520.909 | 190 (exact) | 2,280 (exact) |

The means are exact; the rectangles' largest avalanches come from the simulations of the sections *Tide model* and *Sink model*.

**Comparison with the square grid.** On the square grid with sand lost at all four edges, Bak, Tang and Wiesenfeld found `τ ≈ 1.0` on a `50 × 50` array, close to the slope `−0.93` measured here on the tide rectangle, and Dhar quotes the later estimate `τ ≈ 1.22` and computes the mean avalanche size `⟨T⟩ ∼ ℓ²` on the `ℓ × ℓ` grid, against `h(2h − 1)/6` for the tide rectangle ([[bak-tang-wiesenfeld-1988-self-organized-criticality](pages/bak-tang-wiesenfeld-1988-self-organized-criticality.md)]).[^8][^11] Rossin's grids lose sand through every side in the same way.[^12]

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

In the tide model the `12 × 12` rectangle and the battlement `(1, 12)*6` both average about 46 topplings (exactly `12·23/6 = 46`); the rectangle's largest avalanche is 754 topplings over 193 rounds, the battlement's 66 over 21. In the sink model a single column and a horizontal path of 10 cells both average 31.667, the `2 × 10` and `10 × 2` rectangles both 33.853, and on `6 × 6` the battlement `(1, 6)*3` averages more than the rectangle (50.75 against 35.73) while the rectangle has the larger avalanches.

## Related Concepts

- [[sandpile-group](pages/sandpile-group.md)] - the sandpile, the toppling rule, the two models, and the triviality of the groups of tree castles.
- [[sandpile-identity](pages/sandpile-identity.md)] - the identity the dropping starts from, and the single-grain avalanche profiles.
- [[sandcastle-clock](pages/sandcastle-clock.md)] - grains dropped always on the same cell.
- [[sandpile-census](pages/sandpile-census.md)] - the sandpile groups of every castle to 16 cells.
- [[castle-graph](pages/castle-graph.md)] - tree castles, battlements among them, and the `2 × 2` blocks that join columns.
- [[tree-castle-diffusion](pages/tree-castle-diffusion.md)] - the simple random walk on a battlement: the order-1/2 window, the long-time rate `2/(h + 1)` and the crossover at `t = 8(h + 1)²/π`.
- [[levy-flights](pages/levy-flights.md)] - the inverse reduced Laplacian as a grounded effective-resistance matrix, and a power-law tail of the fractional walk on castles.
- [[sandcastle-seminar](pages/sandcastle-seminar.md)] - the castle `(3,2,1,2,2,1,2,3)` followed through its group, clock, identity and avalanches.

## Appearances in Sources

- [[bak-tang-wiesenfeld-1988-self-organized-criticality](pages/bak-tang-wiesenfeld-1988-self-organized-criticality.md)] - the automaton, the random-dropping protocol, and the size exponent on the square grid.
- [[chau-1993-abelian-sandpile-model](pages/chau-1993-abelian-sandpile-model.md)] - the reference list for the early abelian sandpile literature.
- [[dhar-1990-self-organized-critical-sandpile](pages/dhar-1990-self-organized-critical-sandpile.md)] - the theorem `G = Δ⁻¹` behind Equation (1), the uniform steady state, and the two-dimensional exponent estimate.
- [[dhar-ruelle-sen-verma-1995-algebraic-aspects](pages/dhar-ruelle-sen-verma-1995-algebraic-aspects.md)] - Dhar's steady-state results as summarized in its §2.
- [[rossin-2000-group-of-a-sandpile](pages/rossin-2000-group-of-a-sandpile.md)] - square grids with sand lost through every side.
- [[project-euler-502-castle-factoring](pages/project-euler-502-castle-factoring.md)] - the castle definition behind the castle graph.

## Footnotes

[^1]: [[bak-tang-wiesenfeld-1988-self-organized-criticality](pages/bak-tang-wiesenfeld-1988-self-organized-criticality.md)] pp.364-370 §§I, III.B [synthesis] - the full account of the 1987 letter (*Phys. Rev. Lett.* 59, 381): extended dissipative systems "naturally evolve into a critical state, with no characteristic time or length scales"; on the square lattice, adding units at random sites (eq. 3.8) and toppling by eq. 3.2 gives a size distribution close to a power law, exponent about 1.0 in two dimensions.
[^2]: [[dhar-1990-self-organized-critical-sandpile](pages/dhar-1990-self-organized-critical-sandpile.md)] pp.1614-1616 L85-101, L235-254 [synthesis] - in the steady state "only recurrent configurations have a nonzero probability of occurrence, and this nonzero value is the same for all recurrent configurations"; `G_ij`, "the expected number of topplings at site j, due to the avalanche caused by adding a particle at i", satisfies `Σ_k G_ik Δ_kj = δ_ij` (eq. 19), so `G_ij = [Δ⁻¹]_ij` (eq. 20); for a castle `Δ` is the reduced Laplacian `L̃` of either model.
[^3]: Verified by execution (Python 3.11, NumPy, SymPy, 2026-10-16): tide model, 20,000 drops (seed 1) from the identity on `(2,)*20`, `(10,)*10`, `(20,)*20`, `(1,10)*10`, `(3,)*20`, `(6,)*40` give means 1.000, 31.571, 129.875, 31.584, 2.497, 11.002 against exact 1, 31.667, 130, 31.667, 2.5, 11; sink model, 60,000 drops (seed 5) on `(20,)*20` and `(1,20)*10` give 692.3 and 1,520.6 against exact 692.017 and 1,520.909, 20,000 drops (seed 5) on `(10,)*10` and `(1,10)*10` give 129.8 and 757.5 against 129.909 and 758.899, and 20,000 drops (seed 2) on `(3,2,1,2,2,1,2,3)` give 32.06 against 32.133. Averaging the topplings over all recurrent configurations, found by breadth-first search from the fullest stable configuration, after one grain at each cell reproduces `L̃⁻¹` exactly on `(2,2)`, `(2,2,2)`, `(3,3)`, `(2,3,2)`, `(2,2,2,2)` in the sink model and `(3,3,3)`, `(1,3,3,2)` in the tide model (4 to 95 recurrent configurations).
[^4]: Verified by execution (Python 3.11, NumPy, 2026-10-16): Equation (1) gives `h(2h − 1)/6` for the column `(h)` in both models at `h = 2, 3, 6, 10`, and `n(2n − 1)/6` for `(1,)*n` in the sink model at `n = 2, 5, 10`; the height-10 and 10-cell cases are pinned in the Snippet.
[^5]: Verified by execution (Python 3.11, NumPy, 2026-10-16): the tide mean equals `h(2h − 1)/6` to `10⁻¹²` for every rectangle `(h,)*w` and every battlement `(1, h)*w` with `2 ≤ h ≤ 12`, `1 ≤ w ≤ 8`.
[^6]: Verified by execution (Python 3.11, NumPy, 2026-10-16): for all 2,130 mirror-distinct castles with at most 12 cells and height at least 2, the tide mean is at most the column prediction plus `10⁻⁹`, with equality (to `10⁻⁹`) in 1,129 castles, exactly those in which every maximal run of adjacent columns of height at least 2 has constant height.
[^7]: Verified by execution (Python 3.11, NumPy, 2026-10-16): tide model, 60,000 random drops (seed 5) from the identity of `(20,)*20` and `(1,20)*10`; median and 99th percentile (linear interpolation) over drops with size `> 0`; slope from a least-squares fit of log density against log size over 10 logarithmic bins on `[10, 1000]`. The `10 × 10` maximum 447 is from the 20,000-drop run of [^3]; the `12 × 12` comparison is pinned in the Snippet.
[^8]: [[bak-tang-wiesenfeld-1988-self-organized-criticality](pages/bak-tang-wiesenfeld-1988-self-organized-criticality.md)] p.368 L278-300 [synthesis] - "D(s) ≈ s^{−τ}, τ ≈ 1.0 for D = 2" on a 50 × 50 array (eq. 3.3), with what the paper calls closed boundary conditions, `z(0, y) = z(x, 0) = z(N+1, y) = z(x, N+1) = 0`: the toppling variable `z` of eq. 3.2 is lost at all four edges.
[^9]: Verified by execution (Python 3.11, NumPy, 2026-10-16): Equation (1) in the sink model (sink at the bottom-left cell) for `(h,)*w` with `h ∈ {2, 3, 6, 10}`, `w ∈ {1, 2, 4, 8, 10}`, for `(1, h)*w` with `h ∈ {3, 6, 10}`, `w ∈ {1, 2, 4, 8}`, and for `(20,)*20` and `(1,20)*10`, as tabulated; the symmetry `(h,)*w ↔ (w,)*h` checked on three pairs; several values are pinned in the Snippet.
[^10]: Verified by execution (Python 3.11, NumPy, 2026-10-16): sink model, 60,000 random drops (seed 5) from the identity of `(20,)*20` and `(1,20)*10`, and 20,000 drops (seed 5) on `(10,)*10` and `(1,10)*10`, statistics as in [^7]; the row sums of `L̃⁻¹` on `(1,20)*10`, from 209 to 2,280 with median 1,655, and on `(1,10)*10`, from 109 to 1,135, from the solution of `L̃x = 1`; the smallest simulated avalanche on `(1,20)*10` is 209. A 5,000-drop version on `6 × 6` is pinned in the Snippet.
[^11]: [[dhar-1990-self-organized-critical-sandpile](pages/dhar-1990-self-organized-critical-sandpile.md)] pp.1613, 1616 L42-53, L252-268 [synthesis] - "the numerical estimate τ ≈ 1.22" at `d = 2`, and eq. 21 with "⟨T⟩ ∼ L²" for the lattice with losses at every edge (exponents read from the page images).
[^12]: [[rossin-2000-group-of-a-sandpile](pages/rossin-2000-group-of-a-sandpile.md)] §1 L25 and §4 L92 - "Figure 1: Multi-graph corresponding to the 4 × 4 grid"; "the 2 × 2 grid consisting of 4 cells, each connected twice to the sink": boundary cells are joined to the sink once per missing neighbor, so sand leaves through every side.
