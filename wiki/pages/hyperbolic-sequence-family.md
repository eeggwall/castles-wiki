---
title: Order-4 hyperbolic sequence family
category: Concepts
summary: The four sums of every fourth entry of row n of Pascal's triangle, A038503, A038504, A038505 and A000749, which the OEIS calls the difference analog of the hyperbolic functions of order 4. At height 2, the even-block castles of width w number A038505(w+1) and the odd-block ones A038503(w+1) − 1, and A038503 − A038505 is the signed tower count A146559 = Re((1+i)^n).
tags: [concept, oeis, binomial, hyperbolic, castle, height-2]
sources: [oeis-mining-pe502, oeis-height2-hyperbolic-castles]
created: 2026-09-13
updated: 2026-10-16
---

# Order-4 hyperbolic sequence family

## The four sequences

Summing every fourth entry of row `n` of Pascal's triangle, starting at `C(n, r)` for `r = 0, 1, 2, 3`, gives four sequences:[^1]

| `r` | sequence | `Σ_j C(n, 4j + r)` for `n = 0, 1, 2, …` |
|---|---|---|
| 0 | `A038503` | `1, 1, 1, 1, 2, 6, 16, 36, 72, 136, …` |
| 1 | `A038504` | `0, 1, 2, 3, 4, 6, 12, 28, 64, 136, …` |
| 2 | `A038505` | `0, 0, 1, 3, 6, 10, 16, 28, 56, 120, …` |
| 3 | `A000749` | `0, 0, 0, 1, 4, 10, 20, 36, 64, 120, …` |

At `n = 5`, row 5 is `1, 5, 10, 10, 5, 1`, and the four sums are `C(5, 0) + C(5, 4) = 6`, `C(5, 1) + C(5, 5) = 6`, `C(5, 2) = 10` and `C(5, 3) = 10`.

The four sum to `2^n`. Each satisfies `a(n) = 4a(n−1) − 6a(n−2) + 4a(n−3)` for `n ≥ 4`, whose characteristic polynomial `λ³ − 4λ² + 6λ − 4 = (λ − 2)(λ² − 2λ + 2)` has the roots `2` and `1 ± i`.[^1][^2] The OEIS entries call `{A038503, A038504, A038505, A000749}` the difference analog of the hyperbolic functions of order 4, as `{A146559, A009545}`, the real and imaginary parts of `(1+i)^n`, is the difference analog of `{cos x, sin x}`.[^3]

## Castles of height 2

A castle of width `w` and height 2 ([[castle-polyomino](pages/castle-polyomino.md)]) is determined by the set of its columns of height 2, a binary string of length `w` with at least one 1. If those columns form `r` runs, the castle has `1 + r` blocks. The binary strings of length `w` with `r` runs of 1s number `C(w + 1, 2r)`, one for each choice of the `2r` run ends among the `w + 1` gaps between and around the columns. The block count is even when `r` is odd, that is when `2r ≡ 2 (mod 4)`, and odd when `r ≥ 2` is even, so[^4]

```
A^e(w, 2)  =  Σ_{j≥0} C(w+1, 4j+2)  =  A038505(w + 1)
A^o(w, 2)  =  Σ_{j≥1} C(w+1, 4j)    =  A038503(w + 1) − 1
A(w, 2)    =  2^w − 1               =  A000225(w)
```

Here `A^e(w, 2)` and `A^o(w, 2)` count the even-block and odd-block castles of width `w` and height 2, and `A^e` is the count `F(w, h)` of the problem statement ([[castle-counting-function](pages/castle-counting-function.md)]). At `w = 4`, `A^e(4, 2) = C(5, 2) = 10` and `A^o(4, 2) = C(5, 4) = 5`, and `10 + 5 = 15 = 2^4 − 1`. A castle with three runs of height-2 columns first occurs at `w = 5`, the skyline `(2, 1, 2, 1, 2)`.

The difference of the two sequences is the signed tower count at tower height 1:[^5]

```
A038503(n) − A038505(n)  =  Σ_j (−1)^j C(n, 2j)  =  Re((1+i)^n)  =  A146559(n),
```

so `P(1, L) = A146559(L + 1)` ([[signed-tower-count](pages/signed-tower-count.md)]). Since the two sum to `2^{n−1}` for `n ≥ 1`, `A038503(n) + A038505(n) − 1 = A000225(n − 1)`.

## In the OEIS

`A038503` carries the comment that `a(n) − 1` counts the castles of width `n − 1` and height 2 with an odd number of blocks, for `n ≥ 2`, and the formulas `a(n) = A000225(n−1) − A038505(n) + 1` for `n ≥ 1` and `a(n) = A038505(n) + A146559(n)`. `A038505` carries the comment that `a(n)` counts the castles of width `n − 1` and height 2 with an even number of blocks, for `n ≥ 2`, and the formula `a(n) = A000225(n−1) − A038503(n) + 1` for `n ≥ 1`. `A146559` carries `a(n) = A038503(n) − A038505(n)`.[^2][^3][^5] [[oeis-height2-hyperbolic-castles](pages/oeis-height2-hyperbolic-castles.md)] quotes the comments in full.

## Appearances in Sources

- [[oeis-height2-hyperbolic-castles](pages/oeis-height2-hyperbolic-castles.md)] - the height-2 identities, their proof, and the comments and formulas added to `A038503`, `A038505` and `A146559`.
- [[oeis-mining-pe502](pages/oeis-mining-pe502.md)] - the height-2 rows `A038505` and `A038503` and their place in the family of four.

## Related Concepts

- [[castle-counting-function](pages/castle-counting-function.md)] - the counts `A`, `A^e` and `A^o`, and their height-2 rows.
- [[signed-tower-count](pages/signed-tower-count.md)] - `P(1, L) = Re((1+i)^{L+1}) = A146559(L+1)`, the difference of `A038503` and `A038505`.
- [[block-count-constraints](pages/block-count-constraints.md)] - towers of height at most 1 counted by block count modulo 2: the even-block ones number `A038503(L+1)`, the odd-block ones `A038505(L+1)`.
- [[permutation-cycle-castle-analogy](pages/permutation-cycle-castle-analogy.md)] - the height-2 count `A^e(w, 2) = Σ_s C(w+1, 4s+2)` in the comparison of castle peaks with permutation cycles.
- [[fractional-width-and-height](pages/fractional-width-and-height.md)] - the extension of the height-2 counts to non-integer width, and the period-8 oscillation of the signed count `S(w, 2)` in `w`.
- [[fractional-block-count](pages/fractional-block-count.md)] - the sum of `e^{2πiα·blocks}` over castles, which at `α = 1/4` weights the blocks by powers of `i`.
- [[oeis-cross-referencing](pages/oeis-cross-referencing.md)] - the method that matched the castle counts to OEIS entries with their offsets.

## Footnotes

[^1]: [[oeis-height2-hyperbolic-castles](pages/oeis-height2-hyperbolic-castles.md)] `oeis-xref-draft.md` §"0. Verified identities (offsets nailed)" L26-29 - "A038505(n) = Sum_k binomial(n, 2+4k) = Sum_k binomial(n, 4k+2). Data: 0, 0, 1, 3, 6, 10, 16, 28, ...", "A038503(n) = Sum_k binomial(n, 4k). Data: 1, 1, 1, 1, 2, 6, 16, 36, ..."; https://oeis.org/A038504 and https://oeis.org/A000749 (read 2026-10-16) for the other two. All four rows, the sum `2^n` and the recurrence from `n = 4` checked for `n < 20` (Python 3.11, 2026-10-16).
[^2]: https://oeis.org/A038503 (read 2026-10-16) - "a(n) = 4a(n-1) - 6a(n-2) + 4a(n-3)", "a(n)-1 is the number of castle polyominoes of width n-1 and height 2 with an odd number of blocks (Project Euler, Problem 502: Counting Castles), for n >= 2", "a(n) = A000225(n-1) - A038505(n) + 1 for n >= 1", "a(n) = A038505(n) + A146559(n)".
[^3]: https://oeis.org/A038505 (read 2026-10-16) - "{A038503, A038504, A038505, A000749} is the difference analog of the hyperbolic functions of order 4", "a(n) is the number of castle polyominoes of width n-1 and height 2 with an even number of blocks (Project Euler, Problem 502: Counting Castles), for n >= 2", "a(n) = A000225(n-1) - A038503(n) + 1 for n >= 1"; https://oeis.org/A146559 - "{A146559, A009545} is the difference analog of {cos(x), sin(x)}".
[^4]: [[oeis-height2-hyperbolic-castles](pages/oeis-height2-hyperbolic-castles.md)] `mine-notes.md` §"Vein 3" L55-68 - "F(w,2) = A038505(w+1) = sum_k C(w+1, 2+4k) (even blocks) odd(w,2) = A038503(w+1) - 1 = sum_{k>=1} C(w+1, 4k) (odd blocks) total = A000225(w) = 2^w - 1", "height-2 castles have blocks = 1 + (#runs of top cells), and the number of width-w binary strings with exactly r runs of 1's is C(w+1, 2r). Even blocks <=> r odd <=> j = 2r ≡ 2 (mod 4)".
[^5]: [[oeis-height2-hyperbolic-castles](pages/oeis-height2-hyperbolic-castles.md)] `crosslink-avenues.md` §"3. A146559" L25-29 - "a(n) = P(1, n−1) = the signed tower count", "a(n) = A038503(n) − A038505(n) (verified: Re((1+i)^n) = Σ_{j≡0} − Σ_{j≡2} binomial)"; https://oeis.org/A146559 - "a(n) = A038503(n) - A038505(n)".
