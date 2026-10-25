---
title: The k-direction of P(k, L) as a quasi-polynomial
category: Concepts
summary: At fixed base length L, the signed tower count P(k, L) satisfies a linear recurrence in the tower height k. For every L ≥ 4 its characteristic polynomial is (x+1)^L (x−1)^{L−2}, proved from the eigenvalues −x ± √(1+x²) of the height step and checked by computation for L ≤ 21, and for L ≤ 3 it is (x−1)(x+1), (x+1)² and (x+1)³, so every eigenvalue is +1 or −1 and P(k, L) = (−1)^k A_L(k) + B_L(k) with polynomials A_L, B_L, of degrees L − 1 and L − 3 for L ≥ 4, given explicitly for L ≤ 8. For L ≤ 11 and p ∈ {3, 5, 7, 11}, P(·, L) mod p has period 2·p^{⌈log_p L⌉} (computed). |P(k, 4)| = A352116(k+1).
tags: [concept, signed-tower-count, quasi-polynomial, k-direction, ehrhart, mod-p, oeis]
sources: [oeis-mining-pe502, project-euler-502-solution, project-euler-502-castle-factoring]
created: 2026-09-19
updated: 2026-10-25
---

# The k-direction of P(k, L) as a quasi-polynomial

`P(k, L)` is the signed tower count of [[signed-tower-count](pages/signed-tower-count.md)]: the sum of `(−1)^{blocks}` over the towers of height at most `k` on a base of length `L`. For fixed `k`, `P(k, ·)` satisfies a linear recurrence in `L` of order `k + 1`, with characteristic polynomial `char_k` ([[castle-counting-formula](pages/castle-counting-formula.md)], the Proposition in the section *Signed tower count*). This page fixes `L` instead and treats `P(·, L)` as a sequence in the tower height `k`.

The rows `L = 2` and `L = 3` show the shape: `P(k, 2) = (−1)^k (k + 1)`, proved on [[signed-tower-count](pages/signed-tower-count.md)], and `P(k, 3) = (−1)^k (k + 1)²`.[^1]

## The characteristic polynomials

For fixed `L`, `P(·, L)` satisfies a linear recurrence in `k`, which the source finds with the Berlekamp-Massey algorithm ([[berlekamp-massey](pages/berlekamp-massey.md)]) to evaluate `P` at large `k`.[^2] Berlekamp-Massey on `P(k, L)` for `k ≤ 80`, and factoring, give the characteristic polynomials of the shortest recurrences for `L ≤ 12`, and the section *Proof of the multiplicities* proves the last row for every `L ≥ 4`:[^3]

```
L = 1:              (x − 1)(x + 1)
L = 2:              (x + 1)²
L = 3:              (x + 1)³
L ≥ 4:              (x + 1)^L (x − 1)^{L−2}
```

So for `L ≥ 4` the order is `2L − 2`. The polynomial `x + 1` is palindromic and `x − 1` anti-palindromic, so `(x + 1)^L (x − 1)^{L−2}` is palindromic when `L` is even and anti-palindromic when `L` is odd, which is the pattern of the coefficient lists on [[closed-form-hunting](pages/closed-form-hunting.md)].

Every eigenvalue is `+1` or `−1`, so `P(k, L)` is a **quasi-polynomial** in `k` of period 2:

```
P(k, L)  =  (−1)^k · A_L(k)  +  B_L(k)                                        (1)
```

with polynomials `A_L` and `B_L`. For `L ≥ 4`, `A_L` has degree `L − 1` and `B_L` degree `L − 3`, the multiplicities of `−1` and `+1` less one. For every `L`, `P(k, L)` is a polynomial in `k` of degree at most `L` on each class of `k` modulo 2 ([[sum-of-three-cubes-castles](pages/sum-of-three-cubes-castles.md)], section *The residue test*), so the eigenvalues are `±1` at every `L` and the characteristic polynomial divides `(x − 1)^{L+1} (x + 1)^L` (the Lemma of [[mod-9-coset-lift](pages/mod-9-coset-lift.md)]); the exact multiplicities `L` and `L − 2` are proved in the section *Proof of the multiplicities*.

The even-block castle counts inherit the shape. In `A^e(w, h) = [h^w − (h−1)^w − P(h−1, w) + P(h−2, w)]/2`, the first two terms are a polynomial in `h` of degree `w − 1`, which `(x − 1)^w` annihilates. So for every `w` the column `A^e(w, ·)` is annihilated by `(x + 1)^w (x − 1)^w = (x² − 1)^w`, which every row of the table above divides, the polynomial that the OEIS-mining notes observed for the columns.[^4]

## The quasi-polynomials A_L, B_L

Equation (1) determines `A_L` and `B_L` by interpolation: the values at even `k` give `B_L + A_L`, and those at odd `k` give `B_L − A_L` (the `quasi_split` snippet on [[castle-snippets-number-theory](pages/castle-snippets-number-theory.md)]). Each row of the table agrees with the column-height dynamic program for all `k ≤ 100`:[^3]

| `L` | `A_L(k)`, degree `L − 1` | `B_L(k)`, degree `L − 3` | `P(k, L)` for `k = 0, 1, 2, …` |
|---|---|---|---|
| 2 | `k + 1` | `0` | `1, −2, 3, −4, 5, …` |
| 3 | `(k + 1)²` | `0` | `1, −4, 9, −16, 25, …` |
| 4 | `(k + 1)(2k + 1)(2k + 3) / 6` | `(k + 1) / 2` | `1, −4, 19, −40, 85, −140, 231, −336, 489, −660` |
| 5 | `k (k + 1)² (k + 2) / 3` | `(k + 1)²` | `1, 0, 33, −64, 225, −384, 833, −1280, 2241, −3200` |
| 6 | `k (k + 1)(k + 2)(2k² + 4k − 1) / 15` | `(k + 1)(2k + 1)(2k + 3) / 3` | `1, 8, 59, −32, 541, −680, 2583, −3520, 8601, −11672` |
| 7 | `(k + 1)²(4k⁴ + 16k³ + 4k² − 24k + 45) / 90` | `(k + 1)²(8k² + 16k + 3) / 6` | `1, 16, 121, 192, 1385, −112, 7889, −5376, 30897, −29040` |
| 8 | `(k + 1)(4k⁶ + 24k⁵ + 25k⁴ − 60k³ + 256k² + 696k + 315) / 315` | `4k (k + 1)(k + 2)(2k + 1)(2k + 3) / 15` | `1, 16, 259, 832, 3973, 5040, 26503, 10624, 117129, −11824` |

At `L = 4`: `A_4(2) = 3·5·7/6 = 35/2` and `B_4(2) = 3/2`, so `P(2, 4) = 35/2 + 3/2 = 19`; and `P(3, 4) = −4·7·9/6 + 2 = −40`.

The leading coefficient of `A_L` is `2^{L−2} / (L − 1)!` for every `L ≥ 1`, and that of `B_L` is `2^{2L−9} / (L − 3)!` for every `L ≥ 4` (section *Proof of the multiplicities*). Since `A_L` has the larger degree, for fixed `L` the size `|P(k, L)|` grows like `2^{L−2} k^{L−1} / (L − 1)!`, a polynomial in `k`, while the number of towers is `T(k, L) = (k + 1)^L`. For `4 ≤ L ≤ 12` (computed):[^3]

- `A_L(−1) = B_L(−1) = 0`, which also holds at `L = 2, 3`;
- `B_6 = 2·A_4`.

The generating function in `k` is `Σ_k P(k, L) y^k = N_L(y) / ((1 + y)^L (1 − y)^{L−2})`. For `L = 4, 5, 6` the numerator `N_L` has degree `2L − 4` and palindromic coefficients:

```
N_4:   1, −2, 10, −2, 1
N_5:   1, 2, 31, −4, 31, 2, 1
N_6:   1, 10, 72, 54, 238, 54, 72, 10, 1
```

## Proof of the multiplicities

In this section `x` marks the width, as in `P_k(x)`. The height step of the [[generalized-dyck-grammar](pages/generalized-dyck-grammar.md)] at `y = −1` is the matrix `[[−1, 2], [x, 1 − 2x]]` acting on `(num_k, den_k)`, with `P_k(x) = num_k / den_k` (Equation (5) of [[castle-counting-formula](pages/castle-counting-formula.md)]). It has trace `−2x` and determinant `−1`, so its eigenvalues are

```
λ_±  =  −x ± s,        s  =  √(1 + x²),        λ_+ λ_−  =  −1,
```

and `num_k = a λ_+^k + b λ_−^k`, `den_k = c λ_+^k + d λ_−^k`, with power series fixed by `k = 0, 1`:

```
a  =  (1 − x + s) / (2s),                    b  =  (s − 1 + x) / (2s),
c  =  (1 − x + x² + s(1 − x)) / (2s),        d  =  ((s − 1)(1 − x) − x²) / (2s).
```

So `a = 1 − x/2 + O(x²)`, `b = x/2 + O(x²)`, `c = 1 − x + O(x²)` and `d = −x²/4 + O(x³)`. The ratio of the eigenvalues is `λ_−/λ_+ = −u` with `u = (x + s)² = exp(2 arsinh x)`, so with `D = (bc − ad)/c² = x/2 + O(x²)`,

```
P_k  =  (a + b(−u)^k) / (c + d(−u)^k)
     =  a/c  +  Σ_{m ≥ 0}  D (−d/c)^m (−1)^{k(m+1)} u^{k(m+1)}.
```

The coefficient of `x^n` in `u^{jk} = exp(2jk arsinh x)` is a polynomial in `k` of degree `n` with leading coefficient `(2j)^n / n!`, and the term `m` starts at `x^{2m+1}`. In the coefficient of `x^L`, the terms with `m` even carry `(−1)^k` and the terms with `m` odd do not:

- `A_L` comes from `m = 0, 2, …`. The term `m = 0`, `D u^k`, has degree `L − 1` with leading coefficient `(1/2) · 2^{L−1}/(L − 1)! = 2^{L−2}/(L − 1)!`, and the others have degree at most `L − 5`.
- `B_L` comes from `a/c`, a constant, and from `m = 1, 3, …`. The term `m = 1`, `D(−d/c) u^{2k}` with `D(−d/c) = x³/8 + O(x⁴)`, has degree `L − 3` with leading coefficient `(1/8) · 4^{L−3}/(L − 3)! = 2^{2L−9}/(L − 3)!`, and the others have degree at most `L − 7`.

So for every `L ≥ 4`, `A_L` has degree exactly `L − 1` and `B_L` exactly `L − 3`, with the leading coefficients above, and the shortest recurrence of `P(·, L)` has the eigenvalue `−1` with multiplicity `L` and `+1` with multiplicity `L − 2`, the last row of the section *The characteristic polynomials*. The same sums give `A_L` and `B_L` at every `L` as coefficients of explicit series in `x`.[^5]

## The row L = 4 in the OEIS

- `|P(k, 4)| = A352116(k + 1)`: `1, 4, 19, 40, 85, 140, 231, 336, 489, 660, …`, the partial sums of the odd triangular numbers `A014493`. The values agree for `k ≤ 44`.[^6]
- The even terms are `P(2m, 4) = (2m + 1)(8m² + 8m + 3)/3 = A063496(m + 1)`. Peter Bala's comment on `A063496` identifies it, with offset 0, as the crystal ball sequence of the `C_3` lattice: the number of points `v = (a, b, c) ∈ Z³` with `a + b + c` even and `(|a| + |b| + |c|)/2 ≤ m`.[^6]
- The odd terms are `P(2m + 1, 4) = −4·C(2m + 3, 3) = −4·A000447(m + 1)`, four times the sum of the first `m + 1` odd squares. Their absolute values are the terms `A199833(m + 1)`, for which the OEIS gives `4·A000447(n)` as an empirical formula.[^6]
- `2·A_4(k) = B_6(k) = (k + 1)(2k + 1)(2k + 3)/3 = A000447(k + 1)`, and `A_5(k) = k (k + 1)² (k + 2)/3 = A112742(k + 1)`, where `A112742(n) = n²(n² − 1)/3`.[^6]

## Periods modulo p

For `1 ≤ L ≤ 11` and `p ∈ {3, 5, 7, 11}`, the sequence `P(·, L) mod p` has period (computed)[^3]

```
2 · p^{⌈log_p L⌉},
```

where `p^{⌈log_p L⌉}` is the least power of `p` that is at least `L`: the period is `2p` while `2 ≤ L ≤ p`, and `2p²` for `p < L ≤ p²`. For example, the periods for `p = 3` are 6 at `L = 2, 3` and 18 at `L = 4, …, 9`, and the period for `p = 7` is 98 at `L = 8`.

The factor 2 is the order of the eigenvalue `−1`, and the power of `p` comes from the eigenvalue multiplicities, by the rule on [[mod-p-observatory](pages/mod-p-observatory.md)] that an eigenvalue of multiplicity `m` multiplies the period by `p^{⌈log_p m⌉}`. With `w = 4 > 3`, it gives the period 18 of `A^e(4, ·)` modulo 3 in that page's table of periods in the height direction.[^3]

## Appearances in Sources

- [[project-euler-502-solution](pages/project-euler-502-solution.md)] - the closed forms of `P(k, 2)` and `P(k, 3)`, a linear recurrence of `P(·, L)` in `k`, and the Berlekamp-Massey path that evaluates it at `k = 10^12`.
- [[oeis-mining-pe502](pages/oeis-mining-pe502.md)] - the observation that `(x² − 1)^w` annihilates the column `A^e(w, ·)`.
- [[project-euler-502-castle-factoring](pages/project-euler-502-castle-factoring.md)] - the block count as total descent, which the column-height dynamic program sums.

## Related Concepts

- [[signed-tower-count](pages/signed-tower-count.md)] - `P(k, L)`, its recurrences of order `k + 1` in `L`, and the closed forms of `P(k, 2)` and `P(k, 3)`.
- [[castle-counting-formula](pages/castle-counting-formula.md)] - the generating functions `P_k(x)` in the `L` direction and the formula for `A^e(w, h)`.
- [[generalized-dyck-grammar](pages/generalized-dyck-grammar.md)] - the height step as a 2 × 2 matrix, whose eigenvalues at `y = −1` give the proof of the multiplicities.
- [[castle-eigenvalue-oeis-crosswalk](pages/castle-eigenvalue-oeis-crosswalk.md)] - the computation behind this page, the Ehrhart-type argument for the eigenvalues `±1`, and the eigenvalues of `char_k` set against the OEIS.
- [[recurrence-discovery](pages/recurrence-discovery.md)] - the orders of the recurrences of `P` found by Berlekamp-Massey in both directions.
- [[closed-form-hunting](pages/closed-form-hunting.md)] - the closed forms of `P(k, 2)` and `P(k, 3)` and the palindromic coefficient lists of the recurrences in `k`.
- [[mod-p-observatory](pages/mod-p-observatory.md)] - periods of the castle counts modulo `p`, including the rule for repeated eigenvalues.
- [[mod-9-coset-lift](pages/mod-9-coset-lift.md)] - the 3-adic part of the column periods of `A^e(w, ·)` modulo 9, and the columns that are uniform modulo 9.
- [[mod-9-equidistribution](pages/mod-9-equidistribution.md)] - the residues of `A^e(w, h)` modulo 9 and how often they avoid 4 and 5.
- [[eigenvalue-continued-fractions](pages/eigenvalue-continued-fractions.md)] - continued fractions of the castle eigenvalues, in which the recurrences in `k` contribute only the roots `±1`.
- [[tower-parity-sectors](pages/tower-parity-sectors.md)] - the factorization of `char_k`, the characteristic polynomial in the `L` direction, by the parity of the last column.
- [[castle-snippets-number-theory](pages/castle-snippets-number-theory.md)] - the snippets `P_table`, `berlekamp_massey` and `quasi_split`.

## Footnotes

[^1]: [[project-euler-502-solution](pages/project-euler-502-solution.md)] §"Recursion for P(k, L)" L115-118 - "P(k, 2) = (-1)^k (k+1), satisfying (λ+1)^2 = 0. P(k, 3) = (-1)^k (k+1)^2, satisfying (λ+1)^3 = 0."
[^2]: [[project-euler-502-solution](pages/project-euler-502-solution.md)] §"Recursion for P(k, L)" L84 and §"The k-direction Berlekamp-Massey path (h > 15000)" L157-165 - "For fixed L, P(k, L) satisfies a linear recurrence in k of order at most about 2L. Consequence: computing P(k, L) for large k is O(L^2 log k) after Berlekamp-Massey finds the recurrence", and "For fixed w, generate P(0, w), P(1, w), ..., P(N-1, w) for N = 4(w+2) + 20 ... Berlekamp-Massey finds the minimal linear recurrence."
[^3]: Verified by execution (Python 3.11 with SymPy, 2026-10-16), with `P(k, L)` from the column-height dynamic program, checked against the sum over all towers for `k ≤ 4`, `L ≤ 5`: Berlekamp-Massey on `P(k, L)` for `k ≤ 80` and factoring, for `L ≤ 12`; the table rows for `L ≤ 8` against `P(k, L)` for `k ≤ 100`; for `L ≤ 12`, the interpolated `A_L`, `B_L` against all `k ≤ 100`, their degrees and leading coefficients, and their values at `−1`; `B_6 = 2A_4`; `N_4`, `N_5`, `N_6`; the periods of `P(·, L) mod p` for `L ≤ 11` and `p ∈ {3, 5, 7, 11}` over `k < 420`; the period 18 of `A^e(4, h) mod 3` over `2 ≤ h < 200`; the annihilation of `A^e(w, ·)` by `(x² − 1)^w` for `w ≤ 7`; `|P(k, 4)|`, `P(2m, 4)` and `−P(2m + 1, 4)` against all the terms of `A352116`, `A063496` and `A199833` shown on oeis.org.
[^4]: [[oeis-mining-pe502](pages/oeis-mining-pe502.md)] `mine-notes.md` §"Vein 3" L77-79 - "Columns (fixed w, varying h) are quasi-polynomials: F(w,h) is annihilated by (x^2-1)^w, i.e. F(w,h) = P(h) + (-1)^h Q(h) with P,Q polynomials of degree < w."
[^5]: Verified by execution (Python 3.11 with SymPy, 2026-10-25): the eigenvalue forms of `num_k` and `den_k` for `k ≤ 7`; the series of `a`, `b`, `c`, `d` and `D`; the `A_L` and `B_L` read off the expansion reproduce `P(k, L)` for `L ≤ 10` and `k ≤ 30`, equal the table for `L = 4, …, 8`, and have the stated degrees and leading coefficients; the recurrence with characteristic polynomial `(x + 1)^L (x − 1)^{L−2}` holds for `P(·, L)` and none with a proper divisor does, for `4 ≤ L ≤ 21` and `k ≤ 79`.
[^6]: https://oeis.org/A352116, https://oeis.org/A063496, https://oeis.org/A199833, https://oeis.org/A000447, https://oeis.org/A112742 (read 2026-10-16) - A352116: "Partial sums of the odd triangular numbers (A014493)", offset 1; A063496: "a(n) = (2*n - 1)*(8*n^2 - 8*n + 3)/3", offset 1, with Peter Bala's remark "The following remarks about the C_3 lattice assume the sequence offset is 0 ... this sequence is the crystal ball sequence for the C_3 lattice ... all integer lattice points v = (a,b,c) in Z^3 such that a + b + c is even, equipped with the taxicab type norm ||v|| = (1/2) * (|a| + |b| + |c|)"; A199833: offset 1, "Empirical: a(n) = (16/3)*n^3 - (4/3)*n = 4*A000447(n)"; A000447: "a(n) = 1^2 + 3^2 + 5^2 + 7^2 + ... + (2*n-1)^2 = n*(4*n^2 - 1)/3"; A112742: "a(n) = n^2*(n^2 - 1)/3".
