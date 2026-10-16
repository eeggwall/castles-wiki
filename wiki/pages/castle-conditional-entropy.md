---
title: Conditional entropy given block count and area
category: Analyses
summary: On the uniform distribution over the A^e(w, h) even-block castles of width w and height h, the entropy H(C) = log_2 A^e splits by the chain rule as H(B, N) + H(C | B, N), with B the block count and N the area. Computed for (w, h) up to (12, 3), (6, 4) and (5, 5) - H(N) − H(B) is between 1.46 and 2.24 bits, so the area is the more informative single statistic; H(B, N) − log_2 w approaches a constant depending on h; the residual is H(C | B, N) = w log_2 h − 1 − log_2 w − c(h) with c(3) between 1.39 and 1.41 (w = 8..14), c(4) between 2.29 and 2.36 (w = 6..10), c(5) between 3.03 and 3.05 (w = 5..8). The mutual information I(B; N) is at most 0.32 bits. B takes only even values, and its entropy is 1 bit below the Gaussian value; the entropy of N is within 0.005 bits of the Gaussian value by w = 10.
tags: [analysis, castle, entropy, information-theory, conditional-entropy, block-count, area, statistic, verification]
sources: [project-euler-502-brute-force, project-euler-502-observations]
created: 2026-09-21
updated: 2026-10-16
---

# Conditional entropy given block count and area

## The decomposition

Let `C` be a uniformly random even-block castle of width `w` and height `h`, one of `A^e(w, h)` ([[castle-counting-function](pages/castle-counting-function.md)]), so its entropy is `H(C) = log_2 A^e(w, h)`. [[castle-entropy](pages/castle-entropy.md)] writes this as

```
log_2 A^e  =  log_2 A − 1 + log_2(1 + S/A),        log_2 A  =  w log_2 h + log_2(1 − ((h−1)/h)^w).
```

This page asks how much of `H(C)` two statistics of the castle carry:

- the **block count** `B = blocks(C) = Σ_i max(0, c_i − c_{i−1})`, with `c_0 = 0` ([[castle-sign](pages/castle-sign.md)]);
- the **area** `N = Σ_i c_i` ([[castle-by-area](pages/castle-by-area.md)]).

On this page `B` and `N` are random variables, not the generating functions `B(q, z)` and `N(q)` of [[castle-notation](pages/castle-notation.md)]. Both are functions of `C`, so the chain rule gives

```
H(C)  =  H(B, N)  +  H(C | B, N),                                             (1)
```

and `H(C | X) = H(C) − H(X)` for `X = B`, `N` or `(B, N)`. Given `b` and `n`, the castle is uniform on the set

```
{ c ∈ {1, …, h}^w :  max c_i = h,  blocks(c) = b,  area(c) = n,  b even },
```

and `2^{H(C | B, N)} = A^e(w, h) / 2^{H(B, N)}`. Every number on this page is computed exactly from the joint distribution of `(B, N)`.[^1]

*Example: `w = 4`, `h = 2`.* The ten even-block castles all have two blocks, so `H(B) = 0`. Their areas are 5, 6, 7 and 8 (four, three, two and one castles), so `H(N) = 1.846` bits, and `H(C | N) = log_2 10 − 1.846 = 1.475` bits.

## The marginals

| `(w, h)` | `A^e(w, h)` | `H(C)` | `H(B)` | `H(N)` | `H(B, N)` | `H(B, N) − log_2 w` | `I(B; N)` |
|---|---:|---:|---:|---:|---:|---:|---:|
| `(3, 2)` | 6 | 2.585 | 0.000 | 1.459 | 1.459 | −0.126 | 0.000 |
| `(4, 2)` | 10 | 3.322 | 0.000 | 1.846 | 1.846 | −0.154 | 0.000 |
| `(6, 2)` | 28 | 4.807 | 0.811 | 2.356 | 2.856 | 0.271 | 0.311 |
| `(8, 2)` | 120 | 6.907 | 0.881 | 2.489 | 3.053 | 0.053 | 0.317 |
| `(10, 2)` | 528 | 9.044 | 0.625 | 2.643 | 3.089 | −0.233 | 0.179 |
| `(12, 2)` | 2080 | 11.022 | 0.800 | 2.826 | 3.486 | −0.099 | 0.140 |
| `(4, 3)` | 21 | 4.392 | 0.000 | 2.213 | 2.213 | 0.213 | 0.000 |
| `(6, 3)` | 307 | 8.262 | 0.678 | 2.881 | 3.483 | 0.898 | 0.076 |
| `(8, 3)` | 3031 | 11.566 | 1.181 | 3.190 | 4.273 | 1.273 | 0.097 |
| `(10, 3)` | 28479 | 14.798 | 1.363 | 3.378 | 4.659 | 1.337 | 0.082 |
| `(12, 3)` | 261615 | 17.997 | 1.502 | 3.527 | 4.957 | 1.372 | 0.071 |
| `(4, 4)` | 117 | 6.870 | 0.858 | 2.916 | 3.715 | 1.715 | 0.059 |
| `(6, 4)` | 1729 | 10.756 | 1.411 | 3.323 | 4.675 | 2.090 | 0.059 |
| `(4, 5)` | 122 | 6.931 | 0.950 | 3.191 | 4.029 | 2.029 | 0.112 |
| `(5, 5)` | 906 | 9.823 | 1.234 | 3.444 | 4.575 | 2.253 | 0.103 |

At `h = 3`, `H(B, N) − log_2 w` is `1.273, 1.337, 1.372` at `w = 8, 10, 12`. At `h = 2` the even-block castles of these widths have at most three distinct block counts, and `H(B)` stays below 1 bit.

The mutual information `I(B; N) = H(B) + H(N) − H(B, N)` is 0 in the three rows where `H(B) = 0` and between 0.059 and 0.317 bits in the others; the correlation of `B` and `N` is between 0.024 and 0.309 in those rows.

**Gaussian comparison.** For a statistic with variance `Var`, the entropy of a Gaussian is `(1/2) log_2(2πe Var)`. At `h = 3, 4` and `w = 6, 8, 10, 12`, `H(N)` is below this value by `0.055, 0.014, 0.005, 0.002` bits (`h = 3`) and `0.011, 0.005, 0.003, 0.0015` bits (`h = 4`). `B` takes only even values on this ensemble, so its distribution is spread over a lattice of spacing 2, and `H(B)` is below the Gaussian value by `0.99` to `1.03` bits at the same cells.[^1]

## The conditional entropies

| `(w, h)` | `H(C)` | `H(C \| B)` | `H(C \| N)` | `H(C \| B, N)` | `H(C) − w log_2 h` |
|---|---:|---:|---:|---:|---:|
| `(6, 2)` | 4.807 | 3.996 | 2.451 | 1.951 | −1.193 |
| `(8, 2)` | 6.907 | 6.026 | 4.417 | 3.854 | −1.093 |
| `(10, 2)` | 9.044 | 8.420 | 6.402 | 5.955 | −0.956 |
| `(12, 2)` | 11.022 | 10.222 | 8.196 | 7.537 | −0.978 |
| `(6, 3)` | 8.262 | 7.584 | 5.381 | 4.779 | −1.248 |
| `(8, 3)` | 11.566 | 10.385 | 8.376 | 7.293 | −1.114 |
| `(10, 3)` | 14.798 | 13.435 | 11.420 | 10.139 | −1.052 |
| `(12, 3)` | 17.997 | 16.495 | 14.470 | 13.040 | −1.022 |
| `(6, 4)` | 10.756 | 9.345 | 7.433 | 6.081 | −1.244 |
| `(5, 5)` | 9.823 | 8.590 | 6.379 | 5.248 | −1.786 |

**The area is the more informative statistic.** `H(C | B) − H(C | N) = H(N) − H(B)`, which is between 1.46 bits (at `(3, 2)`) and 2.24 bits (at `(4, 5)`) at every `(w, h)` of the first table, so conditioning on the area leaves less entropy than conditioning on the block count. The even-block condition acts on `B` and hardly on `N`: at `(10, 2)`, passing from all 1023 castles to the 528 even-block ones lowers `H(C)` by 0.954 bits, `H(B)` by 1.141 bits and `H(N)` by 0.055 bits, so `H(C | B)` rises by 0.187 bits and `H(C | N)` falls by 0.899 bits.

**The residual.** Write

```
H(C | B, N)  =  w log_2 h  −  1  −  log_2 w  −  c(h, w).                       (2)
```

The computed values are `c(3, w) = 1.387, 1.389, 1.395, 1.405` at `w = 8, 10, 12, 14`; `c(4, w)` between 2.293 and 2.356 at `w = 6, …, 10`; and `c(5, w)` between 3.034 and 3.050 at `w = 5, …, 8`. By Equation (1) and the decomposition of `log_2 A^e`, `c(h, w)` is `H(B, N) − log_2 w` minus the two corrections `log_2(1 − ((h−1)/h)^w)` and `log_2(1 + S/A)`. The last column of the second table is `H(C) − w log_2 h`, the sum of `−1` and those two corrections; at `h = 2` it is `−0.978` at `w = 12`.

## Where the two statistics come from

**Block count.** A castle of width `w` with `b` blocks stands on towers with `b − 1` blocks, and the towers of any height on a base of length `L` with `b` blocks number `T̂(L, b)`, which has a Narayana-polynomial generating function ([[tower-heap](pages/tower-heap.md)], [[tower-narayana-polynomial](pages/tower-narayana-polynomial.md)]). Over all heights these counts have no finite total for fixed `L`, so they are not the distribution of `B` on the ensemble of this page, which fixes the height.

**Area.** The castles of area `n` are the compositions of `n`, `2^{n−1}` of them; the convex ones are `A001523(n)` ([[weakly-unimodal-composition](pages/weakly-unimodal-composition.md)]). On the ensemble of this page the area is the sum of the `w` column heights.

**Fractional block count.** The fractional block count `B_α` of [[fractional-block-count](pages/fractional-block-count.md)] is the area at `α = 0` and the block count at `α = 1`. At `(4, 2)`, `B_{1/2}` takes ten distinct values on the ten even-block castles, so `H(C | B_{1/2}) = 0` there, against `H(C | N) = 1.475` and `H(C | B) = 3.322`.[^1]

## Appearances in Sources

- [[project-euler-502-brute-force](pages/project-euler-502-brute-force.md)] - the block-count formula and the enumeration of castles by column heights.
- [[project-euler-502-observations](pages/project-euler-502-observations.md)] - the count `A(w, h) = h^w − (h−1)^w` of castles without the even-block condition.

## Related Concepts

- [[castle-entropy](pages/castle-entropy.md)] - the entropy `log_2 A^e(w, h)` and its decomposition into `log_2 A − 1` and two corrections.
- [[castle-sign](pages/castle-sign.md)] - the sign `(−1)^{blocks}` behind the even-block condition.
- [[castle-by-area](pages/castle-by-area.md)] - castles counted by area.
- [[fractional-block-count](pages/fractional-block-count.md)] - the statistic `B_α` between the area and the block count.
- [[tower-heap](pages/tower-heap.md)] - the towers counted by blocks, `T̂(L, b)`.
- [[castle-compression](pages/castle-compression.md)] - code lengths for castles.
- [[castle-steganography](pages/castle-steganography.md)] - the parity of the block count as a channel of one bit per castle.
- [[one-bit-seminar](pages/one-bit-seminar.md)] - the seminar on the even-block condition as one bit, which uses the comparison of block count and area.

## Footnotes

[^1]: Verified by execution (Python 3.11, 2026-10-16): the joint distribution of `(B, N)` over the even-block castles of width `w` and height `h` by a dynamic program over columns (state: last height, whether `h` has been reached, block count, area), checked against `A^e(4, 2) = 10`, `A^e(6, 4) = 1729`, `A^e(12, 3) = 261615`; every entropy, mutual information and correlation in the tables, `c(h, w)` for the stated cells, the Gaussian comparisons for `B` and `N` at `h = 3, 4`, `w = 6, 8, 10, 12`, the any-parity comparison at `(10, 2)`, and the ten distinct values of `B_{1/2}` at `(4, 2)` with `B_0` the area and `B_1` the block count.
