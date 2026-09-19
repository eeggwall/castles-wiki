---
title: Horizontally convex polyomino
category: Concepts
summary: A polyomino meeting every horizontal line in a single segment (or not at all); its count A001169 obeys a(n)=5a(n−1)−7a(n−2)+4a(n−3) — a convexity class to compare with the castle.
tags: [concept, polyomino, horizontally-convex, convexity, combinatorics]
sources: [counting-horizontally-convex-polyominoes]
created: 2026-09-13
updated: 2026-09-19
---

# Horizontally convex polyomino

## Description

A **horizontally convex polyomino** (horizontally convex (HC)-polyomino) is a polyomino — a finite edge-connected union of integer-positioned unit squares, taken up to translation — such that **every horizontal line meets it in a single line segment, or not at all**.[^1] Equivalently, each row of the shape is one contiguous run of cells; there are no horizontal gaps within a row.

The number of HC *n*-ominoes is `a(n)`, Online Encyclopedia of Integer Sequences (OEIS) **A001169**: `1, 2, 6, 19, 61, 196, 629, 2017, 6466, 20727, …`, and it satisfies the third-order linear recurrence `a(n) = 5a(n−1) − 7a(n−2) + 4a(n−3)` for `n ≥ 5`, with growth rate `v = 3.2055694304…` (the real root of `v³ − 5v² + 7v − 4`).[^2] See [[counting-horizontally-convex-polyominoes](pages/counting-horizontally-convex-polyominoes.md)] for Hickerson's 1-dimensional proof.

## Comparison with the castle

HC-polyominoes and [[castle-polyomino](pages/castle-polyomino.md)]s are two different convexity/shape families over the same lattice, and comparing them is one of the threads that links Project Euler 502 (PE 502) to the wider polyomino world:

- **The convexity differs.** HC = one contiguous segment *per row* (horizontal convexity). A castle's [[convex-castle](pages/convex-castle.md)] notion is instead a *skyline* condition (monotone rise to a plateau, then monotone descent) with a full-width base and same-row gaps allowed between stacked blocks. A castle is generally **not** horizontally convex — its rows may contain several separated blocks (the ≥1-unit gap rule) — so the two families overlap only partially.
- **Shared method.** Both are counted by introducing restricted-shape auxiliary functions and eliminating them into a recurrence: Hickerson's `b,c,d,e` for HC-polyominoes, and the tower counts `T`/`P` (with the [[binary-string-bijection](pages/binary-string-bijection.md)]) for castles.
- **Shared phenomenon.** A 2-D family collapsing to a short linear recurrence — the same C-finiteness the castle solution exploits via [[kitamasa](pages/kitamasa.md)] and [[berlekamp-massey](pages/berlekamp-massey.md)].

Precisely characterizing which castles are horizontally convex (and vice versa), and whether the castle's counting recurrences relate to `A001169`, is an open thread worth pursuing.

## Appearances in Sources

- [[counting-horizontally-convex-polyominoes](pages/counting-horizontally-convex-polyominoes.md)] — defines HC-polyominoes and proves the order-3 recurrence for their count.

## Related Concepts

- [[castle-polyomino](pages/castle-polyomino.md)] — the castle object, a different shape family on the same lattice.
- [[convex-castle](pages/convex-castle.md)] — the castle's own convexity class.
- [[column-convex-polygon-enumeration](pages/column-convex-polygon-enumeration.md)] — the broader column/row-convex polyomino literature.

## Footnotes

[^1]: [[counting-horizontally-convex-polyominoes](pages/counting-horizontally-convex-polyominoes.md)] p.1 §0 — "A polyomino P is horizontally convex if each horizontal line meets P in a single line segment, or not at all."
[^2]: [[counting-horizontally-convex-polyominoes](pages/counting-horizontally-convex-polyominoes.md)] p.1-2 §0 — the table "a(n) 1 2 6 19 61 196 629 2017 6466 20727 66441 212980", "a(n) = 5 a(n-1) - 7 a(n-2) + 4 a(n-3)" for n ≥ 5, and "v = 3.2055694304... the unique real root of v^3 - 5 v^2 + 7 v - 4 = 0"; OEIS A001169.
