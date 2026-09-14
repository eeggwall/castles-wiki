---
title: Kitamasa
category: Concepts
summary: The fast method for computing a single far-off term of a linear-recurrence sequence, as x^n mod the characteristic polynomial in O(D² log n); used to jump F's P(k,L) to large indices.
tags: [concept, algorithm, linear-recurrence, kitamasa, method]
sources: [project-euler-502-solution]
created: 2026-09-13
updated: 2026-09-13
---

# Kitamasa

## Description

**Kitamasa** is the method for computing a single, far-off term of a linear-recurrence sequence without stepping through all the intermediate terms. Given a recurrence of order *D*, extracting the term at index *n* is recast as computing `x^n mod charPoly` (reduction modulo the characteristic polynomial), which costs `O(D² log n)` — the `log n` coming from fast exponentiation.[^1] It is the natural partner of [[berlekamp-massey](pages/berlekamp-massey.md)]: Berlekamp–Massey *discovers* the minimal recurrence from sample terms; Kitamasa then *jumps* to any index of that recurrence.

In the castle solution Kitamasa appears on both [[castle-count-algorithms](pages/castle-count-algorithms.md)]:

- On the rational-function path (`h ≤ 15000`), extracting `[x^w] F_{h-1}(x)` for a *large* `w` is done by Kitamasa (`O(D² log w)`), which is how `F(10^12, 100)` is computed (`D ≈ 101`, `w = 10^12`).[^2]
- On the *k*-direction path (`h > 15000`), after Berlekamp–Massey finds the recurrence in *k*, Kitamasa jumps directly to index *k* to obtain `P(h−2,w)` and `P(h−1,w)`.[^3]

Kitamasa is also why the L-direction transfer-matrix approach was *not* used as the primary solve: raising the transfer matrix to a power costs `O(D³ log w)`, a factor of *D* worse than Kitamasa's `O(D² log w)` on the same recurrence.[^4]

**A thread to follow.** Kitamasa is a general tool for linear-recurrent and transfer-matrix–expressible enumeration; it connects the castle count to the wider machinery of holonomic/C-finite sequences and to polyomino recurrence methods, of the kind seen in the enumeration literature ([[counting-horizontally-convex-polyominoes](pages/counting-horizontally-convex-polyominoes.md)], [[column-convex-polygon-enumeration](pages/column-convex-polygon-enumeration.md)]). This page is a stub to be built out as those connections are traced.

## Appearances in Sources

- [[project-euler-502-solution](pages/project-euler-502-solution.md)] — uses Kitamasa as the large-index extractor on both computational paths, and contrasts its cost with the transfer-matrix approach.

## Related Concepts

- [[berlekamp-massey](pages/berlekamp-massey.md)] — finds the recurrence Kitamasa then jumps along.
- [[castle-count-algorithms](pages/castle-count-algorithms.md)] — the two paths where Kitamasa is used.
- [[castle-counting-formula](pages/castle-counting-formula.md)] — the `P(k,L)` term Kitamasa evaluates at large index.
- [[counting-horizontally-convex-polyominoes](pages/counting-horizontally-convex-polyominoes.md)] — a polyomino family whose count collapses to a short linear recurrence, the C-finite phenomenon Kitamasa exploits.

## Footnotes

[^1]: [[project-euler-502-solution](pages/project-euler-502-solution.md)] §"The rational-function path (h ≤ 15000)" L145 — "Kitamasa: turn the recurrence into 'compute x^w mod charPoly', then O(D^2 log w)."
[^2]: [[project-euler-502-solution](pages/project-euler-502-solution.md)] §"The rational-function path (h ≤ 15000)" L147-153 — "Direct wins when w ≤ D+1 ...; otherwise Kitamasa" and "F(10^12, 100): ... D ≈ 101, w = 10^12 gives Kitamasa."
[^3]: [[project-euler-502-solution](pages/project-euler-502-solution.md)] §"The k-direction Berlekamp-Massey path (h > 15000)" L159-161 — "Berlekamp-Massey finds the minimal linear recurrence. Kitamasa jumps directly to any index k."
[^4]: [[project-euler-502-solution](pages/project-euler-502-solution.md)] §"What was tried and did not work" L191 — "L-direction transfer matrix as the primary solve. Works, but slower ...: the matrix power costs O(D^3 log w) versus O(D^2 log w) for Kitamasa."
