---
title: Column-convex polyomino
category: Concepts
summary: A polyomino whose intersection with every vertical line is one segment, so that each column is one run of cells; A001169 by area. Its classes are enumerated by gluing columns one at a time (the add-a-column method of Bousquet-Mélou 1996), and some sub-families directly by the symbolic method, as the stack polyominoes in Example I.8 of Analytic Combinatorics. The castles are the column-convex polyominoes whose columns all start on row 1.
tags: [concept, polyomino, column-convex, convexity, combinatorics, symbolic-method]
sources: [column-convex-polygon-enumeration, analytic-combinatorics-ch1-ogfs]
created: 2026-09-13
updated: 2026-10-16
---

# Column-convex polyomino

## Description

A polyomino is **column-convex**, or vertically convex, when its intersection with every vertical line is one segment: each column is one run of cells, with no vertical gap. It is convex when it is column-convex and row-convex ([[convex-polyomino](pages/convex-polyomino.md)], [[horizontally-convex-polyomino](pages/horizontally-convex-polyomino.md)]).[^1] Every column-convex polyomino is a polygon, a polyomino without holes, since a hole would put a gap in some column.[^1] Column by column, a column-convex polyomino of width `w` is a sequence of column intervals `[b_1, t_1], …, [b_w, t_w]` in which consecutive columns share a row. For example, the columns `[0, 2]`, `[2, 2]`, `[0, 2]` form an arch, column-convex but not row-convex.

By area, the column-convex polyominoes are A001169, `1, 2, 6, 19, 61, 196, …` for `n = 1, 2, …`. Turning a polyomino a quarter turn exchanges rows and columns and keeps its area, so the same sequence counts the horizontally convex polyominoes, which Hickerson's recurrence `a(n) = 5a(n−1) − 7a(n−2) + 4a(n−3)` (`n ≥ 5`) counts ([[counting-horizontally-convex-polyominoes](pages/counting-horizontally-convex-polyominoes.md)]).[^2]

Bousquet-Mélou names three classical families of directed and convex polyominoes, the Ferrers diagrams, the stack polyominoes and the parallelogram (or staircase) polyominoes; the enumeration results for them and for the larger column-convex classes are on [[column-convex-polygon-enumeration](pages/column-convex-polygon-enumeration.md)].[^3]

**The add-a-column method.** A column-convex polyomino is built by gluing columns one at a time, in a way that depends on the class. Bousquet-Mélou turns each way of gluing a new column into a term of a linear q-equation for the generating function, which records the heights of the first and last columns, the width, the vertical half-perimeter and the area; the paper calls the gluing idea the "Temperley methodology".[^4]

**The symbolic method.** Some sub-families have a direct specification ([[symbolic-method](pages/symbolic-method.md)]). A stack polyomino is the diagram of a composition `x_1 ≤ ⋯ ≤ x_j ≥ ⋯ ≥ x_ℓ`. Flajolet and Sedgewick split it at its first column of maximal height `k` into a partition into parts less than `k`, that column, and a partition into parts at most `k`, which gives the generating function `Σ_{k≥1} z^k/(1 − z^k) · 1/((1 − z)(1 − z²)⋯(1 − z^{k−1}))²`, the stack series A001523 ([[stack-polyomino-gf](pages/stack-polyomino-gf.md)]).[^5]

## Relation to the castle

- Every castle is column-convex: each column is a stack of cells from row 1 up. The castles are exactly the column-convex polyominoes whose columns all start on row 1, the bargraphs ([[castle-polyomino](pages/castle-polyomino.md)]). The [[polyominoes](pages/polyominoes.md)] source places castles among the column-convex polyominoes.
- Gluing a column to a castle gives an add-a-column equation without a derivative term, which Bousquet-Mélou's Lemma 2.3 solves ([[castle-add-a-column-equation](pages/castle-add-a-column-equation.md)]). The tower count `T(k, L) = (k + 1)^L` is proved row by row instead, through the binary strings of the first row ([[binary-string-bijection](pages/binary-string-bijection.md)]).
- The castles that are stack polyominoes are the convex castles ([[convex-castle](pages/convex-castle.md)]). The castles that are parallelogram polyominoes are those with weakly increasing skylines, the Ferrers diagrams reflected left to right ([[castle-add-a-column-equation](pages/castle-add-a-column-equation.md)]).

## Appearances in Sources

- [[column-convex-polygon-enumeration](pages/column-convex-polygon-enumeration.md)] - the definition of column-convexity, the three classical families, and the add-a-column method.
- [[analytic-combinatorics-ch1-ogfs](pages/analytic-combinatorics-ch1-ogfs.md)] - Example I.8 (pp. 45-46): the stack polyominoes by the symbolic method.

## Related Concepts

- [[castle-polyomino](pages/castle-polyomino.md)] - the castles, the column-convex polyominoes with every column starting on row 1.
- [[horizontally-convex-polyomino](pages/horizontally-convex-polyomino.md)] - the row-convex polyominoes, also A001169 by area.
- [[convex-polyomino](pages/convex-polyomino.md)] - column-convex and row-convex polyominoes, and their sub-families by bounding-box corners; [[convex-polyomino-by-area](pages/convex-polyomino-by-area.md)] counts them by area.
- [[convex-castle](pages/convex-castle.md)] - the castles that are row-convex, the stack polyominoes.
- [[stack-polyomino-gf](pages/stack-polyomino-gf.md)] - the generating function of stack polyominoes by area.
- [[symbolic-method](pages/symbolic-method.md)] - the specification method of Analytic Combinatorics.

## Footnotes

[^1]: [[column-convex-polygon-enumeration](pages/column-convex-polygon-enumeration.md)] p.1 §1 L90-95 - "A polyomino is said to be vertically convex (or column-convex) when its intersection with any vertical line is convex (Fig. 2). We can define similarly a notion of horizontal (or row-) convexity. A polyomino is convex if it is both vertically and horizontally convex", "Note that any column-convex polyomino is actually a polygon, so we can use indifferently the word 'polyomino' or 'polygon' in this case."
[^2]: https://oeis.org/A001169 (read 2026-10-16) - "Number of board-pile polyominoes with n cells", offset 1, "a(n) = 5*a(n-1) - 7*a(n-2) + 4*a(n-3) for n >= 5", with a link to Hickerson's paper; the column-convex polyominoes of area at most 11 enumerated by column intervals give `1, 2, 6, 19, 61, 196, 629, 2017, 6466, 20727, 66441` (Python 3.11, 2026-10-16).
[^3]: [[column-convex-polygon-enumeration](pages/column-convex-polygon-enumeration.md)] p.2 §1 L131-132 - "Let us also mention three very classical families of directed and convex polyominoes: Ferrers diagrams, stack polyominoes, and parallelogram (or staircase) polyominoes."
[^4]: [[column-convex-polygon-enumeration](pages/column-convex-polygon-enumeration.md)] p.3 §2 L180-184 - "a column-convex polyomino can be obtained by successively gluing columns, in a way that depends on the class of polygons one studies. This idea is sometimes known as 'Temperley methodology' in statistical physics".
[^5]: [[analytic-combinatorics-ch1-ogfs](pages/analytic-combinatorics-ch1-ogfs.md)] Example I.8 "The Durfee square of partitions and stack polyominoes" pp.45-46 - "A stack polyomino is the diagram of a composition such that for some j, ℓ, one has 1 ≤ x_1 ≤ x_2 ≤ ··· ≤ x_j ≥ x_{j+1} ≥ ··· ≥ x_ℓ ≥ 1", with the decomposition `P{1,…,k−1} × Z^k × P{1,…,k}` and the OGF (read in the PDF, book pp. 45-46).
