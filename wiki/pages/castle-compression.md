---
title: Castle compression
category: Concepts
summary: How cheaply a castle can be written down. The castle rules are themselves a compression scheme — the raster↔skyline gap is worth w(h − log₂ h) bits — and the wiki's run-length encodings are a second layer. The payoff is a compressibility axis whose description tiers (parametric / rule-generated / generic) separate "irregular because a complicated process" from "irregular because no process" — a distinction the shape axes cannot express.
tags: [concept, castle, compression, kolmogorov-complexity, encoding, representations, classification, information-theory]
sources: [project-euler-502-representations, project-euler-502-castle-factoring]
created: 2026-09-18
updated: 2026-09-19
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
4. **Parametric** — the highly symmetric types (box, hook, staircase, the periodic/battlement type of [[castle-classification-shape](pages/castle-classification-shape.md)] Axis 7) are pinned by a handful of numbers — an `O(log(w·h))`-bit description even though their count is far larger.

The U/R/D step string ([[urd-step-strings](pages/urd-step-strings.md)]) sits *below* the skyline on this ladder: it is a path of length `~ 2·area`, so it *expands* a tall castle rather than compressing it. Compression is not a property of an encoding alone — it is a property of the encoding *against* the castle's structure.

## The compressibility axis: description tiers

The payoff is a classification the shape axes (1–7 of [[castle-classification-shape](pages/castle-classification-shape.md)]) cannot see. Those axes ask "what does the shape look like." Compressibility asks "what is the cheapest *program* that produces it" — an orthogonal question, stratifying castles by description tier:

- **Tier 0 — parametric.** A short explicit program names a shape: box, hook, staircase, or a periodic/battlement (a period plus a repeat count). Described in `O(log(w·h))` bits.
- **Tier 1 — rule-generated.** The skyline is the column-by-column output of a tiny state machine — a 0/1 transfer matrix with a handful of ones, plus an initial state. These castles look irregular but have a short program: the plastic number's realizer in the [[reachable-field-census](pages/reachable-field-census.md)] is a **4-ones** matrix whose output is not convex, not periodic, not symmetric, yet is specified by four numbers. It is the castle analogue of a pseudorandom number generator (PRNG) with a short seed — apparent randomness, tiny Kolmogorov complexity.
- **Tier 2 — generic.** No structure; `~ w·log₂ h` bits, sitting at the counting-entropy ceiling of [[castle-entropy](pages/castle-entropy.md)].

The shape axes are blind to Tier 1: a rule-generated castle fails every convex / symmetric / path-like predicate, so Axes 1–7 dump it in the same bucket as a truly random castle. Compressibility is the first axis that separates *irregular-because-complicated-process* from *irregular-because-no-process* — a class no single shape predicate can express. The open thread: is there a predicate that *detects* Tier 1 (low-complexity-but-irregular) without simulating the rule?

## Neighbours of the compressibility axis

- **Tier 1 is a castle strip.** The "tiny state machine" is exactly the object of [[castle-strip](pages/castle-strip.md)]: an `h × h` 0/1 transfer matrix over the heights, read column by column. The strip page is the concept behind the Tier-1 factories ([[reachable-field-census](pages/reachable-field-census.md)], [[metallic-strip-realizability](pages/metallic-strip-realizability.md)]), and its rational width generating function (GF) `1/det(I − xM)` is the algebraic signature of a short program.
- **The language-theoretic face.** A Tier-1 skyline is a word of a *regular* language (finite automaton, rational GF); the tower word of [[tower-word-language](pages/tower-word-language.md)] is context-free in general and collapses to regular once height is bounded - which is why [[tower-word-continued-fraction](pages/tower-word-continued-fraction.md)] finds the bounded-height continued fraction terminating at the rational `1/(1 − (k+1)x)`. Chomsky's hierarchy is the description-tier ladder for languages.
- **A Tier-1 detector already exists for linear rules.** [[berlekamp-massey](pages/berlekamp-massey.md)] returns the shortest linear recurrence generating a sequence - "shortest program" restricted to linear machines - from `2L` terms, without simulating anything; [[castle-cryptography-round-two](pages/castle-cryptography-round-two.md)] measures how a degree-`e` nonlinear filter inflates that description (linear complexity `≤ C(d+e−1, e)`). The open question above is answered for the linear subclass; the 0/1-automaton case is the part still open.
- **Spectra as lossy codes.** The skyline discrete Fourier transform (DFT) on [[spectral-analysis](pages/spectral-analysis.md)] compresses periodic skylines to a sparse frequency support (its compressed-sensing hook), and a graph spectrum is a lossy code for the castle whose collisions are exactly the isospectral pairs of [[isospectral-castles](pages/isospectral-castles.md)] - 10 cells for adjacency, 11 for Laplacian, 16 for both - the smallest castles where spectral compression loses information.
- **Enumeration order as encoding.** Under a Gray-code order ([[aocp-generating-permutations-tuples](pages/aocp-generating-permutations-tuples.md)]) consecutive castles differ in one column, so the whole space `{1..h}^w` is a one-symbol-per-step delta stream.
- **The exact size of the Tier-2 codebook.** `A(w,h) = h^w − (h−1)^w` on [[castle-counting-function](pages/castle-counting-function.md)] - the difference-of-powers rows A000225, A001047, A005061, … - so `log₂ A(w,h)` is the exact generic cost and the `w·log₂ h` above is its leading term.

## Related Concepts

- [[castle-representations](pages/castle-representations.md)] — the encodings that form the ladder.
- [[monotone-streak-factorization](pages/monotone-streak-factorization.md)] — the run-length encoding of the difference sequence; the first compression layer past the skyline.
- [[castle-classification-shape](pages/castle-classification-shape.md)] — Axes 1–7, the shape axes that compressibility cross-cuts.
- [[castle-entropy](pages/castle-entropy.md)] — the dual measure: the ceiling that compression approaches.
- [[urd-step-strings](pages/urd-step-strings.md)], [[binary-string-bijection](pages/binary-string-bijection.md)] — the path and raster encodings at opposite ends of the ladder.
- [[reachable-field-census](pages/reachable-field-census.md)], [[metallic-strip-realizability](pages/metallic-strip-realizability.md)] — the rule factories that generate Tier-1 castles.
- [[castle-counting-formula](pages/castle-counting-formula.md)] — `F(w,h)`, the count the skyline encodes within.
- [[castle-strip](pages/castle-strip.md)] — the Tier-1 machine as a concept.
- [[tower-word-language](pages/tower-word-language.md)] / [[tower-word-continued-fraction](pages/tower-word-continued-fraction.md)] — regular vs. context-free, the language-theoretic tier ladder.
- [[berlekamp-massey](pages/berlekamp-massey.md)] / [[castle-cryptography-round-two](pages/castle-cryptography-round-two.md)] — linear complexity as a Tier-1 detector for linear rules.
- [[spectral-analysis](pages/spectral-analysis.md)] / [[isospectral-castles](pages/isospectral-castles.md)] — spectra as lossy codes and their collisions.
- [[aocp-generating-permutations-tuples](pages/aocp-generating-permutations-tuples.md)] — Gray order as a delta encoding.
- [[castle-counting-function](pages/castle-counting-function.md)] — the exact size of the generic codebook.
- [[song-as-castle](pages/song-as-castle.md)] - the ladder run on a real waveform: a peak-normalized 16-bit signal is an `h = 65536` castle, FLAC's LPC + Rice is Tier 1, AAC is the lossy spectral tier, and Berlekamp-Massey over `F_65537` is the exact Tier-1 detector (linear complexity `N/2` on audio, `5` on a 5-tap LFSR skyline).
- [[image-as-castle](pages/image-as-castle.md)] - the ladder on an image: PNG's Sub/Up/Average/Paeth filters are the Tier-1 predictors, JPEG's DCT the spectral tier, and the 2D height field is 32x smaller than its voxel raster.
- [[castle-steganography](pages/castle-steganography.md)] - the "skip rule" reading of compression: one bit per castle of hidden capacity is exactly the parity clause priced on this page.
- [[castle-conditional-entropy](pages/castle-conditional-entropy.md)] - the dual view: conditioning is an oracle-side compression; H(B) vs H(N) makes the one-bit gap this page prices explicit.

## Appearances in Sources

- [[project-euler-502-representations](pages/project-euler-502-representations.md)] — the three primary encodings and the "right encoding, wrong decomposition" note; the raster-vs-skyline gap.
- [[project-euler-502-castle-factoring](pages/project-euler-502-castle-factoring.md)] — the run-length (streak, excursion/gap) encodings; the second compression layer.

## Footnotes

[^1]: Exact: the skyline is a bijection with castles on the grid, so `log₂ A(w,h) ≤ w·log₂ h`, against `w·h` bits for the raster. The `w(h − log₂ h)` figure is the log-ratio of the two spaces.
