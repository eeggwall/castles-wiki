---
title: q-Fibonacci castle
category: Concepts
summary: The q-Fibonacci castles are the Fibonacci castles counted with a second variable q marking area. At width w the count is the polynomial q^w (f_w(q) − 1), with f_w(q) = Σ_m C(w − m + 1, m) q^m (f_w = f_{w−1} + q f_{w−2}), which is F_{w+2} − 1 at q = 1; the even-block part is q^w (f_w(q) − f_w(−q))/2. The generating function in width and area is (1 + q²x)/(1 − qx − q³x²) − 1/(1 − qx). Summed over all widths, the q-Fibonacci castles with n cells number 1, 2, 3, 5, 8, 12, 18, 27, … = A000930(n+1) − 1, growing like the supergolden constant 1.4656; the even-block ones have GF q²/((1 − q)² − q⁶), and even minus odd is of size at most a constant times ψ^{n/2} (ψ the plastic number). Here q marks area, as in the Pólya-Gessel q-Catalan numbers; this is not Carlitz's q-Fibonacci polynomial, which on the same castles counts the sum of the positions of the height-2 columns.
tags: [concept, castle, castle-type, fibonacci, q-analogue, area, generating-function, parity, supergolden, plastic-number, narayana-cows, carlitz]
sources: [project-euler-502]
created: 2026-10-03
updated: 2026-10-03
---

# q-Fibonacci castle

## Definition

A [[fibonacci-castle](pages/fibonacci-castle.md)] is a castle of exact height 2 with no two adjacent height-2 columns; there are `F_{w+2} − 1` of width `w`. The **q-Fibonacci castles** are the same castles counted with a second variable `q` that marks area (the number of cells):

```
Q_w(q)  =  Σ over Fibonacci castles c of width w  of  q^{area(c)}.
```

At `q = 1` this is the Fibonacci castle count `F_{w+2} − 1`; the variable `q` refines it by area. The `q` plays the role it has on the area side of the wiki generally, as in the q-Catalan numbers of Pólya and Gessel, which count parallelogram polyominoes by area ([[q-catalan-numbers](pages/q-catalan-numbers.md)]).[^qcat]

**Example.** The Fibonacci castles of width 3 are `(1,1,2)`, `(1,2,1)`, `(2,1,1)` with 4 cells and `(2,1,2)` with 5, so `Q_3(q) = 3q⁴ + q⁵`.

**Not Carlitz's q-Fibonacci numbers.** In the literature, "q-Fibonacci" usually means Carlitz's polynomials, which weight each domino of a tiling by `q` to the power of its position. On Fibonacci castles that statistic is the sum of the positions of the height-2 columns, not the area. See the section below and [[n-nacci-disambiguation](pages/n-nacci-disambiguation.md)].

## The q-count at width `w`

A Fibonacci castle with `m` height-2 columns has `w + m` cells, and `C(w − m + 1, m)` Fibonacci castles of width `w` have `m` height-2 columns ([[fibonacci-castle](pages/fibonacci-castle.md)]). So

```
Q_w(q)  =  q^w (f_w(q) − 1),      f_w(q)  =  Σ_m C(w − m + 1, m) q^m,
f_0 = 1,   f_1 = 1 + q,   f_w = f_{w−1} + q f_{w−2},
```

where `f_w(q)` counts all second rows of length `w` (0/1 strings with no two adjacent 1s) by their number of 1s, and the `−1` removes the flat row, which does not reach height 2.[^exec] The polynomial `q^w f_w(q)` is the `h = 2` case of the tree-castle polynomials `T_h(w, q)` on [[tree-castle-by-area](pages/tree-castle-by-area.md)], whose recurrence `T_h(w, q) = q T_h(w − 1, q) + q P_h(q) T_h(w − 2, q)` becomes `q T(w − 1) + q³ T(w − 2)` at `h = 2`.

**Generating function in width and area.**

```
Σ_{w ≥ 1} Q_w(q) x^w  =  (1 + q² x) / (1 − q x − q³ x²)  −  1 / (1 − q x).
```

The first term is the second-row generating function `(1 + xy)/(1 − x − x²y)` of [[fibonacci-castle](pages/fibonacci-castle.md)] at `x → qx`, `y → q`; the second removes the flat rows.[^exec]

**Even-block q-count.** A Fibonacci castle with `m` height-2 columns has `m + 1` blocks, so it has an even number of blocks exactly when `m` is odd, and

```
even-block part of Q_w(q)  =  q^w (f_w(q) − f_w(−q)) / 2,
```

which at `q = 1` is `(F_{w+2} − P_F(w))/2`, the even-block Fibonacci castle count.[^exec]

## Counting by number of cells

Setting `x = 1` collects the q-Fibonacci castles of every width by their number of cells `n`:

```
Σ_n (count) q^n  =  (1 + q²) / (1 − q − q³)  −  1 / (1 − q),
count  =  1, 2, 3, 5, 8, 12, 18, 27, 40, 59, 87, 128, 188, …   (n = 2, 3, 4, …)
       =  A000930(n + 1) − 1,
```

one less than Narayana's cows. The growth constant is the supergolden constant `≈ 1.4656`, the real root of `x³ = x² + 1` ([[tree-castle-by-area](pages/tree-castle-by-area.md)], [[castle-classification-growth](pages/castle-classification-growth.md)]). Counted by cells instead of by width, the growth drops from `φ` to supergolden, because a wide castle with few height-2 columns now costs one cell per column.[^exec]

**Even and odd by number of cells.** The even-block q-Fibonacci castles with `n` cells number

```
Σ_n (even) q^n  =  q² / ((1 − q)² − q⁶)  =  q² / ((1 − q − q³)(1 − q + q³)),
even  =  1, 2, 3, 4, 5, 6, 8, 12, 19, 30, 46, 68, 98, 140, …   (n = 2, 3, …).
```

The difference even − odd has generating function `1/(1 − q) − (1 − q²)/(1 − q + q³)`, which gives `1, 2, 3, 3, 2, 0, −2, −3, −2, 1, 5, 8, …` from `n = 2`. The roots of `1 − q + q³` are `−ψ`, with `ψ ≈ 1.3247` the plastic number ([[plastic-number](pages/plastic-number.md)]), and a complex pair of modulus `ψ^{−1/2}`, so the difference changes sign and stays within a constant times `ψ^{n/2}`, far below the supergolden growth of the total.[^exec]

## Carlitz's q-Fibonacci polynomials: a different statistic

Carlitz's q-Fibonacci polynomials weight a tiling of a board by squares and dominoes with `q^i` for each domino starting at position `i`. They satisfy `f_{n+1}(q) = f_n(q) + q^{n−1} f_{n−1}(q)` with `f_1 = f_2 = 1`, so `f_3 = 1 + q`, `f_4 = 1 + q + q²`, `f_5 = 1 + q + q² + q³ + q⁴`.[^carlitz] Translated to Fibonacci castles:[^exec]

| | q marks | polynomial for second rows of length `w` | recurrence |
|---|---|---|---|
| **q-Fibonacci castles** (this page) | area: one `q` per cell, so `q^w` times one `q` per height-2 column | `q^w f_w(q)`, `f_w = Σ_m C(w − m + 1, m) q^m` | `f_w = f_{w−1} + q f_{w−2}` |
| **Carlitz's q-Fibonacci** | the sum of the positions (`1, …, w`) of the height-2 columns | Carlitz's `f_{w+2}(q)` | `f_{n+1} = f_n + q^{n−1} f_{n−1}` |

At `w = 3` the second rows `000, 001, 010, 100, 101` give `1 + 3q + q²` for the number of height-2 columns and `1 + q + q² + q³ + q⁴` for the sum of positions. Both specialize to `F_5 = 5` at `q = 1`, and they differ for every `w ≥ 2`. "q-Fibonacci castle" on this wiki always means the area version.

## Related Concepts

- [[fibonacci-castle](pages/fibonacci-castle.md)] - the castles themselves and their count `F_{w+2} − 1`.
- [[n-nacci-disambiguation](pages/n-nacci-disambiguation.md)] - every Fibonacci appearance, including the separation of q-Fibonacci castles from Carlitz's q-Fibonacci numbers.
- [[tree-castle-by-area](pages/tree-castle-by-area.md)] - the tree-castle q-polynomials, of which these are the exact-height-2 case.
- [[castle-by-area](pages/castle-by-area.md)], [[q-thread-seminar](pages/q-thread-seminar.md)] - castles graded by area.
- [[q-catalan-numbers](pages/q-catalan-numbers.md)] - the q-analogue convention, q marking area.
- [[castle-classification-growth](pages/castle-classification-growth.md)] - the supergolden area growth class.
- [[plastic-number](pages/plastic-number.md)] - the root `−ψ` of the signed denominator.

## Footnotes

[^qcat]: raw/q-catalan-numbers.wiki L9 - "q-Catalan numbers (Polya, Gessel) count parallelogram polyominoes by area".
[^carlitz]: https://d31kydh6n6r5j5.cloudfront.net/uploads/sites/66/2019/04/Fibonacci_comps.pdf (E. Lindgren, M. A. Ngo, S. Segroves, "Weighted Tilings and q-Fibonacci Numbers", Carleton College, 2007) pp.1-2 - "A particular tiling's weight is the product of all q^i such that the tiling has a domino at position (i, i + 1)"; "we get the standard q-analogue: f_n+1(q) = f_n(q) + q^n−1 f_n−1(q), f_1(q) = f_2(q) = 1"; "f_5(q) = ... = 1 + q + q^2 + q^3 + q^4". Their reference [4] is L. Carlitz, "Fibonacci notes III: q-Fibonacci numbers", Fibonacci Quarterly 12(4) (1974), 317-322 (not read).
[^exec]: Verified by execution (Python 3, SymPy, 2026-10-03), by brute force over all Fibonacci castles: for `w ≤ 11`, `Σ q^{area} = q^w (f_w(q) − 1)`, its value at `q = 1` is `F_{w+2} − 1`, `f_w = Σ_m C(w−m+1, m) q^m`, and the even-block part is `q^w (f_w(q) − f_w(−q))/2`; the bivariate GF matches through `x^9`; by number of cells through `n = 22` the counts match `(1 + q²)/(1 − q − q³) − 1/(1 − q)` and `A000930(n+1) − 1` (A000930 from `a(n) = a(n−1) + a(n−3)`, `a(0..2) = 1`), and the even-block counts match `q²/((1 − q)² − q⁶)`; `2·even − total` matches `1/(1 − q) − (1 − q²)/(1 − q + q³)` through `n = 59`, and its absolute value divided by `ψ^{n/2}` stays below `1.141` for `n = 300..399`; the roots of `1 − q + q³` are `−1.32472` and `0.66236 ± 0.56228i` (modulus `0.86883 = ψ^{−1/2}`); Carlitz's recurrence `f_{n+1} = f_n + q^{n−1} f_{n−1}` equals `Σ_k q^{k²} [n−k−1, k]_q` for `n ≤ 11`, and `f_{w+2}(q)` equals the sum over second rows of length `w ≤ 8` of `q^{sum of positions of the 1s}` (positions numbered from 1).
