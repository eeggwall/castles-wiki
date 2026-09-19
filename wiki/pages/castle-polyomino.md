---
title: Castle (polyomino)
category: Concepts
summary: The central object of study. A castle is a skyline (c_1, …, c_w) with 1 ≤ c_i ≤ h and max c_i = h; blocks are the maximal runs of each row so the block count is the total descent; the any-parity count is A(w, h) = h^w − (h−1)^w.
tags: [concept, castle, polyomino, bargraph, column-convex, skyline, combinatorics]
sources: [project-euler-502, project-euler-502-problem-setup, project-euler-502-representations, project-euler-502-castle-factoring, project-euler-502-solution, project-euler-502-brute-force]
created: 2026-09-13
updated: 2026-09-19
---

# Castle (polyomino)

## Definition

A **castle** on a `w × h` grid is a **skyline** - a tuple of column heights[^1]

```
c = (c_1, c_2, …, c_w),   with  1 ≤ c_i ≤ h  for every i,   and  max_i c_i = h.
```

The `i`-th column of the castle is the vertical stack of unit cells at heights `1, 2, …, c_i`; the whole castle is the union of these `w` columns. Every castle is therefore automatically:

- **column-convex** - each column is one contiguous vertical run from the base to height `c_i`;
- **bottom-aligned** - row 1 is a full-width strip `c_i ≥ 1`;
- **exactly `h` tall** - at least one column reaches the ceiling.

In the polyomino literature the object *"column-convex polyomino with a full contiguous bottom row"* is called a **bargraph** (or a **skyline polyomino**), so a castle is a bargraph of width `w`, height at most `h`, that touches the ceiling `h` in at least one column. That places castles inside a well-studied family, next to Ferrers, staircase, stack, and parallelogram polyominoes ([[polyominoes](pages/polyominoes.md)], [[column-convex-polyomino](pages/column-convex-polyomino.md)]).

The name "castle polyomino" reflects the visual intuition: a valid configuration resembles the crenellated silhouette of a castle wall.

## Blocks and the any-parity count

Reading a castle row by row, the **blocks** are the maximal horizontal runs of filled cells:[^2] on row `r` the block set is the maximal intervals `[i, j]` on which `c_i, c_{i+1}, …, c_j ≥ r`, one row-`r` block per interval. Adding one unit to each side of the skyline (`c_0 = c_{w+1} = 0`) makes the total block count a plain sum over column-to-column drops:

```
#blocks(c) = ∑_{i=0}^{w} max(0, c_i − c_{i+1})  =  ∑_{i=0}^{w} max(0, c_{i+1} − c_i).
```

The first sum is the **total descent** of the skyline; the second is the **total ascent**. They are equal because the skyline starts and returns to 0. Both forms are used across the wiki: the descent form drives [[castle-sign](pages/castle-sign.md)] and the closed forms; the ascent form drives the `p_signed` dynamic program in [[project-euler-502-brute-force](pages/project-euler-502-brute-force.md)].

The **any-parity count** is the number of castles of width `w` and exact height `h` regardless of block parity, and it drops out of the skyline definition by inclusion-exclusion:[^3]

```
A(w, h)  =  # castles of width w, height exactly h  =  h^w − (h−1)^w.
```

`h^w` counts skylines with `1 ≤ c_i ≤ h`; subtracting `(h−1)^w` (the skylines confined below the ceiling) leaves exactly the skylines that touch the ceiling. Project Euler 502 (PE 502) restricts this count to castles with an **even** number of blocks;[^4] its count is `F(w, h) = A(w, h) − F_odd(w, h)`, computed in closed form on [[castle-counting-formula](pages/castle-counting-formula.md)]. The parity restriction is what makes PE 502 hard; the general castle object, at any block count, is what most of this wiki works on.

## Placement rules (five equivalent forms)

The definition above already forces every castle rule Project Euler 502 states. The five rules from the source, translated into the skyline model:[^5]

- **Rule 1 - no overhangs, no floating blocks.** A block rests on a horizontal support: either the base row, or the top of another block, or two other blocks sitting at the same level with no gap between them (so their tops form a continuous surface). The skyline model builds this in from the start - each column is a contiguous stack of unit cells rising from row 1 - so there is nothing to overhang and nothing to float.
- **Rule 2 - grid-snapped.** Every cell is aligned to the integer grid; automatic in the skyline model.
- **Rule 3 - same-row spacing.** Any two neighboring row-`r` blocks are separated by at least one column of empty space. Automatic: two adjacent columns `c_i, c_{i+1} ≥ r` are one block on row `r`, not two, because the blocks are defined as maximal runs. This is the point [[generalized-dyck-grammar](pages/generalized-dyck-grammar.md)] records as "no-overhang needs no separate rule".
- **Rule 4 - full base.** Row 1 is a single block of length `w`. Encoded by `c_i ≥ 1` for every `i`.
- **Rule 5 - exact height.** The castle reaches height exactly `h`. Encoded by `max_i c_i = h`.

The equivalence between the source's block-level rules and the skyline conditions above is the content of [[castle-representations](pages/castle-representations.md)]; the U/R/D step-string form, which reads validity off a two-letter forbidden-substring rule, is the deepest of the three encodings and lives on [[urd-step-strings](pages/urd-step-strings.md)].

## Relationship to Project Euler 502

Project Euler 502 counts a *restricted* family of castles: those made from an **even** number of blocks.[^4] The parity constraint is a filter on top of the general castle object, and this wiki treats it that way - `A(w, h)` is the ambient count and `F(w, h)` its even-block restriction, following the notation of [[project-euler-502-solution](pages/project-euler-502-solution.md)]. The parity constraint is precisely what gives PE 502 its particular character; the general castle, at any block count, is the object most threads on this wiki follow.

## Encodings

A castle can be encoded exactly in several ways - column-wise binary strings, the skyline tuple itself, or U/R/D step strings - each turning the placement rules into constraints on the encoding (see [[castle-representations](pages/castle-representations.md)]). In the U/R/D reading, a castle is `U (tower) D`; every `D` step completes one block, and validity is characterized by the absence of `UD` (a zero-width block) and `DU` (two touching blocks) in the tower word.

## Appearances in Sources

- [[project-euler-502](pages/project-euler-502.md)] - defines the block, the castle, and the five placement rules; adds the even-block parity restriction for the PE 502 count.
- [[project-euler-502-problem-setup](pages/project-euler-502-problem-setup.md)] - partially restates the rules (as Rule 1, 3, 4, 5, 6; not repeating Rule 2 is an incomplete restatement, not a change to the problem - no rule is dropped).
- [[project-euler-502-representations](pages/project-euler-502-representations.md)] - encodes the castle and characterizes validity in the U/R/D word (each D completes a block; no UD, no DU).
- [[project-euler-502-castle-factoring](pages/project-euler-502-castle-factoring.md)] - factors a castle via its column heights, reading peaks as cycle-like atoms (the permutation-cycle analogy).
- [[project-euler-502-solution](pages/project-euler-502-solution.md)] - the `A(w, h)` / `F(w, h)` notation and the induction proof `T(k, L) = (k + 1)^L`.
- [[project-euler-502-brute-force](pages/project-euler-502-brute-force.md)] - the ascent-side block-count formula and the `p_signed` dynamic program.

## Related Concepts

- [[castle-representations](pages/castle-representations.md)] - the three encodings of a castle (binary strings, skyline tuples, U/R/D step strings).
- [[castle-counting-function](pages/castle-counting-function.md)] - `F(w, h)`, the even-block count; `A(w, h) = h^w − (h−1)^w` is the ambient any-parity count above.
- [[castle-counting-formula](pages/castle-counting-formula.md)] - the closed form `F(w, h) = (A − P)/2` in terms of the signed tower count.
- [[castle-sign](pages/castle-sign.md)] - `(−1)^{#blocks}` as a homomorphism, block count as the total descent of the skyline.
- [[castle-classification](pages/castle-classification.md)] - the framework organizing castle sub-families by skyline predicate; catalogs 42 types across 9 axes (7 structural, plus a growth-type meta-classification and a spectral one).
- [[castle-strip](pages/castle-strip.md)] - a castle read left to right, one column at a time, under a neighbor rule; the transfer-matrix bridge.
- [[convex-castle](pages/convex-castle.md)] - the unimodal sub-family (skyline rises then falls); the polyomino literature's "stack" family.
- [[column-convex-polyomino](pages/column-convex-polyomino.md)] / [[polyominoes](pages/polyominoes.md)] - the ambient family; a castle is a bargraph (column-convex polyomino with a full contiguous bottom row).
- [[generalized-dyck-grammar](pages/generalized-dyck-grammar.md)] - the tower-word grammar the counts are read off of.
- [[permutation-cycle-castle-analogy](pages/permutation-cycle-castle-analogy.md)] - the cycle-factorization reading.
- [[generating-functions](pages/generating-functions.md)] - the intended method for counting castle configurations at large parameters.

## Footnotes

[^1]: [[project-euler-502](pages/project-euler-502.md)] §"Project 502: Castle Polyominoes" L11-19 [synthesis] - the skyline form `c = (c_1, …, c_w)` with `1 ≤ c_i ≤ h` and `max_i c_i = h` is the column-height reading of the source's five block-level rules, worked out on [[castle-representations](pages/castle-representations.md)] and [[project-euler-502-brute-force](pages/project-euler-502-brute-force.md)] `§"Column-height encoding"` L18-27 ("column heights `c_1, …, c_w ∈ {1, …, h}` with `max c = h`").
[^2]: [[project-euler-502-brute-force](pages/project-euler-502-brute-force.md)] §"Column-height encoding" L18-27 - "`#blocks = c_1 + ∑_{i=2}^w max(0, c_i − c_{i−1})`" (ascent form); the equivalent descent form `∑_{i=0}^{w} max(0, c_i − c_{i+1})` with `c_0 = c_{w+1} = 0` is used on [[castle-sign](pages/castle-sign.md)]. Both re-verified against direct row-scan enumeration during ingest for `w, h ≤ 6`.
[^3]: [[project-euler-502-observations](pages/project-euler-502-observations.md)] §"The 'even number of blocks' clause is almost the entire difficulty" L17 - "Without it, the answer is just `h^w − (h−1)^w`: all castles of height at most `h` minus those of height at most `h − 1`."
[^4]: [[project-euler-502](pages/project-euler-502.md)] §"Project 502: Castle Polyominoes" L20 - "The castle is made from an even number of blocks."
[^5]: [[project-euler-502](pages/project-euler-502.md)] §"Project 502: Castle Polyominoes" L13-19 [synthesis] - the placement rules: no sticking out or overhanging open space, grid-snapped, ≥1 unit gap between same-row neighbors, bottom row a block of length `w`, maximum height exactly `h`.
