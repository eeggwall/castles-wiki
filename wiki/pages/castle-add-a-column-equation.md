---
title: Castles in the add-a-column framework - the Lemma 2.3 equation, the Temperley kernel, and the zoo sub-families
category: Analyses
summary: "Adding a column to a castle and recording its first-column height s gives the Bousquet-Mélou equation X(s) = xsyq/(1-syq) + x sq/(1-sq) X(1) - x sq(1-y)/((1-sq)(1-syq)) X(sq), with x width, y blocks, q area. It has no derivative term, so Lemma 2.3 solves it, and its E(1) and 1 - F(1) are term for term the N - M and M of the q-Bessel closed form. Against A001169 the castle keeps 1 of Temperley's k+l-1 placements, a rank-1 area kernel (2^(n-1)) against a rank-2 one (the order-3 Hickerson recurrence); the block weight y^max(0,l-k) has no finite rank, which is why the signed count is a q-series. Among the zoo families, castles meet convex, directed convex and stacks in the stacks, and parallelograms in reverse Ferrers. Monotone castles by area are 2p(n) - d(n), matching A329398 (interlink), and their signed count 2(-1)^n A000700(n) - sum_{d|n} (-1)^d has no OEIS match."
tags: [analysis, castle, polyomino, column-convex, add-a-column, temperley, functional-equation, q-shift, area, blocks, ferrers, stack-polyomino, parallelogram-polyomino, transfer-matrix, oeis, parity, novel-candidate]
sources: [column-convex-polygon-enumeration, counting-horizontally-convex-polyominoes]
created: 2026-09-23
updated: 2026-09-23
---

# Castles in the add-a-column framework

[[column-convex-polygon-enumeration](pages/column-convex-polygon-enumeration.md)] (Bousquet-Mélou 1996) turns any column-convex class into a q-shift equation by gluing columns one at a time. Castles are column-convex ([[castle-polyomino](pages/castle-polyomino.md)]), but the paper does not treat them as one of its classes. This page writes the castle equation in the paper's notation, solves it with the paper's Lemma 2.3, compares its column kernel with the Temperley kernel behind A001169, and places the paper's named sub-families (Ferrers, stack, parallelogram) inside the castles.

The derivations are own work, checked by execution (footnote 1). The framework and the lemma are from the paper.

## The castle equation

Use the paper's variables: `x` marks width, `y` the vertical half-perimeter, `q` area, and `s` the height of the first column.[^2] On a castle the vertical half-perimeter is the block count ([[castle-perimeter](pages/castle-perimeter.md)]), so `y` marks blocks. Let `X(s) = X(s, x, y, q)` count nonempty castles, with any height and any block parity.

Put a new first column of height `m` in front of a castle whose first column has height `k`. Both bottoms are on row 1. The new column adds `m` cells and one unit of width. It adds `max(0, m - k)` blocks, because the block count is the total ascent of the skyline with `c_0 = 0`. Summing over `m`:

- `m ≤ k` gives `sum_{m=1..k} (sq)^m = sq (1 - (sq)^k)/(1 - sq)`, the term `x sq/(1 - sq) (X(1) - X(sq))`;
- `m > k` gives `sum_{m>k} (sq)^m y^(m-k) = (sq)^k syq/(1 - syq)`, the term `x syq/(1 - syq) X(sq)`.

A single column of height `m` has weight `x (syq)^m`. Collecting terms:

```
X(s) = x e(s) + x f(s) X(1) + x g(s) X(sq),

e(s) = syq/(1 - syq),    f(s) = sq/(1 - sq),    g(s) = -sq(1 - y) / ((1 - sq)(1 - syq))
```

This is the shape of the paper's Lemma 2.3, "X(s) = xe(s) + xf(s)X(1) + xg(s)X(sq)", with no `X'(1)` term.[^3] The paper says the derivative term "only occurs when construction C is used", which is not needed for directed polygons.[^4] Castles are directed (every cell can be reached from the bottom-left cell by north and east steps), and the castle equation above indeed has no derivative term.

At `y = 1`, `g = 0` and the equation reads `X(1) = x q/(1 - q) (1 + X(1))`. At `x = 1` that gives `X(1) = q/(1 - 2q)`, the `2^(n-1)` compositions of [[castle-by-area](pages/castle-by-area.md)].

## Lemma 2.3 gives the q-Bessel closed form

Lemma 2.3 gives `X(1) = E(1)/(1 - F(1))`, where `E(s) = sum_{n≥0} x^(n+1) g(s)g(sq)...g(sq^(n-1)) e(sq^n)`, and `F` is the same sum with `f` in place of `e`.[^3] For castles the product of `g`'s closes up:

```
g(1) g(q) ... g(q^(n-1)) = (-(1 - y))^n q^C(n+1,2) / ((q)_n (yq)_n)

E(1) = sum_{n≥0} (-1)^n (1 - y)^n y x^(n+1) q^C(n+2,2) / ((q)_n (yq)_(n+1))
1 - F(1) = 1 - sum_{n≥0} (-1)^n (1 - y)^n x^(n+1) q^C(n+2,2) / ((q)_(n+1) (yq)_n)
```

Rename the variables of [[castle-q-bessel-closed-form](pages/castle-q-bessel-closed-form.md)] to match (its `u` is width, here `x`, and its `x` is blocks, here `y`). Then `1 - F(1)` equals that page's `M` term by term, and `E(1)` equals its `N - M`. So `X(1) = (N - M)/M = N/M - 1`, which is its castle generating function (GF). The tower-grammar route there and the add-a-column route here give the same series, and the step from the linear equation to the closed form is exactly Lemma 2.3. At `x = 1, y = -1` the denominator `1 - F(1)` vanishes at `q_0 = -0.6158281351848...`, which is the signed pole of [[castle-row-raising-equation](pages/castle-row-raising-equation.md)].

The paper's parallelogram equation (Lemma 3.1) has the same shape, `P(s) = xstyq/(1 - styq) + xsyq/((1 - sq)(1 - syq)) (P(1) - P(sq))`.[^5] The two equations differ only in which placements they allow and which of them add height. That is why the same `J_0`-type denominators appear in both.

## Castles against A001169

A001169 counts column-convex polyominoes by area. By rotation it also counts the horizontally convex ones ([[horizontally-convex-polyomino](pages/horizontally-convex-polyomino.md)]). The classical proofs weight a height-`s` column next to a height-`r` column by `r + s - 1`: "a(r,n) = SUM (r+s-1) a(s,n-r)".[^6] That weight is the number of vertical offsets at which two columns of those heights share an edge. A castle allows exactly one of those offsets, the one with both bottoms on row 1. So the comparison between the two recurrences comes down to their kernels:

| | column kernel `T[k, l]` | rank | GF by area | recurrence | growth |
|---|---|---|---|---|---|
| column-convex (A001169) | `k + l - 1` | 2 | `z(1 - z)^3 / (1 - 5z + 7z^2 - 4z^3)` | `a(n) = 5a(n-1) - 7a(n-2) + 4a(n-3)` | `3.20557` |
| castle (A011782) | `1` | 1 | `z/(1 - 2z)` | `a(n) = 2a(n-1)` | `2` |
| castle, block-signed | `(-1)^max(0, l-k)` | infinite | `E(1)/(1 - F(1))` above | q-shift equation only | `1.62383` |

The rank explains the rows. Write `a_l(z)` for the GF by last-column height `l`. A kernel `k + l - 1 = k · 1 + (l - 1) · 1` has rank 2, so `a_l = z^l (1 + S_1 - S_0 + l S_0)` depends on only two moments, `S_0 = sum a_k` and `S_1 = sum k a_k`. Solving the resulting 2 × 2 linear system gives the rational GF in the first row, and its expansion `1, 2, 6, 19, 61, 196, 629, 2017` is A001169.[^6] The castle kernel has rank 1, so `a_l = z^l (1 + S_0)` and the GF is geometric. The block weight `y^max(0, l-k)` depends on the sign of `l - k`, so no finite set of moments closes it. The equation stays a q-shift equation, and the signed count comes out as a quotient of q-series rather than from a finite linear system. Hickerson's order-3 recurrence and its characteristic root `3.2055694304` are the column-convex row of this table.[^7]

## The zoo sub-families inside the castles

The paper names Ferrers diagrams, stack polyominoes and parallelogram polyominoes as its classical directed-and-convex families, "characterized, in the set of convex polyominoes, by the fact that two or three vertices of the minimal bounding rectangle of the polyomino belong to the polyomino itself".[^8] A castle is a column-convex polyomino with every column bottom on row 1. Intersecting that condition with the column-sweep conditions on [[convex-polyomino](pages/convex-polyomino.md)] places each family:

| family | ∩ castles | castles of width `w`, height `h` | by area | blocks |
|---|---|---|---|---|
| column-convex | all castles | `h^w - (h-1)^w` | `2^(n-1)` | any |
| convex | stacks | `C(2h+w-3, w-1)` | A001523 | `h` |
| directed convex | stacks | `C(2h+w-3, w-1)` | A001523 | `h` |
| stack | stacks = [[convex-castle](pages/convex-castle.md)] | `C(2h+w-3, w-1)` | A001523 | `h` |
| parallelogram | reverse Ferrers `c_1 ≤ ... ≤ c_w` | `C(w+h-2, w-1)` | `p(n)` | `h` |
| Ferrers | Ferrers `c_1 ≥ ... ≥ c_w` | `C(w+h-2, w-1)` | `p(n)` | `h` |
| Ferrers ∪ reverse Ferrers | monotone castles | `2C(w+h-2, w-1) - 1` | `2p(n) - d(n)` | `h` |

The conditions reduce in each row as follows. Fixed bottoms make "bottoms rise" and "bottoms fall then rise" automatic, so directed convex and convex collapse onto stacks, and parallelograms (tops rising) collapse onto reverse Ferrers. The parallelogram polyomino is therefore not a castle sub-family in any larger sense. It enters the castles as a building block instead: castles are a sequence of parallelograms under a change of variables ([[castle-q-bessel-closed-form](pages/castle-q-bessel-closed-form.md)]). Every family in the table after the first is row-convex, so its block count is its height `h`, and the parity clause becomes height parity.

Each restriction is a restriction of the castle kernel, and Lemma 2.3 solves each one. Ferrers allows only `m ≥ k` for the new first column, so `X(s) = xsyq/(1 - syq) + x/(1 - syq) X(sq)`, with `f = 0`, and Lemma 2.3 gives

```
Ferrers castles = sum_{k≥1} x^k y q^k / (yq)_k       (x width, y blocks = height, q area)
```

At `y = 1` this is Euler's `sum q^k/(q)_k` for partitions. Stacks are the two-phase kernel, whose area GF is on [[stack-polyomino-gf](pages/stack-polyomino-gf.md)].

**Monotone castles.** A castle that is Ferrers or reverse Ferrers is a composition that is weakly increasing or weakly decreasing. Both at once means constant, which gives `d(n)` compositions of `n`. So the count by area is `2p(n) - d(n)`:

```
1, 2, 4, 7, 12, 18, 28, 40, 57, 80, 110, 148, 200, 266, 348, 457, 592, 764, 978, 1248      (n = 1..20)
```

These are the terms of A329398, defined through Lyndon and co-Lyndon factorizations of compositions. OEIS gives the "either weakly increasing or weakly decreasing" reading and the formula `2 * A000041(n) - A000005(n)` only as a conjecture.[^9] The formula for the monotone count itself is the two-line inclusion-exclusion above. Its agreement with A329398 is checked through `n = 20` and not proved here, so this is an interlink. The complement, non-monotone castles, is A332834 by that sequence's own name.[^9]

With the block sign, a Ferrers castle has sign `(-1)^h`, and a rectangle of height `d` has sign `(-1)^d`. Conjugation gives `(-1)^n A000700(n)` for each orientation ([[convex-polyomino-by-area](pages/convex-polyomino-by-area.md)]), so

```
even(n) - odd(n) = 2(-1)^n A000700(n) - sum_{d|n} (-1)^d
                 = -1, 0, 0, 1, 0, 2, 0, 2, -1, 4, -2, 4, -4, 6, -4, 7, -8, 10, -10, 12      (n = 1..20)
```

OEIS has no match for this signed row or for its absolute values (searched 2026-09-23), so it is a novel candidate.

## Related

- [[column-convex-polygon-enumeration](pages/column-convex-polygon-enumeration.md)] - the framework and Lemma 2.3.
- [[castle-q-bessel-closed-form](pages/castle-q-bessel-closed-form.md)] - the same closed form from the tower-word grammar.
- [[column-convex-ladder-by-area](pages/column-convex-ladder-by-area.md)] - the paper's other families read at `y = ±1`, with castles inside the directed column-convex rung.
- [[counting-horizontally-convex-polyominoes](pages/counting-horizontally-convex-polyominoes.md)], [[horizontally-convex-polyomino](pages/horizontally-convex-polyomino.md)] - A001169 and the Temperley weight.
- [[convex-polyomino](pages/convex-polyomino.md)], [[convex-polyomino-by-area](pages/convex-polyomino-by-area.md)] - the corner taxonomy and the area ladder the sub-family table intersects.
- [[castle-classification-shape](pages/castle-classification-shape.md)] - Ferrers and reverse Ferrers as castle shape types.
- [[prellberg-brak-1995-cluster-models](pages/prellberg-brak-1995-cluster-models.md)] - the quadratic bar-graph equation for the same GF.

## Footnotes

[^1]: Verified by execution, 2026-09-23. Lemma 2.3's `E(1)/(1 - F(1))` for the castle equation was expanded with exact integer power-series arithmetic and matched brute-force enumeration of compositions by (width, blocks) at every area `n ≤ 18`. Its `y = -1` row reproduces `even(n) - odd(n)` of [[castle-row-raising-equation](pages/castle-row-raising-equation.md)] through `n = 18`. The identities `1 - F(1) = M` and `E(1) = N - M` were checked at four random points of `(-0.9, 0.9)^3` to `10^-30`, and the root of `1 - F(1)` at `x = 1, y = -1` was found at `-0.615828135184805773627625720698`. The rank-2 system was solved symbolically and expands to A001169 through `z^8`. The `(w, h)` counts in the sub-family table were checked by enumerating all skylines for `w, h ≤ 7`, together with blocks `= h` on every Ferrers, reverse Ferrers and stack castle. The Ferrers GF was checked by (area, height) through area 14, and the monotone and signed monotone rows through `n = 20`.
[^2]: [[column-convex-polygon-enumeration](pages/column-convex-polygon-enumeration.md)] p.4 §2 [synthesis] L178-254 - the construction glues columns one at a time and tracks left height, right height, width, vertical perimeter and area by `s, t, x, y, q`; Proposition 2.1 splits the new column into cases A, B, C by the relative position of its top and bottom cells.
[^3]: [[column-convex-polygon-enumeration](pages/column-convex-polygon-enumeration.md)] p.9-10 Lemma 2.3 L459-475 - "Suppose that X(s) = xe(s) + xf(s)X(1) + xg(s)X(sq) ... Then X(1) = E(1)/(1 - F(1)), where E(s) = Σ_{n≥0} x^{n+1} g(s)g(sq)...g(sq^{n-1}) e(sq^n) and F(s) = Σ_{n≥0} x^{n+1} g(s)g(sq)...g(sq^{n-1}) f(sq^n)" (sums read from the PDF; the OCR layer garbles them).
[^4]: [[column-convex-polygon-enumeration](pages/column-convex-polygon-enumeration.md)] p.9 §2.2 L453-457 - "this partial derivative only occurs when construction C is used. Looking at Fig. 6 suggests that this construction is not needed as soon as the class of polygons under consideration is formed with directed polygons. So, in all these cases, we shall apply the following simplified version of Lemma 2.2."
[^5]: [[column-convex-polygon-enumeration](pages/column-convex-polygon-enumeration.md)] p.11 Lemma 3.1 L541-578 - "P(s) = xstyq/(1 - styq) + xsyq/((1-sq)(1-syq)) (P(1) - P(sq))".
[^6]: [[counting-horizontally-convex-polyominoes](pages/counting-horizontally-convex-polyominoes.md)] p.2 §0 - "the function a(r,n), which is the number of horizontally convex n-ominoes with exactly r squares in the top row ... a(r,n) = SUM (r+s-1) a(s,n-r)"; p.1 §0 table "a(n) 1 2 6 19 61 196 629 2017 6466 20727 66441 212980".
[^7]: [[counting-horizontally-convex-polyominoes](pages/counting-horizontally-convex-polyominoes.md)] p.1-2 §0 - "Theorem: For n ≥ 5, a(n) = 5 a(n-1) - 7 a(n-2) + 4 a(n-3)" and "v = 3.2055694304... is the unique real root of v^3 - 5 v^2 + 7 v - 4 = 0".
[^8]: [[column-convex-polygon-enumeration](pages/column-convex-polygon-enumeration.md)] p.3 §1 L131-135 - "three very classical families of directed and convex polyominoes: Ferrers diagrams, stack polyominoes, and parallelogram (or staircase) polyominoes. As Fig. 3 shows, each of these subsets can be characterized, in the set of convex polyominoes, by the fact that two or three vertices of the minimal bounding rectangle of the polyomino belong to the polyomino itself."
[^9]: https://oeis.org/A329398 (fetched 2026-09-23) - "Number of compositions of n with uniform Lyndon factorization and uniform co-Lyndon factorization", data "1, 2, 4, 7, 12, 18, 28, 40, 57, 80, 110, 148, 200, 266, 348, 457, 592, 764, 978, 1248, ..."; "Conjecture: Also the number of compositions of n that are either weakly increasing or weakly decreasing. Hence a(n) = 2 * A000041(n) - A000005(n)"; cross-reference "A332834 Number of compositions of n that are neither weakly increasing nor weakly decreasing."
