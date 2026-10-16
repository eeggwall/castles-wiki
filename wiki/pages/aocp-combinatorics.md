---
title: "AOCP Combinatorics (Knuth TAOCP Vol. 3)"
category: Sources
summary: Notes on the combinatorics that opens Knuth's Vol. 3 - inversions, the inversion table b_1 … b_n with 0 ≤ b_j ≤ n − j (which determines the permutation, Hall 1956), the counts I_n(k) of permutations with k inversions with I_n(k) = I_n(k−1) + I_{n−1}(k) for 1 ≤ k < n, the generating function G_n(z) = Π_{k=1}^{n} (1 + z + ⋯ + z^{k−1}), and the inversion count of a random permutation as a sum of independent uniform variables. On the castle side, the rainbow castles of height h by inversions of the skyline are the Mahonian numbers A008302.
tags: [knuth, taocp, combinatorics, inversions, permutations, generating-functions, q-factorial, source]
sources: [aocp-combinatorics]
created: 2026-09-13
updated: 2026-10-16
---

# AOCP Combinatorics (Knuth, *The Art of Computer Programming*, Vol. 3)

**Source:** https://charlesreid1.com/wiki/AOCP/Combinatorics (notes on Knuth, *The Art of Computer Programming*, Vol. 3: Sorting and Searching)
**Date ingested:** 2026-09-13
**Type:** article (MediaWiki notes page)

## Summary

The notes follow Knuth's start of Vol. 3, which approaches sorting through the combinatorics of permutations. For a permutation `a_1 a_2 … a_n` of `{1, …, n}`, a pair `(a_i, a_j)` with `i < j` and `a_i > a_j` is an **inversion**, an out-of-order pair.[^1]

**Inversion tables.** The inversion table `b_1 b_2 … b_n` of the permutation has `b_j` equal to the number of elements to the left of `j` that are greater than `j`, so `0 ≤ b_j ≤ n − j`. The notes' example is[^2]

```
permutation       5 9 1 8 2 6 4 7 3
inversion table   2 3 6 4 0 2 2 1 0
```

The notes credit Hall (1956) with the fact that the inversion table determines the permutation, so counting problems on permutations become counting problems on tables with independent entries. Under the uniform distribution the entries `b_j` are independent and uniform on `{0, …, n − j}`, so the number of `j` with `b_j = n − j` has mean `1/n + 1/(n − 1) + ⋯ + 1 = H_n`, the harmonic number.[^3] These `j` are the elements greater than every element to their right; the notes describe them as the elements larger than their successor, which is a different statistic.[^7]

**The inversion generating function.** Write `I_n(k)` for the number of permutations of `n` elements with exactly `k` inversions and `G_n(z) = Σ_k I_n(k) z^k`. The notes record the symmetry `I_n(C(n, 2) − k) = I_n(k)`, the recurrence `I_n(k) = I_n(k − 1) + I_{n−1}(k)` for `1 ≤ k < n`, and Knuth's step `G_n(z) = (1 + z + ⋯ + z^{n−1}) G_{n−1}(z)`, which gives[^4]

```
G_n(z)  =  Π_{k=1}^{n} (1 + z + ⋯ + z^{k−1})  =  (1 − z^n)(1 − z^{n−1}) ⋯ (1 − z) / (1 − z)^n.
```

The product is the q-factorial of [[permutation-inversions](pages/permutation-inversions.md)]; at `z = 1` it gives `n!`. The recurrence fails for `k ≥ n` (first at `n = 3`, `k = 3`), where the general form `I_n(k) = I_n(k − 1) + I_{n−1}(k) − I_{n−1}(k − n)` applies.[^7]

**Probability.** Dividing by `n!`, `g_n(z) = G_n(z)/n! = h_1(z) h_2(z) ⋯ h_n(z)`, where `h_k(z) = (1 + z + ⋯ + z^{k−1})/k` is the generating function of a uniform integer in `{0, …, k − 1}`. So the inversion count of a uniform random permutation is a sum of independent uniform variables, and its mean and variance are the sums of theirs.[^5] [[permutation-inversions](pages/permutation-inversions.md)] evaluates them: mean `n(n − 1)/4`, variance `n(n − 1)(2n + 5)/72`.

## Castle readings

These readings are the wiki's; the notes do not mention castles.

- **Rainbow castles are Mahonian.** A rainbow castle ([[castle-classification-shape](pages/castle-classification-shape.md)]) has width `w = h` and column heights forming a permutation of `{1, …, h}`, so the inversions of its skyline are the inversions of a permutation. The `h!` rainbow castles of height `h`, counted by skyline inversions, are `I_h(k)`, the Mahonian numbers `A008302`: `1; 1, 1; 1, 2, 2, 1; 1, 3, 5, 6, 5, 3, 1; …`.[^6] Their block count `c_1 + Σ max(0, c_i − c_{i−1})` is the total ascent of the skyline ([[castle-sign](pages/castle-sign.md)]), a second grading of the same castles, and the ascents and descents of the skyline are the streaks of [[monotone-streak-factorization](pages/monotone-streak-factorization.md)].
- **Product sets.** The inversion tables of permutations of `n` elements are the product set `{0, …, n − 1} × {0, …, n − 2} × ⋯ × {0}`, which is why there are `n!` of them. The towers of height at most `k` on a base of length `L` are the product set `{0, …, k}^L` of their column heights, which is why there are `(k + 1)^L` ([[castle-counting-formula](pages/castle-counting-formula.md)], the Lemma in the section *Tower count*).
- **Inversions of words.** Dyck words counted by inversions give the Carlitz q-Catalan numbers, and steep Dyck words counted by inversions give q-analogs of the Motzkin numbers ([[dyck-words](pages/dyck-words.md)], [[q-catalan-numbers](pages/q-catalan-numbers.md)], [[steep-polyominoes-q-motzkin-bessel](pages/steep-polyominoes-q-motzkin-bessel.md)]). Permutations of a multiset by inversions give the q-multinomial coefficient ([[aocp-multinomial-coefficients](pages/aocp-multinomial-coefficients.md)]).
- **Other q-gradings of castles.** Castles are counted by area on [[castle-by-area](pages/castle-by-area.md)] and tree skylines by area on [[tree-castle-by-area](pages/tree-castle-by-area.md)]; [[tower-word-continued-fraction](pages/tower-word-continued-fraction.md)] counts tower words, which are Motzkin paths, by continued fractions with weights on the steps.

## Entities & Concepts

- [[permutation-inversions](pages/permutation-inversions.md)] - inversions, the q-factorial `G_n(z)`, and the mean and variance of the inversion count.
- [[castle-classification-shape](pages/castle-classification-shape.md)] - the rainbow castles, whose skylines are permutations.
- [[castle-counting-formula](pages/castle-counting-formula.md)] - the towers as the product set `{0, …, k}^L`.
- [[castle-sign](pages/castle-sign.md)], [[monotone-streak-factorization](pages/monotone-streak-factorization.md)] - the block count as total ascent, and the streaks of a skyline.
- [[dyck-words](pages/dyck-words.md)], [[q-catalan-numbers](pages/q-catalan-numbers.md)], [[steep-polyominoes-q-motzkin-bessel](pages/steep-polyominoes-q-motzkin-bessel.md)] - Dyck words and steep Dyck words counted by inversions.
- [[aocp-multinomial-coefficients](pages/aocp-multinomial-coefficients.md)] - permutations of a multiset by inversions.
- [[aocp-permutations](pages/aocp-permutations.md)] - the permutation and factorial basics of Vol. 1.
- [[castle-by-area](pages/castle-by-area.md)], [[tree-castle-by-area](pages/tree-castle-by-area.md)], [[tower-word-continued-fraction](pages/tower-word-continued-fraction.md)] - castles, tree skylines and tower words counted with a second variable.

Linked from the source: [[aocp-multisets](pages/aocp-multisets.md)] and Analytic Combinatorics ([[analytic-combinatorics-ch1-ogfs](pages/analytic-combinatorics-ch1-ogfs.md)]).

## Relation to Other Wiki Pages

[[permutation-inversions](pages/permutation-inversions.md)] is the concept page for the inversion statistic and its generating function; [[aocp-permutations](pages/aocp-permutations.md)] derives the factor `1 + z + ⋯ + z^{n−1}` of `G_n(z)` from the insertion of the largest element.

## Footnotes

[^1]: [[aocp-combinatorics](pages/aocp-combinatorics.md)] §"Permutations and Inversions" L11-15 - "Let a_1 a_2 a_3 … a_n be a permutation of the integers {1 … n}. If i < j and a_i > a_j, then (a_i, a_j) is an inversion. Inversions are out-of-sorts pairs."
[^2]: [[aocp-combinatorics](pages/aocp-combinatorics.md)] §"Permutations and Inversions" L21-32 - "b_j is the number of elements to the left of j that are greater than j", the example "5 9 1 8 2 6 4 7 3 / 2 3 6 4 0 2 2 1 0", and "0 ≤ b_1 ≤ n-1, 0 ≤ b_2 ≤ n-2, …, 0 ≤ b_{n-1} ≤ 1".
[^3]: [[aocp-combinatorics](pages/aocp-combinatorics.md)] §"Permutations and Inversions" L34-59 - "Hall (1956) showed that inversion tables uniquely determine permutations", "Transformation technique: turn counting problems into inversion table problems", "count number of elements larger than their successor. (This is the number of j such that b_j = n-j)", "P(b_1 = n-1) = 1/n", "1/n + 1/(n-1) + … + 1 = H_n. These are the harmonic numbers."
[^4]: [[aocp-combinatorics](pages/aocp-combinatorics.md)] §"Counting Inversions with Generating Functions" L69-96 - the symmetry "I_n(C(n, 2) - k) = I_n(k)" (garbled in the notes), "G_n(z) = I_n(0) + I_n(1)z + I_n(2) z^2 + … = Σ_{k≥0} I_n(k) z^k", "I_n(k) = I_n(k-1) + I_{n-1}(k) for k < n", "G_n(z) = (1 + z + … + z^{n-1}) G_{n-1}(z)", and the product "(1 - z^n)(…)(1 - z^2)(1 - z)/(1 - z)^n".
[^5]: [[aocp-combinatorics](pages/aocp-combinatorics.md)] §"Knuth Goes To Outer Space" L103-131 - "G_n(z)/n! = g_n(z)", "h_k(z) = (1+z+z^2+…+z^{k-1})/k. This is the generating function for the uniform distribution of a random non-negative integer that is less than k", "g_n(z) = h_1(z) h_2(z) … h_n(z)", "E(g_n) = E(h_1) + E(h_2) + … + E(h_n)", "Var(g_n) = Var(h_1) + … + Var(h_n)".
[^6]: https://oeis.org/A008302 (2026-09-19) - "Triangle of Mahonian numbers T(n,k): coefficients in expansion of Product_{i=0..n-1} (1 + x + ... + x^i), where k ranges from 0 to A000217(n-1)", rows "1; 1, 1; 1, 2, 2, 1; 1, 3, 5, 6, 5, 3, 1".
[^7]: Verified by execution (Python 3.11, 2026-10-16): the inversion table of `5 9 1 8 2 6 4 7 3`; `I_n(k) = I_n(k − 1) + I_{n−1}(k)` for `1 ≤ k < n`, `n ≤ 6`, failing first at `(n, k) = (3, 3)`; the `j` with `b_j = n − j` are exactly the elements greater than every element to their right, for every permutation with `n ≤ 6`, and their mean count is `H_n`; the row sums `n!` and the symmetry of `I_n`.
