---
title: Tower parity sectors - why char_k factors, and where the plastic number comes from
category: Analyses
summary: The signed transfer matrix M̃_k commutes with JD, "reflect heights, flip the sign of odd heights", so for even k the signed tower count splits by the parity of the last column, P = P_even + P_odd, and char_k splits into the characteristic polynomials of the two sectors. In μ = λ/2 the factors are H_d(μ) = Σ_i (−1)^i C(⌊(d+i)/2⌋, i) μ^{d−i} and V_d = H_{d+1} + μ² H_{d−1}, with char_{2d}(2μ) = 2^{2d} H_d V_d proved by Pascal's rule and a Lucas-type doubling computation. H_3 is the minimal polynomial of ψ² (ψ the plastic number), so ρ_6 = 2ψ². For k = 4m + 2 the even sector is 2^L times Hardin's counts of words in which every nonzero letter is at most a neighbor (A005251, A202882, A203094, A203184).
tags: [analysis, castle, signed-tower-count, transfer-matrix, symmetry, factorization, plastic-number, quasi-polynomial, oeis, hardin, sympy, verification, pedagogy]
sources: [project-euler-502-solution, project-euler-502-castle-factoring, oeis-encyclopedia]
created: 2026-09-16
updated: 2026-10-25
---

# Tower parity sectors - why `char_k` factors, and where the plastic number comes from

## The question

`char_k(λ) = λ^{k+1} den_k(1/λ)` is the characteristic polynomial of the linear recurrence of the signed tower count `P(k, ·)` in the base length `L` ([[signed-tower-count](pages/signed-tower-count.md)]). For even `k ≤ 40` it has two irreducible factors, of degrees `k/2` and `k/2 + 1`, and for odd `k ≤ 31` it is irreducible ([[generating-function-gallery](pages/generating-function-gallery.md)]), each `k` proved by a prime mod which it stays irreducible ([[castle-cryptography-number-theory](pages/castle-cryptography-number-theory.md)]). At `k = 6` its root of largest modulus is `2ψ²`, with `ψ` the [[plastic-number](pages/plastic-number.md)]. This page derives the factorization from a symmetry of the transfer matrix (Part 1), gives the two factors in closed form and proves the product formula (Part 2), and identifies the sequences of the two sectors (Part 3). For `k ≡ 2 (mod 4)` the even-last-column part of `P(k, L)` is `2^L` times a word count that R. H. Hardin entered in the OEIS with an "empirical" recurrence; [[hardin-word-identity](pages/hardin-word-identity.md)] proves the identity for each `k ≤ 34`.

Every printed value on this page was recomputed.[^1]

## Part 1 - The symmetry

The column-height dynamic program of [[castle-counting-formula](pages/castle-counting-formula.md)] (the section *Signed tower count*) is a matrix product. Towers of height at most `k` on a base of length `L` have column heights `c_1, …, c_L ∈ {0, …, k}`, their block count is the total descent `Σ_{i=0}^{L} max(0, c_i − c_{i+1})` with `c_0 = c_{L+1} = 0`,[^2] and the sign `(−1)^{blocks}` is a product over consecutive pairs. The **signed transfer matrix** `M̃_k`, with the tilde marking the sign, has rows and columns indexed by the heights `0, …, k` and entry `(−1)^{max(0, a − b)}` for a step from height `a` to height `b`:

```python
def M_signed(k):                       # the sign (-1)^max(0, a-b) of a step from height a to height b
    return sp.Matrix(k+1, k+1, lambda a, b: 1 if a <= b else (-1)**(a-b))
```

At `k = 1`, `M̃_1 = [[1, 1], [−1, 1]]`. With `e_0` the start at height 0 and `v_b = (−1)^b` the final drop from height `b` to 0, `P(k, L) = e_0ᵀ M̃_k^L v`. The characteristic polynomial of `M̃_k` is `char_k`:

```
>>> for k in range(1, 7): print(k, sp.factor(M_signed(k).charpoly(lam).as_expr()) == sp.factor(c[k]))
1 True ... 6 True
```

**The involution.** Let `J` reverse the heights (`c ↦ k − c`) and `D = diag((−1)^c)` flip the sign of odd heights. Neither commutes with `M̃_k`, but their product does:

```
>>> for name, X in [("J", J), ("D", D), ("JD", J*D)]:
...     print(name, "commutes:", (X*M - M*X).is_zero_matrix)
J commutes: False
D commutes: False
JD commutes: True                     # k = 4 and k = 6 shown; checked for all k <= 30
```

The proof is one line. `(JD)_{a,b} = [b = k − a]·(−1)^b`, so `(JD)² = (−1)^k I` and

```
(JD · M̃_k · JD)_{a,b}  =  (−1)^k (−1)^{a+b} (−1)^{max(0, b − a)}  =  (−1)^k (−1)^{max(0, a − b)},
```

since `a + b + max(0, b − a) ≡ max(0, a − b) (mod 2)`: both sides are even when `b ≥ a`, and both are `≡ a − b` when `a > b`. So `JD·M̃_k·JD = (JD)²·M̃_k`, and `JD` commutes with `M̃_k`.[^1] Reflecting the heights turns descents into ascents, and flipping the signs of odd heights turns them back. [[castle-sign-kms-matrix](pages/castle-sign-kms-matrix.md)] identifies `JD` as the reversal symmetry of the Kac-Murdock-Szegő matrix `K(i) = (i^{|a−b|})`, carried back through the diagonal similarity `diag(i^c)`, which is where `(JD)² = (−1)^k` comes from.

**Even `k`: two real sectors.** For even `k`, `JD` is an involution with trace `(−1)^{k/2}`, so `M̃_k` preserves its `+1` and `−1` eigenspaces, of dimensions `(k + 1 ± (−1)^{k/2})/2`, and `char_k` is the product of the characteristic polynomials of `M̃_k` on the two eigenspaces. The `+1` sector has dimension `k/2` when `k ≡ 2 (mod 4)` and `k/2 + 1` when `k ≡ 0 (mod 4)`.

**Odd `k`.** For odd `k`, `(JD)² = −I`, and `JD` has no real eigenvectors: its eigenspaces are the `±i` eigenspaces over `Q(i)`, each of dimension `(k + 1)/2`, and `char_k = g·ḡ` for a polynomial `g` over `Q(i)` and its complex conjugate. This rules out the sector split over the rationals but does not prove `char_k` irreducible, since `g` could factor further. Irreducibility is proved for `k = 2^m − 1` by Eisenstein's criterion at 2 after the rescaling `λ = 2μ` ([[char-k-eisenstein-at-two](pages/char-k-eisenstein-at-two.md)]), and computed for odd `k ≤ 31`.

```
>>> # M̃_k restricted to each JD-eigenspace, k even: (eigenvalue of JD, dimension, char poly, root of largest modulus?)
2  [(+1, 1, lam - 2, 'DOM'), (-1, 2, lam**2 - lam + 2, '')]
4  [(+1, 3, lam**3 - 3*lam**2 + 2*lam - 4, 'DOM'), (-1, 2, lam**2 - 2*lam + 4, '')]
6  [(+1, 3, lam**3 - 4*lam**2 + 4*lam - 8, 'DOM'), (-1, 4, lam**4 - 3*lam**3 + 8*lam**2 - 4*lam + 8, '')]
8  [(+1, 5, lam**5 - 5*lam**4 + 8*lam**3 - 20*lam**2 + 8*lam - 16, 'DOM'), (-1, 4, lam**4 - 4*lam**3 + 12*lam**2 - 8*lam + 16, '')]
10 [(+1, 5, lam**5 - 6*lam**4 + 12*lam**3 - 32*lam**2 + 16*lam - 32, 'DOM'), (-1, 6, ..., '')]
12 [(+1, 7, lam**7 - 7*lam**6 + 18*lam**5 - 56*lam**4 + 48*lam**3 - 112*lam**2 + 32*lam - 64, 'DOM'), (-1, 6, ..., '')]
```

For every even `k ≤ 40`, the root of largest modulus `ρ_k` lies in the `+1` sector.

**What the sectors count: the parity of the last column.** For even `k`, the end vector splits as `v = v⁺ + v⁻` with `v⁺_b = [b even]` and `v⁻_b = −[b odd]`, and `JD v⁺ = v⁺`, `JD v⁻ = −v⁻`; the start vector splits as `e_0 = (e_0 + e_k)/2 + (e_0 − e_k)/2`, with `JD e_0 = e_k`. For even `k`, `JD` is symmetric, so its eigenspaces are orthogonal, and `M̃_k` preserves them, so the cross terms vanish:

```
P(k, L)  =  P_even(k, L) + P_odd(k, L),
P_even   =  e_0ᵀ M̃_k^L v⁺  =  Σ_{towers with c_L even} (−1)^{blocks}       (the +1 sector),
P_odd    =  e_0ᵀ M̃_k^L v⁻  =  Σ_{towers with c_L odd}  (−1)^{blocks}       (the −1 sector).
```

The sums over towers agree with the matrix products for `k = 2, 4, 6` and `L ≤ 4`:[^1]

```python
def blocks(cc):
    cc = (0,) + tuple(cc) + (0,)
    return sum(max(0, cc[i]-cc[i+1]) for i in range(len(cc)-1))
be = sum((-1)**blocks(cc) for cc in product(range(k+1), repeat=L) if cc[-1] % 2 == 0)   # == e_0 M^L [b even]
```

The same split by the last column, at `k = 1`, gives the real and imaginary parts of `(1+i)^L` ([[signed-tower-count](pages/signed-tower-count.md)], the section *The case k = 1*):

```
P_even(1, L) =  Re((1+i)^L) = A146559(L):   1, 1, 0, −2, −4, −4, 0, 8, 16, 16, …
P_odd(1, L)  = −Im((1+i)^L) = −A009545(L):  0, −1, −2, −2, 0, 4, 8, 8, 0, −16, …
```

So `A009545(L)` is the number of castles of width `L` and height 2 with last column at height 2 and an even number of blocks, minus the number with an odd number.[^3]

## Part 2 - The factors in closed form

### Rescale by 2

The eigenvalues of `M̃_k` multiply to `2^k`, since the constant term of `char_k` is `(−1)^{k+1} 2^k` ([[castle-counting-formula](pages/castle-counting-formula.md)], the Proposition in the section *Signed tower count*).[^4] So set `λ = 2μ` and `g_k(μ) = char_k(2μ)/2^k`. The recurrence `char_{k+1} = λ² char_{k−1} − 2 char_k` ([[signed-tower-count](pages/signed-tower-count.md)], the section *Recurrences in L*)[^5] becomes

```
g_{k+1}  =  μ² g_{k−1} − g_k,        g_0 = 2μ − 1,   g_1 = 2μ² − 2μ + 1,             (1)
```

so every `g_k` has integer coefficients and leading coefficient 2. Factoring `g_k` for even `k`:

```
>>> # (degree, leading coeff, constant term, root of largest modulus?) of the two factors of g_k in mu
k= 2 (k mod 4 = 2): [(1, 1, -1, 'DOMINANT'), (2, 2, 1, '')]
k= 4 (k mod 4 = 0): [(2, 1, 1, ''), (3, 2, -1, 'DOMINANT')]
k= 6 (k mod 4 = 2): [(3, 1, -1, 'DOMINANT'), (4, 2, 1, '')]
k= 8 (k mod 4 = 0): [(4, 1, 1, ''), (5, 2, -1, 'DOMINANT')]
k=10 (k mod 4 = 2): [(5, 1, -1, 'DOMINANT'), (6, 2, 1, '')]
k=12 (k mod 4 = 0): [(6, 1, 1, ''), (7, 2, -1, 'DOMINANT')]
```

One factor is monic of degree `k/2` with constant term `(−1)^{k/2}`, the other has leading coefficient 2 and degree `k/2 + 1`; the section *The product formula* proves this for every even `k`. For even `k ≤ 40` the root of largest modulus is in the monic factor exactly when `k ≡ 2 (mod 4)`. Then `ρ_k/2` is a root of a monic integer polynomial with constant term `±1`, an algebraic unit; for `k ≡ 0 (mod 4)` and `k ≤ 40` it is a root of an irreducible primitive polynomial with leading coefficient 2, so it is not an algebraic integer.

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

Read `k = 26` down its entries: `1, 7, 21, 56, 70, 126, 84, 120, 45, 55, 11, 12, 1, 1` are `C(6,0), C(7,1), C(7,2), C(8,3), C(8,4), C(9,5), C(9,6), C(10,7), …`, binomial coefficients whose top index rises by one every two steps. With `d = k/2`:

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

`H_1 = μ − 1` gives the eigenvalue 2 of `k = 2`. `H_2 = μ² − μ + 1` is the sixth cyclotomic polynomial, which gives the eigenvalues `2e^{±iπ/3} = 1 ± i√3` of `k = 4`. `H_3 = μ³ − 2μ² + μ − 1` is the minimal polynomial of `ψ²`, the square of the plastic number, which gives `ρ_6 = 2ψ²`.[^6] The constant term of `H_d` is `(−1)^d`, the `i = d` term. `H_d(1) = (−1)^d F_{d−1}` and `H_d(−1) = (−1)^d F_{d+2}`, with `F_n` the Fibonacci numbers and `F_{−1} = 1`: at `μ = ±1`, the recurrence of the next section makes `(−1)^d H_d(±1)` satisfy the Fibonacci recurrence, from the initial values `1, 0` and `1, 2`. `H_d` is irreducible for every `d ≤ 20`.[^1]

### The other factor and the product formula

The factor with leading coefficient 2 is `V_d(μ) = H_{d+1}(μ) + μ² H_{d−1}(μ)`. At `k = 6`:

```
>>> sp.expand(H(4).as_expr() + mu**2*H(2).as_expr())          # k = 6, the quartic sector
2*mu**4 - 3*mu**3 + 4*mu**2 - mu + 1
```

**Theorem.** For `d ≥ 1`,

```
g_{2d}(μ)  =  H_d(μ) · V_d(μ)  =  H_d(μ) · ( H_{d+1}(μ) + μ² H_{d−1}(μ) ),                (2)
```

so `char_k(λ) = 2^k · H_{k/2}(λ/2) · V_{k/2}(λ/2)` for every even `k ≥ 2`.

*Proof.* *Step 1: `H_d` satisfies the recurrence of `g_k`.* `H_{d+2} = −H_{d+1} + μ² H_d`, with `H_0 = 1` and `H_1 = μ − 1`. Coefficient by coefficient this is Pascal's rule: with `n = ⌊(d + i)/2⌋`, the coefficients of `μ^{d+2−i}` in `H_{d+2}`, `−H_{d+1}` and `μ² H_d` are `(−1)^i C(n+1, i)`, `(−1)^i C(n, i−1)` and `(−1)^i C(n, i)`, and `C(n, i−1) + C(n, i) = C(n+1, i)` ([[aocp-binomial-coefficients](pages/aocp-binomial-coefficients.md)]).

*Step 2: doubling.* Let `r, s` be the roots of `z² + z − μ² = 0`, so `r + s = −1` and `rs = −μ²`, and write `H_n = α rⁿ + β sⁿ`. Since `r² + μ² = r(r − s)` and `s² + μ² = −s(r − s)`, `H_{n+1} + μ² H_{n−1} = (r − s)(α rⁿ − β sⁿ)`, so

```
H_n · ( H_{n+1} + μ² H_{n−1} )  =  (r − s)(α² r^{2n} − β² s^{2n}).
```

The sequence `y_m = (r − s)(α² r^m − β² s^m)` satisfies the same recurrence as `H` and as `g` in Equation (1), and its first two terms are `y_0 = (r − s)(α² − β²) = 2μ − 1 = g_0` and `y_1 = (r − s)(α² r − β² s) = 2μ² − 2μ + 1 = g_1`. So `y_m = g_m` for all `m`, and `g_{2n} = y_{2n}` is Equation (2).[^1] □

`H_d` is monic of degree `d` with constant term `(−1)^d`, and `V_d` has degree `d + 1` and leading coefficient 2, since `H_{d+1}` and `μ² H_{d−1}` both have leading term `μ^{d+1}`. Its constant term is `H_{d+1}(0) = (−1)^{d+1}`.

**Which factor is which sector.** For `d ≤ 20`, `H_d` and `V_d` are irreducible and `V_d` is primitive, so the two sector polynomials of `char_{2d}` are `H_d` and `V_d`, in the variable `μ`. Their degrees decide which is which: the `+1` sector has dimension `d` when `d` is odd and `d + 1` when `d` is even. So for even `k ≤ 40`, `H_{k/2}` is the polynomial of the `+1` (even-last-column) sector when `k ≡ 2 (mod 4)` and of the `−1` (odd-last-column) sector when `k ≡ 0 (mod 4)`.

**Over `Z[1/2]` and modulo 2.** The two sector factors `2^d H_d(λ/2)` and `2^d V_d(λ/2)` of `char_{2d}` have resultant `±2^{d(d+1)}` for every `d ≤ 15` (computed), so for these `d` the sector split of `Q[x]/(char_k)` holds over `Z[1/2]` and survives reduction modulo every odd prime ([[chinese-remainder-theorem](pages/chinese-remainder-theorem.md)]). Modulo 2 the two factors are `λ^d` and `λ^d(λ + 1)` for `d ≤ 15` (computed), and [[castle-ring-spectrum](pages/castle-ring-spectrum.md)] reads the two sectors as the components of `Spec Z[x]/(char_k)`, which meet only at the point `(2, x)`.[^7]

## Part 3 - The sector sequences and OEIS

The sectors are invariant under `M̃_k`, so `P_even(k, ·)` and `P_odd(k, ·)` satisfy the linear recurrences of their sector polynomials. The sector of `H_{k/2}` has the characteristic polynomial `2^{k/2} H_{k/2}(λ/2)` in `λ`, so its sequence divided by `2^L` has the monic integer characteristic polynomial `H_{k/2}(μ)`, and is an integer sequence:

```python
def sectors(k, Lmax):
    M = M_signed(k); row = sp.Matrix([[1]+[0]*k])
    ve = sp.Matrix([1 if b % 2 == 0 else 0 for b in range(k+1)]); vo = sp.Matrix([(-1)**b if b % 2 else 0 for b in range(k+1)])
    E, O = [], []
    for L in range(Lmax+1):
        E.append(int((row*ve)[0])); O.append(int((row*vo)[0])); row = row*M
    return E, O
```

**`k ≡ 2 (mod 4)`: the even sector is `2^L` times a Hardin word count.**[^8]

| `k` | `P_even(k, L) / 2^L`, `L = 0, 1, 2, …` | OEIS | description (`n = L + 1`) |
|---|---|---|---|
| 2 | `1, 1, 1, 1, …` | - | (`P_even(2, L) = 2^L`) |
| 6 | `1, 2, 4, 7, 12, 21, 37, 65, 114, 200, …` | **A005251**`(L+3)` | `n`-bit strings with no isolated 1 |
| 10 | `1, 3, 9, 22, 51, 121, 292, 704, 1691, 4059, …` | **A202882**`(L+1)` | Hardin: `n × 1` `0..2` arrays with every nonzero element `≤` some neighbor |
| 14 | `1, 4, 16, 50, 144, 422, 1268, 3823, 11472, …` | **A203094**`(L+1)` | Hardin: the same, `0..3` |
| 18 | `1, 5, 25, 95, 325, 1121, 3985, 14288, 50995, …` | **A203184**`(L+1)` | Hardin: the same, `0..4` |

With `m = (k − 2)/4`, the rows are one statement, which agrees with enumeration for `m ≤ 4` (words of length up to 12 for `m = 1`, 10 for `m = 0, 2`, 8 for `m = 3` and 7 for `m = 4`):[^1]

```
P_even(4m+2, L)  =  2^L · #{ words w ∈ {0,…,m}^{L+1} : every nonzero letter w_i satisfies w_i ≤ w_{i−1} or w_i ≤ w_{i+1} }.
```

At `m = 1` a word over `{0, 1}` qualifies when no `1` is isolated, which is the `k = 6` row.

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

Hardin's entries give their recurrences as "Empirical", for example "a(n) = 3*a(n-1) -3*a(n-2) +4*a(n-3) -a(n-4) +a(n-5)" on A202882, and the recurrences of A202882, A203094 and A203184 are `H_5`, `H_7` and `H_9`. On the castle side, `H_{k/2}` is the characteristic polynomial of the even sector (by the section *Which factor is which sector*), so the recurrence holds for `P_even(k, ·)/2^L`. [[hardin-word-identity](pages/hardin-word-identity.md)] proves that the two sequences agree for each `m ≤ 8`, by an explicit change of basis between the word automaton and the halved even-sector matrix; for general `m` the check is a finite case analysis on the matrix entries, not written out.

**`k ≡ 0 (mod 4)`: the odd sector carries `H_{k/2}`.**[^1]

| `k` | `P_odd(k, L) / 2^L`, `L = 0, 1, 2, …` | characteristic polynomial |
|---|---|---|
| 4 | `0, −1, −1, 0, 1, 1, 0, −1, −1, …`, period 6; `−A010892(L−1)` for `L ≥ 1` | `H_2 = μ² − μ + 1` |
| 8 | `0, −2, −4, −3, 4, 15, 19, 0, −46, −88, −57, 104, …` | `H_4 = μ⁴ − 2μ³ + 3μ² − μ + 1` |
| 12 | `0, −3, −9, −13, 3, 65, 167, 182, −215, −1378, …` | `H_6` |

So for towers of height at most 4, the odd-last-column signed count is `2^L` times the period-6 pattern `0, −1, −1, 0, 1, 1`, from the eigenvalues `1 ± i√3`. The even sectors for `k ≡ 0 (mod 4)` carry `V_{k/2}`, whose leading coefficient is 2, and are not divisible by `2^L`: `1, 3, 9, 25, 69, 193, 541, …` at `k = 4` and `1, 5, 25, 105, 425, 1761, …` at `k = 8`. The odd sector at `k = 2` is `−A107920(L)`, the Lucas sequence of `(1 ± √−7)/2`, the two eigenvalues of `k = 2` other than 2.[^3]

## Snippet index

| snippet | teaches | where |
|---|---|---|
| `M_signed(k)` | the signed transfer matrix `M̃_k`, with characteristic polynomial `char_k` | Part 1 |
| `J`, `D`, `JD` commutation test | find a symmetry by testing candidate involutions | Part 1 |
| `(X ± I).columnspace()` + restricted matrix | block-diagonalize along the eigenspaces of an involution | Part 1 |
| `blocks(cc)` + parity filter | check by brute force that a sector is a sum over towers | Part 1 |
| `H(d)` | a binomial closed form for a factor, tested against `sp.factor` | Part 2 |
| `sp.solve` on coefficient equations | recover a polynomial recurrence `H_{d+2} = A H_{d+1} + B H_d` from data | Part 2 |
| `sectors(k, Lmax)` | the sequences of the invariant subspaces | Part 3 |
| `hardin_count(m, L)` | check an OEIS interpretation by brute force | Part 3 |

## Appearances in Sources

- [[project-euler-502-solution](pages/project-euler-502-solution.md)] - the update of `num_k` and `den_k`, from which the recurrence of `char_k`, and so Equation (1), follows.
- [[project-euler-502-castle-factoring](pages/project-euler-502-castle-factoring.md)] - the block count as total descent, which the transfer matrix encodes.

## Related Concepts

- [[signed-tower-count](pages/signed-tower-count.md)] - `P(k, L)`, the recurrence of `char_k`, and the case `k = 1`.
- [[generating-function-gallery](pages/generating-function-gallery.md)] - the polynomials `num_k`, `den_k`, `char_k` and their roots.
- [[plastic-number](pages/plastic-number.md)] - `ψ` and `ψ²`, the Padovan and Perrin numbers, and the Jacobi-Perron expansions.
- [[castle-eigenvalue-oeis-crosswalk](pages/castle-eigenvalue-oeis-crosswalk.md)] - where `ρ_6 = 2ψ²` and the units `ρ_k/2` for `k ≡ 2 (mod 4)` were first found numerically.
- [[castle-sign-kms-matrix](pages/castle-sign-kms-matrix.md)] - the transfer matrix with a weight `t` per block and its similarity to the Kac-Murdock-Szegő matrix, which accounts for `JD`.
- [[hardin-word-identity](pages/hardin-word-identity.md)] and [[hardin-identity-seminar](pages/hardin-identity-seminar.md)] - the proof of the even-sector identity for `m ≤ 8`, and the seminar on it.
- [[char-k-eisenstein-at-two](pages/char-k-eisenstein-at-two.md)] - the irreducibility of `char_k` for `k = 2^m − 1`.
- [[castle-ring-spectrum](pages/castle-ring-spectrum.md)] - the sectors as the two components of `Spec Z[x]/(char_k)`; the minor sector `H_2` at `k = 4` gives `Z[ω]`.
- [[recurrence-discovery](pages/recurrence-discovery.md)] - the order `k + 1` of the recurrence in `L`, which the sector dimensions split.
- [[signed-tower-k-direction](pages/signed-tower-k-direction.md)] - the recurrences of `P(·, L)` in `k`, whose eigenvalues are `±1`.
- [[castle-sign](pages/castle-sign.md)] - the sign `(−1)^{blocks}` and the block count as total descent.
- [[spectral-analysis](pages/spectral-analysis.md)] - the transfer-matrix spectrum among the spectra of a castle.
- [[metallic-means](pages/metallic-means.md)] and [[castle-classification-growth](pages/castle-classification-growth.md)] - the growth constants of castle families, among which `2ψ²` sits.
- [[finite-fields](pages/finite-fields.md)] and [[mod-p-observatory](pages/mod-p-observatory.md)] - `char_k` reduced modulo `p`, where the sector factors reduce too.
- [[new-sequence-fw3](pages/new-sequence-fw3.md)] - `A^e(w, 3)`, whose recurrence has order 6 because the factor `λ − 2` of `char_2 = (λ − 2)(λ² − λ + 2)` also comes from the term `2^w`.
- [[aocp-generating-permutations-tuples](pages/aocp-generating-permutations-tuples.md)] - Knuth's Algorithm M, the mixed-radix enumeration of `{0, …, k}^L` that the brute-force checks run.
- [[castle-notation](pages/castle-notation.md)] - the tower height `k = h − 1` and the argument orders of `P(k, L)` and `A^e(w, h)`.
- [[tower-heap](pages/tower-heap.md)] - towers counted by blocks without sign, through Narayana polynomials.
- [[oeis-mining-pe502](pages/oeis-mining-pe502.md)] - the castle counts matched against the OEIS, among them the characteristic polynomials of `P(k, ·)`.

## Footnotes

[^1]: Verified by execution (Python 3.11 with SymPy and NumPy, 2026-10-16). (i) `JD·M̃_k = M̃_k·JD`, `(JD)² = (−1)^k I` and `JD·M̃_k·JD = (−1)^k M̃_k` for `k ≤ 30`; `char(M̃_k) = char_k` for `k ≤ 16`; `P(k, L) = e_0ᵀ M̃_k^L v` against the sum over towers for `k ≤ 4`, `L ≤ 5`. (ii) The sector polynomials of `M̃_k` for even `k ≤ 40`: `H_{k/2}` in the `+1` sector exactly when `k ≡ 2 (mod 4)`, and the root of largest modulus in the `+1` sector. (iii) `P_even`, `P_odd` by enumeration against the matrix for `k = 2, 4, 6`, `L ≤ 4`. (iv) Equation (1) for `k ≤ 40`; `H_{d+2} = −H_{d+1} + μ² H_d` for `d ≤ 40`; Equation (2) for `d ≤ 20`. (v) `H_d` and `V_d` irreducible, `V_d` primitive, for `d ≤ 20`; `H_d(±1)` and the constant terms for `d < 30`; `char_k` irreducible for odd `k ≤ 31`; the factor table and the coefficient lists for even `k ≤ 26`. (vi) `P_even(4m+2, L)/2^L` against `hardin_count(m, L+1)` for the stated lengths; the sector tables for `L ≤ 12`. (vii) The resultants and the reductions modulo 2 for `d ≤ 15`.
[^2]: [[project-euler-502-castle-factoring](pages/project-euler-502-castle-factoring.md)] §"The sign of a castle" L104-108 - "In the column-height form, the block count is the total descent: blocks = ∑_{i=0}^{L} max(0, c_i - c_{i+1}), c_0 = c_{L+1} = 0".
[^3]: https://oeis.org/A146559, https://oeis.org/A009545, https://oeis.org/A107920, https://oeis.org/A010892 (read 2026-10-16) - A146559: "Expansion of (1-x)/(1 - 2*x + 2*x^2)", `1, 1, 0, -2, -4, -4, 0, 8, 16, 16, 0, -32`; A009545: "Expansion of e.g.f. sin(x)*exp(x)", `0, 1, 2, 2, 0, -4, -8, -8, 0, 16`; A107920: "Lucas and Lehmer numbers with parameters (1 +- sqrt(-7))/2", `0, 1, 1, -1, -3, -1, 5, 7, -3, -17`; A010892: "Inverse of 6th cyclotomic polynomial. A period 6 sequence", `1, 1, 0, -1, -1, 0, …`, offset 0.
[^4]: Verified by execution (Python 3.11 with SymPy, 2026-10-25): from the update of `num_k` and `den_k`, the constant term of `char_k` is `(−1)^{k+1} 2^k` for `k ≤ 20`.
[^5]: [[project-euler-502-solution](pages/project-euler-502-solution.md)] §"The rational-function path (h ≤ 15000)" L132-138 - "num_k(x) = 2·den_{k-1}(x) - num_{k-1}(x); den_k(x) = den_{k-1}(x)·(1 - 2x) + num_{k-1}(x)·x". The recurrence `den_{k+1} = den_{k−1} − 2x·den_k`, equivalently `char_{k+1} = λ² char_{k−1} − 2 char_k`, follows by the Cayley-Hamilton theorem ([[signed-tower-count](pages/signed-tower-count.md)]).
[^6]: Verified by execution (SymPy, 2026-10-16): `resultant(x³ − x − 1, μ − x², x)` is `μ³ − 2μ² + μ − 1 = H_3` up to sign, and `2³ H_3(λ/2) = λ³ − 4λ² + 4λ − 8`, the cubic factor of `char_6`.
[^7]: Verified by execution (Python 3.11 with SymPy, 2026-10-22): with `H_d` as in the section *The monic factor* and `V_d = H_{d+1} + μ² H_{d−1}`, the resultant in `λ` of `2^d H_d(λ/2)` and `2^d V_d(λ/2)` is `±2^{d(d+1)}` (4, 64, 4096 at `d = 1, 2, 3`), and their reductions modulo 2 are `λ^d` and `λ^d(λ + 1)`, for `d ≤ 15`.
[^8]: https://oeis.org/A005251, https://oeis.org/A202882, https://oeis.org/A203094, https://oeis.org/A203184 (read 2026-10-16) - A005251, offset 0: "For n>=3, a(n) is the number of binary strings of length n-2 without any maximal runs of ones of length 1"; A202882, offset 1: "Number of n X 1 0..2 arrays with every nonzero element less than or equal to some horizontal or vertical neighbor", `1, 3, 9, 22, 51, 121, 292, 704, 1691, 4059, 9749`, "Empirical: a(n) = 3*a(n-1) -3*a(n-2) +4*a(n-3) -a(n-4) +a(n-5)"; A203094: "Number of nX1 0..3 arrays with every nonzero element less than or equal to some horizontal or vertical neighbor", `1, 4, 16, 50, 144, 422, 1268, 3823, 11472, 34350`, "Empirical: a(n) = 4*a(n-1) -6*a(n-2) +10*a(n-3) -5*a(n-4) +6*a(n-5) -a(n-6) +a(n-7)"; A203184: "Number of n X 1 0..4 arrays with every nonzero element less than or equal to some horizontal or vertical neighbor", `1, 5, 25, 95, 325, 1121, 3985, 14288, 50995, 181336`, "Empirical: a(n) = 5*a(n-1) -10*a(n-2) +20*a(n-3) -15*a(n-4) +21*a(n-5) -7*a(n-6) +8*a(n-7) -a(n-8) +a(n-9)". The three empirical recurrences are the coefficient lists of `H_5`, `H_7`, `H_9`.
