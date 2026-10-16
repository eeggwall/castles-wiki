---
title: Unique tournament
category: Concepts
summary: A tournament (complete oriented graph) is unique if every tournament with the same score vector is isomorphic to it; u_n, the number of them on n vertices, is OEIS A000570. Tetali (1998) proved that exactly four strong tournaments are unique, on 1, 3, 4 and 5 vertices with score vectors (0), (1,1,1), (1,1,2,2), (2,2,2,2,2), and that the strong components of every unique tournament are among them. Since the score vector determines the strong components, the unique tournaments on n vertices correspond to the compositions of n into parts {1, 3, 4, 5}, and through them to the tree skylines of height at most 4 and area n − 1. Counts of all, strong, unique and strong unique tournaments are checked by enumeration for n ≤ 8.
tags: [concept, tournament, unique, score-sequence, oeis, a000570, tetali, classification]
sources: [tetali-1998-unique-tournaments]
created: 2026-09-17
updated: 2026-10-16
---

# Unique tournament

## Definition

A **tournament** on `n` vertices is a complete oriented graph: between any two distinct vertices there is exactly one directed edge, and `v` **beats** `u` when the edge is `v → u`. Its **score vector** `S(T) = (s_1, …, s_n)` lists the out-degrees in nondecreasing order. A tournament is **unique** if every tournament with the same score vector is isomorphic to it; equivalently, its score vector has one realizer up to isomorphism. A tournament is **strong** if every vertex can reach every other along directed edges.[^1]

*Example.* On 3 vertices both tournaments are unique: the transitive one, with score vector `(0, 1, 2)`, and the 3-cycle, `(1, 1, 1)`. On 5 vertices there are 12 tournaments up to isomorphism and 9 score vectors; `(1, 2, 2, 2, 3)` has three non-isomorphic realizers and `(1, 1, 2, 3, 3)` has two, so 7 of the 9 score vectors belong to a unique tournament.[^2]

The number `u_n` of unique tournaments on `n` vertices is `A000570(n)`:[^3]

```
u_n  =  1, 1, 2, 4, 7, 11, 18, 31, 53, 89, 149, 251, 424, 715, 1204, …        (n = 1, 2, 3, …)
```

## Tetali's classification

**Theorem (Tetali 1998, Theorem 1).** There are exactly four strong unique tournaments, with score vectors `(0)`, `(1, 1, 1)`, `(1, 1, 2, 2)` and `(2, 2, 2, 2, 2)` on 1, 3, 4 and 5 vertices. The strong components of every other unique tournament are among these four.[^4]

| size | score vector | tournament |
|---|---|---|
| 1 | `(0)` | one vertex |
| 3 | `(1, 1, 1)` | the 3-cycle |
| 4 | `(1, 1, 2, 2)` | the only strong tournament on 4 vertices |
| 5 | `(2, 2, 2, 2, 2)` | the only regular tournament on 5 vertices |

The proof reduces the strong case to two theorems of Muller, Nešetřil and Pelant (1975) on [[simple-tournament](pages/simple-tournament.md)]s and [[forcibly-simple-score-vector](pages/forcibly-simple-score-vector.md)]s, as Tetali paraphrases them. For `n ≠ 4` a strong unique tournament has a forcibly simple score vector, and of the five forcibly simple score vectors only `(0)`, `(1, 1, 1)` and `(2, 2, 2, 2, 2)` belong to strong unique tournaments: `(0, 1)` is not strong, and `(3, 3, 3, 3, 3, 3, 3)` has three non-isomorphic realizers. So no strong tournament on six or more vertices is unique. The size 4 is handled separately, because the strong tournament on 4 vertices is not simple ([[tetali-1998-unique-tournaments](pages/tetali-1998-unique-tournaments.md)]).[^5]

## Counting by compositions

The strong components `C_1, …, C_r` of a tournament can be numbered so that every vertex of `C_j` beats every vertex of `C_i` whenever `i < j`.

**Lemma.** The score vector of a tournament determines the sizes of its strong components, in this order, and the score vector of each component.

*Proof.* A vertex of `C_j` beats every vertex of `C_1, …, C_{j−1}`, so its score is at least `|C_1| + ⋯ + |C_{j−1}|`, while a vertex of `C_i` with `i < j` scores at most `|C_1| + ⋯ + |C_i| − 1`. So the components occupy consecutive blocks of the score vector. A set of `k` vertices has scores summing to at least `C(k, 2)`, from the edges among them, with equality exactly when no edge leads out of the set. A set with no edge leading out contains, with each of its vertices, the whole strong component of that vertex (a strong component with vertices on both sides would have an edge leading out of the set) and every earlier component (since `C_j` beats `C_i` for `i < j`), so it is `C_1 ∪ ⋯ ∪ C_i` for some `i`. So the cumulative sizes `|C_1| + ⋯ + |C_i|` are exactly the `k` with `s_1 + ⋯ + s_k = C(k, 2)`, and the scores of `C_i` within the component are its block of the score vector minus `|C_1| + ⋯ + |C_{i−1}|`. ∎

The edges between components are forced, so two tournaments with the same score vector are isomorphic exactly when their corresponding components are. A tournament is therefore unique exactly when each of its strong components is unique.

**Proposition.** `u_n` is the number of compositions of `n` into parts `{1, 3, 4, 5}`.

*Proof.* By Tetali's Theorem 1, each size in `{1, 3, 4, 5}` carries exactly one strong unique tournament, and no other size carries one. A unique tournament determines the sequence of its component sizes, a composition of `n` into parts `{1, 3, 4, 5}`, and the composition determines the tournament, since each component is the basic tournament of its size. Conversely, stacking basic tournaments of the sizes of a composition, each later one beating every earlier one, gives a tournament whose strong components are these, hence a unique tournament. ∎

So `Σ_n u_n x^n = 1/(1 − x − x³ − x⁴ − x⁵) − 1`, and `u_n = u_{n−1} + u_{n−3} + u_{n−4} + u_{n−5}` for `n ≥ 6` with `u_1, …, u_5 = 1, 1, 2, 4, 7`, the recurrence Tetali states.[^4] At `n = 5` the seven compositions are `(1, 1, 1, 1, 1)`, `(1, 1, 3)`, `(1, 3, 1)`, `(3, 1, 1)`, `(1, 4)`, `(4, 1)` and `(5)`; the first is the transitive tournament and the last the regular one. The growth constant is `α = 1.685137…`, the largest root of `x⁵ − x⁴ − x² − x − 1`, and `u_n ~ 0.47977 · α^n`.[^6]

## Relation to castles

The tree skylines of height at most 4, skylines on `{1, 2, 3, 4}` with no two neighboring columns of height at least 2, are not castles of height 4 in general; [[tree-castle-by-area](pages/tree-castle-by-area.md)] maps those of area `n − 1` one-to-one onto the compositions of `n` into parts `{1, 3, 4, 5}`. With the Proposition,

```
tree skylines of height ≤ 4 and area n − 1   ↔   compositions of n into {1, 3, 4, 5}   ↔   unique tournaments on n vertices.
```

Khovanova (2007) matches the unique tournaments with the "initial-loss non-tracking" binary strings of the radar rule "3 out of 5 with loss 2", which are exactly the concatenations of the four strings `0`, `001`, `0011`, `00101` (Lemma 5.1 of the paper), one character per vertex and one string per basic tournament; the non-tracking strings of length `k` number `u_{k+2}`.[^7]

## The counts for n ≤ 8

| `n` | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|---|---|
| tournaments up to isomorphism, A000568 | 1 | 1 | 2 | 4 | 12 | 56 | 456 | 6880 |
| score vectors, A000571 | 1 | 1 | 2 | 4 | 9 | 22 | 59 | 167 |
| strong tournaments, A051337 | 1 | 0 | 1 | 1 | 6 | 35 | 353 | 6008 |
| unique tournaments, A000570 | 1 | 1 | 2 | 4 | 7 | 11 | 18 | 31 |
| strong unique tournaments | 1 | 0 | 1 | 1 | 1 | 0 | 0 | 0 |

Every entry agrees with an enumeration of all tournaments on at most 8 vertices.[^2][^8] Every score vector on at most 4 vertices has one realizer, so `u_n` equals the number of score vectors there; the first difference is at `n = 5`, 7 of 9.

## Appearances in Sources

- [[tetali-1998-unique-tournaments](pages/tetali-1998-unique-tournaments.md)] - Theorem 1, its proof from two theorems of Muller, Nešetřil and Pelant, and the recurrence for `u_n`.

## Related Concepts

- [[simple-tournament](pages/simple-tournament.md)] - simple tournaments, the property behind Tetali's proof; the strong tournament on 4 vertices is not simple.
- [[forcibly-simple-score-vector](pages/forcibly-simple-score-vector.md)] - the five forcibly simple score vectors that the proof filters.
- [[tree-castle-by-area](pages/tree-castle-by-area.md)] - the tree skylines of height at most 4 by area, their compositions, and the Proposition matching them with the unique tournaments.
- [[block-count-constraints](pages/block-count-constraints.md)] - compositions with parts in a set `D` as the `SEQ` construction, beside the coin-change series of the `MSET` construction.
- [[exact-height-castle-by-area](pages/exact-height-castle-by-area.md)] - the growth `1.9276` of all castles of height 4 by area, beside the growth `1.6851` of A000570.
- [[a005251-bijection](pages/a005251-bijection.md)] - the tree castles of any height by area, compositions with no two neighboring parts at least 2.
- [[castle-snippets-strips](pages/castle-snippets-strips.md)] - `castle_to_composition`, `composition_to_castle` and the strong-connectivity test `is_strongly_connected`.

## Footnotes

[^1]: [[tetali-1998-unique-tournaments](pages/tetali-1998-unique-tournaments.md)] p.157 L11-12, L15-19, L38 - "We call a tournament unique, if there is no other tournament (barring isomorphic ones) which shares the same score vector", "The score vector of a tournament is simply the sequence of outdegrees of the vertices of the tournament", "A tournament is strong if it is strongly connected in the sense of a digraph."
[^2]: Verified by execution (Python 3.11, 2026-10-16): all tournaments on `n ≤ 8` vertices up to isomorphism, generated by adding one vertex at a time and reduced by a canonical form; per `n`, the classes, score vectors, strong classes, unique score vectors and strong unique classes of the table; at `n = 5`, three classes with score vector `(1, 2, 2, 2, 3)` and two with `(1, 1, 2, 3, 3)`. Khovanova, https://arxiv.org/pdf/0712.1621 (read 2026-10-16), p.3: "For tournaments with 5 people there are two score vectors, {1,2,2,2,3} and {1,1,2,3,3}, that define several non-isomorphic tournaments."
[^3]: https://oeis.org/A000570 (read 2026-10-16) - "Number of tournaments on n nodes determined by their score vectors", offset 1, data `1, 1, 2, 4, 7, 11, 18, 31, 53, 89, 149, 251, 424, 715, 1204, …`.
[^4]: [[tetali-1998-unique-tournaments](pages/tetali-1998-unique-tournaments.md)] p.157 L33-34, L39-41 - "u_1 = 1, u_2 = 1, u_3 = 2, u_4 = 4, and u_5 = 7, and for all n > 5, u_n = u_{n−1} + u_{n−3} + u_{n−4} + u_{n−5}", "Theorem 1. There are exactly four (basic) strong tournaments in Unique (see Fig. 1); any other (nonstrong) tournament in Unique can be decomposed into strong components, each of which is one of the four basic tournaments."
[^5]: [[tetali-1998-unique-tournaments](pages/tetali-1998-unique-tournaments.md)] p.158-159 L84-110 [synthesis] - the proof of Theorem 1 from Theorems 2 and 3, the exclusion of `(0, 1)` and of `(3, 3, 3, 3, 3, 3, 3)` ("three nonisomorphic strong tournaments"), "there are no strong tournaments on six or more vertices which belong to Unique", and the case `(1, 1, 2, 2)`.
[^6]: Verified by execution (Python 3.11 with SymPy, 2026-10-16): the compositions of `n` into `{1, 3, 4, 5}` equal `u_n` for `n < 60`; `x⁵ − x⁴ − x² − x − 1` is irreducible with largest root `1.6851371…`; `u_n/α^n = 0.4797670` at `n = 199`.
[^7]: T. Khovanova, "Unique Tournaments and Radar Tracking", https://arxiv.org/pdf/0712.1621 (read 2026-10-16), p.4-6 - "NTr(k) = UT(k + 2)", "Initial-loss non-tracking strings are non-tracking strings that can't have ones in the first and second place", "Lemma 5.1. Any initial-loss non-tracking binary string is a concatenation of strings of 4 basic types: 0, 001, 0011, 00101", "Thus we established a one-to-one correspondence between unique tournaments and initial-loss non-tracking binary strings."
[^8]: https://oeis.org/A000568, https://oeis.org/A000571, https://oeis.org/A051337 (read 2026-10-16) - "Number of outcomes of unlabeled n-team round-robin tournaments" `1, 1, 1, 2, 4, 12, 56, 456, 6880, …`, "Number of different score sequences that are possible in an n-team round-robin tournament" `1, 1, 1, 2, 4, 9, 22, 59, 167, …`, "Number of strongly connected tournaments on n nodes" `1, 1, 0, 1, 1, 6, 35, 353, 6008, …`, each with offset 0.
