---
title: "Castles as an upgrade of the (n−1)! cycle count"
category: Analyses
summary: PE 502 as the same toolkit that proves (n−1)! for cycles, upgraded step-by-step to handle stacked, width-weighted, sign-selected cycles. Seminar-ready framing that ties the elementary anchor to the [[castle-sign]] / [[castle-foata-transform]] / [[monotone-streak-factorization]] triad.
tags: [analysis, castle, permutations, cycles, seminar, factorization, sign]
sources: [pe502-castle-cycle-permutations]
created: 2026-09-15
updated: 2026-09-19
---

# Castles as an upgrade of the (n−1)! cycle count

## The elementary anchor: (n−1)! labelled cycles

A **cycle on `n` labelled items** is a cyclic arrangement — an ordering up to rotation. The number of such directed cycles is `(n−1)!`, and there are two standard proofs:[^1]

1. **Quotient by rotation.** There are `n!` linear orderings of the `n` items; the free `Z/n` rotation action groups them into cycle-equivalence classes of size `n`, giving `n!/n = (n−1)!` cycles.[^1]
2. **Fix a starting point.** Every cycle can be written uniquely starting with the item labelled `1`; the remaining `n−1` items then order freely, giving `(n−1)!` cycles.[^1]

Both proofs are instances of a **bigger machine** — Foata's fundamental transformation, the sign homomorphism, and Knuth's `O(n)` cycle-following loop — and that same machine, upgraded three times, is what proves the [[castle-counting-formula](pages/castle-counting-formula.md)] and drives the fast [[castle-count-algorithms](pages/castle-count-algorithms.md)].[^2]

## The three upgrades

The [[permutation-cycle-castle-analogy](pages/permutation-cycle-castle-analogy.md)] is not decorative: it is a genuine factorization (the [[generalized-dyck-grammar](pages/generalized-dyck-grammar.md)] is the Dyck first-return grammar with a third letter), and each move in the `(n−1)!` proof has a direct castle counterpart. The three-row proof-move ↔ castle-counterpart correspondence table is single-sourced on [[permutation-cycle-castle-analogy](pages/permutation-cycle-castle-analogy.md)] §"The (n−1)! anchor": *divide by `n` / `(1 ± sgn)/2`* → [[castle-sign](pages/castle-sign.md)], *canonical form / Foata* → [[castle-foata-transform](pages/castle-foata-transform.md)], *cycle-follow `i ↦ σ(i)`* → [[monotone-streak-factorization](pages/monotone-streak-factorization.md)].

Nothing in the machine changes. Only the objects it acts on grow: `n` labelled points become `L` columns of unbounded height with `w` widths, one row's cycles become a stack that carries multiplicity, and the sign is measured on **blocks** (stacked atoms) instead of transpositions.[^3]

## Hand check: F(4,2) = 10 via the closed form

The [[castle-counting-formula](pages/castle-counting-formula.md)] gives[^4]

```
F(w,h) = ½ · [ h^w − (h−1)^w − P(h−1, w) + P(h−2, w) ]
```

For `(w,h) = (4,2)`, the four values are `h^w = 16`, `(h−1)^w = 1`, `P(1,4) = −4`, `P(0,4) = 1` (both signed counts re-verified during ingest by direct enumeration over the 16 length-4 binary column-height strings and the trivial `k=0` case).[^4] Substituting:

```
F(4,2) = (16 − 1 − (−4) + 1) / 2 = 20 / 2 = 10.
```

Direct enumeration matches: the bottom-row block is forced full-width, and even-total parity forces an odd number of tower blocks - an odd number of maximal `1`-runs in a length-4 binary string, which at width 4 means exactly one run, since three runs need width at least 5 — `1000, 0100, 0010, 0001, 1100, 0110, 0011, 1110, 0111, 1111` — the 10 configurations of the [[castle-foata-transform](pages/castle-foata-transform.md)] miniature.[^5] (At width 5 the three-run string `10101` joins and `F(5,2) = 16`; the general count is `Σ_s C(w+1, 4s+2) = A038505(w+1)`, see [[hyperbolic-sequence-family](pages/hyperbolic-sequence-family.md)].)

The three upgrades read off this hand check directly:

- **Sign upgrade.** `(T − P)/2` at the tower level selects the "odd tower blocks" class, which is what "even total castle blocks" means (the bottom block adds one). This is the [[castle-sign](pages/castle-sign.md)] projector in action.[^6]
- **Foata upgrade.** Each of the 10 configurations has exactly one maximal positive run → exactly one peak, one record — the [[castle-foata-transform](pages/castle-foata-transform.md)] bijection in miniature.[^7]
- **Streak upgrade.** Each configuration's first-difference sequence has a single up-streak and a single down-streak of magnitude 1 — the [[monotone-streak-factorization](pages/monotone-streak-factorization.md)] one-block reading.[^8]

## The caveat that makes the castle richer than a permutation

**Block count ≠ peak count.** A single peak — one `U…D` excursion — can be several stacked blocks. So the `(−1)^{blocks}` sign atom of [[castle-sign](pages/castle-sign.md)] and the peak-count analogue of the cycle count are **different statistics on the same castle**.[^9] The Foata bijection is with peaks; the sign is measured on blocks. `3! = 6 ≠ 10`: the analogy is one-peak ↔ one-cycle in structure, not in cardinality, because castle rows have arbitrary integer widths where cycles have unit-labelled elements.[^10]

This is the fingerprint of a genuinely richer combinatorial object than plain permutations — the castle sits between **cycles of a permutation** and **cycles with multiplicity and height**. The `(n−1)!` proof is the degenerate case where multiplicity and height are trivial; the castle machinery is running the same three moves at industrial scale.

## Seminar shape

For an outward-facing seminar the material assembles cleanly:

1. Open with `(n−1)!` and its two proofs (the elementary hook).
2. Present the correspondence table from [[permutation-cycle-castle-analogy](pages/permutation-cycle-castle-analogy.md)] as an analogy — this is where the audience begins to guess where the talk is heading.
3. State the three upgrades as the three-row table above, one row per subsequent lecture beat.
4. Land on `F(4,2) = 10` derived twice: once by direct enumeration (permutation-style), once by the closed form (castle-machine-style).
5. Flag the block ≠ peak caveat, and set up q-analog / Viennot heap directions ([[tower-heap](pages/tower-heap.md)], `TODO.md`) as the natural next questions.

The point of the talk is not the answer (`F(w,h)` exists in closed form), but that **the toolkit** — sign homomorphism, Foata flattening, cycle-following — is the same toolkit for both. Project Euler 502 (PE 502) is what happens when you upgrade every move.

## Appearances in Sources

- [[pe502-castle-cycle-permutations](pages/pe502-castle-cycle-permutations.md)] — the working note that stated the "(n−1)! → castles" thesis and supplied the closing correspondence table.

## Related Concepts

- [[permutation-cycle-castle-analogy](pages/permutation-cycle-castle-analogy.md)] — the analogy this analysis upgrades from metaphor to seminar spine.
- [[castle-sign](pages/castle-sign.md)] — the sign upgrade.
- [[castle-foata-transform](pages/castle-foata-transform.md)] — the Foata upgrade.
- [[monotone-streak-factorization](pages/monotone-streak-factorization.md)] — the cycle-following upgrade.
- [[castle-counting-formula](pages/castle-counting-formula.md)] — the closed form the three upgrades combine to yield.
- [[generalized-dyck-grammar](pages/generalized-dyck-grammar.md)] — the factorization on the castle side.
- [[aocp-multisets](pages/aocp-multisets.md)] / [[aocp-permutations](pages/aocp-permutations.md)] — Knuth's Vol. 3 and Vol. 1 sources for the two-line-array cycle apparatus and canonical cycle form.
- [[project-euler-502-observations](pages/project-euler-502-observations.md)] — the source that names `(A + P)/2` "a symmetry trick that recurs in many combinatorial-enumeration problems"; the `(1 ± sgn)/2` anchor above is its elementary case.

## Footnotes

[^1]: [[pe502-castle-cycle-permutations](pages/pe502-castle-cycle-permutations.md)] §"Warm-up: labelled cycles" L5-L8 — "A cycle on n labelled items is a cyclic arrangement - an ordering up to rotation. The number of such directed cycles is (n-1)!, with two standard proofs: 1. Quotient by rotation. n! linear orderings collapse under the free Z/n rotation action, so n!/n = (n-1)! cycles. 2. Fix a starting point. Every cycle can be written uniquely starting with the item labelled 1; the remaining n-1 items order freely, so (n-1)! cycles."
[^2]: [[pe502-castle-cycle-permutations](pages/pe502-castle-cycle-permutations.md)] §"Warm-up: labelled cycles" L10 — "Both proofs are instances of a bigger machine (Foata, sign, cycle-follow) that reappears in PE 502."
[^3]: [[pe502-castle-cycle-permutations](pages/pe502-castle-cycle-permutations.md)] §"Tying back to (n-1)!" L80-L86 — the three-row table "(n-1)! proof move → castle counterpart" mapping divide-by-n / canonical-form / cycle-follow to castle sign / Foata / streak factorization, closing "PE 502 is essentially: take the toolkit that proves (n-1)!, upgrade every step to a version that handles stacked, width-weighted, sign-selected cycles, and you get a closed form plus a fast recurrence."
[^4]: [[pe502-castle-cycle-permutations](pages/pe502-castle-cycle-permutations.md)] §"Connection 1: Castle sign ↔ (1 ± sgn)/2 trick" L40-L42 — "F(w,h) = ½(h^w − (h−1)^w − P(h−1,w) + P(h−2,w)) ... Sanity check for F(4,2): h^w = 16, (h−1)^w = 1, P(1,4) = −4, P(0,4) = 1 from the 16 binary column-height strings, giving F(4,2) = (16 − 1 + 4 + 1)/2 = 10." P(1,4) = 1 − 10 + 5 = −4 (0 runs: 1 config with sign +1; 1 run: 10 configs with sign −1; 2 runs — `1010, 1001, 0101, 1101, 1011` — 5 configs with sign +1; 3+ runs impossible for length 4) and P(0,4) = 1 (only `0000`) re-verified during ingest.
[^5]: [[pe502-castle-cycle-permutations](pages/pe502-castle-cycle-permutations.md)] §"Connection 2: Castle Foata transform ↔ Foata's fundamental transformation" L56 — "For F(4,2) = 10 these are exactly the 10 length-4 binary strings with one positive run: 1000, 0100, 0010, 0001, 1100, 0110, 0011, 1110, 0111, 1111."
[^6]: [[pe502-castle-cycle-permutations](pages/pe502-castle-cycle-permutations.md)] §"Connection 1: Castle sign ↔ (1 ± sgn)/2 trick" L38 — "Weight each castle by (−1)^blocks, splitting the total count T into even- and odd-block halves via (T ± P)/2. This is exactly the (1 ± sgn)/2 trick used to peel A_n out of S_n."
[^7]: [[pe502-castle-cycle-permutations](pages/pe502-castle-cycle-permutations.md)] §"Connection 2" L52-L54 — "Peaks become maximal positive runs, and each peak's 'leader' is the first column of that run - the records of the sequence, in perfect analogy with cycle-leaders as left-to-right maxima. The record set is { i : c_i > 0 and (i = 1 or c_{i-1} = 0) }."
[^8]: [[pe502-castle-cycle-permutations](pages/pe502-castle-cycle-permutations.md)] §"Connection 3: Monotone streak factorization ↔ O(n) cycle-following" L61-L62 — "Take first differences d_i = c_{i+1} − c_i; split into up-runs, flat runs, down-runs. Block count = sum of down-run magnitudes = ∑_i max(0, c_i − c_{i+1}). One linear scan produces the factorization, described on the wiki as 'the castle version of Knuth's O(n) cycle-following loop.'"
[^9]: [[pe502-castle-cycle-permutations](pages/pe502-castle-cycle-permutations.md)] §"The caveat worth flagging" L72-L74 — "Block count ≠ peak count. A tall peak can be several stacked blocks. So the (−1)^blocks sign atom and the peak-count analogue of cycle count are different statistics on the same castle. The Foata bijection is with peaks; the sign is measured on blocks."
[^10]: [[pe502-castle-cycle-permutations](pages/pe502-castle-cycle-permutations.md)] §"Connection 2" L58 — "Ten one-peak castles ↔ single-cycle structural analogue. Note that 3! = 6 ≠ 10: the analogy is one-cycle ↔ one-peak in structure, not in count, because castle rows have arbitrary integer widths while cycles have unit-labelled elements. The correspondence is at the level of factoring, not cardinality."
