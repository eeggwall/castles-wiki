---
title: Motzkin numbers
category: Concepts
summary: M_n counts non-crossing chords on n points and Motzkin (up/flat/down) lattice paths; 1,1,2,4,9,21,…; its q-analog appears in the q-grammar count of steep Dyck words — a castle thread.
tags: [concept, motzkin, lattice-paths, q-analog, generating-functions]
sources: [motzkin-numbers, steep-polyominoes-q-motzkin-bessel]
created: 2026-09-13
updated: 2026-10-06
---

# Motzkin numbers

## Description

The **Motzkin number** `M_n` counts the ways to draw non-intersecting chords between *n* points on a circle, equivalently the **Motzkin paths** — lattice paths from `(0,0)` to `(n,0)` using up, horizontal, and down steps that never drop below the axis.[^1] The first values are[^2]

```
1, 1, 2, 4, 9, 21, 51, 127, 323, 835, …
```

(re-verified during ingest from the recurrence). They satisfy[^3]

```
M_0 = M_1 = 1,   M_n = M_{n−1} + Σ_{k=0}^{n−2} M_k M_{n−2−k},
   generating function  M(x) = (1 − x − √(1 − 2x − 3x²)) / (2x²)
```

Motzkin paths use *three* step types (up/flat/down), the same arity as the castle's U/R/D words.

## Connection to the castle

The relevant thread: the **q-analog `M_n(q)`** refines the Motzkin numbers and appears in the **q-grammar count of steep Dyck words**[^4] — the object in [[steep-polyominoes-q-motzkin-bessel](pages/steep-polyominoes-q-motzkin-bessel.md)], where three q-Motzkin classes are tied to steep parallelogram polyominoes (a q-Bessel-ratio GF), inversions of steep Dyck words, and steep staircase polyominoes by area. The castle's [[generalized-dyck-grammar](pages/generalized-dyck-grammar.md)] is also a three-letter (U/R/D) grammar with run constraints. Graded by area and blocks, it gives a q-Bessel ratio of the same kind, built from the parallelogram series rather than a q-Motzkin one ([[castle-q-bessel-closed-form](pages/castle-q-bessel-closed-form.md)]).

## Appearances in Sources

- `raw/motzkin-numbers.wiki` (charlesreid1.com topic page) — definition, values, recurrence, GF, and the q-analog / steep-Dyck-words remark.
- [[steep-polyominoes-q-motzkin-bessel](pages/steep-polyominoes-q-motzkin-bessel.md)] — the paper where q-Motzkin numbers meet steep polyominoes.

## Related Concepts

- [[motzkin-castles](pages/motzkin-castles.md)] - the hub for exact Motzkin appearances in castles: castles as cornerless Motzkin paths, the parity split of `M_{w-1}` (A343386 / A107587), the Gaussian `1 ± 2i` sign, and the bounded-height ladder.
- [[q-catalan-numbers](pages/q-catalan-numbers.md)] — the sister q-analog family; both reduce at q=1.
- [[castle-q-bessel-closed-form](pages/castle-q-bessel-closed-form.md)] - the castle grammar graded by area: a q-Bessel ratio over the parallelogram series.
- [[narayana-numbers](pages/narayana-numbers.md)], [[catalan-numbers](pages/catalan-numbers.md)] — Motzkin's Catalan relatives (Motzkin sums of Narayana/Catalan-type terms).
- [[generalized-dyck-grammar](pages/generalized-dyck-grammar.md)] — the castle's three-letter grammar, the same arity as Motzkin paths.
- [[tower-word-language](pages/tower-word-language.md)] — the tower words, a Motzkin-path language with the same U/R/D step set.
- [[dyck-words](pages/dyck-words.md)] — steep Dyck words of length 2n are counted by the (n−1)th Motzkin number.
- [[marin-2024-polyominoes-in-rectangle](pages/marin-2024-polyominoes-in-rectangle.md)] — the row automaton for polyominoes with bounding box of width `w` has `M_{w+1} + 2M_w + M_{w−1} − 3` states (A378947).
- [[aocp-multinomial-coefficients](pages/aocp-multinomial-coefficients.md)] — the central trinomial coefficients A002426 count unconstrained `U/R/D` words returning to height 0; Motzkin numbers are the ballot-restricted version.

## Footnotes

[^1]: raw/motzkin-numbers.wiki §"Motzkin Numbers" L3 — "The Motzkin number M_n counts the ways to draw non-intersecting chords between n points on a circle, and the Motzkin paths: lattice paths from (0,0) to (n,0) using up, horizontal, and down steps that never drop below the x axis."
[^2]: raw/motzkin-numbers.wiki §"First values" L8 — "1, 1, 2, 4, 9, 21, 51, 127, 323, 835, ..."; re-verified from the recurrence during ingest.
[^3]: raw/motzkin-numbers.wiki §"Recurrence"/"Generating function" L18-24 — "M_n = M_{n-1} + sum_{k=0}^{n-2} M_k M_{n-2-k}" and "M(x) = (1 - x - sqrt(1 - 2x - 3x^2)) / (2x^2)."
[^4]: raw/motzkin-numbers.wiki §"Motzkin Numbers" L27 — "The q-analog M_n(q) refines the Motzkin numbers and appears in the q-grammar count of steep Dyck Words."
