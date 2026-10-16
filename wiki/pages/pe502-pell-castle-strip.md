---
title: "PE 502: the Pell castle strip"
category: Sources
summary: A note on the Analytic Combinatorics exercise D(x) = 1/(1 − 2x − x²) - coefficient matching gives a_n − 2a_{n−1} − a_{n−2} = [n = 0] with the initial terms, and D(x) counts tilings by a width-1 atom of weight 2 and a width-2 atom of weight 1. The note also reads the two atoms as height-2 towers and Project Euler 502's gap rule, matches D(x) with the signed tower denominators, and calls the coefficients half-companion Pell numbers; none of the three holds: the castles of height at most 2 number 2^w, the signed tower denominator at k = 1 is 1 − 2x + 2x², and the coefficients are the Pell numbers a_n = P⋆_{n+1}.
tags: [note, castle, pell, generating-functions, coefficient-matching, seminar, source]
sources: [pe502-pell-castle-strip]
created: 2026-09-15
updated: 2026-10-16
---

# Project Euler 502 (PE 502): the Pell castle strip

**Source:** `raw/pe502-pell-castle-strip.md` (a note written 2026-09-15 on an Analytic Combinatorics end-of-chapter exercise on `D(x) = 1/(1 − 2x − x²)`)
**Date ingested:** 2026-09-15
**Type:** note (markdown, 58 lines)

## Summary

The note takes the generating function `D(x) = 1/(1 − 2x − x²) = Σ_i a_i x^i` and derives its recurrence and initial terms by coefficient matching. Matching the coefficients of `x^n` in `(1 − 2x − x²)·D(x) = 1`, with `a_{−1} = a_{−2} = 0`, gives the single equation[^1]

```
a_n − 2·a_{n−1} − a_{n−2}  =  [n = 0],
```

whose cases `n = 0` and `n = 1` are the initial terms `a_0 = 1` and `a_1 = 2`.

The note then reads `D(x)` as a sequence of two atoms: a width-1 atom of weight 2, the term `2x`, and a width-2 atom of weight 1, the term `x²`. Then `a_n` is the total weight of the tilings of a strip of length `n`, and removing the last atom gives `a_n = 2·a_{n−1} + a_{n−2}`.[^2] At `n = 2` the tilings are two width-1 atoms, `2·2 = 4` of them by weight, and one width-2 atom, so `a_2 = 5`.

The coefficients are `1, 2, 5, 12, 29, 70, 169, …`, growing like `1 + √2`.[^3]

## What the note says about castles, and the correct facts

The note ties each atom to a castle rule.[^4]

- **The width-1 atom.** The note reads it as the towers of height at most 1 on a base of length `L`, `T(1, L) = 2^L`, one of two states per column.
- **The width-2 atom.** The note reads it as a block followed by the gap that Project Euler's rule 3 requires between neighboring blocks in a row, and concludes that without rule 3 the count would be `2^n`, with rule 3 adding the term `x²`.

The castles of width `w` and height at most 2 stand on the towers of height at most 1 on a base of length `w`, the `2^w` binary strings, and every binary string is the towers of exactly one castle: the blocks of row 2 are its maximal runs of 1s, which satisfy rule 3 automatically ([[binary-string-bijection](pages/binary-string-bijection.md)], [[castle-polyomino](pages/castle-polyomino.md)]). So rule 3 removes no configuration, the castles of height at most 2 number `2^w`, and `D(x)` does not count them. The castle-side objects that `D(x)` counts are the anchored 1-smooth strips on the heights `{1, 2, 3}`, `P⋆_w` of width `w` with `Σ_w P⋆_w x^{w−1} = D(x)`; those that reach height 3 are the Pell castles ([[pell-castle-strip](pages/pell-castle-strip.md)], [[pell-castle](pages/pell-castle.md)]).

The note also sets `D(x)` beside the update `den_k = (1 − 2x)·den_{k−1} + x·num_{k−1}` of the signed tower count and calls it the smallest case of that family.[^5] The smallest case is `den_1 = 1 − 2x + 2x²`, with `P_1(x) = (1 − 2x)/(1 − 2x + 2x²)` ([[castle-counting-formula](pages/castle-counting-formula.md)], Equation (5)), so `1 − 2x − x²` is not one of the `den_k`.

The note calls the coefficients half-companion Pell numbers.[^6] They are the Pell numbers shifted by one, `a_n = P⋆_{n+1}` with `P⋆_0 = 0`, `P⋆_1 = 1` and `P⋆_n = 2P⋆_{n−1} + P⋆_{n−2}` (A000129); the half-companion Pell numbers are the Pell-Lucas numbers A001333, `1, 1, 3, 7, 17, 41, …` ([[pell-numbers](pages/pell-numbers.md)]).[^7]

## Key Takeaways

- **Coefficient matching.** `(1 − 2x − x²)·D(x) = 1` gives `a_n − 2a_{n−1} − a_{n−2} = [n = 0]` with `a_{−1} = a_{−2} = 0`; the initial terms are its cases `n = 0, 1`.[^1]
- **Two atoms.** `1/(1 − 2x − x²)` counts the tilings by a width-1 atom of weight 2 and a width-2 atom of weight 1.[^2]
- **Pell numbers.** `a_n = P⋆_{n+1}`, growing like the silver mean `1 + √2 = [2; 2, 2, …]`, a reduced quadratic surd of norm `−1` ([[eigenvalue-continued-fractions](pages/eigenvalue-continued-fractions.md)]).[^3][^7]
- **The castle strip.** [[pell-castle-strip](pages/pell-castle-strip.md)] develops the exercise into the anchored 1-smooth strips on `{1, 2, 3}`.

## Entities & Concepts

- [[pell-numbers](pages/pell-numbers.md)] - the Pell numbers `P⋆_n` (A000129) and the Pell-Lucas numbers (A001333).
- [[pell-castle-strip](pages/pell-castle-strip.md)] - the Analysis built on this note: the anchored 1-smooth strips on `{1, 2, 3}`, whose generating function in the width is `D(x)`.
- [[pell-castle](pages/pell-castle.md)] - the strips that reach height 3.
- [[generating-functions](pages/generating-functions.md)] - coefficient matching for rational generating functions.
- [[eigenvalue-continued-fractions](pages/eigenvalue-continued-fractions.md)] - the continued fraction `[2; 2, 2, …]` of `1 + √2`.
- [[tower-word-continued-fraction](pages/tower-word-continued-fraction.md)] - the tower words counted by length, also growing like `1 + √2`.
- [[castle-counting-formula](pages/castle-counting-formula.md)] - the update of `num_k`, `den_k`.

## Footnotes

[^1]: raw/pe502-pell-castle-strip.md §"Where the recurrence comes from" L9-L19 - "Matching coefficients on (1 - 2x - x^2) D(x) = 1", "[x^0]: a_0 = 1", "[x^1]: a_1 - 2a_0 = 0, so a_1 = 2", "[x^{n+2}] for n ≥ 0: a_{n+2} - 2a_{n+1} - a_n = 0", "a_n - 2a_{n-1} - a_{n-2} = [n = 0] with a_{-1} = a_{-2} = 0. The base cases a_0 = 1, a_1 = 2 are the same recurrence evaluated at n = 0, 1 with those zeros substituted."
[^2]: raw/pe502-pell-castle-strip.md §"The castle reading" L23-L28 - "D(x) = 1/(1 - 2x - x^2) is a two-atom composition scheme. Read it as counting tilings of a 1 × n strip using: a width-1 atom with weight 2; a width-2 atom with weight 1. Then a_n is the total weight of such tilings, and a_n = 2 a_{n-1} + a_{n-2} is just \"peel off the last atom.\""
[^3]: raw/pe502-pell-castle-strip.md §"The Pell fingerprint" L52-L54 - "a_0, a_1, a_2, … = 1, 2, 5, 12, 29, 70, 169, …", "growth rate 1 + √2".
[^4]: raw/pe502-pell-castle-strip.md §"The castle reading" L30-L40 - "Unsigned tower count. T(k, L) = (k+1)^L. For height-2 towers (k = 1), that's 2^L ... This is the width-1, weight-2 atom.", "Rule 3, mandatory gap. Adjacent blocks on the same row need a gap of width ≥ 1. Bundle \"block-end + start-of-mandatory-gap\" as one atomic unit and its minimum width is 2. This is the width-2, weight-1 atom.", "Without rule 3 you'd only have the 2x atom, denominator 1 - 2x, and a_n = 2^n".
[^5]: raw/pe502-pell-castle-strip.md §"Match with the wiki's rational recurrence" L42-L48 - "den_k = den_{k-1}(1 - 2x) + x · num_{k-1}", "D(x) is the baby case of that family".
[^6]: raw/pe502-pell-castle-strip.md §"The Pell fingerprint" L54 - "Half-companion Pell numbers, growth rate 1 + √2."
[^7]: Verified by execution (Python 3.11 with SymPy, 2026-10-16): the coefficients of `1/(1 − 2x − x²)` equal `P⋆_{n+1}` for `n < 40`; the castles of width `w ≤ 10` and height at most 2 number `2^w`; `den_1 = 1 − 2x + 2x²`; A000129 and A001333 checked on oeis.org.
