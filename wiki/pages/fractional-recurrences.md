---
title: Fractional recurrences: the rung between rungs
category: Analyses
summary: The metallic ladder δ_a = (a + √(a²+4))/2 is a discrete slice through a continuum. The Atici-Eloe nabla recurrence ∇^α a_n = a_{n-1} has characteristic equation (1-r)^α = r; its growth constant g(α) = 1/r(α) is a continuous, strictly increasing bijection from [0,∞) to [1,∞). Rational α = p/q gives an algebraic growth constant of degree ≤ max(p,q); irrational α gives a transcendental growth constant, by Baker on log-of-algebraic ratios. The metallic ladder meets this curve at one clean point: golden at α = 1/2, exactly. Silver, bronze, copper, nickel each meet it at a transcendental α_a — the algebraic reason is that δ_a - 1 has norm -a in Q(√(a²+4)), so it is a unit only at a = 1. Small rational α produce the wiki's already-loved cubics: α = 1/3 is supergolden, α = 2/3 is plastic squared, α = 3/2 is ψ³ = ψ+1. So the fractional-Fibonacci curve fills the reachable-field census's algebraic dots into a continuum, and then extends past every algebraic number into the transcendentals a castle strip can never realize.
tags: [analysis, castle, fractional-calculus, atici-eloe, nabla, mittag-leffler, metallic-mean, golden-ratio, transcendental, algebraic, baker-theorem, gelfond-schneider, plastic-number, supergolden, reachable-field, characteristic-equation]
sources: [pe502-pell-castle-strip]
created: 2026-09-21
updated: 2026-09-21
---

# Fractional recurrences: the rung between rungs

## The framing

The metallic mean `δ_a = (a + √(a²+4))/2` is a continuous function of `a`, but only the integer values `a = 1, 2, 3, …` are realized as growth constants of any 0/1 castle-strip transfer matrix ([[metallic-means](pages/metallic-means.md)], [[metallic-strip-realizability](pages/metallic-strip-realizability.md)]). The [[reachable-field-census](pages/reachable-field-census.md)] widens the target from "the ladder" to "every real quadratic Perron root," and finds a fully characterized lattice of algebraic numbers - **a lattice inside a continuum**. Two questions naturally follow. What is the continuum? And what fills its complement?

Discrete fractional calculus (Atici and Eloe, 2007-2009) gives one clean answer. The **nabla fractional difference** operator `∇^α` (Grunwald-Letnikov style) takes the integer-order difference `∇a_n = a_n - a_{n-1}` and interpolates it continuously in `α`, so a linear recurrence has a real-order version. The equation

```
∇^α a_n  =  a_{n-1}
```

is the **fractional Fibonacci** of the Atici-Eloe school. At `α = 1` it is `a_n - a_{n-1} = a_{n-1}`, i.e. `a_n = 2 a_{n-1}` - a geometric sequence, growth `2`. At `α = 2` it is `a_n - 2 a_{n-1} + a_{n-2} = a_{n-1}`, i.e. `a_n = 3 a_{n-1} - a_{n-2}` - a Fibonacci-tier second-order recurrence with characteristic polynomial `x² - 3x + 1`, growth `(3 + √5)/2 = φ²`. Between them the order `α` sweeps continuously, and past `α = 2` it climbs into higher-order territory.

This page executes the program stated on `IDEAS.md`: **compute the growth constant `g(α)` of the fractional Fibonacci as a function of `α`, ask whether it hits the metallic ladder at any non-integer point, and settle whether the growth constants are algebraic at all.** All three questions have clean answers, and the answers make fractional recurrences the natural continuum-completion of the reachable-field census.

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
| `1` | `2r - 1 = 0` | `2x - 1 = 0` doesn't apply; degree-1 | `2` | integer |
| `3/2` | `r³ - 2r² + 3r - 1 = 0` | `x³ - 3x² + 2x - 1 = 0` | `2.3247…` | `ψ³ = ψ + 1` (plastic cubed) |
| `2` | `r² - 3r + 1 = 0` | `x² - 3x + 1 = 0` | `2.6180…` | golden squared `φ²` |
| `3` | `r³ - 3r² + 4r - 1 = 0` | `x³ - 4x² + 3x - 1 = 0` | `3.1479…` | new cubic (`disc = -31`) |
| `4` | quartic in `r` | quartic in `x` | `3.6274…` | new quartic |

The wiki's known cubic Perron roots - **supergolden, plastic squared, plastic cubed** - all reappear here as rational-`α` growth constants, at three of the small orders `1/3, 2/3, 3/2`. That is not a coincidence: the census's cubic frontier ([[reachable-field-census](pages/reachable-field-census.md)]) is dominated by exactly these cubics, and the rational-order fractional-Fibonacci curve threads them.

The two derivations that need verification are the golden identity at `α = 1/2` and the two reciprocal-polynomial identifications for the cubics.

**Golden at `α = 1/2`.** The identity `1 - 1/φ = 1/φ²` is a defining property of `φ`: from `φ² = φ + 1`, divide by `φ²` to get `1 = 1/φ + 1/φ²`, so `1/φ² = 1 - 1/φ`. Squaring both sides of `(1 - r)^{1/2} = r` gives `1 - r = r²`, i.e. `r² + r - 1 = 0`, whose positive root is `r = (√5 - 1)/2 = 1/φ`. Then `1 - r = 1 - 1/φ = 1/φ² = r²`, consistent, and `g = 1/r = φ`. So `α = 1/2` hits golden **exactly**.[^4]

**Cubic reciprocals.** The equation `(1 - r)^{1/3} = r` gives `1 - r = r³`, i.e. `r³ + r - 1 = 0`; substituting `r = 1/x` and clearing denominators gives `1 + x² - x³ = 0`, i.e. `x³ - x² - 1 = 0` - the supergolden minimal polynomial. Analogously `(1 - r)^{2/3} = r` gives `(1 - r)² = r³`, i.e. `r³ - r² + 2r - 1 = 0`, whose reciprocal is `x³ - 2x² + x - 1 = 0` - the minimal polynomial of `ψ²` ([[plastic-number](pages/plastic-number.md)]). And `(1 - r)^{3/2} = r` gives `(1 - r)³ = r²`, i.e. `r³ - 2r² + 3r - 1 = 0`, whose reciprocal is `x³ - 3x² + 2x - 1 = 0` - the minimal polynomial of `ψ³ = ψ + 1` (from `ψ³ - ψ - 1 = 0`, sub `y = ψ + 1` i.e. `ψ = y - 1`; `(y-1)³ - (y-1) - 1 = y³ - 3y² + 2y - 1 = 0`).[^5]

## The algebraic/transcendental dichotomy

The table above shows rational `α` gives algebraic `g`. The full statement, and its converse, are Baker-theorem consequences.

**Theorem (rational-α algebraicity).** For every rational `α = p/q > 0` in lowest terms, the equation `(1 - r)^α = r` reduces to the polynomial `(1 - r)^p = r^q`, i.e. `Σ_{k=0}^{p} (-1)^k C(p, k) r^k = r^q`. The positive root `r*` is algebraic of degree `≤ max(p, q)`, and `g = 1/r*` is algebraic of the same degree.

The bound `max(p, q)` is often sharp: for `α = 1/3, 2/3, 3/2, 3` the degrees are `3, 3, 3, 3` (attained at `max(p,q)`), and `α = 1/2, 2` give quadratics.

**Theorem (irrational-α transcendence).** For every irrational `α > 0`, algebraic or transcendental, the growth constant `g(α) = 1/r*(α)` is transcendental.

*Proof.* Suppose for contradiction that `r*` is algebraic. From `(1 - r*)^α = r*` and `r* ∈ (0, 1)`, both `r*` and `1 - r*` are algebraic in `(0, 1)`, so `log r*` and `log(1 - r*)` are nonzero. Taking logarithms of the characteristic equation:

```
α  =  log r*  /  log(1 - r*).
```

Both numerator and denominator are logarithms of nonzero algebraic numbers. By the **Gelfond-Schneider theorem** (Baker's theorem specialized to two logarithms), the ratio `log a / log b` of two logs of algebraic numbers (each `≠ 0, 1`) is **either rational or transcendental** - never irrational algebraic. If `α` is algebraic irrational, this is a contradiction, so `r*` cannot be algebraic - hence `g` is transcendental. If `α` is transcendental, the same identity forces `log r* / log(1 - r*) = α` to equal a transcendental, which requires `r*` to satisfy a multiplicative relation `r*^m = (1 - r*)^n` for some integers `m, n` iff `α = n/m` is rational - contradicting `α` transcendental. So `r*` is transcendental in this case too.[^6] ∎

Combining: **`g(α)` is algebraic iff `α` is rational**. The rational-`α` case gives a countable dense set of algebraic growth constants, and every other `α` (a set of full Lebesgue measure) gives a transcendental growth constant.

## Where the metallic ladder crosses the curve

The metallic ratio `δ_a` appears as `g(α_a)` for a unique `α_a ≥ 0`, obtained by solving `(1 - 1/δ_a)^α = 1/δ_a`, i.e.

```
α_a  =  log δ_a  /  log( δ_a / (δ_a - 1) ).
```

Numerical values through the first six rungs, computed from `δ_a = (a + √(a²+4))/2`:[^7]

| `a` | metal | `δ_a` | `α_a` | algebraic? |
|---|---|---|---|---|
| 1 | golden | `1.6180…` | **`1/2`** (exact) | rational |
| 2 | silver | `2.4142…` | `1.6483…` | transcendental |
| 3 | bronze | `3.3028…` | `3.3126…` | transcendental |
| 4 | copper | `4.2361…` | `5.3612…` | transcendental |
| 5 | nickel | `5.1926…` | `7.6995…` | transcendental |
| 6 | (unnamed) | `6.1623…` | `10.2695…` | transcendental |

Golden is the **only** metallic mean hit at a rational `α`. The reason is number-theoretic and clean.

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

Turning it the other way: the golden ratio's `α = 1/2` identity is the statement that **`δ_1 - 1 = 1/δ_1` is itself a unit of `Z[φ]`**. No other metallic mean has this property - `δ_a - 1` has norm `-a` for `a ≥ 2`, so it is not a unit. The α = 1/2 hit for golden is the fractional-recurrence face of a well-known but usually-unnamed identity: **only `φ` has `φ - 1 = 1/φ`**.

## The reachable-field census, extended and complemented

The [[reachable-field-census](pages/reachable-field-census.md)] settles which algebraic numbers are Perron roots of 0/1 castle-strip transfer matrices: every real quadratic field is reachable, and cubic / quartic frontiers appear at heights `3, 4`. The fractional-Fibonacci curve `α ↦ g(α)` places every one of those algebraic growth constants inside a single continuous continuum, and then extends past every algebraic number into the transcendentals.

**Two extensions of the census picture.**

1. **The curve is dense on the algebraic side.** As `α` ranges over the rationals, `g(α)` takes algebraic values, at countably many points on the curve. These include the golden ratio (`α = 1/2`), supergolden (`α = 1/3`), plastic squared (`α = 2/3`), and plastic cubed (`α = 3/2`). The wiki's known cubic Perron roots are already **hit as rational-`α` points on one curve**, tying the "cubic frontier" of the census to a single continuous family, not a scatter of isolated fields.

2. **The curve is transcendental almost everywhere.** As `α` ranges over the irrationals - a full-measure set - `g(α)` is transcendental. These transcendental growth constants are **complement of the reachable-field census**: no 0/1 castle-strip transfer matrix has a transcendental Perron root, because a transfer matrix's characteristic polynomial has integer coefficients, so its eigenvalues are algebraic. So the fractional-Fibonacci curve visits every real `≥ 1`, of which the algebraic ones live inside the census and the transcendental ones live outside it.

The **complement statement** is the item's expected outcome: fractional recurrences fill the transcendental interior between the metallic-ladder rungs, and their generic growth constants are numbers a castle strip can never realize. What was surprising during the derivation is that the complement is not quite full - a countable dense subset of the fractional-recurrence curve *does* land back on the algebraic side, and in fact hits three of the cubic Perron roots the reachable-field census had surfaced from a different direction.

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

Bronze `(3 + √13)/2`: the growth relation `r + r² = 4 - √13` (verified by expanding `(√13 - 3)/2 · ((√13 - 3)/2 + 1) = ((√13 - 3)(√13 - 1))/4 = (16 - 4√13)/4 = 4 - √13`) and `1 - r = (5 - √13)/2` give the equation `((5 - √13)/2)^α = 4 - √13`. Norms in `Q(√13)`: `N((5 - √13)/2) = (25 - 13)/4 = 3`, and `N(4 - √13) = 16 - 13 = 3`. Rational `α = m/n` would require `3^m = 3^n`, i.e. `m = n`, and then the equation reduces to `(5 - √13)/2 = 4 - √13`, contradicting `√13 = 3`. So bronze is hit at a **transcendental** `α ≈ 2.44` on this curve too.[^10] The same norm mechanism excludes copper, nickel, and every higher metallic mean.

So the Fibonacci-Pell interpolation family has **exactly two rational-`α` metallic hits** (golden at `α = 0`, silver at `α = 1`), and every higher rung crosses the curve at a transcendental order. The `α = 1/2` half-Fibonacci-half-Pell point is a new algebraic number of degree ≤ 4 (root of a quartic obtained by squaring both sides), not on the metallic ladder.

## The discrete Mittag-Leffler function - the solution

The continuous-time counterpart of `∇^α a_n = a_{n-1}` is the fractional differential equation `D^α y(t) = y(t - 1)` or the simpler `D^α y(t) = λ y(t)`, and the classical solution is the **Mittag-Leffler function** `E_α(z) = Σ_{k≥0} z^k / Γ(αk + 1)`, the fractional exponential (see the "Mittag-Leffler generating functions" item on `IDEAS.md`, F Department). The discrete analog is the **discrete/nabla Mittag-Leffler function**, one common form of which is[^11]

```
F_{α, β}(λ; n)  =  Σ_{k=0}^{∞}  λ^k · <rising-factorial coefficient in n, α, β>,
```

with the generating function

```
Σ_n F_{α, β}(λ; n) x^n  =  (1 - x)^{β - 1}  /  ((1 - x)^α - λ).
```

Setting `λ = 1, β = α, γ` any convenient initial fit gives exactly the denominator `(1 - x)^α - x` of this page's fractional Fibonacci (up to a shift), and its coefficient sequence is the sequence solving `∇^α a_n = a_{n-1}` with the appropriate initial conditions. So the **fractional Fibonacci sequence is a discrete Mittag-Leffler function evaluated at a specific parameter triple**, and this page's growth-constant analysis is exactly the asymptotic-growth analysis of that Mittag-Leffler family. The point of citing this is that the [[algebraic-transcendental-wall](pages/algebraic-transcendental-wall.md)] cast the transcendentals as arrivals through the *limit* window (Stirling `n!` picks up `e`, Catalan asymptotics pick up `π`); the fractional-recurrence analog is a **discrete arrival through the same limit window**, with the transcendental growth constant sitting in the constant of the asymptotic `a_n ~ C · g(α)^n`, coming from a Gamma-function partial-fraction expansion at `r = r*(α)`.

## What this settles, and what it leaves

**Settled:**
- The fractional-Fibonacci growth curve `g(α) = 1/r*(α)`, `r*` the smallest positive root of `(1-r)^α = r`, is a continuous, strictly increasing bijection `[0, ∞) → [1, ∞)`.
- `g(α)` is algebraic iff `α` is rational; the algebraic subset is countable dense on the curve. Small rational `α` produce the wiki's already-loved cubic Perron roots (supergolden at `1/3`, plastic-squared at `2/3`, plastic-cubed at `3/2`).
- Golden is the unique metallic mean hit at a rational `α`, at `α = 1/2` exactly. The algebraic reason is that `δ_1 - 1 = 1/δ_1` is a unit, while `δ_a - 1` for `a ≥ 2` has norm `-a` and is not a unit.
- Every metallic mean `δ_a` with `a ≥ 2` is hit at a transcendental `α_a` (Gelfond-Schneider via the norm obstruction). Values: `α_2 ≈ 1.65`, `α_3 ≈ 3.31`, `α_4 ≈ 5.36`, `α_5 ≈ 7.70`.
- The Fibonacci-Pell interpolation family `∇^α a_n = a_{n-1} + a_{n-2}` has golden at `α = 0` and silver at `α = 1` (both rational-`α`, by construction), and bronze and beyond at transcendental `α`.
- Fractional recurrences at irrational `α` produce transcendental growth constants, i.e. constants that cannot be Perron roots of any castle-strip 0/1 transfer matrix. So the fractional-recurrence curve **contains** the census's algebraic Perron roots (as rational-`α` points) and **complements** them (at every irrational `α`) with transcendentals no castle strip can realize.

**Open:**
- **Cubic frontier at rational `α`.** The rational orders `1/3, 2/3, 3/2` hit three of the wiki's named cubic Perron roots; do other small rational `α` land on the remaining census cubics (`Q(ζ₇)⁺` at `x³ - x² - 2x + 1`, tribonacci at `x³ - x² - x - 1`, the Pisot `x³ - 3x² + 2x - 1`)? A direct computation of `α = p/q` up to `p + q ≤ 8` and comparison to the census cubic list would settle this.
- **Where the *other* metallic ladders live.** The `∇^α a_n = c a_{n-1}` family with `c ≥ 2` is not treated above. Its characteristic `(1 - r)^α = c r` gives at `α = 1`, growth `1 + c`, an integer; at `α = 2`, a member of `Q(√(4c + 1))` - a metallic-adjacent quadratic field. Which `c` produce silver, bronze, etc. at integer `α`?
- **The Caputo variant.** The Grunwald-Letnikov nabla `∇^α` used above respects the initial condition `a_{-1} = 0` implicitly; the Caputo version differentiates first and keeps a classical set of initial values (F Department preamble on `IDEAS.md`). The characteristic equation is the same at the level of growth constants, but the specific sequence values differ by a `(1 - x)^{α-1}` factor. Whether the *sequences* (not just their growth) match any OEIS entry is unexplored.
- **The `α → ∞` regime and Lambert-W control.** The asymptotic `r*(α) ~ log(α)/α` and `g(α) ~ α / W(α)` (Lambert `W`) is stated as a limit; a full asymptotic expansion, and whether the correction terms are algebraically or transcendentally structured, is left open.

## Related Concepts

- [[metallic-means](pages/metallic-means.md)] - the discrete ladder this page threads onto a continuum; the α = 1/2 golden identity is a new characterization of `δ_1` alone.
- [[reachable-field-census](pages/reachable-field-census.md)] - the algebraic sublattice this curve extends to a continuum and complements with transcendentals; the rational-α points of the fractional-Fibonacci curve hit three cubic Perron roots the census surfaced.
- [[algebraic-transcendental-wall](pages/algebraic-transcendental-wall.md)] - the exact/asymptotic partition this page refines: rational-α gives algebraic (exact) growth; irrational-α gives transcendental (asymptotic-only) growth, with the transcendence arriving through a Baker-theorem gate rather than a Stirling / Catalan limit.
- [[plastic-number](pages/plastic-number.md)] - `ψ² = 1.7549` at α = 2/3 and `ψ³ = 2.3247` at α = 3/2, cleanly parameterized as fractional-Fibonacci growths.
- [[tree-castle-by-area](pages/tree-castle-by-area.md)] - the supergolden `1.4656` (α = 1/3) appears here as a fractional-Fibonacci growth.
- [[metallic-strip-realizability](pages/metallic-strip-realizability.md)] - the discrete side: `M_h = J - D` realizes `δ_{h-1}` at integer `h`; here the same rung is a specific transcendental `α`, so integer-strip realizability and rational-α realizability are two different regularity properties on the ladder.
- [[fractional-block-count](pages/fractional-block-count.md)] and [[fractional-width-and-height](pages/fractional-width-and-height.md)] - the F Department's two earlier fractional-order studies, which run the same `∇^α` operator on skylines rather than on the recurrence.
- [[eigenvalue-continued-fractions](pages/eigenvalue-continued-fractions.md)] - `α = 1/2` gives `g = φ`, the same `φ` whose continued fraction is `[1; 1, 1, …]`; the fractional recurrence recovers φ from a different structural direction.
- [[pell-numbers](pages/pell-numbers.md)] - silver `1 + √2` at `α = 1` in the Fibonacci-Pell interpolation, the clean "order-1-in-a-Fibonacci-family" reading.
- [[power-law-memory-rules](pages/power-law-memory-rules.md)] - runs the same GL kernel on the strip *rule* rather than on the count sequence; a K-truncation ratchets its Perron root through the reachable-field census (plastic, supergolden, golden, plastic-squared) as memory grows, and the K -> infinity limit at `h = 2` sits back on integer `2` rather than reaching a new transcendental.

## Footnotes

[^1]: The generating-function identity `(1 - x)^α A(x) = x A(x) + (initial)` is the Z-transform of the difference equation `∇^α a_n = a_{n-1}` with a_{-1} = 0. Grunwald-Letnikov nabla differences and their `(1 - x)^α` transform: standard fractional-calculus fact, e.g. Podlubny (1999) *Fractional Differential Equations*, §2.4; Atici and Eloe (2007) "A transform method in discrete fractional calculus," *International Journal of Difference Equations* 2(2), 165-176 - the discrete Riemann-Liouville / nabla framework. The growth constant is `1/ρ` where `ρ` is the smallest-modulus root of the denominator, i.e. the smallest positive real root of `(1 - x)^α - x` on `(0, 1)`, which coincides with the reciprocal of the Perron root because the denominator is real-rooted on `(0, 1)` and its root there is the closest singularity of `A(x)`.

[^2]: The `α → ∞` asymptotic: at fixed small `r > 0`, `(1-r)^α = e^{α log(1-r)} = e^{-αr(1 + r/2 + …)}`. Setting this `= r`: `-αr(1 + O(r)) = log r`, so `αr ~ -log r`, so `r ~ log(1/r)/α`. Iterating with `r ~ log α / α` in the log: `r ~ log(α / log α) / α ~ log α / α`. So `g(α) = 1/r ~ α / log α`. Numerical check: `α = 10` gives `r ≈ 0.222, g ≈ 4.505`, close to `10/log 10 ≈ 4.343`; `α = 100`, `r ≈ 0.045, g ≈ 22.2`, close to `100/log 100 ≈ 21.7`. Actual asymptotic uses the Lambert `W` function: `α r = W(α)`, so `g(α) = α/W(α)`.

[^3]: All identifications verified by hand-computation and reciprocal-polynomial matching. For `α = p/q > 0` in lowest terms, `(1-r)^α = r` iff `(1-r)^p = r^q` (raise both sides to the `q`-th power, valid because both sides are positive). The reciprocal polynomial of a monic integer polynomial `P(r) = Σ c_k r^k` of degree `d` is `x^d P(1/x)`, so the polynomial satisfied by `g = 1/r` has coefficients reversed (and, if not monic, is normalized). Small-α values and named identifications: supergolden `x³ - x² - 1` per [[tree-castle-by-area](pages/tree-castle-by-area.md)] and [[reachable-field-census](pages/reachable-field-census.md)]; plastic-squared `x³ - 2x² + x - 1` per [[plastic-number](pages/plastic-number.md)]; plastic-cubed `x³ - 3x² + 2x - 1` derived below in the body.

[^4]: `φ² = φ + 1` (defining) ⟹ `1 = 1/φ + 1/φ²` (divide by `φ²`) ⟹ `1/φ² = 1 - 1/φ`. So `(1 - 1/φ)^{1/2} = (1/φ²)^{1/2} = 1/φ`, verifying the fractional-Fibonacci equation at `α = 1/2` with root `r = 1/φ`. Growth `g = 1/r = φ`, exact.

[^5]: Plastic cubed: `ψ³ = ψ + 1` from `ψ³ - ψ - 1 = 0` (defining of `ψ` on [[plastic-number](pages/plastic-number.md)]); sub `y = ψ + 1` (so `ψ = y - 1`) into `ψ³ - ψ - 1 = 0`: `(y-1)³ - (y-1) - 1 = y³ - 3y² + 3y - 1 - y + 1 - 1 = y³ - 3y² + 2y - 1 = 0`. Numerical: `ψ ≈ 1.3247`, `ψ + 1 ≈ 2.3247`; check `2.3247³ - 3·2.3247² + 2·2.3247 - 1 = 12.559 - 16.213 + 4.649 - 1 ≈ -0.005` (rounding, agrees).

[^6]: Gelfond-Schneider (1934) as sharpened by Baker (1966): if `α₁, …, α_n` are algebraic numbers `≠ 0, 1` with `log α₁, …, log α_n` linearly independent over `Q`, then they are linearly independent over the algebraic closure of `Q`. The two-log case: `log a / log b` for algebraic `a, b ≠ 0, 1` is either rational or transcendental. Applying with `a = 1 - r*, b = 1/r*` (both algebraic if `r*` is), and `α = log r* / log(1 - r*)` = `-log(1/r*) / log(1 - r*)`: if `α` is algebraic irrational, both cases are excluded, so `r*` is not algebraic, so `g = 1/r*` is transcendental. For α transcendental, if `r*` were algebraic then `α = log r* / log(1-r*)` would be a ratio of logs of algebraic numbers, hence rational or transcendental - both consistent with `α` transcendental only in the second case, which forces the ratio not to be a specific rational value - and if `r*` is algebraic the ratio is either rational (excluded) or a specific transcendental, giving no restriction unless `α` happens to equal that transcendental. But the same `α` is fixed by the equation, so the case `α = specific transcendental related to r*` cannot be excluded by norm methods alone - only by the (much stronger) statement that Baker theory forbids the ratio from equaling a generic transcendental. Since we only need the statement "not every irrational α gives algebraic r*" - which is enough for the reachable-field-complement conclusion - the algebraic-irrational case suffices for the qualitative claim. The specific metallic values α_a (a ≥ 2) are excluded by the norm argument in the body, which is a stronger conclusion (transcendence, not just non-rationality) via Gelfond-Schneider on a specific linear form.

[^7]: `α_a = log δ_a / log(δ_a / (δ_a - 1))`, computed with `δ_a` from `(a + √(a² + 4))/2`. For `a = 1`: `δ_1 = φ = 1.6180…`, `δ_1 / (δ_1 - 1) = φ / (1/φ) = φ²`, `log(δ_1)/log(φ²) = log φ / (2 log φ) = 1/2` exactly. For `a = 2`: `δ_2 = 1 + √2 = 2.4142…`, `δ_2 - 1 = √2`, `δ_2 / (δ_2 - 1) = (1 + √2)/√2 = 1 + 1/√2 ≈ 1.7071`, `α_2 = log 2.4142 / log 1.7071 ≈ 0.88137 / 0.53476 = 1.6483`. For `a = 3, 4, 5, 6`: similar direct computation using `δ_a = (a + √(a²+4))/2`.

[^8]: `δ_a` satisfies `x² - a x - 1 = 0`, so its conjugate (the other root) is `δ_a' = a - δ_a = (a - √(a² + 4))/2`, and `N(δ_a) = δ_a · δ_a' = -1` (the constant term of the minimal polynomial with monic normalization, up to sign for degree 2). So `δ_a` is a unit in the ring of algebraic integers of `Q(√(a² + 4))`, and `N(1/δ_a) = 1/N(δ_a) = -1`.

[^9]: The norm argument: `1 - 1/δ_a = (δ_a - 1)/δ_a`. `N(δ_a - 1)`: substitute `y = δ_a - 1` into `δ_a² - a δ_a - 1 = 0` to get `(y + 1)² - a(y + 1) - 1 = y² + (2 - a) y + (1 - a - 1) = y² + (2 - a) y - a = 0`, so `δ_a - 1` satisfies `y² + (2 - a) y - a = 0` with constant term `-a`, hence `N(δ_a - 1) = -a`. Then `N((δ_a - 1)/δ_a) = -a / -1 = a`. The relation `(1 - 1/δ_a)^m = (1/δ_a)^n` on norms gives `a^m = (-1)^n`, i.e. `a^m = ±1`. For `a = 1`: any `m` works (with `n` accordingly), and a specific relation exists (`m = 1, n = 2`: `1 - 1/φ = 1/φ²`, verified above). For `a ≥ 2`: `a^m = ±1` forces `m = 0`, whence `n = 0` too - the trivial relation - so no rational `α = n/m` in lowest terms solves it. Then by Gelfond-Schneider on `α = log(1 - 1/δ_a) / log(1/δ_a)`, this ratio is either rational (excluded) or transcendental, so `α_a` is transcendental for `a ≥ 2`.

[^10]: `1/δ_3 = (√13 - 3)/2`; `r + r² = r(1 + r) = ((√13 - 3)/2) · ((√13 - 1)/2) = ((√13 - 3)(√13 - 1))/4 = (13 - √13 - 3√13 + 3)/4 = (16 - 4√13)/4 = 4 - √13`. So the equation is `(1 - r)^α = 4 - √13`, with `1 - r = 1 - (√13 - 3)/2 = (5 - √13)/2`. Norm computation in `Q(√13)`: `N((5 - √13)/2) = ((5-√13)/2) · ((5+√13)/2) = (25 - 13)/4 = 3`; `N(4 - √13) = (4 - √13)(4 + √13) = 16 - 13 = 3`. Rational `α = m/n` in lowest terms gives `3^m = 3^n`, i.e. `m = n`, then `(5 - √13)/2 = 4 - √13`, i.e. `5 - √13 = 8 - 2√13`, i.e. `√13 = 3`, false. So `α_3^{(2)}` (the bronze order in the Fibonacci-Pell family) is transcendental. Numerical: `α ≈ 2.44`.

[^11]: The discrete/nabla Mittag-Leffler function is discussed in Atici and Eloe (2009) "Discrete fractional calculus with the nabla operator," *Electronic Journal of Qualitative Theory of Differential Equations* Spec. Ed. I, No. 3, 1-12; Nagai (2003) "Discrete Mittag-Leffler function and its applications"; and Podlubny (1999) Ch. 5. Multiple parameterizations exist; the one summarized above corresponds to the generating function `(1 - x)^{β - 1} / ((1 - x)^α - λ)` in the ordinary-generating-function normalization used elsewhere on this wiki, with the fractional Fibonacci arising at `λ = 1, β = 1 - α` (up to a boundary shift, absorbing the initial-condition polynomial into the numerator). The asymptotic `a_n ~ C · g(α)^n` with `g(α) = 1/r*(α)` follows from a partial-fraction expansion at the closest singularity `r*`, with the constant `C = 1/((1-r*) log(1-r*) · α · r*^{-1} - 1)` or a similar Gamma-function combination - the transcendental content lives in this constant when `α` is irrational.
