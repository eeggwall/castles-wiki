---
title: Convex polyomino
category: Concepts
summary: A polyomino that is both column-convex and row-convex - equivalently a run of overlapping column intervals whose tops weakly rise then fall and whose bottoms weakly fall then rise. The classical sub-families are named by which bounding-box corners they contain (Ferrers, stack, parallelogram, directed-convex); the wiki's convex castle is exactly the stack polyomino, and on any row-convex shape the castle block count is the height.
tags: [concept, polyomino, convex, column-convex, row-convex, ferrers, stack-polyomino, parallelogram-polyomino, directed-convex, q-analog]
sources: [column-convex-polygon-enumeration, counting-horizontally-convex-polyominoes, analytic-combinatorics-ch1-ogfs, bousquet-melou-fedou-1995-convex-polyominoes, klarner-rivest-1974-convex-n-ominoes]
created: 2026-09-22
updated: 2026-09-22
---

# Convex polyomino

## Definition

A polyomino is **convex** when it is both column-convex (every vertical line meets it in one segment) and row-convex (every horizontal line meets it in one segment).[^1] The two halves each have their own page: [[column-convex-polyomino](pages/column-convex-polyomino.md)] and [[horizontally-convex-polyomino](pages/horizontally-convex-polyomino.md)].

Read column by column, a convex polyomino of width `w` is a sequence of column intervals `[b_1, t_1], ..., [b_w, t_w]` with

- **overlap**: consecutive columns share at least one row (`b_{i+1} <= t_i` and `t_{i+1} >= b_i`), which is column-convexity plus connectedness;
- **tops unimodal**: `t_1 <= ... <= t_j >= ... >= t_w` for some `j`;
- **bottoms anti-unimodal**: `b_1 >= ... >= b_k <= ... <= b_w` for some `k`.

The last two conditions are row-convexity: a row with a gap would need a top to dip and rise again, or a bottom to rise and fall again. This column-sweep form is the one every count on [[convex-polyomino-by-area](pages/convex-polyomino-by-area.md)] is computed from.

A convex polyomino touches all four sides of its bounding box, and its perimeter equals the box perimeter `2(w + h)`: each boundary step can be pushed out to the box without changing the length. So counting convex polyominoes by perimeter means counting by `w + h`. The perimeter count is OEIS A005436, closed form `(2n + 11) 4^n - 4(2n + 1) C(2n, n)` up to an offset shift, as stated on the OEIS entry.[^2] Lin and Chang's generating function by width `x` and height `y` refines it. The formula is algebraic, with a `Delta^{-3/2}` term, `Delta = 1 - 2x - 2y - 2xy + x^2 + y^2`, and setting `x = y` recovers A005436. Once area is marked as well, the generating function becomes a quotient of q-series ([[bousquet-melou-fedou-1995-convex-polyominoes](pages/bousquet-melou-fedou-1995-convex-polyominoes.md)]).[^3]

## The corner taxonomy

The classical sub-families are distinguished by which corners of the bounding rectangle the polyomino must contain.[^4] The source says only that Ferrers, stack and parallelogram polyominoes are characterized by containing two or three bounding-box vertices. Bousquet-Mélou and Fédou's Fig. 2 marks the corners for three of the rows: parallelogram at bottom-left and top-right, directed convex at bottom-left, and Ferrers at three corners, drawn right-justified, so its third corner is the mirror image of the one in the table.[^5] The stack corners and the column-sweep conditions are this wiki's own reading. The conditions are checked by computation: each one reproduces the OEIS count for its family on [[convex-polyomino-by-area](pages/convex-polyomino-by-area.md)].

| family | corners contained | column-sweep condition |
|---|---|---|
| rectangle | all four | every column `[b, t]` the same |
| Ferrers diagram | three (bottom-left, bottom-right, top-left) | bottoms constant, tops weakly decreasing |
| stack polyomino | two (both bottom) | bottoms constant, tops unimodal |
| parallelogram (staircase) polyomino | two (bottom-left, top-right) | bottoms and tops both weakly increasing |
| directed convex | one (bottom-left) | bottoms weakly increasing, tops unimodal |
| convex | none required | tops unimodal, bottoms anti-unimodal |

These nest: rectangle ⊂ Ferrers ⊂ stack ⊂ directed convex ⊂ convex, and Ferrers ⊂ parallelogram ⊂ directed convex. Above convex sit column-convex (drop row-convexity) and then all polyominoes.

## Where the castle sits

- **A castle is a bar graph.** Every castle skyline has all its columns standing on a common base, so a castle is a column-convex polyomino with constant bottoms. By area every composition is a castle, and there are `2^{n-1}` of them ([[castle-by-area](pages/castle-by-area.md)]).
- **A convex castle is a stack polyomino.** Adding row-convexity to constant bottoms forces a unimodal skyline, which is the stack row of the table. That is the identity behind "convex castles by area = A001523" on [[convex-castle](pages/convex-castle.md)] and [[stack-polyomino-gf](pages/stack-polyomino-gf.md)].
- **So the general convex polyomino is a convex castle with a floating base.** Letting the bottoms follow their own anti-unimodal profile is the only change, and it moves the area count from subexponential (stacks) to exponential growth `2.30913...^n` (convex).
- **Two convex castles and a parallelogram.** Klarner and Rivest cut every convex polyomino along two rows into an upper stack, a middle parallelogram and a lower upside-down stack. Reassembling costs at most a factor `(n+2)^4`, so convex polyominoes grow exactly as fast as parallelograms.[^6] In castle terms, every convex polyomino is a parallelogram with a convex castle on top and another hung underneath.
- **Blocks become height.** A castle block is a maximal horizontal run of cells in one row. On any row-convex shape each row is one run, so the block count is the number of rows, the height. This is the general form of "a convex castle of height `h` has exactly `h` blocks" on [[convex-castle](pages/convex-castle.md)], and it is why the Project Euler 502 parity clause, carried over to convex polyominoes, becomes **height parity**.

## Related Concepts

- [[convex-polyomino-by-area](pages/convex-polyomino-by-area.md)] - every family in the table counted by area, split by height parity, with generating functions and growth constants.
- [[bousquet-melou-fedou-1995-convex-polyominoes](pages/bousquet-melou-fedou-1995-convex-polyominoes.md)] - the width-height-area generating function of the parallelogram, directed-convex and convex rows, solved as a [[q-differential-system](pages/q-differential-system.md)].
- [[column-convex-polyomino](pages/column-convex-polyomino.md)], [[horizontally-convex-polyomino](pages/horizontally-convex-polyomino.md)] - the two halves of the definition.
- [[convex-castle](pages/convex-castle.md)], [[stack-polyomino-gf](pages/stack-polyomino-gf.md)] - the stack row of the table under its castle name and its symbolic-method generating function.
- [[column-convex-polygon-enumeration](pages/column-convex-polygon-enumeration.md)] - Bousquet-Mélou's add-a-column method, which recovers the convex-polyomino generating functions.
- [[polyominoes](pages/polyominoes.md)] - the wider taxonomy.
- [[klarner-rivest-1974-convex-n-ominoes](pages/klarner-rivest-1974-convex-n-ominoes.md)] - the trisection and the growth constant `2.309138...`.

## Footnotes

[^1]: [[column-convex-polygon-enumeration](pages/column-convex-polygon-enumeration.md)] p.1 §1 - "A polyomino is said to be vertically convex (or column-convex) when its intersection with any vertical line is convex ... A polyomino is convex if it is both vertically and horizontally convex."
[^2]: https://oeis.org/A005436 (fetched 2026-09-22) - "Number of convex polygons of perimeter 2n on square lattice ... a(n) = (2*n+11)*4^n - 4*(2*n+1)*binomial(2*n,n) produces the terms (except the first two) with a different offset", (formula line signed N. J. A. Sloane, 2017). The entry's link list includes Delest and Viennot, "Algebraic languages and polyominoes enumeration" (1984); that paper was not read for this page.
[^3]: [[bousquet-melou-fedou-1995-convex-polyominoes](pages/bousquet-melou-fedou-1995-convex-polyominoes.md)] p.55 L117-135 - "the bivariate generating function on convex polyominoes for height and width, obtained by Lin and Chang [13] ... the formula of Lin and Chang refines the perimeter generating function given by Delest and Viennot [10]" (formula read from the page image). Its `x = y = t` expansion `t^2 + 2t^3 + 7t^4 + 28t^5 + 120t^6 + ...` matches A005436 through eight terms (verified by execution, 2026-09-22).
[^4]: [[column-convex-polygon-enumeration](pages/column-convex-polygon-enumeration.md)] p.2 §1 - "three very classical families of directed and convex polyominoes: the Ferrers diagrams, the stack polyominoes, and finally the parallelogram (or staircase) polyominoes ... characterized ... by the fact that two or three vertices of the minimal bounding rectangle ... must also belong to the polyomino."
[^5]: [[bousquet-melou-fedou-1995-convex-polyominoes](pages/bousquet-melou-fedou-1995-convex-polyominoes.md)] Fig. 2, p.55 L100-106 - "Different subclasses of convex polyominoes"; the marked corners are read from the page image.
[^6]: [[klarner-rivest-1974-convex-n-ominoes](pages/klarner-rivest-1974-convex-n-ominoes.md)] p.32-34 §2 [synthesis] L69-124 - "the trisection of a convex n-omino A is accomplished by cutting along the lowest level of A where the left boundary of A goes to the right and by cutting along the lowest level of A where the right boundary of A goes to the left"; "every convex n-omino splits into two stacks and one parallelogram"; (3) `c(n) <= (n+2)^4 p(n)` and (5).
