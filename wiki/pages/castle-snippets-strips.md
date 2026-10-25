---
title: Castle snippets - strips and growth
category: Concepts
summary: Tested Python snippets for castle strips (the Pell and ridge strips, the even-block ridge castles, the number field of a strip's growth constant, the tower-spacing rule), growth-constant probes against the metallic means, tree skylines and skylines by area with their bijection to compositions, and the A005251 and Hardin word automata. Every output is rerun; sibling of castle-snippets.
tags: [concept, castle, python, snippets, strip, growth-constant, metallic-mean, tree-castle, hardin]
sources: [project-euler-502-brute-force]
created: 2026-09-19
updated: 2026-10-25
---

# Castle snippets - strips and growth

A sibling page to [[castle-snippets](pages/castle-snippets.md)]: snippets for castle strips, growth-constant probes, tree skylines and skylines by area, and the Hardin word automaton. A strip is a skyline on the heights `{1, …, h}` read left to right under a rule on neighboring columns; it need not reach `h`, so a strip is not a castle, and the strips that reach `h` are the castles of height `h` of the rule's family ([[castle-strip](pages/castle-strip.md)]). Every output on this page was rerun on 2026-10-16 (Python 3.11 with SymPy and NumPy).[^1]

For the number-theoretic snippets that read continued-fraction convergents / mod-`p` orders / signed tower counts off these strips, see [[castle-snippets-number-theory](pages/castle-snippets-number-theory.md)]. For the cryptography snippets built on the signed transfer matrix, see [[castle-snippets-cryptography](pages/castle-snippets-cryptography.md)].

## Strip predicates and growth-constant probes

### `is_zero_one_strip(c)` → the towers of the Fibonacci castles

Write the towers of a castle of height 2 as a 0/1 string, `1` marking a column of height 2, and forbid two neighboring `1`s. The castles whose strings pass are the Fibonacci castles, the tree castles of height 2 ([[fibonacci-castle](pages/fibonacci-castle.md)], [[castle-graph](pages/castle-graph.md)]).

```python
def is_zero_one_strip(c):
    """Towers of a Fibonacci castle: c in {0,1}^w with no two neighboring 1s."""
    return (all(x in (0, 1) for x in c)
        and all(not (c[i] == 1 and c[i+1] == 1) for i in range(len(c)-1)))
```

```
>>> is_zero_one_strip([1,0,1,0])
True
>>> is_zero_one_strip([1,1,0])
False
```

Of length `w` there are `F_{w+2}` such strings, and the `F_{w+2} − 1` that are not all `0` give the Fibonacci castles of width `w`, `A000071(w+2)`, golden by width ([[castle-classification-growth](pages/castle-classification-growth.md)]).

### `pell_strip_count(w)` → the Pell castle strip

The 1-smooth strips on the heights `{1, 2, 3}` (neighboring heights differ by at most 1) whose first column has height 1 ([[pell-castle-strip](pages/pell-castle-strip.md)]). They number the Pell numbers `P⋆_w`, with `Σ_w P⋆_w x^w = x/(1 − 2x − x²)`; with a free first column they number the Pell-Lucas numbers `A001333(w+1)` ([[pell-numbers](pages/pell-numbers.md)]).

```python
from itertools import product

def pell_strip_count(w, anchored=True):
    return sum(1 for c in product((1, 2, 3), repeat=w)
               if (c[0] == 1 or not anchored)
               and all(abs(c[i+1] - c[i]) <= 1 for i in range(w-1)))
```

```
>>> [pell_strip_count(w) for w in range(1, 9)]                  # Pell numbers P*_w, A000129
[1, 2, 5, 12, 29, 70, 169, 408]
>>> [pell_strip_count(w, anchored=False) for w in range(1, 9)]  # Pell-Lucas numbers A001333(w+1)
[3, 7, 17, 41, 99, 239, 577, 1393]
```

Meaning: the anchored strips number `P⋆_w` and the strips with a free first column `A001333(w+1)`; both are silver by width, with growth `1 + √2`.


## Growth-constant probes

`growth_constant` estimates a growth constant from consecutive ratios, and `nearest_metallic` names the nearest metallic mean `δ_a = (a + √(a² + 4))/2` ([[metallic-means](pages/metallic-means.md)]).

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

Meaning: the Pell numbers give `a = 2`, the silver mean `1 + √2 ≈ 2.4142`, and the Fibonacci numbers `a = 1`, the golden mean `φ ≈ 1.6180`.

`growth_constant` reads the grading its sequence has, by width, by area or by semi-perimeter ([[castle-classification-growth](pages/castle-classification-growth.md)]). `nearest_metallic` returns a metallic mean for every input, so the distance has to be checked:

```python
>>> trib = [1, 2, 4, 7, 13, 24, 44, 81, 149, 274]   # skylines of height at most 3 by area, A000073(A+2)
>>> r = growth_constant(trib); r                     # mean of the last 5 ratios; the tribonacci constant is 1.83929
1.8397657235464842
>>> a = nearest_metallic(r); a, (a + math.sqrt(a*a+4))/2, abs(r - (a + math.sqrt(a*a+4))/2)
(1, 1.618033988749895, 0.22173173479658925)
```

The distance 0.222 rules out a metallic mean: the tribonacci constant `1.83929…`, the real root of `x³ = x² + x + 1`, is a cubic irrational, and every `δ_a` is quadratic. The sequence counts the skylines of height at most 3 by area ([[castles-of-height-h-by-area](pages/castles-of-height-h-by-area.md)]; `bounded_castles_by_area(3, ·)` in the section *Tree skylines and skylines by area*).


## Named strip rules

### `ridge_R(h)`, `ridge_count(h, L_max)` → the ridge strips and their metallic means

The **ridge rule** allows two neighboring columns of equal height only at the top height `h`. Its strips of width `w` number `𝟙ᵀ R_h^{w−1} 𝟙`, where the transfer matrix `R_h = J − D` (`J` all ones, `D = diag(1, …, 1, 0)`) has characteristic polynomial `(x + 1)^{h−2}(x² − (h − 1)x − 1)` and largest eigenvalue the metallic mean `δ_{h−1}`; the strips that reach `h` are the ridge castles ([[ridge-castle](pages/ridge-castle.md)], [[metallic-strip-realizability](pages/metallic-strip-realizability.md)]). Bronze `δ_3` comes at `h = 4`, and `δ_4 = φ³` at `h = 5`, where the strips of width `w` number `F_{3w+2}`. `ridge_count(h, L_max)` lists the counts for the widths `w = L + 1`, `L = 0, …, L_max`. Requires SymPy (`import sympy as sp`).

```python
def ridge_R(h):
    # R[a][b] = 1 iff a != b, or a == b == h  (heights 1..h, 0-indexed here)
    return sp.Matrix(h, h, lambda i, j: 1 if (i != j or i == h-1) else 0)

def ridge_count(h, L_max):
    R = ridge_R(h); ones = sp.ones(h, 1)
    return [int((ones.T * R**L * ones)[0]) for L in range(L_max+1)]
```

```
>>> sp.factor(ridge_R(4).charpoly(sp.Symbol('x')).as_expr())   # bronze
(x + 1)**2*(x**2 - 3*x - 1)
>>> ridge_count(4, 6)                        # bronze (3+sqrt13)/2, Q(sqrt13)
[4, 13, 43, 142, 469, 1549, 5116]
>>> ridge_count(5, 8)                        # delta_4 = 2 + sqrt 5 = phi^3: F_{3w+2}, w = 1..9
[5, 21, 89, 377, 1597, 6765, 28657, 121393, 514229]
>>> [sp.factor(ridge_R(h).charpoly(sp.Symbol('x')).as_expr()) for h in range(2,7)]
[x**2 - x - 1, (x + 1)*(x**2 - 2*x - 1), (x + 1)**2*(x**2 - 3*x - 1), (x + 1)**3*(x**2 - 4*x - 1), (x + 1)**4*(x**2 - 5*x - 1)]
```

Meaning: as `h = 2, 3, 4, 5, 6` the largest eigenvalue runs through golden, silver, bronze, `δ_4` and `δ_5`, the metallic mean of order `a = h − 1`; the factor `(x + 1)^{h−2}` gives the eigenvalue `−1` with multiplicity `h − 2`. The `h = 5` row is every third Fibonacci number, `F_{3w+2}`.


### `proper_even(h, Wmax)` → the even-block ridge castles

`ridge_count` counts strips. The ridge castles of height `h` are the strips that reach `h`, and the even-block ones number `A^e_ridge = (A_ridge + S_ridge)/2`, with `S_ridge` the signed count ([[ridge-castle](pages/ridge-castle.md)], [[castle-sign](pages/castle-sign.md)]). `proper_even` subtracts the strips that stay below `h`, which follow the rule `J − I` (neighboring columns differ), and computes `S_ridge = Σ (−1)^{blocks}` with the signed transfer matrix `R̃_h[a][b] = (−1)^{max(0, b−a)} R_h[a][b]` and the start vector `(−1)^{c_1}`, since a column of height `b` after one of height `a` starts `max(0, b − a)` blocks ([[proper-castle-projection](pages/proper-castle-projection.md)]). Requires SymPy.

```python
def proper_even(h, Wmax):
    """Even-block ridge castles: proper castles (max=h) under the ridge rule R_h = J - D.
    Metal a = h-1. Returns counts by width w = 1..Wmax. Requires SymPy."""
    def free(mat):
        n = mat.shape[0]
        ones = sp.ones(n, 1)
        v = sp.Matrix(n, 1, [(-1)**(a+1) for a in range(n)])              # (-1)^height
        Rt = sp.Matrix(n, n, lambda a, b: (-1)**max(0, b-a) * mat[a, b])   # signed matrix R~
        u, s, Mu, Ms = [], [], sp.eye(n), sp.eye(n)
        for _ in range(Wmax):
            u.append(int((ones.T*Mu*ones)[0])); s.append(int((v.T*Ms*ones)[0]))
            Mu, Ms = Mu*mat, Ms*Rt
        return u, s
    JD  = sp.Matrix(h, h, lambda i, j: 1 if (i != j or i == h-1) else 0)   # R_h = J - D
    PF  = sp.Matrix(h-1, h-1, lambda i, j: 1 if i != j else 0)             # J - I (max < h strip)
    uJ, sJ = free(JD); uP, sP = free(PF)
    return [(uJ[w]-uP[w] + sJ[w]-sP[w]) // 2 for w in range(Wmax)]
```

```
>>> proper_even(4, 8)   # h = 4: growth 3.30278, bronze
[1, 7, 25, 70, 209, 697, 2390, 8169]
>>> proper_even(5, 8)   # h = 5: growth 4.23607 = phi^3
[0, 0, 10, 104, 604, 2836, 12630, 55668]
```

Meaning: both rows agree with enumeration of the ridge castles for `w ≤ 7`. Their growth is `δ_{h−1}`, because the spectral radius of `R̃_h`, `1.000, 1.575, 1.768, 2.242, 2.413` for `h = 2, …, 6`, and the growth `h − 2` of the rule `J − I` are below `δ_{h−1} = 1.618, 2.414, 3.303, 4.236, 5.193`. Without the signed part and the division by 2 the function gives `A_ridge(w, h)`.


### `strip_field(M)` → the Perron root and number field of one rule

The step behind `strip_field_census`: given one `0/1` transfer matrix, return its largest real eigenvalue and the field it generates. The characteristic polynomial is factored first, since `nroots` needs simple roots, and the factor carrying the root is labeled: degree 1 by `Q`, degree 2 by `Q(√d)` with `d` the squarefree part of the discriminant, higher degree by the polynomial ([[reachable-field-census](pages/reachable-field-census.md)]).

```python
import sympy as sp
x = sp.Symbol('x')

def strip_field(M):
    """Perron root and number field of ONE 0/1 strip transfer matrix."""
    p = sp.Matrix(M).charpoly(x).as_expr()
    rho, f = -sp.oo, None
    for g, _ in sp.factor_list(p)[1]:               # factor first: irreducible factors have simple roots
        g = sp.Poly(g, x)
        rr = [complex(z).real for z in sp.nroots(g, n=25) if abs(complex(z).imag) < 1e-8]
        if rr and max(rr) > rho:
            rho, f = max(rr), g
    d = f.degree()
    if d == 1: return sp.N(rho, 8), "Q"
    if d == 2:
        a, b, c = f.all_coeffs()
        D = b*b - 4*a*c
        sq = sp.Mul(*[q for q, e in sp.factorint(D).items() if e % 2])
        return sp.N(rho, 8), f"Q(sqrt({sq}))" if sq != 1 else "Q"
    return sp.N(rho, 8), f"deg {d} ({f.as_expr()})"
```

```
>>> strip_field([[1,1],[1,0]])                       # golden, h=2
(1.6180340, 'Q(sqrt(5))')
>>> strip_field([[0,1,1],[1,0,1],[1,1,1]])           # silver, h=3 (J - D)
(2.4142136, 'Q(sqrt(2))')
>>> strip_field([[0,0,1],[1,0,0],[1,1,0]])           # plastic, h=3
(1.3247180, 'deg 3 (x**3 - x - 1)')
```

Meaning: golden and silver lie in `Q(√5)` and `Q(√2)`, and the plastic number `ψ` is a cubic; the metallic mean `δ_a` lies in `Q(√(a² + 4))`. `strip_field_census` applies the same step to all `2^{h²}` matrices of size `h`.


### `strip_field_census(h)` → which number fields the strips reach

Two phases ([[reachable-field-census](pages/reachable-field-census.md)]): sweep all `2^{h²}` binary transfer matrices and bucket them by their largest real eigenvalue, then identify the field of each distinct value exactly. The function returns the number of distinct values in each field; `h = 4` takes about 40 seconds. Requires NumPy and SymPy.

```python
def strip_field_census(h):
    import numpy as np, sympy as sp, itertools
    from collections import defaultdict
    x = sp.symbols('x')
    def sqfree(m):
        d = 1
        for p, e in sp.factorint(int(round(m))).items():
            if e % 2: d *= p
        return d
    buckets = {}                                   # rounded Perron -> example bit-int
    for b in range(1 << (h*h)):
        M = np.array([[ (b >> (i*h+j)) & 1 for j in range(h)] for i in range(h)], float)
        ev = np.linalg.eigvals(M); r = ev.real[np.abs(ev.imag) < 1e-9]
        if len(r) and r.max() > 1e-9:
            buckets.setdefault(round(float(r.max()), 8), b)
    fields = defaultdict(int)
    for pv, b in buckets.items():
        M = sp.Matrix([[ (b >> (i*h+j)) & 1 for j in range(h)] for i in range(h)])
        for fac, _ in sp.factor_list(M.charpoly(x).as_expr())[1]:
            poly = sp.Poly(fac, x)
            rr = [complex(z).real for z in poly.all_roots() if abs(complex(z).imag) < 1e-9]
            if rr and abs(max(rr) - pv) < 1e-6:
                if poly.degree() == 2:
                    a, bb, c = poly.all_coeffs(); d = sqfree(bb*bb - 4*a*c)
                    fields[f"Q(sqrt{d})" if d > 1 else "Q"] += 1
                else:
                    fields[f"deg{poly.degree()}"] += 1
                break
    return dict(fields)
```

```
>>> strip_field_census(3)         # h = 3: 3 integers, quadratics in Q(sqrt 2), Q(sqrt 3), Q(sqrt 5), nine cubics
{'deg1': 3, 'Q(sqrt5)': 2, 'Q(sqrt2)': 2, 'deg3': 9, 'Q(sqrt3)': 1}
>>> # the nine cubics include x^3 - x - 1 (plastic), x^3 - x^2 - 1 (supergolden),
>>> # x^3 - 2x^2 + x - 1 (psi^2) and x^3 - x^2 - x - 1 (tribonacci)
>>> strip_field_census(4)
{'deg1': 12, 'Q(sqrt5)': 7, 'Q(sqrt2)': 3, 'deg3': 56, 'Q(sqrt3)': 3, 'Q(sqrt13)': 2, 'deg4': 110, 'Q(sqrt17)': 2, 'Q(sqrt21)': 1}
```

Meaning: the quadratic fields reached are `Q(√5)` at `h = 2`, `Q(√2), Q(√3), Q(√5)` at `h = 3`, and `Q(√d)` for `d = 2, 3, 5, 13, 17, 21` at `h = 4`. Bronze `Q(√13)` first appears at `h = 4`, through the ridge rule `R_4`; `δ_4` lies in `Q(√5)`; and the plastic number, a root of `x³ − x − 1`, is already a largest eigenvalue at `h = 3` ([[reachable-field-census](pages/reachable-field-census.md)]).


### `sh_canonical(M)` → S_h orbit representative (spectrum-preserving dedup)

Two transfer matrices related by a simultaneous permutation of rows and columns, `P M Pᵀ`, have the same spectrum. The lexicographically smallest flattening over all `h!` permutations picks one representative of each orbit of the symmetric group `S_h`. At `h = 4` the 65,536 matrices fall into 3,044 orbits, a factor of 21.5 ([[reachable-field-census](pages/reachable-field-census.md)]).

```python
from itertools import permutations

def sh_canonical(M):
    h = len(M)
    best = None
    for p in permutations(range(h)):
        flat = tuple(M[p[i]][p[j]] for i in range(h) for j in range(h))
        if best is None or flat < best:
            best = flat
    return best                        # canonical flattened tuple; equal iff same S_h orbit
```

```
>>> sh_canonical([[0,1],[0,0]]) == sh_canonical([[0,0],[1,0]])   # the two 1-edge 2x2 matrices
True
>>> # dedup a matrix list: len({sh_canonical(M) for M in matrices}) counts orbits
>>> from itertools import product
>>> len({sh_canonical([list(b[i*3:i*3+3]) for i in range(3)]) for b in product([0,1],repeat=9)})
104                                    # 512 binary 3x3 matrices -> 104 S_3 orbits
```

Meaning: the exact factoring step runs once per orbit instead of once per matrix. At `h = 6` the `2^{36}` matrices still give at least `2^{36}/720 ≈ 9.5 × 10^7` orbits, and [[reachable-field-census](pages/reachable-field-census.md)] treats `h ≥ 6` by other means.


### `tower_spacing_matrix(h, g)` → the min-tower-spacing skyline counter

The horizontal-gap variation of rule 3: every valley between raised regions must be `≥ g` columns wide ([[tower-spacing-castles](pages/tower-spacing-castles.md)]). Column-by-column transfer matrix; each constrained row `2..h` carries a state `pre` / `fill` / `g1..g_{g−1}` (empties since the last fill, capped at `g`), and a fill that would close a gap shorter than `g` is illegal. Requires NumPy.

```python
import itertools, numpy as np

def tower_spacing_matrix(h, g):
    rowstates = ['pre', 'fill'] + [f'g{k}' for k in range(1, g)]
    rows = list(range(2, h + 1))
    states = list(itertools.product(rowstates, repeat=len(rows)))
    idx = {s: i for i, s in enumerate(states)}
    M = np.zeros((len(states), len(states)))
    def nxt(st, filled):
        if filled:
            if st.startswith('g') and int(st[1:]) < g: return None   # gap too short - illegal
            return 'fill'
        if st == 'pre':  return 'pre'
        if st == 'fill': return 'g1' if g > 1 else 'pre'
        k = int(st[1:]); return 'pre' if k + 1 >= g else f'g{k+1}'
    for si, st in enumerate(states):
        for height in range(1, h + 1):            # a column of this height
            new, ok = [], True
            for ri, r in enumerate(rows):
                ns = nxt(st[ri], height >= r)
                if ns is None: ok = False; break
                new.append(ns)
            if ok: M[si, idx[tuple(new)]] += 1
    return M

def tower_spacing_counts(h, g, W):
    M = tower_spacing_matrix(h, g); n = M.shape[0]
    v = np.zeros(n); v[[i for i, s in enumerate(_states(h, g)) if all(x == 'pre' for x in s)][0]] = 1
    out = []
    for _ in range(W):
        v = v @ M; out.append(int(round(v.sum())))
    return out

def _states(h, g):
    rowstates = ['pre', 'fill'] + [f'g{k}' for k in range(1, g)]
    return list(itertools.product(rowstates, repeat=len(range(2, h + 1))))
```

```
>>> tower_spacing_counts(3, 2, 7)          # skylines on {1, 2, 3}, every valley at least 2 wide: A202882(w+1)
[3, 9, 22, 51, 121, 292, 704]
>>> M = tower_spacing_matrix(2, 2)          # h=2, towers >= 2 apart -> plastic-squared psi^2
>>> round(max(np.linalg.eigvals(M).real), 6)
1.754878
>>> round(max(np.linalg.eigvals(tower_spacing_matrix(2, 3)).real), 6)   # g=3 -> golden phi
1.618034
```

Meaning: the counts are of skylines on `{1, …, h}`, which need not reach `h`. At `g = 1` the rule imposes nothing, so there are `h^w`. At `h = 2` the growth is `ψ²` for `g = 2`, where the counts are `A005251(w+3)`, and `φ` for `g = 3`. For `3 ≤ h ≤ 5` and `2 ≤ g ≤ 5` no growth constant is a metallic mean `σ_p^q` ([[tower-spacing-castles](pages/tower-spacing-castles.md)]).


## Tree skylines and skylines by area

A tree skyline has no two neighboring columns of height at least 2, so its cells contain no `2 × 2` block; it need not reach its top height, and the tree castles of height `h` are the tree skylines of height `h` ([[tree-castle-by-area](pages/tree-castle-by-area.md)], [[castle-graph](pages/castle-graph.md)]).

### `castle_to_composition(c)` / `composition_to_castle(parts)` → bijection with compositions

The bijection between the tree skylines of height at most 4 and area `n` and the compositions of `n + 1` into parts `{1, 3, 4, 5}`, which also number the unique tournaments on `n + 1` vertices ([[tree-castle-by-area](pages/tree-castle-by-area.md)], the Proposition). `composition_to_castle` handles the parts up to 5, so heights up to 4.

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
(1, 3, 1)
>>> composition_to_castle((1, 3, 1))
(1, 2, 1)
>>> castle_to_composition((2, 1))
(3, 1)
>>> castle_to_composition((4,))
(5,)
>>> composition_to_castle((1, 4))
(1, 3)
```

Meaning: putting a column of height 1 in front and merging each pair `(1, j)` with `j ≥ 2` into the part `1 + j` gives the composition; the inverse expands each part `k ∈ {3, 4, 5}` into `(1, k − 1)` and drops the leading 1. The two maps are inverse bijections for every `n ≤ 11` (checked).


### `is_strongly_connected(T)` → strongly connected component (SCC) test for tournament matrices

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

Meaning: a directed graph is strongly connected exactly when every vertex is reachable from one vertex both forward and backward. The test finds the strong components of unique tournaments, which Tetali's Theorem 1 restricts to four ([[tree-castle-by-area](pages/tree-castle-by-area.md)]).


### `tree_area_gf(h, W)` / `tree_area_by_area(h, A_max)` → area-graded tree castle counts

The generating function `(1 + P_h(q)x)/(1 − qx − qP_h(q)x²)` of the tree skylines of height at most `h` by width (`x`) and area (`q`), with `P_h(q) = q² + ⋯ + q^h`, and its coefficients by area alone, the empty skyline included ([[tree-castle-by-area](pages/tree-castle-by-area.md)]). Requires SymPy.

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
>>> [a - 1 for a in tree_area_by_area(2, 15)][1:]  # tree castles of height 2, area A = 1..15: A077868(A-2) for A >= 2
[0, 1, 2, 3, 5, 8, 12, 18, 27, 40, 59, 87, 128, 188, 276]
>>> tree_area_by_area(3, 15)                       # tree skylines of height <= 3, A = 0..15: A006498(A+1)
[1, 1, 2, 4, 6, 9, 15, 25, 40, 64, 104, 169, 273, 441, 714, 1156]
>>> [int(c.subs(q, 1)) - 1 for c in tree_area_gf(2, 8)]  # tree castles of height 2, width w = 0..8: F_{w+2} - 1
[0, 1, 2, 4, 7, 12, 20, 33, 54]
```

Meaning: at `h = 3` the denominator is `1 − q − q³ − q⁴ = (1 + q²)(1 − q − q²)`, so the tree skylines of height at most 3 are golden by area. Without a height bound the tree skylines of area `A` number `A005251(A + 2)` (section *A005251 and the Hardin word automaton*), the sequence that also gives `P_even(6, L) = 2^L A005251(L + 3)` ([[tower-parity-sectors](pages/tower-parity-sectors.md)]).


### `bounded_castles_by_area(h, A_max)` → the skylines of height at most h by area

The skylines with column heights in `{1, …, h}` and area `A`, the castles of height at most `h`, are the compositions of `A` into parts `{1, …, h}`, counted by the `h`-step Fibonacci numbers with generating function `1/(1 − x − x² − ⋯ − x^h)`. The growth is the `h`-nacci constant: `φ` at `h = 2`, the tribonacci constant `1.8393…` at `h = 3`, increasing to 2 as `h → ∞` ([[castles-of-height-h-by-area](pages/castles-of-height-h-by-area.md)]). The tree skylines of `tree_area_by_area` have the denominator `1 − q − q³ − ⋯ − q^{h+1}`, with no `q²` term.

```python
def bounded_castles_by_area(h, A_max):
    # coeff of x^A in 1/(1 - x - x^2 - ... - x^h) = # compositions of A into parts {1..h}
    a = [1] + [0]*A_max
    for A in range(1, A_max+1):
        a[A] = sum(a[A-p] for p in range(1, h+1) if A-p >= 0)
    return a[1:]                                   # A = 1..A_max
```

```
>>> [a - 1 for a in bounded_castles_by_area(2, 12)]  # castles of height 2, A = 1..12: F_{A+1} - 1 = A000071(A+1)
[0, 1, 2, 4, 7, 12, 20, 33, 54, 88, 143, 232]
>>> bounded_castles_by_area(3, 12)                 # tribonacci A000073(A+2)
[1, 2, 4, 7, 13, 24, 44, 81, 149, 274, 504, 927]
>>> bounded_castles_by_area(4, 12)                 # tetranacci A000078(A+3)
[1, 2, 4, 8, 15, 29, 56, 108, 208, 401, 773, 1490]
```

Brute-force cross-check against the actual castle model (`sum(c)` over height-bounded skylines) agrees term for term:

```
>>> from itertools import product
>>> from collections import Counter
>>> def area_bf(h, Amax):
...     cnt = Counter()
...     for w in range(1, Amax+1):
...         for c in product(range(1, h+1), repeat=w):
...             if sum(c) <= Amax: cnt[sum(c)] += 1
...     return [cnt[A] for A in range(1, Amax+1)]
>>> area_bf(3, 12) == bounded_castles_by_area(3, 12)    # tribonacci, verified
True
```

Meaning: the castles of height 2 by area number `F_{A+1} − 1` (A000071), more than the tree castles of height 2 (A077868), since neighboring columns of height 2 are allowed. At `h = 3` the counts are the tribonacci numbers `A000073(A+2)`.


## A005251 and the Hardin word automaton

### `encode(c)` / `decode(s)` → the A005251 bijection

A composition of `n` with no two neighboring parts at least 2, which is a tree skyline of area `n`, corresponds to a binary string of length `n − 1` with no factor `010` ([[a005251-bijection](pages/a005251-bijection.md)]); both number `A005251(n+2)`, as do Hardin's binary words of length `n` with no isolated `1`. `compositions(n)` is on [[castle-snippets](pages/castle-snippets.md)].

```python
def encode(c):  return '1'.join('0' * (p - 1) for p in c)     # part c_j -> 0^{c_j-1}, join with 1
def decode(s):  return tuple(len(r) + 1 for r in s.split('1'))  # 0-run of length r -> part r+1
```

```
>>> encode((2, 1, 2)), encode((1, 3, 1))          # no adjacent 2s -> avoids 010
('0110', '1001')
>>> encode((2, 2, 1))                              # adjacent 2s -> contains 010 (excluded object)
'0101'
>>> decode('1001')                                 # inverse
(1, 3, 1)
>>> # the map is onto the avoid-010 set, term for term:
>>> from itertools import product
>>> n = 7
>>> comps = [c for c in compositions(n) if all(not (c[i] >= 2 and c[i+1] >= 2) for i in range(len(c)-1))]
>>> imgs  = {encode(c) for c in comps}
>>> tgt   = {''.join(b) for b in product('01', repeat=n-1) if '010' not in ''.join(b)}
>>> imgs == tgt, len(imgs)
(True, 37)
```

Meaning: a part at least 2 becomes a nonempty block of `0`s, so two neighboring parts at least 2 become `0…010…0` around their separating `1`, and the map takes the restricted compositions onto the strings with no `010`. The map is onto for every `n`, by the Proposition on [[a005251-bijection](pages/a005251-bijection.md)], and is checked here for `n ≤ 11`.

### `to_runs(s)` → the strings with no isolated 1, and the block parity

Composed with the column map of [[tree-castle-by-area](pages/tree-castle-by-area.md)], a column of height 1 becoming `0` and a column of height `c ≥ 2` becoming `1^c`, the gap map gives a bijection from the strings of length `n − 1` without `010` onto the strings of length `n` with no isolated `1` ([[a005251-bijection](pages/a005251-bijection.md)]). A tree castle has one more block than its string has zeros, so the strings also give the signed block count of the tree castles by area.

```python
import re

def to_runs(s):   # string of length n-1 without 010 -> string of length n with no isolated 1
    return ''.join('0' if b == '' else '1' * (len(b) + 1) for b in s.split('1'))
```

```
>>> to_runs(encode((1, 4))), to_runs(encode((2, 1, 2)))     # the castles (1, 4) and (2, 1, 2)
('01111', '11011')
>>> n = 7
>>> src = [''.join(b) for b in product('01', repeat=n-1) if '010' not in ''.join(b)]
>>> tgt = {''.join(b) for b in product('01', repeat=n) if all(len(r) >= 2 for r in re.findall('1+', ''.join(b)))}
>>> {to_runs(s) for s in src} == tgt, len(src)
(True, 37)
>>> # sum of (-1)^blocks over the tree castles of area n = 1..12, with blocks = 1 + zeros:
>>> [sum((-1) ** (1 + s.count('0')) for s in product('01', repeat=n-1) if '010' not in ''.join(s)) for n in range(1, 13)]
[-1, 0, 0, 1, 0, 1, -1, 1, -2, 2, -3, 4]
```

Meaning: each run of `r ≥ 1` zeros, a column of height `r + 1`, becomes a run of `r + 1` ones, and each empty block, a column of height 1, becomes a `0`, so the runs of ones are separated by zeros and none has length 1. The signed counts are `(−1)^n A000931(n − 1)`, signed Padovan numbers.


### `A005251(n)` → the plastic-squared sequence directly

The term `a(n)` of A005251 by the Python program on the OEIS entry (Chai Wah Wu), at the entry's offset `a(0) = 0, a(1) = a(2) = a(3) = 1`.[^2] Requires SymPy.

```python
from sympy import Matrix
def A005251(n):
    return (Matrix([[2, -1, 1], [1, 0, 0], [0, 1, 0]]) ** (n - 2) * Matrix([1, 1, 0]))[0]
```

```
>>> [A005251(n) for n in range(15)]
[0, 1, 1, 1, 2, 4, 7, 12, 21, 37, 65, 114, 200, 351, 616]
>>> # tree skylines of area A, any height: A005251(A + 2)
>>> comps = [c for c in compositions(6) if all(not (c[i] >= 2 and c[i+1] >= 2) for i in range(len(c)-1))]
>>> len(comps), A005251(6 + 2)
(21, 21)
```

Meaning: `[[2, −1, 1], [1, 0, 0], [0, 1, 0]]` is the companion matrix of `a(n) = 2a(n−1) − a(n−2) + a(n−3)`, and its power `n − 2` applied to `(1, 1, 0)` gives `a(n)`; the matrix has determinant 1, so the negative powers at `n < 2` are integral. Four castle counts are this sequence: the tree skylines of area `n`, `A005251(n+2)`; Hardin's words of length `N` with no isolated `1`, `A005251(N+2)`; the tower-spacing skylines with `h = 2`, `g = 2` and width `w`, `A005251(w+3)`; and the even-last-column signed tower count at tower height 6, `P_even(6, L)/2^L = A005251(L+3)` ([[a005251-bijection](pages/a005251-bijection.md)], [[plastic-number](pages/plastic-number.md)]).


### `word_matrix(m)` → transfer matrix of Hardin's no-local-maximum words

Words over `{0..m}` in which every nonzero letter is `≤` a neighbor, counted by a `2m+1`-state automaton with a "pending" flag ([[hardin-word-identity](pages/hardin-word-identity.md)]). Requires SymPy.

```python
mu = sp.Symbol('mu')

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
>>> sp.factor(W.charpoly(mu).as_expr())                        # = H_5(mu), as on castle-snippets-number-theory
mu**5 - 3*mu**4 + 3*mu**3 - 4*mu**2 + mu - 1
```

Meaning: the count equals `P_even(10, n−1)/2^{n−1}`, the even-last-column signed tower count at tower height 10, for every `n ≤ 10` (checked); this is the Hardin identity ([[hardin-word-identity](pages/hardin-word-identity.md)]).


### `is_hardin_word(w)` / `W_bruteforce(m, n)` → no-local-maximum words, by brute force

The brute-force definition of the Hardin words behind `word_matrix`: every nonzero letter has a neighbor `≥` it (boundaries count as `0`), so no nonzero letter is a strict local maximum. Counts agree with the automaton and with `2^{−L}` times the even-last-column signed tower count ([[hardin-word-identity](pages/hardin-word-identity.md)]).

```python
from itertools import product

def is_hardin_word(w):
    for i, a in enumerate(w):
        if a == 0: continue
        if (i > 0 and w[i-1] >= a) or (i+1 < len(w) and w[i+1] >= a): continue
        return False
    return True

def W_bruteforce(m, n):
    return sum(1 for w in product(range(m+1), repeat=n) if is_hardin_word(w))
```

```
>>> [W_bruteforce(1, n) for n in range(1, 9)]           # A005251(n+2)
[1, 2, 4, 7, 12, 21, 37, 65]
>>> [W_bruteforce(2, n) for n in range(1, 7)]           # A202882
[1, 3, 9, 22, 51, 121]
>>> [''.join(map(str, w)) for w in product(range(2), repeat=3) if is_hardin_word(w)]
['000', '011', '110', '111']
```

Meaning: for `m = 1` the valid words are binary strings with no isolated `1` (the four length-3 ones are `000, 011, 110, 111`), `W_1(n) = A005251(n+2)`; for `m = 2` it is Hardin's A202882.


## Appearances in Sources

- [[project-euler-502-brute-force](pages/project-euler-502-brute-force.md)] - the column-height encoding of castles used by every snippet.

## Related Concepts

- [[castle-snippets](pages/castle-snippets.md)] - the hub: enumeration, `compositions`, and the shape predicates of [[castle-classification-shape](pages/castle-classification-shape.md)].
- [[castle-strip](pages/castle-strip.md)] / [[metallic-strip-realizability](pages/metallic-strip-realizability.md)] / [[reachable-field-census](pages/reachable-field-census.md)] - the strip-transfer-matrix machinery.
- [[metallic-means](pages/metallic-means.md)] - the family `nearest_metallic` tests against.
- [[pell-castle-strip](pages/pell-castle-strip.md)] - the Pell strip of `pell_strip_count`, silver by width.
- [[proper-castle-projection](pages/proper-castle-projection.md)] - the `proper_even` projection.
- [[tower-spacing-castles](pages/tower-spacing-castles.md)] - the horizontal-gap variation whose transfer matrix is `tower_spacing_matrix`.
- [[tree-castle-by-area](pages/tree-castle-by-area.md)] - the tree skylines by width and area, and their bijections with compositions and unique tournaments.
- [[castles-of-height-h-by-area](pages/castles-of-height-h-by-area.md)] - the castles of height `h` by area and the `h`-nacci growth constants of `bounded_castles_by_area`.
- [[a005251-bijection](pages/a005251-bijection.md)] / [[hardin-word-identity](pages/hardin-word-identity.md)] - the `encode`/`decode` bijection and the `word_matrix` automaton.
- [[plastic-number](pages/plastic-number.md)] - `ψ²`, the growth constant of A005251, and the castle counts that grow at it.

## Footnotes

[^1]: Verified by execution (Python 3.11 with SymPy and NumPy, 2026-10-16): every printed output on this page; `proper_even(4, ·)` and `proper_even(5, ·)` against enumeration of ridge castles for `w ≤ 7`; the spectral radii of `R̃_h` for `h ≤ 6`; `strip_field_census(3)` and `(4)` with the nine cubics at `h = 3`; 104 orbits at `h = 3` and 3,044 at `h = 4`; `tower_spacing_counts(3, 2, ·)` against enumeration for `w ≤ 7` and `tower_spacing_counts(2, 2, ·) = A005251(w + 3)` for `w ≤ 10`; the bijection of `castle_to_composition` for `n ≤ 11`; the tree-skyline series against enumeration for `A ≤ 15`; `encode` onto the strings without `010` for `n ≤ 11`; `P_even(10, n − 1)/2^{n−1} = A202882(n)` for `n ≤ 10`. On 2026-10-25 (Python 3.11): the `to_runs` outputs, `to_runs` onto the strings with no isolated `1` for `n ≤ 14`, and the signed counts from the strings against `(−1)^n A000931(n − 1)` for `n ≤ 12`.
[^2]: https://oeis.org/A005251 (read 2026-10-16) - "(Python) from sympy import Matrix def A005251(n): return (Matrix([[2,-1,1],[1,0,0],[0,1,0]])**(n-2)*Matrix([1,1,0]))[0] # _Chai Wah Wu_, Jun 10 2026"; "a(n+3) is the number of n-bit sequences that avoid 010"; "For n>=3, a(n) is the number of binary strings of length n-2 without any maximal runs of ones of length 1".
