---
title: "Enumeration of Column-Convex Polygons (Bousquet-Mélou, 1996)"
category: Sources
summary: Bousquet-Mélou's universal add-a-column (Temperley) method for column-convex polygons - Lemmas 2.2 and 2.3 solve the one-step and two-step q-shift equations that fall out of the "three column-attachment cases" A/B/C, giving perimeter+area (+width, +left/right height) GFs for six families in one framework - stack (2.4/2.5), parallelogram (3.1/3.2, re-deriving y J_1/J_0), directed-and-convex (3.3/3.4), directed-column-convex (3.5/3.6, new in 1996), convex (4.1/4.4), and column-convex (4.5/4.8, new in 1996). The parallelogram Theorem 3.2 is the one that our castle-q-bessel-closed-form page reuses. The convex Theorem 4.8 introduces a Fibonacci-polynomial-like q-Bessel `I` series that condenses the 1995 J_0/J_1 packaging.
tags: [paper, polyomino, column-convex, generating-functions, temperley, add-a-column, q-shift, q-bessel, source]
sources: [column-convex-polygon-enumeration, bousquet-melou-fedou-1995-convex-polyominoes, klarner-rivest-1974-convex-n-ominoes]
created: 2026-09-13
updated: 2026-09-23
---

# Enumeration of Column-Convex Polygons (Bousquet-Mélou, 1996)

**Source:** `raw/bousquet-melou-1996-column-convex-polygons.pdf`
**Publication:** Mireille Bousquet-Mélou, "A method for the enumeration of various classes of column-convex polygons," *Discrete Mathematics* **154** (1996) 1-25. DOI `10.1016/0012-365X(95)00003-F`. Received 20 December 1993, revised 29 November 1994.[^1]
**Date ingested:** 2026-09-13 (updated 2026-09-23 with the actual PDF)
**Type:** paper (PDF, 25 pp.)

## Summary

The paper gives a **single, systematic method** to enumerate any "natural" class of column-convex polyominoes, tracking left height, right height, width, height (vertical perimeter) and area simultaneously. Two lemmas solve the q-shift equations that come out of the construction. Six families are worked to closed form, two of them for the first time in 1996.[^1]

The method is the classical **Temperley "add-a-column" methodology** framed as functional equations.[^2] For any set `S` of column-convex polygons with generating function `X(s, t, x, y, q)` (where `s`, `t` mark left and right column heights, `x` marks width, `y` marks vertical perimeter, `q` marks area), Proposition 2.1 gives the generating functions for the three ways `A(S)`, `B(S)`, `C(S)` of attaching a new leftmost column: `A` when the new column overshoots both top and bottom, `B` when it overshoots one side and undershoots the other, `C` when the new column sits strictly inside the previous one.[^3] The result is always a q-shift equation of shape

```
X(s) = x e(s) + x f(s) X(1) + x g(s) X(sq) + x h(s) X'(1)
```

with `X'(1) = ∂X/∂s(1)`. **Lemma 2.2** solves this in closed form as `X(1) = (E(1) + H(1) E'(1) - E(1) H'(1)) / (1 - F(1) - H'(1) - H(1) F'(1) + F(1) H'(1))` and gives `X(s)` in terms of three q-series `E, F, H` built by iterating the shift.[^4] When the class is directed (construction `C` is not needed), `h(s) = 0` and the derivative disappears; **Lemma 2.3** collapses to `X(1) = E(1) / (1 - F(1))`, `X(s) = E(s) + (E(1) F(s) - E(s) F(1)) / (1 - F(1))`.[^5] This "one-step q-shift with no derivative" is exactly the shape that `castle-q-bessel-closed-form` reuses.

Six families are worked out. **Stack polygons** (Lemmas 2.4-2.5): `S(s) = xstyq/(1 - styq) + xs²q²/(1 - syq)² · S(sq)` gives a q-series in a single sum.[^6] **Parallelogram polygons** (Theorem 3.2, previously Bousquet-Mélou-Fédou 1995): `P(s) = xstyq/(1 - styq) + xsyq/((1 - sq)(1 - syq)) · (P(1) - P(sq))`, with `P(1) = tyJ_1(1)/J_0(1)` and `J_0(s) = sum_{n≥0} (-1)^n x^n s^n q^{n(n+1)/2} / ((sq)_n (syq)_n)`, `J_1(s) = sum_{n≥1} (-1)^{n-1} x^n s^n q^{n(n+1)/2} / ((sq)_{n-1} (syq)_{n-1} (1 - styq^n))`.[^7] This is the same `J_0`, `J_1` pair as [[bousquet-melou-fedou-1995-convex-polyominoes](pages/bousquet-melou-fedou-1995-convex-polyominoes.md)], but the derivation here is via Lemma 2.3 rather than the 1995 paper's 3×3 q-differential system. **Directed-and-convex** (Theorem 3.4) and **directed-column-convex** (Theorem 3.6, new in 1996) are Lemma-2.3 corollaries in the same style, giving explicit q-series `M_1(s)`, `L_0(s)`, `L_1(s)`.[^8] **Convex polygons** (Theorem 4.4) and **column-convex polygons** (Theorem 4.8, new in 1996) need the general Lemma 2.2, and 4.8 introduces a new q-Bessel-like series `I(s)` obeying a five-term q-recurrence, together with `X, Y, Z` extracted from it.[^9]

**Feretić-Svrtan lineage note** (end of §2.1): "Feretić and Svrtan have independently shown, on some examples, that the Temperley methodology can be translated into linear q-equations ... However, their approach for solving these equations is less efficient than the method we give in this paper, and does not give simple closed expressions for the generating functions [16]."[^10] So the same-era Feretić-Svrtan papers cover column-convex and honeycomb column-convex via a different solving method.

## Why it matters for Project Euler 502 (PE 502)

This paper is the closest external framework to the castle problem, and several castle threads run straight into it.

- **The castle grammar's area grading fits Lemma 2.3.** The equation `A(u) = ((x - (1-x)uq) A(uq) + (1-x)) / (1 - uq A(uq))` on [[castle-q-bessel-closed-form](pages/castle-q-bessel-closed-form.md)] is the one-step q-shift Lemma 2.3 is designed for. Once you pass the Möbius-linearization step to `A = N/M`, the coefficient recursions are the same shape as the `E`, `F` iterations in the paper. The specific parallelogram shortcut - identifying `N` with `J_0` and `N - M` with `(x/(1-x)) J_1` - is what our page adds; the surrounding structure is Lemma 2.3.
- **Add-a-column is the castle recurrence.** Gluing columns and tracking how a new column relates to its predecessor is the same transfer-style recurrence the castle solution runs in the width direction. The three cases `A/B/C` collapse in the castle world because castles sit on a horizontal base (so `C` never happens), which is exactly why our closed form needs only Lemma 2.3.
- **Two classical directed-and-convex families named:** Ferrers diagrams, stack polygons, and parallelogram (staircase) polyominoes, each characterised by which vertices of the minimal bounding rectangle the polyomino must contain.[^11] The stack rung is exactly the convex-castle sub-family on [[convex-polyomino-by-area](pages/convex-polyomino-by-area.md)]; parallelograms are the object our castle GF is a sequence of.

## Key Takeaways

- **Universal add-a-column method:** three attachment cases `A/B/C` (Proposition 2.1) turn any column-convex polygon class into a q-shift equation of a uniform shape.[^3]
- **Two solving lemmas:** Lemma 2.2 (general, with `X'(1)`) and Lemma 2.3 (directed, no derivative). Lemma 2.3 is the tool the castle q-Bessel page reuses.[^4][^5]
- **Six worked families:** stack (2.4/2.5), parallelogram (3.1/3.2), directed-and-convex (3.3/3.4), directed-column-convex (3.5/3.6, **new in 1996**), convex (4.1-4.4), column-convex (4.5-4.8, **new in 1996**).[^1]
- **Parallelogram Theorem 3.2 re-derives `y J_1/J_0`** from Bousquet-Mélou-Fédou 1995 by a shorter route (one Lemma 2.3 application, no q-differential system).[^7]
- **Bar-graphs (castles) are not a target class here.** The paper's directed classes DC and DV have arbitrary column bottoms; a castle has all bottoms at row 1. The castle sits inside DV as a specialisation the paper does not single out.
- **Feretić and Svrtan** independently gave a Temperley-style derivation for column-convex polygons that leads to linear q-equations but not closed forms, in the same 1993-1995 window.[^10]

## Entities & Concepts

- [[column-convex-polyomino](pages/column-convex-polyomino.md)] - the object class, direct structural analogue of the castle.
- [[castle-polyomino](pages/castle-polyomino.md)], [[convex-castle](pages/convex-castle.md)] - the castle objects this connects to.
- [[horizontally-convex-polyomino](pages/horizontally-convex-polyomino.md)] - the row-convex counterpart (Hickerson).
- [[generating-functions](pages/generating-functions.md)] - the tool used throughout.
- [[stack-polyomino-gf](pages/stack-polyomino-gf.md)] - the "stack polygons" family this paper solves via Lemma 2.3, giving Lemma 2.5 in closed form.
- [[convex-polyomino-by-area](pages/convex-polyomino-by-area.md)] - the area ladder whose rungs this paper produces via one uniform method.
- [[castle-q-bessel-closed-form](pages/castle-q-bessel-closed-form.md)] - a Lemma-2.3 application specialised to castles: the tower-word grammar graded by area gives `A(u) = 1 - x + x E(uq)`, `E(u) = A(u)/(1 - u A(u))`, whose linearisation is precisely Lemma 2.3 on castles.

## Relation to Other Wiki Pages

Cited as a reference on [[project-euler-502-solution](pages/project-euler-502-solution.md)]. It is the polyomino-enumeration framework the castle problem most resembles - an add-a-column generating-function method for column-convex shapes - and the natural home for tracing the castle's column-independence, convexity, and stack/Ferrers threads into the literature. [[analytic-combinatorics-ch1-ogfs](pages/analytic-combinatorics-ch1-ogfs.md)] provides a complementary route: the [[symbolic-method](pages/symbolic-method.md)] constructs specific well-structured sub-families like [[stack-polyomino-gf](pages/stack-polyomino-gf.md)] directly, without a functional equation. The convex and directed-convex area generating functions that this paper recovers were first put in closed form by [[bousquet-melou-fedou-1995-convex-polyominoes](pages/bousquet-melou-fedou-1995-convex-polyominoes.md)], which solves the q-differential system from Bousquet-Mélou's earlier algebraic-language encoding ([[q-differential-system](pages/q-differential-system.md)]). All three results share the q-Bessel denominator `J_0`. The nonlinear-functional-equation companion in the same window is [[prellberg-brak-1995-cluster-models](pages/prellberg-brak-1995-cluster-models.md)]: same q-Bessel families, but the equations there are quadratic (not linear as here) and the linearisation identity `G = α H(qx)/H(x) - b` is the analogue of Lemma 2.3's `E/(1-F)`.

## Footnotes

[^1]: [[column-convex-polygon-enumeration](pages/column-convex-polygon-enumeration.md)] p.1 §1, p.4 §1 [synthesis] - "A method for the enumeration of various classes of column-convex polygons ... Discrete Mathematics 154 (1996) 1-25 ... Received 20 December 1993; revised 29 November 1994"; "some of them are only refinements of already known results (parallelogram polyominoes, directed and convex polyominoes, convex polyominoes) ... two others are new; we obtain the perimeter and area generating function for column-convex polygons, and for directed column-convex polygons."
[^2]: [[column-convex-polygon-enumeration](pages/column-convex-polygon-enumeration.md)] p.4 §2 - "a column-convex polyomino can be obtained by successively gluing columns ... This idea is sometimes known as 'Temperley methodology' in statistical physics, where it has been already intensively used."
[^3]: [[column-convex-polygon-enumeration](pages/column-convex-polygon-enumeration.md)] p.5 Proposition 2.1 - "Let A(P) (resp. B(P), C(P)) be the set of column-convex polyominoes Q ... the top-cell of the first column of Q is higher (resp. lower, lower) than the top-cell of the first column of P; the bottom-cell of the first column of Q is lower (resp. lower, higher) than the bottom-cell of the first column of P"; "the generating function for A(P) is (1 - syq)^{-2} x X(sq) ... for B(P) is xsq/((1-sq)(1-syq)) (X(1) - X(sq)) ... for C(P) is xs²q²/(1-sq)² (X(1) - X(sq)) - xs²q²/(1-sq)² sq X'(1)" (formula shape read from p.5, exponents corrected from OCR).
[^4]: [[column-convex-polygon-enumeration](pages/column-convex-polygon-enumeration.md)] p.8 Lemma 2.2 - "Suppose X(s) = xe(s) + xf(s)X(1) + xg(s)X(sq) + xh(s)X'(1) ... Then X(1) = (E(1) + H(1)E'(1) - E(1)H'(1))/(1 - F(1) - H'(1) - H(1)F'(1) + F(1)H'(1))" with `E, F, H` the iterated-shift q-series.
[^5]: [[column-convex-polygon-enumeration](pages/column-convex-polygon-enumeration.md)] p.9 Lemma 2.3 - "Suppose X(s) = xe(s) + xf(s)X(1) + xg(s)X(sq) ... Then X(1) = E(1)/(1 - F(1)) ... X(s) = E(s) + (E(1)F(s) - E(s)F(1))/(1 - F(1))."
[^6]: [[column-convex-polygon-enumeration](pages/column-convex-polygon-enumeration.md)] p.10 Lemma 2.4 and 2.5 - "S(s) = xstyq/(1 - styq) + xs²q²/(1 - syq)² S(sq)"; the closed form `S(s, t, x, y, q) = ...` follows from Lemma 2.3 (Lemma 2.5).
[^7]: [[column-convex-polygon-enumeration](pages/column-convex-polygon-enumeration.md)] p.11 Lemma 3.1 and Theorem 3.2 - "P(s) = xstyq/(1 - styq) + xsyq/((1-sq)(1-syq)) (P(1) - P(sq))"; "The generating function P(s, t, x, y, q) for parallelogram polyominoes satisfies P(1, t, x, y, q) = ty J_1(1)/J_0(1)" with the explicit `J_0`, `J_1` series (read from p.11).
[^8]: [[column-convex-polygon-enumeration](pages/column-convex-polygon-enumeration.md)] pp.12-14 Theorems 3.4, 3.6 - directed-and-convex GF `DC(1, t, x, y, q) = ty M_1(1)/J_0(1)` and directed-column-convex GF `DV(1, t, x, y, q) = ty L_1(1)/L_0(1)`, with explicit series in the theorems.
[^9]: [[column-convex-polygon-enumeration](pages/column-convex-polygon-enumeration.md)] pp.15-24 Theorems 4.4, 4.8 - convex GF `C(1, t, x, y, q) = E(1)/(1 - F(1) - H'(1) - H(1) F'(1) + F(1) H'(1))` and column-convex GF `V(1, 1, x, y, q) = (1 - y) X / (1 + W + y X)` with the `I, X, Y, Z, W` q-series defined in Lemma 4.7.
[^10]: [[column-convex-polygon-enumeration](pages/column-convex-polygon-enumeration.md)] p.8 Note - "Feretić and Svrtan have independently shown, on some examples, that the Temperley methodology can be translated into linear q-equations. They established such equations for the generating function for column-convex polygons on the square lattice and on the honeycomb lattice. However, their approach for solving these equations is less efficient than the method we give in this paper, and does not give simple closed expressions for the generating functions."
[^11]: [[column-convex-polygon-enumeration](pages/column-convex-polygon-enumeration.md)] p.3 §1 - "three very classical families of directed and convex polyominoes: Ferrers diagrams, stack polyominoes, and parallelogram (or staircase) polyominoes ... each of these subsets can be characterized, in the set of convex polyominoes, by the fact that two or three vertices of the minimal bounding rectangle of the polyomino belong to the polyomino itself."
