---
title: Fractional recurrences: the rung between rungs
category: Analyses
summary: The metallic ladder δ_a = (a + √(a²+4))/2 sits on a continuous curve of growth constants. The Atici-Eloe nabla recurrence ∇^α a_n = a_{n-1} has characteristic equation (1-r)^α = r; its growth constant g(α) = 1/r(α) is a continuous, strictly increasing bijection from [0,∞) to [1,∞). Rational α = p/q gives an algebraic growth constant of degree ≤ max(p,q); algebraic irrational α gives a transcendental growth constant (Gelfond-Schneider), and an algebraic growth constant forces α to be rational or transcendental, so g(α) is transcendental for all but countably many α. The metallic ladder meets this curve at one rational point: golden at α = 1/2, exactly. Silver, bronze, copper, nickel each meet it at a transcendental α_a, because δ_a - 1 has norm -a in Q(√(a²+4)) and so is a unit only at a = 1. Small rational α give three of the wiki's cubic Perron roots: α = 1/3 is supergolden, α = 2/3 is plastic squared, α = 3/2 is ψ³ = ψ+1. The curve takes every value ≥ 1, so it passes through every algebraic Perron root of the reachable-field census and also through transcendental values that no castle strip realizes.
tags: [analysis, castle, fractional-calculus, atici-eloe, nabla, mittag-leffler, metallic-mean, golden-ratio, transcendental, algebraic, baker-theorem, gelfond-schneider, plastic-number, supergolden, reachable-field, characteristic-equation]
sources: [pe502-pell-castle-strip]
created: 2026-09-21
updated: 2026-09-28
---

# Fractional recurrences: the rung between rungs

## The framing

The metallic mean `δ_a = (a + √(a²+4))/2` is a continuous function of `a`, and the integer values `a = 1, 2, 3, …` are realized as growth constants of 0/1 castle-strip transfer matrices ([[metallic-means](pages/metallic-means.md)], [[metallic-strip-realizability](pages/metallic-strip-realizability.md)]). The [[reachable-field-census](pages/reachable-field-census.md)] widens the target from the ladder to every real quadratic Perron root. This page places these algebraic values on one continuous curve of growth constants.

Discrete fractional calculus (Atici and Eloe, 2007-2009) supplies such a curve. The **nabla fractional difference** operator `∇^α` (Grunwald-Letnikov style) takes the integer-order difference `∇a_n = a_n - a_{n-1}` and interpolates it continuously in `α`, so a linear recurrence has a real-order version. The equation

```
∇^α a_n  =  a_{n-1}
```

is called the **fractional Fibonacci** recurrence here. At `α = 1` it is `a_n - a_{n-1} = a_{n-1}`, i.e. `a_n = 2 a_{n-1}` - a geometric sequence, growth `2`. At `α = 2` it is `a_n - 2 a_{n-1} + a_{n-2} = a_{n-1}`, i.e. `a_n = 3 a_{n-1} - a_{n-2}` - a second-order recurrence with characteristic polynomial `x² - 3x + 1`, growth `(3 + √5)/2 = φ²`. The order `α` varies continuously between and beyond these values.

This page **computes the growth constant `g(α)` of the fractional Fibonacci as a function of `α`, finds where it meets the metallic ladder, and settles which values are algebraic.**

## The characteristic equation

Write generating functions `A(x) = Σ_{n≥0} a_n x^n` with initial conditions absorbed into a numerator. The nabla operator acts as multiplication by `(1 - x)`:

```
Σ_n (∇a)_n x^n  =  (1 - x) A(x),
```

taking `a_{-1} = 0`. Its `α`-th power is the Grunwald-Letnikov extension,

```
(∇^α a)_n  =  Σ_{k=0}^{n} (-1)^k C(α, k) a_{n-k},
```

with `C(α, k)` the generalized binomial coefficient (a polynomial in `α` of degree `k`, well defined for real `α`). This corresponds to multiplication by `(1 - x)^α` on the generating-function side, expanded as the binomial series `Σ_{k≥0} (-1)^k C(α, k) x^k` (convergent for `|x| < 1`). Substituting into `∇^α a_n = a_{n-1}`:

```
(1 - x)^α · A(x)  =  x · A(x)  +  (initial-condition polynomial),
```

so `A(x) = N(x) / D(x)` with

```
D(x)  =  (1 - x)^α  -  x.
```

The growth constant is the reciprocal of the smallest positive real root of `D`:[^1]

```
D(r) = 0    ⟺    (1 - r)^α = r,        g(α) := 1 / r*(α).
```

Two facts follow directly from `D`. First, `D` is decreasing in `r` on `(0, 1)` (`(1-r)^α` decreases in `r`; `-r` decreases in `r`), with `D(0) = 1 > 0` and `D(1) = -1 < 0`, so a unique root `r*(α) ∈ (0, 1)` exists. Second, `D` is decreasing in `α` at fixed `r ∈ (0, 1)` (`(1-r)^α` is decreasing in `α` when the base `1-r < 1`), so `r*(α)` decreases with `α` and `g(α)` **strictly increases**. Limits: `g(0) = 1` (`r* = 1`), `g(1) = 2` (`r* = 1/2`), and `g(α) → ∞` as `α → ∞` (from the tail estimate `r* ~ log(α)/α`, so `g(α) ~ α/log α`).[^2] So `g` is a continuous, strictly increasing bijection `[0, ∞) → [1, ∞)`.

Every real number `≥ 1` is `g(α)` for exactly one `α`. The rest of the page is about **which α give algebraic g, which give transcendental g**, and **where the metallic ladder falls on this curve**.

## The clean table

Small rational orders `α = p/q` (in lowest terms) turn `(1 - r)^α = r` into the polynomial `(1 - r)^p = r^q`, a rational algebraic equation whose smallest positive root is an algebraic number of degree `≤ max(p, q)`. Solving each by hand gives the identifications:[^3]

| `α = p/q` | equation on `r` | equation on `g = 1/r` | growth `g` | identification |
|---|---|---|---|---|
| `1/3` | `r³ + r - 1 = 0` | `x³ - x² - 1 = 0` | `1.4656…` | supergolden ([[tree-castle-by-area](pages/tree-castle-by-area.md)]) |
| `1/2` | `r² + r - 1 = 0` | `x² - x - 1 = 0` | `1.6180…` | **golden `φ`** ([[metallic-means](pages/metallic-means.md)]) |
| `2/3` | `r³ - r² + 2r - 1 = 0` | `x³ - 2x² + x - 1 = 0` | `1.7549…` | plastic squared `ψ²` ([[plastic-number](pages/plastic-number.md)]) |
| `1` | `2r - 1 = 0` | `x - 2 = 0` | `2` | integer |
| `3/2` | `r³ - 2r² + 3r - 1 = 0` | `x³ - 3x² + 2x - 1 = 0` | `2.3247…` | `ψ³ = ψ + 1` (plastic cubed) |
| `2` | `r² - 3r + 1 = 0` | `x² - 3x + 1 = 0` | `2.6180…` | golden squared `φ²` |
| `3` | `r³ - 3r² + 4r - 1 = 0` | `x³ - 4x² + 3x - 1 = 0` | `3.1479…` | cubic (`disc = -31`) |
| `4` | `r⁴ - 4r³ + 6r² - 5r + 1 = 0` | `x⁴ - 5x³ + 6x² - 4x + 1 = 0` | `3.6297…` | quartic |

Three of the census's cubic Perron roots ([[reachable-field-census](pages/reachable-field-census.md)]) - **supergolden, plastic squared, plastic cubed** - appear here as rational-`α` growth constants, at `α = 1/3, 2/3, 3/2`.

The two derivations that need verification are the golden identity at `α = 1/2` and the two reciprocal-polynomial identifications for the cubics.

**Golden at `α = 1/2`.** The identity `1 - 1/φ = 1/φ²` is a defining property of `φ`: from `φ² = φ + 1`, divide by `φ²` to get `1 = 1/φ + 1/φ²`, so `1/φ² = 1 - 1/φ`. Squaring both sides of `(1 - r)^{1/2} = r` gives `1 - r = r²`, i.e. `r² + r - 1 = 0`, whose positive root is `r = (√5 - 1)/2 = 1/φ`. Then `1 - r = 1 - 1/φ = 1/φ² = r²`, consistent, and `g = 1/r = φ`. So `α = 1/2` hits golden **exactly**.[^4]

**Cubic reciprocals.** The equation `(1 - r)^{1/3} = r` gives `1 - r = r³`, i.e. `r³ + r - 1 = 0`; substituting `r = 1/x` and clearing denominators gives `1 + x² - x³ = 0`, i.e. `x³ - x² - 1 = 0` - the supergolden minimal polynomial. Analogously `(1 - r)^{2/3} = r` gives `(1 - r)² = r³`, i.e. `r³ - r² + 2r - 1 = 0`, whose reciprocal is `x³ - 2x² + x - 1 = 0` - the minimal polynomial of `ψ²` ([[plastic-number](pages/plastic-number.md)]). And `(1 - r)^{3/2} = r` gives `(1 - r)³ = r²`, i.e. `r³ - 2r² + 3r - 1 = 0`, whose reciprocal is `x³ - 3x² + 2x - 1 = 0` - the minimal polynomial of `ψ³ = ψ + 1` (from `ψ³ - ψ - 1 = 0`, sub `y = ψ + 1` i.e. `ψ = y - 1`; `(y-1)³ - (y-1) - 1 = y³ - 3y² + 2y - 1 = 0`).[^5]

## The algebraic/transcendental dichotomy

The table above shows rational `α` gives algebraic `g`. A partial converse follows from the Gelfond-Schneider theorem.

**Theorem (rational-α algebraicity).** For every rational `α = p/q > 0` in lowest terms, the equation `(1 - r)^α = r` reduces to the polynomial `(1 - r)^p = r^q`, i.e. `Σ_{k=0}^{p} (-1)^k C(p, k) r^k = r^q`. The positive root `r*` is algebraic of degree `≤ max(p, q)`, and `g = 1/r*` is algebraic of the same degree.

The bound `max(p, q)` is often sharp: for `α = 1/3, 2/3, 3/2, 3` the degrees are `3, 3, 3, 3` (attained at `max(p,q)`), and `α = 1/2, 2` give quadratics.

**Theorem (algebraic-α transcendence).** For every algebraic irrational `α > 0`, the growth constant `g(α) = 1/r*(α)` is transcendental.

*Proof.* Suppose for contradiction that `r*` is algebraic. From `(1 - r*)^α = r*` and `r* ∈ (0, 1)`, both `r*` and `1 - r*` are algebraic in `(0, 1)`, so `log r*` and `log(1 - r*)` are nonzero. Taking logarithms of the characteristic equation:

```
α  =  log r*  /  log(1 - r*).
```

Both numerator and denominator are logarithms of nonzero algebraic numbers. By the **Gelfond-Schneider theorem** (Baker's theorem specialized to two logarithms), the ratio `log a / log b` of two logs of algebraic numbers (each `≠ 0, 1`) is **either rational or transcendental** - never irrational algebraic. Since `α` is algebraic irrational, this is a contradiction, so `r*` cannot be algebraic - hence `g` is transcendental.[^6] ∎

The same identity shows that transcendental `α` can give algebraic growth: for any algebraic `r ∈ (0, 1)` with `log r / log(1 - r)` irrational, `α = log r / log(1 - r)` is transcendental by Gelfond-Schneider and `g(α) = 1/r` is algebraic. For example `r = 1/3` gives `g = 3` at `α = log 3 / log(3/2) ≈ 2.7095`, a transcendental order.

Combining: **an algebraic `g(α)` forces `α` to be rational or transcendental.** The algebraic values of `g` are countable, so `g(α)` is transcendental for all but countably many `α`, in particular for every algebraic irrational `α`; the rational `α` give a countable dense set of algebraic growth constants.

## Where the metallic ladder crosses the curve

The metallic ratio `δ_a` appears as `g(α_a)` for a unique `α_a ≥ 0`, obtained by solving `(1 - 1/δ_a)^α = 1/δ_a`, i.e.

```
α_a  =  log δ_a  /  log( δ_a / (δ_a - 1) ).
```

Numerical values through the first six rungs, computed from `δ_a = (a + √(a²+4))/2`:[^7]

| `a` | metal | `δ_a` | `α_a` | algebraic? |
|---|---|---|---|---|
| 1 | golden | `1.6180…` | **`1/2`** (exact) | rational |
| 2 | silver | `2.4142…` | `1.6480…` | transcendental |
| 3 | bronze | `3.3028…` | `3.3128…` | transcendental |
| 4 | copper | `4.2361…` | `5.3612…` | transcendental |
| 5 | nickel | `5.1926…` | `7.7004…` | transcendental |
| 6 | (unnamed) | `6.1623…` | `10.2697…` | transcendental |

Golden is the **only** metallic mean hit at a rational `α`.

### Why golden alone lands on a rational `α`

The order-`α` equation for the `a`-th metallic mean is `(1 - 1/δ_a)^α = 1/δ_a`. Both bases live in the real quadratic field `Q(√(a²+4))`. A rational `α = m/n` requires the multiplicative relation

```
(1 - 1/δ_a)^m  =  (1/δ_a)^n     in   Q(√(a²+4)).
```

Take norms to `Q`. The metallic mean `δ_a` is a unit in the ring of integers (norm `-1`), because `δ_a` satisfies `x² - a x - 1 = 0` with product of roots `= -1`, so `N(δ_a) = -1` and `N(1/δ_a) = -1`.[^8] For `1 - 1/δ_a = (δ_a - 1)/δ_a`, the norm is `N(δ_a - 1)/N(δ_a) = N(δ_a - 1)/(-1)`. Compute `N(δ_a - 1)`: from `δ_a² - a δ_a - 1 = 0`, sub `y = δ_a - 1` (i.e. `δ_a = y + 1`) to get `(y+1)² - a(y+1) - 1 = y² + (2 - a) y - a = 0`. The product of roots is `-a`, so

```
N(δ_a - 1)  =  -a,       hence      N(1 - 1/δ_a)  =  -a / -1  =  a.
```

The multiplicative relation `(1 - 1/δ_a)^m = (1/δ_a)^n` then forces `a^m = (-1)^n`, i.e. `a^m = ±1`, which for the natural numbers `a ≥ 1` is possible **only for `a = 1`**. For `a ≥ 2` the norm `a^m` grows unless `m = 0`, and then `n = 0` too, a trivial (non-)relation. So `α_a` is rational only for `a = 1`, and by Gelfond-Schneider (the theorem above), `α_a` is **transcendental** for every `a ≥ 2`.[^9]

The golden ratio's `α = 1/2` identity is the statement that **`δ_1 - 1 = 1/δ_1` is itself a unit of `Z[φ]`**. No other metallic mean has this property: `δ_a - 1` has norm `-a` for `a ≥ 2`, so it is not a unit.

## The reachable-field census, extended and complemented

The [[reachable-field-census](pages/reachable-field-census.md)] settles which algebraic numbers are Perron roots of 0/1 castle-strip transfer matrices: every real quadratic field is reachable, and cubic / quartic frontiers appear at heights `3, 4`. Since `α ↦ g(α)` is a bijection onto `[1, ∞)`, every one of those algebraic growth constants is `g(α)` for exactly one `α`, and the curve also takes transcendental values.

**Two extensions of the census picture.**

1. **The curve is dense on the algebraic side.** As `α` ranges over the rationals, `g(α)` takes algebraic values, at countably many points on the curve. These include the golden ratio (`α = 1/2`), supergolden (`α = 1/3`), plastic squared (`α = 2/3`), and plastic cubed (`α = 3/2`), three of the census's cubic Perron roots **as rational-`α` points on one curve**.

2. **The curve is transcendental almost everywhere.** For all but countably many `α`, including every algebraic irrational `α`, `g(α)` is transcendental. These transcendental growth constants lie **outside the reachable-field census**: no 0/1 castle-strip transfer matrix has a transcendental Perron root, because a transfer matrix's characteristic polynomial has integer coefficients, so its eigenvalues are algebraic. So the fractional-Fibonacci curve visits every real `≥ 1`, of which the algebraic ones live inside the census and the transcendental ones live outside it.

The **complement statement**: fractional recurrences fill the transcendental interior between the metallic-ladder rungs, and their generic growth constants are numbers a castle strip can never realize. The complement is not full: a countable dense subset of the fractional-recurrence curve lands on the algebraic side, and it hits three of the cubic Perron roots in the reachable-field census.

## The Pell / Fibonacci-Pell interpolation family

A cleaner statement of the "sweeping between order-1 and order-2" framing is available with a two-term forcing. Consider

```
∇^α a_n  =  a_{n-1}  +  a_{n-2}.
```

At `α = 0` the operator is the identity, so `a_n = a_{n-1} + a_{n-2}` - **Fibonacci**, growth `φ`. At `α = 1` it is `(a_n - a_{n-1}) = a_{n-1} + a_{n-2}`, i.e. `a_n = 2 a_{n-1} + a_{n-2}` - **Pell** ([[pell-numbers](pages/pell-numbers.md)]), growth `1 + √2`. At `α = 2` the operator collapses the two forcing terms and gives `a_n = 3 a_{n-1}`, growth `3`. The characteristic equation is

```
(1 - r)^α  =  r + r²  =  r(1 + r).
```

The same monotone-continuous-bijection analysis applies: `g_2(α) := 1/r*(α)` is strictly increasing from `φ` at `α = 0` to `∞`, passing through `1 + √2` at `α = 1` and `3` at `α = 2`.

Two clean rational-`α` points sit on this curve without any tricks: **golden at `α = 0`** and **silver at `α = 1`**, both by construction. The question is again which further metallic-ladder rungs land at rational `α`.

Bronze `(3 + √13)/2`: the growth relation `r + r² = 4 - √13` (verified by expanding `(√13 - 3)/2 · ((√13 - 3)/2 + 1) = ((√13 - 3)(√13 - 1))/4 = (16 - 4√13)/4 = 4 - √13`) and `1 - r = (5 - √13)/2` give the equation `((5 - √13)/2)^α = 4 - √13`. Norms in `Q(√13)`: `N((5 - √13)/2) = (25 - 13)/4 = 3`, and `N(4 - √13) = 16 - 13 = 3`. Rational `α = m/n` would require `3^m = 3^n`, i.e. `m = n`, and then the equation reduces to `(5 - √13)/2 = 4 - √13`, contradicting `√13 = 3`. So bronze is hit at a **transcendental** `α ≈ 2.58` on this curve too.[^10] The same norm mechanism excludes copper, nickel, and every higher metallic mean.

So the Fibonacci-Pell interpolation family has **exactly two rational-`α` metallic hits** (golden at `α = 0`, silver at `α = 1`), and every higher rung crosses the curve at a transcendental order. The `α = 1/2` point of this family is a root of the irreducible quartic `r⁴ + 2r³ + r² + r - 1` (from squaring both sides), not on the metallic ladder.

## The discrete Mittag-Leffler function

The continuous-time counterpart of `∇^α a_n = a_{n-1}` is a fractional differential equation, and the classical solutions of `D^α y = λ y` are **Mittag-Leffler functions** `E_α(z) = Σ_{k≥0} z^k / Γ(αk + 1)`, fractional exponentials. The discrete (nabla) Mittag-Leffler functions have generating functions of the form[^11]

```
(1 - x)^{β - 1}  /  ((1 - x)^α - λ)
```

with `λ` a constant. The fractional Fibonacci denominator `(1 - x)^α - x` has the same shape with `λ` replaced by `x`; expanding,

```
1 / ((1 - x)^α - x)  =  Σ_{k≥0}  x^k (1 - x)^{-α(k+1)},
```

a series of discrete Mittag-Leffler type with positive coefficients for `α > 0`. Its dominant singularity is the simple zero `r*(α)` of the denominator (`D'(r*) = -α(1 - r*)^{α-1} - 1 ≠ 0`), so `a_n ~ C · g(α)^n` with `C = -N(r*) / (r* D'(r*))`.

## What this settles, and what it leaves

**Settled:**
- The fractional-Fibonacci growth curve `g(α) = 1/r*(α)`, `r*` the smallest positive root of `(1-r)^α = r`, is a continuous, strictly increasing bijection `[0, ∞) → [1, ∞)`.
- Rational `α` gives algebraic `g(α)`, algebraic irrational `α` gives transcendental `g(α)`, and an algebraic `g(α)` forces `α` rational or transcendental; the algebraic values are countable and dense on the curve. Small rational `α` give three of the census's cubic Perron roots (supergolden at `1/3`, plastic-squared at `2/3`, plastic-cubed at `3/2`).
- Golden is the unique metallic mean hit at a rational `α`, at `α = 1/2` exactly. The algebraic reason is that `δ_1 - 1 = 1/δ_1` is a unit, while `δ_a - 1` for `a ≥ 2` has norm `-a` and is not a unit.
- Every metallic mean `δ_a` with `a ≥ 2` is hit at a transcendental `α_a` (Gelfond-Schneider via the norm obstruction). Values: `α_2 ≈ 1.648`, `α_3 ≈ 3.313`, `α_4 ≈ 5.361`, `α_5 ≈ 7.700`.
- The Fibonacci-Pell interpolation family `∇^α a_n = a_{n-1} + a_{n-2}` has golden at `α = 0` and silver at `α = 1` (both rational-`α`, by construction), and bronze and beyond at transcendental `α`.
- Fractional recurrences at all but countably many `α` (every algebraic irrational `α` among them) produce transcendental growth constants, which cannot be Perron roots of any castle-strip 0/1 transfer matrix. So the curve passes through the census's algebraic Perron roots and also through transcendentals no castle strip realizes.

**Open:**
- **Cubic frontier at rational `α`.** The rational orders `1/3, 2/3, 3/2` hit three of the census's cubic Perron roots (plastic cubed `x³ - 3x² + 2x - 1` among them); do other small rational `α` land on the remaining census cubics (`Q(ζ₇)⁺` at `x³ - x² - 2x + 1`, tribonacci at `x³ - x² - x - 1`, and the rest of the height-3 list)? A direct computation of `α = p/q` up to `p + q ≤ 8` and comparison to the census cubic list would settle this.
- **Where the *other* metallic ladders live.** The `∇^α a_n = c a_{n-1}` family with `c ≥ 2` is not treated above. Its characteristic `(1 - r)^α = c r` gives at `α = 1`, growth `1 + c`, an integer; at `α = 2`, a member of `Q(√(4c + 1))` - a metallic-adjacent quadratic field. Which `c` produce silver, bronze, etc. at integer `α`?
- **The Caputo variant.** The Grunwald-Letnikov nabla `∇^α` used above respects the initial condition `a_{-1} = 0` implicitly; the Caputo version differentiates first and keeps a classical set of initial values. The characteristic equation is the same at the level of growth constants, but the specific sequence values differ by a `(1 - x)^{α-1}` factor. Whether the *sequences* (not just their growth) match any OEIS entry is unexplored.
- **The `α → ∞` regime and Lambert-W control.** The asymptotic `r*(α) ~ log(α)/α` and `g(α) ~ α / W(α)` (Lambert `W`) is stated as a limit; a full asymptotic expansion, and whether the correction terms are algebraically or transcendentally structured, is left open.

## Related Concepts

- [[metallic-means](pages/metallic-means.md)] - the discrete ladder this page places on a continuous curve; the α = 1/2 identity singles out `δ_1` among the metallic means.
- [[reachable-field-census](pages/reachable-field-census.md)] - the algebraic Perron roots this curve passes through; its rational-α points hit three of the census's cubic Perron roots.
- [[algebraic-transcendental-wall](pages/algebraic-transcendental-wall.md)] - rational α gives algebraic growth, and algebraic irrational α gives transcendental growth by Gelfond-Schneider rather than through a Stirling or Catalan limit.
- [[plastic-number](pages/plastic-number.md)] - `ψ² = 1.7549` at α = 2/3 and `ψ³ = 2.3247` at α = 3/2, cleanly parameterized as fractional-Fibonacci growths.
- [[tree-castle-by-area](pages/tree-castle-by-area.md)] - the supergolden `1.4656` (α = 1/3) appears here as a fractional-Fibonacci growth.
- [[metallic-strip-realizability](pages/metallic-strip-realizability.md)] - the discrete side: `M_h = J - D` realizes `δ_{h-1}` at integer `h`; here the same rung is a specific transcendental `α`, so integer-strip realizability and rational-α realizability are two different regularity properties on the ladder.
- [[fractional-block-count](pages/fractional-block-count.md)] and [[fractional-width-and-height](pages/fractional-width-and-height.md)] - the two earlier fractional-order studies, which run the same `∇^α` operator on skylines rather than on the recurrence.
- [[eigenvalue-continued-fractions](pages/eigenvalue-continued-fractions.md)] - `α = 1/2` gives `g = φ`, whose continued fraction is `[1; 1, 1, …]`.
- [[pell-numbers](pages/pell-numbers.md)] - silver `1 + √2` at `α = 1` in the Fibonacci-Pell interpolation.
- [[pell-castle-strip](pages/pell-castle-strip.md)] - the castle-side realization of the α = 1 silver rung: the anchored 1-smooth height-3 strip whose Perron root *is* `1 + √2`.
- [[power-law-memory-rules](pages/power-law-memory-rules.md)] - runs the same GL kernel on the strip *rule* rather than on the count sequence; a K-truncation ratchets its Perron root through the reachable-field census (plastic, supergolden, golden, plastic-squared) as memory grows, and the K -> infinity limit at `h = 2` sits back on integer `2` rather than reaching a new transcendental.

## Footnotes

[^1]: The generating-function identity `(1 - x)^α A(x) = x A(x) + (initial)` is the Z-transform of the difference equation `∇^α a_n = a_{n-1}` with a_{-1} = 0. Grunwald-Letnikov nabla differences and their `(1 - x)^α` transform: standard fractional-calculus fact, e.g. (cited, not read) Podlubny (1999) *Fractional Differential Equations*, §2.4; Atici and Eloe (2007) "A transform method in discrete fractional calculus," *International Journal of Difference Equations* 2(2), 165-176 - the discrete Riemann-Liouville / nabla framework. The growth constant is `1/ρ` where `ρ` is the smallest-modulus singularity, the positive root `r*` of `(1 - x)^α - x` on `(0, 1)`: `1/((1 - x)^α - x) = Σ_k x^k (1 - x)^{-α(k+1)}` has positive coefficients, so by Pringsheim's theorem its radius of convergence is a positive real singularity, and the denominator has no zero on `(0, r*)`.

[^2]: The `α → ∞` asymptotic: at fixed small `r > 0`, `(1-r)^α = e^{α log(1-r)} = e^{-αr(1 + r/2 + …)}`. Setting this `= r`: `-αr(1 + O(r)) = log r`, so `αr ~ -log r`, so `r ~ log(1/r)/α`. Iterating with `r ~ log α / α` in the log: `r ~ log(α / log α) / α ~ log α / α`. So `g(α) = 1/r ~ α / log α`. Numerical check: `α = 10` gives `r ≈ 0.165, g ≈ 6.06`, against `α/W(α) ≈ 5.73` and `α/log α ≈ 4.34`; `α = 100` gives `r ≈ 0.0334, g ≈ 29.9`, against `α/W(α) ≈ 29.5` and `α/log α ≈ 21.7`. The Lambert `W` form `α r ≈ W(α)` is the sharper leading term; `α/log α` converges slowly.

[^3]: All identifications verified by hand-computation and reciprocal-polynomial matching. For `α = p/q > 0` in lowest terms, `(1-r)^α = r` iff `(1-r)^p = r^q` (raise both sides to the `q`-th power, valid because both sides are positive). The reciprocal polynomial of a monic integer polynomial `P(r) = Σ c_k r^k` of degree `d` is `x^d P(1/x)`, so the polynomial satisfied by `g = 1/r` has coefficients reversed (and, if not monic, is normalized). Small-α values and named identifications: supergolden `x³ - x² - 1` per [[tree-castle-by-area](pages/tree-castle-by-area.md)] and [[reachable-field-census](pages/reachable-field-census.md)]; plastic-squared `x³ - 2x² + x - 1` per [[plastic-number](pages/plastic-number.md)]; plastic-cubed `x³ - 3x² + 2x - 1` derived below in the body.

[^4]: `φ² = φ + 1` (defining) ⟹ `1 = 1/φ + 1/φ²` (divide by `φ²`) ⟹ `1/φ² = 1 - 1/φ`. So `(1 - 1/φ)^{1/2} = (1/φ²)^{1/2} = 1/φ`, verifying the fractional-Fibonacci equation at `α = 1/2` with root `r = 1/φ`. Growth `g = 1/r = φ`, exact.

[^5]: Plastic cubed: `ψ³ = ψ + 1` from `ψ³ - ψ - 1 = 0` (defining of `ψ` on [[plastic-number](pages/plastic-number.md)]); sub `y = ψ + 1` (so `ψ = y - 1`) into `ψ³ - ψ - 1 = 0`: `(y-1)³ - (y-1) - 1 = y³ - 3y² + 3y - 1 - y + 1 - 1 = y³ - 3y² + 2y - 1 = 0`. Numerical: `ψ ≈ 1.3247`, `ψ + 1 ≈ 2.3247`; check `2.3247³ - 3·2.3247² + 2·2.3247 - 1 = 12.559 - 16.213 + 4.649 - 1 ≈ -0.005` (rounding, agrees).

[^6]: Gelfond-Schneider (1934): for algebraic `a, b ≠ 0, 1`, `log a / log b` is rational or transcendental. With `a = r*` and `b = 1 - r*` (both algebraic if `r*` is), `α = log r* / log(1 - r*)`, so an algebraic irrational `α` is excluded and `r*` is transcendental. For transcendental `α` the argument gives nothing, and transcendental `α` with algebraic `g` exist (body). The metallic values `α_a` (`a ≥ 2`) are shown transcendental by the norm argument in the body together with Gelfond-Schneider.

[^7]: `α_a = log δ_a / log(δ_a / (δ_a - 1))`, computed with `δ_a` from `(a + √(a² + 4))/2`. For `a = 1`: `δ_1 = φ = 1.6180…`, `δ_1 / (δ_1 - 1) = φ / (1/φ) = φ²`, `log(δ_1)/log(φ²) = log φ / (2 log φ) = 1/2` exactly. For `a = 2`: `δ_2 = 1 + √2 = 2.4142…`, `δ_2 - 1 = √2`, `δ_2 / (δ_2 - 1) = (1 + √2)/√2 = 1 + 1/√2 ≈ 1.7071`, `α_2 = log 2.4142 / log 1.7071 ≈ 0.88137 / 0.53480 = 1.6480`. For `a = 3, 4, 5, 6`: similar direct computation using `δ_a = (a + √(a²+4))/2`.

[^8]: `δ_a` satisfies `x² - a x - 1 = 0`, so its conjugate (the other root) is `δ_a' = a - δ_a = (a - √(a² + 4))/2`, and `N(δ_a) = δ_a · δ_a' = -1` (the constant term of the minimal polynomial with monic normalization, up to sign for degree 2). So `δ_a` is a unit in the ring of algebraic integers of `Q(√(a² + 4))`, and `N(1/δ_a) = 1/N(δ_a) = -1`.

[^9]: The norm argument: `1 - 1/δ_a = (δ_a - 1)/δ_a`. `N(δ_a - 1)`: substitute `y = δ_a - 1` into `δ_a² - a δ_a - 1 = 0` to get `(y + 1)² - a(y + 1) - 1 = y² + (2 - a) y + (1 - a - 1) = y² + (2 - a) y - a = 0`, so `δ_a - 1` satisfies `y² + (2 - a) y - a = 0` with constant term `-a`, hence `N(δ_a - 1) = -a`. Then `N((δ_a - 1)/δ_a) = -a / -1 = a`. The relation `(1 - 1/δ_a)^m = (1/δ_a)^n` on norms gives `a^m = (-1)^n`, i.e. `a^m = ±1`. For `a = 1`: any `m` works (with `n` accordingly), and a specific relation exists (`m = 1, n = 2`: `1 - 1/φ = 1/φ²`, verified above). For `a ≥ 2`: `a^m = ±1` forces `m = 0`, whence `n = 0` too - the trivial relation - so no rational `α = n/m` in lowest terms solves it. Then by Gelfond-Schneider on `α = log(1 - 1/δ_a) / log(1/δ_a)`, this ratio is either rational (excluded) or transcendental, so `α_a` is transcendental for `a ≥ 2`.

[^10]: `1/δ_3 = (√13 - 3)/2`; `r + r² = r(1 + r) = ((√13 - 3)/2) · ((√13 - 1)/2) = ((√13 - 3)(√13 - 1))/4 = (13 - √13 - 3√13 + 3)/4 = (16 - 4√13)/4 = 4 - √13`. So the equation is `(1 - r)^α = 4 - √13`, with `1 - r = 1 - (√13 - 3)/2 = (5 - √13)/2`. Norm computation in `Q(√13)`: `N((5 - √13)/2) = ((5-√13)/2) · ((5+√13)/2) = (25 - 13)/4 = 3`; `N(4 - √13) = (4 - √13)(4 + √13) = 16 - 13 = 3`. Rational `α = m/n` in lowest terms gives `3^m = 3^n`, i.e. `m = n`, then `(5 - √13)/2 = 4 - √13`, i.e. `5 - √13 = 8 - 2√13`, i.e. `√13 = 3`, false. So `α_3^{(2)}` (the bronze order in the Fibonacci-Pell family) is transcendental. Numerical: `α ≈ 2.579`.

[^11]: Discrete nabla Mittag-Leffler functions (cited, not read): Atici and Eloe (2009) "Discrete fractional calculus with the nabla operator," *Electronic Journal of Qualitative Theory of Differential Equations* Spec. Ed. I, No. 3, 1-12; Nagai (2003) "Discrete Mittag-Leffler function and its applications"; Podlubny (1999) Ch. 5. Multiple parameterizations exist; the generating-function shape `(1 - x)^{β - 1} / ((1 - x)^α - λ)` is the one the body compares with. The expansion of `1/((1 - x)^α - x)` and the residue constant `C` are own computation.
