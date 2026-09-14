# Cross-link draft — A001523 (stacks / unimodal compositions) as convex castles by area

Status: DRAFT for Charles to reword and submit.  OEIS requires human authorship.
Execution notes (field map, signature format, scope): see ../SUBMISSION-NOTES.md.

## Identity (verified)

A001523 = number of stacks, or planar partitions of n; also the number of weakly
unimodal compositions of n.  Offset 0,3; data starts `1, 1, 2, 4, 8, 15, 27, 47, 79,
130, 209, 330, 512, ...`.

For n >= 1, A001523(n) is also the number of **convex (unimodal) castles** (Project
Euler Problem 502, "Counting Castles") of area n, where a castle is a column-height
composition (c_1, ..., c_w) of n into positive parts and convex means the sequence is
weakly increasing then weakly decreasing.  This is a direct restatement of the
"weakly unimodal composition" definition: a convex castle of area n is the same object
as a weakly unimodal composition of n.

Verified against A001523 for n = 1..18 by `python3 vein9_area.py`.

## What is already there (do NOT duplicate)

A001523 is dense: stacks of boards, weakly unimodal compositions, planar partitions of
n, graphical partitions on 2n nodes that contain a 1, and it has multiple g.f.s and
Comtet references.  This draft only proposes a *comment* (one line), not a formula or
new g.f.  The convex-castle reading is a synonym in the "unimodal composition" cluster
and does not warrant a separate formula.

## Draft additions

### Comment (append; one line)

> Also the number of convex castles (Project Euler Problem 502, "Counting Castles") of
> area n, for n >= 1; equivalently, the number of column-convex row-convex skylines
> with n cells.  A castle here is a column-height composition (c_1, ..., c_w) of n into
> positive parts; convex means the sequence is weakly unimodal.

### Crossrefs (append if not already present)

> Cf. A038505, A038503, A146559 (castle counts of PE 502 indexed by (width, height)
> instead of area).

## Flags

1. Rewrite in own words; sign `- _Firstname Lastname_, Mon D YYYY` (replace placeholder
   `_Charles Reid_, Sep 05 2026`).
2. This is a small addition on a dense entry.  Do NOT propose the parity-refinement
   sequences (even / odd castles by area, and their convex versions) on this entry —
   those are separate new submissions, not comments here (see `../vein9-area.md`).
3. Verify A001523's current comment list actually lacks the PE 502 phrasing before
   submitting (the "weakly unimodal composition" reading is already there; the PE 502
   framing is what's new).
