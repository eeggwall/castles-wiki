---
title: Simple tournament
category: Concepts
summary: A tournament T_n is simple if, for every proper vertex subset M, some outside vertex both beats and is beaten by vertices in M. Introduced by Muller-Nešetřil-Pelant (1975). Simple ⇒ strongly connected, but the converse fails: the unique strongly connected tournament on 4 vertices is not simple. Used in the proof of Tetali's classification of unique tournaments.
tags: [concept, tournament, simple, strong, muller-nesetril-pelant, definition]
sources: [tetali-1998-unique-tournaments]
created: 2026-09-17
updated: 2026-09-19
---

# Simple tournament

## Definition

A tournament `T_n = (V, A)` is **simple** if for every proper subset `M ⊂ V` there exists a vertex `z ∈ V ∖ M` such that `z` both beats at least one vertex in `M` and is beaten by at least one vertex in `M`.[^1]

Equivalently: no proper vertex subset `M` is "seen uniformly" from the outside - no outside vertex beats all of `M` or loses to all of `M` alone; every outside vertex has a mixed relation to `M`.

## Simple versus strongly connected

Every simple tournament is strongly connected: if some `M` were a "sink" (every outside vertex loses to all of `M`) or "source" (every outside vertex beats all of `M`), the tournament would not be strongly connected, and simplicity would already fail on that `M`. So simple ⇒ strong.[^2]

**The converse fails at `n = 4`.** The unique strongly connected tournament on 4 vertices (score `(1, 1, 2, 2)`) is strong but *not* simple. This is the exception noted by Tetali in the discussion after Definition 1.[^2] For `n ≠ 4`, Muller-Nešetřil-Pelant's Theorem 2 says every strong score vector has a simple realizer, making "simple" and "strong" interchangeable at the level of score sequences.[^3]

## The counts behind the exception

The Online Encyclopedia of Integer Sequences (OEIS) count of strongly connected tournaments on `n` nodes is `A051337 = 1, 0, 1, 1, 6, 35, 353, 6008, …` for `n = 1, 2, 3, …`.[^5] The `n = 4` entry is the `1` in "the unique strongly connected tournament on 4 vertices" - and it is the one strong tournament on the whole list that fails to be simple. At `n = 5` there are `6` strong tournaments, of which only the regular one is unique; at `n = 6` and `n = 7` the `35` and `353` strong tournaments are exactly the rows [[tree-castle-by-area](pages/tree-castle-by-area.md)] exhausted by brute force (using the `is_strongly_connected` test on [[castle-snippets-strips](pages/castle-snippets-strips.md)]) to confirm that no strong tournament of size `≥ 6` is unique. The ambient count of all tournaments up to isomorphism is `A000568 = 1, 1, 2, 4, 12, 56, 456, 6880, …`.[^5]

Tournaments are the wiki's second graph-theoretic object. The first is the [[castle-graph](pages/castle-graph.md)] - bipartite, planar, a subgraph of `Z²`, always connected because of the full base row - and the two sit at opposite corners of graph theory (complete oriented graphs versus sparse undirected grids). They meet in one number: the `h = 4` tree-castle count by area is `A000570`, the unique tournaments ([[unique-tournament](pages/unique-tournament.md)]).

## Role in Tetali's proof

Tetali's classification of [[unique-tournament](pages/unique-tournament.md)]s uses simple tournaments as follows:[^4]

1. For a strong tournament `T_n` in `Unique` with `n ≠ 4`, Muller-Nešetřil-Pelant Theorem 2 says the score of `T_n` has a simple realizer. Since `T_n` is unique, `T_n` itself must be that simple realizer.
2. So the score of `T_n` is [[forcibly-simple-score-vector](pages/forcibly-simple-score-vector.md)] - every realizer is simple, because in fact there is only one realizer and it is simple.
3. Muller-Nešetřil-Pelant Theorem 3 lists all forcibly simple score vectors: exactly five, on 1, 2, 3, 5, 7 vertices.
4. Filter the five to those with strong-and-unique realizers, and add the size-4 case by inspection.

The size-4 exception is unavoidable at Step 1 - Muller-Nešetřil-Pelant Theorem 2 fails at `n = 4` precisely because the unique strong tournament on 4 vertices is not simple.

## Appearances in Sources

- [[tetali-1998-unique-tournaments](pages/tetali-1998-unique-tournaments.md)] - Definition 1 and the accompanying strong-vs-simple discussion (p.158 L60-67); Theorems 2 and 3 attributed to Muller-Nešetřil-Pelant 1975; used in the proof of Theorem 1.

## Related Concepts

- [[unique-tournament](pages/unique-tournament.md)] - the class classified via simple/forcibly-simple.
- [[forcibly-simple-score-vector](pages/forcibly-simple-score-vector.md)] - the score-level version of simplicity.
- [[tree-castle-by-area](pages/tree-castle-by-area.md)] - the castle side of `A000570`, and the brute-force sweep over the `35` and `353` strong tournaments of sizes 6 and 7.
- [[castle-snippets](pages/castle-snippets.md)] - `is_strongly_connected(T)`, the strongly connected component (SCC) test for tournament matrices.
- [[castle-graph](pages/castle-graph.md)] - the wiki's other graph-theoretic object; bipartite planar grids where tournaments are complete oriented graphs.

## Footnotes

[^1]: [[tetali-1998-unique-tournaments](pages/tetali-1998-unique-tournaments.md)] p.158 L63-65 — "Definition 1. `T_n` is simple if, for any proper subset `M` of `V(T_n)`, there exists a `z ∈ V(T_n) ∖ M` such that `z` beats at least one vertex in `M` and `z` is beaten by at least one vertex in `M`."

[^2]: [[tetali-1998-unique-tournaments](pages/tetali-1998-unique-tournaments.md)] p.158 L66-67 — "A simple tournament is clearly strong, but the converse is not necessarily true - the strong tournament on four vertices, for example, is not simple."

[^3]: [[tetali-1998-unique-tournaments](pages/tetali-1998-unique-tournaments.md)] p.158 L72-74 — "Theorem 2 (Muller et al.). For each score vector `S_n` which corresponds to a strong tournament on `n ≠ 4` vertices, there is a simple tournament which has the same score vector."

[^4]: [[tetali-1998-unique-tournaments](pages/tetali-1998-unique-tournaments.md)] p.158-159 L84-110 [synthesis] — the proof of Theorem 1 uses simple tournaments in the manner summarized here.

[^5]: https://oeis.org/A051337 (2026-09-19) — "Number of strongly connected tournaments on n nodes" 1, 1, 0, 1, 1, 6, 35, 353, 6008, 178133, … (offset 0); https://oeis.org/A000568 (2026-09-19) — "Number of outcomes of unlabeled n-team round-robin tournaments" 1, 1, 1, 2, 4, 12, 56, 456, 6880, 191536, … (offset 0).
