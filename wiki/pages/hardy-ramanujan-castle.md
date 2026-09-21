---
title: The Hardy-Ramanujan castle (1729)
category: Analyses
summary: 1729, the taxicab number 1^3+12^3 = 9^3+10^3, is a castle count - F(6,4) = 1729 exactly, the only cell with w,h <= 40 where the Hardy-Ramanujan number appears, and A(6,4) = 16^3 - 9^3 is a difference of cubes in the same cell. The sum-of-three-cubes reading 9^3 + 10^3 + (-12)^3 = 1 opens onto Ramanujan's near-miss family x^3+y^3 = z^3 +- 1, which is a C-finite sequence with denominator (1+x)(1-83x+x^2): Berlekamp-Massey recovers it from the terms, and its growth constant (83+9 sqrt 85)/2 is the SQUARE of the ninth metallic mean delta_9 = (9+sqrt 85)/2 - the Perron root of the height-10 ceiling-exception castle strip. Also on the page - 1729 read as a castle (the base-10 digit castle (1,7,2,9) is a valid even-block castle of area 19 and is Ramanujan in the spectral sense), the first four Carmichael numbers 561, 1105, 1729, 2465 all as castle counts, and F(w,h) mod 1729 with periods 72, 2520, 25200 at h = 2, 3, 4.
tags: [analysis, castle, 1729, taxicab, hardy-ramanujan, sum-of-cubes, near-miss, c-finite, berlekamp-massey, metallic-mean, carmichael, mod-p, worked-example, computation]
sources: [oeis-mining-pe502, project-euler-502-solution]
created: 2026-09-19
updated: 2026-09-20
---

# The Hardy-Ramanujan castle (1729)

1729 is the taxicab number: the smallest integer that is a sum of two positive cubes in two ways, `1^3 + 12^3 = 9^3 + 10^3`. Hardy told the story - he arrived at Ramanujan's bedside in Putney in taxi number 1729 and remarked that it seemed a dull number; Ramanujan answered that it was "the smallest number expressible as the sum of two cubes in two different ways."[^1] This page asks what 1729 has to do with castles, and finds more than expected. The headline: **`F(6,4) = 1729`**. The Project Euler 502 count of even-block castles of width 6 and height exactly 4 is the Hardy-Ramanujan number, and it is the only place the number appears in the `A`, `F`, or odd tables for `w, h <= 40`. The deeper thread runs through the sum of three cubes `9^3 + 10^3 + (-12)^3 = 1` into Ramanujan's family of near-misses to Fermat, which turns out to be a linear recurrence whose growth constant sits on the wiki's metallic ladder.

Not to be confused with [[ramanujan-castles](pages/ramanujan-castles.md)], which is about the spectral Ramanujan property (expander-like adjacency spectra) of individual castle graphs. The two pages meet once, in the section on 1729 as a castle: the digit castle `(1, 7, 2, 9)` is Ramanujan in that sense too.

Every number below was computed while writing and re-run for the final tables; the scripts are described in the execution footnote.[^exec]

## The number 1729

| property | statement | source |
|---|---|---|
| taxicab `Ta(2)` | `1^3 + 12^3 = 9^3 + 10^3 = 1729`; first nontrivial term of A001235 `1729, 4104, 13832, 20683, ...`; the two representations were published by Frenicle de Bessy in 1657 | [^1] [^2] |
| `12^3 + 1` | `1729 = 1728 + 1`, so `9^3 + 10^3 = 12^3 + 1` is a near-miss to Fermat's cubic case; first term of A050794 (`x^3 + y^3 = z^3 + 1`, `1 < x < y < z`) | [^3] |
| factorization | `1729 = 7 * 13 * 19 = 13 * 133 = (12 + 1)(12^2 - 12 + 1) = Phi_2(12) * Phi_6(12)` | [^exec] |
| Carmichael | third Carmichael number (A002997: `561, 1105, 1729, 2465, ...`); `a^1728 = 1 (mod 1729)` for every `a` coprime to 1729, checked exhaustively; Korselt: `6, 12, 18` all divide `1728` | [^4] [^exec] |
| centered cube | `9^3 + 10^3` is by definition the centered cube number with `n = 9` | [^1] |
| Harshad | digit sum `1 + 7 + 2 + 9 = 19` divides 1729 (`1729 = 19 * 91`) | [^exec] |
| palindromic bases | `1001` in base 12, `1 22 1` in base 32, `1 12 1` in base 36 | [^1] [^exec] |
| Ono, Trebat-Leder | Ramanujan's notes on `a^3 + b^3 = c^3 + d^3` around 1729 contain a K3 surface of Picard number 18 giving infinitely many cubic twists of rank at least 2 | [^5] |

The cubic root is `1729^(1/3) = [12; 432, 12, 648, 9, ...]`, whose huge second partial quotient is the whole content of Feynman's party trick (`1729.03^(1/3) = 12.0000694...` by linearizing at `12^3 = 1728`).[^exec]

## 1729 is a castle count: the `(6, 4)` cell

The `F(w, 4)` row of the brute-force tabulation reads `1, 7, 31, 117, 439, 1729, 7063, 29201, ...`, so `F(6, 4) = 1729`.[^6] Re-derived here from scratch by enumerating all `4^6 - 3^6 = 3367` column-height vectors in `{1..4}^6` with some column at height 4, and counting blocks by `c_1 + sum max(0, c_i - c_{i-1})` ([[castle-snippets](pages/castle-snippets.md)]):[^exec]

| quantity at `(w, h) = (6, 4)` | value | factorization |
|---|---|---|
| `A(6,4) = 4^6 - 3^6` | 3367 | `7 * 13 * 37 = 91 * 37` |
| `F(6,4)` (even blocks) | **1729** | `7 * 13 * 19 = 91 * 19` |
| odd-block count `A - F` | 1638 | `2 * 3^2 * 7 * 13 = 91 * 18` |
| `P(2,6)`, `P(3,6)` (signed towers) | 59, -32 | |
| `F - odd = P(2,6) - P(3,6)` | 91 | `7 * 13` |

The formula `F(w,h) = [h^w - (h-1)^w - P(h-1,w) + P(h-2,w)] / 2` of [[castle-counting-formula](pages/castle-counting-formula.md)] gives `(3367 + 32 + 59)/2 = 1729` on the nose. Three cube facts sit in this one cell:

- **`A(6,4)` is a difference of cubes.** `4^6 = 16^3` and `3^6 = 9^3`, so `A(6,4) = 16^3 - 9^3 = (16 - 9)(16^2 + 16*9 + 9^2) = 7 * 481 = 3367`. The `9^3 = 729` here is the same `9^3` as in `9^3 + 10^3 = 1729`.
- **`F(6,4)` is a sum of cubes twice.** In tower language, `T(k, L) = (k+1)^L` counts towers of height at most `k` over a block of length `L` ([[tower-recursion-master-class](pages/tower-recursion-master-class.md)]), so `T(k, 3) = (k+1)^3` is always a cube and the taxicab identity reads `T(0,3) + T(11,3) = T(8,3) + T(9,3) = F(6,4)`. Four families of length-3 towers and one family of width-6 height-4 even castles, all of size 1729. Whether any of these equalities has a natural bijection is open (see the end of the page); `T(0,3) = 1` is the empty tower, so the left-hand side is "the towers of height at most 11 over three columns, plus one."
- **Everything is a multiple of `91 = 4^3 + 3^3`.** `A = 91 * 37`, `F = 91 * 19`, odd `= 91 * 18`, `F - odd = 91`. The first is structural (`4^6 - 3^6 = (4^3 - 3^3)(4^3 + 3^3) = 37 * 91`); the divisibility of `P(2,6) - P(3,6) = 91` by 91 is not, since the `F - odd` table `D(w, h) = 2F - A` is `1, 7, 25, 59, 97, 91, -71, -573, ...` along `h = 4` and equals `h^3 + (h-1)^3` at no other `(w, h)` with `h <= 6`, `w <= 10`. The coincidence is what makes `F(6,4) = 19 * 91 = 1729` land exactly.[^exec]

**Uniqueness.** A sweep of every `(w, h)` with `w, h <= 40` and `A(w,h) <= 10^9` finds 1729 exactly once across all three tables `A`, `F`, `A - F`: at `F(6,4)`.[^exec] (The width-2 cell `A(2, 865) = 2 * 865 - 1 = 1729` is the trivial exception outside the sweep; every width-2 castle of height `h` has exactly `h` blocks, so `F(2, 865) = 0`.)

**The other Carmichael numbers.** The same sweep, run for the first 33 Carmichael numbers, the first 15 taxicab numbers, and the first 6 Fermat near-misses, finds four hits, and they are the first four Carmichael numbers in order:[^exec]

| Carmichael number | castle count |
|---|---|
| 561 | odd-block castles at `(3, 34)` |
| 1105 | `A(4, 7) = 7^4 - 6^4` |
| **1729** | **`F(6, 4)`** |
| 2465 | `A(4, 9) = 9^4 - 8^4` |

No other taxicab number and no other near-miss is a castle count in range. The two `A(4, h)` hits are the difference-of-fourth-powers family `h^4 - (h-1)^4 = (2h - 1)(2h^2 - 2h + 1)`, the rhombic dodecahedral numbers A005917 `1, 15, 65, 175, 369, 671, 1105, 1695, 2465, ...`, which happens to produce Carmichael numbers at `h = 7` and `h = 9`.[^9]

**Rank 1729.** Under the rank/unrank bijection of [[song-as-castle](pages/song-as-castle.md)] (decompose by the first full-height column), castle number 1729 in the `(6, 4)` cell is `(3, 4, 4, 1, 1, 2)`, with 5 blocks - odd, so it is not itself counted by `F`. In the even-block codebook the 1729 even castles of `(6, 4)` run from `(4, 1, 1, 1, 1, 1)` to `(3, 3, 3, 3, 3, 4)` in rank order; the Hardy-Ramanujan number is the size of that codebook, `log_2 1729 = 10.756` bits.[^exec]

## The sum of three cubes

The phrase "sum of three cubes" fits 1729 once the cubes are allowed signs. Rearranging the taxicab identity:

```
9^3 + 10^3 + (-12)^3 = 1.
```

This is the entry `(9, 10, -12)` in the table of primitive solutions to `x^3 + y^3 + z^3 = 1` in the sum-of-three-cubes problem - the problem whose recent celebrities are `33` (Booker 2019) and `42` (Booker and Sutherland 2019, 1.3 million core-hours).[^7] Cubes are `0, +-1 (mod 9)`, so no integer `= 4, 5 (mod 9)` is a sum of three cubes; `1729 = 1 (mod 9)` and `1 = 1 (mod 9)` both pass. The representations of 1729 itself as a sum of three integer cubes with all `|x|, |y|, |z| <= 300` are just four: `(0, 1, 12)`, `(0, 9, 10)`, `(-7, -5, 13)`, `(-215, 98, 208)`; the two with a zero are the taxicab pair, and `13^3 - 7^3 - 5^3 = 2197 - 343 - 125 = 1729` is the one non-trivial small one.[^exec]

For `k = 1` there is a polynomial family, Mahler's `(9t^4)^3 + (3t - 9t^4)^3 + (1 - 9t^3)^3 = 1` (verified symbolically; `t = 1` gives `9^3 + (-6)^3 + (-8)^3 = 1`).[^7] Ramanujan's family for the same equation is of a completely different kind, and that is where the castle connection lives.

## Ramanujan's near-miss family is a linear recurrence

Ramanujan wrote down three rational generating functions:[^8]

```
sum a_n x^n = (1 + 53x +  9x^2) / (1 - 82x - 82x^2 + x^3)      A051028: 1, 135, 11161, 926271, ...
sum b_n x^n = (2 - 26x - 12x^2) / (1 - 82x - 82x^2 + x^3)      A051029: 2, 138, 11468, 951690, ...
sum c_n x^n = (2 +  8x - 10x^2) / (1 - 82x - 82x^2 + x^3)      A051030: 2, 172, 14258, 1183258, ...
```

with the identity `a_n^3 + b_n^3 = c_n^3 + (-1)^n` for every `n >= 0`: an infinite family of near-misses to Fermat's `x^3 + y^3 = z^3`, missing by exactly one, alternating in sign. The common denominator means all three sequences satisfy the order-3 recurrence `s_n = 82 s_{n-1} + 82 s_{n-2} - s_{n-3}` (OEIS signature `(82, 82, -1)`), and Hirschhorn proved the identity in 1995 and again in 1996 in Zeilberger style, observing that since both sides satisfy a recurrence of bounded order, checking `n = 0..6` suffices.[^8]

A linear recurrence runs backwards as well as forwards, and running it backwards is where 1729 appears. With `s_{n-3} = 82 s_{n-1} + 82 s_{n-2} - s_n`:[^exec]

| `n` | `a_n` | `b_n` | `c_n` | `a^3 + b^3 - c^3` |
|---|---|---|---|---|
| -4 | -5444135 | 6954572 | 5593538 | +1 |
| -3 | -65601 | 83802 | 67402 | -1 |
| -2 | -791 | 1010 | 812 | +1 |
| **-1** | **-9** | **12** | **10** | **-1** |
| 0 | 1 | 2 | 2 | +1 |
| 1 | 135 | 138 | 172 | -1 |
| 2 | 11161 | 11468 | 14258 | +1 |
| 3 | 926271 | 951690 | 1183258 | -1 |
| 4 | 76869289 | 78978818 | 98196140 | +1 |
| 5 | 6379224759 | 6554290188 | 8149096378 | -1 |

Row `n = -1` is `(-9)^3 + 12^3 = 10^3 - 1`, i.e. `9^3 + 10^3 = 12^3 + 1 = 1729`. Row `n = -2` is `791^3 + 812^3 = 1010^3 + 1`, and `n = 1` is `135^3 + 138^3 = 172^3 - 1`. The Hardy-Ramanujan number is the `n = -1` term of Ramanujan's own recurrence, one step behind the trivial `1^3 + 2^3 = 2^3 + 1`. Every row was checked exactly in integer arithmetic.

**Berlekamp-Massey recovers it.** Feeding the first twelve `c_n` to the wiki's [[berlekamp-massey](pages/berlekamp-massey.md)] over `Q` returns linear complexity 3 and connection polynomial `1 - 82x - 82x^2 + x^3`, the denominator exactly.[^exec] This is the same instrument [[recurrence-discovery](pages/recurrence-discovery.md)] points at the castle counts `P(k, L)`; here it rediscovers Ramanujan's denominator from ten numbers.

**The denominator factors, and the factors mean something.**

```
1 - 82x - 82x^2 + x^3  =  (1 + x)(1 - 83x + x^2)
x^3 - 82x^2 - 82x + 1  =  (x + 1)(x^2 - 83x + 1)          (characteristic polynomial)
```

The characteristic polynomial has coefficients `[1, -82, -82, 1]`: **palindromic**, in the sense of [[eigenvalue-continued-fractions](pages/eigenvalue-continued-fractions.md)] - its roots come in reciprocal pairs, plus the self-reciprocal root `-1`. The factor `(x + 1)` is the eigenvalue `-1`, and it is exactly the `(-1)^n` on the right-hand side of the identity: partial fractions give

```
a(x) =  8(16 + 101x) / (85 (1 - 83x + x^2))  -  43 / (85 (1 + x))
b(x) = 14(11 -  74x) / (85 (1 - 83x + x^2))  +  16 / (85 (1 + x))
c(x) =  6(31 - 139x) / (85 (1 - 83x + x^2))  -  16 / (85 (1 + x))
```

so `b_n + c_n` has no `(-1)^n` component at all and satisfies the order-2 recurrence alone: `4, 310, 25726, 2134948, ...` with `310 * 83 - 4 = 25726`. Hirschhorn's closed forms have the same shape, `a_n = [(64 + 8 sqrt 85) alpha^n + (64 - 8 sqrt 85) beta^n - 43 (-1)^n] / 85` with `alpha, beta = (83 +- 9 sqrt 85)/2`.[^8] The `85` in every denominator is the discriminant `83^2 - 4 = 6885 = 81 * 85`.

## The growth constant is the ninth metallic mean, squared

The dominant root of `x^2 - 83x + 1` is `alpha = (83 + 9 sqrt 85)/2 = 82.98795...`. Now `85 = 9^2 + 4`, which is the metallic discriminant `a^2 + 4` at `a = 9` ([[metallic-means](pages/metallic-means.md)]): the ninth metallic mean is `delta_9 = (9 + sqrt 85)/2 = 9.10977...`, the root of `x^2 - 9x - 1`, with purely periodic continued fraction `[9; 9, 9, 9, ...]`. And[^exec]

```
delta_9^2 = ((9 + sqrt 85)/2)^2 = (166 + 18 sqrt 85)/4 = (83 + 9 sqrt 85)/2 = alpha.
```

So **Ramanujan's near-miss triples grow, term to term, by exactly the square of the ninth metallic mean.** The roots of `x^2 - 9x - 1` are `delta_9` and `-1/delta_9` (norm `-1`, the anti-palindromic metallic template); their squares are `delta_9^2` and `1/delta_9^2`, the roots of `x^2 - 83x + 1` (norm `+1`, palindromic). Squaring a norm-`-1` unit gives a norm-`+1` unit, and the continued fraction changes character accordingly: `delta_9^2 = [82; 1, 81, 1, 81, ...]`, no longer purely periodic of period one, with a head of `82` (the trace 83 minus one), exactly the "`c = +1` roots `r, 1/r` have a head" case of [[eigenvalue-continued-fractions](pages/eigenvalue-continued-fractions.md)]. The Lucas sequences of `x^2 - 9x - 1` show the same numbers: `U = 0, 1, 9, 82, 747, ...` and `V = 2, 9, 83, 756, ...`, so `82 = U_3` and `83 = V_2 = delta_9^2 + delta_9^{-2}` are the two coefficients of Ramanujan's recurrence read off the ninth rung of the ladder.

**Where `delta_9` lives on the castle side.** [[metallic-strip-realizability](pages/metallic-strip-realizability.md)] realizes every rung of the metallic ladder by one rule, the plateau-free-except-ceiling strip (adjacent columns must differ in height unless both are at the ceiling `h`), whose transfer matrix `M_h = J - D` has characteristic polynomial `(x + 1)^{h-2} (x^2 - (h-1)x - 1)`, Perron root `delta_{h-1}`. Metal 9 is at height 10. Verified here:[^exec]

```
charpoly(M_10)    = (x + 1)^8 (x^2 - 9x - 1)          Perron root delta_9  = 9.10977...
charpoly(M_10^2)  = (x - 1)^8 (x^2 - 83x + 1)         Perron root delta_9^2 = 82.98795...

free strip counts 1^T M_10^{n-1} 1, n = 1..8:   10, 91, 829, 7552, 68797, 626725, 5709322, 52010623
ratio of consecutive terms -> 9.1098;  ratio at width step 2 -> 82.9880
```

So the width-`2n` counts of the height-10 ceiling-exception castle strip and Ramanujan's `a_n, b_n, c_n` share the characteristic factor `x^2 - 83x + 1` and the growth constant `delta_9^2`. The parallel goes one step further: both denominators carry a `(x + 1)` factor next to the metallic quadratic. In the castle strip the `(x + 1)^{h-2}` block is the "spurious" part of the spectrum that the count sequence barely sees; in Ramanujan's identity the single `(x + 1)` is load-bearing, it is the `(-1)^n` that makes the miss alternate between `+1` and `-1`. This is the [[castle-eigenvalue-oeis-crosswalk](pages/castle-eigenvalue-oeis-crosswalk.md)] reading of a Diophantine identity: the sequence of near-miss triples is a C-finite object with algebraic-unit eigenvalues, exactly the class every castle count lives in, and it sits on the ladder at rung 9 squared, one decimation (width step 2) above the strip. Copper's `F_{3n+5}` trisection on the realizability page is the same phenomenon at rung 1.

Two coincidences worth naming as coincidences, so nobody builds on them: the taxicab cubes are `9^3 + 10^3` and the rung is metal 9 at height 10; and the width-2 count of the height-10 strip is `10^2 - 9 = 91 = 7 * 13 = 1729/19`, the same 91 that divides everything in the `(6, 4)` cell. Neither has a mechanism behind it that this page can see.

## 1729 as a castle

A castle is a column-height vector with every height at least 1 and some height equal to `h` ([[castle-representations](pages/castle-representations.md)]). Reading the digits of 1729 in base `b` as column heights gives a candidate castle for each base; a zero digit disqualifies it (no empty column). Across bases 2 to 20, only bases 9, 10, 11, 14, 15, 16, 17, 18, and 20 give valid castles - the famous base-12 palindrome `1001` fails on its zeros.[^exec]

| base | digit castle | `h` | blocks | area | even-block (PE 502) castle? |
|---|---|---|---|---|---|
| 9 | `(2, 3, 3, 1)` | 3 | 3 | 9 | no |
| **10** | **`(1, 7, 2, 9)`** | **9** | **14** | **19** | **yes** |
| 11 | `(1, 3, 3, 2)` | 3 | 3 | 9 | no |
| 14 | `(8, 11, 7)` | 11 | 11 | 26 | no |
| 15 | `(7, 10, 4)` | 10 | 10 | 21 | yes |
| 16 | `(6, 12, 1)` | 12 | 12 | 19 | yes |
| 17 | `(5, 16, 12)` | 16 | 16 | 33 | yes |
| 18 | `(5, 6, 1)` | 6 | 6 | 12 | yes |
| 20 | `(4, 6, 9)` | 9 | 9 | 19 | no |

The base-10 castle `(1, 7, 2, 9)` is the Hardy-Ramanujan castle proper: width 4, height 9, 14 blocks (even, so PE 502 counts it), and area `19`, the digit sum, so the area divides 1729 because 1729 is Harshad.

```
   #        row 9
   #        row 8
 # #        row 7
 # #        row 6
 # #        row 5
 # #        row 4
 # #        row 3
 ###        row 2
####        row 1      column heights (1, 7, 2, 9): 14 blocks, area 19
```

Its castle graph ([[castle-graph](pages/castle-graph.md)]) has 19 cells and 20 edges, cycle rank 2 (two filled `2 x 2` squares, at rows 1-2 across columns 2-3 and 3-4). Adjacency spectrum: `lam_1 = 2.5982`, `lam_2 = 1.8981`; the universal-cover spectral radius by the edge-cavity method of [[ramanujan-castles](pages/ramanujan-castles.md)] is `rho(T) = 2.5756`, so `lam_2 <= rho(T)` and the digit castle is **Ramanujan** in the spectral sense as well.[^exec] (Every castle with at most 22 cells is, per that page's census, so this was never in doubt; the number is recorded for the record.) Its characteristic polynomial is `x (x^18 - 20x^16 + 160x^14 - 670x^12 + 1600x^10 - 2215x^8 + 1723x^6 - 691x^4 + 119x^2 - 5)`, irreducible over `Q` apart from the factor `x`.

Two more readings of 1729 as a single castle:

- **Binary.** `1729 = 11011000001_2`. Under the [[binary-string-bijection](pages/binary-string-bijection.md)] convention `1 -> height 2, 0 -> height 1`, this is the height-2 castle `(2, 2, 1, 2, 2, 1, 1, 1, 1, 1, 2)` of width 11 with 4 blocks (the bottom row plus three runs of 1s): even, valid. Alternatively, `unrank(1729, 11, 2) = (1, 1, 2, 2, 2, 1, 1, 1, 1, 1, 2)` with 3 blocks.
- **Rank.** `unrank(1729, 6, 4) = (3, 4, 4, 1, 1, 2)` in its own cell, `unrank(1729, 4, 9) = (5, 8, 9, 2)`, `unrank(1729, 4, 10) = (8, 10, 3, 10)`.

## 1729 as a modulus

1729 is Carmichael, so `a^1728 = 1 (mod 1729)` for every `a` coprime to it - a composite that passes every Fermat test. Reducing the castle counts modulo 1729 is a CRT exercise over `7, 13, 19`, and [[mod-p-observatory](pages/mod-p-observatory.md)] predicts the answer: `F(., h) mod p` is eventually periodic with period the lcm of the eigenvalue orders, and the period mod 1729 is the lcm of the three prime periods. Computed by running the parity transfer DP modulo each modulus and detecting the first repeated DP state:[^exec]

| `h` | period mod 7 | mod 13 | mod 19 | lcm | period mod 1729 (direct) | DP transient |
|---|---|---|---|---|---|---|
| 2 | 24 | 12 | 72 | 72 | 72 | 3 |
| 3 | 168 | 168 | 360 | 2520 | 2520 | 3 |
| 4 | 8400 | 168 | 360 | 25200 | 25200 | 3 |

The `8400` at `(h, p) = (4, 7)` is the observatory's `1200 x 7` from the double root of `char_2` mod 7, so `F(w, 4) mod 1729` inherits it: period `25200 = 8400 * 3`. The transient of 3 is measured on the full DP state vector, which carries the "has some column reached `h` yet" flag; the count sequence itself may settle sooner.

The factorization `1729 = 12^3 + 1 = Phi_2(12) Phi_6(12) = 13 * 133`, with `133 = 7 * 19`, is `x^3 + 1 = (x + 1)(x^2 - x + 1)` at `x = 12`. The polynomial `Phi_6(p) = p^2 - p + 1` is the order of the cyclotomic subgroup the round-three castle torus item on [[castle-cryptography-round-two](pages/castle-cryptography-round-two.md)] wants to be prime-heavy; at `p = 12` it is `7 * 19`.

## What this page settles and what it opens

Settled:

- `F(6,4) = 1729`, unique in `w, h <= 40`; `A(6,4) = 16^3 - 9^3`; the `(6,4)` cell is `91 * (37, 19, 18, 1)`.
- The first four Carmichael numbers are castle counts: `odd(3,34), A(4,7), F(6,4), A(4,9)`.
- Ramanujan's near-miss family is C-finite of order 3, Berlekamp-Massey recovers it, and its growth constant is `delta_9^2`, the square of the ninth metallic mean, realized on the castle side by the height-10 ceiling-exception strip at width step 2.
- The base-10 digit castle `(1, 7, 2, 9)` is a valid even-block castle of area 19 and is spectrally Ramanujan.
- `F(., h) mod 1729` has periods `72, 2520, 25200` for `h = 2, 3, 4`.

Open:

- **A bijection behind `F(6,4) = 12^3 + 1 = 9^3 + 10^3`.** The natural candidate sets are the length-3 towers `T(k, 3) = (k+1)^3`. Is there an explicit map from the 1729 even castles of `(6, 4)` onto `T(11, 3)` plus a point, or onto `T(8, 3) + T(9, 3)`? The `91`-divisibility suggests looking for a 91-to-1 structure first.
- **Which castle counts are sums of three cubes?** Taken up on [[sum-of-three-cubes-castles](pages/sum-of-three-cubes-castles.md)]: under Heath-Brown the answer is the residue `F(w,h) mod 9`, periodic in both directions; `F(5,5) = 906` is a Booker-Sutherland 2019 number, and `F(13,2) = 16^3` is a cleaner instance of the bijection question above.
- **Which rungs do the other Ramanujan-type identities sit on?** Chen (2012), Han and Hirschhorn (2006), and McLaughlin (2010) give further C-finite Diophantine families; each has a palindromic denominator and a growth constant. Are they metallic (a `(a^2 + 4)` discriminant, hence a ceiling-exception castle strip) or do they land in other reachable fields of the [[reachable-field-census](pages/reachable-field-census.md)]?

## Appearances in Sources

- [[oeis-mining-pe502](pages/oeis-mining-pe502.md)] - the `F(w, 4)` row `1, 7, 31, 117, 439, 1729, ...` in the brute-force tabulation, where 1729 was first noticed as a castle count.
- [[project-euler-502-solution](pages/project-euler-502-solution.md)] - `T(k, L) = (k+1)^L`, the tower count that makes `T(k, 3)` a cube.

## Related Concepts

- [[sum-of-three-cubes-castles](pages/sum-of-three-cubes-castles.md)] - the general question this page opened: which castle counts are sums of three cubes, signed and positive; [[sums-of-three-cubes](pages/sums-of-three-cubes.md)] is the number-theory background.
- [[ramanujan-castles](pages/ramanujan-castles.md)] - the other Ramanujan on this wiki: the spectral expander condition on castle graphs; the digit castle `(1, 7, 2, 9)` satisfies it.
- [[metallic-means](pages/metallic-means.md)] - the ladder `delta_a = (a + sqrt(a^2 + 4))/2`; Ramanujan's near-miss growth constant is `delta_9^2`.
- [[metallic-strip-realizability](pages/metallic-strip-realizability.md)] - the ceiling-exception strip `M_h = J - D` that realizes `delta_9` at height 10.
- [[eigenvalue-continued-fractions](pages/eigenvalue-continued-fractions.md)] - palindromic characteristic polynomials and the norm `+1` versus norm `-1` continued-fraction dichotomy that `delta_9` versus `delta_9^2` illustrates.
- [[castle-eigenvalue-oeis-crosswalk](pages/castle-eigenvalue-oeis-crosswalk.md)] - the same method (convergents, Lucas sequences, OEIS) applied to castle eigenvalues; A051028-A051030 are the Diophantine cousins.
- [[berlekamp-massey](pages/berlekamp-massey.md)] and [[recurrence-discovery](pages/recurrence-discovery.md)] - the instrument that recovers `1 - 82x - 82x^2 + x^3` from the terms.
- [[castle-counting-formula](pages/castle-counting-formula.md)] and [[castle-counting-function](pages/castle-counting-function.md)] - `F(6,4) = (A - P(3,6) + P(2,6))/2 = 1729`.
- [[tower-recursion-master-class](pages/tower-recursion-master-class.md)] - `T(k, 3) = (k+1)^3`, the cube reading of the taxicab identity.
- [[song-as-castle](pages/song-as-castle.md)] - the rank/unrank bijection used for "castle number 1729".
- [[mod-p-observatory](pages/mod-p-observatory.md)] - the period-is-lcm-of-orders mechanism behind the mod-1729 table.
- [[castle-graph](pages/castle-graph.md)] - the polyomino graph of the digit castle.
- [[castle-snippets](pages/castle-snippets.md)] - `all_castles`, `blocks`, `castle_graph`.
- [[castle-cryptography-round-two](pages/castle-cryptography-round-two.md)] - `Phi_6(p)` and the round-three torus, at `p = 12`.

## Footnotes

[^1]: https://en.wikipedia.org/wiki/1729_(number) (2026-09-19) - "It is the first nontrivial taxicab number, expressed as the sum of two cubic positive integers in two different ways"; Hardy's account: "the number seemed to me rather a dull one, and that I hoped it was not an unfavourable omen", Ramanujan: "it is a very interesting number; it is the smallest number expressible as the sum of two cubes in two different ways"; "1729 is a composite number, the first nontrivial taxicab number, a Carmichael number, and a centered cube number"; "It is also the smallest absolute Euler pseudoprime. It is palindromic in bases 12, 32, and 36"; "1729 was later found in one of Ramanujan's notebooks dated years before the incident", "noted by French mathematician Frenicle de Bessy in 1657".
[^2]: https://oeis.org/A001235 (2026-09-19) - "Taxi-cab numbers: sums of 2 cubes in more than 1 way", data `1729, 4104, 13832, 20683, 32832, 39312, 40033, 46683, 64232, 65728, 110656, 110808, 134379, 149389, 165464`; https://en.wikipedia.org/wiki/Taxicab_number (2026-09-19) - "1729 = Ta(2) = 1^3 + 12^3 = 9^3 + 10^3, also known as the Hardy-Ramanujan number"; the two pairs "were first mentioned by Bernard Frenicle de Bessy, who published his observation in 1657"; `Ta(3) = 87539319 = 167^3 + 436^3 = 228^3 + 423^3 = 255^3 + 414^3` (Leech 1957).
[^3]: https://oeis.org/A050794 (2026-09-19) - Diophantine equation `x^3 + y^3 = z^3 + 1` with `1 < x < y < z`, "Fermat near misses", data `1729, 1092728, 3375001, 15438250, 121287376, 401947273, ...`; comment (Omar E. Pol, 2009) "a(1)=1729 is the Hardy-Ramanujan number"; example "577^3 + 2304^3 = 2316^3 + 1 = 12422690497".
[^4]: https://oeis.org/A002997 (2026-09-19) - "Carmichael numbers", data `561, 1105, 1729, 2465, 2821, 6601, 8911, 10585, 15841, 29341, ...`; definition "composite numbers k such that a^(k-1) == 1 (mod k) for every a coprime to k"; Korselt (1899): an odd composite `k` is Carmichael iff squarefree and `p - 1 | k - 1` for every prime `p | k`.
[^5]: https://arxiv.org/abs/1510.00735 (2026-09-19) - Ken Ono and Sarah Trebat-Leder, "The 1729 K3 Surface", Research in Number Theory (2016), abstract [synthesis]: revisiting Ramanujan's writings around 1729 and Euler's `a^3 + b^3 = c^3 + d^3`, they find he "discovered a K3 surface with Picard number 18" yielding "infinitely many cubic twists over Q with rank >= 2".
[^6]: raw/oeis-pe502/terms_50.txt §"F(w,4)" L10-12 - "## F(w,4)  [even blocks, height 4, w=1..50]" followed by the data line beginning "1 7 31 117 439 1729 7063 29201 120471 493617".
[^7]: https://en.wikipedia.org/wiki/Sums_of_three_cubes (2026-09-19) - "cannot equal 4 or 5 modulo 9, because the cubes modulo 9 are 0, 1, and -1"; Mahler 1936: "(9b^4)^3 + (3b - 9b^4)^3 + (1 - 9b^3)^3 = 1"; the primitive-solution table lists `(9, 10, -12)` for `n = 1`; "in 2019, Andrew Booker settled the case n = 33"; "in September 2019, Booker and Andrew Sutherland finally settled the n = 42 case", "using 1.3 million hours of computing on the Charity Engine global grid".
[^8]: https://mathworld.wolfram.com/RamanujansSumIdentity.html (2026-09-19) - the three generating functions with denominator `1 - 82x - 82x^2 + x^3`, the identity `a_n^3 + b_n^3 = c_n^3 + (-1)^n`, Hirschhorn's closed forms with `alpha, beta = (83 +- 9 sqrt 85)/2` and denominators 85, and "the first seven cases n=0 to 6 is sufficient to prove the result" (Hirschhorn 1996); references M. D. Hirschhorn, "An Amazing Identity of Ramanujan", Math. Mag. 68 (1995) 199-201, and "A Proof in the Spirit of Zeilberger of an Amazing Identity of Ramanujan", Math. Mag. 69 (1996) 267-269. https://oeis.org/A051028 (2026-09-19) - "Ramanujan's a-series: expansion of (1+53x+9x^2)/(1-82x-82x^2+x^3)", g.f. "(1+53*x+9*x^2)/((1+x)*(1-83*x+x^2))", recurrence signature `(82, 82, -1)`, comment (Emeric Deutsch, 2006) "The 'amazing' identity of Ramanujan is a(n)^3 + b(n)^3 = c(n)^3 + (-1)^n" with `b, c` = A051029, A051030; further references K.-W. Chen, Fib. Q. 50 (2012) 227-230; J. H. Han and M. D. Hirschhorn, Math. Mag. 79 (2006) 302-304; J. Mc Laughlin, Fib. Q. 48 (2010) 34-38.
[^9]: https://oeis.org/A005917 (2026-09-19) - "Rhombic dodecahedral numbers: a(n) = n^4 - (n - 1)^4", data `1, 15, 65, 175, 369, 671, 1105, 1695, 2465, 3439, 4641, 6095`; formula "a(n) = (2*n - 1)*(2*n^2 - 2*n + 1)".
[^exec]: Verified by execution (2026-09-19): two Python 3 scripts (SymPy 1.14, NumPy 1.26, NetworkX 3.4). Script 1: factorization, Carmichael check over all `a` coprime to 1729, Korselt, base expansions, sums of three cubes for 1729 (`|x|,|y|,|z| <= 300`) and for 1 (`<= 100`), Mahler's identity by symbolic expansion, the three Ramanujan series from their generating functions with the identity checked for `n = 0..5` and the recurrence run backwards to `n = -4`, denominator factorization and partial fractions, Berlekamp-Massey over `Q` on `c_0..c_11`, Lucas sequences and continued fractions of `delta_9`, `delta_9^2`, `1729^(1/3)`, and the height-10 matrix `M_10 = J - D` with `charpoly(M_10)`, `charpoly(M_10^2)`, and free strip counts. Script 2: the parity transfer DP for `F(w, h)` (checked against `F(4,2) = 10` and brute force at `(6,4)`), the `w, h <= 40` sweep for 1729 and for the taxicab / near-miss / Carmichael lists, `P(2,6)` and `P(3,6)` as signed sums over `{0..k}^6`, the `D(w,h) = 2F - A` table, digit castles in bases 2-20, `unrank` from song-as-castle, the even-block codebook endpoints at `(6,4)`, the castle graph of `(1,7,2,9)` with adjacency spectrum, characteristic polynomial, and `rho_cover` from ramanujan-castles, and the mod `7, 13, 19, 1729` periods by first repeated DP state. All quoted numbers are the scripts' printed output.
