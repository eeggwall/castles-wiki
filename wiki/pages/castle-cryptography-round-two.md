---
title: Castle cryptography, round two - break the fixes, size the keys
category: Analyses
summary: The second lap of the build / red-team / blue-team loop on the castle cryptosystem, every claim executed. BUILD - a toy ElGamal and a Schnorr-style signature on the x^a map (and the lesson that on char_1 the prime-order subgroup collapses into the scalars, x^8 = 16, because (1+i)^8 = 16, so the degree-4 castle char_3 with a torus prime q | p^2+1 is used instead). RED TEAM - three results. (1) Pohlig-Hellman actually recovers Alice's private key 373309869 from the published castle_dh public key in 0.07 s. (2) The round-one blue-team fix "use an irreducible odd-k Q" does not survive - the group order p^d − 1 factors algebraically into cyclotomic values ∏ Φ_e(p), so the largest prime factor is at most about p^φ(d), and the private key falls in 0.04 s (char_1, F_{p^2}) and 0.18 s (char_3, F_{p^4}). (3) The fix "nonlinear output defeats Berlekamp-Massey" does not survive either - a degree-e polynomial filter on a d-stage castle register has linear complexity at most C(d+e−1, e) (products of eigenvalues), Berlekamp-Massey over F_p recovers it from 2L terms, and the bound is tight at d = 4, 6 (10 / 14 / 20 / 21 / 27 / 56). BLUE TEAM - the fixes must move a number, not a name - p must be sized so Φ_d(p) carries a 256-bit prime (p ≳ 2^128 at d = 4 or 6, the XTR / torus design), the filter must push linear complexity past ~2^40 (a 64-stage register with a degree-16 filter, i.e. a castle of height 63), and the index-calculus L[1/3] ceiling puts 128-bit security near q = p^d ~ 2^2500. Closes with the four-question red-team method for judging any novel cryptosystem.
tags: [analysis, seminar, cryptography, cryptanalysis, red-team, blue-team, pohlig-hellman, baby-step-giant-step, berlekamp-massey, linear-complexity, elgamal, schnorr, signature, finite-field, cyclotomic, index-calculus, key-size, castle]
sources: [oeis-mining-pe502]
created: 2026-09-18
updated: 2026-09-18
---

# Castle cryptography, round two

[[castle-cryptography](pages/castle-cryptography.md)] ran the loop once (Seminar 1 expanded as [[castle-cryptography-ring](pages/castle-cryptography-ring.md)]): **build** a castle Diffie–Hellman, **red-team** it (the modulus factors; the output is linear), **blue-team** it (irreducible odd-`k` char poly; nonlinear output). This page runs the loop a second time, and the second lap is where the discipline actually lives: the round-one fixes are themselves attacked, both fall, and the blue team learns that a fix has to move a *number*, not rename a *property*. Everything below was executed; the programs are pinned on [[castle-snippets](pages/castle-snippets.md)] (`castle_dlp`, `bm_modp`, `castle_schnorr`).

Notation as before: `p = 10⁹ + 7`, the ring is `R = F_p[x]/(Q)` with `Q = char_k mod p`, the generator is `x`, and `char_1 = x² − 2x + 2`, `char_2 = x³ − 3x² + 4x − 4`, `char_3 = x⁴ − 4x³ + 8x² − 8x + 8` ([[signed-tower-count](pages/signed-tower-count.md)]).

---

# Build, round two — ElGamal and a signature on the `x^a` map

Round one stopped at the shared secret. The natural next deliverables hang off the same `x^a` map:

- **ElGamal.** Public key `A = g^a`. Encrypt a ring element `m` as `(g^k, m · A^k)`; decrypt by computing `(g^k)^a` and dividing. Division in the ring is `s^{-1} = s^{q−1}` inside a subgroup of prime order `q`.
- **Schnorr-style signature.** Choose `k`, publish `e = H(g^k, msg)` and `s = k + a·e mod q`; verify by recomputing `g^s · A^{−e}` and hashing it. The *same* exponentiation, used three ways.

Both need a **prime-order subgroup** `⟨g⟩`, `|⟨g⟩| = q`. That is where the castle taught its first round-two lesson.

**First attempt, on `char_1` (degree 2).** `p ≡ 3 (mod 4)`, so `char_1` is irreducible mod `p` and `R = F_{p²}`. The order of `x` is `8 · 500000003`, so the natural choice is `q = 500000003` and `g = x^8`. But `x^8 = 16` — **a scalar.** The roots of `char_1` are `1 ± i` and `(1+i)^8 = 16`, so the whole prime-order subgroup lives in `F_p ⊂ F_{p²}`: the ElGamal public key came out as `[142542049, 0]`, and the "castle" ring contributed nothing.[^1] The eigenvalue structure that makes `char_1` pretty ([[eigenvalue-continued-fractions](pages/eigenvalue-continued-fractions.md)]) is exactly what collapses it.

**Second attempt, on `char_3` (degree 4).** `p⁴ − 1 = (p−1)(p+1)(p²+1)`, and `p² + 1` contributes two primes, `58699937` and `340715873`, that live in the genuine degree-4 part of `F_{p⁴}^*` (no proper subfield has order divisible by them). With `q = 340715873` and `g = r^{(p⁴−1)/q}` for a random `r`, the generator is a full-width ring element, ElGamal round-trips the message `[1, 1, 3, 9]` (the first four `P(2,·)` terms, for fun), and the signature verifies on the signed message and fails on a tampered one.[^1] That is the Seminar 1 deliverable: **key exchange, encryption, and signatures, all from one `powmod`.**

---

# Red team, round two — the fixes fall

## Attack 3 — recover Alice's private key, for real

Round one *described* the CRT split; round two *runs* it. Take the published `castle_dh` numbers: `Q = char_2`, Alice's public key `A = x^a = [704821174, 848698009, 235195321]`. Factor `Q mod p = (x − 2)(x² − x + 2)`, reduce `A` modulo each factor, solve a discrete log in each piece, and recombine by CRT:

| piece | where it lives | order of `x` there | log |
|---|---|---|---|
| `x − 2` | `F_p^*`, `x ↦ 2` | `500000003` (prime, `= (p−1)/2`) | `373309869` |
| `x² − x + 2` | `F_{p²}^*` | `2³·3²·7·109²·167·500000003` | `373309869` |

Each piece is solved by **Pohlig–Hellman** over the factorization of the element order, with **baby-step giant-step** on each prime-power factor: the largest prime is `500000003 ≈ 2²⁹`, so the biggest BSGS table has about `2¹⁵` entries. **Alice's private key `a = 373309869` comes back in 0.07 s**, from `p`, `Q`, and `A` alone.[^2] The room should watch this happen: the secret exponent that took forty squarings to *use* takes a fraction of a second to *steal*.

## Attack 4 — the "irreducible `Q`" fix does not survive

Round one's Fix 1 said: use an odd-`k` char poly, which is irreducible, so the ring is one field `F_{p^d}` and "the attacker faces the whole discrete log." True as far as it goes, and **not enough**, because the *group order* factors even when the *modulus* does not:

```
p^d − 1  =  ∏_{e | d} Φ_e(p)          (Φ_e = the e-th cyclotomic polynomial)
p² − 1   =  (p − 1)(p + 1)
p⁴ − 1   =  (p − 1)(p + 1)(p² + 1)
```

This is an *algebraic* factorization: it holds for every `p`, and it hands Pohlig–Hellman a head start regardless of how `Q` was chosen. The largest prime factor of `p^d − 1` is at most about `Φ_d(p) ≈ p^{φ(d)}`, and at `p = 10⁹+7` the cyclotomic values are small enough to factor and small enough to BSGS:

| `Q` | irreducible mod `p`? | `ord(x)` | largest prime | private key recovered |
|---|---|---|---|---|
| `char_1` (deg 2) | yes | `2³ · 500000003` | `500000003 ≈ 2²⁹` | **0.04 s** |
| `char_3` (deg 4) | yes | `2⁴ · 5 · 58699937 · 340715873 · 500000003` | `500000003 ≈ 2²⁹` | **0.18 s** |
| Schnorr subgroup on `char_3` | yes | `q = 340715873 ≈ 2²⁹` | itself | **0.07 s** (plain BSGS) |

Same private key `373309869`, same attacker, three "hardened" moduli.[^3] The fix removed the CRT split of the *ring* and left the CRT split of the *group* untouched. **Irreducible was a property; the attacker needed a number.**

## Attack 5 — the "nonlinear output" fix does not survive either

Round one's Fix 2 said: filter the linear castle stream through a nonlinear function so Berlekamp–Massey no longer sees a short recurrence. The red team's response is **linearization**. If `s_n = Σ c_i λ_iⁿ` is a `d`-stage linear recurrence (the `λ_i` are the roots of `Q`), then a product of `e` shifted terms is a linear combination of `(λ_{i₁} ⋯ λ_{i_e})ⁿ` — it is *again* a linear recurrence, whose characteristic roots are the degree-`e` monomials in the `λ_i`. A polynomial filter of degree `e` therefore has **linear complexity at most `Σ_{j≤e} C(d+j−1, j)`** (homogeneous degree `e`: `C(d+e−1, e)`), and Berlekamp–Massey over `F_p` recovers it from `2L` terms as usual. Executed on the castle registers `P(k,·) mod p` (`d = k+1`):[^4]

| filter | `d = 3` (`char_2`) | `d = 4` (`char_3`) | `d = 6` (`char_5`) | bound |
|---|---|---|---|---|
| `s_n · s_{n+1}` | 6 | 10 | 21 | `C(d+1, 2)` |
| `s_n²` | 6 | 10 | 21 | `C(d+1, 2)` |
| `s_n · s_{n+1} + s_{n+2}` | 8 | 14 | 27 | `C(d+1, 2) + d` |
| `s_n · s_{n+1} · s_{n+2}` | 9 | 20 | 56 | `C(d+2, 3)` |

Tight at `d = 4` and `d = 6`; at `d = 3` the two deficits come from coincidences among products of `char_2`'s roots (its quadratic factor `x² − x + 2` has constant term `2`, so the product of its two roots *is* the third root `2`, and monomials collide — structure lowering complexity yet again). In every case the recovered recurrence predicts every later term and `2L` terms suffice. As a check on the mechanism, the exact characteristic polynomial of `s_n s_{n+1}` for `char_2` is `∏_{i≤j}(x − λ_iλ_j) = x⁶ − 5x⁵ + 8x⁴ − 12x³ − 16x² − 64x + 256`, and Berlekamp–Massey mod `p` returned precisely those coefficients.[^4]

So "nonlinear defeats Berlekamp–Massey" is false as stated. What nonlinearity buys is a **quantifiable increase in linear complexity**, from `d` to roughly `C(d+e−1, e)`, and a small register with a low-degree filter stays wide open.

---

# Blue team, round two — move the number

Every round-one fix named a property (irreducible, nonlinear). Every round-two attack ignored the name and measured a number. The blue team's second lap is to make the numbers large.

## Fix 4 — size `p` so `Φ_d(p)` carries a big prime

Generic discrete-log attacks (BSGS, Pollard rho) cost about the square root of the **largest prime factor of the group order**, so `2¹²⁸` security needs a `256`-bit prime dividing `p^d − 1`, and it must sit in `Φ_d(p) ≈ p^{φ(d)}` (any smaller cyclotomic factor lives in a proper subfield, and the norm map projects the problem down into it — the `x^8 = 16` collapse was this in miniature). So:

| `d` | `φ(d)` | `p` needed for a 256-bit prime in `Φ_d(p)` to *exist* |
|---|---|---|
| 2 | 1 | `p ≳ 2²⁵⁶` |
| 4 | 2 | `p ≳ 2¹²⁸` |
| 6 | 2 | `p ≳ 2¹²⁸` |
| 7 | 6 | `p ≳ 2⁴³` |

and then `p` must actually be *chosen* so that `Φ_d(p)` has such a factor — not hoped for. This is precisely the design of **XTR** and **torus-based cryptography**, which work in the order-`Φ_6(p)` subgroup of `F_{p⁶}^*`. The castle already has a degree-6 modulus, `char_5`, so the natural round-three build is a castle torus system.

## Fix 5 — size the register and the filter

Berlekamp–Massey needs `2L` terms and roughly `L²` work, so linear complexity around `2⁴⁰` is the practical wall. The `C(d+e−1, e)` bound tells the blue team what it takes:[^5]

| register stages `d` | filter degree `e` | linear complexity `≤` |
|---|---|---|
| 6 | 6 | `923 ≈ 2¹⁰` |
| 32 | 8 | `≈ 2²⁶` |
| 64 | 16 | `≈ 2⁵⁵` |
| 128 | 16 | `≈ 2⁶⁹` |

A castle register of `d` stages is `char_{d−1}`, so a `64`-stage register is the char poly of a **castle of height 63** — `P(63, L)` — with a degree-16 filter on top. That is a design, with a number attached, rather than a slogan. (The other classical escape, irregular clocking as in the shrinking generator, is the still-open variant below.)

## Fix 6 — the index-calculus ceiling, quantified

Even with Fixes 4 and 5 in place, `F_{p^d}` for small `d` has the subexponential index-calculus / number-field-sieve family of attacks. The standard heuristic cost is `L_q[1/3, (64/9)^{1/3}] = exp((64/9)^{1/3} (ln q)^{1/3} (ln ln q)^{2/3})` with `q = p^d`. At `p = 10⁹ + 7`:[^5]

| `d` | `q = p^d` | generic (rho on largest prime) | `L_q[1/3]` |
|---|---|---|---|
| 2 | `≈ 2⁶⁰` | `2¹⁴` | `≈ 2²³` |
| 4 | `≈ 2¹²⁰` | `2¹⁴` | `≈ 2³³` |
| 6 | `≈ 2¹⁸⁰` | `2²⁴` | `≈ 2⁴⁰` |
| 7 | `≈ 2²¹⁰` | `2³⁴` | `≈ 2⁴³` |

and the field size at which `L_q[1/3]` reaches `2¹²⁸` is about `q ≈ 2²⁵⁰⁰` — `p ≈ 2¹²⁷²` at `d = 2`, `2⁶³⁶` at `d = 4`, `2⁴²⁴` at `d = 6` (the same ballpark as the 3072-bit finite-field recommendation for 128-bit security). This is the honest ceiling of round one, now with a number: the castle DLP is not made safe by any *structural* choice; it is made safe, if at all, by a `p` hundreds of bits wide, at which point it is ordinary finite-field cryptography wearing a castle.

---

# The method (what Seminar 2 is really teaching)

The two laps generalize into a repeatable procedure for judging **any** novel cryptosystem, which is the transferable skill of the red-team track:

1. **Name the hard problem exactly.** Which group, which order, which map. "Discrete log in `F_p[x]/(Q)`" is not an answer until `|⟨g⟩|` is written down.
2. **Ask where the structure leaks.** Does the modulus factor (CRT on the ring)? Does the group order factor (Pohlig–Hellman on the group — it *always* does algebraically for `p^d − 1`)? Does a subgroup collapse into a subfield (norm map; `x^8 = 16`)?
3. **Ask whether the output is linear, or a low-degree function of something linear.** Berlekamp–Massey for the first; linearization with the `C(d+e−1, e)` bound for the second.
4. **Ask what the key size buys against each attack separately.** Square root of the largest prime factor; the linear complexity; `L_q[1/3]`. A fix that does not move one of these numbers has not fixed anything.

A builder who never runs step 4 declares victory after Fix 1. A breaker who never rebuilds never learns that Fix 4 is a real design (XTR). The loop is the lesson.

## Still open

- **Round three build:** a castle torus system — `char_5` (degree 6) with `p` chosen so `Φ_6(p) = p² − p + 1` has a large prime factor; then red-team it with the actual index-calculus literature for `F_{p⁶}`.
- **Irregular clocking:** a shrinking-generator castle (one castle register clocks another) as the nonlinear variant that linearization does *not* cover; measure its linear complexity empirically.
- **The `d = 3` deficits:** prove which monomial coincidences among `char_2`'s roots account for `8` vs `9` and `9` vs `10`.

## Appearances in Sources

- [[oeis-mining-pe502](pages/oeis-mining-pe502.md)] - the `P(k,·)` families whose characteristic polynomials serve as the moduli and registers.

## Related Concepts

- [[castle-cryptography](pages/castle-cryptography.md)] - round one of the loop: the build, the two original attacks, and the fixes this page breaks.
- [[castle-cryptography-ring](pages/castle-cryptography-ring.md)] - the ring seminar; the algebra baseline whose §5 element-order table is the input Attack 3 factors.
- [[castle-cryptography-number-theory](pages/castle-cryptography-number-theory.md)] - char poly, irreducible, and DLP from scratch; this page supplies the caveat that irreducible `Q` still leaves `p^d − 1` factored.
- [[kitamasa](pages/kitamasa.md)] - the `x^a mod Q` exponentiation used by ElGamal, the signature, and every attack's inner loop.
- [[berlekamp-massey](pages/berlekamp-massey.md)] - the recurrence-recovery algorithm, here run over `F_p` against nonlinear filters.
- [[finite-fields](pages/finite-fields.md)] - `F_{p^d}^*` is cyclic of order `p^d − 1`; the cyclotomic factorization and the subfield tower are what Attack 4 exploits.
- [[mod-p-observatory](pages/mod-p-observatory.md)] - element orders as lcm of eigenvalue orders; the same orders Pohlig–Hellman factors.
- [[tower-parity-sectors](pages/tower-parity-sectors.md)] - why `char_2` factors, and the root coincidence `λλ̄ = 2` behind the `d = 3` complexity deficits.
- [[eigenvalue-continued-fractions](pages/eigenvalue-continued-fractions.md)] - the roots `1 ± i` of `char_1` whose eighth power is the scalar `16`.
- [[castle-snippets](pages/castle-snippets.md)] - `castle_dlp`, `bm_modp`, `castle_schnorr`, all pinned with executed output.

## Footnotes

[^1]: Verified by execution (2026-09-18). On `Q = char_1 mod p`, `p = 10⁹+7`: `ord(x) = 4000000024 = 2³ · 500000003`; `g = x^8 = [16, 0]`, a scalar, since `(1+i)^8 = 16`; the ElGamal public key was `[142542049, 0]` (scalar), decryption round-tripped and the Schnorr signature verified, but entirely inside `F_p`. On `Q = char_3 mod p` with `q = 340715873 | p² + 1` and `g = r^{(p⁴−1)/q} = [670690837, 335848460, 27104856, 290696543]` (`r` seeded random): public key `[34518600, 853770003, 669598040, 563247297]`; `dec(a, enc(pub, [1,1,3,9])) = [1,1,3,9]`; signature `(e, s) = (129461214, 65798226)` verifies on `b"castle 502"` and fails on `b"castle 503"`. Hash `H = SHA-256(repr(R, msg)) mod q`.

[^2]: Verified by execution (2026-09-18): `castle_dlp(A, Q2, p)` with `A = x^{373309869} mod char_2 = [704821174, 848698009, 235195321]` returns `[373309869, 500000007000000024]` (the key, and the modulus it is determined modulo) in 0.07 s. The pieces: `x − 2` gives the DLP of `2^a` in `F_p^*`, `ord(2) = 500000003`; `x² − x + 2` gives the DLP of `x^a` in `F_p[x]/(x²−x+2) ≅ F_{p²}`, `ord(x) = 500000007000000024 = 2³·3²·7·109²·167·500000003`. Both logs equal `373309869`; CRT combines them.

[^3]: Verified by execution (2026-09-18): `sp.factorint(p² − 1) = {2: 4, 3: 2, 7: 1, 109: 2, 167: 1, 500000003: 1}`; `char_1` and `char_3` are irreducible mod `p` (SymPy, `modulus=p`); `castle_dlp` recovers `373309869` from `x^{373309869} mod char_1` in 0.04 s (`ord(x) = 4000000024`) and from `x^{373309869} mod char_3` in 0.18 s (`ord(x) = 800000016000000107200000240 = 2⁴·5·58699937·340715873·500000003`, `p⁴ − 1 = 2⁵·3²·5²·7·109²·167·58699937·340715873·500000003`). Plain BSGS recovers the Schnorr private key from the order-`340715873` subgroup in 0.07 s.

[^4]: Verified by execution (2026-09-18): `bm_modp` (Berlekamp–Massey over `F_p`) on `P(k,·) mod p` returns linear complexity `d = k+1` for `k = 2, 3, 5`, and on the four filters the complexities tabulated (300 terms each); for every filter the recovered connection polynomial annihilates all later terms and `bm_modp(z[:2L])` returns the same `(C, L)`. Exact product polynomial for `char_2`: SymPy roots, `∏_{i≤j}(x − λ_iλ_j) = x⁶ − 5x⁵ + 8x⁴ − 12x³ − 16x² − 64x + 256`; `bm_modp` on `s_n s_{n+1}` returned `[256, −64, −16, −12, 8, −5, 1]` (signed representatives, high→low), the same polynomial.

[^5]: Computed 2026-09-18. Linear-complexity bounds `Σ_{j=1}^{e} C(d+j−1, j)`: `(6,6) → 923`, `(32,8) → 76904684 ≈ 2²⁶`, `(64,16) ≈ 2⁵⁵`, `(128,16) ≈ 2⁶⁹`. `L_q[1/3]` with constant `(64/9)^{1/3}` at `q = p^d`, `p = 10⁹+7`: `d = 2, 3, 4, 6, 7 → 2²³, 2²⁸, 2³³, 2⁴⁰, 2⁴³`; largest prime factor of `p^d − 1` (SymPy `factorint`) `≈ 2²⁹, 2⁴⁸, 2²⁹, 2⁴⁸, 2⁶⁹` respectively. `L_q[1/3] = 2⁸⁰` near `q ≈ 2⁸⁶⁴`; `= 2¹²⁸` near `q ≈ 2²⁵⁴⁴`. These are the textbook heuristic exponents, not a tuned NFS estimate; the honest reading is the order of magnitude.
