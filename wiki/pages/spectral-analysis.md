---
title: Spectral analysis of castles
category: Concepts
summary: The centerpiece hub for spectral methods applied to castles as 2D polyominoes. Five different spectra sit on a castle, each classifying different things — transfer-matrix (growth), LGV kernel (correlation universality), skyline DFT (individual signature), combinatorial Laplacian (connectivity / isospectral pairs), Ihara zeta (Ramanujan / expander). Toolkit-side companion to [[castle-classification]] Axis 9's spectral predicates.
tags: [concept, castle, spectral, transfer-matrix, laplacian, dft, ihara-zeta, ramanujan, isospectral, determinantal]
sources: [spectral-analysis]
created: 2026-09-16
updated: 2026-09-19
---

# Spectral analysis of castles

## Why spectral

**Spectral** is a promiscuous word — at least five distinct spectra sit naturally on a castle, and each classifies something different. Growth rates. Correlation structure. Individual shape. Connectivity. Arithmetic-graph optimality. This page is the toolkit-side hub for all of them: what each operator is, what its spectrum computes, what it classifies, and how each method connects to the structural, growth-type, and spectral predicates on [[castle-classification](pages/castle-classification.md)].

The pairing with classification is deliberate. Where [[castle-classification](pages/castle-classification.md)] catalogs **predicates** (which castle is Ramanujan? which class is silver width growth?), this page catalogs **methods** for computing the spectra those predicates test. A completed spectral method + a satisfied predicate = a named castle type. The two pages evolve together; every method here is a lens; every lens sometimes reveals a type there.

The five methods, at a glance:

| # | Spectrum | Operator | Object graded | Classifies | Effort |
|---|---|---|---|---|---|
| 1 | Transfer-matrix eigenvalues `λ_i(h)` | Signed transfer matrix `T` on skyline states | Family / class of castle rules | Asymptotic growth type ([[metallic-means](pages/metallic-means.md)], Axis 8) | Days |
| 2 | LGV kernel eigenvalues | Non-crossing-path kernel `N(w; i, j)` | Random castle ensemble | Correlation universality class (determinantal / sine-kernel) | Weeks |
| 3 | Skyline DFT `ĉ_k` | Discrete Fourier operator on the height sequence | Individual castle | Shape by frequency profile (sparse-spectrum, crenellated → two-atom) | Days |
| 4 | Combinatorial Laplacian `μ_i` | `L = D − A` on the castle polyomino graph | Individual castle | Connectivity, bottleneck, **isospectral pairs** | Weeks |
| 5 | Ihara zeta / adjacency spectrum | Non-backtracking / edge-adjacency operator | Individual castle | Expander / **Ramanujan castle** property | Months |

## 1. Transfer-matrix spectrum — the growth engine

The **signed transfer matrix** `T` acts on skyline states (previous column height) and encodes the [[castle-sign](pages/castle-sign.md)] `s(C) = (−1)^blocks` through its off-diagonal weights. It is the operator implicit in the `p_signed` DP of [[project-euler-502-brute-force](pages/project-euler-502-brute-force.md)] — state a length-`(k+1)` vector indexed by the last column height, transition `(−1)^max(0, b−a)` from height `a` to `b` — and the operator whose rational-function shadow is the `num_k / den_k` recurrence of [[castle-counting-formula](pages/castle-counting-formula.md)].

For fixed height bound `k = h − 1`, `T = M_k` is an `h × h` integer matrix whose signed row sums produce `P(k, L)`. The count itself is dominated by the unsigned term:

```
F(w, h)  =  [h^w − (h−1)^w − P(h−1, w) + P(h−2, w)] / 2   ~   h^w / 2,        λ_1(h) = h,
```

so the growth constant of `F(·, h)` is the integer `h` for every `h`, and the spectrum of `M_k` governs the *correction* terms `P(k, w) ~ ρ_k^w` with `ρ_1 = √2`, `ρ_2 = 2`, `ρ_3 = 2.193`, `ρ_4 = 2.796`, `ρ_5 = 2.892`, `ρ_6 = 2ψ² = 3.510` (`ψ` the [[plastic-number](pages/plastic-number.md)]). None of these is a metallic mean, and none can be: every eigenvalue of `M_k` is twice a root of the monic factor `H_{k/2}` or a root of the leading-coefficient-2 factor `V_{k/2}` ([[tower-parity-sectors](pages/tower-parity-sectors.md)]), and a metallic mean fails both tests ([[castle-graph-spectral-radius](pages/castle-graph-spectral-radius.md)]). Metallic means enter the castle as spectral radii of the 2-state transfer matrices of castle *classes* - the [[pell-castle-strip](pages/pell-castle-strip.md)] `[[2,1],[1,0]]` with `1 + √2`, the `{0,1}`-strip with `φ` - which is what Axis 8 of [[castle-classification](pages/castle-classification.md)] records, and as adjacency spectral radii of individual castle graphs (method 4 below).

**Spectral signature of a rule set.** Any modification of PE 502's rules (change the gap requirement, forbid width-1 blocks, allow diagonal stacking) modifies `T` and therefore perturbs the sequence `{λ_i(h)}_{h ≥ 2}`. Two castle families are asymptotically equivalent iff their transfer-matrix eigenvalue sequences agree — the transfer-matrix spectrum is the **canonical invariant** of a castle rule set.

**Spectral gap → variance.** The gap `λ_1 − |λ_2|` controls the *variance* of block counts, peak counts, and area over the ensemble of random `w × h` castles. Wide gap → tight concentration around the mean (fluctuations are `O(1)`); narrow gap → heavy column-to-column correlations and CLT-scale fluctuations `O(√w)`. This is the classical Perron-Frobenius spectral-gap story specialized to the castle transfer matrix.

**Connection to [[eigenvalue-continued-fractions](pages/eigenvalue-continued-fractions.md)].** That page treats the **characteristic polynomials of the L-direction and k-direction recurrences** on `P(k, L)` — palindromic / anti-palindromic, self-reciprocal, roots pairing as `r ↔ ±1/r`. Those recurrences are *derived* from the transfer matrix via the rational-function form `P_k = num_k / den_k`, so the eigenvalues in play are related but distinct: the transfer-matrix spectrum lives at the operator level; the recurrence spectra live at the sequence level. Same underlying algebra, different objects.

**Wiki ties:** [[castle-counting-formula](pages/castle-counting-formula.md)], [[project-euler-502-brute-force](pages/project-euler-502-brute-force.md)] `p_signed`, [[metallic-means](pages/metallic-means.md)], [[castle-classification](pages/castle-classification.md)] Axis 8 (growth-type meta-classification).

## 2. LGV kernel spectrum — determinantal correlation universality

The **Lindström-Gessel-Viennot (LGV) kernel** `N(w; i, j)` counts non-crossing lattice paths between fixed endpoints via a determinant of a single-path matrix. For castle sub-families expressible as non-crossing path ensembles — parallelogram polyominoes, staircase polyominoes, and the LGV/nomography framing (a working note pending ingest into the wiki) — the count is `det N`, and `N` is the kernel of a **determinantal point process** whose eigenvalues lie in `[0, 1]` and admit an interpretation as probabilities that particular row-configurations appear.

The determinantal-process framing is what makes castles amenable to **random matrix universality** analysis. Two classification questions attach:

- **Is the castle ensemble a genuine determinantal process?** Equivalently: is `N` a projection kernel (all eigenvalues 0 or 1)? If yes, castles inherit the entire toolkit of DPP theory: correlation functions as minors, gap probabilities as Fredholm determinants, exact enumerative bounds. If no, the process has an eigenvalue-weighted mixture structure and the analysis is harder.
- **What is the bulk limit?** The prediction from adjacent literature (random Young tableaux, Aztec diamonds, GUE) is a **sine kernel** at the bulk in the large-`w, h` limit, giving peak-position spacing statistics `sin(π(x − y))/(π(x − y))`. If the prediction holds, castles are in the same universality class as the classical determinantal ensembles.

**The nomography link.** The LGV framework applies to castles through a non-crossing-path bijection that the working note `pe502-nomography.md` (in `/Users/creid/tmp/`, pending wiki ingest) develops. Once ingested that thread will become the fully-linked home of the LGV/determinantal analysis; this section will grow when it lands.

**Wiki ties (pending):** the yet-to-be-ingested nomography note; downstream connections to [[column-convex-polygon-enumeration](pages/column-convex-polygon-enumeration.md)] (parallelogram polyominoes are the canonical LGV castle family), [[polyominoes](pages/polyominoes.md)] (Ferrers / staircase families as non-crossing-path ensembles), and [[castle-classification](pages/castle-classification.md)] Axis 3 (path-like types) as a supply of concrete LGV-amenable castle classes.

## 3. Skyline DFT — individual-castle signatures

Every individual castle has a column-height sequence `c_1, c_2, …, c_w`, and its **discrete Fourier transform**

```
ĉ_k  =  ∑_{j=1}^{w}  c_j · e^{−2πi jk/w},      k = 0, 1, …, w − 1
```

is a complete invariant of the skyline (modulo cyclic shift, which the DFT commutes with). This turns each individual castle into a point in `C^w` and lets **shape classification become frequency-profile classification**.

Three natural regimes:

- **Low-pass castles** — energy concentrated in low-`k` modes. Smooth, mountain-shaped skylines with few tall peaks. The [[convex-castle](pages/convex-castle.md)] class and the [[stack-polyomino-gf](pages/stack-polyomino-gf.md)] unimodal family sit predominantly here.
- **High-pass castles** — energy concentrated in high-`k` modes. Jagged, alternating skylines with many blocks and gaps. The **crenellated** type ([[castle-classification](pages/castle-classification.md)] Axis 7) with heights alternating `{a, h}` is the extreme case — its DFT support is concentrated at `k = w/2`, a **two-atom spectrum**.
- **Sparse-spectrum castles** — a specific set `S ⊂ {0, …, w−1}` of frequencies carries all the energy (`ĉ_k = 0` for `k ∉ S`). Highly periodic skylines. **Crenellated / battlement** = two-atom `S = {0, w/2}`; more general periodic patterns give richer `S`. The classification question — *which sparse-support sequences correspond to valid castles?* — is a hard combinatorial problem that hooks into **compressed sensing** and **turnpike-type reconstruction** from the signal-processing side.

**Skyline energy as an ordering.** The Parseval identity `∑ |ĉ_k|² = w · ∑ c_j²` fixes total energy at the area-squared scale (area = `∑ c_j`), so the DFT gives an orthogonal decomposition of a castle's "total energy" across `w` frequency channels. Ordering castles by *which* channels carry the energy gives a continuous refinement of the discrete Axis 7 value-pattern types.

**Wiki ties:** [[castle-classification](pages/castle-classification.md)] Axis 7 (crenellated = two-atom DFT support) and Axis 9 (sparse-spectrum as an individual-castle predicate; low/high-pass as soft variants); [[castle-representations](pages/castle-representations.md)] (the column-height sequence being transformed); [[castle-snippets](pages/castle-snippets.md)] (a `numpy.fft.fft(c)` one-liner is the natural extension there — not yet added).

## 4. Combinatorial Laplacian — connectivity, bottlenecks, isospectral pairs

Treat the filled cells of a castle as the vertices of a graph; add an edge between every pair of orthogonally adjacent filled cells. This gives the **castle's polyomino graph** `G_C`. Its **combinatorial Laplacian** is

```
L(G_C)  =  D − A,        eigenvalues  0 = μ_0 ≤ μ_1 ≤ … ≤ μ_{n−1}
```

with `D` the diagonal degree matrix and `A` the adjacency matrix. The Laplacian spectrum encodes the castle's connectivity structure with well-known handles:

- **Algebraic connectivity `μ_1` (Fiedler value)** — measures how "bottlenecked" the castle is. A pyramidal castle (broad base) has larger `μ_1` than a T-shape or a castle with a narrow neck between two bulges. Fiedler eigenvector localizes on the bottleneck.
- **Cheeger inequality** — `h(G_C) ≥ μ_1 / 2`, where the Cheeger constant `h(G_C)` is the minimum boundary-to-volume ratio over vertex subsets. Detects **necks and bridges** in the castle geometrically.
- **Heat-kernel trace** — `Tr(e^{−tL}) = ∑_i e^{−t μ_i}`. Encodes the entire Laplacian spectrum in a single time-parameter function, and captures the polyomino up to isospectral isomorphism.

### Isospectral castles — "hear the shape of a castle"

Two castles with the **same Laplacian spectrum but non-isomorphic shape** are **isospectral**. This is Kac's classical "hear the shape of a drum" question specialized to the castle setting: given the spectrum of `L(G_C)`, can we recover `C` up to isomorphism? For polyominoes generally the answer is **no** — Sunada-type constructions produce isospectral non-isomorphic pairs — and it is essentially certain that isospectral castle pairs exist. The seminar target is finding the **smallest**.

**Sketched approach.** Enumerate all castles up to size `n ≤ 20` (or up to `w, h ≤ 6` or so) using the [[castle-snippets](pages/castle-snippets.md)] enumeration primitives. For each castle: (i) build the polyomino graph as a `NetworkX` graph or a sparse adjacency matrix; (ii) compute `L`; (iii) compute the sorted spectrum as a tuple of rounded floats (or symbolic characteristic polynomial for exactness); (iv) hash. Search for collisions across non-isomorphic castles. Report the smallest pair. Both computational and clean-statement outcomes — either an explicit pair is exhibited (and drawn), or an exhaustive search up to size `n_0` shows no pair exists up to `n_0`.

**Wiki ties:** [[castle-classification](pages/castle-classification.md)] Axis 9 (isospectral pair as an Axis-9 predicate; the pair predicate rather than a single-castle predicate); [[castle-snippets](pages/castle-snippets.md)] (enumeration primitives feeding the search).

## 5. Ihara zeta / Ramanujan castles — arithmetic-flavored spectral invariant

For the castle polyomino graph `G_C`, the **Ihara zeta function** is

```
ζ_{G_C}(u)  =  ∏_{[γ]}  (1 − u^{|γ|})^{−1}
```

where the product runs over equivalence classes of prime, backtrackless, tailless closed walks. `ζ_{G_C}(u)` is a rational function, and its poles are the eigenvalues of a modified **non-backtracking / edge-adjacency operator** on the graph. This is the graph-theoretic analog of the **Selberg zeta function** on hyperbolic surfaces — spectral information about the graph packaged as an arithmetic-flavored generating function over closed walks.

### Ramanujan castles

A castle `C` is a **Ramanujan castle** iff the non-trivial adjacency eigenvalues `λ` of `G_C` satisfy the **Alon-Boppana bound**

```
|λ|  ≤  2 · √(d − 1)
```

where `d` is the maximum vertex degree. The bound is the asymptotic optimum for the spectral gap of infinite regular graph families — the defining condition of Ramanujan graphs (Lubotzky-Phillips-Sarnak; Margulis) — and picks out the "spectrally most expander-like" castles at given size. Ramanujan castles are the combinatorial extremes of the castle family in the same sense that Ramanujan graphs are the extremes of the regular-graph family.

Castle graphs are **not regular** in general — interior cells have degree 4, edge cells degree 3, corner cells degree 2 — so the strict definition invokes the max-degree form of the bound. Natural refinements the wiki will want to develop:

- **Bipartite-Ramanujan castles.** Every castle graph is bipartite (color cells by `(i + j) mod 2`), so the Marcus-Spielman-Srivastava existence theory of bipartite Ramanujan graphs applies directly. Bipartite spectra are symmetric around 0, so the condition becomes `|λ| ≤ 2√(d−1)` on the *non-trivial* eigenvalues of the bipartite adjacency operator.
- **Ihara-Ramanujan castles.** Transfer the condition to the non-backtracking operator's spectrum rather than adjacency. This is the version that connects most directly to the Ihara-zeta framework and lifts cleanly to irregular graphs.

**Structural candidates worth checking first** ([[castle-classification](pages/castle-classification.md)] Axis 5 and 7 types with regular local structure):

- **Boxcastle** — the full `w × h` rectangle graph. Its adjacency spectrum is known explicitly: `2·cos(iπ/(w+1)) + 2·cos(jπ/(h+1))` for `1 ≤ i ≤ w, 1 ≤ j ≤ h`. Ramanujan status reduces to bounding these values against `2√(d−1) = 2√3`.
- **Hook** — small, spectrum computable by hand or trivially by SymPy.
- **Ferrers / staircase** — the standard partition-shape polyominoes with partial classical spectral results in the polyomino literature.
- **Crenellated** — alternating heights `{a, h}`; highly regular local structure, a natural Ramanujan candidate.

**Wiki tie:** [[castle-classification](pages/castle-classification.md)] Axis 9's first named type is the Ramanujan castle; this section supplies the *method* (Ihara zeta, adjacency-operator spectral analysis) whose output the Axis-9 predicate tests.

## Construction ↔ spectrum crosswalk

The five spectra above are not independent of the structural axes. Concrete construction rules force concrete spectral consequences — each row here is a **theorem-shaped claim** (some proved, some open) connecting an Axes 1-8 type to its forced spectral fingerprint:

| Structural rule / type | Forced spectral consequence |
|---|---|
| **Crenellated** (Axis 7, `c_i ∈ {a, h}` alternating) | Skyline DFT support at `k = w/2` (two-atom); high-pass spectrum |
| **Boxcastle** (Axis 5, `c_i = h` all) | Laplacian spectrum `2·cos(iπ/(w+1)) + 2·cos(jπ/(h+1))`, explicit closed form |
| **Unimodal / pyramidal** (Axis 1) | Skyline DFT decays like `1/k` (sawtooth-DFT class); low-pass spectrum; Laplacian spectral gap `μ_1 = Θ(1/w)` |
| **Even-parity-only** (PE 502 rule 6) | Transfer-matrix `T` splits into `±1` eigenspaces of the block-parity involution `σ`; castles live in the `+1` half; spectral projection = `½(I + σ)`. This is [[castle-sign](pages/castle-sign.md)]'s `(T ± P)/2` at the operator level. |
| **Silver width growth castle** (Axis 8) | The *class's* transfer matrix (the 1-smooth height-3 matrix `[[1,1,0],[1,1,1],[0,1,1]]` for the Pell strip) has spectral radius `1 + √2 ∈ Q(√2)`; PE 502's own signed transfer matrix never has a metallic eigenvalue |
| **Golden- / silver-spectrum castle** (Axis 9) | Adjacency spectral radius `φ` (the 4-cell paths) or `1 + √2` (the `3×2` rectangle and three non-rectangular castles) - see [[castle-graph-spectral-radius](pages/castle-graph-spectral-radius.md)] |
| **q-Gibbs area-weighted** (`q = e^{−β}`, area-weighted measure) | Transfer matrix `T_β` with `β`-dependent spectrum; **spectral phase transition** at some critical `β_c` where `λ_1(β)` has a non-analyticity — the castle analog of a Yang-Lee zero and the direct meeting-point of combinatorics with statistical mechanics |

The last row is the sharpest open target — a critical-`β` computation for castles graded by area would connect the [[castle-by-area](pages/castle-by-area.md)] thread, the [[q-catalan-numbers](pages/q-catalan-numbers.md)] q-analog thread, and the transfer-matrix spectral analysis in a single result. Statistical-physics adjacency comes for free.

## Two immediate targets (sketched, not run)

### `λ_1(h)` - settled

The transfer matrix `M_k` (`k = h − 1`) has characteristic polynomial `char_k` of degree `h` ([[generating-function-gallery](pages/generating-function-gallery.md)]), factored in closed form on [[tower-parity-sectors](pages/tower-parity-sectors.md)]: `char_k(2μ)/2^k = H_{k/2}(μ)·(H_{k/2+1}(μ) + μ² H_{k/2−1}(μ))` for even `k`, irreducible for odd `k`. The count's growth constant is `λ_1(h) = h`; the signed correction grows like `ρ_{h−1}` with `ρ_1 = √2`, `ρ_2 = 2`, `ρ_3 = 2.193`, `ρ_4 = 2.796`, `ρ_5 = 2.892`, `ρ_6 = 2ψ²` - algebraic, never metallic, and `2 ×` a unit exactly when `h ≡ 3 (mod 4)`. The metallic-mean ladder does not appear in PE 502's own spectrum; it appears in class transfer matrices (Axis 8) and in individual castle graphs (below). Full table and argument on [[castle-graph-spectral-radius](pages/castle-graph-spectral-radius.md)].

### The isospectral-castle hunt - settled

Run exhaustively over every castle with at most 16 cells (compositions of `n`, mirror-deduped, exact integer characteristic polynomials, isomorphism by networkx) on [[isospectral-castles](pages/isospectral-castles.md)]. The smallest non-isomorphic castles with the same **adjacency** spectrum have **10 cells** (`(1,1,1,2,3,2)` vs `(1,1,2,2,3,1)`, two groups at that size); with the same **Laplacian** spectrum, **11 cells** (`(1,1,1,2,1,1,2,1,1)` vs `(1,1,3,1,1,1,2,1)`, both trees); isospectral for both operators, **16 cells**. Groups multiply quickly afterwards (50 adjacency groups at 16 cells), so the spectrum is an invariant, not a classifier.

## Where methods meet predicates

This page and [[castle-classification](pages/castle-classification.md)] are paired. The rough division of labor:

- **This page** — **methods**: how to compute each of the five spectra. What operator, what algorithm, what does the output mean.
- **[[castle-classification](pages/castle-classification.md)]** — **predicates**: which castle satisfies which spectral condition. Axis 9's Ramanujan / isospectral / sparse-spectrum are the current named types; more will land as the methods develop.

**A completed spectral method + a satisfied predicate = a named castle type.** The Ramanujan castle is the simplest live example: the method (Ihara / adjacency-spectrum computation) exists in general graph theory; the predicate (`|λ| ≤ 2√(d−1)`) sits on Axis 9; the type is named. Every other spectral method on this page has a parallel Axis-9 type it would populate when its computational side is fleshed out — sparse-spectrum from the DFT method, isospectral from the Laplacian method, sine-kernel bulk-limit membership from the LGV kernel method, silver-width-growth membership from the transfer-matrix method (already Axis 8).

## Open threads

- **`λ_1(h)`** - settled: `λ_1(h) = h`, signed corrections `ρ_{h−1}`, no metallic means ([[castle-graph-spectral-radius](pages/castle-graph-spectral-radius.md)], [[tower-parity-sectors](pages/tower-parity-sectors.md)]).
- **Golden- and silver-spectrum castles** - the first Axis 9 census: adjacency spectral radius `φ` for the six 4-cell paths, `1 + √2` for the `3×2` rectangle and three non-rectangular castles up to `w = 7`; copper and above impossible (max degree 4), bronze open ([[castle-graph-spectral-radius](pages/castle-graph-spectral-radius.md)]).
- **Isospectral hunt** - settled: smallest pairs at 10 cells (adjacency), 11 (Laplacian), 16 (both), on [[isospectral-castles](pages/isospectral-castles.md)].
- **Nomography ingest** — the working note in `/Users/creid/tmp/pe502-nomography.md` develops the LGV / non-crossing-path framing for castles; ingesting it will populate §2 above with concrete kernel formulas and cross-links.
- **q-Gibbs critical-`β`** — the transfer-matrix phase-transition computation from the construction ↔ spectrum table's last row. Statistical-mechanics-adjacent.
- **Ihara-zeta computations** for small castles — closed-form `ζ_{G_C}(u)` for boxcastles, hooks, staircases.
- **Sparse-spectrum classification** — which sparse DFT-supports correspond to valid castles? Compressed-sensing / turnpike-reconstruction hooks.

Each of these becomes its own Analysis page or Concept page when its content lands.

## Related Concepts

- [[castle-classification](pages/castle-classification.md)] — the predicate-side companion; Axis 9 catalogs spectral types on individual castles, Axis 8 catalogs growth-type meta-classification on classes.
- [[castle-polyomino](pages/castle-polyomino.md)] / [[castle-representations](pages/castle-representations.md)] — the base object each spectral method acts on.
- [[metallic-means](pages/metallic-means.md)] — the family the transfer-matrix `λ_1(h)` values populate.
- [[eigenvalue-continued-fractions](pages/eigenvalue-continued-fractions.md)] — sibling eigenvalue thread on the `P(k, L)` recurrences (sequence-level rather than operator-level); the self-reciprocal / Lagrange-periodicity theory the transfer-matrix spectrum specializes.
- [[project-euler-502-brute-force](pages/project-euler-502-brute-force.md)] — the `p_signed` DP is the transfer matrix in one concrete form.
- [[castle-counting-formula](pages/castle-counting-formula.md)] — the `num_k / den_k` recurrence is the transfer matrix's rational-function shadow.
- [[castle-snippets](pages/castle-snippets.md)] — enumeration primitives feeding the isospectral hunt and future spectral-method snippets.
- [[castle-by-area](pages/castle-by-area.md)] / [[q-catalan-numbers](pages/q-catalan-numbers.md)] — the area / q-analog threads the q-Gibbs critical-`β` row of the crosswalk connects.
- [[castle-sign](pages/castle-sign.md)] — the block-parity involution `σ` whose `±1` eigenspaces are the operator-level form of `(T ± P)/2`.
- [[pell-castle-strip](pages/pell-castle-strip.md)] / [[stack-polyomino-gf](pages/stack-polyomino-gf.md)] — the two smallest concrete castle families whose spectral properties are cleanly computable.
- [[castle-compression](pages/castle-compression.md)] — sparse-spectrum castles are compressible in the transform domain; the compressed-sensing hook in the open threads is the DFT face of the compressibility axis.
