---
title: Unique tournament
category: Concepts
summary: A tournament (complete oriented graph) whose score vector is realized by no other tournament up to isomorphism. Enumerated by OEIS A000570. Tetali (1998) proved a complete classification: the strongly-connected unique tournaments are exactly four (sizes 1, 3, 4, 5 with score vectors (0), (1,1,1), (1,1,2,2), (2,2,2,2,2)), and every unique tournament decomposes into these via strong-component decomposition - giving A000570(n) = number of compositions of n with parts in {1, 3, 4, 5}. On the wiki, this is the graph-theoretic side of the three-way tree castle ↔ composition ↔ unique tournament bijection.
tags: [concept, tournament, unique, score-sequence, oeis, a000570, tetali, classification]
sources: [tetali-1998-unique-tournaments]
created: 2026-09-17
updated: 2026-09-19
---

# Unique tournament

## Description

A **tournament** on `n` vertices is a complete oriented graph: for every pair of distinct vertices, one directed edge is present. Its **score vector** `S(T_n) = (s_1, …, s_n)` is the sorted list of out-degrees. A tournament `T_n` is **unique** if `S(T_n) = S(T'_n)` implies `T_n ≅ T'_n` for every other tournament `T'_n` on the same vertex set. Equivalently, the score vector realized by `T_n` has no other realizer up to isomorphism.[^1]

The class `Unique = ∪_{n ≥ 1} U_n` and its size sequence `u_n = |U_n|` is exactly Online Encyclopedia of Integer Sequences (OEIS) A000570:

```
u_n = 1, 1, 2, 4, 7, 11, 18, 31, 53, 89, 149, 251, 424, 715, 1204, …
```

## Tetali's classification (1998)

The main structural result is Tetali's Theorem 1:[^2]

**Theorem (Tetali 1998).** There are exactly four *basic* strong tournaments in `Unique`, with score vectors `(0)`, `(1, 1, 1)`, `(1, 1, 2, 2)`, `(2, 2, 2, 2, 2)` on 1, 3, 4, 5 vertices respectively. Any other (non-strong) tournament in `Unique` decomposes into strong components, each of which is one of these four.

The proof reduces to two theorems of Muller-Nešetřil-Pelant (1975) about [[simple-tournament](pages/simple-tournament.md)]s and [[forcibly-simple-score-vector](pages/forcibly-simple-score-vector.md)]s; see [[tetali-1998-unique-tournaments](pages/tetali-1998-unique-tournaments.md)] for the full argument.

## Consequences

Because tournament strong-component decomposition assigns each tournament a unique ordered list of strongly-connected components (the components are linearly ordered by the "beats-across" relation), Tetali's classification implies immediately:[^3]

```
A000570(n) = u_n = #{compositions of n with parts in {1, 3, 4, 5}},
```

and hence the recurrence `u_n = u_{n-1} + u_{n-3} + u_{n-4} + u_{n-5}` for `n ≥ 6` with `u_1 = 1, u_2 = 1, u_3 = 2, u_4 = 4, u_5 = 7`.[^2] The growth constant is `α ≈ 1.685`, the dominant root of `x^5 = x^4 + x^2 + x + 1`.[^4]

## The four basic tournaments, explicitly

| size `k` | score vector | tournament |
|---|---|---|
| 1 | `(0)` | singleton (no edges) |
| 3 | `(1, 1, 1)` | the 3-cycle (regular tournament on 3) |
| 4 | `(1, 1, 2, 2)` | the unique strongly connected tournament on 4 vertices |
| 5 | `(2, 2, 2, 2, 2)` | the regular tournament on 5 (the unique regular tournament on 5) |

Sizes 3 and 5 are the odd regular tournaments (unique at those sizes); size 1 is trivially the singleton; size 4 is the one *strongly connected* tournament on 4 vertices, which is *not* simple in the Muller-Nešetřil-Pelant sense and therefore appears as an exception in Tetali's Theorem 2.

## The size-6-and-larger gap

For every `k ≥ 6`, no strongly connected tournament on `k` vertices is unique. Tetali gives the explicit exception at `k = 7`: the regular tournament score `(3, 3, 3, 3, 3, 3, 3)` is *forcibly simple* (by Muller-Nešetřil-Pelant Theorem 3) but has three non-isomorphic strong realizers, so it is not unique.[^5] For `k ≥ 6` no strong-score gives a unique tournament (Muller-Nešetřil-Pelant's Theorem 3 lists all five forcibly-simple score vectors and none has size 6 or larger).[^5]

## Relation to castles

The tree-castle transfer matrix produces the same generating function (GF) as A000570, and the three-way identification is:

```
tree castle of area A (h ≤ 4)   ↔   composition of A + 1 with parts in {1, 3, 4, 5}   ↔   unique tournament on A + 1 vertices.
```

See [[tree-castle-by-area](pages/tree-castle-by-area.md)] for the tree-castle-to-composition arrow and the OEIS matches at heights 2, 3, 4, and ∞. Tetali's classification is the composition-to-tournament arrow.

Two independent castle-adjacent bijections converge on the same object: our tree-castle bijection (via [[castle-graph](pages/castle-graph.md)]'s tree constraint) and Khovanova's 2007 "initial-loss non-tracking binary string" bijection[^6] built from the four basic strings `0`, `001`, `0011`, `00101`. Both encode the composition parts as size-`k` blocks.

## The ambient counts

Four OEIS sequences frame `u_n` from the outside; the first three were read from oeis.org on 2026-09-19.[^7]

| `n` | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|---|---|
| all tournaments up to isomorphism, A000568 | 1 | 1 | 2 | 4 | 12 | 56 | 456 | 6880 |
| score sequences, A000571 | 1 | 1 | 2 | 4 | 9 | 22 | 59 | 167 |
| strongly connected tournaments, A051337 | 1 | 0 | 1 | 1 | 6 | 35 | 353 | 6008 |
| unique tournaments, A000570 | 1 | 1 | 2 | 4 | 7 | 11 | 18 | 31 |

- `u_n ≤ A000571(n)`, with equality through `n = 4`: every score sequence on at most four vertices has one realizer. The first gap is at `n = 5` (`7` of `9`).
- The strong-and-unique tournaments are `1` of `1`, `1` of `1`, `1` of `1`, `1` of `6` at `n = 1, 3, 4, 5`, then `0` of `35` and `0` of `353` at `n = 6, 7` - the rows [[tree-castle-by-area](pages/tree-castle-by-area.md)] exhausted by brute force - and the `6880` at `n = 8` is the isomorphism-class count that page's 35-minute Java run enumerated (`31` unique, all non-strong).
- The regular-tournament count A096368 (`1, 1, 3` at `3, 5, 7` nodes) is the OEIS face of the FS filter on [[forcibly-simple-score-vector](pages/forcibly-simple-score-vector.md)].

## Neighbours on the castle side

- **The composition is the ordered coin problem.** `1/(1 − x − x³ − x⁴ − x⁵)` is the `SEQ` version of the coin-change series over `{1, 3, 4, 5}`; [[block-count-constraints](pages/block-count-constraints.md)] draws the `SEQ` / `MSET` distinction (compositions versus numerical semigroups) that this identity sits on.
- **Same family, other rows.** [[bounded-height-castles-nacci](pages/bounded-height-castles-nacci.md)] tables `A000570` beside tetranacci `A000078` at `h = 4` - tree castles against all castles of that height by area - and [[a005251-bijection](pages/a005251-bijection.md)] is the `h → ∞` row of the tree-castle family encoded as binary strings, the same "composition as a binary string" trick Khovanova's basic strings `0, 001, 0011, 00101` use here. The growth constant `α ≈ 1.685` sits between the `h = 3` row's `φ ≈ 1.618` and the `h → ∞` row's `ψ² ≈ 1.755`.
- **Code.** `castle_to_composition` / `composition_to_castle` and `is_strongly_connected` on [[castle-snippets-strips](pages/castle-snippets-strips.md)] are the two arrows of the bijection in executable form.

## Appearances in Sources

- [[tetali-1998-unique-tournaments](pages/tetali-1998-unique-tournaments.md)] - the paper introducing the classification.

## Related Concepts

- [[simple-tournament](pages/simple-tournament.md)] - Muller-Nešetřil-Pelant condition used in Tetali's proof; strictly stronger than "strongly connected."
- [[forcibly-simple-score-vector](pages/forcibly-simple-score-vector.md)] - the five FS score vectors are the starting point of the classification.
- [[tree-castle-by-area](pages/tree-castle-by-area.md)] - the three-way bijection.
- [[castle-graph](pages/castle-graph.md)] - tree castles, the polyomino side of the bijection.
- [[oeis-index](pages/oeis-index.md)] - A000570 directory entry.
- [[hardin-word-identity](pages/hardin-word-identity.md)] - a different castle-side realization of the same composition object (via signed tower counts).
- [[forcibly-simple-score-vector](pages/forcibly-simple-score-vector.md)] / [[simple-tournament](pages/simple-tournament.md)] - the Muller-Nešetřil-Pelant machinery, with the regular- and strong-tournament OEIS counts that confirm each filtering step.
- [[block-count-constraints](pages/block-count-constraints.md)] - compositions with parts in `D` as the `SEQ` sibling of the coin-change series.
- [[bounded-height-castles-nacci](pages/bounded-height-castles-nacci.md)] / [[a005251-bijection](pages/a005251-bijection.md)] - the neighbouring rows of the tree-castle-by-area family.
- [[castle-snippets](pages/castle-snippets.md)] - the bijection and the strongly connected component (SCC) test as code.

## Footnotes

[^1]: [[tetali-1998-unique-tournaments](pages/tetali-1998-unique-tournaments.md)] p.157 L11-13 — "We call a tournament unique, if there is no other tournament (barring isomorphic ones) which shares the same score vector."

[^2]: [[tetali-1998-unique-tournaments](pages/tetali-1998-unique-tournaments.md)] p.157 L39-41 — "Theorem 1. There are exactly four (basic) strong tournaments in Unique … any other (nonstrong) tournament in Unique can be decomposed into strong components, each of which is one of the four basic tournaments."

[^3]: Standard fact: in any tournament, strong components are linearly ordered (the condensation is a transitive tournament on the components). Combined with Tetali's classification of basic tournaments, `u_n` equals the number of compositions of `n` with parts drawn from `{1, 3, 4, 5}` (one composition per possible ordered sequence of strong-component sizes; each component is uniquely the basic tournament of that size). Re-derived here.

[^4]: [[tetali-1998-unique-tournaments](pages/tetali-1998-unique-tournaments.md)] p.159 L114-115 — "there exist constants c ≈ 0.48 and α ≈ 1.685 such that `lim_{n → ∞} u_n c α^n = 1`."

[^5]: [[tetali-1998-unique-tournaments](pages/tetali-1998-unique-tournaments.md)] p.159 L99-103 — "it is easy to check that there are three nonisomorphic strong tournaments which have the score vector (3, 3, 3, 3, 3, 3, 3). (Note that this among other things gives us that there are no strong tournaments on six or more vertices which belong to Unique.)"

[^6]: T. Khovanova, "Unique Tournaments and Radar Tracking," arXiv:0712.1621 [math.CO] (2007), https://arxiv.org/abs/0712.1621. Khovanova's paper is the accessible full-text quoting Tetali's classification and building a parallel binary-string bijection.

[^7]: https://oeis.org/A000568 (2026-09-19) — "Number of outcomes of unlabeled n-team round-robin tournaments" 1, 1, 1, 2, 4, 12, 56, 456, 6880, 191536, … (offset 0); https://oeis.org/A000571 (2026-09-19) — "Number of different score sequences that are possible in an n-team round-robin tournament" 1, 1, 1, 2, 4, 9, 22, 59, 167, 490, … (offset 0); https://oeis.org/A051337 (2026-09-19) — "Number of strongly connected tournaments on n nodes" 1, 1, 0, 1, 1, 6, 35, 353, 6008, 178133, … (offset 0); https://oeis.org/A096368 (2026-09-19) — "Number of unlabeled regular tournaments with 2n+1 nodes" 1, 1, 1, 3, 15, 1223, …
