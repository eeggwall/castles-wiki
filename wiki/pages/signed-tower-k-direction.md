---
title: The k-direction of P(k, L) as a quasi-polynomial
category: Concepts
summary: At fixed base length L, the signed tower count P(k, L) has k-direction characteristic polynomial (x+1)^L (x-1)^{L-2}, so the only eigenvalues are +1 and -1. P(k, L) is a period-2 quasi-polynomial in k, (-1)^k A_L(k) + B_L(k), with A_L, B_L given explicitly to L = 8; the mod-p period in k is 2·p^{ceil(log_p L)}. Includes the |P(k,4)| = A352116 OEIS hit and its C_3-crystal-ball / tetrahedral bisections.
tags: [concept, signed-tower-count, quasi-polynomial, k-direction, ehrhart, mod-p, oeis]
sources: [oeis-mining-pe502, project-euler-502-solution, project-euler-502-castle-factoring, salem-1963-algebraic-numbers-fourier-analysis]
created: 2026-09-19
updated: 2026-09-25
---

# The k-direction of P(k, L) as a quasi-polynomial

`P(k, L)` is the signed tower count of [[signed-tower-count](pages/signed-tower-count.md)]: the sum of `(−1)^{blocks}` over towers of height at most `k` above a length-`L` base. This page is about what `P(k, L)` looks like as a function of `k` at fixed `L`. The L-direction (fixed `k`, varying `L`) is a C-finite recurrence of order `k + 1` with characteristic polynomial `char_k`, whose roots are the castle's genuinely irrational eigenvalues; that direction is covered on [[signed-tower-count](pages/signed-tower-count.md)] and [[generating-function-gallery](pages/generating-function-gallery.md)]. The k-direction is different: it collapses entirely to eigenvalues `±1`.

## The factorization

The k-direction recurrences of `P(k, L)` at fixed `L` were found by Berlekamp-Massey (BM) on [[recurrence-discovery](pages/recurrence-discovery.md)], with order `2L − 2` for `L ≥ 4` and coefficient lists recorded on [[closed-form-hunting](pages/closed-form-hunting.md)] as "palindromic for even `L`, anti-palindromic for odd `L`". Factoring the characteristic polynomials (BM output + `sp.factor`, verified through `L = 12` with `k ≤ 60`) gives the same shape every time:[^1]

```
L = 4:   (x + 1)^4 (x − 1)^2
L = 5:   (x + 1)^5 (x − 1)^3
L = 6:   (x + 1)^6 (x − 1)^4
…
L:       char_L^{k-dir}(x) = (x + 1)^L (x − 1)^{L−2}.
```

The palindromic / anti-palindromic symmetry is exactly `x + 1` (palindromic) to the `L` and `x − 1` (anti-palindromic) to the `L − 2`. **Every k-direction eigenvalue is `+1` or `−1`**, so `P(k, L)` is a period-2 **quasi-polynomial** in `k`:

```
P(k, L)  =  (−1)^k · A_L(k)  +  B_L(k),        deg A_L ≤ L − 1,   deg B_L ≤ L − 3.
```

**Why it must be so (argument sketch).** `P(k, L)` sums `(−1)^{desc(c)}` over the lattice points `c ∈ {0, …, k}^L`, and the descent `Σ max(0, c_i − c_{i+1})` is a *linear* form on each piece of the cube cut out by the order type of `c`. A sum of a fixed root of unity raised to a linear form over the lattice points of a dilated rational polytope is an **Ehrhart-type quasi-polynomial** in the dilation `k` (Ehrhart's theorem: the number of lattice points in `k · P` for a rational polytope `P` is a quasi-polynomial in `k` of degree `dim P`) whose period divides the order of the root - here 2. So the only possible eigenvalues are `±1`, with `P(k, L) = (−1)^k A_L(k) + B_L(k)`. The first OEIS-mining pass had already seen this shape for the *even-block count*: it noted that the columns `F(w, ·)` are annihilated by `(x²−1)^w`.[^2] What is new is the exact multiplicities: `L` at `−1`, `L − 2` at `+1`, for the signed count.

**A second route to "roots of unity only" (Kronecker).** Take as given that `P(k, L)` is C-finite in `k`. Then its minimal recurrence has integer coefficients and its characteristic polynomial is monic with nonzero integer constant term. Fatou's lemma gives that normalization for any integer sequence with a rational generating function. Because `|P(k, L)| ≤ (k + 1)^L` grows only polynomially, no eigenvalue can exceed modulus 1. The eigenvalues are closed under conjugation, and their product is a nonzero integer, so every eigenvalue has modulus exactly 1. By Kronecker's theorem, an algebraic integer whose conjugates all have modulus 1 is a root of unity. This recovers "no irrational eigenvalues" without Ehrhart, but not the period 2: that needs the sign `(−1)^{desc}`.[^salem3]

A full proof from the Ehrhart route is still open (see IDEAS, "General closed form for `P(k, L)`"); the identity is verified for `L ≤ 12`.

## The quasi-polynomials A_L, B_L

Splitting a period-2 quasi-polynomial from data is two Lagrange interpolations - one on the even terms, one on the odd - which is the `quasi_split` snippet on [[castle-snippets-number-theory](pages/castle-snippets-number-theory.md)]. Applied to `P(k, L)` and verified against the direct dynamic program (DP) for all `k ≤ 60`:[^1]

| `L` | `A_L(k)` (alternating part, degree `L − 1`) | `B_L(k)` (steady part, degree `L − 3`) | `P(k, L)`, `k = 0, 1, 2, …` |
|---|---|---|---|
| 2 | `k + 1` | `0` | `1, −2, 3, −4, 5, …` |
| 3 | `(k + 1)²` | `0` | `1, −4, 9, −16, 25, …` |
| 4 | `(k + 1)(2k + 1)(2k + 3) / 6` | `(k + 1) / 2` | `1, −4, 19, −40, 85, −140, 231, −336, 489, −660` |
| 5 | `k (k + 1)² (k + 2) / 3` | `(k + 1)²` | `1, 0, 33, −64, 225, −384, 833, −1280, 2241, −3200` |
| 6 | `k (k + 1)(k + 2)(2k² + 4k − 1) / 15` | `(k + 1)(2k + 1)(2k + 3) / 3` | `1, 8, 59, −32, 541, −680, 2583, −3520, 8601, −11672` |
| 7 | `(k + 1)²(4k⁴ + 16k³ + 4k² − 24k + 45) / 90` | `(k + 1)²(8k² + 16k + 3) / 6` | `1, 16, 121, 192, 1385, −112, 7889, −5376, 30897, −29040` |
| 8 | `(k + 1)(4k⁶ + 24k⁵ + 25k⁴ − 60k³ + 256k² + 696k + 315) / 315` | `4 k (k + 1)(k + 2)(2k + 1)(2k + 3) / 15` | `1, 16, 259, 832, 3973, 5040, 26503, 10624, 117129, −11824` |

Patterns visible through `L = 12`: the leading coefficient of `A_L` is `2^{L − 2} / (L − 1)!` and that of `B_L` is `2^{2L − 9} / (L − 3)!`, so `|P(k, L)| ~ 2^{L − 2} · k^{L − 1} / (L − 1)!` for fixed `L` - polynomial growth in the height, against `(k + 1)^L` for the unsigned count on [[castle-counting-formula](pages/castle-counting-formula.md)]. `A_L(−1) = 0` and `B_L(−1) = 0` always. `B_6 = 2 · A_4`. The numerators `N_L(y)` of `Σ_k P(k, L) y^k = N_L(y) / ((1 + y)^L (1 − y)^{L − 2})` are themselves palindromic: `1, −2, 10, −2, 1` (`L = 4`), `1, 2, 31, −4, 31, 2, 1` (`L = 5`), `1, 10, 72, 54, 238, 54, 72, 10, 1` (`L = 6`). A uniform formula for `A_L, B_L` is the open item.

## OEIS hits

Checked offset-exact on 2026-09-16:[^3]

- **`|P(k, 4)| = 1, 4, 19, 40, 85, 140, 231, 336, 489, 660, …` is [A352116](https://oeis.org/A352116)**, the partial sums of the odd triangular numbers ([A014493](https://oeis.org/A014493) = `1, 3, 15, 21, 45, 55, 91, 105, …`). Summing them reproduces `|P(k, 4)|`, verified for `k ≤ 39`:

  ```
  >>> odd_tri = [t for t in (m*(m+1)//2 for m in range(1, 40)) if t % 2 == 1]
  >>> [sum(odd_tri[:j+1]) for j in range(10)]
  [1, 4, 19, 40, 85, 140, 231, 336, 489, 660]
  ```

  Read through the quasi-polynomial: `P(2m, 4) = (2m + 1)(8m² + 8m + 3) / 3` is **[A063496](https://oeis.org/A063496)**, whose Peter Bala comment identifies it as the *crystal ball sequence of the C_3 root lattice* (a Pisot-shaped growth that pins down its own root system); and `P(2m + 1, 4) = −4 · C(2m + 3, 3)`, i.e. `|P(2m + 1, 4)|` is **[A199833](https://oeis.org/A199833) = 4 · [A000447](https://oeis.org/A000447)**, four times a tetrahedral number. So the signed height-`k` towers on a length-4 base count, up to sign, lattice points in balls of the `C_3` root lattice (even `k`) and four times a tetrahedral number (odd `k`). A bijective explanation would be a real new interpretation.
- `2 · A_4(k) = B_6(k) = (k + 1)(2k + 1)(2k + 3) / 3` is **A000447** (`= C(2k + 3, 3)`); `A_5(k) = k (k + 1)² (k + 2) / 3` is **[A112742](https://oeis.org/A112742)** (`n²(n² − 1) / 3` at `n = k + 1`).
- `P(k, L)` for `L = 5, 6, 7` and the `N_L` rows have **no OEIS match** - generation candidates, consistent with the mining pass's "columns are new" verdict.[^2]

## Mod-p period: `2 · p^{ceil(log_p L)}`

With all eigenvalues `±1`, the mod-`p` period of `P(·, L)` in `k` comes entirely from the eigenvalue multiplicities - a polynomial part of degree `L − 1` in `k`, with *rational* coefficients (denominators `6, 15, 90, 315, …`), which is why the period can exceed `p`:

```
>>> [(L, [period([P[kk][L] % p for kk in range(261)]) for p in (3, 5, 7)]) for L in (2, 3, 4, 5, 6, 8)]
[(2, [6, 10, 14]), (3, [6, 10, 14]), (4, [18, 10, 14]), (5, [18, 10, 14]), (6, [18, 50, 14]), (8, [18, 50, 98])]
```

The period is `2p` while `L ≤ p` and jumps to `2p²` as soon as `L > p`: `18 = 2 · 3²` at `L = 4`, `50 = 2 · 5²` at `L = 6`, `98 = 2 · 7²` at `L = 8`. Uniform formula (verified for `L ≤ 11`, `p ∈ {3, 5, 7, 11}`):[^1]

```
period_p(P(·, L) in k)  =  2 · p^{ceil(log_p L)}.
```

This is the standard "a repeated eigenvalue of multiplicity `m` contributes `p^{ceil(log_p m)}`" rule of the [[mod-p-observatory](pages/mod-p-observatory.md)], now with the multiplicity known exactly. It accounts for that page's one irregular height-direction entry: `F(4, ·) mod 3` has period 18, not `2p = 6`, because `L = w = 4 > 3`.

## Appearances in Sources

- [[oeis-mining-pe502](pages/oeis-mining-pe502.md)] - the `(x² − 1)^w` observation for the even-block count that this page sharpens to exact multiplicities `(x + 1)^L (x − 1)^{L − 2}` for the signed count.
- [[project-euler-502-solution](pages/project-euler-502-solution.md)] - the `num_k / den_k` recurrence whose k-direction is factored here.
- [[project-euler-502-castle-factoring](pages/project-euler-502-castle-factoring.md)] - the block-count (total descent) formula the `P_table` DP implements.

## Related Concepts

- [[signed-tower-count](pages/signed-tower-count.md)] - `P(k, L)` and its L-direction (C-finite of order `k + 1`).
- [[castle-eigenvalue-oeis-crosswalk](pages/castle-eigenvalue-oeis-crosswalk.md)] - the surrounding analysis: metallic-rung convergents, the norm-`−1` CF-mod-p twin, and the plastic-number L-direction eigenvalue `2ψ²`.
- [[eigenvalue-continued-fractions](pages/eigenvalue-continued-fractions.md)] - the real-number twin of this page's mod-p result.
- [[mod-p-observatory](pages/mod-p-observatory.md)] - the finite-field side; this page's `2 · p^{ceil(log_p L)}` accounts for its irregular `18`.
- [[mod-9-equidistribution](pages/mod-9-equidistribution.md)] - the mod-9 histogram of `F(w, . )` over one h-period; when its period `2 · 3^(1 + ceil(log_3 w))` is divisible by 9, some columns produce exactly uniform histograms (`w = 3^{k-1} + d` for `d in {1, 3, 8}`) and others do not.
- [[mod-9-coset-lift](pages/mod-9-coset-lift.md)] - the mechanism companion: the `(x + 1)^L (x - 1)^{L-2}` char poly of this page is what gives `v_3(per_w) >= 2` and drives the coset-lift proof at `w = 4`.
- [[closed-form-hunting](pages/closed-form-hunting.md)] - the `2L − 2` orders and palindromic coefficient lists factored here.
- [[recurrence-discovery](pages/recurrence-discovery.md)] - where the k-direction recurrences were first extracted by Berlekamp-Massey.
- [[generating-function-gallery](pages/generating-function-gallery.md)] / [[castle-counting-formula](pages/castle-counting-formula.md)] - the L-direction machinery this page is the complementary direction of.
- [[castle-snippets-number-theory](pages/castle-snippets-number-theory.md)] - `P_table`, `quasi_split`, `berlekamp_massey`; the reusable snippets.
- [[tower-parity-sectors](pages/tower-parity-sectors.md)] - the complementary L-direction: `char_k` factors into parity sectors `H_d · V_d` while the k-direction factors as `(x+1)^L (x-1)^{L-2}` here.

## Footnotes

[^1]: Verified by execution (Python 3.11, SymPy 1.14) while writing [[castle-eigenvalue-oeis-crosswalk](pages/castle-eigenvalue-oeis-crosswalk.md)] Part 3. (i) `P_table(60, 12)` + Berlekamp-Massey + `sp.factor`: characteristic polynomial equals `(x + 1)^L (x − 1)^{L − 2}` for every `L = 4..12` (`sp.expand(charpoly − target) == 0`). (ii) `quasi_split` for `L = 1..12`, each `A_L, B_L` re-checked against all 61 DP values; leading coefficients read off as `2^{L − 2} / (L − 1)!` and `2^{2L − 9} / (L − 3)!` for `L ≤ 12`; `N_L(y)` obtained as the truncated series of `(Σ_k P(k, L) y^k) · (1 + y)^L (1 − y)^{L − 2}`, with all coefficients beyond degree `2L − 3` zero. (iii) k-direction periods of `P(·, L) mod p` for `L = 2..11`, `p ∈ {3, 5, 7, 11}` equal `2 · p^j` with `p^j` the least power `≥ L`.

[^2]: [[oeis-mining-pe502](pages/oeis-mining-pe502.md)] `mine-notes.md` §"Vein 3" L77-79 - "Columns (fixed w, varying h) are quasi-polynomials: F(w,h) is annihilated by (x^2-1)^w, i.e. F(w,h) = P(h) + (-1)^h Q(h) with P,Q polynomials of degree < w." and L168 - "F(w,h), w>=3 (columns) | - | NEW (quasi-poly, (x^2-1)^w)".

[^3]: https://oeis.org/A352116 (2026-09-16) - "Partial sums of the odd triangular numbers (A014493)", data `1, 4, 19, 40, 85, 140, 231, 336, 489, 660, 891, 1144, 1469, …`; https://oeis.org/A014493 - "Odd triangular numbers", `1, 3, 15, 21, 45, 55, …`; https://oeis.org/A063496 - "a(n) = (2*n - 1)*(8*n^2 - 8*n + 3)/3", with Peter Bala's comment "this sequence is the crystal ball sequence for the C_3 lattice"; https://oeis.org/A199833 - data `4, 40, 140, 336, 660, 1144, …`, formula "a(n) = (16/3)*n^3 - (4/3)*n = 4*A000447(n)"; https://oeis.org/A000447 - "a(n) = 1^2 + 3^2 + 5^2 + … + (2*n-1)^2 = n*(4*n^2 - 1)/3", "a(n) = binomial(2*n+1, 3)"; https://oeis.org/A112742 - "a(n) = n^2*(n^2 - 1)/3".

[^salem3]: [[salem-1963-algebraic-numbers-fourier-analysis](pages/salem-1963-algebraic-numbers-fourier-analysis.md)] Appendix 3 L4263-4264 - "If an algebraic integer and all its conjugates have all moduli equal to 1, they are all roots of unity"; Ch. I §3 Lemma II (Fatou) L405-410 - integer coefficients ⇒ `P, Q` integral with `Q(0) = 1`. The growth bound and the modulus argument are own reasoning.
