---
title: "Height-2 castles = A038505 / A038503 (hyperbolic family)"
category: Analyses
summary: The castles of width w and height 2 with an even and with an odd number of blocks number A^e(w, 2) = A038505(w+1) and A^o(w, 2) = A038503(w+1) − 1, two of the four sums of every fourth binomial coefficient, and together 2^w − 1 = A000225(w), proved by counting the runs of the height-2 columns. The OEIS entries A038505, A038503 and A146559 state these castle readings, and A038503 − A038505 = A146559, the real part of (1 + i)^n, ties in the signed tower count P(1, ·).
tags: [oeis, castle, height-2, hyperbolic, binomial, cross-reference, analysis]
sources: [oeis-encyclopedia]
created: 2026-09-13
updated: 2026-10-25
---

# Height-2 castles = A038505 / A038503 (hyperbolic family)

The castles of height 2, split by the parity of their block count, are counted by two members of the [[hyperbolic-sequence-family](pages/hyperbolic-sequence-family.md)]. `A^e(w, 2)` and `A^o(w, 2)` are the numbers of castles of width `w` and height 2 with an even and with an odd number of blocks ([[castle-notation](pages/castle-notation.md)]).

## The identity

A castle of width `w` and height 2 is given by the set of its columns of height 2, a binary string of length `w` with at least one 1. The bottom row is one block, and if the 1s form `r` runs, the castle has `1 + r` blocks. The binary strings of length `w` with `r` runs of 1s number `C(w+1, 2r)`, one for each choice of the `2r` run ends among the `w + 1` gaps between and around the columns ([[signed-tower-count](pages/signed-tower-count.md)], section *The case k = 1*). The block count is even exactly when `r` is odd, that is when `2r ≡ 2 (mod 4)`, so[^1]

```
A^e(w, 2)  =  Σ_{k≥0} C(w+1, 4k+2)  =  A038505(w+1)
A^o(w, 2)  =  Σ_{k≥1} C(w+1, 4k)    =  A038503(w+1) − 1
A(w, 2)    =  2^w − 1               =  A000225(w)
```

`A038505(n)` and `A038503(n)` are the sums of `C(n, j)` over `j ≡ 2` and over `j ≡ 0 (mod 4)`, both with offset 0.[^2] So `A038505(n) = A^e(n−1, 2)` for `n ≥ 2`, with `a(0) = a(1) = 0`, and `A038503(n) = A^o(n−1, 2) + 1` for `n ≥ 2`, with `a(0) = a(1) = 1`. The added 1 is the term `C(n, 0)`, the string with no 1s, which gives the flat row, a castle of height 1.

*Example: `w = 4`.* `A^e(4, 2) = C(5, 2) = 10 = A038505(5)`, the ten castles of the example on [[castle-counting-formula](pages/castle-counting-formula.md)], and `A^o(4, 2) = C(5, 4) = 5 = A038503(5) − 1`; together they are the `2^4 − 1 = 15` castles of width 4 and height 2.

Two relations follow. `A038503(n) + A038505(n) = 2^{n−1}`, the sum of `C(n, j)` over even `j`; at `n = w + 1` this is the split `2^w = (A^o(w, 2) + 1) + A^e(w, 2)`. And `A038503(n) − A038505(n) = A146559(n)`, the real part of `(1 + i)^n`, so `A146559(L + 1)` is the signed tower count `P(1, L)` ([[signed-tower-count](pages/signed-tower-count.md)]).[^3] Both relations hold for `n < 40`, and the three identities above, with their offsets, agree with enumeration of the castles and with the OEIS data for `w ≤ 14`.[^4]

## In the OEIS

The entries state the castle readings. `A038505` gives "a(n) is the number of castle polyominoes of width n-1 and height 2 with an even number of blocks", for `n ≥ 2`, with the argument by runs, and `A038503` gives "a(n)-1 is the number of castle polyominoes of width n-1 and height 2 with an odd number of blocks", for `n ≥ 2`. Each records the total, `A038505(n) = A000225(n−1) − A038503(n) + 1` and `A038503(n) = A000225(n−1) − A038505(n) + 1` for `n ≥ 1`, and `A038503` adds `A038503(n) = A038505(n) + A146559(n)`. `A146559` states that among the castles of width `n − 1` reaching height 2, `a(n) − 1` is the number with an odd number of blocks minus the number with an even number, for `n ≥ 2`, which is `A^o(w, 2) − A^e(w, 2) = P(1, w) − 1` at `w = n − 1` ([[signed-tower-count](pages/signed-tower-count.md)]), and gives `a(n) = A038503(n) − A038505(n)`.[^5]

## Related Concepts

- [[hyperbolic-sequence-family](pages/hyperbolic-sequence-family.md)] - the four sums of every fourth binomial coefficient, `A038503`, `A038504`, `A038505`, `A000749`.
- [[castle-counting-function](pages/castle-counting-function.md)] - the counts `A^e(w, 2)` and `A^o(w, 2)` among the castle counts, with the width-3 example.
- [[signed-tower-count](pages/signed-tower-count.md)] - `P(1, L) = A146559(L + 1)`, the count of binary strings by runs, and the height-2 parity `A^o(w, 2) − A^e(w, 2) = P(1, w) − 1`.
- [[block-count-constraints](pages/block-count-constraints.md)] - castles selected by block count, of which the height-2 even-block castles are the residue class read off `Σ_r C(w+1, 2r) z^r`.
- [[oeis-cross-referencing](pages/oeis-cross-referencing.md)] - the offset check and the short-prefix rule that this identification passes.
- [[new-sequence-fw3](pages/new-sequence-fw3.md)] - the row `A^e(·, 3)`.
- [[oeis-mining-pe502](pages/oeis-mining-pe502.md)] - the other matches of castle counts against the OEIS.
- [[project-euler-502](pages/project-euler-502.md)] - the problem statement.
- [[oeis-mining-seminar](pages/oeis-mining-seminar.md)] - a seminar whose stops 1 to 4 follow this identification from the table of counts to its proof.

## Footnotes

[^1]: Verified by execution (Python 3.11, 2026-10-25): for `w ≤ 14`, the binary strings of length `w` with `r` runs of 1s number `C(w+1, 2r)` for every `r`, and the castles of width `w` and height 2 with an even and with an odd number of blocks number `Σ_k C(w+1, 4k+2)` and `Σ_{k≥1} C(w+1, 4k)`, together `2^w − 1`.
[^2]: https://oeis.org/A038505 and https://oeis.org/A038503 (read 2026-10-25) - "Sum of every 4th entry of row n in Pascal's triangle, starting at binomial(n,2)", offset 0, data "0,0,1,3,6,10,16,28,56,120,…"; "Sum of every 4th entry of row n in Pascal's triangle, starting at "n choose 0"", offset 0, data "1,1,1,1,2,6,16,36,72,136,…".
[^3]: https://oeis.org/A146559 (read 2026-10-25) - "a(n) = Re( (1+i)^n ) where i=sqrt(-1)" and "a(n) = A038503(n) - A038505(n)".
[^4]: Verified by execution (Python 3.11 with SymPy, 2026-10-25): `A038503(n) + A038505(n) = 2^{n−1}` and `A038503(n) − A038505(n) = Re((1+i)^n)` for `1 ≤ n < 40`; `A^e(w, 2) = A038505(w+1)` and `A^o(w, 2) = A038503(w+1) − 1` against the enumeration of the castles and against the OEIS data, for `w ≤ 14`.
[^5]: https://oeis.org/A038505, https://oeis.org/A038503, https://oeis.org/A146559 (read 2026-10-25) - A038505: "a(n) is the number of castle polyominoes of width n-1 and height 2 with an even number of blocks (Project Euler, Problem 502: Counting Castles), for n >= 2", "If the columns that reach height 2 form r runs, the number of blocks is 1 + r, so an even number of blocks means r is odd", "a(n) = A000225(n-1) - A038503(n) + 1 for n >= 1"; A038503: "a(n)-1 is the number of castle polyominoes of width n-1 and height 2 with an odd number of blocks (Project Euler, Problem 502: Counting Castles), for n >= 2", "a(n) = A000225(n-1) - A038505(n) + 1 for n >= 1", "a(n) = A038505(n) + A146559(n)"; A146559: "Among the castle polyominoes of width n-1 and reaching height 2, a(n) - 1 is the number with an odd number of blocks minus the number of those with an even number of blocks, for n >= 2", "a(n) = A038503(n) - A038505(n)".
