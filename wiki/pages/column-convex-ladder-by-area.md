---
title: The column-convex ladder by area - Bousquet-Mélou 1996 read at y = 1 and y = -1, with castles located on it
category: Analyses
summary: "Bousquet-Mélou's 1996 closed forms for stacks, parallelograms, directed convex, directed column-convex and column-convex polyominoes, evaluated at unit width weight with the vertical half-perimeter variable y at 1 and at -1, and checked against a column sweep. At y = 1 they give A001523, A006958, A067676, F_(2n-1) = A001519 and A001169. Castles (2^(n-1)) are the directed column-convex polyominoes with a flat bottom, so they sit inside F_(2n-1) inside A001169, with growth 2 < phi^2 < 3.20557. At y = -1 the variable is the PE 502 block sign on castles and the height sign on row-convex shapes. The signed directed column-convex count is -0.009058018 (-1.7300884)^n, the signed column-convex count is 4.12460e-5 (-2.2475612)^n, and castles are 0.0985 (-1.62383)^n; the two new signed rows have no OEIS match. The paper's stack polygons lie on their side, so at y = -1 its stack formula signs stacks by width."
tags: [analysis, polyomino, column-convex, directed-column-convex, area, perimeter, parity, sign, q-series, castle, stack-polyomino, parallelogram-polyomino, directed-convex, oeis, asymptotics, novel-candidate, verification]
sources: [column-convex-polygon-enumeration]
created: 2026-09-23
updated: 2026-09-23
---

# The column-convex ladder by area

[[column-convex-polygon-enumeration](pages/column-convex-polygon-enumeration.md)] gives closed forms for six column-convex families, graded by left height `s`, right height `t`, width `x`, vertical half-perimeter `y` and area `q`.[^1] This page sets `s = t = x = 1` and reads the area series at `y = 1` and at `y = -1`. At `y = 1` it locates the castles on the ladder. At `y = -1` it carries the Project Euler 502 parity clause up the ladder, because on a castle the vertical half-perimeter is the block count ([[castle-perimeter](pages/castle-perimeter.md)]). On a row-convex shape it is the height ([[convex-polyomino](pages/convex-polyomino.md)]).

[[convex-polyomino-by-area](pages/convex-polyomino-by-area.md)] already holds the convex rungs, from Bousquet-Mélou and Fédou 1995 and a column sweep. What is new here is the directed column-convex rung, which is the family directly above the castles, and a signed row for it and for the column-convex rung. The convex Theorem 4.4 needs the derivative `E'(1)` and was not evaluated; its rung comes from the 1995 series on that page.

Every number below is own computation, from the paper's formulas and checked against an independent enumerator (footnote 2).

## At y = 1: the area ladder, and where castles sit

| family | 1996 result | area GF at `y = 1` | first terms | OEIS | growth |
|---|---|---|---|---|---|
| stack | Lemma 2.5 | `sum_k q^k / ((q)_(k-1)^2 (1 - q^k))` | 1, 2, 4, 8, 15, 27, 47, 79 | A001523 | subexponential |
| parallelogram | Theorem 3.2 | `J_1/J_0` | 1, 2, 4, 9, 20, 46, 105, 242 | A006958 | `2.30914` |
| directed convex | Theorem 3.4 | `M_1/J_0` | 1, 2, 5, 13, 33, 82, 200, 481 | A067676 | `2.30914` |
| **castle** (bar graph) | none | `q/(1 - 2q)` | 1, 2, 4, 8, 16, 32, 64, 128 | A011782 | `2` |
| directed column-convex | Theorem 3.6 | `q(1 - q)/(1 - 3q + q^2)` | 1, 2, 5, 13, 34, 89, 233, 610 | A001519 | `φ^2 = 2.61803` |
| column-convex | Theorem 4.8 | `q(1 - q)^3/(1 - 5q + 7q^2 - 4q^3)` | 1, 2, 6, 19, 61, 196, 629, 2017 | A001169 | `3.20557` |

The paper states the last two GFs itself: "the area generating function is DV(1,1,1,1,q) = q(1 - q)/(1 - 3q + q^2)", a result of Delest and Dulucq, and "V(1,1,1,1,q) = q(1 - q)^3/(1 - 5q + 7q^2 - 4q^3)".[^3] Both are rational, and the paper derives that from its theorems.

**Castles sit inside the directed column-convex rung.** A polyomino is directed column-convex when every column is one interval and every cell can be reached from the bottom-left cell by north and east steps. In a column sweep that means each new column's bottom lies between the previous column's bottom and top. A castle is the case where every bottom is on row 1. So the chain is

```
stacks (A001523)  ⊂  castles (2^(n-1))  ⊂  directed column-convex (F_(2n-1))  ⊂  column-convex (A001169)
```

with growth rising from subexponential through `2` and `φ^2` to `3.20557`. On the castle side, [[castle-by-area](pages/castle-by-area.md)] splits the castles into stacks (A001523) and non-convex castles (A115981). The valley castles (A332578) are not one of the paper's classes: their tops fall and then rise, so they are directed column-convex but not convex.

Directed column-convex polyominoes by area and convex castles by semi-perimeter are both A001519 ([[castle-perimeter](pages/castle-perimeter.md)]). This page does not construct a bijection between them.

## At y = -1: the parity clause on every rung

At `y = -1` each GF becomes `sum (-1)^v(P) q^area`, where `2v(P)` is the number of vertical steps of the perimeter.[^1] On castles this is `even(n) - odd(n)` by blocks. On parallelograms and directed convex polyominoes it is the height sign of [[convex-polyomino-by-area](pages/convex-polyomino-by-area.md)], and those rows agree with that page's table.

| n | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| castle | -1 | 0 | 0 | 2 | 0 | 2 | -4 | 2 | -12 | 10 | -20 | 38 | -44 | 98 | -136 | 230 | -388 | 582 | -1008 | 1590 |
| directed column-convex | -1 | 0 | 1 | 1 | 0 | -3 | -3 | 0 | 7 | 5 | 6 | -15 | -5 | -28 | 45 | -27 | 128 | -195 | 229 | -584 |
| column-convex | -1 | 0 | 2 | 1 | -5 | -8 | 3 | 31 | 30 | -59 | -145 | 0 | 383 | 467 | -610 | -2023 | -509 | 5288 | 6939 | -5577 |
| stack, signed by width | -1 | 0 | 0 | 0 | 1 | -1 | 1 | -1 | 2 | -3 | 2 | -2 | 4 | -5 | 3 | -4 | 8 | -8 | 6 | -8 |

The castle row is from [[castle-row-raising-equation](pages/castle-row-raising-equation.md)], and the sweep here reproduces it. For the first three rows the signed GF is a quotient of q-series whose denominator has a simple real zero closest to the origin, so each of them grows like a constant times `(-1/q_0)^n`:

| family | `q_0` | signed growth | constant | unsigned growth |
|---|---|---|---|---|
| castle | `-0.6158281352` | `1.62383` | `0.0985` | `2` |
| directed column-convex | `-0.5780051505` | `1.7300884` | `-0.009058018` | `2.61803` |
| column-convex | `-0.4449266995` | `2.2475612` | `4.12460e-5` | `3.20557` |

For directed column-convex, `q_0` is a zero of Theorem 3.6's denominator `L_0(1)`. Its next zeros are a complex pair of modulus `0.779`. For column-convex, `q_0` is a zero of Theorem 4.8's `1 + W + yX`, whose next zeros are a complex pair of modulus `0.594`. The column-convex constant is small, and the second pole is close behind, so the ratios `a(n+1)/a(n)` wander for a long time. `a(n) q_0^n` settles to `4.1246e-5` only from about `n = 70`. On all three rungs the signed count grows more slowly than the unsigned count, so even and odd are equinumerous to leading order. Relative to its own size the castle is the least balanced of the three (`1.624/2 = 0.81`) and directed column-convex the most (`0.66`), with column-convex at `0.70`.

The directed column-convex and column-convex signed rows, their absolute values, and the stack-by-width row have no OEIS match (searched 2026-09-23). They are novel candidates.

**The paper's stacks lie on their side.** Lemma 2.4 builds every stack polygon of width at least 2 by construction A, which extends the new first column both above and below the old one.[^4] So the paper's stacks are nested columns shrinking away from a base column on the left, a quarter turn from the upright stacks of [[convex-castle](pages/convex-castle.md)]. The area count is the same, but `v(P)` of the paper's stack is the width of the upright stack. At `y = -1`, Lemma 2.5 therefore gives the width-signed row above: stacks signed by number of parts, which is unimodal compositions signed by length. The height-signed stack row is on [[convex-polyomino-by-area](pages/convex-polyomino-by-area.md)].

## Related

- [[column-convex-polygon-enumeration](pages/column-convex-polygon-enumeration.md)] - the six closed forms.
- [[castle-add-a-column-equation](pages/castle-add-a-column-equation.md)] - the castle's own Lemma 2.3 equation, and the sub-family intersections.
- [[convex-polyomino-by-area](pages/convex-polyomino-by-area.md)] - the convex rungs, the growth constant `2.30914`, and the height-signed rows.
- [[castle-by-area](pages/castle-by-area.md)], [[castle-row-raising-equation](pages/castle-row-raising-equation.md)] - the castle rung and its signed asymptotics.
- [[castle-perimeter](pages/castle-perimeter.md)] - blocks as the vertical half-perimeter, and A001519 as convex castles by semi-perimeter.
- [[castle-q-bessel-closed-form](pages/castle-q-bessel-closed-form.md)] - the castle's `q_0` as the first zero of its own q-Bessel denominator.

## Footnotes

[^1]: [[column-convex-polygon-enumeration](pages/column-convex-polygon-enumeration.md)] p.4-5 §2 L196-205 - "the number of horizontal (resp. vertical) steps in its perimeter by 2w(P) (resp. 2v(P)) (note that w(P) is the width of P), its area by a(P)"; the generating function is `Σ s^ℓ(P) t^r(P) x^w(P) y^v(P) q^a(P)` (read from the PDF; the OCR layer garbles it).
[^2]: Verified by execution, 2026-09-23. The Lemma 2.5, Theorem 3.2, 3.4, 3.6 and 4.8 series were expanded in exact rational arithmetic at `s = t = x = 1`. At `y = 1` the stack, parallelogram and directed-convex series match A001523, A006958 and A067676 through area 16. In Theorem 3.4's series (7) the exponent that the scan leaves unclear is `q^C(m,2)`, the value that reproduces A067676 (`q^C(m+1,2)` gives `1, 3, 8, 21, ...`). The independent check is a column sweep over (last-column height, offset) that counts vertical perimeter edges directly, with bottoms fixed (castles), bottoms rising within the previous column (directed column-convex), or any overlapping offset (column-convex). At `y = 1` it gives `2^(n-1)`, `F_(2n-1)` and A001169 through area 14. At `y = -1` and `y = 2` it agrees with Theorems 3.6 and 4.8 at every area through 12, and on castles it reproduces the signed row of [[castle-row-raising-equation](pages/castle-row-raising-equation.md)]. The unimodal-compositions-by-length sign matches Lemma 2.5 at `y = -1` through area 16. Signed rows were extended to area 90 from the theorems. The poles come from [m/m] Padé approximants, stable to 10 digits between `m = 30` and `m = 40`, and they agree with the zeros of the truncated denominators `L_0` and `1 + W + yX`. The constants are `a(n) q_0^n` at `n = 80..90`.
[^3]: [[column-convex-polygon-enumeration](pages/column-convex-polygon-enumeration.md)] p.14 Remark (1) after Theorem 3.6 L748-759 - "the generating function for directed column-convex polygons, counted according to their left height, right height, width and area is a rational function. In particular, the area generating function is DV(1,1,1,1,q) = q(1-q)/(1-3q+q²). This result was proved by Delest and Dulucq"; p.24 Remark (2) after Theorem 4.8 L1342-1350 - "the generating function for column-convex polygons according to their left height, right height, width and area is a rational function. In particular, the area generating function is V(1,1,1,1,q) = q(1-q)³/(1-5q+7q²-4q³)" (formulas read from the PDF).
[^4]: [[column-convex-polygon-enumeration](pages/column-convex-polygon-enumeration.md)] p.6 §2.1 L276-281 and p.10 Lemma 2.4 L502-511 - construction A: "We first duplicate the leftmost column of P ... Then, we glue two pieces of columns, the first one at the top of the new column, the other one at its bottom. This corresponds to a multiplication by 1/(1 - syq)²"; "Applying construction A to the set of stack polygons provides all the stack polygons of width at least 2."
