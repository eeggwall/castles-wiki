---
title: "OEIS mining of PE 502 castles (first pass)"
category: Sources
summary: The first pass at matching castle counts against the OEIS, organized in veins. Matches - P(1, L) = A146559(L+1); A(·, h) = A000225, A001047, A005061, A005060, A005062; A^e(w, 2) = A038505(w+1) and A^o(w, 2) = A038503(w+1) − 1; the convex count C(2h+w−3, w−1); the tower block-count rows A005408, A005891, A063490, A160747; and by area A001523 (convex), A332578 (valley), A115981 (non-convex).
tags: [oeis, castle, research, mining, cross-reference, source]
sources: [oeis-mining-pe502]
created: 2026-09-13
updated: 2026-10-23
---

# Online Encyclopedia of Integer Sequences (OEIS) mining of Project Euler 502 (PE 502) castles (first pass)

**Source:** `raw/oeis-pe502/` (research notes, chiefly `README.md`, `mine-notes.md`, `crosslink-avenues.md`, `vein9-area.md` and `vein9b-concave.md`, with the tables `tables.json` and `terms_50.txt`)
**Date ingested:** 2026-09-13
**Type:** research notes with computed tables

> **See also:** [[oeis-index](pages/oeis-index.md)] - every A-number cited on the wiki and the pages that cite it; [[castle-sequence-catalogue](pages/castle-sequence-catalogue.md)] - the castle sequences with their terms and the entries they equal.

## Summary

The notes match counts of the [[castle-polyomino](pages/castle-polyomino.md)] against the OEIS: for each count they look for an existing A-number with the same terms.[^1] Every accepted match was checked against the OEIS data with offsets, not only its first terms; this is how the notes tell the real part of `(1+i)^n`, `A146559`, from the imaginary part, `A009545`.[^2] The search over a rectangle of `(w, h)` is the use of the enumerator that [[project-euler-502-brute-force](pages/project-euler-502-brute-force.md)] proposes.

The notes are organized in **veins**, each a family of castle counts and the sequences it reaches. They number the veins 1 to 4, 7, 8, 9 and 9b; there are no veins 5 and 6.[^3] The notes write `F(w, h)` and `odd(w, h)` for the wiki's `A^e(w, h)` and `A^o(w, h)`, and "exact height" for height.

- **Vein 1, the signed tower count.** `P(1, L) = Re((1+i)^{L+1}) = A146559(L+1)`, and `A009545(n) = Im((1+i)^n)`. For each `k`, `P(k, ·)` satisfies a linear recurrence of order `k + 1` ([[signed-tower-count](pages/signed-tower-count.md)]).[^4]
- **Vein 2, all castles.** `A(w, h) = h^w − (h−1)^w` is `A000225` (`2^n − 1`) at `h = 2`, `A001047` (`3^n − 2^n`) at `h = 3`, and `A005061`, `A005060`, `A005062` at `h = 4, 5, 6`.[^5]
- **Vein 3, even-block castles.** At height 2, `A^e(w, 2) = A038505(w+1) = Σ_j C(w+1, 4j+2)` ([[oeis-height2-hyperbolic-castles](pages/oeis-height2-hyperbolic-castles.md)], [[hyperbolic-sequence-family](pages/hyperbolic-sequence-family.md)]). For `h ≥ 3` the rows `A^e(·, h)` satisfy linear recurrences of orders 6, 9 and 11 at `h = 3, 4, 5`, with characteristic polynomial `(x − 3)(x − 2)(x² − x + 2)(x² − 2x + 2)` at `h = 3`. For `w = 3, 4, 5` the columns `A^e(w, ·)` have characteristic polynomial `(x² − 1)^w`.[^6]
- **Vein 4, convex castles.** A castle is convex exactly when its skyline is unimodal, and exactly when it has `h` blocks, the least possible. The convex castles of width `w` and height `h` number `C(2h+w−3, w−1)`: `C(w+1, 2)` (`A000217`) at `h = 2` and `C(w+3, 4)` (`A000332`) at `h = 3` ([[convex-castle-binomial-identity](pages/convex-castle-binomial-identity.md)]).[^7]
- **Vein 7, block-count distributions.** Towers of height at most 1 on a base of length `w` with `b` blocks number `C(w+1, 2b)`, the triangle `A034839`. For castles of height `h ≥ 2` the column of minimum block count `h` of the block-count distribution is the convex count `C(2h+w−3, w−1)`.[^8] Over towers of any height, the number `T(w, b)` of towers on a base of length `w` with `b` blocks is `Σ_k N(w, k) C(b+w−k, w−1)`, with `N(w, k)` the Narayana numbers; its rows `w = 2, 3, 4, 5` are `A005408`, `A005891`, `A063490` and `A160747` ([[tower-narayana-polynomial](pages/tower-narayana-polynomial.md)], [[tower-heap](pages/tower-heap.md)]).[^9]
- **Vein 8, odd-block castles.** `A^o(w, 2) = A038503(w+1) − 1 = Σ_{j≥1} C(w+1, 4j)`. For `h = 3, 4, 5` the rows `A^o(·, h)` satisfy linear recurrences of orders 5, 9 and 11.[^10]
- **Veins 9 and 9b, castles by area.** A castle of area `n` is a composition of `n`, so all castles of area `n` number `2^{n−1}`. The convex castles of area `n` are the weakly unimodal compositions of `n`, `A001523(n)`; the valley castles, which weakly fall and then weakly rise, are `A332578(n)`; and the non-convex castles are `A115981(n) = A011782(n) − A001523(n)` ([[castle-by-area](pages/castle-by-area.md)], [[weakly-unimodal-composition](pages/weakly-unimodal-composition.md)]).[^11]

## Results of the first pass

| Count | OEIS | Result |
|---|---|---|
| `P(1, L)` | `A146559(L+1)`; `A009545` is the imaginary part of `(1+i)^n` | match |
| `A(w, h)` at `h = 2, …, 6` | `A000225`, `A001047`, `A005061`, `A005060`, `A005062` | match |
| `A^e(w, 2)` | `A038505(w+1)` | match |
| `A^o(w, 2)` | `A038503(w+1) − 1` | match |
| convex castles of width `w` and height `h` | `C(2h+w−3, w−1)` | binomial coefficients |
| towers of height at most 1 by blocks | `A034839` | match |
| towers by blocks, rows `w = 2, …, 5` | `A005408`, `A005891`, `A063490`, `A160747` | match |
| convex castles by area | `A001523(n)` | match |
| valley castles by area | `A332578(n)` | match |
| non-convex castles by area | `A115981(n)` | match |
| all castles by area | `A000079(n−1) = 2^{n−1}` | match |


## Key facts

- At height 2 the castles of width `w` stand on the nonzero binary strings of length `w`, and the strings with `r` runs of 1s number `C(w+1, 2r)`. The castle has `r + 1` blocks, so the even-block castles are those with `r` odd, and `2^w − 1 = A^e(w, 2) + A^o(w, 2)` splits into two of the sums of every fourth binomial coefficient.[^12]
- Every castle of height `h` has at least `h` blocks, with equality exactly for the unimodal ones. So the convex castles of height `h` all have the parity of `h`, and the even-block convex castles number `C(2h+w−3, w−1)` for even `h` and 0 for odd `h`.[^7]
- The convex count is a binomial coefficient, and the Narayana numbers appear in the block count of towers.[^9]

All identities on this page agree with enumeration and with the OEIS data.[^13]

## Entities & Concepts

- [[oeis-cross-referencing](pages/oeis-cross-referencing.md)] - matching counts against the OEIS with offsets.
- [[signed-tower-count](pages/signed-tower-count.md)] - `P(k, L)` and the row `P(1, ·)`.
- [[hyperbolic-sequence-family](pages/hyperbolic-sequence-family.md)] - the four sums of every fourth binomial coefficient, `A038503`, `A038504`, `A038505` and `A000749`.
- [[oeis-height2-hyperbolic-castles](pages/oeis-height2-hyperbolic-castles.md)] - the castles of height 2 in `A038505`, `A038503` and `A146559`.
- [[convex-castle](pages/convex-castle.md)] and [[convex-castle-binomial-identity](pages/convex-castle-binomial-identity.md)] - the convex castles and the proof of `C(2h+w−3, w−1)`.
- [[tower-narayana-polynomial](pages/tower-narayana-polynomial.md)], [[tower-heap](pages/tower-heap.md)] and [[narayana-numbers](pages/narayana-numbers.md)] - the block count of towers through the Narayana numbers.
- [[castle-by-area](pages/castle-by-area.md)] and [[weakly-unimodal-composition](pages/weakly-unimodal-composition.md)] - castles counted by area.
- [[castle-counting-function](pages/castle-counting-function.md)] and [[castle-counting-formula](pages/castle-counting-formula.md)] - the counts `A`, `A^e`, `A^o` and the closed form.
- [[new-sequence-fw3](pages/new-sequence-fw3.md)] - the row `A^e(·, 3)`: `0, 0, 3, 21, 89, 307, 977, 3031, …`.

## Footnotes

[^1]: raw/oeis-pe502/README.md §"OEIS mining workspace" L3-6 - "take the Project Euler 502 \"castle\" object (a real, third-party combinatorial object) and find the existing A-numbers whose integers its counts reproduce."
[^2]: raw/oeis-pe502/mine-notes.md §"Method notes (interlinking discipline)" L177-179 - "Every accepted match above was checked against the actual OEIS data with offsets, not just the first few terms. The plan's own \"A009545\" was caught this way (real vs imaginary)."
[^3]: raw/oeis-pe502/mine-notes.md [synthesis] L19-150 - the sections "Vein 1", "Vein 2", "Vein 3", "Vein 4", "Vein 7", "Vein 8", "Vein 9" and "Vein 9b".
[^4]: raw/oeis-pe502/mine-notes.md §"Vein 1" L21-37 - "A009545 is the *imaginary* part of (1+i)^n", "P(1,L) = Re((1+i)^{L+1}) = A146559(L+1)", "The general P(k,·) family is C-finite of order k+1".
[^5]: raw/oeis-pe502/mine-notes.md §"Vein 2" L41-46 - "h=2 -> A000225 (2^w - 1, Mersenne) h=3 -> A001047 (3^w - 2^w) h=4 -> A005061 (4^w - 3^w) h=5 -> A005060 (5^w - 4^w) h=6 -> A005062 (6^w - 5^w)".
[^6]: raw/oeis-pe502/mine-notes.md §"Vein 3" L55-79 - "F(w,2) = A038505(w+1) = sum_k C(w+1, 2+4k)", "F(w,3): order 6, (x-3)(x-2)(x^2-x+2)(x^2-2x+2)", "F(w,4): order 9", "F(w,5): order 11", and "(Observed: F(3,h) order 6, F(4,h) order 8, F(5,h) order 10.)" with "annihilated by (x^2-1)^w".
[^7]: raw/oeis-pe502/mine-notes.md §"Vein 4" L83-97 - "every convex castle of height h has EXACTLY h blocks", "#blocks >= h with equality iff convex", "convex(w,h) = C(2h + w - 3, w - 1)", "h=2 -> C(w+1,2) = A000217", "h=3 -> C(w+3,4) = A000332", "the even-parity convex count = convex(w,h) if h even, else 0".
[^8]: raw/oeis-pe502/mine-notes.md §"Vein 7" L105-109 - "Height-<=1 towers (binary strings), b = #runs of 1s: count = C(w+1, 2b) = A034839", "its first (minimum) column is the convex count C(2h+w-3,w-1)."
[^9]: raw/oeis-pe502/crosslink-avenues.md §"Tier 2" L36-56 - "T(w,b) = # towers of width w with exactly b blocks = sum_{k=1..w} Narayana(w,k) * C(b + w − k, w − 1)", with the rows "A005408 (odd numbers)", "A005891 (centered pentagonal)", "A063490", "A160747" for `w = 2, …, 5`.
[^10]: raw/oeis-pe502/mine-notes.md §"Vein 8" L113-114 - "odd(w,2) = A038503(w+1) - 1 (above)", "odd(w,3) order 5, odd(w,4) order 9, odd(w,5) order 11".
[^11]: raw/oeis-pe502/mine-notes.md §"Vein 9" and §"Vein 9b" L118-145 - "conv(n) = A001523(n) for n >= 1", "all(n) = 2^(n-1)", "valley(n) = A332578(n)", "nonconv(n) = A115981(n) ... = A011782(n) − A001523(n)".
[^12]: raw/oeis-pe502/mine-notes.md §"Vein 3" L55-68 - "total = A000225(w) = 2^w - 1", "These are two of the four order-4 \"hyperbolic\" sequences {A038503, A038504, A038505, A000749}", "the number of width-w binary strings with exactly r runs of 1's is C(w+1, 2r). Even blocks <=> r odd".
[^13]: Verified by execution (Python 3.11 with SymPy, 2026-10-16) and against oeis.org (read 2026-10-16): `A^e(w, 2)` and `A^o(w, 2)` by enumeration for `w ≤ 10`; the minimal recurrences of `A^e(·, h)` and `A^o(·, h)` for `h = 2, …, 5` and of the columns `A^e(w, ·)` for `w = 3, 4, 5`, by Berlekamp-Massey on 40 or more terms; `blocks ≥ h` with equality exactly for unimodal skylines, for `w ≤ 6`, `h ≤ 4`; `C(2h+w−3, w−1)` for `w ≤ 7`, `h ≤ 5`; `T(w, b)` against enumeration of towers for `w ≤ 6`, `b ≤ 7`; the counts by area of convex, valley, non-convex and strict-valley castles for `n ≤ 15`; the names and terms of `A000225`, `A001047`, `A005061`, `A005060`, `A005062`, `A034839`, `A005408`, `A005891`, `A063490`, `A160747`, `A001523`, `A332578`, `A115981`, `A011782`, `A000079`, `A000217`, `A000332`, `A038503`, `A038504`, `A038505`, `A000749`, `A009545` and `A146559`.
