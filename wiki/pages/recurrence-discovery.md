---
title: Recurrence discovery for P(k,L)
category: Analyses
summary: Berlekamp-Massey on the signed tower count P(k, L) in both directions, from exact values. In L the shortest recurrence has order k + 1 for k ≤ 8, matching the proved degree of den_k. In k, on the values for k ≤ 50, it has order 2, 2, 3 for L = 1, 2, 3 and 2L − 2 for 4 ≤ L ≤ 12 (computed, and proved for every L ≥ 4), with closed forms for L ≤ 3.
tags: [analysis, castle, recurrence, berlekamp-massey, c-finite, verification]
sources: [project-euler-502-solution, oeis-mining-pe502, project-euler-502-castle-factoring]
created: 2026-09-14
updated: 2026-10-25
---

# Recurrence discovery for P(k,L)

## Overview

The signed tower count `P(k, L)`, the sum of `(−1)^{blocks}` over the towers of height at most `k` on a base of length `L` ([[signed-tower-count](pages/signed-tower-count.md)]), satisfies a linear recurrence in each argument when the other is fixed. The [[castle-count-algorithms](pages/castle-count-algorithms.md)] use both.

- **In `L`, for fixed `k`.** The generating function `P_k(x)` is `num_k(x)/den_k(x)` with `den_k` of degree `k + 1`, so `P(k, ·)` satisfies a recurrence of order `k + 1` ([[castle-counting-formula](pages/castle-counting-formula.md)], the Proposition in the section *Signed tower count*).
- **In `k`, for fixed `L`.** The Solution subpage finds this recurrence with the Berlekamp-Massey algorithm and gives its order as "at most about 2w empirically".[^1]

This page runs [[berlekamp-massey](pages/berlekamp-massey.md)] on exact values of `P(k, L)` in both directions. The program in the section *Method* prints every order in the tables of the section *Results*.

## Method

**Computing `P(k, L)`.** Towers of height at most `k` on a base of length `L` are given by their column heights `c = (c_1, …, c_L) ∈ {0, …, k}^L` ([[castle-representations](pages/castle-representations.md)]), and their block count is the total descent[^2]

```
blocks(c)  =  Σ_{i=0}^{L} max(0, c_i − c_{i+1}),        c_0 = c_{L+1} = 0.
```

A dynamic program over the height of the last column computes `P(k, L)` without listing the `(k+1)^L` towers. It carries the signed count `F[b]` of the towers whose last column has height `b`; appending a column of height `b` after one of height `a` multiplies by `(−1)^{max(0, a−b)}`, and the final descent from the last column to the base multiplies by `(−1)^b`. All values are exact integers.

**Finding the order.** Berlekamp-Massey returns the shortest linear recurrence that generates the given terms. When the sequence satisfies a recurrence of order at most half the number of terms, that is its shortest recurrence ([[berlekamp-massey](pages/berlekamp-massey.md)]).

```python
from fractions import Fraction

def P_table(max_k, max_L):
    """P[k][L] = sum of (-1)^blocks over towers of height <= k above a
    length-L block; blocks = total descent, computed by a DP over the
    last column height (exact integers)."""
    P = [[0]*(max_L+1) for _ in range(max_k+1)]
    for k in range(max_k+1):
        F = [0]*(k+1)            # signed sum over towers ending at height b
        F[0] = 1
        P[k][0] = 1              # empty tower
        for L in range(1, max_L+1):
            newF = [0]*(k+1)
            for b in range(k+1):
                s = 0
                for a in range(k+1):
                    s += F[a] * (1 if a <= b else (-1)**(a-b))  # (-1)^max(0,a-b)
                newF[b] = s
            F = newF
            P[k][L] = sum(F[b]*((-1)**b) for b in range(k+1))    # final descent b
    return P

def berlekamp_massey(s):
    """Shortest linear recurrence s[n] = -sum_{i=1}^L C[i] s[n-i], over Q."""
    s = [Fraction(x) for x in s]
    C = [Fraction(1)]; B = [Fraction(1)]
    L = 0; m = 1; b = Fraction(1)
    for N in range(len(s)):
        d = s[N]
        for i in range(1, L+1):
            d += C[i]*s[N-i]
        if d == 0:
            m += 1
        else:
            coef = d/b
            T = C[:]
            if len(C) < len(B)+m:
                C += [Fraction(0)]*(len(B)+m-len(C))
            for j in range(len(B)):
                C[j+m] -= coef*B[j]
            if 2*L <= N:
                L = N+1-L; B = T; b = d; m = 1
            else:
                m += 1
    return C[:L+1], L

# L-direction: fixed k, vary L
P = P_table(8, 20)
for k in range(9):
    _, order = berlekamp_massey(P[k])
    print(f"k={k}: order {order}")

# k-direction: fixed L, vary k
P = P_table(50, 14)
for L in range(1, 13):
    seq = [P[k][L] for k in range(51)]
    _, order = berlekamp_massey(seq)
    print(f"L={L}: order {order}")
```

## Results

### In L: order k + 1

| k | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|---|---|---|
| order | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |

On the 21 values `L = 0, …, 20`, each order is `k + 1`, the degree of `den_k`; for `k ≤ 40`, `num_k` and `den_k` have no common factor, so `k + 1` is the order of the shortest recurrence ([[castle-counting-formula](pages/castle-counting-formula.md)]). The characteristic polynomials `char_k` are listed on [[signed-tower-count](pages/signed-tower-count.md)].[^3]

### In k: order 2L − 2 for 4 ≤ L ≤ 12

| L | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| order | 2 | 2 | 3 | 6 | 8 | 10 | 12 | 14 | 16 | 18 | 20 | 22 |

On the 51 values `k = 0, …, 50`, the shortest recurrence has order `2L − 2` for `4 ≤ L ≤ 12` (computed), against the source's "at most about 2w".[^1] Every order in the table is at most 25, half the number of terms, so it is the shortest recurrence of the 51 values. The orders 2, 2, 3 for `L ≤ 3` do not follow `2L − 2`; the section *Closed forms for L ≤ 3* gives these rows.

For every `L ≥ 4` the characteristic polynomial is `(x + 1)^L (x − 1)^{L−2}`, computed by Berlekamp-Massey on `k ≤ 80` for `L ≤ 12` and proved from the eigenvalues of the height step ([[signed-tower-k-direction](pages/signed-tower-k-direction.md)], section *Proof of the multiplicities*). So every root is `±1` and the order is `L + (L − 2)`. That every root is `±1` holds at every `L`: `P(k, L)` is a polynomial in `k` of degree at most `L` on each class of `k` modulo 2 ([[sum-of-three-cubes-castles](pages/sum-of-three-cubes-castles.md)], section *The residue test*), so the order is at most `2L + 1` (the Lemma of [[mod-9-coset-lift](pages/mod-9-coset-lift.md)]).

### Closed forms for L ≤ 3

| L | `P(k, L)` | values for `k = 0, 1, 2, …` | characteristic polynomial | order |
|---|---|---|---|---|
| 1 | `(1 + (−1)^k)/2` | `1, 0, 1, 0, …` | `(x − 1)(x + 1)` | 2 |
| 2 | `(−1)^k (k + 1)` | `1, −2, 3, −4, …` | `(x + 1)²` | 2 |
| 3 | `(−1)^k (k + 1)²` | `1, −4, 9, −16, …` | `(x + 1)³` | 3 |

At `L = 1` the towers are one column of height `c ≤ k` with `c` blocks, so `P(k, 1) = Σ_{c=0}^{k} (−1)^c`. The proof of the `L = 2` row is on [[signed-tower-count](pages/signed-tower-count.md)], and [[closed-form-hunting](pages/closed-form-hunting.md)] treats the three rows and the larger `L`.

## Appearances in Sources

- [[project-euler-502-solution](pages/project-euler-502-solution.md)] - the Berlekamp-Massey path in `k` and the source's estimate of its order.
- [[oeis-mining-pe502](pages/oeis-mining-pe502.md)] - the characteristic polynomials of `P(k, ·)` in `L`, of order `k + 1`.
- [[project-euler-502-castle-factoring](pages/project-euler-502-castle-factoring.md)] - the block count as the total descent of the column heights.

## Related Concepts

- [[signed-tower-count](pages/signed-tower-count.md)] - the values, characteristic polynomials and closed forms of `P(k, L)`.
- [[signed-tower-k-direction](pages/signed-tower-k-direction.md)] - the characteristic polynomials in `k`, proved for every `L ≥ 4`, and the polynomials in `k` that make up `P(k, L)`.
- [[closed-form-hunting](pages/closed-form-hunting.md)] - the closed forms of `P(k, L)` in `k` for small `L`.
- [[berlekamp-massey](pages/berlekamp-massey.md)] - the algorithm, and when its output is the shortest recurrence of a sequence.
- [[kitamasa](pages/kitamasa.md)] - the evaluation of a far term of a recurrence once it is known.
- [[castle-count-algorithms](pages/castle-count-algorithms.md)] - the two directions as the two paths that evaluate the Project Euler targets.
- [[generating-function-gallery](pages/generating-function-gallery.md)] - the rational functions `num_k/den_k` and the recurrence `den_{k+1} = den_{k−1} − 2x·den_k`.
- [[tower-parity-sectors](pages/tower-parity-sectors.md)] - the factorization of `char_k` for even `k` by the parity of the last column.
- [[castle-eigenvalue-oeis-crosswalk](pages/castle-eigenvalue-oeis-crosswalk.md)] - the roots of `char_k` and of the recurrences in `k`, set against the OEIS.
- [[castle-sequence-catalogue](pages/castle-sequence-catalogue.md)] - the rows `P(k, ·)`.
- [[aocp-generating-functions](pages/aocp-generating-functions.md)] - the correspondence between linear recurrences and rational generating functions.
- [[generating-functions](pages/generating-functions.md)] - the section *From a rational generating function to its recurrence*, coefficient matching on `den_k(x)·P_k(x) = num_k(x)`.

## Footnotes

[^1]: [[project-euler-502-solution](pages/project-euler-502-solution.md)] §"The k-direction Berlekamp-Massey path (h > 15000)" L165 - "The recurrence order is at most about 2w empirically. Berlekamp-Massey discovers the recurrence, so no proof is required to use it, but the transfer-matrix argument justifies why one exists."
[^2]: [[project-euler-502-castle-factoring](pages/project-euler-502-castle-factoring.md)] §"The sign of a castle" L104-108 - "In the column-height form, the block count is the total descent: blocks = ∑_{i=0}^{L} max(0, c_i - c_{i+1}), c_0 = c_{L+1} = 0".
[^3]: [[oeis-mining-pe502](pages/oeis-mining-pe502.md)] `mine-notes.md` §"Vein 1" L31-37 - "The general P(k,·) family is C-finite of order k+1: P(1): x^2 - 2x + 2 ... P(5): x^6 - 6x^5 + 18x^4 - 32x^3 + 48x^2 - 32x + 32 (constant term = (-1)^{k-1} 2^k; leading coeff -(k+1))". The program on this page re-run with Python 3.11 on 2026-10-16; every order in both tables reproduced.
