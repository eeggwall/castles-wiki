---
title: Castle ring by invariant factors
category: Analyses
summary: The unit group of the castle ring R = F_p[x]/(char_k mod p) as a product of cyclic groups. By the Chinese Remainder Theorem, R^* ≅ ∏ (F_{p^{d_i}}^* × U_i) over the irreducible factors g_i^{m_i} of char_k mod p, with U_i a p-group of order p^{d_i(m_i − 1)}, trivial when m_i = 1. The mod-p period of P(k, ·) is the order of x in R^* (num_k and den_k coprime mod p in every case here), Kitamasa's method is exponentiation in R^*, and Pohlig-Hellman costs about √q for the largest prime q dividing ord(x), which at p = 10⁹ + 7 is 500000003 = (p − 1)/2 for k = 1, 2, 3. At a prime dividing disc(char_k) the p-group supplies the extra factor of p in the period (per(char_2 mod 7) = 21 = 3·7). The two d = 3 linear-complexity deficits of the filtered generator both come from α·ᾱ = 2 for the roots of x² − x + 2.
tags: [analysis, cryptography, ring, finite-field, unit-group, invariant-factors, structure-theorem, pohlig-hellman, kitamasa, discriminant, linear-complexity, castle]
sources: [oeis-mining-pe502, calugareanu-hamburg-exercises-basic-ring-theory]
created: 2026-09-21
updated: 2026-10-25
---

# Castle ring by invariant factors

[[castle-cryptography-ring](pages/castle-cryptography-ring.md)] computes in `R = F_p[x]/(Q)` with `Q = char_k mod p`, the characteristic polynomial of the signed tower count `P(k, ·)` reduced mod an odd prime `p`, and [[castle-cryptography-round-two](pages/castle-cryptography-round-two.md)] attacks discrete logarithms in the cyclic group `⟨x⟩ ⊆ R^*`. This page writes `R^*` as a finite abelian group in invariant factors and reads the periods, the cost of Kitamasa's method, the Pohlig-Hellman attack and the linear-complexity deficits of round two from it.

A finite abelian group is isomorphic to `Z/n_1 × ⋯ × Z/n_t` with `n_1 | n_2 | ⋯ | n_t`; the `n_i` are its **invariant factors**, and `n_t`, the largest, is its **exponent**, the least `n` with `g^n = 1` for every element `g`. For a product of cyclic groups of orders `c_1, …, c_s`, the invariant factors are the nonunit diagonal entries of the Smith normal form of `diag(c_1, …, c_s)`, the diagonal matrix that row and column operations over `Z` reduce it to.

For `Q = ∏_i g_i^{m_i}` with `g_i` distinct monic irreducibles of degree `d_i` over `F_p`, the Chinese Remainder Theorem for the pairwise comaximal ideals `(g_i^{m_i})` ([[chinese-remainder-theorem](pages/chinese-remainder-theorem.md)])[^8] and the structure of the finite fields ([[finite-fields](pages/finite-fields.md)]) give

```
R^*  ≅  ∏_i  ( F_{p^{d_i}}^*  ×  U_i )  ≅  ∏_i  ( Z/(p^{d_i} − 1)  ×  U_i ),        U_i  =  1 + (g_i)/(g_i^{m_i}),      (1)
```

with `U_i` an abelian `p`-group of order `p^{d_i(m_i − 1)}`, trivial when `m_i = 1` (section 4).

## 1. Squarefree `Q`

When `Q` is squarefree every `m_i = 1`, each factor `F_p[x]/(g_i)` is the field `F_{p^{d_i}}`, and by Equation (1), `R^* ≅ ∏_i Z/(p^{d_i} − 1)`, a product of cyclic groups whose exponent is `lcm_i (p^{d_i} − 1)`.

The cases of the cryptography pages:[^1]

| `k` | `p` | factors of `Q = char_k mod p` | `R^*` | invariant factors | order of `x` in `R^*` |
|---|---|---|---|---|---|
| 2 | 101 | `(x − 2)(x² − x + 2)` | `Z/100 × Z/10200` | `(100, 10200)` | `3400` |
| 1 | `10⁹ + 7` | `x² − 2x + 2` (irreducible) | `Z/(p² − 1)` | `(p² − 1)` | `2³·500000003 = 4(p − 1)` |
| 2 | `10⁹ + 7` | `(x − 2)(x² − x + 2)` | `Z/(p − 1) × Z/(p² − 1)` | `(p − 1, p² − 1)` | `2³·3²·7·109²·167·500000003 = (p² − 1)/2` |
| 3 | `10⁹ + 7` | `x⁴ − 4x³ + 8x² − 8x + 8` (irreducible) | `Z/(p⁴ − 1)` | `(p⁴ − 1)` | `2⁴·5·58699937·340715873·500000003` |

**The period is the order of `x`.** The period of `P(k, ·) mod p` divides the order of `x` in `R^*` and equals it when `num_k` and `den_k` are coprime mod `p`, so that `Q` is the minimal polynomial of the sequence mod `p`; that holds at every prime, since the update of `num_k` and `den_k` has determinant `−1` ([[castle-cryptography-ring](pages/castle-cryptography-ring.md)], section 6). The order of `x` in a product is the lcm of the orders of its components, the images of `x` in the factors `F_{p^{d_i}}^*`, which are the roots of the `g_i` ([[mod-p-observatory](pages/mod-p-observatory.md)]). In the first row, `ord(2) = 100` in `F_101^*`, the root `α` of `x² − x + 2` has order `3400 = (101² − 1)/3` in `F_{101²}^*`, and `lcm(100, 3400) = 3400`.

**The order of `x` need not be the exponent.** In the first row the exponent is `10200` and the order of `x` is `3400`. In the third row the exponent is `p² − 1` and the order of `x` is `(p² − 1)/2`. There the norm of `α` from `F_{p²}` to `F_p` is `α^{p+1} = α·ᾱ = 2` (Vieta on `x² − x + 2`), and `2` is a square mod `p` because `p ≡ 7 (mod 8)`. So `α^{(p²−1)/2} = 2^{(p−1)/2} = 1`, and the order of `α` divides `(p² − 1)/2`; it equals it (computed), and `ord(2) = (p − 1)/2` divides it.

## 2. Kitamasa's method is exponentiation in `R^*`

[[kitamasa](pages/kitamasa.md)] computes `x^n mod Q` by repeated squaring in `R`. The constant term of `char_k` is `(−1)^{k+1} 2^k`, nonzero mod every odd prime, so `x` is a unit of `R` and the computation takes place in the group `R^*`: `O(log n)` squarings and products, each `O(D²)` operations for `D = deg Q = k + 1`.

## 3. Pohlig-Hellman and the largest prime factor of `ord(x)`

Attack 3 of round two recovers a private exponent from `x^a` by factoring `n = ord(x)`, solving the discrete logarithm modulo each prime power `q^e` dividing `n`, and combining the results by the Chinese Remainder Theorem on the integers ([[castle-cryptography-round-two](pages/castle-cryptography-round-two.md)]). The group `⟨x⟩` is cyclic of order `n`, and `Z/n ≅ ∏ Z/q^e` over the prime powers `q^e` exactly dividing `n`. Baby-step giant-step solves a logarithm in a cyclic group of prime order `q` in about `√q` operations, and one of order `q^e` with `e` such solutions. So the attack costs about `√q` for the largest prime `q` dividing `ord(x)`.

The last three rows of the table share the largest prime factor `500000003 = (p − 1)/2`, which is prime. Every irreducible factor of degree `d` contributes `F_{p^d}^*`, of order `p^d − 1`, divisible by `p − 1`; so `500000003` divides `|R^*|` for every `Q` at this prime, and it divides the order of `x` in all three rows. This is why Attack 4 of round two recovers the same private key, `373309869`, under three different moduli `Q` at the same `p`. Changing `Q` does not remove the prime from `R^*`; changing `p` does. Round two's Fix 4, to choose `p` so that `Φ_d(p)` carries a 256-bit prime, makes the largest prime factor of `ord(x)` exceed `2^{256}` and the cost exceed `2^{128}`.

## 4. Repeated factors: the `p`-group `U`

`char_k mod p` has a repeated factor exactly when `p` divides `disc(char_k)`.[^2] For `char_2`, `disc = −112 = −2⁴·7`, so the primes are `2` and `7`. A repeated factor `g^m`, `m ≥ 2`, of degree-`d` irreducible `g`, contributes the CRT factor

```
F_p[x]/(g^m),          1  →  1 + (g)/(g^m)  →  ( F_p[x]/(g^m) )^*  →  F_{p^d}^*  →  1 .
```

`F_p[x]/(g^m)` is `F_p[x]/M^m` for the maximal ideal `M = (g)`, and every `R/M^m` is a local ring.[^11] The kernel `U = 1 + (g)/(g^m)` has order `p^{d(m−1)}`: its elements are `1 + n` with `n` a multiple of `g`, and `g` is nilpotent mod `g^m`, so `1 + n` is a unit, by the same fact that makes `1 + aX` a unit of `R[X]` for nilpotent `a`.[^9] The orders `p^{d(m−1)}` and `p^d − 1` are coprime, so the sequence splits: `(F_p[x]/(g^m))^* ≅ F_{p^d}^* × U`.

*Example: `char_2 mod 7`.* `char_2 ≡ (x − 2)(x + 3)² (mod 7)`, since `(x + 3)² = x² + 6x + 9 ≡ x² − x + 2`.[^2] In `F_7[x]/((x + 3)²)`, write `y = x + 3`; then `(a + by)^n = a^n + n a^{n−1} b y`, so the local unit group, of order 42, is `F_7^* × (1 + F_7 y) ≅ Z/6 × Z/7 ≅ Z/42`. With the factor `x − 2`:

```
R^*                ≅  F_7^*  ×  Z/6 × Z/7   =   Z/6 × Z/42                  (invariant factors (6, 42))
order of x in R^*  =  lcm( ord(2) in F_7^*,  order of x mod (x + 3)² )  =  lcm(3, 21)  =  21
```

The image of `x` mod `(x + 3)²` is `4 + y`, and `(4 + y)^n = 4^n + n·4^{n−1} y` is `1` exactly when `3 | n` and `7 | n`. The period `per(char_2 mod 7) = 21` of [[mod-p-observatory](pages/mod-p-observatory.md)] is this order.[^3] Its factor 7, absent at squarefree primes, is the order of the component of `x` in `U = Z/7`; in recurrence language it is the term `n λ^n` of a double root ([[finite-fields](pages/finite-fields.md)]).

The repeated-factor cases of the wiki's tables, with `U` of order `p^{d(m−1)}`:[^4]

| `char_k` | `disc(char_k)` | `p` | factors mod `p` | `U` | invariant factors of `R^*` | order of `x` |
|---|---|---|---|---|---|---|
| `char_2` | `−2⁴·7` | 7 | `(x − 2)(x + 3)²` | `Z/7` | `(6, 42)` | 21 |
| `char_2` | `−2⁴·7` | 2 | `x²(x + 1)` | `Z/2` | `(2)` | `x` not a unit[^5] |
| `char_3` | `2¹²·5` | 5 | `(x − 1)²(x² − 2x − 2)` | `Z/5` | `(4, 120)` | 120 |
| `char_4` | `2¹⁶·3·107` | 3 | `(x − 1)²(x³ − x − 1)` | `Z/3` | `(2, 78)` | 39 |

In the `char_3` row, `R^* ≅ Z/4 × Z/5 × Z/24 ≅ Z/4 × Z/120`, and `x` has orders 1, 5 and 24 in the three factors. In the `char_4` row, `R^* ≅ Z/2 × Z/3 × Z/26 ≅ Z/2 × Z/78`, and `x` has order 1 in `F_3^*` (its image is `1`), 3 in `U` and 13 in `F_27^*`, so its order `39` is half the exponent `78`. In each row with `d = 1` and `m = 2`, the component of `x` in `U` has the full order `p`. In ring terms `U` is `1 + N(R)` for the nilradical `N(R)`, and the period is the period in the reduced ring `R/N(R)` times `p^{⌈log_p m⌉}` at all seven repeated-factor primes `p < 200` with `k ≤ 8` ([[castle-ring-spectrum](pages/castle-ring-spectrum.md)], section 3).

## 5. The two `d = 3` linear-complexity deficits

Attack 5 of round two measures the linear complexity, the length of the shortest linear recurrence, of the filtered sequences `s_n s_{n+1} + s_{n+2}` and `s_n s_{n+1} s_{n+2}` for `s_n = P(2, n) mod p`, whose characteristic polynomial `char_2 = (x − 2)(x² − x + 2)` has `d = 3` roots. Write `s_n = Σ_i c_i λ_i^n` over the roots `λ_i ∈ {2, α, ᾱ}`. A product of shifts expands as a sum `Σ_μ C_μ μ^n` over the products `μ` of roots, and its linear complexity is the number of distinct `μ` with `C_μ ≠ 0`. The bounds are `C(d+1, 2) + d = 9` and `C(d+2, 3) = 10`, and the measured values at `p = 10⁹ + 7` are 8 and 9 (computed), while round two reports `d = 4` and `d = 6` at their bounds ([[castle-cryptography-round-two](pages/castle-cryptography-round-two.md)], Attack 5). Both deficits come from `α + ᾱ = 1` and `α·ᾱ = 2`, Vieta on `x² − x + 2`, which says that the norm of `α` from `F_{p²}` to `F_p` is the third root `2`.

**`s_n s_{n+1} + s_{n+2}`: 8, not 9.** The values `μ` are the six products of two roots, `{4, 2α, 2ᾱ, α², ᾱ², αᾱ}`, and the three roots `{2, α, ᾱ}`. Since `αᾱ = 2`, one product coincides with a root, and there are `6 + 3 − 1 = 8` distinct values.[^6]

**`s_n s_{n+1} s_{n+2}`: 9, not 10.** The ten products of three roots are distinct: `8, 4α, 4ᾱ, 2α², 4, 2ᾱ², α³, 2α, 2ᾱ, ᾱ³`. Here a coefficient vanishes instead. With `s_n s_{n+1} s_{n+2} = Σ_{i,j,l} c_i c_j c_l λ_j λ_l² (λ_i λ_j λ_l)^n`, the value `μ = 4 = 2·α·ᾱ` comes from the six orderings of the multiset `{2, α, ᾱ}`, and its coefficient is `c_1 c_2 c_3` times

```
αᾱ² + ᾱα² + 2ᾱ² + 4ᾱ + 2α² + 4α   =   2ᾱ + 2α + 2(α² + ᾱ²) + 4(α + ᾱ)
                                   =   6(α + ᾱ) + 2(α² + ᾱ²)
                                   =   6·1 + 2·(1 − 2·2)   =   0 ,
```

using `α² + ᾱ² = (α + ᾱ)² − 2αᾱ`. So nine of the ten values occur.[^7]

## Appearances in Sources

- [[oeis-mining-pe502](pages/oeis-mining-pe502.md)] - the family `P(k, ·)` and its characteristic polynomials `char_k`.
- [[calugareanu-hamburg-exercises-basic-ring-theory](pages/calugareanu-hamburg-exercises-basic-ring-theory.md)] - the Chinese Remainder Theorem (Ex. 17.20), local rings `R/M^n` (Ex. 13.26), units of `R[X]` (Exs. 14.15-14.16), and `(2, X)` in `Z[X]` (Exs. 14.13, 14.19).

## Related Concepts

- [[castle-cryptography-ring](pages/castle-cryptography-ring.md)] - the ring `F_p[x]/(Q)` (section 2), the coprimality of `num_k` and `den_k` (section 6), the orders of `x` for `k ≤ 7` at two primes (section 7) and the norm `2^k` of `x` (section 8).
- [[castle-cryptography-round-two](pages/castle-cryptography-round-two.md)] - Attack 3 (Pohlig-Hellman), Attack 4 (the cyclotomic factorization of `p^d − 1`), Attack 5 (the linear-complexity bounds), Fix 4.
- [[castle-cryptography](pages/castle-cryptography.md)] - the castle cryptosystem the two seminars build and attack.
- [[castle-cryptography-number-theory](pages/castle-cryptography-number-theory.md)] - characteristic polynomials, irreducibility and discrete logarithms for the cryptosystem.
- [[mod-p-observatory](pages/mod-p-observatory.md)] - the periods of the castle counts mod `p` and the extra factor of `p` at repeated factors.
- [[finite-fields](pages/finite-fields.md)] - `F_{p^d}^*` is cyclic of order `p^d − 1`.
- [[kitamasa](pages/kitamasa.md)] - `x^n mod Q` by repeated squaring.
- [[tower-parity-sectors](pages/tower-parity-sectors.md)] - why `char_k` factors for even `k`, as `char_2 = (x − 2)(x² − x + 2)`.
- [[eigenvalue-continued-fractions](pages/eigenvalue-continued-fractions.md)] - the real and complex roots of `char_k`.
- [[berlekamp-massey](pages/berlekamp-massey.md)] - the algorithm that measures linear complexity.
- [[larger-prime-periodicity](pages/larger-prime-periodicity.md)] - the factorizations of `char_k` mod `10⁹ + 7` and the periods there.
- [[parity-via-roots-of-unity](pages/parity-via-roots-of-unity.md)] - character sums over `Z/m`, another use of finite abelian groups.
- [[chinese-remainder-theorem](pages/chinese-remainder-theorem.md)] - the product decomposition this page starts from.
- [[idempotent-decomposition](pages/idempotent-decomposition.md)] - the same decomposition by idempotents; a repeated factor changes the unit group but not the number `2^r` of idempotents.
- [[castle-snippets-number-theory](pages/castle-snippets-number-theory.md)] - `char_k mod 2` and `crt_idempotents`.
- [[castle-ring-spectrum](pages/castle-ring-spectrum.md)] - the fibers of `Spec Z[x]/(char_k)`; section 3 splits the period into the reduced part and the nilradical.
- [[castle-fibers-char-2-walkthrough](pages/castle-fibers-char-2-walkthrough.md)] - `char_2` across several primes; Stop 7 reads `α·ᾱ = 2` as the splitting of 2 in `Z[(1 + √−7)/2]`.
- [[sandpile-group](pages/sandpile-group.md)] - another finite abelian group read off a Smith normal form.

## Footnotes

[^1]: Verified by execution (Python 3.11 with SymPy, 2026-10-16): at `p = 10⁹ + 7`, `char_1` and `char_3` are irreducible and `char_2 = (x − 2)(x² − x + 2)`; the order of `x` in each ring by stripping prime factors from the group order: `4000000024 = 2³·500000003 = 4(p − 1)` for `char_1`, `500000007000000024 = 2³·3²·7·109²·167·500000003 = (p² − 1)/2` for `char_2` (equal to the order of `α` in `F_{p²}^*`; `ord(2) = 500000003` in `F_p^*`), `800000016000000107200000240 = 2⁴·5·58699937·340715873·500000003 = (p⁴ − 1)/1250000010` for `char_3`; `500000003` is prime and `p ≡ 7 (mod 8)`. At `p = 101`: `x² − x + 2` irreducible, `ord(2) = 100`, the order of `α` in `F_{101²}^*` is `3400`. `num_k` and `den_k` are coprime mod `p` in all four rows.
[^2]: Verified by execution (Python 3.11 with SymPy, 2026-10-16): `disc(char_2) = −112 = −2⁴·7`, `disc(char_3) = 20480 = 2¹²·5`, `disc(char_4) = 21037056 = 2¹⁶·3·107`; `char_2 ≡ (x − 2)(x + 3)² (mod 7)` and `char_2 ≡ x²(x + 1) (mod 2)`.
[^3]: Verified by execution (Python 3.11, 2026-10-16): `ord(2) = 3` in `F_7^*`; the order of `x` mod `(x + 3)²` over `F_7` is `21`; the order of `x` in `F_7[x]/(char_2)` is `21`, and `num_2`, `den_2` are coprime mod 7.
[^4]: Verified by execution (Python 3.11 with SymPy, 2026-10-16): `char_3 ≡ (x − 1)²(x² − 2x − 2) (mod 5)` with the quadratic irreducible, order of `x` `120`; `char_4 ≡ (x − 1)²(x³ − x − 1) (mod 3)` with the cubic irreducible, order of `x` `39`; `num_k`, `den_k` coprime mod `p` in both.
[^5]: At `p = 2`, `char_2 ≡ x²(x + 1)`, and `x` is nilpotent in the factor `F_2[x]/(x²)`, so it is not a unit; `R^* = (1 + (x)/(x²)) × F_2^* ≅ Z/2`, and `⟨x⟩` is not a subgroup. This is why [[mod-p-observatory](pages/mod-p-observatory.md)] restricts to odd `p`: the constant term `(−1)^{k+1} 2^k` of `char_k` is a power of 2 up to sign, so `p = 2` is the only prime at which `x` is not a unit. Reducing `char_{k+1} = x² char_{k−1} − 2 char_k` mod 2 gives `char_{k+1} ≡ x² char_{k−1}`, so `char_k ≡ x^{k+1}` for odd `k` and `x^k (x + 1)` for even `k`. Hence `F_2[x]/(char_k)` is the local ring `F_2[x]/(x^{k+1})` for odd `k` and `F_2[x]/(x^k) × F_2` for even `k`, and `(2, x)` is a prime of `Z[x]/(char_k)`, the castle form of the non-principal ideal `(2, X)` of `Z[X]`.[^10] This agrees with `P(k, L) ≡ T(k, L) = (k+1)^L (mod 2)`, since signs vanish mod 2.
[^6]: Verified by execution (Python 3.11, 2026-10-16): Berlekamp-Massey gives linear complexity 3 for `P(2, ·) mod p` and 8 for `s_n s_{n+1} + s_{n+2}` at `p = 10⁹ + 7`; with `α = (1 + i√7)/2`, the six products of two roots together with the three roots take 8 distinct values.
[^7]: Verified by execution (Python 3.11 with SymPy, 2026-10-16): the ten products of three roots of `char_2` are distinct complex numbers, and Berlekamp-Massey gives linear complexity 9 for `s_n s_{n+1} s_{n+2}` at `p = 10⁹ + 7`.
[^8]: [[calugareanu-hamburg-exercises-basic-ring-theory](pages/calugareanu-hamburg-exercises-basic-ring-theory.md)] Ex. 17.20 p.76; solution p.193 [synthesis] - for pairwise comaximal ideals `I_1, …, I_n`, `R/∩I_i → ∏ R/I_i` is an isomorphism (equivalently every congruence system is solvable).
[^9]: [[calugareanu-hamburg-exercises-basic-ring-theory](pages/calugareanu-hamburg-exercises-basic-ring-theory.md)] Exs. 14.15-14.16 p.61; solutions pp.171-172 [synthesis] - `f ∈ R[X]` is a unit iff its constant term is a unit and its other coefficients are nilpotent; `R` has a nonzero nilpotent iff `R[X]` has a unit of positive degree.
[^10]: [[calugareanu-hamburg-exercises-basic-ring-theory](pages/calugareanu-hamburg-exercises-basic-ring-theory.md)] Exs. 14.13, 14.19 pp.60-61; solutions pp.171-172 [synthesis] - `(2, X)` is not principal in `Z[X]`, and `Z[X]/(n, X) ≅ Z_n`.
[^11]: [[calugareanu-hamburg-exercises-basic-ring-theory](pages/calugareanu-hamburg-exercises-basic-ring-theory.md)] Ex. 13.26 p.57; solution pp.166-167 [synthesis] - for `M` maximal in a commutative ring with identity, `R/M^n` is local: each `a + 1` with `a ∈ M` is a unit mod `M^n` by the finite geometric series, so `M/M^n` is the unique maximal ideal.
