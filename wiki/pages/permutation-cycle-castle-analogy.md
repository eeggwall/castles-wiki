---
title: Permutation-cycle / castle-peak analogy
category: Concepts
summary: A permutation factors uniquely into disjoint cycles, and the towers on a castle's bottom row factor uniquely into peaks, the blocks of the first row above the base with the towers they carry, separated by gap columns (the Dyck first-return decomposition with the extra letter R). The castle-factoring source builds four constructions on each side of this pairing - the sign (−1)^{n−c} beside (−1)^{blocks}, the even/odd split (1 ± sign)/2, Knuth's canonical cycle form beside the column-height word, and cycle following beside the streak scan. The pairing matches constructions, not objects - one-peak towers on a base of length 4 number 10, one-cycle permutations of 4 points 3! = 6 - and the sign of towers depends on their blocks, which can outnumber their peaks.
tags: [concept, castle, permutations, cycles, factorization, dyck]
sources: [project-euler-502-castle-factoring]
created: 2026-09-13
updated: 2026-10-16
---

# Permutation-cycle / castle-peak analogy

## The two factorizations

A permutation `σ` of `{0, …, n − 1}` factors uniquely into disjoint cycles, found by following `i ↦ σ(i)` from an element not yet visited until the loop closes; the cycles are disjoint because `σ` is a bijection.[^1] Towers on a base of length `L` factor uniquely into **peaks**: in the tower grammar of [[generalized-dyck-grammar](pages/generalized-dyck-grammar.md)], a peak is a production `U V D` at the base, one block in the first row above the base together with the towers `V` it carries, and consecutive peaks are separated by gap columns `R`. In the column heights `c = (c_1, …, c_L)` of the towers, the peaks are the maximal runs of columns with `c_i ≥ 1`. The source calls this "a genuine factorization, not a metaphor": it is the Dyck first-return decomposition with the extra letter `R`.[^2]

*Example.* The towers `(1, 0, 2, 1)`, under the castle `(2, 1, 3, 2)`, have two peaks, the runs `(1)` and `(2, 1)`, and three blocks, since the second peak carries one block on another.

## The paired constructions

The castle-factoring source pairs the two factorizations and builds the same constructions on both sides ([[project-euler-502-castle-factoring](pages/project-euler-502-castle-factoring.md)]):[^2][^3]

| construction | permutation `σ` of `n` points with `c` cycles | towers `c` on a base of length `L` |
|---|---|---|
| factors | the cycles | the peaks, the maximal runs with `c_i ≥ 1` |
| number of factors | `c` | the number of peaks |
| sign | `sgn(σ) = (−1)^{n−c}` | `(−1)^{blocks(c)}`, with `blocks(c) = Σ_i max(0, c_i − c_{i−1})`, `c_0 = 0` ([[castle-sign](pages/castle-sign.md)]) |
| even/odd split | `(n! ± Σ_σ sgn(σ))/2` | `(T(k, L) ± P(k, L))/2` |
| canonical form | Knuth's canonical cycle form, flattened ([[castle-foata-transform](pages/castle-foata-transform.md)]) | the column-height word `c_1 … c_L` |
| records | the cycle leaders, the left-to-right minima of the flattened form | the first columns of the peaks, `{i : c_i > 0 and (i = 1 or c_{i−1} = 0)}` |
| linear scan | following `i ↦ σ(i)`, `O(n)` | splitting the first differences `c_{i+1} − c_i` into up-streaks, flat runs and down-streaks, `O(L)` ([[monotone-streak-factorization](pages/monotone-streak-factorization.md)]) |

Knuth's canonical cycle form (The Art of Computer Programming, Vol. 1, §1.3.3) writes every singleton cycle, puts the smallest element first in each cycle, and orders the cycles by decreasing first element. The source's example is the permutation `2 4 3 0 1` in one-line form, with cycles `(0 2 3)(1 4)` and canonical form `(1 4)(0 2 3)`; erasing the parentheses gives `1 4 0 2 3`, whose left-to-right minima `1` and `0` lead the two cycles.[^4]

Two features keep the pairing from being an isomorphism.

- **It matches constructions, not objects.** The towers of height at most 1 on a base of length 4 with one peak are the ten binary strings with one run of 1s, while the permutations of 4 points with one cycle number `3! = 6`. The source puts this as a correspondence "at the level of factoring, not cardinality".[^5]
- **The sign is measured on blocks, not on peaks.** The sign of a permutation depends only on its number of cycles, but one peak can carry several stacked blocks, so the sign of towers is not determined by their number of peaks: in the example, two peaks and three blocks.[^3]

## The (n−1)! proofs

The cycles on `n` labeled points number `(n − 1)!`, by two proofs: the `n!` orderings fall into classes of `n` under rotation, or every cycle can be written starting at the point 1. The source note reads both proofs as uses of the constructions of the section *The paired constructions* and pairs each step with the castle construction it corresponds to; [[castles-as-upgraded-cycle-count](pages/castles-as-upgraded-cycle-count.md)] develops that reading as a seminar.[^6]

## Castles that are permutations

A **rainbow castle** has width `h` and the heights `1, …, h` in some order ([[castle-classification-shape](pages/castle-classification-shape.md)]), so its skyline is a permutation in one-line form, and the permutation constructions apply to it as a permutation. The two signs then differ: the rainbow castle `(2, 3, 1)` is the cyclic permutation `1 ↦ 2 ↦ 3 ↦ 1`, with one cycle and sign `+1`, while the castle has three blocks and sign `−1`.

The word "peak" means something else on [[castle-classification-shape](pages/castle-classification-shape.md)], where the even-peak type counts local maxima of the skyline: the castle `(2, 3, 2, 3, 2)` stands on the towers `(1, 2, 1, 2, 1)`, which form one peak, and has two local maxima.

## Height 2: peaks and the even-block count

A castle of height 2 has one block in the bottom row and one block for each run of 1s in its row 2, the peaks of its towers. So it has an even number of blocks exactly when its towers have an odd number of peaks, and the binary strings of length `w` with `r` runs of 1s number `C(w + 1, 2r)`:[^7]

```
A^e(w, 2)  =  Σ_{s≥0} C(w + 1, 4s + 2)  =  A038505(w + 1)
```

([[hyperbolic-sequence-family](pages/hyperbolic-sequence-family.md)]). At `w = 4` only one run fits among the odd numbers of runs, so the ten even-block castles of the example `A^e(4, 2) = 10` on [[castle-counting-formula](pages/castle-counting-formula.md)] are the one-peak towers, `C(5, 2) = 10`. At `w = 5` the three-run string `10101` joins them, and `A^e(5, 2) = C(6, 2) + C(6, 6) = 16`.

## Appearances in Sources

- [[project-euler-502-castle-factoring](pages/project-euler-502-castle-factoring.md)] - the pairing of cycles with peaks, the correspondence table, and Knuth's canonical cycle form with its example.

## Related Concepts

- [[generalized-dyck-grammar](pages/generalized-dyck-grammar.md)] - the tower grammar, whose productions `U V D` at the base are the peaks.
- [[castle-sign](pages/castle-sign.md)] - the sign `(−1)^{blocks}` and the split `(T ± P)/2`, set beside the sign of a permutation.
- [[castle-foata-transform](pages/castle-foata-transform.md)] - the bijection from peaks to their first columns, set beside Foata's transformation.
- [[monotone-streak-factorization](pages/monotone-streak-factorization.md)] - the streak scan of the first differences, set beside cycle following.
- [[castles-as-upgraded-cycle-count](pages/castles-as-upgraded-cycle-count.md)] - a seminar that builds these constructions from the two proofs of `(n − 1)!`.
- [[castle-classification-shape](pages/castle-classification-shape.md)] - the rainbow castles and the even-peak type.
- [[aocp-multisets](pages/aocp-multisets.md)] - Knuth's two-line arrays and the cycle factorization of permutations of multisets.
- [[permutation-inversions](pages/permutation-inversions.md)] and [[aocp-combinatorics](pages/aocp-combinatorics.md)] - inversions, the permutation statistic graded by the q-factorial `Π_k (1 − z^k)/(1 − z)^n`.
- [[hyperbolic-sequence-family](pages/hyperbolic-sequence-family.md)] - the sums of every fourth binomial coefficient, among them `A038505`.
- [[block-count-constraints](pages/block-count-constraints.md)] - castles selected by block count, with the even-block condition as the residue class 0 modulo 2.
- [[parity-via-roots-of-unity](pages/parity-via-roots-of-unity.md)] - the split by block count modulo `m`.

## Footnotes

[^1]: [[project-euler-502-castle-factoring](pages/project-euler-502-castle-factoring.md)] §"Knuth canonical cycle form" L27 - "The factorization is the loop i ↦ σ(i): start at an unvisited element and follow the map until it closes. The cycles are disjoint because the map is a bijection."
[^2]: [[project-euler-502-castle-factoring](pages/project-euler-502-castle-factoring.md)] §"Castle Factoring and the Knuth-Castle Foata Transform" L7 and §"The tower grammar" L43 - "each U V D peak leaves the base, lives entirely above a sub-block, and returns to the same level, and disjoint peaks are separated by R gaps. This is a genuine factorization, not a metaphor: it is the Dyck first-return decomposition with one extra letter (R)", and "Disjoint peaks are separated by R gaps, exactly as disjoint cycles are separated by parentheses."
[^3]: [[project-euler-502-castle-factoring](pages/project-euler-502-castle-factoring.md)] §"The tower grammar" L45-68 [synthesis] - the correspondence table (disjoint cycle and disjoint peak, number of cycles and number of peaks, `(−1)^{n−c}` and `(−1)^{blocks}`) and "One peak may contain several stacked blocks, so these are distinct."
[^4]: [[project-euler-502-castle-factoring](pages/project-euler-502-castle-factoring.md)] §"Knuth canonical cycle form" L19-25 - "writing every singleton cycle explicitly; putting the smallest element first within each cycle; ordering the cycles in decreasing order of their first element", "the linear permutation (2 4 3 0 1) has cycles (0 2 3)(1 4), so its canonical form is (1 4)(0 2 3). Erasing the parentheses recovers a one-line permutation, (1 4 0 2 3)." The left-to-right minima checked by execution (Python 3.11, 2026-10-16).
[^5]: raw/pe502-castle-cycle-permutations.md §"Connection 2: Castle Foata transform ↔ Foata's fundamental transformation" L56-58 - "For F(4,2) = 10 these are exactly the 10 length-4 binary strings with one positive run", "Note that 3! = 6 ≠ 10: the analogy is one-cycle ↔ one-peak in structure, not in count ... The correspondence is at the level of factoring, not cardinality."
[^6]: raw/pe502-castle-cycle-permutations.md §"Warm-up: labelled cycles" L5-10 and §"Tying back to (n-1)!" L76-86 [synthesis] - the two proofs of `(n − 1)!`, "Both proofs are instances of a bigger machine (Foata, sign, cycle-follow) that reappears in PE 502", and the table pairing each proof step with a castle construction.
[^7]: Verified by execution (Python 3.11, 2026-10-16): the peaks and blocks of `(1, 0, 2, 1)`; ten one-peak strings of length 4; `A^e(5, 2) = 16` by enumeration; one peak and two local maxima for `(2, 3, 2, 3, 2)`; three blocks for `(2, 3, 1)`. `A^e(w, 2) = Σ_s C(w + 1, 4s + 2)` by enumeration for `w ≤ 10`.
