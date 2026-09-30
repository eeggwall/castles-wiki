---
title: Spectral analysis of castles
category: Concepts
summary: The centerpiece hub for spectral methods applied to castles as 2D polyominoes. Five different spectra sit on a castle, each classifying different things — transfer-matrix (growth), LGV kernel (correlation universality), skyline DFT (the skyline's own spectrum - the eigenbasis of the column difference; whole-number skylines have DFT supports that are exactly unions of divisor classes; homometric castles from 11 cells), combinatorial Laplacian (connectivity / isospectral pairs), Ihara zeta (Ramanujan / expander). Toolkit-side companion to the spectral predicates on castle-classification-spectrum.
tags: [concept, castle, spectral, transfer-matrix, laplacian, dft, dct, galois, ramanujan-sum, homometric, ihara-zeta, ramanujan, isospectral, determinantal]
sources: [spectral-analysis]
created: 2026-09-16
updated: 2026-09-29
---

# Spectral analysis of castles

## Why spectral

At least five distinct spectra sit on a castle: growth rates, correlation structure, individual shape, connectivity, and Ramanujan-type graph optimality. This page is the toolkit-side hub for all of them: what each operator is, what its spectrum computes, what it classifies, and how each method connects to the structural, growth-type, and spectral predicates on [[castle-classification](pages/castle-classification.md)].

The pairing with classification is deliberate. Where [[castle-classification](pages/castle-classification.md)] catalogs **predicates** (which castle is Ramanujan? which class is silver width growth?), this page catalogs **methods** for computing the spectra those predicates test.

The five methods, at a glance:

| # | Spectrum | Operator | Object graded | Classifies |
|---|---|---|---|---|
| 1 | Transfer-matrix eigenvalues `λ_i(h)` | Signed transfer matrix `T` on skyline states | Family / class of castle rules | Asymptotic growth type ([[metallic-means](pages/metallic-means.md)], Axis 8) |
| 2 | Lindstrom-Gessel-Viennot (LGV) kernel eigenvalues | Non-crossing-path kernel `N(w; i, j)` | Random castle ensemble | Correlation universality class (determinantal / sine-kernel) |
| 3 | Skyline discrete Fourier transform (DFT) `ĉ_k` | Discrete Fourier operator on the height sequence | Individual castle | Shape by frequency profile (sparse supports = unions of divisor classes; crenellated → two-atom at even width; homometric pairs) |
| 4 | Combinatorial Laplacian `μ_i` | `L = D − A` on the castle polyomino graph | Individual castle | Connectivity, bottleneck, **isospectral pairs** |
| 5 | Ihara zeta / adjacency spectrum | Non-backtracking / edge-adjacency operator | Individual castle | Expander / **Ramanujan castle** property |

## 1. Transfer-matrix spectrum — the growth engine

The **signed transfer matrix** `T` acts on skyline states (previous column height) and encodes the [[castle-sign](pages/castle-sign.md)] `s(C) = (−1)^blocks` through its off-diagonal weights. It is the operator implicit in the `p_signed` dynamic program (DP) of [[project-euler-502-brute-force](pages/project-euler-502-brute-force.md)] — state a length-`(k+1)` vector indexed by the last column height, transition `(−1)^max(0, b−a)` from height `a` to `b` — and the operator whose rational-function shadow is the `num_k / den_k` recurrence of [[castle-counting-formula](pages/castle-counting-formula.md)].

For fixed height bound `k = h − 1`, `T = M_k` is an `h × h` integer matrix whose signed row sums produce `P(k, L)`. The count itself is dominated by the unsigned term:

```
F(w, h)  =  [h^w − (h−1)^w − P(h−1, w) + P(h−2, w)] / 2   ~   h^w / 2,        λ_1(h) = h,
```

so the growth constant of `F(·, h)` is the integer `h` for every `h`, and the spectrum of `M_k` governs the *correction* terms `P(k, w) ~ ρ_k^w` with `ρ_1 = √2`, `ρ_2 = 2`, `ρ_3 = 2.193`, `ρ_4 = 2.796`, `ρ_5 = 2.892`, `ρ_6 = 2ψ² = 3.510` (`ψ` the [[plastic-number](pages/plastic-number.md)]). None of these is a metallic mean, and none can be: every eigenvalue of `M_k` is twice a root of the monic factor `H_{k/2}` or a root of the leading-coefficient-2 factor `V_{k/2}` ([[tower-parity-sectors](pages/tower-parity-sectors.md)]), and a metallic mean fails both tests ([[castle-graph-spectral-radius](pages/castle-graph-spectral-radius.md)]). Metallic means enter the castle as spectral radii of the 2-state transfer matrices of castle *classes* - the [[pell-castle-strip](pages/pell-castle-strip.md)] `[[2,1],[1,0]]` with `1 + √2`, the `{0,1}`-strip with `φ` - which is what Axis 8 of [[castle-classification](pages/castle-classification.md)] records, and as adjacency spectral radii of individual castle graphs (method 4 below).

**Spectral signature of a rule set.** Any modification of Project Euler 502 (PE 502)'s rules (change the gap requirement, forbid width-1 blocks, allow diagonal stacking) modifies `T` and therefore perturbs the sequence `{λ_i(h)}_{h ≥ 2}`.

**Spectral gap → variance.** The gap `λ_1 − |λ_2|` sets the rate at which column-to-column correlations decay. With a gap, additive statistics (block count, peak count, area) of random width-`w` castles have variance linear in `w` and a Central Limit Theorem (CLT); the gap controls the constant, not the order `√w` of the fluctuations.

**Connection to [[eigenvalue-continued-fractions](pages/eigenvalue-continued-fractions.md)].** That page treats the **characteristic polynomials of the L-direction and k-direction recurrences** on `P(k, L)` — palindromic / anti-palindromic, self-reciprocal, roots pairing as `r ↔ ±1/r`. Those recurrences are *derived* from the transfer matrix via the rational-function form `P_k = num_k / den_k`, so the eigenvalues in play are related but distinct: the transfer-matrix spectrum lives at the operator level; the recurrence spectra live at the sequence level. Same underlying algebra, different objects.

**Wiki ties:** [[castle-counting-formula](pages/castle-counting-formula.md)], [[project-euler-502-brute-force](pages/project-euler-502-brute-force.md)] `p_signed`, [[metallic-means](pages/metallic-means.md)], [[castle-classification-growth](pages/castle-classification-growth.md)] Axis 8 (growth-type meta-classification).

## 2. LGV kernel spectrum — determinantal correlation universality

The **Lindström-Gessel-Viennot (LGV) kernel** `N(w; i, j)` counts non-crossing lattice paths between fixed endpoints via a determinant of a single-path matrix. For castle sub-families expressible as non-crossing path ensembles — parallelogram polyominoes and staircase polyominoes — the count is `det N`, and `N` is the kernel of a **determinantal point process** whose eigenvalues lie in `[0, 1]` and admit an interpretation as probabilities that particular row-configurations appear.

The determinantal-process framing is what makes castles amenable to **random matrix universality** analysis. Two classification questions attach:

- **Is the castle ensemble a genuine determinantal process?** Equivalently: is `N` a projection kernel (all eigenvalues 0 or 1)? If yes, castles inherit the entire toolkit of DPP theory: correlation functions as minors, gap probabilities as Fredholm determinants, exact enumerative bounds. If no, the process has an eigenvalue-weighted mixture structure and the analysis is harder.
- **What is the bulk limit?** The prediction from adjacent literature (random Young tableaux, Aztec diamonds, Gaussian Unitary Ensemble (GUE)) is a **sine kernel** at the bulk in the large-`w, h` limit, giving peak-position spacing statistics `sin(π(x − y))/(π(x − y))`. If the prediction holds, castles are in the same universality class as the classical determinantal ensembles.

**Castles themselves.** A castle is a single-path object, so LGV applies to castles only through a bijection to non-crossing path families, and none is known. The exact LGV sampler for parallelogram polyominoes is on [[castle-samplers](pages/castle-samplers.md)] §8.

**Wiki ties:** [[column-convex-polygon-enumeration](pages/column-convex-polygon-enumeration.md)] (parallelogram polyominoes are the canonical LGV castle family), [[polyominoes](pages/polyominoes.md)] (Ferrers / staircase families as non-crossing-path ensembles), and [[castle-classification-shape](pages/castle-classification-shape.md)] Axis 3 (path-like types) as a supply of concrete LGV-amenable castle classes.

## 3. Skyline DFT - the skyline's own spectrum

The other four spectra need something built first: a transfer matrix, a path kernel, a graph. The skyline discrete Fourier transform (DFT) acts on the skyline itself, the column-height sequence `c_1, c_2, …, c_w` that Project Euler 502 counts:

```
ĉ_k  =  ∑_{j=1}^{w}  c_j · e^{−2πi jk/w},      k = 0, 1, …, w − 1
```

Terms used below. Each `ĉ_k` is a **bin**. The **support** is the set of bins with `ĉ_k ≠ 0`. The **magnitude spectrum** is the list `|ĉ_k|`, the transform with its phases thrown away. Write `ω = e^{2πi/w}`.

The transform is invertible, so it determines the skyline. Three readings are immediate:

- **Bin 0 is the area:** `ĉ_0 = ∑ c_j`, the number of cells, never 0.
- **Energy:** the Parseval identity `∑ |ĉ_k|² = w · ∑ c_j²` splits `∑ c_j²` across `w` frequency channels.
- **What the magnitudes forget:** `|ĉ_k|` is unchanged by a cyclic shift of the columns and by the mirror image.

### Why the Fourier basis: it diagonalizes the column difference

Let `Δ` be the cyclic column difference, `(Δc)_j = c_{j+1} − c_j` with column `w + 1` read as column 1. Shifting the columns by one multiplies bin `k` by `ω^k`, so `Δ` multiplies it by `ω^k − 1`. The Fourier waves are the eigenvectors of `Δ`, its eigenvalues are `ω^k − 1`, and `ĉ_k` is the skyline's coordinate along the `k`-th eigenvector. Squaring and summing:[^dft]

```
∑_j (c_{j+1} − c_j)²   =   (1/w) · ∑_k  4 sin²(πk/w) · |ĉ_k|²        (indices mod w)
```

The weight `4 sin²(πk/w)` is 0 at `k = 0` and largest at `k = w/2`. So a skyline whose neighbouring columns jump a lot carries its energy in the high bins, and a smooth one in the low bins. That is what the low-pass / high-pass split below measures.

**The wrap.** The DFT treats column `w` and column 1 as neighbours, and a castle does not. The version without the wrap is the type-II discrete cosine transform (DCT-II). It is the eigenbasis of the plain (non-wrapping) difference: `Δ^T Δ` is then the Laplacian of the path on `w` columns, with eigenvalues `4 sin²(πk/(2w))`. With orthonormal coefficients `X_k = α_k ∑_j c_j cos(πk(j − ½)/w)`, where `α_0 = √(1/w)` and `α_k = √(2/w)` otherwise:[^dft]

```
∑_{j<w} (c_{j+1} − c_j)²   =   ∑_k  4 sin²(πk/(2w)) · X_k²
```

The DFT is the right tool for periodic skylines (the sparse supports and tones below). The DCT is the right tool when a castle's two ends matter.

**Column differences and the castle graph.** The absolute differences, not their squares, fix the [[castle-graph](pages/castle-graph.md)]'s horizontal edges. From `min(a, b) = (a + b − |a − b|)/2`:[^dft]

```
∑_{i<w} min(c_i, c_{i+1})   =   area  −  (c_1 + c_w)/2  −  ½ ∑_{i<w} |c_{i+1} − c_i|
```

### Which supports a skyline can have

Heights are whole numbers, and that constrains the support completely.

Every `ĉ_k` lies in the field `Q(ω)`. Each symmetry of that field (Galois automorphism) sends `ω ↦ ω^a` for some `a` with `gcd(a, w) = 1`, and it sends `ĉ_k` to `ĉ_{ak}`. So `ĉ_k = 0` exactly when `ĉ_{ak} = 0`. The bins `ak` for such `a` are exactly the bins with the same `gcd(k, w)`. The support is therefore a union of the classes

```
D_d  =  { k : gcd(k, w) = d },      one for each divisor d of w,  of size φ(w/d)
```

where `φ(q)` counts the numbers from 1 to `q` that share no factor with `q`.

Every such union occurs. The Ramanujan sum `r_q(j) = ∑_{1 ≤ a ≤ q, gcd(a,q) = 1} e^{2πi aj/q}` is a whole number for every `j`.[^ramanujan] For `q` dividing `w`, its DFT is `w` on the class `D_{w/q}` and 0 elsewhere. A sum of Ramanujan sums, plus a constant that lifts every height to at least 1, is a skyline with any prescribed union. So:

> **The DFT supports of width-`w` skylines are exactly `{0}` together with any union of the classes `D_d`, `d` a proper divisor of `w`: `2^{τ(w) − 1}` supports, `τ(w)` the number of divisors of `w`.**

Checked on all 408,573 skylines with `w ≤ 9, h ≤ 4` and `w = 10, h ≤ 3`: every support is such a union. At `w = 12` all 32 unions occur.[^dft] Consequences:

- **Crenellated castles.** Support inside `{0, w/2}` means period 2: the heights alternate between two values. That needs `w` even, since `D_{w/2} = {w/2}` is one bin only then. At odd width an alternating skyline leaks into every bin: `(1,3,1,3,1)` has all 5 bins nonzero, `(1,3,1,3,1,3)` only `{0, 3}`.
- **Prime width.** The classes are `{0}` and everything else, so every non-rectangular skyline of prime width has all `w` bins nonzero.
- **Fewest bins.** A pattern repeating every `q` columns needs `φ(q)` bins besides bin 0. A nonconstant skyline has at least `p − 1` of them, `p` the smallest prime dividing `w`. Exactly two besides bin 0 needs `q ∈ {3, 4, 6}`.
- **Tones are sparse only approximately.** On [[song-as-castle](pages/song-as-castle.md)], the 2600 Hz tone at 8 kHz is a width-40 castle whose energy, mean removed, sits over 99% in bins 13 and 27. With whole-number heights it cannot be exactly those two: `gcd(13, 40) = 1`, so bin 13 shares its class with all 16 bins coprime to 40.

The proper-castle clause of Project Euler 502 (an even number of blocks, [[castle-sign](pages/castle-sign.md)]) is not handled by this argument. Which supports survive it is open.

### Three regimes

- **Low-pass castles** - energy concentrated in low-`k` modes. Smooth, mountain-shaped skylines with few tall peaks. The [[convex-castle](pages/convex-castle.md)] class and the [[stack-polyomino-gf](pages/stack-polyomino-gf.md)] unimodal family sit predominantly here.
- **High-pass castles** - energy concentrated in high-`k` modes. Jagged, alternating skylines with many blocks and gaps. The **crenellated** type ([[castle-classification-shape](pages/castle-classification-shape.md)] Axis 7), heights alternating `{a, h}`, is the extreme case. At even width its support is exactly `{0, w/2}`, a **two-atom spectrum**.
- **Sparse-spectrum castles** - a small set `S` of bins carries all the energy (`ĉ_k = 0` for `k ∉ S`). For whole-number skylines the possible `S` are the unions of divisor classes above: crenellated is `S = {0} ∪ D_{w/2}`, and other periodic patterns give larger classes. Approximate sparsity (most of the energy in a few bins, as for tones) is where compressed sensing applies.

**Skyline energy as an ordering.** Ordering castles by *which* channels carry the energy gives a continuous refinement of the discrete Axis 7 value-pattern types.

### Homometric castles - what the magnitude spectrum cannot hear

Two skylines of the same width are **homometric** when they have the same magnitude spectrum. That is the same as having the same cyclic autocorrelation `a_t = ∑_j c_j c_{j+t}` (indices mod `w`), because `|ĉ_k|²` is the DFT of `a_t`. The word is the crystallographers' term for point sets with the same autocorrelation.[^bg]

Three moves never change the magnitude spectrum: cyclic shift, mirror image, and the **flip about the mean height**, `c_j ↦ m − c_j` with `m = 2·area/w`. The flip is available when `m` is a whole number and every `m − c_j ≥ 1`. It keeps bin 0 equal to the area and changes the sign of every other bin. A **genuine** homometric pair is one not related by these moves.

An exhaustive search over every castle with at most 12 cells, using exact integer autocorrelations, finds none up to 10 cells, one pair at 11 cells, and four at 12.[^dft] The 11-cell pair:

```
(1,1,2,2,2,3)   .....#        (1,2,1,2,3,2)   ....#.
                ..####                        .#.###
                ######                        ######

|ĉ| = (11, 2, 2, 1, 2, 2)      a_t = (23, 20, 19, 20, 19, 20)      for both
```

The castle graph tells them apart: the first has three `2 × 2` blocks, the second two. So the edge counts differ, and so do the adjacency and Laplacian spectra.

The same question in two dimensions, for the set of cells instead of the height sequence, is the covariogram problem. Baake and Grimm construct homometric polyomino pairs that way.[^bg]

### The DFT against the graph spectra

- **The full transform separates everything.** It is invertible, so it tells apart any two distinct skylines, including every isospectral pair on [[isospectral-castles](pages/isospectral-castles.md)].
- **The magnitude spectrum fails exactly through the cyclic shift.** Up to 16 cells, mirror images removed, 44 adjacency-cospectral non-isomorphic pairs share their magnitude spectrum: 1 at 10 cells, 6 at 12, 9 at 14, 6 at 15, 22 at 16. So do 4 Laplacian-cospectral pairs, all at 16 cells. In every one, the second castle is a cyclic shift of the first or of its mirror image: two castles cut from the same ring of columns at different seams. No mean flip and no genuine homometric pair appears.[^dft]
- **Each hears what the other cannot.** The DFT hears the width and the column order; the graph spectrum does not tell `(2)` from `(1,1)`. The graph spectra hear the `2 × 2` blocks, which separate the 11-cell homometric pair.

The smallest pair the magnitude spectrum misses is the second of the two 10-cell adjacency groups, with characteristic polynomial `x¹⁰ − 10x⁸ + 30x⁶ − 28x⁴ + 7x²`. The second castle is the mirror image of the first, shifted two columns:

```
(1,2,1,1,3,2)   ....#.        (1,1,2,1,2,3)   .....#
                .#..##                        ..#.##
                ######                        ######
```

**Wiki ties:** [[castle-classification-shape](pages/castle-classification-shape.md)] Axis 7 (crenellated = support `{0, w/2}` at even width) and [[castle-classification-spectrum](pages/castle-classification-spectrum.md)] Axis 9 (sparse-spectrum as an individual-castle predicate; low/high-pass as soft variants); [[castle-representations](pages/castle-representations.md)] (the column-height sequence being transformed); [[castle-graph](pages/castle-graph.md)] (horizontal edges from column differences).

The reverse direction - sound to castle, lossless - is [[song-as-castle](pages/song-as-castle.md)]: a 16-bit waveform is an `h = 65536` skyline, so its DFT is the audio spectrum, and the number-theoretic transform mod 65537 is this same transform over a finite field with no rounding.

## 4. Combinatorial Laplacian — connectivity, bottlenecks, isospectral pairs

Treat the filled cells of a castle as the vertices of a graph; add an edge between every pair of orthogonally adjacent filled cells. This gives the **castle's polyomino graph** `G_C`. Its **combinatorial Laplacian** is

```
L(G_C)  =  D − A,        eigenvalues  0 = μ_0 ≤ μ_1 ≤ … ≤ μ_{n−1}
```

with `D` the diagonal degree matrix and `A` the adjacency matrix. The Laplacian spectrum encodes the castle's connectivity structure with well-known handles:

- **Algebraic connectivity `μ_1` (Fiedler value)** — measures how "bottlenecked" the castle is. A pyramidal castle (broad base) has larger `μ_1` than a T-shape or a castle with a narrow neck between two bulges. Fiedler eigenvector localizes on the bottleneck.
- **Cheeger inequality** — `h(G_C) ≥ μ_1 / 2`, where the Cheeger constant `h(G_C)` is the minimum boundary-to-volume ratio over vertex subsets. Detects **necks and bridges** in the castle geometrically.
- **Kirchhoff and the sandpile group** - every cofactor of `L` is the number of spanning trees, and the Smith normal form of the reduced Laplacian `L̃` is the castle's sandpile group, of that order, in the sink model (one sink cell); merging the bottom row into the sink gives the tide model's group. The sink group sees only the castle's graph of `2 × 2` blocks ([[sandpile-group](pages/sandpile-group.md)], [[sandpile-census](pages/sandpile-census.md)]).
- **Heat-kernel trace** — `Tr(e^{−tL}) = ∑_i e^{−t μ_i}`. Encodes the entire Laplacian spectrum in a single time-parameter function.

### Isospectral castles — "hear the shape of a castle"

Two castles with the **same Laplacian spectrum but non-isomorphic shape** are **isospectral**. This is Kac's classical "hear the shape of a drum" question specialized to the castle setting: given the spectrum of `L(G_C)`, can we recover `C` up to isomorphism? For polyominoes generally the answer is **no** — Sunada-type constructions produce isospectral non-isomorphic pairs — and castles are no exception: the smallest isospectral castle pairs have 10 cells (adjacency) and 11 cells (Laplacian), settled below.

**Search.** The exhaustive search through 16 cells (exact characteristic polynomials, isomorphism by networkx) is on [[isospectral-castles](pages/isospectral-castles.md)]; results below.

**Wiki ties:** [[castle-classification-spectrum](pages/castle-classification-spectrum.md)] Axis 9 (isospectral pair as an Axis-9 predicate; the pair predicate rather than a single-castle predicate); [[castle-snippets](pages/castle-snippets.md)] (enumeration primitives feeding the search).

## 5. Ihara zeta / Ramanujan castles — arithmetic-flavored spectral invariant

For the castle polyomino graph `G_C`, the **Ihara zeta function** is

```
ζ_{G_C}(u)  =  ∏_{[γ]}  (1 − u^{|γ|})^{−1}
```

where the product runs over equivalence classes of prime, backtrackless, tailless closed walks. `ζ_{G_C}(u)` is a rational function, and its poles are the eigenvalues of a modified **non-backtracking / edge-adjacency operator** on the graph. This is the graph-theoretic analog of the **Selberg zeta function** on hyperbolic surfaces — spectral information about the graph packaged as an arithmetic-flavored generating function over closed walks. Its behaviour at `u = 1` also sees the spanning-tree count, the order of the sink-model sandpile group ([[sandpile-group](pages/sandpile-group.md)]).

### Ramanujan castles

Castle graphs beyond four cells are never regular (the top-left cell has at most two neighbors, so a regular castle graph is a path or cycle: the single cell, the domino, or the `2×2` square). The regular-graph definition - every eigenvalue other than `±d` has `|λ| ≤ 2√(d − 1)` - therefore has no content on castles: for an irregular connected graph the spectral radius is strictly below `d_max`, excluding `±d_max` excludes nothing, and the Alon-Boppana bound is a lower bound on the largest *non-trivial* eigenvalue `λ(G) = max(λ_2, −λ_n)`, not on the spectral radius.

The definition that transfers is Greenberg's. Let `T` be the universal covering tree of `G_C` and `ρ(T)` its spectral radius (`2√(d − 1)` in the `d`-regular case). Greenberg's theorem gives `λ(G) ≥ ρ(T) − o(1)` for finite graphs covered by `T`, and `G_C` is a **Ramanujan castle** iff

```
|λ|  ≤  ρ(T)      for every eigenvalue λ ∉ {λ_1, −λ_1}.
```

Castle graphs are bipartite, so this is the bipartite-Ramanujan condition `λ_2 ≤ ρ(T)`. The method this section has to supply is `ρ(T)` for the castle's own covering tree; `2√(d_max − 1)` is only an upper bound on it, so `λ_2 ≤ 2√(d_max − 1)` is a necessary condition. Tree castles are their own universal cover and satisfy the condition trivially; the predicate bites only on castles with a `2×2` block.

- **Ihara-Ramanujan castles.** Transfer the condition to the non-backtracking operator's spectrum rather than adjacency. This is the version that connects most directly to the Ihara-zeta framework.

**Structural candidates worth checking first** ([[castle-classification-shape](pages/castle-classification-shape.md)] Axis 5 and 7 types with regular local structure):

- **Boxcastle** — the full `w × h` rectangle graph. Its adjacency spectrum is known explicitly: `2·cos(iπ/(w+1)) + 2·cos(jπ/(h+1))` for `1 ≤ i ≤ w, 1 ≤ j ≤ h`. **Settled** ([[ramanujan-castles](pages/ramanujan-castles.md)]): among rectangles the width-2 family fails first, at 28 cells - `(14,14)` is the smallest non-Ramanujan rectangle (`λ_2 = 2.82709 > ρ(T) = 2.81393`) - then width 3 at 33 cells and width 4 at 40; along the diagonal the first failing square is `8×8`. The smallest non-Ramanujan castles overall have 15 cells.
- **Hook** — small, spectrum computable by hand or trivially by SymPy.
- **Ferrers / staircase** — the standard partition-shape polyominoes with partial classical spectral results in the polyomino literature.
- **Crenellated** — alternating heights `{a, h}`. With `a = 1` the castle is a tree, hence Ramanujan ([[ramanujan-castles](pages/ramanujan-castles.md)]); with `a ≥ 2` it has cycles, and the census to 22 cells covers the small cases.

**Wiki tie:** [[castle-classification-spectrum](pages/castle-classification-spectrum.md)] Axis 9 states the Ramanujan-castle predicate; this section supplies the *method* (universal-cover spectral radius, Ihara zeta, adjacency-operator spectral analysis) whose output the Axis-9 predicate tests.

## Construction ↔ spectrum crosswalk

The five spectra above are not independent of the structural axes. Concrete construction rules force concrete spectral consequences — each row here is a **theorem-shaped claim** (some proved, some open) connecting an Axes 1-8 type to its forced spectral fingerprint:

| Structural rule / type | Forced spectral consequence |
|---|---|
| **Crenellated** (Axis 7, `c_i ∈ {a, h}` alternating) | Skyline DFT support exactly `{0, w/2}` at even width (two-atom), every bin at odd width; high-pass spectrum |
| **Boxcastle** (Axis 5, `c_i = h` all) | Adjacency spectrum `2·cos(iπ/(w+1)) + 2·cos(jπ/(h+1))` (`1 ≤ i ≤ w`, `1 ≤ j ≤ h`) and Laplacian spectrum `4 − 2·cos(iπ/w) − 2·cos(jπ/h)` (`0 ≤ i < w`, `0 ≤ j < h`), explicit closed forms |
| **Unimodal / pyramidal** (Axis 1) | Skyline DFT decays like `1/k` (sawtooth-DFT class); low-pass spectrum |
| **Even-parity-only** (PE 502 rule 6) | Transfer-matrix `T` splits into `±1` eigenspaces of the block-parity involution `σ`; castles live in the `+1` half; spectral projection = `½(I + σ)`. This is [[castle-sign](pages/castle-sign.md)]'s `(T ± P)/2` at the operator level. |
| **Silver width growth castle** (Axis 8) | The *class's* transfer matrix (the 1-smooth height-3 matrix `[[1,1,0],[1,1,1],[0,1,1]]` for the Pell strip) has spectral radius `1 + √2 ∈ Q(√2)`; PE 502's own signed transfer matrix never has a metallic eigenvalue |
| **Golden- / silver-spectrum castle** (Axis 9) | Adjacency spectral radius `φ` (the 4-cell paths) or `1 + √2` (36 mirror classes in a scan to width 10: both orientations of the `3×2` rectangle and 34 non-rectangular castles) - see [[castle-graph-spectral-radius](pages/castle-graph-spectral-radius.md)] |
| **q-Gibbs area-weighted** (`q = e^{−β}`, area-weighted measure) | Transfer matrix `T_β` with `β`-dependent spectrum. For fixed `h` the Perron root `λ_1(β)` of a finite positive matrix is simple and analytic in `β`, so there is no phase transition; one can occur only as `h → ∞` |

The last row is open in the `h → ∞` limit; it would connect [[castle-by-area](pages/castle-by-area.md)], the [[q-catalan-numbers](pages/q-catalan-numbers.md)] q-analogs, and the transfer-matrix spectrum.

## Two immediate targets

### `λ_1(h)` - settled

The transfer matrix `M_k` (`k = h − 1`) has characteristic polynomial `char_k` of degree `h` ([[generating-function-gallery](pages/generating-function-gallery.md)]), factored in closed form on [[tower-parity-sectors](pages/tower-parity-sectors.md)]: `char_k(2μ)/2^k = H_{k/2}(μ)·(H_{k/2+1}(μ) + μ² H_{k/2−1}(μ))` for even `k`, irreducible for odd `k` (verified `k ≤ 31`, proved for `k = 2^m − 1` on [[char-k-eisenstein-at-two](pages/char-k-eisenstein-at-two.md)]). The count's growth constant is `λ_1(h) = h`; the signed correction grows like `ρ_{h−1}` with `ρ_1 = √2`, `ρ_2 = 2`, `ρ_3 = 2.193`, `ρ_4 = 2.796`, `ρ_5 = 2.892`, `ρ_6 = 2ψ²` - algebraic, never metallic, and `2 ×` a unit exactly when `h ≡ 3 (mod 4)`. The metallic-mean ladder does not appear in PE 502's own spectrum; it appears in class transfer matrices (Axis 8) and in individual castle graphs (below). Full table and argument on [[castle-graph-spectral-radius](pages/castle-graph-spectral-radius.md)].

### The isospectral-castle hunt - settled

Run exhaustively over every castle with at most 16 cells (compositions of `n`, mirror-deduped, exact integer characteristic polynomials, isomorphism by networkx) on [[isospectral-castles](pages/isospectral-castles.md)]. The smallest non-isomorphic castles with the same **adjacency** spectrum have **10 cells** (`(1,1,1,2,3,2)` vs `(1,1,2,2,3,1)`, two groups at that size); with the same **Laplacian** spectrum, **11 cells** (`(1,1,1,2,1,1,2,1,1)` vs `(1,1,3,1,1,1,2,1)`, both trees); isospectral for both operators, **16 cells**. Groups multiply quickly afterwards (50 adjacency groups at 16 cells), so the spectrum is an invariant, not a classifier. Sand separates more: to 16 cells the sink-model sandpile group separates no cospectral group ([[sandpile-census](pages/sandpile-census.md)]), the sink clock spectrum 62 of 105 adjacency and 5 of 17 Laplacian ones ([[sandcastle-clock](pages/sandcastle-clock.md)]), and the avalanche profile all of them ([[sandpile-identity](pages/sandpile-identity.md)]).

## Where methods meet predicates

This page and [[castle-classification](pages/castle-classification.md)] are paired. The rough division of labor:

- **This page** — **methods**: how to compute each of the five spectra. What operator, what algorithm, what does the output mean.
- **[[castle-classification-spectrum](pages/castle-classification-spectrum.md)]** — **predicates**: which castle satisfies which spectral condition. Axis 9's tree, golden-/silver-spectrum, isospectral, and Ramanujan types are the current named types; more will land as the methods develop.

A spectral method plus a predicate on its output defines a castle type. The Ramanujan castle is the simplest example: the method (Ihara / adjacency-spectrum computation) exists in general graph theory; the predicate (`λ_2 ≤ ρ(T)`, the universal-cover threshold) sits on Axis 9; the type is named. Every other spectral method on this page has a parallel Axis-9 type it would populate when its computational side is fleshed out — sparse-spectrum from the DFT method, isospectral from the Laplacian method, sine-kernel bulk-limit membership from the LGV kernel method, silver-width-growth membership from the transfer-matrix method (already Axis 8).

## Open threads

- **`λ_1(h)`** - settled: `λ_1(h) = h`, signed corrections `ρ_{h−1}`, no metallic means ([[castle-graph-spectral-radius](pages/castle-graph-spectral-radius.md)], [[tower-parity-sectors](pages/tower-parity-sectors.md)]).
- **Golden- and silver-spectrum castles** - the first Axis 9 census: adjacency spectral radius `φ` for the six 4-cell paths, `1 + √2` for the `3×2` rectangle and three non-rectangular castles up to `w = 7`; copper and above impossible (max degree 4), bronze open ([[castle-graph-spectral-radius](pages/castle-graph-spectral-radius.md)]).
- **Isospectral hunt** - settled: smallest pairs at 10 cells (adjacency), 11 (Laplacian), 16 (both), on [[isospectral-castles](pages/isospectral-castles.md)].
- **LGV for castles** — a bijection from castles (or pairs of castles) to non-crossing path families, which would make §2 apply to castles themselves.
- **q-Gibbs critical-`β`** — whether the area-weighted transfer matrix has a non-analytic Perron root as `h → ∞` (the construction ↔ spectrum table's last row).
- **Ihara-zeta computations** for small castles — closed-form `ζ_{G_C}(u)` for boxcastles, hooks, staircases.
- **Sparse-spectrum classification** - settled for skylines: the supports are `{0}` plus unions of divisor classes (§3). Open for proper castles under the even-block clause.
- **Homometric census** - counts of genuine homometric pairs beyond 12 cells, and whether each comes from a factorization `c = a ⊛ b` paired with `a ⊛ reverse(b)` (`⊛` cyclic convolution); the turnpike-reconstruction hook.
- **DCT predicates** - low-pass / high-pass restated on the non-wrapping DCT-II, which respects the castle's two ends.


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
- [[levy-flights](pages/levy-flights.md)] — the fractional Laplacian `L^α = U diag(λ^α) U^T` on the castle graph, its Lévy-flight walk, and the local return probability as a non-spectral separator of the 11-cell Laplacian-isospectral tree pair.
- [[castle-eigenvalues-by-example](pages/castle-eigenvalues-by-example.md)] — the from-scratch pedagogy tutorial for Method 1 (adjacency spectrum) that this hub organizes.
- [[ramanujan-castles](pages/ramanujan-castles.md)] — computes `ρ(T)`, settles the boxcastle question §5 raises, and finds the smallest non-Ramanujan castles (15 cells).
- [[hear-the-shape-seminar](pages/hear-the-shape-seminar.md)] - the seminar walk-through of method 4 and the isospectral pairs.
- [[sandpile-group](pages/sandpile-group.md)] - the sandpile group introduced from the Laplacian and the boundary matrix.

## Footnotes

[^dft]: Verified by execution (2026-09-29), Python 3 with NumPy, SymPy and networkx. The cyclic energy identity and the eigenvalues `ω^k − 1` of the cyclic difference matrix (to `3 × 10^-15`) were checked on random skylines. The DCT-II eigenvectors and eigenvalues of the path Laplacian, the orthonormal DCT energy identity, and the horizontal-edge formula were checked on random skylines of widths 3 to 11. The support rule was checked on every skyline with `w ≤ 9, h ≤ 4` and `w = 10, h ≤ 3` (408,573 skylines, 0 violations, bins treated as zero below `10^-7`). At `w = 12`, sums of Ramanujan sums plus a constant realize all 32 unions, and Ramanujan sums are whole numbers to `2 × 10^-13` for `q ≤ 30`. The homometric search covers every composition of `n ≤ 12` (every castle with at most 12 cells, each at its own height), grouped by exact integer cyclic autocorrelation, with pairs related by cyclic shift, mirror image or mean flip set aside. The graph comparison grouped every castle with at most 16 cells (mirror images removed) by magnitude spectrum, compared adjacency and Laplacian eigenvalues at 7 decimals, and tested isomorphism with networkx. The 10-cell polynomial and the 11-cell pair's differing polynomials were confirmed with exact SymPy characteristic polynomials.

[^ramanujan]: https://en.wikipedia.org/wiki/Ramanujan%27s_sum §Formulas for c_q(n), Kluyver - "This shows that cq(n) is always an integer."

[^bg]: https://arxiv.org/pdf/0808.0094.pdf (Grimm and Baake, "Homometric point sets and inverse problems") abstract and §1 - "two point sets are called homometric when they share the same autocorrelation"; the excerpt also states "The polyominoes P1, P2 and their joint covariogram are displayed". Known from a search-result excerpt of the paper; the paper itself has not been read.
