---
title: Polyominoes
category: Sources
summary: The charlesreid1.com polyomino taxonomy — Ferrers, staircase, bar-chart, column-convex, directed — placing the castle as a column-convex polyomino and linking the Catalan / q-Bessel / q-Catalan generating-function threads.
tags: [polyomino, taxonomy, column-convex, ferrers, catalan, q-analog, source]
sources: [polyominoes]
created: 2026-09-13
updated: 2026-09-13
---

# Polyominoes

**Source:** https://charlesreid1.com/wiki/Polyominoes
**Date ingested:** 2026-09-13
**Type:** article (MediaWiki topic page)

## Summary

A **polyomino** is a finite connected union of unit cells in the plane with no cut point; its **area** is the cell count, **height** the number of rows, **width** the number of columns.[^1] The page lays out the main classes and — importantly for this wiki — places the castle explicitly among them.[^2]

The classes:[^2]

- **Ferrers diagrams** — built by gluing successively taller columns moving only east and north (equivalently, two non-intersecting N/E paths). Their **perimeter is enumerated by the Catalan numbers**, and their generating functions by area/width/height relate to **q-Bessel functions and q-Catalan numbers**.[^3]
- **Staircase polyominoes** — height 1 at the far left, changing by ±1 per column (convention-dependent).
- **Bar-chart polyominoes** — columns of varied height on a common baseline, glued side by side.
- **Column-convex polyominoes** — every column connected (a vertical line meets the shape in one segment); see [[column-convex-polyomino](pages/column-convex-polyomino.md)].
- **Directed polyominoes** — a reachability-from-a-root condition (statistical-physics origin).

## The castle in the taxonomy

The page states directly that **castle polyominoes are column-convex polyominoes** built by stacking blocks under the "no overhang, no adjacent same-row blocks, even block count" rules, with [[project-euler-502](pages/project-euler-502.md)] as the worked example (counting castles of width *w* and height *h*, three encodings on [[project-euler-502-representations](pages/project-euler-502-representations.md)]).[^4] This is the wiki's own upstream confirmation of the placement worked out from the literature on [[column-convex-polyomino](pages/column-convex-polyomino.md)] and [[convex-castle](pages/convex-castle.md)].

Two of the named families are exactly the OEIS-mining threads: **Ferrers/staircase/parallelogram** are the classical directed-convex families of [[column-convex-polygon-enumeration](pages/column-convex-polygon-enumeration.md)], and the **Ferrers → q-Bessel / q-Catalan** remark is the same q-analog thread as the steep-parallelogram generating functions of [[steep-polyominoes-q-motzkin-bessel](pages/steep-polyominoes-q-motzkin-bessel.md)]. This page is thus the taxonomic hub tying the castle to the whole polyomino world and pointing at the q-graded direction (see the wiki TODO).

## Key Takeaways

- Polyomino = connected cut-point-free union of cells; parameters area, width, height.[^1]
- Classes: Ferrers, staircase, bar-chart, column-convex, directed.[^2]
- **The castle is a column-convex polyomino** (with the extra no-overhang / same-row-gap / even-count rules); PE 502 is the worked instance.[^4]
- **Ferrers polyominoes** connect to Catalan (perimeter) and to **q-Bessel / q-Catalan** (area/width/height g.f.) — the q-analog thread.[^3]

## Entities & Concepts

- [[column-convex-polyomino](pages/column-convex-polyomino.md)] — the class the castle belongs to.
- [[castle-polyomino](pages/castle-polyomino.md)], [[convex-castle](pages/convex-castle.md)] — the castle and its convex sub-class.
- [[q-catalan-numbers](pages/q-catalan-numbers.md)], [[motzkin-numbers](pages/motzkin-numbers.md)] — the q-analog / Motzkin threads the Ferrers remark points to.
- [[column-convex-polygon-enumeration](pages/column-convex-polygon-enumeration.md)], [[steep-polyominoes-q-motzkin-bessel](pages/steep-polyominoes-q-motzkin-bessel.md)] — the papers on these families.

Linked from the source but not yet ingested: Dyck Words, Lattice Paths, Combinatorics.

## Relation to Other Wiki Pages

This is the taxonomy that situates the castle, and the upstream source for "castle = column-convex polyomino." It closes several of the wiki's outstanding "Polyominoes (not yet ingested)" placeholders and connects the castle directly to the Ferrers/parallelogram families and the q-Bessel/q-Catalan generating-function world.

## Footnotes

[^1]: [[polyominoes](pages/polyominoes.md)] §(lead) L1-13 — "a polyomino is a finite connected union of cells having no cut point ... The area of a polyomino is a count of its cells. The height ... is the number of rows. The width ... is the number of columns."
[^2]: [[polyominoes](pages/polyominoes.md)] §"Classes of Polyominoes" L15-42 — "Ferrer diagrams, Staircase polyominoes, Bar chart polyominoes, Column-convex polyominoes, Directed polyominoes" with each subsection's description.
[^3]: [[polyominoes](pages/polyominoes.md)] §"Ferrers Diagrams" L26-30 — "constructed by gluing successively taller columns ... only moving east and north ... The perimeter of these polyominoes are enumerated by the Catalan numbers. Their generating functions according to area, width, and height are related to q-Bessel functions and q-Catalan numbers."
[^4]: [[polyominoes](pages/polyominoes.md)] §"Column-convex castle polyominoes" L44-46 — "Castle polyominoes are column-convex polyominoes built by stacking blocks under the 'no overhang, no adjacent same-row blocks, even block count' rules. Project Euler/502 is a worked example ... counts castle polyominoes of width w and height h."
