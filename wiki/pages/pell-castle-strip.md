---
title: "The Pell castle strip — from an AC exercise to the castle's rule-3 tax"
category: Analyses
summary: A seminar-shaped analysis. Start with an Analytic Combinatorics end-of-chapter exercise — "extract the recurrence from D(x) = 1/(1−2x−x²)" — and spiral into the castle's structural rules, the wiki's rational recurrence, and the silver-ratio thread already in the wiki. The pedagogy is the point: a small textbook question opens directly onto polyomino theory.
tags: [analysis, castle, pell, generating-functions, coefficient-matching, seminar, pedagogy, silver-ratio]
sources: [pe502-pell-castle-strip]
created: 2026-09-15
updated: 2026-09-15
---

# The Pell castle strip — from an AC exercise to the castle's rule-3 tax

## The pedagogy is the point

An Analytic Combinatorics chapter closes with an exercise that looks like nothing: **given the generating function `D(x) = 1/(1 − 2x − x²)`, produce the recurrence and its base cases**. It is a five-line calculation. But it is also the doorway to an entire seminar on PE 502 castles — the denominator `1 − 2x − x²` splits *exactly* along two of PE 502's structural rules, the same-shape recurrence lifts to the wiki's [[castle-counting-formula](pages/castle-counting-formula.md)], and the sequence that falls out is a fingerprint of a quadratic surd the wiki already tracks. Ninety minutes of blackboard from one line of a textbook.

This page is that seminar in written form. It runs a slightly larger loop than the underlying working note [[pe502-pell-castle-strip](pages/pe502-pell-castle-strip.md)] to make each step teachable — the "where does the base case come from" resolution, the two-atom composition scheme, the identification with PE 502's rules, the silver-ratio thread. The point is not the answer (a rational function and a Pell recurrence). The point is that **a textbook end-of-chapter question about extracting a recurrence spirals into polyomino theory** if you look at what its atoms are counting.

## Act I — Coefficient matching, and where the "base cases" hide

The exercise: given

```
D(x) = 1/(1 − 2x − x²)  =  ∑_{i≥0} a_i · x^i,
```

find the recurrence for `a_n` and its base cases. Multiply through:

```
(1 − 2x − x²) · D(x)  =  1.
```

The left side is a product of two power series; each coefficient of `x^n` on the right must match the corresponding coefficient on the left. Coefficient extraction is mechanical:[^1]

- `[x^0]`: `a_0 = 1`.
- `[x^1]`: `a_1 − 2·a_0 = 0`, so `a_1 = 2`.
- `[x^{n+2}]` for `n ≥ 0`: `a_{n+2} − 2·a_{n+1} − a_n = 0`.

The **"base cases" have no independent existence**. Written uniformly with the "negative index equals zero" convention (a power series has no negative powers), the recurrence and the boundary are the same object:[^1]

```
a_n − 2·a_{n−1} − a_{n−2}  =  [n = 0],       a_{−1} = a_{−2} = 0.
```

At `n = 0`, this reads `a_0 − 2·0 − 0 = 1`, so `a_0 = 1`. At `n = 1`, it reads `a_1 − 2·a_0 − 0 = 0`, so `a_1 = 2`. **Base cases are the recurrence evaluated at the boundary.** The "special-case argument" a student expects at the start never appears because it was never needed.

**Why this matters for the wiki.** The [[castle-counting-formula](pages/castle-counting-formula.md)] carries recurrences whose base cases *look* argued for, but under the same coefficient-matching lens they are the recurrence evaluated at `k = 0` or `L = 0` with zeros substituted. The technique is the shortcut, and it is added to [[generating-functions](pages/generating-functions.md)] as the general GF → recurrence method.

## Act II — Two-atom composition: what is the rational function counting?

`1/(1 − 2x − x²)` is one of the simplest **rational** generating functions after the geometric series `1/(1 − x)` and its weighted cousin `1/(1 − 2x)`. Read symbolically: it is a `SEQ` construction (see [[symbolic-method](pages/symbolic-method.md)]) over two atoms combined into an alphabet of weight `2x + x²`.[^2]

- **Width-1 atom of weight 2** — the `2x` term. Two distinguishable copies of a size-1 building block.
- **Width-2 atom of weight 1** — the `x²` term. One copy of a size-2 building block.

Any word `a_1 a_2 … a_k` over this alphabet has total weight `2^{#(width-1 atoms)}` and total width `∑ |a_i| = n`, and the generating function `∑_{words} (weight)·(x^{width})` is exactly `∑_k (2x + x²)^k = 1/(1 − 2x − x²)`. So `a_n` is the total weight of all strip tilings of length `n` under this alphabet. The recurrence `a_n = 2·a_{n−1} + a_{n−2}` is the "peel off the last atom" argument: either the strip ends in a width-1 atom (2 choices, leaving a strip of length `n−1`) or in a width-2 atom (1 choice, leaving `n−2`).[^2]

## Act III — The two atoms are PE 502's structural rules

Here is where the exercise stops being generic combinatorics and becomes about castles.

**Rule (i): the per-column binary state.** For a castle of height exactly `h` with tower height at most `k = h − 1`, the unsigned tower count is `T(k, L) = (k+1)^L` ([[castle-counting-formula](pages/castle-counting-formula.md)]) — each of the `L` columns picks a height independently in `{0, 1, …, k}`. For `k = 1` (height-2 towers), this is `2^L`. **The width-1 weight-2 atom is exactly this per-column binary choice.**[^3]

**Rule (ii): the mandatory gap (rule 3).** PE 502's rule 3 says adjacent blocks in the same row must have a gap of width `≥ 1`. Bundle "block-end + start-of-mandatory-gap" as a single atomic unit — its minimum width is 2 columns. **The width-2 weight-1 atom is this bundled block+gap unit.**[^3]

So the denominator splits directly along PE 502's structural rules:

```
1     −     2x                             −     x²
                                                  
              per-column binary state,             mandatory-gap block+gap unit
              i.e. T(1, L) = 2^L                   from rule 3
```

Take rule 3 away and the `x²` atom disappears; the denominator collapses to `1 − 2x`, `a_n = 2^n`, and you get the naive height-2 column-product count with no gap correction.[^4] **The `x²` term is the price of rule 3.** Equivalently, `x²` is the correction that turns a raw column product into a proper castle count. It is not a nuisance; it is what makes the counting problem PE 502 rather than PE something-elementary.

## Act IV — The Pell fingerprint

The counts

```
a_n  =  1, 2, 5, 12, 29, 70, 169, 408, 985, 2378, 5741, 13860, …
```

are **Pell numbers, OEIS [A000129](https://oeis.org/A000129) shifted** (`a_n = P_{n+1}`).[^5] See [[pell-numbers](pages/pell-numbers.md)] for the linear-recurrence definition and its Binet form. The dominant characteristic root of `x² − 2x − 1` is `1 + √2 ≈ 2.4142`, so `a_n ~ C · (1 + √2)^n` — the growth rate is the **silver ratio**.

`1 + √2` is not a fresh entrant; the wiki already tracks it prominently. On [[eigenvalue-continued-fractions](pages/eigenvalue-continued-fractions.md)] it is one of two **norm-`−1` reduced quadratic surds** with purely periodic continued fraction: `1 + √2 = [2; 2, 2, 2, …]`. On [[tower-word-continued-fraction](pages/tower-word-continued-fraction.md)] it is the **tower-word growth constant** — the singularity of the algebraic generating function for tower words counted by total steps sits at `√2 − 1`, growth rate `1/(√2 − 1) = √2 + 1`.

So the silver-ratio thread has three concrete faces in the wiki: an algebraic-GF face (tower word), a continued-fraction face (`[2;2,2,…]`), and now an integer-sequence face (Pell) with a physical castle-strip interpretation. Pell is what the surd `1 + √2` looks like as an integer sequence, in exactly the way Fibonacci is what `φ` looks like ([[aocp-generating-functions](pages/aocp-generating-functions.md)]).

## Act V — Same shape as the wiki's rational recurrence

The mnemonic locks in structurally with the full castle recurrence. The wiki gives the signed castle generating function's rational recurrence[^6]

```
den_k  =  den_{k−1} · (1 − 2x)  +  x · num_{k−1}.
```

The **same shape** as the Pell strip's denominator `1 − 2x − x²`:

- A `(1 − 2x)` factor — the per-column binary atom, generalized: for a height-`k+1` tower it becomes `(1 − (k+1)x)` in the unsigned case. In the Pell strip, `k = 1` gives `1 − 2x` exactly.
- A trailing `x`-weighted correction of smaller degree — the generalized mandatory-gap tax, with `x·num_{k−1}` recording the structural memory. In the Pell strip, this collapses to `x²` because `num_0 = x` and there is no signed layer.

The Pell strip is the **baby case** of the entire family. Everything the wiki's algorithms — Kitamasa, Berlekamp-Massey ([[castle-count-algorithms](pages/castle-count-algorithms.md)]) — do on the full family, they do on Pell as a warmup: from a rational generating function, produce a linear recurrence, and evaluate at large indices.

## The seminar shape

Suggested outline for a talk:

1. **Cold open:** put `D(x) = 1/(1 − 2x − x²)` on the board and ask the audience for its recurrence. Solicit "base case" answers, then run coefficient matching to show the base cases *are* the recurrence.
2. **Act II: what is it counting?** Introduce the two-atom composition scheme. Explain the pattern `1/(1 − ∑ (weight)·x^(width))` = strip tilings under a general SEQ. This is the [[symbolic-method](pages/symbolic-method.md)] in miniature.
3. **Act III: reveal the castles.** Draw a height-2 castle strip; identify the two atoms explicitly (one column of binary state + one block-end-plus-gap unit). This is where the audience realizes the exercise was never abstract.
4. **Act IV: pull the growth rate.** Compute a few Pell numbers, take ratios, identify `1 + √2`. Sketch the continued-fraction expansion `[2; 2, 2, …]`. Mention Fibonacci / `φ` as the parallel case.
5. **Act V: lift to the full castle recurrence.** Write `den_k = den_{k−1}(1 − 2x) + x·num_{k−1}` and identify each factor. Point at Kitamasa / Berlekamp-Massey.
6. **Close:** the audience walked in expecting a five-line homework and leaves with the entire PE 502 pipeline — coefficient extraction, symbolic method, structural atomic decomposition, growth via a norm-`−1` quadratic, evaluation at trillion-scale indices. **The exercise was the seminar.**

## The general pedagogy claim

A rational generating function's denominator is a factored inventory of its **structural rules**. The atoms are what the rules cost. In a well-designed exercise, the denominator is small and the atoms are legible; if you are lucky, they map to a rich combinatorial object at another scale. The Pell castle strip is that lucky case: `1 − 2x − x²` is short, its two atoms are legible, and PE 502 is the object at the other scale. This is what turns AC textbook exercises into seminars — reading the atoms, not just the coefficients.

## Appearances in Sources

- [[pe502-pell-castle-strip](pages/pe502-pell-castle-strip.md)] — the working note that seeded this seminar arc.

## Related Concepts

- [[pell-numbers](pages/pell-numbers.md)] — the integer sequence and its silver-ratio growth.
- [[generating-functions](pages/generating-functions.md)] — the coefficient-matching technique and the symbolic-method context.
- [[symbolic-method](pages/symbolic-method.md)] — the `SEQ` construction the two-atom scheme is an instance of.
- [[castle-counting-formula](pages/castle-counting-formula.md)] — the wiki's full rational recurrence, of which Pell is the baby case.
- [[castle-count-algorithms](pages/castle-count-algorithms.md)] — Kitamasa / Berlekamp-Massey on the Pell recurrence as a warmup for the full family.
- [[eigenvalue-continued-fractions](pages/eigenvalue-continued-fractions.md)] — where `1 + √2 = [2;2,2,…]` is developed.
- [[tower-word-continued-fraction](pages/tower-word-continued-fraction.md)] — where `1 + √2` also appears, as the tower-word growth constant.
- [[aocp-generating-functions](pages/aocp-generating-functions.md)] — the Fibonacci / `φ` companion (same story with `a = 1`).
- [[castle-classification](pages/castle-classification.md)] — the Axis-8 meta-classification for which this strip is the canonical **silver width growth castle** example (a class whose count sequence graded by width grows at `1+√2`).

## Footnotes

[^1]: [[pe502-pell-castle-strip](pages/pe502-pell-castle-strip.md)] §"Where the recurrence comes from" L9-L19 — coefficient-matching mechanics, and the uniform recurrence `a_n − 2a_{n−1} − a_{n−2} = [n = 0]` with `a_{−1} = a_{−2} = 0`. Re-verified during ingest by evaluating the recurrence at the boundary and matching against direct series expansion of `1/(1−2x−x²)`.
[^2]: [[pe502-pell-castle-strip](pages/pe502-pell-castle-strip.md)] §"The castle reading" L23-L28 — the two-atom composition scheme, its "peel off the last atom" recurrence. Under the SEQ construction (see [[symbolic-method](pages/symbolic-method.md)] Theorem I.1), `SEQ(2·Z + Z²)` has OGF `1/(1 − 2z − z²)`.
[^3]: [[pe502-pell-castle-strip](pages/pe502-pell-castle-strip.md)] §"The castle reading" L30-L38 — the identification `2x = per-column binary state (T(1,L) = 2^L)` and `x² = block-end + start-of-mandatory-gap bundled as a width-2 unit`.
[^4]: [[pe502-pell-castle-strip](pages/pe502-pell-castle-strip.md)] §"The castle reading" L40 — "Without rule 3 you'd only have the 2x atom, denominator 1 − 2x, and a_n = 2^n - the naive 2^L per-column count. The x² term is what rule 3 costs you."
[^5]: The sequence `1, 2, 5, 12, 29, 70, 169, 408, 985, 2378, 5741, 13860` (produced by the recurrence with `a_0 = 1, a_1 = 2`) was numerically matched against OEIS A000129 = `0, 1, 2, 5, 12, 29, 70, 169, …` during ingest, confirming `a_n = P_{n+1}`. The growth ratio `a_{n+1}/a_n → 2.41421… = 1 + √2` verified for `n = 5..11`.
[^6]: [[pe502-pell-castle-strip](pages/pe502-pell-castle-strip.md)] §"Match with the wiki's rational recurrence" L44-L48 — "den_k = den_{k−1}(1 − 2x) + x · num_{k−1}. Same shape: a (1 − 2x) factor (per-column binary atom) plus a smaller x-weighted correction (the mandatory-gap tax). D(x) is the baby case of that family."
