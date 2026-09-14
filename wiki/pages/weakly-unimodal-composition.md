---
title: Weakly unimodal composition
category: Concepts
summary: A composition of n that weakly ascends then weakly descends (OEIS A001523, "stacks"); a convex castle of area n is exactly one of these, giving the castle-by-area ↔ A001523 match.
tags: [concept, composition, unimodal, oeis, castle, area]
sources: [oeis-mining-pe502, castle-by-area]
created: 2026-09-13
updated: 2026-09-13
---

# Weakly unimodal composition

## Description

A **weakly unimodal composition** of *n* is an ordered sequence of positive parts summing to *n* that is weakly increasing up to a maximum and then weakly decreasing — a "stack." These are counted by OEIS **A001523** (`1, 1, 2, 4, 8, 15, 27, 47, 79, …` with `A001523(0)=1`), described there as "number of stacks, or planar partitions of *n*; also the number of weakly unimodal compositions of *n*."

## The castle-by-area identity

Reading a [[castle-polyomino](pages/castle-polyomino.md)] by its **area** (total cells `= ∑ c_i`) rather than by (w,h), a [[convex-castle](pages/convex-castle.md)] of area *n* is *literally* a weakly unimodal composition of *n*: convex ⟺ unimodal column-height profile, and the parts are the column heights summing to the area.[^1] Hence — verified for `n = 1..18` — the count of convex castles by area is[^2]

```
conv(n) = A001523(n)      (n ≥ 1;  A001523(0) = 1 is the empty stack)
```

with terms `1, 2, 4, 8, 15, 27, 47, 79, 130, 209, 330, 512, 784, 1183, 1765, 2604, 3804, 5504`. This is a definition-level match, not a coincidence — a real synonym for a dense, well-studied entry (so a low-value but legitimate cross-reference). The more quotable result is the **parity refinement** `cev(n) + cod(n) = A001523(n)` (convex-even + convex-odd castles by area), a parity split of a foundational sequence that is itself new (see [[castle-by-area](pages/castle-by-area.md)]).[^3]

The mirror notion — **valley** compositions (weakly decreasing then increasing, i.e. negation-unimodal) — is OEIS **A332578**, matched by valley-shaped castles by area; and the complement (non-stack compositions) is **A115981 = A011782 − A001523**, matched by non-convex castles. All three sit in the same dense-composition cluster (see [[castle-by-area](pages/castle-by-area.md)]).

## Appearances in Sources

- [[castle-by-area](pages/castle-by-area.md)] — the area re-indexing and the A001523 / A332578 / A115981 matches.
- [[oeis-mining-pe502](pages/oeis-mining-pe502.md)] — vein 9: `conv(n) = A001523(n)` and the parity refinement.

## Related Concepts

- [[castle-by-area](pages/castle-by-area.md)] — castles indexed by area.
- [[convex-castle](pages/convex-castle.md)] — the convex (unimodal) castle whose area-count is A001523.
- [[oeis-cross-referencing](pages/oeis-cross-referencing.md)] — why a match on a dense entry is low-value but real.

## Footnotes

[^1]: [[castle-by-area](pages/castle-by-area.md)] `vein9-area.md` §"The main finding" L21-31 — "A convex castle is exactly a unimodal composition of its area: convex + column-convex <=> unimodal column-height profile. So the identity is a definition-level match, not a coincidence."
[^2]: [[castle-by-area](pages/castle-by-area.md)] `vein9-area.md` §"The main finding" L13-19 — "Convex (unimodal) castles of area n matches A001523 exactly for the 18 terms computed: conv(n) = 1, 2, 4, 8, 15, 27, 47, 79, 130, 209, 330, 512, 784, 1183, 1765, 2604, 3804, 5504 ... with A001523(0) = 1"; conv(n) re-verified during ingest.
[^3]: [[castle-by-area](pages/castle-by-area.md)] `vein9-area.md` §"Parity splits" L44-52 — "cev(n) + cod(n) = A001523(n) (parity split of A001523; potentially interesting) ... a genuine refinement of a foundational sequence."
