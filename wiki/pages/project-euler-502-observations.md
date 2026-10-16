---
title: "PE 502: Observations"
category: Sources
summary: The Observations subpage lists six facts about the castle count - towers on different blocks of a row are independent, T(k, L) = (k+1)^L, the even-block count as half the sum of an unsigned and a signed count, the count A(w, h) = h^w − (h−1)^w without the even-block condition, the bare-minimum step string at odd height, and the factorizations of two checkpoint values - and closes with four lessons on method.
tags: [project-euler, castle, observations, lessons, source, subpage]
sources: [project-euler-502-observations]
created: 2026-09-13
updated: 2026-10-16
---

# Project Euler 502 (PE 502): Observations

**Source:** https://charlesreid1.com/wiki/Project_Euler/502/Observations
**Date ingested:** 2026-09-13
**Type:** article (MediaWiki subpage of [[project-euler-502](pages/project-euler-502.md)])

## Summary

This subpage states six facts about the castle count, each in a few lines, and leaves the proofs to the other subpages. The source writes `F(w, h)` for the even-block count, which the wiki writes `A^e(w, h)` ([[castle-notation](pages/castle-notation.md)]). It closes with four lessons on method, one of which names the Berlekamp-Massey algorithm, which finds the shortest linear recurrence that generates a given sequence ([[berlekamp-massey](pages/berlekamp-massey.md)]).[^1]

## Key Takeaways

- **Towers on different blocks are independent.** "Two sibling blocks in the same row generate towers that never interact (the parent-row gap is automatic)."[^2] Every block lies within the span of the block below it, so the towers on two blocks of a row stand over disjoint runs of columns, separated by the gap between the two blocks, and are chosen independently.
- **`T(k, L) = (k+1)^L`**, the number of towers of height at most `k` on a base of length `L`, follows from the binary-string bijection and this independence; the source points to the Solution subpage for the proof.[^3] The proof is also on [[castle-counting-formula](pages/castle-counting-formula.md)], the section *Tower count*.
- **The even-block count from a signed count.** The source writes the even-block count as `(A + P)/2`, with `A` "the unsigned total" and `P` "the signed count with `(−1)^{blocks}`".[^4] In the wiki's symbols, among the `T(k, L)` towers of height at most `k` on a base of length `L` the even-block ones number `(T + P)/2`, and among the castles of width `w` and height `h` the even-block ones number `A^e = (A + S)/2`, with `S` the signed count over castles. The two signs are opposite, because a castle has one block more than its towers ([[castle-sign](pages/castle-sign.md)]).
- **The count without the even-block condition** is "just `h^w − (h−1)^w`: all castles of height at most `h` minus those of height at most `h − 1`", the count `A(w, h)`.[^5]
- **Bare-minimum strings at odd height.** The source notes that at odd `h` the bare-minimum step string needs extra steps to make the block count even.[^6] The bare-minimum string `U^h R D^h` of the Representations subpage is the single column of height `h`, with `h` blocks. For odd `h` that subpage inserts one more `U … D` pair and two more `R` steps, as in `UUUUU R D R U R DDDDD` at `h = 5`: the castle `(5, 4, 5)` of width 3, with `h + 1 = 6` blocks ([[urd-step-strings](pages/urd-step-strings.md)]).[^7]
- **Two factorizations** of checkpoint values:[^8]

  ```
  A^e(13, 10)  =  3 729 050 610 636  =  2² · 3 · 13 · 1163 · 20553887
  A^e(10, 13)  =  37 959 702 514     =  2 · 102859 · 184523
  ```

## Entities & Concepts

- [[generalized-dyck-grammar](pages/generalized-dyck-grammar.md)] - the grammar of tower words, in which each `R` is spent once, so every block lies within the span of the block below it.
- [[binary-string-bijection](pages/binary-string-bijection.md)] - the first-row binary strings in the induction proof of `T(k, L) = (k+1)^L`.
- [[castle-counting-formula](pages/castle-counting-formula.md)] - three proofs of `T(k, L) = (k+1)^L` and the formula for `A^e(w, h)`.
- [[castle-sign](pages/castle-sign.md)] - the splits `(T ± P)/2` of towers and `(A ± S)/2` of castles by the parity of the block count.
- [[castle-counting-function](pages/castle-counting-function.md)] - the counts `A`, `A^e` and `A^o`, and the rows of `A(w, h) = h^w − (h−1)^w` in the OEIS.
- [[urd-step-strings](pages/urd-step-strings.md)] - the step-string encoding and the bare-minimum string.
- [[castle-entropy](pages/castle-entropy.md)] - the information content `log₂ A^e(w, h)` of a castle; the even-block condition lowers `log₂ A(w, h)` by about one bit.
- [[berlekamp-massey](pages/berlekamp-massey.md)] - the algorithm named in the last lesson.
- [[tower-recursion-master-class](pages/tower-recursion-master-class.md)] - a seminar on the tower count and the sign.

Also linked from the source: [[project-euler-502-solution](pages/project-euler-502-solution.md)], [[project-euler-502-representations](pages/project-euler-502-representations.md)].

## Relation to Other Wiki Pages

The observations are proved elsewhere on the wiki: the independence of towers and `T(k, L) = (k+1)^L` on [[project-euler-502-solution](pages/project-euler-502-solution.md)] and [[castle-counting-formula](pages/castle-counting-formula.md)], and the parity split on [[castle-sign](pages/castle-sign.md)].

## Footnotes

[^1]: [[project-euler-502-observations](pages/project-euler-502-observations.md)] §"Lessons learned" L35-38 [synthesis] - four lessons on method; the last is "Berlekamp-Massey turns \"I have a sequence, I don't know the recurrence\" into a solved problem."
[^2]: [[project-euler-502-observations](pages/project-euler-502-observations.md)] §"Sub-block independence" L5 - "Two sibling blocks in the same row generate towers that never interact (the parent-row gap is automatic)."
[^3]: [[project-euler-502-observations](pages/project-euler-502-observations.md)] §"T(k, L) = (k+1)^L" L9 - "The closed form for the number of towers of height at most k above a block of length L. Falls out of the binary-string bijection plus independence. The proof lives on Project Euler/502/Solution."
[^4]: [[project-euler-502-observations](pages/project-euler-502-observations.md)] §"Parity via signs" L13 - "Even-block-count is enforced by (A + P)/2, where A is the unsigned total and P is the signed count with (-1)^{blocks}."
[^5]: [[project-euler-502-observations](pages/project-euler-502-observations.md)] §"The \"even number of blocks\" clause is almost the entire difficulty" L17 - "Without it, the answer is just h^w - (h-1)^w: all castles of height at most h minus those of height at most h-1."
[^6]: [[project-euler-502-observations](pages/project-euler-502-observations.md)] §"Bare-minimum strings" L21 [synthesis] - at odd `h` the bare-minimum string must be extended to make the block count even, with a pointer to the Representations subpage.
[^7]: [[project-euler-502-representations](pages/project-euler-502-representations.md)] §"Step 1 Bare Minimum String" L153-165 - "for castles of height 4 and width 5, the bare minimum string would be 4 Us, 4 Ds, and one R to separate them", "we insert an extra U and an extra D, and two extra Rs to separate them. For example, for castles of height 5 ... U U U U U R D R U R D D D D D".
[^8]: [[project-euler-502-observations](pages/project-euler-502-observations.md)] §"Useful factorizations" L25-31 - "F(13,10) = 3729050610636 = 2^2 \times 3 \times 1163 \times 13 \times 20553887" and "F(10,13) = 37959702514 = 2 \times 102859 \times 184523". Both factorizations checked with SymPy `factorint` (2026-10-16).
