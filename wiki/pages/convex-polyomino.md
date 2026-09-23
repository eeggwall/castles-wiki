---
title: Convex polyomino
category: Concepts
summary: A polyomino that is both column-convex and row-convex - equivalently a run of overlapping column intervals whose tops weakly rise then fall and whose bottoms weakly fall then rise. The classical sub-families are named by which bounding-box corners they contain (Ferrers, stack, parallelogram, directed-convex); the wiki's convex castle is exactly the stack polyomino, and on any row-convex shape the castle block count is the height.
tags: [concept, polyomino, convex, column-convex, row-convex, ferrers, stack-polyomino, parallelogram-polyomino, directed-convex, q-analog]
sources: [column-convex-polygon-enumeration, counting-horizontally-convex-polyominoes, analytic-combinatorics-ch1-ogfs, bender-1974-convex-n-ominoes]
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

A convex polyomino touches all four sides of its bounding box, and its perimeter equals the box perimeter `2(w + h)`: each boundary step can be pushed out to the box without changing the length. So counting convex polyominoes by perimeter means counting by `w + h`. The perimeter count is OEIS A005436, closed form `(2n + 11) 4^n - 4(2n + 1) C(2n, n)` up to an offset shift, as stated on the OEIS entry.[^2]

## The corner taxonomy

The classical sub-families are distinguished by which corners of the bounding rectangle the polyomino must contain.[^3] The source says only that Ferrers, stack and parallelogram polyominoes are characterized by containing two or three bounding-box vertices; the specific corners in the table, the directed-convex row, and the column-sweep conditions are this wiki's own reading. The conditions are checked by computation: each one reproduces the OEIS count for its family on [[convex-polyomino-by-area](pages/convex-polyomino-by-area.md)].

| family | corners contained | column-sweep condition |
|---|---|---|
| rectangle | all four | every column `[b, t]` the same |
| Ferrers diagram | three (bottom-left, bottom-right, top-left) | bottoms constant, tops weakly decreasing |
| stack polyomino | two (both bottom) | bottoms constant, tops unimodal |
| parallelogram (staircase) polyomino | two (bottom-left, top-right) | bottoms and tops both weakly increasing |
| directed convex | one (bottom-left) | bottoms weakly increasing, tops unimodal |
| convex | none required | tops unimodal, bottoms anti-unimodal |

These nest: rectangle ⊂ Ferrers ⊂ stack ⊂ directed convex ⊂ convex, and Ferrers ⊂ parallelogram ⊂ directed convex. Above convex sit column-convex (drop row-convexity) and then all polyominoes.

## Bender's three pieces

Bender reads a convex polyomino row by row and cuts it in two places: after the last row where the left end moves left, and before the first row where the right end moves right. The result is three pieces.[^4]

- **Bottom trapezoid.** Each row lies inside the row below it, so the columns stand on the bottom row with a unimodal skyline. This is a stack polyomino, the convex castle: at `y = 1`, Bender's trapezoid series is the A001523 stack series (own check through area 20).
- **Middle parallelogram.** Both row ends move weakly right. This piece can be empty; when it is nonempty it slants either northeast or northwest, and by symmetry the two cases count equally.
- **Top trapezoid.** The same as the bottom one, inverted.

The trapezoid series converges out to radius 1 and the parallelogram series only to `1/2.30914`, so all the exponential growth is in the middle piece.[^4] A typical convex polyomino of area `n` is therefore a parallelogram, a rod tilted 45 degrees whose height is asymptotically normal with mean `0.42088n` and whose rows average `2.37597` cells, capped at each end by a small stack.[^5] Bender's count is on [[bender-1974-convex-n-ominoes](pages/bender-1974-convex-n-ominoes.md)] and its growth constant on [[convex-polyomino-by-area](pages/convex-polyomino-by-area.md)].

## Where the castle sits

- **A castle is a bar graph.** Every castle skyline has all its columns standing on a common base, so a castle is a column-convex polyomino with constant bottoms. By area every composition is a castle, and there are `2^{n-1}` of them ([[castle-by-area](pages/castle-by-area.md)]).
- **A convex castle is a stack polyomino.** Adding row-convexity to constant bottoms forces a unimodal skyline, which is the stack row of the table. That is the identity behind "convex castles by area = A001523" on [[convex-castle](pages/convex-castle.md)] and [[stack-polyomino-gf](pages/stack-polyomino-gf.md)].
- **So the general convex polyomino is a convex castle with a floating base.** Letting the bottoms follow their own anti-unimodal profile is the only change, and it moves the area count from subexponential (stacks) to exponential growth `2.30913...^n` (convex). Bender's pieces show where the growth comes from: a floating base lets a parallelogram sit between an upright stack and an inverted one, and the exponential growth is all in the parallelogram.
- **Blocks become height.** A castle block is a maximal horizontal run of cells in one row. On any row-convex shape each row is one run, so the block count is the number of rows, the height. This is the general form of "a convex castle of height `h` has exactly `h` blocks" on [[convex-castle](pages/convex-castle.md)], and it is why the Project Euler 502 parity clause, carried over to convex polyominoes, becomes **height parity**.

## Related Concepts

- [[convex-polyomino-by-area](pages/convex-polyomino-by-area.md)] - every family in the table counted by area, split by height parity, with generating functions and growth constants.
- [[column-convex-polyomino](pages/column-convex-polyomino.md)], [[horizontally-convex-polyomino](pages/horizontally-convex-polyomino.md)] - the two halves of the definition.
- [[convex-castle](pages/convex-castle.md)], [[stack-polyomino-gf](pages/stack-polyomino-gf.md)] - the stack row of the table under its castle name and its symbolic-method generating function.
- [[column-convex-polygon-enumeration](pages/column-convex-polygon-enumeration.md)] - Bousquet-Mélou's add-a-column method, which recovers the convex-polyomino generating functions.
- [[polyominoes](pages/polyominoes.md)] - the wider taxonomy.
- [[bender-1974-convex-n-ominoes](pages/bender-1974-convex-n-ominoes.md)] - the trapezoid + parallelogram + trapezoid split, the growth constant, and the typical 45-degree rod shape.

## Footnotes

[^1]: [[column-convex-polygon-enumeration](pages/column-convex-polygon-enumeration.md)] p.1 §1 - "A polyomino is said to be vertically convex (or column-convex) when its intersection with any vertical line is convex ... A polyomino is convex if it is both vertically and horizontally convex."
[^2]: https://oeis.org/A005436 (fetched 2026-09-22) - "Number of convex polygons of perimeter 2n on square lattice ... a(n) = (2*n+11)*4^n - 4*(2*n+1)*binomial(2*n,n) produces the terms (except the first two) with a different offset", (formula line signed N. J. A. Sloane, 2017). The entry's link list includes Delest and Viennot, "Algebraic languages and polyominoes enumeration" (1984); that paper was not read for this page.
[^3]: [[column-convex-polygon-enumeration](pages/column-convex-polygon-enumeration.md)] p.2 §1 - "three very classical families of directed and convex polyominoes: the Ferrers diagrams, the stack polyominoes, and finally the parallelogram (or staircase) polyominoes ... characterized ... by the fact that two or three vertices of the minimal bounding rectangle ... must also belong to the polyomino."
[^4]: [[bender-1974-convex-n-ominoes](pages/bender-1974-convex-n-ominoes.md)] pp.220 §2, 222-223 §4 and Fig. 1 [synthesis] - trapezoids "l_i ≤ l_{i+1} and r_i ≥ r_{i+1}", parallelograms "l_i ≤ l_{i+1} < r_i ≤ r_{i+1}"; I is "the maximum i such that l_i > l_{i+1}", J "the minimum j such that r_{j−1} > r_j", and the three parts are the rows "i ≤ I, I < i < J, i ≥ J"; "Since T(x, 1) has radius of convergence 1 which exceeds r, it follows that c(n) ~ 2c*(n)."
[^5]: [[bender-1974-convex-n-ominoes](pages/bender-1974-convex-n-ominoes.md)] p.219 abstract, pp.224-225 §5 - "most convex n-ominoes resemble rods tilted 45° from the vertical with horizontal (and vertical) thickness roughly equal to 2.37597"; "a normal distribution with mean μ_n ~ 0.42088n and variance σ_n^2 ~ 0.20806n"; §6: "The ideas in the previous section still apply ... All the results are the same except for the length of the bases."
