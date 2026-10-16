---
title: Metallic means in castle spectra
category: Analyses
summary: Where de Spinadel's metallic means appear as eigenvalues on the wiki. The castle count A^e(w, h) ~ h^w/2 grows at the integer h, the largest eigenvalue of the unsigned transfer matrix; the signed transfer matrix M̃_k has spectral radius ρ_k < k + 1, and no δ_a is an eigenvalue of any M̃_k, since every eigenvalue is twice a root of an integer polynomial with leading coefficient 2 (ρ_2 = 2 is copper, σ_1^2). The metallic means are spectral radii of transfer matrices of castle families (the Pell strip is silver by width, the Fibonacci castles golden by width) and of castle graphs. A castle is golden by spectrum when its castle graph has spectral radius φ, which holds for exactly the six castles whose graph is the path P_4, and silver by spectrum at 1 + √2, which holds for 36 castles up to mirror image among 4,868,525 scanned (6 to 20 cells); 11 have spectral radius φ², none in the scan has bronze, and no castle graph has spectral radius δ_a for a ≥ 4.
tags: [analysis, castle, spectral, adjacency, transfer-matrix, metallic-means, golden-ratio, silver-ratio, spectral-type, isospectral, numpy, sympy, verification]
sources: [project-euler-502-castle-factoring, oeis-mining-pe502, project-euler-502-solution]
created: 2026-09-16
updated: 2026-10-16
---

# Metallic means in castle spectra

## The question

The metallic means of [[metallic-means](pages/metallic-means.md)] are de Spinadel's `σ_p^q = (p + √(p² + 4q))/2`, the positive roots of `x² − px − q`, with `δ_a = σ_a^1`: golden `φ = δ_1`, silver `1 + √2 = δ_2`, bronze `(3 + √13)/2 = δ_3`, and copper `σ_1^2 = 2`. Three spectra on the wiki could contain them: the transfer matrices of the castle count, the transfer matrices of castle families, and the adjacency matrices of individual castle graphs. Sections 1 to 3 take them in turn.

## 1. The transfer matrices of the castle count

**Unsigned.** The skylines of width `w` with heights in `{1, …, h}` are read column by column with no restriction, so their transfer matrix is the all-ones `h × h` matrix, with eigenvalues `h` and 0. The count `A(w, h) = h^w − (h−1)^w` of castles of width `w` and height `h` grows at the integer `h`.

**Signed.** The signed tower count is `P(k, L) = e_0ᵀ M̃_k^L v`, where `M̃_k` is the signed transfer matrix on the tower heights `0, …, k` and `char_k` its characteristic polynomial ([[tower-parity-sectors](pages/tower-parity-sectors.md)]). Write `ρ_k` for its spectral radius. Every entry of `M̃_k` is `±1`, so `ρ_k ≤ k + 1`, the largest absolute row sum. For `k ≥ 1` the inequality is strict. By the Perron-Frobenius theorem in the form of Brouwer and Haemers, Theorem 2.2.1(vi), a matrix `S` with `|S| ≤ T`, `T ≥ 0` irreducible, has an eigenvalue of modulus `ρ(T)` only if `S = cETE^{−1}` with `E` diagonal unitary and `|c| = 1`, so only if `S` has rank 1.[^5] Here `|M̃_k|` is the all-ones matrix, and `M̃_k` has rank at least 2: in the convention of [[tower-parity-sectors](pages/tower-parity-sectors.md)], its row 0 is all 1s and its row 1 is `(−1, 1, …, 1)`. So `ρ_k < k + 1`, the signed count `S(w, h) = P(h−2, w) − P(h−1, w)` is `o(h^w)`, and[^1]

```
A^e(w, h)  =  ( A(w, h) + S(w, h) ) / 2   ~   h^w / 2        as w → ∞.
```

At `h = 2` the values for `w = 1, …, 14` are `1, 3, 6, 10, 16, 28, 56, 120, 256, 528, 1056, 2080, 4096, 8128`, with `A^e(13, 2) = 2^12`.[^3]

The spectral radii of the first signed matrices:[^2][^3]

| `h` | `k = h − 1` | dominant eigenvalues of `M̃_k` | `ρ_k` | degree of `ρ_k` over Q |
|---|---|---|---|---|
| 2 | 1 | `1 ± i` | `√2 = 1.414` | 2 |
| 3 | 2 | `2` | `2` | 1 |
| 4 | 3 | a complex pair | `2.193` | 8 |
| 5 | 4 | the real root of `λ³ − 3λ² + 2λ − 4` | `2.796` | 3 |
| 6 | 5 | a complex pair | `2.892` | 18 |
| 7 | 6 | `2ψ²`, `ψ` the plastic number ([[plastic-number](pages/plastic-number.md)]) | `3.510` | 3 |

A member `σ_p^q` of the family has degree at most 2, so `ρ_3, …, ρ_6` are not metallic means; `ρ_2 = 2` is copper, `σ_1^2`.

**Proposition.** No `δ_a`, `a ≥ 1`, is an eigenvalue of any `M̃_k`.

*Proof.* Let `g_k(μ) = char_k(2μ)/2^k`. The recurrence `char_{k+1}(λ) = λ² char_{k−1}(λ) − 2 char_k(λ)` ([[signed-tower-count](pages/signed-tower-count.md)], the section *Recurrences in L*) becomes `g_{k+1} = μ² g_{k−1} − g_k`, with `g_0 = 2μ − 1` and `g_1 = 2μ² − 2μ + 1`. By induction, each `g_k` has integer coefficients and leading coefficient 2. If `δ_a` were an eigenvalue, `δ_a/2` would be a root of `g_k`. Its minimal polynomial over Q is `4μ² − 2aμ − 1`, which is irreducible because `a² + 4` is not a square for `a ≥ 1`, and primitive. By Gauss's lemma it would divide `g_k` in `Z[μ]`, so 4 would divide the leading coefficient 2.[^4]

For `k ≤ 30`, `ρ_k/2` is a root of a monic integer factor of `g_k` with constant term `−1` exactly when `k ≡ 2 (mod 4)`; for those `k` the dominant eigenvalue is twice a unit, a root of `H_{k/2}` in the notation of [[tower-parity-sectors](pages/tower-parity-sectors.md)] (`ψ²` at `k = 6`). For the other `k ≤ 30`, the factor that contains `ρ_k/2` has leading coefficient 2.[^3]

## 2. The transfer matrices of castle families

`δ_a` is the spectral radius of the matrix `[[a, 1], [1, 0]]`, and `σ_p^q` that of `[[p, q], [1, 0]]`, since their characteristic polynomials are `x² − ax − 1` and `x² − px − q`. Two castle families have transfer matrices with metallic spectral radii:

- The anchored 1-smooth strips on the heights `{1, 2, 3}` have the `3 × 3` transfer matrix `[[1, 1, 0], [1, 1, 1], [0, 1, 1]]`, with characteristic polynomial `(λ − 1)(λ² − 2λ − 1)` and spectral radius `1 + √2`. They number `P⋆_w`, the Pell numbers, and the Pell castles among them `P⋆_w − 2^{w−1}`, so both are silver by width ([[pell-castle-strip](pages/pell-castle-strip.md)]).
- The tree skylines of height at most 2 have the transfer matrix `[[1, 1], [1, 0]]` on the heights `{1, 2}`, with spectral radius `φ`. The Fibonacci castles, the tree castles of height 2, number `F_{w+2} − 1` and are golden by width ([[castle-graph](pages/castle-graph.md)]).

[[castle-classification-growth](pages/castle-classification-growth.md)] classifies castle families by such growth constants. The metallic means are not eigenvalues of the count's own transfer matrices (section 1).

## 3. The adjacency spectra of castle graphs

The castle graph of a castle has its cells as vertices and an edge between cells that share a side ([[castle-graph](pages/castle-graph.md)]). It is connected, so its largest adjacency eigenvalue is its spectral radius. A castle is **golden by spectrum** when the spectral radius of its castle graph is `φ`, and **silver by spectrum** when it is `1 + √2` ([[castle-classification-spectrum](pages/castle-classification-spectrum.md)]). The radius `φ² = (3 + √5)/2` is not a member of de Spinadel's family and has no name here.

```python
import numpy as np
from itertools import product

def castle_graph_radius(c):
    """Largest adjacency eigenvalue of the castle graph of the skyline c."""
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

The exact characteristic polynomials confirm the floating-point matches:[^3]

```
(1,1,1,1)          (x**2 - x - 1)*(x**2 + x - 1)                                        # P_4: spectrum ±phi, ±1/phi
(2,2,2)            (x - 1)*(x + 1)*(x**2 - 2*x - 1)*(x**2 + 2*x - 1)                    # P_2 x P_3
(1,2,3,1,2,3)      x**2*(x - 1)*(x + 1)*(x**2 - 2*x - 1)*(x**2 + 2*x - 1)*(x**4 - 6*x**2 + 6)
(2,1,6,2,1,3)      x*(x - 1)*(x + 1)*(x**2 - 3)*(x**2 - 2)*(x**2 - 2*x - 1)*(x**2 - x - 1)*(x**2 + x - 1)*(x**2 + 2*x - 1)
(1,1,2,4,1,3,1)    x*(x - 1)*(x + 1)*(x**2 - 2)*(x**2 - 2*x - 1)*(x**2 + 2*x - 1)*(x**4 - 4*x**2 + 2)
(4,4)              (x**2 - 3*x + 1)*(x**2 - x - 1)*(x**2 + x - 1)*(x**2 + 3*x + 1)     # P_2 x P_4
(1,3,2,3,1)        (x - 1)*(x + 1)*(x**2 - 3*x + 1)*(x**2 - x - 1)*(x**2 + x - 1)*(x**2 + 3*x + 1)
```

**The products.** The path `P_n` has eigenvalues `2cos(jπ/(n+1))`, and the eigenvalues of a Cartesian product of graphs are the sums of the eigenvalues of the factors. `P_4` has spectral radius `2cos(π/5) = φ`, so the six 4-cell castles whose graph is a path, `(4)`, `(1,3)`, `(3,1)`, `(1,1,2)`, `(2,1,1)` and `(1,1,1,1)`, are golden by spectrum. No other castle is ([[castle-classification-spectrum](pages/castle-classification-spectrum.md)], the section *Castles golden and silver by spectrum*, by Smith's theorem). `P_2 × P_3` has spectral radius `2cos(π/3) + 2cos(π/4) = 1 + √2`, so the `3 × 2` rectangle, `(3,3)` and `(2,2,2)`, is silver by spectrum, and `P_2 × P_4` has spectral radius `1 + φ = φ²`. The three non-rectangular silver castles of the first census, up to mirror image:

```
(1,2,3,1,2,3)      (2,1,6,2,1,3)      (1,1,2,4,1,3,1)
..#..#             ..#...             ...#...
.##.##             ..#...             ...#...
######             ..#...             ...#.#.
                   ..#...             ..##.#.
                   #.##.#             #######
                   ######
```

They are not products, and `x² − 2x − 1` divides their characteristic polynomials; `(2,1,6,2,1,3)` has both `φ` and `1 + √2` in its spectrum.

**The bound and the large scan.** A castle graph is a connected subgraph of the square grid, so every cell has at most 4 neighbors. A connected graph that is not regular has largest eigenvalue below its maximum degree (Brouwer and Haemers, Proposition 3.1.2), and the only regular castle graphs are the single cell, `P_2` and the 4-cycle `(2, 2)`, with spectral radius 0, 1 and 2 ([[castle-classification-spectrum](pages/castle-classification-spectrum.md)]). So every castle graph has spectral radius below 4.[^5] `δ_4 = 2 + √5 = 4.236` and every larger `δ_a` are therefore never the spectral radius of a castle graph. Bronze, `(3 + √13)/2 = 3.303`, is below the bound. The spectral radius of every castle with `w ≤ 8` and `h ≤ 7`, with `w = 9` and `h ≤ 5`, and with `w = 10` and `h ≤ 4`, 4,868,525 castles up to mirror image, gives:[^3]

```
golden by spectrum   4 castles up to mirror image (the six P_4 castles)
silver by spectrum  36 castles up to mirror image, 6 to 20 cells:
  (2,2,2) (3,3) (1,2,3,1,2,3) (1,1,2,1,4,2,1,1) (1,1,2,4,1,3,1) (1,2,3,1,1,3,2,1)
  (1,1,1,1,2,6,1,2) (1,1,1,6,2,1,1,2) (1,1,1,6,2,1,3) (2,1,1,2,6,1,2) (2,1,6,2,1,3)
  (1,2,1,1,1,5,2,1,2) (1,2,3,1,2,1,3,2,1) (3,2,1,2,2,1,2,3) (1,1,3,1,2,3,1,1,2,2)
  (1,3,2,1,3,1,2,3,1) (1,1,1,3,2,1,3,1,2,3) (1,2,1,3,2,1,3,1,1,3) (1,2,1,3,2,1,3,1,4)
  (1,2,2,1,2,1,3,2,1,3) (1,2,3,1,1,2,2,1,2,3) (1,2,6,1,1,5,2) (1,2,6,1,2,1,3,2)
  (2,1,1,2,3,1,1,5,2) (2,1,1,2,3,1,2,1,3,2) (2,1,2,2,1,1,3,2,1,3) (2,1,3,2,1,3,1,2,3)
  (2,2,1,1,3,2,1,1,2,3) (2,3,1,2,1,3,2,1,3) (2,5,1,1,3,2,1,3) (1,5,1,1,1,2,5,1,2)
  (1,6,2,1,3,1,3,2) (2,1,3,2,1,2,1,5,2) (2,1,4,2,1,1,1,5,2) (2,1,4,2,1,1,2,1,3,2)
  (1,2,4,1,3,1,2,6)
spectral radius phi^2   11 castles up to mirror image, 8 to 24 cells:
  (2,2,2,2) (4,4) (1,3,2,3,1) (1,1,2,2,4,1,2,4,1) (1,1,3,5,1,2,4,1) (2,4,2,1,2,1,2,4,2)
  (1,3,4,1,1,3,2,7) (2,4,2,1,2,3,1,2,2,4) (2,4,2,1,2,3,1,3,5) (2,1,3,4,1,2,3,1,4,3)
  (5,3,1,2,2,2,1,3,5)
bronze               0
2 psi^2 within 1e-8  1: (1,1,2,7,7,5,7,7)
```

Every silver and `φ²` match is exact: `x² − 2x − 1` (respectively `x² − 3x + 1`) divides the characteristic polynomial, and no other factor has a larger root. The castle `(3,2,1,2,2,1,2,3)` is the 16-cell castle of [[sandcastle-seminar](pages/sandcastle-seminar.md)].

The one castle near `2ψ² = 3.510`:

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

Its characteristic polynomial is `x(x−1)(x+1)` times an irreducible polynomial of degree 34 and is not divisible by `x³ − 4x² + 4x − 8`, the cubic with root `2ψ²`, so its spectral radius is not `2ψ²`.[^3] [[bronze-castle-hunt](pages/bronze-castle-hunt.md)] searches twelve boxes of about `7.1 × 10¹¹` skylines in all, counting overlaps, and finds no castle whose spectral radius is bronze; it proves that no rectangle has bronze as an eigenvalue and that no two-group even split gives bronze.

## Appearances in Sources

- [[project-euler-502-castle-factoring](pages/project-euler-502-castle-factoring.md)] - the formula for `A^e(w, h)` whose term `h^w` sets the growth constant.
- [[oeis-mining-pe502](pages/oeis-mining-pe502.md)] - the characteristic polynomials `char_1` to `char_5`.
- [[project-euler-502-solution](pages/project-euler-502-solution.md)] - the signed tower count `P(k, L)` and its recurrence in `L`.

## Related Concepts

- [[castle-classification-spectrum](pages/castle-classification-spectrum.md)] - the spectral types of castles, with the proof by Smith's theorem that the six `P_4` castles are the only castles golden by spectrum.
- [[spectral-analysis](pages/spectral-analysis.md)] - the spectra on a castle: transfer matrices, the skyline DFT, the Laplacian and the adjacency matrix with its universal cover.
- [[castle-graph](pages/castle-graph.md)] - the castle graph, with its cycle rank and the tree castles.
- [[castle-eigenvalues-by-example](pages/castle-eigenvalues-by-example.md)] - the adjacency matrices, characteristic polynomials and walk counts of small castles worked by hand, including castles golden and silver by spectrum.
- [[bronze-castle-hunt](pages/bronze-castle-hunt.md)] - the bronze search, with the proofs for rectangles and two-group even splits.
- [[isospectral-castles](pages/isospectral-castles.md)] - non-isomorphic castles with equal spectra; no two of the 36 silver castles have the same spectrum.
- [[metallic-means](pages/metallic-means.md)] - de Spinadel's family and its named members.
- [[pell-castle-strip](pages/pell-castle-strip.md)] - the anchored 1-smooth strips on `{1, 2, 3}`, whose transfer matrix has spectral radius `1 + √2`.
- [[tower-parity-sectors](pages/tower-parity-sectors.md)] - the signed transfer matrix `M̃_k`, the factors `H_d` and `V_d` of `char_k`, and `P(k, L) = e_0ᵀ M̃_k^L v`.
- [[plastic-number](pages/plastic-number.md)] - `ρ_6 = 2ψ²` and the units `ρ_k/2`.
- [[generating-function-gallery](pages/generating-function-gallery.md)] - the values `ρ_k` and the row-sum bound `ρ_k ≤ k + 1`.
- [[hyperbolic-sequence-family](pages/hyperbolic-sequence-family.md)] - `A^e(w, 2) = A038505(w+1)`, which grows at 2.
- [[castle-snippets](pages/castle-snippets.md)] - `castle_graph_radius` and an exact test for a metallic mean in the spectrum.
- [[sandcastle-seminar](pages/sandcastle-seminar.md)] - the seminar on the silver castle `(3,2,1,2,2,1,2,3)`, its sandpile group, clock, identity and avalanches.

## Footnotes

[^1]: [[project-euler-502-castle-factoring](pages/project-euler-502-castle-factoring.md)] §"The sign of a castle" L123-127 - "F(w,h) = (h^w - (h-1)^w - P(h-1,w) + P(h-2,w))/2".
[^2]: [[oeis-mining-pe502](pages/oeis-mining-pe502.md)] `mine-notes.md` §"Vein 1" L31-37 - the characteristic polynomials of `P(k, ·)` for `k ≤ 5`, "constant term = (-1)^{k-1} 2^k".
[^3]: Verified by execution (Python 3.11 with NumPy, SymPy and networkx, 2026-10-16): `A^e(w, 2)` for `w ≤ 14` by enumeration; `char(M̃_k) = char_k` for `k ≤ 7`; `g_k` integral with leading coefficient 2 and constant term `±1` for `k ≤ 30`; `ρ_k` for `k ≤ 30`, the degrees 8 and 18 of `ρ_3` and `ρ_5` from the resultant of `char_k(y)` and `y^{k+1} char_k(t/y)`, and the leading coefficient of the factor of `g_k` containing `ρ_k/2` for `k ≤ 30`; the first census (134,111 castles, tolerance `10⁻⁹`) and the seven factorizations; the large scan of all 4,868,525 castles up to mirror image in the stated boxes with `eigvalsh` (tolerance `10⁻⁸`), each silver and `φ²` match confirmed by exact division of the characteristic polynomial; the polynomial of `(1,1,2,7,7,5,7,7)`, whose degree-34 factor has dominant root `3.5097553244763626829414848…`, `8.0·10⁻⁹` below `2ψ²`.
[^4]: Verified by execution: no eigenvalue of `M̃_k` for `k ≤ 20` lies within `10⁻⁶` of `δ_a` for `a ≤ 6`, as the Proposition requires.
[^5]: https://aeb.win.tue.nl/2WF02/spectra.pdf (A. E. Brouwer and W. H. Haemers, *Spectra of Graphs*, monograph version of February 1, 2011, read 2026-10-16) - Theorem 2.2.1(vi), p.22: "If |S| ≤ T and S has eigenvalue σ, then |σ| ≤ θ0. If equality holds, then |S| = T, and there are a diagonal matrix E with diagonal entries of absolute value 1 and a constant c of absolute value 1, such that S = cETE^{−1}"; Proposition 3.1.2, p.33: "Let Γ be a connected graph with largest eigenvalue θ1. If Γ is regular of valency k, then θ1 = k. Otherwise, we have kmin < k̄ < θ1 < kmax where kmin, kmax and k̄ are the minimum, maximum and average degree."
