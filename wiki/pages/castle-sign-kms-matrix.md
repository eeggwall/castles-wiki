---
title: The castle sign is a KMS matrix at ρ = i
category: Analyses
summary: Weight each block by t. The block-weighted tower transfer matrix M_k(t) (tower heights 0..k, entry t^max(0, b-a)) is diagonally similar to the Kac-Murdock-Szegő matrix K(ρ) = (ρ^|a-b|) with ρ = √t, so t only ever enters as √t. Unsigned (ρ = 1) K is the all-ones matrix, rank one, giving (k+1)^L. Signed (ρ = i) K(i) has the tridiagonal inverse (E_∂ - i A_path)/2 with a vanishing interior diagonal, which yields char_k = ½ det(λE_∂ - 2I - iλA_path) and the wiki's recurrence char_{k+1} = λ² char_{k-1} - 2 char_k. Reversal symmetry of K pulled back through the similarity is the sector involution of tower-parity-sectors, with (JD)² = (-1)^k as i^(2k). The Toeplitz symbol is the Poisson kernel, so castles by width with block weight t grow like ((1+√t)/(1-√t))^w, the same Cayley factors that split the Deutsch-Elizalde discriminant over Q(√t); at ρ → iρ those factors turn the unsigned semi-perimeter cubic (τ²) into the signed one (τ).
tags: [analysis, castle, sign, parity, transfer-matrix, toeplitz, kms-matrix, poisson-kernel, gaussian-integers, cayley-transform, characteristic-polynomial, signed-tower-count, semi-perimeter, motzkin]
sources: [project-euler-502-solution, project-euler-502-brute-force, deutsch-elizalde-2016-bargraphs-cornerless-motzkin]
created: 2026-09-27
updated: 2026-09-28
---

# The castle sign is a KMS matrix at ρ = i

## Overview

On the Motzkin-path castle the parity sign `(−1)^blocks` acts by putting `√t = i` into the up-step weight: the growth constant `1 ± 2√t` becomes `1 ± 2i`, and the bounded-height spectrum `1 + 2cos(πj/(h+1))` becomes `1 + 2i·cos(πj/(h+1))` ([[motzkin-castles](pages/motzkin-castles.md)] §3). The signed tower count has `P(1, L) = Re((1+i)^{L+1})`, another Gaussian value ([[signed-tower-count](pages/signed-tower-count.md)]). The same holds for **unrestricted** skylines at any height bound: the block weight `t` enters the transfer matrix only through `√t`, via a classical structured matrix, and the sign is the point `√t = i` of that family. Everything below was checked by execution (SymPy and NumPy, 2026-09-27); the checks are listed with each claim.

## 1. The transfer matrix is a KMS matrix

A tower of height `≤ k` on a base of length `L` is a sequence of column heights `c_1, …, c_L ∈ {0, …, k}`. Its block count is the total rise from height 0,[^1] so a weight `t` per block factors over consecutive columns:

```
M_k(t)[a][b] = t^max(0, b − a)        (a, b = 0, …, k: tower heights, so size k + 1 = castle height bound).
```

Summing `t^blocks` over all towers of height `≤ k` on a base of length `L` gives `e_0ᵀ M_k(t)ᴸ 𝟙`.

At `t = 1` that sum is the tower count `T(k, L) = (k+1)^L` and at `t = −1` it is the signed tower count `P(k, L) = Σ (−1)^blocks` over towers of height `≤ k` above a length-`L` block,[^2] in the tower-height-first order of [[castle-notation](pages/castle-notation.md)]. The code reproduces `P(1, ·) = 1, 0, −2, −4, −4, 0, 8, 16` and `P(2, ·) = 1, 1, 3, 9, 19, 33, 59, 121`, the rows on [[signed-tower-count](pages/signed-tower-count.md)]. (The signed matrix `M_k` of [[tower-parity-sectors](pages/tower-parity-sectors.md)] counts descents instead of rises; `M_k(−1)` is its transpose, with the same characteristic polynomial.)

Conjugate by `D_ρ = diag(1, ρ, ρ², …, ρ^k)` with `ρ² = t`. An entry above the diagonal becomes `t^{b−a} ρ^{a−b} = ρ^{b−a}`, and one below becomes `ρ^{a−b}`. So

```
D_ρ M_k(ρ²) D_ρ⁻¹ = K(ρ),      K(ρ)[a][b] = ρ^|a − b|,
```

the **Kac-Murdock-Szegő (KMS) matrix**, the symmetric Toeplitz matrix of an AR(1) correlation (checked symbolically for sizes up to 6). **The block weight only ever enters as `ρ = √t`.** The two castle weights are two special points of one family:

- **unsigned, `ρ = 1`.** `K(1)` is the all-ones matrix, which has rank one. That is why the unsigned tower count is the pure power `(k+1)^L` ([[castle-counting-formula](pages/castle-counting-formula.md)]).
- **signed, `ρ = i`.** `K(i)[a][b] = i^|a−b|`: a complex symmetric Toeplitz matrix. The signed tower count is `P(k, L) = e_0ᵀ D_i⁻¹ K(i)ᴸ D_i 𝟙`, so its eigenvalues are those of `K(i)`.

The Motzkin strip of [[motzkin-castles](pages/motzkin-castles.md)] §3 is the tridiagonal part of the same matrix: keeping only `|a − b| ≤ 1` gives `I + ρ·A_path`, with `A_path` the adjacency matrix of the path on the heights (not the castle count `A(w, h)`) and eigenvalues `1 + 2ρ·cos(πj/(h+1))` for castle height `h` (`h` states). Both the 1-smooth strip and the unrestricted castle are `ρ = √t` Toeplitz objects, and the sign is `ρ = i` in both.

## 2. At ρ = i the inverse loses its diagonal

A KMS matrix has a tridiagonal inverse (checked symbolically in `ρ` for sizes up to 6):

```
K(ρ)⁻¹ = (1/(1 − ρ²)) · [ diag(1, 1 + ρ², …, 1 + ρ², 1) − ρ·A_path ].
```

At `ρ = 1` the prefactor blows up, since the all-ones matrix is singular. At `ρ = i` the interior diagonal `1 + ρ²` vanishes:

```
K(i)⁻¹ = (E_∂ − i·A_path)/2,      E_∂ = diag(1, 0, …, 0, 1),      det K(i) = 2^k
```

(checked for sizes up to 8 and 9). So the inverse of the signed transfer matrix is a path graph with imaginary edge weights and a loop at each end. The characteristic polynomial follows by clearing denominators:

```
char_k(λ) = ½ · det( λE_∂ − 2I − iλ·A_path )           (checked for k ≤ 8),
```

a tridiagonal determinant with diagonal `(λ − 2, −2, …, −2, λ − 2)` and off-diagonal `−iλ`. Expanding such a continuant along the interior gives `D_m = −2·D_{m−1} − (−iλ)²·D_{m−2} = −2·D_{m−1} + λ²·D_{m−2}`, which is the recurrence

```
char_{k+1}(λ) = λ²·char_{k−1}(λ) − 2·char_k(λ)
```

that [[generating-function-gallery](pages/generating-function-gallery.md)] obtained by eliminating `num_k` from the rational-function recursion, and whose roots `r_± = −1 ± √(1 + λ²)` give its Pell/Chebyshev closed form. The characteristic polynomials of `M_k(−1)` satisfy it for `k = 1..7` (checked). The `i` in the off-diagonal squares to `−1`, which turns the Chebyshev recurrence of a real path graph into this Pell-type one.

## 3. The sector involution is the KMS reversal symmetry

`K(ρ)` is symmetric Toeplitz, so it commutes with the reversal `J` (`c ↦ k − c`). Pull `J` back through the similarity at `ρ = i`:

```
D_i⁻¹ J D_i = i^k · D J,      D = diag((−1)^c),
```

and this commutes with `M_k(−1)` (both checked for sizes up to 9). That is the involution `JD` of [[tower-parity-sectors](pages/tower-parity-sectors.md)], up to the transpose convention and the scalar: the persymmetry of the KMS matrix. The scalar gives the sector dichotomy: `(D_i⁻¹ J D_i)² = I`, so `(DJ)² = i^{−2k} = (−1)^k`. For even `k` the symmetry is a real involution and `char_k` splits over `Q` into the two parity sectors. For odd `k` it squares to `−1`, and `char_k` splits over `Q(i)` into two conjugate halves of degree `(k+1)/2` (over `Q` it is irreducible for odd `k ≤ 31` by SymPy and for all `k = 2^m − 1` by [[char-k-eisenstein-at-two](pages/char-k-eisenstein-at-two.md)]). SymPy confirms both patterns for `k ≤ 11` (over `Q`: `[1,2], [4], [2,3], [6], …`; over `Q(i)`: `[1,1], [1,2], [2,2], [2,3], [3,3], …`). The Gaussian integers in `P(1, L)` and the Gaussian norm form of odd-`k` `char_k` both come from this `i`, the square root of the block sign.

## 4. The symbol is the Poisson kernel

`K(ρ)` is the `n × n` section of the Toeplitz operator whose symbol is

```
Σ_m ρ^|m| e^{imθ} = (1 − ρ²) / (1 − 2ρ cos θ + ρ²) = P_ρ(θ),
```

the Poisson kernel of the unit disk at radius `ρ`. For real `0 < ρ < 1` the matrix is real symmetric, and its largest eigenvalue tends to the symbol's maximum `P_ρ(0) = (1 + ρ)/(1 − ρ)`. So **castles by width, with every block weighted by `0 < t < 1` and no height bound, grow like `((1 + √t)/(1 − √t))^w`**. Numerically, the largest eigenvalue at height cutoff 400 is `1.85707` at `t = 0.09` (predicted `1.85714`), `2.99964` at `t = 0.25` (predicted `3`), and `5.66402` at `t = 0.49` (predicted `5.66667`).

At `ρ = i` the formula gives `P_i(θ) = 2/(−2i cos θ) = i·sec θ`: purely imaginary and unbounded. The finite sections `K(i)` are complex symmetric, not normal, so the symbol does not fix their spectra. Still, the dominant eigenvalue modulus of `K(i)` grows without bound in the height:

| size `k + 1` | 2 | 3 | 4 | 5 | 6 | 7 | 10 | 20 | 40 | 80 | 160 | 320 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| max `\|λ\|` | `√2` | 2 | 2.1928 | 2.7963 | 2.8920 | 3.5098 | 4.156 | 6.936 | 11.81 | 20.43 | 35.87 | 63.73 |

The first six entries are the `P(k, ·)` growth constants `√2, 2, 2.193, 2.796, 2.892, 2ψ²` on [[castle-sequence-catalogue](pages/castle-sequence-catalogue.md)], computed there from `char_k`. Here they come from the tridiagonal `(E_∂ − i·A_path)/2` in the form `λ = 2/μ`, which is numerically stable. The growth is sublinear, about ×1.77 per doubling of the height between 80 and 320, against the linear `k + 1` of the unsigned rank-one matrix, and consistent with the `ρ_k ~ k/log k` asymptotic derived on [[generating-function-gallery](pages/generating-function-gallery.md)].

## 5. The same √t in the generating function

The castle GF by width `x` and blocks `y` satisfies Deutsch and Elizalde's quadratic `xB² − (1 − x − y − xy)B + xy = 0`,[^3] where `y` is the same block weight as `t` above. With `y = ρ²` its discriminant factors completely over `Q(ρ)`:

```
(1 − x − y − xy)² − 4x²y = (1 − ρ²) · [(1 − ρ) − x(1 + ρ)] · [(1 + ρ) − x(1 − ρ)]      (ρ = √y)
```

(checked symbolically). The first singularity in `x` is `x = (1 − ρ)/(1 + ρ)`, the **Cayley transform** of `ρ`. That is the reciprocal of the Poisson-kernel maximum of §4, so the transfer matrix and the generating function involve the same `ρ = √y`.

The semi-perimeter grading marks width and blocks with one variable, `x = z` and `y = ±z` (so `z` counts the semi-perimeter `s = w + #blocks`), and the sign is again `ρ → iρ`:

```
unsigned, ρ = √z:    [(1 − ρ) − z(1 + ρ)]·[(1 + ρ) − z(1 − ρ)] = (1 − z)² − z(1 + z)² = −(z³ + z² + 3z − 1)
signed,   ρ = i√z:   [(1 − ρ) − z(1 + ρ)]·[(1 + ρ) − z(1 − ρ)] = (1 − z)² + z(1 + z)² =  z³ + 3z² − z + 1
```

The full discriminants are `(z − 1)(z³ + z² + 3z − 1)` and `(z + 1)(z³ + 3z² − z + 1)` (SymPy). These are the two cubics [[castle-perimeter](pages/castle-perimeter.md)] found separately, the first giving castles by semi-perimeter growth `τ²` (τ the tribonacci constant) and the second giving the signed count growth `τ`. They are one norm form, `(1 − z)² − ρ²(1 + z)²`, evaluated at `ρ² = z` and at `ρ² = −z`.

## Summary

For the three gradings the wiki uses, the castle sign acts by putting `i` into the up-step weight:

- **by base length at bounded height** (`P(k, L)`): the eigenvalues are those of `K(√t)` at `√t = i`; the recurrence in `k`, the sector split, and the odd-`k` norm form all follow from `K(i)`.
- **on the 1-smooth strip**: `I + √t·A_path` at `√t = i` ([[motzkin-castles](pages/motzkin-castles.md)] §3).
- **by semi-perimeter**: the discriminant is a norm form in `ρ = √y`, and the sign is `ρ → iρ`.

Open: a closed form for the eigenvalues of `K(i)` (for real `ρ` they lie in the range of the Poisson kernel and can be written `P_ρ(θ_j)` for real `θ_j`; at `ρ = i` the symbol is imaginary while the eigenvalues are not, so the `θ_j` must leave the real line; the classical KMS spectral theory for complex `ρ` was not read), a proof of the growth rate of the dominant `|λ|` in `k`, and whether the other castle statistics (area, peaks) enter through square roots in the same way.

## Relation to other pages

- [[motzkin-castles](pages/motzkin-castles.md)] - the 1-smooth case (§3) that raised the question; its tridiagonal matrix is the `|a − b| ≤ 1` part of `K(ρ)`.
- [[signed-tower-count](pages/signed-tower-count.md)] - `P(k, L)`, whose eigenvalues are those of `K(i)`.
- [[generating-function-gallery](pages/generating-function-gallery.md)] - the `k`-recurrence of `char_k`, derived here from the tridiagonal inverse.
- [[tower-parity-sectors](pages/tower-parity-sectors.md)] - the involution `JD`, identified here as the KMS reversal symmetry pulled back through `D_i`.
- [[castle-perimeter](pages/castle-perimeter.md)] - the two semi-perimeter cubics, unified here as one norm form.
- [[deutsch-elizalde-2016-bargraphs-cornerless-motzkin](pages/deutsch-elizalde-2016-bargraphs-cornerless-motzkin.md)] - the (width, blocks) quadratic whose discriminant factors over `Q(√y)`.
- [[castle-sign](pages/castle-sign.md)] / [[parity-via-roots-of-unity](pages/parity-via-roots-of-unity.md)] - the sign as a character; the matrix involves the character's square root. The roots-of-unity counts `P_j(k, L)` are the block-weighted sum at `t = ω^j`, and that page's `P_j(1, L) = ½[(1 + √ω^j)^{L+1} + (1 − √ω^j)^{L+1}]` already shows the weight entering as its square root at `k = 1`.
- [[castle-strip](pages/castle-strip.md)] - transfer matrices whose states are the heights; `M_k(t)` is the unrestricted strip with block weight `t`.
- [[castle-notation](pages/castle-notation.md)] - the symbol conventions; `M_k(t)`, `K(ρ)`, `A_path`, `E_∂` are recorded there.

## Footnotes

[^1]: [[project-euler-502-brute-force](pages/project-euler-502-brute-force.md)] §"brute" L24 - "= c_1 + \sum_{i=2}^{w} \max(0, c_i - c_{i-1})", the column-height block-count formula.
[^2]: [[project-euler-502-solution](pages/project-euler-502-solution.md)] §"Notation" L8, §"The main formula" L52 - "P(k, L) - the signed version of T: sum over the same towers of (-1)^{blocks in tower}" and "P(k, L) = \sum_{towers of height ≤ k above L} (-1)^{blocks in tower}".
[^3]: [[deutsch-elizalde-2016-bargraphs-cornerless-motzkin](pages/deutsch-elizalde-2016-bargraphs-cornerless-motzkin.md)] p.3 §2 L99-101 - "Using that B = y(M − 1), which is a consequence of the bijection ∆, we obtain xB^2 − (1 − x − y − xy)B + xy = 0."
