---
title: Column-convex polyomino
category: Concepts
summary: A polyomino whose intersection with any vertical line is contiguous (each column an unbroken run); the framework class the castle most resembles, enumerated by the add-a-column method — or by [[symbolic-method]] specification, as with [[stack-polyomino-gf]] (Analytic Combinatorics Ex. I.8).
tags: [concept, polyomino, column-convex, convexity, combinatorics, symbolic-method]
sources: [column-convex-polygon-enumeration, analytic-combinatorics-part-a]
created: 2026-09-13
updated: 2026-09-15
---

# Column-convex polyomino

## Description

A **column-convex** (equivalently **vertically convex**) polyomino is one whose intersection with any vertical line is convex — i.e. each column is a single contiguous run of cells, with no vertical gaps.[^1] A polyomino that is both column-convex and row-convex ([[horizontally-convex-polyomino](pages/horizontally-convex-polyomino.md)]) is called **convex**.[^1] Column-convex polyominoes are the setting for a large, well-developed enumeration literature (see [[column-convex-polygon-enumeration](pages/column-convex-polygon-enumeration.md)]), including the classical directed-and-convex families — **Ferrers diagrams, stack polygons, and parallelogram/staircase polyominoes**.[^2]

The defining tool is the **add-a-column ("Temperley") method**: build the polyomino by gluing columns left to right, classifying each new column by how its top and bottom cells sit relative to the previous column, and turn that into a functional equation for a generating function tracking perimeter, area, and column heights.[^3]

**Alternative construction: the [[symbolic-method](pages/symbolic-method.md)].** For unimodal-skyline column-convex polyominoes — the [[stack-polyomino-gf](pages/stack-polyomino-gf.md)] family — Example I.8 of [[analytic-combinatorics-part-a](pages/analytic-combinatorics-part-a.md)] gives the OGF directly by a Durfee-square-style specification, no add-a-column functional equation needed. The two approaches co-exist: add-a-column handles arbitrary column-convex shapes via a functional equation; the symbolic method handles well-structured sub-families (unimodal, restricted parts, etc.) directly.[^4]

## Relation to the castle

Of all the external shape families in the wiki, the column-convex polyomino is the closest structural relative of the [[castle-polyomino](pages/castle-polyomino.md)]:

- A castle is built on a full-width base with contiguous vertical stacks — a strongly column-structured object; whether every castle is literally column-convex (and which column-convex polyominoes are castles) is a precise correspondence worth working out.
- The add-a-column method **is** the castle's width-direction recurrence in mature form: the castle counts towers column by column via the [[binary-string-bijection](pages/binary-string-bijection.md)] and column independence (`T(k,L)=(k+1)^L`), which is a particularly clean instance of gluing columns.
- The castle's own [[convex-castle](pages/convex-castle.md)] (a skyline convexity) and the classical **stack polygon / parallelogram** families are near neighbors; mapping castle sub-families onto these is a live thread.

## Appearances in Sources

- [[column-convex-polygon-enumeration](pages/column-convex-polygon-enumeration.md)] — defines column-convexity and enumerates its classes by the add-a-column method.
- [[analytic-combinatorics-part-a](pages/analytic-combinatorics-part-a.md)] — Example I.8 pp. 45-46 constructs the unimodal-skyline sub-family (stack polyominoes) directly by the symbolic method.

## Related Concepts

- [[castle-polyomino](pages/castle-polyomino.md)] — the castle, a column-structured object closely related to this class.
- [[horizontally-convex-polyomino](pages/horizontally-convex-polyomino.md)] — the row-convex counterpart; both together give convex polyominoes.
- [[convex-castle](pages/convex-castle.md)] — the castle's own convexity notion.
- [[stack-polyomino-gf](pages/stack-polyomino-gf.md)] — the unimodal-skyline sub-family, with a symbolic-method OGF.
- [[symbolic-method](pages/symbolic-method.md)] — the AC framework used for the stack-polyomino construction.

## Footnotes

[^1]: [[column-convex-polygon-enumeration](pages/column-convex-polygon-enumeration.md)] p.1 §1 — "A polyomino is said to be vertically convex (or column-convex) when its intersection with any vertical line is convex ... A polyomino is convex if it is both vertically and horizontally convex."
[^2]: [[column-convex-polygon-enumeration](pages/column-convex-polygon-enumeration.md)] p.2 §1 — "three very classical families of directed and convex polyominoes: the Ferrers diagrams, the stack polyominoes, and finally the parallelogram (or staircase) polyominoes."
[^3]: [[column-convex-polygon-enumeration](pages/column-convex-polygon-enumeration.md)] p.3 §2 — "a column-convex polyomino can be obtained by successively gluing columns ... 'Temperley methodology' ... a functional equation that implicitly defines its generating function."
[^4]: [[analytic-combinatorics-part-a](pages/analytic-combinatorics-part-a.md)] Example I.8 pp. 45-46 — "A stack polyomino is the diagram of a composition such that for some j, ℓ, one has 1 ≤ x_1 ≤ x_2 ≤ … ≤ x_j ≥ x_{j+1} ≥ … ≥ x_ℓ ≥ 1 ... translates immediately into the OGF S(z) = ∑_{k≥1} z^k/(1−z^k) · 1/((1−z)(1−z²)···(1−z^{k−1}))²."
