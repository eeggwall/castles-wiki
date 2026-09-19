---
title: Castle snippets - Python one-liners
category: Concepts
summary: Living reference of short, tested Python snippets for enumerating castles, checking classification predicates, and computing basic graph invariants. Three sibling pages carry the strips/growth, number-theory, and cryptography snippets.
tags: [concept, castle, python, snippets, computational, classification, reference]
sources: [project-euler-502-brute-force]
created: 2026-09-16
updated: 2026-09-19
---

# Castle snippets - Python one-liners

## What this is

A living reference of **short, tested Python snippets** for exploring castles computationally. Each snippet:

- Runs in a plain Python REPL (no external deps unless one line justifies the import - `itertools`, `math`).
- Follows the wiki's conventions: skyline `c = (c_1, …, c_w)` with `1 ≤ c_i ≤ h` and `max c = h` matches [[castle-representations](pages/castle-representations.md)]; block count matches [[castle-sign](pages/castle-sign.md)] and [[project-euler-502-brute-force](pages/project-euler-502-brute-force.md)]; classification names match [[castle-classification](pages/castle-classification.md)].
- Was **executed during ingest**; every printed output is pinned. If a snippet's output disagrees with what this page shows, the wiki is wrong - file a fix.

The purpose is not derivations or full implementations (see [[castle-counting-formula](pages/castle-counting-formula.md)], [[kitamasa](pages/kitamasa.md)], [[project-euler-502-brute-force](pages/project-euler-502-brute-force.md)] for those). The purpose is: **"the wiki mentions class X; here is a two-line function that generates it."**

## Sibling snippet pages (by arc)

The strips-and-growth, number-theory, and cryptography arcs each have their own snippet page; this page keeps the enumeration primitives and Axis 1-7 classification predicates.

- [[castle-snippets-strips](pages/castle-snippets-strips.md)] - Axis-8 growth-constant probes, the ceiling-exception ladder, the plateau-free strip census, tower-spacing, tree-castle-by-area, the A005251 bijection, and Hardin's word automaton.
- [[castle-snippets-number-theory](pages/castle-snippets-number-theory.md)] - the signed tower count `p_signed`, continued-fraction convergents, mod-`p` orders / Pisano-type periods, `P_table`, quasi-polynomial splits, sector transfer matrices, and the `H(d)` factor.
- [[castle-snippets-cryptography](pages/castle-snippets-cryptography.md)] - `castle_dh` / `castle_dlp` / `bm_modp` / `castle_schnorr`: the build-and-attack cryptography seminar snippets.

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


## Classification predicates — Axes 1-7 of [[castle-classification-shape](pages/castle-classification-shape.md)]

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

Wiki ties: [[convex-castle](pages/convex-castle.md)] (unimodal), [[polyominoes](pages/polyominoes.md)] (Ferrers/staircase in the taxonomy), [[castle-classification-shape](pages/castle-classification-shape.md)] Axis 1.

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

Wiki ties: [[castle-classification-shape](pages/castle-classification-shape.md)] Axis 2. Note `is_m_smooth(c, 1)` is the **Motzkin-path** predicate without its endpoint condition `c_1 = c_w = 1` — see Axis 3 below.

### Axis 3: Path-like

```python
def is_dyck_path(c, h):
    """c_1 = c_w = 1, min = 1, |Delta| = 1 always."""
    return (c[0] == 1 and c[-1] == 1 and min(c) == 1
        and all(abs(c[i+1] - c[i]) == 1 for i in range(len(c)-1)))

def is_motzkin_path(c):
    """c_1 = c_w = 1, |Delta| <= 1 always (Dyck-path with flat steps allowed)."""
    return (c[0] == 1 and c[-1] == 1
        and all(abs(c[i+1] - c[i]) <= 1 for i in range(len(c)-1)))
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

Wiki tie: [[castle-classification-shape](pages/castle-classification-shape.md)] Axis 4.

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

Wiki ties: [[castle-classification-shape](pages/castle-classification-shape.md)] Axis 5. **Rainbow castles are in bijection with `S_h`** — the [[castles-as-upgraded-cycle-count](pages/castles-as-upgraded-cycle-count.md)] triad applies directly (not as an upgrade) to this class.


## Graph and enumeration primitives (Axis 9, tree predicate)

The following snippets take a skyline and return graph-theoretic invariants or run direct-enumeration helpers used across the wiki.

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

Meaning: swap in `L = np.diag(A.sum(1)) - A` for the combinatorial Laplacian; feed to `numpy.linalg.eigvalsh` for the spectrum; feed to `sympy.Matrix(...).charpoly(x)` for the exact characteristic polynomial. All Axis 9 predicates on [[castle-classification-spectrum](pages/castle-classification-spectrum.md)] are one line off this.


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


### `castle_graph_radius(c)` → float

Largest adjacency eigenvalue of the castle's polyomino graph (cells as vertices, orthogonal neighbors as edges) - the Axis 9 statistic of [[castle-classification-spectrum](pages/castle-classification-spectrum.md)] and the census on [[castle-graph-spectral-radius](pages/castle-graph-spectral-radius.md)]. Requires NumPy.

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

- [[project-euler-502-brute-force](pages/project-euler-502-brute-force.md)] - the `p_signed` DP, `blocks_of`, and `is_unimodal` reference implementations the wiki-convention snippets above match.

## Related Concepts

- [[castle-classification](pages/castle-classification.md)] - the classification framework the predicates instantiate.
- [[castle-representations](pages/castle-representations.md)] - the skyline encoding all snippets predicate on.
- [[castle-sign](pages/castle-sign.md)] - the block-count convention `blocks(c)` matches.
- [[oeis-mining-pe502](pages/oeis-mining-pe502.md)] - the OEIS-lookup loop the `oeis_snippet` helper feeds.
- [[castle-graph](pages/castle-graph.md)] - the `castle_graph`, `is_tree_castle`, `cycle_rank` snippets and the graph concept behind them.
- [[castle-graph-spectral-radius](pages/castle-graph-spectral-radius.md)] - the `castle_graph_radius` census.
- [[castle-snippets-strips](pages/castle-snippets-strips.md)] / [[castle-snippets-number-theory](pages/castle-snippets-number-theory.md)] / [[castle-snippets-cryptography](pages/castle-snippets-cryptography.md)] - the arc-specific snippet pages this hub points to.
