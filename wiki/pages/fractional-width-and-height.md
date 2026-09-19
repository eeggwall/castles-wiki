---
title: Fractional width and fractional height
category: Analyses
summary: F(w,h) is C-finite in the width and a quasi-polynomial in the height, so both arguments interpolate to real values, and the two directions behave differently. In the width, every eigenvalue of the signed tower recurrence char_k for k <= 8 is either a positive real or one of a complex-conjugate pair (no negative real root), so on the principal branch F(w,h) is a real function of real w for every h <= 9: F(w,2) = (2^{w+1} - 2^{(w+3)/2} cos(pi(w+1)/4))/4, and F(2.5,3) = 0.689, F(3.5,4) = 60.707. In the height, P(k,L) = (-1)^k A_L(k) + B_L(k) and (-1)^k is +-i at half-integers, so F(w, m + 1/2) = (A - B_w(h-1) + B_w(h-2))/2 + i (-1)^m (A_w(h-1) + A_w(h-2))/2 is genuinely complex: F(4, 2.5) = 16.75 + 6i. Half a column is real, half a row is imaginary, and the imaginary part is the alternating part of the parity clause moved onto the imaginary axis. The half-column problem R^2 = M: 8 of the 16 height-2 rules and 88 of the 512 height-3 rules are squares of 0/1 rules; the free strip J has the half-column J/sqrt(h); every metallic strip on the wiki (J-I, the 1-smooth tridiagonal, the ceiling-exception J-D at heights 3 and 4) has a simple negative eigenvalue and therefore no real square root at all. The metallic ladder has no half-steps.
tags: [analysis, castle, fractional-calculus, interpolation, matrix-power, branch-cut, quasi-polynomial, c-finite, eigenvalues, transfer-matrix, square-root, embedding, metallic-means, f-division, computation, verification]
sources: [project-euler-502-solution]
created: 2026-09-19
updated: 2026-09-19
---

# Fractional width and fractional height

The count `F(w, h)` is defined for integer width and integer height, but it is built from objects that make sense off the integers. In the width it is a **C-finite sequence**, a sum of exponentials `c_j lambda_j^w` in the eigenvalues of a transfer matrix, and `lambda^w` is meaningful for real `w` once a branch of `log lambda` is chosen. In the height it is a **quasi-polynomial**, `(-1)^h` times a polynomial plus a polynomial, and `(-1)^h = e^{i pi h}` is meaningful for real `h` too. This page interpolates both arguments, finds that the two directions behave differently, and traces the difference to a single fact about where the parity clause puts its eigenvalues. It then asks the question a fractional matrix power really poses, which strip rules `M` are the square of a finer rule `R`, and answers it for the strips the wiki cares about. Second page of the F Division; the first is [[fractional-block-count](pages/fractional-block-count.md)].

Every number below was computed while writing and re-run for the final tables; the scripts are described in the execution footnote.[^exec]

## What is being interpolated

The closed form is[^1]

```
F(w, h)  =  [ h^w - (h - 1)^w - P(h - 1, w) + P(h - 2, w) ] / 2,
```

with `P(k, L) = sum (-1)^{blocks}` over towers of height at most `k` on a base of length `L`. The unsigned part `A(w, h) = h^w - (h - 1)^w` is a difference of two exponentials with positive bases in `w` and a polynomial in `h`; it interpolates in both directions without incident and is real everywhere. All the interest is in the signed towers `P(k, L)`, which satisfy a linear recurrence in each variable separately: order about `k` in `L`, and order about `2L` in `k`.[^2] The `L`-direction recurrence has characteristic polynomial `char_k` whose roots are the eigenvalues of the signed transfer matrix ([[generating-function-gallery](pages/generating-function-gallery.md)]); the `k`-direction recurrence has characteristic polynomial `(x + 1)^L (x - 1)^{L - 2}`, so `P(k, L) = (-1)^k A_L(k) + B_L(k)` with `A_L, B_L` polynomials ([[signed-tower-k-direction](pages/signed-tower-k-direction.md)]). Two directions, two kinds of function.

## Fractional width: real, on the principal branch

Interpolating `P(k, w)` in `w` means writing `P(k, w) = sum_j c_j lambda_j^w` over the roots `lambda_j` of `char_k` (the coefficients `c_j` are fixed by the first `k + 1` integer values) and evaluating `lambda_j^w = exp(w log lambda_j)`. The result is real for all real `w` exactly when every non-real contribution cancels against its conjugate, and that depends on the sign pattern of the roots:

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

**No `char_k` for `k <= 8` has a negative real root.**[^exec] Odd `k` has no real root at all (the irreducibility noted on the gallery page); even `k` has exactly one real root, positive, the dominant `rho_k`. Complex roots come in conjugate pairs with conjugate coefficients, and on the principal branch `lambda^w` and `conj(lambda)^w` are conjugate for every real `w`, so their sum is real. Therefore **`P(k, w)` is a real function of real `w` for every `k <= 8`, and `F(w, h)` is real for every `h <= 9`.** The imaginary part at `w = 2.5, 3.5, 4.5, 5.5` is zero to machine precision for `k = 1, ..., 6`, and the interpolant reproduces the integer values to `10^{-9}`.[^exec]

The height-2 case is explicit. The Solution's own derivation gives `P(1, L) = Re((1 + i)^{L+1})` from the eigenvalues `1 +- i` of the `2 x 2` signed matrix,[^3] and `(1 + i)^{n} = 2^{n/2} e^{i pi n / 4}`, so

```
F(w, 2)  =  (2^w - P(1, w)) / 2  =  ( 2^{w+1} - 2^{(w+3)/2} cos(pi (w + 1) / 4) ) / 4,
```

which is `1, 3, 6, 10, 16, 28, 56, 120` at `w = 1, ..., 8` and `4.382` at `w = 2.5`. The cosine is the conjugate pair `(1 +- i)^{w+1}` folded together; it is what makes the parity term oscillate with period 8 in the width (the order-4 hyperbolic family on [[hyperbolic-sequence-family](pages/hyperbolic-sequence-family.md)]) and it is real at every real `w`.

The interpolated table, principal branch, for `h = 2, ..., 6`:[^exec]

| `h` | `w = 2` | `2.5` | `3` | `3.5` | `4` | `4.5` | `5` |
|---|---|---|---|---|---|---|---|
| 2 | 3 | 4.382 | 6 | 7.854 | 10 | 12.601 | 16 |
| 3 | 0 | 0.689 | 3 | 8.744 | 21 | 44.894 | 89 |
| 4 | 7 | 15.235 | 31 | 60.707 | 117 | 225.533 | 439 |
| 5 | 0 | 1.742 | 10 | 38.456 | 122 | 345.039 | 906 |
| 6 | 11 | 29.912 | 76 | 185.918 | 448 | 1080.352 | 2630 |

The zeros at `w = 2` for odd `h` are structural: a width-2 castle of height `h` has exactly `h` blocks, so `F(2, h) = 0` for odd `h` and `F(2, h) = 2h - 1` for even `h`. The interpolant passes through those zeros and is positive on either side; nothing forces it to stay nonnegative in general, and whether `F(w, h) >= 0` for all real `w >= 2` is not settled here.

**The branch caveat.** "Real" is a statement about the principal branch. Replacing `log lambda` by `log lambda + 2 pi i n` for one complex root and `log conj(lambda) - 2 pi i n` for its conjugate keeps the interpolant real but adds an oscillation `e^{2 pi i n w}` that vanishes at the integers; there are infinitely many real interpolants and the principal one is the one of smallest exponential type, the choice Carlson's theorem singles out. So the parity clause does not make fractional width *complex*, but it does make it *non-canonical*: `A(w, h)`, with only positive real bases, has one natural interpolant, and the signed part has a family.

## Fractional height: imaginary, unavoidably

In the height direction the only eigenvalues are `+1` and `-1`, and `P(k, L) = (-1)^k A_L(k) + B_L(k)` with `A_L` of degree `L - 1` and `B_L` of degree `L - 3`.[^4] Interpolating in `k` means `(-1)^k = e^{i pi k}`, and at a half-integer `k = m + 1/2` this is `+- i`. There is no conjugate partner to cancel against: `-1` is its own conjugate. So

```
P(m + 1/2, L)  =  B_L(m + 1/2)  +  i (-1)^m A_L(m + 1/2),
```

and the alternating part moves wholesale onto the imaginary axis. For the small bases, whose quasi-polynomials are `A_2 = k + 1`, `A_3 = (k + 1)^2`, `A_4 = (k + 1)(2k + 1)(2k + 3) / 6` with `B_4 = (k + 1) / 2`:[^exec]

| `L` | `P(1/2, L)` | `P(3/2, L)` | `P(5/2, L)` |
|---|---|---|---|
| 2 | `1.5 i` | `-2.5 i` | `3.5 i` |
| 3 | `2.25 i` | `-6.25 i` | `12.25 i` |
| 4 | `0.75 + 2 i` | `1.25 - 10 i` | `1.75 + 28 i` |
| 5 | `2.25 + 0.9375 i` | `6.25 - 10.9375 i` | `12.25 + 45.9375 i` |
| 6 | `4 + 0.1875 i` | `20 - 8.3125 i` | `56 + 56.4375 i` |

Pushing this through the closed form, with `h = m + 1/2`:

```
F(w, m + 1/2)  =  [ A(w, h) - B_w(h - 1) + B_w(h - 2) ] / 2   +   i (-1)^m [ A_w(h - 1) + A_w(h - 2) ] / 2.
```

At width 4: `F(4, 2.5) = 16.75 + 6 i`, `F(4, 3.5) = 55.25 - 19 i`, `F(4, 4.5) = 129.75 + 44 i`, against `A(4, h) = 34, 111, 260`.[^exec] The imaginary parts are exact: `A_4(3/2) + A_4(1/2) = 10 + 2 = 12`, half of which is `6`. **The real part of a half-integer-height count is the steady part of the parity clause and the imaginary part is its alternating part.** The two polynomials that [[signed-tower-k-direction](pages/signed-tower-k-direction.md)] separates by parity of `k` are separated here by the real and imaginary axes.

## Half a column is real, half a row is imaginary

The asymmetry has one cause. A linear recurrence interpolates to a real function on the principal branch exactly when its **negative real eigenvalues** carry zero coefficient; positive reals are harmless and complex pairs cancel. The unsigned count `A(w, h)` has eigenvalues `h` and `h - 1` in the width and none in the height (it is a polynomial), so it is real both ways. The parity clause adds the signed towers, and their eigenvalues are:

- in the **width**, the roots of `char_k`: complex pairs and one positive real, never a negative real (for `k <= 8`; the general statement is open);
- in the **height**, exactly `+1` and `-1`, with `-1` carrying the whole alternating polynomial `A_L`.

So the same clause is invisible to fractional width and is the entire imaginary part of fractional height. This is a sharper version of the IDEAS claim that "the parity clause is a branch cut": in the width it is a *choice* of branch (real either way), in the height it is a *forced* imaginary part. The imaginary part `(-1)^m (A_w(h - 1) + A_w(h - 2)) / 2` is a polynomial in `h` of degree `w - 1`, and it is a clean numerical measure of how much of `F(w, h)` the parity clause is responsible for at a given width.

## The half-column problem

A fractional matrix power `M^{1/2}` asks a combinatorial question: is the strip rule `M` ([[castle-strip](pages/castle-strip.md)]) two steps of a finer rule `R`, with `R^2 = M`? If so, a width-`w` strip under `M` is a width-`2w` strip under `R` read at every other column, and `R` is a **half-column** rule. This is the embedding problem for Markov chains (Kingman 1962: which stochastic matrices are `e^{Q}` for a generator `Q`, equivalently have roots of every order) transposed from probabilities to counts.[^5] Three grades of answer, exhaustively for small heights:[^exec]

| height | 0/1 rules | squares of a 0/1 rule | nonnegative spectrum (real principal root exists) | principal root entrywise nonnegative |
|---|---|---|---|---|
| 2 | 16 | 8 | 13 | 11 |
| 3 | 512 | 88 | 246 | 122 |

Half the height-2 rules and about a sixth of the height-3 rules are the square of another 0/1 rule (as integer matrices, so the finer rule has at most one two-step path between any pair of heights). About half have a real principal square root, and about a quarter have one with nonnegative entries, a weighted half-column rule.

**The named strips.** The rules the wiki has studied for their growth constants:[^exec]

| strip | matrix | eigenvalues | real half-column |
|---|---|---|---|
| free strip, `h = 3` | `J` (all ones) | `3, 0, 0` | **yes**: `J / sqrt(3)` |
| no equal neighbours, `h = 3` | `J - I` | `2, -1, -1` | no real *nonnegative* root found; the double `-1` leaves a real root possible |
| 1-smooth (Motzkin), `h = 3` | tridiagonal | `1 + sqrt 2, 1, 1 - sqrt 2` | **none**: simple negative eigenvalue |
| ceiling exception, `h = 3` (silver) | `J - D` | `1 + sqrt 2, -0.4142, -1` | **none**: simple negative eigenvalues |
| ceiling exception, `h = 4` (bronze) | `J - D` | `3.3028, -0.3028, -1, -1` | **none**: simple negative eigenvalue |

A real matrix has a real square root only if every Jordan block belonging to a negative eigenvalue occurs an even number of times (Higham 1987), so a **simple negative eigenvalue rules out any real square root**, nonnegative or not.[^6] The 1-smooth strip and the ceiling-exception strips all have one. The free strip is the opposite extreme: `J^2 = h J`, so `J^{1/2} = J / sqrt(h)`, a rule in which every height may follow every height with weight `1 / sqrt(h)`, and the count `1^T (J / sqrt h)^{2(w-1)} 1 = h^w` is preserved exactly (checked at `h = 3, w = 3`: `27`).[^exec] Half a column of the unrestricted castle is a uniformly weighted rule; half a column of a metallic castle does not exist.

This is a statement about the metallic ladder of [[metallic-means](pages/metallic-means.md)] and [[metallic-strip-realizability](pages/metallic-strip-realizability.md)]: the realizing rule `J - D` has characteristic polynomial `(x + 1)^{h - 2} (x^2 - (h - 1) x - 1)`, whose quadratic factor always has one negative root `-1 / delta_{h-1}`, simple. **The metallic ladder has no half-steps**: no rung is two half-columns of a finer real rule. (Whether some *other* rule with the same growth constant has a half-column is a different question and is open; silver has three known realizations.) The obstruction is the same `-1`-type eigenvalue that made fractional height imaginary, seen now as a negative root in a strip rule rather than in a quasi-polynomial.

## What this page settles and what it opens

Settled:

- `char_k` has no negative real root for `k <= 8`; `P(k, w)` and `F(w, h)` interpolate to real functions of real `w` on the principal branch for `h <= 9`, with `F(w, 2)` in closed form.
- `F(w, m + 1/2)` is complex with real part `(A - B_w(h-1) + B_w(h-2)) / 2` and imaginary part `(-1)^m (A_w(h-1) + A_w(h-2)) / 2`; `F(4, 2.5) = 16.75 + 6 i`.
- The asymmetry is the sign of the eigenvalues: no negative reals in the width, exactly `-1` in the height.
- 8 of 16 height-2 and 88 of 512 height-3 rules are squares of 0/1 rules; `J^{1/2} = J / sqrt h`; the 1-smooth and ceiling-exception strips have simple negative eigenvalues and no real square root.

Open:

- **No negative real roots for all `k`.** The gallery page gives `char_k` in closed form through Chebyshev-type recurrences; a proof that no root is a negative real would make the width interpolation real for every height.
- **Nonnegativity of the width interpolant.** Is `F(w, h) >= 0` for all real `w >= 2` on the principal branch?
- **Non-principal real interpolants.** Which branch choice, if any, has a combinatorial meaning (a castle of width `w + 1/2` as an object)?
- **The `J - I` half-column.** The double `-1` allows a real square root in principle; find one or show none is nonnegative.
- **Half-columns for the other silver realizations**, the anchored 1-smooth strip and the tower word, and for the plastic-number rules of [[plastic-number](pages/plastic-number.md)].
- **Fractional DFT.** The skyline DFT of [[spectral-analysis](pages/spectral-analysis.md)] is the third castle operator with a spectral fractional power (`DFT^4 = I`, eigenvalues the fourth roots of unity); its `a`-th power rotates the time-frequency plane and its castle signatures are unexplored.

## Appearances in Sources

- [[project-euler-502-solution](pages/project-euler-502-solution.md)] - the closed form, the recurrences in both directions, the `1 +- i` eigenvalues and `P(1, L) = Re((1 + i)^{L+1})`, and `P(k, 2)`, `P(k, 3)` with their `(lambda + 1)^2`, `(lambda + 1)^3` annihilators.

## Related Concepts

- [[fractional-block-count](pages/fractional-block-count.md)] - the F Division's first page; the statistic, not the argument, is interpolated there.
- [[castle-counting-formula](pages/castle-counting-formula.md)] and [[castle-counting-function](pages/castle-counting-function.md)] - the object being interpolated.
- [[generating-function-gallery](pages/generating-function-gallery.md)] - `num_k / den_k` and the roots of `char_k`; the irreducibility for odd `k`.
- [[signed-tower-k-direction](pages/signed-tower-k-direction.md)] - `(x + 1)^L (x - 1)^{L-2}` and the `A_L, B_L` table this page evaluates at half-integers.
- [[castle-eigenvalue-oeis-crosswalk](pages/castle-eigenvalue-oeis-crosswalk.md)] - the quasi-polynomial reading of the `k` direction.
- [[hyperbolic-sequence-family](pages/hyperbolic-sequence-family.md)] - the period-8 oscillation of `F(w, 2)` in the width.
- [[tower-parity-sectors](pages/tower-parity-sectors.md)] - why `char_k` factors for even `k` and not for odd.
- [[castle-strip](pages/castle-strip.md)] - the 0/1 rule matrices whose square roots are the half-columns.
- [[metallic-means](pages/metallic-means.md)] and [[metallic-strip-realizability](pages/metallic-strip-realizability.md)] - the ceiling-exception rule `J - D` and its `(x + 1)^{h-2} (x^2 - (h-1) x - 1)`.
- [[pell-castle-strip](pages/pell-castle-strip.md)] - the 1-smooth strip whose tridiagonal matrix has no real square root.
- [[kitamasa](pages/kitamasa.md)] and [[mod-p-observatory](pages/mod-p-observatory.md)] - where the fractional power `x^{w/2} mod char` becomes root extraction (the F Division's ring item).
- [[spectral-analysis](pages/spectral-analysis.md)] - the skyline DFT, third operator with a spectral fractional power.

## Footnotes

[^1]: [[project-euler-502-solution](pages/project-euler-502-solution.md)] §"The main formula" L66 - "F(w, h) = (h^w - (h-1)^w - P(h-1, w) + P(h-2, w)) / 2".
[^2]: [[project-euler-502-solution](pages/project-euler-502-solution.md)] §"Recursion for P(k, L)" L83-84 - "For fixed k, P(k, L) satisfies a linear recurrence in L of order roughly k ... For fixed L, P(k, L) satisfies a linear recurrence in k of order at most about 2L."
[^3]: [[project-euler-502-solution](pages/project-euler-502-solution.md)] §"Recursion for P(k, L)" L103-108 - "The matrix [[1, 1], [-1, 1]] has eigenvalues 1 + i and 1 - i. So P(1, L) is a sum of terms proportional to (1+i)^L and (1-i)^L; those two are complex conjugates, so their sum is a real number ... P(1, L) = Re((1+i)^{L+1})".
[^4]: [[project-euler-502-solution](pages/project-euler-502-solution.md)] §"Recursion for P(k, L)" L117-118 - "P(k, 2) = (-1)^k (k+1), satisfying (lambda+1)^2 = 0. P(k, 3) = (-1)^k (k+1)^2, satisfying (lambda+1)^3 = 0."; the general `(x + 1)^L (x - 1)^{L-2}` and the `A_L, B_L` table are on [[signed-tower-k-direction](pages/signed-tower-k-direction.md)] and were re-derived here by interpolating even and odd `k` separately.
[^5]: https://doi.org/10.1007/BF00531768 (2026-09-19) [synthesis] - J. F. C. Kingman, "The imbedding problem for finite Markov chains", Z. Wahrscheinlichkeitstheorie 1 (1962) 14-24: which stochastic matrices arise as transition matrices of a continuous-time chain, equivalently as `exp(Q)` for a generator `Q`, so that roots of every order exist within the chain; the castle question replaces stochastic matrices by 0/1 count matrices and asks only for a square root.
[^6]: https://doi.org/10.1016/0024-3795(87)90118-2 (2026-09-19) [synthesis] - N. J. Higham, "Computing real square roots of a real matrix", Linear Algebra and its Applications 88/89 (1987) 405-430: a real matrix has a real square root if and only if it has an even number of Jordan blocks of each size for every negative eigenvalue; in particular a simple negative eigenvalue excludes any real square root, and a matrix with no negative real eigenvalues has a unique real principal square root.
[^exec]: Verified by execution (2026-09-19): one Python 3 script with SymPy 1.14, NumPy 1.26, SciPy 1.15. (i) `num_k, den_k` from the gallery recurrence `num_k = 2 den_{k-1} - num_{k-1}`, `den_k = den_{k-1}(1 - 2x) + x num_{k-1}`; `char_k = lambda^{k+1} den_k(1/lambda)`; roots by `numpy.roots`, classified by sign and imaginary part; factorization by `sympy.factor`, `k = 1..8`. (ii) `P(k, L)` by the signed DP over the last column height; interpolation coefficients from the Vandermonde system on `L = 0..k`; `P(k, w)` on the principal branch via `exp(w log lambda)`; integer reproduction error `<= 1.1e-9` for `L <= 11`; imaginary parts at `w = 2.5, 3.5, 4.5, 5.5` all `< 1e-6`. (iii) `F(w, h)` table for `h = 2..6`, `w = 2..5` in half steps; the `F(w, 2)` cosine form checked against the roots-of-unity sum at `w = 1..8` and `w = 2.5`. (iv) `A_L, B_L` for `L = 2..6` by `sympy.interpolate` on even and odd `k` separately, re-checked against the DP for `k = 0..14`; `P(k, L)` at `k = 1/2, 3/2, 5/2`; `F(4, h)` at `h = 2.5, 3.5, 4.5`. (v) All `2^{h^2}` 0/1 matrices for `h = 2, 3`: which are `R @ R` with entries `<= 1` for a 0/1 `R`; which have all eigenvalues real and `>= 0`; for those, `scipy.linalg.sqrtm` real and entrywise `>= 0`. (vi) Eigenvalues of `J`, `J - I`, the tridiagonal, and `J - D` at `h = 3, 4`; `sqrtm(J) = J / sqrt 3`; `1^T (J / sqrt 3)^4 1 = 27`. All quoted numbers are the script's printed output.
