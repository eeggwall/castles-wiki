---
title: Overview
tags: [overview, synthesis]
sources: [project-euler-502]
updated: 2026-09-13
---

# Project Euler 502 — Overview

> Evolving synthesis of everything in the wiki. Updated by wiki-ingest when sources shift the understanding.

## Current Understanding

The wiki studies **castles**: configurations of stacked integer-length, unit-height *blocks* on a *w*×*h* grid, obeying a fixed set of placement rules (no overhangs or floating blocks, grid-snapped, ≥1 unit gap between same-row neighbors, a full-width bottom row, and a maximum height of exactly *h*). See [[castle-polyomino](pages/castle-polyomino.md)].

The general object of interest is the castle at **any** block count. [[project-euler-502](pages/project-euler-502.md)] studies a special case: its counting function [[castle-counting-function](pages/castle-counting-function.md)] `F(w,h)` counts only castles with an **even** number of blocks, and asks for `(F(10^12,100) + F(10000,10000) + F(100,10^12)) mod 1,000,000,007`. This wiki treats the even-block parity restriction as a special case of the broader, more interesting problem of counting all castles regardless of parity.

## Open Questions

- How does the count of *all* castles (both parities) relate to the even-only count `F(w,h)` that PE 502 asks for? What is the general (parity-agnostic) counting problem, and what makes the even restriction the interesting special case?
- What are the precise connections between castles and the related combinatorial objects the source links but this wiki has not yet ingested: polyominoes, Dyck words, lattice paths, and generating functions?

## Key Entities / Concepts

- [[castle-polyomino](pages/castle-polyomino.md)] — the central object: a valid stacked-block configuration on a grid, at any block parity.
- [[castle-counting-function](pages/castle-counting-function.md)] — `F(w,h)`, the number of castles; PE 502's even-block count is a special case.
