---
title: Mod-9 equidistribution of the castle counts
category: Analyses
summary: The proportion of castle counts A^e(w, h) ≡ 4 or 5 (mod 9), the residues no sum of three cubes takes, over the cells (w, h) with w ≥ 4 and A(w, h) ≤ N. It is 20.46% at N = 10^9 and tends to 2/9 with deficit (4/54)(4^{1/3}/5^{1/4}) N^{−1/12} = 0.0786 N^{−1/12} (proved from the exact rates of the columns w = 4, 5, 6); the computed rates are 21.37% at 10^12, 21.98% at 10^18 and 22.214% at 10^36. The columns w = 4, 6, 10, 12, 17, 28, 30, 35, 82, 84, 89, 244, 246, 251, which are 3^{k−1} + d with d ∈ {1, 3, 8}, are exactly uniform mod 9 for w ≤ 293, and nine more columns have rate exactly 2/9 without being uniform; no row with h ≤ 40 is uniform. No shift or reflection sends A^e to −A^e mod 9 in any row h ≤ 8 or column 3 ≤ w ≤ 15. The castle counts within 1 of a cube with A ≤ 10^9 are listed: those of height 2 come from 2^{w−1} at w ≡ 1 (mod 12), and on the column w = 3 the triangular numbers h(h − 1)/2 within 1 of a cube are exactly h = 91, 127 (integral points of two Mordell curves).
tags: [analysis, castle, sum-of-cubes, mod-9, periodicity, equidistribution, finite-sample-artifact, kitamasa, cube-near-miss, mordell-curve]
sources: [project-euler-502-solution]
created: 2026-09-21
updated: 2026-10-25
---

# Mod-9 equidistribution of the castle counts

No integer `≡ 4` or `5 (mod 9)` is a sum of three cubes, and Heath-Brown conjectured that every other integer is one ([[sums-of-three-cubes](pages/sums-of-three-cubes.md)]). Under the conjecture, a castle count `A^e(w, h)` (the `F(w, h)` of the problem statement) is a sum of three cubes exactly when it is not `4` or `5` mod 9. The **exclusion rate** of a set of cells `(w, h)` is the proportion with `A^e(w, h) ≡ 4` or `5 (mod 9)`; if the residues are equidistributed it is `2/9 = 22.22%`. [[sum-of-three-cubes-castles](pages/sum-of-three-cubes-castles.md)] measured `20.46%` (179 of the 875 cells with `w ≥ 4` and `A(w, h) ≤ 10^9`) and `20.10%` for the row `h = 7` over its period 2184.

This page computes the exclusion rate row by row, column by column, and over the cells with `A(w, h) ≤ N`. The aggregate rate tends to `2/9` (section *The aggregate over A(w, h) ≤ N*), some columns have rate exactly `2/9`, and no row with `h ≤ 40` is uniform. [[mod-9-coset-lift](pages/mod-9-coset-lift.md)] proves the periods and the uniformity of the column `w = 4`.

## The row reading (fixed h)

For fixed `h`, `A^e(·, h) mod 9` is periodic in `w` from `w = 2`, with period `per_h` ([[mod-9-coset-lift](pages/mod-9-coset-lift.md)], section *The row/column divisibility gap*). Over one period:[^exec]

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
| 15 | (the `5,000,000` values `w = 2, …, 5,000,001`; period 25,170,390,960) | 1111880 | 22.238% | `554871, 555731, 555381, 554956, 554891, 556989, 556118, 554630, 556433` |

- **The rates approach `2/9`.** From `h = 9` on every row is within `0.5` percentage points of `22.222%`, and `h = 12, 13, 14, 15` are within `0.1`.
- **The row `h = 7`.** The mean count per residue is `2184/9 = 242.67`; residues 4 and 5 have 220 and 219, and residue 7 has 268. Since 9 does not divide 2184, no row histogram can be flat; the closest would have counts 242 and 243.
- **The rows `h = 2, 3`** have rates `2/24 = 1/12` (a closed form on [[sum-of-three-cubes-castles](pages/sum-of-three-cubes-castles.md)]) and `3/24 = 1/8`.

**No row with `h ≤ 40` is uniform mod 9.** Its period divides `per_h`, and `per_h` is not divisible by 9 for any `h ≤ 40` ([[mod-9-coset-lift](pages/mod-9-coset-lift.md)]), so the nine counts over one period cannot be equal.

## The column reading (fixed w)

For `2 ≤ w ≤ 293`, `A^e(w, ·) mod 9` is periodic in `h` from `h = 2` with minimal period `per_w = 2 · 3^{⌈log_3 w⌉ + 1}` ([[mod-9-coset-lift](pages/mod-9-coset-lift.md)], section *The row/column divisibility gap*). Every `per_w` is divisible by 9 (`18, 54, 162, 486, 1458, 4374`), so a flat histogram is possible, and some columns have one:[^exec]

| `w` | `per_w` | excluded | rate | histogram |
|---|---|---|---|---|
| 2 | 18 | 2 | 11.11% | `[10, 1, 1, 1, 1, 1, 1, 1, 1]` |
| 3 | 18 | 2 | 11.11% | `[2, 5, 0, 2, 2, 0, 5, 2, 0]` |
| **4** | 54 | 12 | **22.22%** | **uniform** `[6, 6, 6, 6, 6, 6, 6, 6, 6]` |
| 5 | 54 | 8 | 14.81% | `[4, 7, 4, 7, 4, 4, 10, 10, 4]` |
| **6** | 54 | 12 | **22.22%** | **uniform** `[6]*9` |
| 7 | 54 | 10 | 18.52% | `[5, 5, 11, 2, 2, 8, 5, 5, 11]` |
| 8 | 54 | 6 | 11.11% | `[17, 8, 4, 11, 2, 4, 2, 2, 4]` |
| 9 | 54 | 15 | 27.78% | `[6, 6, 3, 6, 12, 3, 12, 6, 0]` |
| **10** | 162 | 36 | **22.22%** | **uniform** `[18]*9` |
| 11..16 | 162 | | | uniform only at `w = 12` |
| **17** | 162 | 36 | **22.22%** | **uniform** `[18]*9` |
| 18..27 | 162 | | | none uniform |
| **28, 30** | 486 | 108 | **22.22%** | **uniform** `[54]*9` |
| **35** | 486 | 108 | **22.22%** | **uniform** `[54]*9` |
| **82, 84, 89** | 1458 | 324 | **22.22%** | **uniform** `[162]*9` |
| **244, 246, 251** | 4374 | 972 | **22.22%** | **uniform** `[486]*9` |

The uniform columns with `w ≤ 293` are[^exec]

```
w in {4, 6, 10, 12, 17, 28, 30, 35, 82, 84, 89, 244, 246, 251}
```

and each has exclusion rate exactly `2/9`. For `w = 4` the uniformity is proved on [[mod-9-coset-lift](pages/mod-9-coset-lift.md)] (section *The w = 4 proof*).

**The uniform columns by bracket.** Group the columns by `k = ⌈log_3 w⌉`, so that the bracket `k` is `[3^{k−1} + 1, 3^k]` with period `per_w = 2 · 3^{k+1}`. Within each bracket the uniform columns sit at the same offsets from `3^{k−1} + 1`:

| bracket `k` | `w` range | `per_w` | uniform `w` | offsets from `3^{k−1} + 1` |
|---|---|---|---|---|
| 2 | `[4, 9]` | 54 | `4, 6` | `0, 2` |
| 3 | `[10, 27]` | 162 | `10, 12, 17` | `0, 2, 7` |
| 4 | `[28, 81]` | 486 | `28, 30, 35` | `0, 2, 7` |
| 5 | `[82, 243]` | 1458 | `82, 84, 89` | `0, 2, 7` |
| 6 | `[244, 729]`, computed to 293 | 4374 | `244, 246, 251` | `0, 2, 7` |

The offset 7 does not fit in bracket 2. So for `w ≤ 293` the uniform columns are

```
3^{k−1} + 1  =  4, 10, 28, 82, 244      (k ≥ 2)
3^{k−1} + 3  =  6, 12, 30, 84, 246      (k ≥ 2)
3^{k−1} + 8  =  17, 35, 89, 251         (k ≥ 3)
```

For `k ≥ 3`, `3^{k−1} ≡ 0 (mod 9)`, so these columns satisfy `w ≡ 1, 3` or `8 (mod 9)`. Other columns in the same classes, such as `w = 19` and `w = 37`, are not uniform. [[mod-9-coset-lift](pages/mod-9-coset-lift.md)] (section *The coset-lift criterion*) characterizes the uniform columns for `2 ≤ w ≤ 293` by the differences of `A^e(w, ·)` over a shift of `per_w/3`.

**Columns with rate `2/9` that are not uniform.** For `w ≤ 293` these are[^exec]

```
w in {31, 39, 64, 93, 97, 191, 203, 227, 289}
```

with `count(4) + count(5) = 2 per_w / 9` but unequal counts. For example, `w = 31` has `[51, 60, 48, 60, 60, 48, 60, 51, 48]`.

Over `2 ≤ w ≤ 293` the column rates range from `1/9`, at `w = 2, 3, 8` only, to `49/162 = 30.25%`, at `w = 14`.

## The aggregate over A(w, h) ≤ N

The census of [[sum-of-three-cubes-castles](pages/sum-of-three-cubes-castles.md)] counts the cells `(w, h)` with `w ≥ 4`, `h ≥ 2` and `A(w, h) = h^w − (h−1)^w ≤ N`. For fixed `w` there are `n_w(N) = (N/w)^{1/(w−1)} + O(1)` such cells, so the column `w = 4` has about `N^{1/3}` cells and `w = 5` about `N^{1/4}`. The aggregate rate is the cell-weighted mean of the column rates:[^exec]

| `N` | cells `w ≥ 4` | excluded | rate | deficit below `2/9` |
|---|---|---|---|---|
| `10^6` | 119 | 21 | 17.647% | 4.58 points |
| `10^9` | 875 | 179 | 20.457% | 1.77 points |
| `10^12` | 7,367 | 1,574 | 21.366% | 0.86 points |
| `10^15` | 68,020 | 14,814 | 21.779% | 0.44 points |
| `10^18` | 655,355 | 144,015 | 21.975% | 0.25 points |
| `10^24` | 63,719,987 | 14,110,011 | 22.144% | 0.08 points |
| `10^36` | 630,641,206,298 | 140,092,917,085 | 22.2144% | 0.008 points |

**Proposition.** As `N → ∞`, the deficit `2/9 − rate(N)` is

```
(4/54) · (4^{1/3}/5^{1/4}) · N^{−1/12}  +  O(N^{−1/6} log N),        (4/54) · 4^{1/3}/5^{1/4}  =  0.078634.
```

*Proof.* The column `w = 4` has exclusion rate exactly `2/9` over each period of 54 (the `w = 4` proof), so it contributes `(2/9) n_4 + O(1)` exclusions; the column `w = 6` has rate `2/9` and the column `w = 5` rate `8/54` over their periods of 54 (computed), contributing `(2/9) n_6 + O(1)` and `(8/54) n_5 + O(1)`. The columns `7 ≤ w ≤ log_2(N + 1)` have `O(N^{1/6})` cells each, `O(N^{1/6} log N)` in all. So the deficit is `[(4/54) n_5 + O(N^{1/6} log N)]/(n_4 + O(N^{1/4}))`, and `n_5/n_4 = (4^{1/3}/5^{1/4}) N^{−1/12}(1 + O(N^{−1/4}))`. ∎

Against the computed deficits:[^exec]

| `N` | computed deficit | `0.0786 · N^{−1/12}` | ratio |
|---|---|---|---|
| `10^{15}` | `4.43 · 10^{−3}` | `4.42 · 10^{−3}` | 1.003 |
| `10^{18}` | `2.47 · 10^{−3}` | `2.49 · 10^{−3}` | 0.994 |
| `10^{24}` | `7.85 · 10^{−4}` | `7.86 · 10^{−4}` | 0.998 |
| `10^{36}` | `7.86 · 10^{−5}` | `7.86 · 10^{−5}` | 1.000 |

The log-log slopes of the computed deficit between `10^{15}` and `10^{18}`, `10^{18}` and `10^{24}`, and `10^{24}` and `10^{36}` are `−0.0846`, `−0.0831` and `−0.0833`. At smaller `N` the columns `w = 7, 8, 9`, whose cell counts relative to `w = 4` are of order `N^{−1/6}`, `N^{−4/21}` and `N^{−5/24}`, still matter, and the ratio is `1.84` at `N = 10^6`. At `N = 10^9` the rate `20.46%` is below `2/9` because the columns `w = 5, 7, 8`, with rates `14.81%`, `18.52%` and `11.11%`, carry a share of the cells that tends to 0 as `N` grows.

## Distribution of P(k, ·) mod 9

The signed tower counts `P(k, L) mod 9` for fixed `k` are not equidistributed over their periods in the base length `L` ([[castle-notation](pages/castle-notation.md)]):[^exec]

| `k` | period of `P(k, ·) mod 9` | histogram over `0..8` |
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

At `k = 1`, `P(1, L) = Re((1+i)^{L+1})` vanishes when `L ≡ 1 (mod 4)`, which gives 6 zeros in 24. For `k ≥ 5` every count is within a factor 1.3 of the mean, except at `k = 8` (26 zeros in 60). `A^e(w, h)` uses the difference `P(h−2, w) − P(h−1, w)`, and its rows for `h ≥ 9` are within 0.5 points of `2/9`.

## No {4, 5} pairing

Since `4 + 5 = 9`, the residues 4 and 5 are negatives of each other mod 9, so a map `(w, h) ↦ (w′, h′)` with `A^e(w′, h′) ≡ −A^e(w, h)` would force `count(4) = count(5)`. No row `h ≤ 8` has a shift `s` with `A^e(w + s, h) ≡ −A^e(w, h)` for all `w`, or a reflection `c` with `A^e(c − w, h) ≡ −A^e(w, h)` for all `w`, and no column `3 ≤ w ≤ 15` has one in `h`.[^exec] The column `w = 2` has the reflection `h ↦ 10 − h (mod 18)`, because `A^e(2, h) = 2h − 1` for even `h` and `0` for odd `h`.

The rows confirm it: `count(4) − count(5)` for `h = 2, …, 11` is `2, −1, −6, −16, 0, 1, −46, −28, 73, −58`.

## Castle counts within 1 of a cube

The cells `(w, h)` with `w ≥ 3`, `h ≥ 2` and `A(w, h) ≤ 10^9` at which `A^e`, `A` or `A^o` is within 1 of a cube:[^exec]

| count | cell | value | as `c^3 + j` | source |
|---|---|---|---|---|
| `A^e` | `(6, 2)` | 28 | `3^3 + 1` | |
| `A^e` | `(6, 4)` | 1729 | `12^3 + 1` | [[hardy-ramanujan-castle](pages/hardy-ramanujan-castle.md)] |
| `A^e` | `(3, 91)` | 4095 | `16^3 − 1` | `C(91, 2)` |
| `A^e` | `(13, 2)` | 4096 | `16^3` | `2^{w−1}`, `w ≡ 1 (mod 12)` |
| `A^e` | `(3, 127)` | 8001 | `20^3 + 1` | `C(127, 2)` |
| `A^e` | `(25, 2)` | 16777216 | `256^3` | `2^{w−1}`, `w ≡ 1 (mod 12)` |
| `A` | `(3m, 2)`, `m = 1, …, 9` | `2^{3m} − 1` | `(2^m)^3 − 1` | `7, 63, 511, 4095, …, 134217727` |
| `A` | `(3, 9)` | 217 | `6^3 + 1` | |
| `A` | `(4, 3)` | 65 | `4^3 + 1` | |
| `A^o` | `(3, 2)` | 1 | `1^3` | |
| `A^o` | `(3, 8)` | 28 | `3^3 + 1` | `C(8, 2)` |
| `A^o` | `(5, 4)` | 342 | `7^3 − 1` | |
| `A^o` | `(13, 2)` | 4095 | `16^3 − 1` | `2^{w−1} − 1` |
| `A^o` | `(25, 2)` | 16777215 | `256^3 − 1` | `2^{w−1} − 1` |

**Height 2.** `A(w, 2) = 2^w − 1`, so `A(3m, 2) = (2^m)^3 − 1`. `A^e(w, 2)` is the sum of `C(w + 1, j)` over `j ≡ 2 (mod 4)`, which is `(2^{w+1} − 2 Re((1+i)^{w+1}))/4` ([[castle-counting-function](pages/castle-counting-function.md)]). For `w ≡ 1 (mod 4)` the real part vanishes and `A^e(w, 2) = 2^{w−1}`, a cube when also `3 | w − 1`, that is for `w ≡ 1 (mod 12)`: `A^e(13, 2) = 16^3`, `A^e(25, 2) = 256^3`, `A^e(37, 2) = 4096^3`. Then `A^o(w, 2) = 2^w − 1 − 2^{w−1} = 2^{w−1} − 1`.

**The column `w = 3`.** `P(k, 3) = (−1)^k (k + 1)^2` (the Lemma on [[mod-9-coset-lift](pages/mod-9-coset-lift.md)] reduces this to `k ≤ 6`, checked by summation), so `A^e(3, h) = C(h, 2) = h(h − 1)/2` for odd `h` and `5 C(h, 2) + 1` for even `h`, and `A^o(3, h) = A(3, h) − A^e(3, h)` is the other of the two: `5 C(h, 2) + 1` for odd `h` and `C(h, 2)` for even `h`. The triangular numbers within 1 of a cube satisfy

```
C(h, 2) = c^3 − 1   ⇔   Y^2 = X^3 − 7,
C(h, 2) = c^3 + 1   ⇔   Y^2 = X^3 + 9,          with  X = 2c,  Y = 2h − 1.
```

The integral points of these curves are `(2, ±1)`, `(32, ±181)` on `Y^2 = X^3 − 7` and `(−2, ±1)`, `(0, ±3)`, `(3, ±6)`, `(6, ±15)`, `(40, ±253)` on `Y^2 = X^3 + 9` (LMFDB).[^lmfdb] With `X` even, `Y` odd, `c ≥ 1` and `h ≥ 2`, the solutions are `h = 8` (`28 = 3^3 + 1`), `h = 91` (`4095 = 16^3 − 1`) and `h = 127` (`8001 = 20^3 + 1`). At `h = 8`, which is even, the triangular number 28 is `A^o(3, 8)`; at `h = 91` and `127` it is `A^e(3, h)`. The values `5 C(h, 2) + 1` are not within 1 of a cube for `h ≤ 200000` (computed).

**The column `w = 6`.** `A^e(6, 2) = 28` and `A^e(6, 4) = 1729` are within 1 of a cube; no other `h ≤ 44` (the cells with `A(6, h) ≤ 10^9`) is. For example `A^e(6, 6) = 16126 = 25^3 + 501`, `A^e(6, 8) = 75299 = 42^3 + 1211` and `A^e(6, 40) = 301446067 = 671^3 − 665644`.

## Appearances in Sources

- [[project-euler-502-solution](pages/project-euler-502-solution.md)] - the recurrences of `P(k, L)` in the base length and in the tower height.

## Related Concepts

- [[mod-9-coset-lift](pages/mod-9-coset-lift.md)] - the row and column periods, the proof for `w = 4`, the coset-lift criterion, and the repeated factors of `char_k mod 3`.
- [[sum-of-three-cubes-castles](pages/sum-of-three-cubes-castles.md)] - which castle counts are sums of three cubes, and the census at `N = 10^9`.
- [[sums-of-three-cubes](pages/sums-of-three-cubes.md)] - the residues 4 and 5 mod 9 and Heath-Brown's conjecture.
- [[mod-p-observatory](pages/mod-p-observatory.md)] - the periods of `A^e` modulo a prime.
- [[signed-tower-k-direction](pages/signed-tower-k-direction.md)] - the closed forms of `P(k, L)` in `k` and their periods modulo a prime.
- [[castle-counting-formula](pages/castle-counting-formula.md)] - the formula `A^e = (h^w − (h−1)^w − P(h−1, w) + P(h−2, w))/2`.
- [[hardy-ramanujan-castle](pages/hardy-ramanujan-castle.md)] - `A^e(6, 4) = 1729`.
- [[kitamasa](pages/kitamasa.md)] - jumping a linear recurrence over `Z/9` to a far index.
- [[oeis-mining-pe502](pages/oeis-mining-pe502.md)] - the tables of `A^e(w, h)` studied here mod 9.

## Footnotes

[^exec]: Verified by execution (Python 3.11 with NumPy and SymPy, 2026-10-16). Rows: `P(k, ·) mod 9` from the recurrence given by `den_k`, run in blocks of 4096 terms, and `A^e(w, h) ≡ 5 (h^w − (h−1)^w − P(h−1, w) + P(h−2, w)) (mod 9)` for `w = 2, …, 1 + per_h` (`h ≤ 14`) and `w = 2, …, 5,000,001` (`h = 15`); every row of the table reproduced. Columns: `P(k, L) mod 9` for `k ≤ 6600`, `L ≤ 293` from the series `num_k/den_k` truncated at degree 293, checked against summation over all towers for small `k, L`; for each `2 ≤ w ≤ 293` the histogram over one period, the uniform and rate-matched columns and the rate range. Aggregate: for each `N` and `w ≥ 4`, the largest `h` with `A(w, h) ≤ N` by binary search and the exclusions counted by whole periods plus the remainder; the slopes and ratios from the resulting deficits. `P(k, ·) mod 9` histograms for `k ≤ 10` with their minimal periods. Pairing: every shift and every reflection over one period for the rows `h ≤ 8` and the columns `w ≤ 15`. Cube-adjacency: exact `A`, `A^e`, `A^o` for every cell with `w ≥ 3`, `h ≥ 2`, `A(w, h) ≤ 10^9` (`P(k, 3)` from its closed form, checked by summation for `k ≤ 8`; `P(k, L)` for `L ≥ 4` from the exact truncated series), each tested against the two nearest cubes; the search `8c^3 − 7`, `8c^3 + 9` square for `c ≤ 10^6`; `5 C(h, 2) + 1` for `h ≤ 200000`.

[^lmfdb]: https://www.lmfdb.org/EllipticCurve/Q/5292/i/1 and https://www.lmfdb.org/EllipticCurve/Q/972/b/2 (read 2026-10-16) - the curves `y^2 = x^3 − 7` (5292.i1) and `y^2 = x^3 + 9` (972.b2), with integral points "(2, ±1), (32, ±181)" and "(−2, ±1), (0, ±3), (3, ±6), (6, ±15), (40, ±253)".
