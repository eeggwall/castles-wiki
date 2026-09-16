---
title: "Castle Types (charlesreid1.com)"
category: Sources
summary: The charlesreid1.com catalog of castle types — 7 "base" types drawn from the polyomino literature (column-convex, unimodal, directed, parallelogram, Ferrers, staircase, m-disparate) plus 35 proposed additional types, all as further restrictions on the skyline `c_1, …, c_w`.
tags: [castle, taxonomy, classification, skyline, polyomino, source]
sources: [castle-types]
created: 2026-09-15
updated: 2026-09-15
---

# Castle Types (charlesreid1.com)

**Source:** https://charlesreid1.com/wiki/Project_Euler/502/Castle_Types (raw wikitext cached at `raw/castle-types.wiki`, fetched 2026-09-15)
**Date ingested:** 2026-09-15
**Type:** article (MediaWiki topic page)

## Summary

The page states the framing this wiki adopts for classifying castles: **a castle is determined by its skyline** — the sequence of column heights `c_1, c_2, …, c_w` with `1 ≤ c_i ≤ h` and `max_i c_i = h` — and every castle is automatically column-convex and bottom-aligned by construction, so each "castle type" is a **further restriction on the skyline**.[^1] The parity constraint of PE 502 (even total blocks) is orthogonal to the types listed here — types either ignore it, or re-impose it independently.[^1]

The catalog is organized in two blocks:

- **Base types** (7 entries) — drawn from the established polyomino / composition literature (column-convex, unimodal, Ferrers, staircase, parallelogram, directed, m-disparate).[^2]
- **Proposed additional types** (35 entries) — new candidate classes defined here for the first time or aggregated from adjacent literature: convex (row-convex), reverse Ferrers, strictly unimodal, bimodal, k-modal, anti-unimodal, plateau-free, m-smooth, zigzag, alternating parity, palindromic, centrally symmetric, Dyck-path, Motzkin-path, flat-top, single-summit, even-area, even-peak, equal-block, two-level, self-conjugate, crenellated, moated, rainbow, hook, twin-peak, single-valley, fence-post, linear, convex-skyline, concave-skyline, triangular-area, prime-top, integer-mean, boxcastle.[^3]

Together the 37 types form a **classification framework** for castle sub-families. Many of them correspond directly to wiki threads that were previously scattered:

- **Unimodal** = the [[convex-castle](pages/convex-castle.md)] the [[convex-castle-binomial-identity](pages/convex-castle-binomial-identity.md)] counts.
- **Ferrers, parallelogram, directed, staircase** = the "classical directed-and-convex families" already tracked on [[column-convex-polygon-enumeration](pages/column-convex-polygon-enumeration.md)] and [[polyominoes](pages/polyominoes.md)], and (for Ferrers, by area) the [[q-catalan-numbers](pages/q-catalan-numbers.md)] connection on [[polyominoes](pages/polyominoes.md)].
- **Convex (row-convex)** = the front/middle/back U/R/D form on [[project-euler-502-representations](pages/project-euler-502-representations.md)]; combined with the automatic column-convexity, this is genuine convex-polyomino territory.
- **Dyck-path, Motzkin-path** = the run-constrained tower skyline of [[tower-word-continued-fraction](pages/tower-word-continued-fraction.md)] (peakless-valleyless Motzkin, A004149).
- **k-modal** = a natural refinement of the unimodal / [[stack-polyomino-gf](pages/stack-polyomino-gf.md)] count by number of local maxima.
- **m-disparate, m-smooth** = complementary rate-of-change restrictions; the height-2 castle strip's `|c_{i+1} − c_i| ≤ 1` is exactly the m-smooth condition at `m = 1`.

The page ends by opening the classification to further contributions rather than closing it — its 35 proposed types are a starter set, not a taxonomy claim.[^3]

## Key Takeaways

- **The skyline is the classifying object.** Every castle is column-convex and bottom-aligned already; types are further restrictions on `(c_1, …, c_w)`.[^1]
- **Base types come from the polyomino literature.** Column-convex, unimodal, Ferrers, staircase, parallelogram, directed, m-disparate — each already ingested or referenced on the wiki.[^2]
- **35 proposed additional types** organize sub-families the wiki was already tracking piecemeal, plus new candidates (crenellated, moated, hook, twin-peak, rainbow, palindromic, self-conjugate, …).[^3]
- **Parity is orthogonal.** PE 502's even-block constraint is applied independently of the type.[^1]

## Entities & Concepts

- [[castle-classification](pages/castle-classification.md)] — the concept page this ingest anchors: the classification framework that ties the 37 types to existing wiki threads and to the [[metallic-means](pages/metallic-means.md)] axis.
- [[castle-polyomino](pages/castle-polyomino.md)] / [[castle-representations](pages/castle-representations.md)] — the object and its encodings; the skyline `c_1,…,c_w` is the integer-tuple encoding.
- [[convex-castle](pages/convex-castle.md)] — the unimodal type, whose count is [[convex-castle-binomial-identity](pages/convex-castle-binomial-identity.md)].
- [[polyominoes](pages/polyominoes.md)] / [[column-convex-polyomino](pages/column-convex-polyomino.md)] / [[column-convex-polygon-enumeration](pages/column-convex-polygon-enumeration.md)] — the base-type home literature.
- [[stack-polyomino-gf](pages/stack-polyomino-gf.md)] — the unimodal-skyline sub-family from AC Ex. I.8.
- [[tower-word-continued-fraction](pages/tower-word-continued-fraction.md)] — the Dyck-path / Motzkin-path types.
- [[metallic-means](pages/metallic-means.md)] — the growth-constant classification axis the width-1/width-2 atom decomposition suggests.

## Relation to Other Wiki Pages

Filling the "Taxonomy of castle classes" open thread that has been on `IDEAS.md` since inception. This source page catalogs 42 castle types (7 base, 35 proposed) that the [[castle-classification](pages/castle-classification.md)] concept page organizes into a framework — tying each type back to the wiki thread that already touches it, and identifying which types have counts, which have candidate counts, and which are open.

## Footnotes

[^1]: [[castle-types](pages/castle-types.md)] §"(lead)" L1-L9 — "A castle on a w × h grid is determined by its skyline, the sequence of column heights c_1, c_2, …, c_w with 1 ≤ c_i ≤ h and max_i c_i = h. (Problem 502 also requires an even number of blocks; the types below mostly ignore, or independently re-impose, that parity rule.) Every castle is automatically column-convex and bottom-aligned, so each type is a further restriction on the skyline."
[^2]: [[castle-types](pages/castle-types.md)] §"Base types" L11-L19 — the 7 base types: column-convex, unimodal (`c_1 ≤ … ≤ c_p ≥ … ≥ c_w`), directed (every cell reachable from bottom-left by east/north path), parallelogram (perpendicular-to-main-diagonal sections are connected), Ferrers (`c_1 ≥ … ≥ c_w`), staircase (Ferrers with strict inequality — all distinct heights), m-disparate (`|c_{i+1} − c_i| ≥ m`).
[^3]: [[castle-types](pages/castle-types.md)] §"Proposed additional types" L21-L57 — the 35 proposed types, numbered 1-35: convex/row-convex, reverse Ferrers, strictly unimodal, bimodal, k-modal, anti-unimodal (V-shaped), plateau-free, m-smooth (Lipschitz), zigzag, alternating parity, palindromic, centrally symmetric, Dyck-path, Motzkin-path, flat-top, single-summit, even-area, even-peak, equal-block, two-level, self-conjugate, crenellated, moated, rainbow, hook, twin-peak, single-valley, fence-post, linear, convex-skyline (second differences ≥ 0), concave-skyline (≤ 0), triangular-area, prime-top, integer-mean, boxcastle.
