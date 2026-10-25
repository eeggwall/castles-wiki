---
title: Castle classification
category: Concepts
summary: The hub of the castle classification, at three scopes. Shape types are predicates on one castle's skyline (the 42 types of the Castle Types source plus ridge, hoodoo and monadnock castles). Spectral types are predicates on the spectrum of one castle's graph (tree castles, castles golden and silver by spectrum, isospectral pairs, Ramanujan castles, sparse-spectrum castles). Growth types classify families of castles by the growth constant of their count along a named axis ("golden by width", "tribonacci by area"). Compressibility is a separate invariant on castle-compression.
tags: [concept, castle, classification, taxonomy, hub, scope, shape, spectral, growth]
sources: [project-euler-502-representations]
created: 2026-09-15
updated: 2026-10-25
---

# Castle classification

The wiki classifies castles at three **scopes**: a shape type is a property of one castle's skyline, a spectral type a property of the spectrum of one castle's graph, and a growth type a property of a family of castles. Each scope has its own page; this page maps them.

## Castles and types

A castle of width `w` and height `h` is determined by its skyline, the column heights[^1]

```
(c_1, c_2, …, c_w)      with 1 ≤ c_i ≤ h and some c_i = h
```

([[castle-polyomino](pages/castle-polyomino.md)]). Every castle is column-convex, each column one vertical run of cells from row 1, and its bottom row is full. A **castle type** is a further condition on the castle, and the conditions come in three kinds.

## The three scopes

| scope | what is classified | the invariant | named types | page |
|---|---|---|---|---|
| **shape** | one castle | a predicate on the skyline `(c_1, …, c_w)` | unimodal, Ferrers, staircase, palindromic, Dyck-path, Motzkin-path, rainbow, hook, crenellated, m-smooth, m-disparate, …: the 42 types of the Castle Types source in seven groups, plus ridge, hoodoo and monadnock castles | [[castle-classification-shape](pages/castle-classification-shape.md)] |
| **spectrum** | one castle | a spectrum of its castle graph ([[castle-graph](pages/castle-graph.md)]) or of its skyline | tree castles; castles golden by spectrum (spectral radius `φ`) and silver by spectrum (`1 + √2`); spectral radius `φ²`; isospectral pairs; Ramanujan castles; sparse-spectrum castles | [[castle-classification-spectrum](pages/castle-classification-spectrum.md)] |
| **growth** | a family of castles defined by a rule | the growth constant of the family's count along a named axis: width, height, area or semi-perimeter | golden, silver, bronze, copper and nickel by width; `δ_4`, `δ_5`, … by width; tribonacci, tetranacci, supergolden, plastic and `ψ²` by area | [[castle-classification-growth](pages/castle-classification-growth.md)] |

The shape and spectral scopes classify one castle, but they read it differently. A shape predicate reads the skyline directly. A spectral predicate builds the castle graph, with the cells as vertices and an edge between cells that share a side, and reads the eigenvalues of a matrix attached to it. The graph is determined by the skyline, so every spectral type is a function of the skyline, and a coarser one: different skylines can have isomorphic graphs (the six castles whose graph is the path `P_4`), and non-isomorphic graphs can have the same spectrum ([[isospectral-castles](pages/isospectral-castles.md)]).

The growth scope classifies a family defined by a rule (a rule on neighboring columns, the ridge rule, the tree condition, or any predicate that defines an infinite set of castles) by how fast the number of its castles grows. "Silver by width" is a property of such a family, not of one castle. A shape or spectral predicate defines a family, and that family has a growth type: the tree castles of height 2, a spectral type and a shape type at once, are golden by width ([[castle-classification-growth](pages/castle-classification-growth.md)], the section *Statements across scopes*). The tree condition is a shape condition and a graph condition at once, since a castle graph is a tree exactly when no `2 × 2` square of cells is filled ([[castle-graph](pages/castle-graph.md)]).

Compressibility, the length of the shortest description of a castle, is a separate invariant, with three description tiers that cut across the three scopes ([[castle-compression](pages/castle-compression.md)]).

## Parity

Project Euler 502 counts the castles with an even number of blocks. Every type is defined without the parity condition, and the even-block members of a type are counted by `A^e = (A + S)/2`, with `S` the signed count over its castles ([[castle-sign](pages/castle-sign.md)]). For some types the parity is fixed by the shape: a convex (unimodal) castle of height `h` has exactly `h` blocks, one per row ([[convex-castle](pages/convex-castle.md)], section *Block count*), so all convex castles of height `h` have the parity of `h`, and the even-block condition keeps all of them or none.[^2]

## Source

The shape types are taken from `charlesreid1.com/wiki/Project_Euler/502/Castle_Types` (fetched 2026-09-15, cached at `raw/castle-types.wiki`). It defines 42 types as predicates on the skyline: 7 base types from the polyomino literature (column-convex, unimodal, directed, parallelogram, Ferrers, staircase, m-disparate) and 35 further types.[^3] [[castle-classification-shape](pages/castle-classification-shape.md)] groups them into seven groups and links each to the wiki page that treats it. The spectral, growth and compressibility scopes are the wiki's own.

## Related Concepts

- [[castle-classification-shape](pages/castle-classification-shape.md)] - the shape types, each with its predicate, an example skyline and a count where one is known.
- [[castle-classification-spectrum](pages/castle-classification-spectrum.md)] - the spectral types: tree castles, castles golden and silver by spectrum, isospectral pairs, Ramanujan and sparse-spectrum castles.
- [[castle-classification-growth](pages/castle-classification-growth.md)] - the growth types by width, height, area and semi-perimeter, with the families that realize each constant.
- [[castle-compression](pages/castle-compression.md)] - the description tiers of castles: parametric, rule-generated and generic.
- [[castle-polyomino](pages/castle-polyomino.md)] - the castle definition.
- [[castle-representations](pages/castle-representations.md)] - the skyline and the other encodings of a castle.
- [[castle-graph](pages/castle-graph.md)] - the castle graph, its invariants, and the tree castles.
- [[castle-strip](pages/castle-strip.md)] - families defined by a rule on neighboring columns, counted by a transfer matrix whose largest eigenvalue is the growth constant by width.
- [[castle-eigenvalues-by-example](pages/castle-eigenvalues-by-example.md)] - small castles with their adjacency spectra computed by hand, and the other matrices whose eigenvalues appear on the wiki.
- [[castle-sign](pages/castle-sign.md)] - the sign `(−1)^{blocks}` and the split into even-block and odd-block castles.
- [[convex-castle](pages/convex-castle.md)] - the convex castles, whose block count equals their height.
- [[spectral-analysis](pages/spectral-analysis.md)] - the spectra computed for castles and what each decides.
- [[ramanujan-castles](pages/ramanujan-castles.md)] - every castle with at most 14 cells is Ramanujan; the smallest exceptions have 15 cells.
- [[bronze-castle-hunt](pages/bronze-castle-hunt.md)] - the search for a castle whose graph has spectral radius bronze.
- [[castle-snippets](pages/castle-snippets.md)] - tested Python snippets for the shape predicates and the castle graph.
- [[castle-native-gray-tour](pages/castle-native-gray-tour.md)] - Gray tours on the even-block castles of small width and height.
- [[area-growth-census](pages/area-growth-census.md)] - the growth constants by area of all strip rules through height 5; the smallest above 1 at height `h ≥ 2` is the root of `z^{h(h+1)/2} − z − 1`, the plastic number at `h = 2`, and it first appears at height `h`.

## Footnotes

[^1]: raw/castle-types.wiki L1-L9 - "A castle on a w × h grid is determined by its skyline, the sequence of column heights c_1, c_2, …, c_w with 1 ≤ c_i ≤ h and max_i c_i = h. (Problem 502 also requires an even number of blocks; the types below mostly ignore, or independently re-impose, that parity rule.) Every castle is automatically column-convex and bottom-aligned, so each type is a further restriction on the skyline." (Source: https://charlesreid1.com/wiki/Project_Euler/502/Castle_Types, fetched 2026-09-15.)
[^2]: [[project-euler-502-representations](pages/project-euler-502-representations.md)] §"Steps-Based Approach" L88-90, §"The tower word" L229 [synthesis] - the word of a convex castle has a front of `U` and `R` steps with "No D steps" and a back of `D` and `R` steps with "No U steps", so it has one `U` per row, and "blocks in the tower = number of D's = number of U's". Verified by execution (Python 3.11, 2026-10-25): every unimodal skyline of height `h` has `h` blocks, for `w ≤ 8`, `h ≤ 6` with `h^w ≤ 400000`.
[^3]: raw/castle-types.wiki §"Base types" L11-L19 and §"Proposed additional types" L21-L57 [synthesis] - the 7 base types and the 35 numbered proposed types, all stated as skyline predicates.
