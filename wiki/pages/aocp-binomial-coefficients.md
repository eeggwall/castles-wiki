---
title: "AOCP Binomial Coefficients (Knuth TAOCP Vol. 1)"
category: Sources
summary: Notes on Knuth's TAOCP Vol. 1 §1.2.6. The binomial coefficient C(r, k) for real r, and the identities by type - symmetry, moving in and out of brackets, addition, the two summation formulas, the binomial theorem, negating the upper index, the product rule, Vandermonde's convolution (21) - with the Stirling numbers of both kinds and the row sums 2^n and 0. On the wiki, Vandermonde's convolution proves the convex castle count C(2h + w − 3, w − 1), and the negated upper index gives the negative binomial series 1/(1 − z)^{m+1}.
tags: [knuth, taocp, binomial, vandermonde, hockey-stick, stirling, source]
sources: [aocp-binomial-coefficients]
created: 2026-09-14
updated: 2026-10-16
---

# AOCP Binomial Coefficients (Knuth, *The Art of Computer Programming*, Vol. 1)

**Source:** https://charlesreid1.com/wiki/AOCP/Binomial_Coefficients (notes on Knuth, *The Art of Computer Programming*, Vol. 1, §1.2.6)
**Date ingested:** 2026-09-14
**Type:** article (MediaWiki notes page); reference

## Summary

The notes define the binomial coefficient `C(n, k) = n!/(k!(n−k)!)`, the number of ways to choose `k` of `n` objects, and extend it to a real upper index `r` by[^1]

```
C(r, k)  =  r(r − 1)⋯(r − k + 1) / k!,   k ≥ 0;        C(r, k)  =  0,   k < 0     (eq. (3))
```

They list Knuth's identities by type. For example, `C(4, 2) = 6`, and `C(−4, 3) = (−4)(−5)(−6)/6 = −20 = (−1)^3 C(6, 3)`, an instance of eq. (17), negating the upper index.

## Key Takeaways

- **Symmetry and addition.** `C(n, k) = C(n, n − k)` (eq. (6)) and `C(r, k) = C(r − 1, k) + C(r − 1, k − 1)` (eq. (9)), the rule of Pascal's triangle.[^2]
- **Summation.** `Σ_{0≤k≤n} C(r + k, k) = C(r + n + 1, n)` (eq. (10)) and `Σ_{0≤k≤n} C(k, m) = C(n + 1, m + 1)` (eq. (11)).[^3]
- **Binomial theorem.** `(x + y)^r = Σ_k C(r, k) x^k y^{r−k}` for integers `r ≥ 0` (eq. (13)), with Abel's generalization (eq. (16)). At `x = y = 1` and at `x = −1`, `y = 1`, it gives `Σ_k C(n, k) = 2^n` and `Σ_k (−1)^k C(n, k) = 0` for `n > 0`.[^4]
- **Negating the upper index.** `C(−r, k) = (−1)^k C(r + k − 1, k)` (eq. (17)).[^5]
- **Products.** `C(r, m) C(m, k) = C(r, k) C(r − k, m − k)` (eq. (20)).[^6]
- **Vandermonde's convolution.** `Σ_k C(r, k) C(s, n − k) = C(r + s, n)` (eq. (21)), which the notes say "should be memorized", read as the choices of `n` people from `r` men and `s` women.[^7]
- **Stirling numbers.** The first kind `[n m]` counts the permutations of `n` letters with `m` cycles and the second kind `{n m}` the partitions of `n` elements into `m` nonempty subsets; they convert between powers and falling factorials (eqs. (40), (41)) and satisfy the addition formulas (42) and the inversion formulas (43).[^8]

## Uses on the wiki

- **The convex castle count.** A convex castle of width `w` and height `h` splits at its first column of height `h` into a weakly increasing front and a weakly decreasing back, counted by binomial coefficients, and Vandermonde's convolution sums the product to `C(2h + w − 3, w − 1)` ([[convex-castle-binomial-identity](pages/convex-castle-binomial-identity.md)], [[convex-castle](pages/convex-castle.md)]).
- **The negative binomial series.** By eq. (17), `1/(1 − z)^{m+1} = Σ_k C(m + k, m) z^k`. It gives the factor `1/(1 − x)^L` of the tower generating function by blocks ([[tower-narayana-polynomial](pages/tower-narayana-polynomial.md)]) and the convex castle count as a coefficient ([[generating-functions](pages/generating-functions.md)], [[aocp-generating-functions](pages/aocp-generating-functions.md)]).
- **Row sums and the parity split.** `2^L` is the number of configurations of blocks in the row above a block of length `L` ([[binary-string-bijection](pages/binary-string-bijection.md)]). Halving `Σ_k C(n, k) ± Σ_k (−1)^k C(n, k)` counts the subsets of even and of odd size, the same split that [[castle-sign](pages/castle-sign.md)] makes with `(−1)^{blocks}`.
- **Sums over residue classes.** The binary strings of length `L` with `r` runs of 1s number `C(L + 1, 2r)`. With `z` marking runs, `Σ_r C(L + 1, 2r) z^r` gives `2^L` at `z = 1` and `P(1, L) = Re((1+i)^{L+1})` at `z = −1`; its even and odd `r` give the sums of every fourth binomial coefficient, `A038503(L + 1)` and `A038505(L + 1)` ([[block-count-constraints](pages/block-count-constraints.md)], [[hyperbolic-sequence-family](pages/hyperbolic-sequence-family.md)]). At height 2, `A^e(w, 2) = Σ_s C(w + 1, 4s + 2)`; at `w = 4` only `C(5, 2) = 10` is nonzero, and the castles of width `w` and height 2 whose row 2 is a single run number `C(w + 1, 2)`, the triangular numbers `A000217`.[^9]
- **An alternating sum.** On a base of length 1, `P(k, 1) = Σ_{c=0}^{k} (−1)^c = (1 + (−1)^k)/2` ([[closed-form-hunting](pages/closed-form-hunting.md)]).
- **Pascal's rule in a recurrence.** Applied to `H_d(μ) = Σ_i (−1)^i C(⌊(d+i)/2⌋, i) μ^{d−i}`, the factor of `char_k` on [[tower-parity-sectors](pages/tower-parity-sectors.md)], eq. (9) gives `H_{d+2} = −H_{d+1} + μ² H_d` (checked for `d ≤ 14`).[^9]
- **Stirling numbers.** `[n 1] = (n − 1)!`, the number of cyclic orders of `n` labeled points, which [[castles-as-upgraded-cycle-count](pages/castles-as-upgraded-cycle-count.md)] starts from; the triangles are `A132393` (first kind, unsigned) and `A008277` (second kind), and Pascal's triangle is `A007318`.[^10] [[multiset-partitions](pages/multiset-partitions.md)] and [[bender-1974-partitions-of-multisets](pages/bender-1974-partitions-of-multisets.md)] count the partitions of a multiset, four counts that reduce to `{n k}` when no element repeats.

## Entities & Concepts

- [[convex-castle-binomial-identity](pages/convex-castle-binomial-identity.md)] - the proof of the convex castle count by Vandermonde's convolution.
- [[convex-castle](pages/convex-castle.md)] - convex castles, their count and their block count.
- [[aocp-multinomial-coefficients](pages/aocp-multinomial-coefficients.md)] - the multinomial coefficients, which generalize `C(n, k)` to more than two kinds of object.
- [[aocp-generating-functions](pages/aocp-generating-functions.md)] - the negative binomial series as a power of the geometric series.
- [[binary-string-bijection](pages/binary-string-bijection.md)] - the `2^L` configurations in the row above a block, and the `C(L + 1, 2r)` strings with `r` runs.
- [[block-count-constraints](pages/block-count-constraints.md)] - selecting towers and castles by block count, through `Σ_r C(L + 1, 2r) z^r`.
- [[tower-parity-sectors](pages/tower-parity-sectors.md)] - the factors `H_d` of `char_k`.

Also linked from the source: [[aocp-multinomial-coefficients](pages/aocp-multinomial-coefficients.md)], [[aocp-multisets](pages/aocp-multisets.md)].

## Footnotes

[^1]: [[aocp-binomial-coefficients](pages/aocp-binomial-coefficients.md)] §"Definitions" L7-12 - "The number is the binomial coefficient C(n,k) = n!/(k!(n-k)!)", "For non-integer n, define (AOCP V1 1.2.6 eq (3)): C(r,k) = r(r-1)...(r-k+1) / (k(k-1)...1) = prod_{1<=j<=k} (r+1-j)/j, k in Z, k>=0; C(r,k) = 0 for k < 0".
[^2]: [[aocp-binomial-coefficients](pages/aocp-binomial-coefficients.md)] §"Symmetry Condition", §"Addition formulas" L22, L32 - "C(n,k) = C(n,n-k) for all integers k. (eq (6))" and "C(r,k) = C(r-1,k) + C(r-1,k-1) for integer k (eq (9))".
[^3]: [[aocp-binomial-coefficients](pages/aocp-binomial-coefficients.md)] §"Summation formulas" L36-40 - "sum_{0<=k<=n} C(r+k,k) = ... = C(r+n+1,n), n>=0" and "sum_{0<=k<=n} C(k,m) = ... = C(n+1,m+1), integer m,n >= 0".
[^4]: [[aocp-binomial-coefficients](pages/aocp-binomial-coefficients.md)] §"Binomial Theorem" L50-53, §"Knuth AOCP Section 1.2.6 Problem 36" L91-92 - "(x+y)^r = sum_{0<=k<=r} C(r,k) x^k y^{r-k} for integer r>=0 (eq (13))", "Abel's generalization (eq (16))", "sum_k C(n,k) = 2^n", "sum_k C(n,k)(-1)^k = (1-1)^n = 0^n = 0 for n>0, 1 for n=0".
[^5]: [[aocp-binomial-coefficients](pages/aocp-binomial-coefficients.md)] §"Negating Upper Index" L57 - "C(-r,k) = (-1)^k C(r+k-1,k), k in Z. (eq (17))".
[^6]: [[aocp-binomial-coefficients](pages/aocp-binomial-coefficients.md)] §"Simplifying Products" L64 - "C(r,m) C(m,k) = C(r,k) C(r-k,m-k), integer m, k (eq (20))".
[^7]: [[aocp-binomial-coefficients](pages/aocp-binomial-coefficients.md)] §"Sums of Products" L68-72 - "Vandermonde's convolution (eq (21), published 1772) -- the most important, \"should be memorized\": sum_k C(r,k) C(s,n-k) = C(r+s,n)", "Interpret the RHS as choosing n people from r men and s women".
[^8]: [[aocp-binomial-coefficients](pages/aocp-binomial-coefficients.md)] §"Stirling Numbers" L80-85 - "First kind [n m] (permutations of n letters with m cycles), second kind {n m} (partitions of n elements into m nonempty subsets)", eqs. (40)-(43).
[^9]: Verified by execution (Python 3.11 with SymPy, 2026-10-16): `C(−4, 3) = −20`; `Σ_s C(w + 1, 4s + 2) = 1, 3, 6, 10, 16, 28, 56` for `w = 1, …, 7`, equal to `A^e(w, 2)`; `H_{d+2} = −H_{d+1} + μ² H_d` for `d ≤ 14`.
[^10]: https://oeis.org/A132393, https://oeis.org/A008277, https://oeis.org/A007318, https://oeis.org/A000217 (read 2026-10-16) - "Triangle of unsigned Stirling numbers of the first kind", "Triangle of Stirling numbers of the second kind", "Pascal's triangle read by rows", "Triangular numbers: a(n) = binomial(n+1,2)".
