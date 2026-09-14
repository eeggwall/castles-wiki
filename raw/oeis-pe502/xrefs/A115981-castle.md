# Cross-link draft — A115981 (compositions of n not viewable as stacks) as non-convex castles by area

Status: DRAFT for Charles to reword and submit.  OEIS requires human authorship.
Execution notes (field map, signature format, scope): see ../SUBMISSION-NOTES.md.

## Identity (verified)

A115981 = number of compositions of n which cannot be viewed as stacks, with formula
`a(n) = A011782(n) − A001523(n)`.  Offset 0,7; data starts `0, 0, 0, 0, 0, 1, 5, 17,
49, 126, 303, 694, 1536, 3312, 7009, 14619, ...`.

For n >= 1, A115981(n) is also the number of **non-convex castles** (Project Euler
Problem 502, "Counting Castles") of area n, where a castle is a column-height
composition (c_1, ..., c_w) of n into positive parts and non-convex means the
sequence is NOT weakly unimodal (has at least one interior local minimum).  This is
the complement of the "convex castle" reading of A001523 (see A001523 for the convex
side), and the entry's own formula `A011782(n) − A001523(n)` is exactly
`all castles − convex castles` when castles are indexed by area.

Verified against A115981 for n = 1..15 by `python3 vein9b_concave.py`.

## What is already there (do NOT duplicate)

The entry already gives the "cannot be viewed as a stack" reading, the formula
`A011782 − A001523`, and links to A001523 (the complement).  The castle wording is
a synonym; the value is the Project Euler cross-reference and the visual "non-convex
skyline" phrasing.

## Draft additions

### Comment (append; one line)

> Also the number of non-convex castles (Project Euler Problem 502, "Counting
> Castles") of area n, for n >= 1: column-height compositions (c_1, ..., c_w) of n
> into positive parts that are NOT weakly unimodal (equivalently, skylines with at
> least one interior valley).

### Crossrefs (append if not already present)

> Cf. A332578 (valley-shaped castles), A038505, A038503, A146559 (castle counts of
> PE 502 indexed by width and height).

## Flags

1. Rewrite in own words; sign `- _Firstname Lastname_, Mon D YYYY`.
2. Small comment on a dense entry.  The parity refinements
   (`nc_even`, `nc_odd`) are separate new submissions -- do NOT propose them here.
3. Verify A115981 does not already carry a PE 502 / castle phrasing.
