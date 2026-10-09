---
title: Relaxation time of a sandcastle - Dhar's spectrum in the sink and tide models
category: Analyses
summary: Dhar's transition matrix W (one grain on a uniformly random cell outside the sink, then stabilize) is a random walk on the sandpile group K, so its eigenvalues are character sums λ(ψ) = (1/n_live) Σ_v ψ(e_v), computed exactly from the Smith form of L̃ and checked against the full W on 66 castles. Over all 33,150 castles to 16 cells, in both models, no castle is periodic (every nontrivial group relaxes), the 6,963 tree castles relax after one grain, and the tide model is the slower one, 2.3 to 3.1 times at the same cell count from 6 cells on. Relaxation time t_rel = −1/ln λ* grows like the cell count in both models - about 0.47 grains per cell for the slowest sink castles and 2 × w rectangles, up to 1.71 per cell for the slowest tide castles (three tall columns of nearly equal height, such as (5, 5, 6)). Under the tide, rectangles of fixed width grow linearly in height (2.769 per row at width 2, exact to h = 14; 5.240 at width 3, to h = 8), not like the mean avalanche h(2h − 1)/6. In width they are not monotone: a mirror-symmetric slow mode unfolds to every multiple of its width, so widths 3, 6 and 9 relax at the same rate. The sink castle (2, h) has λ* = (h − 1)/(h + 1).
tags: [analysis, castle, sandpile, relaxation, spectral-gap, markov-chain, character, dhar, sink-model, tide-model, rectangle, laplacian, smith-normal-form, numpy, verification]
sources: [dhar-1990-self-organized-critical-sandpile, bayer-diaconis-1992-dovetail-shuffle]
created: 2026-10-08
updated: 2026-10-08
---

# Relaxation time of a sandcastle - Dhar's spectrum in the sink and tide models

## The question

Drop grains one at a time on a castle, stabilizing after each drop, in either model of [[sandpile-group](pages/sandpile-group.md)]: the **sink model**, where the bottom-left cell is the only sink, or the **tide model**, where the whole bottom row is the sink. The pile settles into the steady state, uniform on the recurrent configurations. This page asks how many grains that takes.

1. Compute the relaxation time of every castle up to 16 cells, in both models.
2. Find how it scales with height and width for rectangles, and whether the tide gives `h²` like the mean avalanche `h(2h − 1)/6` of [[castle-avalanches](pages/castle-avalanches.md)].
3. Find which shapes relax slowest per cell.

Short answers: (1) done, and every castle with a nontrivial group relaxes, none is periodic; (2) linear in height under the tide, not `h²`, and roughly proportional to the cell count in both models; (3) under the tide, three tall columns of nearly equal height; in the sink model, a 2-column next to the sink followed by tall columns.

## Dhar's relaxation spectrum

Let `n_live` be the number of cells outside the sink, `L̃` the reduced Laplacian on them, and `e_v` the configuration with one grain on cell `v`. If `P_t` is the distribution of the stable configuration after `t` grains, Dhar's master equation is `P_{t+1} = W P_t` with `W = Σ_v p_v a_v`, where `a_v` adds a grain at `v` and stabilizes and `p_v` is the chance the grain lands at `v`. The steady state has eigenvalue 1, and the next-largest eigenvalue sets the relaxation time.[^1] Here `p_v = 1/n_live`, as in the avalanche experiments of [[castle-avalanches](pages/castle-avalanches.md)].

On the recurrent configurations, `a_v` acts as adding the class of `e_v` in the sandpile group `K = Z^{n_live} / L̃ Z^{n_live}`, so `W` is a random walk on `K`. Its eigenvectors are the characters `ψ` of `K`, with eigenvalues

```
λ(ψ) = (1/n_live) Σ_v ψ(e_v),        ψ(e_v) = exp(2πi φ_v),   φ ∈ L̃⁻¹ Z^{n_live},
```

which are Dhar's one-dimensional representations `a_v = exp(iφ_v)` with `φ = 2π L̃⁻¹ n` (here `φ` is measured in turns, without the `2π`).[^2] Write `λ* = max |λ(ψ)|` over the nontrivial characters and

```
t_rel = −1 / ln λ*   grains,
```

so a deviation from the steady state shrinks by a factor `e` every `t_rel` grains. When `K` is trivial (the tree castles) there is one recurrent configuration and the pile is in its steady state after one grain from any recurrent start; `t_rel = 0`.

**Method.** The Smith normal form `P L̃ Q = diag(d_1, …, d_r)`, with `P` tracked, sends `e_v` to column `v` of `P` modulo the `d_i`, and the characters are the vectors `k` with `k_i ∈ Z/d_i`. Every character is enumerated, exactly, in integer arithmetic modulo the exponent of `K`. Against the full matrix `W`, built by stabilizing every recurrent configuration plus every grain, the second-largest eigenvalue modulus agrees to `4 × 10⁻¹⁵` on 66 castles in both models (60 random castles to 10 cells and six from the gallery), and the group orders agree with [[sandpile-census](pages/sandpile-census.md)].[^3]

## 1. The census, in both models

Of the 33,150 castles to 16 cells, 6,963 are tree castles with trivial group in both models. For the other 26,187, `λ* < 1` in both models: **no castle sandpile is periodic**. A walk on `K` is periodic exactly when some nontrivial character takes one value on every `e_v`; for castles that never happens.[^4]

The slowest castle at each cell count:

| cells | sink model | `λ*` | `t_rel` | tide model | `λ*` | `t_rel` |
|---|---|---|---|---|---|---|
| 4 | `(2, 2)` | 0.3333 | 0.91 | `(2, 2)` | 0.5000 | 1.44 |
| 5 | `(2, 3)` | 0.5000 | 1.44 | `(2, 3)` | 0.5774 | 1.82 |
| 6 | `(2, 4)` | 0.6000 | 1.96 | `(3, 3)` | 0.8072 | 4.67 |
| 7 | `(2, 5)` | 0.6667 | 2.47 | `(3, 4)` | 0.8395 | 5.72 |
| 8 | `(2, 3, 3)` | 0.7165 | 3.00 | `(4, 4)` | 0.8787 | 7.73 |
| 9 | `(2, 3, 4)` | 0.7518 | 3.51 | `(3, 3, 3)` | 0.9015 | 9.64 |
| 10 | `(2, 3, 5)` | 0.7793 | 4.01 | `(3, 3, 4)` | 0.9150 | 11.26 |
| 11 | `(2, 3, 3, 3)` | 0.8032 | 4.56 | `(3, 4, 4)` | 0.9268 | 13.16 |
| 12 | `(2, 3, 3, 4)` | 0.8210 | 5.07 | `(4, 4, 4)` | 0.9363 | 15.19 |
| 13 | `(2, 3, 4, 4)` | 0.8362 | 5.59 | `(4, 4, 5)` | 0.9426 | 16.93 |
| 14 | `(2, 4, 4, 4)` | 0.8490 | 6.11 | `(4, 5, 5)` | 0.9479 | 18.69 |
| 15 | `(2, 4, 4, 5)` | 0.8598 | 6.62 | `(5, 5, 5)` | 0.9523 | 20.46 |
| 16 | `(2, 4, 4, 6)` | 0.8691 | 7.13 | `(5, 5, 6)` | 0.9560 | 22.21 |

The tide model is the slower one: from 6 cells on, its slowest castle takes 2.3 to 3.1 times as many grains as the sink model's, and the slowest sink time grows by about half a grain per cell, the slowest tide time by about 1.75. The sink model is not mirror-symmetric, since the sink sits in the bottom-left corner: of the 1,293 non-symmetric castles with a nontrivial group to 12 cells, 1,182 relax at a different rate from their mirror image. The tide model is mirror-symmetric.[^4]

**Slowest per cell.** Dividing by `n_live`, the sink model's slowest castles to 16 cells are `(2, 4, 4, 6)`, `(2, 4, 5, 5)` and `(2, 4, 6, 4)` at 0.475 grains per cell: a 2-column on the sink, then tall columns. The tide model's are `(5, 5, 6)` and `(5, 6, 5)` at 1.708, then `(4, 5, 7)`, `(4, 6, 6)` and `(5, 5, 5)`. The fastest nontrivial tide castles at 16 cells take 0.028 grains: a long row of height 1 with three columns of height 2 near one end, such as `(1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 2, 2)`.[^4]

**A closed form.** The sink castles `(2, h)` and `(h, 2)` have a single `2 × 2` block, `K_sink = Z/4`, and

```
λ* = (h − 1)/(h + 1),     t_rel = 1 / ln((h + 1)/(h − 1)) ≈ h/2,
```

checked for `2 ≤ h ≤ 30`.[^5] They are the slowest sink castles from 4 to 7 cells.

**The slowest character is not local.** One might expect the slowest mode to come from a single cell, `φ = L̃⁻¹ e_u` (a column of the expected-toppling matrix). It does not, on 14,078 castles in the sink model and 7,194 in the tide model. The characters `φ = L̃⁻¹ (e_u ± e_v)` together with the single cells find the exact `λ*` on every tide castle to 12 cells and on all but 3 of 1,372 sink castles, but not on the height-3 tide rectangles of widths 7, 8 and 9, so they are only a lower bound on `λ*` in general.[^6]

## 2. Rectangles

**Tide model, by height.** At fixed width the relaxation time grows linearly in height, with a constant increment per row once `h` passes a few rows:[^7]

| width | `h = 2` | 3 | 4 | 5 | 6 | 8 | 10 | 14 | increment per row |
|---|---|---|---|---|---|---|---|---|---|
| 2 | 1.443 | 4.668 | 7.733 | 10.559 | 13.337 | 18.877 | 24.416 | 35.492 | 2.769 (from `h = 10`) |
| 3 | 3.403 | 9.639 | 15.189 | 20.463 | 25.706 | 36.186 | - | - | 5.240 (from `h = 7`) |

So the tide's slowest mode does not scale like the mean avalanche `h(2h − 1)/6`. Per cell outside the ground, `t_rel/n_live` tends to about 1.385 at width 2 and 1.747 at width 3.

**Tide model, by width.** At fixed height the relaxation time is not monotone in width. At height 3 it is 4.67, 9.64, 6.34, 8.57, 9.64 for widths 2 to 6, and 9.64 again at width 9. At height 2 it dips and recovers in the same pattern (3.40 at widths 3 and 6), then grows steadily from width 9: 3.42, 3.65, 3.90, …, 5.95 at width 18, with increments that are themselves growing.[^7]

The repeats are **mirror unfolding**. A character of `K` is a phase vector `φ` with `L̃ φ` integral. Glue a castle `c` to its mirror image `c^R`, giving the castle `c c^R`, and give each cell of the mirrored half the phase of its mirror cell. At the seam each cell gains one neighbour with its own phase, which adds `φ_v − φ_v = 0` to its row of `L̃ φ`, so the glued vector is a character of `c c^R`. It takes each value on twice as many cells, so its `λ` is unchanged. Under the tide the ground is mirror-invariant, so the gluing never moves the sink, and `λ*(c c^R) ≥ λ*(c)`. Gluing `k` alternately mirrored copies works the same way at every seam, and a rectangle is its own mirror image, so a rectangle of width `kw` relaxes at least as slowly as the rectangle of width `w` and the same height, for every `k ≥ 1`. A slowest mode of `(3, 3, 3)` is itself mirror-symmetric (phases `13/19, 12/19, 13/19` on the top row and `14/19, 10/19, 14/19` below), and a slowest mode of `(3, 3, 3, 3, 3, 3)` is that pattern twice.[^8] In the sink model the mirror half would carry a second copy of the corner, which is not a sink, and the argument fails.

**Sink model.** Rectangles are symmetric under turning on their side (the corner sink is fixed by the reflection in the diagonal), and `t_rel` is close to proportional to the cell count. For the `2 × w` rectangles each extra column adds 0.969 grains, and `t_rel/n_live` climbs 0.391, 0.422, …, 0.467 from `w = 3` to `13`; the squares give 0.303, 0.402, 0.447 at sides 2, 3, 4.[^9] The larger rectangles have groups too big to enumerate; the pair characters give lower bounds that continue the same trend, `t_rel ≥ 45.4` at width 12 and height 8 (`0.48` per cell), but these are not exact.

## What this settles and what it opens

**Settled.**
- Dhar's relaxation spectrum is a character sum over `K`, computed exactly for all 33,150 castles to 16 cells in both models.
- No castle sandpile is periodic; tree castles relax in one grain.
- The tide model relaxes 2 to 3 times more slowly than the sink model at the same cell count; its slowest castles are three tall columns of nearly equal height, the sink model's start with a 2-column on the sink.
- Under the tide, rectangles of width 2 and 3 grow linearly in height, not like `h(2h − 1)/6`.
- Mirror unfolding: `λ*(c c^R) ≥ λ*(c)` under the tide, which explains the equal times at widths 3, 6, 9.
- `λ* = (h − 1)/(h + 1)` for the sink castles `(2, h)` and `(h, 2)`.

**Open.**
- Closed forms for the tide increments 2.769 (width 2) and 5.240 (width 3), and the increment for general width.
- How the tide time grows in width at fixed height once unfolding stops dominating (height 2 is still accelerating at width 18), and whether it reaches a `w²` regime.
- Whether `t_rel/n_live` has a limit for sink rectangles (about 0.47 to 0.48 in the range computed).
- A proof that no castle sandpile is periodic.
- A way to find the slowest character without enumerating `K`, since single cells and pairs are not enough.

## Relation to Dhar's scaling

Dhar states that for the undirected `d`-dimensional lattice the slowest relaxation time grows like the linear size to the power `d`, much longer than an avalanche lasts.[^1] His lattice loses sand through all four sides. Castles lose it through one corner or the bottom row, and in the range computed `t_rel` still grows about like the cell count: `ℓ²` for squares, and linearly in height at fixed width under the tide.

The relaxation time measures only the slowest mode. It is not the number of grains needed to come close to the steady state: for the riffle shuffle the slowest eigenvalue is `1/2` at every deck size, while about `(3/2) log₂ n` shuffles are needed to mix `n` cards ([[bayer-diaconis-1992-dovetail-shuffle](pages/bayer-diaconis-1992-dovetail-shuffle.md)]).[^10]

## Snippet

```python
import numpy as np
from math import lcm, log

def reduced_laplacian(c, model):           # cells (column, row); 'sink': bottom-left cell, 'tide': bottom row
    cells = [(i, j) for i, h in enumerate(c) for j in range(h)]
    sink = {(0, 0)} if model == 'sink' else {(i, 0) for i in range(len(c))}
    live = [v for v in cells if v not in sink]
    idx, cs = {v: k for k, v in enumerate(live)}, set(cells)
    L = [[0] * len(live) for _ in live]
    for (i, j) in live:
        for nb in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
            if nb in cs:
                L[idx[(i, j)]][idx[(i, j)]] += 1
                if nb in idx:
                    L[idx[(i, j)]][idx[nb]] -= 1
    return L

def snf_left(A):                           # d, P with P A Q = diag(d); only P is kept
    n, A = len(A), [r[:] for r in A]
    P = [[int(i == j) for j in range(n)] for i in range(n)]
    for t in range(n):
        while True:
            piv = min(((abs(A[i][j]), i, j) for i in range(t, n) for j in range(t, n) if A[i][j]), default=None)
            if piv is None:
                return [abs(A[i][i]) for i in range(n)], P
            _, pi, pj = piv
            A[t], A[pi], P[t], P[pi] = A[pi], A[t], P[pi], P[t]
            for r in A:
                r[t], r[pj] = r[pj], r[t]
            done = True
            for i in range(t + 1, n):
                q = A[i][t] // A[t][t]
                A[i] = [a - q * b for a, b in zip(A[i], A[t])]; P[i] = [a - q * b for a, b in zip(P[i], P[t])]
                done &= A[i][t] == 0
            for j in range(t + 1, n):
                q = A[t][j] // A[t][t]
                for r in A:
                    r[j] -= q * r[t]
                done &= A[t][j] == 0
            if done:
                bad = [i for i in range(t + 1, n) for j in range(t + 1, n) if A[i][j] % A[t][t]]
                if not bad:
                    break
                A[t] = [a + b for a, b in zip(A[t], A[bad[0]])]; P[t] = [a + b for a, b in zip(P[t], P[bad[0]])]
    return [abs(A[i][i]) for i in range(n)], P

def lambda_star(c, model='sink'):          # largest |eigenvalue| of Dhar's W over nontrivial characters
    L = reduced_laplacian(c, model)
    if not L:
        return 0.0
    d, P = snf_left(L)
    rows = [i for i in range(len(L)) if d[i] > 1]
    if not rows:
        return 0.0                         # trivial group: tree castle
    ds = [d[i] for i in rows]; E = lcm(*ds)
    M = np.array([[(P[i][v] % d[i]) * (E // d[i]) for v in range(len(L))] for i in rows], dtype=np.int64)
    k = np.indices(ds).reshape(len(ds), -1).T          # every character
    lam = np.abs(np.exp(2j * np.pi * ((k @ M) % E) / E).mean(axis=1))
    lam[0] = 0.0                                       # the trivial character
    return float(lam.max())

t_rel = lambda lam: 0.0 if lam == 0 else -1 / log(lam)
```

```
>>> round(lambda_star((2, 5)), 6), round(t_rel(lambda_star((3, 3, 3), 'tide')), 3)
(0.666667, 9.639)
>>> [round(t_rel(lambda_star((3,) * w, 'tide')), 3) for w in (3, 6)]
[9.639, 9.639]
>>> lambda_star((1, 2, 1, 3, 1)), lambda_star((1, 2, 1, 3, 1), 'tide')
(0.0, 0.0)
```

## Related Concepts

- [[sandpile-group](pages/sandpile-group.md)] - the two models, the group `K` and its matrices.
- [[sandpile-census](pages/sandpile-census.md)] - the groups of all 33,150 castles to 16 cells, the census this page reuses.
- [[castle-avalanches](pages/castle-avalanches.md)] - the mean avalanche `h(2h − 1)/6` under the tide, set against the linear relaxation time here.
- [[sandcastle-clock](pages/sandcastle-clock.md)] - the order of one element `e_v` of `K`; the relaxation time comes instead from the characters of `K`.
- [[castle-notation](pages/castle-notation.md)] - the sandpile symbols, `W`, `ψ`, `λ*`, `t_rel`, `n_live`.

## Appearances in Sources

- [[dhar-1990-self-organized-critical-sandpile](pages/dhar-1990-self-organized-critical-sandpile.md)] - the master equation, `W = Σ p_v a_v`, its eigenvalues from the phases, and the `ℓ^d` relaxation time.
- [[bayer-diaconis-1992-dovetail-shuffle](pages/bayer-diaconis-1992-dovetail-shuffle.md)] - a random walk on a group whose slowest eigenvalue does not give the mixing time.

## Footnotes

[^1]: [[dhar-1990-self-organized-critical-sandpile](pages/dhar-1990-self-organized-critical-sandpile.md)] p.1616 L269-295 [synthesis] - `P_t(C)` is the probability that the stable configuration after the `t`-th particle is `C`, with master equation `P_{t+1}(C) = Σ_{C'} W(C, C') P_t(C')` (eq. 22) and `W = Σ p_i a_i` (eq. 23); "The next largest eigenvalue determines the relaxation time of the slowest decaying fluctuations in the SOC state", which for the undirected `d`-dimensional model "varies as L^d", much larger than the avalanche duration (exponent read from the page image).
[^2]: [[dhar-1990-self-organized-critical-sandpile](pages/dhar-1990-self-organized-critical-sandpile.md)] pp.1614-1615 L102-177 [synthesis] - `a_j = exp(iφ_j)` with `Σ_j Δ_ij φ_j = 2πn_i`, solved by `φ_i = 2π Σ_j [Δ⁻¹]_ij n_j` (eqs. 10-12), and the number of such representations is `Det Δ` (eq. 13); p.1616 L285-289, the operators are simultaneously diagonalizable, so the eigenvalues of `W` are determined by these.
[^3]: Verified by execution (Python 3, NumPy, 2026-10-08): for 60 random castles to 10 cells and `(2, 2)`, `(3, 3)`, `(2, 2, 2)`, `(3, 3, 3)`, `(2, 3, 3, 2)`, `(2, 2, 1, 2, 2)`, in both models, the recurrent configurations were found by adding grains from the fullest stable pile, `W` was built with weight `1/n_live` per grain, and its second-largest eigenvalue modulus matched `λ*` from the character sum within `3.9 × 10⁻¹⁵`; the number of characters equalled the number of recurrent configurations in every case, and the Smith forms gave `Z/15`, `Z/8`, `Z/8 × Z/24`, `Z/95` for `(2, 2, 2)` sink and tide and `(3, 3, 3)` sink and tide, as on [[sandpile-census](pages/sandpile-census.md)].
[^4]: Verified by execution (2026-10-08, about 76 s): every castle to 16 cells (compositions, mirror images removed, 33,150), both models, all characters enumerated; 6,963 trivial groups in each model and `λ* < 1 − 10⁻¹²` for every other castle; the table rows, the per-cell rankings (`t_rel/n_live` with `n_live` = cells − 1 in the sink model, cells − width in the tide model) and the mirror-image comparison over the castles to 12 cells.
[^5]: Verified by execution (2026-10-08): `λ*` of `(2, h)` and `(h, 2)` in the sink model equals `(h − 1)/(h + 1)` within `10⁻¹²` for `h = 2, …, 30`, with `|K| = 4` throughout.
[^6]: Verified by execution (2026-10-08): over the census to 16 cells, the maximum of `|λ|` over the characters `φ = L̃⁻¹ e_u` falls short of `λ*` on 14,078 sink and 7,194 tide castles; over the castles to 12 cells with nontrivial group (1,372 per model), adding `φ = L̃⁻¹ (e_u ± e_v)` leaves 3 sink misses and 0 tide misses; on the tide rectangles of height 3 and widths 7, 8, 9 the pair bound is below the exact `λ*`.
[^7]: Verified by execution (2026-10-08): exact `λ*` by full character enumeration for tide rectangles of width 2, `h ≤ 14`, width 3, `h ≤ 8`, and height 2, `w ≤ 18`, and for the height-3 values quoted, all with `|K| ≤ 3 × 10⁷`; increments are successive differences of `t_rel`.
[^8]: Verified by execution (2026-10-08): the maximizing characters of `(3, 3, 3)` and `(3, 3, 3, 3, 3, 3)` under the tide, read off as phases in turns, are the patterns quoted, both with `λ* = 0.901455`; `t_rel` at height 3 is 9.639 at widths 3, 6 and 9.
[^9]: Verified by execution (2026-10-08): exact `λ*` for the sink rectangles `2 × w`, `w ≤ 13`, and the squares of side 2 to 4; the pair-character lower bound for rectangles up to width 12 and height 8, which agrees with the exact value on every sink rectangle where both were computed.
[^10]: [[bayer-diaconis-1992-dovetail-shuffle](pages/bayer-diaconis-1992-dovetail-shuffle.md)] §3 p.304 L612-L622 and §4 p.309 L903-L908 [synthesis] - multiplication by the 2-shuffle element has the distinct eigenvalues `1, 1/2, …, 1/2^{n−1}`, and about `(3/2) log₂ n` shuffles are needed to mix `n` cards.
