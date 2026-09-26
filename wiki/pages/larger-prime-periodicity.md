---
title: Larger-prime periodicity of char_k
category: Analyses
summary: The mod-p observatory covers primes p = 3, 5, 7 with periods small enough to enumerate. This page extends the picture to larger primes and to the Project Euler 502 modulus 10^9 + 7. Full periods explode - per(char_k) mod p divides p^{k+1} - 1, so at p = 10^9 + 7 and k = 6 the ceiling is 10^{63} and no computation reaches it. The eigenvalue-order structure persists: char_k factors over F_p by Chebotarev-type patterns predictable from the Galois group of char_k over Q. Discriminants of char_k over Z control where repeated roots appear: disc(char_k) odd prime factors are 7 (at k=2), 5 (k=3), 3 and 107 (k=4), 53 (k=5), 3 and 23 and 643 (k=6), 5449 (k=7) - a sporadic-looking list that determines the "special" primes where the mod-9 observatory's factor-of-p period inflation reappears at a new prime. At 10^9 + 7 specifically: P ≡ 3 (mod 4) makes char_1 irreducible (period divides P^2 - 1 = ~10^18); char_2 has (x - 2) as a linear factor with ord_P(2) = 500000003 (the odd half of P - 1, which is itself prime); char_6 splits with three linear factors (three rational roots mod P), giving three eigenvalue orders each dividing P - 1. The full period at any k >= 1 is beyond enumeration, but the factorization structure is one polynomial-factor-list call.
tags: [analysis, castle, modular-arithmetic, periodicity, large-primes, chebotarev, discriminant, project-euler-502]
sources: [project-euler-502-castle-factoring, oeis-mining-pe502]
created: 2026-09-22
updated: 2026-09-26
---

# Larger-prime periodicity of char_k

The [[mod-p-observatory](pages/mod-p-observatory.md)] catalogues `char_k mod p` factorizations and full periods for `p = 3, 5, 7` and `h <= 5`. That range is where the periods are small enough to enumerate exactly (`58824` at `p = 7, k = 5` is the biggest). Push past `p = 7`, or past `h = 6`, and the periods explode: `per(char_k) mod p` divides `p^{k+1} - 1` when the char poly is irreducible, so at the Project Euler 502 modulus `p = 10^9 + 7` and `k = 6` the ceiling is `(10^9 + 7)^7 - 1 ~ 10^{63}`. No computation reaches it. **The structure persists, though**: `char_k mod p` factors into irreducibles by Chebotarev-type patterns, each irreducible of degree `d` contributes an eigenvalue with order dividing `p^d - 1`, and repeated roots appear at exactly the primes dividing `disc(char_k)`. This page tabulates that structure for larger `p` and works out the `10^9 + 7` case explicitly.

## The two limits: period explosion and structural persistence

For `char_k mod p`:

- If `char_k` is irreducible over `F_p`, its unique irreducible factor has degree `k + 1`, and `per(char_k) mod p = ord(root)` where the root lives in `F_{p^{k+1}}^*`. The order divides `p^{k+1} - 1`. **Ceiling grows as `p^{k+1}`**, exponential in both `p` and `k`.
- If `char_k` splits into irreducibles of degrees `d_1, ..., d_r`, the period is `lcm(ord(root_1), ..., ord(root_r))`, each order dividing its `p^{d_i} - 1`.
- If some irreducible factor `g` has multiplicity `m > 1`, the period picks up an extra factor `p^{ceil(log_p m)}` (the "multiplicity-inflation" rule). Repeated roots occur exactly when `p | disc(char_k)`. The factor is the nilradical of `F_p[x]/(char_k)`: the rule is checked as an exact equality at seven discriminant-zero primes on [[castle-ring-spectrum](pages/castle-ring-spectrum.md)] §3, but its exactness (rather than divisibility) is not proved.

`per(char_k) mod p` for larger primes, tabulated:[^exec]

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

Periods jump erratically. What has clean structure is the **factorization pattern**, which is what determines them.

## Discriminants of char_k: the "special" primes

Repeated roots in `char_k mod p` occur iff `p | disc(char_k)`. Over `Z`, the discriminants are integers with a large power-of-2 factor plus a small odd part:[^exec]

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

**Every one of these odd primes is a place where `char_k mod p` acquires a repeated root**, driving one factor of `p` into the mod-`p` period. Empirically the multiplicity of the repeated factor is always 2 in these cases (the disc primes appear to first order, not to a square). Notable hits:

- **`p = 7` at `k = 2`**: `(x + 3)^2` in `char_2 mod 7`; drives `F(w, 4) mod 7` to period `8400 = 1200 * 7` on the [[mod-p-observatory](pages/mod-p-observatory.md)].
- **`p = 5` at `k = 3`**: `(x - 1)^2` in `char_3 mod 5`.
- **`p = 3` at `k = 4, 6, ...`**: the `k mod 12 in {4, 6}` pattern proved in [[mod-9-coset-lift](pages/mod-9-coset-lift.md)].
- **`p = 5` at `k = 10`**: the disc prime returns for the second time.

The odd part of the discriminant grows fast: `107, 53, 23·643, 5449, 257·49697, 37·14153, 5·19·4409·15121` for `k = 4..10`. Above `k ~ 4` these are "sporadic-looking" - individual primes that happen to divide `disc(char_k)` with no small-prime pattern. **Whether `disc(char_k)` ever hits `10^9 + 7`** for some `k` is a coincidence question; for `k <= 10`, the answer is no (see the `10^9 + 7` section below).

## Splitting patterns follow Chebotarev

Factorization signatures of `char_k mod p` for `k = 1..5`, `p in {3..97}`:[^exec]

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

Read the columns:

- **char_1** (deg 2, disc `-4`) splits iff `p ≡ 1 (mod 4)` (`p in {5, 13, 17, 29, 37, 41, 53, 61, 73, 89, 97}` here) and is irreducible otherwise. Quadratic reciprocity on `-4`.
- **char_2 = (x - 2)(x^2 - x + 2)** always has the linear factor `(x - 2)`. The quadratic has discriminant `-7`, so splits iff `-7` is a QR mod `p`, i.e. iff `p` is a QR mod 7 (up to sign). Hits `1|1|1` at `p in {11, 23, 29, 37, 43, 53, 67, 71, 79}` (QR of 7); hits `1|2` at the rest. Repeated `1|1^2` only at `p = 7` (disc prime).
- **char_3** (deg 4, Galois group appears to be a transitive subgroup of `S_4`): factor signatures include `4` (irreducible), `2|2` (two conjugate quadratics), `1|1|2`, `1|1|1|1` (fully split - a small density), and the disc-prime case `1^2|2` at `p = 5`. Chebotarev density theorem says each pattern has a limiting frequency determined by the cycle types in the Galois group.
- **char_5** rarely fully splits: through the table only `p = 37` and `p = 61, 89, 97` hit `1|1|1|1|2` or `1|1|1|3` (four or five linear factors). The default is `2|4` or `6` (irreducible).

The **repeated-factor rows** are highlighted by the caret notation `d^m` where `m > 1`. Every repeated factor in the table matches a disc-prime listed above. The rest of the table is squarefree, and the periods are computable factor-by-factor.

## The `10^9 + 7` case

Set `P = 10^9 + 7`. This is a Mersenne-adjacent prime widely used in competitive programming and as the mod for Project Euler 502. Its small-prime residues shape which `char_k mod P` splittings occur:[^exec]

```
P = 1000000007  (prime)
P mod 4 = 3          (so -1 is a non-residue; char_1 is irreducible)
P mod 7 = 6          (a non-residue of 7; char_2's quadratic is irreducible)
P - 1 = 2 * 500000003     (500000003 is prime)
P + 1 = 2^3 * 3^2 * 7 * 109^2 * 167
```

The factorization of `P - 1` is remarkably clean: `P - 1 = 2 * q` for a single big odd prime `q = 500000003`. Every element of `F_P^*` has order dividing `2 * q`, and only orders in `{1, 2, q, 2q}` are possible. This makes eigenvalue-order computations for linear factors of `char_k mod P` trivial once the root is known.

**`char_k mod P` factorizations for `k = 1..6`:**

| `k` | deg | factorization mod `P` | linear-root eigenvalue orders |
|---|---|---|---|
| 1 | 2 | irreducible (deg 2) | root in `F_{P^2}`, order divides `P^2 - 1 ~ 10^{18}` |
| 2 | 3 | `(x - 2) * (x^2 - x + 2)` | `ord_P(2) = 500000003 = q` (`2` is a QR of `P`, so ord divides `q`, and `q` is prime, so `ord in {1, q}`; not 1, so `q`) |
| 3 | 4 | irreducible (deg 4) | root in `F_{P^4}`, order divides `P^4 - 1 ~ 10^{36}` |
| 4 | 5 | (deg 2) `*` (deg 3) | root in `F_{P^2}` (order `\| P^2 - 1`); root in `F_{P^3}` (order `\| P^3 - 1`) |
| 5 | 6 | (deg 2) `*` (deg 4) | roots in `F_{P^2}` and `F_{P^4}` |
| 6 | 7 | `(x - r_1)(x - r_2)(x - r_3) * (deg 2) * (deg 2)` | **three linear factors** with roots `r_1 = 958603953, r_2 = 708901077, r_3 = 332494988`; each order divides `P - 1 = 2q` |

The `k = 6` line is the surprise: `char_6 mod P` picks up **three linear factors**, i.e. three rational roots mod `P`. Their orders in `F_P^*` are each in `{1, 2, q, 2q}` and computable by one exponentiation per root. Combined with the two quadratic factors (each contributing a root in `F_{P^2}` of order dividing `P^2 - 1`), `per(char_6) mod P` is the lcm of five eigenvalue orders, each computable.

**Full-period ceiling by k:**

| `k` | max `per(char_k) mod P` (from largest-degree factor) |
|---|---|
| 1 | `P^2 - 1 ~ 10^{18}` |
| 2 | `P^2 - 1 ~ 10^{18}` |
| 3 | `P^4 - 1 ~ 10^{36}` |
| 4 | `P^3 - 1 ~ 10^{27}` |
| 5 | `P^4 - 1 ~ 10^{36}` |
| 6 | `P^2 - 1 ~ 10^{18}` (due to 3 linear + 2 quadratic factors) |
| 7 | `P^{d_max} - 1`, up to `P^8 - 1 ~ 10^{72}` |

**Does `P` divide any `disc(char_k)` for `k <= 10`?** Checking directly: `disc(char_k) mod P` is `1000000003, 999999895, 20480, 21037056, 183367454, 996996034, 176533116, 740488628, ...` for `k = 1..8` - none zero. **No `char_k` for `k <= 10` has a repeated factor mod `P`**, so every factorization is squarefree and the period is a clean lcm of eigenvalue orders. The full period at each `k` is beyond enumeration but the factorization structure is one polynomial-`factor_list` call, and each individual eigenvalue order is computable from the standard discrete-log-in-`F_{P^d}^*` machinery.

## What can be computed vs. what can be enumerated

The mod-p observatory at `p = 3, 5, 7` printed full periods (up to `58824`) as one column of a table. At `p = 10^9 + 7` the analogous table is empty - the periods are astronomical - but the following is one call each:

- `char_k mod P` factorization (SymPy `factor_list`, milliseconds).
- Degrees `d_1, ..., d_r` of the irreducible factors.
- Repeated-factor detection (compare degree sum to `k + 1`).
- For each linear factor `(x - r_i)`, the order of `r_i` in `F_P^*` when `P - 1` has known factorization.
- For each degree-`d` factor, the order divides `p^d - 1`; when `p^d - 1` is factorable (rare for `p = 10^9 + 7, d >= 2`, since `p^2 - 1 = 10^{18}` has no obvious factor structure past `(P-1)(P+1)`), the order is computable by discrete-log.

**The "full period" itself is never computed at `10^9 + 7`.** The [[project-euler-502-implementation-notes](pages/project-euler-502-implementation-notes.md)] pipeline never needs it - it uses Kitamasa evaluation to jump directly to `x^w mod char_k` in `F_P[x] / char_k`, sidestepping period enumeration entirely.

## Connection to castle cryptography

The [[castle-cryptography-ring](pages/castle-cryptography-ring.md)] page uses `F_p[x] / char_k` as the cryptographic ring and computes with elements of order equal to the mod-`p` period. The [[castle-ring-invariant-factors](pages/castle-ring-invariant-factors.md)] decomposition reads:

```
R^* = (F_p[x] / char_k)^*  =  prod_i Z / (p^{d_i} - 1),
```

with one factor per irreducible piece of `char_k mod p`. The invariant-factor decomposition of `R^*` and the mod-`p` period structure of `char_k` are the same theorem stated in two languages: **the period is the order of `x` in `R^*`**, and the order of `x` is `lcm(ord_i(x))` across the invariant factors. When `char_k mod p` has a repeated factor at a discriminant prime, the ring picks up a local `p`-group `U = 1 + (g) / (g)^m` beside the field factor, and `x`'s order in `U` is `p` (for multiplicity 2) - reproducing the multiplicity-inflation rule of [[mod-p-observatory](pages/mod-p-observatory.md)].

At `10^9 + 7`, this reading says the cryptographic ring `R = F_P[x] / char_k` has invariant-factor group `prod_i Z / (P^{d_i} - 1)`, with `d_i` read directly from the mod-`P` factorization: at `k = 2`, `R^* = Z/(P - 1) * Z/(P^2 - 1)`; at `k = 6`, five factors including three `Z/(P - 1)` copies from the linear roots and two `Z/(P^2 - 1)` from the quadratics.

## Appearances in Sources

- [[project-euler-502-castle-factoring](pages/project-euler-502-castle-factoring.md)] - the closed form and the `char_k` machinery.
- [[oeis-mining-pe502](pages/oeis-mining-pe502.md)] - the `P(k, .)` C-finite family whose characteristic polynomials are studied here.

## Related Concepts

- [[mod-p-observatory](pages/mod-p-observatory.md)] - the small-prime observatory this page extends; `p = 3, 5, 7` fully enumerated periods.
- [[castle-cryptography-ring](pages/castle-cryptography-ring.md)] - the ring `F_p[x] / char_k` and its computational cost model.
- [[castle-ring-invariant-factors](pages/castle-ring-invariant-factors.md)] - `R^* = prod Z / (p^{d_i} - 1)`, the algebraic form of the eigenvalue-order lcm.
- [[signed-tower-count](pages/signed-tower-count.md)] - `char_k` over `Z` and the constant term `(-1)^{k-1} 2^k` guaranteeing pure periodicity mod every odd prime.
- [[generating-function-gallery](pages/generating-function-gallery.md)] - the `char_k` recurrence and their explicit forms.
- [[mod-9-coset-lift](pages/mod-9-coset-lift.md)] - the mod-9 (composite) case; `p = 3` extended to `p = 9` by the same multiplicity-inflation rule.
- [[project-euler-502-implementation-notes](pages/project-euler-502-implementation-notes.md)] - the mod-`10^9 + 7` pipeline whose C-finiteness (not its period) is what's exploited.
- [[hardy-ramanujan-castle](pages/hardy-ramanujan-castle.md)] - a composite modulus example: `1729 = 7 * 13 * 19` periods `72, 2520, 25200` for `h = 2, 3, 4`, the lcm of the three prime-mod periods.
- [[finite-fields](pages/finite-fields.md)] - `F_{p^d}^*` orders are this page's central mechanism; the pedagogy hub for exactly the eigenvalue-order arithmetic used here.
- [[castle-ring-spectrum](pages/castle-ring-spectrum.md)] - the fibers over each `p` as points of `Spec Z[x]/(char_k)`, and the inflation rule split into reduced part and nilradical.

## Footnotes

[^exec]: Verified by execution (2026-09-22), Python 3 with SymPy 1.14. **`char_k` construction**: three-term recurrence `char_0 = x - 1, char_1 = x^2 - 2x + 2, char_{k+1} = x^2 char_{k-1} - 2 char_k`; verified against [[generating-function-gallery](pages/generating-function-gallery.md)]. **Discriminants**: `sp.Poly(char_k, x).discriminant()` for `k = 1..10`, factored with `sp.factorint`; odd-prime parts read directly. **Factor signatures**: `sp.factor_list(sp.Poly(char_k, x, modulus=p))[1]` for each `p in {3..97}` and `k in {1..5}`, degree-of-each-irreducible-factor recorded as a sorted multiset. **`per(char_k) mod p` table**: for each irreducible factor `g` of degree `d`, order of `x mod g` computed by iterating the linear recurrence in state `(F_p)^d` until return to `x^0 = 1`; total `per = lcm` of factor orders, with `* p^{ceil(log_p m)}` for any multiplicity-`m` repeated factor. Runs in seconds up to `p = 97, k = 6`; the biggest period computed is `205346960` at `(p, k) = (29, 6)`. **`10^9 + 7` factorization**: `sp.factor_list(..., modulus=10**9 + 7)` for `k = 1..6`; `char_6 mod P` produced three linear factors with roots computed as `-c_0 * pow(c_1, -1, P) mod P`. **`ord_P(2)` computation**: `pow(2, (P-1)/2, P) = 1`, so `ord | (P-1)/2 = 500000003`; since `500000003` is prime, `ord in {1, 500000003}`; `pow(2, 1, P) = 2 != 1`, so `ord = 500000003`. **Disc-mod-P table**: `int(sp.Poly(char_k, x).discriminant()) % P` for `k = 1..8`; no `k` in that range hits zero.

    ```python
    import sympy as sp
    from math import lcm, ceil, log
    x = sp.symbols('x')

    # char_k recurrence
    c = {0: x - 1, 1: x**2 - 2*x + 2}
    for k in range(1, 12):
        c[k+1] = sp.expand(x**2 * c[k-1] - 2 * c[k])

    # Discriminants and their odd prime factors
    for k in range(1, 11):
        d = int(sp.Poly(c[k], x).discriminant())
        odd_primes = sorted(q for q in sp.factorint(abs(d)) if q > 2)
        print(k, d, odd_primes)

    # char_k mod P factorization signature
    def factor_signature(char_poly, p):
        factors = sp.factor_list(sp.Poly(char_poly, x, modulus=p))[1]
        return sorted((sp.Poly(g, x, modulus=p).degree(), m) for g, m in factors)

    # 10^9 + 7 case: which k give linear factors?
    P = 10**9 + 7
    for k in range(1, 7):
        factors = sp.factor_list(sp.Poly(c[k], x, modulus=P))[1]
        for g, m in factors:
            if sp.Poly(g, x, modulus=P).degree() == 1:
                coeffs = [int(v) % P for v in sp.Poly(g, x, modulus=P).all_coeffs()]
                root = (-coeffs[1] * pow(coeffs[0], -1, P)) % P
                print(f'k={k}: rational root {root}')
    ```
