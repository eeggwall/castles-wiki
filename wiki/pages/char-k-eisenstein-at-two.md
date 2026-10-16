---
title: Eisenstein at 2 - char_k is irreducible for k = 2^m - 1
category: Analyses
summary: Rescaling λ = 2μ turns char_k into Q_k(μ) = char_k(2μ)/2^k, an integer polynomial with Q_{k+1} = μ²·Q_{k−1} − Q_k. The reversal of Q_k is Eisenstein at 2 exactly when Q_k ≡ 1 (mod 2), and modulo 2 the recurrence is a Fibonacci recurrence over F_2[t], t = μ², whose k-th term is the power sum α^{k+1} + β^{k+1}; it equals 1 exactly when k + 1 is a power of 2. So char_k is irreducible over Q, with 2 totally ramified, for k = 1, 3, 7, 15, 31, …. The same condition is the condition that the 2-adic Newton polygon of char_k is one segment, so Eisenstein and Dumas at 2 reach no other k; for the other odd k ≤ 31, irreducibility is computed.
tags: [analysis, castle, characteristic-polynomial, irreducible-polynomial, eisenstein, newton-polygon, two-adic, fibonacci-polynomial, signed-tower-count, proof, sympy, verification]
sources: [calugareanu-hamburg-exercises-basic-ring-theory]
created: 2026-09-26
updated: 2026-10-16
---

# Eisenstein at 2 - `char_k` is irreducible for `k = 2^m − 1`

`char_k(λ) = λ^{k+1} den_k(1/λ)` is the characteristic polynomial of the linear recurrence of the signed tower count `P(k, ·)` in the base length ([[signed-tower-count](pages/signed-tower-count.md)]). For odd `k ≤ 31` it is irreducible over `Q` (computed). For even `k` it has two factors, which [[tower-parity-sectors](pages/tower-parity-sectors.md)] derives from the involution `JD` of the signed transfer matrix `M̃_k`. For odd `k`, `(JD)² = −I`, and `JD` makes `char_k` a product `g·ḡ` of conjugate polynomials over `Q(i)`, which does not decide whether `char_k` factors over `Q`.

**Theorem.** For `k + 1 = 2^m`, `m ≥ 1`, `char_k` is irreducible over `Q`, and 2 is totally ramified in `Q(ρ)` for every root `ρ` of `char_k`.

The proof applies Eisenstein's criterion at the prime 2 after a rescaling (Steps 1 to 3). Step 4 shows that the criterion, and its generalization by Newton polygons, reaches exactly these `k`.

**Eisenstein's criterion.** Let `f = a_0 + a_1 X + ⋯ + a_n X^n` have integer coefficients, and let `p` be a prime with `p ∤ a_n`, `p | a_i` for `i < n`, and `p² ∤ a_0`. Then `f` is irreducible over `Q`.[^1]

## Step 1 - rescale by 2

`char_0 = λ − 1`, `char_1 = λ² − 2λ + 2`, and for `k ≥ 1`

```
char_{k+1}(λ)  =  λ²·char_{k−1}(λ) − 2·char_k(λ),                              (1)
```

which is the recurrence `den_{k+1} = den_{k−1} − 2x·den_k` of [[signed-tower-count](pages/signed-tower-count.md)] multiplied by `λ^{k+2}` at `x = 1/λ`. `char_k` is monic of degree `k + 1` with constant term `(−1)^{k+1} 2^k`. Set

```
Q_k(μ)  =  char_k(2μ) / 2^k.
```

Substituting `λ = 2μ` in Equation (1) and dividing by `2^{k+1}` gives

```
Q_0  =  2μ − 1,        Q_1  =  2μ² − 2μ + 1,        Q_{k+1}  =  μ²·Q_{k−1} − Q_k.        (2)
```

Equation (2) has integer coefficients, so every `Q_k` is an integer polynomial. Its leading coefficient is `2^{k+1}/2^k = 2`, and its constant term `char_k(0)/2^k = ±1` is odd.[^2] This is the rescaling `λ = 2μ` of [[tower-parity-sectors](pages/tower-parity-sectors.md)].

## Step 2 - the Eisenstein condition is `Q_k ≡ 1 (mod 2)`

Reverse the coefficients: `R_k(μ) = μ^{k+1} Q_k(1/μ)`. Its leading coefficient is `Q_k(0) = ±1`, which is odd, and its constant term is the leading coefficient 2 of `Q_k`, which is even and not divisible by 4. So `R_k` is Eisenstein at 2 exactly when every other coefficient of `Q_k` is even, that is, when

```
Q_k(μ)  ≡  1   (mod 2).                                                        (3)
```

When Equation (3) holds, `R_k` is irreducible over `Q`. `Q_k` and `R_k` have nonzero constant terms, so `Q_k` is irreducible exactly when `R_k` is, and `char_k(λ) = 2^k Q_k(λ/2)` is irreducible exactly when `Q_k` is.

*Example.* `char_3 = λ⁴ − 4λ³ + 8λ² − 8λ + 8` gives `Q_3 = 2μ⁴ − 4μ³ + 4μ² − 2μ + 1 ≡ 1 (mod 2)`, whose reversal `R_3 = μ⁴ − 2μ³ + 4μ² − 4μ + 2` is Eisenstein at 2, so `char_3` is irreducible.

## Step 3 - modulo 2 the recurrence is Fibonacci

Write `q_k` for `Q_k` modulo 2, a polynomial over the field `F_2` with two elements. Since `2μ ≡ 0`, Equation (2) becomes

```
q_0  =  1,        q_1  =  1,        q_{k+1}  =  q_k + t·q_{k−1}        over F_2[t],  t = μ².
```

Let `α` and `β` be the roots of `z² + z + t` in an extension of `F_2(t)`, so `α + β = 1` and `αβ = t`; they are distinct, since the derivative of `z² + z + t` is 1. The recurrence has characteristic polynomial `z² − z − t = z² + z + t`, and its solution with `q_0 = q_1 = 1` is `q_k = (α^{k+1} − β^{k+1})/(α − β)`, as the cases `k = 0, 1` show. In characteristic 2, `α − β = α + β = 1`, so

```
q_k  =  α^{k+1} + β^{k+1}  =  s_{k+1},        the power sum of degree k + 1.
```

*If `k + 1 = 2^m`*: the Frobenius map `z ↦ z²` is additive in characteristic 2 ([[finite-fields](pages/finite-fields.md)]), so `s_{2^m} = (α + β)^{2^m} = 1`, and `q_k = 1`.

*Otherwise*, write `k + 1 = 2^m·r` with `r ≥ 3` odd. Then `s_{k+1} = (s_r)^{2^m}`, and `(s_r)^{2^m} = 1` only if `s_r = 1`, since `z^{2^m} − 1 = (z − 1)^{2^m}`. The power sums satisfy `s_n = s_{n−1} + t·s_{n−2}`, with `s_0 = 2 = 0` and `s_1 = 1`. Modulo `t` this gives `s_n ≡ 1` for `n ≥ 1`. So the coefficient `c_n` of `t` in `s_n` satisfies `c_n = c_{n−1} + 1` for `n ≥ 3`, with `c_2 = 0`, and `c_r = 1` for every odd `r ≥ 3`. So `s_r ≠ 1`, and `q_k ≠ 1`.

So `Q_k ≡ 1 (mod 2)` exactly when `k + 1` is a power of 2, and by Step 2 `char_k` is irreducible for those `k`.

*Total ramification.* For these `k`, `R_k` is Eisenstein at 2, so its 2-adic Newton polygon is one segment of slope `−1/(k + 1)`, and its roots `2/ρ` have 2-adic valuation `1/(k + 1)` in every extension of the 2-adic valuation to `Q(ρ)`. The ramification index of every prime of `Q(ρ)` over 2 is therefore at least `k + 1 = [Q(ρ) : Q]`, so there is one such prime and 2 is totally ramified. This proves the Theorem.

## Step 4 - the reach of the method

Write `char_k = Σ_i a_i λ^i` and `v` for the 2-adic valuation, so `v(a_0) = k` and `v(a_{k+1}) = 0`. The 2-adic Newton polygon of `char_k` is the single segment from `(0, k)` to `(k + 1, 0)` exactly when `v(a_i) ≥ k(k + 1 − i)/(k + 1)` for every `i`. For `1 ≤ i ≤ k`, `k(k + 1 − i)/(k + 1)` lies strictly between `k − i` and `k + 1 − i`, so for integer valuations the condition is `v(a_i) ≥ k + 1 − i`. The coefficient of `μ^i` in `Q_k` is `a_i 2^{i−k}`, and it is even exactly when `v(a_i) ≥ k + 1 − i`. So the polygon is one segment exactly when Equation (3) holds. A single segment of slope `−k/(k + 1)`, with `gcd(k, k + 1) = 1`, proves irreducibility over the 2-adic numbers (Dumas's generalization of Eisenstein's criterion), and it does so for the same `k`. For every other odd `k`, neither Eisenstein's criterion nor Dumas's at the prime 2 applies.[^3]

| `k` | `Q_k mod 2` | `R_k` Eisenstein at 2 | `char_k` irreducible over `Q` |
|---|---|---|---|
| 1 | `1` | yes: `R_1 = μ² − 2μ + 2` | proved |
| 3 | `1` | yes: `R_3 = μ⁴ − 2μ³ + 4μ² − 4μ + 2` | proved |
| 5 | `1 + μ⁴` | no | computed |
| 7 | `1` | yes | proved |
| 9, 11, 13 | not 1 | no | computed |
| 15 | `1` | yes | proved |

For odd `k ≤ 31` other than `1, 3, 7, 15, 31`, `char_k` is irreducible by computation, with no proof.[^3]

## Snippet

```python
import sympy as sp
mu = sp.symbols('mu')
Q = [sp.Poly(2*mu - 1, mu), sp.Poly(2*mu**2 - 2*mu + 1, mu)]
for k in range(1, 80):
    Q.append(sp.Poly(mu**2, mu)*Q[k-1] - Q[k])         # Equation (2)
def eis_rev(P):                                         # is the reversal of P Eisenstein at 2?
    co = P.all_coeffs()[::-1]
    return co[0] % 2 == 1 and all(a % 2 == 0 for a in co[1:]) and co[-1] % 4 != 0
print([k for k in range(81) if eis_rev(Q[k])])
# modulo 2, as bitmasks over F_2[t]: q_{k+1} = q_k + t q_{k-1}
q = [1, 1]
for k in range(1, 5000): q.append(q[k] ^ (q[k-1] << 1))
print([k for k in range(5001) if q[k] == 1])
```

```
[0, 1, 3, 7, 15, 31, 63]
[0, 1, 3, 7, 15, 31, 63, 127, 255, 511, 1023, 2047, 4095]
```

## Appearances in Sources

- [[calugareanu-hamburg-exercises-basic-ring-theory](pages/calugareanu-hamburg-exercises-basic-ring-theory.md)] - exercise 17.21, Eisenstein's criterion over a unique factorization domain, with Gauss's lemma.

## Related Concepts

- [[signed-tower-count](pages/signed-tower-count.md)] - `P(k, ·)`, `char_k`, and the recurrence of `den_k` behind Equation (1).
- [[tower-parity-sectors](pages/tower-parity-sectors.md)] - the involution `JD`, the factors of `char_k` for even `k`, and the product `g·ḡ` over `Q(i)` for odd `k`.
- [[finite-fields](pages/finite-fields.md)] - the Frobenius map in characteristic `p`, used in Step 3.
- [[castle-cryptography-number-theory](pages/castle-cryptography-number-theory.md)] - `char_1`, `char_3` and `char_5` as irreducible polynomials; the first two are proved irreducible here.
- [[larger-prime-periodicity](pages/larger-prime-periodicity.md)] - the discriminants of `char_k` for `k ≤ 10` and their odd prime factors.
- [[castle-ring-spectrum](pages/castle-ring-spectrum.md)] - the case `k = 1`: `Z[λ]/(char_1) ≅ Z[i]` by `λ ↦ 1 + i`, the prime `(2, λ)` maps to `(1 + i)`, and `2 = −i(1 + i)²`.

## Footnotes

[^1]: [[calugareanu-hamburg-exercises-basic-ring-theory](pages/calugareanu-hamburg-exercises-basic-ring-theory.md)] Ex. 17.21 p.76; solution pp.193-194 [synthesis] - Eisenstein's criterion over a UFD `R` gives irreducibility in `K[X]` for `K` the fraction field, and in `R[X]` when the polynomial is primitive; the solution reduces the `K[X]` case to `R[X]` by clearing denominators (Gauss's lemma).
[^2]: Verified by execution (Python 3.11 with SymPy, 2026-10-16): Equation (1) against `char_k` built from the `num`/`den` update for `k ≤ 80`; `char_k(2μ) = 2^k Q_k` with `Q_k` from Equation (2) for `k ≤ 80`, each with integer coefficients, leading coefficient 2 and constant term `±1`.
[^3]: Verified by execution (Python 3.11 with SymPy, 2026-10-16): the reversal of `Q_k` is Eisenstein at 2 exactly for `k ∈ {0, 1, 3, 7, 15, 31, 63}` among `k ≤ 80`; the 2-adic Newton polygon of `char_k` is one segment exactly for `k ∈ {1, 3, 7, 15, 31, 63}` among odd `k ≤ 69`; the bitmask recurrence over `F_2[t]` gives `q_k = 1` exactly for `k = 2^m − 1` among `k ≤ 5000`; `char_k` has one irreducible factor, of multiplicity 1, for every odd `k ≤ 31`; `R_1`, `R_3` and `Q_5 mod 2` as in the table. The proof in Step 3 is by hand, and the first three checks are consistency checks on it.
