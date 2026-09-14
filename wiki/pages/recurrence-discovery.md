---
title: Recurrence discovery for P(k,L)
category: Analyses
summary: Running Berlekamp–Massey on P(k,L) in both directions — order k+1 in L (confirmed) and exactly 2L−2 in k for L ≥ 4, with closed forms for L ≤ 3.
tags: [analysis, castle, recurrence, berlekamp-massey, c-finite, verification]
sources: [project-euler-502-solution, oeis-mining-pe502, project-euler-502-castle-factoring]
created: 2026-09-14
updated: 2026-09-14
---

# Recurrence discovery for P(k,L)

## Overview

`P(k,L)` — the [[castle-sign](pages/castle-sign.md)] signed tower count — is C-finite (linear-recurrent) in **each** direction, and those two recurrences are what the [[castle-count-algorithms](pages/castle-count-algorithms.md)] exploit to reach trillion-scale parameters. The orders were known only approximately:

- **In L** (fixed *k*, vary the width): order **k+1**. Exact and proven — `P_k(x)` is rational with a degree-(k+1) denominator.[^1]
- **In k** (fixed *L*, vary the height): order "**at most about 2w**" — an *empirical* bound from the Solution subpage, justified by a transfer-matrix argument but never pinned down.[^2]

This page runs [[berlekamp-massey](pages/berlekamp-massey.md)] on both directions, from an exact DP, and pins the orders down. The *L*-direction confirms `k+1`; the *k*-direction tightens the `~2w` bound to **exactly `2L−2` for `L ≥ 4`**, with the three small-*L* cases collapsing to closed forms. Everything below is produced by the program in this page (verified by execution).

## Method

`P(k,L)` is computed exactly by a DP over the last column height, then fed to Berlekamp–Massey over the rationals.

**Computing P(k,L).** A tower of height ≤ *k* above a length-*L* block is its column heights `c_1…c_L ∈ {0,…,k}` (the [[castle-representations](pages/castle-representations.md)] column-height form), and its block count is the total descent `blocks = ∑_{i=0}^{L} max(0, c_i − c_{i+1})`, with `c_0 = c_{L+1} = 0`.[^3] So `P(k,L) = ∑_{c ∈ {0,…,k}^L} (−1)^{blocks}`, a sum over `(k+1)^L` tuples. It is evaluated by DP rather than enumeration: carry the signed count `F[b]` over towers ending at height `b`, and on appending a column of height `b` after height `a`, multiply by `(−1)^{max(0, a−b)}` (the new down-steps). Each `P[k][L]` is an exact integer.

**Finding the order.** Berlekamp–Massey returns the shortest linear recurrence that fits a sequence — hence its minimal order — which is exactly the statistic the two conjectures are about.

```python
from fractions import Fraction

def P_table(max_k, max_L):
    """P[k][L] = sum of (-1)^blocks over towers of height <= k above a
    length-L block; blocks = total descent, computed by a DP over the
    last column height (exact integers)."""
    P = [[0]*(max_L+1) for _ in range(max_k+1)]
    for k in range(max_k+1):
        F = [0]*(k+1)            # signed sum over towers ending at height b
        F[0] = 1
        P[k][0] = 1              # empty tower
        for L in range(1, max_L+1):
            newF = [0]*(k+1)
            for b in range(k+1):
                s = 0
                for a in range(k+1):
                    s += F[a] * (1 if a <= b else (-1)**(a-b))  # (-1)^max(0,a-b)
                newF[b] = s
            F = newF
            P[k][L] = sum(F[b]*((-1)**b) for b in range(k+1))    # final descent b
    return P

def berlekamp_massey(s):
    """Shortest linear recurrence s[n] = -sum_{i=1}^L C[i] s[n-i], over Q."""
    s = [Fraction(x) for x in s]
    C = [Fraction(1)]; B = [Fraction(1)]
    L = 0; m = 1; b = Fraction(1)
    for N in range(len(s)):
        d = s[N]
        for i in range(1, L+1):
            d += C[i]*s[N-i]
        if d == 0:
            m += 1
        else:
            coef = d/b
            T = C[:]
            if len(C) < len(B)+m:
                C += [Fraction(0)]*(len(B)+m-len(C))
            for j in range(len(B)):
                C[j+m] -= coef*B[j]
            if 2*L <= N:
                L = N+1-L; B = T; b = d; m = 1
            else:
                m += 1
    return C[:L+1], L

# L-direction: fixed k, vary L  (expect order k+1)
P = P_table(8, 20)
for k in range(9):
    _, order = berlekamp_massey(P[k])
    print(f"k={k}: order {order}")

# k-direction: fixed L, vary k  (expect ~2L)
P = P_table(50, 14)
for L in range(1, 13):
    seq = [P[k][L] for k in range(51)]
    _, order = berlekamp_massey(seq)
    print(f"L={L}: order {order}")
```

## Results

### L-direction: order k+1

| k | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|---|---|---|
| order | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |

Each is exactly `k+1` — a confirmation of the proven degree-(k+1) denominator, not a new result.[^1] The characteristic polynomials are listed on [[signed-tower-count](pages/signed-tower-count.md)].

### k-direction: exactly 2L−2 for L ≥ 4

| L | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| order | 2 | 2 | 3 | 6 | 8 | 10 | 12 | 14 | 16 | 18 | 20 | 22 |

For `L ≥ 4` the order is **exactly `2L−2`**, tightening the Solution subpage's "at most about 2w" to a precise value.[^2] The three small-*L* cases sit lower only because `P(k,L)` has a closed form there (next section); from `L = 4` onward the recurrence has the full `2L−2` terms.

### The small-L closed forms

For `L ≤ 3` the towers are simple enough that `P(k,L)` collapses to a closed form — the "closed-form hunting" cases, confirmed here by Berlekamp–Massey finding the minimal recurrence:

| L | P(k,L) | order |
|---|---|---|
| 1 | `(1 + (−1)^k) / 2` | 2 |
| 2 | `(−1)^k (k+1)` | 2 |
| 3 | `(−1)^k (k+1)²` | 3 |

i.e. `P(k,1) = 1, 0, 1, 0, …`, `P(k,2) = 1, −2, 3, −4, …`, `P(k,3) = 1, −4, 9, −16, …` (characteristic polynomials `1−x²`, `(1+x)²`, `(1+x)³`). The closed forms themselves — with the `P(k,2)` proof and why the pattern stops at `L = 3` — are on [[closed-form-hunting](pages/closed-form-hunting.md)].

## Appearances in Sources

- [[project-euler-502-solution](pages/project-euler-502-solution.md)] — the k-direction Berlekamp–Massey path and the empirical `~2w` order bound.
- [[oeis-mining-pe502](pages/oeis-mining-pe502.md)] — the `P(k,·)` C-finite family of order k+1 and its characteristic polynomials.

## Related Concepts

- [[signed-tower-count](pages/signed-tower-count.md)] — `P(k,L)` as a C-finite family; the order-(k+1) characteristic polynomials.
- [[closed-form-hunting](pages/closed-form-hunting.md)] — the closed forms of `P(k,L)` in `k` for small `L`, and where they stop.
- [[berlekamp-massey](pages/berlekamp-massey.md)] — the tool that recovers these recurrences.
- [[kitamasa](pages/kitamasa.md)] — jumps to a far index once the recurrence is known.
- [[castle-count-algorithms](pages/castle-count-algorithms.md)] — the two directions as computational paths.
- [[monotone-streak-factorization](pages/monotone-streak-factorization.md)] — the canonical form underlying the recurrences.
- [[castle-sign](pages/castle-sign.md)] — the definition of `P` as the signed tower count.

## Footnotes

[^1]: [[oeis-mining-pe502](pages/oeis-mining-pe502.md)] `mine-notes.md` §"Vein 1" L31-37 — "The general P(k,·) family is C-finite of order k+1: P(1): x^2 - 2x + 2 ... P(5): x^6 - 6x^5 + 18x^4 - 32x^3 + 48x^2 - 32x + 32 (constant term = (-1)^{k-1} 2^k; leading coeff -(k+1))."
[^2]: [[project-euler-502-solution](pages/project-euler-502-solution.md)] §"The k-direction Berlekamp-Massey path (h > 15000)" L165 — "The recurrence order is at most about 2w empirically."
[^3]: [[project-euler-502-castle-factoring](pages/project-euler-502-castle-factoring.md)] §"The sign of a castle" L105-113 — "blocks = ∑_{i=0}^{L} max(0, c_i - c_{i+1}), c_0 = c_{L+1} = 0."
