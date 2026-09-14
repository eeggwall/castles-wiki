---
title: "AOCP Binomial Coefficients (Knuth TAOCP Vol. 1)"
category: Sources
summary: Knuth's binomial-coefficient identity toolkit — symmetry, addition, hockey-stick summation, negating the upper index, and Vandermonde's convolution (the identity that closes the convex-castle count).
tags: [knuth, taocp, binomial, vandermonde, hockey-stick, stirling, source]
sources: [aocp-binomial-coefficients]
created: 2026-09-14
updated: 2026-09-14
---

# AOCP Binomial Coefficients (Knuth TAOCP Vol. 1)

**Source:** https://charlesreid1.com/wiki/AOCP/Binomial_Coefficients (notes on Knuth, *The Art of Computer Programming*, Vol. 1, §1.2.6)
**Date ingested:** 2026-09-14
**Type:** article (MediaWiki notes page); reference

## Summary

Knuth's toolkit of binomial-coefficient identities — the machinery underneath every binomial count in the wiki. `C(n,k) = n!/(k!(n−k)!)`, extended to real upper index `r` by the falling factorial.[^1] The identities the castle work leans on (all re-verified during ingest):

- **Symmetry** `C(n,k) = C(n,n−k)` and **addition** `C(r,k) = C(r−1,k) + C(r−1,k−1)` (Pascal's rule).[^2]
- **Hockey-stick summations:** `∑_{0≤k≤n} C(r+k,k) = C(r+n+1,n)` and `∑_{0≤k≤n} C(k,m) = C(n+1,m+1)`.[^3]
- **Negating the upper index:** `C(−r,k) = (−1)^k C(r+k−1,k)` — the bridge between ordinary and "negative" binomials, hence between unsigned and signed/alternating sums.[^4]
- **Vandermonde's convolution** (eq (21), "should be memorized"): `∑_k C(r,k) C(s,n−k) = C(r+s,n)`.[^5]
- **`∑_k C(n,k) = 2^n`** and the alternating **`∑_k (−1)^k C(n,k) = 0`** (from `(1±1)^n`).[^6]
- **Stirling numbers** (first kind = permutations by cycle count, second kind = set partitions) converting between powers and falling factorials.[^7]

## Relevance to the castle

Several of these are not background but the *exact* identities the castle counts use:

- **Vandermonde closes the convex-castle count.** The proof that `convex(w,h) = C(2h+w−3, w−1)` is a generalized Vandermonde convolution of the ascending-front and descending-back counts — see [[convex-castle-binomial-identity](pages/convex-castle-binomial-identity.md)]. This page is that identity's home (eq (21)).
- **Hockey-stick and negative binomial.** `∑ C(r+k,k) = C(r+n+1,n)` and the negative-binomial form `1/(1−z)^{m+1} = ∑ C(k+m,m) z^k` (from negating the upper index) are the tower / Narayana-denominator counts of [[tower-narayana-polynomial](pages/tower-narayana-polynomial.md)] and [[generating-functions](pages/generating-functions.md)].
- **`2^n` and the alternating sum** are the castle's building blocks: `2^n` is the [[binary-string-bijection](pages/binary-string-bijection.md)] block-configuration count, and the `(1±sgn)/2` parity projector of [[castle-sign](pages/castle-sign.md)] is the alternating sum made into an even/odd split. The height-2 [[hyperbolic-sequence-family](pages/hyperbolic-sequence-family.md)] (`sum every 4th binomial`) is a residue-refined version.
- **Stirling numbers** link to the permutation-cycle side of the [[permutation-cycle-castle-analogy](pages/permutation-cycle-castle-analogy.md)] (first-kind = permutations by cycle count).

## Key Takeaways

- Full identity toolkit: symmetry, Pascal addition, hockey-stick summation, negate-upper-index, product-simplification.[^2][^3][^4]
- **Vandermonde `∑_k C(r,k)C(s,n−k) = C(r+s,n)`** — the identity that closes `convex(w,h) = C(2h+w−3,w−1)`.[^5]
- `∑ C(n,k) = 2^n`, alternating sum `= 0` — the block count and the parity projector.[^6]
- Negative binomial via upper-index negation — the tower / `(1−z)^{m+1}` denominators.[^4]

## Entities & Concepts

- [[convex-castle-binomial-identity](pages/convex-castle-binomial-identity.md)] — the generalized-Vandermonde proof this page's eq (21) drives.
- [[binary-string-bijection](pages/binary-string-bijection.md)] — the `2^n` count; [[castle-sign](pages/castle-sign.md)] — the alternating-sum parity projector.
- [[hyperbolic-sequence-family](pages/hyperbolic-sequence-family.md)] — residue-filtered binomial sums.
- [[generating-functions](pages/generating-functions.md)] / [[tower-narayana-polynomial](pages/tower-narayana-polynomial.md)] — the negative-binomial denominators.
- [[permutation-cycle-castle-analogy](pages/permutation-cycle-castle-analogy.md)] — Stirling first-kind = permutations by cycle count.

Related: [[aocp-multinomial-coefficients](pages/aocp-multinomial-coefficients.md)] (ingested). Linked from the source but not yet ingested: Cards.

## Relation to Other Wiki Pages

The reference behind the wiki's "the castle is binomial, not Catalan" thesis: it is the home of Vandermonde's convolution (which closes the convex-castle count) and of the `2^n` / alternating-sum / negative-binomial identities that recur throughout the castle machinery.

## Footnotes

[^1]: [[aocp-binomial-coefficients](pages/aocp-binomial-coefficients.md)] §"Definitions" L5-14 — "C(n,k) = n!/(k!(n-k)!) ... For non-integer n, C(r,k) = r(r-1)...(r-k+1)/(k(k-1)...1) = prod_{1<=j<=k}(r+1-j)/j."
[^2]: [[aocp-binomial-coefficients](pages/aocp-binomial-coefficients.md)] §"Symmetry Condition"/"Addition formulas" L22, L32 — "C(n,k) = C(n,n-k)" and "C(r,k) = C(r-1,k) + C(r-1,k-1)."
[^3]: [[aocp-binomial-coefficients](pages/aocp-binomial-coefficients.md)] §"Summation formulas" L36-40 — "sum_{0<=k<=n} C(r+k,k) = C(r+n+1,n)" and "sum_{0<=k<=n} C(k,m) = C(n+1,m+1)"; both re-verified during ingest.
[^4]: [[aocp-binomial-coefficients](pages/aocp-binomial-coefficients.md)] §"Negating Upper Index" L57 — "C(-r,k) = (-1)^k C(r+k-1,k)"; re-verified during ingest (C(-4,3) = -20 = (-1)^3 C(6,3)).
[^5]: [[aocp-binomial-coefficients](pages/aocp-binomial-coefficients.md)] §"Sums of Products" L68-70 — "Vandermonde's convolution ... sum_k C(r,k) C(s,n-k) = C(r+s,n) ... should be memorized"; re-verified during ingest.
[^6]: [[aocp-binomial-coefficients](pages/aocp-binomial-coefficients.md)] §"Knuth AOCP Section 1.2.6 Problem 36" L91-93 — "sum_k C(n,k) = 2^n ... sum_k C(n,k)(-1)^k = (1-1)^n = 0^n = 0 for n>0"; both re-verified during ingest.
[^7]: [[aocp-binomial-coefficients](pages/aocp-binomial-coefficients.md)] §"Stirling Numbers" L78-85 — "first kind [n m] (permutations of n letters with m cycles), second kind {n m} (partitions of n elements into m nonempty subsets) ... n! C(x,n) = sum_k (-1)^{n-k} [n k] x^k ... x^n = sum_k {n k} C(x,k) k!."
