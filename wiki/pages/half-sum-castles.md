---
title: Half-sum castles
category: Analyses
summary: The order-1/2 fractional partial sum in the width of the even-block castle count, H_h(w) = Σ_k C(2k,k)/4^k A^e(w−k, h), has generating function G_h(x)/√(1−x), algebraic of degree 2 and not rational, so no finite strip rule counts it. A^e(w, h) grows like h^w/2, the pole at 1/h dominates the branch point at 1, and H_h(w)/A^e(w, h) → √(h/(h−1)). √π enters only in the branch remainder G_h(1)/√(πw), with G_h(1) = 0, 1/2, 1/30, 1/20 for h = 2..5; G_h(1) is minus the sum of the row continued to negative widths, and at h = 2 it vanishes because the numerator carries a factor 1 − x. Shifting the half-sum onto the dominant pole, with weights C(2k,k)(h/4)^k, gives h^w √(w/π) in the leading term; at h = 4 the weights are the integers C(2k,k), and π = lim w·16^w/K_4(w)^2 with K_4(w) = Σ_k C(2k,k) A^e(w−k, 4) = 1, 9, 51, 241, 1069, ... At h = 4 the integer half-sum counts castles followed by a balanced tail (a height-4 skyline with as many columns of height 1 as of height 4). For the nondecreasing castles the half-sum in the width is half a row in the height, C(w+h−2, w−1) → C(w+h−3/2, w−1).
tags: [analysis, castle, fractional-calculus, half-sum, cesaro, riemann-liouville, generating-function, algebraic, singularity-analysis, pi, wallis, central-binomial, context-free, nondecreasing, computation, oeis]
sources: [project-euler-502-brute-force, algebraic-languages-and-polyominoes-enumeration]
created: 2026-09-23
updated: 2026-10-29
---

# Half-sum castles

The partial sum of a count sequence is multiplication of its generating function by `(1 − x)^{−1}`; the Riemann-Liouville fractional sum of order `α` is multiplication by `(1 − x)^{−α}`. This page applies the sum of order `1/2` in the width to the even-block castle count `A^e(w, h)` ([[castle-counting-function](pages/castle-counting-function.md)]). [[fractional-block-count](pages/fractional-block-count.md)] applies the same operator with the opposite sign to a single skyline, and [[fractional-width-and-height](pages/fractional-width-and-height.md)] applies it in the height direction as the half-column of the nondecreasing rule.

## Definition and the tables

The coefficients of `(1 − x)^{−1/2}` are `C(2k, k)/4^k = 1, 1/2, 3/8, 5/16, 35/128, …`, so the **half-sum** of the height-`h` row is

```
H_h(w)  =  Σ_{k=0}^{w}  C(2k, k)/4^k · A^e(w − k, h),        Σ_w H_h(w) x^w  =  G_h(x) / √(1 − x),      (1)
```

with `G_h(x) = Σ_w A^e(w, h) x^w` the rational generating function of the row ([[generating-function-gallery](pages/generating-function-gallery.md)]) and `A^e(0, h) = 0`. Applying the half-sum twice gives the ordinary cumulative count, since `((1 − x)^{−1/2})^2 = (1 − x)^{−1}`. The rows, computed by the last-column transfer matrix and fitted by [[berlekamp-massey](pages/berlekamp-massey.md)]:[^exec]

| `h` | `G_h(x)` |
|---|---|
| 2 | `x (1 − x) / ((1 − 2x)(1 − 2x + 2x²))` |
| 3 | `x³ (3 − 3x + 2x²) / ((1 − 2x)(1 − 3x)(1 − 2x + 2x²)(1 − x + 2x²))` |
| 4 | `x (1 − 7x + 18x² − 26x³ + 40x⁴ − 44x⁵ + 32x⁶ − 16x⁷) / ((1 − 2x)(1 − 3x)(1 − 4x)(1 − x + 2x²)(1 − 4x + 8x² − 8x³ + 8x⁴))` |
| 5 | `2x³ (5 − 29x + 60x² − 94x³ + 112x⁴ − 104x⁵ + 64x⁶ − 32x⁷) / ((1 − 4x)(1 − 5x)(1 − 2x + 4x²)(1 − 3x + 2x² − 4x³)(1 − 4x + 8x² − 8x³ + 8x⁴))` |

The series give `A^e(4, 2) = 10`, `A^e(5, 5) = 906` and `A^e(6, 4) = 1729`, and the `h = 2` row is `A038505(w + 1)` ([[castle-counting-function](pages/castle-counting-function.md)]). The half-sums are dyadic rationals:

| `w` | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|---|---|
| `H_2(w)` | 1 | 7/2 | 63/8 | 231/16 | 3131/128 | 10929/256 | 83691/1024 | 345287/2048 |
| `H_3(w)` | 0 | 0 | 3 | 45/2 | 805/8 | 5765/16 | 149921/128 | 939243/256 |
| `H_4(w)` | 1 | 15/2 | 279/8 | 2167/16 | 65483/128 | 513081/256 | 8334451/1024 | 68729799/2048 |
| `H_5(w)` | 0 | 0 | 10 | 127 | 3883/4 | 47839/8 | 2137191/64 | 22845977/128 |

Two integer versions clear the denominators. `4^w H_h(w)` has generating function `G_h(4x)/√(1 − 4x)`. The **binomial half-sum** `K_h(w) = Σ_k C(2k, k) A^e(w − k, h)` has `G_h(x)/√(1 − 4x)` (it is not the convex castle generating function `K(q, z)` of [[castle-notation](pages/castle-notation.md)]):

| `h` | `K_h(w)` from the first nonzero term |
|---|---|
| 2 | 1, 5, 18, 60, 202, 702, 2508, 9136, 33742, 125934 |
| 3 | 3, 27, 149, 671, 2755, 10833, 41679, 158465, 598681 |
| 4 | 1, 9, 51, 241, 1069, 4671, 20353, 88383, 381583, 1635893 |
| 5 | 10, 142, 1210, 8222, 49806, 283570, 1557158, 8354490 |

## Where the √π goes

The weight `C(2k, k)/4^k` is asymptotic to `1/√(πk)`, and the half-sum of the constant sequence 1 is `(2w + 1) C(2w, w)/4^w ~ 2√(w/π)` (numerators A001803). So the half-sum of a sequence of radius of convergence 1 carries `√π` in its leading constant. Castle rows grow exponentially, and that changes the order of the terms.

**The dominant pole.** `G_h` has a simple pole at `x = 1/h` with `A^e(w, h) ~ h^w/2`, since `A^e = (A + S)/2` and `S/A → 0` ([[castle-entropy](pages/castle-entropy.md)]); every other pole lies inside the unit disk as well. Multiplying a simple pole at `r` by `(1 − x)^{−1/2}` scales its contribution by `(1 − r)^{−1/2}`, so

```
H_h(w)  =  Σ_i  c_i λ_i^w (1 − 1/λ_i)^{−1/2}  +  R_h(w),          H_h(w) / A^e(w, h)  →  √(h / (h − 1)),      (2)
```

where `A^e(w, h) = Σ_i c_i λ_i^w` is the exponential-polynomial form of the row. The leading ratio is `√2, √(3/2), √(4/3), √(5/4)` for `h = 2..5`, matched by the exact `H_h(100)/A^e(100, h)` to at least 11 digits.[^exec] To leading order, half-summing an exponentially growing castle row multiplies it by an algebraic constant.

**√π is in the remainder.** The branch point at `x = 1` contributes `G_h(x)(1 − x)^{−1/2} = G_h(1)(1 − x)^{−1/2} − G_h′(1)(1 − x)^{1/2} + ⋯`, so

```
R_h(w)  =  G_h(1) / √(πw)  +  O(w^{−3/2}).                                    (3)
```

| `h` | `G_h(1)` | `R_h(w) √(πw)` at `w = 50` | at `w = 100` |
|---|---|---|---|
| 2 | 0 | 0.00923 | 0.00480 |
| 3 | 1/2 | 0.48235 | 0.49091 |
| 4 | 1/30 | 0.03473 | 0.03409 |
| 5 | 1/20 | 0.04866 | 0.04931 |

At `h = 2` the numerator of `G_2` is divisible by `1 − x`, so the `w^{−1/2}` term vanishes. The next term is `G_2′(1)/(2√π w^{3/2})` with `G_2′(1) = 1`, and `2√π w^{3/2} R_2(w)` is `0.923, 0.960, 0.980` at `w = 50, 100, 200`.[^exec] `R_h(w)` is the difference between a rational number and an algebraic one, so `π` appears only in the limit, after the exponential part has been subtracted ([[algebraic-transcendental-wall](pages/algebraic-transcendental-wall.md)]).

## The coefficient of √π as a negative-width sum

The recurrence of each row runs backwards, which defines `A^e(w, h)` at negative integer widths; [[fractional-width-and-height](pages/fractional-width-and-height.md)] uses the same continuation at real `w`. For `h = 2..5` the two-sided sequence agrees with `A^e` at every `w ≥ 0`, and `A^e(−1, h) = −1/(2h(h − 1))`:

| `h` | `A^e(−1, h)`, `A^e(−2, h)`, `A^e(−3, h)`, `A^e(−4, h)` |
|---|---|
| 2 | −1/4, −1/8, 1/16, 5/32 |
| 3 | −1/12, −5/72, −19/432, −227/2592 |
| 4 | −1/24, −7/288, −37/3456, −175/41472 |
| 5 | −1/40, −9/800, −61/16000, −369/320000 |

For a single exponential, `Σ_{w ≥ 0} λ^w x^w + Σ_{w < 0} λ^w x^w = 1/(1 − λx) + 1/(λx − 1) = 0` as rational functions. So `G_h(x) = −Σ_{w ≤ −1} A^e(w, h) x^w`, and at `x = 1` the right side converges because every `|λ_i| > 1` (the smallest is `1.196`, at `h = 5`). Therefore

```
G_h(1)  =  − Σ_{w ≤ −1} A^e(w, h),                                            (4)
```

and the sums truncated at `w = −55` are `0`, `−0.5`, `−0.03333`, `−0.04999`, against `−G_h(1) = 0, −1/2, −1/30, −1/20`.[^exec] The coefficient of `1/√(πw)` in the half-sum is minus the sum of the row continued to negative widths. For `h = 6, 7, 8`, `G_h(1) = 41/1740, 103/6090, 421/35490`, and `h = 2` is the only one of these heights whose numerator has the factor `1 − x`.[^exec]

## The matched half-sum: π in the leading term

Moving the fractional singularity onto the dominant pole, with weights `C(2k, k)(h/4)^k` and generating function `G_h(x)/√(1 − hx)`, turns the simple pole into `(1 − hx)^{−3/2}`:

```
Ĥ_h(w)  =  Σ_k  C(2k, k) (h/4)^k  A^e(w − k, h)  ~  (1/2) h^w · 2√(w/π)  =  h^w √(w/π).      (5)
```

At `h = 4` the weights are integers and `Ĥ_4 = K_4`, the binomial half-sum `1, 9, 51, 241, 1069, 4671, 20353, …` of the section *Definition and the tables*. So `π` is a limit of exact castle integers:

```
π  =  lim_{w → ∞}  w · 16^w / K_4(w)^2,        K_4(w) = Σ_k C(2k, k) A^e(w − k, 4).        (6)
```

| `w` | 50 | 100 | 200 | 400 | 800 | 1600 |
|---|---|---|---|---|---|---|
| `p(w) = w 16^w / K_4(w)^2` | 3.26682 | 3.20168 | 3.17108 | 3.15620 | 3.14886 | 3.14522 |
| Richardson `2p(w) − p(w/2)` | 3.11399 | 3.13655 | 3.14047 | 3.14133 | 3.14153 | 3.14158 |

The error is `O(1/w)`, about `1.85π/w`, from the next terms of the expansion at the pole, and one Richardson step makes it `O(1/w²)`. The rational-weight versions at `h = 2, 3, 5` give `3.1298`, `3.2103`, `3.2308` at `w = 200`.[^exec] A pole and a square-root branch point at the same place also shape Delest and Viennot's count of convex polyominoes by perimeter, whose `4^n` term carries a subdominant `C(2n, n)`.[^1]

## What the half-sum counts

`G_h(x)/√(1 − x)` is algebraic of degree 2 over `Q(x)` and not rational, so no finite-state strip rule and no regular language of castle words has the half-sum as its count. The dyadic `H_h` is not a count. The integer versions are N-algebraic: `1/√(1 − 4x) = 1/(1 − 2x c(x))`, with `c(x)` the Catalan generating function ([[catalan-numbers](pages/catalan-numbers.md)]), so `G_h(x)/√(1 − 4x)` counts an even-block castle followed by a word of an unambiguous context-free language. The algebraicity sits in the tail, as in Delest and Viennot's convex polyominoes.[^2]

At `h = 4` the tail is a skyline. `C(2k, k) = [y^0] (y + 2 + 1/y)^k` is the number of skylines of width `k` on the heights `{1, 2, 3, 4}` with as many columns of height 4 as of height 1. So `K_4(w)` counts the skylines of width `w` on `{1, 2, 3, 4}` cut at a column into a prefix that is an even-block castle of height 4 and a balanced suffix, a product of a castle count and a tail count.

**The nondecreasing castles.** A nondecreasing castle of width `w` and height `h` has `c_w = h`, so its block count is `h`, and there are `C(w + h − 2, w − 1)` of them, with generating function `x/(1 − x)^h`. The half-sum raises the exponent by `1/2`:

```
Σ_k  C(2k, k)/4^k · C(w − k + h − 2, w − k − 1)  =  C(w + h − 3/2, w − 1),         (7)
```

the coefficient of `x^w` in `x (1 − x)^{−h−1/2}`, checked exactly for `h ≤ 6`, `w ≤ 19`.[^exec] The right side is the same binomial at height `h + 1/2`: for the nondecreasing castles, half a sum in the width is half a row in the height, by the symmetry of `C(w + h − 2, w − 1)` in `w` and `h`. It matches the half-column of the nondecreasing rule, the same `(1 − x)^{−1/2}` Toeplitz matrix read in the height direction ([[fractional-width-and-height](pages/fractional-width-and-height.md)]). The parity is trivial here: the castle has an even number of blocks exactly when `h` is even. For the full count the symmetry fails: `H_h(w)` is real, while the continuation `A^e(w, h + 1/2)` has a nonzero imaginary part.

## Related Concepts

- [[fractional-block-count](pages/fractional-block-count.md)] - the same `(1 − x)^α` operator on one skyline; the box castle's `B_{1/2}` is the half-sum of a constant.
- [[fractional-width-and-height](pages/fractional-width-and-height.md)] - the continuation of the count in `w` used for negative widths, the complex half-integer heights, and the half-column `U^{1/2}`.
- [[fractional-recurrences](pages/fractional-recurrences.md)] - fractional difference operators applied to castle recurrences.
- [[algebraic-transcendental-wall](pages/algebraic-transcendental-wall.md)] - `π` and `e` reached only through limits of rational and algebraic quantities.
- [[castle-counting-function](pages/castle-counting-function.md)] and [[generating-function-gallery](pages/generating-function-gallery.md)] - the rows `A^e(·, h)` and their generating functions.
- [[castle-perimeter](pages/castle-perimeter.md)] - castles by semi-perimeter, whose generating function is algebraic of degree 2.
- [[catalan-numbers](pages/catalan-numbers.md)] - the `c(x)` in `1/√(1 − 4x) = 1/(1 − 2x c(x))`.
- [[castle-sequence-catalog](pages/castle-sequence-catalog.md)] - the `K_h` rows.
- [[half-derivative-seminar](pages/half-derivative-seminar.md)] - a seminar on the half-sum with the fractional block count, the fractional width and height, and the walk on a tree castle.

## Footnotes

[^1]: [[algebraic-languages-and-polyominoes-enumeration](pages/algebraic-languages-and-polyominoes-enumeration.md)] p.169 Abstract - "we prove that the number of convex polyominoes with perimeter 2n+8 is (2n+11)4^n - 4(2n+1)C(2n,n)."
[^2]: [[algebraic-languages-and-polyominoes-enumeration](pages/algebraic-languages-and-polyominoes-enumeration.md)] p.203 §12(6) - "Roughly speaking, the algebraicity has been 'concentrated' in the Dyck language. The generating functions p_I(t) and p_III(t) are rational expressions in term of t and c(t)."
[^exec]: Verified by execution (Python 3.11 with `fractions`, SymPy and mpmath, 2026-10-16): `A^e(w, h)` for `h = 2..8` by a transfer DP on (last height, block parity, height reached), with `A^e(4, 2) = 10`, `A^e(5, 5) = 906`, `A^e(6, 4) = 1729`; `G_h` by Berlekamp-Massey over `Q` on 60 or 80 terms and factored, with `G_h(1)` for `h = 2..8`; the dyadic `H_h(w)`, `K_h(w)`, `4^w H_h(w)` exactly; the ratios `H_h(100)/A^e(100, h)` at 80 digits; the poles at 80 digits and the remainders `R_h(w) = H_h(w) − Σ_i (exponential part)` at `w = 50, 100`, and at `w = 200` for `h = 2`; the backward continuation of each row by its recurrence, the recurrence checked on `−50 ≤ w ≤ 55`, the negative-width sums truncated at `w = −55`; `K_4(w)` in exact integers to `w = 1600`, the ratios at 400 digits, and the rational-weight sums at `w = 200`; Equation (7) for `h ≤ 6`, `w ≤ 19` in `fractions`.
