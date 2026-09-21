---
title: Sum of three cubes castles
category: Analyses
summary: Which castle counts are sums of three cubes. Signed cubes - under Heath-Brown the answer is the residue test F(w,h) mod 9 not in {4,5}, and F mod 9 is periodic in both directions (periods 24, 24, 240, 3120, 2184, 2184, 2184, 10920, 21840, 21840, 11514360 in w for h = 2..12; 2*3^(1+ceil(log_3 w)) in h), so the question is decided cell by cell - about 22% of F(w,h) with w >= 4 are provably not sums of three cubes, and the three PE 502 targets F(10^12,100), F(10000,10000), F(100,10^12) are 6, 7, 6 mod 9, all admissible. Three cells close in closed form - the height-2 row F(w,2) = 2^(w-1) + eps 2^floor((w-1)/2) is a cube at w = 1 (mod 12), twice a cube at w = 5, four times a cube (hence excluded) at w = 9; the width-3 column is triangular numbers (never excluded) interleaved with 5*C(h,2)+1 (excluded iff h = 4, 6 mod 18); A(3m,h) = (h^m)^3 - ((h-1)^m)^3 always. F(5,5) = 906 is a Booker-Sutherland 2019 number. Positive cubes - 56 of the 552 even counts with w >= 4 below 10^8 are sums of three positive cubes against 55.7 expected at the measured density 0.101, so castle counts are random integers in this respect; the tower reading is F(w,h) = T(a,3) + T(b,3) + T(c,3). Even perfect numbers ride along - 2^(p-1)(2^p - 1) = F(2p, 2) for p = 3 (mod 4) and = odd(3, 2^p) always.
tags: [analysis, castle, sum-of-cubes, mod-9, periodicity, kitamasa, closed-form, height-2, perfect-numbers, taxicab, booker-sutherland, worked-example, computation]
sources: [oeis-mining-pe502, project-euler-502-solution, project-euler-502]
created: 2026-09-20
updated: 2026-09-20
---

# Sum of three cubes castles

[[hardy-ramanujan-castle](pages/hardy-ramanujan-castle.md)] found that `F(6,4) = 1729 = 1^3 + 12^3 = 9^3 + 10^3`: the even-block castle count of the `(6,4)` cell is the taxicab number, a sum of two cubes twice over, hence a sum of three cubes with a zero, and `9^3 + 10^3 + (-12)^3 = 1` besides. This page asks the general question: **which castle counts are sums of three cubes?** The wiki has a closed form for every count ([[castle-counting-formula](pages/castle-counting-formula.md)]), and the [[sums-of-three-cubes](pages/sums-of-three-cubes.md)] problem has exactly one known obstruction, `n = 4, 5 (mod 9)`, conjecturally the only one (Heath-Brown). So the question splits cleanly into an unconditional half (which castle counts are *provably not* sums of three cubes, a residue computation) and a conditional half (everything else, conjecturally *is*, and for small counts the explicit representation can be exhibited). A third, finite question rides alongside: which castle counts are sums of three *positive* cubes, where the tower count `T(k,3) = (k+1)^3` gives every such identity a castle-side reading.

Notation follows [[castle-counting-function](pages/castle-counting-function.md)]: `A(w,h) = h^w - (h-1)^w` counts all castles of width `w` and height exactly `h`, `F(w,h)` the even-block ones, `odd = A - F`. The degenerate cells `w <= 2` are excluded from every census below unless named, because every width-2 castle of height `h` has exactly `h` blocks, so `F(2,h) = 2h - 1` for even `h` and `0` for odd `h` hits every `n = 3 (mod 4)` trivially. Every number on the page was computed while writing; the scripts are described in the execution footnote.[^exec]

## The residue test, and why it decides everything

Under Heath-Brown's conjecture, `F(w,h)` is a sum of three cubes iff `F(w,h) mod 9` is not `4` or `5`.[^1] Two structural facts make this a finite computation for every row and every column:

- **Width direction.** For fixed `h`, `F(., h)` is the sum of `h^w`, `(h-1)^w`, and two C-finite sequences `P(h-1, w)`, `P(h-2, w)`, so `F(., h) mod 9` is eventually periodic ([[mod-p-observatory](pages/mod-p-observatory.md)], whose mechanism is stated for primes and holds verbatim for `9`).
- **Height direction.** For fixed `w`, `P(k, w)` is a quasi-polynomial in `k` with characteristic polynomial `(x+1)^w (x-1)^{w-2}` ([[signed-tower-k-direction](pages/signed-tower-k-direction.md)]), so `F(w, .) mod 9` is periodic in `h` as well.

Computed by running the parity-refined transfer DP modulo 9 and detecting the first repeated state vector (width direction), and by running the `k`-direction recurrence modulo 9 (height direction):[^exec]

| `h` | period of `F(., h) mod 9` in `w` | residues `4, 5` per period | excluded fraction | first excluded `w` |
|---|---|---|---|---|
| 2 | 24 | 2 | 0.083 | 9, 21 |
| 3 | 24 | 3 | 0.125 | 7, 21, 24 |
| 4 | 240 | 54 | 0.225 | 3, 8, 13, 18 |
| 5 | 3120 | 692 | 0.222 | 4, 14, 22, 24 |
| 6 | 2184 | 496 | 0.227 | 3, 10, 11, 14 |
| 7 | 2184 | 439 | 0.201 | 9, 13, 14, 18 |
| 8 | 2184 | 478 | 0.219 | 6, 9, 10, 15 |
| 9 | 10920 | 2422 | 0.222 | 5, 6, 15, 17 |
| 10 | 21840 | 4859 | 0.222 | 9, 20, 36, 39 |
| 11 | 21840 | 4748 | 0.217 | 10, 11, 15, 18 |
| 12 | 11514360 | 2557075 | 0.222 | 2, 12, 27, 34 |

The transient is at most 2 in every row (the "has some column reached `h`" flag settles by `w = 3`). Against the mod-3 periods `8, 8, 80, 3120` of the observatory at `h = 2..5`, the mod-9 periods are three times as long at `h = 2, 3, 4` and identical at `h = 5`. The excluded fraction converges to `2/9 = 0.222`, the equidistribution value, with `h = 2` and `h = 3` the visible exceptions (they are explained in closed form below) and `h = 7` a mild deficit at `0.201` that the period of 2184 makes exact, not statistical.

| `w` | period of `F(w, .) mod 9` in `h` | excluded fraction |
|---|---|---|
| 1 | 2 | 0 |
| 2 | 18 | `2/18` |
| 3 | 18 | `2/18` |
| 4 | 54 | `12/54` |
| 5 | 54 | `8/54` |
| 6 | 54 | `12/54` |
| 7 | 54 | `10/54` |
| 8 | 54 | `6/54` |
| 9 | 54 | `15/54` |
| 10 | 162 | `36/162` |

The height-direction period obeys the law `2 * 3^{1 + ceil(log_3 w)}` for `w >= 2`: `18` for `w = 2, 3`, `54` for `w = 4..9`, `162` for `w = 10..27`, and `1458` at `w = 100`. This is the observatory's `2 p^{ceil(log_p L)}` law for `P(k, L) mod p` with one extra factor of 3 for the second power of the prime; `P(k, w) mod 9` itself was checked to have exactly these periods in `k` for `w <= 10` and `w = 100`.[^exec]

**Over all cells with `A(w,h) <= 10^9`** (19,132 cells, `3 <= w <= 30`): the `F` table has 18,256 entries at `w = 3` of which 2,029 (11.1%) are excluded, and 876 entries at `w >= 4` of which 179 (20.4%) are excluded; the `A` table is *never* excluded at `w = 3` (a theorem, next section) and excluded 225 of 876 times (25.7%) at `w >= 4`; the odd table runs 11.1% and 21.0%. Across all three tables there are 57,349 distinct castle counts below `10^9`, of which 4,643 (8.1%) are provably not sums of three cubes and the remaining 52,706 conjecturally are, out of 777,777,777 admissible integers in range: castle counts are a sparse set (about `sqrt N` of them below `N`, dominated by the width-3 quadratics), and "which sums of three cubes are castle counts" is the same finite list read from the other side.[^exec]

## Three cells that close in closed form

**The `A` table at widths divisible by 3.** `A(3m, h) = h^{3m} - (h-1)^{3m} = (h^m)^3 - ((h-1)^m)^3` is a difference of two cubes for every `h`, hence a sum of three cubes with `z = 0`, unconditionally. `A(6,4) = 16^3 - 9^3` on the Hardy-Ramanujan page is the `m = 2` instance. Modulo 9 this says `A(3m, h)` is a difference of two elements of `{0, +-1}`, never `+-4`, which is why the `A` column at `w = 3` has zero exclusions in the census. Nothing similar holds for `F` or odd, whose `(6,4)` entries are `(16^3 - 9^3 -+ (4^3 + 3^3)) / 2`, a signed sum of four cubes halved.

**The height-2 row.** `F(w,2)` is the hyperbolic sequence A038505 ([[oeis-height2-hyperbolic-castles](pages/oeis-height2-hyperbolic-castles.md)]) with the cosine closed form of [[fractional-width-and-height](pages/fractional-width-and-height.md)]; reading the cosine off `w mod 8` gives an integer form, verified for `w <= 48`:[^exec]

```
F(w,2) = 2^{w-1} + eps_w * 2^{floor((w-1)/2)},      eps_w = 0   for w = 1 (mod 4)
                                                     eps_w = +1  for w = 2, 3, 4 (mod 8)
                                                     eps_w = -1  for w = 6, 7, 0 (mod 8)
```

So for `w = 1 (mod 4)` the even-block count is exactly the power of two `2^{w-1}`, and a power of two is a cube, twice a cube, or four times a cube according to its exponent mod 3:

| `w mod 12` | `F(w,2)` | cube reading | mod 9 | sum of three cubes? |
|---|---|---|---|---|
| 1 | `2^{w-1} = (16^{(w-1)/12})^3` | **a cube**: `F(13,2) = 16^3`, `F(25,2) = 256^3`, `F(37,2) = 4096^3` | 1 | yes, `c^3 + 0 + 0` |
| 5 | `2^{w-1} = 2 (2^{(w-2)/3})^3` | **twice a cube**: `F(5,2) = 2 * 2^3`, `F(17,2) = 2 * 32^3`, `F(29,2) = 2 * 512^3` | 7 | yes, `c^3 + c^3 + 0` |
| 9 | `2^{w-1} = 4 (2^{(w-3)/3})^3` | **four times a cube**: `F(9,2) = 4 * 4^3`, `F(21,2) = 4 * 64^3`, `F(33,2) = 4 * 1024^3` | 4 | **no** |

Four times a cube not divisible by 3 is `+-4 (mod 9)`, so the `w = 9 (mod 12)` entries are the *only* excluded ones in the whole height-2 row: the period-24 census above (excluded at `w = 9, 21`) is this table. The row's `1/12` exclusion rate, half the equidistribution value, is now a theorem rather than a measurement. Two more residues carry a two-cube reading: at `w = 19 (mod 24)`, `F(w,2) = 2^{w-1} + 2^{(w-1)/2} = (2^{(w-1)/3})^3 + (2^{(w-1)/6})^3` (`F(19,2) = 262656 = 64^3 + 8^3`, `F(43,2) = 16384^3 + 128^3`), and at `w = 7 (mod 24)` the same with a minus (`F(7,2) = 56 = 4^3 - 2^3`, `F(31,2) = 1024^3 - 32^3`). The cube case is the cleanest instance of the bijection question the Hardy-Ramanujan page left open: `F(13,2) = 4096 = T(15, 3)`, the 4096 even castles of width 13 and height 2 against the 4096 length-3 towers of height at most 15, and both sides are already `2^{12}` binary objects ([[binary-string-bijection](pages/binary-string-bijection.md)]).

*Aside: perfect numbers.* Put `w = 2p` with `p = 3 (mod 4)`, so `w = 6 (mod 8)` and `F(2p, 2) = 2^{2p-1} - 2^{p-1} = 2^{p-1}(2^p - 1)`. When `2^p - 1` is a Mersenne prime this is an even perfect number: `28 = F(6,2)`, `8128 = F(14,2)`, `137438691328 = F(38,2)`, `2^{126}(2^{127} - 1) = F(254, 2)`; verified exactly for `p = 3, 7, 11, 19, 23, 31` (the formula needs `p = 3 (mod 4)`, not primality). For `p = 1 (mod 4)` the sign flips and `F(2p, 2) = 2^{p-1}(2^p + 1)`: `F(10,2) = 528`, not `496`. Independently, every even perfect number is triangular, `2^{p-1}(2^p - 1) = C(2^p, 2)`, and the width-3 column below shows `odd(3, h) = C(h, 2)` for even `h`, so `6 = odd(3,4)`, `28 = odd(3,8)`, `496 = odd(3,32)`, `8128 = odd(3,128)`: every even perfect number is the odd-block count of the `(3, 2^p)` cell, and those with `p = 3 (mod 4)` are an even-block count as well. `8128 = 4^3 + 4^3 + 20^3` is also a sum of three positive cubes.[^exec]

**The width-3 column.** Interpolating the exact values gives a quasi-polynomial in `h` of period 2, verified for `h <= 30`:[^exec]

```
F(3,h)   = C(h,2)          (h odd)        5 C(h,2) + 1     (h even)
odd(3,h) = 5 C(h,2) + 1    (h odd)        C(h,2)           (h even)
A(3,h)   = 6 C(h,2) + 1 = 3h^2 - 3h + 1 = h^3 - (h-1)^3
```

So the width-3 even counts at odd height are the **triangular numbers** `1, 3, 10, 21, 36, 55, ...` (A000217), and at even height `6, 31, 76, 141, 226, 331, ...`, which is `F(3, 2m) = 10m^2 - 5m + 1 = 5 Hex(m) + 1` with `Hex(m) = m(2m-1)` the hexagonal numbers. The odd column's other half, `odd(3, 2n+1) = 10n^2 + 5n + 1 = 1, 16, 51, 106, 181, 276, ...`, is OEIS A080860 exactly; `F(3, 2m)` is the same quadratic at negative index, `A080860(-m)`, and is not in OEIS as a sequence (searched 2026-09-20 by terms and by formula), so it goes to the [[castle-sequence-catalogue](pages/castle-sequence-catalogue.md)] as a novel candidate.[^3] Triangular numbers are `0, 1, 3, 6 (mod 9)` and never `4, 5`, so every triangular castle count passes the residue test; `5 C(h,2) + 1` is `4 (mod 9)` iff `C(h,2) = 6 (mod 9)` iff `h = 4, 6 (mod 9)`, and is never `5`. Therefore

- `F(3,h)` is excluded iff `h = 4, 6 (mod 18)` (`F(3,4) = 31`, `F(3,6) = 76`, `F(3,22) = 1156`, `F(3,24) = 1381`, ...),
- `odd(3,h)` is excluded iff `h = 13, 15 (mod 18)`,
- `A(3,h)` is never excluded,

exactly `1/9` of each of the `F` and odd columns, the `2/18` in the height-direction table. The width-2 row is the same kind of statement one level down: `F(2,h) = 2h - 1` (even `h`) is excluded iff `h = 12, 16 (mod 18)`.

## The three Project Euler 502 targets

PE 502 asks for `F(10^12, 100) + F(10000, 10000) + F(100, 10^12)` modulo `10^9 + 7` ([[project-euler-502](pages/project-euler-502.md)]). Modulo 9 the three are within reach of the same machinery the solution uses, run over `Z/9` instead of `F_p`:[^exec]

| target | `mod 9` | method | independent check |
|---|---|---|---|
| `F(10^12, 100)` | **6** | [[kitamasa](pages/kitamasa.md)] on `x^w mod char_99` over `Z/9` (degree 100) | 400-state parity transfer matrix raised to `10^12 - 1` over `Z/9`: 6 |
| `F(10000, 10000)` | **7** | Kitamasa on `char_9999` over `Z/9` (degree 10000, 12 s) | method reproduces `F(4,2), F(13,10), F(10,13), F(100,100) mod 9 = 1, 3, 7, 8` against exact values |
| `F(100, 10^12)` | **6** | `k`-direction recurrence for `P(k, 100)`, order 198, Kitamasa to `k = 10^12 - 1, 10^12 - 2` | `P(k,100) mod 9` has period 1458 in `k`; reducing `10^12` mod 1458 gives the same residues |

None of the three is `4` or `5`, so all three targets pass the residue test and are, under Heath-Brown, sums of three cubes; so is `F(100,100) = 8 (mod 9)`. The sum of the three residues is `1 (mod 9)`, a fact about the PE 502 answer that the problem's modulus `10^9 + 7` does not reveal. The `Z/9` Kitamasa is the [[castle-cryptography-ring](pages/castle-cryptography-ring.md)] computation with a composite modulus; nothing in the reduction needs a field, only that `char_k` is monic, which its reversed denominator `den_k` (constant term 1) guarantees.

## Every even-block count below 1000

The `F` table has 50 entries below 1000 with `w >= 3`, `h >= 2`. For each, the residue and an explicit representation with `max(|x|,|y|,|z|) <= 1000` where one exists:[^exec]

| `F` | cell | mod 9 | three cubes | positive |
|---|---|---|---|---|
| 3 | `(3, 3)` | 3 | `1^3 + 1^3 + 1^3` | yes |
| 6 | `(3, 2)` | 6 | `(-1)^3 + (-1)^3 + 2^3` |  |
| 10 | `(3, 5)`, `(4, 2)` | 1 | `1^3 + 1^3 + 2^3` | yes |
| 16 | `(5, 2)` | 7 | `0^3 + 2^3 + 2^3` |  |
| 21 | `(3, 7)`, `(4, 3)` | 3 | `(-11)^3 + (-14)^3 + 16^3` |  |
| 28 | `(6, 2)` | 1 | `0^3 + 1^3 + 3^3` |  |
| 31 | `(3, 4)` | 4 | **no** |  |
| 36 | `(3, 9)` | 0 | `1^3 + 2^3 + 3^3` | yes |
| 55 | `(3, 11)` | 1 | `1^3 + 3^3 + 3^3` | yes |
| 56 | `(7, 2)` | 2 | `0^3 + (-2)^3 + 4^3` |  |
| 76 | `(3, 6)` | 4 | **no** |  |
| 78 | `(3, 13)` | 6 | `26^3 + 53^3 + (-55)^3` |  |
| 89 | `(5, 3)` | 8 | `6^3 + 6^3 + (-7)^3` |  |
| 105 | `(3, 15)` | 6 | `(-4)^3 + (-7)^3 + 8^3` |  |
| 117 | `(4, 4)` | 0 | `0^3 + (-2)^3 + 5^3` |  |
| 120 | `(8, 2)` | 3 | `(-2)^3 + 4^3 + 4^3` |  |
| 122 | `(4, 5)` | 5 | **no** |  |
| 136 | `(3, 17)` | 1 | `2^3 + 4^3 + 4^3` | yes |
| 141 | `(3, 8)` | 6 | `2^3 + 2^3 + 5^3` | yes |
| 171 | `(3, 19)` | 0 | `(-5)^3 + (-6)^3 + 8^3` |  |
| 210 | `(3, 21)` | 3 | `(-2)^3 + (-5)^3 + 7^3` |  |
| 226 | `(3, 10)` | 1 | `2^3 + (-5)^3 + 7^3` |  |
| 253 | `(3, 23)` | 1 | `4^3 + 4^3 + 5^3` | yes |
| 256 | `(9, 2)` | 4 | **no** (`4 * 4^3`) |  |
| 300 | `(3, 25)` | 3 | `34^3 + 55^3 + (-59)^3` |  |
| 307 | `(6, 3)` | 1 | `(-5)^3 + 6^3 + 6^3`; also `3^3 + 4^3 + 6^3` | yes |
| 331 | `(3, 12)` | 7 | `0^3 + (-10)^3 + 11^3` |  |
| 351 | `(3, 27)` | 0 | `0^3 + 2^3 + 7^3` |  |
| 367 | `(4, 7)` | 7 | none with `max <= 50000` |  |
| 406 | `(3, 29)` | 1 | `(-1)^3 + 4^3 + 7^3` |  |
| 439 | `(5, 4)` | 7 | none with `max <= 50000` |  |
| 448 | `(4, 6)` | 7 | `0^3 + (-4)^3 + 8^3` |  |
| 456 | `(3, 14)` | 6 | `2^3 + (-4)^3 + 8^3` |  |
| 465 | `(3, 31)` | 6 | `11^3 + 11^3 + (-13)^3` |  |
| 528 | `(3, 33)`, `(10, 2)` | 6 | `2^3 + 2^3 + 8^3` | yes |
| 595 | `(3, 35)` | 1 | `21^3 + 37^3 + (-39)^3` |  |
| 601 | `(3, 16)` | 7 | `(-4)^3 + (-4)^3 + 9^3` |  |
| 666 | `(3, 37)` | 0 | `1^3 + (-4)^3 + 9^3` |  |
| 741 | `(3, 39)` | 3 | `(-5)^3 + (-11)^3 + 13^3` |  |
| 766 | `(3, 18)` | 1 | `(-3)^3 + 4^3 + 9^3` |  |
| 820 | `(3, 41)`, `(4, 9)` | 1 | `(-5)^3 + 6^3 + 9^3`; also `3^3 + 4^3 + 9^3` | yes |
| 903 | `(3, 43)` | 3 | none with `max <= 50000` |  |
| **906** | **`(5, 5)`** | 6 | `(-74924259395610397)^3 + 72054089679353378^3 + 35961979615356503^3` |  |
| 951 | `(3, 20)` | 6 | `(-10)^3 + (-25)^3 + 26^3` |  |
| 977 | `(7, 3)` | 5 | **no** |  |
| 990 | `(3, 45)` | 0 | `(-5)^3 + (-6)^3 + 11^3` |  |

Five of the fifty are excluded (`31, 76, 122, 256, 977`), one in ten, and each is where the closed forms say: `31 = F(3,4)` and `76 = F(3,6)` at `h = 4, 6`, `256 = F(9,2) = 4 * 4^3`. Forty-one have a representation with all three cubes below `1000^3`. The remaining four are real: `367`, `439`, `903` have no representation with `max(|x|,|y|,|z|) <= 50000` (searched with `|x| <= |y| <= |z|`), yet all three are solved in the literature, since every `n < 1000` off the excluded classes is solved except `114, 390, 627, 633, 732, 921, 975`.[^1] And `906 = F(5,5)`: the even-block castles of the `5 x 5` cell are counted by one of the numbers Booker and Sutherland cracked in 2019, whose smallest known cubes have 17 digits.[^1] The triple was re-multiplied exactly for this page.

**The seven unsolved numbers are not nondegenerate castle counts.** None of `114, 390, 627, 633, 732, 921, 975` appears in the `A`, `F`, or odd table for `w >= 3`, `h >= 2` (the scan covers every cell with `A <= 20000`, hence every count below 1000). In the degenerate width-2 cell, `627 = F(2, 314)` and `975 = F(2, 488)`, `633 = odd(2, 317)` and `921 = odd(2, 461)`, while the three even ones `114, 390, 732` are not castle counts at any width (`A(1,h) = 1` and `A(2,h) = 2h - 1` are odd).[^exec]

Between 1000 and 20000 the `F` table has 141 entries at `w >= 3`; 11 are excluded mod 9 and 130 admissible. Of the admissible, 105 have a representation with cubes below `1000^3`, five more were found below `15000^3` (`F(3,61) = 1830 = (-8993)^3 + 9076^3 + (-2729)^3`, `F(3,89) = 3916 = (-9719)^3 + 9867^3 + (-3492)^3`, `F(4,12) = 4065 = (-1591)^3 + 1490^3 + 896^3`, `F(3,50) = 6126 = (-6592)^3 + 6677^3 + (-2239)^3`, `F(3,56) = 7701 = (-5755)^3 + 5651^3 + 2165^3`), and twenty (`1131, 1626, 2481, 2630, 2775, 3741, 5050, 6555, 8445, 9321, 9591, 9870, 11391, 11490, 12246, 12561, 14196, 15801, 16653, 17391`) have none below `15000^3`. Small castle counts are, in this respect too, ordinary integers: about one admissible `n` in six below 20000 needs cubes above `15000^3`.[^exec]

## Sums of three positive cubes: castle counts are random integers

The positive version is finite, so it can be settled outright. Sums of three positive cubes have measured density `0.101` below `10^8` ([[sums-of-three-cubes](pages/sums-of-three-cubes.md)]). Testing every castle count:[^exec]

| table, cells | entries `<= 10^8` | sums of three positive cubes | expected at `0.101` |
|---|---|---|---|
| `F`, `w >= 4` | 552 | **56** | 55.7 |
| `F`, `w = 3` | 10232 | 1387 (13.6%) | 1033 |
| `A`, `w >= 4` | 446 | 69 | 45.0 |
| odd, `w >= 4` | 555 | 58 | 56.0 |

The even-block table at `w >= 4` lands on the null rate to within one hit: **castle counts behave like random integers with respect to sums of three positive cubes.** The width-3 column runs high because it is two quadratics in `h` and small numbers are denser in cube sums (the density is `0.126` below `1000`). The `A` table's excess at `w >= 4` is partly the `w = 6` entries, which are differences of cubes and so already one cube away from the target.

The 56 even-block hits with `w >= 4`, each read in tower language as `F(w,h) = T(a-1,3) + T(b-1,3) + T(c-1,3)`, a disjoint union of three families of length-3 towers ([[tower-recursion-master-class](pages/tower-recursion-master-class.md)]). The first ten:

| `F(w,h)` | cell | `a^3 + b^3 + c^3` | tower reading |
|---|---|---|---|
| 10 | `(4, 2)` | `1^3 + 1^3 + 2^3` | two empty towers and the 8 binary towers of length 3 |
| 307 | `(6, 3)` | `3^3 + 4^3 + 6^3` | `T(2,3) + T(3,3) + T(5,3)` |
| 528 | `(10, 2)` | `2^3 + 2^3 + 8^3` | `2 T(1,3) + T(7,3)` |
| 820 | `(4, 9)` | `3^3 + 4^3 + 9^3` | `T(2,3) + T(3,3) + T(8,3)` |
| 6572 | `(4, 14)` | `10^3 + 13^3 + 15^3` | `T(9,3) + T(12,3) + T(14,3)` |
| 8128 | `(14, 2)` | `4^3 + 4^3 + 20^3` | the perfect number, `2 T(3,3) + T(19,3)` |
| 9037 | `(5, 8)` | `13^3 + 14^3 + 16^3` | `T(12,3) + T(13,3) + T(15,3)` |
| 54757 | `(4, 35)` | | |
| 86505 | `(11, 3)` | `2^3 + 26^3 + 41^3` | `T(1,3) + T(25,3) + T(40,3)` |
| 190630 | `(4, 42)` | | |

The remaining 46 are at `(4, h)` for `h` in `{52, 80, 93, 118, 122, 143, 149, 155, 163, 182, 187, 191, 210, 214, 233, 236, 249, 251, 258, 260, 272, 295, 307, 322, 347, 379, 387, 413}`, `(5, h)` for `h` in `{26, 27, 35, 40, 60, 61, 67}`, `(6, 14)`, `(6, 16)`, `(7, 8)`, `(7, 9)`, `(7, 17)`, `(16, 3)`, and the height-2 entries `(19, 2), (20, 2), (22, 2), (25, 2), (26, 2)`.[^exec] The bijection question of [[hardy-ramanujan-castle](pages/hardy-ramanujan-castle.md)] (even castles of a cell onto a disjoint union of tower families) has 56 further instances here; `F(4,2) = 10` is small enough to do by hand and is the natural first target, since the ten even castles of `(4,2)` are the triangular number `C(5,2)` and the towers are `{0,1}^3` plus two points.

## Two cubes, one cube, cube plus one

The finer cube properties, over all cells with `A <= 10^9` and `w >= 3`:[^exec]

- **Perfect cubes.** Only `F(13,2) = 16^3` and `F(25,2) = 256^3` (and the trivial `odd(3,2) = 1`): every cube castle count in range is a height-2 power of two, `F(12k+1, 2) = (16^k)^3`.
- **Sums of two positive cubes** (A003325) in the `F` table with `w >= 4`: `16 = F(5,2)`, `28 = F(6,2)`, `1729 = F(6,4)`, `65536 = F(17,2)`, `262656 = F(19,2)`, `804482 = F(4,85) = 5^3 + 93^3`, `268435456 = F(29,2)`. The height-2 ones are structural (the `2 c^3` and `c^3 + d^3` residues above); the two that are not, `F(6,4) = 1^3 + 12^3 = 9^3 + 10^3` and `F(4,85) = 5^3 + 93^3`, are the only sums of two positive cubes among even-block counts with `w >= 4` and `h >= 3` below `10^9`. The taxicab number stays the only taxicab castle count.
- **Cube plus or minus one.** `28 = 3^3 + 1 = F(6,2)`, `1729 = 12^3 + 1 = F(6,4)`, `4095 = 16^3 - 1 = F(3,91) = A(12,2)`, `8001 = 20^3 + 1 = F(3,127)`; the last two are triangular numbers, `C(91,2)` and `C(127,2)`, so the width-3 column supplies Fermat near-misses of its own.
- **Differences of two positive cubes** in the `F` table below `10^7`, outside height 2 and the structural `A(3m,h)`: `F(3,12) = 331 = 11^3 - 10^3`, `F(4,4) = 117 = 5^3 - 2^3`, `F(4,6) = 448 = 8^3 - 4^3`, `F(3,109) = 5886 = 21^3 - 15^3`, `F(3,135) = 9045 = 21^3 - 6^3`, `F(3,209) = 21736 = 28^3 - 6^3`, `F(3,190) = 89776 = 51^3 - 35^3`, `F(4,144) = 7880087 = 199^3 - 8^3`, and about thirty more at `w = 3`.

## What this page settles and what it opens

Settled:

- Under Heath-Brown, "is `F(w,h)` a sum of three cubes" is the residue test, and the residue is periodic in both directions with the periods tabulated above; the excluded fraction of the `F` table is `22%` at `w >= 4` (`2/9` in the limit), `1/9` at `w = 3`, `1/12` at `h = 2`.
- Unconditionally: `A(3m, h)` is always a difference of two cubes; `F(w,2)` is a cube at `w = 1 (mod 12)`, twice a cube at `w = 5`, four times a cube and excluded at `w = 9`, and these are the row's only exclusions; `F(3,h)` at odd `h` is triangular and never excluded, at even `h` is `5 C(h,2) + 1` and excluded iff `h = 4, 6 (mod 18)`.
- `F(10^12, 100), F(10000, 10000), F(100, 10^12)` are `6, 7, 6 (mod 9)`: all admissible.
- `F(5,5) = 906` is a Booker-Sutherland 2019 number; none of the seven unsolved `n < 1000` is a castle count outside the width-2 cell.
- Even-block counts with `w >= 4` are sums of three positive cubes at exactly the background rate (56 of 552 against 55.7); the taxicab number and `F(4,85) = 5^3 + 93^3` are the only nondegenerate two-cube even counts below `10^9`.
- Even perfect numbers: `2^{p-1}(2^p - 1) = F(2p, 2)` for `p = 3 (mod 4)` and `= odd(3, 2^p)` for all `p`.

Open:

- **Mod-9 equidistribution of the `F` table.** The `w >= 4` exclusion rate is `20.4%` against `22.2%` expected, and the `h = 7` row sits at `20.1%` over an exact period of 2184; is the deficit structural (a bias in `P(k,w) mod 9`) or does it wash out with `h`? The `h = 12` row at `22.21%` over 11.5 million terms says it washes out row by row.
- **A bijection for `F(13,2) = T(15,3)`** and for the 56 positive-cube identities, `F(4,2) = 10 = 1 + 1 + 8` first; the Hardy-Ramanujan page's `1729 = 12^3 + 1` question with a smaller test case.
- **Representations for `367 = F(4,7)`, `439 = F(5,4)`, `903 = F(3,43)`** below `50000^3` do not exist; the literature has them, and recording the smallest is a lookup, not a computation.

## Appearances in Sources

- [[oeis-mining-pe502](pages/oeis-mining-pe502.md)] - the `F(w,h)` tabulation in which `1729`, `906`, and the height-2 powers of two were first visible.
- [[project-euler-502-solution](pages/project-euler-502-solution.md)] - `T(k, L) = (k+1)^L`, the tower count behind the cube reading, and the Kitamasa route the mod-9 evaluation reuses.
- [[project-euler-502](pages/project-euler-502.md)] - the three target arguments tested mod 9.

## Related Concepts

- [[sums-of-three-cubes](pages/sums-of-three-cubes.md)] - the number-theory background: the mod-9 obstruction, Heath-Brown, the 2019 results, the positive-cube density.
- [[hardy-ramanujan-castle](pages/hardy-ramanujan-castle.md)] - `F(6,4) = 1729`, the page this one generalizes.
- [[castle-counting-formula](pages/castle-counting-formula.md)] and [[castle-counting-function](pages/castle-counting-function.md)] - the closed form and the `A / F / odd` notation.
- [[mod-p-observatory](pages/mod-p-observatory.md)] - period equals lcm of eigenvalue orders; the mod-9 periods here extend its tables.
- [[signed-tower-k-direction](pages/signed-tower-k-direction.md)] - the `(x+1)^L (x-1)^{L-2}` characteristic polynomial behind the height-direction periods.
- [[kitamasa](pages/kitamasa.md)] and [[castle-cryptography-ring](pages/castle-cryptography-ring.md)] - `x^w mod char_k` over `Z/9` for the PE 502 targets.
- [[oeis-height2-hyperbolic-castles](pages/oeis-height2-hyperbolic-castles.md)] and [[hyperbolic-sequence-family](pages/hyperbolic-sequence-family.md)] - `F(w,2) = A038505(w+1)`, whose closed form the height-2 row reads off.
- [[fractional-width-and-height](pages/fractional-width-and-height.md)] - the cosine form of `F(w,2)`.
- [[tower-recursion-master-class](pages/tower-recursion-master-class.md)] - `T(k,3) = (k+1)^3`.
- [[binary-string-bijection](pages/binary-string-bijection.md)] - the `2^{w-1}` reading of the height-2 row.
- [[castle-snippets](pages/castle-snippets.md)] - `all_castles`, `blocks`, the brute-force check of the DP.
- [[castle-sequence-catalogue](pages/castle-sequence-catalogue.md)] and [[oeis-index](pages/oeis-index.md)] - where A000217, A003072, A003325, A038505, A060464 sit on the wiki.

## Footnotes

[^1]: https://en.wikipedia.org/wiki/Sums_of_three_cubes (2026-09-20) - the mod-9 condition and "It is unknown whether this necessary condition is sufficient"; Heath-Brown's conjecture of infinitely many representations for every `n` not `4, 5 (mod 9)`; "The only remaining unsolved cases up to 1,000 are the seven numbers 114, 390, 627, 633, 732, 921, and 975"; the 2019 representations of 33 (Booker), 42 and 906 (Booker and Sutherland) with the `906 = (-74924259395610397)^3 + 72054089679353378^3 + 35961979615356503^3` triple.
[^3]: https://oeis.org/A080860 (2026-09-20) - "a(n) = 10*n^2 + 5*n + 1", data `1, 16, 51, 106, 181, 276, 391, 526, 681, 856, 1051, 1266, 1501, 1756, 2031, 2326, ...`, g.f. `(1 + 13x + 6x^2)/(1-x)^3`; OEIS term searches for `6, 31, 76, 141, 226, 331, 456, 601, 766, 951`, for `1, 6, 31, 76, 141, 226, 331`, and for the interleaved columns `F(3,h)`, `odd(3,h)`, `F(4,h)` returned no match (2026-09-20).
[^exec]: Verified by execution (2026-09-20): Python 3 scripts with NumPy 1.26 and SymPy 1.14. (1) Exact `P(k,L)` by the signed last-height DP and `F = (A - P(h-1,w) + P(h-2,w))/2`, checked against brute-force enumeration for `w <= 5`, `h <= 4` and against `F(4,2) = 10`, `F(6,4) = 1729`, `F(13,10)`, `F(10,13)`. (2) Width-direction periods mod 9 by iterating the `4h`-state parity transfer matrix over `Z/9` until the state vector repeats (state period and transient), then the minimal divisor of the state period that the `F`, `A`, and odd read-outs obey; `h = 12` needed 11.5 million steps. (3) Height-direction periods by the order-`(2w-2)` recurrence with characteristic polynomial `(x+1)^w (x-1)^{w-2}`, seeded with exact `P(k,w)` for `k < 2w-2` and checked exactly for four further terms, run mod 9 to `k = 6000`; residues re-checked against exact `F(w,h)` for `w <= 6`, `h < 20`. (4) PE 502 targets: `den_k` built by the `num/den` polynomial recurrence over `Z/9`, initial `P(k, 0..k)` by series division, `x^L mod rev(den_k)` by square-and-multiply with NumPy convolution and long-division reduction; validated against exact `P(k,L)` for `k <= 6`, `L <= 14` and against `F(4,2), F(13,10), F(10,13), F(100,100)`; `F(10^12,100)` re-derived by binary powering of the 400-state transfer matrix over `Z/9`; `P(k,100)` at `k = 250, 251, 400` agrees between the `k`-direction recurrence and the `L`-direction Kitamasa; `P(k,100) mod 9` has period 1458 in `k` and reduction of `10^12` mod 1458 reproduces the Kitamasa residues. (5) Small counts: every cell with `A <= 20000`, `w >= 3`; residue mod 9; signed representation by a dictionary of `x^3 + y^3` for `|x|, |y| <= 1000` probed at `n - z^3`; a second pass with `max(|x|,|y|,|z|) <= 15000` for every admissible count below 20000 in any table that the first missed (ten found) and a third with `|x| <= |y| <= |z| <= 50000` for the eight below 1000 (one found, `276 = odd(3,11) = odd(3,24) = 2396^3 + 15131^3 + (-15151)^3`); every representation printed was re-multiplied exactly. (6) Positive cubes: all cells with `A <= 10^9`, `3 <= w <= 30` (19,132 cells), tested against a set of `a^3 + b^3 <= 10^9` (439,959 values) for three positive cubes, membership for two, exact cube roots for cubes and cube `+-1`, and a `y`-loop for differences of two cubes below `10^7`; density of sums of three positive cubes by a boolean sieve to `10^8`. (7) Height-2 row: `F(w,2)` for `w <= 48` against `2^{w-1} + eps_w 2^{floor((w-1)/2)}` and against the cosine form; cube / `2 c^3` / `4 c^3` / two-cube classification per `w mod 24`; `F(2p,2) = 2^{p-1}(2^p - 1)` for `p = 3, 7, 11, 19, 23, 31` and the `p = 5, 13, 17` counterexamples; `C(2^p, 2) = 2^{p-1}(2^p - 1)` for `p = 2, 3, 5, 7, 13`. (8) Width-3 column: SymPy interpolation on even and odd `h` separately for `F(3,h)`, `odd(3,h)`, `F(4,h)`, `odd(4,h)`; the `F(3,h)` forms re-checked for `h <= 30`; triangular residues mod 9 over `n < 100`. All quoted numbers are the scripts' printed output.
