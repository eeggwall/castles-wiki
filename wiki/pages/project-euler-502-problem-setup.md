---
title: "PE 502: Problem Setup"
category: Sources
summary: The Problem Setup subpage of Project Euler 502. It argues from the size of A^e(13, 10) = 3 729 050 610 636 and of the targets of width or height 10^12 that castles must be counted with a generating function, not enumerated; restates the problem's rules 1, 3, 4, 5 and 6; and records a timeline from a first attempt in July 2017 to the solution in March 2026.
tags: [project-euler, castle, generating-functions, source, subpage]
sources: [project-euler-502-problem-setup]
created: 2026-09-13
updated: 2026-10-16
---

# Project Euler 502 (PE 502): Problem Setup

**Source:** https://charlesreid1.com/wiki/Project_Euler/502/Problem_Setup
**Date ingested:** 2026-09-13
**Type:** article (MediaWiki subpage of [[project-euler-502](pages/project-euler-502.md)])

## Summary

The hub page of Project Euler 502 describes this subpage as "the original framing: why counting is impossible, the generating-function intuition, and the castle rules".[^1] The subpage writes `F(w, h)` for the even-block count, which the wiki writes `A^e(w, h)` ([[castle-counting-function](pages/castle-counting-function.md)]), and "maximum achieved height ... exactly `h`" for a castle of height `h`.

## Key Takeaways

- **Scale.** The problem statement gives `A^e(13, 10) = 3 729 050 610 636` for a grid only 13 wide and 10 tall, and the targets have height `10^12` (the term `A^e(100, 10^12)`) or width `10^12`. The source concludes that castles cannot be listed or stored and must be counted instead.[^2]
- **Generating functions.** The source proposes a multivariate generating function whose variables are the dimensions of the problem and whose coefficients are the counts, so that the answer is a particular coefficient, computed by a recursion ([[generating-functions](pages/generating-functions.md)]).[^3]
- **Rules.** The source repeats the problem's rules 1, 3, 4, 5 and 6: no overhangs, at least one unit of space between neighboring blocks in a row, a full bottom row of length `w`, height `h`, and an even number of blocks. Rule 2, alignment to the grid, is not repeated. All six rules are on [[castle-polyomino](pages/castle-polyomino.md)].[^4]
- **Timeline.** A first attempt by direct enumeration in July 2017, repeated returns and reading of the polyomino literature from 2017 to 2025, and the solution in March 2026.[^5]

## Entities & Concepts

- [[castle-polyomino](pages/castle-polyomino.md)] - the castle definition and the six rules.
- [[castle-counting-function](pages/castle-counting-function.md)] - the counts `A`, `A^e`, `A^o`, the checkpoints and the target.
- [[generating-functions](pages/generating-functions.md)] - the method the source proposes.
- [[castle-counting-formula](pages/castle-counting-formula.md)] - the closed form of `A^e(w, h)` through the rational generating functions `P_k(x) = num_k(x)/den_k(x)` of the signed tower counts, one for each tower height `k`.
- [[castle-count-algorithms](pages/castle-count-algorithms.md)] - the computation of the three target terms: Kitamasa's method for the coefficient at width `10^12`, and a recurrence in the tower height for height `10^12`.
- [[castle-entropy](pages/castle-entropy.md)] - the size of the counts in bits: `log₂ A^e(13, 10) = 41.762`, against `log₂ A(13, 10) − 1 = 41.762` and `13 log₂ 10 − 1 = 42.185`, the last without the correction for height.
- [[project-euler-502-brute-force](pages/project-euler-502-brute-force.md)] - the reference enumerator, which runs over `{1, …, h}^w` for small `w` and `h`.
- [[aocp-generating-permutations-tuples](pages/aocp-generating-permutations-tuples.md)] - Knuth's Algorithm M, which generates the tuples of `{1, …, h}^w` one at a time.

Also linked from the source: [[project-euler-502-representations](pages/project-euler-502-representations.md)], [[project-euler-502-solution](pages/project-euler-502-solution.md)].

## Footnotes

[^1]: [[project-euler-502](pages/project-euler-502.md)] §"Subpages" L34 [synthesis] - the subpage list entry for Problem Setup: "the original framing: why counting is impossible, the generating-function intuition, and the castle rules"
[^2]: [[project-euler-502-problem-setup](pages/project-euler-502-problem-setup.md)] §"Don't Count: Generate" L5-9 - "just a measely 13x10 grid - is given in the original problem as F(13,10) = 3,729,050,610,636. You can't ask a computer to COUNT that high, let alone store that many castles", "the question at hand is to enumerate castles with a height of a TRILLION", "Instead of enumerating castles, you should count castles with a generating function."
[^3]: [[project-euler-502-problem-setup](pages/project-euler-502-problem-setup.md)] §"Generating functions" L15-16 - "come up with a multivariate polynomial whose variables are dimensions of the problem (width and height, or some other variables if they are more convenient) and whose coefficients are the solutions to our problem. This turns the problem of finding a solution for a particular problem into evaluating a particular term of the generating function (where each term is implemented using a recursive function or a similar method)."
[^4]: [[project-euler-502-problem-setup](pages/project-euler-502-problem-setup.md)] §"Castle Rules" L22-27 [synthesis] - the rules listed as Rule 1, 3, 4, 5 and 6, with Rule 2 omitted.
[^5]: [[project-euler-502-problem-setup](pages/project-euler-502-problem-setup.md)] §"Timeline" L31-33 - "2017-07: first attempt, direct enumeration.", "2017-2025: repeated returns; polyomino literature dive (see references)", "2026-03: solution."
