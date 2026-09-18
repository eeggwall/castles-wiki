---
title: Castle compression
category: Concepts
summary: How cheaply a castle can be written down. The castle rules are themselves a compression scheme — the raster↔skyline gap is worth w(h − log₂ h) bits — and the wiki's run-length encodings are a second layer. The payoff is a compressibility axis whose description tiers (parametric / rule-generated / generic) separate "irregular because a complicated process" from "irregular because no process" — a distinction the shape axes cannot express.
tags: [concept, castle, compression, kolmogorov-complexity, encoding, representations, classification, information-theory]
sources: [project-euler-502-representations, project-euler-502-castle-factoring]
created: 2026-09-18
updated: 2026-09-18
---

# Castle compression

## The castle rules are a compression scheme

A castle is a `w × h` stack of cells, but you never need `w·h` bits to specify one — the rules already told you most of it. A column-convex, bottom-aligned castle is determined by its skyline `(c₁, …, c_w)` of `w` heights ([[castle-representations](pages/castle-representations.md)]), so it needs `w·log₂ h` bits, whereas a raw raster of the `w × h` grid needs `w·h` bits. The rules are worth

```
w·h − w·log₂ h  =  w·(h − log₂ h)   bits
```

of compression, for free — the gap between raster space and skyline space *is* the information the castle constraints give you.[^1] For `h = 5` that is `w·(5 − 2.32) ≈ 2.68w` bits: more than half the raster. Knowing "it is a valid castle" is already a lossless compression of "which cells are filled."

## The encoding ladder

The encodings on [[castle-representations](pages/castle-representations.md)] form a ladder, each rung exploiting more structure:

1. **Raster / binary string** — `w·h` bits, records every cell. The uncompressed baseline; the Solution subpage's verdict "the right encoding, wrong decomposition" is precisely that this encoding throws the structure away.
2. **Skyline / integer tuple** — `w·log₂ h` bits. Exploits column-convexity and bottom-alignment (each column is one number). The workhorse encoding.
3. **Block / run-length descriptions** — the [[monotone-streak-factorization](pages/monotone-streak-factorization.md)] and the excursion/gap word ([[castle-representations](pages/castle-representations.md)]) record a castle as its blocks: each ascent opens a block ([[castle-sign](pages/castle-sign.md)]), so a `b`-block castle is described by `b` (height, width) pairs against `w` column heights. A unimodal castle is "one bump" (`b ≈ 1`) and compresses hard; a jagged castle with `~ w/2` blocks does not.
4. **Parametric** — the highly symmetric types (box, hook, staircase, the periodic/battlement type of [[castle-classification](pages/castle-classification.md)] Axis 7) are pinned by a handful of numbers — an `O(log(w·h))`-bit description even though their count is far larger.

The U/R/D step string ([[urd-step-strings](pages/urd-step-strings.md)]) sits *below* the skyline on this ladder: it is a path of length `~ 2·area`, so it *expands* a tall castle rather than compressing it. Compression is not a property of an encoding alone — it is a property of the encoding *against* the castle's structure.

## The compressibility axis: description tiers

The payoff is a classification the shape axes (1–7 of [[castle-classification](pages/castle-classification.md)]) cannot see. Those axes ask "what does the shape look like." Compressibility asks "what is the cheapest *program* that produces it" — an orthogonal question, stratifying castles by description tier:

- **Tier 0 — parametric.** A short explicit program names a shape: box, hook, staircase, or a periodic/battlement (a period plus a repeat count). Described in `O(log(w·h))` bits.
- **Tier 1 — rule-generated.** The skyline is the column-by-column output of a tiny state machine — a 0/1 transfer matrix with a handful of ones, plus an initial state. These castles look irregular but have a short program: the plastic number's realizer in the [[reachable-field-census](pages/reachable-field-census.md)] is a **4-ones** matrix whose output is not convex, not periodic, not symmetric, yet is specified by four numbers. It is the castle analogue of a PRNG with a short seed — apparent randomness, tiny Kolmogorov complexity.
- **Tier 2 — generic.** No structure; `~ w·log₂ h` bits, sitting at the counting-entropy ceiling of [[castle-entropy](pages/castle-entropy.md)].

The shape axes are blind to Tier 1: a rule-generated castle fails every convex / symmetric / path-like predicate, so Axes 1–7 dump it in the same bucket as a truly random castle. Compressibility is the first axis that separates *irregular-because-complicated-process* from *irregular-because-no-process* — a class no single shape predicate can express. The open thread: is there a predicate that *detects* Tier 1 (low-complexity-but-irregular) without simulating the rule?

## Related Concepts

- [[castle-representations](pages/castle-representations.md)] — the encodings that form the ladder.
- [[monotone-streak-factorization](pages/monotone-streak-factorization.md)] — the run-length encoding of the difference sequence; the first compression layer past the skyline.
- [[castle-classification](pages/castle-classification.md)] — Axes 1–7, the shape axes that compressibility cross-cuts.
- [[castle-entropy](pages/castle-entropy.md)] — the dual measure: the ceiling that compression approaches.
- [[urd-step-strings](pages/urd-step-strings.md)], [[binary-string-bijection](pages/binary-string-bijection.md)] — the path and raster encodings at opposite ends of the ladder.
- [[reachable-field-census](pages/reachable-field-census.md)], [[metallic-strip-realizability](pages/metallic-strip-realizability.md)] — the rule factories that generate Tier-1 castles.
- [[castle-counting-formula](pages/castle-counting-formula.md)] — `F(w,h)`, the count the skyline encodes within.

## Appearances in Sources

- [[project-euler-502-representations](pages/project-euler-502-representations.md)] — the three primary encodings and the "right encoding, wrong decomposition" note; the raster-vs-skyline gap.
- [[project-euler-502-castle-factoring](pages/project-euler-502-castle-factoring.md)] — the run-length (streak, excursion/gap) encodings; the second compression layer.

## Footnotes

[^1]: Exact: the skyline is a bijection with castles on the grid, so `log₂ A(w,h) ≤ w·log₂ h`, against `w·h` bits for the raster. The `w(h − log₂ h)` figure is the log-ratio of the two spaces.
