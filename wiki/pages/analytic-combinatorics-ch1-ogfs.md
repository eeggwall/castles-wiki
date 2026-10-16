---
title: "Analytic Combinatorics Ch. I - OGFs and the Symbolic Method (Flajolet & Sedgewick)"
category: Sources
summary: Chapter I of Flajolet and Sedgewick's Analytic Combinatorics (book pp. 15-94), the symbolic method for unlabeled classes and ordinary generating functions - the dictionary of admissible constructions (Theorem I.1, p. 27), the generating function of a constructible class (Theorem I.2, p. 33), regular specifications with rational generating functions (Proposition I.2, p. 52), compositions with restricted parts, general trees and the Catalan numbers, and the stack polyominoes, which are the convex castles counted by area (Example I.8, pp. 45-46).
tags: [generating-functions, symbolic-method, ogf, admissible-construction, polyomino, catalan, stack-polyomino, source]
sources: [analytic-combinatorics-ch1-ogfs]
created: 2026-09-15
updated: 2026-10-16
---

# Analytic Combinatorics Ch. I - OGFs and the Symbolic Method (Flajolet & Sedgewick)

**Source:** `raw/analytic-combinatorics-part-a.pdf` (Philippe Flajolet and Robert Sedgewick, *Analytic Combinatorics*, Cambridge University Press 2009, ISBN 978-0-521-89806-5), **Chapter I only**, book pp. 15-94. PDF page = book page + 16.
**Date ingested:** 2026-09-15
**Type:** book chapter (Part A: Symbolic Methods, Chapter I: Combinatorial Structures and Ordinary Generating Functions)

This page covers Chapter I. The rest of the book, Chapters II (labeled structures and exponential generating functions, pp. 95-150) and III (multivariate generating functions, pp. 151-220) of Part A, and Parts B (Complex Asymptotics, from p. 221), C (Random Structures, from p. 609) and D (Appendices, from p. 719), is cited by chapter and page where it is used.[^1]

## Summary

Chapter I develops the **symbolic method** for unlabeled combinatorial classes and their ordinary generating functions ([[symbolic-method](pages/symbolic-method.md)]). A class is described by a specification built from admissible constructions, and the specification translates into equations for its generating function. The chapter has seven sections:[^2]

1. §I.1 Symbolic enumeration methods (p. 16): combinatorial classes and their ordinary generating functions `A(z) = Σ_n A_n z^n`.
2. §I.2 Admissible constructions and specifications (p. 24): the dictionary of Theorem I.1 (p. 27), iterative and recursive specifications (Definition I.7, p. 33), and Theorem I.2 (p. 33).
3. §I.3 Integer compositions and partitions (p. 39): `C = SEQ(I)` and `P = MSET(I)`, restricted parts, and the Durfee squares and stack polyominoes of Example I.8 (pp. 45-46).
4. §I.4 Words and regular languages (p. 49): regular specifications (Definition I.10, p. 51) and their rational generating functions (Proposition I.2, p. 52), with runs and patterns in words.
5. §I.5 Tree structures (p. 64).
6. §I.6 Additional constructions (p. 83): constructions with a fixed number of components (Theorem I.3, p. 84), and pointing and substitution (Theorem I.4, p. 87).
7. §I.7 Perspective (p. 92), with the summary dictionary of Figure I.18 (p. 93).

## Key Takeaways

- **The dictionary** (Theorem I.1, p. 27). Disjoint union, cartesian product, sequence, powerset, multiset and cycle are admissible: the counting sequence of the output depends only on those of the inputs (Definition I.5, p. 22). Their operators are `B + C`, `B·C`, `1/(1 − B)`, `exp(Σ_k (−1)^{k−1} B(z^k)/k)`, `exp(Σ_k B(z^k)/k)` and `Σ_k (φ(k)/k) log(1/(1 − B(z^k)))`, with `φ` Euler's totient.[^3] The neutral class `E` has `E(z) = 1` and the atomic class `Z` has `Z(z) = z`.[^4]
- **Constructible classes** (Definition I.8 and Theorem I.2, p. 33). A class with a specification, possibly recursive, in these constructions has a generating function that is a component of the translated system of functional equations.[^5] An iterative specification gives an explicit generating function, and a recursive one an implicit equation.[^6]
- **Regular specifications** (Definition I.10, p. 51, and Proposition I.2, p. 52). An iterative specification using only atoms, unions, products and sequences is regular, and its generating function is rational, obtained by translating atoms into `z`, unions into sums, products into products and sequences into `1/(1 − ·)`.[^7] The tower words of the castles at fixed height form a regular language, recognized by an automaton that tracks the height and the previous letter ([[tower-word-language](pages/tower-word-language.md)]).
- **Compositions** (§I.3, pp. 40-42). `C = SEQ(I)` with `I(z) = z/(1 − z)` gives `C(z) = (1 − z)/(1 − 2z)`, so there are `2^{n−1}` compositions of `n ≥ 1`. The compositions with parts in `{1, …, r}` have generating function `1/(1 − z − ⋯ − z^r) = (1 − z)/(1 − 2z + z^{r+1})` (Equation (41)), whose coefficients at `r = 2` are the Fibonacci numbers `F_{n+1}`.[^8]
- **General trees** (§I.2.3, pp. 34-35). `G = Z × SEQ(G)` gives `G(z) = z/(1 − G(z))`, so `G² − G + z = 0` and `G(z) = (1 − √(1 − 4z))/2 = Σ_{n≥1} (1/n) C(2n−2, n−1) z^n`, the Catalan numbers `A000108` shifted by one ([[catalan-numbers](pages/catalan-numbers.md)]).[^9]
- **Stack polyominoes** (Example I.8, pp. 45-46). A stack polyomino is the diagram of a composition `x_1, …, x_ℓ` with `1 ≤ x_1 ≤ ⋯ ≤ x_j ≥ x_{j+1} ≥ ⋯ ≥ x_ℓ ≥ 1` for some `j`. Splitting at the first tallest column, of height `k`, into a partition into parts at most `k − 1` before it and a partition into parts at most `k` after it gives[^10]

  ```
  S(z)  =  Σ_{k≥1}  z^k/(1 − z^k) · 1/((1 − z)(1 − z²) ⋯ (1 − z^{k−1}))²  =  z + 2z² + 4z³ + 8z⁴ + 15z⁵ + 27z⁶ + 47z⁷ + 79z⁸ + ⋯,
  ```

  the sequence `A001523`. A stack polyomino with columns `x_1, …, x_ℓ` is the [[convex-castle](pages/convex-castle.md)] with skyline `(x_1, …, x_ℓ)`, so `S(z)` counts the convex castles by area ([[stack-polyomino-gf](pages/stack-polyomino-gf.md)]). The same Example decomposes partitions by their Durfee square, the largest square in the diagram.

## Entities & Concepts

- [[symbolic-method](pages/symbolic-method.md)] - the dictionary, Theorem I.2, regular specifications, and the castle tower grammar as a specification.
- [[stack-polyomino-gf](pages/stack-polyomino-gf.md)] - Example I.8 and the convex castles by area.
- [[convex-castle](pages/convex-castle.md)] - the castles with a unimodal skyline, the stack polyominoes.
- [[catalan-numbers](pages/catalan-numbers.md)] - the general trees `G = Z × SEQ(G)`.
- [[tower-word-language](pages/tower-word-language.md)] - the tower words, a regular language at fixed height.
- [[generalized-dyck-grammar](pages/generalized-dyck-grammar.md)] - the tower grammar, a recursive specification in which only `R` has size.
- [[generating-functions](pages/generating-functions.md)] - the castle generating functions `E_k(x)` and `P_k(x)`.
- [[polyominoes](pages/polyominoes.md)] and [[column-convex-polyomino](pages/column-convex-polyomino.md)] - the polyomino families that contain the stack polyominoes.
- [[dyck-words](pages/dyck-words.md)] and [[lattice-paths](pages/lattice-paths.md)] - Dyck words and lattice paths as specifications.

## Relation to Other Wiki Pages

The wiki has three sources on generating functions. This chapter starts from a specification of a class, while [[aocp-generating-functions](pages/aocp-generating-functions.md)] (Knuth) and [[generating-functions-topic](pages/generating-functions-topic.md)] start from a recurrence for the counts and reach a rational generating function by coefficient matching and partial fractions. The castle generating functions on [[castle-counting-formula](pages/castle-counting-formula.md)] are reached from the tower grammar, a specification, and their recurrences in `L` are read off afterwards.

## Footnotes

[^1]: [[analytic-combinatorics-ch1-ogfs](pages/analytic-combinatorics-ch1-ogfs.md)] "Contents" p.iii - "Part A. SYMBOLIC METHODS 13", "Part B. COMPLEX ASYMPTOTICS 221", "Part C. RANDOM STRUCTURES 609", "Part D. APPENDICES 719", with Chapters I-III listed under Part A.
[^2]: [[analytic-combinatorics-ch1-ogfs](pages/analytic-combinatorics-ch1-ogfs.md)] Chapter I title page p.15 - "I.1. Symbolic enumeration methods 16 / I.2. Admissible constructions and specifications 24 / I.3. Integer compositions and partitions 39 / I.4. Words and regular languages 49 / I.5. Tree structures 64 / I.6. Additional constructions 83 / I.7. Perspective 92".
[^3]: [[analytic-combinatorics-ch1-ogfs](pages/analytic-combinatorics-ch1-ogfs.md)] Theorem I.1 p.27 - "The constructions of union, cartesian product, sequence, powerset, multiset, and cycle are all admissible. The associated operators are as follows", with the six operators; Definition I.5 p.22 - "The construction Φ is admissible iff the counting sequence (A_n) of A only depends on the counting sequences (B_n^(1)), …, (B_n^(m)) of B^(1), …, B^(m)."
[^4]: [[analytic-combinatorics-ch1-ogfs](pages/analytic-combinatorics-ch1-ogfs.md)] Theorem I.1 p.28 - "The class E = {ε} consisting of the neutral object only, and the class Z consisting of a single \"atomic\" object (node, letter) of size 1 have OGFs E(z) = 1 and Z(z) = z."
[^5]: [[analytic-combinatorics-ch1-ogfs](pages/analytic-combinatorics-ch1-ogfs.md)] Definition I.8 and Theorem I.2 pp.33-34 - "A class of combinatorial structures is said to be constructible or specifiable iff it admits a (possibly recursive) specification in terms of sum, product, sequence, set, multiset, and cycle constructions", "The generating function of a constructible class is a component of a system of functional equations whose terms are built from 1, z, +, ×, Q, Exp, Exp̄, Log".
[^6]: [[analytic-combinatorics-ch1-ogfs](pages/analytic-combinatorics-ch1-ogfs.md)] §I.2.3 p.34 - "iterative classes have explicit generating functions involving compositions of the basic operators only, while recursive structures have OGFs that are accessible indirectly via systems of functional equations."
[^7]: [[analytic-combinatorics-ch1-ogfs](pages/analytic-combinatorics-ch1-ogfs.md)] Definition I.10 p.51 and Proposition I.2 p.52 - "An iterative specification that only involves atoms (e.g., letters of a finite alphabet A) together with combinatorial sums, cartesian products, and sequence constructions is said to be a regular specification", "Any S-regular language has an OGF that is a rational function. This OGF is obtained from a regular specification of the language by translating each letter into the variable z, disjoint unions into sums, cartesian products into products, and sequences into quasi-inverses, (1 − ·)^{−1}."
[^8]: [[analytic-combinatorics-ch1-ogfs](pages/analytic-combinatorics-ch1-ogfs.md)] §I.3 pp.40-42 - "C = SEQ(I) ⟹ C(z) = 1/(1 − I(z))", "C_n = 2^{n−1}, n ≥ 1", and Equation (41), "compositions all of whose summands lie in the set {1, 2, …, r} have generating function C^{1..r}(z) = 1/(1 − z − z² − ⋯ − z^r) = (1 − z)/(1 − 2z + z^{r+1})". Both recomputed, the second for `r ≤ 4` (SymPy, 2026-10-16).
[^9]: [[analytic-combinatorics-ch1-ogfs](pages/analytic-combinatorics-ch1-ogfs.md)] §I.2.3 pp.34-35 - "The recursive specification of general trees leads to an implicit definition of their OGF, G = Z × SEQ(G) ⟹ G(z) = z/(1 − G(z))", "G − G² − z = 0", "G(z) = ½(1 − √(1 − 4z)) = z + z² + 2z³ + 5z⁴ + 14z⁵ + 42z⁶ + 132z⁷ + 429z⁸ + ⋯", "general trees are enumerated by Catalan numbers". Coefficients recomputed and checked against https://oeis.org/A000108 (2026-10-16).
[^10]: [[analytic-combinatorics-ch1-ogfs](pages/analytic-combinatorics-ch1-ogfs.md)] Example I.8 "The Durfee square of partitions and stack polyominoes" pp.45-46 - "A stack polyomino is the diagram of a composition such that for some j, ℓ, one has 1 ≤ x_1 ≤ x_2 ≤ ⋯ ≤ x_j ≥ x_{j+1} ≥ ⋯ ≥ x_ℓ ≥ 1", "k ↦ P^{1,…,k−1} × Z^k × P^{1,…,k}", "the number of stack polyominoes (EIS A001523): S(z) = z + 2z² + 4z³ + 8z⁴ + 15z⁵ + 27z⁶ + 47z⁷ + 79z⁸ + ⋯". The series recomputed from the formula and checked against https://oeis.org/A001523 (2026-10-16).
