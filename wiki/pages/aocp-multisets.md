---
title: "AOCP Multisets (Knuth TAOCP Vol. 3)"
category: Sources
summary: Notes on Knuth's permutations of a multiset (TAOCP Vol. 3 §5.1.2) - their number, the multinomial coefficient n!/(n_1! n_2! ⋯); two-line arrays and Foata's intercalation product; counts of words with prescribed numbers of adjacent pairs, as products of binomial coefficients (eqs. (20), (23)); the unique factorization of a two-line array with no fixed column into the prime cycles (ab), (ac), (bc), (abc), (acb), which gives eq. (25), reconciled with eq. (23) by a three-term binomial identity; and Exercise 13. Every formula is checked by enumeration.
tags: [knuth, taocp, multiset, multinomial, foata, cycle-factorization, two-line-array, source]
sources: [aocp-multisets]
created: 2026-09-14
updated: 2026-10-16
---

# AOCP Multisets (Knuth, *The Art of Computer Programming*, Vol. 3)

**Source:** https://charlesreid1.com/wiki/AOCP/Multisets (notes on Knuth, *The Art of Computer Programming*, Vol. 3, §5.1.2 "Permutations of a Multiset")
**Date ingested:** 2026-09-14
**Type:** article (MediaWiki notes page)

## Summary

**Counting.** A permutation of a multiset is an arrangement of its elements as a word. The multiset `{3·a, 2·b, c, 4·d}` has `10!/(3! 2! 1! 4!) = 12 600` permutations, and in general a multiset with multiplicities `n_1, n_2, …` and `n = n_1 + n_2 + ⋯` has the multinomial coefficient `C(n; n_1, n_2, …) = n!/(n_1! n_2! ⋯)` of them (eq. (3); [[aocp-multinomial-coefficients](pages/aocp-multinomial-coefficients.md)]).[^1]

**Two-line arrays.** Knuth writes a permutation of a multiset `M` as a two-line array: the top line lists `M` in nondecreasing order and the bottom line is the permutation (eq. (4)). Foata's **intercalation product** `α ⊺ β` (Foata 1969; eq. (5)) places the two-line arrays of `α` and `β` side by side and sorts the columns stably by their top letters, so columns with equal top letters keep their left-to-right order.[^2] For `α = cadab` and `β = bddad`:

```
α        a a b c d          β        a b d d d
         c a d a b                   b d d a d

side by side   a a b c d a b d d d       stably sorted   a a a b b c d d d d
               c a d a b b d d a d                       c a b d d a b d a d
```

so `cadab ⊺ bddad = cabddabdad`.[^2]

**Words with prescribed adjacent pairs.** The words over `{a, b, c}` with `A` letters `a`, `B` letters `b`, `C` letters `c`, and exactly `k` adjacent pairs `ca`, `l` pairs `cb` and `m` pairs `ba`, number (eq. (20))[^3]

```
C(A, A − k − m) · C(B, m) · C(C, k) · C(B + k, B − l) · C(C − k, l).
```

The source builds the count from the two-line array by placing the `a`s, then the `b`s, then the `c`s.

**Two-line arrays with no fixed column.** Let `N(A, B, C, m)` count the permutations of `{A·a, B·b, C·c}` whose two-line array has no column `a/a`, `b/b` or `c/c`, a column `x/y` having `x` on top and `y` below, and exactly `m` columns `a/b`. The row and column totals and `m` fix the numbers of the six remaining column types (`a/c = A − m`, `c/b = B − m`, `c/a = C − B + m`, `b/c = C − A + m`, `b/a = A + B − C − m`), and choosing their positions in each block of equal top letters gives (eq. (23))[^4]

```
N(A, B, C, m)  =  C(A, m) · C(B, C − A + m) · C(C, B − m).
```

Counting the same arrays by their cycle factorization gives a second formula. With no fixed columns, the only prime cycles on `{a, b, c}` are `(ab)`, `(ac)`, `(bc)`, `(abc)` and `(acb)`, and any two of them share a letter, so the factorization of the array into prime cycles is unique (eq. (24)). If `(abc)` occurs `k` times, the other four occur `m − k`, `C − A + m − k`, `C − B + m − k` and `A + B − C − 2m + k` times, and (eq. (25))[^5]

```
N(A, B, C, m)  =  Σ_k  (C + m − k)! / ( (m − k)! (C − A + m − k)! (C − B + m − k)! k! (A + B − C − 2m + k)! ).
```

The source reconciles the two formulas by the identity (eq. (27), Exercise 1.2.6-31 of Vol. 1)[^5]

```
Σ_j C(M − R + S, j) · C(N + R − S, N − j) · C(R + j, M + N)  =  C(R, M) · C(S, N),
```

with `M = A + B − C − m`, `N = C − B + m`, `R = B`, `S = C` and `j = C − B + m − k`. The binomial coefficients here have arbitrary integer upper index, `C(r, j) = r(r − 1)⋯(r − j + 1)/j!`.

**Exercise 13.** The permutations of `{A·a, B·b, C·c, D·d, E·e, F·f}` with no adjacent pair `ca` and no adjacent pair `db` number, by inclusion-exclusion over the two forbidden pairs,[^6]

```
Σ_t  C(D, A − t) · C(A + B + E + F, t) · C(A + B + C + E + F − t, B) · C(C + D + E + F; C, D, E, F).
```

## Castle readings

These readings are the wiki's, not the source's.

- **Cycle factorization.** The unique factorization of a two-line array into prime cycles is the multiset form of the factorization of a permutation into disjoint cycles, the permutation side of [[permutation-cycle-castle-analogy](pages/permutation-cycle-castle-analogy.md)]. The castle Foata transform ([[castle-foata-transform](pages/castle-foata-transform.md)]) follows Foata's flattening of canonical cycle forms from TAOCP Vol. 1 §1.3.3, by way of [[project-euler-502-castle-factoring](pages/project-euler-502-castle-factoring.md)].
- **Step words.** A castle's step word ([[urd-step-strings](pages/urd-step-strings.md)]) is a permutation of a multiset of letters `U`, `R` and `D`, so the step words with given letter counts number a multinomial coefficient before the castle rules restrict them ([[aocp-multinomial-coefficients](pages/aocp-multinomial-coefficients.md)]).
- **Inversions.** Summing `q^{inv}` over the permutations of a multiset gives the q-multinomial coefficient ([[aocp-multinomial-coefficients](pages/aocp-multinomial-coefficients.md)], section *Castle readings*).
- **Unordered multisets.** Flajolet's `MSET` construction ([[symbolic-method](pages/symbolic-method.md)]) builds unordered multisets of objects, with generating function `exp(Σ_{k≥1} B(z^k)/k)` for objects counted by `B(z)`. For `B(z) = Σ_{d ∈ D} z^d` this is the series `Π_{d ∈ D} 1/(1 − z^d)` of [[block-count-constraints](pages/block-count-constraints.md)]. Knuth's permutations of a multiset are words, built by `SEQ`.
- **Partitions of a multiset.** Splitting a multiset into unordered blocks is [[multiset-partitions](pages/multiset-partitions.md)], with Bender's four counting functions ([[bender-1974-partitions-of-multisets](pages/bender-1974-partitions-of-multisets.md)]).

The multinomial coefficients are tabulated in `A036038`.[^7]

## Entities & Concepts

- [[aocp-multinomial-coefficients](pages/aocp-multinomial-coefficients.md)] - the multinomial coefficient and its factorization into binomial coefficients.
- [[aocp-binomial-coefficients](pages/aocp-binomial-coefficients.md)] - binomial coefficients with arbitrary upper index.
- [[permutation-cycle-castle-analogy](pages/permutation-cycle-castle-analogy.md)] - the correspondence of permutation cycles with castle peaks.
- [[castle-foata-transform](pages/castle-foata-transform.md)] - the castle form of Foata's flattening.
- [[urd-step-strings](pages/urd-step-strings.md)] - the step words of castles.
- [[symbolic-method](pages/symbolic-method.md)], [[block-count-constraints](pages/block-count-constraints.md)] - the `MSET` construction and its product series.
- [[multiset-partitions](pages/multiset-partitions.md)] - partitions of a multiset into blocks.

## Footnotes

[^1]: [[aocp-multisets](pages/aocp-multisets.md)] §"Multiset Permutations" L7-12 - "Multiset M = {a,a,a,b,b,c,d,d,d,d} = {3a, 2b, c, 4d} ... N_perm = 10! / (3! 2! 1! 4!)", "In general the number of permutations of a multiset is the multinomial coefficient C(n; n_1, n_2, ...) = n! / (n_1! n_2! ...)"; `10!/(3! 2! 1! 4!) = 12 600` (Python 3.11, 2026-10-16).
[^2]: [[aocp-multisets](pages/aocp-multisets.md)] §"Multiset Permutations" L16-25 - "Two-line notation (5.1.2 eq (4)): top line = elements of M in non-decreasing order; bottom line = the permutation", "Intercalation product a (top) b (5.1.2 eq (5)): place the two two-line arrays side by side, then STABLE-sort the columns into non-decreasing order of the top line", "so c a d a b (top) b d d a d = c a b d d a b d a d"; the product recomputed with a stable sort (Python 3.11, 2026-10-16).
[^3]: [[aocp-multisets](pages/aocp-multisets.md)] §"Complicated Multiset Counting Example" L29-36 - "String over {a,b,c} with A a's, B b's, C c's, and exactly k adjacent pairs 'ca', l pairs 'cb', m pairs 'ba'", "Total (5.1.2 eq (20)): C(A, A-k-m) C(B, m) C(C, k) C(B+k, B-l) C(C-k, l)"; checked against enumeration of all words with `A, B, C ≤ 3` and `k, l, m ≤ 3` (4032 cases, Python 3.11, 2026-10-16).
[^4]: [[aocp-multisets](pages/aocp-multisets.md)] §"Another Multiset Example" L40-45 - "N(A,B,C,m) = # permutations whose two-line rep has NO agreeing columns (no a/a, b/b, c/c) and exactly m columns of form a/b", "a/c = A-m, c/b = B-m, c/a = C-B+m, b/c = C-A+m, b/a = A+B-C-m", "(5.1.2 eq (23)): N(A,B,C,m) = C(A,m) C(B, C-A+m) C(C, B-m)"; checked against enumeration for `A, B, C ≤ 4` and `m ≤ 4` (Python 3.11, 2026-10-16).
[^5]: [[aocp-multisets](pages/aocp-multisets.md)] §"Another Multiset Example" L47-53 - "the only prime cycles are (a b),(a c),(b c),(a b c),(a c b), and any two share a letter so the factorization is unique (eq (24))", "(eq (25)): N = sum_k (C+m-k)! / ((m-k)!(C-A+m-k)!(C-B+m-k)! k! (A+B-C-2m+k)!)", "the three-term identity (eq (27), = AOCP V1 exercise 1.2.6-31, Vandermonde-Chu type): sum_j C(M-R+S, j) C(N+R-S, N-j) C(R+j, M+N) = C(R,M) C(S,N) with M=A+B-C-m, N=C-B+m, R=B, S=C, j=C-B+m-k"; eq. (25) checked against the same enumeration, and eq. (27) for `0 ≤ M, N ≤ 4`, `0 ≤ R, S ≤ 5` with arbitrary-upper-index binomial coefficients (Python 3.11, 2026-10-16).
[^6]: [[aocp-multisets](pages/aocp-multisets.md)] §"Third Example" L57-59 - "Exercise 13 (M21), 5.1.2: number of permutations of M = {A a,...,F f} with no 'ca' and no 'db' adjacent pairs: sum_t C(D, A-t) C(A+B+E+F, t) C(A+B+C+E+F-t, B) C(C+D+E+F; C,D,E,F)"; checked against enumeration for every multiplicity at most 2 and size at most 9 (700 cases, Python 3.11, 2026-10-16).
[^7]: https://oeis.org/A036038 (read 2026-10-16) - "Triangle T(n,k) read by rows: multinomial coefficients for the partitions of n listed in Abramowitz-Stegun order".
