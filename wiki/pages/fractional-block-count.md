---
title: Fractional block count
category: Analyses
summary: B_alpha(C) = sum_i max(0, Delta^alpha c_i), with Delta^alpha the Grunwald-Letnikov fractional difference of the skyline (binomial weights (-1)^k C(alpha, k) over every earlier column), is the area at alpha = 0 and the block count at alpha = 1, checked on all 5460 castles with w <= 6, h <= 4. For 0 < alpha < 1 it is the sum of the amounts by which each column exceeds a power-law weighted average of the columns to its left. B_{1/2} separates the ten even-block castles of width 4 and height 2 and 14 of the 15 castles of that width and height; at alpha = sqrt 2 - 1 it separates all 15. For nondecreasing skylines B_alpha = [x^w] (1 - x)^{alpha - 1} C(x), decreasing in alpha; the box gives B_alpha = h C(w - alpha, w - 1), which at alpha = 1/2 is 2hw C(2w, w)/4^w ~ 2h sqrt(w/pi). Over all castles with w <= 6, h <= 4, on a grid of 201 orders in [0, 1], 829 have B_alpha increasing somewhere, and these are the 829 whose B_alpha falls below the block count. The phase sum S_alpha = sum_C e^{i pi B_alpha(C)} runs from the area-parity sum (-1)^{w+h+1} at alpha = 0 to the signed count S(w, h) at alpha = 1.
tags: [analysis, castle, fractional-calculus, grunwald-letnikov, block-count, area, statistic, memory, power-law, arfima, compression, parity, computation, verification]
sources: [project-euler-502-castle-factoring, project-euler-502-brute-force]
created: 2026-09-19
updated: 2026-10-29
---

# Fractional block count

The area `sum c_i` of a castle is the sum of its column heights, and its block count is the sum of the positive parts of its column differences ([[castle-sign](pages/castle-sign.md)]). This page defines one statistic `B_alpha` that equals the area at `alpha = 0` and the block count at `alpha = 1`, with the Grunwald-Letnikov fractional difference supplying the orders in between.

## Definition

Write the skyline as `c = (c_1, ..., c_w)` with `c_i in {1, ..., h}`, and put `c_j = 0` for every `j <= 0` ([[castle-representations](pages/castle-representations.md)]). The **Grunwald-Letnikov difference of order `alpha`** at column `i` is[^1]

```
Delta^alpha c_i  =  sum_{k = 0}^{i - 1}  w_k(alpha) c_{i - k},        w_k(alpha) = (-1)^k C(alpha, k),          (1)
```

where `C(alpha, k) = alpha (alpha - 1) ... (alpha - k + 1) / k!` is the generalized binomial coefficient. At `alpha = 1` the weights are `1, -1, 0, 0, ...` and `Delta^1 c_i = c_i - c_{i-1}`; at `alpha = 0` the weights are `1, 0, 0, ...` and `Delta^0 c_i = c_i`. The **fractional block count** is

```
B_alpha(C)  =  sum_{i = 1}^{w}  max(0, Delta^alpha c_i).                                                  (2)
```

At `alpha = 0`, `B_0 = sum c_i` is the area. At `alpha = 1`, `B_1 = sum max(0, c_i - c_{i-1})` with `c_0 = 0` is the total ascent of the skyline, which is the block count: a column of height `b` after a column of height `a` starts `max(0, b - a)` new blocks.[^2] The block count is also the total descent `sum max(0, c_i - c_{i+1})` with `c_{w+1} = 0`;[^3] the fractional version uses the ascent form, so its memory runs from left to right. Both identities hold on all 5460 castles with `w <= 6` and `h <= 4`.[^exec]

At `alpha = 1/2` the weights are

```
w_0, w_1, w_2, ...  =  1, -1/2, -1/8, -1/16, -5/128, -7/256, -21/1024, ...
```

whose numerators in absolute value are A002596 and whose denominators are A046161, the denominators of `C(2k, k)/4^k`.[^4] The denominator of `w_k(1/2)` divides `2^{2k}`, so `B_{1/2}` of a castle of width `w` is an integer multiple of `2^{-(2w - 2)}`.

## The memory reading

For `0 < alpha < 1` every weight after the first is negative, and their absolute values sum to 1:

```
w_k(alpha)  =  -alpha (1 - alpha)(2 - alpha) ... (k - 1 - alpha) / k!  <  0        (k >= 1),
sum_{k >= 1} |w_k(alpha)|  =  1,            |w_k(alpha)|  ~  alpha / (Gamma(1 - alpha) k^{1 + alpha}).
```

The sum is 1 because `sum_k w_k(alpha) = (1 - 1)^alpha = 0`. So `Delta^alpha c_i = c_i - (weighted average of c_{i-1}, c_{i-2}, ...)`, with weights that form a probability distribution with a power-law tail, and `B_alpha` adds up the amounts by which each column exceeds that weighted average of the columns to its left. At `alpha = 1/2` the partial sums of `|w_k|` are `0.727` through `k = 4`, `0.860` through 16, `0.930` through 64 and `0.982` through 1024; a castle of width 6 uses `k <= 5`, about three quarters of the total weight.[^exec]

**Small `alpha`.** Since `(-1)^k C(alpha, k) = -alpha / k + O(alpha^2)` for `k >= 1`,

```
B_alpha(C)  =  area(C)  -  alpha * sum_{j = 1}^{w} c_j H_{w - j}  +  O(alpha^2),
```

with `H_n = 1 + 1/2 + ... + 1/n` the harmonic numbers (`H_0 = 0`). The slope at `alpha = 0` weights the cells of column `j` by `H_{w-j}`, the harmonic number of the number of columns to its right. Finite differences reproduce the slope on `(1, 2, 2, 1)` (`-6.8333`), `(3, 1, 2, 3, 1)` (`-14.0833`) and `(1, 1, 1, 4)` (`-4.3333`).[^exec] So `B_alpha` depends on the positions of the cells, not only on their number.

## Worked example: the ten even-block castles of width 4 and height 2

The even-block castles of width 4 and height 2 are the `A^e(4, 2) = 10` of the Project Euler statement (its `F(4, 2)`; [[castle-counting-function](pages/castle-counting-function.md)]). Their half-order residuals and fractional block counts:[^exec]

| castle | area | blocks | `Delta^{1/2} c` | `B_{1/2}` |
|---|---|---|---|---|
| `(2, 1, 1, 1)` | 5 | 2 | `2, 0, 0.25, 0.25` | **2.5** |
| `(1, 2, 1, 1)` | 5 | 2 | `1, 1.5, -0.125, 0.1875` | **2.6875** |
| `(1, 1, 2, 1)` | 5 | 2 | `1, 0.5, 1.375, -0.1875` | **2.875** |
| `(2, 2, 1, 1)` | 6 | 2 | `2, 1, -0.25, 0.125` | **3.125** |
| `(1, 1, 1, 2)` | 5 | 2 | `1, 0.5, 0.375, 1.3125` | **3.1875** |
| `(1, 2, 2, 1)` | 6 | 2 | `1, 1.5, 0.875, -0.3125` | **3.375** |
| `(1, 1, 2, 2)` | 6 | 2 | `1, 0.5, 1.375, 0.8125` | **3.6875** |
| `(2, 2, 2, 1)` | 7 | 2 | `2, 1, 0.75, -0.375` | **3.75** |
| `(1, 2, 2, 2)` | 7 | 2 | `1, 1.5, 0.875, 0.6875` | **4.0625** |
| `(2, 2, 2, 2)` | 8 | 2 | `2, 1, 0.75, 0.625` | **4.375** |

All ten have two blocks, and they have four distinct areas; `B_{1/2}` takes ten distinct values. The castles `(1, 1, 1, 2)` and `(1, 1, 2, 1)` have the same area and the same blocks and `B_{1/2} = 3.1875` and `2.875`. Over all 15 castles of width 4 and height 2, `B_{1/2}` takes 14 distinct values and `B_alpha` at `alpha = sqrt(2) - 1` takes 15.[^exec]

## Distinguishing power

The same count for larger widths and heights (`B_irr` is `B_alpha` at `alpha = sqrt(2) - 1`):[^exec]

| `(w, h)` | castles | even-block | distinct area | distinct blocks | distinct `(area, blocks)` | distinct `B_{1/2}` | distinct `B_irr` |
|---|---|---|---|---|---|---|---|
| `(4, 2)` | 15 | 10 | 4 | 2 | 6 | 14 | 15 |
| `(6, 2)` | 63 | 28 | 6 | 3 | 12 | 59 | 63 |
| `(8, 2)` | 255 | 120 | 8 | 4 | 20 | 241 | 253 |
| `(4, 3)` | 65 | 21 | 7 | 3 | 15 | 41 | 63 |
| `(6, 3)` | 665 | 307 | 11 | 5 | 35 | 433 | 657 |
| `(7, 3)` | 2059 | 977 | 13 | 7 | 48 | 1400 | 2021 |
| `(5, 4)` | 781 | 439 | 13 | 7 | 46 | 283 | 659 |
| `(6, 4)` | 3367 | 1729 | 16 | 7 | 70 | 1017 | 2866 |
| `(5, 5)` | 2101 | 906 | 17 | 9 | 75 | 470 | 1644 |

The pair `(area, blocks)` takes a few percent as many values as there are castles; `B_irr` takes most of them.

**Collisions at `alpha = 1/2`.** `B_{1/2}` lies in `2^{-(2w-2)} Z`, and many distinct castles share a value; at `alpha = sqrt(2) - 1` most of them separate. At width 8 and height 2 there are 14 collisions at `1/2` and 2 at `sqrt(2) - 1`.

**Collisions on an interval of orders.** Among the castles of width 5 and height 4, 126 pairs have equal `B_alpha` at all 50 orders `alpha = 0.50, 0.51, ..., 0.99`, and 555 pairs among those of width 6 and height 4 (exact rational arithmetic).[^exec] In 117 of the 126 and 525 of the 555, the two castles agree up to some column and every residual after it is `<= 0` at every tested order, for example `(1, 1, 1, 4, 1)` and `(1, 1, 1, 4, 2)`, or `(1, 1, 4, 1, 1)` and `(1, 1, 4, 2, 1)`. Since `B_alpha` adds only positive residuals, two such castles have the same `B_alpha` wherever those residuals stay `<= 0`. At smaller `alpha` the residuals of the differing columns turn positive and the pair separates: `B_{0.1}` of the first pair differs by exactly 1. The other 9 and 30 pairs differ already in the second or third column, as `(2, 1, 2, 4, 4)` and `(2, 3, 3, 2, 4)` do; their sums of positive residuals agree at the 50 tested orders and separate below `1/2` (by `0.0094` at `alpha = 0.49` for that pair). No two distinct castles have equal `B_alpha` at all 49 orders `k/50`, `0 < k < 50`, among the castles of width 6 and height 3, width 7 and height 3, and width 5 and height 4.[^exec]

**Reversal.** Area and block count do not change when the skyline is reversed; `B_alpha` does. The castles with `B_{1/2}(c) = B_{1/2}(reverse c)` are the 19 palindromes at width 5 and height 3, 25 castles against 19 palindromes at width 6 and height 3, and 41 against 37 palindromes at width 5 and height 4.[^exec]

## The shape of `B_alpha` as a function of `alpha`

Each residual is a polynomial in `alpha`, so `B_alpha(C)` is continuous and piecewise polynomial in `alpha`. On the 5460 castles with `w <= 6`, `h <= 4`, on a grid of 201 orders in `[0, 1]`:[^exec]

- **It is not always decreasing.** 829 castles have an increase somewhere on the grid. The largest single step is `0.0138` per `0.005` of `alpha`, and the largest total increase over `[0, 1]` is `0.47`, on the three castles `(4, 3, 1, 4, 1, c_6)` with `c_6 = 2, 3, 4` (8, 9 and 10 blocks). Every nondecreasing castle is decreasing in `alpha` (section *Generating functions*), so every increase belongs to a castle with a descent.
- **It is at most the area** for every castle and every `alpha` in `[0, 1]`: every weight after the first is at most 0 and the heights are positive, so `Delta^alpha c_i <= c_i`.
- **It can fall below the block count.** The 829 castles with an increase are exactly the castles with `B_alpha < blocks` somewhere on the grid. `(4, 3, 1, 4, 1, 2)` has 8 blocks and `B_{0.8} = 7.58`; its residuals at `alpha = 0.8` are `4.0, -0.2, -1.72, 2.83, -2.45, 0.75`, and the two positive ones, at columns 4 and 6, are smaller than the ascents 3 and 1 there, because the weight on the `4` in column 1 is still being subtracted.

For the castles of each width and height below, the mean of `B_alpha` over the castles is convex and decreasing in `alpha` on a grid of step `0.01`, and the variance has an interior minimum:[^exec]

| `(w, h)` | `alpha` | 0 | 0.25 | 0.5 | 0.75 | 1 | argmin of variance |
|---|---|---|---|---|---|---|---|
| `(6, 3)` | mean | 12.289 | 8.461 | 6.229 | 5.047 | 4.364 | 0.72 |
| | variance | 3.291 | 1.671 | 0.773 | 0.593 | 0.893 | |
| `(8, 2)` | mean | 12.016 | 7.684 | 5.234 | 4.007 | 3.259 | 0.69 |
| | variance | 1.945 | 0.845 | 0.443 | 0.344 | 0.545 | |
| `(5, 4)` | mean | 13.278 | 9.601 | 7.348 | 6.070 | 5.380 | 0.70 |
| | variance | 4.608 | 2.440 | 1.133 | 0.864 | 1.278 | |

The argmin is on a grid of step `0.01`. The mean at `alpha = 1/2` is below the average of the endpoint means (`6.23` against `8.33` at width 6 and height 3), as convexity requires.

## Generating functions

Write the skyline as the polynomial `C(x) = sum_{i=1}^{w} c_i x^i`. The weights `w_k(alpha)` are the coefficients of `(1 - x)^alpha`, so Equation (1) is a product of series:

```
sum_i (Delta^alpha c_i) x^i  =  (1 - x)^alpha C(x)          (mod x^{w+1}).                                (3)
```

**The fractional difference is invertible.** Since `(1 - x)^{-alpha} (1 - x)^alpha = 1`, multiplying by `(1 - x)^{-alpha}` inverts Equation (3): the map from skyline to residuals is a lower-triangular Toeplitz matrix with ones on the diagonal. So the residuals determine the castle, and `B_alpha` loses information only through the positive part.

**Proposition (nondecreasing castles).** If `c_1 <= c_2 <= ... <= c_w` and `0 <= alpha <= 1`, then every residual is nonnegative,

```
B_alpha(C)  =  [x^w] (1 - x)^{alpha - 1} C(x)  =  sum_{j=1}^{w} d_j [x^{w-j}] (1 - x)^{alpha - 2},          (4)
```

with `d_j = c_j - c_{j-1} >= 0` the ascents, and `B_alpha` is decreasing in `alpha`.

*Proof.* `(1 - x)^alpha C(x) = (1 - x)^{-(1 - alpha)} D(x)` with `D(x) = (1 - x) C(x) = sum d_j x^j`, and `(1 - x)^{-(1 - alpha)}` has nonnegative coefficients for `0 <= alpha <= 1`. So every residual is nonnegative, `B_alpha` is the sum of the residuals, and summing the coefficients through `x^w` is multiplication by `1/(1 - x)`, which gives Equation (4). The coefficient `[x^n] (1 - x)^{-beta} = beta (beta + 1) ... (beta + n - 1) / n!` increases with `beta`, and `beta = 2 - alpha`, so every coefficient in Equation (4) decreases as `alpha` increases.

Equation (4) agrees with the direct computation on all 791 nondecreasing castles with `w <= 7`, `h <= 5`, at 41 orders.[^exec]

**The box.** For `c_i = h` the ascents are `d = (h, 0, ..., 0)`, and Equation (4) gives

```
B_alpha(box_{w,h})  =  h [x^{w-1}] (1 - x)^{alpha - 2}  =  h C(w - alpha, w - 1)
                    =  h Gamma(w + 1 - alpha) / (Gamma(w) Gamma(2 - alpha))  ~  h w^{1 - alpha} / Gamma(2 - alpha).
```

At `alpha = 0` this is `hw`, the area; at `alpha = 1` it is `h`, the block count of the box, one block per row. At `alpha = 1/2`,

```
B_{1/2}(box_{w,h})  =  h sum_{i=0}^{w-1} C(2i, i) / 4^i  =  2hw C(2w, w) / 4^w  ~  2h sqrt(w / pi),
```

whose numerators `1, 3, 15, 35, 315, 693, 3003, ...` for `h = 1` are A001803, the numerators of `(1 - x)^{-3/2}`.[^4] Since `area * blocks = h^2 w`, this is `(2 / sqrt(pi)) sqrt(area * blocks)` in the limit, with `2 / sqrt(pi) = 1.128`. Values at `h = 3`:[^exec]

| `w` | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|---|---|
| `B_{1/2}(box_{w,3})` | 3 | 4.5 | 5.625 | 6.5625 | 7.3828 | 8.1211 | 8.7979 | 9.4263 |
| ratio to `2h sqrt(w/pi)` | 0.886 | 0.940 | 0.959 | 0.969 | 0.975 | 0.979 | 0.982 | 0.985 |

At `w = 200` the ratio of `h C(w - alpha, w - 1)` to `h w^{1-alpha} / Gamma(2 - alpha)` is `0.9995`, `0.9994` and `0.9995` at `alpha = 1/4, 1/2, 3/4`.

**The ramp.** For `c_i = i` every ascent is 1, and Equation (4) gives `B_alpha = [x^{w-1}] (1 - x)^{alpha - 3} = C(w + 1 - alpha, w - 1)`, which grows like `w^{2 - alpha}`. At `alpha = 1/2` and `w = 6` it is `11.7305`, the value of the direct computation.

## The polynomial `Z(q, alpha)`

Grade the castles of width `w` and height `h` by `B_alpha`:

```
Z_{w,h}(q, alpha)  =  sum_C  q^{B_alpha(C)}.
```

At `alpha = 0` this is the area polynomial of the castles of width `w` and height `h` ([[castle-by-area](pages/castle-by-area.md)] counts castles by area over all widths and heights). At `alpha = 1` it is their block-count polynomial, whose residue classes modulo `m` are the character sums of [[block-count-constraints](pages/block-count-constraints.md)]; in particular `Z_{w,h}(-1, 1) = S(w, h)`, the signed count, and `A^e(w, h) = (A(w, h) + Z_{w,h}(-1, 1)) / 2` ([[castle-notation](pages/castle-notation.md)]).

For non-integer `alpha` the exponents `B_alpha(C)` are not integers, and `Z` is a finite sum `sum_C q^{b_C}` with real exponents. At `alpha = 1/2`, the 665 castles of width 6 and height 3 have 433 distinct exponents, all dyadic, from `3.6992` to `8.4336`, with largest multiplicity 5.[^exec]

## The fractional sign

The castle sign is `(-1)^{blocks} = e^{i pi B_1}` ([[castle-sign](pages/castle-sign.md)]). Replacing `B_1` by `B_alpha` gives a point `e^{i pi B_alpha(C)}` on the unit circle, and its sum over the castles of width `w` and height `h`,

```
S_alpha(w, h)  =  sum_C  e^{i pi B_alpha(C)},
```

written `S_alpha` because it sums over castles and `S_1 = S(w, h)` is the signed count. At `alpha = 0`, `S_0 = sum (-1)^{area}`. Summing `(-1)^c` over `c in {1, ..., h}` gives `-1` for odd `h` and `0` for even `h`, so `S_0(w, h) = (sum_{c <= h} (-1)^c)^w - (sum_{c <= h-1} (-1)^c)^w = (-1)^{w + h + 1}` for every `w >= 1` and `h`, and the castles of even area number `(A(w, h) + (-1)^{w+h+1}) / 2`. In between:[^exec]

| `(w, h)` | `A` | `S_0` | `abs(S_alpha)` at `alpha = 0.1, 0.25, 0.5, 0.75, 0.9` | `S_1 = S(w, h)` |
|---|---|---|---|---|
| `(8, 2)` | 255 | -1 | `1.00, 1.01, 35.5, 49.2, 24.4` | -15 |
| `(6, 3)` | 665 | +1 | `0.19, 0.31, 8.57, 29.8, 41.0` | -51 |
| `(5, 4)` | 781 | +1 | `0.33, 1.11, 6.35, 47.1, 98.0` | +97 |
| `(6, 4)` | 3367 | -1 | `0.19, 0.99, 10.5, 104.2, 157.0` | +91 |

`abs(S_alpha)` stays below 1.2 through `alpha = 0.25` and exceeds `abs(S_1)` somewhere in `(0.5, 1)` in every row: `49.2` against `15` at width 8 and height 2, `157.0` against `91` at width 6 and height 4.

## The residual cost

Drop the positive part and take the total residual size `sum_i abs(Delta^alpha c_i)`. For `0 < alpha < 1`, Equation (1) is fractional differencing by `(1 - B)^alpha`, with `B` the backshift: the operation that defines ARFIMA long-memory time series, in which a process is fractionally integrated of order `d` when `(1 - B)^d` turns it into white noise.[^5] The order that minimizes the residual cost estimates the integration order of a skyline. On sequences of width 64, centered before differencing, with the minimum taken over a grid of step `0.01` in `[0, 2.5]` and 20 random samples of each random kind (NumPy `default_rng(502)`; the fractionally integrated noise is `(1 - B)^{-d}` applied to Gaussian noise with 2000 burn-in terms):[^exec]

| skyline | argmin of `sum abs(Delta^alpha c_i)`: median (range) |
|---|---|
| i.i.d. uniform heights in `{1, ..., 8}` | `0.00` (`0.00` to `0.31`) |
| 1-smooth random walk (steps `-1, 0, +1`) | `1.00` (`0.64` to `1.00`) |
| ramp `1, 2, ..., 64` | `2.00` |
| fractionally integrated Gaussian noise, `d = 0.3` | `0.27` (`0.00` to `0.54`) |

For the ramp the minimum is at `alpha = 2`, where the second difference of the centered ramp is nonzero only in its first two terms. In the ladder of encodings of [[castle-compression](pages/castle-compression.md)], `alpha = 0` codes the heights (the skyline) and `alpha = 1` the first differences, which the run-length descriptions record.

## Appearances in Sources

- [[project-euler-502-castle-factoring](pages/project-euler-502-castle-factoring.md)] - the block count as the total descent of the column heights.
- [[project-euler-502-brute-force](pages/project-euler-502-brute-force.md)] - the block count as maximal horizontal runs and as the total ascent, `max(0, b - a)` per column step.

## Related Concepts

- [[castle-sign](pages/castle-sign.md)] - the sign `(-1)^{blocks} = e^{i pi B_1}`, of which `e^{i pi B_alpha}` is the fractional version.
- [[castle-by-area](pages/castle-by-area.md)] - castles counted by area, the grading of `Z(q, 0)`.
- [[block-count-constraints](pages/block-count-constraints.md)] - castles selected by block count, the grading of `Z(q, 1)`.
- [[castle-representations](pages/castle-representations.md)] - the skyline tuple on which the difference operator acts.
- [[monotone-streak-factorization](pages/monotone-streak-factorization.md)] - the first differences whose positive parts sum to the block count.
- [[castle-compression](pages/castle-compression.md)] and [[castle-entropy](pages/castle-entropy.md)] - code lengths of skylines, and the cost of the even-block condition.
- [[castle-conditional-entropy](pages/castle-conditional-entropy.md)] - `H(C | B_{1/2}) = 0` on the ten even-block castles of width 4 and height 2, against `H(C | N)` for the area and `H(C | B)` for the block count.
- [[castle-counting-function](pages/castle-counting-function.md)] - `A^e(4, 2) = 10`, the worked example.
- [[castle-snippets](pages/castle-snippets.md)] - `all_castles` and the block count.
- [[image-as-castle](pages/image-as-castle.md)] and [[song-as-castle](pages/song-as-castle.md)] - skylines from images and audio, to which the residual cost applies.
- [[fractional-width-and-height](pages/fractional-width-and-height.md)] - the castle counts interpolated in the width and the height, with the same `(1 - x)^{-1/2}` coefficients in the half-column of the nondecreasing rule.
- [[power-law-memory-rules](pages/power-law-memory-rules.md)] - the same weights used in a strip rule instead of a statistic.
- [[half-derivative-seminar](pages/half-derivative-seminar.md)] - a seminar on this page with the half-sum, the fractional width and height, and the walk on a tree castle.

## Footnotes

[^1]: https://en.wikipedia.org/wiki/Gr%C3%BCnwald%E2%80%93Letnikov_derivative (read 2026-09-19) [synthesis] - the Grunwald-Letnikov derivative of order `alpha` is the limit of `h^{-alpha} sum_k (-1)^k C(alpha, k) f(x - k h)` with generalized binomial coefficients, the ordinary `n`-th difference when `alpha = n` is an integer; Equation (1) is that difference with `h = 1` on the columns.
[^2]: [[project-euler-502-brute-force](pages/project-euler-502-brute-force.md)] §"Column-height encoding" L20-24, §"p_signed" L31 - "A block is a maximal horizontal run of columns at a given level, so #blocks = sum_{r=1}^{h} #{runs of columns with c_i >= r} = c_1 + sum_{i=2}^{w} max(0, c_i - c_{i-1})"; "A new column of height b after a column of height a starts max(0, b - a) new runs".
[^3]: [[project-euler-502-castle-factoring](pages/project-euler-502-castle-factoring.md)] §"The sign of a castle" L104-108 - "In the column-height form, the block count is the total descent: blocks = sum_{i=0}^{L} max(0, c_i - c_{i+1}), c_0 = c_{L+1} = 0".
[^4]: https://oeis.org/A002596, https://oeis.org/A046161, https://oeis.org/A001803 (read 2026-10-16) - "Numerators in expansion of sqrt(1+x). Absolute values give numerators in expansion of sqrt(1-x)"; "a(n) = denominator of binomial(2n,n)/4^n", data `1, 2, 8, 16, 128, 256, 1024, ...`; "Numerators in expansion of (1 - x)^(-3/2)", data `1, 3, 15, 35, 315, 693, 3003, ...`.
[^5]: https://en.wikipedia.org/wiki/Autoregressive_fractionally_integrated_moving_average (read 2026-09-19) [synthesis] - ARFIMA allows the differencing order `d` to be a non-integer; the fractional differencing operator `(1 - B)^d` is the binomial series `sum_k C(d, k) (-B)^k`, and processes with `0 < d < 1/2` have long memory with power-law autocorrelation decay.
[^exec]: Verified by execution (Python 3.11 with NumPy, 2026-10-16): the endpoint identities `B_0 = area`, `B_1 = blocks` in exact rational arithmetic on all 5460 castles with `w <= 6`, `h <= 4`; the half-order weights and the dyadic bound for `w <= 6`, `h = 3`; the partial sums of `|w_k(1/2)|`; the slope formula by finite differences at `alpha = 10^{-6}`; the table of the ten castles; the distinct-value table (`B_{1/2}` exact, `B_irr` rounded to `10^{-9}`); the 126 and 555 pairs equal at the 50 orders `0.50, ..., 0.99` in exact arithmetic, with the residual sign test (117 and 525) and the first differing column of the rest, and the absence of pairs equal at the 49 orders `k/50` for the castles of width 6 and height 3, width 7 and height 3, and width 5 and height 4; the reversal counts; the 201-order census (829 castles with an increase, the same 829 with `B_alpha < blocks`, largest step `0.0138`, largest total increase `0.4746`, no castle above its area, none of the 829 nondecreasing); means, variances, convexity, monotonicity and the argmin of the variance on a grid of step `0.01`; Equation (4) on all 791 nondecreasing castles with `w <= 7`, `h <= 5` at 41 orders, with nonnegative residuals and monotonicity; the box values for `w <= 8` at `h = 3`, the identity `sum_{i<w} C(2i, i)/4^i = 2w C(2w, w)/4^w` for `w <= 11`, and the ratios at `w = 200`; the ramp at `w = 6`; the exponents of `Z_{6,3}(q, 1/2)`; `S_0` and `abs(S_alpha)` at five orders; the residual-cost argmins with the stated seed.
