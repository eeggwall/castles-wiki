---
title: Metallic means in castle spectra
category: Analyses
summary: Where the metallic means do and do not appear as eigenvalues. The count F(w,h) grows like h^w/2, so its transfer-matrix growth constant is h; the signed transfer matrix's eigenvalues are 2 × algebraic units or roots of a leading-coefficient-2 factor, so no metallic mean is ever among them (ρ_1 = √2, ρ_2 = 2, ρ_4 = 2.796, ρ_6 = 2ψ², …). Metallic means are the spectral radii of 2-state class transfer matrices (Axis 8) and of individual castle graphs: φ for the six 4-cell path castles, 1+√2 for 36 castles up to width 8 (the 3×2 rectangle and 35 non-rectangular ones), φ² for three more; copper and beyond are impossible (max degree 4); bronze absent among 4.87 million castles; one castle lands within 10⁻⁸ of 2ψ² without equalling it. First Axis 9 data.
tags: [analysis, castle, spectral, adjacency, transfer-matrix, metallic-means, golden-ratio, silver-ratio, axis-9, isospectral, numpy, sympy, verification]
sources: [project-euler-502-castle-factoring, oeis-mining-pe502, project-euler-502-solution]
created: 2026-09-16
updated: 2026-09-19
---

# Metallic means in castle spectra

## The question

Do the metallic means `δ_a = (a + √(a²+4))/2` of [[metallic-means](pages/metallic-means.md)] have anything to do with the spectra catalogued on [[spectral-analysis](pages/spectral-analysis.md)]? Three different spectra are in play - the transfer matrix of the count, the transfer matrices of castle *classes*, and the adjacency matrix of an individual castle's polyomino graph - and the answer differs for each. Every value below was computed by the snippets shown.

## 1. The count's transfer matrix: growth constant `h`, never metallic

`F(w,h) = [h^w − (h−1)^w − P(h−1,w) + P(h−2,w)]/2`,[^1] and the signed terms grow like `ρ_{h−1}^w` with `ρ_k < k+1` ([[generating-function-gallery](pages/generating-function-gallery.md)]), so

```
F(w, h)  ~  h^w / 2        as w → ∞,       λ_1(h) = h.
```

The growth constant of the actual castle count is the integer `h` - the per-column state count - and nothing else. At `h = 2`:

```
>>> F(w,2), w = 1..14
[1, 3, 6, 10, 16, 28, 56, 120, 256, 528, 1056, 2080, 4096, 8128]      # ratios -> 2;  F(13,2) = 2^12
```

The interesting spectrum is the **signed** transfer matrix `M_k` (`k = h − 1`), whose eigenvalues are the roots of `char_k` and set the *correction* terms. Its dominant eigenvalues are

| `h` | `k` | `ρ_k` | value | metallic? |
|---|---|---|---|---|
| 2 | 1 | `|1 ± i|` | `√2 = 1.414` | no |
| 3 | 2 | `2` | `2` | no |
| 4 | 3 | complex pair | `2.193` | no |
| 5 | 4 | root of `λ³ − 3λ² + 2λ − 4` | `2.796` | no |
| 6 | 5 | complex pair | `2.892` | no |
| 7 | 6 | `2ψ²` ([[plastic-number](pages/plastic-number.md)]) | `3.510` | no |

and **no metallic mean is an eigenvalue of any `M_k`** - checked numerically for `k ≤ 20`, and true in general: by [[tower-parity-sectors](pages/tower-parity-sectors.md)] every eigenvalue is `2μ` with `μ` a root of the monic integer polynomial `H_d` or of `V_d`, which has leading coefficient 2. A metallic mean `δ_a` has `δ_a/2` with minimal polynomial `4x² − 2ax − 1`: not an algebraic integer, so not a root of `H_d`, and with leading coefficient 4, which cannot divide 2, so not a factor of `V_d` either (Gauss's lemma).[^4] The castle's version of "metallic" is **twice a unit** - the `2` is the binary per-column state (`P_even(2,L) = 2^L` exactly), and the unit is a root of `H_d` (`ψ²` at `k = 6`).

## 2. Class transfer matrices: this is where Axis 8 lives, correctly

A metallic mean *is* a spectral radius - of the 2-state matrix `[[a, 1], [1, 0]]`, the convergent matrix of `[a; a, a, …]` ([[convergents-oeis-crosswalk](pages/convergents-oeis-crosswalk.md)]). The [[pell-castle-strip](pages/pell-castle-strip.md)] (`1 − 2x − x²`, spectral radius `1 + √2`; its 0/1 transfer matrix is the `3×3` 1-smooth matrix on heights `{1,2,3}`) and the height-2 tree castles (`1 − x − x²`, `φ`; `2×2` matrix `[[1,1],[1,0]]`) are castle *classes* with their own transfer matrices, and "silver width growth castle" on [[castle-classification](pages/castle-classification.md)] Axis 8 means exactly "the class's transfer matrix has spectral radius `1 + √2`." That usage is sound. What the metallic means are *not* is eigenvalues of PE 502's own count.

## 3. Adjacency spectra of individual castles: golden and silver castles exist

Treat the filled cells as vertices with orthogonal-adjacency edges (the Axis 9 graph) and take the largest adjacency eigenvalue:

```python
import numpy as np
from itertools import product

def castle_graph_radius(c):
    """Largest adjacency eigenvalue of the polyomino graph of the skyline c."""
    cells = [(i, j) for i, h in enumerate(c) for j in range(h)]
    idx = {cell: n for n, cell in enumerate(cells)}
    A = np.zeros((len(cells), len(cells)))
    for (i, j), n in idx.items():
        for nb in ((i+1, j), (i, j+1)):
            if nb in idx: A[n, idx[nb]] = A[idx[nb], n] = 1
    return np.linalg.eigvalsh(A)[-1]

named = {"phi": (1+5**.5)/2, "1+sqrt2": 1+2**.5, "bronze": (3+13**.5)/2, "phi^2": (3+5**.5)/2}
found = {name: [] for name in named}
for w in range(1, 8):
    for h in range(1, 7):
        if w == 7 and h == 6: continue
        for c in product(range(1, h+1), repeat=w):
            if max(c) != h: continue
            r = castle_graph_radius(c)
            for name, val in named.items():
                if abs(r - val) < 1e-9: found[name].append(c)
```

```
castles scanned: 134111        (all w <= 6, h <= 6, plus w = 7, h <= 5)
phi      (1.618034): 6 castles: (4,), (1,3), (3,1), (1,1,2), (2,1,1), (1,1,1,1)
1+sqrt2  (2.414214): 8 castles: (3,3), (2,2,2), (1,2,3,1,2,3), (3,2,1,3,2,1), (2,1,6,2,1,3), (3,1,2,6,1,2), (1,1,2,4,1,3,1), (1,3,1,4,2,1,1)
phi^2    (2.618034): 3 castles: (4,4), (2,2,2,2), (1,3,2,3,1)
bronze   (3.302776): 0 castles
```

Exact characteristic polynomials confirm the floating-point matches:[^3]

```
(1,1,1,1)          (x**2 - x - 1)*(x**2 + x - 1)                                        # P_4: spectrum ±phi, ±1/phi
(2,2,2)            (x - 1)*(x + 1)*(x**2 - 2*x - 1)*(x**2 + 2*x - 1)                    # P_2 x P_3
(1,2,3,1,2,3)      x**2*(x - 1)*(x + 1)*(x**2 - 2*x - 1)*(x**2 + 2*x - 1)*(x**4 - 6*x**2 + 6)
(2,1,6,2,1,3)      x*(x - 1)*(x + 1)*(x**2 - 3)*(x**2 - 2)*(x**2 - 2*x - 1)*(x**2 - x - 1)*(x**2 + x - 1)*(x**2 + 2*x - 1)
(1,1,2,4,1,3,1)    x*(x - 1)*(x + 1)*(x**2 - 2)*(x**2 - 2*x - 1)*(x**2 + 2*x - 1)*(x**4 - 4*x**2 + 2)
(4,4)              (x**2 - 3*x + 1)*(x**2 - x - 1)*(x**2 + x - 1)*(x**2 + 3*x + 1)     # P_2 x P_4
(1,3,2,3,1)        (x - 1)*(x + 1)*(x**2 - 3*x + 1)*(x**2 - x - 1)*(x**2 + x - 1)*(x**2 + 3*x + 1)
```

**Why these.** Path graphs have spectrum `2cos(jπ/(n+1))`, and Cartesian-product spectra add. `P_4` has `2cos(π/5) = φ`, so every 4-cell castle whose graph is a path - all six of them, `(4)`, `(1,3)`, `(3,1)`, `(1,1,2)`, `(2,1,1)`, `(1,1,1,1)` - is a **golden-spectrum castle**. `P_2 × P_3` has `1 + √2` (`2cos(π/3) + 2cos(π/4)`), so the `3 × 2` rectangle `(3,3) = (2,2,2)` is a **silver-spectrum castle**; `P_2 × P_4` has `1 + φ = φ²`. The three non-rectangular silver castles are the real content:

```
(1,2,3,1,2,3)      (2,1,6,2,1,3)      (1,1,2,4,1,3,1)
..#..#             ..#...             ...#...
.##.##             ..#...             ...#...
######             ..#...             ...#.#.
                   ..#...             ..##.#.
                   #.##.#             #######
                   ######
```

They are not products, yet `x² − 2x − 1` divides their characteristic polynomials exactly, and `(2,1,6,2,1,3)` carries `φ` and `1 + √2` in the same spectrum. The double staircase `(1,2,3,1,2,3)` and its mirror are 12-cell castles with the same spectral radius as the 6-cell rectangle - a spectral-radius coincidence between structurally different shapes, which is the kind of object the Axis 9 isospectral hunt is looking for.

**What cannot happen, and the big scan.** A castle graph is a subgraph of the square grid, so its maximum degree is at most 4 and its spectral radius is strictly below 4 for every finite castle. Copper `2 + √5 = 4.236`, nickel, and every higher metallic mean are therefore **never** the spectral radius of a castle graph. Bronze `(3 + √13)/2 = 3.303` is below the bound, so it was hunted at scale: **4,868,525 castles** (mirror-deduped; all `w ≤ 8, h ≤ 7`, plus `w = 9, h ≤ 5` and `w = 10, h ≤ 4`), prefiltered by the edge bound `ρ ≤ max_{uv} √(d_u d_v)` (a radius above 3.3 needs an edge whose endpoint degrees multiply to at least 11), then `eigvalsh`. **No bronze castle.** The same scan found 36 silver castles (6 to 20 cells; e.g. `(1,1,2,1,4,2,1,1)`, `(3,2,1,2,2,1,2,3)`, `(1,2,4,1,3,1,2,6)`) and exactly one castle whose radius lies within `10⁻⁸` of `2ψ² = 3.510`:

```
(1,1,2,7,7,5,7,7)      radius 3.50975532447636…      2ψ² = 3.50975533249338…      difference −8.0·10⁻⁹
...##.##
...##.##
...#####
...#####
...#####
..######
########
```

Its exact characteristic polynomial is `x(x−1)(x+1)·(irreducible degree 34)`, not divisible by `x³ − 4x² + 4x − 8`, so this is a near-miss, not a plastic-spectrum castle - and a reminder that a floating-point match at `10⁻⁸` over five million candidates is not evidence of anything until the exact polynomial is factored.[^3] Whether any castle has spectral radius exactly bronze or `2ψ²` remains open beyond the scanned sizes.

## Axis 9 types this populates

- **Golden-spectrum castle** - adjacency spectral radius `φ`. Members: the six 4-cell paths (all isomorphic to `P_4`, so one graph). The predicate is exactly "the polyomino graph is `P_4`" at this size; whether any larger castle has spectral radius `φ` is open (a connected graph with spectral radius `< 2` is a Dynkin path or star, so no).
- **Silver-spectrum castle** - adjacency spectral radius `1 + √2`. Members up to `w = 7`: the `3 × 2` rectangle and three mirror pairs of non-rectangular castles listed above.
- **Golden-squared-spectrum castle** - radius `φ²`: `P_2 × P_4` and `(1,3,2,3,1)`.

Each is a single-castle predicate, exactly the shape Axis 9 on [[castle-classification](pages/castle-classification.md)] asks for, and the first with computed members beyond the Ramanujan stub.

## A fourth, speculative link

A skyline that is a Sturmian word - two heights arranged by the rotation with slope `1/φ` (the Fibonacci word) - is a one-dimensional quasicrystal, and its diffraction (the skyline-DFT method on [[spectral-analysis](pages/spectral-analysis.md)]) has the self-similar singular-continuous spectrum of the Fibonacci chain. That would put the golden ratio into a castle's *DFT* spectrum as a rotation number rather than as an eigenvalue. Not computed here; noted as a thread.

## Appearances in Sources

- [[project-euler-502-castle-factoring](pages/project-euler-502-castle-factoring.md)] - the `F(w,h)` formula whose `h^w` term sets the growth constant.
- [[oeis-mining-pe502](pages/oeis-mining-pe502.md)] / [[project-euler-502-solution](pages/project-euler-502-solution.md)] - `char_k` and the `ρ_k` values.

## Related Concepts

- [[spectral-analysis](pages/spectral-analysis.md)] - the methods hub; this page settles its `λ_1(h)` target and supplies Axis 9 data.
- [[castle-classification](pages/castle-classification.md)] - Axis 8 (class growth constants, where metallic means correctly live) and Axis 9 (single-castle spectral predicates, populated here).
- [[metallic-means](pages/metallic-means.md)] / [[pell-castle-strip](pages/pell-castle-strip.md)] - the family, and the class (the anchored 1-smooth height-3 strip) whose transfer matrix has spectral radius `1 + √2`.
- [[tower-parity-sectors](pages/tower-parity-sectors.md)] / [[plastic-number](pages/plastic-number.md)] - why the signed transfer matrix's eigenvalues are twice units, and `ρ_6 = 2ψ²`.
- [[generating-function-gallery](pages/generating-function-gallery.md)] - the `ρ_k` table.
- [[hyperbolic-sequence-family](pages/hyperbolic-sequence-family.md)] - `F(w,2) = A038505(w+1)`, growth 2.
- [[castle-graph](pages/castle-graph.md)] - the polyomino graph itself as a concept, with the tree case and its Fibonacci / Jacobsthal / k-Fibonacci counts.
- [[castle-snippets](pages/castle-snippets.md)] - `castle_graph_radius` is filed there.
- [[isospectral-castles](pages/isospectral-castles.md)] - the full-spectrum question: smallest non-isomorphic castles with equal adjacency spectrum (10 cells), equal Laplacian spectrum (11), both (16); no two silver castles are isospectral.
- [[aocp-generating-permutations-tuples](pages/aocp-generating-permutations-tuples.md)] - the 4.87-million-castle census is Knuth's Algorithm M over `{1..h}^w`; [[aocp-permutations](pages/aocp-permutations.md)] - it sits at Knuth's `10! ≈ 3.6 × 10^6` "ceiling on brute-force enumeration".

## Footnotes

[^1]: [[project-euler-502-castle-factoring](pages/project-euler-502-castle-factoring.md)] §"The sign of a castle" L123-127 - "F(w,h) = (h^w - (h-1)^w - P(h-1,w) + P(h-2,w))/2." `F(w,2)` values re-enumerated here for `w ≤ 14`.

[^2]: [[oeis-mining-pe502](pages/oeis-mining-pe502.md)] `mine-notes.md` §"Vein 1" L31-37 - the `P(k,·)` characteristic polynomials with constant term `(−1)^{k−1} 2^k`; `ρ_k` values from [[generating-function-gallery](pages/generating-function-gallery.md)], re-computed here.

[^3]: Verified by execution (NumPy 1.x `eigvalsh`, SymPy 1.14 `charpoly`/`factor`, mpmath `polyroots` at 40 digits): first census over all skylines with `max c = h` for `w ≤ 6, h ≤ 6` and `w = 7, h ≤ 5` (134,111 castles) at tolerance `1e−9`; exact characteristic polynomials for the seven castles listed. Big scan: 4,868,525 mirror-deduped castles over `w ≤ 8, h ≤ 7`, `w = 9, h ≤ 5`, `w = 10, h ≤ 4`, edge-bound prefilter, tolerance `1e−8`, 211 s; bronze 0, silver 36, `2ψ²` one candidate `(1,1,2,7,7,5,7,7)` whose exact polynomial factors as `x(x−1)(x+1)` times an irreducible degree-34 polynomial with dominant root `3.509755324476362682941485`, i.e. `8.0·10⁻⁹` below `2ψ²`.

[^4]: Verified by execution: no eigenvalue of `M_k` (`k ≤ 20`) within `1e−6` of `δ_a` for `a ≤ 6`. The general argument uses the factorization `char_k(2μ)/2^k = H_{k/2}(μ)·V_{k/2}(μ)` of [[tower-parity-sectors](pages/tower-parity-sectors.md)] (monic `H`, leading coefficient 2 for `V`) for even `k`, and irreducibility of `char_k` over `Q` with constant term `±2^k` for odd `k` (a quadratic factor `x² − ax − 1` would contradict irreducibility).
