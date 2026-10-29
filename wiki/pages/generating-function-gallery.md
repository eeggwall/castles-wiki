---
title: Generating-function gallery for P(k,L)
category: Analyses
summary: The rational generating functions P_k(x) = Σ_L P(k, L) x^L = num_k(x)/den_k(x) of the signed tower count for k ≤ 6, from the update of num_k and den_k; the three-term recurrence den_{k+1} = den_{k−1} − 2x·den_k and its closed form with roots −x ± √(x² + 1); the coefficients −(k+1), 2⌊(k+1)²/4⌋, (−1)^k 2^k and (−1)^{k+1} 2^k of char_k; the eigenvalues for k ≤ 6; the spectral radius ρ_k ≤ k + 1 and the estimate ρ_k ~ k/log k; and the linear recurrences of P(k, ·) for k ≤ 5.
tags: [analysis, castle, generating-functions, c-finite, sympy, verification]
sources: [project-euler-502-solution]
created: 2026-09-14
updated: 2026-10-29
---

# Generating-function gallery for P(k,L)

## Overview

For fixed `k`, the generating function of the signed tower count `P(k, L)` in the base length `L` is rational,

```
P_k(x)  =  Σ_{L≥0} P(k, L) x^L  =  num_k(x) / den_k(x),
```

built from `P_0(x) = 1/(1 − x)`, since `P(0, L) = 1`, by the update[^1]

```
num_k(x)  =  2·den_{k−1}(x) − num_{k−1}(x)
den_k(x)  =  (1 − 2x)·den_{k−1}(x) + x·num_{k−1}(x).
```

The source writes `F_k(x)` for `P_k(x)`. The update is Equation (5) of [[castle-counting-formula](pages/castle-counting-formula.md)], which derives it from the tower grammar. This page lists `num_k` and `den_k` for `k ≤ 6`, the recurrences and closed form they satisfy, the roots of the characteristic polynomials `char_k`, and the linear recurrences of `P(k, ·)`.

## Building the gallery in SymPy

```python
import sympy as sp
x = sp.symbols('x')

num = {0: sp.Integer(1)}
den = {0: 1 - x}
for k in range(1, 9):
    num[k] = sp.expand(2*den[k-1] - num[k-1])
    den[k] = sp.expand(den[k-1]*(1 - 2*x) + x*num[k-1])
```

## The num_k / den_k catalog

| k | num_k(x) | den_k(x) |
|---|---|---|
| 0 | `1` | `1 − x` |
| 1 | `1 − 2x` | `1 − 2x + 2x²` |
| 2 | `1 − 2x + 4x²` | `1 − 3x + 4x² − 4x³` |
| 3 | `1 − 4x + 4x² − 8x³` | `1 − 4x + 8x² − 8x³ + 8x⁴` |
| 4 | `1 − 4x + 12x² − 8x³ + 16x⁴` | `1 − 5x + 12x² − 20x³ + 16x⁴ − 16x⁵` |
| 5 | `1 − 6x + 12x² − 32x³ + 16x⁴ − 32x⁵` | `1 − 6x + 18x² − 32x³ + 48x⁴ − 32x⁵ + 32x⁶` |
| 6 | `1 − 6x + 24x² − 32x³ + 80x⁴ − 32x⁵ + 64x⁶` | `1 − 7x + 24x² − 56x³ + 80x⁴ − 112x⁵ + 64x⁶ − 64x⁷` |

`num_k` has degree `k` and `den_k` degree `k + 1` ([[castle-counting-formula](pages/castle-counting-formula.md)], the Proposition in the section *Signed tower count*). For `k ≤ 40` they have no common factor, so `k + 1` is the order of the shortest linear recurrence of `P(k, ·)`.[^2]

## A three-term recurrence

The update multiplies the vector `(num_k, den_k)` by a matrix of trace `−2x` and determinant `−1`, so by the Cayley-Hamilton theorem, for `k ≥ 1` ([[signed-tower-count](pages/signed-tower-count.md)], the section *Recurrences in L*),

```
den_{k+1}(x)  =  den_{k−1}(x) − 2x·den_k(x).                                  (1)
```

With `char_k(λ) = λ^{k+1} den_k(1/λ)`, the characteristic polynomial of the recurrence of `P(k, ·)`, Equation (1) becomes

```
char_{k+1}(λ)  =  λ²·char_{k−1}(λ) − 2·char_k(λ),        char_0 = λ − 1,   char_1 = λ² − 2λ + 2.      (2)
```

Checked against the catalog:

```python
assert all(sp.expand(den[k+1] - (den[k-1] - 2*x*den[k])) == 0 for k in range(1, 8))
```

## The closed form in k

Equation (1) is a linear recurrence in `k` whose coefficients depend on `x` only. Its characteristic equation is `r² + 2x·r − 1 = 0`, with roots

```
r_±  =  −x ± √(x² + 1),        r_+ · r_−  =  −1,        r_+ + r_−  =  −2x,
```

so for every `k ≥ 0`

```
den_k(x)  =  A(x)·r_+^k + B(x)·r_−^k,                                         (3)
```

with `A` and `B` fixed by `den_0 = 1 − x` and `den_1 = 1 − 2x + 2x²`. Equation (1) is the recurrence of the Pell polynomials in the variable `−x`. Equation (3) agrees with the catalog for `k ≤ 10`.[^2]

**Coefficients of `char_k`.** The coefficients of `den_k` at `x`, `x²`, `x^k` and `x^{k+1}` are the coefficients of `char_k` at `λ^k`, `λ^{k−1}`, `λ` and `1`:

```
char_k(λ)  =  λ^{k+1} − (k + 1)λ^k + 2⌊(k + 1)²/4⌋ λ^{k−1} + ⋯ + (−1)^k 2^k λ + (−1)^{k+1} 2^k.
```

The coefficients `−(k + 1)` and `(−1)^{k+1} 2^k` are proved on [[signed-tower-count](pages/signed-tower-count.md)]. For `2⌊(k + 1)²/4⌋`: the coefficient of `x` in `den_k` is `−(k + 1)`, so Equation (1) gives `e_{k+1} = e_{k−1} + 2(k + 1)` for the coefficient `e_k` of `x²` in `den_k`, and with `e_0 = 0` and `e_1 = 2` this is `e_k = 2⌊(k + 1)²/4⌋`. The coefficient `(−1)^k 2^k` of `λ` is computed: all four agree with `den_k` for `k ≤ 40`.[^2]

## The eigenvalues

The roots of `char_k` are the eigenvalues of the recurrence of `P(k, ·)`, and of the signed transfer matrix `M̃_k` of [[tower-parity-sectors](pages/tower-parity-sectors.md)], whose characteristic polynomial is `char_k` (computed for `k ≤ 16`). Factored over the rationals:

| k | char_k(λ) |
|---|---|
| 1 | `λ² − 2λ + 2` |
| 2 | `(λ − 2)(λ² − λ + 2)` |
| 3 | `λ⁴ − 4λ³ + 8λ² − 8λ + 8` |
| 4 | `(λ² − 2λ + 4)(λ³ − 3λ² + 2λ − 4)` |
| 5 | `λ⁶ − 6λ⁵ + 18λ⁴ − 32λ³ + 48λ² − 32λ + 32` |
| 6 | `(λ³ − 4λ² + 4λ − 8)(λ⁴ − 3λ³ + 8λ² − 4λ + 8)` |

For even `k ≤ 40`, `char_k` has two irreducible factors, of degrees `k/2` and `k/2 + 1`; [[tower-parity-sectors](pages/tower-parity-sectors.md)] derives the factorization for every even `k`, from a symmetry of `M̃_k`, and gives the factors in closed form. For even `k ≤ 40`, `char_k` has exactly one real root, and that root has the largest modulus. For odd `k ≤ 31`, `char_k` is irreducible and has no real root; irreducibility is proved for `k = 2^m − 1` on [[char-k-eisenstein-at-two](pages/char-k-eisenstein-at-two.md)].[^2]

The roots, with `ρ_k` the largest modulus:[^2]

| k | eigenvalues | ρ_k ≈ |
|---|---|---|
| 1 | `1 ± i` | 1.414 |
| 2 | `2`, `(1 ± i√7)/2` | 2 |
| 3 | `1.786 ± 1.272i`, `0.214 ± 1.272i` | 2.193 |
| 4 | `2.796`, `1 ± √3 i`, `0.102 ± 1.192i` | 2.796 |
| 5 | `2.464 ± 1.514i`, `0.480 ± 1.650i`, `0.055 ± 1.137i` | 2.892 |
| 6 | `3.510`, `1.467 ± 2.107i`, `0.245 ± 1.490i`, `0.033 ± 1.101i` | 3.510 |

`ρ_6 = 2ψ²`, with `ψ` the plastic number ([[signed-tower-count](pages/signed-tower-count.md)], [[plastic-number](pages/plastic-number.md)]). Every entry of `M̃_k` is `±1`, so every eigenvalue has modulus at most the largest absolute row sum: `ρ_k ≤ k + 1`, the base of the unsigned count `T(k, L) = (k + 1)^L`. For `k ≤ 40` every root of `char_k` is a pole of `P_k(x)`, so `limsup_L |P(k, L)|^{1/L} = ρ_k`.

## Growth of ρ_k

Equation (2) is a linear recurrence in `k` with characteristic equation `r² + 2r − λ² = 0`, so

```
char_k(λ)  =  A(λ)·r_+(λ)^k + B(λ)·r_−(λ)^k,        r_±(λ)  =  −1 ± √(1 + λ²),
```

with `A`, `B` fixed by `char_0` and `char_1`. A root of `char_k` therefore satisfies the exact equation `(r_−/r_+)^k = −A/B`, which the computed `ρ_k` satisfy. For large real `λ`, `A ≈ λ`, `B ≈ −1/(4λ)` and `r_−/r_+ ≈ −(λ + 1)/(λ − 1)`, so for even `k` the real root satisfies approximately

```
( (ρ + 1)/(ρ − 1) )^k  ≈  4ρ²,        that is,        ρ · log(2ρ)  ≈  k,
```

which gives the estimate `ρ_k ~ k/log k`. The approximate equation gives `25.46` at `k = 100`, against `ρ_100 = 25.64`. By the estimate, the ratio `ρ_k · log k / k` is about `log k / log(2ρ_k)`, which is still `1.17` at `k = 100`:[^2]

| k | 1 | 2 | 4 | 8 | 10 | 20 | 50 | 100 |
|---|---|---|---|---|---|---|---|---|
| ρ_k | 1.414 | 2.000 | 2.796 | 4.174 | 4.804 | 7.661 | 14.98 | 25.64 |
| ρ_k·log k / k | 0 | 0.693 | 0.969 | 1.085 | 1.106 | 1.147 | 1.172 | 1.181 |

For odd `k` the roots of largest modulus are a complex pair, of modulus slightly less than at the neighboring even `k`: `ρ_99 = 24.45` and `ρ_101 = 24.85`, against `ρ_100 = 25.64`.

## The linear recurrences

Writing `den_k = 1 + d_1 x + ⋯ + d_{k+1} x^{k+1}` gives the recurrence `P(k, L) = −d_1 P(k, L−1) − ⋯ − d_{k+1} P(k, L−k−1)` for `L ≥ k + 1`:

```
P(1,L) = 2·P(1,L−1) − 2·P(1,L−2)
P(2,L) = 3·P(2,L−1) − 4·P(2,L−2) + 4·P(2,L−3)
P(3,L) = 4·P(3,L−1) − 8·P(3,L−2) + 8·P(3,L−3) − 8·P(3,L−4)
P(4,L) = 5·P(4,L−1) − 12·P(4,L−2) + 20·P(4,L−3) − 16·P(4,L−4) + 16·P(4,L−5)
P(5,L) = 6·P(5,L−1) − 18·P(5,L−2) + 32·P(5,L−3) − 48·P(5,L−4) + 32·P(5,L−5) − 32·P(5,L−6)
```

The first coefficient is `k + 1`, the sum of the eigenvalues, and the last is `(−1)^k 2^k`, the negative of the constant term of `char_k`; the eigenvalues multiply to `2^k` ([[signed-tower-count](pages/signed-tower-count.md)], section *Recurrences in L*).[^3]

## Verification: the series equals P(k,L)

The coefficients of `num_k/den_k` agree with `P(k, L)` computed by the column-height dynamic program, which does not use the update:

```python
def P_table(K, Lmax):                      # exact integers, column-height DP
    P = [[0]*(Lmax+1) for _ in range(K+1)]
    for k in range(K+1):
        F = [0]*(k+1); F[0] = 1; P[k][0] = 1
        for L in range(1, Lmax+1):
            G = [0]*(k+1)
            for b in range(k+1):
                G[b] = sum(F[a]*(1 if a <= b else (-1)**(a-b)) for a in range(k+1))
            F = G
            P[k][L] = sum(F[b]*((-1)**b) for b in range(k+1))
    return P

P = P_table(8, 24)
for k in [0, 1, 2, 3, 4, 5, 8]:
    ser = sp.series(num[k]/den[k], x, 0, 21).removeO()
    assert all(sp.nsimplify(ser.coeff(x, L)) == P[k][L] for L in range(21))
    print(f"k={k}: num_k/den_k == P(k,L) for L=0..20")
```

The check includes `k = 8`, beyond the catalog.

## Appearances in Sources

- [[project-euler-502-solution](pages/project-euler-502-solution.md)] - the update of `num_k` and `den_k`, written for `F_k(x)`, in the rational-function path.

## Related Concepts

- [[castle-counting-formula](pages/castle-counting-formula.md)] - the derivation of `P_k(x)` from the tower grammar and the degrees of `num_k` and `den_k`.
- [[signed-tower-count](pages/signed-tower-count.md)] - the values of `P(k, L)`, the proofs of the coefficients of `char_k`, and the case `k = 1`.
- [[tower-parity-sectors](pages/tower-parity-sectors.md)] - the factorization of `char_k` for even `k` by the parity of the last column, its closed-form factors `H_d` and `V_d`, and `ρ_6 = 2ψ²`.
- [[castle-sign-kms-matrix](pages/castle-sign-kms-matrix.md)] - a second derivation of Equation (2): the signed transfer matrix is diagonally similar to the Kac-Murdock-Szegő matrix `K(i)`, whose inverse is tridiagonal, so `char_k` is a continuant.
- [[recurrence-discovery](pages/recurrence-discovery.md)] - the orders of the recurrences of `P` found by Berlekamp-Massey: `k + 1` in `L`, and `2L − 2` in `k` for `4 ≤ L ≤ 12`, which [[signed-tower-k-direction](pages/signed-tower-k-direction.md)] proves for every `L ≥ 4` from the roots `r_±` of Equation (1).
- [[signed-tower-k-direction](pages/signed-tower-k-direction.md)] - the recurrences of `P(·, L)` in `k`, whose eigenvalues are `±1`.
- [[closed-form-hunting](pages/closed-form-hunting.md)] - the closed forms of `P(k, 2)` and `P(k, 3)` in `k`.
- [[castle-count-algorithms](pages/castle-count-algorithms.md)] - the extraction of `P(h−1, w)` from `num_{h−1}/den_{h−1}` at the Project Euler targets.
- [[generating-functions](pages/generating-functions.md)] - rational generating functions and the linear recurrences of their coefficients.
- [[symbolic-method](pages/symbolic-method.md)] - the dictionary from combinatorial specifications to generating functions, which turns the tower grammar into the equation for `P_k(x)`.
- [[mod-p-observatory](pages/mod-p-observatory.md)] - the polynomials `char_k` reduced modulo `p`, whose roots set the periods of `P(k, ·) mod p`.
- [[new-sequence-fw3](pages/new-sequence-fw3.md)] - `Σ_w A^e(w, 3) x^w = ½(1/(1 − 3x) − 1/(1 − 2x) − P_2(x) + P_1(x))`, from `num_1/den_1` and `num_2/den_2`.
- [[algebraic-transcendental-wall](pages/algebraic-transcendental-wall.md)] - the estimate `ρ_k ~ k/log k`.
- [[oeis-mining-pe502](pages/oeis-mining-pe502.md)] - the castle counts matched against the OEIS, among them the characteristic polynomials `char_1` to `char_5`.

## Footnotes

[^1]: [[project-euler-502-solution](pages/project-euler-502-solution.md)] §"The rational-function path (h ≤ 15000)" L124-138 - "F_k(x) = ∑_L P(k, L) x^L ... F_0(x) = 1/(1 - x) ... num_k(x) = 2·den_{k-1}(x) - num_{k-1}(x); den_k(x) = den_{k-1}(x)·(1 - 2x) + num_{k-1}(x)·x; F_k(x) = num_k(x)/den_k(x)."
[^2]: Verified by execution (Python 3.11 with SymPy, NumPy and mpmath, 2026-10-16): the catalog for `k ≤ 6`; `gcd(num_k, den_k) = 1` for `k ≤ 40` ([[castle-counting-formula](pages/castle-counting-formula.md)]); Equation (3) against `den_k` for `k ≤ 10`; the four coefficients of `char_k` for `k ≤ 40`; `char(M̃_k) = char_k` for `k ≤ 16`; two irreducible factors for even `k ≤ 40`, one real root for even `k ≤ 40`, irreducible with no real root for odd `k ≤ 31`; the root of largest modulus real and in the even-last-column sector for even `k ≤ 40` ([[tower-parity-sectors](pages/tower-parity-sectors.md)]); the eigenvalue table; `ρ_k` from the eigenvalues of `M̃_k` for the listed `k` and for `k = 9, 11, 49, 51, 99, 101`; the exact equation at `k = 8, 20, 100`; the approximate equation at the even `k` of the table; the series of `Σ_w A^e(w, 3) x^w` against enumeration for `w ≤ 10`.
[^3]: Verified by execution (Python 3.11 with SymPy, 2026-10-25): from the update of `num_k` and `den_k`, for `k ≤ 20`, `char_k` is monic of degree `k + 1` with coefficient `−(k + 1)` of `λ^k` and constant term `(−1)^{k+1} 2^k`; the recurrences listed for `k ≤ 3` hold for the brute-force values of `P(k, L)`.
