---
title: Castle ring by invariant factors
category: Analyses
summary: The unit group of `R = F_p[x]/(char_k)` written as a product of cyclic groups. When `char_k` is squarefree mod `p`, CRT gives `R^* ≅ ∏ F_{p^{d_i}}^* = ∏ Z/(p^{d_i} - 1)`, and everything the seminars do collapses to one picture: the mod-`p` period is `ord(x)` in that product; Kitamasa is exponentiation in it; Pohlig-Hellman is the fundamental theorem of finitely generated abelian groups run on `⟨x⟩`; security in `castle_dh` is set by the largest prime-power invariant factor of `⟨x⟩`. At a discriminant-zero prime `char_k` acquires a repeated factor `g^m` and the ring gains a `p`-group `1 + (g)/(g)^m` of order `p^{d·(m-1)}` beside the field factor - that is exactly the extra `p` the observatory measured (`per(char_2 mod 7) = 21 = 3·7`, the extra `7` being the size of the `p`-group). The two `d = 3` linear-complexity deficits on round-two are one line in this language: for `char_2` the norm relation `α·ᾱ = 2` identifies a pair-product with the linear factor's root (`8 = 6 + 3 − 1`), and the character `4 = 2·α·ᾱ` in `s_n·s_{n+1}·s_{n+2}` has coefficient `6·s_1 + 2·s_2 = 6 − 6 = 0` (`9 = 10 − 1`).
tags: [analysis, cryptography, ring, finite-field, unit-group, invariant-factors, structure-theorem, pohlig-hellman, kitamasa, discriminant, discriminant-zero, linear-complexity, castle]
sources: [oeis-mining-pe502, calugareanu-hamburg-exercises-basic-ring-theory]
created: 2026-09-21
updated: 2026-09-26
---

# Castle ring by invariant factors

The [[castle-cryptography-ring](pages/castle-cryptography-ring.md)] seminar builds arithmetic in `R = F_p[x]/(Q)` with `Q = char_k mod p`, and [[castle-cryptography-round-two](pages/castle-cryptography-round-two.md)] runs Pohlig-Hellman on `⟨x⟩ ⊂ R^*`. Both pages talk in terms of "factor `Q`, then reduce mod each factor." This page names the same object as an **abelian group written in invariant factors**, and reads five separate seminar facts as one identity.

The one identity: for `Q = ∏_i g_i^{m_i}` with `g_i` distinct irreducibles of degree `d_i` over `F_p`, [[finite-fields](pages/finite-fields.md)] + CRT ([[chinese-remainder-theorem](pages/chinese-remainder-theorem.md)], for the pairwise comaximal ideals `(g_i^{m_i})`)[^8] give

```
R^*  =  ∏_i  ( F_{p^{d_i}}^*  ×  U_i )         where   U_i = (1 + (g_i))/(g_i)^{m_i}
     ≅  ∏_i  ( Z/(p^{d_i} - 1)  ×  Z/p^{d_i(m_i-1)} · (stuff) )
```

with `U_i` a `p`-group of order `p^{d_i(m_i-1)}` (trivial when `m_i = 1`). Everything below is a reading of a specific `(char_k, p)` through this decomposition.

## 1. Squarefree `Q`: `R^* ≅ ∏ Z/(p^{d_i} - 1)`

When `Q` is squarefree mod `p` every `m_i = 1`, so each `U_i` is trivial, each factor is a *field* `F_{p^{d_i}}`, and its unit group is cyclic. The whole thing is a product of cyclic groups of order `p^{d_i} - 1`. Its **invariant factors** are the Smith normal form of the diagonal integer matrix `diag(p^{d_i} - 1)`; the largest one (the *exponent* of `R^*`) is the `lcm`.

The seminar's `(char_k, p)` cases in this language:[^1]

| `k` | `p` | `Q = char_k mod p` (factors) | `R^*` as product | invariant factors | `ord(x) ∈ R^*` |
|---|---|---|---|---|---|
| 2 | 101 | `(x−2)(x²−x+2)` | `Z/100 × Z/10200` | `(100, 10200)` | `3400` |
| 1 | `10⁹+7` | `x²−2x+2` (irreducible) | `Z/(p²−1)` | `(p²−1)` | `2³·500000003 = 4·10⁹+24` |
| 2 | `10⁹+7` | `(x−2)(x²−x+2)` | `Z/(p−1) × Z/(p²−1)` | `(p−1, p²−1)` | `2³·3²·7·109²·167·500000003` |
| 3 | `10⁹+7` | `x⁴−4x³+8x²−8x+8` (irreducible) | `Z/(p⁴−1)` | `(p⁴−1)` | `2⁴·5·58699937·340715873·500000003` |

Two facts to read off:

- **The mod-`p` period is `ord(x)` in the product.** From [[mod-p-observatory](pages/mod-p-observatory.md)] `period = lcm of eigenvalue orders`; the eigenvalues are the projections of `x` into each `F_{p^{d_i}}^*`, and `ord(x)` in a product of cyclic groups is the `lcm` of the componentwise orders. Row 1: `lcm(100, 3400) = 3400`, the period observed at `p = 101`.
- **`ord(x)` need not be the exponent.** Row 1: exponent `= 10200`, `ord(x) = 3400`; the projection of `x` into the `F_{101²}^*` factor has order `3400 = (p²−1)/3`, one-third of the max. Row 3: exponent `= p²−1`, `ord(x)` is `(p²−1)/2` (because `ord(2 mod p) = (p−1)/2`, not `p−1`).

## 2. Kitamasa is exponentiation in `R^*`

[[kitamasa](pages/kitamasa.md)] computes `x^n mod Q` by binary squaring in `R = F_p[x]/(Q)`. When `x` is a unit (which it is whenever `Q(0) ≠ 0 mod p` - `char_k(0) = (−1)^{k−1}2^k` is nonzero mod every odd `p`), that computation lives in `R^*`. The `O(D² log n)` cost is `log n` squarings in the abelian group `R^*`. Read through this page, Kitamasa is *the* fast group exponentiation for the abelian group `∏ Z/(p^{d_i} - 1)` in which the castle recurrence sits.

## 3. Pohlig-Hellman is the structure theorem run on `⟨x⟩`

Round-two Attack 3 recovered Alice's key by factoring `ord(x)`, solving a DLP in each prime-power piece, and CRTing back ([[castle-cryptography-round-two](pages/castle-cryptography-round-two.md)]). In the invariant-factor language that is one sentence: apply the **fundamental theorem of finitely generated abelian groups** to `⟨x⟩ ⊆ R^*` - it splits as a direct product of cyclic groups of prime-power order, one per prime factor of `ord(x)` - and solve the DLP separately in each cyclic factor. Baby-step giant-step handles a cyclic factor of order `n` in `√n` work, so:

**Security of `castle_dh` = square root of the largest prime-power invariant factor of `⟨x⟩`.**

Row 2-4 of the table above all have the same largest prime-power invariant factor: `500000003 ≈ 2²⁹`. This is why the [[castle-cryptography-ring](pages/castle-cryptography-ring.md)] §5 caveat "the size of `ord(x)` sets the naive DLP work; the factorization decides the actual cost" and the round-two Attack 4 result "same private key `373309869`, three hardened moduli" say the *same thing*: at `p = 10⁹+7`, `500000003 = (p−1)/2` divides every `p^d − 1` (`p − 1 | p^d − 1`), so this prime is a **shared** invariant factor across every `char_k` at this prime. No choice of `Q` moves it. Only `p` does.

The round-two blue-team Fix 4 - "size `p` so `Φ_d(p)` carries a 256-bit prime" - is the imperative form of this statement: the largest prime-power invariant factor of `R^* ⊇ ⟨x⟩` must exceed `2²⁵⁶`.

## 4. Discriminant-zero primes: the `p`-group `1 + (g)/(g)^m`

The mod-`p` factorization of `char_k` has a repeated factor exactly when the discriminant `disc(char_k)` vanishes mod `p`.[^2] `disc(char_2) = -112 = -2⁴·7`, so the discriminant-zero primes of `char_2` are `2` and `7`. At those primes `Q` acquires a factor `g^m` with `m ≥ 2` and CRT gives, for that piece,

```
F_p[x]/(g^m)  =  local ring, not a field,
1 → 1 + (g)/(g)^m  →  ( F_p[x]/(g^m) )^*  →  F_{p^d}^*  →  1
```

The kernel is a **`p`-group** of order `p^{d(m-1)}`. Its elements are `1 + n` with `n` a multiple of `g`, and `g` is nilpotent in `F_p[x]/(g^m)`; "unit plus nilpotent is a unit" is the same fact that makes `1 + aX` a unit of `R[X]` when `a` is nilpotent.[^9] Since `gcd(p^{d(m-1)}, p^d − 1) = 1`, the sequence splits: `( F_p[x]/(g^m) )^* ≅ F_{p^d}^* × U`, cyclic-of-order-`(p^d - 1)` times a `p`-group. The extra `p` [[mod-p-observatory](pages/mod-p-observatory.md)] measures at discriminant-zero primes lives in `U`.

**Worked example — `char_2 mod 7`.** `char_2 mod 7 = (x − 2)(x + 3)²`.[^2] The local ring at `(x+3)²` has 42 units; multiplying out `(a + b·y)^n` with `y = x+3` in `F_7[y]/(y²)` gives `(a+by)^n = a^n + n·a^{n-1}by`, so this local unit group is `F_7^* × (1 + F_7·y)` = `Z/6 × Z/7 ≅ Z/42` (cyclic, `gcd(6, 7) = 1`). Combined with the linear piece:

```
R  =  F_7[x] / char_2
R^*  ≅  F_7^*   ×   Z/6 × Z/7
     =  Z/6    ×   Z/42                (invariant factors: (6, 42))
ord(x in R^*)  =  lcm( ord(2 in F_7^*),  ord(x mod (x+3)²) )  =  lcm(3, 21)  =  21
```

and `per(char_2 mod 7) = 21` is exactly the [[mod-p-observatory](pages/mod-p-observatory.md)] table entry.[^3] The **extra 7 vs the squarefree case** is the `Z/7` factor of `U`; it is the `n^{m-1} λ^n` term the observatory §"the finite-field connection" attributed to a repeated root, seen here as a *group* rather than as a polynomial-in-`n`.

**Every discriminant-zero prime used on the wiki, as a table.** Each row is a `(char_k, p)` where `char_k mod p` has a repeated factor `g^m`; the `p`-group column is `p^{d(m-1)}`.[^4]

| `char_k` | `disc` | `p` | factorization mod `p` | `p`-group `U` | `R^*` invariant factors | `ord(x)` |
|---|---|---|---|---|---|---|
| `char_2` | `-112` | 7 | `(x−2)(x+3)²` | `Z/7` | `(6, 42)` | 21 |
| `char_2` | `-112` | 2 | `x²·(x+1)` | `Z/2 × Z/2` | (see [^5]) | - |
| `char_3` | `2¹²·5` | 5 | `(x−1)²(x²−2x−2)` | `Z/5` | `(4, 120)` | 120 |
| `char_4` | `-2¹⁶·3·107` | 3 | `(x−1)²(x³−x−1)` | `Z/3` | `(2, 78)` | 39 |

Row 3: verified `per(char_3 mod 5) = 120`, matching [[mod-p-observatory](pages/mod-p-observatory.md)]. Row 4: `per(char_4 mod 3) = 39` from the same table; here `ord(x) = 39` sits at *half* the exponent `78`, because the projection of `x` into the `(x−1)²` local piece has order `3` (a generator of `U = Z/3`) but only `1` in the field factor `F_3^*` (`x mod (x−1) = 1`), so it misses the `Z/2 ⊂ F_3^*` component. The invariant-factor picture makes the gap between "exponent" and "`ord(x)`" fully explicit: `x` is a full generator of `U` and of `F_{p^d}^*`, but only up to what its residue in each `F_{p^{d_i}}^*` actually reaches. The **extra factor of `p`** in the [[mod-p-observatory](pages/mod-p-observatory.md)] period column is literally the size of `U` at each discriminant-zero prime - not a heuristic.

## 5. The two `d = 3` linear-complexity deficits, in one identity

Round-two Attack 5 measured the linear complexity of `s_n · s_{n+1} + s_{n+2}` and `s_n · s_{n+1} · s_{n+2}` for the `d = 3` register `char_2 = (x−2)(x²−x+2)`. The bounds `C(d+1, 2) + d = 9` and `C(d+2, 3) = 10` were both under-measured by 1 (`8` and `9`), while `d = 4, 6` were exact ([[castle-cryptography-round-two](pages/castle-cryptography-round-two.md)] Attack 5). The invariant-factor picture writes the two deficits as one algebraic fact.

`char_2` has roots `{2, α, ᾱ}` with `α + ᾱ = 1`, `α · ᾱ = 2` (Vieta on `x² − x + 2`). The last identity is the norm-map coincidence

```
N_{F_{p²}/F_p}( α )  =  α · ᾱ  =  2 ,
```

which says: the **norm map** (the map that sends `F_{p²}^*` down to `F_p^*` by multiplying an element by its Galois conjugate) sends `α` into the *very subgroup* the `(x−2)` factor generates. In the invariant-factor picture, the pair `⟨α⟩ ⊂ F_{p²}^*` and `⟨2⟩ ⊂ F_p^*` are *not* independent - their multiplicative structures share the element `2`.

**Deficit A - `s_n · s_{n+1} + s_{n+2}`, bound 9 → observed 8.** The characters are pair-products of the roots (6 distinct: `{4, 2α, 2ᾱ, α², ᾱ², αᾱ}`) plus the roots themselves (3 more: `{2, α, ᾱ}`), potentially 9. But `αᾱ = 2` collides one pair-product with one root, giving `|{4, 2α, 2ᾱ, α², ᾱ², 2} ∪ {2, α, ᾱ}| = 8`.[^6]

**Deficit B - `s_n · s_{n+1} · s_{n+2}`, bound 10 → observed 9.** The 10 unordered triple-products of `{2, α, ᾱ}` (`= C(3 + 2, 3) = C(5, 3) = 10`) simplify using `αᾱ = 2` but are all distinct - so it is *not* a coincidence of character values. Instead it is a **coefficient vanishing**: the coefficient of the character `4 = 2·α·ᾱ` in `s_n · s_{n+1} · s_{n+2}` is (up to the constant `c_1 c_2 c_3`)

```
2ᾱ + 2α + 2ᾱ² + 4ᾱ + 2α² + 4α    (six ordered triples for the multiset {2, α, ᾱ})
=  6(α + ᾱ) + 2(α² + ᾱ²)
=  6·s_1 + 2·s_2                   (Newton's identities:  s_1 = 1,  s_2 = s_1² − 2·αᾱ = 1 − 4 = −3)
=  6·1 + 2·(−3)
=  0 .
```

So the 4-character is present in the "generic 10" but *absent* from the actual signal: the linear complexity is 9, one less than the multiplicity bound.[^7] Both deficits are the **norm relation `α·ᾱ = 2`** projected onto two different filter geometries: in A it collides characters; in B it kills a coefficient via a Newton-identity accident (`s_2 = -3·s_1`).

## 6. What this consolidates

Five separate seminar entries, one identity:

- `[[mod-p-observatory](pages/mod-p-observatory.md)]`: `period = ord(x) in R^*` = `lcm` of componentwise orders.
- `[[kitamasa](pages/kitamasa.md)]`: `powmod(x, a)` is group exponentiation in `R^*`.
- `[[castle-cryptography-ring](pages/castle-cryptography-ring.md)] §5`: `ord(x)` and its factorization *are* the invariant-factor data of `⟨x⟩ ⊆ R^*`.
- `[[castle-cryptography-round-two](pages/castle-cryptography-round-two.md)]` Attack 3: Pohlig-Hellman is the FTFGAG applied to `⟨x⟩`.
- `[[castle-cryptography-round-two](pages/castle-cryptography-round-two.md)]` Attack 5, the `d = 3` deficits: the norm coincidence `α · ᾱ = 2` visible in the invariant-factor product of the `char_2` split.

And the discriminant-zero side of [[mod-p-observatory](pages/mod-p-observatory.md)] gets a *group* explanation: the `p`-group `1 + (g)/(g)^m` beside the field factor at any prime dividing `disc(char_k)`.

## Appearances in Sources

- [[oeis-mining-pe502](pages/oeis-mining-pe502.md)] - the `P(k, ·)` family and the `char_k` polynomials whose mod-`p` unit groups this page factors.

## Related Concepts

- [[castle-cryptography-ring](pages/castle-cryptography-ring.md)] - Seminar 1; §4 (CRT), §5 (`ord(x)` table) are the entry points to the invariant-factor decomposition run here.
- [[castle-cryptography-round-two](pages/castle-cryptography-round-two.md)] - Attack 3 (Pohlig-Hellman on `⟨x⟩` = FTFGAG here), Attack 4 (cyclotomic factorization of the exponent), Attack 5 (the `d = 3` deficits as the norm relation `α · ᾱ = 2`).
- [[castle-cryptography](pages/castle-cryptography.md)] - series overview; the invariant-factor picture is the group-theoretic backbone of Seminars 1-2.
- [[castle-cryptography-number-theory](pages/castle-cryptography-number-theory.md)] - the engineer-facing terms (char poly, irreducible, DLP); this page reads the same terms as an abelian-group structure.
- [[mod-p-observatory](pages/mod-p-observatory.md)] - `period = lcm of eigenvalue orders` and the "double root multiplies the period by `p`" observation, now identified as `ord(x)` in `R^*` and the `p`-group `1 + (g)/(g)^m`.
- [[finite-fields](pages/finite-fields.md)] - `F_{p^d}^*` cyclic of order `p^d − 1`; the field factors this page multiplies together.
- [[kitamasa](pages/kitamasa.md)] - `x^n mod Q` is binary group exponentiation in `R^*`; the seminar's trapdoor.
- [[tower-parity-sectors](pages/tower-parity-sectors.md)] - why `char_2` factors, and the `λ · λ̄ = 2` root relation on the quadratic factor; the same relation this page uses to explain the `d = 3` deficits.
- [[eigenvalue-continued-fractions](pages/eigenvalue-continued-fractions.md)] - the roots of `char_k` in `ℝ` and `ℂ`; the same roots this page reduces mod `p` and puts into `F_{p^{d_i}}^*`.
- [[berlekamp-massey](pages/berlekamp-massey.md)] - measures the linear complexity of a filtered sequence; the tool that produced the `d = 3` deficit numbers this page explains.
- [[larger-prime-periodicity](pages/larger-prime-periodicity.md)] - reads `R^*` via invariant factors at `10^9 + 7`; the concrete Connection-to-castle-cryptography section that this page's structure explains.
- [[parity-via-roots-of-unity](pages/parity-via-roots-of-unity.md)] - the m-th-root character sums that project out block-count residue classes are exactly the invariant-factor projectors on `R^* = ∏ Z/(p^{d_i} − 1)`.
- [[chinese-remainder-theorem](pages/chinese-remainder-theorem.md)] - the comaximal-ideal CRT that produces the product decomposition this page starts from.
- [[idempotent-decomposition](pages/idempotent-decomposition.md)] - the same decomposition by idempotents: repeated factors change the unit group (the `p`-group `U_i`) but not the number of idempotents, `2^r`.
- [[castle-snippets-number-theory](pages/castle-snippets-number-theory.md)] - `char_k` mod 2 in one line, and `crt_idempotents` for the CRT pieces.

## Footnotes

[^1]: Verified by execution (SymPy, 2026-09-21) at `p = 10⁹+7`: `sp.factor_list(char_1, x, modulus=p)` returns the polynomial unchanged (irreducible), `char_2` factors as `(x − 2)(x² − x + 2)`, `char_3` returns unchanged (irreducible). `ord(x)` in each ring computed by factor-stripping `p^d − 1`: `ord(x) mod char_1 = 4000000024 = 2³ · 500000003`; `ord(x) mod char_2 = 500000007000000024 = 2³·3²·7·109²·167·500000003`; `ord(x) mod char_3 = 800000016000000107200000240 = 2⁴·5·58699937·340715873·500000003`. At `p = 101`: `ord(2 in F_101^*) = 100`, `ord(x mod (x²−x+2), p=101) = 3400`, `lcm = 3400`. Invariant factors from the SNF of `diag(...)`: `Z/100 × Z/10200` has invariant factors `(100, 10200)` because `100 | 10200`. `Z/(p−1) × Z/(p²−1)` has invariant factors `(p−1, p²−1)` for the same reason.

[^2]: Verified by execution (SymPy, 2026-09-21): `sp.discriminant(char_2, x) = −112 = −2⁴·7`, so `char_2` has a repeated factor mod `p` iff `p ∈ {2, 7}`; `sp.factor_list(char_2, x, modulus=7)` returns `(x − 2)(x + 3)²`; `sp.factor_list(char_2, x, modulus=2)` returns `x² · (x + 1)`.

[^3]: Verified by execution (2026-09-21): `ord(2 in F_7^*) = 3`; `ord(x in F_7[x]/(x+3)²) = 21` (by factor-stripping `42 = 6·7`); the local unit group at `(x+3)²` has order `42 = 6·7` and structure `Z/6 × Z/7 ≅ Z/42` (cyclic since `gcd(6, 7) = 1`); combined with `F_7^*` from the `(x − 2)` factor, `R^* = Z/6 × Z/42`, invariant factors `(6, 42)`; `ord(x in R^*) = lcm(3, 21) = 21`. Matches `per(char_2 mod 7) = 21` from [[mod-p-observatory](pages/mod-p-observatory.md)]'s period table.

[^4]: Verified by execution (SymPy, 2026-09-21): `char_3 mod 5 = (x − 1)²(x² − 2x − 2)`, `sp.factor_list` confirms `x² − 2x − 2` is irreducible mod 5, `ord(x in F_5[x]/(x−1)²) = 5` (local `p`-group of order 5), `ord(x in F_5[x]/(x²−2x−2)) = 24 = p²−1`, `lcm = 120`, matching `per(char_3 mod 5) = 120` from the observatory. `char_4 mod 3 = (x − 1)²(x³ − x − 1)`; observed `ord(x)` composed similarly. `disc(char_3) = 2¹² · 5` so `p = 2, 5` are the discriminant-zero primes for `char_3`; `disc(char_4) = −2¹⁶ · 3 · 107` so `p = 2, 3, 107` are the discriminant-zero primes for `char_4`.

[^5]: The `p = 2` row for `char_2` is a genuine edge case: `char_2 mod 2 = x² · (x + 1)`, so the repeated factor is `x²` itself, and `x` (the generator!) is *not* a unit in `F_2[x]/(x²·(x+1))` - it projects to zero in the `x²` piece. The invariant-factor picture still applies to `R^*`, but the seminar's central object `⟨x⟩` is nowhere near it. This is why [[mod-p-observatory](pages/mod-p-observatory.md)] restricts to odd `p`: `char_k(0) = (−1)^{k−1} 2^k`, always a power of 2, so `p = 2` is the *only* prime where `x` fails to be a unit and pure periodicity breaks. The edge case is uniform in `k`: reducing `char_{k+1} = x² char_{k−1} − 2 char_k` mod 2 gives `char_{k+1} ≡ x² char_{k−1}`, so `char_k ≡ x^{k+1}` for odd `k` and `x^k (x + 1)` for even `k` (checked `k ≤ 30`). Hence `F_2[x]/(char_k)` is the local ring `F_2[x]/(x^{k+1})` (odd `k`) or `F_2[x]/(x^k) × F_2` (even `k`), `x` is nilpotent in the first factor, and `(2, x)` is a prime of `Z[x]/(char_k)`, the castle version of the non-principal ideal `(2, X)` of `Z[X]`.[^10] This is consistent with `P(k, L) ≡ T(k, L) = (k+1)^L (mod 2)`: signs vanish mod 2.

[^6]: Verified by execution (2026-09-21): `bm(P(2, ·) mod p, p) = 3` (matching the recurrence order), `bm(s_n · s_{n+1} + s_{n+2}) mod p = 8` at `p = 10⁹+7`; the six pair-products of `char_2`'s roots are `{4, 2α, 2ᾱ, α², ᾱ², αᾱ = 2}` and the three linear characters are `{2, α, ᾱ}`, so their union has cardinality `6 + 3 − 1 = 8` because `αᾱ = 2` is in both sets (Vieta on `x² − x + 2` gives constant term `2 = αᾱ`).

[^7]: Verified by execution (SymPy, 2026-09-21) with `α = (1 + i√7)/2` a root of `x² − x + 2` and `ᾱ` its conjugate: `α · ᾱ = 2`, `α + ᾱ = 1`, `α² + ᾱ² = 1 − 4 = −3`. For the ten multisets of size 3 from `{2, α, ᾱ}` the products are `{8, 4α, 4ᾱ, 2α², 4, 2ᾱ², α³, 2α, 2ᾱ, ᾱ³}` (ten distinct values). The character `μ = 4` comes from the multiset `{2, α, ᾱ}`, i.e., six ordered triples; the sum of `c_i c_j c_k · λ_j · λ_k²` across those six triples is `c_1 c_2 c_3 · (6(α + ᾱ) + 2(α² + ᾱ²)) = c_1 c_2 c_3 · (6 − 6) = 0`, so the character `4` is absent from `s_n · s_{n+1} · s_{n+2}` and the linear complexity is `10 − 1 = 9`. `bm(s_n s_{n+1} s_{n+2}, p) = 9` at `p = 10⁹+7`.
[^8]: [[calugareanu-hamburg-exercises-basic-ring-theory](pages/calugareanu-hamburg-exercises-basic-ring-theory.md)] Ex. 17.20 p.76; solution p.193 [synthesis] - for pairwise comaximal ideals `I_1, …, I_n`, `R/∩I_i → ∏ R/I_i` is an isomorphism (equivalently every congruence system is solvable); in `F_p[x]`, `(f)` and `(g)` are comaximal iff `gcd(f, g) = 1`.
[^9]: [[calugareanu-hamburg-exercises-basic-ring-theory](pages/calugareanu-hamburg-exercises-basic-ring-theory.md)] Exs. 14.15-14.16 p.61; solutions pp.171-172 [synthesis] - `f ∈ R[X]` is a unit iff its constant term is a unit and its other coefficients are nilpotent; `R` has a nonzero nilpotent iff `R[X]` has a unit of positive degree.
[^10]: [[calugareanu-hamburg-exercises-basic-ring-theory](pages/calugareanu-hamburg-exercises-basic-ring-theory.md)] Exs. 14.13, 14.19 pp.60-61; solutions pp.171-172 [synthesis] - `(2, X)` is not principal in `Z[X]`, and `Z[X]/(n, X) ≅ Z_n`. The mod-2 shape of `char_k` was verified by execution (SymPy, 2026-09-26): `sp.Poly(char_k, x, modulus=2)` equals `x^{k+1}` for odd `k` and `x^k (x + 1)` for even `k`, every `k ≤ 30`; the first six are pinned on [[castle-snippets-number-theory](pages/castle-snippets-number-theory.md)].
