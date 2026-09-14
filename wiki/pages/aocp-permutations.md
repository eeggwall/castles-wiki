---
title: "AOCP Permutations & Factorials (Knuth TAOCP Vol. 1)"
category: Sources
summary: Knuth's Vol. 1 basics — permutation counts n!, the insert-into-every-slot construction, factorial identities (Stirling's formula, Legendre's prime-multiplicity formula for n!).
tags: [knuth, taocp, permutations, factorial, stirling, legendre, source]
sources: [aocp-permutations]
created: 2026-09-13
updated: 2026-09-13
---

# AOCP Permutations & Factorials (Knuth TAOCP Vol. 1)

**Source:** https://charlesreid1.com/wiki/AOCP/Permutations (notes on Knuth, *The Art of Computer Programming*, Vol. 1, Ch. 1)
**Date ingested:** 2026-09-13
**Type:** article (MediaWiki notes page); largely foundational/reference

## Summary

Basic permutation and factorial facts from TAOCP Vol. 1. Arranging *n* distinct objects in a row gives `n!` orderings; choosing and ordering *k* of *n* gives the falling factorial `p_{n,k} = n(n−1)···(n−k+1)`.[^1] The page highlights the inductive **construction of permutations** — given all permutations of `n−1` objects, form each permutation of *n* by **inserting the new element into every open slot** (the *n* slots of an `(n−1)`-permutation).[^2] (A second "Method 2" from Knuth is transcribed but the note-taker could not reconstruct it — recorded as unresolved on the source.)

The factorial identities are the useful part:[^3]

- Definition `n! = ∏_{1≤k≤n} k`, `0! = 1`, `n! = (n−1)!·n`; `10! = 3,628,800` as a rough "ceiling on brute-force enumeration."
- **Stirling's formula** `n! ≈ √(2πn)·(n/e)^n`, relative error ≈ `1/(12n)` (e.g. `8! = 40320 ≈ 39902`, verified).
- **Legendre's formula** for the multiplicity of a prime *p* in `n!`: `μ = Σ_{k>0} floor(n/p^k)`, with the fast nested-floor identity `floor(n/p^{k+1}) = floor(floor(n/p^k)/p)`. Example: 3 divides `1000!` with multiplicity `333+111+37+12+4+1 = 498` (verified) — so `3^498 ‖ 1000!`.[^4]

It points to the AOCP subpages for Binomial Coefficients, Multinomial Coefficients, and Generating Functions (not yet ingested).

## Relevance to the castle

The connection is foundational rather than deep, but real on two points:

- **Insert-into-every-slot construction.** Knuth's way of building permutations — insert the new element into each open slot of a smaller object — is the same combinatorial move as the castle's enumeration: the [[convex-castle](pages/convex-castle.md)] count and the [[lattice-paths](pages/lattice-paths.md)] path count both come from inserting items (extra `R`s, down-moves) into the available slots of a base string, i.e. stars-and-bars. It is the permutation-theory root of that binomial mechanism, and the natural companion to the *inversion*-table view on [[permutation-inversions](pages/permutation-inversions.md)] (the same permutations, encoded by counts rather than constructed by insertion).
- **Scale and factoring.** Stirling's formula is exactly the tool for the castle's astronomical counts (`F(13,10) ~ 4×10^12`), and Legendre's prime-multiplicity formula is the machinery behind the verified castle factorizations recorded on [[castle-counting-formula](pages/castle-counting-formula.md)] (`F(13,10) = 2²·3·13·1163·20553887`).

## Key Takeaways

- `n!` orderings of *n* objects; falling factorial `p_{n,k} = n(n−1)···(n−k+1)`.[^1]
- Permutations built inductively by **inserting the new element into every slot** — the stars-and-bars root shared with the castle's convex/lattice counts.[^2]
- **Stirling** `n! ≈ √(2πn)(n/e)^n` (verified `8!≈39902`) and **Legendre** `μ = Σ floor(n/p^k)` (verified `3^498 ‖ 1000!`).[^3][^4]

## Entities & Concepts

- [[permutation-inversions](pages/permutation-inversions.md)] — the inversion-table encoding of the same permutations (counts vs. construction).
- [[convex-castle](pages/convex-castle.md)] / [[lattice-paths](pages/lattice-paths.md)] — the stars-and-bars insertions that mirror the permutation construction.
- [[castle-counting-formula](pages/castle-counting-formula.md)] — the verified castle factorizations Legendre's formula underlies.

Linked from the source: AOCP/Generating Functions is ingested ([[aocp-generating-functions](pages/aocp-generating-functions.md)]); AOCP/Binomial Coefficients and AOCP/Multinomial Coefficients are not yet ingested.

## Relation to Other Wiki Pages

A reference page for the permutation/factorial substrate beneath the wiki's combinatorics. Its lasting value here is the insert-into-slots construction (the stars-and-bars root) and the Stirling/Legendre tools that quantify and factor the castle's large counts; it complements the inversion-side view of [[aocp-combinatorics](pages/aocp-combinatorics.md)] and [[permutation-inversions](pages/permutation-inversions.md)].

## Footnotes

[^1]: [[aocp-permutations](pages/aocp-permutations.md)] §"Permutations and Factorials" L7-21 — "we can arrange these things in n! different ways ... p_{n,k} = n(n-1)(...)(n-k+1) ... p_{n,n} = n (n-1) ... (2)(1)."
[^2]: [[aocp-permutations](pages/aocp-permutations.md)] §"Permutations and Factorials" L33-56 — "For each permutation of n-1 elements, form n additional permutations by inserting the nth element in every possible open slot"; Method 2 transcribed but left unresolved ("Aaaaaand... yeah. No idea.").
[^3]: [[aocp-permutations](pages/aocp-permutations.md)] §"Factorial Identities" L60-98 — "n! = ∏_{1≤k≤n} k ... 0! = 1 ... n! = (n-1)! n ... 10! = 3,628,800 ... n! ≈ √(2πn)(n/e)^n ... 8! ≈ 39902 ... Relative error ... 1/(12n)"; Stirling 8!≈39902 re-verified during ingest.
[^4]: [[aocp-permutations](pages/aocp-permutations.md)] §"Factorial Identities" L100-126 — "the prime p is a divisor of n! with multiplicity μ = Σ_{k>0} floor(n/p^k) ... for n = 1000, p = 3 ... μ = 333 + 111 + 37 + 12 + 4 + 1 = 498 ... 1000! is divisible by 3^498, but not 3^499 ... floor(n/p^{k+1}) = floor(floor(n/p^k)/p)"; μ(1000,3)=498 re-verified during ingest.
