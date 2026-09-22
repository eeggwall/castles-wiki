---
title: Lattice paths (Project Euler 15)
category: Sources
summary: Shortest lattice paths as multiset permutations of a step string — C(W+H,H) by stars-and-bars — and higher-dimensional multinomial generalizations; the origin of the castle's U/R/D encoding. Under the [[symbolic-method]], a shortest lattice path is `SEQ(R + D)` restricted to fixed letter counts.
tags: [lattice-paths, project-euler, stars-and-bars, binomial, multiset, urd, symbolic-method, source]
sources: [lattice-paths]
created: 2026-09-13
updated: 2026-09-19
---

# Lattice paths (Project Euler 15)

**Source:** https://charlesreid1.com/wiki/Lattice_Paths (Project Euler [Problem 15](https://projecteuler.net/problem=15))
**Date ingested:** 2026-09-13
**Type:** article (MediaWiki topic page)

## Summary

Project Euler 15 asks for the number of shortest (monotone) paths across a *W*×*H* grid. The key move is to encode a path as a **string of steps** — e.g. `DDRR` for a 2×2 path — so that counting paths becomes counting *unique permutations* of that multiset of steps.[^1] This is the source of the **U/R/D step-string encoding** that the castle problem reuses (see [[urd-step-strings](pages/urd-step-strings.md)]).

Because the string has *H* down moves and *W* right moves, its distinct permutations are a **stars-and-bars** count — distribute the *H* down moves among the `W+1` gaps around the *W* right moves — giving the multichoose / binomial[^2]

```
paths(W,H) = H multichoose (W+1) = binomial(W+H, H)
```

Worked values (verified during ingest): `binomial(4+2,2) = 15`, `binomial(8+8,8) = 12870`, and the 20×20 grid `binomial(40,20) = 137,846,528,820` (the source obscures the low digits, as it is the PE 15 answer).[^3]

The page then **generalizes to higher dimensions**: a path through a `d`-dimensional lattice is a multiset permutation of a step string with `N_i` steps in each direction, counted by the multinomial `binomial(N; N_1,…,N_d) = N! / (N_1!···N_d!)` (e.g. a 3×4×5×3 4-D lattice gives `binomial(15; 3,4,5,3) = 12,612,600`), with the perfect-cube special case reducing to `(3n)!/(n!)³`.[^4] That multinomial is computed as a **telescoping product of binomials** (see [[aocp-multinomial-coefficients](pages/aocp-multinomial-coefficients.md)]): `C(15;3,4,5,3) = C(14,4)·C(10,4)·…`.

## Relevance to the castle

Two direct connections:

- **The U/R/D encoding comes from here.** The castle's step-string representation ([[urd-step-strings](pages/urd-step-strings.md)]) is the same device — "the same representation used to solve the Lattice Paths problem in Project Euler 15" — extended from two step types (R, D) to three (U, R, D) with the additional castle constraints.[^1]
- **Stars-and-bars is the castle's convex count.** The very argument that counts lattice paths — distributing moves into gaps via stars-and-bars — is what counts [[convex-castle](pages/convex-castle.md)]s: `CCC = C(2H+W−3, W−1)` comes from inserting the remaining `R`s into the bare-minimum string's slots. Both are *binomial* for the same reason (independent placements, no ballot constraint) — see [[convex-castle-binomial-identity](pages/convex-castle-binomial-identity.md)].

Unlike Dyck paths (which impose the never-go-negative *ballot* constraint and are counted by Catalan numbers), an unconstrained lattice path is just a multiset permutation and is counted by a plain binomial — the same binomial-vs-Catalan distinction that runs through the castle.

**Under the [[symbolic-method](pages/symbolic-method.md)].** A shortest lattice path over the 2-letter alphabet `{R, D}` is a word in `SEQ(R + D)` — the compositions/words machinery of [[analytic-combinatorics-ch1-ogfs](pages/analytic-combinatorics-ch1-ogfs.md)] §I.3-I.4. Marking `R` and `D` with separate size variables `x, y` gives the bivariate ordinary generating function (OGF) `1/(1 − x − y)`, and `[x^W y^H]` extracts the `binomial(W+H, H)` count — the same stars-and-bars result derived from the specification rather than from balls-and-bars combinatorics. Lattice paths with more constraints (bounded run length, non-negativity, staying inside a strip) are analyzed at length in Analytic Combinatorics (AC) Chapter V (`Applications of Rational and Meromorphic Asymptotics`), §V.4 "Nested sequences, lattice paths, and continued fractions" — the natural next-chapter home for the wiki's [[tower-word-continued-fraction](pages/tower-word-continued-fraction.md)] thread when we ingest Part B.

## Key Takeaways

- Encode a shortest path as a step string; counting paths = counting multiset permutations.[^1]
- `paths(W,H) = binomial(W+H, H)` by stars-and-bars; e.g. 20×20 → `binomial(40,20)` (verified).[^2][^3]
- Higher dimensions: multinomial `binomial(N; N_1,…,N_d)`; perfect cube → `(3n)!/(n!)³`.[^4]
- This is the origin of the castle's [[urd-step-strings](pages/urd-step-strings.md)] encoding and shares the stars-and-bars mechanism with the [[convex-castle](pages/convex-castle.md)] count.[^1]

## Entities & Concepts

- [[urd-step-strings](pages/urd-step-strings.md)] — the castle's step-string encoding, taken from this problem.
- [[convex-castle](pages/convex-castle.md)] / [[convex-castle-binomial-identity](pages/convex-castle-binomial-identity.md)] — the stars-and-bars binomial count shared with lattice paths.
- [[dyck-words](pages/dyck-words.md)] — the ballot-constrained cousin (Catalan, not binomial).
- [[symbolic-method](pages/symbolic-method.md)] / [[analytic-combinatorics-ch1-ogfs](pages/analytic-combinatorics-ch1-ogfs.md)] — the framework: shortest lattice paths as `SEQ(R+D)`; constrained lattice paths as AC Chapter V.4.

Related (ingested): [[aocp-multisets](pages/aocp-multisets.md)] — the multiset-permutation machinery; [[aocp-multinomial-coefficients](pages/aocp-multinomial-coefficients.md)] — the multinomial that counts the higher-D paths. Linked from the source but not yet ingested: Project Euler/172.

## Relation to Other Wiki Pages

The origin of the U/R/D encoding and a clean statement of the stars-and-bars / binomial mechanism that recurs in the castle's convex count. Together with [[dyck-words](pages/dyck-words.md)] it frames the binomial-vs-Catalan divide: unconstrained lattice paths are binomial, ballot-constrained Dyck paths are Catalan, and the castle sits on the binomial side (except in the tower block-count, where Narayana appears).

## Footnotes

[^1]: [[lattice-paths](pages/lattice-paths.md)] §"Formulating the Problem"/"Multiset Approach" L11-41 — "We can represent the particular path we take using a string ... DDRR ... How many unique permutations of the above string are there? ... This is what's often called a stars-and-bars problem in combinatorics."
[^2]: [[lattice-paths](pages/lattice-paths.md)] §"Number of Paths Thru Lattices of Arbitrary Size" L94-113 — "on a lattice of width W and height H, we have W right moves that form W+1 partitions, in which we are placing H items ... (H) multichoose (W+1) = binomial(W+1+H-1, H) = binomial(W+H, H)."
[^3]: [[lattice-paths](pages/lattice-paths.md)] §"Number of Paths..." L118-132 — "binomial(4+2, 2) = 15 ... binomial(8+8, 8) = 12,870 ... binomial(20+20, 20) = 137,846,528,XXX"; binomial(6,2)=15, binomial(16,8)=12870, binomial(40,20)=137,846,528,820 re-verified during ingest.
[^4]: [[lattice-paths](pages/lattice-paths.md)] §"Generalizing to ... Higher-Dimensional Lattices"/"Special Case"/"4 Dimensional Lattice Example" L135-210 — the multinomial "binomial(N; N_1, N_2, ..., N_k) = N!/(N_1!...N_k!)", the perfect-cube "(3n)!/(n!)^3", and "binomial(15; 3,4,5,3) = 12,612,600."
