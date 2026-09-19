---
title: Permutation-cycle / castle-peak analogy
category: Concepts
summary: The correspondence permutation cycles ↔ castle peaks/excursions — a genuine factorization (Dyck first-return with an extra letter), the spine of the castle-factoring reading. The elementary anchor is (n−1)!, upgraded step-by-step into the castle triad — see [[castles-as-upgraded-cycle-count]].
tags: [concept, castle, permutations, cycles, factorization, dyck]
sources: [project-euler-502-castle-factoring, pe502-castle-cycle-permutations]
created: 2026-09-13
updated: 2026-09-19
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

## The (n−1)! anchor

The three constructions have a joint elementary anchor: the classical `(n−1)!` count of labelled cycles on `n` items, whose two proofs — **quotient by the free `Z/n` rotation action** (`n!/n = (n−1)!`) and **fix the cycle to start at element `1`** (the remaining `n−1` order freely) — are instances of a **bigger machine** (Foata, sign, cycle-follow) that reappears intact on the castle side.[^5] Each move of the classical proof has a direct castle counterpart:

| (n−1)! proof move | Castle counterpart |
|---|---|
| divide by `n` / `(1 ± sgn)/2` to peel `A_n` from `S_n` | [[castle-sign](pages/castle-sign.md)] `s(C) = (−1)^{blocks}`, `(T ± P)/2` even/odd projector |
| canonical form starting from element `1` (or Foata's largest-first flattening) | [[castle-foata-transform](pages/castle-foata-transform.md)] — peaks are maximal positive runs, records are their leftmost positive columns |
| cycle-follow `i ↦ σ(i)` (an `O(n)` loop) | [[monotone-streak-factorization](pages/monotone-streak-factorization.md)] — first-difference scan into up/flat/down streaks (an `O(L)` loop) |

The `(n−1)!` proof is the degenerate case: one cycle, no factoring, trivial sign. The castle machinery is the same three moves at industrial scale — stacked, width-weighted, sign-selected cycles.[^6] The seminar-ready form of this synthesis is [[castles-as-upgraded-cycle-count](pages/castles-as-upgraded-cycle-count.md)].

## Appearances in Sources

- [[project-euler-502-castle-factoring](pages/project-euler-502-castle-factoring.md)] — states the analogy, the correspondence table, and Knuth's canonical cycle form as the source-side template.
- [[pe502-castle-cycle-permutations](pages/pe502-castle-cycle-permutations.md)] — supplies the (n−1)! elementary anchor and the closing "proof-move ↔ castle counterpart" table.

## Related Concepts

- [[generalized-dyck-grammar](pages/generalized-dyck-grammar.md)] — the factorization on the castle side.
- [[castle-sign](pages/castle-sign.md)] — the sign atom in the correspondence.
- [[castle-foata-transform](pages/castle-foata-transform.md)] — the cycles-to-records half of the analogy.
- [[monotone-streak-factorization](pages/monotone-streak-factorization.md)] — the cycle-following loop's castle analogue.
- [[castles-as-upgraded-cycle-count](pages/castles-as-upgraded-cycle-count.md)] — the seminar-shaped synthesis reading PE 502 as the (n−1)! toolkit upgraded three times.
- [[permutation-inversions](pages/permutation-inversions.md)] — the other classical permutation statistic (inversions), whose q-factorial generating function underlies the q-analog thread.
- [[aocp-multisets](pages/aocp-multisets.md)] — Knuth's two-line arrays and unique cycle factorization (the Vol. 3 source of this analogy's permutation side).
- [[aocp-combinatorics](pages/aocp-combinatorics.md)] — Knuth's Vol. 3 inversions and the q-factorial `∏(1−z^k)/(1−z)^n`, the source behind the inversion statistic mentioned above.

## Footnotes

[^1]: [[project-euler-502-castle-factoring](pages/project-euler-502-castle-factoring.md)] §"Knuth canonical cycle form" L27 — "The factorization is the loop i ↦ σ(i): start at an unvisited element and follow the map until it closes. The cycles are disjoint because the map is a bijection."
[^2]: [[project-euler-502-castle-factoring](pages/project-euler-502-castle-factoring.md)] §"Castle Factoring and the Knuth-Castle Foata Transform" L7 — "each U V D peak leaves the base, lives entirely above a sub-block, and returns to the same level, and disjoint peaks are separated by R gaps. This is a genuine factorization, not a metaphor: it is the Dyck first-return decomposition with one extra letter (R)."
[^3]: [[project-euler-502-castle-factoring](pages/project-euler-502-castle-factoring.md)] §"The tower grammar" L68 — "The excursion count (peaks) plays the role of the cycle count, while the block count plays the role of the sign atom. One peak may contain several stacked blocks, so these are distinct."
[^4]: [[project-euler-502-castle-factoring](pages/project-euler-502-castle-factoring.md)] §"Knuth canonical cycle form" L19-25 — "writing every singleton cycle explicitly; putting the smallest element first within each cycle; ordering the cycles in decreasing order of their first element ... Erasing the parentheses recovers a one-line permutation."
[^5]: [[pe502-castle-cycle-permutations](pages/pe502-castle-cycle-permutations.md)] §"Warm-up: labelled cycles" L5-L10 — "The number of such directed cycles is (n-1)!, with two standard proofs: 1. Quotient by rotation. n! linear orderings collapse under the free Z/n rotation action, so n!/n = (n-1)! cycles. 2. Fix a starting point ... Both proofs are instances of a bigger machine (Foata, sign, cycle-follow) that reappears in PE 502."
[^6]: [[pe502-castle-cycle-permutations](pages/pe502-castle-cycle-permutations.md)] §"Tying back to (n-1)!" L80-L86 — the three-row proof-move-to-castle-counterpart table and "PE 502 is essentially: take the toolkit that proves (n-1)!, upgrade every step to a version that handles stacked, width-weighted, sign-selected cycles, and you get a closed form plus a fast recurrence."
