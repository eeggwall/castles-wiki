---
title: "Project Euler 502: Castle Polyominoes"
category: Sources
summary: The Project Euler 502 hub page — defines the castle object, the counting function F(w,h), and links the solution's subpages.
tags: [project-euler, castle, polyomino, source, hub]
sources: [project-euler-502]
created: 2026-09-13
updated: 2026-09-13
---

# Project Euler 502: Castle Polyominoes

**Source:** https://charlesreid1.com/wiki/Project_Euler/502 (mirrors [Project Euler problem 502](https://projecteuler.net/problem=502))
**Date ingested:** 2026-09-13
**Type:** article (MediaWiki hub page)

## Summary

This is the hub page for Project Euler problem 502 on the charlesreid1.com wiki. It states the problem, defines the central object — a **[[castle-polyomino](pages/castle-polyomino.md)]** — and introduces the counting function that the problem asks about. A castle is a configuration of stacked *blocks*, where a block is a height-1 rectangle of integer length, arranged on a game grid *w* units wide and *h* units tall.[^1]

The problem asks for the value of a specific counting function, the **[[castle-counting-function](pages/castle-counting-function.md)]** `F(w,h)`, evaluated at three large grid sizes and summed modulo 1,000,000,007.[^2] The Project Euler formulation restricts the count to castles built from an **even** number of blocks[^3] — a parity constraint that, in this wiki's framing, is a *special case* of the more general and more interesting problem of counting all castles regardless of block parity.

The page functions as an index into a worked solution: it links seven subpages covering the problem setup, three encodings of a castle, a cycle-factorization reading, key observations, the full mathematical solution, implementation notes for the Java program, and a Python brute-force cross-check.[^4] It also situates the problem within a cluster of related combinatorial topics — polyominoes, Dyck words, lattice paths, combinatorics, and generating functions.[^5] The problem was first discussed in July 2017 and solved March 31, 2026.[^6]

## Key Takeaways

- A **castle** is a configuration of stacked blocks (a block = a height-1, integer-length rectangle) on a *w*×*h* grid, governed by a fixed set of geometric/structural rules: no overhangs or floating blocks, grid-snapped placement, at least one unit of gap between neighboring blocks on the same row, a bottom row occupied by a single block of length *w*, and a maximum height of exactly *h*.[^1]
- Project Euler 502 adds one further constraint on top of the castle definition — the castle must use an **even** number of blocks[^3] — and this wiki treats that even/odd restriction as a special case of counting the general castle object (see [[castle-counting-function](pages/castle-counting-function.md)]).
- The counting function `F(w,h)` returns the number of valid castles for grid parameters *w* and *h*. Known checkpoints: `F(4,2) = 10`, `F(13,10) = 3729050610636`, `F(10,13) = 37959702514`, and `F(100,100) mod 1,000,000,007 = 841913936`.[^7]
- The problem's answer is `(F(10^12,100) + F(10000,10000) + F(100,10^12)) mod 1,000,000,007`.[^2]
- The solution is decomposed across subpages by theme: setup, representations, factoring, observations, solution, implementation, and brute force.[^4]

## Entities & Concepts

- [[castle-polyomino](pages/castle-polyomino.md)] — the central object: a valid configuration of stacked blocks on a grid.
- [[castle-counting-function](pages/castle-counting-function.md)] — `F(w,h)`, the number of castles; the PE 502 even-block restriction is a special case.

- [[generating-functions](pages/generating-functions.md)] — the intended counting method (concept page seeded from the Problem Setup subpage; the dedicated *Generating Functions* source page is still queued).

Related topics linked from the source but not yet ingested (to be added in later ingests): Polyominoes, Dyck Words, Lattice Paths, Combinatorics.

## Relation to Other Wiki Pages

As the first source ingested, this page seeds the wiki. It defines the two foundational concepts ([[castle-polyomino](pages/castle-polyomino.md)] and [[castle-counting-function](pages/castle-counting-function.md)]) that every subsequent PE 502 subpage will elaborate. The seven subpages and five related-topic pages linked here are the planned ingestion queue; when ingested, each will backlink to this hub.

## Footnotes

[^1]: [[project-euler-502](pages/project-euler-502.md)] §"Project 502: Castle Polyominoes" L11-19 — "We define a block to be a rectangle with a height of 1 and an integer-valued length. Let a castle be a configuration of stacked blocks." plus the placement rules: blocks cannot stick out or overhang open space, are grid-snapped, neighboring same-row blocks have "at least one unit of space between them", the bottom row "is occupied by a block of length w", and "The maximum achieved height of the entire castle is exactly h."
[^2]: [[project-euler-502](pages/project-euler-502.md)] §"Project 502: Castle Polyominoes" L30 — "Find (F(10^12,100) + F(10000,10000) + F(100,10^12)) mod 1,000,000,007."
[^3]: [[project-euler-502](pages/project-euler-502.md)] §"Project 502: Castle Polyominoes" L20 — "The castle is made from an even number of blocks."
[^4]: [[project-euler-502](pages/project-euler-502.md)] §"Subpages" L34-40 [synthesis] — the seven subpage links and their one-line descriptions (Problem Setup, Representations, Castle Factoring, Observations, Solution, Implementation Notes, Brute Force).
[^5]: [[project-euler-502](pages/project-euler-502.md)] §"Related" L44-52 [synthesis] — the related-topic links: Polyominoes, Dyck Words, Lattice Paths, Combinatorics, Generating Functions.
[^6]: [[project-euler-502](pages/project-euler-502.md)] §header L5-7 — "Solved: March 31, 2026" and "First discussed: July 2017".
[^7]: [[project-euler-502](pages/project-euler-502.md)] §"Project 502: Castle Polyominoes" L28 — "F(4,2) = 10, F(13,10) = 3729050610636, F(10,13) = 37959702514, and F(100,100) mod 1,000,000,007 = 841913936".
