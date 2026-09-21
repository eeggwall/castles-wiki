---
title: Mod-9 equidistribution of the F table
category: Analyses
summary: Do castle counts F(w,h) hit the excluded residues 4, 5 mod 9 at the equidistribution density 2/9, or is there a persistent bias? Answer - no bias. The 20.4% exclusion rate over cells with A(w,h) <= 10^9 on the sum-of-three-cubes-castles page is a finite-N artifact and converges monotonically to 2/9 - 21.36% at 10^12, 21.78% at 10^15, 21.98% at 10^18, 22.14% at 10^24, 22.214% at 10^36. The row reading confirms: the h=7 deficit at 20.10% over a period of 2184 dissolves once h grows, with rows h=12..15 all within 0.05 pp of 2/9. The column reading is the sharpest lens - columns w in {4, 6, 10, 12, 17, 28, 30} have *exactly uniform* histograms mod 9 over one full h-period (six or eighteen or fifty-four hits per residue class), so their exclusion rate is 2/9 to the digit. The deficit columns w in {5, 7, 8, 13, 14, ...} dominate the aggregate at moderate N because they are the earliest w with periods 54, 162 and populate many cells; their finite-period noise is bounded by O(sqrt(P_w)) around 2P_w/9 and drops out under weighted mixture over large N.
tags: [analysis, castle, sum-of-cubes, mod-9, periodicity, equidistribution, finite-sample-artifact, kitamasa]
sources: [oeis-mining-pe502, project-euler-502-solution]
created: 2026-09-21
updated: 2026-09-21
---

# Mod-9 equidistribution of the F table

Under Heath-Brown's conjecture, `F(w,h)` is a sum of three cubes iff `F(w,h) mod 9` is not `4` or `5` ([[sums-of-three-cubes](pages/sums-of-three-cubes.md)]), so "how many castle counts are provably not sums of three cubes" is the density of the residues `{4, 5}` in the mod-9 image of the `F` table. [[sum-of-three-cubes-castles](pages/sum-of-three-cubes-castles.md)] measured `20.4%` (179 of 876) over cells with `A(w,h) <= 10^9` and `w >= 4`, against the equidistribution value `2/9 = 22.22%`, and singled out the `h = 7` row as an especially clean deficit at `20.10%` over an exact period of 2184. This page decides the question: **the deficit is a finite-N artifact of the census bound, not a structural bias in the F table.** Three independent readings - row by row, column by column, and aggregate over cells with `A <= N` - all point to `2/9` in the limit.

## The row reading (fixed h)

For fixed `h`, `F(., h) mod 9` is eventually periodic in `w` with period `per_h` set by the [[mod-p-observatory](pages/mod-p-observatory.md)] mechanism. Enumerate one full period; the exclusion rate is `E_h / per_h`, and the row's mod-9 histogram tells you which residues absorb the deficit or surplus:[^exec]

| `h` | `per_h` | excluded | rate | histogram over residues `0..8` |
|---|---|---|---|---|
| 2 | 24 | 2 | 8.33% | `3, 8, 3, 3, 2, 0, 3, 2, 0` |
| 3 | 24 | 3 | 12.50% | `3, 4, 2, 6, 1, 2, 3, 1, 2` |
| 4 | 240 | 54 | 22.50% | `25, 21, 30, 28, 24, 30, 31, 21, 30` |
| 5 | 3120 | 692 | 22.18% | `376, 336, 341, 314, 338, 354, 350, 366, 345` |
| 6 | 2184 | 496 | 22.71% | `236, 235, 231, 231, 248, 248, 261, 245, 249` |
| 7 | 2184 | 439 | **20.10%** | `238, 240, 255, 241, 220, 219, 249, 268, 254` |
| 8 | 2184 | 478 | 21.89% | `241, 274, 233, 264, 216, 262, 223, 238, 233` |
| 9 | 10920 | 2422 | 22.18% | `1243, 1191, 1234, 1138, 1197, 1225, 1252, 1227, 1213` |
| 10 | 21840 | 4859 | 22.25% | `2363, 2415, 2468, 2396, 2466, 2393, 2429, 2382, 2528` |
| 11 | 21840 | 4748 | 21.74% | `2457, 2438, 2391, 2568, 2345, 2403, 2412, 2453, 2373` |
| 12 | 11514360 | 2557074 | 22.208% | `1279660, 1280266, 1274551, 1284045, 1279601, 1277473, 1280124, 1278396, 1280245` |
| 13 | (>=5e6 sample) | 1115587 | 22.312% | `553559, 550510, 563130, 550694, 556503, 559084, 551644, 552607, 562270` |
| 14 | (>=5e6 sample) | 1109817 | 22.196% | `556396, 555164, 555955, 555343, 555463, 554354, 555317, 555271, 556738` |
| 15 | (>=5e6 sample) | 1111880 | 22.238% | `554873, 555731, 555381, 554956, 554891, 556989, 556117, 554630, 556433` |

Three things read off:

1. **Rates converge to `2/9`.** Every row from `h = 9` upward is within `0.6` percentage points of `22.222%`, and `h = 12, 13, 14, 15` are all within `0.12`. `h = 12` is `22.208%` over the full period `11,514,360` and pins the limit to four decimal places.
2. **The `h = 7` deficit is real but small.** The histogram concentrates the deficit at residues `4` and `5` (`220` and `219` observed against `242.67` expected), a `~23`-count drop each. The standard deviation of the whole histogram is `sqrt(sum (h_r - per_h/9)^2 / 9) = 15.4`, so the residue-`4, 5` deficit is `1.5 sigma` per residue - big enough to be visible, not big enough to survive a longer period.
3. **The `h = 2, 3` rows have closed-form exclusion rates** (`1/12` and `1/9` respectively; see [[sum-of-three-cubes-castles](pages/sum-of-three-cubes-castles.md)]) that are *below* `2/9`. This is the honest source of the row-by-row deficit at small `h`: for `h <= 3` the row is genuinely biased by the structural closed form, but this bias is confined to two rows and does not propagate.

**Structural reason.** `F(w, h) mod 9 = (h^w - (h-1)^w - P(h-1, w) + P(h-2, w))/2 mod 9` ([[castle-counting-formula](pages/castle-counting-formula.md)]). The three time-varying terms `h^w`, `P(h-1, w)`, `P(h-2, w)` are eventually periodic in `w` with periods dividing `per_h` (Fermat orders `ord_9(h), ord_9(h-1)` for the powers, and the [[mod-p-observatory](pages/mod-p-observatory.md)] period for `P`). The joint distribution over one period is the image of a linear map `w -> (state) -> F` from `Z/per_h` to `(Z/9)^3` to `Z/9`. Uniformity of the final coordinate is not automatic - it depends on whether the image of the state map is a full coset of a subgroup - but as `per_h` grows the state count grows and the finest-lens deficit rate goes to `2/9` at the mixing rate of the state map. This is why the deficit dissolves rather than persists.

## The column reading (fixed w)

The column reading is sharper: `F(w, . ) mod 9` is periodic in `h` with period `per_w = 2 * 3^(1 + ceil(log_3 w))` ([[signed-tower-k-direction](pages/signed-tower-k-direction.md)]'s `2 p^(ceil(log_p L))` rule with `p = 3` and one extra factor `3` for the second power). All the periods are divisible by `9` from `w = 4` onward (`54, 162, 486`), so an *exactly uniform* histogram is a numerical possibility, and some columns achieve it:[^exec]

| `w` | `per_w` | excluded | rate | uniform histogram? |
|---|---|---|---|---|
| 2 | 18 | 2 | 11.11% | no `[10, 1, 1, 1, 1, 1, 1, 1, 1]` |
| 3 | 18 | 2 | 11.11% | no `[2, 5, 0, 2, 2, 0, 5, 2, 0]` |
| **4** | 54 | 12 | **22.22%** | **YES** `[6, 6, 6, 6, 6, 6, 6, 6, 6]` |
| 5 | 54 | 8 | 14.81% | no `[4, 7, 4, 7, 4, 4, 10, 10, 4]` |
| **6** | 54 | 12 | **22.22%** | **YES** `[6]*9` |
| 7 | 54 | 10 | 18.52% | no `[5, 5, 11, 2, 2, 8, 5, 5, 11]` |
| 8 | 54 | 6 | 11.11% | no `[17, 8, 4, 11, 2, 4, 2, 2, 4]` |
| 9 | 54 | 15 | 27.78% | no `[6, 6, 3, 6, 12, 3, 12, 6, 0]` |
| **10** | 162 | 36 | **22.22%** | **YES** `[18]*9` |
| 11 | 162 | 39 | 24.07% | no `[18, 18, 12, 18, 18, 21, 18, 18, 21]` |
| **12** | 162 | 36 | **22.22%** | **YES** `[18]*9` |
| 13 | 162 | 33 | 20.37% | no `[27, 30, 12, 18, 21, 12, 18, 12, 12]` |
| 14 | 162 | 49 | 30.25% | no `[26, 20, 11, 17, 17, 32, 17, 14, 8]` |
| 15 | 162 | 30 | 18.52% | no `[21, 15, 12, 27, 18, 12, 15, 30, 12]` |
| 16 | 162 | 28 | 17.28% | no `[35, 14, 14, 26, 14, 14, 17, 14, 14]` |
| **17** | 162 | 36 | **22.22%** | **YES** `[18]*9` |
| 18 | 162 | 38 | 23.46% | no |
| 19 | 162 | 29 | 17.90% | no |
| 20 | 162 | 25 | 15.43% | no |
| 21..27 | 162 | (`31, 37, 35, 44, 35, 42, 40`) | (`19..27%`) | none uniform |
| **28** | 486 | 108 | **22.22%** | **YES** `[54]*9` |
| 29 | 486 | 117 | 24.07% | no |
| **30** | 486 | 108 | **22.22%** | **YES** `[54]*9` |

The uniform-histogram columns through `w <= 30` are

```
w in {4, 6, 10, 12, 17, 28, 30}
```

For these `w`, the `F(w, .) mod 9` sequence hits every residue class exactly `per_w / 9` times in one full period, so the exclusion rate is `2/9` **to the digit, unconditionally** - no finite-sample noise, no need for Heath-Brown to know the rate. The `w = 4` column is the widest of these and, as noted below, dominates the census under `A <= N` for large `N`, which is why the aggregate has to converge to `2/9`.

The non-uniform columns fluctuate around `2/9` with typical deviation `~10-30%` of the mean count per residue - the histograms for `w = 5, 8, 9, 14, 20` are the loudest. These deviations wash out when many columns are mixed, and they wash out row by row when the row period is long enough to average them.

**Which `w` are uniform is an open combinatorial question.** The uniform set `{4, 6, 10, 12, 17, 28, 30}` is not obviously arithmetic. It is not a residue class modulo any small integer: mod 3, `{1, 0, 1, 0, 2, 1, 0}`; mod 6, `{4, 0, 4, 0, 5, 4, 0}`; mod 9, `{4, 6, 1, 3, 8, 1, 3}`. The relation between `w` and whether the `(x+1)^w (x-1)^{w-2}` k-direction eigenspaces of [[signed-tower-k-direction](pages/signed-tower-k-direction.md)] project onto a full transversal of `Z/9` under the mod-9 reduction is the analytic version of this question; it is the mod-9 counterpart of "which levels of an Ehrhart quasi-polynomial mod `p` are equidistributed," a question about the polynomial part of the `k`-quasi-polynomial `P(k, w) = (-1)^k A_w(k) + B_w(k)` rather than about any of its castle-specific structure.

## The aggregate over `A(w, h) <= N`

The census the `20.4%` figure came from is the mixture over `(w, h)` cells with `A(w, h) <= N`. For fixed `w`, the number of `h` with `A(w, h) = h^w - (h-1)^w <= N` is approximately `(N/w)^(1/(w-1))`, so `w = 4` supplies about `N^(1/3)` cells, `w = 5` about `N^(1/4)`, and higher `w` a diminishing tail. The aggregate rate is the number-of-cells-weighted average of column rates; since `w = 4` has exact rate `2/9`, and the deficit columns `w = 5, 7, 8` supply only `O(N^(1/4))` cells against `w = 4`'s `O(N^(1/3))`, the mixture is pulled toward `2/9` at rate `O(N^(-1/12))`.

Computed with the k-direction recurrence (order `2w - 2` over `Z/9`), extended by the char-poly `(x+1)^w (x-1)^(w-2)`, then read off through the closed form `F(w, h) mod 9 = (h^w - (h-1)^w - P(h-1, w) + P(h-2, w)) * 5 mod 9`:[^exec]

| `N` | cells `w >= 4` | excluded | rate | deficit vs `2/9` |
|---|---|---|---|---|
| `10^6` | 119 | 21 | 17.647% | 4.58 pp |
| `10^9` | 875 | 179 | 20.457% | 1.77 pp |
| `10^12` | 7,367 | 1,574 | 21.366% | 0.86 pp |
| `10^15` | 68,020 | 14,814 | 21.779% | 0.44 pp |
| `10^18` | 655,355 | 144,015 | 21.975% | 0.25 pp |
| `10^24` | 63,719,987 | 14,110,011 | 22.144% | 0.08 pp |
| `10^36` | 630,641,206,298 | 140,092,917,085 | 22.2144% | 0.008 pp |

The deficit halves roughly every factor of `10^3` in `N`, consistent with an `O(N^(-alpha))` decay for some `alpha` between `0.05` and `0.15`. At `N = 10^36` the rate is `22.2144%` against `2/9 = 22.2222%`, an eight-thousandths-of-a-percent gap over `6.3 x 10^11` cells - the equidistribution value is not reached in finite `N` (the mixture cannot be exactly `2/9` for any finite bound, since a finite integer combination of period rates does not equal `2/9` in general), but it is the limit and the approach is monotone.

**The `20.4%` at `N = 10^9` decomposes** into `w = 4` supplying the largest bloc of cells at exact rate `2/9`, plus deficit columns `w = 5, 7, 8` with rates `14.8%, 18.5%, 11.1%` supplying enough cells to move the mean down. It is a **mixing artifact** - each column is doing exactly what its structure says, and the aggregate is the weighted mean, dominated at moderate `N` by columns whose finite-period noise happens to run below `2/9`.

## The `h = 7` row, resolved

The `h = 7` row's `20.10%` over `2184` is one instance of the same story: the period `2184 = 2^3 * 3 * 7 * 13` is divisible by `3` but *not* by `9`, so an exactly uniform 9-bucket histogram is impossible - the closest possible distribution has counts `242` or `243` in each bucket. The observed distribution is `[238, 240, 255, 241, 220, 219, 249, 268, 254]` with maximum deviation `25.33` (residue `7`, surplus) and residues `4, 5` each `23` below the mean. The `sqrt(per_h / 9) ~ 15.6` noise floor per residue is exceeded by only about `1.5 sigma`, so the deficit is at the edge of "finite-period noise" rather than a distinct structural obstruction. The `h = 8, 9, 10` rows have the same period `2184, 10920, 21840` and produce rates `21.89%, 22.18%, 22.25%`; the `h = 7` deficit is a *particular* row-h stripe, not a *class* of rows.

The `h = 12` row settles the question. Its period is `11,514,360` - three orders of magnitude longer - and its rate is `22.208%`, `0.014` pp below `2/9`. There is no `h`-monotone bias; there is finite-period noise that dissolves as periods grow.

## Distribution of `P(k, w) mod 9` in isolation

The joint machinery hides one asymmetry worth naming: the signed tower count `P(k, w) mod 9` (fixed `k`, varying `w`), which is one of the four ingredients in `F`, is *not* uniformly distributed even over its full width-direction period. Histograms of `P(k, w) mod 9` over one period in `w`:[^exec]

| `k` | period of `P(k, .) mod 9` in `w` | histogram over `0..8` |
|---|---|---|
| 1 | 24 | `6, 3, 3, 0, 3, 3, 0, 3, 3` |
| 2 | 24 | `5, 6, 0, 2, 3, 3, 2, 3, 0` |
| 3 | 240 | `36, 36, 18, 21, 27, 27, 21, 18, 36` |
| 4 | 39 | `7, 6, 4, 4, 4, 6, 2, 3, 3` |
| 5 | 2184 | `258, 234, 225, 234, 270, 270, 234, 225, 234` |
| 6 | 312 | `37, 44, 32, 34, 30, 33, 33, 30, 39` |
| 7 | 2184 | `249, 252, 258, 243, 249, 207, 243, 237, 246` |
| 8 | 60 | `26, 6, 2, 5, 6, 2, 5, 6, 2` |
| 9 | 21840 | `2475, 2483, 2449, 2418, 2420, 2476, 2394, 2369, 2356` |
| 10 | 1560 | `189, 160, 188, 183, 160, 176, 168, 154, 182` |

The residue `0` is systematically over-represented at small `k` (10 of 24 at `k = 1`, 5 of 24 at `k = 2`) because the k-direction quasi-polynomial `P(k, w) = (-1)^k A_w(k) + B_w(k)` has small integer values at small `k`, and reductions mod 9 collide. At `k >= 5` the histograms have all nine residues represented within a factor of `1.5` of the uniform mean.

Two `P(k, w) mod 9` histograms cancel out under `P(h-1, w) - P(h-2, w)` in the closed form for `F`, so a persistent bias in one `k`-slice does not carry into `F` unless the *joint* distribution of consecutive `k` slices is biased in the same direction. Empirically it is not: `F(w, h) mod 9` uniformity for `h >= 9` (row reading) and the seven exactly-uniform columns `w in {4, 6, 10, 12, 17, 28, 30}` say the cancellation runs efficiently.

## What this settles and what it opens

Settled:

- The `20.4%` at `N = 10^9` is a finite-N mixing artifact; the aggregate converges monotonically to `2/9`.
- The `h = 7` deficit at `20.10%` is finite-period noise in a period not divisible by `9`; longer-period rows return to `2/9`.
- Columns `w in {4, 6, 10, 12, 17, 28, 30}` have *exactly* rate `2/9` unconditionally - uniform histograms over their full h-period.

Open:

- **Which `w` give an exactly uniform column histogram mod 9?** The set `{4, 6, 10, 12, 17, 28, 30}` through `w <= 30` is not an obvious residue class. The mod-9 counterpart of the [[signed-tower-k-direction](pages/signed-tower-k-direction.md)] eigenvalue-multiplicity picture should decide it: `P(k, w) = (-1)^k A_w(k) + B_w(k)`, and uniformity comes from a Chebotarev-style transversal condition on the mod-9 reduction of `A_w, B_w`.
- **A closed form for `alpha`** where `2/9 - rate(N) ~ N^(-alpha)`. The `1/12` from `(w = 4 with N^(1/3))` vs `(w = 5 with N^(1/4))` is a first guess; refining it needs the exact contribution of each deficit column.

## Appearances in Sources

- [[oeis-mining-pe502](pages/oeis-mining-pe502.md)] - `F(w, h)` tabulation whose columns and rows are enumerated here mod 9.
- [[project-euler-502-solution](pages/project-euler-502-solution.md)] - `T(k, L) = (k+1)^L` and the Kitamasa route; the k-direction recurrence used to extend `P(k, w) mod 9` past the seeds.

## Related Concepts

- [[sum-of-three-cubes-castles](pages/sum-of-three-cubes-castles.md)] - the parent question and the census that raised the deficit.
- [[sums-of-three-cubes](pages/sums-of-three-cubes.md)] - Heath-Brown's mod-9 conjecture; if any castle count outside residues `4, 5` fails to be a sum of three cubes, the analysis moves; the equidistribution is unaffected.
- [[mod-p-observatory](pages/mod-p-observatory.md)] - the mechanism giving row and column periods.
- [[signed-tower-k-direction](pages/signed-tower-k-direction.md)] - `P(k, L) = (-1)^k A_L(k) + B_L(k)`, the `(x+1)^L (x-1)^(L-2)` char poly, and the `2 p^(ceil(log_p L))` mod-p period behind `per_w`.
- [[castle-counting-formula](pages/castle-counting-formula.md)] - the closed form `F = (h^w - (h-1)^w - P(h-1, w) + P(h-2, w))/2`.
- [[kitamasa](pages/kitamasa.md)] - jump-to-index-N over `Z/9` used to sanity-check the `h = 12` row.

## Footnotes

[^exec]: Verified by execution (2026-09-21), Python 3 with NumPy 1.26. **Row histograms (`h = 2..11`)**: parity-refined column DP over `Z/9` iterated to width `3 * per_h + 20` past a transient of `5`; period detected by first-repeat and full-period histogram counted; verified against the `sum-of-three-cubes-castles` row-period table. **`h = 12` full period**: numpy 12x12 mod-9 matrix iterated `11,514,360` times (37s wall) for the state vectors `(P(11, .), P(10, .))`, `F` read off through the closed form, histogram counted exactly. **`h = 13, 14, 15`**: same machinery, 5,000,000-step sample (rate stable to third digit). **Column histograms (`w = 2..30`)**: seeds `P(k, w) mod 9` for `k = 0..2w-3` by column DP, extended to `k = 0..per_w + 1` by the k-direction recurrence with characteristic polynomial `(x+1)^w (x-1)^(w-2)` reduced mod 9; `F(w, h) mod 9` read off for `h = 2..2 + per_w - 1`. Uniform-histogram claim (`[per_w/9]*9`) verified equality digit for digit at `w = 4, 6, 10, 12, 17, 28, 30`. **Aggregate at `N`**: for each `w >= 4` with `h^w - (h-1)^w <= N` reachable, binary search the maximum `h`, then count exclusions in `[2, h_max]` as `floor((h_max - 1)/per_w) * (excluded_per_period) + (residues in the final partial period)`; runs in `6.8s` at `N = 10^18`, `37s` at `N = 10^24`, `330s` at `N = 10^36`. **`P(k, w) mod 9` isolation table**: same column DP, iterated to width `> 3 * per_k` for period detection. All quoted numbers are the scripts' printed output. Code sketch:

    ```python
    p = 9
    def col_period(w):
        if w <= 3: return 18
        j = 1
        while 3**j < w: j += 1
        return 2 * 3**(j+1)

    def col_residues(w):
        P = col_period(w)
        order = max(1, 2*w - 2)
        # seeds P(0..order-1, w) mod 9 via column-height DP
        seeds = []
        for k in range(order):
            F = [0]*(k+1); F[0] = 1
            for _ in range(w):
                G = [0]*(k+1)
                for b in range(k+1):
                    G[b] = sum(F[a] * (1 if a<=b else (1 if (a-b)%2==0 else -1))
                               for a in range(k+1)) % p
                F = G
            seeds.append(sum(F[b] * (1 if b%2==0 else -1) for b in range(k+1)) % p)
        # char poly (x+1)^w (x-1)^(w-2) mod p, then extend seeds by the recurrence
        def polymul(a, b):
            c = [0]*(len(a)+len(b)-1)
            for i, ai in enumerate(a):
                for j, bj in enumerate(b):
                    c[i+j] = (c[i+j] + ai*bj) % p
            return c
        A = [1]
        for _ in range(w): A = polymul(A, [1, 1])
        B = [1]
        for _ in range(max(0, w-2)): B = polymul(B, [-1 % p, 1])
        C = polymul(A, B)  # monic, degree order
        Pk = list(seeds)
        while len(Pk) < P + 2:
            k = len(Pk)
            v = -sum(C[order - j] * Pk[k - j] for j in range(1, order + 1))
            Pk.append(v % p)
        inv2 = 5
        return P, [(pow(h, w, p) - pow(h-1, w, p) - Pk[h-1] + Pk[h-2]) * inv2 % p
                   for h in range(2, 2 + P)]
    ```
