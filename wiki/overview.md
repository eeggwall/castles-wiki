---
title: Overview
tags: [overview, synthesis]
sources: [project-euler-502, project-euler-502-problem-setup, project-euler-502-representations, project-euler-502-castle-factoring, project-euler-502-observations, project-euler-502-solution, counting-horizontally-convex-polyominoes, column-convex-polygon-enumeration, steep-polyominoes-q-motzkin-bessel]
updated: 2026-09-13
---

# Project Euler 502 — Overview

> Evolving synthesis of everything in the wiki. Updated by wiki-ingest when sources shift the understanding.

## Mission

This wiki does more than record the PE 502 solution. Its purpose is to take **every thread that runs through the known solution methods — and the failed ones — and follow each into the broader polyomino and combinatorics literature**, to find the profound connections PE 502 has to other branches of mathematics, surface research topics, and give seminars and external collaborators concrete threads to pull. Each concept page is written as a thread to follow, not merely a solved step; each ingested paper is an entry point into a neighboring domain.

## Current Understanding

The wiki studies **castles**: configurations of stacked integer-length, unit-height *blocks* on a *w*×*h* grid, obeying a fixed set of placement rules (no overhangs or floating blocks, grid-snapped, ≥1 unit gap between same-row neighbors, a full-width bottom row, and a maximum height of exactly *h*). See [[castle-polyomino](pages/castle-polyomino.md)].

The general object of interest is the castle at **any** block count, counted by `A(w,h)` (all castles of exact height *h*, either parity). [[project-euler-502](pages/project-euler-502.md)] studies a special case: its counting function [[castle-counting-function](pages/castle-counting-function.md)] `F(w,h)` is `A(w,h)` restricted to an **even** number of blocks, and asks for `(F(10^12,100) + F(10000,10000) + F(100,10^12)) mod 1,000,000,007`. This wiki treats the even-block parity restriction as a special case of the broader, more interesting problem of counting all castles regardless of parity. (The odd count `A − F` is left unnamed for now — `G` is reserved for generating functions.)

**The counting problem has a solved closed form.** Castles admit three exact encodings — collected on [[castle-representations](pages/castle-representations.md)] (binary strings, integer tuples, and U/R/D step strings). The U/R/D encoding ([[urd-step-strings](pages/urd-step-strings.md)]) recasts the castle rules as a [[generalized-dyck-grammar](pages/generalized-dyck-grammar.md)], from which the [[castle-counting-formula](pages/castle-counting-formula.md)] follows: an unsigned tower count `T(k,L) = (k+1)^L`, a signed count `P` that encodes the even-block rule as a −1 weight per block, and `F(w,h) = [h^w − (h−1)^w − P(h−1,w) + P(h−2,w)]/2`. This reproduces all three integer checkpoints (verified by executing the source's Python). The enumeration side is organized around the [[convex-castle](pages/convex-castle.md)] class (counted by `C(2H+W−3, W−1)`) and its variations.

**A cycle-factorization reading unifies the machinery.** The integer-tuple / column-height encoding is the workhorse of a second reading built on the analogy [[permutation-cycle-castle-analogy](pages/permutation-cycle-castle-analogy.md)] (permutation cycles ↔ castle peaks). It supplies a product-form proof of `T(k,L)=(k+1)^L` (independent column heights), a [[castle-sign](pages/castle-sign.md)] `s(C)=(−1)^blocks` that makes `P` a genuine sign homomorphism (the `(T±P)/2` even/odd projector), a [[castle-foata-transform](pages/castle-foata-transform.md)] (peaks ↔ positive runs ↔ records), and a [[monotone-streak-factorization](pages/monotone-streak-factorization.md)] — the `O(L)` canonical form over which the fast algorithms (Kitamasa, [[berlekamp-massey](pages/berlekamp-massey.md)]) evaluate the trillion-scale cases.

**The crux and what the parity clause costs.** The single insight that made the problem tractable — and "took years to see" — is that sibling towers in the same row never interact; this column independence (captured on [[generalized-dyck-grammar](pages/generalized-dyck-grammar.md)], and structurally a consequence of the horizontal `R` step that separates a plain Dyck word from the Dyck *grammar*) is what yields the product form. The even-block clause is "almost the entire difficulty": without it the count collapses to the unsigned baseline `h^w − (h−1)^w`, and the entire signed apparatus (`P`, the sign, Berlekamp–Massey) exists to enforce that one parity constraint.

**How the targets are actually computed.** The full solution ([[project-euler-502-solution](pages/project-euler-502-solution.md)]) proves `T(k,L)=(k+1)^L` by induction via the [[binary-string-bijection](pages/binary-string-bijection.md)] and routes each large target through the [[castle-count-algorithms](pages/castle-count-algorithms.md)]: a rational-function path (`h ≤ 15000`) with a direct or [[kitamasa](pages/kitamasa.md)] extractor, and a *k*-direction [[berlekamp-massey](pages/berlekamp-massey.md)] path (`h > 15000`). It also records what *did not* work (direct enumeration; binary strings without independence; convex-castle variation enumeration; L-direction transfer matrix as primary).

**Threads into the wider literature.** Three reference papers are now ingested as entry points: [[counting-horizontally-convex-polyominoes](pages/counting-horizontally-convex-polyominoes.md)] (a neighboring convexity class whose count collapses to a short recurrence via restricted-shape auxiliaries), [[column-convex-polygon-enumeration](pages/column-convex-polygon-enumeration.md)] (the add-a-column / Temperley method — the closest external framework to the castle's column structure, with the classical Ferrers/stack/parallelogram families), and [[steep-polyominoes-q-motzkin-bessel](pages/steep-polyominoes-q-motzkin-bessel.md)] (steep Dyck words and q-Motzkin/q-Bessel generating functions — the Dyck-and-GF thread into q-analogs).

## Open Questions

- How does the count of *all* castles (`A`, both parities) relate to the even-only count `F`? The [[castle-counting-formula](pages/castle-counting-formula.md)] already exposes both halves — the unsigned `T` and the signed `P` — so this is a matter of reading off the general problem rather than an open derivation.
- **Which castles are column-convex or horizontally convex, and do the castle recurrences relate to `A001169` or the add-a-column functional equations?** The castle is a strongly column-structured object; [[column-convex-polyomino](pages/column-convex-polyomino.md)] and [[horizontally-convex-polyomino](pages/horizontally-convex-polyomino.md)] are the two convexity classes to map it against.
- **Is there a q-graded (area-tracking) castle count, and does it land on q-Motzkin / q-Bessel objects** like the steep-polyomino generating functions? The castle's U/R/D grammar and the steep Dyck words share a run-constraint flavor.
- Do the classical **stack / Ferrers / parallelogram** families correspond to castle sub-families?
- What does the *code* actually compute, versus the derivation? The solution enumerates none of the encodings directly — the Implementation Notes subpage (not yet ingested) holds that.

## Key Entities / Concepts

- [[castle-polyomino](pages/castle-polyomino.md)] — the central object: a valid stacked-block configuration on a grid, at any block parity.
- [[castle-counting-function](pages/castle-counting-function.md)] — `F(w,h)`, the number of castles; PE 502's even-block count is a special case.
- [[castle-counting-formula](pages/castle-counting-formula.md)] — the closed form for `F(w,h)`, derived and verified.
- [[castle-representations](pages/castle-representations.md)] — the three exact encodings of a castle.
- [[convex-castle](pages/convex-castle.md)] — the structural backbone of the enumeration.
- [[generalized-dyck-grammar](pages/generalized-dyck-grammar.md)] — the grammar linking castles to Dyck paths and yielding the count.
- [[generating-functions](pages/generating-functions.md)] — the method: a polynomial whose coefficients are the counts.
- [[permutation-cycle-castle-analogy](pages/permutation-cycle-castle-analogy.md)] — cycles ↔ peaks; the spine of the cycle-factorization reading, with the [[castle-sign](pages/castle-sign.md)], [[castle-foata-transform](pages/castle-foata-transform.md)], and [[monotone-streak-factorization](pages/monotone-streak-factorization.md)].
- [[berlekamp-massey](pages/berlekamp-massey.md)] / [[kitamasa](pages/kitamasa.md)] — the fast linear-recurrence toolkit; discover the recurrence for `P`, then jump to a far index, via the [[castle-count-algorithms](pages/castle-count-algorithms.md)].
- [[binary-string-bijection](pages/binary-string-bijection.md)] — block configs ↔ binary strings; the base of the `T(k,L)=(k+1)^L` induction.
- **Literature threads:** [[column-convex-polyomino](pages/column-convex-polyomino.md)] and [[horizontally-convex-polyomino](pages/horizontally-convex-polyomino.md)] (convexity classes to map the castle against), plus the three ingested papers above.
