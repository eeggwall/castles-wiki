---
title: Signed tower count P(k,L)
category: Concepts
summary: P(k, L) = Σ (−1)^blocks over the towers of height at most k on a base of length L, which gives the signed castle count S(w, h) = P(h−2, w) − P(h−1, w). For fixed k it satisfies a linear recurrence of order k + 1 whose characteristic polynomial char_k has λ^k-coefficient −(k+1) and constant term (−1)^{k+1} 2^k. At k = 1, P(1, L) = Re((1+i)^{L+1}) = A146559(L+1).
tags: [concept, castle, signed-count, c-finite, oeis, generating-functions]
sources: [oeis-mining-pe502, project-euler-502-solution, project-euler-502-representations]
created: 2026-09-13
updated: 2026-10-16
---

# Signed tower count P(k,L)

`P(k, L)` is the sum of `(−1)^{blocks}` over the towers of height at most `k` on a base of length `L` ([[castle-sign](pages/castle-sign.md)], [[castle-notation](pages/castle-notation.md)]). It enters the castle counts through the signed count `S(w, h) = P(h−2, w) − P(h−1, w)` and `A^e = (A + S)/2` ([[castle-counting-formula](pages/castle-counting-formula.md)], Equations (1) and (7)), so the row `P(k, ·)` is used by the castles of heights `h = k + 1` and `h = k + 2`. The base length starts at `L = 0`: the only towers on a base of length 0 are empty, so `P(k, 0) = 1`. The only tower of height 0 is empty too, so `P(0, L) = 1`.

The first values, computed by summing over all towers:[^1]

| `k` | `P(k, L)` for `L = 0, 1, 2, …` |
|---|---|
| 0 | `1, 1, 1, 1, 1, 1, 1, 1, …` |
| 1 | `1, 0, −2, −4, −4, 0, 8, 16, …` |
| 2 | `1, 1, 3, 9, 19, 33, 59, 121, …` |
| 3 | `1, 0, −4, −16, −40, −64, −32, 192, …` |
| 4 | `1, 1, 5, 25, 85, 225, 541, …` |
| 5 | `1, 0, −6, −36, −140, −384, −680, …` |
| 6 | `1, 1, 7, 49, 231, 833, 2583, …` |

At `L = 2` the block count of towers `(c_1, c_2)` is `max(c_1, c_2)`, and `2m + 1` of the pairs in `{0, …, k}²` have maximum `m`, so `P(k, 2) = Σ_{m=0}^{k} (−1)^m (2m + 1) = (−1)^k (k + 1)`. The source also gives `P(k, 3) = (−1)^k (k+1)²`, which the table confirms for `k ≤ 6`.[^2]

## Recurrences in L

The generating function `P_k(x) = Σ_L P(k, L) x^L` is `num_k(x)/den_k(x)`, where `num_0 = 1`, `den_0 = 1 − x` and[^3]

```
num_k  =  2·den_{k−1} − num_{k−1}
den_k  =  (1 − 2x)·den_{k−1} + x·num_{k−1}
```

`den_k` has degree `k + 1`, leading coefficient `(−1)^{k+1} 2^k` and constant term 1 ([[castle-counting-formula](pages/castle-counting-formula.md)], the Proposition in the section *Signed tower count*). So `P(k, ·)` satisfies a linear recurrence of order `k + 1` for `L ≥ k + 1`, with characteristic polynomial `char_k(λ) = λ^{k+1} den_k(1/λ)`:[^4]

```
char_1(λ)  =  λ² − 2λ + 2
char_2(λ)  =  λ³ − 3λ² + 4λ − 4                       =  (λ − 2)(λ² − λ + 2)
char_3(λ)  =  λ⁴ − 4λ³ + 8λ² − 8λ + 8
char_4(λ)  =  λ⁵ − 5λ⁴ + 12λ³ − 20λ² + 16λ − 16       =  (λ² − 2λ + 4)(λ³ − 3λ² + 2λ − 4)
char_5(λ)  =  λ⁶ − 6λ⁵ + 18λ⁴ − 32λ³ + 48λ² − 32λ + 32
char_6(λ)  =  λ⁷ − 7λ⁶ + 24λ⁵ − 56λ⁴ + 80λ³ − 112λ² + 64λ − 64
           =  (λ³ − 4λ² + 4λ − 8)(λ⁴ − 3λ³ + 8λ² − 4λ + 8)
```

`char_k` is monic, its constant term is the leading coefficient `(−1)^{k+1} 2^k` of `den_k`, and its coefficient of `λ^k` is the coefficient of `x` in `den_k`, which is `−(k+1)`. For the last claim: at `x = 0` the update gives `num_k(0) = 2 − num_{k−1}(0)`, so `num_k(0) = 1` for every `k`, and the coefficient of `x` in `den_k` is that of `den_{k−1}` minus `2·den_{k−1}(0) − num_{k−1}(0) = 1`.

The update is multiplication of the vector `(num, den)` by the matrix `[[−1, 2], [x, 1 − 2x]]`, which has trace `−2x` and determinant `−1`. By the Cayley-Hamilton theorem, which says that a matrix satisfies its own characteristic polynomial, the matrix `M` satisfies `M² = −2x·M + I`, so for `k ≥ 1`

```
den_{k+1}  =  den_{k−1} − 2x·den_k,
```

and the same for `num`. This is the recurrence of the Pell polynomials in the variable `−x` ([[generating-function-gallery](pages/generating-function-gallery.md)]).

**Factors and dominant roots.** For odd `k ≤ 15`, `char_k` is irreducible over the rationals; for `k = 2^m − 1` this is proved on [[char-k-eisenstein-at-two](pages/char-k-eisenstein-at-two.md)]. For even `k ≤ 14`, `char_k` has exactly two irreducible factors, and [[tower-parity-sectors](pages/tower-parity-sectors.md)] derives the factorization from the split of `P` by the parity of the last column. For `k = 2, 4, 6` the root of largest modulus is real, and `P(k, L) > 0` for every even `k ≤ 12` and `L < 40`. For odd `k ≤ 7` the roots of largest modulus are a complex-conjugate pair, and `P(k, ·)` changes sign in runs.[^1]

At `k = 6` the largest root is `2ψ² = 3.50976…`, with `ψ` the plastic number, the real root of `ψ³ = ψ + 1` ([[plastic-number](pages/plastic-number.md)]). Substituting `λ = 2μ` in the cubic factor gives `8(μ³ − 2μ² + μ − 1)`, and `μ = ψ²` is a root: `ψ⁶ − 2ψ⁴ + ψ² − 1 = (ψ² + 2ψ + 1) − 2(ψ² + ψ) + ψ² − 1 = 0`, using `ψ⁴ = ψ² + ψ` and `ψ⁶ = (ψ + 1)²`.

## The case k = 1

Towers of height at most 1 are binary strings, and their blocks are the runs of 1s. Write `P_even(1, L)` and `P_odd(1, L)` for the sums of `(−1)^{blocks}` over the strings of length `L ≥ 1` that end in 0 and in 1. Appending a 0 never changes the block count, and appending a 1 starts a new block exactly when the string ends in 0, so[^5]

```
P_even(1, L)  =  P_even(1, L−1) + P_odd(1, L−1)
P_odd(1, L)   =  −P_even(1, L−1) + P_odd(1, L−1)
```

with `P_even(1, 1) = 1` and `P_odd(1, 1) = −1`. Then `z_L = P_even(1, L) − i·P_odd(1, L)` satisfies `z_L = (1 + i)·z_{L−1}` and `z_1 = 1 + i`, so `z_L = (1 + i)^L`. Hence

```
P_even(1, L)  =  Re((1+i)^L)          P_odd(1, L)  =  −Im((1+i)^L)
P(1, L)       =  Re((1+i)^L) − Im((1+i)^L)  =  Re((1+i)^{L+1})  =  2^{(L+1)/2} cos((L+1)π/4).
```

`Re((1+i)^n)` is `A146559(n)`, so `P(1, L) = A146559(L+1)` and `P_even(1, L) = A146559(L)`.[^6] `Im((1+i)^n)` is `A009545(n)`, so `P_odd(1, L) = −A009545(L)`; and since `(1+i)^{n+2} = 2i(1+i)^n`, `P(1, L) = A009545(L+3)/2` as well.[^7] Expanding `(1+i)^{L+1}` by the binomial theorem gives `P(1, L) = Σ_r (−1)^r C(L+1, 2r)`, which is `A038503(L+1) − A038505(L+1)`, where `A038503(n)` and `A038505(n)` are the sums of `C(n, j)` over `j ≡ 0` and over `j ≡ 2 (mod 4)` ([[block-count-constraints](pages/block-count-constraints.md)], [[hyperbolic-sequence-family](pages/hyperbolic-sequence-family.md)]).[^6][^9]

Since `(1+i)^4 = −4`, `P(1, L+4) = −4·P(1, L)`. The signs of `P(1, L)` repeat with period 8, `+, 0, −, −, −, 0, +, +` from `L = 0`, and `P(1, L) = 0` exactly when `L ≡ 1 (mod 4)`.

**Castles of height 2.** A castle of width `w` and height 2 stands on towers of height at most 1 that are not all zero, and has one block more. So `S(w, 2) = P(0, w) − P(1, w) = 1 − P(1, w)`, and[^8]

```
A^o(w, 2) − A^e(w, 2)  =  P(1, w) − 1  =  A146559(w+1) − 1.
```

At `w = 2` the castles are `(1, 2)`, `(2, 1)` and `(2, 2)`, each with two blocks, and `P(1, 2) − 1 = −3`. The castles of width `w` and height 2 with `c_w = 2` stand on the strings that end in 1, so for them the number with an even number of blocks minus the number with an odd number is `−P_odd(1, w) = A009545(w)`. This split is the `k = 1` case of [[tower-parity-sectors](pages/tower-parity-sectors.md)].

## Recurrences in k

For fixed `L`, `P(·, L)` also satisfies a linear recurrence in `k`. For every `L`, `P(k, L)` is a polynomial in `k` of degree at most `L` on each class of `k` modulo 2 ([[sum-of-three-cubes-castles](pages/sum-of-three-cubes-castles.md)], section *The residue test*), so `P(k, L)` is `(−1)^k` times a polynomial in `k` plus a polynomial in `k`, as `P(k, 2)` and `P(k, 3)` show, and its characteristic polynomial divides `(λ + 1)^{L+1} (λ − 1)^{L+1}`. For `4 ≤ L ≤ 12` it is `(λ + 1)^L (λ − 1)^{L−2}` (computed by Berlekamp-Massey) ([[signed-tower-k-direction](pages/signed-tower-k-direction.md)], [[castle-eigenvalue-oeis-crosswalk](pages/castle-eigenvalue-oeis-crosswalk.md)]). The Project Euler target `A^e(100, 10^12)` is evaluated through this recurrence ([[castle-count-algorithms](pages/castle-count-algorithms.md)]).

## OEIS

- `A146559`, the real parts of `(1+i)^n`, is the row `k = 1`: `P(1, L) = A146559(L+1)`. The entry carries a comment on castles of height 2 and the formula `a(n) = A038503(n) − A038505(n)` ([[oeis-height2-hyperbolic-castles](pages/oeis-height2-hyperbolic-castles.md)]).[^6]
- `A009545`, the imaginary parts of `(1+i)^n`, gives `P_odd(1, L) = −A009545(L)` and `P(1, L) = A009545(L+3)/2`.
- The OEIS status of the rows `k ≥ 2` is recorded on [[castle-sequence-catalogue](pages/castle-sequence-catalogue.md)].

## Appearances in Sources

- [[oeis-mining-pe502](pages/oeis-mining-pe502.md)] - the characteristic polynomials `char_1` to `char_5`, the identification `P(1, L) = A146559(L+1)`, and `A009545` as the imaginary part.
- [[project-euler-502-solution](pages/project-euler-502-solution.md)] - the definition of `P(k, L)`, the derivation of `P(1, L) = Re((1+i)^{L+1})` from the split by the last bit, and the values `P(k, 2)` and `P(k, 3)`.
- [[project-euler-502-representations](pages/project-euler-502-representations.md)] - the update of `num_k` and `den_k`.

## Related Concepts

- [[castle-sign](pages/castle-sign.md)] - the sign `(−1)^{blocks}` and the split `(T ± P)/2` of towers into even-block and odd-block ones.
- [[castle-counting-formula](pages/castle-counting-formula.md)] - the derivation of `P_k(x)` and of `A^e(w, h)` from `P(h−1, w)` and `P(h−2, w)`.
- [[tower-parity-sectors](pages/tower-parity-sectors.md)] - `P = P_even + P_odd` by the parity of the last column for every `k`, and the factors of `char_k` for even `k`.
- [[signed-tower-k-direction](pages/signed-tower-k-direction.md)] - the recurrence of `P(·, L)` in `k` and its period-2 closed forms.
- [[generating-function-gallery](pages/generating-function-gallery.md)] - the rational functions `num_k/den_k` and the closed form of `den_k` from the Pell-polynomial recurrence.
- [[char-k-eisenstein-at-two](pages/char-k-eisenstein-at-two.md)] - the proof that `char_k` is irreducible for `k = 2^m − 1`.
- [[castle-sign-kms-matrix](pages/castle-sign-kms-matrix.md)] - the transfer matrix with a weight `t` per block, diagonally similar to the Kac-Murdock-Szegő matrix `(ρ^{|a−b|})` with `ρ = √t`; `P(k, L)` is the case `t = −1`, `ρ = i`.
- [[castle-eigenvalue-oeis-crosswalk](pages/castle-eigenvalue-oeis-crosswalk.md)] - the eigenvalues of `char_k` and of the recurrences in `k`, set against the OEIS.
- [[block-count-constraints](pages/block-count-constraints.md)] - selecting towers and castles by block count, with `P(1, L)` as the case of block count modulo 2.
- [[hyperbolic-sequence-family](pages/hyperbolic-sequence-family.md)] - the sequences `A038503` and `A038505` of the castles of height 2.
- [[convex-core](pages/convex-core.md)] - the sum of `(−1)^{blocks}` over the castles with a given convex core, a product of values of `P`.
- [[recurrence-discovery](pages/recurrence-discovery.md)] - the orders `k + 1` in `L` and `2L − 2` in `k`, found by Berlekamp-Massey.
- [[new-sequence-fw3](pages/new-sequence-fw3.md)] - `A^e(w, 3) = (3^w − 2^w − P(2, w) + P(1, w))/2`, the first row of castle counts that uses `P(2, ·)`.
- [[tower-heap](pages/tower-heap.md)] - the towers counted by blocks without sign, through Narayana polynomials.
- [[oeis-cross-referencing](pages/oeis-cross-referencing.md)] - matching sequences against the OEIS up to shifts of the index, as between `A146559` and `A009545`.

## Footnotes

[^1]: Verified by execution (Python 3.11 with SymPy, 2026-10-16): the table by summing `(−1)^{blocks}` over all towers, and the rows `k = 4, 6` from the `num`/`den` update; `char_1` to `char_6` and their factorizations; irreducibility of `char_k` for odd `k ≤ 15` and two irreducible factors for even `k ≤ 14`; the roots of largest modulus for `k ≤ 7`; `P(k, L) > 0` for even `k ≤ 12` and `L < 40`; `P(k, 2) = (−1)^k (k+1)` and `P(k, 3) = (−1)^k (k+1)²` for `k ≤ 6`; `P_even(1, L)` and `P_odd(1, L)` for `L ≤ 11`.
[^2]: [[project-euler-502-solution](pages/project-euler-502-solution.md)] §"Recursion for P(k, L)" L115-118 - "Small cases (also consistent): P(k, 2) = (-1)^k (k+1), satisfying (λ+1)^2 = 0. P(k, 3) = (-1)^k (k+1)^2, satisfying (λ+1)^3 = 0."
[^3]: [[project-euler-502-representations](pages/project-euler-502-representations.md)] §"Signed count" L333-340 - "P_k = (2 - P_{k-1})/(1 - 2x + x P_{k-1}), P_0 = 1/(1-x)" and "num_k = 2 den_{k-1} - num_{k-1}, den_k = den_{k-1}(1-2x) + x num_{k-1}".
[^4]: [[oeis-mining-pe502](pages/oeis-mining-pe502.md)] `mine-notes.md` §"Vein 1" L31-37 - "The general P(k,·) family is C-finite of order k+1: P(1): x^2 - 2x + 2 (eigenvalues 1 +/- i) P(2): x^3 - 3x^2 + 4x - 4 (= (x-2)(x^2-x+2)) ... P(5): x^6 - 6x^5 + 18x^4 - 32x^3 + 48x^2 - 32x + 32 (constant term = (-1)^{k-1} 2^k; leading coeff -(k+1))".
[^5]: [[project-euler-502-solution](pages/project-euler-502-solution.md)] §"Recursion for P(k, L)" L94-108 - "Split the strings by their last bit ... Appending a 0 never changes the run count; appending a 1 starts a new run exactly when the previous bit is 0", "a_L = a_{L-1} + b_{L-1}, b_L = -a_{L-1} + b_{L-1} with a_1 = 1, b_1 = -1", "P(1, L) = Re((1+i)^{L+1})".
[^6]: https://oeis.org/A146559 (read 2026-10-16) - "Expansion of (1-x)/(1 - 2*x + 2*x^2)", "(1+i)^n = a(n) + A009545(n)*i", "a(n) = Re( (1+i)^n )", "a(n) = A038503(n) - A038505(n)", and the comment "Among the castle polyominoes of width n-1 and reaching height 2, a(n) - 1 is the number with an odd number of blocks minus the number of those with an even number of blocks, for n >= 2".
[^7]: [[oeis-mining-pe502](pages/oeis-mining-pe502.md)] `mine-notes.md` §"Vein 1" L21-29 - "A009545 is the *imaginary* part of (1+i)^n ... P(1,L) = Re((1+i)^{L+1}) = A146559(L+1) ... A009545(n) = Im((1+i)^n) (the companion, not P)".
[^8]: raw/oeis-pe502/xrefs/A146559-signed.md §"Identity (verified)" L23-41 - "a(n) - 1 = odd(n-1, 2) - F(n-1, 2) for n >= 2", "Verified by brute force for w = n-1 = 1..14", with the table of values from `n = 2` to `n = 13`.
[^9]: https://oeis.org/A038503 and https://oeis.org/A038505 (read 2026-10-16) - "Sum of every 4th entry of row n in Pascal's triangle, starting at \"n choose 0\"" and "... starting at binomial(n,2)".
