---
title: "PE 502: Problem Setup"
category: Sources
summary: The pre-solution framing subpage — restates the castle rules, points at a generating-function approach, and records the 2017–2026 timeline.
tags: [project-euler, castle, generating-functions, source, subpage]
sources: [project-euler-502-problem-setup]
created: 2026-09-13
updated: 2026-09-19
---

# Project Euler 502 (PE 502): Problem Setup

**Source:** https://charlesreid1.com/wiki/Project_Euler/502/Problem_Setup
**Date ingested:** 2026-09-13
**Type:** article (MediaWiki subpage of [[project-euler-502](pages/project-euler-502.md)])

## Summary

This is the "Problem Setup" subpage for Project Euler 502 — an early, pre-solution framing of the castle-counting problem. It was written before the problem was solved, so it captures the initial orientation toward the problem rather than the eventual method.

Its main content is threefold. First, it argues for scale: the counting function [[castle-counting-function](pages/castle-counting-function.md)] already reaches `F(13,10) = 3,729,050,610,636` on a modest 13×10 grid, and the target grids run to height 10^12, far beyond anything that can be enumerated or stored directly.[^1] Second, it proposes attacking the count with a **[[generating-functions](pages/generating-functions.md)]** approach — building a multivariate polynomial in the problem's dimensions whose coefficients are the answers, reducing "solve the problem" to "evaluate a particular term."[^2] Third, it restates the Project Euler 502 castle rules.[^3]

The rule restatement on this page is **partial**: it lists Rule 1, 3, 4, 5, and 6 and does not repeat Rule 2 (grid-snapped alignment). This is an incomplete restatement, not a change to the problem — the castle is the same object with the same full rule set defined on [[castle-polyomino](pages/castle-polyomino.md)]; no rule is being dropped. The page also records a timeline: a first direct-enumeration attempt in July 2017, repeated returns and a polyomino-literature dive through 2017–2025, and the solution in March 2026.[^4]

## Key Takeaways

- The counting function is astronomically large even at small grid sizes — `F(13,10) = 3,729,050,610,636` — and the PE 502 target grids reach height 10^12, ruling out direct enumeration or storage of castles.[^1]
- The proposed line of attack is a generating function: a multivariate polynomial whose variables are the problem's dimensions and whose coefficients encode the counts, so that solving becomes extracting a particular term.[^2] See [[generating-functions](pages/generating-functions.md)].
- The castle rules are restated here as Rules 1, 3, 4, 5, 6; Rule 2 (grid-snapped) is simply not repeated on this page. The full canonical rule set lives on [[castle-polyomino](pages/castle-polyomino.md)] — no rule is dropped from the problem.[^3]
- Timeline: first attempt July 2017 (direct enumeration); repeated returns and polyomino-literature study 2017–2025; solved March 2026.[^4]

## Entities & Concepts

- [[castle-polyomino](pages/castle-polyomino.md)] — the object being counted; this page restates (partially) its rules.
- [[castle-counting-function](pages/castle-counting-function.md)] — `F(w,h)`, whose sheer scale motivates the setup.
- [[generating-functions](pages/generating-functions.md)] — the counting approach this page points toward.
- [[generating-function-gallery](pages/generating-function-gallery.md)] / [[castle-counting-formula](pages/castle-counting-formula.md)] — the form the generating-function approach finally took.
- [[kitamasa](pages/kitamasa.md)] / [[castle-count-algorithms](pages/castle-count-algorithms.md)] — how the trillion-height targets are actually reached.
- [[castle-entropy](pages/castle-entropy.md)] — the scale argument restated in bits.
- [[project-euler-502-brute-force](pages/project-euler-502-brute-force.md)] / [[aocp-generating-permutations-tuples](pages/aocp-generating-permutations-tuples.md)] — what the 2017 direct-enumeration attempt became.

Also linked from the source, both now ingested: [[project-euler-502-representations](pages/project-euler-502-representations.md)] and [[project-euler-502-solution](pages/project-euler-502-solution.md)].

## Relation to Other Wiki Pages

This subpage sits under the hub [[project-euler-502](pages/project-euler-502.md)] and elaborates the "setup" phase. It is the first source to introduce [[generating-functions](pages/generating-functions.md)] as the intended method. Because it predates the solution, its content is framing rather than result — the actual method and any solution-borne principles belong to [[project-euler-502-solution](pages/project-euler-502-solution.md)] and [[project-euler-502-observations](pages/project-euler-502-observations.md)].

## How the setup resolved

Read against the finished wiki, each of the three framing points has a landing place.

- **The generating-function bet paid off, in a particular shape.** Not one bivariate polynomial in `(w, h)` but a family of rational generating functions `F_k(x) = num_k/den_k` in the width direction, one per tower height `k` ([[generating-function-gallery](pages/generating-function-gallery.md)]), whose coefficients are the signed tower counts `P(k, L)` that the [[castle-counting-formula](pages/castle-counting-formula.md)] assembles into `F(w,h)`. The "evaluate a particular term" step is literal: the `10^12` targets are single far-off coefficients pulled by [[kitamasa](pages/kitamasa.md)], and the routing by regime is on [[castle-count-algorithms](pages/castle-count-algorithms.md)].
- **The scale argument, in bits.** `log₂ F(13,10) ≈ 41.8`, against the entropy estimate `w·log₂ h − 1 ≈ 42.2` of [[castle-entropy](pages/castle-entropy.md)] - each column is worth `log₂ h` bits and the even-block clause exactly one. The `10!` brute-force ceiling that [[aocp-permutations](pages/aocp-permutations.md)] records (`3.6 × 10^6`) is six orders of magnitude below `F(13,10)`; the wiki's own largest exhaustive census, the 4.87 million castles of [[castle-graph-spectral-radius](pages/castle-graph-spectral-radius.md)], sits right at that ceiling.
- **The 2017 direct-enumeration attempt matured into a tool.** The reference enumerator on [[project-euler-502-brute-force](pages/project-euler-502-brute-force.md)] is Knuth's mixed-radix Algorithm M over `{1..h}^w` ([[aocp-generating-permutations-tuples](pages/aocp-generating-permutations-tuples.md)]); it never reaches the targets, but it is the backstop every formula on the wiki is checked against.

## Footnotes

[^1]: [[project-euler-502-problem-setup](pages/project-euler-502-problem-setup.md)] §"Don't Count: Generate" L5-7 — "the number of configurations for a castle ... 13x10 grid ... F(13,10) = 3,729,050,610,636. You can't ask a computer to COUNT that high, let alone store that many castles" and "the question at hand is to enumerate castles with a height of a TRILLION".
[^2]: [[project-euler-502-problem-setup](pages/project-euler-502-problem-setup.md)] §"Generating functions" L17-20 — "come up with a multivariate polynomial whose variables are dimensions of the problem (width and height ...) and whose coefficients are the solutions to our problem. This turns the problem of finding a solution ... into evaluating a particular term of the generating function".
[^3]: [[project-euler-502-problem-setup](pages/project-euler-502-problem-setup.md)] §"Castle Rules" L26-31 [synthesis] — the rules restated as Rule 1, 3, 4, 5, 6 (no Rule 2 repeated); an incomplete restatement of the full rule set, not a modification of the problem.
[^4]: [[project-euler-502-problem-setup](pages/project-euler-502-problem-setup.md)] §"Timeline" L36-38 — "2017-07: first attempt, direct enumeration. 2017-2025: repeated returns; polyomino literature dive ... 2026-03: solution."
