---
title: The column-convex ladder by area
category: Analyses
summary: Bousquet-Mélou's 1996 generating functions for stack, parallelogram, directed convex, directed column-convex and column-convex polyominoes at s = t = x = 1, with the vertical half-perimeter variable y at 1 and at −1. At y = 1 they count by area A001523, A006958, A067676, A001519 = F_{2n−1} and A001169; the castles, 2^{n−1} of area n, are the directed column-convex polyominoes with every column on row 1, so stacks ⊂ castles ⊂ directed column-convex ⊂ column-convex, with growth by area subexponential, 2, φ² and 3.20557. At y = −1 the variable is the block sign on castles and the height sign on row-convex polyominoes; the signed counts are S_castle(n) ~ 0.0985 (−1.62383)^n, S_dcc(n) ~ −0.009058018 (−1.7300884)^n and S_cc(n) ~ 4.12460·10⁻⁵ (−2.2475612)^n (computed). The paper's stack polygons lie on their side, so at y = −1 its stack formula signs stacks by width.
tags: [analysis, polyomino, column-convex, directed-column-convex, area, perimeter, parity, sign, q-series, castle, stack-polyomino, parallelogram-polyomino, directed-convex, oeis, asymptotics, verification]
sources: [column-convex-polygon-enumeration]
created: 2026-09-23
updated: 2026-10-16
---

# The column-convex ladder by area

[[column-convex-polygon-enumeration](pages/column-convex-polygon-enumeration.md)] gives the generating functions of six column-convex families, with `s` and `t` marking the left and right heights, `x` the width, `y` the vertical half-perimeter `v(P)` (half the number of vertical edges of the perimeter) and `q` the area.[^1] This page sets `s = t = x = 1` and reads the area series at `y = 1` and at `y = −1`. On a castle the vertical half-perimeter is the block count ([[castle-perimeter](pages/castle-perimeter.md)]), so `y = −1` is the Project Euler 502 block sign; on a row-convex polyomino it is the height ([[convex-polyomino](pages/convex-polyomino.md)]). The convex family is on [[convex-polyomino-by-area](pages/convex-polyomino-by-area.md)], from Bousquet-Mélou and Fédou 1995 and a column sweep.

*Example.* The castle `(2, 1, 2)` has area 5, 3 blocks and 6 vertical perimeter edges (2 on the left, 1 and 1 at the inner boundaries, 2 on the right), so `v = 3`, and its weight at `y = −1` is `−1`.

## At y = 1: the area ladder

| family | 1996 result | area generating function at `y = 1` | first terms | OEIS | growth by area |
|---|---|---|---|---|---|
| stack | Lemma 2.5 | `Σ_k q^k / ((q; q)_{k−1}² (1 − q^k))` | 1, 2, 4, 8, 15, 27, 47, 79 | A001523 | subexponential |
| parallelogram | Theorem 3.2 | `J_1/J_0` | 1, 2, 4, 9, 20, 46, 105, 242 | A006958 | `2.30914` |
| directed convex | Theorem 3.4 | `M_1/J_0` | 1, 2, 5, 13, 33, 82, 200, 481 | A067676 | `2.30914` |
| castle | none | `q/(1 − 2q)` | 1, 2, 4, 8, 16, 32, 64, 128 | A011782 | `2` |
| directed column-convex | Theorem 3.6 | `q(1 − q)/(1 − 3q + q²)` | 1, 2, 5, 13, 34, 89, 233, 610 | `A001519(n) = F_{2n−1}` | `φ² = 2.61803` |
| column-convex | Theorem 4.8 | `q(1 − q)³/(1 − 5q + 7q² − 4q³)` | 1, 2, 6, 19, 61, 196, 629, 2017 | A001169 | `3.20557` |

The paper states the last two generating functions, which it writes `DV(1, 1, 1, 1, q)` and `V(1, 1, 1, 1, q)`, and credits the first to Delest and Dulucq.[^3]

**Castles inside the ladder.** A polyomino is directed column-convex when every column is one interval and every cell can be reached from the bottom-left cell by north and east steps. In a column sweep, each new column's bottom lies between the bottom and the top of the previous column. A castle is the case in which every bottom is on row 1. So

```
stacks (A001523)  ⊂  castles (2^{n−1})  ⊂  directed column-convex (F_{2n−1})  ⊂  column-convex (A001169),
```

with growth by area subexponential, `2`, `φ²` and `3.20557`. [[castle-by-area](pages/castle-by-area.md)] splits the castles into the convex castles (A001523) and the non-convex castles (A115981). The valley castles (A332578), whose tops fall and then rise, are directed column-convex and not convex, and are not one of the paper's families. The directed column-convex polyominoes by area and the convex castles by semi-perimeter are both counted by A001519 ([[castle-perimeter](pages/castle-perimeter.md)]).

## At y = −1: the block sign on every rung

At `y = −1` each generating function becomes `Σ (−1)^{v(P)} q^{area(P)}`.[^1] Write `S_castle(n)`, `S_dcc(n)` and `S_cc(n)` for the sums of `(−1)^{v(P)}` over the castles, the directed column-convex polyominoes and the column-convex polyominoes of area `n`. On castles, `S_castle(n)` is the even-block count minus the odd-block count. On parallelograms and directed convex polyominoes, `(−1)^{v(P)}` is the height sign, and those rows agree with [[convex-polyomino-by-area](pages/convex-polyomino-by-area.md)].

| `n` | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `S_castle(n)` | −1 | 0 | 0 | 2 | 0 | 2 | −4 | 2 | −12 | 10 | −20 | 38 | −44 | 98 | −136 | 230 | −388 | 582 | −1008 | 1590 |
| `S_dcc(n)` | −1 | 0 | 1 | 1 | 0 | −3 | −3 | 0 | 7 | 5 | 6 | −15 | −5 | −28 | 45 | −27 | 128 | −195 | 229 | −584 |
| `S_cc(n)` | −1 | 0 | 2 | 1 | −5 | −8 | 3 | 31 | 30 | −59 | −145 | 0 | 383 | 467 | −610 | −2023 | −509 | 5288 | 6939 | −5577 |

The castle row is the signed count of [[castle-row-raising-equation](pages/castle-row-raising-equation.md)]. For each of the three rows the signed generating function has a simple real pole `q_0` closest to the origin, so the row grows like a constant times `(−1/q_0)^n` (computed):[^2]

| family | `q_0` | `−1/q_0` | constant | growth of the unsigned count |
|---|---|---|---|---|
| castle | `−0.6158281352` | `1.62383` | `0.0985` | `2` |
| directed column-convex | `−0.5780051505` | `1.7300884` | `−0.009058018` | `2.61803` |
| column-convex | `−0.4449266995` | `2.2475612` | `4.12460·10⁻⁵` | `3.20557` |

For directed column-convex polyominoes, `q_0` is a zero of Theorem 3.6's denominator `L_0(1)`, and the next poles are a complex pair of modulus `0.780`. For column-convex polyominoes, `q_0` is a zero of Theorem 4.8's `1 + W + yX`, and the next poles are a complex pair of modulus `0.594`; with a small constant and a second pole close behind, `S_cc(n) q_0^n` settles to `4.1246·10⁻⁵` only from about `n = 70`. On all three rungs the signed count grows more slowly than the unsigned count, so the even and odd weights balance to leading order. The ratios of the two growth constants are `1.624/2 = 0.81` for castles, `1.730/2.618 = 0.66` for directed column-convex and `2.248/3.206 = 0.70` for column-convex polyominoes. [[castle-sequence-catalogue](pages/castle-sequence-catalogue.md)] records the OEIS status of the signed rows.

**The paper's stacks lie on their side.** Lemma 2.4 builds every stack polygon of width at least 2 by construction A, which extends the new first column both above and below the old one.[^4] So the paper's stacks are nested columns shrinking away from a base column on the left, a quarter turn from the upright stacks of [[convex-castle](pages/convex-castle.md)]. The area count is the same, but `v(P)` of the paper's stack is the width of the upright stack, so at `y = −1` Lemma 2.5 signs stacks by width, which has no Project Euler 502 meaning. The stacks signed by height, which is the block sign of a convex castle, are on [[convex-polyomino-by-area](pages/convex-polyomino-by-area.md)].

## Related

- [[column-convex-polygon-enumeration](pages/column-convex-polygon-enumeration.md)] - the six generating functions and the paper's constructions.
- [[castle-add-a-column-equation](pages/castle-add-a-column-equation.md)] - the castle's add-a-column equation and its relation to the paper's Lemma 2.3.
- [[convex-polyomino-by-area](pages/convex-polyomino-by-area.md)] - the convex families by area, the growth constant `2.30914`, and the rows signed by height.
- [[castle-by-area](pages/castle-by-area.md)], [[castle-row-raising-equation](pages/castle-row-raising-equation.md)] - the castles by area and their signed count.
- [[castle-perimeter](pages/castle-perimeter.md)] - the block count as the vertical half-perimeter, and A001519 as the convex castles by semi-perimeter.
- [[castle-q-bessel-closed-form](pages/castle-q-bessel-closed-form.md)] - the castle's `q_0` as the first zero of its q-Bessel denominator.

## Footnotes

[^1]: [[column-convex-polygon-enumeration](pages/column-convex-polygon-enumeration.md)] p.4-5 §2 L196-205 - "the number of horizontal (resp. vertical) steps in its perimeter by 2w(P) (resp. 2v(P)) (note that w(P) is the width of P), its area by a(P)"; the generating function is `Σ s^{ℓ(P)} t^{r(P)} x^{w(P)} y^{v(P)} q^{a(P)}` (read from the PDF; the OCR layer garbles it).
[^2]: Verified by execution (Python 3.11 with mpmath, 2026-10-16): a column sweep over the height of the last column and the offset of the next one, counting vertical perimeter edges, with every bottom on row 1 (castles), each bottom within the previous column (directed column-convex) or any overlapping offset (column-convex), gives `2^{n−1}`, `F_{2n−1}` and A001169 at `y = 1` and the three signed rows through `n = 95`; the table of `y = −1` matches; the constants are `S(n) q_0^n` at `n = 80, 88, 95` (0.098509175, −0.0090580181, 4.124595·10⁻⁵), and the ratios `S(95)/S(94)` are −1.6238297, −1.7300884, −2.2475612; `q_0` and the next poles from [40/40] Padé approximants of the signed series (directed column-convex: `0.42902 ± 0.65139i`, modulus 0.780; column-convex: `0.20082 ± 0.55870i`, modulus 0.594). The `y = 1` series of Lemma 2.5 and Theorems 3.2 and 3.4 match A001523, A006958 and A067676 through area 16 (2026-09-23).
[^3]: [[column-convex-polygon-enumeration](pages/column-convex-polygon-enumeration.md)] p.14 Remark (1) after Theorem 3.6 L748-759 - "the generating function for directed column-convex polygons, counted according to their left height, right height, width and area is a rational function. In particular, the area generating function is DV(1,1,1,1,q) = q(1-q)/(1-3q+q²). This result was proved by Delest and Dulucq"; p.24 Remark (2) after Theorem 4.8 L1342-1350 - "the generating function for column-convex polygons according to their left height, right height, width and area is a rational function. In particular, the area generating function is V(1,1,1,1,q) = q(1-q)³/(1-5q+7q²-4q³)" (formulas read from the PDF).
[^4]: [[column-convex-polygon-enumeration](pages/column-convex-polygon-enumeration.md)] p.6 §2.1 L276-281 and p.10 Lemma 2.4 L502-511 - construction A: "We first duplicate the leftmost column of P ... Then, we glue two pieces of columns, the first one at the top of the new column, the other one at its bottom. This corresponds to a multiplication by 1/(1 - syq)²"; "Applying construction A to the set of stack polygons provides all the stack polygons of width at least 2."
