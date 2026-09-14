# Vein 9b — concave castles

Companion to `vein9-area.md`.  Computation: `vein9b_concave.py`.

"Concave" is not a single notion; three natural readings:

- **valley** — weakly decreasing then weakly increasing (mirror of unimodal).
  Overlaps with unimodal on monotone profiles.
- **strict-valley** — valley AND not unimodal (has an interior dip).
- **non-convex** — NOT unimodal (has at least one interior valley).  This is
  the *complement* of the convex class.

## Results by area

Verified for n = 1..15.

| our count             | terms n = 1..12                                              | OEIS |
|-----------------------|--------------------------------------------------------------|------|
| `valley(n)`           | 1, 2, 4, 7, 13, 21, 36, 57, 91, 140, 217, 323                | **A332578** |
| `strict_valley(n)`    | 0, 0, 0, 0, 1, 3, 8, 17, 34, 60, 107, 175                    | new  |
| `nonconv(n)`          | 0, 0, 0, 0, 1, 5, 17, 49, 126, 303, 694, 1536                | **A115981** |
| `all(n) − valley(n)`  | 0, 0, 0, 1, 3, 11, 28, 71, 165, 372, 807, 1725               | **A332669** |

Three matches, one genuinely new sequence.

### The matches (all definitional, all dense entries)

**A332578** — "Number of compositions of n whose negation is unimodal."  A composition
is a valley iff its negation is unimodal (negation flips peaks and valleys), so
`valley(n) = A332578(n)` for n >= 1.  Same offset shift as `conv(n) = A001523(n)` from
vein 9a: `A332578(0) = 1` (empty composition), then `A332578(n) = valley(n)`.

**A115981** — "The number of compositions of n which cannot be viewed as stacks",
formula `a(n) = A011782(n) − A001523(n)`.  Since `A011782(n) = 2^(n−1)` = all castles
of area n (any composition), and `A001523(n) = conv(n)`, this is exactly `all − conv =
nonconv`.  `nonconv(n) = A115981(n)` for n >= 1.

**A332669** — "Number of compositions of n whose negation is not unimodal."  Same
relation, but for valleys instead of convex castles: `A332669(n) = 2^(n−1) −
A332578(n) = all(n) − valley(n)`.  Not directly a castle count under a natural name,
but recorded for completeness (and because it identifies the "not-a-valley" complement
as an existing OEIS entry).

None of A332578, A115981, A332669 currently cite Project Euler 502.  Each is a small
comment addition (see `xrefs/A332578-castle.md`, `xrefs/A115981-castle.md`).

### The new sequence — `strict_valley(n)`

Non-monotone, non-convex, valley-shaped castles.  Compositions of n that are strictly
"true dips": weakly-decreasing then weakly-increasing AND have an actual interior
minimum (not just a monotone or unimodal profile that happens to also read as a
valley).  First 15 terms:

    strict_valley(n) = 0, 0, 0, 0, 1, 3, 8, 17, 34, 60, 107, 175, 285, 445, 691

Identity: `strict_valley(n) + (valley ∩ unimodal)(n) = valley(n) = A332578(n)`.  The
intersection `valley ∩ unimodal` is exactly the *monotone* castles (weakly increasing
OR weakly decreasing); a monotone composition of n into a positive number of parts is
counted by `A000009(n)`-type partition sums but for compositions the count is easier:
each monotone-up composition of n corresponds to a partition of n (parts in weakly
increasing order), so weakly-monotone compositions = 2 * A000041(n) − p_flat(n), where
p_flat(n) is the count of flat compositions (all parts equal, which are counted twice).

Cleaner recorded identity (verified numerically for n = 1..15):

    A332578(n) = strict_valley(n) + (weakly-up partitions of n)
                                  + (weakly-down partitions of n)
                                  − (constant compositions of n)

The exact identity for the overlap is `(weakly-up) = (weakly-down) = A000041(n)`
(partitions of n).

`strict_valley` is a candidate new-sequence submission; its parity splits
(`sv_even`, `sv_odd`) below are also new.

## Parity splits — all new

None of the parity-refined concave sequences match OEIS (searched 15 terms each):

| name                | terms n = 1..12                                              |
|---------------------|--------------------------------------------------------------|
| `valley_even(n)`    | 0, 1, 2, 4, 6, 12, 16, 32, 40, 78, 98, 175                   |
| `valley_odd(n)`     | 1, 1, 2, 3, 7, 9, 20, 25, 51, 62, 119, 148                   |
| `sv_even(n)`        | 0, 0, 0, 0, 0, 2, 2, 11, 12, 36, 44, 99                      |
| `sv_odd(n)`         | 0, 0, 0, 0, 1, 1, 6, 6, 22, 24, 63, 76                       |
| `nc_even(n)`        | 0, 0, 0, 0, 0, 2, 6, 24, 58, 156, 340, 788                   |
| `nc_odd(n)`         | 0, 0, 0, 0, 1, 3, 11, 25, 68, 147, 354, 748                  |

Recorded identities (for submission comments):

- `valley_even(n) + valley_odd(n) = valley(n) = A332578(n)` — parity split of A332578.
- `nc_even(n) + nc_odd(n) = nonconv(n) = A115981(n)` — parity split of A115981.
- `sv_even(n) + sv_odd(n) = strict_valley(n)` (both parts new).
- `cev(n) + valley_even(n) - even(n) = 2 * (even-castles-monotone)` — parity split of
  the inclusion-exclusion between convex and valley classes; not verified as a clean
  identity yet, mentioned as a potential relation to explore before submitting.

## Concave counts by (w, h)  — the PE 502 axis

`valley(w, h)` — number of valley-shaped castles of width w, height exactly h:

|   | h=1 | h=2 | h=3 | h=4 | h=5 |
|---|----:|----:|----:|----:|----:|
| w=1 | 1 | 1 | 1 | 1 | 1 |
| w=2 | 1 | 3 | 5 | 7 | 9 |
| w=3 | 1 | 6 | 15 | 28 | 45 |
| w=4 | 1 | 10 | 35 | 84 | 165 |
| w=5 | 1 | 15 | 70 | 210 | 495 |

**This is the same table as `convex(w, h)`** — both equal `C(2h + w − 3, w − 1)`
(the binomial from `binomial-vandermonde-identity.md`).  So convex and valley have
the same *cardinality* in each (w, h) cell but *different sets*; e.g. for (w=3, h=2)
convex has 6 castles and valley has 6 castles, differing in whether (1,2,1) and
(2,1,2) are counted (peak vs. dip).

This is a candidate bijection worth writing up (mirror-shift under the reflection
that swaps peaks and valleys), but numerically it adds nothing new to the OEIS map
for (w, h).

`nonconv(w, h)`:

|   | h=1 | h=2 | h=3 | h=4 | h=5 |
|---|----:|----:|----:|----:|----:|
| w=1 | 0 | 0 | 0 | 0 | 0 |
| w=2 | 0 | 0 | 0 | 0 | 0 |
| w=3 | 0 | 1 | 4 | 9 | 16 |
| w=4 | 0 | 5 | 30 | 91 | 204 |
| w=5 | 0 | 16 | 141 | 571 | 1606 |

Side observation: the w=3 row is `(h−1)^2`.  This looks derivable directly (a
non-convex width-3 castle needs a strict dip in the middle: `c_1 > c_2 < c_3` with
`max = h`), but is not searched further here.

## Summary

- **3 new xref matches** (all definitional, all on dense entries):
  A332578 (valley = negation-unimodal), A115981 (non-convex = "not a stack"),
  A332669 (complement of valley = negation-not-unimodal).  Cheap comments.
- **1 new sequence** — `strict_valley(n)`, castles with a true interior dip.
- **6 new parity-refined sequences** — valley/strict-valley/non-convex, each
  split by block parity; several are parity refinements of A115981 / A332578 /
  A001523 and are the most quotable new-submission candidates.
- **Convex/valley (w,h) equinumeracy** — a candidate bijection to write up, but
  no new OEIS entries drop out of the (w, h) view.
