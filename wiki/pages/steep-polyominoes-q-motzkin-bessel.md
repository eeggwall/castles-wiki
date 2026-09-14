---
title: "Steep Polyominoes, q-Motzkin Numbers and q-Bessel Functions (Barcucci et al.)"
category: Sources
summary: Barcucci–Del Lungo–Fédou–Pinzani connect steep parallelogram/staircase polyominoes and steep Dyck words to three q-Motzkin analogs, one a ratio of q-Bessel functions, via object grammars.
tags: [paper, polyomino, dyck-words, motzkin, generating-functions, q-analog, source]
sources: [steep-polyominoes-q-motzkin-bessel]
created: 2026-09-13
updated: 2026-09-13
---

# Steep Polyominoes, q-Motzkin Numbers and q-Bessel Functions (Barcucci et al.)

**Source:** `assets/PolyominosMotzkinBessel.pdf` (E. Barcucci, A. Del Lungo, J. M. Fédou, R. Pinzani, *Steep polyominoes, q-Motzkin numbers and q-Bessel functions*)
**Date ingested:** 2026-09-13
**Type:** paper (PDF, 21 pp.)

## Summary

The paper introduces **three q-analogs of the Motzkin numbers** and gives each a combinatorial interpretation, illustrating counting and q-counting techniques.[^1] The three interpretations tie Motzkin q-numbers to *steep* polyomino families and to Dyck words:[^1]

- The **first** q-Motzkin class equals the generating function of **steep parallelogram polyominoes** by width, perimeter and area — shown (via a path-pairs-in-the-plane method) to be the **quotient of two q-Bessel functions**.[^1][^2]
- The **second** class enumerates the **inversions of steep Dyck words** (established with q-grammars / object grammars).[^1][^3]
- The **third** class counts **steep staircase polyominoes** by area.[^1]

The steepness conditions are geometric run constraints. A **(lower) steep parallelogram polyomino** is a parallelogram polyomino whose south border has **no two consecutive horizontal steps**; the **steep staircase polyominoes** (set `SS`) are defined analogously.[^4] Object grammars — a grammar formalism over the combinatorial objects — are the engine relating these families to the q-numbers.[^3]

## Why it matters for PE 502

This paper sits on the intersection of three of the castle's central threads — Dyck words, generating functions, and polyomino counting — and points to a richer analytic world:

- **Steep Dyck words ↔ the castle's Dyck grammar.** The castle's [[generalized-dyck-grammar](pages/generalized-dyck-grammar.md)] is a three-letter Dyck grammar with a "no `UD` / no `DU`" run constraint; the "no two consecutive horizontal steps" steepness condition here is the same *flavor* of run restriction on a Dyck-type word. That these steep-Dyck objects carry a **Motzkin** (three-step-type) statistic is a strong hint at where the castle's U/R/D (also three step types) connects.
- **Object grammars = the grammar method, matured.** The paper's use of object/q-grammars to derive generating functions is the sophisticated version of the castle's "recast the rules as a grammar, read off the GF" move ([[generating-functions](pages/generating-functions.md)]).
- **q-Bessel / q-Motzkin as the analytic target.** The castle's `P(k,L)` generating functions are rational; the appearance of **q-Bessel-function ratios** here suggests what richer generating functions look like when area (a second grading variable, the `q`) is tracked — a natural next question for a q-graded castle count.
- **Parallelogram / staircase polyominoes** are exactly the [[column-convex-polygon-enumeration](pages/column-convex-polygon-enumeration.md)] classical families, seen here through the Dyck/Motzkin lens — a cross-link between the two ingested papers.

## Key Takeaways

- Three q-Motzkin analogs, interpreted via steep parallelogram polyominoes (a **q-Bessel ratio** GF), inversions of **steep Dyck words**, and steep staircase polyominoes by area.[^1]
- **Steepness** = no two consecutive horizontal steps on the relevant border — a run constraint on a Dyck-type word.[^4]
- **Object/q-grammars** are the derivation tool, the mature form of the castle's grammar-to-generating-function method.[^3]
- Connects **Dyck words, Motzkin numbers, generating functions, and polyomino area** — the crossroads of several PE 502 threads.

## Entities & Concepts

- [[generalized-dyck-grammar](pages/generalized-dyck-grammar.md)] — the castle's Dyck-type grammar; steep Dyck words are the closest external analogue.
- [[dyck-words](pages/dyck-words.md)] — the steep-Dyck-word grammar and the steep-length-2n = (n−1)th Motzkin result.
- [[generating-functions](pages/generating-functions.md)] — the object-grammar method here is its mature form.
- [[column-convex-polygon-enumeration](pages/column-convex-polygon-enumeration.md)] — where the parallelogram/staircase families are enumerated by the add-a-column method.

## Relation to Other Wiki Pages

Cited as a reference on [[project-euler-502-solution](pages/project-euler-502-solution.md)]. It is the thread that carries the castle's Dyck-word and generating-function structure into the world of Motzkin numbers, q-analogs, and q-Bessel functions — a direction for a possibly richer, area-graded castle enumeration, and a bridge to the parallelogram/staircase families of [[column-convex-polygon-enumeration](pages/column-convex-polygon-enumeration.md)].

## Footnotes

[^1]: [[steep-polyominoes-q-motzkin-bessel](pages/steep-polyominoes-q-motzkin-bessel.md)] p.1 (Abstract) — "We introduce three definitions of the q-analogs of Motzkin numbers ... We relate the first class of q-numbers to the steep parallelogram polyominoes' generating function according to their width, perimeter and area ... this generating function is the quotient of two q-Bessel functions. The second class ... enumerates the inversions of steep Dyck words, while the third one counts the steep staircase polyominoes according to their area."
[^2]: [[steep-polyominoes-q-motzkin-bessel](pages/steep-polyominoes-q-motzkin-bessel.md)] p.1 §1 — "By using a method based on the study of path pairs in the plane, we prove that the generating function is the quotient of two q-Bessel functions."
[^3]: [[steep-polyominoes-q-motzkin-bessel](pages/steep-polyominoes-q-motzkin-bessel.md)] p.1 §1, p.2 — "we use object grammars to establish a relationship between q-Motzkin numbers ... and steep parallelogram polyominoes' generating function" and "steep Dyck words according to their length and inversion number by means of q-grammars."
[^4]: [[steep-polyominoes-q-motzkin-bessel](pages/steep-polyominoes-q-motzkin-bessel.md)] p.3 §2.1.1 — "A (lower) steep parallelogram polyomino is a parallelogram polyomino whose South border has no pairs of subsequent horizontal steps ... We denote the set of steep staircase polyominoes by SS."
