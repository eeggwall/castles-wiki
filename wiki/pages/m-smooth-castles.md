---
title: m-smooth castles
category: Concepts
summary: An m-smooth castle is a castle whose neighbouring columns differ in height by at most m. Starting from the 1-smooth castles, the anchored m-smooth castles of exact height h (first column at height 1) are counted for m = 2, 3, 4 and h up to 12. The count is strips_m(w, h) − strips_m(w, h − 1); the reflection j ↔ h + 1 − j keeps the strip denominator at degree ≤ ⌈h/2⌉ and the exact-height recurrence at order ≤ h for every m. The first castle has width w_min = ⌈(h − 1)/m⌉ + 1, and there are C(slack + w_min − 2, w_min − 2) of them, slack = (w_min − 1)m − (h − 1). The growth constant lies between 2m + 1 − m(m+1)/h and 2m + 1. At h ≤ m + 1 the rule is vacuous: the free count is h^w − (h − 1)^w and its even-block part is the PE 502 count F(w, h). On the diagonal h = m + 2 the Pell structure survives: strips x/(1 − (m+1)x − mx²) (Pell, A007482, A015530, A015537 for m = 1…4), castles m·x³/((1 − (m+1)x − mx²)(1 − (m+1)x)), growth the root of x² − (m+1)x − m. An addendum lists what does not extend from m = 1: the x^h numerator, the explicit eigenvalues and Chebyshev identities, the Motzkin-triangle readings, and the irregular parity orders.
tags: [concept, castle, castle-type, m-smooth, 1-smooth, pell, transfer-matrix, exact-height, parity, generating-functions, oeis]
sources: [pe502-pell-castle-strip, banderier-nicodeme-2010-bounded-discrete-walks]
created: 2026-10-06
updated: 2026-10-07
---

# m-smooth castles

## Definition

A castle is a skyline `(c_1, …, c_w)` of columns standing on a full bottom row, with maximum height exactly `h` ([[castle-polyomino](pages/castle-polyomino.md)]). An **m-smooth castle** is a castle whose neighbouring columns differ in height by at most `m` ([[castle-classification-shape](pages/castle-classification-shape.md)] Axis 2). An **anchored** m-smooth castle also has its first column at height 1:

```
c_1 = 1,      |c_{i+1} − c_i| ≤ m  (1 ≤ i < w),      max_i c_i = h.
```

- **Construction rule.** Start at height 1; at each step move up or down by at most `m`, or stay, never leaving `{1, …, h}`; and reach height `h` at least once.
- **Examples.** At `m = 2`, `h = 4`, the two anchored castles of width 3 are `(1, 2, 4)` and `(1, 3, 4)`; `(1, 3, 2, 4)` and `(1, 2, 4, 2)` have width 4.
- **Non-examples.** At `m = 2`, `(1, 4, 3)` rises by 3 in one step; `(1, 3, 3)` is not a castle of height 4.

The 1-smooth castles are the case `m = 1` ([[1-smooth-castles](pages/1-smooth-castles.md)]). This page starts from them and follows the anchored castles to `m = 2, 3, 4`; the free and the both-ends-pinned boundary conditions are in [Other boundary conditions](#other-boundary-conditions).

**Counts.** For width `w`, ceiling `h` and step bound `m`:

- `strips_m(w, h)` is the number of anchored m-smooth skylines of width `w` with every column in `{1, …, h}`. They need not reach `h`.
- `smooth_m(w, h)` is the number of anchored m-smooth castles of width `w` and exact height `h`.

`strips_1` and `smooth_1` are the `strips` and `smooth` of [[1-smooth-castles](pages/1-smooth-castles.md)]. As there,

```
smooth_m(w, h)  =  strips_m(w, h) − strips_m(w, h − 1).
```

## 1. The starting point: 1-smooth castles (m = 1)

At `m = 1` ([[1-smooth-castles](pages/1-smooth-castles.md)]):

- **Transfer matrix.** The tridiagonal `h × h` matrix `I + A_path`, ones on the diagonal and both off-diagonals.
- **Cancellation.** Eigenvectors that are antisymmetric under the flip `j ↔ h + 1 − j` drop out, so the strip denominator `η_h` has degree `⌈h/2⌉`.
- **Generating function.** `Σ_w smooth(w, h) x^w = x^h/(η_h η_{h−1})`: the numerator is the single monomial `x^h`, and the recurrence has order exactly `h`.
- **Eigenvalues.** Explicit, `1 + 2cos(πk/(h+1))`, with Chebyshev formulas for the determinants.
- **Growth.** `1 + 2cos(π/(h+1))`, climbing to 3.
- **Parity.** The signed recurrence orders are irregular (`3, 5, 7, 7, 9, …`).
- **Pell.** At `h = 3`, the Pell castles: strips `x/(1 − 2x − x²)`, castles `x³/((1 − 2x − x²)(1 − 2x))`, growth `1 + √2`.

Sections 2 and 3 carry each item to `m ≥ 2`; the addendum lists what does not carry over.

## 2. m = 2

The first step past `m = 1`, at the ceiling `h = 4`:[^exec]

| | `m = 1`, `h = 4` | `m = 2`, `h = 4` |
|---|---|---|
| transfer matrix | `4 × 4`, ones for `\|a − b\| ≤ 1` | `4 × 4`, ones for `\|a − b\| ≤ 2` (all but the two corners) |
| `Σ_w strips_m(w, 4) x^w` | `x(1 − x)/(1 − 3x + x²)`: `1, 2, 5, 13, 34, …` | `x/(1 − 3x − 2x²)`: `1, 3, 11, 39, 139, 495, …` = A007482(`w − 1`)[^a007482] |
| first width, number there | `w = 4`, 1 (the staircase) | `w = 3`, 2: `(1, 2, 4)`, `(1, 3, 4)` |
| `smooth_m(w, 4)` | `0, 0, 0, 1, 5, 19, 64, …` | `0, 0, 2, 12, 58, 252, 1034, …` |
| `Σ_w smooth_m(w, 4) x^w` | `x⁴/((1 − 3x + x²)(1 − 2x − x²))` | `2x³/((1 − 3x − 2x²)(1 − 3x))` |
| growth | `φ² ≈ 2.618` | `(3 + √17)/2 ≈ 3.562` |

At `m = 2` the ceiling `h = 4` is the first non-vacuous one (3.3), and its strip generating function has the two-term Pell shape (3.6).

## 3. Every m

### 3.1 The band matrix

The m-smooth rule on heights `{1, …, h}` is the `h × h` band matrix with entry 1 when `|a − b| ≤ m` and 0 otherwise; at `m = 1` it is `I + A_path`. The anchored strip count is `strips_m(w, h) = e_1ᵀ (band)^{w−1} 𝟙`. When `h ≤ m + 1` every entry of the band is 1.

### 3.2 The reflection

For every `m` the band matrix commutes with the flip `j ↔ h + 1 − j`. So its eigenvectors can be chosen symmetric or antisymmetric, and the all-ones vector `𝟙`, which is symmetric, is orthogonal to the antisymmetric ones. Only the symmetric part, of dimension `⌈h/2⌉`, contributes to `strips_m`. Consequences, for every `m` and `h`:

- the reduced denominator of `Σ_w strips_m(w, h) x^w` has degree at most `⌈h/2⌉`;
- the reduced denominator of `Σ_w smooth_m(w, h) x^w` divides the product of the denominators at `h` and `h − 1`, so it has degree at most `⌈h/2⌉ + ⌈(h−1)/2⌉ = h`, and `smooth_m(·, h)` satisfies a linear recurrence of order at most `h`.

At `m = 1` both bounds are attained. At `m ≥ 2` the degrees can be smaller: zero eigenvalues contribute no factor, and the exact-height degree drops below `h` for `m = 2`, `h = 8, …, 11`, for `m = 3`, `h = 9, …, 12`, and for `m = 4`, `h = 12` (tables of 3.7).[^exec]

### 3.3 Small ceilings: the rule is vacuous, and F(w, h) appears

When `h ≤ m + 1`, no step inside `{1, …, h}` is longer than `m`, so every castle of height `h` is m-smooth. For these ceilings:

- the free count (any first column) is `h^w − (h − 1)^w`, all castles of width `w` and exact height `h` ([[castle-notation](pages/castle-notation.md)] `A(w, h)`);
- its even-block part is `F(w, h)`, the Project Euler 502 count;
- the anchored count is `smooth_m(w, h) = h^{w−1} − (h − 1)^{w−1}`, and its even-block part is `F(w − 1, h)`. Deleting the first column, which has height 1, maps the anchored castles of width `w` onto all castles of width `w − 1`, and keeps the block count: `blocks = c_1 + Σ max(0, c_{i+1} − c_i)` loses `1 + max(0, c_2 − 1) = c_2` and gains `c_2`.

So for each fixed `h`, the m-smooth castles run from the 1-smooth castles at `m = 1` to all castles at `m ≥ h − 1`, and the PE 502 count `F(w, h)` is the even-block count at the top of that range.[^exec]

### 3.4 The exact-height generating function

Reaching height `h` from height 1 takes at least `⌈(h − 1)/m⌉` steps, so the first anchored castle has width

```
w_min  =  ⌈(h − 1)/m⌉ + 1,        slack  =  (w_min − 1)·m − (h − 1),    0 ≤ slack < m.
```

**Proposition.** For every `m ≥ 1` and `h ≥ 2`, `smooth_m(w, h) = 0` for `w < w_min`, and

```
smooth_m(w_min, h)  =  C(slack + w_min − 2,  w_min − 2).
```

*Proof.* A castle of width `w_min` cannot reach `h` before its last column, since `w_min − 2` steps rise by at most `(w_min − 2)m < h − 1`. So its `w_min − 1` steps sum to `h − 1`. Write each step as `m − d_i` with `d_i ≥ 0`; then `Σ d_i = slack < m`, so every step is a rise and the skyline stays above height 1. The castles are the solutions of `d_1 + ⋯ + d_{w_min − 1} = slack` in nonnegative integers, `C(slack + w_min − 2, w_min − 2)` of them. ∎

So `Σ_w smooth_m(w, h) x^w = x^{w_min}·N(x)/D(x)` with `N(0) = C(slack + w_min − 2, w_min − 2)` and `deg D ≤ h`.

- **At `m = 1`.** `w_min = h` and `slack = 0`, so `N(0) = 1`; the degree count of [[1-smooth-castles](pages/1-smooth-castles.md)] §3.3 then forces `N = 1`, the numerator `x^h`.
- **At `m ≥ 2`.** `w_min < h` for `h ≥ m + 2`, and `N` is not a constant in general: at `m = 2`, `h = 5` it is `1 + x` (tables of 3.7). When `h − 1` is a multiple of `m`, `slack = 0` and the first castle is the unique staircase with steps of `m`.

### 3.5 Growth

Write `ρ_{h,m}` for the largest eigenvalue of the band matrix, the growth constant of `smooth_m(·, h)`.

- **Bounds.** For `h ≥ m + 1`, `2m + 1 − m(m+1)/h ≤ ρ_{h,m} ≤ 2m + 1`. The upper bound is the largest row sum. The lower bound is the Rayleigh quotient of `𝟙`: the band has `(2m + 1)h − m(m + 1)` ones. So `ρ_{h,m} → 2m + 1` as `h → ∞`, and `ρ_{h,m} = h` for `h ≤ m + 1`.
- **Asymptotics.** As at `m = 1`, the subtracted `strips_m(w, h − 1)` grows at `ρ_{h−1,m} < ρ_{h,m}`, so `smooth_m(w, h)` grows like `ρ_{h,m}^w` and the fraction of anchored strips that reach their ceiling tends to 1.
- **No closed-form eigenvalues.** For `m ≥ 2` the eigenvalues have no formula like `1 + 2cos(πk/(h+1))`; the growth constants in the tables are computed one at a time, and from `h = m + 3` on they are cubic or higher in every case computed.[^exec] The generating functions themselves do have a closed form, in the `2m` roots `u` of `1 − x(u^{−m} + ⋯ + u^m)`, by the [[kernel-method](pages/kernel-method.md)] between two walls ([[banderier-nicodeme-2010-bounded-discrete-walks](pages/banderier-nicodeme-2010-bounded-discrete-walks.md)]).

### 3.6 The diagonal h = m + 2: the Pell structure survives

At `h = m + 2` the band matrix is all ones except the two corners `(1, h)` and `(h, 1)`, so every middle row is all ones. On vectors of the form `(a, b, …, b, a)` it acts as

```
(a, b)  ↦  (a + m·b,  2a + m·b),        the 2 × 2 matrix  [[1, m], [2, m]],
```

and `𝟙` is such a vector. Reading off the first coordinate gives, for every `m ≥ 1`,

```
Σ_w strips_m(w, m + 2) x^w  =  x / (1 − (m+1)x − m·x²),
Σ_w smooth_m(w, m + 2) x^w  =  m·x³ / ((1 − (m+1)x − m·x²)(1 − (m+1)x)),
```

the second because `strips_m(w, m + 1) = (m + 1)^{w−1}` (3.3). The growth constant is the root of `x² − (m+1)x − m`, `(m + 1 + √(m² + 6m + 1))/2`.

- **At `m = 1`** these are the Pell strip and the Pell castles ([[pell-castle](pages/pell-castle.md)]).
- **The strip rows** are Pell A000129(`w`) at `m = 1`, A007482(`w − 1`) at `m = 2`, A015530(`w`) at `m = 3` and A015537(`w`) at `m = 4`, the last two named "Expansion of x/(1 - 4*x - 3*x^2)" and "Expansion of x/(1 - 5*x - 4*x^2)".[^a007482][^a015530][^a015537]
- **The two-atom reading of [[pell-castle-strip](pages/pell-castle-strip.md)] carries over.** `1/(1 − (m+1)x − m·x²)` counts sequences of a width-1 atom of weight `m + 1` and a width-2 atom of weight `m`.
- **Not metallic past `m = 1`.** The growth constant is a metallic mean only at `m = 1`, where `x² − 2x − 1` gives silver ([[metallic-means](pages/metallic-means.md)]).

### 3.7 Tables

For `h ≤ m + 1` every row is `h^{w−1} − (h − 1)^{w−1}` (3.3), so each table starts at `h = m + 2`. "Numerator" is `N(x)` times `x^{w_min}`, normalized so that the denominator has constant term 1. "Den. degree" is the degree of the reduced denominator (at most `h`, 3.2). "Degree" is the degree of the growth constant as an algebraic number.[^exec]

#### m = 2

| `h` | `w_min` | `smooth_2(w, h)`, `w = w_min, …` | numerator | den. degree | growth | degree |
|---|---|---|---|---|---|---|
| 4 | 3 | `2, 12, 58, 252, 1034, 4092, 15802, …` | `2x³` | 3 | `(3 + √17)/2 ≈ 3.5616` | 2 |
| 5 | 3 | `1, 8, 46, 233, 1102, 4996, 22009, …` | `x³(1 + x)` | 5 | ≈ 3.9354 | 3 |
| 6 | 4 | `3, 24, 146, 790, 4010, 19549, 92691, …` | `x⁴(3 − x²)` | 6 | ≈ 4.1819 | 3 |
| 7 | 4 | `1, 12, 87, 528, 2926, 15366, 77889, …` | `x⁴(1 + 3x − x³)` | 7 | ≈ 4.3539 | 3 |
| 8 | 5 | `4, 41, 296, 1832, 10437, 56500, 295570, …` | `x⁵(4 + x − 2x²)` | 7 | ≈ 4.4774 | 3 |
| 9 | 5 | `1, 17, 151, 1062, 6610, 38264, 211317, …` | `x⁵(1 + 6x − 4x³)` | 8 | ≈ 4.5690 | 5 |
| 10 | 6 | `5, 64, 540, 3773, 23711, 139413, 783755, …` | `x⁶(5 − x − 2x²)` | 9 | ≈ 4.6386 | 4 |
| 11 | 6 | `1, 23, 245, 1971, 13647, 86231, 512846, …` | `x⁶(1 + 9x − 8x² − x³ + x⁴)` | 10 | ≈ 4.6928 | 6 |
| 12 | 7 | `6, 94, 916, 7169, 49432, 314167, 1887871, …` | `x⁷(3 − x)(1 + x)(2 + 2x − 2x² − x³)` | 12 | ≈ 4.7357 | 6 |

#### m = 3

| `h` | `w_min` | `smooth_3(w, h)`, `w = w_min, …` | numerator | den. degree | growth | degree |
|---|---|---|---|---|---|---|
| 5 | 3 | `3, 24, 153, 876, 4731, 24624, 124977, …` | `3x³` | 3 | `2 + √7 ≈ 4.6458` | 2 |
| 6 | 3 | `2, 19, 139, 905, 5532, 32496, 185756, …` | `x³(2 + x)` | 5 | ≈ 5.1190 | 3 |
| 7 | 3 | `1, 13, 109, 792, 5335, 34323, 214097, …` | `x³(1 + 3x − x³)` | 7 | ≈ 5.4751 | 4 |
| 8 | 4 | `6, 66, 553, 4127, 28906, 194484, 1272728, …` | `x⁴(3 − x²)(2 − x²)` | 8 | ≈ 5.7400 | 4 |
| 9 | 4 | `3, 42, 395, 3190, 23802, 169269, 1165637, …` | `x⁴(1 + x − x²)(3 − x²)` | 8 | ≈ 5.9434 | 3 |
| 10 | 4 | `1, 23, 255, 2269, 18125, 136109, 982265, …` | `x⁴(1 + 9x − 8x² − 2x³ + 2x⁴)` | 8 | ≈ 6.1024 | 4 |
| 11 | 5 | `10, 146, 1482, 12854, 102454, 775350, 5667758, …` | `2x⁵(1 + x)(5 − 2x − 4x² + 2x³)` | 9 | ≈ 6.2285 | 5 |
| 12 | 5 | `4, 80, 934, 8842, 74930, 594286, 4513930, …` | `2x⁵(2 + 10x − x² − 16x³ + 6x⁵)` | 10 | ≈ 6.3302 | 5 |

#### m = 4

| `h` | `w_min` | `smooth_4(w, h)`, `w = w_min, …` | numerator | den. degree | growth | degree |
|---|---|---|---|---|---|---|
| 6 | 3 | `4, 40, 316, 2240, 14964, 96280, 603756, …` | `4x³` | 3 | `(5 + √41)/2 ≈ 5.7016` | 2 |
| 7 | 3 | `3, 34, 302, 2395, 17860, 128080, 894147, …` | `x³(3 + x)` | 5 | ≈ 6.2434 | 3 |
| 8 | 3 | `2, 27, 266, 2312, 18782, 146282, 1106995, …` | `x³(2 − x)(1 + x)²` | 7 | ≈ 6.6750 | 4 |
| 9 | 3 | `1, 19, 211, 2004, 17556, 146533, 1184153, …` | `x³(1 + 6x − 5x³ + x⁵)` | 9 | ≈ 7.0211 | 5 |
| 10 | 4 | `10, 140, 1495, 14230, 127152, 1091508, 9113801, …` | `x⁴(2 − x²)(5 − 5x² + x⁴)` | 10 | ≈ 7.2962 | 5 |
| 11 | 4 | `6, 100, 1165, 11786, 110716, 993720, 8648360, …` | `x⁴(2 − x²)(3 + 5x − x² − 5x³ + x⁵)` | 11 | ≈ 7.5194 | 5 |
| 12 | 4 | `3, 66, 858, 9297, 91902, 860600, 7777385, …` | `x⁴(3 + 18x − 30x³ + 14x⁵ − 2x⁷)` | 11 | ≈ 7.7027 | 5 |

The first entry of each row is the binomial of 3.4. The `m = 2`, `h = 4` row and the `m = 2` triangle by `(w, h)` (`1; 1, 1, 1; 1, 3, 5, 2, 1; 1, 7, 19, 12, 8, 3, 1; …`) have no OEIS match (searched 2026-10-06); the other rows have not been searched.

### 3.8 Block parity

For an anchored castle, `blocks(c) = c_1 + Σ max(0, c_{i+1} − c_i) = 1 + (total rise)`, so a rise by `r` adds `r` blocks. The signed count `Σ (−1)^{blocks}` is the transfer-matrix count with each rise by `r` weighted `(−1)^r`; even-block and odd-block counts are (`smooth_m` ± signed)/2.

For `m = 2, 3, 4` and every `h ≤ 12`, the reduced denominator of the signed count has degree exactly `2h − 1`, the full degree of the two determinants. At `m = 1` it does not: the orders there repeat at `h = 5` and `h = 9`. For `m = 2`:[^exec]

| `h` | even-block, `w = w_min, …` | odd-block, `w = w_min, …` | growth of even − odd | order, even − odd | order, even / odd |
|---|---|---|---|---|---|
| 4 | `2, 11, 44, 161, 592, 2209, 8252, …` | `0, 1, 14, 91, 442, 1883, 7550, …` | 2.0200 | 7 | 10 |
| 5 | `0, 0, 7, 68, 421, 2177, 10260, …` | `1, 8, 39, 165, 681, 2819, 11749, …` | 2.3892 | 9 | 14 |
| 6 | `3, 22, 111, 516, 2365, 10759, 48863, …` | `0, 2, 35, 274, 1645, 8790, 43828, …` | 2.3892 | 11 | 17 |
| 7 | `0, 0, 13, 154, 1104, 6566, 35713, …` | `1, 12, 74, 374, 1822, 8800, 42176, …` | 2.5747 | 13 | 20 |
| 8 | `4, 38, 228, 1202, 6178, 31331, 157083, …` | `0, 3, 68, 630, 4259, 25169, 138487, …` | 2.5747 | 15 | 22 |
| 9 | `0, 0, 21, 303, 2492, 16369, 96680, …` | `1, 17, 130, 759, 4118, 21895, 114637, …` | 2.6771 | 17 | 25 |
| 10 | `5, 60, 424, 2505, 14078, 77335, 416900, …` | `0, 4, 116, 1268, 9633, 62078, 366855, …` | 2.6771 | 19 | 28 |
| 11 | `0, 0, 31, 539, 5076, 36808, 234711, …` | `1, 23, 214, 1432, 8571, 49423, 278135, …` | 2.7401 | 21 | 31 |
| 12 | `6, 89, 734, 4840, 29581, 174713, 1004744, …` | `0, 5, 182, 2329, 19851, 139454, 883127, …` | 2.7401 | 23 | 35 |

The first-width castles of 3.4 rise by exactly `h − 1` in total, so they all have `h` blocks: the first entry is even-block for even `h` and odd-block for odd `h`. In every row the signed count grows more slowly than `smooth_2(w, h)`, so each parity class is half of `smooth_2(w, h)` up to a smaller term. The even/odd orders for `m = 3` are `12, 16, 20, 23, 25, 27, 30, 33` and for `m = 4` are `14, 18, 22, 26, 29, 32, 34` (from `h = m + 2` to 12).[^exec]

## Other boundary conditions

**Free first column.** For `(w − 1)·m ≤ h − 1` there are exactly `(2m + 1)^{w−1}` free m-smooth castles of exact height `h`: each of the `(2m + 1)^{w−1}` step sequences spans at most `h − 1` rows, so exactly one vertical position puts its top column at height `h`. At `h ≤ m + 1` the free count is all castles (3.3).

**Both end columns at height 1.** The first such castle has width `2w_min − 1`, and there are `C(slack + w_min − 2, w_min − 2)²` of them. The top must be reached exactly at the middle column, and each half is a first-width climb of 3.4, the second one reflected.

For `m = 2`:[^exec]

| `h` | free first column, `w = 1, 2, …` | first pinned width | both ends at height 1, from that width |
|---|---|---|---|
| 4 | `1, 5, 23, 97, 391, 1529, 5855, 22081, …` | 5 | `4, 28, 144, 648, 2716, …` |
| 5 | `1, 5, 25, 117, 527, 2311, 9939, 42121, …` | 5 | `1, 11, 76, 430, 2184, …` |
| 6 | `1, 5, 25, 123, 587, 2741, 12589, 57079, …` | 7 | `9, 99, 732, 4506, 25006, …` |
| 7 | `1, 5, 25, 125, 615, 2977, 14217, 67153, …` | 7 | `1, 19, 198, 1554, 10383, …` |
| 8 | `1, 5, 25, 125, 623, 3075, 15029, 72807, …` | 9 | `16, 248, 2409, 18683, 126728, …` |
| 9 | `1, 5, 25, 125, 625, 3113, 15413, 75831, …` | 9 | `1, 29, 421, 4303, 35839, …` |
| 10 | `1, 5, 25, 125, 625, 3123, 15561, 77237, …` | 11 | `25, 515, 6296, 59370, 477404, …` |
| 11 | `1, 5, 25, 125, 625, 3125, 15611, 77833, …` | 11 | `1, 41, 789, 10117, 101925, …` |
| 12 | `1, 5, 25, 125, 625, 3125, 15623, 78045, …` | 13 | `36, 948, 14188, 159096, 1488832, …` |

## Computation

```python
from math import ceil, comb
def smooth_m(W, h, m):
    """(even, odd) anchored m-smooth castles of exact height h, widths 1..W.
    DP over (last height, block parity, reached h); a rise by r adds r blocks."""
    dp, out = {(1, 1, h == 1): 1}, []
    for w in range(1, W + 1):
        if w > 1:
            nd = {}
            for (a, p, r), v in dp.items():
                for b in range(max(1, a - m), min(h, a + m) + 1):
                    key = (b, (p + max(0, b - a)) % 2, r or b == h)
                    nd[key] = nd.get(key, 0) + v
            dp = nd
        out.append(tuple(sum(v for (a, p, r), v in dp.items() if r and p == q) for q in (0, 1)))
    return out
for m in (1, 2, 3, 4):
    for h in range(2, 13):
        c = [e + o for e, o in smooth_m(30, h, m)]
        w0 = ceil((h - 1) / m) + 1
        slack = (w0 - 1) * m - (h - 1)
        assert all(v == 0 for v in c[:w0 - 1]) and c[w0 - 1] == comb(slack + w0 - 2, w0 - 2)
print([e + o for e, o in smooth_m(10, 4, 2)])    # 0, 0, 2, 12, 58, 252, 1034, 4092, 15802, 59964
```

## Addendum: what does not extend

The definition, the subtraction `strips_m(w, h) − strips_m(w, h − 1)`, the reflection bounds on the denominators, the first width and its count, the growth bounds, the Pell structure on the diagonal `h = m + 2`, and the parity split as a computation extend to every `m`. The following parts of [[1-smooth-castles](pages/1-smooth-castles.md)] do not.

- **The monomial numerator.** At `m = 1` the exact-height generating function is `x^h` over the denominators. For `m ≥ 2` the numerator starts at `x^{w_min}` with `w_min < h` and is in general a polynomial of several terms, even when `slack = 0` (`x³(1 + x)` at `m = 2`, `h = 5`).
- **Exact degrees.** At `m = 1` the strip denominator has degree exactly `⌈h/2⌉` and the exact-height denominator exactly `h`. For `m ≥ 2` these are only upper bounds (3.2).
- **Explicit eigenvalues and Chebyshev identities.** The cosine formula `1 + 2cos(πk/(h+1))`, the three-term determinant recurrence, and the formulas for `η_h` in terms of the determinants all use the tridiagonal structure. The band matrices for `m ≥ 2` have none of them, and their growth constants are cubic or higher for `h ≥ m + 3` in every case computed. In their place, the [[kernel-method](pages/kernel-method.md)] writes the strips through the `2m` roots of the kernel `1 − x(u^{−m} + ⋯ + u^m)` ([[banderier-nicodeme-2010-bounded-discrete-walks](pages/banderier-nicodeme-2010-bounded-discrete-walks.md)]).
- **The Motzkin readings.** At `m = 1` the castle counts are columns of the Motzkin triangles A283595 and A097862. The `m = 2` triangle has no OEIS match (3.7).
- **Irregular parity orders.** The repeats at `h = 5` and `h = 9` in the `m = 1` signed orders do not occur for `m = 2, 3, 4`, where the order is `2h − 1` for every `h ≤ 12` (3.8).

## Related Concepts

- [[1-smooth-castles](pages/1-smooth-castles.md)] - the case `m = 1`, where this page starts.
- [[kernel-method](pages/kernel-method.md)] - the strips of this page between two walls, in closed form in the `2m` kernel roots ([[banderier-nicodeme-2010-bounded-discrete-walks](pages/banderier-nicodeme-2010-bounded-discrete-walks.md)]).
- [[pell-castle](pages/pell-castle.md)] - `m = 1`, `h = 3`, the first point of the diagonal `h = m + 2`.
- [[pell-castle-strip](pages/pell-castle-strip.md)] - the two-atom reading of `1/(1 − 2x − x²)`, which the diagonal `h = m + 2` carries to every `m`.
- [[castle-classification-shape](pages/castle-classification-shape.md)] - Axis 2, the m-smooth type.
- [[castle-counting-formula](pages/castle-counting-formula.md)] - `F(w, h)`, the even-block count at `m ≥ h − 1`.
- [[castle-strip](pages/castle-strip.md)] - how a neighbour rule becomes a transfer matrix on column heights.
- [[metallic-means](pages/metallic-means.md)] - why the diagonal is metallic only at `m = 1`.
- [[castle-sequence-catalogue](pages/castle-sequence-catalogue.md)] - the status of each row.
- [[castle-notation](pages/castle-notation.md)] - `strips_m`, `smooth_m`, `w_min`, `ρ_{h,m}`.

## Footnotes

[^a007482]: https://oeis.org/A007482 (fetched 2026-10-06) - "a(n) is the number of subsequences of [ 1, ..., 2n ] in which each odd number has an even neighbor."; "G.f.: 1/(1-3*x-2*x^2)."; data `1, 3, 11, 39, 139, 495, 1763, 6279, 22363, 79647, …`, offset 0.
[^a015530]: https://oeis.org/A015530 (fetched 2026-10-06) - "Expansion of x/(1 - 4*x - 3*x^2)."; offset 0.
[^a015537]: https://oeis.org/A015537 (fetched 2026-10-06) - "Expansion of x/(1 - 5*x - 4*x^2)."; offset 0.
[^exec]: Verified by execution (Python 3, SymPy, NumPy, 2026-10-06) for `m = 1, 2, 3, 4` and `h = 2, …, 12`: counts by dynamic program over (height, block parity, reached `h`) to width `8h + 12`, against brute-force enumeration for `h ≤ 7`, `m ≤ 3`, `w ≤ 7`, and against `strips_m(w, h) − strips_m(w, h − 1)`; generating functions recovered from the counts by Berlekamp-Massey, each checked to reproduce all computed terms with a recurrence order below half their number; the `m = 1` results agree with [[1-smooth-castles](pages/1-smooth-castles.md)]. Checked: `w_min` and the binomial count at `w_min`; the pinned first width `2w_min − 1` with the squared binomial; the strip denominator degree `≤ ⌈h/2⌉` and the exact-height degree `≤ h`; the growth bounds against the largest eigenvalue; for `h ≤ m + 1`, the counts `h^{w−1} − (h−1)^{w−1}` and `h^w − (h−1)^w` and the anchored even-block count equal to the free even-block count at width `w − 1`; at `h = m + 2`, both diagonal generating functions and the minimal polynomial `x² − (m+1)x − m`; the free count `(2m + 1)^{w−1}` for `(w − 1)m ≤ h − 1`; the signed denominator degree `2h − 1` for `m ≥ 2`; minimal polynomials of the growth constants from the factored characteristic polynomial. OEIS searches with no match (2026-10-06): the `m = 2`, `h = 4` row and the `m = 2` triangle by `(w, h)`.
