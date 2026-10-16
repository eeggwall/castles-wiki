---
title: "Castles as an upgrade of the (n−1)! cycle count"
category: Analyses
summary: A seminar that starts from the two proofs that there are (n−1)! cycles on n labeled points and follows the source note's pairing of three constructions on permutations with three on castles. The sign and the split (1 ± sgn)/2 go with the sign (−1)^blocks and the split (T ± P)/2 of towers; Foata's canonical-cycle flattening goes with the bijection from peaks to the columns where the skyline leaves the base; Knuth's cycle-following loop goes with the monotone streak scan. All three are checked on the ten even-block castles of width 4 and height 2, A^e(4, 2) = 10, and the pairing differs in two places, peaks against blocks and 10 against 3! = 6.
tags: [analysis, castle, permutations, cycles, seminar, factorization, sign]
sources: [project-euler-502-castle-factoring]
created: 2026-09-15
updated: 2026-10-16
---

# Castles as an upgrade of the (n−1)! cycle count

## The anchor: (n−1)! labeled cycles

A **cycle on `n` labeled points** is a cyclic arrangement, an ordering up to rotation. There are `(n − 1)!` of them, by two proofs:[^1]

1. **Quotient by rotation.** The `n!` linear orderings fall into classes of `n` under rotation, which acts freely, so there are `n!/n = (n − 1)!` cycles.
2. **Fix a starting point.** Every cycle can be written uniquely starting with the point labeled 1, and the other `n − 1` points follow in any order.

The source note reads both proofs as uses of three constructions on permutations, the sign, Foata's flattening and Knuth's cycle-following loop, and pairs each with a construction on castles.[^2]

## The three pairs

The source pairs the steps as follows:[^3]

| step in the `(n − 1)!` proofs | construction on permutations | construction on castles |
|---|---|---|
| divide by `n` | the sign `sgn(σ) = (−1)^{n−c}` and the split `(1 ± sgn)/2` into even and odd permutations | the sign `(−1)^{blocks}` and the split `(T ± P)/2` of towers into even-block and odd-block ones ([[castle-sign](pages/castle-sign.md)]) |
| fix a starting point | Foata's flattening of the canonical cycle form, with cycles becoming left-to-right records | the bijection from peaks to the columns where the skyline leaves the base ([[castle-foata-transform](pages/castle-foata-transform.md)]) |
| follow the cycles | Knuth's `O(n)` loop following `i ↦ σ(i)` | the `O(L)` scan of the first differences into up-streaks, flat runs and down-streaks ([[monotone-streak-factorization](pages/monotone-streak-factorization.md)]) |

The objects change: `n` labeled points become `L` columns of height at most `k`, cycles become peaks, the productions `U V D` at the base of the [[generalized-dyck-grammar](pages/generalized-dyck-grammar.md)], and the sign counts blocks instead of `n − c` ([[permutation-cycle-castle-analogy](pages/permutation-cycle-castle-analogy.md)]).

## The hand check: A^e(4, 2) = 10

The [[castle-counting-formula](pages/castle-counting-formula.md)] gives, for `h ≥ 2`,[^4]

```
A^e(w, h)  =  [ h^w − (h−1)^w − P(h−1, w) + P(h−2, w) ] / 2.
```

At `(w, h) = (4, 2)`: `h^w = 16`, `(h − 1)^w = 1`, `P(0, 4) = 1`, the empty tower, and `P(1, 4) = −4`. The towers of height at most 1 on a base of length 4 are the 16 binary strings of length 4, each run of 1s one block: one string has no run, 10 have one run and 5 have two (`1010, 1001, 0101, 1101, 1011`), so `P(1, 4) = 1 − 10 + 5 = −4`. Substituting,

```
A^e(4, 2)  =  (16 − 1 + 4 + 1) / 2  =  10.
```

Directly: the bottom row is one block, so an even-block castle of height 2 stands on towers with an odd number of blocks, and at width 4 that means one run of 1s, since three runs need width at least 5. The ten strings are `1000, 0100, 0010, 0001, 1100, 0110, 0011, 1110, 0111, 1111`.[^5] At width 5 the three-run string `10101` is added, and `A^e(5, 2) = C(6, 2) + C(6, 6) = 16`; in general `A^e(w, 2) = Σ_j C(w+1, 4j+2) = A038505(w+1)` ([[castle-counting-function](pages/castle-counting-function.md)]).

Each of the three pairs can be checked on these ten castles:

- **The sign.** The towers with an odd number of blocks number `(T(1, 4) − P(1, 4))/2 = (16 + 4)/2 = 10`, and they are the towers of the even-block castles of height at most 2; the flat row `(1, 1, 1, 1)` stands on the string `0000`, with no block, so it is not among them.[^6]
- **Foata.** Each of the ten strings has one maximal run of 1s, so one peak and one record.[^7]
- **The streak scan.** With `c_0 = c_5 = 0`, the first differences of each string have one up-streak and one down-streak, each of size 1, and are otherwise 0, so the total descent is 1, one block above the bottom row.[^8]

## Where the pairs differ

**Blocks are not peaks.** One peak can carry several stacked blocks: the towers `(2, 1)` form one peak with two blocks. So the sign `(−1)^{blocks}` and the peak count, the counterpart of the cycle count, are different statistics on the same castle. The Foata bijection is with peaks, and the sign is measured on blocks.[^9]

**The pairing is of constructions, not of counts.** There are 10 one-peak towers on a base of length 4 and `3! = 6` one-cycle permutations of 4 points: the blocks of a castle have any integer width, while the points of a cycle are single labeled elements.[^10]

## Seminar outline

1. The two proofs of `(n − 1)!`.
2. The three pairs of constructions, one row of the table each.
3. `A^e(4, 2) = 10` by the formula and by listing the ten castles, with each pair checked on them.
4. Where the pairs differ: blocks against peaks, and 10 against `3! = 6`.

## Appearances in Sources

- [[project-euler-502-castle-factoring](pages/project-euler-502-castle-factoring.md)] - the three constructions on castles: the sign, the castle Foata transform and the monotone streak factorization, each set beside a construction on permutations.

## Related Concepts

- [[permutation-cycle-castle-analogy](pages/permutation-cycle-castle-analogy.md)] - the pairing of constructions on permutations and on towers, with definitions on both sides.
- [[castle-sign](pages/castle-sign.md)] - the sign `(−1)^{blocks}` and the split `(T ± P)/2`.
- [[castle-foata-transform](pages/castle-foata-transform.md)] - the bijection from peaks to records.
- [[monotone-streak-factorization](pages/monotone-streak-factorization.md)] - the up-streaks, flat runs and down-streaks of the first differences.
- [[castle-counting-formula](pages/castle-counting-formula.md)] - the formula for `A^e(w, h)` used in the hand check.
- [[generalized-dyck-grammar](pages/generalized-dyck-grammar.md)] - the grammar of tower words, whose productions `U V D` at the base are the peaks.
- [[aocp-multisets](pages/aocp-multisets.md)] - Knuth's two-line arrays and the cycle factorization of multiset permutations.
- [[aocp-permutations](pages/aocp-permutations.md)] - Knuth's treatment of the permutations of `n` points and their count `n!`.

## Footnotes

[^1]: raw/pe502-castle-cycle-permutations.md §"Warm-up: labelled cycles" L5-8 - "A cycle on n labelled items is a cyclic arrangement - an ordering up to rotation. The number of such directed cycles is (n-1)!, with two standard proofs: 1. Quotient by rotation. n! linear orderings collapse under the free Z/n rotation action, so n!/n = (n-1)! cycles. 2. Fix a starting point. Every cycle can be written uniquely starting with the item labelled 1; the remaining n-1 items order freely, so (n-1)! cycles."
[^2]: raw/pe502-castle-cycle-permutations.md §"Warm-up: labelled cycles" L10 - "Both proofs are instances of a bigger machine (Foata, sign, cycle-follow) that reappears in PE 502."
[^3]: raw/pe502-castle-cycle-permutations.md §"Tying back to (n-1)!" L80-84 - the table "(n-1)! proof move / Castle counterpart": "divide by n (quotient by rotation) | castle sign / signed-count halving", "canonical form starting from element 1 | castle Foata: canonical form starting from each peak's leftmost positive column", "cycle-follow the permutation to read off cycles | monotone streak scan to read off peaks".
[^4]: raw/pe502-castle-cycle-permutations.md §"Connection 1: Castle sign ↔ (1 ± sgn)/2 trick" L40-42 - "F(w,h) = ½(h^w − (h−1)^w − P(h−1,w) + P(h−2,w))", "Sanity check for F(4,2): h^w = 16, (h−1)^w = 1, P(1,4) = −4, P(0,4) = 1 from the 16 binary column-height strings, giving F(4,2) = (16 − 1 + 4 + 1)/2 = 10." The note writes `F` for `A^e`. The split of the 16 strings by runs (1, 10 and 5 strings with 0, 1 and 2 runs) recomputed by execution (Python 3.11, 2026-10-16).
[^5]: raw/pe502-castle-cycle-permutations.md §"Connection 2: Castle Foata transform ↔ Foata's fundamental transformation" L56 - "For F(4,2) = 10 these are exactly the 10 length-4 binary strings with one positive run: 1000, 0100, 0010, 0001, 1100, 0110, 0011, 1110, 0111, 1111."
[^6]: raw/pe502-castle-cycle-permutations.md §"Connection 1: Castle sign ↔ (1 ± sgn)/2 trick" L38 - "Weight each castle by (−1)^blocks, splitting the total count T into even- and odd-block halves via (T ± P)/2. This is exactly the (1 ± sgn)/2 trick used to peel A_n out of S_n."
[^7]: raw/pe502-castle-cycle-permutations.md §"Connection 2" L52-54 - "Peaks become maximal positive runs, and each peak's \"leader\" is the first column of that run", "The record set is {i : c_i > 0 and (i = 1 or c_{i-1} = 0)}."
[^8]: raw/pe502-castle-cycle-permutations.md §"Connection 3: Monotone streak factorization ↔ O(n) cycle-following" L62 - "Take first differences d_i = c_{i+1} − c_i; split into up-runs, flat runs, down-runs. Block count = sum of down-run magnitudes = ∑_i max(0, c_i − c_{i+1}). One linear scan produces the factorization".
[^9]: raw/pe502-castle-cycle-permutations.md §"The caveat worth flagging" L72 - "Block count ≠ peak count. A tall peak can be several stacked blocks. So the (−1)^blocks sign atom and the peak-count analogue of cycle count are different statistics on the same castle. The Foata bijection is with peaks; the sign is measured on blocks."
[^10]: raw/pe502-castle-cycle-permutations.md §"Connection 2" L58 - "Note that 3! = 6 ≠ 10: the analogy is one-cycle ↔ one-peak in structure, not in count, because castle rows have arbitrary integer widths while cycles have unit-labelled elements. The correspondence is at the level of factoring, not cardinality."
