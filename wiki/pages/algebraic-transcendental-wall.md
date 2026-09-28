---
title: The algebraic/transcendental wall
category: Concepts
summary: The castle's width-and-height counts (T, P, F) are C-finite, so their canonical closed forms carry only algebraic constants — √2, √5, φ, i, the plastic number — while e and π enter only through limits (Stirling, Catalan, natural-log growth) or inside algebraic values such as cos(π/4).
tags: [concept, castle, algebraic, transcendental, c-finite, golden-ratio, sqrt2, e, pi, asymptotics, pedagogy]
sources: [project-euler-502-representations, aocp-permutations, aocp-generating-functions, generating-functions-topic]
created: 2026-09-15
updated: 2026-09-28
---

# The algebraic/transcendental wall

## Summary

Every exact count of castles by width and height, `T(k,L)`, `P(k,L)` and `F(w,h)`, is **C-finite**: it satisfies a linear recurrence, so its generating function is rational and its canonical closed form is a finite sum of polynomial×exponential terms whose bases are **algebraic** numbers. The transcendental constants `e` and `π` are not needed in these formulas. Where they appear in an equivalent form, as in `Re((1+i)^{L+1}) = 2^{(L+1)/2} cos((L+1)π/4)` or a root of unity `e^{2πi/m}`, they sit inside an algebraic value; otherwise they enter through **limits** (Stirling's formula, Catalan asymptotics, natural-log growth). Some counts by area are not C-finite (the convex castles, A001523, and the signed count by area, a q-series on [[castle-q-bessel-closed-form](pages/castle-q-bessel-closed-form.md)]) and fall outside this page.

## The two sides

**Algebraic side — reachable in finitely many steps.** The algebraic numbers are everything obtainable from the rationals by `+ − × ÷` and by taking roots of polynomials. They form a field and are *algebraically closed*: the roots of any polynomial with algebraic coefficients are again algebraic.[^2] So any finite closed form built from rationals, arithmetic, and root-taking stays on this side.

**Transcendental side — reachable only in a limit.** `e` and `π` lie past that line: Hermite (1873) proved `e` transcendental, Lindemann (1882) proved `π` transcendental.[^2] No finite expression of rationals under the algebraic operations can reach them.

## Why the wall holds: C-finite ⟹ algebraic closed forms

The link to the castle is the **Binet formula**. A C-finite sequence `(a_n)` has a rational generating function `N(x)/D(x)`, and its `n`-th term expands as

```
a_n = Σ_i  p_i(n) · r_i^n,
```

where the `r_i` are the roots of the characteristic polynomial — algebraic — and the `p_i` are polynomials with algebraic coefficients. Fibonacci is the simplest example: `x² = x + 1` has roots `φ, φ̂`, and `F_n = (φ^n − φ̂^n)/√5` has this form.[^1] The constants entering the *canonical* closed form of a C-finite sequence are therefore always algebraic. Since the castle's counts — `T(k,L) = (k+1)^L`, `P(k,L)`, and `F(w,h)` — are all C-finite ([[signed-tower-count](pages/signed-tower-count.md)], [[castle-counting-formula](pages/castle-counting-formula.md)]), their closed forms live entirely on the algebraic side.

## The castle's residents on each side

**Exact (algebraic).** The constants that appear exactly are characteristic roots. The named quadratic ones:[^4]

- `φ = (1+√5)/2` — Fibonacci's growth rate (`F_n = (φ^n − φ̂^n)/√5`) and the `F_{n−1}` prime castles of [[prime-castles](pages/prime-castles.md)].
- `√2` — `|1+i| = √2` in `P(1,L) = Re((1+i)^{L+1})`, and the tower-word growth constant `√2 + 1`.
- `√5` — the Fibonacci denominator.
- `i` — the `1±i` eigenvalues of `P(1,·)`.

The higher-degree eigenvalues (the `ρ_k` of [[generating-function-gallery](pages/generating-function-gallery.md)]) are algebraic too, of degree at most `k+1`: the dominant root of `char_4` is a cubic, and `ρ_6 = 2ψ²` is cubic, for `ψ` the plastic number ([[plastic-number](pages/plastic-number.md)]).

**Asymptotic.** `e` and `π` appear in these limits as `n → ∞`:[^3]

- Stirling `n! ≈ √(2πn)(n/e)^n` ([[aocp-permutations](pages/aocp-permutations.md)]).
- Catalan `C_n ~ 4^n/(n^{3/2}√π)` ([[catalan-numbers](pages/catalan-numbers.md)]) and the central binomial `C(2n,n) ~ 4^n/√(πn)`.
- The natural log in `ρ_k ~ k/log k` ([[generating-function-gallery](pages/generating-function-gallery.md)]).

One caveat: the `e` in the exponential generating function `e^x` is formal bookkeeping, `e^x = Σ x^n/n!`, which only equals the number `e` on evaluating `x = 1`. The EGF parity projector `(e^x ± e^{−x})/2` ([[generating-functions-topic](pages/generating-functions-topic.md)]) is the classical EGF form of the castle's `(T±P)/2` even/odd split, and its `e` is a formal symbol. Among the limits above, the number `e` enters through Stirling's `(n/e)^n` and the natural log.

## How the transcendental constants enter

In the exact formulas `e` and `π` are not needed; they enter through **limits**. The standard illustration is `n!`. The factorial is an integer — trivially algebraic — yet its asymptotic

```
n! ≈ √(2πn) · (n/e)^n      (relative error → 0)
```

carries both `e` and `π`.[^3] The equality holds only in the limit `n → ∞`; for every finite `n` the two sides differ. The transcendental constants enter because Stirling's formula is an asymptotic statement, not an identity. The same holds for the Catalan and central-binomial asymptotics (`π`) and the natural-log growth rate `k/log k` (`e`): each is a limit statement over a family whose exact terms are integers.

## Appearances in Sources

- [[aocp-permutations](pages/aocp-permutations.md)] — Stirling `n! ≈ √(2πn)(n/e)^n` and its castle-scale role.
- [[aocp-generating-functions](pages/aocp-generating-functions.md)] — the Fibonacci Binet formula `F_n = (φ^n − φ̂^n)/√5`.
- [[catalan-numbers](pages/catalan-numbers.md)] — `C_n ~ 4^n/(n^{3/2}√π)`.
- [[generating-function-gallery](pages/generating-function-gallery.md)] — `ρ_k ~ k/log k`.

## Related Concepts

- [[signed-tower-count](pages/signed-tower-count.md)] / [[castle-counting-formula](pages/castle-counting-formula.md)] — the C-finite families whose closed forms the wall bounds.
- [[eigenvalue-continued-fractions](pages/eigenvalue-continued-fractions.md)] — the algebraic quadratics `φ`, `√2+1`, `i` and their continued fractions.
- [[tower-word-continued-fraction](pages/tower-word-continued-fraction.md)] — the `√2+1` growth constant.
- [[tower-word-language](pages/tower-word-language.md)] — the regular→rational, context-free→algebraic hierarchy the wall extends one rung further.
- [[castle-by-area](pages/castle-by-area.md)] — `2^{n−1} − F_{n−1}`, where `φ` enters the exact count.
- [[fractional-recurrences](pages/fractional-recurrences.md)] — the fractional-Fibonacci recurrence `∇^α a_n = a_{n-1}` has an algebraic growth constant `g(α)` for rational `α`; by Gelfond-Schneider on `α = log r / log(1-r)`, an algebraic `g(α)` forces `α` rational or transcendental, so every algebraic irrational `α` (and all `α` outside a countable set) gives a transcendental growth constant with no limit involved.
- [[kitamasa](pages/kitamasa.md)] — the reduced polynomial `R` with `R(λ) = λ^n` on the eigenvalues, which are algebraic.
- [[generating-function-gallery](pages/generating-function-gallery.md)] — derives the `ρ_k ~ k / log k` asymptotic.
- [[signed-tower-k-direction](pages/signed-tower-k-direction.md)] — the k-direction eigenvalues are only `±1`, which are rational.
- [[prellberg-brak-1995-cluster-models](pages/prellberg-brak-1995-cluster-models.md)] — the bar-graph GF at fixed perimeter and area is a q-Bessel function, and the tricritical asymptotic scaling function is the logarithmic derivative of Airy, `Ai'/Ai`. The exact q-series is not holonomic, and the scaling function is a transcendental special function obtained in a limit.
- [[castle-samplers](pages/castle-samplers.md)] - samplers for random castles, used in limit-law experiments.

## Footnotes

[^1]: [[aocp-generating-functions](pages/aocp-generating-functions.md)] §"Knuth's Fibonacci example" — the recurrence → rational GF → partial-fractions → `F_n = (φ^n − φ̂^n)/√5` procedure; the Binet form `a_n = Σ p_i(n) r_i^n` is the same partial-fraction expansion at degree `d`.

[^2]: The algebraicity of the algebraic numbers (a field, algebraically closed) and the transcendence of `e` (Hermite 1873) and `π` (Lindemann 1882) are classical: no finite expression built from rationals by the algebraic operations can equal a transcendental.

[^3]: [[aocp-permutations](pages/aocp-permutations.md)] §"Factorial Identities" — `n! ≈ √(2πn)(n/e)^n` (re-verified); [[catalan-numbers](pages/catalan-numbers.md)] — `C_n ~ 4^n/(n^{3/2}√π)`; [[generating-function-gallery](pages/generating-function-gallery.md)] — `ρ_k ~ k/log k`.

[^4]: The quadratic constants: `P(1,L) = Re((1+i)^{L+1})` with `|1+i| = √2` ([[signed-tower-count](pages/signed-tower-count.md)]); the tower-word growth constant `√2+1` from the discriminant `z² + 2z − 1` ([[tower-word-continued-fraction](pages/tower-word-continued-fraction.md)]); `φ`, `√5`, `i` as on [[eigenvalue-continued-fractions](pages/eigenvalue-continued-fractions.md)].
