---
title: Horizontally convex polyomino
category: Concepts
summary: A polyomino that every horizontal line meets in one segment or not at all, so that each row is one run of cells. By area these are A001169, 1, 2, 6, 19, 61, …, with a(n) = 5a(n−1) − 7a(n−2) + 4a(n−3) for n ≥ 5 (Hickerson) and growth constant 3.2055694304…; a quarter turn makes them the column-convex polyominoes, which contain every castle. The castles that are horizontally convex are exactly the convex castles.
tags: [concept, polyomino, horizontally-convex, convexity, combinatorics]
sources: [counting-horizontally-convex-polyominoes, klarner-rivest-1974-convex-n-ominoes]
created: 2026-09-13
updated: 2026-10-16
---

# Horizontally convex polyomino

## Description

A polyomino, a finite edge-connected union of unit squares with integer vertices taken up to translation, is **horizontally convex** when every horizontal line meets it in one segment or not at all.[^1] Each row is then one run of cells. All 19 polyominoes of area 4 are horizontally convex; of the 63 of area 5, the U-pentominoes opening up and opening down are not, since the row of their two arms has a gap, which leaves 61.[^2]

The number `a(n)` of horizontally convex polyominoes of area `n` is A001169: `1, 2, 6, 19, 61, 196, 629, 2017, 6466, 20727, …` for `n = 1, 2, …`. Hickerson proves `a(n) = 5a(n−1) − 7a(n−2) + 4a(n−3)` for `n ≥ 5`, so `a(n) ~ u·v^n` with `v = 3.2055694304…` the real root of `v³ − 5v² + 7v − 4`; the auxiliary counts of the proof are on [[counting-horizontally-convex-polyominoes](pages/counting-horizontally-convex-polyominoes.md)].[^3] A quarter turn exchanges rows and columns and keeps the area, so A001169 also counts the column-convex polyominoes, under the OEIS name "board-pile polyominoes" ([[column-convex-polyomino](pages/column-convex-polyomino.md)]).[^4]

## Castles

- **Which castles are horizontally convex.** A castle's row `r` is one run exactly when no column below height `r` lies between two columns of height at least `r`. So a castle is horizontally convex exactly when its skyline is unimodal: these are the convex castles ([[convex-castle](pages/convex-castle.md)]), the stack polyominoes. The castle `(2, 1, 2)`, whose row 2 has two blocks, is not.[^5]
- **An upper bound by area.** Every castle is column-convex, so the `2^{n−1}` castles of area `n` are at most A001169(n) ([[castle-by-area](pages/castle-by-area.md)]).
- **The two column rules.** Gluing a column of height `l` after one of height `k` can be done in `k + l − 1` ways for column-convex polyominoes and in one way for castles. [[castle-add-a-column-equation](pages/castle-add-a-column-equation.md)] shows that the first kernel has rank 2, which gives the recurrence of order 3, and the second rank 1, which gives `2^{n−1}`.

## Appearances in Sources

- [[counting-horizontally-convex-polyominoes](pages/counting-horizontally-convex-polyominoes.md)] - the definition, the table of `a(n)`, and the proof of the recurrence of order 3.
- [[klarner-rivest-1974-convex-n-ominoes](pages/klarner-rivest-1974-convex-n-ominoes.md)] - the row-convex count `b(n)`, growth constant `3.20…`, as the comparison family for the convex count, whose growth constant is `2.309…`. The transcription of its generating function (1) prints the denominator `1 − 4x + 7x² − 5x³`, which does not give these counts; the generating function is `x(1 − x)^3/(1 − 5x + 7x² − 4x³)`.[^4]

## Related Concepts

- [[castle-polyomino](pages/castle-polyomino.md)] - the castles, which are column-convex and in general not horizontally convex.
- [[convex-castle](pages/convex-castle.md)] - the castles that are horizontally convex.
- [[column-convex-polyomino](pages/column-convex-polyomino.md)] - the column-convex polyominoes, the quarter-turn image of this family.
- [[convex-polyomino](pages/convex-polyomino.md)] - the polyominoes that are both horizontally and column-convex; [[convex-polyomino-by-area](pages/convex-polyomino-by-area.md)] counts their sub-families by area.
- [[column-convex-polygon-enumeration](pages/column-convex-polygon-enumeration.md)] - Bousquet-Mélou's method for column-convex classes.
- [[tree-castle-by-area](pages/tree-castle-by-area.md)] - the tree skylines by area (A000930, A006498, A000570), other linear recurrences by area.

## Footnotes

[^1]: [[counting-horizontally-convex-polyominoes](pages/counting-horizontally-convex-polyominoes.md)] p.1 §0 - "A polyomino P is horizontally convex if each horizontal line meets P in a single line segment, or not at all."
[^2]: Verified by execution (Python 3.11, 2026-10-16): the fixed polyominoes of area 1 to 5 number 1, 2, 6, 19, 63, and the horizontally convex ones 1, 2, 6, 19, 61.
[^3]: [[counting-horizontally-convex-polyominoes](pages/counting-horizontally-convex-polyominoes.md)] p.1-2 §0 - the table "a(n) 1 2 6 19 61 196 629 2017 6466 20727 66441 212980", "a(n) = 5 a(n-1) - 7 a(n-2) + 4 a(n-3)" for n ≥ 5, and "v = 3.2055694304... the unique real root of v^3 - 5 v^2 + 7 v - 4 = 0" (the paper's PDF is not on disk; quoted from its source page).
[^4]: https://oeis.org/A001169 (read 2026-10-16) - "Number of board-pile polyominoes with n cells", "G.f.: x*(1-x)^3/(1 - 5*x + 7*x^2 - 4*x^3)", offset 1; [[klarner-rivest-1974-convex-n-ominoes](pages/klarner-rivest-1974-convex-n-ominoes.md)] p.32 §1 L53-58 - "(1) x(1-x)^3 / (1 - 4x + 7x^2 - 5x^3) = sum_{n>=1} b(n) x^n ... beta = 3.20...". Expanding the OEIS generating function gives `1, 2, 6, 19, 61, 196, …`; the transcribed one gives `1, 1, 0, −3, …` (Python 3.11, 2026-10-16).
[^5]: Verified by execution (Python 3.11, 2026-10-16): for every skyline with `w ≤ 6` and `h ≤ 5`, every row is one run exactly when the skyline is unimodal.
