---
title: Generating-function gallery for P(k,L)
category: Analyses
summary: The rational generating functions F_k(x) = num_k/den_k of P(k,L) in L, built by a two-line recurrence — a num/den catalogue, the denominator roots (eigenvalues), and the C-finite recurrences.
tags: [analysis, castle, generating-functions, c-finite, sympy, verification]
sources: [project-euler-502-solution, oeis-mining-pe502]
created: 2026-09-14
updated: 2026-09-14
---

# Generating-function gallery for P(k,L)

## Overview

For fixed `k`, the ordinary generating function of `P(k,L)` in the width `L` is rational,

```
F_k(x) = Σ_L P(k,L) x^L = num_k(x) / den_k(x),
```

built level-by-level from `F_0(x) = 1/(1−x)` (the height-0 tower is empty, `P(0,L) = 1`) by the two-line recurrence[^1]

```
num_k(x) = 2·den_{k−1}(x) − num_{k−1}(x)
den_k(x) = den_{k−1}(x)·(1 − 2x) + num_{k−1}(x)·x.
```

This recurrence *is* the generalization: a single pass builds numerator and denominator for every `k`. The gallery catalogues them, their roots, and the C-finite recurrences they encode — all built and checked with SymPy.

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

## The num_k / den_k catalogue

| k | num_k(x) | den_k(x) |
|---|---|---|
| 0 | `1` | `1 − x` |
| 1 | `1 − 2x` | `1 − 2x + 2x²` |
| 2 | `1 − 2x + 4x²` | `1 − 3x + 4x² − 4x³` |
| 3 | `1 − 4x + 4x² − 8x³` | `1 − 4x + 8x² − 8x³ + 8x⁴` |
| 4 | `1 − 4x + 12x² − 8x³ + 16x⁴` | `1 − 5x + 12x² − 20x³ + 16x⁴ − 16x⁵` |
| 5 | `1 − 6x + 12x² − 32x³ + 16x⁴ − 32x⁵` | `1 − 6x + 18x² − 32x³ + 48x⁴ − 32x⁵ + 32x⁶` |
| 6 | `1 − 6x + 24x² − 32x³ + 80x⁴ − 32x⁵ + 64x⁶` | `1 − 7x + 24x² − 56x³ + 80x⁴ − 112x⁵ + 64x⁶ − 64x⁷` |

Each `den_k` has degree `k+1` — the order of the C-finite recurrence (see [[recurrence-discovery](pages/recurrence-discovery.md)]).

## Denominator roots (the eigenvalues)

The recurrence's eigenvalues are the roots of the **characteristic polynomial** `char_k(λ) = λ^{k+1} den_k(1/λ)` (the reversed denominator). SymPy factors them:

| k | char_k(λ) (factored) |
|---|---|
| 1 | `λ² − 2λ + 2` |
| 2 | `(λ − 2)(λ² − λ + 2)` |
| 3 | `λ⁴ − 4λ³ + 8λ² − 8λ + 8` |
| 4 | `(λ² − 2λ + 4)(λ³ − 3λ² + 2λ − 4)` |
| 5 | `λ⁶ − 6λ⁵ + 18λ⁴ − 32λ³ + 48λ² − 32λ + 32` |
| 6 | `(λ³ − 4λ² + 4λ − 8)(λ⁴ − 3λ³ + 8λ² − 4λ + 8)` |

**Structure.** For **even `k`** the polynomial factors into two factors of degrees `k/2` and `k/2 + 1` — one of them carrying the single real root that dominates the growth. For **odd `k`** it is irreducible over ℚ, so *every* eigenvalue is non-real. The roots (eigenvalues), with the dominant modulus ρ_k = max|λ|:

| k | eigenvalues | ρ_k ≈ |
|---|---|---|
| 1 | `1 ± i` | 1.414 |
| 2 | `2`, `(1 ± i√7)/2` | 2 |
| 3 | `1.786 ± 1.272i`, `0.214 ± 1.272i` | 2.193 |
| 4 | `2.796`, `1 ± √3 i`, `0.102 ± 1.192i` | 2.796 |
| 5 | `2.464 ± 1.514i`, `0.480 ± 1.650i`, `0.055 ± 1.137i` | 2.892 |
| 6 | `3.510`, `1.467 ± 2.107i`, `0.245 ± 1.490i`, `0.033 ± 1.101i` | 3.510 |

`ρ_k ≤ k+1` (the unsigned count `T(k,L) = (k+1)^L` bounds the signed one), with equality never reached — the sign always suppresses the largest tower term.

## The C-finite recurrences

Writing `den_k = 1 + d_1 x + ⋯ + d_{k+1} x^{k+1}` gives the recurrence `P(k,L) = −d_1 P(k,L−1) − ⋯ − d_{k+1} P(k,L−k−1)`:

```
P(1,L) = 2·P(1,L−1) − 2·P(1,L−2)
P(2,L) = 3·P(2,L−1) − 4·P(2,L−2) + 4·P(2,L−3)
P(3,L) = 4·P(3,L−1) − 8·P(3,L−2) + 8·P(3,L−3) − 8·P(3,L−4)
P(4,L) = 5·P(4,L−1) − 12·P(4,L−2) + 20·P(4,L−3) − 16·P(4,L−4) + 16·P(4,L−5)
P(5,L) = 6·P(5,L−1) − 18·P(5,L−2) + 32·P(5,L−3) − 48·P(5,L−4) + 32·P(5,L−5) − 32·P(5,L−6)
```

The first coefficient is `k+1` (the sum of the eigenvalues), and the last is `(−1)^{k−1} 2^k` — the product `2^k` of the eigenvalues, times the sign `(−1)^{k−1}` — the two invariants recorded on [[signed-tower-count](pages/signed-tower-count.md)].[^2]

## Verification: the series equals P(k,L)

SymPy confirms each `num_k/den_k` expands to the actual tower count, computed independently by the column-height DP:

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
    print(f"k={k}: num_k/den_k == P(k,L) for L=0..20  ✓")
```

This checks `k = 8` too — the recurrence, not the hand-listed table, is the source of truth, so the generalization is exercised rather than assumed.

## Appearances in Sources

- [[project-euler-502-solution](pages/project-euler-502-solution.md)] — the rational-function path and the `num_k`/`den_k` recurrence.
- [[oeis-mining-pe502](pages/oeis-mining-pe502.md)] — the `P(k,·)` C-finite family and its characteristic polynomials.

## Related Concepts

- [[signed-tower-count](pages/signed-tower-count.md)] — the characteristic polynomials and their coefficient invariants.
- [[recurrence-discovery](pages/recurrence-discovery.md)] — the orders (k+1 in L, 2L−2 in k) these recurrences realize.
- [[closed-form-hunting](pages/closed-form-hunting.md)] — the k-direction closed forms the eigenvalues would have to reproduce.
- [[castle-counting-formula](pages/castle-counting-formula.md)] / [[castle-count-algorithms](pages/castle-count-algorithms.md)] — where `num_k/den_k` is evaluated at scale.
- [[generating-functions](pages/generating-functions.md)] — the ordinary-GF toolkit behind a linear recurrence ⇒ rational GF.

## Footnotes

[^1]: [[project-euler-502-solution](pages/project-euler-502-solution.md)] §"The rational-function path (h ≤ 15000)" L124-138 — "F_k(x) = ∑_L P(k, L) x^L ... F_0(x) = 1/(1 - x) ... num_k(x) = 2·den_{k-1}(x) - num_{k-1}(x); den_k(x) = den_{k-1}(x)·(1 - 2x) + num_{k-1}(x)·x; F_k(x) = num_k(x)/den_k(x)."
[^2]: [[oeis-mining-pe502](pages/oeis-mining-pe502.md)] `mine-notes.md` §"Vein 1" L31-37 — "The general P(k,·) family is C-finite of order k+1: P(1): x^2 - 2x + 2 ... P(5): x^6 - 6x^5 + 18x^4 - 32x^3 + 48x^2 - 32x + 32 (constant term = (-1)^{k-1} 2^k; leading coeff -(k+1))."
