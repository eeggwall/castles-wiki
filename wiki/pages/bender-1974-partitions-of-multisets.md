---
title: "Partitions of Multisets (Bender, 1974)"
category: Sources
summary: Bender's eleven-page Discrete Math. paper - four partition numbers c, v, c*, v* for a multiset (repeated blocks allowed or not, repeated elements within a block allowed or not), one inclusion-exclusion formula that sandwiches them, closed EGFs when every element appears once, twice, or three times, a Bell-number asymptotic for bounded repetition, and a de Bruijn / cycle-index generating function for v*.
tags: [source, paper, bender, multiset, set-partition, stirling, bell-number, inclusion-exclusion, egf, asymptotics, de-bruijn, cycle-index, comtet, oeis]
sources: [bender-1974-partitions-of-multisets]
created: 2026-09-22
updated: 2026-10-16
---

# Partitions of Multisets (Bender, 1974)

**Source:** `raw/bender-1974-partitions-of-multisets.txt`, a transcription of the paper from its page images (the PDF is not in the repository)
**Publication:** Edward A. Bender, "Partitions of Multisets," Discrete Mathematics 9 (1974) 301-311, North-Holland. Institute for Defense Analyses, Princeton.[^1]
**Date ingested:** 2026-09-22
**Type:** paper

Not to be confused with Bender's "Convex n-ominoes" (Discrete Math. 8, 1974; [[bender-1974-convex-n-ominoes](pages/bender-1974-convex-n-ominoes.md)]), the source of the convex-polyomino growth constant; this paper has no polyominoes and no area statistic.

## Summary

A set has one partition number per block count, the Stirling number of the second kind. A multiset has four, because two independent choices open up once elements repeat: whether two blocks may be equal, and whether a block may itself contain a repeated element. Bender names them `c(m,k)` (neither allowed), `v(m,k)` (repeated blocks allowed), `c*(m,k)` (multiset blocks allowed), and `v*(m,k)` (both), where the type vector `m` records that exactly `m_i` distinct elements appear exactly `i` times.[^2] The paper's worked example is `{a,b,c,c}`, type `(2,1)`, whose 11 partitions split `c = 0,2,2,0`, `v = 0,2,3,1`, `c* = 1,5,3,0`, `v* = 1,5,4,1` over `k = 1..4`.[^3]

The method is a single inclusion-exclusion count of onto functions from the multiset to a `k`-set. Onto functions overcount a partition by `k!/prod_i (i!)^{v_i}`, where `v_i` is the number of distinct blocks repeated exactly `i` times, so the normalized count `b*(m,k)` lands between `c*` and `v*`; restricting to functions that send copies of one element to different targets gives `b(m,k)` between `c` and `v`.[^4] Summing over `k` turns both into series of the same shape as Dobinski's formula for the Bell numbers,[^15] `e^{-y} sum_s (y^s/s!) prod_i C(s+i-1,i)^{m_i}` and `e^{-y} sum_s (y^s/s!) prod_i C(s,i)^{m_i}`.[^5] For `m = (n)` this collapses to the classical `exp{y(e^x - 1)}`.[^6] For `m = (0,n)` (every element twice) the correction for repeated blocks is one extra `C_1` factor, which gives four closed EGFs, two of them Comtet's.[^7] For `m = (0,0,n)` (every element three times) the correction is subtler, since a doubled block and a tripled block can interact; Bender handles it with a second inclusion-exclusion plus a lemma on the nonnegative-part operator `P_x`, and ends with four EGFs of the same shape.[^8]

Two results reach past the explicit cases. Theorem 1: with repetition bounded by a fixed `r`, all six counts `c, v, b` and `c*, v*, b*` are asymptotic to `B(M)/prod_i i!^{m_i}` times `exp{-sum_i m_i C(i,2)/s}` or `exp{+sum_i m_i C(i,2)/s}`, where `M = sum i m_i`, `s log s = M`, and `B(M)` is the Bell number, the number of partitions of a set of `M` elements; the proof is a saddle-point estimate of the Dobinski-shaped sum plus a bound showing repeated blocks are asymptotically negligible.[^9] Table 3 tests it at `m = (0,0,10)` and `(0,0,20)`.[^10] Theorem 2 gives `V_r*`, the EGF of `v*` for `r` copies of each of `n` elements, as a differential operator in the cycle index of `S_r`, derived from de Bruijn's form of Pólya counting; `r = 4` is written out explicitly.[^11]

## Key Takeaways

- **The bounds.** `c(m,k) <= b(m,k) <= v(m,k)` and `c*(m,k) <= b*(m,k) <= v*(m,k)`, with `b` and `b*` exactly computable by inclusion-exclusion; for an ordinary set all four equal the Stirling number of the second kind `{n k}`.[^4][^3]
- **Dobinski generalized.** Eq. (18), `b(m) = e^{-1} sum_{s>=0} prod_i C(s,i)^{m_i}/s!`, reduces at `m = (n)` to Dobinski's formula `B(n) = e^{-1} sum_s s^n/s!` for the Bell numbers.[^12][^15]
- **Closed EGFs for `r = 1, 2, 3`.** Eqs. (8), (11), (15)-(17); the `r = 2` pair for `c` and `v` is Comtet's (1968), rederived by Baróti with linear operators.[^6][^7][^8]
- **Repeated blocks don't matter asymptotically.** `c(m) ~ v(m)` and `c*(m) ~ v*(m)` under bounded repetition, so each pair shares one Bell-number asymptotic.[^9]
- **Cycle-index route.** `v*` is also a count of equivalence classes of functions under `S_r + ... + S_r` acting on the domain and `S_k` on the range, which is where de Bruijn's theorem enters.[^11]

### Totals

Over all `k`, the multisets in which each of `n` elements appears twice have[^16]

```
c  =  0, 1, 8, 80, 1088        v   =  1, 3, 16, 139, 1750
c* =  1, 5, 40, 457, 6995      v*  =  2, 9, 66, 712, 10457          (n = 1, …, 5)
```

partitions, and those in which each appears three times have `c = 0, 0, 5`, `v = 1, 4, 39`, `c* = 2, 17, 364`, `v* = 3, 31, 686` for `n = 1, 2, 3`. These are the OEIS sequences, each at index `n`: for every element twice, `c` is A002718 ("Number of bicoverings of an n-set"), `v` is A020554 ("Number of multigraphs on n labeled edges (without loops)"), `c*` is A094574 ("Number of (<=2)-covers of an n-set") and `v*` is A020555 ("Number of multigraphs on n labeled edges (with loops)").[^13] For every element three times, `c` is A060486 ("Tricoverings of an n-set"), `v` is A165434 ("Number of tri-coverings of a set"), `c*` is A319591 and `v*` is A322487.[^14] Table 3's counts at `m = (0, 0, 10)` and `(0, 0, 20)` agree with EGFs (15)-(17) to the three digits printed.[^10]

## Entities & Concepts

- [[multiset-partitions](pages/multiset-partitions.md)] - the four counting functions and the inclusion-exclusion bounds.
- [[aocp-multisets](pages/aocp-multisets.md)] - multiset *permutations* (ordered words, the multinomial); this paper counts the unordered splittings of the same objects.
- [[aocp-binomial-coefficients](pages/aocp-binomial-coefficients.md)] - Stirling numbers of the second kind, the `m = (n)` case of all four counts.
- [[symbolic-method](pages/symbolic-method.md)] - Flajolet's `MSET` construction builds unordered multisets of objects; Bender partitions a fixed multiset, a different operation.
- [[aocp-permutations](pages/aocp-permutations.md)] - Stirling's formula for `s!`; the paper takes the asymptotic `B(M) ~ (s/e)^M e^{s−1}/√(log s)` as "well-known".

## Relation to Other Wiki Pages

Knuth's pages treat permutations of a multiset and the multinomial ([[aocp-multisets](pages/aocp-multisets.md)], [[aocp-multinomial-coefficients](pages/aocp-multinomial-coefficients.md)]); this paper supplies the partition side of the same objects, beyond the Stirling-number identities on [[aocp-binomial-coefficients](pages/aocp-binomial-coefficients.md)].

**A homonym to keep apart.** Bender's "blocks" are the parts of a partition. On castle pages, a block is a height-1, integer-length rectangle ([[project-euler-502](pages/project-euler-502.md)]), and the block count is the statistic filtered on [[block-count-constraints](pages/block-count-constraints.md)]. The two uses are unrelated.

**The wiki's reading, not in the paper.** Castles glued at height-1 columns form a free monoid on the prime castles ([[prime-castles](pages/prime-castles.md)]), so the castles built from a given multiset of primes correspond to the orderings of that multiset and are counted by a multinomial coefficient ([[signed-prime-castles](pages/signed-prime-castles.md)]); Bender's numbers count unordered groupings instead.

## Footnotes

[^1]: [[bender-1974-partitions-of-multisets](pages/bender-1974-partitions-of-multisets.md)] p.301 L3-11 - "DISCRETE MATHEMATICS 9 (1974) 301-311 ... PARTITIONS OF MULTISETS / Edward A. BENDER / Institute for Defense Analyses, Princeton, N.J. 08540, USA / Received 25 October 1973"
[^2]: [[bender-1974-partitions-of-multisets](pages/bender-1974-partitions-of-multisets.md)] p.301 §1 L25-38 - "A multiset of type m is a multiset in which exactly m_i different elements appear exactly i times ... We can either allow or not allow repeated blocks and we can either allow or not allow repeated elements within blocks. Therefore, we have four ways to count the number of partitions into k blocks of a multiset of type m."
[^3]: [[bender-1974-partitions-of-multisets](pages/bender-1974-partitions-of-multisets.md)] p.302 Table 2 and §1 [synthesis] L41-59 - the 11 partitions of {a,b,c,c} with their c/v/c*/v* marks, per-k tallies computed from the table; "In the classical case m = (n), all four numbers equal the Stirling numbers of the second kind."
[^4]: [[bender-1974-partitions-of-multisets](pages/bender-1974-partitions-of-multisets.md)] pp.302-303 §2 [synthesis] L72-108 - N_=(K) by inclusion-exclusion (1); "pi corresponds to precisely k!/prod_i (i!)^{v_i(pi)} onto functions"; (3) c*(m,k) <= N_=(K)/k! <= v*(m,k); restricting copies to different targets gives (6) c(m,k) <= b(m,k) <= v(m,k).
[^5]: [[bender-1974-partitions-of-multisets](pages/bender-1974-partitions-of-multisets.md)] pp.303-304 eqs. (5), (7) L102, L113 - "sum_k b*(m,k) y^k = e^{-y} sum_s (y^s/s!) prod_i C(s+i-1, i)^{m_i}" and "sum_k b(m,k) y^k = e^{-y} sum_s (y^s/s!) prod_i C(s,i)^{m_i}"
[^6]: [[bender-1974-partitions-of-multisets](pages/bender-1974-partitions-of-multisets.md)] p.304 §3 eq. (8) L119-126 - "This is the case of ordinary set partitions ... C_1(x,y) = sum_{n,k} c((n),k) y^k x^n/n! = exp{y(e^x - 1)}."
[^7]: [[bender-1974-partitions-of-multisets](pages/bender-1974-partitions-of-multisets.md)] pp.304-305 §4 [synthesis] L130-151 - (9)-(10) "the C_1 factor counts those blocks which appear twice"; the four EGFs (11) for C, V, C*, V*; "The first two were discovered by Comtet [2]."
[^8]: [[bender-1974-partitions-of-multisets](pages/bender-1974-partitions-of-multisets.md)] pp.305-307 §5 [synthesis] L155-235 - Lemma 1 on P_x, the construction of a (m,0,n) partition from pi_1, pi_2, pi_3 with inclusion-exclusion on pi_1 intersect pi_2, and the resulting EGFs (15), (16), C_3*, (17).
[^9]: [[bender-1974-partitions-of-multisets](pages/bender-1974-partitions-of-multisets.md)] pp.307-309 §6 [synthesis] L241-318 - Theorem 1 statement (L241-248, "where s log s = M" L251); saddle-point estimate (18)-(19) for b(m); (20)-(23) bound (v(m) - c(m))/v(m) -> 0.
[^10]: [[bender-1974-partitions-of-multisets](pages/bender-1974-partitions-of-multisets.md)] p.310 Table 3 L323-330 - "c((0,0,n)) 7.39 x 10^14 1.00 x 10^43 / v((0,0,n)) 1.41 x 10^15 1.49 x 10^43 / ~ 1.16 x 10^15 1.30 x 10^43 / c*((0,0,n)) 1.28 x 10^17 4.36 x 10^45 / v*((0,0,n)) 2.02 x 10^17 6.06 x 10^45 / ~ 1.69 x 10^17 5.35 x 10^45"; EGFs (15)-(17) reproduce the exact counts to the printed digits.
[^11]: [[bender-1974-partitions-of-multisets](pages/bender-1974-partitions-of-multisets.md)] pp.310-311 §7 [synthesis] L332-382 - (24) defines V_r*; Theorem 2 in terms of the cycle index P_{S_r}; (25) V_4*; proof via g_r(n,k), "the groups acting on A or B are S_r + S_r + ... + S_r and S_k", and "By de Bruijn's theorem [3]" (27).
[^12]: [[bender-1974-partitions-of-multisets](pages/bender-1974-partitions-of-multisets.md)] p.308 eq. (18) L259 - "b(m) = e^{-1} sum_{s>=0} prod_i C(s,i)^{m_i} / s!"; at m = (n) the product is s^n, which is Dobinski's formula.
[^13]: https://oeis.org/A002718 (read 2026-10-16) - "Number of bicoverings of an n-set"; https://oeis.org/A020554 (read 2026-10-16) - "Number of multigraphs on n labeled edges (without loops)"; https://oeis.org/A094574 (read 2026-10-16) - "Number of (<=2)-covers of an n-set"; https://oeis.org/A020555 (read 2026-10-16) - "Number of multigraphs on n labeled edges (with loops). Also number of genetically distinct states amongst n individuals." Each matches the totals of eq. (11) at index `n`.
[^14]: https://oeis.org/A060486 (read 2026-10-16) - "Tricoverings of an n-set"; https://oeis.org/A165434 (read 2026-10-16) - "Number of tri-coverings of a set"; https://oeis.org/A319591 (read 2026-10-16) - "Number of nonnegative integer matrices with n columns and any number of nonzero distinct rows with every column summing to 3 up to permutation of rows"; https://oeis.org/A322487 (read 2026-10-16) - "Number of (3*n) X n matrices with nonnegative integer entries and each column sum being 3 up to permutation of rows." Each matches the totals of eqs. (15)-(17) at index `n`.
[^15]: https://oeis.org/A000110 (read 2026-10-16) - "Bell or exponential numbers: number of ways to partition a set of n labeled elements", and the comment "(1/e)*Sum_{k>=0} (k+1)^n/k! = (1/e) Sum_{k=1..oo} k^(n+1)/k! = a(n+1), n >= 0, using the Dobinski formula" (Wolfdieter Lang, 2015).
[^16]: Verified by execution (Python 3.11, 2026-10-16): enumeration of all multiset partitions of `{a, b, c, c}` gives the 11 rows of Table 2 and the tallies `c = 0, 2, 2, 0`, `v = 0, 2, 3, 1`, `c* = 1, 5, 3, 0`, `v* = 1, 5, 4, 1`; enumeration of all multiset partitions gives the totals for every element twice (`n ≤ 5`) and three times (`n ≤ 3`), equal to the EGFs (11) and (15)-(17) and to the OEIS entries at index `n`.
