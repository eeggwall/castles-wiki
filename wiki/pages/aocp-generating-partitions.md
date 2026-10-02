---
title: "AOCP Generating All Partitions (Knuth TAOCP Vol. 4A §7.2.1.4)"
category: Sources
summary: "Knuth's section on integer partitions - Algorithm P (all partitions, reverse lexicographic), the Hindenburg algorithm (Algorithm H, partitions into exactly m parts, colex), the part-count and rim representations, Euler's product and pentagonal recurrence, Hardy-Ramanujan-Rademacher asymptotics, the triangle of partitions into m parts with its recurrence and GF, Cauchy's Theorem C for partitions in a box, and Savage's partition Gray code. Exercise 34's staircase shift turns the Hindenburg algorithm into a generator of distinct-part partitions, which are the sides of hoodoo and monadnock castles."
tags: [knuth, taocp, source, partitions, distinct-parts, generation, hindenburg-algorithm, euler, hardy-ramanujan, gaussian-binomial, gray-code, hoodoo-castle, monadnock-castle]
sources: [aocp-generating-partitions]
created: 2026-10-02
updated: 2026-10-02
---

# AOCP Generating All Partitions (Knuth, *The Art of Computer Programming*, Vol. 4A §7.2.1.4)

**Source:** `assets/knuth-taocp-4a-7.2.1.4-generating-all-partitions.pdf` - Donald E. Knuth, *The Art of Computer Programming*, Vol. 4A, *Combinatorial Algorithms, Part 1* (2011), §7.2.1.4 "Generating all partitions", pp. 390-415. The PDF is a scan with no text layer and is git-ignored; it is cited by book page.
**Date ingested:** 2026-10-02
**Type:** book section (algorithms, enumeration, asymptotics, 73 exercises)

## Notation used on this page

The wiki keeps `q` for area and `P(k, L)` for the signed tower count ([[castle-notation](pages/castle-notation.md)]), so three of Knuth's symbols are renamed here. Footnote quotes keep Knuth's symbols.

| Knuth | meaning | written here as |
|---|---|---|
| `p(n)` | partitions of `n` | `p(n)` |
| `q(n)` (ex. 21) | partitions of `n` into distinct parts | `pd(n)` |
| `\|n m\|` (vertical bars, eq. 38) | partitions of `n` into exactly `m` parts | `part(n, m)` |
| `P(z)` | Euler's generating function `Σ p(n) z^n` | `Σ p(n) z^n` (written out) |
| Algorithm H of §7.2.1.4 | partitions of `n` into `m` parts | **the Hindenburg algorithm** |

Knuth reuses the label "Algorithm H" in neighbouring sections: §7.2.1.1 for loopless reflected mixed-radix Gray generation (the wiki's **loopless Gray algorithm**, [[castle-gray-code](pages/castle-gray-code.md)]) and §7.2.1.5 for restricted growth strings. Only the §7.2.1.4 one is meant below.

## Summary

The section opens with the Twelvefold Way, the twelve ways of putting `n` balls into `m` urns with balls and urns labeled or not, and the urns optionally holding at least one ball or at most one ball. It then takes up the five entries that involve partitions.[^1] A partition of `n` is a weakly decreasing sequence of positive parts summing to `n`. Two generators are given. **Algorithm P** visits all partitions in reverse lexicographic order, from `n` down to `11…1`. The **Hindenburg algorithm** (Knuth's Algorithm H, from Hindenburg's 1779 dissertation) visits the partitions of `n` into exactly `m` parts in colex order.[^2] Its cost is linear in its output: Theorem H bounds the accumulated work by `3·part(n, m) + m`.[^3]

The counting half starts from Euler's product `Π 1/(1 − z^m)`, the pentagonal-number identity and its recurrence for `p(n)`, and Dedekind's functional equation, which leads to the Hardy-Ramanujan-Rademacher series and the leading term `p(n) ≈ e^{π√(2n/3)}/(4n√3)`.[^4] For partitions into exactly `m` parts it gives the recurrence `part(n, m) = part(n − 1, m − 1) + part(n − m, m)`, the generating function `z^m/((1 − z)(1 − z²)…(1 − z^m))`, and a table for `n, m ≤ 11`.[^5] Partitions in an `m × l` box are counted by a Gaussian binomial (Theorem C, due to Cauchy).[^6] Ferrers diagrams, conjugation, the Durfee square and the **rim representation** tie partitions to lattice paths: the boundary of a partition of `n` is a 0/1 string with `n` zeros, `n` ones and exactly `n` inversions.[^7] The section ends with Savage's Gray code, in which consecutive partitions differ by moving one dot.[^8]

The exercises carry most of the distinct-part material. Exercise 34 is the staircase shift: subtracting `m − 1, m − 2, …, 0` from a partition into `m` distinct parts leaves a partition of `n − m(m − 1)/2` into `m` parts. It also gives the estimate `part(n, m) ≈ n^{m−1}/(m!(m − 1)!)` for `m ≤ n^{1/3}`.[^9] Exercise 12 is Euler's theorem that distinct parts and odd parts are equinumerous, exercise 14 is Sylvester's refinement by the number of "gaps", exercise 21 asks for `pd(n)` from `p(n)`, and exercise 47 is the Nijenhuis-Wilf uniform random-partition generator.[^10]

## Key Takeaways

- **The Hindenburg algorithm plus the staircase shift generates every hoodoo and monadnock castle side.** A side of `m` steps rising by `n` is a partition of `n` into `m` distinct parts. Run the Hindenburg algorithm on `(n − m(m − 1)/2, m)` and add `(m − 1, m − 2, …, 0)` to each output, which gives the steps largest first. That is a monadnock rising side as is and a hoodoo rising side reversed. Adding a fixed vector preserves colex order, so the sides come out in colex order, at constant amortized cost by Theorem H. Implemented and checked on [[hoodoo-monadnock-castles](pages/hoodoo-monadnock-castles.md)].[^2][^3][^9]
- **The side counts are Knuth's `part(n, m)` shifted.** Sides of `m` steps with rise `n` number `part(n − m(m − 1)/2, m)`, so recurrence (39), GF (41) and Table 2 count them, and exercise 34's estimate gives the polynomial growth of hoodoo counts in `h` at fixed width.[^5][^9]
- **Knuth's asymptotics cover `p(n)`, not `pd(n)`.** The large-width hoodoo count by height needs the distinct-part asymptotic, taken from OEIS A000009 on [[hoodoo-monadnock-castles](pages/hoodoo-monadnock-castles.md)]. Knuth's eq. (36) is used there only to compare that count with `p(2(h − 1))`.[^4]
- **Ferrers castles in a fixed `(w, h)` cell are counted by area by Theorem C.** A Ferrers castle has `c_1 = h ≥ c_2 ≥ … ≥ c_w ≥ 1`; lowering the last `w − 1` columns by one leaves a partition in a `(w − 1) × (h − 1)` box, so by area the cell is `q^{h+w−1} [w + h − 2, w − 1]_q` (checked by enumeration for `w ≤ 6`, `h ≤ 5`).[^6]
- **The rim representation is the inversion grading.** A partition of `n` is a permutation of the multiset `{n·0, n·1}` with exactly `n` inversions, the same area = inversions correspondence that [[permutation-inversions](pages/permutation-inversions.md)] uses for Dyck words.[^7]

## Entities & Concepts

- [[hoodoo-monadnock-castles](pages/hoodoo-monadnock-castles.md)] - the castle families whose sides are partitions into distinct parts; generated here by the Hindenburg algorithm.
- [[castle-classification-shape](pages/castle-classification-shape.md)] - the catalogue entries for hoodoo, monadnock and Ferrers castles.
- [[multiset-partitions](pages/multiset-partitions.md)] - partitions into parts and into distinct parts as the one-element case of Bender's multiset partitions.
- [[permutation-inversions](pages/permutation-inversions.md)] - the rim representation as multiset permutations with `n` inversions.
- [[castle-q-bessel-closed-form](pages/castle-q-bessel-closed-form.md)] - the "partition in a box" Gaussian binomials of Theorem C.
- [[castle-gray-code](pages/castle-gray-code.md)] - the other Algorithm H (§7.2.1.1), and Gray codes in general.
- [[castle-samplers](pages/castle-samplers.md)] - where a Nijenhuis-Wilf-style sampler would sit.

## Relation to Other Wiki Pages

This is the wiki's second Vol. 4A source, after the tuple and Gray-code notes of [[aocp-generating-permutations-tuples](pages/aocp-generating-permutations-tuples.md)] (§7.2.1.1-7.2.1.2). Those sections walk the whole cube `{1..h}^w`; this one generates a restricted class directly. For the castle the restricted class is the set of sides of [[hoodoo-monadnock-castles](pages/hoodoo-monadnock-castles.md)], so those two families are enumerated with no filtering at all.

Theorem C is the classical source of the Gaussian binomials already used on [[castle-q-bessel-closed-form](pages/castle-q-bessel-closed-form.md)] (towers with no descent by area) and gives the Ferrers row of [[castle-classification-shape](pages/castle-classification-shape.md)] its `(w, h)`-cell count by area. The rim representation joins the inversion grading of [[aocp-combinatorics](pages/aocp-combinatorics.md)] and [[permutation-inversions](pages/permutation-inversions.md)].

Not used on the wiki: the Erdős-Lehner distribution of the number of parts (Theorem E), Temperley's limiting shape, the majorization lattice (exercises 54-58), and Bulgarian solitaire (exercises 70-72).

## Footnotes

[^1]: [[aocp-generating-partitions](pages/aocp-generating-partitions.md)] p.390-391 [synthesis] - Table 1 "The Twelvefold Way" (balls labeled or unlabeled, urns labeled or unlabeled, at most one / at least one ball per urn); "we can complete our study of classical combinatorial mathematics by learning about the remaining five entries in the table, which all involve partitions."
[^2]: [[aocp-generating-partitions](pages/aocp-generating-partitions.md)] p.392 - "Algorithm P (Partitions of n in reverse lexicographic order)"; "Another simple algorithm is available when we want to generate all partitions of n into a fixed number of parts", "featured in C. F. Hindenburg's 18th-century dissertation [Infinitinomii Dignitatum Exponentis Indeterminati (Göttingen, 1779), 73-91]", which "visits the partitions in colex order"; "Algorithm H (Partitions of n into m parts)", steps H1-H6, and list (7) for `n = 11`, `m = 4`: "8111, 7211, 6311, 5411, 6221, 5321, 4421, 4331, 5222, 4322, 3332".
[^3]: [[aocp-generating-partitions](pages/aocp-generating-partitions.md)] p.393 - "the total running time of Algorithm H is at most a small constant times the number of partitions visited, plus O(m)"; p.404 Theorem H [synthesis] - the cost measure `c_m(n)` of Algorithm H is at most three times the number of partitions of `n` into `m` parts, plus `m`.
[^4]: [[aocp-generating-partitions](pages/aocp-generating-partitions.md)] pp.395-399 [synthesis] - Euler's product (17), the pentagonal identity (18) and recurrence (20), Theorem D (Dedekind), the Hardy-Ramanujan-Rademacher formula (32), and the leading term (36) `p(n) = e^{π√(2n/3)}/(4n√3) (1 + O(n^{−1/2}))`.
[^5]: [[aocp-generating-partitions](pages/aocp-generating-partitions.md)] pp.399-400 [synthesis] - notation (38) "for the number of partitions of n that have exactly m parts"; recurrence (39), "because" the first term "counts the partitions whose smallest part is 1" and the second "counts the others"; generating function (41) `z^m/((1−z)(1−z²)…(1−z^m))`; Table 2 "Partition numbers" for `0 ≤ n, m ≤ 11`.
[^6]: [[aocp-generating-partitions](pages/aocp-generating-partitions.md)] p.403 Theorem C - "The number of partitions of n that have no more than m parts and no part larger than l is" `[z^n]` of the Gaussian binomial `(l+m choose m)_z`; "This result is due to A. Cauchy".
[^7]: [[aocp-generating-partitions](pages/aocp-generating-partitions.md)] pp.394-395 [synthesis] - Ferrers diagrams, the Durfee square and conjugation; the rim representation as a path from the lower left to the upper right corner of an `n × n` square, with "every permutation of the multiset {n·0, n·1} that has exactly n inversions" corresponding "to a partition of n."
[^8]: [[aocp-generating-partitions](pages/aocp-generating-partitions.md)] pp.405-407 [synthesis] - "A Gray code for partitions": the successor obtained by `a_j ← a_j + 1` and `a_k ← a_k − 1`, unique for `n = 6`; Carla D. Savage's construction (J. Algorithms 10 (1989)) and Theorem S.
[^9]: [[aocp-generating-partitions](pages/aocp-generating-partitions.md)] p.411 exercise 34 [synthesis] - the number of partitions of `n − m(m−1)/2` into `m` parts "is the number of partitions of n into m distinct parts", and consequently the number of partitions of `n` into `m` parts is `n^{m−1}/(m!(m−1)!) (1 + O(m³/n))` "when m ≤ n^{1/3}".
[^10]: [[aocp-generating-partitions](pages/aocp-generating-partitions.md)] pp.408-411 [synthesis] - exercise 12 (Euler: distinct parts and odd parts); exercise 14 (Sylvester: distinct-part partitions with "exactly k 'gaps' where a_j > a_{j+1} + 1"); exercise 21 ("Let q(n) be the number of partitions of n into distinct parts"); exercise 47 (Nijenhuis and Wilf: a random partition "with equal probability" from a table of `p(0), …, p(n)`).
