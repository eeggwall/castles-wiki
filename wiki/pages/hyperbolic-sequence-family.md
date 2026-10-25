---
title: Order-4 hyperbolic sequence family
category: Concepts
summary: The four sums of every fourth entry of row n of Pascal's triangle, A038503, A038504, A038505 and A000749, which the OEIS calls the difference analog of the hyperbolic functions of order 4. At height 2, the even-block castles of width w number A038505(w+1) and the odd-block ones A038503(w+1) − 1, and A038503 − A038505 is the signed tower count A146559 = Re((1+i)^n).
tags: [concept, oeis, binomial, hyperbolic, castle, height-2]
sources: [oeis-encyclopedia]
created: 2026-09-13
updated: 2026-10-25
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

A castle of width `w` and height 2 ([[castle-polyomino](pages/castle-polyomino.md)]) is determined by the set of its columns of height 2, a binary string of length `w` with at least one 1. If those columns form `r` runs, the castle has `1 + r` blocks. The binary strings of length `w` with `r` runs of 1s number `C(w + 1, 2r)`, one for each choice of the `2r` run ends among the `w + 1` gaps between and around the columns ([[signed-tower-count](pages/signed-tower-count.md)], section *The case k = 1*). The block count is even when `r` is odd, that is when `2r ≡ 2 (mod 4)`, and odd when `r ≥ 2` is even, so[^4]

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

## Related Concepts

- [[oeis-height2-hyperbolic-castles](pages/oeis-height2-hyperbolic-castles.md)] - the height-2 identities, their proof, and the castle comments and formulas of `A038503`, `A038505` and `A146559`, quoted in full.
- [[oeis-mining-pe502](pages/oeis-mining-pe502.md)] - the height-2 rows `A038505` and `A038503` among the other matches of castle counts against the OEIS.
- [[castle-counting-function](pages/castle-counting-function.md)] - the counts `A`, `A^e` and `A^o`, and their height-2 rows.
- [[signed-tower-count](pages/signed-tower-count.md)] - `P(1, L) = Re((1+i)^{L+1}) = A146559(L+1)`, the difference of `A038503` and `A038505`.
- [[block-count-constraints](pages/block-count-constraints.md)] - towers of height at most 1 counted by block count modulo 2: the even-block ones number `A038503(L+1)`, the odd-block ones `A038505(L+1)`.
- [[permutation-cycle-castle-analogy](pages/permutation-cycle-castle-analogy.md)] - the height-2 count `A^e(w, 2) = Σ_s C(w+1, 4s+2)` in the comparison of castle peaks with permutation cycles.
- [[fractional-width-and-height](pages/fractional-width-and-height.md)] - the extension of the height-2 counts to non-integer width, and the period-8 oscillation of the signed count `S(w, 2)` in `w`.
- [[fractional-block-count](pages/fractional-block-count.md)] - the sum of `e^{2πiα·blocks}` over castles, which at `α = 1/4` weights the blocks by powers of `i`.
- [[oeis-cross-referencing](pages/oeis-cross-referencing.md)] - the method that matched the castle counts to OEIS entries with their offsets.

## Footnotes

[^1]: https://oeis.org/A038503, https://oeis.org/A038504, https://oeis.org/A038505, https://oeis.org/A000749 (read 2026-10-25) - "Sum of every 4th entry of row n in Pascal's triangle, starting at \"n choose 0\"", "... starting at \"n choose 1\"", "... starting at binomial(n,2)", and for A000749 "a(n) = Sum_{k=0..n} binomial(n, 4*k+3)"; all four with offset 0. Verified by execution (Python 3.11 with SymPy, 2026-10-25): the four rows of the table against the OEIS data for `n < 17`, their sum `2^n`, and the recurrence from `n = 4`, for `n < 40`.
[^2]: https://oeis.org/A038503 (read 2026-10-16) - "a(n) = 4a(n-1) - 6a(n-2) + 4a(n-3)", "a(n)-1 is the number of castle polyominoes of width n-1 and height 2 with an odd number of blocks (Project Euler, Problem 502: Counting Castles), for n >= 2", "a(n) = A000225(n-1) - A038505(n) + 1 for n >= 1", "a(n) = A038505(n) + A146559(n)".
[^3]: https://oeis.org/A038505 (read 2026-10-16) - "{A038503, A038504, A038505, A000749} is the difference analog of the hyperbolic functions of order 4", "a(n) is the number of castle polyominoes of width n-1 and height 2 with an even number of blocks (Project Euler, Problem 502: Counting Castles), for n >= 2", "a(n) = A000225(n-1) - A038503(n) + 1 for n >= 1"; https://oeis.org/A146559 - "{A146559, A009545} is the difference analog of {cos(x), sin(x)}".
[^4]: Verified by execution (Python 3.11, 2026-10-25): for `w ≤ 14`, the binary strings of length `w` with `r` runs of 1s number `C(w + 1, 2r)`, the castles of width `w` and height 2 with an even and with an odd number of blocks number `Σ_j C(w+1, 4j+2)` and `Σ_{j≥1} C(w+1, 4j)`, together `2^w − 1`, and these equal `A038505(w + 1)` and `A038503(w + 1) − 1` in the OEIS data.
[^5]: https://oeis.org/A146559 (read 2026-10-25) - "a(n) = Re( (1+i)^n ) where i=sqrt(-1)", "a(n) = A038503(n) - A038505(n)". Verified by execution (Python 3.11 with SymPy, 2026-10-25): `A038503(n) − A038505(n) = Re((1+i)^n)` for `n < 40`.
