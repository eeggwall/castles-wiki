---
title: The Hardy-Ramanujan castle (1729)
category: Analyses
summary: 1729, the taxicab number 1^3 + 12^3 = 9^3 + 10^3, is a castle count - A^e(6, 4) = 1729, the only cell with w, h <= 40 where 1729 appears among A, A^e and A^o, and A(6, 4) = 16^3 - 9^3 is a difference of cubes in the same cell. The rearrangement 9^3 + 10^3 + (-12)^3 = 1 leads to Ramanujan's near-miss family a_n^3 + b_n^3 = c_n^3 + (-1)^n, a linear recurrence with denominator (1 + x)(1 - 83x + x^2) that Berlekamp-Massey recovers from six terms; 1729 is its n = -1 term, and its growth constant (83 + 9 sqrt 85)/2 is the square of the metallic mean delta_9 = (9 + sqrt 85)/2, the Perron root of the height-10 ridge matrix R_10 = J - D. Also - the base-10 digit castle (1, 7, 2, 9) (an even-block castle of area 19, Ramanujan in the spectral sense, with skyline DFT bins 19, 13 and 2 +- i that give 1729 mod 9, mod 11 and mod 101), the first four Carmichael numbers 561, 1105, 1729, 2465 as castle counts, and A^e(w, h) mod 1729 with periods 72, 2520, 25200 at h = 2, 3, 4.
tags: [analysis, castle, 1729, taxicab, hardy-ramanujan, dft, divisibility-test, sum-of-cubes, near-miss, c-finite, berlekamp-massey, metallic-mean, carmichael, mod-p, worked-example, computation]
sources: [oeis-mining-pe502, project-euler-502-solution]
created: 2026-09-19
updated: 2026-10-16
---

# The Hardy-Ramanujan castle (1729)

1729 is the taxicab number, the smallest integer that is a sum of two positive cubes in two ways: `1^3 + 12^3 = 9^3 + 10^3`. In Hardy's account, Hardy visited Ramanujan in Putney in taxi number 1729 and remarked that the number seemed a dull one; Ramanujan answered that it was "the smallest number expressible as the sum of two cubes in two different ways."[^1] This page collects the connections between 1729 and castles. The main one is `A^e(6, 4) = 1729`: the even-block castles of width 6 and height 4, the count Project Euler 502 writes `F(6, 4)`, number 1729, and this is the only place 1729 appears among the counts `A`, `A^e` and `A^o` for `w, h ≤ 40`. A second connection runs from the rearrangement `9^3 + 10^3 + (−12)^3 = 1` to Ramanujan's family of near-misses to Fermat's equation, a linear recurrence whose growth constant is the square of a metallic mean.

[[ramanujan-castles](pages/ramanujan-castles.md)] is a different subject, the spectral Ramanujan property of castle graphs; the two pages meet once, since the digit castle `(1, 7, 2, 9)` has that property.

## The number 1729

| property | statement | source |
|---|---|---|
| taxicab `Ta(2)` | `1^3 + 12^3 = 9^3 + 10^3 = 1729`, the first term of A001235 (`1729, 4104, 13832, 20683, …`); the two representations were published by Frenicle de Bessy in 1657 | [^1] [^2] |
| `12^3 + 1` | `9^3 + 10^3 = 12^3 + 1`, a near-miss to Fermat's equation for cubes, and the first term of A050794 (`x^3 + y^3 = z^3 + 1` with `1 < x < y < z`) | [^3] |
| factorization | `1729 = 7 · 13 · 19 = 13 · 133 = (12 + 1)(12^2 − 12 + 1) = Φ_2(12) · Φ_6(12)`, with `Φ_n` the `n`-th cyclotomic polynomial | [^exec] |
| Carmichael | the third Carmichael number (A002997: `561, 1105, 1729, 2465, …`): `a^1728 ≡ 1 (mod 1729)` for every `a` coprime to 1729 (checked for all such `a`), and by Korselt's criterion `6`, `12` and `18` divide `1728` | [^4] [^exec] |
| centered cube | `9^3 + 10^3` is the centered cube number with `n = 9` | [^1] |
| Harshad | the digit sum `1 + 7 + 2 + 9 = 19` divides 1729 (`1729 = 19 · 91`) | [^exec] |
| palindromic bases | `1001` in base 12, `1 22 1` in base 32, `1 12 1` in base 36 | [^1] [^exec] |
| Ono, Trebat-Leder | Ramanujan's notes on `a^3 + b^3 = c^3 + d^3` around 1729 contain a K3 surface of Picard number 18, which gives infinitely many cubic twists of rank at least 2 | [^5] |

The continued fraction of the cube root is `1729^{1/3} = [12; 432, 12, 648, 9, 1, …]`. The large second partial quotient comes from `1729 = 12^3 + 1`: to first order, `(12^3 + 1)^{1/3} ≈ 12 + 1/(3 · 12^2) = 12 + 1/432`.[^exec]

## 1729 is a castle count: the cell (6, 4)

The row `A^e(w, 4)` of the mining notes reads `1, 7, 31, 117, 439, 1729, 7063, 29201, …`, so `A^e(6, 4) = 1729`.[^6] Enumerating the `4^6 − 3^6 = 3367` skylines in `{1, …, 4}^6` that reach 4, with the block count `c_1 + Σ max(0, c_i − c_{i−1})` ([[castle-snippets](pages/castle-snippets.md)]), gives:[^exec]

| quantity at `(w, h) = (6, 4)` | value | factorization |
|---|---|---|
| `A(6, 4) = 4^6 − 3^6` | 3367 | `7 · 13 · 37 = 91 · 37` |
| `A^e(6, 4)` | **1729** | `7 · 13 · 19 = 91 · 19` |
| `A^o(6, 4)` | 1638 | `2 · 3^2 · 7 · 13 = 91 · 18` |
| `P(2, 6)`, `P(3, 6)` (signed tower counts) | 59, −32 | |
| `S(6, 4) = A^e − A^o = P(2, 6) − P(3, 6)` | 91 | `7 · 13` |

The [[castle-counting-formula](pages/castle-counting-formula.md)], `A^e(w, h) = [h^w − (h−1)^w − P(h−1, w) + P(h−2, w)]/2`, gives `(3367 + 32 + 59)/2 = 1729`. The cell carries three facts about cubes:

- **`A(6, 4)` is a difference of cubes.** `4^6 = 16^3` and `3^6 = 9^3`, so `A(6, 4) = 16^3 − 9^3 = (16 − 9)(16^2 + 16 · 9 + 9^2) = 7 · 481 = 3367`.
- **The taxicab identity in tower counts.** The tower count `T(k, L) = (k+1)^L` ([[castle-counting-formula](pages/castle-counting-formula.md)]) makes `T(k, 3) = (k+1)^3` a cube, so the taxicab identity reads `T(0, 3) + T(11, 3) = T(8, 3) + T(9, 3) = A^e(6, 4)`: two disjoint unions of tower sets, each with 1729 elements, and the 1729 even-block castles. `T(0, 3) = 1` counts the empty towers.
- **Every count in the cell is a multiple of `91 = 4^3 + 3^3`.** For `A` this is the factorization `4^6 − 3^6 = (4^3 − 3^3)(4^3 + 3^3) = 37 · 91`. The signed count `S(6, 4) = 91` is a separate fact: along `h = 4` the signed counts `S(w, 4)` are `1, 7, 25, 59, 97, 91, −71, −573, …` for `w = 1, 2, …`, and `S(w, h) = h^3 + (h−1)^3` holds at no other `(w, h)` with `h ≤ 6`, `w ≤ 10`. So `A^e = (A + S)/2 = 91 · (37 + 1)/2 = 91 · 19`.[^exec]

**Uniqueness.** Among all `(w, h)` with `w, h ≤ 40` and `A(w, h) ≤ 10^9`, the number 1729 occurs once in the three tables `A`, `A^e`, `A^o`: as `A^e(6, 4)`.[^exec] Outside that range, `A(2, h) = 2h − 1` gives `A(2, 865) = 1729`. A castle `(a, b)` of width 2 and height `h` has `max(a, b) = h` blocks, so at `h = 865` all of them have an odd number of blocks: `A^o(2, 865) = 1729` and `A^e(2, 865) = 0`.

**The other Carmichael numbers.** The same sweep, run on the first 33 Carmichael numbers, the first 15 taxicab numbers and the first 6 near-misses of A050794, finds four values, the first four Carmichael numbers:[^exec]

| Carmichael number | castle count |
|---|---|
| 561 | `A^o(3, 34)` |
| 1105 | `A(4, 7) = 7^4 − 6^4` |
| **1729** | **`A^e(6, 4)`** |
| 2465 | `A(4, 9) = 9^4 − 8^4` |

No other taxicab number and no other near-miss is a castle count in that range. The two values of `A(4, h)` are differences of fourth powers, `h^4 − (h−1)^4 = (2h − 1)(2h^2 − 2h + 1)`, the rhombic dodecahedral numbers A005917 (`1, 15, 65, 175, 369, 671, 1105, 1695, 2465, …`), which are Carmichael numbers at `h = 7` and `h = 9`.[^9]

**Rank 1729.** Under the rank/unrank bijection of [[song-as-castle](pages/song-as-castle.md)], which orders the castles of a cell by the position of their first column of height `h`, castle number 1729 of the cell `(6, 4)` is the skyline `(3, 4, 4, 1, 1, 2)`, with 5 blocks, so it is not an even-block castle. In rank order, the 1729 even-block castles of the cell run from `(4, 1, 1, 1, 1, 1)` to `(3, 3, 3, 3, 3, 4)`, and indexing them takes `log_2 1729 = 10.756` bits.[^exec]

## The sum of three cubes

Moving `12^3` to the other side of the taxicab identity gives a representation of 1 as a sum of three integer cubes:

```
9^3 + 10^3 + (−12)^3  =  1.
```

The triple `(9, 10, −12)` appears in the table of primitive solutions of `x^3 + y^3 + z^3 = 1`; in the problem of representing integers as sums of three cubes, the cases `33` (Booker) and `42` (Booker and Sutherland) were settled in 2019.[^7] Cubes are `0` or `±1 (mod 9)`, so no integer `≡ 4, 5 (mod 9)` is a sum of three cubes; `1729 ≡ 1 (mod 9)`. With `|x|, |y|, |z| ≤ 300`, 1729 has four representations as a sum of three integer cubes: `(0, 1, 12)`, `(0, 9, 10)`, `(−7, −5, 13)` and `(−215, 98, 208)`. The two with a zero are the taxicab pair, and `13^3 − 7^3 − 5^3 = 2197 − 343 − 125 = 1729`.[^exec]

For the sum 1 there is a polynomial family, Mahler's `(9t^4)^3 + (3t − 9t^4)^3 + (1 − 9t^3)^3 = 1` (an identity in `t`; `t = 1` gives `9^3 + (−6)^3 + (−8)^3 = 1`).[^7] Ramanujan's family, in the next section, is of a different kind.

## Ramanujan's near-miss family is a linear recurrence

Ramanujan gave three rational generating functions:[^8]

```
Σ a_n x^n  =  (1 + 53x +  9x^2) / (1 − 82x − 82x^2 + x^3)      A051028: 1, 135, 11161, 926271, …
Σ b_n x^n  =  (2 − 26x − 12x^2) / (1 − 82x − 82x^2 + x^3)      A051029: 2, 138, 11468, 951690, …
Σ c_n x^n  =  (2 +  8x − 10x^2) / (1 − 82x − 82x^2 + x^3)      A051030: 2, 172, 14258, 1183258, …
```

with `a_n^3 + b_n^3 = c_n^3 + (−1)^n` for every `n ≥ 0`, an infinite family of near-misses to `x^3 + y^3 = z^3` that miss by 1 with alternating sign. The common denominator means that all three sequences satisfy `s_n = 82 s_{n−1} + 82 s_{n−2} − s_{n−3}`. Hirschhorn proved the identity in 1995, and again in 1996 by noting that both sides satisfy a recurrence of bounded order, so that checking `n = 0, …, 6` suffices.[^8]

The recurrence also runs backwards, `s_{n−3} = 82 s_{n−1} + 82 s_{n−2} − s_n`, and the term `n = −1` is the taxicab identity:[^exec]

| `n` | `a_n` | `b_n` | `c_n` | `a_n^3 + b_n^3 − c_n^3` |
|---|---|---|---|---|
| −4 | −5444135 | 6954572 | 5593538 | +1 |
| −3 | −65601 | 83802 | 67402 | −1 |
| −2 | −791 | 1010 | 812 | +1 |
| **−1** | **−9** | **12** | **10** | **−1** |
| 0 | 1 | 2 | 2 | +1 |
| 1 | 135 | 138 | 172 | −1 |
| 2 | 11161 | 11468 | 14258 | +1 |
| 3 | 926271 | 951690 | 1183258 | −1 |
| 4 | 76869289 | 78978818 | 98196140 | +1 |
| 5 | 6379224759 | 6554290188 | 8149096378 | −1 |

Row `n = −1` is `(−9)^3 + 12^3 = 10^3 − 1`, that is `9^3 + 10^3 = 12^3 + 1 = 1729`. Row `n = −2` is `791^3 + 812^3 = 1010^3 + 1`, and row `n = 1` is `135^3 + 138^3 = 172^3 − 1`. Every row was checked in integer arithmetic.

**Berlekamp-Massey recovers the denominator.** Over the rationals, [[berlekamp-massey](pages/berlekamp-massey.md)] returns linear complexity 3 and the connection polynomial `1 − 82x − 82x^2 + x^3` from the first six terms of `c_n` (and the same from twelve), the order-3 case of its guarantee from `2L` terms ([[recurrence-discovery](pages/recurrence-discovery.md)] applies it to the castle counts).[^exec]

**The denominator factors.**

```
1 − 82x − 82x^2 + x^3  =  (1 + x)(1 − 83x + x^2)
x^3 − 82x^2 − 82x + 1  =  (x + 1)(x^2 − 83x + 1)          (characteristic polynomial)
```

The characteristic polynomial has coefficients `[1, −82, −82, 1]`, so it is palindromic, and its roots are closed under `r ↦ 1/r`: the reciprocal pair of roots of `x^2 − 83x + 1` and the root `−1` ([[eigenvalue-continued-fractions](pages/eigenvalue-continued-fractions.md)]). The root `−1` gives the `(−1)^n` on the right of the identity. Partial fractions give

```
a(x)  =   8(16 + 101x) / (85 (1 − 83x + x^2))  −  43 / (85 (1 + x))
b(x)  =  14(11 −  74x) / (85 (1 − 83x + x^2))  +  16 / (85 (1 + x))
c(x)  =   6(31 − 139x) / (85 (1 − 83x + x^2))  −  16 / (85 (1 + x))
```

so `b_n + c_n` has no `(−1)^n` component and satisfies the order-2 recurrence of `1 − 83x + x^2`: `4, 310, 25726, 2134948, …`, with `83 · 310 − 4 = 25726`. Hirschhorn's closed forms have the same shape, `a_n = [(64 + 8√85) α^n + (64 − 8√85) β^n − 43 (−1)^n]/85` with `α, β = (83 ± 9√85)/2`.[^8] The `85` in every denominator divides the discriminant `83^2 − 4 = 6885 = 81 · 85`.

## The growth constant is a metallic mean squared

The dominant root of `x^2 − 83x + 1` is `α = (83 + 9√85)/2 = 82.98795…`. Since `85 = 9^2 + 4`, the metallic mean with `a = 9` ([[metallic-means](pages/metallic-means.md)]) is `δ_9 = (9 + √85)/2 = 9.10977…`, the root of `x^2 − 9x − 1`, with continued fraction `[9; 9, 9, 9, …]`, and[^exec]

```
δ_9^2  =  ((9 + √85)/2)^2  =  (166 + 18√85)/4  =  (83 + 9√85)/2  =  α.
```

So Ramanujan's near-miss triples grow, from one term to the next, by the factor `δ_9^2`. The roots of `x^2 − 9x − 1` are `δ_9` and `−1/δ_9`, a unit of norm `−1`, and their squares `δ_9^2` and `δ_9^{−2}` are the roots of `x^2 − 83x + 1`, a unit of norm `+1`. Their continued fractions differ accordingly: `δ_9^2 = [82; 1, 81, 1, 81, …]` is not purely periodic, since its conjugate `δ_9^{−2}` lies in `(0, 1)`, not in `(−1, 0)`, so `δ_9^2` is not a reduced quadratic surd ([[eigenvalue-continued-fractions](pages/eigenvalue-continued-fractions.md)]). The Lucas sequence `V_n = δ_9^n + (−1/δ_9)^n` of `x^2 − 9x − 1` is `2, 9, 83, 756, …`, and `V_2 = δ_9^2 + δ_9^{−2} = 83` is the trace of `x^2 − 83x + 1`.

**`δ_9` on the castle side.** The ridge rule allows two neighboring columns of the same height only at the ceiling `h`; its transfer matrix `R_h = J − D`, with `J` the all-ones matrix and `D = diag(1, …, 1, 0)`, has characteristic polynomial `(x + 1)^{h−2}(x^2 − (h−1)x − 1)` and Perron root `δ_{h−1}` ([[ridge-castle](pages/ridge-castle.md)], [[metallic-strip-realizability](pages/metallic-strip-realizability.md)]). At `h = 10`:[^exec]

```
charpoly(R_10)    =  (x + 1)^8 (x^2 − 9x − 1)          Perron root  δ_9    =  9.10977…
charpoly(R_10^2)  =  (x − 1)^8 (x^2 − 83x + 1)         Perron root  δ_9^2  =  82.98795…

ridge strips 1ᵀ R_10^{n−1} 1, n = 1, …, 8:   10, 91, 829, 7552, 68797, 626725, 5709322, 52010623
ratio of consecutive terms → 9.1098;  ratio at width step 2 → 82.9880
```

So the ridge strips of height 10 at even widths and Ramanujan's `a_n`, `b_n`, `c_n` share the characteristic factor `x^2 − 83x + 1` and the growth constant `δ_9^2`.

## 1729 as a castle

A castle is a skyline with every column at least 1 and some column at the ceiling ([[castle-polyomino](pages/castle-polyomino.md)]). Reading the digits of 1729 in base `b` as column heights gives a castle exactly when no digit is 0. In bases 2 to 20 this happens in bases 9, 10, 11, 14, 15, 16, 17, 18 and 20; the base-12 palindrome `1001` has zeros.[^exec]

| base | digit castle | `h` | blocks | area | even number of blocks? |
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

The base-10 castle `(1, 7, 2, 9)` has width 4, height 9, 14 blocks and area 19, the digit sum, which divides 1729 since 1729 is a Harshad number.

```
   #        row 9
   #        row 8
 # #        row 7
 # #        row 6
 # #        row 5
 # #        row 4
 # #        row 3
 ###        row 2
####        row 1      the skyline (1, 7, 2, 9): 14 blocks, area 19
```

Its castle graph ([[castle-graph](pages/castle-graph.md)]) has 19 cells and 20 edges, so cycle rank 2, with two filled `2 × 2` squares, in rows 1-2 across columns 2-3 and 3-4. The two largest adjacency eigenvalues are `λ_1 = 2.5982` and `λ_2 = 1.8981`, and the spectral radius of the universal covering tree is `ρ(T) = 2.5756` by the edge-cavity method of [[ramanujan-castles](pages/ramanujan-castles.md)], so `λ_2 ≤ ρ(T)` and the digit castle is Ramanujan in the spectral sense.[^exec] That page's census finds every castle with at most 14 cells Ramanujan and the first failures at 15 cells, so at 19 cells the property is not automatic. The characteristic polynomial is `x (x^18 − 20x^16 + 160x^14 − 670x^12 + 1600x^10 − 2215x^8 + 1723x^6 − 691x^4 + 119x^2 − 5)`, and the factor of degree 18 is irreducible over the rationals.

**Its skyline spectrum.** The discrete Fourier transform (DFT) of the column heights, `ĉ_k = Σ_{j=1}^{4} c_j e^{−2πijk/4}`, is `(19, 2 + i, 13, 2 − i)` for `k = 0, 1, 2, 3`. With `y = 10`, the digit polynomial `y^3 + 7y^2 + 2y + 9` reduced modulo the factors `y − 1`, `y + 1` and `y^2 + 1` of `y^4 − 1` gives the residues of 1729 modulo the factors `9`, `11` and `101` of `10^4 − 1`, and these are the bins:

- bin 0 is the digit sum 19, and `1729 ≡ 19 ≡ 1 (mod 9)`;
- bin 2 is the alternating digit sum 13, and `1729 ≡ 13 ≡ 2 (mod 11)`;
- bins 1 and 3, `2 ± i`, give the test for 101 (alternating two-digit blocks, `29 − 17 = 12`), and `1729 ≡ 12 (mod 101)`.

With the mean height removed, `169/179 = 94%` of the energy is in bin 2. Among the castles of area 19 (mirror images removed), the 29 whose graphs have the adjacency and Laplacian spectrum of `(1, 7, 2, 9)` all have a graph isomorphic to its graph.[^dft] [[spectral-analysis](pages/spectral-analysis.md)] works this example in full.

Two more readings of 1729 as one castle:

- **Binary.** `1729 = 11011000001_2`. Raising the columns at the 1s gives the castle `(2, 2, 1, 2, 2, 1, 1, 1, 1, 1, 2)` of width 11 and height 2, with 4 blocks: the bottom row and the three runs of 1s in row 2 ([[binary-string-bijection](pages/binary-string-bijection.md)]). Under the unrank map, castle number 1729 of the cell `(11, 2)` is `(1, 1, 2, 2, 2, 1, 1, 1, 1, 1, 2)`, with 3 blocks.
- **Rank.** Castle number 1729 is `(3, 4, 4, 1, 1, 2)` in the cell `(6, 4)`, `(5, 8, 9, 2)` in the cell `(4, 9)` and `(8, 10, 3, 10)` in the cell `(4, 10)`.

## 1729 as a modulus

Since `1729 = 7 · 13 · 19` is squarefree, `Z/1729 = Z/7 × Z/13 × Z/19` is a product of fields ([[castle-ring-spectrum](pages/castle-ring-spectrum.md)] §5), and the period of `A^e(·, h) mod 1729` is the lcm of its periods modulo 7, 13 and 19, by the Chinese remainder theorem. The periods come from the orders of the roots of the characteristic polynomials modulo each prime ([[mod-p-observatory](pages/mod-p-observatory.md)]). The minimal periods of the count sequences, computed with the dynamic program over (last height, block parity, ceiling reached) modulo each modulus:[^exec]

| `h` | period mod 7 | mod 13 | mod 19 | lcm | period mod 1729 |
|---|---|---|---|---|---|
| 2 | 24 | 12 | 72 | 72 | 72 |
| 3 | 168 | 168 | 360 | 2520 | 2520 |
| 4 | 8400 | 168 | 360 | 25200 | 25200 |

Each sequence is periodic from `w = 1`. The period `8400` at `(h, p) = (4, 7)` is `1200 · 7`, the factor 7 coming from the double root of `char_2(x) = (x − 2)(x^2 − x + 2)` modulo 7 (the discriminant of `x^2 − x + 2` is `−7`), and `A^e(·, 4) mod 1729` has period `25200 = 8400 · 3`.

The factorization `1729 = 12^3 + 1 = Φ_2(12) Φ_6(12) = 13 · 133`, with `133 = 7 · 19`, is `x^3 + 1 = (x + 1)(x^2 − x + 1)` at `x = 12`. `Φ_6(p) = p^2 − p + 1` is the order of the torus subgroup of [[castle-cryptography-round-three](pages/castle-cryptography-round-three.md)], where `p` is chosen so that it has a large prime factor; at `p = 12` it is `7 · 19`.

## Appearances in Sources

- [[oeis-mining-pe502](pages/oeis-mining-pe502.md)] - the row `A^e(w, 4) = 1, 7, 31, 117, 439, 1729, …` of the mining tables, where 1729 is a castle count.
- [[project-euler-502-solution](pages/project-euler-502-solution.md)] - the tower count `T(k, L) = (k+1)^L`, which makes `T(k, 3)` a cube.

## Related Concepts

- [[sum-of-three-cubes-castles](pages/sum-of-three-cubes-castles.md)] - which castle counts are sums of three cubes; [[sums-of-three-cubes](pages/sums-of-three-cubes.md)] is the number theory.
- [[ramanujan-castles](pages/ramanujan-castles.md)] - the spectral Ramanujan property of castle graphs and the edge-cavity computation of `ρ(T)`.
- [[metallic-means](pages/metallic-means.md)] - the metallic means `δ_a = (a + √(a^2 + 4))/2`; Ramanujan's near-miss growth constant is `δ_9^2`.
- [[ridge-castle](pages/ridge-castle.md)] and [[metallic-strip-realizability](pages/metallic-strip-realizability.md)] - the ridge matrix `R_h = J − D` with Perron root `δ_{h−1}`.
- [[eigenvalue-continued-fractions](pages/eigenvalue-continued-fractions.md)] - palindromic characteristic polynomials and the continued fractions of quadratic units of norm `−1` and `+1`.
- [[castle-eigenvalue-oeis-crosswalk](pages/castle-eigenvalue-oeis-crosswalk.md)] - continued fractions, Lucas sequences and OEIS entries of castle eigenvalues.
- [[berlekamp-massey](pages/berlekamp-massey.md)] and [[recurrence-discovery](pages/recurrence-discovery.md)] - the algorithm that recovers `1 − 82x − 82x^2 + x^3` from the terms.
- [[castle-counting-formula](pages/castle-counting-formula.md)] and [[castle-counting-function](pages/castle-counting-function.md)] - `A^e(6, 4) = (A − P(3, 6) + P(2, 6))/2 = 1729`.
- [[song-as-castle](pages/song-as-castle.md)] - the rank/unrank bijection.
- [[mod-p-observatory](pages/mod-p-observatory.md)] - the periods of castle counts modulo a prime.
- [[castle-graph](pages/castle-graph.md)] - the castle graph of the digit castle.
- [[spectral-analysis](pages/spectral-analysis.md)] - the skyline DFT, with `(1, 7, 2, 9)` as its worked example.
- [[castle-snippets](pages/castle-snippets.md)] - `all_castles`, `blocks`, `castle_graph`.
- [[castle-cryptography-round-three](pages/castle-cryptography-round-three.md)] - the torus subgroup of order `Φ_6(p)`.

## Footnotes

[^1]: https://en.wikipedia.org/wiki/1729_(number) (2026-09-19) - "It is the first nontrivial taxicab number, expressed as the sum of two cubic positive integers in two different ways"; Hardy's account: "the number seemed to me rather a dull one, and that I hoped it was not an unfavourable omen", Ramanujan: "it is a very interesting number; it is the smallest number expressible as the sum of two cubes in two different ways"; "1729 is a composite number, the first nontrivial taxicab number, a Carmichael number, and a centered cube number"; "It is palindromic in bases 12, 32, and 36"; "noted by French mathematician Frenicle de Bessy in 1657".
[^2]: https://oeis.org/A001235 (2026-09-19) - "Taxi-cab numbers: sums of 2 cubes in more than 1 way", data `1729, 4104, 13832, 20683, 32832, 39312, 40033, 46683, 64232, 65728, 110656, 110808, 134379, 149389, 165464`; https://en.wikipedia.org/wiki/Taxicab_number (2026-09-19) - "1729 = Ta(2) = 1^3 + 12^3 = 9^3 + 10^3, also known as the Hardy-Ramanujan number"; the two pairs "were first mentioned by Bernard Frenicle de Bessy, who published his observation in 1657".
[^3]: https://oeis.org/A050794 (2026-09-19) - Diophantine equation `x^3 + y^3 = z^3 + 1` with `1 < x < y < z`, "Fermat near misses", data `1729, 1092728, 3375001, 15438250, 121287376, 401947273, …`; comment (Omar E. Pol, 2009) "a(1)=1729 is the Hardy-Ramanujan number".
[^4]: https://oeis.org/A002997 (2026-09-19) - "Carmichael numbers", data `561, 1105, 1729, 2465, 2821, 6601, 8911, 10585, 15841, 29341, …`; definition "composite numbers k such that a^(k-1) == 1 (mod k) for every a coprime to k"; Korselt (1899): an odd composite `k` is Carmichael if and only if it is squarefree and `p − 1 | k − 1` for every prime `p | k`.
[^5]: https://arxiv.org/abs/1510.00735 (2026-09-19) - Ken Ono and Sarah Trebat-Leder, "The 1729 K3 Surface", Research in Number Theory (2016), abstract [synthesis]: revisiting Ramanujan's writings around 1729 and Euler's `a^3 + b^3 = c^3 + d^3`, they find that Ramanujan "discovered a K3 surface with Picard number 18" yielding "infinitely many cubic twists over Q with rank >= 2".
[^6]: raw/oeis-pe502/terms_50.txt §"F(w,4)" L10-12 - "## F(w,4)  [even blocks, height 4, w=1..50]" followed by the data line beginning "1 7 31 117 439 1729 7063 29201 120471 493617".
[^7]: https://en.wikipedia.org/wiki/Sums_of_three_cubes (2026-09-19) - "cannot equal 4 or 5 modulo 9, because the cubes modulo 9 are 0, 1, and -1"; Mahler 1936: "(9b^4)^3 + (3b - 9b^4)^3 + (1 - 9b^3)^3 = 1"; the primitive-solution table lists `(9, 10, -12)` for `n = 1`; "in 2019, Andrew Booker settled the case n = 33"; "in September 2019, Booker and Andrew Sutherland finally settled the n = 42 case".
[^8]: https://mathworld.wolfram.com/RamanujansSumIdentity.html (2026-09-19) - the three generating functions with denominator `1 - 82x - 82x^2 + x^3`, the identity `a_n^3 + b_n^3 = c_n^3 + (-1)^n`, Hirschhorn's closed forms with `alpha, beta = (83 +- 9 sqrt 85)/2` and denominators 85, and "the first seven cases n=0 to 6 is sufficient to prove the result" (Hirschhorn 1996); references M. D. Hirschhorn, "An Amazing Identity of Ramanujan", Math. Mag. 68 (1995) 199-201, and "A Proof in the Spirit of Zeilberger of an Amazing Identity of Ramanujan", Math. Mag. 69 (1996) 267-269. https://oeis.org/A051028 (2026-09-19) - "Ramanujan's a-series: expansion of (1+53x+9x^2)/(1-82x-82x^2+x^3)", g.f. "(1+53*x+9*x^2)/((1+x)*(1-83*x+x^2))", recurrence signature `(82, 82, -1)`, comment (Emeric Deutsch, 2006) "The 'amazing' identity of Ramanujan is a(n)^3 + b(n)^3 = c(n)^3 + (-1)^n" with `b, c` = A051029, A051030.
[^9]: https://oeis.org/A005917 (2026-09-19) - "Rhombic dodecahedral numbers: a(n) = n^4 - (n - 1)^4", data `1, 15, 65, 175, 369, 671, 1105, 1695, 2465, 3439, 4641, 6095`; formula "a(n) = (2*n - 1)*(2*n^2 - 2*n + 1)".
[^exec]: Verified by execution (Python 3.11 with SymPy, NumPy and NetworkX, 2026-09-19, recomputed 2026-10-16): the factorization of 1729, the Carmichael condition for all `a` coprime to 1729 and Korselt's criterion, the first 33 Carmichael numbers by Korselt's criterion (the 33rd is 512461), base expansions, the representations of 1729 as a sum of three cubes with `|x|, |y|, |z| ≤ 300`, Mahler's identity by symbolic expansion, the three Ramanujan series from their generating functions with the identity for `n = 0, …, 5` and the recurrence run back to `n = −4`, the factorization and partial fractions of the denominator, Hirschhorn's closed form for `a_0, …, a_3`, Berlekamp-Massey over the rationals on `c_0, …, c_5` and on `c_0, …, c_11`, the Lucas sequences and the continued fractions of `δ_9^2` and `1729^{1/3}`, `charpoly(R_10)`, `charpoly(R_10^2)` and the ridge strip counts; the cell `(6, 4)` by enumeration of all skylines, `P(2, 6)` and `P(3, 6)` as signed sums over `{0, …, k}^6`, the signed counts `S(w, h)` for `h ≤ 6`, `w ≤ 10`, the sweep of `w, h ≤ 40` with `A ≤ 10^9` for 1729 and for the Carmichael, taxicab and near-miss lists, the digit castles in bases 2 to 20, the unrank map of song-as-castle and the even-block castles of `(6, 4)` in rank order, the castle graph of `(1, 7, 2, 9)` with its spectrum, characteristic polynomial (the degree-18 factor irreducible) and `ρ(T)` by the edge-cavity bisection, the DFT bins and residues, and the minimal periods of `A^e(·, h)` modulo 7, 13, 19 and 1729 for `h = 2, 3, 4` from the dynamic program.
[^dft]: Verified by execution (2026-09-30), Python 3 with NumPy, SymPy and networkx: the four bins with column index `j = 1, …, 4`, the residues of 1729 mod 9, 11 and 101 against the digit polynomial reduced mod `y − 1`, `y + 1` and `y^2 + 1`, the energy share with the mean removed, and every composition of 19 (mirror images removed) compared with `(1, 7, 2, 9)` by adjacency and Laplacian eigenvalues, where all 28 other matches are isomorphic to it by networkx.
