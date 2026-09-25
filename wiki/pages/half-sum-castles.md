---
title: Half-sum castles
category: Analyses
summary: The order-1/2 fractional partial sum of the castle count, H_h(w) = sum_k C(2k,k)/4^k F(w-k,h), has generating function G_h(x)/sqrt(1-x), algebraic of degree 2 and never rational, so no finite strip rule counts it. Because F grows like h^w/2, the pole at 1/h dominates the branch point at 1, and H_h(w)/F(w,h) -> sqrt(h/(h-1)), an algebraic constant. sqrt(pi) enters only in the branch remainder, which is G_h(1)/sqrt(pi w) with G_h(1) = 0, 1/2, 1/30, 1/20 for h = 2..5; G_h(1) is minus the sum of the castle count continued to negative widths, and at h = 2 it vanishes because the numerator carries a factor (1-x), leaving 1/(2 sqrt(pi) w^{3/2}). Shifting the half-sum onto the dominant pole, weights C(2k,k)(h/4)^k, gives h^w sqrt(w/pi) exactly in the leading term; at h = 4 the weights are the integers C(2k,k), and pi = lim w 16^w / K(w)^2 with K(w) = sum_k C(2k,k) F(w-k,4) = 1, 9, 51, 241, 1069, ... The integer half-sums count castles followed by a balanced tail (at h = 4, a height-4 skyline with as many 1s as 4s), a product and not a castle-intrinsic object; the one family where the half-sum is intrinsic is the nondecreasing castles, where half a sum in the width is half a row in the height, C(w+h-2, w-1) -> C(w+h-3/2, w-1). No half-sum row has an OEIS match.
tags: [analysis, castle, fractional-calculus, half-sum, cesaro, riemann-liouville, generating-function, algebraic, singularity-analysis, pi, wallis, central-binomial, context-free, nondecreasing, computation, oeis, novel-candidate]
sources: [project-euler-502-brute-force, algebraic-languages-and-polyominoes-enumeration]
created: 2026-09-23
updated: 2026-09-23
---

# Half-sum castles

The partial sum of a count sequence is multiplication of its generating function by `(1 - x)^{-1}`; the Riemann-Liouville fractional sum of order `alpha` is multiplication by `(1 - x)^{-alpha}`, the Cesaro mean of order `alpha`. This page applies the order-`1/2` sum to the castle count `F(w, h)` in the width. Its companion [[fractional-block-count](pages/fractional-block-count.md)] runs the same operator with the opposite sign on a single skyline, and [[fractional-width-and-height](pages/fractional-width-and-height.md)] runs it in the height direction as the half-column of the nondecreasing rule.

Every number below was computed while writing; the method is in the execution footnote.[^exec]

## Definition and the tables

The coefficients of `(1 - x)^{-1/2}` are `C(2k, k) / 4^k = 1, 1/2, 3/8, 5/16, 35/128, ...`, so the **half-sum** of the height-`h` row is

```
H_h(w)  =  sum_{k = 0}^{w}  C(2k, k) / 4^k  *  F(w - k, h),        sum_w H_h(w) x^w  =  G_h(x) / sqrt(1 - x),
```

with `G_h(x) = sum_w F(w, h) x^w` the rational generating function of the row ([[generating-function-gallery](pages/generating-function-gallery.md)]) and `F(0, h) = 0`. Applying the half-sum twice gives the ordinary cumulative count. The rows, recomputed by the last-column transfer matrix and fitted by [[berlekamp-massey](pages/berlekamp-massey.md)]:[^exec]

| `h` | `G_h(x)` |
|---|---|
| 2 | `x (1 - x) / ((1 - 2x)(1 - 2x + 2x^2))` |
| 3 | `x^3 (3 - 3x + 2x^2) / ((1 - 2x)(1 - 3x)(1 - 2x + 2x^2)(1 - x + 2x^2))` |
| 4 | `x (1 - 7x + 18x^2 - 26x^3 + 40x^4 - 44x^5 + 32x^6 - 16x^7) / ((1 - 2x)(1 - 3x)(1 - 4x)(1 - x + 2x^2)(1 - 4x + 8x^2 - 8x^3 + 8x^4))` |
| 5 | `2x^3 (5 - 29x + 60x^2 - 94x^3 + 112x^4 - 104x^5 + 64x^6 - 32x^7) / ((1 - 4x)(1 - 5x)(1 - 2x + 4x^2)(1 - 3x + 2x^2 - 4x^3)(1 - 4x + 8x^2 - 8x^3 + 8x^4))` |

The series reproduce `F(4, 2) = 10`, `F(5, 5) = 906`, and `F(6, 4) = 1729`, and the `h = 2` row is A038505 shifted by one. The half-sums are dyadic rationals:

| `w` | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|---|---|
| `H_2(w)` | 1 | 7/2 | 63/8 | 231/16 | 3131/128 | 10929/256 | 83691/1024 | 345287/2048 |
| `H_3(w)` | 0 | 0 | 3 | 45/2 | 805/8 | 5765/16 | 149921/128 | 939243/256 |
| `H_4(w)` | 1 | 15/2 | 279/8 | 2167/16 | 65483/128 | 513081/256 | 8334451/1024 | 68729799/2048 |
| `H_5(w)` | 0 | 0 | 10 | 127 | 3883/4 | 47839/8 | 2137191/64 | 22845977/128 |

Two integer versions clear the denominators. `4^w H_h(w)` has generating function `G_h(4x) / sqrt(1 - 4x)`. The **binomial half-sum** `K_h(w) = sum_k C(2k, k) F(w - k, h)` has `G_h(x) / sqrt(1 - 4x)`:

| `h` | `K_h(w)` from the first nonzero term |
|---|---|
| 2 | 1, 5, 18, 60, 202, 702, 2508, 9136, 33742, 125934 |
| 3 | 3, 27, 149, 671, 2755, 10833, 41679, 158465, 598681 |
| 4 | 1, 9, 51, 241, 1069, 4671, 20353, 88383, 381583, 1635893 |
| 5 | 10, 142, 1210, 8222, 49806, 283570, 1557158, 8354490 |

None of the four `K_h` rows, the `4^w H_h` rows, or the dyadic numerators of `H_2` has an OEIS match (search API, 2026-09-23).[^exec] They go on [[castle-sequence-catalogue](pages/castle-sequence-catalogue.md)] as novel-candidates, with the caveat that convolutions of a known sequence with the central binomials rarely get their own entry.

## Where the `sqrt(pi)` goes

The weight `C(2k, k) / 4^k` is `~ 1 / sqrt(pi k)`, and the half-sum of the constant sequence `1` is `(2w + 1) C(2w, w) / 4^w ~ 2 sqrt(w / pi)` (numerators A001803), the Wallis case. The half-sum of a sequence of radius 1 therefore carries `sqrt(pi)` in its leading constant. Castle rows grow exponentially, and that changes the order of the terms.

**The pole wins.** `G_h` has a simple pole at `x = 1/h` with `F(w, h) ~ h^w / 2` (the residue constant is `1/2` at every `h = 2..5`), and every other pole also lies inside the unit disk. Multiplying a simple pole at `r` by `(1 - x)^{-1/2}` scales it by `(1 - r)^{-1/2}`, so

```
H_h(w)  =  sum_i  c_i lambda_i^w (1 - 1/lambda_i)^{-1/2}  +  R_h(w),          H_h(w) / F(w, h)  ->  sqrt(h / (h - 1)),
```

where `F(w, h) = sum_i c_i lambda_i^w` is the exponential-polynomial form of the row. The leading ratio is `sqrt 2, sqrt(3/2), sqrt(4/3), sqrt(5/4)` for `h = 2..5`, which matches to 12 digits at `w = 100`.[^exec] Half-summing an exponentially growing castle row only scales it by an algebraic constant.

**`sqrt(pi)` is in the remainder.** The branch point at `x = 1` contributes `G_h(x) (1 - x)^{-1/2} = G_h(1) (1 - x)^{-1/2} - G_h'(1) (1 - x)^{1/2} + ...`, so

```
R_h(w)  =  G_h(1) / sqrt(pi w)  +  O(w^{-3/2}).
```

| `h` | `G_h(1)` | `R_h(w) sqrt(pi w)` at `w = 50` | at `w = 100` |
|---|---|---|---|
| 2 | 0 | 0.00923 | 0.00480 |
| 3 | 1/2 | 0.48235 | 0.49091 |
| 4 | 1/30 | 0.03473 | 0.03409 |
| 5 | 1/20 | 0.04866 | 0.04931 |

At `h = 2` the numerator of `G_2` is divisible by `1 - x`, so the `w^{-1/2}` term vanishes. The next term is `G_2'(1) / (2 sqrt(pi) w^{3/2})` with `G_2'(1) = 1`, and `2 sqrt(pi) w^{3/2} R_2(w)` reads `0.923, 0.960, 0.980` at `w = 50, 100, 200`.[^exec] `R_h(w)` is the difference between a rational number and an algebraic one, so it gives `pi` only in the limit, and only after the algebraic exponential part has been subtracted. The half-sum leaves [[algebraic-transcendental-wall](pages/algebraic-transcendental-wall.md)] intact: it is another limit route.

## The coefficient of `sqrt(pi)` is the negative-width count

The recurrence of each row runs backwards, which defines `F(w, h)` at negative integer widths. That is the same continuation [[fractional-width-and-height](pages/fractional-width-and-height.md)] uses at real `w`. For `h = 2..5` the two-sided sequence agrees with `F` at every `w >= 0` (no exceptional initial terms), and `F(-1, h) = -1 / (2h(h - 1))`:

| `h` | `F(-1, h)`, `F(-2, h)`, `F(-3, h)`, `F(-4, h)` |
|---|---|
| 2 | -1/4, -1/8, 1/16, 5/32 |
| 3 | -1/12, -5/72, -19/432, -227/2592 |
| 4 | -1/24, -7/288, -37/3456, -175/41472 |
| 5 | -1/40, -9/800, -61/16000, -369/320000 |

For a single exponential, `sum_{w >= 0} lambda^w x^w + sum_{w < 0} lambda^w x^w = 1/(1 - lambda x) + 1/(lambda x - 1) = 0` as rational functions. So `G_h(x) = -sum_{w <= -1} F(w, h) x^w`, and at `x = 1` the right side converges because every `|lambda_i| > 1` (the smallest is `1.196` at `h = 5`). Therefore

```
G_h(1)  =  - sum_{w <= -1} F(w, h),
```

which the truncated sums confirm: `0`, `-0.5`, `-0.03333`, `-0.04999` against `G_h(1) = 0, 1/2, 1/30, 1/20`.[^exec] The coefficient of `1/sqrt(pi w)` in the half-sum is minus the total count of castles of negative width.

## The matched half-sum: `pi` in the leading term

Moving the fractional singularity onto the dominant pole, with weights `C(2k, k) (h/4)^k` and generating function `G_h(x) / sqrt(1 - hx)`, turns the simple pole into `(1 - hx)^{-3/2}`:

```
M_h(w)  =  sum_{k} C(2k, k) (h/4)^k F(w - k, h)  ~  (1/2) h^w * 2 sqrt(w / pi)  =  h^w sqrt(w / pi).
```

At `h = 4` the weights are integers and `M_4 = K_4`, the binomial half-sum `1, 9, 51, 241, 1069, 4671, 20353, ...` of the table above. So `pi` is a limit of exact castle integers:

```
pi  =  lim_{w -> infinity}  w 16^w / K_4(w)^2,        K_4(w) = sum_k C(2k, k) F(w - k, 4).
```

| `w` | 50 | 100 | 200 | 400 | 800 | 1600 |
|---|---|---|---|---|---|---|
| `w 16^w / K_4(w)^2` | 3.26682 | 3.20168 | 3.17108 | 3.15620 | 3.14886 | 3.14522 |
| Richardson `2 p(w) - p(w/2)` | 3.11399 | 3.13655 | 3.14047 | 3.14133 | 3.14153 | 3.14158 |

The error is `O(1/w)` (about `1.85 pi / w`), from the next terms of the expansion at the pole, and one Richardson step makes it `O(1/w^2)`. The rational-weight version at `h = 2, 3, 5` converges the same way: `3.1298`, `3.2103`, `3.2308` at `w = 200`.[^exec] A pole and a square-root branch at the same point is also the shape of Delest and Viennot's perimeter count of convex polyominoes, whose `4^n` term carries a subdominant `C(2n, n)`.[^1]

## What the half-sum counts

`G_h(x) / sqrt(1 - x)` is algebraic of degree 2 over `Q(x)` and not rational. So no finite-state strip rule, and no regular language of castle words, has the half-sum as its count. The dyadic `H_h` is not a count at all. The integer versions are N-algebraic: `1 / sqrt(1 - 4x) = 1 / (1 - 2x C(x))` with `C` the Catalan series, so `G_h(x) / sqrt(1 - 4x)` counts a regular castle word followed by a word of an unambiguous context-free language. The algebraicity sits entirely in the tail, as in Delest and Viennot's convex polyominoes.[^2]

At `h = 4` the tail has a castle reading. `C(2k, k) = [y^0] (y + 2 + 1/y)^k` is the number of width-`k` skylines over heights `{1, 2, 3, 4}` with as many columns of height 4 as of height 1. So `K_4(w)` counts width-`w` height-4 skylines cut at a marked column into an even-block castle prefix that reaches height 4 and a balanced suffix. This is a product: nothing inside the castle has changed. No castle-intrinsic object with count `K_h` was found.

**The nondecreasing castles are the exception.** A nondecreasing castle of width `w` and height `h` has `c_w = h`, so its block count is `h`, and there are `C(w + h - 2, w - 1)` of them, generating function `x / (1 - x)^h`. The half-sum raises the exponent by `1/2`:

```
sum_k C(2k, k)/4^k  C(w - k + h - 2, w - k - 1)  =  C(w + h - 3/2, w - 1),
```

verified exactly for `h <= 6`, `w <= 19`.[^exec] The right side is the same binomial at height `h + 1/2`: for the nondecreasing family, half a sum in the width is half a row in the height. This is the width/height symmetry of `C(w + h - 2, w - 1)`, and it matches the half-column of the nondecreasing rule, which is the same `(1 - x)^{-1/2}` Toeplitz matrix read in the height direction ([[fractional-width-and-height](pages/fractional-width-and-height.md)]). The parity clause is trivial here (even iff `h` is even). For the full count the symmetry fails: `H_h(w)` is real, while `F(w, h + 1/2)` has a nonzero imaginary part.

## What this settles, and what it leaves

- Settled: the half-sum of every castle row `h = 2..5` in closed generating-function form, with the leading constant `sqrt(h / (h - 1))`, the `sqrt(pi)` coefficient `G_h(1)`, its reading as minus the negative-width count, and the integer limit formula for `pi` at `h = 4`.
- Settled: the half-sum is never a regular-language count; the integer half-sums are context-free as castle-times-balanced-tail products.
- Open: a castle-intrinsic object with count `K_4(w)`, or a proof that the cut is forced (for instance, a bijection from skylines with a balanced suffix to some rule-changed castle family of [[castle-classification](pages/castle-classification.md)]).
- Open: a formula for `G_h(1)`. The values for `h = 2..8` are `0, 1/2, 1/30, 1/20, 41/1740, 103/6090, 421/35490`, with no visible pattern; only `h = 2` has the factor `1 - x`, so only there does the negative-width count sum to zero.

## Related Concepts

- [[fractional-block-count](pages/fractional-block-count.md)] - the same `(1 - x)^{alpha}` operator on one skyline; the box castle's `B_{1/2}` is the half-sum of a constant.
- [[fractional-width-and-height](pages/fractional-width-and-height.md)] - the continuation of `F` in `w` used for negative widths, the complex half-integer heights, and the half-column `U^{1/2}`.
- [[fractional-recurrences](pages/fractional-recurrences.md)] - the other `nabla^alpha` construction on castle recurrences.
- [[algebraic-transcendental-wall](pages/algebraic-transcendental-wall.md)] - why `pi` still arrives only through a limit.
- [[castle-counting-function](pages/castle-counting-function.md)] and [[generating-function-gallery](pages/generating-function-gallery.md)] - the rows being summed.
- [[castle-perimeter](pages/castle-perimeter.md)] - the other place castle counts become algebraic, graded by semi-perimeter.
- [[catalan-numbers](pages/catalan-numbers.md)] - the `C(x)` in `1 / sqrt(1 - 4x) = 1 / (1 - 2x C(x))`.
- [[castle-sequence-catalogue](pages/castle-sequence-catalogue.md)] - where the `K_h` rows are listed.

## Footnotes

[^1]: [[algebraic-languages-and-polyominoes-enumeration](pages/algebraic-languages-and-polyominoes-enumeration.md)] p.169 Abstract - "we prove that the number of convex polyominoes with perimeter 2n+8 is (2n+11)4^n - 4(2n+1)C(2n,n)."

[^2]: [[algebraic-languages-and-polyominoes-enumeration](pages/algebraic-languages-and-polyominoes-enumeration.md)] p.203 §12(6) - "Roughly speaking, the algebraicity has been 'concentrated' in the Dyck language. The generating functions p_I(t) and p_III(t) are rational expressions in term of t and c(t)."

[^exec]: Verified by execution (2026-09-23): Python 3, `fractions`, SymPy 1.14, mpmath. `F(w, h)` for `h = 2..5` by a transfer DP on (last height, block parity, height reached), block count as total ascent; checked against `F(4, 2) = 10`, `F(5, 5) = 906`, `F(6, 4) = 1729`. Rational `G_h` by Berlekamp-Massey over `Q` on 60 terms, numerator from the product with the denominator, factored by `sympy.factor`. Dyadic `H_h(w)` exactly in `fractions`; `4^w H_h`, `K_h`, and the matched sums as integers. Poles by `mpmath.polyroots` at 80 digits; the exponential part `sum_i -N(r_i)/D'(r_i) (1 - r_i)^{-1/2} r_i^{-w-1}` subtracted from the exact `H_h(w)` at `w = 50, 100, 200` (the `w = 200` rows at `h >= 3` lose precision and are not quoted). Backward extension of each row by its recurrence in `fractions`, recurrence checked on `-50 <= w <= 55`, the negative-width sum truncated at `w = -55`. `K_4(w)` to `w = 1600` in exact integers, the ratio at 400 digits. Nondecreasing identity: enumeration for `h <= 5`, `w <= 7` (count and block count `= h`), then the half-sum against `C(w + h - 3/2, w - 1)` in `fractions` for `h <= 6`, `w <= 19`. `G_h` and `G_h(1)` for `h = 6..8` by the same fit, checked on 40 further terms. OEIS lookups of the `h = 2..5` rows, `K_h`, `4^w H_h`, and the `H_2` numerators by the search API. All quoted numbers are the scripts' printed output.
