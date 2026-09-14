# Vein 9 — castles indexed by area

Computation: `vein9_area.py` (enumerates castles by area n = total cells for n <= 18;
cross-references match `castle.py` on shared quantities).

Area = sum of column heights = number of cells in the skyline.  A castle of area n has
1 <= w <= n and 1 <= h <= n, so the enumeration by area is a finite brute force.

## The trivial baseline

**All castles of area n** = all compositions of n into positive parts = 2^(n-1)
= A000079(n-1) = A011782 shifted.  This is just the composition count; every ordered
sequence (c_1..c_w) of positive integers summing to n is a valid castle shape (Rule 3 is
automatic).  Not new; not worth a comment.

## The main finding

**Convex (unimodal) castles of area n** matches **A001523** exactly for the 18 terms
computed:

    conv(n) = 1, 2, 4, 8, 15, 27, 47, 79, 130, 209, 330, 512, 784, 1183, 1765, 2604, 3804, 5504

vs A001523 starting at n=1:

    1, 2, 4, 8, 15, 27, 47, 79, 130, 209, 330, 512, 784, 1183, 1765, 2604, 3804, 5504

with A001523(0) = 1 (the empty stack).

A001523 is "number of stacks, or planar partitions of n; also the number of weakly
unimodal compositions of n."  A convex castle is exactly a unimodal composition of its
area:  convex + column-convex <=> unimodal column-height profile.  So the identity is a
definition-level match, not a coincidence.

A001523 is already densely commented (stacks-of-boards, weakly unimodal compositions,
plane partitions containing a 1, graphical partitions on 2n nodes).  A PE 502 xref is
a legitimate additional interpretation but only marginally valuable — this entry does
not need another synonym.  Draft in `xrefs/A001523-castle.md` regardless (cheap).

## Parity splits — four new sequences

None of the parity-filtered area sequences match anything in OEIS (searched for the
first 18 terms of each):

| name         | terms n = 1..12                                              | OEIS |
|--------------|--------------------------------------------------------------|------|
| `even(n)`    | 0, 1, 2, 5, 8, 17, 30, 65, 122, 261, 502, 1043               | new  |
| `odd(n)`     | 1, 1, 2, 3, 8, 15, 34, 63, 134, 251, 522, 1005               | new  |
| `cev(n)`     | 0, 1, 2, 5, 8, 15, 24, 41, 64, 105, 162, 255                 | new  |
| `cod(n)`     | 1, 1, 2, 3, 7, 12, 23, 38, 66, 104, 168, 257                 | new  |

Identities to record on the parity-split entries when submitting:

- `even(n) + odd(n) = 2^(n-1)`      (composition-count total, A000079(n-1))
- `cev(n)  + cod(n)  = A001523(n)`  (**parity split of A001523**; potentially interesting)
- `even(n) = F_area_even(n)` where the corresponding (w,h)-view is
  `even(n) = sum_{w,h : any castle of area n} [F-parity]`

The `cev(n) + cod(n) = A001523(n)` relation is the most quotable: A001523 is a
well-studied entry, and the parity refinement of "unimodal compositions of n" is not
obviously present in OEIS.  It is a genuine refinement of a foundational sequence.

## Not-a-match (what the plan speculated but ruled out)

The plan (vein 9) named A001168 (fixed polyominoes: 1, 1, 2, 6, 19, 63, 216, 760, ...)
and A005435 (column-convex polyominoes by perimeter: 1, 2, 7, 28, 122, 558, ...) as
possible matches.  Neither is close numerically — those entries count much richer
polyomino classes (allowing gaps, disconnected columns, non-unimodal shapes).  The
right match for castles is unambiguously A001523 (stacks / unimodal compositions),
which sits in the *exactly* correct combinatorial slot.

## Summary

- **1 xref match** — A001523 = convex castles by area (real; marginal value on a
  dense entry; draft in `xrefs/A001523-castle.md`).
- **4 new sequences** — even/odd/cev/cod by area (generation candidates; `cev+cod`
  is a parity refinement of A001523, worth writing up as one of the parity-refinement
  submissions the plan lists in vein 8).
