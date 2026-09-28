---
title: "Analytic Combinatorics Ch. I - OGFs and the Symbolic Method (Flajolet & Sedgewick)"
category: Sources
summary: Flajolet & Sedgewick's Chapter I only - Combinatorial Structures and Ordinary Generating Functions (book pp. 15-94, ~80 pages). Recasts recurrence-⇒-rational-GF as one case of the [[symbolic-method]] (SEQ/MSET/PSET/CYC dictionary), and constructs stack polyominoes (the convex castles) and Catalan trees directly as specifications. Chapters II (EGFs) and III (MGFs) of Part A are outside this page; cite the book directly for those.
tags: [generating-functions, symbolic-method, ogf, admissible-construction, polyomino, catalan, stack-polyomino, source]
sources: [analytic-combinatorics-ch1-ogfs]
created: 2026-09-15
updated: 2026-09-28
---

# Analytic Combinatorics Ch. I - OGFs and the Symbolic Method (Flajolet & Sedgewick)

**Source:** `raw/analytic-combinatorics-part-a.pdf` (Flajolet & Sedgewick, *Analytic Combinatorics*, Cambridge University Press 2009, ISBN 978-0-521-89806-5) - **Chapter I only** (book pp. 15-94, ~80 pages)
**Date ingested:** 2026-09-15
**Type:** book chapter (Part A: Symbolic Methods, Chapter I: `Combinatorial Structures and Ordinary Generating Functions`)

> **Scope.** Only Chapter I is summarized here. Part A's remaining chapters (II: labelled structures / EGFs, book pp. 95-150; III: multivariate GFs / MGFs, pp. 151-220) and Parts B (Complex Asymptotics), C (Random Structures), D (Appendices) are not read here; cite the book directly by chapter and page for those.

## Summary

Flajolet & Sedgewick's *Analytic Combinatorics* is structured in four parts: Part A **Symbolic Methods** (unlabelled OGFs, labelled EGFs, multivariate MGFs), Part B **Complex Asymptotics**, Part C **Random Structures**, Part D **Appendices**.[^1] This page covers **Part A, Chapter I** (`Combinatorial Structures and Ordinary Generating Functions`, pp. 15-94) — the seven sections that build the OGF half of the *symbolic method*: symbolic enumeration (§I.1), admissible constructions and specifications (§I.2), integer compositions and partitions (§I.3), words and regular languages (§I.4), tree structures (§I.5), additional constructions (§I.6), and a perspective closer (§I.7).[^2]

The chapter generalizes the generating-function method of [[aocp-generating-functions](pages/aocp-generating-functions.md)] (Knuth's Fibonacci-method, recurrence ⇒ rational GF) and [[generating-functions-topic](pages/generating-functions-topic.md)] (Sedgewick / Trotter, worked examples with an explicit Project Euler 502 (PE 502) section) from **"recurrences yield rational GFs"** to **"specifications yield GFs by a mechanical dictionary."** The dictionary (Theorem I.1 p.27, summary Figure I.18 p.93) is the [[symbolic-method](pages/symbolic-method.md)]: six admissible constructions — disjoint union `+`, cartesian product `×`, sequence `SEQ`, powerset `PSET`, multiset `MSET`, cycle `CYC` — each with a mechanical OGF translation.[^3] The recurrence route is one case of it (regular languages → rational GFs, Prop. I.2 p.52).[^4]

Two connections to the castle:

- **Stack polyominoes are constructed here by the symbolic method** (Example I.8, pp. 45-46), giving the direct OGF `S(z) = ∑_{k≥1} z^k/(1−z^k) · 1/((1−z)(1−z²)···(1−z^{k−1}))²` from the decomposition `P^{1..k−1} × Z^k × P^{1..k}`: a first column of maximal height `k`, with a partition into parts `≤ k−1` before it and a partition into parts `≤ k` after it.[^5] A stack polyomino — a composition whose parts first weakly rise then weakly fall — is the shape of a [[convex-castle](pages/convex-castle.md)] (a unimodal skyline on a full base), so this Example constructs a castle sub-family by the symbolic method. See [[stack-polyomino-gf](pages/stack-polyomino-gf.md)].
- **Catalan / Dyck / general trees are the canonical recursive example.** The specification `G = Z × SEQ(G)` gives `G(z) = z/(1−G(z))` and, after solving the quadratic, the Catalan generating function `(1−√(1−4z))/2` = `∑ (1/n)C(2n−2,n−1) z^n`, also on [[catalan-numbers](pages/catalan-numbers.md)] and [[dyck-words](pages/dyck-words.md)], derived here in one line from the tree specification.[^6] The castle's own [[generalized-dyck-grammar](pages/generalized-dyck-grammar.md)] is a first-return grammar in this style, with a third letter.

The chapter also covers operations used elsewhere on the wiki: compositions of integers with restricted / bounded summands (§I.3.1, e.g. `SEQ(SEQ_{1..r}(Z))` giving the Fibonacci-like `(1−z)/(1−2z+z^{r+1})` for parts ≤ r), regular-language OGFs and rational-generating-function equivalence (§I.4.2), and the neutral/atomic-class primitives (`ε`, `Z`) that ground the whole apparatus.

## Key Takeaways

- **The symbolic method** (Theorem I.1 p.27, summary Figure I.18 p.93) — six admissible constructions with mechanical OGF translations: `+ → A+B`, `× → A·B`, `SEQ → 1/(1−B)`, `PSET → exp(∑_k (−1)^{k−1} B(z^k)/k)`, `MSET → exp(∑_k B(z^k)/k)`, `CYC → ∑_k φ(k)/k · log(1/(1−B(z^k)))`.[^3] This is the *general* result for which "linear recurrence ⇒ rational GF" is the SEQ-only special case.
- **Stack polyominoes**, Example I.8 (pp. 45-46): the OGF `S(z) = ∑_{k≥1} z^k/(1−z^k) · 1/((1−z)(1−z²)···(1−z^{k−1}))²` (EIS A001523), read off directly from the decomposition `P^{1..k−1} × Z^k × P^{1..k}` (a first tallest column with a partition on each side), the companion in the same Example of the Durfee-square decomposition `P ≅ ⋃_{h≥0}(Z^{h²} × P^{(≤h)} × P^{1..h})` of partitions. Stack polyominoes are the convex castles.[^5]
- **Catalan trees and triangulations** are canonical recursive specifications (§I.2, p. 34-35): `G = Z × SEQ(G)` → `G(z) = (1−√(1−4z))/2`, the [[catalan-numbers](pages/catalan-numbers.md)] generating function.[^6]
- **Regular languages have rational OGFs** (Proposition I.2, p. 52): any *S-regular* language — specifiable by atoms + `+`, `×`, `SEQ` — has a rational OGF.[^7] The compositions-with-bounded-parts, avoidance-of-a-pattern, and bounded-run families of §I.4 are then all rational by construction, as are the castle's tower words at bounded height ([[tower-word-language](pages/tower-word-language.md)], over the [[urd-step-strings](pages/urd-step-strings.md)] alphabet).
- **Integer compositions and partitions** are literal specifications (§I.3): `C = SEQ(I)`, `P = MSET(I)` with `I = SEQ_{≥1}(Z) = z/(1−z)`; the bounded-parts family `C^{1..r} = SEQ(SEQ_{1..r}(Z))` is rational with OGF `(1−z)/(1−2z+z^{r+1})` and generalizes to r-Fibonacci counts.[^8]

## Chapter I structure

The seven sections build the OGF machinery in this order (page numbers are book pages):[^2]

1. **§I.1 Symbolic enumeration methods** (p. 16) — combinatorial class = size-graded (finite / denumerable) set; OGF as `A(z) = ∑ A_n z^n = ∑_{α∈A} z^{|α|}`; the disjoint-union / cartesian-product admissibility examples.
2. **§I.2 Admissible constructions and specifications** (p. 24) — the full six-construction dictionary (Theorem I.1 p.27); iterative vs. recursive specifications; the [[symbolic-method](pages/symbolic-method.md)] as a specification language for combinatorial classes.
3. **§I.3 Integer compositions and partitions** (p. 39) — `C = SEQ(I)`, `P = MSET(I)`; restricted / bounded families; the Durfee-square / **stack polyomino** Example I.8.
4. **§I.4 Words and regular languages** (p. 49) — `W = SEQ(A)`; regular specifications; Prop. I.2 (regular ⇒ rational).
5. **§I.5 Tree structures** (p. 64) — general trees `G = Z × SEQ(G)` → Catalan.
6. **§I.6 Additional constructions** (p. 83) — pointing (`Θ`) and substitution (`B ∘ C`).
7. **§I.7 Perspective** (p. 92) — the chapter's own map (Figure I.18 dictionary, bibliographic notes).

Chapters II (labelled structures / EGFs, pp. 95-150) and III (multivariate GFs / MGFs, pp. 151-220) are the labelled and parameter-tracking companions to this chapter and are not covered here.

## Entities & Concepts

- [[symbolic-method](pages/symbolic-method.md)] — the top-level page for the chapter's thesis; Theorem I.1 dictionary lives here.
- [[stack-polyomino-gf](pages/stack-polyomino-gf.md)] — Example I.8, direct polyomino tie-in.
- [[generating-functions](pages/generating-functions.md)] — the concept page; the recurrence-⇒-rational-GF framing sits inside the symbolic-method framing of this chapter.
- [[generating-functions-topic](pages/generating-functions-topic.md)] — the third GF source; complementary to this one (Sedgewick / Trotter worked-example flavor) and to [[aocp-generating-functions](pages/aocp-generating-functions.md)] (Knuth Fibonacci-method flavor).
- [[polyominoes](pages/polyominoes.md)] / [[column-convex-polyomino](pages/column-convex-polyomino.md)] — the polyomino families around the stacks, which are the convex castles.
- [[catalan-numbers](pages/catalan-numbers.md)] / [[dyck-words](pages/dyck-words.md)] / [[lattice-paths](pages/lattice-paths.md)] — canonical objects the chapter constructs by specification.
- [[generalized-dyck-grammar](pages/generalized-dyck-grammar.md)] — the castle's grammar, a first-return specification in this style.
- [[tower-word-language](pages/tower-word-language.md)] — the castle's tower words, a regular language at bounded height, rational by Prop. I.2.

## Relation to Other Wiki Pages

This is the most general of the wiki's three GF sources, with [[aocp-generating-functions](pages/aocp-generating-functions.md)] (Knuth: recurrence ⇒ rational GF; the Fibonacci method) and [[generating-functions-topic](pages/generating-functions-topic.md)] (Sedgewick / Trotter: worked examples including PE 502). Where those two operate at the level of *"you have a recurrence, here is the OGF,"* this one operates at the level of *"you have a combinatorial specification, here is the OGF."* Both prior sources' machinery falls out as the SEQ / rational-language special case of the dictionary here.

The castle-side content is in §I.3 (Example I.8, a symbolic-method construction of the stack polyominoes, which are the convex castles) and §I.5 (recursive tree specifications, the specification style of the [[generalized-dyck-grammar](pages/generalized-dyck-grammar.md)]).

## Footnotes

[^1]: [[analytic-combinatorics-ch1-ogfs](pages/analytic-combinatorics-ch1-ogfs.md)] "Contents" p.iii-v — "Part A. Symbolic Methods 13 ... Part B. Complex Asymptotics 221 ... Part C. Random Structures 609 ... Part D. Appendices 719" with chapters I-III listed under Part A.
[^2]: [[analytic-combinatorics-ch1-ogfs](pages/analytic-combinatorics-ch1-ogfs.md)] Ch. I title page p.15 — "I. Combinatorial Structures and Ordinary Generating Functions ... I.1. Symbolic enumeration methods 16 / I.2. Admissible constructions and specifications 24 / I.3. Integer compositions and partitions 39 / I.4. Words and regular languages 49 / I.5. Tree structures 64 / I.6. Additional constructions 83 / I.7. Perspective 92."
[^3]: [[analytic-combinatorics-ch1-ogfs](pages/analytic-combinatorics-ch1-ogfs.md)] Theorem I.1 p.27 — "The constructions of union, cartesian product, sequence, powerset, multiset, and cycle are all admissible. The associated operators are as follows: Sum: A(z) = B(z) + C(z); Cartesian product: A(z) = B(z) · C(z); Sequence: A(z) = 1/(1−B(z)); Powerset: A(z) = ∏(1+z^n)^{B_n} = exp(∑ (−1)^{k−1}/k · B(z^k)); Multiset: A(z) = ∏(1−z^n)^{−B_n} = exp(∑ (1/k) · B(z^k)); Cycle: A(z) = ∑ (φ(k)/k) log(1/(1−B(z^k)))." Summary reproduced Figure I.18 p.93.
[^4]: [[analytic-combinatorics-ch1-ogfs](pages/analytic-combinatorics-ch1-ogfs.md)] Proposition I.2 p.52 — "Any S-regular language has an OGF that is a rational function. This OGF is obtained from a regular specification of the language by translating each letter into the variable z, disjoint unions into sums, cartesian products into products, and sequences into quasi-inverses, (1−·)^{−1}."
[^5]: [[analytic-combinatorics-ch1-ogfs](pages/analytic-combinatorics-ch1-ogfs.md)] Example I.8 "The Durfee square of partitions and stack polyominoes" pp. 45-46 — "A stack polyomino is the diagram of a composition such that for some j, ℓ, one has 1 ≤ x_1 ≤ x_2 ≤ … ≤ x_j ≥ x_{j+1} ≥ … ≥ x_ℓ ≥ 1. ... translates immediately into the OGF S(z) = ∑_{k≥1} z^k/(1−z^k) · 1/((1−z)(1−z²)···(1−z^{k−1}))² ... a bona fide algorithm for computing the initial values of the number of stack polyominoes (EIS A001523): S(z) = z + 2z² + 4z³ + 8z⁴ + 15z⁵ + 27z⁶ + 47z⁷ + 79z⁸ + ⋯"; sequence 1, 2, 4, 8, 15, 27, 47, 79 confirmed to match Online Encyclopedia of Integer Sequences (OEIS) A001523 during ingest.
[^6]: [[analytic-combinatorics-ch1-ogfs](pages/analytic-combinatorics-ch1-ogfs.md)] §I.2 pp. 33-35 — "The recursive specification of general trees leads to an implicit definition of their OGF, G = Z × SEQ(G) ⟹ G(z) = z/(1−G(z)) ... From this point on, basic algebra does the rest ... G − G² − z = 0 ... G(z) = ½(1 − √(1−4z)) = z + z² + 2z³ + 5z⁴ + 14z⁵ + 42z⁶ + 132z⁷ + 429z⁸ + ⋯ = ∑_{n≥1} (1/n)C(2n−2,n−1) z^n ... general trees are enumerated by Catalan numbers." Values 1, 1, 2, 5, 14, 42, 132, 429 match the standard Catalan sequence.
[^7]: [[analytic-combinatorics-ch1-ogfs](pages/analytic-combinatorics-ch1-ogfs.md)] Proposition I.2 p.52 and Definition I.10 p.51 — "An iterative specification that only involves atoms (e.g., letters of a finite alphabet A) together with combinatorial sums, cartesian products, and sequence constructions is said to be a regular specification. A language L is said to be S-regular ... if there exists a class M described by a regular specification such that L and M are combinatorially isomorphic."
[^8]: [[analytic-combinatorics-ch1-ogfs](pages/analytic-combinatorics-ch1-ogfs.md)] §I.3 pp. 40-42 — "C = SEQ(I) ⟹ C(z) = 1/(1−I(z)) = (1−z)/(1−2z) ... implying C_n = 2^{n−1}, n ≥ 1"; and "compositions all of whose summands lie in the set {1,2,…,r} have generating function C^{1..r}(z) = 1/(1−z−z²−⋯−z^r) = (1−z)/(1−2z+z^{r+1})"; the r=2 case gives Fibonacci `F_{n+1}`.
