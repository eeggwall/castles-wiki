---
title: Forcibly simple score vector
category: Concepts
summary: A score vector is forcibly simple if every tournament with that score vector is simple (Tetali's Definition 2). By Theorem 3 of Muller, Nešetřil and Pelant (1975), as Tetali paraphrases it, there are exactly five, (0), (0, 1), (1, 1, 1), (2, 2, 2, 2, 2) and (3, 3, 3, 3, 3, 3, 3); an enumeration of all tournaments on at most 8 vertices finds exactly these. Tetali's classification of unique tournaments keeps three of them, dropping (0, 1), which is not strong, and (3, 3, 3, 3, 3, 3, 3), which has three non-isomorphic realizers, and adds (1, 1, 2, 2) separately.
tags: [concept, tournament, forcibly-simple, score-vector, muller-nesetril-pelant, classification, tetali]
sources: [tetali-1998-unique-tournaments]
created: 2026-09-17
updated: 2026-10-16
---

# Forcibly simple score vector

## Definition

A score vector `S` is **forcibly simple** if every tournament with score vector `S` is a [[simple-tournament](pages/simple-tournament.md)].[^1] This is Tetali's Definition 2; Tetali paraphrases the theorems of Muller, Nešetřil and Pelant "to suit our terminology".[^2]

*Example.* `(1, 1, 1)` is forcibly simple: its only realizer is the 3-cycle, which is simple. `(1, 1, 2, 2)` is not: its only realizer, the strong tournament on 4 vertices, has the uniform set `{1, 2}` of the example on [[simple-tournament](pages/simple-tournament.md)].

## The five forcibly simple score vectors

**Theorem (Muller, Nešetřil and Pelant, as Tetali's Theorem 3).** A score vector is forcibly simple exactly when it is one of[^3]

```
(0),   (0, 1),   (1, 1, 1),   (2, 2, 2, 2, 2),   (3, 3, 3, 3, 3, 3, 3).
```

They lie on 1, 2, 3, 5 and 7 vertices. `(1, 1, 1)`, `(2, 2, 2, 2, 2)` and `(3, 3, 3, 3, 3, 3, 3)` are the regular score vectors on 3, 5 and 7 vertices, `(0)` belongs to the one-vertex tournament, and `(0, 1)` to the tournament on two vertices, which is simple because it has no set `M` with `2 ≤ |M| < 2`. An enumeration of all tournaments on at most 8 vertices, testing every realizer of every score vector for simplicity, finds exactly these five for `n ≤ 8`.[^4]

## Role in Tetali's classification

For `n ≠ 4`, a strong unique tournament has a forcibly simple score vector ([[simple-tournament](pages/simple-tournament.md)], section *Role in Tetali's proof*). Tetali's Theorem 1 then keeps three of the five:[^5]

- `(0)`, `(1, 1, 1)` and `(2, 2, 2, 2, 2)` each have one realizer, which is strong: the basic tournaments on 1, 3 and 5 vertices.
- `(0, 1)` has one realizer, which is not strong: one vertex beats the other, and no edge leads back.
- `(3, 3, 3, 3, 3, 3, 3)` has three non-isomorphic realizers, all strong, so it is not unique. It is the only forcibly simple score vector on more than five vertices, so no strong tournament on six or more vertices is unique.

`(1, 1, 2, 2)` is not forcibly simple, and Tetali adds it as the fourth basic tournament, on 4 vertices, by inspection.[^6]

## Regular tournaments

A regular tournament on `n = 2r + 1` vertices, every score equal to `r`, is strong: a set `X` with no edge leading out of it has scores summing to `C(|X|, 2)`, so `|X| · r = |X|(|X| − 1)/2`, and `|X| = n`. The regular tournaments up to isomorphism number `A096368`, `1, 1, 1, 3, 15, 1223, …` on `1, 3, 5, 7, 9, 11` vertices:[^7]

| vertices | regular score vector | regular tournaments, `A096368` | in Tetali's proof |
|---|---|---|---|
| 3 | `(1, 1, 1)` | 1 | unique and strong, a basic tournament |
| 5 | `(2, 2, 2, 2, 2)` | 1 | unique and strong, a basic tournament |
| 7 | `(3, 3, 3, 3, 3, 3, 3)` | 3 | three realizers, not unique |

The three realizers that Tetali checks by hand are `A096368(3) = 3`, and the enumeration finds the same three.[^4] Among all score vectors, `A000571 = 1, 1, 2, 4, 9, 22, 59` on `1, …, 7` vertices, the forcibly simple ones are `1` of `1`, `1` of `1`, `1` of `2`, `1` of `9` and `1` of `59` at `n = 1, 2, 3, 5, 7`.

The sizes of the basic tournaments, `{1, 3, 4, 5}`, are the parts of the compositions that count the unique tournaments ([[unique-tournament](pages/unique-tournament.md)]), and of the compositions that the tree skylines of height at most 4 and area `n − 1` correspond to ([[tree-castle-by-area](pages/tree-castle-by-area.md)]); they are not the sizes `1, 2, 3, 5, 7` of the forcibly simple score vectors.

## Appearances in Sources

- [[tetali-1998-unique-tournaments](pages/tetali-1998-unique-tournaments.md)] - Definition 2, Theorem 3 of Muller et al. as Tetali paraphrases it, and the filtering of the five score vectors in the proof of Theorem 1.

## Related Concepts

- [[simple-tournament](pages/simple-tournament.md)] - simple tournaments, of which this is the score-vector version, and the strong tournament on 4 vertices that is not simple.
- [[unique-tournament](pages/unique-tournament.md)] - the four basic strong unique tournaments and the count by compositions into `{1, 3, 4, 5}`.
- [[tree-castle-by-area](pages/tree-castle-by-area.md)] - the tree skylines of height at most 4, equinumerous with the unique tournaments.
- [[castle-snippets-strips](pages/castle-snippets-strips.md)] - `is_strongly_connected(T)`, a strong-connectivity test for tournament matrices.

## Footnotes

[^1]: [[tetali-1998-unique-tournaments](pages/tetali-1998-unique-tournaments.md)] p.158 L68-69 - "Definition 2. We call a score vector S forcibly simple (FS) if every tournament with the score vector S is simple."
[^2]: [[tetali-1998-unique-tournaments](pages/tetali-1998-unique-tournaments.md)] p.158 L70-71, p.159 L132-133 - "Muller et al. [4] prove, inter alia, the following interesting theorems. We paraphrase the theorems to suit our terminology", and reference 4: "V. Muller, J. Nešetřil, and J. Pelant, Either tournaments or algebras?, Discrete Math. 11 (1975), 37-66."
[^3]: [[tetali-1998-unique-tournaments](pages/tetali-1998-unique-tournaments.md)] p.158 L75-82 - "Theorem 3. (Muller et al.). The following two statements are equivalent: (1) S is forcibly simple; (2) S ∈ {(0), (0, 1), (1, 1, 1), (2, 2, 2, 2, 2), (3, 3, 3, 3, 3, 3, 3)}."
[^4]: Verified by execution (Python 3.11, 2026-10-16): all tournaments on `n ≤ 8` vertices up to isomorphism, every class tested for simplicity over all sets `M` with `2 ≤ |M| < n`; the score vectors all of whose realizers are simple are exactly the five of Theorem 3; `(3, 3, 3, 3, 3, 3, 3)` has three realizers, all strong; the regular tournaments on 3, 5 and 7 vertices number 1, 1 and 3, all strong.
[^5]: [[tetali-1998-unique-tournaments](pages/tetali-1998-unique-tournaments.md)] p.159 L96-103 - "a score vector which corresponds to a tournament that is both strong and unique (except for n=4) must come from the list of five score vectors in statement (2) of Theorem 3. The score vector (0, 1) corresponds to a unique tournament which is not strong; it is easy to check that there are three nonisomorphic strong tournaments which have the score vector (3, 3, 3, 3, 3, 3, 3). (Note that this among other things gives us that there are no strong tournaments on six or more vertices which belong to Unique.)"
[^6]: [[tetali-1998-unique-tournaments](pages/tetali-1998-unique-tournaments.md)] p.159 L104-107 - "The only case not covered by the above is the unique strong tournament on four vertices with the score vector (1, 1, 2, 2). Thus the only strong tournaments which are in Unique are the four tournaments shown in Fig. 1."
[^7]: https://oeis.org/A096368 and https://oeis.org/A000571 (read 2026-10-16) - "Number of unlabeled regular tournaments with 2n+1 nodes" `1, 1, 1, 3, 15, 1223, 1495297, …` (offset 0); "Number of different score sequences that are possible in an n-team round-robin tournament" `1, 1, 1, 2, 4, 9, 22, 59, 167, …` (offset 0).
