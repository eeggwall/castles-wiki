---
title: Berlekamp–Massey
category: Concepts
summary: The algorithm that recovers the shortest linear recurrence generating a sequence; in PE 502 it turns an observed count sequence into the recurrence used to evaluate F at large parameters.
tags: [concept, algorithm, linear-recurrence, berlekamp-massey, method]
sources: [project-euler-502-observations, project-euler-502-solution, project-euler-502-implementation-notes]
created: 2026-09-13
updated: 2026-09-19
---

# Berlekamp–Massey

## Description

**Berlekamp–Massey** is the algorithm that, given the leading terms of a sequence, recovers the shortest linear recurrence that generates it. In the castle work it is highlighted as a key tool: it "turns 'I have a sequence, I don't know the recurrence' into a solved problem."[^1] That is exactly the situation the counting problem lands in — the signed tower count `P(k,L)` is known to satisfy *some* linear recurrence in the relevant direction, and Berlekamp–Massey pins down that recurrence from computed terms so the sequence can be extrapolated cheaply. A notable practical point: Berlekamp–Massey *discovers* the recurrence empirically, so no proof of the recurrence is needed to use it - the transfer-matrix argument only justifies that one exists.[^3]

Once the recurrence is known, [[kitamasa](pages/kitamasa.md)] advances the sequence to a very large index. In the castle problem this is the *k*-direction path of the [[castle-count-algorithms](pages/castle-count-algorithms.md)] (used when `h > 15000`); the sample-count formula `N = 4(w+2)+20`, the pinned order (`2L−2` for `L ≥ 4`), and the recovered recurrences and characteristic polynomials are on [[recurrence-discovery](pages/recurrence-discovery.md)], and the `computePviaKBoth` code walk (including the `poly2 · x mod charPoly` one-pass index-shift that saves a second Kitamasa call) is on [[project-euler-502-implementation-notes](pages/project-euler-502-implementation-notes.md)] §"k-direction BM path".

This page is a stub keyed to the castle problem's use of the method; the general algorithm and the deeper literature connections will be built out as those threads are traced.

## Appearances in Sources

- [[project-euler-502-observations](pages/project-euler-502-observations.md)] — names Berlekamp–Massey as a lesson learned: it recovers an unknown recurrence from a sequence.
- [[project-euler-502-solution](pages/project-euler-502-solution.md)] — specifies the *k*-direction path: `N = 4(w+2)+20` terms, order ~`2w`, one-pass extraction of `P(h−2,w)` and `P(h−1,w)`.
- [[project-euler-502-implementation-notes](pages/project-euler-502-implementation-notes.md)] — the `computePviaKBoth` code steps and the `poly2·x mod charPoly` one-pass shift.

## Related Concepts

- [[kitamasa](pages/kitamasa.md)] — the partner method that jumps to a far index once the recurrence is known.
- [[castle-count-algorithms](pages/castle-count-algorithms.md)] — the *k*-direction path where Berlekamp–Massey is used.
- [[monotone-streak-factorization](pages/monotone-streak-factorization.md)] — the canonical form underlying the recurrences.
- [[castle-counting-formula](pages/castle-counting-formula.md)] — the formula whose `P(k,L)` term is evaluated by these fast-recurrence methods.
- [[castle-counting-function](pages/castle-counting-function.md)] — the large-parameter evaluations `F(10^12,100)`, `F(100,10^12)` this enables.
- [[recurrence-discovery](pages/recurrence-discovery.md)] — running Berlekamp–Massey in both directions pins the k-direction order to exactly `2L−2` for `L ≥ 4`.
- [[castle-compression](pages/castle-compression.md)] — linear complexity, the shortest linear recurrence, is "shortest program" restricted to linear machines: a detector for the rule-generated tier.

## Footnotes

[^1]: [[project-euler-502-observations](pages/project-euler-502-observations.md)] §"Lessons learned" L38 — "Berlekamp-Massey turns 'I have a sequence, I don't know the recurrence' into a solved problem."
[^3]: [[project-euler-502-solution](pages/project-euler-502-solution.md)] §"The k-direction Berlekamp-Massey path (h > 15000)" L165 — "The recurrence order is at most about 2w empirically. Berlekamp-Massey discovers the recurrence, so no proof is required to use it, but the transfer-matrix argument justifies why one exists."
