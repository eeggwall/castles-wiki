---
title: Castle snippets - number theory
category: Concepts
summary: Snippets for the signed tower count, continued-fraction convergents, mod-p orders / Pisano-type periods, quasi-polynomial splits, sector transfer matrices, and the H(d) factor. Sibling of the core castle-snippets hub.
tags: [concept, castle, python, snippets, signed-tower-count, continued-fraction, mod-p, quasi-polynomial, plastic-number]
sources: [project-euler-502-brute-force]
created: 2026-09-19
updated: 2026-09-19
---

# Castle snippets - number theory

A sibling page to [[castle-snippets](pages/castle-snippets.md)]: snippets that compute the signed tower count `P(k, L)`, continued-fraction convergents, Pisano-type periods, quasi-polynomial splits, and the Hilbert factor `H(d)` behind the plastic-eigenvalue identity. Same conventions as the hub page - every output pinned, every snippet executed during ingest.

## The signed tower count

### `p_signed(k, L)` → the signed tower count P(k,L)

The signed sum `Σ (−1)^blocks` over towers of height `≤ k` above a length-`L` block, by an `O(k²L)` last-column-height DP ([[signed-tower-count](pages/signed-tower-count.md)]). A new column of height `b` after height `a` opens `max(0, b−a)` new blocks, each weighted `−1`.

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
>>> [p_signed(1, L) for L in range(8)]        # Re((1+i)^{L+1}) = A146559
[1, 0, -2, -4, -4, 0, 8, 16]
>>> [p_signed(2, L) for L in range(10)]       # order-3, all positive; novel (no OEIS match)
[1, 1, 3, 9, 19, 33, 59, 121, 259, 529]
>>> [p_signed(4, L) for L in range(9)]        # order-5; novel
[1, 1, 5, 25, 85, 225, 541, 1385, 3973]
```

Meaning: `P(k,·)` is C-finite of order `k+1`, and the whole family's generating-function denominators satisfy `den_{k+1} = den_{k−1} − 2x·den_k`, whose roots `−x ± √(x²+1)` give the Pell/Chebyshev closed form on [[generating-function-gallery](pages/generating-function-gallery.md)]. Even-`k` rows are all-positive (the clean new-sequence candidates); odd-`k` rows alternate in sign.


## Continued fractions, convergents, and quasi-polynomials

Snippets behind [[castle-eigenvalue-oeis-crosswalk](pages/castle-eigenvalue-oeis-crosswalk.md)] and [[eigenvalue-continued-fractions](pages/eigenvalue-continued-fractions.md)]. The first three are stdlib-only; `quasi_split` needs SymPy (the one import that earns its keep here).

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

Meaning: with a constant digit `a`, numerators and denominators are the *same* metallic sequence one step apart - one OEIS entry per rung of [[metallic-means](pages/metallic-means.md)], not two.


### `order_mod(a, c, p)` / `period_mod(a, p)` → int

The order of the root of `t² − a t + c` in `F_p[t]/(t² − a t + c)` (a hand-built `F_p` or `F_{p²}`), and the Pisano-type period of `x_n = a x_{n−1} + x_{n−2}` mod `p`. They agree - the period *is* the eigenvalue order ([[mod-p-observatory](pages/mod-p-observatory.md)]).

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

Meaning: at inert primes (`3, 7, 13` for `√5`) the norm-`−1` golden ratio has order `2(p+1)` - `8, 16, 28` - while the norm-`+1` `φ²` has order `p+1` - `4, 8, 14`. The `−1` that makes `φ`'s continued fraction purely periodic is the `−1` in `φ^{p+1} = −1`.


### `P_table(max_k, max_L)` → `P[k][L]`

The [[castle-sign](pages/castle-sign.md)] signed tower count as a compact DP (exact integers; `P[k][0] = 1` for the empty tower).

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

Berlekamp–Massey with exact rational coefficients (the mod-`p` cousin is `bm_modp` in the cryptography snippets). Given a sequence, returns the connection polynomial (low→high, `C[0] = 1`) and its order. Over `Q` this is exact — [[convergents-oeis-crosswalk](pages/convergents-oeis-crosswalk.md)] Part 3 runs it on `P(·, L)` to recover `(x+1)^L (x−1)^{L−2}`.

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

Meaning: the coefficients `[1, −3, 4, −4]` are `char_2 = x³ − 3x² + 4x − 4`, recovered from ten terms — the castle's whole identity from its output (the LFSR attack of [[castle-cryptography](pages/castle-cryptography.md)]).


### `quasi_split(seq, deg)` → `(A, B)` with `seq[k] = (−1)^k A(k) + B(k)`

Two Lagrange interpolations (even `k`, odd `k`) - all you need when every eigenvalue is `±1`, which is the case for the k-direction of `P` ([[castle-eigenvalue-oeis-crosswalk](pages/castle-eigenvalue-oeis-crosswalk.md)]). Requires SymPy.

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

Meaning: `P(k,4) = (−1)^k (k+1)(2k+1)(2k+3)/6 + (k+1)/2`, and `|P(k,4)|` is A352116 (partial sums of odd triangular numbers). Always give `deg` at least the true degree (`L−1` here); with too few terms the interpolation silently returns garbage - re-check against the sequence, as the crosswalk page does.


### `M_signed(k)` / `sectors(k, Lmax)` → transfer matrix and last-column-parity sectors

The signed transfer matrix of [[signed-tower-count](pages/signed-tower-count.md)] and the split `P = P_even + P_odd` by the parity of the last column height ([[tower-parity-sectors](pages/tower-parity-sectors.md)]). Requires SymPy.

```python
def M_signed(k):                       # s(a, b) = (-1)^max(0, a-b)
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

Meaning: `E[L] + O[L] = P(k, L)`; the two sequences are C-finite with the two factors of `char_k` as characteristic polynomials. `E[L]/2^L` is an integer exactly when `k ≡ 2 (mod 4)`.


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

Meaning: `H_3` is the minimal polynomial of `ψ²` (plastic number squared), hence `ρ_6 = 2ψ²` ([[plastic-number](pages/plastic-number.md)]); the identity `g_{2d} = H_d·(H_{d+1} + μ² H_{d−1})` holds for every `d` (proof on [[tower-parity-sectors](pages/tower-parity-sectors.md)]).


### `cf_digits(poly, x0, n)` → the simple continued fraction of an algebraic number

The digit stream of a real algebraic number by repeated `⌊·⌋` and reciprocal, at `mpmath` precision. For a quadratic it repeats (Lagrange); for a cubic it never does, and the digits look random. Part 4 of [[convergents-oeis-crosswalk](pages/convergents-oeis-crosswalk.md)] uses this to show `ρ_6` has no simple-CF period. Requires mpmath.

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

Meaning: the cubic digits (including the `282`) never repeat — eventually-periodic ⟺ quadratic — while the quadratic `1+√2` is all `2`s.


### `jacobi_perron(f, x0, steps)` → the multidimensional continued fraction, exactly

The Jacobi–Perron algorithm (JPA) — the `d`-dimensional continued fraction — on a degree-`d` algebraic number, with exact arithmetic in `Q(ρ)` (reduce and invert mod the minimal polynomial; mpmath only for the floors). Detects periodicity exactly: `ρ_6 = 2ψ²` is JPA-periodic, `ρ_4` is not within 400 steps. Requires SymPy + mpmath.

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

Meaning: `ρ_6` has a period-4 multidimensional continued fraction (the cubic analogue of `[2; 2, 2, …]`), while `ρ_4` shows none in 400 exact steps — the unit/non-unit split: `ρ_6/2 = ψ²` is a unit, `ρ_4/2` is not even an algebraic integer ([[convergents-oeis-crosswalk](pages/convergents-oeis-crosswalk.md)]).


## Appearances in Sources

- [[project-euler-502-brute-force](pages/project-euler-502-brute-force.md)] - the reference `p_signed` DP.

## Related Concepts

- [[castle-snippets](pages/castle-snippets.md)] - the enumeration and predicates hub.
- [[castle-eigenvalue-oeis-crosswalk](pages/castle-eigenvalue-oeis-crosswalk.md)] - the analysis these snippets were written for; every pinned value here matches that page.
- [[eigenvalue-continued-fractions](pages/eigenvalue-continued-fractions.md)] - the real side of the CF-period / mod-p-order twin.
- [[mod-p-observatory](pages/mod-p-observatory.md)] - the finite-field mirror.
- [[metallic-means](pages/metallic-means.md)] / [[pell-numbers](pages/pell-numbers.md)] - the rungs the convergents snippets sit on.
- [[recurrence-discovery](pages/recurrence-discovery.md)] / [[closed-form-hunting](pages/closed-form-hunting.md)] - the recurrence orders and coefficients `quasi_split` factors.
- [[signed-tower-count](pages/signed-tower-count.md)] / [[tower-parity-sectors](pages/tower-parity-sectors.md)] / [[plastic-number](pages/plastic-number.md)] - the `M_signed`, sectors, and `H(d)` snippets.
- [[castle-sign](pages/castle-sign.md)] - the block-count convention `p_signed` matches.
