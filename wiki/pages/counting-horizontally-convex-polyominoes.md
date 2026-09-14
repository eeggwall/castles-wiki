---
title: "Counting Horizontally Convex Polyominoes (Hickerson 1999)"
category: Sources
summary: Hickerson's 1-dimensional proof that horizontally convex n-ominoes satisfy a(n)=5a(n−1)−7a(n−2)+4a(n−3), via four auxiliary restricted-shape counts — a template for castle-style recurrences.
tags: [paper, polyomino, horizontally-convex, linear-recurrence, combinatorics, source]
sources: [counting-horizontally-convex-polyominoes]
created: 2026-09-13
updated: 2026-09-13
---

# Counting Horizontally Convex Polyominoes (Hickerson 1999)

**Source:** `assets/PolyominoTransferMatrix.pdf` (Dean Hickerson, *Counting Horizontally Convex Polyominoes*, Journal of Integer Sequences, Vol. 2 (1999), Article 99.1.8; mirror: `cs.uwaterloo.ca/journals/JIS/HICK2/chcp.html`)
**Date ingested:** 2026-09-13
**Type:** paper (PDF, 6 pp.)

## Summary

A **polyomino** is a finite edge-connected union of unit squares with integer-coordinate vertices (an *n*-omino has area *n*), counted up to translation. A polyomino is **horizontally convex** (an HC-polyomino) if every horizontal line meets it in a single segment or not at all.[^1] Let `a(n)` count HC *n*-ominoes; the sequence is `1, 2, 6, 19, 61, 196, 629, 2017, 6466, 20727, 66441, 212980, …` (OEIS **A001169**).[^2]

The paper's result is that `a(n)` satisfies a third-order linear recurrence — remarkable for a 2-D counting problem:[^2]

```
a(n) = 5 a(n−1) − 7 a(n−2) + 4 a(n−3),    n ≥ 5
```

with growth `a(n) ~ u·v^n`, where `v = 3.2055694304…` is the unique real root of `v³ − 5v² + 7v − 4 = 0` and `u = (163 − 129v + 41v²)/944 = 0.1809155018…`.[^3] The recurrence was apparently first proved by Pólya (1938, unpublished); prior published proofs are "2-dimensional," introducing `a(r,n)` (HC *n*-ominoes with exactly *r* top-row squares) and the relation `a(r,n) = ∑_{s} (r+s−1) a(s,n−r)`.[^4]

Hickerson's contribution is a **1-dimensional proof**: introduce four auxiliary functions `b,c,d,e(n)` counting restricted HC *n*-ominoes (by top-row width and alignment of the top square over the second/third rows), find linear relations among them by add/delete-a-square bijections, and combine to eliminate them — leaving the recurrence in `a` alone.[^5] Each of `b,c,d,e` turns out to be a fixed linear combination of `a(n),a(n−1),a(n−2)` (e.g. `e(n)=a(n)−3a(n−1)`), so all satisfy the same recurrence.[^6]

## Why it matters for PE 502

The relevance is structural and runs along several threads this wiki is chasing:

- **Restricted-shape auxiliary counts to force a recurrence.** Hickerson's method — introduce restricted-configuration counting functions, relate them by adding/removing cells, and eliminate — is exactly the shape of the castle argument, where restricted counts (the [[convex-castle](pages/convex-castle.md)], the unsigned `T` and signed `P` towers) combine into the [[castle-counting-formula](pages/castle-counting-formula.md)]. The failed "U/R/D convex-castle variation enumeration" thread on [[project-euler-502-solution](pages/project-euler-502-solution.md)] is an attempt at this same style that did not close; Hickerson shows the style *can* close for a neighboring convexity class.
- **Horizontal convexity vs. the castle's convexity.** An HC-polyomino's "single horizontal segment per row" is a different convexity from the castle's [[convex-castle](pages/convex-castle.md)] (monotone-up-then-down skyline). Comparing the two is a direct connection to the broader column/row-convex polyomino literature (see [[column-convex-polygon-enumeration](pages/column-convex-polygon-enumeration.md)]).
- **A linear recurrence with a small transfer/companion structure.** That a 2-D family collapses to an order-3 recurrence is the same phenomenon the castle solution exploits: `P(k,L)` is linear-recurrent in each direction, evaluated by [[kitamasa](pages/kitamasa.md)] / [[berlekamp-massey](pages/berlekamp-massey.md)]. The characteristic polynomial `v³−5v²+7v−4` is the HC analogue of the castle recurrences' characteristic polynomials.

## Key Takeaways

- HC *n*-ominoes (`A001169`): `a(n) = 5a(n−1) − 7a(n−2) + 4a(n−3)` for `n ≥ 5` — verified here against the tabulated values `a(1..12)`.[^2]
- Growth `a(n) ~ u·v^n`, `v = 3.2055694304…` the real root of `v³−5v²+7v−4`, verified.[^3]
- Method: four auxiliary restricted-shape counts `b,c,d,e` related by cell add/delete bijections, then eliminated — a 1-D alternative to the standard `a(r,n)` 2-D generating-function proofs.[^5]
- Each auxiliary is a linear combination of `a(n),a(n−1),a(n−2)` (e.g. `c(n)=a(n)−4a(n−1)+4a(n−2)`, `e(n)=a(n)−3a(n−1)`), verified against the table.[^6]

## Entities & Concepts

- [[horizontally-convex-polyomino](pages/horizontally-convex-polyomino.md)] — the object counted; a convexity notion to compare with the castle's.
- [[convex-castle](pages/convex-castle.md)] — the castle's own convexity class, whose variation-enumeration did not close.
- [[column-convex-polygon-enumeration](pages/column-convex-polygon-enumeration.md)], [[kitamasa](pages/kitamasa.md)], [[berlekamp-massey](pages/berlekamp-massey.md)] — related threads.

## Relation to Other Wiki Pages

Cited as a reference on [[project-euler-502-solution](pages/project-euler-502-solution.md)]. It is a worked instance of the restricted-count-elimination method that the castle solution uses, applied to a neighboring convexity class, and an entry point into the polyomino-convexity literature.

## Footnotes

[^1]: [[counting-horizontally-convex-polyominoes](pages/counting-horizontally-convex-polyominoes.md)] p.1 §0 — "A finite union of closed unit squares whose vertices have integer coordinates is called a polyomino if its interior is connected ... A polyomino P is horizontally convex if each horizontal line meets P in a single line segment, or not at all."
[^2]: `assets/PolyominoTransferMatrix.pdf` p.1 §0 — table "a(n) 1 2 6 19 61 196 629 2017 6466 20727 66441 212980" and "Theorem: For n ≥ 5, a(n) = 5 a(n-1) - 7 a(n-2) + 4 a(n-3)"; recurrence re-verified against a(1..12) during ingest (holds for n=5..12); OEIS A001169.
[^3]: `assets/PolyominoTransferMatrix.pdf` p.2 §0 — "v = 3.2055694304... is the unique real root of v^3 - 5 v^2 + 7 v - 4 = 0 ... u = (163 - 129 v + 41 v^2)/944 = 0.1809155018..."; real root re-verified numerically during ingest.
[^4]: `assets/PolyominoTransferMatrix.pdf` p.2 §0 — "first proved by Pólya in 1938 ... the function a(r,n), which is the number of horizontally convex n-ominoes with exactly r squares in the top row ... a(r,n) = SUM (r+s-1) a(s,n-r)."
[^5]: `assets/PolyominoTransferMatrix.pdf` p.2-4 §1 — "the proof given here is 1-dimensional: We introduce 4 new functions of n ... find linear relations among these functions and combine them to obtain the recurrence" with Lemmas 0-4 (b, c, d, e definitions and the add/delete-square bijections).
[^6]: `assets/PolyominoTransferMatrix.pdf` p.5 §2 — "b(n) = 3 a(n-1) - 4 a(n-2) ... c(n) = a(n) - 4 a(n-1) + 4 a(n-2) ... d(n) = 2 a(n-1) - 4 a(n-2) ... e(n) = a(n) - 3 a(n-1)"; each re-verified against the n=6 table row during ingest.
