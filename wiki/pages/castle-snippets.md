---
title: Castle snippets — Python one-liners
category: Concepts
summary: A living reference of short, tested Python snippets for enumerating castles, testing classification predicates, computing growth constants, continued-fraction convergents, mod-p eigenvalue orders, quasi-polynomial splits, and looking up OEIS sequences. Every snippet ran during ingest; outputs pinned to the values shown.
tags: [concept, castle, python, snippets, computational, classification, reference]
sources: [project-euler-502-brute-force]
created: 2026-09-16
updated: 2026-09-17
---

# Castle snippets — Python one-liners

## What this is

A living reference of **short, tested Python snippets** for exploring castles computationally. Each snippet:

- Runs in a plain Python REPL (no external deps unless one line justifies the import — `itertools`, `math`).
- Follows the wiki's conventions: skyline `c = (c_1, …, c_w)` with `1 ≤ c_i ≤ h` and `max c = h` matches [[castle-representations](pages/castle-representations.md)]; block count matches [[castle-sign](pages/castle-sign.md)] and [[project-euler-502-brute-force](pages/project-euler-502-brute-force.md)]; classification names match [[castle-classification](pages/castle-classification.md)].
- Was **executed during ingest**; every printed output is pinned. If a snippet's output disagrees with what this page shows, the wiki is wrong — file a fix.

The purpose is not derivations or full implementations (see [[castle-counting-formula](pages/castle-counting-formula.md)], [[kitamasa](pages/kitamasa.md)], [[project-euler-502-brute-force](pages/project-euler-502-brute-force.md)] for those). The purpose is: **"the wiki mentions class X; here is a two-line function that generates it."**

## Enumeration primitives

### `all_castles(w, h)` → list of skylines

Every castle of width `w` and exact height `h`.

```python
from itertools import product

def all_castles(w, h):
    return [c for c in product(range(1, h+1), repeat=w) if max(c) == h]
```

```
>>> len(all_castles(4, 2))
15
>>> all_castles(2, 2)
[(1, 2), (2, 1), (2, 2)]
```

Wiki tie: [[castle-representations](pages/castle-representations.md)] integer-tuple encoding; [[castle-polyomino](pages/castle-polyomino.md)] definition.

### `blocks(c)` → int

Block count under the wiki convention (matches [[castle-sign](pages/castle-sign.md)] and the `p_signed` DP on [[project-euler-502-brute-force](pages/project-euler-502-brute-force.md)]).

```python
def blocks(c):
    return c[0] + sum(max(0, c[i] - c[i-1]) for i in range(1, len(c)))
```

```
>>> blocks((2, 1, 2))
3
>>> blocks((1, 2, 1))
2
>>> blocks((3, 1, 2, 1))
4
```

### `area(c)` → int

Total cell count `∑ c_i`. The natural size axis for area-graded classifications on [[castle-by-area](pages/castle-by-area.md)].

```python
def area(c):
    return sum(c)
```

```
>>> area((2, 1, 2))
5
```

### `castles_where(w, h, pred)` → list of skylines

Filter all castles at `(w, h)` by any predicate.

```python
def castles_where(w, h, pred):
    return [c for c in all_castles(w, h) if pred(c)]
```

```
>>> len(castles_where(4, 2, is_unimodal))
10
```

Matches [[convex-castle-binomial-identity](pages/convex-castle-binomial-identity.md)]: `C(2h+w-3, w-1) = C(5,3) = 10`.

## Hand-check: `F(4, 2) = 10`

Reproduce the [[castle-counting-function](pages/castle-counting-function.md)] value on the smallest interesting case using only the primitives above.

```python
even = sum(1 for c in all_castles(4, 2) if blocks(c) % 2 == 0)
```

```
>>> even
10
```

Also matches the [[castle-counting-formula](pages/castle-counting-formula.md)] `F(4,2) = ½(16 − 1 + 4 + 1) = 10` and the [[castles-as-upgraded-cycle-count](pages/castles-as-upgraded-cycle-count.md)] hand check.

## Classification predicates — Axes 1-7 of [[castle-classification]]

Each predicate takes a skyline `c` (a tuple or list of positive ints) and returns `bool`. Some also take `h` when the type is parameterized by height.

### Axis 1: Convexity / modality

```python
def is_unimodal(c):
    """Weakly rises to a peak, then weakly falls."""
    i = c.index(max(c))
    return (all(c[j] <= c[j+1] for j in range(i))
        and all(c[j] >= c[j+1] for j in range(i, len(c)-1)))

def is_ferrers(c):
    return all(c[i] >= c[i+1] for i in range(len(c)-1))

def is_reverse_ferrers(c):
    return all(c[i] <= c[i+1] for i in range(len(c)-1))

def is_staircase(c):
    """Ferrers with all heights distinct."""
    return is_ferrers(c) and len(set(c)) == len(c)

def is_strictly_unimodal(c):
    i = c.index(max(c))
    return (all(c[j] < c[j+1] for j in range(i))
        and all(c[j] > c[j+1] for j in range(i, len(c)-1)))
```

```
>>> is_unimodal([1,2,3,2,1])
True
>>> is_unimodal([1,3,2,3])
False
>>> is_ferrers([3,3,2,1])
True
>>> is_ferrers([1,2,3])
False
>>> is_reverse_ferrers([1,2,3])
True
>>> is_staircase([3,2,1])
True
>>> is_staircase([3,3,2,1])
False
```

Wiki ties: [[convex-castle](pages/convex-castle.md)] (unimodal), [[polyominoes](pages/polyominoes.md)] (Ferrers/staircase in the taxonomy), [[castle-classification](pages/castle-classification.md)] Axis 1.

### Axis 2: Rate of change

```python
def is_m_smooth(c, m=1):
    """|c_{i+1} - c_i| <= m for all i."""
    return all(abs(c[i+1] - c[i]) <= m for i in range(len(c)-1))

def is_m_disparate(c, m=1):
    """|c_{i+1} - c_i| >= m for all i."""
    return all(abs(c[i+1] - c[i]) >= m for i in range(len(c)-1))

def is_plateau_free(c):
    return all(c[i] != c[i+1] for i in range(len(c)-1))
```

```
>>> is_m_smooth([1,2,1,2], 1)
True
>>> is_m_smooth([1,3,1,3], 1)
False
>>> is_m_disparate([1,3,1,3], 2)
True
```

Wiki ties: [[castle-classification](pages/castle-classification.md)] Axis 2. Note `is_m_smooth(c, 1)` is exactly the **Motzkin-path** predicate for the interior — see Axis 3 below.

### Axis 3: Path-like

```python
def is_dyck_path(c, h):
    """c_1 = c_w = 1, min = 1, |Delta| = 1 always."""
    return (c[0] == 1 and c[-1] == 1 and min(c) == 1
        and all(abs(c[i+1] - c[i]) == 1 for i in range(len(c)-1)))

def is_motzkin_path(c):
    """|Delta| <= 1 always (Dyck-path with flat steps allowed)."""
    return all(abs(c[i+1] - c[i]) <= 1 for i in range(len(c)-1))
```

```
>>> is_dyck_path((1,2,1,2,1), 2)
True
>>> is_motzkin_path((1,2,2,1,1))
True
```

Wiki ties: [[dyck-words](pages/dyck-words.md)], [[motzkin-numbers](pages/motzkin-numbers.md)], [[tower-word-continued-fraction](pages/tower-word-continued-fraction.md)].

### Axis 4: Symmetry

```python
def is_palindromic(c):
    return list(c) == list(c)[::-1]

def is_centrally_symmetric(c, h):
    """c_i + c_{w+1-i} = h + 1 (180-degree rotation inside bounding box)."""
    w = len(c)
    return all(c[i] + c[w-1-i] == h + 1 for i in range(w))
```

```
>>> is_palindromic([1,2,3,2,1])
True
>>> is_centrally_symmetric([1,2,3], 3)
True
```

Wiki tie: [[castle-classification](pages/castle-classification.md)] Axis 4.

### Axis 5: Extremum / value patterns

```python
def is_rainbow(c, h):
    """w = h, heights are a permutation of {1,...,h}."""
    return len(c) == h and sorted(c) == list(range(1, h+1))

def is_boxcastle(c, h):
    return all(x == h for x in c)

def is_hook(c, h):
    """c_1 = h, c_i = 1 for i >= 2 (Young-diagram hook)."""
    return c[0] == h and all(x == 1 for x in c[1:])
```

```
>>> is_rainbow((1,3,2), 3)
True
>>> is_rainbow((1,1,2), 3)
False
>>> is_boxcastle((3,3,3), 3)
True
>>> is_hook((3,1,1,1), 3)
True
```

Wiki ties: [[castle-classification](pages/castle-classification.md)] Axis 5. **Rainbow castles are in bijection with `S_h`** — the [[castles-as-upgraded-cycle-count](pages/castles-as-upgraded-cycle-count.md)] triad applies directly (not as an upgrade) to this class.

### Axis 8: growth-type predicate skeleton — the {0, 1}-strip

The [[pell-castle-strip](pages/pell-castle-strip.md)]-style predicates encode the "state above the base" (0 = empty column, 1 = height-1 tower cell). See [[castle-classification](pages/castle-classification.md)] Axis 8 for the meta-classification these strips instantiate.

```python
def is_zero_one_strip(c):
    """Golden width growth castle predicate: c in {0,1}^w, no adjacent 1s."""
    return (all(x in (0, 1) for x in c)
        and all(not (c[i] == 1 and c[i+1] == 1) for i in range(len(c)-1)))
```

```
>>> is_zero_one_strip([1,0,1,0])
True
>>> is_zero_one_strip([1,1,0])
False
```

Wiki tie: [[castle-classification](pages/castle-classification.md)] Axis 8 — the {0,1}-strip is a golden width growth castle; its count sequence is Fibonacci `F_{w+2}`.

## Axis 8: growth-constant probes

Test whether a count sequence has a metallic-mean growth constant (see [[metallic-means](pages/metallic-means.md)]) and identify which `<metal>` if so.

```python
import math

def growth_constant(seq, tail=5):
    """Estimate the growth ratio from the last `tail` consecutive ratios."""
    ratios = [seq[i+1]/seq[i] for i in range(len(seq)-1) if seq[i] > 0]
    return sum(ratios[-tail:]) / tail

def nearest_metallic(r, max_a=6):
    """Which delta_a = (a + sqrt(a^2+4))/2 (a = 1..max_a) is closest to r?"""
    return min(range(1, max_a+1),
               key=lambda a: abs(r - (a + math.sqrt(a*a + 4))/2))
```

```
>>> pell = [1, 2, 5, 12, 29, 70, 169, 408, 985, 2378]
>>> f"{growth_constant(pell):.6f}"
'2.414142'
>>> nearest_metallic(growth_constant(pell))
2

>>> fib = [1, 2, 3, 5, 8, 13, 21, 34, 55]
>>> f"{growth_constant(fib):.6f}"
'1.615416'
>>> nearest_metallic(growth_constant(fib))
1
```

Meaning: Pell → `a=2` (silver, `1+√2 ≈ 2.4142`). Fibonacci → `a=1` (golden, `φ ≈ 1.6180`). The sequence a candidate silver / golden / bronze / … *width* growth castle would produce, in the sense of [[castle-classification](pages/castle-classification.md)] Axis 8.

**Cautions:**
- `growth_constant` estimates from **width**-graded sequences; use the appropriate size-axis sequence for vertical / area / block growth castles (see [[castle-classification](pages/castle-classification.md)] Axis 8).
- `nearest_metallic` always returns *some* answer — even a transcendental growth constant will return the closest metallic mean. Check the actual distance if uncertain:

```python
>>> trib = [1, 1, 2, 4, 7, 13, 24, 44, 81, 149]  # Tribonacci-like
>>> r = growth_constant(trib); r
1.8434087882822903
>>> a = nearest_metallic(r); a, (a + math.sqrt(a*a+4))/2, abs(r - (a + math.sqrt(a*a+4))/2)
(1, 1.618033988749895, 0.22537479953239528)
```

A gap of ~0.225 is *not* a metallic-mean hit — this is honestly not a `δ_a`-castle for small `a`. `nearest_metallic` gives the closest metal; only trust it when the residual is small.

## Continued fractions, convergents, and quasi-polynomials

Snippets behind [[convergents-oeis-crosswalk](pages/convergents-oeis-crosswalk.md)] and [[eigenvalue-continued-fractions](pages/eigenvalue-continued-fractions.md)]. The first three are stdlib-only; `quasi_split` needs SymPy (the one import that earns its keep here).

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

### `quasi_split(seq, deg)` → `(A, B)` with `seq[k] = (−1)^k A(k) + B(k)`

Two Lagrange interpolations (even `k`, odd `k`) - all you need when every eigenvalue is `±1`, which is the case for the k-direction of `P` ([[convergents-oeis-crosswalk](pages/convergents-oeis-crosswalk.md)]). Requires SymPy.

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

```python
from math import comb
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

### `castle_graph(c)` → adjacency matrix

Adjacency matrix of the castle's polyomino graph - the [[castle-graph](pages/castle-graph.md)] object; every Axis 9 spectrum takes this matrix as input.

```python
import numpy as np

def castle_graph(c):
    cells = [(i, j) for i, h in enumerate(c) for j in range(h)]
    idx = {cell: n for n, cell in enumerate(cells)}
    A = np.zeros((len(cells), len(cells)))
    for (i, j), u in idx.items():
        for nb in ((i+1, j), (i, j+1)):
            if nb in idx: A[u, idx[nb]] = A[idx[nb], u] = 1
    return A
```

```
>>> castle_graph((2, 1, 2)).astype(int).tolist()      # 5 cells arranged as two spikes on a base
[[0, 1, 1, 0, 0], [1, 0, 0, 0, 0], [1, 0, 0, 1, 1], [0, 0, 1, 0, 0], [0, 0, 1, 0, 0]]
```

Meaning: swap in `L = np.diag(A.sum(1)) - A` for the combinatorial Laplacian; feed to `numpy.linalg.eigvalsh` for the spectrum; feed to `sympy.Matrix(...).charpoly(x)` for the exact characteristic polynomial. All Axis 9 predicates on [[castle-classification](pages/castle-classification.md)] are one line off this.

### `is_tree_castle(c)` / `cycle_rank(c)` → tree predicate and cycle rank

The castle is a tree iff no `2 × 2` block is filled, iff no two horizontally adjacent columns both have height at least 2. Cycle rank `|E| − |V| + 1` equals the number of `2 × 2` filled blocks - a Euler-formula identity for the [[castle-graph](pages/castle-graph.md)].

```python
def is_tree_castle(c):
    return all(not (c[i] >= 2 and c[i+1] >= 2) for i in range(len(c)-1))

def cycle_rank(c):
    return sum(max(0, min(c[i], c[i+1]) - 1) for i in range(len(c)-1))
```

```
>>> [c for c in all_castles(3, 2) if is_tree_castle(c)]
[(1, 1, 2), (1, 2, 1), (2, 1, 1), (2, 1, 2)]
>>> is_tree_castle((2, 2)), cycle_rank((2, 2)), cycle_rank((3, 3)), cycle_rank((1, 2, 3, 1, 2, 3))
(False, 1, 2, 2)
>>> [sum(1 for c in product(range(1, 3), repeat=w) if is_tree_castle(c)) for w in range(1, 9)]
[2, 3, 5, 8, 13, 21, 34, 55]
```

Meaning: the last line is `F_{w+2}` for `w = 1..8`. Tree castles of height at most 2 are counted by Fibonacci (offset 2); Jacobsthal A001045 counts height at most 3; the k-Fibonacci family A006130, A006131 counts higher `h`. All catalogued on [[castle-graph](pages/castle-graph.md)].

### `castle_to_composition(c)` / `composition_to_castle(parts)` → bijection with compositions

The three-way bijection tree castle ↔ composition of `A + 1` with parts in `{1, 3, 4, 5}` ↔ SUD tournament on `A + 1` nodes ([[tree-castle-by-area](pages/tree-castle-by-area.md)]).

```python
def castle_to_composition(c):
    aug = [1] + list(c); parts = []; i = 0
    while i < len(aug):
        if i + 1 < len(aug) and aug[i] == 1 and aug[i + 1] >= 2:
            parts.append(1 + aug[i + 1]); i += 2
        else:
            parts.append(aug[i]); i += 1
    return tuple(parts)

def composition_to_castle(parts):
    aug = []
    for p in parts:
        if p == 1: aug.append(1)
        elif p in (3, 4, 5): aug.extend([1, p - 1])
        else: raise ValueError(f'unexpected part {p}')
    return tuple(aug[1:])
```

```
>>> castle_to_composition((1, 2, 1))
(3, 1)
>>> composition_to_castle((3, 1))
(1, 2, 1)
>>> castle_to_composition((4,))
(1, 4)
>>> composition_to_castle((1, 4))
(4,)
```

Meaning: prepending a virtual `1` column and merging each `(1, tall)` pair produces the composition; the inverse expands each part `k ∈ {3, 4, 5}` back into `(1, k − 1)` and drops the leading `1`.

### `is_strongly_connected(T)` → SCC test for tournament matrices

```python
def is_strongly_connected(T):
    n = len(T)
    def reach(adj, start):
        seen = {start}; stack = [start]
        while stack:
            u = stack.pop()
            for v in range(n):
                if adj[u][v] and v not in seen:
                    seen.add(v); stack.append(v)
        return seen
    Tt = [[T[j][i] for j in range(n)] for i in range(n)]
    return len(reach(T, 0)) == n and len(reach(Tt, 0)) == n
```

Meaning: forward and backward reachability from a single vertex - a valid SCC test for tournaments since every pair has an edge in some direction, so 0-reachability determines connectivity. Used in the classification of strongly connected score-uniquely-determined tournaments ([[tree-castle-by-area](pages/tree-castle-by-area.md)]).

### `tree_area_gf(h, W)` / `tree_area_by_area(h, A_max)` → area-graded tree castle counts

Bivariate GF for tree castles by width and area, and the area-only sequence at fixed height ([[tree-castle-by-area](pages/tree-castle-by-area.md)]). Requires SymPy.

```python
import sympy as sp
x, q = sp.symbols('x q')

def P_h(h):
    return sum(q**i for i in range(2, h+1)) if h >= 2 else sp.Integer(0)

def tree_area_gf(h, W):
    T = sp.series((1 + P_h(h)*x) / (1 - q*x - q*P_h(h)*x**2), x, 0, W+1).removeO()
    return [sp.expand(T.coeff(x, w)) for w in range(W+1)]

def tree_area_by_area(h, A_max):
    Ph = P_h(h)
    S = sp.series((1 + Ph) / (1 - q - q*Ph), q, 0, A_max+1).removeO()
    return [int(S.coeff(q, A)) for A in range(A_max+1)]
```

```
>>> tree_area_by_area(2, 15)                       # Narayana's cows A000930(A+1)
[1, 1, 2, 3, 4, 6, 9, 13, 19, 28, 41, 60, 88, 129, 189, 277]
>>> tree_area_by_area(3, 15)                       # A006498(A+1), golden growth via cyclotomic factor
[1, 1, 2, 4, 6, 9, 15, 25, 40, 64, 104, 169, 273, 441, 714, 1156]
>>> [int(coef) for coef in [c.subs(sp.Symbol('q'), 1) for c in tree_area_gf(2, 8)]]  # Fibonacci: T_h(w, 1) at h=2
[1, 2, 3, 5, 8, 13, 21, 34, 55]
```

Meaning: the h=∞ (unlimited height) case is A005251(A+2), the same plastic-squared sequence that appears in the Hardin identity for `P_even(6, L)` - two independent castle interpretations of A005251 meeting at the same recurrence.

### `castle_graph_radius(c)` → float

Largest adjacency eigenvalue of the castle's polyomino graph (cells as vertices, orthogonal neighbors as edges) - the Axis 9 statistic of [[castle-classification](pages/castle-classification.md)] and the census on [[castle-graph-spectral-radius](pages/castle-graph-spectral-radius.md)]. Requires NumPy.

```python
import numpy as np

def castle_graph_radius(c):
    cells = [(i, j) for i, h in enumerate(c) for j in range(h)]
    idx = {cell: n for n, cell in enumerate(cells)}
    A = np.zeros((len(cells), len(cells)))
    for (i, j), n in idx.items():
        for nb in ((i+1, j), (i, j+1)):
            if nb in idx: A[n, idx[nb]] = A[idx[nb], n] = 1
    return np.linalg.eigvalsh(A)[-1]
```

```
>>> round(castle_graph_radius((1, 1, 1, 1)), 6)      # P_4: phi
1.618034
>>> round(castle_graph_radius((2, 2, 2)), 6)         # 3x2 rectangle: 1 + sqrt(2)
2.414214
>>> round(castle_graph_radius((1, 2, 3, 1, 2, 3)), 6)
2.414214
>>> [c for c in all_castles(3, 2) if abs(castle_graph_radius(c) - (1 + 2**.5)) < 1e-9]
[(2, 2, 2)]
```

Meaning: `(1,1,1,1)` is a golden-spectrum castle, `(2,2,2)` and `(1,2,3,1,2,3)` are silver-spectrum castles. Combine with `castles_where` to census a spectral predicate; swap `eigvalsh(A)[-1]` for the full spectrum (or `np.diag(A.sum(1)) - A` for the Laplacian) to hunt isospectral pairs.

### `compositions(n)` → all castles with exactly `n` cells

A castle with `n` cells is a composition of `n` (every column height `≥ 1`), so size-by-cells enumeration is `2^{n−1}` skylines regardless of `w, h` - the right loop for isospectral searches ([[isospectral-castles](pages/isospectral-castles.md)]).

```python
def compositions(n):
    if n == 0: yield (); return
    for first in range(1, n+1):
        for rest in compositions(n-first): yield (first,) + rest
```

```
>>> list(compositions(3))
[(1, 1, 1), (1, 2), (2, 1), (3,)]
>>> sum(1 for c in compositions(10) if not c[::-1] < c)      # mirror-deduped 10-cell castles
272
```

### `word_matrix(m)` → transfer matrix of Hardin's no-local-maximum words

Words over `{0..m}` in which every nonzero letter is `≤` a neighbor, counted by a `2m+1`-state automaton with a "pending" flag ([[hardin-word-identity](pages/hardin-word-identity.md)]). Requires SymPy.

```python
def word_matrix(m):
    S = [(0, '+')] + [(a, s) for a in range(1, m+1) for s in ('+', '-')]; idx = {s: i for i, s in enumerate(S)}
    W = sp.zeros(len(S), len(S))
    for (a, flag) in S:
        for b in range(m+1):
            if flag == '-' and b < a: continue
            new = (0, '+') if b == 0 else ((b, '+') if b <= a else (b, '-'))
            W[idx[(a, flag)], idx[new]] += 1
    return W, S
```

```
>>> W, S = word_matrix(2); start = sp.Matrix(1, 5, [1, 0, 0, 0, 0]); end = sp.Matrix([1 if s[1] == '+' else 0 for s in S])
>>> [int((start*W**n*end)[0]) for n in range(1, 10)]          # A202882
[1, 3, 9, 22, 51, 121, 292, 704, 1691]
>>> sp.factor(W.charpoly(mu).as_expr())                        # = H(5)
mu**5 - 3*mu**4 + 3*mu**3 - 4*mu**2 + mu - 1
```

Meaning: the count equals `P_even(10, n−1)/2^{n−1}`, the even-last-column signed tower count at height 10 - the Hardin identity.

### `oeis_lookup(terms)` → list of `(A-number, name)`

The live version of `oeis_snippet` below. **OEIS answers Python's default `urllib` User-Agent with HTTP 403**; go through `curl` with a real UA and sleep a second between calls.

```python
import json, subprocess, urllib.parse

def oeis_lookup(terms, n=3):
    q = ",".join(str(t) for t in terms)
    url = "https://oeis.org/search?" + urllib.parse.urlencode({"q": q, "fmt": "json"})
    raw = subprocess.run(["curl", "-s", "-m", "30", "-A", "Mozilla/5.0 castles-wiki-verifier/1.0", url],
                         capture_output=True, text=True).stdout
    return [(f"A{e['number']:06d}", e["name"]) for e in (json.loads(raw) or [])[:n]]
```

```
>>> oeis_lookup([1, 2, 5, 12, 29, 70, 169, 408, 985, 2378])[0]
('A000129', 'Pell numbers: a(0) = 0, a(1) = 1; for n > 1, a(n) = 2*a(n-1) + a(n-2).')
>>> oeis_lookup([1, 4, 19, 40, 85, 140, 231, 336, 489, 660])
[('A352116', 'Partial sums of the odd triangular numbers (A014493).')]
>>> oeis_lookup([1, 2, 4, 7, 12, 21, 37, 65, 114, 200, 351, 616])
[('A005251', 'a(0) = 0, a(1) = a(2) = a(3) = 1; thereafter, a(n) = a(n-1) + a(n-2) + a(n-4).')]
```

Discipline reminder from [[oeis-cross-referencing](pages/oeis-cross-referencing.md)]: a hit is a *candidate* until you compare against the full stored `data` field with the offset - fetch `https://oeis.org/search?q=id:A005251&fmt=json` and read `offset` and `data` before writing anything down.

## OEIS lookup helper

Format a sequence for pasting into `oeis.org`.

```python
def oeis_snippet(seq, n=10):
    return ", ".join(str(x) for x in seq[:n])
```

```
>>> oeis_snippet([1, 2, 5, 12, 29, 70, 169, 408, 985, 2378])
'1, 2, 5, 12, 29, 70, 169, 408, 985, 2378'
```

Combined with `all_castles` + `blocks` this is the [[oeis-mining-pe502](pages/oeis-mining-pe502.md)] loop in a one-liner. Example: even-block castle count `F(w, 2)` for `w = 1..8`:

```python
>>> oeis_snippet([sum(1 for c in all_castles(w, 2) if blocks(c) % 2 == 0)
...               for w in range(1, 9)])
'1, 3, 6, 10, 16, 28, 56, 120'
```

Paste that into `oeis.org` to check for known-sequence hits (this one lands on the [[oeis-height2-hyperbolic-castles](pages/oeis-height2-hyperbolic-castles.md)] hyperbolic family — height-2 castles are `A038505(w+1)`).

## Extension patterns

The snippets above are intentionally minimal. Common extensions the reader may want:

- **Compose predicates:** filter under multiple axes with `castles_where(w, h, lambda c: is_unimodal(c) and blocks(c) % 2 == 0)`.
- **Distributions instead of counts:** replace `sum(1 for c in ... if pred)` with a `collections.Counter` on some statistic (block count, area, peak count).
- **Larger `w, h`:** `all_castles(w, h)` builds `h^w` tuples; expect it to hit the wall around `w * log(h) ≈ 20`. For larger parameters the DP on [[project-euler-502-brute-force](pages/project-euler-502-brute-force.md)] is what to reach for; the fast algorithms on [[castle-count-algorithms](pages/castle-count-algorithms.md)] handle trillion-scale inputs.
- **Bijective constructions:** build a skyline from a step string ([[urd-step-strings](pages/urd-step-strings.md)]) or a binary run pattern ([[binary-string-bijection](pages/binary-string-bijection.md)]); these are two-line functions the wiki has not yet snippeted.

## Discipline: how to add snippets to this page

1. **Write the snippet in a scratch script.** No exception, ever.
2. **Run it.** Capture the output.
3. **Only after** you have the actual output, paste both snippet and output into this page. The output shown must be what the snippet actually produced — never a hand-computed expectation.
4. **Cross-reference the wiki page** the snippet supports. A snippet without a wiki-page tie-in is a snippet in search of a purpose.

Snippets that break this discipline will rot; snippets that follow it stay useful.

## Appearances in Sources

- [[project-euler-502-brute-force](pages/project-euler-502-brute-force.md)] — the `p_signed` DP, `blocks_of`, and `is_unimodal` reference implementations the wiki-convention snippets above match.

## Related Concepts

- [[castle-classification](pages/castle-classification.md)] — the classification framework the predicates instantiate.
- [[castle-representations](pages/castle-representations.md)] — the skyline encoding all snippets predicate on.
- [[castle-sign](pages/castle-sign.md)] — the block-count convention `blocks(c)` matches.
- [[metallic-means](pages/metallic-means.md)] — the family `nearest_metallic` tests against.
- [[pell-castle-strip](pages/pell-castle-strip.md)] — the silver-width-growth-castle example; the `is_zero_one_strip` predicate is its `w_1 = 1` analog for golden.
- [[oeis-mining-pe502](pages/oeis-mining-pe502.md)] — the OEIS-lookup loop the `oeis_snippet` helper feeds.
- [[convergents-oeis-crosswalk](pages/convergents-oeis-crosswalk.md)] - the analysis the continued-fraction / mod-p / quasi-polynomial snippets were written for; every pinned value here matches that page.
- [[tower-parity-sectors](pages/tower-parity-sectors.md)] / [[plastic-number](pages/plastic-number.md)] - the transfer-matrix, sector, and `H(d)` snippets.
- [[castle-graph](pages/castle-graph.md)] - the `castle_graph`, `is_tree_castle`, `cycle_rank` snippets and the graph concept behind them.
- [[tree-castle-by-area](pages/tree-castle-by-area.md)] - the `tree_area_gf`, `tree_area_by_area` snippets.
- [[castle-graph-spectral-radius](pages/castle-graph-spectral-radius.md)] - the `castle_graph_radius` census.
- [[isospectral-castles](pages/isospectral-castles.md)] / [[hardin-word-identity](pages/hardin-word-identity.md)] - the `compositions` and `word_matrix` snippets.
- [[eigenvalue-continued-fractions](pages/eigenvalue-continued-fractions.md)] / [[mod-p-observatory](pages/mod-p-observatory.md)] - the two sides (real periods, finite-field orders) that `convergents` and `order_mod` compute.
- [[castle-count-algorithms](pages/castle-count-algorithms.md)] / [[kitamasa](pages/kitamasa.md)] — the fast-algorithm side, one abstraction level up.
