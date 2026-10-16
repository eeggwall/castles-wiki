---
title: "Convex castle count is binomial (Vandermonde)"
category: Analyses
summary: A proof that the convex castles of width w and height h number A_convex(w, h) = C(2h+w−3, w−1). Splitting the skyline at its first column of height h gives a weakly increasing front and a weakly decreasing back, chosen independently, so the count is a convolution of two binomial sequences, which the generalized Vandermonde convolution sums.
tags: [analysis, castle, convex, binomial, vandermonde, catalan]
sources: [oeis-mining-pe502, algebraic-languages-and-polyominoes-enumeration]
created: 2026-09-13
updated: 2026-10-16
---

# Convex castle count is binomial (Vandermonde)

A [[convex-castle](pages/convex-castle.md)] is a castle with a unimodal skyline, `c_1 ≤ ⋯ ≤ c_p ≥ ⋯ ≥ c_w`, and `A_convex(w, h)` is the number of convex castles of width `w` and height `h`. This page proves

**Theorem.** `A_convex(w, h) = C(2h + w − 3, w − 1)`.

[[convex-castle](pages/convex-castle.md)] (section *Count*) proves the Theorem by placing letters `R` in the slots of a step word. The proof here splits the skyline into two monotone pieces. At `h = 1` the only castle is the flat row and `C(w − 1, w − 1) = 1`, so take `h ≥ 2`.

## The front and the back

Let `p` be the first column of height `h`. A unimodal skyline splits at `p` into[^1]

- a **front** `c_1 ≤ ⋯ ≤ c_{p−1}`, a weakly increasing sequence of length `p − 1` with values in `{1, …, h − 1}`, and
- a **back** `c_{p+1} ≥ ⋯ ≥ c_w` after `c_p = h`, a weakly decreasing sequence of length `w − p` with values in `{1, …, h}`.

Any front goes with any back. A weakly increasing, or weakly decreasing, sequence of length `j` with values in a set of `v` numbers is a multiset of size `j` from `v` numbers, so there are `C(v − 1 + j, j)` of them. The front has `v = h − 1` and the back `v = h`, so

```
A_convex(w, h)  =  Σ_{p=1}^{w}  C((h−2) + (p−1), p−1) · C((h−1) + (w−p), w−p).        (1)
```

The front's values stop at `h − 1` because `p` is the first column of height `h`, and the back's go up to `h`.

*Example: `w = 4`, `h = 2`.* Every front is all 1s, and the back is a weakly decreasing sequence in `{1, 2}` of length `4 − p`, which can be chosen in `5 − p` ways. Equation (1) gives `4 + 3 + 2 + 1 = 10 = C(5, 3)`.[^1] These ten castles are the skylines in `{1, 2}^4` whose height-2 columns form one interval, the ten castles of the example `A^e(4, 2) = 10` on [[castle-counting-formula](pages/castle-counting-formula.md)]: at width 4, a castle of height 2 with an even number of blocks has one block in row 2.

## The Vandermonde convolution

**Lemma (generalized Vandermonde convolution).** For integers `r, s, n ≥ 0`,

```
Σ_{a=0}^{n}  C(r + a, a) · C(s + n − a, n − a)  =  C(r + s + n + 1, n).                  (2)
```

*Proof.* `Σ_a C(r + a, a) x^a = (1 − x)^{−(r+1)}`, so the left side of Equation (2) is the coefficient of `x^n` in `(1 − x)^{−(r+1)} (1 − x)^{−(s+1)} = (1 − x)^{−(r+s+2)}`, which is `C(r + s + 1 + n, n)`.[^2]

*Proof of the Theorem.* Substitute `a = p − 1` and `n = w − 1` in Equation (1). It is the left side of Equation (2) with `r = h − 2` and `s = h − 1`, so[^2]

```
A_convex(w, h)  =  C((h−2) + (h−1) + (w−1) + 1, w−1)  =  C(2h + w − 3, w − 1).
```

At `h = 2` the Theorem gives `C(w + 1, 2)`, the triangular numbers `A000217(w)`, and at `h = 3` it gives `C(w + 3, 4)`.

The front and the back are chosen independently, so the count is a convolution of two binomial sequences, and Equation (2) makes it a single binomial coefficient.[^3] By contrast, the parallelogram polyominoes, whose upper and lower boundary paths share both endpoints and do not cross, are counted by the Catalan numbers by perimeter ([[parallelogram-polyomino-dyck-bijection](pages/parallelogram-polyomino-dyck-bijection.md)]).

Summed along `w + h = n + 2`, the Theorem gives the Fibonacci number `F_{2n+1}`, Delest and Viennot's count of stack polyominoes of perimeter `2n + 4` ([[convex-castle](pages/convex-castle.md)], section *Other gradings*).[^4]

## Appearances in Sources

- [[oeis-mining-pe502](pages/oeis-mining-pe502.md)] - the split at the first column of height `h`, Equation (1), the Vandermonde convolution with its proof, and the example at `w = 4`, `h = 2`.
- [[algebraic-languages-and-polyominoes-enumeration](pages/algebraic-languages-and-polyominoes-enumeration.md)] - stack polyominoes counted by perimeter, and parallelogram polyominoes coded by Dyck words.

## Related Concepts

- [[convex-castle](pages/convex-castle.md)] - convex castles, their block count, the stars-and-bars proof of the Theorem, and their counts by area and by perimeter.
- [[aocp-binomial-coefficients](pages/aocp-binomial-coefficients.md)] - Vandermonde's convolution `Σ_k C(r, k) C(s, n−k) = C(r + s, n)`, Knuth's equation (21), and the other binomial identities.
- [[castle-perimeter](pages/castle-perimeter.md)] - the semi-perimeter `w + blocks`, and the convex castles counted by semi-perimeter with the block sign.
- [[weakly-unimodal-composition](pages/weakly-unimodal-composition.md)] - the convex castles counted by area, `A001523`.
- [[parallelogram-polyomino-dyck-bijection](pages/parallelogram-polyomino-dyck-bijection.md)] - the bijection from Dyck words onto parallelogram polyominoes.
- [[tower-narayana-polynomial](pages/tower-narayana-polynomial.md)] - towers counted by blocks through Narayana polynomials.
- [[hyperbolic-sequence-family](pages/hyperbolic-sequence-family.md)] - castles of height 2 counted by block parity, through the binomial coefficients `C(w + 1, 2r)`.

## Footnotes

[^1]: [[oeis-mining-pe502](pages/oeis-mining-pe502.md)] `binomial-vandermonde-identity.md` §2 L37-62 - "Fix p = the leftmost column of height h (the first peak). A unimodal profile splits at p into two independent pieces", "convex(w,h) = sum_{p=1}^{w} C((h-2) + (p-1), p-1) · C((h-1) + (w-p), w-p)", and "Worked example, w = 4, h = 2: ... p=1,2,3,4 give 4,3,2,1 backs, total 4+3+2+1 = 10 = C(5,3) = C(2h+w-3, w-1)".
[^2]: [[oeis-mining-pe502](pages/oeis-mining-pe502.md)] `binomial-vandermonde-identity.md` §3 L66-80 - "sum_{k=0}^{n} C(r+k, k) · C(s+n-k, n-k) = C(r+s+n+1, n), with r = h-2, s = h-1, n = w-1. (Proof: sum_k C(r+k,k) x^k = (1-x)^{-(r+1)}, so the product of the two generating functions is (1-x)^{-(r+s+2)}, whose coefficient of x^n is C(r+s+n+1, n).)", "convex(w,h) = C((h-2)+(h-1)+(w-1)+1, w-1) = C(2h + w - 3, w - 1)". The Theorem was checked against enumeration of all skylines for `w ≤ 7`, `h ≤ 6` with `h^w ≤ 300000` (Python 3.11, 2026-10-16).
[^3]: [[oeis-mining-pe502](pages/oeis-mining-pe502.md)] `binomial-vandermonde-identity.md` §4 L84-86 - "The two halves are **independent**: the front is any non-decreasing sequence, the back any non-increasing sequence, and they are combined by an ordinary product (then summed by Vandermonde)."
[^4]: [[algebraic-languages-and-polyominoes-enumeration](pages/algebraic-languages-and-polyominoes-enumeration.md)] p.181 Lemma 3.2 - "The number of stack polyominoes with perimeter 2n+4 is the Fibonacci number F_{2n}", with `F_0 = F_1 = 1`, which is `F_{2n+1}` with `F_1 = F_2 = 1`; the sums over `w + h = n + 2` were checked for `n ≤ 14` (Python 3.11, 2026-10-16).
