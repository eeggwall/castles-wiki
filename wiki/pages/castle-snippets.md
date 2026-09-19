---
title: Castle snippets — Python one-liners
category: Concepts
summary: A living reference of short, tested Python snippets for enumerating castles, testing classification predicates, computing growth constants, continued-fraction convergents, mod-p eigenvalue orders, quasi-polynomial splits, and looking up OEIS sequences. Every snippet ran during ingest; outputs pinned to the values shown.
tags: [concept, castle, python, snippets, computational, classification, reference]
sources: [project-euler-502-brute-force]
created: 2026-09-16
updated: 2026-09-19
---

# Castle snippets — Python one-liners

## What this is

A living reference of **short, tested Python snippets** for exploring castles computationally. Each snippet:

- Runs in a plain Python read-eval-print loop (REPL) (no external deps unless one line justifies the import — `itertools`, `math`).
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

Block count under the wiki convention (matches [[castle-sign](pages/castle-sign.md)] and the `p_signed` dynamic program (DP) on [[project-euler-502-brute-force](pages/project-euler-502-brute-force.md)]).

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

Also matches the [[castle-counting-formula](pages/castle-counting-formula.md)] `F(4,2) = ½(16 − 1 + 4 + 1) = 10` and the [[castles-as-upgraded-cycle-count](pages/castles-as-upgraded-cycle-count.md)] hand check. The ten castles are those whose second row has an odd number of runs of `1`s ([[pe502-castle-cycle-permutations](pages/pe502-castle-cycle-permutations.md)]); at width 4 that is exactly one run, and `all_castles(5, 2)` adds the three-run row `10101` to make `F(5,2) = 16`.

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

### Axis 8: growth-type predicate skeleton — the height-2 tree-castle strip

Encode the state above the base (0 = empty column, 1 = one raised cell) and forbid two adjacent raised columns; this is the height-2 tree castle of [[castle-graph](pages/castle-graph.md)]. See [[castle-classification](pages/castle-classification.md)] Axis 8 for the meta-classification these strips instantiate.

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

Wiki tie: [[castle-classification](pages/castle-classification.md)] Axis 8 — the height-2 tree castles are a golden width growth castle; their count sequence is Fibonacci `F_{w+2}` (see also `is_tree_castle` below).

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

Meaning: Pell → `a=2` (silver, `1+√2 ≈ 2.4142`). Fibonacci → `a=1` (golden, `φ ≈ 1.6180`). The sequence a candidate silver / golden / bronze / … *width* growth castle would produce, in the sense of [[castle-classification](pages/castle-classification.md)] Axis 8.

**Cautions:**
- `growth_constant` estimates from **width**-graded sequences; use the appropriate size-axis sequence for vertical / area / block growth castles (see [[castle-classification](pages/castle-classification.md)] Axis 8).
- `nearest_metallic` always returns *some* answer — even a transcendental growth constant will return the closest metallic mean. Check the actual distance if uncertain:

```python
>>> trib = [1, 2, 4, 7, 13, 24, 44, 81, 149, 274]   # tribonacci A000073(A+2), the h=3 bounded-height-by-area castle
>>> r = growth_constant(trib); r                     # 5-term tail avg -> approaches tribonacci const 1.83929
1.8397657235464842
>>> a = nearest_metallic(r); a, (a + math.sqrt(a*a+4))/2, abs(r - (a + math.sqrt(a*a+4))/2)
(1, 1.618033988749895, 0.22173173479658925)
```

A gap of ~0.222 is *not* a metallic-mean hit — the tribonacci constant `≈ 1.83929` (root of `x³ = x² + x + 1`) is a genuine *cubic*, so `nearest_metallic` returning golden `φ` is a false positive. This sequence *is* a real castle count — all castles of height `≤ 3` by area ([[bounded-height-castles-nacci](pages/bounded-height-castles-nacci.md)], `bounded_castles_by_area(3, ·)` below) — but its growth is cubic, not metallic. `nearest_metallic` gives the closest metal regardless; only trust it when the residual is small.

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

### `strip_field(M)` → the Perron root and number field of one rule

The single-matrix step behind `strip_field_census` above: given one `0/1` transfer matrix, read off its growth constant and field. Factor first (irreducible factors have simple roots, which `nroots` needs), then label — degree 1 → `Q`, degree 2 → `Q(√d)` by the squarefree part of the discriminant, degree ≥ 3 → the minimal polynomial. The core step of [[reachable-field-census](pages/reachable-field-census.md)] in one function.

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

Meaning: the metallic fields are `Q(√5)`, `Q(√2)`, `Q(√13)`, …; the plastic number is a degree-3 growth constant. `strip_field_census` above just loops this one step over all `2^{h²}` matrices and buckets the labels.

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

### `berlekamp_massey(s)` → the shortest recurrence over the rationals

Berlekamp–Massey with exact rational coefficients (the mod-`p` cousin is `bm_modp` in the cryptography section). Given a sequence, returns the connection polynomial (low→high, `C[0] = 1`) and its order. Over `Q` this is exact — [[convergents-oeis-crosswalk](pages/convergents-oeis-crosswalk.md)] Part 3 runs it on `P(·, L)` to recover `(x+1)^L (x−1)^{L−2}`.

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
[[0, 1, 1, 0, 0], [1, 0, 0, 0, 0], [1, 0, 0, 1, 0], [0, 0, 1, 0, 1], [0, 0, 0, 1, 0]]
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

### `oeis_lookup(terms)` → list of `(A-number, name)`

The live version of `oeis_snippet` below. **OEIS answers Python's default `urllib` User-Agent with HyperText Transfer Protocol (HTTP) 403**; go through `curl` with a real UA and sleep a second between calls.

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

### `castle_dh` → a working castle Diffie–Hellman

Public-key exchange in the ring `F_p[x]/(Q)`, where `Q` is a castle characteristic polynomial ([[castle-cryptography](pages/castle-cryptography.md)]). The "public castle" is `Q`; a private key is a secret exponent; the trapdoor `x^a mod Q` is [[kitamasa](pages/kitamasa.md)] exponentiation. Stdlib only.

```python
def one(Q): return [1] + [0]*(len(Q)-2)          # multiplicative identity in F_p[x]/(Q)
def gen(Q): return [0, 1] + [0]*(len(Q)-3)        # the generator polynomial x

def mulmod(A, B, Q, p):                       # multiply in F_p[x]/(Q), Q monic degree d
    r = [0] * (len(A) + len(B) - 1)
    for i, a in enumerate(A):
        for j, b in enumerate(B):
            r[i + j] = (r[i + j] + a * b) % p
    d = len(Q) - 1
    for i in range(len(r) - 1, d - 1, -1):    # reduce mod Q = the recurrence rewrite
        c = r[i]
        for j in range(d + 1):
            r[i - d + j] = (r[i - d + j] - c * Q[j]) % p
    return (r[:d] + [0] * d)[:d]

def powmod(base, e, Q, p):                     # x^e mod Q by binary exponentiation (Kitamasa)
    res = [1] + [0] * (len(Q) - 2)
    base = (base[:len(Q)-1] + [0]*len(Q))[:len(Q)-1]
    while e:
        if e & 1: res = mulmod(res, base, Q, p)
        base = mulmod(base, base, Q, p)
        e >>= 1
    return res

def castle_dh(Q, p, a, b):                     # returns (Alice_pub, Bob_pub, shared_secret)
    g = [0, 1] + [0] * (len(Q) - 3)            # the generator polynomial x
    A, B = powmod(g, a, Q, p), powmod(g, b, Q, p)
    return A, B, powmod(B, a, Q, p)            # x^{ab} mod Q; == powmod(A, b, Q, p)
```

```
>>> p = 10**9 + 7
>>> Q = [-4 % p, 4, -3 % p, 1]                 # char_2 = x^3 - 3x^2 + 4x - 4 (the public castle)
>>> A, B, s = castle_dh(Q, p, 373309869, 566180101)
>>> s == powmod(A, 566180101, Q, p)            # both parties get the same shared secret
True
>>> s
[395423824, 86931747, 647893869]
```

Meaning: a running asymmetric cryptosystem built from the castle's own Kitamasa primitive — the "public castle" is `Q`, the private key is the exponent, and the shared secret is `x^{ab} mod Q`. It is a *teaching* system, not a secure one: `Q` factors (`(x−2)(x²−x+2)`) so the discrete log splits, and Berlekamp–Massey reconstructs `Q` from the count sequence — both attacks are the seminar's point ([[castle-cryptography](pages/castle-cryptography.md)], [[berlekamp-massey](pages/berlekamp-massey.md)]).

### `castle_dlp(A, Q, p)` → recover the private key from a castle public key

The red team's tool ([[castle-cryptography-round-two](pages/castle-cryptography-round-two.md)]): factor `Q mod p`, reduce `A` modulo each factor, solve each piece's discrete log by Pohlig–Hellman over the factored element order with baby-step giant-step on each prime, and Chinese Remainder Theorem (CRT) the pieces. Uses `mulmod` / `powmod` / `one` / `gen` from `castle_dh`. Requires SymPy.

```python
from math import isqrt
from sympy.ntheory.modular import crt

def bsgs(g, h, n, Q, p):                       # solve g^x = h in F_p[x]/(Q), ord(g) | n
    m = isqrt(n) + 1; tbl = {}; cur = one(Q)
    for j in range(m):
        tbl.setdefault(tuple(cur), j); cur = mulmod(cur, g, Q, p)
    step, cur = powmod(g, (n - m) % n, Q, p), h  # g^{-m}
    for i in range(m):
        if tuple(cur) in tbl: return (i*m + tbl[tuple(cur)]) % n
        cur = mulmod(cur, step, Q, p)

def pohlig_hellman(g, h, n, Q, p):             # log_g h, ord(g) = n exactly; cost ~ sqrt(largest prime | n)
    res, mod = 0, 1
    for q, e in sp.factorint(n).items():
        qe = q**e; gq, hq = powmod(g, n // qe, Q, p), powmod(h, n // qe, Q, p)
        x, gam = 0, powmod(gq, q**(e-1), Q, p)
        for i in range(e):
            hk = powmod(mulmod(hq, powmod(gq, (qe - x) % qe, Q, p), Q, p), q**(e-1-i), Q, p)
            x += bsgs(gam, hk, q, Q, p) * q**i
        res, mod = [int(v) for v in crt([mod, qe], [res, x])]
    return res

def elem_order(g, Q, p, N):                    # order of g given a multiple N (e.g. p^d - 1)
    o = N
    for q in sp.factorint(N):
        while o % q == 0 and powmod(g, o // q, Q, p) == one(Q): o //= q
    return o

def castle_dlp(A, Q, p):                       # recover a from A = x^a mod Q: split Q, solve each piece, CRT
    x = sp.Symbol('x'); logs = []
    for f, _ in sp.factor_list(sp.Poly(Q[::-1], x).as_expr(), modulus=p)[1]:
        Qf = [int(c) % p for c in sp.Poly(f, x).all_coeffs()[::-1]]; d = len(Qf) - 1
        if d == 1:                              # linear factor (x - r): the piece is F_p^*, x -> r
            r = (-Qf[0]) % p; Qf, g, h = [0, 1], [r], [sum(c * pow(r, i, p) for i, c in enumerate(A)) % p]
        else:
            g, h = gen(Qf), mulmod(A, one(Qf), Qf, p)
        n = elem_order(g, Qf, p, p**d - 1)
        logs.append((pohlig_hellman(g, h, n, Qf, p), n))
    return [int(v) for v in crt([n for _, n in logs], [a for a, _ in logs])]
```

```
>>> p = 10**9 + 7; Q2 = [-4 % p, 4, -3 % p, 1]              # char_2, the castle_dh public castle
>>> A = powmod(gen(Q2), 373309869, Q2, p); A                 # Alice's public key from castle_dh
[704821174, 848698009, 235195321]
>>> castle_dlp(A, Q2, p)   # Alice's private key, and the modulus it is known mod
[373309869, 500000007000000024] # 0.07s
>>> Q1 = [2, -2 % p, 1]                                      # char_1, irreducible mod p: still falls
>>> castle_dlp(powmod(gen(Q1), 373309869, Q1, p), Q1, p)
[373309869, 4000000024] # 0.04s
>>> sp.factorint(p**2 - 1)                                   # the group order factors even though Q does not
{2: 4, 3: 2, 7: 1, 109: 2, 167: 1, 500000003: 1}
>>> Q3 = [8, -8 % p, 8, -4 % p, 1]                           # char_3, degree 4, irreducible mod p
>>> castle_dlp(powmod(gen(Q3), 373309869, Q3, p), Q3, p)
[373309869, 800000016000000107200000240] # 0.18s
```

Meaning: the private key falls in a fraction of a second whether or not `Q` factors, because `p^d − 1 = ∏_{e|d} Φ_e(p)` factors algebraically and its largest prime here is `500000003 ≈ 2²⁹`. "Irreducible" removed the CRT split of the ring, not of the group ([[castle-cryptography-round-two](pages/castle-cryptography-round-two.md)], Attack 4).

### `bm_modp(s, p)` → Berlekamp–Massey over `F_p`, and the linearization attack

Linear complexity of a sequence mod `p` ([[berlekamp-massey](pages/berlekamp-massey.md)]), used to measure what a nonlinear filter on a castle register actually buys ([[castle-cryptography-round-two](pages/castle-cryptography-round-two.md)], Attack 5). Stdlib only.

```python
def bm_modp(s, p):                             # -> (connection poly low->high, C[0] = 1; linear complexity L)
    C, B, L, m, b = [1], [1], 0, 1, 1
    for n in range(len(s)):
        d = (s[n] + sum(C[i]*s[n-i] for i in range(1, L+1))) % p
        if d == 0: m += 1; continue
        T, coef = C[:], d * pow(b, -1, p) % p
        C = C + [0]*(len(B)+m-len(C))
        for i in range(len(B)): C[i+m] = (C[i+m] - coef*B[i]) % p
        if 2*L <= n: L, B, b, m = n+1-L, T, d, 1
        else: m += 1
    return C, L

def lfsr(Q, init, n, p):                       # run the castle recurrence with char poly Q from initial terms
    s = list(init); d = len(Q) - 1
    while len(s) < n: s.append(sum(-Q[j]*s[-d+j] for j in range(d)) % p)
    return s
```

```
>>> s = lfsr(Q3, [1, 0, -4 % p, -16 % p], 300, p)  # P(3, L) mod p: a 4-stage castle register
>>> bm_modp(s, p)[1]
4
>>> z = [s[i]*s[i+1] % p for i in range(299)]      # 'nonlinear output': product of adjacent terms
>>> C, L = bm_modp(z, p); L                        # = C(5, 2): products of pairs of roots
10
>>> all(sum(C[i]*z[n-i] for i in range(L+1)) % p == 0 for n in range(L, len(z)))   # the recovered recurrence predicts every later term
True
>>> bm_modp(z[:2*L], p) == (C, L)   # 2L terms suffice
True
>>> z3 = [s[i]*s[i+1]*s[i+2] % p for i in range(298)]
>>> bm_modp(z3, p)[1]   # degree-3 filter: C(6,3) = 20
20
```

Meaning: a degree-`e` polynomial filter on a `d`-stage linear register is itself linear of complexity `≤ C(d+e−1, e)` (the characteristic roots are the degree-`e` monomials in the roots of `Q`), so Berlekamp–Massey still recovers it from `2L` terms. Nonlinearity buys a computable increase in `L`, not immunity.

### `castle_schnorr` → ElGamal and a Schnorr-style signature on the `x^a` map

Seminar 1's round-two deliverable ([[castle-cryptography-round-two](pages/castle-cryptography-round-two.md)]): encryption and signatures from the same `powmod` as `castle_dh`, in a prime-order subgroup of `F_p[x]/(char_3) ≅ F_{p⁴}`. The subgroup prime `q = 340715873` divides `p² + 1`, so `⟨g⟩` lives in the genuine degree-4 part of the field (on `char_1` the analogous subgroup collapses to scalars: `x^8 = 16`).

```python
import hashlib, random
Q, N = Q3, p**4 - 1                            # char_3 mod p is irreducible: the ring is F_{p^4}
q = 340715873                                  # a prime factor of p^2 + 1 -> a subgroup living in the genuine degree-4 part
random.seed(502)
while True:
    g = powmod([random.randrange(p) for _ in range(4)], N // q, Q, p)
    if g != one(Q): break
H = lambda *parts: int.from_bytes(hashlib.sha256(repr(parts).encode()).digest(), 'big') % q
def keygen():            a = random.randrange(1, q); return a, powmod(g, a, Q, p)
def enc(pub, m):         k = random.randrange(1, q); return powmod(g, k, Q, p), mulmod(m, powmod(pub, k, Q, p), Q, p)
def dec(a, c1, c2):      s = powmod(c1, a, Q, p); return mulmod(c2, powmod(s, q - 1, Q, p), Q, p)
def sign(a, msg):        k = random.randrange(1, q); e = H(powmod(g, k, Q, p), msg); return e, (k + a*e) % q
def verify(pub, msg, e, s): return H(mulmod(powmod(g, s, Q, p), powmod(pub, (q - e) % q, Q, p), Q, p), msg) == e
```

```
>>> a, pub = keygen(); g, pub
[670690837, 335848460, 27104856, 290696543] [34518600, 853770003, 669598040, 563247297]
>>> dec(a, *enc(pub, [1, 1, 3, 9]))
[1, 1, 3, 9]
>>> e, sg = sign(a, b'castle 502'); (e, sg), verify(pub, b'castle 502', e, sg), verify(pub, b'castle 503', e, sg)
(129461214, 65798226) True False
>>> bsgs(g, pub, q, Q, p) == a   # red team: q is 29 bits, so ~2^15 steps
True # 0.07s
```

Meaning: key exchange, encryption, and signatures all hang off one exponentiation — and the same `bsgs` that the red team wrote for `castle_dlp` recovers the signing key in a fraction of a second, because a 29-bit subgroup is a 15-bit search. The build works; the size does not.

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
- [[pell-castle-strip](pages/pell-castle-strip.md)] — the silver-width-growth-castle example (the anchored 1-smooth height-3 strip, `pell_strip_count`); `is_zero_one_strip` is its golden analog.
- [[oeis-mining-pe502](pages/oeis-mining-pe502.md)] — the OEIS-lookup loop the `oeis_snippet` helper feeds.
- [[convergents-oeis-crosswalk](pages/convergents-oeis-crosswalk.md)] - the analysis the continued-fraction / mod-p / quasi-polynomial snippets were written for; every pinned value here matches that page.
- [[tower-parity-sectors](pages/tower-parity-sectors.md)] / [[plastic-number](pages/plastic-number.md)] - the transfer-matrix, sector, and `H(d)` snippets.
- [[castle-graph](pages/castle-graph.md)] - the `castle_graph`, `is_tree_castle`, `cycle_rank` snippets and the graph concept behind them.
- [[tree-castle-by-area](pages/tree-castle-by-area.md)] - the `tree_area_gf`, `tree_area_by_area` snippets.
- [[castle-graph-spectral-radius](pages/castle-graph-spectral-radius.md)] - the `castle_graph_radius` census.
- [[isospectral-castles](pages/isospectral-castles.md)] / [[hardin-word-identity](pages/hardin-word-identity.md)] - the `compositions` and `word_matrix` snippets.
- [[eigenvalue-continued-fractions](pages/eigenvalue-continued-fractions.md)] / [[mod-p-observatory](pages/mod-p-observatory.md)] - the two sides (real periods, finite-field orders) that `convergents` and `order_mod` compute.
- [[castle-count-algorithms](pages/castle-count-algorithms.md)] / [[kitamasa](pages/kitamasa.md)] — the fast-algorithm side, one abstraction level up.
- [[castle-cryptography](pages/castle-cryptography.md)] / [[castle-cryptography-ring](pages/castle-cryptography-ring.md)] / [[castle-cryptography-round-two](pages/castle-cryptography-round-two.md)] - the `castle_dh`, `castle_dlp`, `bm_modp`, `castle_schnorr` snippets: the build and the attacks of the cryptography seminar series.
- [[aocp-generating-permutations-tuples](pages/aocp-generating-permutations-tuples.md)] - `all_castles(w, h)` is Knuth's Algorithm M (mixed-radix odometer over `{1..h}^w`) with a `max == h` post-filter; the castle Gray code thread starts there.
- [[unique-tournament](pages/unique-tournament.md)] / [[simple-tournament](pages/simple-tournament.md)] / [[forcibly-simple-score-vector](pages/forcibly-simple-score-vector.md)] - the concepts behind `castle_to_composition`, `composition_to_castle`, and `is_strongly_connected`.
- [[new-sequence-fw3](pages/new-sequence-fw3.md)] - `sum(1 for c in all_castles(w, 3) if blocks(c) % 2 == 0)` reproduces `0, 0, 3, 21, 89, 307, …`.
