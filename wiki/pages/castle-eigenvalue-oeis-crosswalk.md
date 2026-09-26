---
title: Castle eigenvalues meet OEIS - the convergent crosswalk
category: Analyses
summary: Every castle eigenvalue's "convergents" run against OEIS. The metallic rungs give one sequence each (numerator = denominator shifted; A001333 is the numerator sequence of √2). The k-direction has no irrational eigenvalues at all - its characteristic polynomial is (x+1)^L (x−1)^(L−2), so P(k,L) is a quasi-polynomial in k with |P(k,4)| = A352116. The real higher-degree eigenvalues are the L-direction char_k roots; ρ_6 = 2ψ² (plastic number), P(6,L) = 2^L·A005251(L+3) + remainder, and its Jacobi–Perron expansion is periodic. The CF-period ↔ mod-p-order link is made quantitative (norm −1 ⟺ δ^(p+1) = −1 at inert primes; k-direction period 2·p^⌈log_p L⌉).
tags: [analysis, castle, continued-fraction, convergents, oeis, eigenvalue, quasi-polynomial, plastic-number, jacobi-perron, pisano, mod-p, sympy, verification, pedagogy]
sources: [oeis-mining-pe502, project-euler-502-solution, project-euler-502-castle-factoring]
created: 2026-09-16
updated: 2026-09-26
---

# Castle eigenvalues meet OEIS: the convergent crosswalk

## The question, and what came out

[[eigenvalue-continued-fractions](pages/eigenvalue-continued-fractions.md)] ends on a promise: the eigenvalue's *continued-fraction period* over `R` and its *multiplicative order* mod `p` are two readings of one structure. This page cashes that promise in integers. A continued fraction's **convergents** `p_n/q_n` are its best rational approximations, and the numerators and denominators are integer sequences in their own right - Fibonacci for `φ`, Pell for `1+√2`. So: for every eigenvalue the castle produces, what are the convergent sequences, which OEIS entries do they hit, and where does the mod-`p` order show up in them?

The through-line is one sentence, and each part follows it one step:

> A castle eigenvalue is a number, and a number has two kinds of repeating behavior — a continued-fraction period (over the reals) and a multiplicative order (mod `p`). These are two readings of one structure; the page walks each side to its integers.

**Four parts, each one job:**

1. **Part 1 — the metallic crosswalk.** The convergent sequences of the metallic means, matched offset-exact to OEIS (Pell A000129 for `1+√2`, and so on).
2. **Part 2 — the mod-`p` bridge.** One integer, the norm `N(δ) = ±1`, decides both the continued-fraction period and the mod-`p` order — the "two readings of one structure," made quantitative.
3. **Part 3 — the k-direction.** Run the castle in the other variable and every eigenvalue is `±1`, so there is no irrational continued fraction at all — just a quasi-polynomial, with `|P(k,4)| = A352116`. Full write-up on [[signed-tower-k-direction](pages/signed-tower-k-direction.md)].
4. **Part 4 — the L-direction.** The genuinely irrational eigenvalues (`ρ_6 = 2ψ²`, the plastic number) and their multidimensional Jacobi–Perron continued fractions.

Part 1 feeds Part 2; Parts 3 and 4 are the two independent directions (`k` and `L`) the castle can be run in. Read any part on its own.

**What comes out (headline results):**

1. **The metallic rungs are a one-sequence story each.** For `δ_a = [a; a, a, …]` the numerators and denominators are the *same* recurrence sequence one step apart, and the companion (Lucas-type) sequence appears as a trace. For `1+√2` both are A000129; A001333 is the numerator sequence of `√2 = (1+√2) − 1`.
2. **The k-direction has no irrational eigenvalues.** The order-`(2L − 2)` characteristic polynomial of `P(·, L)` is `(x + 1)^L (x − 1)^{L − 2}` for every `L ≤ 12` tested. `P(k, L)` is a period-2 quasi-polynomial in `k`, and its first non-trivial row is in OEIS: `|P(k, 4)|` = A352116, the partial sums of the odd triangular numbers.
3. **The real higher-degree eigenvalues are in the L-direction**, the roots of `char_k` on [[generating-function-gallery](pages/generating-function-gallery.md)]. The `k = 6` dominant eigenvalue is `2ψ²` for `ψ` the plastic number; the plastic component of `P(6,L)` is exactly `2^L · A005251(L+3)`; and the multidimensional (Jacobi–Perron) expansion of `ρ_6` is periodic with a period matrix whose characteristic polynomial has Perrin-number coefficients. `ρ_4`'s expansion shows no period in 400 exact steps.
4. **The CF ↔ mod-p link, quantitatively.** For a norm-`−1` quadratic, the `−1` that makes the fraction purely periodic (Galois) is the `−1` in `δ^{p+1} = N(δ) = −1` at every inert prime, so the Pisano-type period divides `2(p+1)` and never `p+1` - verified for all five rungs and every prime below 100, with the norm-`+1` control `φ²` behaving the opposite way. For the `±1` k-direction eigenvalues the period of `P(·,L) mod p` in `k` is `2·p^{⌈log_p L⌉}`, which explains the lone `18` in the [[mod-p-observatory](pages/mod-p-observatory.md)]'s height table.

Everything below was produced by the snippets shown, executed during writing; every printed value is pinned. The snippets are the pedagogy - each one teaches the piece of theory it computes.

## Part 1 - Convergents, and the metallic crosswalk

### What a convergent is (one snippet)

Truncate `[a₀; a₁, a₂, …]` after `n` terms and clear denominators: the result `p_n/q_n` obeys the same three-term recurrence in both numerator and denominator,

```
p_n = a_n p_{n−1} + p_{n−2},     q_n = a_n q_{n−1} + q_{n−2},
```

with the seeds `(p_{−1}, p_{−2}) = (1, 0)` and `(q_{−1}, q_{−2}) = (0, 1)`. That is the whole algorithm:

```python
def convergents(digits):
    """p_n/q_n for the continued fraction [a0; a1, a2, ...] via p_n = a_n p_{n-1} + p_{n-2}."""
    p, p_prev, q, q_prev = digits[0], 1, 1, 0
    out = [(p, q)]
    for a in digits[1:]:
        p, p_prev = a*p + p_prev, p
        q, q_prev = a*q + q_prev, q
        out.append((p, q))
    return out
```

```
>>> convergents([1]*8)          # phi = [1; 1, 1, ...]
[(1, 1), (2, 1), (3, 2), (5, 3), (8, 5), (13, 8), (21, 13), (34, 21)]
>>> convergents([2]*7)          # 1 + sqrt(2) = [2; 2, 2, ...]
[(2, 1), (5, 2), (12, 5), (29, 12), (70, 29), (169, 70), (408, 169)]
```

**What it teaches.** When every digit is the same `a`, the convergent recurrence *is* the metallic recurrence `x_n = a·x_{n−1} + x_{n−2}`, so numerator and denominator are the same sequence: `q_n = x_{n+1}`, `p_n = x_{n+2}`. That is why Fibonacci convergents to `φ` are `F_{n+2}/F_{n+1}` and Pell convergents to `1+√2` are `P_{n+2}/P_{n+1}` - **one** OEIS entry per rung, not two. In matrix form `[[p_n, p_{n−1}], [q_n, q_{n−1}]] = M^{n+1}` with `M = [[a, 1], [1, 0]]`, `det M = −1`; the trace of `M^{n+1}` is `p_n + q_{n−1} = y_{n+1}`, the companion sequence. Verified:

```
>>> [p - q for p, q in convergents([2]*8)]            # convergent numerators of sqrt(2) = [1; 2, 2, ...]
[1, 3, 7, 17, 41, 99, 239, 577]
>>> [p + q_prev for (p, _), (_, q_prev) in zip(convergents([2]*8)[1:], convergents([2]*8))]
[6, 14, 34, 82, 198, 478, 1154]                        # companion Pell A002203 from index 2
```

Subtracting the integer part changes only `a₀`, so `√2 = (1+√2) − 1` has the same denominators and numerators `p_n − q_n` - which is where **A001333** lives.

### The crosswalk table

Every OEIS number below was checked offset-exact against the stored OEIS data on 2026-09-16 (the lookup helper is in the snippet index at the end).[^5]

| `a` | `δ_a = [a; a, …]` | `q_n = x_{n+1}` (and `p_n = x_{n+2}`) | trace `y_n = δ^n + δ̂^n` | `p_n − q_n` (convergents of `δ_a − 1`) | `√(a²+4)` | its convergents (num / den) |
|---|---|---|---|---|---|---|
| 1 | `φ` | **A000045** Fibonacci | **A000032** Lucas | A000045 again (`φ − 1 = 1/φ`) | `[2; 4̄]` | A001077 / A001076 |
| 2 | `1+√2` | **A000129** Pell | **A002203** companion Pell (`= 2·A001333`) | **A001333** (numerators of `√2`) | `[2; 1, 4]` (period 2) | A041010 / A041011 |
| 3 | `(3+√13)/2` | **A006190** | **A006497** | A052924 | `[3; 1, 1, 1, 1, 6]` (period 5) | A041018 / A041019 |
| 4 | `2+√5 = φ³` | **A001076** = denominators of `√5` | **A014448** `L_{3n}` | A033887 `F_{3n+1}` | `[4; 2, 8]` (period 2) | A041030 / A041031 |
| 5 | `(5+√29)/2` | **A052918** (offset: `A052918(n) = x_{n+1}`) | **A087130** | A100237 | `[5; 2, 1, 1, 2, 10]` (period 5) | A041046 / A041047 |

Three lessons sit in this table.

- **Same field, different number, different period.** `δ_3 = (3+√13)/2` has period 1, but `√13` in the same field `Q(√13)` has period 5. The continued-fraction period is a property of the *number*, and the unit `δ_a` is the number in its field with the simplest expansion. (`√(a²+4) = 2δ_a − a`; multiplying by 2 destroys the period-1 structure except when it does not: `√5 = [2; 4̄]` because `√5 = δ_4 − 2 = φ³ − 2`, the copper coincidence of [[metallic-means](pages/metallic-means.md)] - which is why the copper sequence A001076 is literally "denominators of continued fraction convergents to `√5`".)
- **`√(a²+4)` CFs were generated with SymPy** (`sp.continued_fraction_periodic(0, 1, a*a + 4)` returns `[a₀, [period]]`): `[2, [4]]`, `[2, [1, 4]]`, `[3, [1, 1, 1, 1, 6]]`, `[4, [2, 8]]`, `[5, [2, 1, 1, 2, 10]]`.
- **Trace versus half-trace.** The trace sequence for `a = 2` (`2, 2, 6, 14, 34, …`) is A002203; A001333 (`1, 1, 3, 7, 17, …`) is its half, and is the sequence that shows up as convergent numerators of `√2`.

## Part 2 - The bridge to mod p: the norm is visible on both sides

Reduce the convergent matrix `M = [[a, 1], [1, 0]]` mod `p`. The sequence `x_n mod p` is periodic with period equal to the order of `M` in `GL₂(F_p)`, which is the lcm of the orders of its two eigenvalues `δ` and `δ̂ = a − δ` in the field where they live: `F_p` if `a² + 4` is a square mod `p`, `F_{p²}` if not. When the discriminant is a square mod `p` the polynomial `x² − ax − 1` factors over `F_p` and the prime is **split** in `Q(√(a² + 4))` (`δ` and `δ̂` land in `F_p` itself); when it is a non-square the polynomial stays irreducible and the prime is **inert** (`δ` and `δ̂` land in the quadratic extension `F_{p²}`). Here is the whole computation, in a quotient ring you build by hand:

```python
def order_mod(a, c, p):
    """Multiplicative order of the root t of t^2 - a t + c in F_p[t]/(t^2 - a t + c)."""
    def mul(u, v):
        (u0, u1), (v0, v1) = u, v            # u0 + u1 t, with t^2 = a t - c
        return ((u0*v0 - c*u1*v1) % p, (u0*v1 + u1*v0 + a*u1*v1) % p)
    cur, e = (0, 1), 1
    while cur != (1, 0):
        cur, e = mul(cur, (0, 1)), e + 1
    return e

def period_mod(a, p):
    """Period of x_n = a x_{n-1} + x_{n-2} (x_0, x_1 = 0, 1) modulo p."""
    s, n = (0, 1), 0
    while True:
        s, n = (s[1], (a*s[1] + s[0]) % p), n + 1
        if s == (0, 1):
            return n
```

```
>>> # (p, ord(delta_a), period of x_n mod p, Legendre symbol (a^2+4 | p))
>>> [(p, order_mod(1, -1, p), period_mod(1, p), int(sp.legendre_symbol(5, p))) for p in (3, 7, 11, 13, 19)]
[(3, 8, 8, -1), (7, 16, 16, -1), (11, 10, 10, 1), (13, 28, 28, -1), (19, 18, 18, 1)]
>>> [(p, order_mod(2, -1, p), period_mod(2, p), int(sp.legendre_symbol(8, p))) for p in (3, 7, 11, 13, 19)]
[(3, 8, 8, -1), (7, 6, 6, 1), (11, 24, 24, -1), (13, 28, 28, -1), (19, 40, 40, -1)]
>>> [(p, order_mod(3, 1, p), int(sp.legendre_symbol(5, p))) for p in (3, 7, 11, 13, 19)]   # control: phi^2, norm +1
[(3, 4, -1), (7, 8, -1), (11, 5, 1), (13, 14, -1), (19, 9, 1)]
```

**What it teaches.** Read the two lists for `a = 1` (Fibonacci) and the control together:

- **Split primes** (Legendre `+1`): `δ ∈ F_p`, so its order divides `p − 1`. `p = 11`: order 10; `p = 19`: order 18. This is the classical "Pisano period divides `p − 1` when `p ≡ ±1 (mod 5)`."
- **Inert primes** (Legendre `−1`): `δ ∈ F_{p²}`, and the **Frobenius** `x ↦ x^p` - the field automorphism of `F_{p²}` that fixes `F_p` pointwise and swaps the two roots of any irreducible quadratic - sends `δ` to `δ̂`, so `δ^{p+1} = δ · δ̂ = N(δ)`. For a metallic mean `N(δ) = −1`, hence **`δ^{p+1} = −1`**: the order divides `2(p + 1)` and does *not* divide `p + 1`. `p = 3`: order 8 = `2 · 4`; `p = 7`: 16 = `2 · 8`; `p = 13`: 28 = `2 · 14`. The classical "Pisano period divides `2(p + 1)` when `p ≡ ±2 (mod 5)`" - and now you can see *why the 2 is there*.
- **The control `φ² = (3+√5)/2`**, root of the palindromic `x² − 3x + 1`, has norm `+1`. At inert primes `(φ²)^{p+1} = +1`, so its order divides `p + 1` outright: `p = 3`: 4; `p = 7`: 8; `p = 13`: 14. No factor of 2.

So the single integer `N(δ) = ±1` is read twice: over `R` it decides whether the continued fraction is *purely* periodic (**Galois' reduced-surd criterion**: a quadratic surd `α > 1` has a purely periodic simple CF iff its conjugate `α̂` lies in `(−1, 0)`, which for a norm-`−1` surd `α > 1` with `α · α̂ = −1` is automatic; see [[eigenvalue-continued-fractions](pages/eigenvalue-continued-fractions.md)] Step 3), and mod `p` it decides whether `δ^{p + 1}` is `−1` or `+1` at the inert primes, i.e. whether the Pisano-type period carries an extra factor 2 beyond `p + 1`. **That is the concrete quantitative link the eigenvalue page drew in the abstract.**

The full sweep - `a = 1..5`, all primes `p < 100`, skipping the ramified `p | a²+4` - asserted, without exception: `period_mod(a, p) == lcm(ord δ, ord δ̂)`; split ⇒ `ord | p−1`; inert ⇒ `δ^{p+1} = −1`, `ord | 2(p+1)`, `ord ∤ p+1`.[^8] (Aside for the observant: `ord δ = ord δ̂` in every row of the sweep, so the period is simply `ord δ`; the two are equal because `δ̂ = −1/δ` has the same order as `−δ`, and the order of `δ` is even at every prime tested.)

## Part 3 - The k-direction: there are no irrational eigenvalues

The k-direction recurrence of `P(k, L)` (fixed `L`, varying height bound `k`) has characteristic polynomial `(x + 1)^L (x − 1)^{L − 2}` for every `L` from 4 to 12 checked, so its only eigenvalues are `±1` and `P(k, L)` is a period-2 quasi-polynomial in `k`:

```
P(k, L)  =  (−1)^k · A_L(k) + B_L(k),         deg A_L ≤ L − 1,  deg B_L ≤ L − 3.
```

The full derivation - the factorization from Berlekamp-Massey, the **Ehrhart argument** sketch (Ehrhart's theorem: the number of lattice points in a dilated rational polytope `k · P` is a quasi-polynomial in `k`; here the sign-weighted variant, summing a root of unity raised to a linear form, cuts the period down to the order of the root - here 2), the explicit `A_L, B_L` table through `L = 8`, the OEIS hits (`|P(k, 4)| = A352116` with the `C_3` crystal-ball / tetrahedral bisections `P(2m, 4) = A063496`, `|P(2m + 1, 4)| = A199833 = 4·A000447`), and the mod-`p` period formula `2 · p^{⌈log_p L⌉}` (which accounts for the lone `18` in the [[mod-p-observatory](pages/mod-p-observatory.md)] table) all live on [[signed-tower-k-direction](pages/signed-tower-k-direction.md)]. From there:

- Nothing in this direction has a continued fraction to speak of - rational numbers terminate. The interesting eigenvalues live in the L-direction (Part 4).
- The `(x + 1)^L (x − 1)^{L − 2}` factorization sharpens the OEIS-mining pass's `(x² − 1)^w` observation for the even-block count `F(w, ·)`[^4] to exact multiplicities for the signed count.
- The mod-`p` result is the finite-field twin of Part 2, in the direction where every eigenvalue is `±1`: no `p + 1` versus `2(p + 1)` distinction (that requires a norm-`−1` quadratic), just a multiplicity effect from the repeated eigenvalues.

## Part 4 - The L-direction: the real higher-degree eigenvalues

### Where they live, and the plastic surprise

The L-direction recurrences (fixed `k`, vary the base length `L`) have characteristic polynomials `char_k` of degree `k+1`, built by `char_{k+1} = λ²·char_{k−1} − 2·char_k` from `char_0 = λ−1`, `char_1 = λ²−2λ+2`, with constant term `(−1)^{k−1}2^k`.[^1][^2] Their roots are the castle's genuinely irrational eigenvalues. For even `k` the polynomial splits into two factors and the dominant eigenvalue `ρ_k` is real; for odd `k` it is irreducible with a complex dominant pair ([[generating-function-gallery](pages/generating-function-gallery.md)]; irreducibility proved for `k = 2^m − 1` on [[char-k-eisenstein-at-two](pages/char-k-eisenstein-at-two.md)]). Take the dominant factor for even `k`, and - because the product of *all* eigenvalues is `2^k` - try dividing the root by 2:

```
>>> sp.factor(c[6])
(lam**3 - 4*lam**2 + 4*lam - 8)*(lam**4 - 3*lam**3 + 8*lam**2 - 4*lam + 8)
>>> sp.factor(sp.resultant(x**3 - x - 1, mu - x**2, x))        # minimal polynomial of psi^2
mu**3 - 2*mu**2 + mu - 1
>>> sp.factor(sp.resultant(mu**3 - 2*mu**2 + mu - 1, lam - 2*mu, mu))   # minimal polynomial of 2 psi^2
lam**3 - 4*lam**2 + 4*lam - 8
```

**`ρ_6 = 2ψ²`, where `ψ = 1.3247…` is the plastic number**, the real root of `x³ = x + 1` (A060006) - the smallest **Pisot number** (a real algebraic integer `> 1` all of whose other Galois conjugates lie strictly inside the unit circle), whose Fibonacci and Lucas are the Padovan (A000931) and Perrin (A001608) sequences.[^7] Numerically `2ψ² = 3.50975533249…`, matching the gallery's `ρ_6 = 3.510`. The same rescaling test for every even `k ≤ 18`:[^8]

| `k` | `ρ_k` | minimal polynomial of `ρ_k` | degree | `ρ_k / 2` | unit? |
|---|---|---|---|---|---|
| 2 | `2` | `λ − 2` | 1 | `1` | yes |
| 4 | `2.796321903…` | `λ³ − 3λ² + 2λ − 4` | 3 | `μ³ − 3μ²/2 + μ/2 − 1/2` | **no** - not even an algebraic integer |
| 6 | `3.509755332…` | `λ³ − 4λ² + 4λ − 8` | 3 | `μ³ − 2μ² + μ − 1`, i.e. `ψ²` | yes (Pisot) |
| 8 | `4.174029055…` | `λ⁵ − 5λ⁴ + 8λ³ − 20λ² + 8λ − 16` | 5 | half-integer coefficients | no |
| 10 | `4.804417668…` | `λ⁵ − 6λ⁴ + 12λ³ − 32λ² + 16λ − 32` | 5 | `μ⁵ − 3μ⁴ + 3μ³ − 4μ² + μ − 1` | yes (not Pisot: a conjugate has modulus 1.09) |
| 12 | `5.409433398…` | degree 7 | 7 | half-integer coefficients | no |
| 14 | `5.994422837…` | degree 7 | 7 | `μ⁷ − 4μ⁶ + 6μ⁵ − 10μ⁴ + 5μ³ − 6μ² + μ − 1` | yes |
| 16 | `6.563018640…` | degree 9 | 9 | half-integer coefficients | no |
| 18 | `7.117830358…` | degree 9 | 9 | `μ⁹ − 5μ⁸ + 10μ⁷ − 20μ⁶ + 15μ⁵ − 21μ⁴ + 7μ³ − 8μ² + μ − 1` | yes |

The pattern through `k = 18`: both factors of `char_k` have constant term of absolute value `2^{k/2}`; the dominant root sits in the degree-`k/2` factor when `k ≡ 2 (mod 4)` - making **`ρ_k/2` an algebraic unit** - and in the degree-`(k/2+1)` factor when `k ≡ 0 (mod 4)`, where `ρ_k/2` is not even an algebraic integer. Units are what the metallic means are (fundamental units of their fields), so for `k ≡ 2 (mod 4)` the L-direction eigenvalue keeps the number-theoretic structure that makes continued fractions of quadratic units so clean; for `k ≡ 0 (mod 4)` that structure is gone. A proof of the pattern is open (IDEAS, "Plastic eigenvalue and the unit pattern").

**The plastic component of `P(6,L)` is an OEIS sequence.** Partial fractions on the gallery's `num_6/den_6` split `P(6,L)` into a cubic part (the `2ψ²` block) and a quartic remainder, and the cubic part is exact:[^7][^8]

```python
# Preamble: build num_k / den_k from the recurrence in [[project-euler-502-solution]],
# and a small series-coefficient helper.
x = sp.symbols('x')
num, den = sp.Integer(1), 1 - x
for _ in range(6):
    num, den = sp.expand(2*den - num), sp.expand(den*(1-2*x) + x*num)
num6, den6 = num, den

def series_coefficients_of(f, n):
    s = sp.series(f, x, 0, n).removeO()
    return [int(s.coeff(x, k)) for k in range(n)]
```

```
>>> sp.apart(num6/den6, x)
-x*(4*x**2 + 3)/(8*x**4 - 4*x**3 + 8*x**2 - 3*x + 1) - (4*x**2 + 1)/(8*x**3 - 4*x**2 + 4*x - 1)
>>> [c/2**L for L, c in enumerate(series_coefficients_of(-(4*x**2 + 1)/(8*x**3 - 4*x**2 + 4*x - 1), 12))]
[1, 2, 4, 7, 12, 21, 37, 65, 114, 200, 351, 616]
```

That is **A005251(L+3)**: `a(n) = 2a(n−1) − a(n−2) + a(n−3)`, and by the OEIS comment `a(n+3)` is "the number of `n`-bit sequences that avoid 010" - binary strings with no isolated 1. So

```
P(6, L)  =  2^L · #{binary strings of length L with no isolated 1}  +  (order-4 remainder with characteristic polynomial λ⁴ − 3λ³ + 8λ² − 4λ + 8),
```

with the remainder `−2, −3, −1, 9, 71, 289, 727, 1361, …`. The signed count of height-`≤6` towers on a length-`L` base has, as its dominant piece, the per-column binary state `2^L` (the height-2 unsigned tower count `T(1, L)` of [[castle-counting-formula](pages/castle-counting-formula.md)]) times a no-isolated-1 count in the plastic field. Nothing on the wiki predicts that; a bijection is the obvious target.

### Simple continued fractions: non-periodic, as Lagrange requires

```python
def cf_digits(poly_coeffs, x0, n=20):
    r = findroot(lambda t: sum(cc*t**(len(poly_coeffs)-1-i) for i, cc in enumerate(poly_coeffs)), mpf(x0))
    digs, t = [], r
    for _ in range(n):
        a = int(floor(t)); digs.append(a); t = 1/(t - a)
    return digs
```

```
>>> mp.dps = 200
>>> cf_digits([1, -3, 2, -4], 2.8)        # rho_4
[2, 1, 3, 1, 10, 13, 3, 2, 1, 30, 1, 12, 1, 1, 36, 1, 11, 10, 1, 21]
>>> cf_digits([1, -4, 4, -8], 3.5)        # rho_6 = 2 psi^2
[3, 1, 1, 25, 7, 1, 6, 1, 8, 1, 282, 40, 4, 2, 1, 5, 4, 5, 8, 1]
>>> cf_digits([1, -2, -1], 2.4, 8)        # 1 + sqrt(2), for contrast
[2, 2, 2, 2, 2, 2, 2, 2]
```

**What it teaches.** The digits of a cubic look random - `282` shows up in `ρ_6`'s expansion - and by Lagrange they *cannot* repeat: eventually periodic ⟺ quadratic. Their convergents are integer sequences, but ones with no linear recurrence, and unsurprisingly none of them (nor the digit strings, nor the decimal expansions of `ρ_4`, `ρ_6`) is in OEIS. The digits are believed to follow the Gauss–Kuzmin statistics of a "typical" real number, but nothing about the castle is visible in them. For a cubic the right object is the next one.

### Multi-variable convergents: Jacobi–Perron, exactly

A quadratic's continued fraction is one number and one period; a cubic needs a *vector* of numbers, and that is the **Jacobi–Perron algorithm** (JPA), the standard multidimensional continued fraction. For a degree-`d` number `ρ` start from the vector `(ρ, ρ², …, ρ^{d−1})`, take integer parts `a_i = ⌊α_i⌋`, and map

```
(α_1, …, α_{d−1})  ↦  ( (α_2 − a_2)/(α_1 − a_1), …, (α_{d−1} − a_{d−1})/(α_1 − a_1), 1/(α_1 − a_1) ).
```

For `d = 2` this is the ordinary Euclidean step. Its periodicity for cubic irrationals is the famous open question the classical theory (Bernstein) answers only for special families,[^10] so the honest way to test it is with *exact* arithmetic in `Q(ρ)` - represent every quantity as a polynomial in `ρ` reduced modulo the minimal polynomial, invert with the extended Euclidean algorithm, and use floating point only to take floors:

```python
def jacobi_perron(f, x0, steps):
    """JPA on (rho, rho^2, ..., rho^{d-1}) for rho the root of f near x0, exact arithmetic in Q(rho)."""
    fP = sp.Poly(f, lam); d = fP.degree()
    r = findroot(lambda t: sum(int(cc)*t**(d-i) for i, cc in enumerate(fP.all_coeffs())), mpf(x0))
    red = lambda e: sp.rem(sp.Poly(e, lam, domain='QQ'), fP)
    val = lambda e: sum(mpf(int(cc.p))/int(cc.q) * r**(sp.Poly(e, lam).degree()-i)
                        for i, cc in enumerate(sp.Poly(e, lam, domain='QQ').all_coeffs()))
    inv = lambda e: sp.Poly(sp.invert(e.as_expr(), fP.as_expr(), lam), lam, domain='QQ')
    alphas = [red(lam**i) for i in range(1, d)]
    seen, digits = {}, []
    for n in range(steps):
        key = tuple(tuple(al.all_coeffs()) for al in alphas)
        if key in seen:
            return digits, f"periodic: preperiod {seen[key]}, period {n - seen[key]}"
        seen[key] = n
        a = [int(floor(val(al))) for al in alphas]; digits.append(a)
        i0 = inv(red(alphas[0] - a[0]))
        alphas = [red((alphas[j] - a[j]) * i0) for j in range(1, d-1)] + [red(i0)]
    return digits, f"no period within {steps} steps"
```

```
>>> jacobi_perron(lam**3 - 4*lam**2 + 4*lam - 8, 3.5, 40)                   # rho_6 = 2 psi^2
([[3, 12], [0, 1], [1, 1], [1, 1], [7, 8], [1, 1], [1, 1], [1, 1], [5, 9]], 'periodic: preperiod 5, period 4')
>>> jacobi_perron(lam**3 - 3*lam**2 + 2*lam - 4, 2.8, 400)[1]              # rho_4
'no period within 400 steps'
```

**`ρ_6` is JPA-periodic**: five preperiod digit pairs, then `[1,1], [1,1], [1,1], [5,9]` forever - the cubic analogue of `[2; 2, 2, …]`, and the affirmative answer to the IDEAS entry's "do the multi-variable convergents hit anything?" **`ρ_4` is not** periodic within 400 exact steps (largest digit seen 646), and neither are the quintics `ρ_8`, `ρ_10` within 60 - consistent with (though not proof of) the unit/non-unit split above: `ρ_6/2` is a unit; `ρ_4/2` is not an algebraic integer at all.[^9]

**The convergents, and the unit they encode.** Bernstein's convergent vectors `A^{(v)} ∈ Z³` start as the unit vectors and follow `A^{(v+3)} = A^{(v)} + a₁^{(v)} A^{(v+1)} + a₂^{(v)} A^{(v+2)}`; the first coordinate is the denominator, `A₁/A₀ → ρ`, `A₂/A₀ → ρ²`. The preperiod / period of the `ρ_6` expansion above splits its digit pairs into `pre` and `per`:

```python
# From jacobi_perron(lam**3 - 4*lam**2 + 4*lam - 8, 3.5, 40): preperiod 5, period 4.
pre = [[3, 12], [0, 1], [1, 1], [1, 1], [7, 8]]
per = [[1, 1], [1, 1], [1, 1], [5, 9]]

def jpa_convergents(digs):
    A = [sp.Matrix([1, 0, 0]), sp.Matrix([0, 1, 0]), sp.Matrix([0, 0, 1])]
    for a1, a2 in digs:
        A.append(A[-3] + a1*A[-2] + a2*A[-1])
    return A
```

```
>>> A = jpa_convergents(pre + per*10)
>>> [int(v[0]) for v in A[:16]]
[1, 0, 0, 1, 1, 2, 4, 47, 53, 104, 204, 2409, 2717, 5330, 10456, 123471]
>>> sp.N(A[30][1]/A[30][0], 22), sp.N(A[30][2]/A[30][0], 22)
(3.509755332493385518781, 12.31838249396575515334)      # rho_6 = 3.509755332493385520099..., rho_6^2 = 12.31838249396575514404...
```

Because the expansion is periodic, the denominators satisfy a linear recurrence (order 12, characteristic polynomial `(x⁶ − 7x⁴ − x² − 1)(x⁶ + 7x⁴ − x² + 1)`), and the every-fourth-term subsequences each satisfy `x³ − 51x² − 13x − 1`. That cubic is the characteristic polynomial of the **period matrix** - the product of the four step matrices over one period:

```
>>> M = sp.eye(3)
>>> for a1, a2 in per: M *= sp.Matrix([[0, 1, 0], [0, 0, 1], [1, a1, a2]])
>>> M.tolist(), M.det(), sp.factor(M.charpoly(x).as_expr())
([[1, 6, 10], [2, 11, 20], [4, 22, 39]], 1, x**3 - 51*x**2 - 13*x - 1)
>>> psi = sp.real_roots(sp.Poly([1, 0, -1, -1], sp.Symbol('t')))[0]     # plastic number
>>> sp.N(psi**14, 20)
51.254019310876249536                                    # = the dominant eigenvalue of M
```

Determinant 1 and dominant eigenvalue **`ψ^14`**: a periodic JPA expansion produces a unit of the field (Bernstein's theorem),[^10] and here it is the fourteenth power of the plastic number. The coefficients `51` and `−13` are `Perrin(14)` and `Perrin(−14)` - the trace of `ψ^14` and of `ψ^{−14}` - so **the period matrix is written in Perrin numbers**.[^9] None of the JPA convergent sequences is in OEIS (searched 2026-09-16); they are generation candidates, though a weaker kind than a castle count, since OEIS's convergent tables (the A041xxx family above) cover simple continued fractions only.

One more thing the convergents teach: `|ρ_6 − A₁/A₀| · A₀^{3/2}` stays between 0.15 and 0.9 for `v = 20, 40, 60, 80`, i.e. JPA convergents approximate a cubic to about `q^{−3/2}` - the Dirichlet rate for *simultaneous* approximation of `(ρ, ρ²)` - not the `q^{−2}` a simple continued fraction achieves for one number. That is the price of periodicity: the multidimensional expansion is the one that repeats, and the one-dimensional expansion is the one that approximates best.

## What this settles and what it opens

**Settled.**
- The convergent crosswalk for all five metallic rungs (Part 1): primary, trace, and `δ_a − 1` sequences, all offset-verified.
- The k-direction of `P(k, L)` is a quasi-polynomial with eigenvalues `±1` only, `(x + 1)^L (x − 1)^{L − 2}` (`L ≤ 12`), explicit `A_L, B_L` to `L = 12`, `|P(k, 4)|` = A352116 with the `C_3` crystal-ball and tetrahedral bisections, and the `2 · p^{⌈log_p L⌉}` mod-`p` period. Full write-up: [[signed-tower-k-direction](pages/signed-tower-k-direction.md)].
- The CF ↔ mod-`p` twin made quantitative: `N(δ) = −1` ⟺ purely periodic ⟺ `δ^{p+1} = −1` at inert primes (Part 2).
- `ρ_6 = 2ψ²`, `P(6,L) = 2^L·A005251(L+3) + remainder`, and a periodic Jacobi–Perron expansion for `ρ_6` with unit `ψ^14`.

**Open** (also filed on IDEAS).
- Prove `(x+1)^L (x−1)^{L−2}` (the Ehrhart sketch is the route) and find `A_L, B_L` uniformly - this is most of "General closed form for `P(k,L)`."
- Why the plastic field at `k = 6`, and why `ρ_k/2` is a unit exactly for `k ≡ 2 (mod 4)` - answered on [[tower-parity-sectors](pages/tower-parity-sectors.md)]: the even-`k` factors are `H_d(μ) = Σ (−1)^i C(⌊(d+i)/2⌋, i) μ^{d−i}` and its Lucas companion, `H_3` is the minimal polynomial of `ψ²`, and the dominant root lies in the monic factor `H_{k/2}` exactly when `k ≡ 2 (mod 4)`. The JPA of `ρ_10`, `ρ_10/2`, `ρ_14/2` is not periodic within 300 / 200 exact steps.
- A bijective reading of `P(6,L) = 2^L · #(no-isolated-1 strings) + …` - sharpened on [[tower-parity-sectors](pages/tower-parity-sectors.md)] to `P_even(6,L) = 2^L·A005251(L+3)` (even last column), and generalized to Hardin's word counts for every `k ≡ 2 (mod 4)`; the bijection itself is still open. Likewise `|P(k,4)|` as `C₃`-lattice crystal-ball / tetrahedral numbers.
- Whether the Axis-8 growth classification on [[castle-classification-growth](pages/castle-classification-growth.md)] should grow a non-metallic rung: `2ψ²` is a Pisot-type growth constant that is *not* a metallic mean.

## Snippet index (what each one teaches)

All snippets ran under Python 3.11 with SymPy 1.14 and mpmath 1.3; the DP and Berlekamp–Massey need only the standard library. Reusable ones are filed on [[castle-snippets-number-theory](pages/castle-snippets-number-theory.md)] (`convergents`, `order_mod` / `period_mod`, `P_table`, `quasi_split`, `M_signed` / `sectors`, `H(d)`).

| snippet | teaches | where |
|---|---|---|
| `convergents(digits)` | the three-term convergent recurrence; why period 1 ⇒ numerator = denominator shifted | Part 1 |
| `sp.continued_fraction_periodic(0, 1, d)` | SymPy's periodic CF of `√d`; period is a property of the number, not the field | Part 1 |
| `order_mod(a, c, p)`, `period_mod(a, p)` | build `F_p[t]/(t² − at + c)` by hand; Pisano period = eigenvalue order; the `δ^{p+1} = N(δ)` Frobenius argument | Part 2 |
| `P_table`, `berlekamp_massey`, `sp.factor` | the signed-tower DP; minimal recurrence; *always factor the characteristic polynomial* | [[signed-tower-k-direction]] |
| `quasi_split(seq, deg)` | a period-2 quasi-polynomial is two interpolations | [[signed-tower-k-direction]] |
| `period(seq)` on `P mod p` | repeated eigenvalues give `p^{⌈log_p m⌉}` | [[signed-tower-k-direction]] |
| `sp.resultant` twice | minimal polynomial of `ψ²` and of `2ψ²` without solving anything | Part 4 |
| `sp.apart` on `num_k/den_k` | partial fractions split a C-finite sequence into its eigenvalue blocks | Part 4 |
| `cf_digits` (mpmath, 200 digits) | simple CF of an algebraic number; Lagrange in action | Part 4 |
| `jacobi_perron` (exact in `Q(ρ)`) | multidimensional CF with exact periodicity detection | Part 4 |
| `jpa_convergents`, period matrix | Bernstein's convergents; periodic JPA ⇒ a unit (`ψ^14`), read off as Perrin numbers | Part 4 |
| `oeis_lookup(terms)` via `curl -A` | OEIS returns HyperText Transfer Protocol (HTTP) 403 to Python's default `urllib` User-Agent; send a real one and throttle | castle-snippets |

## Appearances in Sources

- [[oeis-mining-pe502](pages/oeis-mining-pe502.md)] - the `P(k,·)` C-finite family and `char_k`; the observation that the columns `F(w,·)` are `(x²−1)^w`-quasi-polynomials, which Part 3 sharpens to exact multiplicities.
- [[project-euler-502-solution](pages/project-euler-502-solution.md)] - the `num_k/den_k` recurrence behind `char_k` and the partial-fraction split of `P(6,L)`.
- [[project-euler-502-castle-factoring](pages/project-euler-502-castle-factoring.md)] - the block-count (total descent) formula the `P_table` DP implements.

## Related Concepts

- [[eigenvalue-continued-fractions](pages/eigenvalue-continued-fractions.md)] - the page whose abstract twin (CF period ↔ mod-p order) this one makes quantitative.
- [[metallic-means](pages/metallic-means.md)] / [[pell-numbers](pages/pell-numbers.md)] - the rungs of Part 1; their OEIS numbers are now all verified.
- [[signed-tower-k-direction](pages/signed-tower-k-direction.md)] - the full write-up of Part 3: `(x + 1)^L (x − 1)^{L − 2}`, the `A_L, B_L` quasi-polynomial table, `|P(k, 4)| = A352116`, and the mod-`p` period `2 · p^{⌈log_p L⌉}`.
- [[mod-p-observatory](pages/mod-p-observatory.md)] - the finite-field side; Part 2 is its real-number mirror.
- [[recurrence-discovery](pages/recurrence-discovery.md)] / [[closed-form-hunting](pages/closed-form-hunting.md)] - the `2L−2` orders and palindromic coefficient lists whose k-direction factorization is on the split page above.
- [[generating-function-gallery](pages/generating-function-gallery.md)] / [[signed-tower-count](pages/signed-tower-count.md)] - `char_k`, `ρ_k`, and the `P(k,·)` rows Part 4 decomposes.
- [[finite-fields](pages/finite-fields.md)] - `F_p` vs `F_{p²}`, the Frobenius, and why `δ^{p+1} = N(δ)`.
- [[oeis-cross-referencing](pages/oeis-cross-referencing.md)] - the offset-exact verification discipline every A-number here went through.
- [[castle-snippets](pages/castle-snippets.md)] - where the reusable snippets from this page are filed.
- [[pell-castle-strip](pages/pell-castle-strip.md)] - the silver-ratio seminar arc; its Pell numbers are the convergent denominators of `1 + √2` in Part 1.
- [[algebraic-transcendental-wall](pages/algebraic-transcendental-wall.md)] - every constant on this page is algebraic, as C-finiteness demands; `ψ` joins `φ` and `1+√2` on the algebraic side.
- [[tower-parity-sectors](pages/tower-parity-sectors.md)] / [[plastic-number](pages/plastic-number.md)] - the explanation of Part 4: the symmetry that factors `char_k`, the closed-form factors, and the plastic number's own page.
- [[castle-eigenvalues-by-example](pages/castle-eigenvalues-by-example.md)] - the from-scratch pedagogy that motivates the higher-degree eigenvalues of Part 4 by working small castles by hand.

## Footnotes

[^1]: [[oeis-mining-pe502](pages/oeis-mining-pe502.md)] `mine-notes.md` §"Vein 1" L31-37 - "The general P(k,·) family is C-finite of order k+1: P(1): x^2 - 2x + 2 ... P(5): x^6 - 6x^5 + 18x^4 - 32x^3 + 48x^2 - 32x + 32 (constant term = (-1)^{k-1} 2^k; leading coeff -(k+1))."

[^2]: [[project-euler-502-solution](pages/project-euler-502-solution.md)] §"The rational-function path (h ≤ 15000)" L124-138 - "F_k(x) = ∑_L P(k, L) x^L ... num_k(x) = 2·den_{k-1}(x) - num_{k-1}(x); den_k(x) = den_{k-1}(x)·(1 - 2x) + num_{k-1}(x)·x; F_k(x) = num_k(x)/den_k(x)." The three-term form `char_{k+1} = λ²·char_{k−1} − 2·char_k` used here is derived from it on [[generating-function-gallery](pages/generating-function-gallery.md)].

[^3]: [[project-euler-502-castle-factoring](pages/project-euler-502-castle-factoring.md)] §"The sign of a castle" L105-113 - "blocks = ∑_{i=0}^{L} max(0, c_i - c_{i+1}), c_0 = c_{L+1} = 0."

[^4]: [[oeis-mining-pe502](pages/oeis-mining-pe502.md)] `mine-notes.md` §"Vein 3" L77-79 - "Columns (fixed w, varying h) are quasi-polynomials: F(w,h) is annihilated by (x^2-1)^w, i.e. F(w,h) = P(h) + (-1)^h Q(h) with P,Q polynomials of degree < w." and L168 - "F(w,h), w>=3 (columns) | - | NEW (quasi-poly, (x^2-1)^w)".

[^5]: OEIS entries fetched by id on 2026-09-16 and matched offset-exact against the recurrence output (`x_0, x_1 = 0, 1`; trace `y_0, y_1 = 2, a`): https://oeis.org/A000045 "Fibonacci numbers"; https://oeis.org/A000032 "Lucas numbers beginning at 2"; https://oeis.org/A000129 "Pell numbers"; https://oeis.org/A002203 "Companion Pell numbers: a(n) = 2*a(n-1) + a(n-2), a(0) = a(1) = 2"; https://oeis.org/A001333 "Pell-Lucas numbers: numerators of continued fraction convergents to sqrt(2)"; https://oeis.org/A006190 "a(n) = 3*a(n-1) + a(n-2), with a(0)=0, a(1)=1"; https://oeis.org/A006497 "a(n) = 3*a(n-1) + a(n-2) with a(0) = 2, a(1) = 3"; https://oeis.org/A001076 "Denominators of continued fraction convergents to sqrt(5)"; https://oeis.org/A001077 "Numerators of continued fraction convergents to sqrt(5)"; https://oeis.org/A014448 "Even Lucas numbers: a(n) = L(3*n)"; https://oeis.org/A033887 "a(n) = Fibonacci(3*n + 1)"; https://oeis.org/A052918 "a(0) = 1, a(1) = 5, a(n+1) = 5*a(n) + a(n-1)" (offset 1 relative to `x_n`); https://oeis.org/A087130 "a(n) = 5*a(n-1)+a(n-2) for n>1, a(0)=2, a(1)=5"; https://oeis.org/A052924 "Expansion of generating function (GF): (1-x)/(1 - 3*x - x^2)"; https://oeis.org/A100237 (`(1-x)/(1-5x-x^2)`; its comment already reads "n-th convergent … = A100237(n)/A052918(n)"); and the `√d` convergent tables https://oeis.org/A041010, A041011 (`√8`), A041018, A041019 (`√13`), A041030, A041031 (`√20`), A041046, A041047 (`√29`), each named "Numerators/Denominators of continued fraction convergents to sqrt(d)".

[^6]: https://oeis.org/A352116 (2026-09-16) - "Partial sums of the odd triangular numbers (A014493)", data `1, 4, 19, 40, 85, 140, 231, 336, 489, 660, 891, 1144, 1469, …`; https://oeis.org/A014493 - "Odd triangular numbers", `1, 3, 15, 21, 45, 55, …`; https://oeis.org/A063496 - "a(n) = (2*n - 1)*(8*n^2 - 8*n + 3)/3", with Peter Bala's comment "this sequence is the crystal ball sequence for the C_3 lattice"; https://oeis.org/A199833 - data `4, 40, 140, 336, 660, 1144, …`, formula "a(n) = (16/3)*n^3 - (4/3)*n = 4*A000447(n)"; https://oeis.org/A000447 - "a(n) = 1^2 + 3^2 + 5^2 + … + (2*n-1)^2 = n*(4*n^2 - 1)/3", "a(n) = binomial(2*n+1, 3)"; https://oeis.org/A112742 - "a(n) = n^2*(n^2 - 1)/3". Searches for `P(k,5)`, `P(k,6)`, `P(k,7)`, the `N_L` rows, the `P(k,·)` rows for `k = 2, 4, 6, 8`, the CF digit strings and decimal expansions of `ρ_4`, `ρ_6`, and the JPA convergent sequences returned no results.

[^7]: https://oeis.org/A060006 (2026-09-16) - "Decimal expansion of real root of x^3 - x - 1 (the plastic constant)", `1.3247…`; https://oeis.org/A000931 - "Padovan sequence"; https://oeis.org/A001608 - "Perrin sequence", `3, 0, 2, 3, 2, 5, 5, 7, 10, 12, 17, 22, 29, 39, 51, …`; https://oeis.org/A005251 - offset 0, "a(0) = 0, a(1) = a(2) = a(3) = 1; thereafter, a(n) = a(n-1) + a(n-2) + a(n-4)", data `0, 1, 1, 1, 2, 4, 7, 12, 21, 37, 65, 114, 200, 351, 616, …`, formulas "a(n) = 2*a(n-1) - a(n-2) + a(n-3)" and "G.f.: z*(1-z)/(1 - 2*z + z^2 - z^3)", comment "a(n+3) is the number of n-bit sequences that avoid 010".

[^8]: Verified by execution (Python 3.11, SymPy 1.14, mpmath 1.3) while writing this page. (i) `P_table(60, 12)` + Berlekamp–Massey + `sp.factor`: characteristic polynomial equals `(x+1)^L (x−1)^{L−2}` for every `L = 4..12` (`sp.expand(charpoly − target) == 0`). (ii) `quasi_split` for `L = 1..12`, each `A_L, B_L` re-checked against all 61 DP values; leading coefficients read off as `2^{L−2}/(L−1)!` and `2^{2L−9}/(L−3)!` for `L ≤ 12`; `N_L(y)` obtained as the truncated series of `(Σ_k P(k,L) y^k)·(1+y)^L (1−y)^{L−2}`, with all coefficients beyond degree `2L−3` zero. (iii) Mod-`p` sweep: for `a = 1..5` and all primes `p < 100` with `p ∤ a²+4`, `period_mod(a,p) == lcm(ord δ, ord δ̂)` asserted, plus split ⇒ `ord | p−1` and inert ⇒ `δ^{p+1} = −1`, `ord | 2(p+1)`, `ord ∤ p+1`; control `x² − 3x + 1` at inert primes gives `(φ²)^{p+1} = 1`. (iv) k-direction periods of `P(·,L) mod p` for `L = 2..11`, `p ∈ {3,5,7,11}` equal `2·p^j` with `p^j` the least power `≥ L`. (v) Even `k ≤ 18`: dominant factor of `char_k`, its constant term, and whether `f(2μ)/2^{deg f}` is monic-integral with constant `−1`. (vi) `sp.apart(num_6/den_6)`: cubic component coefficients `1, 4, 16, 56, 192, 672, 2368, 8320, 29184, 102400, 359424, 1261568`, divided by `2^L` giving `1, 2, 4, 7, 12, 21, 37, 65, 114, 200, 351, 616`; remainder's Berlekamp–Massey characteristic polynomial `λ⁴ − 3λ³ + 8λ² − 4λ + 8`.

[^9]: Verified by execution: `jacobi_perron` with exact `Q(ρ)` arithmetic (SymPy `rem`/`invert` mod the minimal polynomial, mpmath at 600 digits for floors) - `ρ_6`: periodic, preperiod 5, period 4; `ρ_4`: no repeated state in 400 steps, largest digit 646; `ρ_8`, `ρ_10` (4-vectors): no repeated state in 60 steps. Bernstein convergents from the periodic digit string: `A₁/A₀ → ρ_6`, `A₂/A₀ → ρ_6²` to 22 digits by `v = 40`; denominators' Berlekamp–Massey order 12 with the stated factorization; every-4th subsequences order 3 with `x³ − 51x² − 13x − 1`; period matrix `[[1,6,10],[2,11,20],[4,22,39]]`, determinant 1, dominant eigenvalue `51.25401931087624953…` `= ψ^14`; Perrin numbers computed forward (`P(14) = 51`) and backward via `P(n) = P(n+3) − P(n+1)` (`P(−14) = −13`).

[^10]: Standard references, not ingested: J.-L. Lagrange's theorem (eventually periodic ⟺ quadratic) and the Pisano-period divisibility facts (`π(p) | p−1` for `p ≡ ±1 (mod 5)`, `π(p) | 2(p+1)` for `p ≡ ±2 (mod 5)`) are classical; L. Bernstein, *The Jacobi–Perron Algorithm: Its Theory and Application*, Lecture Notes in Mathematics 207 (Springer, 1971) is the source for the convergent recursion `A^{(v+n)} = A^{(v)} + Σ a_i^{(v)} A^{(v+i)}` and for "a periodic Jacobi–Perron expansion yields a unit of the field." The periodicity of the JPA for *all* cubic irrationals is an open problem, which is why the `ρ_4` result is reported as "no period within 400 steps" and not as non-periodicity.
