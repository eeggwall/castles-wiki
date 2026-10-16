---
title: Castle Foata transform
category: Concepts
summary: The castle counterpart of Foata's fundamental transformation. Flattening a permutation's canonical cycle form turns its cycles into left-to-right records; flattening a tower word to its column heights turns its peaks, the blocks of the first row above the base with what they carry, into the maximal runs of positive heights, and sending each peak to the first column of its run is a bijection onto the columns where the skyline leaves the base. So the number of peaks equals the number of these records. Peaks and blocks are different statistics.
tags: [concept, castle, foata, permutations, records, bijection]
sources: [project-euler-502-castle-factoring]
created: 2026-09-13
updated: 2026-10-16
---

# Castle Foata transform

## Foata's fundamental transformation

Write a permutation in **canonical cycle form**. In Knuth's convention every cycle, singletons included, is written with its smallest element first, and the cycles are listed in decreasing order of their first elements. Erasing the parentheses gives a one-line permutation, and the cycles of the original are recovered by cutting before each left-to-right minimum of the result, so the flattening is a bijection on the permutations of `n` points, **Foata's fundamental transformation**, and the number of cycles of a permutation is the number of left-to-right minima of its flattening. In Foata's own convention each cycle is written with its largest element first and the cycles in increasing order of their first elements, and the cycle leaders become the left-to-right maxima.[^1]

*Example.* The permutation `2 4 3 0 1` of `{0, …, 4}` has the cycles `(0 2 3)(1 4)`, canonical form `(1 4)(0 2 3)`, and flattening `1 4 0 2 3`, whose left-to-right minima `1` and `0` are one per cycle.[^2]

Knuth finds the cycles by following `i ↦ σ(i)` from an unvisited element until it returns, which gives disjoint cycles because `σ` is a bijection.[^3] The source sets this construction beside one on castles: the [[generalized-dyck-grammar](pages/generalized-dyck-grammar.md)] writes the towers on a base as a word in which the **peaks**, the productions `U V D` at the base, are separated by `R` gaps, as the cycles of a canonical cycle form are separated by parentheses.[^4] [[permutation-cycle-castle-analogy](pages/permutation-cycle-castle-analogy.md)] states the pairing of the two sides.

## The castle Foata transform

The castle side takes four steps.[^5]

1. **The tower word.** Removing the bottom row of a castle leaves towers, written as a word in `U` (up one row), `R` (one column, at its height) and `D` (down one row) ([[castle-representations](pages/castle-representations.md)]). The castle's own word is `U (towers) D`, with the outer `U … D` for the bottom row. A peak is a production `U V D` at the base: one block in the first row above the base, together with the towers `V` it carries.
2. **Flatten to column heights.** Reading the height above the base at each column gives the tuple `c = (c_1, …, c_L)`, with `c_i ≥ 0`; the `R` gaps between peaks become columns with `c_i = 0`.
3. **Peaks are positive runs.** A peak spans a run of consecutive columns with `c_i ≥ 1`, and consecutive peaks are separated by at least one column with `c_i = 0`. So the peaks, from left to right, are the maximal runs of positive entries of `c`.
4. **Peak ↦ first column of its run.** Sending each peak to the first column of its run is a bijection from the peaks onto the **record set**

   ```
   { i : c_i > 0 and (i = 1 or c_{i−1} = 0) },
   ```

   the columns at which the skyline leaves the base.

Hence **the number of peaks equals the number of records**.[^5][^6] In the castle itself, with column heights `c_i + 1`, a peak is a maximal run of columns of height at least 2.

## Example 1: one peak

The castle `(2, 2, 1)` of width 3 and height 2 leaves the towers `c = (1, 1, 0)`: one block of width 2 in the first row above the base. Its tower word, with one `R` per column at the column's height, is `URRDR`, with one `D`, one block, matching the total descent `Σ_{i=0}^{L} max(0, c_i − c_{i+1}) = 1` with `c_0 = c_{L+1} = 0`.[^7] The castle's word is `U URRDR D = UURRDRD`, with 2 blocks. The tuple `c` has one maximal positive run, columns 1 to 2, which is the one peak, and its first column 1 is the one record.

## Example 2: two peaks and four blocks

The castle `(3, 2, 1, 3, 2)` of width 5 and height 3 leaves the towers

```
c = (2, 1, 0, 2, 1),
```

two peaks, at columns 1 to 2 and 4 to 5, each a block of width 2 carrying a block of width 1 on its left column. The tower word is `UURDRDRUURDRD`, with four `D`, four blocks, matching the total descent `1 + 1 + 0 + 1 + 1 = 4`.[^7] The castle's word is `UUURDRDRUURDRDD`, with 5 blocks. The maximal positive runs of `c` are `{1, 2}` and `{4, 5}`, and the records are columns 1 and 4 (`c_4 = 2 > 0` with `c_3 = 0`); the bijection sends the two peaks to them.

The two peaks hold four blocks: a peak can carry several stacked blocks, so the number of peaks and the number of blocks are different statistics, and the transform counts peaks.[^8]

## The ten even-block castles of width 4 and height 2

A castle of height 2 stands on towers of height at most 1, a binary string whose runs of 1s are the blocks in row 2. The castle has an even number of blocks when the string has an odd number of runs, and at width 4 that means one run, since three runs need width at least 5. So the `A^e(4, 2) = 10` even-block castles stand on the strings `1000, 0100, 0010, 0001, 1100, 0110, 0011, 1110, 0111, 1111`, and each has one peak and one record.[^9] In general `A^e(w, 2) = Σ_j C(w+1, 4j+2) = A038505(w+1)` ([[castle-counting-function](pages/castle-counting-function.md)]).

## Appearances in Sources

- [[project-euler-502-castle-factoring](pages/project-euler-502-castle-factoring.md)] - Knuth's canonical cycle form and Foata's convention, the bijection from peaks to the first columns of the positive runs, and the ten castles of width 4 and height 2.

## Related Concepts

- [[permutation-cycle-castle-analogy](pages/permutation-cycle-castle-analogy.md)] - the pairing of constructions on permutations and on towers, of which this transform is the canonical form and records.
- [[generalized-dyck-grammar](pages/generalized-dyck-grammar.md)] - the grammar of tower words, whose productions `U V D` at the base are the peaks.
- [[castle-representations](pages/castle-representations.md)] - the step-word and column-height encodings the transform passes between.
- [[castle-sign](pages/castle-sign.md)] - the block count as total descent, used to check the examples.
- [[deutsch-elizalde-2017-bargraphs-dyck-paths](pages/deutsch-elizalde-2017-bargraphs-dyck-paths.md)] - uses "peak" for a plateau `U H^ℓ D` higher than both neighbors, a different statistic: the castle `(3, 2, 3)` has one peak here and two there.
- [[prime-castles](pages/prime-castles.md)] - cut at their height-1 columns, castles factor into primes, and the peaks are the nontrivial prime factors.
- [[signed-prime-castles](pages/signed-prime-castles.md)] - peaks and records are additive over prime factors; left-to-right maxima are not.
- [[aocp-multisets](pages/aocp-multisets.md)] - Foata's intercalation product and the cycle factorization of multiset permutations, from TAOCP Vol. 3.
- [[castles-as-upgraded-cycle-count](pages/castles-as-upgraded-cycle-count.md)] - a seminar that builds the sign, this transform and the streak factorization from the proofs that there are `(n − 1)!` cycles on `n` labeled points.
- [[castle-samplers](pages/castle-samplers.md)] - samplers on both sides: the cycle count of a random permutation has mean `H_n`, and the peak count of a random castle grows linearly in the width.

## Footnotes

[^1]: [[project-euler-502-castle-factoring](pages/project-euler-502-castle-factoring.md)] §"The permutation template" L133-137 - "Knuth's canonical-cycle flattening is Foata's fundamental transformation. In Knuth's decreasing order the cycle leaders are the left-to-right minima of the flattened permutation; in Foata's more common presentation each cycle is written with its maximum first and the cycles are ordered increasingly, and then the leaders are the left-to-right maxima", "number of cycles = number of left-to-right records"; raw/pe502-castle-cycle-permutations.md §"Connection 2" L50 - "Parentheses recover from left-to-right maxima."
[^2]: [[project-euler-502-castle-factoring](pages/project-euler-502-castle-factoring.md)] §"Knuth canonical cycle form" L21-25 - "writing every singleton cycle explicitly; putting the smallest element first within each cycle; ordering the cycles in decreasing order of their first element", "the linear permutation (2 4 3 0 1) has cycles (0 2 3)(1 4), so its canonical form is (1 4)(0 2 3). Erasing the parentheses recovers a one-line permutation, (1 4 0 2 3)"; §"The permutation template" L139 - "The left-to-right minima are 1 and 0, one per cycle."
[^3]: [[project-euler-502-castle-factoring](pages/project-euler-502-castle-factoring.md)] §"Knuth canonical cycle form" L27 - "The factorization is the loop i ↦ σ(i): start at an unvisited element and follow the map until it closes. The cycles are disjoint because the map is a bijection."
[^4]: [[project-euler-502-castle-factoring](pages/project-euler-502-castle-factoring.md)] §"Castle Factoring and the Knuth-Castle Foata Transform" L7 - "each U V D peak leaves the base, lives entirely above a sub-block, and returns to the same level, and disjoint peaks are separated by R gaps".
[^5]: [[project-euler-502-castle-factoring](pages/project-euler-502-castle-factoring.md)] §"The castle version" L143-155 - "Put the peaks in canonical order left-to-right, i.e. in the order they occur in the tower word, with the R gaps acting as the parentheses", "A peak U V D spans a contiguous interval of columns on which c_i ≥ 1, and consecutive peaks are separated by at least one column with c_i = 0", "peak ↦ first column of its positive run is a bijection between peaks and the set { i : c_i > 0 and (i = 1 or c_{i-1} = 0) }".
[^6]: [[project-euler-502-castle-factoring](pages/project-euler-502-castle-factoring.md)] §"The castle version" L157 - "This set is the castle's record statistic: the left-to-right ascents from the base."
[^7]: [[project-euler-502-castle-factoring](pages/project-euler-502-castle-factoring.md)] §"The sign of a castle" L104-108 - "In the column-height form, the block count is the total descent: blocks = ∑_{i=0}^{L} max(0, c_i - c_{i+1}), c_0 = c_{L+1} = 0". The tower words and block counts of both examples recomputed by execution (Python 3.11, 2026-10-16).
[^8]: [[project-euler-502-castle-factoring](pages/project-euler-502-castle-factoring.md)] §"The tower grammar" L68 - "The excursion count (peaks) plays the role of the cycle count, while the block count plays the role of the sign atom. One peak may contain several stacked blocks, so these are distinct."
[^9]: [[project-euler-502-castle-factoring](pages/project-euler-502-castle-factoring.md)] §"The castle version" L159-165 - "The 10 valid castles have tower column heights 1000 0100 0010 0001 1100 0110 0011 1110 0111 1111 ... Each has exactly one positive run, hence exactly one peak, and the record set has size one."
