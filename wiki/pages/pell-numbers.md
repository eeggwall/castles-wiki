---
title: Pell numbers
category: Concepts
summary: P_n = 2·P_{n−1} + P_{n−2} with P_0=0, P_1=1 — the integer sequence 0, 1, 2, 5, 12, 29, 70, 169, … (OEIS A000129) whose growth constant is the silver ratio 1 + √2. In the castle wiki, they count the 1-smooth height-3 castle strip anchored at the base ([[pell-castle-strip]]).
tags: [concept, pell, integer-sequence, silver-ratio, quadratic-irrational, continued-fraction, oeis]
sources: [pe502-pell-castle-strip]
created: 2026-09-15
updated: 2026-09-19
---

# Pell numbers

## Definition

The **Pell numbers** are the integer sequence `P_n` defined by the linear recurrence[^1]

```
P_0 = 0,   P_1 = 1,   P_n = 2·P_{n−1} + P_{n−2}   for n ≥ 2.
```

The first values are

```
P_n  =  0, 1, 2, 5, 12, 29, 70, 169, 408, 985, 2378, 5741, 13860, 33461, …
```

= **OEIS [A000129](https://oeis.org/A000129)**. The generating function is the rational function[^1]

```
∑_{n≥0} P_n · x^n  =  x / (1 − 2x − x²).
```

Ratios of consecutive Pell numbers `P_{n+1}/P_n` converge to `√2 + 1 = 2.41421…` — the **silver ratio** (or **silver mean**), denoted `δ_S` or `δ_2` — because the characteristic polynomial `x² − 2x − 1` has roots `1 ± √2` and the recurrence is dominated by the larger root.[^2] `√2 + 1` is the norm-`−1` reduced surd whose purely periodic continued fraction is `[2; 2, 2, 2, …]` (see [[eigenvalue-continued-fractions](pages/eigenvalue-continued-fractions.md)]).

**Naming caveat.** "Silver ratio" is not universal. The dominant modern usage — and the one this wiki adopts — is `1 + √2` (the metallic-mean value, per Vera W. de Spinadel's [[metallic-means](pages/metallic-means.md)] framing; matches Wikipedia and OEIS cross-references).[^7] A minority usage (typically in paper-size / A-series-paper contexts) reserves "silver ratio" for `√2 ≈ 1.4142` itself. Both are correct in their own literature; whenever this wiki says "silver ratio" we mean `1 + √2`. The Pell numbers realize the silver ratio in the same way Fibonacci realizes the golden ratio — both are members of the [[metallic-means](pages/metallic-means.md)] family (Pell at `a = 2`, Fibonacci at `a = 1`).

## Two roles in the wiki

The Pell numbers earn a page here because they land at two structurally-informative points:

### 1. As the count sequence of the [[pell-castle-strip](pages/pell-castle-strip.md)]

The rational function `1/(1 − 2x − x²)` — one degree of freedom away from Pell's own generating function `x/(1 − 2x − x²)` — has coefficients `1, 2, 5, 12, 29, 70, 169, …` = `P_{n+1}` shifted.[^3] Read symbolically it is a two-atom tiling scheme (a width-1 atom of weight 2 and a width-2 atom of weight 1), and it has an exact castle realization: the **1-smooth strip of height at most 3, anchored at the base** — skylines over `{1, 2, 3}` with `|c_{i+1} − c_i| ≤ 1` and first column at height 1 — whose width generating function is exactly `1/(1 − 2x − x²)`, so the number of such strips of width `w` is `P_{w+1}`. Freeing the first column gives the companion Pell numbers (A001333) instead.[^8]

### 2. As the concrete integer realization of `1 + √2`

The [[eigenvalue-continued-fractions](pages/eigenvalue-continued-fractions.md)] page presents `1 + √2 = [2; 2, 2, …]` as one of the castle's two purely periodic norm-`−1` quadratics (the other being `φ` for Fibonacci). Pell is what `1 + √2` looks like as an integer recurrence, in the way that Fibonacci is what `φ` looks like — the *convergents* of `[2; 2, 2, …]` are Pell ratios `P_{n+1}/P_n = 2, 5/2, 12/5, 29/12, 70/29, 169/70, …`, verified in [[eigenvalue-continued-fractions](pages/eigenvalue-continued-fractions.md)] footnote 4.[^4] The tower-word growth constant is the same `1 + √2` ([[tower-word-continued-fraction](pages/tower-word-continued-fraction.md)]) — so Pell is the integer skeleton of the castle's silver-ratio thread the same way Fibonacci is the integer skeleton of its golden-ratio thread.

## The Pell / Fibonacci parallelism

The wiki now tracks the two norm-`−1` quadratics symmetrically:

| Quadratic surd | Continued fraction | Recurrence | Sequence | Wiki appearance |
|---|---|---|---|---|
| `φ = (1+√5)/2` | `[1; 1, 1, …]` | `F_n = F_{n−1} + F_{n−2}` | Fibonacci (A000045) | prime-castle count `2^{n−1} − F_{n−1}` on [[castle-by-area](pages/castle-by-area.md)]; the Fibonacci method of [[aocp-generating-functions](pages/aocp-generating-functions.md)] |
| `1 + √2` | `[2; 2, 2, …]` | `P_n = 2·P_{n−1} + P_{n−2}` | **Pell (A000129)** | the anchored 1-smooth height-3 strip of [[pell-castle-strip](pages/pell-castle-strip.md)]; tower-word growth constant on [[tower-word-continued-fraction](pages/tower-word-continued-fraction.md)] |

Both are the fundamental units of their respective real quadratic fields (`φ` of `Q(√5)`, `1+√2` of `Q(√2)`), both are period-one purely periodic, and both realize their surd through a linear recurrence with characteristic polynomial `x² − ax − 1` (`a = 1` for Fibonacci, `a = 2` for Pell). The Pell case adds nothing conceptually new; it fills in the wiki's second row of a two-row family we had already implicitly assembled.

## Closed forms and identities

The **Binet-style formula** follows from the characteristic roots `1 ± √2`:[^2]

```
P_n = ((1 + √2)^n − (1 − √2)^n) / (2√2).
```

The **companion Pell** (or *Pell-Lucas half*) sequence is OEIS A001333 = `1, 1, 3, 7, 17, 41, 99, 239, 577, …`, defined by the same recurrence but with `Q_0 = 1, Q_1 = 1`, and satisfies `Q_n = ((1+√2)^n + (1−√2)^n)/2` — the numerators of the continued-fraction convergents of `√2 = [1; 2, 2, 2, …]`.[^5] The anchored Pell castle strip counts are Pell proper; the free strip counts are companion Pell.

## Appearances in Sources

- [[pe502-pell-castle-strip](pages/pe502-pell-castle-strip.md)] — introduces the two-atom reading of `1/(1 − 2x − x²)`; the sequence identity was verified against OEIS A000129 during ingest.

## Related Concepts

- [[pell-castle-strip](pages/pell-castle-strip.md)] — the Analysis page that runs from the AC end-of-chapter exercise to the castle interpretation.
- [[eigenvalue-continued-fractions](pages/eigenvalue-continued-fractions.md)] — where `1 + √2 = [2; 2, 2, …]` is developed as one of the castle's two norm-`−1` quadratics.
- [[tower-word-continued-fraction](pages/tower-word-continued-fraction.md)] — where `1 + √2` also appears, as the tower-word growth constant.
- [[aocp-generating-functions](pages/aocp-generating-functions.md)] — the Fibonacci companion (`φ`, `[1;1,1,…]`) — the same story with `a = 1`.
- [[castle-by-area](pages/castle-by-area.md)] — the wiki's other integer-sequence-plus-quadratic-surd pairing (`2^{n−1} − F_{n−1}`).
- [[metallic-means](pages/metallic-means.md)] — the family `δ_a = (a + √(a²+4))/2` (`a = 1, 2, 3, …`) — Fibonacci/Pell/Bronze/Copper/… — that Pell sits at `a = 2` of.

## Footnotes

[^1]: OEIS A000129, verified during ingest — the recurrence `P_0 = 0, P_1 = 1, P_n = 2P_{n−1} + P_{n−2}` gives values `0, 1, 2, 5, 12, 29, 70, 169, 408, 985, 2378, 5741, 13860, 33461, …`; the generating function `x/(1−2x−x²)` follows from coefficient-matching `(1−2x−x²)·G(x) = x` (the standard `x·[1] − 0 = x` boundary).
[^2]: The characteristic polynomial `x² − 2x − 1` has roots `1 ± √2`; the Binet form `P_n = ((1+√2)^n − (1−√2)^n)/(2√2)` was re-derived and verified numerically for `n = 0..12` during ingest.
[^3]: [[pe502-pell-castle-strip](pages/pe502-pell-castle-strip.md)] §"The castle reading" L23-L28 — the two-atom composition scheme for `1/(1 − 2x − x²)`.
[^4]: [[eigenvalue-continued-fractions](pages/eigenvalue-continued-fractions.md)] §"Step 5 — The castle's eigenvalues" and footnote 4 — the convergents `5/2, 12/5, 29/12, 70/29, 169/70 → √2 + 1` are exactly the Pell ratios `P_{n+1}/P_n` for `n = 2..6`, verified during that page's ingest.
[^5]: OEIS A001333 = `1, 1, 3, 7, 17, 41, 99, 239, 577, 1393, …`, the companion Pell / Pell-Lucas half. Its Binet form `Q_n = ((1+√2)^n + (1−√2)^n)/2` was verified numerically for `n = 0..10` during ingest. A001333 numerators pair with A000129 denominators to give the continued-fraction convergents of `√2 = [1; 2, 2, 2, …]`.
[^7]: [[metallic-means](pages/metallic-means.md)] §"The naming caveat" — Wikipedia "Silver ratio" and OEIS A001333 (whose comment describes it in Pell / silver-mean context) both use "silver ratio" for `1 + √2`; this is also the usage in de Spinadel's original paper (`δ_S`). Competing "silver ratio = √2" appears in paper-size / A-series / architecture literature; when meant, it is usually specified. Wiki standard: `δ_2 = 1 + √2`.
[^8]: Verified by execution (Python 3, SymPy), 2026-09-19, recorded on [[pell-castle-strip](pages/pell-castle-strip.md)] footnote 4: for the 1-smooth matrix `M = [[1,1,0],[1,1,1],[0,1,1]]` on heights `{1,2,3}`, `e_1ᵀ(I − xM)^{−1}𝟙 = 1/(1 − 2x − x²)`, with enumerated counts `1, 2, 5, 12, 29, 70, 169, 408` (first column 1) and `3, 7, 17, 41, 99, 239, 577, 1393` (free first column).
