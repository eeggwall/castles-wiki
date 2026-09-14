---
title: Castle Foata transform
category: Concepts
summary: The castle analogue of Foata's canonical-cycle flattening — peaks are the maximal positive runs of the column-height sequence, giving #peaks = #records.
tags: [concept, castle, foata, permutations, records, bijection]
sources: [project-euler-502-castle-factoring]
created: 2026-09-13
updated: 2026-09-13
---

# Castle Foata transform

## Description

The **castle Foata transform** is the castle analogue of Foata's fundamental transformation (Knuth's canonical-cycle flattening). In the permutation template, flattening the canonical cycle form makes the cycle leaders the left-to-right records of the resulting one-line permutation, so that the **number of cycles equals the number of left-to-right records**.[^1] (In Knuth's decreasing-order convention the leaders are left-to-right minima; in Foata's increasing-order convention they are left-to-right maxima — the same correspondence, order reversed.[^1] Example: `(1 4)(0 2 3)` flattens to `1 4 0 2 3`, whose left-to-right minima `1` and `0` are one per cycle.[^1])

The castle version is a concrete bijection.[^2] Take the peaks in the order they occur in the tower word (the `R` gaps acting as parentheses) and flatten the tower into its **column-height sequence** `c_1…c_L` — one of the [[castle-representations](pages/castle-representations.md)] — which erases the gap parentheses. The peaks then become visible as the maximal positive runs of `c`:

> **Claim.** A peak `U V D` spans a contiguous interval of columns where `c_i ≥ 1`, and consecutive peaks are separated by at least one column with `c_i = 0`. Hence the peaks, left-to-right, are exactly the maximal positive runs of `c`, and
> ```
> peak ↦ first column of its positive run
> ```
> is a bijection between peaks and the record set `{ i : c_i > 0 and (i = 1 or c_{i−1} = 0) }`.[^2]

That set is the castle's **record statistic**: the left-to-right ascents from the base. The analogy is exact — in permutation Foata a cycle leader is a new record; in castle Foata a peak is a new excursion, a return to positive height after zero.[^3]

## Verification: the F(4,2) = 10 miniature

For height exactly 2 the tower above the base is a single row of blocks, encoded by a length-4 binary string whose runs of 1s are the tower blocks; even total blocks means the tower has an odd number of blocks, i.e. exactly one run. The 10 valid castles have tower column heights:[^4]

```
1000  0100  0010  0001  1100  0110  0011  1110  0111  1111
```

Each has exactly one positive run, hence exactly one peak, and a record set of size one — the castle Foata theorem in miniature.[^4] Re-checked during ingest: all 10 strings have exactly one maximal positive run, each corresponds to a single tower block (odd), and each full castle (heights + 1 for the bottom block) has 2 blocks (even).

## Appearances in Sources

- [[project-euler-502-castle-factoring](pages/project-euler-502-castle-factoring.md)] — states the permutation template, the peak↔positive-run bijection, and the `F(4,2)=10` test.

## Related Concepts

- [[permutation-cycle-castle-analogy](pages/permutation-cycle-castle-analogy.md)] — the analogy this transform instantiates.
- [[castle-representations](pages/castle-representations.md)] — the column-height sequence the transform flattens onto.
- [[castle-sign](pages/castle-sign.md)] — the parity used to select the valid castles in the miniature test.

## Footnotes

[^1]: [[project-euler-502-castle-factoring](pages/project-euler-502-castle-factoring.md)] §"The permutation template" L133-139 — "the cycle leaders are the left-to-right minima ... in Foata's ... presentation ... the left-to-right maxima ... number of cycles = number of left-to-right records ... (1 4)(0 2 3) flattens to 1 4 0 2 3. The left-to-right minima are 1 and 0, one per cycle."
[^2]: [[project-euler-502-castle-factoring](pages/project-euler-502-castle-factoring.md)] §"The castle version" L143-157 — "the peaks ... are exactly the maximal positive runs of c, and the map peak ↦ first column of its positive run is a bijection between peaks and the set { i : c_i > 0 and (i = 1 or c_{i-1} = 0) }."
[^3]: [[project-euler-502-castle-factoring](pages/project-euler-502-castle-factoring.md)] §"The castle version" L157 — "This set is the castle's record statistic: the left-to-right ascents from the base. In permutation Foata, a cycle leader is a new record; in castle Foata, a peak is a new excursion, a return to positive height after zero."
[^4]: [[project-euler-502-castle-factoring](pages/project-euler-502-castle-factoring.md)] §"The castle version" L159-165 — "The 10 valid castles have tower column heights 1000 0100 0010 0001 1100 0110 0011 1110 0111 1111 ... Each has exactly one positive run, hence exactly one peak, and the record set has size one."
