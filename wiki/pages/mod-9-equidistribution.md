---
title: Mod-9 equidistribution of the F table
category: Analyses
summary: Do castle counts F(w,h) hit the excluded residues 4, 5 mod 9 at the equidistribution density 2/9, or is there a persistent bias? Answer - no bias. The 20.4% exclusion rate over cells with A(w,h) <= 10^9 on the sum-of-three-cubes-castles page is a finite-N artifact: the rate increases with N in the computed range and converges to 2/9 at asymptotic rate `deficit(N) ~ (4/54) * (4^{1/3} / 5^{1/4}) * N^{-1/12} = 0.0786 * N^{-1/12}` (exponent and constant derived from the mixture argument, matched within 0.6% for N >= 10^{15}): 21.36% at 10^12, 21.78% at 10^15, 21.98% at 10^18, 22.14% at 10^24, 22.214% at 10^36. The row and column readings behave differently: columns w in {4, 6, 10, 12, 17, 28, 30, 35, 82, 84, 89, 244, 246, 251, ...} - the pattern w = 3^{k-1} + d for k >= 2, d in {1, 3, 8} - hit 2/9 exactly, while every row computed (h <= 40) carries a +-1-per-residue rounding jitter. The mechanism (a row / column three-adic divisibility gap, a coset-lift criterion for uniform columns, and a six-step proof at w = 4) is on the companion page mod-9-coset-lift. The tempting {4, 5} pairing hypothesis - that some (w, h) involution forces count(4) = count(5) in every row - is refuted: no such shift or reflection exists in either direction, and rows h = 8, 10, 11 show 3 sigma asymmetries between count(4) and count(5). Cube-adjacent castle counts are a short sporadic list: six F(w, h) below A <= 10^9 are c^3 +- 1, all accounted for by three structural sources (the height-2 power family, triangular numbers on w = 3 solved by Mordell curves, and two sporadic w = 6 hits including F(6, 4) = 1729); F(6, h) is not a Ramanujan family.
tags: [analysis, castle, sum-of-cubes, mod-9, periodicity, equidistribution, finite-sample-artifact, kitamasa, cube-near-miss, mordell-curve]
sources: [oeis-mining-pe502, project-euler-502-solution]
created: 2026-09-21
updated: 2026-09-28
---

# Mod-9 equidistribution of the F table

Under Heath-Brown's conjecture, `F(w,h)` is a sum of three cubes iff `F(w,h) mod 9` is not `4` or `5` ([[sums-of-three-cubes](pages/sums-of-three-cubes.md)]), so "how many castle counts are provably not sums of three cubes" is the density of the residues `{4, 5}` in the mod-9 image of the `F` table. [[sum-of-three-cubes-castles](pages/sum-of-three-cubes-castles.md)] measured `20.4%` (179 of the 875 cells) with `A(w,h) <= 10^9` and `w >= 4`, against the equidistribution value `2/9 = 22.22%`, and singled out the `h = 7` row as an especially clean deficit at `20.10%` over an exact period of 2184. **The deficit is a finite-N artifact of the census bound; the F table has no structural bias.** Three independent readings - row by row, column by column, and aggregate over cells with `A <= N` - all point to `2/9` in the limit. The structural mechanism (why some columns hit `2/9` exactly, why no row can) is on [[mod-9-coset-lift](pages/mod-9-coset-lift.md)].

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
| 12 | 11514360 | 2557075 | 22.208% | `1279659, 1280265, 1274551, 1284045, 1279602, 1277473, 1280124, 1278396, 1280245` |
| 13 | 177144 | 39526 | 22.313% | `19610, 19505, 19955, 19511, 19718, 19808, 19541, 19577, 19919` |
| 14 | 1771440 | 393211 | 22.197% | `197151, 196699, 196965, 196740, 196717, 196494, 196725, 196753, 197196` |
| 15 | (5,000,000-`w` sample; period 25,170,390,960) | 1111880 | 22.238% | `554873, 555731, 555381, 554956, 554891, 556989, 556117, 554630, 556433` |

Three things read off:

1. **Rates converge to `2/9`.** Every row from `h = 9` upward is within `0.6` percentage points of `22.222%`, and `h = 12, 13, 14, 15` are all within `0.12`. `h = 12` is `22.208%` over its full period `11,514,360`.
2. **The `h = 7` deficit is real but small.** The histogram concentrates the deficit at residues `4` and `5` (`220` and `219` observed against `242.67` expected), a `~23`-count drop each. The standard deviation of the whole histogram is `sqrt(sum (h_r - per_h/9)^2 / 9) = 15.4`, so the residue-`4, 5` deficit is about `1.5 sigma` per residue.
3. **The `h = 2, 3` rows have small exclusion rates**: `1/12` at `h = 2` (a closed form on [[sum-of-three-cubes-castles](pages/sum-of-three-cubes-castles.md)]) and `3/24 = 1/8` at `h = 3`, both below `2/9`. The row deficit at small `h` comes from these two rows.

**No row with `h <= 40` is exactly uniform mod 9.** The reason is 3-adic: `per_h` is not divisible by 9 for any `h <= 40` (computed on [[mod-9-coset-lift](pages/mod-9-coset-lift.md)]), so `per_h / 9` is not an integer and some residue buckets hit `floor(per_h / 9)` while others hit `ceil(per_h / 9)`. Full derivation on [[mod-9-coset-lift](pages/mod-9-coset-lift.md)] ("The row / column divisibility gap").

## The column reading (fixed w)

The column reading is sharper: `F(w, . ) mod 9` is periodic in `h` with period `per_w = 2 * 3^(1 + ceil(log_3 w))` ([[signed-tower-k-direction](pages/signed-tower-k-direction.md)]'s `2 p^(ceil(log_p L))` rule with `p = 3` and one extra factor `3` for the second power). All the periods are divisible by `9` from `w >= 2` onward (`18, 54, 162, 486, 1458, ...`), so an *exactly uniform* histogram is a numerical possibility, and some columns achieve it:[^exec]

| `w` | `per_w` | excluded | rate | uniform histogram? |
|---|---|---|---|---|
| 2 | 18 | 2 | 11.11% | no `[10, 1, 1, 1, 1, 1, 1, 1, 1]` |
| 3 | 18 | 2 | 11.11% | no `[2, 5, 0, 2, 2, 0, 5, 2, 0]` |
| **4** | 54 | 12 | **22.22%** | **YES** `[6, 6, 6, 6, 6, 6, 6, 6, 6]` |
| 5 | 54 | 8 | 14.81% | no `[4, 7, 4, 7, 4, 4, 10, 10, 4]` |
| **6** | 54 | 12 | **22.22%** | **YES** `[6]*9` |
| 7 | 54 | 10 | 18.52% | no |
| 8 | 54 | 6 | 11.11% | no |
| 9 | 54 | 15 | 27.78% | no |
| **10** | 162 | 36 | **22.22%** | **YES** `[18]*9` |
| 11..16 | 162 | (mixed) | (mixed) | uniform only at `w = 12` |
| **17** | 162 | 36 | **22.22%** | **YES** `[18]*9` |
| 18..27 | 162 | (mixed) | (mixed) | none uniform |
| **28, 30** | 486 | 108 | **22.22%** | **YES** `[54]*9` |
| **35** | 486 | 108 | **22.22%** | **YES** `[54]*9` |
| **82, 84, 89** | 1458 | 324 | **22.22%** | **YES** `[162]*9` |
| **244, 246, 251** | 4374 | 972 | **22.22%** | **YES** `[486]*9` |

The uniform-histogram columns through `w <= 293` are:[^exec]

```
w in {4, 6, 10, 12, 17, 28, 30, 35, 82, 84, 89, 244, 246, 251}
```

For these `w`, the `F(w, .) mod 9` sequence hits every residue class exactly `per_w / 9` times in one full period, so the exclusion rate is **exactly `2/9`**. The `w = 4` column supplies the most cells under `A <= N` for large `N` (about `N^{1/3}`, below), which drives the aggregate to `2/9`.

**The uniform-`w` pattern.** Group the uniform `w`'s by the [[signed-tower-k-direction](pages/signed-tower-k-direction.md)] bracket `k = ceil(log_3 w)`, whose h-period is `per_w = 2 * 3^{k + 1}` and whose w-range is `[3^{k-1} + 1, 3^k]`. Within each bracket the uniform `w`'s sit at three fixed offsets from the bracket start `3^{k-1} + 1`:

| bracket `k` | w-range | `per_w` | uniform `w` | offsets from `3^{k-1} + 1` |
|---|---|---|---|---|
| 2 | `[4, 9]` | 54 | `4, 6` | `0, 2` |
| 3 | `[10, 27]` | 162 | `10, 12, 17` | `0, 2, 7` |
| 4 | `[28, 81]` | 486 | `28, 30, 35` | `0, 2, 7` |
| 5 | `[82, 243]` | 1458 | `82, 84, 89` | `0, 2, 7` |
| 6 | `[244, 729]` | 4374 | `244, 246, 251` | `0, 2, 7` |

The offset set `{0, 2, 7}` is invariant from bracket 3 through bracket 6. Bracket 2 is truncated (only offsets `0, 2` fit before the next bracket starts). This produces three explicit sequences of uniform `w`'s:

```
A_k = 3^{k-1} + 1  =  4, 10, 28, 82, 244, 730, ...      (k >= 2)
B_k = 3^{k-1} + 3  =  6, 12, 30, 84, 246, 732, ...      (k >= 2)
C_k = 3^{k-1} + 8  =  17, 35, 89, 251, 737, ...         (k >= 3)
```

Equivalently, the uniform-`w` set is `{ 3^{k-1} + d : k >= 2, d in {1, 3, 8}, 3^{k-1} + d <= 3^k }`. **A mod-9 congruence reading**: for `k >= 3`, `3^{k-1} ≡ 0 (mod 9)`, so the uniform `w`'s satisfy `w ≡ 1, 3, or 8 (mod 9)` - or equivalently `w ≡ 1, 3, or -1 (mod 9)`. That is a necessary condition; higher-offset representatives of the same residue class (e.g. `w = 19` in bracket 3, `w = 37` in bracket 4) are *not* uniform.

**A criterion is on [[mod-9-coset-lift](pages/mod-9-coset-lift.md)]**: for every `w` in `[10, 100]`, `w` is uniform iff the shift-by-`per_w / 3` differences of `F(w, . ) mod 9` take only the values `{3, 6}`; non-uniform `w` also take `0` (a coset-shift fixed point). The `w = 4` proof there writes the shift argument out for one column.

**Rate-matched-but-not-uniform columns**, a distinct second class, also exist. These are `w` where the exclusion rate equals `2/9` on the digit but the full 9-bucket histogram is *not* `[per_w / 9] * 9`. Through `w <= 293`:[^exec]

```
w in {31, 39, 64, 93, 97, 191, 289}
```

Sample histograms: `w = 31: [51, 60, 48, 60, 60, 48, 60, 51, 48]` (rate 22.22% via `count(4) + count(5) = 108`, with the individual residues running from 48 to 60). The count in residues `{4, 5}` is exactly `2 * per_w / 9` while the other residues are unbalanced. No pattern in these `w` is known.

The other columns fluctuate around `2/9` by about `10-30%` of the mean count per residue; `w = 5, 8, 9, 14, 20` deviate most.

## The aggregate over `A(w, h) <= N`

The census the `20.4%` figure came from is the mixture over `(w, h)` cells with `A(w, h) <= N`. For fixed `w`, the number of `h` with `A(w, h) = h^w - (h-1)^w <= N` is approximately `(N/w)^(1/(w-1))`, so `w = 4` supplies about `N^(1/3)` cells, `w = 5` about `N^(1/4)`, and higher `w` a diminishing tail. The aggregate rate is the number-of-cells-weighted average of column rates; since `w = 4` has exact rate `2/9`, and the deficit columns `w = 5, 7, 8` supply only `O(N^(1/4))` cells against `w = 4`'s `O(N^(1/3))`, the mixture is pulled toward `2/9` at rate `O(N^(-1/12))`.

Computed with the k-direction recurrence (order `2w - 2` over `Z/9`, which is not a field; see [[castle-ring-spectrum](pages/castle-ring-spectrum.md)] §5), extended by the char-poly `(x+1)^w (x-1)^(w-2)`, then read off through the closed form `F(w, h) mod 9 = (h^w - (h-1)^w - P(h-1, w) + P(h-2, w)) * 5 mod 9`:[^exec]

| `N` | cells `w >= 4` | excluded | rate | deficit vs `2/9` |
|---|---|---|---|---|
| `10^6` | 119 | 21 | 17.647% | 4.58 pp |
| `10^9` | 875 | 179 | 20.457% | 1.77 pp |
| `10^12` | 7,367 | 1,574 | 21.366% | 0.86 pp |
| `10^15` | 68,020 | 14,814 | 21.779% | 0.44 pp |
| `10^18` | 655,355 | 144,015 | 21.975% | 0.25 pp |
| `10^24` | 63,719,987 | 14,110,011 | 22.144% | 0.08 pp |
| `10^36` | 630,641,206,298 | 140,092,917,085 | 22.2144% | 0.008 pp |

The deficit obeys `2/9 - rate(N) ~ C * N^{-1/12}` with a closed-form leading coefficient. Fitting the seven data points in log-log: the successive slopes at `N in {10^{15}..10^{18}, 10^{18}..10^{24}, 10^{24}..10^{36}}` are `-0.0845, -0.0833, -0.0833`, consistent with `-1/12 = -0.0833...`.[^exec] The **mixture argument** predicts both exponent and constant: at large `N`, the cell census is dominated by column `w = 4` (uniform, exact `2/9` rate, `~N^{1/3}` cells) plus the leading deficit column `w = 5` (rate `8/54 = 14.81%`, deficit `4/54` from `2/9`, `~N^{1/4}` cells). The ratio of cell counts is

```
n_5 / n_4  =  (N/5)^{1/4} / (N/4)^{1/3}  =  (4^{1/3} / 5^{1/4}) * N^{-1/12}  ~  1.062 * N^{-1/12}
```

so `deficit(N) ~ (4/54) * (4^{1/3} / 5^{1/4}) * N^{-1/12} = 0.07863 * N^{-1/12}`. Compare against the observed deficits:

| `N` | observed deficit | predicted `0.0786 * N^{-1/12}` | ratio |
|---|---|---|---|
| `10^{15}` | `4.43 * 10^{-3}` | `4.42 * 10^{-3}` | 1.002 |
| `10^{18}` | `2.47 * 10^{-3}` | `2.49 * 10^{-3}` | 0.994 |
| `10^{24}` | `7.82 * 10^{-4}` | `7.86 * 10^{-4}` | 0.995 |
| `10^{36}` | `7.82 * 10^{-5}` | `7.86 * 10^{-5}` | 0.995 |

Within 0.6% from `N = 10^{15}` on. At smaller `N` the columns `w = 7, 8, 9` (relative weights `N^{-1/6}, N^{-4/21}, N^{-5/24}`) still register, driving the ratio up to `1.84` at `N = 10^6`; their weights decay faster than `N^{-1/12}`. In the computed range the aggregate rate stays below `2/9` and increases with `N`; its limit is `2/9` because the uniform `w = 4` column supplies all but a vanishing fraction of the cells.

**The `20.4%` at `N = 10^9` decomposes** into `w = 4` supplying the largest bloc of cells at exact rate `2/9`, plus deficit columns `w = 5, 7, 8` with rates `14.8%, 18.5%, 11.1%` supplying enough cells to move the mean down. It is a **mixing artifact**: the aggregate is the cell-weighted mean of the column rates, and at moderate `N` the columns `w = 5, 7, 8` pull it below `2/9`.

## The `h = 7` row

The `h = 7` row's `20.10%` over `2184` is one instance of the same story: the period `2184 = 2^3 * 3 * 7 * 13` is divisible by `3` but *not* by `9`, so an exactly uniform 9-bucket histogram is impossible - the closest possible distribution has counts `242` or `243` in each bucket. The observed distribution is `[238, 240, 255, 241, 220, 219, 249, 268, 254]` with maximum deviation `25.33` (residue `7`, surplus) and residues `4, 5` each `23` below the mean. Against a `sqrt(per_h / 9) ~ 15.6` scale per residue this is about `1.5 sigma`. The `h = 8, 9, 10` rows (periods `2184, 10920, 21840`) have rates `21.89%, 22.18%, 22.25%`; the `h = 7` deficit is specific to that row.

The `h = 12` row, with period `11,514,360`, has rate `22.208%`, `0.014` pp below `2/9`. The row rates show no monotone bias in `h`.

## Distribution of `P(k, w) mod 9` in isolation

One ingredient is not uniform: the signed tower count `P(k, w) mod 9` (fixed `k`, varying `w`; this is `P(k, L)` at base length `L = w`, [[castle-notation](pages/castle-notation.md)]), which is one of the four ingredients in `F`, is *not* uniformly distributed even over its full width-direction period. Histograms of `P(k, w) mod 9` over one period in `w`:[^exec]

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

The residue `0` is over-represented at small `k` (6 of 24 at `k = 1`, 5 of 24 at `k = 2`); at `k = 1`, `P(1, w) = Re((1+i)^{w+1})` vanishes whenever `w = 1 (mod 4)`. At `k >= 5` every residue is within a factor `1.3` of the uniform mean, except at `k = 8` (period 60, with 26 zeros).

`F` uses the difference `P(h-2, w) - P(h-1, w)`, whose distribution depends on the joint distribution of consecutive `k` slices, not on either histogram alone. The near-uniform `F` rows for `h >= 9` and the uniform columns show that the bias of a single slice does not carry into `F`.

## The `{4, 5}` pairing hypothesis, refuted

The two obstruction residues are `4` and `5`, and `4 + 5 = 9`, so they are negatives of each other mod 9. An involution of `(w, h)` mapping `F` to `-F mod 9` would force `count(4) = count(5)` in every row histogram. The `h = 6` and `h = 12` rows come close, `(248, 248)` and `(1279602, 1277473)`, as does the `h = 7` row, `(220, 219)`.

**No such involution exists.** Direct search over shifts and reflections in the w-direction for every row through `h = 8`, and in the h-direction for every column through `w = 15`, returns nothing: there is no `s` such that `F(w + s, h) = -F(w, h) mod 9` for all `w`, and no `c` such that `F(c - w, h) = -F(w, h) mod 9` for all `w`, aside from the trivial reflection in the width-2 column.[^exec]

**And the empirical pattern breaks.** The `h = 8` row histogram is `[241, 274, 233, 264, 216, 262, 223, 238, 233]` with `count(4) = 216, count(5) = 262`, a difference of `46` at the noise scale of `15.4` - `3 sigma` apart. The `h = 10` row has `count(4) - count(5) = 73`. The `h = 11` row has `-58`. Across `h = 2..11` the `count(4) - count(5)` differences are `+2, -1, -6, -16, 0, +1, -46, -28, +73, -58` - no pattern, no forced pairing.

So the deficit in residues `{4, 5}` at low-`h` rows is **not** algebraically pinned to those two residues: rows such as `h = 7` fall short of `2/9` through ordinary 9-bucket rounding, with no symmetry acting on the excluded classes.

## Cube-adjacent castle counts

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

**The `A(3m, h) = (h^m)^3 - ((h-1)^m)^3` identity** ([[sum-of-three-cubes-castles](pages/sum-of-three-cubes-castles.md)]) gives an infinite series of cube-adjacent values on the row `h = 2`: `A(3, 2) = 7 = 2^3 - 1`, `A(6, 2) = 63 = 4^3 - 1`, `A(9, 2) = 511 = 8^3 - 1`, `A(12, 2) = 4095 = 16^3 - 1`, and so on: **`A(3m, 2) = (2^m)^3 - 1` for every `m >= 1`.** The identity is `2^{3m} - 1 = (2^m - 1)(2^{2m} + 2^m + 1) = (2^m)^3 - 1`. Every entry in the `A` column at `h = 2` and `w = 3m` is one below a perfect cube, unconditionally.

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

**Only three triangular numbers below `10^{18}` are cube-adjacent**, and two of them are on the `F(3, .)` column of the castle table. The Mordell curves involved have finite integer-point sets (Siegel's theorem), so the three solutions may well be *all* such T (an open question for the underlying elliptic curves). The companion sequence `5 T(h) + 1` (the even-`h` half of the `w = 3` column) has **no cube-adjacent values for `h <= 200000`**.

**F(6, h) is not a Ramanujan family.** Two of the near-misses sit at `w = 6`: `F(6, 2) = 28 = 3^3 + 1` and `F(6, 4) = 1729 = 12^3 + 1`. There is no continuation - `F(6, h)` for `h = 6, 8, 10, ..., 44` (all cells with `A(6, h) <= 10^9`) is nowhere near a cube: `F(6, 6) = 16126 = 25^3 + 501`, `F(6, 8) = 75299 = 42^3 + 1211`, `F(6, 40) = 301446067 = 671^3 - 665644`. The two cube-adjacent values at `w = 6` are coincidental sporadic hits, not the tip of a parametric family.

**Reading of the census.** Six sporadic `F` near-cubes below `A <= 10^9`, all accounted for: two by the height-2 power-of-two family (`4096, 16777216`), two triangular by the Mordell curves on `w = 3` (`4095, 8001`), and two sporadic on `w = 6` (`28, 1729`). The `1729` is not special in the castle sense - it is a member of the same short sporadic list as `F(6, 2) = 28`. What makes it famous is Ramanujan's taxicab reading, not its castle-side cube-adjacency.

## What this settles and what it opens

Settled:

- The `20.4%` at `N = 10^9` is a finite-N mixing artifact; the aggregate rate increases with `N` in the computed range and converges to `2/9`.
- **Convergence rate `alpha = 1/12`, with closed-form constant**: `deficit(N) = 2/9 - rate(N) ~ (4/54) * (4^{1/3} / 5^{1/4}) * N^{-1/12} = 0.0786 * N^{-1/12}`, matching observed values within 0.6% from `N = 10^{15}` onward. The exponent and constant come from the mixture argument dominant column `w = 4` (uniform, `~ N^{1/3}` cells at `2/9`) vs. leading deficit column `w = 5` (`~ N^{1/4}` cells, deficit `4/54`).
- The `h = 7` row's `20.10%` is set by its period (2184, not divisible by `9`); rows with longer periods come closer to `2/9`.
- Columns `w in {4, 6, 10, 12, 17, 28, 30, 35, 82, 84, 89, 244, 246, 251, ...}` have *exactly* rate `2/9` unconditionally - uniform histograms over their full h-period. The pattern is `w = 3^{k-1} + d` for `k >= 2, d in {1, 3, 8}` (with `d in {1, 3}` only in bracket 2), verified across brackets 2..6 (`w <= 293`). Necessary mod-9 congruence `w in {1, 3, -1} (mod 9)` derivable for `k >= 3`. The mechanism, the `w = 4` proof and the coset-lift criterion are on [[mod-9-coset-lift](pages/mod-9-coset-lift.md)].
- **Cube-adjacent castle counts are a short sporadic list**: six `F(w, h)` below `A <= 10^9` are `c^3 +- 1`, all accounted for by three structural sources - the height-2 power-of-two family (`4096, 16777216`), triangular numbers on the `w = 3` column solved by Mordell curves (`4095, 8001`), and the two sporadic `w = 6` hits (`28, 1729`). Ramanujan's `1729` is a member of the sporadic list, not the head of a family. On the `A` table the identity `A(3m, 2) = (2^m)^3 - 1` gives an infinite series of "cube minus one" values.
- **No `{4, 5}` pairing symmetry**: no shift or reflection in either direction sends `F(w, h) mod 9` to `-F(w, h) mod 9` universally, so `count(4) = count(5)` is not a forced equality of row histograms. The apparent near-equality at `h = 6, 7, 12` is coincidence, and rows `h = 8, 10, 11` show `3 sigma` asymmetries.

Open:

- **Rate-matched-but-not-uniform second class**: `w in {31, 39, 64, 93, 97, 191, 289}` have `count(4) + count(5) = 2 per_w / 9` exactly, without the full histogram being `[per_w / 9] * 9`. The offsets look coincidental across brackets. Is there structural content to this class, or is it noise that happens to satisfy a single linear constraint?
- **Are there more triangular cube-adjacent numbers past `c = 10^6`?** The three found (`T(8) = 28, T(91) = 4095, T(127) = 8001`) may be all of them. The two Mordell curves `x^2 = 8 c^3 - 7` and `x^2 = 8 c^3 + 9` have rank and torsion computable by standard techniques; a proof that there are no further integer solutions, or a further solution, would settle it.
- The mechanism-side open items (a proof of the coset-lift criterion, the squarefree conjecture on `char_k mod 3`, and `v_3(per_h) = 1` for all `h`) are on [[mod-9-coset-lift](pages/mod-9-coset-lift.md)].

## Appearances in Sources

- [[oeis-mining-pe502](pages/oeis-mining-pe502.md)] - `F(w, h)` tabulation whose columns and rows are enumerated here mod 9.
- [[project-euler-502-solution](pages/project-euler-502-solution.md)] - `T(k, L) = (k+1)^L` and the Kitamasa route; the k-direction recurrence used to extend `P(k, w) mod 9` past the seeds.

## Related Concepts

- [[mod-9-coset-lift](pages/mod-9-coset-lift.md)] - the mechanism companion: divisibility gap, `w = 4` proof, coset-lift criterion, joint-state theorem for `(x +- 1)^3`.
- [[sum-of-three-cubes-castles](pages/sum-of-three-cubes-castles.md)] - the parent question and the census that raised the deficit.
- [[sums-of-three-cubes](pages/sums-of-three-cubes.md)] - Heath-Brown's mod-9 conjecture; if any castle count outside residues `4, 5` fails to be a sum of three cubes, the analysis moves; the equidistribution is unaffected.
- [[mod-p-observatory](pages/mod-p-observatory.md)] - the mechanism giving row and column periods.
- [[signed-tower-k-direction](pages/signed-tower-k-direction.md)] - `P(k, L) = (-1)^k A_L(k) + B_L(k)`, the `(x+1)^L (x-1)^(L-2)` char poly, and the `2 p^(ceil(log_p L))` mod-p period behind `per_w`.
- [[castle-counting-formula](pages/castle-counting-formula.md)] - the closed form `F = (h^w - (h-1)^w - P(h-1, w) + P(h-2, w))/2`.
- [[hardy-ramanujan-castle](pages/hardy-ramanujan-castle.md)] - `F(6, 4) = 1729`, the taxicab coincidence behind the sum-of-three-cubes pages.
- [[kitamasa](pages/kitamasa.md)] - jump-to-index-N over `Z/9` used to sanity-check the `h = 12` row.
- [[castle-eigenvalue-oeis-crosswalk](pages/castle-eigenvalue-oeis-crosswalk.md)] - the `2 · p^{ceil(log_p L)}` k-direction period used here is pinned quantitatively there; one-hop shortcut.

## Footnotes

[^exec]: Verified by execution (2026-09-21), Python 3 with NumPy 1.26 and SymPy 1.14. **Cube-adjacent enumeration on the F, A, odd tables**: for every cell `(w, h)` with `A(w, h) <= 10^9` and `w >= 3`, `F` and `A` and `odd` computed via `F(w, h) = (h^w - (h-1)^w - P(h-1, w) + P(h-2, w))/2` (with `P(k, 3) = (-1)^k (k+1)^2` closed form for `w = 3` and the k-direction recurrence with char poly `(x+1)^w (x-1)^{w-2}` for `w >= 4`); each value tested for `|n - c^3| <= 1` via integer cube root. **Triangular-near-cubes deep search**: iterating `c = 2..10^6` and testing `8 c^3 + 9` and `8 c^3 - 7` for perfect squares (equivalent conditions on `T(h) = c^3 +- 1`); found exactly `T(8), T(91), T(127)`; and `5 T(h) + 1 = c^3 +- 1` for `h <= 200000` returned no hits. **Uniform-`w` search through `w <= 293` (brackets 2..6)**: for every `w` in the range, `col_residues_fast(w)` (numpy-vectorized seed DP for `k = 0..2w-3`, then k-direction recurrence with char poly `(x+1)^w (x-1)^{w-2}` mod 9 up to `k = per_w + 1`) enumerates one full h-period and reads the 9-bucket histogram. Uniform = histogram equals `[per_w / 9] * 9` element-wise; rate-matched = `hist[4] + hist[5] = 2 * per_w / 9` regardless of bucket balance. Wall time: `6s` at `w = 100`, `121s` at `w = 200`, `225s` for bracket-6 offsets 0..49 (`w in [244, 293]`). Uniform set found: `{4, 6, 10, 12, 17, 28, 30, 35, 82, 84, 89, 244, 246, 251}`; rate-matched non-uniform: `{31, 39, 64, 93, 97, 191, 289}`. **Rate-of-convergence fit**: log-log linear regression on the seven aggregate data points at `N = 10^6, 10^9, 10^{12}, 10^{15}, 10^{18}, 10^{24}, 10^{36}`; successive-pair slopes converge to `-1/12` for `N >= 10^{18}` (0.0845, 0.0833, 0.0833); the mixture-argument coefficient `(4/54) * (4^{1/3} / 5^{1/4}) = 0.078634` predicts each late data point within `0.5%`. **Row histograms (`h = 2..11`)**: parity-refined column DP over `Z/9` iterated to width `3 * per_h + 20` past a transient of `5`; period detected by first-repeat and full-period histogram counted; verified against the `sum-of-three-cubes-castles` row-period table. **`h = 12` full period**: numpy 12x12 mod-9 matrix iterated `11,514,360` times (37s wall) for the state vectors `(P(11, .), P(10, .))`, `F` read off through the closed form, histogram counted exactly. **`h = 13, 14`** (re-run 2026-09-28): full periods 177,144 and 1,771,440 with the same machinery; **`h = 12`** re-run over `w = 5 .. 5 + 11,514,359` (past the `w <= 1` transient of `12^w mod 9`); **`h = 15`**: a 5,000,000-step sample. **`{4, 5}` pairing search**: for each row `h in {2..8}` and each column `w in {2..15}`, exhaustive search over shifts `s in [1, per - 1]` and reflection centers `c in [0, per - 1]` looking for the condition `F(w + s, h) = -F(w, h) mod 9` or `F(c - w, h) = -F(w, h) mod 9` for all indices; only the trivial `w = 2` column reflection at center 6 hit. **Aggregate at `N`**: for each `w >= 4` with `h^w - (h-1)^w <= N` reachable, binary search the maximum `h`, then count exclusions in `[2, h_max]` as `floor((h_max - 1)/per_w) * (excluded_per_period) + (residues in the final partial period)`; runs in `6.8s` at `N = 10^18`, `37s` at `N = 10^24`, `330s` at `N = 10^36`. **`P(k, w) mod 9` isolation table**: same column DP, iterated to width `> 3 * per_k` for period detection. All quoted numbers are the scripts' printed output. Code sketch for the column-residues computation:

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
        C = polymul(A, B)
        Pk = list(seeds)
        while len(Pk) < P + 2:
            k = len(Pk)
            v = -sum(C[order - j] * Pk[k - j] for j in range(1, order + 1))
            Pk.append(v % p)
        inv2 = 5
        return P, [(pow(h, w, p) - pow(h-1, w, p) - Pk[h-1] + Pk[h-2]) * inv2 % p
                   for h in range(2, 2 + P)]
    ```
