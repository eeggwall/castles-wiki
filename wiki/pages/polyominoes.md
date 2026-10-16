---
title: Polyominoes
category: Sources
summary: The charlesreid1.com Polyominoes page defines a polyomino and its area, width and height, and lists five classes, Ferrers diagrams, staircase, bar chart, column-convex and directed polyominoes. It places castles among the column-convex polyominoes; in its own classes a castle is a bar chart polyomino, a bargraph. Its two-path description of Ferrers diagrams and its Catalan and q-Bessel statements for them belong to the parallelogram polyominoes, of which Ferrers diagrams are a special case.
tags: [polyomino, taxonomy, column-convex, ferrers, catalan, q-analog, bargraph, source]
sources: [polyominoes]
created: 2026-09-13
updated: 2026-10-16
---

# Polyominoes

**Source:** https://charlesreid1.com/wiki/Polyominoes
**Date ingested:** 2026-09-13
**Type:** article (MediaWiki topic page)

## Summary

A **polyomino** is a finite connected union of unit cells of the plane with no cut point. A column of a polyomino is its intersection with a vertical strip of cells. The **area** of a polyomino is its number of cells, its **height** the number of rows and its **width** the number of columns.[^1] The page lists five classes:[^2]

- **Ferrers diagrams**, built by gluing successively taller columns side by side, moving only east and north.[^3]
- **Staircase polyominoes**, which start at height 1 on the far left and usually change height by 1 per column, a convention that "varies from author to author".[^4]
- **Bar chart polyominoes**, columns of varied height on a common baseline, glued side by side.[^4]
- **Column-convex polyominoes**, in which every column is connected, so that a vertical line meets the polyomino in one segment.[^4]
- **Directed polyominoes**, listed without a description.[^2]

**Ferrers diagrams and parallelogram polyominoes.** The page also describes Ferrers diagrams by two non-intersecting paths of north and east steps, says that their perimeters are counted by the Catalan numbers, and says that their generating functions by area, width and height are related to q-Bessel functions and q-Catalan numbers.[^3] These three statements describe the **parallelogram polyominoes**, the polyominoes bounded by two north-east lattice paths that meet only at their ends. The parallelogram polyominoes of perimeter `2n + 2` number the Catalan number `C_n` ([[algebraic-languages-and-polyominoes-enumeration](pages/algebraic-languages-and-polyominoes-enumeration.md)]); their generating function by width, height and area is the q-Bessel quotient `y J_1/J_0` of [[bousquet-melou-fedou-1995-convex-polyominoes](pages/bousquet-melou-fedou-1995-convex-polyominoes.md)]; and by area they are counted by the Pólya-Gessel q-Catalan numbers ([[q-catalan-numbers](pages/q-catalan-numbers.md)]). A Ferrers diagram with columns `c_1 ≤ ⋯ ≤ c_w` on a common baseline is the parallelogram polyomino whose lower path is `w` east steps followed by `c_w` north steps. There are `C(w + h − 2, w − 1)` of them in a `w × h` bounding box, so `2^{s−2}` of semi-perimeter `s = w + h ≥ 2`.[^5] For example, the parallelogram polyominoes of semi-perimeter 4 number `C_3 = 5`, and four of them are Ferrers diagrams: the skylines `(1, 1, 1)`, `(1, 2)`, `(2, 2)` and `(3)`. The fifth is a column of two cells followed by one cell beside its top cell.

## Castles

The page states that "castle polyominoes are column-convex polyominoes built by stacking blocks under the 'no overhang, no adjacent same-row blocks, even block count' rules", with Project Euler 502 as the worked example that counts them by width `w` and height `h`, and points to the three encodings of the Representations subpage ([[project-euler-502](pages/project-euler-502.md)], [[project-euler-502-representations](pages/project-euler-502-representations.md)]).[^6] The even-block rule selects the castles counted by `A^e(w, h)`; the wiki's castles have any number of blocks ([[castle-counting-function](pages/castle-counting-function.md)]). In the page's own classes a castle is a bar chart polyomino: its columns stand on a common baseline, the full bottom row ([[castle-polyomino](pages/castle-polyomino.md)]).

## Key Takeaways

- A polyomino is a finite connected union of cells with no cut point; its area, height and width are its numbers of cells, rows and columns.[^1]
- The five classes are Ferrers diagrams, staircase, bar chart, column-convex and directed polyominoes.[^2]
- The page places castles among the column-convex polyominoes; a castle is a bar chart polyomino.[^6]
- The page's two-path description, Catalan count and q-Bessel statement for Ferrers diagrams hold for the parallelogram polyominoes; Ferrers diagrams number `2^{s−2}` by semi-perimeter `s`.[^3][^5]

## Entities & Concepts

- [[castle-polyomino](pages/castle-polyomino.md)] - the castle as a skyline, and as a bargraph of the polyomino literature.
- [[column-convex-polyomino](pages/column-convex-polyomino.md)] - the column-convex polyominoes.
- [[convex-polyomino](pages/convex-polyomino.md)] - the polyominoes that are both row-convex and column-convex.
- [[convex-polyomino-by-area](pages/convex-polyomino-by-area.md)] - the Ferrers, stack, parallelogram, directed convex and convex polyominoes counted by area, with the bargraphs and the column-convex polyominoes.
- [[parallelogram-polyomino-dyck-bijection](pages/parallelogram-polyomino-dyck-bijection.md)] - parallelogram polyominoes of perimeter `2n + 2` and the Dyck words of length `2n`, with area as the sum of peak heights.
- [[q-catalan-numbers](pages/q-catalan-numbers.md)] - the q-Catalan numbers, among them the Pólya-Gessel count of parallelogram polyominoes by area.
- [[bousquet-melou-fedou-1995-convex-polyominoes](pages/bousquet-melou-fedou-1995-convex-polyominoes.md)] - the parallelogram, directed convex and convex polyominoes by width, height and area, as quotients of q-Bessel series.
- [[prellberg-brak-1995-cluster-models](pages/prellberg-brak-1995-cluster-models.md)] - functional equations for bar-graph polygons, which are the castles, by width, blocks and area.
- [[inscribed-polyomino](pages/inscribed-polyomino.md)] - the polyominoes with bounding box `w × h`, among which the castles are the bargraphs.

Also linked from the source: [[dyck-words](pages/dyck-words.md)], [[lattice-paths](pages/lattice-paths.md)].

## Relation to Other Wiki Pages

The page lists neither the stack polyominoes nor, by name, the parallelogram polyominoes. A stack polyomino, a unimodal skyline on a full bottom row, is a [[convex-castle](pages/convex-castle.md)]; Flajolet and Sedgewick count the stacks by area in Example I.8 ([[analytic-combinatorics-ch1-ogfs](pages/analytic-combinatorics-ch1-ogfs.md)], [[stack-polyomino-gf](pages/stack-polyomino-gf.md)]). Ferrers diagrams, stacks and parallelograms are the three classical directed convex families of [[column-convex-polygon-enumeration](pages/column-convex-polygon-enumeration.md)]. Delest and Viennot cut every convex polyomino into a parallelogram polyomino and two stacks and count the convex polyominoes by perimeter ([[algebraic-languages-and-polyominoes-enumeration](pages/algebraic-languages-and-polyominoes-enumeration.md)]).

## Footnotes

[^1]: [[polyominoes](pages/polyominoes.md)] (lead) L7-13 - "A cell is a unit square in π, and a polyomino is a finite connected union of cells having no cut point. A column of polyominoes is the intersection between the polyomino and an infinite vertical strip of cells. The area of a polyomino is a count of its cells. The height of a polyomino is the number of rows. The width of a polyomino is the number of columns."
[^2]: [[polyominoes](pages/polyominoes.md)] §"Classes of Polyominoes" L15-22 - "Classes of polyominoes include: Ferrer diagrams, Staircase polyominoes, Bar chart polyominoes, Column-convex polyominoes, Directed polyominoes"; Directed polyominoes have no subsection.
[^3]: [[polyominoes](pages/polyominoes.md)] §"Ferrers Diagrams" L26-30 - "The polyomino is constructed by gluing successively taller columns together, only moving east and north", "These are defined by two non-intersecting paths having only north or east steps", "The perimeter of these polyominoes are enumerated by the Catalan numbers. Their generating functions according to area, width, and height are related to q-Bessel functions and q-Catalan numbers."
[^4]: [[polyominoes](pages/polyominoes.md)] §"Staircase Polyominoes", §"Bar Chart Polyominoes", §"Column Convex Polyominoes" L34-42 - "Staircase polyominoes begin with a height of 1 on the far left. These usually increase or decrease in height by 1 unit at a time, but that varies from author to author", "Bar chart polyominoes consist of columns of varied height, but sharing a common baseline, glued together side by side", "A column convex polyomino is one in which all columns are connected."
[^5]: Verified by execution (Python 3.11, 2026-10-16): enumeration of parallelogram polyominoes by width and height for semi-perimeter at most 7 gives the Catalan numbers 1, 1, 2, 5, 14, 42 and the Narayana rows; Ferrers diagrams number 2^{s−2} for 2 ≤ s ≤ 12.
[^6]: [[polyominoes](pages/polyominoes.md)] §"Column-convex castle polyominoes" L46 - "Castle polyominoes are column-convex polyominoes built by stacking blocks under the \"no overhang, no adjacent same-row blocks, even block count\" rules. Project Euler/502 is a worked example: it counts castle polyominoes of width w and height h, and its Project Euler/502/Representations page walks through three encodings of them."
