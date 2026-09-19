---
title: "PE 502: Observations"
category: Sources
summary: The observations subpage — the crux (sibling sub-blocks don't interact), the parity-sign trick, why the even-block clause is the whole difficulty, verified factorizations, and lessons learned.
tags: [project-euler, castle, observations, lessons, source, subpage]
sources: [project-euler-502-observations]
created: 2026-09-13
updated: 2026-09-19
---

# Project Euler 502 (PE 502): Observations

**Source:** https://charlesreid1.com/wiki/Project_Euler/502/Observations
**Date ingested:** 2026-09-13
**Type:** article (MediaWiki subpage of [[project-euler-502](pages/project-euler-502.md)])

## Summary

This subpage distills the facts and lessons that cracked the castle problem open. Its headline claim is the crux: **two sibling blocks in the same row generate towers that never interact** — the parent-row gap is automatic — and this single fact, which "took years to see," is what makes the problem tractable.[^1] In this wiki that independence is captured as a structural property of the [[generalized-dyck-grammar](pages/generalized-dyck-grammar.md)] (each `R` is spent once, so siblings cannot interfere). Independence plus the binary-string bijection is exactly what gives the closed form `T(k,L) = (k+1)^L` for towers of height ≤ *k* above a length-*L* block.[^2]

The page also crystallizes three framing points already developed in earlier subpages: the even-block count is enforced by the parity-sign trick `(A + P)/2` (unsigned total `A`, signed count `P` with weight `(−1)^{blocks}`) — "a symmetry trick that recurs in many combinatorial-enumeration problems" (see [[castle-sign](pages/castle-sign.md)]);[^3] the **"even number of blocks" clause is almost the entire difficulty**, since without it the answer collapses to `h^w − (h−1)^w`;[^4] and odd *h* forces two extra rows in the bare-minimum string to keep the block count even (see [[urd-step-strings](pages/urd-step-strings.md)]).[^5]

Finally it records two concrete factorizations (both verified during ingest) and a short list of lessons learned — including that **Berlekamp–Massey** turns an unknown-recurrence sequence into a solved problem (see [[berlekamp-massey](pages/berlekamp-massey.md)]).[^6][^7]

## Key Takeaways

- **The crux — sub-block independence.** Sibling blocks in the same row spawn non-interacting towers (the separating gap is automatic); this is "the single fact that makes the problem tractable, and it took years to see."[^1] Captured on [[generalized-dyck-grammar](pages/generalized-dyck-grammar.md)].
- **`T(k,L) = (k+1)^L`** follows from the binary-string bijection plus that independence.[^2]
- **Parity via signs:** even-block-count `= (A + P)/2`, a general symmetry trick (unsigned total `A`, signed count `P` weighting each configuration by `(−1)^{blocks}`).[^3] See [[castle-sign](pages/castle-sign.md)].
- **The even-block clause is almost the whole difficulty:** drop it and the count is just `h^w − (h−1)^w` (all castles of height ≤ *h* minus those of height ≤ *h*−1).[^4]
- **Verified factorizations:** `F(13,10) = 3729050610636 = 2²·3·13·1163·20553887` and `F(10,13) = 37959702514 = 2·102859·184523` (both confirmed by factoring during ingest).[^6]

## Lessons learned (from the source)

The source lists four methodology lessons, recorded here as its own commentary:[^7]

- Enumerate small cases before trusting a formula.
- When counts run past 10¹², stop counting and start *generating* (functions).
- The right representation collapses the problem; the wrong one hides it.
- [[berlekamp-massey](pages/berlekamp-massey.md)] turns "I have a sequence, I don't know the recurrence" into a solved problem.

## Where each observation now lives

Each of the source's five observations has grown into a thread on the wiki.

- **The crux (sub-block independence)** is captured on [[generalized-dyck-grammar](pages/generalized-dyck-grammar.md)], taught end-to-end on [[tower-recursion-master-class](pages/tower-recursion-master-class.md)], and is the induction step of the [[binary-string-bijection](pages/binary-string-bijection.md)] proof of `T(k,L) = (k+1)^L`.
- **"A symmetry trick that recurs"** is the `m = 2` case of a general extraction: [[parity-via-roots-of-unity](pages/parity-via-roots-of-unity.md)] replaces the sign by an `m`-th root of unity, [[block-count-constraints](pages/block-count-constraints.md)] places it in a residue / sparse / semigroup trichotomy, [[generating-functions-topic](pages/generating-functions-topic.md)] shows the exponential generating function (EGF) twin `(e^x + e^{−x})/2`, and [[castles-as-upgraded-cycle-count](pages/castles-as-upgraded-cycle-count.md)] gives the elementary anchor - `(1 ± sgn)/2` peeling `A_n` out of `S_n`.
- **"Almost the entire difficulty" is now a number.** [[castle-entropy](pages/castle-entropy.md)] shows `log₂ F(w,h) ≈ w·log₂ h − 1`: the even-block clause costs exactly one bit. The unsigned baseline `h^w − (h−1)^w` is the any-parity count `A(w,h)` on [[castle-counting-function](pages/castle-counting-function.md)], the difference-of-powers rows A000225 (`h = 2`), A001047 (`h = 3`), A005061, A005060, A005062 (`4^n − 3^n`, `5^n − 4^n`, `6^n − 5^n`) indexed on [[oeis-index](pages/oeis-index.md)]; its `h = 3` complement is the new sequence on [[new-sequence-fw3](pages/new-sequence-fw3.md)].
- **The two factorizations** are point samples of what [[mod-p-observatory](pages/mod-p-observatory.md)] studies systematically (`F(w,h) mod p` is eventually periodic in each direction); the factoring machinery itself (Legendre's prime-multiplicity formula) is on [[aocp-permutations](pages/aocp-permutations.md)].
- **The Berlekamp–Massey lesson** is run in both directions on [[recurrence-discovery](pages/recurrence-discovery.md)], routes the `h > 15000` targets on [[castle-count-algorithms](pages/castle-count-algorithms.md)], and turns adversarial on [[castle-cryptography](pages/castle-cryptography.md)], where the same algorithm is the linear feedback shift register (LFSR) attack that reconstructs a secret castle from its count stream.

## Entities & Concepts

- [[generalized-dyck-grammar](pages/generalized-dyck-grammar.md)] — where the sub-block-independence crux is captured.
- [[castle-sign](pages/castle-sign.md)] — the `(A+P)/2` parity-sign trick.
- [[castle-counting-formula](pages/castle-counting-formula.md)] — `T(k,L)=(k+1)^L`, the `h^w−(h−1)^w` baseline, and the verified factorizations.
- [[berlekamp-massey](pages/berlekamp-massey.md)] — the recurrence-recovery method named in the lessons.
- [[urd-step-strings](pages/urd-step-strings.md)] — bare-minimum strings and the odd-*h* parity fix.
- [[tower-recursion-master-class](pages/tower-recursion-master-class.md)] / [[binary-string-bijection](pages/binary-string-bijection.md)] — the crux taught, and the induction it powers.
- [[parity-via-roots-of-unity](pages/parity-via-roots-of-unity.md)] / [[block-count-constraints](pages/block-count-constraints.md)] / [[generating-functions-topic](pages/generating-functions-topic.md)] / [[castles-as-upgraded-cycle-count](pages/castles-as-upgraded-cycle-count.md)] — the parity trick generalized, twinned, and anchored.
- [[castle-entropy](pages/castle-entropy.md)] / [[castle-counting-function](pages/castle-counting-function.md)] / [[oeis-index](pages/oeis-index.md)] / [[new-sequence-fw3](pages/new-sequence-fw3.md)] — the one-bit price of the even clause and the difference-of-powers baseline.
- [[mod-p-observatory](pages/mod-p-observatory.md)] / [[aocp-permutations](pages/aocp-permutations.md)] — factorizations, systematic and mechanical.
- [[recurrence-discovery](pages/recurrence-discovery.md)] / [[castle-count-algorithms](pages/castle-count-algorithms.md)] / [[castle-cryptography](pages/castle-cryptography.md)] — Berlekamp–Massey at work, and turned against the castle.

Also linked from the source, now ingested: [[project-euler-502-solution](pages/project-euler-502-solution.md)].

## Relation to Other Wiki Pages

This page adds little new machinery but supplies the *motivation and attribution* behind machinery already in the wiki: it names sub-block independence as the crux behind the product form, frames the parity-sign identity as a general technique, and isolates the even-block clause as the source of the difficulty. Its lessons and the Berlekamp–Massey pointer look ahead to [[project-euler-502-solution](pages/project-euler-502-solution.md)] and [[project-euler-502-implementation-notes](pages/project-euler-502-implementation-notes.md)], both since ingested.

## Footnotes

[^1]: [[project-euler-502-observations](pages/project-euler-502-observations.md)] §"Sub-block independence" L5 — "Two sibling blocks in the same row generate towers that never interact (the parent-row gap is automatic). This is the single fact that makes the problem tractable, and it took years to see."
[^2]: [[project-euler-502-observations](pages/project-euler-502-observations.md)] §"T(k, L) = (k+1)^L" L7-9 — "The closed form for the number of towers of height at most k above a block of length L. Falls out of the binary-string bijection plus independence."
[^3]: [[project-euler-502-observations](pages/project-euler-502-observations.md)] §"Parity via signs" L13 — "Even-block-count is enforced by (A + P)/2, where A is the unsigned total and P is the signed count with (-1)^{blocks}. A symmetry trick that recurs in many combinatorial-enumeration problems."
[^4]: [[project-euler-502-observations](pages/project-euler-502-observations.md)] §"The \"even number of blocks\" clause is almost the entire difficulty" L17 — "Without it, the answer is just h^w - (h-1)^w: all castles of height at most h minus those of height at most h-1."
[^5]: [[project-euler-502-observations](pages/project-euler-502-observations.md)] §"Bare-minimum strings" L21 — "Odd h needs two extra rows to make the block count even. This shows how the parity constraint bites even in the naive enumeration path."
[^6]: [[project-euler-502-observations](pages/project-euler-502-observations.md)] §"Useful factorizations" L25-31 — "F(13,10) = 3729050610636 = 2^2 × 3 × 1163 × 13 × 20553887" and "F(10,13) = 37959702514 = 2 × 102859 × 184523"; both re-factored during ingest and confirmed.
[^7]: [[project-euler-502-observations](pages/project-euler-502-observations.md)] §"Lessons learned" L35-38 — "Enumerate small cases before trusting a formula. When counts run past 10^{12}, stop counting and start generating (functions). The right representation collapses the problem; the wrong one hides it. Berlekamp-Massey turns 'I have a sequence, I don't know the recurrence' into a solved problem."
