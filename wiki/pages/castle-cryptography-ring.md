---
title: Castle cryptography, seminar 1 - the ring
category: Analyses
summary: Seminar 1 of the castle cryptography series, the algebra the later rounds use, in the order the system is used. (1) char_2 = x^3 − 3x^2 + 4x − 4 is the recurrence P(2, L) = 3P(2, L−1) − 4P(2, L−2) + 4P(2, L−3). (2) In R = F_p[x]/(Q), multiplication by x is one step of the recurrence. (3) x^a mod Q by binary exponentiation costs bitlength(a) + popcount(a) ring multiplications in the loop as written (53 at a = 10^12), the Kitamasa step of the castle count. (4) Diffie-Hellman on R with public parameters (p, Q), private exponent a and public key x^a mod Q. (5) The public key is the window P(k, a), …, P(k, a + k) mod p of signed tower counts, through the Hankel matrix of P(k, 0), …, P(k, 2k), of determinant (−1)^{k(k+1)/2} 2^{k²} for k ≤ 7 and invertible mod every odd prime. (6) num_k and den_k are coprime mod every prime, since their update matrix has determinant −1, so the period of P(k, ·) mod an odd prime is the order of x; at p = 101 it is 3400. (7) The unit group of R, by the Chinese Remainder Theorem a product of the unit groups of the factors of Q, and the order of x at p = 10^9 + 7 for k = 1, 2, 3, factored; the prime 500000003 = (p − 1)/2 divides all three.
tags: [analysis, seminar, cryptography, ring, finite-field, quotient-ring, linear-recurrence, characteristic-polynomial, kitamasa, diffie-hellman, chinese-remainder-theorem, hankel-matrix, mod-p-observatory, baseline, pedagogy, implementation, castle]
sources: [oeis-mining-pe502, calugareanu-hamburg-exercises-basic-ring-theory]
created: 2026-09-18
updated: 2026-10-25
---

# Castle cryptography, seminar 1 - the ring

The [[castle-cryptography](pages/castle-cryptography.md)] series has three seminars: build, red team and blue team. This page is Seminar 1 in full, the algebra the attacks and fixes use; [[castle-cryptography-round-two](pages/castle-cryptography-round-two.md)] is the second round of the series. Sections 1 to 4 build the system in the order it is used: the recurrence, the ring, the one-way map and the key exchange. Section 5 reads the public key as castle counts. Sections 6 and 7 describe the group the keys live in: the period and the order of `x`. The page leaves security to Seminar 2, and section 8 lists the facts that Seminar 2 and round two start from. The central object is the characteristic polynomial `char_k` of the signed tower count `P(k, ·)`, reduced mod a prime `p`.

---

## 1. The characteristic polynomial is the recurrence

The signed tower count `P(k, L)` satisfies a linear recurrence of order `k + 1` in `L` ([[signed-tower-count](pages/signed-tower-count.md)]). At `k = 2`:[^1]

```
P(2, L)  =  1, 1, 3, 9, 19, 33, 59, 121, …            (L = 0, 1, 2, …)
P(2, L)  =  3·P(2, L−1) − 4·P(2, L−2) + 4·P(2, L−3)
char_2(x)  =  x³ − 3x² + 4x − 4
```

The characteristic polynomial records the coefficients of the recurrence, and with the three initial values `1, 1, 3` it determines the whole sequence. In the language of linear feedback shift registers (LFSRs), registers whose next bit is a fixed linear combination of the previous ones, `char_2` is the feedback polynomial of a three-stage register.

The companion matrix of `char_2`, with ones above the diagonal and the recurrence coefficients in the last row, advances the state vector `(P(2, L), P(2, L+1), P(2, L+2))` by one step. It has the same characteristic polynomial as the signed transfer matrix `M̃_2` ([[signed-tower-count](pages/signed-tower-count.md)]). In the ring of section 2, the same step is multiplication of a polynomial by `x`.

## 2. The ring `F_p[x]/(Q)`, where multiplying by `x` is the recurrence

An element of `R = F_p[x]/(Q)` is a polynomial of degree less than `d = deg Q` with coefficients in `F_p`, stored as its list of `d` coefficients. Addition is coefficientwise mod `p`. Multiplication is polynomial multiplication followed by reduction mod `Q`: whenever the product reaches degree `d`, `x^d` is replaced by the recurrence. For `Q = char_2` the replacement is `x³ → 3x² − 4x + 4`.

```python
def mulmod(A, B, Q, p):              # multiply in F_p[x]/(Q), Q monic, coefficients low to high
    r = [0]*(len(A)+len(B)-1)
    for i, a in enumerate(A):
        for j, b in enumerate(B):
            r[i+j] = (r[i+j] + a*b) % p
    for i in range(len(r)-1, len(Q)-2, -1):        # reduce: x^d -> the recurrence
        for j, c in enumerate(Q):
            r[i-len(Q)+1+j] = (r[i-len(Q)+1+j] - r[i]*c) % p
    return r[:len(Q)-1]

def powmod(base, e, Q, p):           # base^e by binary exponentiation
    res = [1] + [0]*(len(Q)-2)
    while e:
        if e & 1: res = mulmod(res, base, Q, p)
        base = mulmod(base, base, Q, p); e >>= 1
    return res
```

The second loop of `mulmod` is the replacement `x³ → 3x² − 4x + 4`, and `powmod` is the exponentiation of [[kitamasa](pages/kitamasa.md)]. The versions used by the later rounds are `castle_dh` and its helpers on [[castle-snippets-cryptography](pages/castle-snippets-cryptography.md)].

At `p = 10⁹ + 7`, with `Q = char_2`:[^2]

```
>>> mulmod([1, 1, 0], [2, 1, 0], Q, p)       # (1 + x)(2 + x) = 2 + 3x + x^2
[2, 3, 1]
>>> mulmod([2, 3, 1], [0, 1, 0], Q, p)       # times x: reaches x^3, so it is replaced
[4, 1000000005, 6]                           # 4 − 2x + 6x^2
```

By hand, `x · (2 + 3x + x²) = 2x + 3x² + x³`, and replacing `x³` by `3x² − 4x + 4` gives `4 + (2 − 4)x + (3 + 3)x² = 4 − 2x + 6x²`.

The state of the three-stage castle register is an element of `R`, and one step of the register is multiplication by `x`. The term at position `n` and the period are statements about the powers of `x` in `R`.

## 3. Binary exponentiation

The one-way map of the cryptosystem is `a ↦ x^a mod Q`. Computed one step at a time it takes `a − 1` multiplications. Binary exponentiation squares once per bit of `a` and multiplies once per set bit, so the `powmod` loop of section 3 calls `mulmod` `bitlength(a) + popcount(a)` times. This is the step of [[kitamasa](pages/kitamasa.md)] that the castle count uses to reach `P(k, 10¹²)`. At `p = 10⁹ + 7`, `Q = char_2`:[^3]

| `a` | bits | set bits | squarings | multiplications | `mulmod` calls |
|---|---|---|---|---|---|
| `7` | 3 | 3 | 3 | 3 | 6 |
| `12345` | 14 | 6 | 14 | 6 | 20 |
| `10⁶` | 20 | 7 | 20 | 7 | 27 |
| `10¹²` | 40 | 13 | 40 | 13 | 53 |
| `10³⁰` | 100 | 37 | 100 | 37 | 137 |

The loop's last squaring and its first multiplication, by the identity, are not needed, so `bitlength(a) − 1` squarings and `popcount(a) − 1` multiplications suffice: 39 squarings and 12 multiplications at `a = 10¹²`, as on [[castle-cryptography](pages/castle-cryptography.md)].

The inverse direction, by trying `x, x², x³, …`, takes `a` multiplications:

```python
A = powmod(g, 12345, Q, p)          # forward: 20 mulmod calls
cur = [1, 0, 0]; e = 0              # backward: x, x^2, x^3, ... until A
while cur != A:
    cur = mulmod(cur, g, Q, p); e += 1
```

```
>>> A
[24371334, 336255992, 769290382]
>>> e
12345
```

For the private key `a = 373309869` of section 4 the same search takes `373309869` multiplications, while the forward direction takes 40 `mulmod` calls (29 bits, 11 of them set). Faster inverse attacks, baby-step giant-step and Pohlig-Hellman, are the subject of Seminar 2 and round two.

## 4. Diffie-Hellman on the ring

The public parameters are the prime `p` and `Q = char_k mod p`, and the generator is `g = x`. Alice's private key is an exponent `a` and Alice's public key is `A = x^a mod Q`; Bob's are `b` and `B = x^b mod Q`. Both compute the shared secret `x^{ab} mod Q`, Alice as `B^a` and Bob as `A^b`. At `p = 10⁹ + 7`, `Q = char_2`:[^4]

```
>>> A = powmod(x, 373309869, Q, p)
[704821174, 848698009, 235195321]
>>> B = powmod(x, 566180101, Q, p)
[12836899, 147220895, 148070992]
>>> powmod(B, 373309869, Q, p) == powmod(A, 566180101, Q, p)
True
>>> powmod(B, 373309869, Q, p)
[395423824, 86931747, 647893869]
```

The exchange is `castle_dh` on [[castle-snippets-cryptography](pages/castle-snippets-cryptography.md)]. ElGamal encryption, with public key `A` and ciphertext `(g^k, m · A^k)`, and a Schnorr-style signature use the same map; round two builds both ([[castle-cryptography-round-two](pages/castle-cryptography-round-two.md)]).

## 5. The public key is a window of castle counts

[[kitamasa](pages/kitamasa.md)]'s method reads a term of the sequence off a ring element. For `c = c_0 + c_1 x + ⋯ + c_k x^k` in `R`, set

```
ℓ(c)  =  c_0·P(k, 0) + c_1·P(k, 1) + ⋯ + c_k·P(k, k)   (mod p).
```

Then `ℓ(x^n) = P(k, n) mod p` for every `n ≥ 0`, since reducing `x^n` modulo `Q` uses the same recurrence as the sequence. So the public key `A = x^a mod Q` determines a **window** of `k + 1` consecutive signed tower counts:

```
ℓ(A), ℓ(x·A), …, ℓ(x^k·A)  =  P(k, a), P(k, a + 1), …, P(k, a + k)   (mod p).
```

The map from the coefficients of `A` to its window is the Hankel matrix `H_k`, whose entry in row `i` and column `j` is `P(k, i + j)`, for `0 ≤ i, j ≤ k`. At `k = 2`,

```
H_2  =  [[1, 1, 3], [1, 3, 9], [3, 9, 19]],        det H_2  =  −16,
```

and for every `k ≤ 7` (computed)

```
det H_k  =  (−1)^{k(k+1)/2} · 2^{k²}.
```

`H_k` is invertible mod every odd prime `p`. A sequence that satisfies a recurrence of order `k + 1` has an invertible `(k + 1) × (k + 1)` Hankel matrix exactly when it satisfies no shorter recurrence, and section 6 proves that the shortest recurrence of `P(k, ·) mod p` is `char_k mod p`. So the window determines `A`, and the exchange of section 4 can be run on castle counts alone. At `p = 10⁹ + 7` and `Q = char_2`, with the keys of section 4:[^5]

```
Alice publishes   P(2, a),  P(2, a + 1),  P(2, a + 2)   =  259105132, 367673055, 221456604
Bob publishes     P(2, b),  P(2, b + 1),  P(2, b + 2)   =  604270770, 787138505, 176847572
shared window     P(2, ab), P(2, ab + 1), P(2, ab + 2)  =  426037164, 487263844, 278640608
```

Each party turns the other's window into a ring element with `H_2^{−1}`, raises it to its own exponent, and reads off the window of `x^{ab}`. The keypair is a castle count: the private key is a base length `a`, the public key is the signed count of the towers of height at most `k` on the bases of length `a`, …, `a + k`, mod `p`, and the discrete logarithm asks for the base length from that window. A run of `2(k + 1)` consecutive terms is twice a window, and from it Berlekamp-Massey recovers `Q` (section 8).

## 6. The period is the order of `x`

Over the rationals `P(2, L)` grows: the roots of `char_2` are `2` and `(1 ± i√7)/2`, of moduli `2` and `√2`. Mod a prime `p` the state vector takes at most `p³` values, so it repeats, and since the constant term `−4` of `char_2` is invertible mod an odd prime `p`, the step can be run backwards and the sequence is purely periodic ([[mod-p-observatory](pages/mod-p-observatory.md)]).

At `p = 101`:[^6]

```
>>> [P(2, L) % 101 for L in range(12)]
[1, 1, 3, 9, 19, 33, 59, 20, 57, 24, 25, 5]
>>> period of P(2, ·) mod 101
3400
```

`char_2 mod 101 = (x − 2)(x² − x + 2)`, and the quadratic factor is irreducible mod 101, since its discriminant `−7` is not a square mod 101 (Euler's criterion: `(−7)^{50} ≡ −1 mod 101`). The roots of `char_2` lie in `F_101` and `F_{101²}`, and the order of `x` in `R = F_101[x]/(char_2)` is the lcm of their multiplicative orders:

| root | lies in | multiplicative order |
|---|---|---|
| `2`, the root of `x − 2` | `F_101^*` | `100` |
| a root of `x² − x + 2` | `F_{101²}^*` | `3400` |

`lcm(100, 3400) = 3400`, which is the period. The period of a sequence mod `p` always divides the order of `x` in `R`, and it equals it when `num_k` and `den_k` are coprime mod `p`, so that `Q` is the shortest recurrence of the sequence ([[castle-ring-invariant-factors](pages/castle-ring-invariant-factors.md)]). That condition holds at every prime.

**Proposition.** For every `k` and every prime `p`, `num_k` and `den_k` are coprime mod `p`. So for every odd prime `p` the shortest recurrence of `P(k, ·) mod p` is `char_k mod p`, and the period of `P(k, ·) mod p` is the order of `x` in `R`.

*Proof.* The update of [[signed-tower-count](pages/signed-tower-count.md)], `num_k = 2·den_{k−1} − num_{k−1}` and `den_k = (1 − 2x)·den_{k−1} + x·num_{k−1}`, multiplies the vector `(num, den)` by the matrix `M = [[−1, 2], [x, 1 − 2x]]`, whose determinant is `−1`. So `M` is invertible over `F_p[x]` for every prime `p`, and `(num_0, den_0) = (1, 1 − x)` is `M^{−k}` applied to `(num_k, den_k)`. A common factor of `num_k` and `den_k` mod `p` therefore divides `num_0 = 1`. For odd `p`, `den_k` keeps its degree `k + 1` mod `p`, since its leading coefficient is `(−1)^{k+1} 2^k`, and `deg num_k ≤ k` by the update; so `num_k/den_k` is in lowest terms with a denominator of degree `k + 1`, and the shortest recurrence of `P(k, ·) mod p` is `char_k mod p`. ∎

Over the integers, `|Res(num_k, den_k)| = 2^{k²}` for `k ≤ 7` (computed), the absolute value of `det H_k` in section 5. It has no odd prime factor, although the discriminant of `char_k` has some: `7` for `char_2`, a prime at which `char_2` has a repeated root ([[castle-ring-invariant-factors](pages/castle-ring-invariant-factors.md)]).[^7]

## 7. The unit group and the order of `x`

The units of `R`, its invertible elements, form a group, and discrete-logarithm cryptography works in that group.

- **`Q` irreducible over `F_p`.** Then `R` is the field `F_{p^d}`, every nonzero element is a unit, and the unit group is cyclic of order `p^d − 1` ([[finite-fields](pages/finite-fields.md)]).
- **`Q = Q_1 · Q_2` over `F_p` with `gcd(Q_1, Q_2) = 1`.** Then by the Chinese Remainder Theorem `R ≅ F_p[x]/(Q_1) × F_p[x]/(Q_2)` ([[chinese-remainder-theorem](pages/chinese-remainder-theorem.md)]).[^8] Multiplication is componentwise, so the unit group is the product of the unit groups of the two factors.

At `p = 101`, `char_2 = (x − 2)(x² − x + 2)` with the quadratic factor irreducible, so `R ≅ F_101 × F_{101²}` and its unit group is `F_101^* × F_{101²}^*`. Attack 1 of [[castle-cryptography](pages/castle-cryptography.md)] computes the two projections and the idempotents that invert them.

The order of an element `g` divides the order `N` of the unit group, and is found by factoring `N` and removing each prime factor `q` while `g^{N/q} = 1`. For `g = x` at `p = 10⁹ + 7`:[^9]

| `k` | `d = k + 1` | `char_k mod p` | unit group of `R` | `ord(x)` | factored |
|---|---|---|---|---|---|
| 1 | 2 | irreducible | `F_{p²}^*` | `4,000,000,024` | `2³ · 500,000,003` |
| 2 | 3 | `(x − 2)(x² − x + 2)` | `F_p^* × F_{p²}^*` | `500,000,007,000,000,024` | `2³ · 3² · 7 · 109² · 167 · 500,000,003` |
| 3 | 4 | irreducible | `F_{p⁴}^*` | `800,000,016,000,000,107,200,000,240` | `2⁴ · 5 · 58,699,937 · 340,715,873 · 500,000,003` |

The orders have 32, 59 and 90 bits. In every row the largest prime factor is `500,000,003 = (p − 1)/2`, about `2^28.9`, which divides every `p^d − 1`. Generic discrete-logarithm attacks cost about the square root of the largest prime factor of the order, so that prime, not the size of the order, is what round two attacks and sizes.

## 8. What Seminar 2 and round two take up

Three facts from this page are the starting points of the attacks:

1. `char_2 = (x − 2)(x² − x + 2)` over the integers, and the two factors are coprime mod every odd prime, so the CRT splits `R` at every odd prime (section 7). Attack 1 of [[castle-cryptography](pages/castle-cryptography.md)] splits the discrete logarithm along this factorization, and Attack 3 of round two recovers the private key `373309869` from `p`, `Q` and `A`.
2. `ord(x)` factors into small primes and `500,000,003` (section 7). Pohlig-Hellman reduces the discrete logarithm to these primes; Attack 4 of round two applies it even when `Q` is irreducible.
3. `P(k, ·)` satisfies a linear recurrence (section 1), so any leaked run of `2(k + 1)` terms, twice the window of section 5, determines `Q` by Berlekamp-Massey: Attack 2 of [[castle-cryptography](pages/castle-cryptography.md)].

## Appearances in Sources

- [[oeis-mining-pe502](pages/oeis-mining-pe502.md)] - the families `P(k, ·)` and their characteristic polynomials, used as the moduli.
- [[calugareanu-hamburg-exercises-basic-ring-theory](pages/calugareanu-hamburg-exercises-basic-ring-theory.md)] - the Chinese Remainder Theorem for pairwise comaximal ideals.

## Related Concepts

- [[castle-cryptography](pages/castle-cryptography.md)] - the series: Seminar 1 (this page), the two attacks of Seminar 2, with the CRT split of `R` at `p = 101` worked out in Attack 1, and the fixes of Seminar 3.
- [[castle-cryptography-round-two](pages/castle-cryptography-round-two.md)] - the second round: ElGamal and a signature, the private key recovered by Pohlig-Hellman, and both round-one fixes broken.
- [[castle-cryptography-number-theory](pages/castle-cryptography-number-theory.md)] - the terms characteristic polynomial, irreducible polynomial and discrete logarithm, explained from the `castle_dh` code.
- [[signed-tower-count](pages/signed-tower-count.md)] - `P(k, L)`, `char_k`, its factors for even `k`, and the update of `num_k` and `den_k`, of determinant `−1`.
- [[finite-fields](pages/finite-fields.md)] - `F_p`, `F_{p^d}` and their cyclic unit groups, the factors of the CRT split.
- [[mod-p-observatory](pages/mod-p-observatory.md)] - the periods of `P(k, ·)` and of the castle counts mod `p`, which divide the lcm of the orders of the roots.
- [[kitamasa](pages/kitamasa.md)] - `x^a mod Q` by binary exponentiation, the fast step of the castle count and the one-way map here.
- [[recurrence-discovery](pages/recurrence-discovery.md)] - the recurrence orders of `P(k, ·)` found by Berlekamp-Massey.
- [[eigenvalue-continued-fractions](pages/eigenvalue-continued-fractions.md)] - the roots of `char_k`, whose orders mod `p` section 2 takes the lcm of.
- [[castle-snippets-cryptography](pages/castle-snippets-cryptography.md)] - `castle_dh` and the `mulmod` and `powmod` helpers.
- [[new-sequence-fw3](pages/new-sequence-fw3.md)] - `A^e(w, 3)`, whose characteristic polynomial contains `char_2 = (x − 2)(x² − x + 2)`.
- [[castle-ring-invariant-factors](pages/castle-ring-invariant-factors.md)] - the unit group `R^*` as a product of cyclic groups, `R^* ≅ ∏ Z/(p^{d_i} − 1)` when `Q` is squarefree mod `p`, and the period of `P(k, ·)` as the order of `x`.
- [[chinese-remainder-theorem](pages/chinese-remainder-theorem.md)] - the theorem behind the unit group of section 7.
- [[idempotent-decomposition](pages/idempotent-decomposition.md)] - the CRT split by explicit idempotents of `R`, `2^r` of them for `r` distinct factors of `Q`.

## Footnotes

[^1]: Verified by execution (Python 3.11, 2026-10-16): `P(2, L)` for `L ≤ 7` by summing `(−1)^{blocks}` over all towers of height at most 2, and the recurrence for `3 ≤ L ≤ 7`.
[^2]: Verified by execution (Python 3.11, 2026-10-16) at `p = 10⁹ + 7`, `Q = [−4, 4, −3, 1]`: `mulmod([1, 1, 0], [2, 1, 0], Q, p) = [2, 3, 1]` and `mulmod([2, 3, 1], [0, 1, 0], Q, p) = [4, 1000000005, 6]`, with `1000000005 = −2 mod p`.
[^3]: Verified by execution (Python 3.11, 2026-10-16) at `p = 10⁹ + 7`, `Q = char_2`, counting the squarings and multiplications in the `powmod` loop for each `a`; `powmod(x, 12345) = [24371334, 336255992, 769290382]`, and the search over `x, x², …` reaches it after `12345` multiplications.
[^4]: Verified by execution (Python 3.11, 2026-10-16) at `p = 10⁹ + 7`, `Q = char_2`, `a = 373309869`, `b = 566180101`: the values of `A`, `B` and the shared secret shown, and `powmod(B, a) = powmod(A, b)`; the same numbers as `castle_dh` on [[castle-snippets-cryptography](pages/castle-snippets-cryptography.md)].
[^5]: Verified by execution (Python 3.11 with SymPy, 2026-10-25): `det H_k = (−1)^{k(k+1)/2} 2^{k²}` for `k ≤ 7`, with `P(k, 0), …, P(k, 2k)` from the signed transfer matrix; at `p = 10⁹ + 7`, `Q = char_2`, the windows `ℓ(A), ℓ(xA), ℓ(x²A)` of Alice's key and of the shared secret agree with `P(2, n), P(2, n + 1), P(2, n + 2) mod p` for `n = a` and `n = ab`, computed independently by powers of the signed transfer matrix, which also gives Bob's window; `H_2^{−1}` applied to Alice's window returns `A = [704821174, 848698009, 235195321]`.
[^6]: Verified by execution (Python 3.11 with SymPy, 2026-10-16): the terms mod 101; the first return of `(1, 1, 3)` at `L = 3400`; `char_2 mod 101 = (x − 2)(x² − x + 2)`; `(−7)^{50} ≡ −1 mod 101`; the order of `2` in `F_101^*` is `100`, and the order of `x` in `F_101[x]/(x² − x + 2)` is `3400`, with `101² − 1 = 10200 = 2³ · 3 · 5² · 17`.
[^7]: Verified by execution (Python 3.11 with SymPy, 2026-10-25): `det M = −1`; for `k ≤ 8`, `deg num_k ≤ k`, `deg den_k = k + 1`, `den_k(0) = 1` and `gcd(num_k, den_k) = 1` over the rationals; for `k ≤ 7`, `|Res(num_k, den_k)| = 2^{k²}`, and `num_k`, `den_k` follow the three-term update `u_{k+1} = u_{k−1} − 2x·u_k` of [[signed-tower-count](pages/signed-tower-count.md)].
[^8]: [[calugareanu-hamburg-exercises-basic-ring-theory](pages/calugareanu-hamburg-exercises-basic-ring-theory.md)] Ex. 17.20 p.76; solution p.193 [synthesis] - for pairwise comaximal ideals `I_1, …, I_n`, `R/∩I_i → ∏ R/I_i` is an isomorphism; in `F_p[x]`, `(f)` and `(g)` are comaximal exactly when `gcd(f, g) = 1`.
[^9]: Verified by execution (Python 3.11 with SymPy, 2026-10-16) at `p = 10⁹ + 7`: `char_1` and `char_3` are irreducible mod `p` and `char_2 = (x − 2)(x² − x + 2)`; the orders of `x` by removing prime factors from the exponent of the unit group, with the factorizations shown; `log₂` of the orders 31.9, 58.8, 89.4.
