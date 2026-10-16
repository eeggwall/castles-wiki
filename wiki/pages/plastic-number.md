---
title: Plastic number
category: Concepts
summary: ψ = 1.3247…, the real root of x³ = x + 1 and the smallest Pisot number, with the Padovan numbers (A000931) and the Perrin numbers (A001608) as its Fibonacci and Lucas numbers. Its square ψ² has minimal polynomial μ³ − 2μ² + μ − 1 (the recurrence of A005251) and a Jacobi-Perron expansion of period 1. On the castle wiki, 2ψ² is the largest root of char_6, the growth constant of the signed tower count P(6, ·), and ψ itself is the Perron root of six 3 × 3 strip rules, whose strips are plastic by width; the maximal and (1, 2)-RLL castles are plastic by width and the ridge castles of height 2 by area, all counted by shifted Padovan numbers.
tags: [concept, plastic-number, pisot, padovan, perrin, cubic, jacobi-perron, eigenvalue, castle, oeis, strip-perron-root]
sources: [verger-gaugry-2024-salem-minoration, oeis-mining-pe502, project-euler-502-solution]
created: 2026-09-16
updated: 2026-10-16
---

# Plastic number

## Definition

The **plastic number**, also called the plastic constant, is the real root of[^1]

```
x³ = x + 1,        ψ = 1.324717957244746…      (A060006)
```

It plays for the cubic `x³ − x − 1` the role the golden ratio `φ` plays for `x² − x − 1`. The recurrence `a(n) = a(n−2) + a(n−3)` with the initial values `1, 0, 0` gives the **Padovan numbers** `A000931`, and its power sums `ψ^n + ψ'^n + ψ''^n` over the three roots give the **Perrin numbers** `A001608`, as the Fibonacci and Lucas numbers come from `φ`:[^1]

| | golden ratio `φ` | plastic number `ψ` |
|---|---|---|
| minimal polynomial | `x² − x − 1` | `x³ − x − 1` |
| recurrence, initial values `1, 0(, 0)` | Fibonacci `F_n`, A000045 | Padovan `1, 0, 0, 1, 0, 1, 1, 1, 2, 2, 3, 4, 5, 7, 9, 12, 16, 21, 28, …`, A000931 |
| power sums of the roots | Lucas `L_n`, A000032 | Perrin `3, 0, 2, 3, 2, 5, 5, 7, 10, 12, 17, 22, 29, 39, 51, …`, A001608 |
| other roots | `−1/φ`, modulus `0.618` | a complex pair of modulus `ψ^{−1/2} = 0.8688` |
| Pisot number | yes | yes, the smallest |
| field | `Q(√5)`, discriminant 5 | `Q(ψ)`, discriminant `−23` |

A **Pisot number** is a real algebraic integer greater than 1 whose other conjugates all have modulus less than 1. The product of the roots of `x³ − x − 1` is 1, so the complex pair has modulus `ψ^{−1/2} < 1` and `ψ` is a Pisot number. Siegel proved that it is the smallest one, as Verger-Gaugry states.[^2] Since the other two roots tend to 0 in modulus when raised to the `n`-th power, `ψ^n − Perrin(n) → 0`.

`ψ` is the fundamental unit of `Q(ψ)`. Its norm is 1, so it is a unit, and the discriminant `−23` of `x³ − x − 1` is squarefree, so `Z[ψ]` is the whole ring of integers. A unit `ε > 1` of this field has two complex conjugates of modulus `ε^{−1/2} < 1`, so it is a Pisot number, and therefore `ε ≥ ψ`.

The same pairing for the silver ratio `1 + √2` gives the Pell numbers `P⋆_n` and their power sums, the companion Pell numbers `A002203` ([[pell-numbers](pages/pell-numbers.md)]).

## The square, and its expansion

`ψ²` has minimal polynomial[^3]

```
μ³ − 2μ² + μ − 1,        ψ² = 1.754877666…,
```

the resultant of `x³ − x − 1` and `μ − x²`. The corresponding recurrence `a(n) = 2a(n−1) − a(n−2) + a(n−3)` is satisfied by `A005251`. The OEIS reads `A005251(n + 3)` as the number of binary strings of length `n` that avoid the factor `010`; the binary strings of length `N` with no isolated 1 number `A005251(N + 2)`, so the two families are equinumerous with lengths differing by one ([[a005251-bijection](pages/a005251-bijection.md)]).[^3] The even-indexed Padovan numbers `A000931(2n)`, `1, 0, 0, 1, 2, 3, 5, 9, 16, 28, …`, satisfy the same recurrence, since squaring the roots of `x³ − x − 1` gives the roots of `μ³ − 2μ² + μ − 1`.

By Lagrange's theorem, a real number has an eventually periodic simple continued fraction exactly when it is a quadratic irrational, so neither `ψ` nor `ψ²` has one. The Jacobi-Perron algorithm is a two-dimensional continued fraction: starting from `(α_1, α_2) = (α, α²)`, it records the digits `(⌊α_1⌋, ⌊α_2⌋)` and replaces the pair by `((α_2 − ⌊α_2⌋)/(α_1 − ⌊α_1⌋), 1/(α_1 − ⌊α_1⌋))`. On `ψ`, `ψ²` and `2ψ²` its digits are[^4]

```
ψ :  (1,1), (2,3), then (0,3), (0,4) repeating                                    preperiod 2, period 2
ψ²:  (1,3), (0,1), (3,9), (6,12), then (7,12) repeating                           preperiod 4, period 1
2ψ²: (3,12), (0,1), (1,1), (1,1), (7,8), then (1,1), (1,1), (1,1), (5,9) repeating   preperiod 5, period 4
```

The expansion of `ψ²` has period 1, as the simple continued fraction `[a; a, a, …]` of `δ_a` does ([[metallic-means](pages/metallic-means.md)]). The period matrix of the expansion of `2ψ²` has determinant 1 and characteristic polynomial `x³ − 51x² − 13x − 1`, where `51 = Perrin(14)` and `−13 = Perrin(−14)`, the Perrin recurrence run backward. An integer matrix with determinant 1 has a monic integer characteristic polynomial with constant term `±1`, so its eigenvalues are units; the dominant one here is `ψ^14` ([[castle-eigenvalue-oeis-crosswalk](pages/castle-eigenvalue-oeis-crosswalk.md)]).[^4]

## The signed tower count at k = 6

For fixed `k`, the signed tower count `P(k, ·)` satisfies the linear recurrence with characteristic polynomial `char_k` of degree `k + 1` ([[signed-tower-count](pages/signed-tower-count.md)]). At `k = 6`,[^3]

```
char_6(λ)  =  (λ³ − 4λ² + 4λ − 8)(λ⁴ − 3λ³ + 8λ² − 4λ + 8),
```

and the root of largest modulus is the root of the cubic factor

```
ρ_6  =  2ψ²  =  3.509755332…,
```

since substituting `λ = 2μ` turns the cubic factor into `8(μ³ − 2μ² + μ − 1)`. So `P(6, L)` grows like `(2ψ²)^L`.

[[tower-parity-sectors](pages/tower-parity-sectors.md)] explains the factorization. For even `k = 2d`,

```
char_k(2μ) / 2^k  =  H_d(μ) · ( H_{d+1}(μ) + μ² H_{d−1}(μ) ),        H_d(μ)  =  Σ_i (−1)^i C(⌊(d+i)/2⌋, i) μ^{d−i},
```

and `H_3(μ) = μ³ − 2μ² + μ − 1` is the minimal polynomial of `ψ²`. When `k ≡ 2 (mod 4)`, `H_d` is the characteristic polynomial of the towers whose last column has even height, and at `k = 6` their signed count is[^5]

```
Σ_{towers of height at most 6 on a base of length L, last column even}  (−1)^{blocks}  =  2^L · A005251(L + 3),
```

`2^L` times the number of binary strings of length `L + 1` with no isolated 1. At `L = 1` this is `4 = 2·2`: the towers `(0)`, `(2)`, `(4)`, `(6)` have `0, 2, 4, 6` blocks.

`2ψ²` is not a Pisot number, since its conjugates have modulus `2/ψ = 1.51`; `ψ² = ρ_6/2` is. For `k ≡ 2 (mod 4)` and `k ≤ 30`, `ρ_k/2` is a root of `H_{k/2}` (computed), whose constant term is `−1`, so `ρ_k/2` is an algebraic unit.[^5]

## The plastic number as a growth constant

Three powers of `ψ` are growth constants on the wiki:

| constant | value | where |
|---|---|---|
| `2ψ²` | `3.5098` | the signed tower count `P(6, ·)` (section *The signed tower count at k = 6*). The castle graph of `(1, 1, 2, 7, 7, 5, 7, 7)` has spectral radius `8.0 · 10⁻⁹` below `2ψ²`, and `2ψ²` is not an eigenvalue of it ([[castle-graph-spectral-radius](pages/castle-graph-spectral-radius.md)]) |
| `ψ²` | `1.7549` | `A005251`, which counts the tree castles by area with no bound on the height ([[tree-castle-by-area](pages/tree-castle-by-area.md)]), the skylines of height at most 2 whose raised columns are separated by valleys at least 2 columns wide ([[tower-spacing-castles](pages/tower-spacing-castles.md)]), and the binary strings with no isolated 1 of [[hardin-word-identity](pages/hardin-word-identity.md)], related by the bijections of [[a005251-bijection](pages/a005251-bijection.md)]; by semi-perimeter `s`, all castles of height 2, `A077855(s − 3)` ([[golden-silver-bronze-plastic-castles](pages/golden-silver-bronze-plastic-castles.md)]) |
| `ψ` | `1.3247` | by width, the strips of the rule in the paragraph *A rule on three heights*, found in the census of strip Perron roots ([[reachable-field-census](pages/reachable-field-census.md)]), the maximal castles and the `(1, 2)`-RLL castles of height 2, and the castles of the rule `1 → 2 → 3 → {1, 2}` of height 3; by area, the ridge castles of height 2. All are counted by shifted Padovan numbers ([[golden-silver-bronze-plastic-castles](pages/golden-silver-bronze-plastic-castles.md)], [[padovan-families](pages/padovan-families.md)]) |

**A rule on three heights.** Of the 512 binary `3 × 3` matrices, exactly 6 have characteristic polynomial `x³ − x − 1`, and each has four entries equal to 1.[^6] One is

```
        to 1  to 2  to 3
from 1 [  0     0     1  ]
from 2 [  1     0     0  ]
from 3 [  1     1     0  ]
```

the rule in which a column of height 1 is followed by one of height 3, a column of height 2 by one of height 1, and a column of height 3 by one of height 1 or 2 ([[castle-strip](pages/castle-strip.md)]). By the Cayley-Hamilton theorem, `M³ = M + I`, so for any start and end vectors the number of strips of width `w` satisfies `N(w + 3) = N(w + 1) + N(w)`. With free ends the strips number `3, 4, 5, 7, 9, 12, 16, 21, 28, …`, which is `A000931(w + 9)`, and they are plastic by width.[^6] Strips under this rule that avoid height 3 have width at most 2, so all but finitely many strips reach height 3 and are castles of height 3.

## Appearances in Sources

- [[verger-gaugry-2024-salem-minoration](pages/verger-gaugry-2024-salem-minoration.md)] - Siegel's theorem that `ψ` is the smallest Pisot number, and `ψ = θ_5^{−1}` on the trinomial scale of the Salem bound.
- [[oeis-mining-pe502](pages/oeis-mining-pe502.md)] - the family `P(k, ·)`, whose row `k = 6` grows like `(2ψ²)^L`.
- [[project-euler-502-solution](pages/project-euler-502-solution.md)] - the update of `num_k` and `den_k` that gives `char_k`.

## Related Concepts

- [[tower-parity-sectors](pages/tower-parity-sectors.md)] - the factorization of `char_k` for even `k` into `H_d` and its cofactor, and the word counts of the even-last-column towers.
- [[castle-eigenvalue-oeis-crosswalk](pages/castle-eigenvalue-oeis-crosswalk.md)] - the computation of `ρ_6 = 2ψ²` and of the Jacobi-Perron expansions and period matrices.
- [[signed-tower-count](pages/signed-tower-count.md)] - the characteristic polynomials `char_k` and the factorization of `char_6`.
- [[metallic-means](pages/metallic-means.md)] - the quadratic units `δ_a = σ_a^1`, whose simple continued fractions `[a; a, a, …]` have period 1.
- [[eigenvalue-continued-fractions](pages/eigenvalue-continued-fractions.md)] - the simple continued fractions of the quadratic eigenvalues, and Lagrange's theorem.
- [[pell-numbers](pages/pell-numbers.md)] - the Pell numbers and companion Pell numbers of `1 + √2`, the quadratic counterpart of the Padovan and Perrin numbers.
- [[reachable-field-census](pages/reachable-field-census.md)] - the census of Perron roots of strip rules, in which `x³ − x − 1` occurs among the rules on three heights.
- [[golden-silver-bronze-plastic-castles](pages/golden-silver-bronze-plastic-castles.md)] - `ψ` beside golden, silver and bronze by width, area, semi-perimeter and spectrum; no graph has spectral radius `ψ`.
- [[padovan-families](pages/padovan-families.md)] - the castle families counted by Padovan numbers, their common core of blocks of size 2 and 3, and the bijections between them.
- [[algebraic-transcendental-wall](pages/algebraic-transcendental-wall.md)] - the closed forms of the castle counts, whose constants are algebraic numbers such as `ψ`.
- [[fractional-recurrences](pages/fractional-recurrences.md)] - the recurrence `∇^α a_n = a_{n−1}`, whose characteristic equation `(1 − r)^α = r` gives the growth constant `ψ²` at `α = 2/3` and `ψ³ = ψ + 1` at `α = 3/2`.

## Footnotes

[^1]: https://oeis.org/A060006, https://oeis.org/A000931, https://oeis.org/A001608 (read 2026-09-16) - "Decimal expansion of real root of x^3 - x - 1 (the plastic constant)"; "Padovan sequence (or Padovan numbers): a(n) = a(n-2) + a(n-3) with a(0) = 1, a(1) = a(2) = 0"; "Perrin sequence (or Perrin numbers, or Ondrej Such sequence): a(n) = a(n-2) + a(n-3)", data `3, 0, 2, 3, 2, 5, 5, 7, 10, 12, 17, 22, 29, 39, 51, 68, 90`. Padovan and Perrin terms recomputed from the recurrence (Python 3.11, 2026-10-16).
[^2]: [[verger-gaugry-2024-salem-minoration](pages/verger-gaugry-2024-salem-minoration.md)] §1 "Introduction" L69-70 - "The set of Pisot numbers admits the minorant Θ = 1.3247 . . ., unique root > 1 of X 3 − X − 1 by a result of Siegel [97]." Siegel's theorem is taken as Verger-Gaugry states it.
[^3]: Verified by execution (Python 3.11 with SymPy, 2026-10-16): `resultant(x³ − x − 1, μ − x²) = μ³ − 2μ² + μ − 1`; the factorization of `char_6` and `2ψ² = 3.5097553324…` as its root of largest modulus; avoid-`010` strings of length `n ≤ 9` equal `A005251(n+3)` and strings of length `N ≤ 9` with no isolated 1 equal `A005251(N+2)`; `A000931(2n)` against the recurrence for `n < 10`. https://oeis.org/A005251 (read 2026-09-16) - "a(n) = 2*a(n-1) - a(n-2) + a(n-3)", comment "a(n+3) is the number of n-bit sequences that avoid 010".
[^4]: Verified by execution (mpmath at 200 digits, 2026-10-16): the Jacobi-Perron digits of `(ψ, ψ²)`, `(ψ², ψ⁴)` and `(2ψ², 4ψ⁴)` to 10, 10 and 14 steps; `Perrin(−14) = −13`; the characteristic polynomial of `ψ^14` is `x³ − 51x² − 13x − 1`. The exact computation in `Q(ψ)` is on [[castle-eigenvalue-oeis-crosswalk](pages/castle-eigenvalue-oeis-crosswalk.md)].
[^5]: Verified by execution (Python 3.11 with SymPy, 2026-10-16): the factorization `char_k(2μ)/2^k = H_d(μ)(H_{d+1}(μ) + μ² H_{d−1}(μ))` for even `k ≤ 30`; for `k ≡ 2 (mod 4)`, `k ≤ 30`, the root of largest modulus of `char_k` is twice a root of `H_{k/2}`, and the constant term of `H_{k/2}` is `−1`; the even-last-column sum at `k = 6` against `2^L A005251(L+3)` by summing over all towers for `L ≤ 7`.
[^6]: Verified by execution (Python 3.11 with SymPy, 2026-10-16): all 512 binary `3 × 3` matrices, of which 6 have characteristic polynomial `x³ − x − 1`, all with four entries 1; the strip counts `1ᵀ M^{w−1} 1` for `w ≤ 15` against `N(w + 3) = N(w + 1) + N(w)` and `A000931(w + 9)`.
