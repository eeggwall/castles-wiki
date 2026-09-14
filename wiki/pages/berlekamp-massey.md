---
title: Berlekamp–Massey
category: Concepts
summary: The algorithm that recovers the shortest linear recurrence generating a sequence; in PE 502 it turns an observed count sequence into the recurrence used to evaluate F at large parameters.
tags: [concept, algorithm, linear-recurrence, berlekamp-massey, method]
sources: [project-euler-502-observations]
created: 2026-09-13
updated: 2026-09-13
---

# Berlekamp–Massey

## Description

**Berlekamp–Massey** is the algorithm that, given the leading terms of a sequence, recovers the shortest linear recurrence that generates it. In the castle work it is highlighted as a key tool: it "turns 'I have a sequence, I don't know the recurrence' into a solved problem."[^1] That is exactly the situation the counting problem lands in — the signed tower count `P(k,L)` is known to satisfy *some* linear recurrence in the relevant direction, and Berlekamp–Massey pins down that recurrence from computed terms so the sequence can be extrapolated cheaply.

Once the recurrence is known, the sequence can be advanced to a very large index by fast linear-recurrence evaluation. For the castle problem this is the route to the trillion-scale grid parameters: the [[castle-counting-formula](pages/castle-counting-formula.md)] needs `P(k,L)` at `L` up to 10¹², and the [[monotone-streak-factorization](pages/monotone-streak-factorization.md)] page records that `P(k,L)` is evaluated in `O(k² log L)` by Kitamasa in the *L* direction, or in the *k* direction by Berlekamp–Massey — the pairing that computes `F(10^12, 100)` and `F(100, 10^12)`.

This page is a stub keyed to the castle problem's use of the method; the full algorithmic detail and its role in the actual solution code will be filled in when the Solution and Implementation Notes subpages are ingested.

## Appearances in Sources

- [[project-euler-502-observations](pages/project-euler-502-observations.md)] — names Berlekamp–Massey as a lesson learned: it recovers an unknown recurrence from a sequence.

## Related Concepts

- [[monotone-streak-factorization](pages/monotone-streak-factorization.md)] — where the *k*-direction Berlekamp–Massey evaluation of `P(k,L)` is described (paired with Kitamasa in the *L* direction).
- [[castle-counting-formula](pages/castle-counting-formula.md)] — the formula whose `P(k,L)` term is evaluated by these fast-recurrence methods.
- [[castle-counting-function](pages/castle-counting-function.md)] — the large-parameter evaluations `F(10^12,100)`, `F(100,10^12)` this enables.

## Footnotes

[^1]: [[project-euler-502-observations](pages/project-euler-502-observations.md)] §"Lessons learned" L38 — "Berlekamp-Massey turns 'I have a sequence, I don't know the recurrence' into a solved problem."
