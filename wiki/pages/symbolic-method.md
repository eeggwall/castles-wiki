---
title: Symbolic method
category: Concepts
summary: Flajolet and Sedgewick's dictionary from combinatorial specifications to ordinary generating functions - disjoint union, product, sequence, powerset, multiset and cycle, each with an operator on generating functions (Theorem I.1), so that a specified class has a generating function solving the translated system (Theorem I.2). Regular specifications give rational generating functions (Proposition I.2). The tower grammar of the castles is a recursive specification, and Equation (2) of castle-counting-formula is its translation.
tags: [concept, generating-functions, symbolic-method, admissible-construction, specification, ogf]
sources: [analytic-combinatorics-ch1-ogfs]
created: 2026-09-15
updated: 2026-10-25
---

# Symbolic method

## The dictionary

A combinatorial class is a set of objects with a size, finitely many of each size, and its ordinary generating function is `A(z) = Σ_n A_n z^n`, with `A_n` the number of objects of size `n`. The **symbolic method** of Flajolet and Sedgewick describes a class by a **specification**, an equation or system of equations built from a fixed set of constructions, and translates each construction into an operation on generating functions.[^1] The constructions are:[^2]

| construction | class relation | generating function |
|---|---|---|
| disjoint union | `A = B + C` | `A(z) = B(z) + C(z)` |
| cartesian product | `A = B × C` | `A(z) = B(z) · C(z)` |
| sequence | `A = SEQ(B)` | `A(z) = 1/(1 − B(z))` |
| powerset | `A = PSET(B)` | `A(z) = exp(Σ_{k≥1} (−1)^{k−1} B(z^k)/k)` |
| multiset | `A = MSET(B)` | `A(z) = exp(Σ_{k≥1} B(z^k)/k)` |
| cycle | `A = CYC(B)` | `A(z) = Σ_{k≥1} (φ(k)/k) · log(1/(1 − B(z^k)))` |

Here `φ(k)` is Euler's totient, the number of integers in `[1, k]` prime to `k`. `SEQ(B)` requires `B` to have no object of size 0.[^2] The constructions start from two classes: the neutral class `E`, one object of size 0, with `E(z) = 1`, and the atomic class `Z`, one object of size 1, with `Z(z) = z`.[^3] Two further constructions translate as well: **pointing**, `A(z) = z·B′(z)`, and **substitution**, `A(z) = B(C(z))`.[^4]

A construction is **admissible** when the counting sequence of its output depends only on the counting sequences of its inputs (Definition I.5), and Theorem I.1 states that the six constructions of the table are admissible with the operators shown.[^5] A class is **constructible**, or specifiable, when it has a specification, possibly recursive, in these constructions (Definition I.8).[^6] Theorem I.2 then states that the generating function of a constructible class is a component of the system of functional equations obtained by translating its specification.[^7]

*Example.* The binary words are `W = SEQ(Z + Z)`, so `W(z) = 1/(1 − 2z)` and there are `2^n` words of length `n`.[^7]

## Iterative and recursive specifications

A specification is **iterative** when no class in it depends on itself, directly or through other classes; then the class is a single term in `E`, `Z` and the constructions, and its generating function is explicit. Otherwise it is **recursive**, and the generating function is a solution of the translated system (Definition I.7).[^8]

- The compositions of `n`, sequences of positive integers with sum `n`, are iterative: `C = SEQ(I)` with `I = SEQ_{≥1}(Z)`, so `I(z) = z/(1 − z)` and `C(z) = (1 − z)/(1 − 2z)`, which gives `2^{n−1}` compositions of `n ≥ 1`.[^9]
- The general (rooted plane) trees are recursive: a tree is a root and a sequence of trees, `G = Z × SEQ(G)`, so `G(z) = z/(1 − G(z))`. Solving the quadratic `G² − G + z = 0` gives `G(z) = (1 − √(1 − 4z))/2 = z + z² + 2z³ + 5z⁴ + 14z⁵ + ⋯`, the [[catalan-numbers](pages/catalan-numbers.md)] shifted by one.[^10]

## Regular specifications and rational generating functions

A **regular specification** is an iterative specification that uses only atoms, disjoint unions, products and sequences (Definition I.10). Proposition I.2 states that a class with a regular specification has a rational generating function, obtained by translating each atom into `z`, unions into sums, products into products, and sequences into `1/(1 − ·)`.[^11]

This is one route to a rational generating function. The other runs through a linear recurrence with constant coefficients: multiplying by the denominator and matching coefficients turns the recurrence into a rational generating function and back ([[generating-functions](pages/generating-functions.md)], [[aocp-generating-functions](pages/aocp-generating-functions.md)]). The two routes start from different data, a specification of the class or a recurrence for its counts.

*Example.* The compositions of `n` into parts in `{1, …, r}` are `SEQ(Z + Z² + ⋯ + Z^r)`, a regular specification, with generating function `1/(1 − z − ⋯ − z^r) = (1 − z)/(1 − 2z + z^{r+1})`. At `r = 2` the coefficients are the Fibonacci numbers `F_{n+1}`.[^12]

## The castles

- **The towers.** The towers of height at most `k` on a base of length `L` are given by their column heights in `{0, …, k}^L` ([[castle-counting-formula](pages/castle-counting-formula.md)], the section *Tower count*), so as a class they are `SEQ(Z + Z + ⋯ + Z)`, with `k + 1` copies of `Z`, one for each height of a column, and `E_k(x) = Σ_L T(k, L) x^L = 1/(1 − (k+1)x)`.
- **The tower grammar.** The [[generalized-dyck-grammar](pages/generalized-dyck-grammar.md)] `E_k → empty | R E_k | U V D (empty | R E_k)` is a recursive specification in which each `R` is an atom and `U` and `D` have size 0. Equation (2) of [[castle-counting-formula](pages/castle-counting-formula.md)] is its translation by the rules for unions and products. The signed count `P_k(x)` weights each block by `−1`, so it is a weighted sum over the class rather than the generating function of a class; Equation (3) there is the same translation with a factor `−1` on the production `U V D`. With a second variable `y` marking each block, the translation is one equation for the class graded by width and blocks, and solving it for `E_k` gives a Möbius map in `E_{k−1}` whose cases `y = 1` and `y = −1` are Equations (2) and (3) ([[generalized-dyck-grammar](pages/generalized-dyck-grammar.md)], section *Counts*).
- **Regular languages.** At fixed height the tower words form a regular language: a finite automaton that tracks the height and the previous letter recognizes them ([[tower-word-language](pages/tower-word-language.md)]), so their generating function is rational, as `E_k(x)` and `P_k(x)` are.
- **Stack polyominoes.** The stack polyominoes, whose column heights weakly rise and then weakly fall, are the convex castles counted by area. Example I.8 specifies them by the first tallest column, `Z^k`, with a partition into parts at most `k − 1` before it and a partition into parts at most `k` after it ([[stack-polyomino-gf](pages/stack-polyomino-gf.md)]).

## Appearances in Sources

- [[analytic-combinatorics-ch1-ogfs](pages/analytic-combinatorics-ch1-ogfs.md)] - Chapter I of *Analytic Combinatorics*: the dictionary (Theorem I.1, p. 27), Theorem I.2 (p. 33), regular specifications (Definition I.10, p. 51, and Proposition I.2, p. 52), pointing and substitution (Theorem I.4, p. 87), and the summary table (Figure I.18, p. 93).

## Related Concepts

- [[generating-functions](pages/generating-functions.md)] - the castle generating functions `E_k(x)` and `P_k(x)`, and reading a recurrence off a rational generating function.
- [[aocp-generating-functions](pages/aocp-generating-functions.md)] - Knuth's route from a linear recurrence to a rational generating function and its partial fractions.
- [[generating-functions-topic](pages/generating-functions-topic.md)] - worked examples of recurrences, partial fractions and exponential generating functions.
- [[generalized-dyck-grammar](pages/generalized-dyck-grammar.md)] - the tower grammar, a recursive specification.
- [[tower-word-language](pages/tower-word-language.md)] - the tower words as a formal language, regular at fixed height.
- [[stack-polyomino-gf](pages/stack-polyomino-gf.md)] - Example I.8, the generating function of the stack polyominoes by area (A001523).
- [[catalan-numbers](pages/catalan-numbers.md)] - the general trees `G = Z × SEQ(G)`.
- [[block-count-constraints](pages/block-count-constraints.md)] - compositions with parts in a set `D`, `SEQ`, against the coin-change series `Π 1/(1 − z^d)`, `MSET`, over the same parts.
- [[aocp-multisets](pages/aocp-multisets.md)] - Knuth's permutations of a multiset, which are words with repeated letters, built by `SEQ`, not `MSET` objects.
- [[multiset-partitions](pages/multiset-partitions.md)] - partitions of one fixed multiset into blocks, which are not built by `MSET` either.
- [[generating-function-gallery](pages/generating-function-gallery.md)] - the polynomials `num_k`, `den_k` of `P_k(x)` and their roots.

## Footnotes

[^1]: [[analytic-combinatorics-ch1-ogfs](pages/analytic-combinatorics-ch1-ogfs.md)] §I.1 p.15 - "The principle is that many general set-theoretic constructions admit a direct translation as operations over generating functions. This principle is made concrete by means of a dictionary that includes a collection of core constructions, namely the operations of union, cartesian product, sequence, set, multiset, and cycle."
[^2]: [[analytic-combinatorics-ch1-ogfs](pages/analytic-combinatorics-ch1-ogfs.md)] Theorem I.1 p.27 - "Sum: A = B + C ⟹ A(z) = B(z) + C(z); Cartesian product: A = B × C ⟹ A(z) = B(z) · C(z); Sequence: A = SEQ(B) ⟹ A(z) = 1/(1 − B(z))", with the powerset, multiset and cycle operators and "the Euler totient function ϕ(k) defined as the number of integers in [1, k] that are relatively prime to k"; p.25 - "the construction A = SEQ(B) defines a proper class satisfying the finiteness condition for sizes if and only if B contains no object of size 0".
[^3]: [[analytic-combinatorics-ch1-ogfs](pages/analytic-combinatorics-ch1-ogfs.md)] Theorem I.1 p.28 - "The class E = {ε} consisting of the neutral object only, and the class Z consisting of a single \"atomic\" object (node, letter) of size 1 have OGFs E(z) = 1 and Z(z) = z."
[^4]: [[analytic-combinatorics-ch1-ogfs](pages/analytic-combinatorics-ch1-ogfs.md)] Theorem I.4 p.87 - "The constructions of pointing and substitution are admissible: A = ΘB ⟹ A(z) = z∂_z B(z), A = B ∘ C ⟹ A(z) = B(C(z))"; also Figure I.18 p.93.
[^5]: [[analytic-combinatorics-ch1-ogfs](pages/analytic-combinatorics-ch1-ogfs.md)] Definition I.5 p.22 - "The construction Φ is admissible iff the counting sequence (A_n) of A only depends on the counting sequences (B_n^(1)), …, (B_n^(m)) of B^(1), …, B^(m)"; Theorem I.1 p.27 - "The constructions of union, cartesian product, sequence, powerset, multiset, and cycle are all admissible."
[^6]: [[analytic-combinatorics-ch1-ogfs](pages/analytic-combinatorics-ch1-ogfs.md)] Definition I.8 p.33 - "A class of combinatorial structures is said to be constructible or specifiable iff it admits a (possibly recursive) specification in terms of sum, product, sequence, set, multiset, and cycle constructions."
[^7]: [[analytic-combinatorics-ch1-ogfs](pages/analytic-combinatorics-ch1-ogfs.md)] Theorem I.2 pp.33-34 - "The generating function of a constructible class is a component of a system of functional equations whose terms are built from 1, z, +, ×, Q, Exp, Exp̄, Log"; p.34 - "W = SEQ(Z + Z) ⟹ W(z) = 1/(1 − 2z), whence the expected result, W_n = 2^n".
[^8]: [[analytic-combinatorics-ch1-ogfs](pages/analytic-combinatorics-ch1-ogfs.md)] Definition I.7 p.33 - "the system (29) is an iterative or non-recursive specification if it is strictly upper-triangular ... for an iterative specification, A^(1) can be equivalently described by a single term involving only the initial classes and the basic constructors. Otherwise, the system is said to be recursive"; p.34 - "iterative classes have explicit generating functions involving compositions of the basic operators only, while recursive structures have OGFs that are accessible indirectly via systems of functional equations."
[^9]: [[analytic-combinatorics-ch1-ogfs](pages/analytic-combinatorics-ch1-ogfs.md)] §I.3 pp.40-41 - "C = SEQ(I) ⟹ C(z) = 1/(1 − I(z))", "C_n = 2^{n−1}, n ≥ 1", with `I(z) = z/(1 − z)` from Note I.5, p.27.
[^10]: [[analytic-combinatorics-ch1-ogfs](pages/analytic-combinatorics-ch1-ogfs.md)] §I.2.3 pp.34-35 - "The recursive specification of general trees leads to an implicit definition of their OGF, G = Z × SEQ(G) ⟹ G(z) = z/(1 − G(z))", "G − G² − z = 0", "G(z) = ½(1 − √(1 − 4z)) = z + z² + 2z³ + 5z⁴ + 14z⁵ + 42z⁶ + 132z⁷ + 429z⁸ + ⋯".
[^11]: [[analytic-combinatorics-ch1-ogfs](pages/analytic-combinatorics-ch1-ogfs.md)] Definition I.10 p.51 - "An iterative specification that only involves atoms (e.g., letters of a finite alphabet A) together with combinatorial sums, cartesian products, and sequence constructions is said to be a regular specification"; Proposition I.2 p.52 - "Any S-regular language has an OGF that is a rational function. This OGF is obtained from a regular specification of the language by translating each letter into the variable z, disjoint unions into sums, cartesian products into products, and sequences into quasi-inverses, (1 − ·)^{−1}."
[^12]: [[analytic-combinatorics-ch1-ogfs](pages/analytic-combinatorics-ch1-ogfs.md)] §I.3 p.42, Equation (41) - "compositions all of whose summands lie in the set {1, 2, …, r} have generating function C^{1..r}(z) = 1/(1 − z − z² − ⋯ − z^r) = (1 − z)/(1 − 2z + z^{r+1})". The identity and the Fibonacci case recomputed for `r ≤ 4` (SymPy, 2026-10-16).
