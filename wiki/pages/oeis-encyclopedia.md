---
title: The On-Line Encyclopedia of Integer Sequences (OEIS)
category: Sources
summary: The OEIS, the database of integer sequences maintained by The OEIS Foundation Inc. An entry has an A-number (A followed by six digits), Data lines with the first terms, a Name line, an Offset line giving the index of the first term, and Formula, Comments and References lines. Wiki pages cite entries by URL, read date and a verbatim quote, and count a castle sequence as matching an entry only at the entry's offset.
tags: [oeis, integer-sequences, database, reference, source]
sources: [oeis-encyclopedia]
created: 2026-10-25
updated: 2026-10-29
---

# The On-Line Encyclopedia of Integer Sequences (OEIS)

**Source:** https://oeis.org/ and https://oeis.org/eishelp2.html
**Date ingested:** 2026-10-25
**Type:** reference database (web)

## Summary

The On-Line Encyclopedia of Integer Sequences is a database of integer sequences maintained by The OEIS Foundation Inc.[^1] Each sequence has an A-number, its catalog number, "A followed by 6 digits".[^2]

An entry is a set of lines. The Data lines "give the beginning of the sequence", the Name line "gives a brief description or definition of the sequence", the Formula lines give "formulae, recurrences, generating functions, etc.", the Comments lines give other contexts in which the sequence occurs, and the References and Links lines give the literature.[^2] The Offset line fixes the indexing: "The first offset usually gives the subscript of the first term in the sequence, or is 1 if the sequence is a list."[^2] So two sequences with the same terms can differ in their index, and a formula `a(n) = …` in an entry is stated at that entry's offset.

## Key Takeaways

- An A-number is the catalog number of a sequence; the Name line defines it and the Data lines give its first terms.[^2]
- The first offset is the index of the first term, so a match between a castle count and an entry has to state the shift of the index.[^2]
- Formulas, generating functions and further contexts of a sequence are in its Formula and Comments lines, and its literature in its References and Links lines.[^2]

## Relation to Other Wiki Pages

Wiki pages cite an entry by its URL, the date it was read and a verbatim quote from it. [[oeis-cross-referencing](pages/oeis-cross-referencing.md)] is the method of matching a castle count against an entry at its offset, [[oeis-index](pages/oeis-index.md)] lists every A-number cited on the wiki with the citing pages, and [[oeis-mining-pe502](pages/oeis-mining-pe502.md)] and [[castle-sequence-catalog](pages/castle-sequence-catalog.md)] collect the castle counts with their entries.

## Footnotes

[^1]: https://oeis.org/ (read 2026-10-25) - "The On-Line Encyclopedia of Integer Sequences (OEIS)", "Maintained by The OEIS Foundation Inc."
[^2]: https://oeis.org/eishelp2.html (read 2026-10-25) - "The A-number ... is the absolute catalogue number of the sequence. It consists of A followed by 6 digits.", "These lines give the beginning of the sequence.", "The \"Name\" line gives a brief description or definition of the sequence.", "These lines give formulae, recurrences, generating functions, etc. for the sequence.", "Additional remarks about the sequence that do not fit into any of the other lines (additional contexts where the sequence occurs, for instance).", "References where information about the sequence can be found.", "The first offset usually gives the subscript of the first term in the sequence, or is 1 if the sequence is a list."
