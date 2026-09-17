---
title: Forcibly simple score vector
category: Concepts
summary: A score vector S is forcibly simple if every tournament realizing S is simple (Muller-Nešetřil-Pelant, 1975). There are exactly five: (0), (0, 1), (1, 1, 1), (2, 2, 2, 2, 2), and (3, 3, 3, 3, 3, 3, 3). Tetali's classification of unique tournaments filters this list to the four strong-and-unique cases, dropping (0, 1) (not strong) and (3, 3, 3, 3, 3, 3, 3) (has three non-isomorphic strong realizers, so not unique).
tags: [concept, tournament, forcibly-simple, score-vector, muller-nesetril-pelant, classification, tetali]
sources: [tetali-1998-unique-tournaments]
created: 2026-09-17
updated: 2026-09-17
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

## Appearances in Sources

- [[tetali-1998-unique-tournaments](pages/tetali-1998-unique-tournaments.md)] - Definition 2 (p.158 L68-69), Theorem 3 quotation (p.158 L75-82), and the filtering argument in the proof of Theorem 1 (p.159 L94-107).

## Related Concepts

- [[simple-tournament](pages/simple-tournament.md)] - the underlying property; FS is the score-level version.
- [[unique-tournament](pages/unique-tournament.md)] - the four basic strong-and-unique tournaments come from filtering the five FS score vectors.

## Footnotes

[^1]: [[tetali-1998-unique-tournaments](pages/tetali-1998-unique-tournaments.md)] p.158 L68-69 — "Definition 2. We call a score vector `S` forcibly simple (FS) if every tournament with the score vector `S` is simple."

[^2]: [[tetali-1998-unique-tournaments](pages/tetali-1998-unique-tournaments.md)] p.158 L75-82 — "Theorem 3 (Muller et al.). The following two statements are equivalent: (1) `S` is forcibly simple; (2) `S ∈ {(0), (0, 1), (1, 1, 1), (2, 2, 2, 2, 2), (3, 3, 3, 3, 3, 3, 3)}`."

[^3]: [[tetali-1998-unique-tournaments](pages/tetali-1998-unique-tournaments.md)] p.159 L94-103 [synthesis] — the filtering of the five FS score vectors down to the four basic strong-and-unique tournaments.

[^4]: [[tetali-1998-unique-tournaments](pages/tetali-1998-unique-tournaments.md)] p.159 L104-107 — "The only case not covered by the above is the unique strong tournament on four vertices with the score vector (1, 1, 2, 2)."
