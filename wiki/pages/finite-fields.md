---
title: Finite fields for the castle count
category: Concepts
summary: Why the castle and tower counts are periodic modulo a prime p. Over the rationals P(1, L) = Re((1+i)^{L+1}) never repeats, since |1 + i| = √2; modulo p the roots of char_k lie in finite fields F_{p^d}, whose nonzero elements form a cyclic group of order p^d − 1, so every root has finite order and the sequence is periodic. Worked from F_5 (period 4) and F_49 (period 24) to the general rule, with the effect of repeated roots (A^e(·, 4) mod 7 has period 8400 = 7 · 1200) and the Frobenius map.
tags: [concept, finite-field, modular-arithmetic, periodicity, pedagogy]
sources: [project-euler-502-representations, calugareanu-hamburg-exercises-basic-ring-theory]
created: 2026-09-14
updated: 2026-10-25
---

# Finite fields for the castle count

Over the rationals, the signed tower count is a sum of powers of the roots of its characteristic polynomial, `P(k, L) = Σ_i p_i(L) λ_i^L` ([[signed-tower-count](pages/signed-tower-count.md)]). Modulo a prime `p`, the roots become elements of a **finite field** `F_{p^d}`, a field with `p^d` elements. Its nonzero elements form a cyclic group of order `p^d − 1` under multiplication, so every root has finite order, and the sequence `P(k, ·) mod p` is periodic. This page works this out for `P(1, ·)` at `p = 5` and `p = 7` and then states the general rule; [[mod-p-observatory](pages/mod-p-observatory.md)] tabulates the periods.

## Over the rationals

`P(1, L) = Re((1+i)^{L+1})` has characteristic polynomial `char_1(λ) = λ² − 2λ + 2`, with roots `1 ± i`:[^1]

```
P(1, L)  =  1, 0, −2, −4, −4, 0, 8, 16, …
```

Since `|1 ± i| = √2 > 1`, the values grow in absolute value along every period of 4 (`P(1, L + 4) = −4 P(1, L)`), and the sequence never repeats.

## Modulo 5: the roots lie in F_5

`−1 ≡ 4 = 2² (mod 5)`, so `i = ±2` in `F_5`, and the roots `1 ± i` are `3` and `4`. The nonzero elements `{1, 2, 3, 4}` of `F_5` form a cyclic group of order 4; `3` has order 4 and `4` has order 2. So `P(1, L) mod 5` has period `lcm(4, 2) = 4`:[^2]

```
P(1, L) mod 5  =  1, 0, 3, 1, 1, 0, 3, 1, …
```

## Modulo 7: the roots lie in F_49

Modulo 7 the squares are `{1, 2, 4}`, and `−1 ≡ 6` is not among them, so `char_1` does not factor over `F_7`. The roots lie in `F_7[x]/(x² + 1) = F_49`, a field of 49 elements, whose nonzero elements form a cyclic group of order 48. In it, `(1 + i)^2 = 2i`, `(1 + i)^4 = −4 = 3`, and `3` has order 6 in `F_7`, so `1 + i` has order 24, and[^2]

```
P(1, L) mod 7  has period 24.
```

## The general rule

Reduce `char_k` modulo `p` and factor it into irreducible polynomials over `F_p`. An irreducible factor of degree `d` has its `d` roots in `F_{p^d}`, whose nonzero elements form a cyclic group of order `p^d − 1`; by Lagrange's theorem, the order of every element divides the order of the group. So:

1. each simple root `λ` has an order dividing `p^d − 1`, and `λ^L` is periodic in `L` with period `ord(λ)`;
2. the sequence has period the **lcm** of the periods of its terms.

For `char_1`, the discriminant is `−4`, so for odd `p` it factors over `F_p` exactly when `−1` is a square modulo `p`, which by Euler's criterion is when `p ≡ 1 (mod 4)`. So it factors modulo 5 and is irreducible modulo 3 and 7.

**Repeated roots.** A root of multiplicity `m` contributes the terms `C(L, j) λ^L` for `j < m`, and for `m ≤ p` the binomial coefficients `C(L, j)` are periodic modulo `p` with period `p`. So a double root multiplies the period it contributes by `p`. Modulo 7, `char_2 = (λ − 2)(λ + 3)²`, with roots of order 3, so `P(2, ·) mod 7` has period `3 · 7 = 21`, and `A^e(·, 4) mod 7` has period `8400 = 7 · 1200`.[^2]

**Primitive roots.** A root that generates the cyclic group `F_{p^d}^*` has the full order `p^d − 1`. If `char_{h−1}` stays irreducible of degree `h` modulo `p`, the period of `A^e(·, h) mod p` can be as large as `p^h − 1`, far too long to observe at `p = 10^9 + 7`; it is computed as an order, not by listing terms.

## The Frobenius map

In characteristic `p` the map `a ↦ a^p` preserves sums as well as products, `(a + b)^p = a^p + b^p`, and on a field it is injective.[^3] It permutes the roots of each irreducible factor (`λ ↦ λ^p`), and `λ^p` has the same order as `λ`, since `p` is prime to the order; so all roots of one irreducible factor have the same order.

At every `p ≡ 3 (mod 4)` the roots of `char_1` lie in `F_p[x]/(x² + 1)`, as for `F_49` in the section *Modulo 7*. At `p = 3` this is the field of 9 elements `F_3[i] = Z[i]/(3)`.[^4] Since `char_1(x) = (x − 1)² + 1`, the ring `Z[x]/(char_1)` is `Z[i]` with `x ↦ 1 + i`, and `Z[i]/(3)` is its reduction modulo 3.

When `char_k mod p` has several distinct irreducible factors, the ring `F_p[x]/(char_k)` is the product of the corresponding fields (and of local rings for repeated factors), by the [[chinese-remainder-theorem](pages/chinese-remainder-theorem.md)]; the period is the lcm of the periods of the factors.

**Polynomials and functions.** Over `F_q` every function `F_q → F_q` is a polynomial of degree less than `q`, by Lagrange interpolation, and two polynomials give the same function exactly when they differ by a multiple of `x^q − x`: over `F_3`, `x^5 + x^3 + x` and `x^5 + 2x` are different polynomials and the same function.[^5][^6] So although `a^p = a` for every `a ∈ F_p`, in the ring `F_p[x]/(char_k)` the element `x^p` equals `x` only when `char_k mod p` divides `x^p − x`, that is, when it splits into distinct linear factors over `F_p`; then the period divides `p − 1`. Kitamasa's method computes `x^n mod char_k` in this ring ([[kitamasa](pages/kitamasa.md)]).

## Appearances in Sources

- [[project-euler-502-representations](pages/project-euler-502-representations.md)] - the recurrence `P(1, L) = 2P(1, L−1) − 2P(1, L−2)` and the closed form `P(1, L) = Re((1+i)^{L+1})`.
- [[calugareanu-hamburg-exercises-basic-ring-theory](pages/calugareanu-hamburg-exercises-basic-ring-theory.md)] - the Frobenius map, the field of 9 elements, polynomial functions over a finite field.

## Related Concepts

- [[mod-p-observatory](pages/mod-p-observatory.md)] - the periods of the castle and tower counts modulo small primes, and the pigeonhole proof that they are periodic.
- [[signed-tower-count](pages/signed-tower-count.md)] - `P(1, L) = Re((1+i)^{L+1})` and the polynomials `char_k`.
- [[generating-function-gallery](pages/generating-function-gallery.md)] - the rational functions `num_k/den_k` whose denominators give `char_k`.
- [[chinese-remainder-theorem](pages/chinese-remainder-theorem.md)] - the product decomposition over the distinct irreducible factors.
- [[char-k-eisenstein-at-two](pages/char-k-eisenstein-at-two.md)] - the Frobenius map in characteristic 2, `(α + β)^{2^m} = α^{2^m} + β^{2^m}`, in the proof that `char_k` is irreducible over the rationals for `k = 2^m − 1`.
- [[castle-ring-spectrum](pages/castle-ring-spectrum.md)] - the rings `F_p[x]/(char_k)` over each prime, and their structure read from the Frobenius matrix.
- [[oeis-mining-pe502](pages/oeis-mining-pe502.md)] - the castle counts matched against the OEIS, among them `P(1, L) = A146559(L+1)` and the polynomials `char_k`.

## Footnotes

[^1]: [[project-euler-502-representations](pages/project-euler-502-representations.md)] §"Signed count" L345 - "k=1: P(1,L) = 2P(1,L-1) - 2P(1,L-2), closed form P(1,L) = Re((1+i)^{L+1})".
[^2]: Verified by execution (Python 3.11 with SymPy, 2026-10-16): `P(1, L) mod 5` with period 4, `mod 7` with period 24 and `mod 3` with period 8; the order 24 of `1 + i` in `F_49`; `char_2 ≡ (λ − 2)(λ + 3)² (mod 7)`; the periods 21 of `P(2, ·) mod 7`, 400 of `P(3, ·) mod 7`, and 8400 of `A^e(·, 4) mod 7`, from 60,000 terms.
[^3]: [[calugareanu-hamburg-exercises-basic-ring-theory](pages/calugareanu-hamburg-exercises-basic-ring-theory.md)] Ex. 5.14 p.25; solution p.113 [synthesis] - `x ↦ x^{p^n}` is an injective ring homomorphism of a field of characteristic `p`.
[^4]: [[calugareanu-hamburg-exercises-basic-ring-theory](pages/calugareanu-hamburg-exercises-basic-ring-theory.md)] Ex. 5.11 p.24; solution p.112 [synthesis] - `Z_3 × Z_3` with Gaussian multiplication `(a, b)(c, d) = (ac − bd, ad + bc)` is a field of 9 elements.
[^5]: [[calugareanu-hamburg-exercises-basic-ring-theory](pages/calugareanu-hamburg-exercises-basic-ring-theory.md)] Ex. 17.13 p.75; solution p.191 [synthesis] - over a finite field `K`, `P(X) = Σ_{a ∈ K} f(a) ∏_{b ≠ a} (X − b)/(a − b)` agrees with `f` everywhere, so every map `K → K` is polynomial.
[^6]: [[calugareanu-hamburg-exercises-basic-ring-theory](pages/calugareanu-hamburg-exercises-basic-ring-theory.md)] Ex. 14.10 p.60; solution p.170 [synthesis] - `f = X⁵ + X³ + X`, `g = X⁵ + 2X` over `Z_3` agree at `0, 1, 2`.
