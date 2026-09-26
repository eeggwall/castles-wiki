---
title: Eisenstein at 2 - char_k is irreducible for k = 2^m - 1
category: Analyses
summary: Rescale x = 2y and divide out 2^k - Q_k(y) = char_k(2y)/2^k is an integer polynomial with the same shape of recurrence, Q_{k+1} = y² Q_{k-1} - Q_k. Its reversal is Eisenstein at 2 exactly when Q_k ≡ 1 (mod 2), and mod 2 the recurrence is a Fibonacci recurrence over F_2[y²] whose k-th term is α^(k+1) + β^(k+1) - equal to 1 iff k+1 is a power of 2. So char_k is irreducible over Q, with 2 totally ramified, for k = 1, 3, 7, 15, 31, …, by a proof, not a computation. The same condition is exactly "the 2-adic Newton polygon of char_k is one segment", so no other k is reached this way; irreducibility for the remaining odd k is still only SymPy-verified.
tags: [analysis, castle, characteristic-polynomial, irreducible-polynomial, eisenstein, newton-polygon, two-adic, fibonacci-polynomial, signed-tower-count, proof, sympy, verification]
sources: [calugareanu-hamburg-exercises-basic-ring-theory, oeis-mining-pe502]
created: 2026-09-26
updated: 2026-09-26
---

# Eisenstein at 2 - `char_k` is irreducible for `k = 2^m − 1`

## The gap this closes

[[generating-function-gallery](pages/generating-function-gallery.md)] and [[castle-cryptography-number-theory](pages/castle-cryptography-number-theory.md)] record that `char_k` - the degree-`(k+1)` characteristic polynomial of the signed tower count `P(k, ·)` ([[signed-tower-count](pages/signed-tower-count.md)]) - is irreducible over `Q` for every odd `k` tested. [[tower-parity-sectors](pages/tower-parity-sectors.md)] explains the *even* `k` factorization by a symmetry `JD` of the transfer matrix, but for odd `k` that symmetry is a complex structure, and a complex structure only says `char_k` is a norm `g·ḡ` from `Q(i)[x]`. It does not rule out a further split over `Q`. So until now odd-`k` irreducibility was a computation, not a theorem.

This page proves it for the infinite subfamily `k = 2^m − 1` using the Eisenstein criterion in its unique-factorization-domain form (Gauss's lemma plus Eisenstein, exercise 17.21 of [[calugareanu-hamburg-exercises-basic-ring-theory](pages/calugareanu-hamburg-exercises-basic-ring-theory.md)]), and shows the method reaches exactly that subfamily and no more.

**Eisenstein's criterion.** Let `f = a_0 + a_1 X + … + a_n X^n` have integer coefficients and let `p` be a prime with `p ∤ a_n`, `p | a_i` for `i < n`, and `p² ∤ a_0`. Then `f` is irreducible over `Q`; if also no prime divides every coefficient, it is irreducible over `Z` as well.[^1]

## Step 1 - rescale by 2

`char_k` obeys `char_0 = x − 1`, `char_1 = x² − 2x + 2`, `char_{k+1} = x²·char_{k−1} − 2·char_k`.[^2] Its constant term is `±2^k`, and in general its coefficients carry a lot of 2s. Take them out: set

```
Q_k(y)  =  char_k(2y) / 2^k .
```

Substituting `x = 2y` into the recurrence and dividing by `2^{k+1}` gives

```
Q_0 = 2y − 1,   Q_1 = 2y² − 2y + 1,   Q_{k+1} = y²·Q_{k−1} − Q_k .
```

This recurrence has integer coefficients, so every `Q_k` is an integer polynomial. Its leading coefficient is `2^{k+1}/2^k = 2`, and its constant term `char_k(0)/2^k = ±1` is odd.[^3] (This is the same rescaling `λ = 2μ` that [[tower-parity-sectors](pages/tower-parity-sectors.md)] uses to make the even-`k` factors explicit.)

## Step 2 - the Eisenstein condition is "`Q_k ≡ 1 mod 2`"

Reverse the coefficients: `R_k(y) = y^{k+1} Q_k(1/y)`. `R_k` has leading coefficient `Q_k(0) = ±1` (odd) and constant term `2` (even, not divisible by 4). So `R_k` is Eisenstein at 2 **exactly when every middle coefficient of `Q_k` is even**, that is, when

```
Q_k(y)  ≡  1   (mod 2).
```

When it holds, `R_k` is irreducible over `Q`. Reversal and rescaling preserve irreducibility (for polynomials with nonzero constant term), so `char_k` is irreducible too.

## Step 3 - mod 2 the recurrence is Fibonacci

Reduce mod 2 and write `q_k = Q_k mod 2`. Since `2y ≡ 0`,

```
q_0 = 1,   q_1 = 1,   q_{k+1} = q_k + t·q_{k−1}      over F_2[t],  t = y².
```

That is a Fibonacci recurrence. Let `α, β` be the roots of `z² + z + t` over an extension of `F_2(t)`, so `α + β = 1` and `αβ = t`. The Binet form `q_k = (α^{k+1} − β^{k+1})/(α − β)` has denominator `α − β = α + β = 1` in characteristic 2, so

```
q_k  =  α^{k+1} + β^{k+1}  =  s_{k+1},   the (k+1)-st power sum.
```

**If `k + 1 = 2^m`:** Frobenius gives `s_{2^m} = (α + β)^{2^m} = 1`. So `q_k = 1`.

**Otherwise** write `k + 1 = 2^m·r` with `r ≥ 3` odd. Then `s_{k+1} = (s_r)^{2^m}`, so it suffices that `s_r ≠ 1`. Newton's recurrence `s_n = s_{n−1} + t·s_{n−2}` with `s_0 = 2 = 0`, `s_1 = 1` gives constant term `1` for every `s_n` with `n ≥ 1`, and the coefficient of `t` obeys `c_n = c_{n−1} + 1` for `n ≥ 3` from `c_2 = 0`. So `c_r = 1` for every odd `r ≥ 3`, `s_r` has a nonzero `t`-term, and `q_k ≠ 1`.

**Theorem.** `Q_k ≡ 1 (mod 2)` if and only if `k + 1` is a power of 2. Consequently `char_k` is irreducible over `Q` for `k = 1, 3, 7, 15, 31, 63, …`, and 2 is totally ramified in `Q(ρ)` for any root `ρ` of these `char_k`.[^4]

## Step 4 - this is exactly the reach of the method

The 2-adic valuations of `char_k`'s coefficients `a_i` run from `v(a_0) = k` down to `v(a_{k+1}) = 0`. The **2-adic Newton polygon** is a single segment of slope `k/(k+1)` exactly when `v(a_i) ≥ k − ik/(k+1)`, i.e. (valuations are integers) `v(a_i) ≥ k − i + 1` for `1 ≤ i ≤ k`. That is the same inequality as Step 2's "every middle coefficient of `Q_k` is even." Because `gcd(k, k+1) = 1`, a single segment of that slope forces irreducibility over `Q_2`. This is Dumas's generalization of Eisenstein, and here it adds nothing new: it succeeds for exactly the same `k`. For every other odd `k` the polygon breaks into several segments, and neither Eisenstein nor Dumas at 2 decides irreducibility.[^4]

| `k` | `Q_k mod 2` | reversed `Q_k` Eisenstein at 2? | irreducible over `Q` |
|---|---|---|---|
| 1 | `1` | yes: `y² − 2y + 2` | proved here |
| 3 | `1` | yes: `y⁴ − 2y³ + 4y² − 4y + 2` | proved here |
| 5 | `1 + y⁴` | no | SymPy only |
| 7 | `1` | yes | proved here |
| 9, 11, 13 | `≠ 1` | no | SymPy only |
| 15 | `1` | yes | proved here |

## What this settles and what it opens

**Settled.**
- `char_{2^m − 1}` is irreducible over `Q` for every `m ≥ 1`, with 2 totally ramified. These are the `k` where `P(k, ·)` has order `2^m`.
- Eisenstein and Dumas at the prime 2 reach exactly this family, and nothing else, because the obstruction mod 2 is a Fibonacci polynomial over `F_2`.

**Open.**
- Odd `k` not of the form `2^m − 1` (`k = 5, 9, 11, 13, 17, …`): irreducible by SymPy through `k = 31`, with no proof. A proof needs a different prime, a different substitution, or a Galois-theoretic argument (for instance, showing the `Q(i)`-factors `g, ḡ` from the `JD` complex structure are themselves irreducible and not defined over `Q`).
- Which odd primes divide `disc(char_k)` ([[larger-prime-periodicity](pages/larger-prime-periodicity.md)] lists `k ≤ 10`), and whether any of them is totally ramified for other `k`, is a natural next place to look for further Eisenstein primes.

## Snippet

```python
import sympy as sp
y = sp.symbols('y')
Q = [sp.Poly(2*y - 1, y), sp.Poly(2*y**2 - 2*y + 1, y)]
for k in range(1, 80):
    Q.append(sp.Poly(y**2, y)*Q[k-1] - Q[k])          # Q_{k+1} = y^2 Q_{k-1} - Q_k
def eis_rev(P):                                        # reversed P Eisenstein at 2?
    co = P.all_coeffs()[::-1]
    return co[0] % 2 == 1 and all(a % 2 == 0 for a in co[1:]) and co[-1] % 4 != 0
print([k for k in range(81) if eis_rev(Q[k])])
# mod 2, as bitmasks over F_2[t]: q_{k+1} = q_k + t q_{k-1}
q = [1, 1]
for k in range(1, 5000): q.append(q[k] ^ (q[k-1] << 1))
print([k for k in range(5001) if q[k] == 1])
```

```
[0, 1, 3, 7, 15, 31, 63]
[0, 1, 3, 7, 15, 31, 63, 127, 255, 511, 1023, 2047, 4095]
```

## Appearances in Sources

- [[calugareanu-hamburg-exercises-basic-ring-theory](pages/calugareanu-hamburg-exercises-basic-ring-theory.md)] - exercise 17.21 (Eisenstein over a UFD, with Gauss's lemma), the tool applied here.
- [[oeis-mining-pe502](pages/oeis-mining-pe502.md)] - the `P(k, ·)` family and its `char_k`.

## Related Concepts

- [[tower-parity-sectors](pages/tower-parity-sectors.md)] - the `JD` symmetry: it explains the even-`k` split and makes odd-`k` `char_k` a norm from `Q(i)[x]`. That is the step this page's proof replaces for `k = 2^m − 1`.
- [[generating-function-gallery](pages/generating-function-gallery.md)] - the `char_k` table and the even/odd factorization pattern.
- [[castle-cryptography-number-theory](pages/castle-cryptography-number-theory.md)] - "irreducible = prime for polynomials"; the odd-`k` rows of its table are proved here for `k = 1, 3`.
- [[finite-fields](pages/finite-fields.md)] - the Frobenius identity `(α + β)^{2^m} = α^{2^m} + β^{2^m}` in characteristic 2 is the whole of Step 3.
- [[larger-prime-periodicity](pages/larger-prime-periodicity.md)] - discriminants of `char_k`; total ramification at 2 is the extreme case of 2 dividing the discriminant.
- [[pell-numbers](pages/pell-numbers.md)] - another Lucas/Fibonacci-type sequence on the wiki; here a Fibonacci recurrence appears one level down, over `F_2[t]`.
- [[castle-ring-spectrum](pages/castle-ring-spectrum.md)] - the fiber over 2: for `k = 1`, `Z[x]/(char_1) ≅ Z[i]` and the prime `(2, x)` is `(1 + i)` with `2 = −i(1 + i)²`, the smallest case of the total ramification proved here.

## Footnotes

[^1]: [[calugareanu-hamburg-exercises-basic-ring-theory](pages/calugareanu-hamburg-exercises-basic-ring-theory.md)] Ex. 17.21 p.76; solution pp.193-194 [synthesis] - Eisenstein's criterion over a UFD `R` gives irreducibility in `K[X]` for `K` the fraction field, and in `R[X]` when the polynomial is primitive; the solution reduces the `K[X]` case to `R[X]` by clearing denominators (Gauss's lemma).
[^2]: [[oeis-mining-pe502](pages/oeis-mining-pe502.md)] `mine-notes.md` §"Vein 1" L31-37 [synthesis] - the `char_k` family of the signed tower counts, `P(k, ·)` C-finite of order `k+1`, `char_1..char_5` listed with constant term `(−1)^{k−1} 2^k`. The three-term construction `char_{k+1} = x²·char_{k−1} − 2·char_k` is the one used on [[larger-prime-periodicity](pages/larger-prime-periodicity.md)] and checked there against [[generating-function-gallery](pages/generating-function-gallery.md)].
[^3]: Verified by execution (Python 3.10, SymPy, 2026-09-26): `Poly(char_k(2y)) == 2^k · Q_k` for every `k ≤ 80`, with `Q_k` built from `Q_0 = 2y − 1`, `Q_1 = 2y² − 2y + 1`, `Q_{k+1} = y² Q_{k−1} − Q_k`; every `Q_k` has integer coefficients and leading coefficient 2.
[^4]: Verified by execution (Python 3.10, SymPy, 2026-09-26): (i) reversed `Q_k` is Eisenstein at 2 exactly for `k ∈ {0, 1, 3, 7, 15, 31, 63}` among `k ≤ 80`, the same set as `Q_k ≡ 1 mod 2`; (ii) the 2-adic Newton polygon of `char_k` is a single segment exactly for `k ∈ {1, 3, 7, 15, 31, 63}` among odd `k ≤ 69`; (iii) the `F_2[t]` bitmask recurrence has `q_k = 1` exactly for `k = 2^m − 1` among `k ≤ 5000`; (iv) `sp.factor_list(char_k)` has a single factor of multiplicity 1 for every odd `k ≤ 31`. The proof in Step 3 is by hand; (i)-(iii) are consistency checks on it.
