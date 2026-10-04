---
title: "Height-2 castles = A038505 / A038503 (hyperbolic family)"
category: Sources
summary: The lead OEIS interlink of the mining pass - height-2 castles by block parity are A038505(w+1) (even) and A038503(w+1)−1 (odd), a new geometric reading of two order-4 hyperbolic sequences, now in both OEIS entries (approved Oct 2026) together with A146559 = A038503 − A038505.
tags: [oeis, castle, height-2, hyperbolic, binomial, cross-reference, source]
sources: [oeis-height2-hyperbolic-castles]
created: 2026-09-13
updated: 2026-10-04
---

# Height-2 castles = A038505 / A038503 (hyperbolic family)

**Source:** `raw/oeis-pe502/oeis-xref-draft.md` (with `raw/oeis-pe502/mine-notes.md` §Vein 3)
**Date ingested:** 2026-09-13
**Type:** verified OEIS cross-reference finding (approved on A038503, A038505 and A146559)

## Summary

The lead interlink from the [[oeis-mining-pe502](pages/oeis-mining-pe502.md)] pass: the height-2 [[castle-polyomino](pages/castle-polyomino.md)], split by block-count parity, gives a **new geometric interpretation** for two members of the order-4 [[hyperbolic-sequence-family](pages/hyperbolic-sequence-family.md)].[^1]

A castle of height exactly 2 is determined by which columns reach height 2 — a length-*w* binary string with at least one `1`. The bottom row is one block; if the height-2 columns form *r* runs, the number of blocks is `1 + r`, and the number of width-*w* binary strings with exactly *r* runs of `1`s is `C(w+1, 2r)`.[^2] Splitting by parity:

```
F(w,2)   = A038505(w+1) = Σ_k C(w+1, 4k+2)        (even blocks ⟺ r odd)
odd(w,2) = A038503(w+1) − 1 = Σ_{k≥1} C(w+1, 4k)  (odd blocks ⟺ r even, r>0)
total    = A000225(w) = 2^w − 1
```

Both identities were re-verified by direct enumeration during ingest (`w = 1..7`), with offsets checked against the live OEIS entries: `A038505(n) = F(n−1,2)` for `n ≥ 2` (`a(0)=a(1)=0`), and `A038503(n) = odd(n−1,2) + 1` for `n ≥ 2` (`a(0)=a(1)=1`, the extra `1` being the all-height-1 castle).[^3] So the height-2 castle **decomposes the Mersenne number `2^w−1` by block-count parity** into two otherwise-isolated "sum of every 4th binomial" sequences.

## Why it was the lead target

A038505 ("sum of every 4th entry starting at C(n,2)") and A038503 ("...starting at C(n,0)") are relatively isolated entries whose existing comments are algebraic (trace/subtrace over generating function (GF)(2), matrix `M^n`, the Shevelev hyperbolic analog), none geometric.[^4] The castle comment is therefore a new interpretation, and the one clearly missing cross-reference is **A000225** (the total). The draft adds a Comment and a Formula (`a(n) = F(n−1,2)` / `a(n) = odd(n−1,2)+1`) to each, plus `Cf. A000225`, and links the signed vein via `A146559(n) = A038503(n) − A038505(n)` (see [[signed-tower-count](pages/signed-tower-count.md)]).[^5]

Per [[oeis-cross-referencing](pages/oeis-cross-referencing.md)], the submission text was drafted in `raw/oeis-pe502/oeis-xref-draft.md`, then reworded and signed by a person, and is now part of the entries (next section).

## On OEIS

The edits were drafted on both entries on 2026-09-18, proposed for review on 2026-09-26, and approved; all three entries show them as of 2026-10-04 (A038503 revision #93 and A038505 revision #136, both Oct 03 2026; A146559 revision #152, Sep 28 2026).[^6][^7][^8] Two changes from the `raw/oeis-pe502/oeis-xref-draft.md` draft: the A038503 comment counts castles of **height at most 2** (removing the wiki's `−1` offset), and the FORMULA lines use the **A000225 decomposition** rather than the direct `F(w,2)`/`odd(w,2)` form.

**A038503 — odd count.** The draft framed A038503 as "*1 more than* the number of height-2 castles with an odd block count" (the extra 1 = the all-height-1 castle). The live comment includes that castle by allowing height 1:[^6]

> a(n) is the number of castle polyominoes of width n-1 and height at most 2 with an odd number of blocks (Project Euler, Problem 502: Counting Castles), for n >= 2. Here a castle is a stack of unit blocks on a grid, whose bottom row is a single block of length n-1, whose higher blocks have height 1 and rest on the blocks below without overhang, whose height is at most 2, and in which two neighboring blocks of the same row are separated by a gap. If the columns that reach height 2 form r runs, the number of blocks is 1 + r, so an odd number of blocks means r is even. - _Chaz Reid_, Sep 18 2026

The wiki states the same fact at exact height: `odd(w,2) = A038503(w+1) − 1`, the `−1` removing the single castle of height 1.

**A038505 — even count.** Here the comment says "height 2", since the height-1 castle has one block and never enters the even count:[^7]

> a(n) is the number of castle polyominoes of width n-1 and height 2 with an even number of blocks (Project Euler, Project 502: Counting Castles), for n >= 2. Here a castle is a stack of unit blocks on a grid, whose bottom row is a single block of length n-1, whose higher blocks have height 1 and rest on the blocks below without overhang, whose maximum height is 2, and in which two neighboring blocks of the same row are separated by a gap. If the columns that reach height 2 form r runs, the number of blocks is 1 + r, so an even number of blocks means r is odd. - _Chaz Reid_, Sep 26 2026

The live A038505 comment reads "Project Euler, *Project* 502" where A038503 reads "*Problem* 502"; the entry's Link line has the correct title, `Project Euler, Problem 502: Counting Castles` → `https://projecteuler.net/problem=502`; a correction to "Problem 502" was submitted on 2026-10-04.[^7]

**Formulas** (each verified for `n = 1..13` against the binomial sums; all signed _Chaz Reid_, Sep 26 2026):[^6][^7][^8]

```
A038503:  a(n) = A000225(n-1) − A038505(n) + 1   for n ≥ 1
A038503:  a(n) = A038505(n) + A146559(n)
A038505:  a(n) = A000225(n-1) − A038503(n) + 1   for n ≥ 1
A146559:  a(n) = A038503(n) − A038505(n)
```

The two A000225 formulas are equivalent to `A038503(n) + A038505(n) = 2^(n−1)`, the castle split of the Mersenne number by block parity. The last two put **A146559** ([[signed-tower-count](pages/signed-tower-count.md)]) into the family, one in each direction.

**Cross-references.** **A000225** (the total) now heads the `Cf.` list of both entries, and A038503's `Cf.` also lists **A146559**.[^6][^7]

**Still a draft:** the A146559 comment `a(n) = P(1, n − 1)` (the signed tower count at `k = 1`) has not been submitted ([[castle-sequence-catalogue](pages/castle-sequence-catalogue.md)]).

## Key Takeaways

- **`F(w,2) = A038505(w+1)`**, **`odd(w,2) = A038503(w+1) − 1`**, total `2^w − 1 = A000225(w)` — verified with offsets.[^3]
- Proof: `blocks = 1 + r`, `#{width-w strings with r runs} = C(w+1, 2r)`, parity of `r` ↔ residue of `2r` mod 4.[^2]
- A new **geometric** reading of two isolated order-4 hyperbolic sequences; the only missing xref is A000225.[^4]
- `A146559 = A038503 − A038505` ties the signed count into the same family.[^5]
- **On OEIS since the Oct 03 2026 revisions** (Chaz Reid): the castle comment on A038503 (counting height at most 2, so no `−1`) and A038505, the decomposition formulas `a(n) = A000225(n−1) − A038505(n) + 1` and `a(n) = A038505(n) + A146559(n)` on A038503 and `a(n) = A000225(n−1) − A038503(n) + 1` on A038505, `a(n) = A038503(n) − A038505(n)` on A146559, `Cf. A000225` on both, and the Project Euler 502 link on A038505.[^6][^7][^8]

## Entities & Concepts

- [[hyperbolic-sequence-family](pages/hyperbolic-sequence-family.md)] — the four-sequence family A038503/4/5/A000749.
- [[castle-counting-function](pages/castle-counting-function.md)] — `F(w,2)`, `odd(w,2)`.
- [[signed-tower-count](pages/signed-tower-count.md)] — `A146559 = A038503 − A038505`.
- [[oeis-cross-referencing](pages/oeis-cross-referencing.md)] — the submission discipline (draft text kept in raw/).
- [[project-euler-502](pages/project-euler-502.md)] — the problem whose castle these entries now cite.
- [[block-count-constraints](pages/block-count-constraints.md)] — the interlink read as a residue class: even total blocks ⟺ an odd number of runs in row 2, the `m = 2` character sum on `Σ_r C(w+1, 2r) z^r`.
- [[new-sequence-fw3](pages/new-sequence-fw3.md)] — the `h = 3` row, where the same construction meets no OEIS entry.
- [[oeis-mining-seminar](pages/oeis-mining-seminar.md)] - Stops 1-4 and 7 of the seminar walk this interlink from enumeration to submission.


## Relation to Other Wiki Pages

The concrete, verified realization of the [[oeis-mining-pe502](pages/oeis-mining-pe502.md)] vein 3 headline, and an outward contribution of the wiki: a new interpretation offered to existing OEIS entries. Built on the binomial run-count structure also central to [[convex-castle-binomial-identity](pages/convex-castle-binomial-identity.md)].

## Footnotes

[^1]: [[oeis-height2-hyperbolic-castles](pages/oeis-height2-hyperbolic-castles.md)] `oeis-xref-draft.md` §0 "Verified identities" — the four sequences, offsets, and "F(w,2) = A038505(w+1) ... odd(w,2) = A038503(w+1) - 1 ... Total height-2 castles (any parity) = 2^w - 1 = A000225(w)."
[^2]: [[oeis-height2-hyperbolic-castles](pages/oeis-height2-hyperbolic-castles.md)] `oeis-xref-draft.md` §0 — "the number of blocks is 1 + r, where r = number of runs of height-2 columns. #strings of length w with exactly r runs of 1's = binomial(w+1, 2r). Even block count <=> 1 + r even <=> r odd <=> 2r = 2 mod 4."
[^3]: [[oeis-height2-hyperbolic-castles](pages/oeis-height2-hyperbolic-castles.md)] `oeis-xref-draft.md` §0 "Offset statements" — "A038505: a(n) = F(n-1, 2) for n >= 2, with a(0) = a(1) = 0 ... A038503: a(n) = odd(n-1, 2) + 1 for n >= 2, with a(0) = a(1) = 1"; F(w,2)=A038505(w+1) and odd(w,2)=A038503(w+1)-1 re-verified for w=1..7 during ingest.
[^4]: [[oeis-height2-hyperbolic-castles](pages/oeis-height2-hyperbolic-castles.md)] `oeis-xref-draft.md` §1 "What is already there" — the existing algebraic comments (trace/subtrace, M^n, Shevelev) and "the only genuinely missing cross-reference is A000225."
[^5]: [[oeis-height2-hyperbolic-castles](pages/oeis-height2-hyperbolic-castles.md)] `oeis-xref-draft.md` §§2-4 and `crosslink-avenues.md` §"Tier 1" L12-32 — the drafted Comment/Formula additions, `Cf. A000225`, and "a(n) = A038503(n) − A038505(n)" for A146559.
[^6]: OEIS [A038503](https://oeis.org/A038503), revision #93 (Oct 03 2026), read 2026-10-04 — the %C castle comment ("height at most 2 with an odd number of blocks", signed _Chaz Reid_, Sep 18 2026), the %F lines "a(n) = A000225(n-1) - A038505(n) + 1 for n >= 1" and "a(n) = A038505(n) + A146559(n)" (signed Sep 26 2026), and the Cf. line, which now begins with A000225 and ends with A146559.
[^7]: OEIS [A038505](https://oeis.org/A038505), revision #136 (Oct 03 2026), read 2026-10-04 — the %C castle comment ("height 2 with an even number of blocks (Project Euler, Project 502: Counting Castles)", signed _Chaz Reid_, Sep 26 2026), the %H link "Project Euler, Problem 502: Counting Castles" to projecteuler.net/problem=502, the %F line "a(n) = A000225(n-1) - A038503(n) + 1 for n >= 1", and the Cf. line, which now begins with A000225.
[^8]: OEIS [A146559](https://oeis.org/A146559), revision #152 (Sep 28 2026), read 2026-10-04 — the %F line "a(n) = A038503(n) - A038505(n). - _Chaz Reid_, Sep 26 2026".
