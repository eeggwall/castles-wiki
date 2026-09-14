---
title: Overview
tags: [overview, synthesis]
sources: [project-euler-502, project-euler-502-problem-setup, project-euler-502-representations]
updated: 2026-09-13
---

# Project Euler 502 — Overview

> Evolving synthesis of everything in the wiki. Updated by wiki-ingest when sources shift the understanding.

## Current Understanding

The wiki studies **castles**: configurations of stacked integer-length, unit-height *blocks* on a *w*×*h* grid, obeying a fixed set of placement rules (no overhangs or floating blocks, grid-snapped, ≥1 unit gap between same-row neighbors, a full-width bottom row, and a maximum height of exactly *h*). See [[castle-polyomino](pages/castle-polyomino.md)].

The general object of interest is the castle at **any** block count. [[project-euler-502](pages/project-euler-502.md)] studies a special case: its counting function [[castle-counting-function](pages/castle-counting-function.md)] `F(w,h)` counts only castles with an **even** number of blocks, and asks for `(F(10^12,100) + F(10000,10000) + F(100,10^12)) mod 1,000,000,007`. This wiki treats the even-block parity restriction as a special case of the broader, more interesting problem of counting all castles regardless of parity.

**The counting problem has a solved closed form.** Castles admit three exact encodings — collected on [[castle-representations](pages/castle-representations.md)] (binary strings, integer tuples, and U/R/D step strings). The U/R/D encoding ([[urd-step-strings](pages/urd-step-strings.md)]) recasts the castle rules as a [[generalized-dyck-grammar](pages/generalized-dyck-grammar.md)], from which the [[castle-counting-formula](pages/castle-counting-formula.md)] follows: an unsigned tower count `T(k,L) = (k+1)^L`, a signed count `P` that encodes the even-block rule as a −1 weight per block, and `F(w,h) = [h^w − (h−1)^w − P(h−1,w) + P(h−2,w)]/2`. This reproduces all three integer checkpoints (verified by executing the source's Python). The enumeration side is organized around the [[convex-castle](pages/convex-castle.md)] class (counted by `C(2H+W−3, W−1)`) and its variations.

## Open Questions

- How does the count of *all* castles (both parities) relate to the even-only count `F(w,h)` that PE 502 asks for? The [[castle-counting-formula](pages/castle-counting-formula.md)] already exposes both halves — the unsigned count `T` (all parities) and the signed `P` — so this is now a matter of reading off the general problem rather than an open derivation.
- What are the precise connections between castles and the related combinatorial objects the source links but this wiki has not yet ingested: polyominoes, Dyck words, and lattice paths? The [[generalized-dyck-grammar](pages/generalized-dyck-grammar.md)] makes the Dyck connection concrete (a first-return split with a nested interior tower).
- What does the *code* actually compute, versus the derivation? The representations subpage notes the winning solution enumerates none of these encodings directly — the Implementation Notes and Solution subpages (not yet ingested) hold that.

## Key Entities / Concepts

- [[castle-polyomino](pages/castle-polyomino.md)] — the central object: a valid stacked-block configuration on a grid, at any block parity.
- [[castle-counting-function](pages/castle-counting-function.md)] — `F(w,h)`, the number of castles; PE 502's even-block count is a special case.
- [[castle-counting-formula](pages/castle-counting-formula.md)] — the closed form for `F(w,h)`, derived and verified.
- [[castle-representations](pages/castle-representations.md)] — the three exact encodings of a castle.
- [[convex-castle](pages/convex-castle.md)] — the structural backbone of the enumeration.
- [[generalized-dyck-grammar](pages/generalized-dyck-grammar.md)] — the grammar linking castles to Dyck paths and yielding the count.
- [[generating-functions](pages/generating-functions.md)] — the method: a polynomial whose coefficients are the counts.
