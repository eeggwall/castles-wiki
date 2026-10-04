# Cross-link draft — A146559 as the signed count of height-2 castles

Status: DRAFT for Charles to reword and submit. OEIS requires human authorship.
Execution notes (field map, signature format, scope): see ../SUBMISSION-NOTES.md.
Checked against the live entry 2026-10-04 (A146559 revision #152, Sep 28 2026).
Rewritten 2026-10-04 to state every castle count at exact height 2.

**SUBMITTED for review 2026-10-04** as "Chaz Reid" (Comment only; resubmitted the same day with the date written `Oct 04 2026`). Final text, reworded and
signed by a person; the draft below is kept as the pre-submission record:

> Among the castle polyominoes of width n-1 and height 2, a(n) - 1 is the number with an
> odd number of blocks minus the number with an even number of blocks (Project Euler,
> Problem 502: Counting Castles), for n >= 2. Here a castle is a stack of unit blocks on a
> grid, whose bottom row is a single block of length n-1, whose higher blocks have height 1
> and rest on the blocks below without overhang, whose maximum height is 2, and in which
> neighboring blocks of the same row are separated by a gap. - _Chaz Reid_, Oct 04 2026

## Identity (verified)

A146559 = "Expansion of (1-x)/(1 - 2*x + 2*x^2)", offset 0, data
`1, 1, 0, -2, -4, -4, 0, 8, 16, 16, 0, -32, -64, -64, 0, 128, ...`.

    a(n) - 1 = odd(n-1, 2) - F(n-1, 2)     for n >= 2,

where F(w, 2) and odd(w, 2) are the numbers of castles of width w and height 2 with an
even and an odd number of blocks. In words: a(n) - 1 is the number of castles of width
n-1 and height 2 with an odd number of blocks minus the number with an even number of
blocks. The 1 is the r = 0 term binomial(n, 0) below. a(0) = a(1) = 1 are not covered.

This is the live formula a(n) = A038503(n) - A038505(n) read at exact height:
A038503(n) - 1 = odd(n-1, 2) and A038505(n) = F(n-1, 2).

Wiki notation: a(n) = P(1, n-1), the signed tower count at k = 1 (towers with column
heights in {0, 1}, the empty word included). Do not use P or "tower" in the comment.

Verified by brute force for w = n-1 = 1..14 (script below).

| n | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| a(n) | 0 | -2 | -4 | -4 | 0 | 8 | 16 | 16 | 0 | -32 | -64 | -64 |
| odd(n-1,2) - F(n-1,2) | -1 | -3 | -5 | -5 | -1 | 7 | 15 | 15 | -1 | -33 | -65 | -65 |

## Proof

A castle of width w and height 2 is determined by which columns reach height 2: a binary
word of length w with at least one 1. If the 1's form r >= 1 runs, the castle has 1 + r
blocks, odd exactly when r is even, so it contributes (-1)^r to "odd minus even". There
are binomial(w+1, 2r) words with r runs. With n = w + 1,

    odd(w, 2) - F(w, 2) = Sum_{r>=1} (-1)^r * binomial(n, 2r) = a(n) - 1,

since a(n) = Re((1+i)^n) = Sum_{r>=0} (-1)^r * binomial(n, 2r) and the r = 0 term is 1.

## What is already there (do NOT duplicate)

- `a(n) = Re((1+i)^n)` (Sykora) and `(1+i)^n = a(n) + A009545(n)*i` (Deleham).
- `a(n) = Sum_{n=0..floor(n/2)} binomial(n,2j)*(-1)^j` (Chai Wah Wu, Feb 15 2024) — the
  binomial sum, already present. (Its summation index is printed as `n`, not `j`; not
  ours to edit.)
- `a(n) = A038503(n) - A038505(n)` (Chaz Reid, Sep 26 2026).
- Cf. already lists A009545, A038503, A038505.

So the new content is only the interpretation. No new formula is needed.

## Draft additions

### Comment (append)

> a(n) - 1 is the number of castle polyominoes of width n-1 and height 2 with an odd
> number of blocks minus the number with an even number of blocks (Project Euler, Problem
> 502: Counting Castles), for n >= 2. Here a castle is a stack of unit blocks on a grid,
> whose bottom row is a single block of length n-1, whose higher blocks have height 1 and
> rest on the blocks below without overhang, whose maximum height is 2, and in which two
> neighboring blocks of the same row are separated by a gap. If the columns that reach
> height 2 form r >= 1 runs, the castle has 1 + r blocks, and binomial(n, 2*r) castles
> have r runs; the 1 is the term binomial(n, 0) of a(n) = Sum_{r>=0} (-1)^r*binomial(n, 2*r).

The definition sentence is the A038505 comment's, word for word.

### Links (optional)

> Project Euler, <a href="https://projecteuler.net/problem=502">Problem 502: Counting Castles</a>

A038505 carries this Link line; A038503 does not.

### Crossrefs

No change: A038503, A038505 and A009545 are already in the Cf. list.

## Recommendation

**Submit (Comment only)**, after the A038503 exact-height correction
(`A038503-exact-height.md`), so the three entries state the castle count the same way.
This is the last piece of the tier-1 cluster, and A146559 is the k = 1 row of the signed
tower count P(k, L), the parity ingredient of the PE 502 castle formula; the k >= 2 rows
are not in OEIS (searched 2026-09-18) and are on the new-sequence list.

## Flags

1. Rewrite in own words and sign `- _Chaz Reid_, Mon DD YYYY` with the actual submission
   date (see ../SUBMISSION-NOTES.md §3).
2. Every castle count in the comment is at exact height 2 ("height 2", "maximum height
   is 2"). Do not write "height at most 2".
3. If the editor finds the comment long, the clause after the semicolon can go: Wu's
   formula already gives the binomial sum.
4. "Problem 502" (not "Project 502").
5. Do not change Name/Data/Offset/Keywords or existing lines.

## Verification script

```python
from itertools import product
from math import comb

A146559 = [1, 1, 0, -2, -4, -4, 0, 8, 16, 16, 0, -32, -64, -64, 0, 128]  # live, n = 0..15

for w in range(1, 15):
    n = w + 1
    odd = even = 0
    for word in product((0, 1), repeat=w):          # columns reaching height 2
        r = sum(1 for i in range(w) if word[i] and (i == 0 or not word[i - 1]))
        if r == 0:
            continue                                # no column reaches 2: not height 2
        if (1 + r) % 2: odd += 1                    # castle blocks = 1 + r
        else: even += 1
    binom = sum((-1) ** r * comb(n, 2 * r) for r in range(n // 2 + 1))
    assert binom == A146559[n]
    assert odd - even == A146559[n] - 1
print("ok")
```
