---
title: "Counting Polyominoes in a Rectangle b × h (Marin, 2024)"
category: Sources
summary: Marin counts the fixed polyominoes inscribed in a w × h rectangle (a cell on every side, so the bounding box is exactly w × h) with a deterministic automaton that reads one row at a time. Its states are non-crossing labelings of a row's connected components plus two wall flags. At fixed width the count is rational in h; the paper derives the width-2 generating function, reports the degrees for widths 3-6, and gives a closed-form state count (A378947). Castles are the bargraph subclass of these polyominoes. Their strip needs h states, where the inscribed automaton needs A378947(h).
tags: [paper, source, polyomino, inscribed-polyomino, bounding-box, automaton, transfer-matrix, non-crossing-partition, catalan, motzkin, pell, generating-functions, oeis]
sources: [marin-2024-polyominoes-in-rectangle]
created: 2026-10-06
updated: 2026-10-06
---

# Counting Polyominoes in a Rectangle b × h (Marin, 2024)

**Source:** `raw/marin-2024-polyominoes-in-rectangle.pdf` (text layer at `raw/marin-2024-polyominoes-in-rectangle.txt`, extracted with `pdftotext -layout`; the PDF is git-ignored, the text is tracked). arXiv:2406.16413v1; published in S. Brlek and L. Ferrari (eds.), GASCom 2024, EPTCS 403, 2024, pp. 145-149, doi:10.4204/EPTCS.403.30.[^1]
**Author:** Louis Marin (UQAM, LaCIM).[^1]
**Date ingested:** 2026-10-06
**Type:** paper (PDF, 5 pp., extended abstract)

**Notation.** The paper writes `b` for the width. This page writes `w`, as everywhere on the wiki, and keeps `h` for the height. `I(w, h)` is the number of inscribed polyominoes, and `G_w(x) = Σ_{h ≥ 0} I(w, h) x^h` is its generating function in the height, with `I(w, 0) = 1`. The automaton is written `𝒜_w` (script), because plain `A(w, h)` is the castle count ([[castle-notation](pages/castle-notation.md)]).

## Summary

A polyomino is **inscribed** in a `w × h` rectangle when it lies inside the rectangle and has at least one cell on each of its four sides.[^2] Equivalently, its bounding box is exactly `w × h`. The counts are the OEIS table A292357 ("fixed polyominoes that have a width of m and height of n"), and its width-2, -3 and -4 columns are A034182, A034184 and A034187.[^2] For fixed `w` the count satisfies a linear recurrence in `h`. At `w = 2` this has a short combinatorial proof. At `w = 3, 4` the recurrences were known only empirically, without proof.[^3] The paper builds, for every `w`, a finite automaton that reads the polyomino one row at a time. Rationality of `G_w` follows, and `G_w` can be computed from the automaton.[^4]

**The automaton 𝒜_w.** The construction adapts Zeilberger's transfer-matrix method and the methods surveyed by Bousquet-Mélou and Brak.[^4] A row is a word `u ∈ {0, 1}^w` with at least one `1`, where `1` marks a cell of the polyomino, and the automaton reads the rows from top to bottom.[^5] A state is a triple: a word `v ∈ {0, 1, …, ⌈w/2⌉}^w` plus two booleans, the *left flag* and the *right flag*. The word `v` labels each cell of the last row read with `0` (empty) or with the number of the connected component the cell belongs to in the part of the polyomino read so far. Components are numbered left to right. Each flag records whether the polyomino has yet touched that wall.[^6] The states are restricted as follows:[^7]

- **Start.** The all-zero word occurs only as the initial state, with both flags false.
- **Inscription.** A cell in the first (last) column sets the left (right) flag.
- **Separation.** Two horizontally adjacent occupied cells of `v` carry the same label.
- **Non-crossing.** For positions `1 ≤ i < k < j < l ≤ w`, if `v_i = v_j ≠ 0` and `v_k = v_l ≠ 0`, then all four labels are equal. Two distinct components cannot interleave along the row, since they would have to cross above it.
- **Renaming.** Words that differ only by a permutation of the nonzero labels are the same state, and the lexicographically least word represents it.[^8]

A transition on row `u` is allowed only if every component of `v` has a cell directly below it in `u`. A component that lost all its cells could never be reconnected.[^9] A cell of `u` under a labelled cell inherits its label, and a cell of `u` under an empty cell gets a fresh label. Every maximal horizontal run of `1`s in `u` then merges all the labels it contains, and the merges are closed transitively. The merged components are renumbered left to right. The left flag becomes `left ∨ u_1` and the right flag becomes `right ∨ u_w`.[^10] A state accepts when it has a single component (`v ∈ {0, 1}^w`) and both flags are true.[^11] Each step is determined, so `𝒜_w` is deterministic. Theorem 1 says that the accepted stacks of `h` rows are in bijection with the polyominoes inscribed in `w × h`.[^12] The paper's Figure 1 traces a 5 × 9 example through `𝒜_5`.[^13]

**Results.** The width-2 generating function is[^3]

```
G_2(x)  =  (1 − 2x + 3x² + 2x³) / ((1 − x)(1 − 2x − x²)).
```

The paper computes `G_w` for `w = 3, 4, 5, 6` but does not print them. As rational functions they have degree 9, 20, 49 and 112. For `w = 3, 4` it also computes the area generating functions, which count inscribed polyominoes of `w × h` by their number of cells.[^14] The automaton for `w = 7` was built, but its generating function was not yet extracted.[^15] The number of states is[^16]

```
#states(𝒜_w)  =  1 + Σ_{n=1}^{2^w − 1}  C_{f(n)} · 2^[n even] · 2^[n < 2^{w−1}],
```

where `C_m` is the `m`-th Catalan number, `f(n)` is the number of runs of `1`s in the binary expansion of `n` (A069010), and `[·]` is 1 when the condition holds and 0 otherwise. Here `n` reads a row's occupancy as a binary number. For that occupancy, `C_{f(n)}` counts the non-crossing ways to group its runs into components, and each factor 2 is a wall flag that the end cells leave undetermined. The values for `w = 0, …, 11` are 1, 2, 6, 16, 40, 99, 247, 625, 1605, 4178, 11006, 29292.[^17] This is OEIS A378947, which also gives the Motzkin form `M_{w+1} + 2M_w + M_{w−1} − 3` for `w > 0`, with `M_n` the Motzkin numbers (A001006). The same entry notes that the state count bounds the order of `G_w`.[^18] The paper cites A140662, which counts the column states of an automaton for self-avoiding polygons in a slit of width `n`, as a related state count.[^17]

**Checks.** An independent implementation of `𝒜_w` reproduces all of the following:[^exec]

- the formula's state counts as the reachable states for `w = 1..7`;
- the OEIS columns A034182, A034184 and A034187;
- the rational-function degrees 9, 20 and 49 for `w = 3, 4, 5`.

It also gives the width-3 function that the paper leaves out:

```
G_3(x)  =  (1 − 9x + 38x² − 51x³ + 10x⁴ + 29x⁵ − 38x⁶ + 7x⁷ + 5x⁸)
           / ((1 − x)(1 − 2x − x²)(1 − 7x + 11x² − 6x³ − x⁴ + 7x⁵ − x⁶)),
```

with coefficients 1, 1, 15, 111, 649, 3495, 18189, … (A034184). The sextic factor is irreducible, and `I(3, h)` grows like `≈ 5.0566^h`. The denominator of `G_2` divides the denominator of `G_3`.[^exec]

## Key Takeaways

- **Castles are inscribed polyominoes.** A castle of width `w` and exact height `h` has a full bottom row, which touches the bottom, left and right sides, and a column at height `h`, which touches the top. So every castle is inscribed in its `w × h` rectangle: the castles are the bargraphs among the inscribed polyominoes, and `A(w, h) = h^w − (h−1)^w ≤ I(w, h)` ([[castle-polyomino](pages/castle-polyomino.md)], [[inscribed-polyomino](pages/inscribed-polyomino.md)]). At `w = h = 3` there are 19 castles among 111 inscribed polyominoes.[^exec]
- **The state counts show what the castle rules save.** By transposition `I(w, h) = I(h, w)`, so `𝒜_h`, read along columns, counts at fixed height and growing width, the PE 502 orientation. It needs A378947(h) states: 99 at `h = 5` and 29,292 at `h = 11`.[^17] The castle strip needs only `h` states, one per column height ([[castle-strip](pages/castle-strip.md)]). Every castle column is one vertical run standing on the full base row, so it is connected to everything else through row 1, and no component labels are needed.
- **Width 2 is Pell-Lucas.** `I(2, h) = Q_{h+1} − 2`, where `Q_n` are the Pell-Lucas numbers (A001333), and the growth rate is the silver mean `1 + √2`. OEIS states this identity on A034182 ([[pell-numbers](pages/pell-numbers.md)]).[^19]
- **Rationality comes with a proof.** For `w = 3, 4` the recurrences had been found from data. The automaton proves that a recurrence exists for every `w` and computes it. On the castle side, the solver's Berlekamp-Massey path uses the same split: the data find the recurrence, and a transfer-matrix argument justifies that one exists ([[castle-count-algorithms](pages/castle-count-algorithms.md)]).[^3]

## Entities & Concepts

- [[inscribed-polyomino](pages/inscribed-polyomino.md)] - the counted object, the A292357 table, and castles as its bargraph subclass.
- [[castle-polyomino](pages/castle-polyomino.md)] - the castle, an inscribed bargraph.
- [[castle-strip](pages/castle-strip.md)] - the `h`-state transfer matrix that column-convexity allows, against A378947(h) states here.
- [[polyominoes](pages/polyominoes.md)], [[convex-polyomino](pages/convex-polyomino.md)] - the polyomino taxonomy; every convex polyomino is inscribed in its bounding box.
- [[catalan-numbers](pages/catalan-numbers.md)], [[motzkin-numbers](pages/motzkin-numbers.md)] - the non-crossing component partitions in the state count, and its Motzkin form.
- [[pell-numbers](pages/pell-numbers.md)] - the width-2 count.
- [[castle-count-algorithms](pages/castle-count-algorithms.md)] - recurrences found from data and justified by a transfer matrix.

## Relation to Other Wiki Pages

The paper supplies the ambient count for the castle. Castles of width `w` and exact height `h` sit inside the `w × h` entry of A292357 as its bargraphs. The table on [[inscribed-polyomino](pages/inscribed-polyomino.md)] puts the two counts side by side. The comparison of state spaces makes concrete why the castle strip is small: connectivity, the expensive part of `𝒜_w`, is automatic for skylines on a full base. The automaton is the general form of the wiki's strip transfer matrices. Its states carry a non-crossing partition and boundary flags where a strip state carries one column height. None of the paper's numbers conflicts with the wiki's castle counts, because the paper does not count castles.

## Footnotes

[^1]: [[marin-2024-polyominoes-in-rectangle](pages/marin-2024-polyominoes-in-rectangle.md)] p.145 title block L1-6, L47-49 - "Counting Polyominoes in a Rectangle b × h", "Louis Marin", "UQAM LACIM", "S. Brlek and L. Ferrari (Eds.): GASCom 2024", "EPTCS 403, 2024, pp. 145–149, doi:10.4204/EPTCS.403.30".
[^2]: [[marin-2024-polyominoes-in-rectangle](pages/marin-2024-polyominoes-in-rectangle.md)] p.145 §1 L15-20 - "By inscribed, we mean a polyomino that is included in a rectangle of size b × h and that has at least one cell touching each side of the rectangle"; "The sequences for b = 2, 3, 4 are registered on the Online Encyclopedia of Integer Sequences (OEIS) (A034182 [3], A034184 [3] and A034187 [3], respectively)"; A292357 for the further values. A292357's name is from https://oeis.org/A292357 (fetched 2026-10-06).
[^3]: [[marin-2024-polyominoes-in-rectangle](pages/marin-2024-polyominoes-in-rectangle.md)] p.145 §1 L17-28 [synthesis] - "If we fix b and increase h, the number of inscribed polyominoes satisfies a linear recurrence"; the b = 2 recurrence "can be proved using simple combinatorial argument", with `G_2 = (2x³ + 3x² − 2x + 1)/((x − 1)(x² + 2x − 1))` (rewritten here with both factors negated); "Recurrences for b = 3, 4 have been discovered empirically but, to the best of our knowledge, no proof seems to be available."
[^4]: [[marin-2024-polyominoes-in-rectangle](pages/marin-2024-polyominoes-in-rectangle.md)] p.145 §1 L29-32 - "we show how we obtained the formulas for b = 3, 4, 5, 6 and we design a method for obtaining the formulas for any b. To do so, we adapt methods described in previous works by Zeilberger [4] and by Bousquet-Mélou and Brak [1] in order to build an automaton A_b recognizing exactly the polyominoes inscribed in a rectangle of fixed width b and any height h."
[^5]: [[marin-2024-polyominoes-in-rectangle](pages/marin-2024-polyominoes-in-rectangle.md)] pp.145-146 §2 L36-44, L54 [synthesis] - a row configuration is "a unique word u ∈ {0, 1}^b, |u|_1 > 0"; a stack of h such words encodes a unique polyomino; the automaton "operates by reading the stack of words from top to bottom".
[^6]: [[marin-2024-polyominoes-in-rectangle](pages/marin-2024-polyominoes-in-rectangle.md)] p.146 §2 L54-64 [synthesis] - the alphabet extended to {0, 1, …, ⌈b/2⌉}, a cell labelled "with the value i ... if the cell belongs to the i-th connected component of the polyomino, where the connected components are labeled with increasing values from left to right"; two booleans for whether "the leftmost (resp. rightmost) column has at least one selected cell"; states `(w, l, r)`.
[^7]: [[marin-2024-polyominoes-in-rectangle](pages/marin-2024-polyominoes-in-rectangle.md)] p.146 §2 L66-78 [synthesis] - the four conditions Empty row, Inscription, Separation and Non-crossing defining the set of admissible triplets; non-crossing "comes from the fact that two distinct connected components cannot have crossed earlier in P". Stated here over cell positions `1..w` and nonzero labels.
[^8]: [[marin-2024-polyominoes-in-rectangle](pages/marin-2024-polyominoes-in-rectangle.md)] p.146 §2 L79-89 [synthesis] - the words 10201 and 20102 represent the same configuration; `w ≡ w′` when the zero positions agree and a permutation of `{1, …, ⌈b/2⌉}` carries the label classes of one to the other; the representative is "the minimum element with respect to the lexicographic order".
[^9]: [[marin-2024-polyominoes-in-rectangle](pages/marin-2024-polyominoes-in-rectangle.md)] p.147 §2 L101-103 - the transition is defined only when "|Pos_a(w)| > 0 implies Pos_a(w) ∩ Pos_1(u) ≠ ∅. This ensures that, in the polyomino P, no connected component is 'lost'."
[^10]: [[marin-2024-polyominoes-in-rectangle](pages/marin-2024-polyominoes-in-rectangle.md)] p.147 §2 L110-143 [synthesis] - Vertical connexity (inherit the label above, else a new label `N + 1`), Horizontal connexity (horizontally connected components "directly linked if they share a letter", transitive closure, letters assigned left to right), Adjacency "l′ = l ∨ u_1 and r′ = r ∨ u_b"; Example 1 with `w = 10203020104`, `u = 10111011101` giving `w′ = 10111011102`.
[^11]: [[marin-2024-polyominoes-in-rectangle](pages/marin-2024-polyominoes-in-rectangle.md)] p.147 §2 L99-100 - a state is accepting "if and only if it has a single connected component (i.e. w ∈ {0, 1}^b) and is inscribed in the rectangle (i.e. l = r = T)".
[^12]: [[marin-2024-polyominoes-in-rectangle](pages/marin-2024-polyominoes-in-rectangle.md)] p.148 §2 L147-150 - "every step in the construction of A_b is automatic and δ_b is unambiguous. A_b is thus deterministic. Theorem 1. The set of stacks of size h of words recognized by A_b is in bijection with the set of polyominoes inscribed in a rectangle of size b × h."
[^13]: [[marin-2024-polyominoes-in-rectangle](pages/marin-2024-polyominoes-in-rectangle.md)] p.148 Figure 1 L151-166 - "a stack of length 9 recognized by A_5 and the associated polyomino", with the states visited from (00000,F,F) to (11101,T,T).
[^14]: [[marin-2024-polyominoes-in-rectangle](pages/marin-2024-polyominoes-in-rectangle.md)] p.148 §3 L175-179 - "we computed the generating functions G_b for b = 3, 4, 5, 6. We also could compute G′_b for b = 3, 4 where G′_b is the generating function for the number of polyominoes of area n inscribed in a rectangle of size b × h ... G_3 is of degree 9, G_4 is of degree 20, G_5 is of degree 49 and G_6 is of degree 112."
[^15]: [[marin-2024-polyominoes-in-rectangle](pages/marin-2024-polyominoes-in-rectangle.md)] p.148 §3 L180-182 - "The case b = 7 was generated but the calculations to produce the generating function still need to be done."
[^16]: [[marin-2024-polyominoes-in-rectangle](pages/marin-2024-polyominoes-in-rectangle.md)] p.148 §3 eq. (1) L182-191 [synthesis] - the state-count formula with "C_m is the m-th Catalan number, f(k) is the number of runs of 1's in the binary expansion of k (A069010 [3])" and the indicator function; summation index renamed `n` here. The reading of each factor is this wiki's, confirmed by the reachable-state check in [^exec].
[^17]: [[marin-2024-polyominoes-in-rectangle](pages/marin-2024-polyominoes-in-rectangle.md)] pp.148-149 §3 L192-193 and Figure 2 L199-202 - "the sequence A140662 [3], also counting states in an automaton recognizing polyominoes"; the table "number of states in A_b" `1, 2, 6, 16, 40, 99, 247, 625, 1605, 4178, 11006, 29292` for `b = 0, …, 11`.
[^18]: https://oeis.org/A378947 (fetched 2026-10-06) - "Number of row states in an automaton for the enumeration of the number of fixed polyominoes with bounding box of width n"; formula "a(n) = A001006(n+1) + 2*A001006(n) + A001006(n-1) - 3 for n > 0" (Andrew Howroyd); comment "a(n) is an upper bound on the order of the generating function of row n of A292357."
[^19]: https://oeis.org/A034182 (fetched 2026-10-06) - "a(n) = A001333(n+1)-2" (R. J. Mathar) and "G.f.: x*(1+x)^2/((1-x)*(1 - 2*x - x^2))"; the same g.f. as `G_2 − 1`.
[^exec]: Verified by execution (2026-10-06). An independent implementation of `𝒜_w`, using union-find over the labels of each run and canonical relabelling, reached exactly 2, 6, 16, 40, 99, 247, 625 states for `w = 1..7`, matching eq. (1). Its counts `I(w, h)` match a brute-force enumeration of connected cell sets touching all four sides (`w = 2`, `h ≤ 6`; `w = 3`, `h ≤ 5`) and the OEIS data of A034182, A034184 and A034187. Minimal recurrences fitted to 40-130 terms give `G_w` as rational functions of numerator / denominator degree 3/3, 8/9, 20/20 and 48/49 for `w = 2, 3, 4, 5`. `G_3` is the function displayed above; its series matches A034184. The growth rate is the reciprocal of the smallest root of the sextic factor. Castle counts `A(w, h) = h^w − (h−1)^w` were compared against `I(w, h)` for `w, h ≤ 5`.
