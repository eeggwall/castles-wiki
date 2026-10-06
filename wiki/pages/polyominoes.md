---
title: Polyominoes
category: Sources
summary: The charlesreid1.com polyomino taxonomy — Ferrers, staircase, bar-chart, column-convex, directed — placing the castle as a column-convex polyomino and linking the Catalan / q-Bessel / q-Catalan generating-function threads. AC's stack polyomino (Example I.8) is the convex castle, built by the symbolic method.
tags: [polyomino, taxonomy, column-convex, ferrers, catalan, q-analog, stack-polyomino, source]
sources: [polyominoes, bousquet-melou-fedou-1995-convex-polyominoes, algebraic-languages-and-polyominoes-enumeration]
created: 2026-09-13
updated: 2026-10-06
---

# Polyominoes

**Source:** https://charlesreid1.com/wiki/Polyominoes
**Date ingested:** 2026-09-13
**Type:** article (MediaWiki topic page)

## Summary

A **polyomino** is a finite connected union of unit cells in the plane with no cut point; its **area** is the cell count, **height** the number of rows, **width** the number of columns.[^1] The page lays out the main classes and places the castle among them.[^2]

The classes:[^2]

- **Ferrers diagrams** — built by gluing successively taller columns moving only east and north (equivalently, two non-intersecting N/E paths). Their generating functions by area/width/height relate to **q-Bessel functions and q-Catalan numbers**.[^3]
- **Staircase polyominoes** — height 1 at the far left, changing by ±1 per column (convention-dependent).
- **Bar-chart polyominoes** — columns of varied height on a common baseline, glued side by side.
- **Column-convex polyominoes** — every column connected (a vertical line meets the shape in one segment); see [[column-convex-polyomino](pages/column-convex-polyomino.md)].
- **Directed polyominoes** — a reachability-from-a-root condition (statistical-physics origin).

## The castle in the taxonomy

The page states directly that **castle polyominoes are column-convex polyominoes** built by stacking blocks under the "no overhang, no adjacent same-row blocks, even block count" rules, with [[project-euler-502](pages/project-euler-502.md)] as the worked example (counting castles of width *w* and height *h*, three encodings on [[project-euler-502-representations](pages/project-euler-502-representations.md)]).[^4] This agrees with the placement worked out from the literature on [[column-convex-polyomino](pages/column-convex-polyomino.md)] and [[convex-castle](pages/convex-castle.md)].

Two of the named families lead to other pages: **Ferrers** and **staircase** polyominoes, with the parallelogram polyominoes, are the classical directed-convex families of [[column-convex-polygon-enumeration](pages/column-convex-polygon-enumeration.md)], and the **Ferrers → q-Bessel / q-Catalan** remark is the q-analog thread of the steep-parallelogram generating functions of [[steep-polyominoes-q-motzkin-bessel](pages/steep-polyominoes-q-motzkin-bessel.md)].

**Not in this page's taxonomy: the [[stack-polyomino-gf](pages/stack-polyomino-gf.md)]** (unimodal-skyline polyominoes), constructed in Example I.8 of [[analytic-combinatorics-ch1-ogfs](pages/analytic-combinatorics-ch1-ogfs.md)] by the [[symbolic-method](pages/symbolic-method.md)]. A stack polyomino is a unimodal skyline on a full bottom row, that is, a [[convex-castle](pages/convex-castle.md)], counted by area ([[convex-castle-binomial-identity](pages/convex-castle-binomial-identity.md)] counts it by width and height).

**Convex polyominoes and their trisection.** Delest and Viennot cut every convex polyomino (column- and row-convex) by the vertical lines through its lowest-leftmost and highest-rightmost boundary points. This gives a **parallelogram polyomino** in the middle and two **stack polyominoes** on the sides. By perimeter, parallelograms are Catalan (Dyck words, with area = Σ peak heights; [[parallelogram-polyomino-dyck-bijection](pages/parallelogram-polyomino-dyck-bijection.md)]), stacks are Fibonacci, and convex polyominoes total `(2n+11)4^n - 4(2n+1)C(2n,n)` at perimeter `2n+8` (A005436).[^5] The stack is the castle's own convex sub-family ([[convex-castle](pages/convex-castle.md)]).

## Key Takeaways

- Polyomino = connected cut-point-free union of cells; parameters area, width, height.[^1]
- Classes: Ferrers, staircase, bar-chart, column-convex, directed.[^2]
- **The castle is a column-convex polyomino** (with the extra no-overhang / same-row-gap / even-count rules); Project Euler 502 (PE 502) is the worked instance.[^4]
- **Ferrers polyominoes** connect to **q-Bessel / q-Catalan** (area/width/height GF), the q-analog thread.[^3]

## Entities & Concepts

- [[column-convex-polyomino](pages/column-convex-polyomino.md)] — the class the castle belongs to.
- [[convex-polyomino](pages/convex-polyomino.md)], [[convex-polyomino-by-area](pages/convex-polyomino-by-area.md)] - the row- and column-convex class, its corner taxonomy, and every sub-family counted by area.
- [[castle-polyomino](pages/castle-polyomino.md)], [[convex-castle](pages/convex-castle.md)] — the castle and its convex sub-class.
- [[stack-polyomino-gf](pages/stack-polyomino-gf.md)] — the unimodal-skyline sub-family; the AC-native "castle tower with one peak" via the symbolic method.
- [[algebraic-languages-and-polyominoes-enumeration](pages/algebraic-languages-and-polyominoes-enumeration.md)] / [[parallelogram-polyomino-dyck-bijection](pages/parallelogram-polyomino-dyck-bijection.md)] - convex polyominoes by perimeter via the stack / parallelogram / stack trisection.
- [[q-catalan-numbers](pages/q-catalan-numbers.md)], [[motzkin-numbers](pages/motzkin-numbers.md)] — the q-analog / Motzkin threads the Ferrers remark points to.
- [[column-convex-polygon-enumeration](pages/column-convex-polygon-enumeration.md)], [[steep-polyominoes-q-motzkin-bessel](pages/steep-polyominoes-q-motzkin-bessel.md)], [[klarner-rivest-1974-convex-n-ominoes](pages/klarner-rivest-1974-convex-n-ominoes.md)] — the papers on these families; the last gives the convex growth constant `2.309138...`.
- [[prellberg-brak-1995-cluster-models](pages/prellberg-brak-1995-cluster-models.md)] — bar-chart (bar-graph) polygons by width, perimeter and area; with `y` on vertical steps their equation (3.11) is the castle GF by blocks.
- [[castle-strip](pages/castle-strip.md)] — a castle read column by column under a neighbor rule; the transfer-matrix form of gluing columns side by side.
- [[inscribed-polyomino](pages/inscribed-polyomino.md)] / [[marin-2024-polyominoes-in-rectangle](pages/marin-2024-polyominoes-in-rectangle.md)] — all fixed polyominoes with bounding box `w × h`, counted by a row automaton; the castles are its bargraphs.

Related topics: [[dyck-words](pages/dyck-words.md)], [[lattice-paths](pages/lattice-paths.md)].

## Relation to Other Wiki Pages

This is the taxonomy that situates the castle, and the upstream source for "castle = column-convex polyomino." It connects the castle to the Ferrers/parallelogram families and the q-Bessel/q-Catalan generating-function world. The area generating functions of the parallelogram, directed-convex and convex families, as q-Bessel quotients, are on [[bousquet-melou-fedou-1995-convex-polyominoes](pages/bousquet-melou-fedou-1995-convex-polyominoes.md)].

## Footnotes

[^1]: [[polyominoes](pages/polyominoes.md)] §(lead) L1-13 — "a polyomino is a finite connected union of cells having no cut point ... The area of a polyomino is a count of its cells. The height ... is the number of rows. The width ... is the number of columns."
[^2]: [[polyominoes](pages/polyominoes.md)] §"Classes of Polyominoes" L15-42 — "Ferrer diagrams, Staircase polyominoes, Bar chart polyominoes, Column-convex polyominoes, Directed polyominoes" with each subsection's description.
[^3]: [[polyominoes](pages/polyominoes.md)] §"Ferrers Diagrams" L26-30 — "constructed by gluing successively taller columns ... only moving east and north ... These are defined by two non-intersecting paths having only north or east steps ... Their generating functions according to area, width, and height are related to q-Bessel functions and q-Catalan numbers."
[^4]: [[polyominoes](pages/polyominoes.md)] §"Column-convex castle polyominoes" L44-46 — "Castle polyominoes are column-convex polyominoes built by stacking blocks under the 'no overhang, no adjacent same-row blocks, even block count' rules. Project Euler/502 is a worked example ... counts castle polyominoes of width w and height h."
[^5]: [[algebraic-languages-and-polyominoes-enumeration](pages/algebraic-languages-and-polyominoes-enumeration.md)] pp.176-181 §3 and p.171 Thm 1.1 [synthesis] - the trisection by the vertical lines through S and N into a parallelogram part and two stack parts; Lemma 3.1 (parallelograms: Catalan), Lemma 3.2 (stacks: Fibonacci), and "p_{2n+8} = (2n+11)4^n - 4(2n+1)C(2n,n)".
