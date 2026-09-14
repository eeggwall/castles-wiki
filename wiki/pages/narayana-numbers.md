---
title: Narayana numbers
category: Concepts
summary: N(n,k) = (1/n)C(n,k)C(n,k−1) (OEIS A001263); the Narayana polynomial is the numerator of the tower block-count generating function — where the castle's Catalan/Narayana thread actually lives.
tags: [concept, narayana, catalan, oeis, tower, generating-functions]
sources: [oeis-mining-pe502, tower-narayana-polynomial]
created: 2026-09-13
updated: 2026-09-13
---

# Narayana numbers

## Description

The **Narayana numbers** `N(n,k) = (1/n) C(n,k) C(n,k−1)` form the triangle OEIS **A001263** (`1; 1,1; 1,3,1; 1,6,6,1; 1,10,20,10,1; …`), a refinement of the [[catalan-numbers](pages/catalan-numbers.md)] (`∑_k N(n,k) = C_n`, verified). They count, among many things, Dyck paths by number of peaks. They are the classical Catalan/Narayana object the parent plan hoped the castle problem would touch.

## The castle connection lives in the tower count

The [[oeis-mining-pe502](pages/oeis-mining-pe502.md)] pass established that the Catalan/Narayana thread does **not** appear in the convex-castle count (that is binomial — see [[convex-castle-binomial-identity](pages/convex-castle-binomial-identity.md)]); it appears instead in the block-count generating function of the **[[tower-heap](pages/tower-heap.md)]** (a Viennot heap of unit-height segments). The number of towers of width *w* with *b* blocks is[^1]

```
T(w,b) = Σ_{k=1..w} N(w,k) · C(b + w − k, w − 1),
   g.f. by b:  ( Σ_k N(w,k) x^{k−1} ) / (1 − x)^w   =  Narayana_w(x) / (1−x)^w
```

i.e. the **Narayana polynomial** `Narayana_w(x)` is the numerator. Verified for `w = 1..7`. The width rows land on existing OEIS entries — `A005408` (w=2), `A005891` (w=3), `A063490` (w=4), `A160747` (w=5) — with `w ≥ 6` new (see [[tower-narayana-polynomial](pages/tower-narayana-polynomial.md)]).[^2]

A proposed cross-reference on A001263 itself records this: `T(w,b) = Σ_k N(w,k) C(b+w−k, w−1)` — the Narayana polynomial as the numerator of the tower block-count g.f. (stated as a generating-function identity, **not** a peaks bijection, which was tested and does not factor this way).[^3]

## Appearances in Sources

- [[tower-narayana-polynomial](pages/tower-narayana-polynomial.md)] — the full finding and the A001263 cross-reference draft.
- [[oeis-mining-pe502](pages/oeis-mining-pe502.md)] — identifies this as the Catalan/Narayana thread (tower, not convex).

## Related Concepts

- [[tower-heap](pages/tower-heap.md)] — the heap-of-pieces object whose block-count Narayana governs.
- [[catalan-numbers](pages/catalan-numbers.md)] — the sequence Narayana refines (`∑_k N(n,k) = C_n`).
- [[convex-castle-binomial-identity](pages/convex-castle-binomial-identity.md)] — why the *convex* count is binomial, not Narayana.
- [[generating-functions](pages/generating-functions.md)] — the tool the identity is stated in.

## Footnotes

[^1]: [[tower-narayana-polynomial](pages/tower-narayana-polynomial.md)] `crosslink-avenues.md` §"Tier 2" L43-47 — "T(w,b) = # towers of width w with exactly b blocks = sum_{k=1..w} Narayana(w,k) * C(b + w − k, w − 1) ... g.f. = (Narayana_w(x)) / (1 − x)^w ... Narayana(w,k) = (1/w) C(w,k) C(w,k−1) = A001263."
[^2]: [[tower-narayana-polynomial](pages/tower-narayana-polynomial.md)] `crosslink-avenues.md` §"Tier 2" L49-56 — the width-row table hitting A005408 (w=2), A005891 (w=3), A063490 (w=4), A160747 (w=5), "new" for w=6,7.
[^3]: [[tower-narayana-polynomial](pages/tower-narayana-polynomial.md)] `xrefs/A001263-tower.md` §"Identity" — "It is a generating-function identity, not a 'peaks' bijection: a direct peaks refinement was tested and does not factor this way, so do not state a peaks interpretation."
