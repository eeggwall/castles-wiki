---
title: OEIS mining seminar - one castle sequence, end to end
category: Concepts
summary: The seminar walk-through for the "OEIS mining as a research method" arc - the whole method run on castle sequences at one blackboard. Enumerate castles by brute force; slice the table into rows; look a row up in the On-Line Encyclopedia of Integer Sequences (OEIS) and dodge the short false positive (1, 3, 6, 10 is also the triangular numbers, until 16); align the offset exactly, F(w,2) = A038505(w+1) and odd(w,2) = A038503(w+1) − 1; prove it with a runs-counting argument; learn from the trap the wiki fell into (P(1,L) was claimed as A009545, which agrees at the first term and is really a shifted, halved relative, P(1,L) = A009545(L+3)/2, while the exact match is A146559(L+1)); handle a non-match (F(w,3) = 0, 0, 3, 21, 89, 307, … has no entry, so Berlekamp-Massey finds its order-6 recurrence and it becomes a new-sequence candidate); and finish with the human step, since OEIS text must be written and signed by a person (the height-2 comments were submitted 2026-09-18). One runnable block pins every value.
tags: [concept, castle, seminar, pedagogy, teaching, oeis, interlinking, generation, offsets, false-positive, berlekamp-massey, hyperbolic-sequence, a038505, a038503, a146559, a009545]
sources: [oeis-mining-pe502, oeis-height2-hyperbolic-castles, new-sequence-fw3]
created: 2026-09-26
updated: 2026-09-26
---

# OEIS mining seminar - one castle sequence, end to end

**Thesis.** A counting problem becomes connected to the rest of mathematics one sequence at a time. Compute a sequence, look it up in the On-Line Encyclopedia of Integer Sequences (OEIS), and either **interlink** (an existing entry gains a new meaning) or **generate** (a new entry is proposed). The method is simple, and the discipline is where the value lies: exact offsets, rejecting coincidences, proving every match, and leaving the final text to a human.

**Format.** About 60 minutes at one blackboard, seven stops: one sequence that matches, one trap, one sequence that does not match, and the submission. Every value quoted is pinned by the Snippet block at the end. The method page is [[oeis-cross-referencing](pages/oeis-cross-referencing.md)], and the full first pass is [[oeis-mining-pe502](pages/oeis-mining-pe502.md)].

## Stop 0 - the machine

A castle of width `w` and height `h` is a skyline of column heights in `{1, …, h}` with at least one column of height `h`. Its **blocks** are the horizontal runs of cells, row by row, and each rise in the skyline starts new ones. The Project Euler 502 question is about castles with an **even** number of blocks:

```
F(w, h)  =  #{castles of width w, height h, even number of blocks}
```

For small sizes, brute force is the whole algorithm: list every skyline, count its blocks, keep the even ones ([[project-euler-502-brute-force](pages/project-euler-502-brute-force.md)], [[castle-snippets](pages/castle-snippets.md)]).

*Idea:* a slow, obviously correct enumerator is the first research tool. Every clever method is checked against it.

## Stop 1 - slice the table

`F` is a two-parameter table. The OEIS indexes one-parameter sequences, so cut the table into **rows** (fix `h`, vary `w`), **columns** (fix `w`), and refinements (odd blocks, by area, …). Start with the smallest interesting row, height 2:

```
F(w, 2)  =  1, 3, 6, 10, 16, 28, 56, 120, 256, 528, …        (w = 1, 2, 3, …)
```

*Idea:* choose slices the OEIS is likely to know: rows, columns, diagonals, and complements such as the odd count.

## Stop 2 - look it up, and do not trust the first hit

The first four terms `1, 3, 6, 10` are also the **triangular numbers** `1, 3, 6, 10, 15, 21, …`, a false positive that breaks at the fifth term (16, not 15). The row agrees term for term with **A038505**, "sum of every 4th binomial coefficient starting at `C(n, 2)`": `Σ_k C(n, 4k+2)`.[^1]

The wiki's first pass rejected several such coincidences: "sqrt(5) difference" sequences and decimal-expansion hits on short block distributions that agreed on a few terms for no reason.[^2]

*Idea:* a match on four terms is a coincidence until it matches on many terms and has a reason.

## Stop 3 - align the offset, exactly

A038505 starts `0, 0, 1, 3, 6, 10, 16, 28, 56, …` at `n = 0`, so the castle row is the entry shifted by one:

```
F(w, 2)    =  A038505(w + 1)
odd(w, 2)  =  A038503(w + 1) − 1              (A038503 = Σ_k C(n, 4k), the "every 4th, from C(n,0)" sibling)
F + odd    =  2^w − 1                          (A000225, all height-2 castles)
```

Checked term by term for `w ≤ 12`.[^3] The height-2 castles split the Mersenne numbers `2^w − 1` by block parity into two otherwise isolated entries of the order-4 "hyperbolic" family ([[hyperbolic-sequence-family](pages/hyperbolic-sequence-family.md)]).

*Idea:* a match is a statement with an index shift in it. Write the shift down and test it on every available term.

## Stop 4 - prove it

A height-2 castle is a bottom row (one block) plus a choice of which columns reach height 2, that is, a binary string of length `w` with at least one `1`. If the `1`s form `r` runs, there are `1 + r` blocks. The number of length-`w` strings with exactly `r` runs of `1`s is `C(w + 1, 2r)`: choose the `2r` run boundaries among the `w + 1` gaps. So:

```
blocks even  ⇔  r odd  ⇔  2r ≡ 2 (mod 4)      ⇒      F(w, 2) = Σ_k C(w+1, 4k+2) = A038505(w+1)
blocks odd   ⇔  r even, r > 0                  ⇒      odd(w, 2) = Σ_{k≥1} C(w+1, 4k) = A038503(w+1) − 1
```

That is the whole proof.[^4] A match with a proof is a new **interpretation** of the entry. Here it was the first geometric reading of two sequences whose existing comments were all algebraic ([[oeis-height2-hyperbolic-castles](pages/oeis-height2-hyperbolic-castles.md)]).

*Idea:* the lookup suggests the identity, and a short bijective or counting argument makes it a theorem.

## Stop 5 - the trap

The signed tower count `P(1, L)` (towers of height `≤ 1`, weighted by `(−1)^{blocks}`) is `1, 0, −2, −4, −4, 0, 8, 16, …`. A plan claimed it was **A009545**, `Im((1+i)^n)`. At `L = 0` both give 1, so a first-term check passes. The offset-exact comparison fails from `L = 1` on ([[signed-tower-count](pages/signed-tower-count.md)]):

```
P(1, L)            =  1, 0, −2, −4, −4,  0,  8, 16, …        =  Re((1+i)^(L+1))  =  A146559(L+1)
A009545(L+1)       =  1, 2,  2,  0, −4, −8, −8,  0, …        (the imaginary part: not a match)
```

The rejected sequence is not unrelated either. Since `(1+i)^{L+3} = 2i·(1+i)^{L+1}`, it is exactly `P(1, L) = A009545(L+3)/2`. So the wrong claim was a **shifted, halved relative**, and the right entry is the one that matches with no shift or scale, A146559.[^5] The relative even has a castle meaning of its own. Split `P(1, L)` by the parity of the last column: the even part is `A146559(L)` and the odd part is `−A009545(L)`, so `P(1, L) = A146559(L) − A009545(L)` ([[tower-parity-sectors](pages/tower-parity-sectors.md)], Part 3). The sequence the plan wrongly claimed is a genuine castle count, just not this one.

*Idea:* the most dangerous false positive is a relative of the right answer. Prefer the entry that matches exactly, and record relatives as cross-references rather than matches.

## Stop 6 - when nothing matches

The next row, height 3, has no OEIS entry:

```
F(w, 3)  =  0, 0, 3, 21, 89, 307, 977, 3031, 9321, 28479, 86505, 261615, 788969, …
```

A search for `3, 21, 89, 307, 977, 3031` returned nothing on 2026-09-19.[^6] A non-match is a **generation** candidate, but it needs a structure worth recording first. Feed the terms to Berlekamp–Massey ([[berlekamp-massey](pages/berlekamp-massey.md)]), which finds the shortest linear recurrence:

```
a(n) = 8a(n−1) − 27a(n−2) + 54a(n−3) − 70a(n−4) + 56a(n−5) − 24a(n−6)
characteristic polynomial (x − 3)(x − 2)(x² − x + 2)(x² − 2x + 2)
```

Every factor has a meaning. `3^w` and `2^w` come from the all-parity counts, `x² − x + 2` and `x² − 2x + 2` are the signed tower counts `P(2, ·)` and `P(1, ·)`, and the closed form is `F(w, 3) = (3^w − 2^w − P(2, w) + P(1, w))/2`. Its complement satisfies `F(w, 3) + odd(w, 3) = 3^w − 2^w` (A001047), which is itself an interlink ([[new-sequence-fw3](pages/new-sequence-fw3.md)]).[^7]

*Idea:* a new sequence is worth proposing when it comes with its recurrence, its generating function and its meaning, not just terms.

## Stop 7 - the human step

OEIS text must be **written and signed by a person**. A tool may verify terms, check offsets and format data, but may not author the prose.[^8] New contributors are also throttled to a few open drafts, so submissions go in order of value: the isolated, clean interlinks first. The wiki keeps verified identities on its pages and draft text in `raw/oeis-pe502/`, to be rewritten by a person.

The height-2 interlink went through this: drafted, rewritten and signed by a person, and submitted to A038503 and A038505 on 2026-09-18, with the A038503 comment rephrased as "height at most 2" so the `− 1` disappears ([[oeis-height2-hyperbolic-castles](pages/oeis-height2-hyperbolic-castles.md)], "Submitted to OEIS"). The status of every castle sequence (known, interlink, novel candidate, unchecked) is tracked on [[castle-sequence-catalogue](pages/castle-sequence-catalogue.md)], and every A-number the wiki cites is listed on [[oeis-index](pages/oeis-index.md)].

*Idea:* the machine finds and checks. The person writes and signs, and the wiki keeps the verified mathematics separate from the prose.

## The board

| sequence | terms | lookup | outcome |
|---|---|---|---|
| `F(w, 2)` | `1, 3, 6, 10, 16, 28, …` | A000217 agrees for 4 terms (false), A038505 | **interlink**, offset `w + 1`, proved by counting runs, submitted 2026-09-18 |
| `odd(w, 2)` | `0, 0, 1, 5, 15, 35, …` | A038503 | **interlink**, `A038503(w+1) − 1` |
| `P(1, L)` | `1, 0, −2, −4, −4, 0, …` | A009545 claimed (wrong), A146559 | **interlink** A146559(L+1); A009545 is the odd-last-column part, and `A009545(L+3)/2` a relative |
| `F(w, 3)` | `0, 0, 3, 21, 89, 307, …` | none (2026-09-19) | **generation candidate**, order-6 recurrence, closed form |

## Snippet

One block reproduces the board: the enumerator, the two height-2 identities, the Mersenne split, the `P(1, L)` trap and its halved relative, and Berlekamp–Massey on `F(w, 3)`. `all_castles`, `blocks` and `berlekamp_massey` are the versions on [[castle-snippets](pages/castle-snippets.md)] and [[castle-snippets-number-theory](pages/castle-snippets-number-theory.md)]. The two OEIS entries are computed from their binomial-sum definitions, so no network is needed.

```python
from itertools import product
from fractions import Fraction
from math import comb

def all_castles(w, h):                     # skylines of width w, every column >= 1, height exactly h
    return [c for c in product(range(1, h+1), repeat=w) if max(c) == h]

def blocks(c):                             # each rise in the skyline starts new blocks
    return c[0] + sum(max(0, c[i] - c[i-1]) for i in range(1, len(c)))

def F(w, h):                               # castles with an even number of blocks
    return sum(1 for c in all_castles(w, h) if blocks(c) % 2 == 0)

def odd(w, h):
    return sum(1 for c in all_castles(w, h) if blocks(c) % 2 == 1)

A038505 = lambda n: sum(comb(n, k) for k in range(2, n+1, 4))      # sum of every 4th binomial, from C(n,2)
A038503 = lambda n: sum(comb(n, k) for k in range(0, n+1, 4))      # ... from C(n,0)

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
>>> [F(w, 2) for w in range(1, 11)]
[1, 3, 6, 10, 16, 28, 56, 120, 256, 528]
>>> [A038505(n) for n in range(12)]
[0, 0, 1, 3, 6, 10, 16, 28, 56, 120, 256, 528]
>>> all(F(w, 2) == A038505(w + 1) and odd(w, 2) == A038503(w + 1) - 1 for w in range(1, 13))
True
>>> [(w, F(w, 2) + odd(w, 2), 2**w - 1) for w in (4, 8)]
[(4, 15, 15), (8, 255, 255)]
>>> P1 = [int(((1 + 1j)**(L + 1)).real) for L in range(8)]          # P(1, L) = Re((1+i)^(L+1))
>>> A009545 = [int(((1 + 1j)**n).imag) for n in range(11)]          # Im((1+i)^n)
>>> P1, A009545[1:9]
([1, 0, -2, -4, -4, 0, 8, 16], [1, 2, 2, 0, -4, -8, -8, 0])
>>> all(2 * P1[L] == A009545[L + 3] for L in range(8))
True
>>> F3 = [F(w, 3) for w in range(1, 14)]; F3
[0, 0, 3, 21, 89, 307, 977, 3031, 9321, 28479, 86505, 261615, 788969]
>>> berlekamp_massey(F3)
([Fraction(1, 1), Fraction(-8, 1), Fraction(27, 1), Fraction(-54, 1), Fraction(70, 1), Fraction(-56, 1), Fraction(24, 1)], 6)
>>> all(F(w, 3) + odd(w, 3) == 3**w - 2**w for w in range(1, 10))
True
```

## Exercises for the room

1. Where exactly does `F(w, 2)` leave the triangular numbers, and what property of castles makes the fifth term 16 instead of 15?
2. Compute `odd(w, 3)` for `w ≤ 13` and run `berlekamp_massey` on it. Why is its order 5, one less than `F(w, 3)`? ([[odd-castles-and-block-tables](pages/odd-castles-and-block-tables.md)])
3. Write the `P(1, L)` trap as a general rule: if `a(n)` matches a sequence `b` only after a shift and a scale, when is that an interlink and when is it a cross-reference?
4. Pick an unchecked row from [[castle-sequence-catalogue](pages/castle-sequence-catalogue.md)], compute 12 terms, and run the whole method on it.

## What is still open

These are the open items feeding Arc 7 in `IDEAS.md`: the `h ≥ 5` tree-castle-by-area rows (no OEIS match yet), and the unfiled tower-spacing cells on [[tower-spacing-castles](pages/tower-spacing-castles.md)], which are submission material. Submissions themselves are a human action.

## Appearances in Sources

- [[oeis-mining-pe502](pages/oeis-mining-pe502.md)] - the first-pass mining and its discipline notes.
- [[oeis-height2-hyperbolic-castles](pages/oeis-height2-hyperbolic-castles.md)] - the height-2 interlink and its submission.
- [[new-sequence-fw3](pages/new-sequence-fw3.md)] - the height-3 generation candidate.

## Related Concepts

- [[oeis-cross-referencing](pages/oeis-cross-referencing.md)] - the method and its rules; this page is its classroom version.
- [[castle-sequence-catalogue](pages/castle-sequence-catalogue.md)] / [[oeis-index](pages/oeis-index.md)] - where every sequence's status and every cited A-number live.
- [[signed-tower-count](pages/signed-tower-count.md)] - the `P(1, L)` correction.
- [[hyperbolic-sequence-family](pages/hyperbolic-sequence-family.md)] - the order-4 family the height-2 castles join.
- [[berlekamp-massey](pages/berlekamp-massey.md)] - the recurrence finder of Stop 6.
- [[castle-eigenvalue-oeis-crosswalk](pages/castle-eigenvalue-oeis-crosswalk.md)] / [[odd-castles-and-block-tables](pages/odd-castles-and-block-tables.md)] - the method run on eigenvalue convergents and on the odd and joint tables.
- [[hardin-identity-seminar](pages/hardin-identity-seminar.md)] / [[hear-the-shape-seminar](pages/hear-the-shape-seminar.md)] / [[castle-fibers-char-2-walkthrough](pages/castle-fibers-char-2-walkthrough.md)] / [[tower-recursion-master-class](pages/tower-recursion-master-class.md)] - the other seminar pages.

## Footnotes

[^1]: https://oeis.org/A038505 and https://oeis.org/A000217 - A038505 is `Sum_{k} binomial(n, 4k+2)` (`0, 0, 1, 3, 6, 10, 16, 28, 56, 120, …`); A000217 is the triangular numbers (`0, 1, 3, 6, 10, 15, …`). The castle row and A038505 are recomputed in the Snippet from the binomial-sum definition.
[^2]: [[oeis-mining-pe502](pages/oeis-mining-pe502.md)] `mine-notes.md` §"Method notes (interlinking discipline)" L175-182 - "checked against the actual OEIS data with offsets, not just the first few terms ... The false positives seen during search (A325842, A325668 "sqrt(5) difference sequences"; decimal-expansion/Collatz hits on short block distributions) were rejected".
[^3]: Verified by execution (Python 3.10, 2026-09-26): `F(w, 2) = A038505(w+1)` and `odd(w, 2) = A038503(w+1) − 1` for every `w ≤ 12` by brute-force enumeration against the binomial-sum definitions, and `F + odd = 2^w − 1`, as pinned in the Snippet.
[^4]: [[oeis-height2-hyperbolic-castles](pages/oeis-height2-hyperbolic-castles.md)] `oeis-xref-draft.md` §0 L35-42 - "1 + r, where r = number of runs of height-2 columns. #strings of length w with exactly r runs of 1's = binomial(w+1, 2r). Even block count <=> 1 + r even <=> r odd <=> 2r = 2 mod 4, so F(w,2) = A038505(w+1) ... odd(w,2) = A038503(w+1) - 1".
[^5]: https://oeis.org/A009545 and https://oeis.org/A146559 - A009545 is the expansion whose terms are `Im((1+i)^n)`, and A146559 is `Re((1+i)^n)` with generating function `(1−x)/(1−2x+2x²)`. The claim-and-correction is recorded on [[oeis-mining-pe502](pages/oeis-mining-pe502.md)] `mine-notes.md` §"Vein 1" L21-28. The halved-relative identity `P(1, L) = A009545(L+3)/2` was verified by execution for `L < 30` (2026-09-26) and follows from `(1+i)² = 2i`.
[^6]: https://oeis.org/search?q=3,21,89,307,977,3031 (2026-09-19) - the term search returned no matching sequence, as recorded on [[new-sequence-fw3](pages/new-sequence-fw3.md)].
[^7]: [[new-sequence-fw3](pages/new-sequence-fw3.md)] `new-sequence-F3.md` §"Formula" L63-68 - "a(n) = 8*a(n-1) - 27*a(n-2) + 54*a(n-3) - 70*a(n-4) + 56*a(n-5) - 24*a(n-6) ... Characteristic polynomial (x-3)(x-2)(x^2-x+2)(x^2-2x+2)"; the recurrence is re-derived by `berlekamp_massey` in the Snippet, and `F + odd = 3^w − 2^w` is checked there for `w ≤ 9`.
[^8]: [[oeis-mining-pe502](pages/oeis-mining-pe502.md)] `SUBMISSION-NOTES.md` §"Mechanical vs human" L41-44 - "A tool may: run the verification scripts, check offsets against the live entries, format data. It may NOT author the prose. Only a human may: rewrite the draft prose in their own words, sign it, and submit. OEIS forbids AI-authored text".
