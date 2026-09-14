---
title: Monotone streak factorization
category: Concepts
summary: Factoring the first-difference sequence d_i = c_{i+1}−c_i into up/flat/down streaks — an O(L) scan (Knuth's cycle loop analogue) the fast castle-counting algorithms sum over.
tags: [concept, castle, factorization, algorithms, kitamasa, berlekamp-massey]
sources: [project-euler-502-castle-factoring]
created: 2026-09-13
updated: 2026-09-13
---

# Monotone streak factorization

## Description

The **monotone streak factorization** is the run-length canonical form of a castle that the fast counting algorithms sum over. Represent a castle by its column heights `c_i` (the integer-tuple [[castle-representations](pages/castle-representations.md)]) and take first differences:[^1]

```
d_i = c_{i+1} − c_i,    c_0 = c_{L+1} = 0
```

Factor the `d` sequence into maximal **up-streaks** (`d_i > 0`), **flat runs** (`d_i = 0`), and **down-streaks** (`d_i < 0`). Three facts make this the useful canonical form:[^2]

- Each `D` move completes one block, so the **block count = number of `D` moves = total descent** `∑ max(0, c_i − c_{i+1})` = the sum of the magnitudes of the down-streaks (the sign-carrying atoms of the [[castle-sign](pages/castle-sign.md)]).
- The factorizer is a single **`O(L)` scan** — the castle analogue of Knuth's `O(n)` cycle-following loop.
- The flat-run lengths between vertical moves are the widths of gaps and sub-blocks.

## Fast algorithms

The counting algorithms read as sums over these canonical forms:[^3]

- **Unsigned count.** `T(k,L) = (k+1)^L` is a product form because the `L` column heights are independent — equivalently, the peaks are independent excursions.
- **Signed count.** `P(k,L) = ∑_{c ∈ {0,…,k}^L} (−1)^{descent(c)}`, following the rational-function update
  ```
  num_k = 2·den_{k−1} − num_{k−1}
  den_k = den_{k−1}(1 − 2x) + x·num_{k−1}
  ```
  (the same recurrence on the [[castle-counting-formula](pages/castle-counting-formula.md)]), evaluated in `O(k² log L)` by **Kitamasa** in the *L* direction, or in the *k* direction by [[berlekamp-massey](pages/berlekamp-massey.md)]. This is how the Solution subpage computes `F(10^12, 100)` and `F(100, 10^12)` — the large-parameter evaluations the [[castle-counting-function](pages/castle-counting-function.md)] requires.[^3]

The streak factorization is thus the bridge between the combinatorial reading (peaks, blocks, signs) and the fast linear-recurrence evaluation that makes the trillion-scale grid parameters computable.

## Appearances in Sources

- [[project-euler-502-castle-factoring](pages/project-euler-502-castle-factoring.md)] — defines the `d`-sequence streak factorization and connects it to the unsigned/signed fast algorithms.

## Related Concepts

- [[castle-representations](pages/castle-representations.md)] — the column-height representation this factors.
- [[castle-sign](pages/castle-sign.md)] — the down-streaks carry the sign.
- [[castle-counting-formula](pages/castle-counting-formula.md)] — the `T` and `P` this factorization computes.
- [[berlekamp-massey](pages/berlekamp-massey.md)] — the *k*-direction fast-recurrence method paired with Kitamasa here.
- [[permutation-cycle-castle-analogy](pages/permutation-cycle-castle-analogy.md)] — the `O(L)` scan as Knuth's cycle loop.

## Footnotes

[^1]: [[project-euler-502-castle-factoring](pages/project-euler-502-castle-factoring.md)] §"Monotone streak factorization and fast algorithms" L169-175 — "take first differences d_i = c_{i+1} - c_i with c_0 = c_{L+1} = 0. Factor the d sequence into maximal up-streaks (d_i > 0), flat runs (d_i = 0), and down-streaks (d_i < 0)."
[^2]: [[project-euler-502-castle-factoring](pages/project-euler-502-castle-factoring.md)] §"Monotone streak factorization and fast algorithms" L177-181 — "the number of blocks equals the number of D moves, the total descent ∑ max(0, c_i - c_{i+1}), and the sum of the magnitudes of the down-streaks ... a single O(L) scan, the castle version of Knuth's O(n) cycle-following loop ... The flat-run lengths ... are the widths of gaps and sub-blocks."
[^3]: [[project-euler-502-castle-factoring](pages/project-euler-502-castle-factoring.md)] §"Monotone streak factorization and fast algorithms" L183-192 — "T(k,L) = (k+1)^L is a product form ... P(k,L) = ∑ (-1)^{descent(c)} ... num_k = 2 den_{k-1} - num_{k-1}, den_k = den_{k-1}(1-2x) + x num_{k-1} ... evaluated in O(k^2 log L) by Kitamasa in the L direction, or ... by Berlekamp-Massey, which is how [Solution] computes F(10^12, 100) and F(100, 10^12)."
