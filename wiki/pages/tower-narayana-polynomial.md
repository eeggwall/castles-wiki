---
title: "Tower block-count = Narayana polynomial"
category: Sources
summary: The tower (heap-of-pieces) block-count GF is Narayana_w(x)/(1−x)^w; width rows are A005408/A005891/A063490/A160747 (w≥6 new) — the Catalan/Narayana thread, living in the tower not the convex count.
tags: [oeis, tower, narayana, heap-of-pieces, generating-functions, cross-reference, source]
sources: [tower-narayana-polynomial]
created: 2026-09-13
updated: 2026-09-22
---

# Tower block-count = Narayana polynomial

**Source:** `~/code/oeis/pe502/crosslink-avenues.md` §"Tier 2" and `xrefs/A001263-tower.md` (+ `A005408/A005891/A063490/A160747-tower.md`), copied to `raw/oeis-pe502/`
**Date ingested:** 2026-09-13
**Type:** verified OEIS finding (Python `tower.py`; draft cross-references)

## Summary

This is the **Catalan/Narayana connection** the parent plan hoped for — and it lives in the [[tower-heap](pages/tower-heap.md)] block-count, not in the convex-castle count (which is binomial, see [[convex-castle-binomial-identity](pages/convex-castle-binomial-identity.md)]). A tower of width *w* is a Viennot heap of unit-height segments (column heights `c_1..c_w ≥ 0`, blocks = maximal runs). Counting towers by number of blocks, verified for `w = 1..7` against brute force:[^1]

```
T(w,b) = Σ_{k=1..w} N(w,k) · C(b + w − k, w − 1),
   GF by b:  Narayana_w(x) / (1 − x)^w,   Narayana_w(x) = Σ_k N(w,k) x^{k−1}
```

with `N(w,k) = (1/w)C(w,k)C(w,k−1)` the [[narayana-numbers](pages/narayana-numbers.md)] (A001263). The **Narayana polynomial** is exactly the numerator of the tower block-count generating function.

The width rows land on existing OEIS entries:[^2]

| width *w* | `T(w,b)`, `b = 0,1,2,3,…` | OEIS |
|---|---|---|
| 2 | 1, 3, 5, 7, 9, 11, … | **A005408** (odd numbers) |
| 3 | 1, 6, 16, 31, 51, 76, … | **A005891** (centered pentagonal) |
| 4 | 1, 10, 40, 105, 219, 396, … | **A063490** |
| 5 | 1, 15, 85, 295, 771, 1681, … | **A160747** |
| 6 | 1, 21, 161, 721, 2331, 6083, … | **new** |
| 7 | 1, 28, 280, 1582, 6244, 19348, … | **new** |

**Offset note:** **A063490 is offset 1** (`a(n) = T(4, n−1)`) — the only width-row entry with a shift; A005408/A005891/A160747 are offset 0. Per the phase-2 plan, **A005408 is skipped by default** (densest entry, weakest of the set), and the submission order is A160747 → A005891 → A063490 → A001263.

## Cross-reference actions

- **A005408, A005891, A063490, A160747** — add the heap/tower interpretation ("also the number of towers of unit-height segments on *w* columns with *n* blocks") plus the Narayana-polynomial formula. Drafts in `raw/oeis-pe502/xrefs/A005408-tower.md` etc.[^2]
- **A001263** (Narayana) — add a Formula: the tower block-count GF has the Narayana polynomial as numerator, `T(w,b) = Σ_k N(w,k) C(b+w−k, w−1)`. Stated as a generating-function identity, **not** a peaks bijection — a direct peaks refinement was tested and does not factor this way.[^3]
- **Generation:** the `w ≥ 6` tower rows are new sequences (new rows of the Narayana-polynomial triangle).[^2]

Per [[oeis-cross-referencing](pages/oeis-cross-referencing.md)] these are draft cross-references (human authorship required), kept in `raw/oeis-pe502/xrefs/`. This is the "tier 2" submission bundle.

## Key Takeaways

- Tower block-count GF `= Narayana_w(x)/(1−x)^w`; `T(w,b) = Σ_k N(w,k) C(b+w−k, w−1)`, verified `w=1..7`.[^1]
- Width rows: A005408, A005891, A063490, A160747 (w=2..5); new for w≥6.[^2]
- **This — not the convex count — is where Catalan/Narayana enters the castle world**, via the heap-of-pieces tower.[^1]
- The A001263 link is a generating-function identity, explicitly not a peaks bijection.[^3] The refinement that does factor it is by **descents**: towers with `k-1` descents number `N(w,k) C(b+w-k, w-1)` (brute-force verified `w, b ≤ 7`, second Delest-Viennot pass; see [[narayana-numbers](pages/narayana-numbers.md)]).
- Re-indexed by semi-perimeter `s = w + blocks` (a castle's semi-perimeter, [[castle-perimeter](pages/castle-perimeter.md)]), castles by `(s, w)` are the bargraph triangle A271942, and by `s` alone A082582.

## Entities & Concepts

- [[tower-heap](pages/tower-heap.md)] — the object being counted.
- [[narayana-numbers](pages/narayana-numbers.md)] — A001263, the GF numerator.
- [[convex-castle-binomial-identity](pages/convex-castle-binomial-identity.md)] — the contrast: convex count is binomial, not Narayana.

## Relation to Other Wiki Pages

Resolves the "where is Catalan?" question the wiki has carried since [[project-euler-502-representations](pages/project-euler-502-representations.md)]: the Dyck-shape analogy of the [[generalized-dyck-grammar](pages/generalized-dyck-grammar.md)] does connect to Narayana/Catalan — through the tower block-count, giving four existing OEIS entries a heap interpretation and opening the Viennot heap-theory thread.

The Narayana-polynomial GF `Narayana_w(x) / (1 - x)^w` for the block-count distribution is the analytical origin of the marginal entropy `H(B)` used on [[castle-conditional-entropy](pages/castle-conditional-entropy.md)]: taking its `w -> infty` limit gives a distribution with mean and variance both linear in `w`, so `H(B) ~ (1/2) log_2 w + const`, matching the brute-force conditional-entropy table on castles.

## Footnotes

[^1]: [[tower-narayana-polynomial](pages/tower-narayana-polynomial.md)] `crosslink-avenues.md` §"Tier 2" L36-47 — "T(w,b) = # towers of width w with exactly b blocks = sum_{k=1..w} Narayana(w,k) * C(b + w − k, w − 1) ... GF = (Narayana_w(x)) / (1 − x)^w ... verified for w = 1..7 against brute force ... Narayana(w,k) = ... = A001263."
[^2]: [[tower-narayana-polynomial](pages/tower-narayana-polynomial.md)] `crosslink-avenues.md` §"Tier 2" L49-63 — the width-row table (A005408/A005891/A063490/A160747; new for w=6,7) and the cross-link actions "add the heap/tower interpretation ... plus the Narayana-polynomial formula."
[^3]: [[tower-narayana-polynomial](pages/tower-narayana-polynomial.md)] `xrefs/A001263-tower.md` §"Identity" — "It is a generating-function identity, not a 'peaks' bijection: a direct peaks refinement was tested and does not factor this way, so do not state a peaks interpretation."
