---
title: Eigenvalue continued fractions
category: Concepts
summary: Continued fractions of the eigenvalues of the castle recurrences. A real number has an eventually periodic continued fraction exactly when it is a quadratic irrational (Lagrange), and a quadratic irrational α > 1 is purely periodic exactly when its conjugate lies in (−1, 0) (Galois); a quadratic unit of norm −1, such as φ or 1 + √2, is therefore purely periodic. The recurrences of P(·, L) in the tower height have only the eigenvalues ±1 for 4 ≤ L ≤ 12 (computed); the irrational eigenvalues are the roots of char_k, which are not units, and the real ones of degree 3 or more have non-periodic continued fractions. At inert primes the norm −1 gives δ^{p+1} = −1.
tags: [concept, castle, continued-fraction, eigenvalue, characteristic-polynomial, palindromic, lagrange, galois, quadratic, fibonacci, mod-p, pedagogy]
sources: [de-spinadel-1999-family-of-metallic-means, project-euler-502-solution]
created: 2026-09-15
updated: 2026-10-16
---

# Eigenvalue continued fractions

The castle counts satisfy linear recurrences, and the roots of a recurrence's characteristic polynomial are its eigenvalues. A real eigenvalue has a continued fraction, and whether it is periodic depends on the eigenvalue's degree (Lagrange's theorem) and, for a quadratic, on where its conjugate lies (Galois's theorem). This page states the two theorems with examples and applies them to the eigenvalues of the castle recurrences. [[castle-eigenvalue-oeis-crosswalk](pages/castle-eigenvalue-oeis-crosswalk.md)] computes the convergents and matches them against the OEIS.

## Continued fractions

A continued fraction is

```
[a₀; a₁, a₂, …]  =  a₀ + 1/(a₁ + 1/(a₂ + 1/( … ))),
```

with integers `a₀` and `a₁, a₂, … ≥ 1`. Every real number has one, computed by taking the integer part, subtracting it, inverting the remainder, and repeating. The golden mean `φ = (1 + √5)/2 ≈ 1.618` satisfies `φ = 1 + 1/φ`, so the remainder after the first step is `φ` again and `φ = [1; 1, 1, 1, …]`. A continued fraction is **eventually periodic** when its digits repeat from some point on, and **purely periodic** when they repeat from the first digit.

**Convergents.** The truncations `p_n/q_n = [a₀; a₁, …, a_n]` satisfy `p_n = a_n p_{n−1} + p_{n−2}` and `q_n = a_n q_{n−1} + q_{n−2}`. For `φ`, every `a_n = 1`, so this is the Fibonacci recurrence and the convergents are `F_{n+2}/F_{n+1}`:[^1]

| truncation | `[1]` | `[1; 1]` | `[1; 1, 1]` | `[1; 1, 1, 1]` | `[1; 1, 1, 1, 1]` |
|---|---|---|---|---|---|
| value | `1` | `2` | `3/2` | `5/3` | `8/5` |

## Periodic means quadratic (Lagrange)

**Theorem (Lagrange).** A real number has an eventually periodic continued fraction exactly when it is a quadratic irrational, a root of `ax² + bx + c` with integers `a ≠ 0`, `b`, `c` and irrational roots.[^2]

The direction from periodic to quadratic is the computation for `φ`: if the digits repeat, the number satisfies an equation of degree 2. The period-one fractions are

```
[a; a, a, …]  =  (a + √(a² + 4))/2,
```

the positive root of `x² − ax − 1`, since `x = a + 1/x`. These are the metallic means `δ_a`: `a = 1` gives `φ`, `a = 2` the silver mean `1 + √2`, `a = 3` the bronze mean `(3 + √13)/2` ([[metallic-means](pages/metallic-means.md)]).[^3]

## Purely periodic means reduced (Galois)

`φ = [1; 1, 1, …]` is purely periodic, while `φ² = (3 + √5)/2 = 2 + 1/φ = [2; 1, 1, 1, …]` has the digit 2 before its period. The difference is in the conjugate, the other root of the minimal polynomial:

```
φ          =  [1; 1, 1, …]     conjugate  1 − φ = −0.618 ∈ (−1, 0)      purely periodic
(3 + √5)/2 =  [2; 1, 1, …]     conjugate  (3 − √5)/2 = 0.382 ∉ (−1, 0)  not purely periodic
```

**Theorem (Galois).** A quadratic irrational `α > 1` has a purely periodic continued fraction exactly when its conjugate lies in `(−1, 0)`; such an `α` is called **reduced**.[^2]

For a quadratic unit, a root of `x² − sx + c` with integer `s` and `c = ±1`, the product of the two roots is `c`, and `c` places the conjugate of the root `r > 1`:

- `c = +1`: the conjugate is `1/r ∈ (0, 1)`, so `r` is not reduced and its continued fraction is not purely periodic, as for `φ²`, the root of `x² − 3x + 1`.
- `c = −1`: the conjugate is `−1/r ∈ (−1, 0)`, so `r` is reduced and its continued fraction is purely periodic, as for `φ` and `1 + √2`.

So every quadratic unit of norm `−1` greater than 1 is purely periodic.

## Palindromic polynomials

A polynomial `f(x) = a_d x^d + ⋯ + a_0` with `a_0 ≠ 0` is **palindromic** when `a_i = a_{d−i}` for every `i`, that is `x^d f(1/x) = f(x)`, and **anti-palindromic** when `a_i = −a_{d−i}`, that is `x^d f(1/x) = −f(x)`. In both cases the roots, with multiplicity, are closed under `r ↦ 1/r`; conversely, if the roots of `f` are closed under `r ↦ 1/r`, then `x^d f(1/x) = c·f(x)` with `c = (−1)^d` times the product of the roots, and `c = ±1` because `f ↦ x^d f(1/x)` applied twice gives `f` back. For example, `x² − 3x + 1` is palindromic and its roots `(3 ± √5)/2` are reciprocals, and `x² − 1` is anti-palindromic with roots `±1`.

The quadratics of norm `−1` are of a different kind: the roots `r` and `−1/r` of `x² − sx − 1` are exchanged by `r ↦ −1/r`, and the corresponding identity is `x² f(−1/x) = −f(x)`. `x² − x − 1` is neither palindromic nor anti-palindromic.

## The castle's eigenvalues

The signed tower count `P(k, L)` satisfies linear recurrences in both arguments ([[signed-tower-count](pages/signed-tower-count.md)]).

**In the tower height `k`.** For `4 ≤ L ≤ 12`, the shortest recurrence of `P(·, L)` has order `2L − 2` and characteristic polynomial `(x + 1)^L (x − 1)^{L−2}` (computed; [[signed-tower-k-direction](pages/signed-tower-k-direction.md)], [[closed-form-hunting](pages/closed-form-hunting.md)]):[^4]

```
L = 4:  [1, 2, −1, −4, −1, 2, 1]                   (x + 1)⁴ (x − 1)²
L = 5:  [1, 2, −2, −6, 0, 6, 2, −2, −1]            (x + 1)⁵ (x − 1)³
L = 6:  [1, 2, −3, −8, 2, 12, 2, −8, −3, 2, 1]     (x + 1)⁶ (x − 1)⁴
```

The roots `±1` are their own reciprocals, so these polynomials are palindromic for even `L` and anti-palindromic for odd `L`. The eigenvalues are rational, so their continued fractions terminate, and for these `L` `P(k, L)` is `(−1)^k` times a polynomial in `k` plus a polynomial in `k`.

**In the base length `L`.** The recurrence of `P(k, ·)` has characteristic polynomial `char_k(λ) = λ^{k+1} den_k(1/λ)` of degree `k + 1`, whose roots have product `2^k`. For `k ≤ 30`, no irreducible factor of `char_k` has constant term `±1`, so no root of `char_k` is an algebraic unit (computed).[^4] The real roots of degree 3 or more have continued fractions that are not eventually periodic, by Lagrange's theorem; the first such root, in order of `k`, is the dominant root of `char_4`, a root of the cubic factor `λ³ − 3λ² + 2λ − 4`. [[castle-eigenvalue-oeis-crosswalk](pages/castle-eigenvalue-oeis-crosswalk.md)] computes them and replaces the simple continued fraction by the Jacobi-Perron expansion, which is periodic for the dominant root `2ψ²` of `char_6`, with `ψ` the plastic number ([[plastic-number](pages/plastic-number.md)]).

At `k = 1`, `char_1 = λ² − 2λ + 2` has the complex roots `1 ± i`, so `P(1, L) = Re((1+i)^{L+1})`; complex roots have no simple continued fraction.[^5]

**The metallic means on the castle side.** The metallic means appear as growth constants of castle families ([[metallic-means](pages/metallic-means.md)]):

| `a` | `δ_a = [a; a, a, …]` | name | sequence | castle families with this growth |
|---|---|---|---|---|
| 1 | `(1 + √5)/2 ≈ 1.618` | golden | Fibonacci, `A000045` | the Fibonacci castles, golden by width ([[fibonacci-castle](pages/fibonacci-castle.md)]); the prime castles, `F_{n−1}` of area `n`, golden by area ([[prime-castles](pages/prime-castles.md)]) |
| 2 | `1 + √2 ≈ 2.414` | silver | Pell, `A000129` ([[pell-numbers](pages/pell-numbers.md)]) | the anchored 1-smooth strips on the heights `{1, 2, 3}`, silver by width ([[pell-castle-strip](pages/pell-castle-strip.md)]); the tower words, silver by length ([[tower-word-continued-fraction](pages/tower-word-continued-fraction.md)]) |
| `a ≥ 3` | `(a + √(a² + 4))/2` | bronze at `a = 3`; no name for `a ≥ 4` | | the ridge castles of height `h = a + 1`, `δ_{h−1}` by width ([[ridge-castle](pages/ridge-castle.md)]) |

`φ` and `1 + √2` are the fundamental units of `Q(√5)` and `Q(√2)`, and `δ_a` is the fundamental unit of `Z[δ_a]` ([[metallic-means](pages/metallic-means.md)]).

## Modulo p

Modulo an odd prime `p` with `p ∤ a² + 4`, the sequence `x_n = a·x_{n−1} + x_{n−2}` of `δ_a` is periodic, with period the lcm of the multiplicative orders of `δ_a` and its conjugate `δ̂_a` in the field that contains them. At a prime where `x² − ax − 1` is irreducible over `F_p`, the Frobenius map `z ↦ z^p` exchanges `δ_a` and `δ̂_a`, so `δ_a^{p+1} = δ_a·δ̂_a = −1`, and the period divides `2(p + 1)` and not `p + 1`. The norm `−1` that makes the continued fraction of `δ_a` purely periodic is the value of `δ_a^{p+1}` ([[castle-eigenvalue-oeis-crosswalk](pages/castle-eigenvalue-oeis-crosswalk.md)], Part 2). The periods of `char_k` and of `A^e(w, h)` modulo `p` are on [[mod-p-observatory](pages/mod-p-observatory.md)].

## Appearances in Sources

- [[de-spinadel-1999-family-of-metallic-means](pages/de-spinadel-1999-family-of-metallic-means.md)] - the metallic means and their purely periodic continued fractions `[n̄]`.
- [[project-euler-502-solution](pages/project-euler-502-solution.md)] - the eigenvalues `1 ± i` of the recurrence of `P(1, L)`.

## Related Concepts

- [[castle-eigenvalue-oeis-crosswalk](pages/castle-eigenvalue-oeis-crosswalk.md)] - the convergents of the metallic means against the OEIS, the norm modulo `p`, and the Jacobi-Perron expansions of the roots of `char_k`.
- [[metallic-means](pages/metallic-means.md)] - de Spinadel's family `σ_p^q`, the members `δ_a = σ_a^1`, and their units.
- [[signed-tower-k-direction](pages/signed-tower-k-direction.md)] - the recurrences of `P(·, L)` in `k`.
- [[recurrence-discovery](pages/recurrence-discovery.md)] - the orders `k + 1` in `L` and `2L − 2` in `k`.
- [[generating-function-gallery](pages/generating-function-gallery.md)] - `char_k` and its dominant root `ρ_k`.
- [[tower-parity-sectors](pages/tower-parity-sectors.md)] and [[plastic-number](pages/plastic-number.md)] - the factors of `char_k` for even `k`, and the root `2ψ²` of `char_6`.
- [[char-k-eisenstein-at-two](pages/char-k-eisenstein-at-two.md)] - the proof that `char_k` is irreducible for `k = 2^m − 1`.
- [[mod-p-observatory](pages/mod-p-observatory.md)] and [[finite-fields](pages/finite-fields.md)] - periods modulo `p` and the Frobenius map.
- [[aocp-generating-functions](pages/aocp-generating-functions.md)] - Knuth's derivation of `F_n = (φ^n − φ̂^n)/√5`.
- [[algebraic-transcendental-wall](pages/algebraic-transcendental-wall.md)] - algebraic and transcendental constants and generating functions.

## Footnotes

[^1]: Verified by execution (Python 3.11, 2026-10-16): the convergents of `[1; 1, 1, …]` are `1, 2, 3/2, 5/3, 8/5, 13/8, 21/13`, and those of `[2; 2, 2, …]` are `2, 5/2, 12/5, 29/12, 70/29, 169/70`; `φ·(1 − φ) = −1` and `(1 + √2)(1 − √2) = −1`.
[^2]: https://www.numdam.org/article/AMPA_1828-1829__19__294_0.pdf (read 2026-10-16) - É. Galois, "Démonstration d'un théorème sur les fractions continues périodiques", Annales de Mathématiques pures et appliquées 19 (1828-1829), 294-301. p.294: "si, par la méthode de Lagrange, on développe en fraction continue une des racines d'une équation du second degré, cette fraction continue sera périodique" (the periodicity of quadratic irrationals, attributed to Lagrange); pp.298-299: a root greater than 1 of a quadratic is immediately (purely) periodic exactly when the other root lies between 0 and −1.
[^3]: [[de-spinadel-1999-family-of-metallic-means](pages/de-spinadel-1999-family-of-metallic-means.md)] L159-186 [synthesis] - the Golden Mean `[1̄]`, the Silver Mean `[2̄]`, the Bronze Mean `(3 + √13)/2 = [3̄]`, `σ_4^1 = 2 + √5 = [4̄] = φ³`, and "all of them are of the form [n̄], a purely periodic continued fraction expansion".
[^4]: Verified by execution (Python 3.11 with SymPy, 2026-10-16): Berlekamp-Massey on `P(k, L)` for `k ≤ 59` gives the characteristic polynomial `(x + 1)^L (x − 1)^{L−2}` for `4 ≤ L ≤ 12`, with the coefficient lists of the table; for `k ≤ 30`, every irreducible factor of `char_k` has constant term of absolute value greater than 1; the dominant root of `char_4` is the root `2.7963…` of `λ³ − 3λ² + 2λ − 4`.
[^5]: [[project-euler-502-solution](pages/project-euler-502-solution.md)] §"Recursion for P(k, L)" L103-108 - "The matrix (1 1; -1 1) has eigenvalues 1 + i and 1 - i", "P(1, L) = Re((1+i)^{L+1})".
