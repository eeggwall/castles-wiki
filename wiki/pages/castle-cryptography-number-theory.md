---
title: Castle cryptography - the number theory, for engineers
category: Analyses
summary: The three terms the castle cryptosystem uses, explained from the castle_dh code. The characteristic polynomial records the recurrence of P(k, ·) (the feedback polynomial of a linear feedback shift register) and is the modulus Q of the ring F_p[x]/(Q). An irreducible polynomial is the polynomial analogue of a prime: a reducible Q splits the discrete logarithm problem (DLP) into smaller ones by the Chinese Remainder Theorem, while a Q irreducible mod p makes the ring one field F_{p^d}. An irreducible Q is not enough for security: p^d − 1 = ∏ Φ_e(p) factors for every p, so Pohlig-Hellman still applies, finite fields have subexponential index-calculus attacks, and Berlekamp-Massey recovers any linear output whatever Q is.
tags: [analysis, cryptography, number-theory, characteristic-polynomial, irreducible-polynomial, discrete-logarithm, finite-field, pedagogy, engineer, castle]
sources: [oeis-mining-pe502]
created: 2026-09-18
updated: 2026-10-25
---

# Castle cryptography - the number theory, for engineers

The [[castle-cryptography](pages/castle-cryptography.md)] seminar series uses three number-theory terms. This page explains them from scratch, using the running `castle_dh` code.

## The characteristic polynomial

In `castle_dh`, the modulus was `Q = [-4, 4, -3, 1]`, i.e. `Q(x) = x³ − 3x² + 4x − 4`. That is the **characteristic polynomial** `char_2` of the signed tower count `P(2, L) = 1, 1, 3, 9, 19, 33, 59, …` ([[signed-tower-count](pages/signed-tower-count.md)]), which satisfies a **linear recurrence**:

```
P(2,L)  =  3·P(2,L−1)  −  4·P(2,L−2)  +  4·P(2,L−3).
```

The characteristic polynomial records the coefficients of the recurrence. For a linear feedback shift register (LFSR), a register whose next value is a fixed linear combination of the previous ones, it is the feedback polynomial. With the initial terms it determines the whole sequence, and [[kitamasa](pages/kitamasa.md)]'s method computes a far term from it in `O(d² log L)` operations.

Three coefficients and three seeds regenerate the sequence:

```python
def p2(L):               # char_2 = x^3 - 3x^2 + 4x - 4  =>  P(L) = 3P(L-1) - 4P(L-2) + 4P(L-3)
    if L < 3: return (1, 1, 3)[L]
    return 3*p2(L-1) - 4*p2(L-2) + 4*p2(L-3)
```

```
>>> [p2(L) for L in range(8)]
[1, 1, 3, 9, 19, 33, 59, 121]
```

That is `P(2, L)` for `L = 0, …, 7`. The coefficients `(3, −4, 4)` give the polynomial `x³ − 3x² + 4x − 4`, and with the initial values `(1, 1, 3)` they determine the sequence.[^2]

In the cryptosystem, `Q` is the **modulus**: arithmetic is mod `Q`, so whenever a product reaches degree 3, `x³` is replaced by `3x² − 4x + 4`, which brings it back below degree 3. The replacement is the recurrence, applied to polynomials instead of numbers. The ring is `F_p[x]/(Q)`: polynomials of degree less than 3 with coefficients mod `p`.

## Irreducible polynomials, the analogue of primes

**Irreducible is the polynomial analogue of prime.**

- A **prime integer** doesn't factor into smaller integers > 1: `7` is prime, `12 = 3·4` is not.
- An **irreducible polynomial** doesn't factor into smaller-degree polynomials over the given field: `x² + 1` is irreducible over the reals, `x² − 1 = (x−1)(x+1)` is not.

For the castle characteristic polynomials the split goes by the parity of `k`: `char_k` is irreducible over the rationals for odd `k ≤ 31` and has exactly two irreducible factors for even `k ≤ 40` (computed; [[signed-tower-count](pages/signed-tower-count.md)], [[tower-parity-sectors](pages/tower-parity-sectors.md)]). The first six:[^1]

| | char poly | factors? |
|---|---|---|
| **even `k`** (`char_2` is used in `castle_dh`) | `char_2 = x³−3x²+4x−4 = (x−2)(x²−x+2)` | **reducible** (composite) |
| | `char_4 = (x²−2x+4)(x³−3x²+2x−4)` | reducible |
| | `char_6 = (x³−4x²+4x−8)(x⁴−3x³+8x²−4x+8)` | reducible |
| **odd `k`** | `char_1 = x²−2x+2` | **irreducible** (prime) |
| | `char_3 = x⁴−4x³+8x²−8x+8` | irreducible |
| | `char_5 = x⁶−6x⁵+18x⁴−32x³+48x²−32x+32` | irreducible |

The split, verified in one line:

```python
import sympy as sp
x = sp.Symbol('x')
sp.factor(x**3 - 3*x**2 + 4*x - 4)          # char_2 : composite
sp.factor(x**4 - 4*x**3 + 8*x**2 - 8*x + 8)  # char_3 : irreducible
```

```
>>> sp.factor(x**3 - 3*x**2 + 4*x - 4)
(x - 2)*(x**2 - x + 2)
>>> sp.factor(x**4 - 4*x**3 + 8*x**2 - 8*x + 8)
x**4 - 4*x**3 + 8*x**2 - 8*x + 8
```

`factor` returns `char_3` unchanged: it has no factor over `ℚ`.[^3] For `char_1` and `char_3` there is also a proof: substitute `x = 2y`, divide by `2^k`, reverse the coefficients, and the result (`y⁴ − 2y³ + 4y² − 4y + 2` for `char_3`) is Eisenstein at 2. That works for exactly `k = 1, 3, 7, 15, …` ([[char-k-eisenstein-at-two](pages/char-k-eisenstein-at-two.md)]); the irreducibility of `char_5` is computed.

Irreducibility depends on the field. The table is over the rationals `ℚ`. Mod a prime `p`, a polynomial irreducible over `ℚ` can still split ([[finite-fields](pages/finite-fields.md)]): `char_3` splits into four linear factors mod 101 and stays irreducible mod `10⁹ + 7`.[^4] For the quadratic `char_1`, with discriminant `−4`, the question is whether `−1` is a square mod `p`, which Euler's criterion answers: it is irreducible exactly when `p ≡ 3 (mod 4)`. A factorization over the integers holds mod every `p`, so `char_2` splits mod every prime.

## The discrete logarithm problem (DLP)

The security of `castle_dh` rests on the gap between two directions:

- **Forward:** given a secret exponent `a`, compute the public key `A = x^a mod Q`. That is `powmod`: for `a = 10¹²`, 39 squarings and 12 multiplications ([[castle-cryptography-ring](pages/castle-cryptography-ring.md)], section 3).
- **Backward:** given `A` and `Q`, recover `a`. That is the **discrete logarithm**: which power of `x` gives `A`? Generic attacks, which use only the group operation, cost about the square root of the largest prime factor of the order of `x`.

Classic Diffie-Hellman has the same two directions, with numbers mod a prime in place of polynomials mod `Q`. "Discrete" refers to the finite group, and "logarithm" means the exponent.

## Reducible and irreducible `Q`

This is why Fix 1 of [[castle-cryptography](pages/castle-cryptography.md)] replaces an even-`k` `Q` by an odd-`k` one.

**Reducible `Q` (even `k`): the DLP splits.** Because `char_2 = (x−2)(x²−x+2)`, the ring `F_p[x]/(Q)` splits by the **Chinese Remainder Theorem** ([[chinese-remainder-theorem](pages/chinese-remainder-theorem.md)]) into one ring per factor:

- the factor `x − 2` has degree 1, and its piece is `F_p`, an ordinary discrete logarithm mod `p`;
- the factor `x² − x + 2` has degree 2, and its piece is `F_{p²}` when the factor is irreducible mod `p`.

The attacker solves the two smaller discrete logarithms separately and combines them by the CRT. At `p = 101`:

```
reducible char_2:   pieces of group order (p−1) = 100  and  (p²−1) = 10200
an irreducible quartic:   one group of order  p⁴−1 = 104,060,400
```

(`char_3` itself splits into four linear factors mod 101, so at this `p` it would not give the quartic field; at `p = 10⁹ + 7` it does.)

**Irreducible `Q` (odd `k`): no split of the ring.** When `Q` stays irreducible mod `p`, `F_p[x]/(Q)` is the field `F_{p^d}`, and the DLP is the discrete logarithm in `F_{p^d}^*`, of order `p^d − 1`. The ring gives no CRT split.

The order of the group still factors, for every `p` and whatever `Q` is: `p² − 1 = (p − 1)(p + 1)`, `p⁴ − 1 = (p − 1)(p + 1)(p² + 1)`, and in general `p^d − 1 = ∏_{e | d} Φ_e(p)` with `Φ_e` the `e`-th cyclotomic polynomial. So Pohlig-Hellman runs on the prime factors of the order instead of the factors of the modulus, and its cost is about the square root of the largest prime dividing the order of `x`. At `p = 10⁹ + 7` that prime is `500000003 ≈ 2^28.9` for both `char_1` and `char_3`, and Attack 4 of [[castle-cryptography-round-two](pages/castle-cryptography-round-two.md)] recovers the private key in both cases. The norm forces `500000003` into the order of `x` for every `k` at this prime, since the norm of `x` is `2^k` and `2` has order `500000003` mod `p` ([[castle-cryptography-ring](pages/castle-cryptography-ring.md)], section 8). An irreducible `Q` removes the split of the ring; the split of the group is removed only by choosing `p` so that `Φ_d(p)` has a large prime factor.


| | reducible `Q` (even `k`) | irreducible `Q` (odd `k`, irreducible mod `p`) |
|---|---|---|
| `Q` factors? | yes, `(x−2)(x²−x+2)` | no |
| ring `F_p[x]/(Q)` | splits by the CRT | one field `F_{p^d}` |
| discrete logarithm | one per factor, combined by the CRT | one in `F_{p^d}^*`, split by Pohlig-Hellman along `p^d − 1` |

## Two caveats

1. **An irreducible `Q` is not enough.** Discrete logarithms in `F_{p^d}` have a subexponential attack, index calculus, of cost `L_q[1/3]` in the field size `q = p^d`, so the field must have about 3072 bits for 128-bit security ([[castle-cryptography-round-three](pages/castle-cryptography-round-three.md)]). Before index calculus, the factorization of `p^d − 1` already sets the generic cost by the largest prime factor of `Φ_d(p)`, not by `p^d`; round two sizes it ([[castle-cryptography-round-two](pages/castle-cryptography-round-two.md)], Fix 4). The norm comes first: `N(A) = 2^{ka}` carries every public key into `F_p^*`, where one discrete logarithm gives `ka` modulo the order of 2 ([[castle-cryptography-ring](pages/castle-cryptography-ring.md)], section 9).
2. **Berlekamp-Massey recovers `Q` whatever it is.** It finds the shortest linear recurrence of a sequence from twice as many terms as its order ([[berlekamp-massey](pages/berlekamp-massey.md)]), irreducible or not. A public key read as castle counts is a window of `d` consecutive terms ([[castle-cryptography-ring](pages/castle-cryptography-ring.md)], section 5), half of what Berlekamp-Massey needs. If a scheme publishes `2d` consecutive terms of `P(k, ·) mod p`, `Q` is recovered, so the fix for published output is a nonlinear filter (Fix 2 of [[castle-cryptography](pages/castle-cryptography.md)]), which round two's Attack 5 also breaks at small sizes.

## Appearances in Sources

- [[oeis-mining-pe502](pages/oeis-mining-pe502.md)] - the `P(k,·)` families and their characteristic polynomials.

## Related Concepts

- [[castle-cryptography](pages/castle-cryptography.md)] - the build / red-team / blue-team seminar series this page supports.
- [[castle-cryptography-ring](pages/castle-cryptography-ring.md)] - Seminar 1 in full: the ring `F_p[x]/(Q)`, the key exchange and its windows of castle counts, the element orders and the norm.
- [[castle-cryptography-round-two](pages/castle-cryptography-round-two.md)] - the second lap, where the irreducible-`Q` fix is shown necessary but not sufficient (group-order Pohlig–Hellman) and the keys are sized.
- [[finite-fields](pages/finite-fields.md)] - `F_{p^d}`, cyclic groups, and why over-`ℚ`-irreducible polys can still split mod `p`.
- [[kitamasa](pages/kitamasa.md)] - `x^a mod Q` by binary exponentiation, the easy forward direction.
- [[berlekamp-massey](pages/berlekamp-massey.md)] - recovers the char poly from the output; the linearity attack no modulus choice fixes.
- [[signed-tower-count](pages/signed-tower-count.md)] / [[generating-function-gallery](pages/generating-function-gallery.md)] - where the `char_k` characteristic polynomials come from, and the even/odd factorization pattern.
- [[tower-parity-sectors](pages/tower-parity-sectors.md)] - why `char_k` factors for even `k`, the factorization that Attack 1 of [[castle-cryptography](pages/castle-cryptography.md)] uses.
- [[new-sequence-fw3](pages/new-sequence-fw3.md)] - `A^e(w, 3)`, whose characteristic polynomial contains `char_2`; its recurrence has order 6, not 7, because the root 2 of the factor `x − 2` is also the root of the term `2^w`.
- [[castle-ring-invariant-factors](pages/castle-ring-invariant-factors.md)] - the unit group `R^*` as a product of cyclic groups for reducible and irreducible `Q` alike, and Pohlig-Hellman as the reduction to prime-order parts.
- [[char-k-eisenstein-at-two](pages/char-k-eisenstein-at-two.md)] - the Eisenstein proof behind the odd-`k` rows for `k = 2^m − 1`.
- [[chinese-remainder-theorem](pages/chinese-remainder-theorem.md)] - the ring-level CRT that splits a reducible `Q`.


## Footnotes

[^1]: Verified by execution (SymPy, 2026-10-16): `char_1, char_3, char_5` (odd `k`) are irreducible over `ℚ`; `char_2 = (x−2)(x²−x+2)`, `char_4 = (x²−2x+4)(x³−3x²+2x−4)`, `char_6 = (x³−4x²+4x−8)(x⁴−3x³+8x²−4x+8)` (even `k`) factor. The even-`k` factorization is the tower-parity-sector structure ([[tower-parity-sectors](pages/tower-parity-sectors.md)]); the `x³−4x²+4x−8` factor of `char_6` is the plastic-number factor (`2ψ²`, [[plastic-number](pages/plastic-number.md)]).

[^2]: Verified by execution (Python 3.11, 2026-10-16): `[p2(L) for L in range(8)] = [1, 1, 3, 9, 19, 33, 59, 121]` — the recurrence `P(L) = 3P(L−1) − 4P(L−2) + 4P(L−3)` with seeds `(1, 1, 3)` reproduces `P(2, ·)` exactly.

[^3]: Verified by execution (SymPy, 2026-10-16): `sp.factor(x**3 − 3*x**2 + 4*x − 4) = (x − 2)*(x**2 − x + 2)` (composite) and `sp.factor(x**4 − 4*x**3 + 8*x**2 − 8*x + 8)` returns the polynomial unchanged (irreducible).
[^4]: Verified by execution (SymPy, 2026-10-16): `char_3 mod 101 = (x + 21)(x + 24)(x − 26)(x − 23)`, and `char_3` is irreducible mod `10⁹ + 7`; `10⁹ + 7 ≡ 3 (mod 4)`.
