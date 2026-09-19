---
title: Castles by area
category: Concepts
summary: Re-indexing castles by total cells n instead of (w,h) — convex↔A001523, all↔2^{n−1}, valley↔A332578, non-convex↔A115981, plus new parity-refined and strict-valley sequences.
tags: [concept, castle, area, composition, oeis, unimodal, valley]
sources: [oeis-mining-pe502, castle-by-area]
created: 2026-09-13
updated: 2026-09-19
---

# Castles by area

## Description

**Area** re-indexing counts castles by total cells `n = ∑ c_i` instead of by width and height — a finite enumeration (a castle of area *n* has `1 ≤ w,h ≤ n`) that recasts each castle as a **composition of *n*** (an ordered sequence of positive parts). This single change of index turns several castle counts into well-known composition sequences and produces new parity-refined ones. It is veins 9 and 9b of the [[oeis-mining-pe502](pages/oeis-mining-pe502.md)] pass (computed by `vein9_area.py` / `vein9b_concave.py`, verified for `n ≤ 15..18`).

## Matches (all definitional; dense OEIS entries)

- **All castles of area *n* = `2^{n−1}`** (`A000079(n−1)` / `A011782`) — every composition of *n* is a castle shape (Rule 3 automatic). Trivial.[^1]
- **Convex castles = `A001523(n)`** — a [[convex-castle](pages/convex-castle.md)] of area *n* is exactly a [[weakly-unimodal-composition](pages/weakly-unimodal-composition.md)] of *n* ("stacks"). Verified `n=1..18`.[^2]
- **Valley castles = `A332578(n)`** — a valley-shaped castle (weakly decreasing then increasing) is a composition whose *negation* is unimodal; the mirror of A001523.[^3]
- **Non-convex castles = `A115981(n)` = `A011782(n) − A001523(n)`** — compositions "not viewable as stacks."[^3]
- **Not-valley (complement of valley) = `A332669(n)` = `2^{n−1} − A332578(n)`.**[^3]

Per the phase-2 submission plan, the three dense matches — **A001523**, **A332578**, **A115981** — cross-reference the phase-1 height-2 sequences **A038505 / A038503 / A146559** ([[oeis-height2-hyperbolic-castles](pages/oeis-height2-hyperbolic-castles.md)]), tying the area-parametrized block-parity counts back to the width-index hyperbolic family.

## New sequences (generation candidates)

- **Parity splits by area** — `even/odd` (block-parity of all castles) and CEV/COD (convex-even and convex-odd: block-parity of convex castles), none in OEIS. The quotable identities: `even(n)+odd(n) = 2^{n−1}` and **`cev(n)+cod(n) = A001523(n)`** — a parity refinement of a foundational sequence.[^4]
- **`strict_valley(n)`** — castles with a *true* interior dip (valley and not unimodal): `0,0,0,0,1,3,8,17,34,60,107,175,285,445,691,…`. New, no OEIS match on 15 terms.[^5]
- **Six parity-refined concave sequences** — `valley_even/odd` (split of A332578), `nc_even/odd` (split of A115981), `sv_even/odd` — all new.[^5]

## The (w,h) view, and a candidate bijection

By (w,h) the concave counts add nothing new: `valley(w,h) = convex(w,h) = C(2h+w−3, w−1)` — the same binomial as [[convex-castle-binomial-identity](pages/convex-castle-binomial-identity.md)], different *sets*. Convex and valley castles are therefore **equinumerous in every (w,h) cell** under the peak↔valley mirror — a candidate bijection worth writing up, even though it yields no new OEIS entry on the (w,h) axis.[^6] (The plan's speculated matches — A001168 fixed polyominoes, A005435 column-convex-by-perimeter — were numerically far off; castles-by-area live in the "stacks of boards" class, not the general polyomino class.)[^7]

## Appearances in Sources

- [[oeis-mining-pe502](pages/oeis-mining-pe502.md)] — veins 9 and 9b: the area re-indexing and all matches/new sequences.

## Related Concepts

- [[weakly-unimodal-composition](pages/weakly-unimodal-composition.md)] — A001523, the convex-by-area match.
- [[convex-castle](pages/convex-castle.md)] — convex/valley castles and their binomial (w,h) count.
- [[oeis-cross-referencing](pages/oeis-cross-referencing.md)] — why dense-entry matches are low-value but real.
- [[aocp-combinatorics](pages/aocp-combinatorics.md)] — area is the castle's natural second grading; the inversion statistic and its q-factorial generating function (GF) are the permutation-level prototype of such q-gradings.

## Footnotes

[^1]: [[castle-by-area](pages/castle-by-area.md)] `vein9-area.md` §"The trivial baseline" L8-13 — "All castles of area n = all compositions of n into positive parts = 2^(n-1) = A000079(n-1) ... every ordered sequence (c_1..c_w) ... is a valid castle shape (Rule 3 is automatic)."
[^2]: [[castle-by-area](pages/castle-by-area.md)] `vein9-area.md` §"The main finding" L13-31 — "Convex (unimodal) castles of area n matches A001523 exactly for the 18 terms computed ... a definition-level match, not a coincidence"; re-verified during ingest.
[^3]: [[castle-by-area](pages/castle-by-area.md)] `vein9b-concave.md` §"Results by area" L8-40 — "valley(n) = A332578(n) ... nonconv(n) = A115981(n) ... all(n) − valley(n) = A332669(n) ... A115981(n) = A011782(n) − A001523(n)."
[^4]: [[castle-by-area](pages/castle-by-area.md)] `vein9-area.md` §"Parity splits" L35-52 — the even/odd/CEV/COD table and "cev(n) + cod(n) = A001523(n) (parity split of A001523) ... a genuine refinement of a foundational sequence."
[^5]: [[castle-by-area](pages/castle-by-area.md)] `vein9b-concave.md` §"The new sequence" L48-56 and §"Parity splits — all new" L60-78 — "strict_valley(n) = 0, 0, 0, 0, 1, 3, 8, 17, 34, 60, 107, 175, 285, 445, 691" and the six parity-refined variants with "valley_even + valley_odd = A332578 ... nc_even + nc_odd = A115981."
[^6]: [[castle-by-area](pages/castle-by-area.md)] `vein9b-concave.md` §"Concave counts by (w, h)" L100-118 — "This is the same table as convex(w, h) — both equal C(2h + w − 3, w − 1) ... same cardinality in each (w, h) cell but different sets ... a candidate bijection worth writing up."
[^7]: [[castle-by-area](pages/castle-by-area.md)] `vein9-area.md` §"Not-a-match" L54-63 — "A001168 (fixed polyominoes) ... and A005435 ... Neither is close numerically ... The right match for castles is unambiguously A001523 (stacks / unimodal compositions)."
