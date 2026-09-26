---
title: "Height-2 castles = A038505 / A038503 (hyperbolic family)"
category: Sources
summary: The first-pass's highest-value OEIS interlink — height-2 castles by block parity are A038505(w+1) (even) and A038503(w+1)−1 (odd), a new geometric reading of two order-4 hyperbolic sequences.
tags: [oeis, castle, height-2, hyperbolic, binomial, cross-reference, source]
sources: [oeis-height2-hyperbolic-castles]
created: 2026-09-13
updated: 2026-09-26
---

# Height-2 castles = A038505 / A038503 (hyperbolic family)

**Source:** `~/code/oeis/pe502/oeis-xref-draft.md` (with `mine-notes.md` §Vein 3), copied to `raw/oeis-pe502/`
**Date ingested:** 2026-09-13
**Type:** verified OEIS cross-reference finding (draft submission for A038505/A038503)

## Summary

The single highest-value interlink from the [[oeis-mining-pe502](pages/oeis-mining-pe502.md)] pass: the height-2 [[castle-polyomino](pages/castle-polyomino.md)], split by block-count parity, gives a **new geometric interpretation** for two members of the order-4 [[hyperbolic-sequence-family](pages/hyperbolic-sequence-family.md)].[^1]

A castle of height exactly 2 is determined by which columns reach height 2 — a length-*w* binary string with at least one `1`. The bottom row is one block; if the height-2 columns form *r* runs, the number of blocks is `1 + r`, and the number of width-*w* binary strings with exactly *r* runs of `1`s is `C(w+1, 2r)`.[^2] Splitting by parity:

```
F(w,2)   = A038505(w+1) = Σ_k C(w+1, 4k+2)        (even blocks ⟺ r odd)
odd(w,2) = A038503(w+1) − 1 = Σ_{k≥1} C(w+1, 4k)  (odd blocks ⟺ r even, r>0)
total    = A000225(w) = 2^w − 1
```

Both identities were re-verified by direct enumeration during ingest (`w = 1..7`), with offsets checked against the live OEIS entries: `A038505(n) = F(n−1,2)` for `n ≥ 2` (`a(0)=a(1)=0`), and `A038503(n) = odd(n−1,2) + 1` for `n ≥ 2` (`a(0)=a(1)=1`, the extra `1` being the all-height-1 castle).[^3] So the height-2 castle **decomposes the Mersenne number `2^w−1` by block-count parity** into two otherwise-isolated "sum of every 4th binomial" sequences.

## Why it is the best target

A038505 ("sum of every 4th entry starting at C(n,2)") and A038503 ("...starting at C(n,0)") are relatively isolated entries whose existing comments are algebraic (trace/subtrace over generating function (GF)(2), matrix `M^n`, the Shevelev hyperbolic analog) — none geometric.[^4] The castle comment is therefore a genuinely new interpretation, and the one clearly missing cross-reference is **A000225** (the total). The draft adds a Comment and a Formula (`a(n) = F(n−1,2)` / `a(n) = odd(n−1,2)+1`) to each, plus `Cf. A000225`, and links the signed vein via `A146559(n) = A038503(n) − A038505(n)` (see [[signed-tower-count](pages/signed-tower-count.md)]).[^5]

Per [[oeis-cross-referencing](pages/oeis-cross-referencing.md)], the submission text started as a draft only (human authorship required); it lived in `raw/oeis-pe502/oeis-xref-draft.md`, was reworded and signed, and was submitted on 2026-09-18 (next section). This is the lead ("tier 1") interlink.

## Submitted to OEIS (2026-09-18)

The draft was submitted to both entries on 2026-09-18 (attributed "Chaz Reid, Sep 18 2026"). Two changes from the `raw/oeis-pe502/oeis-xref-draft.md` draft are worth recording: the A038503 comment adopts a cleaner **"height at most 2"** phrasing (removing the wiki's `−1` offset), and the FORMULA set is the **A000225-decomposition** form rather than the direct `F(w,2)`/`odd(w,2)` form.

**A038503 — odd count.** The draft framed A038503 as "*1 more than* the number of height-2 castles with an odd block count" (the extra 1 = the all-height-1 castle). The submitted comment folds that 1 in directly by allowing height 1:

> a(n) is the number of castle polyominoes of width n-1 and height at most 2 with an odd number of blocks (Project Euler, Problem 502: Counting Castles), for n >= 2. Here a castle is a stack of unit blocks on a grid, whose bottom row is a single block of length n-1, whose higher blocks have height 1 and rest on the blocks below without overhang, whose height is at most 2, and in which two neighboring blocks of the same row are separated by a gap. If the columns that reach height 2 form r runs, the number of blocks is 1 + r, so an odd number of blocks means r is even. - Chaz Reid, Sep 18 2026

So OEIS now states **A038503(n) = odd-block castles of height ≤ 2** with no offset correction; the wiki's `odd(w,2) = A038503(w+1) − 1` is the equivalent "height exactly 2" restatement that subtracts the single height-1 castle.

**A038505 — even count** (unchanged "height 2", since a height-1 castle is odd and never enters the even count):

> a(n) is the number of castle polyominoes of width n-1 and height 2 with an even number of blocks (Project Euler, Problem 502: Counting Castles), for n >= 2. Here a castle is a stack of unit blocks on a grid, whose bottom row is a single block of length w = n-1, whose higher blocks have height 1 and rest on the blocks below without overhang, whose maximum height is 2, and in which two neighboring blocks of the same row are separated by a gap. If the columns that reach height 2 form r runs, the number of blocks is 1 + r, so an even number of blocks means r is odd. - Chaz Reid, Sep 18 2026

**Submitted formulas** (each re-verified for `n = 0..13` against the binomial sums during this update):

```
A038503:  a(n) = A000225(n-1) − A038505(n) + 1   for n ≥ 1
A038503:  a(n) = A038505(n) + A146559(n)          (the signed-tower link, now in OEIS)
A038505:  a(n) = A000225(n-1) − A038503(n) + 1   for n ≥ 1
```

The two A000225 formulas are equivalent to `A038503(n) + A038505(n) = 2^(n−1)` — the castle split of the Mersenne number by block parity, now stated inside OEIS itself. The third puts **A146559** ([[signed-tower-count](pages/signed-tower-count.md)]) directly into the entry as `a(n) = A038505(n) + A146559(n)` — the signed vein's first appearance in an OEIS entry; **A146559 itself** was also updated the same day with the converse `a(n) = A038503(n) − A038505(n)`.

**Also added:** the clickable `Project Euler, Problem 502: Counting Castles` link on A038505, and **A000225** (the total) to the `Cf.` list of both entries, with **A146559** added to A038503's `Cf.`.

## Key Takeaways

- **`F(w,2) = A038505(w+1)`**, **`odd(w,2) = A038503(w+1) − 1`**, total `2^w − 1 = A000225(w)` — verified with offsets.[^3]
- Proof: `blocks = 1 + r`, `#{width-w strings with r runs} = C(w+1, 2r)`, parity of `r` ↔ residue of `2r` mod 4.[^2]
- A new **geometric** reading of two isolated order-4 hyperbolic sequences; the only missing xref is A000225.[^4]
- `A146559 = A038503 − A038505` ties the signed count into the same family.[^5]
- **Submitted 2026-09-18** (Chaz Reid): the castle comment now lives in both entries — A038503 stated as "height ≤ 2, odd blocks" (no `−1`) — with the decomposition formulas `a(n) = A000225(n−1) − A038505(n) + 1` and `a(n) = A038505(n) + A146559(n)` on A038503, and `a(n) = A000225(n−1) − A038503(n) + 1` on A038505.

## Entities & Concepts

- [[hyperbolic-sequence-family](pages/hyperbolic-sequence-family.md)] — the four-sequence family A038503/4/5/A000749.
- [[castle-counting-function](pages/castle-counting-function.md)] — `F(w,2)`, `odd(w,2)`.
- [[signed-tower-count](pages/signed-tower-count.md)] — `A146559 = A038503 − A038505`.
- [[oeis-cross-referencing](pages/oeis-cross-referencing.md)] — the submission discipline (draft text kept in raw/).
- [[block-count-constraints](pages/block-count-constraints.md)] — the interlink read as a residue class: even total blocks ⟺ an odd number of runs in row 2, the `m = 2` character sum on `Σ_r C(w+1, 2r) z^r`.
- [[new-sequence-fw3](pages/new-sequence-fw3.md)] — the `h = 3` row, where the same construction meets no OEIS entry.
- [[oeis-mining-seminar](pages/oeis-mining-seminar.md)] - Stops 1-4 and 7 of the seminar walk this interlink from enumeration to submission.


## Relation to Other Wiki Pages

The concrete, verified realization of the [[oeis-mining-pe502](pages/oeis-mining-pe502.md)] vein 3 headline, and the wiki's first genuine outward contribution: a new interpretation offered to existing OEIS entries. Built on the binomial run-count structure also central to [[convex-castle-binomial-identity](pages/convex-castle-binomial-identity.md)].

## Footnotes

[^1]: [[oeis-height2-hyperbolic-castles](pages/oeis-height2-hyperbolic-castles.md)] `oeis-xref-draft.md` §0 "Verified identities" — the four sequences, offsets, and "F(w,2) = A038505(w+1) ... odd(w,2) = A038503(w+1) - 1 ... Total height-2 castles (any parity) = 2^w - 1 = A000225(w)."
[^2]: [[oeis-height2-hyperbolic-castles](pages/oeis-height2-hyperbolic-castles.md)] `oeis-xref-draft.md` §0 — "the number of blocks is 1 + r, where r = number of runs of height-2 columns. #strings of length w with exactly r runs of 1's = binomial(w+1, 2r). Even block count <=> 1 + r even <=> r odd <=> 2r = 2 mod 4."
[^3]: [[oeis-height2-hyperbolic-castles](pages/oeis-height2-hyperbolic-castles.md)] `oeis-xref-draft.md` §0 "Offset statements" — "A038505: a(n) = F(n-1, 2) for n >= 2, with a(0) = a(1) = 0 ... A038503: a(n) = odd(n-1, 2) + 1 for n >= 2, with a(0) = a(1) = 1"; F(w,2)=A038505(w+1) and odd(w,2)=A038503(w+1)-1 re-verified for w=1..7 during ingest.
[^4]: [[oeis-height2-hyperbolic-castles](pages/oeis-height2-hyperbolic-castles.md)] `oeis-xref-draft.md` §1 "What is already there" — the existing algebraic comments (trace/subtrace, M^n, Shevelev) and "the only genuinely missing cross-reference is A000225."
[^5]: [[oeis-height2-hyperbolic-castles](pages/oeis-height2-hyperbolic-castles.md)] `oeis-xref-draft.md` §§2-4 and `crosslink-avenues.md` §"Tier 1" L12-32 — the drafted Comment/Formula additions, `Cf. A000225`, and "a(n) = A038503(n) − A038505(n)" for A146559.
