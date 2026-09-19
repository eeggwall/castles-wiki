---
title: "PE 502: Castle Factoring"
category: Sources
summary: The cycle-factorization subpage — the permutation-cycle/castle-peak analogy, the castle sign, a castle Foata transform, and the monotone streak factorization.
tags: [project-euler, castle, permutations, foata, factorization, source, subpage]
sources: [project-euler-502-castle-factoring]
created: 2026-09-13
updated: 2026-09-19
---

# Project Euler 502 (PE 502): Castle Factoring

**Source:** https://charlesreid1.com/wiki/Project_Euler/502/Castle_Factoring
**Date ingested:** 2026-09-13
**Type:** article (MediaWiki subpage of [[project-euler-502](pages/project-euler-502.md)])

## Summary

This subpage develops a cycle-factorization reading of the castle problem around a single through-line analogy: **permutation cycles are to a castle what peaks/excursions are to its skyline.**[^1] Just as Knuth factors a permutation into disjoint cycles by following the map `i ↦ σ(i)` until it closes, the [[generalized-dyck-grammar](pages/generalized-dyck-grammar.md)] factors a castle's tower word: each `U V D` peak leaves the base, lives entirely above one sub-block, and returns to the base, with `R` gaps playing the role of the parentheses that separate disjoint cycles. The page frames this as a genuine factorization — the Dyck first-return decomposition with one extra letter — not a metaphor.[^1]

The workhorse representation throughout is the **integer-tuple / column-height** encoding `c_1…c_L` (the number of blocks over each column), one of the [[castle-representations](pages/castle-representations.md)]. Reading castles this way yields three developments, each a castle analogue of a classical permutation construction:[^2] a **[[castle-sign](pages/castle-sign.md)]** `s(C) = (−1)^{blocks}` (the sign homomorphism); a **[[castle-foata-transform](pages/castle-foata-transform.md)]** matching peaks to the positive runs of the column-height sequence (Foata's canonical-cycle flattening); and a **[[monotone-streak-factorization](pages/monotone-streak-factorization.md)]** of the first-difference sequence into up-/flat-/down-streaks (the run-length form the fast algorithms sum over). The whole framework is organized by the [[permutation-cycle-castle-analogy](pages/permutation-cycle-castle-analogy.md)].

A clean by-product is a **product-form proof** of the unsigned tower count: because each column height ranges independently over `{0,…,k}`, immediately `T(k,L) = (k+1)^L`.[^3] The page also names the algorithms that make the signed count fast — the `P(k,L)` rational-function update evaluated by **Kitamasa** (`O(k² log L)` in the *L* direction) or **Berlekamp–Massey** (in the *k* direction), which is how the Solution subpage computes `F(10^12, 100)` and `F(100, 10^12)`.[^4] Finally it sketches three further encodings "worth writing up," now folded into [[castle-representations](pages/castle-representations.md)].[^5]

## Key Takeaways

- **The central analogy** (see [[permutation-cycle-castle-analogy](pages/permutation-cycle-castle-analogy.md)]): permutation cycles ↔ castle peaks; number of cycles ↔ number of peaks; permutation sign `(−1)^{n−c}` ↔ castle sign `(−1)^{blocks}`. Peak/excursion count and block count are *distinct* statistics — one peak can hold several stacked blocks.[^1]
- **Column-height product form:** each `c_i` chooses independently from `{0,…,k}`, so `T(k,L) = (k+1)^L` — the simplest proof of the unsigned count.[^3]
- **[[castle-sign](pages/castle-sign.md)]:** `s(C) = (−1)^{blocks(C)}` with `blocks = ∑ max(0, c_i − c_{i+1})`; then `(T+P)/2` counts even-block and `(T−P)/2` odd-block towers — the `(1 ± sgn)/2` even/odd projector, making `P(k,L)` the castle analogue of the sign homomorphism.[^6]
- **[[castle-foata-transform](pages/castle-foata-transform.md)]:** peaks are exactly the maximal positive runs of the column-height sequence; peak ↦ first column of its run is a bijection to the record set (left-to-right ascents from the base), so #peaks = #records. Verified on the `F(4,2)=10` miniature (all 10 towers have exactly one positive run).[^7]
- **[[monotone-streak-factorization](pages/monotone-streak-factorization.md)]:** first differences `d_i = c_{i+1} − c_i` factor into up-/flat-/down-streaks in one `O(L)` scan (the castle analogue of Knuth's `O(n)` cycle loop); block count = sum of down-streak magnitudes; the fast algorithms (Kitamasa / Berlekamp–Massey) sum over these canonical forms.[^4][^8]

## Entities & Concepts

- [[permutation-cycle-castle-analogy](pages/permutation-cycle-castle-analogy.md)] — the central analogy and its correspondence table.
- [[castle-sign](pages/castle-sign.md)] — `s(C) = (−1)^{blocks}`, the sign-homomorphism analogue and the even/odd projector.
- [[castle-foata-transform](pages/castle-foata-transform.md)] — peaks ↔ positive runs ↔ record set.
- [[monotone-streak-factorization](pages/monotone-streak-factorization.md)] — the first-difference streak decomposition and the fast-algorithm connection.
- [[castle-representations](pages/castle-representations.md)] — the integer-tuple/column-height representation is the workhorse here; three further encodings from this source are folded in.
- [[generalized-dyck-grammar](pages/generalized-dyck-grammar.md)], [[castle-counting-formula](pages/castle-counting-formula.md)], [[castle-polyomino](pages/castle-polyomino.md)] — updated by this source.

Also linked from the source and since ingested: [[polyominoes](pages/polyominoes.md)], [[dyck-words](pages/dyck-words.md)], [[project-euler-502-solution](pages/project-euler-502-solution.md)].
- Sibling subpages of the [[project-euler-502](pages/project-euler-502.md)] hub: [[project-euler-502-problem-setup](pages/project-euler-502-problem-setup.md)], [[project-euler-502-representations](pages/project-euler-502-representations.md)], [[project-euler-502-observations](pages/project-euler-502-observations.md)], [[project-euler-502-solution](pages/project-euler-502-solution.md)], [[project-euler-502-implementation-notes](pages/project-euler-502-implementation-notes.md)], [[project-euler-502-brute-force](pages/project-euler-502-brute-force.md)].
- [[aocp-multisets](pages/aocp-multisets.md)] — Knuth's Vol. 3 source for Foata's intercalation product and the two-line-array cycle factorization this subpage carries to castles; [[pe502-castle-cycle-permutations](pages/pe502-castle-cycle-permutations.md)] — the seminar note that upgrades the `(n−1)!` proof into this subpage's sign / Foata / streak triad.
- [[block-count-constraints](pages/block-count-constraints.md)] — the sign `(−1)^{blocks}` generalized to residue, sparse, and semigroup block-count constraints; [[castle-compression](pages/castle-compression.md)] — the run-length (streak, excursion/gap) encodings read as the second compression layer.

## Relation to Other Wiki Pages

This page reinterprets machinery already established on [[project-euler-502-representations](pages/project-euler-502-representations.md)] through the lens of permutation combinatorics. It gives the [[castle-counting-formula](pages/castle-counting-formula.md)] two things it lacked: a product-form proof of `T(k,L) = (k+1)^L` and an explanation of *why* `P(k,L)` is the right signed object (it is the sign homomorphism). It also names the evaluation algorithms (Kitamasa, Berlekamp–Massey) that the still-queued Solution subpage uses for the large-parameter evaluations.

## References (from the source)

- Donald E. Knuth, *The Art of Computer Programming*, Vol. 1, 3rd ed., §1.3.3 ("An Unusual Correspondence").[^9]
- GNU Scientific Library — Permutations, canonical cyclic form.[^9]
- Foata's fundamental transformation (Knuth canonical-cycle flattening).[^9]

## Footnotes

[^1]: [[project-euler-502-castle-factoring](pages/project-euler-502-castle-factoring.md)] §"Castle Factoring and the Knuth-Castle Foata Transform" L5-9 — "permutation cycles : castle peaks/excursions" and "each U V D peak leaves the base, lives entirely above a sub-block, and returns to the same level ... This is a genuine factorization, not a metaphor: it is the Dyck first-return decomposition with one extra letter (R)."
[^2]: [[project-euler-502-castle-factoring](pages/project-euler-502-castle-factoring.md)] §"Castle Factoring and the Knuth-Castle Foata Transform" L11-13 — "a sign for castles ...; a castle Foata transform ...; a monotone streak factorization, the run-length view the fast algorithms sum over."
[^3]: [[project-euler-502-castle-factoring](pages/project-euler-502-castle-factoring.md)] §"A column-height factorization" L72-89 — "each c_i ranges independently over {0, …, k} ... T(k,L) = (k+1)^L ... each of the L columns independently chooses one of k+1 heights. This is the product-form proof."
[^4]: [[project-euler-502-castle-factoring](pages/project-euler-502-castle-factoring.md)] §"Monotone streak factorization and fast algorithms" L192 — "evaluated in O(k^2 log L) by Kitamasa in the L direction, or in the k direction by Berlekamp-Massey, which is how [Solution] computes F(10^12, 100) and F(100, 10^12)."
[^5]: [[project-euler-502-castle-factoring](pages/project-euler-502-castle-factoring.md)] §"New representations worth writing up" L194-216 [synthesis] — the excursion/gap word, cycle-forest form, and signed column-difference sequence.
[^6]: [[project-euler-502-castle-factoring](pages/project-euler-502-castle-factoring.md)] §"The sign of a castle" L101-127 — "s(C) = (-1)^{blocks(C)}", "blocks = ∑ max(0, c_i - c_{i+1})", and "(T + P)/2 = even-block castles, (T - P)/2 = odd-block castles ... exactly the (1 ± sgn)/2 trick ... P(k,L) ... is the castle analogue of the sign homomorphism."
[^7]: [[project-euler-502-castle-factoring](pages/project-euler-502-castle-factoring.md)] §"The castle version" L141-165 — the peak↔positive-run bijection and the F(4,2)=10 test with tower heights "1000 0100 0010 0001 1100 0110 0011 1110 0111 1111", "Each has exactly one positive run, hence exactly one peak"; re-verified during ingest (all 10 have exactly one positive run).
[^8]: [[project-euler-502-castle-factoring](pages/project-euler-502-castle-factoring.md)] §"Monotone streak factorization and fast algorithms" L169-181 — "d_i = c_{i+1} - c_i ... Factor the d sequence into maximal up-streaks ..., flat runs ..., and down-streaks ... the number of blocks equals ... the sum of the magnitudes of the down-streaks ... a single O(L) scan, the castle version of Knuth's O(n) cycle-following loop."
[^9]: [[project-euler-502-castle-factoring](pages/project-euler-502-castle-factoring.md)] §"References" L236-238 — Knuth TAOCP Vol. 1 §1.3.3 "An Unusual Correspondence"; GSL Permutations canonical cyclic form; "Foata's fundamental transformation (Knuth canonical-cycle flattening)."
