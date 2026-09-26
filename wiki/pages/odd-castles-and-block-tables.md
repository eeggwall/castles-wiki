---
title: The odd castles and the block-count tables
category: Analyses
summary: "The last part of the castle sequence bank. The odd count odd(w,h) = A - F gets its own rows: odd(w,h) = (A + P(h-1,w) - P(h-2,w))/2, with the same characteristic polynomial as F(w,h) for every h from 4 to 7. It differs only at h = 2 (odd gains the root 1) and h = 3 (odd loses the root 2, so its order is 5 against 6). The ten parity-refined area sequences and their signed differences were searched against OEIS on 2026-09-26, with no match. Three joint tables were enumerated. By area and blocks, the b-block column is rational with denominator (1-q)^2...(1-q^(b-1))^2 (1-q^b) for b <= 4; the pattern breaks at b = 5. By area, blocks and peaks, two blocks give the quarter-squares A002620, three blocks with one peak A097701, and three blocks with two peaks A002624, all three interlinks. By (w,h) and blocks, the h-block column is the convex count C(N, 2h-2) with N = w+2h-3, the (h+1)-block column is (2h-3) C(N, 2h), and the (h+2)-block column is a three-term binomial sum."
tags: [analysis, castle, oeis, sequence, odd-count, parity, area, block-count, peaks, joint-distribution, c-finite, binomial, interlink, novel-candidate, verification]
sources: [oeis-mining-pe502]
created: 2026-09-26
updated: 2026-09-26
---

# The odd castles and the block-count tables

## What this closes

The first mining pass on [[oeis-mining-pe502](pages/oeis-mining-pe502.md)] covered `F`, `A = h^w - (h-1)^w` and the signed tower count `P`. Three things were left over. The odd count `odd(w,h) = A(w,h) - F(w,h)` had no record of its own. The parity-refined area sequences of [[castle-by-area](pages/castle-by-area.md)] were marked "none in OEIS" with no dated search. And the joint distributions of block count, peaks and area had been enumerated only one pair at a time: area and peaks on [[castle-row-raising-equation](pages/castle-row-raising-equation.md)], and area and blocks only as a generating function (GF) on [[castle-q-bessel-closed-form](pages/castle-q-bessel-closed-form.md)]. This page closes all three. The records go into [[castle-sequence-catalogue](pages/castle-sequence-catalogue.md)].

The statistics are the wiki's standard ones. Blocks are `B(c) = c_1 + sum_{i>=2} max(0, c_i - c_{i-1})` ([[castle-sign](pages/castle-sign.md)]). A peak is a maximal run of columns with `c_i >= 2` ([[castle-foata-transform](pages/castle-foata-transform.md)], [[prime-castles](pages/prime-castles.md)]). Area is `sum c_i`. By area, a castle is any composition; by `(w, h)`, it is a PE 502 castle with maximum exactly `h`. Every number below was computed while writing and checked two ways: brute force over compositions and skylines, and transfer-matrix dynamic programming (DP).[^exec] Every OEIS status is from a search on 2026-09-26.[^search]

## The odd count as its own entry

A castle is a full base row with a tower of heights `0..h-1` on top, so its block count is one more than the tower's. That gives `sum (-1)^blocks = P(h-2, w) - P(h-1, w)` over castles of maximum exactly `h`, with `P(k, L)` the signed tower count of [[signed-tower-count](pages/signed-tower-count.md)]. Halving the difference from `A`:

```
odd(w, h) = (A(w, h) + P(h-1, w) - P(h-2, w)) / 2
F(w, h)   = (A(w, h) - P(h-1, w) + P(h-2, w)) / 2
```

At `h = 3` this is `F(w,3) = (3^w - 2^w - P(2,w) + P(1,w))/2`, the closed form of [[new-sequence-fw3](pages/new-sequence-fw3.md)].[^exec]

The rows, from `w = 1`:

| `h` | `odd(w, h)` | order | characteristic polynomial |
|---|---|---|---|
| 2 | `0, 0, 1, 5, 15, 35, 71, 135, 255, 495, 991, 2015` | 4 | `(x-2)(x-1)(x^2-2x+2)` |
| 3 | `1, 5, 16, 44, 122, 358, 1082, 3274, 9850, 29546, 88594` | 5 | `(x-3)(x^2-2x+2)(x^2-x+2)` |
| 4 | `0, 0, 6, 58, 342, 1638, 7134, 29774, 121990, 495910` | 9 | `(x-4)(x-3)(x-2)(x^2-x+2)(x^4-4x^3+8x^2-8x+8)` |
| 5 | `1, 9, 51, 247, 1195, 6051, 31467, 164115, 850379` | 11 | `(x-5)(x-4)(x^2-2x+4)(x^3-3x^2+2x-4)(x^4-4x^3+8x^2-8x+8)` |
| 6 | `0, 0, 15, 223, 2021, 14905, 100157, 645029, 4069173` | 13 | `(x-6)(x-5)(x^2-2x+4)(x^3-3x^2+2x-4)(x^6-6x^5+18x^4-32x^3+48x^2-32x+32)` |
| 7 | `1, 13, 106, 738, 5124, 37128, 275804, 2053324` | 15 | `(x-7)(x-6)(x^3-4x^2+4x-8)(x^4-3x^3+8x^2-4x+8)(x^6-6x^5+18x^4-32x^3+48x^2-32x+32)` |

The `h = 2` row is `A038503(w+1) - 1`, as on [[oeis-height2-hyperbolic-castles](pages/oeis-height2-hyperbolic-castles.md)]. The rows for `h = 3..7` have no OEIS match: **novel-candidate**. The orders 5, 9 and 11 at `h = 3, 4, 5` agree with the first pass.[^exec][^search]

**Where odd and even part ways.** For `h = 4..7` the minimal characteristic polynomial of `odd(., h)` equals that of `F(., h)`, factor for factor. They differ only at `h = 2` and `h = 3`, where `(h-1)^w` from `A` meets an eigenvalue `h - 1` of one of the `P` terms. At `h = 3` the root 2 of `P(2, .)` enters `odd` with coefficient `+1/2` and cancels the `-2^w/2` from `A`, so `odd(., 3)` has order 5 while `F(., 3)` has order 6. At `h = 2` it goes the other way: the constant `P(0, w) = 1` cancels the `-1^w` of `A` in `F` and doubles it in `odd`, so `odd` has the extra root 1. From `h = 4` on, no `P(k, .)` with `k = h-1` or `h-2` has the integer eigenvalue `h - 1` (checked through `h = 7`), so nothing cancels and both rows have order `2h + 1`.[^exec]

**Columns.** At fixed `w` the counts are quasi-polynomials in `h` that alternate by the parity of `h`. The `w = 3` column is on [[sum-of-three-cubes-castles](pages/sum-of-three-cubes-castles.md)] and `F(4, h)` is in the catalogue. The new columns, from `h = 1`:

| column | first terms | status |
|---|---|---|
| `odd(4, h)` | `1, 5, 44, 58, 247, 223, 738, 564, 1645, 1145, 3096, 2030` | **novel-candidate** (also its even-`h` and odd-`h` halves) |
| `odd(5, h)` | `1, 15, 122, 342, 1195, 2021, 5124, 6924, 14901, 17755, 34606` | **novel-candidate** |
| `odd(6, h)` | `1, 35, 358, 1638, 6051, 14905, 37128, 69196, 140709, 224143` | **novel-candidate** |
| `F(5, h)` | `0, 16, 89, 439, 906, 2630, 3907, 9037, 11380, 23196, 26445` | **novel-candidate** |
| `F(6, h)` | `0, 28, 307, 1729, 5478, 16126, 33865, 75299, 128588, 244416` | **novel-candidate** |

## The parity-refined area sequences

Each by-area family splits by block parity. Terms from `n = 1`:[^exec]

| name | castles of area `n` | first terms | sum |
|---|---|---|---|
| `even` | all, even blocks | `0, 1, 2, 5, 8, 17, 30, 65, 122, 261, 502, 1043, 2026, 4145, 8124, 16499` | `even + odd = 2^(n-1)` |
| `odd` | all, odd blocks | `1, 1, 2, 3, 8, 15, 34, 63, 134, 251, 522, 1005, 2070, 4047, 8260, 16269` | |
| `cev` | convex, even | `0, 1, 2, 5, 8, 15, 24, 41, 64, 105, 162, 255, 386, 589, 874, 1300` | `cev + cod = A001523` |
| `cod` | convex, odd | `1, 1, 2, 3, 7, 12, 23, 38, 66, 104, 168, 257, 398, 594, 891, 1304` | |
| `valley_even` | valley, even | `0, 1, 2, 4, 6, 12, 16, 32, 40, 78, 98, 175, 224, 380, 488, 786` | sum `= A332578` |
| `valley_odd` | valley, odd | `1, 1, 2, 3, 7, 9, 20, 25, 51, 62, 119, 148, 261, 331, 551, 708` | |
| `nc_even` | non-convex, even | `0, 0, 0, 0, 0, 2, 6, 24, 58, 156, 340, 788, 1640, 3556, 7250, 15199` | sum `= A115981` |
| `nc_odd` | non-convex, odd | `0, 0, 0, 0, 1, 3, 11, 25, 68, 147, 354, 748, 1672, 3453, 7369, 14965` | |
| `sv_even` | strict valley, even | `0, 0, 0, 0, 0, 2, 2, 11, 12, 36, 44, 99, 126, 244, 316, 554` | sum `= strict_valley` |
| `sv_odd` | strict valley, odd | `0, 0, 0, 0, 1, 1, 6, 6, 22, 24, 63, 76, 159, 201, 375, 483` | |

A strict-valley castle is a valley that is not monotone. The first sixteen terms of `strict_valley` itself are `0, 0, 0, 0, 1, 3, 8, 17, 34, 60, 107, 175, 285, 445, 691, 1037`, and they agree with the first pass. All eleven sequences have no OEIS match. The same holds for the signed differences: `even - odd`, `cev - cod` (`-1, 0, 0, 2, 1, 3, 1, 3, -2, 1, -6, -2`), `valley_even - valley_odd` (`-1, 0, 0, 1, -1, 3, -4, 7, -11, 16, -21, 27`), `nc_even - nc_odd` and `sv_even - sv_odd`. The status of all of them is **novel-candidate**, now dated.[^search]

## Joint tables

### Area and blocks

`T(n, b)` counts castles of area `n` with `b` blocks. Rows from `n = 1`, for `b = 1..n`:

```
1
1  1
1  2   1
1  4   2   1
1  6   6   2   1
1  9  12   7   2  1
1 12  24  16   8  2  1
1 16  41  39  19  9  2  1
1 20  69  78  53 22 10  2 1
1 25 106 157 117 67 25 11 2 1
```

Row sums are `2^(n-1)`. The alternating row sums are `even(n) - odd(n)`. The rows are the coefficients of the trivariate GF on [[castle-q-bessel-closed-form](pages/castle-q-bessel-closed-form.md)] at unit width weight. The triangle read by rows has no OEIS match: **novel-candidate**.[^exec][^search]

With `b` fixed, a castle is one of finitely many nested arrangements of `b` intervals, and each arrangement contributes a rational GF in the area. So every column is rational. The columns found, checked to area 90:[^exec]

| `b` | column GF | first terms (`n = b..`) | status |
|---|---|---|---|
| 2 | `q^2 / ((1-q)^2 (1-q^2))` | `1, 2, 4, 6, 9, 12, 16, 20, 25, 30, 36` | **interlink** → [A002620](https://oeis.org/A002620) quarter-squares, `= A002620(n)` |
| 3 | `q^3 (1 + q^2 + q^3 + q^4) / ((1-q)^2 (1-q^2)^2 (1-q^3))` | `1, 2, 6, 12, 24, 41, 69, 106, 160, 229, 322` | **novel-candidate** |
| 4 | `q^4 N_4(q) / ((1-q)^2 (1-q^2)^2 (1-q^3)^2 (1-q^4))` | `1, 2, 7, 16, 39, 78, 157, 284, 502, 834, 1351` | **novel-candidate** |
| 5 | rational; smallest product denominator found `(1-q)(1-q^2)^2(1-q^3)^3(1-q^4)^2(1-q^5)` | `1, 2, 8, 19, 53, 117, 266, 540, 1078, 2011, 3659` | **novel-candidate** |

Here `N_4(q) = 1 + 2q^2 + 2q^3 + 6q^4 + 4q^5 + 7q^6 + 4q^7 + 4q^8 + 2q^9 + q^10`. For `b <= 4` the denominator is `(1-q)^2 ... (1-q^(b-1))^2 (1-q^b)`. At `b = 5` that denominator no longer clears the column. For every `b <= 6` the pole at `q = 1` has order `2b - 1`, so the `b`-block column grows like `n^(2b-2)`. The two-block case is elementary: a two-block castle is `1^a 2^m 1^c` with `m >= 1`, which leaves `floor(n^2/4)` choices.

### Area, blocks and peaks

Peaks refine the columns. Every castle with `p` peaks has at least `p + 1` blocks. Equality `b = p + 1` means every peak is a single block, which is exactly height at most 2, so that diagonal is the Fibonacci row of [[bounded-height-castles-nacci](pages/bounded-height-castles-nacci.md)]. The next cells, in castles of area `n`:[^exec][^oeis]

| blocks, peaks | first terms | identification | status |
|---|---|---|---|
| 2, 1 | `1, 2, 4, 6, 9, 12, 16, 20` (from `n = 2`) | `A002620(n)` | **interlink** (above) |
| 3, 1 | `1, 2, 5, 9, 16, 25, 39, 56, 80, 109, 147, 192` (from `n = 3`) | `A097701(n-3)`, "Expansion of `1/((1-x)^2*(1-x^2)^2*(1-x^3))`" | **interlink** |
| 3, 2 | `1, 3, 8, 16, 30, 50, 80, 120, 175, 245, 336, 448` (from `n = 5`) | `A002624(n-5)`, "Expansion of `(1-x)^(-3) * (1-x^2)^(-2)`" | **interlink** |
| 4, 1 | `1, 2, 5, 10, 20, 34, 60, 96, 153, 232, 348, 502` | | **novel-candidate** |
| 5, 1 | `1, 2, 5, 10, 22, 39, 74, 127, 219, 357, 582, 905` | | **novel-candidate** |
| 4, 2 | `2, 6, 18, 40, 84, 156, 278, 462, 744, 1146, 1722, 2508` | | **novel-candidate** |
| 5, 2 | `3, 9, 28, 66, 149, 297, 573, 1029, 1794, 2988, 4853, 7627` | | **novel-candidate** |

Both new interlinks agree with the OEIS data over the full length compared, through area 40. Neither entry has a composition or castle reading. The readings are direct. A three-block one-peak castle is a base, a block on it and a block on that. A three-block two-peak castle is a base carrying two separated one-block towers. The two-peak and three-block-one-peak GFs differ only by trading one `(1-q^3)` for a `(1-q)`.

### Width, height and blocks

At fixed `(w, h)` the blocks run from `h` (the convex castles, [[convex-castle-binomial-identity](pages/convex-castle-binomial-identity.md)]) up to a maximum reached by the battlement `h, 1, h, 1, ...`. The first pass named this table as new ([[tower-narayana-polynomial](pages/tower-narayana-polynomial.md)] holds the tower side). Its `h = 3` rows from `w = 1`, for blocks `3, 4, 5, ...`:

```
1
5
15    3    1
35   21    9
70   84   51    5    1
126  252  219   55   13
210  630  765  340  106   7   1
```

Each row sums to `3^w - 2^w`. At `h = 2` the entries are binomials, `C(w+1, 2b-2)`. For general `h`, set `N = w + 2h - 3`. Then the first three columns are, verified for `w <= 25` and `2 <= h <= 6`:[^exec]

```
blocks h     :  C(N, 2h-2)
blocks h + 1 :  (2h-3) C(N, 2h)
blocks h + 2 :  (2h-5) C(N, 2h) + 2(2h-5) C(N, 2h+1) + (2h+1)(h-2) C(N, 2h+2)      (h >= 3)
```

The first line is the convex count. The `b`-block column is a polynomial in `w` of degree `2b - 2`, the same exponent as the area column. The last entry of each row is `1` at odd `w` (the battlement alone) and `(h-1)w + 1` at even `w`. The second column at `h = 3` is **interlink** → [A253943](https://oeis.org/A253943), `a(n) = 3*binomial(n+1,6)`, at `n = w + 2`. The `h = 4` second column `5 C(w+5, 8)`, the `h = 3` third column `1, 9, 51, 219, 765, 2277, 5973`, and the `h = 3` and `h = 4` triangles have no OEIS match: **novel-candidate**.[^search][^oeis]

## Related Concepts

- [[castle-sequence-catalogue](pages/castle-sequence-catalogue.md)] - the bank these records enter.
- [[castle-by-area](pages/castle-by-area.md)] - the by-area families split by parity here.
- [[new-sequence-fw3](pages/new-sequence-fw3.md)] - `F(w,3)`, whose odd companion is the `h = 3` row above.
- [[signed-tower-count](pages/signed-tower-count.md)] - the `P(k, .)` terms in the odd-count formula.
- [[castle-row-raising-equation](pages/castle-row-raising-equation.md)] - the area and peaks triangle, the pair not repeated here.
- [[castle-q-bessel-closed-form](pages/castle-q-bessel-closed-form.md)] - the closed-form GF behind the area and blocks triangle.
- [[castle-conditional-entropy](pages/castle-conditional-entropy.md)] - the joint `(B, N)` distribution read as entropy.
- [[convex-castle-binomial-identity](pages/convex-castle-binomial-identity.md)] - the first column of the `(w, h)` block table.
- [[oeis-cross-referencing](pages/oeis-cross-referencing.md)] - the verify-with-offsets discipline used for the three interlinks.

## Footnotes

[^exec]: Verified by execution (2026-09-26), Python 3 with SymPy. `odd(w,h)` and `F(w,h)` by a column DP on (last height, block parity, maximum reached) for `w <= 44`, `h <= 7`. Minimal recurrences were found by linear solve and Berlekamp-Massey on 40 terms and then factored. The `P(k, L)` identity was brute-forced for `h <= 5`, `w <= 6`. The area families were brute-forced over all compositions of `n <= 20`. The area and blocks table came from an area DP on (last height, blocks) through area 45, and the columns `b <= 7` from the same DP through area 90, which served for the column GFs: each column was multiplied by product denominators `prod (1-q^j)^(m_j)`, `m_j <= 3`, and the result checked to be a polynomial of degree below 80. The area, blocks and peaks table came from a DP on (last height, blocks, peaks) through area 40. The `(w, h)` block table came from a DP on (last height, blocks, maximum reached) for `w <= 25`, `h <= 7`; its columns were solved exactly in the basis `C(N, k)` with zero residual, and the last-entry law was checked for `w <= 15`, `h <= 7`. Cross-checks: row sums `2^(n-1)` and `h^w - (h-1)^w`, `F(6,4) = 1729`, `odd(w,2) = A038503(w+1) - 1`, and the first-pass terms of `even`, `odd`, `cev`, `cod` and `strict_valley`.
[^search]: OEIS searches (https://oeis.org/search, JSON format, 2026-09-26) on the first 8 to 12 nonzero terms returned no results for: the `odd(., h)` rows for `h = 3..7`; the columns `odd(4..6, .)`, the even-`h` and odd-`h` halves of `odd(4, .)`, and `F(5, .)`, `F(6, .)`; all ten parity-refined area sequences, `strict_valley` and the five signed differences; the area and blocks columns `b = 3, 4, 5` and the antidiagonals `b = n - 3, n - 4`; the blocks and peaks cells `(4,1), (5,1), (6,1), (4,2), (5,2), (6,2)`; and the `h = 3` third column, the `h = 4` second column and the `h = 3, 4` triangles read by rows. The area and blocks triangle read by rows (12 terms) returned only entries that share the opening `1, 1, 1, 1, 2, 1` and then diverge.
[^oeis]: OEIS entries fetched in JSON (2026-09-26). A002620 "Quarter-squares: a(n) = floor(n/2)*ceiling(n/2)". A097701 "Expansion of 1/((1-x)^2*(1-x^2)^2*(1-x^3))", offset 0, comments on partitions into five parts and partitions "into two kinds of parts 1, two kinds of parts 2, and one kind of parts 3". A002624 "Expansion of (1-x)^(-3) * (1-x^2)^(-2)", offset 0, comments on a triangle product, queens on a chessboard, and partitions "with three kinds of 1 and two kinds of 2". A253943 "a(n) = 3*binomial(n+1,6)", offset 5. None of the four mentions compositions or castles. The alignments were compared by execution against the listed data: A002620 for areas 2 to 40, A097701 for 38 terms, A002624 for 36 terms.
