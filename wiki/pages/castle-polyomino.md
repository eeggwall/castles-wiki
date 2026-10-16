---
title: Castle (polyomino)
category: Concepts
summary: The central object of study. A castle of width w and height h is a skyline (c_1, …, c_w) with 1 ≤ c_i ≤ h and some c_i = h; its blocks are the maximal runs of columns in each row, so the block count is the total ascent of the skyline, equal to its total descent. There are A(w, h) = h^w − (h−1)^w castles of width w and height h, of which A^e(w, h), the Project Euler 502 count, have an even number of blocks. In the polyomino literature a castle is a bargraph.
tags: [concept, castle, polyomino, bargraph, column-convex, skyline, combinatorics]
sources: [project-euler-502, prellberg-brak-1995-cluster-models, project-euler-502-problem-setup, project-euler-502-representations, project-euler-502-castle-factoring, project-euler-502-solution, project-euler-502-brute-force]
created: 2026-09-13
updated: 2026-10-16
---

# Castle (polyomino)

## Definition

A **castle** of width `w` and height `h` is a **skyline**, a tuple of column heights[^1]

```
c = (c_1, c_2, …, c_w),   with  1 ≤ c_i ≤ h  for every i,   and  c_i = h  for some i.
```

Column `i` is the stack of unit cells at heights `1, 2, …, c_i`, and the castle is the union of the `w` columns. Every column is one vertical run of cells starting at row 1, so row 1 is full, and some column reaches row `h`; that is what "height `h`" means. The only castle of height 1 is the flat row `(1, …, 1)`.

*Example.* The skyline `(1, 3, 2, 3, 1)` is a castle of width 5 and height 3:

```
row 3   .  #  .  #  .
row 2   .  #  #  #  .
row 1   #  #  #  #  #
```

A castle is a column-convex polyomino with a horizontal lower boundary, which the polyomino literature calls a **bar-graph polygon** or **bargraph**.[^2] So the castles of width `w` and height `h` are the bargraphs of width `w` whose tallest column has height `h`, next to the Ferrers, staircase, stack and parallelogram polyominoes ([[polyominoes](pages/polyominoes.md)], [[column-convex-polyomino](pages/column-convex-polyomino.md)]). The full bottom row meets the left, right and bottom sides of the `w × h` rectangle, and a column of height `h` meets its top, so the castles are the bargraphs among the polyominoes with bounding box `w × h` ([[inscribed-polyomino](pages/inscribed-polyomino.md)]).

## Blocks

The **blocks** in row `r` are the maximal runs of consecutive columns with `c_i ≥ r`.[^3] With `c_0 = c_{w+1} = 0`, the block count is

```
blocks(c)  =  Σ_{i=1}^{w} max(0, c_i − c_{i−1})  =  Σ_{i=0}^{w} max(0, c_i − c_{i+1}).
```

A column of height `c_i` next to a column of height `c_{i−1}` starts `max(0, c_i − c_{i−1})` new blocks, which gives the first sum, the **total ascent**. The second sum is the **total descent**, and the two are equal because `Σ_{i=0}^{w} (c_{i+1} − c_i) = c_{w+1} − c_0 = 0`. In the example, the total ascent is `1 + 2 + 0 + 1 + 0 = 4` and the total descent is `1 + 2 + 1 = 4`: one block in row 1, one in row 2 and two in row 3.

## Counts

The skylines in `{1, …, h}^w` number `h^w`, and those that do not reach `h` number `(h−1)^w`, so the number of castles of width `w` and height `h` is[^4]

```
A(w, h)  =  h^w − (h−1)^w.
```

`A^e(w, h)` and `A^o(w, h)` count the castles of width `w` and height `h` with an even and with an odd number of blocks, so `A = A^e + A^o`. Project Euler 502 asks for `A^e(w, h)`, which the problem statement writes `F(w, h)`,[^5] and the [[castle-counting-formula](pages/castle-counting-formula.md)] gives it in closed form. The example castle has 4 blocks, so it is one of the `A^e(5, 3)` even-block castles of width 5 and height 3. [[castle-notation](pages/castle-notation.md)] lists the counts and the signed count `S = A^e − A^o`.

## The Project Euler rules

Project Euler 502 defines a castle as a configuration of blocks, rectangles of height 1 and integer length, on a grid `w` units wide and `h` units tall, by six rules:[^6]

1. A block rests on other blocks, with nothing sticking out past their edges or hanging over open space.
2. Blocks are aligned to the grid.
3. Any two neighboring blocks in the same row have at least one unit of space between them.
4. The bottom row is one block of length `w`.
5. The castle has height `h`.
6. The castle has an even number of blocks.

Rules 1 to 5 define the castles of width `w` and height `h`, and rule 6 selects the even-block ones, counted by `A^e(w, h)`. A configuration satisfying rules 1 to 5 has the column heights of a castle as defined in the section *Definition*: by rules 1 and 4 every column is a run of cells from row 1 up, by rule 2 its height is an integer, and by rule 5 the tallest column has height `h`. The configuration is determined by its skyline: by rule 3 two blocks in a row never touch, so the blocks of each row are its maximal runs of cells. Conversely, the maximal runs of every skyline satisfy rules 1 to 4. So castles in the sense of the rules correspond one-to-one with skylines.[^3]

[[castle-representations](pages/castle-representations.md)] states each rule as a constraint on the binary-string, skyline and step-string encodings, and [[urd-step-strings](pages/urd-step-strings.md)] gives the step-string form.

## Encodings

Besides the skyline, a castle can be encoded by column-wise binary strings or by a word in the steps `U`, `R` and `D` ([[castle-representations](pages/castle-representations.md)]). In the step word, a castle is `U (towers) D`, where the outer `U … D` is the bottom row; each `D` ends one block. The tower grammar excludes the factors `UD`, a block of width 0, and `DU`, two touching blocks in a row ([[generalized-dyck-grammar](pages/generalized-dyck-grammar.md)]).[^7]

## Appearances in Sources

- [[project-euler-502](pages/project-euler-502.md)] - the problem statement: blocks, the six castle rules, and the count `F(w, h)`.
- [[project-euler-502-problem-setup](pages/project-euler-502-problem-setup.md)] - a restatement of the rules other than rule 2.
- [[project-euler-502-representations](pages/project-euler-502-representations.md)] - the encodings of a castle, and validity of the step word (each `D` ends a block; no `UD`, no `DU`).
- [[project-euler-502-castle-factoring](pages/project-euler-502-castle-factoring.md)] - the column heights of towers, and the block count as total descent.
- [[project-euler-502-solution](pages/project-euler-502-solution.md)] - the notation `A(w, h)` and `F(w, h)`.
- [[project-euler-502-brute-force](pages/project-euler-502-brute-force.md)] - the skyline encoding and the block count as total ascent.
- [[prellberg-brak-1995-cluster-models](pages/prellberg-brak-1995-cluster-models.md)] - the definition of bar-graph polygons.

## Related Concepts

- [[castle-notation](pages/castle-notation.md)] - the symbols `A`, `A^e`, `A^o`, `S`, `T`, `P` and the tower height `k = h − 1`.
- [[castle-counting-function](pages/castle-counting-function.md)] - the counts `A`, `A^e` and `A^o`, and the Project Euler checkpoints.
- [[castle-counting-formula](pages/castle-counting-formula.md)] - the closed form `A^e(w, h) = [A(w, h) − P(h−1, w) + P(h−2, w)]/2` through the signed tower count.
- [[castle-sign](pages/castle-sign.md)] - the sign `(−1)^{blocks}` and the split into even-block and odd-block castles.
- [[castle-representations](pages/castle-representations.md)] - the three encodings: binary strings, skylines, and step strings.
- [[castle-classification](pages/castle-classification.md)] - families of castles, with the 42 shape types of [[castle-classification-shape](pages/castle-classification-shape.md)].
- [[castle-strip](pages/castle-strip.md)] - castles read one column at a time under a rule on neighboring columns, counted by transfer matrices.
- [[convex-castle](pages/convex-castle.md)] - castles with a unimodal skyline, the stack polyominoes of the literature.
- [[castle-perimeter](pages/castle-perimeter.md)] - the semi-perimeter `w + blocks` of a castle, and castles counted by semi-perimeter (A082582).
- [[inscribed-polyomino](pages/inscribed-polyomino.md)] - the polyominoes with bounding box `w × h`, counted by `I(w, h)` (A292357), with `A(w, h) ≤ I(w, h)`.
- [[column-convex-polyomino](pages/column-convex-polyomino.md)] and [[polyominoes](pages/polyominoes.md)] - the families of polyominoes that contain the castles.
- [[prellberg-brak-1995-cluster-models](pages/prellberg-brak-1995-cluster-models.md)] - the functional equation (3.11) for bargraphs, with `x` marking width, `y` the vertical half-perimeter, which is the block count, and `q` area.
- [[column-convex-polygon-enumeration](pages/column-convex-polygon-enumeration.md)] - the add-a-column method for column-convex polygons; a castle is a directed column-convex polygon whose columns all start on row 1.
- [[generalized-dyck-grammar](pages/generalized-dyck-grammar.md)] - the grammar of tower words.
- [[permutation-cycle-castle-analogy](pages/permutation-cycle-castle-analogy.md)] - the correspondence of permutation cycles with peaks.

## Footnotes

[^1]: [[project-euler-502-brute-force](pages/project-euler-502-brute-force.md)] §"Column-height encoding" L18 - "A castle of width w, height h is a skyline: column heights c_1, …, c_w ∈ {1, …, h} with max c = h. This is Rules 1, 2, 4, 5."
[^2]: [[prellberg-brak-1995-cluster-models](pages/prellberg-brak-1995-cluster-models.md)] §3.1 "Bar-Graph Polygons" L399-402 - "Our next example will be bar-graph polygons, that is, column-convex polygons with a horizontal lower boundary."
[^3]: [[project-euler-502-brute-force](pages/project-euler-502-brute-force.md)] §"Column-height encoding" L20-27 - "A block is a maximal horizontal run of columns at a given level, so #blocks = ∑_{r=1}^{h} #{runs of columns with c_i ≥ r} = c_1 + ∑_{i=2}^{w} max(0, c_i − c_{i−1})", and "Rule 3 (gap between neighbouring blocks in the same row) is automatic in the run decomposition: two runs at the same level are always separated by a strictly lower column."
[^4]: [[project-euler-502-observations](pages/project-euler-502-observations.md)] §"The \"even number of blocks\" clause is almost the entire difficulty" L17 - "Without it, the answer is just h^w - (h-1)^w: all castles of height at most h minus those of height at most h-1."
[^5]: [[project-euler-502](pages/project-euler-502.md)] §"Project 502: Castle Polyominoes" L26 - "Let F(w,h) represent the number of valid castles, given grid parameters w and h."
[^6]: [[project-euler-502](pages/project-euler-502.md)] §"Project 502: Castle Polyominoes" L11-20 - "We define a block to be a rectangle with a height of 1 and an integer-valued length", "Blocks can be placed on top of other blocks as long as nothing sticks out past the edges or hangs out over open space. All blocks are aligned/snapped to the grid. Any two neighboring blocks on the same row have at least one unit of space between them. The bottom row is occupied by a block of length w. The maximum achieved height of the entire castle is exactly h. The castle is made from an even number of blocks."
[^7]: [[project-euler-502-representations](pages/project-euler-502-representations.md)] §"The grammar" L270-276 [synthesis] - the tail `empty | R E_k` keeps two blocks from touching (no `DU`) and a nonempty interior keeps every block's width positive (no `UD`).
