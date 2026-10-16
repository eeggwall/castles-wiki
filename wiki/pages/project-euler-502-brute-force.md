---
title: "PE 502: Brute Force"
category: Sources
summary: The Python reference module castle.py for Project Euler 502, in exact integer arithmetic. It computes A^e, A^o and A from the closed form, the signed tower count P(k, L) by a dynamic program over the last column height, and the castles of width w and height h by enumeration, tallied by block parity and by unimodality. Its self-test checks the four Project Euler values and the enumeration for w, h ≤ 5.
tags: [project-euler, castle, brute-force, python, verification, oeis, source, subpage]
sources: [project-euler-502-brute-force]
created: 2026-09-13
updated: 2026-10-16
---

# Project Euler 502 (PE 502): Brute Force

**Source:** https://charlesreid1.com/wiki/Project_Euler/502/Brute_Force (module: `castle.py`)
**Date ingested:** 2026-09-13
**Type:** article (MediaWiki subpage of [[project-euler-502](pages/project-euler-502.md)]) documenting a Python module

## Summary

`castle.py` cross-checks the Java solver of [[project-euler-502-implementation-notes](pages/project-euler-502-implementation-notes.md)] in exact integer arithmetic, with no modular reduction, no Berlekamp-Massey and no Kitamasa. The source puts the enumerator's range at about `w, h ≤ 15`, and the dynamic program covers every exact checkpoint.[^1] The module computes:[^2]

- `F(w, h)`, the even-block count `A^e(w, h)`, from the closed form of the [[castle-counting-formula](pages/castle-counting-formula.md)];
- `F_odd(w, h)`, the odd-block count `A^o(w, h)`;
- `F_any(w, h) = h^w − (h−1)^w`, the count `A(w, h)` of castles of width `w` and height `h`;
- `p_signed(k, L)`, the signed tower count `P(k, L)`;
- `brute(w, h)`, the castles of width `w` and height `h` by enumeration of `{1, …, h}^w`, tallied by the parity of the block count and by unimodality;
- `block_poly(w, h)`, the distribution of the block count over the castles of width `w` and height at most `h`.

**Block count.** A castle of width `w` and height `h` is a skyline `c_1, …, c_w ∈ {1, …, h}` with `max c = h`, and a block is a maximal run of columns at one level, so[^3]

```
blocks(c)  =  Σ_{r=1}^{h} #{runs of columns with c_i ≥ r}  =  c_1 + Σ_{i=2}^{w} max(0, c_i − c_{i−1}).
```

The gap rule between neighboring blocks in a row holds for every skyline, since two runs at one level are separated by a lower column, and the even-block rule is a filter on the block count.[^3]

**Signed tower count.** `p_signed` computes `P(k, L)` from its definition. A column of height `b` after a column of height `a` starts `max(0, b − a)` new blocks, each contributing a factor `−1`, so the state is a vector of length `k + 1` indexed by the last column height, updated in `O(k²)` operations per column and `O(k²L)` in all.[^4] It uses neither the grammar generating function nor the rational-function update, which makes it an independent check of both.

**Unimodal castles.** `brute` also tallies the unimodal skylines, which rise and then fall, into `conv_even` and `conv_odd`.[^5] These are the [[convex-castle](pages/convex-castle.md)]s, of which there are `C(2h+w−3, w−1)` of width `w` and height `h`; every one has exactly `h` blocks, so they are all even-block or all odd-block according to the parity of `h`.

**OEIS mining.** The source lists three uses of the enumerator: ground truth for `p_signed`, which is checked against `brute` on `w, h ≤ 5` before any change reaches the Java solver; the block-count distributions and unimodal counts of the other subpages; and sequences from a rectangle of `(w, h)` to look up in the OEIS.[^6] [[oeis-mining-pe502](pages/oeis-mining-pe502.md)] is that search.

The source's `F`, `F_odd` and `F_any` are the wiki's `A^e`, `A^o` and `A` ([[castle-notation](pages/castle-notation.md)]).

## Verification

The self-test checks:[^7]

- the four Project Euler values `A^e(4, 2) = 10`, `A^e(13, 10) = 3 729 050 610 636`, `A^e(10, 13) = 37 959 702 514` and `A^e(100, 100) mod (10^9 + 7) = 841 913 936`, which also head the Java `main`;
- for all `w, h ≤ 5`, that `brute` agrees with `F` and `F_odd`, and that the even and odd tallies add up to `F_any`.

The same checks, with the block-count formula against the definition by runs for `w, h ≤ 6` and `p_signed` against the sum over all towers for `k ≤ 4`, `L ≤ 5`, agree when recomputed.[^8]

## Key Takeaways

- An exact reference for `A^e`, `A^o`, `A` and `P`, with an enumerator that is the ground truth for the dynamic program.[^6]
- The block count of a skyline is its total ascent `c_1 + Σ_{i≥2} max(0, c_i − c_{i−1})`.[^3]
- `p_signed` computes `P(k, L)` from its definition in `O(k²L)` operations.[^4]
- The unimodal skylines are the convex castles; `brute` splits them by block parity.[^5]

## Entities & Concepts

- [[castle-counting-formula](pages/castle-counting-formula.md)] - the closed form behind `F`, and the dynamic program for `P(k, L)` as an independent check.
- [[castle-counting-function](pages/castle-counting-function.md)] - the counts `A`, `A^e` and `A^o`.
- [[castle-sign](pages/castle-sign.md)] - the block count as total ascent and as total descent.
- [[convex-castle](pages/convex-castle.md)] - the unimodal castles that `conv_even` and `conv_odd` count, `C(2h+w−3, w−1)` of width `w` and height `h`.
- [[horizontally-convex-polyomino](pages/horizontally-convex-polyomino.md)], [[column-convex-polyomino](pages/column-convex-polyomino.md)] - the two convexities; every castle is column-convex, and the unimodal castles are the row-convex ones.
- [[aocp-generating-permutations-tuples](pages/aocp-generating-permutations-tuples.md)] - Knuth's Algorithm M, which generates `{1, …, h}^w` in the lexicographic order of the enumeration, with every radix `h`.
- [[castle-snippets](pages/castle-snippets.md)] - tested Python snippets for enumeration, predicates and OEIS lookups, with the same `is_unimodal` test.
- [[oeis-mining-pe502](pages/oeis-mining-pe502.md)] - the OEIS search over the module's sequences.

Sibling subpages of [[project-euler-502](pages/project-euler-502.md)]: [[project-euler-502-problem-setup](pages/project-euler-502-problem-setup.md)], [[project-euler-502-representations](pages/project-euler-502-representations.md)], [[project-euler-502-castle-factoring](pages/project-euler-502-castle-factoring.md)], [[project-euler-502-observations](pages/project-euler-502-observations.md)], [[project-euler-502-solution](pages/project-euler-502-solution.md)], [[project-euler-502-implementation-notes](pages/project-euler-502-implementation-notes.md)].

## Footnotes

[^1]: [[project-euler-502-brute-force](pages/project-euler-502-brute-force.md)] §"Brute Force" L5 - "A small Python module used to cross-check the Java solver on Project Euler/502/Implementation Notes. Exact integer arithmetic, no modular reduction, no BM, no Kitamasa. Fast enough for w, h ≤ 15 or so on the brute enumerator, and for the full range of the exact F(w, h) checks on the DP path."
[^2]: [[project-euler-502-brute-force](pages/project-euler-502-brute-force.md)] §"What it computes" [synthesis] L9-14 - `F` (even-block, exact, by the closed form), `F_odd` (odd-block, the complement of `F`), `F_any` (any parity, `h^w − (h−1)^w`), `p_signed(k, L)` (the signed sum `P(k, L)` by an `O(k·L·k)` DP), `brute(w, h)` (enumeration tallied by parity and unimodality), `block_poly(w, h)` (the block-count distribution over height `≤ h`).
[^3]: [[project-euler-502-brute-force](pages/project-euler-502-brute-force.md)] §"Column-height encoding" L18-27 - "column heights c_1, …, c_w ∈ {1, …, h} with max c = h", "#blocks = ∑_{r=1}^{h} #{runs of columns with c_i ≥ r} = c_1 + ∑_{i=2}^{w} max(0, c_i − c_{i−1})", "Rule 3 (gap between neighbouring blocks in the same row) is automatic in the run decomposition: two runs at the same level are always separated by a strictly lower column. Rule 6 (even block count) is applied by parity at the end."
[^4]: [[project-euler-502-brute-force](pages/project-euler-502-brute-force.md)] §"p_signed" L31-47 - "A new column of height b after a column of height a starts max(0, b − a) new runs, each contributing a factor of −1", "State is a length-(k+1) vector indexed by the last column height. The transition is O(k^2), so O(k^2 L) total. Exact integers throughout."
[^5]: [[project-euler-502-brute-force](pages/project-euler-502-brute-force.md)] §"brute" L51-67 - "conv_even, conv_odd - the same, restricted to unimodal skylines (column-convex AND row-convex)", and the test "walk up, then walk down; accept iff the walk covers the whole tuple". The count `C(2h+w−3, w−1)` and the block count `h` are from [[convex-castle](pages/convex-castle.md)], checked by enumeration for `w ≤ 7`, `h ≤ 5` and for `w ≤ 6`, `h ≤ 4` (Python 3.11, 2026-10-16).
[^6]: [[project-euler-502-brute-force](pages/project-euler-502-brute-force.md)] §"Why keep a brute enumerator" L89-93 - "Ground truth for the DP. Any change to p_signed is validated against brute on w, h ≤ 5 before touching the Java solver.", "The dist and conv_* counts feed the observations", "OEIS mining. Running brute over a rectangle of (w, h) produces sequences (even, odd, unimodal, block-count distributions) that can be looked up in the OEIS to reveal further structure."
[^7]: [[project-euler-502-brute-force](pages/project-euler-502-brute-force.md)] §"Self-test" L72-85 - "F(4, 2) = 10", "F(13, 10) = 3 729 050 610 636", "F(10, 13) = 37 959 702 514", "F(100, 100) mod (10^9 + 7) = 841 913 936", "brute(w, h)[\"even\"] == F(w, h)", "brute(w, h)[\"odd\"] == F_odd(w, h)", "brute(w, h)[\"even\"] + brute(w, h)[\"odd\"] == F_any(w, h)", and "The same four checks appear at the top of the Java main".
[^8]: Verified by execution (Python 3.11, 2026-10-16): the four values from the closed form with `P` from the rational-function update and from `p_signed`; the closed form against enumeration for `2 ≤ h ≤ 5`, `w ≤ 6`; the block-count formula against the count of runs row by row for all skylines with `w, h ≤ 6`; `p_signed(k, L)` against the sum of `(−1)^{blocks}` over all towers for `k ≤ 4`, `1 ≤ L ≤ 5`.
