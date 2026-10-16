---
title: Castle snippets
category: Concepts
summary: Short tested Python snippets that enumerate the castles of width w and height h, count their blocks, test the shape types of castle-classification-shape, and compute the castle graph, its cycle rank and spectral radius, with an exact test for a metallic mean in the spectrum and an OEIS lookup. Three sibling pages carry the snippets for strips and growth, number theory, and cryptography.
tags: [concept, castle, python, snippets, computational, classification, reference]
sources: [project-euler-502-brute-force]
created: 2026-09-16
updated: 2026-10-16
---

# Castle snippets

## Conventions

The snippets on this page enumerate castles, test their shape types, and compute invariants of their graphs. A castle of width `w` and height `h` is a skyline `c = (c_1, …, c_w)` with `1 ≤ c_i ≤ h` and some `c_i = h` ([[castle-polyomino](pages/castle-polyomino.md)]), its block count is that of [[castle-sign](pages/castle-sign.md)], and the type names are those of [[castle-classification](pages/castle-classification.md)]. Each snippet uses only `itertools` and `math` unless it says that it needs NumPy, SymPy or network access, and the output printed under each snippet is the output of running it.[^1] Derivations and full implementations are on [[castle-counting-formula](pages/castle-counting-formula.md)], [[kitamasa](pages/kitamasa.md)] and [[project-euler-502-brute-force](pages/project-euler-502-brute-force.md)].

Three sibling pages carry the snippets of other topics:

- [[castle-snippets-strips](pages/castle-snippets-strips.md)] - growth constants of strip rules, the ridge matrices `R_h = J − D`, plateau-free strips, tower spacing, tree castles by area, the bijection for A005251, and Hardin's word automaton.
- [[castle-snippets-number-theory](pages/castle-snippets-number-theory.md)] - the signed tower count `p_signed`, continued-fraction convergents, orders and periods modulo `p`, the table `P_table`, the split of `P(k, L)` into two polynomials in `k`, the sector transfer matrices, and the factor `H(d)`.
- [[castle-snippets-cryptography](pages/castle-snippets-cryptography.md)] - `castle_dh`, `castle_dlp`, `bm_modp` and `castle_schnorr`, the snippets of the cryptography seminar.

## Enumeration

### `all_castles(w, h)` → list of skylines

The castles of width `w` and height `h`.

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

`len(all_castles(w, h))` is `A(w, h) = h^w − (h−1)^w`; at `(4, 2)`, `16 − 1 = 15`.

### `blocks(c)` → int

The block count, the total ascent `c_1 + Σ_{i≥2} max(0, c_i − c_{i−1})`, as in the dynamic program `p_signed` of [[project-euler-502-brute-force](pages/project-euler-502-brute-force.md)].

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

The number of cells `Σ c_i`, the size of a castle on [[castle-by-area](pages/castle-by-area.md)].

```python
def area(c):
    return sum(c)
```

```
>>> area((2, 1, 2))
5
```

### `castles_where(w, h, pred)` → list of skylines

The castles of width `w` and height `h` that satisfy a predicate `pred`.

```python
def castles_where(w, h, pred):
    return [c for c in all_castles(w, h) if pred(c)]
```

```
>>> len(castles_where(4, 2, is_unimodal))
10
```

`is_unimodal` is defined in the section *Convexity and modality*. The count is the number `C(2h + w − 3, w − 1) = C(5, 3) = 10` of convex castles of width 4 and height 2 ([[convex-castle](pages/convex-castle.md)], [[convex-castle-binomial-identity](pages/convex-castle-binomial-identity.md)]).

## Example: A^e(4, 2) = 10

The even-block castles of width 4 and height 2, counted with `all_castles` and `blocks`:

```python
even = sum(1 for c in all_castles(4, 2) if blocks(c) % 2 == 0)
```

```
>>> even
10
```

This is the value `A^e(4, 2) = (16 − 1 + 4 + 1)/2 = 10` of [[castle-counting-formula](pages/castle-counting-formula.md)], Equation (1), and of the problem statement, which writes it `F(4, 2)`. A castle of height 2 has one block more than the runs of 1s in its second row, so the even-block castles are those whose second row has an odd number of runs. At width 4 that is one run; at width 5 the row `10101`, with three runs, joins the 15 rows with one run, and `A^e(5, 2) = 16`.

## Shape predicates

Each predicate takes a skyline `c`, a tuple or list of positive integers, and returns a Boolean; some also take the height `h`. The sections follow the axes of [[castle-classification-shape](pages/castle-classification-shape.md)].

### Convexity and modality (Axis 1)

```python
def is_unimodal(c):
    """Weakly rises to a maximum, then weakly falls."""
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

def summit_sides(c):
    """Rising steps and falling drops around the run of columns at height h, or None
    unless c is unimodal with at least one column on each side of that run."""
    h = max(c)
    i = c.index(h)
    j = len(c) - 1 - c[::-1].index(h)
    if i == 0 or j == len(c) - 1 or any(x != h for x in c[i:j+1]):
        return None
    up = [c[t+1] - c[t] for t in range(i)]
    down = [c[t] - c[t+1] for t in range(j, len(c) - 1)]
    if min(up) <= 0 or min(down) <= 0:
        return None
    return up, down

def is_hoodoo(c):
    """Rising steps strictly increase, drops strictly decrease."""
    s = summit_sides(c)
    return s is not None and (all(a < b for a, b in zip(s[0], s[0][1:]))
                              and all(a > b for a, b in zip(s[1], s[1][1:])))

def is_monadnock(c):
    """Rising steps strictly decrease, drops strictly increase."""
    s = summit_sides(c)
    return s is not None and (all(a > b for a, b in zip(s[0], s[0][1:]))
                              and all(a < b for a, b in zip(s[1], s[1][1:])))
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
>>> is_hoodoo((2, 3, 6, 16, 35, 35, 25, 18, 14, 12))
True
>>> is_monadnock((2, 21, 31, 34, 35, 35, 33, 29, 22, 12))
True
>>> is_hoodoo((1, 2, 3, 2)), is_monadnock((1, 2, 3, 2))    # equal steps 1, 1
(False, False)
```

The hoodoo example rises by `1, 3, 10, 19` and drops by `10, 7, 4, 2`; the monadnock example rises by `19, 10, 3, 1` and drops by `2, 4, 7, 10`. At height 4 there are 9, 15 and 16 hoodoo castles of widths 3, 4 and 5, and as many monadnock castles.[^1] Related pages: [[convex-castle](pages/convex-castle.md)] for the unimodal castles, [[polyominoes](pages/polyominoes.md)] for the Ferrers and staircase polyominoes, and [[hoodoo-monadnock-castles](pages/hoodoo-monadnock-castles.md)] for a generator of the hoodoo and monadnock castles, checked against these two predicates.

### Rate of change (Axis 2)

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

`is_m_smooth(c, 1)` is the Motzkin-path predicate of the section *Paths* without its end condition `c_1 = c_w = 1`.

### Paths (Axis 3)

```python
def is_dyck_path(c):
    """c_1 = c_w = 1 and |c_{i+1} - c_i| = 1 for all i."""
    return (c[0] == 1 and c[-1] == 1
        and all(abs(c[i+1] - c[i]) == 1 for i in range(len(c)-1)))

def is_motzkin_path(c):
    """c_1 = c_w = 1 and |c_{i+1} - c_i| <= 1 for all i."""
    return (c[0] == 1 and c[-1] == 1
        and all(abs(c[i+1] - c[i]) <= 1 for i in range(len(c)-1)))
```

```
>>> is_dyck_path((1,2,1,2,1))
True
>>> is_motzkin_path((1,2,2,1,1))
True
```

Since every `c_i ≥ 1`, a skyline with `is_dyck_path` is a Dyck path lifted by one row, and one with `is_motzkin_path` a Motzkin path lifted by one row ([[dyck-words](pages/dyck-words.md)], [[motzkin-numbers](pages/motzkin-numbers.md)]).

### Symmetry (Axis 4)

```python
def is_palindromic(c):
    return list(c) == list(c)[::-1]

def is_centrally_symmetric(c, h):
    """c_i + c_{w+1-i} = h + 1: the half-turn about the center of the w x h box
    sends the top cell of each column to the top cell of the opposite column."""
    w = len(c)
    return all(c[i] + c[w-1-i] == h + 1 for i in range(w))
```

```
>>> is_palindromic([1,2,3,2,1])
True
>>> is_centrally_symmetric([1,2,3], 3)
True
```

### Values (Axis 5)

```python
def is_rainbow(c, h):
    """w = h, and the heights are a permutation of {1, ..., h}."""
    return len(c) == h and sorted(c) == list(range(1, h+1))

def is_boxcastle(c, h):
    return all(x == h for x in c)

def is_hook(c, h):
    """c_1 = h, c_i = 1 for i >= 2."""
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

The rainbow castles of height `h` are the `h!` permutations of `{1, …, h}`.

## Graphs

### `castle_graph(c)` → adjacency matrix

The adjacency matrix of the [[castle-graph](pages/castle-graph.md)]: the cells are the vertices, and two cells are joined when they share a side. Requires NumPy.

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
>>> castle_graph((2, 1, 2)).astype(int).tolist()      # the castle (2, 1, 2): a path on 5 cells
[[0, 1, 1, 0, 0], [1, 0, 0, 0, 0], [1, 0, 0, 1, 0], [0, 0, 1, 0, 1], [0, 0, 0, 1, 0]]
```

`np.diag(A.sum(1)) - A` is the Laplacian, `numpy.linalg.eigvalsh` gives the spectrum, and `sympy.Matrix(...).charpoly(x)` the exact characteristic polynomial, the inputs of the spectral types of [[castle-classification-spectrum](pages/castle-classification-spectrum.md)].

### `is_tree_castle(c)`, `cycle_rank(c)`

A castle has no holes, so by Euler's formula for planar graphs the cycle rank `|E| − |V| + 1` of its graph is the number of `2 × 2` squares of cells. Between columns `i` and `i + 1` there are `max(0, min(c_i, c_{i+1}) − 1)` of them, so the graph is a tree exactly when no two neighboring columns both have height at least 2 ([[castle-graph](pages/castle-graph.md)]). A tree has one spanning tree, so the sandpile group of a tree castle is trivial; the sandpile snippets are on [[sandpile-group](pages/sandpile-group.md)], [[sandpile-census](pages/sandpile-census.md)], [[sandcastle-clock](pages/sandcastle-clock.md)], [[sandpile-identity](pages/sandpile-identity.md)] and [[castle-avalanches](pages/castle-avalanches.md)].

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
>>> [sum(1 for c in all_castles(w, 2) if is_tree_castle(c)) for w in range(1, 9)]
[1, 2, 4, 7, 12, 20, 33, 54]
```

The last line is `F_{w+2} − 1` for `w = 1, …, 8`, the tree castles of height 2, which are the Fibonacci castles ([[fibonacci-castle](pages/fibonacci-castle.md)]). The tree castles of height at most 3, 4 and 5 number `A001045(w + 2)` (Jacobsthal), `A006130(w + 1)` and `A006131(w + 1)` ([[castle-graph](pages/castle-graph.md)]).[^1]

### `castle_graph_radius(c)` → float

The largest eigenvalue of the adjacency matrix of the castle graph, the statistic of [[castle-classification-spectrum](pages/castle-classification-spectrum.md)] and of the census on [[castle-graph-spectral-radius](pages/castle-graph-spectral-radius.md)]. Requires NumPy.

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
>>> round(castle_graph_radius((1, 1, 1, 1)), 6)      # the path on 4 cells: phi
1.618034
>>> round(castle_graph_radius((2, 2, 2)), 6)         # the 3 x 2 rectangle: 1 + sqrt(2)
2.414214
>>> round(castle_graph_radius((1, 2, 3, 1, 2, 3)), 6)
2.414214
>>> [c for c in all_castles(3, 2) if abs(castle_graph_radius(c) - (1 + 2**.5)) < 1e-9]
[(2, 2, 2)]
```

The spectral radius of the castle `(1, 1, 1, 1)` is the golden ratio `φ`, so it is golden by spectrum, and that of `(2, 2, 2)` and of `(1, 2, 3, 1, 2, 3)` is the silver ratio `1 + √2`, so they are silver by spectrum ([[castle-classification-spectrum](pages/castle-classification-spectrum.md)]). `castles_where` with a test on `castle_graph_radius` counts the castles of a given spectral radius.

### `metallic_in_spectrum(c, a)` → bool

An exact test of whether the metallic mean `δ_a = (a + √(a² + 4))/2` (golden at `a = 1`, silver at `a = 2`, bronze at `a = 3`) is an eigenvalue of the castle graph. `δ_a` is a root of `x² − ax − 1`. If it is an eigenvalue of the adjacency matrix `A`, then `A² − aA − I` is singular. Conversely, if `A² − aA − I` is singular, some eigenvalue of `A` is a root of `x² − ax − 1`; the characteristic polynomial of `A` has integer coefficients and `δ_a` is irrational, so its conjugate `(a − √(a² + 4))/2` is an eigenvalue only together with `δ_a`. So `δ_a` is an eigenvalue exactly when the integer determinant `det(A² − aA − I)` is 0, which SymPy computes without rounding. [[bronze-castle-hunt](pages/bronze-castle-hunt.md)] uses the test on floating-point near-misses. Requires NumPy and SymPy, and uses `castle_graph`.

```python
import numpy as np
from sympy import Matrix

def metallic_in_spectrum(c, a):
    A = castle_graph(c).astype(int)
    return Matrix(A @ A - a * A - np.eye(len(A), dtype=int)).det(method='bareiss') == 0
```

```
>>> metallic_in_spectrum((1, 1, 1, 1), 1), metallic_in_spectrum((2, 2, 2), 2), metallic_in_spectrum((1, 2, 3, 1, 2, 3), 2)
(True, True, True)
>>> near = (4, 4, 1, 4, 4, 1, 3, 5, 3, 1, 2, 4, 5, 4, 5, 1)
>>> "%.1e" % (castle_graph_radius(near) - (3 + 13**.5)/2)
'2.3e-12'
>>> metallic_in_spectrum(near, 3)
False
```

The castle `near`, with 51 cells, has a spectral radius within `2.3 × 10⁻¹²` of the bronze ratio in floating point, and the bronze ratio is not an eigenvalue of its graph.

## Castles by area

### `compositions(n)` → the castles with `n` cells

A castle with `n` cells is a composition of `n`, since every column has height at least 1, so there are `2^{n−1}` of them over all widths and heights. Enumerating by area is the loop of the search on [[isospectral-castles](pages/isospectral-castles.md)].

```python
def compositions(n):
    if n == 0: yield (); return
    for first in range(1, n+1):
        for rest in compositions(n-first): yield (first,) + rest
```

```
>>> list(compositions(3))
[(1, 1, 1), (1, 2), (2, 1), (3,)]
>>> sum(1 for c in compositions(10) if not c[::-1] < c)      # 10-cell castles up to mirror image
272
```

Of the `2^9 = 512` compositions of 10, `2^5 = 32` are palindromes, so `(512 + 32)/2 = 272` castles of 10 cells remain up to mirror image.

## OEIS

### `oeis_snippet(seq)` → string

A sequence formatted for the search box of oeis.org.

```python
def oeis_snippet(seq, n=10):
    return ", ".join(str(x) for x in seq[:n])
```

```
>>> oeis_snippet([1, 2, 5, 12, 29, 70, 169, 408, 985, 2378])
'1, 2, 5, 12, 29, 70, 169, 408, 985, 2378'
>>> oeis_snippet([sum(1 for c in all_castles(w, 2) if blocks(c) % 2 == 0)
...               for w in range(1, 9)])
'1, 3, 6, 10, 16, 28, 56, 120'
```

The second line is `A^e(w, 2)` for `w = 1, …, 8`, which is `A038505(w + 1)` ([[oeis-height2-hyperbolic-castles](pages/oeis-height2-hyperbolic-castles.md)]).

### `oeis_lookup(terms)` → list of `(A-number, name)`

A search of oeis.org. It needs network access and `curl`: oeis.org answers a request with the default user agent of Python's `urllib` with HTTP status 403 (observed 2026-10-16), so the snippet sends a browser user agent through `curl`, one request at a time with a pause of a second between requests.

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

A search result is a candidate match until its stored terms and offset agree with the castle count; `https://oeis.org/search?q=id:A005251&fmt=json` returns the fields `offset` and `data` to compare ([[oeis-cross-referencing](pages/oeis-cross-referencing.md)]).

## Extensions

- Predicates combine in one filter, as in `castles_where(w, h, lambda c: is_unimodal(c) and blocks(c) % 2 == 0)`.
- A `collections.Counter` over a statistic such as `blocks`, `area` or the number of peaks gives a distribution in place of a count.
- `all_castles(w, h)` builds all `h^w` tuples. The dynamic program on [[project-euler-502-brute-force](pages/project-euler-502-brute-force.md)] counts larger cases, and [[castle-count-algorithms](pages/castle-count-algorithms.md)] the Project Euler parameters.
- A skyline can also be built from a step string ([[urd-step-strings](pages/urd-step-strings.md)]) or from binary strings of runs ([[binary-string-bijection](pages/binary-string-bijection.md)]).

## Appearances in Sources

- [[project-euler-502-brute-force](pages/project-euler-502-brute-force.md)] - the reference `blocks_of`, `is_unimodal` and the dynamic program `p_signed`, which `blocks` and `is_unimodal` here agree with.

## Related Concepts

- [[castle-classification](pages/castle-classification.md)] - the classification of castles by shape, spectrum and growth, whose shape types the predicates test.
- [[castle-representations](pages/castle-representations.md)] - the skyline encoding the snippets use.
- [[castle-sign](pages/castle-sign.md)] - the block count as total ascent and as total descent.
- [[oeis-mining-pe502](pages/oeis-mining-pe502.md)] - the first pass of castle counts against the OEIS.
- [[castle-graph](pages/castle-graph.md)] - the castle graph, its cycle rank, and the tree castles by height.
- [[castle-graph-spectral-radius](pages/castle-graph-spectral-radius.md)] - the census of spectral radii.

## Footnotes

[^1]: Verified by execution (Python 3.11 with NumPy and SymPy, 2026-10-16): every snippet on this page run as shown, and every printed output reproduced, `oeis_lookup` included; the hoodoo and monadnock counts 9, 15, 16 at height 4 and widths 3, 4, 5; the cycle rank against `|E| − |V| + 1` for every castle with `w ≤ 5`, `h ≤ 4`; the tree castles of height at most 3, 4, 5 against A001045, A006130, A006131 for `w ≤ 8`, `w ≤ 7`, `w ≤ 6`; the HTTP status 403 for `urllib`'s default user agent.
