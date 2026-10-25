---
title: Larger-prime periodicity of char_k
category: Analyses
summary: For odd primes p up to 97 and k ≤ 6, the order per(char_k) of x in (F_p[x]/(char_k))^*, which is the period of P(k, ·) mod p in every tabulated case, read off the factorization of char_k mod p; a factor of multiplicity m multiplies the order by exactly p^⌈log_p m⌉ (proved). The odd prime factors of disc(char_k) for k ≤ 10 are the primes where char_k mod p has a repeated factor, each time one linear factor of multiplicity 2. The degrees of the factors follow the Galois group of char_k over Q (D_4 for char_3). At the Project Euler modulus M = 10^9 + 7, char_1 and char_3 are irreducible, char_2 = (x − 2)(x² − x + 2) with ord_M(2) = (M − 1)/2, char_6 has three roots mod M of order (M − 1)/2, and M divides no disc(char_k) for k ≤ 30.
tags: [analysis, castle, modular-arithmetic, periodicity, large-primes, chebotarev, discriminant, project-euler-502]
sources: [project-euler-502-castle-factoring, oeis-mining-pe502]
created: 2026-09-22
updated: 2026-10-25
---

# Larger-prime periodicity of char_k

The [[mod-p-observatory](pages/mod-p-observatory.md)] computes the periods of the castle counts `A^e(·, h)` mod `p` for `p = 3, 5, 7`, from the periods of the signed tower counts `P(k, ·)` mod `p`. This page computes those tower periods for odd primes up to 97, explains them by the factorization of the characteristic polynomial `char_k` of `P(k, ·)` ([[signed-tower-count](pages/signed-tower-count.md)]), and works out the Project Euler modulus `M = 10^9 + 7` (written `M`, since `P` is the signed tower count, [[castle-notation](pages/castle-notation.md)]).

For an odd prime `p`, let `R = F_p[x]/(char_k)`. The constant term `(−1)^{k+1} 2^k` of `char_k` is nonzero mod `p`, so `x` is a unit of `R`, and `per(char_k)` denotes the order of `x` in the unit group `R^*`. Every sequence mod `p` that satisfies the recurrence of `char_k` is purely periodic with a period dividing `per(char_k)`, and `P(k, ·) mod p` has period exactly `per(char_k)` when `num_k` and `den_k` are coprime mod `p` ([[chinese-remainder-theorem](pages/chinese-remainder-theorem.md)]). They are coprime in every case tabulated on this page (computed).[^exec]

## The period from the factorization

Write `char_k ≡ ∏ g_i^{m_i} (mod p)` with distinct irreducible `g_i` of degree `d_i`. The Chinese remainder theorem splits `R` into the rings `F_p[x]/(g_i^{m_i})`, and `per(char_k)` is the lcm of the orders of `x` in their unit groups.

- When `m_i = 1`, `F_p[x]/(g_i)` is the field `F_{p^{d_i}}`, and the order of `x` there divides `p^{d_i} − 1`. If `char_k` is irreducible mod `p`, then `per(char_k)` divides `p^{k+1} − 1`.
- When `m_i = m ≥ 2`, the order of `x` in `F_p[x]/(g^m)` is its order mod `g` times exactly `p^{⌈log_p m⌉}`.

*Proof of the second case.* In `S = F_p[x]/(g^m)` the Frobenius map `y ↦ y^p` is additive. Let `q = p^d`, choose `t` with `q^t ≥ m`, and set `θ = x^{q^t}`. Then `g(θ) = g(x)^{q^t} = 0`, since `g` has coefficients in `F_p` and `(g)^m = 0`; `θ ≡ x (mod g)`; and `θ^q = θ`, because `x^q = x + n` with `n ∈ (g)` and `n^{q^t} = 0`. So `θ` has the order of `x mod g`, which is prime to `p`. Write `g(X) = (X − θ)u(X)`; then `u(x) ≡ u(θ) = g′(θ) ≡ g′(x) (mod g)`, a unit because `g` is separable, so `x − θ = g(x)u(x)^{−1}` generates the ideal `(g)`, and `a = (x − θ)θ^{−1}` has `a^j ≠ 0` for `j < m`. Since `(1 + a)^{p^e} = 1 + a^{p^e}`, the order of `1 + a` is `p^{⌈log_p m⌉}`. So `x = θ(1 + a)` is a product of commuting elements of coprime orders `ord(x mod g)` and `p^{⌈log_p m⌉}`. ∎

[[castle-ring-spectrum](pages/castle-ring-spectrum.md)] (section 3) describes the same factor as the exponent of `1 + N`, `N` the nilradical of `R`, and checks the full order at every odd discriminant prime below 200 for `k ≤ 8`.

`per(char_k)` mod `p`:[^exec]

| `p` | `k = 1` | `k = 2` | `k = 3` | `k = 4` | `k = 5` | `k = 6` |
|---|---|---|---|---|---|---|
| 3 | 8 | 8 | 80 | 39 | 728 | 312 |
| 5 | 4 | 24 | 120 | 12 | 124 | 372 |
| 7 | 24 | 21 | 400 | 48 | 58824 | 16 |
| 11 | 40 | 10 | 120 | 1995 | 7320 | 7980 |
| 13 | 12 | 168 | 84 | 2196 | 15372 | 1742160 |
| 17 | 16 | 144 | 288 | 288 | 288 | 44208 |
| 19 | 72 | 360 | 360 | 3429 | 9409176 | 130320 |
| 23 | 88 | 22 | 46640 | 5214 | 93280 | 6072 |
| 29 | 28 | 28 | 28 | 84 | 146328 | 205346960 |
| 31 | 40 | 160 | 960 | 960 | 61568 | 14895 |
| 37 | 36 | 36 | 1368 | 50652 | 1368 | 1874160 |
| 41 | 20 | 840 | 840 | 103380 | 964880 | 34460 |
| 53 | 52 | 52 | 1404 | 446628 | 148824 | 1578096 |
| 97 | 96 | 4704 | 9408 | 4704 | 912672 | 44720928 |

The entries vary widely with `p`; each one is the lcm read off the factorization in the section *Factorization patterns and the Galois group*.

## Discriminants: the primes with repeated factors

Since `char_k` is monic, `char_k mod p` has a repeated factor exactly when `p` divides the discriminant `disc(char_k)`. The discriminants are a power of 2 times a small odd part:[^exec]

| `k` | degree | `disc(char_k)` | odd prime factors |
|---|---|---|---|
| 1 | 2 | `-2^2` | *(none)* |
| 2 | 3 | `-2^4 * 7` | 7 |
| 3 | 4 | `+2^{12} * 5` | 5 |
| 4 | 5 | `+2^{16} * 3 * 107` | 3, 107 |
| 5 | 6 | `-2^{31} * 53` | 53 |
| 6 | 7 | `-2^{36} * 3 * 23 * 643` | 3, 23, 643 |
| 7 | 8 | `+2^{56} * 5449` | 5449 |
| 8 | 9 | `+2^{64} * 257 * 49697` | 257, 49697 |
| 9 | 10 | `-2^{90} * 37 * 14153` | 37, 14153 |
| 10 | 11 | `-2^{100} * 5 * 19 * 4409 * 15121` | 5, 19, 4409, 15121 |

For `k ≤ 10`, each odd prime factor divides `disc(char_k)` exactly once, and at each such `p` the polynomial `char_k mod p` has exactly one repeated factor, linear and of multiplicity 2 (computed). By the section *The period from the factorization*, each such prime multiplies the order of `x` by exactly `p`. Examples:

- `p = 7`, `k = 2`: `char_2 ≡ (x − 2)(x + 3)^2 (mod 7)`, which makes the period of `A^e(·, 4) mod 7` equal to `8400 = 1200 · 7` ([[mod-p-observatory](pages/mod-p-observatory.md)]).
- `p = 5`, `k = 3`: `char_3 ≡ (x − 1)^2 · (quadratic) (mod 5)`.
- `p = 3`: `(x − 1)^2` divides `char_k mod 3` exactly when `k ≡ 4 (mod 12)` and `(x + 1)^2` exactly when `k ≡ 6 (mod 12)`, and no cube of a linear factor ever does (proved on [[mod-9-coset-lift](pages/mod-9-coset-lift.md)]); no factor of degree at least 2 repeats for `k ≤ 200` (computed). `k = 4` and `k = 6` appear in the table.
- `p = 5` divides both `disc(char_3)` and `disc(char_10)`.

The odd parts for `k = 4, …, 10` are `3·107`, `53`, `3·23·643`, `5449`, `257·49697`, `37·14153` and `5·19·4409·15121`. The modulus `M = 10^9 + 7` divides none of `disc(char_k)` for `k ≤ 30` (computed).

## Factorization patterns and the Galois group

For a prime `p` not dividing `disc(char_k)`, the degrees of the irreducible factors of `char_k mod p` are the cycle lengths of a permutation of the `k + 1` roots of `char_k`, the Frobenius element at `p` in the Galois group `G` of `char_k` over `Q`. Chebotarev's density theorem states that each cycle type occurs for a proportion of primes equal to the proportion of elements of `G` with that cycle type. The factorization signatures of `char_k mod p` for `k = 1, …, 5`, with `d^m` marking a factor of degree `d` and multiplicity `m > 1`:[^exec]

| `p` | `char_1` | `char_2` | `char_3` | `char_4` | `char_5` |
|---|---|---|---|---|---|
| 3 | `2` | `1\|2` | `4` | `1^2\|3` | `6` |
| 5 | `1\|1` | `1\|2` | `1^2\|2` | `1\|2\|2` | `3\|3` |
| 7 | `2` | `1\|1^2` | `4` | `1\|1\|1\|2` | `6` |
| 11 | `2` | `1\|1\|1` | `2\|2` | `2\|3` | `2\|4` |
| 13 | `1\|1` | `1\|2` | `1\|1\|2` | `1\|1\|3` | `1\|2\|3` |
| 17 | `1\|1` | `1\|2` | `1\|1\|2` | `1\|2\|2` | `1\|1\|2\|2` |
| 19 | `2` | `1\|2` | `2\|2` | `1\|1\|3` | `6` |
| 23 | `2` | `1\|1\|1` | `4` | `2\|3` | `2\|4` |
| 29 | `1\|1` | `1\|1\|1` | `1\|1\|1\|1` | `1\|1\|1\|2` | `1\|2\|3` |
| 31 | `2` | `1\|2` | `2\|2` | `1\|1\|1\|2` | `2\|4` |
| 37 | `1\|1` | `1\|1\|1` | `1\|1\|2` | `1\|1\|3` | `1\|1\|1\|1\|2` |
| 41 | `1\|1` | `1\|2` | `2\|2` | `2\|3` | `1\|2\|3` |
| 43 | `2` | `1\|1\|1` | `4` | `1\|1\|1\|2` | `2\|4` |
| 47 | `2` | `1\|2` | `4` | `1\|1\|1\|2` | `6` |
| 53 | `1\|1` | `1\|1\|1` | `1\|1\|2` | `2\|3` | `1\|1\|1^2\|2` |
| 59 | `2` | `1\|2` | `2\|2` | `1\|2\|2` | `2\|4` |
| 61 | `1\|1` | `1\|2` | `2\|2` | `1\|1\|3` | `1\|1\|1\|3` |
| 67 | `2` | `1\|1\|1` | `4` | `1\|1\|1\|2` | `6` |
| 71 | `2` | `1\|1\|1` | `2\|2` | `1\|2\|2` | `2\|4` |
| 73 | `1\|1` | `1\|2` | `1\|1\|2` | `1\|1\|1\|2` | `1\|2\|3` |
| 79 | `2` | `1\|1\|1` | `2\|2` | `1\|1\|3` | `2\|4` |
| 83 | `2` | `1\|2` | `4` | `1\|1\|1\|2` | `6` |
| 89 | `1\|1` | `1\|2` | `1\|1\|1\|1` | `2\|3` | `1\|1\|1\|3` |
| 97 | `1\|1` | `1\|2` | `1\|1\|2` | `1\|1\|1\|2` | `1\|1\|1\|3` |

By column:

- `char_1 = (x − 1)^2 + 1` has discriminant `−4`. It splits mod `p` exactly when `−1` is a square mod `p`, which by Euler's criterion means `p ≡ 1 (mod 4)`: `p = 5, 13, 17, 29, 37, 41, 53, 61, 73, 89, 97` in the table.
- `char_2 = (x − 2)(x^2 − x + 2)`. The quadratic has discriminant `−7` and splits mod `p ≠ 7` exactly when `−7` is a square mod `p`, which by quadratic reciprocity means `p ≡ 1, 2, 4 (mod 7)`: `p = 11, 23, 29, 37, 43, 53, 67, 71, 79` in the table. At `p = 7` it is the square `(x + 3)^2`.
- `char_3` has Galois group the dihedral group `D_4` of order 8 (computed). Its elements have cycle types `1|1|1|1` (one element), `2|2` (three), `1|1|2` (two) and `4` (two), so the four signatures occur with densities `1/8`, `3/8`, `1/4` and `1/4`. `D_4` has no 3-cycle, so `1|3` never occurs. Over the primes `3 ≤ p < 3000` other than 5, the proportions are `0.105`, `0.379`, `0.262` and `0.255` (computed). At `p = 5` the signature is `1^2|2`.
- `char_5` splits completely mod no prime in the table. At `p = 37` it has four linear factors and a quadratic, at `p = 61, 89, 97` three linear factors and a cubic. The commonest signatures are `2|4` (seven primes) and `6`, irreducible (six primes).

Every repeated factor in the table occurs at a prime dividing the discriminant, as listed in the section *Discriminants: the primes with repeated factors*.

## The Project Euler modulus M = 10^9 + 7

The residues of `M` decide which of the factorizations of the section *Factorization patterns and the Galois group* occur mod `M`:[^exec]

```
M = 1000000007  (prime)
M mod 4 = 3          (so -1 is not a square; char_1 is irreducible)
M mod 7 = 6          (not a square mod 7; char_2's quadratic is irreducible)
M mod 8 = 7          (so 2 is a square mod M)
M - 1 = 2 * 500000003     (500000003 is prime)
M + 1 = 2^3 * 3^2 * 7 * 109^2 * 167
```

`M − 1 = 2q` with `q = 500000003` prime, so every element of `F_M^*` has order 1, 2, `q` or `2q`. The norm of `x` in `F_M[x]/(char_k)` is `2^k`, of order `q`, so `q` divides `per(char_k)` for every `k` ([[castle-cryptography-ring](pages/castle-cryptography-ring.md)], section 8).

`char_k mod M` for `k = 1, …, 7`:

| `k` | degree | factorization mod `M` | orders of the roots |
|---|---|---|---|
| 1 | 2 | irreducible | in `F_{M^2}`, dividing `M^2 − 1 ~ 10^{18}` |
| 2 | 3 | `(x − 2)(x^2 − x + 2)` | `ord_M(2) = q`: `2` is a square mod `M`, so its order divides `q`, which is prime, and `2 ≠ 1` |
| 3 | 4 | irreducible | in `F_{M^4}`, dividing `M^4 − 1 ~ 10^{36}` |
| 4 | 5 | (degree 2)(degree 3) | in `F_{M^2}` and `F_{M^3}` |
| 5 | 6 | (degree 2)(degree 4) | in `F_{M^2}` and `F_{M^4}` |
| 6 | 7 | `(x − r_1)(x − r_2)(x − r_3)` (degree 2)(degree 2) | `r_1 = 958603953`, `r_2 = 708901077`, `r_3 = 332494988`, each of order `q` |
| 7 | 8 | (degree 2)(degree 6) | in `F_{M^2}` and `F_{M^6}` |

So `per(char_6)` mod `M` is the lcm of `q` and the orders of the roots of the two quadratic factors, each dividing `M^2 − 1`.

Upper bounds for `per(char_k)` mod `M`, the lcm of `M^{d_i} − 1` over the factor degrees `d_i`, and the exact periods, the orders of `x` in the census of [[castle-cryptography-ring](pages/castle-cryptography-ring.md)] (section 7):[^per-m]

| `k` | bound | `per(char_k)` |
|---|---|---|
| 1 | `M^2 − 1 ~ 10^{18}` | `4(M − 1) ≈ 2^{31.9}` |
| 2 | `M^2 − 1 ~ 10^{18}` | `(M^2 − 1)/2 ≈ 2^{58.8}` |
| 3 | `M^4 − 1 ~ 10^{36}` | the bound divided by `1,250,000,010`, `≈ 2^{89.4}` |
| 4 | `lcm(M^2 − 1, M^3 − 1) = (M^2 − 1)(M^2 + M + 1) ~ 10^{36}` | the bound divided by `333,333,336`, `≈ 2^{91.3}` |
| 5 | `M^4 − 1 ~ 10^{36}` | the bound divided by `25`, `≈ 2^{114.9}` |
| 6 | `M^2 − 1 ~ 10^{18}` (three linear and two quadratic factors) | `(M^2 − 1)/2 ≈ 2^{58.8}`, the same as `per(char_2)` |
| 7 | `M^6 − 1 ~ 10^{54}` (factors of degree 2 and 6) | `M^6 − 1`, the bound |

`disc(char_k) mod M` is `1000000003, 999999895, 20480, 21037056, 183367454, 996996034, 176533116, 740488628` for `k = 1, …, 8`, and no `disc(char_k)` with `k ≤ 30` is divisible by `M` (computed). So `char_k mod M` is squarefree for every `k ≤ 30`, and its period is the lcm of the orders of its roots.

## What is computed at large p

At `p = 3, 5, 7` the [[mod-p-observatory](pages/mod-p-observatory.md)] lists full periods. At `M` the periods are too large to list, and each of the following is one computation:

- the factorization of `char_k mod M` and the degrees `d_i` of its factors;
- whether a factor is repeated (`M | disc(char_k)`);
- the order of each root `r_i` of a linear factor in `F_M^*`, from the factorization of `M − 1`;
- for a factor of degree `d`, the order of its roots from the factorization of `M^d − 1`. `M^2 − 1 = (M − 1)(M + 1)` is factored in the section *The Project Euler modulus M = 10^9 + 7*, and `M^2 + M + 1 = 6067 · 164826110927971`, `M^2 + 1 = 2 · 5^2 · 58699937 · 340715873`.

The evaluation of the Project Euler targets does not use these periods: Kitamasa's method computes `x^w mod char_k` in `F_M[x]/(char_k)` directly ([[project-euler-502-implementation-notes](pages/project-euler-502-implementation-notes.md)], [[kitamasa](pages/kitamasa.md)]).

## The unit group of R

The ring `R = F_p[x]/(char_k)` is the ring of [[castle-cryptography-ring](pages/castle-cryptography-ring.md)]. When `char_k mod p` is squarefree, `R` is a product of fields and

```
R^*  ≅  ∏_i Z/(p^{d_i} − 1),
```

with one cyclic factor per irreducible factor `g_i` ([[castle-ring-invariant-factors](pages/castle-ring-invariant-factors.md)]), and `per(char_k)` is the lcm of the orders of `x` in the fields `F_p[x]/(g_i)`. A factor `g` of multiplicity `m ≥ 2` contributes `F_{p^d}^* × (1 + (g)/(g^m))`, a unit group times a `p`-group, and the component of `x` in the `p`-group has order `p^{⌈log_p m⌉}` (section *The period from the factorization*).

At `M`: for `k = 2`, `R^* ≅ Z/(M − 1) × Z/(M^2 − 1)`; for `k = 6`, three copies of `Z/(M − 1)` from the linear factors and two of `Z/(M^2 − 1)` from the quadratic factors.

## Appearances in Sources

- [[project-euler-502-castle-factoring](pages/project-euler-502-castle-factoring.md)] - the update of `num_k` and `den_k`, whose reversed denominators are the `char_k`.
- [[oeis-mining-pe502](pages/oeis-mining-pe502.md)] - the characteristic polynomials `char_1` to `char_5` of the rows `P(k, ·)`.

## Related Concepts

- [[mod-p-observatory](pages/mod-p-observatory.md)] - the periods of `A^e(·, h)` mod 3, 5, 7, built from `per(char_k)`.
- [[signed-tower-count](pages/signed-tower-count.md)] - `char_k` over `Z`, its constant term `(−1)^{k+1} 2^k`, and its irreducibility for odd `k`.
- [[chinese-remainder-theorem](pages/chinese-remainder-theorem.md)] - the period of `P(k, ·) mod p` as the order of `x`, since `num_k` and `den_k` are coprime mod every prime.
- [[castle-ring-spectrum](pages/castle-ring-spectrum.md)] - the fibers of `Z[x]/(char_k)` over each prime, and the nilradical of the fat fibers.
- [[castle-ring-invariant-factors](pages/castle-ring-invariant-factors.md)] - the unit group of `R` in invariant-factor form.
- [[castle-cryptography-ring](pages/castle-cryptography-ring.md)] - the ring `R` as a group for discrete-logarithm cryptography.
- [[generating-function-gallery](pages/generating-function-gallery.md)] - the recurrence `char_{k+1} = x^2 char_{k−1} − 2 char_k` and the closed form of the denominators.
- [[mod-9-coset-lift](pages/mod-9-coset-lift.md)] - the repeated factors of `char_k mod 3` and the periods mod 9.
- [[finite-fields](pages/finite-fields.md)] - the orders of elements of `F_{p^d}^*`.
- [[project-euler-502-implementation-notes](pages/project-euler-502-implementation-notes.md)] - the evaluation mod `10^9 + 7` by the recurrence.
- [[hardy-ramanujan-castle](pages/hardy-ramanujan-castle.md)] - the periods `72, 2520, 25200` of the castle counts mod `1729 = 7 · 13 · 19` for `h = 2, 3, 4`, the lcm of the periods mod 7, 13 and 19.

## Footnotes

[^exec]: Verified by execution (Python 3.11 with SymPy, 2026-10-16). `char_k` from `char_0 = x − 1`, `char_1 = x^2 − 2x + 2`, `char_{k+1} = x^2 char_{k−1} − 2 char_k`, checked equal to `x^{k+1} den_k(1/x)` for `k ≤ 9`. The `per(char_k)` table: the order of `x` in `F_p[x]/(char_k)`, computed in the full ring by fast exponentiation and reduction of the exponent `lcm((p^{d_i} − 1) p^{⌈log_p m_i⌉})`; every entry reproduced; `gcd(num_k, den_k) = 1` mod `p` for every cell. The discriminants for `k ≤ 10` and the factorizations of `char_k` modulo each odd prime factor (one linear factor of multiplicity 2 each time). The signature table for `p ≤ 97`, `k ≤ 5`, every cell reproduced. The Galois group of `char_3` (`D_4`, order 8) and the signature proportions over `3 ≤ p < 3000`. The residues and factorizations of `M ± 1`, `M^2 + M + 1`, `M^2 + 1`; the factorizations of `char_k mod M` for `k ≤ 7`; the roots of `char_6 mod M` and their orders; `disc(char_k) mod M` for `k ≤ 30`. The snippet below reproduces the discriminants and the roots of `char_6 mod M`:

    ```python
    import sympy as sp
    x = sp.symbols('x')

    c = {0: x - 1, 1: x**2 - 2*x + 2}
    for k in range(1, 12):
        c[k+1] = sp.expand(x**2 * c[k-1] - 2 * c[k])

    for k in range(1, 11):
        d = int(sp.Poly(c[k], x).discriminant())
        print(k, d, sorted(q for q in sp.factorint(abs(d)) if q > 2))

    M = 10**9 + 7
    for k in range(1, 7):
        for g, m in sp.factor_list(sp.Poly(c[k], x, modulus=M))[1]:
            if sp.Poly(g, x, modulus=M).degree() == 1:
                a, b = [int(v) % M for v in sp.Poly(g, x, modulus=M).all_coeffs()]
                print(f'k={k}: root {(-b * pow(a, -1, M)) % M}')
    ```

[^per-m]: Verified by execution (Python 3.11 with SymPy, 2026-10-25): for `k ≤ 7`, the factor degrees of `char_k mod M`, the bound `lcm(M^{d_i} − 1)` factored through the cyclotomic factors `Φ_e(M)`, and the order of `x` in `F_M[x]/(char_k)` by removing prime factors from the bound; each order is a multiple of `q = 500000003`.
