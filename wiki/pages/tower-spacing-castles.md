---
title: Minimum tower spacing - skylines and castles
category: Analyses
summary: A skyline has tower spacing at least g when, in every row, each run of empty cells with filled cells on both sides has length at least g. spacing_g(w, h) counts such skylines of width w on {1, …, h}, which need not reach h; the castles of height h among them number spacing_g(w, h) − spacing_g(w, h − 1). A skyline has tower spacing at least g exactly when its 0-based heights are the window-g running minimum of a longer array, so spacing_g(·, h) is Hardin's count of minimum-filter outputs (A217883, A217954, A228461 and their columns), and at g = 2 it is W_{h−1}(w + 1), Hardin's words with no strict local maximum. At h = 2, spacing_g(w, 2) = Σ_k C(w + g − (g−1)k, 2k), with denominator (1 − x)² − x^{g+1}, growth ψ² at g = 2, φ at g = 3 and the supergolden ratio at g = 5. The minimal recurrence has order (h − 1)g + 1 at every h and g ≥ 2: the arrays whose level sets have all runs at least g long satisfy a recursion in h whose numerator and denominator advance by a 2 × 2 matrix of determinant 1. For h ≥ 3 no growth constant is a metallic mean. The row h = 2 is Hardin's table A217839, with spacing_7(w, 2) = A217838(w), and spacing_h(s − h, 2) − 1 counts the castles of height h with every column 1 or h by semi-perimeter s.
tags: [analysis, castle, gap-rule, tower-spacing, transfer-matrix, growth-constant, plastic-number, golden-ratio, generating-function, rule-3, sympy, verification, oeis, min-filter, unimodal]
sources: [pe502-pell-castle-strip, balado-silvestre-2026-runs-binary-strings]
created: 2026-09-18
updated: 2026-10-26
---

# Minimum tower spacing - skylines and castles

## The rule

Project Euler 502's rule 3 asks for at least one unit of empty space between neighboring blocks in a row ([[castle-polyomino](pages/castle-polyomino.md)]). Raise "one" to `g`: a skyline `c = (c_1, …, c_w)` has **tower spacing at least `g`** when, for every row `r`, each run of empty cells in row `r` that has filled cells on both sides has length at least `g`. Row `r` is filled at the columns with `c_i ≥ r`, so the rule says that two columns reaching row `r` with only lower columns between them are at least `g + 1` columns apart. Row 1 is full in every skyline, so the rule constrains rows `2, …, h`. At `g = 1` every skyline qualifies.[^1]

`spacing_g(w, h)` is the number of skylines of width `w` with entries in `{1, …, h}` and tower spacing at least `g`. These skylines need not reach height `h`, so they need not be castles of height `h`; the castles of height `h` among them number

```
A_spacing(g)(w, h)  =  spacing_g(w, h) − spacing_g(w, h − 1).
```

*Example: `h = 2`, `g = 2`, `w = 3`.* Of the eight skylines in `{1, 2}^3`, only `(2, 1, 2)` has a run of empty cells of length 1 between filled cells in row 2, so `spacing_2(3, 2) = 7`. Removing the flat row `(1, 1, 1)` leaves the six castles of height 2.

The rule bounds the horizontal distance between raised columns, unlike the rules of [[metallic-strip-realizability](pages/metallic-strip-realizability.md)] and [[castle-strip](pages/castle-strip.md)], which restrict the heights of neighboring columns.

## The minimum-filter description

**Theorem.** A skyline `c` of width `w` on `{1, …, h}` has tower spacing at least `g` exactly when the array `b = c − 1`, with entries in `{0, …, h − 1}`, is the window-`g` running minimum of an array `a` of length `w + g − 1` over `{0, …, h − 1}`: `b_i = min(a_i, …, a_{i+g−1})` for `i = 1, …, w`.

*Proof.* Thresholding commutes with the minimum, so for each level `r` the set `{i : b_i ≥ r}` is the erosion of `{i : a_i ≥ r}` by a window of length `g`. If `b_i ≥ r` and `b_j ≥ r` with `0 < j − i ≤ g`, the two windows overlap or abut, so `a ≥ r` on `[i, j + g − 1]` and `b_m ≥ r` for `i < m < j`; so every internal run of the complement has length at least `g`. Conversely, given `b` with every internal run at least `g` at every level, let `a` be the window-`g` running maximum of `b`, with indices clipped to `1, …, w`. The running minimum of `a` is the morphological closing of `b`, level by level, and closing by a window of length `g` changes a set only by filling internal runs of length less than `g`; `b` has none, so the closing returns `b`. ∎

Write `ε` for the window-`g` running minimum from arrays of length `w + g − 1` to arrays of length `w`, and `δ` for the clipped running maximum back. They are adjoint: `εa ≥ b` exactly when `a ≥ δb`, entrywise. So `εδε = ε` and `δεδ = δ`, and `ε` maps the image of `δ` one-to-one onto the image of `ε`, with inverse `δ`. The image of `ε` is the set of skylines with tower spacing at least `g`, by the Theorem. The image of `δ` is the set of arrays fixed by the opening `δε`: those in which every entry lies in a window of `g` consecutive entries that are all at least as large. Equivalently, every level set `{a ≥ r}`, `r = 1, …, h − 1`, has all its runs of length at least `g`: an entry `a_i = v` lies in such a window exactly when the run of `{a ≥ v}` that contains position `i` has length at least `g`, and a shorter run of some `{a ≥ r}` would leave its smallest entry in no such window. Hence `spacing_g(w, h)` counts both:

- the distinct outputs of a window-`g` minimum filter on `{0, …, h − 1}^{w+g−1}`, which Hardin counts on the OEIS as the arrays "with each element the minimum of k adjacent elements" of a longer random array, and, by the complement `x → h − 1 − x`, the outputs of a maximum filter, counted on the OEIS as the "arrays of maxima of three adjacent elements" at `g = 3` ([[castle-sequence-catalogue](pages/castle-sequence-catalogue.md)]);
- the arrays of length `w + g − 1` fixed by the opening, those whose level sets have all runs of length at least `g`. At `h = 2` these are the binary words whose runs of `1`s have length at least `g`. At `g = 2` they are the words in which every nonzero entry is at most one of its neighbors, with a virtual `0` beyond each end, the words counted by `W_{h−1}` on [[hardin-word-identity](pages/hardin-word-identity.md)]:

```
spacing_2(w, h)  =  W_{h−1}(w + 1).                                             (1)
```

With the Hardin word identity, `spacing_2(L, m + 1) = P_even(4m + 2, L) / 2^L`: the skylines of height at most `m + 1` with tower spacing at least 2 are counted by the even sector of the signed tower count at tower height `4m + 2`.[^5]

## The level-run recursion

Let `A_h(x) = Σ_n a_h(n) x^n` count the arrays over `{0, …, h − 1}` whose level sets have all runs of length at least `g`, by their length `n`, so that `spacing_g(w, h) = a_h(w + g − 1)` (section *The minimum-filter description*).

**Recursion.** Such an array is a sequence of 0s and maximal runs of nonzero entries, with a 0 between any two runs. Each run is a run of `{a ≥ 1}`, so it has length at least `g`, and subtracting 1 from its entries leaves an array over `{0, …, h − 2}` whose level sets again have all runs of length at least `g`; every such array of length at least `g` arises. An array shorter than `g` has no nonzero entry, so `a_{h−1}(n) = 1` for `n < g`, and the runs have generating function `K_h = A_{h−1} − (1 + x + ⋯ + x^{g−1})`. The words in 0s and runs with no two runs adjacent give

```
A_h  =  (1 + K_h) / (1 − x − x K_h),        A_1  =  1/(1 − x).                     (2)
```

**The matrix.** Write `A_h = N_h / D_h`, with `N_1 = 1` and `D_1 = 1 − x`. With `R = 1 + x + ⋯ + x^{g−1}`, `K_h = (N_{h−1} − R D_{h−1}) / D_{h−1}`, and since `1 − R = −xS` and `1 − x + xR = 1 + x²S`, Equation (2) advances the pair by one matrix:

```
( N_h )     (  1     −xS    ) ( N_{h−1} )
( D_h )  =  ( −x    1 + x²S ) ( D_{h−1} ),        S = 1 + x + ⋯ + x^{g−2}.          (3)
```

At `h = 2` it gives `A_2 = (1 − x + x^g)/((1 − x)² − x^{g+1})`, whose coefficients from `x^{g−1}` on are those of Equation (5) (section *Height 2*). At `(h, g) = (3, 2)`, `S = 1` and `D_3 = (1 + x²)(1 − 2x + x² − x³) − x(1 − x + x²) = 1 − 3x + 3x² − 4x³ + x⁴ − x⁵`, the reversal of `H_5` (section *The table*). At `g = 1`, `S = 0` and `D_h = 1 − hx`, the count `h^w` of all skylines.[^11]

**Theorem.** For every `h ≥ 1` and `g ≥ 2`, `N_h` and `D_h` are coprime and `D_h` has degree `(h − 1)g + 1`, so `spacing_g(·, h)` satisfies a linear recurrence of order `(h − 1)g + 1` and no shorter one.

*Proof.* The matrix of Equation (3) has determinant `(1 + x²S) − x²S = 1`, so its inverse has polynomial entries, and `(1, 1 − x)` is the inverse to the power `h − 1` applied to `(N_h, D_h)`; a common factor of `N_h` and `D_h` therefore divides 1. For the degrees, `deg N_h = deg D_h − 1` holds at `h = 1`, and if it holds at `h − 1`, then `(1 + x²S) D_{h−1}` has degree `deg D_{h−1} + g`, above the degree `deg D_{h−1}` of `x N_{h−1}`, so `deg D_h = deg D_{h−1} + g`, and `N_h = N_{h−1} − xS D_{h−1}` has degree `deg D_{h−1} + g − 1 = deg D_h − 1`. So `deg D_h = 1 + (h − 1)g`. The coefficients of the reduced fraction `N_h / D_h`, with `D_h(0) = 1`, satisfy the recurrence of `D_h` and no shorter one, and since the leading coefficient of `D_h` is nonzero, dropping the first `g − 1` of them does not shorten it. ∎

## Height 2

At `h = 2` a skyline is a binary string, `1` for a column of height 2, whose internal runs of `0`s have length at least `g`. With `k` runs of `1`s, the `k − 1` internal runs of `0`s have length at least `g` and the two end runs at least 0; removing `g − 1` from each internal run leaves the strings of length `w − (k − 1)(g − 1)` with `k` runs of `1`s, `C(w − (k − 1)(g − 1) + 1, 2k)` of them. So

```
spacing_g(w, 2)  =  Σ_{k ≥ 0} C(w + g − (g − 1)k, 2k).                         (4)
```

Equation (2) at `h = 2` has `K_2 = x^g/(1 − x)`, so `A_2 = (1 − x + x^g)/((1 − x)² − x^{g+1})`, and dropping its first `g − 1` coefficients gives the generating function

```
Σ_{w ≥ 0} spacing_g(w, 2) x^w  =  (1 + x² + x³ + ⋯ + x^g) / ((1 − x)² − x^{g+1}).   (5)
```

Its coefficients are positive, so the growth constant is `1/x_g` for the root `x_g` of `(1 − x)² = x^{g+1}` in `(0, 1)`. As `g` grows, `x^{g+1}` decreases on `(0, 1)`, so `x_g` increases toward 1, and the growth constant decreases toward 1.

For odd `g = 2j − 1`, the denominator is a difference of squares, `(1 − x − x^j)(1 − x + x^j)`, and the growth constant is the positive root of `y^j = y^{j−1} + 1`, from the first factor. For even `g ≤ 40` the denominator is irreducible (computed).[^3]

| `g` | denominator | growth | `spacing_g(w, 2)` |
|---|---|---|---|
| 2 | `1 − 2x + x² − x³` | `1.75488 = ψ²` | `A005251(w + 3)` |
| 3 | `(1 − x − x²)(1 − x + x²)` | `1.61803 = φ` | `A005252(w + 3)` |
| 4 | `1 − 2x + x² − x⁵` | `1.52895` | `A005253(w + 3)` |
| 5 | `(1 − x − x³)(1 − x + x³)` | `1.46557`, the supergolden ratio, `y³ = y² + 1` | `A005689(w + 6)` |
| 6 | `1 − 2x + x² − x⁷` | `1.41780` | `A098574(w + 6)` |
| 7 | `(1 − x − x⁴)(1 − x + x⁴)` | `1.38028`, `y⁴ = y³ + 1` | `A217838(w)` |

`ψ` is the plastic number, and `x³ − 2x² + x − 1`, the reversal of the `g = 2` denominator, is the minimal polynomial of `ψ²` ([[plastic-number](pages/plastic-number.md)]). The OEIS entries of the table carry Equation (4) as binomial sums, and `A005253` counts "binary words of length n in which the ones occur only in blocks of length at least 4".[^4] By the Theorem of section *The minimum-filter description*, `spacing_g(w, 2)` is also the number of binary words of length `w + g − 1` whose runs of `1`s all have length at least `g`.

These words are the strings with no run of 1s of length 1 to `g − 1` in [[balado-silvestre-2026-runs-binary-strings](pages/balado-silvestre-2026-runs-binary-strings.md)], a census of runs in binary strings, which finds them in the OEIS as A005251, A005252, A005253, A005689, A098574 and A217838 for `g = 2, …, 7`, at the shifts of the table above. A217838 fills the row `g = 7`: `spacing_7(w, 2) = A217838(w)`, whose generating function has the denominator `(1 − x + x⁴)(1 − x − x⁴)`. Hardin's table A217839, "Number of n element 0..1 arrays with each element the minimum of k adjacent elements of a random 0..1 array of n+k-1 elements", is the whole row `h = 2`: `T(w, g) = spacing_g(w, 2)`, with the columns 2 to 6 at the shifts above.[^8][^9][^10]

**Castles by semi-perimeter.** Subtracting the all-zero word, `spacing_h(s − h, 2) − 1` counts the castles of height `h` with every column 1 or `h` and semi-perimeter `s`: lengthening each run of height-`h` columns by `h − 1` columns sends them one-to-one onto the nonzero words of length `s − 1` whose runs of 1s are all at least `h` long ([[balado-silvestre-2026-runs-binary-strings](pages/balado-silvestre-2026-runs-binary-strings.md)], section *The castle reading*). So the denominator `(1 − x)² − x^{g+1}` at `g = h` is the one that [[semi-perimeter-growth-census](pages/semi-perimeter-growth-census.md)] gives for the castles on the two heights 1 and `h`, and the growth constants by semi-perimeter of the `{1, 3}` castles (golden) and of all castles of height 2 (`ψ²`) are those of this table at `g = 3` and `g = 2`.[^10]

## The transfer matrix

A second count, which checks the recursion, reads the skyline one column at a time. For each row `r = 2, …, h` the state records one of: no filled cell yet in the row, or a run of at least `g` empty cells since the last filled one (a filled cell may follow); the last column filled the row; or `k` empty cells since the last filled one, `1 ≤ k < g` (a filled cell may not follow). A column of height `c` fills the rows `r ≤ c`; it is forbidden when it fills a row in a state of the third kind. For `2 ≤ h, g ≤ 6` the reachable states number `C(h + g − 1, g)`, from 3 at `(2, 2)` to 462 at `(6, 6)`, so `spacing_g(·, h)` satisfies a linear recurrence of at most that order; the recursion gives the exact order, `(h − 1)g + 1`. The counts agree with enumeration of all skylines for `(h, g)` in `{(2, 2), (2, 3), (3, 2), (3, 3), (3, 4), (4, 2), (4, 3)}` and `w ≤ 7`.[^2] The snippet `tower_spacing_matrix(h, g)` on [[castle-snippets-strips](pages/castle-snippets-strips.md)] builds the matrix.

## The table

Growth constants, the largest roots of the minimal recurrences:[^6]

| `h \ g` | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|
| 2 | 1.7549 | 1.6180 | 1.5289 | 1.4656 | 1.4178 |
| 3 | 2.4022 | 2.1069 | 1.9274 | 1.8051 | 1.7157 |
| 4 | 2.9972 | 2.5398 | 2.2733 | 2.0966 | 1.9697 |
| 5 | 3.5589 | 2.9392 | 2.5888 | 2.3608 | 2.1991 |
| 6 | 4.0967 | 3.3154 | 2.8839 | 2.6069 | 2.4123 |

- **Minimal recurrence order.** The shortest linear recurrence of `spacing_g(·, h)` has order `(h − 1)g + 1` at every `h` and `g ≥ 2` (section *The level-run recursion*). In every cell with `2 ≤ h, g ≤ 6`, Berlekamp-Massey finds the same order from 100 terms, and the found recurrence holds on (states + order + 5) terms, where the states number `C(h + g − 1, g)`. At `(3, 3)` and `(4, 3)` these are the recurrences that A217878 and A217949 list as "Empirical", coefficient for coefficient, so those hold.
- **No metallic growth for `h ≥ 3`.** For `3 ≤ h ≤ 6` and `2 ≤ g ≤ 6`, the minimal polynomial of the growth constant has degree at least 4, while every metallic mean `σ_p^q` has degree at most 2 ([[metallic-means](pages/metallic-means.md)]). At `(3, 2)` the growth `2.40221` is the largest root of `x⁵ − 3x⁴ + 3x³ − 4x² + x − 1`, the polynomial `H_5` of [[hardin-word-identity](pages/hardin-word-identity.md)], just below the silver mean `2.41421`. At `h = 2` the growth constant is the golden mean `φ = σ_1^1` at `g = 3`; at `g = 2` and `g = 5` it is the cubic `ψ²` or the supergolden ratio.
- **The limit `g → ∞`.** For `w ≤ g + 1` an internal run of length at least `g` does not fit between two filled cells, so the rule forbids every internal run and the skylines are the unimodal ones ([[weakly-unimodal-composition](pages/weakly-unimodal-composition.md)]); at `w = g + 2` the skyline `(2, 1, …, 1, 2)` is allowed and not unimodal. So `spacing_g(w, h)` equals the number of unimodal skylines exactly for `w ≤ g + 1` (at `h = 2` the unimodal count is `1 + C(w + 1, 2)`, `A000124`).

## OEIS

The cells with `2 ≤ h, g ≤ 6`, with `spacing_g(w, h) = a(w)` where no shift is written:[^7]

| `h \ g` | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|
| 2 | A005251`(w+3)` | A005252`(w+3)` | A005253`(w+3)` | A005689`(w+6)` | A098574`(w+6)` |
| 3 | A202882`(w+1)` | A217878 | A217879 | A217880 | A217881 |
| 4 | A203094`(w+1)` | A217949 | A217950 | A217951 | A217952 |
| 5 | A203184`(w+1)` | A228457 | - | - | - |
| 6 | A203050`(w+1)` | A228458 | - | - | - |

Hardin's two-dimensional tables are the rows `h = 2` (A217839, "0..1 arrays"), `h = 3` (A217883, "0..2 arrays with each element the minimum of k adjacent elements") and `h = 4` (A217954) and the column `g = 3` (A228461, "arrays of maxima of three adjacent elements"). The column `g = 2` is Hardin's words with no strict local maximum (Equation (1)). The cells marked `-` in the table above have these first terms:

| cell | `spacing_g(w, h)` for `w = 1, …, 10` | growth | order |
|---|---|---|---|
| `(5, 4)` | `5, 25, 95, 295, 791, 1927, 4496, 10606, 26290, 68711` | `2.58882` | 17 |
| `(5, 5)` | `5, 25, 95, 295, 791, 1897, 4196, 8848, 18502, 39962` | `2.36081` | 21 |
| `(5, 6)` | `5, 25, 95, 295, 791, 1897, 4166, 8548, 16744, 32174` | `2.19911` | 25 |
| `(6, 4)` | `6, 36, 161, 581, 1792, 4955, 12889, 33279, 89509, 255685` | `2.88388` | 21 |
| `(6, 5)` | `6, 36, 161, 581, 1792, 4900, 12229, 28681, 65485, 151801` | `2.60694` | 26 |
| `(6, 6)` | `6, 36, 161, 581, 1792, 4900, 12174, 28021, 60887, 127777` | `2.41234` | 31 |

## Appearances in Sources

- [[pe502-pell-castle-strip](pages/pe502-pell-castle-strip.md)] - the note that reads rule 3's gap as an atom of width 2 in the Pell generating function; the rule of this page raises the gap to `g`.

## Related Concepts

- [[hardin-word-identity](pages/hardin-word-identity.md)] - the words `W_m` of Equation (1), and `P_even(4m + 2, L) = 2^L W_m(L + 1)`.
- [[castle-sequence-catalogue](pages/castle-sequence-catalogue.md)] - every cell.
- [[weakly-unimodal-composition](pages/weakly-unimodal-composition.md)] - the unimodal skylines, the limit `g → ∞`.
- [[castle-strip](pages/castle-strip.md)] and [[metallic-strip-realizability](pages/metallic-strip-realizability.md)] - skylines counted under rules on the heights of neighboring columns, and the growth constants those rules reach.
- [[reachable-field-census](pages/reachable-field-census.md)] - the growth constants reachable by rules on neighboring heights.
- [[plastic-number](pages/plastic-number.md)] - `ψ²`, the growth at `(h, g) = (2, 2)`.
- [[tree-castle-by-area](pages/tree-castle-by-area.md)] and [[a005251-bijection](pages/a005251-bijection.md)] - the other castle readings of A005251; the gap map followed by the complement sends the tree castles of area `n` one-to-one onto the skylines of width `n − 1` at `h = 2`, `g = 2`.
- [[pell-castle-strip](pages/pell-castle-strip.md)] - the 1-smooth strips on `{1, 2, 3}`, silver by width.
- [[castle-classification-shape](pages/castle-classification-shape.md)] - the shape types, among them the m-smooth and m-disparate rules on neighboring heights.
- [[castle-snippets-strips](pages/castle-snippets-strips.md)] - the snippet `tower_spacing_matrix(h, g)`.
- [[balado-silvestre-2026-runs-binary-strings](pages/balado-silvestre-2026-runs-binary-strings.md)] - the binary words of the row `h = 2` as strings with no short run of 1s, and their OEIS entries through `g = 7`.
- [[golden-silver-bronze-plastic-castles](pages/golden-silver-bronze-plastic-castles.md)] and [[semi-perimeter-growth-census](pages/semi-perimeter-growth-census.md)] - the castles on the heights 1 and `h` by semi-perimeter, counted by `spacing_h(s − h, 2) − 1`.

## Footnotes

[^1]: The rule on the skyline: for every level `r ∈ {2, …, h}`, the indicator string `(𝟙[c_i ≥ r])_{i=1..w}`, with its leading and trailing zeros removed, contains no run of zeros shorter than `g`. At `g = 1` this holds for every skyline.
[^2]: Verified by execution (Python 3.11, 2026-10-16): the column-by-column dynamic program over the per-row states against enumeration of all `h^w` skylines for the listed cells and `w ≤ 7`, for example `spacing_2(w, 3) = 3, 9, 22, 51, 121, 292, 704`; the reachable state counts for `2 ≤ h, g ≤ 6`.
[^3]: Verified by execution (Python 3.11 with SymPy, 2026-10-16): Equation (4) against the dynamic program for `2 ≤ g ≤ 7`, `w ≤ 16`; the factorization `(1 − x)² − x^{2j} = (1 − x − x^j)(1 − x + x^j)` for `j ≤ 9`, with the root of smallest modulus in the first factor for `j ≤ 5`; irreducibility of `(1 − x)² − x^{g+1}` for even `g ≤ 40`; the growth constants for `g ≤ 7`.
[^4]: https://oeis.org/A005252, https://oeis.org/A005253, https://oeis.org/A005689, https://oeis.org/A098574 (read 2026-10-16) - "a(n) = Sum_{k=0..floor(n/4)} binomial(n-2k,2k)", "Number of binary words of length n in which the ones occur only in blocks of length at least 4", "Number of Twopins positions", "a(n) = Sum_{k=0..floor(n/7)} C(n-5*k,2*k)"; the data fields agree with `spacing_g(w, 2)` at the stated shifts for 35 to 39 terms.
[^5]: Verified by execution (Python 3.11, 2026-10-16): Equation (1) against brute-force counts of Hardin's words for `2 ≤ h ≤ 5`, `w ≤ 6`; the binary words of length `w + g − 1` with every run of `1`s at least `g` against Equation (4) for `2 ≤ g ≤ 6`, `w ≤ 8`.
[^6]: Verified by execution (Python 3.11 with SymPy, 2026-10-16): `spacing_g(w, h)` for `2 ≤ h, g ≤ 6` and `w ≤ 100` by the dynamic program; Berlekamp-Massey over the rationals gives order `(h − 1)g + 1` in every cell, and the recurrence holds on `C(h + g − 1, g) + (h − 1)g + 6` terms (up to 498 at `(6, 6)`); the growth constant as the largest root of the recurrence polynomial and the degree of its irreducible factor (2 at `(2, 3)`, 3 at `(2, 2)` and `(2, 5)`, at least 4 for `h ≥ 3`); the recurrences of A217878 (`3, −3, 1, 3, −1, 1, 1`) and A217949 (`4, −6, 4, 5, −4, 6, 4, 0, 2, 1`) equal the computed ones; the unimodal comparison for `h ≤ 4`, `g ≤ 5`.
[^7]: https://oeis.org (read 2026-10-16) - the data fields of A202882, A203094, A203184, A203050, A217878 to A217881, A217949 to A217952, A228457 and A228458 agree with `spacing_g(w, h)` at the stated shifts for every listed term (22 to 33 terms); A217883 and A217954 are "T(n,k) = number of n-element 0..2 [0..3] arrays with each element the minimum of k adjacent elements of a random 0..2 [0..3] array of n+k-1 elements", and A228461 is "T(n,k) = number of arrays of maxima of three adjacent elements of some length n+2 0..k array".
[^8]: [[balado-silvestre-2026-runs-binary-strings](pages/balado-silvestre-2026-runs-binary-strings.md)] §2.4.4 p.24 L1169-1176 - "w≤1 (n − 2, 0) = w1 (n − 2, 0) is A005251 for n ≥ 2", "w≤2 (n − 1, 0) is A005252 for n ≥ 1", "w≤3 (n, 0) is A005253", "w≤4 (n − 2, 0) is A005689 (number of Twopins positions) for n ≥ 6", "w≤5 (n − 1, 0) is A098574 for n ≥ 1", "w≤6 (n + 6, 0) is A217838", where `w_{≤k}(n, 0)` counts the `n`-strings with no nonnull run of length at most `k`.
[^9]: https://oeis.org/A217838 and https://oeis.org/A217839 (read 2026-10-25) - A217838 "Number of n element 0..1 arrays with each element the minimum of 7 adjacent elements of a random 0..1 array of n+6 elements", offset 0, data `1, 2, 4, 7, 11, 16, 22, 29, 37, 47, 61, 82, …`, g.f. `(x^7+x^6+x^5+x^4+x^3+x^2+1)/((1 - x + x^4)*(1 - x - x^4))`, "Column 7 of A217839"; A217839 "T(n,k)=Number of n element 0..1 arrays with each element the minimum of k adjacent elements of a random 0..1 array of n+k-1 elements", "Column 2 is A005251(n+3)" through "Column 6 is A098574(n+6)".
[^10]: Verified by execution (Python 3.11 with SymPy, 2026-10-25): `spacing_7(w, 2)` against A217838 for `w ≤ 16`; every listed term of A217839 (the antidiagonals through `n + k = 12`) against `spacing_k(n, 2)`; the lengthening map, a bijection from the castles of height `h` with every column 1 or `h` and semi-perimeter `s` onto the nonzero binary words of length `s − 1` with every run of 1s at least `h` long, for `h ≤ 5`, `s ≤ 14`, and the count `spacing_h(s − h, 2) − 1` for `h ≤ 9`, `s ≤ h + 11`.
[^11]: Verified by execution (Python 3.11 with SymPy, 2026-10-26): Equation (2) against the dynamic program of section *The transfer matrix* for `2 ≤ h, g ≤ 5` and `w ≤ 40`; Equation (3), the coprimality of `N_h` and `D_h`, and `deg D_h = (h − 1)g + 1` for `2 ≤ h, g ≤ 7`; `D_3` at `g = 2`.
