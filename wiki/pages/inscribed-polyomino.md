---
title: Inscribed polyomino
category: Concepts
summary: A polyomino inscribed in a w × h rectangle has a cell on each of the four sides, so its bounding box is exactly w × h. The count I(w, h) is the OEIS table A292357, symmetric in w and h and rational in h at fixed w (Marin's row automaton). Every castle of width w and exact height h is inscribed in w × h; the castles are the bargraphs in the table, A(w, h) ≤ I(w, h).
tags: [concept, polyomino, inscribed-polyomino, bounding-box, fixed-polyomino, castle, bargraph, automaton, transfer-matrix, oeis]
sources: [marin-2024-polyominoes-in-rectangle]
created: 2026-10-06
updated: 2026-10-06
---

# Inscribed polyomino

## Description

A polyomino is **inscribed** in a `w × h` rectangle when it lies inside the rectangle and has at least one cell on each of the rectangle's four sides.[^1] The rectangle is then the polyomino's bounding box, so "inscribed in `w × h`" is the same as "width exactly `w` and height exactly `h`". Write `I(w, h)` for the number of such polyominoes, counted as **fixed** polyominoes: translates are identified, while rotations and reflections are distinct. This is the OEIS table A292357 ("the number of fixed polyominoes that have a width of m and height of n"). OEIS also describes it as the number of `m × n` binary arrays whose 1s are connected and include at least one 1 on each edge.[^2] Transposing a polyomino swaps width and height, so `I(w, h) = I(h, w)`.

For fixed width `w`, the count is a linear recurrence in `h`. Marin's automaton `𝒜_w` reads a polyomino one row at a time. A state records a non-crossing labelling of the row's connected components and whether the left and right walls have been touched. It proves the recurrence for every `w` and computes it ([[marin-2024-polyominoes-in-rectangle](pages/marin-2024-polyominoes-in-rectangle.md)]).[^3] The state count is OEIS A378947: 1, 2, 6, 16, 40, 99, 247, 625, … for `w = 0, 1, 2, …`.[^4] At width 2 the count is `I(2, h) = Q_{h+1} − 2`, where `Q_n` are the Pell-Lucas numbers (A001333, [[pell-numbers](pages/pell-numbers.md)]). Its generating function is `(1 − 2x + 3x² + 2x³)/((1 − x)(1 − 2x − x²))`, which includes `h = 0`.[^5]

## Castles inside the table

A castle of width `w` and exact height `h` ([[castle-polyomino](pages/castle-polyomino.md)]) is inscribed in `w × h`. Its full bottom row meets the bottom, left and right sides, and a column of height `h` meets the top. The castles are exactly the **bargraphs** among the inscribed polyominoes: those whose columns are single vertical runs standing on the bottom row. So

```
A(w, h)  =  h^w − (h − 1)^w  ≤  I(w, h).
```

Unlike `I`, `A` is not symmetric: the transpose of a castle is in general not a castle. The two counts for `w, h ≤ 5`, with `I(w, h)` first and `A(w, h)` in brackets:[^exec]

| `w \ h` | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|
| 1 | 1 (1) | 1 (1) | 1 (1) | 1 (1) | 1 (1) |
| 2 | 1 (1) | 5 (3) | 15 (5) | 39 (7) | 97 (9) |
| 3 | 1 (1) | 15 (7) | 111 (19) | 649 (37) | 3495 (61) |
| 4 | 1 (1) | 39 (15) | 649 (65) | 7943 (175) | 86995 (369) |
| 5 | 1 (1) | 97 (31) | 3495 (211) | 86995 (781) | 1890403 (2101) |

At height 2 the castles are `2^w − 1` of `I(w, 2)`, which is the width-2 column read by transposition: 3 of 5, 7 of 15, 15 of 39.

**State counts.** At fixed height `h` and growing width, the orientation of Project Euler 502, an inscribed polyomino needs `𝒜_h` read along columns, with A378947(h) states. A castle needs only the `h` states of the castle strip, one per column height ([[castle-strip](pages/castle-strip.md)]). The difference is connectivity. Each castle column is one run standing on the full base row, so every cell is joined to the rest through row 1, and no component labels or wall flags are needed. The left and right walls are touched by the base, and the top wall is the exact-height condition `max c_i = h`.

**Convex polyominoes.** Every polyomino is inscribed in its own bounding box. For the convex class this is how perimeter counting reduces to counting by `w + h` ([[convex-polyomino](pages/convex-polyomino.md)]). The stack polyominoes, which are the convex castles ([[convex-castle](pages/convex-castle.md)]), lie in both the convex and the castle subclasses of `I(w, h)`.

## Appearances in Sources

- [[marin-2024-polyominoes-in-rectangle](pages/marin-2024-polyominoes-in-rectangle.md)] - defines inscribed polyominoes, builds the row automaton `𝒜_w`, gives `G_2`, the degrees of `G_3`-`G_6`, and the state-count formula.

## Related Concepts

- [[castle-polyomino](pages/castle-polyomino.md)] - the castle, the bargraph subclass of `I(w, h)`.
- [[castle-strip](pages/castle-strip.md)] - the `h`-state castle transfer matrix, against the A378947(h) states of `𝒜_h`.
- [[polyominoes](pages/polyominoes.md)] / [[column-convex-polyomino](pages/column-convex-polyomino.md)] - the class taxonomy; a bargraph is a column-convex polyomino with a full bottom row.
- [[convex-polyomino](pages/convex-polyomino.md)] - the row- and column-convex subclass, counted by width and height through Lin and Chang's generating function.
- [[pell-numbers](pages/pell-numbers.md)] - the width-2 count `Q_{h+1} − 2`.
- [[catalan-numbers](pages/catalan-numbers.md)] / [[motzkin-numbers](pages/motzkin-numbers.md)] - the non-crossing component partitions in the state count and its Motzkin form.

## Footnotes

[^1]: [[marin-2024-polyominoes-in-rectangle](pages/marin-2024-polyominoes-in-rectangle.md)] p.145 §1 L15-17 - "By inscribed, we mean a polyomino that is included in a rectangle of size b × h and that has at least one cell touching each side of the rectangle."
[^2]: https://oeis.org/A292357 (fetched 2026-10-06) - "Array read by antidiagonals: T(m,n) is the number of fixed polyominoes that have a width of m and height of n"; comment "Equivalently, the number of m X n binary arrays with all 1's connected and at least one 1 on each edge."
[^3]: [[marin-2024-polyominoes-in-rectangle](pages/marin-2024-polyominoes-in-rectangle.md)] pp.145-148 §1-2 [synthesis] L17-32, L54-78, L147-150 - fixed `b` gives a linear recurrence in `h`; states `(w, l, r)` with component labels, wall flags and the non-crossing condition; Theorem 1, the bijection between accepted stacks of `h` rows and polyominoes inscribed in `b × h`.
[^4]: [[marin-2024-polyominoes-in-rectangle](pages/marin-2024-polyominoes-in-rectangle.md)] p.149 Figure 2 L199-202 - "number of states in A_b" `1, 2, 6, 16, 40, 99, 247, 625, 1605, 4178, 11006, 29292`; listed at https://oeis.org/A378947 (fetched 2026-10-06).
[^5]: https://oeis.org/A034182 (fetched 2026-10-06) - "a(n) = A001333(n+1)-2" and "G.f.: x*(1+x)^2/((1-x)*(1 - 2*x - x^2))"; adding the `h = 0` term 1 gives the paper's `G_2`, [[marin-2024-polyominoes-in-rectangle](pages/marin-2024-polyominoes-in-rectangle.md)] p.145 §1 L23-25.
[^exec]: Verified by execution (2026-10-06). `I(w, h)` was computed from an implementation of Marin's automaton, with entries `w = 2, h ≤ 6` and `w = 3, h ≤ 5` also checked by brute-force enumeration of connected cell sets touching all four sides. All values agree with the A292357 data. `A(w, h) = h^w − (h − 1)^w`.
