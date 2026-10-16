---
title: Permutation inversions (and the q-factorial)
category: Concepts
summary: An inversion of a permutation is a pair of entries out of order. The permutations of n with k inversions number I_n(k), with generating function the q-factorial G_n(z) = Π_{k=1}^{n} (1 + z + ⋯ + z^{k−1}); I_n(k) is symmetric about C(n,2)/2 and satisfies I_n(k) = I_n(k−1) + I_{n−1}(k) for k < n, and the number of inversions of a uniform random permutation has mean n(n−1)/4 and variance n(n−1)(2n+5)/72. Inversion tables encode permutations as tuples with 0 ≤ b_j ≤ n − j. On the wiki, Dyck words counted by inversions give the Carlitz q-Catalan numbers.
tags: [concept, inversions, permutations, q-factorial, q-analog, generating-functions]
sources: [aocp-combinatorics, aocp-generating-partitions]
created: 2026-09-13
updated: 2026-10-16
---

# Permutation inversions (and the q-factorial)

## Description

An **inversion** of a permutation `a_1 … a_n` of `{1, …, n}` is a pair `(a_i, a_j)` with `i < j` and `a_i > a_j`.[^1] Write `I_n(k)` for the number of permutations of `n` elements with exactly `k` inversions, and `G_n(z) = Σ_k I_n(k) z^k` for their generating function, the **q-factorial**:[^2]

```
G_n(z)  =  Π_{k=1}^{n} (1 + z + ⋯ + z^{k−1})  =  Π_{k=1}^{n} (1 − z^k) / (1 − z)^n.
```

*Example.* The permutations of `{1, 2, 3}` have inversions `123: 0`, `132: 1`, `213: 1`, `231: 2`, `312: 2`, `321: 3`, so `G_3(z) = 1 + 2z + 2z² + z³ = (1 + z)(1 + z + z²)`.

The product form gives three properties:[^3]

- `G_n(1) = n!`.
- `I_n(k) = I_n(C(n, 2) − k)`: reversing a permutation turns its inversions into its non-inversions, and there are `C(n, 2)` pairs.
- `I_n(k) = I_n(k − 1) + I_{n−1}(k)` for `k < n`, from `G_n(z) = (1 + z + ⋯ + z^{n−1}) G_{n−1}(z)`.

Dividing by `n!`, `G_n(z)/n! = h_1(z) h_2(z) ⋯ h_n(z)` with `h_k(z) = (1 + z + ⋯ + z^{k−1})/k`, the generating function of a uniform integer in `{0, …, k − 1}`. So the number of inversions of a uniform random permutation is a sum of independent uniform variables, and its mean and variance add over the factors:[^4]

```
mean  =  Σ_{k=1}^{n} (k − 1)/2  =  n(n − 1)/4,        variance  =  Σ_{k=1}^{n} (k² − 1)/12  =  n(n − 1)(2n + 5)/72.
```

The **inversion table** `b_1 … b_n` of a permutation has `b_j` equal to the number of entries to the left of `j` that exceed `j`, so `0 ≤ b_j ≤ n − j`, and every such tuple is the inversion table of exactly one permutation.[^1] Knuth's example is `5 9 1 8 2 6 4 7 3`, with inversion table `2 3 6 4 0 2 2 1 0`. So the permutations of `n` correspond to the product `{0, …, n−1} × {0, …, n−2} × ⋯ × {0}`, as the towers of height at most `k` on a base of length `L` correspond to `{0, …, k}^L` ([[castle-counting-formula](pages/castle-counting-formula.md)], the Lemma in the section *Tower count*).

## Inversion gradings on the wiki

- **Dyck words by inversions** give the Carlitz q-Catalan numbers, and the inversion number of a Dyck word equals the area of the Ferrers diagram between the word and the path `x…x x̄…x̄` ([[dyck-words](pages/dyck-words.md)], [[q-catalan-numbers](pages/q-catalan-numbers.md)]). Restricted to steep Dyck words, the same statistic gives the q-Motzkin numbers of [[steep-polyominoes-q-motzkin-bessel](pages/steep-polyominoes-q-motzkin-bessel.md)].
- **Permutations of a multiset by inversions** give the q-multinomial coefficient, whose case with all multiplicities 1 is `G_n(z)` ([[aocp-multinomial-coefficients](pages/aocp-multinomial-coefficients.md)], section *Castle readings*).
- **Partitions as multiset permutations.** The partitions of `n` correspond to the permutations of the multiset `{n·0, n·1}` with exactly `n` inversions, through the boundary of the Ferrers diagram read as a 0/1 string, Knuth's rim representation ([[aocp-generating-partitions](pages/aocp-generating-partitions.md)]).

## Appearances in Sources

- [[aocp-combinatorics](pages/aocp-combinatorics.md)] - Knuth's definition of inversions, inversion tables, the generating function `G_n(z)`, its recurrence, and the uniform factors `h_k`.
- [[aocp-generating-partitions](pages/aocp-generating-partitions.md)] - the rim representation of a partition as a 0/1 string.

## Related Concepts

- [[dyck-words](pages/dyck-words.md)] - the inversion number of a Dyck word as the area of a Ferrers diagram.
- [[q-catalan-numbers](pages/q-catalan-numbers.md)], [[steep-polyominoes-q-motzkin-bessel](pages/steep-polyominoes-q-motzkin-bessel.md)] - the q-Catalan and q-Motzkin numbers, with inversions as the q-statistic.
- [[aocp-multinomial-coefficients](pages/aocp-multinomial-coefficients.md)], [[aocp-multisets](pages/aocp-multisets.md)] - permutations of a multiset by inversions and the q-multinomial coefficient.
- [[aocp-permutations](pages/aocp-permutations.md)] - the construction of permutations by inserting each new element into one of the available slots, which gives `n!` as the same product as the inversion tables.
- [[castle-counting-formula](pages/castle-counting-formula.md)] - the towers as a product set `{0, …, k}^L`, the castle analogue of the inversion tables.
- [[castle-notation](pages/castle-notation.md)] - `I_n(k)` and `G_n(z)` here, as distinct from the inscribed-polyomino count `I(w, h)` and its generating function `G_w(x)`.

## Footnotes

[^1]: [[aocp-combinatorics](pages/aocp-combinatorics.md)] §"Permutations and Inversions" L11-34 - "Let a_1 a_2 a_3 \dots a_n be a permutation of the integers {1 \dots n}. If i < j and a_i > a_j, then (a_i, a_j) is an inversion", "b_j is the number of elements to the left of j that are greater than j", the example "5 9 1 8 2 6 4 7 3 / 2 3 6 4 0 2 2 1 0", "0 \leq b_1 \leq n-1, 0 \leq b_2 \leq n-2, \dots, 0 \leq b_{n-1} \leq 1", and "Hall (1956) showed that inversion tables uniquely determine permutations".
[^2]: [[aocp-combinatorics](pages/aocp-combinatorics.md)] §"Counting Inversions with Generating Functions" L71-96 - "G_n(z) = I_n(0) + I_n(1)z + I_n(2) z^2 + \dots = \sum_{k \geq 0} I_n(k) z^k", "G_n(z) = (1 + z + \dots + z^{n-1}) G_{n-1}(z)", and "(1+z+\dots+z^{n-1}) ( \dots )(1+z+z^2)(1+z)(1) = \dfrac{ (1-z^n)( \dots )(1-z^2)(1-z) }{ (1-z)^n }".
[^3]: [[aocp-combinatorics](pages/aocp-combinatorics.md)] §"Counting Inversions with Generating Functions" [synthesis] L69, L84, L90 - the symmetry of `I_n(k)` about `C(n, 2)`, the recurrence `I_n(k) = I_n(k−1) + I_{n−1}(k)` "for k < n", and the product recursion; all three properties, the example and the mean and variance verified by enumeration for `n ≤ 7` (Python 3.11, 2026-10-16).
[^4]: [[aocp-combinatorics](pages/aocp-combinatorics.md)] §"Knuth Goes To Outer Space" L103-131 - "\dfrac{G_n(z)}{n!} = g_n(z)", "h_k(z) = \dfrac{(1+z+z^2+\dots+z^{k-1})}{k}", "This is the generating function for the uniform distribution of a random non-negative integer that is less than k", "g_n(z) = h_1(z) h_2(z) \dots h_n(z)", and the sums of the means and of the variances; the closed forms are the sums of `(k − 1)/2` and `(k² − 1)/12`.
