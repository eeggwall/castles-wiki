---
title: Fractional width and fractional height
category: Analyses
summary: A^e(w, h) is a sum of exponentials in the width and, for w <= 12 (computed), a quasi-polynomial in the height, so both arguments interpolate to real values. In the width, char_k has no negative real root for k <= 40, so on the principal branch of the logarithm A^e(w, h) is a real function of real w for h <= 41, and it is the only interpolant of exponential type below pi in the imaginary direction (Carlson's theorem); A^e(w, 2) = (2^{w+1} - 2^{(w+3)/2} cos(pi(w+1)/4))/4. In the height the only eigenvalues are +1 and -1, and -1 lies on the branch cut: the principal branch gives the complex values A^e(w, m + 1/2) = (A - B_w(h-1) + B_w(h-2))/2 + i(-1)^m (A_w(h-1) + A_w(h-2))/2, for example A^e(4, 2.5) = 16.75 + 6i, the conjugate branch gives their conjugates, and cos(pi k) gives a real interpolant; all three have type pi, so none is singled out. The half-column problem R^2 = M: 8, 88, 3245 rules at heights 2, 3, 4 are squares of 0/1 rules (A226321); 13, 261, 15418 have all eigenvalues real and nonnegative (A086510); 3, 25, 543 have all eigenvalues positive (A003024, I + N with N a DAG); among those, the rules whose principal square root has nonnegative entries are exactly the partial orders, 3, 19, 219, 4231 at heights 2 to 5 (A001035). The 1-smooth strip and every ridge rule J - D have a simple negative eigenvalue and so no real square root.
tags: [analysis, castle, fractional-calculus, interpolation, matrix-power, branch-cut, quasi-polynomial, c-finite, eigenvalues, transfer-matrix, square-root, embedding, metallic-means, computation, verification]
sources: [project-euler-502-solution]
created: 2026-09-19
updated: 2026-10-16
---

# Fractional width and fractional height

The count `A^e(w, h)` of even-block castles of width `w` and height `h` (the problem statement's `F(w, h)`; [[castle-counting-function](pages/castle-counting-function.md)]) is defined for integers, but its closed form is built from functions that make sense at real arguments. In the width it is a sum of exponentials `c_j lambda_j^w` in the eigenvalues of a transfer matrix, and `lambda^w = exp(w log lambda)` makes sense for real `w` once a branch of `log lambda` is chosen. In the height it is `(-1)^h` times a polynomial plus a polynomial, and `(-1)^h` can likewise be written `exp(h log(-1))`. This page interpolates both arguments and locates the difference between them in the eigenvalue `-1`. It then asks which strip rules `M` are the square of another rule `R`.

## What is being interpolated

The closed form is ([[castle-counting-formula](pages/castle-counting-formula.md)], Equation (1))[^1]

```
A^e(w, h)  =  [ h^w - (h - 1)^w - P(h - 1, w) + P(h - 2, w) ] / 2,
```

with `P(k, L) = sum (-1)^{blocks}` over towers of height at most `k` on a base of length `L`. The count `A(w, h) = h^w - (h - 1)^w` of all castles is a difference of two exponentials with positive bases in `w` and a polynomial in `h`. The signed tower count satisfies a linear recurrence in each variable. In `L` it has order `k + 1` and characteristic polynomial `char_k` ([[signed-tower-count](pages/signed-tower-count.md)]). In `k`, for `4 <= L <= 12` (computed), it has characteristic polynomial `(x + 1)^L (x - 1)^{L - 2}`, so `P(k, L) = (-1)^k A_L(k) + B_L(k)` with `A_L`, `B_L` polynomials ([[signed-tower-k-direction](pages/signed-tower-k-direction.md)]).[^2]

## Fractional width: real on the principal branch

Here `P(k, w)` is `P(k, L)` at base length `L = w` ([[castle-notation](pages/castle-notation.md)]). For `k <= 8` the roots `lambda_j` of `char_k` are distinct, and `P(k, w) = sum_j c_j lambda_j^w` for every integer `w >= 0`, with the coefficients `c_j` fixed by the first `k + 1` values. Interpolating means evaluating `lambda_j^w = exp(w log lambda_j)` with the principal logarithm, `-pi < arg lambda_j <= pi`. Whether the result is real depends on the signs of the roots:[^exec]

| `k` | degree | positive real roots | negative real roots | complex pairs | factorization of `char_k` |
|---|---|---|---|---|---|
| 1 | 2 | none | none | 1 | `x^2 - 2x + 2` |
| 2 | 3 | `2` | none | 1 | `(x - 2)(x^2 - x + 2)` |
| 3 | 4 | none | none | 2 | irreducible |
| 4 | 5 | `2.7963` | none | 2 | `(x^2 - 2x + 4)(x^3 - 3x^2 + 2x - 4)` |
| 5 | 6 | none | none | 3 | irreducible |
| 6 | 7 | `3.5098` | none | 3 | `(x^3 - 4x^2 + 4x - 8)(x^4 - 3x^3 + 8x^2 - 4x + 8)` |
| 7 | 8 | none | none | 4 | irreducible |
| 8 | 9 | `4.1740` | none | 4 | `(x^4 - 4x^3 + 12x^2 - 8x + 16)(x^5 - 5x^4 + 8x^3 - 20x^2 + 8x - 16)` |

For every `k <= 40`, `char_k` has no real root when `k` is odd and exactly one, positive, when `k` is even (exact root counts).[^exec] So no `char_k` with `k <= 40` has a negative real root. The complex roots come in conjugate pairs with conjugate coefficients, and on the principal branch `lambda^w` and `conj(lambda)^w` are conjugate for every real `w`, so their sum is real. Therefore **`P(k, w)` is a real function of real `w` for every `k <= 40`, and so is `A^e(w, h)` for every `h <= 41`.** For `k <= 8` the imaginary part at `w = 2.5, 3.5, 4.5, 5.5` is below `10^{-40}`, and the interpolant reproduces the integer values to `10^{-33}` for `L <= 11` (40-digit arithmetic).[^exec]

**Carlson's theorem** says that an entire function of exponential type that grows at most like `e^{c|y|}` on the imaginary axis for some `c < pi`, and vanishes at every nonnegative integer, is identically zero.[^3] The principal-branch interpolant `sum_j c_j exp(w log lambda_j)` grows like `e^{c|y|}` along `w = iy` with `c = max_j |arg lambda_j| < pi`, since no root is a negative real. Two interpolants of type below `pi` differ by a function of type below `pi` that vanishes at the integers, so the principal one is the only interpolant of type below `pi`. Other branches, `log lambda + 2 pi i n` for a complex root and `log conj(lambda) - 2 pi i n` for its conjugate, keep the interpolant real but add terms of type at least `pi` that vanish at the integers.

The height-2 case is explicit. The Solution derives `P(1, L) = Re((1 + i)^{L+1})` from the eigenvalues `1 +- i` of the `2 x 2` signed matrix,[^4] and `(1 + i)^n = 2^{n/2} e^{i pi n / 4}`, so

```
A^e(w, 2)  =  (2^w - P(1, w)) / 2  =  ( 2^{w+1} - 2^{(w+3)/2} cos(pi (w + 1) / 4) ) / 4,
```

which is `1, 3, 6, 10, 16, 28, 56, 120` at `w = 1, ..., 8` and `4.382` at `w = 2.5`. The cosine is the conjugate pair `(1 +- i)^{w+1}`; it gives the signs of `P(1, w)` their period 8 in the width ([[signed-tower-count](pages/signed-tower-count.md)]).

The interpolated values on the principal branch for `h = 2, ..., 6`:[^exec]

| `h` | `w = 2` | `2.5` | `3` | `3.5` | `4` | `4.5` | `5` |
|---|---|---|---|---|---|---|---|
| 2 | 3 | 4.382 | 6 | 7.854 | 10 | 12.601 | 16 |
| 3 | 0 | 0.689 | 3 | 8.744 | 21 | 44.894 | 89 |
| 4 | 7 | 15.235 | 31 | 60.707 | 117 | 225.533 | 439 |
| 5 | 0 | 1.742 | 10 | 38.456 | 122 | 345.039 | 906 |
| 6 | 11 | 29.912 | 76 | 185.918 | 448 | 1080.352 | 2630 |

A castle `(a, b)` of width 2 has `max(a, b) = h` blocks, so `A^e(2, h) = 0` for odd `h` and `A^e(2, h) = A(2, h) = 2h - 1` for even `h`; the table passes through these values.

## Fractional height: complex on the principal branch

In the height the only eigenvalues are `+1` and `-1`, and for `2 <= L <= 8`, `P(k, L) = (-1)^k A_L(k) + B_L(k)` for every `k >= 0`, with `A_L` of degree `L - 1`, `B_L = 0` for `L <= 3`, and `B_L` of degree `L - 3` for `L >= 4` (fitted on even and odd `k` separately and checked for `k <= 33`).[^5] The first cases are

```
A_2 = k + 1,   A_3 = (k + 1)^2,   A_4 = (k + 1)(2k + 1)(2k + 3) / 6,   B_4 = (k + 1) / 2,
A_5 = k (k + 1)^2 (k + 2) / 3,    B_5 = (k + 1)^2.
```

On the principal branch `log(-1) = i pi`, so `(-1)^k = e^{i pi k}`, which is `i (-1)^m` at `k = m + 1/2`, and

```
P(m + 1/2, L)  =  B_L(m + 1/2)  +  i (-1)^m A_L(m + 1/2).
```

The values:[^exec]

| `L` | `P(1/2, L)` | `P(3/2, L)` | `P(5/2, L)` |
|---|---|---|---|
| 2 | `1.5 i` | `-2.5 i` | `3.5 i` |
| 3 | `2.25 i` | `-6.25 i` | `12.25 i` |
| 4 | `0.75 + 2 i` | `1.25 - 10 i` | `1.75 + 28 i` |
| 5 | `2.25 + 0.9375 i` | `6.25 - 10.9375 i` | `12.25 + 45.9375 i` |
| 6 | `4 + 0.1875 i` | `20 - 8.3125 i` | `56 + 56.4375 i` |

In the closed form, with `h = m + 1/2`, `h - 1 = (m - 1) + 1/2` and `h - 2 = (m - 2) + 1/2`:

```
A^e(w, m + 1/2)  =  [ A(w, h) - B_w(h - 1) + B_w(h - 2) ] / 2   +   i (-1)^m [ A_w(h - 1) + A_w(h - 2) ] / 2.
```

At width 4, `A^e(4, 2.5) = 16.75 + 6 i`, `A^e(4, 3.5) = 55.25 - 19 i` and `A^e(4, 4.5) = 129.75 + 44 i`, against `A(4, h) = 34, 111, 260`.[^exec] The imaginary part at `h = 2.5` is `(A_4(3/2) + A_4(1/2))/2 = (10 + 2)/2 = 6`. The real part carries `A` and the polynomials `B_w`, the imaginary part the polynomials `A_w`.

The principal branch is a choice. The conjugate branch `log(-1) = -i pi` gives the complex conjugate of every value above, and the average of the two branches, `(-1)^k -> cos(pi k)`, gives the real interpolant `A_L(k) cos(pi k) + B_L(k)`. The three interpolants of `(-1)^k` differ by multiples of `sin(pi k)`, which vanishes at the integers, and all three have type exactly `pi` on the imaginary axis, so Carlson's theorem singles out none of them.

## Why the two directions differ

The difference is the location of the eigenvalues relative to the branch cut of the logarithm, the negative real axis. In the width, the eigenvalues of `A(w, h)` are `h` and `h - 1`, and those of the signed towers are the roots of `char_k`: one positive real root or none, and complex pairs, but no negative real root for `k <= 40`. Every eigenvalue lies off the cut, so the principal branch gives a real interpolant, and Carlson's theorem makes it the only one of type below `pi`. In the height, `A(w, h)` is a polynomial, but the signed towers have the eigenvalue `-1`, on the cut, carrying the polynomial `A_L`. Each branch of `log(-1)` gives a complex interpolant, a real one needs the average of two branches, and no interpolant is singled out by its type.

## The half-column problem

Is the strip rule `M` ([[castle-strip](pages/castle-strip.md)]) two steps of another rule `R`, `R^2 = M`? If so, a strip of width `w` under `M` is a strip of width `2w - 1` under `R` read at every other column, and `R` is a **half-column** rule. Exhaustively for small heights:[^exec]

| height | 0/1 rules | squares of a 0/1 rule | all eigenvalues real and `>= 0` | all eigenvalues real and `> 0` | of those, principal square root with nonnegative entries |
|---|---|---|---|---|---|
| 2 | 16 | 8 | 13 | 3 | 3 |
| 3 | 512 | 88 | 261 | 25 | 19 |
| 4 | 65536 | 3245 | 15418 | 543 | 219 |
| 5 | | | | 29281 | 4231 |
| OEIS | | A226321 | A086510 | A003024 | A001035 |

The eigenvalue columns are exact (real roots of the integer characteristic polynomials, with multiplicity). All four columns are OEIS sequences:[^6][^7][^8][^9]

- **Squares of 0/1 rules** are A226321, the 0/1 matrices that are squares of 0/1 matrices. These are the rules that are two steps of a 0/1 rule in which any two heights are joined by at most one two-step path.
- **All eigenvalues real and nonnegative** is A086510. A real matrix none of whose real eigenvalues is negative or zero has a real square root,[^10] which covers the rules of the next column but not those with an eigenvalue 0.
- **All eigenvalues positive** is A003024, the number of acyclic digraphs (DAGs) on labeled vertices: McKay, Oggier, Royle, Sloane, Wanless and Wilf proved that the 0/1 matrices with all eigenvalues positive real are exactly the matrices `I + N` with `N` the adjacency matrix of a DAG, and that all their eigenvalues are 1.[^8] For strips: every height may follow itself, and the other transitions form an acyclic graph.
- **Nonnegative half-column.** For `M = I + N` the principal square root is the finite sum `sqrt(I + N) = sum_k C(1/2, k) N^k`. Its entries are nonnegative for exactly 3, 19, 219, 4231 of these rules at heights 2 to 5, and these rules are exactly the partial orders on the heights (`M_ab = 1` iff `a <= b`, reflexive, antisymmetric and transitive), A001035, checked as sets in exact rational arithmetic.[^exec] The coefficient `C(1/2, 2) = -1/8` falls on every two-step chain `a < b < c`, and only a direct edge `a < c` contributes `+1/2` against it. The rule with `1 -> 3`, `2 -> 1` and all loops has a two-step chain without its closing edge, and its square root has `-1/8` at `(2, 3)`.

**The chain poset is the nondecreasing rule, and its half-column is the half-sum.** The total order `1 < 2 < ... < h` is the rule "the next column is at least as tall", with matrix the upper-triangular all-ones `U = (I - E)^{-1}`, `E` the superdiagonal shift. Then `U^{1/2} = (I - E)^{-1/2} = sum_k C(2k, k) 4^{-k} E^k`, a Toeplitz matrix whose weight for a jump of `k` heights is `1, 1/2, 3/8, 5/16, 35/128, 63/256, ...`, the coefficients of `(1 - x)^{-1/2}`, with denominators A046161 ([[fractional-block-count](pages/fractional-block-count.md)]). Two small posets: the `V` (`1 < 2`, `1 < 3`) has half-column weights `1/2` on both edges and nothing else; the diamond (`1 < 2 < 4`, `1 < 3 < 4`) has `1/2` on the four covering edges and `1/2 - 2 * (1/8) = 1/4` on the edge `1 < 4`.

**A negative simple eigenvalue excludes a real square root.** If `X` is real and `X^2 = M`, every eigenvalue `mu` of `X` with `mu^2 = lambda < 0` is `+- i sqrt(-lambda)`, and its conjugate `-mu` is an eigenvalue of `X` with the same multiplicity; both square to `lambda`, and no real eigenvalue of `X` does, so `lambda` has even multiplicity in `M`. The named strips:[^exec]

| strip | matrix | eigenvalues | real half-column |
|---|---|---|---|
| free strip, `h = 3` | `J` (all ones) | `3, 0, 0` | **yes**: `J / sqrt(3)` |
| no equal neighbors, `h = 3` | `J - I` | `2, -1, -1` | a real one; no nonnegative one |
| 1-smooth, `h = 3` | tridiagonal | `1 + sqrt 2, 1, 1 - sqrt 2` | **none**: simple negative eigenvalue |
| ridge, `h = 3` | `J - D` | `1 + sqrt 2, -0.4142, -1` | **none**: simple negative eigenvalues |
| ridge, `h = 4` | `J - D` | `3.3028, -0.3028, -1, -1` | **none**: simple negative eigenvalue |

The free strip has `J^2 = hJ`, so `J^{1/2} = J / sqrt(h)`, a rule in which every height may follow every height with weight `1 / sqrt(h)`, and `1^T (J / sqrt h)^{2(w-1)} 1 = 1^T h^{w-2} J 1 = h^w`. The matrix `J - I` is symmetric with eigenvalues `2, -1, -1`, so `J - I = Q diag(2, -1, -1) Q^T` with `Q` orthogonal, and `Q diag(sqrt 2, [[0, 1], [-1, 0]]) Q^T` is a real square root, since `[[0, 1], [-1, 0]]^2 = -I`. It has no nonnegative square root: if `R >= 0` and `R^2 = J - I`, the zero diagonal forces `R_ii = 0` and `R_ij R_ji = 0` for `i != j`; then `(R^2)_12 = R_13 R_32 = 1` and `(R^2)_21 = R_23 R_31 = 1` make `R_13` and `R_31` both positive, a contradiction.

The ridge rule `R_h = J - D` (neighboring columns differ in height unless both equal `h`) has characteristic polynomial `(x + 1)^{h - 2} (x^2 - (h - 1) x - 1)` ([[ridge-castle](pages/ridge-castle.md)], [[metallic-strip-realizability](pages/metallic-strip-realizability.md)]), whose quadratic factor has the simple negative root `-1 / delta_{h-1}`, different from `-1`. So **no ridge rule `R_h`, `h >= 2`, has a real square root.**

## Appearances in Sources

- [[project-euler-502-solution](pages/project-euler-502-solution.md)] - the closed form, the recurrences in both directions, the eigenvalues `1 +- i` and `P(1, L) = Re((1 + i)^{L+1})`, and `P(k, 2)`, `P(k, 3)` with their annihilators `(lambda + 1)^2`, `(lambda + 1)^3`.

## Related Concepts

- [[fractional-block-count](pages/fractional-block-count.md)] - the block count interpolated in the order of a difference, with the same `(1 - x)^{-1/2}` coefficients.
- [[castle-counting-formula](pages/castle-counting-formula.md)] and [[castle-counting-function](pages/castle-counting-function.md)] - the closed form being interpolated.
- [[generating-function-gallery](pages/generating-function-gallery.md)] - `num_k/den_k`, the roots of `char_k`, and their real-root counts.
- [[signed-tower-k-direction](pages/signed-tower-k-direction.md)] - the polynomials `A_L`, `B_L` evaluated here at half-integers.
- [[castle-eigenvalue-oeis-crosswalk](pages/castle-eigenvalue-oeis-crosswalk.md)] - the recurrences in `k` and their quasi-polynomial form.
- [[hyperbolic-sequence-family](pages/hyperbolic-sequence-family.md)] - the height-2 counts `A038505`, `A038503` and their recurrence, whose characteristic roots are `2` and `1 +- i`.
- [[tower-parity-sectors](pages/tower-parity-sectors.md)] - the factorization of `char_k` for even `k`.
- [[castle-strip](pages/castle-strip.md)] - the 0/1 rule matrices whose square roots are the half-columns.
- [[ridge-castle](pages/ridge-castle.md)] and [[metallic-strip-realizability](pages/metallic-strip-realizability.md)] - the ridge rule `J - D` and its characteristic polynomial.
- [[pell-castle-strip](pages/pell-castle-strip.md)] - the 1-smooth strip on three heights, whose tridiagonal matrix has no real square root.

## Footnotes

[^1]: [[project-euler-502-solution](pages/project-euler-502-solution.md)] §"The main formula" L66 - "F(w, h) = (h^w - (h-1)^w - P(h-1, w) + P(h-2, w)) / 2".
[^2]: [[project-euler-502-solution](pages/project-euler-502-solution.md)] §"Recursion for P(k, L)" L83-84 - "For fixed k, P(k, L) satisfies a linear recurrence in L of order roughly k ... For fixed L, P(k, L) satisfies a linear recurrence in k of order at most about 2L"; the exact orders are on the linked pages.
[^3]: https://en.wikipedia.org/wiki/Carlson%27s_theorem (read 2026-10-16) - "f(z) is an entire function of exponential type ... There exists c < pi such that |f(iy)| <= C e^{c|y|} ... f(n) = 0 for every non-negative integer n. Then f is identically zero"; sharpness shown by `sin(pi z)`.
[^4]: [[project-euler-502-solution](pages/project-euler-502-solution.md)] §"Recursion for P(k, L)" L103-108 - "The matrix [[1, 1], [-1, 1]] has eigenvalues 1 + i and 1 - i. So P(1, L) is a sum of terms proportional to (1+i)^L and (1-i)^L; those two are complex conjugates, so their sum is a real number ... P(1, L) = Re((1+i)^{L+1})".
[^5]: [[project-euler-502-solution](pages/project-euler-502-solution.md)] §"Recursion for P(k, L)" L117-118 - "P(k, 2) = (-1)^k (k+1), satisfying (lambda+1)^2 = 0. P(k, 3) = (-1)^k (k+1)^2, satisfying (lambda+1)^3 = 0."
[^6]: https://oeis.org/A226321 (read 2026-09-19) - "Number of real {0,1} matrices n X n which are the square of a {0,1} matrix", data `1, 2, 8, 88, 3245, 254411, 37324414`.
[^7]: https://oeis.org/A086510 (read 2026-09-19) - "Number of n X n real (0,1)-matrices with all eigenvalues >= 0", data `1, 2, 13, 261, 15418, 2566333`.
[^8]: https://oeis.org/A003024 (read 2026-09-19) - "Number of acyclic digraphs (or DAGs) with n labeled nodes", data `1, 1, 3, 25, 543, 29281, ...`; https://arxiv.org/abs/math/0310423 (read 2026-10-16) - B. D. McKay, F. E. Oggier, G. F. Royle, N. J. A. Sloane, I. M. Wanless, H. S. Wilf, "Acyclic digraphs and eigenvalues of (0,1)-matrices", J. Integer Sequences 7 (2004), 04.3.3, Theorem 1: "the number of acyclic directed graphs with n labeled vertices is equal to the number of n X n matrices of 0's and 1's whose eigenvalues are positive real numbers"; the proof shows that such a matrix `B` has all eigenvalues 1 and that `B - I` is the adjacency matrix of an acyclic digraph.
[^9]: https://oeis.org/A001035 (read 2026-09-19) - "Number of partially ordered sets ("posets") with n labeled elements (or labeled acyclic transitive digraphs)", data `1, 1, 3, 19, 219, 4231, 130023, ...`.
[^10]: https://arxiv.org/abs/0805.0245 (read 2026-10-16) - J. Gallier, "Logarithms and Square Roots of Real Matrices", Abstract and §1 p.2: "under the same condition (no negative eigenvalues) every real n x n matrix, A, has a real square root", where the condition is that "no real eigenvalue of A is negative or zero".
[^exec]: Verified by execution (Python 3.11 with SymPy, NumPy and mpmath, 2026-10-16): `char_k = lambda^{k+1} den_k(1/lambda)` from the update of `num_k`, `den_k`, its factorization and distinct roots for `k <= 8`, and exact counts of real and negative real roots for `k <= 40`; `P(k, L)` by the column-height dynamic program, the interpolation coefficients from the Vandermonde system, the principal-branch interpolant in 40-digit arithmetic (reproduction error and imaginary parts for `k <= 8`), the table of `A^e(w, h)` for `h = 2..6`, and the cosine form of `A^e(w, 2)`; `A_L`, `B_L` for `L = 2..8` by interpolation on even and odd `k`, checked against the dynamic program for `k <= 33`, and the half-integer values; all `2^{h^2}` 0/1 matrices for `h = 2, 3, 4`: squares of 0/1 matrices, and the exact real-root classification of their characteristic polynomials; all DAG rules `I + N` for `h <= 5` (strictly upper-triangular patterns conjugated by permutations), the exact square root `sum_k C(1/2, k) N^k` and the partial-order test; the chain, `V` and diamond posets; the eigenvalues of the named strips and `1^T (J / sqrt 3)^4 1 = 27`.
