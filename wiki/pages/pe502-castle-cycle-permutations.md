---
title: "PE 502 castles as an upgrade of the (n−1)! cycle-count proof"
category: Sources
summary: A working note framing PE 502 as the elementary (n−1)! cycle-count toolkit — quotient-by-rotation, canonical form, cycle-following — upgraded step-by-step into the castle's sign / Foata / streak-factorization triad. The synthesis behind [[castles-as-upgraded-cycle-count]].
tags: [note, castle, permutations, cycles, seminar, source]
sources: [pe502-castle-cycle-permutations]
created: 2026-09-15
updated: 2026-09-22
---

# Project Euler 502 (PE 502) castles as an upgrade of the (n−1)! cycle-count proof

**Source:** `raw/pe502-castle-cycle-permutations.md` (working note authored 2026-09-15 in preparation for a seminar spine)
**Date ingested:** 2026-09-15
**Type:** note (markdown, line-numbered; ~86 lines)

## Summary

The note builds a **direct upgrade path** from the two elementary proofs of "there are `(n−1)!` labelled cycles on `n` items" — quotient by the free `Z/n` rotation, or fix the cycle to start at element `1` — to the full castle-counting toolkit of PE 502. Both proofs, the note argues, are instances of a bigger machine (**Foata, sign, cycle-follow**) that reappears intact on the castle side.[^1] The three-row proof-move ↔ castle-counterpart correspondence table (*divide by `n` / `(1 ± sgn)/2`* → [[castle-sign](pages/castle-sign.md)], *canonical form / Foata* → [[castle-foata-transform](pages/castle-foata-transform.md)], *cycle-follow `i ↦ σ(i)`* → [[monotone-streak-factorization](pages/monotone-streak-factorization.md)]) is single-sourced on [[permutation-cycle-castle-analogy](pages/permutation-cycle-castle-analogy.md)] §"The (n−1)! anchor"; the `F(4,2) = 10` hand-check that runs the machinery in miniature, the seminar-shaped narrative, and the "block count ≠ peak count" caveat that gives the castle its shape all live on the Analysis this note is the source for: [[castles-as-upgraded-cycle-count](pages/castles-as-upgraded-cycle-count.md)].[^2]

## Threads the note opens

- **Its own source material.** The sign / Foata / streak triad the note upgrades toward was first written down on the PE subpage [[project-euler-502-castle-factoring](pages/project-euler-502-castle-factoring.md)]; the permutation-side Foata apparatus (two-line arrays, intercalation, unique cycle factorization) is Knuth's, on [[aocp-multisets](pages/aocp-multisets.md)]; and the `n!` and `(n−1)! = n!/n` basics are on [[aocp-permutations](pages/aocp-permutations.md)].
- **Where the analogy becomes literal.** A **rainbow castle** ([[castle-classification-shape](pages/castle-classification-shape.md)]: `w = h`, heights a permutation of `{1..h}`) has a skyline that *is* a permutation, so the three moves apply to it verbatim, and the classification's **even-peak** type is precisely the "block count ≠ peak count" caveat turned into a predicate the wiki has not yet investigated.
- **The `(1 ± sgn)/2` move, generalized.** Peeling `A_n` from `S_n` is the `m = 2` character sum; [[parity-via-roots-of-unity](pages/parity-via-roots-of-unity.md)] does it for `Z/m`, and [[tower-recursion-master-class](pages/tower-recursion-master-class.md)] teaches the `(T ± P)/2` lesson end-to-end, `F(4,2) = 10` included. `F(4,2) = 10` is also one of the three checkpoints the problem statement supplies ([[castle-counting-function](pages/castle-counting-function.md)]), and `all_castles(4, 2)` on [[castle-snippets](pages/castle-snippets.md)] reproduces the ten strings.
- **Even blocks ⟺ odd runs.** A height-2 castle has `1 + (number of maximal positive runs in row 2)` blocks, so the even-block castles are those whose second row has an odd number of runs: `F(w,2) = Σ_s C(w+1, 4s+2) = A038505(w+1)` ([[hyperbolic-sequence-family](pages/hyperbolic-sequence-family.md)]), the `m = 2` residue extraction of [[block-count-constraints](pages/block-count-constraints.md)]. At `w = 4` the only odd run count that fits is one, so the hand-check's ten strings are the one-run strings, `C(5,2) = 10`; at `w = 5` the three-run string `10101` joins and `F(5,2) = C(6,2) + C(6,6) = 16`.

## Entities & Concepts

- [[castles-as-upgraded-cycle-count](pages/castles-as-upgraded-cycle-count.md)] — the Analysis page this note is the source for.
- [[permutation-cycle-castle-analogy](pages/permutation-cycle-castle-analogy.md)] — the analogy the note upgrades from correspondence to proof template; carries the three-row correspondence table.
- [[castle-sign](pages/castle-sign.md)], [[castle-foata-transform](pages/castle-foata-transform.md)], [[monotone-streak-factorization](pages/monotone-streak-factorization.md)] — the three castle-side moves the note maps to the `(n−1)!` proof moves.
- [[castle-counting-formula](pages/castle-counting-formula.md)] — the closed form used in the `F(4,2)` hand-check on the Analysis.
- [[generalized-dyck-grammar](pages/generalized-dyck-grammar.md)] — the factorization that makes the analogy a genuine structural correspondence.
- [[project-euler-502-castle-factoring](pages/project-euler-502-castle-factoring.md)] / [[aocp-multisets](pages/aocp-multisets.md)] / [[aocp-permutations](pages/aocp-permutations.md)] — the castle-side and permutation-side sources of the triad.
- [[castle-classification-shape](pages/castle-classification-shape.md)] — rainbow castles (skyline = permutation) and the even-peak type (the block ≠ peak caveat as a predicate).
- [[parity-via-roots-of-unity](pages/parity-via-roots-of-unity.md)] / [[tower-recursion-master-class](pages/tower-recursion-master-class.md)] / [[castle-counting-function](pages/castle-counting-function.md)] / [[castle-snippets](pages/castle-snippets.md)] — the sign move generalized and taught; `F(4,2) = 10` as checkpoint and as code.
- [[hyperbolic-sequence-family](pages/hyperbolic-sequence-family.md)] / [[block-count-constraints](pages/block-count-constraints.md)] — why the one-run description of `F(4,2)` does not survive to `w = 5`.

## Relation to Other Wiki Pages

This note is the source that crystallizes the seminar framing behind the wiki's cycle-factorization thread. Where [[permutation-cycle-castle-analogy](pages/permutation-cycle-castle-analogy.md)] states the analogy, carries the three-row correspondence table, and points at each castle-side construction, and each of [[castle-sign](pages/castle-sign.md)] / [[castle-foata-transform](pages/castle-foata-transform.md)] / [[monotone-streak-factorization](pages/monotone-streak-factorization.md)] develops one castle-side construction, this note supplies the **elementary anchor** (`(n−1)!`) and the closing correspondence that pull the three constructions into a single upgrade narrative. The synthesis lives on [[castles-as-upgraded-cycle-count](pages/castles-as-upgraded-cycle-count.md)].

## Footnotes

[^1]: [[pe502-castle-cycle-permutations](pages/pe502-castle-cycle-permutations.md)] §"Warm-up: labelled cycles" L5-L10 — "A cycle on n labelled items is a cyclic arrangement - an ordering up to rotation. The number of such directed cycles is (n-1)!, with two standard proofs: 1. Quotient by rotation ... 2. Fix a starting point ... Both proofs are instances of a bigger machine (Foata, sign, cycle-follow) that reappears in PE 502."
[^2]: [[pe502-castle-cycle-permutations](pages/pe502-castle-cycle-permutations.md)] §"Tying back to (n-1)!" L76-L86 — the three-row table mapping "divide by n / canonical form starting from element 1 / cycle-follow" to "castle sign / castle Foata / monotone streak scan", closing "PE 502 is essentially: take the toolkit that proves (n-1)!, upgrade every step to a version that handles stacked, width-weighted, sign-selected cycles, and you get a closed form plus a fast recurrence." §"The caveat worth flagging" L72-L74 — "Block count ≠ peak count."
