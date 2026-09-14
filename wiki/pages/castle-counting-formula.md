---
title: Castle counting formula
category: Analyses
summary: The closed form F(w,h) = [h^w − (h−1)^w − P(h−1,w) + P(h−2,w)]/2, from the unsigned tower count (k+1)^L and the signed count P_k; verified on all checkpoints.
tags: [analysis, castle, generating-functions, closed-form, dyck]
sources: [project-euler-502-representations]
created: 2026-09-13
updated: 2026-09-13
---

# Castle counting formula

## Overview

This is the closed-form derivation of the [[castle-counting-function](pages/castle-counting-function.md)] `F(w,h)`, read off the [[generalized-dyck-grammar](pages/generalized-dyck-grammar.md)] for castles. It replaces enumeration with a direct count and reproduces the problem's known checkpoints exactly. It has two ingredients — an **unsigned** tower count and a **signed** tower count that encodes the even-block rule — combined into the formula for `F(w,h)`.

## Unsigned count: T(k,L) = (k+1)^L

Mark each `R` step by a variable *x*, so a tower of *L* columns is worth `x^L`. Writing `E_k(x)` for the generating function of towers of height at most *k*, the grammar `E_k → empty | R E_k | U V D (empty | R E_k)` reads off term-by-term as:[^1]

```
E_k = 1 + x·E_k + (E_{k−1} − 1)(1 + x·E_k)
```

where `1` is the empty tower, `x·E_k` a gap column then the rest, `(E_{k−1} − 1)` the nonempty interior tower `V`, and `(1 + x·E_k)` the "stop, or gap and continue" tail; the vertical `U`/`D` add no *x*.[^1] Collecting terms gives `E_k = E_{k−1} / (1 − x·E_{k−1})`, with base case `E_0 = 1/(1−x)` (a height-0 skyline is any number of empty columns). Unwinding the recurrence:[^2]

```
E_k = 1 / (1 − (k+1)x)      ⟹      T(k,L) = (k+1)^L
```

So the number of towers of height at most *k* above a length-*L* block is `(k+1)^L` — the same closed form used on the Solution subpage, here derived straight from the grammar.[^2]

## Signed count: the even-block rule as a sign

The even-block rule is the hard constraint, and it enters as a **sign**: weight each block — that is, each `D` — by −1. Since a peak `U V D` adds one block on top of `V`, it flips the sign of everything inside it. With `P_k` the signed tower generating function, the grammar picks up a single minus on the peak production, giving:[^3]

```
P_k = 1 + x·P_k − (P_{k−1} − 1)(1 + x·P_k)
```

which solves to the rational recurrence (with `P_0 = 1/(1−x)`):[^4]

```
P_k = (2 − P_{k−1}) / (1 − 2x + x·P_{k−1})
```

Writing `P_k = num_k / den_k`, this is a polynomial update:[^5]

```
num_k = 2·den_{k−1} − num_{k−1}
den_k = den_{k−1}·(1 − 2x) + x·num_{k−1}
```

For fixed *k*, `P_k` is rational with denominator of degree *k*+1, so `P(k,L)` obeys an order-(*k*+1) linear recurrence in *L*. Two small cases:[^6]

- *k*=1: `P(1,L) = 2P(1,L−1) − 2P(1,L−2)`, closed form `P(1,L) = Re((1+i)^{L+1})`.
- *k*=2: `P(2,L) = 3P(2,L−1) − 4P(2,L−2) + 4P(2,L−3)`.

## The main formula

A full castle is `U (tower) D`, so its block count is the tower's block count plus one (the bottom block); **even total blocks means an odd number of blocks in the tower.**[^7] Since `T(h−1,w) = h^w` counts towers of height ≤ *h*−1 of any parity and `P(h−1,w)` is the signed version, `(T − P)/2` counts towers of *odd* block count. That expression `(h^w − P(h−1,w))/2` still includes every height from 0 to *h*−1, so subtracting the height ≤ *h*−2 case forces height exactly *h*:[^8]

```
F(w,h) = [ h^w − (h−1)^w − P(h−1,w) + P(h−2,w) ] / 2
```

## Verification

The source gives Python that builds `P(k,L)` as the coefficient of `x^L` in `num_k/den_k` (via the polynomial recurrence above) and evaluates `F(w,h)`.[^9] Re-running it during ingest reproduces all three problem checkpoints exactly:

```
F(4,2)   = 10
F(13,10) = 3729050610636
F(10,13) = 37959702514
```

matching the values on [[castle-counting-function](pages/castle-counting-function.md)].[^9]

## Appearances in Sources

- [[project-euler-502-representations](pages/project-euler-502-representations.md)] — derives the unsigned count `(k+1)^L`, the signed count `P_k`, and the closed form for `F(w,h)`, with verifying Python.

## Related Concepts

- [[castle-counting-function](pages/castle-counting-function.md)] — the function `F(w,h)` this formula computes.
- [[generalized-dyck-grammar](pages/generalized-dyck-grammar.md)] — the grammar the generating functions are read off.
- [[generating-functions](pages/generating-functions.md)] — the method embodied here.
- [[convex-castle](pages/convex-castle.md)] — the enumeration-side backbone, complementary to this counting-side formula.

## Footnotes

[^1]: [[project-euler-502-representations](pages/project-euler-502-representations.md)] §"Unsigned count" L286-292 — "Let x mark one R step ... E_k = 1 + x E_k + (E_{k-1} - 1)(1 + x E_k)" with the term-by-term reading (empty, gap, nonempty interior V, tail; vertical U/D add no x).
[^2]: [[project-euler-502-representations](pages/project-euler-502-representations.md)] §"Unsigned count" L297-309 — "E_k = E_{k-1}/(1 - x E_{k-1})", base "E_0 ... 1/(1-x)", unwinding to "E_k = 1/(1-(k+1)x)" and "T(k,L) = (k+1)^L", "the closed form already on Project Euler/502/Solution."
[^3]: [[project-euler-502-representations](pages/project-euler-502-representations.md)] §"Signed count" L316-329 — "The even-block rule is the hard constraint, and it enters as a sign. Weight each block, that is each D, by -1 ... one minus sign on the peak ... P_k = 1 + x P_k - (P_{k-1} - 1)(1 + x P_k)".
[^4]: [[project-euler-502-representations](pages/project-euler-502-representations.md)] §"Signed count" L333 — "P_k = (2 - P_{k-1})/(1 - 2x + x P_{k-1}), P_0 = 1/(1-x)".
[^5]: [[project-euler-502-representations](pages/project-euler-502-representations.md)] §"Signed count" L338-339 — "num_k = 2 den_{k-1} - num_{k-1}, den_k = den_{k-1}(1-2x) + x num_{k-1}".
[^6]: [[project-euler-502-representations](pages/project-euler-502-representations.md)] §"Signed count" L343-345 — "k=1: P(1,L) = 2P(1,L-1) - 2P(1,L-2), closed form P(1,L) = Re((1+i)^{L+1}); k=2: P(2,L) = 3P(2,L-1) - 4P(2,L-2) + 4P(2,L-3)".
[^7]: [[project-euler-502-representations](pages/project-euler-502-representations.md)] §"The main formula" L350 — "The full castle is U (tower) D, so its block count is the tower's block count plus one for the bottom block. Even total blocks means an odd number of blocks in the tower."
[^8]: [[project-euler-502-representations](pages/project-euler-502-representations.md)] §"The main formula" L352-367 — "h^w = T(h-1,w) counts towers ... any parity. P(h-1,w) is the signed version, so (T - P)/2 counts towers with an odd block count ... subtract the height ≤ h-2 case to force height exactly h", giving "F(w,h) = (h^w - (h-1)^w - P(h-1,w) + P(h-2,w))/2".
[^9]: [[project-euler-502-representations](pages/project-euler-502-representations.md)] §"The main formula" L372-411 — the Python building P(k,L) from the num/den recurrence and F(w,h) from the formula, printing "F(4,2) = 10 / F(13,10) = 3729050610636 / F(10,13) = 37959702514"; re-run during ingest, all three reproduce exactly.
