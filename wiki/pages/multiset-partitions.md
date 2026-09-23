---
title: Multiset partitions
category: Concepts
summary: Splitting a multiset into unordered blocks - Bender's four counting functions c, v, c*, v* (repeated blocks allowed or not, repeated elements within a block allowed or not), the inclusion-exclusion sandwich that computes them, and their OEIS totals when every element appears twice or three times.
tags: [concept, multiset, set-partition, stirling, bell-number, inclusion-exclusion]
sources: [bender-1974-partitions-of-multisets]
created: 2026-09-22
updated: 2026-09-22
---

# Multiset partitions

## Description

A partition of a multiset is a collection of multisets (blocks) whose union with repetition is the original.[^1] For an ordinary set there is one count per block number, the Stirling number of the second kind `S(n,k)`, with the Bell number `B(n)` as its total. For a multiset there are four, set by two yes/no choices:[^1]

| Function | Repeated blocks? | Repeated element inside a block? |
|---|---|---|
| `c(m,k)` | no | no |
| `v(m,k)` | yes | no |
| `c*(m,k)` | no | yes |
| `v*(m,k)` | yes | yes |

The type vector `m = (m_1, m_2, ...)` says that `m_i` distinct elements each appear `i` times. `{a,b,c,c}` has type `(2,1)` and 12 partitions in all. Of these, `ab|c|c` is counted by `v` and `v*` only (the block `c` repeats), and `a|bcc` by `c*` and `v*` only (the block `bcc` repeats `c`).[^2]

**Computing them.** Bender counts onto functions from the multiset to a `k`-set by inclusion-exclusion and divides by `k!`. That gives exact numbers `b(m,k)` and `b*(m,k)`, which bound the four functions: `c <= b <= v` and `c* <= b* <= v*`.[^3] The totals over `k` are Dobinski-shaped sums. When each element appears once, twice, or three times they have closed EGFs.[^3] When repetition is bounded they are asymptotic to a Bell number divided by `prod_i i!^{m_i}`, times a correction factor of the form `exp(-/+ sum_i m_i C(i,2)/s)` with `s log s = M`.[^3]

**Sequences.** The totals are all in OEIS:

| Type | `c` | `v` | `c*` | `v*` |
|---|---|---|---|---|
| each element twice, `(0,n)` | A002718 | A020554 | A094574 | A020555 |
| each element three times, `(0,0,n)` | A060486 | A165434 | A319591 | A322487 |

The `(0,n)` row matches the ingest recomputation of Bender's eq. (11) for `n <= 5`. The `(0,0,n)` row matches eqs. (15)-(17) for `n <= 5`.[^4]

**Not to be confused with** Knuth's multiset *permutations* (ordered words with repeated letters, counted by the multinomial) or with Flajolet's `MSET` construction (building unordered multisets of objects, `exp(sum_k B(z^k)/k)`). Both are covered elsewhere on the wiki.

**One repeated element gives integer partitions** (own reasoning). For the multiset `{a^n}`, a single element repeated `n` times, every block has the form `a^j`. So `v*(·, k)` counts partitions of `n` into `k` parts and `c*(·, k)` counts partitions into `k` distinct parts, with totals `p(n)` (A000041) and A000009. `c` and `v` are trivial there, since no block may repeat `a`. Checked by enumeration for `n <= 12`. The Ferrers rung of [[convex-polyomino-by-area](pages/convex-polyomino-by-area.md)] is therefore Bender's `v*` at one element, and his four-way split generalizes the unrestricted/distinct pair of integer partitions to several elements.

## Appearances in Sources

- [[bender-1974-partitions-of-multisets](pages/bender-1974-partitions-of-multisets.md)] - defines the four functions, the inclusion-exclusion sandwich, the EGFs for `r = 1, 2, 3`, the Bell-number asymptotic, and a cycle-index GF for `v*`.

## Related Concepts

- [[aocp-multisets](pages/aocp-multisets.md)] - multiset permutations; the ordered counterpart.
- [[aocp-binomial-coefficients](pages/aocp-binomial-coefficients.md)] - Stirling numbers of the second kind, the set case of all four functions.
- [[symbolic-method](pages/symbolic-method.md)] - the `MSET` construction, a different operation under the same word.
- [[aocp-multinomial-coefficients](pages/aocp-multinomial-coefficients.md)] - the multinomial counting orderings of a fixed multiset.
- [[convex-polyomino-by-area](pages/convex-polyomino-by-area.md)] - Ferrers diagrams by area, the one-element case of `v*`.

## Footnotes

[^1]: [[bender-1974-partitions-of-multisets](pages/bender-1974-partitions-of-multisets.md)] p.301 §1 Table 1 L25-38 - "A partition of a multiset M is a collection of multisets (called blocks) whose multiset union (i.e., union with repetition) is M. We can either allow or not allow repeated blocks and we can either allow or not allow repeated elements within blocks."
[^2]: [[bender-1974-partitions-of-multisets](pages/bender-1974-partitions-of-multisets.md)] p.302 Table 2 L45-57 - rows "2 | a|bcc | | | x | x" and "3 | ab|c|c | | x | | x".
[^3]: [[bender-1974-partitions-of-multisets](pages/bender-1974-partitions-of-multisets.md)] pp.302-308 [synthesis] L72-113, L241-253 - inclusion-exclusion (1)-(7) with the bounds (3) and (6); Theorem 1 with s log s = M.
[^4]: https://oeis.org/A002718, https://oeis.org/A020554, https://oeis.org/A094574, https://oeis.org/A020555, https://oeis.org/A060486, https://oeis.org/A165434, https://oeis.org/A319591, https://oeis.org/A322487 (2026-09-22) [synthesis] - OEIS sequence search on the recomputed initial terms returned these entries.
