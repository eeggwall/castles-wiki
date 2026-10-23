---
title: Fractional recurrences and the metallic means
category: Analyses
summary: For the recurrence ∇^α a_n = a_{n−1}, with ∇^α the Grunwald-Letnikov difference of order α, the growth constant g(α) = 1/r*(α), with r* the root in (0, 1) of (1 − r)^α = r, increases continuously from 1 at α = 0 to infinity, like α/log α. A rational order α = p/q gives an algebraic g of degree at most max(p, q); α = 1/3, 1/2, 2/3, 3/2 give the supergolden constant, the golden mean φ, ψ² and ψ³ = ψ + 1, with ψ the plastic number. An algebraic irrational α gives a transcendental g by the Gelfond-Schneider theorem. The metallic mean δ_a is g(α_a), and α_a is rational only at a = 1 (α_1 = 1/2), because 1 − 1/δ_a has norm a; for a ≥ 2, α_a is transcendental. For ∇^α a_n = a_{n−1} + a_{n−2}, Fibonacci at α = 0 and Pell at α = 1, the only metallic mean at a positive rational order is silver, at α = 1.
tags: [analysis, castle, fractional-calculus, grunwald-letnikov, metallic-mean, golden-ratio, transcendental, algebraic, gelfond-schneider, plastic-number, supergolden, reachable-field, characteristic-equation]
sources: [de-spinadel-1999-family-of-metallic-means]
created: 2026-09-21
updated: 2026-10-16
---

# Fractional recurrences and the metallic means

The metallic mean `δ_a = (a + √(a² + 4))/2` is the positive root of `x² − ax − 1`, de Spinadel's `σ_a^1` ([[metallic-means](pages/metallic-means.md)]).[^1] For every integer `a ≥ 1` it is the growth constant of a 0/1 strip rule, the ridge rule on `a + 1` heights ([[metallic-strip-realizability](pages/metallic-strip-realizability.md)]). This page puts the growth constants of a family of recurrences of real order `α` on one curve, finds the orders at which the curve passes through the metallic means, and decides which growth constants on the curve are algebraic.

## The recurrence

The Grunwald-Letnikov difference of order `α`, Equation (1) of [[fractional-block-count](pages/fractional-block-count.md)], is

```
(∇^α a)_n  =  Σ_{k=0}^{n} (−1)^k C(α, k) a_{n−k},        a_j = 0 for j < 0,
```

with `C(α, k) = α(α − 1)…(α − k + 1)/k!`. At `α = 1` it is the difference `a_n − a_{n−1}`. Consider the recurrence

```
∇^α a_n  =  a_{n−1}        (n ≥ 1),        a_0 = 1.                                     (1)
```

At `α = 1` it is `a_n = 2a_{n−1}`, with growth 2. At `α = 2` it is `a_n − 2a_{n−1} + a_{n−2} = a_{n−1}`, so `a_n = 3a_{n−1} − a_{n−2}`, with characteristic polynomial `x² − 3x + 1` and growth `φ² = (3 + √5)/2`. At `α = 1/2` the first terms are[^exec]

```
a_n  =  1, 1.5, 2.375, 3.8125, 6.1484, 9.9336, 16.0615, …,        a_60 / a_59  =  1.618034.
```

The weights `(−1)^k C(α, k)` are the coefficients of `(1 − x)^α`, so with `A(x) = Σ_n a_n x^n`, Equation (1) and `a_0 = 1` give `(1 − x)^α A(x) = x A(x) + 1`, and

```
A(x)  =  1 / D(x),        D(x)  =  (1 − x)^α − x.                                      (2)
```

**Growth.** For `α > 0`, expanding Equation (2) in powers of `x/(1 − x)^α` gives

```
1 / D(x)  =  Σ_{k≥0}  x^k (1 − x)^{−α(k+1)},
```

and every coefficient of `(1 − x)^{−β}` with `β > 0` is positive, so `A(x)` has positive coefficients. By Pringsheim's theorem, a power series with nonnegative coefficients has a singularity on the positive real axis at its radius of convergence. On `(0, 1)`, `D` is analytic and strictly decreasing, from `D(0) = 1` to `D(1) = −1`, so it has exactly one zero `r*(α)` there, and the radius of convergence of `A` is `r*(α)`. So the exponential growth rate of `a_n` is

```
g(α)  =  1 / r*(α),        (1 − r*)^α  =  r*.                                          (3)
```

**Monotonicity.** At fixed `r ∈ (0, 1)`, `(1 − r)^α` decreases in `α`, so `D` decreases in `α` and its zero `r*(α)` decreases. So `g` is continuous and strictly increasing, with `g(0) = 1` (at `α = 0`, `(1 − r)^0 = 1 = r`) and `g(1) = 2`. For large `α`, taking logarithms in Equation (3) gives `α r* (1 + O(r*)) = log(1/r*)`, so `α r* = W(α)(1 + o(1))`, with `W` the Lambert function, and `g(α) ~ α/W(α) ~ α/log α`. At `α = 10`, `r* = 0.1649` and `g = 6.064`, against `α/W(α) = 5.729`; at `α = 100`, `g = 29.93`, against `29.54`.[^exec] So `g` is a continuous, strictly increasing bijection from `[0, ∞)` onto `[1, ∞)`: every real number `≥ 1` is the growth constant of Equation (1) at exactly one order.

## Rational orders

**Proposition.** For a rational `α = p/q > 0` in lowest terms, `r*(α)` is a root of `(1 − r)^p = r^q`, so `g(α)` is algebraic of degree at most `max(p, q)`.

*Proof.* Both sides of Equation (3) are positive, and raising them to the power `q` gives `(1 − r*)^p = r*^q`, a polynomial equation of degree `max(p, q)` (for `p ≠ q`; at `α = 1` it is `1 − r = r`). Then `g = 1/r*` is a root of the reversed polynomial.

| `α` | equation for `r*` | equation for `g` | `g` | name |
|---|---|---|---|---|
| `1/3` | `r³ + r − 1 = 0` | `x³ − x² − 1 = 0` | `1.46557` | supergolden ([[tree-castle-by-area](pages/tree-castle-by-area.md)]) |
| `1/2` | `r² + r − 1 = 0` | `x² − x − 1 = 0` | `1.61803` | golden mean `φ` |
| `2/3` | `r³ − r² + 2r − 1 = 0` | `x³ − 2x² + x − 1 = 0` | `1.75488` | `ψ²` ([[plastic-number](pages/plastic-number.md)]) |
| `1` | `2r − 1 = 0` | `x − 2 = 0` | `2` | |
| `3/2` | `r³ − 2r² + 3r − 1 = 0` | `x³ − 3x² + 2x − 1 = 0` | `2.32472` | `ψ³ = ψ + 1` |
| `2` | `r² − 3r + 1 = 0` | `x² − 3x + 1 = 0` | `2.61803` | `φ²` |
| `3` | `r³ − 3r² + 4r − 1 = 0` | `x³ − 4x² + 3x − 1 = 0` | `3.14790` | cubic, discriminant `−31` |
| `4` | `r⁴ − 4r³ + 6r² − 5r + 1 = 0` | `x⁴ − 5x³ + 6x² − 4x + 1 = 0` | `3.62966` | quartic, discriminant `−283` |

Every polynomial in the table is irreducible, so in every row the degree of `g` is `max(p, q)`.[^exec] At `α = 1/2`, `r*` is the positive root of `r² + r − 1`, which is `1/φ`, since `φ² = φ + 1` gives `1 − 1/φ = 1/φ²`. The plastic number `ψ` is the real root of `ψ³ = ψ + 1`; substituting `ψ = y − 1` gives `(y − 1)³ − (y − 1) − 1 = y³ − 3y² + 2y − 1`, so `ψ + 1 = ψ³` is the root of the `α = 3/2` row.

The supergolden constant, `ψ²` and `ψ³` are Perron roots of 0/1 strip matrices on three heights ([[reachable-field-census](pages/reachable-field-census.md)], the section *Cubics at h = 3*).

## Irrational orders

The **Gelfond-Schneider theorem** says that if `a` and `b` are algebraic, `a ∉ {0, 1}` and `b` is irrational, then `a^b` is transcendental; equivalently, for nonzero algebraic `α` and `γ`, `log γ / log α` is rational or transcendental.[^2]

**Proposition.** If `α` is algebraic and irrational, then `g(α)` is transcendental.

*Proof.* If `r*` were algebraic, then `1 − r*` would be algebraic and in `(0, 1)`, and `r* = (1 − r*)^α` would be transcendental by the Gelfond-Schneider theorem, a contradiction. So `r*` is transcendental, and so is `g = 1/r*`.

Conversely, Equation (3) gives `α = log r* / log(1 − r*)`, so by the same theorem an algebraic `g(α)` forces `α` to be rational or transcendental. Both occur: `r = 1/3` gives `g = 3` at `α = log 3 / log(3/2) = 2.70951`, which is irrational and so transcendental. Since `g` is a bijection and the algebraic numbers are countable, `g(α)` is transcendental for all but countably many `α`, and since the rationals are dense and `g` is continuous, the algebraic values `g(p/q)` are dense in `[1, ∞)`. A 0/1 strip matrix has an integer characteristic polynomial, so every strip growth constant is algebraic, and the transcendental values of `g` are not growth constants of any strip rule ([[castle-strip](pages/castle-strip.md)]).

## The metallic means on the curve

The order `α_a` with `g(α_a) = δ_a` solves `(1 − 1/δ_a)^α = 1/δ_a`:

```
α_a  =  log δ_a / log( δ_a / (δ_a − 1) ).                                              (4)
```

| `a` | | `δ_a` | `α_a` |
|---|---|---|---|
| 1 | golden | `1.61803` | `1/2` |
| 2 | silver | `2.41421` | `1.64804` |
| 3 | bronze | `3.30278` | `3.31282` |
| 4 | | `4.23607` | `5.36116` |
| 5 | | `5.19258` | `7.70043` |
| 6 | | `6.16228` | `10.2697` |

At `a = 1`, `δ_1/(δ_1 − 1) = φ/(1/φ) = φ²`, so `α_1 = log φ / (2 log φ) = 1/2`.

**Proposition.** `α_a` is rational only for `a = 1`; for every `a ≥ 2`, `α_a` is transcendental.

*Proof.* `δ_a` and `1 − 1/δ_a` lie in the real quadratic field `Q(√(a² + 4))` (`a² + 4` lies strictly between `a²` and `(a + 2)²` and is not `(a + 1)²`, so it is not a square). The norm of `δ_a` is the product of the roots of `x² − ax − 1`, which is `−1`. The number `δ_a − 1` is a root of `(y + 1)² − a(y + 1) − 1 = y² + (2 − a)y − a`, so its norm is `−a`, and

```
N(1 − 1/δ_a)  =  N(δ_a − 1) / N(δ_a)  =  a,        N(1/δ_a)  =  −1.
```

A rational `α_a = m/n` with `m, n > 0` gives `(1 − 1/δ_a)^m = (1/δ_a)^n`, and taking norms gives `a^m = (−1)^n`, which forces `a = 1`. For `a ≥ 2`, `α_a` is therefore irrational, and as the ratio of the logarithms of the algebraic numbers `1/δ_a` and `1 − 1/δ_a` it is transcendental by the Gelfond-Schneider theorem.

At `a = 1` the relation is `1 − 1/φ = (1/φ)²`, with `m = 1`, `n = 2`.

## The recurrence ∇^α a_n = a_{n−1} + a_{n−2}

With two terms on the right,

```
∇^α a_n  =  a_{n−1} + a_{n−2},        characteristic equation  (1 − r)^α = r + r².         (5)
```

At `α = 0` it is `a_n = a_{n−1} + a_{n−2}`, the Fibonacci recurrence, with growth `φ`; at `α = 1` it is `a_n = 2a_{n−1} + a_{n−2}`, the Pell recurrence ([[pell-numbers](pages/pell-numbers.md)]), with growth `1 + √2`; at `α = 2` it is `a_n = 3a_{n−1}`, with growth 3. The argument for Equation (3) applies unchanged: the growth constant `g_2(α) = 1/r*` increases continuously from `φ` at `α = 0` to infinity.

**Proposition.** For `a ≥ 1` and rational `α > 0`, `g_2(α) = δ_a` holds only for `a = 2` and `α = 1`.

*Proof.* Let `r = 1/δ_a`. By the norm computation in the section *The metallic means on the curve*, `N(1 − r) = a`, and `r + r² = r(1 + r)` has norm `N(r) N(1 + 1/δ_a) = (−1) · N(δ_a + 1)/N(δ_a) = N(δ_a + 1)`, where `δ_a + 1` is a root of `(y − 1)² − a(y − 1) − 1 = y² − (a + 2)y + a`, so `N(r + r²) = a`. A rational `α = m/n` gives `(1 − r)^m = (r + r²)^n`, so `a^m = a^n`. For `a = 1`, `r + r² = 1`, and `(1 − r)^m = 1` with `0 < 1 − r < 1` forces `m = 0`. For `a ≥ 2`, `m = n`, so `α = 1` and `1 − r = r + r²`, whose positive root is `r = √2 − 1`, so `δ_a = 1 + √2` and `a = 2`.

So for every `a ≥ 3` the order at which `g_2` meets `δ_a` is irrational, and transcendental by the Gelfond-Schneider theorem; for bronze it is `α = 2.57943`. At `α = 1/2`, squaring Equation (5) gives `r⁴ + 2r³ + r² + r − 1 = 0`, an irreducible quartic, with `g_2(1/2) = 2.06599`.[^exec]

## Appearances in Sources

- [[de-spinadel-1999-family-of-metallic-means](pages/de-spinadel-1999-family-of-metallic-means.md)] - the metallic means as the positive roots of `x² − px − q`.

## Related Concepts

- [[metallic-means](pages/metallic-means.md)] - de Spinadel's family `σ_p^q`, with `δ_a = σ_a^1`.
- [[metallic-strip-realizability](pages/metallic-strip-realizability.md)] - the ridge rule `J − D` on `a + 1` heights, whose growth constant is `δ_a`.
- [[reachable-field-census](pages/reachable-field-census.md)] - the Perron roots of 0/1 strip matrices by number field, including the three cubics of the rational-order table.
- [[fractional-block-count](pages/fractional-block-count.md)] - the same Grunwald-Letnikov difference applied to the column heights of a castle.
- [[fractional-width-and-height](pages/fractional-width-and-height.md)] - the castle counts interpolated to real width and height.
- [[power-law-memory-rules](pages/power-law-memory-rules.md)] - strip rules whose condition applies the same weights to the last `K` columns.
- [[plastic-number](pages/plastic-number.md)] - `ψ`, `ψ² = 1.7549` and `ψ³ = ψ + 1 = 2.3247`.
- [[tree-castle-by-area](pages/tree-castle-by-area.md)] - the tree skylines of height at most 2 by area, which grow at the supergolden constant `1.4656`.
- [[algebraic-transcendental-wall](pages/algebraic-transcendental-wall.md)] - the castle counts at fixed height, whose closed forms have algebraic bases.
- [[eigenvalue-continued-fractions](pages/eigenvalue-continued-fractions.md)] - the continued fractions of the growth constants, `φ = [1; 1, 1, …]` among them.
- [[pell-numbers](pages/pell-numbers.md)] - the Pell recurrence, the case `α = 1` of Equation (5).
- [[pell-castle-strip](pages/pell-castle-strip.md)] - the anchored 1-smooth strips on the heights `{1, 2, 3}`, silver by width.

## Footnotes

[^1]: [[de-spinadel-1999-family-of-metallic-means](pages/de-spinadel-1999-family-of-metallic-means.md)] §3 L143-147 - "All the members of this family are positive quadratic irrational numbers that are the positive solutions of quadratic equations of the type (3.2) x² − px − q = 0".
[^2]: https://en.wikipedia.org/wiki/Gelfond%E2%80%93Schneider_theorem (read 2026-10-16) §"Statement" - "If a and b are algebraic numbers with a ∉ {0,1} and b irrational, then any value of a^b is a transcendental number", and "if α and γ are nonzero algebraic numbers, and we take any non-zero logarithm of α, then (ln γ)/(ln α) is either rational or transcendental".
[^exec]: Verified by execution (Python 3.11 with SymPy and mpmath, 2026-10-16): the first terms of Equation (1) at `α = 1/2` and the ratio `a_60/a_59`; the polynomials, roots, irreducibility and discriminants of the rational-order table; `r*` and `g` at `α = 10, 100` against `α/W(α)` and `α/log α`; `log 3 / log(3/2)`; the values of Equation (4) for `a ≤ 6`; `N(1 − 1/δ_a) = N(1/δ_a + 1/δ_a²) = a` for `a ≤ 6`; the bronze order on Equation (5); the irreducibility of `r⁴ + 2r³ + r² + r − 1` and `g_2(1/2)`, also as the limit of `a_80/a_79` for the recurrence (5).
