---
title: Castle (polyomino)
category: Concepts
summary: A configuration of stacked integer-length unit-height blocks on a w×h grid, obeying the castle placement rules — the central object of study.
tags: [concept, castle, polyomino, combinatorics]
sources: [project-euler-502, project-euler-502-problem-setup, project-euler-502-representations, project-euler-502-castle-factoring]
created: 2026-09-13
updated: 2026-09-19
---

# Castle (polyomino)

## Description

A **castle** is the central object of study in this wiki: a configuration of stacked *blocks* on a bounded grid. A **block** is a rectangle of height 1 and integer-valued length.[^1] Castles are built on a game grid that is *w* units wide and *h* units tall, and a configuration is a valid castle when it obeys the following geometric and structural rules:[^2]

- **No overhangs, no floating blocks** — a block may rest on top of other blocks only where nothing sticks out past the edges or hangs over open space.
- **Grid-snapped** — every block is aligned to the integer grid.
- **Same-row spacing** — any two neighboring blocks on the same row are separated by at least one unit of empty space.
- **Full base** — the bottom row is occupied by a single block of length *w*.
- **Exact height** — the maximum achieved height of the entire castle is exactly *h*.

These five rules define the castle object **independent of how many blocks it contains** — a castle may be built from any number of blocks, even or odd. The general object of interest to this wiki is the castle as such, at any block count.

**Relationship to Project Euler 502.** Project Euler 502 counts a *restricted* family of castles: those made from an **even** number of blocks.[^3] This wiki treats that even-block requirement not as part of the definition of a castle, but as a parity restriction layered on top — a special case of the broader, more interesting problem of counting all castles regardless of block parity. The parity constraint is what gives PE 502 its particular character; the general castle (both parities) is the object this wiki ultimately cares about. The counting itself is carried by the [[castle-counting-function](pages/castle-counting-function.md)].

The name "castle polyomino" reflects the visual intuition: a valid configuration resembles the crenellated silhouette of a castle wall, and the connected cell-set it occupies relates it to the broader family of polyominoes.

**Encodings.** A castle can be encoded exactly in several ways — column-wise binary strings, integer height-tuples, or U/R/D step strings — each turning the placement rules into constraints on the encoding (see [[castle-representations](pages/castle-representations.md)]). In the U/R/D reading, a castle is `U (tower) D`, every `D` step completes one block, and validity is characterized by the absence of `UD` (a zero-width block) and `DU` (two touching blocks) in the tower word.

## Appearances in Sources

- [[project-euler-502](pages/project-euler-502.md)] — defines the block, the castle, and the five placement rules; adds the even-block parity restriction for the PE 502 count.
- [[project-euler-502-problem-setup](pages/project-euler-502-problem-setup.md)] — partially restates the rules (as Rule 1, 3, 4, 5, 6; not repeating Rule 2 is an incomplete restatement, not a change to the problem — no rule is dropped).
- [[project-euler-502-representations](pages/project-euler-502-representations.md)] — encodes the castle and characterizes validity in the U/R/D word (each D completes a block; no UD, no DU).
- [[project-euler-502-castle-factoring](pages/project-euler-502-castle-factoring.md)] — factors a castle via its column heights, reading peaks as cycle-like atoms (the permutation-cycle analogy).

## Related Concepts

- [[castle-counting-function](pages/castle-counting-function.md)] — `F(w,h)`, the function counting castles; PE 502's even-block count is a special case of counting the general castle object.
- [[castle-representations](pages/castle-representations.md)] — exact encodings of a castle (binary strings, integer tuples, U/R/D step strings).
- [[convex-castle](pages/convex-castle.md)] — a structurally important sub-class of castle.
- [[permutation-cycle-castle-analogy](pages/permutation-cycle-castle-analogy.md)] — the cycle-factorization reading of a castle.
- [[generating-functions](pages/generating-functions.md)] — the intended method for counting castle configurations at large parameters.
- [[castle-classification](pages/castle-classification.md)] — the framework organizing castle sub-families by skyline predicate; catalogs 42 types across 9 axes: 7 structural, plus a growth-type meta-classification (Axis 8) and a spectral one (Axis 9).

## Footnotes

[^1]: [[project-euler-502](pages/project-euler-502.md)] §"Project 502: Castle Polyominoes" L11 — "We define a block to be a rectangle with a height of 1 and an integer-valued length. Let a castle be a configuration of stacked blocks."
[^2]: [[project-euler-502](pages/project-euler-502.md)] §"Project 502: Castle Polyominoes" L13-19 [synthesis] — the placement rules: no sticking out or overhanging open space, grid-snapped, ≥1 unit gap between same-row neighbors, bottom row a block of length w, maximum height exactly h.
[^3]: [[project-euler-502](pages/project-euler-502.md)] §"Project 502: Castle Polyominoes" L20 — "The castle is made from an even number of blocks."
