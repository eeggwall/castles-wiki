---
title: Eigenvalue continued fractions
category: Concepts
summary: Continued fractions of castle eigenvalues, taught from "what is a continued fraction": periodic exactly for quadratic irrationals (Lagrange), purely periodic exactly for reduced ones (Galois), which for a quadratic unit means norm −1, as for the castle's φ and √2+1. The self-reciprocal k-direction characteristic polynomials have only the roots ±1; the L-direction roots of degree 3 and up have non-periodic continued fractions; plus the mod-p counterpart.
tags: [concept, castle, continued-fraction, eigenvalue, characteristic-polynomial, palindromic, lagrange, galois, quadratic, fibonacci, mod-p, pedagogy]
sources: [project-euler-502-representations, oeis-mining-pe502]
created: 2026-09-15
updated: 2026-10-04
---

# Eigenvalue continued fractions

## Summary

The castle's counts obey linear recurrences, and every linear recurrence has a **characteristic polynomial** whose roots are its **eigenvalues**. A real eigenvalue has a continued fraction, and whether it repeats depends on the eigenvalue's degree (Lagrange) and, for a quadratic, on where its conjugate lies (Galois). For a quadratic unit the conjugate is placed by the sign of the norm, which is the constant term of a palindromic (`+1`) or anti-palindromic (`−1`) quadratic.

The page builds up in three parts:

1. **What a continued fraction is** — and why `φ = 1 + 1/(1 + 1/(1 + …))` is the canonical example.
2. **Why "periodic" and "quadratic" are synonyms** — Lagrange's theorem, and the sharper "purely periodic = reduced" (Galois).
3. **Where the castle's eigenvalues land** — the two real quadratics that arise, and the higher-degree case, where the simple continued fraction does not repeat.

## Step 1 — What a continued fraction is

A **continued fraction** is a staircase of reciprocals,

```
[a₀; a₁, a₂, …]  =  a₀ + 1/( a₁ + 1/( a₂ + 1/( … ) ) ),
```

and any real number has one, computed by the Euclidean algorithm: take the integer part, subtract it, invert, repeat. The simplest case is a number that reproduces itself after one step. The **golden ratio** `φ = (1+√5)/2 ≈ 1.618` satisfies[^2]

```
φ − 1 = 1/φ,    so    φ = 1 + 1/φ.
```

Because the remainder `1/φ` is *the same φ again*, the process never changes: `φ = [1; 1, 1, 1, …]`. A periodic continued fraction is one where the algorithm returns to an earlier remainder.

**Convergents.** Truncating gives the best rational approximations. For `φ` each truncation is a ratio of consecutive Fibonacci numbers (the recurrence `p_n = a_n p_{n−1} + p_{n−2}` with every `a_n = 1` *is* the Fibonacci recurrence):[^2]

| truncation | `[1]` | `[1;1]` | `[1;1,1]` | `[1;1,1,1]` | `[1;1,1,1,1]` |
|---|---|---|---|---|---|
| value | `1` | `2` | `3/2` | `5/3` | `8/5` |

converging to `φ` as `F_{n+1}/F_n`. (Run the same game starting from `x = 2 + 1/x` and you get `√2 + 1 = [2; 2, 2, 2, …]` — the tower-word growth constant, below.)

## Step 2 — Periodic means quadratic (Lagrange)

A continued fraction is **periodic** when the same block of digits repeats forever. The governing theorem is due to Lagrange:[^3]

> A real number has an eventually periodic continued fraction **if and only if** it is a quadratic irrational (a root of `ax² + bx + c = 0` with integer coefficients).

The easy direction is the self-similarity above: if `φ = 1 + 1/φ`, then `φ` is a root of `x² − x − 1 = 0`, a **quadratic**, and in general a repeating block gives a quadratic equation for the number. The converse, that every quadratic irrational has a repeating fraction, is Lagrange's contribution.

The simplest periodic fraction is the **period-one** case. The equation `x = a + 1/x` is `x² − ax − 1 = 0`, so

```
[a; a, a, a, …]  =  (a + √(a² + 4)) / 2,
```

a quadratic of **trace `a`, norm −1** (the constant term `−1` is the product of the two roots). `a = 1` gives `φ`; `a = 2` gives `√2 + 1`.

## Step 3 — Purely periodic means reduced (Galois)

Look closer and there are two kinds of periodic fraction. `φ = [1; 1, 1, …]` repeats from the very first digit — **purely** periodic. The number `(3+√5)/2 = φ² ≈ 2.618` is `[2; 1, 1, 1, …]`: a one-digit head `[2;]` before the repeating `[1]`.[^6] What is the difference? It is visible in the *other* root (the **conjugate**):

```
φ         = [1; 1, 1, …]   conjugate 1−φ = −0.618 ∈ (−1, 0)      purely periodic
(3+√5)/2  = [2; 1, 1, …]   conjugate (3−√5)/2 = 0.382 ∉ (−1, 0)   has a head
```

Galois' theorem:[^3]

> A quadratic surd `α` is **purely** periodic if and only if it is **reduced**: `α > 1` and its conjugate lies in `(−1, 0)`.

For a quadratic unit `x² − s·x + c` with `c = ±1`, the constant term `c` is the product of the roots, so it decides where the conjugate lies:

- **`c = +1`** — roots `r` and `1/r` (reciprocals). This is the **palindromic** quadratic (`x² − s·x + 1`), and `r` is *not* reduced (`1/r ∈ (0,1)`), so its fraction has a head: `(3+√5)/2 = [2; 1, 1, …]`.
- **`c = −1`** — roots `r` and `−1/r`. For `r > 1` the conjugate `−1/r` sits in `(−1, 0)` automatically, so `r` **is** reduced, hence **purely** periodic: `φ = [1;1,1,…]`, `√2+1 = [2;2,2,…]`.

So norm `−1` (constant term `−1`) guarantees pure periodicity.

## Step 4 — Palindromic polynomials: roots in reciprocal pairs

A polynomial `p(x) = a_d x^d + … + a_0` is **palindromic** when its coefficients read the same backwards, `a_i = a_{d−i}`, and **anti-palindromic** when they read backwards with a sign flip, `a_i = −a_{d−i}`. The test is mechanical — for `x² − 3x + 1` the coefficients `[1, −3, 1]` are symmetric, so it is palindromic, and indeed its roots `(3±√5)/2` multiply to `1`, i.e. are reciprocals. The general fact:[^1]

```
palindromic       ⟺  p(x) =  x^d · p(1/x)   ⟺  roots closed under  r ↦  1/r
anti-palindromic  ⟺  p(x) = −x^d · p(1/x)   ⟺  roots closed under  r ↦ −1/r
```

For a quadratic this is Step 3's `c = ±1` condition. At higher degree the reciprocal pairing of roots can still hold, but whether a root's continued fraction repeats depends only on whether that root is quadratic (Lagrange), not on the pairing.

## Step 5 — The castle's eigenvalues

The signed tower count `P(k,L)` ([[signed-tower-count](pages/signed-tower-count.md)]) is C-finite in both directions, and its two characteristic-polynomial families behave differently.

**The k-direction is self-reciprocal - and the symmetry turns out to be trivial.** For fixed `L`, the sequence `P(·,L)` has order `2L−2` (for `L ≥ 4`), and its characteristic polynomial is palindromic for even `L`, anti-palindromic for odd `L` ([[closed-form-hunting](pages/closed-form-hunting.md)]):[^1]

```
L=4: [1, 2, −1, −4, −1, 2, 1]                  = (x+1)⁴ (x−1)²
L=5: [1, 2, −2, −6, 0, 6, 2, −2, −1]           = (x+1)⁵ (x−1)³
L=6: [1, 2, −3, −8, 2, 12, 2, −8, −3, 2, 1]    = (x+1)⁶ (x−1)⁴
```

By the factorizations, **every k-direction eigenvalue is `+1` or `−1`.** The polynomial is `(x+1)^L (x−1)^{L−2}` for every `L` from 4 to 12 checked ([[signed-tower-k-direction](pages/signed-tower-k-direction.md)]), so the roots are `±1`, each its own reciprocal, and `P(k,L)` is a **quasi-polynomial** in `k` - `(−1)^k A_L(k) + B_L(k)` with polynomials `A_L, B_L` - not an exponential sum with irrational bases. The palindromic symmetry comes entirely from "`x+1` is palindromic, `x−1` is anti-palindromic, and the multiplicities are `L` and `L−2`." Irrational eigenvalues live in the other direction (below).

**Two real quadratic constants.** The real quadratic constants on the castle side, `φ` and `√2 + 1`, come from other counts; both are norm-−1 reduced surds of period one:[^4]

- `φ = (1+√5)/2 = [1; 1, 1, …]`, root of `x² − x − 1` — Fibonacci's growth rate (`F_n = (φ^n − φ̂^n)/√5`, [[aocp-generating-functions](pages/aocp-generating-functions.md)]) and the `2^{n−1} − F_{n−1}` of prime-castle counting ([[castle-by-area](pages/castle-by-area.md)]).
- `√2 + 1 = [2; 2, 2, …]`, root of `x² − 2x − 1` — the tower-word growth constant from [[tower-word-continued-fraction](pages/tower-word-continued-fraction.md)]. The integer sequence that realizes this surd via its Binet form is the [[pell-numbers](pages/pell-numbers.md)] (`P⋆_n = 2P⋆_{n−1} + P⋆_{n−2}`, OEIS A000129), whose convergents `P⋆_{n+1}/P⋆_n = 2, 5/2, 12/5, 29/12, 70/29, 169/70, …` are the continued-fraction truncations of `1 + √2`; the anchored 1-smooth height-3 strip on [[pell-castle-strip](pages/pell-castle-strip.md)] is a castle-strip realization with exactly these counts.

Both are the fundamental units of their quadratic fields (`φ` of `Q(√5)`, `√2+1` of `Q(√2)`).

**The metallic means.** `φ` and `√2 + 1` are the first two members of the [[metallic-means](pages/metallic-means.md)] family `δ_a = (a + √(a²+4))/2` for `a = 1, 2, 3, …`, each the positive root of `x² − a·x − 1 = 0` and each a norm-`−1` reduced surd with purely periodic continued fraction `[a; a, a, …]` — the same argument, one parameter substituted. The name is standard (de Spinadel 1997); on the wiki:

| `a` | `δ_a = [a; a, a, …]` | Name | Integer sequence | Castle appearance |
|---|---|---|---|---|
| 1 | `(1+√5)/2 ≈ 1.618` | Golden | Fibonacci A000045 | `2^{n−1} − F_{n−1}` in prime-castle count ([[castle-by-area](pages/castle-by-area.md)]) |
| 2 | `1+√2 ≈ 2.414` | Silver | Pell A000129 ([[pell-numbers](pages/pell-numbers.md)]) | tower-word growth constant; the anchored 1-smooth strip of [[pell-castle-strip](pages/pell-castle-strip.md)] |
| 3, 4, 5, … | Bronze, Copper, Nickel, … | | | the ridge castles (ridge rule `R_h = J − D`) at heights 4, 5, 6, … ([[castle-classification-growth](pages/castle-classification-growth.md)]) |

Every castle class whose count sequence has growth constant `δ_a` for some `a ≥ 1` is a **`<metal>` `<axis>` growth castle** (Axis 8 of [[castle-classification-growth](pages/castle-classification-growth.md)]) — a meta-classification on castle *classes* (not on individual castles) whose naming convention `<metal>` ∈ {golden, silver, bronze, copper, …} and `<axis>` ∈ {width, vertical, area, block} is developed there.

**Higher degree.** The k-direction roots are `±1`: rational numbers have *terminating* continued fractions, so there is nothing there to approximate. The castle's higher-degree eigenvalues are the **L-direction** roots of `char_k` on [[generating-function-gallery](pages/generating-function-gallery.md)]: `char_k` has degree `k+1` and root product `2^k`, so it is not self-reciprocal and its roots are not units. A real root of degree 3 or more (the dominant root of `char_4` is already a cubic) has a non-periodic simple continued fraction by Lagrange, and the replacement for "period" is the multidimensional Jacobi–Perron expansion. The [[castle-eigenvalue-oeis-crosswalk](pages/castle-eigenvalue-oeis-crosswalk.md)] runs that program: the `k = 6` dominant eigenvalue is `2ψ²` for `ψ` the plastic number (real root of `x³ = x + 1`), and its Jacobi–Perron expansion *is* periodic (preperiod 5, period 4) - a cubic analogue of `[2; 2, 2, …]`.

**The complex eigenvalues.** `P(1,L)` has characteristic polynomial `x² − 2x + 2`, roots `1 ± i` — Gaussian integers, with `|1+i| = √2`.[^5] They are not real, so they have no simple continued fraction, and as elements of `Z[i]` their Gaussian continued fractions stop after one term.

## The mod-p counterpart

This page is the real-number counterpart of the [[mod-p-observatory](pages/mod-p-observatory.md)]. Modulo a prime, `F(w,h)` is eventually periodic with period the lcm of the **eigenvalue orders** - the smallest `m` with `λ^m ≡ 1` in `F_{p^d}^*`. Over `R` the analogous invariant is the eigenvalue's **continued-fraction period** (simple for the quadratics, Jacobi–Perron for the cubic `2ψ²`). The [[castle-eigenvalue-oeis-crosswalk](pages/castle-eigenvalue-oeis-crosswalk.md)] links the two: for a norm-`−1` quadratic the same `−1` that makes the fraction purely periodic (Galois) forces `δ^{p+1} = −1` at every inert prime, so the mod-`p` period divides `2(p+1)` but never `p+1` - verified for all five metallic rungs and every prime below 100; and for the `±1` k-direction eigenvalues the period of `P(·,L) mod p` in `k` is `2·p^{⌈log_p L⌉}`.

## Appearances in Sources

- [[closed-form-hunting](pages/closed-form-hunting.md)] — the palindromic/anti-palindromic k-direction characteristic polynomials (orders `2L−2`).
- [[generating-function-gallery](pages/generating-function-gallery.md)] — the L-direction `char_k` polynomials, their complex/high-degree roots, and the dominant eigenvalue `ρ_k ~ k/log k`.
- [[signed-tower-count](pages/signed-tower-count.md)] — `P(1,L) = Re((1+i)^{L+1})`, the `1±i` roots.
- [[mod-p-observatory](pages/mod-p-observatory.md)] — the eigenvalue orders in `F_{p^d}^*` that set the mod-p periods.

## Related Concepts

- [[tower-word-continued-fraction](pages/tower-word-continued-fraction.md)] — the `√2 + 1` growth constant and the Flajolet/Motzkin continued fractions this page's eigenvalue side mirrors.
- [[aocp-generating-functions](pages/aocp-generating-functions.md)] — the Fibonacci/`φ` method, the golden ratio's algebraic home.
- [[pell-numbers](pages/pell-numbers.md)] — the integer sequence realizing `1 + √2 = [2;2,2,…]`, the Pell/silver-ratio companion to Fibonacci/`φ`.
- [[pell-castle-strip](pages/pell-castle-strip.md)] — the castle strip (1-smooth, height ≤ 3, anchored at the base) whose width counts are the Pell numbers.
- [[metallic-means](pages/metallic-means.md)] — the family `δ_a = (a + √(a²+4))/2` (a = 1, 2, 3, …) whose first two members (`φ`, `1+√2`) this page treats; the axis of the Axis-8 "`<metal>` `<axis>` growth castle" meta-classification on [[castle-classification-growth](pages/castle-classification-growth.md)].
- [[castle-by-area](pages/castle-by-area.md)] — `2^{n−1} − F_{n−1}`, where Fibonacci/`φ` enters the castle count.
- [[algebraic-transcendental-wall](pages/algebraic-transcendental-wall.md)] — the algebraic/transcendental split the named constants inhabit.
- [[recurrence-discovery](pages/recurrence-discovery.md)] — the orders (`k+1` in L, `2L−2` in k) the two polynomial families realize.
- [[finite-fields](pages/finite-fields.md)] — the field structure behind the mod-p eigenvalue orders.
- [[spectral-analysis](pages/spectral-analysis.md)] — sibling thread at the *operator* level; this page is at the *sequence* level (`P(k,L)` recurrence characteristic polynomials).
- [[tower-parity-sectors](pages/tower-parity-sectors.md)] / [[plastic-number](pages/plastic-number.md)] - why the L-direction `char_k` factors for even `k` and where the cubic `2ψ²` comes from.
- [[castle-eigenvalue-oeis-crosswalk](pages/castle-eigenvalue-oeis-crosswalk.md)] - the computational follow-through of this page: the metallic rungs' convergents matched to OEIS, the `(x+1)^L (x−1)^{L−2}` factorization that collapses the k-direction, the plastic-number eigenvalue `2ψ²` with its periodic Jacobi–Perron expansion, and the mod-p counterpart made quantitative.
- [[char-k-eisenstein-at-two](pages/char-k-eisenstein-at-two.md)] - proves `char_k` irreducible over `Q` for `k = 2^m − 1`.

## Footnotes

[^1]: [[closed-form-hunting](pages/closed-form-hunting.md)] §"The single-polynomial form stops at L = 3" — the k-direction characteristic polynomials `L=4: [1,2,−1,−4,−1,2,1]`, `L=5: [1,2,−2,−6,0,6,2,−2,−1]`, `L=6: [1,2,−3,−8,2,12,2,−8,−3,2,1]`, "palindromic for even L and anti-palindromic for odd L." The equivalence `p(x) = ±x^d p(1/x) ⟺` reciprocal roots, and the self-reciprocity of the three polynomials, were re-verified with SymPy.

[^2]: The continued-fraction setup and the convergent recurrence `p_n = a_n p_{n−1} + p_{n−2}` (with the golden ratio's convergents `1, 2, 3/2, 5/3, 8/5, 13/8, 21/13` = `F_{n+1}/F_n`) are standard and were verified by executing the fixed-point iterations `x = 1 + 1/x` and `x = 2 + 1/x`.

[^3]: Lagrange's theorem (eventually periodic ⟺ quadratic) and Galois' theorem (purely periodic ⟺ reduced, `α > 1` and conjugate in `(−1, 0)`) are classical. The period-one specialization `[a; a, a, …] = (a + √(a²+4))/2 ⟺ x² − ax − 1 = 0` and the norm-−1 ⇒ reduced argument were verified by execution.

[^4]: Convergents computed and matched: `[1;1,1,…]` gives `2, 3/2, 5/3, 8/5, 13/8, 21/13 → φ`; `[2;2,2,…]` gives `5/2, 12/5, 29/12, 70/29, 169/70 → √2+1`. Norms checked: `φ·(1−φ) = −1` and `(√2+1)(1−√2) = −1`.

[^5]: [[signed-tower-count](pages/signed-tower-count.md)] §"The k = 1 case" — `P(1,L) = Re((1+i)^{L+1})`, characteristic polynomial `x² − 2x + 2`, eigenvalues `1 ± i`.

[^6]: `(3+√5)/2 = 2 + 1/φ = [2; 1, 1, 1, …]` (root of the palindromic `x² − 3x + 1`, norm `+1`, conjugate `0.382 ∉ (−1,0)`, hence not purely periodic) — verified; the contrast with `φ = [1;1,1,…]` (root of `x² − x − 1`, norm `−1`, purely periodic) is the worked illustration of Galois' reduced condition.
