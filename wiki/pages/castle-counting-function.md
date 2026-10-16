---
title: Castle counts A(w,h), A^e(w,h) and A^o(w,h)
category: Concepts
summary: The castle counts A(w, h) = h^w − (h−1)^w, A^e(w, h) and A^o(w, h) of castles of width w and height h, all of them, those with an even number of blocks, and those with an odd number. A^e is the Project Euler 502 count F(w, h); the problem gives four checkpoint values and asks for A^e(10^12, 100) + A^e(10^4, 10^4) + A^e(100, 10^12) mod 10^9 + 7. At height 2, A^e(w, 2) = A038505(w+1) and A^o(w, 2) = A038503(w+1) − 1.
tags: [concept, castle, counting-function, project-euler]
sources: [project-euler-502, project-euler-502-problem-setup, project-euler-502-representations, project-euler-502-solution, project-euler-502-brute-force, oeis-mining-pe502]
created: 2026-09-13
updated: 2026-10-16
---

# Castle counts A(w,h), A^e(w,h) and A^o(w,h)

## The counts

For a [[castle-polyomino](pages/castle-polyomino.md)] of width `w` and height `h`, the wiki counts[^1]

- `A(w, h) = h^w − (h−1)^w`, the castles of width `w` and height `h`;
- `A^e(w, h)`, those with an even number of blocks;
- `A^o(w, h)`, those with an odd number of blocks, so `A = A^e + A^o`.

Project Euler 502 asks for `A^e(w, h)`, which the problem statement writes `F(w, h)`.[^2] The source's own notation is `A(w, h)` for all castles and `F(w, h)` for the even-block ones, and its reference module computes `A^o` as `F_odd`.[^3] The signed count `S = A^e − A^o` and the other symbols are on [[castle-notation](pages/castle-notation.md)].

*Example.* At width 3 and height 2, `A(3, 2) = 8 − 1 = 7`. The castle `(2, 1, 2)` has three blocks and the other six have two, so `A^e(3, 2) = 6` and `A^o(3, 2) = 1`.

## Checkpoints and the target

The problem statement gives four values:[^4]

| `(w, h)` | `A^e(w, h)` |
|---|---|
| `(4, 2)` | 10 |
| `(13, 10)` | 3 729 050 610 636 |
| `(10, 13)` | 37 959 702 514 |
| `(100, 100)` | 841 913 936 (mod `1 000 000 007`) |

and asks for[^5]

```
( A^e(10^12, 100) + A^e(10000, 10000) + A^e(100, 10^12) )  mod  1 000 000 007.
```

The [[castle-counting-formula](pages/castle-counting-formula.md)] gives `A^e(w, h)` in closed form through the signed tower count `P(k, L)`, and reproduces all four values. [[castle-count-algorithms](pages/castle-count-algorithms.md)] evaluates the three terms of the target: `A^e(10^12, 100)` and `A^e(10000, 10000)` from the rational generating function of `P(h−1, ·)`, and `A^e(100, 10^12)` from a recurrence in the tower height found by Berlekamp-Massey.[^6] The source records the value of the target only as a base64 checksum, and the wiki does not reproduce it ([[project-euler-502-solution](pages/project-euler-502-solution.md)]).

## Rows in the OEIS

- For each height `h`, `A(·, h)` is a difference of powers: `A000225` (`2^n − 1`) at `h = 2`, `A001047` (`3^n − 2^n`) at `h = 3`, `A005061` (`4^n − 3^n`), `A005060` (`5^n − 4^n`) and `A005062` (`6^n − 5^n`) at `h = 4, 5, 6`.[^7]
- At height 2, `A^e(·, 2)` and `A^o(·, 2)` are shifts of `A038505` and `A038503` (section *Height 2*).
- [[new-sequence-fw3](pages/new-sequence-fw3.md)] treats the row `A^e(·, 3)`, and [[castle-sequence-catalogue](pages/castle-sequence-catalogue.md)] records the OEIS status of the other rows.

### Height 2

A castle of width `w` and height 2 stands on a nonzero binary string of length `w`, whose runs of 1s are its blocks in row 2. The strings of length `w` with `r` runs of 1s number `C(w+1, 2r)`, one for each choice of the `2r` run ends among the `w + 1` gaps between and around the columns. The castle has an even number of blocks when `r` is odd, so[^8]

```
A^e(w, 2)  =  Σ_{j≥0} C(w+1, 4j+2)  =  A038505(w+1)
A^o(w, 2)  =  Σ_{j≥1} C(w+1, 4j)    =  A038503(w+1) − 1
```

`A038503(n)` and `A038505(n)` are the sums of `C(n, j)` over `j ≡ 0` and over `j ≡ 2 (mod 4)`, two of the four sums of every fourth binomial coefficient ([[hyperbolic-sequence-family](pages/hyperbolic-sequence-family.md)]). Both OEIS entries carry the castle reading ([[oeis-height2-hyperbolic-castles](pages/oeis-height2-hyperbolic-castles.md)]). At width 3, `A^e(3, 2) = C(4, 2) = 6` and `A^o(3, 2) = C(4, 4) = 1`.

## Appearances in Sources

- [[project-euler-502](pages/project-euler-502.md)] - the problem statement: the count `F(w, h)`, the four checkpoint values, and the target sum.
- [[project-euler-502-problem-setup](pages/project-euler-502-problem-setup.md)] - the size of `F(13, 10)` as the reason to count with generating functions rather than by enumeration.
- [[project-euler-502-representations](pages/project-euler-502-representations.md)] - the closed form for `F(w, h)` from the tower grammar, checked against three checkpoints.
- [[project-euler-502-solution](pages/project-euler-502-solution.md)] - the notation `A(w, h)`, `F(w, h)`, and the evaluation paths for the three terms of the target.
- [[project-euler-502-brute-force](pages/project-euler-502-brute-force.md)] - the module that computes `F`, `F_odd` and `F_any = A`, and checks `F + F_odd = F_any` by enumeration.
- [[oeis-mining-pe502](pages/oeis-mining-pe502.md)] - the OEIS rows `A(·, h)` and the height-2 sequences `A038505` and `A038503`.

## Related Concepts

- [[castle-polyomino](pages/castle-polyomino.md)] - the castle definition and the block count.
- [[castle-counting-formula](pages/castle-counting-formula.md)] - the closed form of `A^e(w, h)`.
- [[castle-notation](pages/castle-notation.md)] - the symbols `A`, `A^e`, `A^o`, `S`, `T` and `P`.
- [[castle-sign](pages/castle-sign.md)] - the sign `(−1)^{blocks}` that separates `A^e` from `A^o`.
- [[castle-count-algorithms](pages/castle-count-algorithms.md)] - the computation of the three terms of the target.
- [[block-count-constraints](pages/block-count-constraints.md)] - castles selected by block count in residue classes, sparse sets and numerical semigroups, of which the even-block condition is the residue class 0 modulo 2.
- [[weakly-unimodal-composition](pages/weakly-unimodal-composition.md)] - the convex castles counted by area (A001523).

## Footnotes

[^1]: [[project-euler-502-observations](pages/project-euler-502-observations.md)] §"The \"even number of blocks\" clause is almost the entire difficulty" L17 - "Without it, the answer is just h^w - (h-1)^w: all castles of height at most h minus those of height at most h-1."
[^2]: [[project-euler-502](pages/project-euler-502.md)] §"Project 502: Castle Polyominoes" L20-26 - "The castle is made from an even number of blocks", "Let F(w,h) represent the number of valid castles, given grid parameters w and h."
[^3]: [[project-euler-502-solution](pages/project-euler-502-solution.md)] §"Notation" L5-6 - "A(w, h) - number of castles with bottom block of length w and height exactly h. F(w, h) - A(w, h) restricted to even total block count."; [[project-euler-502-brute-force](pages/project-euler-502-brute-force.md)] §"What it computes" L10-11 - "F_odd(w, h) - odd-block-count castles, exact. Complement of F. F_any(w, h) - height exactly h, any parity: h^w - (h-1)^w".
[^4]: [[project-euler-502](pages/project-euler-502.md)] §"Project 502: Castle Polyominoes" L28 - "F(4,2) = 10, F(13,10) = 3729050610636, F(10,13) = 37959702514, and F(100,100) mod 1,000,000,007 = 841913936". All four recomputed from the closed form on [[castle-counting-formula](pages/castle-counting-formula.md)] (Python 3.11, 2026-10-16).
[^5]: [[project-euler-502](pages/project-euler-502.md)] §"Project 502: Castle Polyominoes" L30 - "Find (F(10^12,100) + F(10000,10000) + F(100,10^12)) mod 1,000,000,007."
[^6]: [[project-euler-502-solution](pages/project-euler-502-solution.md)] §"The rational-function path (h ≤ 15000)" [synthesis] L149-153, §"The k-direction Berlekamp-Massey path (h > 15000)" L155-163 - `F(10^12, 100)` and `F(10000, 10000)` take the rational-function path, with Kitamasa and direct extraction, and `F(100, 10^12)` the Berlekamp-Massey path in `k`.
[^7]: [[oeis-mining-pe502](pages/oeis-mining-pe502.md)] `mine-notes.md` §"Vein 2" L42-46 - "h=2 -> A000225 (2^w - 1, Mersenne) h=3 -> A001047 (3^w - 2^w) h=4 -> A005061 (4^w - 3^w) h=5 -> A005060 (5^w - 4^w) h=6 -> A005062 (6^w - 5^w)"; names checked against oeis.org on 2026-10-16.
[^8]: [[oeis-mining-pe502](pages/oeis-mining-pe502.md)] `mine-notes.md` §"Vein 3" L55-60 - "F(w,2) = A038505(w+1) = sum_k C(w+1, 2+4k) (even blocks) odd(w,2) = A038503(w+1) - 1 = sum_{k>=1} C(w+1, 4k) (odd blocks)", "A038505 = \"sum of every 4th entry of row n, starting at binomial(n,2)\"; A038503 = \"… starting at n choose 0\""; both identities checked by enumeration for `w ≤ 10` (Python 3.11, 2026-10-16).
