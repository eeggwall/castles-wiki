---
title: The odd castles and the block-count tables
category: Analyses
summary: "The odd-block count A^o(w, h) = (A − S)/2 = (A + P(h−1, w) − P(h−2, w))/2 as a sequence of its own: for 4 <= h <= 7 its minimal characteristic polynomial is that of A^e(·, h); at h = 2 A^o gains the root 1, and at h = 3 it loses the root 2, so its order is 5 against 6. The by-area families (all castles, convex, valley, non-convex, strict valley) split by block parity. Three joint tables: by area and blocks, the b-block column has denominator (1−q)^2 ⋯ (1−q^{b−1})^2 (1−q^b) for b <= 4 and not at b = 5; by area, blocks and peaks, two blocks give the quarter-squares A002620, three blocks with one peak A097701 and three blocks with two peaks A002624; by width, height and blocks, the h-block column is C(N, 2h−2) with N = w + 2h − 3, the (h+1)-block column (2h−3) C(N, 2h), and the (h+2)-block column a three-term binomial sum."
tags: [analysis, castle, oeis, sequence, odd-count, parity, area, block-count, peaks, joint-distribution, c-finite, binomial, verification]
sources: [oeis-mining-pe502]
created: 2026-09-26
updated: 2026-10-16
---

# The odd castles and the block-count tables

[[oeis-mining-pe502](pages/oeis-mining-pe502.md)] covers `A^e`, `A = h^w − (h−1)^w` and the signed tower count `P`. This page adds three sets of records: the odd-block count `A^o(w, h)` as a sequence of its own; the splits by block parity of the by-area families of [[castle-by-area](pages/castle-by-area.md)]; and the joint distributions of block count, peaks and area. Area and peaks alone are on [[castle-row-raising-equation](pages/castle-row-raising-equation.md)], and area and blocks as a generating function on [[castle-q-bessel-closed-form](pages/castle-q-bessel-closed-form.md)]. The OEIS status of every sequence on this page is recorded on [[castle-sequence-catalogue](pages/castle-sequence-catalogue.md)].

The statistics are the wiki's standard ones. The block count is `blocks(c) = c_1 + Σ_{i≥2} max(0, c_i − c_{i−1})` ([[castle-sign](pages/castle-sign.md)]). A peak is a maximal run of columns with `c_i ≥ 2` ([[castle-notation](pages/castle-notation.md)], [[prime-castles](pages/prime-castles.md)]). The area is `Σ c_i`. The castles of area `n` are the compositions of `n`; by width and height, the castles are those of width `w` and height `h`. Every number on this page was checked two ways, by brute force over compositions and skylines and by a transfer-matrix dynamic program.[^exec]

## The odd-block count

Removing the bottom row of a castle of width `w` and height `h` leaves towers of height at most `h − 1` with one block fewer, so the signed count over these castles is `S(w, h) = P(h−2, w) − P(h−1, w)`, with `P(k, L)` the signed tower count ([[castle-counting-formula](pages/castle-counting-formula.md)], [[signed-tower-count](pages/signed-tower-count.md)]). Then

```
A^o(w, h)  =  (A − S)/2  =  ( A(w, h) + P(h−1, w) − P(h−2, w) ) / 2
A^e(w, h)  =  (A + S)/2  =  ( A(w, h) − P(h−1, w) + P(h−2, w) ) / 2
```

At `h = 3` the second line is `A^e(w, 3) = (3^w − 2^w − P(2, w) + P(1, w))/2`, the closed form of [[new-sequence-fw3](pages/new-sequence-fw3.md)].[^exec]

The rows, from `w = 1`:

| `h` | `A^o(w, h)` | order | characteristic polynomial |
|---|---|---|---|
| 2 | `0, 0, 1, 5, 15, 35, 71, 135, 255, 495, 991, 2015` | 4 | `(x−2)(x−1)(x²−2x+2)` |
| 3 | `1, 5, 16, 44, 122, 358, 1082, 3274, 9850, 29546, 88594` | 5 | `(x−3)(x²−2x+2)(x²−x+2)` |
| 4 | `0, 0, 6, 58, 342, 1638, 7134, 29774, 121990, 495910` | 9 | `(x−4)(x−3)(x−2)(x²−x+2)(x⁴−4x³+8x²−8x+8)` |
| 5 | `1, 9, 51, 247, 1195, 6051, 31467, 164115, 850379` | 11 | `(x−5)(x−4)(x²−2x+4)(x³−3x²+2x−4)(x⁴−4x³+8x²−8x+8)` |
| 6 | `0, 0, 15, 223, 2021, 14905, 100157, 645029, 4069173` | 13 | `(x−6)(x−5)(x²−2x+4)(x³−3x²+2x−4)(x⁶−6x⁵+18x⁴−32x³+48x²−32x+32)` |
| 7 | `1, 13, 106, 738, 5124, 37128, 275804, 2053324` | 15 | `(x−7)(x−6)(x³−4x²+4x−8)(x⁴−3x³+8x²−4x+8)(x⁶−6x⁵+18x⁴−32x³+48x²−32x+32)` |

The `h = 2` row is `A038503(w + 1) − 1` ([[oeis-height2-hyperbolic-castles](pages/oeis-height2-hyperbolic-castles.md)]). The orders 5, 9 and 11 at `h = 3, 4, 5` agree with [[oeis-mining-pe502](pages/oeis-mining-pe502.md)].[^exec]

**Where the odd and even rows part.** For `h = 4..7` the minimal characteristic polynomial of `A^o(·, h)` equals that of `A^e(·, h)`, factor for factor. They differ only at `h = 2` and `h = 3`, where `(h−1)^w` from `A` meets the eigenvalue `h − 1` of one of the `P` terms. At `h = 3` the root 2 of `P(2, ·)` enters `A^o` with coefficient `+1/2` and cancels the `−2^w/2` from `A`, so `A^o(·, 3)` has order 5 while `A^e(·, 3)` has order 6. At `h = 2` it goes the other way: the constant `P(0, w) = 1` cancels the `−1^w` of `A` in `A^e`, which has order 3, and doubles it in `A^o`, which gains the root 1. For `4 ≤ h ≤ 7` neither `P(h−1, ·)` nor `P(h−2, ·)` has the eigenvalue `h − 1`, so nothing cancels and both rows have order `2h + 1`.[^exec]

**Columns.** At fixed `w` the counts depend on the parity of `h`, since `P(·, w)` is a period-2 quasi-polynomial in the tower height (computed for `4 ≤ w ≤ 12`, [[signed-tower-k-direction](pages/signed-tower-k-direction.md)]). The `w = 3` column is on [[sum-of-three-cubes-castles](pages/sum-of-three-cubes-castles.md)] and `A^e(4, h)` is on [[castle-sequence-catalogue](pages/castle-sequence-catalogue.md)]. Further columns, from `h = 1`:

| column | first terms |
|---|---|
| `A^o(4, h)` | `1, 5, 44, 58, 247, 223, 738, 564, 1645, 1145, 3096, 2030` |
| `A^o(5, h)` | `1, 15, 122, 342, 1195, 2021, 5124, 6924, 14901, 17755, 34606` |
| `A^o(6, h)` | `1, 35, 358, 1638, 6051, 14905, 37128, 69196, 140709, 224143` |
| `A^e(5, h)` | `0, 16, 89, 439, 906, 2630, 3907, 9037, 11380, 23196, 26445` |
| `A^e(6, h)` | `0, 28, 307, 1729, 5478, 16126, 33865, 75299, 128588, 244416` |

## The parity-refined area sequences

Each by-area family splits by block parity. Terms from `n = 1`:[^exec]

| name | castles of area `n` | first terms | sum |
|---|---|---|---|
| `even` | all, even blocks | `0, 1, 2, 5, 8, 17, 30, 65, 122, 261, 502, 1043, 2026, 4145, 8124, 16499` | `even + odd = 2^(n−1)` |
| `odd` | all, odd blocks | `1, 1, 2, 3, 8, 15, 34, 63, 134, 251, 522, 1005, 2070, 4047, 8260, 16269` | |
| `cev` | convex, even | `0, 1, 2, 5, 8, 15, 24, 41, 64, 105, 162, 255, 386, 589, 874, 1300` | `cev + cod = A001523` |
| `cod` | convex, odd | `1, 1, 2, 3, 7, 12, 23, 38, 66, 104, 168, 257, 398, 594, 891, 1304` | |
| `valley_even` | valley, even | `0, 1, 2, 4, 6, 12, 16, 32, 40, 78, 98, 175, 224, 380, 488, 786` | sum `= A332578` |
| `valley_odd` | valley, odd | `1, 1, 2, 3, 7, 9, 20, 25, 51, 62, 119, 148, 261, 331, 551, 708` | |
| `nc_even` | non-convex, even | `0, 0, 0, 0, 0, 2, 6, 24, 58, 156, 340, 788, 1640, 3556, 7250, 15199` | sum `= A115981` |
| `nc_odd` | non-convex, odd | `0, 0, 0, 0, 1, 3, 11, 25, 68, 147, 354, 748, 1672, 3453, 7369, 14965` | |
| `sv_even` | strict valley, even | `0, 0, 0, 0, 0, 2, 2, 11, 12, 36, 44, 99, 126, 244, 316, 554` | sum `= strict_valley` |
| `sv_odd` | strict valley, odd | `0, 0, 0, 0, 1, 1, 6, 6, 22, 24, 63, 76, 159, 201, 375, 483` | |

A strict-valley castle is a valley castle that is not convex ([[castle-by-area](pages/castle-by-area.md)]); the skyline `(2, 1, 2)` is the smallest. The first sixteen terms of `strict_valley` itself are `0, 0, 0, 0, 1, 3, 8, 17, 34, 60, 107, 175, 285, 445, 691, 1037`. The signed differences begin `cev − cod = −1, 0, 0, 2, 1, 3, 1, 3, −2, 1, −6, −2` and `valley_even − valley_odd = −1, 0, 0, 1, −1, 3, −4, 7, −11, 16, −21, 27`.[^exec]

## Joint tables

### Area and blocks

Write `a_b(n)` for the number of castles of area `n` with `b` blocks. Rows from `n = 1`, for `b = 1..n`:

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

Row sums are `2^(n−1)`, and the alternating row sums are `even(n) − odd(n)`. The rows are the coefficients of the generating function by area and blocks on [[castle-q-bessel-closed-form](pages/castle-q-bessel-closed-form.md)] at unit width weight.[^exec]

With `b` fixed, a castle is one of finitely many nested arrangements of `b` intervals, and each arrangement contributes a rational generating function in the area. So every column is rational. The columns, checked to area 90:[^exec]

| `b` | column generating function | first terms (`n = b, b+1, …`) | OEIS |
|---|---|---|---|
| 2 | `q² / ((1−q)² (1−q²))` | `1, 2, 4, 6, 9, 12, 16, 20, 25, 30, 36` | `A002620(n)`, the quarter-squares |
| 3 | `q³ (1 + q² + q³ + q⁴) / ((1−q)² (1−q²)² (1−q³))` | `1, 2, 6, 12, 24, 41, 69, 106, 160, 229, 322` | |
| 4 | `q⁴ N_4(q) / ((1−q)² (1−q²)² (1−q³)² (1−q⁴))` | `1, 2, 7, 16, 39, 78, 157, 284, 502, 834, 1351` | |
| 5 | rational, with denominator `(1−q)(1−q²)²(1−q³)³(1−q⁴)²(1−q⁵)` | `1, 2, 8, 19, 53, 117, 266, 540, 1078, 2011, 3659` | |

Here `N_4(q) = 1 + 2q² + 2q³ + 6q⁴ + 4q⁵ + 7q⁶ + 4q⁷ + 4q⁸ + 2q⁹ + q¹⁰`. For `b ≤ 4` the denominator is `(1−q)² ⋯ (1−q^{b−1})² (1−q^b)`; at `b = 5` that product does not clear the column, and the denominator in the table does, with a numerator of degree 25. For `b ≤ 6` the pole at `q = 1` has order `2b − 1`, so the `b`-block column grows like `n^{2b−2}` (computed). The two-block case is elementary: a two-block castle is `1^a 2^m 1^c` with `m ≥ 1`, which leaves `⌊n²/4⌋` choices.

### Area, blocks and peaks

Peaks refine the columns. A castle with `p` peaks has at least `p + 1` blocks. Equality `b = p + 1` means every peak is a single block, so the castle has height 2; that diagonal is the row `h = 2` of [[castles-of-height-h-by-area](pages/castles-of-height-h-by-area.md)]. The next cells, in castles of area `n`:[^exec][^oeis]

| blocks, peaks | first terms | OEIS |
|---|---|---|
| 2, 1 | `1, 2, 4, 6, 9, 12, 16, 20` (from `n = 2`) | `A002620(n)` |
| 3, 1 | `1, 2, 5, 9, 16, 25, 39, 56, 80, 109, 147, 192` (from `n = 3`) | `A097701(n − 3)`, "Expansion of `1/((1-x)^2*(1-x^2)^2*(1-x^3))`" |
| 3, 2 | `1, 3, 8, 16, 30, 50, 80, 120, 175, 245, 336, 448` (from `n = 5`) | `A002624(n − 5)`, "Expansion of `(1-x)^(-3) * (1-x^2)^(-2)`" |
| 4, 1 | `1, 2, 5, 10, 20, 34, 60, 96, 153, 232, 348, 502` (from `n = 4`) | |
| 5, 1 | `1, 2, 5, 10, 22, 39, 74, 127, 219, 357, 582, 905` (from `n = 5`) | |
| 4, 2 | `2, 6, 18, 40, 84, 156, 278, 462, 744, 1146, 1722, 2508` (from `n = 6`) | |
| 5, 2 | `3, 9, 28, 66, 149, 297, 573, 1029, 1794, 2988, 4853, 7627` (from `n = 7`) | |

Both identifications with OEIS entries hold over the full length compared, through area 40. A three-block castle with one peak is a base, a block on it and a block on that. A three-block castle with two peaks is a base carrying two separated one-block towers. The two generating functions differ only by one factor: `(1−q³)` for one peak against `(1−q)` for two.

### Width, height and blocks

At fixed `(w, h)` the block count runs from `h`, for the convex castles ([[convex-castle-binomial-identity](pages/convex-castle-binomial-identity.md)]), up to a maximum reached by the battlement `h, 1, h, 1, …` ([[tower-narayana-polynomial](pages/tower-narayana-polynomial.md)] treats the towers by blocks). Its `h = 3` rows from `w = 1`, for blocks `3, 4, 5, …`:

```
1
5
15    3    1
35   21    9
70   84   51    5    1
126  252  219   55   13
210  630  765  340  106   7   1
```

Each row sums to `3^w − 2^w`. At `h = 2` the entries are binomials, `C(w + 1, 2b − 2)`. For general `h`, set `N = w + 2h − 3`. Then the first three columns are, checked for `w ≤ 18` and `2 ≤ h ≤ 6`:[^exec]

```
blocks h     :  C(N, 2h − 2)
blocks h + 1 :  (2h − 3) C(N, 2h)
blocks h + 2 :  (2h − 5) C(N, 2h) + 2(2h − 5) C(N, 2h + 1) + (2h + 1)(h − 2) C(N, 2h + 2)      (h ≥ 3)
```

The first line is the convex count. The `b`-block column is a polynomial in `w` of degree `2b − 2`, the same exponent as the area column. The last entry of each row is `1` at odd `w` (the battlement alone) and `(h − 1)w + 1` at even `w` (checked for `w ≤ 15`, `h ≤ 7`). The second column at `h = 3` is `3 C(w + 3, 6) = A253943(w + 2)`, and the second column at `h = 4` is `5 C(w + 5, 8)`.[^oeis]

## Related Concepts

- [[castle-sequence-catalogue](pages/castle-sequence-catalogue.md)] - the OEIS status of the sequences on this page.
- [[castle-by-area](pages/castle-by-area.md)] - the by-area families and their definitions.
- [[new-sequence-fw3](pages/new-sequence-fw3.md)] - `A^e(w, 3)`, whose odd-block companion is the `h = 3` row of the first table.
- [[signed-tower-count](pages/signed-tower-count.md)] - the `P(k, ·)` terms in the formulas for `A^o` and `A^e`.
- [[castle-row-raising-equation](pages/castle-row-raising-equation.md)] - castles counted by area and peaks.
- [[castle-q-bessel-closed-form](pages/castle-q-bessel-closed-form.md)] - the generating function by area, width and blocks behind the area-and-blocks triangle.
- [[castle-conditional-entropy](pages/castle-conditional-entropy.md)] - the joint distribution of blocks and area read as entropy.
- [[convex-castle-binomial-identity](pages/convex-castle-binomial-identity.md)] - the first column of the width-height-blocks table.
- [[oeis-cross-referencing](pages/oeis-cross-referencing.md)] - the offset check used for the identifications with OEIS entries.

## Footnotes

[^exec]: Verified by execution (Python 3.11 with SymPy, 2026-10-16): `A^o(w, h)` and `A^e(w, h)` by a column DP on (last height, block parity, height reached) for `w ≤ 44`, `h ≤ 7`, with minimal recurrences by Berlekamp-Massey over `Q` and factored, and the columns at fixed `w = 4, 5, 6`; the by-area families and the area-blocks and area-blocks-peaks tables by brute force over all compositions of `n ≤ 16`; the area-blocks columns `b ≤ 6` by a DP on (last height, blocks) through area 90, with the column generating functions for `b ≤ 4` checked to area 90, the `b ≤ 4` denominator failing at `b = 5` and the table's `b = 5` denominator clearing the column with a numerator of degree 25; the width-height-blocks table by a DP on (last height, blocks, height reached), its three column formulas for `w ≤ 18`, `2 ≤ h ≤ 6`, the binomials at `h = 2` for `w ≤ 14`, the last-entry law for `w ≤ 15`, `h ≤ 7`, and `3 C(w + 3, 6)`, `5 C(w + 5, 8)`.
[^oeis]: OEIS entries (read 2026-10-16). A002620 "Quarter-squares: a(n) = floor(n/2)*ceiling(n/2)". A097701 "Expansion of 1/((1-x)^2*(1-x^2)^2*(1-x^3))", offset 0. A002624 "Expansion of (1-x)^(-3) * (1-x^2)^(-2)", offset 0. A253943 "a(n) = 3*binomial(n+1,6)", offset 5. The alignments were compared by execution against the listed data: A002620 for areas 2 to 40, A097701 for 38 terms, A002624 for 36 terms.
