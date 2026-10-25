---
title: Castle cryptography - a build / red-team / blue-team seminar series
category: Analyses
summary: A three-seminar series on a toy public-key system built from the signed tower count. The public parameters are a prime p and Q = char_k mod p, a private key is an exponent a, the public key is x^a mod Q, and Diffie-Hellman key exchange is exponentiation in F_p[x]/(Q), the step Kitamasa's method performs. Seminar 1 builds the system; Seminar 2 breaks it two ways (even-k char_k factor, so the ring splits by the CRT and the discrete log splits; Berlekamp-Massey recovers Q from 2 deg Q terms of any published stream); Seminar 3 closes both breaks (an irreducible Q mod p; a nonlinear filter, whose linear complexity is at most C(d+e-1, e)) and names the remaining ceiling, index calculus in F_{p^d}. Rounds two and three of the series break and rebuild the fixes.
tags: [analysis, seminar, cryptography, public-key, finite-field, kitamasa, berlekamp-massey, discrete-log, diffie-hellman, cryptanalysis, red-team, blue-team, pedagogy, implementation, castle]
sources: [project-euler-502-representations]
created: 2026-09-18
updated: 2026-10-25
---

# Castle cryptography

## The series

Three seminars, one per phase of security work:

1. **Seminar 1 - Build.** A public-key system whose public modulus comes from the signed tower count, implemented as short programs, with Diffie-Hellman key exchange between two parties. Security is not evaluated in this seminar.
2. **Seminar 2 - Red team.** Two attacks on the system, each a small instance of a standard attack.
3. **Seminar 3 - Blue team.** A fix for each attack, and the attack that remains after both fixes.

The series runs three times. [[castle-cryptography-round-two](pages/castle-cryptography-round-two.md)] is the second round: it adds ElGamal encryption and a Schnorr-style signature, recovers a private key, breaks both fixes of this page, sizes the keys against the three attacks (the largest prime factor of the group order, the linear complexity, index calculus), and states four questions to ask of a new cryptosystem. [[castle-cryptography-round-three](pages/castle-cryptography-round-three.md)] is the third: it builds on `char_5`, a field of degree 6, in a prime-order subgroup of the torus (the XTR/CEILIDH construction), which closes the subfield attack of round two, and sizes the remaining index-calculus attack against the extended tower number field sieve.

## The shared setup

The signed tower count `P(k, L)` satisfies a linear recurrence in `L` with characteristic polynomial `char_k(x)` of degree `k + 1` ([[signed-tower-count](pages/signed-tower-count.md)]); for example `char_2(x) = x³ − 3x² + 4x − 4`. Reducing `char_k` modulo a prime `p` gives a polynomial `Q(x)` over the field `F_p` with `p` elements, and the arithmetic of the series takes place in the quotient ring

```
R  =  F_p[x] / (Q(x)),        Q  =  char_k mod p.
```

Multiplying two elements of `R` means multiplying polynomials and reducing modulo `Q`, which rewrites `x^{deg Q}` by the recurrence, the same reduction [[kitamasa](pages/kitamasa.md)]'s method uses. The public parameters are `p` and `Q`; a private key is an exponent `a`, and the matching public key is `x^a mod Q`.

---

# Seminar 1 - Build

[[castle-cryptography-ring](pages/castle-cryptography-ring.md)] is Seminar 1 in full, in the order the system is used: the recurrence and `char_k`, the ring `R` with multiplication by `x` as one step of the recurrence, the cost of Kitamasa's method, a Diffie-Hellman exchange with private keys `a = 373309869` and `b = 566180101` at `p = 10⁹ + 7`, and the same exchange run on windows of castle counts. It then describes the group the keys live in: the period of `P(k, ·) mod p` as the order of `x` at every odd prime, the order of `x` for `k ≤ 7` at two primes, and the norm `2^k` of `x`.

1. **Periodicity.** Modulo `p`, the roots of `Q` lie in a finite field `F_{p^d}`, where every nonzero element has finite multiplicative order, so `P(k, ·) mod p` is periodic ([[finite-fields](pages/finite-fields.md)], [[mod-p-observatory](pages/mod-p-observatory.md)]). Its period is the order of `x` in `R` at every odd prime: the update of the numerator and denominator of its generating function has determinant `−1`, so they are coprime mod every prime.
2. **The forward map.** `x^a mod Q` is computed by binary exponentiation in `O(deg(Q)² · log a)` operations; at `a = 10^12` that is 39 squarings and 12 multiplications. This is the computation of [[kitamasa](pages/kitamasa.md)]'s method.
3. **Key exchange.** With public parameters `(p, Q = char_2 mod p)` and generator `x`, the two parties publish `A = x^a mod Q` and `B = x^b mod Q`, and each computes `x^{ab} mod Q` from the other's public key and its own exponent.
4. **The public key is a window of castle counts.** `x^a mod Q` determines `P(k, a), …, P(k, a + k) mod p` and is determined by it, through the Hankel matrix of the first `2k + 1` terms, of determinant `±2^{k²}` for `k ≤ 7` and invertible mod every odd prime. The private key is a base length, and the public key is a signed tower count.
5. **The norm.** The determinant of multiplication by `x` is `2^k`, so the order of `2^k` in `F_p^*` divides the order of `x`; at `p = 10⁹ + 7` the prime `500,000,003 = (p − 1)/2` divides it for every `k`.

The `mulmod` and `powmod` functions and their output are on [[castle-cryptography-ring](pages/castle-cryptography-ring.md)] and [[castle-snippets-cryptography](pages/castle-snippets-cryptography.md)].

---

# Seminar 2 - Red team

## Attack 1 - the modulus factors, so the discrete log splits

For even `k`, `char_k` factors over the rationals ([[tower-parity-sectors](pages/tower-parity-sectors.md)]); for example `char_2(x) = (x − 2)(x² − x + 2)`. When `Q` factors, the Chinese remainder theorem splits `R` into one ring per factor: for `char_2`, the field `F_p` and the ring `F_p[x]/(x² − x + 2)`, which is the field `F_{p²}` when `x² − x + 2` is irreducible mod `p`. The discrete logarithm of a public key splits into discrete logarithms in the unit groups of the factors, solved separately and recombined by the CRT on the exponents, and each of those splits further over the prime factors of its group order (Pohlig-Hellman). A system whose security rests on the discrete logarithm uses a group whose order has a large prime factor.

**The split at `p = 101`.** There `x² − x + 2` is irreducible, since its discriminant `−7` is not a square mod 101, so the CRT gives `R ≅ F_101 × F_{101²}` ([[chinese-remainder-theorem](pages/chinese-remainder-theorem.md)]), and the projections can be computed. For `Q = char_2 mod 101 = (x − 2)(x² − x + 2)` and `A = 7 + 3x + 5x²`:[^1]

- mod `x − 2`: substitute `x = 2`, giving `7 + 6 + 20 = 33` in `F_101`;
- mod `x² − x + 2`: reduce `A`, giving `98 + 8x` in `F_101[x]/(x² − x + 2) ≅ F_{101²}`.

Multiplication commutes with the projections. With `B = 2 + x²`:

```
A·B mod Q              =  86 + 55x + 51x²
mod x − 2:              A ↦ 33,  B ↦ 6,  33 · 6 = 97,  A·B ↦ 97
mod x² − x + 2:         A·B ↦ 85 + 5x,  (98 + 8x)(2 + x²) ↦ 85 + 5x
```

Element orders and discrete logarithms split along the factorization of `Q` in the same way, and Attack 3 of [[castle-cryptography-round-two](pages/castle-cryptography-round-two.md)] recovers a private key this way.

The inverse map uses the idempotents `e_1 = (x² − x + 2)/4 = 51 + 25x + 76x²` and `e_2 = 1 − e_1` mod `char_2` at `p = 101`. `e_1` is `1` mod `x − 2` and `0` mod `x² − x + 2`, so a pair of projections `(a_1, a_2)` lifts to `a_1 e_1 + a_2 e_2` in `R`. Multiplication by `e_1` keeps only the root `2`: `x^L e_1 = 2^L e_1` ([[idempotent-decomposition](pages/idempotent-decomposition.md)]).

## Attack 2 - Berlekamp-Massey recovers the modulus

Suppose a variant keeps `Q` secret and publishes the terms of a sequence that satisfies its recurrence, as a keystream. [[berlekamp-massey](pages/berlekamp-massey.md)] returns the shortest linear recurrence of the published terms, and it is the recurrence of `Q` once `2·deg(Q)` consecutive terms are known. The first six terms of `P(2, ·)`, `1, 1, 3, 9, 19, 33`, already give the coefficient vector `[1, −3, 4, −4]`, that is `char_2(x) = x³ − 3x² + 4x − 4`.[^2]

Any sequence that satisfies a linear recurrence of order `d` is recovered this way from `2d` terms, so a scheme that publishes terms of `P(k, ·) mod p` publishes `Q`. Read as castle counts, a public key is a window of `d = k + 1` consecutive terms ([[castle-cryptography-ring](pages/castle-cryptography-ring.md)], section 5), half of what Berlekamp-Massey needs, so a variant that keeps `Q` secret and publishes windows reveals `Q` as soon as `2d` consecutive terms are public.

## Seminar 2 verdict

The system as built is broken twice: once through the factorization of the modulus, once through the linearity of its output.

---

# Seminar 3 - Blue team

## Fix 1 - an irreducible modulus closes the CRT split

Attack 1 used the factorization of `Q`, so the fix is a `Q` that does not factor, an irreducible polynomial. For odd `k ≤ 31`, `char_k` is irreducible over the rationals, each `k` proved by a prime mod which it stays irreducible ([[castle-cryptography-number-theory](pages/castle-cryptography-number-theory.md)]), and `k = 2^m − 1` also by Eisenstein ([[char-k-eisenstein-at-two](pages/char-k-eisenstein-at-two.md)]): `char_1(x) = x² − 2x + 2`, `char_3(x) = x⁴ − 4x³ + 8x² − 8x + 8`, `char_5`, ….[^3] Irreducibility over the rationals is not enough: `Q` must stay irreducible modulo the chosen `p`. `char_1` is irreducible mod an odd prime `p` exactly when `p ≡ 3 (mod 4)`, and `char_3` splits into four linear factors mod 101 and is irreducible mod `10⁹ + 7`.[^3] For every odd `k`, `char_k = g·ḡ` over `Q(i)` ([[tower-parity-sectors](pages/tower-parity-sectors.md)]), so `char_k` can stay irreducible only at `p ≡ 3 (mod 4)`, as `10⁹ + 7` is and `101` is not; round three finds `char_5` irreducible mod a density `1/6` of primes ([[castle-cryptography-round-three](pages/castle-cryptography-round-three.md)]). With such a `p`, `R` is the single field `F_{p^d}`, `d = deg Q`, and the discrete logarithm lives in one cyclic group of order `p^d − 1`.

The split of the ring is gone, but the group order still factors: `p^d − 1 = Π_{e | d} Φ_e(p)`, with `Φ_e` the `e`-th cyclotomic polynomial, so Pohlig-Hellman applies to the group order, and round two recovers a private key from an irreducible `char_1` this way ([[castle-cryptography-round-two](pages/castle-cryptography-round-two.md)], Attack 4). The factor `Φ_1(p) = p − 1` is reached without Pohlig-Hellman: the norm of a public key, `N(A) = 2^{ka}`, lies in `F_p^*` and is computed from `A`, and at `k = 3`, with `R = F_{p⁴}` and `p = 10⁹ + 7`, one discrete logarithm in `F_p^*` returns the private key `373309869` ([[castle-cryptography-ring](pages/castle-cryptography-ring.md)], section 9). The fix needs `Φ_d(p)` to have a large prime factor as well. [[castle-cryptography-number-theory](pages/castle-cryptography-number-theory.md)] explains characteristic polynomials, irreducible polynomials and the discrete logarithm problem from the start, with the reducible and irreducible cases worked side by side.

## Fix 2 - a nonlinear filter raises the linear complexity

Attack 2 used the linearity of the output, which no choice of `Q` removes. The fix is a nonlinear filter: publish a polynomial function of several consecutive terms instead of the terms. If `s_n = Σ_i c_i λ_i^n` with `λ_1, …, λ_d` the roots of `Q`, a product of `e` terms is a sum over the degree-`e` monomials in the `λ_i`, so it satisfies a linear recurrence of order at most `C(d + e − 1, e)`, and Berlekamp-Massey recovers that recurrence from twice as many terms. Round two measures the orders 10, 14 and 20 for the filters `s_n s_{n+1}`, `s_n s_{n+1} + s_{n+2}` and `s_n s_{n+1} s_{n+2}` on the four-stage register of `char_3` ([[castle-cryptography-round-two](pages/castle-cryptography-round-two.md)], Attack 5). The filter therefore has to be sized: a 64-stage register (`P(63, ·)`, castles of height 64) with a degree-16 filter has linear complexity up to `C(79, 16) ≈ 2^{54.3}`. Round two's Fix 5 sizes the same register, with every term of degree at most 16 (`L ≈ 2^54.6`), against a Berlekamp-Massey of `O(L log² L)` operations: about `2^66` operations on `2^55.6` output terms ([[castle-cryptography-round-two](pages/castle-cryptography-round-two.md)]).

## Fix 3 - the remaining ceiling

With an irreducible `Q` and a filtered output, the discrete logarithm lives in `F_{p^d}` with `d = k + 1` small, and discrete logarithms in finite fields have a subexponential attack, index calculus, of cost `L_q[1/3]` in the field size `q = p^d`. The field must then be large, about 3072 bits for 128-bit security, the sizing that [[castle-cryptography-round-three](pages/castle-cryptography-round-three.md)] takes from the published literature; round two computes the field size at which `L_q[1/3]` reaches `2^{128}`.

## The series at a glance

| seminar | track | result | pages |
|---|---|---|---|
| 1 | build | Diffie-Hellman key exchange in `F_p[x]/(char_2)`, also run on windows of castle counts; the period, the order of `x` and its norm `2^k`; security not evaluated | [[castle-cryptography-ring](pages/castle-cryptography-ring.md)], [[finite-fields](pages/finite-fields.md)], [[kitamasa](pages/kitamasa.md)], [[mod-p-observatory](pages/mod-p-observatory.md)] |
| 2 | red team | two attacks: the CRT and Pohlig-Hellman split, worked at `p = 101`, and Berlekamp-Massey recovery of `Q` | [[tower-parity-sectors](pages/tower-parity-sectors.md)], [[chinese-remainder-theorem](pages/chinese-remainder-theorem.md)], [[idempotent-decomposition](pages/idempotent-decomposition.md)], [[berlekamp-massey](pages/berlekamp-massey.md)] |
| 3 | blue team | an irreducible `Q`, a nonlinear filter, and the index-calculus ceiling | [[castle-cryptography-number-theory](pages/castle-cryptography-number-theory.md)], [[char-k-eisenstein-at-two](pages/char-k-eisenstein-at-two.md)] |
| round 2 | build, red team, blue team | ElGamal and a Schnorr signature; a private key recovered; both fixes broken; key sizes; the four questions | [[castle-cryptography-round-two](pages/castle-cryptography-round-two.md)] |
| round 3 | build, red team, blue team | a prime-order torus subgroup on `char_5`; the subfield attack closed; Pollard rho and the extended tower number field sieve set the key size | [[castle-cryptography-round-three](pages/castle-cryptography-round-three.md)] |

## Reproduce

The key exchange `castle_dh` (the functions `mulmod` and `powmod`), round two's `castle_dlp` (Pohlig-Hellman with baby-step giant-step), `bm_modp` (Berlekamp-Massey over `F_p`) and `castle_schnorr` are on [[castle-snippets-cryptography](pages/castle-snippets-cryptography.md)], with their outputs: the two shared secrets agree, and Berlekamp-Massey returns `[1, −3, 4, −4]` from the terms of `P(2, ·)`.

## Related Concepts

- [[finite-fields](pages/finite-fields.md)] - the fields `F_{p^d}`, their cyclic unit groups, and the periods of the sequences mod `p`.
- [[kitamasa](pages/kitamasa.md)] - `x^n mod Q` by binary exponentiation, the forward map of the system.
- [[berlekamp-massey](pages/berlekamp-massey.md)] - the shortest linear recurrence of a sequence, and when the output is correct.
- [[mod-p-observatory](pages/mod-p-observatory.md)] - the periods of `P(k, ·) mod p` as orders of `x` in `R`, and how they depend on `p`.
- [[signed-tower-count](pages/signed-tower-count.md)] - `P(k, L)` and its characteristic polynomials `char_k`.
- [[generating-function-gallery](pages/generating-function-gallery.md)] - the rational functions `num_k/den_k` whose denominators give `char_k`.
- [[tower-parity-sectors](pages/tower-parity-sectors.md)] - the factorization of `char_k` for even `k`, which Attack 1 uses.
- [[chinese-remainder-theorem](pages/chinese-remainder-theorem.md)], [[idempotent-decomposition](pages/idempotent-decomposition.md)] - the CRT split of Attack 1 and the idempotents that invert it.
- [[castle-cryptography-ring](pages/castle-cryptography-ring.md)] - Seminar 1 in full, with every computation.
- [[castle-cryptography-number-theory](pages/castle-cryptography-number-theory.md)] - characteristic polynomials, irreducible polynomials and the discrete logarithm problem from the start.
- [[castle-cryptography-round-two](pages/castle-cryptography-round-two.md)] - the second round: ElGamal and a signature, a private key recovered, both fixes broken, key sizes.
- [[castle-cryptography-round-three](pages/castle-cryptography-round-three.md)] - the third round: a prime-order torus subgroup on `char_5`, attacked with Pollard rho and the extended tower number field sieve.
- [[castle-ring-invariant-factors](pages/castle-ring-invariant-factors.md)] - the unit group of `R` as a product of cyclic groups; Pohlig-Hellman runs on its primary decomposition, and at a prime where `char_k` has a repeated factor `R` gains a `p`-group beside the field factor.
- [[castle-sign](pages/castle-sign.md)] - the sign `(−1)^{blocks}` summed in `P(k, L)`.
- [[castle-snippets-cryptography](pages/castle-snippets-cryptography.md)] - the programs of the series.
- [[hear-the-shape-seminar](pages/hear-the-shape-seminar.md)], [[one-bit-seminar](pages/one-bit-seminar.md)], [[hardin-identity-seminar](pages/hardin-identity-seminar.md)], [[oeis-mining-seminar](pages/oeis-mining-seminar.md)], [[sandcastle-seminar](pages/sandcastle-seminar.md)], [[castle-fibers-char-2-walkthrough](pages/castle-fibers-char-2-walkthrough.md)], [[tower-recursion-master-class](pages/tower-recursion-master-class.md)], [[pell-castle-strip](pages/pell-castle-strip.md)], [[song-as-castle](pages/song-as-castle.md)] - the other seminar pages.
- [[oeis-mining-pe502](pages/oeis-mining-pe502.md)] - the rows `P(k, ·)` and their characteristic polynomials `char_1` to `char_5`.

## Footnotes

[^1]: Verified by execution (Python 3.11, 2026-10-16) at `p = 101`: `A(2) = 33`, `A mod (x² − x + 2) = 98 + 8x`, `A·B mod char_2 = 86 + 55x + 51x²`, `B(2) = 6`, `(A·B)(2) = 97 = 33 · 6 mod 101`, both sides of the quadratic projection equal to `85 + 5x`; `e_1 = 51 + 25x + 76x²` is idempotent, `1` at `x = 2` and `0` mod `x² − x + 2`, and `x^L e_1 = 2^L e_1` for `L = 1, 5, 9`.
[^2]: Verified by execution (Python 3.11, 2026-10-16): `P(2, L) = 1, 1, 3, 9, 19, 33, 59, 121, 259, 529, 1035, 2025` for `L = 0, …, 11` from the `num`/`den` update; rational Berlekamp-Massey returns the order-3 recurrence with coefficient vector `[1, −3, 4, −4]` from the first 6 terms and from all 12; `char_2(x) = (x − 2)(x² − x + 2)` by SymPy `factor`.
[^3]: Verified by execution (Python 3.11 with SymPy, 2026-10-16): `char_k(x) = x^{k+1} den_k(1/x)` irreducible over the rationals for every odd `k ≤ 31`; `char_1` mod `p` irreducible for `p = 3, 7, 11, 10⁹ + 7` and split for `p = 5, 13, 101`; `char_3 ≡ (x + 21)(x + 24)(x − 26)(x − 23) mod 101` and irreducible mod `10⁹ + 7`; `C(79, 16) = 21566576904406820 ≈ 2^{54.26}`; 39 squarings and 12 multiplications for `a = 10^12`.
