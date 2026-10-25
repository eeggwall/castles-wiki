---
title: The mod-9 coset-lift mechanism
category: Concepts
summary: Why the column w = 4 of A^e mod 9 is exactly uniform, why some columns can be and no row with h ≤ 40 can. P(·, L) satisfies a linear recurrence whose characteristic polynomial divides (x − 1)^{L+1}(x + 1)^L (proved), so for 2 ≤ w ≤ 293 the column A^e(w, ·) mod 9 has minimal period per_w = 2·3^{⌈log_3 w⌉+1}, divisible by 9; the row periods per_h have v_3 = 1 for h ≤ 40 (computed), so no such row is uniform. Over F_3, (x − 1)^2 divides char_k exactly when k ≡ 4 (mod 12), (x + 1)^2 exactly when k ≡ 6 (mod 12), and no cube of a linear factor ever does (proved by a state cycle of length 24); no factor of degree ≥ 2 repeats for k ≤ 200 (computed). An elementary proof shows A^e(4, h) mod 9 hits each residue 6 times per period 54, so the w = 4 column has exclusion rate exactly 2/9. The coset-lift criterion, computed for 2 ≤ w ≤ 293: a column is uniform exactly when the shift-by-per_w/3 differences mod 9 take only the values 3 and 6.
tags: [concept, castle, sum-of-cubes, mod-9, periodicity, coset-lift, elementary-proof, three-adic, characteristic-polynomial]
sources: [oeis-mining-pe502, project-euler-502-solution]
created: 2026-09-22
updated: 2026-10-25
---

# The mod-9 coset-lift mechanism

No integer `≡ 4` or `5 (mod 9)` is a sum of three cubes, since every cube is `0` or `±1` mod 9 ([[sums-of-three-cubes](pages/sums-of-three-cubes.md)]). For a set of castle counts, the **exclusion rate** is the proportion of them `≡ 4` or `5 (mod 9)`; if the residues mod 9 are equidistributed it is `2/9`. [[mod-9-equidistribution](pages/mod-9-equidistribution.md)] computes these rates for the castle counts `A^e(w, h)` (the `F(w, h)` of the problem statement): the columns `w = 4, 6, 10, 12, 17, 28, 30, 35, 82, 84, 89, 244, 246, 251` are exactly uniform mod 9 for `w ≤ 293`, and no row with `h ≤ 40` is. This page gives three results behind that finding.

1. **The row/column divisibility gap.** For `2 ≤ w ≤ 293` the column period is divisible by 9; for `h ≤ 40` the row period is divisible by 3 and not by 9. A sequence can be uniform mod 9 over one period only if 9 divides the period.
2. **The `w = 4` proof.** An elementary argument shows that `A^e(4, ·) mod 9` hits every residue 6 times in each period of 54.
3. **The coset-lift criterion.** For `2 ≤ w ≤ 293` (computed), the column `w` is uniform exactly when the differences `A^e(w, h + per_w/3) − A^e(w, h) mod 9` take only the values 3 and 6.

A **coset lift** is the step used in results 2 and 3: a value mod 9 is a residue mod 3 together with a choice inside its coset `r + 3Z/9`, and a shift of `h` that preserves the residue mod 3 moves the value inside the coset. When the shift by `per_w/3` always moves the value by 3 or 6, the three shifts of one `h` cover the whole coset.

## The recurrence in the tower height

**Lemma.** For fixed `L`, the sequence `P(·, L)` satisfies a linear recurrence whose characteristic polynomial divides `(x − 1)^{L+1}(x + 1)^L`.

*Proof.* Let `c ∈ {0, …, k}^L` be the column heights of towers, with `c_0 = 0`, and let `0 = v_0 < v_1 < ⋯ < v_r` be the distinct values among `0, c_1, …, c_L`, so `r ≤ L`. Fix the pattern, which `c_i` takes which value `v_{a_i}`, and write `d_j = v_j − v_{j−1} ≥ 1`. Then `blocks(c) = Σ_i max(0, c_i − c_{i−1}) = Σ_j b_j d_j`, with `b_j` the number of `i` such that `a_{i−1} < j ≤ a_i`. So with `s_j = (−1)^{b_j}`, the towers of this pattern and height at most `k` contribute `Σ s_1^{d_1} ⋯ s_r^{d_r}` over `d_j ≥ 1`, `d_1 + ⋯ + d_r ≤ k`, and

```
Σ_{k ≥ 0} t^k · (contribution at k)  =  1/(1 − t) · Π_{j=1}^{r} s_j t/(1 − s_j t).
```

Summing over the finitely many patterns, `Σ_k P(k, L) t^k` is a proper rational function whose denominator divides `(1 − t)^{L+1}(1 + t)^L`. ∎

In particular `P(k, L)` is a polynomial in `k` of degree at most `L` on each class of `k` modulo 2, the form in which [[sum-of-three-cubes-castles](pages/sum-of-three-cubes-castles.md)] proves it. The characteristic polynomial, `(x + 1)^L (x − 1)^{L−2}` for every `L ≥ 4`, is a divisor ([[signed-tower-k-direction](pages/signed-tower-k-direction.md)]). For fixed `w`, the column `A^e(w, ·) mod 9` therefore satisfies a linear recurrence of order `2w + 1`, since `h^w − (h−1)^w` is a polynomial of degree `w − 1` in `h`. A period checked on `2w + 1` consecutive values of `h` is a period for all `h ≥ 2`.

## The row/column divisibility gap

| direction | period mod 9 | `v_3(period)` | 9 divides? |
|---|---|---|---|
| columns (fixed `w`, `2 ≤ w ≤ 293`) | `per_w = 2 · 3^{⌈log_3 w⌉ + 1}` | `⌈log_3 w⌉ + 1 ≥ 2` | yes |
| rows (fixed `h`, `h ≤ 40`) | divides `per_h = lcm(ord_9(h), ord_9(h−1), per_9(char_{h−1}), per_9(char_{h−2}))` | `1` | no |

Here `ord_9(a)` is the order of `a` mod 9, taken as 1 when `3 | a` (then `a^w ≡ 0` for `w ≥ 2`), and `per_9(char_k)` is the order of `x` in `Z/9[x]/(char_k)`. Row periods `per_h` for `h = 2, …, 16`:[^exec]

| `h` | `per_h` | factorization | `v_3` |
|---|---|---|---|
| 2 | 24 | `2^3 * 3` | 1 |
| 3 | 24 | `2^3 * 3` | 1 |
| 4 | 240 | `2^4 * 3 * 5` | 1 |
| 5 | 3120 | `2^4 * 3 * 5 * 13` | 1 |
| 6 | 2184 | `2^3 * 3 * 7 * 13` | 1 |
| 7 | 2184 | `2^3 * 3 * 7 * 13` | 1 |
| 8 | 2184 | `2^3 * 3 * 7 * 13` | 1 |
| 9 | 10920 | `2^3 * 3 * 5 * 7 * 13` | 1 |
| 10 | 21840 | `2^4 * 3 * 5 * 7 * 13` | 1 |
| 11 | 21840 | `2^4 * 3 * 5 * 7 * 13` | 1 |
| 12 | 11514360 | `2^3 * 3 * 5 * 11^2 * 13 * 61` | 1 |
| 13 | 177144 | `2^3 * 3 * 11^2 * 61` | 1 |
| 14 | 1771440 | `2^4 * 3 * 5 * 11^2 * 61` | 1 |
| 15 | 25170390960 | `2^4 * 3 * 5 * 11^2 * 13 * 61 * 1093` | 1 |
| 16 | 88096368360 | `2^3 * 3 * 5 * 7 * 11^2 * 13 * 61 * 1093` | 1 |

For `h ≤ 11`, `per_h` is the minimal period of `A^e(·, h) mod 9` from `w = 2` (computed from the recurrence of `P(k, ·)` in the base length). The same computation gives `v_3(per_h) = 1` for every `h ≤ 40`.

**Columns.** For `2 ≤ w ≤ 293`, `per_w` is the minimal period of `A^e(w, ·) mod 9` from `h = 2`: the values, computed from `P(k, w) mod 9` for `k ≤ 6600`, repeat with period `per_w` over more than `2w + 1` consecutive `h` and with no proper divisor of it, and the Lemma extends the period to every `h`.[^exec] The form of `per_w` follows from the computed characteristic polynomial. In `Z/9[x]/((x + 1)^w)` put `N = x + 1`, so `x^{2n} = (1 − N)^{2n} = Σ_j C(2n, j)(−N)^j`. Since `j · C(n, j) = n · C(n − 1, j − 1)`, `3^{e − v_3(j)}` divides `C(2 · 3^e, j)`, so `x^{2·3^e} = 1` once `e ≥ 2 + v_3(j)` for every `j < w`, that is for `e = ⌈log_3 w⌉ + 1`; the factor `(x − 1)^{w−2}` needs no more, and the two factors are coprime because `(x + 1) − (x − 1) = 2` is a unit mod 9. For `w ≥ 2`, `9 | per_w`.

**Rows.** The multiplicative orders `ord_9(h)` and `ord_9(h−1)` divide `φ(9) = 6`, with `φ` Euler's totient. For each `char_k`, the order of `x` mod 9 is its order `N` mod 3 or `3N`: if `x^N = 1 + 3g`, then `x^{3N} = 1` mod 9. The order mod 3 has 3-adic valuation exactly `⌈log_3 m⌉`, with `m` the largest multiplicity of a factor of `char_k mod 3`, because the orders of the irreducible factors are prime to 3 and a factor of multiplicity `m` contributes exactly `3^{⌈log_3 m⌉}` ([[larger-prime-periodicity](pages/larger-prime-periodicity.md)], section *The period from the factorization*). So `v_3(per_9(char_k)) ≤ 1 + ⌈log_3 m⌉`.

**Theorem.** Over `F_3`, `(x − 1)^2` divides `char_k` exactly when `k ≡ 4 (mod 12)`, `(x + 1)^2` divides `char_k` exactly when `k ≡ 6 (mod 12)`, and neither `(x − 1)^3` nor `(x + 1)^3` divides any `char_k`.

*Proof.* Modulo 3 the recurrence `char_{k+1} = x^2 char_{k−1} − 2 char_k` is `char_{k+1} = x^2 char_{k−1} + char_k`. At `x_0 = ±1`, using `x_0^2 = 1` and `4 ≡ 1`, the values `y_k = char_k(x_0)`, `z_k = char_k′(x_0)` and `u_k = char_k″(x_0)` mod 3 satisfy

```
y_{k+1}  =  y_{k-1} + y_k
z_{k+1}  =  2 x_0 y_{k-1} + z_{k-1} + z_k
u_{k+1}  =  2 y_{k-1} + x_0 z_{k-1} + u_{k-1} + u_k
```

The state `(y_{k−1}, y_k, z_{k−1}, z_k, u_{k−1}, u_k)` lies in `F_3^6` and evolves by a fixed linear map, starting from `(0, 1, 1, 0, 0, 2)` at `x_0 = 1` and `(1, 2, 1, 2, 0, 2)` at `x_0 = −1`. In both cases the state sequence is periodic from `k = 0` with period 24. Over one period, `(y_k, z_k) = (0, 0)` exactly at `k = 4, 16` for `x_0 = 1` and at `k = 6, 18` for `x_0 = −1`, and `(y_k, z_k, u_k) = (0, 0, 0)` never.[^exec] Since `2` is invertible mod 3, `(x − x_0)^3` divides `char_k` exactly when `y_k = z_k = u_k = 0`, and `(x − x_0)^2` exactly when `y_k = z_k = 0`. ∎

No irreducible factor of degree at least 2 of `char_k mod 3` is repeated for `k ≤ 200` (computed). So for `k ≤ 200` the largest multiplicity is 2, at `k ≡ 4, 6 (mod 12)`, and `v_3(per_9(char_k)) ≤ 2`. The computed value is `v_3 = 1` for every `1 ≤ k ≤ 40`: at the squarefree `k` the lift from 3 to 9 multiplies the order by 3, and at `k ≡ 4, 6 (mod 12)` it does not. Hence `v_3(per_h) = 1` for every `h ≤ 40`.

**Consequence for uniformity.** If `9 ∤ per_h`, the period of the row `A^e(·, h) mod 9`, which divides `per_h`, is not divisible by 9, so the nine residues cannot occur equally often over one period and the row's exclusion rate differs from `2/9`. This bound alone does not say how far from `2/9` the rows are. If `9 | per_w`, uniformity is possible, and it occurs for the columns listed in the introduction.

## The `w = 4` proof

**Theorem.** `A^e(4, ·) mod 9` has period 54, and each residue mod 9 occurs exactly 6 times in each period. So the exclusion rate of the column `w = 4` is exactly `12/54 = 2/9`.

The proof is elementary and uses no conjecture on sums of three cubes.

*Step 1. Closed form.* `P(k, 4) = (−1)^k A_4(k) + B_4(k)` with `A_4(k) = (k+1)(2k+1)(2k+3)/6` and `B_4(k) = (k+1)/2` ([[signed-tower-k-direction](pages/signed-tower-k-direction.md)]). Both sides satisfy the recurrence of the Lemma, of order 9, and they agree for `k = 0, …, 8` (computed by summing over all towers), so they agree for all `k`. Substituting into `A^e(4, h) = (h^4 − (h−1)^4 − P(h−1, 4) + P(h−2, 4))/2` ([[castle-counting-formula](pages/castle-counting-formula.md)], Equation (1)) gives

```
12 · A^e(4, h)  =  (24 h^3 − 36 h^2 + 24 h − 9)  +  (−1)^h (8 h^3 − 12 h^2 + 10 h − 3).
```

It gives `A^e(4, 2) = 10`, `A^e(4, 3) = 21`, `A^e(4, 4) = 117`, `A^e(4, 5) = 122` and `A^e(4, 7) = 367`, which agree with enumeration of the castles.

*Step 2. Split by parity.* For `h = 2m` and `h = 2m + 1`,

```
A^e(4, 2m)      =  Q_e(m)/3,     Q_e(m)  =  64 m^3 − 48 m^2 + 17 m − 3,
A^e(4, 2m + 1)  =  Q_o(m)/3,     Q_o(m)  =  32 m^3 + 24 m^2 + 7 m.
```

Modulo 3, `Q_e ≡ m^3 − m` and `Q_o ≡ −(m^3 − m)`, which vanish for every integer `m` by Fermat's little theorem.

*Step 3. Uniform mod 3.* `A^e(4, 2m) mod 3 = (Q_e(m) mod 9)/3`, and `Q_e(m) ≡ m^3 + 6m^2 + 8m + 6 (mod 9)`. For `m = 0, …, 8`, `Q_e mod 9 = 6, 3, 0, 3, 0, 6, 0, 6, 3`, so `A^e(4, 2m) mod 3 = 2, 1, 0, 1, 0, 2, 0, 2, 1`, each residue three times. The same evaluation gives `A^e(4, 2m + 1) mod 3 = 0, 0, 2, 1, 1, 0, 2, 2, 1`, again three of each.

*Step 4. Coset lift.* For a cubic `Q(m) = a_3 m^3 + a_2 m^2 + a_1 m + a_0`,

```
Q(m + 9) − Q(m)  =  27 a_3 m^2 + (243 a_3 + 18 a_2) m + 729 a_3 + 81 a_2 + 9 a_1  ≡  18 a_2 m + 9 a_1   (mod 27).
```

For `Q_e` and `Q_o`, `3 | a_2` (`a_2 = −48` and `24`), so the difference is the constant `9 a_1 mod 27`: `9 · 17 ≡ 18` for `Q_e` and `9 · 7 ≡ 9` for `Q_o`. The difference over a shift of 18 is twice that. Dividing by 3,

```
A^e(4, 2(m + 9)) − A^e(4, 2m)          ≡  6 (mod 9),     A^e(4, 2(m + 18)) − A^e(4, 2m)          ≡  3 (mod 9),
A^e(4, 2(m + 9) + 1) − A^e(4, 2m + 1)  ≡  3 (mod 9),     A^e(4, 2(m + 18) + 1) − A^e(4, 2m + 1)  ≡  6 (mod 9).
```

The shift by 27 in `m` adds `3 · 18 ≡ 0` or `3 · 9 ≡ 0 (mod 27)` to `Q`, so `A^e(4, h + 54) ≡ A^e(4, h) (mod 9)`: 54 is a period.

*Step 5. Cosets.* For every `h`, the three values `A^e(4, h)`, `A^e(4, h + 18)`, `A^e(4, h + 36)` mod 9 are `v`, `v + 6`, `v + 3` or `v`, `v + 3`, `v + 6`, the whole coset `v + 3Z/9`.

*Step 6. Counting.* On the even side, the nine values `m = 0, …, 8` fall three into each class mod 3 (Step 3), and each lifts to the three residues of its coset at `m`, `m + 9`, `m + 18` (Step 5). So over `m = 0, …, 26` each residue mod 9 occurs 3 times. The odd side is the same. Over one period of 54 values of `h`, each residue occurs `3 + 3 = 6` times, the residues 4 and 5 together 12 times. ∎

The proof uses three properties of `Q_e` and `Q_o`: `3 | a_2`, `3 ∤ a_1`, and uniformity of the values mod 3 over `m mod 9`. The coset-lift criterion (section *The coset-lift criterion*) is the computed counterpart for other columns.

## The coset-lift criterion

For `2 ≤ w ≤ 293` (computed):[^exec]

```
the column w is uniform mod 9   ⇔   { A^e(w, h + per_w/3) − A^e(w, h)  mod 9 : one period of h }  =  {3, 6}.
```

The differences always lie in `3Z/9`. At the 14 uniform columns the set is `{3, 6}`. At every other column with `w ≥ 3` it is `{0, 3, 6}`, and at `w = 2` it is `{0, 3}`: some `h` has `A^e(w, h + per_w/3) ≡ A^e(w, h) (mod 9)`, a fixed point of the coset shift. In the `w = 4` proof the shift by `per_w/3 = 18` moves the even values by 6 and the odd values by 3, never by 0.

**The offsets.** The uniform columns are `w = 3^{k−1} + d` with `d ∈ {1, 3, 8}` for `k = 3, 4, 5, 6` and `d ∈ {1, 3}` for `k = 2` ([[mod-9-equidistribution](pages/mod-9-equidistribution.md)], section *The column reading*). Other columns in the same residue class mod 9, such as `w = 19` and `w = 37`, have a fixed point. The criterion is computed, not proved, and does not explain the offsets.

## Appearances in Sources

- [[oeis-mining-pe502](pages/oeis-mining-pe502.md)] - the tables of `A^e(w, h)` whose residues mod 9 are studied here.
- [[project-euler-502-solution](pages/project-euler-502-solution.md)] - the recurrences of `P(k, L)` in the base length and in the tower height.

## Related Concepts

- [[mod-9-equidistribution](pages/mod-9-equidistribution.md)] - the row and column histograms mod 9, the uniform and rate-matched columns, and the aggregate rate over cells with `A ≤ N`.
- [[sum-of-three-cubes-castles](pages/sum-of-three-cubes-castles.md)] - which castle counts are sums of three cubes.
- [[sums-of-three-cubes](pages/sums-of-three-cubes.md)] - the residues 4 and 5 mod 9 and Heath-Brown's conjecture.
- [[mod-p-observatory](pages/mod-p-observatory.md)] - the periods of `A^e` modulo a prime and the factor `p^{⌈log_p m⌉}` of a repeated factor.
- [[larger-prime-periodicity](pages/larger-prime-periodicity.md)] - the proof that a factor of multiplicity `m` multiplies the order by exactly `p^{⌈log_p m⌉}`, and the repeated factors of `char_k` modulo larger primes.
- [[signed-tower-k-direction](pages/signed-tower-k-direction.md)] - the closed forms `P(k, L) = (−1)^k A_L(k) + B_L(k)` and the characteristic polynomial `(x + 1)^L (x − 1)^{L−2}`, proved for every `L ≥ 4`.
- [[castle-counting-formula](pages/castle-counting-formula.md)] - the formula for `A^e(w, h)` used in the `w = 4` proof.
- [[castle-ring-spectrum](pages/castle-ring-spectrum.md)] - the fibers of `char_k` over 3 and their nilradicals.

## Footnotes

[^exec]: Verified by execution (Python 3.11 with SymPy and NumPy, 2026-10-16). The state cycle of the Theorem at `x_0 = ±1` (period 24, the pair zeros, no triple zero) and the factorization of `char_k mod 3` for `k ≤ 200` (repeated factors exactly `(x − 1)^2` at `k ≡ 4` and `(x + 1)^2` at `k ≡ 6 (mod 12)`, none of degree ≥ 2). The orders of `x` in `Z/9[x]/(char_k)` for `k ≤ 40` (from the order mod 3, by fast exponentiation, and a test of `x^N = 1` mod 9), with `v_3 = 1` for `1 ≤ k ≤ 40` and the lift from 3 to 9 multiplying the order by 3 exactly at the squarefree `k`, and the row periods `per_h` for `h ≤ 40`; for `h ≤ 11`, `per_h` equals the minimal period of `A^e(·, h) mod 9` from `w = 2`, computed from the recurrence of `P(k, ·)` given by `den_k`. `P(k, L) mod 9` for `k ≤ 6600` and `L ≤ 293` from the series `num_k/den_k` truncated at degree 293, checked against summation over all towers for small `k, L`; from it, for each `2 ≤ w ≤ 293`, the minimal period `per_w` of `A^e(w, ·) mod 9`, the histogram over one period, the uniform columns, and the difference sets of the criterion. The `w = 4` proof: `P(k, 4)` by summation for `k ≤ 8`, the closed form against the formula for `h < 40`, `Q_e` and `Q_o` against `A^e(4, 2m)` and `A^e(4, 2m + 1)` for `m ≤ 27`, the residues of Step 3, the differences of Step 4 as polynomials mod 27, and the histogram `[6, 6, 6, 6, 6, 6, 6, 6, 6]` over `h = 2, …, 55`.
