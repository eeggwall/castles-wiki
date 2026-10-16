---
title: "AOCP Permutations & Factorials (Knuth TAOCP Vol. 1)"
category: Sources
summary: Notes on Knuth's Vol. 1 basics - n! arrangements of n objects and the falling factorial p_{n,k}, permutations of n built from those of n − 1 by inserting the new element into every slot, Stirling's formula with relative error about 1/(12n), and the multiplicity of a prime p in n! as Σ floor(n/p^k) (498 for p = 3, n = 1000). On the castle side, the rainbow castles of height h number h!, and inserting n with j elements to its right adds j inversions, which gives the q-factorial.
tags: [knuth, taocp, permutations, factorial, stirling, source]
sources: [aocp-permutations]
created: 2026-09-13
updated: 2026-10-16
---

# AOCP Permutations & Factorials (Knuth, *The Art of Computer Programming*, Vol. 1)

**Source:** https://charlesreid1.com/wiki/AOCP/Permutations (notes on Knuth, *The Art of Computer Programming*, Vol. 1, Ch. 1)
**Date ingested:** 2026-09-13
**Type:** article (MediaWiki notes page)

## Summary

The notes cover the basic counts of Vol. 1, Ch. 1. Arranging `n` distinct objects in a row gives `n!` orderings, and choosing and arranging `k` of `n` gives the falling factorial `p_{n,k} = n(n−1)⋯(n−k+1)`.[^1]

**Building permutations.** All permutations of `n` objects come from those of `n − 1` by inserting the `n`-th element into each of the `n` open slots. The notes' example inserts 4 into the permutation `2 3 1`, giving `4 2 3 1`, `2 4 3 1`, `2 3 4 1` and `2 3 1 4`. They begin a second method, which appends a value `1/2, 3/2, …, n − 1/2` to each permutation of `n − 1` elements, and leave it unfinished.[^2]

**Factorial identities.**[^3]

- `n! = Π_{1≤k≤n} k`, with `0! = 1`, so `n! = (n−1)!·n` for every positive integer `n`; `10! = 3 628 800`, which the notes call "an upper ceiling on computable tasks".
- Stirling's formula `n! ≈ √(2πn) (n/e)^n`, with relative error about `1/(12n)`. At `n = 8` it gives `39902` against `8! = 40320`, a relative error of `0.0104`, against `1/96 = 0.0104`.

The prime `p` divides `n!` with multiplicity[^4]

```
μ  =  Σ_{k>0} floor(n/p^k),        floor(n/p^{k+1})  =  floor(floor(n/p^k)/p).
```

At `n = 1000` and `p = 3`, `μ = 333 + 111 + 37 + 12 + 4 + 1 = 498`, so `3^498` divides `1000!` and `3^499` does not.

The notes point to the AOCP subpages on binomial coefficients, multinomial coefficients and generating functions.

## Castle readings

These readings are the wiki's; the notes do not mention castles.

- **Insertion and inversions.** Inserting `n` into a permutation of `{1, …, n − 1}` with `j` elements to its right adds exactly `j` inversions, the pairs `(n, x)` with `x` to the right of `n`. Since `j` ranges over `0, …, n − 1`, the permutations of `n` by inversions have generating function `G_{n−1}(z)·(1 + z + ⋯ + z^{n−1})`, the product form of the q-factorial on [[permutation-inversions](pages/permutation-inversions.md)].[^5]
- **Rainbow castles.** A rainbow castle has width `w = h` and column heights forming a permutation of `{1, …, h}`; each such skyline reaches `h`, so the rainbow castles of height `h` number `h! = A000142(h)` ([[castle-classification-shape](pages/castle-classification-shape.md)]).[^6] The `(n − 1)!` cyclic orders of `n` labeled points that [[castles-as-upgraded-cycle-count](pages/castles-as-upgraded-cycle-count.md)] starts from are `n!/n`, the Stirling number `[n 1]` of [[aocp-binomial-coefficients](pages/aocp-binomial-coefficients.md)].
- **Stirling's formula.** [[algebraic-transcendental-wall](pages/algebraic-transcendental-wall.md)] applies it to `C(2n, n) = (2n)!/(n!)²`. In base 2, `log₂ n! = n log₂ n − n log₂ e + O(log n)` is the entropy of a uniform random permutation of `n` elements; [[castle-entropy](pages/castle-entropy.md)] gives the corresponding statement for castles, `log₂ A^e(w, h) = log₂ A(w, h) − 1 + log₂(1 + S/A)`.
- **Slot insertion with identical items.** The convex castle count on [[convex-castle](pages/convex-castle.md)] and the lattice-path counts on [[lattice-paths](pages/lattice-paths.md)] also insert items into the slots of a base word, but the items are identical letters, so the count is by stars and bars rather than a product.

## Entities & Concepts

- [[permutation-inversions](pages/permutation-inversions.md)] - inversions and the q-factorial, whose product form is the insertion step of the section *Castle readings*.
- [[castle-classification-shape](pages/castle-classification-shape.md)] - the rainbow castles, `h!` of them at height `h`.
- [[castles-as-upgraded-cycle-count](pages/castles-as-upgraded-cycle-count.md)] - the `(n − 1)!` cyclic orders of `n` points.
- [[aocp-binomial-coefficients](pages/aocp-binomial-coefficients.md)] - the Stirling numbers `[n m]`, with `[n 1] = (n − 1)!`.
- [[algebraic-transcendental-wall](pages/algebraic-transcendental-wall.md)] - Stirling's formula applied to the central binomial coefficients.
- [[castle-entropy](pages/castle-entropy.md)] - the information content of castles, against `log₂ n!` for permutations.
- [[convex-castle](pages/convex-castle.md)], [[lattice-paths](pages/lattice-paths.md)] - counts by inserting identical letters into the slots of a word.

Linked from the source: [[aocp-binomial-coefficients](pages/aocp-binomial-coefficients.md)], [[aocp-multinomial-coefficients](pages/aocp-multinomial-coefficients.md)], [[aocp-generating-functions](pages/aocp-generating-functions.md)].

## Relation to Other Wiki Pages

[[aocp-combinatorics](pages/aocp-combinatorics.md)] and [[permutation-inversions](pages/permutation-inversions.md)] count the same permutations by inversions; the insertion step of this page is the factor `1 + z + ⋯ + z^{n−1}` of their q-factorial.

## Footnotes

[^1]: [[aocp-permutations](pages/aocp-permutations.md)] §"Permutations and Factorials" L7-21 - "If we have n distinct objects to arrange in a row, and order of placement matters, we can arrange these things in n! different ways", "p_{n,k} = n(n-1)(...)(n-k+1)".
[^2]: [[aocp-permutations](pages/aocp-permutations.md)] §"Permutations and Factorials" L33-56 - "For each permutation of n-1 elements, form n additional permutations by inserting the nth element in every possible open slot", "Adding 4 to our set of objects and using method 1 gives: (4 2 3 1), (2 4 3 1), (2 3 4 1), (2 3 1 4)", and Method 2's array with entries 1/2, 3/2, …, n − 1/2, after which the notes stop.
[^3]: [[aocp-permutations](pages/aocp-permutations.md)] §"Factorial Identities" L60-98 - "n! = 1 · 2 … n", "0! = 1", "n! = (n-1)! n", "10! = 3,628,800", "10! represents an upper ceiling on computable tasks", "n! ≈ √(2πn)(n/e)^n", "8! ≈ 4√π(8/e)^8 ≈ 39902", "Relative error of Stirling's formula is approximately 1/(12n)".
[^4]: [[aocp-permutations](pages/aocp-permutations.md)] §"Factorial Identities" L100-126 - "the prime p is a divisor of n! with multiplicity μ = Σ_{k>0} floor(n/p^k)", "μ = 333 + 111 + 37 + 12 + 4 + 1 = 498", "1000! is divisible by 3^498, but not by 3^499", "floor(n/p^{k+1}) = floor(floor(n/p^k)/p)".
[^5]: Verified by execution (Python 3.11, 2026-10-16): inserting `n` with `j` elements to its right adds `j` inversions, for every permutation of `{1, …, n − 1}` and every `j`, `n ≤ 6`; `√(2π·8)(8/e)^8 = 39902.4`, relative error `0.01036`; the multiplicity of 3 in `1000!` is 498.
[^6]: https://oeis.org/A000142 (2026-09-19) - "Factorial numbers: n! = 1*2*3*4*...*n (order of symmetric group S_n, number of permutations of n letters)".
