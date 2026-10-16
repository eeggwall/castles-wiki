---
title: Monotone streak factorization
category: Concepts
summary: The first differences d_i = c_{i+1} − c_i of a skyline, with c_0 = c_{L+1} = 0, split in one O(L) scan into maximal up-streaks, flat runs and down-streaks. The block count is the sum of the magnitudes of the down-streaks, so the sign of a castle or of towers is (−1) to that sum, and a flat run of r zeros is a run of r + 1 equal heights. The source sets the scan beside Knuth's O(n) cycle-following loop on permutations.
tags: [concept, castle, factorization, algorithms]
sources: [project-euler-502-castle-factoring]
created: 2026-09-13
updated: 2026-10-16
---

# Monotone streak factorization

## Definition

Let `c = (c_1, …, c_L)` be the column heights of a castle or of towers ([[castle-representations](pages/castle-representations.md)]), and set `c_0 = c_{L+1} = 0`. The first differences are[^1]

```
d_i  =  c_{i+1} − c_i,        i = 0, 1, …, L.
```

The **monotone streak factorization** splits `(d_0, …, d_L)` into maximal **up-streaks** (consecutive `d_i > 0`), **flat runs** (consecutive `d_i = 0`) and **down-streaks** (consecutive `d_i < 0`).[^1]

*Example.* For the castle `(2, 2, 1, 3, 3)`, the extended heights are `(0, 2, 2, 1, 3, 3, 0)` and the differences are `(2, 0, −1, 2, 0, −3)`. They split into the up-streak `(2)`, the flat run `(0)`, the down-streak `(−1)`, the up-streak `(2)`, the flat run `(0)` and the down-streak `(−3)`.

## Properties

- **Blocks.** The block count is the total descent `Σ_{i=0}^{L} max(0, c_i − c_{i+1})`, the sum of the magnitudes of the down-streaks; in the tower word each `D` step ends one block ([[castle-sign](pages/castle-sign.md)]).[^2] So the sign `(−1)^{blocks}` is `−1` to the sum of the down-streak magnitudes, and summed over the towers of height at most `k` on a base of length `L` it gives `P(k, L)` ([[signed-tower-count](pages/signed-tower-count.md)]). The example has `1 + 3 = 4` blocks: the bottom row, two blocks in row 2 (columns 1-2 and 4-5) and one in row 3 (columns 4-5).
- **Plateaus.** A flat run of `r` zeros is a run of `r + 1` equal consecutive entries of `(c_0, …, c_{L+1})`. Between two nonzero differences, these are `r + 1` columns at one height; in the example, the two flat runs mark the columns `(2, 2)` and `(3, 3)`.
- **One scan.** The factorization takes a single `O(L)` scan of the differences. The source sets this scan beside Knuth's `O(n)` loop that follows the cycles of a permutation, the third row of the table of `(n − 1)!` proof moves on [[permutation-cycle-castle-analogy](pages/permutation-cycle-castle-analogy.md)].[^2][^3]

## Appearances in Sources

- [[project-euler-502-castle-factoring](pages/project-euler-502-castle-factoring.md)] - the definition of the factorization, the block count as the sum of the down-streak magnitudes, and the comparison with Knuth's cycle-following loop.

## Related Concepts

- [[castle-sign](pages/castle-sign.md)] - the block count as total ascent and as total descent, and the sign `(−1)^{blocks}`.
- [[signed-tower-count](pages/signed-tower-count.md)] - `P(k, L)`, the sum of the sign over towers.
- [[castle-representations](pages/castle-representations.md)] - the column-height encoding that the factorization reads.
- [[permutation-cycle-castle-analogy](pages/permutation-cycle-castle-analogy.md)] - the correspondence of permutation cycles with peaks, in which the streak scan stands opposite the cycle-following loop.
- [[castles-as-upgraded-cycle-count](pages/castles-as-upgraded-cycle-count.md)] - a seminar that builds the sign, the castle Foata transform and the streak factorization from the proof that there are `(n−1)!` cycles on `n` labeled points.
- [[castle-compression](pages/castle-compression.md)] - the streak factorization as a run-length description of a castle.
- [[castle-gray-code](pages/castle-gray-code.md)] - the reflected Gray code on the skylines in `{1, …, h}^w`, which changes one column per step.

## Footnotes

[^1]: [[project-euler-502-castle-factoring](pages/project-euler-502-castle-factoring.md)] §"Monotone streak factorization and fast algorithms" L169-175 - "Represent a castle by column heights c_i and take first differences d_i = c_{i+1} - c_i with c_0 = c_{L+1} = 0. Factor the d sequence into maximal up-streaks (d_i > 0), flat runs (d_i = 0), and down-streaks (d_i < 0)."
[^2]: [[project-euler-502-castle-factoring](pages/project-euler-502-castle-factoring.md)] §"Monotone streak factorization and fast algorithms" L177-178 - "Each D move completes one block, so the number of blocks equals the number of D moves, the total descent ∑ max(0, c_i - c_{i+1}), and the sum of the magnitudes of the down-streaks." and "The streak factorizer is a single O(L) scan, the castle version of Knuth's O(n) cycle-following loop."
[^3]: raw/pe502-castle-cycle-permutations.md §"Connection 3: Monotone streak factorization ↔ O(n) cycle-following" L62, §"Tying back to (n-1)!" L84 - "Take first differences d_i = c_{i+1} − c_i; split into up-runs, flat runs, down-runs. Block count = sum of down-run magnitudes", and the table row "cycle-follow the permutation to read off cycles | monotone streak scan to read off peaks".
