---
title: "Convex castle count is binomial (Vandermonde)"
category: Analyses
summary: Why convex(w,h) = C(2h+w−3, w−1) — an up/down decomposition at the peak plus a generalized Vandermonde convolution; binomial, not Catalan, because the two halves are independent.
tags: [analysis, castle, convex, binomial, vandermonde, catalan]
sources: [oeis-mining-pe502, algebraic-languages-and-polyominoes-enumeration]
created: 2026-09-13
updated: 2026-09-26
---

# Convex castle count is binomial (Vandermonde)

## Overview

This is the *reason* the [[convex-castle](pages/convex-castle.md)] count is a binomial coefficient, `C(2h+w−3, w−1)`, and why no Catalan/Narayana number appears in the natural (w,h) parameterization. The short answer: a convex castle's ascending front and descending back are chosen **independently** — there is no ballot / non-crossing condition to couple them — and a product of two monotone-piece counts is a binomial. Everything below was verified numerically (up/down decomposition and the Vandermonde identity checked against brute force for `w,h ≤ 7`; the binomial and the "exactly h blocks" facts re-verified for `w,h ≤ 5` during ingest).[^1]

## Convex ⟺ unimodal ⟺ exactly *h* blocks

A castle is convex (row- and column-convex) exactly when its height profile `c_1..c_w` is **unimodal** (non-decreasing then non-increasing): the columns reaching level *r* form an interval for every *r* iff the profile is unimodal. For any profile, `#blocks = c_1 + ∑_{i≥2} max(0, c_i − c_{i−1})`, and the positive rises telescope to the running maximum, so[^2]

```
#blocks ≥ max(c) = h,   with equality iff the profile is unimodal.
```

Hence a convex castle of height *h* has **exactly *h* blocks**, and convex castles are precisely the *minimum-block* castles of height *h*. (So the even-parity convex count is `C(2h+w−3, w−1)` when *h* is even and `0` when *h* is odd.) In boundary terms this is the classical convexity-perimeter fact. A castle's semi-perimeter is `w + #blocks`, so `#blocks ≥ h` says the perimeter is at least the bounding-box perimeter `2(w+h)`, with equality iff the castle is convex ([[castle-perimeter](pages/castle-perimeter.md)]).

## The up/down decomposition + Vandermonde

Fix `p` = the leftmost column of height *h*. A unimodal profile splits at `p` into two independent monotone pieces: an ascending **front** (`c_1 ≤ … ≤ c_{p−1} ≤ h−1`, values in `{1..h−1}`) and a descending **back** (`h = c_p ≥ … ≥ c_w`, values in `{1..h}`). Counting each as a monotone sequence and summing over `p`:[^3]

```
convex(w,h) = Σ_{p=1}^{w} C((h−2)+(p−1), p−1) · C((h−1)+(w−p), w−p)
```

(the off-by-one — `h−2` for the front, `h−1` for the back — is because the peak belongs to the back). With `a = p−1`, `n = w−1`, this is the **generalized Vandermonde convolution** `Σ_k C(r+k,k)C(s+n−k,n−k) = C(r+s+n+1, n)` at `r = h−2`, `s = h−1`, giving[^4]

```
convex(w,h) = C((h−2)+(h−1)+(w−1)+1, w−1) = C(2h + w − 3, w − 1).   ∎
```

For example `convex(w,2) = C(w+1, 2)` (triangular), `convex(w,3) = C(w+3,4)` — diagonals of Pascal's triangle.

## Why binomial and not Catalan

The two halves combine by an ordinary product (then a Vandermonde sum) precisely because they are **independent**. Catalan/Narayana counts arise when a **non-crossing or ballot constraint couples the halves** (as a Dyck path's up and down segments must jointly stay above the diagonal). The castle's Rule 3 (same-row gap) imposes no such coupling - in the run decomposition it is automatic - so the hoped-for "Catalan find" does not exist for the (w,h) parameterization; a Catalan object would require grafting on an extra condition the castle does not contain.[^5] (The Catalan/Narayana thread does appear elsewhere - in the [[tower-narayana-polynomial](pages/tower-narayana-polynomial.md)] block-count.) The coupled counterpart is the parallelogram polyomino. Its two boundary paths share both endpoints and must not cross, and it is Catalan by perimeter ([[parallelogram-polyomino-dyck-bijection](pages/parallelogram-polyomino-dyck-bijection.md)]).

The binomial character runs through the whole object: the height-2 block distribution `C(w+1, 2r)` (feeding the [[hyperbolic-sequence-family](pages/hyperbolic-sequence-family.md)]), the height-≤1 tower (castle height ≤ 2) distribution `C(w+1, 2b) = A034839`, and the any-parity `h^w − (h−1)^w` differences are all binomial.[^6]

## The anti-diagonal sums are Fibonacci

Summing the binomial along `w + h = n + 2` (fixed perimeter `2n+4`) gives `F_{2n}` with `F_0 = F_1 = 1` (A001519: 2, 5, 13, 34, 89, ...; checked for `n = 1..14` during ingest). This is Delest-Viennot's count of stack polyominoes by perimeter. They obtain it from a rational grammar of "Fibonacci words" rather than from the binomial.[^7] The Vandermonde argument and the Fibonacci-word argument are two proofs that the same generating function `Σ_{w,h} C(2h+w-3, w-1) x^w y^h` is rational. The Fibonacci words specialize it at `x = y = t`.

## Appearances in Sources

- [[oeis-mining-pe502](pages/oeis-mining-pe502.md)] — vein 4; the binomial-vs-Catalan fork resolved.
- [[algebraic-languages-and-polyominoes-enumeration](pages/algebraic-languages-and-polyominoes-enumeration.md)] - the same class by perimeter (Fibonacci), and parallelogram polyominoes as the coupled-boundary Catalan counterpart.

## Related Concepts

- [[convex-castle](pages/convex-castle.md)] — the object counted here.
- [[castle-perimeter](pages/castle-perimeter.md)] - blocks = semi-perimeter minus width; the anti-diagonal (perimeter) parity split of this binomial.
- [[tower-narayana-polynomial](pages/tower-narayana-polynomial.md)] — where Catalan/Narayana *does* live.
- [[weakly-unimodal-composition](pages/weakly-unimodal-composition.md)] — convex castles by area (A001523).
- [[aocp-binomial-coefficients](pages/aocp-binomial-coefficients.md)] — Vandermonde's convolution (the identity that closes this sum) and the binomial toolkit.

## Footnotes

[^1]: [[oeis-mining-pe502](pages/oeis-mining-pe502.md)] `binomial-vandermonde-identity.md` L9-13 — "verified numerically ... the up/down decomposition and the Vandermonde identity were each checked against brute force for w,h <= 7"; binomial and blocks==h re-verified for w,h ≤ 5 during ingest.
[^2]: [[oeis-mining-pe502](pages/oeis-mining-pe502.md)] `binomial-vandermonde-identity.md` §1 L14-33 — "#blocks >= max(c) = h, with equality iff the profile is unimodal ... a convex castle of height h has exactly h blocks, and convex castles are exactly the minimum-block castles."
[^3]: [[oeis-mining-pe502](pages/oeis-mining-pe502.md)] `binomial-vandermonde-identity.md` §2 L35-62 — the front/back decomposition and "convex(w,h) = sum_{p=1}^{w} C((h-2)+(p-1), p-1) · C((h-1)+(w-p), w-p)."
[^4]: [[oeis-mining-pe502](pages/oeis-mining-pe502.md)] `binomial-vandermonde-identity.md` §3 L64-80 — "the generalized Vandermonde convolution sum_k C(r+k,k)·C(s+n-k,n-k) = C(r+s+n+1, n), with r = h-2, s = h-1, n = w-1 ... convex(w,h) = C(2h + w - 3, w - 1)."
[^5]: [[oeis-mining-pe502](pages/oeis-mining-pe502.md)] `binomial-vandermonde-identity.md` §4 L82-96 — "The two halves are independent ... A binomial is exactly what a product of two monotone-piece counts gives. Catalan / Narayana counts arise when a non-crossing or ballot constraint couples the two halves ... The castle's Rule 3 ... imposes no such coupling."
[^6]: [[oeis-mining-pe502](pages/oeis-mining-pe502.md)] `binomial-vandermonde-identity.md` §5 L98-116 — the height-2 distribution C(w+1,2r), the height-≤1 distribution C(w+1,2b) = A034839, and the h^w−(h−1)^w family, all binomial.
[^7]: [[algebraic-languages-and-polyominoes-enumeration](pages/algebraic-languages-and-polyominoes-enumeration.md)] p.181 Lemma 3.2 [synthesis] - stacks by perimeter 2n+4 are counted by F_{2n} with GF (1-t^2)/((1-t-t^2)(1+t-t^2)); the anti-diagonal identity is own reasoning, verified numerically n = 1..14.
