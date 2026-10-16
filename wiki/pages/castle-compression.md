---
title: Castle compression
category: Concepts
summary: How many bits a castle takes to write down. The castles of width w and height h number A(w, h) = h^w − (h−1)^w, so a fixed-length code needs log₂ A(w, h) ≤ w·log₂ h bits against w·h for the raster, a saving of at least w(h − log₂ h) bits. The encodings form a ladder (raster, skyline, run-length descriptions, parametric), and castles fall into three description tiers - parametric, rule-generated (a strip rule plus an index, about w·log₂ ρ(M) bits) and generic (at least log₂ A(w, h) − c bits for all but a fraction 2^{−c}).
tags: [concept, castle, compression, kolmogorov-complexity, encoding, representations, classification, information-theory]
sources: [project-euler-502-representations, project-euler-502-castle-factoring]
created: 2026-09-18
updated: 2026-10-16
---

# Castle compression

## The castle rules as a code

A castle of width `w` and height `h` is determined by its skyline `(c_1, …, c_w)` ([[castle-representations](pages/castle-representations.md)]), and the castles of width `w` and height `h` number `A(w, h) = h^w − (h−1)^w` ([[castle-counting-function](pages/castle-counting-function.md)]). A fixed-length code for them needs `⌈log₂ A(w, h)⌉` bits, and

```
log₂ A(w, h)  =  w·log₂ h + log₂(1 − ((h−1)/h)^w)  ≤  w·log₂ h
```

([[castle-entropy](pages/castle-entropy.md)], Equation (2)). The raster of the `w × h` grid takes `w·h` bits, one per cell, so the castle rules save at least[^1]

```
w·h − w·log₂ h  =  w·(h − log₂ h)   bits.
```

At `h = 5` that is `w·(5 − 2.32) ≈ 2.68w` bits, more than half of the `5w`-bit raster.

## The encoding ladder

The encodings of [[castle-representations](pages/castle-representations.md)] form a ladder, each rung using more of the structure of a castle:

1. **Raster.** The column-wise binary encoding, `1^{c_i} 0^{h−c_i}` for each column, takes `w·h` bits.
2. **Skyline.** The `w` heights take `w·⌈log₂ h⌉` bits, or `⌈log₂ A(w, h)⌉` bits for the rank of the castle in a fixed order.
3. **Run-length descriptions.** The [[monotone-streak-factorization](pages/monotone-streak-factorization.md)] and the excursion/gap word of [[castle-representations](pages/castle-representations.md)] record where the height changes. A skyline that changes height at `m` of its `w − 1` column boundaries is determined by `c_1`, the `m` boundaries and the `m` changes, each a nonzero integer between `−(h − 1)` and `h − 1`. A convex castle of height `h` changes height at most `2(h − 1)` times, at most `h − 1` times on its rising side and on its falling side, so it is described by `O(h·log₂(wh))` bits. A castle that changes height at every boundary gains nothing.
4. **Parametric.** The rectangle `(h, …, h)`, the hooks, the staircases and the other shape types fixed by a few integers ([[castle-classification-shape](pages/castle-classification-shape.md)]) are described by `O(log₂(wh))` bits.

The step string `U`, `R`, `D` ([[urd-step-strings](pages/urd-step-strings.md)]) has `w` letters `R` and as many `U` and as many `D` as the castle has blocks, `w + 2·blocks` letters in all. The single column `(h)` is `U^h R D^h`, `2h + 1` letters against the `⌈log₂ h⌉` bits of its skyline, so the step string is longer than the skyline for a castle with many blocks.

## Description tiers

The tiers sort castles by the length of their shortest description.

- **Tier 0, parametric.** The skyline is fixed by a constant number of integers up to `max(w, h)`, so by `O(log₂(wh))` bits: the rectangle, the hooks, the staircases. A periodic castle is fixed by its period of length `p` and a repeat count, `p·log₂ h + O(log₂ w)` bits.
- **Tier 1, rule-generated.** The skyline is fixed by a rule from a small family together with data much shorter than `w·log₂ h` bits. A strip rule gives one such description ([[castle-strip](pages/castle-strip.md)]). A 0/1 transfer matrix `M` on the heights `1, …, h` allows `N(w)` strips of width `w`, with `N(w)^{1/w} → ρ(M)`, the largest eigenvalue of `M`, so a strip of the rule is fixed by `M`, `h²` bits, and its index among the `N(w)` strips, `⌈log₂ N(w)⌉ = w·log₂ ρ(M) + o(w)` bits. The rule `[[0, 0, 1], [1, 0, 0], [1, 1, 0]]` on three heights has characteristic polynomial `λ³ − λ − 1` and `ρ(M) = ψ`, the plastic number ([[reachable-field-census](pages/reachable-field-census.md)], [[plastic-number](pages/plastic-number.md)]), so its strips take `log₂ ψ = 0.406` bits per column, against `log₂ 3 = 1.585` for a skyline on three heights.[^2] Linear prediction with a coded residual, as in FLAC, is another rule-generated description ([[song-as-castle](pages/song-as-castle.md)]).
- **Tier 2, generic.** There are fewer than `2^{n−c}` binary descriptions shorter than `n − c` bits, so for every `c ≥ 0` all but a fraction `2^{−c}` of the castles of width `w` and height `h` have no description shorter than `log₂ A(w, h) − c` bits, the counting ceiling of [[castle-entropy](pages/castle-entropy.md)].

The shape types of [[castle-classification-shape](pages/castle-classification-shape.md)] are predicates on single skylines; the tiers depend on the shortest description of the skyline, which no single shape predicate decides.

## Related constructions

- **Strip rules.** [[castle-strip](pages/castle-strip.md)] defines the strips of a rule and shows that their width generating function is rational, with a denominator dividing `det(I − xM)`; [[reachable-field-census](pages/reachable-field-census.md)] and [[metallic-strip-realizability](pages/metallic-strip-realizability.md)] list the rules by their Perron root.
- **Bounded height.** The tower words of height at most `k` form a regular language, with generating function `E_k(x) = 1/(1 − (k+1)x)`; without a height bound they form an unambiguous context-free language, and the generating function of the tower words by length is algebraic and not rational ([[tower-word-language](pages/tower-word-language.md)], [[tower-word-continued-fraction](pages/tower-word-continued-fraction.md)]).
- **Linear complexity.** [[berlekamp-massey](pages/berlekamp-massey.md)] returns the shortest linear recurrence of `N` terms when its order is at most `N/2`. On [[castle-cryptography-round-two](pages/castle-cryptography-round-two.md)], a product of `e` terms of a `d`-stage linear recurrence has linear complexity at most `C(d + e − 1, e)`, `10 = C(5, 2)` for `d = 4`, `e = 2`.
- **Spectra.** The DFT of a skyline that repeats with period `p` dividing `w` is zero outside the bins that are multiples of `w/p` ([[spectral-analysis](pages/spectral-analysis.md)]). The spectrum of the castle graph does not determine the castle: the smallest non-isomorphic castles with equal spectra have 10 cells for the adjacency matrix, 11 for the Laplacian and 16 for both ([[isospectral-castles](pages/isospectral-castles.md)]).
- **Gray order.** In the reflected Gray order on `{1, …, h}^w`, consecutive skylines differ in one column by one ([[castle-gray-code](pages/castle-gray-code.md)]).

## Related Concepts

- [[castle-representations](pages/castle-representations.md)] - the encodings that form the ladder.
- [[monotone-streak-factorization](pages/monotone-streak-factorization.md)] - the run-length description of the first differences, rung 3 of the ladder.
- [[castle-classification-shape](pages/castle-classification-shape.md)] - the shape types, predicates on single skylines.
- [[castle-entropy](pages/castle-entropy.md)] - the counting entropy `log₂ A(w, h)`, the ceiling of tier 2.
- [[urd-step-strings](pages/urd-step-strings.md)], [[binary-string-bijection](pages/binary-string-bijection.md)] - the step string and the binary strings of a block's first row.
- [[castle-strip](pages/castle-strip.md)] - the strip rules of tier 1.
- [[castle-counting-function](pages/castle-counting-function.md)] - the count `A(w, h)`, the size of the generic codebook.
- [[song-as-castle](pages/song-as-castle.md)] - a waveform read as a castle: 16-bit samples as a castle of height 65536, FLAC's linear prediction with a residual, transform codes, and linear complexity over `F_65537` by Berlekamp-Massey.
- [[image-as-castle](pages/image-as-castle.md)] - an image read as castles: PNG's row filters as predictors, JPEG as a transform code, and a height field `256/log₂ 256 = 32` times smaller than its voxel raster.
- [[castle-steganography](pages/castle-steganography.md)] - hiding a message in castles, with one channel that carries one bit per castle in its block parity.
- [[castle-conditional-entropy](pages/castle-conditional-entropy.md)] - the entropy of castles conditioned on their block count and area.
- [[one-bit-seminar](pages/one-bit-seminar.md)] - a seminar on the even-block condition as information.

## Appearances in Sources

- [[project-euler-502-representations](pages/project-euler-502-representations.md)] - the binary-string, skyline and step-string encodings.
- [[project-euler-502-castle-factoring](pages/project-euler-502-castle-factoring.md)] - the streak and excursion/gap encodings, rung 3 of the ladder.

## Footnotes

[^1]: The skyline is a bijection from the castles of width `w` and height `h` onto the skylines in `{1, …, h}^w` that reach `h`, so `log₂ A(w, h) ≤ w·log₂ h` bits suffice against `w·h` for the raster, and the difference is at least `w(h − log₂ h)`.
[^2]: Verified by execution (Python 3.11 with NumPy, 2026-10-16): the characteristic polynomial `λ³ − λ − 1` and Perron root `1.3247` of the rule; its strips with free ends number `3, 4, 5, 7, 9, 12, 16, 21, 28, …` for `w = 1, 2, …`, `A000931(w + 9)`; `log₂ ψ = 0.4057`.
