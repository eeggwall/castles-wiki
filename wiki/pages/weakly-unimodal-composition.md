---
title: Weakly unimodal composition
category: Concepts
summary: A weakly unimodal composition of n weakly increases and then weakly decreases; these are counted by A001523, the "stacks". A castle of area n is a composition of n, and the convex castles of area n are exactly the weakly unimodal compositions, so they number A001523(n). The vee castles are A332578 and the non-convex castles A115981; the smallest non-convex castle is the skyline (2, 1, 2), of area 5.
tags: [concept, composition, unimodal, oeis, castle, area]
sources: [oeis-encyclopedia]
created: 2026-09-13
updated: 2026-10-25
---

# Weakly unimodal composition

## Definition

A **composition** of `n` is a sequence of positive integers with sum `n`. It is **weakly unimodal** when it weakly increases up to a largest part and then weakly decreases. The weakly unimodal compositions of `n` are counted by `A001523`, whose name is "Number of stacks, or planar partitions of n; also number of weakly unimodal compositions of n":[^1]

```
A001523(n)  =  1, 1, 2, 4, 8, 15, 27, 47, 79, 130, 209, 330, …        (n = 0, 1, 2, …)
```

*Example.* All eight compositions of 4 are weakly unimodal. Of the sixteen compositions of 5, only `(2, 1, 2)` is not, so `A001523(5) = 15`.

## Castles by area

A castle of area `n`, the number of its cells, has a skyline `(c_1, …, c_w)` of positive integers with sum `n`, and every composition of `n` is the skyline of a castle, of width its number of parts and height its largest part. So the castles of area `n` are the compositions of `n`, and there are `2^{n−1}` of them ([[castle-by-area](pages/castle-by-area.md)]). A [[convex-castle](pages/convex-castle.md)] is a castle with a weakly unimodal skyline, so the convex castles of area `n` are the weakly unimodal compositions of `n`, and they number `A001523(n)` for `n ≥ 1`.[^2] The skyline `(2, 1, 2)` is the smallest non-convex castle.

The same reading gives two more rows ([[castle-by-area](pages/castle-by-area.md)]):[^3]

- the **vee castles**, whose skylines weakly decrease and then weakly increase, are the compositions whose negation is unimodal, `A332578`: `1, 2, 4, 7, 13, 21, 36, …` from `n = 1`;
- the **non-convex castles** are `A115981 = 2^{n−1} − A001523`, "the number of compositions of n which cannot be viewed as stacks": `0, 0, 0, 0, 1, 5, 17, 49, …` from `n = 1`.

**By block parity.** A convex castle of height `h` has exactly `h` blocks ([[convex-castle](pages/convex-castle.md)]), so its block count is even exactly when its largest part is even. Split this way, `A001523(n) = cev(n) + cod(n)`, the convex castles of area `n` with an even and with an odd number of blocks:[^2][^4]

```
cev(n)  =  0, 1, 2, 5, 8, 15, 24, 41, 64, 105, 162, 255, …
cod(n)  =  1, 1, 2, 3, 7, 12, 23, 38, 66, 104, 168, 257, …        (n = 1, 2, 3, …)
```

At `n = 4`, `cev(4) = 5` counts the castles `(2, 2)`, `(1, 2, 1)`, `(2, 1, 1)`, `(1, 1, 2)` and `(4)`, and `cod(4) = 3` counts `(1, 1, 1, 1)`, `(3, 1)` and `(1, 3)`.

## Related Concepts

- [[oeis-mining-pe502](pages/oeis-mining-pe502.md)] - the convex castles by area against `A001523`, and the parity split `cev`, `cod`.
- [[castle-by-area](pages/castle-by-area.md)] - the castles counted by area, with the convex, vee and non-convex rows and their parity splits for `n ≤ 12`.
- [[convex-castle](pages/convex-castle.md)] - the convex castles by width and height, `C(2h + w − 3, w − 1)`, each with `h` blocks.
- [[stack-polyomino-gf](pages/stack-polyomino-gf.md)] - the stack polyominoes, which are the convex castles drawn as polyominoes, and their generating function by area.
- [[oeis-cross-referencing](pages/oeis-cross-referencing.md)] - the two checks an OEIS match must pass: the offset, and more than a short prefix.

## Footnotes

[^1]: https://oeis.org/A001523 (read 2026-10-16) - "Number of stacks, or planar partitions of n; also number of weakly unimodal compositions of n", data "1, 1, 2, 4, 8, 15, 27, 47, 79, 130, 209, 330, 512, 784, 1183, 1765, 2604, 3804, 5504, …".
[^2]: Verified by execution (Python 3.11, 2026-10-25): for `n ≤ 20`, the castles of area `n` with a weakly unimodal skyline number `1, 2, 4, 8, 15, 27, 47, 79, 130, 209, 330, 512, 784, 1183, 1765, 2604, 3804, 5504, 7898, 11240`, the terms `A001523(1), …, A001523(20)` of https://oeis.org/A001523 (read 2026-10-25), and each has as many blocks as its largest part.
[^3]: https://oeis.org/A332578 and https://oeis.org/A115981 (read 2026-10-16) - "Number of compositions of n whose negation is unimodal" and "The number of compositions of n which cannot be viewed as stacks".
[^4]: Verified by execution (Python 3.11, 2026-10-16): for `n ≤ 18`, the weakly unimodal, V-shaped and non-unimodal compositions of `n` against `A001523`, `A332578` and `A115981`; for `n ≤ 20` (rechecked 2026-10-25), the convex castles of area `n` split by block parity, which gives the `cev(n)` and `cod(n)` shown.
