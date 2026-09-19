---
title: "PE 502: the Pell castle strip"
category: Sources
summary: A marginalia note from an Analytic Combinatorics chapter — coefficient-matching to solve `(1−2x−x²)D(x) = 1` for the base cases and recurrence, the two-atom tiling reading of the rational function, and its Pell-number coefficients.
tags: [note, castle, pell, generating-functions, coefficient-matching, seminar, source]
sources: [pe502-pell-castle-strip]
created: 2026-09-15
updated: 2026-09-19
---

# Project Euler 502 (PE 502): the Pell castle strip

**Source:** `raw/pe502-pell-castle-strip.md` (marginalia note authored 2026-09-15 while working through an Analytic Combinatorics end-of-chapter exercise on `D(x) = 1/(1−2x−x²)`)
**Date ingested:** 2026-09-15
**Type:** note (markdown, line-numbered; ~58 lines)

## Summary

The note starts with a textbook-shaped question: given the generating function `D(x) = 1/(1 − 2x − x²) = ∑ a_i x^i`, where does the recurrence come from, and why don't we need a special "base case" argument? By coefficient-matching `(1 − 2x − x²)·D(x) = 1` term-by-term, the recurrence emerges uniformly as[^1]

```
a_n − 2·a_{n−1} − a_{n−2}  =  [n = 0]
```

with the "negative index equals zero" convention (`a_{−1} = a_{−2} = 0`). The base cases `a_0 = 1, a_1 = 2` are simply this recurrence evaluated at the boundary — the `a_n` term at `n = 1` multiplies `a_{−1} = 0`, and so on. Nothing special is happening at the boundary; the appearance of a special base-case argument is what the coefficient-matching mechanic dissolves.[^1]

The note then reads `D(x)` as a two-atom composition scheme:[^2]

- **width-1 atom, weight 2** — the `2x` term
- **width-2 atom, weight 1** — the `x²` term

Then `a_n` is the total weight of strip tilings of length `n`, and the recurrence `a_n = 2·a_{n−1} + a_{n−2}` is just "peel off the last atom." The castle strip that realizes this scheme — 1-smooth skylines of height at most 3 anchored at the base, whose width generating function is exactly `D(x)` — is on [[pell-castle-strip](pages/pell-castle-strip.md)].

## The Pell fingerprint

The counts `a_0, a_1, a_2, … = 1, 2, 5, 12, 29, 70, 169, 408, 985, 2378, …` are **Pell numbers, Online Encyclopedia of Integer Sequences (OEIS) [A000129](https://oeis.org/A000129) shifted** (`a_n = P_{n+1}` where `P_0 = 0, P_1 = 1, P_n = 2P_{n−1} + P_{n−2}`).[^3] The growth rate is the **silver ratio** `1 + √2 ≈ 2.4142`, which the [[eigenvalue-continued-fractions](pages/eigenvalue-continued-fractions.md)] page treats as one of the castle's two purely-periodic norm-`−1` quadratics (root of `x² − 2x − 1`, continued fraction `[2; 2, 2, …]`). The same constant appears as the growth rate of the tower word ([[tower-word-continued-fraction](pages/tower-word-continued-fraction.md)]).

## Key Takeaways

- **Coefficient-matching as a mechanical method.** `(1 − 2x − x²)·D(x) = 1` → uniform recurrence `a_n − 2a_{n−1} − a_{n−2} = [n=0]` with `a_{negative} = 0`. Base cases are the same recurrence, not a special argument.[^1]
- **Two-atom composition reading.** `1/(1 − 2x − x²)` counts strip tilings with a width-1 weight-2 atom and a width-2 weight-1 atom.[^2]
- **Pell fingerprint.** Sequence `1, 2, 5, 12, 29, …` = OEIS A000129 shifted (Pell); growth constant `1 + √2 = [2;2,2,…]` — the silver ratio tracked as one of the wiki's two norm-`−1` reduced quadratics.[^3]
- **Pedagogy shape.** A textbook end-of-chapter question about extracting a recurrence from a generating function *spirals into* a seminar on castles and polyomino theory. The Analysis page [[pell-castle-strip](pages/pell-castle-strip.md)] captures that arc.

## Entities & Concepts

- [[pell-numbers](pages/pell-numbers.md)] — the underlying integer sequence and its silver-ratio growth.
- [[pell-castle-strip](pages/pell-castle-strip.md)] — the seminar-shaped Analysis this note is the source for, including the transfer matrix that realizes `D(x)`.
- [[generating-functions](pages/generating-functions.md)] — the concept page, whose "coefficient matching for GF → recurrence" section this note supplies.
- [[eigenvalue-continued-fractions](pages/eigenvalue-continued-fractions.md)] — where `1+√2 = [2;2,2,…]` lives.
- [[tower-word-continued-fraction](pages/tower-word-continued-fraction.md)] — where `1+√2` also appears, as the tower-word growth constant.

## Relation to Other Wiki Pages

The note is the seed of a small but coherent thread: (i) a general method (coefficient matching, on [[generating-functions](pages/generating-functions.md)]), (ii) a sequence page ([[pell-numbers](pages/pell-numbers.md)]) that connects existing continued-fraction and eigenvalue material to a castle strip, (iii) an Analysis page ([[pell-castle-strip](pages/pell-castle-strip.md)]) that captures the pedagogy — how a small AC exercise opens onto castle strips and the silver ratio.

## Footnotes

[^1]: [[pe502-pell-castle-strip](pages/pe502-pell-castle-strip.md)] §"Where the recurrence comes from" L9-L19 — "Matching coefficients on (1 − 2x − x²) D(x) = 1: [x^0]: a_0 = 1; [x^1]: a_1 − 2a_0 = 0, so a_1 = 2; [x^{n+2}] for n ≥ 0: a_{n+2} − 2a_{n+1} − a_n = 0 ... The a_n term doesn't 'disappear' at the boundary - it multiplies a_{−1}, which is 0 by convention (a power series has no negative powers). Uniformly: a_n − 2a_{n−1} − a_{n−2} = [n = 0] with a_{−1} = a_{−2} = 0. The base cases a_0 = 1, a_1 = 2 are the same recurrence evaluated at n = 0, 1 with those zeros substituted. Nothing special about them."
[^2]: [[pe502-pell-castle-strip](pages/pe502-pell-castle-strip.md)] §"The castle reading" L23-L28 — "D(x) = 1/(1 − 2x − x²) is a two-atom composition scheme. Read it as counting tilings of a 1 × n strip using: a width-1 atom with weight 2; a width-2 atom with weight 1. Then a_n is the total weight of such tilings, and a_n = 2 a_{n−1} + a_{n−2} is just 'peel off the last atom.'"
[^3]: [[pe502-pell-castle-strip](pages/pe502-pell-castle-strip.md)] §"The Pell fingerprint" L52-L54 — "a_0, a_1, a_2, … = 1, 2, 5, 12, 29, 70, 169, … growth rate 1 + √2." The sequence `1, 2, 5, 12, 29, 70, 169, 408, 985, 2378` verified during ingest as OEIS A000129 shifted (`a_n = P_{n+1}`).
