---
title: "A Characterization of Unique Tournaments (Tetali, 1998)"
category: Sources
summary: Tetali's three-page note proves that exactly four strong tournaments are determined by their score vectors, with score vectors (0), (1, 1, 1), (1, 1, 2, 2) and (2, 2, 2, 2, 2) on 1, 3, 4 and 5 vertices, and that the strong components of every other such tournament are among these four. The proof combines two theorems of Muller, Nešetřil and Pelant (1975) on simple tournaments, as Tetali paraphrases them. The number u_n of such tournaments on n vertices, OEIS A000570, satisfies u_n = u_{n−1} + u_{n−3} + u_{n−4} + u_{n−5} for n ≥ 6 and grows like c·α^n with α ≈ 1.685.
tags: [source, tournament, unique, score-sequence, jctb, tetali, muller-nesetril-pelant, simple-tournament, oeis, a000570, paper]
sources: [tetali-1998-unique-tournaments]
created: 2026-09-17
updated: 2026-10-16
---

# A Characterization of Unique Tournaments (Tetali, 1998)

**Source:** raw/tetali-1998-unique-tournaments.pdf, with the text extraction `raw/tetali-1998-unique-tournaments.txt`
**Publication:** Prasad Tetali, "A Characterization of Unique Tournaments," Journal of Combinatorial Theory Series B 72 (1998), 157-159. DOI: `10.1006/jctb.1997.1799`. Received September 20, 1995.[^1]
**Date ingested:** 2026-09-17
**Type:** paper (three-page note)

## Summary

A **tournament** is a complete oriented graph, and its **score vector** `S(T_n) = (s_1, …, s_n)` lists the out-degrees in nondecreasing order. Tetali calls a tournament **unique** when no tournament that is not isomorphic to it has the same score vector, and writes `U_n` for the unique tournaments on `n` vertices, `Unique = ∪_n U_n`, and `u_n` for the number of them up to isomorphism, which is the number of score vectors with one realizer.[^2] The note's examples are `(1, 1, 1)`, `(0, 1, 2, 3)`, `(2, 2, 2, 2, 2)`, and every transitive tournament, with score vector `(0, 1, …, n − 1)`.[^3] A tournament is **strong** if it is strongly connected.

**Theorem 1 (Tetali).** There are exactly four strong tournaments in `Unique`; every other tournament in `Unique` decomposes into strong components, each of which is one of the four.[^4]

The four, drawn in the note's Figure 1, have the score vectors `(0)`, `(1, 1, 1)`, `(1, 1, 2, 2)` and `(2, 2, 2, 2, 2)`, on 1, 3, 4 and 5 vertices; the proof names each of them.[^5] Tetali deduces that `u_1, …, u_5 = 1, 1, 2, 4, 7` and that for `n ≥ 6`[^6]

```
u_n  =  u_{n−1} + u_{n−3} + u_{n−4} + u_{n−5}.
```

The step from Theorem 1 to this count is not written out in the note, which calls it "a basic exercise in recurrence relations"; [[unique-tournament](pages/unique-tournament.md)] gives it.

## The proof

The proof uses two results of Muller, Nešetřil and Pelant, reference [4] of the note, which Tetali paraphrases "to suit our terminology".[^7] A tournament `T_n` is **simple** if for every proper subset `M` of its vertices some vertex outside `M` beats at least one vertex of `M` and is beaten by at least one; a score vector is **forcibly simple** if every tournament with that score vector is simple ([[simple-tournament](pages/simple-tournament.md)], [[forcibly-simple-score-vector](pages/forcibly-simple-score-vector.md)]). Tetali notes that a simple tournament is strong and that the strong tournament on four vertices is not simple.[^8]

- **Theorem 2 (Muller et al.).** Every score vector of a strong tournament on `n ≠ 4` vertices is also the score vector of a simple tournament.[^9]
- **Theorem 3 (Muller et al.).** A score vector is forcibly simple exactly when it is one of `(0)`, `(0, 1)`, `(1, 1, 1)`, `(2, 2, 2, 2, 2)`, `(3, 3, 3, 3, 3, 3, 3)`.[^9]

Proof of Theorem 1, in Tetali's steps:[^10]

1. A strong unique tournament on `n ≠ 4` vertices is simple by Theorem 2, since it is the only tournament with its score vector; so its score vector is forcibly simple.
2. By Theorem 3 its score vector is one of the five. `(0, 1)` belongs to a unique tournament that is not strong, and `(3, 3, 3, 3, 3, 3, 3)` has three non-isomorphic strong realizers, so it is not unique. This leaves `(0)`, `(1, 1, 1)` and `(2, 2, 2, 2, 2)`, and shows that no strong tournament on six or more vertices is unique.
3. The case `n = 4` is the unique strong tournament on four vertices, with score vector `(1, 1, 2, 2)`.
4. The strong components of a nonstrong unique tournament are themselves unique, so they are among the four.

## The recurrence and the growth

The note's Remark states the recurrence for `n ≥ 6` and constants `c ≈ 0.48` and `α ≈ 1.685` with `u_n ~ c·α^n`.[^11] The text extraction of that line (L114-115) drops the fraction bar; `u_n/(c·α^n) → 1` is the limit that holds, with `c = 0.47977` and `α = 1.685137`, the largest root of `x⁵ − x⁴ − x² − x − 1`, which is irreducible over the rationals.[^12] So `α` has degree 5 and is not a metallic mean, each of which has degree at most 2 ([[metallic-means](pages/metallic-means.md)]).

The note compares its count with Garey's: the tournaments on `n ≥ 4` vertices with exactly one Hamiltonian cycle number the Fibonacci number `F_{2n−6}`.[^13]

OEIS A000570, "Number of tournaments on n nodes determined by their score vectors", is this sequence (offset 1: `1, 1, 2, 4, 7, 11, 18, 31, …`); it lists the recurrence (Jon E. Schoenfield, 2006), the generating function `(1 + x² + x³ + x⁴)/(1 − x − x³ − x⁴ − x⁵)` (Harvey P. Dale, 2011) and Tetali's paper, and names Tetali as its author.[^14]

An enumeration of all tournaments on at most 8 vertices reproduces `u_1, …, u_8 = 1, 1, 2, 4, 7, 11, 18, 31`, the four strong unique tournaments and no others, the five forcibly simple score vectors as the only ones for `n ≤ 8`, Theorem 2 for `n ≤ 8`, `n ≠ 4`, the failure of simplicity at `n = 4`, and the three strong realizers of `(3, 3, 3, 3, 3, 3, 3)`.[^15]

## Key Takeaways

- **Four strong unique tournaments,** on 1, 3, 4 and 5 vertices, and every unique tournament is a sequence of them (Theorem 1).
- **Proof by forcibly simple score vectors:** for `n ≠ 4`, a strong unique tournament has a forcibly simple score vector, and there are five such vectors; the size 4 is handled separately because the strong tournament on four vertices is not simple.
- **The count:** `u_n = u_{n−1} + u_{n−3} + u_{n−4} + u_{n−5}` for `n ≥ 6`, `u_n ~ 0.48 · 1.685^n`, OEIS A000570.
- **References in the note:** Douglas 1970 and Garey 1972 on tournaments with one Hamiltonian circuit, Moon 1968 (*Topics on Tournaments*), Muller, Nešetřil and Pelant 1975 ("Either tournaments or algebras?"), and Reid and Beineke 1978.[^16]

## Entities & Concepts

- [[unique-tournament](pages/unique-tournament.md)] - unique tournaments, the proof that `u_n` counts the compositions of `n` into parts `{1, 3, 4, 5}`, and the counts of all, strong and unique tournaments for `n ≤ 8`.
- [[simple-tournament](pages/simple-tournament.md)] - Definition 1 of the note, with the four-vertex example that is strong and not simple.
- [[forcibly-simple-score-vector](pages/forcibly-simple-score-vector.md)] - Definition 2 and Theorem 3, the five forcibly simple score vectors, checked for `n ≤ 8`.
- [[tree-castle-by-area](pages/tree-castle-by-area.md)] - the tree skylines of height at most 4 and area `n − 1`, equinumerous with the unique tournaments on `n` vertices through the compositions of `n` into `{1, 3, 4, 5}`.

## Relation to Other Wiki Pages

Theorem 1 is the tournament side of the Proposition on [[tree-castle-by-area](pages/tree-castle-by-area.md)], which matches the unique tournaments on `n` vertices, the compositions of `n` into parts `{1, 3, 4, 5}` and the tree skylines of height at most 4 and area `n − 1`. Khovanova (2007) matches the unique tournaments with binary strings built from the four strings `0`, `001`, `0011`, `00101`, one character per vertex ([[unique-tournament](pages/unique-tournament.md)]).

## Footnotes

[^1]: [[tetali-1998-unique-tournaments](pages/tetali-1998-unique-tournaments.md)] p.157 L1-10 - "Journal of Combinatorial Theory, Series B 72, 157159 (1998)", "Received September 20, 1995".
[^2]: [[tetali-1998-unique-tournaments](pages/tetali-1998-unique-tournaments.md)] p.157 L11-12, L26-32 - "We call a tournament unique, if there is no other tournament (barring isomorphic ones) which shares the same score vector", "Let U_n = {T_n : S(T_n) = S(T'_n) ⇒ T_n ≅ T'_n}. We define Unique = ∪_{n=1}^∞ U_n", "Let u_n denote the cardinality of U_n. That is, u_n is the number of score vectors (or tournaments) on n vertices with the above-mentioned property."
[^3]: [[tetali-1998-unique-tournaments](pages/tetali-1998-unique-tournaments.md)] p.157 L23-25 - "The score vectors (1, 1, 1), (0, 1, 2, 3), and (2, 2, 2, 2, 2) are some obvious examples. In general, any transitive tournament on n vertices (which has the score vector (0, 1, ..., n−1)) is also an example."
[^4]: [[tetali-1998-unique-tournaments](pages/tetali-1998-unique-tournaments.md)] p.157 L39-41 - "Theorem 1. There are exactly four (basic) strong tournaments in Unique (see Fig. 1); any other (nonstrong) tournament in Unique can be decomposed into strong components, each of which is one of the four basic tournaments."
[^5]: [[tetali-1998-unique-tournaments](pages/tetali-1998-unique-tournaments.md)] p.158 L54-56, p.159 L96-106 [synthesis] - Figure 1, "The four basic unique tournaments" (a drawing, not in the text extraction); the proof keeps `(0)`, `(1, 1, 1)`, `(2, 2, 2, 2, 2)` from the list of Theorem 3 and adds "the unique strong tournament on four vertices with the score vector (1, 1, 2, 2)".
[^6]: [[tetali-1998-unique-tournaments](pages/tetali-1998-unique-tournaments.md)] p.157 L33-34, p.159 L111-113, L119 - "We show that u_1 = 1, u_2 = 1, u_3 = 2, u_4 = 4, and u_5 = 7, and for all n > 5, u_n = u_{n−1} + u_{n−3} + u_{n−4} + u_{n−5}", "Remark. It is a basic exercise in recurrence relations to show that the above characterization yields for n ≥ 6, u_n = u_{n−1} + u_{n−3} + u_{n−4} + u_{n−5}".
[^7]: [[tetali-1998-unique-tournaments](pages/tetali-1998-unique-tournaments.md)] p.158 L58-60, L70-71, p.159 L132-133 - "We make use of two existing results (Theorem 2 and Theorem 3 below) to prove the above theorem", "Muller et al. [4] prove, inter alia, the following interesting theorems. We paraphrase the theorems to suit our terminology", and reference 4: "V. Muller, J. Nešetřil, and J. Pelant, Either tournaments or algebras?, Discrete Math. 11 (1975), 37-66."
[^8]: [[tetali-1998-unique-tournaments](pages/tetali-1998-unique-tournaments.md)] p.158 L63-69 - "Definition 1. T_n is simple if, for any proper subset M of V(T_n), there exists a z ∈ V(T_n) ∖ M such that z beats at least one vertex in M and z is beaten by at least one vertex in M. A simple tournament is clearly strong, but the converse is not necessarily true - the strong tournament on four vertices, for example, is not simple. Definition 2. We call a score vector S forcibly simple (FS) if every tournament with the score vector S is simple."
[^9]: [[tetali-1998-unique-tournaments](pages/tetali-1998-unique-tournaments.md)] p.158 L72-82 - "Theorem 2 (Muller et al.). For each score vector S_n which corresponds to a strong tournament on n ≠ 4 vertices, there is a simple tournament which has the same score vector. Theorem 3. (Muller et al.). The following two statements are equivalent: (1) S is forcibly simple; (2) S ∈ {(0), (0, 1), (1, 1, 1), (2, 2, 2, 2, 2), (3, 3, 3, 3, 3, 3, 3)}."
[^10]: [[tetali-1998-unique-tournaments](pages/tetali-1998-unique-tournaments.md)] p.158-159 L84-110 [synthesis] - the proof of Theorem 1, including "it is easy to check that there are three nonisomorphic strong tournaments which have the score vector (3, 3, 3, 3, 3, 3, 3). (Note that this among other things gives us that there are no strong tournaments on six or more vertices which belong to Unique.)" and "the strong components of any nonstrong tournament in Unique are themselves members of Unique".
[^11]: [[tetali-1998-unique-tournaments](pages/tetali-1998-unique-tournaments.md)] p.159 L114-115 [synthesis] - "there exist constants c ≈ 0.48 and α ≈ 1.685 such that lim u_n c α^n = 1", as extracted.
[^12]: Verified by execution (Python 3.11 with SymPy, 2026-10-16): `x⁵ − x⁴ − x² − x − 1` is irreducible over the rationals, with largest root `1.6851371101652…`; from the recurrence, `u_n/α^n = 0.4797670` at `n = 150` and `n = 199`.
[^13]: [[tetali-1998-unique-tournaments](pages/tetali-1998-unique-tournaments.md)] p.157 L35-37 - "This result is similar in spirit to a result of Garey [2], wherein the number of tournaments on n vertices (n ≥ 4) having exactly one Hamiltonian cycle was shown to be F_{2n−6}, the (2n−6)th Fibonacci number (see also [1])."
[^14]: https://oeis.org/A000570 (read 2026-10-16) - "Number of tournaments on n nodes determined by their score vectors", offset 1, "a(n) = a(n-5) + a(n-4) + a(n-3) + a(n-1). - Jon E. Schoenfield, Aug 07 2006", "G.f.: (1+x^2+x^3+x^4)/(1-x-x^3-x^4-x^5). - Harvey P. Dale, May 05 2011", the link to Tetali's paper, and author "Prasad Tetali".
[^15]: Verified by execution (Python 3.11, 2026-10-16): all tournaments on `n ≤ 8` vertices up to isomorphism (1, 1, 2, 4, 12, 56, 456, 6880 classes), generated by adding a vertex and reduced by a canonical form; for each `n` the score vectors, the unique ones (1, 1, 2, 4, 7, 11, 18, 31), the strong unique ones (`(0)`, `(1, 1, 1)`, `(1, 1, 2, 2)`, `(2, 2, 2, 2, 2)` only), simplicity of every class, the forcibly simple score vectors (exactly the five of Theorem 3), a simple realizer for every strong score vector at `n ≠ 4`, and the three classes with score vector `(3, 3, 3, 3, 3, 3, 3)`, all strong.
[^16]: [[tetali-1998-unique-tournaments](pages/tetali-1998-unique-tournaments.md)] p.159 L126-135 - the reference list.
