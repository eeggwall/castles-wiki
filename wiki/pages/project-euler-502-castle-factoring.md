---
title: "PE 502: Castle Factoring"
category: Sources
summary: The Project Euler 502 subpage that compares towers with permutations. Peaks of the tower word play the role of cycles, (−1)^blocks the role of the permutation sign, and the source builds a castle Foata transform (peaks are the maximal positive runs of the column heights) and a monotone streak factorization (blocks = total descent). It also gives the column-height proof of T(k, L) = (k+1)^L.
tags: [project-euler, castle, permutations, foata, factorization, source, subpage]
sources: [project-euler-502-castle-factoring]
created: 2026-09-13
updated: 2026-10-16
---

# Project Euler 502 (PE 502): Castle Factoring

**Source:** https://charlesreid1.com/wiki/Project_Euler/502/Castle_Factoring
**Date ingested:** 2026-09-13
**Type:** article (MediaWiki subpage of [[project-euler-502](pages/project-euler-502.md)])

## Summary

The source compares the towers of a castle with permutations: the peaks of a tower word correspond to the cycles of a permutation, and `R` gaps between peaks to the parentheses between cycles.[^1] A peak is a production `U V D` at the base of the tower grammar, one block in the first row above the base together with the towers `V` it carries ([[generalized-dyck-grammar](pages/generalized-dyck-grammar.md)]). The source calls the comparison a factorization, the Dyck first-return decomposition with the extra letter `R`.[^1]

The source works with the column heights `c_1, …, c_L` of towers on a base of length `L`, where `c_i` is the number of blocks over column `i` ([[castle-representations](pages/castle-representations.md)]). With them it develops three constructions, each set beside a construction on permutations:[^2]

- the sign `(−1)^{blocks}` of towers, beside the sign of a permutation ([[castle-sign](pages/castle-sign.md)]);
- a castle Foata transform, beside Foata's fundamental transformation ([[castle-foata-transform](pages/castle-foata-transform.md)]);
- a monotone streak factorization of the first differences of the column heights ([[monotone-streak-factorization](pages/monotone-streak-factorization.md)]).

It also proves `T(k, L) = (k+1)^L` from the column heights,[^3] and lists three further encodings of towers, which [[castle-representations](pages/castle-representations.md)] records.[^4]

## Key Takeaways

- **The correspondence.** Cycles correspond to peaks, the number of cycles to the number of peaks, and the sign `(−1)^{n−c}` of a permutation of `n` points with `c` cycles to `(−1)^{blocks}`. The number of peaks and the number of blocks are different statistics, since one peak can carry several stacked blocks.[^5] [[permutation-cycle-castle-analogy](pages/permutation-cycle-castle-analogy.md)] gives the full table.
- **Canonical cycle form.** The permutation side uses Knuth's canonical cycle form: singletons written out, the smallest element first in each cycle, and the cycles in decreasing order of first element. The source's example is the permutation `2 4 3 0 1` of `{0, …, 4}`, with cycles `(0 2 3)(1 4)`, canonical form `(1 4)(0 2 3)`, and flattened form `1 4 0 2 3`.[^6]
- **Column heights.** The column heights of towers of height at most `k` range independently over `{0, …, k}`, and the tower word is recovered from them by moving from `c_{i−1}` to `c_i` with `U` or `D` steps, one `R` per column, and `D^{c_L}` at the end, with `c_0 = 0`. Hence `T(k, L) = (k+1)^L`.[^3]
- **The sign.** With `c_0 = c_{L+1} = 0`, the block count is the total descent `Σ_{i=0}^{L} max(0, c_i − c_{i+1})`, and each `D` step ends one block. Over the towers of height at most `k` on a base of length `L`, the even-block ones number `(T(k, L) + P(k, L))/2` and the odd-block ones `(T(k, L) − P(k, L))/2`; the source sets this split beside the split of permutations into even and odd ones by `(1 ± sgn)/2`. A castle has one block more than its towers, so its even-block castles stand on odd-block towers, which is the term `(T − P)/2` of the [[castle-counting-formula](pages/castle-counting-formula.md)].[^7]
- **Castle Foata transform.** The peaks of a tower word, in order, are the maximal runs of columns with `c_i ≥ 1`, and consecutive peaks are separated by a column with `c_i = 0`. Sending each peak to the first column of its run is a bijection onto `{i : c_i > 0 and (i = 1 or c_{i−1} = 0)}`, so the number of peaks equals the number of these records, as the number of cycles equals the number of left-to-right records of the flattened permutation.[^8] For the castles of height 2 and width 4, the 10 even-block castles stand on the strings `1000, 0100, 0010, 0001, 1100, 0110, 0011, 1110, 0111, 1111`, each with one run, so each has one peak.[^9]
- **Monotone streak factorization.** The first differences `d_i = c_{i+1} − c_i`, `i = 0, …, L`, split into maximal up-streaks (`d_i > 0`), flat runs (`d_i = 0`) and down-streaks (`d_i < 0`) in one `O(L)` scan, which the source sets beside Knuth's `O(n)` cycle-following loop. The block count is the sum of the magnitudes of the down-streaks.[^10]
- **Fast algorithms.** The source writes `P(k, L)` as the sum of `(−1)^{descent(c)}` over `c ∈ {0, …, k}^L` and names the rational-function update of [[project-euler-502-representations](pages/project-euler-502-representations.md)], evaluated by Kitamasa's method in `O(k² log L)` in the `L` direction or by Berlekamp-Massey in the `k` direction.[^11] Of the Project Euler targets, `A^e(10^12, 100)` is evaluated by Kitamasa's method in `L`, and `A^e(100, 10^12)` by a recurrence in `k` found by Berlekamp-Massey ([[castle-count-algorithms](pages/castle-count-algorithms.md)]).

The source writes `F(w, h)` for the even-block count `A^e(w, h)` and `s(C)` for the sign; the wiki writes `(−1)^{blocks}`, since `s` is the semi-perimeter.

## Entities & Concepts

- [[permutation-cycle-castle-analogy](pages/permutation-cycle-castle-analogy.md)] - the correspondence of cycles with peaks, and its table.
- [[castle-sign](pages/castle-sign.md)] - the sign `(−1)^{blocks}`, the block count as total ascent and as total descent, and the even/odd split.
- [[castle-foata-transform](pages/castle-foata-transform.md)] - the bijection from peaks to the first columns of the positive runs.
- [[monotone-streak-factorization](pages/monotone-streak-factorization.md)] - the up-streaks, flat runs and down-streaks of the first differences.
- [[castle-representations](pages/castle-representations.md)] - the column-height encoding, and the three encodings this source adds: the excursion/gap word, the cycle forest, and the signed column-difference sequence.
- [[generalized-dyck-grammar](pages/generalized-dyck-grammar.md)] - the tower grammar whose productions `U V D` are the peaks.
- [[castle-counting-formula](pages/castle-counting-formula.md)] - the column-height proof of `T(k, L) = (k+1)^L` and the term `(T − P)/2`.
- [[aocp-multisets](pages/aocp-multisets.md)] - Knuth's two-line arrays, Foata's intercalation product, and the cycle factorization of multiset permutations.
- [[castles-as-upgraded-cycle-count](pages/castles-as-upgraded-cycle-count.md)] - a seminar that builds the sign, the Foata transform and the streak factorization from the proof that there are `(n−1)!` cycles on `n` labeled points.
- [[block-count-constraints](pages/block-count-constraints.md)] - castles selected by block count modulo `m`, in sparse sets and in numerical semigroups, of which the sign is the case modulo 2.
- [[castle-compression](pages/castle-compression.md)] - the streak and excursion/gap encodings as run-length descriptions of a castle.

Also linked from the source: [[polyominoes](pages/polyominoes.md)], [[dyck-words](pages/dyck-words.md)], [[project-euler-502-solution](pages/project-euler-502-solution.md)], [[project-euler-502-representations](pages/project-euler-502-representations.md)].

Sibling subpages of [[project-euler-502](pages/project-euler-502.md)]: [[project-euler-502-problem-setup](pages/project-euler-502-problem-setup.md)], [[project-euler-502-representations](pages/project-euler-502-representations.md)], [[project-euler-502-observations](pages/project-euler-502-observations.md)], [[project-euler-502-solution](pages/project-euler-502-solution.md)], [[project-euler-502-implementation-notes](pages/project-euler-502-implementation-notes.md)], [[project-euler-502-brute-force](pages/project-euler-502-brute-force.md)].

## References (from the source)

- Donald E. Knuth, *The Art of Computer Programming*, Vol. 1, 3rd ed., §1.3.3 ("An Unusual Correspondence").[^12]
- GNU Scientific Library, Permutations, canonical cyclic form.[^12]
- Foata's fundamental transformation (Knuth canonical-cycle flattening).[^12]

## Footnotes

[^1]: [[project-euler-502-castle-factoring](pages/project-euler-502-castle-factoring.md)] §"Castle Factoring and the Knuth-Castle Foata Transform" L5-7 - "permutation cycles : castle peaks/excursions", "each U V D peak leaves the base, lives entirely above a sub-block, and returns to the same level, and disjoint peaks are separated by R gaps. This is a genuine factorization, not a metaphor: it is the Dyck first-return decomposition with one extra letter (R)".
[^2]: [[project-euler-502-castle-factoring](pages/project-euler-502-castle-factoring.md)] §"Castle Factoring and the Knuth-Castle Foata Transform" L9-13 - "a sign for castles, the castle analogue of the permutation sign; a castle Foata transform, the castle analogue of Knuth's canonical-cycle flattening; a monotone streak factorization, the run-length view the fast algorithms sum over."
[^3]: [[project-euler-502-castle-factoring](pages/project-euler-502-castle-factoring.md)] §"A column-height factorization" L72-88 - "c_i is the number of blocks covering column i. Then each c_i ranges independently over {0, …, k}, and the tower word is recovered by ... it is invertible. Hence T(k,L) = (k+1)^L".
[^4]: [[project-euler-502-castle-factoring](pages/project-euler-502-castle-factoring.md)] §"New representations worth writing up" [synthesis] L194-216 - the excursion/gap word, the cycle-forest form, and the signed column-difference sequence.
[^5]: [[project-euler-502-castle-factoring](pages/project-euler-502-castle-factoring.md)] §"The tower grammar" L45-68 - the correspondence table, ending "sign (-1)^{n-c} | sign (-1)^{blocks}", and "One peak may contain several stacked blocks, so these are distinct."
[^6]: [[project-euler-502-castle-factoring](pages/project-euler-502-castle-factoring.md)] §"Knuth canonical cycle form" L19-25 - "writing every singleton cycle explicitly; putting the smallest element first within each cycle; ordering the cycles in decreasing order of their first element", "the linear permutation (2 4 3 0 1) has cycles (0 2 3)(1 4), so its canonical form is (1 4)(0 2 3). Erasing the parentheses recovers a one-line permutation, (1 4 0 2 3)."
[^7]: [[project-euler-502-castle-factoring](pages/project-euler-502-castle-factoring.md)] §"The sign of a castle" [synthesis] L92-127 - the sign `s(C) = (−1)^{blocks(C)}`, the block count as total descent with `c_0 = c_{L+1} = 0`, the split `(T ± P)/2` set beside "the (1 ± sgn)/2 trick that separates permutations into even and odd classes", and "\"castle has even total blocks\" is therefore \"tower has an odd number of blocks\", which is the (T-P)/2 term".
[^8]: [[project-euler-502-castle-factoring](pages/project-euler-502-castle-factoring.md)] §"The permutation template" L133-139 and §"The castle version" [synthesis] L143-157 - cycles counted by left-to-right records of the flattened permutation; the claim that peaks span maximal runs of columns with `c_i ≥ 1`, separated by columns with `c_i = 0`, and the bijection from peaks to `{i : c_i > 0 and (i = 1 or c_{i−1} = 0)}`.
[^9]: [[project-euler-502-castle-factoring](pages/project-euler-502-castle-factoring.md)] §"The castle version" L159-165 - "The 10 valid castles have tower column heights 1000 0100 0010 0001 1100 0110 0011 1110 0111 1111 ... Each has exactly one positive run, hence exactly one peak". The ten strings and their one run each were checked by enumeration of the castles of width 4 and height 2 (Python 3.11, 2026-10-16).
[^10]: [[project-euler-502-castle-factoring](pages/project-euler-502-castle-factoring.md)] §"Monotone streak factorization and fast algorithms" L169-178 - "d_i = c_{i+1} - c_i with c_0 = c_{L+1} = 0. Factor the d sequence into maximal up-streaks (d_i > 0), flat runs (d_i = 0), and down-streaks (d_i < 0)", "the number of blocks equals ... the sum of the magnitudes of the down-streaks", "a single O(L) scan, the castle version of Knuth's O(n) cycle-following loop".
[^11]: [[project-euler-502-castle-factoring](pages/project-euler-502-castle-factoring.md)] §"Monotone streak factorization and fast algorithms" L184-192 - "P(k,L) = \sum_{c \in \{0,\dots,k\}^L} (-1)^{\text{descent}(c)}", "evaluated in O(k^2 \log L) by Kitamasa in the L direction, or in the k direction by Berlekamp-Massey".
[^12]: [[project-euler-502-castle-factoring](pages/project-euler-502-castle-factoring.md)] §"References" L236-238 - Knuth, TAOCP Vol. 1, 3rd ed., Section 1.3.3 ("An Unusual Correspondence"); GNU Scientific Library, Permutations, canonical cyclic form; "Foata's fundamental transformation (Knuth canonical-cycle flattening)."
