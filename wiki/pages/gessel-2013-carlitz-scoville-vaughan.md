---
title: "Gessel (2013) - The Carlitz-Scoville-Vaughan theorem and its generalizations"
category: Sources
summary: Ira M. Gessel's talk at the 2013 Joint Mathematics Meetings on the Carlitz-Scoville-Vaughan theorem. For a relation R on an alphabet, the sum of the words in which every neighboring pair is in R is the inverse of the alternating sum of the words in which every neighboring pair is outside R, in noncommuting variables. Three proofs - a sign-reversing pairing, inclusion-exclusion over the R-descents, and transfer matrices - and applications to words counted by R-runs and by run lengths along the walks of a digraph, to permutations by descents through z^n/n!, to Parker's and Drake's tree versions for compositional inverses, and to the Goulden-Jackson cluster theorem for longer forbidden words. In castle terms the letters are heights, R is a strip rule M and the complement is the dual rule J − M, so the theorem is the Hilbert duality G_M(x) G_{J−M}(−x) = 1 of the Hilbert castles; Gessel's first example, words with no two neighboring x, is the tree skylines of height at most 2.
tags: [source, slides, carlitz-scoville-vaughan, inclusion-exclusion, noncommutative-generating-functions, strip-rule, hilbert-castle, transfer-matrix, goulden-jackson, fibonacci]
sources: [gessel-2013-carlitz-scoville-vaughan]
created: 2026-10-28
updated: 2026-10-28
---

# Gessel (2013) - The Carlitz-Scoville-Vaughan theorem and its generalizations

**Source:** `raw/gessel-2013-carlitz-scoville-vaughan.pdf` (text layer at `raw/gessel-2013-carlitz-scoville-vaughan.txt`, extracted with `pdftotext -layout`; the PDF is git-ignored, the text is tracked). I. M. Gessel, "The Carlitz-Scoville-Vaughan Theorem and its Generalizations", slides, Joint Mathematics Meetings, San Diego, January 12, 2013, https://people.brandeis.edu/~gessel/homepage/slides/csv.pdf.[^1] The slides are built with overlays, so the text layer repeats a slide each time a line is added to it.
**Date ingested:** 2026-10-28
**Type:** slides (PDF)

## Notation used on this page

The wiki writes `M` for a strip rule, a 0/1 matrix on the heights `1, …, h`, `J − M` for its dual rule, which allows exactly the pairs that `M` forbids, and `G_M(x)` for the strip series with the empty strip included ([[hilbert-castles](pages/hilbert-castles.md)]). The slides' symbols are kept on this page. The text layer drops the bars over `R̄`, so some quotes in the footnotes read `R` where the slide has `R̄`.

| slides | meaning | castle reading |
|---|---|---|
| `A`, `A*` | an alphabet, the words over it | the heights `1, …, h`, the skylines |
| `R ⊆ A²`, `R̄ = A² − R` | a relation on the letters and its complement | a strip rule `M` and its dual rule `J − M` |
| `A(R)` | the words `a_1 ⋯ a_n` with `a_1 R a_2 R ⋯ R a_n`, the empty word and the single letters included | the strips of `M` |
| `l(w)` | the length of a word | the width of a skyline |
| R-descent | a position `i` with `a_i R̄ a_{i+1}` | a position whose pair `M` forbids |
| R-run | a maximal nonempty factor in `A(R)` | a maximal strip of `M` inside a skyline |
| `h_n^(R)` | the sum of the words of length `n` in `A(R)` | the strips of width `n`, as a sum of words |

## Summary

**The theorem.** Gessel recounts that in their 1976 paper *Enumeration of pairs of sequences by rises, falls and levels* Carlitz, Scoville and Vaughan count pairs of integer sequences by the nine joint specifications `RR, …, LL` of rises, falls and levels, and one of their results says that for a partition `{A, B}` of the specifications, the generating function of the sequences with every specification in `A` is the reciprocal of the alternating generating function of those with every specification in `B`; the paper's appendix proves a more general version.[^2] Gessel states that version as the **Carlitz-Scoville-Vaughan theorem**: for an alphabet `A` and a relation `R ⊆ A²`,

```
Σ_{w ∈ A(R̄)} w  =  ( Σ_{w ∈ A(R)} (−1)^{l(w)} w )^{−1},
```

in the ring of formal power series in noncommuting variables. He writes that he believes it "should be considered one of the fundamental theorems of enumerative combinatorics".[^3]

**Two examples.** With `A = {x, y}` and `R̄ = {xx}`, the words with no two neighboring `x` have the sum `((1 + x)^{−1} − y)^{−1} = (1 + x)(1 − y(1 + x))^{−1}`, which at `y = x` is a generating function of the Fibonacci numbers. With `R = {x_i x_j : i ≤ j}` on `x_1, x_2, …`, the theorem is the identity `Σ_n e_n = (Σ_n (−1)^n h_n)^{−1}` between the noncommutative elementary and complete symmetric functions.[^4]

**Three proofs.** *Proof 1*, essentially the original one, shows that `Σ_{v ∈ A(R)} (−1)^{l(v)} v · Σ_{w ∈ A(R̄)} w = 1`: "Every nonempty word that occurs in this sum appears twice, once with a plus sign and once with a minus sign." *Proof 2* counts the words with a given set of R-descents by inclusion-exclusion from the `h_n^(R)`; the words in which every position is an R-descent then have the sum `(1 − Σ_{n≥1} (−1)^{n−1} h_n^(R))^{−1}`. *Proof 3*, for the commutative version, takes `A` finite, writes both sides as entries of matrices by the transfer-matrix method, and refers to Goulden and Jackson's *Combinatorial Enumeration* for the matrix algebra.[^5]

**Runs.** The R-descents cut a nonempty word into R-runs, one more than the number of R-descents. Applying the theorem on a new alphabet whose letters are the words of `A(R)`, and weighting each R-run, gives `Σ_{w ∈ A*} t^{R-run(w)} w = (1 − t Σ_{n≥1} (1 − t)^{n−1} h_n^(R))^{−1}`, and more generally a weight `t_i` on each run of length `i`; for instance the words whose R-runs all have length 3 sum to `(Σ_k (−1)^k h_{3k}^(R))^{−1}`, and those whose runs all have odd length to `(1 + Σ_k (−1)^k F_k h_k^(R))^{−1}`, with `F_k` the Fibonacci numbers. Run lengths read along the walks of a digraph give the words whose sequence of run lengths lies in a regular language, as entries of the inverse of a matrix of alternating sums of the `h_n^(R)`.[^6]

**Permutations.** With `A = {1, 2, …}` and `R = ≤`, the linear map that sends a permutation of `[n]` to `z^n/n!` and every other word to 0 is a homomorphism on the algebra generated by the `h_n^(R)`, with `h_n^(R) ↦ z^n/n!`. This turns the run formula into the generating function `(1 − t)/(1 − t e^{(1−t)x})` of the Eulerian polynomials, and gives the pairs of permutations with no common ascents.[^7]

**Generalizations.** Gessel's students Susan Parker (1993) and Brian Drake (2008) extended the theorem to trees: the compositional inverse of the generating function of the trees with a given set of links is the alternating generating function of the trees with the complementary set, and the Carlitz-Scoville-Vaughan theorem is the case of unary trees; Drake's version, for exponential generating functions, interprets `(e^x − 1)^{⟨−1⟩} = log(1 + x)`. For forbidden factors of length more than 2 the Goulden-Jackson cluster theorem plays the same role, and the sum of the words avoiding a set of factors is `(Σ_w μ(w) w)^{−1}` with every `μ(w)` in `{0, 1, −1}`.[^8]

## The castle reading

Take the heights `1, …, h` as the alphabet and a strip rule `M` as the relation `R` ([[castle-strip](pages/castle-strip.md)]). Then `A(R)` is the set of strips of `M`, `A(R̄)` the set of strips of the dual rule `J − M`, and sending every letter `a` to a commuting variable `x` turns the theorem into

```
G_{J−M}(x)  =  1 / G_M(−x),
```

the Hilbert duality of [[hilbert-castles](pages/hilbert-castles.md)], whose proof there is Proof 2 in castle terms. Sending the letter `a` to `q^a x` counts by width and area as well. So:

- **The first example is a castle family.** With `x` the height 2 and `y` the height 1, the words with no two neighboring `x` are the tree skylines of height at most 2 of [[castle-graph](pages/castle-graph.md)]: the Fibonacci castles of [[fibonacci-castle](pages/fibonacci-castle.md)] and the flat row `(1, …, 1)`. Gessel's sum at `y = x` is their count by width; with `x ↦ q²x` and `y ↦ qx` it counts them by width and area.
- **Hilbert castles.** The zig-zag rule and the Hilbert rule `|a − b| ≠ 1` are complementary relations, so the Hilbert strips have the series `1/Z_h(−x)`, with `Z_h` the zig-zag strip series ([[hilbert-castles](pages/hilbert-castles.md)], [[zig-zag-castles](pages/zig-zag-castles.md)]).
- **Proof 1 is the Koszul complex.** The pairing that cancels each nonempty word is the boundary of the Koszul complex of a quadratic monomial algebra in [[loday-vallette-2012-algebraic-operads](pages/loday-vallette-2012-algebraic-operads.md)], Theorem 4.3.6: for a skyline cut into a strip of `J − M` followed by a strip of `M`, the admissible cuts come in neighboring pairs.
- **R-runs of a skyline.** The R-runs of a skyline are its maximal strips of `M`, so the run formula counts all skylines by the number of maximal strips of a rule, one more than the number of positions whose pair the rule forbids.
- **Not covered.** The theorem weights letters, so it counts by width and area but not by the Project Euler 502 block count, which weights each neighboring pair by its rise.

The castle reading of the theorem was checked by execution on every rule of height at most 4, and the pairing of Proof 1 on the skylines of width at most 6 under 120 random rules ([[hilbert-castles](pages/hilbert-castles.md)], footnote 1 there).[^exec]

## Key Takeaways

- **A rule and its complement have reciprocal series at `−x`.** The words obeying `R` and the words obeying `R̄` determine each other, in noncommuting variables.[^3]
- **Three proofs.** A sign-reversing pairing, inclusion-exclusion over the R-descents, and transfer matrices.[^5]
- **Runs and regular languages.** Weighting the R-runs extends the theorem to words counted by their runs and to run-length sequences read along a digraph.[^6]

## Entities & Concepts

- [[hilbert-castles](pages/hilbert-castles.md)] - the Hilbert duality of strip rules, proved by inclusion-exclusion, and the Hilbert castles.
- [[castle-strip](pages/castle-strip.md)] - strip rules, the relations `R` of the theorem on the alphabet of heights.
- [[castle-graph](pages/castle-graph.md)], [[fibonacci-castle](pages/fibonacci-castle.md)] - the tree skylines and the Fibonacci castles, the first example of the slides.
- [[generating-functions](pages/generating-functions.md)] - the transfer-matrix route of Proof 3.

## Relation to Other Wiki Pages

[[loday-vallette-2012-algebraic-operads](pages/loday-vallette-2012-algebraic-operads.md)] gives the same identity for quadratic monomial algebras and their Koszul duals, as Hilbert series, with the pairing of Proof 1 as the boundary of the Koszul complex. The Goulden-Jackson cluster theorem of the last slides is the route for rules on more than two neighboring columns.

## Footnotes

[^1]: [[gessel-2013-carlitz-scoville-vaughan](pages/gessel-2013-carlitz-scoville-vaughan.md)] title slide L1-L12 [synthesis] - the title "The Carlitz-Scoville-Vaughan Theorem and its Generalizations", "Ira M. Gessel", "Department of Mathematics, Brandeis University", "Joint Mathematics Meeting, San Diego, January 12, 2013".
[^2]: [[gessel-2013-carlitz-scoville-vaughan](pages/gessel-2013-carlitz-scoville-vaughan.md)] slide "Counting pairs of sequences" L13-L41 [synthesis] - "In their 1976 paper Enumeration of pairs of sequences by rises, falls and levels in Manuscripta Mathematica, Leonard Carlitz, Richard Scoville, and Theresa Vaughan studied pairs of sequences of integers of the same length according to rises, falls and levels."; "Let {A, B} be a partition of {RR, . . . , LL}. Then the reciprocal of the generating function for sequences in which every specification is in A is the generating function, with alternating signs, of the generating function for sequences in which every specification is in B."; "In the appendix to their paper, they proved a more general version of this result, which I will state a little differently."
[^3]: [[gessel-2013-carlitz-scoville-vaughan](pages/gessel-2013-carlitz-scoville-vaughan.md)] slide "The Carlitz-Scoville-Vaughan Theorem" L42-L72 [synthesis] - "Let A be an alphabet, and let R be a relation on A, that is, a subset of A × A = A2. Let A(R) be the set of words a1 · · · an in A∗ such that a1 R a2 R · · · R an. Note that the empty word 1 and all words of length one are in A(R)."; the displayed identity; "Here l(w) is the length of w, and we are working in the ring of formal power series in noncommuting variables."; "Carlitz, Scoville, and Vaughan didn’t do anything more with this result. But I believe that it should be considered one of the fundamental theorems of enumerative combinatorics."
[^4]: [[gessel-2013-carlitz-scoville-vaughan](pages/gessel-2013-carlitz-scoville-vaughan.md)] slides "A simple example" and "Another simple example" L73-L143 [synthesis] - `A = {x, y}` with no consecutive `xx`, `Σ_{w ∈ A(R̄)} (−1)^{l(w)} w = 1 − y − x + x² − x³ + ⋯ = (1 + x)^{−1} − y`, the words of `A(R̄)` being those in which every neighboring pair is `xx`, the sum `((1 + x)^{−1} − y)^{−1} = (1 + x)(1 − y(1 + x))^{−1}`, "Note that if we set y = x, we get a generating function for Fibonacci numbers."; `R = {x_i x_j : i ≤ j}` and the identity of the noncommutative symmetric functions `e_n` and `h_n`.
[^5]: [[gessel-2013-carlitz-scoville-vaughan](pages/gessel-2013-carlitz-scoville-vaughan.md)] slides "Proof of the CSV theorem" to "Proof 3" L144-L200 [synthesis] - "Proof 1. (Essentially the same as Carlitz, Scoville, and Vaughan’s proof.)", "Every nonempty word that occurs in this sum appears twice, once with a plus sign and once with a minus sign."; Proof 2, "Let us define an R-descent ... Then the set of words of length n with a given R-descent set can be expressed by inclusion-exclusion in terms of the h_n^(R)", with the example "the sum of the words of length 5 with R-descent set {3} is h3 h2 − h5" and the sum over the words in which every position is an R-descent; "Proof 3. (At least for the commutative version.) ... The coefficients on both sides can be expressed as matrix entries by the transfer matrix method. Then the result follows by matrix algebra. (See, e.g., Goulden and Jackson’s Combinatorial Enumeration.)".
[^6]: [[gessel-2013-carlitz-scoville-vaughan](pages/gessel-2013-carlitz-scoville-vaughan.md)] slides "An application: counting words by R-runs" and "Walks in digraphs" L201-L367 [synthesis] - "An R-run in a word is a maximal nonempty subword in A(R), so the R-descents break up a word into R-runs. For a nonempty word, the number of R-runs is one more than the number of R-descents."; the run-weighted formula, the weights `t_i` by run length, the runs of length 3 and of odd length with the Fibonacci numbers `F_k`; "In other words, we can count words whose R-run length sequences are in a regular language.", with the two digraph examples as entries of inverse matrices.
[^7]: [[gessel-2013-carlitz-scoville-vaughan](pages/gessel-2013-carlitz-scoville-vaughan.md)] slides "Permutations" L368-L437 [synthesis] - `R = ≤`, the map taking a permutation of `[n]` to `z^n/n!` and other words to 0, a homomorphism on the algebra generated by the `h_n^(R)` with `h_n^(R) ↦ z^n/n!`; the Eulerian polynomials, `(1 − t)/(1 − te^{(1−t)x})`; the pairs of permutations of `[n]` with no common ascents; "By applying other homomorphisms we can count permutations by the number of inversions, descent set, number of descents, major index, or number of peaks of π−1."
[^8]: [[gessel-2013-carlitz-scoville-vaughan](pages/gessel-2013-carlitz-scoville-vaughan.md)] slides "Generalizations" to the last slide L438-L756 [synthesis] - "Two of my students, Susan Parker and Brian Drake, generalized the CSV to give a combinatorial interpretation of the compositional inverse of power series."; "Susan Parker’s Theorem (1993) (Rediscovered by Jean-Louis Loday, 2006)"; "Parker’s Theorem: Given a set of letters, the compositional inverse of the generating function for trees with a given set of links is the generating function for trees with the complementary set of links, with alternating signs."; "The CSV theorem is the special case of Parker's theorem for unary trees."; "Brian Drake’s Theorem (2008) (Rediscovered by Vladimir Dotsenko, 2011)", `(e^x − 1)^{⟨−1⟩} = log(1 + x)`; the Goulden-Jackson cluster theorem and "Theorem. The sum of all words in A∗ that avoid the words in F may be written (Σ_{w∈A∗} µ(w)w)^{−1} where for every word w, µ(w) is 0, 1, or −1.", with the note on Curtis Greene's lattices with Möbius function `±1, 0`.
[^exec]: Verified by execution (Python 3.11 with NumPy and SymPy, 2026-10-28): `bin/python/hilbert_castles.py` items [1] and [8], run log `bin/python/hilbert_castles-run.log`. The commutative identity on all 66,066 rules of heights 1 to 4 and on 900 random rules of heights 5 to 7, by width, and by width and area on the 530 rules of height at most 3; the cuts of every skyline of width 1 to 6 under 120 random rules, none or two neighboring cuts in every case; the tree skylines by width and area from the dual rule.
