---
title: "Convex castle count is binomial (Vandermonde)"
category: Analyses
summary: A proof that the convex castles of width w and height h number A_convex(w, h) = C(2h+w−3, w−1). Splitting the skyline at its first column of height h gives a weakly increasing front and a weakly decreasing back, chosen independently, so the count is a convolution of two binomial sequences, which the generalized Vandermonde convolution sums.
tags: [analysis, castle, convex, binomial, vandermonde, catalan]
sources: [aocp-binomial-coefficients, algebraic-languages-and-polyominoes-enumeration]
created: 2026-09-13
updated: 2026-10-25
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

*Proof of the Theorem.* Substitute `a = p − 1` and `n = w − 1` in Equation (1). It is the left side of Equation (2) with `r = h − 2` and `s = h − 1`, so[^3]

```
A_convex(w, h)  =  C((h−2) + (h−1) + (w−1) + 1, w−1)  =  C(2h + w − 3, w − 1).
```

At `h = 2` the Theorem gives `C(w + 1, 2)`, the triangular numbers `A000217(w)`, and at `h = 3` it gives `C(w + 3, 4)`.

The front and the back are chosen independently, so the count is a convolution of two binomial sequences, and Equation (2) makes it a single binomial coefficient. By contrast, the parallelogram polyominoes, whose upper and lower boundary paths share both endpoints and do not cross, are counted by the Catalan numbers by perimeter ([[parallelogram-polyomino-dyck-bijection](pages/parallelogram-polyomino-dyck-bijection.md)]).

Summed along `w + h = n + 2`, the Theorem gives the Fibonacci number `F_{2n+1}`, Delest and Viennot's count of stack polyominoes of perimeter `2n + 4` ([[convex-castle](pages/convex-castle.md)], section *Other gradings*).[^4]

## Appearances in Sources

- [[aocp-binomial-coefficients](pages/aocp-binomial-coefficients.md)] - negating the upper index, Knuth's equation (17), and Vandermonde's convolution, his equation (21), which together give Equation (2).
- [[algebraic-languages-and-polyominoes-enumeration](pages/algebraic-languages-and-polyominoes-enumeration.md)] - stack polyominoes counted by perimeter, and parallelogram polyominoes coded by Dyck words.

## Related Concepts

- [[convex-castle](pages/convex-castle.md)] - convex castles, their block count, the stars-and-bars proof of the Theorem, and their counts by area and by perimeter.
- [[castle-perimeter](pages/castle-perimeter.md)] - the semi-perimeter `w + blocks`, and the convex castles counted by semi-perimeter with the block sign.
- [[weakly-unimodal-composition](pages/weakly-unimodal-composition.md)] - the convex castles counted by area, `A001523`.
- [[parallelogram-polyomino-dyck-bijection](pages/parallelogram-polyomino-dyck-bijection.md)] - the bijection from Dyck words onto parallelogram polyominoes.
- [[tower-narayana-polynomial](pages/tower-narayana-polynomial.md)] - towers counted by blocks through Narayana polynomials.
- [[hyperbolic-sequence-family](pages/hyperbolic-sequence-family.md)] - castles of height 2 counted by block parity, through the binomial coefficients `C(w + 1, 2r)`.

## Footnotes

[^1]: Verified by execution (Python 3.11, 2026-10-25): Equation (1) equals the number of unimodal skylines of width `w` and height `h` for `w ≤ 8`, `h ≤ 6` with `h^w ≤ 400000`, and equals `C(2h + w − 3, w − 1)` for `w, h ≤ 15`; at `w = 4`, `h = 2` its terms for `p = 1, 2, 3, 4` are `4, 3, 2, 1`.
[^2]: [[aocp-binomial-coefficients](pages/aocp-binomial-coefficients.md)] §"Negating Upper Index" L57, §"Sums of Products" L68-70 - "C(-r,k) = (-1)^k C(r+k-1,k), k in Z. (eq (17))" and "sum_k C(r,k) C(s,n-k) = C(r+s,n)"; by (17), `C(r + a, a) = (−1)^a C(−r − 1, a)`, so Equation (2) is (21) at the upper indices `−r − 1` and `−s − 1`. Verified by execution (Python 3.11, 2026-10-25) for `r, s, n ≤ 11`.
[^3]: Verified by execution (Python 3.11, 2026-10-25): the Theorem against enumeration of all skylines for `w ≤ 8`, `h ≤ 6` with `h^w ≤ 400000`.
[^4]: [[algebraic-languages-and-polyominoes-enumeration](pages/algebraic-languages-and-polyominoes-enumeration.md)] p.181 Lemma 3.2 - "The number of stack polyominoes with perimeter 2n+4 is the Fibonacci number F_{2n}", with `F_0 = F_1 = 1`, which is `F_{2n+1}` with `F_1 = F_2 = 1`; the sums over `w + h = n + 2` were checked for `n ≤ 14` (Python 3.11, 2026-10-16).
