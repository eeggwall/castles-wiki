---
title: "Height-2 castles = A038505 / A038503 (hyperbolic family)"
category: Sources
summary: The OEIS cross-reference of the mining pass. The castles of width w and height 2 with an even and with an odd number of blocks number A^e(w, 2) = A038505(w+1) and A^o(w, 2) = A038503(w+1) − 1, two of the four sums of every fourth binomial coefficient, and together 2^w − 1 = A000225(w). Both OEIS entries carry the castle comment and formulas through A000225, and A146559 = A038503 − A038505 ties in the signed tower count P(1, ·).
tags: [oeis, castle, height-2, hyperbolic, binomial, cross-reference, source]
sources: [oeis-mining-pe502]
created: 2026-09-13
updated: 2026-10-16
---

# Height-2 castles = A038505 / A038503 (hyperbolic family)

**Source:** `raw/oeis-pe502/oeis-xref-draft.md` (with `raw/oeis-pe502/mine-notes.md` §Vein 3)
**Date ingested:** 2026-09-13
**Type:** OEIS cross-reference record (A038503, A038505, A146559)

## Summary

The source records the identification of the castles of height 2, split by the parity of their block count, with two members of the [[hyperbolic-sequence-family](pages/hyperbolic-sequence-family.md)], and the edits to the OEIS entries that state it.[^1] It writes `F(w, 2)` and `odd(w, 2)` for the wiki's `A^e(w, 2)` and `A^o(w, 2)` ([[castle-notation](pages/castle-notation.md)]).

## The identity

A castle of width `w` and height 2 is given by the set of its columns of height 2, a binary string of length `w` with at least one 1. The bottom row is one block, and if the 1s form `r` runs, the castle has `1 + r` blocks. The binary strings of length `w` with `r` runs of 1s number `C(w+1, 2r)`, one for each choice of the `2r` run ends among the `w + 1` gaps between and around the columns. The block count is even exactly when `r` is odd, that is when `2r ≡ 2 (mod 4)`, so[^1]

```
A^e(w, 2)  =  Σ_{k≥0} C(w+1, 4k+2)  =  A038505(w+1)
A^o(w, 2)  =  Σ_{k≥1} C(w+1, 4k)    =  A038503(w+1) − 1
A(w, 2)    =  2^w − 1               =  A000225(w)
```

`A038505(n)` and `A038503(n)` are the sums of `C(n, j)` over `j ≡ 2` and over `j ≡ 0 (mod 4)`. In the offsets of the OEIS entries, `A038505(n) = A^e(n−1, 2)` for `n ≥ 2`, with `a(0) = a(1) = 0`, and `A038503(n) = A^o(n−1, 2) + 1` for `n ≥ 2`, with `a(0) = a(1) = 1`. The added 1 is the term `C(n, 0)`, the string with no 1s, which gives the flat row, a castle of height 1.[^2]

*Example: `w = 4`.* `A^e(4, 2) = C(5, 2) = 10 = A038505(5)`, the ten castles of the example on [[castle-counting-formula](pages/castle-counting-formula.md)], and `A^o(4, 2) = C(5, 4) = 5 = A038503(5) − 1`; together they are the `2^4 − 1 = 15` castles of width 4 and height 2.

## On the OEIS

Before the castle comments, both entries carried readings by trace and subtrace of binary strings over `Z_2` and over `GF(2)`, a matrix power `M^n` (Adamson), and the difference analog of the hyperbolic functions of order 4 (Shevelev); `A038505` also a binomial transform (Barry), and `A038503` generalized compositions (Janjic). `A000225` was in neither cross-reference list.[^3]

**A038503, the odd count.**[^4]

> a(n)-1 is the number of castle polyominoes of width n-1 and height 2 with an odd number of blocks (Project Euler, Problem 502: Counting Castles), for n >= 2. Here a castle is a stack of unit blocks on a grid, whose bottom row is a single block of length n-1, whose higher blocks have height 1 and rest on the blocks below without overhang, whose height is 2, and in which two neighboring blocks of the same row are separated by a gap. If the columns that reach height 2 form r >= 1 runs, the number of blocks is 1 + r, so an odd number of blocks means r is even.

**A038505, the even count.**[^5]

> a(n) is the number of castle polyominoes of width n-1 and height 2 with an even number of blocks (Project Euler, Problem 502: Counting Castles), for n >= 2. Here a castle is a stack of unit blocks on a grid, whose bottom row is a single block of length n-1, whose higher blocks have height 1 and rest on the blocks below without overhang, whose maximum height is 2, and in which two neighboring blocks of the same row are separated by a gap. If the columns that reach height 2 form r runs, the number of blocks is 1 + r, so an even number of blocks means r is odd.

`A038505` links to `https://projecteuler.net/problem=502` as "Project Euler, Problem 502: Counting Castles".[^5]

**Formulas.**[^4][^5][^6]

```
A038503:  a(n) = A000225(n−1) − A038505(n) + 1   for n ≥ 1
A038503:  a(n) = A038505(n) + A146559(n)
A038505:  a(n) = A000225(n−1) − A038503(n) + 1   for n ≥ 1
A146559:  a(n) = A038503(n) − A038505(n)
```

The two formulas through `A000225` both say `A038503(n) + A038505(n) = 2^{n−1}`, the sum of `C(n, j)` over even `j`; at `n = w + 1` this is the split `2^w = (A^o(w, 2) + 1) + A^e(w, 2)`. `A146559(n)` is the real part of `(1 + i)^n`, and `A146559(L + 1)` is the signed tower count `P(1, L)` ([[signed-tower-count](pages/signed-tower-count.md)]). Every formula holds for `n < 40`, and the three identities of the section *The identity* hold for `w ≤ 13` by enumeration of the castles.[^7]

**Cross-references.** `A000225` heads the `Cf.` lists of both entries, and the list of `A038503` also contains `A146559`.[^4][^5]

## Entities & Concepts

- [[hyperbolic-sequence-family](pages/hyperbolic-sequence-family.md)] - the four sums of every fourth binomial coefficient, `A038503`, `A038504`, `A038505`, `A000749`.
- [[castle-counting-function](pages/castle-counting-function.md)] - the counts `A^e(w, 2)` and `A^o(w, 2)` among the castle counts, with the width-3 example.
- [[signed-tower-count](pages/signed-tower-count.md)] - `P(1, L) = A146559(L + 1)` and `A146559 = A038503 − A038505`.
- [[block-count-constraints](pages/block-count-constraints.md)] - castles selected by block count, of which the height-2 even-block castles are the residue class read off `Σ_r C(w+1, 2r) z^r`.
- [[oeis-cross-referencing](pages/oeis-cross-referencing.md)] - the offset check and the short-prefix rule that this identification passes.
- [[new-sequence-fw3](pages/new-sequence-fw3.md)] - the row `A^e(·, 3)`, whose OEIS status is on [[castle-sequence-catalogue](pages/castle-sequence-catalogue.md)].
- [[project-euler-502](pages/project-euler-502.md)] - the problem that `A038505` links to.
- [[oeis-mining-seminar](pages/oeis-mining-seminar.md)] - a seminar whose stops 1 to 4 and 7 follow this identification from the table of counts to the OEIS edit.

## Relation to Other Wiki Pages

This identification is vein 3 of the mining pass on [[oeis-mining-pe502](pages/oeis-mining-pe502.md)].

## Footnotes

[^1]: raw/oeis-pe502/oeis-xref-draft.md §"0. Verified identities (offsets nailed)" L31-45 - "A castle of width w, height exactly 2 is a subset of columns reaching height 2 ... with at least one such column. The bottom row is one block; the number of blocks is 1 + r, where r = number of runs of height-2 columns", "#strings of length w with exactly r runs of 1's = binomial(w+1, 2r)", "Even block count <=> 1 + r even <=> r odd <=> 2r = 2 mod 4, so F(w,2) = A038505(w+1)", "odd(w,2) = A038503(w+1) - 1 = Sum_{k>=1} binomial(w+1, 4k)", "Total height-2 castles (any parity) = 2^w - 1 = A000225(w)".
[^2]: raw/oeis-pe502/oeis-xref-draft.md §"0. Verified identities (offsets nailed)" L47-52 - "A038505: a(n) = F(n-1, 2) for n >= 2, with a(0) = a(1) = 0", "A038503: a(n) = odd(n-1, 2) + 1 for n >= 2, with a(0) = a(1) = 1."
[^3]: raw/oeis-pe502/oeis-xref-draft.md §"1. What is already there (do NOT duplicate)" L56-81 [synthesis] - the existing comments (trace and subtrace over Z_2 and GF(2), Barry's binomial transform, Adamson's M^n, Shevelev's hyperbolic analog, Janjic's generalized compositions) and "(A000225 is missing.)" in both Cf. lists; confirmed against the live entries.
[^4]: https://oeis.org/A038503 (read 2026-10-16) - the comment quoted above (_Chaz Reid_, Sep 18 2026); %F "a(n) = A000225(n-1) - A038505(n) + 1 for n >= 1" and "a(n) = A038505(n) + A146559(n)"; %Y "Cf. A000225, A024493, A024494, A024495, A038505, A038504, A000749, A146559."
[^5]: https://oeis.org/A038505 (read 2026-10-16) - the comment quoted above (_Chaz Reid_, Sep 26 2026); %H "Project Euler, Problem 502: Counting Castles"; %F "a(n) = A000225(n-1) - A038503(n) + 1 for n >= 1"; %Y "Cf. A000225, A000749, A009116, A009545, A038503, A038504."
[^6]: https://oeis.org/A146559 (read 2026-10-16) - %F "a(n) = Re( (1+i)^n )" and "a(n) = A038503(n) - A038505(n). - _Chaz Reid_, Sep 26 2026".
[^7]: Verified by execution (Python 3.11, 2026-10-16): the four formulas and `A038503(n) + A038505(n) = 2^{n−1}` for `1 ≤ n < 40`; `A^e(w, 2)`, `A^o(w, 2)` and `A(w, 2)` against the enumeration of the castles of width `w ≤ 13` and height 2.
