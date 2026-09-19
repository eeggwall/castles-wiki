---
title: "A Characterization of Unique Tournaments (Tetali, 1998)"
category: Sources
summary: Tetali's three-page JCTB note proving that the score-uniquely-determined tournaments have exactly four strong-and-unique building blocks (score vectors (0), (1,1,1), (1,1,2,2), (2,2,2,2,2) on 1, 3, 4, 5 vertices) and that every unique tournament decomposes into these via strong-component decomposition; yields the recurrence u_n = u_{n-1} + u_{n-3} + u_{n-4} + u_{n-5} for n ≥ 6, growth ≈ 1.685. This is OEIS A000570 and the graph-theoretic side of the three-way tree-castle ↔ composition ↔ unique-tournament bijection.
tags: [source, tournament, unique, score-sequence, jctb, tetali, muller-nesetril-pelant, simple-tournament, oeis, a000570, paper]
sources: [tetali-1998-unique-tournaments]
created: 2026-09-17
updated: 2026-09-19
---

# A Characterization of Unique Tournaments (Tetali, 1998)

**Source:** raw/tetali-1998-unique-tournaments.pdf (also `raw/tetali-1998-unique-tournaments.txt`, plaintext extraction)
**Publication:** Prasad Tetali, "A Characterization of Unique Tournaments," Journal of Combinatorial Theory Series B, Volume 72, Issue 1 (January 1998), Pages 157-159. DOI: `10.1006/jctb.1997.1799`.
**Received:** September 20, 1995.[^1]
**Date ingested:** 2026-09-17
**Type:** paper (three-page note)

## Summary

Tetali's note gives a *complete* classification of the tournaments determined uniquely by their score vectors, and it deduces from that classification the recurrence and enumeration listed by Online Encyclopedia of Integer Sequences (OEIS) as A000570.[^2] The set `Unique` is defined as `∪_{n ≥ 1} U_n`, where `U_n = {T_n : S(T_n) = S(T'_n) ⇒ T_n ≅ T'_n}` and `S(T_n)` is the sorted out-degree vector.[^3] Tetali's main result (Theorem 1) says there are **exactly four "basic" strong tournaments** in `Unique`, and every other member decomposes into them:[^4]

**Theorem 1 (Tetali 1998).** There are exactly four basic strong tournaments in `Unique`. Their score vectors are `(0)`, `(1, 1, 1)`, `(1, 1, 2, 2)`, and `(2, 2, 2, 2, 2)`, on 1, 3, 4, and 5 vertices. Any other (non-strong) tournament in `Unique` decomposes into strong components, each of which is one of the four basic tournaments.

The proof reduces to two earlier results of Muller, Nešetřil, and Pelant (1975).[^5] A tournament is *simple* if for every proper vertex subset `M` there is an outside vertex that both beats and is beaten by vertices in `M`;[^6] a score vector is *forcibly simple* (FS) if every tournament realizing it is simple.[^7] Muller et al. proved (i) that every strong-tournament score vector on `n ≠ 4` vertices has a simple realizer, and (ii) that the FS score vectors are exactly the five `{(0), (0, 1), (1, 1, 1), (2, 2, 2, 2, 2), (3, 3, 3, 3, 3, 3, 3)}`.[^8] Combining these, Tetali argues:[^9]

- for `n ≠ 4`, a strong-and-unique tournament's score is (necessarily) forcibly simple;
- among the five FS score vectors, `(0, 1)` is not strong and `(3, 3, 3, 3, 3, 3, 3)` has three non-isomorphic strong realizers so is not unique - leaving `(0)`, `(1, 1, 1)`, `(2, 2, 2, 2, 2)`;
- the `n = 4` exception is `(1, 1, 2, 2)` (the unique strong tournament on 4 vertices), verified by inspection;
- for non-strong unique tournaments, the strong components are themselves in `Unique` (easy), so the strong-component decomposition uses only the four basic tournaments.

From the four basic sizes `{1, 3, 4, 5}` and the strong-component decomposition Tetali reads off the enumeration and the recurrence: `u_1 = 1, u_2 = 1, u_3 = 2, u_4 = 4, u_5 = 7`, and for all `n ≥ 6`,[^10]

```
u_n = u_{n-1} + u_{n-3} + u_{n-4} + u_{n-5},
```

with `u_n · c · α^n → 1` for constants `c ≈ 0.48` and `α ≈ 1.685` (the dominant root of `x^5 = x^4 + x^2 + x + 1`).[^11]

**Why this matters here.** The identity is what `A000570` records - and Tetali's proof, from 1998, predates OEIS's "empirical" label on Schoenfield's 2006 recurrence and Dale's 2011 generating function on that entry by many years.[^12] The three-way bijection tree castle ↔ composition of `{1, 3, 4, 5}` parts ↔ unique tournament developed on [[tree-castle-by-area](pages/tree-castle-by-area.md)] is *exactly* Tetali's strong-component decomposition read across a transfer matrix: the composition parts are the strong-component sizes and each part carries a unique-realizer basic tournament.

## Key Takeaways

- **Four basic strong-and-unique tournaments** (Tetali 1998, Theorem 1): sizes 1, 3, 4, 5 with score vectors `(0)`, `(1, 1, 1)`, `(1, 1, 2, 2)`, `(2, 2, 2, 2, 2)`. No others.[^4]
- **Every unique tournament decomposes into these** via strong-component decomposition, so `A000570(n) = #{compositions of n with parts in {1, 3, 4, 5}}`.[^4]
- **Proof strategy** is not compositional in the modern sense - Tetali reduces to Muller-Nešetřil-Pelant's 1975 characterization of forcibly simple score vectors.[^5]
- **The size-4 exception**: Theorem 2 (Muller et al.) works for `n ≠ 4`; at `n = 4` the strong tournament exists but is not simple, so it is handled by direct inspection.[^13]
- **The size-7 near-miss**: the regular tournament score `(3, 3, 3, 3, 3, 3, 3)` is forcibly simple but not unique - three non-isomorphic strong realizers. This is Tetali's explicit example of why the strong-and-unique series stops at size 5.[^14]
- **Growth constant `α ≈ 1.685`** is the dominant root of `x^5 = x^4 + x^2 + x + 1`, distinct from the metallic and plastic families.[^11]
- **References cited by Tetali**: Douglas 1970 (Hamiltonian tournaments), Garey 1972 (single-Hamiltonian tournaments count `F_{2n−6}`, cited as analogous), Moon 1968 (*Topics on Tournaments*), Muller-Nešetřil-Pelant 1975 (simple/forcibly-simple), Reid-Beineke 1978 (tournament survey).[^15]

## Entities & Concepts

- [[unique-tournament](pages/unique-tournament.md)] - the class `Unique` defined by score-vector-uniqueness up to isomorphism; enumerated by A000570.
- [[simple-tournament](pages/simple-tournament.md)] - Muller-Nešetřil-Pelant condition; strictly stronger than "strongly connected" (fails at `n = 4`).
- [[forcibly-simple-score-vector](pages/forcibly-simple-score-vector.md)] - a score vector every realizer of which is simple; Muller et al. classified these exactly.
- [[tree-castle-by-area](pages/tree-castle-by-area.md)] - our three-way bijection tree castle ↔ composition of `{1, 3, 4, 5}` parts ↔ unique tournament, whose graph-theoretic arrow is now theorem, not conjecture.
- [[oeis-index](pages/oeis-index.md)] - A000570's authoritative source for the recurrence is this paper, not the OEIS "empirical" formula tag.
- [[castle-graph](pages/castle-graph.md)] - tree castles of height 4 by area are exactly A000570-counted, via this classification.
- [[hardin-word-identity](pages/hardin-word-identity.md)] / [[tower-parity-sectors](pages/tower-parity-sectors.md)] - siblings on the wiki that also count objects with the same 4-block decomposition (bit-strings with no run of 5 ones).

## Relation to Other Wiki Pages

The classification here is the "primary source" that the wiki has been citing as *Tetali 1998* on [[tree-castle-by-area](pages/tree-castle-by-area.md)]. Ingesting the paper resolves three loose ends:

1. **The OEIS "empirical" tags are historical, not mathematical.** Schoenfield's 2006 recurrence and Dale's 2011 generating function on A000570 are labeled "empirical" on OEIS, but Tetali proved the same recurrence in 1998 as a consequence of Theorem 1.[^10] The wiki should present the identity `A000570(n) = comp(n, {1, 3, 4, 5})` as a theorem citing Tetali, not as an empirically-observed pattern with a separate proof from the tree-castle side.
2. **The 4-basic-tournaments claim is now a first-source quote**, not a claim relayed through Khovanova 2007 or Repine-Yang 2020. Both stay useful - Khovanova gives an accessible full-text and an independent binary-string bijection, and Repine-Yang give a modern reworking - but the primary is Tetali.
3. **The proof strategy differs from the wiki's presentation.** Our page proved the composition-of-`{1, 3, 4, 5}` identity by exhibiting explicit bijections and by direct enumeration; Tetali proves it by reducing to Muller-Nešetřil-Pelant's classification of *forcibly simple* score vectors. Both are valid; the wiki records both to keep the graph-theoretic and the transfer-matrix routes in one place.

## Footnotes

[^1]: [[tetali-1998-unique-tournaments](pages/tetali-1998-unique-tournaments.md)] p.157 L10 — "Received September 20, 1995."

[^2]: [[tetali-1998-unique-tournaments](pages/tetali-1998-unique-tournaments.md)] p.157 L11-13 [synthesis] — "We call a tournament unique, if there is no other tournament (barring isomorphic ones) which shares the same score vector. In this note, we provide a simple characterization of such unique tournaments."

[^3]: [[tetali-1998-unique-tournaments](pages/tetali-1998-unique-tournaments.md)] p.157 L27-29 — "let `T_n ≅ T'_n` denote the fact that `T_n` is isomorphic to `T'_n`. Let `U_n = {T_n : S(T_n) = S(T'_n) ⇒ T_n ≅ T'_n}`. We define `Unique = ∪_{n ≥ 1} U_n`."

[^4]: [[tetali-1998-unique-tournaments](pages/tetali-1998-unique-tournaments.md)] p.157 L39-41 — "Theorem 1. There are exactly four (basic) strong tournaments in Unique (see Fig. 1); any other (nonstrong) tournament in Unique can be decomposed into strong components, each of which is one of the four basic tournaments." Figure 1 (p.158) shows the four with score vectors `(0)`, `(1, 1, 1)`, `(1, 1, 2, 2)`, `(2, 2, 2, 2, 2)` (transcribed from `raw/tetali-1998-unique-tournaments.txt` L47).

[^5]: [[tetali-1998-unique-tournaments](pages/tetali-1998-unique-tournaments.md)] p.158 L58-59, L70-71 — "We make use of two existing results (Theorem 2 and Theorem 3 below) to prove the above theorem" and "Muller et al. [4] prove, inter alia, the following interesting theorems." Reference [4] is V. Muller, J. Nešetřil, J. Pelant, "Either tournaments or algebras?" Discrete Math. 11 (1975), 37-66.

[^6]: [[tetali-1998-unique-tournaments](pages/tetali-1998-unique-tournaments.md)] p.158 L63-65 — "Definition 1. `T_n` is simple if, for any proper subset `M` of `V(T_n)`, there exists a `z ∈ V(T_n) ∖ M` such that `z` beats at least one vertex in `M` and `z` is beaten by at least one vertex in `M`."

[^7]: [[tetali-1998-unique-tournaments](pages/tetali-1998-unique-tournaments.md)] p.158 L68-69 — "Definition 2. We call a score vector `S` forcibly simple (FS) if every tournament with the score vector `S` is simple."

[^8]: [[tetali-1998-unique-tournaments](pages/tetali-1998-unique-tournaments.md)] p.158 L72-74, L75-82 — "Theorem 2 (Muller et al.). For each score vector `S_n` which corresponds to a strong tournament on `n ≠ 4` vertices, there is a simple tournament which has the same score vector." and "Theorem 3 (Muller et al.). ... `S` is forcibly simple; ... `S ∈ {(0), (0, 1), (1, 1, 1), (2, 2, 2, 2, 2), (3, 3, 3, 3, 3, 3, 3)}`."

[^9]: [[tetali-1998-unique-tournaments](pages/tetali-1998-unique-tournaments.md)] p.158-159 L84-110 [synthesis] — the proof of Theorem 1 in full. The four bullets in the Summary paraphrase Tetali's proof steps.

[^10]: [[tetali-1998-unique-tournaments](pages/tetali-1998-unique-tournaments.md)] p.157 L33-34 — "u_1 = 1, u_2 = 1, u_3 = 2, u_4 = 4, and u_5 = 7, and for all n > 5, u_n = u_{n−1} + u_{n−3} + u_{n−4} + u_{n−5}"; also stated in the Remark, p.159 L111-113.

[^11]: [[tetali-1998-unique-tournaments](pages/tetali-1998-unique-tournaments.md)] p.159 L114-115 — "there exist constants c ≈ 0.48 and α ≈ 1.685 such that `lim_{n → ∞} u_n · c · α^n = 1`." The characteristic polynomial `x^5 − x^4 − x^2 − x − 1 = 0` follows from the recurrence.

[^12]: OEIS A000570 (https://oeis.org/A000570, fetched 2026-09-17) — "Formula" section lists "a(n) = a(n-5) + a(n-4) + a(n-3) + a(n-1). - Jon E. Schoenfield, Aug 07 2006" and "G.f.: (1+x^2+x^3+x^4)/(1-x-x^3-x^4-x^5). - Harvey P. Dale, May 05 2011"; both are listed as user contributions without citing Tetali 1998 (though Tetali is the sequence's original author).

[^13]: [[tetali-1998-unique-tournaments](pages/tetali-1998-unique-tournaments.md)] p.158 L66-67 — "A simple tournament is clearly strong, but the converse is not necessarily true - the strong tournament on four vertices, for example, is not simple." Also p.159 L104-107 — "The only case not covered by the above is the unique strong tournament on four vertices with the score vector (1, 1, 2, 2). Thus the only strong tournaments which are in Unique are the four tournaments shown in Fig. 1."

[^14]: [[tetali-1998-unique-tournaments](pages/tetali-1998-unique-tournaments.md)] p.159 L99-103 — "it is easy to check that there are three nonisomorphic strong tournaments which have the score vector (3, 3, 3, 3, 3, 3, 3). (Note that this among other things gives us that there are no strong tournaments on six or more vertices which belong to Unique.)"

[^15]: [[tetali-1998-unique-tournaments](pages/tetali-1998-unique-tournaments.md)] p.159 L127-138 — references list.
