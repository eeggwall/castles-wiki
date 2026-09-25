---
title: Minimum height for a quadratic growth constant
category: Analyses
summary: For each quadratic growth constant - the larger root of x^2 - p1 x - p2 - the smallest height h at which some 0/1 castle-strip rule (which column heights may follow which) grows at exactly that rate. Exact answer for every pair with minimum height up to 6, from an exhaustive census of all 0/1 rule tables up to 6 x 6 (2^36 tables at height 6, cut to 1.28 billion by sorting rows; 758,878 distinct characteristic polynomials), which finds 53 pairs. Three results proved - (1) height > growth, so h >= floor(growth) + 1, exact whenever the second root is small; (2) the metallic line: min height (p1, 1) = p1 + 1 for every p1, so nickel first appears at height 6; (3) the square-root line: min height (0, p2) = ceil(2 sqrt p2), by a Perron-Frobenius period-2 argument for the lower bound and a rank-one two-group construction for the upper. One conjecture - every pair reaches its minimum height with a rule whose heights split into at most three evenly connected groups. Two groups are optimal for 47 of the 53 pairs (all six misses have p2 = 5 or 7, a prime forcing a lopsided split); three groups match all 53 and never undercut the exhaustive search. The conjecture turns min height into a finite search; its predicted table through height 9 is given. Open - a proof, or a height-7 counterexample; a closed form for p1 > 0, where ceil(2 sqrt p2) is no longer a lower bound ((2, 13) is built at height 7).
tags: [analysis, castle, castle-strip, transfer-matrix, perron-frobenius, growth-constant, quadratic-field, metallic-means, min-height, equitable-partition, census, exhaustive-search, conjecture, implementation, verification]
sources: [oeis-mining-pe502]
created: 2026-09-25
updated: 2026-09-25
---

# Minimum height for a quadratic growth constant

## The question in plain words

A **castle strip** is a row of columns with heights `1..h`, together with a rule saying which heights may stand next to each other. The rule is an `h x h` table of 0s and 1s: a 1 in row `a`, column `b` means "a column of height `a` may be followed by one of height `b`" ([[castle-strip](pages/castle-strip.md)]). The number of strips of width `L` obeying the rule grows like `ρ^L`, and `ρ` - the **growth constant** - is the table's largest eigenvalue.

When `ρ` is a quadratic number, it is the larger root of

```
x^2 - p1 x - p2          ρ = (p1 + sqrt(p1^2 + 4 p2)) / 2
```

which is the recurrence `a(L) = p1 a(L-1) + p2 a(L-2)`: build a row by adding one column in `p1` ways or two columns in `p2` ways, like tiling with squares in `p1` colours and dominoes in `p2` colours. Golden is `(1, 1)`, the metallic means are the `p2 = 1` line ([[metallic-means](pages/metallic-means.md)]), and [[reachable-field-census](pages/reachable-field-census.md)] showed that every pair is the growth constant of some 0/1 rule at some height.

This page asks: **what is the smallest height `h` that can do it?** Three lines of the answer are proved here, the rest is computed exactly up to height 6, and one conjecture covers everything computed so far.

## Terms used on this page

- **Pair** - the two integers `(p1, p2)`. Only pairs where `p1^2 + 4 p2` is not a perfect square are in scope (otherwise `ρ` is a whole number), and `p2` may be negative, as for `phi^2`, which is `(3, -1)`.
- **Conjugate** - the other root, `(p1 - sqrt(p1^2 + 4 p2))/2`. It is always an eigenvalue of the same table.
- **Min height** - the smallest `h` for which some `h x h` 0/1 table has growth constant exactly `ρ`.
- **Evenly connected groups** (an equitable partition) - a split of the heights into groups such that every height in a group has the same number of allowed successors in each group. The small table of those counts has the same growth constant as the full table.

## The exact census

Every 0/1 table up to 6 x 6 was generated and its characteristic polynomial computed exactly in integers. Reordering the heights does not change the polynomial, so at height 6 only tables with rows sorted by number of 1s were needed: 1.28 billion of the `2^36`. Each distinct polynomial was checked for a factor `x^2 - p1 x - p2` carrying its largest root, with the division done exactly.[^exec]

| height | distinct characteristic polynomials | pairs whose min height is this |
|---|---|---|
| 2 | 6 | 1 |
| 3 | 32 | 4 |
| 4 | 333 | 9 |
| 5 | 8,927 | 15 |
| 6 | 758,878 | 24 |

As checks, heights 2 to 4 reproduce the grid on [[reachable-field-census](pages/reachable-field-census.md)], and every pair found at height 5 or less appears again in the height-6 run (a smaller table padded with an empty row and column has the same growth constant). Min height for all 53 pairs, by `p1` (rows) and `p2` (columns); `·` marks a square discriminant:

```
p1\p2   -7  -6  -5  -4  -3  -2  -1 |  1   2   3   4   5   6   7   8   9
  0                                |  ·   3   4   ·   5   5   6   6   ·
  1                                |  2   ·   4   4   5   ·   6   6   6
  2                                |  3   3   ·   4   5   5   6   ·   6
  3                            3   |  4   4   4   ·   5   5   6   6   6
  4                        4   4   |  5   5   5   5   ·   6   6   6
  5            5   ·   5   5   5   |  6   6   6   6   6
  6    6   6   ·   6   6   6   6   |
```

Blank cells with a lower bound of 6 or less were not realized by height 6; their min height is at least 7.

## Three proved results

### 1. The general lower bound: height > growth

An `h x h` table of 0s and 1s has at most `h` ones per row, so its largest eigenvalue is at most `h`, with equality only for the all-ones table, whose growth `h` is a whole number. A quadratic `ρ` is irrational, so

```
min height  >=  floor(ρ) + 1
```

In the census this is exact whenever the conjugate is smaller than about 1 in size (the whole lower-left of the grid), and it falls behind as `p2` grows: `(1, 3)` has `ρ = 2.30` and bound 3 but needs height 4.

### 2. The metallic line: min height `(p1, 1) = p1 + 1`

The metallic mean `δ_a` sits strictly between `a` and `a + 1`, so bound 1 gives height at least `a + 1`, and the plateau-free-except-ceiling rule `J - D` realizes `δ_a` at exactly height `a + 1` ([[metallic-strip-realizability](pages/metallic-strip-realizability.md)]). So **min height `(a, 1) = a + 1` for every `a`.** In particular nickel, `(5+√29)/2 = 5.19`, first appears at height 6; the census confirms it there and not before.

### 3. The square-root line: min height `(0, p2) = ceil(2 sqrt p2)`

Here `ρ = sqrt p2` and the conjugate is `-sqrt p2`, the same size.

*Lower bound.* The growth constant of a table is the growth constant of one of its irreducible blocks (a set of heights that can all reach each other). By Perron-Frobenius, an irreducible nonnegative matrix with two eigenvalues of largest size, `ρ` and `-ρ`, has period 2: its heights split into groups `A` and `B`, and every allowed step goes from one group to the other. Two steps take `A` back to `A`, and the two-step table on `A` has growth `ρ^2 = p2`. Each row of that two-step table counts paths `A -> B -> A` from one height, which is at most `|B| · |A|`. So `p2 <= |A| · |B|`, and the smallest `|A| + |B|` with `|A| · |B| >= p2` is `ceil(2 sqrt p2)`.

*Construction.* Take `|A| = a` and `|B| = b` with `a b >= p2`. Allow every step from `A` to `B`, and exactly `p2` steps from `B` to `A` in total, spread any way at all. Every height in `A` then reaches every height in `B`, so every row of the two-step table on `A` equals the same vector of counts. The two-step table has rank one, and its growth is the sum of that vector: exactly `p2`.

```
(0, 5) at height 5:   A = {1, 2}, B = {3, 4, 5}
   00111        1, 2 may be followed by any of 3, 4, 5
   00111
   11000        3 and 4 may be followed by 1 or 2
   11000        5 may be followed by 1 only       -> 5 steps from B to A
   10000        characteristic polynomial  x^3 (x^2 - 5)
```

Checked against the table for every non-square `p2` up to 20.

## The three-group conjecture

The rank-one construction is a special case of **evenly connected groups**. With two groups of sizes `a` and `b`, where each height in the first group has `α` successors in the first and `β` in the second, and each in the second has `γ` in the first and `δ` in the second, the growth constant is the larger root of `x^2 - (α + δ) x + (α δ - β γ)`. So `p1 = α + δ` and `p2 = β γ - α δ`, at height `a + b`, subject to `α, γ <= a` and `β, δ <= b`. That is a small search, and it gives an upper bound for every pair.

- **Two groups** are optimal for 47 of the 53 exactly known pairs. All six misses - `(0,5)`, `(1,5)`, `(3,5)`, `(0,7)`, `(1,7)`, `(4,7)` - have `p2 = 5` or `7`. A prime `p2` forces `β γ` into a lopsided product, so one group has to be large.
- **Three groups** (the same construction with a 3 x 3 table of counts, whose characteristic polynomial is a cubic `(x - t)(x^2 - p1 x - p2)` with `ρ` the largest root) match **all 53** exact values, and never claim a height below what the exhaustive search found. The `(0, 5)` table above is three groups when read by columns (sizes 1, 1, 3), and the `(3, 5)` and `(4, 7)` optima are staircase tables: rows of 1s of lengths `5, 5, 5, 3, 2` and `6, 6, 6, 6, 4, 3`.

**Conjecture: every pair reaches its minimum height with a rule whose heights split into at most three evenly connected groups.** If it holds, min height is a finite search over small tables of counts. Its predicted values through height 9 (`*` = three groups beat the best two-group split):

```
p1\p2  1   2   3   4   5   6   7   8   9  10  11  12  13  14  15  16  17  18  19  20
  0    ·   3   4   ·   5*  5   6*  6   ·   7   7*  7   8*  8*  8   ·   9*  9   9*  9
  1    2   ·   4   4   5*  ·   6*  6   6   7   7*  ·   8*  8*  8   8   9*  9   9*  ·
  2    3   3   ·   4   5   5   6   ·   6   7   7   7   7*  8   ·   8   8*  9   9   9
  3    4   4   4   ·   5*  5   6   6   6   ·   7*  7   8   8   8   8   9*  ·   9*  9
  4    5   5   5   5   ·   6   6*  6   7   7   7*  ·   8   8*  8   8   9   9   9*  9
  5    6   6   6   6   6   ·   7*  7   7*  7   8   8   8*  ·   8   9   9*  9   9*  9
  6    7   7   7   7   7   7   ·   8   8*  8   8*  8   9   9   9   ·   9*  9
  7    8   8   8   8   8   8   8   ·   9   9   9*  9   9*  9
```

Through height 6 these are proved minima; beyond 6 they are upper bounds that the conjecture says are exact. The `p1 = 0` row agrees with result 3 everywhere, as it must.

## What is still open

- **A proof of the three-group conjecture, or a counterexample at height 7.** Exhaustive height 7 is about `10^12` tables even after sorting rows, so a test needs a targeted search on the pairs the conjecture puts at 8 or 9.
- **A closed form for `p1 > 0`.** Result 3 does not extend directly: `ceil(2 sqrt p2)` is not a lower bound once `p1 > 0`, since `(2, 13)` is built at height 7 where `ceil(2 sqrt 13) = 8`.
- **Min height of a field.** [[reachable-field-census](pages/reachable-field-census.md)] asks when a number field first appears; that is the minimum of this page's min height over all pairs with that field, which the table above answers for every field it covers.

## Related Concepts

- [[reachable-field-census](pages/reachable-field-census.md)] - the reachability law this page sharpens, and the census grid through height 5 it extends to 6.
- [[metallic-strip-realizability](pages/metallic-strip-realizability.md)] - the `J - D` rule that makes the metallic line exact.
- [[metallic-means](pages/metallic-means.md)] - the `p2 = 1` line.
- [[castle-strip](pages/castle-strip.md)] - castle strips and their 0/1 transfer tables.
- [[castle-classification-growth](pages/castle-classification-growth.md)] - growth constants as a classification axis.

## Appearances in Sources

- [[oeis-mining-pe502](pages/oeis-mining-pe502.md)] - the castle-strip count sequences whose growth constants are the Perron roots studied here.

## Footnotes

[^exec]: Verified by execution (2026-09-25). Census: a C program enumerating every 0/1 matrix of size 2 to 5, and every 6 x 6 matrix with row sums in nonincreasing order (1,277,642,344 matrices, 18 s on 14 processes), computing the characteristic polynomial exactly in 64-bit integers by the Faddeev-LeVerrier recursion and keeping the distinct ones. For each polynomial, the largest real root `ρ` was found numerically; every candidate `x^2 - p1 x - p2` with `p1 = round((ρ^2 - p2)/ρ)`, `-60 <= p2 <= 60`, non-square discriminant and larger root `ρ` was confirmed by exact polynomial division. Every height-5 pair reappeared in the height-6 run. Two- and three-group constructions: exhaustive over group sizes summing to at most 9 and all count tables with entries bounded by the group sizes, with the three-group cubic split into an integer root times the quadratic and `ρ` required to be the largest root. All quoted numbers are the programs' printed output.
