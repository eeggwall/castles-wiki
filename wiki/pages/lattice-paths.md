---
title: Lattice paths (Project Euler 15)
category: Sources
summary: The topic page on Project Euler 15 counts the shortest paths through a W × H lattice by writing a path as a string of W right steps and H down steps and counting the distinct permutations of that multiset, binomial(W+H, H) by stars and bars. It extends the count to higher dimensions as a multinomial coefficient, (3n)!/(n!)³ for a cube. The castle's U/R/D step strings reuse this string encoding.
tags: [lattice-paths, project-euler, stars-and-bars, binomial, multiset, urd, symbolic-method, source]
sources: [lattice-paths]
created: 2026-09-13
updated: 2026-10-16
---

# Lattice paths (Project Euler 15)

**Source:** https://charlesreid1.com/wiki/Lattice_Paths (Project Euler [Problem 15](https://projecteuler.net/problem=15))
**Date ingested:** 2026-09-13
**Type:** article (MediaWiki topic page)

## Summary

Project Euler 15 asks for the number of shortest paths through a `20 × 20` lattice, from one corner to the opposite one. The source writes a path as a string of steps, `D` for one step down and `R` for one step right: in a lattice of `2 × 2` squares, `DDRR` is the path that goes down two steps and then right two. Counting paths is then counting the distinct permutations of the multiset of letters.[^1]

A path through a lattice of width `W` and height `H` has `W` letters `R` and `H` letters `D`. The `W` letters `R` make `W + 1` gaps, before, between and after them, and a path places its `H` letters `D` in these gaps, any number in each. By stars and bars the number of placements is[^2]

```
paths(W, H)  =  C(H + (W + 1) − 1, H)  =  C(W + H, H).
```

At `W = H = 2` the six paths are `DDRR`, `DRDR`, `DRRD`, `RDDR`, `RDRD` and `RRDD`, and `C(4, 2) = 6`.[^3] The source gives `C(4 + 2, 2) = 15` for a `4 × 2` lattice, `C(8 + 8, 8) = 12 870` for `8 × 8`, and the value of `C(40, 20)` for `20 × 20` with its last three digits hidden, since it is the answer to Problem 15.[^4]

**Higher dimensions.** A shortest path through a `d`-dimensional lattice with `N_i` steps in direction `i` is a permutation of a multiset with `N_i` copies of letter `i`, and their number is the multinomial coefficient `N!/(N_1! ⋯ N_d!)` with `N = N_1 + ⋯ + N_d`. The source computes it as a product of binomial coefficients, choosing the places of one letter at a time.[^5] For the `4 × 4 × 6` lattice, with letters `U`, `R` and `B`,

```
C(14; 4, 4, 6)  =  C(14, 4) · C(10, 4)  =  1001 · 210  =  210 210.
```

For a cube of side `n` the count is `(3n)!/(n!)³`, which is 90 at `n = 2`, the permutations of `UURRBB`. The source's four-dimensional example, a `3 × 4 × 5 × 3` lattice, gives `15!/(3! 4! 5! 3!) = 12 612 600`.[^6]

## Relevance to the castle

The castle's step strings reuse this encoding. The Representations subpage of Project Euler 502 writes a castle as a string in `U`, `R` and `D`, "the same representation used to solve the Lattice Paths problem in Project Euler 15" ([[urd-step-strings](pages/urd-step-strings.md)], [[project-euler-502-representations](pages/project-euler-502-representations.md)]).[^7] The convex castles are counted by the same stars-and-bars argument: their `w − 1` letters `R` beyond the bare-minimum string `U^h R D^h` go into `2h − 1` slots, which gives `C(2h + w − 3, w − 1)` ([[convex-castle](pages/convex-castle.md)], [[convex-castle-binomial-identity](pages/convex-castle-binomial-identity.md)]).

In the symbolic method, which the source does not use, the paths are the words in `SEQ(R + D)` with `W` letters `R` and `H` letters `D`; marking `R` by `x` and `D` by `y`, their number is the coefficient `[x^W y^H] 1/(1 − x − y) = C(W + H, H)` ([[symbolic-method](pages/symbolic-method.md)], [[analytic-combinatorics-ch1-ogfs](pages/analytic-combinatorics-ch1-ogfs.md)]).

## Key Takeaways

- A shortest lattice path is a permutation of a multiset of steps, so `paths(W, H) = C(W + H, H)` by stars and bars.[^2]
- In `d` dimensions the count is the multinomial coefficient `N!/(N_1! ⋯ N_d!)`, `(3n)!/(n!)³` for a cube.[^5][^6]
- The castle's U/R/D step strings come from this encoding, and the convex castles are counted by the same stars-and-bars argument.[^7]

## Entities & Concepts

- [[urd-step-strings](pages/urd-step-strings.md)] - the castle's step-string encoding.
- [[convex-castle](pages/convex-castle.md)] and [[convex-castle-binomial-identity](pages/convex-castle-binomial-identity.md)] - the convex castles, counted by stars and bars.
- [[dyck-words](pages/dyck-words.md)] - the lattice paths that never go below the diagonal, counted by the Catalan numbers.
- [[aocp-multisets](pages/aocp-multisets.md)] - permutations of multisets.
- [[aocp-multinomial-coefficients](pages/aocp-multinomial-coefficients.md)] - the multinomial coefficient as a product of binomial coefficients.
- [[symbolic-method](pages/symbolic-method.md)] and [[analytic-combinatorics-ch1-ogfs](pages/analytic-combinatorics-ch1-ogfs.md)] - words as sequences of letters.

## Footnotes

[^1]: [[lattice-paths](pages/lattice-paths.md)] §"Formulating the Problem" L11-17 - "We can represent the particular path we take using a string, so the following would represent the path that travels down two squares then right two squares: DDRR", "How many ''unique'' permutations of the above string are there?"
[^2]: [[lattice-paths](pages/lattice-paths.md)] §"Number of Paths Thru Lattices of Arbitrary Size" L96-113 - "on a lattice of width W and height H, we have W right moves that form W+1 partitions, in which we are placing H items", "(H) multichoose (W+1) = \binom{W+1+H-1}{H} = \binom{W+H}{H}".
[^3]: [[lattice-paths](pages/lattice-paths.md)] §"Multiset Approach for Two Variables" L58-68 [synthesis] - the six placements of two `*` among the `R`s of `RR` for the `2 × 2` lattice.
[^4]: [[lattice-paths](pages/lattice-paths.md)] §"Number of Paths Thru Lattices of Arbitrary Size" L116-133 - "\binom{4+2}{2} = \binom{4+2}{4} = 15", "\binom{8+8}{8} = 12,870", "\binom{20+20}{20} = 137,846,528,\mbox{XXX}". Recomputed (Python 3.11, 2026-10-16).
[^5]: [[lattice-paths](pages/lattice-paths.md)] §"Generalizing to 3-Dimensional and Higher-Dimensional Lattices" L159-203 [synthesis] - the string `UUUURRRRBBBBBB` for the `4 × 4 × 6` lattice, counted by placing the `U`s, "\binom{14}{10} = 1001", then the `R`s among the rest, "\binom{10}{4} = 210", giving "P = \binom{14}{4} \cdot \binom{10}{4} = 210,210".
[^6]: [[lattice-paths](pages/lattice-paths.md)] §"Special Case: Perfect Cube Lattice" L207-211 and §"4 Dimensional Lattice Example" L215-216 - "\dfrac{(3n)!}{(n!)^3}" and "P = 12,612,600 = binomial(15; 3,4,5,3)". Both recomputed (Python 3.11, 2026-10-16).
[^7]: [[project-euler-502-representations](pages/project-euler-502-representations.md)] §"Steps-Based Approach" L78 - "The representation that led to the most breakthroughs in progressing with PE 502 was the same representation used to solve the Lattice Paths problem in Project Euler/15."
