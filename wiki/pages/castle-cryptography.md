---
title: Castle cryptography - a hands-on wandering seminar
category: Analyses
summary: An implementation-first seminar that builds a working public-key system whose keypair is a "castle" instead of an SSH keypair. The public castle is a characteristic polynomial Q(x) over F_p (a castle's own char_k); the private key is a secret exponent; encryption/key-exchange is Kitamasa exponentiation x^a mod Q — the exact primitive the castle solve uses to reach P(k, 10^12). A running castle Diffie-Hellman is given in ~20 lines. The seminar wanders through finite fields (F_{p^d}, cyclic groups), binary exponentiation, primes (splitting via quadratic reciprocity), and integer sequences, always via short programs and worked examples — and then breaks its own toy system two ways (the char polys factor, so the discrete log splits; and Berlekamp–Massey reconstructs the secret castle from the public count sequence), turning "why real crypto needs unstructured hardness" into the punchline. Every wiki primitive it needs already exists: finite-fields, kitamasa, berlekamp-massey, mod-p-observatory, castle-sign.
tags: [analysis, seminar, cryptography, public-key, finite-field, kitamasa, berlekamp-massey, discrete-log, diffie-hellman, pedagogy, implementation, castle]
sources: [oeis-mining-pe502]
created: 2026-09-18
updated: 2026-09-18
---

# Castle cryptography

## The pitch

A wandering, implementation-first seminar: **build a public-key system whose keypair is a castle.** Instead of an SSH `id_rsa` / `id_rsa.pub`, you carry a **private castle** and a **public castle**, and two people who have never met derive a shared secret from each other's public castles. The seminar is not a theorem march — it is short programs, worked examples, and a system you can actually run, wandering through the fields that connect at the castle: **finite fields, binary exponentiation, primes, and integer sequences**. Then, honestly, we **break the toy** — twice — because the ways it breaks are exactly the lessons real cryptography teaches.

Every primitive the seminar needs is already on the wiki. The whole thing is "we already built the machine; now point it at cryptography."

## The one idea: a castle *is* its characteristic polynomial mod p

A castle's signed tower count `P(k,L)` satisfies a linear recurrence with **characteristic polynomial** `char_k(x)` ([[signed-tower-count](pages/signed-tower-count.md)], [[generating-function-gallery](pages/generating-function-gallery.md)]). Reduce it modulo a prime `p` and you get a polynomial over the finite field `F_p`. The quotient ring

```
R  =  F_p[x] / (Q(x)),        Q = char_k mod p,
```

is where all the arithmetic happens. Multiplying two elements of `R` and reducing is just "apply the recurrence's rewrite rule `x^{deg Q} → …` until the degree drops" — the same rewrite [[kitamasa](pages/kitamasa.md)] uses. **The castle is the modulus `Q`.** That is the whole setup.

## Wander 1 — finite fields (why anything is periodic at all)

Over `ℚ`, `P(1,L) = 1, 0, −2, −4, −4, 0, 8, 16, …` never repeats: its eigenvalue `1+i` has `|1+i| = √2 ≠ 1`, so its powers spiral out. Reduce mod `p` and the eigenvalues land in a **finite field** `F_{p^d}` whose nonzero elements form a **cyclic group of order `p^d − 1`** — so every element now has finite order, and the sequence becomes periodic ([[finite-fields](pages/finite-fields.md)]). This is the seminar's first hands-on hour: reduce, factor `char_k mod p`, watch the period appear, and read the period off as the lcm of the eigenvalue orders ([[mod-p-observatory](pages/mod-p-observatory.md)]).

The one program: reduce a castle char poly mod `p`, factor it, and predict the period. Ten minutes, and the whole finite-field picture is in the room.

## Wander 2 — binary exponentiation is the trapdoor

The forward operation is **`x^a mod Q`** — raise the generator `x` to a secret power `a` in the ring `R`. Done by **binary exponentiation** (square, reduce, multiply on set bits), this costs `O(deg(Q)² · log a)` — about **40 squarings** to reach `a = 10^12`, no matter how astronomically large `a` is. This is *exactly* [[kitamasa](pages/kitamasa.md)]: the castle solve already uses `x^n mod char_k` to jump to `P(k, 10^12)`. **The castle's fast-index trick is a modular exponentiation, and modular exponentiation is the trapdoor of Diffie–Hellman.** The seminar's second hour is just noticing that we already wrote the trapdoor.

## The centerpiece — a working castle Diffie–Hellman

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

Alice and Bob, exchanging only their public castle-keys `A` and `B`, arrive at the **same** ring element `x^{ab} mod Q` — a shared secret an eavesdropper who saw only `Q`, `A`, `B` cannot (naively) reconstruct without solving a discrete logarithm. **That is a working asymmetric castle cryptosystem in twenty lines**, built entirely from the wiki's own Kitamasa primitive.[^1] From here the seminar hangs the usual constructions off the shared secret: a one-time pad, a toy ElGamal, a signature by the same `x^a` map.

## Wander 3 — primes decide the shape (quadratic reciprocity, live)

Whether `Q` splits mod `p` — and therefore how the group `R^*` factors and how big the key space is — is a **prime-dependent** question answered by **quadratic reciprocity**. For `char_1 = x² − 2x + 2`, the discriminant is `−4`, so it splits iff `−1` is a square mod `p`, i.e. **`p ≡ 1 (mod 4)`** ([[finite-fields](pages/finite-fields.md)], [[mod-p-observatory](pages/mod-p-observatory.md)]). Choosing the prime is choosing the arithmetic, and the seminar makes that choice a hands-on experiment: try `p = 5` (splits) vs `p = 7` (stays irreducible, roots live in `F_{49}`), and watch the key space and period change. Integer sequences enter here too: the period sequence, the eigenvalue-order sequence, the count sequence mod `p` — all OEIS-adjacent, all `Berlekamp–Massey`-recoverable (next).

## The punchline — break your own castle (twice)

A good crypto seminar earns its trust by attacking what it built. The castle toy breaks in two instructive ways, and *both attacks are already on the wiki*:

1. **The castle char polys factor — so the discrete log splits.** `char_2 = (x − 2)(x² − x + 2)` ([[tower-parity-sectors](pages/tower-parity-sectors.md)] explains why even-`k` char polys factor). By CRT the ring `R` decomposes along the factors, and the discrete log reduces to smaller discrete logs in `F_p` and `F_{p²}` (Pohlig–Hellman). **The castle's beautiful structure is a cryptographic liability** — the exact opposite of what you want. This is the seminar's sharpest lesson: real systems need *unstructured* hardness (large prime-order groups, no cheap factorization), and the castle, being so richly structured, is a cautionary example, not a product.

2. **Berlekamp–Massey reconstructs the secret castle from the public sequence.** If a scheme instead tried to keep `Q` secret and publish a stream of count terms, [[berlekamp-massey](pages/berlekamp-massey.md)] — the wiki's recurrence-recovery tool, and historically *the* linear-feedback-shift-register attack — recovers the whole recurrence from about `2·deg(Q)` consecutive terms. Feed it `P(2,L) = 1,1,3,9,19,33,59,…` and it returns `1, −3, 4, −4`: the castle, reconstructed.[^2] **A linear recurrence is never a secret** — the seminar's second one-liner attack, and the reason stream ciphers use *nonlinear* feedback.

The arc "build it → run it → break it → understand why it broke" is the whole pedagogy: the castle cryptosystem is a superb *teaching* cryptosystem precisely because it is transparent enough to attack by hand.

## Suggested three-session shape

1. **Session 1 — the ring.** Reduce a castle char poly mod `p`, factor it, predict the period ([[finite-fields](pages/finite-fields.md)], [[mod-p-observatory](pages/mod-p-observatory.md)]). Establish `R = F_p[x]/(Q)` and its multiplication as the recurrence rewrite. Program: `mulmod`.
2. **Session 2 — the system.** Binary exponentiation = Kitamasa = the trapdoor; run the castle Diffie–Hellman above; build a one-time pad on the shared secret. Program: `powmod` and the key exchange. Prime-choice experiment (Wander 3).
3. **Session 3 — the attacks.** Factor the modulus and split the discrete log (Pohlig–Hellman by hand on a small `p`); reconstruct the secret castle with Berlekamp–Massey. Close on "what real crypto changes to survive these" — nonlinearity, large prime-order groups, no exploitable structure.

Everything runs in a plain Python REPL; no libraries beyond `sympy` for the factoring demo. The pinned programs live on [[castle-snippets](pages/castle-snippets.md)].

## Where this sits

This is a **T-Division-adjacent** wandering seminar (like the transcendental-approximation thread, it is a pedagogical tour that borrows the whole machine), but it draws mainly on the number-theoretic core: [[finite-fields](pages/finite-fields.md)], [[mod-p-observatory](pages/mod-p-observatory.md)], [[kitamasa](pages/kitamasa.md)], [[berlekamp-massey](pages/berlekamp-massey.md)]. It is honest about being a *teaching* system, not a secure one — its value is that every abstract crypto idea (trapdoor, discrete log, group structure, LFSR attack) has a concrete castle avatar you can run in the room.

## Reproduce

The `castle_dh` key exchange (the `mulmod` / `powmod` pair above) and the Berlekamp–Massey reconstruction demo are pinned on [[castle-snippets](pages/castle-snippets.md)]; both were executed during ingest — the shared secret matches, and Berlekamp–Massey returns `[1, −3, 4, −4]` from the `P(2,·)` terms.

## Appearances in Sources

- [[oeis-mining-pe502](pages/oeis-mining-pe502.md)] - the `P(k,·)` families and their characteristic polynomials that serve as the public castles.

## Related Concepts

- [[finite-fields](pages/finite-fields.md)] - `F_{p^d}`, cyclic multiplicative groups, and why the sequences are periodic mod `p`; the seminar's field foundation.
- [[kitamasa](pages/kitamasa.md)] - `x^n mod Q` by binary exponentiation; the castle solve's fast-index trick *is* the cryptosystem's trapdoor.
- [[berlekamp-massey](pages/berlekamp-massey.md)] - recovers the recurrence from sample terms; the LFSR attack that breaks the naive secret-castle scheme.
- [[mod-p-observatory](pages/mod-p-observatory.md)] - `period = lcm of eigenvalue orders`; the group structure the discrete log lives in, and the prime-choice experiment.
- [[signed-tower-count](pages/signed-tower-count.md)] / [[generating-function-gallery](pages/generating-function-gallery.md)] - the `P(k,L)` characteristic polynomials `char_k` used as public castles.
- [[tower-parity-sectors](pages/tower-parity-sectors.md)] - why even-`k` `char_k` factors — the structural weakness the first attack exploits.
- [[castle-sign](pages/castle-sign.md)] - the `(−1)^{blocks}` sign underlying `P(k,L)`; the object being exponentiated.
- [[castle-snippets](pages/castle-snippets.md)] - the runnable `castle_dh` and Berlekamp–Massey programs.

## Footnotes

[^1]: Verified by execution (2026-09-18): the `mulmod` / `powmod` pair above with `Q = [−4, 4, −3, 1]` (i.e. `char_2 = x³ − 3x² + 4x − 4` monic), `p = 10⁹+7`, `g = x`, private keys `a`, `b`, yields `powmod(B,a) == powmod(A,b)` — the shared secret `x^{ab} mod Q` agrees for both parties (a nonzero degree-2 ring element). The primitive is identical to the castle solve's `P(k, 10^12)` extraction ([[kitamasa](pages/kitamasa.md)]).

[^2]: Verified by execution: rational Berlekamp–Massey on `P(2,L) = 1, 1, 3, 9, 19, 33, 59, 121, 259, 529, 1035, 2025` returns the length-3 recurrence with coefficient vector `[1, −3, 4, −4]`, i.e. the characteristic polynomial `x³ − 3x² + 4x − 4` reconstructed from the count terms alone. `char_2 = (x − 2)(x² − x + 2)` (SymPy `factor`), the factorization the discrete-log split exploits.
