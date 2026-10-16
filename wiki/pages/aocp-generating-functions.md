---
title: "AOCP Generating Functions (Knuth TAOCP Vol. 1)"
category: Sources
summary: Notes on Knuth's treatment of generating functions (TAOCP Vol. 1 §1.2.9) - the Fibonacci example, G(z) = z/(1 − z − z²) = (1/√5)(1/(1 − φz) − 1/(1 − φ̂z)) and F_n = (φ^n − φ̂^n)/√5; a linear recurrence gives a polynomial over 1 − c_1 z − ⋯ − c_m z^m; the operations (addition, shifting, multiplication as convolution, partial sums, exponential generating functions for binomial convolutions, differentiation and integration); the binomial theorem with the negative binomial 1/(1 − z)^{n+1} = Σ C(n+k, n) z^k, the exponential and logarithm series; and Exercise 1, 1/(1 − 2z) + 1/(1 − 3z) = (2 − 5z)/(1 − 5z + 6z²).
tags: [knuth, taocp, generating-functions, c-finite, rational, partial-fractions, source]
sources: [aocp-generating-functions]
created: 2026-09-13
updated: 2026-10-16
---

# AOCP Generating Functions (Knuth, *The Art of Computer Programming*, Vol. 1)

**Source:** https://charlesreid1.com/wiki/AOCP/Generating_Functions (notes on Knuth, *The Art of Computer Programming*, Vol. 1, §1.2.9, with Knuth's Fibonacci example)
**Date ingested:** 2026-09-13
**Type:** article (MediaWiki notes page)

## Summary

**The Fibonacci example.** With `F_0 = 0`, `F_1 = 1` and `F_n = F_{n−1} + F_{n−2}`, let `G(z) = Σ_{n≥0} F_n z^n`. Subtracting `zG(z)` and `z²G(z)` from `G(z)` leaves[^1]

```
(1 − z − z²) G(z)  =  F_0 + (F_1 − F_0) z  =  z,        G(z)  =  z / (1 − z − z²).
```

The denominator factors as `1 − z − z² = (1 − φz)(1 − φ̂z)`, with `φ = (1 + √5)/2` and `φ̂ = 1 − φ`, so the poles of `G` are `z = 1/φ` and `z = 1/φ̂`. Partial fractions give[^1]

```
G(z)  =  (1/√5) ( 1/(1 − φz) − 1/(1 − φ̂z) ),        F_n  =  (φ^n − φ̂^n) / √5,
```

using `1/(1 − az) = Σ_n a^n z^n`. Since `|φ̂^n/√5| < 1/2`, `F_n` is the integer nearest `φ^n/√5`. The coefficients of `G` are `0, 1, 1, 2, 3, 5, 8, 13, 21, …`.[^2]

**Linear recurrences.** If `a_n = c_1 a_{n−1} + ⋯ + c_m a_{n−m}` for `n ≥ m`, then `(1 − c_1 z − ⋯ − c_m z^m) G(z)` has no coefficient of degree `m` or more, so `G(z)` is a polynomial of degree less than `m` divided by `1 − c_1 z − ⋯ − c_m z^m`.[^3] The simplest case, `1, 1, 1, …`, gives `(1 − z)G(z) = 1` and `1/(1 − z) = 1 + z + z² + ⋯`.

**Operations.** The source lists Knuth's operations on generating functions:[^4]

- addition, and multiplication by a constant;
- shifting: multiplying by `z^k` moves every coefficient `k` places, `z^k Σ_n a_n z^n = Σ_{n≥k} a_{n−k} z^n`;
- multiplication: `G_1(z) G_2(z)` has coefficients `s_n = Σ_{k=0}^{n} a_k b_{n−k}`, the convolution of the two sequences; with `b_n = 1`, `G(z)/(1 − z)` has the partial sums `a_0 + ⋯ + a_n`;
- exponential generating functions: if `c_n = Σ_k C(n, k) a_k b_{n−k}`, then `Σ c_n z^n/n! = (Σ a_n z^n/n!)(Σ b_n z^n/n!)`;
- change of variable, which selects the even or the odd coefficients;
- differentiation and integration, `G'(z) = Σ_k (k+1) a_{k+1} z^k` and `∫_0^z G(t) dt = Σ_{k≥1} a_{k−1} z^k / k`, with `d/dz (1/(1 − z)) = Σ_k (k+1) z^k` and `∫_0^z dt/(1 − t) = ln(1/(1 − z)) = Σ_{k≥1} z^k/k`.

**Known generating functions.** The binomial theorem `(1 + z)^r = Σ_k C(r, k) z^k`, and for a negative integer exponent the **negative binomial** series[^5]

```
1/(1 − z)^{n+1}  =  Σ_{k≥0} C(n + k, n) z^k;
```

the exponential series `e^z = Σ z^k/k!`; and the logarithm series `ln(1 + z) = Σ_{k≥1} (−1)^{k+1} z^k/k`.[^5]

**Exercise 1 of §1.2.9.** The sequence `2^n + 3^n = 2, 5, 13, 35, 97, 275, …` has generating function[^6]

```
1/(1 − 2z) + 1/(1 − 3z)  =  (2 − 5z) / (1 − 5z + 6z²).
```

## Castle readings

These readings are the wiki's, not the source's.

- **Rational generating functions.** The signed tower count has generating function `P_k(x) = Σ_L P(k, L) x^L = num_k(x)/den_k(x)`, with `den_k` of degree `k + 1`, and the recurrence of `P(k, ·)` has characteristic polynomial `char_k(λ) = λ^{k+1} den_k(1/λ)`, the reciprocal of the denominator ([[castle-counting-formula](pages/castle-counting-formula.md)], [[signed-tower-count](pages/signed-tower-count.md)]). [[kitamasa](pages/kitamasa.md)] evaluates far terms of such a recurrence, and [[berlekamp-massey](pages/berlekamp-massey.md)] finds it from terms.
- **Partial fractions for `P(1, L)`.** `P_1(x) = (1 − 2x)/(1 − 2x + 2x²)` has poles at `1/(1 ± i)`, and[^7]

  ```
  P_1(x)  =  ½ ( (1 + i)/(1 − (1 + i)x) + (1 − i)/(1 − (1 − i)x) ),        P(1, L)  =  Re((1 + i)^{L+1}).
  ```

- **Negative binomial.** The convex castles of width `w` and height `h` number `C(2h + w − 3, w − 1) = [z^{w−1}] (1 − z)^{−(2h−1)}` ([[convex-castle](pages/convex-castle.md)]). The towers on a base of length `L` counted by blocks have generating function `Σ_k N(L, k) x^{k−1} / (1 − x)^L`, with `N(L, k)` the Narayana numbers, and the negative binomial series turns it into `T̂(L, b) = Σ_k N(L, k) C(b + L − k, L − 1)` ([[tower-heap](pages/tower-heap.md)], [[tower-narayana-polynomial](pages/tower-narayana-polynomial.md)]). The tower count `E_k(x) = 1/(1 − (k+1)x)` is geometric.
- **Differences of geometric series.** As in Exercise 1, the castles of height `h` counted by width have generating function `Σ_{w≥1} (h^w − (h−1)^w) z^w = z / ((1 − hz)(1 − (h − 1)z))` ([[castle-counting-function](pages/castle-counting-function.md)]). At `h = 3` the coefficients are `A001047(w) = 3^w − 2^w = A^e(w, 3) + A^o(w, 3)` ([[new-sequence-fw3](pages/new-sequence-fw3.md)]).

## Entities & Concepts

- [[generating-functions](pages/generating-functions.md)] - generating functions on the wiki and the castle counts they compute.
- [[generating-functions-topic](pages/generating-functions-topic.md)] - the source's linked page on generating functions.
- [[analytic-combinatorics-ch1-ogfs](pages/analytic-combinatorics-ch1-ogfs.md)] - Flajolet-Sedgewick Chapter I, linked from the source.
- [[aocp-binomial-coefficients](pages/aocp-binomial-coefficients.md)] - the binomial coefficients with negative upper index behind the negative binomial series.
- [[castle-counting-formula](pages/castle-counting-formula.md)], [[signed-tower-count](pages/signed-tower-count.md)] - the rational generating functions `P_k(x)` and their recurrences.
- [[kitamasa](pages/kitamasa.md)], [[berlekamp-massey](pages/berlekamp-massey.md)] - evaluating and finding linear recurrences.
- [[tower-heap](pages/tower-heap.md)], [[tower-narayana-polynomial](pages/tower-narayana-polynomial.md)] - the towers by blocks, with the denominator `(1 − x)^L`.
- [[convex-castle](pages/convex-castle.md)] - the convex count as a coefficient of a negative binomial series.
- [[new-sequence-fw3](pages/new-sequence-fw3.md)] - the castles of height 3 split by parity.
- [[recurrence-discovery](pages/recurrence-discovery.md)] - the orders of the recurrences of `P(k, L)` in `L` and in `k`, found by Berlekamp-Massey.

## Footnotes

[^1]: [[aocp-generating-functions](pages/aocp-generating-functions.md)] §"Knuth's Fibonacci Example", §"Partial Fraction Expansion", §"Closed Form Expression for Approx Nth Fib Number" L13-92 - "G(z) = F_0 + F_1 z + F_2 z^2 + ... (Note this uses the convention that F0 = 0 and F1 = 1", "(1 - z - z^2) G(z) = z, G(z) = z/(1 - z - z^2)", "z^2 + z - 1 = (phi + z)(hat phi + z)", "G(z) = (1/sqrt 5)(1/(1 - phi z) - 1/(1 - hat phi z))", "F_n = (1/sqrt 5)(phi^n - hat phi^n)", "F_n ~ phi^n/sqrt 5 correct to nearest integer".
[^2]: Verified by execution (Python 3.11 with SymPy, 2026-10-16): the coefficients of `z/(1 − z − z²)` through `z^8`, and of `(2 − 5z)/(1 − 5z + 6z²)` through `z^5`.
[^3]: [[aocp-generating-functions](pages/aocp-generating-functions.md)] §"Generating Functions for Linearly Recurrent Series" L120-138 - "Given any linearly recurrent sequence, where a_n = c_1 a_{n-1} + ... + c_m a_{n-m} the resulting generating function is a polynomial divided by the quantity (1 - c_1 z - ... - c_m z^m)", "the simplest sequence 1, 1, 1, ...: (1 - z) G(z) = 1".
[^4]: [[aocp-generating-functions](pages/aocp-generating-functions.md)] §"Chapter 1: Basic Concepts: Generating Functions" L98-104 and §§"Addition"-"Calculus" L106-176 [synthesis] - the list of operations ("Addition", "Shifting", "Multiplication", "Change of variable in z (even or odd coefficients only)", "Differentiation and integration", "Known generating functions"), the convolution "s_n = sum_{k=0}^{n} a_k b_{n-k}", the partial sums "1/(1-z) G(z) = a_0 + (a_0 + a_1) z + ...", the exponential generating functions for "c_n = sum_k C(n,k) a_k b_{n-k}", and the derivative and integral formulas.
[^5]: [[aocp-generating-functions](pages/aocp-generating-functions.md)] §"Functions With Known Generating Functions" L180-202 - "(1 + z)^r = sum_{k >= 0} C(r, k) z^k", "When r is a negative integer, the special case: 1/(1-z)^{n+1} = sum_{k >= 0} C(n+k, n) z^k", "e^z = sum 1/k! z^k", "ln(1+z) = sum_{k >= 1} (-1)^{k+1}/k z^k".
[^6]: [[aocp-generating-functions](pages/aocp-generating-functions.md)] §"Knuth AOCP Section 1.2.9 Exercise 1" L206-216 - "What is the generating function for <2^n + 3^n> = {2, 5, 13, 35, ...}?", "G(z) = 1/(1-2z) + 1/(1-3z) = (2-5z)/(1-5z+6z^2)".
[^7]: Verified by execution (Python 3.11 with SymPy, 2026-10-16): the partial-fraction form of `P_1(x)`; `Σ_w (h^w − (h−1)^w) z^w = z/((1 − hz)(1 − (h−1)z))` symbolically in `h`; `(1 − φz)(1 − φ̂z) = 1 − z − z²`.
