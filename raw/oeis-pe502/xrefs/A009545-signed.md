# Cross-link draft — A009545 as the signed count of height-2 castles ending at height 2

Status: DRAFT for Charles to reword and submit. OEIS requires human authorship.
Execution notes (field map, signature format, scope): see ../SUBMISSION-NOTES.md.
Checked against the live entry 2026-10-04 (A009545 revision #193, Jul 27 2026).

## Identity (verified)

A009545 = "Expansion of e.g.f. sin(x)*exp(x)", offset 0, data
`0, 1, 2, 2, 0, -4, -8, -8, 0, 16, 32, 32, 0, -64, -128, -128, 0, 256, ...`.

    a(n) = (even-block) - (odd-block) castles of width n and height 2
           whose last column reaches height 2,                         for n >= 1.

Every castle counted has a column at height 2 (the last one), so all are castles of exact
height 2: no `- 1` correction and no index shift (width n goes with a(n)). a(0) = 0 is
consistent (no castle of width 0), but state the range as n >= 1.

Wiki notation: a(n) = -P_odd(1, n), the k = 1 parity sector of the signed tower count
(`wiki/pages/signed-tower-count.md`, `wiki/pages/tower-parity-sectors.md`). Do not use P or
"tower" in the comment.

Verified by brute force for n = 1..16 (script below).

| n | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| even | 1 | 2 | 3 | 4 | 6 | 12 | 28 | 64 | 136 | 272 | 528 | 1024 |
| odd | 0 | 0 | 1 | 4 | 10 | 20 | 36 | 64 | 120 | 240 | 496 | 1024 |
| a(n) | 1 | 2 | 2 | 0 | -4 | -8 | -8 | 0 | 16 | 32 | 32 | 0 |

## Proof

A castle of width n and height 2 whose last column reaches height 2 is determined by which
columns reach height 2: a binary word of length n ending in 1. If the 1's form r >= 1
runs, the castle has 1 + r blocks, even exactly when r is odd, so it contributes
(-1)^(r+1) to "even minus odd". The words of length n ending in 1 with exactly r runs number
binomial(n, 2r-1): a word with r runs has 2r run boundaries among the n + 1 gaps around its
letters, one of them is the gap after the last letter (the word ends in 1), and the other
2r - 1 are chosen from the remaining n gaps. Hence

    a(n) = Sum_{r>=1} (-1)^(r+1) * binomial(n, 2r-1) = Sum_{k>=0} (-1)^k * binomial(n, 2k+1)
         = Im((1+i)^n).

The middle sum is Paul Barry's formula already on the entry.

## Relation to A146559

Split the binary words of length n (the columns reaching height 2) by their last column and
sum the sign (-1)^r. Words ending in 1 give -a(n) (this entry, sign flipped); words ending
in 0 give A146559(n), which includes the all-0 word (not a castle). Deleham's line on
A146559, `(1+i)^n = A146559(n) + A009545(n)*i`, already ties the two entries together, and
A009545's Cf. lists A146559, so the comment does not need to state the split.

## What is already there (do NOT duplicate)

- `Imaginary part of (1+i)^n` (LeBrun) and `a(n) = Im((1+i)^n)` (Sykora).
- `a(n) = Sum_{k=0..floor(n/2)} binomial(n, 2*k+1)*(-1)^k` (Paul Barry, Sep 20 2003) — the
  castle sum above.
- `a(n) = Sum_{k=0..n-1} (-1)^floor(k/2)*binomial(n-1, k)` (Cloitre), the order-3
  recurrence, the e.g.f.
- Cf. already lists A146559.
- None of the 7 existing comments is a castle, bargraph or binary-word interpretation of
  this kind (checked 2026-10-04).

So the new content is only the interpretation. No new formula is needed.

## Draft additions

### Comment (append)

> Among the castle polyominoes of width n and height 2 whose last column reaches height 2,
> a(n) is the number with an even number of blocks minus the number with an odd number of
> blocks (Project Euler, Problem 502: Counting Castles), for n >= 1. Here a castle is a
> stack of unit blocks on a grid, whose bottom row is a single block of length n, whose
> higher blocks have height 1 and rest on the blocks below without overhang, whose maximum
> height is 2, and in which neighboring blocks of the same row are separated by a gap.

The wording follows the A146559 comment as submitted 2026-10-04 ("Among the castle
polyominoes of width ... and height 2, ...", the same definition sentence). Note the
differences from A146559: width n (not n-1), no "a(n) - 1", even minus odd (not odd minus
even), range n >= 1.

### Optional last sentence

> If the columns that reach height 2 form r >= 1 runs, the castle has 1 + r blocks, and
> binomial(n, 2*r-1) of these castles have r runs.

Ties the comment to Barry's formula; drop it if the editor finds the comment long.

### Crossrefs

No change: A146559 is already in the Cf. list. (A038503 / A038505 are not, and are not
needed here.)

## Recommendation

**Submit (Comment only), at lower priority** than the exact-height sweep, and after the
A038503 correction and the A146559 comment clear review. It is a clean, new geometric
reading (exact height, no offset shift), but A009545 is a dense entry (193 revisions), and
the "last column reaches height 2" condition makes the family more specialised than the
A038503 / A038505 families.

## Flags

1. Rewrite in own words and sign `- _Chaz Reid_, Mon D YYYY` with the actual submission
   date (see ../SUBMISSION-NOTES.md §3).
2. Every castle in the comment is at exact height 2 ("height 2", "maximum height is 2").
   Do not write "height at most 2".
3. Scope the family once ("Among the castle polyominoes of width n and height 2 whose last
   column reaches height 2, ...") so both counts refer to it.
4. Even minus odd, in that order: the sign is positive at n = 1 (one castle, 2 blocks).
5. "Problem 502" (not "Project 502").
6. Do not change Name/Data/Offset/Keywords or existing lines.

## Verification script

```python
from itertools import product
from math import comb

A009545 = [0, 1, 2, 2, 0, -4, -8, -8, 0, 16, 32, 32, 0, -64, -128, -128, 0]  # live, n = 0..16

for n in range(1, 17):
    even = odd = 0
    for word in product((0, 1), repeat=n):          # columns reaching height 2
        if word[-1] != 1:
            continue                                # last column must reach height 2
        r = sum(1 for i in range(n) if word[i] and (i == 0 or not word[i - 1]))
        if (1 + r) % 2: odd += 1                    # castle blocks = 1 + r, r >= 1 here
        else: even += 1
    barry = sum((-1) ** k * comb(n, 2 * k + 1) for k in range(n // 2 + 1))
    assert even - odd == barry == A009545[n]
print("ok")
```
