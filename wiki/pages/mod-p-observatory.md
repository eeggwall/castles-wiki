---
title: Mod-p observatory for F(w,h)
category: Analyses
summary: F(w,h) mod p is eventually periodic in each direction, the period being the lcm of the eigenvalue orders — char_k mod p splits by quadratic reciprocity and has repeated roots at discriminant-zero primes.
tags: [analysis, castle, modular-arithmetic, periodicity, automaticity, sympy]
sources: [project-euler-502-castle-factoring, oeis-mining-pe502]
created: 2026-09-14
updated: 2026-09-19
---

# Mod-p observatory for F(w,h)

## Overview

`F(w,h) = [h^w − (h−1)^w − P(h−1,w) + P(h−2,w)]/2` is a sum of periodic and C-finite terms.[^1] **Modulo a prime p, every C-finite sequence is eventually periodic** — its rational generating function over `F_p` is algebraic, hence (Christol) p-automatic. So "automaticity" here is not an extra condition: it *is* periodicity, and the observatory catalogues the periods and their origin.

## The mechanism: period = lcm of eigenvalue orders

- `h^w mod p` has period `ord_p(h) | p−1` (Fermat); `(h−1)^w` likewise.
- `P(k,·) mod p` is C-finite of order `k+1` with characteristic polynomial `char_k`; since `char_k(0) = (−1)^{k−1}2^k ≢ 0` (odd p), it is **purely periodic**, with period `per(char_k)` = the lcm of the orders of `char_k`'s irreducible factors over `F_p` — a repeated factor `g^m` contributes an extra factor `p` (the `n^{m−1}λ^n` term has period `p`).

So in the width direction (fixed `h`):

```
period_w(F(·,h)) = lcm( ord_p(h), ord_p(h−1), per(char_{h−1}), per(char_{h−2}) ).
```

Verified exactly for `p = 3, 5, 7`, `h ≤ 5` (all `OK`):

| p | h=2 | h=3 | h=4 | h=5 |
|---|---|---|---|---|
| 3 | 8 | 8 | 80 | 3120 |
| 5 | 4 | 24 | 120 | 120 |
| 7 | 24 | 168 | 8400 | 1200 |

The width direction has a **transient** only when `h ≡ 0, 1 (mod p)`: then `h^w` (or `(h−1)^w`) is `1` at `w=0` and `0` after. Otherwise it is purely periodic from the first term.

In the height direction (fixed `w`), `F(w,h)` is `2p`-periodic for small `w` — the `(−1)^k` factor contributes period 2 and the polynomial-in-`k` factor contributes period p:

| p | w=1 | w=2 | w=3 | w=4 |
|---|---|---|---|---|
| 3 | 2 | 6 | 6 | 18 |
| 5 | 2 | 10 | 10 | 10 |
| 7 | 2 | 14 | 14 | 14 |

(`p=3, w=4` is `6p = 18`, not `2p`, because the k-direction characteristic polynomial has a repeated root mod 3 — the same doubling that appears below.)

The repeated root is exact, not a mod-3 accident: the k-direction characteristic polynomial of `P(·,L)` is `(x+1)^L (x−1)^{L−2}` over `Z` ([[convergents-oeis-crosswalk](pages/convergents-oeis-crosswalk.md)]), so the only eigenvalues are `±1` (orders 1 and 2) and the whole period comes from the multiplicities. `P(k,L) mod p` has period `2·p^{⌈log_p L⌉}` in `k`: `2p` while `L ≤ p`, jumping to `2p²` once `L > p` - `18 = 2·3²` at `L = 4, p = 3`, `50 = 2·5²` at `L = 6, p = 5`, `98 = 2·7²` at `L = 8, p = 7` (verified for `L ≤ 11`, `p ∈ {3, 5, 7, 11}`). The `18` in the table is the `L = w = 4 > 3` case.

## The finite-field connection

*A from-scratch, pedagogical build-up of this picture — F_5, F_49, and the general F_{p^d} — is on [[finite-fields](pages/finite-fields.md)].*

Why does "period = lcm of eigenvalue orders" hold? It is the standard finite-field picture of a linear recurrence. Over ℚ, `P(k,L) = Σ c_i λ_i^L` is *aperiodic* — the eigenvalues `λ_i` have infinite order. Reducing mod p is what tames it:

1. `char_k` factors over `F_p` into irreducibles; an irreducible factor `g` of degree `d` has its `d` roots in the finite field `F_{p^d}` (the unique degree-`d` extension).
2. Every nonzero `λ ∈ F_{p^d}` lies in the **cyclic** group `F_{p^d}^*` of order `p^d − 1`, so `λ^{p^d − 1} = 1` (Lagrange) and `λ^L` is periodic in `L` with period `ord(λ) | p^d − 1`.
3. Hence the whole sequence is periodic, with period the lcm of the root orders — each order dividing some `p^d − 1`.

**Worked example.** `char_1 = x²−2x+2` has roots `1 ± i`.

- **mod 5**, `−1` is a square (`2² = −1`), so `i = ±2 ∈ F_5` and the roots `1±2 = 3, 4` are plain elements of `F_5`, with orders `ord_5(3) = 4` and `ord_5(4) = 2`, lcm `4` — matching `per(char_1) mod 5 = 4`.
- **mod 7**, `−1` is not a square, so `i ∉ F_7` and the roots live in `F_{7²}`; their order divides `7² − 1 = 48` and is in fact `24` — matching `per(char_1) mod 7 = 24`.

A repeated root `g^m` adds a polynomial part `n^{m−1}λ^n` to the solution, and `n^{m−1} mod p` has period `p^{⌈log_p m⌉}` — which is why a double root multiplies the period by `p` (`char_2 mod 7`'s `(x+3)²`, hence `8400 = 1200 × 7`).

This is also the finite-field reason **automaticity is automatic** here: a finite multiplicative group gives finite orders, hence periodicity, hence (Christol) p-automaticity.

## char_k mod p: splitting and repeated roots

The characteristic polynomials reduce with clean structure:

| k | char_k mod 3 | char_k mod 5 | char_k mod 7 |
|---|---|---|---|
| 1 | `x²+x−1` | `(x+1)(x+2)` | `x²−2x+2` |
| 2 | `(x+1)(x²−x−1)` | `(x−2)(x²−x+2)` | `(x−2)(x+3)²` |
| 3 | `x⁴−x³−x²+x−1` | `(x−1)²(x²−2x−2)` | `x⁴+3x³+x²−x+1` |
| 4 | `(x−1)²(x³−x−1)` | `(x+1)(x²−2x−1)(x²+x+1)` | `(x−3)(x+1)(x+2)(x²+2x−2)` |

Two clean facts:

1. **Splitting is quadratic reciprocity.** `char_1 = x²−2x+2` has discriminant `−4`, so it splits over `F_p` iff `−1` is a square mod p, i.e. `p ≡ 1 (mod 4)` — the eigenvalues `1±i` live in `F_p` exactly when `i = √(−1)` does. It splits for `p = 5`, stays irreducible for `p = 3, 7`.
2. **Repeated roots at discriminant-zero primes.** `char_2 = (x−2)(x²−x+2)`, whose quadratic has discriminant `−7`, has a double root mod 7 (since `−7 ≡ 0`): `(x+3)²`. These repeated roots push a period up by a factor of p — e.g. `F(w,4) mod 7` has period `8400 = 1200 × 7`, the `7` coming from `char_2`'s double root.

`per(char_k) mod p` — the lcm of factor orders:

| k | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|
| p=3 | 8 | 8 | 80 | 39 | 728 | 312 |
| p=5 | 4 | 24 | 120 | 12 | 124 | 372 |
| p=7 | 24 | 21 | 400 | 48 | 58824 | 16 |

For irreducible `char_k` of degree `k+1` the roots live in `F_{p^{k+1}}`, so `per(char_k)` divides `p^{k+1}−1` — the periods grow like a power of p in the height (this is why the `10^9+7` observatory can never print a full period, only the eigenvalue orders).

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

def F_modp(p, w, h, P):
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

- [[project-euler-502-castle-factoring](pages/project-euler-502-castle-factoring.md)] — the `F(w,h)` closed form and the `P`/`char_k` machinery reduced here.
- [[oeis-mining-pe502](pages/oeis-mining-pe502.md)] — the `P(k,·)` C-finite family and its characteristic polynomials.

## Related Concepts

- [[generating-function-gallery](pages/generating-function-gallery.md)] — the `char_k` polynomials whose roots (reduced mod p) set the periods.
- [[recurrence-discovery](pages/recurrence-discovery.md)] — the orders `k+1` (L) and `2L−2` (k) that bound `per(char_k)`.
- [[signed-tower-count](pages/signed-tower-count.md)] — `char_k` over ℚ and the `(−1)^{k−1}2^k` constant term that guarantees pure periodicity.
- [[project-euler-502-implementation-notes](pages/project-euler-502-implementation-notes.md)] — the mod-`10^9+7` path whose C-finiteness (not its period) is what's exploited.
- [[convergents-oeis-crosswalk](pages/convergents-oeis-crosswalk.md)] - the real-number twin of this page: continued-fraction periods of the eigenvalues, the norm-`−1` signature (`δ^{p+1} = −1` at inert primes) read on both sides, and the `2·p^{⌈log_p L⌉}` k-direction period.
- [[new-sequence-fw3](pages/new-sequence-fw3.md)] — `F(w,3)`, whose char poly contains `x² − x + 2` (discriminant `−7`): its period mod 7 inherits the `(x+3)²` double root above.

## Footnotes

[^1]: [[project-euler-502-castle-factoring](pages/project-euler-502-castle-factoring.md)] §"The sign of a castle" L123-127 — "'castle has even total blocks' ... F(w,h) = (h^w - (h-1)^w - P(h-1,w) + P(h-2,w))/2."
[^2]: [[oeis-mining-pe502](pages/oeis-mining-pe502.md)] `mine-notes.md` §"Vein 1" L31-37 — "The general P(k,·) family is C-finite of order k+1: P(1): x^2 - 2x + 2 ... (constant term = (-1)^{k-1} 2^k; leading coeff -(k+1))."
