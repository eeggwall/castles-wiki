---
title: Castle cryptography - a build / red-team / blue-team seminar series
category: Analyses
summary: A three-seminar series that treats a castle-based public-key system the way real security work is organized — separate build, attack, and remediate tracks. Seminar 1 (BUILD) implements a working public-key system whose keypair is a "castle" instead of an SSH keypair, deferring the security question entirely to focus on the implementation: the public castle is a characteristic polynomial Q = char_k mod p over F_p, a private key is a secret exponent, and key exchange is Kitamasa exponentiation x^a mod Q (the castle solve's own fast-index trick) — a running castle Diffie-Hellman in ~20 lines. Seminar 2 (RED TEAM) is applied cryptanalysis of this novel system: the char polys factor so the discrete log splits (Pohlig-Hellman), and Berlekamp-Massey reconstructs the secret castle from the count stream (the LFSR attack). Seminar 3 (BLUE TEAM) is remediation: given the breaks, how do you improve the system — irreducible (prime) char polys to stop the factorization split, nonlinear feedback to defeat Berlekamp-Massey, and an honest account of what still doesn't reach real security. Wanders finite fields, binary exponentiation, primes, and integer sequences throughout, always via short programs. Every primitive already exists: finite-fields, kitamasa, berlekamp-massey, mod-p-observatory, signed-tower-count. Round two of the loop (castle-cryptography-round-two) builds ElGamal and a signature, recovers Alice's actual private key in 0.07 s, breaks both round-one fixes (the group order p^d − 1 factors algebraically; nonlinear filters linearize to complexity C(d+e−1, e)), and sizes the keys.
tags: [analysis, seminar, cryptography, public-key, finite-field, kitamasa, berlekamp-massey, discrete-log, diffie-hellman, cryptanalysis, red-team, blue-team, pedagogy, implementation, castle]
sources: [oeis-mining-pe502]
created: 2026-09-18
updated: 2026-09-18
---

# Castle cryptography

## The series

Three seminars, structured the way real security work actually splits — **build**, **attack**, **remediate** — so each session has one job and the audience isn't asked to design and break a system in the same breath:

1. **Seminar 1 — BUILD.** *Implement* a public-key system whose keypair is a castle: a **private castle** and a **public castle** in place of an SSH `id_rsa` / `id_rsa.pub`, and two strangers deriving a shared secret from each other's public castles. **This session explicitly sets the security question aside** — "this might well be insecure; we are not evaluating that today, we are building the thing and making it run." Pure implementation focus: short programs, worked examples, a system you can execute in a REPL.
2. **Seminar 2 — RED TEAM.** *Attack* it. Applied cryptanalysis of a novel, unproven system — exactly the skill of evaluating something nobody has vetted. Two concrete breaks, each a one-liner, each a famous attack in miniature.
3. **Seminar 3 — BLUE TEAM.** *Improve* it. Given the breaks, how do you harden the system — and, just as important, how do you tell when you've merely patched a symptom versus reached genuine hardness?

The through-line is a wandering tour of **finite fields, binary exponentiation, primes, and integer sequences**, all via the castle. Every primitive the series needs is already on the wiki — "we already built the machine; now point it at cryptography."

**Track separation is the pedagogy.** Building without red-teaming teaches you to make crypto *work*; red-teaming without having built teaches you to attack in the abstract. Doing them as separate, sequenced tracks — build it and trust it, then break that trust, then earn it back — is how practitioners actually learn the discipline, and it keeps Seminar 1 honestly free of the "but is it secure?" anxiety that would otherwise swamp the implementation.

**The loop runs twice.** This page is the first lap. [[castle-cryptography-round-two](pages/castle-cryptography-round-two.md)] is the second: the build adds ElGamal and a signature, the red team recovers Alice's real private key and then breaks *both* of this page's fixes, and the blue team learns to move a number (largest prime factor of the group order, linear complexity, `L_q[1/3]`) rather than rename a property. The second lap is where the method - four questions to ask of any novel cryptosystem - is stated.

## The one idea (shared by all three seminars): a castle *is* its characteristic polynomial mod p

A castle's signed tower count `P(k,L)` satisfies a linear recurrence with **characteristic polynomial** `char_k(x)` ([[signed-tower-count](pages/signed-tower-count.md)], [[generating-function-gallery](pages/generating-function-gallery.md)]). Reduce it modulo a prime `p` and you get a polynomial over the finite field `F_p`. The quotient ring

```
R  =  F_p[x] / (Q(x)),        Q = char_k mod p,
```

is where all the arithmetic happens. Multiplying two elements of `R` and reducing is just "apply the recurrence's rewrite rule `x^{deg Q} → …` until the degree drops" — the same rewrite [[kitamasa](pages/kitamasa.md)] uses. **The castle is the modulus `Q`.** That is the whole setup, and all three seminars live in this ring.

---

# Seminar 1 — BUILD

> *Ground rule for the room:* we are implementing a cryptosystem, not certifying one. It may well be insecure — **that is Seminar 2's job, not today's.** Today we make the thing run: reduce a castle to a ring, exponentiate, exchange a key.

## Build 1 — finite fields (why anything is periodic at all)

Over `ℚ`, `P(1,L) = 1, 0, −2, −4, −4, 0, 8, 16, …` never repeats: its eigenvalue `1+i` has `|1+i| = √2 ≠ 1`, so its powers spiral out. Reduce mod `p` and the eigenvalues land in a **finite field** `F_{p^d}` whose nonzero elements form a **cyclic group of order `p^d − 1`** — so every element now has finite order, and the sequence becomes periodic ([[finite-fields](pages/finite-fields.md)]). This is the seminar's first hands-on hour: reduce, factor `char_k mod p`, watch the period appear, and read the period off as the lcm of the eigenvalue orders ([[mod-p-observatory](pages/mod-p-observatory.md)]).

The one program: reduce a castle char poly mod `p`, factor it, and predict the period. Ten minutes, and the whole finite-field picture is in the room.

## Build 2 — binary exponentiation is the trapdoor

The forward operation is **`x^a mod Q`** — raise the generator `x` to a secret power `a` in the ring `R`. Done by **binary exponentiation** (square, reduce, multiply on set bits), this costs `O(deg(Q)² · log a)` — about **40 squarings** to reach `a = 10^12`, no matter how astronomically large `a` is. This is *exactly* [[kitamasa](pages/kitamasa.md)]: the castle solve already uses `x^n mod char_k` to jump to `P(k, 10^12)`. **The castle's fast-index trick is a modular exponentiation, and modular exponentiation is the trapdoor of Diffie–Hellman.** The seminar's second hour is just noticing that we already wrote the trapdoor.

## Build 3 — a working castle Diffie–Hellman (the deliverable)

Public parameters: a prime `p` and a public castle `Q = char_k mod p` (here `char_2 = x³ − 3x² + 4x − 4`, degree 3). The generator is the polynomial `g = x`.

```python
p = 10**9 + 7
Q = [-4 % p, 4, -3 % p, 1]        # x^3 - 3x^2 + 4x - 4, monic, low->high  (the public castle)
g = [0, 1, 0]                      # the polynomial x

def mulmod(A, B, Q, p):            # multiply in F_p[x]/(Q)
    r = [0] * (len(A) + len(B) - 1)
    for i, a in enumerate(A):
        for j, b in enumerate(B):
            r[i + j] = (r[i + j] + a * b) % p
    d = len(Q) - 1                 # reduce mod Q (Q monic degree d) — the recurrence rewrite
    for i in range(len(r) - 1, d - 1, -1):
        c = r[i]
        for j in range(d + 1):
            r[i - d + j] = (r[i - d + j] - c * Q[j]) % p
    return (r[:d] + [0] * d)[:d]

def powmod(base, e, Q, p):         # x^e mod Q, by binary exponentiation (Kitamasa)
    res = ([1] + [0] * (len(Q) - 2))
    base = (base[:len(Q)-1] + [0]*len(Q))[:len(Q)-1]
    while e:
        if e & 1: res = mulmod(res, base, Q, p)
        base = mulmod(base, base, Q, p)
        e >>= 1
    return res

a = 373309869                      # Alice's PRIVATE key (a secret exponent)
b = 566180101                      # Bob's PRIVATE key
A = powmod(g, a, Q, p)             # Alice's PUBLIC castle-key = x^a mod Q
B = powmod(g, b, Q, p)             # Bob's   PUBLIC castle-key = x^b mod Q
sA = powmod(B, a, Q, p)            # Alice computes (x^b)^a
sB = powmod(A, b, Q, p)            # Bob   computes (x^a)^b
assert sA == sB                    # x^{ab} mod Q — the SHARED SECRET
```

Alice and Bob, exchanging only their public castle-keys `A` and `B`, arrive at the **same** ring element `x^{ab} mod Q` — a shared secret an eavesdropper who saw only `Q`, `A`, `B` cannot (naively) reconstruct without solving a discrete logarithm. **That is a working asymmetric castle cryptosystem in twenty lines**, built entirely from the wiki's own Kitamasa primitive.[^1] From here Seminar 1 hangs the usual constructions off the shared secret and stops: a one-time pad, a toy ElGamal, a signature by the same `x^a` map — all *implementation*, no security claims. The room leaves with a running system and one deliberately unanswered question ("is it any good?") that becomes the whole of Seminar 2.

## Build 4 — primes decide the shape (quadratic reciprocity, live)

Whether `Q` splits mod `p` — and therefore how the group `R^*` factors and how big the key space is — is a **prime-dependent** question answered by **quadratic reciprocity**. For `char_1 = x² − 2x + 2`, the discriminant is `−4`, so it splits iff `−1` is a square mod `p`, i.e. **`p ≡ 1 (mod 4)`** ([[finite-fields](pages/finite-fields.md)], [[mod-p-observatory](pages/mod-p-observatory.md)]). Choosing the prime is choosing the arithmetic, and the seminar makes that choice a hands-on experiment: try `p = 5` (splits) vs `p = 7` (stays irreducible, roots live in `F_{49}`), and watch the key space and period change. Integer sequences enter here too: the period sequence, the eigenvalue-order sequence, the count sequence mod `p` — all OEIS-adjacent. (Foreshadowing only: whether these are *secrets* is Seminar 2's question.)

---

# Seminar 2 — RED TEAM

> *This session's mindset:* you've been handed a novel cryptosystem nobody has vetted. **Evaluate it.** This is applied cryptanalysis — the real-world skill of judging an unproven design — and the castle toy is a perfect specimen because it breaks in two famous ways, each reproducible by hand.

Both attacks are already on the wiki as tools; here they are *offensive*.

## Attack 1 — the char polys factor, so the discrete log splits

`char_2 = (x − 2)(x² − x + 2)` ([[tower-parity-sectors](pages/tower-parity-sectors.md)] explains why *even-`k`* char polys factor — an internal structural fact that is now a weakness). Because `Q` factors, the ring `R = F_p[x]/(Q)` **decomposes** by the Chinese Remainder Theorem into one ring per factor — a degree-1 piece living in `F_p` and a degree-2 piece living in `F_{p²}`. The discrete log the security rested on splits into **two smaller discrete logs**, solved independently and recombined (**Pohlig–Hellman**). The attacker never faces the full-size problem.

**The lesson — structure is a liability.** Everything that makes the castle mathematically beautiful (its char poly factors, its eigenvalues have clean orders) is exactly what a cryptanalyst exploits. Real systems want *unstructured* hardness: a large prime-order group with no cheap factorization. A reducible modulus hands the attacker the factorization for free — the same reason RSA's `N = p·q` is fatal the instant it's factored.

## Attack 2 — Berlekamp–Massey reconstructs the secret castle

Suppose a variant instead tried to keep `Q` *secret* and publish a stream of count terms (a keystream). [[berlekamp-massey](pages/berlekamp-massey.md)] — the wiki's recurrence-recovery tool, and historically **the** linear-feedback-shift-register (LFSR) attack — recovers the entire recurrence from only about `2·deg(Q)` consecutive terms. Feed it `P(2,L) = 1, 1, 3, 9, 19, 33, 59, …` and it returns `1, −3, 4, −4`: **the secret castle, reconstructed from its output.**[^2]

**The lesson — a linear recurrence is never a secret.** Any linearly-generated stream is transparent to Berlekamp–Massey; this is precisely why real stream ciphers use *nonlinear* feedback. The castle's whole identity is a linear recurrence, so any scheme that leaks its output leaks the castle.

## What Seminar 2 leaves the room with

A verdict: **the toy, as built, is broken two independent ways** — one exploiting the modulus's factorization, one exploiting the linearity of its output. Neither break needed anything beyond the tools already on the wiki. The audience has now done real cryptanalysis on a novel system and can articulate *why* it fails, which is the setup for the hardening work.

---

# Seminar 3 — BLUE TEAM

> *This session's job:* remediation. You broke it in Seminar 2; now **improve it**, break the improvement, and — the hardest discipline — recognize when you've only patched a symptom rather than reached genuine hardness.

## Fix 1 — an irreducible (prime) char poly closes the CRT split

Attack 1 exploited `Q` factoring. The fix is to choose a `Q` that **does not factor** — an *irreducible* polynomial, the polynomial analogue of a prime number. And the castle family hands us exactly that for free: the **odd-`k`** char polys are irreducible over `ℚ` (`char_1 = x²−2x+2`, `char_3 = x⁴−4x³+8x²−8x+8`, `char_5`), while the even-`k` ones factor.[^3] Swap the reducible even-`k` modulus for an irreducible odd-`k` one and the ring `F_p[x]/(Q)` stops decomposing — it is (generically) the single field `F_{p^d}`, and the discrete log is now the full-size problem in one group of order `p^d − 1`, with no CRT shortcut. **The ring's Pohlig–Hellman split is gone** - but only the ring's: `p^d − 1 = ∏_{e|d} Φ_e(p)` factors *algebraically*, so Pohlig–Hellman on the **group order** still applies, and round two recovers the private key from an irreducible `char_1` in 0.04 s ([[castle-cryptography-round-two](pages/castle-cryptography-round-two.md)], Attack 4). Irreducibility is necessary, and a number - a large prime factor of `Φ_d(p)` - is what actually has to be bought. ([[castle-cryptography-number-theory](pages/castle-cryptography-number-theory.md)] unpacks *char poly*, *irreducible = prime*, and *DLP* from scratch for the engineer, with the reducible-vs-irreducible comparison worked out.)

## Fix 2 — nonlinear feedback defeats Berlekamp–Massey

Attack 2 exploited *linearity*: the castle's output obeys a linear recurrence, so Berlekamp–Massey reads it off. No choice of `Q` helps — linearity itself is the flaw. The blue-team move is the same one real stream ciphers make: **break the linearity.** Filter the linear castle stream through a nonlinear function (a nonlinear combining/filter generator), or clock it irregularly, so the visible output's linear complexity rises. *How much* it rises is computable: a degree-`e` polynomial filter on a `d`-stage register is itself linear of complexity at most `C(d+e−1, e)` (its characteristic roots are the degree-`e` monomials in the roots of `Q`), and Berlekamp–Massey over `F_p` recovers it from `2L` terms - round two measures `10 / 14 / 20` on the 4-stage `char_3` register ([[castle-cryptography-round-two](pages/castle-cryptography-round-two.md)], Attack 5). So the filter has to be *sized* (a 64-stage register with a degree-16 filter, i.e. a castle of height 63, reaches `≈ 2⁵⁵`), not merely applied.

## Fix 3 — the honest ceiling (when patching isn't hardening)

The essential blue-team skill: knowing what your fix *didn't* buy. Even with an irreducible `Q` and nonlinear output, the castle DLP lives in `F_{p^d}` for **small `d`** (these char polys are degree 2–7). Small-degree finite fields have a **subexponential** discrete-log attack (index calculus) — so the system is *less degenerate*, not *strong*. Real finite-field crypto uses enormous `d` or abandons finite fields for elliptic curves precisely for this reason. **The lesson — a patch that removes one named attack is not the same as reaching a hardness assumption nobody can break.** Seminar 3's real payoff is teaching the audience to tell those two apart: closing the CRT split is real progress; declaring victory afterward is the classic blue-team mistake.

## The series at a glance

| Seminar | Track | Deliverable | Wiki tools |
|---|---|---|---|
| 1 | **Build** | a running castle Diffie–Hellman; security question *deferred* | [[finite-fields](pages/finite-fields.md)], [[kitamasa](pages/kitamasa.md)], [[mod-p-observatory](pages/mod-p-observatory.md)] |
| 2 | **Red team** | two working attacks (CRT/Pohlig–Hellman split; Berlekamp–Massey LFSR recovery) | [[tower-parity-sectors](pages/tower-parity-sectors.md)], [[berlekamp-massey](pages/berlekamp-massey.md)] |
| 3 | **Blue team** | irreducible-`Q` fix, nonlinear-output fix, and the honest ceiling | [[castle-cryptography-number-theory](pages/castle-cryptography-number-theory.md)], odd-`k` char polys |
| 2nd lap | **Build / red / blue again** | ElGamal + Schnorr signature; Alice's key recovered (0.07 s); both fixes broken; key sizes (`Φ_d(p)` prime, linear complexity, `L_q[1/3]`); the four-question method | [[castle-cryptography-round-two](pages/castle-cryptography-round-two.md)] |

Everything runs in a plain Python REPL; no libraries beyond `sympy` for the factoring demos. The pinned programs live on [[castle-snippets](pages/castle-snippets.md)].

## Where this sits

This is a **T-Division-adjacent** seminar series (like the transcendental-approximation thread, it is a pedagogical tour that borrows the whole machine), drawing mainly on the number-theoretic core: [[finite-fields](pages/finite-fields.md)], [[mod-p-observatory](pages/mod-p-observatory.md)], [[kitamasa](pages/kitamasa.md)], [[berlekamp-massey](pages/berlekamp-massey.md)]. The **build / red-team / blue-team** split mirrors how security work is actually organized, and it keeps each session honest: Seminar 1 builds without apologizing for security, Seminar 2 evaluates a novel system on its own terms, Seminar 3 hardens and then admits the ceiling. It is a *teaching* system, not a secure one — its value is that every abstract crypto idea (trapdoor, discrete log, group structure, CRT/Pohlig–Hellman, the LFSR attack) has a concrete castle avatar you can run in the room. The from-scratch number theory for engineers (char poly, irreducible, DLP) is on [[castle-cryptography-number-theory](pages/castle-cryptography-number-theory.md)].

## Reproduce

The `castle_dh` key exchange (the `mulmod` / `powmod` pair above) and the Berlekamp–Massey reconstruction demo are pinned on [[castle-snippets](pages/castle-snippets.md)]; both were executed during ingest — the shared secret matches, and Berlekamp–Massey returns `[1, −3, 4, −4]` from the `P(2,·)` terms. Round two's `castle_dlp` (Pohlig–Hellman + baby-step giant-step), `bm_modp` (Berlekamp–Massey over `F_p`), and `castle_schnorr` are pinned there too.

## Appearances in Sources

- [[oeis-mining-pe502](pages/oeis-mining-pe502.md)] - the `P(k,·)` families and their characteristic polynomials that serve as the public castles.

## Related Concepts

- [[finite-fields](pages/finite-fields.md)] - `F_{p^d}`, cyclic multiplicative groups, and why the sequences are periodic mod `p`; the seminar's field foundation.
- [[kitamasa](pages/kitamasa.md)] - `x^n mod Q` by binary exponentiation; the castle solve's fast-index trick *is* the cryptosystem's trapdoor.
- [[berlekamp-massey](pages/berlekamp-massey.md)] - recovers the recurrence from sample terms; the LFSR attack that breaks the naive secret-castle scheme.
- [[mod-p-observatory](pages/mod-p-observatory.md)] - `period = lcm of eigenvalue orders`; the group structure the discrete log lives in, and the prime-choice experiment.
- [[signed-tower-count](pages/signed-tower-count.md)] / [[generating-function-gallery](pages/generating-function-gallery.md)] - the `P(k,L)` characteristic polynomials `char_k` used as public castles.
- [[tower-parity-sectors](pages/tower-parity-sectors.md)] - why even-`k` `char_k` factors — the structural weakness Seminar 2's first attack exploits, and the odd-`k` irreducibility Seminar 3's first fix relies on.
- [[castle-cryptography-number-theory](pages/castle-cryptography-number-theory.md)] - the engineer-facing explainer: char poly, irreducible (= prime for polynomials), and the discrete logarithm problem, from scratch.
- [[castle-cryptography-round-two](pages/castle-cryptography-round-two.md)] - the second lap: ElGamal and signature built, Alice's key recovered, both fixes broken, keys sized, and the four-question red-team method.
- [[castle-sign](pages/castle-sign.md)] - the `(−1)^{blocks}` sign underlying `P(k,L)`; the object being exponentiated.
- [[castle-snippets](pages/castle-snippets.md)] - the runnable `castle_dh` and Berlekamp–Massey programs.

## Footnotes

[^1]: Verified by execution (2026-09-18): the `mulmod` / `powmod` pair above with `Q = [−4, 4, −3, 1]` (i.e. `char_2 = x³ − 3x² + 4x − 4` monic), `p = 10⁹+7`, `g = x`, private keys `a`, `b`, yields `powmod(B,a) == powmod(A,b)` — the shared secret `x^{ab} mod Q` agrees for both parties (a nonzero degree-2 ring element). The primitive is identical to the castle solve's `P(k, 10^12)` extraction ([[kitamasa](pages/kitamasa.md)]).

[^2]: Verified by execution: rational Berlekamp–Massey on `P(2,L) = 1, 1, 3, 9, 19, 33, 59, 121, 259, 529, 1035, 2025` returns the length-3 recurrence with coefficient vector `[1, −3, 4, −4]`, i.e. the characteristic polynomial `x³ − 3x² + 4x − 4` reconstructed from the count terms alone. `char_2 = (x − 2)(x² − x + 2)` (SymPy `factor`), the factorization the discrete-log split exploits.

[^3]: Verified by execution (SymPy `Poly.is_irreducible` over `ℚ`, 2026-09-18): odd-`k` char polys `char_1 = x²−2x+2`, `char_3 = x⁴−4x³+8x²−8x+8`, `char_5 = x⁶−6x⁵+18x⁴−32x³+48x²−32x+32` are **irreducible**; even-`k` char polys `char_2`, `char_4`, `char_6` **factor** (the even/odd split of [[tower-parity-sectors](pages/tower-parity-sectors.md)]). So swapping an even-`k` modulus for an odd-`k` one removes the CRT/Pohlig–Hellman split of Attack 1. Full worked comparison on [[castle-cryptography-number-theory](pages/castle-cryptography-number-theory.md)].
