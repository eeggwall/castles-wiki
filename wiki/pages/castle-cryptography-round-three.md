---
title: Castle cryptography, round three - the castle torus
category: Analyses
summary: The third lap of the build / red-team / blue-team loop, taking round two's own prescription - build on char_5 (degree 6) with p chosen so p^2 - p + 1 carries a large prime - and red-teaming it against the published attack literature for fields of size p^6. BUILD, executed at a toy size (p = 171271) and at full 128-bit size (512-bit p, 1024-bit prime q = p^2 - p + 1, 3072-bit field). char_5 is irreducible mod p for about 1 prime in 6 (94 of 600 near 10^6). The generator is the castle's own shift x raised to (p^6 - 1)/q, so the group is the prime-order "torus" subgroup XTR and CEILIDH use. Keys compress 3 to 1 by sending only the trace to the subfield with p^2 elements, and the receiver finishes the key exchange from that trace by a Kitamasa jump on the 3-term recurrence t_{n+3} = c t_{n+2} - c^p t_{n+1} + t_n, a castle-style recurrence inside the castle field. RED TEAM - the subfield collapse that broke round two finds nothing (a torus element pushed down to either smaller subfield is always 1), Pohlig-Hellman has nothing to split (q is prime), Pollard rho breaks the toy in 127,402 steps (sqrt q = 171,270) and faces about 2^512 at full size, and index calculus is the real ceiling. The 2016 extended tower number field sieve applies because 6 is composite, cutting the cost constant from 1.923 (round two's estimate) to 1.747 (or 1.71 with several number fields), so a 128-bit system needs p of about 530 to 560 bits on the heuristic formula rather than 424, and a 512-bit p sits just under 2^128 (2^126). A p of special form, such as a castle count, drops the constant to 1.526 and costs about 16 more bits. BLUE TEAM verdict - round three is XTR wearing a castle, secure at the right size and no better than XTR, which the literature rates no longer competitive with elliptic curves.
tags: [analysis, seminar, cryptography, cryptanalysis, red-team, blue-team, torus, xtr, ceilidh, trace, compression, kitamasa, pollard-rho, pohlig-hellman, index-calculus, number-field-sieve, extnfs, key-size, finite-field, cyclotomic, castle]
sources: [oeis-mining-pe502]
created: 2026-09-24
updated: 2026-09-24
---

# Castle cryptography, round three - the castle torus

## What this round does

[[castle-cryptography](pages/castle-cryptography.md)] built a public-key system out of a castle and broke it. [[castle-cryptography-round-two](pages/castle-cryptography-round-two.md)] broke the fixes and ended with a prescription for the third build: use the degree-6 castle polynomial `char_5`, choose the prime `p` so that `p^2 - p + 1` has a large prime factor, and then attack the result with the real published attacks on fields of size `p^6`. This page does exactly that, at a toy size small enough to break and at full size for 128-bit security (the attacker needs about `2^128` operations).[^exec]

The short answer: the system works, the attacks that broke rounds one and two find nothing, and the security is set by one attack family - index calculus - whose best published version has improved since the number round two used. The castle contributes the field and a nice recurrence, and nothing else, good or bad.

## Terms used on this page

- **`char_5`** - the characteristic polynomial of the castle recurrence for height-5 towers, `x^6 - 6x^5 + 18x^4 - 32x^3 + 48x^2 - 32x + 32` ([[castle-cryptography-number-theory](pages/castle-cryptography-number-theory.md)]). When it has no factors mod `p`, arithmetic on castle states mod `char_5` is arithmetic in the finite field with `p^6` elements, `F_{p^6}` ([[finite-fields](pages/finite-fields.md)]).
- **Discrete logarithm** - given `g` and `g^a`, find `a`. Key exchange (Diffie-Hellman) is safe exactly as long as this is hard.
- **Torus** - the subgroup of `F_{p^6}` of size `p^2 - p + 1`. Its elements are the ones that carry no information into any smaller field inside `F_{p^6}`. Cryptographers call it the torus `T_6`; the XTR and CEILIDH systems work in it.
- **Trace** - a way to squeeze an element `h` of `F_{p^6}` down to the subfield with `p^2` elements: `Tr(h) = h + h^{p^2} + h^{p^4}`. It needs 2 numbers mod `p` instead of 6.
- **Pollard rho, Pohlig-Hellman** - the generic discrete-log attacks: rho costs about the square root of the group size; Pohlig-Hellman breaks the problem into pieces along the prime factors of the group size, so it gains nothing when that size is prime.
- **Index calculus / number field sieve** - the attack family that uses the structure of finite fields specifically. Its cost is written `L_Q[1/3, c] = exp(c (ln Q)^{1/3} (ln ln Q)^{2/3})` for a field of size `Q`; the constant `c` is what research papers lower.

## Build, round three

### Choosing `p`

Three conditions: `p` prime, `char_5` irreducible mod `p`, and `q = p^2 - p + 1` itself prime (which needs `p ≡ 1 mod 3`, since otherwise 3 divides it). The irreducibility condition holds for about one prime in six: 94 of the 600 primes tested near `10^6`.

| size | `p` | `q = p^2 - p + 1` | field `F_{p^6}` | primes `p ≡ 1 mod 6` tried |
|---|---|---|---|---|
| toy | `171271` (18 bits) | `29,333,584,171` (35 bits), prime | 105 bits | 62 |
| full | 512 bits | 1024 bits, prime | 3072 bits | 1706 |

The full size matches the published sizing for this kind of system at 128-bit security: compressed elements of 1024 bits, so a 512-bit `p` and a 3072-bit field.[^stam-table]

### The generator is the castle shift

In the castle ring `F_p[x]/(char_5)`, the element `x` is the one-step shift of the castle recurrence, and raising it to a power is a Kitamasa jump ([[kitamasa](pages/kitamasa.md)]). The generator is that shift, jumped into the torus:

```
g = x^((p^6 - 1)/q)  mod (char_5, p)          g != 1,  g^q = 1        (both sizes)
Alice: A = g^a       Bob: B = g^b             A^b == B^a              (both sizes)
```

### Compression, and the recurrence inside

XTR's observation is that a torus element is pinned down (up to two harmless conjugates) by its trace, because its three conjugates `h, h^{p^2}, h^{p^4}` are the roots of

```
X^3 - c X^2 + c^p X - 1,        c = Tr(h)
```

so a public key can be sent as `Tr(g^a)`, 2 numbers mod `p` instead of 6.[^xtr] Checked exactly at both sizes: the three conjugates of `g^a` multiply to 1 and their pairwise products sum to `c^p`.

The castle reading comes from what the receiver does with the compressed key. The traces `t_n = Tr(h^n)` are the power sums of those three roots, so they obey the 3-term linear recurrence

```
t_{n+3} = c t_{n+2} - c^p t_{n+1} + t_n,       t_0 = 3,  t_1 = c,  t_2 = c^2 - 2 c^p
```

with coefficients in the subfield with `p^2` elements - a castle-style recurrence living inside the castle field. Bob computes `t_b = Tr(g^{ab})` from Alice's trace `c = Tr(g^a)` and his own `b` alone by a Kitamasa jump: reduce `X^b` modulo the cubic, then combine the three remainder coefficients with `t_0, t_1, t_2`. Alice does the same from Bob's trace. Both agree with the trace of the full shared secret at both sizes. XTR's own exponentiation ladder is a faster special-purpose version of the same jump.[^xtr]

## Red team, round three

### The subfield collapse finds nothing

Round two's sharpest attack pushed the key down into a smaller field inside the big one, where the discrete log was easy. Here the smaller fields are `F_{p^2}` and `F_{p^3}`, and pushing down means raising to `p^4 + p^2 + 1` or to `p^3 + 1`. Both of those numbers are multiples of `p^2 - p + 1`, so every torus element lands on 1: checked at both sizes. There is nothing to project. This is the reason the torus exists.

### Generic attacks: nothing to split, square root to pay

`q` is prime, so Pohlig-Hellman has nothing to split - the step that recovered Alice's key in round two in 0.07 s. Pollard rho on the toy recovered the private key `a = 4696630792` in 127,402 steps against `sqrt q = 171,270`, in 1.3 s. At full size the same attack faces `sqrt q ≈ 2^512` steps, far beyond 128-bit security.

### Index calculus: the real ceiling, and it moved

Index calculus works on the field `F_{p^6}` directly, and its best version for fields like this one improved in 2016. The **extended tower number field sieve** of Kim and Barbulescu lowers the cost for fields `F_{p^n}` of medium-size `p` with composite `n`, "from `L_Q(1/3, (96/9)^{1/3})` to `L_Q(1/3, (48/9)^{1/3})`", or to 1.71 with several number fields, and "can be used when n=6 and n=12".[^kb] Kim and Jeong extend the same constants to every composite `n`, and show that when "p is of special form" the constant falls to `(32/9)^{1/3}`.[^kj]

Degree 6 is composite, so all of this applies to the castle torus. Heuristic costs, with the lower-order term dropped as in round two:

| constant `c` | where it comes from | cost at 512-bit `p` | `p` needed for `2^128` |
|---|---|---|---|
| 2.201 = `(96/9)^{1/3}` | medium-size `p`, before 2016[^kb] | `2^159` | 308 bits |
| 1.923 = `(64/9)^{1/3}` | general sieve, the constant round two used | `2^139` | 423 bits |
| 1.747 = `(48/9)^{1/3}` | extended tower sieve, one number field[^kb] | `2^126` | 532 bits |
| 1.71 | extended tower sieve, several number fields[^kb] | `2^123` | 559 bits |
| 1.526 = `(32/9)^{1/3}` | `p` of special form[^kj] | `2^110` | 734 bits |

Three readings:

- **Composite degree cuts both ways.** Degree 6 is what makes the torus and the 3-to-1 compression possible, and it is also what lets the tower sieve in. On the heuristic formula a 128-bit castle torus needs `p` of about 530 to 560 bits, not round two's 424, and the published 512-bit size sits right at the edge (`2^126`). The published sizes are rounded recommendations built on more careful cost models than this formula,[^stam-table] so the fair reading is "512 bits is the minimum, with no margin", not "512 bits is broken".
- **Do not take `p` from castle numbers.** A `p` with special structure - a castle count, a value of a castle polynomial, anything with a short description - opens the special-form sieve and costs about 16 more bits at the same size. `p` must be random.
- **The castle's small coefficients do not help the attacker.** `char_5` has small integer coefficients, but the sieve chooses its own polynomials for the field; every description of `F_{p^6}` is the same field to it. Only the form of `p` matters.

### Attacks that do not apply

Granger and Vercauteren gave an index calculus attack on tori (CRYPTO 2005); per Stam's survey it matters for tori built over fields that are themselves extensions, such as `T_30`, and "for T6(q) having non-prime q seems to offer no discernible benefit over prime T6".[^stam-gv] The castle torus is built over the prime field `F_p`, so this attack does not apply. (Granger-Vercauteren is cited here through Stam; the paper itself was not read.)

## Blue team verdict

Round one fixed properties. Round two learned to move numbers. Round three moves every number it can: prime group order (Pohlig-Hellman gone), torus subgroup (subfield collapse gone), `sqrt q ≈ 2^512` (rho gone), and a 512-bit random `p` (index calculus at the edge of `2^128`). What is left is **XTR wearing a castle**: the castle supplies a convenient irreducible degree-6 polynomial and a recurrence reading of trace exponentiation, and nothing that makes the system harder or easier to break than XTR itself. And the literature's verdict on XTR is that after the move to 128-bit security and the improvements in finite-field discrete logs it is "no longer competitive with elliptic curves".[^stam-abs]

That is the end of the loop's arc: the castle cryptosystem, done correctly, becomes a known good system, and the remaining gap to modern practice is the gap between finite fields and elliptic curves, not anything about castles.

## Related Concepts

- [[castle-cryptography-round-two](pages/castle-cryptography-round-two.md)] - the second lap, whose Fix 4 and Fix 6 prescribe this build and whose `L_q[1/3]` table this page updates.
- [[castle-cryptography](pages/castle-cryptography.md)] - the first lap and the three-seminar structure.
- [[castle-cryptography-number-theory](pages/castle-cryptography-number-theory.md)] - `char_5` and why the odd-`k` castle polynomials are irreducible over the rationals.
- [[castle-cryptography-ring](pages/castle-cryptography-ring.md)] - the ring `F_p[x]/(Q)` and the castle Diffie-Hellman baseline.
- [[kitamasa](pages/kitamasa.md)] - the jump behind both the torus generator and the compressed key exchange.
- [[finite-fields](pages/finite-fields.md)] - `F_{p^6}`, its subfields, and the cyclotomic factorization of `p^6 - 1`.
- [[larger-prime-periodicity](pages/larger-prime-periodicity.md)] - how often `char_5` stays irreducible mod `p`.
- [[castle-ring-invariant-factors](pages/castle-ring-invariant-factors.md)] - security as the largest prime-power invariant factor, here a single prime `q`.

## Appearances in Sources

- [[oeis-mining-pe502](pages/oeis-mining-pe502.md)] - the `P(k,·)` castle families whose characteristic polynomials, `char_5` among them, serve as the field moduli.

## Footnotes

[^exec]: Verified by execution (2026-09-24): Python 3 with `gmpy2` primality tests; field arithmetic in `F_p[x]/(char_5)` written directly. Irreducibility of `char_5` mod `p` by Rabin's test (`x^{p^6} = x` and `gcd(x^{p^k} - x, char_5) = 1` for `k = 2, 3`), on 600 primes from `nextprime(10^6 + 997 i)`. Primes `p ≡ 1 mod 6` searched from a seeded random generator until `char_5` was irreducible and `p^2 - p + 1` prime. At both sizes: `g ≠ 1`, `g^q = 1`, both subfield norms equal 1, Diffie-Hellman agreed, the trace-only Kitamasa exchange matched the trace of the shared secret in both directions, and the cubic identity held for `g^a`. Pollard rho with a 3-way partition walk and Floyd cycle detection on the toy. Index-calculus costs from `L_Q[1/3, c]` with `Q = p^6` and the `o(1)` term dropped. All quoted numbers are the program's printed output.

[^xtr]: https://en.wikipedia.org/wiki/XTR (read 2026-09-24) - XTR "uses the trace over GF(p²) to represent elements of a subgroup of GF(p⁶)*", with minimal polynomial "F(c,X) = X³ − cX² + c^p X − 1", "a factor of 3 reduction in representation size", and the recurrences "c_{2n} = c_n² − 2c_n^p" and "c_{n+2} = c_{n+1}·c − c^p·c_n + c_{n−1}".

[^kb]: https://eprint.iacr.org/2015/1027 (Kim and Barbulescu, "Extended Tower Number Field Sieve: A New Complexity for the Medium Prime Case", CRYPTO 2016; abstract read 2026-09-24) - "from L_Q(1/3, (96/9)^{1/3}) to L_Q(1/3, (48/9)^{1/3})", "from L_Q(1/3,2.15) to L_Q(1/3,1.71) if multiple number fields are used", and exTNFS "can be used when n=6 and n=12".

[^kj]: https://eprint.iacr.org/2016/526 (Kim and Jeong, "Extended Tower Number Field Sieve with Application to Finite Fields of Arbitrary Composite Extension Degree"; abstract read 2026-09-24) - the `(48/9)^{1/3}` and 1.71 constants for "n ... an arbitrary composite", and `L_{p^n}(1/3, (32/9)^{1/3})` when "p is of special form".

[^stam-table]: https://eprint.iacr.org/2021/1659 (Stam, "XTR and Tori", chapter in *Computational Cryptography*, Cambridge University Press; PDF read 2026-09-24) p.15 Table 1 [synthesis] - compact representations in bits: the `T_6` row gives 1024 bits at 128-bit security under the 2020 NIST recommendation (5120 at 256-bit), i.e. `lg p = 512`; p.14 [synthesis] - the 2020 columns follow NIST SP 800-57 and match ECRYPT.

[^stam-gv]: https://eprint.iacr.org/2021/1659 (Stam) p.14 - "for T30 the Granger–Vercauteren attack ([GV05] ...) and later developments need to be taken into account", and "for T6(q) having non-prime q seems to offer no discernible benefit over prime T6 or T2"; p.17 reference [GV05]: Granger and Vercauteren, "On the discrete logarithm problem on algebraic tori", CRYPTO 2005, LNCS 3621, pp. 66-85 (cited via Stam, not read).

[^stam-abs]: https://eprint.iacr.org/2021/1659 (Stam) p.1 abstract - "Subsequent developments, such as the move to 128-bit security and improvements in finite field DLP" leave XTR and related schemes "no longer competitive with elliptic curves".
