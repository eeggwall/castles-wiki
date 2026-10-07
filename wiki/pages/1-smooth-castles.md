---
title: 1-smooth castles
category: Concepts
summary: A 1-smooth castle is a castle whose neighbouring columns differ in height by at most 1. Starting from the Pell castles (first column at height 1, exact height 3), the anchored 1-smooth castles of exact height h are counted for every h; this page gives h = 2 to 12. The count is strips(w, h) − strips(w, h − 1), the anchored strips with ceiling h minus those with ceiling h − 1, and its width generating function is x^h/(η_h(x)·η_{h−1}(x)) for every h, where η_h(x) = Π(1 − λ_k x) over odd k ≤ h, λ_k = 1 + 2cos(πk/(h+1)); so the count satisfies a recurrence of order exactly h and grows like 1 + 2cos(π/(h+1)), climbing 2, 1+√2, φ², 1+√3, … to 3. The counts are column h − 1 of A283595 (Motzkin prefixes by height); pinning both end columns gives x^{2h−1}/(χ_h·χ_{h−1}) and column h − 1 of A097862. What does not extend past small h - Pell and Fibonacci closed forms, quadratic and metallic growth constants, the two-atom reading of 1/(1 − 2x − x²), a uniform parity recurrence - is collected in an addendum.
tags: [concept, castle, castle-type, 1-smooth, pell, transfer-matrix, chebyshev, exact-height, parity, motzkin, generating-functions, oeis]
sources: [pe502-pell-castle-strip]
created: 2026-10-06
updated: 2026-10-06
---

# 1-smooth castles

## Definition

A castle is a skyline `(c_1, …, c_w)` of columns standing on a full bottom row, with maximum height exactly `h` ([[castle-polyomino](pages/castle-polyomino.md)]). A **1-smooth castle** is a castle whose neighbouring columns differ in height by at most 1 (the m-smooth type at `m = 1`, [[castle-classification-shape](pages/castle-classification-shape.md)] Axis 2). An **anchored** 1-smooth castle also has its first column at height 1:

```
c_1 = 1,      |c_{i+1} − c_i| ≤ 1  (1 ≤ i < w),      max_i c_i = h.
```

- **Construction rule.** Start at height 1; at each step move up one, down one, or stay, never leaving `{1, …, h}`; and reach height `h` at least once.
- **Examples.** At `h = 4`, the five anchored 1-smooth castles of width 5 are `(1, 1, 2, 3, 4)`, `(1, 2, 2, 3, 4)`, `(1, 2, 3, 3, 4)`, `(1, 2, 3, 4, 3)`, `(1, 2, 3, 4, 4)`.
- **Non-examples.** `(1, 2, 3, 3)` is not a castle of height 4 (it never reaches 4); `(1, 2, 4, 3)` rises by 2 in one step.

The Pell castles are the anchored 1-smooth castles of exact height 3 ([[pell-castle](pages/pell-castle.md)]). This page starts from them and follows the anchored castles to every `h`; the free and the both-ends-pinned boundary conditions are in [Other boundary conditions](#other-boundary-conditions).

**Counts.** For width `w` and ceiling `h`:

- `strips(w, h)` is the number of anchored 1-smooth skylines of width `w` with every column in `{1, …, h}`. They need not reach `h`: these are the anchored strips of the Motzkin strip of height `h` ([[motzkin-castles](pages/motzkin-castles.md)] §4).
- `smooth(w, h)` is the number of anchored 1-smooth castles of width `w` and exact height `h`.

A strip with ceiling `h` either reaches `h` or stays in `{1, …, h − 1}`, so

```
smooth(w, h)  =  strips(w, h) − strips(w, h − 1).
```

## 1. The starting point: Pell castles (h = 3)

At `h = 3` the pieces are:[^exec]

- **Transfer matrix.** The column heights are the states, and the 1-smooth rule is the `3 × 3` matrix `I + A_path` with ones on the diagonal and both off-diagonals ([[castle-strip](pages/castle-strip.md)]). Its characteristic polynomial is `(x − 1)(x² − 2x − 1)`.
- **Strips.** Anchored at height 1, the `(1 − x)` factor cancels and `Σ_w strips(w, 3) x^w = x/(1 − 2x − x²)`, so `strips(w, 3) = P⋆_w`, the Pell numbers (A000129, [[pell-numbers](pages/pell-numbers.md)]).
- **Subtraction.** The strips that never reach 3 stay on `{1, 2}`, where every column after the first is free: `strips(w, 2) = 2^{w−1}`. So `smooth(w, 3) = P⋆_w − 2^{w−1}`.
- **Generating function.** `Σ_w smooth(w, 3) x^w = x³/((1 − 2x − x²)(1 − 2x))`.
- **Growth.** `1 + √2`, the silver ratio.
- **Parity.** Split by PE 502's block parity, the even-block and odd-block rows satisfy a recurrence of order 8 and their difference one of order 5.

Sections 2 and 3 carry each item to higher `h`; the addendum lists what does not carry over.

## 2. h = 4

Raising the ceiling to 4 changes each item:[^exec]

| | `h = 3` (Pell castles) | `h = 4` |
|---|---|---|
| transfer matrix | `3 × 3` band of ones | `4 × 4` band of ones |
| characteristic polynomial | `(x − 1)(x² − 2x − 1)` | `(x² − 3x + 1)(x² − x − 1)` |
| `Σ_w strips(w, h) x^w` | `x/(1 − 2x − x²)`: `1, 2, 5, 12, 29, …` `= P⋆_w` | `x(1 − x)/(1 − 3x + x²)`: `1, 2, 5, 13, 34, 89, …` `= F_{2w−1}`, A001519(`w`)[^a001519] |
| strips that never reach `h` | `strips(w, 2) = 2^{w−1}` | `strips(w, 3) = P⋆_w` |
| `smooth(w, h)` | `P⋆_w − 2^{w−1}` = `0, 0, 1, 4, 13, 38, …` | `F_{2w−1} − P⋆_w` = `0, 0, 0, 1, 5, 19, 64, 202, 612, …` |
| `Σ_w smooth(w, h) x^w` | `x³/((1 − 2x − x²)(1 − 2x))` | `x⁴/((1 − 3x + x²)(1 − 2x − x²))` |
| growth | `1 + √2` | `φ² = (3 + √5)/2 ≈ 2.618` |

Here `F_n` are the Fibonacci numbers with `F_1 = F_2 = 1`. At `h = 4` the Pell numbers appear only as the subtracted term.

## 3. Every h

### 3.1 The transfer matrix and its determinant

The 1-smooth rule on heights `{1, …, h}` is the `h × h` matrix `I + A_path`. Let

```
χ_h(x)  =  det(I − x(I + A_path)),        χ_0 = 1,   χ_1 = 1 − x,   χ_h = (1 − x)·χ_{h−1} − x²·χ_{h−2}.
```

The recurrence is the cofactor expansion of a tridiagonal determinant along its last row. Expanding the first row of `(I − x(I + A_path))^{−1}` by cofactors gives the strip generating function for any `h`:[^exec]

```
Σ_w strips(w, h) x^w  =  x · Σ_{j=1}^{h} x^{j−1} χ_{h−j}(x)  /  χ_h(x).
```

### 3.2 Which eigenvalues survive

`I + A_path` has eigenvalues and eigenvectors

```
λ_k  =  1 + 2cos θ_k,      θ_k = πk/(h+1),      v_k(j) = sin(j θ_k)      (k, j = 1, …, h).
```

The strip count is `e_1ᵀ(I + A_path)^{w−1}𝟙`, so eigenvalue `λ_k` contributes in proportion to `v_k(1) · Σ_j v_k(j)`. The sum `Σ_j sin(jθ_k)` is 0 when `k` is even, and `cot(θ_k/2)` when `k` is odd. So only odd `k` contribute, and

```
strips(w, h)  =  (2/(h+1)) · Σ_{k odd, k ≤ h} (1 + cos θ_k) · λ_k^{w−1}.
```

Every odd-`k` coefficient `1 + cos θ_k` is positive. The odd-`k` eigenvalues are distinct and nonzero: `λ_k = 0` only at `θ_k = 2π/3`, that is `k = 2(h+1)/3`, which is even. So the reduced denominator of the strip generating function is

```
η_h(x)  =  Π_{k odd, k ≤ h} (1 − λ_k x),        degree ⌈h/2⌉,        η_0 = 1.
```

At `h = 3` the dropped factor is `k = 2`, `λ_2 = 1`: the `(1 − x)` that cancels on [[pell-castle-strip](pages/pell-castle-strip.md)].[^exec]

| `h` | `η_h(x)` | `h` | `η_h(x)` |
|---|---|---|---|
| 1 | `1 − x` | 7 | `1 − 4x + 2x² + 4x³ − x⁴` |
| 2 | `1 − 2x` | 8 | `(1 − 2x)(1 − 3x + x³)` |
| 3 | `1 − 2x − x²` | 9 | `(1 − x)(1 − 4x + x² + 6x³ + x⁴)` |
| 4 | `1 − 3x + x²` | 10 | `1 − 6x + 10x² − x³ − 6x⁴ + x⁵` |
| 5 | `(1 − x)(1 − 2x − 2x²)` | 11 | `(1 − 2x − x²)(1 − 4x + 2x² + 4x³ − 2x⁴)` |
| 6 | `1 − 4x + 3x² + x³` | 12 | `1 − 7x + 15x² − 6x³ − 11x⁴ + 6x⁵ + x⁶` |

**Without trigonometry.** Each `η_h` is a combination of two determinants:

```
η_{2m}(x)  =  χ_m(x) − x·χ_{m−1}(x),        η_{2m+1}(x)  =  χ_{m+1}(x) − x²·χ_{m−1}(x)        (χ_{−1} = 0).
```

With `χ_h(x) = x^h U_h((1 − x)/(2x))`, where `U_h` are the Chebyshev polynomials of the second kind, these come from the factorizations of `U_{2m+1}` and `U_{2m}`:

```
χ_{2m+1}  =  χ_m · (χ_{m+1} − x²χ_{m−1}),        χ_{2m}  =  (χ_m − xχ_{m−1}) · (χ_m + xχ_{m−1}).
```

At `h = 2m + 1` the even-`k` angles `θ_{2j} = πj/(m+1)` are the angles of `χ_m`, so `χ_m` is the factor that cancels. At `h = 2m` the factor `χ_m − xχ_{m−1}` is the one whose zeros sit at the odd angles `θ = (2j − 1)π/(2m + 1)`. For example, `η_4 = χ_2 − xχ_1 = (1 − 2x) − x(1 − x) = 1 − 3x + x²`.[^exec]

### 3.3 The exact-height generating function

**Proposition.** For every `h ≥ 1`,

```
Σ_w smooth(w, h) x^w  =  x^h / (η_h(x) · η_{h−1}(x)).
```

*Proof.* By 3.2, `Σ_w strips(w, h) x^w = x·N_h(x)/η_h(x)` with `deg N_h < deg η_h`, a sum of terms `c_k x/(1 − λ_k x)`. The eigenvalues of `η_h` and `η_{h−1}` are disjoint, since `cos(πk/(h+1)) = cos(πj/h)` would need `k/(h+1) = j/h`. Subtracting the `h − 1` series gives `x(N_h η_{h−1} − N_{h−1} η_h)/(η_h η_{h−1})`, whose numerator has degree at most `h`. Reaching height `h` from height 1 takes `h − 1` rises, so `smooth(w, h) = 0` for `w < h` and the numerator is divisible by `x^h`. At `w = h` the only castle is the staircase `(1, 2, …, h)`, so the coefficient is 1. ∎

At `h = 3` this gives `x³/((1 − 2x − x²)(1 − 2x))`, the Pell castle generating function. In general:[^exec]

- **Recurrence.** The denominator has degree `⌈h/2⌉ + ⌈(h−1)/2⌉ = h` and the numerator is a monomial, so `smooth(·, h)` satisfies a linear recurrence of order exactly `h`.
- **Smallest widths.** `smooth(h, h) = 1` (the staircase) and, for `h ≥ 2`, `smooth(h + 1, h) = h + 1`: the one step that is not a rise is a flat step in any of `h` places, or a final step down.
- **Explicit form.** `smooth(w, h) = strips(w, h) − strips(w, h − 1)`, each term given by the cosine sum of 3.2.

### 3.4 Growth

The largest eigenvalue is `λ_1 = 1 + 2cos(π/(h+1))`, and the subtracted `strips(w, h − 1)` grows at the smaller rate `1 + 2cos(π/h)`. So, for each fixed `h`,

```
smooth(w, h)  ~  (2/(h+1)) · (1 + cos(π/(h+1))) · (1 + 2cos(π/(h+1)))^{w−1}        (w → ∞),
```

and the fraction of anchored strips that reach their ceiling tends to 1. The growth constants climb `2, 1 + √2, φ², 1 + √3, …` toward 3. This is the ladder of [[motzkin-castles](pages/motzkin-castles.md)] §4: the same matrix with both end columns pinned at height 1. The boundary condition changes which eigenvalues appear, not the largest one.

### 3.5 Table, h = 2 to 12

| `h` | `strips(w, h)`, `w = 1, 2, …` | OEIS | `smooth(w, h)`, `w = h, h+1, …` | growth `1 + 2cos(π/(h+1))` | degree |
|---|---|---|---|---|---|
| 2 | `1, 2, 4, 8, 16, 32, 64, 128, 256, 512, …` | `2^{w−1}` | `1, 3, 7, 15, 31, 63, 127, 255, …` | `2` | 1 |
| 3 | `1, 2, 5, 12, 29, 70, 169, 408, 985, 2378, …` | A000129 (Pell) | `1, 4, 13, 38, 105, 280, 729, 1866, …` | `1 + √2 ≈ 2.4142` | 2 |
| 4 | `1, 2, 5, 13, 34, 89, 233, 610, 1597, 4181, …` | A001519 (`F_{2w−1}`) | `1, 5, 19, 64, 202, 612, 1803, 5205, …` | `φ² ≈ 2.6180` | 2 |
| 5 | `1, 2, 5, 13, 35, 95, 259, 707, 1931, 5275, …` | A057960(`w − 1`) | `1, 6, 26, 97, 334, 1094, 3465, 10714, …` | `1 + √3 ≈ 2.7321` | 2 |
| 6 | `1, 2, 5, 13, 35, 96, 266, 741, 2070, 5791, …` | A085810(`w`) | `1, 7, 34, 139, 516, 1802, 6038, 19643, …` | `1 + 2cos(π/7) ≈ 2.8019` | 3 |
| 7 | `1, 2, 5, 13, 35, 96, 267, 749, 2113, 5982, …` | no match | `1, 8, 43, 191, 760, 2816, 9933, 33812, …` | `1 + √(2 + √2) ≈ 2.8478` | 4 |
| 8 | `1, 2, 5, 13, 35, 96, 267, 750, 2122, 6035, …` | no match | `1, 9, 53, 254, 1078, 4223, 15639, 55575, …` | `1 + 2cos(π/9) ≈ 2.8794` | 3 |
| 9 | `1, 2, 5, 13, 35, 96, 267, 750, 2123, 6045, …` | no match | `1, 10, 64, 329, 1483, 6123, 23751, 87957, …` | `1 + 2cos(π/10) ≈ 2.9021` | 4 |
| 10 | `1, 2, 5, 13, 35, 96, 267, 750, 2123, 6046, 17302, …` | - | `1, 11, 76, 417, 1989, 8631, 34993, 134828, …` | `1 + 2cos(π/11) ≈ 2.9190` | 5 |
| 11 | `1, 2, 5, 13, 35, 96, 267, 750, 2123, 6046, 17303, 49720, …` | - | `1, 12, 89, 519, 2611, 11878, 50236, 201076, …` | `1 + (√6 + √2)/2 ≈ 2.9319` | 4 |
| 12 | `1, 2, 5, 13, 35, 96, 267, 750, 2123, 6046, 17303, 49721, 143364, …` | - | `1, 13, 103, 636, 3365, 16012, 70516, 292791, …` | `1 + 2cos(π/13) ≈ 2.9419` | 6 |

"Degree" is the degree of the growth constant as an algebraic number, half of Euler's totient of `2h + 2`. "No match" means an oeis.org search of at least the first ten terms on 2026-10-06 returned nothing; "-" means not searched.[^exec]

- **The strip rows.** An anchored skyline of width `w` cannot rise above height `w`, so the ceiling matters only from `w = h + 1` on, and for `w ≤ h` the strip row equals the anchored 1-smooth count with no ceiling, A005773(`w`).[^a005773] The `h = 5` row is A057960, base-5 digit strings that start with 0 and whose adjacent digits differ by at most 1;[^a057960] the `h = 6` row is A085810, three-choice paths in a corridor of height 5.[^a085810]
- **The castle rows.** Every `smooth` row is a column of one OEIS triangle: `smooth(w, h)` is A283595 at row `w − 1`, column `h − 1`, the number of Motzkin prefixes of length `w − 1` and height `h − 1`. The entry gives no generating function.[^a283595] At `h = 3` the row is also A094706(`w − 2`) ([[pell-castle](pages/pell-castle.md)]).

### 3.6 Block parity

PE 502 counts castles by the parity of their block count. For an anchored 1-smooth castle, `blocks(c) = c_1 + Σ max(0, c_{i+1} − c_i) = 1 + (number of rises)`. So the signed count `Σ (−1)^{blocks}` is the transfer-matrix count with each rise weighted by `−1`, and the eigenvalues become `1 + 2i·cos θ_k` ([[motzkin-castles](pages/motzkin-castles.md)] §3). Even-block and odd-block counts are (`smooth` ± signed)/2.

At `w = h` and, for `h ≥ 2`, `w = h + 1`, every anchored 1-smooth castle of exact height `h` has `h − 1` rises and so `h` blocks. The first entries are all even-block for even `h` and all odd-block for odd `h`.[^exec]

| `h` | even-block, `w = h, h+1, …` | odd-block, `w = h, h+1, …` | even − odd, `w = h, h+1, …` | growth of even − odd | order, even − odd | order, even / odd |
|---|---|---|---|---|---|---|
| 2 | `1, 3, 6, 10, 16, 28, 56, 120, …` | `0, 0, 1, 5, 15, 35, 71, 135, …` | `1, 3, 5, 5, 1, −7, −15, −15, …` | 1.4142 | 3 | 3 / 4 |
| 3 | `0, 0, 2, 13, 51, 154, 400, 969, …` | `1, 4, 11, 25, 54, 126, 329, 897, …` | `−1, −4, −9, −12, −3, 28, 71, 72, …` | 1.7321 | 5 | 8 |
| 4 | `1, 5, 16, 42, 106, 287, 843, 2535, …` | `0, 0, 3, 22, 96, 325, 960, 2670, …` | `1, 5, 13, 20, 10, −38, −117, −135, …` | 1.9021 | 7 | 11 |
| 5 | `0, 0, 4, 33, 158, 577, 1827, 5456, …` | `1, 6, 22, 64, 176, 517, 1638, 5258, …` | `−1, −6, −18, −31, −18, 60, 189, 198, …` | 1.9021 | 7 | 11 |
| 6 | `1, 7, 29, 93, 275, 854, 2850, 9636, …` | `0, 0, 5, 46, 241, 948, 3188, 10007, …` | `1, 7, 24, 47, 34, −94, −338, −371, …` | 2.0608 | 9 | 14 |
| 7 | `0, 0, 6, 61, 348, 1472, 5256, 17301, …` | `1, 8, 37, 130, 412, 1344, 4677, 16511, …` | `−1, −8, −31, −69, −64, 128, 579, 790, …` | 2.1010 | 11 | 18 |
| 8 | `1, 9, 46, 176, 596, 2037, 7360, 27003, …` | `0, 0, 7, 78, 482, 2186, 8279, 28572, …` | `1, 9, 39, 98, 114, −149, −919, −1569, …` | 2.1289 | 13 | 21 |
| 9 | `0, 0, 8, 97, 646, 3131, 12556, 45407, …` | `1, 10, 56, 232, 837, 2992, 11195, 42550, …` | `−1, −10, −48, −135, −191, 139, 1361, 2857, …` | 2.1289 | 13 | 21 |
| 10 | `1, 11, 67, 299, 1146, 4279, 16550, 64998, …` | `0, 0, 9, 118, 843, 4352, 18443, 69830, …` | `1, 11, 58, 181, 303, −73, −1893, −4832, …` | 2.1639 | 15 | 24 |
| 11 | `0, 0, 10, 141, 1076, 5898, 26358, 104378, …` | `1, 12, 79, 378, 1535, 5980, 23878, 96698, …` | `−1, −12, −69, −237, −459, −82, 2480, 7680, …` | 2.1753 | 17 | 28 |
| 12 | `1, 13, 92, 470, 2017, 8190, 33730, 140609, …` | `0, 0, 11, 166, 1348, 7822, 36786, 152182, …` | `1, 13, 81, 304, 669, 368, −3056, −11573, …` | 2.1842 | 19 | 31 |

The orders are the degrees of the reduced denominators, from the weighted transfer matrix; at `h = 2` the even-block row has order 3 and the odd-block row order 4. For every `h ≤ 12` the signed count grows more slowly than `smooth(w, h)`, so each parity class is half of `smooth(w, h)` up to a smaller term. The signed growth rate is `√(1 + 4cos²(π/(h+1)))` for every `h ≤ 12` except `h = 5` and `h = 9`, where that eigenvalue cancels and the rate equals the one at `h − 1`. The `h = 4` even-block and odd-block rows have no OEIS match (searched 2026-10-06); the rows for `h ≥ 5` have not been searched.[^exec]

## Other boundary conditions

The same matrix with other end conditions gives the other two 1-smooth families of exact height `h`. Both have the growth `1 + 2cos(π/(h+1))` of 3.4.[^exec]

**Both end columns at height 1.** The strip generating function is `x·χ_{h−1}/χ_h`, a corner cofactor. The determinants satisfy `χ_{h−1}² − χ_h χ_{h−2} = x^{2(h−1)}`: substituting the recurrence shows the left side is `x²` times its value at `h − 1`, and it equals 1 at `h = 1`. So for every `h ≥ 1` (with `χ_{−1} = 0`),

```
Σ_w #{1-smooth castles of exact height h with c_1 = c_w = 1} x^w  =  x^{2h−1} / (χ_h(x) · χ_{h−1}(x)),
```

of order `2h − 1`. No eigenvalue cancels here, since `v_k(1) = sin θ_k ≠ 0`. The first such castle has width `2h − 1`, `(1, 2, …, h, …, 2, 1)`. Subtracting 1 from every column gives a Motzkin path of length `w − 1` and height `h − 1`, so the count is A097862 at row `w − 1`, column `h − 1`. The entry states this column generating function, `z^{2k}/(P_k P_{k+1})` with its `P_k` equal to `χ_k`, by path length instead of width;[^a097862] [[castle-classification-shape](pages/castle-classification-shape.md)] Axis 3 tabulates it by `(w, h)` for `w ≤ 9`. At `h = 3` this is the row `0, 0, 0, 0, 1, 5, 18, 56, …` on [[pell-castle](pages/pell-castle.md)].

**Free first column.** Only odd `k` contribute, because `𝟙` is orthogonal to the even-`k` eigenvectors on both sides, and the reduced denominator is again `η_h η_{h−1}` (checked for `h ≤ 12`), but the numerator is not a monomial. At `h = 3` it is `x(1 − x)`. The count of skylines is `(2/(h+1)) Σ_{k odd} cot²(θ_k/2) λ_k^{w−1}`. For `w ≤ h` there are exactly `3^{w−1}` free 1-smooth castles of exact height `h`. Each of the `3^{w−1}` step sequences spans at most `w − 1 ≤ h − 1` rows, so it has exactly one vertical position that puts its top column at height `h`.

| `h` | free first column, `w = h+1, h+2, …` | both ends at height 1, `w = 2h−1, 2h, …` |
|---|---|---|
| 2 | `7, 15, 31, 63, 127, …` | `1, 3, 7, 15, 31, 63, …` |
| 3 | `25, 67, 175, 449, 1137, …` | `1, 5, 18, 56, 161, 441, …` |
| 4 | `79, 227, 643, 1801, 4999, …` | `1, 7, 33, 129, 453, 1485, …` |
| 5 | `241, 711, 2081, 6049, 17479, …` | `1, 9, 52, 242, 990, 3718, …` |
| 6 | `727, 2167, 6433, 19021, 56031, …` | `1, 11, 75, 403, 1872, 7878, …` |
| 7 | `2185, 6539, 19531, 58211, 173113, …` | `1, 13, 102, 620, 3215, 14943, …` |
| 8 | `6559, 19659, 58871, 176105, 526159, …` | `1, 15, 133, 901, 5151, 26163, …` |
| 9 | `19681, 59023, 176941, 530165, 1587529, …` | `1, 17, 168, 1254, 7828, 43092, …` |
| 10 | `59047, 177119, 531205, 1592781, 4774365, …` | `1, 19, 207, 1687, 11410, 67620, …` |
| 11 | `177145, 531411, 1594055, 4781127, 14338159, …` | `1, 21, 250, 2208, 16077, 102005, …` |
| 12 | `531439, 1594291, 4782667, 14346729, 43033457, …` | `1, 23, 297, 2825, 22025, 148905, …` |

The free row at `h = 3` is A106514(`w − 1`) ([[pell-castle](pages/pell-castle.md)]). The `h = 4` free row `1, 3, 9, 27, 79, 227, 643, 1801, 4999` has no OEIS match (searched 2026-10-06).

## Computation

```python
from math import cos, pi
def smooth(W, h):
    """(even, odd) anchored 1-smooth castles of exact height h, widths 1..W.
    DP over (last height, block parity, reached h); blocks = 1 + number of rises."""
    dp, out = {(1, 1, h == 1): 1}, []
    for w in range(1, W + 1):
        if w > 1:
            nd = {}
            for (a, p, r), v in dp.items():
                for b in (a - 1, a, a + 1):
                    if 1 <= b <= h:
                        key = (b, (p + max(0, b - a)) % 2, r or b == h)
                        nd[key] = nd.get(key, 0) + v
            dp = nd
        out.append(tuple(sum(v for (a, p, r), v in dp.items() if r and p == q) for q in (0, 1)))
    return out
def strips(w, h):
    return 0 if h == 0 else round(2 / (h + 1) * sum((1 + cos(pi * k / (h + 1))) * (1 + 2 * cos(pi * k / (h + 1))) ** (w - 1)
                                                     for k in range(1, h + 1, 2)))
for h in range(1, 13):
    c = smooth(20, h)
    assert all(e + o == strips(w, h) - strips(w, h - 1) for w, (e, o) in enumerate(c, start=1))
print([e + o for e, o in smooth(12, 4)])    # 0, 0, 0, 1, 5, 19, 64, 202, 612, 1803, 5205, 14797
```

## Addendum: what does not extend

The definition, the subtraction `strips(w, h) − strips(w, h − 1)`, the transfer matrix, the exact-height generating function and its monomial numerator, the growth ladder, and the parity split as a computation extend to every `h`. The following do not.

- **Named integer sequences.** The strip rows are Pell at `h = 3` and odd-indexed Fibonacci at `h = 4`. At `h = 5` and `6` they are corridor-path entries with no castle reading (A057960, A085810), and at `h = 7, 8, 9` they have no OEIS match. The castle rows exist in the OEIS only as columns of A283595, and at `h = 3` as A094706.
- **Quadratic growth constants.** `1 + 2cos(π/(h+1))` has degree equal to half of Euler's totient of `2h + 2`, which is at most 2 only for `h ≤ 5`. From `h = 6` on the growth constants are cubic, quartic, quintic and sextic (table 3.5).
- **Metallic labels.** Among `h ≥ 2`, only `h = 3` grows at a metallic mean, a root of `x² − ax − 1` ([[metallic-means](pages/metallic-means.md)]). `φ²` (`h = 4`, root of `x² − 3x + 1`) and `1 + √3` (`h = 5`, root of `x² − 2x − 2`) are quadratic but not metallic. So "silver width growth castle" ([[castle-classification-growth](pages/castle-classification-growth.md)]) has no metallic counterpart at other heights. Silver at `h = 3` comes from the 1-smooth rule. The ridge rule reaches the metallic means at every height ([[metallic-strip-realizability](pages/metallic-strip-realizability.md)]).
- **The two-atom reading.** The Analytic Combinatorics exercise of [[pell-castle-strip](pages/pell-castle-strip.md)] reads `1/(1 − 2x − x²)` as sequences of a width-1 atom of weight 2 and a width-2 atom of weight 1. That reading needs a denominator `1 − (2x + x²)` and belongs to `h = 3`. Writing `Σ_w strips(w, h) x^{w−1} = 1/(1 − a_h(x))`, the series `a_h` is `2x + x²` at `h = 3` and `2x + x²/(1 − x)` at `h = 4`. Its first 25 coefficients are nonnegative for every `h ≤ 12`, but its terms have no known combinatorial reading as atoms.
- **A uniform parity recurrence.** At `h = 3` the parity rows have order 8 and the signed row order 5. For `h = 2, …, 12` the signed orders are `3, 5, 7, 7, 9, 11, 13, 13, 15, 17, 19`, with repeats at `h = 5` and `h = 9`. Unlike the order `h` of the unsigned count (3.3), these orders follow no single formula in `h`, and each height is computed separately.

## Related Concepts

- [[pell-castle](pages/pell-castle.md)] - the `h = 3` case, where this page starts.
- [[pell-castle-strip](pages/pell-castle-strip.md)] - the `h = 3` strip and the two-atom reading of `1/(1 − 2x − x²)`.
- [[motzkin-castles](pages/motzkin-castles.md)] - the same matrix with both end columns pinned (§4, the growth ladder) and the signed eigenvalues `1 + 2i·cos θ_k` (§3); anchored at height 1 with no ceiling, the Motzkin prefixes A005773 (§5).
- [[castle-strip](pages/castle-strip.md)] - how a neighbour rule becomes a transfer matrix on column heights.
- [[castle-classification-shape](pages/castle-classification-shape.md)] - Axis 2, the m-smooth type at `m = 1`.
- [[castle-classification-growth](pages/castle-classification-growth.md)] - growth types; the Pell castles are its silver example.
- [[metallic-strip-realizability](pages/metallic-strip-realizability.md)] - the ridge rule, which reaches the metallic means at every height.
- [[pell-numbers](pages/pell-numbers.md)] - `P⋆_w = strips(w, 3)`.
- [[castle-sequence-catalogue](pages/castle-sequence-catalogue.md)] - the status of each row.
- [[castle-notation](pages/castle-notation.md)] - `strips`, `smooth`, `χ_h`, `η_h`, `θ_k`, `λ_k`.

## Footnotes

[^a001519]: https://oeis.org/A001519 (fetched 2026-10-06) - "a(n) = 3*a(n-1) - a(n-2) for n >= 2, with a(0) = a(1) = 1."; comment "This is a bisection of the Fibonacci sequence A000045. a(n) = F(2*n-1)"; "G.f.: (1-2*x)/(1-3*x+x^2)."; data `1, 1, 2, 5, 13, 34, 89, 233, 610, 1597, …`, offset 0.
[^a005773]: https://oeis.org/A005773 (fetched 2026-10-06) - "Number of directed animals of size n (or directed n-ominoes in standard position)."; comment "(i.e., left factors of length n-1 of Motzkin paths, ...)"; data `1, 1, 2, 5, 13, 35, 96, 267, 750, 2123, 6046, 17303, 49721, 143365, …`, offset 0.
[^a057960]: https://oeis.org/A057960 (fetched 2026-10-06) - "Number of base-5 (n+1)-digit numbers starting with a zero and with adjacent digits differing by one or less."; comment "Or, number of three-choice paths along a corridor of width 5 and length n, starting from one side."; "G.f.: (1-x-x^2)/((1-x)*(1-2*x-2*x^2));"; data `1, 2, 5, 13, 35, 95, 259, 707, 1931, 5275, 14411, 39371, 107563, 293867, …`, offset 0.
[^a085810]: https://oeis.org/A085810 (fetched 2026-10-06) - "Number of three-choice paths along a corridor of height 5, starting from the lower side."; "G.f.: (1-2*x)/(1-4*x+3*x^2+x^3)."; data `1, 2, 5, 13, 35, 96, 266, 741, 2070, 5791, 16213, 45409, 127206, 356384, …`, offset 1.
[^a283595]: https://oeis.org/A283595 (fetched 2026-10-06) - "Triangle read by rows: T(n,k) is the number of Motzkin prefixes (i.e., left factors of Motzkin paths) of length n and height k."; data `1, 1, 1, 1, 3, 1, 1, 7, 4, 1, 1, 15, 13, 5, 1, 1, 31, 38, 19, 6, 1, …`, offset 0; the entry has no formula section.
[^a097862]: https://oeis.org/A097862 (fetched 2026-10-06) - "Triangle read by rows: T(n,k) is the number of Motzkin paths of length n and height k (n>=0, k>=0)."; "The g.f. for column k is z^(2k)/[P_k*P_{k+1}], where the polynomials P_k are defined by P_0=1, P_1=1-z, P_k=(1-z)P_{k-1}-z^2*P_{k-2}."; data `1, 1, 1, 1, 1, 3, 1, 7, 1, 1, 15, 5, 1, 31, 18, 1, …`, offset 0, row `n` has `1 + ⌊n/2⌋` terms.
[^exec]: Verified by execution (Python 3, SymPy, 2026-10-06) for `h = 1, …, 12`: the strip, exact-height, signed, free and pinned generating functions from the transfer matrix `I + A_path` (rises weighted `−1` for the signed count); the cofactor formula and the cosine sums against them; `Σ_w smooth(w, h) x^w = x^h/(η_h η_{h−1})` and the pinned formula `x^{2h−1}/(χ_h χ_{h−1})` as identities; the even/odd split against brute-force enumeration for `w ≤ 13`; `smooth(h + 1, h) = h + 1` with all `h` blocks; the free count `3^{w−1}` for `w ≤ h`; the anchored rows against A283595 rows 0-8, the pinned rows against A097862 rows 0-11, the strip rows against A001519, A057960, A085810 (14 terms) and A005773 for `w ≤ h`; the minimal polynomial degree of `1 + 2cos(π/(h+1))` against half of Euler's totient of `2h + 2`; the signed growth rates and reduced-denominator degrees as tabulated; the first 25 coefficients of `a_h` nonnegative; the two `η_h` formulas in terms of `χ` as polynomial identities for `h ≤ 12`, and the two factorizations of `χ_{2m+1}` and `χ_{2m}` for `m ≤ 15`. OEIS searches (2026-10-06) with no match: the strip rows at `h = 7, 8, 9`; the `smooth` rows at `h = 4, …, 9` as standalone sequences (they are columns of A283595); the `h = 4` even-block and odd-block rows; the `h = 4` free row.
