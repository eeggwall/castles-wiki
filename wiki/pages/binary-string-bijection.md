---
title: Binary-string bijection
category: Concepts
summary: Configurations of non-overlapping, non-adjacent sub-blocks in a length-L block biject with length-L binary strings via maximal runs of 1s — 2^L configs, r runs ↔ r sub-blocks.
tags: [concept, castle, bijection, binary-strings, combinatorics]
sources: [project-euler-502-solution]
created: 2026-09-13
updated: 2026-10-01
---

# Binary-string bijection

## Description

The **binary-string bijection** underlies the castle solution's induction. The configurations of a single block of length *L* — the ways to place non-overlapping, non-adjacent, integer-length sub-blocks along it, including the empty configuration — are in bijection with the binary strings of length *L*: map each string to the configuration whose sub-blocks are its **maximal runs of 1s**.[^1]

Two consequences follow immediately:[^1]

1. The number of configurations in a length-*L* block is `2^L`.
2. A binary string with *r* maximal runs of 1s corresponds to a configuration with *r* sub-blocks.

## Worked example: the 1729 castle (4 × 9)

Read the decimal digits of 1729 as column heights: `(1, 7, 2, 9)` gives a castle of width 4 and height 9 ([[hardy-ramanujan-castle](pages/hardy-ramanujan-castle.md)]). Write `1` for a filled cell and `0` for an empty cell, with columns read left to right and rows numbered from the bottom:

| Row(s) | Four columns | New blocks |
|---|---|---|
| 1 (base) | `1111` | one, spanning all four columns |
| 2 | `0111` | one, spanning columns 2–4 |
| 3–7 | `0101` | two per row, in columns 2 and 4 |
| 8–9 | `0001` | one per row, in column 4 |

Start with the mandatory length-4 base. The row immediately above it is `0111`: its single maximal run, `111`, makes **one** length-3 sub-block, not three separate blocks. There are `2^4 = 16` possible strings for this row, hence 16 possible configurations above a length-4 base (including `0000`, which adds no blocks). Above the length-3 block in row 2, consider only its columns 2–4: row 3 reads `101`. Its two runs of `1` make **two** separate length-1 sub-blocks, with the `0` between them supplying the required gap. Conversely, marking those two sub-blocks with 1s and the gap with 0 recovers `101` uniquely. Each later row is encoded relative to the block directly below it in the same way; `0101` in the full-width view shows the two continuing columns.

Counting the runs row by row gives `1` base block + `1` in row 2 + `5 × 2` in rows 3–7 + `2 × 1` in rows 8–9 = **14 blocks**. This is why the digit castle for 1729 is an even-block castle; 1729 here labels its column heights, rather than the number of configurations of the base.

This is the binary encoding of [[castle-representations](pages/castle-representations.md)], stated as an exact bijection with the run/sub-block correspondence. It is the base layer of the induction that proves the [[castle-counting-formula](pages/castle-counting-formula.md)]'s `T(k,L) = (k+1)^L`: a tower of height ≤ *k* above a length-*L* block is a length-*L* binary string (which columns are covered by a sub-block in the row directly above) together with, for each maximal run of length *l*, an independent tower of height ≤ *k*−1 above that sub-block.[^2] Because sibling sub-blocks never interact (the [[generalized-dyck-grammar](pages/generalized-dyck-grammar.md)] crux), the count factors over runs:

```
T(k, L) = ∑_{b ∈ {0,1}^L} ∏_{runs of length l in b} T(k−1, l) = ∑_b k^{ones(b)} = (1 + k)^L
```

The *signed* count uses the same bijection with a `(−1)^{runs(b)}` weight, giving the `P(k,L)` recursion.[^3] At *k*=1 the run count gives a binary-string statistic — `P(1,L) = ∑_b (−1)^{runs(b)} = Re((1+i)^{L+1})` (see [[castle-counting-formula](pages/castle-counting-formula.md)]).[^3]

**Related structure.** The `2^L` count and the run structure connect the castle problem to compositions, run statistics of binary strings, and gap-constrained placements; [[block-count-constraints](pages/block-count-constraints.md)] treats gap-constrained placements through the semigroup and lacunary branches of its trichotomy.

## Appearances in Sources

- [[project-euler-502-solution](pages/project-euler-502-solution.md)] — states the bijection precisely and uses it as the base of the `T(k,L)=(k+1)^L` induction and the `P(k,L)` recursion.

## Related Concepts

- [[castle-representations](pages/castle-representations.md)] — the binary-string encoding this bijection formalizes.
- [[castle-counting-formula](pages/castle-counting-formula.md)] — the induction and recursion built on the bijection.
- [[generalized-dyck-grammar](pages/generalized-dyck-grammar.md)] — the sibling-independence that makes the count factor.
- [[block-count-constraints](pages/block-count-constraints.md)] — gap-constrained placements, through the semigroup / lacunary branches of the trichotomy.

## Footnotes

[^1]: [[project-euler-502-solution](pages/project-euler-502-solution.md)] §"The binary-string bijection" L14-19 — "Configurations within a block of length L (non-overlapping, non-adjacent integer-length sub-blocks, including the empty config) biject with binary strings of length L: map each string to the configuration whose sub-blocks are its maximal runs of 1s ... The number of configurations in a length-L block is 2^L ... If a binary string has r maximal runs of 1s, the corresponding configuration has r sub-blocks."
[^2]: [[project-euler-502-solution](pages/project-euler-502-solution.md)] §"T(k, L) = (k+1)^L" L27-34 — "A tower of height ≤ k above a length-L block is a length-L binary string ... plus, for each maximal run of length l, an independent tower of height ≤ k-1 ... T(k, L) = ∑_b ∏_{runs} T(k-1, l) = ∑_b k^{ones(b)} = (1 + k)^L."
[^3]: [[project-euler-502-solution](pages/project-euler-502-solution.md)] §"Recursion for P(k, L)" L76, L102-108 — "P(k, L) = ∑_b (-1)^{runs(b)} ∏_{runs of length l} P(k-1, l)" and, at k=1, "P(1, L) = ∑_b (-1)^{runs(b)} ... = Re((1+i)^{L+1})".
