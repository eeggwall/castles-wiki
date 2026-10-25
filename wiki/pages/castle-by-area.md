---
title: Castles by area
category: Concepts
summary: Castles counted by their area n, the number of cells, instead of by width and height. A castle of area n is a composition of n, so there are 2^{n−1} of them; the convex castles of area n are the weakly unimodal compositions (A001523), the valley castles A332578, the non-convex castles A115981 and the castles that are not valleys A332669. The page tabulates these counts and their splits by block parity for n ≤ 12.
tags: [concept, castle, area, composition, oeis, unimodal, valley]
sources: [oeis-mining-pe502]
created: 2026-09-13
updated: 2026-10-25
---

# Castles by area

The **area** of a castle with skyline `(c_1, …, c_w)` is its number of cells, `n = c_1 + ⋯ + c_w`. A castle of area `n` has `1 ≤ w ≤ n` and `1 ≤ h ≤ n`, so there are finitely many. The skyline is a composition of `n`, a sequence of positive integers with sum `n`, and every composition of `n` is the skyline of a castle ([[castle-polyomino](pages/castle-polyomino.md)]).[^1]

*Example: area 3.* The castles of area 3 are the skylines `(3)`, `(1, 2)`, `(2, 1)` and `(1, 1, 1)`:

```
#       . .        . .        . . .
#       . #        # .        . . .
#       # #        # #        # # #
(3)     (1, 2)     (2, 1)     (1, 1, 1)
```

The skylines `(1, 2)` and `(2, 1)` have two blocks, the skyline `(3)` has three and `(1, 1, 1)` has one, so two of the four have an even number of blocks. All four are convex.

## Families

The counts use these families of skylines:

- **convex**: unimodal, weakly increasing and then weakly decreasing ([[convex-castle](pages/convex-castle.md)]);
- **valley**: weakly decreasing and then weakly increasing;
- **strict valley**: valley and not convex, so with a column lower than a column on each side of it;
- **non-convex**: not convex.

The skyline `(2, 1, 2)` is a strict valley, `(1, 2, 1)` is convex and not a valley, and the monotone skylines, such as `(1, 1, 2)`, are both convex and valleys.

## Counts by area

For `n = 1, …, 12`, the numbers of castles of area `n` are:[^2]

| castles of area `n` | source's name | `n = 1, 2, …, 12` | OEIS |
|---|---|---|---|
| all | `all` | 1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048 | `A011782(n) = 2^{n−1}` |
| all, even block count | `even` | 0, 1, 2, 5, 8, 17, 30, 65, 122, 261, 502, 1043 | |
| all, odd block count | `odd` | 1, 1, 2, 3, 8, 15, 34, 63, 134, 251, 522, 1005 | |
| convex | `conv` | 1, 2, 4, 8, 15, 27, 47, 79, 130, 209, 330, 512 | `A001523(n)` |
| convex, even block count | `cev` | 0, 1, 2, 5, 8, 15, 24, 41, 64, 105, 162, 255 | |
| convex, odd block count | `cod` | 1, 1, 2, 3, 7, 12, 23, 38, 66, 104, 168, 257 | |
| valley | `valley` | 1, 2, 4, 7, 13, 21, 36, 57, 91, 140, 217, 323 | `A332578(n)` |
| valley, even block count | `valley_even` | 0, 1, 2, 4, 6, 12, 16, 32, 40, 78, 98, 175 | |
| valley, odd block count | `valley_odd` | 1, 1, 2, 3, 7, 9, 20, 25, 51, 62, 119, 148 | |
| strict valley | `strict_valley` | 0, 0, 0, 0, 1, 3, 8, 17, 34, 60, 107, 175 | |
| strict valley, even block count | `sv_even` | 0, 0, 0, 0, 0, 2, 2, 11, 12, 36, 44, 99 | |
| strict valley, odd block count | `sv_odd` | 0, 0, 0, 0, 1, 1, 6, 6, 22, 24, 63, 76 | |
| non-convex | `nonconv` | 0, 0, 0, 0, 1, 5, 17, 49, 126, 303, 694, 1536 | `A115981(n)` |
| non-convex, even block count | `nc_even` | 0, 0, 0, 0, 0, 2, 6, 24, 58, 156, 340, 788 | |
| non-convex, odd block count | `nc_odd` | 0, 0, 0, 0, 1, 3, 11, 25, 68, 147, 354, 748 | |
| not a valley | `all − valley` | 0, 0, 0, 1, 3, 11, 28, 71, 165, 372, 807, 1725 | `A332669(n)` |

Every entry agrees with brute-force enumeration of the compositions of `n`.[^3] Each parity split adds up to its family, and the OEIS rows read as follows:[^4]

- `A011782(n) = 2^{n−1}` for `n ≥ 1`, the number of compositions of `n`.
- `A001523(n)`, "number of stacks, or planar partitions of n; also number of weakly unimodal compositions of n": a convex castle of area `n` is a weakly unimodal composition of `n` ([[weakly-unimodal-composition](pages/weakly-unimodal-composition.md)]).
- `A332578(n)`, the compositions of `n` whose negation is unimodal: negating a skyline exchanges valleys and unimodal sequences.
- `A115981(n) = A011782(n) − A001523(n)`, the compositions of `n` "which cannot be viewed as stacks".
- `A332669(n) = 2^{n−1} − A332578(n)`, the compositions of `n` whose negation is not unimodal.

A skyline is both convex and a valley exactly when it is monotone. The weakly increasing and the weakly decreasing compositions of `n` each correspond to the partitions of `n`, and the compositions that are both have all parts equal, one for each divisor of `n`. So, with `p(n)` the number of partitions of `n` and `d(n)` the number of divisors,[^5]

```
valley(n)  =  strict_valley(n) + 2p(n) − d(n).
```

At `n = 5`: `13 = 1 + 2·7 − 2`.

[[odd-castles-and-block-tables](pages/odd-castles-and-block-tables.md)] lists sixteen terms of each parity split.

## By width and height

Counted by width and height instead of area, the valley castles and the convex castles agree: for `w ≤ 7` and `h ≤ 6` (with `h^w ≤ 300000`), the valley castles of width `w` and height `h` number `C(2h + w − 3, w − 1) = A_convex(w, h)` ([[convex-castle-binomial-identity](pages/convex-castle-binomial-identity.md)]).[^6] The two sets differ: at `w = 3`, `h = 2`, the skyline `(1, 2, 1)` is convex and not a valley, and `(2, 1, 2)` is a valley and not convex. By area they differ from `n = 4` on, 8 convex castles against 7 valleys.

## Appearances in Sources

- [[oeis-mining-pe502](pages/oeis-mining-pe502.md)] - the counts by area of all, convex, valley, strict-valley and non-convex castles and their parity splits for `n ≤ 15` to `18`, the OEIS matches, and the valley counts by width and height.

## Related Concepts

- [[convex-castle](pages/convex-castle.md)] - convex castles and their count `C(2h + w − 3, w − 1)` by width and height.
- [[weakly-unimodal-composition](pages/weakly-unimodal-composition.md)] - the weakly unimodal compositions, `A001523`, which are the convex castles by area.
- [[stack-polyomino-gf](pages/stack-polyomino-gf.md)] - the generating function of `A001523` by the symbolic method.
- [[odd-castles-and-block-tables](pages/odd-castles-and-block-tables.md)] - sixteen terms of each parity split, and tables of castles by area jointly with blocks and with peaks.
- [[castle-row-raising-equation](pages/castle-row-raising-equation.md)] - the even-block minus odd-block count by area to area 300, which grows like `C·(−ρ)^n` with `ρ = 1.62383…` and `C = 0.09851…`.
- [[castle-q-bessel-closed-form](pages/castle-q-bessel-closed-form.md)] - the generating function of castles by width, blocks and area in closed form, through the parallelogram-polyomino q-Bessel series.
- [[signed-prime-castles](pages/signed-prime-castles.md)] - the sign `(−1)^{blocks − 1}` on the free monoid of prime castles, which reproduces the odd-block minus even-block count by area.
- [[prime-castles](pages/prime-castles.md)] - castles cut at their height-1 columns into prime castles, those with no column of height 1, of which there are `F_{n−1}` of area `n`.
- [[prime-convex-castles](pages/prime-convex-castles.md)] - the convex castles with no column of height 1, counted by the second difference of `A001523`.
- [[q-fibonacci-castle](pages/q-fibonacci-castle.md)] - the Fibonacci castles counted by area, `A000930(n+1) − 1`, supergolden by area.
- [[tree-castle-by-area](pages/tree-castle-by-area.md)] - the tree castles counted by area at each height: `A077868` at height 2, `A006498` at height 3, `A000570` at height 4, and `A005251` with no bound on the height.
- [[area-growth-census](pages/area-growth-census.md)] - the growth constants by area of castle strips under every rule on neighboring columns through height 5.
- [[convex-polyomino-by-area](pages/convex-polyomino-by-area.md)] - the families of convex polyominoes counted by area, with the convex castles as the stacks and the castles as the bargraphs.
- [[column-convex-ladder-by-area](pages/column-convex-ladder-by-area.md)] - castles by area inside the directed column-convex polyominoes (`A001519`) and the column-convex polyominoes (`A001169`), unsigned and with the block sign.
- [[column-convex-polygon-enumeration](pages/column-convex-polygon-enumeration.md)] - the add-a-column method for column-convex polygons; castles are its directed column-convex polygons whose columns all start on row 1.
- [[prellberg-brak-1995-cluster-models](pages/prellberg-brak-1995-cluster-models.md)] - the functional equation (3.11) for bargraphs, the generating function of castles by width, blocks and area.
- [[castle-conditional-entropy](pages/castle-conditional-entropy.md)] - the entropy of the area of a castle chosen uniformly at fixed width and height.
- [[aocp-combinatorics](pages/aocp-combinatorics.md)] - permutations counted by inversions, with the q-factorial generating function.
- [[oeis-cross-referencing](pages/oeis-cross-referencing.md)] - matching castle counts against OEIS data, with offsets.
- [[q-thread-seminar](pages/q-thread-seminar.md)] - a seminar on castles counted by area.

## Footnotes

[^1]: [[oeis-mining-pe502](pages/oeis-mining-pe502.md)] `vein9-area.md` §"The trivial baseline" L6-14 - "A castle of area n has 1 <= w <= n and 1 <= h <= n, so the enumeration by area is a finite brute force", "All castles of area n = all compositions of n into positive parts = 2^(n-1) = A000079(n-1) = A011782 shifted ... every ordered sequence (c_1..c_w) of positive integers summing to n is a valid castle shape (Rule 3 is automatic)". The same count is the bargraph row of raw/bousquet-melou-rechnitzer-2002-lattice-animals-heaps-of-dimers.pdf p.237 Table 1 - "Bargraph (Compositions) 2 Rational Obvious".
[^2]: [[oeis-mining-pe502](pages/oeis-mining-pe502.md)] `vein9-area.md` §"The main finding" and §"Parity splits — four new sequences" L18-49, and `vein9b-concave.md` §"Results by area" and §"Parity splits — all new" L5-22, L80-87 [synthesis] - the definitions of the valley, strict-valley and non-convex families and the tables of `conv`, `even`, `odd`, `cev`, `cod`, `valley`, `strict_valley`, `nonconv`, `all − valley` and the six parity splits for `n = 1, …, 12`.
[^3]: Verified by execution (Python 3.11, 2026-10-16): every row of the table for `n ≤ 15`, by enumerating the compositions of `n`; the identity for `valley(n)` for `n ≤ 14`; the valley and convex castles by width and height for `w ≤ 7`, `h ≤ 6` with `h^w ≤ 300000`.
[^4]: https://oeis.org/A011782, https://oeis.org/A001523, https://oeis.org/A332578, https://oeis.org/A115981, https://oeis.org/A332669 (read 2026-10-16) - "Coefficients of expansion of (1-x)/(1-2*x) in powers of x", "Number of stacks, or planar partitions of n; also number of weakly unimodal compositions of n", "Number of compositions of n whose negation is unimodal", "The number of compositions of n which cannot be viewed as stacks", "Number of compositions of n whose negation is not unimodal"; [[oeis-mining-pe502](pages/oeis-mining-pe502.md)] `vein9b-concave.md` §"The matches" L28-42 - "A115981 ... formula a(n) = A011782(n) − A001523(n)" and "A332669(n) = 2^(n−1) − A332578(n) = all(n) − valley(n)".
[^5]: [[oeis-mining-pe502](pages/oeis-mining-pe502.md)] `vein9b-concave.md` §"The new sequence — strict_valley(n)" L56-71 [synthesis] - `strict_valley(n)` plus the monotone castles is `valley(n)`, and the monotone compositions are the weakly increasing and the weakly decreasing ones, each counted by the partitions `A000041(n)`, with the constant compositions counted twice.
[^6]: [[oeis-mining-pe502](pages/oeis-mining-pe502.md)] `vein9b-concave.md` §"Concave counts by (w, h) — the PE 502 axis" L100-114 - "This is the same table as convex(w, h) — both equal C(2h + w − 3, w − 1) ... So convex and valley have the same cardinality in each (w, h) cell but different sets; e.g. for (w=3, h=2) convex has 6 castles and valley has 6 castles, differing in whether (1,2,1) and (2,1,2) are counted (peak vs. dip)." The source's table covers `w, h ≤ 5`.
