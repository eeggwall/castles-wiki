---
title: Castle snippets - cryptography
category: Concepts
summary: Four tested Python snippets for the castle cryptosystem in R = F_p[x]/(char_k mod p) at p = 10^9 + 7. castle_dh is Diffie-Hellman with public parameters (p, Q), a private exponent and public key x^a mod Q; castle_dlp recovers the private key 373309869 by splitting Q, Pohlig-Hellman and baby-step giant-step, for char_2, char_1 and char_3; bm_modp is Berlekamp-Massey over F_p and measures the linear complexity 10 of s_n s_{n+1} on a 4-stage register; castle_schnorr is ElGamal and a Schnorr-style signature in the subgroup of order 340715873 of F_{p^4}.
tags: [concept, castle, python, snippets, cryptography, diffie-hellman, discrete-log, berlekamp-massey, schnorr, elgamal]
sources: [project-euler-502-representations]
created: 2026-09-19
updated: 2026-10-25
---

# Castle snippets - cryptography

The snippets of the cryptography series ([[castle-cryptography](pages/castle-cryptography.md)], [[castle-cryptography-ring](pages/castle-cryptography-ring.md)], [[castle-cryptography-round-two](pages/castle-cryptography-round-two.md)]), in the format of [[castle-snippets](pages/castle-snippets.md)]: each snippet with the output it prints.[^1]

### `castle_dh` → a working castle Diffie–Hellman

Key exchange in the ring `F_p[x]/(Q)`, with `Q = char_k mod p` ([[castle-cryptography](pages/castle-cryptography.md)]). The public parameters are `(p, Q)`, a private key is an exponent `a`, and the public key is `x^a mod Q`, computed by the exponentiation of [[kitamasa](pages/kitamasa.md)]. Standard library only.

```python
def one(Q): return [1] + [0]*(len(Q)-2)          # multiplicative identity in F_p[x]/(Q)
def gen(Q): return [0, 1] + [0]*(len(Q)-3)        # the generator polynomial x

def mulmod(A, B, Q, p):                       # multiply in F_p[x]/(Q), Q monic degree d
    r = [0] * (len(A) + len(B) - 1)
    for i, a in enumerate(A):
        for j, b in enumerate(B):
            r[i + j] = (r[i + j] + a * b) % p
    d = len(Q) - 1
    for i in range(len(r) - 1, d - 1, -1):    # reduce mod Q = the recurrence rewrite
        c = r[i]
        for j in range(d + 1):
            r[i - d + j] = (r[i - d + j] - c * Q[j]) % p
    return (r[:d] + [0] * d)[:d]

def powmod(base, e, Q, p):                     # x^e mod Q by binary exponentiation (Kitamasa)
    res = [1] + [0] * (len(Q) - 2)
    base = (base[:len(Q)-1] + [0]*len(Q))[:len(Q)-1]
    while e:
        if e & 1: res = mulmod(res, base, Q, p)
        base = mulmod(base, base, Q, p)
        e >>= 1
    return res

def castle_dh(Q, p, a, b):                     # returns (Alice_pub, Bob_pub, shared_secret)
    g = [0, 1] + [0] * (len(Q) - 3)            # the generator polynomial x
    A, B = powmod(g, a, Q, p), powmod(g, b, Q, p)
    return A, B, powmod(B, a, Q, p)            # x^{ab} mod Q; == powmod(A, b, Q, p)
```

```
>>> p = 10**9 + 7
>>> Q = [-4 % p, 4, -3 % p, 1]                 # char_2 = x^3 - 3x^2 + 4x - 4, the public modulus
>>> A, B, s = castle_dh(Q, p, 373309869, 566180101)
>>> s == powmod(A, 566180101, Q, p)            # both parties get the same shared secret
True
>>> s
[395423824, 86931747, 647893869]
```

Meaning: both parties obtain the shared secret `x^{ab} mod Q`. The system is not secure at this size: `Q = (x − 2)(x² − x + 2)` factors, so the discrete logarithm splits (Attack 1), and Berlekamp-Massey recovers `Q` from `2 deg Q` terms of the sequence (Attack 2), both on [[castle-cryptography](pages/castle-cryptography.md)] ([[berlekamp-massey](pages/berlekamp-massey.md)]).


### `castle_dlp(A, Q, p)` → recover the private key from a castle public key

Attack 3 of [[castle-cryptography-round-two](pages/castle-cryptography-round-two.md)]: factor `Q mod p`, reduce `A` modulo each factor, solve the discrete logarithm of each piece by Pohlig-Hellman over the factored order of `x`, with baby-step giant-step for each prime, and combine the pieces by the Chinese Remainder Theorem (CRT). Uses `mulmod`, `powmod`, `one` and `gen` from `castle_dh`. Requires SymPy.

```python
from math import isqrt
import sympy as sp
from sympy.ntheory.modular import crt

def bsgs(g, h, n, Q, p):                       # solve g^x = h in F_p[x]/(Q), ord(g) | n
    m = isqrt(n) + 1; tbl = {}; cur = one(Q)
    for j in range(m):
        tbl.setdefault(tuple(cur), j); cur = mulmod(cur, g, Q, p)
    step, cur = powmod(g, (n - m) % n, Q, p), h  # g^{-m}
    for i in range(m):
        if tuple(cur) in tbl: return (i*m + tbl[tuple(cur)]) % n
        cur = mulmod(cur, step, Q, p)

def pohlig_hellman(g, h, n, Q, p):             # log_g h, ord(g) = n exactly; cost ~ sqrt(largest prime | n)
    res, mod = 0, 1
    for q, e in sp.factorint(n).items():
        qe = q**e; gq, hq = powmod(g, n // qe, Q, p), powmod(h, n // qe, Q, p)
        x, gam = 0, powmod(gq, q**(e-1), Q, p)
        for i in range(e):
            hk = powmod(mulmod(hq, powmod(gq, (qe - x) % qe, Q, p), Q, p), q**(e-1-i), Q, p)
            x += bsgs(gam, hk, q, Q, p) * q**i
        res, mod = [int(v) for v in crt([mod, qe], [res, x])]
    return res

def elem_order(g, Q, p, N):                    # order of g given a multiple N (e.g. p^d - 1)
    o = N
    for q in sp.factorint(N):
        while o % q == 0 and powmod(g, o // q, Q, p) == one(Q): o //= q
    return o

def castle_dlp(A, Q, p):                       # recover a from A = x^a mod Q: split Q, solve each piece, CRT
    x = sp.Symbol('x'); logs = []
    for f, _ in sp.factor_list(sp.Poly(Q[::-1], x).as_expr(), modulus=p)[1]:
        Qf = [int(c) % p for c in sp.Poly(f, x).all_coeffs()[::-1]]; d = len(Qf) - 1
        if d == 1:                              # linear factor (x - r): the piece is F_p^*, x -> r
            r = (-Qf[0]) % p; Qf, g, h = [0, 1], [r], [sum(c * pow(r, i, p) for i, c in enumerate(A)) % p]
        else:
            g, h = gen(Qf), mulmod(A, one(Qf), Qf, p)
        n = elem_order(g, Qf, p, p**d - 1)
        logs.append((pohlig_hellman(g, h, n, Qf, p), n))
    return [int(v) for v in crt([n for _, n in logs], [a for a, _ in logs])]
```

```
>>> p = 10**9 + 7; Q2 = [-4 % p, 4, -3 % p, 1]              # char_2, the castle_dh modulus
>>> A = powmod(gen(Q2), 373309869, Q2, p); A                 # Alice's public key from castle_dh
[704821174, 848698009, 235195321]
>>> castle_dlp(A, Q2, p)   # Alice's private key, and the modulus it is known mod
[373309869, 500000007000000024]
>>> Q1 = [2, -2 % p, 1]                                      # char_1, irreducible mod p: still falls
>>> castle_dlp(powmod(gen(Q1), 373309869, Q1, p), Q1, p)
[373309869, 4000000024]
>>> sp.factorint(p**2 - 1)                                   # the group order factors even though Q does not
{2: 4, 3: 2, 7: 1, 109: 2, 167: 1, 500000003: 1}
>>> Q3 = [8, -8 % p, 8, -4 % p, 1]                           # char_3, degree 4, irreducible mod p
>>> castle_dlp(powmod(gen(Q3), 373309869, Q3, p), Q3, p)
[373309869, 800000016000000107200000240]
```

Meaning: the private key is recovered whether or not `Q` factors, because `p^d − 1 = ∏_{e | d} Φ_e(p)` factors for every `p` and its largest prime factor here is `500000003 ≈ 2^28.9`. An irreducible `Q` removes the CRT split of the ring, not the factorization of the order of the group ([[castle-cryptography-round-two](pages/castle-cryptography-round-two.md)], Attack 4).


### `bm_modp(s, p)` → Berlekamp–Massey over `F_p`, and the linearization attack

The linear complexity of a sequence mod `p`, the order of its shortest linear recurrence ([[berlekamp-massey](pages/berlekamp-massey.md)]), used to measure how much a polynomial filter on a castle register raises it ([[castle-cryptography-round-two](pages/castle-cryptography-round-two.md)], Attack 5). Standard library only.

```python
def bm_modp(s, p):                             # -> (connection poly low->high, C[0] = 1; linear complexity L)
    C, B, L, m, b = [1], [1], 0, 1, 1
    for n in range(len(s)):
        d = (s[n] + sum(C[i]*s[n-i] for i in range(1, L+1))) % p
        if d == 0: m += 1; continue
        T, coef = C[:], d * pow(b, -1, p) % p
        C = C + [0]*(len(B)+m-len(C))
        for i in range(len(B)): C[i+m] = (C[i+m] - coef*B[i]) % p
        if 2*L <= n: L, B, b, m = n+1-L, T, d, 1
        else: m += 1
    return C, L

def lfsr(Q, init, n, p):                       # run the castle recurrence with char poly Q from initial terms
    s = list(init); d = len(Q) - 1
    while len(s) < n: s.append(sum(-Q[j]*s[-d+j] for j in range(d)) % p)
    return s
```

```
>>> s = lfsr(Q3, [1, 0, -4 % p, -16 % p], 300, p)  # P(3, L) mod p: a 4-stage castle register
>>> bm_modp(s, p)[1]
4
>>> z = [s[i]*s[i+1] % p for i in range(299)]      # filtered output: product of adjacent terms
>>> C, L = bm_modp(z, p); L                        # = C(5, 2): products of pairs of roots
10
>>> all(sum(C[i]*z[n-i] for i in range(L+1)) % p == 0 for n in range(L, len(z)))   # the recovered recurrence predicts every later term
True
>>> bm_modp(z[:2*L], p) == (C, L)   # 2L terms suffice
True
>>> z3 = [s[i]*s[i+1]*s[i+2] % p for i in range(298)]
>>> bm_modp(z3, p)[1]   # degree-3 filter: C(6,3) = 20
20
```

Meaning: a product of `e` terms of a `d`-stage linear register satisfies a linear recurrence of order at most `C(d + e − 1, e)`, whose characteristic roots are among the products of `e` roots of `Q`, so Berlekamp-Massey recovers it from `2L` terms.


### `castle_schnorr` → ElGamal and a Schnorr-style signature on the `x^a` map

The build of round two ([[castle-cryptography-round-two](pages/castle-cryptography-round-two.md)]): encryption and signatures from the same `powmod` as `castle_dh`, in a subgroup of prime order of `F_p[x]/(char_3) ≅ F_{p⁴}`. The prime `q = 340715873` divides `p² + 1` and not `p² − 1`, so `⟨g⟩` lies in no proper subfield (on `char_1` the subgroup of order `(p − 1)/2` lies in `F_p`, since `x⁸ = 16`).

```python
import hashlib, random
Q, N = Q3, p**4 - 1                            # char_3 mod p is irreducible: the ring is F_{p^4}
q = 340715873                                  # a prime factor of p^2 + 1 -> a subgroup in the degree-4 part
random.seed(502)
while True:
    g = powmod([random.randrange(p) for _ in range(4)], N // q, Q, p)
    if g != one(Q): break
H = lambda *parts: int.from_bytes(hashlib.sha256(repr(parts).encode()).digest(), 'big') % q
def keygen():            a = random.randrange(1, q); return a, powmod(g, a, Q, p)
def enc(pub, m):         k = random.randrange(1, q); return powmod(g, k, Q, p), mulmod(m, powmod(pub, k, Q, p), Q, p)
def dec(a, c1, c2):      s = powmod(c1, a, Q, p); return mulmod(c2, powmod(s, q - 1, Q, p), Q, p)
def sign(a, msg):        k = random.randrange(1, q); e = H(powmod(g, k, Q, p), msg); return e, (k + a*e) % q
def verify(pub, msg, e, s): return H(mulmod(powmod(g, s, Q, p), powmod(pub, (q - e) % q, Q, p), Q, p), msg) == e
```

```
>>> a, pub = keygen(); g, pub
[670690837, 335848460, 27104856, 290696543] [34518600, 853770003, 669598040, 563247297]
>>> dec(a, *enc(pub, [1, 1, 3, 9]))
[1, 1, 3, 9]
>>> e, sg = sign(a, b'castle 502'); (e, sg), verify(pub, b'castle 502', e, sg), verify(pub, b'castle 503', e, sg)
(129461214, 65798226) True False
>>> bsgs(g, pub, q, Q, p) == a   # Attack 4: q has 29 bits, a table of 18,459 baby steps
True
```

Meaning: key exchange, encryption and signatures all come from one exponentiation, and the `bsgs` of `castle_dlp` recovers the signing key with a table of `⌈√q⌉ = 18,459` entries. The construction works; its parameters are far too small.


## Related Concepts

- [[castle-snippets](pages/castle-snippets.md)] - the enumeration and predicates hub.
- [[castle-cryptography](pages/castle-cryptography.md)] / [[castle-cryptography-ring](pages/castle-cryptography-ring.md)] / [[castle-cryptography-round-two](pages/castle-cryptography-round-two.md)] - the build, ring, and round-two seminar pages.
- [[kitamasa](pages/kitamasa.md)] - the fast-index exponentiation `powmod` implements.
- [[berlekamp-massey](pages/berlekamp-massey.md)] - the recovery attack `bm_modp` runs.
- [[signed-tower-count](pages/signed-tower-count.md)] - the `P(k, ·)` sequence the LFSR attack reconstructs.
- [[finite-fields](pages/finite-fields.md)] - the field structure of `F_p[x] / (Q)`.
- [[oeis-mining-pe502](pages/oeis-mining-pe502.md)] - the `P(k, ·)` characteristic polynomials used as moduli and registers.

## Footnotes

[^1]: Verified by execution (Python 3.11 with SymPy, 2026-10-16): every code block on the page run as printed, in order; each output shown is the printed output, including `castle_dlp` for `char_2`, `char_1` and `char_3`, `bm_modp` (4, 10, 20, and both checks `True`), and `castle_schnorr` with `random.seed(502)`.
