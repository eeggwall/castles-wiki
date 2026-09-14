---
title: Permutation-cycle / castle-peak analogy
category: Concepts
summary: The correspondence permutation cycles ↔ castle peaks/excursions — a genuine factorization (Dyck first-return with an extra letter), the spine of the castle-factoring reading.
tags: [concept, castle, permutations, cycles, factorization, dyck]
sources: [project-euler-502-castle-factoring]
created: 2026-09-13
updated: 2026-09-13
---

# Permutation-cycle / castle-peak analogy

## Description

The central organizing idea of the castle-factoring reading is a single analogy:

> **permutation cycles : castle peaks/excursions**

Knuth factors a permutation into disjoint cycles by following the map `i ↦ σ(i)` from an unvisited element until the loop closes; the cycles are disjoint because the map is a bijection.[^1] The [[generalized-dyck-grammar](pages/generalized-dyck-grammar.md)] factors a castle's tower word the same way: each `U V D` **peak** leaves the base, lives entirely above one sub-block, and returns to the base, and disjoint peaks are separated by `R` gaps — exactly as disjoint cycles are separated by parentheses.[^2] This is presented as a genuine factorization, not a metaphor: it is the Dyck first-return decomposition with one extra letter (`R`).[^2]

## The correspondence

| Permutation | Castle tower |
|---|---|
| element *i*, map `i ↦ σ(i)` | column; skyline step `U`, `R`, or `D` |
| disjoint cycle | disjoint peak `U V D` (an excursion above one sub-block) |
| parenthesized cycle form | peaks separated by `R` gaps |
| number of cycles | number of peaks |
| sign `(−1)^{n−c}` | sign `(−1)^{blocks}` (see [[castle-sign](pages/castle-sign.md)]) |

Two statistics come out of this, and they are **distinct**: the excursion count (peaks) plays the role of the cycle count, while the *block* count plays the role of the sign atom. One peak may contain several stacked blocks, so peaks and blocks are not the same statistic.[^3]

The analogy's source side is Knuth's **canonical cycle form** (TAOCP Vol. 1, §1.3.3): write every singleton cycle explicitly, put the smallest element first within each cycle, and order cycles by decreasing first element; erasing parentheses recovers a one-line permutation.[^4] From this analogy the castle-factoring page derives three constructions — the [[castle-sign](pages/castle-sign.md)], the [[castle-foata-transform](pages/castle-foata-transform.md)], and the [[monotone-streak-factorization](pages/monotone-streak-factorization.md)] — each a castle analogue of a classical permutation notion.

## Appearances in Sources

- [[project-euler-502-castle-factoring](pages/project-euler-502-castle-factoring.md)] — states the analogy, the correspondence table, and Knuth's canonical cycle form as the source-side template.

## Related Concepts

- [[generalized-dyck-grammar](pages/generalized-dyck-grammar.md)] — the factorization on the castle side.
- [[castle-sign](pages/castle-sign.md)] — the sign atom in the correspondence.
- [[castle-foata-transform](pages/castle-foata-transform.md)] — the cycles-to-records half of the analogy.
- [[monotone-streak-factorization](pages/monotone-streak-factorization.md)] — the cycle-following loop's castle analogue.

## Footnotes

[^1]: [[project-euler-502-castle-factoring](pages/project-euler-502-castle-factoring.md)] §"Knuth canonical cycle form" L27 — "The factorization is the loop i ↦ σ(i): start at an unvisited element and follow the map until it closes. The cycles are disjoint because the map is a bijection."
[^2]: [[project-euler-502-castle-factoring](pages/project-euler-502-castle-factoring.md)] §"Castle Factoring and the Knuth-Castle Foata Transform" L7 — "each U V D peak leaves the base, lives entirely above a sub-block, and returns to the same level, and disjoint peaks are separated by R gaps. This is a genuine factorization, not a metaphor: it is the Dyck first-return decomposition with one extra letter (R)."
[^3]: [[project-euler-502-castle-factoring](pages/project-euler-502-castle-factoring.md)] §"The tower grammar" L68 — "The excursion count (peaks) plays the role of the cycle count, while the block count plays the role of the sign atom. One peak may contain several stacked blocks, so these are distinct."
[^4]: [[project-euler-502-castle-factoring](pages/project-euler-502-castle-factoring.md)] §"Knuth canonical cycle form" L19-25 — "writing every singleton cycle explicitly; putting the smallest element first within each cycle; ordering the cycles in decreasing order of their first element ... Erasing the parentheses recovers a one-line permutation."
