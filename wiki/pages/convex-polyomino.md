---
title: Convex polyomino
category: Concepts
summary: A polyomino that is column-convex and row-convex - a sequence of overlapping column intervals whose tops are unimodal and whose bottoms are anti-unimodal - with perimeter 2(w + h), the perimeter of its bounding box. The classical sub-families (Ferrers diagrams, stack, parallelogram and directed convex polyominoes) are told apart by the corners of the bounding box they contain. The stack polyominoes are the convex castles, and on any row-convex polyomino the castle block count is the height.
tags: [concept, polyomino, convex, column-convex, row-convex, ferrers, stack-polyomino, parallelogram-polyomino, directed-convex, q-analog]
sources: [column-convex-polygon-enumeration, bousquet-melou-fedou-1995-convex-polyominoes, klarner-rivest-1974-convex-n-ominoes, bender-1974-convex-n-ominoes, algebraic-languages-and-polyominoes-enumeration]
created: 2026-09-22
updated: 2026-10-16
---

# Convex polyomino

## Definition

A polyomino is **convex** when it is column-convex, every vertical line meeting it in one segment, and row-convex, every horizontal line meeting it in one segment.[^1] The two conditions have their own pages, [[column-convex-polyomino](pages/column-convex-polyomino.md)] and [[horizontally-convex-polyomino](pages/horizontally-convex-polyomino.md)].

Column by column, a column-convex polyomino of width `w` is a sequence of column intervals `[b_1, t_1], …, [b_w, t_w]`, column `i` filling the rows `b_i` to `t_i`, in which consecutive columns share a row: `b_{i+1} ≤ t_i` and `t_{i+1} ≥ b_i`. It is row-convex exactly when

- the tops are **unimodal**: `t_1 ≤ ⋯ ≤ t_j ≥ ⋯ ≥ t_w` for some `j`, and
- the bottoms are **anti-unimodal**: `b_1 ≥ ⋯ ≥ b_k ≤ ⋯ ≤ b_w` for some `k`.

*Proof.* If both conditions hold, the columns that contain row `r` are those with `t_i ≥ r` and `b_i ≤ r`, the intersection of two intervals of indices, so row `r` is one segment. Conversely, suppose `i < j < k` with `t_j < t_i` and `t_j < t_k`, and let `r = t_j + 1`. Let `i'` be the last column before `j` with `t_{i'} ≥ r` and `k'` the first column after `j` with `t_{k'} ≥ r`. The column after `i'` has its top below `r` and shares a row with column `i'`, so `b_{i'} < r` and column `i'` contains row `r`; so does column `k'`, and column `j` does not, so row `r` has a gap. The bottoms are the same argument turned upside down.

*Example.* The polyomino with columns `[1, 2]`, `[0, 2]`, `[0, 1]` has tops `2, 2, 1` and bottoms `1, 0, 0`: it is convex, with 7 cells in a `3 × 3` box. The polyomino with columns `[0, 2]`, `[2, 2]`, `[0, 2]`, an arch, is column-convex, but its bottoms `0, 2, 0` are not anti-unimodal, and its rows 0 and 1 each have a gap in the middle column.

The counts on [[convex-polyomino-by-area](pages/convex-polyomino-by-area.md)] are computed from this column form. For area at most 11 it reproduces the convex polyominoes A067675, and the conditions agree with a direct row-by-row test on every column-convex polyomino.[^2]

**Perimeter.** Column-convexity gives each column exactly two horizontal boundary edges, its top and its bottom, and row-convexity gives each row two vertical ones, so a convex polyomino of width `w` and height `h` has perimeter `2(w + h)`, the perimeter of its bounding box.[^3] Counting by perimeter is therefore counting by `w + h`. The convex polyominoes of perimeter `2n` are A005436(n), `1, 2, 7, 28, 120, …` for `n = 2, 3, …`; the seven of perimeter 8 are the two straight trominoes, the four L-trominoes and the `2 × 2` square. Delest and Viennot proved that there are `(2n + 11) 4^n − 4(2n + 1) C(2n, n)` of perimeter `2n + 8` by coding each convex polyomino as a word of an algebraic language ([[algebraic-languages-and-polyominoes-enumeration](pages/algebraic-languages-and-polyominoes-enumeration.md)]).[^4] Lin and Chang's generating function by width `x` and height `y` refines this count: it is algebraic, with a factor `Δ^{−3/2}`, `Δ = 1 − 2x − 2y − 2xy + x² + y²`, and at `x = y` it gives A005436. With area marked as well, the generating function is a quotient of q-series ([[bousquet-melou-fedou-1995-convex-polyominoes](pages/bousquet-melou-fedou-1995-convex-polyominoes.md)]).[^5]

## The corner taxonomy

Bousquet-Mélou characterizes three classical families of directed and convex polyominoes, the Ferrers diagrams, the stack polyominoes and the parallelogram polyominoes, by which two or three corners of the bounding rectangle they contain, and a convex polyomino is directed exactly when it contains the bottom-left corner.[^6] Bousquet-Mélou and Fédou's Fig. 2 marks the corners for three of the families: parallelogram at bottom-left and top-right, directed convex at bottom-left, and Ferrers at three corners, drawn right-justified, so its third corner is the mirror image of the one in the table.[^7] The stack corners and the column conditions of the table are the wiki's reading. Each column condition reproduces the OEIS count of its family by area through area 11.[^2]

| family | corners contained | column condition | by area |
|---|---|---|---|
| rectangle | all four | every column `[b, t]` the same | number of divisors `d(n)` |
| Ferrers diagram | three (bottom-left, bottom-right, top-left) | bottoms constant, tops weakly decreasing | partitions, A000041 |
| stack polyomino | two (both bottom) | bottoms constant, tops unimodal | A001523 |
| parallelogram (staircase) polyomino | two (bottom-left, top-right) | bottoms and tops both weakly increasing | A006958 |
| directed convex | one (bottom-left) | bottoms weakly increasing, tops unimodal | A067676 |
| convex | none required | tops unimodal, bottoms anti-unimodal | A067675 |

The families nest: rectangle ⊂ Ferrers ⊂ stack ⊂ directed convex ⊂ convex, and, after a left-right reflection of the Ferrers diagrams, Ferrers ⊂ parallelogram ⊂ directed convex. Dropping row-convexity gives the column-convex polyominoes, A001169 by area.

## Bender's three pieces

Bender reads a convex polyomino row by row, with left and right row ends `l_i` and `r_i`, and cuts it at the rows `I = max{i : l_i > l_{i+1}}` and `J = min{j : r_{j−1} > r_j}` into three pieces:[^8]

- **two trapezoids**, in which consecutive rows are nested (`l_i ≤ l_{i+1}`, `r_i ≥ r_{i+1}`), so that the columns stand on the widest row with a unimodal skyline: a stack polyomino, one upright and one upside down. At `y = 1` Bender's trapezoid series is the stack series A001523 (computed through area 20);
- **a parallelogram** in the middle, whose two row ends move the same way. It can be empty; when it is not, it slants northeast or northwest, and the two cases count equally.

The trapezoid series has radius of convergence 1 and the parallelogram series `1/2.30914`, so the number of convex polyominoes of area `n` grows at the rate of the parallelograms.[^8] Bender shows that most convex polyominoes of area `n` resemble rods tilted 45 degrees: the height is asymptotically normal with mean `0.42088n` and variance `0.20806n`, and the horizontal thickness is about `2.37597`.[^9] The count and its constants are on [[bender-1974-convex-n-ominoes](pages/bender-1974-convex-n-ominoes.md)] and [[convex-polyomino-by-area](pages/convex-polyomino-by-area.md)].

## Where the castle sits

- **A castle is a bargraph**, a column-convex polyomino whose columns all start on row 1, so its bottoms are constant ([[castle-polyomino](pages/castle-polyomino.md)]). By area the castles are the compositions of `n`, `2^{n−1}` of them ([[castle-by-area](pages/castle-by-area.md)]).
- **A convex castle is a stack polyomino.** With constant bottoms, row-convexity says that the skyline is unimodal, the stack row of the table. So the convex castles of area `n` are counted by A001523 ([[convex-castle](pages/convex-castle.md)], [[stack-polyomino-gf](pages/stack-polyomino-gf.md)]).
- **Two convex castles and a parallelogram.** Klarner and Rivest cut every convex polyomino along two rows into an upper stack, a middle parallelogram and a lower upside-down stack: a convex castle standing on the parallelogram and another hanging below it. Gluing the pieces back gives `c(n) ≤ (n + 2)^4 p(n)` for the convex count `c(n)` and the parallelogram count `p(n)`, so the two have the same growth constant `2.30913…` (A276994).[^10] The stacks grow subexponentially: A001523(n) ~ `exp(2π√(n/3)) / (8·3^{3/4} n^{5/4})`.[^11] Delest and Viennot make the same cut along the vertical lines through two extreme boundary points, so their stacks stand sideways, and they code each piece as a word: the stacks by Fibonacci words, the parallelogram by a Dyck word ([[algebraic-languages-and-polyominoes-enumeration](pages/algebraic-languages-and-polyominoes-enumeration.md)], [[parallelogram-polyomino-dyck-bijection](pages/parallelogram-polyomino-dyck-bijection.md)]).
- **Blocks become height.** A castle block is a maximal horizontal run of cells in one row. On a row-convex polyomino each row is one run, so the block count is the number of rows, the height. This is the general form of the statement on [[convex-castle](pages/convex-castle.md)] that a convex castle of height `h` has `h` blocks, and it makes the Project Euler 502 parity condition, applied to convex polyominoes, the parity of the height.

## Related Concepts

- [[convex-polyomino-by-area](pages/convex-polyomino-by-area.md)] - every family of the table counted by area and split by the parity of the height, with generating functions and growth constants.
- [[bousquet-melou-fedou-1995-convex-polyominoes](pages/bousquet-melou-fedou-1995-convex-polyominoes.md)] - the generating function by width, height and area of the parallelogram, directed convex and convex polyominoes, from a [[q-differential-system](pages/q-differential-system.md)].
- [[column-convex-polyomino](pages/column-convex-polyomino.md)], [[horizontally-convex-polyomino](pages/horizontally-convex-polyomino.md)] - the two halves of the definition.
- [[convex-castle](pages/convex-castle.md)], [[stack-polyomino-gf](pages/stack-polyomino-gf.md)] - the stack row of the table as castles, and its generating function by area.
- [[column-convex-polygon-enumeration](pages/column-convex-polygon-enumeration.md)] - Bousquet-Mélou's add-a-column method, which gives the parallelogram and directed convex generating functions.
- [[polyominoes](pages/polyominoes.md)] - the wider classification of polyominoes.
- [[inscribed-polyomino](pages/inscribed-polyomino.md)] - all polyominoes with bounding box `w × h` (A292357), which contain the convex ones of that box.
- [[klarner-rivest-1974-convex-n-ominoes](pages/klarner-rivest-1974-convex-n-ominoes.md)] - the trisection and the growth constant `2.309138…`.
- [[bender-1974-convex-n-ominoes](pages/bender-1974-convex-n-ominoes.md)] - the trapezoid, parallelogram and trapezoid split, the growth constant, and the rod shape of most convex polyominoes.
- [[algebraic-languages-and-polyominoes-enumeration](pages/algebraic-languages-and-polyominoes-enumeration.md)] - the count by perimeter and the word coding of the three pieces.

## Footnotes

[^1]: [[column-convex-polygon-enumeration](pages/column-convex-polygon-enumeration.md)] p.1 §1 L90-93 - "A polyomino is said to be vertically convex (or column-convex) when its intersection with any vertical line is convex (Fig. 2). We can define similarly a notion of horizontal (or row-) convexity. A polyomino is convex if it is both vertically and horizontally convex."
[^2]: Verified by execution (Python 3.11, 2026-10-16): all column-convex polyominoes of area at most 11 enumerated by column intervals (A001169: 1, 2, 6, 19, 61, …, 66441); row-convexity tested row by row agrees with the two column conditions on every one; the convex, stack, Ferrers, parallelogram and directed convex counts are A067675, A001523, A000041, A006958 and A067676 (names and data checked on oeis.org); every convex polyomino has perimeter `2(w + h)`; the trapezoid series against A001523 through area 20.
[^3]: [[bousquet-melou-fedou-1995-convex-polyominoes](pages/bousquet-melou-fedou-1995-convex-polyominoes.md)] p.55 L130-133 - "since the perimeter of a convex polyomino is twice the sum of its height and width, the enumeration according to height and width is a refinement of the enumeration according to perimeter."
[^4]: [[algebraic-languages-and-polyominoes-enumeration](pages/algebraic-languages-and-polyominoes-enumeration.md)] p.169 Abstract - "we prove that the number of convex polyominoes with perimeter 2n+8 is (2n+11)4^n - 4(2n+1)C(2n,n)" (the paper's PDF is not on disk; quoted from its source page); https://oeis.org/A005436 (read 2026-10-16) - "Number of convex polygons of perimeter 2n on square lattice", offset 2. The formula agrees with enumeration of convex polyominoes by `w + h` through `w + h = 10` (Python 3.11, 2026-10-16).
[^5]: [[bousquet-melou-fedou-1995-convex-polyominoes](pages/bousquet-melou-fedou-1995-convex-polyominoes.md)] p.55 L117-135 - "the bivariate generating function on convex polyominoes for height and width, obtained by Lin and Chang [13] ... the formula of Lin and Chang refines the perimeter generating function given by Delest and Viennot [10]" (formula read from the page image).
[^6]: [[column-convex-polygon-enumeration](pages/column-convex-polygon-enumeration.md)] p.2 §1 L131-137 - "three very classical families of directed and convex polyominoes: Ferrers diagrams, stack polyominoes, and parallelogram (or staircase) polyominoes. As Fig. 3 shows, each of these subsets can be characterized, in the set of convex polyominoes, by the fact that two or three vertices of the minimal bounding rectangle of the polyomino belong to the polyomino itself. Moreover, a convex polyomino is directed if and only if it contains the south-west vertex of its minimal bounding rectangle."
[^7]: [[bousquet-melou-fedou-1995-convex-polyominoes](pages/bousquet-melou-fedou-1995-convex-polyominoes.md)] Fig. 2, p.55 L100-106 - "Different subclasses of convex polyominoes"; the marked corners are read from the page image.
[^8]: [[bender-1974-convex-n-ominoes](pages/bender-1974-convex-n-ominoes.md)] pp.220 §2, 222-223 §4 and Fig. 1 [synthesis] - trapezoids "l_i ≤ l_{i+1} and r_i ≥ r_{i+1}", parallelograms "l_i ≤ l_{i+1} < r_i ≤ r_{i+1}"; I is "the maximum i such that l_i > l_{i+1}", J "the minimum j such that r_{j−1} > r_j", and the three parts are the rows "i ≤ I, I < i < J, i ≥ J"; "Since T(x, 1) has radius of convergence 1 which exceeds r, it follows that c(n) ~ 2c*(n)."
[^9]: [[bender-1974-convex-n-ominoes](pages/bender-1974-convex-n-ominoes.md)] p.219 abstract, pp.224-225 §5 - "most convex n-ominoes resemble rods tilted 45° from the vertical with horizontal (and vertical) thickness roughly equal to 2.37597"; "a normal distribution with mean μ_n ~ 0.42088n and variance σ_n^2 ~ 0.20806n".
[^10]: [[klarner-rivest-1974-convex-n-ominoes](pages/klarner-rivest-1974-convex-n-ominoes.md)] p.32-34 §2 L69-124 [synthesis] - "the trisection of a convex n-omino A is accomplished by cutting along the lowest level of A where the left boundary of A goes to the right and by cutting along the lowest level of A where the right boundary of A goes to the left"; "every convex n-omino splits into two stacks and one parallelogram"; (3) `c(n) <= (n+2)^4 p(n)` and (5); https://oeis.org/A276994 (read 2026-10-16) - "Decimal expansion of the Klarner-Rivest polyomino constant".
[^11]: https://oeis.org/A001523 (read 2026-10-16) - "a(n) ~ exp(2*Pi*sqrt(n/3)) / (8 * 3^(3/4) * n^(5/4)) [Auluck, 1951]".
