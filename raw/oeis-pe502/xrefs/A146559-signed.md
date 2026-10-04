# Cross-link draft — A146559 as the signed castle count of height 2

Status: DRAFT for Charles to reword and submit. OEIS requires human authorship.
Execution notes (field map, signature format, scope): see ../SUBMISSION-NOTES.md.
Checked against the live entry 2026-10-04 (A146559 revision #152, Sep 28 2026).

## Identity (verified)

A146559 = "Expansion of (1-x)/(1 - 2*x + 2*x^2)", offset 0, data
`1, 1, 0, -2, -4, -4, 0, 8, 16, 16, 0, -32, -64, -64, 0, 128, ...`.

    a(n) = P(1, n-1)                                         for n >= 1
         = odd(n-1, 2) + 1 - F(n-1, 2)                       for n >= 2

where P(1, w) is the signed tower count at k = 1 (sum of (-1)^blocks over towers of
height <= 1 on w columns), F(w, 2) is the number of castles of width w and exact height 2
with an even number of blocks, and odd(w, 2) the number with an odd number of blocks.
The `+ 1` is the single castle of width w and height 1 (one block, odd).

In words: a(n) = (castles of width n-1 with at most one layer above the bottom row and an
odd number of blocks) - (those with an even number of blocks).

Verified by brute force for w = n-1 = 0..14 (script below): the direct signed sum, the
odd-minus-even castle difference, the binomial sum, and the live terms all agree.

| w = n-1 | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| a(n) | 1 | 0 | -2 | -4 | -4 | 0 | 8 | 16 | 16 | 0 | -32 | -64 | -64 |

## Proof

A castle of width w with at most one layer above the bottom row is determined by which
columns reach height 2: a binary word of length w. If the 1's form r runs, the castle has
1 + r blocks (the bottom row plus one block per run), so its block count is odd exactly
when r is even, and its sign in "odd minus even" is (-1)^r. The number of binary words of
length w with exactly r runs of 1's is binomial(w+1, 2r) (choose the 2r run endpoints among
the w+1 gaps). Hence, with n = w + 1,

    a(n) = Sum_{r>=0} (-1)^r * binomial(n, 2r) = Re((1+i)^n).

The same count gives the live identity a(n) = A038503(n) - A038505(n): A038503 counts the
odd-block castles (height at most 2) and A038505 the even-block ones (height 2).

## Offsets

- Word / tower reading: valid for n >= 1. For n = 1 the only word is the empty word
  (r = 0), so a(1) = 1. The tower of width 0 is the empty tower, P(1, 0) = 1.
- Castle reading: valid for n >= 2 (a castle has width >= 1). At n = 2 the two castles of
  width 1 are the single block (odd) and the 2-high column (2 blocks, even): a(2) = 1 - 1 = 0.
- a(0) = 1 is not covered by either reading; state the range explicitly.

## The castle object (self-contained definition)

Use the same definition as the live A038503 comment, so the three entries read alike: a
castle is a stack of unit blocks on a grid, whose bottom row is a single block of length
n-1, whose higher blocks have height 1 and rest on the blocks below without overhang, and
in which two neighboring blocks of the same row are separated by a gap. Its height here is
at most 2.

## What is already there (do NOT duplicate)

- `a(n) = Re((1+i)^n)` (Sykora) and `(1+i)^n = a(n) + A009545(n)*i` (Deleham).
- `a(n) = Sum_{n=0..floor(n/2)} binomial(n,2j)*(-1)^j` (Chai Wah Wu, Feb 15 2024) — the
  binomial sum above, already present. (Its summation index is printed as `n`, not `j`;
  not ours to edit.)
- `a(n) = A038503(n) - A038505(n)` (Chaz Reid, Sep 26 2026) — the castle difference in
  formula form, already live.
- Cf. already lists A009545, A038503, A038505.

So the new content is only the **interpretation**: a(n) as a signed castle count (and the
run-counting reason for it). No new formula is needed.

## Draft additions

### Comment (append)

> a(n) is the number of castle polyominoes of width n-1 and height at most 2 with an odd
> number of blocks minus the number with an even number of blocks (Project Euler, Problem
> 502: Counting Castles), for n >= 2. Here a castle is a stack of unit blocks on a grid,
> whose bottom row is a single block of length n-1, whose higher blocks have height 1 and
> rest on the blocks below without overhang, whose height is at most 2, and in which two
> neighboring blocks of the same row are separated by a gap. If the columns that reach
> height 2 form r runs, the castle has 1 + r blocks, and binomial(n, 2*r) castles have r
> runs, so a(n) = Sum_{r>=0} (-1)^r*binomial(n, 2*r).

### Links (optional)

> Project Euler, <a href="https://projecteuler.net/problem=502">Problem 502: Counting Castles</a>

A038505 carries this Link line; A038503 does not. Add it here only if you want the comment's
"Project Euler, Problem 502" reference clickable.

### Crossrefs

No change: A038503, A038505 and A009545 are already in the Cf. list.

## Recommendation

**Submit (Comment only).** It is the one remaining piece of the tier-1 cluster: the castle
reading of A146559 currently has to be assembled from the A038503/A038505 comments and the
`A038503 - A038505` formula. It is also the k = 1 row of the signed tower count P(k, L),
the parity ingredient of the PE 502 castle formula; the k >= 2 rows are not in OEIS
(searched 2026-09-18) and are on the new-sequence list.

## Flags

1. Rewrite in own words and sign `- _Chaz Reid_, Mon D YYYY` with the actual submission
   date (see ../SUBMISSION-NOTES.md §3).
2. Keep the range "for n >= 2" in the castle sentence; the word/tower reading also covers
   n = 1 if you prefer to phrase it that way (then say "for n >= 1").
3. The comment is long; if the editor asks, move the last sentence to FORMULA as
   `a(n) = Sum_{r>=0} (-1)^r*binomial(n, 2*r)` — but the Wu formula already says this, so
   dropping it is also fine.
4. "Problem 502" (not "Project 502").
5. Do not change Name/Data/Offset/Keywords or existing lines.

## Verification script

```python
from itertools import product
from math import comb

A146559 = [1, 1, 0, -2, -4, -4, 0, 8, 16, 16, 0, -32, -64, -64, 0, 128]  # live, n = 0..15

for w in range(0, 15):
    n = w + 1
    signed = odd = even = 0
    for word in product((0, 1), repeat=w):          # columns reaching height 2
        r = sum(1 for i in range(w) if word[i] and (i == 0 or not word[i - 1]))
        signed += (-1) ** r                         # tower blocks = r
        if w >= 1:
            if (1 + r) % 2: odd += 1                # castle blocks = 1 + r
            else: even += 1
    binom = sum((-1) ** r * comb(n, 2 * r) for r in range(n // 2 + 1))
    assert signed == binom == A146559[n]
    if w >= 1:
        assert odd - even == A146559[n]
print("ok")
```
