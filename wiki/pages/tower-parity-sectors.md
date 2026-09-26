---
title: Tower parity sectors - why char_k factors, and where the plastic number comes from
category: Analyses
summary: The signed transfer matrix commutes with "reflect heights, flip signs", so for even k the signed tower count splits by the parity of the last column height, P = P_even + P_odd, and char_k factors accordingly. Rescaled by λ = 2μ the factors are explicit - H_d(μ) = Σ (−1)^i C(⌊(d+i)/2⌋, i) μ^(d−i) and its Lucas companion H_(d+1) + μ² H_(d−1) - a doubling identity proved via Pascal's rule. H_3 is the minimal polynomial of ψ² (plastic), and for k = 4m+2 the even sector is 2^L times Hardin's "every nonzero letter ≤ a neighbor" word counts (A005251, A202882, A203094, A203184).
tags: [analysis, castle, signed-tower-count, transfer-matrix, symmetry, factorization, plastic-number, quasi-polynomial, oeis, hardin, sympy, verification, pedagogy]
sources: [oeis-mining-pe502, project-euler-502-solution, project-euler-502-castle-factoring]
created: 2026-09-16
updated: 2026-09-26
---

# Tower parity sectors - why `char_k` factors, and where the plastic number comes from

## The question

[[generating-function-gallery](pages/generating-function-gallery.md)] observed that `char_k`, the degree-`(k+1)` characteristic polynomial of the signed tower count `P(k, ·)` in the base length `L`, factors into two pieces for even `k` and is irreducible for odd `k`, and [[castle-eigenvalue-oeis-crosswalk](pages/castle-eigenvalue-oeis-crosswalk.md)] found that the `k = 6` dominant eigenvalue is `2ψ²` for `ψ` the [[plastic-number](pages/plastic-number.md)]. This page explains both. The factorization is a symmetry of the transfer matrix; the factors have closed forms; and the closed form for `k = 6` is the minimal polynomial of `ψ²`. Along the way the even-last-column sector of `P(k, L)` turns out to be, for every `k ≡ 2 (mod 4)`, `2^L` times a word count that R. H. Hardin put in OEIS with an "empirical" recurrence - which this page's factors supply.

Everything below was produced by the snippets shown; every printed value is pinned.

## Part 1 - The symmetry

Write the column-height dynamic program (DP) of [[castle-sign](pages/castle-sign.md)] as a matrix. A tower of height `≤ k` on a length-`L` base is a height sequence `c_1, …, c_L ∈ {0, …, k}`, its block count is the total descent with `c_0 = c_{L+1} = 0`,[^3] and the sign `(−1)^{blocks}` factors over consecutive pairs:

```python
def M_signed(k):                       # s(a, b) = (-1)^max(0, a-b): the sign of stepping from height a to height b
    return sp.Matrix(k+1, k+1, lambda a, b: 1 if a <= b else (-1)**(a-b))
```

Then `P(k, L) = e_0ᵀ M_kᴸ v` with `e_0` = "start at height 0" and `v_b = (−1)^b` = "final drop from height `b` to 0". Its characteristic polynomial is the gallery's `char_k`:

```
>>> for k in range(1, 7): print(k, sp.factor(M_signed(k).charpoly(lam).as_expr()) == sp.factor(c[k]))
1 True ... 6 True
```

**The involution.** Let `J` reverse the heights (`c ↦ k − c`) and `D = diag((−1)^c)` flip the sign of odd heights. Neither commutes with `M_k` on its own, but their product does:

```
>>> for name, X in [("J", J), ("D", D), ("JD", J*D)]:
...     print(name, "commutes:", (X*M - M*X).is_zero_matrix)
J commutes: False
D commutes: False
JD commutes: True                     # k = 4 and k = 6 shown; verified for all k <= 30
```

Entrywise this is one line: `(JD·M·JD)_{a,b} = (−1)^{a+b} s(k−a, k−b) = (−1)^{a+b+max(0,b−a)} = (−1)^{max(0,a−b)} = M_{a,b}`, since `a + b + max(0, b−a) ≡ a − b + max(0, b−a) = max(0, a−b) (mod 2)`.[^8] Reflecting heights turns descents into ascents; flipping the sign of odd heights turns them back.

**Even `k`: two real sectors.** `(JD)² = (−1)^k I`. For even `k` it is an involution with trace `(−1)^{k/2}`, so `M_k` preserves its `+1` and `−1` eigenspaces, of dimensions `(k+1 ± (−1)^{k/2})/2`, and `char_k` is the product of the two restricted characteristic polynomials - **that is the gallery's factorization.** For odd `k`, `(JD)² = −I`: the eigenspaces are the `±i` eigenspaces over `Q(i)`, each of dimension `(k+1)/2`, and `char_k` factors over `Q(i)` into a conjugate pair `g·ḡ`. That removes the sector split over `Q`, but on its own it does not prove `char_k` irreducible over `Q`: `g` could factor further. Irreducibility for odd `k` is proved for `k = 2^m − 1` by Eisenstein at 2 after the rescaling `λ = 2μ` ([[char-k-eisenstein-at-two](pages/char-k-eisenstein-at-two.md)]) and is SymPy-verified for every odd `k ≤ 31`. This is why `k = 1` gives `1 ± i`.

```
>>> # M restricted to each JD-eigenspace, k even: sector (eigenvalue of JD), dimension, char poly, dominant?
2  [(+1, 1, lam - 2, 'DOM'), (-1, 2, lam**2 - lam + 2, '')]
4  [(+1, 3, lam**3 - 3*lam**2 + 2*lam - 4, 'DOM'), (-1, 2, lam**2 - 2*lam + 4, '')]
6  [(+1, 3, lam**3 - 4*lam**2 + 4*lam - 8, 'DOM'), (-1, 4, lam**4 - 3*lam**3 + 8*lam**2 - 4*lam + 8, '')]
8  [(+1, 5, lam**5 - 5*lam**4 + 8*lam**3 - 20*lam**2 + 8*lam - 16, 'DOM'), (-1, 4, lam**4 - 4*lam**3 + 12*lam**2 - 8*lam + 16, '')]
10 [(+1, 5, lam**5 - 6*lam**4 + 12*lam**3 - 32*lam**2 + 16*lam - 32, 'DOM'), (-1, 6, ..., '')]
12 [(+1, 7, lam**7 - 7*lam**6 + 18*lam**5 - 56*lam**4 + 48*lam**3 - 112*lam**2 + 32*lam - 64, 'DOM'), (-1, 6, ..., '')]
```

The dominant eigenvalue `ρ_k` sits in the `+1` sector for every even `k ≤ 40` tested. The `+1` sector has dimension `k/2` when `k ≡ 2 (mod 4)` and `k/2 + 1` when `k ≡ 0 (mod 4)` - the alternation behind the unit pattern of [[castle-eigenvalue-oeis-crosswalk](pages/castle-eigenvalue-oeis-crosswalk.md)].

**What the sectors count: the parity of the last column.** The end vector decomposes as `v = v⁺ + v⁻` with `v⁺_b = [b even]` and `v⁻_b = −[b odd]` (check: `(JD v⁺)_a = (−1)^a [k−a even] = [a even]`), and `e_0` decomposes as `(e_0 ± e_k)/2`. Sectors are orthogonal (`JD` is symmetric for even `k`) and `M`-invariant, so the cross terms vanish and

```
P(k, L)  =  P_even(k, L) + P_odd(k, L),
P_even   =  Σ_{towers with c_L even} (−1)^{blocks}       (the +1 sector),
P_odd    =  Σ_{towers with c_L odd}  (−1)^{blocks}       (the −1 sector).
```

Verified against brute-force enumeration for `k = 2, 4, 6`, `L ≤ 4`:[^8]

```python
def blocks(cc):
    cc = (0,) + tuple(cc) + (0,)
    return sum(max(0, cc[i]-cc[i+1]) for i in range(len(cc)-1))
be = sum((-1)**blocks(cc) for cc in product(range(k+1), repeat=L) if cc[-1] % 2 == 0)   # == e_0 M^L [b even]
```

One consequence is immediate and pretty: at `k = 1` the two sectors are the real and imaginary parts of `(1+i)^L`,

```
P_even(1, L) =  Re((1+i)^L) = A146559(L):   1, 1, 0, −2, −4, −4, 0, 8, 16, 16, …
P_odd(1, L)  = −Im((1+i)^L) = −A009545(L):  0, −1, −2, −2, 0, 4, 8, 8, 0, −16, …
```

so **A009545 is a castle count after all**: minus the signed number of height-`≤1` towers whose last column has height 1. The two sequences the OEIS-mining pass had to tell apart ([[signed-tower-count](pages/signed-tower-count.md)]) are the two `JD` sectors of the same matrix.[^5]

## Part 2 - The factors in closed form

### Rescale by 2

Every eigenvalue of `M_k` has product `2^k` with the others (constant term of `char_k`),[^1] so set `λ = 2μ` and `g_k(μ) = char_k(2μ)/2^k`. The gallery's three-term recurrence `char_{k+1} = λ² char_{k−1} − 2 char_k`[^2] becomes

```
g_{k+1} = μ² g_{k−1} − g_k,        g_0 = 2μ − 1,   g_1 = 2μ² − 2μ + 1,
```

with integer coefficients and leading coefficient 2. Factoring `g_k` for even `k` and reading off the two factors:

```
>>> # (degree, leading coeff, constant term, dominant?) of the two factors of g_k in mu
k= 2 (k mod 4 = 2): [(1, 1, -1, 'DOMINANT'), (2, 2, 1, '')]
k= 4 (k mod 4 = 0): [(2, 1, 1, ''), (3, 2, -1, 'DOMINANT')]
k= 6 (k mod 4 = 2): [(3, 1, -1, 'DOMINANT'), (4, 2, 1, '')]
k= 8 (k mod 4 = 0): [(4, 1, 1, ''), (5, 2, -1, 'DOMINANT')]
k=10 (k mod 4 = 2): [(5, 1, -1, 'DOMINANT'), (6, 2, 1, '')]
k=12 (k mod 4 = 0): [(6, 1, 1, ''), (7, 2, -1, 'DOMINANT')]
```

(and so on through `k = 26`). One factor is always **monic of degree `k/2`** with constant term `∓1`; the other has leading coefficient 2 and degree `k/2 + 1`. The dominant root is in the monic factor exactly when `k ≡ 2 (mod 4)` - so `ρ_k/2` is an algebraic unit exactly then, as the crosswalk page found numerically.

### The monic factor: `H_d`

The monic factors, as coefficient lists:

```
k= 2: [1, -1]
k= 6: [1, -2, 1, -1]
k=10: [1, -3, 3, -4, 1, -1]
k=14: [1, -4, 6, -10, 5, -6, 1, -1]
k=18: [1, -5, 10, -20, 15, -21, 7, -8, 1, -1]
k=22: [1, -6, 15, -35, 35, -56, 28, -36, 9, -10, 1, -1]
k=26: [1, -7, 21, -56, 70, -126, 84, -120, 45, -55, 11, -12, 1, -1]
```

Read `k = 26` down its entries: `1, 7, 21, 56, 70, 126, 84, 120, 45, 55, 11, 12, 1, 1` are `C(6,0), C(7,1), C(7,2), C(8,3), C(8,4), C(9,5), C(9,6), C(10,7), …` - binomials whose top index climbs by one every *two* steps. With `d = k/2`:

```
H_d(μ)  =  Σ_{i=0}^{d} (−1)^i · C(⌊(d+i)/2⌋, i) · μ^{d−i}
```

```python
def H(d):
    return sp.Poly(sum((-1)**i * comb((d+i)//2, i) * mu**(d-i) for i in range(d+1)), mu)
```

```
>>> H(0).as_expr(), H(1).as_expr(), H(2).as_expr(), H(3).as_expr()
(1, mu - 1, mu**2 - mu + 1, mu**3 - 2*mu**2 + mu - 1)
```

`H_1 = μ − 1` (the `k = 2` eigenvalue `2`), `H_2 = μ² − μ + 1` (the sixth cyclotomic polynomial: the `k = 4` non-dominant eigenvalues `2e^{±iπ/3} = 1 ± i√3`), and **`H_3 = μ³ − 2μ² + μ − 1` is the minimal polynomial of `ψ²`**, the plastic number squared - the whole reason `ρ_6 = 2ψ²`.[^4] Every `H_d` for `d ≤ 16` is irreducible over `Q`, with constant term `(−1)^d`, and `H_d(1) = (−1)^{d+1} F_{d−1}`, `H_d(−1) = (−1)^{d+1} F_{d+2}` (Fibonacci numbers).[^8]

### The other factor is the Lucas companion, and the identity is a theorem

The leading-coefficient-2 factor is `V_d(μ) = H_{d+1}(μ) + μ² H_{d−1}(μ)`:

```
>>> sp.expand(H(4).as_expr() + mu**2*H(2).as_expr())          # k = 6, the quartic sector
2*mu**4 - 3*mu**3 + 4*mu**2 - mu + 1
```

and the full statement, checked symbolically for every even `k ≤ 40`,[^8] is

```
g_{2d}(μ)  =  H_d(μ) · ( H_{d+1}(μ) + μ² H_{d−1}(μ) ).
```

This is not just a pattern; it is a **doubling identity** of Lucas-sequence type, and it has a proof:

1. **`H_d` satisfies the same recurrence as `g_k`.** `H_{d+2} = −H_{d+1} + μ² H_d`, with `H_0 = 1`, `H_1 = μ − 1`. Coefficient by coefficient this is Pascal's rule: the coefficient of `μ^{d+2−i}` in `H_{d+2}`, `−H_{d+1}`, `μ²H_d` is `(−1)^i C(n+1, i)`, `(−1)^i C(n, i−1)`, `(−1)^i C(n, i)` with `n = ⌊(d+i)/2⌋`, and `C(n, i−1) + C(n, i) = C(n+1, i)`. (Verified symbolically for `d ≤ 40`.)
2. **A one-line Lucas-type computation.** With `r, s` the roots of `z² + z − μ² = 0` (so `r + s = −1`, `rs = −μ²`), any solution `x_n = αrⁿ + βsⁿ` of the recurrence has `x_{n+1} + μ² x_{n−1} = (r − s)(αrⁿ − βsⁿ)`, hence `x_n (x_{n+1} + μ² x_{n−1}) = (r−s)(α² r^{2n} − β² s^{2n})` - a solution of the same recurrence at index `2n`. Applied to `x = H`, its values at `n = 0, 1` are `(r−s)(α² − β²) = 2μ − 1 = g_0` and `(r−s)(α² r − β² s) = 2μ² − 2μ + 1 = g_1` (both verified symbolically), so the product agrees with `g_{2n}` at two consecutive indices and therefore for all `n`.

Together with the gallery's proven three-term recurrence this makes the factorization a theorem: **for even `k = 2d`, `char_k(λ) = 2^k · H_d(λ/2) · V_d(λ/2)`**, and `ρ_6 = 2ψ²` is the case `d = 3`. What remains conjectural (verified `k ≤ 40`) is the assignment - `H_d` is the `+1` (even-last-column) sector's polynomial when `d` is odd and the `−1` (odd-last-column) sector's when `d` is even - and the fact that the dominant root always lies in the `+1` sector.

## Part 3 - The sector sequences and OEIS

Because the sectors are `M`-invariant, `P_even(k, ·)` and `P_odd(k, ·)` are themselves C-finite, with the two factors as characteristic polynomials. Dividing the monic-sector sequence by `2^L` gives an **integer** sequence with characteristic polynomial `H_{k/2}`:

```python
def sectors(k, Lmax):
    M = M_signed(k); row = sp.Matrix([[1]+[0]*k])
    ve = sp.Matrix([1 if b % 2 == 0 else 0 for b in range(k+1)]); vo = sp.Matrix([(-1)**b if b % 2 else 0 for b in range(k+1)])
    E, O = [], []
    for L in range(Lmax+1):
        E.append(int((row*ve)[0])); O.append(int((row*vo)[0])); row = row*M
    return E, O
```

**`k ≡ 2 (mod 4)`: the even sector is `2^L` times a Hardin word count.**[^6]

| `k` | `P_even(k, L) / 2^L`, `L = 0, 1, 2, …` | OEIS | Hardin's description (`n = L + 1`) |
|---|---|---|---|
| 2 | `1, 1, 1, 1, …` | - | (`P_even(2, L) = 2^L` exactly) |
| 6 | `1, 2, 4, 7, 12, 21, 37, 65, 114, 200, …` | **A005251**`(L+3)` | `n`-bit strings with no isolated 1 |
| 10 | `1, 3, 9, 22, 51, 121, 292, 704, 1691, 4059, …` | **A202882**`(L+1)` | `n × 1` `0..2` arrays with every nonzero element `≤` some neighbor |
| 14 | `1, 4, 16, 50, 144, 422, 1268, 3823, 11472, …` | **A203094**`(L+1)` | same, `0..3` |
| 18 | `1, 5, 25, 95, 325, 1121, 3985, 14288, 50995, …` | **A203184**`(L+1)` | same, `0..4` |

The uniform statement, verified by brute force for `m = 0..4` (word lengths up to 10):[^8]

```
P_even(4m+2, L)  =  2^L · #{ words w ∈ {0,…,m}^{L+1} : every nonzero letter w_i satisfies w_i ≤ w_{i−1} or w_i ≤ w_{i+1} }.
```

```python
def hardin_count(m, L):                # words of length L over {0..m}, every nonzero letter <= some neighbor
    n = 0
    for w in product(range(m+1), repeat=L):
        ok = all(any(v <= w[j] for j in (i-1, i+1) if 0 <= j < L) for i, v in enumerate(w) if v)
        n += ok
    return n
```

```
m=1 (k=6):  words(L+1) = [1, 2, 4, 7, 12, 21, 37, 65, 114]     P_even/2^L = [1, 2, 4, 7, 12, 21, 37, 65, 114]
m=2 (k=10): words(L+1) = [1, 3, 9, 22, 51, 121, 292, 704, 1691] P_even/2^L = [1, 3, 9, 22, 51, 121, 292, 704, 1691]
```

Hardin's OEIS entries carry their recurrences as "Empirical: a(n) = 3a(n−1) − 3a(n−2) + 4a(n−3) − a(n−4) + a(n−5)" (A202882), and likewise for A203094 and A203184. Those are exactly `H_5`, `H_7`, `H_9`. On the castle side they are theorems (the sector's characteristic polynomial); what the word side still lacks is a bijective or transfer-matrix argument that the two objects agree - the open item filed on IDEAS. A proof would confirm four empirical OEIS recurrences at once and give the castle a genuinely new interpretation of a family of sequences.

**`k ≡ 0 (mod 4)`: the odd sector carries `H_d`.**[^8]

| `k` | `P_odd(k, L) / 2^L` | characteristic polynomial |
|---|---|---|
| 4 | `0, −1, −1, 0, 1, 1, 0, −1, −1, …` = `−A010892(L)` (period 6) | `H_2 = μ² − μ + 1` |
| 8 | `0, −2, −4, −3, 4, 15, 19, 0, −46, −88, −57, 104, …` (not in OEIS) | `H_4 = μ⁴ − 2μ³ + 3μ² − μ + 1` |
| 12 | `0, −3, −9, −13, 3, 65, 167, 182, −215, −1378, …` (not in OEIS) | `H_6` |

So for height-`≤4` towers the odd-last-column signed count is `−2^L · (0, 1, 1, 0, −1, −1, …)`: a `2^L` times a sixth-root-of-unity pattern, the eigenvalues `1 ± i√3` in action. The even sectors for `k ≡ 0 (mod 4)` (`1, 3, 9, 25, 69, 193, 541, …` at `k = 4`; `1, 5, 25, 105, 425, 1761, …` at `k = 8`) carry the leading-coefficient-2 factor, are not divisible by `2^L`, and are not in OEIS. The `k = 2` odd sector is `−A107920`, the Lucas-type sequence of `(1 ± √−7)/2` - the `k = 2` non-dominant eigenvalues.

## What this settles and what it opens

**Settled.**
- `char_k` factors for even `k` because `M_k` commutes with `JD`; the factors are the even- and odd-last-column sectors; for odd `k`, `JD` is a complex structure and `char_k` is a norm `g·ḡ` from `Q(i)[x]`. Irreducibility over `Q` is proved for `k = 2^m − 1` ([[char-k-eisenstein-at-two](pages/char-k-eisenstein-at-two.md)]) and verified for odd `k ≤ 31`.
- Closed forms: `char_{2d}(λ) = 2^{2d} H_d(λ/2) V_d(λ/2)` with `H_d = Σ (−1)^i C(⌊(d+i)/2⌋, i) μ^{d−i}` and `V_d = H_{d+1} + μ² H_{d−1}`, proved via Pascal's rule and a Lucas doubling computation.
- `ρ_6 = 2ψ²` because `H_3` is the minimal polynomial of `ψ²`; `ρ_k/2` is a unit for `k ≡ 2 (mod 4)` because the dominant root then lies in the monic factor.
- `P_even(4m+2, L) = 2^L ·` Hardin word count (A005251, A202882, A203094, A203184), verified `m ≤ 4`; `P_odd(4, L) = −2^L · A010892(L)`; `P_even(1, L) = A146559(L)`, `P_odd(1, L) = −A009545(L)`; `P_odd(2, L) = −A107920(L)`.

**Open** (filed on IDEAS).
- Prove `char_k` irreducible over `Q` for every odd `k`. Eisenstein at 2 reaches exactly `k = 2^m − 1` ([[char-k-eisenstein-at-two](pages/char-k-eisenstein-at-two.md)]); `k = 5, 9, 11, 13, …` need another argument.
- Prove that the dominant root lies in the `+1` sector and that `H_d` belongs to the `+1` sector iff `d` is odd.
- The Hardin identity is proved on [[hardin-word-identity](pages/hardin-word-identity.md)] by an explicit unimodular change of basis between the word automaton and the halved even-sector matrix (every `m ≤ 8` checked symbolically; general `m` reduces to a finite entrywise check). A sign-reversing involution realizing it object by object is still open.
- Which `H_d` have Pisot dominant roots (`d = 3` yes; `d = 5, 7, 9, …` no) and whether the Jacobi-Perron expansion of `ρ_k/2` is ever periodic beyond `k = 6` (`k = 10, 14`: not within 300 / 200 exact steps).
- Whether Axis 8 of [[castle-classification-growth](pages/castle-classification-growth.md)] should admit a non-metallic rung for `2ψ²`.

## Snippet index

| snippet | teaches | where |
|---|---|---|
| `M_signed(k)` | the signed transfer matrix; `char(M_k) = char_k` | Part 1 |
| `J`, `D`, `JD` commutation test | find the symmetry by testing candidate involutions, not by staring | Part 1 |
| `(X ± I).columnspace()` + restricted matrix | block-diagonalize along an involution's eigenspaces | Part 1 |
| `blocks(cc)` + parity filter | brute-force check that a sector is a combinatorial statistic | Part 1 |
| `H(d)` | a binomial closed form for a factor; test it against `sp.factor` output | Part 2 |
| `sp.solve` on coefficient equations | recover a polynomial recurrence `H_{d+2} = A H_{d+1} + B H_d` from data | Part 2 |
| `sectors(k, Lmax)` | C-finite subsequences from invariant subspaces | Part 3 |
| `hardin_count(m, L)` | brute-force a conjectured OEIS interpretation before believing it | Part 3 |

## Appearances in Sources

- [[oeis-mining-pe502](pages/oeis-mining-pe502.md)] - the `P(k, ·)` family and `char_k`.
- [[project-euler-502-solution](pages/project-euler-502-solution.md)] - the `num_k/den_k` recurrence from which the three-term recurrence for `char_k` (and hence for `g_k`) follows.
- [[project-euler-502-castle-factoring](pages/project-euler-502-castle-factoring.md)] - the block-count formula the transfer matrix encodes.

## Related Concepts

- [[plastic-number](pages/plastic-number.md)] - `ψ`, `ψ²`, Padovan / Perrin, and the Jacobi-Perron expansions.
- [[castle-eigenvalue-oeis-crosswalk](pages/castle-eigenvalue-oeis-crosswalk.md)] - where `ρ_6 = 2ψ²` and the `k mod 4` unit pattern were found numerically; this page is their explanation.
- [[generating-function-gallery](pages/generating-function-gallery.md)] - the `char_k` catalogue and three-term recurrence this page factors.
- [[signed-tower-count](pages/signed-tower-count.md)] - `P(k, L)`, A146559 and A009545, which are the two `k = 1` sectors.
- [[recurrence-discovery](pages/recurrence-discovery.md)] - the orders `k + 1` in `L`; the sector dimensions `(k+1 ± (−1)^{k/2})/2` refine them.
- [[castle-sign](pages/castle-sign.md)] - the sign `(−1)^{blocks}` and its factorization over consecutive columns.
- [[spectral-analysis](pages/spectral-analysis.md)] - the transfer-matrix spectrum (method 1 there); this page is a worked instance of "find the symmetry, block-diagonalize, read off the growth constant".
- [[metallic-means](pages/metallic-means.md)] / [[castle-classification-growth](pages/castle-classification-growth.md)] - the Axis-8 growth-constant ladder that `2ψ²` sits beside.
- [[finite-fields](pages/finite-fields.md)] / [[mod-p-observatory](pages/mod-p-observatory.md)] - the sector polynomials reduce mod `p` too; their orders are the pieces of `per(char_k)`.
- [[aocp-binomial-coefficients](pages/aocp-binomial-coefficients.md)] - Pascal's rule `C(r,k) = C(r−1,k) + C(r−1,k−1)`, the identity that proves the `H_{d+1} + μ² H_{d−1}` doubling identity in Part 2.
- [[new-sequence-fw3](pages/new-sequence-fw3.md)] - `char_2 = (x−2)(x²−x+2)` is why `F(w,3)` has order 6: its `(x−2)` is shared with the `2^w` term.
- [[aocp-generating-permutations-tuples](pages/aocp-generating-permutations-tuples.md)] - the sector tables are computed by Algorithm M enumeration of `{0..k}^L`.
- [[signed-tower-k-direction](pages/signed-tower-k-direction.md)] - the complementary direction of the same `P(k, L)` 2D array: k-direction factors as `(x+1)^L (x-1)^{L-2}` while this page factors the L-direction char_k into parity sectors.

## Footnotes

[^1]: [[oeis-mining-pe502](pages/oeis-mining-pe502.md)] `mine-notes.md` §"Vein 1" L31-37 - "The general P(k,·) family is C-finite of order k+1: P(1): x^2 - 2x + 2 ... (constant term = (-1)^{k-1} 2^k; leading coeff -(k+1))."

[^2]: [[project-euler-502-solution](pages/project-euler-502-solution.md)] §"The rational-function path (h ≤ 15000)" L124-138 - "num_k(x) = 2·den_{k-1}(x) - num_{k-1}(x); den_k(x) = den_{k-1}(x)·(1 - 2x) + num_{k-1}(x)·x"; the elimination to `den_{k+1} = den_{k−1} − 2x·den_k`, i.e. `char_{k+1} = λ² char_{k−1} − 2 char_k`, is carried out on [[generating-function-gallery](pages/generating-function-gallery.md)] and re-verified here for `k ≤ 40`.

[^3]: [[project-euler-502-castle-factoring](pages/project-euler-502-castle-factoring.md)] §"The sign of a castle" L105-113 - "blocks = ∑_{i=0}^{L} max(0, c_i - c_{i+1}), c_0 = c_{L+1} = 0."

[^4]: Verified by execution (SymPy 1.14): `resultant(x³ − x − 1, μ − x², x)` factors to `μ³ − 2μ² + μ − 1 = H_3`; `resultant(H_3, λ − 2μ, μ) = λ³ − 4λ² + 4λ − 8`, the cubic factor of `char_6`.

[^5]: https://oeis.org/A146559 (2026-09-16) - "Expansion of (1-x)/(1 - 2*x + 2*x^2)", data `1, 1, 0, -2, -4, -4, 0, 8, 16, 16, 0, -32`; https://oeis.org/A009545 - "Expansion of exponential generating function (EGF) sin(x)*exp(x)", data `0, 1, 2, 2, 0, -4, -8, -8, 0, 16`; https://oeis.org/A107920 - "Lucas and Lehmer numbers with parameters (1 +- sqrt(-7))/2", data `0, 1, 1, -1, -3, 1, 5, 7, -3, -17`; https://oeis.org/A010892 - "Inverse of 6th cyclotomic polynomial. A period 6 sequence", `1, 1, 0, -1, -1, 0, …` (our `P_odd(4,L)/2^L` is `−A010892(L−1)`-aligned: `0, −1, −1, 0, 1, 1, …`; matched by OEIS search on the terms). Sector sequences computed by execution, `L ≤ 24`.

[^6]: https://oeis.org/A005251 (2026-09-16) - offset 0, "a(n) = 2*a(n-1) - a(n-2) + a(n-3)", comment "a(n+3) is the number of n-bit sequences that avoid 010"; https://oeis.org/A202882 - offset 1, "Number of n X 1 0..2 arrays with every nonzero element less than or equal to some horizontal or vertical neighbor", data `1, 3, 9, 22, 51, 121, 292, 704, 1691, 4059, 9749`, formula "Empirical: a(n) = 3*a(n-1) -3*a(n-2) +4*a(n-3) -a(n-4) +a(n-5)", xref "Column 1 of A202889"; https://oeis.org/A203094 - "Number of nX1 0..3 arrays with every nonzero element less than or equal to some horizontal or vertical neighbor", data `1, 4, 16, 50, 144, 422, 1268, 3823, 11472, 34350`, "Empirical: a(n) = 4*a(n-1) -6*a(n-2) +10*a(n-3) -5*a(n-4) +6*a(n-5) -a(n-6) +a(n-7)"; https://oeis.org/A203184 - "Number of n X 1 0..4 arrays with every nonzero element less than or equal to some horizontal or vertical neighbor", data `1, 5, 25, 95, 325, 1121, 3985, 14288, 50995, 181336`, "Empirical: a(n) = 5*a(n-1) -10*a(n-2) +20*a(n-3) -15*a(n-4) +21*a(n-5) -7*a(n-6) +8*a(n-7) -a(n-8) +a(n-9)". The three empirical recurrences are the coefficient lists of `H_5`, `H_7`, `H_9`.

[^7]: Verified by execution: exact Jacobi-Perron (see [[plastic-number](pages/plastic-number.md)]) on `ρ_10/2` (`μ⁵ − 3μ⁴ + 3μ³ − 4μ² + μ − 1`) and `ρ_10`: no repeated state in 300 steps; on `ρ_14/2` (`H_7`): none in 200 steps; on `ρ_8/2`: none in 200 steps.

[^8]: Verified by execution (Python 3.11, SymPy 1.14). (i) `JD·M_k = M_k·JD` for `k ≤ 30`; the entrywise identity `(−1)^{a+b+max(0,b−a)} = (−1)^{max(0,a−b)}` for `a, b ≤ 40`. (ii) Restricted characteristic polynomials on the `±1` eigenspaces of `JD` for `k ≤ 12`, dominant root always in the `+1` sector; monic/leading-2 factor assignment and `H_d` coefficient formula for all even `k ≤ 40`. (iii) `P_even`, `P_odd` by enumeration vs matrix for `k = 2, 4, 6`, `L ≤ 4`. (iv) `H_{d+2} = −H_{d+1} + μ² H_d` for `d ≤ 40`; `g_{k+1} = μ² g_{k−1} − g_k` for `k ≤ 40`; `g_{2d} = H_d (H_{d+1} + μ² H_{d−1})` for `d ≤ 20`; the two closed-form identities `(r−s)(α² − β²) = 2μ − 1`, `(r−s)(α² r − β² s) = 2μ² − 2μ + 1` simplified symbolically with `s = −1 − r`, `r² = μ² − r`. (v) `H_d` irreducible for `d ≤ 16` (`sp.factor_list`); dominant-root moduli and Pisot check. (vi) `P_even(4m+2, L)/2^L = hardin_count(m, L+1)` for `m = 0..4`, `L ≤ 9` (`m ≤ 2`) or `L ≤ 7`; `P_even(6, L) = 2^L·A005251(L+3)` for `L ≤ 16`; `P_odd(4, L)/2^L` period-6 pattern for `L ≤ 16`; `P_even(1,L) = Re((1+i)^L)`, `P_odd(1,L) = −Im((1+i)^L)` for `L ≤ 12`; Berlekamp-Massey characteristic polynomials of the sector sequences for `k = 2..16`.
