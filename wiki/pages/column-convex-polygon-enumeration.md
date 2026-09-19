---
title: "Enumeration of Column-Convex Polygons (Bousquet-Mélou)"
category: Sources
summary: Bousquet-Mélou's universal "add-a-column" (Temperley) method — one functional-equation template for the generating functions (perimeter + area) of every natural column-convex polyomino class.
tags: [paper, polyomino, column-convex, generating-functions, temperley, source]
sources: [column-convex-polygon-enumeration]
created: 2026-09-13
updated: 2026-09-19
---

# Enumeration of Column-Convex Polygons (Bousquet-Mélou)

**Source:** `assets/EnumerationColumnConvexPolynomials.pdf` (Mireille Bousquet-Mélou, *A method for the enumeration of various classes of column-convex polygons*, LaBRI, Université Bordeaux 1)
**Date ingested:** 2026-09-13
**Type:** paper (PDF, 17 pp.)

## Summary

The paper gives a **single, systematic method** to enumerate essentially any "natural" class of **column-convex** polyominoes, tracking perimeter and area (and other parameters such as width) simultaneously.[^1] A polyomino is **column-convex** (equivalently vertically convex) when its intersection with any vertical line is a contiguous segment — every column is a single unbroken run of cells; it is **convex** when both column- and row-convex.[^2] Enumerating general polyominoes is famously open (even the growth constant `K`, `3.87 < K < 4.65`, is barely pinned down), which is why restricted convex classes are studied instead.[^3]

The method — the **"add-a-column" / Temperley methodology** — builds a column-convex polyomino by successively gluing columns, classifying the ways a new first column can be attached relative to the previous one (three cases `A/B/C`, by whether the new column's top and bottom cells sit higher or lower).[^4] Translating this into a functional equation for the generating function
`∑_P s^{l(P)} t^{r(P)} x^{h(P)} y^{v(P)} q^{a(P)}`
(tracking left/right column heights `l,r`, half-perimeters `h,v`, and area `a`) gives one equation of a uniform type per class, solvable by a uniform procedure.[^5] The paper recovers known results (parallelogram, directed-and-convex, convex polyominoes) and derives new ones (perimeter+area GF for column-convex and directed-column-convex polygons).[^6]

It also fixes a vocabulary of classical directed-and-convex families the wiki will want: **Ferrers diagrams, stack polygons, and parallelogram (staircase) polyominoes**, each characterized by which vertices of the minimal bounding rectangle the polyomino must contain.[^7]

## Why it matters for Project Euler 502 (PE 502)

This is arguably the closest external framework to the castle problem, and several castle threads run straight into it:

- **Column-convexity ≈ the castle's column structure.** A [[castle-polyomino](pages/castle-polyomino.md)] is exactly a shape whose columns are contiguous stacks on a full-width base — a column-convex-like object. Bousquet-Mélou's per-column generating-function bookkeeping is the continuous analogue of the castle's per-column [[binary-string-bijection](pages/binary-string-bijection.md)] and the `T(k,L)=(k+1)^L` column-independence product form.
- **Add-a-column = the castle recurrence.** Gluing columns and tracking how the new column relates to the previous is precisely the transfer-style recurrence the castle solution runs in the width direction; the Temperley methodology is the mature form of that idea.
- **The castle's [[convex-castle](pages/convex-castle.md)] and its variations.** Convex castles are near neighbors of the "convex polyomino" and "stack polygon" families here; the failed castle thread (convex-castle *variation* enumeration never closing into a formula) is exactly the kind of obstruction this paper's universal method is designed to route around.
- **Stack polygons / Ferrers diagrams** are candidate exact sub-correspondences with castle sub-families — a concrete thread to chase.

## Key Takeaways

- **Column-convex** = every vertical line meets the polyomino in one segment (each column contiguous); **convex** = column- and row-convex.[^2]
- A **universal add-a-column (Temperley) method** produces a uniform functional equation for the perimeter+area generating function of any natural column-convex class, solvable uniformly.[^1][^4]
- Classical directed-and-convex families named: **Ferrers diagrams, stack polygons, parallelogram/staircase polyominoes**, distinguished by which bounding-rectangle corners they must touch.[^7]
- General polyomino enumeration is open (growth constant `K ∈ (3.87, 4.65)`), motivating the study of restricted convex classes.[^3]

## Entities & Concepts

- [[column-convex-polyomino](pages/column-convex-polyomino.md)] — the object class; a direct structural analogue of the castle.
- [[castle-polyomino](pages/castle-polyomino.md)], [[convex-castle](pages/convex-castle.md)] — the castle objects this connects to.
- [[horizontally-convex-polyomino](pages/horizontally-convex-polyomino.md)] — the row-convex counterpart (Hickerson).
- [[generating-functions](pages/generating-functions.md)] — the tool used throughout.
- [[stack-polyomino-gf](pages/stack-polyomino-gf.md)] — the "stack polyominoes" family this paper names, given a direct ordinary generating function (OGF) via the [[symbolic-method](pages/symbolic-method.md)] in Example I.8 of [[analytic-combinatorics-part-a](pages/analytic-combinatorics-part-a.md)] — a specification-driven alternative to this paper's add-a-column functional equation, applicable when the class has enough structure (like the unimodal skyline of a stack polyomino).

## Relation to Other Wiki Pages

Cited as a reference on [[project-euler-502-solution](pages/project-euler-502-solution.md)]. It is the polyomino-enumeration framework the castle problem most resembles — an add-a-column generating-function method for column-convex shapes — and the natural home for tracing the castle's column-independence, convexity, and stack/Ferrers threads into the literature. [[analytic-combinatorics-part-a](pages/analytic-combinatorics-part-a.md)] provides a complementary route: the [[symbolic-method](pages/symbolic-method.md)] constructs specific well-structured sub-families like [[stack-polyomino-gf](pages/stack-polyomino-gf.md)] directly, without a functional equation.

## Footnotes

[^1]: [[column-convex-polygon-enumeration](pages/column-convex-polygon-enumeration.md)] p.3 §2 — "for any 'natural' class of column-convex polyominoes, a functional equation that implicitly defines its generating function ... all the equations we thus obtain are of the same type ... solved in the same way ... both the way of establishing an equation and the way of solving it are systematic."
[^2]: [[column-convex-polygon-enumeration](pages/column-convex-polygon-enumeration.md)] p.1 §1 — "A polyomino is said to be vertically convex (or column-convex) when its intersection with any vertical line is convex ... A polyomino is convex if it is both vertically and horizontally convex."
[^3]: [[column-convex-polygon-enumeration](pages/column-convex-polygon-enumeration.md)] p.1 §1 — "let p(n) denote the number of polyominoes having n cells. Klarner and Rivest proved that (p(n))^{1/n} tends to a limit K, which satisfies 3.87 < K < 4.65 ... the first digit of K is not even known."
[^4]: [[column-convex-polygon-enumeration](pages/column-convex-polygon-enumeration.md)] p.3 §2, §2.1 — "a column-convex polyomino can be obtained by successively gluing columns ... sometimes known as 'Temperley methodology' ... three ways of adding a new column ... A(P) (resp. B(P), C(P)) ... the top-cell of the first column of Q is higher (resp. lower, lower) ... the bottom-cell ... lower (resp. lower, higher)."
[^5]: [[column-convex-polygon-enumeration](pages/column-convex-polygon-enumeration.md)] p.3 §2 — the generating function "∑_{P∈P} s^{l(P)} t^{r(P)} x^{h(P)} y^{v(P)} q^{a(P)}" tracking left/right-height, horizontal/vertical perimeter steps (h = width), and area.
[^6]: [[column-convex-polygon-enumeration](pages/column-convex-polygon-enumeration.md)] p.3 §1 — "some of them are only refinements of already known results (parallelogram polyominoes, directed and convex polyominoes, convex polyominoes) ... two others are new; we obtain the perimeter and area generating function of column-convex polygons, and of directed column-convex polygons."
[^7]: [[column-convex-polygon-enumeration](pages/column-convex-polygon-enumeration.md)] p.2 §1 — "three very classical families of directed and convex polyominoes: the Ferrers diagrams, the stack polyominoes, and finally the parallelogram (or staircase) polyominoes ... characterized ... by the fact that two or three vertices of the minimal bounding rectangle ... must also belong to the polyomino."
