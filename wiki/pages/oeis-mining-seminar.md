---
title: OEIS mining seminar - one castle sequence, end to end
category: Concepts
summary: A seminar that runs OEIS mining on castle counts, one row at a time. Enumerate castles by brute force; cut the table into rows; look a row up and reject a short false positive (1, 3, 6, 10 also begins the triangular numbers, which give 15 where castles give 16); align the offset, A^e(w, 2) = A038505(w+1) and A^o(w, 2) = A038503(w+1) − 1; prove both by counting runs; reject a relative of the right entry (P(1, L) = A009545(L+3)/2, while the exact match is P(1, L) = A146559(L+1)); and read the next row, A^e(w, 3) = 0, 0, 3, 21, 89, 307, …, through its order-6 recurrence from Berlekamp-Massey and its closed form. One Snippet block reproduces every value.
tags: [concept, castle, seminar, pedagogy, teaching, oeis, offsets, false-positive, berlekamp-massey, hyperbolic-sequence, a038505, a038503, a146559, a009545]
sources: [oeis-encyclopedia]
created: 2026-09-26
updated: 2026-10-29
---

# OEIS mining seminar - one castle sequence, end to end

**Thesis.** A row of castle counts is connected to the rest of mathematics when it equals an entry of the On-Line Encyclopedia of Integer Sequences (OEIS) at an exact offset. Each match is checked at that offset, short coincidences are rejected, and every accepted match is proved; a row is also read through its recurrence and closed form.

**Structure.** Seven stops, 0 to 6: one row that matches, one false match, and one row read through its recurrence. The Snippet block at the end reproduces every value. The method is stated on [[oeis-cross-referencing](pages/oeis-cross-referencing.md)], and the other matches of castle counts against the OEIS are collected on [[oeis-mining-pe502](pages/oeis-mining-pe502.md)].

## Stop 0 - the enumerator

A castle of width `w` and height `h` is a skyline `(c_1, …, c_w)` with `1 ≤ c_i ≤ h` and some `c_i = h`. Its **blocks** are the maximal runs of columns in each row, so its block count is `blocks(c) = c_1 + Σ_{i≥2} max(0, c_i − c_{i−1})` ([[castle-polyomino](pages/castle-polyomino.md)]). Project Euler 502 counts the castles with an even number of blocks,

```
A^e(w, h)  =  #{castles of width w and height h with an even number of blocks},
```

which the problem statement writes `F(w, h)`; `A^o(w, h)` counts those with an odd number. For small sizes the whole algorithm is to list every skyline, count its blocks and keep the even ones ([[project-euler-502-brute-force](pages/project-euler-502-brute-force.md)], [[castle-snippets](pages/castle-snippets.md)]).

*Idea:* every faster method is checked against the enumerator.

## Stop 1 - slice the table

`A^e` is a two-parameter table, and the OEIS indexes one-parameter sequences, so the table is cut into **rows** (fixed `h`), **columns** (fixed `w`) and refinements such as the odd count `A^o` or the count by area. The first row is height 2:

```
A^e(w, 2)  =  1, 3, 6, 10, 16, 28, 56, 120, 256, 528, …        (w = 1, 2, 3, …)
```

*Idea:* rows, columns and complements are the one-parameter slices the OEIS can index.

## Stop 2 - look it up, and reject a short match

The first four terms `1, 3, 6, 10` also begin the **triangular numbers** `1, 3, 6, 10, 15, 21, …` (A000217), and the fifth term separates them: 16, not 15. The row agrees term by term with **A038505**, the sums `Σ_k C(n, 4k+2)` of every fourth binomial coefficient starting at `C(n, 2)`.[^1]

*Idea:* agreement on a few terms is not a match until many more terms agree and a proof explains why.

## Stop 3 - align the offset

A038505 starts `0, 0, 1, 3, 6, 10, 16, 28, 56, …` at `n = 0`, so the castle row is the entry shifted by one:

```
A^e(w, 2)              =  A038505(w + 1)
A^o(w, 2)              =  A038503(w + 1) − 1        (A038503(n) = Σ_k C(n, 4k))
A^e(w, 2) + A^o(w, 2)  =  2^w − 1                   (A000225)
```

All three hold for `w ≤ 12` by enumeration.[^2] A038503 and A038505 are two of the four sums of every fourth binomial coefficient ([[hyperbolic-sequence-family](pages/hyperbolic-sequence-family.md)]).

*Idea:* a match is an identity with an index shift in it, and the shift is tested on every computed term.

## Stop 4 - prove it

A castle of height 2 is the bottom row, one block, together with a binary string of length `w` that marks the columns of height 2 and contains at least one `1`. If the `1`s form `r` runs, the castle has `1 + r` blocks. The binary strings of length `w` with `r` runs of `1`s number `C(w + 1, 2r)`, one for each choice of the `2r` run ends among the `w + 1` gaps between and around the columns. So:[^3]

```
blocks even  ⇔  r odd         ⇔  2r ≡ 2 (mod 4)     ⇒     A^e(w, 2)  =  Σ_k C(w+1, 4k+2)    =  A038505(w+1)
blocks odd   ⇔  r even, r > 0                       ⇒     A^o(w, 2)  =  Σ_{k≥1} C(w+1, 4k)  =  A038503(w+1) − 1
```

For `w ≤ 4` only `k = 0` contributes, so `A^e(w, 2) = C(w + 1, 2)` is the triangular number; at `w = 5`, `A^e(5, 2) = C(6, 2) + C(6, 6) = 15 + 1 = 16`, and the extra castle is `(2, 1, 2, 1, 2)`, the first with three runs of height-2 columns.

*Idea:* the lookup suggests the identity, and a counting argument proves it.

## Stop 5 - a relative of the right entry

The signed tower count `P(1, L)`, the sum of `(−1)^{blocks}` over the towers of height at most 1 on a base of length `L`, enters `A^e(w, 2)` and `A^e(w, 3)` ([[castle-notation](pages/castle-notation.md)]). Its values are `1, 0, −2, −4, −4, 0, 8, 16, …`. **A009545**, the imaginary parts `Im((1+i)^n)`, is a tempting match: `A009545(L + 1)` and `P(1, L)` are both 1 at `L = 0`, and they differ from `L = 1` on ([[signed-tower-count](pages/signed-tower-count.md)]):

```
P(1, L)         =  1, 0, −2, −4, −4,  0,  8, 16, …     =  Re((1+i)^{L+1})  =  A146559(L+1)
A009545(L+1)    =  1, 2,  2,  0, −4, −8, −8,  0, …     (the imaginary parts: not a match)
```

The rejected entry is related to the right one. Since `(1+i)^{L+3} = 2i·(1+i)^{L+1}`, `P(1, L) = A009545(L+3)/2`, a shift and a halving. The entry that matches with no shift or scale is A146559.[^4] A009545 also has a castle reading of its own: splitting `P(1, L)` by the parity of the last column gives `P_even(1, L) = A146559(L)` and `P_odd(1, L) = −A009545(L)` ([[tower-parity-sectors](pages/tower-parity-sectors.md)], Part 3). So `A009545(w)` is the number of castles of width `w` and height 2 with `c_w = 2` and an even number of blocks, minus the number with an odd number.

*Idea:* an entry that matches only after a shift and a scale is a cross-reference, and the match is the entry that agrees exactly.

## Stop 6 - a row read through its recurrence

The next row is height 3:

```
A^e(w, 3)  =  0, 0, 3, 21, 89, 307, 977, 3031, 9321, 28479, 86505, 261615, 788969, …
```

The Berlekamp-Massey algorithm finds the shortest linear recurrence of the terms ([[berlekamp-massey](pages/berlekamp-massey.md)]):

```
a(n) = 8a(n−1) − 27a(n−2) + 54a(n−3) − 70a(n−4) + 56a(n−5) − 24a(n−6)
characteristic polynomial  (x − 3)(x − 2)(x² − x + 2)(x² − 2x + 2)
```

Each factor comes from the closed form `A^e(w, 3) = (3^w − 2^w − P(2, w) + P(1, w))/2` ([[castle-counting-formula](pages/castle-counting-formula.md)], Equation (1)): `x − 3` and `x − 2` from `3^w − 2^w`, which is `A(w, 3)` (A001047), and the rest from `char_2(x) = (x − 2)(x² − x + 2)` and `char_1(x) = x² − 2x + 2`, the characteristic polynomials of `P(2, ·)` and `P(1, ·)`. The odd count `A^o(w, 3)` has a recurrence of order 5, since its components at the root 2 cancel ([[new-sequence-fw3](pages/new-sequence-fw3.md)]).[^5]

*Idea:* the recurrence of a row, its generating function and its closed form come from the closed form of `A^e(w, h)`.

## Summary table

| sequence | terms | lookup | outcome |
|---|---|---|---|
| `A^e(w, 2)` | `1, 3, 6, 10, 16, 28, …` | A000217 agrees for 4 terms; A038505 | `A038505(w+1)`, proved by counting runs |
| `A^o(w, 2)` | `0, 0, 1, 5, 15, 35, …` | A038503 | `A038503(w+1) − 1`, proved by counting runs |
| `P(1, L)` | `1, 0, −2, −4, −4, 0, …` | A009545 agrees at `L = 0` only; A146559 | match `A146559(L+1)`; `P(1, L) = A009545(L+3)/2`, and `−A009545` is the odd-last-column part |
| `A^e(w, 3)` | `0, 0, 3, 21, 89, 307, …` | - | an order-6 recurrence and a closed form |

## Snippet

One block reproduces the summary table: the enumerator, the two height-2 identities, the split of `2^w − 1`, the comparison of `P(1, L)` with A009545, and Berlekamp-Massey on `A^e(w, 3)`. `all_castles`, `blocks` and `berlekamp_massey` are the versions on [[castle-snippets](pages/castle-snippets.md)] and [[castle-snippets-number-theory](pages/castle-snippets-number-theory.md)]. The two OEIS entries are computed from their binomial-sum definitions, so no network is needed.

```python
from itertools import product
from fractions import Fraction
from math import comb

def all_castles(w, h):                     # skylines of width w, every column >= 1, some column h
    return [c for c in product(range(1, h+1), repeat=w) if max(c) == h]

def blocks(c):                             # each rise in the skyline starts new blocks
    return c[0] + sum(max(0, c[i] - c[i-1]) for i in range(1, len(c)))

def Ae(w, h):                              # castles with an even number of blocks
    return sum(1 for c in all_castles(w, h) if blocks(c) % 2 == 0)

def Ao(w, h):                              # castles with an odd number of blocks
    return sum(1 for c in all_castles(w, h) if blocks(c) % 2 == 1)

A038505 = lambda n: sum(comb(n, k) for k in range(2, n+1, 4))      # every 4th binomial, from C(n, 2)
A038503 = lambda n: sum(comb(n, k) for k in range(0, n+1, 4))      # every 4th binomial, from C(n, 0)

def berlekamp_massey(s):                   # shortest linear recurrence over Q
    s = [Fraction(v) for v in s]
    C, B, L, m, b = [Fraction(1)], [Fraction(1)], 0, 1, Fraction(1)
    for N in range(len(s)):
        d = s[N] + sum(C[i]*s[N-i] for i in range(1, L+1))
        if d == 0: m += 1; continue
        T = C[:]; C += [Fraction(0)]*max(0, len(B)+m-len(C))
        for j in range(len(B)): C[j+m] -= (d/b)*B[j]
        if 2*L <= N: L, B, b, m = N+1-L, T, d, 1
        else: m += 1
    return C[:L+1], L
```

```
>>> [Ae(w, 2) for w in range(1, 11)]
[1, 3, 6, 10, 16, 28, 56, 120, 256, 528]
>>> [A038505(n) for n in range(12)]
[0, 0, 1, 3, 6, 10, 16, 28, 56, 120, 256, 528]
>>> all(Ae(w, 2) == A038505(w + 1) and Ao(w, 2) == A038503(w + 1) - 1 for w in range(1, 13))
True
>>> [(w, Ae(w, 2) + Ao(w, 2), 2**w - 1) for w in (4, 8)]
[(4, 15, 15), (8, 255, 255)]
>>> P1 = [int(((1 + 1j)**(L + 1)).real) for L in range(8)]          # P(1, L) = Re((1+i)^(L+1))
>>> A009545 = [int(((1 + 1j)**n).imag) for n in range(11)]          # Im((1+i)^n)
>>> P1, A009545[1:9]
([1, 0, -2, -4, -4, 0, 8, 16], [1, 2, 2, 0, -4, -8, -8, 0])
>>> all(2 * P1[L] == A009545[L + 3] for L in range(8))
True
>>> F3 = [Ae(w, 3) for w in range(1, 14)]; F3
[0, 0, 3, 21, 89, 307, 977, 3031, 9321, 28479, 86505, 261615, 788969]
>>> berlekamp_massey(F3)
([Fraction(1, 1), Fraction(-8, 1), Fraction(27, 1), Fraction(-54, 1), Fraction(70, 1), Fraction(-56, 1), Fraction(24, 1)], 6)
>>> all(Ae(w, 3) + Ao(w, 3) == 3**w - 2**w for w in range(1, 10))
True
```

## Exercises

1. Find the smallest `w` at which `A^o(w, 2)` differs from `C(w + 1, 4)`, and list the castles that make the difference.
2. Compute `A^o(w, 3)` for `w ≤ 13` and run `berlekamp_massey` on it. Show that its order is 5 by writing `A^o = (A − S)/2` with `S(w, 3) = P(1, w) − P(2, w)` and checking which roots cancel ([[odd-castles-and-block-tables](pages/odd-castles-and-block-tables.md)]).

## Related Concepts

- [[oeis-mining-pe502](pages/oeis-mining-pe502.md)] - the other matches of castle counts against the OEIS.
- [[oeis-height2-hyperbolic-castles](pages/oeis-height2-hyperbolic-castles.md)] - the height-2 identities `A^e(w, 2) = A038505(w+1)` and `A^o(w, 2) = A038503(w+1) − 1`, and the castle comments of their OEIS entries.
- [[new-sequence-fw3](pages/new-sequence-fw3.md)] - the row `A^e(·, 3)` with its recurrence and characteristic polynomial.
- [[oeis-cross-referencing](pages/oeis-cross-referencing.md)] - the two checks of the method, offsets and short prefixes.
- [[castle-sequence-catalog](pages/castle-sequence-catalog.md)] / [[oeis-index](pages/oeis-index.md)] - every castle sequence with its terms, and every A-number the wiki cites.
- [[signed-tower-count](pages/signed-tower-count.md)] - `P(1, L) = A146559(L+1)` and the rows `P(k, ·)`.
- [[hyperbolic-sequence-family](pages/hyperbolic-sequence-family.md)] - the four sums of every fourth binomial coefficient, two of which count the castles of height 2.
- [[berlekamp-massey](pages/berlekamp-massey.md)] - the algorithm of Stop 6, and when its output is the shortest recurrence.
- [[castle-counting-formula](pages/castle-counting-formula.md)] - the closed form of `A^e(w, h)` behind the factors of Stop 6.
- [[castle-eigenvalue-oeis-crosswalk](pages/castle-eigenvalue-oeis-crosswalk.md)] / [[odd-castles-and-block-tables](pages/odd-castles-and-block-tables.md)] - the same method on eigenvalue convergents, on the odd count and on the block-count tables.
- [[hardin-identity-seminar](pages/hardin-identity-seminar.md)] / [[hear-the-shape-seminar](pages/hear-the-shape-seminar.md)] / [[castle-fibers-char-2-walkthrough](pages/castle-fibers-char-2-walkthrough.md)] / [[tower-recursion-master-class](pages/tower-recursion-master-class.md)] / [[one-bit-seminar](pages/one-bit-seminar.md)] / [[q-thread-seminar](pages/q-thread-seminar.md)] / [[half-derivative-seminar](pages/half-derivative-seminar.md)] - the other seminar pages.
- [[sandcastle-seminar](pages/sandcastle-seminar.md)] - a seminar on the 16-cell castle `(3, 2, 1, 2, 2, 1, 2, 3)`, silver by spectrum, through its sandpile group, clock, identity and avalanches.
- [[pell-castle-strip](pages/pell-castle-strip.md)] / [[castle-cryptography](pages/castle-cryptography.md)] / [[song-as-castle](pages/song-as-castle.md)] - the seminar pages on the Pell strip, castle cryptography, and audio as castles.

## Footnotes

[^1]: https://oeis.org/A038505 and https://oeis.org/A000217 (read 2026-10-16) - A038505 is "Sum of every 4th entry of row n in Pascal's triangle, starting at binomial(n,2)" (`0, 0, 1, 3, 6, 10, 16, 28, 56, 120, …`); A000217 is the triangular numbers (`0, 1, 3, 6, 10, 15, …`).
[^2]: Verified by execution (Python 3.11, 2026-10-16): `A^e(w, 2) = A038505(w+1)`, `A^o(w, 2) = A038503(w+1) − 1` and `A^e + A^o = 2^w − 1` for every `w ≤ 12`, by enumeration against the binomial-sum definitions; every output of the Snippet block; the order 5 of `A^o(w, 3)` for `w ≤ 13`.
[^3]: Verified by execution (Python 3.11, 2026-10-25): for `w ≤ 14`, the binary strings of length `w` with `r` runs of `1`s number `C(w + 1, 2r)`, and the castles of width `w` and height 2 with an even and with an odd number of blocks number `Σ_k C(w+1, 4k+2)` and `Σ_{k≥1} C(w+1, 4k)`, which equal `A038505(w+1)` and `A038503(w+1) − 1` in the OEIS data.
[^4]: https://oeis.org/A009545 and https://oeis.org/A146559 (read 2026-10-25) - A009545 is "Expansion of e.g.f. sin(x)*exp(x)" with "Imaginary part of (1+i)^n"; A146559 is "Expansion of (1-x)/(1 - 2*x + 2*x^2)" with "(1+i)^n = a(n) + A009545(n)*i" and "a(n) = Re( (1+i)^n )".
[^5]: Verified by execution (Python 3.11 with SymPy, 2026-10-25): Berlekamp-Massey on 60 terms of `A^e(·, 3)` gives order 6 with characteristic polynomial `(x − 3)(x − 2)(x² − x + 2)(x² − 2x + 2)`, and on 60 terms of `A^o(·, 3)` order 5; the recurrence holds for `7 ≤ w ≤ 50`; the recurrence is re-derived by `berlekamp_massey` in the Snippet.
