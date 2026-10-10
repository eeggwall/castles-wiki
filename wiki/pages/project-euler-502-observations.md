---
title: "PE 502: Observations"
category: Sources
summary: The observations subpage, a list of short notes on PE 502 - sibling blocks carry independent towers, the tower count T(k, L) = (k+1)^L, the even-block count F = (A + S)/2, the any-parity count A(w, h) = h^w − (h−1)^w, the extra block an odd height needs, the factorizations of F(13, 10) and F(10, 13), and four methodology lessons.
tags: [project-euler, castle, observations, lessons, source, subpage]
sources: [project-euler-502-observations]
created: 2026-09-13
updated: 2026-10-10
---

# Project Euler 502 (PE 502): Observations

**Source:** https://charlesreid1.com/wiki/Project_Euler/502/Observations
**Date ingested:** 2026-09-13
**Type:** article (MediaWiki subpage of [[project-euler-502](pages/project-euler-502.md)])

## Summary

The subpage is a list of short notes, each a sentence or two, that restate results from the other subpages. This page records them in the wiki's notation ([[castle-notation](pages/castle-notation.md)]) and corrects one of them.

- **Sibling independence.** Two blocks in the same row are separated by a gap, and the tower on each is chosen independently of the other.[^1] On the wiki this is the structural property of the [[generalized-dyck-grammar](pages/generalized-dyck-grammar.md)] that lets a tower be decomposed block by block.
- **The tower count.** A tower of height `≤ k` on a base of length `L` is a sequence of column heights in `{0, …, k}`, so `T(k, L) = (k + 1)^L`.[^2] The source derives this from the binary-string bijection ([[binary-string-bijection](pages/binary-string-bijection.md)]); reading the tower as its column heights gives it directly.
- **The even-block count.** With `A(w, h)` the number of castles of width `w` and height exactly `h` and `S(w, h) = Σ (−1)^{blocks}` over the same castles, the even-block count is `F(w, h) = (A(w, h) + S(w, h))/2` ([[castle-sign](pages/castle-sign.md)]).[^3]
- **Without the parity clause.** Dropping the even-block requirement leaves `A(w, h) = h^w − (h−1)^w`: the column-height sequences in `{1, …, h}^w` minus those in `{1, …, h−1}^w`.[^4] All the work in computing `F` is in `S(w, h) = P(h−2, w) − P(h−1, w)`, the signed tower counts of [[signed-tower-count](pages/signed-tower-count.md)].
- **Odd heights.** In the U/R/D enumeration of [[urd-step-strings](pages/urd-step-strings.md)], the shortest string for height `h` has `h` blocks, which is odd when `h` is odd. The fix adds one block (a `U`, a `D` and two more `R` steps), so an even-block castle of odd height has `h + 1` blocks or more and width at least 3: `F(1, h) = F(2, h) = 0` for odd `h`.[^5] The source states this as "two extra rows"; the height does not change, and the addition is one block.
- **Factorizations.** The problem statement gives `F(13, 10) = 3729050610636` and `F(10, 13) = 37959702514`.[^pe] The source factors them as `F(13, 10) = 2²·3·13·1163·20553887` and `F(10, 13) = 2·102859·184523`.[^6]
- **Lessons.** Four methodology notes: enumerate small cases before trusting a formula; past about `10¹²`, use generating functions instead of enumeration; the choice of representation decides how hard the problem is; and [[berlekamp-massey](pages/berlekamp-massey.md)] recovers an unknown linear recurrence from enough terms of a sequence.[^7]

The source calls sibling independence "the single fact that makes the problem tractable." It is not: the tower count follows from column heights without it, and the cost of computing `F` lies in `P(k, L)` ([[castle-count-algorithms](pages/castle-count-algorithms.md)]).

## Where each note leads

- **Sibling independence** is part of the [[generalized-dyck-grammar](pages/generalized-dyck-grammar.md)] and is worked through on [[tower-recursion-master-class](pages/tower-recursion-master-class.md)].
- **`F = (A + S)/2`** is the `m = 2` case of the roots-of-unity filter on [[parity-via-roots-of-unity](pages/parity-via-roots-of-unity.md)]. [[block-count-constraints](pages/block-count-constraints.md)] treats other constraints on the block count, [[generating-functions-topic](pages/generating-functions-topic.md)] has the exponential generating function version `(e^x + e^{−x})/2`, and [[castles-as-upgraded-cycle-count](pages/castles-as-upgraded-cycle-count.md)] compares it with `(1 ± sgn(σ))/2`, which picks out the even permutations.
- **The parity clause as one bit.** Since `S(w, h)` is exponentially smaller than `A(w, h)`, `log₂ F(w, h) = log₂ A(w, h) − 1` up to a correction that vanishes as `w` grows ([[castle-entropy](pages/castle-entropy.md)], [[one-bit-seminar](pages/one-bit-seminar.md)]). The rows of `A(w, h)` are A000225 (`h = 2`), A001047 (`h = 3`), A005061 (`h = 4`), A005060 (`h = 5`) and A005062 (`h = 6`) ([[castle-counting-function](pages/castle-counting-function.md)], [[oeis-index](pages/oeis-index.md)]); the even-block row `F(w, 3)` is on [[new-sequence-fw3](pages/new-sequence-fw3.md)].
- **The factorizations** are single values of what [[mod-p-observatory](pages/mod-p-observatory.md)] studies: `F(w, h) mod p` is eventually periodic in each direction.
- **Berlekamp–Massey** is used on [[recurrence-discovery](pages/recurrence-discovery.md)], computes the `h > 15000` targets on [[castle-count-algorithms](pages/castle-count-algorithms.md)], and is the attack on a secret castle's count stream on [[castle-cryptography](pages/castle-cryptography.md)].

## Entities & Concepts

- [[castle-notation](pages/castle-notation.md)] - `A`, `F`, `S`, `T`, `P` as used above.
- [[generalized-dyck-grammar](pages/generalized-dyck-grammar.md)] - sibling independence in the grammar.
- [[castle-sign](pages/castle-sign.md)] - the sign `(−1)^{blocks}` and `F = (A + S)/2`.
- [[castle-counting-formula](pages/castle-counting-formula.md)] - `T(k, L) = (k + 1)^L` and the formula for `F` in terms of `P`.
- [[signed-tower-count](pages/signed-tower-count.md)] - `P(k, L)`.
- [[urd-step-strings](pages/urd-step-strings.md)] - the shortest U/R/D strings and the odd-height fix.
- [[berlekamp-massey](pages/berlekamp-massey.md)] - the recurrence-recovery method named in the lessons.

Also linked from the source: [[project-euler-502-solution](pages/project-euler-502-solution.md)].

## Relation to Other Wiki Pages

Every note on the source restates a result proved or computed on another subpage: [[project-euler-502-solution](pages/project-euler-502-solution.md)] for the tower count and the formula for `F`, [[project-euler-502-representations](pages/project-euler-502-representations.md)] for the U/R/D strings, and [[project-euler-502-implementation-notes](pages/project-euler-502-implementation-notes.md)] for the computation.

## Footnotes

[^1]: [[project-euler-502-observations](pages/project-euler-502-observations.md)] §"Sub-block independence" L5 - "Two sibling blocks in the same row generate towers that never interact (the parent-row gap is automatic)."
[^2]: [[project-euler-502-observations](pages/project-euler-502-observations.md)] §"T(k, L) = (k+1)^L" L7-9 - "The closed form for the number of towers of height at most k above a block of length L. Falls out of the binary-string bijection plus independence."
[^3]: [[project-euler-502-observations](pages/project-euler-502-observations.md)] §"Parity via signs" L13 - the even-block count as half the sum of the unsigned and the `(−1)^{blocks}`-signed counts.
[^4]: [[project-euler-502-observations](pages/project-euler-502-observations.md)] §"The \"even number of blocks\" clause is almost the entire difficulty" L17 - "Without it, the answer is just h^w - (h-1)^w: all castles of height at most h minus those of height at most h-1."
[^5]: [[project-euler-502-observations](pages/project-euler-502-observations.md)] §"Bare-minimum strings" L21 - "Odd h needs two extra rows to make the block count even."; [[project-euler-502-representations](pages/project-euler-502-representations.md)] §"Step 1 Bare Minimum String" L159-161 - "we insert an extra U and an extra D, and two extra Rs to separate them." Verified by execution (Python 3, 2026-10-10): brute force gives `F(w, 3) = 0, 0, 3, 21, 89` and `F(w, 5) = 0, 0, 10, 122` for `w = 1, 2, …`.
[^pe]: https://projecteuler.net/problem=502 - the problem lists `F(13,10) = 3729050610636` and `F(10,13) = 37959702514` among its example values.
[^6]: [[project-euler-502-observations](pages/project-euler-502-observations.md)] §"Useful factorizations" L25-31 - "F(13,10) = 3729050610636 = 2^2 × 3 × 1163 × 13 × 20553887" and "F(10,13) = 37959702514 = 2 × 102859 × 184523". Verified by execution (SymPy `factorint`, 2026-10-10).
[^7]: [[project-euler-502-observations](pages/project-euler-502-observations.md)] §"Lessons learned" L35-38 - "Enumerate small cases before trusting a formula. When counts run past 10^{12}, stop counting and start generating (functions). The right representation collapses the problem; the wrong one hides it. Berlekamp-Massey turns 'I have a sequence, I don't know the recurrence' into a solved problem."
