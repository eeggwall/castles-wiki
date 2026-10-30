---
title: "Thomas and May (2022) - Mountain Counting"
category: Sources
summary: Aaron Thomas and Russell May count mountains of spheres, stacks on a w × ℓ rectangular base in which every higher sphere rests on four spheres below, by slicing them into fountains of coins. They put the coin in row r at position k when it rests on the coins at positions k − 1 and k of row r − 1, and cut a fountain of width w diagonally into w slants; the slant heights ⟨s_1, …, s_w⟩ describe a fountain exactly when s_1 = 1 and s_{k−1} ≥ s_k − 1, so the fountains of width w are counted by the Catalan number C_w, and by the height s of the last slant they form a ballot table. Every lateral face of a mountain is a fountain, a mountain is a sequence of fountains each leaning on the one before, and the number of mountains on a w × ℓ base is a sum of entries of the (ℓ − 1)-st power of a C_w × C_w leaning matrix, tabulated for w, ℓ ≤ 6. In castle terms the slants shear a castle on the brick wall onto a square-grid skyline that rises by at most 1 and starts at height 1, the mirror image of the castles that drop by at most 1 and end at height 1.
tags: [source, paper, fountain-of-coins, slant, mountains-of-spheres, catalan, ballot-numbers, transfer-matrix, continued-fraction, three-dimensional]
sources: [thomas-may-2022-mountain-counting]
created: 2026-10-29
updated: 2026-10-29
---

# Thomas and May (2022) - Mountain Counting

**Source:** `raw/thomas-may-2022-mountain-counting.pdf` (text layer at `raw/thomas-may-2022-mountain-counting.txt`, extracted with `pdftotext -layout`; the PDF is git-ignored, the text is tracked). A. Thomas and R. May, "Mountain Counting: On the Enumeration of Three-Dimensional Stacks of Spheres", *The PUMP Journal of Undergraduate Research* 5 (2022), 70-79, https://journals.calstate.edu/pump/article/view/2664; the PDF was fetched from the copy at http://cord.distantreader.org/stacks/journals-ojs/pump/pump-2664.pdf.[^1] The text layer drops summation signs; the formulas below are read from the PDF.
**Date ingested:** 2026-10-29
**Type:** paper (PDF)

## Notation used on this page

| paper | meaning | castle reading |
|---|---|---|
| `(n, w)` fountain | `n` coins, `w` contiguous coins in the bottom row, every higher coin resting on two coins of the row below (the gravity rule) | a castle on the brick wall of width `w` with `n` cells |
| `(r, k)` | the coin in row `r` at position `k`, resting on `(r − 1, k − 1)` and `(r − 1, k)` | a brick and its two supports |
| the `k`th slant | the coins with position `k` | column `k` of the sheared skyline |
| `⟨s_1, …, s_w⟩` | the fountain with `s_k` coins on its `k`th slant | the sheared skyline, column heights `s_k` |
| `f_{w,s}` | the fountains of width `w` with `s` coins on the rightmost slant | |
| `(n, w, ℓ)` mountain | `n` spheres on a `w × ℓ` rectangular base, every higher sphere resting on four spheres below | |
| `m_{w,ℓ}`, `L_w` | the mountains on a `w × ℓ` base, the leaning matrix | |

## Summary

**Fountains and the continued fraction.** An `(n, w)` fountain is an arrangement of `n` identical coins whose bottom row is `w` contiguous coins, the coins in higher rows obeying the gravity rule that each rests on two coins of the row immediately below; `w` is its width. The authors write that Odlyzko and Wilf attributed the question to J. M. Propp, noted that the fountains with `w` coins in the bottom row are counted by the Catalan number `C_w`, and showed that the fountains counted by their total number of coins `n` have the generating function[^2]

```
f(x)  =  Σ_n a_n x^n  =  1 / (1 − x / (1 − x² / (1 − x³ / (1 − ⋯)))),
```

a continued fraction first studied by Ramanujan.[^3]

**Slants.** A coin is named by its row `r` and its position `k`, numbered so that a coin has the position of the coin to its right in the row below. A fountain of width `w` is then a set of pairs with `(1, k)` for exactly `1 ≤ k ≤ w`, in which `(r, k)` with `r > 1` requires `(r − 1, k − 1)` and `(r − 1, k)`. The `k`th slant is the set of coins at position `k`. By the gravity rule a slant has no gaps, so a fountain is the `w`-tuple `⟨s_1, …, s_w⟩` of its slant heights, with `Σ s_k` coins, and the fountain of Figure 2 is `⟨1, 2, 3, 2, 1, 2, 3, 4⟩`.[^4] The top coin of slant `k` is `(s_k, k)` and rests on `(s_k − 1, k − 1)`, so a sequence of positive integers is a fountain exactly when[^5]

```
s_1 = 1,    s_{k−1} ≥ s_k − 1   for 1 < k ≤ w.
```

The authors note that these sequences are one of the Catalan objects of Stanley's *Enumerative Combinatorics*, Volume 2 (example U, p. 224).[^5]

**Fountains by the last slant.** Appending a slant of `s` coins to a fountain whose last slant has `s' ≥ s − 1` coins builds every fountain once, which gives the recurrence `f_{n,w,s} = Σ_{s' ≥ s − 1} f_{n−s,w−1,s'}`. Summed over `n`, it gives the table below of `f_{w,s}`, the fountains of width `w` whose last slant has `s` coins; the authors relate it to the Catalan triangle of Lee and Oh, and its first column is the Catalan numbers.[^6]

| `f_{w,s}` | `s = 1` | 2 | 3 | 4 | 5 | 6 | `f_w` |
|---|---|---|---|---|---|---|---|
| `w = 1` | 1 | 0 | 0 | 0 | 0 | 0 | 1 |
| 2 | 1 | 1 | 0 | 0 | 0 | 0 | 2 |
| 3 | 2 | 2 | 1 | 0 | 0 | 0 | 5 |
| 4 | 5 | 5 | 3 | 1 | 0 | 0 | 14 |
| 5 | 14 | 14 | 9 | 4 | 1 | 0 | 42 |
| 6 | 42 | 42 | 28 | 14 | 5 | 1 | 132 |

In closed form `f_{w,s} = (s/w) C(2w − s − 1, w − s)`, the ballot numbers; that and the table were checked by execution for `w ≤ 8`.[^exec]

**Mountains.** An `(n, w, ℓ)` mountain is `n` spheres whose bottom layer is a `w × ℓ` rectangular grid, every higher sphere resting on four spheres of the layer below, a class of stacks introduced by Endicott, May and Shacklette ([[endicott-may-shacklette-2018-stacks-of-spheres](pages/endicott-may-shacklette-2018-stacks-of-spheres.md)]).[^7] The mountains of width 1 are single rows, and those of width 2 number `m_{2,ℓ} = 2^{ℓ−1}`.[^8] Every lateral face of a mountain, the spheres with one `x`-position, is a fountain, since the two supports of a sphere that lie in its own face are its two supports as a coin. A fountain `F = ⟨s_1, …, s_w⟩` leans on `F' = ⟨s'_1, …, s'_w⟩` when `s'_{k−1} ≥ s_k − 1` and `s'_k ≥ s_k − 1` for all `1 < k ≤ w`, and a sequence of fountains of width `w` is a mountain exactly when the first is the flat row `1^w` and each leans on the one before.[^9] The leaning matrix `L_w` is the `C_w × C_w` 0/1 matrix of that relation, and[^10]

```
m_{w,ℓ}  =  1 · L_w^{ℓ−1} · m_{w,1},
```

the sum of the entries of the first column of `L_w^{ℓ−1}` with the fountains in dictionary order of their slants. The paper tabulates `m_{w,ℓ}` for `w, ℓ ≤ 6`, gives the mountains by number of spheres for `n ≤ 20`, and notes that `m_{3,ℓ}` has generating function `x(1 − x)/(1 − 5x + 3x²)`, the sequence A018902.[^10][^11]

**Open problems.** The leaning matrix has size `C_w`, exponential in the width, so the formula is not efficient, and the generating functions of mountains are open. Serban Raianu's variant puts the spheres of each layer on a hexagonal lattice, a parallelogram base with each higher sphere resting on three spheres below.[^12]

## The castle reading

- **A fountain is a castle on the brick wall.** A coin resting on two coins of the row below is a brick resting on both bricks below it in running bond, so an `(n, w)` fountain is a brick-wall castle of width `w` with `n` cells, and the maximal runs of coins in a row are its blocks.
- **The slants are a shear onto the square grid.** Moving the coins of row `r` by `r − 1` places stacks each slant into one column, and the slant heights `⟨s_1, …, s_w⟩` are a square-grid skyline with `s_1 = 1` that rises by at most 1 from each column to the next. Its mirror image drops by at most 1 and ends at height 1, the castles counted by `C_w` in the section *Relatives in the semi-perimeter grading* of [[motzkin-castles](pages/motzkin-castles.md)] and in [[castle-sequence-catalog](pages/castle-sequence-catalog.md)]. The shift moves a whole row at once, so the rows, the blocks, the height and the cells of the fountain are those of the skyline; checked brick by brick for `w ≤ 10`.[^exec]
- **The last slant is the first column of the mirror.** `f_{w,s}` counts the castles of width `w` that drop by at most 1, end at height 1 and start at height `s`.
- **The leaning matrix is a transfer matrix.** The leaning relation is a rule on neighboring lateral faces, as a strip rule of [[castle-strip](pages/castle-strip.md)] is a rule on neighboring columns, and `m_{w,ℓ}` is a sum of entries of the rule's power. Its letters are the `C_w` fountains of width `w` instead of the heights `1, …, h`.

## Key Takeaways

- **A fountain is its slant heights**, `s_1 = 1` and `s_{k−1} ≥ s_k − 1`, which makes the Catalan count by width a count of sequences.[^5]
- **Fountains by coins** have Ramanujan's continued fraction `1/(1 − x/(1 − x²/(1 − x³/⋯)))`.[^2][^3]
- **Fountains by width and last slant** are the ballot numbers `f_{w,s}`.[^6][^exec]
- **Mountains are sequences of leaning fountains**, counted by powers of a `C_w × C_w` leaning matrix.[^9][^10]

## Entities & Concepts

- [[motzkin-castles](pages/motzkin-castles.md)] - the castles that drop by at most 1 and end at height 1, the mirror images of the slant sequences.
- [[catalan-numbers](pages/catalan-numbers.md)] - the fountains by width.
- [[castle-strip](pages/castle-strip.md)] - strip rules and their transfer matrices, the pattern of the leaning matrix.
- [[endicott-may-shacklette-2018-stacks-of-spheres](pages/endicott-may-shacklette-2018-stacks-of-spheres.md)] - the stacks of spheres this paper counts in general.

## Footnotes

[^1]: [[thomas-may-2022-mountain-counting](pages/thomas-may-2022-mountain-counting.md)] p.70 L1-L37 [synthesis] - "Mountain Counting", "A. Thomas and R. May", the abstract, "Mathematics Subject Classification (2020) : 05A15", "the pump journal of undergraduate research 5 (2022), 70–79".
[^2]: [[thomas-may-2022-mountain-counting](pages/thomas-may-2022-mountain-counting.md)] §1 p.71 L50-L75 - "An (n, w) fountain of coins is an arrangement of n identical coins subject to two rules: the bottom row must consist of w contiguous coins, and the coins in higher rows must satisfy the gravity rule that each coin has to rest on two coins in the row immediately below. The number of coins in the bottom row of a fountain is called its width."; "Odlyzko and Wilf analyzed fountains of coins in [7] and attributed the question of their enumeration to J.M. Propp. They noted that the number of fountains with exactly w coins in the bottom row coincides with the wth Catalan number"; "they showed that if an denotes the number of fountains with n total coins, then the generating function f (x) = n an x is the continued fraction", displayed as (1).
[^3]: [[thomas-may-2022-mountain-counting](pages/thomas-may-2022-mountain-counting.md)] §1 p.71 L76-L78 - "This continued fraction was first studied by S. Ramanujan, and an identity in his “lost notebook” [1] provided a direct method in [7] to approximate the coefficients of this generating function."
[^4]: [[thomas-may-2022-mountain-counting](pages/thomas-may-2022-mountain-counting.md)] §2 pp.71-73 L47-L48, L120-L144 [synthesis] - the caption of Figure 2, "A fountain of coins of width 8 and the same fountain with its slant representation h1, 2, 3, 2, 1, 2, 3, 4i"; "Note that the position of a coin in one row is the same as the position of the coin to its right in the row below."; the gravity rule "if r > 1 and (r, k) ∈ F , then (r − 1, k − 1) and (r − 1, k) are also in F"; "We say the k th slant of a fountain is the set of all coins with constant position k in the rows."; "By the gravity rule, we can see that a slant has no “gaps”"; "any fountain of width w may be expressed completely as a w-tuple of the numbers of coins on its slants".
[^5]: [[thomas-may-2022-mountain-counting](pages/thomas-may-2022-mountain-counting.md)] §2 p.73 L145-L162 - "The leftmost slant s1 must be exactly 1 because there are no coins to the left of the beginning of any fountain. The highest coin in the k th slant has coordinates (sk , k) and, as long as sk > 1, by the gravity rule must be supported by the coin below and to the left, which has coordinates (sk − 1, k − 1). Therefore, the number coins sk−1 in the k − 1th slant must be at least sk − 1."; condition (2); "Sequences satisfying Equation 2 are one of the sixty six incarnations of combinatorial objects in [11] (example U, page 224) giving rise to the Catalan numbers."
[^6]: [[thomas-may-2022-mountain-counting](pages/thomas-may-2022-mountain-counting.md)] §2 pp.73-74 L166-L208 [synthesis] - the refinements `f_{n,w,s}`, `f_{w,s}`, `f_w`; "Any fountain can be extended in width by tacking a slant of coins onto the rightmost slant, as limited by Equation 2."; the recurrence (3); the table of `f_{w,s}` for `w ≤ 6`; "The recurrence relation and values for fw,s coincide with that of a transpose of the so-called Catalan triangle"; "In particular, the leftmost column in the table coincides with the Catalan numbers".
[^7]: [[thomas-may-2022-mountain-counting](pages/thomas-may-2022-mountain-counting.md)] §1 p.71 L79-L89 - "Mountains of spheres were first introduced by Endicott et al. in [2]. As defined there, an (n, w, `) mountain is an arrangement of n identical spheres into a three-dimensional lattice that follows two rules: its bottom layer forms a w × ` rectangular grid of spheres, and higher layers follow the gravity rule that every sphere must rest on four spheres in the layer immediately below."
[^8]: [[thomas-may-2022-mountain-counting](pages/thomas-may-2022-mountain-counting.md)] §3 p.75 L235-L240 [synthesis] - `m_{w,ℓ} = m_{ℓ,w}`; "A mountain of width 1 could only consist of a single contiguous row of spheres"; the second layer of a mountain of width 2 "has ` − 1 places to insert spheres", so `m_{2,ℓ} = 2^{ℓ−1}`.
[^9]: [[thomas-may-2022-mountain-counting](pages/thomas-may-2022-mountain-counting.md)] §3 pp.75-76 L255-L282 [synthesis] - "The k th lateral face of a mountain is the set of spheres whose x-position is k"; "each lateral face of a mountain actually forms a fountain when placed upright"; the leaning relation, `s'_{k−1} ≥ s_k − 1` and `s'_k ≥ s_k − 1`; "a sequence F1 , . . . , F` of fountains of width w represents a mountain if and only if F1 = 1w , the sequence of w ones, and F1 ≻ · · · ≻ F`".
[^10]: [[thomas-may-2022-mountain-counting](pages/thomas-may-2022-mountain-counting.md)] §3 pp.76-77 L283-L366 [synthesis] - the recurrence (4); the mountains by number of spheres for `n ≤ 20`, "1, 2, 2, 3, 3, 4, 6, 6, 9, 14, 18, 22, 33, 57, 76, 91, 139, 236, 348, 470"; the recurrence (5); the leaning matrix (6), "The size of Lw is Cw × Cw"; `L_3`; formula (8), "mw,` is the sum of the entries in the first column of the ` − 1th power of the leaning matrix Lw"; the table of `m_{w,ℓ}` for `w, ℓ ≤ 6`.
[^11]: [[thomas-may-2022-mountain-counting](pages/thomas-may-2022-mountain-counting.md)] §3 p.78 L368-L374 - "We note that the sequence hm3,` i in the table has been shown in [2] to have the following ordinary generating function", (9) `x(1 − x)/(1 − 5x + 3x²)`, "whose coefficients happen to coincide with OEIS sequence A018902 [9]."
[^12]: [[thomas-may-2022-mountain-counting](pages/thomas-may-2022-mountain-counting.md)] §4 p.78 L376-L407 [synthesis] - "the size of the leaning matrix is exponential in the length of the mountain’s base"; "The problem of computing the generating functions for general classes of mountains is open."; "We conclude with a related problem suggested by Serban Raianu. Instead of arranging spheres in the base of a mountain in a rectangle as part of a square lattice, the spheres can also be arranged in a parallelogram as part of a hexagonal lattice. In this case the gravity rule becomes simpler—each sphere above the base must sit on just the three spheres immediately below it."
[^exec]: Verified by execution (Python 3.11, 2026-10-29): `bin/python/brick_wall_castles.py` items [1] and [8], run log `bin/python/brick_wall_castles-run.log`. The shear of every brick-wall castle of width `w ≤ 10` onto its slant heights, a bijection onto the sequences with `s_1 = 1` and `s_{k+1} ≤ s_k + 1` that keeps rows, height, blocks and cells; the table of `f_{w,s}` for `w ≤ 6` and the closed form `(s/w) C(2w − s − 1, w − s)` for `w ≤ 8`.
