# Correction draft — A038503 castle comment at exact height

Status: DRAFT for Charles to reword and submit. OEIS requires human authorship.
Execution notes (field map, signature format, scope): see ../SUBMISSION-NOTES.md.
Checked against the live entry 2026-10-04 (A038503 revision #93, Oct 03 2026).

**SUBMITTED for review 2026-10-04** as "Chaz Reid" (replacing the Sep 18 2026 comment).
Text as reviewed before submission (a person's rewording, with "whose maximum height is 2"
and "r >= 1" runs):

> a(n) - 1 is the number of castle polyominoes of width n-1 and height 2 with an odd number
> of blocks (Project Euler, Problem 502: Counting Castles), for n >= 2. Here a castle is a
> stack of unit blocks on a grid, whose bottom row is a single block of length n-1, whose
> higher blocks have height 1 and rest on the blocks below without overhang, whose maximum
> height is 2, and in which two neighboring blocks of the same row are separated by a gap.
> If the columns that reach height 2 form r >= 1 runs, the number of blocks is 1 + r, so an
> odd number of blocks means r is even. - _Chaz Reid_, Sep 18 2026

## The problem

The live comment (signed _Chaz Reid_, Sep 18 2026) reads "castle polyominoes of width n-1
and **height at most 2** with an odd number of blocks". A castle of height 2 has at least
one column that reaches height 2 (PE 502: "the maximum achieved height of the entire castle
is exactly h"). "Height at most 2" is not a castle family of exact height: it counts the
r = 0 term binomial(n, 0) = 1, where no column reaches height 2, as one of the castles.

The companion comment on A038505 is already at exact height ("height 2", "whose maximum
height is 2"). The correction makes A038503 match it.

## Identity (verified)

    a(n) - 1 = odd(n-1, 2)     for n >= 2,

where odd(w, 2) is the number of castles of width w and height 2 with an odd number of
blocks. The 1 is the r = 0 term binomial(n, 0) of a(n) = Sum_k binomial(n, 4k).
a(0) = a(1) = 1 are not covered.

Verified by brute force for w = n-1 = 1..14 (script below).

| n | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|---|
| a(n) | 1 | 1 | 2 | 6 | 16 | 36 | 72 | 136 | 256 |
| odd(n-1, 2) | 0 | 0 | 1 | 5 | 15 | 35 | 71 | 135 | 255 |

## Proof

A castle of width w and height 2 is determined by which columns reach height 2: a binary
word of length w with at least one 1. If the 1's form r >= 1 runs, the castle has 1 + r
blocks, odd exactly when r is even. There are binomial(w+1, 2r) words with r runs, so
odd(w, 2) = Sum_{k>=1} binomial(w+1, 4k) = a(w+1) - binomial(w+1, 0).

## Draft replacement

Edit the existing castle comment (your own line) to:

> a(n) - 1 is the number of castle polyominoes of width n-1 and height 2 with an odd
> number of blocks (Project Euler, Problem 502: Counting Castles), for n >= 2. Here a
> castle is a stack of unit blocks on a grid, whose bottom row is a single block of length
> n-1, whose higher blocks have height 1 and rest on the blocks below without overhang,
> whose maximum height is 2, and in which two neighboring blocks of the same row are
> separated by a gap. If the columns that reach height 2 form r >= 1 runs, the number of
> blocks is 1 + r, so an odd number of blocks means r is even; the 1 is the term
> binomial(n, 0) of a(n) = Sum_k binomial(n, 4*k).

The definition sentence is the A038505 comment's, word for word, so the two entries read
alike.

## Leave alone

- The two FORMULA lines (`a(n) = A000225(n-1) - A038505(n) + 1`, `a(n) = A038505(n) +
  A146559(n)`): no height language, still correct.
- Name, Data, Offset, Keywords, Cf.

## Flags

1. Rewrite in own words. Since this replaces your own line, keep or update the signature
   per the editor's preference (usually the original signature stays and the edit is
   recorded in the history; ask in the edit's "reason" box if unsure).
2. In the edit's reason/notes box, say why: "state the count at exact height 2, as on
   A038505; a castle of height 2 must reach height 2".
3. "Problem 502" (not "Project 502").
4. Throttle: the A038505 typo fix (submitted 2026-10-04) may still be open. If OEIS limits
   open edits, wait for it to clear.

## Verification script

```python
from itertools import product
from math import comb

for w in range(1, 15):
    n = w + 1
    odd = 0
    for word in product((0, 1), repeat=w):          # columns reaching height 2
        r = sum(1 for i in range(w) if word[i] and (i == 0 or not word[i - 1]))
        if r >= 1 and (1 + r) % 2:                  # height 2 needs r >= 1
            odd += 1
    a = sum(comb(n, j) for j in range(0, n + 1, 4))  # A038503(n)
    assert a - 1 == odd
print("ok")
```
