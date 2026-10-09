---
title: Narayana numbers
category: Concepts
summary: N(n,k) = (1/n)C(n,k)C(n,k−1) (OEIS A001263); the Narayana polynomial is the numerator of the tower block-count generating function — where the castle's Catalan/Narayana thread actually lives.
tags: [concept, narayana, catalan, oeis, tower, generating-functions]
sources: [oeis-mining-pe502, tower-narayana-polynomial, algebraic-languages-and-polyominoes-enumeration, bayer-diaconis-1992-dovetail-shuffle]
created: 2026-09-13
updated: 2026-10-08
---

# Narayana numbers

## Description

The **Narayana numbers** `N(n,k) = (1/n) C(n,k) C(n,k−1)` form the triangle Online Encyclopedia of Integer Sequences (OEIS) **A001263** (`1; 1,1; 1,3,1; 1,6,6,1; 1,10,20,10,1; …`), a refinement of the [[catalan-numbers](pages/catalan-numbers.md)] (`∑_k N(n,k) = C_n`, verified). They count, among many things, Dyck paths by number of peaks, and parallelogram polyominoes of perimeter `2n+2` by width `k`. Delest and Viennot connect these two counts through their bijection β, which sends peaks to columns ([[parallelogram-polyomino-dyck-bijection](pages/parallelogram-polyomino-dyck-bijection.md)]).[^4]

## The castle connection lives in the tower count

The [[oeis-mining-pe502](pages/oeis-mining-pe502.md)] pass established that the Catalan/Narayana thread does **not** appear in the convex-castle count (that is binomial — see [[convex-castle-binomial-identity](pages/convex-castle-binomial-identity.md)]); it appears instead in the block-count generating function of the **[[tower-heap](pages/tower-heap.md)]** (a Viennot heap of unit-height segments). The number of towers of width *w* with *b* blocks is[^1]

```
T(w,b) = Σ_{k=1..w} N(w,k) · C(b + w − k, w − 1),
   GF by b:  ( Σ_k N(w,k) x^{k−1} ) / (1 − x)^w   =  Narayana_w(x) / (1−x)^w
```

i.e. the **Narayana polynomial** `Narayana_w(x)` is the numerator. Verified for `w = 1..7`. The width rows land on existing OEIS entries — `A005408` (w=2), `A005891` (w=3), `A063490` (w=4), `A160747` (w=5) — with `w ≥ 6` new (see [[tower-narayana-polynomial](pages/tower-narayana-polynomial.md)]).[^2]

A proposed cross-reference on A001263 records `T(w,b) = Σ_k N(w,k) C(b+w−k, w−1)` as a generating-function identity: the Narayana polynomial is the numerator of the tower block-count GF. A peaks refinement was tested and does not factor it.[^3]

**What `k` counts.** Peaks do not factor the identity, but descents do. `k - 1` is the number of **descents** of the height sequence (positions `i` with `c_i > c_{i+1}`): towers of width `w` with `b` blocks and `k - 1` descents number exactly `N(w,k) C(b+w-k, w-1)`. By the reversal symmetry, ascents give the same distribution. This is verified by brute force over all height vectors for `w ≤ 7`, `b ≤ 7`, and unproved on the wiki. One reading (own reasoning) is that `Narayana_w(x)/(1-x)^w` has the "h-polynomial over `(1-x)^w`" shape, with descents in the role they play for Eulerian numbers in Worpitzky's identity. Bayer and Diaconis prove Worpitzky's identity by stars and bars: a permutation with `r` rising sequences comes from `C(a + n − r, n)` cuts of an `n`-card deck into `a` packets, since `r − 1` cuts are forced and the `a − r` spare cuts fall into `n + 1` gaps.[^5] Under `a = b + 1`, `n = w − 1`, `r = k` that binomial is `C(b+w-k, w-1)` ([[bayer-diaconis-1992-dovetail-shuffle](pages/bayer-diaconis-1992-dovetail-shuffle.md)] §"The castle reading"). Through Delest-Viennot's β, the same `N(w,k)` counts width-`k` parallelogram polyominoes of semi-perimeter `w+1` ([[parallelogram-polyomino-dyck-bijection](pages/parallelogram-polyomino-dyck-bijection.md)]). The counts therefore suggest a structural bijection from towers with `k-1` descents to pairs (width-`k` parallelogram, weak composition of `b-k+1` into `w` parts); none is constructed. Re-indexed by semi-perimeter, the identity is the bargraph triangle A271942 ([[castle-perimeter](pages/castle-perimeter.md)]).

## Appearances in Sources

- [[tower-narayana-polynomial](pages/tower-narayana-polynomial.md)] — the full finding and the A001263 cross-reference draft.
- [[oeis-mining-pe502](pages/oeis-mining-pe502.md)] — identifies this as the Catalan/Narayana thread (tower, not convex).
- [[bayer-diaconis-1992-dovetail-shuffle](pages/bayer-diaconis-1992-dovetail-shuffle.md)] - Worpitzky's identity proved by stars and bars over the cuts of a shuffle, the model for the descent refinement.
- [[algebraic-languages-and-polyominoes-enumeration](pages/algebraic-languages-and-polyominoes-enumeration.md)] - Remark 4.4: parallelogram polyominoes by width are Narayana, by a 2 × 2 Gessel-Viennot determinant, and β carries this to Dyck words by peaks.

## Related Concepts

- [[tower-heap](pages/tower-heap.md)] — the heap-of-pieces object whose block-count Narayana governs.
- [[catalan-numbers](pages/catalan-numbers.md)] — the sequence Narayana refines (`∑_k N(n,k) = C_n`).
- [[convex-castle-binomial-identity](pages/convex-castle-binomial-identity.md)] — why the *convex* count is binomial, not Narayana.
- [[generating-functions](pages/generating-functions.md)] — the tool the identity is stated in.
- [[parallelogram-polyomino-dyck-bijection](pages/parallelogram-polyomino-dyck-bijection.md)] - width = number of peaks, the bijective Narayana.

## Footnotes

[^1]: [[tower-narayana-polynomial](pages/tower-narayana-polynomial.md)] `crosslink-avenues.md` §"Tier 2" L43-47 — "T(w,b) = # towers of width w with exactly b blocks = sum_{k=1..w} Narayana(w,k) * C(b + w − k, w − 1) ... GF = (Narayana_w(x)) / (1 − x)^w ... Narayana(w,k) = (1/w) C(w,k) C(w,k−1) = A001263."
[^2]: [[tower-narayana-polynomial](pages/tower-narayana-polynomial.md)] `crosslink-avenues.md` §"Tier 2" L49-56 — the width-row table hitting A005408 (w=2), A005891 (w=3), A063490 (w=4), A160747 (w=5), "new" for w=6,7.
[^3]: `raw/oeis-pe502/xrefs/A001263-tower.md` §"Identity (verified)" L23-25 — "It is a generating-function identity, not a 'peaks' bijection: a direct peaks refinement was tested and does not factor this way, so do not state a peaks interpretation."
[^4]: [[algebraic-languages-and-polyominoes-enumeration](pages/algebraic-languages-and-polyominoes-enumeration.md)] p.184 Remark 4.4 - "the number b_{n,k} of parallelogram polyominoes with perimeter 2n+2 and width k is given by the 2 × 2 determinant ... This determinant is equal to (1/n)C(n,k)C(n,k-1) and using Proposition 4.1, we deduce the well-known formula for the number of Dyck words of length 2n having k peaks."
[^5]: [[bayer-diaconis-1992-dovetail-shuffle](pages/bayer-diaconis-1992-dovetail-shuffle.md)] §3 proof of Theorem 3 p.301 L452-L463, p.302 L497-L505 [synthesis] - "the n cards form dividers creating n + 1 bins, into which the a - r spare cuts are allocated", giving `C(a + n − r, n)` for a permutation with `r` rising sequences; summed over permutations this is Worpitzky's identity.
