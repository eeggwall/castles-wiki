---
title: Castle cryptography, round three - the castle torus
category: Analyses
summary: The third round of the build / red-team / blue-team series: round two's prescription, a system on char_5 (degree 6) with p chosen so that q = p^2 - p + 1 is prime, attacked with the published attacks on fields of size p^6. BUILD, at a toy size (p = 171271, q of 35 bits) and at a 128-bit size (512-bit p, 1024-bit q, field of about 3072 bits). char_5 is irreducible mod 94 of 600 primes near 10^6. The generator is the shift x raised to (p^6 - 1)/q, an element of the torus of order q used by XTR and CEILIDH. A public key is sent as its trace to F_{p^2}, 2 numbers mod p instead of 6, and the receiver finishes the exchange by a Kitamasa jump on the recurrence t_{n+3} = c t_{n+2} - c^p t_{n+1} + t_n of the traces. RED TEAM - the norms to both subfields of a torus element are 1, Pohlig-Hellman has nothing to split since q is prime, Pollard rho recovers the toy key in 199,332 steps against sqrt q = 171,270 and faces about 2^512 at full size, and index calculus sets the security level. The extended tower number field sieve (2016) applies because 6 is composite and lowers the cost constant from 1.923, round two's, to 1.747 (1.71 with several number fields), so on the heuristic formula a 128-bit system needs p of 531 to 559 bits, not 423, and a 512-bit p gives 2^126; a p of special form, such as a castle count, lowers the constant to 1.526 and the cost at 512 bits to 2^110. BLUE TEAM - the system is an instance of XTR, which the literature rates no longer competitive with elliptic curves.
tags: [analysis, seminar, cryptography, cryptanalysis, red-team, blue-team, torus, xtr, ceilidh, trace, compression, kitamasa, pollard-rho, pohlig-hellman, index-calculus, number-field-sieve, extnfs, key-size, finite-field, cyclotomic, castle]
sources: [granger-vercauteren-2005-dlp-algebraic-tori]
created: 2026-09-24
updated: 2026-10-25
---

# Castle cryptography, round three - the castle torus

## What this round does

[[castle-cryptography](pages/castle-cryptography.md)] built a public-key system on the signed tower count and broke it. [[castle-cryptography-round-two](pages/castle-cryptography-round-two.md)] broke the fixes and ended with a prescription for the third build (Fix 4): use the degree-6 castle polynomial `char_5`, choose the prime `p` so that `p^2 - p + 1` has a large prime factor, and then attack the result with the real published attacks on fields of size `p^6`. This page does that, at a toy size small enough to break and at full size for 128-bit security (the attacker needs about `2^128` operations).[^exec]

The system works, the attacks that broke rounds one and two do not apply, and the security level is set by index calculus, whose best published constant is lower than the one round two used. The castle supplies the modulus `char_5` and a recurrence reading of the exponentiation, and changes the security in neither direction.

## Terms used on this page

- **`char_5`** - the characteristic polynomial `x^6 - 6x^5 + 18x^4 - 32x^3 + 48x^2 - 32x + 32` of the signed tower count `P(5, ·)`, over towers of height at most 5, the towers of castles of height 6 ([[castle-cryptography-number-theory](pages/castle-cryptography-number-theory.md)]). When it has no factors mod `p`, arithmetic on castle states mod `char_5` is arithmetic in the finite field with `p^6` elements, `F_{p^6}` ([[finite-fields](pages/finite-fields.md)]).
- **Discrete logarithm** - given `g` and `g^a`, find `a`. Diffie-Hellman key exchange is broken if this is easy.
- **Torus** - the subgroup of `F_{p^6}` of size `p^2 - p + 1`. Its elements are those whose norms to the subfields `F_{p^2}` and `F_{p^3}` are both 1. Cryptographers call it the torus `T_6`; the XTR and CEILIDH systems work in it.[^gv-torus]
- **Trace** - a way to squeeze an element `h` of `F_{p^6}` down to the subfield with `p^2` elements: `Tr(h) = h + h^{p^2} + h^{p^4}`. It needs 2 numbers mod `p` instead of 6.
- **Pollard rho, Pohlig-Hellman** - the generic discrete-log attacks: rho costs about the square root of the group size; Pohlig-Hellman breaks the problem into pieces along the prime factors of the group size, so it gains nothing when that size is prime.
- **Index calculus / number field sieve** - the attack family that uses the structure of finite fields specifically. Its cost is written `L_Q[1/3, c] = exp(c (ln Q)^{1/3} (ln ln Q)^{2/3})` for a field of size `Q`; the constant `c` is what research papers lower.

## Build, round three

### Choosing `p`

Three conditions: `p` prime, `char_5` irreducible mod `p`, and `q = p^2 - p + 1` prime, which needs `p ≡ 1 (mod 3)`, since for `p ≡ 2 (mod 3)` the number `p^2 - p + 1` is divisible by 3. The irreducibility condition holds for 94 of the 600 primes `nextprime(10^6 + 997i)`, `0 ≤ i < 600`, about one in six.

| size | `p` | `q = p^2 - p + 1` | field `F_{p^6}` |
|---|---|---|---|
| toy | `171271` (18 bits) | `29,333,584,171` (35 bits), prime | 105 bits |
| full | 512 bits | 1024 bits, prime | about 3072 bits |

The full size matches the published sizing for this kind of system at 128-bit security: compressed elements of 1024 bits, so a 512-bit `p` and a 3072-bit field.[^stam-table]

### The generator is the castle shift

In the castle ring `F_p[x]/(char_5)`, the element `x` is the one-step shift of the castle recurrence, and raising it to a power is a Kitamasa jump ([[kitamasa](pages/kitamasa.md)]). The generator is that shift, jumped into the torus:

```
g = x^((p^6 - 1)/q)  mod (char_5, p)          g != 1,  g^q = 1        (both sizes)
Alice: A = g^a       Bob: B = g^b             A^b == B^a              (both sizes)
```

### Compression, and the recurrence inside

XTR uses the fact that a torus element is determined by its trace up to its two conjugates, because its three conjugates `h, h^{p^2}, h^{p^4}` are the roots of

```
X^3 - c X^2 + c^p X - 1,        c = Tr(h)
```

so a public key can be sent as `Tr(g^a)`, 2 numbers mod `p` instead of 6.[^xtr] Checked exactly at both sizes: the three conjugates of `g^a` multiply to 1 and their pairwise products sum to `c^p`.

The castle reading is in what the receiver does with the compressed key. The traces `t_n = Tr(h^n)` are the power sums of those three roots, so they obey the 3-term linear recurrence

```
t_{n+3} = c t_{n+2} - c^p t_{n+1} + t_n,       t_0 = 3,  t_1 = c,  t_2 = c^2 - 2 c^p
```

with coefficients in the subfield `F_{p^2}`, a linear recurrence of order 3 like the castle recurrences. Bob computes `t_b = Tr(g^{ab})` from Alice's trace `c = Tr(g^a)` and Bob's own `b` alone by a Kitamasa jump: reduce `X^b` modulo the cubic, then combine the three remainder coefficients with `t_0, t_1, t_2`. Alice does the same from Bob's trace. Both agree with the trace of the full shared secret at both sizes. XTR's own exponentiation ladder is a faster special-purpose version of the same jump.[^xtr]

## Red team, round three

### The subfield reduction finds nothing

Round two's subfield attack carried the key into a smaller field inside the large one, where the discrete logarithm was easy. Here the smaller fields are `F_{p^2}` and `F_{p^3}`, and pushing down means raising to `p^4 + p^2 + 1` or to `p^3 + 1`. Both of those numbers are multiples of `p^2 - p + 1`, so every torus element lands on 1: checked at both sizes. This is the defining property of the torus. Norms to the subfields determine a discrete log only modulo the subfield orders, and what remains lives in the torus.[^gv-reduction]

### Generic attacks

`q` is prime, so Pohlig-Hellman, the step that recovered Alice's key in round two, has nothing to split. Pollard rho, with the walk partitioned into three classes by the first two coefficients of the element and Floyd's cycle detection, recovers the toy private key `a = 4696630792` after 199,332 steps of the slower walk, against `sqrt q = 171,270`.[^exec] At full size the same attack takes about `sqrt q ≈ 2^512` steps.

### Index calculus

Index calculus works on the field `F_{p^6}` directly, and its best version for fields like this one improved in 2016. The **extended tower number field sieve** of Kim and Barbulescu lowers the cost for fields `F_{p^n}` of medium-size `p` with composite `n`, "from `L_Q(1/3, (96/9)^{1/3})` to `L_Q(1/3, (48/9)^{1/3})`", or to 1.71 with several number fields, and "can be used when n=6 and n=12".[^kb] Kim and Jeong extend the same constants to every composite `n`, and show that when "p is of special form" the constant falls to `(32/9)^{1/3}`.[^kj]

Degree 6 is composite, so all of this applies to the castle torus. Heuristic costs, with the lower-order term dropped as in round two:

| constant `c` | where it comes from | cost at 512-bit `p` | `p` needed for `2^128` |
|---|---|---|---|
| 2.201 = `(96/9)^{1/3}` | medium-size `p`, before 2016[^kb] | `2^159` | 308 bits |
| 1.923 = `(64/9)^{1/3}` | general sieve, the constant round two used | `2^139` | 423 bits |
| 1.747 = `(48/9)^{1/3}` | extended tower sieve, one number field[^kb] | `2^126` | 531 bits |
| 1.71 | extended tower sieve, several number fields[^kb] | `2^123` | 559 bits |
| 1.526 = `(32/9)^{1/3}` | `p` of special form[^kj] | `2^110` | 734 bits |

Three readings:

- **Composite degree.** Degree 6 makes the torus and the 3-to-1 compression possible, and it also makes the tower sieve apply. On the heuristic formula a 128-bit castle torus needs `p` of 531 to 559 bits, not round two's 423, and the published 512-bit size gives `2^126`. The published sizes are rounded recommendations built on more careful cost models than this formula,[^stam-table] so 512 bits is the minimum, with no margin.
- **`p` must not be a castle number.** A `p` of special form, such as a castle count or a value of a castle polynomial, admits the special-form sieve, which lowers the cost at a 512-bit `p` from `2^126` to `2^110`. `p` must be random.
- **The small coefficients of `char_5` do not help the attacker.** Any two irreducible polynomials of degree 6 over `F_p` define isomorphic fields, and discrete logarithms carry across the isomorphism, so the sieve may choose its own polynomials; the special-form speedup depends on the form of `p`, not on the modulus.

### Attacks that do not apply

Granger and Vercauteren's index calculus works directly in the tori `T_2(F_{q^m})` and `T_6(F_{q^m})` ([[granger-vercauteren-2005-dlp-algebraic-tori](pages/granger-vercauteren-2005-dlp-algebraic-tori.md)]). It matters for tori over fields that are themselves extensions: `T_30(F_p)` embeds in `T_6(F_{p^5})`, and they call for the security of fields `F_{q^30}` to be "completely reassessed". Over prime fields they state that LUC, XTR and CEILIDH are not affected.[^gv] The castle torus is `T_6(F_p)`, their case `m = 1`, where their `T_6` algorithm is slower than Pollard rho in every row of their running-time table (fields up to 1000 bits).[^gv-table] Stam's later survey agrees: "for T6(q) having non-prime q seems to offer no discernible benefit over prime T6".[^stam-gv] So this attack does not apply.

## Blue team verdict

Round three sets every parameter the earlier rounds identified: a prime group order (no Pohlig-Hellman), the torus subgroup (no subfield reduction), `sqrt q ≈ 2^512` (Pollard rho out of reach), and a random 512-bit `p` (index calculus at about `2^126` on the heuristic formula). The result is XTR: the castle supplies an irreducible polynomial of degree 6 and a recurrence reading of the trace exponentiation, and nothing that makes the system harder or easier to break than XTR. And the literature's verdict on XTR is that after the move to 128-bit security and the improvements in finite-field discrete logs it is "no longer competitive with elliptic curves".[^stam-abs]

## Related Concepts

- [[castle-cryptography-round-two](pages/castle-cryptography-round-two.md)] - the second lap, whose Fix 4 and Fix 6 prescribe this build and whose `L_q[1/3]` table this page updates.
- [[castle-cryptography](pages/castle-cryptography.md)] - the first lap and the three-seminar structure.
- [[castle-cryptography-number-theory](pages/castle-cryptography-number-theory.md)] - `char_5`, and the irreducibility of the odd-`k` castle polynomials over the rationals (checked to `k = 31`, proved for `k = 2^m − 1`).
- [[castle-cryptography-ring](pages/castle-cryptography-ring.md)] - the ring `F_p[x]/(Q)` and the castle Diffie-Hellman baseline.
- [[kitamasa](pages/kitamasa.md)] - the jump behind both the torus generator and the compressed key exchange.
- [[finite-fields](pages/finite-fields.md)] - `F_{p^6}`, its subfields, and the cyclotomic factorization of `p^6 - 1`.
- [[larger-prime-periodicity](pages/larger-prime-periodicity.md)] - the factorizations and periods of `char_k` mod larger primes, including `10⁹ + 7`.
- [[castle-ring-invariant-factors](pages/castle-ring-invariant-factors.md)] - security set by the largest prime dividing the group order, here the prime `q` itself.
- [[sandpile-group](pages/sandpile-group.md)] - another finite abelian group attached to a castle, read off a Smith normal form.
- [[oeis-mining-pe502](pages/oeis-mining-pe502.md)] - the `P(k,·)` castle families whose characteristic polynomials, `char_5` among them, serve as the field moduli.

## Appearances in Sources

- [[granger-vercauteren-2005-dlp-algebraic-tori](pages/granger-vercauteren-2005-dlp-algebraic-tori.md)] - the torus definition, the subfield-norm reduction, and the index calculus on tori that leaves `T_6` over a prime field unaffected.

## Footnotes

[^exec]: Verified by execution (Python 3.11 with SymPy, 2026-10-16), with arithmetic in `F_p[x]/(char_5)` written directly. Irreducibility of `char_5` mod each of the 600 primes `nextprime(10^6 + 997i)` by SymPy: 94. Toy size: `p = 171271` is prime, `p ≡ 1 (mod 6)`, `char_5` is irreducible mod `p`, and `q = 29333584171` is prime. Full size, with a 512-bit `p ≡ 1 (mod 6)` from a seeded random search (`random.seed(2026)`) for which `char_5` is irreducible mod `p` (Rabin's test: `x^{p^6} = x` and `gcd(x^{p^k} − x, char_5) = 1` for `k = 2, 3`) and the 1024-bit `q` is prime. At both sizes: `g ≠ 1`, `g^q = 1`, both subfield norms of `g` equal 1, Diffie-Hellman agrees, the trace-only Kitamasa exchange equals the trace of the shared secret in both directions, and the conjugates of `g^a` multiply to 1 with pairwise products summing to `c^p`; at the toy size the traces `t_n` for `n ≤ 7` satisfy the recurrence. Pollard rho on the toy, starting from `A·g`, with steps `y ↦ yA`, `y ↦ y²`, `y ↦ yg` chosen by `(y_0 + y_1) mod 3` and Floyd's cycle detection, recovers `a = 4696630792` after 199,332 steps. Index-calculus costs from `L_Q[1/3, c]` with `Q = p^6` and the `o(1)` term dropped: at `log₂ Q = 3072`, `2^158.8`, `2^138.7`, `2^126.1`, `2^123.4`, `2^110.1` for the five constants, and `2^128` at `p` of 307.6, 422.9, 531.0, 559.0 and 733.7 bits.

[^xtr]: https://en.wikipedia.org/wiki/XTR (read 2026-09-24) - XTR "uses the trace over GF(p²) to represent elements of a subgroup of GF(p⁶)*", with minimal polynomial "F(c,X) = X³ − cX² + c^p X − 1", "a factor of 3 reduction in representation size", and the recurrences "c_{2n} = c_n² − 2c_n^p" and "c_{n+2} = c_{n+1}·c − c^p·c_n + c_{n−1}".

[^kb]: https://eprint.iacr.org/2015/1027 (Kim and Barbulescu, "Extended Tower Number Field Sieve: A New Complexity for the Medium Prime Case", CRYPTO 2016; abstract read 2026-09-24) - "from L_Q(1/3, (96/9)^{1/3}) to L_Q(1/3, (48/9)^{1/3})", "from L_Q(1/3,2.15) to L_Q(1/3,1.71) if multiple number fields are used", and exTNFS "can be used when n=6 and n=12".

[^kj]: https://eprint.iacr.org/2016/526 (Kim and Jeong, "Extended Tower Number Field Sieve with Application to Finite Fields of Arbitrary Composite Extension Degree"; abstract read 2026-09-24) - the `(48/9)^{1/3}` and 1.71 constants for "n ... an arbitrary composite", and `L_{p^n}(1/3, (32/9)^{1/3})` when "p is of special form".

[^stam-table]: https://eprint.iacr.org/2021/1659 (Stam, "XTR and Tori", chapter in *Computational Cryptography*, Cambridge University Press; PDF read 2026-09-24) p.15 Table 1 [synthesis] - compact representations in bits: the `T_6` row gives 1024 bits at 128-bit security under the 2020 NIST recommendation (5120 at 256-bit), i.e. `lg p = 512`; p.14 [synthesis] - the 2020 columns follow NIST SP 800-57 and match ECRYPT.

[^stam-gv]: https://eprint.iacr.org/2021/1659 (Stam) p.14 - "for T30 the Granger–Vercauteren attack ([GV05] ...) and later developments need to be taken into account", and "for T6(q) having non-prime q seems to offer no discernible benefit over prime T6 or T2"; p.17 reference [GV05]: Granger and Vercauteren, "On the discrete logarithm problem on algebraic tori", CRYPTO 2005, LNCS 3621, pp. 66-85.

[^gv-torus]: [[granger-vercauteren-2005-dlp-algebraic-tori](pages/granger-vercauteren-2005-dlp-algebraic-tori.md)] §2.2 p.69 L152-155, L164-166 - "Tn(Fq) = {α ∈ K | NK/kd(α) = 1 for all subfields k ⊆ kd ⊊ K}"; "#Tn(Fq) = Φn(q)"; §1 p.67 L59-62 - XTR and CEILIDH work "in a subgroup G ⊂ F×q6 with |G| | Φ6(q) = q² − q + 1".

[^gv-reduction]: [[granger-vercauteren-2005-dlp-algebraic-tori](pages/granger-vercauteren-2005-dlp-algebraic-tori.md)] §2.1 p.68 L133-140 - the subfield norms determine `s mod lcm{Φd(q)}d|n,d≠n`, and "the remaining modular information required to determine the full discrete logarithm comes from the order Φn(q) subgroup of K×", the torus `T_n(F_q)`.

[^gv]: [[granger-vercauteren-2005-dlp-algebraic-tori](pages/granger-vercauteren-2005-dlp-algebraic-tori.md)] §1 p.67 L78-81 - "We stress that when defined over prime fields Fp, the security of these cryptosystems is not affected by our algorithm. Over extension fields however, this is not always the case"; Remark 2 p.82 L784-792 - "the column for m = 5 provides an upper bound for the hardness of the DLP in T30(Fq), since this can be embedded in T6(Fq5)", "the security offered by the DLP in finite fields of the form Fq30 should be completely reassessed."

[^gv-table]: [[granger-vercauteren-2005-dlp-algebraic-tori](pages/granger-vercauteren-2005-dlp-algebraic-tori.md)] §5.4 p.82 Table 2 L766-779 [synthesis] - log₂ expected running times against Pollard rho in a subgroup of size `2^160`, for `F_{p^{6m}}` of 200 to 1000 bits; at `m = 1` the `T_6` algorithm takes 25, 42, 59, 75, 93, 109, 127, 144, 161 against Pollard rho's 18, 34, 52, 66, 66, 66, 66, 68, 69.

[^stam-abs]: https://eprint.iacr.org/2021/1659 (Stam) p.1 abstract - "Subsequent developments, such as the move to 128-bit security and improvements in finite field DLP" leave XTR and related schemes "no longer competitive with elliptic curves".
