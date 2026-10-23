---
title: "Even-block castles of height 3, A^e(w, 3)"
category: Sources
summary: The sequence A^e(w, 3) of castles of width w and height 3 with an even number of blocks, 0, 0, 3, 21, 89, 307, 977, … from w = 1, with 50 terms, the closed form (3^w − 2^w − P(2, w) + P(1, w))/2, a linear recurrence of order 6 with characteristic polynomial (x−3)(x−2)(x²−x+2)(x²−2x+2), and its generating function. The order is 6, not 7, because P(2, ·) and 2^w share the root 2; the odd-block row A^o(w, 3) has order 5.
tags: [oeis, castle, new-sequence, c-finite, height-3, source]
sources: [new-sequence-fw3]
created: 2026-09-13
updated: 2026-10-23
---

# Even-block castles of height 3, A^e(w, 3)

**Source:** `raw/oeis-pe502/new-sequence-F3.md`
**Date ingested:** 2026-09-13
**Type:** notes on one sequence: terms, definition, formulas and programs

## Summary

The source works out the row `h = 3` of the even-block castle count, `a(w) = A^e(w, 3)`, the number of [[castle-polyomino](pages/castle-polyomino.md)] of width `w` and height 3 with an even number of blocks. The source writes it `F(n, 3)`, with `n` the width. Its terms from `w = 1` are[^1]

```
0, 0, 3, 21, 89, 307, 977, 3031, 9321, 28479, 86505, 261615, 788969, …
```

and the source lists 50 of them. The first two are 0 because a castle of width 1 or 2 and height 3 has exactly 3 blocks: with two columns the block count is `max(c_1, c_2)`.[^2] At width 3 the even-block castles are the skylines `(2, 1, 3)`, `(3, 1, 2)` and `(3, 2, 3)`, each with 4 blocks.

The source counts the blocks of a castle of height 3 by runs: with `r_2` the number of maximal runs of columns of height at least 2, and `r_3` the number of runs of columns of height 3, a castle has `1 + r_2 + r_3` blocks, so it has an even number exactly when `r_2 + r_3` is odd.[^3]

## Formulas

The [[castle-counting-formula](pages/castle-counting-formula.md)] at `h = 3` gives the closed form[^4]

```
A^e(w, 3)  =  ( 3^w − 2^w − P(2, w) + P(1, w) ) / 2,
```

with the signed tower counts `P(1, w) = Re((1+i)^{w+1}) = A146559(w+1)` and `P(2, w)`, which satisfies `P(2, w) = 3P(2, w−1) − 4P(2, w−2) + 4P(2, w−3)` ([[signed-tower-count](pages/signed-tower-count.md)]). The odd-block castles of height 3 number `A^o(w, 3) = 3^w − 2^w − A^e(w, 3)`, where `3^w − 2^w = A001047(w)` counts all castles of width `w` and height 3.

The sequence satisfies, for `w ≥ 7`,[^5]

```
a(w)  =  8a(w−1) − 27a(w−2) + 54a(w−3) − 70a(w−4) + 56a(w−5) − 24a(w−6),
```

with characteristic polynomial `(x − 3)(x − 2)(x² − x + 2)(x² − 2x + 2)`, and its generating function is

```
Σ_w a(w) x^w  =  (3x³ − 3x⁴ + 2x⁵) / (1 − 8x + 27x² − 54x³ + 70x⁴ − 56x⁵ + 24x⁶).
```

**The order.** The four terms of the closed form have characteristic polynomials `x − 3`, `x − 2`, `char_2 = (x − 2)(x² − x + 2)` and `char_1 = x² − 2x + 2`, of total degree 7. `char_2` shares the root 2 with `2^w`, so their least common multiple has degree 6, and Berlekamp-Massey on the terms confirms order 6.[^6] The odd-block row `A^o(w, 3)` = `1, 5, 16, 44, 122, 358, 1082, 3274, …` has order 5, with characteristic polynomial `(x − 3)(x² − x + 2)(x² − 2x + 2)`: in `A^o` the two components at the root 2 cancel. For `4 ≤ h ≤ 8` both `A^e(·, h)` and `A^o(·, h)` have order `2h + 1`, the total degree of `x − h`, `x − (h−1)`, `char_{h−1}` and `char_{h−2}`; at `h = 2` the orders are 3 and 4.[^7]

**Columns.** At fixed width `w` the column `A^e(w, ·)` is annihilated by `(x² − 1)^w`, so it is a polynomial in `h` plus `(−1)^h` times a polynomial in `h` ([[signed-tower-k-direction](pages/signed-tower-k-direction.md)]); the source notes the orders 6, 8 and 10 of the columns `w = 3, 4, 5`.[^8]

## Where the factors appear on the wiki

- `char_1 = x² − 2x + 2`, with roots `1 ± i`, is the characteristic polynomial of `P(1, ·)`, and `char_2 = (x − 2)(x² − x + 2)` that of `P(2, ·)` ([[signed-tower-count](pages/signed-tower-count.md)]). [[tower-parity-sectors](pages/tower-parity-sectors.md)] derives the factorization of `char_k` for even `k` from the split of `P` by the parity of the last column.
- **Modulo `p`.** `A^e(w, 3) mod p` is periodic in `w`. The discriminant of `x² − x + 2` is `−7`, so modulo 7 it is `(x − 4)²`, a double root, and the period modulo 7 is `168 = 7 · 24`, against 24 modulo 5 and 40 modulo 11 ([[mod-p-observatory](pages/mod-p-observatory.md)]).[^7]
- **Evaluation.** [[kitamasa](pages/kitamasa.md)] uses `P(2, ·)`, with recurrence coefficients `3, −4, 4`, as its order-3 example, and [[generating-function-gallery](pages/generating-function-gallery.md)] gives the rational function `num_2/den_2` of `P(2, ·)`. The castles can be enumerated with `all_castles(w, 3)` on [[castle-snippets](pages/castle-snippets.md)] or the reference module on [[project-euler-502-brute-force](pages/project-euler-502-brute-force.md)].
- **Entropy.** At `w = 12`, `log₂ A^e(12, 3) = log₂ 261615 = 17.997`, against `log₂ A(12, 3) − 1 = 18.008`, Equation (1) of [[castle-entropy](pages/castle-entropy.md)] without its correction term.[^7]

## Key Takeaways

- `A^e(w, 3)`: `0, 0, 3, 21, 89, 307, 977, 3031, …` from `w = 1`; a castle of height 3 has `1 + r_2 + r_3` blocks.[^1][^3]
- Closed form `(3^w − 2^w − P(2, w) + P(1, w))/2`, recurrence of order 6 with characteristic polynomial `(x − 3)(x − 2)(x² − x + 2)(x² − 2x + 2)`, and a rational generating function.[^4][^5]
- `A^o(w, 3)` has order 5; for `4 ≤ h ≤ 8` both rows have order `2h + 1` (computed).[^7]

## Entities & Concepts

- [[castle-counting-function](pages/castle-counting-function.md)] - the counts `A`, `A^e` and `A^o`, of which this is the row `h = 3`.
- [[castle-counting-formula](pages/castle-counting-formula.md)] - the closed form of `A^e(w, h)`.
- [[signed-tower-count](pages/signed-tower-count.md)] - `P(1, ·)` and `P(2, ·)` and their characteristic polynomials.
- [[hyperbolic-sequence-family](pages/hyperbolic-sequence-family.md)] - the row `h = 2`, `A^e(w, 2) = A038505(w+1)`.
- [[aocp-generating-functions](pages/aocp-generating-functions.md)] - geometric generating functions and the difference of powers `3^w − 2^w = A001047(w)`.
- [[oeis-height2-hyperbolic-castles](pages/oeis-height2-hyperbolic-castles.md)] - the height-2 rows `A^e(w, 2) = A038505(w+1)` and `A^o(w, 2) = A038503(w+1) − 1`.
- [[castle-sequence-catalogue](pages/castle-sequence-catalogue.md)] - the rows `A^e(·, h)` and `A^o(·, h)`.
- [[castle-cryptography-ring](pages/castle-cryptography-ring.md)] - the ring `F_p[x]/(char_2)`, in which `x` has order 3400 for `p = 101`.
- [[tower-parity-sectors](pages/tower-parity-sectors.md)] - the factorization of `char_k` for even `k`.
- [[mod-p-observatory](pages/mod-p-observatory.md)] - castle counts modulo primes, and the repeated root of `char_2` modulo 7.
- [[kitamasa](pages/kitamasa.md)] / [[generating-function-gallery](pages/generating-function-gallery.md)] - the evaluation of `P(2, ·)`.
- [[castle-snippets](pages/castle-snippets.md)] / [[project-euler-502-brute-force](pages/project-euler-502-brute-force.md)] - enumeration of castles.
- [[castle-entropy](pages/castle-entropy.md)] - `log₂ A^e` against `log₂ A − 1`.
- [[oeis-mining-seminar](pages/oeis-mining-seminar.md)] - a seminar that runs this row through Berlekamp-Massey.

## Footnotes

[^1]: [[new-sequence-fw3](pages/new-sequence-fw3.md)] `new-sequence-F3.md` §"The sequence" L15-29 - "The sequence (index n = width w, so a(n) = F(n,3)): 0, 0, 3, 21, 89, 307, 977, 3031, 9321, 28479, 86505, 261615, 788969, …". All 50 listed terms agree with the closed form, and the first 9 with enumeration of all skylines (Python 3.11, 2026-10-16).
[^2]: [[new-sequence-fw3](pages/new-sequence-fw3.md)] `new-sequence-F3.md` §"Data & offset" L38-40 - "a width-1 or width-2 castle of height 3 always has max(c) = 3 blocks (odd), so none has an even block count."
[^3]: [[new-sequence-fw3](pages/new-sequence-fw3.md)] `new-sequence-F3.md` §"Comment (definition, plain English)" L54-57 - "the number of blocks is c(1) + Sum_{i=2..n} max(0, c(i)-c(i-1)). Equivalently, with r2 = number of runs of columns of height >= 2 and r3 = number of runs of columns of height 3, the number of blocks is 1 + r2 + r3, so it is even iff r2 + r3 is odd."
[^4]: [[new-sequence-fw3](pages/new-sequence-fw3.md)] `new-sequence-F3.md` §"Formula" L61-68 - "a(n) = (3^n - 2^n - P(2,n) + P(1,n)) / 2, where P(1,n) = Re((1+i)^(n+1)) = A146559(n+1)", "P(2,n) = 3*P(2,n-1) - 4*P(2,n-2) + 4*P(2,n-3)".
[^5]: [[new-sequence-fw3](pages/new-sequence-fw3.md)] `new-sequence-F3.md` §"Formula" L70-79 - "Linear recurrence (holds for n >= 7): a(n) = 8*a(n-1) - 27*a(n-2) + 54*a(n-3) - 70*a(n-4) + 56*a(n-5) - 24*a(n-6)", "Characteristic polynomial (x-3)(x-2)(x^2-x+2)(x^2-2x+2)", "A(x) = (3*x^3 - 3*x^4 + 2*x^5) / (1 - 8*x + 27*x^2 - 54*x^3 + 70*x^4 - 56*x^5 + 24*x^6)".
[^6]: [[new-sequence-fw3](pages/new-sequence-fw3.md)] `mine-notes.md` §"Vein 3" L70-75 - "F(w,3): order 6, (x-3)(x-2)(x^2-x+2)(x^2-2x+2)", "F(w,4): order 9", "F(w,5): order 11", "F(w,3) loses one order because P(2,·) has x-2 as a factor, shared with 2^w."
[^7]: Verified by execution (Python 3.11 with SymPy, 2026-10-16): Berlekamp-Massey on 60 terms of `A^e(·, h)` and `A^o(·, h)` for `2 ≤ h ≤ 8` (orders 3, 6, 9, 11, 13, 15, 17 and 4, 5, 9, 11, 13, 15, 17); the recurrence and generating function of the section *Formulas* from the terms; the periods of `A^e(·, 3)` modulo 5, 7, 11 and 13 (24, 168, 40, 168) on 3000 terms; `log₂ 261615` and `log₂(3^12 − 2^12) − 1`; the order 3400 of `x` in `F_101[x]/(char_2)`.
[^8]: [[new-sequence-fw3](pages/new-sequence-fw3.md)] `mine-notes.md` §"Vein 3" L77-79 - "Columns (fixed w, varying h) are quasi-polynomials: F(w,h) is annihilated by (x^2-1)^w, i.e. F(w,h) = P(h) + (-1)^h Q(h) with P,Q polynomials of degree < w. (Observed: F(3,h) order 6, F(4,h) order 8, F(5,h) order 10.)"
