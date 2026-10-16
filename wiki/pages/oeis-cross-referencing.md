---
title: OEIS cross-referencing (interlinking method)
category: Concepts
summary: The wiki's method for relating castle counts to the OEIS. A count that reproduces an existing entry at a stated offset is an interlink (a new reading of a known sequence); a count with no match in a dated search is recorded as such on castle-sequence-catalogue. Matches are checked against the entry's data with its offset, and agreement on a short prefix is not a match.
tags: [concept, oeis, method, cross-reference, research-workflow]
sources: [oeis-mining-pe502]
created: 2026-09-13
updated: 2026-10-16
---

# Online Encyclopedia of Integer Sequences (OEIS) cross-referencing (interlinking method)

## Description

The wiki relates the counting sequences of castles ([[castle-polyomino](pages/castle-polyomino.md)]) to the On-Line Encyclopedia of Integer Sequences, the OEIS, in two ways:

- **Interlinking.** A castle count that reproduces the data of an existing entry, at a stated offset, gives that sequence a castle reading. For example, the castles of width `w` and height 2 with an even number of blocks number `A038505(w+1)` ([[oeis-height2-hyperbolic-castles](pages/oeis-height2-hyperbolic-castles.md)]).
- **Recording a non-match.** A castle count whose terms match no entry in a search is recorded with the search date, so the search can be repeated.

[[castle-sequence-catalogue](pages/castle-sequence-catalogue.md)] records the result for every castle sequence on the wiki, and [[oeis-mining-pe502](pages/oeis-mining-pe502.md)] is the first pass of both.

## Checks

The mining pass states two checks, and the catalogue applies them to every row.[^1]

- **The offset.** A match is checked against the entry's data and offset, not against a few leading terms. The signed tower count `P(1, L)` agrees with `A009545`, the imaginary parts of `(1+i)^n`, only after a shift and a factor 2, `P(1, L) = A009545(L+3)/2`; the entry it equals is `A146559`, the real parts, with `P(1, L) = A146559(L+1)` ([[signed-tower-count](pages/signed-tower-count.md)]).
- **Short prefixes.** Agreement on a few terms with no combinatorial reason is not a match. The mining pass discarded two "sqrt(5) difference" sequences and some hits of short block-count distributions. A search on the first terms of the anchored 1-smooth castles of height 4 returns `A378383`, which agrees through width 10 and differs at width 11, where the castles number 5205 and A378383 has 5206 ([[castle-sequence-catalogue](pages/castle-sequence-catalogue.md)]).[^2]

The OEIS accepts comments and formulas only from human authors, so the wiki records the verified identities and offsets, and the texts written for OEIS entries are not on wiki pages.[^3]

## Appearances in Sources

- [[oeis-mining-pe502](pages/oeis-mining-pe502.md)] - the first mining pass: the offset check, the discarded false positives, and the rule that a tool may verify but not author OEIS text.

## Related Concepts

- [[castle-sequence-catalogue](pages/castle-sequence-catalogue.md)] - every castle sequence with its OEIS status (known, interlink, novel-candidate, unchecked), dated searches and offsets.
- [[oeis-index](pages/oeis-index.md)] - the generated directory of every A-number cited on the wiki, with the citing pages.
- [[signed-tower-count](pages/signed-tower-count.md)] - `P(1, L) = A146559(L+1)` and `P(1, L) = A009545(L+3)/2`, the offset example.
- [[oeis-height2-hyperbolic-castles](pages/oeis-height2-hyperbolic-castles.md)] - the castle reading of `A038505` and `A038503` on the OEIS.
- [[castle-by-area](pages/castle-by-area.md)], [[hyperbolic-sequence-family](pages/hyperbolic-sequence-family.md)], [[narayana-numbers](pages/narayana-numbers.md)] - families of castle counts matched to OEIS entries.
- [[oeis-mining-seminar](pages/oeis-mining-seminar.md)] - a seminar that takes one sequence through the method.

## Footnotes

[^1]: [[oeis-mining-pe502](pages/oeis-mining-pe502.md)] `mine-notes.md` §"Method notes (interlinking discipline)" L177-179 - "Every accepted match above was checked against the actual OEIS data with offsets, not just the first few terms. The plan's own \"A009545\" was caught this way (real vs imaginary)."
[^2]: [[oeis-mining-pe502](pages/oeis-mining-pe502.md)] `mine-notes.md` §"Method notes (interlinking discipline)" L180-182 - "The false positives seen during search (... \"sqrt(5) difference sequences\"; decimal-expansion/Collatz hits on short block distributions) were rejected — no reason behind them."; the `A378383` comparison by transfer matrix against https://oeis.org/A378383 (read 2026-10-16).
[^3]: [[oeis-mining-pe502](pages/oeis-mining-pe502.md)] `SUBMISSION-NOTES.md` §"4. Mechanical vs human (division of labor)" L43-45 - "A tool may: run the verification scripts, check offsets against the live entries, format data. It may NOT author the prose. Only a human may: rewrite the draft prose in their own words, sign it, and submit."
