---
title: Castle cryptography, seminar 1 - the ring
category: Analyses
summary: The baseline seminar of the castle cryptography series - the algebra everyone needs before red team or blue team makes sense - as its own standalone page, peer to castle-cryptography-round-two. Seven executed sections. (1) The characteristic polynomial x^3 - 3x^2 + 4x - 4 is the recurrence P(2, L) = 3 P(2, L-1) - 4 P(2, L-2) + 4 P(2, L-3) - six numbers encode the whole sequence. (2) Reducing mod p = 101 makes the sequence periodic; period 3400 verified as lcm of eigenvalue orders (order of 2 in F_101 is 100, order of the quadratic factor's root in F_101^2 is 3400). (3) The ring F_p[x]/(Q) - elements are polynomials of degree less than d, multiplying by x is one step of the recurrence, verified in one line ([2, 3, 1] * x mod (x^3 - 3x^2 + 4x - 4) = [4, -2, 6]). (4) When Q factors, F_p[x]/(Q) splits by CRT into a product of fields; A * B in the big ring commutes with projection to each factor, verified over char_2 mod 101 which factors (x - 2)(x^2 - x + 2). (5) Element orders of x at p = 10^9 + 7 across k = 1, 2, 3, all factored - the input to every Pohlig-Hellman analysis in the later seminars. (6) Binary exponentiation - x^a mod Q for a as large as 10^30 takes 137 ring multiplies (log a squarings), so the fast index Kitamasa trick that produces P(k, 10^12) also produces the trapdoor. (7) Diffie-Hellman on the ring - twenty lines of code, security question deferred to seminar 2 by design. Companion to castle-cryptography (series overview) and castle-cryptography-round-two (second lap of the loop).
tags: [analysis, seminar, cryptography, ring, finite-field, quotient-ring, linear-recurrence, characteristic-polynomial, kitamasa, diffie-hellman, chinese-remainder-theorem, mod-p-observatory, baseline, pedagogy, implementation, castle]
sources: [oeis-mining-pe502]
created: 2026-09-18
updated: 2026-09-18
---

# Castle cryptography, seminar 1 - the ring

The [[castle-cryptography](pages/castle-cryptography.md)] series is three seminars: **ring**, **red team**, **blue team**. This is the first - the algebra baseline everyone needs before any attack or fix is legible. It sits peer to [[castle-cryptography-round-two](pages/castle-cryptography-round-two.md)] (the second lap), and it lives at one level of resolution below the compressed **BUILD** section in the series overview. Every claim below was executed; outputs are pinned. The ground rule for the room: **we are constructing a cryptosystem, not certifying one - the "is it secure?" question is entirely seminar 2's job, and setting it aside here is what lets the algebra actually get built.**

The one idea: **a castle is its characteristic polynomial mod `p`.** The seminar builds up to why that sentence carries every construction the series needs.

---

## 1. The characteristic polynomial *is* the recurrence

The signed tower count `P(k, L)` ([[signed-tower-count](pages/signed-tower-count.md)]) is C-finite of order `k+1` ([[recurrence-discovery](pages/recurrence-discovery.md)]). At `k = 2`:

```
P(2, L) = 1, 1, 3, 9, 19, 33, 59, 121, …
P(2, L) = 3·P(2, L−1) − 4·P(2, L−2) + 4·P(2, L−3)          (verified L = 3..7)
char_2(x) = x³ − 3x² + 4x − 4                                (the coefficients, monic)
```

The **characteristic polynomial** just encodes the recurrence's coefficients. Six numbers - three initial values and three coefficients - determine the entire infinite sequence. If you've built LFSRs, this is the feedback (tap) polynomial - same object, same role. It is the castle's DNA.[^1]

The **companion matrix** of `char_2` is the transfer matrix `M` you already know from [[signed-tower-count](pages/signed-tower-count.md)]: `M[i][j] = 1` if `j = i+1`, and the last row is the recurrence coefficients. Multiplying by `M` advances the state by one step. The **ring** we're about to construct is where that "multiply to advance" becomes a first-class operation on **polynomials** instead of vectors, and turns the whole sequence into one algebraic object.

## 2. Reduce mod `p`, and periodicity appears

Over `ℚ`, `P(2, L)` grows without bound - its eigenvalues have absolute value `≠ 1`, so the sequence spirals out and never repeats. Reduce mod a prime `p`, and everything now lives in a finite set: the sequence must revisit a state and become **eventually periodic** ([[mod-p-observatory](pages/mod-p-observatory.md)]).

At `p = 101`:

```
>>> [p_signed(2, L) % 101 for L in range(12)]
[1, 1, 3, 9, 19, 33, 59, 20, 57, 24, 25, 5]
>>> period of P(2, · mod 101) = 3400
>>> seq[3400 : 3403] == seq[:3]           # returns to the initial state
True
```

Not arbitrary. `char_2 mod 101` factors as `(x − 2)(x² − x + 2)` - the quadratic factor is irreducible mod 101. The sequence's eigenvalues live in `F_101` and `F_{101²}` respectively; the *period* is the **lcm of their multiplicative orders**:

| eigenvalue | lives in | multiplicative order |
|---|---|---|
| the root `2` of `(x − 2)` | `F_101^*` | `100` |
| a root of `x² − x + 2` | `F_{101²}^*` | `3400` |

`lcm(100, 3400) = 3400` - **which is exactly the period seen**.[^2] This isn't a coincidence, and it isn't a black box: the ring we're about to build is where the equation "period = lcm of eigenvalue orders" *lives*.

## 3. The ring `F_p[x] / (Q)` - and why multiplying by `x` is the recurrence

An element of `F_p[x] / (Q)` is a polynomial of degree less than `d = deg Q`, coefficients in `F_p`. Store it as a length-`d` list of coefficients. Addition is componentwise mod `p`. Multiplication is: polynomial multiplication in the usual way, then **reduce mod `Q`** - whenever the result reaches degree `d`, replace `x^d` with the recurrence rewrite. For `Q = char_2 = x³ − 3x² + 4x − 4` that rewrite is `x³ → 3x² − 4x + 4`.

Here is the whole ring in full — every operation the seminar uses:

```python
def mulmod(A, B, Q, p):              # multiply in F_p[x]/(Q), Q monic, low->high
    r = [0]*(len(A)+len(B)-1)
    for i, a in enumerate(A):
        for j, b in enumerate(B):
            r[i+j] = (r[i+j] + a*b) % p
    for i in range(len(r)-1, len(Q)-2, -1):        # reduce: x^d -> the recurrence
        for j, c in enumerate(Q):
            r[i-len(Q)+1+j] = (r[i-len(Q)+1+j] - r[i]*c) % p
    return r[:len(Q)-1]

def powmod(base, e, Q, p):           # x^e by squaring — the Kitamasa trapdoor
    res = [1] + [0]*(len(Q)-2)
    while e:
        if e & 1: res = mulmod(res, base, Q, p)
        base = mulmod(base, base, Q, p); e >>= 1
    return res
```

`mulmod`'s second loop is the `x³ → 3x² − 4x + 4` rewrite applied to polynomials, and `powmod` is the same fast-index exponentiation as [[kitamasa](pages/kitamasa.md)]. These are the page-local teaching versions of the primitives; the full pinned set (`castle_dh` and friends) lives on [[castle-snippets](pages/castle-snippets.md)].

Live, at `p = 10⁹+7`:

```
>>> mulmod([1, 1, 0], [2, 1, 0], Q, p)       # (1 + x)(2 + x) mod Q = 2 + 3x + x^2
[2, 3, 1]
>>> mulmod([2, 3, 1], [0, 1, 0], Q, p)       # ... * x mod Q: hits x^3, forces the rewrite
[4, 1000000005, 6]                           # = 4 − 2x + 6x^2  (verified by hand)
```

Manually: `x · (2 + 3x + x²) = 2x + 3x² + x³`; substitute `x³ → 3x² − 4x + 4`, and you get `4 + (2 − 4)x + (3 + 3)x² = 4 − 2x + 6x²`, matching the ring output.[^3]

Read from the LFSR side, this says the state of a length-3 castle register is precisely a ring element, and **stepping the register by one position is multiplying by `x` in the ring**. Every question about the sequence - value at position `n`, period, statistics - has become a question about the algebra of one ring.

## 4. Multiplicative structure - the CRT split of `F_p[x] / (Q)`

A ring is more than addition and multiplication: the **units** (invertible elements) form a group whose structure is what cryptography actually rests on.

- **`Q` irreducible over `F_p`.** Then `F_p[x] / (Q)` is a *field*, `F_{p^d}`, all `p^d − 1` nonzero elements are units, and the unit group is **cyclic** of order `p^d − 1`.
- **`Q` factors as `Q_1 · Q_2` over `F_p`.** Then by the **Chinese Remainder Theorem** the whole ring splits as `F_p[x] / (Q_1) × F_p[x] / (Q_2)`. Multiplication is componentwise, so the unit group is the *product* of the two factor groups.

The split isn't abstract - it's a **projection you can compute**. At `p = 101` with `Q = char_2 mod 101 = (x − 2)(x² − x + 2)`, take a ring element `A = 7 + 3x + 5x²`:

- Project mod `(x − 2)`: substitute `x = 2` into `A`. Result: `7 + 6 + 20 = 33 ∈ F_101`.
- Project mod `(x² − x + 2)`: reduce `A` mod that polynomial (or equivalently, work with `A` inside `F_101[x] / (x² − x + 2)`). Result: `[98, 8] ∈ F_{101²}`.

And multiplication commutes with these projections. With `B = 2 + x²`:

```
>>> mulmod(A, B, Q, p) = [86, 55, 51]                        # A·B in the big ring
   (mod x − 2)    A = 33, B = 6,  A·B = 97,  project(A·B) = 97      ✓
   (mod x² − x + 2)   project(A·B) == project(A) · project(B)        ✓
```

The whole point: **the ring's structure is only as coarse as its coarsest factor.** Any question about the group - element order, discrete log - splits along the factorization of `Q`. This is the setup Pohlig-Hellman will exploit in seminar 2; here it is only the algebra.

## 5. Element orders of `x` - the number the whole later series turns on

Given the unit-group order `N`, the **order of a specific element** `g` divides `N` and is computed by factoring `N` and stripping prime powers under which `g` reduces to `1`. For the generator `g = x` at `p = 10⁹ + 7`:

| `k` | `d = deg Q` | group exponent (lcm of factor group orders) | `ord(x)` | factored |
|---|---|---|---|---|
| 1 | 2 | `10¹⁸ · 1.4 · …` | `4,000,000,024` | `2³ · 500,000,003` |
| 2 | 3 | same | `500,000,007,000,000,024` | `2³ · 3² · 7 · 109² · 167 · 500,000,003` |
| 3 | 4 | `10³⁶ · …` | `800,000,016,000,000,107,200,000,240` | `2⁴ · 5 · 58,699,937 · 340,715,873 · 500,000,003` |

Two facts to lodge in the room before seminar 2 opens:[^4]

- **The size** of `ord(x)` sets the naive DLP work. At 60+ bits with big prime factors it looks intimidating.
- **The factorization** of `ord(x)` is what actually decides the DLP's cost - the largest prime factor here is `500,000,003 ≈ 2²⁹` throughout, because `p − 1 = 2 · 500,000,003` and `p − 1` divides every `p^d − 1`. This number, not `p^d`, is what the later seminars have to move.

## 6. Binary exponentiation - Kitamasa is the trapdoor

The one-way direction of the whole cryptosystem is **`x^a mod Q`**: given `a`, produce this ring element. Naively that's `a − 1` recurrence steps; with binary exponentiation ("square, reduce, and multiply on set bits") it's roughly `log₂ a` squarings and `log₂ a` conditional multiplies. This is **exactly** [[kitamasa](pages/kitamasa.md)], the algorithm the castle solve uses to jump to `P(k, 10¹²)`.

Live cost at `p = 10⁹ + 7`, `Q = char_2`:

```
   a ≈ 2^3 :    3 sq +  3 mul =   6 ops,   0.02 ms
   a ≈ 2^14:   14 sq +  6 mul =  20 ops,   0.04 ms
   a ≈ 2^20:   20 sq +  7 mul =  27 ops,   0.06 ms
   a ≈ 2^40:   40 sq + 13 mul =  53 ops,   0.11 ms
   a ≈ 2^100:  100 sq + 37 mul = 137 ops,  0.26 ms
```

Two hundred squarings for a `2²⁰⁰` exponent - **the forward map cannot be defeated by making `a` bigger**.[^5] The castle solve's fast-index trick is the trapdoor; the same twenty lines of code produce both.

The asymmetry in one screen — forward costs `log₂ a`, backward costs `a`:

```python
A = powmod(g, 12345, Q, p)          # forward: 13 squarings + 5 multiplies — instant
cur = [1, 0, 0]; e = 0              # backward: grind x, x^2, x^3, ... until you hit A
while cur != A:
    cur = mulmod(cur, g, Q, p); e += 1
```

```
>>> A
[24371334, 336255992, 769290382]
>>> e
12345
```

Recovering a 14-bit exponent cost `12345` multiplies; recovering the real private key `373309869` costs that many — and making `a` bigger never slows the forward direction. That `log₂ a`-versus-`a` gap *is* the trapdoor.[^7]

## 7. Diffie-Hellman on the ring - the seminar's deliverable

Public parameters: a prime `p` and a public castle `Q = char_k mod p`. Generator: the polynomial `g = x`. Private key: a secret exponent. Public key: `A = g^a mod Q`. Shared secret: `x^{ab} mod Q`, computed as `B^a` by one party and `A^b` by the other. The whole exchange is `mulmod` + `powmod`:

```
>>> A = powmod(x, 373309869, Q, p) = [704821174, 848698009, 235195321]
>>> B = powmod(x, 566180101, Q, p) = [ 12836899, 147220895, 148070992]
>>> powmod(B, 373309869, Q, p) == powmod(A, 566180101, Q, p)
True
>>> shared secret = [395423824, 86931747, 647893869]
```

Twenty lines of Python, no libraries, verified.[^6] Pinned as `castle_dh` on [[castle-snippets](pages/castle-snippets.md)].

The seminar hangs the natural next constructions off `castle_dh` without expanding scope: a one-time-pad symmetric cipher keyed on the shared secret; a toy ElGamal (public key `A`, encrypt as `(g^k, m · A^k)`); a Schnorr-style signature (also on the `x^a` map). Round-two builds ElGamal and the signature in earnest ([[castle-cryptography-round-two](pages/castle-cryptography-round-two.md)]).

## 8. What seminar 1 leaves the room with - and what it deliberately doesn't

**Deliverable:** a running asymmetric cryptosystem built entirely from the castle's own [[kitamasa](pages/kitamasa.md)] primitive - keypair, exchange, shared secret, all executable.

**Deliberately unanswered - and this is the point:** three open questions, each a red-team hook, each set up by an observation already made above:

1. `char_2` **factored** over `F_101` (§4). Does the same thing happen mod `10⁹ + 7`, and if so, does that factorization *do* something to the discrete log? (Seminar 2 - Attack 1.)
2. **`ord(x)` factors** as `2³ · 3² · 7 · 109² · 167 · 500,000,003` (§5). If the whole reason we chose big `p` is to make the DLP hard, does the *factorization* of the group order weaken it? (Seminar 2 - Attack 3 in round two.)
3. The sequence `P(k, L)` satisfies **a linear recurrence** with known coefficients (§1). If a variant ever leaks a stream of terms, is the whole modulus recoverable? (Seminar 2 - Attack 2.)

Each of these is a *legitimate* question about the object we just built, sitting one step past the algebra - the boundary between "we made this work" and "does anyone else's version of this work" is exactly where seminar 2 starts. Not answering them here is the discipline: a room that tries to build and attack at once ships nothing.

## Appearances in Sources

- [[oeis-mining-pe502](pages/oeis-mining-pe502.md)] - the `P(k, ·)` families and their characteristic polynomials serving as the moduli.

## Related Concepts

- [[castle-cryptography](pages/castle-cryptography.md)] - the series overview this is Seminar 1 of.
- [[castle-cryptography-round-two](pages/castle-cryptography-round-two.md)] - the second lap of the loop, where every question §8 leaves open is actually answered (private key recovered in 0.07 s, both round-one fixes broken).
- [[castle-cryptography-number-theory](pages/castle-cryptography-number-theory.md)] - engineer-facing explainer for char poly, irreducible, DLP; a lighter appendix to this page.
- [[signed-tower-count](pages/signed-tower-count.md)] / [[generating-function-gallery](pages/generating-function-gallery.md)] - where `char_k` comes from and where its factorizations are catalogued.
- [[finite-fields](pages/finite-fields.md)] - `F_p`, `F_{p^d}`, cyclic multiplicative groups; the target of the CRT projection when `Q` factors.
- [[mod-p-observatory](pages/mod-p-observatory.md)] - the period = lcm of eigenvalue orders identity, with the same experiment at more primes.
- [[kitamasa](pages/kitamasa.md)] - `x^a mod Q` by binary exponentiation; the castle solve's fast-index trick, and this seminar's trapdoor.
- [[recurrence-discovery](pages/recurrence-discovery.md)] - the recurrence order and how the char poly is discovered from data (a nice bookend to §1's "assumed known").
- [[eigenvalue-continued-fractions](pages/eigenvalue-continued-fractions.md)] - the roots of `char_k` and their continued fractions; the same eigenvalues whose orders §2 takes the lcm of.
- [[castle-snippets](pages/castle-snippets.md)] - `castle_dh` pinned; the `mulmod` / `powmod` / `p_signed` primitives used throughout.

## Footnotes

[^1]: Verified by execution (2026-09-18): `[p_signed(2, L) for L in range(8)] = [1, 1, 3, 9, 19, 33, 59, 121]`; the recurrence `P(L) = 3 P(L−1) − 4 P(L−2) + 4 P(L−3)` holds for `L = 3, 4, 5, 6, 7` (five independent checks); `char_2(x) = x³ − 3x² + 4x − 4` from the signed transfer matrix's characteristic polynomial (SymPy).

[^2]: Verified by execution (2026-09-18): with `p = 101`, `Q = char_2 mod p = (x − 2)(x² − x + 2)` (SymPy `factor_list`, `modulus = 101`), the sequence `P(2, L) mod 101` first returns to its initial state `(1, 1, 3)` at `L = 3400`. Independently: the root `2` has multiplicative order `100` in `F_101^*` (max possible); a root of `x² − x + 2` has multiplicative order `3400` in `F_{101²}^*` (verified by factor-stripping `p² − 1 = 10200`, `10200 = 2³ · 3 · 5² · 17`). `lcm(100, 3400) = 3400`, the observed period.

[^3]: Verified by execution (2026-09-18) at `p = 10⁹ + 7`, `Q = [-4, 4, -3, 1]` (i.e. `x³ − 3x² + 4x − 4`): `mulmod([1,1,0], [2,1,0], Q, p) = [2, 3, 1]`; `mulmod([2,3,1], [0,1,0], Q, p) = [4, 1000000005, 6]`, i.e. `4 − 2x + 6x²` (since `−2 mod p = 10⁹ + 5`), matching the hand computation `2x + 3x² + x³ → 4 − 2x + 6x²` after the rewrite `x³ = 3x² − 4x + 4`.

[^4]: Verified by execution (2026-09-18) at `p = 10⁹ + 7`. `char_1 mod p` irreducible, `ord(x) = 4000000024 = 2³ · 500000003`. `char_2 mod p` factors as `(x − 2)(x² − x + 2)` (same as over `ℚ`, since `p` doesn't split anything new here), `ord(x) = 500000007000000024 = 2³ · 3² · 7 · 109² · 167 · 500000003`. `char_3 mod p` irreducible (odd `k`), `ord(x) = 800000016000000107200000240 = 2⁴ · 5 · 58699937 · 340715873 · 500000003`. `500000003 = (p − 1)/2` divides every `ord(x)` shown because `p − 1 | p^d − 1` for all `d`.

[^5]: Verified by execution (2026-09-18) at `p = 10⁹ + 7`, `Q = char_2 mod p`, `g = x`, counting `mulmod` calls. Operation count for `powmod(x, a)`: 6 at `a = 7`, 20 at `a ≈ 2¹⁴`, 27 at `a ≈ 2²⁰`, 53 at `a ≈ 2⁴⁰`, 137 at `a ≈ 2¹⁰⁰`. Wall-clock 0.02-0.26 ms in pure Python. Squaring count = `⌊log₂ a⌋`, multiply count = popcount(`a`) − 1 (each set bit past the top).

[^6]: Verified by execution (2026-09-18) at `p = 10⁹ + 7`, `Q = char_2 mod p`, `g = x`, `a = 373309869`, `b = 566180101`: `A = [704821174, 848698009, 235195321]`, `B = [12836899, 147220895, 148070992]`, and `powmod(B, a) == powmod(A, b) = [395423824, 86931747, 647893869]`. Same numbers as pinned on `castle_dh` in [[castle-snippets](pages/castle-snippets.md)] and [[castle-cryptography](pages/castle-cryptography.md)].

[^7]: Verified by execution (2026-09-18) at `p = 10⁹ + 7`, `Q = char_2 mod p`: `powmod(g, 12345, Q, p) = [24371334, 336255992, 769290382]` costs 13 squarings + 5 multiplies (`⌊log₂ 12345⌋ = 13`, `popcount(12345) = 6`), while brute-force `x, x², x³, …` recovers the exponent only after `12345` multiplies. For the real private key the same loop is `373309869` multiplies.
