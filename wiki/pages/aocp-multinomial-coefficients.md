---
title: "AOCP Multinomial Coefficients (Knuth TAOCP Vol. 1)"
category: Sources
summary: Notes on Knuth's multinomial coefficient C(n; k_1, …, k_m) = n!/(k_1! ⋯ k_m!) (TAOCP Vol. 1 §1.2.6, eq. (38)), the number of ways to divide n items into m labeled groups and of permutations of a multiset; the multinomial theorem (eq. (39)); and its factorization into a product of binomial coefficients, e.g. C(15; 3, 4, 5, 3) = C(7, 3) C(12, 7) C(15, 12) = 12 612 600. On the castle side, the step words over {U, R, D} with given letter counts number C(n; #U, #R, #D).
tags: [knuth, taocp, multinomial, binomial, multiset, lattice-path, source]
sources: [aocp-multinomial-coefficients]
created: 2026-09-14
updated: 2026-10-16
---

# AOCP Multinomial Coefficients (Knuth, *The Art of Computer Programming*, Vol. 1)

**Source:** https://charlesreid1.com/wiki/AOCP/Multinomial_Coefficients (notes on Knuth, *The Art of Computer Programming*, Vol. 1, §1.2.6)
**Date ingested:** 2026-09-14
**Type:** article (MediaWiki notes page); short reference

## Summary

The **multinomial coefficient** generalizes the binomial coefficient ([[aocp-binomial-coefficients](pages/aocp-binomial-coefficients.md)]). With `n = k_1 + ⋯ + k_m` and every `k_i ≥ 0`,[^1]

```
C(n; k_1, …, k_m)  =  n! / (k_1! k_2! ⋯ k_m!)                                 (§1.2.6, eq. (38))
```

It counts the ways to divide `n` items into `m` labeled groups of sizes `k_1, …, k_m`, which is the number of permutations of a multiset with multiplicities `k_1, …, k_m` ([[aocp-multisets](pages/aocp-multisets.md)]).[^1] At `m = 2`, `C(n; k, n − k) = C(n, k)`. For example, the multiset `{a, a, b}` has `C(3; 2, 1) = 3` permutations, `aab`, `aba` and `baa`.

The **multinomial theorem** generalizes the binomial theorem `(x + y)^n = Σ_k C(n, k) x^k y^{n−k}` (eq. (13)):[^2]

```
(x_1 + ⋯ + x_m)^n  =  Σ_{k_1 + ⋯ + k_m = n}  C(n; k_1, …, k_m) x_1^{k_1} ⋯ x_m^{k_m}       (eq. (39))
```

Every multinomial coefficient is a product of binomial coefficients, since the intermediate factorials cancel:[^3]

```
C(k_1 + ⋯ + k_m; k_1, …, k_m)  =  C(k_1 + k_2, k_1) · C(k_1 + k_2 + k_3, k_1 + k_2) ⋯ C(k_1 + ⋯ + k_m, k_1 + ⋯ + k_{m−1})
```

For example, `C(15; 3, 4, 5, 3) = 15!/(3! 4! 5! 3!) = C(7, 3)·C(12, 7)·C(15, 12) = 35 · 792 · 455 = 12 612 600`.[^4]

## Castle readings

These readings are the wiki's, not the source's.

- **Lattice paths.** The shortest paths in `d` dimensions with `N_i` steps in direction `i` number `C(N; N_1, …, N_d)`, and [[lattice-paths](pages/lattice-paths.md)] evaluates them by the binomial product: `C(15; 3, 4, 5, 3) = 12 612 600` in four dimensions, and `C(14, 4)·C(10, 4) = 1001 · 210 = 210 210` in three.[^4] The stars-and-bars count of [[convex-castle](pages/convex-castle.md)], `C(2h + w − 3, w − 1)`, is the case `m = 2`: the arrangements of `w − 1` letters `R` and `2h − 2` slot boundaries.
- **Step words.** The words over `{U, R, D}` with `a` letters `U`, `b` letters `R` and `c` letters `D` are the permutations of a three-letter multiset, `C(a + b + c; a, b, c)` of them ([[urd-step-strings](pages/urd-step-strings.md)]). The words of length `n` with as many `U` as `D` number the central trinomial coefficient `A002426(n)`, the largest coefficient of `(1 + x + x²)^n`: `1, 1, 3, 7, 19, 51, 141, 393, 1107` for `n = 0, …, 8`. Among them, the Motzkin paths, which never go below height 0, number `M_n` ([[motzkin-numbers](pages/motzkin-numbers.md)]), and the Motzkin paths with no factor `UD` or `DU` number `A004149(n + 1)`: `1, 1, 1, 2, 4, 8, 16, 33, 69` ([[tower-word-language](pages/tower-word-language.md)]).[^5]
- **Inversions.** Summing `q^{inv}` over the permutations of a multiset with multiplicities `k_1, …, k_m`, where `inv` counts the pairs `i < j` with the `i`-th letter after the `j`-th in the alphabet, gives the q-multinomial coefficient `[n]_q! / ([k_1]_q! ⋯ [k_m]_q!)`, with `[k]_q! = (1 − q)(1 − q²)⋯(1 − q^k)/(1 − q)^k`. It factors into q-binomial coefficients as the multinomial coefficient factors into binomials (checked for three-letter multisets of size at most 7).[^6] [[permutation-inversions](pages/permutation-inversions.md)] treats the case of a set.
- **Convex castles.** [[convex-castle-binomial-identity](pages/convex-castle-binomial-identity.md)] splits a convex castle at its first column of height `h` into an increasing front and a decreasing back, counts each by a binomial coefficient, and sums the products with Vandermonde's identity.

The multinomial coefficients are tabulated in `A036038`, by the partitions of `n` in Abramowitz-Stegun order: `1; 1, 2; 1, 3, 6; 1, 4, 6, 12, 24; …`.[^5]

## Entities & Concepts

- [[aocp-binomial-coefficients](pages/aocp-binomial-coefficients.md)] - the binomial coefficients in the product.
- [[aocp-multisets](pages/aocp-multisets.md)] - permutations of a multiset, counted by the multinomial coefficient.
- [[lattice-paths](pages/lattice-paths.md)] - lattice paths in `d` dimensions, counted by a multinomial coefficient.
- [[convex-castle](pages/convex-castle.md)] - the stars-and-bars count `C(2h + w − 3, w − 1)`.
- [[urd-step-strings](pages/urd-step-strings.md)] - the step words over `{U, R, D}`.
- [[motzkin-numbers](pages/motzkin-numbers.md)], [[tower-word-language](pages/tower-word-language.md)] - the Motzkin paths and the tower words among the step words.
- [[permutation-inversions](pages/permutation-inversions.md)] - inversions of permutations of a set.
- [[convex-castle-binomial-identity](pages/convex-castle-binomial-identity.md)] - the product of two binomials in the convex count.
- [[multiset-partitions](pages/multiset-partitions.md)] - splitting a multiset into unordered blocks, the unordered counterpart.

## Footnotes

[^1]: [[aocp-multinomial-coefficients](pages/aocp-multinomial-coefficients.md)] §"Definition" L7-17 - "The multinomial coefficient generalizes the binomial coefficient ... instead of choosing k of n items, it divides n items into m labeled groups", "C(k_1 + k_2 + ... + k_m; k_1, k_2, ..., k_m) = (k_1 + ... + k_m)! / (k_1! k_2! ... k_m!) (AOCP V1 1.2.6 eq (38))", "the same as the permutations of a multiset with those multiplicities".
[^2]: [[aocp-multinomial-coefficients](pages/aocp-multinomial-coefficients.md)] §"Generalization of the Binomial Theorem" L21-25 - "The binomial theorem (eq (13)): (x+y)^n = sum_{0<=k<=n} C(n,k) x^k y^{n-k}", "Analogous multinomial theorem (eq (39)): (x_1 + x_2 + ... + x_m)^n = sum_{k_1 + ... + k_m = n} C(n; k_1, ..., k_m) x_1^{k_1} x_2^{k_2} ... x_m^{k_m}".
[^3]: [[aocp-multinomial-coefficients](pages/aocp-multinomial-coefficients.md)] §"Generalization of the Binomial Theorem" L27-31 - "Any multinomial coefficient can also be expressed as a product of binomial coefficients (the intermediate factorials telescope): C(k_1+...+k_m; k_1,...,k_m) = C(k_1+k_2, k_1) C(k_1+k_2+k_3, k_1+k_2) ... C(k_1+...+k_m, k_1+...+k_{m-1}) (AOCP V1 1.2.6, unnumbered)."
[^4]: Verified by execution (Python 3.11, 2026-10-16): `15!/(3! 4! 5! 3!) = 35 · 792 · 455 = 12 612 600`, `C(14, 4) C(10, 4) = 210 210`.
[^5]: https://oeis.org/A002426, https://oeis.org/A004149, https://oeis.org/A036038 (read 2026-10-16) - "Central trinomial coefficients: largest coefficient of (1 + x + x^2)^n", "Generalized Catalan numbers: a(n+1) = a(n) + Sum_{k=2..n-1} a(k)*a(n-1-k)", "Triangle T(n,k) read by rows: multinomial coefficients for the partitions of n listed in Abramowitz-Stegun order"; the word counts by enumeration of all words of length at most 8 (Python 3.11, 2026-10-16).
[^6]: Verified by execution (Python 3.11 with SymPy, 2026-10-16): the inversion sum over the permutations of the multisets with multiplicities `(1, 1, 1)`, `(2, 1, 1)`, `(2, 2, 1)`, `(2, 2, 2)`, `(3, 2, 2)`, `(1, 3, 2)`, `(4, 1, 2)` equals the q-multinomial coefficient and the product of two q-binomial coefficients.
