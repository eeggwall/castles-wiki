---
title: "OEIS matches of PE 502 castle counts"
category: Analyses
summary: The castle counts of Project Euler 502 that equal OEIS entries, offsets included. P(1, L) = A146559(L+1), with the imaginary part of (1+i)^n in A009545; A(·, h) = A000225, A001047, A005061, A005060, A005062 for h = 2, …, 6; A^e(w, 2) = A038505(w+1) and A^o(w, 2) = A038503(w+1) − 1, two of the four sums of every fourth binomial coefficient; the rows A^e(·, h) and A^o(·, h) with recurrences of orders 6, 9, 11 and 5, 9, 11 for h = 3, 4, 5, and the columns A^e(w, ·) with characteristic polynomial (x² − 1)^w; the convex count C(2h+w−3, w−1), A000217 and A000332 at h = 2, 3; towers by blocks, A034839 at height at most 1 and the rows A005408, A005891, A063490, A160747 of any height; and by area A000079, A001523 (convex), A332578 (vee), A115981 (non-convex).
tags: [analysis, oeis, castle, cross-reference]
sources: [oeis-encyclopedia, project-euler-502-solution]
created: 2026-09-13
updated: 2026-10-25
---

# OEIS matches of Project Euler 502 (PE 502) castle counts

> **See also:** [[oeis-index](pages/oeis-index.md)] - every A-number cited on the wiki and the pages that cite it; [[castle-sequence-catalogue](pages/castle-sequence-catalogue.md)] - the castle sequences with their terms and the entries they equal.

## Summary

Counts of the [[castle-polyomino](pages/castle-polyomino.md)] that equal entries of the On-Line Encyclopedia of Integer Sequences (OEIS), each checked against the OEIS terms with its offset ([[oeis-cross-referencing](pages/oeis-cross-referencing.md)]). `A(w, h)`, `A^e(w, h)` and `A^o(w, h)` count all castles of width `w` and height `h`, those with an even number of blocks, and those with an odd number ([[castle-counting-function](pages/castle-counting-function.md)]).

## Signed tower count

`P(1, L) = Re((1+i)^{L+1}) = A146559(L+1)`, and the imaginary parts `Im((1+i)^n)` are `A009545(n)`.[^1] The closed form and a proof by a sign-reversing involution are on [[signed-tower-count](pages/signed-tower-count.md)] (section *The case k = 1*).[^2] For each `k`, `P(k, ·)` satisfies a linear recurrence of order `k + 1` ([[castle-counting-formula](pages/castle-counting-formula.md)], the Proposition in the section *Signed tower count*).

## All castles and the parity split

`A(w, h) = h^w − (h−1)^w` is `A000225(w)` (`2^n − 1`) at `h = 2`, `A001047(w)` (`3^n − 2^n`) at `h = 3`, and `A005061(w)`, `A005060(w)`, `A005062(w)` at `h = 4, 5, 6`.[^3][^4]

At height 2 the castles of width `w` stand on the nonzero binary strings of length `w`, and the strings with `r` runs of 1s number `C(w+1, 2r)`, the row `w + 1` of `A034839`: a string with `r` runs changes value at `2r` of the `w + 1` gaps of `0 c_1 ⋯ c_w 0`. The castle has `r + 1` blocks, so it has an even number exactly when `r` is odd, and[^5][^6]

```
A^e(w, 2)  =  Σ_j C(w+1, 4j+2)  =  A038505(w+1),
A^o(w, 2)  =  Σ_{j≥1} C(w+1, 4j)  =  A038503(w+1) − 1,
```

with `A^e(w, 2) + A^o(w, 2) = 2^w − 1`. `A038503`, `A038504`, `A038505` and `A000749` are the four sums of every fourth binomial coefficient, starting at `C(n, 0)`, `C(n, 1)`, `C(n, 2)` and `C(n, 3)`, and add to `2^n` ([[hyperbolic-sequence-family](pages/hyperbolic-sequence-family.md)], [[oeis-height2-hyperbolic-castles](pages/oeis-height2-hyperbolic-castles.md)]).[^5]

For `h = 3, 4, 5` the rows satisfy linear recurrences of orders 6, 9 and 11 for `A^e(·, h)` and 5, 9 and 11 for `A^o(·, h)`; at `h = 3` the characteristic polynomials are `(x − 3)(x − 2)(x² − x + 2)(x² − 2x + 2)` and `(x − 3)(x² − x + 2)(x² − 2x + 2)`. In the height, every column `A^e(w, ·)` is annihilated by `(x² − 1)^w` ([[signed-tower-k-direction](pages/signed-tower-k-direction.md)]), and for `w = 3, 4, 5, 6` this is the characteristic polynomial of its shortest recurrence.[^7]

## Convex castles

Every castle of height `h` has at least `h` blocks, with equality exactly when its skyline is unimodal, that is when it is convex. The convex castles of width `w` and height `h` number `C(2h+w−3, w−1)` ([[convex-castle-binomial-identity](pages/convex-castle-binomial-identity.md)]): `C(w+1, 2) = A000217(w)` at `h = 2` and `C(w+3, 4) = A000332(w+3)` at `h = 3`.[^8][^9] So in the distribution of the castles of height `h` by block count, the entry at the least block count `h` is the convex count, and the convex castles all have the parity of `h`: the even-block convex castles number `C(2h+w−3, w−1)` for even `h` and 0 for odd `h` ([[convex-castle](pages/convex-castle.md)]).

## Towers by blocks

Towers of height at most 1 on a base of length `w` are binary strings, and those with `b` blocks number `C(w+1, 2b)`, the entry `T(w+1, b)` of the triangle `A034839`.[^5][^6] Over towers of any height, the number `T̂(w, b)` of towers on a base of length `w` with `b` blocks is `Σ_k N(w, k) C(b+w−k, w−1)`, with `N(w, k)` the Narayana numbers (`A001263`), proved on [[tower-heap](pages/tower-heap.md)] from the fixed point of the tower grammar ([[narayana-numbers](pages/narayana-numbers.md)], [[tower-narayana-polynomial](pages/tower-narayana-polynomial.md)]). Its rows `w = 2, 3, 4, 5` are `A005408(b)`, `A005891(b)`, `A063490(b + 1)` and `A160747(b)`.[^10][^11]

## Castles by area

A castle of area `n` is a composition of `n`, its column heights in order, so all castles of area `n` number `2^{n−1} = A000079(n−1) = A011782(n)`. The convex castles of area `n` are the weakly unimodal compositions of `n`, `A001523(n)`; the vee castles, which weakly fall and then weakly rise, are `A332578(n)`; and the non-convex castles are `A115981(n) = A011782(n) − A001523(n)` ([[castle-by-area](pages/castle-by-area.md)], [[weakly-unimodal-composition](pages/weakly-unimodal-composition.md)]).[^12][^13]

## The matches

| Count | OEIS |
|---|---|
| `P(1, L)` | `A146559(L+1)`; `A009545` is the imaginary part of `(1+i)^n` |
| `A(w, h)` at `h = 2, …, 6` | `A000225`, `A001047`, `A005061`, `A005060`, `A005062` |
| `A^e(w, 2)` | `A038505(w+1)` |
| `A^o(w, 2)` | `A038503(w+1) − 1` |
| convex castles of width `w` and height `h` | `C(2h+w−3, w−1)`; `A000217(w)` at `h = 2`, `A000332(w+3)` at `h = 3` |
| towers of height at most 1 by blocks | `A034839` |
| towers by blocks, rows `w = 2, …, 5` | `A005408`, `A005891`, `A063490` (offset 1), `A160747` |
| all castles by area | `A000079(n−1) = A011782(n) = 2^{n−1}` |
| convex castles by area | `A001523(n)` |
| vee castles by area | `A332578(n)` |
| non-convex castles by area | `A115981(n)` |

## Appearances in Sources

- [[oeis-encyclopedia](pages/oeis-encyclopedia.md)] - the entries matched on this page, with their names, offsets and terms.

## Related Concepts

- [[oeis-cross-referencing](pages/oeis-cross-referencing.md)] - matching counts against the OEIS with offsets.
- [[signed-tower-count](pages/signed-tower-count.md)] - `P(k, L)` and the row `P(1, ·)`.
- [[signed-tower-k-direction](pages/signed-tower-k-direction.md)] - the recurrences in the height, and the annihilator `(x² − 1)^w` of the columns.
- [[hyperbolic-sequence-family](pages/hyperbolic-sequence-family.md)] - the four sums of every fourth binomial coefficient, `A038503`, `A038504`, `A038505` and `A000749`.
- [[oeis-height2-hyperbolic-castles](pages/oeis-height2-hyperbolic-castles.md)] - the castles of height 2 in `A038505`, `A038503` and `A146559`.
- [[convex-castle](pages/convex-castle.md)] and [[convex-castle-binomial-identity](pages/convex-castle-binomial-identity.md)] - the convex castles and the proof of `C(2h+w−3, w−1)`.
- [[tower-narayana-polynomial](pages/tower-narayana-polynomial.md)], [[tower-heap](pages/tower-heap.md)] and [[narayana-numbers](pages/narayana-numbers.md)] - the block count of towers through the Narayana numbers.
- [[castle-by-area](pages/castle-by-area.md)] and [[weakly-unimodal-composition](pages/weakly-unimodal-composition.md)] - castles counted by area.
- [[castle-counting-function](pages/castle-counting-function.md)] and [[castle-counting-formula](pages/castle-counting-formula.md)] - the counts `A`, `A^e`, `A^o` and the closed form.
- [[new-sequence-fw3](pages/new-sequence-fw3.md)] - the row `A^e(·, 3)`: `0, 0, 3, 21, 89, 307, 977, 3031, …`.

## Footnotes

[^1]: https://oeis.org/A146559 and https://oeis.org/A009545 (read 2026-10-25) - A146559, offset 0: "Expansion of (1-x)/(1 - 2*x + 2*x^2).", "a(n) = Re( (1+i)^n ) where i=sqrt(-1)"; A009545, offset 0: "Expansion of e.g.f. sin(x)*exp(x).", "a(n) = Im( (1+i)^n ) where i=sqrt(-1)" and "(1+i)^n = A146559(n) + a(n)*i where i = sqrt(-1)".
[^2]: Verified by execution (Python 3.11 with SymPy, 2026-10-25): `P(1, L)`, summed over all binary strings of length `L`, equals `A146559(L+1)` for `L ≤ 12`; the terms of `A146559` and `A009545` read today are the real and imaginary parts of `(1+i)^n` for `n < 30`.
[^3]: https://oeis.org/A000225, https://oeis.org/A001047, https://oeis.org/A005061, https://oeis.org/A005060, https://oeis.org/A005062 (read 2026-10-25), each with offset 0 - "a(n) = 2^n - 1.", "a(n) = 3^n - 2^n.", "a(n) = 4^n - 3^n.", "a(n) = 5^n - 4^n.", "a(n) = 6^n - 5^n."
[^4]: Verified by execution (Python 3.11, 2026-10-25): the skylines of width `w` with heights in `1..h` and maximum `h` number `h^w − (h−1)^w`, equal to the terms read today of the entry for `h`, for `w ≤ 7` at `h ≤ 4` and `w ≤ 5` at `h = 5, 6`.
[^5]: https://oeis.org/A038503, https://oeis.org/A038504, https://oeis.org/A038505, https://oeis.org/A000749, https://oeis.org/A034839 (read 2026-10-25) - A038503: "Sum of every 4th entry of row n in Pascal's triangle, starting at \"n choose 0\"."; A038504: "Sum of every 4th entry of row n in Pascal's triangle, starting at \"n choose 1\"."; A038505: "Sum of every 4th entry of row n in Pascal's triangle, starting at binomial(n,2)."; A000749: "a(n) = Sum_{k=0..n} binomial(n, 4*k+3)."; A034839: "Triangular array formed by taking every other term of each row of Pascal's triangle." and "Number of binary words of length n-1 having k runs of consecutive 1's."
[^6]: Verified by execution (Python 3.11, 2026-10-25): by enumeration of the skylines of height 2, `A^e(w, 2) = A038505(w+1) = Σ_j C(w+1, 4j+2)` and `A^o(w, 2) = A038503(w+1) − 1 = Σ_{j≥1} C(w+1, 4j)` for `w ≤ 14`; the binary strings of length `w` with `r` runs of 1s number `C(w+1, 2r)`, the entry `T(w+1, r)` of `A034839`, for `w ≤ 12`; `A038503(n) + A038504(n) + A038505(n) + A000749(n) = 2^n` for `n < 30`.
[^7]: Verified by execution (Python 3.11 with SymPy, 2026-10-25): `A^e(w, h)` from the formula of [[project-euler-502-solution](pages/project-euler-502-solution.md)] with `P` by the column-height dynamic program, checked against enumeration for `w ≤ 7`, `h ≤ 4` and `w ≤ 5`, `h = 5, 6`; Berlekamp-Massey over the rationals on `A^e(w, h)` and `A^o(w, h)` for `w = 1, …, 60` gives the orders 6, 9, 11 and 5, 9, 11 for `h = 3, 4, 5` and the two polynomials at `h = 3`, and on `A^e(w, h)` for `h = 2, …, 61` gives `(x − 1)^w (x + 1)^w` for `w = 3, 4, 5, 6`; every order is below 30, so each recurrence is the shortest one of the terms used.
[^8]: https://oeis.org/A000217 and https://oeis.org/A000332 (read 2026-10-25) - A000217, offset 0: "Triangular numbers: a(n) = binomial(n+1,2) = n*(n+1)/2 = 0 + 1 + 2 + ... + n."; A000332, offset 0: "Binomial coefficient binomial(n,4) = n*(n-1)*(n-2)*(n-3)/24."
[^9]: Verified by execution (Python 3.11, 2026-10-25): every skyline of width `w ≤ 6` and height `h ≤ 4` has at least `h` blocks, with equality exactly when it is unimodal; the castles with `h` blocks number `C(2h+w−3, w−1)` for `w ≤ 7`, `h ≤ 4` and `w ≤ 5`, `h = 5`, equal to `A000217(w)` at `h = 2` and `A000332(w+3)` at `h = 3`.
[^10]: https://oeis.org/A005408, https://oeis.org/A005891, https://oeis.org/A063490, https://oeis.org/A160747, https://oeis.org/A001263 (read 2026-10-25) - A005408, offset 0: "The odd numbers: a(n) = 2*n + 1."; A005891, offset 0: "Centered pentagonal numbers: (5n^2+5n+2)/2; crystal ball sequence for 3.3.3.4.4. planar net."; A063490, offset 1: "a(n) = (2*n - 1)*(7*n^2 - 7*n + 6)/6."; A160747, offset 0: "Expansion of (1 + 10*x + 20*x^2 + 10*x^3 + x^4)/(1-x)^5."; A001263: "Triangle of Narayana numbers T(n,k) = C(n-1,k-1)*C(n,k-1)/k with 1 <= k <= n, read by rows."
[^11]: Verified by execution (Python 3.11, 2026-10-25): the towers on a base of length `w = 2, 3, 4, 5` with `b ≤ 7` blocks, enumerated over column heights `0..b`, number `Σ_k N(w, k) C(b+w−k, w−1)`, equal to `A005408(b)`, `A005891(b)`, `A063490(b + 1)` and `A160747(b)`.
[^12]: https://oeis.org/A000079, https://oeis.org/A011782, https://oeis.org/A001523, https://oeis.org/A332578, https://oeis.org/A115981 (read 2026-10-25) - A000079, offset 0: "Powers of 2: a(n) = 2^n."; A011782: "Number of compositions (ordered partitions) of n." and "a(0) = 1, a(n) = 2^(n-1)."; A001523: "Number of stacks, or planar partitions of n; also number of weakly unimodal compositions of n."; A332578: "Number of compositions of n whose negation is unimodal."; A115981: "The number of compositions of n which cannot be viewed as stacks." and "a(n) = A011782(n) - A001523(n)."
[^13]: Verified by execution (Python 3.11, 2026-10-25): for `n ≤ 15`, the compositions of `n` number `2^{n−1} = A000079(n−1) = A011782(n)`; the weakly unimodal ones number `A001523(n)`, those whose negation is weakly unimodal `A332578(n)`, and the rest `A115981(n) = A011782(n) − A001523(n)`.
