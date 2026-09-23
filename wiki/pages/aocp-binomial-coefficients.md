---
title: "AOCP Binomial Coefficients (Knuth TAOCP Vol. 1)"
category: Sources
summary: Knuth's binomial-coefficient identity toolkit — symmetry, addition, hockey-stick summation, negating the upper index, and Vandermonde's convolution (the identity that closes the convex-castle count).
tags: [knuth, taocp, binomial, vandermonde, hockey-stick, stirling, source]
sources: [aocp-binomial-coefficients]
created: 2026-09-14
updated: 2026-09-22
---

# The Art of Computer Programming (AOCP) Binomial Coefficients (Knuth The Art of Computer Programming (TAOCP) Vol. 1)

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

## More places these identities fire

- **Pascal's rule proves a castle theorem.** The doubling identity `H_{d+1} + μ² H_{d−1}` for the parity-sector factors of `char_k` on [[tower-parity-sectors](pages/tower-parity-sectors.md)] is proved by the addition formula `C(r,k) = C(r−1,k) + C(r−1,k−1)` applied to `H_d(μ) = Σ (−1)^i C(⌊(d+i)/2⌋, i) μ^{d−i}` - the first identity on this page doing structural work.
- **Vandermonde, from the concept side.** [[convex-castle](pages/convex-castle.md)] states the minimum-block characterization and the `C(2h+w−3, w−1)` count; [[convex-castle-binomial-identity](pages/convex-castle-binomial-identity.md)] proves it. The multinomial generalization of the same product-of-binomials pattern is on [[aocp-multinomial-coefficients](pages/aocp-multinomial-coefficients.md)].
- **Residue-filtered binomial sums.** The height-1 tower's block-count generating function (GF) `G_{1,L}(z) = Σ_r C(L+1, 2r) z^r` on [[block-count-constraints](pages/block-count-constraints.md)] is this page's `2^n` row split by a residue class of `r`: `z = 1` gives `2^L`, `z = −1` gives the alternating sum that is `P(1,L) = Re((1+i)^{L+1})`, and the even/odd classes are the every-4th sums A038503 / A038505. The degenerate alternating sum `P(k,1) = Σ_{c=0}^{k} (−1)^c = (1 + (−1)^k)/2` opens [[closed-form-hunting](pages/closed-form-hunting.md)].
- **The negative binomial's other home.** `1/(1−z)^{n+1} = Σ C(n+k, n) z^k` is developed as the geometric-GF power on the sibling Knuth page [[aocp-generating-functions](pages/aocp-generating-functions.md)].
- **Stirling first kind, `m = 1`.** `[n, 1] = (n−1)!` is the cycle count that anchors [[castles-as-upgraded-cycle-count](pages/castles-as-upgraded-cycle-count.md)]; the full triangle is the unsigned A132393, the second kind A008277, and Pascal's triangle itself A007318.[^8]
- **Stirling second kind, for multisets.** `{n k}` counts partitions of an `n`-set into `k` blocks; for a multiset the count splits four ways by whether blocks may repeat and whether a block may repeat an element, and all four collapse back to `{n k}` when nothing repeats - see [[multiset-partitions](pages/multiset-partitions.md)] and [[bender-1974-partitions-of-multisets](pages/bender-1974-partitions-of-multisets.md)].
- **A triangular-number cameo.** `F(4,2) = 10 = C(5,2)` - the hand-check on [[pe502-castle-cycle-permutations](pages/pe502-castle-cycle-permutations.md)] - is the `s = 0` term of `F(w,2) = Σ_s C(w+1, 4s+2)`; the triangular numbers A000217 count the height-2 castles whose second row is a single run.

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
- [[tower-parity-sectors](pages/tower-parity-sectors.md)] - Pascal's rule proving the `H_d` doubling identity.
- [[convex-castle](pages/convex-castle.md)] / [[aocp-multinomial-coefficients](pages/aocp-multinomial-coefficients.md)] - the Vandermonde count from the concept side, and its multinomial generalization.
- [[block-count-constraints](pages/block-count-constraints.md)] / [[closed-form-hunting](pages/closed-form-hunting.md)] - residue-filtered and alternating binomial sums on the castle.
- [[aocp-generating-functions](pages/aocp-generating-functions.md)] - the negative binomial as a geometric-GF power.
- [[castles-as-upgraded-cycle-count](pages/castles-as-upgraded-cycle-count.md)] / [[pe502-castle-cycle-permutations](pages/pe502-castle-cycle-permutations.md)] - `[n,1] = (n−1)!`, and `F(4,2) = C(5,2)`.

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
[^8]: https://oeis.org/A132393 (2026-09-19) — "Triangle of unsigned Stirling numbers of the first kind" 1; 0, 1; 0, 1, 1; 0, 2, 3, 1; 0, 6, 11, 6, 1; …; https://oeis.org/A008277 (2026-09-19) — "Triangle of Stirling numbers of the second kind" 1; 1, 1; 1, 3, 1; 1, 7, 6, 1; …; https://oeis.org/A000217 (2026-09-19) — "Triangular numbers: a(n) = binomial(n+1,2)" 0, 1, 3, 6, 10, 15, 21, …
