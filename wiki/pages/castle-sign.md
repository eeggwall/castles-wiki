---
title: Castle sign
category: Concepts
summary: s(C) = (−1)^blocks, the castle analogue of the permutation sign; (T±P)/2 splits towers into even/odd-block classes, making P(k,L) a sign homomorphism.
tags: [concept, castle, sign, permutations, parity, generating-functions]
sources: [project-euler-502-castle-factoring]
created: 2026-09-13
updated: 2026-09-13
---

# Castle sign

## Description

The **castle sign** is the castle analogue of the permutation sign, and it is what makes the even-block constraint tractable. A permutation sign is `sgn(σ) = (−1)^{n−c} = ∏_cycles (−1)^{|γ|−1}`, with *c* cycles.[^1] For a castle, each block is an excursion atom (a `U…D` pair) and each `D` completes one block, so weighting every block by −1 defines:[^1]

```
s(C) = (−1)^{blocks(C)}
```

In the column-height ([[castle-representations](pages/castle-representations.md)] integer-tuple) form, the block count is the total descent, so the sign is a function of the column heights directly:[^2]

```
blocks = ∑_{i=0}^{L} max(0, c_i − c_{i+1}),   c_0 = c_{L+1} = 0
s(C) = (−1)^{∑ max(0, c_i − c_{i+1})}
```

## The even/odd projector

Let `T` be the unsigned tower count and `P = ∑_C s(C)` the signed count. Then the sign separates towers into parity classes exactly as `(1 ± sgn)/2` separates permutations into even and odd:[^3]

```
(T + P)/2 = even-block towers
(T − P)/2 = odd-block towers
```

This is the meaning of the signed tower recursion `P(k,L)`: it is the castle analogue of the **sign homomorphism**.[^3] A full castle is `U (tower) D`, so its block count is the tower's plus one for the bottom block — "castle has even total blocks" means "tower has an odd number of blocks," which is the `(T−P)/2` term in the [[castle-counting-formula](pages/castle-counting-formula.md)]:[^4]

```
F(w,h) = [ h^w − (h−1)^w − P(h−1,w) + P(h−2,w) ] / 2
```

So the [[castle-counting-formula](pages/castle-counting-formula.md)] and this sign reading are two views of the same object `P`: the formula uses `(T−P)/2` for the tower's odd-block count; this page explains *why* `P` is the correct signed count — it is the sign homomorphism whose parity projector isolates the even-castle class.

## Appearances in Sources

- [[project-euler-502-castle-factoring](pages/project-euler-502-castle-factoring.md)] — defines `s(C) = (−1)^blocks`, gives the descent formula for the block count, and shows the `(T±P)/2` even/odd split.

## Related Concepts

- [[permutation-cycle-castle-analogy](pages/permutation-cycle-castle-analogy.md)] — the analogy in which the sign is the "sign atom."
- [[castle-counting-formula](pages/castle-counting-formula.md)] — where `P(k,L)` and the `(T−P)/2` term appear.
- [[monotone-streak-factorization](pages/monotone-streak-factorization.md)] — the block count as the sum of down-streak magnitudes.
- [[castle-counting-function](pages/castle-counting-function.md)] — the even-block count the sign isolates.

## Footnotes

[^1]: [[project-euler-502-castle-factoring](pages/project-euler-502-castle-factoring.md)] §"The sign of a castle" L92-101 — "sgn(σ) = (-1)^{n - c} = ∏ (-1)^{|γ|-1} ... Each block is an excursion atom (a U ... D pair), and each D move completes one block. Weight each block by -1 and define s(C) = (-1)^{blocks(C)}."
[^2]: [[project-euler-502-castle-factoring](pages/project-euler-502-castle-factoring.md)] §"The sign of a castle" L105-113 — "blocks = ∑_{i=0}^{L} max(0, c_i - c_{i+1}), c_0 = c_{L+1} = 0 ... s(C) = (-1)^{∑_i max(0, c_i - c_{i+1})}."
[^3]: [[project-euler-502-castle-factoring](pages/project-euler-502-castle-factoring.md)] §"The sign of a castle" L116-123 — "(T + P)/2 = even-block castles, (T - P)/2 = odd-block castles ... exactly the (1 ± sgn)/2 trick ... P(k,L) ... is the castle analogue of the sign homomorphism."
[^4]: [[project-euler-502-castle-factoring](pages/project-euler-502-castle-factoring.md)] §"The sign of a castle" L123-127 — "'castle has even total blocks' is therefore 'tower has an odd number of blocks', which is the (T-P)/2 term in F(w,h) = (h^w - (h-1)^w - P(h-1,w) + P(h-2,w))/2."
