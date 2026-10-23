---
title: "Project Euler 502: Castle Polyominoes"
category: Sources
summary: The Project Euler 502 hub page. It states the problem, a castle as blocks stacked on a w × h grid under six rules, with the count the problem writes F(w, h), which the wiki writes A^e(w, h), four checkpoint values, and the target A^e(10^12, 100) + A^e(10000, 10000) + A^e(100, 10^12) mod 1 000 000 007; and it links the seven subpages of the solution.
tags: [project-euler, castle, polyomino, source, hub]
sources: [project-euler-502]
created: 2026-09-13
updated: 2026-10-23
---

# Project Euler 502: Castle Polyominoes

**Source:** https://charlesreid1.com/wiki/Project_Euler/502 (mirrors [Project Euler problem 502](https://projecteuler.net/problem=502))
**Date ingested:** 2026-09-13
**Type:** article (MediaWiki hub page)

## Summary

This hub page states Project Euler problem 502 and links the seven subpages of its solution.[^1][^2] The problem defines a block as a rectangle of height 1 and integer length, and a castle on a grid `w` units wide and `h` units tall as a configuration of stacked blocks under six rules.[^1] It writes `F(w, h)` for the number of castles, and its sixth rule makes these the castles with an even number of blocks, so `F(w, h)` is the count the wiki writes `A^e(w, h)` ([[castle-notation](pages/castle-notation.md)]). Its fifth rule says that the maximum height is "exactly `h`"; the wiki says that the castle has height `h`.

## Key Takeaways

- **The rules.** Blocks rest on other blocks with nothing sticking out past the edges or hanging over open space; blocks are aligned to the grid; two neighboring blocks in the same row have at least one unit of space between them; the bottom row is one block of length `w`; the castle has height `h`; and the castle has an even number of blocks.[^1] [[castle-polyomino](pages/castle-polyomino.md)] shows that the first five rules make a castle the same as a skyline `(c_1, …, c_w)` with `1 ≤ c_i ≤ h` and some `c_i = h`.
- **The sample castle.** The page draws a castle of width 8 and height 5,[^3] the skyline `(2, 3, 5, 2, 3, 1, 5, 4)` with 10 blocks ([[project-euler-502-representations](pages/project-euler-502-representations.md)]).
- **Checkpoints.** `A^e(4, 2) = 10`, `A^e(13, 10) = 3 729 050 610 636`, `A^e(10, 13) = 37 959 702 514`, and `A^e(100, 100) ≡ 841 913 936 (mod 1 000 000 007)`.[^4] [[castle-counting-formula](pages/castle-counting-formula.md)] reproduces all four.
- **The target.** The problem asks for[^4]

  ```
  ( A^e(10^12, 100) + A^e(10000, 10000) + A^e(100, 10^12) )  mod  1 000 000 007.
  ```

- **The subpages.** Problem Setup, Representations, Castle Factoring, Observations, Solution, Implementation Notes and Brute Force.[^2]
- **Dates.** The page records that the problem was first discussed in July 2017 and solved on March 31, 2026, and links the Java solution.[^5]

## Entities & Concepts

- [[castle-polyomino](pages/castle-polyomino.md)] - the castle as a skyline, the block count, and the six rules.
- [[castle-counting-function](pages/castle-counting-function.md)] - the counts `A`, `A^e` and `A^o`, the checkpoints, and the target.
- [[castle-counting-formula](pages/castle-counting-formula.md)] - the closed form of `A^e(w, h)` through the signed tower count.
- [[castle-count-algorithms](pages/castle-count-algorithms.md)] - the computation of the three terms of the target.

Also linked from the source: [[polyominoes](pages/polyominoes.md)], [[dyck-words](pages/dyck-words.md)], [[lattice-paths](pages/lattice-paths.md)], [[generating-functions-topic](pages/generating-functions-topic.md)].

## Relation to Other Wiki Pages

The seven subpages each have a source page: [[project-euler-502-problem-setup](pages/project-euler-502-problem-setup.md)], [[project-euler-502-representations](pages/project-euler-502-representations.md)], [[project-euler-502-castle-factoring](pages/project-euler-502-castle-factoring.md)], [[project-euler-502-observations](pages/project-euler-502-observations.md)], [[project-euler-502-solution](pages/project-euler-502-solution.md)], [[project-euler-502-implementation-notes](pages/project-euler-502-implementation-notes.md)] and [[project-euler-502-brute-force](pages/project-euler-502-brute-force.md)].

The castles of height 2 appear in the OEIS. Their even-block count is `A^e(w, 2) = A038505(w+1)`, their odd-block count `A^o(w, 2) = A038503(w+1) − 1`, and their total `2^w − 1 = A000225(w)`. Both `A038505` and `A038503` carry a comment on castles that names Project Euler Problem 502, and `A038505` links to the problem.[^6] Their difference `A038503 − A038505` is `A146559`, the real part of `(1+i)^n`, which gives the signed tower count `P(1, L) = A146559(L+1)` ([[oeis-height2-hyperbolic-castles](pages/oeis-height2-hyperbolic-castles.md)], [[hyperbolic-sequence-family](pages/hyperbolic-sequence-family.md)], [[signed-tower-count](pages/signed-tower-count.md)]).

## Footnotes

[^1]: [[project-euler-502](pages/project-euler-502.md)] §"Project 502: Castle Polyominoes" L11-20 - "We define a block to be a rectangle with a height of 1 and an integer-valued length. Let a castle be a configuration of stacked blocks.", "Given a game grid that is w units wide and h units tall, a castle is generated according to the following rules: Blocks can be placed on top of other blocks as long as nothing sticks out past the edges or hangs out over open space. All blocks are aligned/snapped to the grid. Any two neighboring blocks on the same row have at least one unit of space between them. The bottom row is occupied by a block of length w. The maximum achieved height of the entire castle is exactly h. The castle is made from an even number of blocks."
[^2]: [[project-euler-502](pages/project-euler-502.md)] §"Subpages" L34-40 [synthesis] - the links to the seven subpages, Problem Setup, Representations, Castle Factoring, Observations, Solution, Implementation Notes and Brute Force, each with a one-line description.
[^3]: [[project-euler-502](pages/project-euler-502.md)] §"Project 502: Castle Polyominoes" L22-24 - "The following is a sample castle for w = 8 and h = 5:" followed by the image `PE502.png`, the image that [[project-euler-502-representations](pages/project-euler-502-representations.md)] encodes as the tuple `2 3 5 2 3 1 5 4`.
[^4]: [[project-euler-502](pages/project-euler-502.md)] §"Project 502: Castle Polyominoes" L26-30 - "Let F(w,h) represent the number of valid castles, given grid parameters w and h. For example, F(4,2) = 10, F(13,10) = 3729050610636, F(10,13) = 37959702514, and F(100,100) mod 1,000,000,007 = 841913936", "Find (F(10^12,100) + F(10000,10000) + F(100,10^12)) mod 1,000,000,007."
[^5]: [[project-euler-502](pages/project-euler-502.md)] §header L3-7 - "Solution: https://git.charlesreid1.com/cs/euler/src/branch/main/java/Problem502.java", "Solved: March 31, 2026", "First discussed: July 2017".
[^6]: https://oeis.org/A038505 and https://oeis.org/A038503 (read 2026-10-16) - "a(n) is the number of castle polyominoes of width n-1 and height 2 with an even number of blocks (Project Euler, Problem 502: Counting Castles), for n >= 2" and the link "Project Euler, Problem 502: Counting Castles" on A038505; "a(n)-1 is the number of castle polyominoes of width n-1 and height 2 with an odd number of blocks (Project Euler, Problem 502: Counting Castles), for n >= 2" on A038503.
