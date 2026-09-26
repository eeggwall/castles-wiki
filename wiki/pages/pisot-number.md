---
title: Pisot number (class S)
category: Concepts
summary: A real algebraic integer θ > 1 whose other conjugates all lie strictly inside the unit circle (Salem's class S). Its powers approach integers geometrically because the trace is an integer; every real number field contains one; and ‖λθ^n‖ → 0 forces θ to be Pisot whenever θ is algebraic or the errors are square-summable. Eight of the nine height-3 castle-strip cubics are Pisot (all but 2cos(π/7)), and 32 of the 56 at height 4.
tags: [concept, pisot-number, algebraic-integer, diophantine-approximation, near-integer, trace, rational-generating-function, hankel-determinant, castle, growth-constant, number-field]
sources: [salem-1963-algebraic-numbers-fourier-analysis]
created: 2026-09-25
updated: 2026-09-25
---

# Pisot number (class S)

## Description

A **Pisot number** is a real algebraic integer `θ > 1` all of whose other conjugates have modulus strictly less than 1. Salem calls the set of them **the class S**. Every rational integer `> 1` is trivially in S, and `1` is excluded by convention.[^1]

**Why powers approach integers.** If `θ` has degree `k` and conjugates `α_1, …, α_{k−1}`, then the trace `θ^n + α_1^n + … + α_{k−1}^n` is a rational integer. The conjugate part is at most `(k−1)ρ^n` with `ρ = max|α_j| < 1`. So the distance `‖θ^n‖` from `θ^n` to the nearest integer tends to 0 like a geometric progression, and the same holds for `λθ^n` with `λ` any algebraic integer of `Q(θ)`.[^2] The trace sequence is the integer sequence the powers hug: Lucas for `φ`, Perrin for the plastic number ([[plastic-number](pages/plastic-number.md)]), companion Pell for `1 + √2` ([[pell-numbers](pages/pell-numbers.md)]).

**Existence.** Every real algebraic number field contains Pisot numbers of the field's full degree, by Minkowski's theorem on linear forms.[^3] Consequently no real field is "Pisot-free", and the question for castle constants is always which *particular* Perron root is Pisot.

**The converse, and what is open.** Salem proves two partial converses.[^4]

- **Theorem A.** If some real `λ ≠ 0` has `Σ ‖λθ^n‖² < ∞`, then `θ` is Pisot and `λ ∈ Q(θ)`.
- **Theorem B.** If `θ` is algebraic and `‖λθ^n‖ → 0`, then `θ` is Pisot.

Whether a *transcendental* `θ` can satisfy `‖λθ^n‖ → 0` is open. The set of all such `θ` is countable: once the errors are small, the nearest integers obey `a_{n+2} = round(a_{n+1}²/a_n)`, so finitely many terms fix the sequence and `θ = lim a_{n+1}/a_n`.[^5]

## The rational-series machinery

The proofs of Theorems A and B turn "powers near integers" into "a rational generating function with integer coefficients", which is the castle's native language ([[generating-functions](pages/generating-functions.md)]).[^6]

- **Recurrence ⇔ rational** (Lemma I): the wiki's standing principle ([[aocp-generating-functions](pages/aocp-generating-functions.md)]).
- **Fatou's lemma** (Lemma II): an integer series that is rational is `P/Q` with `P, Q` integer polynomials and `Q(0) = 1`. Every castle count with a rational GF, such as `num_k/den_k` on [[generating-function-gallery](pages/generating-function-gallery.md)], therefore has an integer denominator normalized to constant term 1.
- **Kronecker's Hankel test** (Lemma III): `Σ c_n z^n` is rational iff the Hankel determinants `det(c_{i+j})_{0 ≤ i,j ≤ m}` vanish for all large `m`. This is the determinant form of the minimal-order question [[berlekamp-massey](pages/berlekamp-massey.md)] solves by elimination: the first `m` at which they start vanishing is the recurrence order.

Once `Σ a_n z^n = P/Q` with `Q(0) = 1`, the difference `λ/(1 − θz) − P/Q` has radius of convergence at least 1. So `1/θ` is the only root of `Q` inside the unit disc, the error hypothesis keeps roots off the circle, and the reciprocal of `Q` is a polynomial whose only root outside the unit circle is `θ`.[^7]

## Castle constants tested

Applied to the growth constants the wiki has already met. The nine height-3 cubics are the cubic frontier of [[reachable-field-census](pages/reachable-field-census.md)], which also carries the height-4 count (32 of 56 cubics Pisot).[^exec]

| constant | minimal polynomial | other conjugates, modulus | Pisot? | `‖θ^40‖` |
|---|---|---|---|---|
| plastic `ψ = 1.3247` | `x³ − x − 1` | `0.8688` (complex pair) | yes | `7.2e-3` |
| supergolden `1.4656` | `x³ − x² − 1` | `0.8260` (pair) | yes | `4.0e-4` |
| `ψ² = 1.7549` | `x³ − 2x² + x − 1` | `0.7549` (pair) | yes | `2.5e-5` |
| `Q(ζ₇)⁺` cubic `1.8019` | `x³ − x² − 2x + 1` | `1.247`, `0.445` (real) | **no** | `0.27` |
| tribonacci `1.8393` | `x³ − x² − x − 1` | `0.7374` (pair) | yes | `6.2e-6` |
| `2.1479` | `x³ − x² − 2x − 1` | `0.6823` (pair) | yes | `3.0e-7` |
| `2.2056` | `x³ − 2x² − 1` | `0.6733` (pair) | yes | `2.7e-7` |
| second `Q(ζ₇)⁺` root `2.2470` | `x³ − 2x² − x + 1` | `0.802`, `0.555` (real) | yes | `1.5e-4` |
| `ψ + 1 = 2.3247` | `x³ − 3x² + 2x − 1` | `0.6559` (pair) | yes | `8.8e-8` |

The `Q(ζ₇)⁺` root `2cos(π/7)` is totally real, and its conjugate `2cos(5π/7) = −1.247` sits outside the unit circle, so its powers do not settle: `‖θ^n‖` reads `0.002, 0.09, 0.36, 0.27` at `n = 5, 10, 20, 40`. By Theorem B no `λ` can make `‖λθ^n‖ → 0` for it. The same field also holds the Pisot Perron root `2.2470`, a totally real Pisot number, so one field can hold both a Pisot and a non-Pisot castle constant, consistent with Theorem 2.

Elsewhere on the wiki:

- **Every metallic mean is Pisot.** `δ_a` has norm `−1`, so its conjugate `δ̂_a = −1/δ_a` lies in `(−1, 0)` ([[metallic-means](pages/metallic-means.md)]). Theorem 1 is then the Binet decay the metallic page already uses.
- **`2ψ²` is not Pisot but `ψ²` is.** `ρ_6 = 2ψ²` has conjugates of modulus `1.51`. Halving it gives the Pisot `ψ²` ([[plastic-number](pages/plastic-number.md)], [[tower-parity-sectors](pages/tower-parity-sectors.md)]).
- **The `k = 10` quintic half-eigenvalue is not Pisot** (a conjugate of modulus `1.09`, [[castle-eigenvalue-oeis-crosswalk](pages/castle-eigenvalue-oeis-crosswalk.md)]).

**Hankel test on Perrin.** The Hankel determinants of the Perrin sequence `3, 0, 2, 3, 2, 5, 5, 7, …` are `3, 6, −23, 0, 0, 0, 0` for orders `m = 0..6`. They vanish from `m = 3` on, which is Kronecker's certificate that Perrin is order-3 C-finite. The last nonzero value, `−23`, is the discriminant of `x³ − x − 1`: the Hankel matrix of a power-sum sequence factors as `VᵀV` with `V` the Vandermonde of the roots, so its determinant is the squared Vandermonde.[^exec]

**The countability recursion on a castle trace.** The trace of `ψ + 1` (`3, 3, 5, 12, 29, 68, 158, 367, 853, 1983, …`) satisfies `a_{n+2} = round(a_{n+1}²/a_n)` for every `n ≥ 7` checked (through `n = 40`). It fails only at `n = 0, 1, 3, 4, 6`, while the conjugate error is still large. That is the Chapter I §4 mechanism: past a threshold, two terms determine the rest.[^exec]

```python
from mpmath import mp, polyroots, nint, fabs
mp.dps = 60
def pisot_check(coeffs, n=40):
    """Conjugate moduli and ||theta^n|| for a monic integer polynomial (highest degree first)."""
    r = sorted(polyroots(coeffs, maxsteps=200, extraprec=100), key=abs, reverse=True)
    th = r[0].real
    return all(abs(z) < 1 for z in r[1:]), [float(abs(z)) for z in r[1:]], float(fabs(th**n - nint(th**n)))
pisot_check([1, -1, -2, 1])   # (False, [1.247..., 0.445...], 0.27...)
```

## Appearances in Sources

- [[salem-1963-algebraic-numbers-fourier-analysis](pages/salem-1963-algebraic-numbers-fourier-analysis.md)] - Chapter I: definition of class S, Theorems 1 and 2, the converses A and B, and the countability of the open case.

## Related Concepts

- [[plastic-number](pages/plastic-number.md)] - a cubic Pisot number; `ψ^n − Perrin(n) → 0` is Theorem 1 for it.
- [[metallic-means](pages/metallic-means.md)] - the quadratic Pisot units of norm `−1`.
- [[reachable-field-census](pages/reachable-field-census.md)] - the castle-strip Perron roots, whose cubic frontier is classified above.
- [[castle-classification-growth](pages/castle-classification-growth.md)] - the "cubic-Pisot family" of growth castles.
- [[tower-parity-sectors](pages/tower-parity-sectors.md)] / [[castle-eigenvalue-oeis-crosswalk](pages/castle-eigenvalue-oeis-crosswalk.md)] - where signed-tower eigenvalues are tested for the Pisot property.
- [[berlekamp-massey](pages/berlekamp-massey.md)] / [[recurrence-discovery](pages/recurrence-discovery.md)] - the algorithmic counterpart of Kronecker's Hankel test.
- [[pell-numbers](pages/pell-numbers.md)] - the trace sequence of `1 + √2`.

## Footnotes

[^1]: [[salem-1963-algebraic-numbers-fourier-analysis](pages/salem-1963-algebraic-numbers-fourier-analysis.md)] Ch. I §2 p.2 [synthesis] L275-282 - definition of class S (all conjugates other than θ of modulus strictly less than 1); θ is real, taken positive; every natural integer belongs to S, but 1 is excluded, so θ > 1.
[^2]: [[salem-1963-algebraic-numbers-fourier-analysis](pages/salem-1963-algebraic-numbers-fourier-analysis.md)] Ch. I §2 Theorem 1 and Remark p.3 [synthesis] L289-315 - the integer trace, the `(k−1)ρ^n` bound, "the general term of a convergent geometric progression", and the extension to `λθ^n` for λ an algebraic integer of the field of θ.
[^3]: [[salem-1963-algebraic-numbers-fourier-analysis](pages/salem-1963-algebraic-numbers-fourier-analysis.md)] Ch. I §2 Theorem 2 p.3 [synthesis] L316-347 - "In every real algebraic field, there exist numbers of the class S", via Minkowski's theorem on linear forms; footnote: of the degree of the field.
[^4]: [[salem-1963-algebraic-numbers-fourier-analysis](pages/salem-1963-algebraic-numbers-fourier-analysis.md)] Ch. I §3 p.4 [synthesis] L357-392 - "This important problem is still unsolved"; Theorems A and B.
[^5]: [[salem-1963-algebraic-numbers-fourier-analysis](pages/salem-1963-algebraic-numbers-fourier-analysis.md)] Ch. I §4 p.11 [synthesis] L839-898 - the open problem (transcendental θ) and the theorem that the set of such θ is denumerable, since `a_{n+2}` "is uniquely determined by the two preceding integers".
[^6]: [[salem-1963-algebraic-numbers-fourier-analysis](pages/salem-1963-algebraic-numbers-fourier-analysis.md)] Ch. I §3 Lemmas I-III pp.4-7 [synthesis] L393-661 - Lemma I (rational iff recurrence), Lemma II (Fatou: integral `P, Q`, `Q(0) = 1`), Lemma III (Kronecker: rational iff the Hankel determinants vanish for `m > m_1`), with proofs of II and III.
[^7]: [[salem-1963-algebraic-numbers-fourier-analysis](pages/salem-1963-algebraic-numbers-fourier-analysis.md)] Ch. I §3 proof of Theorem A pp.8-9 [synthesis] L663-771 - `Q` has the one root `1/θ` inside the unit circle and none on it; the reciprocal polynomial has θ as its only root of modulus larger than 1.
[^exec]: Verified by execution (2026-09-25, own computation; Python 3, mpmath at 60 digits, SymPy): conjugate moduli and `‖θ^n‖` at `n = 5, 10, 20, 40` for the nine height-3 cubics; Hankel determinants of Perrin for `m = 0..6`; the rule `a_{n+2} = round(a_{n+1}²/a_n)` on the trace of `x³ − 3x² + 2x − 1` for `n ≤ 40`. The discriminant-as-squared-Vandermonde step is own reasoning.
