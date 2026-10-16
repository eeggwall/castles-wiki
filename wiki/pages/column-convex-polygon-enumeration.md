---
title: "Enumeration of Column-Convex Polygons (Bousquet-Mélou, 1996)"
category: Sources
summary: Bousquet-Mélou's add-a-column method for column-convex polygons. Proposition 2.1 turns three ways of gluing a new first column (A, B, C) into a linear q-shift equation for the generating function by left and right column height, width, vertical half-perimeter and area; Lemma 2.2 solves the equation with a derivative term, which only construction C produces, and Lemma 2.3 the equation without it, which covers the directed classes. Six families are solved in closed form - stacks (Lemma 2.5), parallelograms (Theorem 3.2, y J_1/J_0), directed convex (Theorem 3.4), directed column-convex (Theorem 3.6), convex (Theorem 4.4) and column-convex polygons (Theorem 4.8); the generating functions by perimeter and area of the directed column-convex and the column-convex polygons are new. Castles are directed column-convex polygons with every column on row 1; their add-a-column equation has no derivative term, and Lemma 2.3 solves it.
tags: [paper, polyomino, column-convex, generating-functions, temperley, add-a-column, q-shift, q-bessel, source]
sources: [column-convex-polygon-enumeration, bousquet-melou-fedou-1995-convex-polyominoes, klarner-rivest-1974-convex-n-ominoes]
created: 2026-09-13
updated: 2026-10-16
---

# Enumeration of Column-Convex Polygons (Bousquet-Mélou, 1996)

**Source:** `raw/bousquet-melou-1996-column-convex-polygons.pdf` (text layer at `raw/bousquet-melou-1996-column-convex-polygons.txt`; the text layer is OCR, so formulas are read from the PDF and line numbers point into the text layer)
**Publication:** Mireille Bousquet-Mélou, "A method for the enumeration of various classes of column-convex polygons," *Discrete Mathematics* **154** (1996) 1-25. DOI `10.1016/0012-365X(95)00003-F`. Received 20 December 1993, revised 29 November 1994.[^1]
**Date ingested:** 2026-09-13
**Type:** paper (PDF, 25 pp.)

## Summary

A polyomino is **column-convex** when every column is one vertical run of cells. The paper enumerates the classes of column-convex polygons by one method, which it calls the Temperley methodology: a column-convex polygon is built by gluing columns one at a time, the gluing gives a linear functional equation, and two lemmas solve every equation that arises.[^2] It applies the method to six classes. The stack polygons are a worked example; for parallelogram, directed convex and convex polygons the results refine known ones; and for directed column-convex and column-convex polygons the generating function by perimeter and area is new.[^1]

**Variables.** For a polygon `P`, the generating function has the weight `s^{ℓ(P)} t^{r(P)} x^{w(P)} y^{u(P)} q^{a(P)}`: `ℓ(P)` and `r(P)` are the heights of the first and last columns, `2w(P)` and `2u(P)` the numbers of horizontal and vertical steps of the perimeter, so that `w(P)` is the width, and `a(P)` is the area.[^3] For a castle, `u(P)` is the block count ([[castle-perimeter](pages/castle-perimeter.md)]). A generating function `X(s, t, x, y, q)` is written `X(s)`, and `X'(s) = ∂X/∂s`.

The paper writes `S`, `P` and `C` for the generating functions of stack, parallelogram and convex polygons. This page writes `St`, `Π` and `Conv`, since `S` and `P` are the signed castle and tower counts and `C` is the binomial coefficient on the wiki ([[castle-notation](pages/castle-notation.md)]); `DC`, `DV` and `V` are the paper's.

## Gluing a new column (Proposition 2.1)

Let `P` be a column-convex polygon and `Q` a polygon whose first column, when removed, leaves `P`. A cell is **higher** (**lower**) than another when its level is greater than or equal to (less than or equal to) the other's. The three constructions are:[^4]

- `A(P)`: the top cell of the first column of `Q` is higher than the top cell of the first column of `P`, and its bottom cell is lower than theirs: the new column covers the old one.
- `B(P)`: both the top cell and the bottom cell of the new first column are lower than those of `P`'s first column.
- `C(P)`: the top cell is lower and the bottom cell higher: the new column lies within the rows of the old one.

For a set `𝒫` of polygons with generating function `X(s)`, the generating functions of `A(𝒫)`, `B(𝒫)` and `C(𝒫)` are[^4]

```
A:   x/(1 − syq)² · X(sq)
B:   xsq/((1 − sq)(1 − syq)) · (X(1) − X(sq))
C:   xsq/(1 − sq) · X'(1)  −  xs²q²/(1 − sq)² · (X(1) − X(sq))
```

The paper also uses the variants `A_2`, `A_3`, `B_1` and `B'_1`, which make one or both of the inequalities strict.[^5]

## Solving the equations (Lemmas 2.2 and 2.3)

**Lemma 2.2.** If `X(s) = x e(s) + x f(s) X(1) + x g(s) X(sq) + x h(s) X'(1)`, then[^6]

```
X(1)  =  ( E(1) + H(1) E'(1) − E(1) H'(1) ) / ( 1 − F(1) − H'(1) − H(1) F'(1) + F(1) H'(1) ),
```

where `E(s) = Σ_{n≥0} x^{n+1} g(s) g(sq) ⋯ g(sq^{n−1}) e(sq^n)`, and `F`, `H` are the same sums with `f`, `h` in place of `e`. The proof iterates the equation at `s, sq, sq², …`, which gives `X(s) = E(s) + X(1) F(s) + X'(1) H(s)`, and then solves for `X(1)` and `X'(1)` from this identity and its derivative at `s = 1`.

**Lemma 2.3.** Only construction `C` produces the derivative term, and the paper notes that `C` is not needed for directed polygons. When `h = 0`,[^7]

```
X(1)  =  E(1) / (1 − F(1)),        X(s)  =  ( E(s) + E(1) F(s) − E(s) F(1) ) / (1 − F(1)).
```

## The six families

| family | equation | closed form |
|---|---|---|
| stack polygons | Lemma 2.4: construction `A` | Lemma 2.5: `St(s, t, x, y, q) = sty Σ_{n≥1} x^n q^n / ((syq; q)_{n−1}² (1 − styq^n))` |
| parallelogram polygons | Lemma 3.1: construction `B` | Theorem 3.2: `Π(1, t, x, y, q) = ty J_1(1)/J_0(1)` |
| directed convex polygons | Lemma 3.3: three cases, using `St(s)` | Theorem 3.4: `DC(1, t, x, y, q) = ty M_1(1)/J_0(1)` |
| directed column-convex polygons | Lemma 3.5: constructions `A_2` and `B` | Theorem 3.6: `DV(1, t, x, y, q) = ty L_1(1)/L_0(1)` |
| convex polygons | Lemma 4.1: five cases, using `St(s)`, `DC(s)` and construction `C` | Proposition 4.2 by Lemma 2.2; Theorem 4.4: `Conv(1, t, x, y, q) = J̃_1 E'(1) − K̃_1 E(1)` |
| column-convex polygons | Lemma 4.5: constructions `A_3`, `B_1`, `B'_1` and `C` | Proposition 4.6 by Lemma 2.2; Theorem 4.8: `V(1, 1, x, y, q) = y(1 − y) X / (1 + W + yX)` |

Here `(a; q)_n = (1 − a)(1 − aq)⋯(1 − aq^{n−1})`, which the paper writes `(a)_n`, and the series `M_1`, `L_0`, `L_1`, `J̃_1`, `K̃_1`, `E` and `X`, `W` are given in the theorems and in Lemma 4.7.[^8] The **stack polygons** are built by construction `A`, so each new first column covers the old one: they lie on their left column, a quarter turn from the upright stacks of [[stack-polyomino-gf](pages/stack-polyomino-gf.md)].[^9] At `s = t = x = y = 1`, Lemma 2.5 is the series of the stacks by area, `A001523`.

The **parallelogram polygons** satisfy[^10]

```
Π(s)  =  xstyq/(1 − styq)  +  xsq/((1 − sq)(1 − syq)) · (Π(1) − Π(sq)),

J_0(s)  =  Σ_{n≥0} (−1)^n x^n s^n q^{C(n+1,2)} / ((sq; q)_n (syq; q)_n),
J_1(s)  =  Σ_{n≥1} (−1)^{n−1} x^n s^n q^{C(n+1,2)} / ((sq; q)_{n−1} (syq; q)_{n−1} (1 − styq^n)).
```

The paper credits special cases of Theorem 3.2 to Klarner and Rivest (area), Delest and Fédou (width and area), and Bousquet-Mélou and Viennot (width, height and area).[^11] [[bousquet-melou-fedou-1995-convex-polyominoes](pages/bousquet-melou-fedou-1995-convex-polyominoes.md)] quotes the same quotient `y J_1/J_0` as its eq. (1).

At `s = t = x = y = 1`, the remarks after Theorems 3.6 and 4.8 give the area generating functions of the directed column-convex and the column-convex polygons:[^12]

```
DV(1, 1, 1, 1, q)  =  q(1 − q)/(1 − 3q + q²)                  1, 2, 5, 13, 34, 89, …      (A001519)
V(1, 1, 1, 1, q)   =  q(1 − q)³/(1 − 5q + 7q² − 4q³)          1, 2, 6, 19, 61, 196, …     (A001169, board-pile polyominoes)
```

Both agree with enumeration of the polygons for area at most 9.[^13]

**Feretić and Svrtan.** The paper notes that Feretić and Svrtan derived linear q-equations from the Temperley methodology for column-convex polygons on the square and honeycomb lattices, "less efficient than the method we give in this paper", without simple closed forms.[^14]

**Motivation.** The paper quotes Klarner and Rivest's bounds `3.87 < K < 4.65` for the growth constant `K` of all polyominoes by area as the reason to study restricted classes.[^15]

## Castles in this framework

- **Castles are directed column-convex polygons** whose columns all start on row 1: every cell can be reached from the bottom-left cell by North and East steps. The paper does not treat them as a class.
- **The castle equation.** [[castle-add-a-column-equation](pages/castle-add-a-column-equation.md)] writes the castles with first-column height `s` as `X(s) = x e(s) + x f(s) X(1) + x g(s) X(sq)` with `e(s) = syq/(1 − syq)`, `f(s) = sq/(1 − sq)` and `g(s) = −sq(1 − y)/((1 − sq)(1 − syq))`. There is no derivative term, and Lemma 2.3 gives the closed form `N/M − 1` of [[castle-q-bessel-closed-form](pages/castle-q-bessel-closed-form.md)], with `E(1) = N − M` and `1 − F(1) = M`. The equation agrees with enumeration of the castles through area 9 at `x = 2`, `y = −3`.[^13]
- **The parallelogram series.** The castle closed form is `Π/(1 − y − Π)` with `Π` the parallelogram series of Theorem 3.2 at width `(1 − y)x` and height `y`, in this page's variables ([[castle-q-bessel-closed-form](pages/castle-q-bessel-closed-form.md)], section *Castles are a sequence of parallelograms*).
- **Ferrers diagrams, stacks and parallelograms** are the three classical directed convex families. In the set of convex polyominoes, each is characterized by which two or three corners of its bounding box it contains.[^16] The upright stacks are the convex castles ([[convex-castle](pages/convex-castle.md)]).

## Entities & Concepts

- [[column-convex-polyomino](pages/column-convex-polyomino.md)] - the class the method enumerates.
- [[castle-add-a-column-equation](pages/castle-add-a-column-equation.md)] - the castle equation in this paper's variables, solved by Lemma 2.3, and the Ferrers, stack and parallelogram polyominoes among the castles.
- [[castle-q-bessel-closed-form](pages/castle-q-bessel-closed-form.md)] - castles by width, blocks and area as `N/M − 1`, with `N` the series `J_0` of Theorem 3.2.
- [[stack-polyomino-gf](pages/stack-polyomino-gf.md)] - the stacks by area, which Lemma 2.5 gives at `s = t = x = y = 1`.
- [[column-convex-ladder-by-area](pages/column-convex-ladder-by-area.md)] - the closed forms for stacks, parallelograms, directed convex, directed column-convex and column-convex polygons at width weight 1 and `y = ±1`, checked by a column sweep.
- [[convex-polyomino-by-area](pages/convex-polyomino-by-area.md)] - the stack, parallelogram, directed convex and convex polyominoes counted by area.
- [[bousquet-melou-fedou-1995-convex-polyominoes](pages/bousquet-melou-fedou-1995-convex-polyominoes.md)] - the generating function of convex polyominoes by width, height and area from a q-differential system; the paper states that the formula of Theorem 4.4 at `t = 1` is the same.[^17]
- [[klarner-rivest-1974-convex-n-ominoes](pages/klarner-rivest-1974-convex-n-ominoes.md)] - parallelograms by area, a special case of Theorem 3.2. Their recursion `B(x, y) = xy/(1 − xy) + xy/(1 − xy)² (B(x, 1) − B(x, xy))` has the form of Lemma 2.3, with one shift and no derivative term (the wiki's reading).
- [[prellberg-brak-1995-cluster-models](pages/prellberg-brak-1995-cluster-models.md)] - nonlinear functional equations for staircase and bar-graph polygons (quadratic) and directed column-convex polygons (cubic), each turned into a linear q-equation by a substitution of the form `G(x) = α H(qx)/H(x) − b(x)`.
- [[horizontally-convex-polyomino](pages/horizontally-convex-polyomino.md)] - the polyominoes convex along rows, counted by area by Hickerson.
- [[castle-polyomino](pages/castle-polyomino.md)], [[convex-castle](pages/convex-castle.md)] - the castles and the convex castles.

## Relation to Other Wiki Pages

[[project-euler-502-solution](pages/project-euler-502-solution.md)] lists this paper as a reference. [[analytic-combinatorics-ch1-ogfs](pages/analytic-combinatorics-ch1-ogfs.md)] derives the stack series from a decomposition at the first tallest column, by the [[symbolic-method](pages/symbolic-method.md)], without a functional equation ([[stack-polyomino-gf](pages/stack-polyomino-gf.md)]).

## Footnotes

[^1]: [[column-convex-polygon-enumeration](pages/column-convex-polygon-enumeration.md)] `bousquet-melou-1996-column-convex-polygons.txt` L3-13, L160-165 p.1 §1, p.4 §1 [synthesis] - "A method for the enumeration of various classes of column-convex polygons ... Discrete Mathematics 154 (1996) 1-25 ... Received 20 December 1993; revised 29 November 1994"; "some of them are only refinements of already known results (parallelogram polyominoes, directed and convex polyominoes, convex polyominoes) ... two others are new; we obtain the perimeter and area generating function for column-convex polygons, and for directed column-convex polygons." DOI checked against Crossref (2026-10-16).
[^2]: [[column-convex-polygon-enumeration](pages/column-convex-polygon-enumeration.md)] `bousquet-melou-1996-column-convex-polygons.txt` L180-183 p.4 §2 - "a column-convex polyomino can be obtained by successively gluing columns, in a way that depends on the class of polygons one studies. This idea is sometimes known as 'Temperley methodology' in statistical physics".
[^3]: [[column-convex-polygon-enumeration](pages/column-convex-polygon-enumeration.md)] `bousquet-melou-1996-column-convex-polygons.txt` L194-209 pp.4-5 §2 - "Its left height (resp. right height) is the height of its leftmost (resp. rightmost) column", "the number of horizontal (resp. vertical) steps in its perimeter by 2w(P) (resp. 2u(P)) (note that w(P) is the width of P)", "its area by a(P)", and the generating function "Σ_{P∈𝒫} s^{ℓ(P)} t^{r(P)} x^{w(P)} y^{u(P)} q^{a(P)}" (read from p.5).
[^4]: [[column-convex-polygon-enumeration](pages/column-convex-polygon-enumeration.md)] `bousquet-melou-1996-column-convex-polygons.txt` L220-248 p.5 §2.1, Proposition 2.1 (formulas read from the PDF) - "Let A(P) (resp. B(P), C(P)) be the set of column-convex polyominoes Q satisfying the three following properties: removing the first column of Q gives P; the top-cell of the first column of Q is higher (resp. lower, lower) than the top-cell of the first column of P; the bottom-cell of the first column of Q is lower (resp. lower, higher) than the bottom-cell of the first column of P", "a cell c_1 is said to be higher (resp. lower) than a cell c_2 if the level (ordinate) of c_1 is greater than or equal to (resp. less than or equal to) the level of c_2", and the three generating functions.
[^5]: [[column-convex-polygon-enumeration](pages/column-convex-polygon-enumeration.md)] `bousquet-melou-1996-column-convex-polygons.txt` L327-352 pp.7-8 Remark [synthesis] - the constructions `A_1`, `A_2`, `A_3`, `B'`, `B_1`, `B'_1`, with strict inequalities in place of one or both of those of `A` and `B`, and their generating functions.
[^6]: [[column-convex-polygon-enumeration](pages/column-convex-polygon-enumeration.md)] `bousquet-melou-1996-column-convex-polygons.txt` L371-449 pp.8-9 Lemma 2.2 and proof - "Suppose that X(s) = xe(s) + xf(s)X(1) + xg(s)X(sq) + xh(s) ∂X/∂s(1) ... Then X(1) = (E(1) + H(1)E'(1) − E(1)H'(1))/(1 − F(1) − H'(1) − H(1)F'(1) + F(1)H'(1))", "X(s) = E(s) + X(1)F(s) + X'(1)H(s). (3)", "Substituting s by 1 leads to a system of two linear equations in X(1) and X'(1)".
[^7]: [[column-convex-polygon-enumeration](pages/column-convex-polygon-enumeration.md)] `bousquet-melou-1996-column-convex-polygons.txt` L452-484 pp.9-10 Lemma 2.3 (formulas read from p.10) - "this partial derivative only occurs when construction C is used. Looking at Fig. 6 suggests that this construction is not needed as soon as the class of polygons under consideration is formed with directed polygons", "X(1) = E(1)/(1 − F(1))", "X(s) = (E(s) + E(1)F(s) − E(s)F(1))/(1 − F(1))".
[^8]: [[column-convex-polygon-enumeration](pages/column-convex-polygon-enumeration.md)] `bousquet-melou-1996-column-convex-polygons.txt` L500-525, L541-578, L614-746, L772-842, L1037-1041, L1079-1132, L1165-1283 pp.10-23 [synthesis] - Lemmas 2.4, 3.1, 3.3, 3.5, 4.1, 4.5 (the equations, with the constructions each proof uses), Lemma 2.5 and Theorems 3.2, 3.4, 3.6, 4.4, 4.8 (the closed forms, read from the PDF: "C(1, t, x, y, q) = J̃_1 E'(1) − K̃_1 E(1)" and "V(1, 1, x, y, q) = y (1 − y)X/(1 + W + yX)"), Propositions 4.2 and 4.6 (Lemma 2.2), and Lemma 4.7 (the series `I` and `X`, `Y`, `Z`).
[^9]: [[column-convex-polygon-enumeration](pages/column-convex-polygon-enumeration.md)] `bousquet-melou-1996-column-convex-polygons.txt` L500-511 p.10 Lemma 2.4 - "S(s) = xstyq/(1 − styq) + x/(1 − syq)² S(sq)", "Applying construction A to the set of stack polygons provides all the stack polygons of width at least 2. Moreover, the generating function for stack polygons of width 1 is xstyq/(1 − styq)."
[^10]: [[column-convex-polygon-enumeration](pages/column-convex-polygon-enumeration.md)] `bousquet-melou-1996-column-convex-polygons.txt` L541-578 p.11 Lemma 3.1 and Theorem 3.2 (formulas read from the PDF) - "P(s) = xstyq/(1 − styq) + xsq/((1 − sq)(1 − syq)) (P(1) − P(sq))", "Applying construction B to the set of parallelogram polyominoes provides all the parallelogram polyominoes of width at least 2", "P(1, t, x, y, q) = ty J_1(1)/J_0(1)" with the series `J_0`, `J_1`.
[^11]: [[column-convex-polygon-enumeration](pages/column-convex-polygon-enumeration.md)] `bousquet-melou-1996-column-convex-polygons.txt` L587-589 p.12 Remark (2) after Theorem 3.2 - "Special important cases of this theorem were proved by Klarner and Rivest [22] (area generating function), Delest and Fedou [12] (width and area generating function), Bousquet-Mélou and Viennot [6] (width, height and area generating function)."
[^12]: [[column-convex-polygon-enumeration](pages/column-convex-polygon-enumeration.md)] `bousquet-melou-1996-column-convex-polygons.txt` L748-759 p.14, L1342-1350 p.24 Remarks (formulas read from the PDF) - "the area generating function is DV(1, 1, 1, 1, q) = q(1 − q)/(1 − 3q + q²). This result was proved by Delest and Dulucq [11]" and "the area generating function is V(1, 1, 1, 1, q) = q(1 − q)³/(1 − 5q + 7q² − 4q³). This result can be found at several places [10, 20]."
[^13]: Verified by execution (Python 3.11 with SymPy, 2026-10-16): the column-convex and directed column-convex polygons by area for area at most 9 against the two area generating functions (`1, 2, 6, 19, 61, 196, 629, 2017, 6466` and `1, 2, 5, 13, 34, 89, 233, 610, 1597`); Lemma 2.5 against the polygons with nested columns through area 7; the castle equation against all compositions of area at most 9, weighted `s^{c_1} x^{width} y^{blocks} q^{area}` at `x = 2`, `y = −3`.
[^14]: [[column-convex-polygon-enumeration](pages/column-convex-polygon-enumeration.md)] `bousquet-melou-1996-column-convex-polygons.txt` L354-359 p.8 Note - "Feretić and Svrtan have independently shown, on some examples, that the Temperley methodology can be translated into linear q-equations. They established such equations for the generating function for column-convex polygons on the square lattice and on the honeycomb lattice. However, their approach for solving these equations is less efficient than the method we give in this paper, and does not give simple closed expressions for the generating functions [16]."
[^15]: [[column-convex-polygon-enumeration](pages/column-convex-polygon-enumeration.md)] `bousquet-melou-1996-column-convex-polygons.txt` L82-88 p.2 §1 - "let p(n) denote the number of polyominoes having n cells. Klarner and Rivest proved that (p(n))^{1/n} tends to a limit K, which satisfies the following inequality: 3.87 < K < 4.65 [21]", "The difficulty of these questions has led to the study of various restricted classes of polyominoes or polygons."
[^16]: [[column-convex-polygon-enumeration](pages/column-convex-polygon-enumeration.md)] `bousquet-melou-1996-column-convex-polygons.txt` L131-137 p.3 §1 - "three very classical families of directed and convex polyominoes: Ferrers diagrams, stack polyominoes, and parallelogram (or staircase) polyominoes. As Fig. 3 shows, each of these subsets can be characterized, in the set of convex polyominoes, by the fact that two or three vertices of the minimal bounding rectangle of the polyomino belong to the polyomino itself."
[^17]: [[column-convex-polygon-enumeration](pages/column-convex-polygon-enumeration.md)] `bousquet-melou-1996-column-convex-polygons.txt` L945-948 p.17 - "In the case where t = 1, a short computation proves that this new formula is the same as the one given by Bousquet-Mélou and Fédou [5]."
