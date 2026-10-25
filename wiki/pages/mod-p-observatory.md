---
title: Mod-p observatory for A^e(w,h)
category: Analyses
summary: Modulo an odd prime p, the castle count A^e(w, h) is eventually periodic in the width and in the height. In the width its period divides lcm(ord_p(h), ord_p(h−1), per(char_{h−1}), per(char_{h−2})), with equality for p = 3, 5, 7 and h ≤ 5 (computed), where per(char_k) is the lcm of the orders of the irreducible factors of char_k mod p, multiplied by p^{⌈log_p m⌉} for a factor of multiplicity m. char_1 splits mod p exactly when p ≡ 1 (mod 4), and char_2 has a double root mod 7, which multiplies a period by 7. In the height, P(k, L) mod p has period 2·p^{⌈log_p L⌉} in k (L ≤ 11, p ≤ 11, computed).
tags: [analysis, castle, modular-arithmetic, periodicity, automaticity, sympy]
sources: [project-euler-502-castle-factoring, oeis-mining-pe502]
created: 2026-09-14
updated: 2026-10-25
---

# Mod-p observatory for A^e(w,h)

## Overview

For `h ≥ 2` the even-block castle count is[^1]

```
A^e(w, h)  =  [ h^w − (h−1)^w − P(h−1, w) + P(h−2, w) ] / 2,
```

the `F(w, h)` of the problem statement ([[castle-counting-formula](pages/castle-counting-formula.md)]). Each term satisfies a linear recurrence in `w`. Modulo a prime `p`, a sequence that satisfies a linear recurrence of order `d` is eventually periodic, since its state, the last `d` values, takes at most `p^d` values; it is purely periodic when the constant term of the recurrence is nonzero mod `p`, since the step from one state to the next can then be inverted. An eventually periodic sequence is automatic in every base. This page computes the periods for `p = 3, 5, 7` and where they come from; division by 2 needs `p` odd.

## Periods in the width

- `h^w mod p` has period `ord_p(h)`, the multiplicative order of `h` mod `p`, which divides `p − 1` by Fermat's little theorem; the same holds for `(h−1)^w`. When `p` divides the base, the term is 1 at `w = 0` and 0 after.
- `P(k, ·)` satisfies a linear recurrence of order `k + 1` with characteristic polynomial `char_k` ([[signed-tower-count](pages/signed-tower-count.md)]).[^2] Its constant term is `(−1)^{k+1} 2^k`, nonzero mod every odd `p`, so `P(k, ·) mod p` is purely periodic. Its period divides `per(char_k)`, the lcm of the orders of the irreducible factors `g` of `char_k` mod `p`, where the order of `g` is the least `e` with `g` dividing `x^e − 1`, and a factor of multiplicity `m` contributes its order times `p^{⌈log_p m⌉}` (section *The finite-field picture*). For `p = 3, 5, 7` and `k ≤ 4` the period of `P(k, ·)` is `per(char_k)`.[^3]

So in the width, for fixed `h ≥ 2`, the period of `A^e(·, h) mod p` divides

```
lcm( ord_p(h), ord_p(h−1), per(char_{h−1}), per(char_{h−2}) ),
```

leaving out the order of a base divisible by `p`. It equals it for `p = 3, 5, 7` and `h ≤ 5`:[^3]

| p | h=2 | h=3 | h=4 | h=5 |
|---|---|---|---|---|
| 3 | 8 | 8 | 80 | 3120 |
| 5 | 4 | 24 | 120 | 120 |
| 7 | 24 | 168 | 8400 | 1200 |

The sequence in the width is purely periodic unless `h ≡ 0` or `1 (mod p)`, when `h^w` or `(h−1)^w` is 1 at `w = 0` and 0 after.

## Periods in the height

For fixed `w`, `h^w − (h−1)^w` is a polynomial in `h`, which has period `p` mod `p`. For every `L ≥ 4` the recurrence of `P(·, L)` in `k` has characteristic polynomial `(x + 1)^L (x − 1)^{L−2}` (proved on [[signed-tower-k-direction](pages/signed-tower-k-direction.md)]), with the forms `(x − 1)(x + 1)`, `(x + 1)²` and `(x + 1)³` at `L = 1, 2, 3`, so its only roots are `±1`, of orders 1 and 2, and the rest of the period comes from their multiplicities. `P(k, L) mod p` has period `2·p^{⌈log_p L⌉}` in `k`: `2p` while `2 ≤ L ≤ p`, and `2p²` once `p < L ≤ p²`, as `18 = 2·3²` at `L = 4`, `p = 3`, `50 = 2·5²` at `L = 6`, `p = 5`, and `98 = 2·7²` at `L = 8`, `p = 7`. This holds for `L ≤ 11` and `p ∈ {3, 5, 7, 11}` (computed).[^4] The periods of `A^e(w, ·) mod p` in the height:[^4]

| p | w=1 | w=2 | w=3 | w=4 |
|---|---|---|---|---|
| 3 | 2 | 6 | 6 | 18 |
| 5 | 2 | 10 | 10 | 10 |
| 7 | 2 | 14 | 14 | 14 |

At `w = 1` the castle of height `h` is one column with `h` blocks, so `A^e(1, h) = 1` for even `h` and 0 for odd `h`, period 2. At `p = 3`, `w = 4` the period is `18 = 2·3²`, since `L = 4 > 3`.

## The finite-field picture

[[finite-fields](pages/finite-fields.md)] builds `F_5`, `F_49` and the general `F_{p^d}` from the start. Over the rationals, `P(k, L) = Σ_i c_i λ_i^L` is not periodic, since the roots `λ_i` of `char_k` have infinite multiplicative order. Modulo `p` it is:

1. `char_k` factors over `F_p` into irreducible polynomials, and an irreducible factor `g` of degree `d` has its `d` roots in the field `F_{p^d}`.
2. Every nonzero `λ ∈ F_{p^d}` lies in the cyclic group `F_{p^d}^*` of order `p^d − 1`, so `λ^{p^d − 1} = 1` by Lagrange's theorem, and `λ^L` is periodic in `L` with period `ord(λ)`, which divides `p^d − 1`. The roots of `g` are conjugate and have the same order, the order of `g`.
3. For a root `λ` of multiplicity `m`, the solutions of the recurrence include `C(L, j)·λ^{L−j}` for `j < m`. By Lucas's theorem, which computes `C(L, j) mod p` digit by digit in base `p`, `C(L, j) mod p` has period `p^t` in `L`, with `p^t` the least power of `p` greater than `j`. With `j = m − 1` this multiplies the period by `p^{⌈log_p m⌉}`.

*Example.* `char_1 = x² − 2x + 2` has roots `1 ± i`.

- Modulo 5, `−1 = 2²` is a square, so `i = ±2` lies in `F_5`, and the roots `1 ± 2` are 3 and 4, of orders 4 and 2. Their lcm is `per(char_1) = 4` at `p = 5`.
- Modulo 7, `−1` is not a square, so the roots lie in `F_{49}`; their order divides `48`, and it is 24, since `(1 + i)^8 = 16 ≡ 2`, which has order 3 mod 7. So `per(char_1) = 24` at `p = 7`.

`char_2 mod 7` is `(x − 2)(x + 3)²`: the double root `−3` has order 3, so the factor contributes `3·7 = 21`, and `A^e(·, 4) mod 7` has period `8400 = lcm(6, 3, 400, 21)`, seven times `lcm(6, 3, 400, 3) = 1200`.

## char_k mod p: factors and repeated roots

The characteristic polynomials mod 3, 5 and 7:[^3]

| k | char_k mod 3 | char_k mod 5 | char_k mod 7 |
|---|---|---|---|
| 1 | `x²+x−1` | `(x+1)(x+2)` | `x²−2x+2` |
| 2 | `(x+1)(x²−x−1)` | `(x−2)(x²−x+2)` | `(x−2)(x+3)²` |
| 3 | `x⁴−x³−x²+x−1` | `(x−1)²(x²−2x−2)` | `x⁴+3x³+x²−x+1` |
| 4 | `(x−1)²(x³−x−1)` | `(x+1)(x²−2x−1)(x²+x+1)` | `(x−3)(x+1)(x+2)(x²+2x−2)` |

1. **`char_1` splits exactly when `p ≡ 1 (mod 4)`.** Its discriminant is `−4`, so it splits over `F_p` exactly when `−1` is a square mod `p`, which for odd `p` means `p ≡ 1 (mod 4)` (Euler's criterion). It splits at `p = 5` and is irreducible at `p = 3, 7`.
2. **Repeated roots at primes dividing the discriminant.** `char_2 = (x − 2)(x² − x + 2)`, and the quadratic factor has discriminant `−7`, so it has a double root mod 7, `(x + 3)²`. Likewise `char_3` has the double root 1 mod 5 and `char_4` the double root 1 mod 3. Each multiplies the period it enters by `p`, as in `8400 = 1200 × 7`.

`per(char_k)` mod `p`:[^3]

| k | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|
| p=3 | 8 | 8 | 80 | 39 | 728 | 312 |
| p=5 | 4 | 24 | 120 | 12 | 124 | 372 |
| p=7 | 24 | 21 | 400 | 48 | 58824 | 16 |

When `char_k` is irreducible mod `p`, its roots lie in `F_{p^{k+1}}` and `per(char_k)` divides `p^{k+1} − 1`. At `p = 10^9 + 7` the periods can be of order `10^{9(k+1)}`, far beyond enumeration, and the Project Euler evaluation uses the recurrence, not the period ([[castle-count-algorithms](pages/castle-count-algorithms.md)]).

## Verification (SymPy)

```python
import sympy as sp
from math import lcm, ceil, log
x = sp.symbols('x')

def P_table_modp(p, K, W):                       # P[k][L] mod p, column-height DP
    P = [[0]*(W+1) for _ in range(K+1)]
    for k in range(K+1):
        F = [0]*(k+1); F[0] = 1; P[k][0] = 1 % p
        for L in range(1, W+1):
            G = [0]*(k+1)
            for b in range(k+1):
                G[b] = sum(F[a]*(1 if a <= b else (1 if (a-b)%2 == 0 else -1)) for a in range(k+1)) % p
            F = G
            P[k][L] = sum(F[b]*((-1)**b) for b in range(k+1)) % p
    return P

def F_modp(p, w, h, P):                          # A^e(w, h) mod p
    if h <= 1: return 0
    inv2 = (p+1)//2
    return (pow(h, w, p) - pow(h-1, w, p) - P[h-1][w] + P[h-2][w]) * inv2 % p

def find_period(seq, skip=30):                   # eventual period, past a transient prefix
    N = len(seq)
    for T in range(1, (N-skip)//2 + 1):
        if all(seq[n] == seq[n+T] for n in range(skip, N-T)):
            return T

def poly_order(g, p):                            # order of monic g: smallest e with x^e ≡ 1 (mod g)
    d = len(g) - 1
    cur = [1] + [0]*(d-1)
    for e in range(1, p**d):
        top = cur[d-1]
        cur = [(-top*g[0]) % p] + [(cur[i-1] - top*g[i]) % p for i in range(1, d)]
        if cur == [1] + [0]*(d-1):
            return e

def per_char(char, p):                           # lcm of factor orders; g^m adds ×p
    period = 1
    for g, m in sp.factor_list(sp.Poly(char, x, modulus=p))[1]:
        c = sp.Poly(g, x, modulus=p).all_coeffs()[::-1]
        lead = c[-1]
        c = [(v * pow(int(lead), -1, p)) % p for v in c]
        period = lcm(period, poly_order(c, p) * (p**ceil(log(m, p)) if m > 1 else 1))
    return period

def ord_p(a, p):
    e = 1
    while pow(a % p, e, p) != 1: e += 1
    return e

# char_k via the three-term recurrence (see generating-function-gallery)
c = {0: x-1, 1: x**2 - 2*x + 2}
for k in range(1, 7):
    c[k+1] = sp.expand(x**2*c[k-1] - 2*c[k])

# verify: period of F(·,h) == lcm(ord_p(h), ord_p(h-1), per(char_{h-1}), per(char_{h-2}))
p = 7; W = 24000
Pw = P_table_modp(p, 7, W)
for h in range(2, 6):
    seq = [F_modp(p, w, h, Pw) for w in range(W+1)]
    observed = find_period(seq)
    expected = lcm(lcm(ord_p(h, p), ord_p(h-1, p)), lcm(per_char(c[h-1], p), per_char(c[h-2], p)))
    assert observed == expected, (h, observed, expected)
```

## Appearances in Sources

- [[project-euler-502-castle-factoring](pages/project-euler-502-castle-factoring.md)] - the formula for `A^e(w, h)` through `P`, which this page reduces mod `p`.
- [[oeis-mining-pe502](pages/oeis-mining-pe502.md)] - the recurrences of `P(k, ·)` and their characteristic polynomials.

## Related Concepts

- [[signed-tower-count](pages/signed-tower-count.md)] - `char_k` over the rationals and its constant term `(−1)^{k+1} 2^k`, which makes `P(k, ·) mod p` purely periodic.
- [[generating-function-gallery](pages/generating-function-gallery.md)] - the rational functions `num_k/den_k` and the polynomials `char_k`.
- [[recurrence-discovery](pages/recurrence-discovery.md)] - the orders `k + 1` in `L` and `2L − 2` in `k` (computed for `4 ≤ L ≤ 12`, and proved for every `L ≥ 4`).
- [[finite-fields](pages/finite-fields.md)] - the fields `F_{p^d}` in which the roots of `char_k` lie.
- [[castle-count-algorithms](pages/castle-count-algorithms.md)] - the evaluation modulo `10^9 + 7`, which uses the recurrence.
- [[castle-eigenvalue-oeis-crosswalk](pages/castle-eigenvalue-oeis-crosswalk.md)] - the continued fractions of the eigenvalues, and `δ^{p+1} = −1` for a quadratic unit of norm `−1` at a prime `p` inert in its field.
- [[new-sequence-fw3](pages/new-sequence-fw3.md)] - `A^e(w, 3)`, which uses `P(2, w)`, so its period mod 7 contains the factor 7 of `char_2`'s double root.
- [[hardy-ramanujan-castle](pages/hardy-ramanujan-castle.md)] - `A^e(·, h) mod 1729 = 7·13·19`, with periods 72, 2520 and 25200 for `h = 2, 3, 4`, the lcm of the periods mod 7, 13 and 19.
- [[mod-9-equidistribution](pages/mod-9-equidistribution.md)] - the distribution of `A^e(w, h) mod 9` by row, by column and over the cells with `A(w, h) ≤ N`.
- [[mod-9-coset-lift](pages/mod-9-coset-lift.md)] - the periods mod 9, and a proof that `(x ± 1)^3` never divides `char_k mod 3`.
- [[larger-prime-periodicity](pages/larger-prime-periodicity.md)] - primes beyond 7: the primes dividing the discriminants of `char_k`, the factorization patterns at `11 ≤ p ≤ 97`, and the modulus `10^9 + 7`.
- [[castle-ring-invariant-factors](pages/castle-ring-invariant-factors.md)] - the period as the order of `x` in the unit group of `F_p[x]/(char_k)`, with the factor `p` from a repeated root as the `p`-group `1 + (g)/(g^m)`.
- [[castle-ring-spectrum](pages/castle-ring-spectrum.md)] - the factorization of `char_k` mod `p` as the fiber over `p` of `Spec Z[x]/(char_k)`; a repeated factor is a nonzero nilradical of the fiber.
- [[calugareanu-hamburg-exercises-basic-ring-theory](pages/calugareanu-hamburg-exercises-basic-ring-theory.md)] - exercises 14.7 to 14.9, which factor small polynomials over `F_3`, `F_5`, `F_7`, among them `x³ + x + 2 = (x + 1)(x² − x + 2)`, whose quadratic factor is that of `char_2`.
- [[parity-via-roots-of-unity](pages/parity-via-roots-of-unity.md)] - counting castles by block count modulo `m` with roots of unity.

## Footnotes

[^1]: [[project-euler-502-castle-factoring](pages/project-euler-502-castle-factoring.md)] §"The sign of a castle" L123-127 - "\"castle has even total blocks\" is therefore \"tower has an odd number of blocks\", which is the (T-P)/2 term in F(w,h) = (h^w - (h-1)^w - P(h-1,w) + P(h-2,w))/2".
[^2]: [[oeis-mining-pe502](pages/oeis-mining-pe502.md)] `mine-notes.md` §"Vein 1" L31-37 - "The general P(k,·) family is C-finite of order k+1: P(1): x^2 - 2x + 2 ... P(5): x^6 - 6x^5 + 18x^4 - 32x^3 + 48x^2 - 32x + 32 (constant term = (-1)^{k-1} 2^k; leading coeff -(k+1))".
[^3]: Verified by execution (Python 3.11 with SymPy, 2026-10-16): the factorizations of `char_k` mod 3, 5, 7 for `k ≤ 4` and `per(char_k)` for `k ≤ 6`; the periods of the sequences `P(k, ·) mod p` for `k ≤ 4`, equal to `per(char_k)`; the periods of `A^e(·, h) mod p` for `2 ≤ h ≤ 5`, read off 8000, 800 and 20000 terms at `p = 3, 5, 7` and equal to the lcm; pure periodicity from `w = 0` except at `h ≡ 0, 1 (mod p)`. The code in the section *Verification (SymPy)* reruns the case `p = 7`.
[^4]: Verified by execution (Python 3.11, 2026-10-16): the period of `P(k, L) mod p` in `k` equals `2·p^{⌈log_p L⌉}` for `1 ≤ L ≤ 11` and `p ∈ {3, 5, 7, 11}`, from at least `4·2p^{⌈log_p L⌉}` values of `k`; the periods of `A^e(w, ·) mod p` for `w ≤ 4`, from `h < 300`.
