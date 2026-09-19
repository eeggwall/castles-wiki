---
title: Forcibly simple score vector
category: Concepts
summary: A score vector S is forcibly simple if every tournament realizing S is simple (Muller-Nešetřil-Pelant, 1975). There are exactly five: (0), (0, 1), (1, 1, 1), (2, 2, 2, 2, 2), and (3, 3, 3, 3, 3, 3, 3). Tetali's classification of unique tournaments filters this list to the four strong-and-unique cases, dropping (0, 1) (not strong) and (3, 3, 3, 3, 3, 3, 3) (has three non-isomorphic strong realizers, so not unique).
tags: [concept, tournament, forcibly-simple, score-vector, muller-nesetril-pelant, classification, tetali]
sources: [tetali-1998-unique-tournaments]
created: 2026-09-17
updated: 2026-09-19
---

# Forcibly simple score vector

## Definition

A score vector `S` is **forcibly simple** (FS) if every tournament realizing `S` is a [[simple-tournament](pages/simple-tournament.md)].[^1] The term is Muller-Nešetřil-Pelant's (1975), quoted here from Tetali's Definition 2.

## The classification

Muller-Nešetřil-Pelant proved:[^2]

**Theorem (Muller-Nešetřil-Pelant 1975).** A score vector `S` is forcibly simple if and only if `S ∈ {(0), (0, 1), (1, 1, 1), (2, 2, 2, 2, 2), (3, 3, 3, 3, 3, 3, 3)}`.

Five score vectors, on 1, 2, 3, 5, 7 vertices respectively. Three of them are odd regular tournaments (`(1, 1, 1)` = `R_3`, `(2, 2, 2, 2, 2)` = `R_5`, `(3, 3, 3, 3, 3, 3, 3)` = a regular score on 7 vertices with 3 non-isomorphic realizers), one is the empty tournament (`(0)`), and one is the transitive tournament on 2 vertices (`(0, 1)`).

## Role in Tetali's classification

Tetali's Theorem 1 filters this list to the strong-and-unique cases:[^3]

- `(0)`: unique, strongly connected trivially, retained → 1-vertex basic.
- `(0, 1)`: unique but **not strong** (the transitive tournament on 2 vertices has a source and a sink) → dropped.
- `(1, 1, 1)`: unique, strong → 3-vertex basic.
- `(2, 2, 2, 2, 2)`: unique, strong → 5-vertex basic.
- `(3, 3, 3, 3, 3, 3, 3)`: forcibly simple **but not unique** - Tetali notes explicitly that this score vector has three non-isomorphic strong realizers → dropped.

The `n = 4` case (`(1, 1, 2, 2)`) is *not* on the FS list because the strong tournament on 4 vertices is not simple; Tetali adds it back by direct inspection.[^4]

This is the exact chain by which Tetali reduces the classification of unique tournaments to the five-element list above.

## Why the size-7 regular tournament is not unique

The regular tournament on 7 vertices has three non-isomorphic strong realizers, all with score `(3, 3, 3, 3, 3, 3, 3)`. Tetali cites this as the "note" observation that the strong-and-unique series stops at size 5: `(3, 3, 3, 3, 3, 3, 3)` is the only remaining candidate above size 5, and it fails uniqueness.[^3]

## Cross-check against the Online Encyclopedia of Integer Sequences (OEIS): regular tournaments

Three of the five FS score vectors are regular, and the OEIS count of unlabeled regular tournaments on `2n+1` nodes is `A096368 = 1, 1, 1, 3, 15, 1223, …` for `1, 3, 5, 7, 9, 11` nodes.[^5] Read against Tetali's filter:

| nodes | regular score | `A096368` | Tetali |
|---|---|---|---|
| 3 | `(1, 1, 1)` | 1 | unique, strong → basic |
| 5 | `(2, 2, 2, 2, 2)` | 1 | unique, strong → basic |
| 7 | `(3, 3, 3, 3, 3, 3, 3)` | 3 | three realizers → not unique |

The "three non-isomorphic strong realizers" Tetali checks by hand is `A096368(3) = 3` (a regular tournament on `≥ 3` nodes is automatically strong). The same table explains why the FS list is so short relative to the ambient supply of score vectors - `A000571 = 1, 1, 2, 4, 9, 22, 59, …` score sequences on `1, 2, 3, 4, 5, 6, 7` nodes - the FS vectors are `1` of `1`, `1` of `1`, `1` of `2`, `1` of `9`, and `1` of `59`.[^5] The wiki's own brute force on [[tree-castle-by-area](pages/tree-castle-by-area.md)] re-derived the same picture through `n = 8` (zero strong unique tournaments at sizes 6 and 7, all 31 unique tournaments at `n = 8` non-strong), using the `is_strongly_connected` snippet on [[castle-snippets](pages/castle-snippets.md)].

On the castle side the five FS sizes `1, 2, 3, 5, 7` are *not* the composition parts: the parts are Tetali's basic sizes `{1, 3, 4, 5}`, with `4` the strong-but-not-simple exception added by inspection. That part set is what makes the `h = 4` tree-castle row of [[tree-castle-by-area](pages/tree-castle-by-area.md)] equal `A000570` ([[oeis-index](pages/oeis-index.md)]).

## Appearances in Sources

- [[tetali-1998-unique-tournaments](pages/tetali-1998-unique-tournaments.md)] - Definition 2 (p.158 L68-69), Theorem 3 quotation (p.158 L75-82), and the filtering argument in the proof of Theorem 1 (p.159 L94-107).

## Related Concepts

- [[simple-tournament](pages/simple-tournament.md)] - the underlying property; FS is the score-level version.
- [[unique-tournament](pages/unique-tournament.md)] - the four basic strong-and-unique tournaments come from filtering the five FS score vectors.
- [[tree-castle-by-area](pages/tree-castle-by-area.md)] - the castle side of the part set `{1, 3, 4, 5}`, and the wiki's brute-force re-verification through `n = 8`.
- [[castle-snippets](pages/castle-snippets.md)] - `is_strongly_connected(T)`, the strongly connected component (SCC) test used in that verification.
- [[oeis-index](pages/oeis-index.md)] - `A000570` catalogue entry.

## Footnotes

[^1]: [[tetali-1998-unique-tournaments](pages/tetali-1998-unique-tournaments.md)] p.158 L68-69 — "Definition 2. We call a score vector `S` forcibly simple (FS) if every tournament with the score vector `S` is simple."

[^2]: [[tetali-1998-unique-tournaments](pages/tetali-1998-unique-tournaments.md)] p.158 L75-82 — "Theorem 3 (Muller et al.). The following two statements are equivalent: (1) `S` is forcibly simple; (2) `S ∈ {(0), (0, 1), (1, 1, 1), (2, 2, 2, 2, 2), (3, 3, 3, 3, 3, 3, 3)}`."

[^3]: [[tetali-1998-unique-tournaments](pages/tetali-1998-unique-tournaments.md)] p.159 L94-103 [synthesis] — the filtering of the five FS score vectors down to the four basic strong-and-unique tournaments.

[^4]: [[tetali-1998-unique-tournaments](pages/tetali-1998-unique-tournaments.md)] p.159 L104-107 — "The only case not covered by the above is the unique strong tournament on four vertices with the score vector (1, 1, 2, 2)."

[^5]: https://oeis.org/A096368 (2026-09-19) — "Number of unlabeled regular tournaments with 2n+1 nodes" 1, 1, 1, 3, 15, 1223, 1495297, …; https://oeis.org/A000571 (2026-09-19) — "Number of different score sequences that are possible in an n-team round-robin tournament" 1, 1, 1, 2, 4, 9, 22, 59, 167, 490, … (offset 0).
