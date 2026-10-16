---
title: Multiset partitions
category: Concepts
summary: Partitions of a multiset into unordered blocks, counted by Bender's four functions c, v, c*, v* (repeated blocks allowed or not, repeated elements inside a block allowed or not), with the inclusion-exclusion bounds that compute them, the Bell-number asymptotic, and the OEIS totals when every element appears twice or three times. For one element repeated n times, v* and c* are the partitions of n and the partitions of n into distinct parts.
tags: [concept, multiset, set-partition, stirling, bell-number, inclusion-exclusion]
sources: [bender-1974-partitions-of-multisets, aocp-generating-partitions]
created: 2026-09-22
updated: 2026-10-16
---

# Multiset partitions

## Definition

A partition of a multiset is a collection of multisets, the blocks, whose union with repetition is the original multiset.[^1] For a set of `n` elements there is one count per number of blocks `k`, the Stirling number of the second kind `{n k}`, and the total is the Bell number `B(n)` (`A000110`). The wiki writes `{n k}` as on [[aocp-binomial-coefficients](pages/aocp-binomial-coefficients.md)], since `S` is the signed castle count. For a multiset there are four counts, set by two choices:[^1]

| function | repeated blocks allowed? | repeated element inside a block allowed? |
|---|---|---|
| `c(m, k)` | no | no |
| `v(m, k)` | yes | no |
| `c*(m, k)` | no | yes |
| `v*(m, k)` | yes | yes |

The type `m = (m_1, m_2, …)` says that `m_i` distinct elements each appear `i` times, and `M = Σ_i i·m_i` is the number of elements counted with repetition. The totals over `k` are written `c(m)`, `v(m)`, `c*(m)` and `v*(m)`.

*Example.* The multiset `{a, b, c, c}` has type `(2, 1)` and 11 partitions. Of these, `c` counts 4 (`ac|bc`, `abc|c`, `a|bc|c`, `ac|b|c`), `v` counts 6 (those four, `ab|c|c` and `a|b|c|c`, whose block `c` repeats), `c*` counts 9 (all but `ab|c|c` and `a|b|c|c`), and `v*` counts all 11.[^2]

## Counting by inclusion-exclusion

Bender counts the functions from a multiset of type `m` onto a `k`-set by inclusion-exclusion, where copies of the same element may take different values, and divides by `k!`. The result `b*(m, k)` lies between two of the four counts, and restricting the functions to send copies of one element to different values gives `b(m, k)` between the other two:[^3]

```
c*(m, k)  ≤  b*(m, k)  ≤  v*(m, k),        c(m, k)  ≤  b(m, k)  ≤  v(m, k).
```

Their generating functions are[^3]

```
Σ_k b*(m, k) y^k  =  e^{−y} Σ_s (y^s/s!) Π_i C(s + i − 1, i)^{m_i},
Σ_k b(m, k) y^k   =  e^{−y} Σ_s (y^s/s!) Π_i C(s, i)^{m_i}.
```

When each element appears once, twice or three times, the paper derives closed generating functions for all four counts. When the repetition is bounded by a fixed `r`, Bender's Theorem 1 gives, with `s log s = M`,[^4]

```
c(m)  ~  v(m)  ~  b(m)    ~  ( B(M) / Π_i i!^{m_i} ) · exp( − Σ_i m_i C(i, 2)/s ),
c*(m) ~  v*(m) ~  b*(m)   ~  ( B(M) / Π_i i!^{m_i} ) · exp( + Σ_i m_i C(i, 2)/s ).
```

## Sequences

The totals for the types `(0, n)`, each of `n` elements twice, and `(0, 0, n)`, each of `n` elements three times, are in the OEIS:[^5]

| type | `c` | `v` | `c*` | `v*` |
|---|---|---|---|---|
| `(0, n)` | `A002718`: `1, 0, 1, 8, 80, 1088` | `A020554`: `1, 1, 3, 16, 139, 1750` | `A094574`: `1, 1, 5, 40, 457, 6995` | `A020555`: `1, 2, 9, 66, 712, 10457` |
| `(0, 0, n)` | `A060486`: `1, 0, 0, 5, 205` | `A165434`: `1, 1, 4, 39, 862` | `A319591`: `1, 2, 17, 364, 14595` | `A322487`: `1, 3, 31, 686, 27036` |

The values are listed from `n = 0`. Every entry agrees with enumeration of all multiset partitions, for `n ≤ 5` in the first row and `n ≤ 4` in the second.[^6]

## One element repeated

**Proposition.** For the multiset `{a^n}`, one element repeated `n` times, `v*(·, k)` is the number of partitions of `n` into `k` parts and `c*(·, k)` the number of partitions of `n` into `k` distinct parts, so the totals are `p(n)` (`A000041`) and the number of partitions of `n` into distinct parts (`A000009`). For `n ≥ 2`, `c = 0` and `v = 1`.

*Proof.* Every block has the form `a^j`, so a partition into `k` blocks is a multiset of `k` positive integers summing to `n`, a partition of `n` into `k` parts; forbidding repeated blocks makes the parts distinct. Forbidding a repeated element inside a block forces every block to be `a`, so the only partition is `a|a|…|a`, which repeats its block when `n ≥ 2`.

Checked by enumeration for `n ≤ 7`.[^6] The Ferrers diagrams counted by area on [[convex-polyomino-by-area](pages/convex-polyomino-by-area.md)] are the partitions of `n`, so they are `v*` at one element.

## Other uses of the word

Knuth's multiset permutations are ordered words with repeated letters, counted by the multinomial coefficient ([[aocp-multisets](pages/aocp-multisets.md)], [[aocp-multinomial-coefficients](pages/aocp-multinomial-coefficients.md)]). Flajolet and Sedgewick's `MSET` construction builds unordered multisets of objects from a class with generating function `G(z)`, with generating function `exp(Σ_k G(z^k)/k)` ([[symbolic-method](pages/symbolic-method.md)]). Neither is a partition of a fixed multiset.

## Appearances in Sources

- [[bender-1974-partitions-of-multisets](pages/bender-1974-partitions-of-multisets.md)] - the four counting functions, the inclusion-exclusion bounds and generating functions, the closed forms for each element appearing once, twice or three times, the Bell-number asymptotic, and a cycle-index generating function for `v*`.

## Related Concepts

- [[aocp-binomial-coefficients](pages/aocp-binomial-coefficients.md)] - the Stirling numbers of the second kind `{n k}`, which all four counts equal when every element appears once.
- [[aocp-multisets](pages/aocp-multisets.md)] - permutations of a multiset, the ordered counterpart.
- [[aocp-multinomial-coefficients](pages/aocp-multinomial-coefficients.md)] - the multinomial coefficient, which counts the orderings of a fixed multiset.
- [[symbolic-method](pages/symbolic-method.md)] - the `MSET` construction.
- [[convex-polyomino-by-area](pages/convex-polyomino-by-area.md)] - Ferrers diagrams by area, the one-element case of `v*`.
- [[aocp-generating-partitions](pages/aocp-generating-partitions.md)] - Knuth's generators of integer partitions; the Hindenburg algorithm with the staircase shift lists the partitions into `k` distinct parts counted by `c*(·, k)` at one element.
- [[hoodoo-monadnock-castles](pages/hoodoo-monadnock-castles.md)] - castles whose two sides are partitions into distinct parts.

## Footnotes

[^1]: [[bender-1974-partitions-of-multisets](pages/bender-1974-partitions-of-multisets.md)] p.301 §1 Table 1 L25-38 - "A partition of a multiset M is a collection of multisets (called blocks) whose multiset union (i.e., union with repetition) is M. We can either allow or not allow repeated blocks and we can either allow or not allow repeated elements within blocks."
[^2]: [[bender-1974-partitions-of-multisets](pages/bender-1974-partitions-of-multisets.md)] p.302 Table 2 [synthesis] L41-57 - the 11 partitions of `{a, b, c, c}` with the functions that count each; the tallies 4, 6, 9, 11 recomputed by enumeration (Python 3.11, 2026-10-16).
[^3]: [[bender-1974-partitions-of-multisets](pages/bender-1974-partitions-of-multisets.md)] §2 pp.302-304 L72-113 - "By inclusion-exclusion, (1) N_=(K) = sum_{X subset K} (-1)^{|K|-|X|} N_<=(X)", "(3) c*(m,k) <= N_=(K)/k! <= v*(m,k)", "(5) sum_k b*(m,k) y^k = e^{-y} sum_s (y^s/s!) prod_i C(s+i-1, i)^{m_i}", "(6) c(m,k) <= b(m,k) <= v(m,k)", "(7) sum_k b(m,k) y^k = e^{-y} sum_s (y^s/s!) prod_i C(s,i)^{m_i}".
[^4]: [[bender-1974-partitions-of-multisets](pages/bender-1974-partitions-of-multisets.md)] §6 pp.307-308 L241-253 - "Theorem 1. Let r be fixed and let B(M) be the number of partitions of an M element set. Then we have uniformly, as m in Z^r is such that M = sum i m_i -> infinity, c(m) ~ v(m) ~ b(m) ~ (B(M)/prod_i i!^{m_i}) exp{ - sum_i m_i C(i,2)/s } and c*(m) ~ v*(m) ~ b*(m) ~ (B(M)/prod_i i!^{m_i}) exp{ + sum_i m_i C(i,2)/s }, where s log s = M".
[^5]: https://oeis.org/A002718, https://oeis.org/A020554, https://oeis.org/A094574, https://oeis.org/A020555, https://oeis.org/A060486, https://oeis.org/A165434, https://oeis.org/A319591, https://oeis.org/A322487 (read 2026-10-16) - "Number of bicoverings of an n-set", "Number of multigraphs on n labeled edges (without loops)", "Number of (<=2)-covers of an n-set", "Number of multigraphs on n labeled edges (with loops)", "Tricoverings of an n-set", "Number of tri-coverings of a set", "Number of nonnegative integer matrices with n columns and any number of nonzero distinct rows with every column summing to 3 up to permutation of rows", "Number of (3*n) X n matrices with nonnegative integer entries and each column sum being 3 up to permutation of rows", with the data listed in the table.
[^6]: Verified by execution (Python 3.11, 2026-10-16): enumeration of all multiset partitions of the types `(0, n)` for `n ≤ 5` and `(0, 0, n)` for `n ≤ 4`, classified by repeated blocks and repeated elements, against the eight OEIS rows; the four counts of `{a, b, c, c}`; and `{a^n}` for `n ≤ 7` (`c = 0`, `v = 1`, `c*` and `v*` the partitions of `n` into distinct parts and into any parts).
