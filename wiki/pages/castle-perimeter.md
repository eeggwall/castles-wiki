---
title: Castle perimeter - blocks are the vertical half-perimeter
category: Analyses
summary: A castle of width w has semi-perimeter s = w + blocks, so the block count is half the vertical perimeter and the even-block condition of Project Euler 502 says that s and w have the same parity; s ≥ w + h with equality exactly for convex castles. Castles by semi-perimeter are the bargraphs A082582, with the algebraic generating function B(t) = (1 − 2t − t² − √(1 − 4t + 2t² + t⁴))/(2t) and growth τ² = 3.38297 (τ the tribonacci constant); by semi-perimeter and width they are A271942. The signed count has generating function (1 + t² − √((1 + t)(1 − t + 3t² + t³)))/(2t) and grows only like τ. Convex castles by semi-perimeter are F_{2s−3} = A001519(s − 1), and their signed count is periodic with period 6.
tags: [analysis, castle, perimeter, blocks, parity, bargraph, generating-function, algebraic, tribonacci, fibonacci, delest-viennot, oeis]
sources: [algebraic-languages-and-polyominoes-enumeration, project-euler-502-brute-force, tower-narayana-polynomial, baril-florez-ramirez-2026-generalized-narayana-arrays]
created: 2026-09-22
updated: 2026-10-23
---

# Castle perimeter - blocks are the vertical half-perimeter

## The identity

A castle of width `w` is a skyline `c = (c_1, …, c_w)` with every `c_i ≥ 1` ([[castle-polyomino](pages/castle-polyomino.md)]). With `c_0 = c_{w+1} = 0`, its block count is the total rise of the skyline,[^1]

```
blocks(c)  =  Σ_{i=1}^{w} max(0, c_i − c_{i−1}).
```

As a polyomino, the castle has `2w` horizontal unit edges on its boundary, `w` on the base and `w` on the tops of the columns, and `Σ_{i=0}^{w} |c_{i+1} − c_i|` vertical ones. The total rise equals the total fall, because the differences `c_{i+1} − c_i` sum to `c_{w+1} − c_0 = 0`, so the vertical boundary has length `2·blocks(c)`, and

```
perimeter  =  2(w + blocks(c)),        semi-perimeter  s  =  w + blocks(c).          (1)
```

*Example.* The castle `(2, 1, 2)` has `3` blocks and semi-perimeter `6`: its boundary has 6 horizontal edges and the 6 vertical edges `2, 1, 1, 2`.

Three consequences:

- **The even-block condition is a perimeter parity.** `A^e(w, h)`, the Project Euler 502 count (the problem statement's `F(w, h)`), counts the castles of width `w` and height `h` whose semi-perimeter has the parity of `w`. At fixed width, the distribution of the block count is the distribution of the semi-perimeter shifted by `w`.
- **Convex castles have the least perimeter.** A castle of height `h` has at least `h` blocks, with equality exactly when it is convex, that is, when its skyline rises and then falls ([[convex-castle](pages/convex-castle.md)], the Proposition there). By Equation (1), `s ≥ w + h`: the perimeter is at least `2(w + h)`, the perimeter of the bounding box, with equality exactly for convex castles, as for convex polyominoes in general ([[convex-polyomino](pages/convex-polyomino.md)]).
- **Perimeter grading.** Delest and Viennot count convex polyominoes by perimeter.[^2] For castles the semi-perimeter is width plus blocks, the two statistics of the tower-Narayana identity in the section *Castles by semi-perimeter*.

## Castles by semi-perimeter

Removing the bottom row leaves towers with one block fewer ([[castle-notation](pages/castle-notation.md)]). The towers on a base of length `w` with `b` blocks, over all heights, number[^3]

```
Σ_{k=1}^{w}  N(w, k) · C(b + w − k, w − 1),
```

where `N(w, k) = C(w, k) C(w, k − 1)/w` are the Narayana numbers ([[tower-narayana-polynomial](pages/tower-narayana-polynomial.md)], [[narayana-numbers](pages/narayana-numbers.md)]). So the castles of width `w` and semi-perimeter `s` have `s − w − 1` blocks in their towers and number `Σ_k N(w, k) C(s − k − 1, w − 1)`. The Narayana generating function `G(u, y) = Σ_{w,k} N(w, k) u^w y^k` satisfies `G = u(y + G)(1 + G)`. Marking width by `x` and blocks by `y` turns the factor `1/(1 − y)^w` of the tower count into the substitution `u = x/(1 − y)`, and setting `x = y = t` marks the semi-perimeter. This gives the generating function `B(t)` of the castles by semi-perimeter:[^4]

```
t·B² − (1 − 2t − t²)·B + t²  =  0
B(t)  =  ( 1 − 2t − t² − √(1 − 4t + 2t² + t⁴) ) / (2t)
      =  t² + 2t³ + 5t⁴ + 13t⁵ + 35t⁶ + 97t⁷ + 275t⁸ + 794t⁹ + ⋯
```

This is `A082582`, whose entry states that "a(n) is the number of bargraphs of semiperimeter n (n>=2)"; the OEIS generating function is `B(t) + 1 + t`. The triangle by semi-perimeter and width is `A271942`, "the number of bargraphs of semiperimeter n having width k", and its entries are `A271942(s, w) = Σ_k N(w, k) C(s − k − 1, w − 1)`, rechecked for `s = 2, …, 8`.[^5] `A082582` also counts the Dyck paths of semilength `n` that avoid `UUDD`, and the Dyck paths of semilength `n` with no peak at a height `≡ 2 (mod 3)`, which Baril, Flórez and Ramírez join by a bijection.[^6]

**Growth `τ²`.** The discriminant `1 − 4t + 2t² + t⁴` factors as `(t − 1)(t³ + t² + 3t − 1)`. Substituting `t = 1/y` and multiplying by `−y³` turns the cubic into `y³ − 3y² − y − 1`, the minimal polynomial of `τ²`, where `τ = 1.83928…` is the tribonacci constant, the real root of `τ³ = τ² + τ + 1`. The singularity of `B(t)` nearest 0 is the square-root branch point `t = 1/τ²`, so the castles of semi-perimeter `s` grow like `τ^{2s} s^{−3/2}`, with `τ² = 3.38297…`. The ratio of consecutive coefficients is `3.29999` at `s = 60`, below `τ²` as the factor `s^{−3/2}` requires.[^4]

## The parity split

The sign `(−1)^{blocks}` is `y = −t` with `x = t`, so `u = t/(1 + t)`, and the signed generating function `B_s(t)` satisfies[^4]

```
t·B_s² − (1 + t²)·B_s − t²  =  0
B_s(t)  =  ( 1 + t² − √((1 + t)(1 − t + 3t² + t³)) ) / (2t)
        =  −t² + t⁴ + t⁵ − t⁶ − 3t⁷ − t⁸ + 6t⁹ + 9t¹⁰ − 5t¹¹ − 29t¹² − 20t¹³ + 55t¹⁴ + ⋯
```

The even-block castles by semi-perimeter have generating function `(B + B_s)/2`:

```
s = 2, …, 16:   0, 1, 3, 7, 17, 47, 137, 400, 1168, 3450, 10338, 31311, 95521, 293169, 904999
```

Both series agree with a dynamic program over skylines through `s = 30`.

**The sign halves the growth exponent.** Substituting `t = −1/y` in the signed cubic `t³ + 3t² − t + 1` and multiplying by `y³` gives `y³ + y² + 3y − 1`, the unsigned cubic in `y`. Its roots are `1/τ²` and a complex pair whose product with `1/τ²` is 1, so the pair has modulus `τ`. The singularities of `B_s` are therefore `t = −1`, `t = −τ²`, and a complex pair of modulus `1/τ`, which is the nearest to 0. So the signed count grows like `τ^s s^{−3/2}` with an oscillating factor: `|[t^n] B_s| · n^{3/2}/τ^n` lies between `0.07` and `0.84` for `n = 300, …, 320`. The unsigned count grows like `τ^{2s}`, so the even-block and odd-block castles of semi-perimeter `s` differ by about the square root of their number.[^4]

## Convex castles by semi-perimeter

A convex castle of height `h` has exactly `h` blocks, so its semi-perimeter is `s = w + h`. From the convex count `C(2h + w − 3, w − 1)` ([[convex-castle](pages/convex-castle.md)]),

```
Σ_{w,h≥1} C(2h + w − 3, w − 1) x^w y^h  =  xy(1 − x) / ((1 − x)² − y),
```

and at `x = t`, with `y = t` or `y = −t`:[^4]

| series | generating function in `t` | terms from `s = 2` |
|---|---|---|
| all | `t²(1 − t)/(1 − 3t + t²)` | `1, 2, 5, 13, 34, 89, …` `= A001519(s − 1) = F_{2s−3}` |
| signed | `−t²(1 − t)/(1 − t + t²)` | `−1, 0, 1, 1, 0, −1`, repeating with period 6 |
| even `h` | `t³(1 − t)/((1 − 3t + t²)(1 − t + t²))` | `0, 1, 3, 7, 17, 44, 116, 305, 799, 2091, 5473, …` |

Here `F_n` are the Fibonacci numbers with `F_1 = F_2 = 1`; Delest and Viennot write the same count as `F_{2n}` at perimeter `2n + 4`, with their indexing `F_0 = F_1 = 1`.[^7] The signed convex count is periodic because the roots of `1 − t + t²` are primitive sixth roots of unity. So the convex castles of semi-perimeter `s` with an even number of blocks number `(A001519(s − 1) + p(s))/2`, with `p(s)` the period-6 signed count.

## Relation to other pages

- [[algebraic-languages-and-polyominoes-enumeration](pages/algebraic-languages-and-polyominoes-enumeration.md)] - Delest and Viennot's counts of polyominoes by perimeter through algebraic languages. `B(t)` is algebraic; at bounded height the tower words form a regular language and the generating function is rational ([[tower-word-language](pages/tower-word-language.md)]).
- [[convex-castle](pages/convex-castle.md)], [[stack-polyomino-gf](pages/stack-polyomino-gf.md)] - convex castles are the stack polyominoes; the minimum-block Proposition and the convex count.
- [[tower-narayana-polynomial](pages/tower-narayana-polynomial.md)], [[narayana-numbers](pages/narayana-numbers.md)] - the tower-Narayana identity, of which `A271942` is a re-indexing; `k − 1` is the number of descents of the column heights.
- [[convex-polyomino](pages/convex-polyomino.md)], [[bousquet-melou-fedou-1995-convex-polyominoes](pages/bousquet-melou-fedou-1995-convex-polyominoes.md)] - convex polyominoes, whose perimeter is the perimeter of the bounding box, and Lin and Chang's generating function `Z(x, y, 1)` of convex polyominoes by width and height.
- [[deutsch-elizalde-2016-bargraphs-cornerless-motzkin](pages/deutsch-elizalde-2016-bargraphs-cornerless-motzkin.md)] - the same `B` from cornerless Motzkin paths: the first-return decomposition gives `xB² − (1 − x − y − xy)B + xy = 0`, with `x` marking width and `y` blocks, which is the quadratic of `B(t)` at `x = y = t`; the signed count is `y → −y`. Its row-deletion bijection sends the castles with every column at least 2, the prime castles ([[prime-castles](pages/prime-castles.md)]), to castles of semi-perimeter one less, so the prime castles by semi-perimeter are `A082582` shifted by one, with the opposite sign.
- [[baril-florez-ramirez-2026-generalized-narayana-arrays](pages/baril-florez-ramirez-2026-generalized-narayana-arrays.md)] - `A082582` as Dyck paths avoiding `UUDD` and as Dyck paths with no peak at a height `≡ 2 (mod 3)`, joined by the bijection `µ″`; the paper has no bargraphs.
- [[prodinger-2025-cornerless-motzkin-bargraphs](pages/prodinger-2025-cornerless-motzkin-bargraphs.md)] - skew Motzkin paths returning to the axis, of length `n`, are also counted by `A082582`, matching the castles of semi-perimeter `n + 1`; the paper gives their generating function refined by peaks and valleys, and no bijection with castles.
- [[castle-sign-kms-matrix](pages/castle-sign-kms-matrix.md)] - the discriminant of the Deutsch-Elizalde quadratic factors through `(1 − x)² − y(1 + x)²`, which at `x = t` is `−(t³ + t² + 3t − 1)` for `y = t` and `t³ + 3t² − t + 1` for `y = −t`: the unsigned and signed cubics of this page, related by `√y → i√y`.
- [[castle-sign](pages/castle-sign.md)] - the sign `(−1)^{blocks} = (−1)^{s − w}`.
- [[castles-of-height-h-by-area](pages/castles-of-height-h-by-area.md)] - the tribonacci constant `τ` as the growth of the castles of height 3 counted by area, where this page has `τ²` as the growth by semi-perimeter.
- [[prellberg-brak-1995-cluster-models](pages/prellberg-brak-1995-cluster-models.md)] - the functional equation (3.11) for bargraphs by horizontal perimeter, vertical perimeter and area, quadratic in `B`, and the scaling exponents `γ_u = −1/2`, `γ_t = −1/3`, `φ = 2/3` of their continuum limit.
- [[castle-q-bessel-closed-form](pages/castle-q-bessel-closed-form.md)] - the castle generating function `Π/(1 − x − Π)` by width, blocks and area, which at equal weights for width and blocks grades by semi-perimeter and area.
- [[semi-perimeter-growth-census](pages/semi-perimeter-growth-census.md)] - strip rules counted by semi-perimeter: the growth constants at each height through 4, silver first at height 5, and the bound that excludes bronze below height 22.

## Footnotes

[^1]: [[project-euler-502-brute-force](pages/project-euler-502-brute-force.md)] §"Column-height encoding" L22-24 - "#blocks = ∑_{r=1}^{h} #{runs of columns with c_i ≥ r} = c_1 + ∑_{i=2}^{w} max(0, c_i − c_{i−1})".
[^2]: [[algebraic-languages-and-polyominoes-enumeration](pages/algebraic-languages-and-polyominoes-enumeration.md)] p.169 Abstract - "we prove that the number of convex polyominoes with perimeter 2n+8 is (2n+11)4^n - 4(2n+1)C(2n,n)."
[^3]: raw/oeis-pe502/xrefs/A001263-tower.md L15-20 - "sum_b (number of towers of width w with b blocks) x^b = ( sum_{k=1..w} N(w,k) x^{k-1} ) / (1 - x)^w" and "the number of towers of width w with exactly b blocks is sum_{k=1..w} N(w,k) * C(b + w - k, w - 1)".
[^4]: Verified by execution (Python 3.11 with SymPy, 2026-10-16): the series of `B(t)` and `B_s(t)` against a dynamic program over skylines by semi-perimeter, width and blocks, through `s = 30`; the even-block counts for `s ≤ 16`; the factorization of the discriminant and the cubic of `τ²`; the coefficients of `B_s` to `n = 330` from its quadratic, with `|[t^n] B_s| n^{3/2}/τ^n` in `[0.0719, 0.8335]` for `300 ≤ n ≤ 320`; the coefficient ratio `3.29999` of `B` at `s = 60`; the convex generating function for `w, h ≤ 5` and its three series; the semi-perimeter of the castle `(2, 1, 2)`.
[^5]: https://oeis.org/A082582 and https://oeis.org/A271942 (read 2026-10-16) - A082582: "Expansion of (1 + x^2 - sqrt( 1 - 4*x + 2*x^2 + x^4)) / (2*x) in powers of x", "a(n) is the number of bargraphs of semiperimeter n (n>=2)", "a(n) is the number of Dyck paths of semilength n with no UUDD"; A271942: "Triangle read by rows: T(n,k) is the number of bargraphs of semiperimeter n having width k (n>=2, k>=1)", data "1, 1, 1, 1, 3, 1, 1, 5, 6, 1, 1, 7, 16, 10, 1, 1, 9, 31, 40, 15, 1, 1, 11, 51, 105, 85, 21, 1, …".
[^6]: [[baril-florez-ramirez-2026-generalized-narayana-arrays](pages/baril-florez-ramirez-2026-generalized-narayana-arrays.md)] §3.1.3 pp.342-344 L514-558, L618-628 - Example 3.10's array of Dyck paths by the number of peaks at heights `≡ 2 (mod 3)` has first column `1, 1, 1, 2, 5, 13, 35, 97`; "the first column ... corresponds to the sequence A082582, where the n-th term represents the number of Dyck paths of semilength n that avoid the pattern UUDD", and `µ″` is "a bijection mapping a Dyck path avoiding UUDD to the set of Dyck paths avoiding peaks at height congruent to 2 modulo 3".
[^7]: [[algebraic-languages-and-polyominoes-enumeration](pages/algebraic-languages-and-polyominoes-enumeration.md)] p.181 Lemma 3.2 - "The number of stack polyominoes with perimeter 2n+4 is the Fibonacci number F_{2n} with generating function (1-t^2)/((1-t-t^2)(1+t-t^2))."
