---
title: "PE 502: the Pell castle strip"
category: Sources
summary: A marginalia note from an Analytic Combinatorics chapter — coefficient-matching to solve `(1−2x−x²)D(x) = 1` for the base cases and recurrence — and a proposed reading of the denominator's two atoms as PE 502 structural rules (per-column binary state + a rule-3 gap tax), which later computation withdrew; the castle home of Pell is the anchored 1-smooth height-3 strip.
tags: [note, castle, pell, generating-functions, coefficient-matching, seminar, source]
sources: [pe502-pell-castle-strip]
created: 2026-09-15
updated: 2026-09-19
---

# PE 502: the Pell castle strip

**Source:** `raw/pe502-pell-castle-strip.md` (marginalia note authored 2026-09-15 while working through an Analytic Combinatorics end-of-chapter exercise on `D(x) = 1/(1−2x−x²)`)
**Date ingested:** 2026-09-15
**Type:** note (markdown, line-numbered; ~58 lines)

## Summary

The note starts with a textbook-shaped question: given the generating function `D(x) = 1/(1 − 2x − x²) = ∑ a_i x^i`, where does the recurrence come from, and why don't we need a special "base case" argument? By coefficient-matching `(1 − 2x − x²)·D(x) = 1` term-by-term, the recurrence emerges uniformly as[^1]

```
a_n − 2·a_{n−1} − a_{n−2}  =  [n = 0]
```

with the "negative index equals zero" convention (`a_{−1} = a_{−2} = 0`). The base cases `a_0 = 1, a_1 = 2` are simply this recurrence evaluated at the boundary — the `a_n` term at `n = 1` multiplies `a_{−1} = 0`, and so on. Nothing special is happening at the boundary; the appearance of a special base-case argument is what the coefficient-matching mechanic dissolves.[^1]

The note then turns to the **castle reading** of the same rational function. Read `D(x)` as a two-atom composition scheme:[^2]

- **width-1 atom, weight 2** — the `2x` term
- **width-2 atom, weight 1** — the `x²` term

Then `a_n` is the total weight of strip tilings of length `n`, and the recurrence `a_n = 2·a_{n−1} + a_{n−2}` is just "peel off the last atom." The note then identifies these atoms with castle structure (a reading withdrawn in the Correction below):[^3]

1. **Unsigned tower count.** `T(k,L) = (k+1)^L`; for height-2 towers (`k = 1`), that is `2^L` — each column independently picks one of two states. This is the width-1 weight-2 atom.
2. **Mandatory-gap rule 3.** Adjacent blocks on the same row need a gap of width `≥ 1`. Bundle "block-end + start-of-mandatory-gap" as one atomic unit — its minimum width is 2. This is the width-2 weight-1 atom.

In the note's reading, the denominator splits along PE 502's rules:

```
1  −  2x                              −  x²
      ↑                                  ↑
      per-column binary state (T(1,L))   rule-3 mandatory-gap tax
```

Without rule 3, the note argues, the denominator would be `1 − 2x`, giving `a_n = 2^n` — the naive per-column count; in its words, "the `x²` term is what rule 3 costs."[^4]

The note then matches this to the wiki's rational recurrence for the signed castle count, `den_k = den_{k−1}(1 − 2x) + x·num_{k−1}` (see [[castle-counting-formula](pages/castle-counting-formula.md)]), reading the `(1 − 2x)` factor as the per-column binary atom and the trailing `x·num_{k−1}` as a correction of the same shape as the `x²` tax, and calls `D(x)` the baby case of the family.[^5]

## The Pell fingerprint

The counts `a_0, a_1, a_2, … = 1, 2, 5, 12, 29, 70, 169, 408, 985, 2378, …` are **Pell numbers, OEIS [A000129](https://oeis.org/A000129) shifted** (`a_n = P_{n+1}` where `P_0 = 0, P_1 = 1, P_n = 2P_{n−1} + P_{n−2}`).[^6] The growth rate is the **silver ratio** `1 + √2 ≈ 2.4142`, which the [[eigenvalue-continued-fractions](pages/eigenvalue-continued-fractions.md)] page already treats as one of the castle's two purely-periodic norm-`−1` quadratics (root of `x² − 2x − 1`, continued fraction `[2; 2, 2, …]`). The same constant appears as the growth rate of the tower word ([[tower-word-continued-fraction](pages/tower-word-continued-fraction.md)]).

The note calls these "half-companion Pell numbers"; the sequence is in fact the Pell numbers proper (A000129). Half-companion / Pell-Lucas is A001333 = `1, 1, 3, 7, 17, 41, …`, which does not match here. Corrected during ingest.

## Correction (2026-09-19)

The note's identification of the two atoms with PE 502's rules, and its "baby case" claim, do not hold; both are recorded here as what the source says and corrected on [[pell-castle-strip](pages/pell-castle-strip.md)] Act III.[^7]

- **Height-2 castles are counted by `2^w`, not by Pell.** Under the castle rules a row's blocks are its maximal runs, so the rule-3 gap is automatic and costs nothing; skylines over `{1, 2}` of widths 1 to 7 number `2, 4, 8, 16, 32, 64, 128`. There is no `x²` correction to the height-2 count.
- **The `k = 1` member of `den_k` is `1 − 2x + 2x²`**, the A146559 denominator ([[signed-tower-count](pages/signed-tower-count.md)]), not `1 − 2x − x²`. The resemblance between `(1 − 2x) + x·num_{k−1}` and the Pell denominator is one of shape only.
- **No two-state 0/1 transfer matrix has denominator `1 − 2x − x²`**; the smallest is `3×3`. The Pell strip is therefore not a height-`{1,2}` rule on the [[castle-strip](pages/castle-strip.md)] model.
- **Where Pell does live:** the 1-smooth strip on heights `{1, 2, 3}` (adjacent heights differ by at most 1), anchored at height 1, has width generating function exactly `1/(1 − 2x − x²)` and counts `P_{w+1}`; the free strip gives companion Pell A001333.

The coefficient-matching mechanic (Act I) and the two-atom tiling reading (Act II) are unaffected.

## Key Takeaways

- **Coefficient-matching as a mechanical method.** `(1 − 2x − x²)·D(x) = 1` → uniform recurrence `a_n − 2a_{n−1} − a_{n−2} = [n=0]` with `a_{negative} = 0`. Base cases are the same recurrence, not a special argument.[^1]
- **Two-atom composition reading.** `1/(1 − 2x − x²)` counts strip tilings with a width-1 weight-2 atom and a width-2 weight-1 atom.[^2]
- **The note's reading of the atoms as PE 502's structural rules** (per-column binary state supplies `2x`; the rule-3 block+gap unit supplies `x²`)[^3] — **withdrawn**, see the Correction above.
- **The note's "baby case" claim** (that `D(x)` is the `k = 1` member of `den_k = den_{k−1}(1−2x) + x·num_{k−1}`)[^5] — **withdrawn**; `den_1 = 1 − 2x + 2x²`.
- **Pell fingerprint.** Sequence `1, 2, 5, 12, 29, …` = OEIS A000129 shifted (Pell); growth constant `1 + √2 = [2;2,2,…]` — the silver ratio already tracked as one of the wiki's two norm-`−1` reduced quadratics.[^6]
- **Pedagogy shape.** A textbook end-of-chapter question about extracting a recurrence from a generating function *spirals into* an entire seminar on castles and polyomino theory. The Analysis page [[pell-castle-strip](pages/pell-castle-strip.md)] captures that arc.

## Entities & Concepts

- [[pell-numbers](pages/pell-numbers.md)] — the underlying integer sequence and its silver-ratio growth.
- [[pell-castle-strip](pages/pell-castle-strip.md)] — the seminar-shaped Analysis this note is the source for.
- [[generating-functions](pages/generating-functions.md)] — the concept page, whose "coefficient matching for GF → recurrence" section this note supplies.
- [[castle-counting-formula](pages/castle-counting-formula.md)] — the recurrence (`den_k = den_{k−1}(1−2x) + x·num_{k−1}`) the note tried to match; its `k = 1` member is `1 − 2x + 2x²`.
- [[eigenvalue-continued-fractions](pages/eigenvalue-continued-fractions.md)] — where `1+√2 = [2;2,2,…]` already lives.
- [[tower-word-continued-fraction](pages/tower-word-continued-fraction.md)] — where `1+√2` also appears, as the tower-word growth constant.

## Relation to Other Wiki Pages

The note is the seed of a small but coherent thread: (i) a general method (coefficient matching, added to [[generating-functions](pages/generating-functions.md)]), (ii) a new sequence page ([[pell-numbers](pages/pell-numbers.md)]) that connects existing continued-fraction and eigenvalue material to a fresh castle-shaped example, (iii) an Analysis page ([[pell-castle-strip](pages/pell-castle-strip.md)]) that captures the pedagogy — how a small AC exercise opens onto castle strips and the silver ratio, with the rule-3 reading corrected along the way.

## Footnotes

[^1]: [[pe502-pell-castle-strip](pages/pe502-pell-castle-strip.md)] §"Where the recurrence comes from" L9-L19 — "Matching coefficients on (1 − 2x − x²) D(x) = 1: [x^0]: a_0 = 1; [x^1]: a_1 − 2a_0 = 0, so a_1 = 2; [x^{n+2}] for n ≥ 0: a_{n+2} − 2a_{n+1} − a_n = 0 ... The a_n term doesn't 'disappear' at the boundary - it multiplies a_{−1}, which is 0 by convention (a power series has no negative powers). Uniformly: a_n − 2a_{n−1} − a_{n−2} = [n = 0] with a_{−1} = a_{−2} = 0. The base cases a_0 = 1, a_1 = 2 are the same recurrence evaluated at n = 0, 1 with those zeros substituted. Nothing special about them."
[^2]: [[pe502-pell-castle-strip](pages/pe502-pell-castle-strip.md)] §"The castle reading" L23-L28 — "D(x) = 1/(1 − 2x − x²) is a two-atom composition scheme. Read it as counting tilings of a 1 × n strip using: a width-1 atom with weight 2; a width-2 atom with weight 1. Then a_n is the total weight of such tilings, and a_n = 2 a_{n−1} + a_{n−2} is just 'peel off the last atom.'"
[^3]: [[pe502-pell-castle-strip](pages/pe502-pell-castle-strip.md)] §"The castle reading" L30-L38 — "Unsigned tower count. T(k, L) = (k+1)^L. For height-2 towers (k = 1), that's 2^L: each column independently picks one of two states. This is the width-1, weight-2 atom. ... Rule 3, mandatory gap. Adjacent blocks on the same row need a gap of width ≥ 1. Bundle 'block-end + start-of-mandatory-gap' as one atomic unit and its minimum width is 2. This is the width-2, weight-1 atom."
[^4]: [[pe502-pell-castle-strip](pages/pe502-pell-castle-strip.md)] §"The castle reading" L40 — "Without rule 3 you'd only have the 2x atom, denominator 1 − 2x, and a_n = 2^n - the naive 2^L per-column count. The x² term is what rule 3 costs you."
[^5]: [[pe502-pell-castle-strip](pages/pe502-pell-castle-strip.md)] §"Match with the wiki's rational recurrence" L44-L48 — "The wiki gives, for the signed castle generating function: den_k = den_{k−1}(1 − 2x) + x · num_{k−1}. Same shape: a (1 − 2x) factor (per-column binary atom) plus a smaller x-weighted correction (the mandatory-gap tax). D(x) is the baby case of that family - the height-2, one-signed-strip castle."
[^6]: [[pe502-pell-castle-strip](pages/pe502-pell-castle-strip.md)] §"The Pell fingerprint" L52-L54 — "a_0, a_1, a_2, … = 1, 2, 5, 12, 29, 70, 169, … Half-companion Pell numbers, growth rate 1 + √2." The sequence `1, 2, 5, 12, 29, 70, 169, 408, 985, 2378` re-verified during ingest as OEIS A000129 shifted (`a_n = P_{n+1}`), *not* the half-companion Pell A001333 = `1, 1, 3, 7, 17, 41, …` — the note's terminology is slightly off; the sequence is Pell proper.
[^7]: Verified by execution (Python 3, SymPy) on 2026-09-19; the computations are pinned in [[pell-castle-strip](pages/pell-castle-strip.md)] footnotes 4 and 6 (height-2 enumeration `2, 4, 8, 16, 32, 64, 128`; `den_1 = 1 − 2x + 2x²`; the six possible `2×2` 0/1 determinants; and `e_1ᵀ(I − xM)^{−1}𝟙 = 1/(1 − 2x − x²)` for the 1-smooth height-3 matrix).
