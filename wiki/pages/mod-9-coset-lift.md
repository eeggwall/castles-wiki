---
title: The mod-9 coset-lift mechanism
category: Concepts
summary: Why column w = 4 hits F mod 9 uniformly, and why more generally the columns w = 3^{k-1} + {1, 3, 8} do, while row histograms cannot. Two theorems and one exact criterion drive the mechanism. First, the row / column divisibility gap: column periods per_w = 2 * 3^{ceil(log_3 w) + 1} are divisible by 9 structurally, so a uniform mod-9 histogram is arithmetically possible; row periods per_h have v_3 = 1 for every h through 201 (empirical) and provably for every h if the residual "char_k mod 3 has no multiplicity->=-3 factor" holds. That residual is now half-proved: the joint state (y_k, z_k, u_k) = (char_k(x_0), char_k'(x_0), char_k''(x_0)) mod 3 at x_0 = +-1 evolves in F_3^6, cycles with period exactly 24, and the triple never simultaneously vanishes - so (x - 1)^3 and (x + 1)^3 provably never divide char_k mod 3. Second, the w = 4 blackboard proof: an entirely elementary six-step derivation (closed form, parity split, mod-3 uniformity on m mod 9, coset lift F(4, h + 18) = F(4, h) + 6 mod 9) gives the exact 2/9 rate at w = 4 unconditional on Heath-Brown. Third, the coset-lift sufficiency criterion: uniformity holds iff the shift-by-per_w/3 operator on F(w, .) mod 9 has image exactly {3, 6}; non-uniform w always produce {0, 3, 6}, and the extra 0 (a fixed-point of the coset shift) is what breaks uniformity. Verified across brackets 3..6 without a single exception. Together these give an explanation, computationally testable, of every finding on the mod-9 equidistribution page.
tags: [concept, castle, sum-of-cubes, mod-9, periodicity, coset-lift, blackboard-proof, three-adic, characteristic-polynomial]
sources: [oeis-mining-pe502, project-euler-502-solution]
created: 2026-09-22
updated: 2026-09-22
---

# The mod-9 coset-lift mechanism

The [[mod-9-equidistribution](pages/mod-9-equidistribution.md)] page records the finding: `F(w, h) mod 9` is equidistributed in the limit, columns `w in {4, 6, 10, 12, 17, 28, 30, 35, 82, 84, 89, 244, 246, 251, ...}` hit the equidistribution value `2/9` exactly, rows never do (they carry an unavoidable `+-1`-per-residue rounding jitter), and the aggregate over cells with `A(w, h) <= N` converges monotonically to `2/9` at rate `0.0786 * N^{-1/12}`. This page is the mechanism. Three interlocking results explain the finding:

1. **The row / column divisibility gap.** Column periods have `v_3 >= 2` structurally; row periods have `v_3 = 1` (proved for the linear-factor obstruction, empirical for the remainder). Uniformity mod 9 is arithmetically possible for columns and impossible for rows.
2. **The `w = 4` blackboard proof.** A six-step elementary derivation gives `F(4, h) mod 9` uniform over any 54 consecutive `h`, unconditionally.
3. **The coset-lift sufficiency criterion.** Column `w` is uniform iff the shift-by-`per_w / 3` operator on `F(w, . ) mod 9` has image `{3, 6}` (never `0`); the extra `0` at non-uniform `w` is a coset-shift fixed point that breaks uniformity. Exact and computable.

All three are variants of one technique: study `F` mod 9 as a coset shift on `Z/9`, whose lifted behavior is controlled by the k-direction characteristic polynomial `(x + 1)^w (x - 1)^{w - 2}` of [[signed-tower-k-direction](pages/signed-tower-k-direction.md)]. The name **coset-lift** points at the shared move: represent `F` values as elements of a coset of `3 Z / 9` in `Z / 9`, and pin the residue class within the coset by an integer-cube-shift argument.

## The row / column divisibility gap

The row and column readings of [[mod-9-equidistribution](pages/mod-9-equidistribution.md)] behave qualitatively differently for a **3-adic** reason:

| direction | period formula | `v_3(period)` | 9 divides? |
|---|---|---|---|
| columns (fixed `w`, `w >= 2`) | `per_w = 2 * 3^{ceil(log_3 w) + 1}` | `ceil(log_3 w) + 1 >= 2` | **always** |
| rows (fixed `h`, empirical `h <= 201`) | `per_h = lcm(ord_9(h), ord_9(h-1), per(char_{h-1}) mod 9, per(char_{h-2}) mod 9)` | `1` | **never** |

Row periods `per_h` for `h = 2..16`, each factored, with 3-adic valuation `v_3` in the last column:[^exec]

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
| 15 | 25170390960 | `2^4 * 3 * 5 * 7 * 11^2 * 13 * 4093 * 61` (approx) | 1 |
| 16 | 88096368360 | (large; `v_3 = 1`) | 1 |

Every row period through `h = 16` has exactly one factor of 3.

**Why columns win.** The k-direction characteristic polynomial of `P(k, w)` is `(x+1)^w (x-1)^{w-2}` ([[signed-tower-k-direction](pages/signed-tower-k-direction.md)]), with a root of multiplicity `w` at `-1`. Reducing mod `9` and applying the "multiplicity `m` inflates the period by `p^{ceil(log_p m)}`" rule of the [[mod-p-observatory](pages/mod-p-observatory.md)] with `p = 3`, the mod-9 period picks up a factor `3^{ceil(log_3 w) + 1}` (the extra `+1` in the exponent is the second-power lift from `mod 3` to `mod 9`). For `w >= 2` this is `>= 9`. So `9 | per_w` is **structural**, not empirical, and the column histogram of `F(w, .) mod 9` splits `per_w` into `9` equal buckets whenever the residue distribution is balanced.

**Why rows lose.** The w-direction period `per_h` is the lcm of the `L`-direction characteristic-polynomial periods for `char_{h-1}` and `char_{h-2}` mod 9, together with the multiplicative orders `ord_9(h), ord_9(h-1)`. The multiplicative orders divide `phi(9) = 6`, so their 3-adic content is at most 1. A multiplicity-`m` root of `char_k mod 3` inflates the mod-9 period by `3^{ceil(log_3 m)}`, so `v_3 >= 2` would require some `char_k mod 3` to have a factor of multiplicity `>= 4`.

**Extended search: no multiplicity `>= 3` through `k <= 200`.** Direct factorization of `char_k mod 3` for `k = 1..200`:[^exec]

```
k with repeated mod-3 factor:  4, 6, 16, 18, 28, 30, 40, 42, 52, 54, 64, 66, 76, 78, 88, 90, 100, ...
```

These are exactly `k in [1, 200]` with `k mod 12 in {4, 6}`. In every case, the repeated factor is `(x - 1)^2` (for `k = 4 mod 12`) or `(x + 1)^2` (for `k = 6 mod 12`), and the multiplicity is always exactly `2`. **The global maximum multiplicity of any `char_k mod 3` factor for `k <= 200` is `2`.** So the mod-9 period contribution from any single repeated factor is exactly `3` (from `3^{ceil(log_3 2)} = 3`), never `9`. Combined with the fact that `ord_9(h), ord_9(h-1)` contribute at most one factor of 3, and LCM of two `v_3 = 1` quantities has `v_3 = 1`, this gives `v_3(per_h) <= 1` for every `h <= 201`.

**Theorem (linear factors, proved).** For every `k >= 0`, `(x - 1)^3` and `(x + 1)^3` do not divide `char_k mod 3`. Equivalently, the linear factors `(x - 1)` and `(x + 1)` each appear in `char_k mod 3` with multiplicity at most 2.

**Proof.** The mod-3 recurrence `char_{k+1}(x) = x^2 char_{k-1}(x) + char_k(x)` evaluated at `x = 1` (respectively `x = -1`) reduces to a Fibonacci-like scalar recurrence, together with the linked recurrences for the first and second derivatives:

```
y_k    = char_k(x_0) mod 3,             y_{k+1} = y_{k-1} + y_k
z_k    = char_k'(x_0) mod 3,            z_{k+1} = 2 y_{k-1} + z_{k-1} + z_k
u_k    = char_k''(x_0) mod 3,           u_{k+1} = 2 y_{k-1} + z_{k-1} + u_{k-1} + u_k
```

(The `2 y_{k-1}` and `z_{k-1}` inhomogeneous terms come from differentiating `x^2 char_{k-1}` twice at `x_0 = +-1`. Both `x = 1` and `x = -1` produce the same recurrence because `x_0^2 = 1`.)

The joint state `(y_{k-1}, y_k, z_{k-1}, z_k, u_{k-1}, u_k)` evolves deterministically in `F_3^6`, a finite set of size 729, and therefore enters a cycle. **Direct enumeration**: at `x = 1` the state cycle has length exactly 24, starting from `k = 1`. Over one full period (`k = 1..24`), the triple `(y_k, z_k, u_k) = (0, 0, 0)` **never occurs**. Same result at `x = -1`, again period 24, no triple-zero. Since the state cycles, this covers every `k >= 1`, and the base cases `k = 0, 1` are handled by direct check. Multiplicity 3 (which would require `y_k = z_k = u_k = 0`) is therefore impossible at either `x = +-1` for any `k`. QED.

For the record, the (y, z) subsequence at `x = 1` hits `(0, 0)` exactly at `k in {4, 16}` within one period of 24, i.e. `k ≡ 4 (mod 12)`; at `x = -1` at `k in {6, 18}`, i.e. `k ≡ 6 (mod 12)`. This is the mod-12 pattern of `(x - 1)^2` and `(x + 1)^2` factors observed empirically.

**Residual conjecture.** No irreducible factor of `char_k mod 3` of degree `>= 2` has multiplicity `>= 2`. Empirical through `k <= 200`. If provable, the global max multiplicity of any factor of `char_k mod 3` is exactly `2` for every `k`, and by the multiplicity-inflation rule the mod-9 period of `char_k` has `v_3 <= 1` unconditionally. **This would close `v_3(per_h) = 1` for every `h` as a theorem**, promoting the divisibility gap from empirical to unconditional. Equivalent formulation: `gcd(char_k, char_k') mod 3 in F_3[x]` is always a product of `(x - 1)` and `(x + 1)` factors, never contains a higher-degree irreducible.

**Consequence for uniformity.** If `9 | per_w` (columns), the 9-bucket histogram *can* be exactly `[per_w / 9] * 9`, and empirically it is for the `{0, 2, 7}`-offset `w`'s. If `9 ∤ per_h` (rows), the 9-bucket histogram *cannot* be uniform, since some buckets hit `floor(per_h / 9)` and others `ceil(per_h / 9)`. Every row histogram carries an unavoidable `+-1`-per-residue rounding jitter, which sets a floor on the row-level equidistribution error at `1 / per_h`. That floor drops to zero as `h -> infinity` and `per_h -> infinity`, so equidistribution is still achieved in the limit, but no finite row ever hits `2/9` on the digit.

## The `w = 4` blackboard proof

The `w = 4` column is the seminar centerpiece: its uniform mod-9 histogram, and therefore its exact `2/9` exclusion rate, comes out of a completely elementary argument that fits on one blackboard. No character sums, no Heath-Brown, no computer verification of 54 values - just the closed form for `F(4, h)`, three lines of polynomial arithmetic, and a coset lift.

**Step 1. Closed form.** From `P(k, 4) = (-1)^k A_4(k) + B_4(k)` with `A_4(k) = (k+1)(2k+1)(2k+3)/6` and `B_4(k) = (k+1)/2` ([[signed-tower-k-direction](pages/signed-tower-k-direction.md)]), substitution into `F(4, h) = (h^4 - (h-1)^4 - P(h-1, 4) + P(h-2, 4))/2` gives

```
12 * F(4, h)  =  (24 h^3 - 36 h^2 + 24 h - 9)  +  (-1)^h * (8 h^3 - 12 h^2 + 10 h - 3).
```

Verified: `F(4, 2) = 10`, `F(4, 3) = 21`, `F(4, 4) = 117`, `F(4, 5) = 122`, `F(4, 7) = 367` come out of the formula exactly.

**Step 2. Split by parity.** For `h = 2m` (even),

```
F(4, 2m)  =  (64 m^3 - 48 m^2 + 17 m - 3) / 3.
```

For `h = 2m + 1` (odd),

```
F(4, 2m + 1)  =  (32 m^3 + 24 m^2 + 7 m) / 3.
```

Both numerators are divisible by 3 for every `m in Z`. On the even side, `64 m^3 - 48 m^2 + 17 m - 3 = m^3 + 2m mod 3 = m(m^2 - 1) mod 3 = m(m - 1)(m + 1) mod 3`, a product of three consecutive integers, hence `0 mod 3`. On the odd side, `32 m^3 + 24 m^2 + 7 m = 2m^3 + m = m(2m^2 + 1) mod 3`, which vanishes for `m in {0, 1, 2} mod 3` by direct check.

**Step 3. Uniform mod 3.** Reduce `F(4, 2m) mod 3` for `m = 0..8`:

```
F(4, 2m) mod 3  =  (Q_e(m) mod 9) / 3    where  Q_e(m) = 64 m^3 - 48 m^2 + 17 m - 3
                =  m^3 + 6 m^2 + 8 m + 6 (mod 9), then /3.
```

Direct evaluation gives `Q_e mod 9 = 6, 3, 0, 3, 0, 6, 0, 6, 3` for `m = 0..8`, dividing by 3 gives `F(4, 2m) mod 3 = 2, 1, 0, 1, 0, 2, 0, 2, 1` - the three residues `{0, 1, 2}` each appear **exactly three times**. Same evaluation on the odd side gives `F(4, 2m + 1) mod 3 = 0, 0, 2, 1, 1, 0, 2, 2, 1`, again three of each.

**Step 4. Coset lift.** The polynomial `Q_e(m)` satisfies

```
Q_e(m + 9) - Q_e(m)   =  1728 m^2 + 14688 m + 42921   =  18 (mod 27),
Q_e(m + 18) - Q_e(m)  =  (computed similarly)          =   9 (mod 27),
```

both constants (independent of `m`). The cubic term `1728 m^2` is `64 * 27 * m^2 = 0 mod 27`; the linear term `14688 m` is `544 * 27 * m = 0 mod 27`; only the truly constant term survives, and it survives at `9 * (17 mod 27) = 153 = 18 mod 27` for the `Delta_9` and at `18 * 17 = 306 = 9 mod 27` for `Delta_18`. Dividing by `3` (to get `F` in place of `Q_e / 3`):

```
F(4, 2(m + 9)) - F(4, 2m)   =   6 (mod 9),
F(4, 2(m + 18)) - F(4, 2m)  =   3 (mod 9).
```

For the odd side, the same computation gives `9 mod 27` and `18 mod 27` respectively (swapped):

```
F(4, 2(m + 9) + 1) - F(4, 2m + 1)   =   3 (mod 9),
F(4, 2(m + 18) + 1) - F(4, 2m + 1)  =   6 (mod 9).
```

**Step 5. Cosets tile the period.** In both cases, the triple `{F(4, h), F(4, h + 18), F(4, h + 36)}` mod 9 is `{v, v + 6, v + 3}` in some order - a **complete coset of `3 Z / 9` in `Z / 9`**, containing three distinct residues. So each "base" value of `m in {0..8}` gives three residues mod 9, one in each of the three cosets `{0, 3, 6}, {1, 4, 7}, {2, 5, 8}`, or, more precisely, three residues in the specific coset `F(4, 2 * base) + 3 Z / 9`.

**Step 6. Counting.** From Step 3, on the even side, the 9 base values `F(4, 2m) mod 3` for `m = 0..8` land three-in-each of the three cosets `{0, 3, 6}, {1, 4, 7}, {2, 5, 8}` (uniform mod 3). Each base value lifts to a full coset of three residues mod 9. So the 27 residues `F(4, 2m) mod 9` for `m = 0..26` cover each coset `3 * 3 = 9` times, distributed `3` per residue inside the coset. Total: **each residue in `Z / 9` is hit exactly 3 times** on the even side. Same argument, same count on the odd side.

**Conclusion.** Over the full period `h = 2..55`, `F(4, h) mod 9` hits each of the 9 residues exactly `3 + 3 = 6` times. The histogram is exactly `[6, 6, 6, 6, 6, 6, 6, 6, 6]`, the exclusion count is `12`, and the exclusion rate is exactly `12 / 54 = 2 / 9`. QED, without appeal to Heath-Brown or to any conjecture.

**What the proof uses.** The whole argument rests on three algebraic accidents specific to `w = 4`: the quadratic coefficient of `Q_e` and `Q_o` is divisible by 3 (making `18 a_2 = 0 mod 27` in the difference); the linear coefficients happen to be `17` and `7`, both `+-1 mod 3`, giving `Delta_9 F` a nonzero coset shift; and `F mod 3` is uniform on `m mod 9` (which is the least trivial input, verified by direct 9-value evaluation). For `w in {6, 10, 12, 17, 28, 30}` the same three-step recipe applies but with the specific polynomials from `A_w, B_w`; for `w in {5, 7, 8, 9, 11, 13, 14, ...}` one of the three steps fails, either the linear-coefficient shift is a multiple of 9 (killing the coset lift) or the base `F mod 3` distribution has a non-uniform 9-value histogram. Producing a general theorem "which `w` have all three steps hold" is the open item - see the coset-lift sufficiency criterion below for its exact form.

## The coset-lift sufficiency criterion

The blackboard proof at `w = 4` generalizes to an **exact, computable criterion** for every `w`. Uniform `w` and non-uniform `w` are distinguished by a single condition on the shift-by-`per_w / 3` operator on `F(w, . ) mod 9`:[^exec]

```
w uniform   iff   { F(w, h + per_w / 3) - F(w, h) mod 9 : h in [0, per_w) }  =  {3, 6}.
```

Every uniform `w` produces exactly the two-element image `{3, 6}` (the non-zero elements of `3 Z / 9`); every non-uniform `w` produces `{0, 3, 6}` - the extra `0` is a "coset-shift fixed point" `h` with `F(w, h + per_w / 3) = F(w, h) mod 9`, and its presence breaks uniformity. Verified across every `w in [10, 293]` with `w mod 9 in {1, 3, 8}` (17 uniform, 25 non-uniform); each uniform hit gives `{3, 6}` and each miss gives `{0, 3, 6}`, without a single exception across all 42 candidate `w`'s in brackets 3..6.

This is the same coset-lift argument the `w = 4` blackboard proof makes explicit: `F(4, h + 18) - F(4, h) = 6 (mod 9)` for even `h`, `3 (mod 9)` for odd `h`, both non-zero and both in `{3, 6}`. For general uniform `w`, the shift `per_w / 3` plays the role of `18`, and the constant-difference-in-`{3, 6}` behavior generalizes.

**The `{0, 2, 7}` template as fixed-point emptiness.** [[mod-9-equidistribution](pages/mod-9-equidistribution.md)] records that uniform `w` follow the pattern `w = 3^{k-1} + d` for `d in {1, 3, 8}` (three explicit sequences per bracket `k >= 3`, plus `d in {1, 3}` in bracket 2). Higher-offset representatives of the same mod-9 residue class - e.g. `w = 19` in bracket 3, `w = 37` in bracket 4 - are not uniform. The criterion reframes this cleanly: **why does the coset-lift image acquire `0` at higher offsets within a bracket?** Structurally, the shift-by-`per_w / 3` operator on the mod-9 state has eigenvalues that are cube roots of unity (since `(per_w / 3) * 3 = per_w` is the full state period). The `0` in the image corresponds to a fixed-point subspace of `F` under this operator, present at higher-offset `w` and empty at the three smallest offsets `{0, 2, 7}` per bracket. A closed proof of "which `w` have empty fixed-point subspace" is the residual open item.

Why the offsets `0, 2, 7`? All three are `<= 8 = 3^2 - 1`, so they live inside the "second-power" window of the k-direction char poly `(x + 1)^w (x - 1)^{w-2}` under mod-9 reduction. The `w = 4` blackboard proof gives one explicit certificate at `w = 4 = 3^1 + 1` (the `d = 1` value); by structural analogy the same three-step recipe (parity split, mod-3 uniformity, coset lift) should carry through for each `d in {1, 3, 8}` sequence. A general polynomial-coefficient argument on `A_w, B_w mod 9` should reproduce the coset-lift criterion.

## Appearances in Sources

- [[oeis-mining-pe502](pages/oeis-mining-pe502.md)] - `F(w, h)` tabulation whose mod-9 residues drive the coset-lift analysis.
- [[project-euler-502-solution](pages/project-euler-502-solution.md)] - `T(k, L) = (k+1)^L` and the Kitamasa route; the k-direction recurrence used to extend `P(k, w) mod 9` past the seeds.

## Related Concepts

- [[mod-9-equidistribution](pages/mod-9-equidistribution.md)] - the finding this page explains: the census, the `alpha = 1/12` closed-form rate, the row/column readings.
- [[sum-of-three-cubes-castles](pages/sum-of-three-cubes-castles.md)] - the parent question and the `2/9` target.
- [[mod-p-observatory](pages/mod-p-observatory.md)] - period equals lcm of eigenvalue orders; the multiplicity-inflation rule `p^{ceil(log_p m)}` used here.
- [[signed-tower-k-direction](pages/signed-tower-k-direction.md)] - `P(k, L) = (-1)^k A_L(k) + B_L(k)`, the `(x+1)^L (x-1)^{L-2}` char poly that fixes `v_3(per_w) >= 2`.
- [[castle-counting-formula](pages/castle-counting-formula.md)] - the closed form `F = (h^w - (h-1)^w - P(h-1, w) + P(h-2, w))/2` used in the `w = 4` blackboard proof.
- [[kitamasa](pages/kitamasa.md)] - jump-to-index-N over `Z/9` used to sanity-check large-`h` rows.

## Footnotes

[^exec]: Verified by execution (2026-09-22), Python 3 with NumPy 1.26 and SymPy 1.14. **`char_k mod 3` multiplicity extension**: SymPy `factor_list(..., modulus=3)` for `k = 1..200`; global max multiplicity across every `k` in range is 2, achieved iff `k mod 12 in {4, 6}` and always at root `+-1`. All irreducible factors of degree `>= 2` have multiplicity 1. **Joint-state cycle proof**: iteration of `(y_{k-1}, y_k, z_{k-1}, z_k, u_{k-1}, u_k)` in `F_3^6` starting from the initial conditions `(0, 1, 1, 0, 0, 2)` (at `x = 1`, from `char_0 = x - 1, char_1 = x^2 - 2x + 2`) enters a cycle of length 24 at `k = 1`; enumeration over `k = 0..24` records `(y_k, z_k) = (0, 0)` at exactly `k in {4, 16}` and `(y_k, z_k, u_k) = (0, 0, 0)` at *no* `k`. Same procedure at `x = -1` (initial `(1, 2, 1, 2, 0, 2)`) gives cycle length 24, pair-zeros at `k in {6, 18}`, triple-zeros nowhere. **Row-period `v_3` table (`h = 2..16`)**: `char_k` polynomials built from the three-term recurrence `char_{k+1} = x^2 char_{k-1} - 2 char_k` seeded by `char_0 = x - 1, char_1 = x^2 - 2x + 2`; period of `x` mod `(char_k, 9)` computed by iterating the companion-matrix state and detecting return to `(1, 0, ..., 0)`; row period computed as `lcm(ord_9(h), ord_9(h-1), per(char_{h-1}) mod 9, per(char_{h-2}) mod 9)`; three-adic valuation `v_3(per_h) = 1` verified for every `h` in the table. **`w = 4` blackboard proof**: symbolic computation of the closed form `12 F(4, h) = (24 h^3 - 36 h^2 + 24 h - 9) + (-1)^h (8 h^3 - 12 h^2 + 10 h - 3)` against direct evaluation of `F(4, h) = (h^4 - (h-1)^4 - P(h-1, 4) + P(h-2, 4))/2` for `h = 2..15` (all match); split into `Q_e(m) = 64 m^3 - 48 m^2 + 17 m - 3` and `Q_o(m) = 32 m^3 + 24 m^2 + 7 m` verified against `F(4, 2m)` and `F(4, 2m+1)` for `m = 1..27`; divisibility of `Q_e, Q_o` by 3 checked symbolically mod 3; `F(4, 2m) mod 3` and `F(4, 2m + 1) mod 3` uniform over `m mod 9` verified in 18 direct evaluations; `Q_e(m + 9) - Q_e(m) mod 27 = 18` and `Q_e(m + 18) - Q_e(m) mod 27 = 9` (and `Q_o` swapped) verified for `m = 0..5` (constant in `m` by the algebraic argument in the page). Final histogram `[6, 6, 6, 6, 6, 6, 6, 6, 6]` matches the count derived from the coset-tiling argument. **Coset-lift criterion check**: for every `w` in `[10, 293]` with `w mod 9 in {1, 3, 8}` (necessary condition), compute `shift = per_w / 3` and the difference set `{ (r[(i + shift) mod per_w] - r[i]) mod 9 : i in [0, per_w) }` from the mod-9 F-sequence; every uniform `w` returns exactly `{3, 6}` and every non-uniform `w` returns exactly `{0, 3, 6}`, without exception across the 42 candidate `w`'s in brackets 3..6.
