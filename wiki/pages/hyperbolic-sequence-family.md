---
title: Order-4 hyperbolic sequence family
category: Concepts
summary: The four "sum of every 4th binomial" sequences A038503/A038504/A038505/A000749; the height-2 castle gives two of them (F and odd block counts) a new geometric reading.
tags: [concept, oeis, binomial, hyperbolic, castle, height-2]
sources: [oeis-mining-pe502, oeis-height2-hyperbolic-castles]
created: 2026-09-13
updated: 2026-09-13
---

# Order-4 hyperbolic sequence family

## Description

The **order-4 "hyperbolic" family** is the set of four OEIS sequences formed by summing every fourth entry of a row of Pascal's triangle, starting at each of the four residues:[^1]

- **A038503** = `Σ_k C(n, 4k)` (start at `C(n,0)`)
- **A038504** = `Σ_k C(n, 4k+1)` (start at `C(n,1)`)
- **A038505** = `Σ_k C(n, 4k+2)` (start at `C(n,2)`)
- **A000749** = `Σ_k C(n, 4k+3)` (start at `C(n,3)`)

They satisfy a common order-4 linear recurrence (roots the 8th roots of unity scaled — the "hyperbolic" analog of `Re/Im` of `(1+i)^n`) and sum to `2^n`. Two of them are relatively isolated "sum of every 4th entry" entries, under-connected in the OEIS.

## The castle reading

The height-2 [[castle-polyomino](pages/castle-polyomino.md)] gives two members of this family a genuine new combinatorial interpretation — the central win of the [[oeis-mining-pe502](pages/oeis-mining-pe502.md)] pass (see [[oeis-height2-hyperbolic-castles](pages/oeis-height2-hyperbolic-castles.md)]):[^2]

```
F(w,2)   = A038505(w+1) = Σ_k C(w+1, 4k+2)        (even-block castles)
odd(w,2) = A038503(w+1) − 1 = Σ_{k≥1} C(w+1, 4k)  (odd-block castles)
total    = A000225(w) = 2^w − 1
```

A height-2 castle is fixed by which columns reach height 2 (a length-*w* binary string, ≥1 one); if those columns form *r* runs, the block count is `1 + r`, and there are `C(w+1, 2r)` strings with *r* runs. Even blocks ⟺ *r* odd ⟺ `2r ≡ 2 (mod 4)`, which is exactly A038505; odd blocks ⟺ *r* even (excluding `r=0`), which is A038503 minus one.[^2] So the height-2 castle **decomposes the Mersenne number `2^w−1` by block-count parity** into two of the four hyperbolic sequences. The signed count `A146559 = Re((1+i)^n)` closes the circle: `A146559(n) = A038503(n) − A038505(n)` (see [[signed-tower-count](pages/signed-tower-count.md)]).[^3]

## Appearances in Sources

- [[oeis-height2-hyperbolic-castles](pages/oeis-height2-hyperbolic-castles.md)] — the full identity, proof, and cross-reference draft.
- [[oeis-mining-pe502](pages/oeis-mining-pe502.md)] — vein 3; names this the highest-value interlinking target.

## Related Concepts

- [[castle-counting-function](pages/castle-counting-function.md)] — `F(w,2)`, `odd(w,2)`.
- [[signed-tower-count](pages/signed-tower-count.md)] — `A146559 = A038503 − A038505`.
- [[oeis-cross-referencing](pages/oeis-cross-referencing.md)] — why isolated entries like these are the best cross-link targets.

## Footnotes

[^1]: [[oeis-height2-hyperbolic-castles](pages/oeis-height2-hyperbolic-castles.md)] `oeis-xref-draft.md` §0 — "A038505(n) = Sum_k binomial(n, 2+4k) ... A038503(n) = Sum_k binomial(n, 4k)"; `mine-notes.md` §"Vein 3" L60-61 — "two of the four order-4 'hyperbolic' sequences {A038503, A038504, A038505, A000749}."
[^2]: [[oeis-height2-hyperbolic-castles](pages/oeis-height2-hyperbolic-castles.md)] `mine-notes.md` §"Vein 3" L55-68 — "F(w,2) = A038505(w+1) = sum_k C(w+1, 2+4k) ... odd(w,2) = A038503(w+1) - 1 ... blocks = 1 + (#runs of top cells), and the number of width-w binary strings with exactly r runs of 1's is C(w+1, 2r). Even blocks <=> r odd <=> j = 2r ≡ 2 (mod 4)"; F(w,2), odd(w,2) re-verified for w=1..7 during ingest.
[^3]: [[oeis-height2-hyperbolic-castles](pages/oeis-height2-hyperbolic-castles.md)] `crosslink-avenues.md` §"Tier 1 / 3. A146559" L25-32 — "a(n) = A038503(n) − A038505(n) (verified: Re((1+i)^n) = Σ_{j≡0} − Σ_{j≡2} binomial)."
