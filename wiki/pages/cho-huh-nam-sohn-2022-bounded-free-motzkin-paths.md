---
title: "Combinatorics on bounded free Motzkin paths and its applications (Cho-Huh-Nam-Sohn, 2022)"
category: Sources
summary: Cho, Huh, Nam and Sohn put the t-core partitions with m corners and largest hook length below kt in bijection with the cornerless Motzkin paths with t − 1 flat steps in the strip 0 ≤ y ≤ k, and count the cores with m corners by a Narayana sum; the self-conjugate cores and the symmetric paths get the same treatment. On castles the paths are tower words, so the (L+1)-cores with b corners and largest hook below k(L+1) correspond to the towers on a base of length L with b blocks and height at most k, and A^e(w, h) is the number of (w+1)-cores with an odd number of corners and largest hook length in [(h−2)(w+1), (h−1)(w+1)). The Narayana sum is T̂(L, b) = Σ_i N(b, i) C(L+1+2b−2i, 2b), indexed by blocks, its i-th term counting the towers with i bargraph peaks, and the self-conjugate count is the number T̂_pal(L, b) of palindromic towers in closed form.
tags: [paper, source, partition, t-core, self-conjugate, motzkin, cornerless, dyck, narayana, tower, palindromic, bijection, oeis]
sources: [cho-huh-nam-sohn-2022-bounded-free-motzkin-paths]
created: 2026-10-17
updated: 2026-10-17
---

# Combinatorics on bounded free Motzkin paths and its applications (Cho-Huh-Nam-Sohn, 2022)

**Source:** `raw/cho-huh-nam-sohn-2022-bounded-free-motzkin-paths.pdf` (text layer at `raw/cho-huh-nam-sohn-2022-bounded-free-motzkin-paths.txt`, extracted with `pdftotext -layout`; the PDF is git-ignored, the text is tracked). arXiv:2205.15554v1 [math.CO], 31 May 2022.[^1]
**Authors:** Hyunsoo Cho (Ewha Womans University), JiSun Huh (Ajou University), Hayan Nam (Duksung Women's University), Jaebum Sohn (Yonsei University).[^1]
**Date ingested:** 2026-10-17
**Type:** paper (PDF, 19 pp.)

## Summary

This page records the paper's §3.2 and §3.3, which count core partitions through cornerless Motzkin paths, and reads them on castles.

A partition `λ = (λ_1 ≥ λ_2 ≥ … ≥ λ_ℓ > 0)` has `ℓ(λ) = ℓ` parts and is drawn as a Young diagram with `λ_i` boxes in row `i`. The hook length of a box counts the box itself, the boxes to its right and the boxes below it. For an integer `t ≥ 2`, `λ` is a **`t`-core** if no box has hook length `t`. A **corner** of `λ` is a box whose removal leaves the diagram of a partition; there is one at the end of the last row of each part size, so the number of corners is the number of distinct parts. The largest hook length is that of the box in row 1 and column 1, `λ_1 + ℓ(λ) − 1`. The paper writes it `h(1, 1)`; this page writes it out, since `h` is the castle height.[^2]

Theorem 3.3 puts three sets in bijection, for integers `t`, `m`, `k ≥ 0`: the `t`-cores with `m` corners and `h(1, 1) < kt`; the sequences `(n_0, n_1, …, n_{t−1})` with `n_0 = 0` and `0 ≤ n_i ≤ k` that satisfy `Σ_{i=1}^{t} |n_i − n_{i−1}| = 2m`, where `n_t = 0`; and the cornerless Motzkin paths, those with no peak `UD` and no valley `DU`, of length `2m + t − 1` with `t − 1` flat steps that stay in the strip `0 ≤ y ≤ k`.[^3] The first map sends a core to the sequence in which `n_j` is the number of first-column hook lengths of `λ` congruent to `j` modulo `t`. None of them is a multiple of `t`, and each maximal run of consecutive integers among them gives one corner. The second map draws the path with its flat steps at the heights `n_1, …, n_{t−1}`, joined by up and down steps; this is Deutsch and Elizalde's bargraph bijection ([[deutsch-elizalde-2016-bargraphs-cornerless-motzkin](pages/deutsch-elizalde-2016-bargraphs-cornerless-motzkin.md)]).[^4]

Proposition 3.4 counts the cores. Deleting the flat steps of such a path leaves a Dyck path with `m` up steps, and the Dyck paths with `m` up steps and `i` peaks number `N(m, i)`, the [[narayana-numbers](pages/narayana-numbers.md)]. The path is cornerless exactly when each of the `i` peaks and `i − 1` valleys of its Dyck path receives at least one of the `t − 1` flat steps, which can be done in `C(t + 2m − 2i, 2m)` ways. So the number of `t`-cores with `m ≥ 1` corners is[^5]

```
cc(t, m)  =  Σ_{i=1}^{min(m, ⌊t/2⌋)}  N(m, i) · C(t + 2m − 2i, 2m).
```

The authors know of no earlier formula for the number of `t`-cores with a given number of corners. The paper tabulates `cc(t, m)` for `2 ≤ t ≤ 6` and `1 ≤ m ≤ 8` and points to A063490 and A160747 for `t = 5` and `t = 6`.[^6]

Theorem 3.7 and Proposition 3.8 do the same for the self-conjugate cores, those whose diagram is symmetric about the main diagonal. The self-conjugate `t`-cores with `m` corners and `h(1, 1) < kt` are in bijection with the cornerless symmetric Motzkin paths of length `2m + t − 1` with `t − 1` flat steps in the strip `0 ≤ y ≤ k`.[^7] The symmetric Dyck paths with `m` up steps and `i` peaks number `C(⌊(m−1)/2⌋, ⌊(i−1)/2⌋) · C(⌊m/2⌋, ⌊i/2⌋)`, a known count that the paper reproves as its formula (13),[^8] and the flat steps can be inserted symmetrically in `C(⌊t/2⌋ + m − i, m)` ways, so for `m ≥ 1`[^9]

```
scc(t, m)  =  Σ_{i=1}^{min(m, ⌊t/2⌋)}  C(⌊(m−1)/2⌋, ⌊(i−1)/2⌋) · C(⌊m/2⌋, ⌊i/2⌋) · C(⌊t/2⌋ + m − i, m),
```

with `scc(t, 0) = 1` and `scc(t, m) = scc(t + 1, m)` for even `t`. The paper tabulates it for `2 ≤ t ≤ 11` and `1 ≤ m ≤ 8`.[^9]

## Castles as core partitions

A cornerless Motzkin path is the tower word of a castle ([[motzkin-castles](pages/motzkin-castles.md)] §1): its flat steps `R` are the columns, at heights `c_j − 1`, and its up steps are the blocks above the bottom row. So the sequence `(n_1, …, n_{t−1})` of Theorem 3.3 is a tower `(c_1, …, c_L)` on a base of length `L = t − 1` ([[tower-heap](pages/tower-heap.md)]). Its sum of differences is twice the total rise, `Σ |n_i − n_{i−1}| = 2 · blocks`, and the strip bound `k` is the tower height bound of [[castle-notation](pages/castle-notation.md)], `k = h − 1` for castles of height `h`. In the wiki's notation Theorem 3.3 reads

```
(L+1)-cores with b corners and  λ_1 + ℓ(λ) − 1 < k(L + 1)
        ↔  towers on a base of length L with b blocks and height at most k,
```

the tower having as its `j`-th column the number of first-column hook lengths congruent to `j` modulo `L + 1`.[^exec] The paper's symbols translate as follows:

| paper | wiki |
|---|---|
| `t` | `L + 1`, the base length plus one, which is the castle width plus one |
| `m`, the number of corners | `b`, the blocks of the tower; the castle has `b + 1` |
| `k`, the strip bound | `k`, the tower height bound |
| `n_1, …, n_{t−1}` | the tower's column heights `c_1, …, c_L` |
| `h(1, 1)` | `λ_1 + ℓ(λ) − 1` |
| `u`, `d`, `f` (up, down, flat) | `U`, `D`, `R` of the tower word |
| `N(m, i)` | `N(b, i)` |
| `cc(t, m)` | `T̂(t − 1, m)` |
| `scc(t, m)` | `T̂_pal(t − 1, m)`, the palindromic towers (below) |

*Example.* The 4-core `(4, 4, 2, 2)` has first-column hook lengths `7, 6, 3, 2`, with residues `3, 2, 3, 2` modulo 4, so `n_1 = 0`, `n_2 = 2` and `n_3 = 2`. This is the tower `(0, 2, 2)` and the castle `(1, 3, 3)` of width 3 and height 3. The tower has 2 blocks and the partition has 2 corners, one for each of the part sizes 4 and 2, and the largest hook length 7 is below `2 · 4`, the bound for towers of height at most 2. The paper lists this core first among the sixteen 4-cores with 2 corners.[^10]

**Castles of height `h`.** Removing the bottom row sends the castles of width `w` and height `h` onto the towers of height at most `h − 1` that are not of height at most `h − 2`. A castle has one block more than its towers, so an even number of castle blocks is an odd number of corners. With the counts `A(w, h)` and `A^e(w, h)` of [[castle-notation](pages/castle-notation.md)], for `h ≥ 2`,

```
A(w, h)    =  the number of nonempty (w+1)-cores λ with  (h − 2)(w + 1)  ≤  λ_1 + ℓ(λ) − 1  <  (h − 1)(w + 1),
A^e(w, h)  =  the number of these cores with an odd number of corners.
```

So Project Euler 502 counts `(w+1)`-cores in a window of largest hook lengths by the parity of their number of corners.[^exec] For castles of height 2 the window is `λ_1 + ℓ(λ) − 1 < w + 1`, and since no hook length exceeds the largest one, every nonempty partition with `λ_1 + ℓ(λ) ≤ w + 1` is a `(w+1)`-core in the window. There are `2^w − 1 = A(w, 2)` of them. At width 4 these are the 15 nonempty partitions with `λ_1 + ℓ(λ) ≤ 5`; 10 of them have an odd number of corners, and `F(4, 2) = 10` is the first example value of the problem statement.[^pe][^exec]

**Palindromic castles.** A symmetric tower word is the word of a palindromic tower, `c_j = c_{L+1−j}`. So Theorem 3.7 makes the self-conjugate `(L+1)`-cores with `b` corners and `λ_1 + ℓ(λ) − 1 < k(L + 1)` as many as the palindromic towers on a base of length `L` with `b` blocks and height at most `k`. In the same way, the palindromic castles of width `w` and height `h` with an even number of blocks are as many as the self-conjugate `(w+1)`-cores in the window above with an odd number of corners. The bijection of Theorem 3.7 is not the map of Theorem 3.3 restricted to self-conjugate cores: that map sends the self-conjugate 3-core `(1)` to the tower `(1, 0)`, which is not palindromic.[^exec]

## Key Takeaways

- **Towers are core partitions.** The `(L+1)`-cores with `b` corners and largest hook length below `k(L + 1)` correspond to the towers on a base of length `L` with `b` blocks and height at most `k`. Column `j` of the tower is the number of first-column hook lengths of the core congruent to `j` modulo `L + 1`. For `h ≥ 2`, `A^e(w, h)` is the number of `(w+1)`-cores with an odd number of corners and largest hook length in `[(h − 2)(w + 1), (h − 1)(w + 1))`.[^3][^exec]
- **A Narayana sum indexed by blocks.** For `b ≥ 1`, `T̂(L, b) = Σ_{i=1}^{min(b, ⌊(L+1)/2⌋)} N(b, i) C(L + 1 + 2b − 2i, 2b)`, with the bijective proof of Proposition 3.4.[^5] [[tower-heap](pages/tower-heap.md)] also has the sum `Σ_k N(L, k) C(b + L − k, L − 1)`, indexed by the base length and refined by descents. In the new sum, term `i` counts the towers whose word with its flat steps deleted is a Dyck path with `i` peaks. These are the towers with `i` plateaus higher than the columns on both sides, with height 0 outside the base. For `b ≥ 1` they are the bargraph peaks of the castle in Deutsch and Elizalde's sense, factors `U H⋯H D` of its bargraph word, and not the castle peaks of [[castle-foata-transform](pages/castle-foata-transform.md)].[^exec]
- **Table 1 is the tower table.** `cc(t, m) = T̂(t − 1, m)`, so the paper's rows `t = 3, 4, 5, 6` are the rows `L = 2, 3, 4, 5` of [[tower-narayana-polynomial](pages/tower-narayana-polynomial.md)]: A005408, A005891, A063490 (with offset 1) and A160747.[^6][^exec]
- **Palindromic towers in closed form.** Write `T̂_pal(L, b)` for the number of palindromic towers on a base of length `L` with `b` blocks. For `b ≥ 1`, `T̂_pal(L, b) = Σ_{i=1}^{min(b, ⌊(L+1)/2⌋)} C(⌊(b−1)/2⌋, ⌊(i−1)/2⌋) C(⌊b/2⌋, ⌊i/2⌋) C(⌊(L+1)/2⌋ + b − i, b)`, and `T̂_pal(L, 0) = 1`. The palindromic castles of width `w` with `b + 1` blocks, of any height, number `T̂_pal(w, b)`. For `b = 0, 1, …, 7` the rows `L = 3` and `L = 5` are `1, 2, 4, 5, 7, 8, 10, 11` and `1, 3, 9, 15, 27, 37, 55, 69`.[^9][^exec]
- **Doubling the middle column.** The paper's `scc(t, m) = scc(t + 1, m)` for even `t` is `T̂_pal(L, b) = T̂_pal(L + 1, b)` for odd `L`. On castles it is a bijection: doubling the middle column of a palindromic tower on an odd base keeps its blocks and its height, and every palindromic tower on an even base arises exactly once, since its two middle columns are equal.[^exec]

## Entities & Concepts

- [[tower-heap](pages/tower-heap.md)] - towers counted by blocks, `T̂(L, b)`, now with the sum indexed by blocks.
- [[narayana-numbers](pages/narayana-numbers.md)] - `N(b, i)`, the Dyck paths by peaks, in the sum indexed by blocks.
- [[motzkin-castles](pages/motzkin-castles.md)] - the castle as a cornerless Motzkin path, which is the second map of Theorem 3.3.
- [[deutsch-elizalde-2016-bargraphs-cornerless-motzkin](pages/deutsch-elizalde-2016-bargraphs-cornerless-motzkin.md)] - the paper's reference [8], the bargraph bijection, and the bargraph peaks.
- [[castle-classification-shape](pages/castle-classification-shape.md)] - the palindromic castles.
- [[tower-narayana-polynomial](pages/tower-narayana-polynomial.md)] - the rows of `T̂` and their A-numbers, which are the rows of Table 1.
- [[castle-notation](pages/castle-notation.md)] - the translation of the paper's symbols.

## Relation to Other Wiki Pages

The second map of Theorem 3.3 is the bijection the wiki already uses between castles and cornerless Motzkin paths, so the counts of the paper are tower counts the wiki already has: `cc(t, m) = T̂(t − 1, m)`, whose generating function in `b` is the Narayana polynomial over `(1 − x)^L` on [[tower-heap](pages/tower-heap.md)]. The paper adds three things: the towers as core partitions, with the tower height bound `k` turned into a bound on the largest hook length; the sum indexed by blocks, which comes with a proof; and the palindromic towers by base and blocks in closed form, where [[castle-classification-shape](pages/castle-classification-shape.md)] had a generating function in width and blocks from Deutsch and Elizalde and the semi-perimeter count A273905. The paper gives no formula at a fixed height bound `k`, so the window statement for `A^e(w, h)` is a reformulation of the castle count, not a new way to compute it.

## Footnotes

[^1]: [[cho-huh-nam-sohn-2022-bounded-free-motzkin-paths](pages/cho-huh-nam-sohn-2022-bounded-free-motzkin-paths.md)] p.1 title block L1-8 - "COMBINATORICS ON BOUNDED FREE MOTZKIN PATHS AND ITS APPLICATIONS", "arXiv:2205.15554v1 [math.CO] 31 May 2022", "HYUNSOO CHO, JISUN HUH, HAYAN NAM, AND JAEBUM SOHN"; affiliations p.19 L1085-1097.
[^2]: [[cho-huh-nam-sohn-2022-bounded-free-motzkin-paths](pages/cho-huh-nam-sohn-2022-bounded-free-motzkin-paths.md)] pp.12-13 §3.2 L691-703 [synthesis] - a partition as a non-increasing positive sequence with its Young diagram; "An inner corner of a Young diagram is a box that can be removed from the Young diagram and the rest of the Young diagram is still the Young diagram of a partition"; the hook length `h(i, j)` "is the number of boxes on the right, in the below, and itself"; "A partition is called a t-core if its Young diagram has no box of hook length t".
[^3]: [[cho-huh-nam-sohn-2022-bounded-free-motzkin-paths](pages/cho-huh-nam-sohn-2022-bounded-free-motzkin-paths.md)] p.13 Theorem 3.3 L721-733 - "(a) The set of t-core partitions with m corners such that h(1, 1) < kt. (b) The set of non-negative integer sequences (n0, n1, . . . , nt−1) satisfying that n0 = 0, ni ≤ k for all i, and Σ_{i=1}^{t} |ni − ni−1| = 2m, where we set nt := 0. (c) The set of cornerless Motzkin paths of length 2m + t − 1 with t − 1 flat steps that are contained in the strip 0 ≤ y ≤ k"; the steps `u`, `d`, `f` and "We say that a path is cornerless if it has no peaks or valleys", p.1 §1 L26-33.
[^4]: [[cho-huh-nam-sohn-2022-bounded-free-motzkin-paths](pages/cho-huh-nam-sohn-2022-bounded-free-motzkin-paths.md)] pp.13-14 proof of Theorem 3.3 L702-708, L735-744, L758-761 [synthesis] - the first-column hook lengths form the beta-set `β(λ)`, placed at the positions labeled `ti + j`, so `n_j` counts the elements of `β(λ)` congruent to `j` modulo `t`; "we get one inner corner for each maximal sequence of consecutive numbers in the beta-set"; the path "has t − 1 flat steps at height n1, n2, · · · , nt−1 with proper up and/or down steps connecting those flat steps"; the bijection used is "introduced by Deutsch and Elizalde [8]" (L718-719).
[^5]: [[cho-huh-nam-sohn-2022-bounded-free-motzkin-paths](pages/cho-huh-nam-sohn-2022-bounded-free-motzkin-paths.md)] p.14 Proposition 3.4 and proof L785-801 - "The number of t-core partitions with m corners is given by cc(t, m) := Σ_{i=1}^{min(m,⌊t/2⌋)} N(m, i) C(t + 2m − 2i, 2m)", and "we have to insert at least one flat steps at the positions of i peaks and i − 1 valleys. As the number of Dyck paths consisting of m up steps and m down steps with i peaks is counted by the Narayana number N(m, i), the proof is followed."
[^6]: [[cho-huh-nam-sohn-2022-bounded-free-motzkin-paths](pages/cho-huh-nam-sohn-2022-bounded-free-motzkin-paths.md)] p.14 L782-784, L802-805, and Table 1 p.15 L870-877 - "As far as we know, it seems new to get the formula for the number of t-core partitions with the fixed number of corners"; "The numbers of t-core partitions with m corners for 2 ≤ t ≤ 6 and 1 ≤ m ≤ 8 are given in Table 1"; "See sequences A063490 and A160747 in [14] for more the values of cc(t, m) for t = 5 and t = 6, respectively."
[^7]: [[cho-huh-nam-sohn-2022-bounded-free-motzkin-paths](pages/cho-huh-nam-sohn-2022-bounded-free-motzkin-paths.md)] p.16 Theorem 3.7 L916-918, L931-932 - "there is a bijection between any pair of the following sets. (a) The set of self-conjugate t-cores with m corners such that h(1, 1) < kt." and "(e) The set of cornerless symmetric Motzkin paths of length 2m + t − 1 with t − 1 flat steps that are contained in the strip 0 ≤ y ≤ k"; self-conjugate, `λ = λ′`, p.14 L807-810.
[^8]: [[cho-huh-nam-sohn-2022-bounded-free-motzkin-paths](pages/cho-huh-nam-sohn-2022-bounded-free-motzkin-paths.md)] p.12 L650-658 - "a combinatorial proof of the well-known fact that the number of symmetric Dyck paths of length 2m with i peaks is given by (13)", the product `C(⌊(m−1)/2⌋, ⌊(i−1)/2⌋) C(⌊m/2⌋, ⌊i/2⌋)`.
[^9]: [[cho-huh-nam-sohn-2022-bounded-free-motzkin-paths](pages/cho-huh-nam-sohn-2022-bounded-free-motzkin-paths.md)] p.17 Proposition 3.8 and proof L965-986, Table 2 p.18 L1040-1048 [synthesis] - `scc(t, m)` as displayed, "for m > 0 and scc(t, 0) = 1. In addition, scc(t, m) = scc(t + 1, m) for even t"; the number of ways to insert the `t − 1` flat steps symmetrically is `C(⌊t/2⌋ + m − i, m)`; Table 2 gives `scc(t, m)` for `2 ≤ t ≤ 11` and `1 ≤ m ≤ 8`.
[^10]: [[cho-huh-nam-sohn-2022-bounded-free-motzkin-paths](pages/cho-huh-nam-sohn-2022-bounded-free-motzkin-paths.md)] pp.14-15 L773-776, Figure 7 L815 - "there are sixteen 4-core partitions with 2 corners", and the first row of Figure 7, "(4,4,2,2) ↔ … ↔ [0,0,2,2]".
[^pe]: https://projecteuler.net/problem=502 (fetched 2026-10-17) - "For example, F(4,2) = 10, F(13,10) = 3729050610636, F(10,13) = 37959702514, and F(100,100) mod 1 000 000 007 = 841913936."
[^exec]: Verified by execution (Python 3.10, 2026-10-17): `bin/python/bounded_t_cores.py`, run log `bin/python/bounded_t_cores-run.log`. The towers on a base of length `L ≤ 6` with `b ≤ 7` blocks and `L = 7` with `b ≤ 6` against the sum indexed by blocks, its term `i` against the towers with `i` plateaus higher than both neighbors, and the palindromic towers against `T̂_pal`; the middle-column doubling for `L = 1, 3, 5` and `b ≤ 5`; the residue map as a bijection from the `t`-cores with largest hook length below `kt` onto the towers of height at most `k` with blocks equal to corners, and the self-conjugate cores against the palindromic towers by count, for `t ≤ 6` and `k ≤ 3`; `A(w, h)`, `A^e(w, h)` and their palindromic and self-conjugate counterparts against the cores in the window for `w ≤ 5` and `2 ≤ h ≤ 4`; the example `(4, 4, 2, 2)` and the 3-core `(1)`; the paper's Tables 1 and 2.
