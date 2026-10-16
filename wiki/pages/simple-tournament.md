---
title: Simple tournament
category: Concepts
summary: A tournament is simple if for every set M of at least two and fewer than all of its vertices, some vertex outside M beats a vertex of M and is beaten by a vertex of M. Tetali takes the notion from Muller, Nešetřil and Pelant (1975). A simple tournament on at least three vertices is strong, but the only strong tournament on 4 vertices is not simple; for n ≠ 4, Tetali quotes, every strong score vector has a simple realizer. The simple tournaments up to isomorphism number 1, 1, 1, 0, 3, 15, 197, 4008 for n = 1, …, 8 (OEIS A280772, checked by enumeration). The notion is the main tool in Tetali's classification of unique tournaments.
tags: [concept, tournament, simple, strong, muller-nesetril-pelant, definition]
sources: [tetali-1998-unique-tournaments]
created: 2026-09-17
updated: 2026-10-16
---

# Simple tournament

## Definition

A tournament `T_n` on the vertex set `V` is **simple** if for every proper subset `M` of `V` there is a vertex `z ∉ M` that beats at least one vertex of `M` and is beaten by at least one vertex of `M`.[^1] Taken literally the condition fails for every one-vertex set `M`, so it is read for `2 ≤ |M| < n`. Call `M` **uniform** if every vertex outside `M` either beats all of `M` or loses to all of `M`; a tournament is simple exactly when it has no uniform set `M` with `2 ≤ |M| < n`.

Tetali takes the definition from Muller, Nešetřil and Pelant (1975), the reference the note gives "for information on simple tournaments".[^2]

*Example.* The 3-cycle is simple: for each two-vertex set `M`, the third vertex beats one vertex of `M` and loses to the other. The tournament on `{0, 1, 2, 3}` with the edges `0 → 3`, `3 → 2`, `2 → 1`, `1 → 0`, `2 → 0`, `3 → 1` is strong, since `0 → 3 → 2 → 1 → 0` is a cycle through all four vertices, and has score vector `(1, 1, 2, 2)`. It is not simple: `M = {1, 2}` is uniform, since `0` loses to both and `3` beats both.[^3]

## Simple versus strong

Tetali calls a simple tournament "clearly strong".[^4] This holds on at least three vertices: a tournament on `n ≥ 3` vertices that is not strong splits its vertex set into nonempty parts `X` and `Y` with every vertex of `X` beating every vertex of `Y`, and whichever part has at least two vertices is uniform. On two vertices the transitive tournament is simple, since it has no set `M` with `2 ≤ |M| < 2`, and it is not strong; this is why `(0, 1)` is a forcibly simple score vector ([[forcibly-simple-score-vector](pages/forcibly-simple-score-vector.md)]).

The converse fails at `n = 4`: the only strong tournament on 4 vertices, the one in the example, is not simple.[^4] For every other `n`, Tetali quotes Muller et al.'s Theorem 2: every score vector of a strong tournament on `n ≠ 4` vertices is also the score vector of a simple tournament.[^5] With the first paragraph, for `n ≥ 3`, `n ≠ 4`, a score vector belongs to a strong tournament exactly when it belongs to a simple one.

## Counts

| `n` | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|---|---|
| simple tournaments up to isomorphism, A280772 | 1 | 1 | 1 | 0 | 3 | 15 | 197 | 4008 |
| strong tournaments, A051337 | 1 | 0 | 1 | 1 | 6 | 35 | 353 | 6008 |

Every entry agrees with an enumeration of all tournaments on at most 8 vertices, which also confirms Theorem 2 for `n ≤ 8`, `n ≠ 4`.[^6] OEIS A280772, "Number of simple tournaments with n nodes", gives these eight terms and cites Table 1 of Muller, Nešetřil and Pelant.[^7]

## Role in Tetali's proof

Tetali's classification of [[unique-tournament](pages/unique-tournament.md)]s uses simple tournaments in three steps:[^8]

1. A strong unique tournament `T_n` with `n ≠ 4` is simple: by Theorem 2 its score vector has a simple realizer, and `T_n` is the only realizer.
2. So its score vector is forcibly simple, every realizer being `T_n`.
3. Theorem 3 of Muller et al., as Tetali quotes it, lists the five forcibly simple score vectors, on 1, 2, 3, 5 and 7 vertices; Tetali keeps those of strong unique tournaments and adds the size 4 separately.

Step 1 is unavailable at `n = 4`, since the strong tournament on 4 vertices is not simple.

## Appearances in Sources

- [[tetali-1998-unique-tournaments](pages/tetali-1998-unique-tournaments.md)] - Definition 1, the remark that a simple tournament is strong and the strong tournament on 4 vertices is not simple, and Theorems 2 and 3 of Muller et al. as Tetali paraphrases them.

## Related Concepts

- [[unique-tournament](pages/unique-tournament.md)] - the tournaments determined by their score vectors, classified with simple tournaments.
- [[forcibly-simple-score-vector](pages/forcibly-simple-score-vector.md)] - the score vectors all of whose realizers are simple.
- [[tree-castle-by-area](pages/tree-castle-by-area.md)] - the tree skylines of height at most 4, equinumerous with the unique tournaments, and the enumeration of tournaments on at most 8 vertices.
- [[castle-snippets-strips](pages/castle-snippets-strips.md)] - `is_strongly_connected(T)`, a strong-connectivity test for tournament matrices.

## Footnotes

[^1]: [[tetali-1998-unique-tournaments](pages/tetali-1998-unique-tournaments.md)] p.158 L63-65 - "Definition 1. T_n is simple if, for any proper subset M of V(T_n), there exists a z ∈ V(T_n) ∖ M such that z beats at least one vertex in M and z is beaten by at least one vertex in M."
[^2]: [[tetali-1998-unique-tournaments](pages/tetali-1998-unique-tournaments.md)] p.158 L59-60, p.159 L132-133 - "We begin with the definition of a simple tournament (see [4] for information on simple tournaments)", and reference 4: "V. Muller, J. Nešetřil, and J. Pelant, Either tournaments or algebras?, Discrete Math. 11 (1975), 37-66."
[^3]: Verified by execution (Python 3.11, 2026-10-16): the tournament of the example is the only strong tournament on 4 vertices up to isomorphism, and `{1, 2}` is its only uniform set of size 2 or 3.
[^4]: [[tetali-1998-unique-tournaments](pages/tetali-1998-unique-tournaments.md)] p.158 L66-67 - "A simple tournament is clearly strong, but the converse is not necessarily true - the strong tournament on four vertices, for example, is not simple."
[^5]: [[tetali-1998-unique-tournaments](pages/tetali-1998-unique-tournaments.md)] p.158 L70-74 - "Muller et al. [4] prove, inter alia, the following interesting theorems. We paraphrase the theorems to suit our terminology. Theorem 2 (Muller et al.). For each score vector S_n which corresponds to a strong tournament on n ≠ 4 vertices, there is a simple tournament which has the same score vector."
[^6]: Verified by execution (Python 3.11, 2026-10-16): all tournaments on `n ≤ 8` vertices up to isomorphism, each tested for simplicity over all sets `M` with `2 ≤ |M| < n` and for strong connectivity; every simple class with `n ≥ 3` is strong, and every strong score vector with `n ≠ 4` has a simple realizer.
[^7]: https://oeis.org/A280772 (read 2026-10-16) - "Number of simple tournaments with n nodes", offset 1, data `1, 1, 1, 0, 3, 15, 197, 4008`, a link to Müller, Nešetřil and Pelant, "Either tournaments or algebras?", Discrete Math. 11 (1975), "See table 1 on page 65". https://oeis.org/A051337 (read 2026-10-16) - "Number of strongly connected tournaments on n nodes", offset 0, `1, 1, 0, 1, 1, 6, 35, 353, 6008, …`.
[^8]: [[tetali-1998-unique-tournaments](pages/tetali-1998-unique-tournaments.md)] p.158-159 L84-110 [synthesis] - the proof of Theorem 1 from Theorems 2 and 3.
