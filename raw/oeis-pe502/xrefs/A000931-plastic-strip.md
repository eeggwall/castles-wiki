# Cross-link draft — A000931 (Padovan) as the plastic castle strip

Status: DRAFT for Charles to reword and submit. OEIS requires human authorship.
Execution notes (field map, signature format, scope): see ../SUBMISSION-NOTES.md.
Checked against the live entry 2026-10-04 (A000931; 33 comments).

## Identity (verified)

A000931 = "Padovan sequence (or Padovan numbers): a(n) = a(n-2) + a(n-3) with a(0) = 1,
a(1) = a(2) = 0", offset 0, `1, 0, 0, 1, 0, 1, 1, 1, 2, 2, 3, 4, 5, 7, 9, 12, 16, 21, 28, …`.

The **plastic strip** is the castle strip with column heights in `{1, 2, 3}` and the rule:
a column of height 1 is followed by one of height 3, a column of height 2 by one of height 1,
and a column of height 3 by one of height 1 or 2. Its transfer matrix is
`[[0,0,1],[1,0,0],[1,1,0]]` (characteristic polynomial `x^3 - x - 1`, Perron root the plastic
number), the sparsest 0/1 matrix with that polynomial (`wiki/pages/reachable-field-census.md`).

    #{strips of width n}  =  a(n + 9)  =  3, 4, 5, 7, 9, 12, 16, 21, 28, …      (n >= 1)

For `n >= 3` every strip reaches height 3 (a 1 is followed by a 3, and a 2 by a 1), so for
`n >= 3` the strips are exactly the castles of width `n` and exact height 3 obeying the rule.
(At `n = 1, 2` the strips `(1)`, `(2)`, `(2, 1)` stay below height 3.) Verified by brute force
for `n <= 15`, and the matrix count for `n <= 40`.

Structure (own reasoning): after each 3 the skyline returns to 3 through `3, 1, 3` or
`3, 2, 1, 3`, so a strip is a window of a concatenation of the pieces `(3, 1)` and `(3, 2, 1)`,
which is why the count is a Padovan number (compositions into 2s and 3s, Deutsch's comment on
the entry).

## What is already there

33 comments, among them: compositions of `n-3` into 2s and 3s (Deutsch); "a(n+8) is the number
of solus bitstrings of length n with no runs of 3 zeros" (Finch), i.e. the `(1, 2)`-run-length-
limited binary words; maximal independent sets of the path graph; strings over `{A, B}` with no
`AA` and no `BBB`.

## Draft addition (only if submitted)

### Comment (append)

> For n >= 3, a(n+9) is the number of castle polyominoes of width n and height 3 in which a
> column of height 1 is followed by a column of height 3, a column of height 2 by a column of
> height 1, and a column of height 3 by a column of height 1 or 2 (Project Euler, Problem 502:
> Counting Castles). Here a castle is a stack of unit blocks on a grid, whose bottom row is a
> single block of length n, whose higher blocks have height 1 and rest on the blocks below
> without overhang, whose maximum height is 3, and in which neighboring blocks of the same row
> are separated by a gap.

## Recommendation

**Skip by default.** A000931 is one of the densest entries in the OEIS (33 comments), and it
already carries word and automaton readings of the same count (Finch's `(1, 2)`-RLL words,
Deutsch's compositions into 2s and 3s). The plastic strip is a wiki-built transfer rule rather
than a natural castle family, so the comment would add a third automaton reading of a count the
entry already explains. The castle readings worth submitting are the ones that give an entry
something it lacks (A049703, A226136/A003410). If submitted anyway, comment only, low priority.

## Flags

1. Rewrite in own words and sign `- _Chaz Reid_, Mon DD YYYY` (two-digit day).
2. Keep `n >= 3`: at `n = 1, 2` some strips never reach height 3 and are not castles of height 3.
3. "Problem 502" (not "Project 502").

## Verification script

```python
from itertools import product
P = [1, 0, 0]
while len(P) < 60: P.append(P[-2] + P[-3])                 # A000931
nxt = {1: {3}, 2: {1}, 3: {1, 2}}
for n in range(1, 16):
    strips = [c for c in product((1, 2, 3), repeat=n) if all(c[i+1] in nxt[c[i]] for i in range(n - 1))]
    assert len(strips) == P[n + 9]
    if n >= 3:
        assert all(max(c) == 3 for c in strips)               # castles of exact height 3
print("ok")
```
