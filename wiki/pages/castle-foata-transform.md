---
title: Castle Foata transform
category: Concepts
summary: The castle analogue of Foata's canonical-cycle flattening — peaks are the maximal positive runs of the column-height sequence, giving #peaks = #records. The Foata upgrade in the [[castles-as-upgraded-cycle-count]] triad — paralleling "largest element = cycle leader" with "leftmost positive column = peak leader."
tags: [concept, castle, foata, permutations, records, bijection]
sources: [project-euler-502-castle-factoring, pe502-castle-cycle-permutations]
created: 2026-09-13
updated: 2026-09-19
---

# Castle Foata transform

## What Foata refers to

**Foata's fundamental transformation** is a classical bijection on permutations, also known as Knuth's *canonical-cycle flattening*.[^1] Take a permutation written in **canonical cycle form** — every cycle written with its smallest element first, the cycles ordered by their first elements — and erase the parentheses. Read as a one-line permutation, the result is a different permutation, and the two are related by a single clean statistic: **the number of cycles of the original equals the number of left-to-right records of the flattened permutation**.[^1] (In Knuth's decreasing-first-element convention the cycle leaders become left-to-right *minima*; in Foata's increasing convention they become left-to-right *maxima* — the same correspondence, order reversed.[^1])

Example: the canonical cycle form `(1 4)(0 2 3)` flattens to the one-line permutation `1 4 0 2 3`, whose left-to-right minima `1` and `0` are one per cycle.[^1]

A castle is not a permutation, but its skyline factors into cycle-like atoms — the **peaks** of the [[permutation-cycle-castle-analogy](pages/permutation-cycle-castle-analogy.md)] — so the same flattening carries over, with a peak playing the role of a cycle and a "new excursion from the base" playing the role of a record. The rest of this page makes that exact.

## The Knuth connection

The flattening is Knuth's, from *The Art of Computer Programming* Vol. 1, §1.3.3 ("An Unusual Correspondence"), and it is the source side of the castle's central analogy.[^2] Knuth factors a permutation into disjoint cycles by following the map `i ↦ σ(i)` from an unvisited element until the loop closes; the cycles are disjoint because `σ` is a bijection.[^3] Presenting those cycles canonically — smallest element first, decreasing first-element order, singletons written explicitly — and then erasing the parentheses is precisely Foata's transformation.[^2]

On the castle side, the [[generalized-dyck-grammar](pages/generalized-dyck-grammar.md)] factors a tower word the same way: each `U V D` **peak** is a self-contained excursion above one sub-block, and disjoint peaks are separated by `R` gaps exactly as disjoint cycles are separated by parentheses.[^4] So the permutation's *cycles* become the castle's *peaks*, and the flattening that turns cycles into records becomes a flattening that turns peaks into records — the castle Foata transform below. The full correspondence table lives on [[permutation-cycle-castle-analogy](pages/permutation-cycle-castle-analogy.md)].

## The castle Foata transform

The transform is a concrete bijection in four steps.[^5]

1. **Start from the tower word** — the `U`/`R`/`D` string of the skyline *above* the base (the [[castle-representations](pages/castle-representations.md)] step-string form). A castle is `U (tower) D`: the outer `U…D` pair is the **single full-width base block**, and the tower word traces only what sits on top of it. The peaks (the `U V D` excursions) are the cycle-like atoms; the `R` gaps between them are the parentheses.
2. **Flatten to column heights.** Erase the gaps by reading off the height above the base at each column: the integer tuple `c_1…c_L` (the [[castle-representations](pages/castle-representations.md)] column-height form). This is the castle analogue of erasing the parentheses.
3. **Peaks are positive runs.** In `c`, a peak `U V D` spans exactly the contiguous columns where `c_i ≥ 1`, and consecutive peaks are separated by at least one column with `c_i = 0`. So the peaks, left to right, are precisely the **maximal positive runs** of `c`.[^5]
4. **Peak ↦ first column of its run.** The map
   ```
   peak ↦ first column of its positive run
   ```
   is a bijection between peaks and the **record set**
   ```
   { i : c_i > 0 and (i = 1 or c_{i−1} = 0) }
   ```
   — the columns where the skyline leaves the base, i.e. its left-to-right ascents.[^5]

Hence **#peaks = #records**: the number of cycle-like atoms equals the number of new excursions from the base, exactly as permutation cycles correspond to left-to-right records.[^5][^6]

## Worked example 1: a single block

Consider a castle of width 3 and height 2 whose tower (the part above the base) is one block of width 2. Its **tower** column heights are

```
c = (1, 1, 0)
```

Reading the skyline above the base column by column — up to height 1 (`U`), right (`R`); unchanged, right (`R`); down to 0 (`D`), right (`R`) — gives the tower word `URRDR`, with one `U` and one `D` (one tower block, matching the descent count `∑ max(0, c_i − c_{i+1}) = 1`).[^7] The **full castle** wraps this in the base block: `U URRDR D` = `UURRDRD`. Its outer `U…D` pair is the single full-width base block (row 1, all three columns), and the tower block sits on top at columns 1–2 — a valid castle of 2 blocks.

Flattened, `c` has a single maximal positive run `{1, 2}` (columns 1–2, both `≥ 1`). That run is the one peak. Its first column, 1, is the unique record: `c_1 = 1 > 0` and `i = 1`.

So **one peak ↔ one record** — the castle Foata theorem in its simplest form.

## Worked example 2: two independent towers

Now a castle of width 5 and height 3 whose tower holds two **independent towers** side by side: one at columns 1–2 and one at columns 4–5, separated by the one-column gap at column 3. Each tower is a width-2 block with a width-1 block stacked on its left column. The tower column heights are

```
c = (2, 1, 0, 2, 1)
```

The tower word is `UURDRDRUURDRD` (the columns change by `+2, −1, −1, +2, −1`), with four `U`s and four `D`s — four tower blocks, matching the descent count `max(0,2−1) + max(0,1−0) + max(0,2−1) + max(0,1−0) = 4`.[^7] The **full castle** is `U UURDRDRUURDRD D` = `UUURDRDRUURDRDD`: the outer `U…D` is the single full-width base block (row 1, all five columns), and the two towers sit on top of it — a valid castle of 5 blocks.

Flattened, `c` has two maximal positive runs: `{1, 2}` and `{4, 5}` — the two towers. The records are the first columns of these runs: column 1, and column 4 (`c_4 = 2 > 0` with `c_3 = 0`). The bijection sends peak `{1, 2}` ↦ 1 and peak `{4, 5}` ↦ 4:

**two peaks ↔ two records.**

These two peaks are genuinely independent towers — each a self-contained excursion that leaves the base, stacks two blocks, and returns. Note that there are **two peaks but four blocks**: a peak can hold several stacked blocks, so peaks and blocks are different statistics, and the transform counts *peaks* (= records), the statistic the cycle count maps onto.[^8]

## The F(4,2) = 10 miniature

For height exactly 2 the tower above the base is a single row of blocks, encoded by a length-4 binary string whose runs of 1s are the tower blocks; even total castle blocks means an odd number of tower blocks, which at width 4 means exactly one run (three runs need width at least 5; the general count is `Σ_s C(w+1, 4s+2) = A038505(w+1)`). The 10 valid castles have tower column heights `1000 0100 0010 0001 1100 0110 0011 1110 0111 1111`, and each has exactly one maximal positive run — hence exactly one peak and one record — the transform in miniature across the whole case.[^9]

## Appearances in Sources

- [[project-euler-502-castle-factoring](pages/project-euler-502-castle-factoring.md)] — states the permutation template, the peak↔positive-run bijection, and the `F(4,2)=10` test.
- [[pe502-castle-cycle-permutations](pages/pe502-castle-cycle-permutations.md)] — reads this transform as the "Foata upgrade" in the (n−1)!-to-castle triad, paralleling largest-element cycle-leaders with leftmost-positive-column peak-leaders.

## Related Concepts

- [[permutation-cycle-castle-analogy](pages/permutation-cycle-castle-analogy.md)] — the analogy this transform instantiates.
- [[generalized-dyck-grammar](pages/generalized-dyck-grammar.md)] — the tower-word grammar whose peaks are the cycle-like atoms.
- [[castle-representations](pages/castle-representations.md)] — the column-height sequence the transform flattens onto.
- [[castle-sign](pages/castle-sign.md)] — the descent formula for the block count used to check the examples.
- [[aocp-multisets](pages/aocp-multisets.md)] — Foata's intercalation product and two-line-array cycle apparatus, the Vol. 3 sibling of this Vol. 1 construction.
- [[castles-as-upgraded-cycle-count](pages/castles-as-upgraded-cycle-count.md)] — the seminar synthesis; this transform is the middle row of the three-move (n−1)!-to-castle table.

## Footnotes

[^1]: [[project-euler-502-castle-factoring](pages/project-euler-502-castle-factoring.md)] §"The permutation template" L133-139 — "the cycle leaders are the left-to-right minima ... in Foata's ... presentation ... the left-to-right maxima ... number of cycles = number of left-to-right records ... (1 4)(0 2 3) flattens to 1 4 0 2 3. The left-to-right minima are 1 and 0, one per cycle."
[^2]: [[project-euler-502-castle-factoring](pages/project-euler-502-castle-factoring.md)] §"Knuth canonical cycle form" L19-25 — "writing every singleton cycle explicitly; putting the smallest element first within each cycle; ordering the cycles in decreasing order of their first element ... Erasing the parentheses recovers a one-line permutation."
[^3]: [[project-euler-502-castle-factoring](pages/project-euler-502-castle-factoring.md)] §"Knuth canonical cycle form" L27 — "The factorization is the loop i ↦ σ(i): start at an unvisited element and follow the map until it closes. The cycles are disjoint because the map is a bijection."
[^4]: [[project-euler-502-castle-factoring](pages/project-euler-502-castle-factoring.md)] §"Castle Factoring and the Knuth-Castle Foata Transform" L7 — "each U V D peak leaves the base, lives entirely above a sub-block, and returns to the same level, and disjoint peaks are separated by R gaps ... the Dyck first-return decomposition with one extra letter (R)."
[^5]: [[project-euler-502-castle-factoring](pages/project-euler-502-castle-factoring.md)] §"The castle version" L143-157 — "the peaks ... are exactly the maximal positive runs of c, and the map peak ↦ first column of its positive run is a bijection between peaks and the set { i : c_i > 0 and (i = 1 or c_{i-1} = 0) }."
[^6]: [[project-euler-502-castle-factoring](pages/project-euler-502-castle-factoring.md)] §"The castle version" L157 — "This set is the castle's record statistic: the left-to-right ascents from the base. In permutation Foata, a cycle leader is a new record; in castle Foata, a peak is a new excursion, a return to positive height after zero."
[^7]: [[project-euler-502-castle-factoring](pages/project-euler-502-castle-factoring.md)] §"The sign of a castle" L105-113 — "blocks = ∑_{i=0}^{L} max(0, c_i - c_{i+1}), c_0 = c_{L+1} = 0"; the tower words and block counts in the worked examples were re-derived and checked by execution.
[^8]: [[project-euler-502-castle-factoring](pages/project-euler-502-castle-factoring.md)] §"The tower grammar" L68 — "The excursion count (peaks) plays the role of the cycle count, while the block count plays the role of the sign atom. One peak may contain several stacked blocks, so these are distinct."
[^9]: [[project-euler-502-castle-factoring](pages/project-euler-502-castle-factoring.md)] §"The castle version" L159-165 — "The 10 valid castles have tower column heights 1000 0100 0010 0001 1100 0110 0011 1110 0111 1111 ... Each has exactly one positive run, hence exactly one peak, and the record set has size one."
