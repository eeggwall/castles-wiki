---
title: Minimum height for a quadratic growth constant
category: Analyses
summary: For each quadratic growth constant ρ, the larger root of x² − p₁x − p₂, the smallest height h at which some 0/1 castle-strip rule on h heights has Perron root exactly ρ. The exact minimum height is known for the 53 pairs with minimum height at most 6, from a census of all 0/1 matrices up to 6 × 6 (1.28 billion at height 6 after sorting rows; 758,878 distinct characteristic polynomials). Four results are proved. (1) The minimum height exceeds ρ, so it is at least ⌊ρ⌋ + 1; the bound is attained for 31 of the 53 pairs. (2) On the line p₂ = 1, the minimum height of δ_a is a + 1, so δ_5 first appears at height 6. (3) On the line p₁ = 0, the minimum height of √p₂ is ⌈2√p₂⌉, by a period-2 Perron-Frobenius argument for the lower bound and a rank-one construction with two groups of heights for the upper. (4) For 1 ≤ p₂ ≤ p₁, the minimum height is p₁ + 1, by a construction with two groups of heights. Rules whose heights split into at most three evenly connected groups attain the minimum height of all 53 pairs, and two groups attain it for 47; the upper bounds that such rules give through height 9 are tabulated.
tags: [analysis, castle, castle-strip, transfer-matrix, perron-frobenius, growth-constant, quadratic-field, metallic-means, min-height, equitable-partition, census, exhaustive-search, implementation, verification]
sources: [pe502-pell-castle-strip]
created: 2026-09-25
updated: 2026-10-16
---

# Minimum height for a quadratic growth constant

## The question

A castle strip on the heights `1, …, h` is a skyline with column heights in `{1, …, h}`, under a rule saying which height may follow which; strips need not reach height `h`, so they need not be castles of height `h` ([[castle-strip](pages/castle-strip.md)]). The rule is an `h × h` matrix `M` of 0s and 1s, with a 1 in row `a`, column `b` when a column of height `a` may be followed by one of height `b`. The number of strips of width `w` grows like `ρ^w`, where `ρ`, the **growth constant**, is the Perron root of `M`, its largest eigenvalue.

When `ρ` is a quadratic irrational, it is the larger root of

```
x² − p₁x − p₂,          ρ = (p₁ + √(p₁² + 4p₂)) / 2,
```

the characteristic polynomial of the recurrence `a(L) = p₁ a(L − 1) + p₂ a(L − 2)`. For `p₁, p₂ ≥ 0`, `a(L)` counts the tilings of a row of length `L` by squares in `p₁` colors and dominoes in `p₂` colors. The golden mean is `(1, 1)`; for `p₁, p₂ ≥ 1` the root is de Spinadel's metallic mean `σ_{p₁}^{p₂}`, and the `δ_a` are the line `p₂ = 1` ([[metallic-means](pages/metallic-means.md)]). Every pair with `p₁ ≥ 0` and `p₂ ≥ 1` is the Perron root of some 0/1 matrix ([[reachable-field-census](pages/reachable-field-census.md)]).

This page finds the smallest height that realizes each pair. A general lower bound, two lines and a triangle of the answer are proved, and the rest is computed exactly up to height 6.

## Terms used on this page

- **Pair** - the two integers `(p₁, p₂)`, with `p₁² + 4p₂` not a perfect square (otherwise `ρ` is an integer). `p₂` may be negative, as for `φ²`, the pair `(3, −1)`.
- **Conjugate** - the other root, `(p₁ − √(p₁² + 4p₂))/2`. It is an eigenvalue of every matrix that has `ρ` as an eigenvalue, since `x² − p₁x − p₂` is irreducible.
- **Min height** - the smallest `h` for which some `h × h` 0/1 matrix has Perron root exactly `ρ`.
- **Evenly connected groups** (an equitable partition) - a split of the heights into groups such that every height in a group has the same number of allowed successors in each group. The matrix of those counts, the **quotient**, has the same Perron root as `M`.

## The exact census

Every 0/1 matrix up to `6 × 6` was generated and its characteristic polynomial computed exactly in integers. Relabeling the heights, `M → PMPᵀ`, does not change the characteristic polynomial, so at height 6 only matrices with rows in nonincreasing order of their number of ones were needed: 1,277,642,344 of the `2^{36}`. Each distinct polynomial was tested for a factor `x² − p₁x − p₂` carrying its largest root, by exact division.[^exec]

| height | distinct characteristic polynomials | pairs whose min height is this |
|---|---|---|
| 2 | 6 | 1 |
| 3 | 32 | 4 |
| 4 | 333 | 9 |
| 5 | 8,927 | 15 |
| 6 | 758,878 | 24 |

Every pair found at height 5 or less appears again at height 6, since a smaller matrix padded with a zero row and column has the same Perron root. Min height for all 53 pairs, by `p₁` (rows) and `p₂` (columns); `·` marks a square discriminant:

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

A blank cell whose lower bound (result 1) is 6 or less was not realized by height 6, so its min height is at least 7.

## Four proved results

### 1. The general lower bound: height > growth

A 0/1 matrix of size `h` has at most `h` ones in each row, and its Perron root is at most its largest row sum, so `ρ ≤ h`; equality needs a row sum `h` in every row of the strongly connected part carrying `ρ`, which makes `ρ = h` an integer. A quadratic `ρ` is irrational, so

```
min height  ≥  ⌊ρ⌋ + 1.
```

The bound is attained for 31 of the 53 pairs. Every pair whose conjugate has absolute value at most 1.25 attains it, and `(6, −6)`, whose conjugate `3 − √3 = 1.27` is slightly larger, does not. `(1, 3)` has `ρ = 2.30`, conjugate `−1.30` and bound 3, and needs height 4.[^exec]

### 2. The δ_a line: min height of (a, 1) is a + 1

`δ_a` lies strictly between `a` and `a + 1`, so result 1 gives height at least `a + 1`, and the ridge matrix `R_h = J − D` (neighboring columns may have equal height only at the ceiling `h`) has Perron root `δ_{h−1}` ([[metallic-strip-realizability](pages/metallic-strip-realizability.md)], [[ridge-castle](pages/ridge-castle.md)]). So **the min height of `(a, 1)` is `a + 1` for every `a ≥ 1`.** In particular `δ_5 = (5 + √29)/2 = 5.19` first appears at height 6, which the census confirms.

### 3. The square-root line: min height of (0, p₂) is ⌈2√p₂⌉

Here `ρ = √p₂` and the conjugate is `−√p₂`, of the same absolute value.

*Lower bound.* The Perron root of `M` is the Perron root of one of its strongly connected parts (a set of heights that can all reach each other), and that part has the integer characteristic polynomial of a principal submatrix, so it also has the eigenvalue `−√p₂`. By the Perron-Frobenius theorem, an irreducible nonnegative matrix whose eigenvalues of largest absolute value include `ρ` and `−ρ` has even period, so its heights split into two groups `A` and `B` with every allowed step going from one group to the other. Two steps take `A` back to `A`, and the two-step matrix on `A` has Perron root `ρ² = p₂`. Each row sum of that two-step matrix counts paths `A → B → A` from one height, at most `|B|·|A|` of them, so `p₂ ≤ |A|·|B|`. The smallest `|A| + |B|` with `|A|·|B| ≥ p₂` is `⌈2√p₂⌉`, since `s` heights split into groups of sizes `⌊s/2⌋` and `⌈s/2⌉` have product `⌊s²/4⌋`.

*Construction.* Take `|A| = a` and `|B| = b` with `ab ≥ p₂`. Allow every step from `A` to `B`, and exactly `p₂` steps from `B` to `A` in total, placed anywhere. Every height in `A` then reaches every height in `B`, so every row of the two-step matrix on `A` is the same vector of counts. That matrix has rank one, and its Perron root is the sum of the vector: exactly `p₂`.

```
(0, 5) at height 5:   A = {1, 2}, B = {3, 4, 5}
   00111        1, 2 may be followed by any of 3, 4, 5
   00111
   11000        3 and 4 may be followed by 1 or 2
   11000        5 may be followed by 1 only       -> 5 steps from B to A
   10000        characteristic polynomial  x³(x² − 5)
```

The construction gives `⌈2√p₂⌉` for every non-square `p₂ ≤ 20`.[^exec] The bound does not carry over to `p₁ > 0`: `(2, 13)` is realized at height 7, where `⌈2√13⌉ = 8`.

### 4. The triangle 1 ≤ p₂ ≤ p₁: min height p₁ + 1

Fix `p₁ = n ≥ 1`. For `1 ≤ p₂ ≤ n`, `ρ` lies strictly between `n` and `n + 1`: `ρ > n` because `p₂ > 0`, and `ρ < n + 1` exactly when `n² + 4p₂ < (n + 2)²`, that is `p₂ < n + 1`. The discriminant `n² + 4p₂` lies strictly between `n²` and `(n + 2)²`, and it equals `(n + 1)²` only if `4p₂ = 2n + 1`, which is odd, so it is never a square. At `p₂ = n + 1` the polynomial factors as `(x − (n + 1))(x + 1)` and `ρ = n + 1`. So the row `p₁ = n` of the grid begins with exactly `n` pairs `(n, 1), …, (n, n)` with `⌊ρ⌋ = n`, followed by a square discriminant.

*Lower bound.* Result 1, since `ρ > n`.

*Construction.* Use the heights `1, …, n + 1`. Each of the heights `1, …, n` may be followed by any height; height `n + 1` may be followed by `p₂` of the heights `1, …, n` and not by itself. The groups `{1, …, n}` and `{n + 1}` are evenly connected, with quotient `[[n, 1], [p₂, 0]]` and characteristic polynomial `x² − nx − p₂`. The first `n` rows of the matrix are equal, so it has rank at most 2, and its characteristic polynomial is `x^{n−1}(x² − nx − p₂)`.

```
(3, 2) at height 4:
   1111        1, 2, 3 may be followed by any height
   1111
   1111
   1100        4 may be followed by 1 or 2 only
   characteristic polynomial  x²(x² − 3x − 2)
```

**So the min height of `(p₁, p₂)` is `p₁ + 1` for every `1 ≤ p₂ ≤ p₁`.** At `p₂ = 1` this is result 2 again, by a different matrix from the ridge matrix. In the census grid the triangle is the 15 pairs with `p₁ ≤ 5` and `1 ≤ p₂ ≤ p₁`, and the table of the next section shows it for `p₁ = 6` and `7`.[^tri]

## Rules with two or three evenly connected groups

The rank-one construction is a rule with two evenly connected groups. In general, with two groups of sizes `a` and `b`, where each height in the first group has `α` successors in the first and `β` in the second, and each height in the second has `γ` in the first and `δ` in the second, the Perron root is the larger root of `x² − (α + δ)x + (αδ − βγ)`. So `p₁ = α + δ` and `p₂ = βγ − αδ` at height `a + b`, subject to `α, γ ≤ a` and `β, δ ≤ b`. Every such table of counts is realized by a 0/1 matrix, and the search over tables is small, so it gives an upper bound for every pair.

- **Two groups** attain the min height for 47 of the 53 pairs. The six they miss, `(0, 5)`, `(1, 5)`, `(3, 5)`, `(0, 7)`, `(1, 7)` and `(4, 7)`, have `p₂ = 5` or `7`; in each, `βγ = p₂ + αδ` has no factorization whose factors fit into groups of total size the min height.
- **Three groups** (a `3 × 3` table of counts, whose characteristic polynomial is `(x − t)(x² − p₁x − p₂)` with `ρ` the largest root) attain the min height of all six, and no construction with at most three groups goes below a min height of the census. The `(0, 5)` rule of result 3 has three evenly connected groups by successors, `{1, 2}`, `{3, 4}` and `{5}`, with quotient `[[0, 2, 1], [2, 0, 0], [1, 0, 0]]` and characteristic polynomial `x(x² − 5)`. The `(3, 5)` and `(4, 7)` optima are staircase matrices, whose row `i` has ones in its first `ℓ_i` columns: `ℓ = 5, 5, 5, 3, 2` with characteristic polynomial `x³(x² − 3x − 5)`, and `ℓ = 6, 6, 6, 6, 4, 3` with `x⁴(x² − 4x − 7)`.[^exec]

So for every pair with min height at most 6, some rule with at most three evenly connected groups attains the min height. The heights that such rules reach through height 9 (`*` where three groups beat the best two-group rule):

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

Through height 6 these are the exact min heights; above 6 they are upper bounds. The row `p₁ = 0` agrees with result 3 everywhere. The min height of a number field is the minimum over the pairs whose discriminant has that field's squarefree part; [[reachable-field-census](pages/reachable-field-census.md)] uses the table that way for `Q(√10)` and `Q(√11)`, which first appear at height 6.

## Related Concepts

- [[reachable-field-census](pages/reachable-field-census.md)] - the number fields of strip Perron roots through height 5, and the proof that every pair with `p₂ ≥ 1` is realized at some height.
- [[area-growth-census](pages/area-growth-census.md)] - the same rules counted by area instead of width, with its own minimum heights.
- [[metallic-strip-realizability](pages/metallic-strip-realizability.md)] and [[ridge-castle](pages/ridge-castle.md)] - the ridge matrix `R_h = J − D`, which realizes the line `p₂ = 1`.
- [[metallic-means](pages/metallic-means.md)] - de Spinadel's `σ_p^q`, the quadrant `p₁, p₂ ≥ 1`, with the `δ_a` on its line `p₂ = 1`.
- [[castle-strip](pages/castle-strip.md)] - castle strips and their 0/1 transfer matrices.
- [[castle-classification-growth](pages/castle-classification-growth.md)] - growth types of castle families by width and by the other axes.

## Appearances in Sources

- [[pe502-pell-castle-strip](pages/pe502-pell-castle-strip.md)] - the transfer-matrix model of strips whose Perron roots this page studies.

## Footnotes

[^exec]: Census (2026-09-25): a C program enumerating every 0/1 matrix of size 2 to 5, and every `6 × 6` matrix with row sums in nonincreasing order (1,277,642,344 matrices), computing the characteristic polynomial exactly in 64-bit integers by the Faddeev-LeVerrier recursion and keeping the distinct ones; for each polynomial, every candidate `x² − p₁x − p₂` with `−60 ≤ p₂ ≤ 60`, non-square discriminant and larger root the largest real root was confirmed by exact polynomial division. Rechecked by execution (Python 3.11 with NumPy and SymPy, 2026-10-16): the full census through height 5 (6, 32, 333 and 8,927 characteristic polynomials; 1, 4, 9 and 15 pairs new at heights 2 to 5, as in the grid); the lower bound attained for 31 of the 53 pairs, every pair with conjugate of absolute value at most 1.25 among them, and missed by `(6, −6)` (conjugate 1.27) and by `(1, 3)`; all two-group tables with group sizes summing to at most 9 and all three-group tables with sizes summing to at most 9, which reproduce the six two-group misses, attain every min height of the grid including the 24 pairs of height 6, never go below it, give `(2, 13)` at height 7, and reproduce the table through height 9 entry for entry; the `(0, 5)` matrix, its quotient, and the two staircase matrices. The height-6 enumeration itself was not rerun, so the 758,878 polynomials and the blank cells at height 6 rest on the 2026-09-25 run.
[^tri]: Verified by execution (Python 3.11 with SymPy, 2026-10-16): for every `1 ≤ n ≤ 12` and `1 ≤ p₂ ≤ n`, the `(n + 1) × (n + 1)` matrix of result 4 has characteristic polynomial exactly `x^{n−1}(x² − nx − p₂)`, its larger root lies in `(n, n + 1)`, and `n² + 4p₂` is not a square; the grid entries with `p₁ ≤ 5` and `1 ≤ p₂ ≤ p₁` all read `p₁ + 1`.
