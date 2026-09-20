---
title: Fractional block count
category: Analyses
summary: B_alpha(C) = sum_i max(0, Delta^alpha c_i), with Delta^alpha the Grunwald-Letnikov fractional difference of the skyline (binomial weights (-1)^k C(alpha,k) run back over every earlier column), equals the area at alpha = 0 and the block count at alpha = 1 exactly, verified on all 5460 castles with w <= 6, h <= 4. In between it is the total positive surprise of each column against a power-law weighted average of its past. B_{1/2} is a dyadic rational that separates all ten (4,2) even castles and 14 of the 15 castles in the cell; at an irrational alpha it separates all 15. The statistic is not monotone in alpha (829 of 5460 castles have an uptick), is bounded above by area but can undershoot the block count, is position-aware (unlike area and blocks), and is blind to a castle's descending tail for alpha near 1 for the same reason the block count is. The mean over a cell is convex decreasing in alpha; the variance has an interior minimum near alpha = 0.75. The fractional sign e^{i pi B_alpha} gives a phase sum P_alpha that runs from the area-parity sum (always +-1) at alpha = 0 to the signed count P at alpha = 1 and exceeds |P| in the interior. The L1 residual sum |Delta^alpha c| is the ARFIMA fractional-differencing cost, and its argmin recovers the integration order of a skyline (0 for i.i.d. columns, 1 for a random walk, 2 for a ramp). Generating functions: the fractional difference is multiplication of the skyline GF by (1 - x)^alpha, so for every nondecreasing skyline B_alpha = [x^w] (1 - x)^{alpha - 1} C(x) exactly and B_alpha is monotone in alpha (791 castles); the box castle has B_alpha = h C(w - alpha, w - 1), which at alpha = 1/2 is h 2w C(2w, w) / 4^w ~ 2h sqrt(w / pi), so sqrt(pi) enters the block count.
tags: [analysis, castle, fractional-calculus, grunwald-letnikov, block-count, area, statistic, memory, power-law, arfima, compression, parity, computation, verification]
sources: [project-euler-502-castle-factoring, project-euler-502-brute-force, project-euler-502-observations]
created: 2026-09-19
updated: 2026-09-19
---

# Fractional block count

The castle's two structural statistics are its **area** `sum c_i` and its **block count**, and the wiki pairs them constantly: the q-thread grades by area ([[castle-by-area](pages/castle-by-area.md)]), the parity clause and the Narayana polynomial grade by blocks ([[castle-sign](pages/castle-sign.md)], [[tower-narayana-polynomial](pages/tower-narayana-polynomial.md)]), and the entropy and compression pages ask how the two trade off ([[castle-entropy](pages/castle-entropy.md)], [[castle-compression](pages/castle-compression.md)]). This page shows that they are the two ends of one statistic. The block count is the positive part of the first difference of the skyline; the area is the positive part of the zeroth difference; fractional calculus supplies every difference in between.

Every number below was computed while writing and re-run for the final tables; the scripts are described in the execution footnote.[^exec]

## Definition

Write the skyline as `c = (c_1, ..., c_w)` with `c_i in {1, ..., h}`, and put a **ground column** `c_0 = 0` to its left, with `c_j = 0` for every `j <= 0` ([[castle-representations](pages/castle-representations.md)]). The **Grunwald-Letnikov difference of order `alpha`** at column `i` is

```
Delta^alpha c_i  =  sum_{k = 0}^{i - 1}  w_k(alpha) c_{i - k},        w_k(alpha) = (-1)^k C(alpha, k),
```

where `C(alpha, k) = alpha (alpha - 1) ... (alpha - k + 1) / k!` is the generalized binomial coefficient.[^1] At `alpha = 1` the weights are `1, -1, 0, 0, ...` and `Delta^1 c_i = c_i - c_{i-1}` is the ordinary column difference; at `alpha = 0` the weights are `1, 0, 0, ...` and `Delta^0 c_i = c_i`. The **fractional block count** is the positive part summed over the castle:

```
B_alpha(C)  =  sum_{i = 1}^{w}  max(0, Delta^alpha c_i).
```

**The two endpoints are exact.** At `alpha = 0`, `B_0 = sum c_i` is the area. At `alpha = 1`, `B_1 = sum max(0, c_i - c_{i-1})` with `c_0 = 0` is the **total ascent** of the skyline, and the total ascent is the block count: each new block is opened by a column rising above its left neighbour, and a column of height `b` after a column of height `a` opens `max(0, b - a)` new blocks.[^2] (The wiki's other formula for the block count, the total descent `sum max(0, c_i - c_{i+1})` with `c_{w+1} = 0`, is the same number read from the other end;[^3] the fractional version is built on the ascent form because the memory runs left to right.) Both identities were checked on every castle with `w <= 6` and `h <= 4`, 5460 castles, with no exceptions.[^exec]

**The weights at `alpha = 1/2`** are dyadic rationals:

```
w_0, w_1, w_2, ...  =  1, -1/2, -1/8, -1/16, -5/128, -7/256, -21/1024, ...
```

so `B_{1/2}` of a width-`w` castle is an integer multiple of `2^{-(2w - 2)}` (checked for `w <= 6`, `h = 3`).[^exec] The half-order block count is exactly representable in fixed-point binary with `2w - 2` fractional bits.

## The memory reading

For `0 < alpha < 1` every weight past the first is **negative**, and they sum to `-1` in the limit:

```
w_k(alpha) = -alpha (1 - alpha)(2 - alpha) ... (k - 1 - alpha) / k!  <  0     (k >= 1),
sum_{k >= 1} |w_k(alpha)| = 1,            |w_k(alpha)| ~ alpha / (Gamma(1 - alpha) k^{1 + alpha}).
```

So the fractional difference is `Delta^alpha c_i = c_i - (weighted average of c_{i-1}, c_{i-2}, ...)` where the weights form a probability distribution with a **power-law tail**, and `B_alpha` is the total amount by which each column exceeds the power-law-weighted memory of everything to its left. That is the nonlocality fractional calculus is known for, in castle form: the ordinary block count asks "is this column higher than the one before?", the fractional block count asks "is this column higher than the long-memory average of all the ones before?". At `alpha = 1/2` the partial sums of `|w_k|` reach `0.727` at `k = 4`, `0.860` at `16`, `0.930` at `64`, and `0.982` at `1024`: the memory is long, and a width-6 castle sees only about three quarters of the total weight.[^exec]

**Small `alpha`.** Since `(-1)^k C(alpha, k) = -alpha / k + O(alpha^2)` for `k >= 1`, the first-order expansion is

```
B_alpha(C)  =  area(C)  -  alpha * sum_{j = 1}^{w} c_j H_{w - j}  +  O(alpha^2),
```

with `H_n = 1 + 1/2 + ... + 1/n` the harmonic numbers (`H_0 = 0`). The slope at `alpha = 0` weights each column by the harmonic number of how many columns lie to its right: a cell of height in column 1 is worth `H_{w-1}` of slope, a cell in the last column nothing. Finite differences confirm the formula to four decimals on `(1, 2, 2, 1)` (slope `-6.8333`), `(3, 1, 2, 3, 1)` (`-14.0833`), and `(1, 1, 1, 4)` (`-4.3333`).[^exec] This is the first sign that `B_alpha` knows *where* a castle's mass sits, which neither endpoint does.

## Worked example: the ten `(4, 2)` castles

The even-block castles of width 4 and height 2 are the `F(4, 2) = 10` of the Project Euler statement ([[castle-counting-function](pages/castle-counting-function.md)]). Their half-order residual vectors and fractional block counts:[^exec]

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

All ten have the same block count and only four distinct areas; **`B_{1/2}` takes ten distinct values.** Reading down the table, the statistic orders the castles by how late and how briefly the second row appears: `(2, 1, 1, 1)`, whose upper block is at the far left where the memory is empty, scores lowest, and `(1, 1, 1, 2)` scores higher than `(1, 1, 2, 1)` with the same area because its raised column comes after a longer run of low history. Across the whole `(4, 2)` cell of 15 castles, `B_{1/2}` takes 14 distinct values (one dyadic coincidence) and `B_alpha` at `alpha = sqrt(2) - 1` takes all 15.[^exec]

## Distinguishing power and its limits

The same count across larger cells (`B_irr` is `B_alpha` at `alpha = sqrt(2) - 1`):[^exec]

| cell `(w, h)` | castles | even | distinct area | distinct blocks | distinct `(area, blocks)` | distinct `B_{1/2}` | distinct `B_irr` |
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

The pair `(area, blocks)` separates a few percent of a cell; a single fractional order separates most of it. The collisions come in two kinds.

**Dyadic coincidences at `alpha = 1/2`.** Because `B_{1/2}` lives on the lattice `2^{-(2w-2)} Z`, distinct castles land on the same value often; at an irrational `alpha` almost all of these separate (`(8, 2)`: 14 collisions at `1/2`, 2 at `sqrt(2) - 1`).

**Tail blindness for `alpha` near 1.** The collisions that survive at irrational `alpha` are structural. In `(5, 4)` there are 126 pairs of castles with `B_alpha` identical for every `alpha` in `[0.5, 1)`, and 555 such pairs in `(6, 4)`. Every one inspected has the same form: the two castles share a prefix through their last column with a positive residual and differ only in the descending tail after it, for example `(1, 1, 1, 4, 1)` and `(1, 1, 1, 4, 2)`, or `(1, 1, 4, 1, 1)` and `(1, 1, 4, 2, 1)`.[^exec] The mechanism is inherited from the endpoint: the block count is the total *ascent*, so it never sees how a castle comes down, and `B_alpha` for `alpha` close to 1 keeps that blindness wherever the trailing residuals stay negative. The blindness lifts as `alpha` falls toward 0, where the area sees every cell (`B_{0.1}` differs by exactly `1.000` on the first pair above). No pair of distinct castles was found with `B_alpha` equal on all of `(0, 1)`: 49 orders tested, in `(6, 3)`, `(7, 3)`, and `(5, 4)`, zero pairs.[^exec]

**Position awareness.** Area and block count are both unchanged by reversing the skyline. `B_alpha` is not: in `(5, 3)` the castles with `B_{1/2}(c) = B_{1/2}(reverse c)` are exactly the 19 palindromes; in `(6, 3)` 25 castles pass against 19 palindromes; in `(5, 4)` 41 against 37.[^exec] This is a consequence of the left-to-right memory and is the first single-number castle statistic on the wiki that knows which end of the castle is which.

## The shape of `B_alpha` as a function of `alpha`

`B_alpha(C)` is continuous and piecewise polynomial in `alpha` (each residual is a polynomial in `alpha`, and the positive part clips). Three facts about its shape, all from the `w <= 6`, `h <= 4` census on a grid of 201 orders:[^exec]

- **It is not monotone.** 829 of the 5460 castles have at least one uptick on `[0, 1]`. The upticks are small: the largest single step is `0.014` per `0.005` of `alpha`, and the largest total rise over `[0, 1]` is `0.47`, on `(4, 3, 1, 4, 1, 4)` (area 17, blocks 10). The IDEAS conjecture that `B_alpha` decreases in `alpha` for every castle is false in general; it is true for every nondecreasing castle, by the generating-function argument below, so the upticks all come from castles with descents.
- **It is bounded above by the area** for every castle and every `alpha` in `[0, 1]`.
- **It is not bounded below by the block count.** `(4, 3, 1, 4, 1, 2)` has 8 blocks and `B_{0.8} = 7.58`; its residuals at `alpha = 0.8` are `4.0, -0.2, -1.72, 2.83, -2.45, 0.75`, and the two positive ones at columns 4 and 6 fall short of the ascents `3` and `1` they correspond to, because the long memory of the `4` in column 1 is still being subtracted.

Over a whole cell the statistic is well behaved. The mean is convex and decreasing; the variance has an interior minimum:[^exec]

| cell | `alpha` | 0 | 0.25 | 0.5 | 0.75 | 1 |
|---|---|---|---|---|---|---|
| `(6, 3)` | mean | 12.289 | 8.461 | 6.229 | 5.047 | 4.364 |
| | variance | 3.291 | 1.671 | 0.773 | 0.593 | 0.893 |
| `(8, 2)` | mean | 12.016 | 7.684 | 5.234 | 4.007 | 3.259 |
| | variance | 1.945 | 0.845 | 0.443 | 0.344 | 0.545 |
| `(5, 4)` | mean | 13.278 | 9.601 | 7.348 | 6.070 | 5.380 |
| | variance | 4.608 | 2.440 | 1.133 | 0.864 | 1.278 |

The mean at `alpha = 1/2` is well below the average of the endpoints (`6.23` against `8.33` for `(6, 3)`): most of the drop from area to block count happens at small `alpha`, where the harmonic-number slope is steepest. The variance minimum near `alpha = 0.75` says the uniform castle is most predictable in its three-quarter-order block count, less so in either its area or its integer block count.

## Generating functions: the box, the ramp, and the nondecreasing theorem

Write the skyline as a polynomial `C(x) = sum_{i=1}^{w} c_i x^i`. The Grunwald-Letnikov weights are the coefficients of `(1 - x)^alpha`, so the residual sequence is a product of generating functions:

```
sum_i (Delta^alpha c_i) x^i  =  (1 - x)^alpha C(x)          (mod x^{w+1}).
```

At `alpha = 1/2` the coefficients of `(1 - x)^{1/2}` are `1, -1/2, -1/8, -1/16, -5/128, -7/256, -21/1024, ...`; their numerators are A002596 and their denominators A046161, the same denominators as `C(2k, k) / 4^k`. Two consequences fall out of the product form.[^exec]

**The fractional difference is lossless.** `(1 - x)^{-alpha}` inverts it: the map from skyline to residual sequence is a triangular Toeplitz matrix with ones on the diagonal, and the roundtrip through `alpha = 0.37` and back returns the skyline to `10^{-15}`. All the information loss in `B_alpha` is in the positive part; the residual sequence itself is an exact re-encoding of the castle.

**Nondecreasing castles.** If `c_1 <= c_2 <= ... <= c_w`, then `Delta^alpha = Delta^{-(1 - alpha)} Delta^1` applies the ordinary difference first, giving the nonnegative ascents `d_j = c_j - c_{j-1}`, and then the fractional sum `(1 - x)^{-(1 - alpha)}`, all of whose coefficients are positive for `0 <= alpha <= 1`. So every residual is nonnegative, the positive part does nothing, and

```
B_alpha(C)  =  [x^w] (1 - x)^{alpha - 1} C(x)  =  sum_{j=1}^{w} d_j [x^{w-j}] (1 - x)^{alpha - 2}.
```

The coefficients of `(1 - x)^{alpha - 2}` decrease in `alpha`, so **`B_alpha` is monotone decreasing in `alpha` for every nondecreasing castle**. Checked on all 791 nondecreasing castles with `w <= 7`, `h <= 5` at 41 orders: residuals nonnegative, the formula exact to `10^{-7}`, monotone.[^exec] The monotonicity failures of the previous section are therefore all castles with a descent somewhere, where a clipped negative residual can release its memory later.

**The box.** For the box castle `c_i = h` the ascent sequence is `d = (h, 0, ..., 0)` and the formula collapses to one coefficient:

```
B_alpha(box_{w,h})  =  h [x^{w-1}] (1 - x)^{alpha - 2}  =  h C(w - alpha, w - 1)  =  h Gamma(w + 1 - alpha) / (Gamma(w) Gamma(2 - alpha))  ~  h w^{1 - alpha} / Gamma(2 - alpha).
```

At `alpha = 0` this is `hw`, the area; at `alpha = 1` it is `h`, the block count (a box has `h` blocks, one per row); at `alpha = 1/2`,

```
B_{1/2}(box_{w,h})  =  h sum_{i=0}^{w-1} C(2i, i) / 4^i  =  h 2w C(2w, w) / 4^w  ~  2h sqrt(w / pi),
```

whose numerators `1, 3, 15, 35, 315, 693, 3003, ...` are A001803, the numerators of `(1 - x)^{-3/2}`.[^exec] The half-order block count of a box is `(2 / sqrt(pi)) sqrt(area * blocks)` in the limit: the geometric mean of the two integer statistics, scaled by `2 / sqrt(pi) = 1.128`. This is the [[algebraic-transcendental-wall](pages/algebraic-transcendental-wall.md)] crossed from the block-count side, through `Gamma(1/2) = sqrt(pi)`, and it is the same mechanism fractional partial sums of counts obey (Gamma at half-integer orders). Values at `h = 3`:

| `w` | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|---|---|
| `B_{1/2}(box_{w,3})` | 3 | 4.5 | 5.625 | 6.5625 | 7.3828 | 8.1211 | 8.7979 | 9.4263 |
| ratio to `2h sqrt(w/pi)` | 0.886 | 0.940 | 0.959 | 0.969 | 0.975 | 0.979 | 0.982 | 0.985 |

At `w = 200` the ratio to `h w^{1-alpha} / Gamma(2 - alpha)` is `0.9994` for `alpha = 1/4, 1/2, 3/4`.[^exec]

**The ramp.** For `c_i = i` the ascents are all `1`, `C(x) = x / (1 - x)^2`, and `B_alpha = [x^{w-1}] (1 - x)^{alpha - 3} = C(w + 1 - alpha, w - 1)`; at `alpha = 1/2` and `w = 6` this is `11.7305`, matching the direct computation, and it grows like `w^{3/2}`. Between the box (`w^{1/2}` at half order) and the ramp (`w^{3/2}`) the exponent is set by the growth of the skyline, `w^{1 - alpha} * (degree of C)`.

## The partition function `Z(q, alpha)`

Grade a cell by `B_alpha`:

```
Z_{w,h}(q, alpha)  =  sum_{castles C of the (w, h) cell}  q^{B_alpha(C)}.
```

At `alpha = 0` this is the area generating polynomial of the cell, the `(w, h)`-cell slice of the area grading on [[castle-by-area](pages/castle-by-area.md)] (which grades by area across all cells at once). At `alpha = 1` it is the block-count generating polynomial, whose tower version is the Narayana numerator on [[tower-narayana-polynomial](pages/tower-narayana-polynomial.md)] and whose residue classes are the character sums of [[block-count-constraints](pages/block-count-constraints.md)]; the PE 502 count is `Z(-1, 1)` folded with the total, `F = (A + Z(-1, 1)) / 2` up to the bottom-block shift. So the area-grading `q` and the parity clause's `(-1)^{blocks}` are the same variable at two orders.

For non-integer `alpha` the exponents are no longer integers and `Z` is a finite **Dirichlet polynomial** `sum_C q^{b_C}` with real `b_C`, not a power series. At `alpha = 1/2` in `(6, 3)` there are 433 distinct exponents among 665 castles, all dyadic, running from `3.6992` to `8.4336`, with the largest multiplicity 5.[^exec] Where the integer-order polynomials have a few dozen coefficients carrying all the multiplicity, the half-order object is nearly a bare list of the castles. Whether `Z(q, alpha)` has any product or recursive structure at non-integer `alpha` is open; the tower-independence that makes the `alpha = 1` polynomial factor does not obviously survive a memory that reaches across gaps.

## The fractional sign

The castle sign is `(-1)^{blocks} = e^{i pi B_1}` ([[castle-sign](pages/castle-sign.md)]), and the even-block count is enforced by `(A + P) / 2` with `P` the signed sum.[^4] The natural deformation is the **fractional sign** `e^{i pi B_alpha(C)}`, a point on the unit circle rather than `+-1`, and its sum over a cell

```
P_alpha(w, h)  =  sum_C  e^{i pi B_alpha(C)}.
```

At `alpha = 1`, `P_1 = sum (-1)^{blocks}` is the signed count that drives the PE 502 formula. At `alpha = 0`, `P_0 = sum (-1)^{area}` is the *area*-parity signed count, and it is always `+-1`: summing `(-1)^{c}` over `c in {1, ..., h}` gives `-1` for odd `h` and `0` for even `h`, so `P_0(w, h) = (-1)^{w + h + 1}` for every cell. Area parity is balanced to within one castle in every cell, and a hypothetical "even-area" version of PE 502 would have the trivial answer `(A +- 1) / 2`. The block-parity clause is hard precisely because it sits at the other end of the interpolation. In between:[^exec]

| cell | `A` | `P_0` | `|P_alpha|` at `alpha = 0.1, 0.25, 0.5, 0.75, 0.9` | `P_1` |
|---|---|---|---|---|
| `(8, 2)` | 255 | -1 | `1.00, 1.01, 35.5, 49.2, 24.4` | -15 |
| `(6, 3)` | 665 | +1 | `0.19, 0.31, 8.57, 29.8, 41.0` | -51 |
| `(5, 4)` | 781 | +1 | `0.33, 1.11, 6.35, 47.1, 98.0` | +97 |
| `(6, 4)` | 3367 | -1 | `0.19, 0.99, 10.5, 104.2, 157.0` | +91 |

The phase sum is **not** a monotone dephasing between the two integer ends. It stays near zero out to `alpha = 0.25`, then grows, and in every cell it **exceeds** `|P_1|` somewhere in `(0.5, 1)`: `49` against `15` in `(8, 2)`, `157` against `91` in `(6, 4)`. The fractional phases partially align at three-quarter order in a way the integer signs do not. There is no `alpha`-deformation of the projector `(A +- P) / 2` here yet, because `e^{i pi B_alpha}` is not `+-1` and does not split the cell into two classes; the candidate is to read `P_alpha` as a characteristic function and ask what distribution on the circle it is the transform of.

## The compression reading

Drop the positive part and take the full residual cost `sum_i |Delta^alpha c_i|`. For `0 < alpha < 1` this is the L1 size of the skyline after **fractional differencing** by `(1 - B)^alpha`, `B` the backshift, which is the operation that defines the ARFIMA family of long-memory time series: a process is fractionally integrated of order `d` when `(1 - B)^d` turns it into white noise.[^5] The order `alpha` that minimizes the residual cost is therefore an estimate of the skyline's integration order, and on synthetic width-64 skylines (heights centred before differencing) it lands where it should:[^exec]

| skyline | argmin of `sum |Delta^alpha c|` |
|---|---|
| i.i.d. uniform heights in `{1, ..., 8}` | `0.00` |
| 1-smooth random walk (steps `-1, 0, +1`) | `1.00` |
| ramp `1, 2, ..., 64` | `2.00` |
| fractionally integrated Gaussian noise, `d = 0.3` | `0.48` |

The three integer cases are exact; the fractional case is recovered as "between 0 and 1" with the upward bias one expects from an L1 argmin on 64 samples. In the language of [[castle-compression](pages/castle-compression.md)], the skyline tier codes the heights (`alpha = 0`) and the run-length tier codes the first difference (`alpha = 1`); the fractional order is the continuous knob between them, and the best `alpha` for a skyline is a one-number description of how much memory it has. This is where a Hurst-exponent reading picks up, on the real skylines of [[image-as-castle](pages/image-as-castle.md)] and [[song-as-castle](pages/song-as-castle.md)].

## What this page settles and what it opens

Settled:

- `B_alpha` with the positive-part definition and a left ground column has `B_0 = area` and `B_1 = blocks` exactly (5460 castles).
- `B_{1/2}` is dyadic with `2w - 2` fractional bits; it separates the ten `(4, 2)` even castles and 14 of the 15 castles in the cell; an irrational order separates all 15 and most of every cell tested.
- `B_alpha` is not monotone in `alpha` (829 of 5460 castles), is bounded above by area, and can undershoot the block count.
- The structural collisions are tail-blind pairs, inherited from the block count being the total ascent; no pair coincides on all of `(0, 1)`.
- `B_alpha` is position-aware; only palindromes (essentially) match their reversal.
- `P_0 = (-1)^{w+h+1}` in every cell; `|P_alpha|` exceeds `|P_1|` in the interior.
- The L1 residual argmin recovers the integration order of synthetic skylines.
- The fractional difference is multiplication of the skyline GF by `(1 - x)^alpha`, invertible by `(1 - x)^{-alpha}`; for nondecreasing castles `B_alpha = [x^w] (1 - x)^{alpha-1} C(x)` and `B_alpha` is monotone (791 castles).
- `B_alpha(box_{w,h}) = h C(w - alpha, w - 1)`; at `alpha = 1/2` it is `h 2w C(2w,w) / 4^w ~ 2h sqrt(w/pi)`, so `sqrt(pi)` enters the block count.

Open:

- **A uniform formula for the cell mean `E[B_alpha]`**, at least for `h = 2` where the castles are binary strings and the residuals are explicit.
- **The exact collision law.** Is every pair with `B_alpha` equal on an interval a tail-blind pair, and for which `alpha` does a given pair separate?
- **The best order.** Which `alpha` maximizes the number of distinct values in a cell, and does it converge as the cell grows?
- **Structure of `Z(q, alpha)`.** A recursion, a product form, or a proof that neither exists off the integers.
- **A fractional projector.** What `P_alpha` is the characteristic function of, and whether any `alpha` in `(0, 1)` gives a two-class split of a cell that is not the block parity.
- **Two-sided memory.** The left-to-right convention is a choice; the symmetric statistic `(B_alpha(c) + B_alpha(reverse c)) / 2` restores reversal invariance at the cost of the position information, and the Riesz-type two-sided fractional difference is the third option.

## Appearances in Sources

- [[project-euler-502-castle-factoring](pages/project-euler-502-castle-factoring.md)] - the block count as the total descent of the column-height sequence, and the castle sign `(-1)^{blocks}`.
- [[project-euler-502-brute-force](pages/project-euler-502-brute-force.md)] - the block count as maximal horizontal runs and as the total ascent `max(0, b - a)` per column step.
- [[project-euler-502-observations](pages/project-euler-502-observations.md)] - `(A + P) / 2` with `P` the `(-1)^{blocks}`-signed count.

## Related Concepts

- [[castle-sign](pages/castle-sign.md)] - `s(C) = (-1)^{blocks} = e^{i pi B_1}`; the fractional sign deforms it.
- [[castle-by-area](pages/castle-by-area.md)] - the area grading, `Z(q, 0)` summed over cells.
- [[tower-narayana-polynomial](pages/tower-narayana-polynomial.md)] and [[block-count-constraints](pages/block-count-constraints.md)] - the block-count grading, `Z(q, 1)`.
- [[castle-representations](pages/castle-representations.md)] - the skyline tuple the difference operator acts on.
- [[monotone-streak-factorization](pages/monotone-streak-factorization.md)] - the first-difference sequence whose positive part is the integer block count.
- [[castle-compression](pages/castle-compression.md)] and [[castle-entropy](pages/castle-entropy.md)] - the tier ladder the fractional order interpolates, and the one-bit parity cost.
- [[castle-counting-function](pages/castle-counting-function.md)] - `F(4, 2) = 10`, the worked cell.
- [[castle-snippets](pages/castle-snippets.md)] - `all_castles`, `blocks`.
- [[image-as-castle](pages/image-as-castle.md)] and [[song-as-castle](pages/song-as-castle.md)] - the real skylines the compression reading is aimed at.
- [[algebraic-transcendental-wall](pages/algebraic-transcendental-wall.md)] - `sqrt(pi)` in the half-order block count of a box is a crossing of the wall via `Gamma(1/2)`.

## Footnotes

[^1]: https://en.wikipedia.org/wiki/Gr%C3%BCnwald%E2%80%93Letnikov_derivative (2026-09-19) [synthesis] - the Grunwald-Letnikov derivative of order `alpha` is the limit of the finite difference `h^{-alpha} sum_k (-1)^k C(alpha, k) f(x - k h)` with generalized binomial coefficients, reducing to the ordinary `n`-th difference when `alpha = n` is an integer; the discrete operator on this page is that difference with `h = 1` on the integer grid of columns.
[^2]: [[project-euler-502-brute-force](pages/project-euler-502-brute-force.md)] §"Column-height encoding" L20-23 - "A block is a maximal horizontal run of columns at a given level, so #blocks = sum_{r=1}^{h} #{runs of columns with c_i >= r}"; §"Signed sum" L31 - "A new column of height b after a column of height a starts max(0, b - a) new runs, each contributing a factor of -1."
[^3]: [[project-euler-502-castle-factoring](pages/project-euler-502-castle-factoring.md)] §"Sign" L104-107 - "In the column-height form, the block count is the total descent: blocks = sum_{i=0}^{L} max(0, c_i - c_{i+1}), c_0 = c_{L+1} = 0"; L98-101 - "Weight each block by -1 and define s(C) = (-1)^{blocks(C)}".
[^4]: [[project-euler-502-observations](pages/project-euler-502-observations.md)] L13 - "Even-block-count is enforced by (A + P)/2, where A is the unsigned total and P is the signed count with (-1)^{blocks}. A symmetry trick that recurs in many combinatorial-enumeration problems."
[^5]: https://en.wikipedia.org/wiki/Autoregressive_fractionally_integrated_moving_average (2026-09-19) [synthesis] - ARFIMA generalizes ARIMA by allowing the differencing order `d` to be a non-integer; the fractional differencing operator `(1 - B)^d` is defined by the binomial series `sum_k C(d, k) (-B)^k`, and processes with `0 < d < 1/2` exhibit long memory with power-law autocorrelation decay (Granger and Joyeux 1980, Hosking 1981).
[^exec]: Verified by execution (2026-09-19): two Python 3 scripts, standard library only. Script 1: `gl_weights`, `frac_diff` (left ground column, `c_j = 0` for `j <= 0`), `B` (positive part), `Babs` (full L1), `blocks` (total ascent), `castles(w, h)`; endpoint identities `B_0 = area`, `B_1 = blocks` asserted on all 5460 castles with `w <= 6`, `h <= 4`; partial sums of `|w_k(1/2)|` to `n = 4, 16, 64, 1024`; the `(4, 2)` table; the harmonic-slope check by finite difference at `alpha = 10^{-4}`; the distinct-value census with collisions at `alpha = 1/2` re-tested at `sqrt(2) - 1`, `0.3141592`, `0.7071`; means and variances on `alpha in {0, 0.25, 0.5, 0.75, 1}`; the `Z(q, 1/2)` exponent spectrum of `(6, 3)`; `P_alpha` on a seven-point grid; the raw L1 argmin on four width-64 skylines. Script 2: monotonicity on a 201-point grid (violators, largest single step, largest total rise, `B_alpha <= area` and `B_alpha >= blocks` tests); dyadic check `B_{1/2} * 2^{2w-2} in Z` for `w <= 6, h = 3` and the exact weights via `fractions.Fraction`; pairs equal on all 49 orders `k/50` in `(0, 1)` (zero found) and pairs equal on the 50 orders `0.5 + k/100` in `[0.5, 1)` with their last positive-residual column and common prefix; reversal test; centred L1 argmin on a grid to `alpha = 2.5`, including an ARFIMA `d = 0.3` skyline generated by `(1 - B)^{-0.3}` on Gaussian noise. Script 3 (SymPy 1.14, NumPy 1.26): series of `(1 - x)^{1/2}` against the GL weights with `fractions`; the box identity `h sum_{i<w} C(2i,i)/4^i = h 2w C(2w,w)/4^w` for `w <= 8` and the general `h C(w - alpha, w - 1)` at `alpha = 1/4, 1/2, 3/4`; the nondecreasing theorem on all 791 nondecreasing castles with `w <= 7`, `h <= 5` (`itertools.combinations_with_replacement`) at 41 orders, checking residual nonnegativity, the coefficient formula via `(1 - x)^{alpha - 1}` and the ascent form via `(1 - x)^{alpha - 2}`, and monotonicity; the ramp value at `w = 6`; the roundtrip `(1 - x)^{-alpha} (1 - x)^{alpha}`; the box asymptotic ratio at `w = 200` by `math.lgamma`; OEIS lookups of the numerator and denominator sequences by the search API. All quoted numbers are the scripts' printed output.
