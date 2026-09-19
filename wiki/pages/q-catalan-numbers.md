---
title: q-Catalan numbers
category: Concepts
summary: Polynomial q-analogs of the Catalan numbers (C_n(q) → C_n at q=1) — several families (Carlitz, MacMahon/Krattenthaler/Gessel, Polya/Gessel); the last counts parallelogram polyominoes by area, a castle q-thread.
tags: [concept, q-catalan, q-analog, catalan, dyck-words, polyomino]
sources: [q-catalan-numbers]
created: 2026-09-13
updated: 2026-09-13
---

# q-Catalan numbers

## Description

The **q-Catalan numbers** are polynomial q-analogs of the [[catalan-numbers](pages/catalan-numbers.md)]: each `C_n(q)` reduces to `C_n` at `q = 1`. Because different authors track different statistics, there is more than one family:[^1]

- **Carlitz q-Catalan** — count inversions of Dyck words and Catalan permutations.[^2]
- **MacMahon / Krattenthaler / Gessel q-Catalan** — enumerate Dyck words by parameters of the down set.[^2]
- **Polya / Gessel q-Catalan** — count **parallelogram polyominoes by area**.[^2]

## Connection to the castle

The third family is the direct castle thread: **parallelogram polyominoes by area** are exactly the objects of [[steep-polyominoes-q-motzkin-bessel](pages/steep-polyominoes-q-motzkin-bessel.md)] (steep parallelogram polyominoes, whose area/perimeter generating function is a ratio of q-Bessel functions), and the [[polyominoes](pages/polyominoes.md)] page notes Ferrers polyominoes' area generating functions relate to q-Bessel and q-Catalan numbers. The castle is counted by *area* to great effect (convex ↔ A001523 on [[castle-by-area](pages/castle-by-area.md)]); grading that area count by *q* is the natural way the castle would meet the q-Catalan world — the open q-equivalent thread (see the wiki TODO). The inversion-counting Carlitz family also rhymes with the inversion statistic on steep Dyck words.

## Appearances in Sources

- [[q-catalan-numbers](pages/q-catalan-numbers.md)] (charlesreid1.com topic page) — the three q-Catalan families and their statistics.

## Related Concepts

- [[catalan-numbers](pages/catalan-numbers.md)] — the q=1 specialization.
- [[motzkin-numbers](pages/motzkin-numbers.md)] — the sister q-analog thread (q-Motzkin).
- [[steep-polyominoes-q-motzkin-bessel](pages/steep-polyominoes-q-motzkin-bessel.md)] — parallelogram polyominoes by area, q-Bessel GF
- [[castle-by-area](pages/castle-by-area.md)] — the castle's area grading, the q-analog's entry point.
- [[dyck-words](pages/dyck-words.md)] — the object whose inversions the Carlitz q-Catalan (and, by steepness, q-Motzkin) count.
- [[permutation-inversions](pages/permutation-inversions.md)] — the inversion statistic and the q-factorial `∏(1−z^k)/(1−z)^n`, the prototype q-graded generating function.

## Footnotes

[^1]: [[q-catalan-numbers](pages/q-catalan-numbers.md)] §"q-Catalan Numbers" L5 — "polynomial q-analogs of the ordinary Catalan Numbers: each C_n(q) reduces to C_n at q = 1. Different authors track different statistics, so there is more than one family."
[^2]: [[q-catalan-numbers](pages/q-catalan-numbers.md)] §"q-Catalan Numbers" L7-9 — "Carlitz q-Catalan numbers count inversions of Dyck Words and Catalan permutations ... MacMahon, Krattenthaler, Gessel ... enumerate Dyck words by parameters of the down set ... Polya, Gessel ... count parallelogram polyominoes by area."
