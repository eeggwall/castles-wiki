---
title: The castle sign is a KMS matrix at ρ = i
category: Analyses
summary: Weight each block of towers by t. The block-weighted tower transfer matrix M_k(t) on tower heights 0..k, with entry t^max(0, b−a), is diagonally similar to the Kac-Murdock-Szegő matrix K(ρ) = (ρ^|a−b|) with ρ = √t, so t enters only as √t. At ρ = 1, K is the all-ones matrix, of rank one, which gives (k+1)^L. At ρ = i, K(i) has the tridiagonal inverse (E_∂ − iA_path)/2, which gives char_k(λ) = ½ det(λE_∂ − 2I − iλA_path) and the recurrence char_{k+1} = λ² char_{k−1} − 2 char_k. The reversal symmetry of K pulled back through the similarity is the involution of tower-parity-sectors, with (DJ)² = (−1)^k. For real 0 < ρ < 1 the Toeplitz symbol is the Poisson kernel, so the towers of any height weighted by t^blocks grow like ((1+√t)/(1−√t))^w, matching the first singularity of the Deutsch-Elizalde generating function, whose discriminant factors over Q(√y); at y = ±z it gives the unsigned and the signed semi-perimeter cubics.
tags: [analysis, castle, sign, parity, transfer-matrix, toeplitz, kms-matrix, poisson-kernel, gaussian-integers, cayley-transform, characteristic-polynomial, signed-tower-count, semi-perimeter, motzkin]
sources: [project-euler-502-solution, project-euler-502-brute-force, deutsch-elizalde-2016-bargraphs-cornerless-motzkin]
created: 2026-09-27
updated: 2026-10-16
---

# The castle sign is a KMS matrix at ρ = i

## Overview

On the Motzkin-path castles the sign `(−1)^{blocks}` acts by putting `√t = i` into the up-step weight: the branch points `x = 1/(1 ± 2√t)` of their generating function become `x = 1/(1 ± 2i)`, and the eigenvalues `1 + 2√t cos(πj/(h+1))` of the bounded-height strip become `1 + 2i cos(πj/(h+1))` ([[motzkin-castles](pages/motzkin-castles.md)] §3). The signed tower count `P(1, L) = Re((1+i)^{L+1})` is another Gaussian value ([[signed-tower-count](pages/signed-tower-count.md)]). This page shows the same for towers with no rule on neighboring columns, at every height bound: a weight `t` per block enters the transfer matrix only through `√t`, by a diagonal similarity to a Kac-Murdock-Szegő matrix, and the sign is the point `√t = i`. Every identity and number on this page was rechecked by execution.[^5]

## 1. The transfer matrix is a KMS matrix

Towers of height at most `k` on a base of length `L` are given by their column heights `c_1, …, c_L ∈ {0, …, k}`. Their block count is the total rise from height 0, `Σ max(0, c_i − c_{i−1})` with `c_0 = 0`,[^1] so a weight `t` per block factors over consecutive columns:

```
M_k(t)[a][b] = t^max(0, b − a)        (a, b = 0, …, k; size k + 1 = the castle height bound)
```

Summing `t^{blocks}` over all towers of height at most `k` on a base of length `L` gives `e_0ᵀ M_k(t)ᴸ 𝟙`, with `e_0` the start state at height 0 and `𝟙` the all-ones vector.

At `t = 1` this sum is the tower count `T(k, L) = (k+1)^L`, and at `t = −1` it is the signed tower count `P(k, L)`, the sum of `(−1)^{blocks}` over the towers of height at most `k` on a base of length `L`.[^2] The matrices reproduce `P(1, ·) = 1, 0, −2, −4, −4, 0, 8, 16` and `P(2, ·) = 1, 1, 3, 9, 19, 33, 59, 121` of [[signed-tower-count](pages/signed-tower-count.md)]. The signed transfer matrix `M̃_k` of [[tower-parity-sectors](pages/tower-parity-sectors.md)], with entry `(−1)^{max(0, a − b)}`, counts descents instead of rises; `M_k(−1)` is its transpose and has the same characteristic polynomial `char_k`.

Conjugate by `D_ρ = diag(1, ρ, ρ², …, ρ^k)` with `ρ² = t`. An entry above the diagonal becomes `ρ^a t^{b−a} ρ^{−b} = ρ^{b−a}`, and an entry below it becomes `ρ^{a−b}`. So

```
D_ρ M_k(ρ²) D_ρ⁻¹ = K(ρ),      K(ρ)[a][b] = ρ^{|a − b|},                         (1)
```

the **Kac-Murdock-Szegő (KMS) matrix**, a symmetric Toeplitz matrix; Fikioris studies its eigenvalues for complex `ρ`.[^4] By Equation (1), the block weight enters only as `ρ = √t`, and the two castle weights are two points of one family:

- **unsigned, `ρ = 1`.** `K(1)` is the all-ones matrix, of rank one, with the single nonzero eigenvalue `k + 1`, which gives `T(k, L) = (k+1)^L` ([[castle-counting-formula](pages/castle-counting-formula.md)]).
- **signed, `ρ = i`.** `K(i)[a][b] = i^{|a−b|}`, a complex symmetric Toeplitz matrix. `P(k, L) = e_0ᵀ D_i⁻¹ K(i)ᴸ D_i 𝟙`, so `M_k(−1)` and `K(i)` have the same characteristic polynomial, and the recurrence of `P(k, ·)` has the eigenvalues of `K(i)` as its roots.

The Motzkin strip of [[motzkin-castles](pages/motzkin-castles.md)] §3 is the tridiagonal part of the same matrix. Keeping only `|a − b| ≤ 1` gives `I + ρ·A_path`, with `A_path` the adjacency matrix of the path on the heights (not the castle count `A(w, h)`), whose eigenvalues are `1 + 2ρ cos(πj/(h+1))` on `h` states. In both cases the sign is `ρ = i`.

## 2. At ρ = i the inverse loses its interior diagonal

A KMS matrix has a tridiagonal inverse:

```
K(ρ)⁻¹ = (1/(1 − ρ²)) · [ diag(1, 1 + ρ², …, 1 + ρ², 1) − ρ·A_path ],      ρ² ≠ 1.        (2)
```

Multiplying out proves it: in an interior column the entry `ρ^m` of `K(ρ)` at distance `m ≥ 1` from the diagonal meets `ρ^m (1 + ρ²) − ρ(ρ^{m−1} + ρ^{m+1}) = 0`, the diagonal entry meets `(1 + ρ²) − 2ρ² = 1 − ρ²`, and the two end columns work the same way with diagonal entry 1. At `ρ = 1` the prefactor is infinite, since the all-ones matrix is singular. At `ρ = i` the interior diagonal `1 + ρ²` vanishes:

```
K(i)⁻¹ = (E_∂ − i·A_path)/2,      E_∂ = diag(1, 0, …, 0, 1),      det K(i) = 2^k.             (3)
```

The determinant follows from `det K(ρ) = (1 − ρ²)^k`. So the inverse of the signed transfer matrix, up to the similarity, is a path with imaginary edge weights and a loop at each end. From `det(λI − K) = det K · det(λK⁻¹ − I)` and Equation (3),

```
char_k(λ) = ½ · det( λE_∂ − 2I − iλ·A_path ),                                              (4)
```

a tridiagonal determinant with diagonal `(λ − 2, −2, …, −2, λ − 2)` and off-diagonal entries `−iλ`. Expanding it along the interior gives `D_m = −2·D_{m−1} − (−iλ)²·D_{m−2} = −2·D_{m−1} + λ²·D_{m−2}`, which is the recurrence

```
char_{k+1}(λ) = λ²·char_{k−1}(λ) − 2·char_k(λ)                                             (5)
```

of [[generating-function-gallery](pages/generating-function-gallery.md)], there obtained from the update of `num_k` and `den_k`. Its characteristic roots in `k` are `r_± = −1 ± √(1 + λ²)`. With a real off-diagonal `−λ` the expansion would give `D_m = −2·D_{m−1} − λ²·D_{m−2}`; the factor `i` changes the sign of the `λ²` term.

## 3. The sector involution is the KMS reversal symmetry

`K(ρ)` is symmetric Toeplitz, so it commutes with the reversal `J` (`c ↦ k − c`). Pulled back through the similarity at `ρ = i`,

```
D_i⁻¹ J D_i = i^k · D J,      D = diag((−1)^c),
```

which commutes with `M_k(−1)`. This is the involution `JD` of [[tower-parity-sectors](pages/tower-parity-sectors.md)], up to the transpose and the scalar `i^k`. Since `(D_i⁻¹ J D_i)² = J² = I`, `(DJ)² = i^{−2k} I = (−1)^k I`. For even `k`, `DJ` is a real involution and `char_k` splits over `Q` into the characteristic polynomials of its two eigenspaces. For odd `k`, `DJ` squares to `−I`, its eigenvalues are `±i`, and `char_k` splits over `Q(i)` into two complex-conjugate factors of degree `(k+1)/2`, so `char_k` is a norm from `Q(i)`. Over `Q`, `char_k` is irreducible for odd `k ≤ 31` (computed) and for every `k = 2^m − 1` ([[char-k-eisenstein-at-two](pages/char-k-eisenstein-at-two.md)]). For `k ≤ 11` the irreducible factors of `char_k` have degrees `[2], [1, 2], [4], [2, 3], [6], [3, 4], …` over `Q` and `[1, 1], [1, 2], [2, 2], [2, 3], [3, 3], [3, 4], …` over `Q(i)` (computed). At `k = 1`, `K(i) = [[1, i], [i, 1]]` has eigenvalues `1 ± i`, which give `P(1, L) = Re((1+i)^{L+1})`.

## 4. The symbol is the Poisson kernel

For `|ρ| < 1`, `K(ρ)` is the `(k+1) × (k+1)` section of the Toeplitz operator with symbol

```
P_ρ(θ) = Σ_m ρ^{|m|} e^{imθ} = (1 − ρ²) / (1 − 2ρ cos θ + ρ²),                              (6)
```

the Poisson kernel of the unit disk at radius `ρ`. For real `0 < ρ < 1` the matrix is real symmetric, and for a vector `v`, `vᵀ K(ρ) v = (1/2π) ∫ P_ρ(θ) |Σ_a v_a e^{iaθ}|² dθ ≤ max P_ρ · |v|²`, so its largest eigenvalue is at most `P_ρ(0) = (1 + ρ)/(1 − ρ)`. The computed largest eigenvalues at size 400 approach that bound: `1.85707` at `t = 0.09` (bound `1.85714`), `2.99964` at `t = 0.25` (bound 3), and `5.66402` at `t = 0.49` (bound `5.66667`). So the towers of any height on a base of length `w`, weighted by `t^{blocks}` with `0 < t < 1`, grow like `((1 + √t)/(1 − √t))^w`, in agreement with the first singularity of the generating function in section 5.

At `ρ = i` the closed form of Equation (6) gives `P_i(θ) = 2/(−2i cos θ) = i sec θ`, purely imaginary and unbounded, and the sections `K(i)` are complex symmetric, not normal, so the symbol does not bound their spectra. The largest modulus of an eigenvalue of `K(i)` grows with the size:

| size `k + 1` | 2 | 3 | 4 | 5 | 6 | 7 | 10 | 20 | 40 | 80 | 160 | 320 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| max `\|λ\|` | `√2` | 2 | 2.1928 | 2.7963 | 2.8920 | 3.5098 | 4.156 | 6.936 | 11.81 | 20.43 | 35.87 | 63.73 |

The first six entries are the growth constants `ρ_k` of `P(k, ·)` for `k = 1, …, 6`, with `ρ_6 = 2ψ²` for the plastic number `ψ` ([[signed-tower-count](pages/signed-tower-count.md)], [[castle-graph-spectral-radius](pages/castle-graph-spectral-radius.md)]). They were computed as `λ = 1/μ` from the eigenvalues `μ` of the tridiagonal `(E_∂ − i·A_path)/2`. From size 40 to 320 the ratio at each doubling is `1.73`, `1.76`, `1.78`, against the factor 2 of the unsigned eigenvalue `k + 1`; [[generating-function-gallery](pages/generating-function-gallery.md)] gives the estimate `ρ_k ~ k/log k`.

## 5. The same √t in the generating function

The castle generating function `B(x, y)` by width `x` and blocks `y` satisfies Deutsch and Elizalde's quadratic `xB² − (1 − x − y − xy)B + xy = 0`,[^3] where `y` is the block weight `t` of section 1. With `y = ρ²` its discriminant factors over `Q(ρ)`:

```
(1 − x − y − xy)² − 4x²y = (1 − ρ²) · [(1 − ρ) − x(1 + ρ)] · [(1 + ρ) − x(1 − ρ)]      (ρ = √y)
```

For `0 < ρ < 1` the first singularity in `x` is `x = (1 − ρ)/(1 + ρ)`, the reciprocal of the maximum `P_ρ(0)` of section 4.

The semi-perimeter grading marks width and blocks with one variable `z`, so that `z` counts the semi-perimeter `s = w + #blocks`: `x = z` and `y = z` for the castles, `y = −z` for the signed count. Writing the product of the two bracketed factors as `(1 − x)² − ρ²(1 + x)²`,

```
unsigned, ρ² = z:     (1 − z)² − z(1 + z)²  =  −(z³ + z² + 3z − 1)
signed,   ρ² = −z:    (1 − z)² + z(1 + z)²  =   z³ + 3z² − z + 1
```

and the full discriminants are `(z − 1)(z³ + z² + 3z − 1)` and `(z + 1)(z³ + 3z² − z + 1)`. These are the two cubics of [[castle-perimeter](pages/castle-perimeter.md)], the first for the castles by semi-perimeter, which grow like `τ^{2s}` with `τ` the tribonacci constant, and the second for the signed count, which grows like `τ^s`. Both are the norm form `(1 − z)² − ρ²(1 + z)²`, at `ρ² = z` and at `ρ² = −z`.

## Summary

In the three gradings the castle sign acts by putting `i` in the place of `√t`:

- **by base length at bounded height** (`P(k, L)`): `M_k(−1)` is similar to `K(i)`, which gives Equations (4) and (5), the involution `DJ` and the splitting of `char_k` over `Q(i)` for odd `k`.
- **on the Motzkin strip**: `I + √t·A_path` at `√t = i` ([[motzkin-castles](pages/motzkin-castles.md)] §3).
- **by semi-perimeter**: the discriminant is a norm form in `ρ = √y`, and the sign is `ρ → iρ`.

## Relation to other pages

- [[motzkin-castles](pages/motzkin-castles.md)] - the Motzkin-path castles (§3), whose tridiagonal transfer matrix is the `|a − b| ≤ 1` part of `K(ρ)`.
- [[signed-tower-count](pages/signed-tower-count.md)] - `P(k, L)`, whose recurrence has the eigenvalues of `K(i)` as roots.
- [[generating-function-gallery](pages/generating-function-gallery.md)] - Equation (5) from the update of `num_k` and `den_k`, and the estimate `ρ_k ~ k/log k`.
- [[tower-parity-sectors](pages/tower-parity-sectors.md)] - the signed transfer matrix `M̃_k` and the involution `JD`, here the KMS reversal pulled back through `D_i`.
- [[castle-graph-spectral-radius](pages/castle-graph-spectral-radius.md)] - the growth constants `ρ_k` of `P(k, ·)` and their degrees over `Q`.
- [[castle-perimeter](pages/castle-perimeter.md)] - the two semi-perimeter cubics, one norm form here.
- [[deutsch-elizalde-2016-bargraphs-cornerless-motzkin](pages/deutsch-elizalde-2016-bargraphs-cornerless-motzkin.md)] - the quadratic in width and blocks whose discriminant factors over `Q(√y)`.
- [[parity-via-roots-of-unity](pages/parity-via-roots-of-unity.md)] - the block-weighted sums at `t = ω^j` for an `m`-th root of unity `ω`, of which the sign is the case `m = 2`.
- [[castle-strip](pages/castle-strip.md)] - transfer matrices whose states are the heights; `M_k(t)` is the matrix of towers with no rule on neighboring columns and a weight `t` per block.
- [[castle-notation](pages/castle-notation.md)] - the symbols `M_k(t)`, `M̃_k`, `K(ρ)`, `A_path` and `E_∂`.

## Footnotes

[^1]: [[project-euler-502-brute-force](pages/project-euler-502-brute-force.md)] §"Column-height encoding" L24 - "= c_1 + \sum_{i=2}^{w} \max(0, c_i - c_{i-1})", the block count from the column heights.
[^2]: [[project-euler-502-solution](pages/project-euler-502-solution.md)] §"Notation" L8, §"The main formula" L52 - "P(k, L) - the signed version of T: sum over the same towers of (-1)^{blocks in tower}" and "P(k, L) = \sum_{towers of height ≤ k above L} (-1)^{blocks in tower}".
[^3]: [[deutsch-elizalde-2016-bargraphs-cornerless-motzkin](pages/deutsch-elizalde-2016-bargraphs-cornerless-motzkin.md)] §2 L99-101 - "Using that B = y(M − 1), which is a consequence of the bijection ∆, we obtain xB^2 − (1 − x − y − xy)B + xy = 0."
[^4]: https://arxiv.org/abs/1804.08140 (abstract read 2026-10-16) - G. Fikioris, "Spectral properties of Kac-Murdock-Szegö matrices with a complex parameter" (2018): "When 0 < ρ < 1, the Kac-Murdock-Szegö matrix K_n(ρ) = [ρ^{|j−k|}]_{j,k=1}^n is a Toeplitz correlation matrix with many applications and very well known spectral properties. We study the eigenvalues and eigenvectors of K_n(ρ) for the general case where ρ is complex".
[^5]: Verified by execution (Python 3.11 with SymPy and NumPy, 2026-10-16): Equation (1) symbolically for `k ≤ 5`; Equation (2) symbolically, and Equation (3) with `det K(i) = 2^k`, for sizes 2 to 8; Equation (4) against the characteristic polynomial of `M_k(−1)` for `k ≤ 10`, and Equation (5) for `k ≤ 9`; `D_i⁻¹ J D_i = i^k DJ` and its commutation with `M_k(−1)` for `k ≤ 8`; the factor degrees over `Q` and `Q(i)` for `k ≤ 11`; the largest eigenvalues at size 400 for `t = 0.09, 0.25, 0.49`; every entry of the table; the discriminant factorization and the two semi-perimeter discriminants.
