---
title: OEIS cross-referencing (interlinking method)
category: Concepts
summary: The wiki's method for relating castle counts to the OEIS. A count that reproduces an existing entry at a stated offset is an interlink, a new reading of a known sequence. Matches are checked against the entry's data with its offset, and agreement on a short prefix is not a match.
tags: [concept, oeis, method, cross-reference, research-workflow]
sources: [oeis-encyclopedia]
created: 2026-09-13
updated: 2026-10-25
---

# Online Encyclopedia of Integer Sequences (OEIS) cross-referencing (interlinking method)

## Description

The wiki relates the counting sequences of castles ([[castle-polyomino](pages/castle-polyomino.md)]) to the On-Line Encyclopedia of Integer Sequences, the OEIS, by interlinking: a castle count that reproduces the data of an existing entry, at a stated offset, gives that sequence a castle reading. For example, the castles of width `w` and height 2 with an even number of blocks number `A038505(w+1)` ([[oeis-height2-hyperbolic-castles](pages/oeis-height2-hyperbolic-castles.md)]).

[[castle-sequence-catalogue](pages/castle-sequence-catalogue.md)] lists every castle sequence on the wiki with the entry it equals, and [[oeis-mining-pe502](pages/oeis-mining-pe502.md)] collects the castle counts matched to OEIS entries, with their offsets.

## Checks

Two checks decide whether a match is an interlink.

- **The offset.** A match is checked against the entry's data and offset, not against a few leading terms. The signed tower count `P(1, L)` agrees with `A009545`, the imaginary parts of `(1+i)^n`, only after a shift and a factor 2, `P(1, L) = A009545(L+3)/2`; the entry it equals is `A146559`, the real parts, with `P(1, L) = A146559(L+1)` ([[signed-tower-count](pages/signed-tower-count.md)]).[^1]
- **Short prefixes.** Agreement on a few terms with no combinatorial reason is not a match. A search on the first terms of the anchored 1-smooth castles of height 4 returns `A378383`, the subwords `UDDD` in nondecreasing Dyck paths, which agrees through width 10 and differs at width 11, where the castles number 5205 and A378383 has 5206 ([[1-smooth-castles](pages/1-smooth-castles.md)]).[^2]


## Appearances in Sources

- [[oeis-encyclopedia](pages/oeis-encyclopedia.md)] - the entries `A146559`, `A009545` and `A378383` of the two checks.

## Related Concepts

- [[castle-sequence-catalogue](pages/castle-sequence-catalogue.md)] - every castle sequence with its terms and the entry it equals, at the stated offset.
- [[oeis-index](pages/oeis-index.md)] - the generated directory of every A-number cited on the wiki, with the citing pages.
- [[signed-tower-count](pages/signed-tower-count.md)] - `P(1, L) = A146559(L+1)` and `P(1, L) = A009545(L+3)/2`, the offset example.
- [[oeis-height2-hyperbolic-castles](pages/oeis-height2-hyperbolic-castles.md)] - the height-2 identities `A^e(w, 2) = A038505(w+1)` and `A^o(w, 2) = A038503(w+1) − 1`.
- [[castle-by-area](pages/castle-by-area.md)], [[hyperbolic-sequence-family](pages/hyperbolic-sequence-family.md)], [[narayana-numbers](pages/narayana-numbers.md)] - families of castle counts matched to OEIS entries.
- [[oeis-mining-seminar](pages/oeis-mining-seminar.md)] - a seminar that takes one sequence through the method.
- [[oeis-mining-pe502](pages/oeis-mining-pe502.md)] - the castle counts matched to OEIS entries, with their offsets.

## Footnotes

[^1]: https://oeis.org/A146559 (read 2026-10-25) - "(1+i)^n = a(n) + A009545(n)*i where i = sqrt(-1)."; https://oeis.org/A009545 (read 2026-10-25) - "Imaginary part of (1+i)^n."; verified by execution (Python 3.11 with SymPy, 2026-10-25): `Re((1+i)^{L+1}) = Im((1+i)^{L+3})/2` for `L ≤ 19`.
[^2]: https://oeis.org/A378383 (read 2026-10-25) - "Number of subwords of the form UDDD in nondecreasing Dyck paths of length 2*n.", data "0,0,0,1,5,19,64,202,612,1803,5206,14809"; verified by execution (Python 3.11, 2026-10-25): the anchored 1-smooth castles of height 4 for the widths 4 to 11 number 1, 5, 19, 64, 202, 612, 1803, 5205.
