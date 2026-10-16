---
title: "Steep Polyominoes, q-Motzkin Numbers and q-Bessel Functions (Barcucci et al.)"
category: Sources
summary: Barcucci, Del Lungo, Fédou and Pinzani define three q-analogs of the Motzkin numbers and interpret each. The first gives the generating function of steep parallelogram polyominoes by width, perimeter and area, which is a quotient of two q-Bessel functions; the second counts steep Dyck words by inversions; the third counts steep staircase polyominoes by area. The derivations use object grammars and q-grammars.
tags: [paper, polyomino, dyck-words, motzkin, generating-functions, q-analog, source]
sources: [steep-polyominoes-q-motzkin-bessel, bousquet-melou-fedou-1995-convex-polyominoes]
created: 2026-09-13
updated: 2026-10-16
---

# Steep Polyominoes, q-Motzkin Numbers and q-Bessel Functions (Barcucci et al.)

**Source:** `assets/PolyominosMotzkinBessel.pdf` (E. Barcucci, A. Del Lungo, J. M. Fédou, R. Pinzani, *Steep polyominoes, q-Motzkin numbers and q-Bessel functions*)
**Publication:** *Discrete Mathematics* **189** (1998) 21-42, DOI `10.1016/S0012-365X(97)00275-6`.[^1]
**Date ingested:** 2026-09-13
**Type:** paper (PDF, 21 pp.)

## Summary

The paper introduces three q-analogs of the Motzkin numbers and gives each a combinatorial interpretation:[^2]

- The **first** class gives the generating function of **steep parallelogram polyominoes** by width, perimeter and area. By a method based on pairs of paths in the plane, the paper proves that this generating function is a quotient of two q-Bessel functions.[^2][^3]
- The **second** class enumerates **steep Dyck words** by their number of inversions.[^2][^4]
- The **third** class counts **steep staircase polyominoes** by area.[^2]

A **(lower) steep parallelogram polyomino** is a parallelogram polyomino whose South border has no two consecutive horizontal steps; the steep staircase polyominoes form the set `SS`.[^5] The paper relates the q-Motzkin numbers to these families with object grammars, and counts the steep Dyck words by length and inversion number with q-grammars.[^4]

## Connections to castles

- **Steep Dyck words and Motzkin paths.** A Dyck word is steep when it is nonempty and has no factor `x x̄ x`; the steep Dyck words of length `2n` are counted by the Motzkin number `M_{n−1}`, and by inversions by the q-Motzkin number `M_{n−1}(q)` ([[dyck-words](pages/dyck-words.md)]). The tower words of castles, read with `U = +1`, `R = 0`, `D = −1`, are the Motzkin paths with no factor `UD` and no factor `DU`, the cornerless Motzkin paths ([[deutsch-elizalde-2016-bargraphs-cornerless-motzkin](pages/deutsch-elizalde-2016-bargraphs-cornerless-motzkin.md)], [[castle-notation](pages/castle-notation.md)]).
- **q-Bessel quotients.** Counted by width, blocks and area, the castles have the generating function `N/M − 1`, with `N` and `M` q-series built from the q-Bessel series `J_0`, `J_1` of the parallelogram polyominoes ([[castle-q-bessel-closed-form](pages/castle-q-bessel-closed-form.md)]). Without area, the generating functions `P_k(x)` of the signed tower counts are rational ([[castle-counting-formula](pages/castle-counting-formula.md)]).
- **Parallelogram polyominoes** are one of the classes of [[column-convex-polygon-enumeration](pages/column-convex-polygon-enumeration.md)], whose Theorem 3.2 gives their generating function by left and right height, width, vertical half-perimeter and area as a quotient of the same series `J_1/J_0`.

## Key Takeaways

- Three q-analogs of the Motzkin numbers, interpreted by steep parallelogram polyominoes (a quotient of q-Bessel functions), steep Dyck words by inversions, and steep staircase polyominoes by area.[^2]
- Steep parallelogram polyominoes have no two consecutive horizontal steps on their South border.[^5]
- The derivations use object grammars and q-grammars.[^4]

## Entities & Concepts

- [[dyck-words](pages/dyck-words.md)] - the steep Dyck words, their grammar, and their count by the Motzkin numbers.
- [[motzkin-numbers](pages/motzkin-numbers.md)] - the numbers whose q-analogs the paper defines.
- [[permutation-inversions](pages/permutation-inversions.md)] - the inversion statistic, with the q-factorial as its generating function.
- [[generalized-dyck-grammar](pages/generalized-dyck-grammar.md)] - the grammar of tower words, a Dyck-type grammar with the letter `R`.
- [[column-convex-polygon-enumeration](pages/column-convex-polygon-enumeration.md)] - the parallelogram polyominoes by the add-a-column method.
- [[castle-q-bessel-closed-form](pages/castle-q-bessel-closed-form.md)] - castles by width, blocks and area through the parallelogram series.

## Relation to Other Wiki Pages

[[project-euler-502-solution](pages/project-euler-502-solution.md)] lists this paper as a reference. [[bousquet-melou-fedou-1995-convex-polyominoes](pages/bousquet-melou-fedou-1995-convex-polyominoes.md)] writes the generating function of all parallelogram polyominoes by width, height and area as the q-Bessel quotient `y J_1/J_0`, and the generating functions of the directed convex and convex polyominoes over the same denominator `J_0`.

## Footnotes

[^1]: https://api.crossref.org/works (query "Steep polyominoes, q-Motzkin numbers and q-Bessel functions", read 2026-10-16) - title, authors, *Discrete Mathematics* volume 189, pages 21-42, issued July 1998, DOI 10.1016/s0012-365x(97)00275-6.
[^2]: [[steep-polyominoes-q-motzkin-bessel](pages/steep-polyominoes-q-motzkin-bessel.md)] p.1 (Abstract) - "We introduce three definitions of the q-analogs of Motzkin numbers ... We relate the first class of q-numbers to the steep parallelogram polyominoes' generating function according to their width, perimeter and area ... this generating function is the quotient of two q-Bessel functions. The second class ... enumerates the inversions of steep Dyck words, while the third one counts the steep staircase polyominoes according to their area."
[^3]: [[steep-polyominoes-q-motzkin-bessel](pages/steep-polyominoes-q-motzkin-bessel.md)] p.1 §1 - "By using a method based on the study of path pairs in the plane, we prove that the generating function is the quotient of two q-Bessel functions."
[^4]: [[steep-polyominoes-q-motzkin-bessel](pages/steep-polyominoes-q-motzkin-bessel.md)] p.1 §1, p.2 - "we use object grammars to establish a relationship between q-Motzkin numbers ... and steep parallelogram polyominoes' generating function" and "steep Dyck words according to their length and inversion number by means of q-grammars."
[^5]: [[steep-polyominoes-q-motzkin-bessel](pages/steep-polyominoes-q-motzkin-bessel.md)] p.3 §2.1.1 - "A (lower) steep parallelogram polyomino is a parallelogram polyomino whose South border has no pairs of subsequent horizontal steps ... We denote the set of steep staircase polyominoes by SS."
