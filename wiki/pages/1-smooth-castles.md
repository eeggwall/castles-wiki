---
title: 1-smooth castles
category: Concepts
summary: A 1-smooth castle is a castle whose neighboring columns differ in height by at most 1; an anchored one also has its first column at height 1. Starting from the Pell castles (anchored 1-smooth castles of height 3), the anchored 1-smooth castles of height h are counted for every h, with tables for h = 2 to 12. The count smooth(w, h) = strips(w, h) − strips(w, h − 1) subtracts the anchored strips on {1, ..., h − 1} from those on {1, ..., h}, and its width generating function is x^h/(η_h(x) η_{h−1}(x)) = x^h/(η_{2h}(x) + x^h) for every h, where η_h(x) = Π(1 − λ_k x) over odd k ≤ h, λ_k = 1 + 2cos(πk/(h+1)), is a Chebyshev polynomial of the first or third kind in (1 − x)/(2x). So the count satisfies a recurrence of order h and grows like 1 + 2cos(π/(h+1)): 2, 1 + √2, φ², 1 + √3, ... toward 3. Also for every h: under the block sign the eigenvalues become 1 + 2i·cos(πk/(h+1)) and about half of them cancel when h is odd, so the parity orders follow h mod 4; for w ≤ 2h − 1 the ceiling acts once and smooth(w, h) is a sum of four trinomial coefficients; and the strips are sequences of atoms, Σ_w strips(w, h) x^{w−1} = 1/(1 − 2x − x²·mot_h(x)) with mot_h a Motzkin series on half the height. The counts are column h − 1 of A283595 (Motzkin prefixes by height); pinning both end columns gives x^{2h−1}/(χ_h χ_{h−1}) and column h − 1 of A097862; a free first column gives the smooth words of Knopfmacher, Mansour, Munagi and Prodinger, one castle of height h for each step sequence of range at most h − 1; and a last column within 1 of the first gives a difference of traces. Facts that hold only at small heights (Pell and Fibonacci closed forms, quadratic and metallic growth constants, the finite two-atom reading of 1/(1 − 2x − x²)) are collected at the end.
tags: [concept, castle, castle-type, 1-smooth, pell, transfer-matrix, chebyshev, parity, motzkin, generating-functions, oeis]
sources: [pe502-pell-castle-strip, barry-2005-catalan-transform, knopfmacher-mansour-munagi-prodinger-2008-smooth-words]
created: 2026-10-06
updated: 2026-10-22
---

# 1-smooth castles

## Definition

A castle of height `h` is a skyline `(c_1, …, c_w)` with `1 ≤ c_i ≤ h` and some `c_i = h` ([[castle-polyomino](pages/castle-polyomino.md)]). A **1-smooth castle** is a castle whose neighboring columns differ in height by at most 1 (the m-smooth type of [[castle-classification-shape](pages/castle-classification-shape.md)] at `m = 1`; general `m` on [[m-smooth-castles](pages/m-smooth-castles.md)]). An **anchored** 1-smooth castle also has its first column at height 1:

```
c_1 = 1,      |c_{i+1} − c_i| ≤ 1  (1 ≤ i < w),      max_i c_i = h.
```

- **Construction rule.** Start at height 1; at each step move up one, down one, or stay, never leaving `{1, …, h}`; and reach height `h` at least once.
- **Examples.** At `h = 4`, the five anchored 1-smooth castles of width 5 are `(1, 1, 2, 3, 4)`, `(1, 2, 2, 3, 4)`, `(1, 2, 3, 3, 4)`, `(1, 2, 3, 4, 3)`, `(1, 2, 3, 4, 4)`.
- **Non-examples.** The skyline `(1, 2, 3, 3)` is not a castle of height 4, since it never reaches 4; the skyline `(1, 2, 4, 3)` rises by 2 in one step.

The Pell castles are the anchored 1-smooth castles of height 3; they have height 3 by definition ([[pell-castle](pages/pell-castle.md)]). This page starts from them and follows the anchored castles to every `h`; the both-ends-pinned, free and cyclic boundary conditions are in [Other boundary conditions](#other-boundary-conditions).

**Counts.** For width `w` and ceiling `h`:

- `strips(w, h)` is the number of anchored 1-smooth skylines of width `w` with every column in `{1, …, h}`. They need not reach `h`, so they need not be castles of height `h`: they are the anchored strips of the Motzkin strip of height `h` ([[motzkin-castles](pages/motzkin-castles.md)] §4).
- `smooth(w, h)` is the number of anchored 1-smooth castles of width `w` and height `h`, the family count `A_X(w, h)` of [[castle-notation](pages/castle-notation.md)] for X the anchored 1-smooth castles.

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
- **Growth.** The silver mean `δ_2 = 1 + √2`: the Pell castles are silver by width.
- **Parity.** Split by PE 502's block parity, the even-block and odd-block rows satisfy a recurrence of order 8 and their difference one of order 5.

Sections 2 and 3 extend these to higher `h`; the last section lists the facts that hold only at small heights.

## 2. h = 4

At `h = 4` the same pieces are:[^exec]

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

The determinants `χ_i` are the `θ_i` of Knopfmacher, Mansour, Munagi and Prodinger, who invert `I − x(I + A_path)` entry by entry with Usmani's formula for tridiagonal matrices and write the generating function of their smooth words with a given first letter in Chebyshev polynomials. With first letter 1 it is this one ([[knopfmacher-mansour-munagi-prodinger-2008-smooth-words](pages/knopfmacher-mansour-munagi-prodinger-2008-smooth-words.md)]).[^kmmp-inverse]

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

**The four Chebyshev kinds.** Write `t = (1 − x)/(2x) = cos φ`. The Chebyshev polynomials of the first to fourth kinds are `T_n(cos φ) = cos(nφ)`, `U_n(cos φ) = sin((n+1)φ)/sin φ`, `V_n(cos φ) = cos((n + ½)φ)/cos(φ/2)` and `W_n(cos φ) = sin((n + ½)φ)/sin(φ/2)`, and `U_n − U_{n−1} = V_n`, `U_n + U_{n−1} = W_n` and `U_{n+1} − U_{n−1} = 2T_{n+1}`. So the formulas above say

```
χ_h = x^h U_h(t),        η_{2m} = x^m V_m(t),        η_{2m+1} = 2x^{m+1} T_{m+1}(t),        χ_m + xχ_{m−1} = x^m W_m(t),
```

and the factor that cancels at `h = 2m` is `x^m W_m(t)`.

**The numerators.** The cofactor sum of 3.1 is `x^{h−1} Σ_{k<h} U_k(t)`, and `Σ_{j=1}^{h} sin(jφ) = sin(hφ/2) sin((h+1)φ/2)/sin(φ/2)` gives `Σ_{k<2m} U_k = U_{m−1}W_m` and `Σ_{k<2m+1} U_k = U_mW_m`. Dividing by `χ_{2m} = η_{2m}·x^mW_m` and `χ_{2m+1} = χ_m η_{2m+1}` leaves the reduced strip generating functions:

```
Σ_w strips(w, 2m) x^w  =  x·χ_{m−1} / η_{2m},        Σ_w strips(w, 2m + 1) x^w  =  x·(χ_m + xχ_{m−1}) / η_{2m+1}.
```

At `h = 5` and `h = 6` they are `x(1 − x − x²)/((1 − x)(1 − 2x − 2x²))` and `x(1 − 2x)/(1 − 4x + 3x² + x³)`, `x` times the generating functions printed in A057960 and A085810 (table 3.5).[^exec]

### 3.3 The generating function of the castles of height h

**Proposition.** For every `h ≥ 1`,

```
Σ_w smooth(w, h) x^w  =  x^h / (η_h(x) · η_{h−1}(x)).
```

*Proof.* By 3.2, `Σ_w strips(w, h) x^w = x·N_h(x)/η_h(x)` with `deg N_h < deg η_h`, a sum of terms `c_k x/(1 − λ_k x)`. The eigenvalues of `η_h` and `η_{h−1}` are disjoint, since `cos(πk/(h+1)) = cos(πj/h)` would need `k/(h+1) = j/h`. Subtracting the `h − 1` series gives `x(N_h η_{h−1} − N_{h−1} η_h)/(η_h η_{h−1})`, whose numerator has degree at most `h`. Reaching height `h` from height 1 takes `h − 1` rises, so `smooth(w, h) = 0` for `w < h` and the numerator is divisible by `x^h`. At `w = h` the only castle is the staircase `(1, 2, …, h)`, so the coefficient is 1. ∎

At `h = 3` this gives `x³/((1 − 2x − x²)(1 − 2x))`, the Pell castle generating function. In general:[^exec]

- **Recurrence.** The denominator has degree `⌈h/2⌉ + ⌈(h−1)/2⌉ = h` and the numerator is a monomial, so `smooth(·, h)` satisfies a linear recurrence of order exactly `h`.
- **Smallest widths.** `smooth(h, h) = 1` (the staircase) and, for `h ≥ 2`, `smooth(h + 1, h) = h + 1`: the one step that is not a rise is a flat step in any of `h` places, or a final step down.
- **Explicit form.** `smooth(w, h) = strips(w, h) − strips(w, h − 1)`, each term given by the cosine sum of 3.2 or the trinomial sum of 3.7.

**Proposition.** For every `h ≥ 1`, `η_h η_{h−1} = η_{2h} + x^h`, so

```
Σ_w smooth(w, h) x^w  =  x^h / (η_{2h}(x) + x^h).
```

*Proof.* By the Chebyshev forms of 3.2, at `h = 2m` the claim is `2V_m T_m = V_{2m} + 1` and at `h = 2m + 1` it is `2T_{m+1} V_m = V_{2m+1} + 1`. Both follow from `2cos(aφ)cos(bφ) = cos((a + b)φ) + cos((a − b)φ)` with `a − b = ½` after dividing by `cos(φ/2)`. ∎

So the castles of height `h` have the strip denominator of height `2h` plus `x^h`, and since `x^h/(η_{2h} + x^h) = x^h/η_{2h} − x^{2h}/η_{2h}² + ⋯`, the castle row agrees with the coefficients of `x^h/η_{2h}` for its first `h` terms, `w = h, …, 2h − 1`. At `h = 6`, `1/η_12` is A122611, which agrees with `smooth(w, 6)` for `w = 6, …, 11` and has 6039 against 6038 at `w = 12`.[^a122611][^exec]

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
| 7 | `1, 2, 5, 13, 35, 96, 267, 749, 2113, 5982, …` | - | `1, 8, 43, 191, 760, 2816, 9933, 33812, …` | `1 + √(2 + √2) ≈ 2.8478` | 4 |
| 8 | `1, 2, 5, 13, 35, 96, 267, 750, 2122, 6035, …` | - | `1, 9, 53, 254, 1078, 4223, 15639, 55575, …` | `1 + 2cos(π/9) ≈ 2.8794` | 3 |
| 9 | `1, 2, 5, 13, 35, 96, 267, 750, 2123, 6045, …` | - | `1, 10, 64, 329, 1483, 6123, 23751, 87957, …` | `1 + 2cos(π/10) ≈ 2.9021` | 4 |
| 10 | `1, 2, 5, 13, 35, 96, 267, 750, 2123, 6046, 17302, …` | - | `1, 11, 76, 417, 1989, 8631, 34993, 134828, …` | `1 + 2cos(π/11) ≈ 2.9190` | 5 |
| 11 | `1, 2, 5, 13, 35, 96, 267, 750, 2123, 6046, 17303, 49720, …` | - | `1, 12, 89, 519, 2611, 11878, 50236, 201076, …` | `1 + (√6 + √2)/2 ≈ 2.9319` | 4 |
| 12 | `1, 2, 5, 13, 35, 96, 267, 750, 2123, 6046, 17303, 49721, 143364, …` | - | `1, 13, 103, 636, 3365, 16012, 70516, 292791, …` | `1 + 2cos(π/13) ≈ 2.9419` | 6 |

"Degree" is the degree of the growth constant as an algebraic number, half of Euler's totient of `2h + 2`. "-" means no A-number is listed here; [[castle-sequence-catalogue](pages/castle-sequence-catalogue.md)] records the OEIS status of those rows.[^exec]

- **The strip rows.** An anchored skyline of width `w` cannot rise above height `w`, so the ceiling matters only from `w = h + 1` on, and for `w ≤ h` the strip row equals the anchored 1-smooth count with no ceiling, A005773(`w`).[^a005773] The `h = 5` row is A057960, base-5 digit strings that start with 0 and whose adjacent digits differ by at most 1;[^a057960] the `h = 6` row is A085810, three-choice paths in a corridor of height 5.[^a085810]
- **The castle rows.** Every `smooth` row is a column of one OEIS triangle: `smooth(w, h)` is A283595 at row `w − 1`, column `h − 1`, the number of Motzkin prefixes of length `w − 1` and height `h − 1`. The entry gives no generating function.[^a283595] At `h = 3` the row is also A094706(`w − 2`) ([[pell-castle](pages/pell-castle.md)]).

### 3.6 Block parity

Project Euler 502 counts the castles with an even number of blocks. For an anchored 1-smooth castle, `blocks(c) = c_1 + Σ max(0, c_{i+1} − c_i) = 1 + (number of rises)`. So the signed count `Σ (−1)^{blocks}` is the transfer-matrix count with each rise weighted by `−1`, and the eigenvalues become `1 + 2i·cos θ_k` ([[motzkin-castles](pages/motzkin-castles.md)] §3). Even-block and odd-block counts are (`smooth` ± signed)/2.

At `w = h` and, for `h ≥ 2`, `w = h + 1`, every anchored 1-smooth castle of height `h` has `h − 1` rises and so `h` blocks. The first entries are all even-block for even `h` and all odd-block for odd `h`.[^exec]

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

The orders are the degrees of the reduced denominators, from the weighted transfer matrix; at `h = 2` the even-block row has order 3 and the odd-block row order 4. At `h = 2` every anchored castle is a castle of width `w` whose first column has height 1, and deleting that column keeps the block count ([[m-smooth-castles](pages/m-smooth-castles.md)] §3.3), so the rows are those of all castles of height 2 and width `w − 1`: even-block `A038505(w)`, odd-block `A038503(w) − 1`, even − odd `A077860(w − 2)`.[^h2rows][^exec]

**Proposition (signed eigenvalues).** Let `H ≥ 1` and `θ_k = πk/(H + 1)`. The signed count `Σ (−1)^{#rises}` over the anchored strips of width `w` on `{1, …, H}` is `Σ_k c_k (1 + 2i·cos θ_k)^{w−1}` with

```
c_k  =  (2/(H + 1)) · sin θ_k · Σ_{j=1}^{H} i^{j−1} sin(jθ_k),
```

and `c_k = 0` exactly when `2k ≠ H + 1` and `i^{H+1}(−1)^k = 1`. So all `H` eigenvalues survive when `H` is even, `(H + 1)/2` of them when `H ≡ 1 (mod 4)` (the even `k` and `k = (H + 1)/2`), and `(H + 3)/2` when `H ≡ 3 (mod 4)` (the odd `k` and `k = (H + 1)/2`).

*Proof.* The weighted matrix has `−1` above the diagonal and `1` below it. Conjugating by `D = diag((−i)^{j−1})` turns it into `I + i·A_path`, whose eigenvectors are `v_k(j) = sin(jθ_k)` with `|v_k|² = (H + 1)/2`, and `D^{−1}𝟙` has entries `i^{j−1}`; this gives `c_k`. Write the sum as `(1/i)Σ_j i^j sin(jθ_k)` and expand the sine: with `q_± = i·e^{±iθ_k}`, both `q_±^{H+1}` equal `ε = i^{H+1}(−1)^k`, and when neither `q_±` is 1 the two geometric series give `Σ_j i^j sin(jθ_k) = i sin θ_k (1 − ε)/((1 − q_+)(1 − q_−))`, which vanishes exactly when `ε = 1`. `q_+ ≠ 1` always, and `q_− = 1` only at `θ_k = π/2`, that is `2k = H + 1`; there `Σ_j i^j sin(jπ/2) = i(H + 1)/2 ≠ 0`, and `c_k = 1`. ∎

The signed castle count at height `h` is the signed strip count at `h − 1` minus the one at `h`. The eigenvalues `1 + 2i·cos θ` are distinct, nonzero (real part 1), and different at `h` and `h − 1` (as in 3.3), so for every `h ≥ 2`:

- **Signed orders.** The order of even − odd is the number of survivors at `h` and at `h − 1`: `(3h + 2)/2`, `(3h − 1)/2`, `3h/2`, `(3h + 1)/2` for `h ≡ 0, 1, 2, 3 (mod 4)`. This gives `3, 5, 7, 7, 9, 11, 13, 13, …`, with the repeats at `h ≡ 1 (mod 4)`.
- **Signed growth.** The largest `|1 + 2i·cos θ_k| = √(1 + 4cos² θ_k)` is at `k = 1` and `k = H`, which cancel exactly when `H ≡ 1 (mod 4)` and `H ≥ 5`. So even − odd grows like `√(1 + 4cos²(π/(h+1)))`, except at `h ≡ 1 (mod 4)`, `h ≥ 5`, where the rate is the one at `h − 1`, `√(1 + 4cos²(π/h))`. This is below `1 + 2cos(π/(h+1))`, so each parity class is half of `smooth(w, h)` up to a smaller term.
- **Even and odd orders.** The real eigenvalues of 3.3 and the signed ones share only the value 1. It occurs in the signed count at every `h`, from whichever of `h`, `h − 1` is odd, with coefficient `−1` for odd `h` and `+1` for even `h`, and in `smooth(w, h)` exactly when `h ≡ 1` or `2 (mod 4)`, with coefficient `2/(h + 1)` or `−2/h`. It cancels in `(smooth ± signed)/2` only in the even-block row at `h = 2`. So for `h ≥ 3` both parity rows have order `h` plus the signed order, minus 1 when `h ≡ 1` or `2 (mod 4)`: `(5h + 2)/2`, `(5h − 3)/2`, `(5h − 2)/2`, `(5h + 1)/2` for `h ≡ 0, 1, 2, 3 (mod 4)`, the column of the table.[^exec]

### 3.7 Without eigenvalues: the method of images

Write `tri(n, d) = [t^d](t^{−1} + 1 + t)^n` for the trinomial coefficients, the number of step sequences in `{−1, 0, 1}^n` with sum `d`; they are the rows of A027907 read from the center.[^a027907] A strip on `{1, …, h}` is a walk that never visits the heights 0 and `h + 1`, and a step of size at most 1 cannot pass a height without landing on it, so the reflection principle applies at both walls. The walks from height 1 to height `e` number `Σ_{j∈Z} [tri(w − 1, e − 1 + 2j(h+1)) − tri(w − 1, e + 1 + 2j(h+1))]`, and the sum over `e = 1, …, h` telescopes:

```
strips(w, h)  =  Σ_{j∈Z} [ tri(w−1, 2j(h+1)) + tri(w−1, 2j(h+1) + 1) − tri(w−1, 2j(h+1) + h) − tri(w−1, 2j(h+1) + h + 1) ].
```

Only the `j` with `|j| ≤ (w − 1)/(2(h + 1)) + 1` contribute, since `tri(n, d) = 0` for `|d| > n`. With no ceiling the sum is `tri(w − 1, 0) + tri(w − 1, 1)`, the Motzkin prefix count A005773(`w`).[^exec]

**The near-staircase range.** For `w ≤ 2h − 1` only the terms `j = 0` and `j = −1` are nonzero, in both `strips(w, h)` and `strips(w, h − 1)`, and their difference is

```
smooth(w, h)  =  tri(w−1, h−1) + tri(w−1, h) − tri(w−1, h+1) − tri(w−1, h+2)        (w ≤ 2h − 1).
```

In this range the ceiling acts once. At `w = 2h` the term `tri(2h − 1, 2h − 1) = 1` of `strips(w, h − 1)` enters, and the right side exceeds `smooth(2h, h)` by 1. Since `tri(n, n − s)` is a polynomial in `n` of degree `s`, the count at a fixed excess `d = w − h` is a polynomial in `h` of degree `d`, with leading coefficient `1/d!`, valid for `h ≥ d + 1`:

```
smooth(h, h) = 1,    smooth(h + 1, h) = h + 1,    smooth(h + 2, h) = (h² + 5h + 2)/2,    smooth(h + 3, h) = (h³ + 12h² + 29h + 12)/6.
```

The first two are the staircase counts of 3.3, and by the second form of 3.3 these are also the first `h` coefficients of `1/η_{2h}`. The last width of the range, `w = 2h − 1`, is the diagonal A283667 of A283595, the Motzkin prefixes of length `2n` and height `n`: `smooth(2h − 1, h) = A283667(h − 1)`. That entry gives a recursion and an asymptotic, and the formula above gives it in closed form, `A283667(n) = tri(2n, n) + tri(2n, n + 1) − tri(2n, n + 2) − tri(2n, n + 3)`.[^a283667][^exec]

### 3.8 The strip as a sequence of atoms

**Proposition.** For every `h ≥ 2`,

```
Σ_w strips(w, h) x^{w−1}  =  1 / (1 − 2x − x²·mot_h(x)),
```

where `mot_h(x)` counts by length the Motzkin paths on the levels `0, …, ⌈h/2⌉ − 2`, with flat steps forbidden on the top level when `h` is odd. At `h = 2` there are no levels and `mot_2 = 0`; at `h = 3` the only path is the empty one and `mot_3 = 1`; `mot_4 = 1/(1 − x)`.

*Proof.* Use the reduced forms of 3.2. At `h = 2m` the reciprocal of the left side is `η_{2m}/χ_{m−1} = χ_m/χ_{m−1} − x`, and `χ_m = (1 − x)χ_{m−1} − x²χ_{m−2}` makes it `1 − 2x − x²·χ_{m−2}/χ_{m−1}`. At `h = 2m + 1` put `ξ_j = χ_j + xχ_{j−1} = x^j W_j(t)`, which satisfies the recurrence of `χ_j`; then `η_{2m+1} = ξ_{m+1} − xξ_m`, and the reciprocal is `1 − 2x − x²·ξ_{m−1}/ξ_m`. Both ratios satisfy `r_L = 1/(1 − x − x²·r_{L−1})`. This is the first-return decomposition of a Motzkin path on the levels `0, …, L` (empty, or a flat step and a path, or `U`, a path on the levels `1, …, L`, `D` and a path), so `r_L` counts the paths on `0, …, L` with the top-level rule of `r_0`. The starting values are `χ_{−1}/χ_0 = 0`, no levels, and `ξ_0/ξ_1 = 1`, one level and no flat step on it. ∎

So for every `h` the anchored strips are free sequences of atoms: two atoms of width 1, and `[x^n] mot_h(x)` atoms of width `n + 2`. The series `a_h(x) = 2x + x²·mot_h(x)` has nonnegative coefficients for every `h`. At `h = 3` there are exactly two atoms, the two-atom reading of `1/(1 − 2x − x²)` on [[pell-castle-strip](pages/pell-castle-strip.md)]. With no ceiling `mot_h` becomes the Motzkin generating function `M(x)`, and then the atoms are combinatorial. A Motzkin prefix, the strip lowered by one, is a free sequence of flat steps, up steps never matched by a later down step, and factors `U·(Motzkin path)·D`. At finite `h` the proof is algebraic: in a strip a factor `U·(path)·D` starting at altitude `a` has height at most `h − 2 − a`, which depends on `a`, while the height bound `⌈h/2⌉ − 2` of the atoms in `mot_h` does not, so the atoms are not these factors.[^exec]

## Other boundary conditions

The same matrix with other end conditions gives three more 1-smooth families of height `h`. All three have the growth `1 + 2cos(π/(h+1))` of 3.4.[^exec]

**Both end columns at height 1.** The strip generating function is `x·χ_{h−1}/χ_h`, a corner cofactor. The determinants satisfy `χ_{h−1}² − χ_h χ_{h−2} = x^{2(h−1)}`: substituting the recurrence shows the left side is `x²` times its value at `h − 1`, and it equals 1 at `h = 1`. So for every `h ≥ 1` (with `χ_{−1} = 0`),

```
Σ_w #{1-smooth castles of height h with c_1 = c_w = 1} x^w  =  x^{2h−1} / (χ_h(x) · χ_{h−1}(x)),
```

of order `deg χ_h + deg χ_{h−1}`: `2h − 1` when `h ≡ 1 (mod 3)` and `2h − 2` otherwise, since `χ_h` has degree `h − 1` when 3 divides `h + 1` (the zero eigenvalue `λ_k = 0`). No eigenvalue cancels here, since `v_k(1) = sin θ_k ≠ 0`. The first such castle has width `2h − 1`, `(1, 2, …, h, …, 2, 1)`. Subtracting 1 from every column gives a Motzkin path of length `w − 1` and height `h − 1`, so the count is A097862 at row `w − 1`, column `h − 1`. The entry states this column generating function, `z^{2k}/(P_k P_{k+1})` with its `P_k` equal to `χ_k`, by path length instead of width;[^a097862] [[castle-classification-shape](pages/castle-classification-shape.md)] tabulates it by `(w, h)` for `w ≤ 9` under the Motzkin-path type. At `h = 3` this is the row `0, 0, 0, 0, 1, 5, 18, 56, …` on [[pell-castle](pages/pell-castle.md)]. Since the transfer matrix is `I + A`, the strips with both ends at height 1, whether or not they reach `h`, are a [[binomial-transform](pages/binomial-transform.md)]: choose the `2k` column boundaries where the height changes, then a Dyck path of semilength `k` and height `≤ h − 1` through them, so the strip count is `Σ_k C(w − 1, 2k)·#{Dyck paths of semilength k, height ≤ h − 1}`, Barry's aerated transform; with no ceiling it is Barry's `M_n = Σ_k C(n, 2k) C_k`.[^barry]

**Free first column.** The free 1-smooth skylines on `{1, …, h}` are the smooth words over `{1, …, h}` of Knopfmacher, Mansour, Munagi and Prodinger, and their Theorem 2.4 counts them as `(2/(h+1)) Σ_{k odd} cot²(θ_k/2) λ_k^{w−1}`. Only odd `k` contribute, because `𝟙` is orthogonal to the even-`k` eigenvectors on both sides.[^kmmp-free] Every coefficient is positive, so for every `h` the reduced denominator of the free castles of height `h` is again `η_h η_{h−1}`, but the numerator is not a monomial. At `h = 3` it is `x(1 − x)`. A step sequence in `{−1, 0, 1}^{w−1}` whose partial sums have range `r` fits on `{1, …, h}` with its top column at height `h` in exactly one way if `r ≤ h − 1`, and in none otherwise. So the free 1-smooth castles of height `h` and width `w` correspond one to one to the step sequences of length `w − 1` and range at most `h − 1`. For `w ≤ h` every sequence qualifies, and there are `3^{w−1}` of them. In the OEIS the free skylines are the rows of A188866, so for `h ≥ 3` the free castles of height `h` number `A188866(h − 1, w) − A188866(h − 2, w)`.[^a188866]

**Last column within 1 of the first.** The same paper counts the smooth cyclic words, which also satisfy `|c_w − c_1| ≤ 1`. On `{1, …, h}` their number is the trace `Σ_{k=1}^{h} λ_k^w`, every eigenvalue with coefficient 1 (their Theorem 3.3).[^kmmp-cyclic] So the cyclic 1-smooth castles of height `h` number

```
Σ_{k=1}^{h} (1 + 2cos(πk/(h+1)))^w  −  Σ_{j=1}^{h−1} (1 + 2cos(πj/h))^w,
```

with the reduced denominator `χ_h χ_{h−1}` of the pinned castles. Under the step-sequence correspondence they are the sequences of range at most `h − 1` whose sum is `−1`, 0 or 1. A sequence with range `h` and such a sum has at least `2h − 1` steps, so for `w ≤ 2h − 1` every such sequence qualifies, and the count is `tri(w − 1, −1) + tri(w − 1, 0) + tri(w − 1, 1) = tri(w, 0)`, the central trinomial coefficient A002426(`w`) (3.7). At `w = 2h` the `2h` sequences `D^b U^h D^{h−1−b}` (`0 ≤ b < h`) and their negatives drop out, which leaves `A002426(2h) − 2h`.[^a002426][^exec]

| `h` | free first column, `w = h+1, h+2, …` | both ends at height 1, `w = 2h−1, 2h, …` | cyclic, `w = 2h, 2h+1, …` |
|---|---|---|---|
| 2 | `7, 15, 31, 63, 127, …` | `1, 3, 7, 15, 31, 63, …` | `15, 31, 63, 127, …` |
| 3 | `25, 67, 175, 449, 1137, …` | `1, 5, 18, 56, 161, 441, …` | `135, 351, 899, 2275, …` |
| 4 | `79, 227, 643, 1801, 4999, …` | `1, 7, 33, 129, 453, 1485, …` | `1099, 3067, 8523, 23563, …` |
| 5 | `241, 711, 2081, 6049, 17479, …` | `1, 9, 52, 242, 990, 3718, …` | `8943, 25543, 73021, …` |
| 6 | `727, 2167, 6433, 19021, 56031, …` | `1, 11, 75, 403, 1872, 7878, …` | `73777, 212785, 614981, …` |
| 7 | `2185, 6539, 19531, 58211, 173113, …` | `1, 13, 102, 620, 3215, 14943, …` | `616213, 1787397, 5194739, …` |
| 8 | `6559, 19659, 58871, 176105, 526159, …` | `1, 15, 133, 901, 5151, 26163, …` | `5196611, 15134659, …` |
| 9 | `19681, 59023, 176941, 530165, 1587529, …` | `1, 17, 168, 1254, 7828, 43092, …` | `44152791, 128996511, …` |
| 10 | `59047, 177119, 531205, 1592781, 4774365, …` | `1, 19, 207, 1687, 11410, 67620, …` | `377379349, 1105350309, …` |
| 11 | `177145, 531411, 1594055, 4781127, 14338159, …` | `1, 21, 250, 2208, 16077, 102005, …` | `3241135505, 9513227617, …` |
| 12 | `531439, 1594291, 4782667, 14346729, 43033457, …` | `1, 23, 297, 2825, 22025, 148905, …` | `27948336357, 82176835701, …` |

The free row at `h = 3` is A106514(`w − 1`) ([[pell-castle](pages/pell-castle.md)]). The cyclic rows begin with A002426(`w`) for `w ≤ 2h − 1`, so the table starts them at `w = 2h`.

## Computation

```python
from math import comb, cos, pi
def smooth(W, h):
    """(even, odd) anchored 1-smooth castles of height h, widths 1..W.
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
def tri(n, d):
    """[t^d](1/t + 1 + t)^n: a down steps, a + |d| up steps, the rest flat."""
    d = abs(d)
    return sum(comb(n, a) * comb(n - a, a + d) for a in range(n + 1) if n - a >= a + d)
for h in range(1, 13):
    c = smooth(20, h)
    assert all(e + o == strips(w, h) - strips(w, h - 1) for w, (e, o) in enumerate(c, start=1))
    assert all(sum(c[w - 1]) == tri(w - 1, h - 1) + tri(w - 1, h) - tri(w - 1, h + 1) - tri(w - 1, h + 2)
               for w in range(1, min(20, 2 * h - 1) + 1))    # 3.7, w <= 2h - 1
print([e + o for e, o in smooth(12, 4)])    # 0, 0, 0, 1, 5, 19, 64, 202, 612, 1803, 5205, 14797
```

## Facts that hold only at small heights

The definition, the subtraction `strips(w, h) − strips(w, h − 1)`, the transfer matrix and its Chebyshev determinants, the generating function of the castles of height `h` and its monomial numerator, the growth ladder, the parity orders and signed growth (3.6), the trinomial form (3.7), the atoms of the strip (3.8) and the four boundary conditions extend to every `h`. The following do not.

- **Named integer sequences.** The strip rows are Pell at `h = 3` and odd-indexed Fibonacci at `h = 4`. At `h = 5` and `6` they are OEIS entries named for digit strings and corridor paths (A057960, A085810). The castle rows exist in the OEIS only as columns of A283595, and at `h = 2` and `h = 3` as A000225 (`2^{w−1} − 1`) and A094706.[^a000225]
- **Quadratic growth constants.** `1 + 2cos(π/(h+1))` has degree equal to half of Euler's totient of `2h + 2`, which is at most 2 only for `h ≤ 5`. For `h = 6, …, 12` the growth constants are cubic, quartic, quintic and sextic (table 3.5).
- **Metallic labels.** The growth `1 + 2cos(π/(h+1))` is a metallic mean ([[metallic-means](pages/metallic-means.md)]) at three heights: copper `2 = σ_1^2` at `h = 2`, silver `1 + √2` at `h = 3`, and `1 + √3 = σ_2^2`, the root of `x² − 2x − 2`, at `h = 5`. So the anchored 1-smooth castles of heights 2, 3 and 5 are copper, silver and `σ_2^2` by width ([[castle-classification-growth](pages/castle-classification-growth.md)]). `φ²` (`h = 4`, root of `x² − 3x + 1`) is quadratic but not a member. Silver at `h = 3` comes from the 1-smooth rule. The ridge rule reaches the metallic means at every height ([[metallic-strip-realizability](pages/metallic-strip-realizability.md)]).
- **The two-atom reading.** The Analytic Combinatorics exercise of [[pell-castle-strip](pages/pell-castle-strip.md)] reads `1/(1 − 2x − x²)` as sequences of a width-1 atom of weight 2 and a width-2 atom of weight 1. The atom series `a_h = 2x + x²·mot_h` of 3.8 is a polynomial only for `h ≤ 3`: `2x` at `h = 2`, `2x + x²` at `h = 3`, and from `h = 4` on (`2x + x²/(1 − x)` at `h = 4`) it has infinitely many atoms. In the other direction, the m-smooth castles keep the two-atom reading on the diagonal `h = m + 2`, with atoms of weight `m + 1` and `m` ([[m-smooth-castles](pages/m-smooth-castles.md)] §3.6).

## Related Concepts

- [[1-smooth-pell-castles-by-area](pages/1-smooth-pell-castles-by-area.md)] - the Pell castles of height 3 counted by cells rather than columns, with joint width/area bookkeeping and area growth.
- [[pell-castle](pages/pell-castle.md)] - the `h = 3` case, where this page starts.
- [[knopfmacher-mansour-munagi-prodinger-2008-smooth-words](pages/knopfmacher-mansour-munagi-prodinger-2008-smooth-words.md)] - smooth words: the free strips, the anchored strips through Usmani's tridiagonal inverse, and the cyclic words as a trace.
- [[kernel-method](pages/kernel-method.md)] - the same strips through the two roots of the kernel `1 − x(u^{−1} + 1 + u)` ([[banderier-nicodeme-2010-bounded-discrete-walks](pages/banderier-nicodeme-2010-bounded-discrete-walks.md)]).
- [[pell-castle-strip](pages/pell-castle-strip.md)] - the `h = 3` strip and the two-atom reading of `1/(1 − 2x − x²)`.
- [[binomial-transform](pages/binomial-transform.md)] - `I + A` as a binomial transform: flat steps chosen freely, the walls only constrain the skeleton ([[barry-2005-catalan-transform](pages/barry-2005-catalan-transform.md)]).
- [[motzkin-castles](pages/motzkin-castles.md)] - the same matrix with both end columns pinned (§4, the growth ladder) and the signed eigenvalues `1 + 2i·cos θ_k` (§3); anchored at height 1 with no ceiling, the Motzkin prefixes A005773 (§5).
- [[castle-strip](pages/castle-strip.md)] - how a rule on neighboring columns becomes a transfer matrix on column heights.
- [[m-smooth-castles](pages/m-smooth-castles.md)] - neighboring columns differing by at most `m`, starting from this page.
- [[castle-classification-shape](pages/castle-classification-shape.md)] - the m-smooth type, here at `m = 1`.
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
[^kmmp-inverse]: [[knopfmacher-mansour-munagi-prodinger-2008-smooth-words](pages/knopfmacher-mansour-munagi-prodinger-2008-smooth-words.md)] §2 (2.1)-(2.2), (2.5) L120-L137, L208-L211 [synthesis] - the matrix with "aii = 1 − x, ai(i+1) = a(i+1)i = −x", inverted by "a result of Usmani [8]", with "θi = (1 − x)θi−1 − x2 θi−2 , with the initial conditions θ0 = 1 and θ1 = 1 − x" and "θi = x^i Ui((1−x)/2x)"; (2.5) is the generating function of the smooth words with first letter `i`.
[^kmmp-free]: [[knopfmacher-mansour-munagi-prodinger-2008-smooth-words](pages/knopfmacher-mansour-munagi-prodinger-2008-smooth-words.md)] §2 Theorem 2.4 L321-L332 [synthesis] - "The number of smooth words of length n over the alphabet [k] is given by", in the second form, `(2/(k+1)) Σ_{0≤j≤(k−1)/2} cot²((2j+1)π/(2(k+1))) (1 + 2cos((2j+1)π/(k+1)))^{n−1}`.
[^kmmp-cyclic]: [[knopfmacher-mansour-munagi-prodinger-2008-smooth-words](pages/knopfmacher-mansour-munagi-prodinger-2008-smooth-words.md)] §3 Theorem 3.3 L597-L602 [synthesis] - "The number of smooth cyclic words of length n over the alphabet [k] is given by scwn,k = Σ_{j=1}^{k} (1 + 2 cos(jπ/(k+1)))^n", for `n ≥ 1`; smooth cyclic means "|σn − σ1 | ≤ 1" in addition (L12-L13).
[^a188866]: https://oeis.org/A188866 (read 2026-10-22) - comment "Number of 0..n strings of length k and adjacent elements differing by one or less."; offset 1,1, so row `n` holds the free skylines on `n + 1` heights; the difference of rows matched the free castles of height `h` for `3 ≤ h ≤ 11`, `w ≤ 14`, against the table printed in the entry.
[^a002426]: https://oeis.org/A002426 (read 2026-10-22) - "Central trinomial coefficients: largest coefficient of (1 + x + x^2)^n."; comment "Number of paths of length n with steps U = (1,1), D = (1,-1) and H = (1,0), running from (0,0) to (n,0) (i.e., grand Motzkin paths of length n)"; data `1, 1, 3, 7, 19, 51, 141, 393, 1107, 3139, 8953, 25653, 73789, …`, offset 0.
[^a027907]: https://oeis.org/A027907 (read 2026-10-22) - "Triangle of trinomial coefficients T(n,k) (n >= 0, 0 <= k <= 2*n), read by rows: n-th row is obtained by expanding (1 + x + x^2)^n."; so `tri(n, d) = T(n, n + d)`.
[^a122611]: https://oeis.org/A122611 (read 2026-10-22) - "G.f.: 1/(1 - 7 x + 15 x^2 - 6 x^3 - 11 x^4 + 6 x^5 + x^6)."; data `1, 7, 34, 139, 516, 1802, 6039, 19657, …`, offset 1; the denominator is `η_12` of the table in 3.2.
[^h2rows]: https://oeis.org/A038505, https://oeis.org/A038503, https://oeis.org/A077860 (read 2026-10-22) - A038505, "Sum of every 4th entry of row n in Pascal's triangle, starting at binomial(n,2).", whose comment reads `a(n)` as the castles of width `n − 1` and height 2 with an even number of blocks; A038503, "Sum of every 4th entry of row n in Pascal's triangle, starting at "n choose 0".", whose comment reads `a(n) − 1` as those with an odd number of blocks; A077860, "Expansion of 1/((1 - 2*x + 2*x^2)*(1-x))."; all offset 0, matched for `w ≤ 16`.
[^a283667]: https://oeis.org/A283667 (read 2026-10-22) - "Number of Motzkin prefixes of length 2n and height n."; formulas "Recursion: see Maple program.", "a(n) = A283595(2n,n)." and an asymptotic by Kotesovec; data `1, 3, 13, 64, 334, 1802, 9933, 55575, …`, offset 0; the trinomial formula matched all 24 listed terms.
[^a000225]: https://oeis.org/A000225 (read 2026-10-22) - "a(n) = 2^n - 1."; offset 0, so `smooth(w, 2) = A000225(w − 1)`.
[^exec]: Verified by execution (Python 3.11, SymPy, 2026-10-06 and 2026-10-16) for `h = 1, …, 12`: the strip, castle, signed, free and pinned generating functions from the transfer matrix `I + A_path` (rises weighted `−1` for the signed count); the cofactor formula and the cosine sums against them; `Σ_w smooth(w, h) x^w = x^h/(η_h η_{h−1})` and the pinned formula `x^{2h−1}/(χ_h χ_{h−1})` as identities; the even/odd split against brute-force enumeration for `w ≤ 13`; `smooth(h + 1, h) = h + 1` with all `h` blocks; the free count `3^{w−1}` for `w ≤ h`; the anchored rows against A283595 rows 0-8, the pinned rows against A097862 rows 0-11, the strip rows against A001519, A057960, A085810 (14 terms) and A005773 for `w ≤ h`; the minimal polynomial degree of `1 + 2cos(π/(h+1))` against half of Euler's totient of `2h + 2`; the signed growth rates and reduced-denominator degrees as tabulated; the first 25 coefficients of `a_h` nonnegative; the two `η_h` formulas in terms of `χ` as polynomial identities for `h ≤ 12`, and the two factorizations of `χ_{2m+1}` and `χ_{2m}` for `m ≤ 15`. On 2026-10-16 every table on the page was recomputed by a dynamic program over (last height, block parity, reached h), the reduced denominators η_h and the generating function x^h/(η_h η_{h−1}) were rederived from (I − x(I + A_path))^{−1} for `h ≤ 12`, the parity orders were recomputed by Berlekamp-Massey on 120 terms, and A001519, A005773, A057960, A085810, A097862 and A283595 were rechecked on oeis.org. On 2026-10-22: the Chebyshev forms of `χ_h`, `η_{2n}`, `η_{2n+1}` and `χ_n + xχ_{n−1}` (numerically at three values of `t`, `n < 20`), the cofactor sums, the reduced strip generating functions and the factorizations of 3.2 as polynomial identities for `h ≤ 47`, and `η_h η_{h−1} = η_{2h} + x^h` for `h ≤ 24`; the signed-eigenvalue proposition, by comparing the reduced denominator of the signed castle count (Berlekamp-Massey on `6h + 20` terms) with the product over the predicted surviving eigenvalues to `10^{−40}`, and the even/odd orders, for `h ≤ 30`; the method-of-images formula against the dynamic program for `h ≤ 15`, `w ≤ 45`, the near-staircase formula for `w ≤ 2h − 1` with its excess of exactly 1 at `w = 2h`, and the fixed-excess polynomials for `d ≤ 7`, `h ≤ 44`; the atom proposition to 45 terms for `h ≤ 30`, with `mot_h` from a dynamic program over Motzkin paths, and the nonnegativity of 40 coefficients of `a_h` for `h ≤ 12`; the free castles against the step sequences of range at most `h − 1` by enumeration for `h ≤ 6`, `w ≤ 9`; the cyclic castles against the trace formula, `A002426(w)` for `w ≤ 2h − 1` and `A002426(2h) − 2h` at `w = 2h`, for `h ≤ 12`; the extended code block.
[^barry]: [[barry-2005-catalan-transform](pages/barry-2005-catalan-transform.md)] §7 L1100-L1130, L1174-L1194 [synthesis] - the transform `b_n = Σ_k C(n, 2k) a_k`, factored as `Bin ◦ (1, x²)` ("'aerate' a sequence with interpolated zeros and then follow this with a binomial transform"), and `M_n = Σ_k C(n, 2k) C(k)`. The castle reading is verified on the source page (footnote exec): with `c_1 = c_w = 1`, the strip count equals `Σ_k C(w − 1, 2k)` times the closed flat-free walks of length `2k` for `h ∈ {2, 3, 4, 5, 8}` and no ceiling, `w ≤ 14`.
