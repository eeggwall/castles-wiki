---
title: Tower (heap of pieces)
category: Concepts
summary: A tower is a castle without the full-base / max-height / parity rules — column heights c_1..c_w ≥ 0, a Viennot heap of unit-height segments; its block-count GF is a Narayana polynomial over (1−x)^w.
tags: [concept, tower, heap-of-pieces, viennot, narayana, castle]
sources: [oeis-mining-pe502, tower-narayana-polynomial, project-euler-502-representations]
created: 2026-09-13
updated: 2026-09-23
---

# Tower (heap of pieces)

## Description

A **tower** is the castle's underlying object with the boundary rules stripped away: column heights `c_1, …, c_w ≥ 0` (no mandatory full-width bottom block, no exact-max-height constraint, no parity filter), with blocks the maximal horizontal runs, `#blocks = c_1 + ∑_{i≥2} max(0, c_i − c_{i−1})`.[^1] It is precisely **Viennot's "heap of pieces"**: unit-height segments stacked on *w* columns, each resting on the floor or the segment directly below, segments in the same row separated by a gap.[^2]

Towers are the scaffolding of the castle solution — the [[castle-counting-formula](pages/castle-counting-formula.md)] counts towers above the bottom block, and the [[generalized-dyck-grammar](pages/generalized-dyck-grammar.md)] is a grammar over tower words. This page treats the tower as an object in its own right, because that is where the Online Encyclopedia of Integer Sequences (OEIS) mining found its richest external connection.

## Heap presentation and cell count

Presented as a Viennot heap, the tower's piece basis is one piece per column, `B = {u_1, …, u_w}` with `u_i =` "place one unit-height segment at column *i*", and dependency `u_i R u_j iff i = j`. Different columns never obstruct each other because gravity acts column by column, so the trace monoid is the free commutative monoid `N^w` and a heap is exactly a column-height vector `c = (c_1, …, c_w) in N^w` - heaps `=` towers, one-to-one. Weighting each piece by `x`, the cell-count generating function is `C_w(x) = ∑_c x^{|c|} = 1/(1 - x)^w`, so `[x^n] C_w = C(n+w-1, w-1)`. Cartier-Foata inversion `1/C_w = ∑_S (-x)^{|S|} = (1-x)^w` is tautological here because the columns already commute freely - all the Viennot content sits in the block count, not the cell count.

## Block count and the Narayana polynomial

Counting towers by number of blocks is where the Catalan/Narayana thread lives (not in the convex-castle count, which is binomial). The number of towers of width *w* with *b* blocks is[^3]

```
T(w,b) = Σ_{k=1..w} N(w,k) · C(b + w − k, w − 1),
   GF by b:  Narayana_w(x) / (1 − x)^w
```

with `N(w,k)` the [[narayana-numbers](pages/narayana-numbers.md)]. The `k`-th term counts the towers with exactly `k-1` descents in their height sequence (brute-force verified `w, b ≤ 7`). The block count itself is a boundary statistic: for a castle, semi-perimeter = width + blocks ([[castle-perimeter](pages/castle-perimeter.md)]). The width rows are `A005408` (w=2, odd numbers), `A005891` (w=3, centered pentagonal), `A063490` (w=4), `A160747` (w=5), and new for `w ≥ 6` - the full [[tower-narayana-polynomial](pages/tower-narayana-polynomial.md)] finding.[^3]

**A thread being walked.** The heap-of-pieces framing connects castles to Viennot's heap theory and to the transfer-matrix / commutation-monoid machinery of statistical mechanics, a direction into the broader combinatorics literature well beyond Project Euler 502 (PE 502). The setup is written out in [[viennot-heap-tower](pages/viennot-heap-tower.md)]: the tower as a heap over the trace monoid `N^w`, Cartier-Foata inversion recovering `1/(1-x)^w` for the cell count, and the transfer-matrix reading that produces `Narayana_w(x)/(1-x)^w` for the block count. That page also identifies where the naive heap-of-block-pieces recipe (intervals in `[1,w]`, dependency `=` shared column) fails to reproduce the tower count and what a heap-theoretic proof of the Narayana numerator would have to supply - the open half of the thread.

## Appearances in Sources

- [[tower-narayana-polynomial](pages/tower-narayana-polynomial.md)] — the tower block-count = Narayana-polynomial finding.
- [[oeis-mining-pe502](pages/oeis-mining-pe502.md)] — locates the Catalan/Narayana thread in the tower (veins 6/7).
- [[project-euler-502-representations](pages/project-euler-502-representations.md)] — the castle-as-`U (tower) D` reading the tower comes from.

## Related Concepts

- [[narayana-numbers](pages/narayana-numbers.md)] — the numerator of the tower block-count generating function (GF)
- [[castle-polyomino](pages/castle-polyomino.md)] — the tower plus the full-base / max-height / parity rules.
- [[generalized-dyck-grammar](pages/generalized-dyck-grammar.md)] — the grammar over tower words.
- [[viennot-heap-tower](pages/viennot-heap-tower.md)] — the trace-monoid / Cartier-Foata / transfer-matrix reading of the tower's cell and block counts.
- [[tower-word-continued-fraction](pages/tower-word-continued-fraction.md)] — the same tower object counted by step, matched to A004149 via a Motzkin J-fraction with a no-UD / no-DU run constraint.
- [[prellberg-brak-1995-cluster-models](pages/prellberg-brak-1995-cluster-models.md)] — the heap-bijection explanation of the staircase `H(qx)/H(x)` form, and the bar-graph (castle) equation in the same linearizable class.[^4]
- [[castle-foata-transform](pages/castle-foata-transform.md)] — blocks as maximal positive runs; the `c_1 + Σ max(0, c_i − c_{i−1})` block-count formula is the identity Foata builds on.
- [[castle-conditional-entropy](pages/castle-conditional-entropy.md)] — the tower block-count marginal whose `H(B) ~ (1/2) log_2 w` scaling this page's Narayana structure explains.

## Footnotes

[^1]: [[tower-narayana-polynomial](pages/tower-narayana-polynomial.md)] `SUBMISSION-NOTES.md` §"Definitions" L60-62 — "Tower (tier 2): column heights c_1..c_w >= 0 (no full-bottom, no max-height, no parity); blocks = maximal runs = c_1 + Sum_{i=2..w} max(0, c_i - c_{i-1})."
[^2]: [[tower-narayana-polynomial](pages/tower-narayana-polynomial.md)] `crosslink-avenues.md` §"Tier 2" L38-40 — "This is Viennot's 'heap of pieces': stack unit-height segments on w columns, each segment resting on the one below, segments in the same row separated by a gap."
[^3]: [[tower-narayana-polynomial](pages/tower-narayana-polynomial.md)] `crosslink-avenues.md` §"Tier 2" L43-56 — the tower block-count formula, its Narayana-polynomial GF, and the width-row table (A005408, A005891, A063490, A160747; new for w≥6).
[^4]: [[prellberg-brak-1995-cluster-models](pages/prellberg-brak-1995-cluster-models.md)] `prellberg-brak-1995-partially-directed-cluster-models.txt` §4 L771-778 - "both models have generating functions which can be expressed in the form G(x, y, q) = y(H(qx, y, q)/H(x, y, q) - 1) (4.14) where the function H satisfies a linear functional equation. In the case of staircase polygons, this structure can also be explained via a bijection with heaps".
