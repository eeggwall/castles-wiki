---
title: Kolmogorov castles
category: Concepts
summary: A Kolmogorov castle is the castle of a merged order of two samples of n values each. Column i, for i = 1, …, 2n + 1, has height one more than the absolute lead |a_i − b_i| of the first sample over the second among the first i − 1 values, and each peak is marked by the sample that is ahead on it. The skyline is a Dyck-path castle, a Dyck-path castle with p peaks carries 2^p Kolmogorov castles, C(2n, n) in all, and the height minus 1 is n D_{n,n}, with D_{n,n} the two-sample statistic of Smirnov. The Kolmogorov castles of width 2n + 1 and height h number Σ_k (−1)^k [C(2n, n + kh) − C(2n, n + k(h − 1))], by the reflection count of Gnedenko and Korolyuk, also a sum of cosine powers from the path with 2h − 1 heights: 2^n at height 2 (A000079), 2(3^{n−1} − 2^{n−1}) at height 3 (A056182), and 16, 38, 14, 2 at heights 2 to 5 for width 9; those of height h grow at 2cos(π/(2h)) by width. Every member has n + 1 blocks. By the limit theorems of Kolmogorov (1933) and Smirnov, the share of height at most 1 + x√(w − 1) tends to K⋆(x) = 1 − 2 Σ (−1)^{k−1} e^{−2k²x²}, which reaches 95% at x = 1.3581, so the test's 5% critical value is a castle height.
tags: [concept, castle, kolmogorov-castle, kolmogorov-smirnov, two-sample-test, dyck-path, bridge, reflection-principle, ballot-theorem, central-binomial, path-graph, brownian-bridge, limit-law, block-count, parity, oeis, verification]
sources: [kolmogorov-1933-determinazione-empirica, smirnov-1944-approximation-distribution-laws, korolyuk-1955-two-independent-samples, lutsenko-marinich-matsak-2009-gnedenko-korolyuk-method, banderier-nicodeme-2010-bounded-discrete-walks, project-euler-502-brute-force]
created: 2026-10-28
updated: 2026-10-28
---

# Kolmogorov castles

## The two-sample test

Take two samples `x_1, …, x_n` and `y_1, …, y_n` of real numbers, all `2n` of them distinct, and let `F_n(t)` and `G_n(t)` be the fractions of the first and of the second sample that are at most `t`. Smirnov's statistic for two samples is

```
D_{n,n}  =  sup_t |F_n(t) − G_n(t)|,
```

the largest gap between the two empirical distribution functions, and large values of it count against the hypothesis that both samples come from the same continuous law.[^test] Under that hypothesis every arrangement of the two samples in the sorted list of all `2n` values is equally likely, so the law of `D_{n,n}` is a count over the `C(2n, n)` arrangements.[^merge]

The **merged order** of the samples is the word in the letters `X` and `Y` obtained by sorting the `2n` values and writing `X` for a value of the first sample and `Y` for a value of the second. It has `n` letters of each kind.

## Definition

For `i = 1, …, 2n + 1`, let `a_i` and `b_i` be the numbers of `X` and of `Y` among the first `i − 1` letters of the merged order, and call `a_i − b_i` the **lead** of the first sample. The skyline of the merged order is

```
c_i  =  1 + |a_i − b_i|,        i = 1, …, 2n + 1.
```

Between the `(i − 1)`-th and the `i`-th smallest values, `F_n − G_n` equals `(a_i − b_i)/n`, so

```
n D_{n,n}  =  max_i |a_i − b_i|  =  max_i c_i − 1.                          (1)
```

A **peak** of a castle is a maximal run of neighboring columns of height at least 2 ([[castle-notation](pages/castle-notation.md)]). The lead is 0 just outside a peak and nonzero on it, and it changes by 1 at each letter, so it keeps one sign on each peak: positive where the first sample is ahead and negative where the second is. A **Kolmogorov castle** of width `2n + 1` is the skyline `(c_1, …, c_{2n+1})` of a merged order together with a mark on each peak, `X` or `Y` for the sample that is ahead on it. `A_Kol(w, h)` is the number of Kolmogorov castles of width `w` and height `h`; it is 0 at even widths. The family is named for the Kolmogorov-Smirnov test and for Kolmogorov's limit law, which governs its heights (section *Kolmogorov's law*).

*Example.* The merged order `XXYYYX`, with `n = 3`, has the leads `0, 1, 2, 1, 0, −1, 0` and the skyline `(1, 2, 3, 2, 1, 2, 1)` of height 3, so `D_{3,3} = 2/3` by Equation (1). Its first peak is marked `X` and its second `Y`. In the drawing the bottom row is `#` and each cell above it carries the mark of its peak:

```
  . . X . . . .
  . X X X . Y .
  # # # # # # #
```

The six merged orders with `n = 2` give the six Kolmogorov castles of width 5:[^exec1]

```
XXYY           XYXY           XYYX           YXXY           YXYX           YYXX
(1,2,3,2,1)    (1,2,1,2,1)    (1,2,1,2,1)    (1,2,1,2,1)    (1,2,1,2,1)    (1,2,3,2,1)

  . . X . .                                                                  . . Y . .
  . X X X .      . X . X .      . X . Y .      . Y . X .      . Y . Y .      . Y Y Y .
  # # # # #      # # # # #      # # # # #      # # # # #      # # # # #      # # # # #
```

Two of them have height 3, with `D_{2,2} = 1`, and four have height 2, with `D_{2,2} = 1/2`. A peak of a castle is a whole run of raised columns: the skyline `(1, 2, 3, 2, 3, 2, 1)` has one peak, while its Dyck path has two peaks `UD`.

## Dyck-path castles with marked peaks

A **Dyck-path castle** is a castle with `c_1 = c_w = 1` whose neighboring columns differ by exactly 1 ([[castle-classification-shape](pages/castle-classification-shape.md)], Axis 3); lowering every column by one turns it into a Dyck path of `w − 1` steps.

**Theorem.** The merged orders of two samples of size `n` correspond one-to-one to the Kolmogorov castles of width `2n + 1`. The skyline of a Kolmogorov castle is a Dyck-path castle, and a Dyck-path castle of width `2n + 1` with `p` peaks is the skyline of exactly `2^p` Kolmogorov castles. So there are `C(2n, n)` Kolmogorov castles of width `2n + 1`.

*Proof.* The lead is 0 at `i = 1` and at `i = 2n + 1` and changes by `±1` at each letter, so `|a_i − b_i|` changes by exactly 1 at each letter, and the skyline is a Dyck-path castle. Conversely, a Dyck-path castle and a mark on each peak give back the lead: `a_i − b_i` is `c_i − 1` with the sign of the mark of the peak containing column `i`, and 0 outside the peaks. The differences of the lead are the letters, `+1` for `X` and `−1` for `Y`, so the merged order is determined. Every choice of marks occurs, since the lead may leave 0 upward or downward at the start of each peak. ∎

Summing over the skylines, the Dyck-path castles of width `2n + 1` weighted by 2 to the number of their peaks add up to `C(2n, n)`; without the weight they add up to the Catalan number `C_n` ([[catalan-numbers](pages/catalan-numbers.md)]). At fixed height the Dyck-path castles are A080936, the Dyck paths of semilength `n` and height `h − 1`, and a Dyck-path castle with `p` peaks lowers to a Dyck path that returns to 0 `p` times.[^exec2]

## Counting by height

A path of steps `±1` from 0 back to 0 is a **bridge**,[^bridge] so the leads of the merged orders are the bridges of `2n` steps, and a Kolmogorov castle has height at most `h` exactly when its lead stays strictly between `−h` and `h`.

**Theorem** (Gnedenko and Korolyuk). For `n ≥ 1` and `h ≥ 2`, the Kolmogorov castles of width `2n + 1` and height `h` number

```
A_Kol(2n + 1, h)  =  Σ_{k∈ℤ} (−1)^k [ C(2n, n + kh) − C(2n, n + k(h − 1)) ].                       (2)
```

*Proof.* The Kolmogorov castles of height at most `h` number `Σ_k (−1)^k C(2n, n + kh) = C(2n, n) − 2 Σ_{k≥1} (−1)^{k−1} C(2n, n − kh)`, the two forms being equal since `C(2n, n + kh) = C(2n, n − kh)`. This is Lemma 2.2 of [[lutsenko-marinich-matsak-2009-gnedenko-korolyuk-method](pages/lutsenko-marinich-matsak-2009-gnedenko-korolyuk-method.md)] with `c = h`, which counts the bridges that touch `h` or `−h` by inclusion-exclusion: a bridge that touches the two lines alternately at least `k` times is reflected after each of its first `k` alternate touches, in the line at height `h`, then at `3h`, then at `5h`, …, and ends at `±2kh`, where `C(2n, n − kh)` paths end on each side.[^lmm] Subtracting the castles of height at most `h − 1` leaves those of height `h`. ∎

[[korolyuk-1955-two-independent-samples](pages/korolyuk-1955-two-independent-samples.md)] states that the exact laws of `D_{n,n}` and of its one-sided form were found in the joint paper of Gnedenko and Korolyuk in *Doklady* 1951, and extends them by the same path counting to samples of sizes `n` and `pn`.[^gk]

*Example.* At `n = 4`, width 9, the castles of height at most 2, 3, 4 and 5 number

```
70 − 2(C(8, 2) − C(8, 0))  =  16,      70 − 2 C(8, 1)  =  54,      70 − 2 C(8, 0)  =  68,      70,
```

so the 70 Kolmogorov castles of width 9 have heights 2, 3, 4 and 5 in the numbers `16, 38, 14, 2`.

The counts `A_Kol(w, h)`, with the row sums `C(2n, n)`:[^exec3]

| `w` | `h = 2` | 3 | 4 | 5 | 6 | 7 | 8 | 9 | total |
|---|---|---|---|---|---|---|---|---|---|
| 3 | 2 | | | | | | | | 2 |
| 5 | 4 | 2 | | | | | | | 6 |
| 7 | 8 | 10 | 2 | | | | | | 20 |
| 9 | 16 | 38 | 14 | 2 | | | | | 70 |
| 11 | 32 | 130 | 70 | 18 | 2 | | | | 252 |
| 13 | 64 | 422 | 306 | 108 | 22 | 2 | | | 924 |
| 15 | 128 | 1330 | 1246 | 546 | 154 | 26 | 2 | | 3432 |
| 17 | 256 | 4118 | 4858 | 2518 | 880 | 208 | 30 | 2 | 12870 |

Every entry agrees with brute-force enumeration over the merged orders. The castles of height `n + 1` are the two orders `X^n Y^n` and `Y^n X^n`. The castles of height 2 are the `2^n` orders made of the pairs `XY` and `YX`, A000079(`n`), and Equation (2) gives `2(3^{n−1} − 2^{n−1})` castles of height 3, A056182(`n − 1`). The row sums are the central binomial coefficients, A000984(`n`).[^exec4]

### A cosine formula

The lead of a Kolmogorov castle of height at most `h` takes values in `−(h − 1), …, h − 1` and moves by `±1`, so these castles are the closed walks of `2n` steps from the middle vertex of the path on `2h − 1` vertices. With `A_path` the adjacency matrix of the path on `2h − 1` heights ([[zig-zag-castles](pages/zig-zag-castles.md)]), their number is the middle diagonal entry of `A_path^{2n}`. The eigenvectors of `A_path` are `(sin(πkv/(2h)))_{v = 1, …, 2h−1}`, `k = 1, …, 2h − 1`, with eigenvalues `2cos(πk/(2h))` and squared length `h`. Their middle entry `sin(πk/2)` is `±1` for odd `k` and 0 for even `k`, and `(2cos(πk/(2h)))² = 2 + 2cos(πk/h)`. Subtracting the same expression at `h − 1`, for `h ≥ 2`,

```
A_Kol(2n + 1, h)  =  (1/h) Σ_{j=0}^{h−1} (2 + 2cos((2j + 1)π/h))^n  −  (1/(h − 1)) Σ_{j=0}^{h−2} (2 + 2cos((2j + 1)π/(h − 1)))^n.     (3)
```

At `h = 2` the second sum is `0^n`, and Equation (3) is `2^n`; at `h = 3` it is `2 · 3^{n−1} − 2^n`.[^exec4]

### Growth by width

The largest term of Equation (3) is `(2 + 2cos(π/h))^n`, at `j = 0`, and the subtracted sum grows at the smaller `2 + 2cos(π/(h − 1))`, so

```
A_Kol(w + 2, h) / A_Kol(w, h)  →  2 + 2cos(π/h)  =  4cos²(π/(2h)),
```

and the Kolmogorov castles of height `h` grow at `2cos(π/(2h))` by width, along the odd widths, the largest eigenvalue of the path on `2h − 1` heights: `√2` at `h = 2`, `√3` at `h = 3`, `2cos(π/8) = 1.84776…` at `h = 4`, `2cos(π/10) = 1.90211…` at `h = 5`, increasing to 2.[^exec5]

## Blocks

The block count of a castle is `c_1 + Σ_{i=2}^{w} max(0, c_i − c_{i−1})`.[^blocks] A Dyck-path castle is a zig-zag castle with both end columns at height 1, so by Equation (4) of [[zig-zag-castles](pages/zig-zag-castles.md)] a Kolmogorov castle of width `2n + 1` has `(1 + 1 + 2n)/2 = n + 1` blocks: the bottom row and one block for each of the `n` up-steps of its skyline. The block count depends only on the width, so at width `2n + 1` all `C(2n, n)` Kolmogorov castles are even-block castles when `n` is odd, and none are when `n` is even:

```
A^e_Kol(2n + 1, h)  =  A_Kol(2n + 1, h)   (n odd),          A^e_Kol(2n + 1, h)  =  0   (n even).
```

For the example `XXYYYX`, `n = 3` and the castle has 4 blocks, one in row 1, two in row 2 and one in row 3.[^exec6]

## One sample ahead

The one-sided statistic `D^+_{n,n} = sup_t (F_n(t) − G_n(t))` is `max_i (a_i − b_i)/n`, so `n D^+_{n,n} + 1` is the height of the tallest peak marked `X`, or 1 if no peak is marked `X`. Split a merged order whose lead reaches `h` at its first visit to `h`: reflecting the rest of the path in the line at height `h` maps these orders onto the paths from 0 to `2h` (Lemma 2.1 of [[lutsenko-marinich-matsak-2009-gnedenko-korolyuk-method](pages/lutsenko-marinich-matsak-2009-gnedenko-korolyuk-method.md)]), and summing over the step of the first visit counts them by the ballot numbers `(h/k) C(k, (k − h)/2)` (Theorem 1 of [[korolyuk-1955-two-independent-samples](pages/korolyuk-1955-two-independent-samples.md)] at `p = 1`).[^lemma21] So for `1 ≤ h ≤ n` the Kolmogorov castles of width `2n + 1` whose `X` peaks all have height at most `h` number

```
C(2n, n) − C(2n, n − h).                                                    (4)
```

At `h = 1` no peak is marked `X`, and Equation (4) is `C(2n, n) − C(2n, n − 1) = C(2n, n)/(n + 1)`, the Catalan number `C_n`: one Kolmogorov castle for each Dyck-path castle, with every peak marked `Y`.[^exec7]

## Kolmogorov's law

[[kolmogorov-1933-determinazione-empirica](pages/kolmogorov-1933-determinazione-empirica.md)] proves that for one sample of size `n` from a continuous `F`, the probability that `sup |F_n − F| < λ/√n` tends, uniformly in `λ`, to

```
K⋆(λ)  =  Σ_{k=−∞}^{+∞} (−1)^k e^{−2k²λ²}  =  1 − 2 Σ_{k≥1} (−1)^{k−1} e^{−2k²λ²},          (5)
```

and tabulates it, with `K⋆(1) = 0.7300` and `K⋆(1.4) = 0.9603`.[^kol] The bare letter `K` is taken on the wiki, by the sandpile group and the Kac-Murdock-Szegő matrix ([[castle-notation](pages/castle-notation.md)]), so Kolmogorov's law is starred. Kolmogorov's proof writes the finite-`n` law as the probability that a random walk stays strictly between two walls and returns to its start, and evaluates its limit through the Green's function of the heat equation in a strip, an alternating sum of Gaussians over the images of the starting point; the count of the castles of height at most `h` in the proof of Equation (2) is an alternating sum of the same kind, over the reflections of the walk of the lead. Smirnov's Theorem 9 in [[smirnov-1944-approximation-distribution-laws](pages/smirnov-1944-approximation-distribution-laws.md)] gives the same limit for two samples: for sizes `n_1` and `n_2` growing with a fixed ratio, the probability that `D(n_1, n_2) ≤ λ/√n`, with `n = n_1 n_2/(n_1 + n_2)`, tends to `K⋆(λ)`.[^smi] For `n_1 = n_2 = n` this is a statement about `√(n/2) D_{n,n}`, and the limit also follows from the count of the castles of height at most `h` in the proof of Equation (2), by Stirling's formula, `C(2n, n − kh)/C(2n, n) → e^{−2k²x²}` when `h/√(2n) → x`.[^limit] `K⋆` is also the law of the maximum of `|B(t)|` over `0 ≤ t ≤ 1`, with `B` the Brownian bridge.[^bb] By Equation (1) and `w − 1 = 2n`, `√(n/2) D_{n,n} = (max_i c_i − 1)/√(w − 1)`, so:

**Theorem.** For every `x > 0`, as the odd width `w` grows, the share of the Kolmogorov castles of width `w` whose height is at most `1 + x√(w − 1)` tends to `K⋆(x)`, and the share whose `X` peaks all have height at most `1 + x√(w − 1)` tends to `1 − e^{−2x²}`.

The one-sided limit is Smirnov's, as restated in [[korolyuk-1955-two-independent-samples](pages/korolyuk-1955-two-independent-samples.md)],[^gk] and it is the Rayleigh law of the height of a bridge, Theorem 6 of [[banderier-nicodeme-2010-bounded-discrete-walks](pages/banderier-nicodeme-2010-bounded-discrete-walks.md)], which holds for bridges with any finite set of jumps and no drift.[^rayleigh] The convergence is slow:[^exec8]

| `x` | `K⋆(x)` | `w = 2001` | `w = 200001` |
|---|---|---|---|
| 0.5 | 0.03605 | 0.04578 | 0.03662 |
| 1.0 | 0.73000 | 0.73653 | 0.73188 |
| 1.5 | 0.97778 | 0.98040 | 0.97784 |

**The critical value as a castle height.** `K⋆(x) = 0.95` at `x = 1.35810…`, and `K⋆(1.36) = 0.95051`. So for large `w` about 95% of the Kolmogorov castles of width `w` have height at most `1 + 1.3581√(w − 1)`: at width 400001, `n = 200000`, the castles of height at most `1 + 1.36√400000`, that is at most 861, are a share 0.95088 of all. The **critical height** of width `w` is the smallest `h` for which at least 95% of the Kolmogorov castles of width `w` have height at most `h`; a merged order is significant at the 5% level exactly when its castle is taller than the critical height.[^exec8]

| `w` | `n` | critical height | share of height at most it | `1 + 1.3581√(w − 1)` |
|---|---|---|---|---|
| 11 | 5 | 5 | 0.99206 | 5.29 |
| 21 | 10 | 7 | 0.98766 | 7.07 |
| 41 | 20 | 9 | 0.96646 | 9.59 |
| 101 | 50 | 14 | 0.96081 | 14.58 |
| 201 | 100 | 20 | 0.96362 | 20.21 |
| 2001 | 1000 | 61 | 0.95160 | 61.74 |
| 20001 | 10000 | 193 | 0.95177 | 193.06 |

In each row the critical height is the integer part of `1 + 1.3581√(w − 1)`. For two samples of 50 values, 0.93221 of the Kolmogorov castles of width 101 have height at most 13 and 0.96081 at most 14, so a merged order is significant at the 5% level exactly when its castle has height at least 15, that is, when `D_{50,50} ≥ 0.28`. The order `XXYYYX` of the example is not: 12 of the 20 Kolmogorov castles of width 7 are at least as tall as its height 3, a share of `3/5`.

## Related Concepts

- [[castle-classification-shape](pages/castle-classification-shape.md)] - the Dyck-path castles, the skylines of the Kolmogorov castles, with their counts at fixed height (A080936).
- [[zig-zag-castles](pages/zig-zag-castles.md)] - the block count `(c_1 + c_w + w − 1)/2` and the path matrix `A_path`, whose powers count the Kolmogorov castles of each height.
- [[catalan-numbers](pages/catalan-numbers.md)], [[dyck-words](pages/dyck-words.md)] - Dyck paths; the Kolmogorov castles with every peak marked `Y` are counted by the Catalan numbers.
- [[castle-classification-growth](pages/castle-classification-growth.md)] - growth types by width; the Kolmogorov castles of height `h` grow at `2cos(π/(2h))`.
- [[castle-notation](pages/castle-notation.md)] - `A_Kol(w, h)`, `D_{n,n}` and `K⋆(x)`.

## Footnotes

[^test]: [[smirnov-1944-approximation-distribution-laws](pages/smirnov-1944-approximation-distribution-laws.md)] §5.1 p.203 L1222-L1256 [synthesis] - two series of `n_1` and `n_2` independent observations with empirical distribution functions `S_{n_1}` and `S_{n_2}`, the measure of discrepancy `D(n_1, n_2) = sup |S_{n_1}(x) − S_{n_2}(x)|`, and the task of bounding its random variation, "превышение которых мало вероятно при данных n_1 и n_2 и ставит под сомнение гипотезу о тождественности закона распределения в обеих сериях наблюдений". [[lutsenko-marinich-matsak-2009-gnedenko-korolyuk-method](pages/lutsenko-marinich-matsak-2009-gnedenko-korolyuk-method.md)] §4 p.144 L843-L844 calls `D_{n,n}` "Smirnov's statistic".
[^merge]: [[korolyuk-1955-two-independent-samples](pages/korolyuk-1955-two-independent-samples.md)] §1 p.83 L137-L152 [synthesis] - "Заметим прежде всего, что любые взаимные расположения наблюдений обеих серий равновероятны", each of the `N!` arrangements having probability `1/N!`. [[lutsenko-marinich-matsak-2009-gnedenko-korolyuk-method](pages/lutsenko-marinich-matsak-2009-gnedenko-korolyuk-method.md)] §2 pp.137-138 L316-L340 [synthesis] - the merged sample and "all allocations of the symbols 1 and −1 in the sequence (εi) have the same probability."
[^bridge]: [[banderier-nicodeme-2010-bounded-discrete-walks](pages/banderier-nicodeme-2010-bounded-discrete-walks.md)] Fig. 1 p.37 L96-L104, L140 [synthesis] - the walks "ending at 0" are the bridges, one of "The four types of paths: walks, bridges, meanders, and excursions".
[^lmm]: [[lutsenko-marinich-matsak-2009-gnedenko-korolyuk-method](pages/lutsenko-marinich-matsak-2009-gnedenko-korolyuk-method.md)] §2 Lemma 2.2 and proof pp.135-137 L193-L304 [synthesis] - the number `C_{2n}^n − 2 Σ_{i=1}^{[n/c]} (−1)^{i−1} C_{2n}^{n−ic}` of lines from `(0, 0)` to `(2n, 0)` with slopes `±1` that meet neither `y = c` nor `y = −c`, proved by reflecting in `y = c`, `y = 3c`, `y = 5c`, … and the recursion `|L_i| = 2C_{2n}^{n−ic} − |L_{i+1}|`.
[^gk]: [[korolyuk-1955-two-independent-samples](pages/korolyuk-1955-two-independent-samples.md)] pp.82-83 L88-L112 [synthesis] - Smirnov's Theorem 2, `lim P{√(nm/(n+m)) D(n, m) < z} = K(z)` and `lim P{√n D⁺(n, m) < z} = 1 − e^{−2z²}` for `z > 0` (read from the page image), and "В частном случае n = m задача разыскания функций Φ⁺_nm(z) и Φ_nm(z) была решена в совместной работе автора с Б. В. Гнеденко [см. (2)]", reference (2) being Gnedenko and Korolyuk, *Доклады Ак. наук СССР* LXXX, № 4 (1951), 525-528, at p.96 L877-L889.
[^lemma21]: [[lutsenko-marinich-matsak-2009-gnedenko-korolyuk-method](pages/lutsenko-marinich-matsak-2009-gnedenko-korolyuk-method.md)] §2 Lemma 2.1 p.135 L143-L171 - "Reflecting, with respect to the line y = c, the part of the polygonal line to the right of the first intersection point with y = c we obtain a new polygonal line starting at the point (0; 0) and ending at the point (2n; 2c)."; the count `C_{2n}^n − C_{2n}^{n−c}` for `c ≤ n`. [[korolyuk-1955-two-independent-samples](pages/korolyuk-1955-two-independent-samples.md)] §1 pp.84-85 L160-L237 [synthesis] - the paths split at the first crossing of `x = c`, formula (4), and `N_k(c) = (c/k) C_k^{(k−c)/(p+1)}` (7), read from the page images.
[^kol]: [[kolmogorov-1933-determinazione-empirica](pages/kolmogorov-1933-determinazione-empirica.md)] §1 Theorem I and the table p.84 L48-L75 [synthesis] - Theorem I, formula [1] and the values `Φ(1,0) = 0,7300` and `Φ(1,4) = 0,9603` of the table, read from the page image.
[^smi]: [[smirnov-1944-approximation-distribution-laws](pages/smirnov-1944-approximation-distribution-laws.md)] §5.1 p.203 L1242-L1256 [synthesis] - Theorem 9, `P(n_1, n_2) = P{D(n_1, n_2) ≤ λ/√n} → Φ(λ)` with `n = n_1 n_2/(n_1 + n_2)` and `Φ(λ) = Σ_{k=−∞}^{+∞} (−1)^k e^{−2k²λ²}`, read from the page image, and "Предельный закон Φ(λ) здесь тот же самый, как и для верхней грани уклонений |S_n(x) − F(x)|". [[kolmogorov-1933-determinazione-empirica](pages/kolmogorov-1933-determinazione-empirica.md)] §3 pp.89-91 L261-L394 [synthesis] - the walk between the walls, the Green's function of the heat equation and the alternating sum `u(0, 0, s, t) = (1/(2√(πt))) Σ (−1)^k e^{−(s−2k)²/(4t)}`, read from the page images.
[^limit]: [[lutsenko-marinich-matsak-2009-gnedenko-korolyuk-method](pages/lutsenko-marinich-matsak-2009-gnedenko-korolyuk-method.md)] §2 Corollary 2.2 pp.138-140 L395-L544 [synthesis] - `lim P(√(n/2) D_{n,n} < z) = K(z)` and `lim P(√(n/2) D^+_{n,n} < z) = 1 − e^{−2z²}` for `z > 0`, from Stirling's formula `C_{2n}^{n−kc}/C_{2n}^n = e^{−2k²z² + o(1)}` with `c = ⌈z√(2n)⌉`. The paper's strict inequality and the theorem's "at most" give the same limit, since `K⋆` and `1 − e^{−2x²}` are continuous.
[^bb]: [[lutsenko-marinich-matsak-2009-gnedenko-korolyuk-method](pages/lutsenko-marinich-matsak-2009-gnedenko-korolyuk-method.md)] §3 pp.140-144 L546-L825 [synthesis] - the Brownian bridge `W⁰(t) = W(t) − tW(1)`, equality (10), `P(max |W⁰(t)| < z) = K(z)` (the text layer drops the absolute value bars), proved through Proposition 3.2 and Corollary 2.2.
[^rayleigh]: [[banderier-nicodeme-2010-bounded-discrete-walks](pages/banderier-nicodeme-2010-bounded-discrete-walks.md)] §4.1 Theorem 6 p.42 L402-L411 [synthesis] - for a discrete bridge `(B_k)_{k=0,…,n}` with zero drift and variance `σ²`, `lim Pr(max_{0≤k≤n} B_k > xσ√n) = e^{−2x²}(1 + O(1/√n))`, "a Rayleigh limit law of parameter 1/2". For the steps `±1`, `σ = 1`, and the bridge has `2n` steps.
[^blocks]: [[project-euler-502-brute-force](pages/project-euler-502-brute-force.md)] §"brute" L24 - "= c_1 + \sum_{i=2}^{w} \max(0, c_i - c_{i-1})", the column-height block-count formula.
[^exec1]: Verified by execution (Python 3.11, 2026-10-28): `bin/python/kolmogorov_castles.py` items [1] and [2], run log `bin/python/kolmogorov_castles-run.log`. The example `XXYYYX` and its drawing; the six Kolmogorov castles of width 5, their marks, heights and `D_{2,2}`.
[^exec2]: Verified by execution (Python 3.11, 2026-10-28): `bin/python/kolmogorov_castles.py` items [3] and [5], run log `bin/python/kolmogorov_castles-run.log`. For `n = 1, …, 9`, every merged order gives a Dyck-path castle with one mark per peak, distinct orders give distinct marked castles, and each skyline carries `2^p` of them; the skylines of height `h` against A080936(`n`, `h − 1`) (https://oeis.org/A080936, "Triangle read by rows: T(n,k) is the number of Dyck paths of semilength n and height k (1 <= k <= n).", read 2026-10-28).
[^exec3]: Verified by execution (Python 3.11, 2026-10-28): `bin/python/kolmogorov_castles.py` items [3] and [4], run log `bin/python/kolmogorov_castles-run.log`. Equation (2) against the heights of all merged orders for `n ≤ 9`; the two forms of the count of height at most `h` agree with each other and with the path-matrix entry for `n < 40`.
[^exec4]: Verified by execution (Python 3.11, 2026-10-28): `bin/python/kolmogorov_castles.py` items [3] and [5], run log `bin/python/kolmogorov_castles-run.log`. Equation (3) against Equation (2) for `n ≤ 20`, `h ≤ 12`; `A_Kol(2n + 1, 2)` against every term of A000079 from `n = 1` (34 terms), `A_Kol(2n + 1, 3)` against A056182(`n − 1`) (29 terms), and the row sums against A000984 (28 terms), all at offset 0 (https://oeis.org, data fields read 2026-10-28).
[^exec5]: Verified by execution (Python 3.11, 2026-10-28): `bin/python/kolmogorov_castles.py` item [8], run log `bin/python/kolmogorov_castles-run.log`. `A_Kol(8003, h)/A_Kol(8001, h)` against `2 + 2cos(π/h)` for `h = 2, …, 8`, equal to twelve decimals.
[^exec6]: Verified by execution (Python 3.11, 2026-10-28): `bin/python/kolmogorov_castles.py` items [1], [3] and [9], run log `bin/python/kolmogorov_castles-run.log`. Every Kolmogorov castle of width `2n + 1` has `n + 1` blocks for `n ≤ 9`; the even-block counts for `n ≤ 8`.
[^exec7]: Verified by execution (Python 3.11, 2026-10-28): `bin/python/kolmogorov_castles.py` items [6] and [13], run log `bin/python/kolmogorov_castles-run.log`. Equation (4) against enumeration for `n ≤ 9` and `1 ≤ h ≤ n + 1`, with `C(2n, n − h) = 0` for `h > n`; at `h = 1` against every term of A000108, the Catalan numbers (31 terms, https://oeis.org/A000108, read 2026-10-28); the first-passage sum with the ballot numbers against `C(2n, n − h)`.
[^exec8]: Verified by execution (Python 3.11, 2026-10-28): `bin/python/kolmogorov_castles.py` items [1] and [7], run log `bin/python/kolmogorov_castles-run.log`. `K⋆` from Equation (5), its 95% point by bisection; the shares with `log Γ`, and the critical heights in rational arithmetic for `n ≤ 1000`; the share `3/5` for `XXYYYX` by enumeration.
