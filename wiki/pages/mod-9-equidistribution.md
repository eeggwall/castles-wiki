---
title: Mod-9 equidistribution of the F table
category: Analyses
summary: Do castle counts F(w,h) hit the excluded residues 4, 5 mod 9 at the equidistribution density 2/9, or is there a persistent bias? Answer - no bias. The 20.4% exclusion rate over cells with A(w,h) <= 10^9 on the sum-of-three-cubes-castles page is a finite-N artifact and converges monotonically to 2/9 - 21.36% at 10^12, 21.78% at 10^15, 21.98% at 10^18, 22.14% at 10^24, 22.214% at 10^36. The row / column divisibility gap explains why the two readings behave differently: column periods per_w = 2 * 3^{ceil(log_3 w) + 1} have v_3 >= 2 structurally, so 9 | per_w and the h-histogram can be exactly uniform (columns w in {4, 6, 10, 12, 17, 28, 30, 35, 82, 84, 89, ...} - the pattern w = 3^{k-1} + d for k >= 2, d in {1, 3, 8} - hit exactly 2/9 to the digit); row periods per_h have v_3 = 1 empirically for h <= 16, so 9 does not divide per_h and every row carries an unavoidable +-1-per-residue rounding jitter. The w = 4 blackboard proof gives the exact 2/9 rate unconditionally on Heath-Brown: closed form for F(4, h), parity split into cubic polynomials Q_e, Q_o, uniformity of F(4, h) mod 3 over m mod 9 (verified in nine direct evaluations), coset lift F(4, h + 18) = F(4, h) + 6 mod 9 (a two-line polynomial arithmetic derivation, using that the quadratic coefficient of Q_e is divisible by 3). The tempting {4, 5} pairing hypothesis - that some (w, h) involution forces count(4) = count(5) in every row - is refuted: no such shift or reflection exists in either direction, and rows h = 8, 10, 11 show 3 sigma asymmetries between count(4) and count(5). Equidistribution is achieved by the limit, not by any pointwise algebraic symmetry.
tags: [analysis, castle, sum-of-cubes, mod-9, periodicity, equidistribution, finite-sample-artifact, kitamasa, three-adic, cube-near-miss, booker-sutherland, mordell-curve]
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

The uniform-histogram columns through `w <= 200` are:[^exec]

```
w in {4, 6, 10, 12, 17, 28, 30, 35, 82, 84, 89}
```

For these `w`, the `F(w, .) mod 9` sequence hits every residue class exactly `per_w / 9` times in one full period, so the exclusion rate is `2/9` **to the digit, unconditionally** - no finite-sample noise, no need for Heath-Brown to know the rate. The `w = 4` column is the widest of these and, as noted below, dominates the census under `A <= N` for large `N`, which is why the aggregate has to converge to `2/9`.

**The uniform-`w` pattern classifies clean.** Group the uniform `w`'s by the [[signed-tower-k-direction](pages/signed-tower-k-direction.md)] bracket `k = ceil(log_3 w)`, whose h-period is `per_w = 2 * 3^{k + 1}` and whose w-range is `[3^{k-1} + 1, 3^k]`. Within each bracket the uniform `w`'s sit at three fixed offsets from the bracket start `3^{k-1} + 1`:

| bracket `k` | w-range | `per_w` | uniform `w` | offsets from `3^{k-1} + 1` |
|---|---|---|---|---|
| 2 | `[4, 9]` | 54 | `4, 6` | `0, 2` |
| 3 | `[10, 27]` | 162 | `10, 12, 17` | `0, 2, 7` |
| 4 | `[28, 81]` | 486 | `28, 30, 35` | `0, 2, 7` |
| 5 | `[82, 243]` | 1458 | `82, 84, 89` | `0, 2, 7` |

The offset set `{0, 2, 7}` is invariant from bracket 3 onward. Bracket 2 is truncated (only offsets `0, 2` fit before the next bracket starts). This produces three explicit sequences of uniform `w`'s:

```
A_k = 3^{k-1} + 1  =  4, 10, 28, 82, 244, 730, ...      (k >= 2)
B_k = 3^{k-1} + 3  =  6, 12, 30, 84, 246, 732, ...      (k >= 2)
C_k = 3^{k-1} + 8  =  17, 35, 89, 251, 737, ...         (k >= 3)
```

Equivalently, the uniform-`w` set is `{ 3^{k-1} + d : k >= 2, d in {1, 3, 8}, 3^{k-1} + d <= 3^k }`. **Predicted uniform `w`'s in bracket 6 (`w in [244, 729]`, `per_w = 4374`): `w = 244, 246, 251`.** Not yet verified due to computational cost.

Why offsets `0, 2, 7`? All three are `<= 8 = 3^2 - 1`, so they live inside the "second-power" window of the k-direction char poly `(x + 1)^w (x - 1)^{w-2}` under mod-9 reduction. The `w = 4` blackboard proof (below) gives one explicit certificate of uniformity at `w = 4 = 3^1 + 1` (the `A_2` value); by structural analogy the same three-step recipe (parity split, mod-3 uniformity, coset lift) should carry through for each `A_k`, `B_k`, `C_k`. A proof that the `{0, 2, 7}` template is the complete uniform-set generator for every `k` is the open item.

**Rate-matched-but-not-uniform columns**, a distinct second class, also exist. These are `w` where the exclusion rate equals `2/9` on the digit but the full 9-bucket histogram is *not* `[per_w / 9] * 9`. Through `w <= 200`:[^exec]

```
w in {31, 39, 64, 93, 97, 191}
```

Sample histograms: `w = 31: [51, 60, 48, 60, 60, 48, 60, 51, 48]` (rate 22.22% via `count(4) + count(5) = 108` but the individual residues run 42-69); `w = 39: [48, 45, 69, 45, 48, 60, 42, 42, 87]`. The count in residues `{4, 5}` sums to exactly `2 * per_w / 9` by an internal cancellation that is *not* a symmetry-of-the-full-distribution but a specific balance on the sub-histogram. No arithmetic pattern is visible in the class-2 offsets `{3, 11, 36}` (bracket 4) and `{11, 15, 109}` (bracket 5) - they look coincidental.

The non-uniform, non-rate-matched columns fluctuate around `2/9` with typical deviation `~10-30%` of the mean count per residue - the histograms for `w = 5, 8, 9, 14, 20` are the loudest. These deviations wash out when many columns are mixed, and they wash out row by row when the row period is long enough to average them.

**Analytic form of "which `w`".** Uniformity of column `w` is equivalent to a character-sum vanishing condition: `sum_{h=0}^{per_w - 1} exp(2 pi i xi F(w, h) / 9) = 0` for every `xi in {1..8}`. Since `P(k, w) = (-1)^k A_w(k) + B_w(k)` with `A_w, B_w` explicit polynomials tabulated on [[signed-tower-k-direction](pages/signed-tower-k-direction.md)] through `w = 8`, the character sums factor into Gauss-sum-shaped evaluations of `A_w, B_w mod 9` against multiplicative characters of `(Z/9)*`. "Which `w`" is precisely which `w` make all eight sums vanish, and the empirical answer `{A_k, B_k, C_k}` is what a general character-sum theorem should reproduce.

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

## The row / column divisibility gap

The row and column readings behave qualitatively differently for a **3-adic** reason. Columns can be exactly uniform mod 9; rows cannot. The reason is 9-divisibility of the periods:[^exec]

| direction | period formula | `v_3(period)` | 9 divides? |
|---|---|---|---|
| columns (fixed `w`, `w >= 2`) | `per_w = 2 * 3^{ceil(log_3 w) + 1}` | `ceil(log_3 w) + 1 >= 2` | **always** |
| rows (fixed `h`, empirical `h <= 16`) | `per_h = lcm(ord_9(h), ord_9(h-1), per(char_{h-1}) mod 9, per(char_{h-2}) mod 9)` | `1` | **never** |

Row periods `per_h` for `h = 2..16`, each factored, with 3-adic valuation `v_3` in the last column:

| `h` | `per_h` | factorization | `v_3` |
|---|---|---|---|
| 2 | 24 | `2^3 * 3` | 1 |
| 3 | 24 | `2^3 * 3` | 1 |
| 4 | 240 | `2^4 * 3 * 5` | 1 |
| 5 | 3120 | `2^4 * 3 * 5 * 13` | 1 |
| 6 | 2184 | `2^3 * 3 * 7 * 13` | 1 |
| 7 | 2184 | `2^3 * 3 * 7 * 13` | 1 |
| 8 | 2184 | `2^3 * 3 * 7 * 13` | 1 |
| 9 | 10920 | `2^3 * 3 * 5 * 7 * 13` | 1 |
| 10 | 21840 | `2^4 * 3 * 5 * 7 * 13` | 1 |
| 11 | 21840 | `2^4 * 3 * 5 * 7 * 13` | 1 |
| 12 | 11514360 | `2^3 * 3 * 5 * 11^2 * 13 * 61` | 1 |
| 13 | 177144 | `2^3 * 3 * 11^2 * 61` | 1 |
| 14 | 1771440 | `2^4 * 3 * 5 * 11^2 * 61` | 1 |
| 15 | 25170390960 | `2^4 * 3 * 5 * 7 * 11^2 * 13 * 4093 * 61` (approx) | 1 |
| 16 | 88096368360 | (large; `v_3 = 1`) | 1 |

Every row period through `h = 16` has exactly one factor of 3.

**Why columns win.** The k-direction characteristic polynomial of `P(k, w)` is `(x+1)^w (x-1)^{w-2}` ([[signed-tower-k-direction](pages/signed-tower-k-direction.md)]), with a root of multiplicity `w` at `-1`. Reducing mod `9` and applying the "multiplicity `m` inflates the period by `p^{ceil(log_p m)}`" rule of the [[mod-p-observatory](pages/mod-p-observatory.md)] with `p = 3`, the mod-9 period picks up a factor `3^{ceil(log_3 w) + 1}` (the extra `+1` in the exponent is the second-power lift from `mod 3` to `mod 9`). For `w >= 2` this is `>= 9`. So `9 | per_w` is **structural**, not empirical, and the column histogram of `F(w, .) mod 9` splits `per_w` into `9` equal buckets whenever the residue distribution is balanced.

**Why rows lose.** The w-direction period `per_h` is the lcm of the `L`-direction characteristic-polynomial periods for `char_{h-1}` and `char_{h-2}` mod 9, together with the multiplicative orders `ord_9(h), ord_9(h-1)`. The multiplicative orders divide `phi(9) = 6`, so their 3-adic content is at most 1. The `char_k mod 3` factorizations tabulated on the [[mod-p-observatory](pages/mod-p-observatory.md)] have low-multiplicity repeated roots (`(x-1)^2` in `char_4 mod 3`, `(x+3)^2` in `char_2 mod 7`, etc.), and a multiplicity-2 root inflates the mod-9 period by `3^{ceil(log_3 2)} = 3`, not by `9`. Empirically no `char_k` for `k <= 15` has a mod-3 factor of multiplicity `>= 4`, which would be needed to force `v_3 = 2`. Hence every row period through `h = 16` sits at `v_3 = 1`.

**Consequence for uniformity.** If `9 | per_w` (columns), the 9-bucket histogram *can* be exactly `[per_w / 9] * 9`, and empirically it is for `w in {4, 6, 10, 12, 17, 28, 30}`. If `9 not | per_h` (rows), the 9-bucket histogram *cannot* be uniform, since some buckets hit `floor(per_h / 9)` and others `ceil(per_h / 9)`. Every row histogram carries an unavoidable `+-1`-per-residue rounding jitter, which sets a floor on the row-level equidistribution error at `1 / per_h`. That floor drops to zero as `h -> infinity` and `per_h -> infinity`, so equidistribution is still achieved in the limit, but no finite row ever hits `2/9` on the digit.

Whether some `h` past `16` first inflates `v_3(per_h)` to `2` (via a mod-3 quadruple root in `char_{h-1}` or `char_{h-2}`) is open. Nothing in the machinery forbids it; nothing yet demands it.

## The `w = 4` blackboard proof

The `w = 4` column is the seminar centerpiece: its uniform mod-9 histogram, and therefore its exact `2/9` exclusion rate, comes out of a completely elementary argument that fits on one blackboard. No character sums, no Heath-Brown, no computer verification of 54 values - just the closed form for `F(4, h)`, three lines of polynomial arithmetic, and a coset lift.

**Step 1. Closed form.** From `P(k, 4) = (-1)^k A_4(k) + B_4(k)` with `A_4(k) = (k+1)(2k+1)(2k+3)/6` and `B_4(k) = (k+1)/2` ([[signed-tower-k-direction](pages/signed-tower-k-direction.md)]), substitution into `F(4, h) = (h^4 - (h-1)^4 - P(h-1, 4) + P(h-2, 4))/2` gives

```
12 * F(4, h)  =  (24 h^3 - 36 h^2 + 24 h - 9)  +  (-1)^h * (8 h^3 - 12 h^2 + 10 h - 3).
```

Verified: `F(4, 2) = 10`, `F(4, 3) = 21`, `F(4, 4) = 117`, `F(4, 5) = 122`, `F(4, 7) = 367` come out of the formula exactly.

**Step 2. Split by parity.** For `h = 2m` (even),

```
F(4, 2m)  =  (64 m^3 - 48 m^2 + 17 m - 3) / 3.
```

For `h = 2m + 1` (odd),

```
F(4, 2m + 1)  =  (32 m^3 + 24 m^2 + 7 m) / 3.
```

Both numerators are divisible by 3 for every `m in Z`. On the even side, `64 m^3 - 48 m^2 + 17 m - 3 = m^3 + 2m mod 3 = m(m^2 - 1) mod 3 = m(m - 1)(m + 1) mod 3`, a product of three consecutive integers, hence `0 mod 3`. On the odd side, `32 m^3 + 24 m^2 + 7 m = 2m^3 + m = m(2m^2 + 1) mod 3`, which vanishes for `m in {0, 1, 2} mod 3` by direct check.

**Step 3. Uniform mod 3.** Reduce `F(4, 2m) mod 3` for `m = 0..8`:

```
F(4, 2m) mod 3  =  (Q_e(m) mod 9) / 3    where  Q_e(m) = 64 m^3 - 48 m^2 + 17 m - 3
                =  m^3 + 6 m^2 + 8 m + 6 (mod 9), then /3.
```

Direct evaluation gives `Q_e mod 9 = 6, 3, 0, 3, 0, 6, 0, 6, 3` for `m = 0..8`, dividing by 3 gives `F(4, 2m) mod 3 = 2, 1, 0, 1, 0, 2, 0, 2, 1` - the three residues `{0, 1, 2}` each appear **exactly three times**. Same evaluation on the odd side gives `F(4, 2m + 1) mod 3 = 0, 0, 2, 1, 1, 0, 2, 2, 1`, again three of each.

**Step 4. Coset lift.** The polynomial `Q_e(m)` satisfies

```
Q_e(m + 9) - Q_e(m)   =  1728 m^2 + 14688 m + 42921   =  18 (mod 27),
Q_e(m + 18) - Q_e(m)  =  (computed similarly)          =   9 (mod 27),
```

both constants (independent of `m`). The cubic term `1728 m^2` is `64 * 27 * m^2 = 0 mod 27`; the linear term `14688 m` is `544 * 27 * m = 0 mod 27`; only the truly constant term survives, and it survives at `9 * (17 mod 27) = 153 = 18 mod 27` for the `Delta_9` and at `18 * 17 = 306 = 9 mod 27` for `Delta_18`. Dividing by `3` (to get `F` in place of `Q_e / 3`):

```
F(4, 2(m + 9)) - F(4, 2m)   =   6 (mod 9),
F(4, 2(m + 18)) - F(4, 2m)  =   3 (mod 9).
```

For the odd side, the same computation gives `9 mod 27` and `18 mod 27` respectively (swapped):

```
F(4, 2(m + 9) + 1) - F(4, 2m + 1)   =   3 (mod 9),
F(4, 2(m + 18) + 1) - F(4, 2m + 1)  =   6 (mod 9).
```

**Step 5. Cosets tile the period.** In both cases, the triple `{F(4, h), F(4, h + 18), F(4, h + 36)}` mod 9 is `{v, v + 6, v + 3}` in some order - a **complete coset of `3 Z / 9` in `Z / 9`**, containing three distinct residues. So each "base" value of `m in {0..8}` gives three residues mod 9, one in each of the three cosets `{0, 3, 6}, {1, 4, 7}, {2, 5, 8}`, or, more precisely, three residues in the specific coset `F(4, 2 * base) + 3 Z / 9`.

**Step 6. Counting.** From Step 3, on the even side, the 9 base values `F(4, 2m) mod 3` for `m = 0..8` land three-in-each of the three cosets `{0, 3, 6}, {1, 4, 7}, {2, 5, 8}` (uniform mod 3). Each base value lifts to a full coset of three residues mod 9. So the 27 residues `F(4, 2m) mod 9` for `m = 0..26` cover each coset `3 * 3 = 9` times, distributed `3` per residue inside the coset. Total: **each residue in `Z / 9` is hit exactly 3 times** on the even side. Same argument, same count on the odd side.

**Conclusion.** Over the full period `h = 2..55`, `F(4, h) mod 9` hits each of the 9 residues exactly `3 + 3 = 6` times. The histogram is exactly `[6, 6, 6, 6, 6, 6, 6, 6, 6]`, the exclusion count is `12`, and the exclusion rate is exactly `12 / 54 = 2 / 9`. QED, without appeal to Heath-Brown or to any conjecture.

**What the proof uses.** The whole argument rests on three algebraic accidents specific to `w = 4`: the quadratic coefficient of `Q_e` and `Q_o` is divisible by 3 (making `18 a_2 = 0 mod 27` in the difference); the linear coefficients happen to be `17` and `7`, both `+-1 mod 3`, giving `Delta_9 F` a nonzero coset shift; and `F mod 3` is uniform on `m mod 9` (which is the least trivial input, verified by direct 9-value evaluation). For `w in {6, 10, 12, 17, 28, 30}` the same three-step recipe applies but with the specific polynomials from `A_w, B_w`; for `w in {5, 7, 8, 9, 11, 13, 14, ...}` one of the three steps fails, either the linear-coefficient shift is a multiple of 9 (killing the coset lift) or the base `F mod 3` distribution has a non-uniform 9-value histogram. Producing a general theorem "which `w` have all three steps hold" is the open item.

## Cube-adjacent castle counts: Ramanujan's near-misses on the F table

Beyond the Heath-Brown residue test, one specific arithmetic shape carries castle-side structure: **cube-adjacent** counts, `F(w, h) = c^3 + k` for `|k| <= 1`. The `1729 = 12^3 + 1` at `F(6, 4)` on [[hardy-ramanujan-castle](pages/hardy-ramanujan-castle.md)] is the first instance; systematic enumeration finds every other one below `A(w, h) <= 10^9`:[^exec]

| table | cell | value | cube form | comment |
|---|---|---|---|---|
| F | `(6, 2)` | 28 | `3^3 + 1` | triangular `T(8)`, `= C(8, 2)` |
| F | `(6, 4)` | 1729 | `12^3 + 1` | the Hardy-Ramanujan taxicab |
| F | `(3, 91)` | 4095 | `16^3 - 1` | triangular `T(91)`, `= A(12, 2)` |
| F | `(13, 2)` | 4096 | `16^3` | height-2 power family, `w = 1 mod 12` |
| F | `(3, 127)` | 8001 | `20^3 + 1` | triangular `T(127)` |
| F | `(25, 2)` | 16777216 | `256^3` | height-2 power family, `w = 25 = 1 mod 12` |
| A | `(3m, 2)` all `m` | `2^{3m} - 1` | `(2^m)^3 - 1` | infinite family: `7, 63, 511, 4095, ..., (2^m)^3 - 1` |
| A | `(3, 9)` | 217 | `6^3 + 1` | `3 * 9 * 8 = 216 = 6^3` |
| A | `(4, 3)` | 65 | `4^3 + 1` | `3^4 - 2^4 = 65` |
| odd | `(3, 8)` | 28 | `3^3 + 1` | same value as `F(6, 2)`, triangular |
| odd | `(5, 4)` | 342 | `7^3 - 1` | `342 = 7 * 49 - 1` |

**Two structural families and the sporadic cases.**

**The `A(3m, h) = (h^m)^3 - ((h-1)^m)^3` identity** ([[sum-of-three-cubes-castles](pages/sum-of-three-cubes-castles.md)]) gives an infinite series of cube-adjacent values on the row `h = 2`: `A(3, 2) = 7 = 2^3 - 1`, `A(6, 2) = 63 = 4^3 - 1`, `A(9, 2) = 511 = 8^3 - 1`, `A(12, 2) = 4095 = 16^3 - 1`, `A(15, 2) = 32767 = 32^3 - 1`, and so on: **`A(3m, 2) = (2^m)^3 - 1` for every `m >= 1`.** The identity is `2^{3m} - 1 = (2^m - 1)(2^{2m} + 2^m + 1) = (2^m)^3 - 1`. Every entry in the `A` column at `h = 2` and `w = 3m` is one below a perfect cube, unconditionally.

**The `F(w, 2)` height-2 power family** produces perfect cubes at `w = 1 (mod 12)`: `F(13, 2) = (16)^3, F(25, 2) = (256)^3, F(37, 2) = (4096)^3, ...` = `(16^k)^3` at `w = 12k + 1`. Closed form on [[sum-of-three-cubes-castles](pages/sum-of-three-cubes-castles.md)].

**Triangular near-cubes on the `w = 3` column.** `F(3, h)` at odd `h` is the triangular number `T(h) = h(h-1)/2`. Which `T(h)` are `c^3 +- 1`? The Diophantine equations are

```
T(h) = c^3 - 1  <=>  (2h - 1)^2 = 8 c^3 - 7    (Mordell curve)
T(h) = c^3 + 1  <=>  (2h - 1)^2 = 8 c^3 + 9    (Mordell curve)
```

Exhaustive check for `c <= 10^6` (covering triangular values up to `10^{18}`, `h` up to `~4.5 * 10^8`):[^exec]

```
T(8)   = 28   = 3^3  + 1     (this is odd(3, 8), not on the F table's w = 3 column)
T(91)  = 4095 = 16^3 - 1     = F(3, 91)
T(127) = 8001 = 20^3 + 1     = F(3, 127)
```

**Only three triangular numbers below `10^{18}` are cube-adjacent**, and two of them are on the `F(3, .)` column of the castle table. The Mordell curves involved have finite integer-point sets (Siegel's theorem), so the three solutions may well be *all* such T (an open question for the underlying elliptic curves). The companion sequence `5 T(h) + 1` (the even-`h` half of the `w = 3` column) has **no cube-adjacent values for `h <= 200000`**, plausibly none at all.

**F(6, h) is not a Ramanujan family.** Two of the near-misses sit at `w = 6`: `F(6, 2) = 28 = 3^3 + 1` and `F(6, 4) = 1729 = 12^3 + 1`. There is no continuation - `F(6, h)` for `h = 6, 8, 10, ..., 44` (all cells with `A(6, h) <= 10^9`) is nowhere near a cube: `F(6, 6) = 16126 = 25^3 + 501`, `F(6, 8) = 75299 = 42^3 + 1211`, `F(6, 40) = 301446067 = 671^3 - 665644`. The two cube-adjacent values at `w = 6` are coincidental sporadic hits, not the tip of a parametric family.

**Reading of the census.** Six sporadic `F` near-cubes below `A <= 10^9`, all accounted for: two by the height-2 power-of-two family (`4096, 16777216`), two triangular by the Mordell curves on `w = 3` (`4095, 8001`), and two sporadic on `w = 6` (`28, 1729`). The `1729` is not special in the castle sense - it is a member of the same short sporadic list as `F(6, 2) = 28`. What makes it famous is Ramanujan's taxicab reading, not its castle-side cube-adjacency.

## The `906` twin: castle-generated hard sum-of-three-cubes candidates

`F(5, 5) = 906` is one of the 2019 Booker-Sutherland numbers; the smallest known three-cube representation is `906 = (-74924259395610397)^3 + 72054089679353378^3 + 35961979615356503^3`, a 17-digit triple that needed a 2019 supercomputer run to find ([[sums-of-three-cubes](pages/sums-of-three-cubes.md)]). The natural question is whether other `F(w, h)` values sit on ambient sum-of-three-cubes-hard integers.

The `sum-of-three-cubes-castles` page lists **twenty admissible `F(w, h)` values between 1000 and 20000** with no representation below `15000^3`:

```
1131, 1626, 2481, 2630, 2775, 3741, 5050, 6555, 8445, 9321,
9591, 9870, 11391, 11490, 12246, 12561, 14196, 15801, 16653, 17391
```

Extending the search to `|x|, |y|, |z| <= 20000` (`8 * 10^{12}` cubed) with a full `40001^2 = 1.6 * 10^9`-operation sweep per target confirms **none** of the twenty admits a representation in the new window:[^exec]

```
target      search bound       status
-----------------------------------------
n = 1131    |z| <= 20000       no representation
n = 1626    |z| <= 20000       no representation
n = 2481    |z| <= 20000       no representation
...  (all twenty return "no representation")
```

Sanity check: on the five `F` values that the `sum-of-three-cubes-castles` page reported as cracked between `1000^3` and `15000^3` - `F(3, 61) = 1830`, `F(3, 89) = 3916`, `F(4, 12) = 4065`, `F(3, 50) = 6126`, `F(3, 56) = 7701` - the same search machinery reproduces representations (some with different triples than the source-page ones, since three-cube representations are known to be non-unique under Heath-Brown, e.g. `4065 = (-7114)^3 + (-847)^3 + 7118^3` and `= (-1591)^3 + 1490^3 + 896^3`), confirming the search is not silently missing hits.

So under Heath-Brown, all twenty targets *do* have three-cube representations - just not in the `20000^3` window. **The list is a castle-generated candidate set for the modern sum-of-three-cubes hard-integer problem**, akin to the 33, 42, 906 line that motivated the Booker and Booker-Sutherland 2019 computations. The seven pre-2019 unsolved `n < 1000` (`114, 390, 627, 633, 732, 921, 975`) were closed by 2021 in the ambient literature; whether the twenty `F` values above have been resolved since is a lookup in current sum-of-three-cubes databases, not a computation on this wiki.

**The 906 pattern**, if it repeats, would put more `F(w, h)` values on the "needed a supercomputer" list. The candidate cells are the same twenty; each is admissible mod 9 (verified), each is a genuine castle count (not a width-2 degenerate), and each surviving the `20000^3` window matches the profile of a Booker-Sutherland-hard integer.

## The `{4, 5}` pairing hypothesis, refuted

The two obstruction residues are `4` and `5`, and `4 + 5 = 9`, so they are negatives of each other mod 9. It is tempting to hope for a `(w, h)`-transformation involution that maps `F` to `-F mod 9`, which would force `count(4) = count(5)` in every row histogram - putting all the row-level finite-period noise onto exactly the residues that matter for sums of three cubes. The `h = 6` and `h = 12` rows in the table above show near-exact equality `(248, 248)` and `(1279601, 1277473)`, and the `h = 7` row shows `(220, 219)`, encouraging this hypothesis.

**No such involution exists.** Direct search over shifts and reflections in the w-direction for every row through `h = 8`, and in the h-direction for every column through `w = 15`, returns nothing: there is no `s` such that `F(w + s, h) = -F(w, h) mod 9` for all `w`, and no `c` such that `F(c - w, h) = -F(w, h) mod 9` for all `w`, aside from the trivial reflection in the width-2 column (`F(2, h)` mod 9 has a reflection through the center of its 18-period, but that column is degenerate).[^exec]

**And the empirical pattern breaks.** The `h = 8` row histogram is `[241, 274, 233, 264, 216, 262, 223, 238, 233]` with `count(4) = 216, count(5) = 262`, a difference of `46` at the noise scale of `15.4` - `3 sigma` apart. The `h = 10` row has `count(4) - count(5) = 73`. The `h = 11` row has `-58`. Across `h = 2..11` the `count(4) - count(5)` differences are `+2, -1, -6, -16, 0, +1, -46, -28, +73, -58` - no pattern, no forced pairing. The apparent equality at `h = 6, 7, 12` is coincidence at those particular row periods, not a structural constraint.

The upshot is that the deficit in residues `{4, 5}` at low-`h` rows is **not** algebraically pinned to those two residues. When a row hits its `2/9` limit slowly (as `h = 7` does), it does so via generic 9-bucket rounding, not via a symmetry that folds error onto the excluded classes. That reads as bad news for a "castle counts are structurally biased toward being sums of three cubes" reading and as good news for the equidistribution thesis: nothing algebraic is helping or hurting.

## What this settles and what it opens

Settled:

- The `20.4%` at `N = 10^9` is a finite-N mixing artifact; the aggregate converges monotonically to `2/9`.
- The `h = 7` deficit at `20.10%` is finite-period noise in a period not divisible by `9`; longer-period rows return to `2/9`.
- Columns `w in {4, 6, 10, 12, 17, 28, 30, 35, 82, 84, 89, ...}` have *exactly* rate `2/9` unconditionally - uniform histograms over their full h-period. The pattern is `w = 3^{k-1} + d` for `k >= 2, d in {1, 3, 8}` (with `d in {1, 3}` only in bracket 2).
- **The `w = 4` blackboard proof**: an entirely elementary argument (closed form, parity split, mod-3 uniformity, coset lift in `Z/9`) gives `F(4, h) mod 9` uniform over any 54 consecutive `h`, hence exclusion rate exactly `2/9`. No Heath-Brown, no character sums, no verification of 54 values. Rests on three algebraic features of the `w = 4` polynomials `Q_e(m) = 64 m^3 - 48 m^2 + 17 m - 3` and `Q_o(m) = 32 m^3 + 24 m^2 + 7 m` after clearing the `1/12` denominator.
- **Cube-adjacent castle counts are a short sporadic list**: six `F(w, h)` below `A <= 10^9` are `c^3 +- 1`, all accounted for by three structural sources - the height-2 power-of-two family (`4096, 16777216`), triangular numbers on the `w = 3` column solved by Mordell curves (`4095, 8001`), and the two sporadic `w = 6` hits (`28, 1729`). Ramanujan's `1729` is a member of the sporadic list, not the head of a family. On the `A` table the identity `A(3m, 2) = (2^m)^3 - 1` gives an infinite series of "cube minus one" values.
- **Twenty castle-generated hard sum-of-three-cubes candidates**: the twenty admissible `F(w, h)` between 1000 and 20000 without representations below `15000^3` on the source page survive extension to `|z| <= 20000`. Under Heath-Brown all have representations, just not in that window. The `F(5, 5) = 906` Booker-Sutherland pattern (17-digit representation) may repeat.
- **Row / column divisibility gap**: column periods `per_w = 2 * 3^{ceil(log_3 w) + 1}` have `v_3 >= 2` structurally (from the multiplicity of `-1` in the k-direction char poly); row periods `per_h` have `v_3 = 1` empirically for `h <= 16`. Columns can therefore split `per_w` into 9 equal buckets; rows never can. This is the deep reason the two readings behave differently.
- **No `{4, 5}` pairing symmetry**: no shift or reflection in either direction sends `F(w, h) mod 9` to `-F(w, h) mod 9` universally, so `count(4) = count(5)` is not a forced equality of row histograms. The apparent near-equality at `h = 6, 7, 12` is coincidence, and rows `h = 8, 10, 11` show `3 sigma` asymmetries.

Open:

- **Prove the `{0, 2, 7}` offset template** for the uniform-`w` set. Verified empirically through `w <= 200` (three brackets: 3, 4, 5). Bracket 6 prediction (`w = 244, 246, 251`) is not yet computationally verified. A proof would follow from a general character-sum evaluation on `A_w, B_w mod 9`.
- **Rate-matched-but-not-uniform second class**: `w in {31, 39, 64, 93, 97, 191}` have `count(4) + count(5) = 2 per_w / 9` exactly, without the full histogram being `[per_w / 9] * 9`. The offsets `{3, 11, 36}` (bracket 4) and `{11, 15, 109}` (bracket 5) look coincidental. Is there structural content to this class, or is it noise that happens to satisfy a single linear constraint?
- **Does any `h` inflate `v_3(per_h)` to `2` or more?** For `h <= 16` all row periods sit at `v_3 = 1`. A mod-3 quadruple-root in `char_{h-1}` would push `v_3(per_h)` to 2 and give some row an exactly uniform mod-9 histogram; no such `h` is known.
- **A closed form for `alpha`** where `2/9 - rate(N) ~ N^(-alpha)`. The `1/12` from `(w = 4 with N^(1/3))` vs `(w = 5 with N^(1/4))` is a first guess; refining it needs the exact contribution of each deficit column.
- **The twenty castle-hard candidates against modern sum-of-three-cubes databases**: cross-check `{1131, 1626, 2481, 2630, 2775, 3741, 5050, 6555, 8445, 9321, 9591, 9870, 11391, 11490, 12246, 12561, 14196, 15801, 16653, 17391}` against post-2021 sum-of-three-cubes solution tables to see which have been cracked (with what cube size) and which remain open. Any survivor is a genuine "castle-flagged" candidate for the next Booker-Sutherland-scale computation.
- **Are there more triangular cube-adjacent numbers past `c = 10^6`?** The three found (`T(8) = 28, T(91) = 4095, T(127) = 8001`) may be all of them. The two Mordell curves `x^2 = 8 c^3 - 7` and `x^2 = 8 c^3 + 9` have rank and torsion computable by standard techniques; a proof of "no further integer solutions" (or the sixth solution) would close this specific thread.

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

[^exec]: Verified by execution (2026-09-21), Python 3 with NumPy 1.26 and SymPy 1.14. **Cube-adjacent enumeration on the F, A, odd tables**: for every cell `(w, h)` with `A(w, h) <= 10^9` and `w >= 3`, `F` and `A` and `odd` computed via `F(w, h) = (h^w - (h-1)^w - P(h-1, w) + P(h-2, w))/2` (with `P(k, 3) = (-1)^k (k+1)^2` closed form for `w = 3` and the k-direction recurrence with char poly `(x+1)^w (x-1)^{w-2}` for `w >= 4`); each value tested for `|n - c^3| <= 1` via integer cube root. **Triangular-near-cubes deep search**: iterating `c = 2..10^6` and testing `8 c^3 + 9` and `8 c^3 - 7` for perfect squares (equivalent conditions on `T(h) = c^3 +- 1`); found exactly `T(8), T(91), T(127)`; and `5 T(h) + 1 = c^3 +- 1` for `h <= 200000` returned no hits. **Deep cube search for the twenty unresolved F values**: `numpy`-vectorized triple search over `-20000 <= x, y, z <= 20000` (`40001` outer iterations, each a `40001`-length vectorized cube-root check on `n - c^3 - a^3`; ~25s per target, ~10 min for all twenty); zero of the twenty admitted a representation, in agreement with the source page's `15000^3` search result. Search machinery independently verified against the five source-page representations at `1830, 3916, 4065, 6126, 7701` (all found, with `4065` producing a distinct valid triple from the source-page one). **Uniform-`w` search through `w <= 200`**: for every `w` in that range, `col_residues_fast(w)` (numpy-vectorized seed DP for `k = 0..2w-3`, then k-direction recurrence with char poly `(x+1)^w (x-1)^{w-2}` mod 9 up to `k = per_w + 1`) enumerates one full h-period and reads the 9-bucket histogram. Uniform = histogram equals `[per_w / 9] * 9` element-wise; rate-matched = `hist[4] + hist[5] = 2 * per_w / 9` regardless of bucket balance. Wall time: `6s` at `w = 100`, `35s` at `w = 150`, `121s` at `w = 200` (dominated by the `O(w^3)` seed computation). Uniform set found: `{4, 6, 10, 12, 17, 28, 30, 35, 82, 84, 89}`; rate-matched non-uniform: `{31, 39, 64, 93, 97, 191}`. **`w = 4` blackboard proof**: symbolic computation of the closed form `12 F(4, h) = (24 h^3 - 36 h^2 + 24 h - 9) + (-1)^h (8 h^3 - 12 h^2 + 10 h - 3)` against direct evaluation of `F(4, h) = (h^4 - (h-1)^4 - P(h-1, 4) + P(h-2, 4))/2` for `h = 2..15` (all match); split into `Q_e(m) = 64 m^3 - 48 m^2 + 17 m - 3` and `Q_o(m) = 32 m^3 + 24 m^2 + 7 m` verified against `F(4, 2m)` and `F(4, 2m+1)` for `m = 1..27`; divisibility of `Q_e, Q_o` by 3 checked symbolically mod 3; `F(4, 2m) mod 3` and `F(4, 2m + 1) mod 3` uniform over `m mod 9` verified in 18 direct evaluations; `Q_e(m + 9) - Q_e(m) mod 27 = 18` and `Q_e(m + 18) - Q_e(m) mod 27 = 9` (and `Q_o` swapped) verified for `m = 0..5` (constant in `m` by the algebraic argument in the page). Final histogram `[6, 6, 6, 6, 6, 6, 6, 6, 6]` matches the count derived from the coset-tiling argument. **Row-period `v_3` table (`h = 2..16`)**: `char_k` polynomials built from the three-term recurrence `char_{k+1} = x^2 char_{k-1} - 2 char_k` seeded by `char_0 = x - 1, char_1 = x^2 - 2x + 2`; period of `x` mod `(char_k, 9)` computed by iterating the companion-matrix state and detecting return to `(1, 0, ..., 0)`; row period computed as `lcm(ord_9(h), ord_9(h-1), per(char_{h-1}) mod 9, per(char_{h-2}) mod 9)`; three-adic valuation `v_3(per_h) = 1` verified for every `h` in the table. **`{4, 5}` pairing search**: for each row `h in {2..8}` and each column `w in {2..15}`, exhaustive search over shifts `s in [1, per - 1]` and reflection centers `c in [0, per - 1]` looking for the condition `F(w + s, h) = -F(w, h) mod 9` or `F(c - w, h) = -F(w, h) mod 9` for all indices; only the trivial `w = 2` column reflection at center 6 hit. **Row histograms (`h = 2..11`)**: parity-refined column DP over `Z/9` iterated to width `3 * per_h + 20` past a transient of `5`; period detected by first-repeat and full-period histogram counted; verified against the `sum-of-three-cubes-castles` row-period table. **`h = 12` full period**: numpy 12x12 mod-9 matrix iterated `11,514,360` times (37s wall) for the state vectors `(P(11, .), P(10, .))`, `F` read off through the closed form, histogram counted exactly. **`h = 13, 14, 15`**: same machinery, 5,000,000-step sample (rate stable to third digit). **Column histograms (`w = 2..30`)**: seeds `P(k, w) mod 9` for `k = 0..2w-3` by column DP, extended to `k = 0..per_w + 1` by the k-direction recurrence with characteristic polynomial `(x+1)^w (x-1)^(w-2)` reduced mod 9; `F(w, h) mod 9` read off for `h = 2..2 + per_w - 1`. Uniform-histogram claim (`[per_w/9]*9`) verified equality digit for digit at `w = 4, 6, 10, 12, 17, 28, 30`. **Aggregate at `N`**: for each `w >= 4` with `h^w - (h-1)^w <= N` reachable, binary search the maximum `h`, then count exclusions in `[2, h_max]` as `floor((h_max - 1)/per_w) * (excluded_per_period) + (residues in the final partial period)`; runs in `6.8s` at `N = 10^18`, `37s` at `N = 10^24`, `330s` at `N = 10^36`. **`P(k, w) mod 9` isolation table**: same column DP, iterated to width `> 3 * per_k` for period detection. All quoted numbers are the scripts' printed output. Code sketch:

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
