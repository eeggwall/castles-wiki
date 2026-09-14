# Cross-link draft — A332578 (compositions of n with unimodal negation) as valley castles by area

Status: DRAFT for Charles to reword and submit.  OEIS requires human authorship.
Execution notes (field map, signature format, scope): see ../SUBMISSION-NOTES.md.

## Identity (verified)

A332578 = number of compositions of n whose negation is unimodal.  Offset 0,3; data
starts `1, 1, 2, 4, 7, 13, 21, 36, 57, 91, 140, 217, 323, 485, 711, 1039, ...`.

For n >= 1, A332578(n) is also the number of **valley-shaped castles** (Project Euler
Problem 502, "Counting Castles") of area n, where a castle is a column-height
composition (c_1, ..., c_w) of n into positive parts and valley-shaped means the
sequence is weakly decreasing then weakly increasing (i.e. it has at most one
interior minimum).  This is the mirror of the "unimodal composition" reading in
A001523: a composition is a valley iff its negation is unimodal.

Verified against A332578 for n = 1..15 by `python3 vein9b_concave.py`.

## What is already there (do NOT duplicate)

The entry already gives the negation-unimodal reading, the g.f., and links to A001523
(unimodal), A332669 (not-negation-unimodal), and A329398 (both unimodal and
negation-unimodal).  The castle wording is a synonym in that same cluster, valuable
mostly for the Project Euler cross-reference.

## Draft additions

### Comment (append; one line)

> Also the number of valley-shaped castles (Project Euler Problem 502, "Counting
> Castles") of area n, for n >= 1: column-height compositions (c_1, ..., c_w) of n
> into positive parts that are weakly decreasing then weakly increasing.

### Crossrefs (append if not already present)

> Cf. A001523 (unimodal / convex-castle counterpart), A115981 (non-convex castles),
> A038505, A038503, A146559 (castle counts of PE 502 indexed by width and height).

## Flags

1. Rewrite in own words; sign `- _Firstname Lastname_, Mon D YYYY`.
2. This is a small addition on a dense entry.  Do NOT propose the strict-valley
   sequence or the parity refinements on this entry — those are separate new
   submissions (see `../vein9b-concave.md`).
3. Verify A332578's current comment list actually lacks a PE 502 / castle phrasing
   before submitting.
