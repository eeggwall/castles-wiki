---
title: "Completely deterministic self-organized critical state of sandpile automaton models (Chau-Cheng, 1991)"
category: Sources
summary: Chau and Cheng ask when an abelian sandpile's steady state is completely deterministic, meaning every grain operator acts the same on the recurrent configurations, so the future depends only on how many grains are added and not where. Then the recurrent set is cyclic, Z_{n+1}, described by a single height. Two toppling matrices give the same steady-state dynamics iff they differ by elementary row operations, each class has a "fundamental" representative (−Δ_ij < Δ_jj), and a sandpile is deterministic iff its fundamental rule is the identity or a single dissipating site fed by all others (eq. 13). The one-dimensional BTW sandpile is the trivial case, and the paper compares the property to circle maps. On castles, sandpile-group proves that a castle sandpile is deterministic exactly when its group is trivial, which happens exactly for the tree castles.
tags: [paper, source, sandpile, abelian-sandpile, self-organized-criticality, deterministic, cyclic-group, toppling-matrix, elementary-row-operations, circle-map]
sources: [chau-cheng-1991-deterministic-soc-sandpile]
created: 2026-09-27
updated: 2026-10-16
---

# Completely deterministic self-organized critical state of sandpile automaton models (Chau-Cheng, 1991)

**Source:** text layer `raw/chau-cheng-1991-deterministic-soc-sandpile.txt`, extracted with `pdftotext -layout`; the PDF is not in the repository. The two-column text layer loses the displayed matrices of eq. 13, which were read from the page image of a local copy; the form stated below agrees with eqs. 6-8 and 14 of the text.
**Publication:** H. F. Chau and K. S. Cheng, *Physics Letters A* **157** (1991) 103-106; received 18 March 1991. University of Hong Kong.[^1]
**Date ingested:** 2026-09-27
**Type:** paper (PDF, 4 pp.)

## Summary

The paper works in Dhar's abelian sandpile model (ASM) ([[dhar-1990-self-organized-critical-sandpile](pages/dhar-1990-self-organized-critical-sandpile.md)]). Heights are integers, a site topples when its height exceeds a critical value, and toppling subtracts a row of an integer matrix `Δ` with positive diagonal, non-positive off-diagonal and non-negative row sums.[^2] Chau and Cheng shift the critical heights to 0, so stable heights are `≤ 0`, where Dhar uses `1..Δ_ii` and the wiki `0..deg − 1` ([[castle-notation](pages/castle-notation.md)]).[^2] Following Dhar, the grain operators `a_i` commute, so the set `R` of steady-state (self-organized critical, SOC) configurations can be treated as a finite abelian group.[^3]

Where earlier work studied relaxation times, critical exponents and two-point correlations, the authors look for sandpiles whose steady state is **completely deterministic**: once the system is in `R`, dropping a grain on any site gives the same result, `a_i|_R = a_j|_R` for all `i, j` (eq. 5). The future then depends only on the total number of grains added, and the probability distribution of where grains land no longer matters.[^4] Their first result is that, up to relabeling, `R` is then `{(0, 0, …, 0), (−1, 0, …, 0), …, (−n, 0, …, 0)}` (eq. 6). At most one site can vary, because two distinct sites that accept a grain without toppling would give two different results. So `R ≅ Z_{n+1}`: the system is "one-dimensional", labeled by a single height.[^5] The authors note that the argument does not use the abelian property, so after a slight modification the result holds for any toppling condition, including BTW's local-gradient rule.[^5]

To classify these systems they introduce **equivalent toppling rules**. Two matrices `Δ, Δ′` are equivalent if they have the same `R` and the same grain operators on it (eq. 9). By Dhar's criterion that two configurations are equivalent when they differ by an integer combination of rows of `Δ` (eq. 10), this holds iff one matrix becomes the other by elementary row additions and subtractions.[^6] Row operations can always reach a **fundamental toppling rule**, one with `−Δ_ij < Δ_jj` for `i ≠ j` (eq. 11); `−Δ_ij ≥ Δ_jj` is exactly the condition that site `j` always topples whenever `i` does (eq. 12).[^6]

The main theorem is that an SOC system is completely deterministic iff, after relabeling, its fundamental toppling rule is either the identity matrix or the matrix with `Δ_11 = n` (`n > 1`), `Δ_ii = 1` and `Δ_i1 = −1` for `i ≠ 1`, and zeros elsewhere (eq. 13).[^7] In the second form a site `i ≠ 1` topples at one grain and passes it to site 1, and site 1 topples at one grain and loses `n`, so the recurrent configurations have every other site at 0 and site 1 at `0, −1, …, −(n − 1)`: there are `det Δ = n` of them. The one-dimensional BTW sandpile is the trivial case: its SOC state is a single configuration with every local gradient just below critical, every added grain slides off, and `R` is the trivial group.[^8] The paper closes with circle maps. A family of maps `f(x) = (x + θ) mod 2π` evolves deterministically when all the `θ`s are equal, and the orbit of a point then forms `Z_n` for rational `θ/2π`, as `R` is cyclic here.[^9]

## The castle reading

These consequences are the wiki's, not the paper's.

- **Deterministic castles are the tree castles.** [[sandpile-group](pages/sandpile-group.md)] proves that a castle sandpile, in the sink model or the tide model, is completely deterministic exactly when its group `K = Z^{n_live}/L̃ Z^{n_live}` is trivial, and that the group is trivial exactly when the castle is a tree castle, one with no `2 × 2` block. The first proof uses eq. 5 and Dhar's equivalence: if every grain is the same class `g` of `K`, toppling a cell `v` gives `s(v)·g = 0`, with `s(v)` the number of edges from `v` to the sink, and a cell next to the sink has `s(v) = 1`. Among the castles with 2 to 12 cells, up to mirror image, the tree castles number 769, and 758 of them have height at least 2 and so a tide model (computed).[^10]
- **Any deterministic sandpile.** The same argument applies to any toppling matrix: if every grain is the same class `g`, then `s(v)·g = 0` for every site, where `s(v)` is the row sum of `Δ` at `v`, the number of grains `v` loses. So `|R|` divides every nonzero row sum. In eq. 13 the only nonzero row sum is site 1's, `n`, and `|R| = n`. (This `n` is eq. 13's; in eq. 6, `|R| = n + 1`.)
- **Deterministic is stronger than cyclic.** A deterministic sandpile has a cyclic group, but not conversely: the castle `(2, 2)` has the cyclic group `Z/4` in the sink model and is not a tree castle, so it is not deterministic ([[sandpile-group](pages/sandpile-group.md)], [[sandpile-census](pages/sandpile-census.md)]).
- **Equivalent rules and isomorphic groups.** Equivalent toppling rules have isomorphic groups, but not conversely: the block-matrix presentation on [[sandpile-group](pages/sandpile-group.md)] gives the castle group by a matrix of a different size, which is not row-equivalent to `L̃`.
- **Tree castles.** A tree castle has one spanning tree in both models, so its group is trivial and its steady state is a single configuration, as for the paper's one-dimensional BTW sandpile.

## Entities & Concepts

- [[dhar-1990-self-organized-critical-sandpile](pages/dhar-1990-self-organized-critical-sandpile.md)] - the model, the commuting grain operators, and the equivalence of configurations used here (ref. [3]).
- [[sandpile-group](pages/sandpile-group.md)] - the castle sandpile group in the sink and tide models, with the Propositions that a castle sandpile is completely deterministic exactly when its group is trivial, and that the group is trivial exactly for the tree castles.
- [[sandpile-census](pages/sandpile-census.md)] - the census of castle groups to 16 cells, with the cyclic groups counted in each model.
- [[castle-graph](pages/castle-graph.md)] - the tree castles, castles with no `2 × 2` block.
- [[sandcastle-seminar](pages/sandcastle-seminar.md)] - a seminar on castle sandpiles and their recurrent configurations.

## Relation to Other Wiki Pages

The paper adds a classification (deterministic steady states) and an equivalence relation (row operations) to the sandpile theory the wiki sources to Dhar. Its height convention (stable heights `≤ 0`) differs from Dhar's and the wiki's by a shift, recorded on [[castle-notation](pages/castle-notation.md)]. [[dhar-ruelle-sen-verma-1995-algebraic-aspects](pages/dhar-ruelle-sen-verma-1995-algebraic-aspects.md)] works in the same toppling-matrix formalism.

## Footnotes

[^1]: [[chau-cheng-1991-deterministic-soc-sandpile](pages/chau-cheng-1991-deterministic-soc-sandpile.md)] p.103 title block L6-13 - "Completely deterministic self-organized critical state of sandpile automaton models", "H.F. Chau and K.S. Cheng", "Department of Physics, University of Hong Kong", received 18 March 1991.
[^2]: [[chau-cheng-1991-deterministic-soc-sandpile](pages/chau-cheng-1991-deterministic-soc-sandpile.md)] pp.103-104 L47-85 [synthesis] - sites `1..N` with integer heights; a site topples when `z_i > z_ic`, by `z_j → z_j − Δ_ij` (eq. 1) with `Δ_ii > 0`, `Δ_ij ≤ 0`, `Σ_j Δ_ij ≥ 0` (eqs. 2-4); "we may rescale our system so that the z_ic are all zero".
[^3]: [[chau-cheng-1991-deterministic-soc-sandpile](pages/chau-cheng-1991-deterministic-soc-sandpile.md)] p.104 L86-98 - "As shown by Dhar [3], the operators a_i are Abelian", and "we can regard R as a finite Abelian group".
[^4]: [[chau-cheng-1991-deterministic-soc-sandpile](pages/chau-cheng-1991-deterministic-soc-sandpile.md)] pp.103-104 L46-51, L99-111, L58-61 [synthesis] - earlier studies "mainly focus on the spectra of relaxation times, critical exponents and the two-point correlation functions"; "completely deterministic" means dropping particles at site `i` or `j` gives the same final stable configuration, `a_i|_R = a_j|_R` (eq. 5); the evolution "depends only on the total number of particles added".
[^5]: [[chau-cheng-1991-deterministic-soc-sandpile](pages/chau-cheng-1991-deterministic-soc-sandpile.md)] p.104 L62-111 [synthesis] - `R` has the form of eq. 6 "for some non-negative integer n"; at most one site can differ from zero; "R is isomorphic to the group Z_{n+1}"; "a one-dimensional system"; "our above arguments do not make use of the Abelian properties".
[^6]: [[chau-cheng-1991-deterministic-soc-sandpile](pages/chau-cheng-1991-deterministic-soc-sandpile.md)] p.105 L118-171 [synthesis] - equivalent toppling matrices (eq. 9); Dhar's configuration equivalence (eq. 10); equivalent "if and only if one can transform Δ to Δ′ by elementary row addition and subtraction"; the fundamental rule `−Δ_ij < Δ_jj` (eq. 11); "a site j always topples whenever another site i does if and only if −Δ_ij ≥ Δ_jj" (eq. 12).
[^7]: [[chau-cheng-1991-deterministic-soc-sandpile](pages/chau-cheng-1991-deterministic-soc-sandpile.md)] p.105 L116-148, L173-174 [synthesis] - "a SOC system is completely deterministic if and only if their fundamental toppling rules are, after a suitable reorganization of the site labels, of the form" eq. 13 (the identity matrix, or first row `(n, 0, …)` and rows `(−1, …, 1, …)`), "where n is a positive integer greater than 1"; the proof reduces to `Δ_ii = 1` for `i ≠ 1` (eq. 14).
[^8]: [[chau-cheng-1991-deterministic-soc-sandpile](pages/chau-cheng-1991-deterministic-soc-sandpile.md)] p.105 L160-174 - in BTW's one-dimensional sandpile "the SOC configuration is nothing but a single state where all the local gradients are just below the critical one", so "the SOC state is just isomorphic to the trivial group".
[^9]: [[chau-cheng-1991-deterministic-soc-sandpile](pages/chau-cheng-1991-deterministic-soc-sandpile.md)] p.106 L180-199 [synthesis] - the circle map `f(x) = (x + θ) mod 2π`; a collection of them is completely deterministic when all the `θ`s are equal, and repeated application forms `Z_n` when `θ/2π` is rational.
[^10]: Verified by execution (Python 3.11, 2026-10-16): the castles with 2 to 12 cells and no `2 × 2` block, counted up to mirror image, number 769, and 758 of them have height at least 2; the recurrent configurations of the eq. 13 rule are the `n` configurations with every site but site 1 at 0.
