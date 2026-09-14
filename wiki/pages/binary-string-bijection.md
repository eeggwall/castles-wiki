---
title: Binary-string bijection
category: Concepts
summary: Configurations of non-overlapping, non-adjacent sub-blocks in a length-L block biject with length-L binary strings via maximal runs of 1s — 2^L configs, r runs ↔ r sub-blocks.
tags: [concept, castle, bijection, binary-strings, combinatorics]
sources: [project-euler-502-solution]
created: 2026-09-13
updated: 2026-09-13
---

# Binary-string bijection

## Description

The **binary-string bijection** is the engine of the castle solution. The configurations of a single block of length *L* — the ways to place non-overlapping, non-adjacent, integer-length sub-blocks along it, including the empty configuration — are in bijection with the binary strings of length *L*: map each string to the configuration whose sub-blocks are its **maximal runs of 1s**.[^1]

Two consequences follow immediately:[^1]

1. The number of configurations in a length-*L* block is `2^L`.
2. A binary string with *r* maximal runs of 1s corresponds to a configuration with *r* sub-blocks.

This is the [[castle-representations](pages/castle-representations.md)] binary encoding, now pinned down as an exact bijection with the run/sub-block correspondence made precise. It is the base layer of the induction that proves the [[castle-counting-formula](pages/castle-counting-formula.md)]'s `T(k,L) = (k+1)^L`: a tower of height ≤ *k* above a length-*L* block is a length-*L* binary string (which columns start a sub-block in the row directly above) together with, for each maximal run of length *l*, an independent tower of height ≤ *k*−1 above that sub-block.[^2] Because sibling sub-blocks never interact (the [[generalized-dyck-grammar](pages/generalized-dyck-grammar.md)] crux), the count factors over runs:

```
T(k, L) = ∑_{b ∈ {0,1}^L} ∏_{runs of length l in b} T(k−1, l) = ∑_b k^{ones(b)} = (1 + k)^L
```

The *signed* count uses the same bijection with a `(−1)^{runs(b)}` weight, giving the `P(k,L)` recursion.[^3] The run-count reading is also what makes the *k*=1 case a clean binary-string statistic — `P(1,L) = ∑_b (−1)^{runs(b)} = Re((1+i)^{L+1})` (see [[castle-counting-formula](pages/castle-counting-formula.md)]).[^3]

**A thread to follow.** The `2^L` count and the run structure connect the castle problem to compositions, run statistics of binary strings, and the broader combinatorics of gap-constrained placements — one of the threads that reaches outward from the solution into the general polyomino/combinatorics domain.

## Appearances in Sources

- [[project-euler-502-solution](pages/project-euler-502-solution.md)] — states the bijection precisely and uses it as the base of the `T(k,L)=(k+1)^L` induction and the `P(k,L)` recursion.

## Related Concepts

- [[castle-representations](pages/castle-representations.md)] — the binary-string encoding this bijection formalizes.
- [[castle-counting-formula](pages/castle-counting-formula.md)] — the induction and recursion built on the bijection.
- [[generalized-dyck-grammar](pages/generalized-dyck-grammar.md)] — the sibling-independence that makes the count factor.

## Footnotes

[^1]: [[project-euler-502-solution](pages/project-euler-502-solution.md)] §"The binary-string bijection" L14-19 — "Configurations within a block of length L (non-overlapping, non-adjacent integer-length sub-blocks, including the empty config) biject with binary strings of length L: map each string to the configuration whose sub-blocks are its maximal runs of 1s ... The number of configurations in a length-L block is 2^L ... If a binary string has r maximal runs of 1s, the corresponding configuration has r sub-blocks."
[^2]: [[project-euler-502-solution](pages/project-euler-502-solution.md)] §"T(k, L) = (k+1)^L" L27-34 — "A tower of height ≤ k above a length-L block is a length-L binary string ... plus, for each maximal run of length l, an independent tower of height ≤ k-1 ... T(k, L) = ∑_b ∏_{runs} T(k-1, l) = ∑_b k^{ones(b)} = (1 + k)^L."
[^3]: [[project-euler-502-solution](pages/project-euler-502-solution.md)] §"Recursion for P(k, L)" L76, L102-108 — "P(k, L) = ∑_b (-1)^{runs(b)} ∏_{runs of length l} P(k-1, l)" and, at k=1, "P(1, L) = ∑_b (-1)^{runs(b)} ... = Re((1+i)^{L+1})".
