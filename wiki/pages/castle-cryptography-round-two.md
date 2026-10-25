---
title: Castle cryptography, round two - break the fixes, size the keys
category: Analyses
summary: The second round of the build / red-team / blue-team series on the castle cryptosystem. BUILD - ElGamal and a Schnorr-style signature on the map x^a; on char_1 the subgroup of prime order (p − 1)/2 lies in the scalars (x^8 = 16, since (1 + i)^8 = 16), so the build uses char_3 with the prime q = 340715873 dividing p^2 + 1. RED TEAM - (Attack 3) Pohlig-Hellman with baby-step giant-step recovers the castle_dh private key 373309869 from p, Q and the public key; (Attack 4) an irreducible Q does not help, since p^d − 1 = ∏_{e | d} Φ_e(p) factors for every p and the largest prime factor at p = 10^9 + 7 is 500000003 for char_1 and char_3; (Attack 5) a polynomial filter of degree e on a d-stage castle register has linear complexity at most C(d + e − 1, e) in each degree, measured 10, 14, 20 at d = 4 and 21, 27, 56 at d = 6, and Berlekamp-Massey recovers it from 2L terms. BLUE TEAM - Φ_d(p) must carry a 256-bit prime (p of 128 bits at d = 4 or 6, the XTR and torus design), the linear complexity must be pushed to about 2^40 or beyond (a 64-stage register with a degree-16 filter reaches 2^54.6), and the index-calculus cost L_q[1/3, (64/9)^{1/3}] reaches 2^128 near q = p^d of 2537 bits.
tags: [analysis, seminar, cryptography, cryptanalysis, red-team, blue-team, pohlig-hellman, baby-step-giant-step, berlekamp-massey, linear-complexity, elgamal, schnorr, signature, finite-field, cyclotomic, index-calculus, key-size, castle]
sources: [granger-vercauteren-2005-dlp-algebraic-tori]
created: 2026-09-18
updated: 2026-10-25
---

# Castle cryptography, round two

[[castle-cryptography](pages/castle-cryptography.md)] runs the series once, with Seminar 1 in full on [[castle-cryptography-ring](pages/castle-cryptography-ring.md)]: it builds a castle Diffie-Hellman exchange, attacks it twice (Attack 1: the modulus factors; Attack 2: the output is a linear recurrence), and fixes it twice (Fix 1: an irreducible `char_k` with odd `k`; Fix 2: a nonlinear filter on the output). This page runs the series a second time: Attacks 3 to 5 break the round-one fixes, and Fixes 4 to 6 size the quantities the attacks depend on. The programs are `castle_dlp`, `bm_modp` and `castle_schnorr` on [[castle-snippets-cryptography](pages/castle-snippets-cryptography.md)].

Notation: `p = 10⁹ + 7`, `R = F_p[x]/(Q)` with `Q = char_k mod p`, the generator is `x`, and `char_1 = x² − 2x + 2`, `char_2 = x³ − 3x² + 4x − 4`, `char_3 = x⁴ − 4x³ + 8x² − 8x + 8` ([[signed-tower-count](pages/signed-tower-count.md)]). The public parameters are `(p, Q)`, a private key is an exponent, and the public key is `x^a mod Q`.

---

# Build, round two - ElGamal and a signature on the map `x^a`

Round one stopped at the shared secret. ElGamal encryption and a signature use the same map:

- **ElGamal.** The public key is `A = g^a`. A ring element `m` is encrypted as `(g^k, m · A^k)` and decrypted by computing `(g^k)^a` and dividing by it. In a subgroup of prime order `q`, the inverse of `s` is `s^{q−1}`.
- **Schnorr-style signature.** Choose `k`, publish `e = H(g^k, msg)` and `s = k + a·e mod q`; verify by checking that `H(g^s · A^{−e}, msg) = e`.

Both need a subgroup `⟨g⟩` of prime order `q`.

**On `char_1`, degree 2.** Since `p ≡ 3 (mod 4)`, `−1` is not a square mod `p` (Euler's criterion), so `char_1`, with discriminant `−4`, is irreducible and `R = F_{p²}`. The order of `x` is `8 · 500000003`, so the choice is `q = 500000003` and `g = x⁸`. But `x⁸ = 16` in `R`: the roots of `char_1` are `1 ± i`, and `(1 + i)⁸ = 16`. So the subgroup of order `q` lies in `F_p ⊂ F_{p²}`, every public key `g^a = 16^a` is a scalar, and the ring contributes nothing beyond `F_p`.[^1]

**On `char_3`, degree 4.** `p⁴ − 1 = (p − 1)(p + 1)(p² + 1)`, and `p² + 1 = 2 · 5² · 58699937 · 340715873`. The primes `58699937` and `340715873` do not divide `p² − 1`, the order of the unit group of the largest proper subfield `F_{p²}`, since `gcd(p² + 1, p² − 1) = 2`. With `q = 340715873` and `g = r^{(p⁴ − 1)/q}` for a random `r ∈ R`, the generator has all four coefficients nonzero, ElGamal decrypts the message `[1, 1, 3, 9]` (the first four terms of `P(2, ·)`), and the signature verifies on the signed message and fails on a changed one.[^1]

---

# Red team, round two - the fixes fall

## Attack 3 - recover Alice's private key

Round one used the Chinese Remainder Theorem (CRT) split of `R` to explain why the discrete logarithm splits ([[chinese-remainder-theorem](pages/chinese-remainder-theorem.md)]); Attack 3 carries it out. Take the published `castle_dh` values: `Q = char_2` and Alice's public key `A = x^a = [704821174, 848698009, 235195321]`. Factor `Q mod p = (x − 2)(x² − x + 2)`, reduce `A` modulo each factor, solve a discrete logarithm in each piece, and combine the two by the CRT:[^2]

| piece | where it lies | order of `x` there | logarithm |
|---|---|---|---|
| `x − 2` | `F_p^*`, with `x ↦ 2` | `500000003 = (p − 1)/2`, prime | `373309869` |
| `x² − x + 2` | `F_{p²}^*` | `2³·3²·7·109²·167·500000003` | `373309869` |

Each piece is solved by Pohlig-Hellman, which reduces a discrete logarithm in a group of order `n` to discrete logarithms in groups of prime order `q` for each prime power `q^e ∥ n`, with baby-step giant-step (BSGS) for each prime: a table of `⌈√q⌉` powers and as many lookups. The largest prime is `500000003 ≈ 2^28.9`, so the largest table has `22,361` entries. The private key `a = 373309869` is recovered from `p`, `Q` and `A`.

The smallest piece is the factor `x − 2`, which gives an ordinary discrete logarithm mod `p`:

```python
from math import isqrt
def bsgs_modp(g, h, n, p):           # solve g^x = h (mod p), ord(g) = n
    m = isqrt(n) + 1
    tbl = {}; e = 1
    for j in range(m): tbl.setdefault(e, j); e = e*g % p        # baby steps g^0..g^{m-1}
    gs = pow(g, (n - m) % n, p)                                # g^{-m}
    for i in range(m):                                         # giant steps h*g^{-im}
        if h in tbl: return i*m + tbl[h]
        h = h*gs % p

p  = 10**9 + 7
A  = [704821174, 848698009, 235195321]   # Alice's public key x^a mod char_2
A2 = (A[0] + 2*A[1] + 4*A[2]) % p        # project onto (x - 2): substitute x = 2
bsgs_modp(2, A2, 500000003, p)           # 2^a = A2 (mod p), ord(2) = 500000003
```

```
>>> A2
342998455
>>> bsgs_modp(2, A2, 500000003, p)
373309869
```

This piece determines `a` modulo `500000003`, and since `a < 500000003` it is the key.[^3]

## Attack 4 - an irreducible `Q` does not help

Round one's Fix 1 used an odd-`k` characteristic polynomial, irreducible over the rationals, so that `R` is one field `F_{p^d}` when `Q` stays irreducible mod `p`. That removes the split of the ring but not the split of the group, because the order of the group factors whether or not `Q` does:

```
p^d − 1  =  ∏_{e | d} Φ_e(p)          (Φ_e the e-th cyclotomic polynomial)
p² − 1   =  (p − 1)(p + 1)
p⁴ − 1   =  (p − 1)(p + 1)(p² + 1)
```

The factorization holds for every `p`, and Pohlig-Hellman runs over the prime factors of the order. Since `φ(e) ≤ φ(d)` for `e | d`, the largest factor `Φ_e(p)` is `Φ_d(p) ≈ p^{φ(d)}`, so the largest prime factor of `p^d − 1` is at most about `p^{φ(d)}`. At `p = 10⁹ + 7` all of these are small enough for BSGS:[^4]

| `Q` | irreducible mod `p` | `ord(x)` | largest prime factor | private key |
|---|---|---|---|---|
| `char_1`, degree 2 | yes | `2³ · 500000003` | `500000003 ≈ 2^28.9` | recovered |
| `char_3`, degree 4 | yes | `2⁴ · 5 · 58699937 · 340715873 · 500000003` | `500000003 ≈ 2^28.9` | recovered |
| the Schnorr subgroup on `char_3` | yes | `q = 340715873 ≈ 2^28.3` | `q` | recovered by plain BSGS |

The factors depend only on `p`:

```python
import sympy as sp
sp.factorint(10**9 + 8)          # p + 1
sp.factorint((10**9 + 7)**2 + 1) # p^2 + 1
```

```
>>> sp.factorint(10**9 + 8)
{2: 3, 3: 2, 7: 1, 109: 2, 167: 1}
>>> sp.factorint((10**9 + 7)**2 + 1)
{2: 1, 5: 2, 340715873: 1, 58699937: 1}
```

The subgroup prime of the build is `340715873`, a factor of `p² + 1`, and a BSGS table for it has `18,459` entries. The same private key `373309869` is recovered under `char_2`, `char_1` and `char_3`.[^5]

## Attack 5 - a nonlinear filter does not help either

Round one's Fix 2 published a polynomial function of consecutive terms instead of the terms, so that Berlekamp-Massey would not find a short recurrence. The attack is linearization. If `s_n = Σ_i c_i λ_iⁿ` satisfies a recurrence with characteristic polynomial `Q` of degree `d`, with roots `λ_i`, then a product of `e` shifted terms is a linear combination of the powers `(λ_{i₁} ⋯ λ_{i_e})ⁿ`, so it satisfies a linear recurrence whose characteristic roots are among the `C(d + e − 1, e)` products of `e` roots. A filter that is a polynomial of degree `e` therefore has linear complexity, the order of its shortest linear recurrence, at most `Σ_{j ≤ e} C(d + j − 1, j)` (at most `C(d + e − 1, e)` if every term has degree `e`), and Berlekamp-Massey over `F_p` recovers that recurrence from `2L` terms. On the castle registers `P(k, ·) mod p`, `d = k + 1`:[^6]

| filter | `d = 3` (`char_2`) | `d = 4` (`char_3`) | `d = 6` (`char_5`) | bound |
|---|---|---|---|---|
| `s_n · s_{n+1}` | 6 | 10 | 21 | `C(d+1, 2)` |
| `s_n²` | 6 | 10 | 21 | `C(d+1, 2)` |
| `s_n · s_{n+1} + s_{n+2}` | 8 | 14 | 27 | `C(d+1, 2) + d` |
| `s_n · s_{n+1} · s_{n+2}` | 9 | 20 | 56 | `C(d+2, 3)` |

The bounds are reached at `d = 4` and `d = 6`. At `d = 3` both shortfalls come from `α + ᾱ = 1` and `α·ᾱ = 2` for the roots `α, ᾱ` of `x² − x + 2`: for `s_n s_{n+1} + s_{n+2}` the product `αᾱ = 2` equals the third root, so one root is counted twice, and for `s_n s_{n+1} s_{n+2}` the ten products are distinct but the coefficient of `4 = 2αᾱ` vanishes ([[castle-ring-invariant-factors](pages/castle-ring-invariant-factors.md)], section 5). The characteristic polynomial of `s_n s_{n+1}` for `char_2` is `∏_{i ≤ j}(x − λ_iλ_j) = x⁶ − 5x⁵ + 8x⁴ − 12x³ − 16x² − 64x + 256`, and Berlekamp-Massey mod `p` returns these coefficients. In every case the recovered recurrence predicts every later term, and `2L` terms suffice.

A four-stage register has linear complexity 4, and the product of two adjacent terms has linear complexity `10 = C(5, 2)`:

```python
def bm(s, p):                        # Berlekamp-Massey: linear complexity of s mod p
    C, B, L, m, b = [1], [1], 0, 1, 1
    for n in range(len(s)):
        d = (s[n] + sum(C[i]*s[n-i] for i in range(1, L+1))) % p
        if d == 0: m += 1; continue
        T = C[:]; coef = d * pow(b, -1, p) % p
        C = C + [0]*(len(B)+m-len(C))
        for i in range(len(B)): C[i+m] = (C[i+m] - coef*B[i]) % p
        if 2*L <= n: L, B, b, m = n+1-L, T, d, 1
        else: m += 1
    return L

def lfsr(Q, init, n, p):             # run the castle recurrence from its initial terms
    s = list(init); d = len(Q)-1
    while len(s) < n: s.append(sum(-Q[j]*s[-d+j] for j in range(d)) % p)
    return s

p  = 10**9 + 7
Q3 = [8, -8 % p, 8, -4 % p, 1]       # char_3 = x^4 - 4x^3 + 8x^2 - 8x + 8
s  = lfsr(Q3, [1, 0, -4 % p, -16 % p], 300, p)   # P(3, L) mod p: a 4-stage register
z  = [(s[i]*s[i+1]) % p for i in range(299)]     # the filtered output s_n * s_{n+1}
```

```
>>> bm(s, p), bm(z, p)
(4, 10)
```

Berlekamp-Massey recovers the filtered stream from 20 terms.[^7] The filter raises the linear complexity from `d` to at most `C(d + e − 1, e)` in each degree, and a small register with a low-degree filter is still recovered.

---

# Blue team, round two - size the parameters

The three attacks depend on three quantities: the largest prime factor of the order of the group, the linear complexity of the output, and the size of the field against index calculus. Fixes 4 to 6 size each.

## Fix 4 - choose `p` so that `Φ_d(p)` has a large prime factor

Generic discrete-logarithm attacks, BSGS and Pollard rho, cost about the square root of the largest prime factor of the order of the group, so `2¹²⁸` security needs a prime of 256 bits dividing `p^d − 1`. It must divide `Φ_d(p)`, of size about `p^{φ(d)}`: a prime dividing a smaller factor `Φ_e(p)` with `e < d` divides the order of the unit group of the subfield `F_{p^e}`, and the norm map carries the problem into that subfield, as `x⁸ = 16` carried the `char_1` subgroup into `F_p`. So:

| `d` | `φ(d)` | `p` needed for `Φ_d(p)` to have 256 bits |
|---|---|---|
| 2 | 1 | `p ≳ 2²⁵⁶` |
| 4 | 2 | `p ≳ 2¹²⁸` |
| 6 | 2 | `p ≳ 2¹²⁸` |
| 7 | 6 | `p ≳ 2⁴³` |

and `p` must then be chosen so that `Φ_d(p)` has such a prime factor. This is the design of XTR and torus-based cryptography, which work in the subgroup of order `Φ_6(p) = p² − p + 1` of `F_{p⁶}^*` ([[granger-vercauteren-2005-dlp-algebraic-tori](pages/granger-vercauteren-2005-dlp-algebraic-tori.md)]). The castle has a degree-6 modulus, `char_5`, and round three builds a castle torus on it ([[castle-cryptography-round-three](pages/castle-cryptography-round-three.md)]).

## Fix 5 - size the register and the filter

Berlekamp-Massey needs `2L` terms and about `L²` operations for linear complexity `L`, so `L ≈ 2⁴⁰` already costs about `2⁸⁰` operations. The bound `Σ_{j ≤ e} C(d + j − 1, j) = C(d + e, e) − 1` gives the linear complexity a register and filter can reach:[^8]

| register stages `d` | filter degree `e` | linear complexity at most |
|---|---|---|
| 6 | 6 | `923 ≈ 2^9.9` |
| 32 | 8 | `76,904,684 ≈ 2^26.2` |
| 64 | 16 | `≈ 2^54.6` |
| 128 | 16 | `≈ 2^69.2` |

A castle register of `d` stages runs `char_{d−1}`, so a 64-stage register is `char_63`, the signed tower count `P(63, L)` for castles of height 64, with a filter of degree 16.

## Fix 6 - the index-calculus ceiling

With Fixes 4 and 5 in place, discrete logarithms in `F_{p^d}` still face index calculus and the number field sieve, of heuristic cost `L_q[1/3, (64/9)^{1/3}] = exp((64/9)^{1/3} (ln q)^{1/3} (ln ln q)^{2/3})` for `q = p^d`, with the `o(1)` term dropped. At `p = 10⁹ + 7`:[^8]

| `d` | `q = p^d` | Pollard rho on the largest prime factor | `L_q[1/3]` |
|---|---|---|---|
| 2 | `2^59.8` | `2^14.4` | `2^23.1` |
| 4 | `2^119.6` | `2^14.4` | `2^32.6` |
| 6 | `2^179.4` | `2^23.6` | `2^39.5` |
| 7 | `2^209.3` | `2^34.3` | `2^42.5` |

`L_q[1/3]` reaches `2¹²⁸` at `q ≈ 2²⁵³⁷`: `p ≈ 2¹²⁶⁹` at `d = 2`, `2⁶³⁴` at `d = 4` and `2⁴²³` at `d = 6`, close to the 3072-bit finite fields recommended for 128-bit security ([[castle-cryptography-round-three](pages/castle-cryptography-round-three.md)]). So at `p = 10⁹ + 7` no choice of `Q` makes the castle discrete logarithm hard; 128-bit security needs `p` of hundreds of bits, and the system is then ordinary finite-field cryptography. Round three replaces the constant `(64/9)^{1/3}` by that of the extended tower number field sieve, which applies at composite `d`.

---

# The method

The two rounds give a procedure for judging a new cryptosystem:

1. **Name the hard problem exactly:** the group, its order and the map. "Discrete logarithm in `F_p[x]/(Q)`" is incomplete until `|⟨g⟩|` is written down.
2. **Find where the structure splits:** does the modulus factor (the CRT on the ring), does the order of the group factor (Pohlig-Hellman, always possible for `p^d − 1` by the cyclotomic factorization), does a subgroup lie in a subfield (the norm map, as in `x⁸ = 16`)?
3. **Check whether the output is linear or a low-degree function of something linear:** Berlekamp-Massey for the first, linearization with the bound `C(d + e − 1, e)` for the second.
4. **Size each attack separately:** the square root of the largest prime factor, the linear complexity, and `L_q[1/3]`.

## Appearances in Sources

- [[granger-vercauteren-2005-dlp-algebraic-tori](pages/granger-vercauteren-2005-dlp-algebraic-tori.md)] - the torus of order `Φ_n(p)` as the part of `F_{p^n}^×` that no proper subfield reaches (Fix 4), and index calculus on tori, which does not affect tori over a prime field.

## Related Concepts

- [[castle-cryptography](pages/castle-cryptography.md)] - round one: the build, Attacks 1 and 2, and Fixes 1 to 3.
- [[castle-cryptography-round-three](pages/castle-cryptography-round-three.md)] - round three: Fix 4 built as a castle torus on `char_5` (512-bit `p`, prime `p² − p + 1`, 3-to-1 compression by the trace), and the `L_q[1/3]` table of Fix 6 updated for the extended tower number field sieve.
- [[castle-cryptography-ring](pages/castle-cryptography-ring.md)] - Seminar 1, whose table of element orders (section 5) Attack 3 factors.
- [[castle-cryptography-number-theory](pages/castle-cryptography-number-theory.md)] - the terms characteristic polynomial, irreducible polynomial and discrete logarithm, and why an irreducible `Q` still leaves `p^d − 1` factored.
- [[kitamasa](pages/kitamasa.md)] - the exponentiation `x^a mod Q` used by ElGamal, the signature and every attack.
- [[berlekamp-massey](pages/berlekamp-massey.md)] - the algorithm that recovers a linear recurrence, run here over `F_p` against filters.
- [[finite-fields](pages/finite-fields.md)] - `F_{p^d}^*` is cyclic of order `p^d − 1`; the cyclotomic factorization and the subfields that Attack 4 and Fix 4 use.
- [[mod-p-observatory](pages/mod-p-observatory.md)] - the periods of `P(k, ·) mod p` and the orders of the roots of `char_k`.
- [[tower-parity-sectors](pages/tower-parity-sectors.md)] - the factorization of `char_k` for even `k`, which Attack 3 uses for `char_2`.
- [[eigenvalue-continued-fractions](pages/eigenvalue-continued-fractions.md)] - the roots `1 ± i` of `char_1`, whose eighth power is `16`.
- [[castle-snippets-cryptography](pages/castle-snippets-cryptography.md)] - `castle_dlp`, `bm_modp` and `castle_schnorr`, with their outputs.
- [[castle-compression](pages/castle-compression.md)] - linear complexity as a description length.
- [[new-sequence-fw3](pages/new-sequence-fw3.md)] - `A^e(w, 3)`, whose recurrence has order 6 because the root 2 of `char_2` is also the root of the term `2^w`.
- [[castle-ring-invariant-factors](pages/castle-ring-invariant-factors.md)] - the unit group `R^*` as a product of cyclic groups, Pohlig-Hellman through `Z/n ≅ ∏ Z/q^e`, and the two `d = 3` shortfalls of Attack 5 from `α + ᾱ = 1` and `α·ᾱ = 2`.
- [[oeis-mining-pe502](pages/oeis-mining-pe502.md)] - the families `P(k, ·)`, whose characteristic polynomials serve as the moduli and registers.

## Footnotes

[^1]: Verified by execution (Python 3.11 with SymPy, 2026-10-16). On `Q = char_1 mod p`: `ord(x) = 4000000024 = 2³ · 500000003` and `x⁸ = [16, 0]`. On `Q = char_3 mod p`, with the `castle_schnorr` code of [[castle-snippets-cryptography](pages/castle-snippets-cryptography.md)] (`random.seed(502)`): `g = [670690837, 335848460, 27104856, 290696543]`, the public key `[34518600, 853770003, 669598040, 563247297]`, decryption returns `[1, 1, 3, 9]`, and the signature `(129461214, 65798226)` verifies on `b"castle 502"` and fails on `b"castle 503"`, with `H` the SHA-256 hash of the representation mod `q`; `p² + 1 = 2 · 5² · 58699937 · 340715873`.
[^2]: Verified by execution (Python 3.11 with SymPy, 2026-10-16): `castle_dlp(A, Q2, p)` with `A = x^{373309869} mod char_2` returns `[373309869, 500000007000000024]`, the key and the modulus it is determined modulo; the order of `2` in `F_p^*` is `500000003`, and the order of `x` in `F_p[x]/(x² − x + 2)` is `500000007000000024 = 2³·3²·7·109²·167·500000003`.
[^3]: Verified by execution (Python 3.11, 2026-10-16): `A(2) = A[0] + 2A[1] + 4A[2] = 342998455 mod p`, and `bsgs_modp(2, 342998455, 500000003, p) = 373309869`; `⌈√500000003⌉ = 22,361`.
[^4]: Verified by execution (Python 3.11 with SymPy, 2026-10-16): `char_1` and `char_3` are irreducible mod `p`; `castle_dlp` recovers `373309869` from `x^{373309869} mod char_1` (`ord(x) = 4000000024`) and mod `char_3` (`ord(x) = 800000016000000107200000240 = 2⁴·5·58699937·340715873·500000003`); plain BSGS recovers the Schnorr private key in the subgroup of order `340715873`.
[^5]: Verified by execution (SymPy `factorint`, 2026-10-16): `p + 1 = 2³ · 3² · 7 · 109² · 167`, `p² + 1 = 2 · 5² · 58699937 · 340715873`, `p² − 1 = 2⁴ · 3² · 7 · 109² · 167 · 500000003`; `⌈√340715873⌉ = 18,459`.
[^6]: Verified by execution (Python 3.11 with SymPy, 2026-10-16): Berlekamp-Massey over `F_p` on `P(k, ·) mod p` returns linear complexity `k + 1` for `k = 2, 3, 5`, and on the four filters the values in the table (400 terms each); the recovered connection polynomials annihilate all later terms. `∏_{i ≤ j}(x − λ_iλ_j)` over the roots of `char_2` is `x⁶ − 5x⁵ + 8x⁴ − 12x³ − 16x² − 64x + 256`.
[^7]: Verified by execution (Python 3.11, 2026-10-16): `bm(P(3, ·) mod p, p) = 4` and `bm(s_n s_{n+1}, p) = 10`, and the first `20` terms give the same connection polynomial.
[^8]: Computed (Python 3.11 with SymPy, 2026-10-16): `C(d + e, e) − 1` gives `923`, `76904684`, `2^54.58`, `2^69.22`; at `p = 10⁹ + 7`, the largest prime factor of `p^d − 1` is `2^28.9` for `d = 2, 4`, `2^47.2` for `d = 3, 6` and `2^68.5` for `d = 7`, and `L_q[1/3, (64/9)^{1/3}]` is `2^23.1`, `2^28.3`, `2^32.6`, `2^39.5`, `2^42.5` for `d = 2, 3, 4, 6, 7`; it equals `2⁸⁰` at `q ≈ 2^850` and `2¹²⁸` at `q ≈ 2^2537`.
