---
title: Castles of exact height h by area - the n-nacci family
category: Analyses
summary: All castles (not just tree castles) of exact height h, graded by total area A, are the compositions of A with largest part exactly h, so their count is the difference of two consecutive n-nacci counts, (compositions into {1, …, h}) − (compositions into {1, …, h − 1}), with GF 1/(1 − x − ⋯ − x^h) − 1/(1 − x − ⋯ − x^{h−1}). The count grows like the h-nacci constant - φ at h = 2 (F_{A+1} − 1), tribonacci 1.8393 at h = 3 (A000073(A+2) − F_{A+1}), tetranacci 1.9276 at h = 4, pentanacci 1.9659 at h = 5 - tending to 2, the growth of all castles by area. Tree castles of exact height h grow more slowly (supergolden, golden, 1.6851, and plastic squared with the height unrestricted).
tags: [analysis, castle, area, generating-function, oeis, fibonacci, tribonacci, tetranacci, n-nacci, composition, growth-constant]
sources: [project-euler-502-castle-factoring]
created: 2026-09-17
updated: 2026-10-03
---

# Castles of exact height `h` by area

## The result

Grade **all** castles - no tree or convexity restriction - of exact height `h` (some column reaches `h`) by total area `A = Σ c_i`. A castle skyline `(c_1, …, c_w)` is a composition of its area ([[castle-representations](pages/castle-representations.md)]), and Rule 3 is automatic for area-graded all-castles (the same observation that gives the `2^{A−1}` count of all castles on [[castle-by-area](pages/castle-by-area.md)]). Exact height `h` means largest part exactly `h`. Compositions with every part in `{1, …, h}` satisfy the `h`-term recurrence `a(A) = a(A−1) + ⋯ + a(A−h)`, the `h`-nacci recurrence, because the last part is one of `1, …, h`. So

```
#{castles of exact height h and area A}
    =  #{compositions of A into parts {1, …, h}}  −  #{compositions of A into parts {1, …, h − 1}},
```

with ordinary generating function[^1]

```
Σ_A (count) x^A  =  1 / (1 − x − ⋯ − x^h)  −  1 / (1 − x − ⋯ − x^{h−1}).
```

The first term dominates, so the count grows like the `h`-nacci constant, the root in `(1, 2)` of `x^h = x^{h−1} + ⋯ + x + 1`.

## The ladder

| `h` | exact-height-`h` castles by area, `A = 1..12` | closed form | growth constant |
|---|---|---|---|
| 2 | `0, 1, 2, 4, 7, 12, 20, 33, 54, 88, 143, 232` | `F_{A+1} − 1` (A000045) | `φ ≈ 1.6180` |
| **3** | `0, 0, 1, 2, 5, 11, 23, 47, 94, 185, 360, 694` | `A000073(A+2) − F_{A+1}` | **`τ ≈ 1.8393`** (root of `x³ = x² + x + 1`) |
| 4 | `0, 0, 0, 1, 2, 5, 12, 27, 59, 127, 269, 563` | `A000078(A+3) − A000073(A+2)` | `≈ 1.9276` (root of `x⁴ = x³ + x² + x + 1`) |
| 5 | `0, 0, 0, 0, 1, 2, 5, 12, 28, 63, 139, 303` | `A001591(A+4) − A000078(A+3)` | `≈ 1.9659` |
| unrestricted | `1, 2, 4, 8, 16, 32, 64, …` | `2^{A−1}` (A011782) | `2` |

The n-nacci constants increase from `φ` to `2`, the growth of all castles by area ([[castle-by-area](pages/castle-by-area.md)]). The closed forms use the OEIS offsets: A000073 has GF `x²/(1−x−x²−x³)`, so compositions of `A` into parts `{1, 2, 3}` number `A000073(A+2)`; A000078 has GF `x³/(1−x−x²−x³−x⁴)`, giving `A000078(A+3)`; and likewise `A001591(A+4)` for parts up to 5.[^2]

## Why this is not the tree-castle-by-area family

The neighbouring family is [[tree-castle-by-area](pages/tree-castle-by-area.md)]: **tree** castles (no 2×2 filled block, i.e. no two adjacent columns both `≥ 2`) graded by area. At the same exact height they grow more slowly:[^1]

| exact height `h` | all castles (this page) | tree castles |
|---|---|---|
| 2 | `φ` | supergolden `≈ 1.4656` (one less than Narayana's cows, A000930) |
| 3 | tribonacci `τ ≈ 1.8393` | golden `φ` (from A006498, whose denominator has the factor `1 − q − q²`) |
| 4 | tetranacci `≈ 1.9276` | `≈ 1.6851` (from A000570, Tetali; [[unique-tournament](pages/unique-tournament.md)]) |
| unrestricted | `2` | plastic squared `ψ² ≈ 1.7549` (A005251) |

The OEIS sequences in the tree column count tree castles with every column at most `h`; the exact-height count is the difference of consecutive rows and has the same growth constant. At exact height `h` the all-castle count exceeds the tree count from area `h + 2` on, where the tree constraint first deletes a composition with two adjacent parts `≥ 2`. The tree family's area denominators (`1 − q − q³`, `1 − q − q³ − q⁴`, …) have no `q²` term, because in its composition form every tall column merges with a short one into a part of size at least 3; the all-castle denominators `1 − x − ⋯ − x^h` keep it.

## Fibonacci and tribonacci, on one ladder

Fibonacci and tribonacci are the `h = 2` and `h = 3` members of this one family.

- **Fibonacci (`h = 2`).** Castles of exact height 2 by area number `F_{A+1} − 1`: compositions into `{1, 2}` with at least one 2. This is a different Fibonacci appearance from the prime-castle count `F_{n−1}` ([[prime-castles](pages/prime-castles.md)], compositions into parts `≥ 2`) and from the Fibonacci castles by width ([[castle-graph](pages/castle-graph.md)]). It has the same numbers as the Fibonacci castles of width `A − 1` (by appending a height-1 column and reading each height-2 column with the column after it as a part 2; [[n-nacci-disambiguation](pages/n-nacci-disambiguation.md)]).
- **Tribonacci (`h = 3`).** Castles of exact height 3 by area number `A000073(A+2) − F_{A+1}` and grow like `τ`. With the supergolden constant (`x³ = x² + 1`, the q-Fibonacci castles by number of cells, [[q-fibonacci-castle](pages/q-fibonacci-castle.md)]) and the plastic number (`x³ = x + 1`, as `ψ²` and `2ψ²` on [[plastic-number](pages/plastic-number.md)]), the castle realizes three cubic constants by area.

## Relation to the metallic-means classification

On the Axis-8 meta-classification of [[castle-classification](pages/castle-classification.md)] / [[metallic-means](pages/metallic-means.md)], this family is **not** metallic: the n-nacci constants for `h ≥ 3` are roots of `x^h = x^{h−1} + ⋯ + 1`, algebraic of degree `h`, and none is a metallic mean `(a + √(a²+4))/2`. Only the `h = 2` rung (`φ`) is on the metallic ladder. The tree castles by area are metallic only at exact height 3, where their growth is `φ`.

## Reproduce

The `bounded_castles_by_area(h, A_max)` snippet on [[castle-snippets-strips](pages/castle-snippets-strips.md)] computes the compositions of `A` with parts at most `h`, with a brute-force cross-check against skylines. The exact-height counts above are `bounded_castles_by_area(h, ·)` minus `bounded_castles_by_area(h − 1, ·)`.

## Appearances in Sources

- [[project-euler-502-castle-factoring](pages/project-euler-502-castle-factoring.md)] - the `F(w, h)` skyline model whose height `h` and area statistic this grading uses.

## Related Concepts

- [[n-nacci-disambiguation](pages/n-nacci-disambiguation.md)] - every Fibonacci, tribonacci and higher n-nacci appearance on the wiki, with this page as the common spine.
- [[tree-castle-by-area](pages/tree-castle-by-area.md)] - the sparser sibling (2×2-block ban), with term-skipping denominators.
- [[castle-by-area](pages/castle-by-area.md)] - all castles by area, `2^{A−1}`, the limit of this ladder.
- [[plastic-number](pages/plastic-number.md)] - the third cubic constant (`ψ`, `x³ = x + 1`); this page adds the tribonacci constant (`x³ = x² + x + 1`) to the cubic constants by area.
- [[metallic-means](pages/metallic-means.md)] - the family the `h = 2` rung (`φ`) belongs to and the `h ≥ 3` rungs sit outside.
- [[castle-graph](pages/castle-graph.md)] - the tree castles by width (Fibonacci, Jacobsthal, k-Fibonacci), the width-axis cousin of this area-axis ladder.
- [[weakly-unimodal-composition](pages/weakly-unimodal-composition.md)] - the composition ↔ castle correspondence this result rests on, in its convex (stack) form.
- [[unique-tournament](pages/unique-tournament.md)] - the graph-theoretic side of the `h = 4` tree sequence A000570.
- [[aocp-generating-permutations-tuples](pages/aocp-generating-permutations-tuples.md)] - the by-area enumeration behind `bounded_castles_by_area` is Knuth's Algorithm M with an area filter.
- [[area-growth-census](pages/area-growth-census.md)] - every castle-strip rule through height 5 by area; the `h`-nacci constant is the largest growth at each height.

## Footnotes

[^1]: Verified by execution (Python 3, 2026-10-02): brute-force enumeration of compositions with largest part exactly `h` agrees with the difference of the two composition recurrences for `h = 2..5` and `A ≤ 14`; the tree-castle counts at exact height `h = 2, 3, 4` by area were enumerated directly for `A ≤ 16` and by a two-state transfer recurrence to `A = 400`, where the successive ratios are `1.465571`, `1.618034`, `1.685137`; at each `h` the all-castle and tree counts agree through area `h + 1` and differ from area `h + 2`. The GF `1/(1 − x − ⋯ − x^h)` is the standard OGF for compositions into parts `{1, …, h}` (sequence (SEQ) of `{x, x², …, x^h}`; [[symbolic-method](pages/symbolic-method.md)] SEQ construction). An earlier check (2026-09-17) compared the composition counts with parts at most `h` to skylines `c ∈ {1, …, h}^w` for `h = 2..5` and `A ≤ 14`.

[^2]: OEIS (fetched 2026-09-17): https://oeis.org/A000073 - tribonacci, "a(n) = a(n-1) + a(n-2) + a(n-3)", GF `x²/(1 − x − x² − x³)`, data `0, 0, 1, 1, 2, 4, 7, 13, 24, 44, 81, 149, 274`, comment "number of compositions of n-2 with no part greater than 3"; tribonacci constant `1.839286755…`, the real root of `x³ − x² − x − 1`. https://oeis.org/A000078 - tetranacci, GF `x³/(1 − x − x² − x³ − x⁴)`, "number of compositions of n-3 with no part greater than 4". Offsets `A000073(A+2)`, `A000078(A+3)`, `A001591(A+4)` follow from the numerator power `x^{h−1}` in each GF. A000045 (Fibonacci) and A011782 (`2^{n−1}`) are standard.
