---
title: The Padovan families of castles
category: Analyses
summary: Five castle families grow at the plastic number ψ and are counted exactly by shifted Padovan numbers (A000931) - the maximal castles and the (1, 2)-RLL castles by width, the ridge castles of height 2 and the palindromic tree castles by area, and the height-3 rule 1 → 2 → 3 → {1, 2} by width. Every one is a sequence of blocks of size 2 and 3 (generating function 1/(1 − x² − x³)) between two boundary pieces, and four share the boundary x(1 + x)² up to a power of x. Three explicit bijections carry the ridge castles of area A, the rule's castles of width w and the (1, 2)-RLL castles of width w onto the maximal castles of widths A − 1, w − 2 and w + 2. The palindromic tree castles of area n have exactly the maximal castles' generating function x(1 + x)²/(1 − x² − x³), because halving a palindrome substitutes y = x² into the tree castles' denominator 1 − 2y + y² − y³, which factors as (1 − x² − x³)(1 − x² + x³); no explicit bijection is known for them.
tags: [analysis, castle, padovan, plastic-number, generating-function, bijection, maximal-castle, run-length-limited, ridge-castle, tree-castle, palindrome, oeis, sympy, verification]
sources: [project-euler-502]
created: 2026-10-11
updated: 2026-10-16
---

# The Padovan families of castles

## The question

The **Padovan numbers** `P(n)` (A000931) start `1, 0, 0, 1, 0, 1, 1, 1, 2, 2, 3, 4, 5, 7, 9, 12, 16, …` and satisfy `P(n) = P(n − 2) + P(n − 3)`; they grow at the plastic number `ψ ≈ 1.3247`, the real root of `x³ = x + 1` ([[plastic-number](pages/plastic-number.md)]). Five castle families are counted by them exactly, each at its own shift ([[golden-silver-bronze-plastic-castles](pages/golden-silver-bronze-plastic-castles.md)]). This page explains why: what they share, and how to turn one into another.

## The five families

A column of height 2 next to columns of height 1 is the basic piece throughout. In the first two families a **gap** is a run of height-1 columns between two height-2 columns, and an **end run** is a run of height-1 columns at either end.

| family | rule | example | count | graded by |
|---|---|---|---|---|
| maximal castles ([[fibonacci-castles-sub-families](pages/fibonacci-castles-sub-families.md)]) | height 2; gaps of 1 or 2; end runs of at most 1 | `(2, 1, 1, 2, 1)` | `P(w + 6)` | width `w` |
| `(1, 2)`-RLL castles ([[fibonacci-castles-sub-families](pages/fibonacci-castles-sub-families.md)]) | height 2; gaps of 1 or 2; end runs of at most 2 | `(1, 1, 2, 1, 2)` | `P(w + 8)` for `w ≥ 3` | width `w` |
| ridge castles of height 2 ([[ridge-castle](pages/ridge-castle.md)]) | columns 1 and 2, some 2, no two adjacent 1s | `(2, 1, 2, 2, 1)` | `P(A + 5)` for `A ≥ 2` | area `A` |
| palindromic tree castles ([[castle-sequence-catalogue](pages/castle-sequence-catalogue.md)]) | no two adjacent columns both of height 2 or more; the same read backwards | `(3, 1, 3)` | `P(A + 6)` | area `A` |
| the rule `1 → 2 → 3 → {1, 2}` from height 1 | first column 1; each column one higher than the last, except after a 3, which drops to 1 or 2; reaches 3 | `(1, 2, 3, 2, 3, 1, 2)` | `P(w + 4)` for `w ≥ 3` | width `w` |

Their generating functions all have the denominator `1 − x² − x³`:[^exec]

| family | generating function |
|---|---|
| maximal castles | `x (1 + x)² / (1 − x² − x³)` |
| palindromic tree castles | `x (1 + x)² / (1 − x² − x³)` |
| ridge castles of height 2 | `x² (1 + x)² / (1 − x² − x³)` |
| the rule from height 1 | `x³ (1 + x)² / (1 − x² − x³)` |
| `(1, 2)`-RLL castles | `x (1 + x + x²)² / (1 − x² − x³)` |

## The common core: blocks of size 2 and 3

`1 / (1 − x² − x³)` counts sequences of blocks of size 2 and 3: the compositions of `n` into 2s and 3s, `P(n + 3)` of them. Four of the families are visibly such a sequence between two boundary pieces:

- **Maximal castles.** After the first height-2 column, the castle is a sequence of blocks `(1, 2)` (size 2) and `(1, 1, 2)` (size 3), each a gap followed by the next height-2 column. The first height-2 column gives `x`; an optional height-1 column at each end gives `(1 + x)` twice.
- **`(1, 2)`-RLL castles.** The same blocks, with end runs of 0, 1 or 2 columns, so each end gives `1 + x + x²`.
- **Ridge castles of height 2, by area.** An optional leading column `1` (area 1), then a nonempty sequence of the pieces `(2)` (area 2) and `(2, 1)` (area 3). One leading `1` and the first piece give `(1 + x)(x² + x³) = x² (1 + x)²`.
- **The rule from height 1.** The first climb `1, 2, 3` gives `x³`; then climbs `2, 3` (size 2) and `1, 2, 3` (size 3); then a tail after the last 3 of `1`, `2` or `1, 2`, which with the empty tail gives `1 + 2x + x² = (1 + x)²`.

The **palindromic tree castles** have no such reading; their generating function comes out of the algebra below.

The core with no boundary at all is a sixth plastic family: the **prime castles of height 3** by area ([[prime-castles](pages/prime-castles.md)]) have every column of height 2 or 3 and some 3, so they are the compositions into 2s and 3s other than the all-2 ones, `P(A + 3) − 1` for even `A` and `P(A + 3)` for odd `A`.[^exec]

## Three bijections onto the maximal castles

Each map below is a bijection, checked exhaustively at every size listed.[^exec]

**Ridge castles of area `A` → maximal castles of width `A − 1`.** Read the ridge castle's cells column by column, bottom to top, and write one new column per cell: height 2 if another cell sits on top of it, height 1 otherwise. Drop the last new column, which is always 1. A height-2 column becomes `2, 1` and a height-1 column becomes `1`; a gap of 3 in the image would need two adjacent height-1 columns in the ridge castle, which the ridge rule forbids. Example: `(2, 1, 2, 2, 1)` (area 8) becomes `(2, 1, 1, 2, 1, 2, 1)` (width 7). Checked for `A = 2, …, 20`.

**The rule's castles of width `w` → maximal castles of width `w − 2`.** Every 3 becomes a column of height 2, and the one or two columns between consecutive 3s become that many columns of height 1. The opening `1, 2` is dropped. The tail after the last 3 decides the ends: tail `1` adds a height-1 column on the right, tail `2` one on the left, tail `1, 2` one on each side. Example: `(1, 2, 3, 2, 3, 1, 2, 3, 1, 2)` becomes `(1, 2, 1, 2, 1, 1, 2, 1)`. Checked for `w = 3, …, 20`.

**`(1, 2)`-RLL castles of width `w` → maximal castles of width `w + 2`, for `w ≥ 3`.** Add one column at each end: a height-1 column beside an end column of height 2, and a height-2 column beside an end column of height 1. An end run of 1 or 2 height-1 columns becomes a gap of 1 or 2 next to the new height-2 column. Example: `(1, 1, 2, 1, 2)` becomes `(2, 1, 1, 2, 1, 2, 1)`. Checked for `w = 3, …, 18`. At `w = 1, 2` the counts are 1 and 2 against 2 and 3, so the shift holds only from `w = 3`.

## The palindromic tree castles

A tree castle has no two adjacent columns both of height 2 or more ([[castle-classification-spectrum](pages/castle-classification-spectrum.md)]). By area the tree castles have denominator `1 − 2y + y² − y³`, whose reversed root is `ψ²` ([[tree-castle-by-area](pages/tree-castle-by-area.md)]). A palindrome is its left half, an optional middle column, and the left half reversed; the two copies of the half together have twice its area, so the half is counted with `y = x²`. Splitting by whether there is a middle column and by the half's last column: with no middle column the two copies of that last column stand side by side, so it must have height 1; with a middle column, a last column of height 2 or more forces the middle one to have height 1:

```
D(x) = T_1(x²) + x/(1 − x) + T_1(x²) · x/(1 − x) + T_b(x²) · x  =  x (1 + x)² / (1 − x² − x³)
```

with `T_1(y) = y (1 − y + y²) / (1 − 2y + y² − y³)` and `T_b(y) = y² / (1 − 2y + y² − y³)` the tree castles by area whose last column has height 1, and height 2 or more.[^exec] At `y = x²` the denominator factors,

```
1 − 2x² + x⁴ − x⁶  =  (1 − x² − x³)(1 − x² + x³),
```

and the factor `1 − x² + x³` cancels from the sum. The factorization is the polynomial form of `ψ²` being the square of `ψ`: `(x³ − x − 1)(x³ − x + 1) = x⁶ − 2x⁴ + x² − 1`, whose roots are `±` the roots of `x³ − x − 1`. So halving the ψ² family of all tree castles gives a ψ family, and its generating function is the maximal castles' exactly.

## Open threads

1. **A bijection for the palindromic tree castles.** They have the maximal castles' generating function at every size, but no map between them is written down; the cancellation of `1 − x² + x³` suggests the map is not block by block.

## Related Concepts

- [[golden-silver-bronze-plastic-castles](pages/golden-silver-bronze-plastic-castles.md)] - the five families in the four-constant grid.
- [[plastic-number](pages/plastic-number.md)] - `ψ`, `ψ²` and the Padovan and Perrin numbers.
- [[fibonacci-castles-sub-families](pages/fibonacci-castles-sub-families.md)] - maximal castles and the run-length-limited castles.
- [[ridge-castle](pages/ridge-castle.md)] - golden by width and plastic by area at height 2.
- [[tree-castle-by-area](pages/tree-castle-by-area.md)] - the tree castles by area, the `ψ²` family that the palindromes halve.

## Footnotes

[^exec]: Verified by execution (Python 3.10, SymPy, 2026-10-11): `bin/python/padovan_families.py`, run log `bin/python/padovan_families-run.log`. Each family enumerated by brute force (castles of width or area `n`); the series of each generating function above equals the counts for `n = 1, …, 18`. The three maps are injective with image exactly the maximal castles of the stated width, for ridge area `A = 2, …, 20`, rule width `w = 3, …, 20` and `(1, 2)`-RLL width `w = 3, …, 18`. Prime castles of height 3 by brute force for `A = 1, …, 20`. `T_1`, `T_b` and `D(x)` by solving `T_1 = y(1 + T_1 + T_b)`, `T_b = (y²/(1 − y))(1 + T_1)` and simplifying; the factorization by `sp.factor`. Padovan values from https://oeis.org/A000931/b000931.txt (fetched 2026-10-10).
