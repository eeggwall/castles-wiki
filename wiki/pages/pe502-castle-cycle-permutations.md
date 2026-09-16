---
title: "PE 502 castles as an upgrade of the (n−1)! cycle-count proof"
category: Sources
summary: A working note framing PE 502 as the elementary (n−1)! cycle-count toolkit — quotient-by-rotation, canonical form, cycle-following — upgraded step-by-step into the castle's sign / Foata / streak-factorization triad. The synthesis behind [[castles-as-upgraded-cycle-count]].
tags: [note, castle, permutations, cycles, seminar, source]
sources: [pe502-castle-cycle-permutations]
created: 2026-09-15
updated: 2026-09-15
---

# PE 502 castles as an upgrade of the (n−1)! cycle-count proof

**Source:** `raw/pe502-castle-cycle-permutations.md` (working note authored 2026-09-15 in preparation for a seminar spine)
**Date ingested:** 2026-09-15
**Type:** note (markdown, line-numbered; ~86 lines)

## Summary

The note builds a **direct upgrade path** from the two elementary proofs of "there are `(n−1)!` labelled cycles on `n` items" to the full castle-counting toolkit of PE 502. The two elementary proofs are (i) quotient the `n!` linear orderings by the free `Z/n` rotation action, and (ii) fix the cycle to start at element `1` and let the remaining `n−1` order freely — both proofs, the note observes, are instances of a bigger machine (**Foata, sign, cycle-follow**) that reappears intact on the castle side.[^1]

The heart of the note is a three-row **correspondence table** between the moves of the `(n−1)!` proof and the moves of the castle machinery:[^2]

- **Divide by `n` (quotient by rotation), or `(1 ± sgn)/2` to peel `A_n` from `S_n`** ↔ [[castle-sign](pages/castle-sign.md)] `s(C) = (−1)^{blocks}` with the `(T ± P)/2` even/odd projector.
- **Canonical form starting from element `1`** (Foata: start each cycle with its largest, order cycles increasingly, drop parentheses) ↔ [[castle-foata-transform](pages/castle-foata-transform.md)]: flatten to column heights, peaks are maximal positive runs, records are the leftmost positive columns.
- **Cycle-follow `i ↦ σ(i)` (an `O(n)` loop)** ↔ [[monotone-streak-factorization](pages/monotone-streak-factorization.md)]: first-difference scan into up/flat/down streaks (`O(L)`, block count = sum of down-streak magnitudes).

A concrete hand-check runs the machinery on `F(4,2) = 10`: the [[castle-counting-formula](pages/castle-counting-formula.md)] gives `F(4,2) = (16 − 1 + 4 + 1)/2 = 10` (with `P(1,4) = −4`, `P(0,4) = 1`, both re-verified during ingest by direct enumeration over the 16 length-4 binary column-height strings), and the same 10 castles are the 10 length-4 binary strings with exactly one maximal positive run — the [[castle-foata-transform](pages/castle-foata-transform.md)] miniature applied across the entire case.[^3]

The note closes with the caveat that gives the castle its shape: **block count ≠ peak count**.[^4] A single peak can be several stacked blocks, so the `(−1)^{blocks}` sign atom and the peak-count-as-cycle-count analogue are different statistics on the same castle. The Foata bijection is with peaks; the sign is measured on blocks. This is the fingerprint of a genuinely richer combinatorial object — the castle sits between *cycles of a permutation* and *cycles with multiplicity and height*.[^5]

## Key Takeaways

- **The `(n−1)!` proof is the degenerate case** — one cycle, no factoring, sign trivial — of the same three-move machine that proves the [[castle-counting-formula](pages/castle-counting-formula.md)].[^2]
- **`F(4,2) = 10` hand-check** runs the closed form and the Foata bijection in miniature on the same 10 configurations.[^3]
- **Block count ≠ peak count** — the castle carries multiplicity where a permutation does not; the analogy is at the level of factoring, not cardinality (`3! = 6 ≠ 10`).[^4][^5]
- **Seminar-shaped** — the note is written as an outward-facing narrative arc, hooking on the elementary `(n−1)!` warm-up and landing on the [[castle-counting-formula](pages/castle-counting-formula.md)] via three telegraphed upgrades. This is the shape the wiki's [[castles-as-upgraded-cycle-count](pages/castles-as-upgraded-cycle-count.md)] Analysis page adopts.

## Entities & Concepts

- [[castles-as-upgraded-cycle-count](pages/castles-as-upgraded-cycle-count.md)] — the Analysis page this note is the source for.
- [[permutation-cycle-castle-analogy](pages/permutation-cycle-castle-analogy.md)] — the analogy the note upgrades from correspondence to proof template.
- [[castle-sign](pages/castle-sign.md)], [[castle-foata-transform](pages/castle-foata-transform.md)], [[monotone-streak-factorization](pages/monotone-streak-factorization.md)] — the three castle-side moves the note maps to the `(n−1)!` proof moves.
- [[castle-counting-formula](pages/castle-counting-formula.md)] — the closed form used in the `F(4,2)` hand-check.
- [[generalized-dyck-grammar](pages/generalized-dyck-grammar.md)] — the factorization that makes the analogy a genuine structural correspondence.

## Relation to Other Wiki Pages

This note is the source that crystallizes the seminar framing behind the wiki's cycle-factorization thread. Where [[permutation-cycle-castle-analogy](pages/permutation-cycle-castle-analogy.md)] states the analogy and each of [[castle-sign](pages/castle-sign.md)] / [[castle-foata-transform](pages/castle-foata-transform.md)] / [[monotone-streak-factorization](pages/monotone-streak-factorization.md)] develops one castle-side construction, this note supplies the **elementary anchor** (`(n−1)!`) and the **closing correspondence table** that pull the three constructions into a single upgrade narrative. The synthesis lives on [[castles-as-upgraded-cycle-count](pages/castles-as-upgraded-cycle-count.md)].

## Footnotes

[^1]: [[pe502-castle-cycle-permutations](pages/pe502-castle-cycle-permutations.md)] §"Warm-up: labelled cycles" L5-L10 — "A cycle on n labelled items is a cyclic arrangement - an ordering up to rotation. The number of such directed cycles is (n-1)!, with two standard proofs: 1. Quotient by rotation ... 2. Fix a starting point ... Both proofs are instances of a bigger machine (Foata, sign, cycle-follow) that reappears in PE 502."
[^2]: [[pe502-castle-cycle-permutations](pages/pe502-castle-cycle-permutations.md)] §"Tying back to (n-1)!" L76-L86 — the three-row table mapping "divide by n / canonical form starting from element 1 / cycle-follow" to "castle sign / castle Foata / monotone streak scan", closing "PE 502 is essentially: take the toolkit that proves (n-1)!, upgrade every step to a version that handles stacked, width-weighted, sign-selected cycles, and you get a closed form plus a fast recurrence."
[^3]: [[pe502-castle-cycle-permutations](pages/pe502-castle-cycle-permutations.md)] §"Connection 1" L40-L42 and §"Connection 2" L56 — "F(w,h) = ½(h^w − (h−1)^w − P(h−1,w) + P(h−2,w)) ... F(4,2): h^w = 16, (h−1)^w = 1, P(1,4) = −4, P(0,4) = 1 ... F(4,2) = (16 − 1 + 4 + 1)/2 = 10 ... the 10 length-4 binary strings with one positive run: 1000, 0100, 0010, 0001, 1100, 0110, 0011, 1110, 0111, 1111." P(1,4) = −4 and P(0,4) = 1 re-verified during ingest.
[^4]: [[pe502-castle-cycle-permutations](pages/pe502-castle-cycle-permutations.md)] §"The caveat worth flagging" L72-L74 — "Block count ≠ peak count. A tall peak can be several stacked blocks. So the (−1)^blocks sign atom and the peak-count analogue of cycle count are different statistics on the same castle."
[^5]: [[pe502-castle-cycle-permutations](pages/pe502-castle-cycle-permutations.md)] §"The caveat worth flagging" L74 — "That is the fingerprint of a genuinely richer combinatorial object than plain permutations - the castle sits somewhere between 'cycles of a permutation' and 'cycles with multiplicity/height.'"
