---
title: "Generalized Narayana arrays, restricted Dyck paths, and related bijections (Baril-Flórez-Ramírez, 2026)"
category: Sources
summary: Baril, Flórez and Ramírez refine the Narayana triangle N(n, k), Dyck paths of semilength n with k peaks, by the heights of the peaks or valleys. Type 1 counts k peaks with heights in a set S, other peaks allowed; type 2 counts k peaks, all with heights in S. For the residue classes A_{3,b} of heights ≡ b (mod 3), the first column of the type-1 array for b = 2 is A082582, the Dyck paths of semilength n avoiding UUDD and, equally, the Dyck paths with no peak at a height ≡ 2 (mod 3), joined by a recursive bijection µ″. A082582 is also the count of castles by semi-perimeter, so for n ≥ 2 the castles of semi-perimeter n, the UUDD-avoiding Dyck paths and the Dyck paths with no peak at a height ≡ 2 (mod 3) of semilength n are equinumerous (checked by brute force). The paper contains no bargraphs and no castle bijection, and none of its arrays is the tower-Narayana identity. Summarized: §§1-2 and §3.1.3; not the S = {m, m+1}, even/odd-height, valley and type-2 sections or the computational appendix.
tags: [paper, source, narayana, dyck-path, peaks, valleys, bijection, generating-functions, bargraph, semiperimeter, oeis, a082582]
sources: [baril-florez-ramirez-2026-generalized-narayana-arrays]
created: 2026-10-09
updated: 2026-10-16
---

# Generalized Narayana arrays, restricted Dyck paths, and related bijections (Baril-Flórez-Ramírez, 2026)

**Source:** `raw/baril-florez-ramirez-2026-generalized-narayana-arrays.pdf` (text layer at `raw/baril-florez-ramirez-2026-generalized-narayana-arrays.txt`, extracted with `pdftotext -layout`; the PDF is git-ignored, the text is tracked). *Australasian Journal of Combinatorics* 94(3) (2026), pp. 333-365, CC BY 4.0, from the journal's download page `ajc.maths.uq.edu.au/download/94/ajc_v94_p333.pdf` (identical to the copy on Baril's homepage). Received 30 April 2025, revised 11 December 2025.[^1]
**Authors:** Jean-Luc Baril (Université Bourgogne Europe), Rigoberto Flórez (The Citadel), José L. Ramírez (Universidad Nacional de Colombia).[^1]
**Date ingested:** 2026-10-09
**Type:** paper (PDF, 33 pp.)

> **Scope.** Summarized here: §1 (introduction), §2 (definitions and the Narayana triangle) and §3.1.3 (peaks at heights in residue classes, with the A082582 column and the bijections µ, µ′, µ″, pp. 341-344). Not summarized: §3.1.1 (`S = {m, m+1}`), §3.1.2 (even or odd heights and 132-avoiding permutations), §4 (valleys), §§5-6 (type-2 arrays) and the computational appendix §7.

## Summary

**The Narayana triangle and its two generalizations.** `N(n, k)`, the number of Dyck paths of semilength `n` with exactly `k` peaks (A001263), is `(1/k) C(n−1, k−1) C(n, k−1)` for `n, k ≥ 1`. A peak is a factor `UD`, and its height is the height of its top point.[^2] For a set `S` of non-negative integers:[^3]

- `P_S(n, k)` counts Dyck paths of semilength `n` with exactly `k` peaks whose heights lie in `S`; other peaks are allowed. This is the **Narayana array of type 1**, and `S = ℕ` gives `N(n, k)`.
- `P̄_S(n, k)` counts Dyck paths with exactly `k` peaks, every peak with height in `S`. This is the **Narayana array of type 2**.
- `V_S` and `V̄_S` are the same counts for valleys (`DU`), the dual arrays.

The column `P_S(n, 0)` counts Dyck paths whose peak heights avoid `S`, the sequence studied by Eu, Liu and Yeh.[^4]

**Peaks in residue classes mod 3.** Write `A_{a,b}` for the heights `≡ b (mod a)`. Corollary 3.9 gives the generating functions `Δ_{A_{3,b}}(x, y)` for `b = 0, 1, 2`. Example 3.10 prints the first rows of the three type-1 arrays, and the first column of `P^{(1)}_{A_{3,2}}` is `1, 1, 1, 2, 5, 13, 35, 97, …`.[^5] Three bijections come with them:[^6]

- `µ` maps Dyck paths avoiding `UUDU` (A105633, the first column of `P^{(1)}_{A_{3,0}}`) onto Dyck paths with no peak at a height `≡ 0 (mod 3)`.
- `µ′` maps Dyck paths onto Dyck paths and sends peaks at heights `≡ 2` to peaks at heights `≡ 1 (mod 3)`, except on the one path `U(UD)^{n−1}D`, which goes to `(UD)^n`.
- `µ″` maps Dyck paths avoiding `UUDD` onto Dyck paths with no peak at a height `≡ 2 (mod 3)`. It is defined by `µ″(ε) = ε` and `µ″(UPDQ) = U µ′(µ″(P)) D µ″(Q)` for `P ≠ UD`, with `µ′(ε) = ε`; the condition `P ≠ UD` holds on every `UUDD`-avoiding path, since `UPDQ` with `P = UD` begins with `UUDD`. The paper identifies this column with A082582, "the number of Dyck paths of semilength n that avoid the pattern UUDD".

The text writes the array in this sentence as `P^{(2)}_{A_{3,2}}`, but the displayed array whose first column is `1, 1, 1, 2, 5, 13, 35, 97` is `P^{(1)}_{A_{3,2}}`, and the bijection's target is the type-1 count.[^5][^6] Peaks at heights in each class `≡ 0, 1, 2 (mod 3)` average `n/6` per Dyck path of semilength `n`, asymptotically.[^7]

## The castle reading

A082582 is the sequence of castles by semi-perimeter on [[castle-perimeter](pages/castle-perimeter.md)]: castles with `w + #blocks = n` number `1, 2, 5, 13, 35, 97, 275, …` for `n = 2, 3, 4, …`. This paper gives the same numbers two Dyck-path readings. For `n ≥ 2`, three families are equinumerous:

| semi-perimeter / semilength `n` | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|---|
| castles of semi-perimeter `n` | 1 | 2 | 5 | 13 | 35 | 97 | 275 |
| Dyck paths avoiding `UUDD` | 1 | 2 | 5 | 13 | 35 | 97 | 275 |
| Dyck paths, no peak at a height `≡ 2 (mod 3)` | 1 | 2 | 5 | 13 | 35 | 97 | 275 |

(Brute force; the two Dyck families also agree at `n = 9` and `n = 10`, with 794 and 2327, the next terms of A082582.)[^exec]

- **No castle bijection here.** The paper counts Dyck paths only, and its `µ″` joins the two Dyck families. The map of [[deutsch-elizalde-2017-bargraphs-dyck-paths](pages/deutsch-elizalde-2017-bargraphs-dyck-paths.md)] sends a Dyck path of semilength `n` to a bargraph whose semi-perimeter minus its number of peaks is `n`, peaks in their sense being plateaus higher than both neighbors, so it does not give this equinumerosity.
- **Not the tower-Narayana form.** The castle-perimeter triangle A271942 is the tower-Narayana identity: the castles of width `w` and semi-perimeter `s` stand on the towers with `s − w − 1` blocks, which number `T̂(w, s − w − 1) = Σ_k N(w, k) C(s − k − 1, w − 1)` ([[tower-heap](pages/tower-heap.md)]), with `w` the castle's width. The paper's arrays refine `N(n, k)` by peak heights instead. None of the summarized sections states the castle triangle or the tower-Narayana sum.
- **Four path readings of A082582.** The castles by semi-perimeter are also counted by the skew Motzkin paths of [[prodinger-2025-cornerless-motzkin-bargraphs](pages/prodinger-2025-cornerless-motzkin-bargraphs.md)] and the cornerless Motzkin paths of [[deutsch-elizalde-2016-bargraphs-cornerless-motzkin](pages/deutsch-elizalde-2016-bargraphs-cornerless-motzkin.md)], besides the two Dyck families here.

## Key Takeaways

- The castle count by semi-perimeter (A082582) counts the Dyck paths of semilength `n` that avoid `UUDD`, and also those with no peak at a height `≡ 2 (mod 3)`. The paper's `µ″` is a bijection between the two (checked to `n = 10`).
- The paper does not contain the tower-Narayana form of the castle triangle; its Narayana arrays grade Dyck paths by peak heights.
- `µ′` exchanges peaks at heights `≡ 2` and `≡ 1 (mod 3)` on all but one Dyck path of each semilength (checked to `n = 10`).

## Entities & Concepts

- The Narayana triangle `N(n, k)` - [[narayana-numbers](pages/narayana-numbers.md)].
- Dyck paths, peaks and valleys - [[dyck-words](pages/dyck-words.md)].
- Castles by semi-perimeter, A082582 - [[castle-perimeter](pages/castle-perimeter.md)].

## Relation to Other Wiki Pages

[[castle-perimeter](pages/castle-perimeter.md)] cites this paper for the two Dyck readings of A082582. [[narayana-numbers](pages/narayana-numbers.md)] records `N(n, k)` as the Dyck paths with `k` peaks; this paper refines that count by the heights of the peaks.

## Footnotes

[^1]: [[baril-florez-ramirez-2026-generalized-narayana-arrays](pages/baril-florez-ramirez-2026-generalized-narayana-arrays.md)] p.333 L1-23, L46 and p.365 L1887 - "AUSTRALASIAN JOURNAL OF COMBINATORICS Volume 94(3) (2026), Pages 333–365"; authors and affiliations; "Released under the CC BY 4.0 International License"; "(Received 30 Apr 2025; revised 11 Dec 2025)".
[^2]: [[baril-florez-ramirez-2026-generalized-narayana-arrays](pages/baril-florez-ramirez-2026-generalized-narayana-arrays.md)] §1 p.334 L57-59 and §2 p.335 L106-113 - "A peak in a Dyck path is a subpath of the form UD, while a valley is a subpath of the form DU. The height of a peak (respectively valley) is the y-coordinate of its highest point (respectively lowest point)"; "Let N(n, k) denote the number of Dyck paths of semilength n with exactly k peaks. The array (N(n, k))n,k≥0, known as the Narayana triangle (see [16] and A001263 in [18])", `N(n, k) = (1/k) C(n−1, k−1) C(n, k−1)`, `n, k ≥ 1`.
[^3]: [[baril-florez-ramirez-2026-generalized-narayana-arrays](pages/baril-florez-ramirez-2026-generalized-narayana-arrays.md)] §2 p.335 L121-140 - "Define PS(n, k) as the number of Dyck paths of semilength n with exactly k peaks whose heights belong to S. Note that the paths may also contain additional peaks whose heights are not in S ... called Narayana array of type 1. Clearly, whenever S = N, the sequence PN(n, k) coincides with the Narayana number N(n, k)"; "let P̄S(n, k) denote the number of Dyck paths of semilength n with exactly k peaks, where every peak has height in S ... called the Narayana array of type 2."
[^4]: [[baril-florez-ramirez-2026-generalized-narayana-arrays](pages/baril-florez-ramirez-2026-generalized-narayana-arrays.md)] §1 p.334 L80-82 - "Eu, Liu, and Yeh [11] studied the sequence (PS(n, 0))n, which counts the number of Dyck paths whose peak heights avoid S."
[^5]: [[baril-florez-ramirez-2026-generalized-narayana-arrays](pages/baril-florez-ramirez-2026-generalized-narayana-arrays.md)] §3.1.3 pp.341-342 L481-558 [synthesis] - `A_{a,b} = {m ∈ ℕ : m ≡ b (mod a)}`; Corollary 3.9, the generating functions `Δ_{A_{3,0}}`, `Δ_{A_{3,1}}`, `Δ_{A_{3,2}}`; Example 3.10, "The first column of P(1)A3,0 corresponds to the sequence A105633, where the n-th term is the number of Dyck paths of semilength n that avoid the pattern UUDU", and the displayed array `P^{(1)}_{A_{3,2}}` with first column `1, 1, 1, 2, 5, 13, 35, 97`.
[^6]: [[baril-florez-ramirez-2026-generalized-narayana-arrays](pages/baril-florez-ramirez-2026-generalized-narayana-arrays.md)] §3.1.3 pp.342-344 L560-628 [synthesis] - `µ` from Dyck paths avoiding `UUDU` to "Dyck paths with no peaks at heights congruent to 0 modulo 3"; `µ′` with `µ′(U(UD)^{n−1}D) = (UD)^n` and four more cases, "µ′ preserves the relevant statistics as expected, except for the special Dyck path U(UD)^{n−1}D"; "the first column of P(2)A3,2 corresponds to the sequence A082582, where the n-th term represents the number of Dyck paths of semilength n that avoid the pattern UUDD", `µ″(UPDQ) = Uµ′(µ″(P))Dµ″(Q)`, "a bijection mapping a Dyck path avoiding UUDD to the set of Dyck paths avoiding peaks at height congruent to 2 modulo 3."
[^7]: [[baril-florez-ramirez-2026-generalized-narayana-arrays](pages/baril-florez-ramirez-2026-generalized-narayana-arrays.md)] Corollary 3.14 p.344 L632-634 - "An asymptotic estimate for the expected number of peaks of heights congruent to i modulo 3 (0 ≤ i ≤ 2) among all Dyck paths of semilength n is given by n/6 (for each i = 0, 1, 2)."
[^exec]: Verified by execution (Python 3.11, 2026-10-16): castles enumerated as skylines with semi-perimeter `w + #blocks`, for `n = 2..8`; all Dyck paths of semilength `n ≤ 10` enumerated, counting those without the factor `UUDD` and those with no peak at a height `≡ 2 (mod 3)` (equal through `n = 10`: 1, 1, 2, 5, 13, 35, 97, 275, 794, 2327 for `n = 1..10`, matching A082582 on oeis.org). `µ′` and `µ″` were implemented from the paper's case definitions (L599-603, L622-623). `µ′` is a bijection on Dyck paths of each semilength `n ≤ 10` and sends the number of peaks at heights `≡ 2` to the number at heights `≡ 1 (mod 3)` on every path but `U(UD)^{n−1}D`. `µ″` maps the `UUDD`-avoiding paths onto the paths with no peak at a height `≡ 2 (mod 3)` for `n ≤ 10`. Examples 3.12 and 3.13 are reproduced. The tower-Narayana identity is checked on [[tower-heap](pages/tower-heap.md)].
