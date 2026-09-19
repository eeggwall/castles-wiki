---
title: "AOCP Multinomial Coefficients (Knuth TAOCP Vol. 1)"
category: Sources
summary: The multinomial coefficient n!/(k_1!…k_m!) — the multinomial theorem and the telescoping factorization into a product of binomials, the mechanism behind the higher-dimensional lattice-path count.
tags: [knuth, taocp, multinomial, binomial, multiset, lattice-path, source]
sources: [aocp-multinomial-coefficients]
created: 2026-09-14
updated: 2026-09-19
---

# AOCP Multinomial Coefficients (Knuth TAOCP Vol. 1)

**Source:** https://charlesreid1.com/wiki/AOCP/Multinomial_Coefficients (notes on Knuth, *The Art of Computer Programming*, Vol. 1, §1.2.6)
**Date ingested:** 2026-09-14
**Type:** article (MediaWiki notes page); short reference

## Summary

The **multinomial coefficient** generalizes the [[aocp-binomial-coefficients](pages/aocp-binomial-coefficients.md)]: instead of choosing *k* of *n*, it divides *n* items into *m* labeled groups of sizes `k_1,…,k_m`:[^1]

```
C(n; k_1, …, k_m) = n! / (k_1! k_2! … k_m!),   n = k_1 + … + k_m
```

It counts exactly the permutations of a multiset with those multiplicities — the same quantity as [[aocp-multisets](pages/aocp-multisets.md)].[^1] It appears in the **multinomial theorem**, the generalization of the binomial theorem:[^2]

```
(x_1 + … + x_m)^n = ∑_{k_1+…+k_m = n} C(n; k_1,…,k_m) x_1^{k_1} … x_m^{k_m}
```

The key structural fact is that a multinomial **telescopes into a product of binomials** — the intermediate factorials cancel:[^3]

```
C(k_1+…+k_m; k_1,…,k_m) = C(k_1+k_2, k_1) · C(k_1+k_2+k_3, k_1+k_2) · … · C(k_1+…+k_m, k_1+…+k_{m−1})
```

(re-verified during ingest, e.g. `C(15; 3,4,5,3) = C(7,3)·C(12,7)·C(15,12) = 12,612,600`).

## Relevance to the castle

Two concrete connections, both on the enumeration side:

- **The higher-dimensional lattice-path count is this telescoping.** [[lattice-paths](pages/lattice-paths.md)] counts *d*-dimensional shortest paths by the multinomial `C(N; N_1,…,N_d)`, computed as the telescoping product of binomials — exactly the identity above. Its worked 4-D example `C(15; 3,4,5,3) = 12,612,600 = C(14,4)·C(10,4)·…` *is* this factorization (verified). The multinomial is thus the general form of the stars-and-bars binomial count the castle's [[convex-castle](pages/convex-castle.md)] enumeration also uses.
- **Two-line-array counts are binomial products.** The multiset-permutation counts on [[aocp-multisets](pages/aocp-multisets.md)] (e.g. `C(A,A−k−m) C(B,m) C(C,k) …`) are multinomials factored into binomial products by the same telescoping — the counting template behind the castle's own placement/insertion arguments.

## Three more castle appearances

- **The U/R/D string is a three-letter multiset permutation.** A castle's step string over `{U, R, D}` with prescribed letter counts is exactly a permutation of the multiset `{#U·U, #R·R, #D·D}`, so the *unconstrained* count is a trinomial coefficient. Words of length `n` over three letters with `#U − #D = k` are the coefficients of `(1 + x + x²)^n` - the trinomial triangle A027907 - and the height-0 diagonal is the central trinomial A002426 (1, 1, 3, 7, 19, 51, 141, …).[^4] The castle grammar's ballot and run constraints ([[urd-step-strings](pages/urd-step-strings.md)], [[tower-word-language](pages/tower-word-language.md)]) cut these down to Motzkin-type counts ([[motzkin-numbers](pages/motzkin-numbers.md)]) - the multinomial is the ceiling the grammar prunes from.
- **The q-multinomial is the q-thread's multiset case.** MacMahon's theorem: permutations of a multiset counted by inversions give the *Gaussian* multinomial coefficient, and it telescopes into Gaussian binomials exactly as the identity above telescopes into ordinary ones. This is the multiset form of the q-factorial on [[aocp-combinatorics](pages/aocp-combinatorics.md)] and [[permutation-inversions](pages/permutation-inversions.md)], and it is what an inversion-graded count of U/R/D strings would be built from.
- **The convex-castle proof is a two-part telescope.** The up/down decomposition at the peak on [[convex-castle-binomial-identity](pages/convex-castle-binomial-identity.md)] writes the count as a product of two binomials and then re-sums it with Vandermonde; the multinomial-into-binomials factorization is the general pattern that product instantiates.

**OEIS.** The multinomial coefficients themselves are tabulated as A036038 (rows indexed by the partitions of `n`).[^4]

## Key Takeaways

- `C(n; k_1,…,k_m) = n!/(k_1!…k_m!)` = the multiset-permutation count.[^1]
- **Multinomial theorem** expands `(x_1+…+x_m)^n`.[^2]
- **Telescoping into binomials** `C(n; k_1,…) = ∏_i C(k_1+…+k_i, k_1+…+k_{i−1})` — the mechanism of the higher-D lattice-path count (verified).[^3]

## Entities & Concepts

- [[aocp-binomial-coefficients](pages/aocp-binomial-coefficients.md)] — the binomials this factors into.
- [[aocp-multisets](pages/aocp-multisets.md)] — the multiset-permutation interpretation.
- [[lattice-paths](pages/lattice-paths.md)] — the higher-D path count = the telescoping multinomial.
- [[convex-castle](pages/convex-castle.md)] — the castle's stars-and-bars binomial count, of which the multinomial is the general form.
- [[urd-step-strings](pages/urd-step-strings.md)] / [[tower-word-language](pages/tower-word-language.md)] / [[motzkin-numbers](pages/motzkin-numbers.md)] - the U/R/D string as a constrained three-letter multiset permutation; trinomial coefficients as its ceiling.
- [[aocp-combinatorics](pages/aocp-combinatorics.md)] / [[permutation-inversions](pages/permutation-inversions.md)] - the q-multinomial (MacMahon), the inversion-graded version of this page's telescoping.
- [[convex-castle-binomial-identity](pages/convex-castle-binomial-identity.md)] - the two-binomial product the peak decomposition produces.

## Relation to Other Wiki Pages

The third corner of the AOCP binomial/multiset/multinomial triangle. Its lasting content for the castle is the telescoping factorization — the general mechanism behind the higher-dimensional lattice-path count and the two-line-array binomial products, both kin to the castle's stars-and-bars convex enumeration.

## Footnotes

[^1]: [[aocp-multinomial-coefficients](pages/aocp-multinomial-coefficients.md)] §"Definition" L7-17 — "generalizes the binomial coefficient ... C(n; k_1, ..., k_m) = n!/(k_1! k_2! ... k_m!) ... counts the ways to divide n items into m labeled groups ... the same as the permutations of a multiset with those multiplicities."
[^2]: [[aocp-multinomial-coefficients](pages/aocp-multinomial-coefficients.md)] §"Generalization of the Binomial Theorem" L23-25 — "(x_1 + x_2 + ... + x_m)^n = sum_{k_1 + ... + k_m = n} C(n; k_1, ..., k_m) x_1^{k_1} x_2^{k_2} ... x_m^{k_m}" (eq (39)).
[^3]: [[aocp-multinomial-coefficients](pages/aocp-multinomial-coefficients.md)] §"Generalization of the Binomial Theorem" L27-29 — "C(k_1+...+k_m; k_1,...,k_m) = C(k_1+k_2, k_1) C(k_1+k_2+k_3, k_1+k_2) ... C(k_1+...+k_m, k_1+...+k_{m-1})"; telescoping re-verified during ingest (incl. C(15;3,4,5,3) = 12,612,600).
[^4]: https://oeis.org/A027907 (2026-09-19) — "Triangle of trinomial coefficients T(n,k) (n >= 0, 0 <= k <= 2*n), read by rows: n-th row is obtained by expanding (1 + x + x^2)^n"; https://oeis.org/A002426 (2026-09-19) — "Central trinomial coefficients: largest coefficient of (1 + x + x^2)^n" 1, 1, 3, 7, 19, 51, 141, 393, …; https://oeis.org/A036038 (2026-09-19) — "Triangle T(n,k) read by rows: multinomial coefficients for the partitions of n listed in Abramowitz-Stegun order."
