---
title: Hilbert castles
category: Concepts
summary: A Hilbert castle is a castle in which no two neighboring columns differ in height by exactly 1, under the Hilbert rule J − A_path, which allows exactly the neighbor pairs that the zig-zag rule forbids. Hilbert duality - for every strip rule M, the strip series G_M(x), counted by width with the empty strip included, satisfies G_M(x) G_{J−M}(−x) = 1 - is proved by inclusion-exclusion; it is Gessel's form of the Carlitz-Scoville-Vaughan theorem, and in Loday and Vallette's terms G_M is the Hilbert series of a quadratic monomial algebra and G_{J−M} that of its Koszul dual. So the Hilbert strips have series 1/Z_h(−x), with Z_h the zig-zag strip series, and are David Nacin's OEIS entries A287804 to A287832 at h = 5 to 11, A126358 at h = 4. The Hilbert castles number 2^w − 1 at height 3, all with an odd number of blocks, and 2F_{2w+1} − 2^w − 1 at height 4. The path on four heights is its own complement, so at h = 4 a relabeling turns the 1-smooth rule into the Hilbert rule, and the Hilbert castles of height 4 grow at φ² by width. The duality also pairs the m-disparate rule with the (m − 1)-smooth rule and gives the tree skylines by width and area.
tags: [concept, castle, hilbert-castle, strip-rule, transfer-matrix, hilbert-series, koszul-duality, monomial-algebra, carlitz-scoville-vaughan, inclusion-exclusion, zig-zag-castle, m-disparate, tree-castle, block-count, parity, oeis, verification]
sources: [loday-vallette-2012-algebraic-operads, gessel-2013-carlitz-scoville-vaughan, knopfmacher-mansour-munagi-prodinger-2008-smooth-words, project-euler-502-brute-force]
created: 2026-10-28
updated: 2026-10-28
---

# Hilbert castles

## Definition

A castle of width `w` and height `h` is a skyline `(c_1, …, c_w)` with `1 ≤ c_i ≤ h` and some `c_i = h` ([[castle-polyomino](pages/castle-polyomino.md)]). The **Hilbert rule** lets a column of height `a` stand next to a column of height `b` when `|a − b| ≠ 1`. A **Hilbert castle** is a castle whose neighboring columns all obey the Hilbert rule: no column is exactly one higher or one lower than the column before it. `A_hilbert(w, h)` is the number of Hilbert castles of width `w` and height `h`, and `A^e_hilbert(w, h)` and `A^o_hilbert(w, h)` count those with an even and with an odd number of blocks ([[castle-notation](pages/castle-notation.md)]).

The Hilbert rule allows exactly the neighbor pairs that the zig-zag rule `|a − b| = 1` of [[zig-zag-castles](pages/zig-zag-castles.md)] forbids. The name is for the Hilbert series of section *The Hilbert-series reading*, through which a rule and the rule of its forbidden pairs determine each other's strips.

*Example.* The skyline `(1, 3, 3, 1, 4)` is a Hilbert castle of width 5 and height 4: its neighboring heights differ by 2, 0, 2 and 3.

```
(1, 3, 3, 1, 4)

  . . . . #
  . # # . #
  . # # . #
  # # # # #
```

The Hilbert castles of width 2 and height 4 are the five skylines

```
(1, 4)   (2, 4)   (4, 1)   (4, 2)   (4, 4)

 . #      . #      # .      # .      # #
 . #      . #      # .      # .      # #
 . #      # #      # .      # #      # #
 # #      # #      # #      # #      # #
```

The skylines `(3, 4)` and `(1, 2, 4)` are not Hilbert castles, since in each the first two heights differ by 1.[^exec2]

## The strip series of a rule

A strip rule on the heights `1, …, h` is an `h × h` matrix `M` of 0s and 1s, with a 1 in row `a` and column `b` when a column of height `a` may stand to the left of a column of height `b`, and a strip of width `w` under `M` is a skyline in `{1, …, h}^w` whose neighboring columns all obey `M` ([[castle-strip](pages/castle-strip.md)]). Let `N_M(w)` be the number of strips of width `w`, with `N_M(0) = 1` for the empty strip, and let

```
G_M(x)  =  Σ_{w≥0} N_M(w) x^w  =  1 + x 𝟙ᵀ (I − xM)^{−1} 𝟙
```

be the **strip series** of `M`, with `I` the identity matrix and `𝟙` the all-ones vector of length `h`; the second form is Equation (3) of [[castle-strip](pages/castle-strip.md)] with the empty strip added. The **dual rule** of `M` is `J − M`, with `J` the all-ones matrix: it allows exactly the pairs that `M` forbids. The dual of `J − M` is `M` again.

The Hilbert rule is the dual of the zig-zag rule. The zig-zag rule is the adjacency matrix `A_path` of the path on the heights, with a 1 where `|a − b| = 1`, so the Hilbert rule is `J − A_path`. At `h = 4`:

```
  zig-zag rule A_path       Hilbert rule J − A_path

  [0 1 0 0]                 [1 0 1 1]
  [1 0 1 0]                 [0 1 0 1]
  [0 1 0 1]                 [1 0 1 0]
  [0 0 1 0]                 [1 1 0 1]
```

## Hilbert duality

**Theorem (Hilbert duality).** For every rule `M` on the heights `1, …, h`,

```
G_M(x) · G_{J−M}(−x)  =  1.                                                    (1)
```

*Proof.* Fix `w ≥ 1`. In a skyline `c ∈ {1, …, h}^w`, call the position `i` between the columns `i` and `i + 1` **forbidden** when `M` forbids the pair `(c_i, c_{i+1})`. The skyline is a strip of `M` exactly when it has no forbidden position, so by inclusion-exclusion `N_M(w)` is the sum of `(−1)^{|S|}` over the pairs `(c, S)` in which `S` is a set of forbidden positions of `c`. Cutting `c` at the positions outside `S` splits it into `r ≥ 1` pieces of widths `k_1 + ⋯ + k_r = w`. Every neighbor pair inside a piece sits at a position of `S`, so `M` forbids it and `J − M` allows it: each piece is a strip of `J − M`. Conversely, strips of `J − M` of widths `k_1, …, k_r` placed side by side give one such pair, with `S` the positions inside the pieces, so `|S| = w − r` and

```
N_M(w)  =  Σ_{k_1 + ⋯ + k_r = w}  (−1)^{w−r}  N_{J−M}(k_1) ⋯ N_{J−M}(k_r).
```

With `Q(x) = Σ_{k≥1} (−1)^{k−1} N_{J−M}(k) x^k`, the right side is the coefficient of `x^w` in `Σ_{r≥0} Q(x)^r = 1/(1 − Q(x))`, and so is `N_M(0) = 1` at `w = 0`. Since `1 − Q(x) = G_{J−M}(−x)`, this is Equation (1). ∎

The proof keeps every column, so Equation (1) also holds with a column of height `a` weighted by its own variable `x_a` in place of `x`. In that form, with the heights as the letters of an alphabet and `M` as a relation `R` on it, Equation (1) is the Carlitz-Scoville-Vaughan theorem as Ira M. Gessel states it, with the letters commuting; Gessel states it in noncommuting variables, which the same proof gives. His second proof is the same inclusion-exclusion, over the positions of a word whose pair is not in `R`.[^csv] With `x_a = q^a x` the weighted form counts strips by width and area. Equation (1) was checked by execution on every rule of height at most 4, on 300 random rules at each of the heights 5, 6 and 7, and in the weighted form by width and area on every rule of height at most 3.[^exec1]

*Example: every pair and no pair.* The rule `J` allows every pair, so its strips are all `h^w` skylines and `G_J(x) = 1/(1 − hx)`. Its dual `0` allows no pair, so its strips are the empty strip and the `h` single columns, and `G_0(x) = 1 + hx`. Then `G_J(x) G_0(−x) = (1 − hx)/(1 − hx) = 1`.

*Example: plateau-free and constant.* The plateau-free rule `J − I` has `h(h − 1)^{w−1}` strips of width `w ≥ 1`, so `G_{J−I}(x) = (1 + x)/(1 − (h − 1)x)`. Its dual `I` allows only equal neighbors, with the `h` constant strips of each width `w ≥ 1`, so `G_I(x) = 1 + hx/(1 − x)`, and `1 − hx/(1 + x) = (1 − (h − 1)x)/(1 + x)` is the reciprocal of `G_{J−I}(x)`.[^exec1]

## The Hilbert-series reading

Let `K` be a field and `v_1, …, v_h` noncommuting variables, one for each height. The **monomial algebra** of a rule `M` is the quotient of the free associative algebra `K⟨v_1, …, v_h⟩` by the two-sided ideal generated by the products `v_a v_b` of the pairs `(a, b)` that `M` forbids. Loday and Vallette call such a quotient a quadratic monomial algebra and write `L̄(2)` for the pairs whose products are relations and `L(2)` for the others; here `L(2)` is the set of pairs that `M` allows. Their Proposition 4.3.4 states that the words `v_{c_1} ⋯ v_{c_w}` whose neighboring pairs all lie in `L(2)` form a basis of the algebra.[^lv-monomial] These words are the strips of `M`, so the part of degree `w` has dimension `N_M(w)` and `G_M(x)` is the algebra's Hilbert series, which Loday and Vallette call its generating series or Hilbert-Poincaré series `f^A(x)`.[^lv-series]

The Koszul dual algebra `A^!` of a quadratic algebra `A` has the dual generators `v*_a` and the orthogonal space of relations (their Proposition 3.2.3).[^lv-dual] For a monomial algebra, Proposition 4.3.5 of Loday and Vallette identifies it as the monomial algebra with relations `v*_a v*_b` for the pairs in `L(2)`, with basis the words whose neighboring pairs all lie in `L̄(2)`: the monomial algebra of `J − M`.[^lv-monomial] Their Theorem 4.3.6 states that every quadratic monomial algebra is Koszul, and their Theorem 3.5.1 that a Koszul algebra and its dual satisfy `f^A(x) f^{A^!}(−x) = 1`.[^lv-koszul][^lv-series] With `A` the monomial algebra of `M`, this is Equation (1). The pair `J`, `0` of the first example is their example of the identity: the tensor algebra `T(V)` on a space of dimension `k`, with series `1/(1 − kx)`, against `K ⊕ V`, with series `1 + kx`.[^lv-series] Vic Reiner's talk *Koszul algebras in combinatorics* states the same case for the algebra of walks in a directed graph, whose Koszul dual is the algebra of the complementary directed graph.[^reiner]

The proof of Theorem 4.3.6 is a pairing. In the Koszul complex a basis element is a pair `(u, v)`, `u` a strip of `J − M` and `v` a strip of `M`, and the boundary moves the last column of `u` to the front of `v` when `M` allows the pair of columns at the cut.[^lv-koszul] For a fixed skyline `c = uv` of width `w ≥ 1`, the cuts of `c` into a strip of `J − M` followed by a strip of `M` are either none or two neighboring cuts, which have opposite signs `(−1)^{width of u}`. So the coefficient of `x^w` in `G_{J−M}(−x) G_M(x)` vanishes. Gessel's first proof is the same cancellation.[^csv][^exec1]

## Hilbert strips and Hilbert castles

A **Hilbert strip** of width `w` on the heights `1, …, h` is a skyline in `{1, …, h}^w` whose neighboring columns obey the Hilbert rule. A Hilbert strip need not reach `h`, so it need not be a castle of height `h`; the Hilbert strips that reach `h` are the Hilbert castles of height `h`. Write `hstrips(w, h)` for their number, with `hstrips(0, h) = 1`, so that

```
A_hilbert(w, h)  =  hstrips(w, h) − hstrips(w, h − 1)    (w ≥ 1).               (2)
```

Write `Z_h(x) = Σ_{w≥0} zstrips(w, h) x^w` for the strip series of the zig-zag rule, with `zstrips(0, h) = 1` and `zstrips(w, h)` the zig-zag strip count of [[zig-zag-castles](pages/zig-zag-castles.md)]. Equation (1) with `M = A_path` gives

```
Σ_{w≥0} hstrips(w, h) x^w  =  1 / Z_h(−x).                                    (3)
```

The numerator of one series is the denominator of the other at `−x`:[^exec3]

| `h` | `Z_h(x)` | `Σ_w hstrips(w, h) x^w = 1/Z_h(−x)` | OEIS |
|---|---|---|---|
| 2 | `(1 + x)/(1 − x)` | `(1 + x)/(1 − x)` | |
| 3 | `(1 + x)(1 + 2x)/(1 − 2x²)` | `(1 − 2x²)/((1 − x)(1 − 2x))` | A083318 |
| 4 | `(1 + 3x + x²)/(1 − x − x²)` | `(1 + x − x²)/(1 − 3x + x²)` | A126358 |
| 5 | `(1 + 5x + 5x² − x³)/(1 − 3x²)` | `(1 − 3x²)/(1 − 5x + 5x² + x³)` | A287804 |
| 6 | `(1 + 5x + 2x² − 3x³)/(1 − x − 2x² + x³)` | `(1 + x − 2x² − x³)/(1 − 5x + 2x² + 3x³)` | A287806 |

At `h = 2` the zig-zag rule is the plateau-free rule `J − I` and the Hilbert rule is `I`, so both series are `(1 + x)/(1 − x)`.

The OEIS counts the Hilbert strips as sequences over `h` digits in which no two consecutive terms have distance 1, with the empty sequence at `n = 0`; the heights `1, …, h` are the digits `0, …, h − 1`. David Nacin's entries are A287804, A287806, A287808, A287812, A287816, A287825 and A287832 at `h = 5, …, 11`, named for instance "Number of quinary sequences of length n such that no two consecutive terms have distance 1."; at `h = 4` the count is A126358, with Nacin's comment "a(n) is the number of quaternary sequences of length n such that no two adjacent terms differ by exactly 1."; at `h = 3` it is A083318, "a(0) = 1; for n>0, a(n) = 2^n + 1.".[^nacin] Every entry agrees with `hstrips(n, h)` on every term of its data field.[^exec3]

The Hilbert castles, by Equation (2):[^exec3]

| `h` | `A_hilbert(w, h)`, `w = 1, …, 12` |
|---|---|
| 2 | `1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1` |
| 3 | `1, 3, 7, 15, 31, 63, 127, 255, 511, 1023, 2047, 4095` |
| 4 | `1, 5, 17, 51, 145, 401, 1091, 2937, 7849, 20867, 55265, 145953` |
| 5 | `1, 7, 33, 137, 535, 2015, 7415, 26863, 96267, 342333, 1210609, 4263811` |
| 6 | `1, 9, 55, 295, 1481, 7147, 33617, 155365, 709093, 3206785, 14403417, 64359653` |
| 7 | `1, 11, 83, 549, 3393, 20129, 116239, 658731, 3682401, 20376223, 111876335, 610570527` |

Every entry agrees with brute-force enumeration wherever `h^w ≤ 3·10^6`.

**Heights 2, 3 and 4.**

- At `h = 2` the Hilbert rule is `I`, so the only Hilbert castle of width `w` and height 2 is the skyline `(2, …, 2)`.
- At `h = 3` the Hilbert rule lets a column of height 2 stand only next to another of height 2, and lets the heights 1 and 3 follow each other freely. So a Hilbert strip on three heights is the skyline `(2, …, 2)` or a skyline in `{1, 3}^w`, and the Hilbert castles of height 3 are the skylines in `{1, 3}^w` other than `(1, …, 1)`: `A_hilbert(w, 3) = 2^w − 1`, A000225(`w`).
- At `h = 4`, Equation (3) gives `(1 + x − x²)/(1 − 3x + x²) = 2(1 − x)/(1 − 3x + x²) − 1`, and `(1 − x)/(1 − 3x + x²) = Σ_{w≥0} F_{2w+1} x^w`, with `F_n` the Fibonacci numbers. So `hstrips(w, 4) = 2F_{2w+1}` for `w ≥ 1`, as A126358 records,[^nacin] and subtracting the `2^w + 1` Hilbert strips on three heights,

```
A_hilbert(w, 4)  =  2F_{2w+1} − 2^w − 1,                                        (4)
```

for example `2 · 13 − 8 − 1 = 17` at `w = 3`.[^exec3]

## Height 4: the path is its own complement

On the heights `1, 2, 3, 4`, the zig-zag rule `A_path` joins `1 − 2 − 3 − 4`, and the 2-disparate rule `|a − b| ≥ 2` of [[castle-classification-shape](pages/castle-classification-shape.md)] joins `3 − 1 − 4 − 2`, the complement of the path: both are paths on four vertices. Relabeling the heights by `1 ↦ 3`, `2 ↦ 1`, `3 ↦ 4`, `4 ↦ 2` maps the first path onto the second. With a loop at every height added, it maps the 1-smooth rule `I + A_path` onto the Hilbert rule `J − A_path`.[^exec4] So at height 4 the four rules form two dual pairs, and the relabeling matches them across:

| rule on 4 heights | matrix | dual rule | strips of width `w ≥ 1` |
|---|---|---|---|
| 1-smooth | `I + A_path` | 2-disparate | `2F_{2w+1}` |
| Hilbert | `J − A_path` | zig-zag | `2F_{2w+1}` |
| zig-zag | `A_path` | Hilbert | `2F_{w+2}` |
| 2-disparate | `J − I − A_path` | 1-smooth | `2F_{w+2}` |

The relabeled rules have the same strip counts: the name of A126358, "Number of base 4 n-digit numbers with adjacent digits differing by one or less", counts the free 1-smooth strips on four heights, and Nacin's comment on it counts the Hilbert strips.[^nacin] The free 1-smooth strips on four heights are the smooth words of [[knopfmacher-mansour-munagi-prodinger-2008-smooth-words](pages/knopfmacher-mansour-munagi-prodinger-2008-smooth-words.md)], whose generating function at `k = 4` is the series `(1 + x − x²)/(1 − 3x + x²)` of the table above.[^kmmp] Castles do not correspond, since the relabeling sends the height 3 to the height 4: it maps the free 1-smooth strips on four heights that use the height 3 onto the Hilbert castles of height 4.[^exec4]

The relabeled matrices are similar, so `I + A_path` and `J − A_path` on four heights both have the characteristic polynomial `(x² − 3x + 1)(x² − x − 1)` and the largest eigenvalue `1 + 2cos(π/5) = 1 + φ = φ²`, with `φ = (1 + √5)/2`. No other height above 1 has this property: the path on `h` heights has `h − 1` edges and its complement has `(h − 1)(h − 2)/2`, which are equal only at `h = 1` and `h = 4`.[^exec4]

## Growth

The Hilbert strips on the heights `1, …, h` grow by width at the largest eigenvalue `ρ(J − A_path)` of the Hilbert rule, by Equation (2) of [[castle-strip](pages/castle-strip.md)]. The Hilbert rule on `h − 1` heights has a smaller largest eigenvalue, as the table shows, so the Hilbert castles of height `h`, the difference in Equation (2), grow at `ρ(J − A_path)` by width too:[^exec5]

| `h` | `ρ(J − A_path)` | minimal polynomial |
|---|---|---|
| 2 | `1` | `x − 1` |
| 3 | `2` | `x − 2` |
| 4 | `φ² = 2.61803…` | `x² − 3x + 1` |
| 5 | `3.48119…` | `x³ − 5x² + 5x + 1` |
| 6 | `4.38848…` | `x³ − 5x² + 2x + 3` |
| 7 | `5.32619…` | `x⁴ − 7x³ + 8x² + 6x − 6` |
| 8 | `6.28099…` | `x⁴ − 7x³ + 3x² + 10x − 3` |
| 9 | `7.24673…` | `x⁵ − 9x⁴ + 11x³ + 15x² − 19x − 1` |
| 10 | `8.21986…` | `x⁵ − 9x⁴ + 4x³ + 21x² − 9x − 5` |

The Hilbert castles of height 3 are copper by width, `σ_1^2 = 2` ([[metallic-means](pages/metallic-means.md)]), and those of height 4 grow at `φ²`, the growth of the 1-smooth castles of height 4 with first column at height 1 ([[1-smooth-castles](pages/1-smooth-castles.md)]).

**Bounds.** For `h ≥ 2`,

```
h − 2 + 2/h  ≤  ρ(J − A_path)  ≤  h − 1.
```

The upper bound is the largest row sum: the rows of the heights 1 and `h` have `h − 1` ones, the others `h − 2`. The lower bound is the Rayleigh quotient of `𝟙`, since the matrix has `h² − 2(h − 1)` ones.[^exec5]

**The symmetric part.** The flip `a ↦ h + 1 − a` of the heights commutes with `J − A_path`, so the matrix maps the vectors that are symmetric under the flip to symmetric vectors, and the antisymmetric ones to antisymmetric ones. `J` sends every antisymmetric vector to 0, so on the antisymmetric vectors `J − A_path` acts as `−A_path`, with the eigenvalues `−2cos θ_k` for the even `k = 2, 4, …`, `θ_k = πk/(h + 1)`, of [[zig-zag-castles](pages/zig-zag-castles.md)]. The symmetric vectors have dimension `⌈h/2⌉` and contain `𝟙`, so `hstrips(w, h) = 𝟙ᵀ(J − A_path)^{w−1}𝟙` involves only the symmetric part, and the reduced denominator of Equation (3) has degree at most `⌈h/2⌉`. The growth `ρ(J − A_path)` of `hstrips(w, h)` is then at most the largest modulus of an eigenvalue of the symmetric part, and so equal to it. In the basis `e_a + e_{h+1−a}`, with `e_a` the unit vector of the height `a`, the symmetric part is a nonnegative matrix, so by the Perron-Frobenius theorem `ρ(J − A_path)` is one of its eigenvalues and has degree at most `⌈h/2⌉`, as the table shows.[^exec5]

## Blocks

The block count of a castle is `blocks(c) = c_1 + Σ_{i=2}^{w} max(0, c_i − c_{i−1})`.[^blocks] The castle `(1, 3, 3, 1, 4)` of the example has `1 + 2 + 3 = 6` blocks, and each of the five Hilbert castles of width 2 and height 4 has 4.

At height 3 every rise of a Hilbert castle goes from 1 to 3, so every rise is 2 and `blocks(c) ≡ c_1 (mod 2)`. Since `c_1` is 1 or 3, **every Hilbert castle of height 3 has an odd number of blocks**: `A^e_hilbert(w, 3) = 0` and `A^o_hilbert(w, 3) = 2^w − 1`. At height 2 the castle `(2, …, 2)` has 2 blocks. The even-block and odd-block counts for `w = 1, …, 10`:[^exec6]

| `h` | `A^e_hilbert(w, h)` | `A^o_hilbert(w, h)` |
|---|---|---|
| 4 | `1, 5, 16, 44, 114, 288, 721, 1805, 4542, 11516` | `0, 0, 1, 7, 31, 113, 370, 1132, 3307, 9351` |
| 5 | `0, 0, 3, 27, 151, 693, 2870, 11202, 42163, 155049` | `1, 7, 30, 110, 384, 1322, 4545, 15661, 54104, 187284` |
| 6 | `1, 9, 49, 225, 981, 4249, 18562, 81920, 364073, 1623179` | `0, 0, 6, 70, 500, 2898, 15055, 73445, 345020, 1583606` |
| 7 | `0, 0, 10, 142, 1222, 8504, 53187, 313931, 1792490, 10031562` | `1, 11, 73, 407, 2171, 11625, 63052, 344800, 1889911, 10344661` |

Every entry agrees with brute-force enumeration wherever `h^w ≤ 2·10^6`. The block count is a weight on neighbor pairs, not on single columns, so Equation (1) does not carry it.

## Other dual pairs

Equation (1) pairs every rule with its dual. The pairs on the wiki:[^exec1][^exec7][^exec8]

| rule `M` | its strips | dual rule `J − M` | its strips |
|---|---|---|---|
| every pair, `J` | all skylines, `1/(1 − hx)` | no pair, `0` | single columns, `1 + hx` |
| plateau-free, `J − I` | `(1 + x)/(1 − (h − 1)x)` | constant, `I` | `1 + hx/(1 − x)` |
| zig-zag, `A_path` | `Z_h(x)` | Hilbert, `J − A_path` | `1/Z_h(−x)` |
| `(m − 1)`-smooth, `\|a − b\| ≤ m − 1` | the free `(m − 1)`-smooth strips | m-disparate, `\|a − b\| ≥ m` | the m-disparate strips |
| tree, `a = 1` or `b = 1` | the tree skylines | both at least 2 | single columns, and `{2, …, h}^w` for `w ≥ 2` |

**The m-disparate castles.** The `(m − 1)`-smooth rule forbids exactly the pairs with `|a − b| ≥ m`, so its dual is the m-disparate rule of [[castle-classification-shape](pages/castle-classification-shape.md)], and the m-disparate strips have the series `1/G(−x)`, with `G` the strip series of the free `(m − 1)`-smooth rule ([[m-smooth-castles](pages/m-smooth-castles.md)]). At `m = 1` this is the plateau-free row. At `m = 2` the free 1-smooth strips are the smooth words of [[knopfmacher-mansour-munagi-prodinger-2008-smooth-words](pages/knopfmacher-mansour-munagi-prodinger-2008-smooth-words.md)], whose Theorem 2.2 writes their series `sw_h(x)` with Chebyshev polynomials, so the 2-disparate strips on `h` heights have the series `1/sw_h(−x)`.[^kmmp][^exec7] The 2-disparate rule is `J − I − A_path`, the Hilbert rule with its diagonal removed, so its eigenvalues are those of the Hilbert rule minus 1, and the 2-disparate castles of height `h` grow at `ρ(J − A_path) − 1` by width: golden at `h = 4`. The m-disparate counts, and the m-disparate castles of height `m + 2`, which number `2(F_{w+2} − 1)` for `w ≥ 2` at every `m ≥ 2`, are in the paragraph *m-disparate castles* of [[castle-classification-shape](pages/castle-classification-shape.md)].[^exec7]

**Tree skylines.** The tree skylines of [[castle-graph](pages/castle-graph.md)], with no two neighboring columns both of height at least 2, are the strips of the rule that allows a pair when one of its columns has height 1. The dual rule allows a pair when both columns have height at least 2, so its strips are the empty strip, the `h` single columns, and for `w ≥ 2` the `(h − 1)^w` skylines in `{2, …, h}^w`. With a column of height `a` weighted by `q^a x` and `P_h(q) = q² + q³ + ⋯ + q^h`, their series is `1 + qx + P_h(q)x/(1 − P_h(q)x)`, and the weighted form of Equation (1) gives the tree skylines by width and area,

```
Σ_{tree skylines c} q^{c_1 + ⋯ + c_w} x^w  =  (1 + P_h(q)x) / (1 − qx − qP_h(q)x²),
```

the generating function of [[castle-graph](pages/castle-graph.md)] and [[tree-castle-by-area](pages/tree-castle-by-area.md)]. At `q = 1` it is `(1 + (h − 1)x)/(1 − x − (h − 1)x²)`, whose denominator is the recurrence `T_h(w + 2) = T_h(w + 1) + (h − 1)T_h(w)` of [[castle-graph](pages/castle-graph.md)].[^exec8]

## Related Concepts

- [[zig-zag-castles](pages/zig-zag-castles.md)] - the zig-zag rule `A_path`, the dual of the Hilbert rule; its strip series `Z_h(x)` gives the Hilbert strips through Equation (3).
- [[castle-strip](pages/castle-strip.md)] - strip rules as 0/1 matrices, the strip count `𝟙ᵀ M^{w−1} 𝟙`, its generating function and the Perron root; the dual rule `J − M`.
- [[loday-vallette-2012-algebraic-operads](pages/loday-vallette-2012-algebraic-operads.md)] - quadratic monomial algebras, their Koszul duals, and the generating-series identity behind Equation (1).
- [[gessel-2013-carlitz-scoville-vaughan](pages/gessel-2013-carlitz-scoville-vaughan.md)] - the Carlitz-Scoville-Vaughan theorem, Equation (1) for words, with three proofs.
- [[castle-classification-shape](pages/castle-classification-shape.md)] - the Hilbert type among the rate-of-change types, and the m-disparate castles, the duals of the `(m − 1)`-smooth castles.
- [[m-smooth-castles](pages/m-smooth-castles.md)], [[1-smooth-castles](pages/1-smooth-castles.md)] - the smooth rules whose duals are the disparate rules; at height 4 the 1-smooth rule is the Hilbert rule relabeled.
- [[knopfmacher-mansour-munagi-prodinger-2008-smooth-words](pages/knopfmacher-mansour-munagi-prodinger-2008-smooth-words.md)] - the free 1-smooth strips in Chebyshev polynomials, whose reciprocal at `−x` is the 2-disparate strip series.
- [[castle-graph](pages/castle-graph.md)], [[tree-castle-by-area](pages/tree-castle-by-area.md)] - the tree skylines, the dual of the strips with every column at height at least 2.
- [[castle-classification-growth](pages/castle-classification-growth.md)] - growth by width; the Hilbert castles of height 3 are copper by width and those of height 4 grow at `φ²`.
- [[castle-notation](pages/castle-notation.md)] - `G_M(x)`, `J − M`, `hstrips(w, h)` and `A_hilbert(w, h)`.

## Footnotes

[^csv]: [[gessel-2013-carlitz-scoville-vaughan](pages/gessel-2013-carlitz-scoville-vaughan.md)] slides "The Carlitz-Scoville-Vaughan Theorem" and "Proof of the CSV theorem" L42-L57, L144-L195 [synthesis] - the statement for an alphabet `A`, a relation `R ⊆ A²`, the set `A(R)` of words `a_1 ⋯ a_n` with `a_1 R a_2 R ⋯ R a_n` ("Note that the empty word 1 and all words of length one are in A(R)") and `R̄ = A² − R`: the sum of the words of `A(R̄)` is the inverse of `Σ_{w ∈ A(R)} (−1)^{l(w)} w`, "in the ring of formal power series in noncommuting variables" (the text layer drops the bars over `R̄`); Proof 1, "Every nonempty word that occurs in this sum appears twice, once with a plus sign and once with a minus sign."; Proof 2, by "inclusion-exclusion" over the `R`-descents, the positions `i` with `a_i R̄ a_{i+1}`, a word with no `R`-descent being a word of `A(R)`.
[^lv-series]: [[loday-vallette-2012-algebraic-operads](pages/loday-vallette-2012-algebraic-operads.md)] §3.5 L555-L583 [synthesis] - "By definition the generating series or Hilbert-Poincaré series of A is f^A(x) := Σ_{n≥0} dim A^(n) x^n."; Theorem 3.5.1, "If (V, R) is a finite dimensional quadratic data which is Koszul, then the following identity holds between the generating series of A and A^!: f^A(x) f^{A^!}(−x) = 1.", proved by the Euler-Poincaré characteristic of the Koszul complex in each weight; and the example `f^{T(V)}(x) = 1/(1 − kx)` and `1 + kx` for `K ⊕ V`, "which satisfy f^{K⊕V}(x) f^{T(V)}(−x) = 1", when `V` has dimension `k`.
[^lv-dual]: [[loday-vallette-2012-algebraic-operads](pages/loday-vallette-2012-algebraic-operads.md)] §3.2 Proposition 3.2.3 L185-L190 - "In other words the orthogonal space R⊥ is defined as the image of (V⊗2/R)∗ in (V∗)⊗2"; "The Koszul dual algebra A! admits the following quadratic presentation A! = A(V∗, R⊥)."
[^lv-monomial]: [[loday-vallette-2012-algebraic-operads](pages/loday-vallette-2012-algebraic-operads.md)] §4.3.3 Propositions 4.3.4 and 4.3.5 L1723-L1753 [synthesis] - a quadratic monomial algebra has relations "linearly spanned by a set {vi vj}(i,j)∈L̄(2)", with `L(2)` the complement of `L̄(2)`; the tuples with every `(i_m, i_{m+1})` in `L(2)` label a basis of the algebra, those with every pair in `L̄(2)` label a basis of the Koszul dual coalgebra, and "the Koszul dual algebra Å^! is also a monomial algebra, with presentation Å^! ≅ A(V*, R⊥), with R⊥ = ⟨v*_i v*_j, (i, j) ∈ L(2)⟩ and basis labelled by L̄."
[^lv-koszul]: [[loday-vallette-2012-algebraic-operads](pages/loday-vallette-2012-algebraic-operads.md)] §4.3.3 Theorem 4.3.6 L1760-L1769 [synthesis] - "Any quadratic monomial algebra is a Koszul algebra."; the proof writes the Koszul complex in the basis `s^k v_ī ⊗ v_j̄`, `ī ∈ L̄(k)`, `j̄ ∈ L(l)`, with boundary `± s^{k−1} v_{i_1} ⋯ v_{i_{k−1}} ⊗ v_{i_k} v_{j_1} ⋯ v_{j_l}` "when (i_k, j_1) ∈ L(2)" and 0 when `(i_k, j_1) ∈ L̄(2)`, in which case the element is the boundary of `s^{k+1} v_{i_1} ⋯ v_{i_k} v_{j_1} ⊗ v_{j_2} ⋯ v_{j_l}`, so "the Koszul complex is acyclic".
[^reiner]: https://www-users.cse.umn.edu/~reiner/Talks/kslides.pdf (V. Reiner, "Koszul algebras in combinatorics", slides, read 2026-10-28) p.17 - "Algebras from walks in directed graphs. D a directed graph on [n], that is, a collection of ordered pairs (i, j) (with i = j allowed). AD := k⟨x1, . . . , xn⟩/⟨xixj : (i, j) ∉ D⟩ is Koszul ... Its Koszul dual A!D := AD̄ for the complementary digraph D̄. AD has Hilbert function h(AD, n) := |{walks of length n in D}| so that Hilb(AD, t) can be computed via the transfer-matrix method."; the slide's walk of length `n` is a word of `n` letters.
[^nacin]: https://oeis.org/A287804, https://oeis.org/A287806, https://oeis.org/A287808, https://oeis.org/A287812, https://oeis.org/A287816, https://oeis.org/A287825, https://oeis.org/A287832, https://oeis.org/A126358, https://oeis.org/A083318 (read 2026-10-28) - A287804, "Number of quinary sequences of length n such that no two consecutive terms have distance 1.", with "G.f.: (1 - 3*x^2)/(1 - 5*x + 5*x^2 + x^3)", by David Nacin, and the same name for senary, septenary, octonary and nonary sequences and for the alphabets `{0, 1, …, 9}` and `{0, 1, …, 10}`, all at offset 0; A126358, "Number of base 4 n-digit numbers with adjacent digits differing by one or less.", with the formula "a(n) = 2*F(2*n+1) = A052995(n+1) for n>0, F(n)=A000045(n) and a(0)=1. - _Mircea Merca_, Jun 28 2012", "G.f.: (1+x-x^2)/(1-3*x+x^2)." and the comment "a(n) is the number of quaternary sequences of length n such that no two adjacent terms differ by exactly 1. - _David Nacin_, May 31 2017"; A083318, "a(0) = 1; for n>0, a(n) = 2^n + 1.".
[^kmmp]: [[knopfmacher-mansour-munagi-prodinger-2008-smooth-words](pages/knopfmacher-mansour-munagi-prodinger-2008-smooth-words.md)] §2 Theorem 2.2 and p.5 L216-L222, L235-L238 [synthesis] - Theorem 2.2, the generating function `sw_k(x) = 1 + x(k − (3k + 2)x)/(1 − 3x)² + 2x²(1 + U_{k−1}((1 − x)/(2x)))/((1 − 3x)² U_k((1 − x)/(2x)))` of the smooth words over `[k]`, the empty word included, and at `k = 4` "sw4 (x) = (1+x−x²)/(1−3x+x²)", the number of smooth words "= 2F2n+1".
[^blocks]: [[project-euler-502-brute-force](pages/project-euler-502-brute-force.md)] §"brute" L24 - "= c_1 + \sum_{i=2}^{w} \max(0, c_i - c_{i-1})", the column-height block-count formula.
[^exec1]: Verified by execution (Python 3.11 with NumPy and SymPy, 2026-10-28): `bin/python/hilbert_castles.py` item [1], run log `bin/python/hilbert_castles-run.log`. Equation (1) to `x^10` on all 66,066 rules of heights 1 to 4 (to `x^8` at height 4), and to `x^14`, `x^14`, `x^12` on 300 random rules at each of the heights 5, 6, 7; the weighted form with `q^a` for a column of height `a`, to `x^8` on all 530 rules of height at most 3 and to `x^7` on 100 random rules at each of the heights 4 and 5; the cuts of every skyline of width 1 to 6 under 120 random rules of heights 2 to 4, none or two neighboring cuts in every case; the series of `J`, `0`, `J − I` and `I` for `h = 2, …, 8`.
[^exec2]: Verified by execution (Python 3.11, 2026-10-28): `bin/python/hilbert_castles.py` item [2], run log `bin/python/hilbert_castles-run.log`. The example, the five Hilbert castles of width 2 and height 4 with their drawings and block counts, and the two non-examples.
[^exec3]: Verified by execution (Python 3.11 with SymPy, 2026-10-28): `bin/python/hilbert_castles.py` item [3], run log `bin/python/hilbert_castles-run.log`. `hstrips(n, h)` against every term of A083318, A126358, A287804, A287806, A287808, A287812, A287816, A287825 and A287832 at offset 0 (21 to 32 terms); the castle table by Equation (2) and by brute force; the closed forms at heights 2, 3 and 4 and `hstrips(w, 4) = 2F_{2w+1}` for `w ≤ 60`; Equation (3) as an identity of rational functions for `h = 2, …, 8`, with the table rows for `h ≤ 6`; A000225 against `A_hilbert(w, 3)`.
[^exec4]: Verified by execution (Python 3.11 with SymPy, 2026-10-28): `bin/python/hilbert_castles.py` item [4], run log `bin/python/hilbert_castles-run.log`. The relabeling maps `I + A_path` onto `J − A_path` and `A_path` onto `J − I − A_path` on four heights; the two characteristic polynomials; no relabeling maps the path onto its complement at any other height `h = 2, …, 8`; the free 1-smooth strips and the Hilbert strips on four heights against each other and A126358, the zig-zag and 2-disparate strips against each other and `2F_{w+2}`, for `w ≤ 30`; the free 1-smooth strips on four heights that use the height 3 against `A_hilbert(w, 4)` for `w ≤ 8`.
[^exec5]: Verified by execution (Python 3.11 with NumPy, SymPy and mpmath, 2026-10-28): `bin/python/hilbert_castles.py` item [5], run log `bin/python/hilbert_castles-run.log`. For `h = 2, …, 12`: the largest eigenvalue, its minimal polynomial and degree; the two bounds; `A_hilbert(401, h)/A_hilbert(400, h)` against the eigenvalue, to 14 decimals; the eigenvalues on the antisymmetric vectors against `−2cos(πk/(h + 1))`, `k` even. The degree of the reduced denominator of Equation (3) for `h = 2, …, 8` (item [3]).
[^exec6]: Verified by execution (Python 3.11, 2026-10-28): `bin/python/hilbert_castles.py` item [6], run log `bin/python/hilbert_castles-run.log`. The even-block and odd-block counts by a transfer count with the block sign, for `h = 2, …, 7` and `w ≤ 12`, against brute force wherever `h^w ≤ 2·10^6`; no even-block Hilbert castle of height 3 for `w ≤ 30`.
[^exec7]: Verified by execution (Python 3.11 with NumPy and SymPy, 2026-10-28): `bin/python/hilbert_castles.py` item [7], run log `bin/python/hilbert_castles-run.log`. `J` minus the `(m − 1)`-smooth rule is the m-disparate rule, with Equation (1) to `x^20`, for `m = 1, …, 5` and `h = 1, …, 9`; Theorem 2.2 of Knopfmacher, Mansour, Munagi and Prodinger against the free 1-smooth strip series, and the 2-disparate strip series against `1/sw_h(−x)`, for `h = 2, …, 8`; the 2-disparate rule against `J − I − A_path` and its largest eigenvalue against `ρ(J − A_path) − 1`.
[^exec8]: Verified by execution (Python 3.11 with SymPy, 2026-10-28): `bin/python/hilbert_castles.py` item [8], run log `bin/python/hilbert_castles-run.log`. The reciprocal at `−x` of the series of the dual rule against `(1 + P_h(q)x)/(1 − qx − qP_h(q)x²)`, and that against the tree skylines by width and area to `x^8`, for `h = 2, …, 7`; the case `q = 1`.
