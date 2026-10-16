---
title: q-Fibonacci castle
category: Concepts
summary: The q-Fibonacci castles are the Fibonacci castles, the tree castles of height 2, counted with a second variable q marking area. At width w the q-count is A_Fib(w; q) = q^w (f_w(q) − 1), with f_w(q) = Σ_m C(w − m + 1, m) q^m (f_w = f_{w−1} + q f_{w−2}), which is F_{w+2} − 1 at q = 1, and the even-block part is q^w (f_w(q) − f_w(−q))/2. The generating function in area and width is B_Fib(q, z) = (1 + q²z)/(1 − qz − q³z²) − 1/(1 − qz). Over all widths the q-Fibonacci castles with n cells number A000930(n+1) − 1, supergolden by area (1.46557…); the even-block ones have g.f. q²/((1 − q)² − q⁶), and the even-minus-odd count is at most a constant times ψ^{n/2}, ψ the plastic number. This q is not the q of the standard q-Fibonacci polynomials of weighted tilings, which on the same castles counts the sum of the positions of the height-2 columns.
tags: [concept, castle, castle-type, fibonacci, q-analogue, area, generating-function, parity, supergolden, plastic-number, narayana-cows]
sources: [q-catalan-numbers]
created: 2026-10-03
updated: 2026-10-16
---

# q-Fibonacci castle

## Definition

A [[fibonacci-castle](pages/fibonacci-castle.md)] is a castle of height 2 with no two adjacent height-2 columns; there are `A_Fib(w) = F_{w+2} − 1` of width `w`, and they are the tree castles of height 2 ([[tree-castle-by-area](pages/tree-castle-by-area.md)]). The **q-Fibonacci castles** are the same castles counted with a second variable `q` that marks area, the number of cells:

```
A_Fib(w; q)  =  Σ over the Fibonacci castles c of width w  of  q^{area(c)}.
```

At `q = 1` this is `A_Fib(w)`. Here `q` marks area as in the q-Catalan numbers of Pólya and Gessel, which count parallelogram polyominoes by area ([[q-catalan-numbers](pages/q-catalan-numbers.md)]).[^qcat]

*Example.* The Fibonacci castles of width 3 are the skylines `(1, 1, 2)`, `(1, 2, 1)` and `(2, 1, 1)`, with 4 cells, and `(2, 1, 2)`, with 5, so `A_Fib(3; q) = 3q⁴ + q⁵`.

The standard q-Fibonacci polynomials of weighted tilings count a different statistic on the same castles, the sum of the positions of the height-2 columns (section *Tiling q-Fibonacci polynomials*; [[n-nacci-disambiguation](pages/n-nacci-disambiguation.md)]).

## The q-count at width w

A Fibonacci castle with `m` height-2 columns has `w + m` cells, and `C(w − m + 1, m)` of the Fibonacci castles of width `w` have `m` height-2 columns ([[fibonacci-castle](pages/fibonacci-castle.md)]). So[^exec]

```
A_Fib(w; q)  =  q^w (f_w(q) − 1),        f_w(q)  =  Σ_m C(w − m + 1, m) q^m,
f_0 = 1,   f_1 = 1 + q,   f_w = f_{w−1} + q f_{w−2},                                  (1)
```

where `f_w(q)` counts the Fibonacci towers of length `w`, the 0/1 strings with no two adjacent 1s, by their number of 1s, and the `−1` removes the flat row, which does not reach height 2. The polynomial `q^w f_w(q)` is `T_2(w, q)`, the area polynomial of the tree skylines of height at most 2 on [[tree-castle-by-area](pages/tree-castle-by-area.md)]; its recurrence `T_h(w, q) = q T_h(w − 1, q) + q P_h(q) T_h(w − 2, q)`, with `P_2(q) = q²`, is the recurrence of Equation (1) multiplied through by `q^w`.

**Generating function in area and width.** With `z` marking width, as in castle-notation's `B(q, z)`,[^exec]

```
B_Fib(q, z)  =  Σ_{w ≥ 1} A_Fib(w; q) z^w  =  (1 + q² z) / (1 − q z − q³ z²)  −  1 / (1 − q z).      (2)
```

The first term is the Fibonacci-tower generating function `(1 + xy)/(1 − x − x²y)` of [[fibonacci-castle](pages/fibonacci-castle.md)], with `x` marking length and `y` the 1s, at `x = qz`, `y = q`; the second removes the flat rows.

**Even-block part.** A Fibonacci castle with `m` height-2 columns has `m + 1` blocks, so it has an even number of blocks exactly when `m` is odd, and[^exec]

```
A^e_Fib(w; q)  =  q^w (f_w(q) − f_w(−q)) / 2.
```

At `q = 1` this is `(F_{w+2} − P_F(w))/2`, with `P_F(w) = f_w(−1)` the signed Fibonacci tower count, the even-block Fibonacci castle count `A^e_Fib(w)` of [[fibonacci-castle](pages/fibonacci-castle.md)].

## Counting by number of cells

Setting `z = 1` collects the q-Fibonacci castles of every width by their number of cells `n`:[^exec]

```
B_Fib(q, 1)  =  (1 + q²) / (1 − q − q³)  −  1 / (1 − q),
coefficients  1, 2, 3, 5, 8, 12, 18, 27, 40, 59, 87, 128, 188, 276, …   (n = 2, 3, 4, …)
           =  A000930(n + 1) − 1,
```

one less than Narayana's cows `A000930`.[^a000930] These are the tree castles of height 2 by area, the row `h = 2` of Table 2 on [[tree-castle-by-area](pages/tree-castle-by-area.md)]. The growth constant is the real root `1.46557…` of `x³ = x² + 1`, which the OEIS calls the supergolden ratio, so the q-Fibonacci castles are supergolden by area;[^a092526] counted by width instead, the Fibonacci castles are golden by width.

**Even and odd by number of cells.** The even-block q-Fibonacci castles with `n` cells have generating function[^exec]

```
B^e_Fib(q, 1)  =  q² / ((1 − q)² − q⁶)  =  q² / ((1 − q − q³)(1 − q + q³)),
coefficients  1, 2, 3, 4, 5, 6, 8, 12, 19, 30, 46, 68, 98, 140, …   (n = 2, 3, …).
```

The difference between the even-block and the odd-block counts has generating function

```
2 B^e_Fib(q, 1) − B_Fib(q, 1)  =  1/(1 − q) − (1 − q²)/(1 − q + q³),
coefficients  1, 2, 3, 3, 2, 0, −2, −3, −2, 1, 5, 8, …   (n = 2, 3, …).
```

The roots of `1 − q + q³` are `−ψ`, with `ψ = 1.32472…` the plastic number ([[plastic-number](pages/plastic-number.md)]), and a complex pair of modulus `ψ^{−1/2} = 0.86883…`, since the product of the three roots is `−1`. So the difference changes sign and stays within a constant times `ψ^{n/2}`, against the supergolden growth of the total; for `300 ≤ n < 400` its absolute value is below `1.141 ψ^{n/2}`.[^exec]

## Tiling q-Fibonacci polynomials

Lindgren, Ngo and Segroves call the following "the standard q-analogue" of the Fibonacci numbers: a tiling of a board by squares and dominoes has weight `q^i` for each domino at position `(i, i + 1)`, and `f^C_{n+1}(q)` is the sum of the weights of the tilings of a board of length `n`. These polynomials satisfy `f^C_{n+1}(q) = f^C_n(q) + q^{n−1} f^C_{n−1}(q)` with `f^C_1 = f^C_2 = 1`, so `f^C_3 = 1 + q`, `f^C_4 = 1 + q + q²` and `f^C_5 = 1 + q + q² + q³ + q⁴`.[^carlitz] On Fibonacci towers of length `w`, `f^C_{w+2}(q)` is the sum of `q` to the sum of the positions of the 1s, the positions numbered from 1 (computed for `w ≤ 8`):[^exec]

| | `q` marks | polynomial for the Fibonacci towers of length `w` | recurrence |
|---|---|---|---|
| q-Fibonacci castles (this page) | the number of height-2 columns (area minus `w`) | `f_w(q) = Σ_m C(w − m + 1, m) q^m` | `f_w = f_{w−1} + q f_{w−2}` |
| tiling q-Fibonacci polynomials | the sum of the positions of the height-2 columns | `f^C_{w+2}(q)` | `f^C_{n+1} = f^C_n + q^{n−1} f^C_{n−1}` |

At `w = 3` the towers `000`, `001`, `010`, `100`, `101` give `f_3(q) = 1 + 3q + q²` and `f^C_5(q) = 1 + q + q² + q³ + q⁴`. Both are `F_5 = 5` at `q = 1`. The two polynomials agree at `w = 1` and differ for every `w ≥ 2` (computed for `w ≤ 7`). On the wiki, "q-Fibonacci castle" means the area version.

## Related Concepts

- [[fibonacci-castle](pages/fibonacci-castle.md)] - the Fibonacci castles, their towers and the counts `A_Fib(w) = F_{w+2} − 1`, `A^e_Fib`, `A^o_Fib`.
- [[tree-castle-by-area](pages/tree-castle-by-area.md)] - the tree skylines and tree castles by area; its row `h = 2` is this page's count by cells, with the same growth constant `1.46557…`.
- [[n-nacci-disambiguation](pages/n-nacci-disambiguation.md)] - the Fibonacci appearances on the wiki, including the q-Fibonacci polynomials of weighted tilings.
- [[castle-by-area](pages/castle-by-area.md)] and [[q-thread-seminar](pages/q-thread-seminar.md)] - castles counted by area.
- [[q-catalan-numbers](pages/q-catalan-numbers.md)] - parallelogram polyominoes counted by area, the source of the convention that `q` marks area.
- [[castle-classification-growth](pages/castle-classification-growth.md)] - growth constants by area and by width.
- [[plastic-number](pages/plastic-number.md)] - `ψ`, whose negative is the real root of `1 − q + q³`.

## Footnotes

[^qcat]: raw/q-catalan-numbers.wiki L9 - "q-Catalan numbers (Polya, Gessel) count parallelogram polyominoes by area".
[^a000930]: https://oeis.org/A000930 (read 2026-10-16) - "Narayana's cows sequence: a(0) = a(1) = a(2) = 1; thereafter a(n) = a(n-1) + a(n-3)."
[^a092526]: https://oeis.org/A092526 (read 2026-10-16) - "the real root of x^3 - x^2 - 1", "This is the limit x of the ratio N(n+1)/N(n) for n -> infinity of the Narayana sequence N(n) = A000930(n)", and "Sometimes called the supergolden ratio or Narayana's cows constant".
[^carlitz]: https://d31kydh6n6r5j5.cloudfront.net/uploads/sites/66/2019/04/Fibonacci_comps.pdf (E. Lindgren, M. A. Ngo, S. Segroves, "Weighted Tilings and q-Fibonacci Numbers", Carleton College, 2007) pp.1-2 - "A particular tiling's weight is the product of all q^i such that the tiling has a domino at position (i, i + 1)"; "we get the standard q-analogue: f_n+1(q) = f_n(q) + q^n−1 f_n−1(q), f_1(q) = f_2(q) = 1"; "f_5(q) = ... = 1 + q + q^2 + q^3 + q^4".
[^exec]: Verified by execution (Python 3.11 with SymPy, 2026-10-16), by enumeration of the Fibonacci castles: for `w ≤ 11`, `A_Fib(w; q) = q^w (f_w(q) − 1)`, the count `F_{w+2} − 1`, the recurrence of `f_w`, and the even-block part `q^w (f_w(q) − f_w(−q))/2`; Equation (2) through `z^9`; by number of cells through `n = 22`, the totals equal the coefficients of `B_Fib(q, 1)` and `A000930(n + 1) − 1` (the latter through `n = 40`), the even-block counts those of `q²/((1 − q)² − q⁶)`, and the difference those of `1/(1 − q) − (1 − q²)/(1 − q + q³)`; the factorization of `(1 − q)² − q⁶`; the roots of `1 − q + q³` (`−1.32472`, `0.66236 ± 0.56228i`); the bound `1.1408 ψ^{n/2}` for `300 ≤ n < 400`; the real root `1.46557` of `x³ − x² − 1`; the tiling recurrence against the sum over the Fibonacci towers of length `w ≤ 8` of `q^{sum of the positions of the 1s}`, and `f_w ≠ f^C_{w+2}` for `2 ≤ w ≤ 7`.
