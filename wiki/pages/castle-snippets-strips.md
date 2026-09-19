---
title: Castle snippets - strips and growth
category: Concepts
summary: Snippets for castle strips, Axis-8 growth-constant probes, tree-castle-by-area, and the Hardin word automaton. Sibling of the core castle-snippets hub.
tags: [concept, castle, python, snippets, strip, growth-constant, metallic-mean, tree-castle, hardin]
sources: [project-euler-502-brute-force]
created: 2026-09-19
updated: 2026-09-19
---

# Castle snippets - strips and growth

A sibling page to [[castle-snippets](pages/castle-snippets.md)]: snippets for castle strips (a skyline read left-to-right under a neighbor rule, [[castle-strip](pages/castle-strip.md)]), Axis-8 growth-constant probes, the tree-castle-by-area family, and the Hardin word automaton. Same conventions as the hub page - every output pinned, every snippet executed during ingest.

For the number-theoretic snippets that read continued-fraction convergents / mod-`p` orders / signed tower counts off these strips, see [[castle-snippets-number-theory](pages/castle-snippets-number-theory.md)]. For the cryptography snippets built on the signed transfer matrix, see [[castle-snippets-cryptography](pages/castle-snippets-cryptography.md)].

## Strip predicates and growth-constant probes

### Axis 8: growth-type predicate skeleton — the height-2 tree-castle strip

Encode the state above the base (0 = empty column, 1 = one raised cell) and forbid two adjacent raised columns; this is the height-2 tree castle of [[castle-graph](pages/castle-graph.md)]. See [[castle-classification-non-geometric](pages/castle-classification-non-geometric.md)] Axis 8 for the meta-classification these strips instantiate.

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

Wiki tie: [[castle-classification-non-geometric](pages/castle-classification-non-geometric.md)] Axis 8 — the height-2 tree castles are a golden width growth castle; their count sequence is Fibonacci `F_{w+2}` (see also `is_tree_castle` below).

### `pell_strip_count(w)` → the Pell castle strip

The silver counterpart ([[pell-castle-strip](pages/pell-castle-strip.md)]): 1-smooth skylines over heights `{1, 2, 3}` (adjacent heights differ by at most 1) whose first column has height 1. Their width generating function is exactly `1/(1 − 2x − x²)`, so the counts are Pell numbers `P_{w+1}`; dropping the anchor gives companion Pell (A001333).

```python
from itertools import product

def pell_strip_count(w, anchored=True):
    return sum(1 for c in product((1, 2, 3), repeat=w)
               if (c[0] == 1 or not anchored)
               and all(abs(c[i+1] - c[i]) <= 1 for i in range(w-1)))
```

```
>>> [pell_strip_count(w) for w in range(1, 9)]                  # Pell P_{w+1}, A000129
[1, 2, 5, 12, 29, 70, 169, 408]
>>> [pell_strip_count(w, anchored=False) for w in range(1, 9)]  # companion Pell, A001333
[3, 7, 17, 41, 99, 239, 577, 1393]
```

Meaning: the boundary condition selects the sequence - anchoring the first column at the base gives Pell proper, a free first column gives companion Pell; both grow at `1 + √2`.


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

Meaning: Pell → `a=2` (silver, `1+√2 ≈ 2.4142`). Fibonacci → `a=1` (golden, `φ ≈ 1.6180`). The sequence a candidate silver / golden / bronze / … *width* growth castle would produce, in the sense of [[castle-classification-non-geometric](pages/castle-classification-non-geometric.md)] Axis 8.

**Cautions:**
- `growth_constant` estimates from **width**-graded sequences; use the appropriate size-axis sequence for vertical / area / block growth castles (see [[castle-classification-non-geometric](pages/castle-classification-non-geometric.md)] Axis 8).
- `nearest_metallic` always returns *some* answer — even a transcendental growth constant will return the closest metallic mean. Check the actual distance if uncertain:

```python
>>> trib = [1, 2, 4, 7, 13, 24, 44, 81, 149, 274]   # tribonacci A000073(A+2), the h=3 bounded-height-by-area castle
>>> r = growth_constant(trib); r                     # 5-term tail avg -> approaches tribonacci const 1.83929
1.8397657235464842
>>> a = nearest_metallic(r); a, (a + math.sqrt(a*a+4))/2, abs(r - (a + math.sqrt(a*a+4))/2)
(1, 1.618033988749895, 0.22173173479658925)
```

A gap of ~0.222 is *not* a metallic-mean hit — the tribonacci constant `≈ 1.83929` (root of `x³ = x² + x + 1`) is a genuine *cubic*, so `nearest_metallic` returning golden `φ` is a false positive. This sequence *is* a real castle count — all castles of height `≤ 3` by area ([[bounded-height-castles-nacci](pages/bounded-height-castles-nacci.md)], `bounded_castles_by_area(3, ·)` below) — but its growth is cubic, not metallic. `nearest_metallic` gives the closest metal regardless; only trust it when the residual is small.


## Named strip rules

### `ceiling_exception_ladder(h)` → the whole metallic ladder from one rule

The **plateau-free-except-ceiling** castle-strip rule — adjacent columns differ in height unless both equal the max `h` — realizes every metallic mean: at height `h` its transfer matrix is `M_h = J − D` (all-ones minus `diag(1,…,1,0)`), char poly `(x+1)^{h−2}(x² − (h−1)x − 1)`, Perron root the `(h−1)`-th metallic mean `δ_{h−1}` ([[metallic-strip-realizability](pages/metallic-strip-realizability.md)]). So bronze is `h = 4`, copper `h = 5`, and copper's count is the Fibonacci trisection `F_{3n+5}`. Requires SymPy.

```python
def ceiling_exception_M(h):
    # M[a][b] = 1 iff a != b, or a == b == h  (heights 1..h, 0-indexed here)
    return sp.Matrix(h, h, lambda i, j: 1 if (i != j or i == h-1) else 0)

def ceiling_exception_count(h, L_max):
    M = ceiling_exception_M(h); ones = sp.ones(h, 1)
    return [int((ones.T * M**L * ones)[0]) for L in range(L_max+1)]
```

```
>>> sp.factor(ceiling_exception_M(4).charpoly(sp.Symbol('x')).as_expr())   # bronze
(x + 1)**2*(x**2 - 3*x - 1)
>>> ceiling_exception_count(4, 6)                        # bronze (3+sqrt13)/2, Q(sqrt13)
[4, 13, 43, 142, 469, 1549, 5116]
>>> ceiling_exception_count(5, 8)                        # copper 2+sqrt5 = phi^3: F_{3n+5}
[5, 21, 89, 377, 1597, 6765, 28657, 121393, 514229]
>>> [sp.factor(ceiling_exception_M(h).charpoly(sp.Symbol('x')).as_expr()) for h in range(2,7)]
[x**2 - x - 1, (x + 1)*(x**2 - 2*x - 1), (x + 1)**2*(x**2 - 3*x - 1), (x + 1)**3*(x**2 - 4*x - 1), (x + 1)**4*(x**2 - 5*x - 1)]
```

Meaning: one rule, one parameter `h`, sweeps golden → silver → bronze → copper → nickel → … as `h = 2, 3, 4, 5, 6, …` (metal `a = h−1`). The `(x+1)^{h−2}` factor is the subdominant eigenvalue `−1`; the metallic quadratic `x² − (h−1)x − 1` carries the growth. The copper (`h=5`) row is every third Fibonacci — the decimation forced by `δ_4 = φ³`.


### `proper_even(h, Wmax)` → the proper-castle projection of the ladder

The `ceiling_exception_count` above is a *free-height strip* count (`𝟙ᵀM^L𝟙`); a **proper** PE-502 castle imposes `max_i c_i = h` and the even-block parity `(A±P)/2` ([[castle-sign](pages/castle-sign.md)]). This projects both on at once: subtract the `max < h` strips (which satisfy *plateau-free*, `J − I`, since the ceiling exception is unreachable) and fold in the signed count `P = Σ (−1)^{blocks}` via the signed matrix `S[a][b] = (−1)^{max(0, b−a)} M[a][b]`. The metallic growth survives (the signed matrix is spectrally subdominant), but the sequences are **new** — see [[proper-castle-projection](pages/proper-castle-projection.md)]. Requires SymPy.

```python
def proper_even(h, Wmax):
    """Even-block proper castles (max=h) under the J-D plateau-free-except-ceiling rule.
    Metal a = h-1. Returns counts by width w = 1..Wmax. Requires SymPy."""
    def free(mat):
        n = mat.shape[0]
        ones = sp.ones(n, 1)
        v = sp.Matrix(n, 1, [(-1)**(a+1) for a in range(n)])              # (-1)^height
        S = sp.Matrix(n, n, lambda a, b: (-1)**max(0, b-a) * mat[a, b])    # (-1)^blocks increment
        u, s, Mu, Ms = [], [], sp.eye(n), sp.eye(n)
        for _ in range(Wmax):
            u.append(int((ones.T*Mu*ones)[0])); s.append(int((v.T*Ms*ones)[0]))
            Mu, Ms = Mu*mat, Ms*S
        return u, s
    JD  = sp.Matrix(h, h, lambda i, j: 1 if (i != j or i == h-1) else 0)   # J - D
    PF  = sp.Matrix(h-1, h-1, lambda i, j: 1 if i != j else 0)             # J - I (max < h strip)
    uJ, sJ = free(JD); uP, sP = free(PF)
    return [(uJ[w]-uP[w] + sJ[w]-sP[w]) // 2 for w in range(Wmax)]
```

```
>>> proper_even(4, 8)   # bronze (a=3): new sequence, growth -> 3.30278
[1, 7, 25, 70, 209, 697, 2390, 8169]
>>> proper_even(5, 8)   # copper (a=4): growth -> 4.23607 = phi^3
[0, 0, 10, 104, 604, 2836, 12630, 55668]
```

Meaning: the even-block proper-castle rows are a new family (no Online Encyclopedia of Integer Sequences (OEIS) match for `h ≥ 3`); the growth is still the metal `δ_{h−1}` (the signed matrix's spectral radius `1.000/1.575/1.768/2.242/2.413` for `h = 2..6` sits below `δ = 1.618/2.414/3.303/4.236/5.193`). Drop the `// 2` and the signed half to get the unsigned `max=h` count.


### `strip_field(M)` → the Perron root and number field of one rule

The single-matrix step behind `strip_field_census` below: given one `0/1` transfer matrix, read off its growth constant and field. Factor first (irreducible factors have simple roots, which `nroots` needs), then label — degree 1 → `Q`, degree 2 → `Q(√d)` by the squarefree part of the discriminant, degree ≥ 3 → the minimal polynomial. The core step of [[reachable-field-census](pages/reachable-field-census.md)] in one function.

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

Meaning: the metallic fields are `Q(√5)`, `Q(√2)`, `Q(√13)`, …; the plastic number is a degree-3 growth constant. `strip_field_census` below just loops this one step over all `2^{h²}` matrices and buckets the labels.


### `strip_field_census(h)` → which number fields the strips reach

Two-phase census ([[reachable-field-census](pages/reachable-field-census.md)]): sweep all `2^{h²}` binary transfer matrices, bucket by numeric Perron root, then exactly identify each distinct root's number field. `h ≤ 4` exhaustive in seconds. Requires NumPy + SymPy.

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
>>> strip_field_census(3)         # h=3: 3 integer, quadratics Q(sqrt2,3,5), nine cubics
{'deg1': 3, 'Q(sqrt5)': 2, 'Q(sqrt2)': 2, 'deg3': 9, 'Q(sqrt3)': 1}
>>> # the deg-3 roots at h=3 include x^3-x-1 (plastic!), x^3-x^2-x-1 (tribonacci), supergolden, plastic^2
```

Meaning: the reachable quadratic fields grow `{5} → {2,3,5} → {2,3,5,13,17,21}` as `h = 2,3,4`; every squarefree metallic discriminant `a²+4` appears (bronze `Q(√13)` at h=4), copper collapses into `Q(√5)`, and the **bare plastic number** `x³−x−1` shows up as a Perron root already at h=3 ([[reachable-field-census](pages/reachable-field-census.md)]).


### `sh_canonical(M)` → S_h orbit representative (spectrum-preserving dedup)

Two strip transfer matrices related by simultaneous row+column permutation `P M Pᵀ` (relabeling the `h` height-states) have identical spectra. The canonical form — lexicographically-minimal flattening over all `h!` permutations — collapses each `S_h` orbit to one representative, cutting the census work by up to `h!` (≈ 21× at h=4). Deduping by it reproduces the field lists exactly ([[reachable-field-census](pages/reachable-field-census.md)]).

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

Meaning: canonicalizing before the expensive exact-factor step means factoring one matrix per orbit instead of one per matrix. It validated the census (canonical-rep field lists match the full sweep at h ≤ 4), but even the `≈ h!` compression leaves `h = 6` at ~95M orbits — so `h ≥ 6` is settled by the reachability law plus targeted construction, not exhaustion ([[reachable-field-census](pages/reachable-field-census.md)]).


### `tower_spacing_matrix(h, g)` → the min-tower-spacing castle counter

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
            if st.startswith('g') and int(st[1:]) < g: return None   # gap too short — illegal
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
>>> tower_spacing_counts(3, 2, 7)          # h=3 castles, valleys >= 2 wide
[3, 9, 22, 51, 121, 292, 704]
>>> M = tower_spacing_matrix(2, 2)          # h=2, towers >= 2 apart -> plastic-squared psi^2
>>> round(max(np.linalg.eigvals(M).real), 6)
1.754878
>>> round(max(np.linalg.eigvals(tower_spacing_matrix(2, 3)).real), 6)   # g=3 -> golden phi
1.618034
```

Meaning: `g = 1` is the trivial rule (growth `h`, count `h^w`); `g ≥ 2` carves out sparser families whose growth constants decrease toward 1 as `g` grows, passing through `ψ²` (h=2,g=2) and `φ` (h=2,g=3). For `g ≥ 2, h ≥ 3` the constants are non-metallic ([[tower-spacing-castles](pages/tower-spacing-castles.md)]).


## Tree castles by area

### `castle_to_composition(c)` / `composition_to_castle(parts)` → bijection with compositions

The three-way bijection tree castle ↔ composition of `A + 1` with parts in `{1, 3, 4, 5}` ↔ score-uniquely-determined (SUD) tournament on `A + 1` nodes ([[tree-castle-by-area](pages/tree-castle-by-area.md)]).

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


### `bounded_castles_by_area(h, A_max)` → the n-nacci-by-height family

**All** castles (not just tree castles) with column heights in `{1, …, h}`, graded by area `A`. A castle bounded by height `h` is exactly a composition of `A` into parts `{1, …, h}`, so the count is the **`h`-step Fibonacci** (n-nacci) number, GF `1 / (1 − x − x² − ⋯ − x^h)`. Growth marches up the n-nacci constants: `h = 2` **Fibonacci** (φ), `h = 3` **tribonacci** (`t ≈ 1.8393`), … → `2` as `h → ∞` ([[bounded-height-castles-nacci](pages/bounded-height-castles-nacci.md)]). Distinct from `tree_area_by_area` above, whose 2×2-block ban gives the term-*skipping* cubics (supergolden, plastic) instead.

```python
def bounded_castles_by_area(h, A_max):
    # coeff of x^A in 1/(1 - x - x^2 - ... - x^h) = # compositions of A into parts {1..h}
    a = [1] + [0]*A_max
    for A in range(1, A_max+1):
        a[A] = sum(a[A-p] for p in range(1, h+1) if A-p >= 0)
    return a[1:]                                   # A = 1..A_max
```

```
>>> bounded_castles_by_area(2, 12)                 # Fibonacci A000045(A+1)
[1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233]
>>> bounded_castles_by_area(3, 12)                 # tribonacci A000073(A+2)
[1, 2, 4, 7, 13, 24, 44, 81, 149, 274, 504, 927]
>>> bounded_castles_by_area(4, 12)                 # tetranacci A000078
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

Meaning: this is the "sum of the previous `h`" companion to the tree-castle family. `h = 2` here is **A000045** (Fibonacci) - a *different, denser* sequence than the `h = 2` tree-castle row `tree_area_by_area(2, ·)` = A000930 (Narayana's cows), because dropping the tree (no-2×2-block) constraint restores the `(…,2,2,…)` adjacencies. `h = 3` is the tribonacci sequence **A000073** - the castle's first tribonacci interpretation.


## A005251 and the Hardin word automaton

### `encode(c)` / `decode(s)` → the A005251 bijection

Composition of `n` (no two adjacent parts `≥ 2`, = tree castle of area `n`) ↔ length-`(n−1)` binary string avoiding `010` (= Hardin no-isolated-1 word) — the classic gap-string map, constraint-preserving ([[a005251-bijection](pages/a005251-bijection.md)]).

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

Meaning: "no two adjacent parts `≥ 2`" ⟺ "no factor `010`" because a part `≥ 2` is a nonempty `0`-block and two adjacent such blocks straddle a boundary `1` as `010`. Verified onto the avoid-010 set for `n ≤ 11` — the explicit bijection closing the tree-castle ↔ Hardin-word coincidence at plastic-squared ([[a005251-bijection](pages/a005251-bijection.md)]).


### `A005251(n)` → the plastic-squared sequence directly

The `n`-th A005251 term by the sequence's own matrix-power one-liner (lifted verbatim from the [OEIS A005251](https://oeis.org/A005251) page), at the canonical offset `a(0)=0, a(1)=a(2)=a(3)=1`. Handy for checking any castle count against A005251 without re-deriving the recurrence. Requires SymPy.

```python
from sympy import Matrix
def A005251(n):
    return (Matrix([[2, -1, 1], [1, 0, 0], [0, 1, 0]]) ** (n - 2) * Matrix([1, 1, 0]))[0]
```

```
>>> [A005251(n) for n in range(15)]
[0, 1, 1, 1, 2, 4, 7, 12, 21, 37, 65, 114, 200, 351, 616]
>>> # cross-check a castle count: tree castles of area A (unlimited height) = A005251(A+2)
>>> comps = [c for c in compositions(6) if all(not (c[i] >= 2 and c[i+1] >= 2) for i in range(len(c)-1))]
>>> len(comps), A005251(6 + 2)
(21, 21)
```

Meaning: the companion matrix `[[2,−1,1],[1,0,0],[0,1,0]]` is the transfer matrix of the recurrence `a(n) = 2a(n−1) − a(n−2) + a(n−3)`; its `(n−2)`-th power against the seed `[1,1,0]` reads off the **canonical** `a(n)` (OEIS offset 0, `a(0)=0`). The four castle objects that hit this sequence sit at these offsets: tree castles / compositions of `n` = `A005251(n+2)`; Hardin no-isolated-1 words of length `N` = `A005251(N+3)`; tower-spacing `(h=2,g=2)` width `w` = `A005251(w+3)`; signed height-6 even-last-column towers `P_even(6,L)/2^L` = `A005251(L+3)` ([[a005251-bijection](pages/a005251-bijection.md)], [[plastic-number](pages/plastic-number.md)]).


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


### `is_hardin_word(w)` / `W_bruteforce(m, n)` → no-local-maximum words, by brute force

The brute-force definition of the Hardin words behind `word_matrix` above: every nonzero letter has a neighbor `≥` it (boundaries count as `0`), so no nonzero letter is a strict local maximum. Counts agree with the automaton and with `2^{−L}` times the even-last-column signed tower count ([[hardin-word-identity](pages/hardin-word-identity.md)]).

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

- [[project-euler-502-brute-force](pages/project-euler-502-brute-force.md)] - the reference `p_signed` DP against which these strip and tree-castle snippets were cross-checked during ingest.

## Related Concepts

- [[castle-snippets](pages/castle-snippets.md)] - the enumeration-primitives / Axis 1-7 predicates hub.
- [[castle-strip](pages/castle-strip.md)] / [[metallic-strip-realizability](pages/metallic-strip-realizability.md)] / [[reachable-field-census](pages/reachable-field-census.md)] - the strip-transfer-matrix machinery.
- [[metallic-means](pages/metallic-means.md)] - the family `nearest_metallic` tests against.
- [[pell-castle-strip](pages/pell-castle-strip.md)] - the silver-width-growth-castle example (`pell_strip_count`).
- [[proper-castle-projection](pages/proper-castle-projection.md)] - the `proper_even` projection.
- [[tower-spacing-castles](pages/tower-spacing-castles.md)] - the horizontal-gap variation whose transfer matrix is `tower_spacing_matrix`.
- [[tree-castle-by-area](pages/tree-castle-by-area.md)] - the `tree_area_gf`, `tree_area_by_area`, and `castle_to_composition` snippets.
- [[bounded-height-castles-nacci](pages/bounded-height-castles-nacci.md)] - the n-nacci area-growth family from `bounded_castles_by_area`.
- [[a005251-bijection](pages/a005251-bijection.md)] / [[hardin-word-identity](pages/hardin-word-identity.md)] - the `encode`/`decode` bijection and the `word_matrix` automaton.
- [[plastic-number](pages/plastic-number.md)] - the plastic-squared sequence via `A005251` and the four-reading hub.
