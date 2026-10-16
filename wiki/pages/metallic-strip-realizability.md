---
title: Which metallic means are castle-strip growth constants
category: Analyses
summary: The growth constant of a castle strip is the spectral radius of its 0/1 transfer matrix M on the heights 1, …, h, and its width generating function has a denominator dividing det(I − xM). A quadratic denominator 1 − p₁x − p₂x² with p₁, p₂ ≥ 1 grows at de Spinadel's metallic mean σ_{p₁}^{p₂}, which is on the q = 1 row δ_a = σ_a^1 exactly when p₂ = 1. The five natural rules on three heights grow at 3, copper 2, σ_2^2 = 1 + √3, silver (the 1-smooth rule, denominator (1 − x)(1 − 2x − x²)) and 1. A 0/1 matrix on h heights has spectral radius at most h, so δ_a needs at least a + 1 heights; the ridge rule R_h = J − D, with characteristic polynomial (x + 1)^{h−2}(x² − (h−1)x − 1), reaches δ_{h−1} at height h, so bronze first appears at height 4. At height 5 the ridge strips are the Fibonacci numbers F_{3w+2}, since δ_4 = φ³.
tags: [analysis, castle, ridge-castle, metallic-mean, growth-constant, transfer-matrix, perron-root, bronze, silver, fibonacci-decimation, realizability, sympy, verification]
sources: [pe502-pell-castle-strip, de-spinadel-1999-family-of-metallic-means]
created: 2026-09-18
updated: 2026-10-16
---

# Which metallic means are castle-strip growth constants

## The question

A **castle strip** on the heights `1, …, h` is a skyline in `{1, …, h}^w` under a rule that says which column height may follow which ([[castle-strip](pages/castle-strip.md)]). A strip need not reach `h`, so it is not a castle of height `h`. The rule is a 0/1 **transfer matrix** `M`, with rows and columns indexed by the heights and `M[a][b] = 1` when a column of height `a` may be followed by one of height `b`. The strips of width `w` number `𝟙ᵀ M^{w−1} 𝟙`, with `𝟙` the all-ones vector. Their width generating function `𝟙ᵀ (I − xM)^{−1} 𝟙` is rational, and by Cramer's rule its denominator divides `det(I − xM)`. The sum of the entries of `M^n` is a matrix norm, so by Gelfand's formula `𝟙ᵀ M^n 𝟙` grows like `ρ(M)^n`, where `ρ(M)` is the spectral radius, the Perron root of `M`.

The metallic means are de Spinadel's family `σ_p^q = (p + √(p² + 4q))/2`, the positive roots of `x² − px − q` for natural `p` and `q` ([[metallic-means](pages/metallic-means.md)], [[de-spinadel-1999-family-of-metallic-means](pages/de-spinadel-1999-family-of-metallic-means.md)]). Their `q = 1` row is `δ_a = σ_a^1 = (a + √(a² + 4))/2`: golden at `a = 1`, silver at `a = 2`, bronze at `a = 3`. This page asks which metallic means are growth constants of strips, and at which height.

## Quadratic denominators

A strip whose width generating function has the quadratic denominator `1 − p₁x − p₂x²`, with `p₁, p₂ ≥ 1`, grows at the larger root of `x² − p₁x − p₂`, the metallic mean `σ_{p₁}^{p₂}`. It is on the `q = 1` row exactly when `p₂ = 1`, and then it is `δ_{p₁}`. The Pell denominator `1 − 2x − x²` of [[pell-castle-strip](pages/pell-castle-strip.md)] has `p₁ = 2`, `p₂ = 1`, silver. Read as a tiling scheme, `p₁` is the number of kinds of atom of width 1 and `p₂` the number of kinds of atom of width 2; neither is a number of heights. No 0/1 rule on two heights has the denominator `1 − 2x − x²` ([[pell-castle-strip](pages/pell-castle-strip.md)]).

On three heights, the five natural rules give:[^1]

| rule on the heights `1, 2, 3` | `b` may follow `a` when | `det(I − xM)` | growth `ρ(M)` | metallic mean |
|---|---|---|---|---|
| all pairs | always | `1 − 3x` | `3` | `σ_1^6 = σ_2^3` |
| plateau-free | `a ≠ b` | `(1 − 2x)(1 + x)²` | `2` | copper `σ_1^2` |
| no two ceiling columns | not `a = b = 3` | `1 − 2x − 2x²` | `1 + √3 ≈ 2.732` | `σ_2^2` |
| 1-smooth | `|a − b| ≤ 1` | `(1 − x)(1 − 2x − x²)` | `1 + √2 ≈ 2.414` | silver `σ_2^1` |
| weakly increasing | `a ≤ b` | `(1 − x)³` | `1` | none |

Only the 1-smooth rule has a quadratic factor with `p₂ = 1`.

## The 1-smooth rule on three heights: silver

The 1-smooth rule `|c_{i+1} − c_i| ≤ 1` on three heights has `det(I − xM) = (1 − x)(1 − 2x − x²)`,[^2] so it grows at silver, `1 + √2`. `M` is symmetric, its eigenvector for the eigenvalue 1 is `(1, 0, −1)`, and this vector is orthogonal to `𝟙`, so the factor `1 − x` cancels from the generating function of the strips with a free last column. With the first column at height 1 these are the Pell castle strips, `P⋆_w` of width `w` ([[pell-castle-strip](pages/pell-castle-strip.md)]); with both end columns free they number the Pell-Lucas numbers `A001333(w + 1)`. The strips that reach height 3 are the Pell castles ([[pell-castle](pages/pell-castle.md)]).

Silver is also the growth of the tower words counted by length, which are silver by length ([[tower-word-continued-fraction](pages/tower-word-continued-fraction.md)]).

## The minimum height of `δ_a`

The spectral radius of a nonnegative matrix is at most its largest row sum, and a 0/1 matrix on `h` heights has row sums at most `h`. Since `δ_a > a`, a strip rule that grows at `δ_a` needs at least `a + 1` heights ([[quadratic-min-height](pages/quadratic-min-height.md)]). In particular bronze, `δ_3 = (3 + √13)/2 ≈ 3.303`, is not an eigenvalue of any 0/1 matrix of size at most 3. Of the `2^{16} = 65536` 0/1 matrices of size 4, exactly 192 have bronze as an eigenvalue, and each has 13 entries equal to 1.[^3]

## The ridge rule reaches every `δ_a`

The **ridge rule** at height `h` lets a column of height `b` follow one of height `a` when `a ≠ b` or `a = b = h`: neighboring columns differ in height unless both are at the ceiling ([[ridge-castle](pages/ridge-castle.md)]). Its transfer matrix is

```
R_h  =  J − D,          J the h × h all-ones matrix,   D = diag(1, …, 1, 0),
```

and its characteristic polynomial is[^4]

```
det(xI − R_h)  =  (x + 1)^{h−2} · (x² − (h − 1)x − 1).
```

[[ridge-castle](pages/ridge-castle.md)] proves it: the plane spanned by `𝟙` and the last unit vector `e_h` is invariant, and `R_h` acts on it by `[[h − 1, 1], [1, 0]]`, while every vector with coordinate sum 0 and last coordinate 0 has eigenvalue `−1`. So `ρ(R_h) = δ_{h−1}`, and the ridge rule reaches `δ_a` at height `a + 1`, the least height possible. At height 4:

```
R_4  =  [0 1 1 1]          det(xI − R_4)  =  (x + 1)²(x² − 3x − 1),
        [1 0 1 1]
        [1 1 0 1]          ridge strips of width w = 1, 2, 3, …:  4, 13, 43, 142, 469, 1549, 5116, …
        [1 1 1 1]
```

with ratio tending to bronze.[^5]

| `h` | growth `δ_{h−1}` | metallic mean | `x² − (h − 1)x − 1` |
|---|---|---|---|
| 2 | `φ ≈ 1.6180` | golden `δ_1` | `x² − x − 1` |
| 3 | `1 + √2 ≈ 2.4142` | silver `δ_2` | `x² − 2x − 1` |
| 4 | `(3 + √13)/2 ≈ 3.3028` | bronze `δ_3` | `x² − 3x − 1` |
| 5 | `2 + √5 ≈ 4.2361` | `δ_4` | `x² − 4x − 1` |
| 6 | `(5 + √29)/2 ≈ 5.1926` | `δ_5` | `x² − 5x − 1` |

Up to the factor `(1 + x)^{h−2}`, `det(I − xR_h)` is `1 − (h − 1)x − x²`, with `p₁ = h − 1` and `p₂ = 1`. At `h = 2` the ridge rule is the Fibonacci rule (no two neighboring columns of height 2) with the heights 1 and 2 exchanged ([[fibonacci-castle](pages/fibonacci-castle.md)]). At `h = 3` it is a different rule from the 1-smooth rule, with the same growth.

The ridge castles of height `h`, the ridge strips that reach `h`, are `δ_{h−1}` by width, and so are their even-block members: the signed transfer matrix `R̃_h` has spectral radius below `δ_{h−1}` for `h ≤ 6` ([[ridge-castle](pages/ridge-castle.md)], [[proper-castle-projection](pages/proper-castle-projection.md)]). With `x_n` the metallic sequence of order `h − 1` (`x_0 = 0`, `x_1 = 1`), the ridge strips number `x_{w+1} + x_w`: `A001333(w + 1)` at `h = 3`, `A003688(w + 1)` at `h = 4`, `A015448(w + 1)` at `h = 5`, while `x_n` itself is `A000129`, `A006190`, `A001076`.[^6]

### Height 5: every third Fibonacci number

`δ_4 = 2 + √5 = φ³`, since `φ³ = φ² + φ = 2φ + 1`.[^7] The metallic sequence of order 4 is `x_n = F_{3n}/2` (`A001076`), and `F_{3w+3} + F_{3w} = 2F_{3w+2}`, so the ridge strips of height 5 number

```
x_{w+1} + x_w  =  F_{3w+2}:   5, 21, 89, 377, 1597, 6765, 28657, …   (w = 1, 2, 3, …).
```

More generally `δ_a` is a power of `φ` exactly when `a` is a Lucas number `L_n` with `n` odd: `L_n² − 5F_n² = −4` for odd `n`, so `δ_{L_n} = (L_n + F_n√5)/2 = φ^n`. The cases are `a = 1, 4, 11, 29, 76, …`; bronze, in `Q(√13)`, is not among them.[^7]

## Other members of the family

Rules off the `q = 1` row give other metallic means:

- `σ_2^2 = 1 + √3`, in `Q(√3)`: the rule on three heights with no two neighboring ceiling columns, `p₂ = 2`;
- the integer `h − 1 = σ_1^{(h−1)(h−2)}`: the plateau-free rule `J − I` on `h ≥ 3` heights, copper `2` at `h = 3`.

[[reachable-field-census](pages/reachable-field-census.md)] lists which real quadratic fields arise from strip rules on at most five heights, and [[quadratic-min-height](pages/quadratic-min-height.md)] the least height of each quadratic growth constant.

## Appearances in Sources

- [[pe502-pell-castle-strip](pages/pe502-pell-castle-strip.md)] - the denominator `1 − 2x − x²` read as a tiling by an atom of width 1 in two kinds and an atom of width 2 in one kind.
- [[de-spinadel-1999-family-of-metallic-means](pages/de-spinadel-1999-family-of-metallic-means.md)] - the Metallic Means Family `σ_p^q`, the roots of `x² − px − q`, which contains every growth constant `(p₁ + √(p₁² + 4p₂))/2` of a quadratic denominator.

## Related Concepts

- [[ridge-castle](pages/ridge-castle.md)] - the ridge castles of height `h`, their counts and their even-block counts.
- [[metallic-means](pages/metallic-means.md)] - de Spinadel's family and its named members.
- [[pell-castle-strip](pages/pell-castle-strip.md)] - the silver denominator `1 − 2x − x²` and the anchored 1-smooth strips on three heights.
- [[castle-strip](pages/castle-strip.md)] - strips, transfer matrices and growth by width.
- [[castle-classification-growth](pages/castle-classification-growth.md)] - the growth types "X by width".
- [[castle-classification-shape](pages/castle-classification-shape.md)] - the plateau-free, 1-smooth and ridge types among the rate-of-change types.
- [[quadratic-min-height](pages/quadratic-min-height.md)], [[reachable-field-census](pages/reachable-field-census.md)] - the least height of each quadratic growth constant, and the fields that strip rules reach.
- [[eigenvalue-continued-fractions](pages/eigenvalue-continued-fractions.md)] - the purely periodic continued fractions of the `δ_a` and their fields `Q(√(a² + 4))`.
- [[castle-graph-spectral-radius](pages/castle-graph-spectral-radius.md)] - the metallic means as spectral radii of castle graphs, where the maximum degree 4 rules out `δ_4` and above.

## Footnotes

[^1]: Verified by execution (Python 3.11 with SymPy, 2026-10-16): for each rule, `M[i][j] = 1` when height `j + 1` may follow height `i + 1`, `det(I − xM)` factored, and `ρ(M)` the largest eigenvalue modulus. The table's denominators and growths are the output.
[^2]: SymPy `factor(det(I − xM))` for the 1-smooth rule on three heights gives `(x − 1)(x² + 2x − 1) = (1 − x)(1 − 2x − x²)`; `M(1, 0, −1)ᵀ = (1, 0, −1)ᵀ` checked.
[^3]: Verified by execution (Python 3.11 with NumPy, 2026-10-16): over all `2^9` 0/1 matrices of size 3, none has an eigenvalue within `10^{−9}` of `(3 + √13)/2`; over all `2^{16}` of size 4, exactly 192 do, each with 13 entries equal to 1; `[[0,0,0,1],[1,1,1,1],[1,1,1,1],[1,1,1,1]]` has characteristic polynomial `x²(x² − 3x − 1)`.
[^4]: Verified by execution (SymPy, 2026-10-16): `det(xI − R_h) − (x + 1)^{h−2}(x² − (h−1)x − 1)` expands to 0 for `h = 2, …, 6`.
[^5]: Verified by execution (SymPy, 2026-10-16): `factor(det(xI − R_4)) = (x + 1)²(x² − 3x − 1)`, and `𝟙ᵀ R_4^{w−1} 𝟙 = 4, 13, 43, 142, 469, 1549, 5116` for `w = 1, …, 7`.
[^6]: https://oeis.org/A001333, https://oeis.org/A003688, https://oeis.org/A015448, https://oeis.org/A000129, https://oeis.org/A006190, https://oeis.org/A001076 (read 2026-10-16) - A001333 "Pell-Lucas numbers: numerators of continued fraction convergents to sqrt(2)"; A003688 "a(n) = 3*a(n-1) + a(n-2), with a(1)=1 and a(2)=4"; A015448 "a(0) = 1, a(1) = 1, and a(n) = 4*a(n-1) + a(n-2) for n >= 2"; A000129 "Pell numbers"; A006190 "a(n) = 3*a(n-1) + a(n-2), with a(0)=0, a(1)=1"; A001076 "Denominators of continued fraction convergents to sqrt(5)".
[^7]: Verified by execution (Python 3.11 with SymPy, 2026-10-16): `φ³ − (2 + √5)` simplifies to 0; the ridge strips of height 5 equal `F_{3w+2}` for `w ≤ 12`; `|(L_n + √(L_n² + 4))/2 − φ^n| < 10^{−6}` for odd `n ≤ 11`, and the `a ≤ 200` with `a² + 4` equal to 5 times a square are `1, 4, 11, 29, 76, 199`.
