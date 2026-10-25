---
title: Castle sequence catalogue
category: Analyses
summary: Catalogue of every castle-counting sequence on the wiki, by the object it counts, with first terms, recurrence or generating function, growth constant, and the OEIS entry it equals where there is one, at the stated offset. Every row with listed terms was recomputed by enumeration, transfer matrix or dynamic program, and every cited entry was compared with the computed terms.
tags: [analysis, oeis, castle, sequence, catalogue]
sources: [oeis-mining-pe502]
created: 2026-09-17
updated: 2026-10-25
---

# Castle sequence catalogue

## What this is

This page catalogues the sequences that castles produce, organized by the castle object each one counts rather than by OEIS A-number. Every sequence has a record with first terms, a recurrence or generating function (g.f.), its growth constant, and the entry of the On-Line Encyclopedia of Integer Sequences (OEIS) it equals, at the stated offset; "-" means no entry is listed.[^1]

[[oeis-index](pages/oeis-index.md)] is the generated directory of every A-number cited on the wiki, with the citing pages. [[oeis-cross-referencing](pages/oeis-cross-referencing.md)] describes the checks a match must pass, [[oeis-mining-pe502](pages/oeis-mining-pe502.md)] is the first mining pass, and [[oeis-height2-hyperbolic-castles](pages/oeis-height2-hyperbolic-castles.md)] proves the height-2 rows.

The symbols are those of [[castle-notation](pages/castle-notation.md)]: `A^e(w, h)` and `A^o(w, h)` count the castles of width `w` and height `h` with an even and an odd number of blocks. A skyline on `{1, …, h}` need not reach height `h`, so a count of skylines on `{1, …, h}` is a count of castles of every height up to `h`.

## OEIS entries proved on other pages

These identities are stated and proved on the pages cited; the section *Catalogue* gives the terms of most of them.

- `A038505`, `A038503`, `A146559`: `A^e(w, 2) = A038505(w+1)` and `A^o(w, 2) = A038503(w+1) − 1` ([[oeis-height2-hyperbolic-castles](pages/oeis-height2-hyperbolic-castles.md)]); `A146559(n) = P(1, n − 1)`, so `A146559(n) − 1` is the number of castles of width `n − 1` and height 2 with an odd number of blocks minus the number with an even number ([[signed-tower-count](pages/signed-tower-count.md)]).

- `A009545`: among the castles of width `n` and height 2 whose last column has height 2, `A009545(n)` is the number with an even number of blocks minus the number with an odd number ([[tower-parity-sectors](pages/tower-parity-sectors.md)]).
- `A005251`, `A202882`, `A203094`, `A203184`: the Hardin word identity reads each as `2^{−L}` times a signed tower count over the towers whose last column is even, and proves their empirical recurrences ([[hardin-word-identity](pages/hardin-word-identity.md)]). The tower-spacing skylines with `g = 2` give each an unsigned reading ([[tower-spacing-castles](pages/tower-spacing-castles.md)]), and `A005251` has four readings related by an explicit bijection ([[a005251-bijection](pages/a005251-bijection.md)]; the section *Multi-interpretation hub*).
- `A000071`, `A000073`, `A000078`, `A001591`: castles by area of height 2 and of height at most 3, 4, 5, through compositions with bounded parts ([[castles-of-height-h-by-area](pages/castles-of-height-h-by-area.md)]).
- The tower-spacing arrays of Hardin, "each element the minimum of `g` adjacent elements" (`A217878` to `A217881`, `A217949` to `A217952`) and "maxima of three adjacent elements" (`A228457`, `A228458`), with the tables `A217883`, `A217954` and `A228461`; the `h = 2` row `A005252`, `A005253`, `A005689`, `A098574` joins `A005251` with the closed form `Sum_k C(w+g−(g−1)k, 2k)` ([[tower-spacing-castles](pages/tower-spacing-castles.md)]).
- `A001045`, `A006130`, `A006131`: the tree castles of height at most 3, 4 and 5 by width number `A001045(w+2)`, `A006130(w+1)` and `A006131(w+1)` ([[castle-graph](pages/castle-graph.md)]).
- `A005408`, `A005891`, `A063490`, `A160747`: the towers of width `w = 2, 3, 4, 5` by number of blocks `b` are `A005408(b)`, `A005891(b)`, `A063490(b+1)` and `A160747(b)`, and the Narayana triangle `A001263` enters the general row ([[tower-narayana-polynomial](pages/tower-narayana-polynomial.md)]).
- `A001523`, `A115981`, `A332578`: the convex, non-convex and valley castles by area ([[castle-by-area](pages/castle-by-area.md)]).
- `A352116`: `|P(k, 4)| = A352116(k+1)` in the tower height `k` ([[castle-eigenvalue-oeis-crosswalk](pages/castle-eigenvalue-oeis-crosswalk.md)]).
- `A343386`, `A107587`, `A343773`, `A171842`, `A005773`: the Motzkin-path castles and their parity split, the Motzkin strip of height 3, and the Motzkin left factors ([[motzkin-castles](pages/motzkin-castles.md)]; the section *Motzkin castles*).

## Catalogue

### Multi-interpretation hub

`A005251` (`0, 1, 1, 1, 2, 4, 7, 12, 21, 37, …` from `n = 0`, growth `ψ² = 1.7549`, with `ψ` the plastic number) counts four castle objects, related by an explicit bijection ([[a005251-bijection](pages/a005251-bijection.md)]):

| castle object | count | `A005251` offset |
|---|---|---|
| tree castles of area `n`, any height (compositions of `n` with no two adjacent parts `≥ 2`) | `1, 2, 4, 7, 12, …` from `n = 1` | `A005251(n+2)` |
| binary strings of length `N` with no factor `010` | `1, 2, 4, 7, 12, …` from `N = 0` | `A005251(N+3)` |
| tower-spacing skylines `(h = 2, g = 2)` of width `w` | `2, 4, 7, 12, 21, …` from `w = 1` | `A005251(w+3)` |
| Hardin's words with no isolated 1, equivalently `P_even(6, L)/2^L` | `1, 2, 4, 7, …` from `L = 0` | `A005251(L+3)` (binary words of length `L + 1` with no isolated 1) |

The bijection takes a composition of `n` to a binary string of length `n − 1` with no factor `010`, and "no two adjacent parts `≥ 2`" to "no factor `010`". A tower-spacing skyline of width `w` with `g = 2` is a raised-column string of length `w` with no factor `101`, which complementing the bits turns into the second row. See [[plastic-number](pages/plastic-number.md)].

### Castles by area with bounded height: the n-nacci family

A castle of area `n` is a composition of `n`, its column heights in order ([[castles-of-height-h-by-area](pages/castles-of-height-h-by-area.md)]). The castles of height at most `h` are the compositions with parts at most `h`, counted by the `h`-step Fibonacci numbers with g.f. `1/(1 − x − ⋯ − x^h)`; the castles of height 2 are the compositions into parts 1 and 2 that use a 2, `F_{n+1} − 1` of them.

| object | first terms (`n = 1…`) | growth | OEIS |
|---|---|---|---|
| height 2 | `0, 1, 2, 4, 7, 12, 20, 33` | `φ` | [A000071](https://oeis.org/A000071) (`= A000071(n+1) = F_{n+1} − 1`) |
| height at most 3 | `1, 2, 4, 7, 13, 24, 44, 81` | tribonacci `1.8393` | [A000073](https://oeis.org/A000073) (`= A000073(n+2)`) |
| height at most 4 | `1, 2, 4, 8, 15, 29, 56, 108` | tetranacci `1.9276` | [A000078](https://oeis.org/A000078) (`= A000078(n+3)`) |
| height at most 5 | `1, 2, 4, 8, 16, 31, 61, 120` | pentanacci `1.9659` | [A001591](https://oeis.org/A001591) (`= A001591(n+4)`) |

*(Every row agrees with enumeration of compositions for `n ≤ 14` and with the OEIS data at the stated offset, 2026-10-16.)*

### Tower-spacing skylines

Skylines on `{1, …, h}` in which every row `2, …, h` has its empty runs between filled cells at least `g` long, so towers that reach a row are at least `g` columns apart ([[tower-spacing-castles](pages/tower-spacing-castles.md)]). A column-by-column transfer matrix counts them.

| object | first terms (`w = 1…`) | growth | OEIS |
|---|---|---|---|
| `(h=2, g=2)` | `2, 4, 7, 12, 21, 37, 65` | `ψ²` `1.7549` | [A005251](https://oeis.org/A005251) (`= A005251(w+3)`; the section *Multi-interpretation hub*) |
| `(h=3, g=2)` | `3, 9, 22, 51, 121, 292, 704` | `2.4022` | [A202882](https://oeis.org/A202882) (`= A202882(w+1)`; Hardin) |
| `(h=4, g=2)` | `4, 16, 50, 144, 422, 1268` | `2.9972` | [A203094](https://oeis.org/A203094) (`= A203094(w+1)`; Hardin) |
| `(h=5, g=2)` | `5, 25, 95, 325, 1121, 3985` | `3.5589` | [A203184](https://oeis.org/A203184) (`= A203184(w+1)`; Hardin) |
| `(h=6, g=2)` | `6, 36, 161, 636, 2507, 10213` | `4.0967` | [A203050](https://oeis.org/A203050) (`= A203050(w+1)`; Hardin) |
| `(h=2, g=3)` | `2, 4, 7, 11, 17, 27, 44` | `φ` `1.6180` | [A005252](https://oeis.org/A005252) (`= A005252(w+3)`) |
| `(h=2, g=4)` | `2, 4, 7, 11, 16, 23, 34` | `1.5289` | [A005253](https://oeis.org/A005253) (`= A005253(w+3)`) |
| `(h=2, g=5)` | `2, 4, 7, 11, 16, 22, 30` | `1.4656` | [A005689](https://oeis.org/A005689) Twopins positions (`= A005689(w+6)`) |
| `(h=2, g=6)` | `2, 4, 7, 11, 16, 22, 29` | `1.4178` | [A098574](https://oeis.org/A098574) (`= A098574(w+6)`) |
| `(h=3, g=3)` | `3, 9, 22, 46, 91, 183, 383` | `2.1069` | [A217878](https://oeis.org/A217878) (0..2 arrays, "minimum of 3 adjacent elements") |
| `(h=3, g=4)` | `3, 9, 22, 46, 86, 153, 274` | `1.9274` | [A217879](https://oeis.org/A217879) (0..2, minimum of 4) |
| `(h=3, g=5)` | `3, 9, 22, 46, 86, 148, 244` | `1.8051` | [A217880](https://oeis.org/A217880) (0..2, minimum of 5) |
| `(h=3, g=6)` | `3, 9, 22, 46, 86, 148, 239` | `1.7157` | [A217881](https://oeis.org/A217881) (0..2, minimum of 6) |
| `(h=4, g=3)` | `4, 16, 50, 130, 310, 736` | `2.5398` | [A217949](https://oeis.org/A217949) (0..3, minimum of 3) |
| `(h=4, g=4)` | `4, 16, 50, 130, 296, 624, 1289` | `2.2733` | [A217950](https://oeis.org/A217950) (0..3, minimum of 4) |
| `(h=4, g=5)` | `4, 16, 50, 130, 296, 610, 1177` | `2.0966` | [A217951](https://oeis.org/A217951) (0..3, minimum of 5) |
| `(h=4, g=6)` | `4, 16, 50, 130, 296, 610, 1163` | `1.9697` | [A217952](https://oeis.org/A217952) (0..3, minimum of 6) |
| `(h=5, g=3)` | `5, 25, 95, 295, 821, 2227, 6254` | `2.9392` | [A228457](https://oeis.org/A228457) (0..4 arrays, "maxima of three adjacent elements") |
| `(h=6, g=3)` | `6, 36, 161, 581, 1847, 5615, 17487` | `3.3154` | [A228458](https://oeis.org/A228458) (0..5, maxima of three) |
| `(h=5, g=4)` | `5, 25, 95, 295, 791, 1927, 4496, 10606` | `2.5888` | - (order 17) |
| `(h=5, g=5)` | `5, 25, 95, 295, 791, 1897, 4196, 8848` | `2.3608` | - (order 21) |
| `(h=5, g=6)` | `5, 25, 95, 295, 791, 1897, 4166, 8548` | `2.1991` | - (order 25) |
| `(h=6, g=4)` | `6, 36, 161, 581, 1792, 4955, 12889, 33279` | `2.8839` | - (order 21) |
| `(h=6, g=5)` | `6, 36, 161, 581, 1792, 4900, 12229, 28681` | `2.6069` | - (order 26) |
| `(h=6, g=6)` | `6, 36, 161, 581, 1792, 4900, 12174, 28021` | `2.4123` | - (order 31) |

*(A tower-spacing skyline with spacing `g` is one whose heights minus 1 are the window-`g` running minimum of some array, so the `(h, g)` count is Hardin's count of "0..(h−1) arrays, each element the minimum of `g` adjacent elements", proved on [[tower-spacing-castles](pages/tower-spacing-castles.md)]. The `h = 3` row is Hardin's table [A217883](https://oeis.org/A217883), the `h = 4` row [A217954](https://oeis.org/A217954), and the `g = 3` column [A228461](https://oeis.org/A228461). Every cell agrees with the OEIS data at the stated offset for `w ≤ 24`, and its minimal recurrence order, found by Berlekamp-Massey on 90 terms, is `(h − 1)g + 1`, 2026-10-16.)*

### The Pell castle strip: 1-smooth strips on {1, 2, 3}

Skylines on `{1, 2, 3}` whose neighboring heights differ by at most 1 ([[pell-castle-strip](pages/pell-castle-strip.md)]); the condition on the end columns picks the sequence.

| object | first terms (`w = 1…`) | growth | OEIS |
|---|---|---|---|
| first column at height 1 | `1, 2, 5, 12, 29, 70, 169, 408` | `1+√2` | [A000129](https://oeis.org/A000129) Pell numbers (`= P⋆_w`; width g.f. `x/(1−2x−x²)`) |
| any first column | `3, 7, 17, 41, 99, 239, 577, 1393` | `1+√2` | [A001333](https://oeis.org/A001333) Pell-Lucas numbers (`= A001333(w+1)`) |
| both end columns at height 1 | `1, 1, 2, 4, 9, 21, 50, 120` | `1+√2` | [A171842](https://oeis.org/A171842) (`= A171842(w−1)`, "Motzkin n-paths of height <= 2"; [[motzkin-castles](pages/motzkin-castles.md)]) |
| **Pell castles**: first column at height 1, height 3 | `0, 0, 1, 4, 13, 38, 105, 280, 729` | `1+√2` | [A094706](https://oeis.org/A094706) (`= A094706(w−2) = P⋆_w − 2^{w−1}`, g.f. `x³/((1−2x−x²)(1−2x))`, proved) and column 2 of [A283595](https://oeis.org/A283595) (Motzkin prefixes by height, row `w − 1`); [[pell-castle](pages/pell-castle.md)] |
| any first column, height 3 | `1, 3, 9, 25, 67, 175, 449, 1137` | `1+√2` | [A106514](https://oeis.org/A106514) (`= A106514(w−1)`, g.f. `x(1−x)/((1−2x)(1−2x−x²))`, proved) |
| both end columns at height 1, height 3 | `0, 0, 0, 0, 1, 5, 18, 56, 161, 441` | `1+√2` | column 2 of [A097862](https://oeis.org/A097862) (Motzkin paths by height, row `w − 1`; g.f. `x⁵/((1−x)(1−2x)(1−2x−x²))`, the partial sums of the Pell castles shifted by 2) |
| even-block / odd-block Pell castles | `0, 0, 0, 0, 2, 13, 51, 154, …` / `0, 0, 1, 4, 11, 25, 54, 126, …` | `1+√2` | - (order 8 each; [[pell-castle](pages/pell-castle.md)]) |
| signed Pell castles (even − odd) | `0, 0, −1, −4, −9, −12, −3, 28, 71, 72, …` | `√3` | - (denominator `(1−x)(1−2x+2x²)(1−2x+3x²)`) |

*(Every row agrees with a transfer-matrix count for `w ≤ 24`, and every A-number row with the OEIS data at the stated offset, 2026-10-16.)*

### 1-smooth castles of height h

The 1-smooth rule on `{1, …, h}` ([[1-smooth-castles](pages/1-smooth-castles.md)]) extends the Pell rows to `h = 2, …, 12`. `strips(w, h)` counts the skylines on `{1, …, h}` with first column at height 1, and `smooth(w, h)` those of height `h`, with g.f. `x^h/(η_h η_{h−1})`.

| object | first terms | growth | OEIS |
|---|---|---|---|
| `smooth(w, h)`, first column at height 1, height `h` | `h = 4`: `0, 0, 0, 1, 5, 19, 64, 202, 612`; one row per `h` on the concept page | `1 + 2cos(π/(h+1))` | column `h − 1` of [A283595](https://oeis.org/A283595) (Motzkin prefixes by height, row `w − 1`; checked for `h ≤ 7`, `w ≤ 14`); the row `h = 2` is [A000225](https://oeis.org/A000225)(`w − 1`) |
| `strips(w, 4)` | `1, 2, 5, 13, 34, 89, 233` | `φ²` | [A001519](https://oeis.org/A001519) (`= A001519(w) = F_{2w−1}`) |
| `strips(w, 5)` | `1, 2, 5, 13, 35, 95, 259, 707` | `1+√3` | [A057960](https://oeis.org/A057960) (`= A057960(w−1)`) |
| `strips(w, 6)` | `1, 2, 5, 13, 35, 96, 266, 741` | `1+2cos(π/7)` | [A085810](https://oeis.org/A085810) (`= A085810(w)`, corridor of height 5) |
| `strips(w, h)`, `h = 7…12` | `h = 7`: `1, 2, 5, 13, 35, 96, 267, 749, 2113, 5982` | `1+2cos(π/(h+1))` | - (each agrees with [A005773](https://oeis.org/A005773) exactly for `w ≤ h`) |
| even-block / odd-block, `h = 4` | `1, 5, 16, 42, 106, 287, 843, 2535` / `0, 0, 3, 22, 96, 325, 960, 2670` (from `w = 4`) | `φ²` | - (order 11 each) |
| even-block / odd-block / signed, `h = 2` | `1, 3, 6, 10, 16, 28, 56, 120` / `0, 0, 1, 5, 15, 35, 71, 135` / `1, 3, 5, 5, 1, −7, −15, −15` (from `w = 2`) | `2` / `2` / `√2` | [A038505](https://oeis.org/A038505)(`w`), [A038503](https://oeis.org/A038503)(`w`) `− 1` and [A077860](https://oeis.org/A077860)(`w − 2`): deleting the first column gives all castles of height 2 and width `w − 1` |
| even-block / odd-block / signed, `h = 5…12` | on the concept page | `1 + 2cos(π/(h+1))` | - (orders and signed growth for every `h` on the concept page) |
| both end columns at height 1, height `h` | `h = 4`: `1, 7, 33, 129, 453, 1485` from `w = 7` | `1 + 2cos(π/(h+1))` | column `h − 1` of [A097862](https://oeis.org/A097862) (row `w − 1`, checked for `h ≤ 7`, `w ≤ 14`; g.f. `x^{2h−1}/(χ_h χ_{h−1})`) |
| any first column, height `h = 4…12` | `h = 4`: `1, 3, 9, 27, 79, 227, 643, 1801, 4999` | `1 + 2cos(π/(h+1))` | [A188866](https://oeis.org/A188866)`(h − 1, w) − A188866(h − 2, w)`, the difference of two rows of the smooth-word table |
| last column within 1 of the first (cyclic), height `h` | `A002426(w)` for `w ≤ 2h − 1`; `h = 3` from `w = 6`: `135, 351, 899, 2275, 5703` | `1 + 2cos(π/(h+1))` | [A002426](https://oeis.org/A002426)(`w`) for `w ≤ 2h − 1` (central trinomial coefficients) |

### m-smooth castles of height h

Skylines whose neighboring columns differ by at most `m`, with first column at height 1 ([[m-smooth-castles](pages/m-smooth-castles.md)]), for `m = 2, 3, 4`. For `h ≤ m + 1` every skyline qualifies, so with the first column at height 1 the castles of width `w ≥ 2` and height `h` number `h^{w−1} − (h−1)^{w−1}`; with any first column they number `A(w, h) = h^w − (h−1)^w`, with even-block part `A^e(w, h)`.

| object | first terms (`w = 1…`) | growth | OEIS |
|---|---|---|---|
| strips on the diagonal `h = m + 2`, `m = 2` | `1, 3, 11, 39, 139, 495, 1763` | `(3+√17)/2` | [A007482](https://oeis.org/A007482) (`= A007482(w−1)`, g.f. `1/(1−3x−2x²)`) |
| strips, `h = m + 2`, `m = 3` | `1, 4, 19, 88, 409, 1900` | `2+√7` | [A015530](https://oeis.org/A015530) (`= A015530(w)`, "Expansion of x/(1 - 4*x - 3*x^2)") |
| strips, `h = m + 2`, `m = 4` | `1, 5, 29, 165, 941, 5365` | `(5+√41)/2` | [A015537](https://oeis.org/A015537) (`= A015537(w)`, "Expansion of x/(1 - 5*x - 4*x^2)") |
| castles, `m = 2`, height 4 | `0, 0, 2, 12, 58, 252, 1034, 4092, 15802` | `(3+√17)/2` | - (g.f. `2x³/((1−3x−2x²)(1−3x))`) |
| castles, `m = 2`, triangle by `(w, h)` | `1; 1, 1, 1; 1, 3, 5, 2, 1; 1, 7, 19, 12, 8, 3, 1; …` | - | - |
| strips, `m = 2`, `h = 5` | `1, 3, 12, 47, 185, 728, 2865, 11275` | `≈ 3.9354` | [A088132](https://oeis.org/A088132)(`w − 1`) (g.f. `(1 − x)/(1 − 4x + x³)`) |
| first column at height 1, no ceiling, `m = 2` / both end columns at height 1, no ceiling, `m = 2` | `1, 3, 12, 51, 226, 1025, 4724` / `1, 1, 3, 9, 32, 120, 473` | - | [A180898](https://oeis.org/A180898)(`w`) and [A104184](https://oeis.org/A104184)(`w − 1`), walks with steps `−2, …, 2` above the axis ([[banderier-nicodeme-2010-bounded-discrete-walks](pages/banderier-nicodeme-2010-bounded-discrete-walks.md)]) |
| castles of height `h ≥ m + 2`, other rows; their parity splits; rows with free and pinned ends | on the concept page | `ρ_{h,m}` | - |

*(Every row agrees with a transfer-matrix count for `w ≤ 24`, 2026-10-16.)*

### Motzkin castles

A **Motzkin-path castle** is a 1-smooth skyline (`|c_{i+1} − c_i| ≤ 1`) with both end columns at height 1 ([[motzkin-castles](pages/motzkin-castles.md)]). Its heights minus 1 form a Motzkin path of length `w − 1`, and its block count is `1 + #up-steps`, so the even-block castles are the Motzkin paths with an odd number of up-steps.

| object | first terms | growth | OEIS |
|---|---|---|---|
| Motzkin-path castles by width | `1, 1, 2, 4, 9, 21, 51, 127, 323, 835` | `3` | [A001006](https://oeis.org/A001006) (`= M_{w−1}`) |
| even-block Motzkin-path castles | `0, 0, 1, 3, 6, 10, 20, 56, 168, 456, 1137, 2827` | `3` | [A343386](https://oeis.org/A343386) (`= A343386(w−1)`, odd Motzkin paths) |
| odd-block Motzkin-path castles | `1, 1, 1, 1, 3, 11, 31, 71, 155, 379, 1051, 2971` | `3` | [A107587](https://oeis.org/A107587) (`= A107587(w−1)`, even Motzkin paths) |
| signed `Σ(−1)^blocks` | `−1, −1, 0, 2, 3, −1, −11, −15, 13, 77, 86, −144` | `\ | 1±2i\ | = √5` | [A343773](https://oeis.org/A343773) (`= −A343773(w−1)`; `A343773(n) = (−1)^n A007440(n+1)`, the reversion of the Fibonacci g.f.) |
| Motzkin-path castles, heights at most 4 | `1, 1, 2, 4, 9, 21, 51, 127, 322, 826` | `φ²` | [A005207](https://oeis.org/A005207) (`= A005207(w−1) = (F_{2w−3} + F_w)/2`; Kociemba's comment counts these walks) |
| Motzkin-path castles, heights at most 5 | `1, 1, 2, 4, 9, 21, 51, 127, 323, 835, 2187` | `1+√3` | [A094286](https://oeis.org/A094286) (`= A094286(w−1)`; its name is the same condition with heights below 6) |
| 1-smooth, first column at height 1, by width | `1, 2, 5, 13, 35, 96, 267, 750` | `3` | [A005773](https://oeis.org/A005773) (`= A005773(w)`, Motzkin left factors and directed animals) |
| drops of at most 1, last column at height 1, by width | `1, 2, 5, 14, 42, 132, 429` | `4` | [A000108](https://oeis.org/A000108) (`= C_w`) |
| Motzkin-path castles by semi-perimeter (`s = 2…`) | `1, 1, 1, 2, 4, 7, 13, 26, 52, 104, 212, 438` | - | [A023431](https://oeis.org/A023431) (`= A023431(s−2)`, Motzkin paths with no `UD` and no `UU`) |
| drops of at most 1, last column at height 1, by semi-perimeter | `1, 1, 2, 4, 8, 17, 37, 82, 185, 423, 978` | - | [A004148](https://oeis.org/A004148) (`= A004148(s−1)`, peakless Motzkin paths; the mirror image without double rises is Deutsch-Elizalde's RNA-secondary-structure bijection, [[deutsch-elizalde-2016-bargraphs-cornerless-motzkin](pages/deutsch-elizalde-2016-bargraphs-cornerless-motzkin.md)]) |
| drops of at most 1, any ends, by semi-perimeter | `1, 2, 5, 12, 29, 71, 175, 434, 1082, 2709, 6807, 17157` | - | - (in bijection with the valleyless Motzkin meanders of length `s − 2` of [[prodinger-2025-cornerless-motzkin-bargraphs](pages/prodinger-2025-cornerless-motzkin-bargraphs.md)]; refined by last-column height and spires on [[motzkin-castles](pages/motzkin-castles.md)]) |
| 1-smooth, first column at height 1, by semi-perimeter | `1, 1, 2, 4, 8, 16, 33, 69, 145, 307, 655, 1405, 3027` | - | - |
| 1-smooth, any ends, by semi-perimeter | `1, 2, 5, 11, 24, 52, 113, 246, 537, 1176, 2583, 5688` | - | - |

*(Every row agrees with a transfer-matrix count for `w ≤ 24` or with enumeration for `s ≤ 16`, and every A-number row with the OEIS data at the stated offset, 2026-10-16. All castles by semi-perimeter, `A082582`, are cornerless Motzkin paths and are equinumerous with skew Motzkin paths; they are in the section *Castles by semi-perimeter*. Their first five terms `1, 2, 5, 13, 35` agree with `A005773`, and the sixth differs, 97 against 96.)*

### Ridge strips and ridge castles

The ridge rule: neighboring columns differ in height unless both have height `h`, with transfer matrix `R_h = J − D` ([[castle-classification-shape](pages/castle-classification-shape.md)], [[ridge-castle](pages/ridge-castle.md)]). The ridge strips are the skylines on `{1, …, h}` under the rule, and the ridge castles those of height `h`, `𝟙ᵀR_h^{w−1}𝟙 − (h−1)(h−2)^{w−1}` of them; their even-block part is on [[proper-castle-projection](pages/proper-castle-projection.md)].

| object | first terms (`w = 1…`) | growth | OEIS |
|---|---|---|---|
| ridge strips, `h = 3` | `3, 7, 17, 41, 99, 239, 577` | `1+√2`, silver by width | [A001333](https://oeis.org/A001333) Pell-Lucas numbers (`= A001333(w+1)`) |
| ridge strips, `h = 4` | `4, 13, 43, 142, 469, 1549` | `(3+√13)/2`, bronze by width | [A003688](https://oeis.org/A003688) (`= A003688(w+1)`) |
| ridge strips, `h = 5` | `5, 21, 89, 377, 1597, 6765` | `δ_4 = 2+√5 = φ³` | [A015448](https://oeis.org/A015448) (`= A015448(w+1) = F_{3w+2}`) |
| ridge castles of height 4 | `1, 7, 31, 118, 421, 1453, 4924` | `(3+√13)/2` | - |
| even-block ridge castles of height 4 | `1, 7, 25, 70, 209, 697, 2390` | `(3+√13)/2` | - |
| even-block ridge castles of height 5 | `0, 0, 10, 104, 604, 2836, 12630` | `φ³` | - |

*(Every row agrees with a transfer-matrix count for `w ≤ 24`, 2026-10-16.)*

### Signed tower count P(k, ·) rows

The signed tower count `P(k, L) = Σ (−1)^{blocks}` in the base length `L` at fixed tower height `k` ([[signed-tower-count](pages/signed-tower-count.md)]), with a linear recurrence of order `k + 1`. The even-`k` rows are positive (checked `k ≤ 12`, `L < 40`); for odd `k` the roots of largest modulus are a complex-conjugate pair and the rows change sign in runs.

| object | first terms (`L = 0…`) | order | growth | OEIS |
|---|---|---|---|---|
| `P(1, L)` | `1, 0, −2, −4, −4, 0, 8, 16, …` | 2 | `√2` (`1±i`) | [A146559](https://oeis.org/A146559) (`= A146559(L+1) = Re((1+i)^{L+1})`) |
| `P(2, L)` | `1, 1, 3, 9, 19, 33, 59, 121, 259, 529` | 3 | `2` | - |
| `P(3, L)` | `1, 0, −4, −16, −40, −64, −32, 192, 832, …` | 4 | `2.193` (modulus) | - |
| `P(4, L)` | `1, 1, 5, 25, 85, 225, 541, 1385, 3973` | 5 | `2.796` | - |
| `P(5, L)` | `1, 0, −6, −36, −140, −384, −680, −112, 5040, …` | 6 | `2.892` (modulus) | - |
| `P(6, L)` | `1, 1, 7, 49, 231, 833, 2583, 7889, 26503, …` | 7 | `2ψ² = 3.5098` | - (`char_6 = (x³−4x²+4x−8)(x⁴−3x³+8x²−4x+8)`, largest root `2ψ²`, [[plastic-number](pages/plastic-number.md)]) |

*(The characteristic polynomials `char_k` are irreducible for odd `k ≤ 31`, each proved by a prime mod which it stays irreducible ([[castle-cryptography-number-theory](pages/castle-cryptography-number-theory.md)]), and have two irreducible factors for even `k ≤ 14` (computed). The denominators have the closed form `den_k = A·r_+^k + B·r_−^k` with `r_± = −x ± √(x²+1)`, on [[generating-function-gallery](pages/generating-function-gallery.md)].)*

### Strip Perron-root sequences

Width counts of the 0/1 transfer-matrix strips of [[reachable-field-census](pages/reachable-field-census.md)] and [[metallic-strip-realizability](pages/metallic-strip-realizability.md)].

- The plastic strip (height 3, rule `1 → 3`, `2 → 1`, `3 → {1, 2}`), `3, 4, 5, 7, 9, 12, 16, 21, 28, …` from `w = 1`: [A000931](https://oeis.org/A000931) Padovan (`= A000931(w+9)`, checked `w ≤ 40`); these are the maximal Fibonacci castles of width `w + 3`.
- The quadratic strips off the line `p₂ = 1` reach the fields `Q(√17)`, `Q(√21)`, `Q(√6)`, `Q(√7)` and `Q(√33)`, each through several strip matrices, so a field has no single count sequence.

### Castles by semi-perimeter

A castle's semi-perimeter is `s = w + blocks` ([[castle-perimeter](pages/castle-perimeter.md)]), so these are the castle counts in Delest-Viennot's perimeter grading, with the Project Euler parity split. The g.f. are algebraic, and rational for the convex castles.

| object | first terms (`s = 2…`) | g.f. | growth | OEIS |
|---|---|---|---|---|
| all castles (bargraphs) | `1, 2, 5, 13, 35, 97, 275, 794, 2327` | `(1-2t-t²-√(1-4t+2t²+t⁴))/(2t)` | `τ² = 3.38298` (`τ` the tribonacci constant) | [A082582](https://oeis.org/A082582) (`= A082582(s)`, bargraphs by semi-perimeter) |
| castles by `(s, w)` | rows `1; 1,1; 1,3,1; 1,5,6,1; …` | tower Narayana form | - | [A271942](https://oeis.org/A271942) (rows checked for `s ≤ 16`) |
| even-block castles | `0, 1, 3, 7, 17, 47, 137, 400, 1168, 3450, 10338` | `(B + B_s)/2` | `τ²` | - |
| signed castles `Σ(-1)^blocks` | `-1, 0, 1, 1, -1, -3, -1, 6, 9, -5, -29, -20, 55` | `(1+t²-√((1+t)(1-t+3t²+t³)))/(2t)` | `τ` (a complex pair of singularities of modulus `1/τ`) | - |
| convex castles | `1, 2, 5, 13, 34, 89, 233` | `t²(1-t)/(1-3t+t²)` | `φ²` | [A001519](https://oeis.org/A001519) (`= A001519(s−1)`; Delest-Viennot's stacks by perimeter) |
| even-block convex castles | `0, 1, 3, 7, 17, 44, 116, 305, 799, 2091` | `t³(1-t)/((1-3t+t²)(1-t+t²))` | `φ²` | - |
| signed convex castles | `-1, 0, 1, 1, 0, -1` (period 6) | `-t²(1-t)/(1-t+t²)` | periodic | - |
| palindromic castles | `1, 2, 3, 5, 9, 15, 27, 46, 83` | the symmetric-bargraph g.f. ([[deutsch-elizalde-2016-bargraphs-cornerless-motzkin](pages/deutsch-elizalde-2016-bargraphs-cornerless-motzkin.md)] §4.1) | - | [A273905](https://oeis.org/A273905) (`= A273905(s)`, symmetric bargraphs) |
| castles of height 5 with no 1 next to a 2 and no 4 next to a 5, silver by semi-perimeter | `1, 7, 26, 74, 196, 525, 1421, 3809, 10040, 26102, 67250` (from `s = 6`) | rational, denominator `(1 − x)²(1 + x²)(1 − 2x − x²)(1 − x + x² + x³)` | `1 + √2` | - ([[semi-perimeter-growth-census](pages/semi-perimeter-growth-census.md)]) |
| prime castles (no column of height 1) | `0, 1, 2, 5, 13, 35, 97, 275, 794, 2327` | `t·B(t)` | `τ²` | [A082582](https://oeis.org/A082582) (`= A082582(s−1)` for `s ≥ 3`; the row-deletion bijection, [[deutsch-elizalde-2016-bargraphs-cornerless-motzkin](pages/deutsch-elizalde-2016-bargraphs-cornerless-motzkin.md)] §3.9) |

*(Every row agrees with enumeration for `s ≤ 16` and with the series of its g.f., and every A-number row with the OEIS data at the stated offset, 2026-10-16; [[castle-perimeter](pages/castle-perimeter.md)] checks the series through `s = 30`.)*

### Prime castles by area

Gluing castles at a shared column of height 1 makes a free monoid; its primes correspond to the castles with no column of height 1, the prime castles, `F_{n−1}` of them of area `n` ([[prime-castles](pages/prime-castles.md)]). A convex castle has at most one prime factor ([[prime-convex-castles](pages/prime-convex-castles.md)]). Terms from `n = 2` unless stated.

| object | first terms | g.f. / formula | OEIS |
|---|---|---|---|
| prime castles | `1, 1, 2, 3, 5, 8, 13, 21` | `q²/(1−q−q²)` | [A000045](https://oeis.org/A000045) (`= F_{n−1}`; compositions into parts `≥ 2`) |
| prime convex castles `U` | `1, 1, 2, 3, 5, 8, 12, 19, 28, 42, 61, 90` | `Δ² A001523`; `Σ_k q^k/((1−q^k)(q²;q)_{k−2}²)` | - |
| non-convex prime castles `F_{n−1} − U` | `1, 2, 6, 13, 28, 54, 106, 194` (from `n = 8`) |  | - |
| `U` by width | rows `1; 1; 1,1; 1,2; 1,3,1; 1,4,3; 1,5,5,1` | convex castles of area `n − w`, width `w` | - |
| convex castles with first column not at height 1 | `1, 2, 4, 7, 12, 20, 32, 51, 79` | `Δ A001523` | [A342528](https://oeis.org/A342528) (`= A342528(n−1) = A001523(n) − A001523(n−1)`, checked for `n ≤ 1001` against the two b-files) |
| castles of area `n` up to rearranging prime factors | `1, 2, 3, 5, 9, 15, 26, 45, 78, 134, 233` (from `n = 1`) | `Σ_n a(n) q^{n+1} = Π_j (1−q^j)^{−π_j} − 1`, with `π_j` the number of prime castles of area `j − 1` and `π_1 = 1` | - ([[signed-prime-castles](pages/signed-prime-castles.md)]) |
| prime parity splits (all and convex) | on the two pages |  | - |
| signed castles by area `even − odd` | `-1, 0, 0, 2, 0, 2, -4, 2, -12, 10, -20, 38` (from `n = 1`; 300 terms computed) | the row-raising recursion; `~ C(−ρ)^n` | - ([[castle-row-raising-equation](pages/castle-row-raising-equation.md)]) |
| signed growth constant `ρ` and prefactor `C` | `1.62382967400459...`, `0.09850917497311...` | pole at `q E(q, q) = 1`, the first zero of `M(q)` on [[castle-q-bessel-closed-form](pages/castle-q-bessel-closed-form.md)] | - |
| second signed singularity `q_1` | `-0.82027198` | second zero of `M(q)`; correction `O(0.7508^n)` | - ([[castle-q-bessel-closed-form](pages/castle-q-bessel-closed-form.md)]) |
| castles by area and peaks | rows `1; 1,1; 1,3; 1,7; 1,14,1; 1,26,5` | `(1−q−q²+tq²)/(1−2q+q³−tq³)` | - |
| one-peak castles | `1, 3, 7, 14, 26, 46, 79, 133` | `q²/((1−q)²(1−q−q²))` | [A001924](https://oeis.org/A001924) (`= A001924(n−1)`) |

*(A peak is a maximal run of columns of height at least 2. Every row agrees with enumeration of compositions for `n ≤ 15`, 2026-10-16.)*

### Classical polyomino families among castles, by area

The classical polyomino families intersected with the castles ([[castle-add-a-column-equation](pages/castle-add-a-column-equation.md)]): a monotone castle is a Ferrers or reverse-Ferrers skyline. Terms from `n = 1`.

| object | first terms | g.f. / formula | OEIS |
|---|---|---|---|
| monotone castles (weakly increasing or weakly decreasing) | `1, 2, 4, 7, 12, 18, 28, 40, 57, 80, 110, 148` | `2p(n) − d(n)` | [A329398](https://oeis.org/A329398) (defined by Lyndon factorizations; the entry proves that these are the weakly monotone compositions, so `a(n) = 2A000041(n) − A000005(n)`) |
| non-monotone castles | `0, 0, 0, 1, 4, 14, 36, 88, 199, 432` | `2^{n−1} − 2p(n) + d(n)` | [A332834](https://oeis.org/A332834) (compositions neither weakly increasing nor weakly decreasing) |
| signed monotone castles `even − odd` | `-1, 0, 0, 1, 0, 2, 0, 2, -1, 4, -2, 4, -4, 6` | `2(−1)^n A000700(n) − Σ_{d\ | n} (−1)^d` | - |

*(Every row and formula agrees with enumeration of compositions for `n ≤ 15`, 2026-10-16.)*

### Odd-block counts, parity-refined area, and joint block tables

The remaining rows of the first mining pass; full terms on [[odd-castles-and-block-tables](pages/odd-castles-and-block-tables.md)].

| object | first terms | g.f. / formula | OEIS |
|---|---|---|---|
| `A^o(w, h)` rows, `h = 3..7` | `h = 3`: `1, 5, 16, 44, 122, 358, 1082, 3274` | `(A + P(h−1, w) − P(h−2, w))/2`; order 5, 9, 11, 13, 15 | - |
| columns `A^o(4..6, h)`, `A^e(5, h)`, `A^e(6, h)` | `A^o(4, h)`: `1, 5, 44, 58, 247, 223, 738, 564` | a polynomial in `h` plus `(−1)^h` times a polynomial in `h` | - |
| even, odd, convex, valley, non-convex and strict-valley castles by area, split by parity, and their signed differences | on the page | `cev + cod = A001523`, `valley_even + valley_odd = A332578`, `nc_even + nc_odd = A115981` | - |
| castles by area and blocks, triangle | rows `1; 1,1; 1,2,1; 1,4,2,1; 1,6,6,2,1` | column `b` rational for `b ≤ 4` | - |
| two-block castles by area | `1, 2, 4, 6, 9, 12, 16, 20, 25` (from `n = 2`) | `q²/((1−q)²(1−q²))` | [A002620](https://oeis.org/A002620) quarter-squares (`= A002620(n)`) |
| three-block castles with one peak, by area | `1, 2, 5, 9, 16, 25, 39, 56, 80` (from `n = 3`) | `q³/((1−q)²(1−q²)²(1−q³))` | [A097701](https://oeis.org/A097701) (`= A097701(n−3)`) |
| three-block castles with two peaks, by area | `1, 3, 8, 16, 30, 50, 80, 120, 175` (from `n = 5`) | `q⁵/((1−q)³(1−q²)²)` | [A002624](https://oeis.org/A002624) (`= A002624(n−5)`) |
| three-, four- and five-block columns; other cells by blocks and peaks | on the page | rational | - |
| castles of width `w` and height `h` with `h + 1` blocks | `h = 3`: `3, 21, 84, 252, 630, 1386` (from `w = 3`) | `(2h−3) C(w+2h−3, 2h)` | [A253943](https://oeis.org/A253943) at `h = 3` (`= A253943(w+2) = 3 C(w+3, 6)`); at `h = 4`: `5, 45, 225, 825, 2475, 6435` |
| castles of width `w` and height `h` by blocks, triangles `h = 3, 4`, and the column `h + 2` | `h = 3` rows from `b = 3`: `1; 5; 15,3,1; 35,21,9; 70,84,51,5,1` | first three columns in closed form | - |

*(The `h = 3` rows and the rows by area agree with enumeration for `w ≤ 8` and `n ≤ 15`, 2026-10-16.)*

### Half-sum rows

The binomial half-sum of `A^e(w, h)` in the width ([[half-sum-castles](pages/half-sum-castles.md)]), `K_h(w) = Σ_k C(2k, k) A^e(w − k, h)`, with g.f. `G_h(x)/√(1 − 4x)`. Terms from the first nonzero width.

| object | first terms | growth | OEIS |
|---|---|---|---|
| `K_2` | `1, 5, 18, 60, 202, 702, 2508, 9136, 33742, 125934` | `4` | - |
| `K_3` | `3, 27, 149, 671, 2755, 10833, 41679, 158465, 598681` | `4` | - |
| `K_4` | `1, 9, 51, 241, 1069, 4671, 20353, 88383, 381583, 1635893` | `4`, with `K_4(w) ~ 4^w √(w/π)`, so `π = lim w·16^w/K_4(w)²` | - |
| `K_5` | `10, 142, 1210, 8222, 49806, 283570, 1557158, 8354490` | `5` | - |
| dyadic half-sum `4^w H_h(w)`, `h = 2..5`, and the numerators of `H_2`, `1, 7, 63, 231, 3131, 10929` | on the page | `4h` | - |

### Tree castles by area at fixed height

Tree castles, the castles with no `2 × 2` square, of height 2 and of height at most `h ≥ 3`, by area `n` ([[tree-castle-by-area](pages/tree-castle-by-area.md)]). For `h ≥ 3` the count at area `n` is the number of compositions of `n + 1` into parts `{1, 3, 4, …, h + 1}`; at height 2 it is the number of compositions of `n + 1` into parts `{1, 3}` that use a 3. Terms from `n = 1`. Without a bound on the height the count is `A005251(n+2)` (section *Multi-interpretation hub*).

| object | first terms | g.f. / formula | OEIS |
|---|---|---|---|
| height 2 | `0, 1, 2, 3, 5, 8, 12, 18, 27, 40` | parts `{1, 3}`, using a 3; `A000930(n+1) − 1` | [A077868](https://oeis.org/A077868) (`= A077868(n−2)`, `n ≥ 2`) |
| height at most 3 | `1, 2, 4, 6, 9, 15, 25, 40, 64, 104` | parts `{1, 3, 4}` | [A006498](https://oeis.org/A006498) (`= A006498(n+1)`) |
| height at most 4 | `1, 2, 4, 7, 11, 18, 31, 53, 89, 149` | parts `{1, 3, 4, 5}` | [A000570](https://oeis.org/A000570), tournaments determined by their score vectors (`= A000570(n+1)`) |
| height at most 5 | `1, 2, 4, 7, 12, 20, 34, 59, 102, 175` | parts `{1, 3, …, 6}` | [A079816](https://oeis.org/A079816) (`= A079816(n+1)`) |
| height at most 6 | `1, 2, 4, 7, 12, 21, 36, 62, 108, 188` | parts `{1, 3, …, 7}` | [A189593](https://oeis.org/A189593) (`= A189593(n+1)`; the composition reading proves the entry's empirical recurrence) |
| height at most 7 | `1, 2, 4, 7, 12, 21, 37, 64, 111, 194` | parts `{1, 3, …, 8}` | [A189600](https://oeis.org/A189600) (`= A189600(n+1)`) |
| height at most 8 | `1, 2, 4, 7, 12, 21, 37, 65, 113, 197, 345, 604, 1056, 1846` | parts `{1, 3, …, 9}` | - |

*(Every row agrees with enumeration for `n ≤ 15` and with the OEIS data at the stated offset, 2026-10-16.)*

### Sandpile groups

The sandpile groups of the castles with at most 16 cells, mirror images identified, in both models: `K_sink`, with one cell as the sink, and `K_tide`, with the bottom row as the sink ([[sandpile-census](pages/sandpile-census.md)]). Terms by number of cells from `n = 1`.

| object | first terms | g.f. / formula | OEIS |
|---|---|---|---|
| castles, mirror images identified (the castles of the census) | `1, 2, 3, 6, 10, 20, 36, 72, 136, 272, 528, 1056, 2080, 4160, 8256, 16512` | `(2^{n−1} + 2^{⌊n/2⌋})/2` | [A005418](https://oeis.org/A005418) compositions of `n` up to direction ([[castle-graph](pages/castle-graph.md)]) |
| castles with trivial group (the tree castles, in both models) | `1, 2, 3, 5, 8, 13, 22, 37, 63, 108, 186, 322, 559, 973, 1697, 2964` | `(A005251(n+2) + A000931(n+6))/2` | [A005683](https://oeis.org/A005683) Twopins positions (`= A005683(n+2)`; the formula agrees with the b-file for `n ≤ 38`) |
| palindromic tree castles | `1, 2, 2, 3, 4, 5, 7, 9, 12, 16, 21, 28, 37, 49, 65, 86` | `A000931(n+6)` | [A000931](https://oeis.org/A000931) Padovan |
| castles with cyclic `K_sink` | `1, 2, 3, 6, 10, 20, 36, 72, 134, 264, 503, 997, 1933, 3791, 7338, 14329` |  | - |
| distinct groups `K_sink` among castles of `n` cells | `1, 1, 1, 2, 2, 3, 3, 4, 6, 8, 10, 13, 18, 25, 34, 48` |  | - |
| castles with cyclic `K_tide` | `1, 2, 3, 6, 10, 20, 36, 72, 135, 268, 513, 1015, 1975, 3902, 7631, 15028` |  | - |
| distinct groups `K_tide` among castles of `n` cells | `1, 1, 1, 2, 2, 4, 4, 7, 9, 14, 18, 27, 38, 56, 78, 113` |  | - |
| `\ | K_sink\ | ` of the ladder of width 2, lying `(2, …, 2)` by width or standing `(h, h)` by height | `1, 4, 15, 56, 209, 780` | `a(n) = 4a(n−1) − a(n−2)`, cyclic | [A001353](https://oeis.org/A001353) (spanning trees of the `2 × n` grid) |
| `\ | K_tide\ | ` of the lying ladder `(2, …, 2)` by width | `1, 3, 8, 21, 55, 144` | `a(n) = 3a(n−1) − a(n−2)`, cyclic | [A001906](https://oeis.org/A001906) `F_{2n}` (`= A001906(w)`; every block on the ground) |
| `\ | K_tide\ | ` of the standing ladder `(h, h)` by height | `1, 3, 11, 41, 153, 571` | `a(n) = 4a(n−1) − a(n−2)`, cyclic | [A001835](https://oeis.org/A001835) (`= A001835(h)`; one block on the ground) |

*(Every row agrees with Smith normal forms of the reduced Laplacians of all castles with at most 16 cells, in both models, 2026-10-16.)*

### Fibonacci castle sub-families

Fibonacci castles, the castles of height 2 with no two neighboring columns of height 2, selected by a rule on their towers; terms by width from `w = 1` ([[fibonacci-castles-sub-families](pages/fibonacci-castles-sub-families.md)]).

| object | first terms | g.f. / formula | OEIS |
|---|---|---|---|
| Fibonacci-word castles (tower a factor of the Fibonacci word) | `1, 2, 4, 5, 6, 7, 8, 9` | `w + 1` for `w ≥ 3` (Sturmian complexity) | - (linear) |
| balanced castles | `1, 2, 4, 7, 12, 18, 27, 38, 52, 68, 89, 112` | `A005598(w)/2`, `~ w³/(2π²)` | [A049703](https://oeis.org/A049703) (`= A049703(w)`) |
| maximal castles (no column can be raised) | `1, 2, 2, 3, 4, 5, 7, 9, 12, 16, 21, 28` | `x(1+x)²/(1−x²−x³)` | [A000931](https://oeis.org/A000931) (`= A000931(w+6)`; the entry counts the maximal independent vertex sets of the path graph) |
| spaced castles (columns of height 2 at least 3 apart) | `1, 2, 3, 5, 8, 12, 18, 27, 40, 59` | `A000930(w+2) − 1` | [A077868](https://oeis.org/A077868) (`= A077868(w−1)`); the bijection with the Fibonacci castles of `w + 1` cells is on the page |
| `(1, 3)`-RLL castles | `1, 2, 4, 7, 10, 15, 22, 32, 47, 69` | `x(1+x)(1+x²)²/(1−x−x³)` | [A003410](https://oeis.org/A003410) (`= A003410(w)` for `w ≥ 4` and `A003410(w) − 1` for `w ≤ 3`; the entry counts the binary words with no `11` and no `0000`, the towers); [A226136](https://oeis.org/A226136), whose terms equal the castle counts |
| `(1, 7)`-RLL castles | `1, 2, 4, 7, 12, 20, 33, 54, 86, 138, 221` | gap generating function | - |
| `(2, 7)`-RLL castles | `1, 2, 3, 5, 8, 12, 18, 27, 38, 54, 78` | gap generating function | - |
| `(2, 10)`-RLL castles | `1, 2, 3, 5, 8, 12, 18, 27, 40, 59, 87, 126, 183` | gap generating function | - |

*(A tower is `(d, k)`-run-length-limited when the runs of 0s between consecutive 1s have length at least `d` and every run of 0s, the end runs included, has length at most `k`. Every row agrees with enumeration of the towers for `w ≤ 14`, 2026-10-16.)*

### Other rows

- `A^e(w, 3)`, the even-block castles of height 3, `0, 0, 3, 21, 89, 307, 977, 3031, …` ([[new-sequence-fw3](pages/new-sequence-fw3.md)]).
- The rows `A^e(w, 4) = 1, 7, 31, 117, 439, 1729, 7063, 29201, …`, `A^e(w, 5) = 0, 0, 10, 122, 906, 5478, 30274, …` and `A^e(w, 6) = 1, 11, 76, 448, 2630, 16126, 101654, …` of the array `A^e(w, h)`.
- The odd-block rows `A^o(w, 3) = 1, 5, 16, 44, 122, 358, 1082, 3274, …` and `A^o(w, 4) = 0, 0, 6, 58, 342, 1638, 7134, …`.
- Columns of width 3 ([[sum-of-three-cubes-castles](pages/sum-of-three-cubes-castles.md)]): `A^e(3, 2m) = 10m² − 5m + 1 = 5m(2m − 1) + 1`, `6, 31, 76, 141, 226, 331, 456, 601, 766, 951, …`, which is `A080860(−m)`. `A^o(3, 2n+1) = 10n² + 5n + 1`, `1, 16, 51, 106, 181, 276, …`, is [A080860](https://oeis.org/A080860)(`n`). `A^e(3, 2m+1) = C(2m+1, 2) = m(2m+1)` are the second hexagonal numbers [A014105](https://oeis.org/A014105), and `A^o(3, 2m) = C(2m, 2) = m(2m − 1)` the hexagonal numbers [A000384](https://oeis.org/A000384). The interleaved columns are `A^e(3, h)` (`6, 3, 31, 10, 76, 21, …` from `h = 2`), `A^o(3, h)` (`1, 1, 16, 6, 51, 15, …` from `h = 1`) and `A^e(4, h)` (`10, 21, 117, 122, 448, 367, 1131, 820, …` from `h = 2`). `A^e(4, h)` is `(4h−3)(4h²−3h+2)/6` at even `h` and `(h−1)(8h²−4h+3)/6` at odd `h` (checked `h < 30`).
- `|P(k, L)|` in the tower height `k` at fixed `L ≥ 5` ([[castle-eigenvalue-oeis-crosswalk](pages/castle-eigenvalue-oeis-crosswalk.md)]): `|P(k, 5)| = 1, 0, 33, 64, 225, 384, 833, 1280, 2241, …` and `|P(k, 6)| = 1, 8, 59, 32, 541, 680, 2583, 3520, …` from `k = 0`. The rows in `L` are in the section *Signed tower count P(k, ·) rows*.
- The parity-refined sequences by area (even and odd; convex, valley, non-convex and strict-valley) ([[castle-by-area](pages/castle-by-area.md)]); terms on [[odd-castles-and-block-tables](pages/odd-castles-and-block-tables.md)].
- The towers of width `w ≥ 6` by number of blocks `b` ([[tower-narayana-polynomial](pages/tower-narayana-polynomial.md)]): `w = 6`: `1, 21, 161, 721, 2331, 6083, …`; `w = 7`: `1, 28, 280, 1582, 6244, 19348, …` from `b = 0`.
- The denominators of the Jacobi-Perron convergents of `2ψ²` ([[castle-eigenvalue-oeis-crosswalk](pages/castle-eigenvalue-oeis-crosswalk.md)]): `1, 1, 2, 4, 47, 53, 104, 204, 2409, 2717, 5330, …`.

## Appearances in Sources

- [[oeis-mining-pe502](pages/oeis-mining-pe502.md)] - the first mining pass, the source of the difference-of-powers, height-2, signed tower, convex and area rows.

## Related Concepts

- [[oeis-index](pages/oeis-index.md)] - the generated directory of every A-number cited on the wiki, with the citing pages.
- [[oeis-cross-referencing](pages/oeis-cross-referencing.md)] - the checks a match must pass: the offset, and agreement beyond a short prefix.
- [[oeis-height2-hyperbolic-castles](pages/oeis-height2-hyperbolic-castles.md)] - the height-2 rows `A038505` and `A038503`.
- [[hyperbolic-sequence-family](pages/hyperbolic-sequence-family.md)] - the four sums of every fourth binomial coefficient, `A038503`, `A038504`, `A038505`, `A000749`.
- [[metallic-means](pages/metallic-means.md)] / [[pell-numbers](pages/pell-numbers.md)] / [[plastic-number](pages/plastic-number.md)] - the metallic means, the Pell numbers and the plastic number, the growth constants of several rows.
- [[castle-graph](pages/castle-graph.md)] - the tree castles and tree skylines by width (`A001045`, `A006130`, `A006131`).
- [[castle-eigenvalue-oeis-crosswalk](pages/castle-eigenvalue-oeis-crosswalk.md)] - the convergents of castle eigenvalues against the OEIS, `|P(k, 4)| = A352116(k+1)`, and the Jacobi-Perron expansion of `2ψ²`.
- [[hardin-word-identity](pages/hardin-word-identity.md)] - the Hardin sequences `A202882`, `A203094`, `A203184` and the proof of their recurrences.
- [[new-sequence-fw3](pages/new-sequence-fw3.md)] - the row `A^e(·, 3)`.
- [[castles-of-height-h-by-area](pages/castles-of-height-h-by-area.md)] - castles by area with bounded height and the n-nacci numbers.
- [[tower-spacing-castles](pages/tower-spacing-castles.md)] - the tower-spacing skylines and Hardin's running-minimum arrays.
- [[proper-castle-projection](pages/proper-castle-projection.md)] - the even-block ridge castles.
- [[reachable-field-census](pages/reachable-field-census.md)] - the strip Perron roots and the fields they reach.
- [[odd-castles-and-block-tables](pages/odd-castles-and-block-tables.md)] - the odd-block rows, the parity splits by area, and the tables by blocks and peaks.
- [[a005251-bijection](pages/a005251-bijection.md)] - the bijection between the readings of `A005251`.
- [[oeis-mining-seminar](pages/oeis-mining-seminar.md)] - a seminar that takes one row through the method.
- [[motzkin-castles](pages/motzkin-castles.md)] - the Motzkin rows: cornerless Motzkin paths, the parity split of `M_{w−1}`, the Motzkin paths of bounded height, and the rows by semi-perimeter.

## Footnotes

[^1]: Verified by execution (Python 3.11 with SymPy, 2026-10-16 and 2026-10-22): every row with listed terms recomputed by enumeration, transfer matrix or dynamic program at the ranges stated under each table; every cited A-number fetched from oeis.org and compared with the computed terms at the stated offset.
