---
title: Plastic number
category: Concepts
summary: ψ = 1.3247…, the real root of x³ = x + 1 - the cubic sibling of the golden ratio, the smallest Pisot number, with Padovan (A000931) and Perrin (A001608) as its Fibonacci and Lucas. Its square ψ² has minimal polynomial μ³ − 2μ² + μ − 1 and a period-1 Jacobi-Perron expansion. It enters the castle as the k = 6 signed-tower eigenvalue ρ_6 = 2ψ².
tags: [concept, plastic-number, pisot, padovan, perrin, cubic, jacobi-perron, eigenvalue, castle, oeis]
sources: [oeis-mining-pe502, project-euler-502-solution]
created: 2026-09-16
updated: 2026-09-16
---

# Plastic number

## Definition

The **plastic number** (also plastic ratio, plastic constant, or "le nombre radiant" in van der Laan's architectural writing) is the real root of

```
x³ = x + 1,        ψ = 1.324717957244746…      (OEIS A060006)
```

It is the cubic analogue of the golden ratio `φ` (`x² = x + 1`) and stands to the **Padovan** and **Perrin** sequences as `φ` stands to Fibonacci and Lucas:[^1]

| | golden `φ` | plastic `ψ` |
|---|---|---|
| minimal polynomial | `x² − x − 1` | `x³ − x − 1` |
| "Fibonacci" (`a(n) = a(n−2) + a(n−3)`) | `F_n`, A000045 | Padovan `1, 1, 1, 2, 2, 3, 4, 5, 7, 9, 12, 16, 21, 28, …`, A000931 |
| "Lucas" (trace `ψ^n + ψ'^n + ψ''^n`) | `L_n`, A000032 | Perrin `3, 0, 2, 3, 2, 5, 5, 7, 10, 12, 17, 22, 29, 39, 51, …`, A001608 |
| conjugates | `−1/φ`, modulus `0.618` | a complex pair of modulus `ψ^{−1/2} = 0.8688` |
| Pisot? | yes | yes - the **smallest** Pisot number |
| unit? | fundamental unit of `Q(√5)` | fundamental unit of the cubic field `Q(ψ)`, discriminant `−23` |

The **Pisot** property (all conjugates strictly inside the unit circle) is what makes `ψ^n` approach integers: `ψ^n − Perrin(n) → 0`. Padovan numbers are the impulse response of the recurrence, Perrin the trace; the same relationship as [[pell-numbers](pages/pell-numbers.md)] and companion Pell for `1 + √2`.

## The square, and its expansion

`ψ²` has minimal polynomial[^2]

```
μ³ − 2μ² + μ − 1,        ψ² = 1.754877666…
```

(the resultant of `x³ − x − 1` with `μ − x²`), and it is the number that actually appears on this wiki. The corresponding recurrence `a(n) = 2a(n−1) − a(n−2) + a(n−3)` is the recurrence of **A005251**, the count of `n`-bit strings with no isolated `1` (equivalently, avoiding the factor `010`); the Padovan bisection `A000931(2n)` satisfies it too.

Neither `ψ` nor `ψ²` has a periodic *simple* continued fraction - Lagrange forbids it for any cubic - but both have periodic **Jacobi-Perron** expansions (the two-dimensional continued fraction on `(α, α²)`), computed exactly on [[convergents-oeis-crosswalk](pages/convergents-oeis-crosswalk.md)]:[^3]

```
ψ :  digits (1,1), (2,3), then (0,3), (0,4) repeating          preperiod 2, period 2
ψ²:  digits (1,3), (0,1), (3,9), (6,12), then (7,12) repeating  preperiod 4, period 1
2ψ²: digits (3,12), (0,1), (1,1), (1,1), (7,8), then (1,1), (1,1), (1,1), (5,9) repeating   preperiod 5, period 4
```

`ψ²` has a **period-one** Jacobi-Perron expansion - the cubic counterpart of the metallic means' `[a; a, a, …]`. The period matrix of the `2ψ²` expansion has determinant 1, characteristic polynomial `x³ − 51x² − 13x − 1` (coefficients `Perrin(14) = 51` and `Perrin(−14) = −13`), and dominant eigenvalue `ψ^14` - the unit that a periodic Jacobi-Perron expansion always produces.

## Where it enters the castle

The L-direction recurrence of the signed tower count `P(k, L)` ([[signed-tower-count](pages/signed-tower-count.md)]) has characteristic polynomial `char_k` of degree `k+1` ([[generating-function-gallery](pages/generating-function-gallery.md)]). For `k = 6` the dominant eigenvalue is[^2]

```
ρ_6 = 2ψ² = 3.509755332…,      minimal polynomial λ³ − 4λ² + 4λ − 8.
```

The structural reason is on [[tower-parity-sectors](pages/tower-parity-sectors.md)]: for even `k = 2d` the rescaled polynomial `char_k(2μ)/2^k` factors as `H_d(μ)·(H_{d+1}(μ) + μ² H_{d−1}(μ))` with `H_d(μ) = Σ_i (−1)^i C(⌊(d+i)/2⌋, i) μ^{d−i}`, and `H_3 = μ³ − 2μ² + μ − 1` is exactly the minimal polynomial of `ψ²`. The factor `H_d` is the characteristic polynomial of the **even-last-column sector** when `k ≡ 2 (mod 4)`, which gives the identity

```
Σ_{towers of height ≤ 6, length L, last column even} (−1)^{blocks}  =  2^L · A005251(L+3)
                                                                    =  2^L · #{(L+1)-bit strings with no isolated 1}.
```

So the plastic number is the growth constant of height-`≤6` signed towers, and `2ψ²` sits on the wiki's list of algebraic growth constants next to `φ` and `1 + √2` ([[metallic-means](pages/metallic-means.md)]) - a non-metallic, non-quadratic rung. `2ψ²` itself is not Pisot (its conjugates have modulus `2/ψ = 1.51`), but `ψ² = ρ_6/2` is, and `ρ_k/2` is an algebraic unit for every `k ≡ 2 (mod 4)`.

## Appearances in Sources

- [[oeis-mining-pe502](pages/oeis-mining-pe502.md)] - the `P(k,·)` family whose `k = 6` row carries the plastic eigenvalue.
- [[project-euler-502-solution](pages/project-euler-502-solution.md)] - the `num_k/den_k` recurrence that generates `char_k`.

## Related Concepts

- [[tower-parity-sectors](pages/tower-parity-sectors.md)] - the factorization `H_d · V_d` that produces `2ψ²`, and the Hardin word-count identities it implies.
- [[convergents-oeis-crosswalk](pages/convergents-oeis-crosswalk.md)] - where `ρ_6 = 2ψ²` was found; the Jacobi-Perron computations.
- [[metallic-means](pages/metallic-means.md)] - the quadratic family (`φ`, `1+√2`, …) the plastic number sits beside; same Pisot / unit / periodic-expansion story one degree up.
- [[eigenvalue-continued-fractions](pages/eigenvalue-continued-fractions.md)] - why a cubic cannot have a periodic simple continued fraction, and what replaces it.
- [[pell-numbers](pages/pell-numbers.md)] - the impulse / trace pairing (Pell / companion Pell) that Padovan / Perrin repeat in degree 3.
- [[algebraic-transcendental-wall](pages/algebraic-transcendental-wall.md)] - `ψ` is algebraic of degree 3, on the reachable side of the wall.

## Footnotes

[^1]: https://oeis.org/A060006 (2026-09-16) - "Decimal expansion of real root of x^3 - x - 1 (the plastic constant)"; https://oeis.org/A000931 - "Padovan sequence (or Padovan numbers): a(n) = a(n-2) + a(n-3) with a(0) = 1, a(1) = a(2) = 0"; https://oeis.org/A001608 - "Perrin sequence (or Perrin numbers, or Ondrej Such sequence): a(n) = a(n-2) + a(n-3)", data `3, 0, 2, 3, 2, 5, 5, 7, 10, 12, 17, 22, 29, 39, 51, 68, 90`. The Pisot property, the conjugate modulus `ψ^{−1/2}` (product of the three roots is 1) and the field discriminant `−23` are standard.

[^2]: Verified by execution (SymPy 1.14): `factor(resultant(x³ − x − 1, μ − x², x)) = μ³ − 2μ² + μ − 1`; `factor(resultant(μ³ − 2μ² + μ − 1, λ − 2μ, μ)) = λ³ − 4λ² + 4λ − 8`, which is the cubic factor of `char_6 = (λ³ − 4λ² + 4λ − 8)(λ⁴ − 3λ³ + 8λ² − 4λ + 8)`; numerically `2ψ² = 3.5097553324933855…` against the gallery's `ρ_6`. https://oeis.org/A005251 (2026-09-16) - "a(n) = 2*a(n-1) - a(n-2) + a(n-3)", comment "a(n+3) is the number of n-bit sequences that avoid 010".

[^3]: Verified by execution: exact Jacobi-Perron in `Q(ρ)` (SymPy `rem`/`invert` modulo the minimal polynomial, mpmath at 800 digits for floors) on `x³ − x − 1` near `1.32` (periodic, preperiod 2, period 2, digits `[1,1],[2,3],[0,3],[0,4]`), on `μ³ − 2μ² + μ − 1` near `1.75` (periodic, preperiod 4, period 1, digits `[1,3],[0,1],[3,9],[6,12],[7,12]`), and on `λ³ − 4λ² + 4λ − 8` near `3.5` (periodic, preperiod 5, period 4). Period matrix and Perrin identification as on [[convergents-oeis-crosswalk](pages/convergents-oeis-crosswalk.md)].
