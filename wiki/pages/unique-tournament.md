---
title: Unique tournament
category: Concepts
summary: A tournament (complete oriented graph) whose score vector is realized by no other tournament up to isomorphism. Enumerated by OEIS A000570. Tetali (1998) proved a complete classification: the strongly-connected unique tournaments are exactly four (sizes 1, 3, 4, 5 with score vectors (0), (1,1,1), (1,1,2,2), (2,2,2,2,2)), and every unique tournament decomposes into these via strong-component decomposition - giving A000570(n) = number of compositions of n with parts in {1, 3, 4, 5}. On the wiki, this is the graph-theoretic side of the three-way tree castle ↔ composition ↔ unique tournament bijection.
tags: [concept, tournament, unique, score-sequence, oeis, a000570, tetali, classification]
sources: [tetali-1998-unique-tournaments]
created: 2026-09-17
updated: 2026-09-17
---

# Unique tournament

## Description

A **tournament** on `n` vertices is a complete oriented graph: for every pair of distinct vertices, one directed edge is present. Its **score vector** `S(T_n) = (s_1, …, s_n)` is the sorted list of out-degrees. A tournament `T_n` is **unique** if `S(T_n) = S(T'_n)` implies `T_n ≅ T'_n` for every other tournament `T'_n` on the same vertex set. Equivalently, the score vector realized by `T_n` has no other realizer up to isomorphism.[^1]

The class `Unique = ∪_{n ≥ 1} U_n` and its size sequence `u_n = |U_n|` is exactly OEIS A000570:

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

The tree-castle transfer matrix produces the same GF as A000570, and the three-way identification is:

```
tree castle of area A (h ≤ 4)   ↔   composition of A + 1 with parts in {1, 3, 4, 5}   ↔   unique tournament on A + 1 vertices.
```

See [[tree-castle-by-area](pages/tree-castle-by-area.md)] for the tree-castle-to-composition arrow and the OEIS matches at heights 2, 3, 4, and ∞. Tetali's classification is the composition-to-tournament arrow.

Two independent castle-adjacent bijections converge on the same object: our tree-castle bijection (via [[castle-graph](pages/castle-graph.md)]'s tree constraint) and Khovanova's 2007 "initial-loss non-tracking binary string" bijection[^6] built from the four basic strings `0`, `001`, `0011`, `00101`. Both encode the composition parts as size-`k` blocks.

## Appearances in Sources

- [[tetali-1998-unique-tournaments](pages/tetali-1998-unique-tournaments.md)] - the paper introducing the classification.

## Related Concepts

- [[simple-tournament](pages/simple-tournament.md)] - Muller-Nešetřil-Pelant condition used in Tetali's proof; strictly stronger than "strongly connected."
- [[forcibly-simple-score-vector](pages/forcibly-simple-score-vector.md)] - the five FS score vectors are the starting point of the classification.
- [[tree-castle-by-area](pages/tree-castle-by-area.md)] - the three-way bijection.
- [[castle-graph](pages/castle-graph.md)] - tree castles, the polyomino side of the bijection.
- [[oeis-index](pages/oeis-index.md)] - A000570 catalog entry.
- [[hardin-word-identity](pages/hardin-word-identity.md)] - a different castle-side realization of the same composition object (via signed tower counts).

## Footnotes

[^1]: [[tetali-1998-unique-tournaments](pages/tetali-1998-unique-tournaments.md)] p.157 L11-13 — "We call a tournament unique, if there is no other tournament (barring isomorphic ones) which shares the same score vector."

[^2]: [[tetali-1998-unique-tournaments](pages/tetali-1998-unique-tournaments.md)] p.157 L39-41 — "Theorem 1. There are exactly four (basic) strong tournaments in Unique … any other (nonstrong) tournament in Unique can be decomposed into strong components, each of which is one of the four basic tournaments."

[^3]: Standard fact: in any tournament, strong components are linearly ordered (the condensation is a transitive tournament on the components). Combined with Tetali's classification of basic tournaments, `u_n` equals the number of compositions of `n` with parts drawn from `{1, 3, 4, 5}` (one composition per possible ordered sequence of strong-component sizes; each component is uniquely the basic tournament of that size). Re-derived here.

[^4]: [[tetali-1998-unique-tournaments](pages/tetali-1998-unique-tournaments.md)] p.159 L114-115 — "there exist constants c ≈ 0.48 and α ≈ 1.685 such that `lim_{n → ∞} u_n c α^n = 1`."

[^5]: [[tetali-1998-unique-tournaments](pages/tetali-1998-unique-tournaments.md)] p.159 L99-103 — "it is easy to check that there are three nonisomorphic strong tournaments which have the score vector (3, 3, 3, 3, 3, 3, 3). (Note that this among other things gives us that there are no strong tournaments on six or more vertices which belong to Unique.)"

[^6]: T. Khovanova, "Unique Tournaments and Radar Tracking," arXiv:0712.1621 [math.CO] (2007), https://arxiv.org/abs/0712.1621. Khovanova's paper is the accessible full-text quoting Tetali's classification and building a parallel binary-string bijection.
