---
title: Closed-form hunting for P(k,L)
category: Analyses
summary: Closed forms of the signed tower count P(k, L) as a function of the tower height k at fixed base length L. P(k, 1) = (1 + (−1)^k)/2, P(k, 2) = (−1)^k (k+1) (proved) and P(k, 3) = (−1)^k (k+1)²; for every L ≥ 4 the recurrence in k has order 2L − 2 and characteristic polynomial (x+1)^L (x−1)^{L−2} (computed here for L ≤ 12, proved on the k-direction page), so P(k, L) is (−1)^k times a polynomial of degree L − 1 plus a polynomial of degree L − 3, not (−1)^k times a single power.
tags: [analysis, castle, closed-form, c-finite, verification]
sources: [project-euler-502-castle-factoring, project-euler-502-solution]
created: 2026-09-14
updated: 2026-10-25
---

# Closed-form hunting for P(k,L)

The signed tower count `P(k, L)` adds up `(−1)^{blocks}` over the towers of height at most `k` on a base of length `L` ([[signed-tower-count](pages/signed-tower-count.md)]). This page gives its closed forms as a function of `k` at fixed `L`. For `L = 2, 3`, `P(k, L)` is `(−1)^k` times a power of `k + 1`. For every `L ≥ 4` the recurrence in `k` has order `2L − 2`, and `P(k, L)` is the sum of `(−1)^k` times one polynomial and a second polynomial. The orders are tabulated on [[recurrence-discovery](pages/recurrence-discovery.md)].

## The closed forms for L ≤ 3

| `L` | `P(k, L)` | characteristic polynomial of the recurrence in `k` |
|---|---|---|
| 1 | `(1 + (−1)^k)/2` | `(x − 1)(x + 1)` |
| 2 | `(−1)^k (k + 1)` | `(x + 1)²` |
| 3 | `(−1)^k (k + 1)²` | `(x + 1)³` |

At `L = 1` the towers are the single columns of height `c ∈ {0, …, k}`, with `c` blocks, so `P(k, 1) = Σ_{c=0}^{k} (−1)^c = (1 + (−1)^k)/2`.

**Proposition.** `P(k, 2) = (−1)^k (k + 1)`.

*Proof.* Towers on a base of length 2 are pairs `(a, b) ∈ {0, …, k}²`. With `c_0 = c_3 = 0`, the block count is the total descent `max(0, a − b) + b = max(a, b)`.[^1] For each `m`, `2m + 1` pairs have `max(a, b) = m`, so `P(k, 2) = Σ_{m=0}^{k} (−1)^m (2m + 1)`. The case `k = 0` gives 1, and `(−1)^k (k + 1) − (−1)^{k−1} k = (−1)^k (2k + 1)` is the term added at `k`, so induction on `k` gives the claim.

The source states `P(k, 3) = (−1)^k (k + 1)²`, with the recurrence `(x + 1)³`; it is not derived here, and it agrees with the sum over all towers for `k ≤ 29`.[^2][^3]

## From L = 4 on

At `L = 4`, `P(1, 4) = −4` while `(−1)^1 (1 + 1)^3 = −8`, so the pattern of `L ≤ 3` stops. At every `L`, `P(k, L)` is a polynomial in `k` of degree at most `L` on each class of `k` modulo 2 ([[sum-of-three-cubes-castles](pages/sum-of-three-cubes-castles.md)], section *The residue test*), so `P(k, L) = (−1)^k A_L(k) + B_L(k)` with polynomials of degree at most `L`. For every `L ≥ 4` the shortest recurrence of `P(·, L)` has order `2L − 2` ([[signed-tower-k-direction](pages/signed-tower-k-direction.md)], section *Proof of the multiplicities*; computed here for `L ≤ 12`), and its characteristic polynomial is[^3]

```
(x + 1)^L (x − 1)^{L−2}.
```

It is palindromic for even `L` and anti-palindromic for odd `L`, since `x^{2L−2} f(1/x) = (−1)^L f(x)` for `f = (x + 1)^L (x − 1)^{L−2}`. The coefficient lists, from `x^{2L−2}` down, are

```
L = 4:  [1, 2, −1, −4, −1, 2, 1]                   (x + 1)⁴ (x − 1)²
L = 5:  [1, 2, −2, −6, 0, 6, 2, −2, −1]            (x + 1)⁵ (x − 1)³
L = 6:  [1, 2, −3, −8, 2, 12, 2, −8, −3, 2, 1]     (x + 1)⁶ (x − 1)⁴
```

The roots `−1` of multiplicity `L` and `1` of multiplicity `L − 2` give, for these `L`,

```
P(k, L)  =  (−1)^k A_L(k) + B_L(k),        deg A_L ≤ L − 1,  deg B_L ≤ L − 3,
```

so even `k` and odd `k` each follow a polynomial of degree `L − 1`, `A_L + B_L` and `−A_L + B_L`. The first two cases are[^3]

```
P(k, 4)  =  (−1)^k (k + 1)(2k + 1)(2k + 3)/6  +  (k + 1)/2
P(k, 5)  =  (−1)^k k (k + 1)² (k + 2)/3      +  (k + 1)²
```

`|P(k, 4)| = A352116(k + 1)`, the partial sums of the odd triangular numbers.[^4] The polynomials `A_L` and `B_L` up to `L = 8` are on [[signed-tower-k-direction](pages/signed-tower-k-direction.md)].

In the other direction, at fixed `k`, `P(k, ·)` has a rational generating function with a denominator of degree `k + 1`, and `P(1, L) = Re((1+i)^{L+1})` ([[signed-tower-count](pages/signed-tower-count.md)]).

## Appearances in Sources

- [[project-euler-502-castle-factoring](pages/project-euler-502-castle-factoring.md)] - the block count as total descent, used in the proof for `L = 2`.
- [[project-euler-502-solution](pages/project-euler-502-solution.md)] - the closed forms `P(k, 2) = (−1)^k (k + 1)` and `P(k, 3) = (−1)^k (k + 1)²`.

## Related Concepts

- [[recurrence-discovery](pages/recurrence-discovery.md)] - the orders of the recurrences of `P` in `k` and in `L`, found by Berlekamp-Massey.
- [[signed-tower-k-direction](pages/signed-tower-k-direction.md)] - the polynomials `A_L`, `B_L` to `L = 8`, the periods modulo primes, and the OEIS identities of the rows.
- [[signed-tower-count](pages/signed-tower-count.md)] - `P(k, L)` and its recurrences in `L`.
- [[castle-sign](pages/castle-sign.md)] - the sign `(−1)^{blocks}` and the total ascent and descent.
- [[berlekamp-massey](pages/berlekamp-massey.md)] - the algorithm that finds the shortest recurrences, and when its output is correct.
- [[char-k-eisenstein-at-two](pages/char-k-eisenstein-at-two.md)] - irreducibility of the characteristic polynomials `char_k` of the recurrences in `L`.

## Footnotes

[^1]: [[project-euler-502-castle-factoring](pages/project-euler-502-castle-factoring.md)] §"The sign of a castle" L104-108 - "In the column-height form, the block count is the total descent: blocks = ∑_{i=0}^{L} max(0, c_i - c_{i+1}), c_0 = c_{L+1} = 0".
[^2]: [[project-euler-502-solution](pages/project-euler-502-solution.md)] §"Recursion for P(k, L)" L115-118 - "P(k, 2) = (-1)^k (k+1), satisfying (λ+1)^2 = 0. P(k, 3) = (-1)^k (k+1)^2, satisfying (λ+1)^3 = 0."
[^3]: Verified by execution (Python 3.11 with SymPy, 2026-10-16): `P(k, L)` by the column-height dynamic program for `k ≤ 59`, `L ≤ 12`; Berlekamp-Massey on these 60 values gives order 2 at `L = 1, 2`, 3 at `L = 3` and `2L − 2` for `4 ≤ L ≤ 12`, with the characteristic polynomials of the table and `(x + 1)^L (x − 1)^{L−2}` (each order is at most 30, so each recurrence is the shortest one for these values); the closed forms for `L ≤ 5` for `k ≤ 29`; the coefficient lists for `L = 4, 5, 6`.
[^4]: https://oeis.org/A352116 (read 2026-10-16) - "Partial sums of the odd triangular numbers (A014493)", offset 1, data 1, 4, 19, 40, 85, 140, 231, ...; `|P(k, 4)|` for `k = 0, …, 9` is 1, 4, 19, 40, 85, 140, 231, 336, 489, 660.
