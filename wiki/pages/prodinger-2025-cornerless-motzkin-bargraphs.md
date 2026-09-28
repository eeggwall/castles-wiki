---
title: "Cornerless, peakless, valleyless Motzkin paths (regular and skew) and applications to bargraphs (Prodinger, 2025)"
category: Sources
summary: Prodinger counts Motzkin paths and prefixes (meanders) by length z, final height u, and the numbers of UD and DU factors, with the kernel method on a three-layer automaton, then repeats this for skew Motzkin paths (a fourth layer for the left step). For castles, UD and DU are exactly the zero-width block and the touching blocks that the tower word forbids, so the GF interpolates between tower words (A004149) and Motzkin paths (A001006). Its "not in OEIS" open-end sequence 1, 2, 5, 12, 29, 71, 175, … counts the castles whose columns never drop by more than 1, graded by semi-perimeter (bijection verified on the wiki), and the skew returning paths give A082582, the castles by semi-perimeter. In the paper's formulas τ marks UD and σ marks DU.
tags: [paper, source, motzkin, cornerless, peakless, valleyless, meander, prefix, skew-motzkin, kernel-method, automaton, bargraph, generating-functions, oeis]
sources: [prodinger-2025-cornerless-motzkin-bargraphs]
created: 2026-09-27
updated: 2026-09-28
---

# Cornerless, peakless, valleyless Motzkin paths (regular and skew) and applications to bargraphs (Prodinger, 2025)

**Source:** `raw/prodinger-2025-cornerless-motzkin-bargraphs.pdf` (text layer at `raw/prodinger-2025-cornerless-motzkin-bargraphs.txt`, extracted with `pdftotext -layout`; the PDF is git-ignored, the text is tracked). arXiv:2501.13645v1 [math.CO], 23 January 2025.[^1]
**Author:** Helmut Prodinger (Stellenbosch and NITheCS).[^1]
**Date ingested:** 2026-09-27
**Type:** paper (PDF, 12 pp.)

## Summary

The paper picks up Deutsch and Elizalde's bijection between bargraphs and cornerless Motzkin paths ([[deutsch-elizalde-2016-bargraphs-cornerless-motzkin](pages/deutsch-elizalde-2016-bargraphs-cornerless-motzkin.md)]) from the prefix side. Blecher and Knopfmacher studied *prefixes* of bargraphs, meaning walks along a bargraph that may stop anywhere. Prodinger studies prefixes of cornerless Motzkin paths (Motzkin "meanders") instead, and goes one step further. Peaks `UD` and valleys `DU` are allowed, but each is counted by its own variable.[^2] The count is by `(n, j, k, ℓ)`: length, final height, and the two corner counts, with variables `z, u` and the two corner weights.[^3] Setting both corner weights to 0 gives the cornerless world, setting one to 0 gives peakless or valleyless paths, and setting both to 1 gives ordinary Motzkin paths.[^4]

The method is the kernel method on a finite automaton. The states come in three layers by the type of the last step (up, level, down) and are indexed by height. Reading off the last step gives recursions for three families of height-indexed generating functions. Summing them against `u^j` gives a linear system in `F(u), G(u), H(u)` whose common denominator factors as `z(u − r_1)(u − r_2)`. The factor `u − r_2` has no power series expansion at `u = z = 0`, so it must cancel, and that cancellation determines the unknown boundary values `G(0)` and `H(0)`.[^5] The result is an explicit algebraic GF in `z, u` and both corner weights, with a single square root `W`.[^5] Section 3 repeats this for **skew Motzkin paths**, which add a left step `L = (−1, −1)` with `UL` and `LU` forbidden so the path cannot overlap itself. This needs a fourth layer of states.[^6] Asymptotics are not treated. The paper notes that everything is driven by the square-root singularity of `W`.[^7]

The paper prints special cases and names their OEIS entries.[^8]

| specialization | first terms | OEIS (per the paper) |
|---|---|---|
| cornerless, return to 0 | `1, 1, 1, 2, 4, 8, 16, 33, …` | A004149 |
| no `DU` (valleyless), return to 0 | `1, 1, 2, 4, 8, 17, 37, 82, …` | A004148 (shifted) |
| no `UD` (peakless), return to 0 | `1, 1, 1, 2, 4, 8, 17, 37, …` | A004148 |
| no corner forbidden, return to 0 | `1, 1, 2, 4, 9, 21, 51, 127, 323, …` | A001006 |
| no `DU`, open end | `1, 2, 5, 12, 29, 71, 175, 434, 1082, 2709, 6807, …` | "not in [OEIS]" |
| no `UD`, open end | `1, 2, 4, 9, 21, 50, 121, 296, …` | A091964 |
| cornerless, open end | `1, 2, 4, 9, 20, 45, 102, 233, …` | A308435 |
| no corner forbidden, open end | `1, 2, 5, 13, 35, 96, 267, …` | A005773 |
| skew, no corner forbidden, return to 0 | `1, 1, 2, 5, 13, 35, 97, …` | A082582 |

**The corner variables.** In the recursions a down step taken right after an up step picks up `τ`, and an up step taken right after a down step picks up `σ`,[^9] so **`τ` marks `UD` and `σ` marks `DU`**: `UDUD` (two peaks, one valley) contributes `τ²σ` to the length-4 coefficient `4 + τ²σ + 4τ`,[^10] as a brute-force count of the nine Motzkin paths of length 4 by (peaks, valleys) confirms. The table's pattern names follow this convention; A091964 names its row "left factors of peakless Motzkin paths". Peaks and valleys are not symmetric (reversing a path keeps a peak a peak), so peakless and valleyless returning paths are A004148 at offsets one apart. Brute force confirms every row.

## Key Takeaways

- **The corner weights are the castle rules.** A tower word forbids `UD` because it would be a zero-width block and forbids `DU` because it would be two touching blocks ([[tower-word-language](pages/tower-word-language.md)]). The paper's two corner variables therefore count *violations of the castle rules*. At both weights 0 the returning paths are the tower words, A004149 by length ([[tower-word-continued-fraction](pages/tower-word-continued-fraction.md)]), and at both weights 1 the rules are gone and the count is Motzkin.[^8] The GF is a two-parameter family of "castles with relaxed rules", read as words.
- **The "not in OEIS" sequence is a castle count.** Castles whose columns never drop by more than one level (any first and last column), counted by semi-perimeter `s = w + #blocks`, are `1, 2, 5, 12, 29, 71, 175, 434, 1082, 2709, 6807, …` for `s = 2, 3, …`. These equal the valleyless meanders of length `s − 2`, which is the paper's "not in [OEIS]" row (checked to 24 terms). The bijection and the refinement it carries are on [[motzkin-castles](pages/motzkin-castles.md)] §7. An oeis.org search on 2026-09-27 finds no match.
- **Skew Motzkin paths are counted by the castle numbers.** With both corner weights 1, skew Motzkin paths returning to the axis give A082582,[^11] the castles by semi-perimeter ([[castle-perimeter](pages/castle-perimeter.md)]): skew paths of length `n` and castles of semi-perimeter `n + 1` (brute-force check to `n = 10`). The corner-refined skew GF is explicit, but no castle-to-skew-path bijection is known. With both weights 0 (cornerless skew paths) the returning counts are `1, 1, 1, 3, 7, 17, 41, 103, 259, …`, the constant terms of the paper's returning skew series, continued by brute force as `661, 1701`.
- **The kernel method as a castle tool.** The automaton is a transfer matrix in the height, with the last step as a hidden state. That is the wiki's castle-strip picture ([[castle-strip](pages/castle-strip.md)]) with a catalytic variable `u` for the unbounded height, solved by cancelling the bad root. The PE 502 block sign would enter the same template as one more weight (not done).
- **Cited works (not read).** Blecher and Knopfmacher's *Prefixes of bargraph paths* (2024) is the bargraph analogue. Prodinger's bounded-height papers, *Motzkin paths of bounded height with two forbidden contiguous subwords* (2023) and *Peakless Motzkin paths of bounded height* (2025), treat bounded-height tower words. His survey *A walk in my lattice path garden* (2023) catalogues the automaton method, and Roitner's 2020 thesis has the earlier work on the two forbidden factors.[^12]

## Entities & Concepts

- [[motzkin-castles](pages/motzkin-castles.md)] - the hub; this paper supplies the valleyless-meander reading (§7) and the skew-path GF.
- [[deutsch-elizalde-2016-bargraphs-cornerless-motzkin](pages/deutsch-elizalde-2016-bargraphs-cornerless-motzkin.md)] - the bijection this paper starts from (its ref. [3]).
- [[tower-word-language](pages/tower-word-language.md)] / [[tower-word-continued-fraction](pages/tower-word-continued-fraction.md)] - the cornerless returning paths, A004149.
- [[castle-perimeter](pages/castle-perimeter.md)] - A082582, now also the skew Motzkin count.
- [[castle-strip](pages/castle-strip.md)] - the transfer-matrix picture the automaton generalizes.
- [[motzkin-numbers](pages/motzkin-numbers.md)] - the both-weights-1 specialization.

## Relation to Other Wiki Pages

Every specialization the paper prints agrees with the wiki's counts. It adds three things: a closed-form GF for relaxed tower words with both corners counted, the valleyless-meander count that is also a castle family, and an explicit GF for skew Motzkin paths, the second object counted by A082582. The bounded-height sequels it cites relate to the wiki's own bounded-height tower count `(k+1)^L` ([[castle-counting-formula](pages/castle-counting-formula.md)]), which grades by width rather than by length.

## Footnotes

[^1]: [[prodinger-2025-cornerless-motzkin-bargraphs](pages/prodinger-2025-cornerless-motzkin-bargraphs.md)] p.1 title block L1-8 - "CORNERLESS, PEAKLESS, VALLEYLESS MOTZKIN PATHS (REGULAR AND SKEW) AND APPLICATIONS TO BAR GRAPHS", "arXiv:2501.13645v1 [math.CO] 23 Jan 2025", "HELMUT PRODINGER"; affiliation L484-486.
[^2]: [[prodinger-2025-cornerless-motzkin-bargraphs](pages/prodinger-2025-cornerless-motzkin-bargraphs.md)] p.4 §1 L141-156 [synthesis] - Blecher and Knopfmacher "analyze the progress of walking along a bargraph, but being allowed to stop anywhere"; "we consider the equivalend concept of cornerless Motzkin paths"; peaks `UD` and valleys `DU` are allowed and each is counted by its own variable.
[^3]: [[prodinger-2025-cornerless-motzkin-bargraphs](pages/prodinger-2025-cornerless-motzkin-bargraphs.md)] p.4 §1 L155-160 - "(n, j, k, ℓ) where n is the number of steps of the prefix of a Motzkin path, j is the height of the end point, k is the number of of UD's and ℓ is the number of DU's", with variables "z, u, σ, τ".
[^4]: [[prodinger-2025-cornerless-motzkin-bargraphs](pages/prodinger-2025-cornerless-motzkin-bargraphs.md)] p.3 §1 L117-120 - "if both variables are zero, we are in the cornerless world, and if σ = τ = 1, we have ordinary Motzkin paths."
[^5]: [[prodinger-2025-cornerless-motzkin-bargraphs](pages/prodinger-2025-cornerless-motzkin-bargraphs.md)] pp.4-6 §2 L164-260 [synthesis] - three layers of states with GFs `f_j, g_j, h_j`, recursions from the last step, summed into `F(u), G(u), H(u)`; the square root `W`, the denominator `z(u − r_1)(u − r_2)`, and "The factor u − r_2 can be divided out (this is the 'bad' factor ...)", footnote: "1/(u − r_2) has no power series expansion around u = z = 0"; then "one can set u = 0 and compute G(0) and H(0)".
[^6]: [[prodinger-2025-cornerless-motzkin-bargraphs](pages/prodinger-2025-cornerless-motzkin-bargraphs.md)] pp.2, 9 L71-76, L351-376 [synthesis] - skew Dyck paths add "a third step L = (−1, −1)" with "UL and LU" forbidden, lifted to skew Motzkin paths; §3 adds "a fourth layer" `k_j, K(u)` and the four-equation system.
[^7]: [[prodinger-2025-cornerless-motzkin-bargraphs](pages/prodinger-2025-cornerless-motzkin-bargraphs.md)] p.11 §4 L456-460 - "Asymptotic questions are not addressed in this paper" and "everything is driven by square-root singularities".
[^8]: [[prodinger-2025-cornerless-motzkin-bargraphs](pages/prodinger-2025-cornerless-motzkin-bargraphs.md)] pp.7-8 §2 L284-328 [synthesis] - the returning and open-end specializations and their sequences: A004148 (L301-310), A004149 (L311-315), A001006 (L316-320), the open-end row "not in [10]" (L321-322), A091964 (L323-324), A308435 (L325-326), A005773 (L327-328).
[^9]: [[prodinger-2025-cornerless-motzkin-bargraphs](pages/prodinger-2025-cornerless-motzkin-bargraphs.md)] p.5 §2 L200-205 - "f_{i+1} = zf_i + zg_i + σzh_i" and "h_i = τzf_{i+1} + zg_{i+1} + zh_{i+1}", where `f`, `g`, `h` are the states entered by an up, level and down step.
[^10]: [[prodinger-2025-cornerless-motzkin-bargraphs](pages/prodinger-2025-cornerless-motzkin-bargraphs.md)] p.7 §2 L284-285 - the return-to-axis series "1 + z + (1 + τ)z^2 + 2(1 + τ)z^3 + (4 + τ^2σ + 4τ)z^4 + · · ·".
[^11]: [[prodinger-2025-cornerless-motzkin-bargraphs](pages/prodinger-2025-cornerless-motzkin-bargraphs.md)] p.11 §3 L443-454 [synthesis] - the returning skew series "1 + z + (τ + 1)z^2 + (3 + 2τ)z^3 + (τ^2σ + 7 + 5τ)z^4 + · · ·" and "For σ = τ = 1, we obtain sequence A082582"; at `σ = τ = 1` the returning series is `1, 1, 2, 5, 13, 35, …`, A082582.
[^12]: [[prodinger-2025-cornerless-motzkin-bargraphs](pages/prodinger-2025-cornerless-motzkin-bargraphs.md)] References L465-479 - "[2] Aubrey Blecher and Arnold Knopfmacher. Prefixes of bargraph paths. Aequationes Math., 98(4):1133–1149, 2024", "[6] ... Motzkin paths of bounded height with two forbidden contiguous subwords of length two, 2023", "[7] ... A walk in my lattice path garden. Sém. Lothar. Combin., 87B", "[8] ... Peakless Motzkin paths of bounded height. BICA, page to appear, 2025", "[9] Valerie Roitner. Studies on several parameters in lattice paths. PhD thesis".
