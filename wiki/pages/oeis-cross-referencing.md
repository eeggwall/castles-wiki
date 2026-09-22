---
title: OEIS cross-referencing (interlinking method)
category: Concepts
summary: The discipline of matching castle counts to existing OEIS A-numbers (interlinking) and identifying unmatched counts (generation) — verify against OEIS data with offsets; drafts require human authorship.
tags: [concept, oeis, method, cross-reference, research-workflow]
sources: [oeis-mining-pe502]
created: 2026-09-13
updated: 2026-09-19
---

# Online Encyclopedia of Integer Sequences (OEIS) cross-referencing (interlinking method)

## Description

**OEIS cross-referencing** is the research method at the heart of the wiki's mission: take a real combinatorial object (here the [[castle-polyomino](pages/castle-polyomino.md)]), compute its counting sequences, and connect them to the On-Line Encyclopedia of Integer Sequences. Two complementary actions:

- **Interlinking** — find an existing A-number whose terms a castle count reproduces, and record the castle as a new interpretation of that sequence (a cross-reference comment/formula). This is how the castle problem is tied into the wider web of combinatorics.
- **Generation** — identify a castle count with *no* OEIS match; that is a candidate new sequence to mint.

The [[oeis-mining-pe502](pages/oeis-mining-pe502.md)] work is a full pass of both.

## Discipline

The method only has value if the matches are real, so a few rules hold throughout:[^1]

- **Verify against the actual OEIS data, with offsets** — not just the first few terms. The single most important catch of the first pass was `P(1,L)`: a plan had claimed `A009545`, but that is `Im((1+i)^n)`; the real match is `A146559(L+1) = Re((1+i)^{L+1})`. Only an offset-correct comparison against the stored data distinguishes them (see [[signed-tower-count](pages/signed-tower-count.md)]).
- **Reject short-term false positives** — coincidental agreement on a handful of terms (e.g. sqrt-5 difference sequences, decimal-expansion hits on short block distributions) is discarded unless there is a structural reason.
- **Prefer isolated entries** — a cross-reference is highest-value on a sparse, under-connected sequence (like the "sum of every 4th binomial" entries A038503/A038505) and marginal on a dense one (like A001523, already richly commented).

## Submission is a human act

OEIS requires **human authorship** — a tool may run the verification scripts, check offsets, and format data, but may **not** author the prose, and every added comment/formula line must be signed by a human. New contributors are throttled to a few open drafts, so submissions lead with the highest-value, lowest-risk interlinks.[^2] Accordingly, this wiki records the *verified findings and identities*; the submission-ready draft text is kept as drafts in `raw/oeis-pe502/` (and `raw/oeis-pe502/xrefs/`), to be reworded and signed by a person before submission — the wiki does not present draft prose as final.

## Appearances in Sources

- [[oeis-mining-pe502](pages/oeis-mining-pe502.md)] — applies this method across the castle veins; states the offset-verification discipline and the interlinking-vs-generation split.
- [[oeis-index](pages/oeis-index.md)] - the wiki's OEIS directory, script-generated: every A-number cited across the wiki, grouped by role (castle interpretation, metallic ladder, plastic, supporting), with the citing pages and mention counts.
- [[castle-sequence-catalogue](pages/castle-sequence-catalogue.md)] - the hand-curated catalogue: every castle-counting sequence with its novelty status (known / interlink / novel-candidate / unchecked) and the submission priority list.

## Related Concepts

- [[castle-by-area](pages/castle-by-area.md)], [[hyperbolic-sequence-family](pages/hyperbolic-sequence-family.md)], [[narayana-numbers](pages/narayana-numbers.md)] — sequence families reached by this method.
- [[signed-tower-count](pages/signed-tower-count.md)] — where the offset-verification discipline caught a real/imaginary mixup.
- [[oeis-index](pages/oeis-index.md)] — the OEIS meta-triad's mechanical half: script-generated directory of every A-number on the wiki.
- [[castle-sequence-catalogue](pages/castle-sequence-catalogue.md)] — the OEIS meta-triad's hand-curated half: castle-counting sequences with novelty status and submission priority.

## Footnotes

[^1]: [[oeis-mining-pe502](pages/oeis-mining-pe502.md)] `mine-notes.md` §"Method notes (interlinking discipline)" L175-186 — "checked against the actual OEIS data with offsets, not just the first few terms ... false positives ... were rejected ... The single highest-value new-interpretation targets are A038505 and A038503."
[^2]: [[oeis-mining-pe502](pages/oeis-mining-pe502.md)] `SUBMISSION-NOTES.md` §"Mechanical vs human" L36-41, `crosslink-avenues.md` §"Suggested submission order" L120-124 — "A tool may ... NOT author the prose. Only a human may ... sign it, and submit. OEIS forbids AI-authored text" and "New contributors are throttled to a few open drafts, so lead with tier 1."
