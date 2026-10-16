---
title: Pell numbers
category: Concepts
summary: The Pell numbers P⋆_n (A000129; 0, 1, 2, 5, 12, 29, 70, …), with P⋆_n = 2P⋆_{n−1} + P⋆_{n−2}, generating function x/(1 − 2x − x²) and growth constant the silver mean δ_2 = 1 + √2. The 1-smooth strips on the heights {1, 2, 3} with first column at height 1 number P⋆_w. The Pell-Lucas numbers Q_n (A001333), half the companion Pell numbers A002203, satisfy the same recurrence from Q_0 = Q_1 = 1.
tags: [concept, pell, integer-sequence, silver-ratio, quadratic-irrational, continued-fraction, oeis]
sources: [pe502-pell-castle-strip, barry-2005-catalan-transform]
created: 2026-09-15
updated: 2026-10-16
---

# Pell numbers

## Definition

The **Pell numbers** `P⋆_n` are the sequence `A000129`,[^1]

```
P⋆_0 = 0,   P⋆_1 = 1,   P⋆_n = 2·P⋆_{n−1} + P⋆_{n−2}   for n ≥ 2,
P⋆_n  =  0, 1, 2, 5, 12, 29, 70, 169, 408, 985, 2378, 5741, 13860, 33461, …
```

The star separates them from the signed tower count `P(k, L)` ([[castle-notation](pages/castle-notation.md)]). By the recurrence and the initial values, `(1 − 2x − x²) Σ_n P⋆_n x^n = x`, so the generating function is

```
Σ_{n≥0} P⋆_n x^n  =  x / (1 − 2x − x²).
```

The characteristic polynomial `λ² − 2λ − 1` has roots `1 ± √2`, so[^2]

```
P⋆_n  =  ( (1 + √2)^n − (1 − √2)^n ) / (2√2),
```

and `P⋆_{n+1}/P⋆_n → 1 + √2 = 2.41421…`. This is the **silver mean**, de Spinadel's `σ_2^1`, written `σ_Ag` in the paper and `δ_2` on the wiki ([[metallic-means](pages/metallic-means.md)], [[de-spinadel-1999-family-of-metallic-means](pages/de-spinadel-1999-family-of-metallic-means.md)]). Its continued fraction is `[2; 2, 2, …]`, and its convergents are the ratios `P⋆_{n+1}/P⋆_n`: `2, 5/2, 12/5, 29/12, 70/29, 169/70, …` ([[eigenvalue-continued-fractions](pages/eigenvalue-continued-fractions.md)]).[^2]

## The Pell-Lucas numbers

The **Pell-Lucas numbers** `Q_n` (`A001333`) satisfy the same recurrence with `Q_0 = Q_1 = 1`:[^3]

```
Q_n  =  1, 1, 3, 7, 17, 41, 99, 239, 577, 1393, …,        Q_n  =  ( (1 + √2)^n + (1 − √2)^n ) / 2.
```

They are half the companion Pell numbers `A002203` (`2, 2, 6, 14, 34, …`), and `Q_n = P⋆_n + P⋆_{n−1}` for `n ≥ 1`. The fractions `Q_n/P⋆_n`, `1, 3/2, 7/5, 17/12, 41/29, …`, are the convergents of `√2 = [1; 2, 2, …]`.[^2][^3] Both sequences are binomial sums,[^4]

```
P⋆_n  =  Σ_k C(n, 2k + 1)·2^k,          Q_n  =  Σ_k C(n, 2k)·2^k.
```

## Castle appearances

**The Pell strip.** The 1-smooth strips on the heights `{1, 2, 3}` are the skylines over `{1, 2, 3}` whose neighboring columns differ in height by at most 1; they need not reach height 3, so they are strips, not castles. Those with first column at height 1 number `P⋆_w` at width `w`, with `Σ_w P⋆_w x^{w−1} = 1/(1 − 2x − x²)`, and those with a free first column number `Q_{w+1}` ([[pell-castle-strip](pages/pell-castle-strip.md)]).[^5] At width 3 the five strips with first column at height 1 are `(1, 1, 1)`, `(1, 1, 2)`, `(1, 2, 1)`, `(1, 2, 2)` and `(1, 2, 3)`. Split by the last column, those ending at height 2 number `P⋆_{w−1}` and those ending at height 1 or 3 number `Q_{w−1}`, the binomial sums at `n = w − 1` (section 3 of [[pell-castle-strip](pages/pell-castle-strip.md)], [[binomial-transform](pages/binomial-transform.md)]).

**Pell castles.** The strips with first column at height 1 that reach height 3 are the Pell castles, `A_Pell(w) = P⋆_w − 2^{w−1}` of them ([[pell-castle](pages/pell-castle.md)]).

**The source's reading.** The source reads `1/(1 − 2x − x²)` as counting the tilings of a strip of length `n` by a width-1 atom of weight 2 and a width-2 atom of weight 1, and `a_n = 2a_{n−1} + a_{n−2}` as removing the last atom.[^6]

**Polyominoes in a `2 × h` rectangle.** The polyominoes with bounding box `2 × h` number `Q_{h+1} − 2` (`A034182`); at `h = 2` these are the square and the four L-shaped trominoes ([[inscribed-polyomino](pages/inscribed-polyomino.md)]).[^2]

**Tower words.** The tower words counted by their number of steps grow at `1 + √2`: they are silver by length ([[tower-word-continued-fraction](pages/tower-word-continued-fraction.md)]).

## Pell and Fibonacci

| mean | continued fraction | recurrence | sequence | castle appearance |
|---|---|---|---|---|
| golden `φ = (1 + √5)/2` | `[1; 1, 1, …]` | `F_n = F_{n−1} + F_{n−2}` | Fibonacci (`A000045`) | the castles of area `n` with no column of height 1 number `F_{n−1}` ([[prime-castles](pages/prime-castles.md)]) |
| silver `δ_2 = 1 + √2` | `[2; 2, 2, …]` | `P⋆_n = 2P⋆_{n−1} + P⋆_{n−2}` | Pell (`A000129`) | the 1-smooth strips on `{1, 2, 3}` with first column at height 1 ([[pell-castle-strip](pages/pell-castle-strip.md)]) |

Both are the cases `a = 1, 2` of the roots of `λ² − aλ − 1`, and each is the fundamental unit of its ring of integers: `φ` of `Z[φ]`, the integers of `Q(√5)`, and `1 + √2` of `Z[√2]`, the integers of `Q(√2)` ([[metallic-means](pages/metallic-means.md)]).

## Appearances in Sources

- [[pe502-pell-castle-strip](pages/pe502-pell-castle-strip.md)] - coefficient matching on `(1 − 2x − x²)D(x) = 1` and the two-atom reading of `D(x)`.
- [[barry-2005-catalan-transform](pages/barry-2005-catalan-transform.md)] - the binomial sums for `P⋆_n` and `Q_n`, from the aerated binomial transform of `2^k`.

## Related Concepts

- [[pell-castle-strip](pages/pell-castle-strip.md)] - the strips counted by `P⋆_w`, their transfer matrix and the splits by the boundary columns.
- [[pell-castle](pages/pell-castle.md)] - the Pell castles, `P⋆_w − 2^{w−1}` of width `w`.
- [[metallic-means](pages/metallic-means.md)] - de Spinadel's family `σ_p^q`, of which the silver mean is `σ_2^1 = δ_2`.
- [[eigenvalue-continued-fractions](pages/eigenvalue-continued-fractions.md)] - the purely periodic continued fraction `[2; 2, 2, …]` of `1 + √2`.
- [[plastic-number](pages/plastic-number.md)] - the companion Pell numbers `A002203` as the power sums `(1 + √2)^n + (1 − √2)^n`, next to the same pairing for the plastic number.
- [[binomial-transform](pages/binomial-transform.md)] - the strips with a pinned end as a binomial transform of their skeletons.
- [[inscribed-polyomino](pages/inscribed-polyomino.md)] - the polyominoes with bounding box `2 × h`, `Q_{h+1} − 2` of them.
- [[tower-word-continued-fraction](pages/tower-word-continued-fraction.md)] - the tower words, silver by length.
- [[prime-castles](pages/prime-castles.md)] - the castles with no column of height 1, `F_{n−1}` of area `n`.
- [[aocp-generating-functions](pages/aocp-generating-functions.md)] - the same method for the Fibonacci numbers: a rational generating function, partial fractions, and the closed form.

## Footnotes

[^1]: https://oeis.org/A000129 (read 2026-10-16) - "Pell numbers: a(0) = 0, a(1) = 1; for n > 1, a(n) = 2*a(n-1) + a(n-2)", data "0, 1, 2, 5, 12, 29, 70, 169, 408, 985, 2378, 5741, 13860, 33461, …".
[^2]: Verified by execution (Python 3.11, 2026-10-16): the Binet forms of `P⋆_n` and `Q_n` for `n < 30`; `Q_n = P⋆_n + P⋆_{n−1}`; the binomial sums for `n < 30`; the convergents of `[2; 2, 2, …]` and of `[1; 2, 2, …]` to seven terms; the polyominoes with bounding box `2 × h` for `h ≤ 8` by enumeration (`1, 5, 15, 39, 97, 237, 575, 1391`); the compositions of `n` into parts at least 2 for `n ≤ 13` (`F_{n−1}`).
[^3]: https://oeis.org/A001333 and https://oeis.org/A002203 (read 2026-10-16) - "Pell-Lucas numbers: numerators of continued fraction convergents to sqrt(2)" and "Companion Pell numbers: a(n) = 2*a(n-1) + a(n-2), a(0) = a(1) = 2"; A034182, "Number of not-necessarily-symmetric n X 2 crossword puzzle grids", data "1, 5, 15, 39, 97, 237, …".
[^4]: [[barry-2005-catalan-transform](pages/barry-2005-catalan-transform.md)] §7 L1142-1157 - "Σ C(n, 2k) 2^k = 1, 1, 3, 7, 17, . . . = ((1 + √2)^n + (1 − √2)^n)/2 which is the sequence A001333. Related to this is the following formula for the Pell numbers A000129 ... Σ C(n, 2k + 1) 2^k = Pell(n)."
[^5]: Verified by execution (Python 3.11, 2026-10-16) for `w ≤ 9` by enumerating the 1-smooth skylines over `{1, 2, 3}`: `P⋆_w` with first column at height 1, `Q_{w+1}` with a free first column, and, with first column at height 1, `P⋆_{w−1}` ending at height 2 and `Q_{w−1}` ending at height 1 or 3.
[^6]: [[pe502-pell-castle-strip](pages/pe502-pell-castle-strip.md)] §"The castle reading" L23-28 - "D(x) = 1/(1 - 2x - x^2) is a two-atom composition scheme. Read it as counting tilings of a 1 × n strip using: a width-1 atom with weight 2, a width-2 atom with weight 1. Then a_n is the total weight of such tilings, and a_n = 2 a_{n-1} + a_{n-2} is just \"peel off the last atom.\""
