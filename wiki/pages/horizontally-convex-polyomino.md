---
title: Horizontally convex polyomino
category: Concepts
summary: A polyomino meeting every horizontal line in a single segment (or not at all); its count A001169 obeys a(n)=5a(n−1)−7a(n−2)+4a(n−3) — a convexity class to compare with the castle.
tags: [concept, polyomino, horizontally-convex, convexity, combinatorics]
sources: [counting-horizontally-convex-polyominoes, klarner-rivest-1974-convex-n-ominoes]
created: 2026-09-13
updated: 2026-09-28
---

# Horizontally convex polyomino

## Description

A **horizontally convex polyomino** (horizontally convex (HC)-polyomino) is a polyomino — a finite edge-connected union of integer-positioned unit squares, taken up to translation — such that **every horizontal line meets it in a single line segment, or not at all**.[^1] Equivalently, each row of the shape is one contiguous run of cells; there are no horizontal gaps within a row.

The number of HC *n*-ominoes is `a(n)`, Online Encyclopedia of Integer Sequences (OEIS) **A001169**: `1, 2, 6, 19, 61, 196, 629, 2017, 6466, 20727, …`; it satisfies a third-order linear recurrence with growth rate `v ≈ 3.2056` - the closed form of the recurrence, the growth-rate cubic, and Hickerson's 1-dimensional proof (auxiliaries `b`, `c`, `d`, `e` eliminated into a single relation) are all on the source page [[counting-horizontally-convex-polyominoes](pages/counting-horizontally-convex-polyominoes.md)].[^2]

## Comparison with the castle

HC-polyominoes and [[castle-polyomino](pages/castle-polyomino.md)]s are two different convexity/shape families over the same lattice:

- **The convexity differs.** HC = one contiguous segment *per row* (horizontal convexity). A castle's [[convex-castle](pages/convex-castle.md)] notion is instead a *skyline* condition (monotone rise to a plateau, then monotone descent) with a full-width base and same-row gaps allowed between stacked blocks. A castle is generally **not** horizontally convex — its rows may contain several separated blocks (the ≥1-unit gap rule). The castles that are horizontally convex are exactly the convex castles: every row is one segment exactly when the skyline is unimodal.
- **Auxiliary counts.** Both counts go through auxiliary counts: Hickerson's `b,c,d,e` for HC-polyominoes, and the tower counts `T`/`P` (with the [[binary-string-bijection](pages/binary-string-bijection.md)]) for castles.
- **Shared phenomenon.** A 2-D family collapsing to a short linear recurrence — the same C-finiteness the castle solution exploits via [[kitamasa](pages/kitamasa.md)] and [[berlekamp-massey](pages/berlekamp-massey.md)].

Against `A001169`, [[castle-add-a-column-equation](pages/castle-add-a-column-equation.md)] compares the two column kernels: the castle keeps 1 of Temperley's `k+l−1` placements, a rank-1 area kernel (castles by area are `2^(n−1)`), against the rank-2 kernel behind Hickerson's order-3 recurrence.

## Appearances in Sources

- [[counting-horizontally-convex-polyominoes](pages/counting-horizontally-convex-polyominoes.md)] — defines HC-polyominoes and proves the order-3 recurrence for their count.
- [[klarner-rivest-1974-convex-n-ominoes](pages/klarner-rivest-1974-convex-n-ominoes.md)] - uses the row-convex count, with generating-function denominator `1 - 5x + 7x^2 - 4x^3` and growth `3.20...`, as its comparison family against `2.309...` for convex polyominoes.

## Related Concepts

- [[castle-polyomino](pages/castle-polyomino.md)] — the castle object, a different shape family on the same lattice.
- [[convex-castle](pages/convex-castle.md)] — the castle's own convexity class.
- [[column-convex-polygon-enumeration](pages/column-convex-polygon-enumeration.md)] — the broader column/row-convex polyomino literature.
- [[tree-castle-by-area](pages/tree-castle-by-area.md)] — low-order C-finite castle sequences by area (A000930, A006498, A000570), for comparison with the A001169 recurrence.
- [[convex-polyomino-by-area](pages/convex-polyomino-by-area.md)] - A001169 is also the column-convex count by area (rotating a polyomino 90 degrees turns its rows into columns and keeps its area, so it is a one-to-one map from row-convex to column-convex polyominoes of the same area), the envelope of every castle area count; the ladder of convex sub-families sits below it.

## Footnotes

[^1]: [[counting-horizontally-convex-polyominoes](pages/counting-horizontally-convex-polyominoes.md)] p.1 §0 — "A polyomino P is horizontally convex if each horizontal line meets P in a single line segment, or not at all."
[^2]: [[counting-horizontally-convex-polyominoes](pages/counting-horizontally-convex-polyominoes.md)] p.1-2 §0 — the table "a(n) 1 2 6 19 61 196 629 2017 6466 20727 66441 212980", "a(n) = 5 a(n-1) - 7 a(n-2) + 4 a(n-3)" for n ≥ 5, and "v = 3.2055694304... the unique real root of v^3 - 5 v^2 + 7 v - 4 = 0"; OEIS A001169.
