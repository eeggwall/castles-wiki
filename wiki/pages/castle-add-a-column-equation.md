---
title: Castles in the add-a-column framework - the Lemma 2.3 equation, the column kernel, and the classical sub-families
category: Analyses
summary: "Adding a first column to a castle and recording its height s gives the equation X(s) = xsyq/(1-syq) + x sq/(1-sq) X(1) - x sq(1-y)/((1-sq)(1-syq)) X(sq) of Bousquet-Melou's add-a-column method, with x width, y blocks, q area. It has no derivative term, so Lemma 2.3 solves it, and its E(1) and 1 - F(1) are term for term the N - M and M of the q-Bessel closed form. Against A001169 the castle keeps 1 of the r + s - 1 placements of a column next to a column: a column kernel of rank 1 (2^(n-1) castles of area n) against rank 2 (the order-3 recurrence of A001169); the block weight y^max(0, l-k) has full rank on every section computed. Castles meet the convex, directed convex and stack polyominoes in the stacks, and the parallelogram polyominoes in the weakly increasing skylines. Monotone castles by area are 2p(n) - d(n) = A329398(n), and their signed count is 2(-1)^n A000700(n) - sum_{d|n} (-1)^d."
tags: [analysis, castle, polyomino, column-convex, add-a-column, functional-equation, q-shift, area, blocks, ferrers, stack-polyomino, parallelogram-polyomino, transfer-matrix, oeis, parity]
sources: [column-convex-polygon-enumeration, counting-horizontally-convex-polyominoes]
created: 2026-09-23
updated: 2026-10-23
---

# Castles in the add-a-column framework

[[column-convex-polygon-enumeration](pages/column-convex-polygon-enumeration.md)] (Bousquet-Mélou 1996) turns a column-convex class into a q-shift equation by gluing columns one at a time. Castles are column-convex ([[castle-polyomino](pages/castle-polyomino.md)]), but the paper does not treat them as one of its classes. This page writes the castle equation in the paper's notation, solves it with the paper's Lemma 2.3, compares its column kernel with the kernel `r + s − 1` behind A001169, and places the paper's classical sub-families (Ferrers diagrams, stack and parallelogram polyominoes) among the castles. The castle equation and its consequences are derived on this page and checked by execution;[^1] the framework and the lemma are the paper's.

## The castle equation

Use the paper's variables: `x` marks width, `y` the vertical half-perimeter, `q` area, and `s` the height of the first column.[^2] On a castle the vertical half-perimeter is the block count ([[castle-perimeter](pages/castle-perimeter.md)]), so `y` marks blocks. Let `X(s) = X(s, x, y, q)` count the nonempty castles, of any height and any block parity.

Put a new first column of height `m` in front of a castle whose first column has height `k`. Both bottoms are on row 1. The new column adds `m` cells and one unit of width, and it adds `max(0, m − k)` blocks, because the block count is the total ascent of the skyline with `c_0 = 0`. Summing over `m`:

- `m ≤ k` gives `Σ_{m=1}^{k} (sq)^m = sq (1 − (sq)^k)/(1 − sq)`, the term `x sq/(1 − sq) (X(1) − X(sq))`;
- `m > k` gives `Σ_{m>k} (sq)^m y^{m−k} = (sq)^k syq/(1 − syq)`, the term `x syq/(1 − syq) X(sq)`.

A single column of height `m` has weight `x (syq)^m`. Collecting terms:

```
X(s) = x e(s) + x f(s) X(1) + x g(s) X(sq),                                   (1)

e(s) = syq/(1 − syq),    f(s) = sq/(1 − sq),    g(s) = −sq(1 − y) / ((1 − sq)(1 − syq))
```

This is the shape of the paper's Lemma 2.3, "X(s) = xe(s) + xf(s)X(1) + xg(s)X(sq)", with no `X′(1)` term.[^3] The paper says the derivative term "only occurs when construction C is used", which is not needed for directed polygons.[^4] Castles are directed (every cell can be reached from the bottom-left cell by north and east steps), and Equation (1) has no derivative term.

At `y = 1`, `g = 0` and Equation (1) reads `X(1) = x q/(1 − q) (1 + X(1))`. At `x = 1` that gives `X(1) = q/(1 − 2q)`, the `2^{n−1}` castles of area `n`, A011782(n) for `n ≥ 1` ([[castle-by-area](pages/castle-by-area.md)]).

## Lemma 2.3 gives the q-Bessel closed form

Lemma 2.3 gives `X(1) = E(1)/(1 − F(1))`, where `E(s) = Σ_{n≥0} x^{n+1} g(s) g(sq) ⋯ g(sq^{n−1}) e(sq^n)`, and `F` is the same sum with `f` in place of `e`.[^3] (These `E` and `F` are the lemma's, not the tower generating function `E_k(x)` or the old name `F(w, h)`.) For castles the product of `g`'s closes up, with `(a)_n = (1 − aq)(1 − aq²) ⋯ (1 − aq^n)`:

```
g(1) g(q) ⋯ g(q^{n−1})  =  (−(1 − y))^n q^{C(n+1,2)} / ((1)_n (y)_n)

E(1)      =  Σ_{n≥0} (−1)^n (1 − y)^n y x^{n+1} q^{C(n+2,2)} / ((1)_n (y)_{n+1})
1 − F(1)  =  1 − Σ_{n≥0} (−1)^n (1 − y)^n x^{n+1} q^{C(n+2,2)} / ((1)_{n+1} (y)_n)
```

Rename the variables of [[castle-q-bessel-closed-form](pages/castle-q-bessel-closed-form.md)] to match (its `u` is width, here `x`, and its `x` is blocks, here `y`). Then `1 − F(1)` equals that page's `M` term by term, and `E(1)` equals its `N − M`. So `X(1) = (N − M)/M = N/M − 1`, the castle generating function there. The tower-grammar route there and the add-a-column route here give the same series, and the step from the linear equation to the closed form is Lemma 2.3. At `x = 1, y = −1` the denominator `1 − F(1)` vanishes at `q_0 = −0.6158281351848…`, the pole of the signed count on [[castle-row-raising-equation](pages/castle-row-raising-equation.md)].

The paper's equation for parallelogram polyominoes (Lemma 3.1) has the same shape, `Π(s) = xstyq/(1 − styq) + xsq/((1 − sq)(1 − syq)) (Π(1) − Π(sq))`, where `Π` is the paper's `P`.[^5] The two equations differ in which placements of the new column they allow and in which placements add to the vertical half-perimeter, and Lemma 2.3 solves both.

## Castles against A001169

A001169 counts the column-convex polyominoes by area, and by a quarter turn the horizontally convex ones ([[horizontally-convex-polyomino](pages/horizontally-convex-polyomino.md)]). The classical proofs count by the length of the top row with the weight `r + s − 1`: "a(r,n) = SUM (r+s-1) a(s,n-r)", "since we may add a row of r squares to the top of a polyomino counted by a(s,n-r) in exactly r+s-1 ways".[^6] In column terms, `r + s − 1` is the number of vertical offsets at which a column of height `r` and a column of height `s` share an edge. A castle allows exactly one of those offsets, the one with both bottoms on row 1. So the two recurrences differ in their kernels:

| | column kernel `T[k, l]` | rank | generating function by area | recurrence | growth |
|---|---|---|---|---|---|
| column-convex (A001169) | `k + l − 1` | 2 | `z(1 − z)^3 / (1 − 5z + 7z^2 − 4z^3)` | `a(n) = 5a(n−1) − 7a(n−2) + 4a(n−3)` | `3.20557` |
| castle (A011782) | `1` | 1 | `z/(1 − 2z)` | `a(n) = 2a(n−1)` | `2` |
| castle, block-signed | `(−1)^{max(0, l−k)}` | full on every section computed | `E(1)/(1 − F(1))` at `y = −1` | q-shift equation | `1.62383` |

Write `a_l(z)` for the generating function by last-column height `l`. The kernel `k + l − 1 = k · 1 + (l − 1) · 1` has rank 2, so `a_l = z^l (1 + S_1 + (l − 1) S_0)` depends on two moments, `S_0 = Σ_k a_k` and `S_1 = Σ_k k a_k`. Solving the resulting 2 × 2 linear system gives the rational generating function in the first row, whose expansion `1, 2, 6, 19, 61, 196, 629, 2017` is A001169.[^6] The castle kernel has rank 1, so `a_l = z^l (1 + S_0)` and the generating function is geometric. The block weight `y^{max(0, l−k)}` takes one value above the diagonal and another below it, and its `n × n` sections have rank `n` for every `n ≤ 10` at `y = −1` and at `y = 2` (computed), so the moment reduction gives no finite linear system; the signed count is the quotient of q-series of the previous section. The column-convex row is Hickerson's recurrence (0.0), with characteristic root `3.2055694304` ([[counting-horizontally-convex-polyominoes](pages/counting-horizontally-convex-polyominoes.md)]).[^7]

## The classical sub-families among the castles

The paper names Ferrers diagrams, stack polyominoes and parallelogram polyominoes as "three very classical families of directed and convex polyominoes", each "characterized, in the set of convex polyominoes, by the fact that two or three vertices of the minimal bounding rectangle of the polyomino belong to the polyomino itself".[^8] A castle is a column-convex polyomino with every column bottom on row 1. Intersecting that condition with the column conditions on [[convex-polyomino](pages/convex-polyomino.md)] places each family:

| family | ∩ castles | castles of width `w`, height `h` | by area | blocks |
|---|---|---|---|---|
| column-convex | all castles | `h^w − (h−1)^w` | `2^{n−1}` | any |
| convex | stacks | `C(2h+w−3, w−1)` | A001523 | `h` |
| directed convex | stacks | `C(2h+w−3, w−1)` | A001523 | `h` |
| stack | stacks = [[convex-castle](pages/convex-castle.md)] | `C(2h+w−3, w−1)` | A001523 | `h` |
| parallelogram | weakly increasing skylines `c_1 ≤ ⋯ ≤ c_w` | `C(w+h−2, w−1)` | `p(n)` | `h` |
| Ferrers | weakly decreasing skylines `c_1 ≥ ⋯ ≥ c_w` | `C(w+h−2, w−1)` | `p(n)` | `h` |
| Ferrers ∪ parallelogram | monotone castles | `2C(w+h−2, w−1) − 1` | `2p(n) − d(n)` | `h` |

Here `p(n)` is the number of partitions of `n` and `d(n)` the number of divisors. With the column bottoms fixed, the conditions on the bottoms ("bottoms rise", "bottoms fall then rise") hold automatically, so the directed convex and convex castles are the stacks, and the parallelogram castles (tops weakly rising) are the weakly increasing skylines. The parallelogram polyominoes enter the castles as a building block instead: castles are a sequence of parallelograms under a change of variables ([[castle-q-bessel-closed-form](pages/castle-q-bessel-closed-form.md)]). Every family in the table after the first is row-convex, so its castles have `h` blocks, and the parity of the block count is the parity of the height.

Each family restricts the castle kernel, and Lemma 2.3 solves each one. A Ferrers castle allows only `m ≥ k` for the new first column, so `X(s) = xsyq/(1 − syq) + x/(1 − syq) X(sq)`, with `f = 0`, and Lemma 2.3 gives

```
Ferrers castles  =  Σ_{k≥1} x^k y q^k / (y)_k        (x width, y blocks = height, q area)       (2)
```

At `y = 1` this is Euler's `Σ q^k/(q; q)_k` for partitions. Stacks are the two-phase kernel, whose area generating function is on [[stack-polyomino-gf](pages/stack-polyomino-gf.md)].

**Monotone castles.** A castle that is Ferrers or parallelogram is a composition that is weakly decreasing or weakly increasing. Both at once means constant, which gives `d(n)` compositions of `n`. So the count by area is `2p(n) − d(n)`:

```
1, 2, 4, 7, 12, 18, 28, 40, 57, 80, 110, 148, 200, 266, 348, 457, 592, 764, 978, 1248      (n = 1..20)
```

This is A329398, "Number of compositions of n with uniform Lyndon factorization and uniform co-Lyndon factorization". The entry states and proves that these are exactly the compositions that are weakly increasing or weakly decreasing, so `A329398(n) = 2p(n) − d(n)`.[^9] The complement, the non-monotone castles, is A332834 by that sequence's name.[^9]

With the block sign, a Ferrers castle of height `h` has sign `(−1)^h`, and a rectangle of height `d` has sign `(−1)^d`. By conjugation, the Ferrers castles of area `n` have signed sum `(−1)^n A000700(n)`, with `A000700(n)` the partitions of `n` into distinct odd parts ([[convex-polyomino-by-area](pages/convex-polyomino-by-area.md)]), so

```
A^e − A^o over monotone castles of area n  =  2(−1)^n A000700(n) − Σ_{d|n} (−1)^d
                                           =  −1, 0, 0, 1, 0, 2, 0, 2, −1, 4, −2, 4, −4, 6, −4, 7, −8, 10, −10, 12      (n = 1..20)
```

## Related

- [[column-convex-polygon-enumeration](pages/column-convex-polygon-enumeration.md)] - the add-a-column method and Lemma 2.3, with the paper's `S`, `P`, `C` written `St`, `Π`, `Conv`.
- [[castle-q-bessel-closed-form](pages/castle-q-bessel-closed-form.md)] - the same closed form from the tower grammar.
- [[column-convex-ladder-by-area](pages/column-convex-ladder-by-area.md)] - the paper's other families at `y = ±1`, with castles inside the directed column-convex polyominoes.
- [[counting-horizontally-convex-polyominoes](pages/counting-horizontally-convex-polyominoes.md)], [[horizontally-convex-polyomino](pages/horizontally-convex-polyomino.md)] - A001169 and the weight `r + s − 1`.
- [[convex-polyomino](pages/convex-polyomino.md)], [[convex-polyomino-by-area](pages/convex-polyomino-by-area.md)] - the convex sub-families by bounding-box corners, and their counts by area.
- [[castle-classification-shape](pages/castle-classification-shape.md)] - Ferrers and reverse Ferrers skylines as castle shape types.
- [[prellberg-brak-1995-cluster-models](pages/prellberg-brak-1995-cluster-models.md)] - (3.11), the quadratic bar-graph equation for the same generating function.

## Footnotes

[^1]: Verified by execution (Python 3.11, 2026-10-16). `E(1)/(1 − F(1))` for Equation (1), expanded in exact rational arithmetic, matches the enumeration of compositions by width, blocks and area through area 11 at `(x, y) = (2, 3), (1, −1), (−3/2, 5/7)`; the `n × n` sections of `y^{max(0, l−k)}` have rank `n` for `n = 4, 7, 10` at `y = −1` and `y = 2`; `z(1 − z)³/(1 − 5z + 7z² − 4z³)` expands to `1, 2, 6, 19, 61, 196, 629, 2017, 6466`; Equation (2) matches the Ferrers castles by width, height and area through area 12; the monotone and signed monotone rows match enumeration through `n = 20`, and so do `2p(n) − d(n)` and `2(−1)^n A000700(n) − Σ_{d|n} (−1)^d`. From an earlier session (2026-09-23): `1 − F(1) = M` and `E(1) = N − M` at four random points of `(−0.9, 0.9)^3` to `10^{−30}`; the root of `1 − F(1)` at `x = 1, y = −1` at `−0.615828135184805773627625720698`; the `(w, h)` counts of the sub-family table for `w, h ≤ 7`, with `h` blocks on every Ferrers, increasing and stack castle.
[^2]: [[column-convex-polygon-enumeration](pages/column-convex-polygon-enumeration.md)] p.4 §2 [synthesis] L178-254 - the construction glues columns one at a time and tracks left height, right height, width, vertical half-perimeter and area by `s, t, x, y, q`; Proposition 2.1 splits the new column into cases A, B, C by the relative position of its top and bottom cells.
[^3]: [[column-convex-polygon-enumeration](pages/column-convex-polygon-enumeration.md)] pp.9-10 Lemma 2.3 L459-475 - "Suppose that X(s) = xe(s) + xf(s)X(1) + xg(s)X(sq) ... Then X(1) = E(1)/(1 - F(1)), where E(s) = Σ_{n≥0} x^{n+1} g(s)g(sq)...g(sq^{n-1}) e(sq^n) and F(s) = Σ_{n≥0} x^{n+1} g(s)g(sq)...g(sq^{n-1}) f(sq^n)" (sums read from the PDF; the OCR layer garbles them).
[^4]: [[column-convex-polygon-enumeration](pages/column-convex-polygon-enumeration.md)] p.9 §2.2 L453-457 - "this partial derivative only occurs when construction C is used. Looking at Fig. 6 suggests that this construction is not needed as soon as the class of polygons under consideration is formed with directed polygons. So, in all these cases, we shall apply the following simplified version of Lemma 2.2."
[^5]: [[column-convex-polygon-enumeration](pages/column-convex-polygon-enumeration.md)] p.11 Lemma 3.1 L541-578 [synthesis] - Lemma 3.1 for the parallelogram polyominoes, `Π(s) = xstyq/(1 − styq) + xsq/((1 − sq)(1 − syq)) (Π(1) − Π(sq))` as read from the PDF on that page; the coefficient `xsq` is also what the placement count gives (a new column of height `m` overlapping the old first column, of height `k`, in `j ≤ min(m, k)` rows extends the box by `m − j`, and `Σ_{j≤k} Σ_{m≥j} (sq)^m y^{m−j} = sq(1 − (sq)^k)/((1 − sq)(1 − syq))`).
[^6]: https://cs.uwaterloo.ca/journals/JIS/HICK2/chcp.html §0 (0.6) - "a(r,n) = SUM (r+s-1) a(s,n-r) for 1 ≤ r < n, since we may add a row of r squares to the top of a polyomino counted by a(s,n-r) in exactly r+s-1 ways", and the table "1 2 6 19 61 196 629 2017 6466 20727 66441 212980".
[^7]: https://cs.uwaterloo.ca/journals/JIS/HICK2/chcp.html §0 (0.0)-(0.3) - "Theorem: For n ≥ 5, a(n) = 5 a(n-1) - 7 a(n-2) + 4 a(n-3)" and "v = 3.2055694304... is the unique real root of v^3 - 5 v^2 + 7 v - 4 = 0".
[^8]: [[column-convex-polygon-enumeration](pages/column-convex-polygon-enumeration.md)] p.3 §1 L131-135 - "three very classical families of directed and convex polyominoes: Ferrers diagrams, stack polyominoes, and parallelogram (or staircase) polyominoes. As Fig. 3 shows, each of these subsets can be characterized, in the set of convex polyominoes, by the fact that two or three vertices of the minimal bounding rectangle of the polyomino belong to the polyomino itself."
[^9]: https://oeis.org/A329398 (read 2026-10-16) - "Number of compositions of n with uniform Lyndon factorization and uniform co-Lyndon factorization", data "1, 2, 4, 7, 12, 18, 28, 40, 57, 80, 110, 148, 200, 266, 348, 457, 592, 764, 978, 1248, ..."; "Theorem: a composition has a uniform Lyndon factorization and a uniform co-Lyndon factorization if and only if it is weakly increasing or weakly decreasing. This proves Wiseman's conjecture above" (Benjamin Schippers, Sep 18 2026), with the conjecture "Hence a(n) = 2 * A000041(n) - A000005(n)"; https://oeis.org/A332834 "Number of compositions of n that are neither weakly increasing nor weakly decreasing."
