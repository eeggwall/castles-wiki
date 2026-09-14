---
title: "AOCP Multisets (Knuth TAOCP Vol. 3)"
category: Sources
summary: Knuth's multiset permutations — the multinomial coefficient, two-line arrays, Foata's intercalation product, and the cycle-factorization of two-line arrays that grounds the castle's permutation-cycle analogy.
tags: [knuth, taocp, multiset, multinomial, foata, cycle-factorization, two-line-array, source]
sources: [aocp-multisets]
created: 2026-09-14
updated: 2026-09-14
---

# AOCP Multisets (Knuth TAOCP Vol. 3)

**Source:** https://charlesreid1.com/wiki/AOCP/Multisets (notes on Knuth, *The Art of Computer Programming*, Vol. 3, §5.1.2 "Permutations of a Multiset")
**Date ingested:** 2026-09-14
**Type:** article (MediaWiki notes page)

## Summary

Permutations of a **multiset** are counted by the **multinomial coefficient**: for `M = {n_1·a_1, n_2·a_2, …}` of total size `n`, the number of distinct arrangements is `C(n; n_1, n_2, …) = n!/(n_1! n_2! …)` (e.g. `{3a,2b,c,4d}` gives `10!/(3!2!1!4!) = 12600`, verified).[^1] This is the same count as the [[lattice-paths](pages/lattice-paths.md)] step-string permutations.

The page's substantive content is Foata's apparatus for multiset permutations, built on **two-line arrays** — top row the multiset in non-decreasing order, bottom row the permutation:[^2]

- **Foata's intercalation product** `a ⊤ b`: concatenate two two-line arrays and **stable-sort the columns by the top line** (ties keep left-to-right order). Worked example: `c a d a b ⊤ b d d a d = c a b d d a b d a d`.[^2]
- **Cycle factorization of a two-line array.** Removing the "agreeing" columns (a/a, b/b, c/c), the only prime cycles on `{a,b,c}` are `(ab), (ac), (bc), (abc), (acb)`, and since any two share a letter the factorization is **unique**; counting a permutation class two ways (directly, and by cycle factorization) yields a binomial identity, which Knuth reconciles with a Vandermonde–Chu three-term identity.[^3]
- Worked enumeration examples: strings with prescribed adjacent-pair counts, counted by products of binomials via the two-line-array placement (`C(A,A−k−m) C(B,m) C(C,k) C(B+k,B−l) C(C−k,l)`).[^4]

## Relevance to the castle

This page is the **source-level root of the castle's permutation-cycle machinery**:

- **Two-line arrays + cycle factorization** are exactly what the [[permutation-cycle-castle-analogy](pages/permutation-cycle-castle-analogy.md)] mirrors: Knuth's unique factorization of a (two-line) permutation into disjoint cycles is the permutation side of "permutation cycles ↔ castle peaks," and Foata's canonical-cycle apparatus is the source of the [[castle-foata-transform](pages/castle-foata-transform.md)]. The `(ab),(ac),(bc),(abc),(acb)` prime-cycle enumeration is the concrete Vol. 3 example those pages generalize.
- **The multinomial count** is the [[lattice-paths](pages/lattice-paths.md)] path count and the stars-and-bars mechanism shared with the [[convex-castle](pages/convex-castle.md)] enumeration.
- **Adjacent-pair-constrained counting** (no `ca`, no `db`, etc.) rhymes with the castle's own adjacency/run constraints (no same-row touching, the no-`UD`/no-`DU` tower-word rules); the two-line-array placement method is a template for such constrained counts.

## Key Takeaways

- Multiset permutations = multinomial `n!/(n_1!n_2!…)` (`10!/(3!2!1!4!) = 12600`, verified).[^1]
- **Two-line arrays** and **Foata's intercalation product** (stable column-sort by the top line).[^2]
- **Unique cycle factorization** of a two-line array into prime cycles `(ab),(ac),(bc),(abc),(acb)` — the source of the castle's cycle analogy.[^3]
- Constrained-adjacency counts via binomial products over two-line-array placements.[^4]

## Entities & Concepts

- [[permutation-cycle-castle-analogy](pages/permutation-cycle-castle-analogy.md)] — the cycle factorization this page grounds (Knuth/Foata).
- [[castle-foata-transform](pages/castle-foata-transform.md)] — the castle analogue of Foata's canonical-cycle apparatus.
- [[lattice-paths](pages/lattice-paths.md)] / [[convex-castle](pages/convex-castle.md)] — the multinomial / stars-and-bars counts.
- [[aocp-binomial-coefficients](pages/aocp-binomial-coefficients.md)] — the Vandermonde–Chu identity used to reconcile the two counts.

Linked from the source but not yet ingested: AOCP/Multinomial Coefficients.

## Relation to Other Wiki Pages

The Vol. 3 source beneath the castle's cycle-factorization reading: Knuth's two-line arrays, Foata intercalation, and unique cycle factorization are the classical machinery that [[permutation-cycle-castle-analogy](pages/permutation-cycle-castle-analogy.md)] and [[castle-foata-transform](pages/castle-foata-transform.md)] carry over to castle peaks/excursions. Its multinomial count ties back to lattice paths and the castle's stars-and-bars convex count.

## Footnotes

[^1]: [[aocp-multisets](pages/aocp-multisets.md)] §"Multiset Permutations" L7-13 — "N_perm = 10!/(3! 2! 1! 4!) ... the multinomial coefficient C(n; n_1, n_2, ...) = n!/(n_1! n_2! ...)"; 10!/(3!2!1!4!) = 12600 re-verified during ingest.
[^2]: [[aocp-multisets](pages/aocp-multisets.md)] §"Multiset Permutations" L16-25 — "Foata (1969) ... the intercalation product ... Two-line notation ... top line = elements of M in non-decreasing order; bottom line = the permutation ... place the two two-line arrays side by side, then STABLE-sort the columns ... c a d a b (top) b d d a d = c a b d d a b d a d."
[^3]: [[aocp-multisets](pages/aocp-multisets.md)] §"Another Multiset Example" L47-53 — "with a/a,b/b,c/c removed the only prime cycles are (a b),(a c),(b c),(a b c),(a c b), and any two share a letter so the factorization is unique (eq (24)) ... Knuth simplifies with the three-term identity (eq (27), = AOCP V1 exercise 1.2.6-31, Vandermonde-Chu type)."
[^4]: [[aocp-multisets](pages/aocp-multisets.md)] §"Complicated Multiset Counting Example"/"Another Multiset Example" L27-45 — "C(A, A-k-m) C(B, m) C(C, k) C(B+k, B-l) C(C-k, l)" (eq (20)) and "N(A,B,C,m) = C(A,m) C(B, C-A+m) C(C, B-m)" (eq (23))."
