---
title: Castle eigenvalues meet OEIS - the convergent crosswalk
category: Analyses
summary: The convergents of the castle eigenvalues against the OEIS. Each metallic mean δ_a = [a; a, …] has numerators and denominators from one sequence, matched offset-exact for a ≤ 5 (Fibonacci, Pell A000129, A006190, A001076, A052918). The norm −1 makes δ_a purely periodic (Galois) and gives δ^{p+1} = −1 at every inert prime, so the period of the sequence modulo p divides 2(p+1) and not p+1. In the k-direction the characteristic polynomial of P(·, L) is (x+1)^L (x−1)^{L−2} for 4 ≤ L ≤ 12 (computed), with |P(k, 4)| = A352116(k+1). In the L-direction the dominant root of char_6 is 2ψ², ψ the plastic number; the even-sector part of P(6, L) is 2^L·A005251(L+3); and the Jacobi-Perron expansion of 2ψ² is periodic, with the unit ψ^14 as the dominant eigenvalue of its period matrix.
tags: [analysis, castle, continued-fraction, convergents, oeis, eigenvalue, quasi-polynomial, plastic-number, jacobi-perron, pisano, mod-p, sympy, verification, pedagogy]
sources: [oeis-mining-pe502, project-euler-502-solution, project-euler-502-castle-factoring]
created: 2026-09-16
updated: 2026-10-16
---

# Castle eigenvalues meet OEIS: the convergent crosswalk

The convergents `p_n/q_n` of a continued fraction are its truncations, and their numerators and denominators are integer sequences. This page computes them for the eigenvalues of the castle recurrences, matches them against the OEIS, and relates the continued-fraction period of an eigenvalue to its multiplicative order modulo `p` ([[eigenvalue-continued-fractions](pages/eigenvalue-continued-fractions.md)]). Its results:

1. **The metallic means** (Part 1). For `δ_a = [a; a, a, …]` the numerators and denominators are one recurrence sequence, one step apart, and the trace of the convergent matrix is the companion sequence. For `1 + √2` both are the Pell numbers `A000129`, and `A001333` is the numerator sequence of `√2 = (1 + √2) − 1`.
2. **The norm on both sides** (Part 2). The norm `δ_a·δ̂_a = −1` makes the continued fraction of `δ_a` purely periodic, and at every inert prime it gives `δ_a^{p+1} = −1`, so the period of the sequence modulo `p` divides `2(p + 1)` and not `p + 1`.
3. **The k-direction** (Part 3). For `4 ≤ L ≤ 12`, the characteristic polynomial of `P(·, L)` is `(x + 1)^L (x − 1)^{L−2}` (computed), so its eigenvalues are `±1` and there is no irrational continued fraction. `|P(k, 4)| = A352116(k + 1)`.
4. **The L-direction** (Part 4). The roots of `char_k` are the irrational eigenvalues. The dominant root of `char_6` is `2ψ²`, with `ψ` the plastic number; the even-sector part of `P(6, L)` is `2^L·A005251(L+3)`; and the Jacobi-Perron expansion of `2ψ²` is periodic, with period matrix of dominant eigenvalue `ψ^14`.

The snippets ran under Python 3.11 with SymPy and mpmath, and their outputs are reproduced as printed.[^8][^9]

## Part 1 - Convergents and the metallic crosswalk

### Convergents

Truncate `[a₀; a₁, a₂, …]` after `n` terms and clear denominators. The numerator and the denominator of `p_n/q_n` obey the same three-term recurrence,

```
p_n = a_n p_{n−1} + p_{n−2},     q_n = a_n q_{n−1} + q_{n−2},
```

with `(p_{−1}, p_{−2}) = (1, 0)` and `(q_{−1}, q_{−2}) = (0, 1)`:

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

When every digit is `a`, the convergent recurrence is the recurrence `x_n = a·x_{n−1} + x_{n−2}` with `x_0 = 0`, `x_1 = 1`, so `q_n = x_{n+1}` and `p_n = x_{n+2}`: the convergents of `φ` are `F_{n+2}/F_{n+1}` and those of `1 + √2` are `P⋆_{n+2}/P⋆_{n+1}`, with `P⋆` the Pell numbers. In matrix form `[[p_n, p_{n−1}], [q_n, q_{n−1}]] = M^{n+1}` with `M = [[a, 1], [1, 0]]` and `det M = −1`, and the trace `p_n + q_{n−1}` is the companion sequence `y_{n+1} = δ_a^{n+1} + δ̂_a^{n+1}`, with `δ̂_a = a − δ_a` the conjugate of `δ_a`:

```
>>> [p - q for p, q in convergents([2]*8)]            # convergent numerators of sqrt(2) = [1; 2, 2, ...]
[1, 3, 7, 17, 41, 99, 239, 577]
>>> [p + q_prev for (p, _), (_, q_prev) in zip(convergents([2]*8)[1:], convergents([2]*8))]
[6, 14, 34, 82, 198, 478, 1154]                        # companion Pell A002203 from index 2
```

Subtracting 1 changes only `a₀`, so `√2 = (1 + √2) − 1` has the same denominators and the numerators `p_n − q_n`, the sequence `A001333`.

### The crosswalk table

Every A-number in the table was checked against the OEIS data at the stated offset.[^5]

| `a` | `δ_a = [a; a, …]` | `q_n = x_{n+1}`, `p_n = x_{n+2}` | trace `y_n = δ_a^n + δ̂_a^n` | `p_n − q_n` (convergents of `δ_a − 1`) | `√(a² + 4)` | its convergents (numerators / denominators) |
|---|---|---|---|---|---|---|
| 1 | `φ` | `A000045` Fibonacci | `A000032` Lucas | `A000045` (`φ − 1 = 1/φ`) | `[2; 4̄]` | `A001077` / `A001076` |
| 2 | `1 + √2` | `A000129` Pell | `A002203` companion Pell (`= 2·A001333`) | `A001333` (numerators of `√2`) | `[2; 1, 4]` (period 2) | `A041010` / `A041011` |
| 3 | `(3 + √13)/2` | `A006190` | `A006497` | `A052924` | `[3; 1, 1, 1, 1, 6]` (period 5) | `A041018` / `A041019` |
| 4 | `2 + √5 = φ³` | `A001076` | `A014448`, `L_{3n}` | `A033887`, `F_{3n+1}` | `[4; 2, 8]` (period 2) | `A041030` / `A041031` |
| 5 | `(5 + √29)/2` | `A052918`, with `A052918(n) = x_{n+1}` | `A087130` | `A100237` | `[5; 2, 1, 1, 2, 10]` (period 5) | `A041046` / `A041047` |

- **The period belongs to the number.** `δ_3 = (3 + √13)/2` has period 1, and `√13 = 2δ_3 − 3`, in the same field, has period 5. `√(a² + 4) = 2δ_a − a` in general; at `a = 4`, `√5 = δ_4 − 2`, since `δ_4 = φ³ = 2 + √5` ([[metallic-means](pages/metallic-means.md)]), which is why `A001076` is both the `δ_4` sequence and the denominators of the convergents of `√5`.
- **The continued fractions of `√(a² + 4)`** are from SymPy, `sp.continued_fraction_periodic(0, 1, a*a + 4)`: `[2, [4]]`, `[2, [1, 4]]`, `[3, [1, 1, 1, 1, 6]]`, `[4, [2, 8]]`, `[5, [2, 1, 1, 2, 10]]`.
- **Trace and half-trace.** At `a = 2` the trace sequence `2, 2, 6, 14, 34, …` is `A002203`, and its half `1, 1, 3, 7, 17, …` is `A001333`, the numerators of the convergents of `√2`.

## Part 2 - The norm modulo p

Reduce `M = [[a, 1], [1, 0]]` modulo a prime `p ∤ a² + 4`. The sequence `x_n mod p` is periodic, with period the order of `M` in `GL₂(F_p)`, which is the lcm of the orders of its eigenvalues `δ` and `δ̂` in the field that contains them. When `a² + 4` is a square modulo `p`, `x² − ax − 1` factors over `F_p` and `p` is **split** in `Q(√(a² + 4))`; when it is not, `x² − ax − 1` is irreducible over `F_p`, its roots lie in `F_{p²}`, and `p` is **inert**. The computation, in a quotient ring built by hand:

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
>>> [(p, order_mod(3, 1, p), int(sp.legendre_symbol(5, p))) for p in (3, 7, 11, 13, 19)]   # phi^2, norm +1
[(3, 4, -1), (7, 8, -1), (11, 5, 1), (13, 14, -1), (19, 9, 1)]
```

- **Split primes.** `δ ∈ F_p^*`, so its order divides `p − 1`: at `a = 1`, order 10 at `p = 11` and 18 at `p = 19`.
- **Inert primes.** The Frobenius map `z ↦ z^p` is the automorphism of `F_{p²}` that fixes `F_p` and swaps the two roots of an irreducible quadratic over `F_p`, so `δ^p = δ̂` and `δ^{p+1} = δ·δ̂ = −1`. So the order of `δ` divides `2(p + 1)` and not `p + 1`: at `a = 1`, 8 at `p = 3`, 16 at `p = 7` and 28 at `p = 13`.
- **Norm `+1`.** `φ² = (3 + √5)/2`, the root of `x² − 3x + 1`, has norm `+1`, so at inert primes `(φ²)^{p+1} = 1` and its order divides `p + 1`: 4 at `p = 3`, 8 at `p = 7`, 14 at `p = 13`.

So the norm decides two things. Over the reals, a quadratic surd `α > 1` has a purely periodic continued fraction exactly when its conjugate lies in `(−1, 0)` (Galois); for a surd of norm `−1`, the conjugate is `−1/α`, which lies there.[^10] Modulo `p`, the norm is `δ^{p+1}` at the inert primes.

For `a ≤ 5` and every prime `3 ≤ p < 100` with `p ∤ a² + 4`, the period of `x_n mod p` is the lcm of the orders of `δ` and `δ̂`, the order divides `p − 1` at split primes, and at inert primes `δ^{p+1} = −1`, so the order divides `2(p + 1)` and not `p + 1`.[^8] At inert primes `δ` and `δ̂ = δ^p` have the same order. At split primes the orders can differ: for `a = 1`, `p = 11`, `δ ≡ 8` has order 10 and `δ̂ ≡ 4` has order 5.

## Part 3 - The k-direction

`P(k, L)` is computed by a dynamic program over the column heights, with the block count as total descent.[^3] For `4 ≤ L ≤ 12`, the shortest recurrence of `P(·, L)` in the tower height `k` has characteristic polynomial `(x + 1)^L (x − 1)^{L−2}` (computed); at every `L` it divides `(x − 1)^{L+1} (x + 1)^L` (the Lemma of [[mod-9-coset-lift](pages/mod-9-coset-lift.md)]), since `P(k, L)` is a polynomial in `k` of degree at most `L` on each class of `k` modulo 2 ([[sum-of-three-cubes-castles](pages/sum-of-three-cubes-castles.md)], section *The residue test*). Its eigenvalues are `±1`, and

```
P(k, L)  =  (−1)^k · A_L(k) + B_L(k),         deg A_L ≤ L − 1,  deg B_L ≤ L − 3,
```

for these `L`. [[signed-tower-k-direction](pages/signed-tower-k-direction.md)] gives the polynomials `A_L`, `B_L`, the OEIS identities of the rows, and the periods modulo primes:

- `|P(k, 4)| = A352116(k + 1)`, the partial sums of the odd triangular numbers; `P(2m, 4) = A063496(m + 1)` and `|P(2m + 1, 4)| = A199833(m + 1) = 4·A000447(m + 1)`.[^6]
- The period of `P(·, L) mod p` in `k` is `2·p^j`, with `p^j` the least power of `p` that is at least `L`, for `2 ≤ L ≤ 11` and `p ∈ {3, 5, 7, 11}` (computed). At `L = 4` and `p = 3` this is `2·3² = 18`, the period of `A^e(4, ·)` modulo 3 on [[mod-p-observatory](pages/mod-p-observatory.md)].[^8]
- The OEIS-mining notes observe that the columns `A^e(w, ·)` are annihilated by `(x² − 1)^w`.[^4]

The eigenvalues are `±1`, so there is no irrational continued fraction in this direction. Modulo `p` there is no `p + 1` against `2(p + 1)`: the repeated eigenvalues `±1` give the factor `p^j`.

## Part 4 - The L-direction

### The plastic number

The recurrences of `P(k, ·)` in `L` have characteristic polynomials `char_k(λ) = λ^{k+1} den_k(1/λ)` of degree `k + 1`, with `char_0 = λ − 1`, `char_1 = λ² − 2λ + 2`, `char_{k+1} = λ²·char_{k−1} − 2·char_k`, and constant term `(−1)^{k+1} 2^k` ([[signed-tower-count](pages/signed-tower-count.md)]).[^1][^2] For even `k`, `char_k` has two irreducible factors and the root of largest modulus `ρ_k` is real ([[tower-parity-sectors](pages/tower-parity-sectors.md)]); for odd `k ≤ 31` it is irreducible (proved for `k = 2^m − 1` on [[char-k-eisenstein-at-two](pages/char-k-eisenstein-at-two.md)]), with a complex-conjugate pair of largest modulus ([[generating-function-gallery](pages/generating-function-gallery.md)]). The product of all the roots of `char_k` is `2^k`, so divide the dominant root by 2:

```
>>> sp.factor(c[6])
(lam**3 - 4*lam**2 + 4*lam - 8)*(lam**4 - 3*lam**3 + 8*lam**2 - 4*lam + 8)
>>> sp.factor(sp.resultant(x**3 - x - 1, mu - x**2, x))        # minimal polynomial of psi^2
mu**3 - 2*mu**2 + mu - 1
>>> sp.factor(sp.resultant(mu**3 - 2*mu**2 + mu - 1, lam - 2*mu, mu))   # minimal polynomial of 2 psi^2
lam**3 - 4*lam**2 + 4*lam - 8
```

So `ρ_6 = 2ψ² = 3.50975533249…`, where `ψ = 1.3247…` is the plastic number, the real root of `x³ = x + 1` (`A060006`), the smallest Pisot number ([[plastic-number](pages/plastic-number.md)]).[^7] The same test for the even `k ≤ 18`:[^8]

| `k` | `ρ_k` | minimal polynomial of `ρ_k` | degree | `ρ_k / 2` | algebraic unit |
|---|---|---|---|---|---|
| 2 | `2` | `λ − 2` | 1 | `1` | yes |
| 4 | `2.796321903…` | `λ³ − 3λ² + 2λ − 4` | 3 | root of `μ³ − 3μ²/2 + μ/2 − 1/2`, not an algebraic integer | no |
| 6 | `3.509755332…` | `λ³ − 4λ² + 4λ − 8` | 3 | `ψ²`, root of `μ³ − 2μ² + μ − 1` | yes |
| 8 | `4.174029055…` | `λ⁵ − 5λ⁴ + 8λ³ − 20λ² + 8λ − 16` | 5 | not an algebraic integer | no |
| 10 | `4.804417668…` | `λ⁵ − 6λ⁴ + 12λ³ − 32λ² + 16λ − 32` | 5 | root of `μ⁵ − 3μ⁴ + 3μ³ − 4μ² + μ − 1` | yes; a conjugate has modulus 1.09, so not a Pisot number |
| 12 | `5.409433398…` | degree 7 | 7 | not an algebraic integer | no |
| 14 | `5.994422837…` | degree 7 | 7 | root of `μ⁷ − 4μ⁶ + 6μ⁵ − 10μ⁴ + 5μ³ − 6μ² + μ − 1` | yes |
| 16 | `6.563018640…` | degree 9 | 9 | not an algebraic integer | no |
| 18 | `7.117830358…` | degree 9 | 9 | root of `μ⁹ − 5μ⁸ + 10μ⁷ − 20μ⁶ + 15μ⁵ − 21μ⁴ + 7μ³ − 8μ² + μ − 1` | yes |

For even `k ≤ 18`, both factors of `char_k` have constant term of absolute value `2^{k/2}`. For even `k ≤ 40`, the dominant root lies in the factor of degree `k/2` exactly when `k ≡ 2 (mod 4)`, and then `ρ_k/2` is an algebraic unit; when `k ≡ 0 (mod 4)` it lies in the factor of degree `k/2 + 1`, and `ρ_k/2` is not an algebraic integer (computed).[^8] [[tower-parity-sectors](pages/tower-parity-sectors.md)] derives the two factors.

**The plastic part of `P(6, L)`.** Partial fractions split `P_6(x) = num_6(x)/den_6(x)` into a part with the cubic denominator, from the factor of `2ψ²`, and a part with the quartic denominator:[^7][^8]

```python
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

These are `A005251(L+3)`, which satisfy `a(n) = 2a(n−1) − a(n−2) + a(n−3)` and by the OEIS comment count the binary strings of length `L` that avoid `010`. So

```
P(6, L)  =  2^L · A005251(L+3)  +  r(L),
```

where `r(L) = 0, −3, −9, −7, 39, 161, 215, −431, …` has characteristic polynomial `λ⁴ − 3λ³ + 8λ² − 4λ + 8`. The two parts are the even-sector and odd-sector parts of `P(6, ·)` ([[tower-parity-sectors](pages/tower-parity-sectors.md)]), and [[hardin-word-identity](pages/hardin-word-identity.md)] proves `P_even(6, L) = 2^L·A005251(L+3)` by a change of basis.

### Simple continued fractions

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
>>> cf_digits([1, -2, -1], 2.4, 8)        # 1 + sqrt(2)
[2, 2, 2, 2, 2, 2, 2, 2]
```

`ρ_4` and `ρ_6` are cubic irrationals, so their simple continued fractions are not eventually periodic: a real number has an eventually periodic continued fraction exactly when it is a quadratic irrational (Lagrange).[^10]

### The Jacobi-Perron algorithm

The Jacobi-Perron algorithm is a continued fraction for a vector. For `ρ` of degree `d`, start from `(α_1, …, α_{d−1}) = (ρ, ρ², …, ρ^{d−1})`, take the integer parts `a_i = ⌊α_i⌋`, and map

```
(α_1, …, α_{d−1})  ↦  ( (α_2 − a_2)/(α_1 − a_1), …, (α_{d−1} − a_{d−1})/(α_1 − a_1), 1/(α_1 − a_1) ).
```

For `d = 2` this is the step of the simple continued fraction. The snippet runs it in exact arithmetic in `Q(ρ)`, with every quantity a polynomial in `ρ` reduced modulo the minimal polynomial and inverses from the extended Euclidean algorithm; floating point is used only to take the integer parts:

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

The expansion of `ρ_6` is periodic: five digit pairs, then `[1, 1], [1, 1], [1, 1], [5, 9]` repeating. The expansion of `ρ_4` has no period within 400 exact steps (largest digit 646), and those of the quintics `ρ_8`, `ρ_10` none within 60.[^9]

**Convergents and the unit.** The convergent vectors `A^{(v)} ∈ Z³` start as the unit vectors and follow `A^{(v+3)} = A^{(v)} + a₁^{(v)} A^{(v+1)} + a₂^{(v)} A^{(v+2)}`; the first coordinate is the denominator, with `A₁/A₀ → ρ` and `A₂/A₀ → ρ²`:

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

The expansion is periodic, so the denominators after the preperiod satisfy a linear recurrence, of order 12 with characteristic polynomial `(x⁶ − 7x⁴ − x² − 1)(x⁶ + 7x⁴ − x² + 1)`, and every fourth term satisfies the recurrence with characteristic polynomial `x³ − 51x² − 13x − 1`. That cubic is the characteristic polynomial of the **period matrix**, the product of the four step matrices of one period:

```
>>> M = sp.eye(3)
>>> for a1, a2 in per: M *= sp.Matrix([[0, 1, 0], [0, 0, 1], [1, a1, a2]])
>>> M.tolist(), M.det(), sp.factor(M.charpoly(x).as_expr())
([[1, 6, 10], [2, 11, 20], [4, 22, 39]], 1, x**3 - 51*x**2 - 13*x - 1)
>>> psi = sp.real_roots(sp.Poly([1, 0, -1, -1], sp.Symbol('t')))[0]     # plastic number
>>> sp.N(psi**14, 20)
51.254019310876249536                                    # = the dominant eigenvalue of M
```

`M` has integer entries and determinant 1, so its characteristic polynomial is monic with integer coefficients and constant term `−1`, and its eigenvalues are algebraic units. The dominant one is `ψ^14`. Since `ψ` and its two conjugates have product 1, the coefficients `51` and `−13` are `Perrin(14)` and `Perrin(−14)`, the sums of the fourteenth powers of `ψ` and its conjugates and of their inverses.[^9]

The convergents approximate `ρ_6` at the rate `q^{−3/2}`: `|ρ_6 − A₁/A₀|·A₀^{3/2}` lies between 0.14 and 0.91 at `v = 20, 40, 60, 80`.[^9] This is Dirichlet's rate for the simultaneous approximation of the pair `(ρ, ρ²)`, against `q^{−2}` for the simple continued fraction of a single number.

## Snippet index

All snippets ran under Python 3.11 with SymPy and mpmath; the dynamic program and Berlekamp-Massey need only the standard library. Reusable ones are on [[castle-snippets-number-theory](pages/castle-snippets-number-theory.md)].

| snippet | computes | where |
|---|---|---|
| `convergents(digits)` | the convergents of a continued fraction by the three-term recurrence | Part 1 |
| `sp.continued_fraction_periodic(0, 1, d)` | the periodic continued fraction of `√d` | Part 1 |
| `order_mod(a, c, p)`, `period_mod(a, p)` | the order of a root of `t² − at + c` in `F_p[t]/(t² − at + c)`, and the period of `x_n mod p` | Part 2 |
| `P_table`, `berlekamp_massey`, `sp.factor` | `P(k, L)` by the dynamic program, its shortest recurrence in `k`, and the factored characteristic polynomial | [[signed-tower-k-direction](pages/signed-tower-k-direction.md)] |
| `quasi_split(seq, deg)` | the polynomials `A_L`, `B_L` by interpolating even and odd `k` | [[signed-tower-k-direction](pages/signed-tower-k-direction.md)] |
| `period(seq)` on `P mod p` | the period of `P(·, L) mod p` in `k` | [[signed-tower-k-direction](pages/signed-tower-k-direction.md)] |
| `sp.resultant` | the minimal polynomials of `ψ²` and `2ψ²` | Part 4 |
| `sp.apart` on `num_k/den_k` | the partial-fraction split of `P_k(x)` by factor of the denominator | Part 4 |
| `cf_digits` | the simple continued fraction of an algebraic number, at 200 digits | Part 4 |
| `jacobi_perron` | the Jacobi-Perron expansion in exact arithmetic, with period detection | Part 4 |
| `jpa_convergents`, period matrix | the convergent vectors and the period matrix of a periodic expansion | Part 4 |

## Appearances in Sources

- [[oeis-mining-pe502](pages/oeis-mining-pe502.md)] - the characteristic polynomials of `P(k, ·)`, and the observation that the columns `A^e(w, ·)` are annihilated by `(x² − 1)^w`.
- [[project-euler-502-solution](pages/project-euler-502-solution.md)] - the update of `num_k` and `den_k`, from which `char_k` and the partial fractions of `P_6(x)` are computed.
- [[project-euler-502-castle-factoring](pages/project-euler-502-castle-factoring.md)] - the block count as total descent, which the dynamic program for `P(k, L)` uses.

## Related Concepts

- [[eigenvalue-continued-fractions](pages/eigenvalue-continued-fractions.md)] - continued fractions, Lagrange's and Galois's theorems, and the castle eigenvalues.
- [[metallic-means](pages/metallic-means.md)] and [[pell-numbers](pages/pell-numbers.md)] - the metallic means `δ_a` and their sequences.
- [[signed-tower-k-direction](pages/signed-tower-k-direction.md)] - the recurrences of `P(·, L)` in `k`: characteristic polynomials, `A_L`, `B_L`, OEIS identities and periods modulo primes.
- [[mod-p-observatory](pages/mod-p-observatory.md)] - the factorizations and periods of `char_k` modulo `p = 3, 5, 7`.
- [[recurrence-discovery](pages/recurrence-discovery.md)] and [[closed-form-hunting](pages/closed-form-hunting.md)] - the orders `k + 1` in `L` and `2L − 2` in `k`, and the closed forms of `P(k, L)` in `k`.
- [[generating-function-gallery](pages/generating-function-gallery.md)] and [[signed-tower-count](pages/signed-tower-count.md)] - `char_k`, `ρ_k`, and the rows `P(k, ·)`.
- [[finite-fields](pages/finite-fields.md)] - `F_p` and `F_{p²}` and the Frobenius map.
- [[oeis-cross-referencing](pages/oeis-cross-referencing.md)] - matching sequences against the OEIS at their offsets.
- [[pell-castle-strip](pages/pell-castle-strip.md)] - the anchored strips counted by the Pell numbers, the denominators of the convergents of `1 + √2`.
- [[algebraic-transcendental-wall](pages/algebraic-transcendental-wall.md)] - algebraic and transcendental generating functions and constants.
- [[tower-parity-sectors](pages/tower-parity-sectors.md)] and [[plastic-number](pages/plastic-number.md)] - the factors of `char_k` for even `k`, and the plastic number.
- [[hardin-word-identity](pages/hardin-word-identity.md)] - the proof of `P_even(4m + 2, L) = 2^L` times a count of words, with `m = 1` giving `2^L·A005251(L+3)`.

## Footnotes

[^1]: [[oeis-mining-pe502](pages/oeis-mining-pe502.md)] `mine-notes.md` §"Vein 1" L31-37 - "The general P(k,·) family is C-finite of order k+1: P(1): x^2 - 2x + 2 ... P(5): x^6 - 6x^5 + 18x^4 - 32x^3 + 48x^2 - 32x + 32 (constant term = (-1)^{k-1} 2^k; leading coeff -(k+1))."

[^2]: [[project-euler-502-solution](pages/project-euler-502-solution.md)] §"The rational-function path (h ≤ 15000)" L124-138 - "F_k(x) = ∑_L P(k, L) x^L ... num_k(x) = 2·den_{k-1}(x) - num_{k-1}(x); den_k(x) = den_{k-1}(x)·(1 - 2x) + num_{k-1}(x)·x; F_k(x) = num_k(x)/den_k(x)." The source's `F_k(x)` is the wiki's `P_k(x)`.

[^3]: [[project-euler-502-castle-factoring](pages/project-euler-502-castle-factoring.md)] §"The sign of a castle" L104-108 - "In the column-height form, the block count is the total descent: blocks = ∑_{i=0}^{L} max(0, c_i - c_{i+1}), c_0 = c_{L+1} = 0".

[^4]: [[oeis-mining-pe502](pages/oeis-mining-pe502.md)] `mine-notes.md` §"Vein 3" L77-79 - "Columns (fixed w, varying h) are quasi-polynomials: F(w,h) is annihilated by (x^2-1)^w, i.e. F(w,h) = P(h) + (-1)^h Q(h) with P,Q polynomials of degree < w." The notes' `F(w, h)` is `A^e(w, h)`.

[^5]: OEIS entries read 2026-10-16 and matched against the recurrence output (`x_0, x_1 = 0, 1`; trace `y_0, y_1 = 2, a`): https://oeis.org/A000045 "Fibonacci numbers"; https://oeis.org/A000032 "Lucas numbers beginning at 2"; https://oeis.org/A000129 "Pell numbers"; https://oeis.org/A002203 "Companion Pell numbers: a(n) = 2*a(n-1) + a(n-2), a(0) = a(1) = 2"; https://oeis.org/A001333 "Pell-Lucas numbers: numerators of continued fraction convergents to sqrt(2)"; https://oeis.org/A006190 "a(n) = 3*a(n-1) + a(n-2), with a(0)=0, a(1)=1"; https://oeis.org/A006497 "a(n) = 3*a(n-1) + a(n-2) with a(0) = 2, a(1) = 3"; https://oeis.org/A052924 "Expansion of g.f.: (1-x)/(1 - 3*x - x^2)"; https://oeis.org/A001076 "Denominators of continued fraction convergents to sqrt(5)"; https://oeis.org/A001077 "Numerators of continued fraction convergents to sqrt(5)"; https://oeis.org/A014448 "Even Lucas numbers: a(n) = L(3*n)"; https://oeis.org/A033887 "a(n) = Fibonacci(3*n + 1)"; https://oeis.org/A052918 "a(0) = 1, a(1) = 5, a(n+1) = 5*a(n) + a(n-1)"; https://oeis.org/A087130 "a(n) = 5*a(n-1)+a(n-2) for n>1, a(0)=2, a(1)=5"; https://oeis.org/A100237 "Secondary diagonal of triangle A100235 divided by row number", data `1, 4, 21, 109, 566, …`; and https://oeis.org/A041010, A041011 (`√8`), A041018, A041019 (`√13`), A041030, A041031 (`√20`), A041046, A041047 (`√29`), each named "Numerators" or "Denominators of continued fraction convergents to sqrt(d)".

[^6]: https://oeis.org/A352116 (read 2026-10-16) - "Partial sums of the odd triangular numbers (A014493)", offset 1, data `1, 4, 19, 40, 85, 140, 231, …`; https://oeis.org/A063496 - "a(n) = (2*n - 1)*(8*n^2 - 8*n + 3)/3", data `1, 19, 85, 231, …`; https://oeis.org/A199833 - "Number of -n..n arrays of 4 elements with zero sum and no two neighbors summing to zero", data `4, 40, 140, 336, …`; https://oeis.org/A000447 - "a(n) = 1^2 + 3^2 + 5^2 + 7^2 + ... + (2*n-1)^2 = n*(4*n^2 - 1)/3", data `0, 1, 10, 35, …`.

[^7]: https://oeis.org/A060006 (read 2026-10-16) - "Decimal expansion of real root of x^3 - x - 1 (the plastic constant)"; https://oeis.org/A005251 - "a(0) = 0, a(1) = a(2) = a(3) = 1; thereafter, a(n) = a(n-1) + a(n-2) + a(n-4)", data `0, 1, 1, 1, 2, 4, 7, 12, 21, 37, 65, 114, 200, 351, 616, …`, formula "a(n) = 2*a(n-1) - a(n-2) + a(n-3)", comment "a(n+3) is the number of n-bit sequences that avoid 010".

[^8]: Verified by execution (Python 3.11 with SymPy and mpmath, 2026-10-16): the continued fractions of `√(a² + 4)` for `a ≤ 5`; for `a ≤ 5` and primes `3 ≤ p < 100` with `p ∤ a² + 4`, the period of `x_n mod p` equal to the lcm of the orders of the roots, the order dividing `p − 1` at split primes, and `δ^{p+1} = −1` with the order dividing `2(p + 1)` and not `p + 1` at inert primes; the orders of `φ²` at `p = 3, 7, 13`; the periods of `P(·, L) mod p` in `k` for `2 ≤ L ≤ 11`, `p ∈ {3, 5, 7, 11}`; the table for even `k ≤ 18` (dominant factor, its constant term, `ρ_k/2` integral with constant `±1`, the moduli of the conjugates at `k = 10`), and the location of the dominant root for even `k ≤ 40`; `sp.apart(num_6/den_6)`, with the cubic part `2^L·A005251(L+3)` and the quartic part `0, −3, −9, −7, 39, 161, 215, −431`.

[^9]: Verified by execution (Python 3.11 with SymPy and mpmath, 2026-10-16): the Jacobi-Perron expansion in exact arithmetic over `Q(ρ)` (rationals, with floors from mpmath at 300 to 3000 digits): `ρ_6` periodic with preperiod 5 and period 4; `ρ_4` no repeated state in 400 steps, largest digit 646; `ρ_8` and `ρ_10` no repeated state in 60 steps; the convergent denominators, their Berlekamp-Massey recurrence of order 12 with the stated factorization, and the order-3 recurrence of every fourth term; the period matrix, its determinant 1, characteristic polynomial `x³ − 51x² − 13x − 1` and dominant eigenvalue `51.25401931087624953… = ψ^14`; `|ρ_6 − A₁/A₀|·A₀^{3/2}` = 0.856, 0.148, 0.694, 0.904 at `v = 20, 40, 60, 80`.

[^10]: https://www.numdam.org/article/AMPA_1828-1829__19__294_0.pdf (read 2026-10-16) - É. Galois, "Démonstration d'un théorème sur les fractions continues périodiques", Annales de Mathématiques pures et appliquées 19 (1828-1829), 294-301. p.294: "si, par la méthode de Lagrange, on développe en fraction continue une des racines d'une équation du second degré, cette fraction continue sera périodique" (the periodicity of quadratic irrationals, attributed to Lagrange); pp.298-299: a root greater than 1 of a quadratic is immediately (purely) periodic exactly when the other root lies between 0 and −1.
