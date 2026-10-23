---
title: Castle snippets - number theory
category: Concepts
summary: Tested Python snippets for the signed tower count P(k, L), continued-fraction convergents, orders and periods modulo p, the split of P(·, L) into (−1)^k A(k) + B(k), the signed transfer matrix M̃_k and its parity sectors, the factor H_d, simple and Jacobi-Perron continued fractions, and the ring theory of char_k (its shape mod 2, CRT and Lagrange idempotents, the sector resultant, reduced periods, the sector idempotent, ideal counts and the Frobenius map of the fibers, the conductors of the metallic rings, the inverse of x). Every output is rerun; sibling of castle-snippets.
tags: [concept, castle, python, snippets, signed-tower-count, continued-fraction, mod-p, quasi-polynomial, plastic-number]
sources: [project-euler-502-brute-force, calugareanu-hamburg-exercises-basic-ring-theory]
created: 2026-09-19
updated: 2026-10-23
---

# Castle snippets - number theory

A sibling page to [[castle-snippets](pages/castle-snippets.md)]: snippets that compute the signed tower count `P(k, L)`, continued-fraction convergents, periods modulo `p`, the split of `P(·, L)` into `(−1)^k A(k) + B(k)`, and the factor `H_d` behind the plastic root of `char_6`. Every output on this page was rerun on 2026-10-16 (Python 3.11 with SymPy and mpmath).[^1]

## The signed tower count

### `p_signed(k, L)` → the signed tower count P(k,L)

The sum of `(−1)^{blocks}` over the towers of height at most `k` on a base of length `L`, by a dynamic program over the height of the last column, `O(k²L)` operations ([[signed-tower-count](pages/signed-tower-count.md)]). A column of height `b` after a column of height `a` starts `max(0, b − a)` blocks.

```python
def p_signed(k, L):
    dp = {0: 1}                       # last-column height -> signed count so far
    for _ in range(L):
        nd = {}
        for a, w in dp.items():
            for b in range(k + 1):
                nd[b] = nd.get(b, 0) + w * (-1) ** max(0, b - a)
        dp = nd
    return sum(dp.values())
```

```
>>> [p_signed(1, L) for L in range(8)]        # Re((1+i)^{L+1}) = A146559(L+1)
[1, 0, -2, -4, -4, 0, 8, 16]
>>> [p_signed(2, L) for L in range(10)]       # order 3
[1, 1, 3, 9, 19, 33, 59, 121, 259, 529]
>>> [p_signed(4, L) for L in range(9)]        # order 5
[1, 1, 5, 25, 85, 225, 541, 1385, 3973]
```

Meaning: `P(k, ·)` satisfies a linear recurrence of order `k + 1`, and the denominators of its generating functions satisfy `den_{k+1} = den_{k−1} − 2x·den_k`, the Pell-polynomial recurrence in `−x` ([[signed-tower-count](pages/signed-tower-count.md)], [[generating-function-gallery](pages/generating-function-gallery.md)]). The rows for even `k ≤ 12` are positive for `L < 40`; for odd `k ≤ 7` the roots of largest modulus are a complex pair, and the rows change sign in runs (computed).

## Continued fractions, convergents, and quasi-polynomials

Snippets behind [[castle-eigenvalue-oeis-crosswalk](pages/castle-eigenvalue-oeis-crosswalk.md)] and [[eigenvalue-continued-fractions](pages/eigenvalue-continued-fractions.md)]. The snippets through `berlekamp_massey` are stdlib-only; the rest need SymPy or mpmath, as marked.

### `convergents(digits)` → list of `(p_n, q_n)`

The three-term recurrence `p_n = a_n p_{n−1} + p_{n−2}` (same for `q`), seeded `(1, 0)` / `(0, 1)`.

```python
def convergents(digits):
    p, p_prev, q, q_prev = digits[0], 1, 1, 0
    out = [(p, q)]
    for a in digits[1:]:
        p, p_prev = a*p + p_prev, p
        q, q_prev = a*q + q_prev, q
        out.append((p, q))
    return out
```

```
>>> convergents([1]*8)          # phi
[(1, 1), (2, 1), (3, 2), (5, 3), (8, 5), (13, 8), (21, 13), (34, 21)]
>>> convergents([2]*7)          # 1 + sqrt(2)
[(2, 1), (5, 2), (12, 5), (29, 12), (70, 29), (169, 70), (408, 169)]
>>> [p - q for p, q in convergents([2]*8)]     # numerators of sqrt(2) = A001333
[1, 3, 7, 17, 41, 99, 239, 577]
```

Meaning: with every digit equal to `a`, the numerators and denominators are one sequence shifted by one step, `p_n = q_{n+1}`, so each metallic mean of [[metallic-means](pages/metallic-means.md)] has one OEIS entry for both. The numerators `p_n − q_n` of the convergents to `√2` are the Pell-Lucas numbers A001333.


### `order_mod(a, c, p)` / `period_mod(a, p)` → int

`order_mod` is the order of `t` in `F_p[t]/(t² − a t + c)`, and `period_mod` the period of `x_n = a x_{n−1} + x_{n−2}` mod `p`, which is the order of `t` for `c = −1`. When `p` does not divide the discriminant, the order of `t` is the lcm of the orders of the two roots ([[mod-p-observatory](pages/mod-p-observatory.md)]). At an inert prime the two conjugate roots have the same order; at a split prime they can differ (`a = 1`, `p = 11`: the roots `8` and `4` have orders 10 and 5).

```python
def order_mod(a, c, p):
    def mul(u, v):
        (u0, u1), (v0, v1) = u, v            # u0 + u1 t, with t^2 = a t - c
        return ((u0*v0 - c*u1*v1) % p, (u0*v1 + u1*v0 + a*u1*v1) % p)
    cur, e = (0, 1), 1
    while cur != (1, 0):
        cur, e = mul(cur, (0, 1)), e + 1
    return e

def period_mod(a, p):
    s, n = (0, 1), 0
    while True:
        s, n = (s[1], (a*s[1] + s[0]) % p), n + 1
        if s == (0, 1):
            return n
```

```
>>> [(p, order_mod(1, -1, p), period_mod(1, p)) for p in (3, 7, 11, 13, 19)]   # Fibonacci
[(3, 8, 8), (7, 16, 16), (11, 10, 10), (13, 28, 28), (19, 18, 18)]
>>> [(p, order_mod(3, 1, p)) for p in (3, 7, 13)]                               # control: phi^2, norm +1
[(3, 4), (7, 8), (13, 14)]
```

Meaning: at a prime `p` inert in `Q(√5)`, the Frobenius map `u ↦ u^p` sends `φ` to its conjugate, so `φ^{p+1} = φφ̄ = −1`; the order of `φ` divides `2(p + 1)` and not `p + 1`, while `φ²`, of norm `+1`, has order dividing `p + 1`. At the inert primes 3, 7 and 13 the orders are exactly `2(p + 1) = 8, 16, 28` and `p + 1 = 4, 8, 14`.


### `P_table(max_k, max_L)` → `P[k][L]`

The signed tower count of [[castle-sign](pages/castle-sign.md)] as a table, in exact integers, with `P[k][0] = 1` for the empty towers. The row `L = 4` is `(−1)^k A352116(k + 1)`, used by `quasi_split`.

```python
def P_table(max_k, max_L):
    P = [[0]*(max_L+1) for _ in range(max_k+1)]
    for k in range(max_k+1):
        F = [1] + [0]*k; P[k][0] = 1
        for L in range(1, max_L+1):
            F = [sum(F[a]*(1 if a <= b else (-1)**(a-b)) for a in range(k+1)) for b in range(k+1)]
            P[k][L] = sum(F[b]*(-1)**b for b in range(k+1))
    return P
```

```
>>> P = P_table(9, 4)
>>> [P[k][4] for k in range(10)]
[1, -4, 19, -40, 85, -140, 231, -336, 489, -660]
>>> [P[1][L] for L in range(11)]          # Re((1+i)^(L+1)) = A146559(L+1)
[1, 0, -2, -4, -4, 0, 8, 16, 16, 0, -32]
```


### `berlekamp_massey(s)` → the shortest recurrence over the rationals

The Berlekamp-Massey algorithm with exact rational coefficients; `bm_modp` on [[castle-snippets-cryptography](pages/castle-snippets-cryptography.md)] is the version mod `p`. It returns the connection polynomial, coefficients from low to high with `C[0] = 1`, and its order; the output is the shortest recurrence when the order is at most half the number of terms ([[berlekamp-massey](pages/berlekamp-massey.md)]). [[castle-eigenvalue-oeis-crosswalk](pages/castle-eigenvalue-oeis-crosswalk.md)] Part 3 runs it on `P(·, L)` and finds `(x+1)^L (x−1)^{L−2}` for `4 ≤ L ≤ 12`.

```python
from fractions import Fraction
def berlekamp_massey(s):
    s = [Fraction(v) for v in s]
    C, B, L, m, b = [Fraction(1)], [Fraction(1)], 0, 1, Fraction(1)
    for N in range(len(s)):
        d = s[N] + sum(C[i]*s[N-i] for i in range(1, L+1))
        if d == 0: m += 1; continue
        T = C[:]; C += [Fraction(0)]*max(0, len(B)+m-len(C))
        for j in range(len(B)): C[j+m] -= (d/b)*B[j]
        if 2*L <= N: L, B, b, m = N+1-L, T, d, 1
        else: m += 1
    return C[:L+1], L
```

```
>>> berlekamp_massey([1, 1, 3, 9, 19, 33, 59, 121, 259, 529])   # P(2, L)
([Fraction(1, 1), Fraction(-3, 1), Fraction(4, 1), Fraction(-4, 1)], 3)
```

Meaning: the coefficients `[1, −3, 4, −4]` give `char_2 = x³ − 3x² + 4x − 4`, recovered from ten terms, enough since the order 3 is at most half of 10. [[castle-cryptography](pages/castle-cryptography.md)] uses the same recovery against a linear-feedback shift register.


### `quasi_split(seq, deg)` → `(A, B)` with `seq[k] = (−1)^k A(k) + B(k)`

Two Lagrange interpolations, one through the even `k` and one through the odd `k`. They suffice when every eigenvalue of the recurrence is `±1`, which holds in the `k` direction of `P` for `L ≤ 12` (computed; [[castle-eigenvalue-oeis-crosswalk](pages/castle-eigenvalue-oeis-crosswalk.md)]). Requires SymPy.

```python
import sympy as sp
k = sp.symbols('k')

def quasi_split(seq, deg):
    E = sp.interpolate([(kk, seq[kk]) for kk in range(0, 2*deg+2, 2)], k)   # A + B on even k
    O = sp.interpolate([(kk, seq[kk]) for kk in range(1, 2*deg+3, 2)], k)   # B - A on odd k
    return sp.factor((E - O)/2), sp.factor((E + O)/2)
```

```
>>> P = P_table(40, 6)
>>> quasi_split([P[kk][4] for kk in range(41)], 3)
((k + 1)*(2*k + 1)*(2*k + 3)/6, (k + 1)/2)
>>> quasi_split([P[kk][5] for kk in range(41)], 4)
(k*(k + 1)**2*(k + 2)/3, (k + 1)**2)
```

Meaning: `P(k, 4) = (−1)^k (k+1)(2k+1)(2k+3)/6 + (k+1)/2` for every `k ≤ 40` (checked), and `|P(k, 4)| = A352116(k + 1)`, the partial sums of the odd triangular numbers. `deg` must be at least the true degree, `L − 1` here; with less, the interpolation returns a wrong polynomial without warning, so the result is checked against the sequence.


### `M_signed(k)` / `sectors(k, Lmax)` → transfer matrix and last-column-parity sectors

The signed transfer matrix `M̃_k`, with entry `(−1)^{max(0, a−b)}` from height `a` to height `b`, and the split `P = P_even + P_odd` by the parity of the height of the last column ([[tower-parity-sectors](pages/tower-parity-sectors.md)]). Requires SymPy.

```python
def M_signed(k):                       # M~_k[a][b] = (-1)^max(0, a-b)
    return sp.Matrix(k+1, k+1, lambda a, b: 1 if a <= b else (-1)**(a-b))

def sectors(k, Lmax):
    M = M_signed(k); row = sp.Matrix([[1]+[0]*k])
    ve = sp.Matrix([1 if b % 2 == 0 else 0 for b in range(k+1)]); vo = sp.Matrix([(-1)**b if b % 2 else 0 for b in range(k+1)])
    E, O = [], []
    for L in range(Lmax+1):
        E.append(int((row*ve)[0])); O.append(int((row*vo)[0])); row = row*M
    return E, O
```

```
>>> sp.factor(M_signed(6).charpoly(sp.Symbol('lam')).as_expr())
(lam**3 - 4*lam**2 + 4*lam - 8)*(lam**4 - 3*lam**3 + 8*lam**2 - 4*lam + 8)
>>> E, O = sectors(6, 9); E, O
([1, 4, 16, 56, 192, 672, 2368, 8320, 29184, 102400], [0, -3, -9, -7, 39, 161, 215, -431, -2681, -5023])
>>> [e // 2**L for L, e in enumerate(E)]          # = A005251(L+3): (L+1)-bit strings with no isolated 1
[1, 2, 4, 7, 12, 21, 37, 65, 114, 200]
>>> sectors(1, 8)                                  # Re((1+i)^L) and -Im((1+i)^L)
([1, 1, 0, -2, -4, -4, 0, 8, 16], [0, -1, -2, -2, 0, 4, 8, 8, 0])
```

Meaning: `E[L] + O[L] = P(k, L)`; for even `k` the two sequences satisfy the recurrences whose characteristic polynomials are the two factors of `char_k`. For even `k ≤ 20` and `L ≤ 20`, `E[L]/2^L` is an integer exactly when `k ≡ 2 (mod 4)` (computed).


### `H(d)` → the monic factor of `char_{2d}(2μ)/2^{2d}`

Requires SymPy. Preamble: build the characteristic polynomials `c[k] = char_k(λ)` from the gallery recurrence `char_{k+1} = λ²·char_{k−1} − 2·char_k` ([[generating-function-gallery](pages/generating-function-gallery.md)]).

```python
from math import comb
import sympy as sp
lam, mu = sp.symbols('lam mu')
c = [lam - 1, lam**2 - 2*lam + 2]                          # c[0] = char_0, c[1] = char_1
for k in range(2, 8):
    c.append(sp.expand(lam**2 * c[k-2] - 2*c[k-1]))         # c[k] = char_k

def H(d):
    return sp.Poly(sum((-1)**i * comb((d+i)//2, i) * mu**(d-i) for i in range(d+1)), mu)
```

```
>>> [H(d).as_expr() for d in range(1, 5)]
[mu - 1, mu**2 - mu + 1, mu**3 - 2*mu**2 + mu - 1, mu**4 - 2*mu**3 + 3*mu**2 - mu + 1]
>>> g6 = sp.Poly(sp.expand(c[6].subs(lam, 2*mu)/2**6), mu)          # c[6] = char_6 from the gallery recurrence
>>> (g6 - H(3)*sp.Poly(H(4).as_expr() + mu**2*H(2).as_expr(), mu)).is_zero
True
```

Meaning: `H_3` is the minimal polynomial of `ψ²`, the square of the plastic number, so `ρ_6 = 2ψ²` ([[plastic-number](pages/plastic-number.md)]); the identity `g_{2d} = H_d·(H_{d+1} + μ² H_{d−1})`, with `g_{2d}(μ) = char_{2d}(2μ)/2^{2d}`, is proved for every `d` on [[tower-parity-sectors](pages/tower-parity-sectors.md)].


### `cf_digits(poly, x0, n)` → the simple continued fraction of an algebraic number

The digits of a real algebraic number by repeated floor and reciprocal, at `mpmath` precision. A real number has an eventually periodic continued fraction exactly when it is a quadratic irrational (Lagrange; [[eigenvalue-continued-fractions](pages/eigenvalue-continued-fractions.md)]), so the digits of a cubic never become periodic; Part 4 of [[castle-eigenvalue-oeis-crosswalk](pages/castle-eigenvalue-oeis-crosswalk.md)] uses this for `ρ_6`. Requires mpmath.

```python
from mpmath import mp, mpf, findroot, floor
mp.dps = 200
def cf_digits(poly_coeffs, x0, n=20):
    r = findroot(lambda t: sum(cc*t**(len(poly_coeffs)-1-i) for i, cc in enumerate(poly_coeffs)), mpf(x0))
    digs, t = [], r
    for _ in range(n):
        a = int(floor(t)); digs.append(a); t = 1/(t - a)
    return digs
```

```
>>> cf_digits([1, -3, 2, -4], 2.8)        # rho_4
[2, 1, 3, 1, 10, 13, 3, 2, 1, 30, 1, 12, 1, 1, 36, 1, 11, 10, 1, 21]
>>> cf_digits([1, -4, 4, -8], 3.5)        # rho_6 = 2 psi^2
[3, 1, 1, 25, 7, 1, 6, 1, 8, 1, 282, 40, 4, 2, 1, 5, 4, 5, 8, 1]
>>> cf_digits([1, -2, -1], 2.4, 8)        # 1 + sqrt(2), for contrast
[2, 2, 2, 2, 2, 2, 2, 2]
```

Meaning: `ρ_4` and `ρ_6` are cubic, so their digits are not eventually periodic; the quadratic `1 + √2` is `[2; 2, 2, …]`.


### `jacobi_perron(f, x0, steps)` → the multidimensional continued fraction, exactly

The Jacobi-Perron algorithm, a continued fraction in `d − 1` dimensions for an algebraic number of degree `d`, with exact arithmetic in `Q(ρ)` (reduction and inversion modulo the minimal polynomial; mpmath only for the floors), so a repeated state is detected exactly. Requires SymPy and mpmath.

```python
import sympy as sp
from mpmath import mp, mpf, findroot, floor
lam = sp.Symbol('lam'); mp.dps = 200
def jacobi_perron(f, x0, steps):
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
>>> jacobi_perron(lam**3 - 4*lam**2 + 4*lam - 8, 3.5, 40)      # rho_6 = 2 psi^2
([[3, 12], [0, 1], [1, 1], [1, 1], [7, 8], [1, 1], [1, 1], [1, 1], [5, 9]], 'periodic: preperiod 5, period 4')
>>> jacobi_perron(lam**3 - 3*lam**2 + 2*lam - 4, 2.8, 400)[1]  # rho_4
'no period within 400 steps'
```

Meaning: the Jacobi-Perron expansion of `ρ_6` has preperiod 5 and period 4, and that of `ρ_4` shows no period in 400 exact steps. `ρ_6/2 = ψ²` is a unit, and `ρ_4/2`, a root of `2μ³ − 3μ² + μ − 1`, is not an algebraic integer ([[castle-eigenvalue-oeis-crosswalk](pages/castle-eigenvalue-oeis-crosswalk.md)]).

## Ring theory of `char_k`

Snippets behind [[chinese-remainder-theorem](pages/chinese-remainder-theorem.md)], [[idempotent-decomposition](pages/idempotent-decomposition.md)], [[char-k-eisenstein-at-two](pages/char-k-eisenstein-at-two.md)] and the mod-2 note on [[castle-ring-invariant-factors](pages/castle-ring-invariant-factors.md)] and [[castle-ring-spectrum](pages/castle-ring-spectrum.md)], following Chapters 17, 14, 13, 12, 5 and 4 of [[calugareanu-hamburg-exercises-basic-ring-theory](pages/calugareanu-hamburg-exercises-basic-ring-theory.md)]. All need SymPy.

```python
import sympy as sp
x = sp.symbols('x')
```

### `char_k(k)` → the characteristic polynomial of `P(k, ·)`, and its shape mod 2

The three-term recurrence `char_{k+1} = x²·char_{k−1} − 2·char_k` from `char_0 = x − 1`, `char_1 = x² − 2x + 2`. Mod 2 the `−2·char_k` term drops out, which proves the shape of the output.

```python
def char_k(k):
    a, b = x - 1, x**2 - 2*x + 2
    for _ in range(k):
        a, b = b, sp.expand(x**2*a - 2*b)
    return a
```

```
>>> [sp.Poly(char_k(k), x, modulus=2).as_expr() for k in range(1, 7)]
[x**2, x**3 + x**2, x**4, x**5 + x**4, x**6, x**7 + x**6]
```

Meaning: `char_k ≡ x^{k+1}` (odd `k`) or `x^k(x + 1)` (even `k`) mod 2, so `x` is never a unit of `F_2[x]/(char_k)`, and the mod-`p` pages start at `p = 3`.

### `crt_idempotents(Q, p)` → the primitive idempotents of `F_p[x]/(Q)`

One per distinct irreducible factor `g^m` of `Q mod p`: `N · (N^{−1} mod g^m)` with `N = Q/g^m`, which is `1` on that CRT factor and `0` on the others.

```python
def crt_idempotents(Q, p):
    F = sp.Poly(Q, x, modulus=p)
    mods = [g**m for g, m in sp.factor_list(F)[1]]
    out = []
    for i, Mi in enumerate(mods):
        Ni = sp.prod([mods[j] for j in range(len(mods)) if j != i]) if len(mods) > 1 else sp.Poly(1, x, modulus=p)
        inv = sp.invert(Ni.as_expr(), Mi.as_expr(), x, modulus=p) if len(mods) > 1 else 1
        out.append(sp.Poly(Ni.as_expr() * inv, x, modulus=p).rem(F))
    return out
```

```
>>> E = crt_idempotents(char_k(2), 101); F = sp.Poly(char_k(2), x, modulus=101)
>>> [e.as_expr() for e in E]
[-25*x**2 + 25*x - 50, 25*x**2 - 25*x - 50]
>>> [(e*e - e).rem(F).is_zero for e in E], (E[0]*E[1]).rem(F).is_zero, (E[0] + E[1]).rem(F).as_expr()
([True, True], True, 1)
>>> len(crt_idempotents(char_k(3), 3)), len(crt_idempotents(char_k(3), 5))
(1, 2)
```

Meaning: at `k = 2`, `p = 101` the first idempotent is `(x² − x + 2)/4 ≡ 76x² + 25x + 51`, the projector onto the dominant eigenvalue `2`. `char_3` is irreducible mod 3 (a field, only the idempotent `1`) and has two distinct factors mod 5 (`(x − 1)²` and a quadratic).

### `lagrange_idempotents(p)` → the indicator polynomials of `F_p`

`δ_a = 1 − (x − a)^{p−1}` is `1` at `a` and `0` at every other point (Fermat), so the `δ_a` are the primitive idempotents of `F_p[x]/(x^p − x)`, the ring of all functions `F_p → F_p`.

```python
def lagrange_idempotents(p):
    return [sp.Poly(1 - (x - a)**(p - 1), x, modulus=p) for a in range(p)]
```

```
>>> [[int(d.eval(b)) % 5 for b in range(5)] for d in lagrange_idempotents(5)]
[[1, 0, 0, 0, 0], [0, 1, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 1, 0], [0, 0, 0, 0, 1]]
>>> f, g = sp.Poly(x**5 + x**3 + x, x, modulus=3), sp.Poly(x**5 + 2*x, x, modulus=3)
>>> f == g, [int((f - g).eval(b)) % 3 for b in range(3)], (f - g).rem(sp.Poly(x**3 - x, x, modulus=3)).as_expr()
(False, [0, 0, 0], 0)
```

Meaning: the second line is exercise 14.10 - two different polynomials, one function, because their difference is a multiple of `x^3 − x`.

### `sector_resultant(k)` → the resultant of the two parity-sector factors (even `k`)

```python
def sector_resultant(k):
    (f, _), (g, _) = sp.factor_list(char_k(k))[1]
    return sp.resultant(f, g, x)
```

```
>>> [(k, sp.factorint(sector_resultant(k))) for k in range(2, 13, 2)]
[(2, {2: 2}), (4, {2: 6}), (6, {2: 12}), (8, {2: 20}), (10, {2: 30}), (12, {2: 42})]
>>> all(sector_resultant(k) == 2**(k*(k+2)//4) for k in range(2, 31, 2))
True
```

Meaning: the resultant is `2^{k(k+2)/4} = 2^{d(d+1)}` for even `k = 2d ≤ 30` (computed), so for these `k` the two sector factors have a common root only modulo 2, and the parity-sector split of `Q[x]/(char_k)` is defined over `Z[1/2]`.

### `x_order(Q, p)` / `reduced_period(k, p)` → the period of `P(k, ·) mod p`, split into reduced part and nilpotent inflation

`x_order` is the multiplicative order of `x` in `F_p[x]/(Q)` (odd `p`, so `x` is a unit): start from the unit-group order `∏ (p^d − 1)·p^{d(m−1)}` and strip prime factors. `reduced_period` computes it twice, for `char_k` and for its radical (the product of the distinct factors, i.e. the ring modulo its nilradical), and reports the inflation `p^⌈log_p m⌉` for the largest multiplicity `m`.

```python
def x_order(Q, p):
    F = sp.Poly(Q, x, modulus=p)
    fl = sp.factor_list(F)[1]
    N = 1
    for g, m in fl:
        N *= (p**g.degree() - 1) * p**(g.degree()*(m - 1))
    one = sp.Poly(1, x, modulus=p)
    def pow_mod(e):
        r, b = one, sp.Poly(x, x, modulus=p)
        while e:
            if e & 1: r = (r*b).rem(F)
            b, e = (b*b).rem(F), e >> 1
        return r
    o = N
    for q in sp.factorint(N):
        while o % q == 0 and pow_mod(o // q) == one:
            o //= q
    return o

def reduced_period(k, p):
    fl = sp.factor_list(sp.Poly(char_k(k), x, modulus=p))[1]
    rad = sp.prod([g for g, _ in fl]).as_expr()
    m, e = max(m for _, m in fl), 0
    while p**e < m:
        e += 1
    return x_order(rad, p), p**e, x_order(char_k(k), p)
```

```
>>> [reduced_period(k, p) for k, p in [(2, 7), (3, 5), (4, 3), (6, 23)]]
[(3, 7, 21), (24, 5, 120), (13, 3, 39), (264, 23, 6072)]
>>> reduced_period(2, 5)                      # squarefree mod 5: no nilradical, no inflation
(24, 1, 24)
```

Meaning: in each case shown the full period is the reduced period times `p^⌈log_p m⌉` - the nilradical of `F_p[x]/(char_k)` accounts for exactly the extra `p`.

### `sectors_mod2(k)` → the two parity-sector factors of `char_k` (even `k`), reduced mod 2

```python
def sectors_mod2(k):
    return [sp.Poly(f, x, modulus=2).as_expr() for f, _ in sp.factor_list(char_k(k))[1]]
```

```
>>> [sectors_mod2(k) for k in (2, 4, 6)]
[[x, x**2 + x], [x**2, x**3 + x**2], [x**3, x**4 + x**3]]
```

Meaning: the factors reduce to `x^{k/2}` and `x^{k/2}(x + 1)`, so the two sector components of `Spec Z[x]/(char_k)` meet over 2 only at the point `(2, x)`, and, by the resultant, over no other prime (for even `k ≤ 30`).

### `sector_idempotent(k)` → the rational idempotent that splits the two parity sectors (even `k`), and the power of 2 in its denominator

Over `Q`, the element that is `1` on the `f`-sector and `0` on the `g`-sector is `g·(g^{−1} mod f)`, reduced mod `char_k`. Its coefficients are fractions, and the function returns the exponent of 2 in the lcm of their denominators; for even `k ≤ 40` no other prime divides them (computed).

```python
def sector_idempotent(k):
    (f, _), (g, _) = sp.factor_list(char_k(k))[1]
    e = sp.rem(sp.expand(g * sp.invert(g, f, x)), char_k(k), x)
    den = sp.ilcm(*[sp.fraction(c)[1] for c in sp.Poly(e, x).all_coeffs()])
    return e, sp.multiplicity(2, den)
```

```
>>> sector_idempotent(2)
(x**2/4 - x/4 + 1/2, 2)
>>> [sector_idempotent(k)[1] for k in range(2, 21, 2)]
[2, 4, 5, 8, 9, 11, 12, 16, 17, 19]
>>> all(sector_idempotent(k)[1] == sp.multiplicity(2, sp.factorial(k)) + 1 for k in range(2, 41, 2))
True
```

Meaning: at `k = 2` the idempotent is `(x² − x + 2)/4`, the same element whose reduction mod 101 is `76x² + 25x + 51` in `crt_idempotents`. The denominator is `2^{v_2(k!) + 1}` for every even `k ≤ 40` (computed), so the idempotent lies in `Z[1/2][x]/(char_k)` and not in `Z[x]/(char_k)`.

### `fiber_ideal_count(k, p)` → `(ideals, idempotents)` of the fiber `F_p[x]/(char_k mod p)`

Ideals of `F_p[x]/(Q)` correspond to monic divisors of `Q`, so there are `∏ (m_i + 1)` of them; idempotents correspond to subsets of the distinct factors, so there are `2^r`. The two counts agree exactly when every `m_i = 1`, i.e. when the fiber is semisimple.

```python
from math import prod
def fiber_ideal_count(k, p):
    fl = sp.factor_list(sp.Poly(char_k(k), x, modulus=p))[1]
    return prod(m + 1 for _, m in fl), 2**len(fl)
```

```
>>> [(k, p, fiber_ideal_count(k, p)) for k, p in [(2, 5), (2, 7), (3, 5), (4, 3)]]
[(2, 5, (4, 4)), (2, 7, (6, 4)), (3, 5, (6, 4)), (4, 3, (6, 4))]
```

Meaning: `char_2 mod 5` is squarefree (semisimple fiber, 4 ideals, all generated by idempotents); `char_2 mod 7`, `char_3 mod 5`, `char_4 mod 3` are fat (6 ideals, only 4 idempotents). In `char_2 mod 7 = (x − 2)(x + 3)²` the two extra ideals are `(x + 3)` and `(x − 2)(x + 3)`: they cut partway into the fat factor `(x + 3)²`, so no idempotent generates them.

### `frobenius_profile(k, p)` → `(rank of a ↦ a^p, dim of {a : a^p = a})` on the fiber `F_p[x]/(char_k mod p)`

On a ring of characteristic `p`, `a ↦ a^p` is additive and fixes `F_p`, so it is an `F_p`-linear map of the fiber (a `(k+1) × (k+1)` matrix whose `j`-th column is `x^{jp} mod char_k`). Its rank drops exactly on fat fibers, and its fixed space `{a : a^p = a}` has dimension `r`, the number of distinct irreducible factors - the Berlekamp count, obtained without factoring.

```python
from sympy.polys.matrices import DomainMatrix

def frobenius_profile(k, p):
    F = sp.Poly(char_k(k), x, modulus=p)
    n = F.degree()
    cols = []
    for j in range(n):
        v = [int(c) % p for c in sp.Poly(x**(j*p), x, modulus=p).rem(F).all_coeffs()[::-1]]
        cols.append(v + [0]*(n - len(v)))
    M = sp.Matrix(n, n, lambda i, j: cols[j][i])
    rank = lambda A: DomainMatrix.from_Matrix(A).convert_to(sp.GF(p)).rank()
    return rank(M), n - rank(M - sp.eye(n))
```

```
>>> [(k, p, frobenius_profile(k, p)) for k, p in [(2, 5), (2, 7), (4, 5), (6, 3)]]
[(2, 5, (3, 2)), (2, 7, (2, 2)), (4, 5, (5, 3)), (6, 3, (6, 3))]
>>> frobenius_profile(5, 3)                   # char_5 irreducible mod 3: full rank, fixed space = F_3
(6, 1)
```

Meaning: `char_2 mod 5` is squarefree (rank 3 = full) with 2 points; `char_2 mod 7 = (x − 2)(x + 3)²` is fat (rank 2 < 3, the missing dimension is the nilpotent `(x − 2)(x + 3)`) and still has 2 points; `char_4 mod 5` has 3 points, `char_6 mod 3` is fat with 3 points. The rank is `Σ d_i ⌈m_i/p⌉` in all 12 fibers checked on [[castle-ring-spectrum](pages/castle-ring-spectrum.md)] §6.

### `metallic_ring(a)` → `(D0, f)`: the ring `Z[δ_a] = Z[x]/(x² − a x − 1)` as an order of conductor `f` in the field of fundamental discriminant `D0`

`disc(x² − a x − 1) = a² + 4 = f² · D0`. The rung generates the full ring of integers of `Q(√(a²+4))` exactly when `f = 1`.

```python
def metallic_ring(a):
    D, f = a*a + 4, 1
    for q, e in sp.factorint(D).items():
        f *= q**(e // 2)
    D0 = D // (f*f)
    if D0 % 4 in (2, 3):
        D0, f = 4*D0, f // 2
    return D0, f
```

```
>>> [(a, metallic_ring(a)) for a in (1, 2, 3, 4, 8, 11, 14)]
[(1, (5, 1)), (2, (8, 1)), (3, (13, 1)), (4, (5, 2)), (8, (17, 2)), (11, (5, 5)), (14, (8, 5))]
```

Meaning: golden, silver, bronze generate full rings of integers; `δ_4 = φ³` generates `Z[√5]`, index 2 in `Z[φ]`; `a = 11` (`= φ⁵`) and `a = 14` (`= (1 + √2)³`) have index 5, the Fibonacci and Pell numbers `F_5` and `P⋆_3`; `a = 8` has index 2 without being a power of a smaller rung.

### `x_inverse(k)` → `(h, c)` with `x · h(x) = c = ±2^k` in `Z[x]/(char_k)`

Since `char_k(x) = 0`, moving the constant term across gives `x · h(x) = −char_k(0) = ±2^k`. So `x^{−1} = h(x)/c`: a unit in every fiber over an odd prime, but not in `Z[x]/(char_k)`, where the inverse needs `1/2^k`.

```python
def x_inverse(k):
    c = -char_k(k).subs(x, 0)
    return sp.expand((char_k(k) + c) / x), c
```

```
>>> [x_inverse(k) for k in (1, 2, 3)]
[(x - 2, -2), (x**2 - 3*x + 4, 4), (x**3 - 4*x**2 + 8*x - 8, -8)]
```

## Appearances in Sources

- [[project-euler-502-brute-force](pages/project-euler-502-brute-force.md)] - the reference `p_signed` DP.
- [[calugareanu-hamburg-exercises-basic-ring-theory](pages/calugareanu-hamburg-exercises-basic-ring-theory.md)] - Chapters 17 and 14, the ring theory the `char_k` snippets implement (CRT 17.20, idempotents 17.19, Lagrange 17.13 and 14.10, `Z[X]/(2, X)` 14.13).

## Related Concepts

- [[castle-snippets](pages/castle-snippets.md)] - the enumeration and predicates hub.
- [[castle-eigenvalue-oeis-crosswalk](pages/castle-eigenvalue-oeis-crosswalk.md)] - the convergents, quasi-polynomials and continued fractions of the castle eigenvalues, computed with these snippets.
- [[eigenvalue-continued-fractions](pages/eigenvalue-continued-fractions.md)] - the real side of the CF-period / mod-p-order correspondence.
- [[mod-p-observatory](pages/mod-p-observatory.md)] - the finite-field side.
- [[metallic-means](pages/metallic-means.md)] / [[pell-numbers](pages/pell-numbers.md)] - the metallic means of `convergents` and `metallic_ring`, and the Pell and Pell-Lucas numbers.
- [[recurrence-discovery](pages/recurrence-discovery.md)] / [[closed-form-hunting](pages/closed-form-hunting.md)] - the recurrence orders of `P` in both directions and the closed forms `quasi_split` finds.
- [[signed-tower-count](pages/signed-tower-count.md)] / [[tower-parity-sectors](pages/tower-parity-sectors.md)] / [[plastic-number](pages/plastic-number.md)] - `P(k, L)`, `M̃_k` and its sectors, and `H_d` with the plastic root of `char_6`.
- [[castle-sign](pages/castle-sign.md)] - the block-count convention `p_signed` matches.
- [[chinese-remainder-theorem](pages/chinese-remainder-theorem.md)] / [[idempotent-decomposition](pages/idempotent-decomposition.md)] - `crt_idempotents`, `lagrange_idempotents`, `sector_resultant`.
- [[char-k-eisenstein-at-two](pages/char-k-eisenstein-at-two.md)] - `char_k` and its mod-2 shape.
- [[castle-ring-spectrum](pages/castle-ring-spectrum.md)] - `reduced_period`, `sectors_mod2`, `sector_idempotent`, `fiber_ideal_count`, `frobenius_profile`, `x_inverse`.

## Footnotes

[^1]: Verified by execution (Python 3.11 with SymPy 1.14 and mpmath, 2026-10-16): every printed output on this page; `P_table` against `p_signed` for `k ≤ 6`, `L ≤ 8`; the split of `P(k, 4)` against the table for `k ≤ 40`; `E[L]/2^L` for even `k ≤ 20`, `L ≤ 20`; the roots `4, 8` of `t² − t − 1` mod 11 and their orders 5 and 10; the sector-idempotent denominators for even `k ≤ 40`; `char_3` irreducible mod 3 and `(x − 1)²` times a quadratic mod 5; `char_2 ≡ (x − 2)(x + 3)²` mod 7.
