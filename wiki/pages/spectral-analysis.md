---
title: Spectral analysis of castles
category: Concepts
summary: The spectra computed for castles and what each decides. (1) The signed transfer matrix M̃_k of the castle count, whose spectral radius ρ_k < k + 1 sets the correction terms of A^e(w, h) ~ h^w/2 and never equals a δ_a. (2) The Lindström-Gessel-Viennot determinant, which counts parallelogram polyominoes but not castles. (3) The skyline DFT, whose supports for whole-number heights are exactly bin 0 plus unions of divisor classes, with homometric castles from 11 cells and a worked example on the 1729 castle, whose bins are the divisibility tests for 9, 11 and 101. (4) The Laplacian of the castle graph, with its spanning trees, sandpile group and isospectral pairs. (5) The adjacency spectrum with the universal cover, which defines Ramanujan castles and the castles golden and silver by spectrum.
tags: [concept, castle, spectral, transfer-matrix, laplacian, dft, dct, galois, ramanujan-sum, homometric, ihara-zeta, ramanujan, isospectral, determinantal]
sources: [project-euler-502-brute-force]
created: 2026-09-16
updated: 2026-10-25
---

# Spectral analysis of castles

## The spectra

The wiki computes four spectra on castles, each from a different matrix, and section 2 records a determinant that applies to a neighboring family. [[castle-classification-spectrum](pages/castle-classification-spectrum.md)] states the castle types that each spectrum defines.

| § | spectrum | matrix | object | what it decides |
|---|---|---|---|---|
| 1 | eigenvalues of `M̃_k` | the signed transfer matrix on the tower heights `0, …, k` | the count `A^e(w, h)` | the growth `h` of the count and its correction terms; no `δ_a` |
| 2 | (a determinant) | Lindström-Gessel-Viennot | parallelogram polyominoes | their counts and exact sampling, not castles |
| 3 | the skyline DFT `ĉ_k` | the Fourier matrix on the column heights | one castle | supports, sparse-spectrum and crenellated castles, homometric pairs |
| 4 | Laplacian eigenvalues `μ_i` | `L = D − A` on the castle graph | one castle | spanning trees, sandpile group, isospectral pairs |
| 5 | adjacency eigenvalues and the universal cover | `A` on the castle graph | one castle | Ramanujan castles; castles golden and silver by spectrum |

The castle graph of a castle has its cells as vertices and an edge between cells that share a side ([[castle-graph](pages/castle-graph.md)]).

## 1. Transfer-matrix spectrum

The column-height dynamic program of [[project-euler-502-brute-force](pages/project-euler-502-brute-force.md)] steps from a column of height `a` to one of height `b` with the sign `(−1)^{max(0, b − a)}`, one factor `−1` for each new block. The same sum is the matrix product `P(k, L) = e_0ᵀ M̃_k^L v`, with `M̃_k` the signed transfer matrix of size `k + 1` on the tower heights `0, …, k`, which counts the blocks by descents, and `char_k` its characteristic polynomial ([[tower-parity-sectors](pages/tower-parity-sectors.md)]).[^bf] The unsigned transfer matrix of the skylines of height at most `h` is the all-ones `h × h` matrix, with largest eigenvalue `h`, and

```
A^e(w, h)  =  [h^w − (h−1)^w − P(h−1, w) + P(h−2, w)] / 2   ~   h^w / 2.
```

The spectral radius `ρ_k` of `M̃_k` satisfies `ρ_k < k + 1` for `k ≥ 1`, so the signed terms are `o(h^w)`. Its values are `ρ_1 = √2`, `ρ_2 = 2`, `ρ_3 = 2.193`, `ρ_4 = 2.796`, `ρ_5 = 2.892` and `ρ_6 = 2ψ² = 3.510`, with `ψ` the plastic number ([[plastic-number](pages/plastic-number.md)]). No `δ_a` is an eigenvalue of any `M̃_k`, because every eigenvalue is twice a root of the integer polynomial `char_k(2μ)/2^k`, whose leading coefficient is 2; `ρ_2 = 2` is copper, `σ_1^2`. [[castle-graph-spectral-radius](pages/castle-graph-spectral-radius.md)] gives the proofs and the table.

The metallic means `δ_a` appear as spectral radii of the transfer matrices of castle families: the anchored 1-smooth strips on the heights `{1, 2, 3}`, with the `3 × 3` matrix `[[1, 1, 0], [1, 1, 1], [0, 1, 1]]` and spectral radius `1 + √2` ([[pell-castle-strip](pages/pell-castle-strip.md)]), and the tree skylines of height at most 2, with the matrix `[[1, 1], [1, 0]]` and spectral radius `φ`. They also appear as adjacency spectral radii of castle graphs (section 5).

For each `k`, `char_k` is the characteristic polynomial of the recurrence of `P(k, ·)` in `L`, so the roots of that recurrence are the eigenvalues of `M̃_k`. The recurrence of `P(·, L)` in the tower height `k` is a different recurrence, with characteristic polynomial `(x+1)^L (x−1)^{L−2}` for every `L ≥ 4` ([[signed-tower-k-direction](pages/signed-tower-k-direction.md)]). [[eigenvalue-continued-fractions](pages/eigenvalue-continued-fractions.md)] gives the continued fractions of the roots of both recurrences.

## 2. Non-crossing paths

A parallelogram polyomino is a pair of lattice paths that meet only at their ends, so by the Lindström-Gessel-Viennot lemma the parallelogram polyominoes in a box are counted by a `2 × 2` determinant of binomial coefficients, a Narayana number, and [[castle-samplers](pages/castle-samplers.md)] §8 samples them exactly from that determinant. A castle is bounded by a single path, its skyline, so the lemma counts no castles.

## 3. Skyline DFT - the skyline's own spectrum

The skyline discrete Fourier transform (DFT) acts on the column-height sequence `c_1, c_2, …, c_w` itself:

```
ĉ_k  =  ∑_{j=1}^{w}  c_j · e^{−2πi jk/w},      k = 0, 1, …, w − 1
```

Terms used in this section. Each `ĉ_k` is a **bin**. The **support** is the set of bins with `ĉ_k ≠ 0`. The **magnitude spectrum** is the list `|ĉ_k|`, the transform with its phases thrown away. Write `ω = e^{2πi/w}`.

The transform is invertible, so it determines the skyline. Three readings are immediate:

- **Bin 0 is the area:** `ĉ_0 = ∑ c_j`, the number of cells, never 0.
- **Energy:** the Parseval identity `∑ |ĉ_k|² = w · ∑ c_j²` splits `∑ c_j²` across the `w` bins.
- **What the magnitudes forget:** `|ĉ_k|` is unchanged by a cyclic shift of the columns and by the mirror image.

### The Fourier basis diagonalizes the column difference

Let `Δ` be the cyclic column difference, `(Δc)_j = c_{j+1} − c_j` with column `w + 1` read as column 1. Shifting the columns by one multiplies bin `k` by `ω^k`, so `Δ` multiplies it by `ω^k − 1`. The Fourier waves are the eigenvectors of `Δ`, its eigenvalues are `ω^k − 1`, and `ĉ_k` is the skyline's coordinate along the `k`-th eigenvector. Squaring and summing:[^dft]

```
∑_j (c_{j+1} − c_j)²   =   (1/w) · ∑_k  4 sin²(πk/w) · |ĉ_k|²        (indices mod w)
```

The weight `4 sin²(πk/w)` is 0 at `k = 0` and largest at `k = w/2`, so the total squared jump between neighboring columns is the energy of the bins weighted toward `k = w/2`.

**The wrap.** The DFT treats column `w` and column 1 as neighbors, and a castle does not. The version without the wrap is the type-II discrete cosine transform (DCT-II). It is the eigenbasis of the plain (non-wrapping) difference: `ΔᵀΔ` is then the Laplacian of the path on `w` columns, with eigenvalues `4 sin²(πk/(2w))`. With orthonormal coefficients `X_k = α_k ∑_j c_j cos(πk(j − ½)/w)`, where `α_0 = √(1/w)` and `α_k = √(2/w)` otherwise:[^dft]

```
∑_{j<w} (c_{j+1} − c_j)²   =   ∑_k  4 sin²(πk/(2w)) · X_k²
```

The DFT suits periodic skylines, such as the tones of the next subsection; the DCT suits castles whose two ends differ.

**Column differences and the castle graph.** The absolute differences, not their squares, fix the castle graph's horizontal edges. From `min(a, b) = (a + b − |a − b|)/2`:[^dft]

```
∑_{i<w} min(c_i, c_{i+1})   =   area  −  (c_1 + c_w)/2  −  ½ ∑_{i<w} |c_{i+1} − c_i|
```

### Which supports a skyline can have

Heights are whole numbers, and that constrains the support completely.

Every `ĉ_k` lies in the field `Q(ω)`. Each symmetry of that field (Galois automorphism) sends `ω ↦ ω^a` for some `a` with `gcd(a, w) = 1`, and it sends `ĉ_k` to `ĉ_{ak}`. So `ĉ_k = 0` exactly when `ĉ_{ak} = 0`. The bins `ak` for such `a` are exactly the bins with the same `gcd(k, w)`. The support is therefore a union of the classes

```
D_d  =  { k : gcd(k, w) = d },      one for each divisor d of w,  of size tot(w/d)
```

where `tot(q)` is Euler's totient, the number of `a` from 1 to `q` with `gcd(a, q) = 1`, written `tot` because `φ` is the golden mean on the wiki.

Every such union occurs. For `q` dividing `w`, the Ramanujan sum `r_q(j) = ∑_{1 ≤ a ≤ q, gcd(a,q) = 1} e^{2πi aj/q}` is a whole number for every `j`: it is a sum of roots of unity, so an algebraic integer, and every automorphism of `Q(e^{2πi/q})` permutes its terms, so it is rational, and a rational algebraic integer is an integer. Its DFT is `w` on the class `D_{w/q}` and 0 elsewhere. A sum of Ramanujan sums, plus a constant that lifts every height to at least 1, is a skyline with any prescribed union. So:

> **The DFT supports of width-`w` skylines are exactly `{0}` together with any union of the classes `D_d`, `d` a proper divisor of `w`: `2^{τ(w) − 1}` supports, `τ(w)` the number of divisors of `w`.**

Checked on all 408,573 skylines with `w ≤ 9, h ≤ 4` and `w = 10, h ≤ 3`: every support is such a union. At `w = 12` all 32 unions occur.[^dft] Consequences:

- **Crenellated castles.** Support inside `{0, w/2}` means period 2: the heights alternate between two values. That needs `w` even, since `D_{w/2} = {w/2}` is one bin only then. At odd width an alternating skyline has every bin nonzero: for `k ≠ 0`, `ĉ_k` is the difference of the two heights times the sum of `ω^{−jk}` over the odd `j`, a geometric sum with ratio `ω^{−2k} ≠ 1` and nonzero numerator `1 − ω^{−k}`. So `(1,3,1,3,1)` has all 5 bins nonzero, and `(1,3,1,3,1,3)` only `{0, 3}`.
- **Prime width.** The classes are `{0}` and everything else, so every non-rectangular skyline of prime width has all `w` bins nonzero.
- **Fewest bins.** The class `D_{w/q}` of the waves of exact period `q` has `tot(q)` bins. A nonconstant skyline has at least `p − 1` bins besides bin 0, `p` the smallest prime dividing `w`. Exactly two besides bin 0 needs the class of a period `q ∈ {3, 4, 6}`.
- **Tones are sparse only approximately.** On [[song-as-castle](pages/song-as-castle.md)], the 2600 Hz tone at 8 kHz is a width-40 castle whose energy, mean removed, sits over 99% in bins 13 and 27. With whole-number heights it cannot be exactly those two: `gcd(13, 40) = 1`, so bin 13 shares its class with all 16 bins coprime to 40. Across the 35 telephone signals of [[tone-castle-catalogue](pages/tone-castle-catalogue.md)] (DTMF, MF, call progress, 2600 Hz) quantized to `h = 256`, the bins of the tones carry 99.997% to 99.999% of the mean-removed energy, and 30 of the 35 castles have all `w` bins nonzero.

A castle is sparse-spectrum when its support is bin 0 together with at most one class and is not all `w` bins: the rectangles, the crenellated castles at even width, and the castles whose support is one class ([[castle-classification-spectrum](pages/castle-classification-spectrum.md)]). Which supports occur among castles with an even number of blocks, the Project Euler condition ([[castle-sign](pages/castle-sign.md)]), is not settled by this argument.

### Homometric castles

Two skylines of the same width are **homometric** when they have the same magnitude spectrum. That is the same as having the same cyclic autocorrelation `a_t = ∑_j c_j c_{j+t}` (indices mod `w`), because `|ĉ_k|²` is the DFT of `a_t`. The word is from diffraction theory, where two point sets are homometric when they share the same autocorrelation.[^bg]

Three moves never change the magnitude spectrum: cyclic shift, mirror image, and the **flip about the mean height**, `c_j ↦ m − c_j` with `m = 2·area/w`. The flip is available when `m` is a whole number and every `m − c_j ≥ 1`. It keeps bin 0 equal to the area and changes the sign of every other bin. A **genuine** homometric pair is one not related by these moves.

An exhaustive search over every castle with at most 12 cells, using exact integer autocorrelations, finds no genuine pair up to 10 cells, one pair at 11 cells, and four at 12.[^dft] The 11-cell pair:

```
(1,1,2,2,2,3)   .....#        (1,2,1,2,3,2)   ....#.
                ..####                        .#.###
                ######                        ######

|ĉ| = (11, 2, 2, 1, 2, 2)      a_t = (23, 20, 19, 20, 19, 20)      for both
```

The castle graph tells them apart: the first has three `2 × 2` squares of cells, the second two. So their edge counts differ, and so do their adjacency and Laplacian spectra.

For sets of cells in the plane instead of height sequences, Grimm and Baake give two polyominoes with the same covariogram, the two-dimensional autocorrelation, obtained from a homometric pair of finite point sets in `Z²`.[^bg]

### The DFT against the graph spectra

- **The full transform separates everything.** It is invertible, so it tells apart any two distinct skylines, including every isospectral pair on [[isospectral-castles](pages/isospectral-castles.md)].
- **The magnitude spectrum fails exactly through the cyclic shift.** Up to 16 cells, mirror images removed, 44 pairs of castles with non-isomorphic graphs and the same adjacency spectrum share their magnitude spectrum: 1 at 10 cells, 6 at 12, 9 at 14, 6 at 15, 22 at 16. So do 4 pairs with the same Laplacian spectrum, all at 16 cells. In every one, the second castle is a cyclic shift of the first or of its mirror image. No mean flip and no genuine homometric pair appears.[^dft]
- **Each separates pairs the other does not.** The DFT detects the width and the column order; the graph spectrum does not tell `(2)` from `(1,1)`. The graph spectra detect the `2 × 2` squares, which separate the 11-cell homometric pair.

The smallest pair the magnitude spectrum misses is the second of the two 10-cell adjacency groups, with characteristic polynomial `x¹⁰ − 10x⁸ + 30x⁶ − 28x⁴ + 7x²`. The second castle is the mirror image of the first, shifted two columns:

```
(1,2,1,1,3,2)   ....#.        (1,1,2,1,2,3)   .....#
                .#..##                        ..#.##
                ######                        ######
```

### Worked example: the 1729 castle

The base-10 digit castle of 1729, `(1, 7, 2, 9)`, is the Hardy-Ramanujan castle of [[hardy-ramanujan-castle](pages/hardy-ramanujan-castle.md)]: width 4, height 9, area 19.[^hr]

```
   #
   #
 # #
 # #
 # #
 # #
 # #
 ###
####      (1, 7, 2, 9)
```

**The four bins.** At width 4, `ω = i`, so `e^{−2πi jk/4} = (−i)^{jk}`:

```
ĉ_0  =   1 +  7 +  2 + 9     =  19
ĉ_1  =  −i −  7 + 2i + 9     =  2 + i
ĉ_2  =  −1 +  7 −  2 + 9     =  13
ĉ_3  =  conjugate of ĉ_1     =  2 − i
```

Parseval checks: `19² + 5 + 13² + 5 = 540 = 4 · (1 + 49 + 4 + 81)`.

**Nearly crenellated.** Remove the mean height `19/4` and 94.4% of the remaining energy sits in bin 2, the wave that alternates column by column; bins 1 and 3 share the other 5.6%. The support is every bin, the classes `D_4 = {0}`, `D_2 = {2}` and `D_1 = {1, 3}`, with bins 1 and 3 arriving as a pair as the support rule requires. The non-wrapping DCT-II spreads the same energy 66% on its mode 3, 34% on mode 1 and under 1% on mode 2. The difference is the wrap: the DFT puts column 4 (height 9) next to column 1 (height 1) and reads one more alternation.

**The bins are divisibility tests.** Read the columns as the digits of `N = 1729`. The digit polynomial `Q(y) = y³ + 7y² + 2y + 9` has `Q(10) = N` and `ĉ_k = Q(ω^k)`. And `10⁴ − 1 = 9 · 11 · 101` factors into the cyclotomic values `Φ_1(10) = 9`, `Φ_2(10) = 11`, `Φ_4(10) = 101`, one per class:

| class | bins | value | the test it is | 1729 mod |
|---|---|---|---|---|
| `D_4` | `ĉ_0` | 19, the digit sum | casting out nines | `9`: `19 ≡ 1` |
| `D_2` | `ĉ_2` | 13, the alternating digit sum | the test for 11 | `11`: `13 ≡ 2` |
| `D_1` | `ĉ_1, ĉ_3` | `2 ± i`, from `Q mod (y² + 1) = y + 2` | the test for 101 (alternate two-digit blocks: `29 − 17`) | `101`: `10 + 2 = 12` |

In general, for a digit castle of width `w` and a divisor `q` of `w`, the bins of the class of order `q` are the values of `Q` at the primitive `q`-th roots of unity. They determine the remainder of `Q` modulo the cyclotomic polynomial `Φ_q`, because `Z[y]/Φ_q` embeds in `Q(e^{2πi/q})` by evaluation, and so they determine `N mod Φ_q(10)`, since evaluation at 10 maps `Z[y]/Φ_q` onto `Z/Φ_q(10)`. When they all vanish, `Φ_q` divides `Q`, and `Φ_q(10)` divides `N`. At four digits, bin 2 is zero exactly when the alternating digit sum is, the classical test for 11. The vanishing case was checked on every digit castle of 2 to 6 digits.[^hr]

**What the magnitudes determine.** The magnitude spectrum is `(19, √5, 13, √5)` and the autocorrelation `a_t = (135, 48, 130, 48)`. The width-4 castles with this autocorrelation are exactly the cyclic shifts and mirror images of `(1, 7, 2, 9)`, and the mean flip is unavailable because `2 · 19 / 4` is not whole.[^hr]

**The graph side.** 19 cells, 20 edges, and two `2 × 2` squares sharing an edge, so 15 spanning trees and sandpile group `Z/15` ([[sandpile-group](pages/sandpile-group.md)]), the same as the 10-cell adjacency-cospectral pair `(1,1,1,2,3,2)`, `(1,1,2,2,3,1)` of [[isospectral-castles](pages/isospectral-castles.md)]. Adjacency spectral radius `2.5982`, and `λ_2 = 1.8981`. The castle is Ramanujan: a finite subtree of its universal covering tree has spectral radius at least `2.5559`, so `ρ ≥ 2.5559 > λ_2` (section 5).[^hr] The Fiedler value (the smallest nonzero Laplacian eigenvalue) is `0.046`. Among all 19-cell castles, none with a different graph shares its adjacency or its Laplacian spectrum, so the graph spectrum determines the graph. It does not determine the castle: 29 skylines, mirror images removed, have that same graph, `(1, 3, 10, 1, 4)` among them.[^hr]

[[song-as-castle](pages/song-as-castle.md)] reads a 16-bit waveform, shifted to heights 1 to 65536, as a skyline, so its DFT is the audio spectrum; the number-theoretic transform modulo the prime 65537 computes the same transform with no rounding ([[finite-fields](pages/finite-fields.md)]).

## 4. Combinatorial Laplacian - spanning trees, sandpiles, isospectral pairs

The combinatorial Laplacian of the castle graph is

```
L  =  D − A,        eigenvalues  0 = μ_0 ≤ μ_1 ≤ … ≤ μ_{n−1}
```

with `D` the diagonal matrix of degrees and `A` the adjacency matrix. The castle graph is connected, so `μ_1 > 0`; `μ_1` is the **Fiedler value**, or algebraic connectivity. For the 1729 castle it is `0.046`, small because two tall columns stand on a four-cell base.

**Spanning trees and the sandpile group.** Every cofactor of `L` is the number of spanning trees of the castle graph (the matrix-tree theorem). Deleting the row and column of one sink cell gives the reduced Laplacian `L̃`, whose Smith normal form is the castle's sandpile group in the sink model, of that order; merging the whole bottom row into the sink gives the tide model's group. In the sink model the group depends only on the castle's graph of `2 × 2` squares ([[sandpile-group](pages/sandpile-group.md)], [[sandpile-census](pages/sandpile-census.md)]).

**Isospectral castles.** The spectrum of the castle graph does not determine the graph. Over every castle with at most 16 cells ([[isospectral-castles](pages/isospectral-castles.md)]), the smallest non-isomorphic castle graphs with the same adjacency spectrum have 10 cells, `(1,1,1,2,3,2)` and `(1,1,2,2,3,1)`; with the same Laplacian spectrum, 11 cells, `(1,1,1,2,1,1,2,1,1)` and `(1,1,3,1,1,1,2,1)`, both trees; with both spectra equal, 16 cells. Up to 16 cells there are 105 groups of non-isomorphic castle graphs with the same adjacency spectrum, 50 of them at 16 cells, and 17 with the same Laplacian spectrum.[^dft] The sink-model sandpile group separates none of these groups ([[sandpile-census](pages/sandpile-census.md)]), the sink clock spectrum separates 62 of the 105 adjacency groups and 5 of the 17 Laplacian groups ([[sandcastle-clock](pages/sandcastle-clock.md)]), and the sink avalanche profile separates all of them ([[sandpile-identity](pages/sandpile-identity.md)]).

## 5. Adjacency spectrum and the universal cover - Ramanujan castles

**Ramanujan castles.** For a connected graph `G` with adjacency eigenvalues `λ_n ≤ ⋯ ≤ λ_2 ≤ λ_1`, let `λ(G) = max(λ_2, −λ_n)` and let `ρ(G)` be the spectral radius of the universal covering tree of `G`, which is `2√(d − 1)` when `G` is `d`-regular. Greenberg's theorem gives `λ(G) ≥ ρ − o(1)` for the finite graphs covered by a fixed tree, and the graphs with `λ(G) ≤ ρ(G)` are the Ramanujan graphs.[^hps] Castle graphs with more than four cells are not regular ([[castle-classification-spectrum](pages/castle-classification-spectrum.md)]), so `ρ(G)` is computed for each castle's own covering tree. Castle graphs are bipartite, so `λ_n = −λ_1`, and a **Ramanujan castle** is one whose castle graph satisfies `λ_2 ≤ ρ(G)`, the bipartite form of the condition.

The covering tree `T` has maximum degree `d_max`, the largest degree in `G`, so it is a subgraph of the `d_max`-regular tree and `ρ(G) ≤ 2√(d_max − 1)`; so `λ_2 ≤ 2√(d_max − 1)` is a necessary condition. Every finite subtree of `T` has spectral radius at most `ρ(G)`, which gives lower bounds, as for the 1729 castle (section 3). A finite tree is its own universal cover, so every tree castle is Ramanujan.

[[ramanujan-castles](pages/ramanujan-castles.md)] computes `ρ(G)` exactly by an edge-cavity method. Every castle with at most 14 cells is Ramanujan, and the smallest non-Ramanujan castles have 15 cells. Among rectangles, whose adjacency spectrum is `2cos(iπ/(w+1)) + 2cos(jπ/(h+1))` for `1 ≤ i ≤ w`, `1 ≤ j ≤ h`, the `2 × 14` rectangle `(14, 14)` fails first, at 28 cells, with `λ_2 = 2.82709` against `ρ = 2.81393`; the first failing `3 × h` rectangle has 33 cells, the first `4 × h` 40, and the first failing square is `8 × 8`. A crenellated castle with low height 1 is a tree, so it is Ramanujan.

**Castles golden and silver by spectrum.** The spectral radius `λ_1` of the castle graph is the statistic of these types: `φ` for exactly the six castles whose graph is the path `P_4`, and `1 + √2` for 36 castles up to mirror image in a scan of 4,868,525 castles ([[castle-graph-spectral-radius](pages/castle-graph-spectral-radius.md)]).

**The Ihara zeta function.** `ζ(u) = ∏_{[γ]} (1 − u^{|γ|})^{−1}`, over the equivalence classes of closed walks that are prime, without backtracking and without tails, is a further invariant of the castle graph. A tree has no such walk, so a tree castle has `ζ(u) = 1`.

## Construction and spectrum

| castle type | spectral consequence |
|---|---|
| **Crenellated**, heights alternating between two values | skyline DFT support exactly `{0, w/2}` at even width, every bin at odd width (section 3) |
| **Rectangle** `w × h` | adjacency spectrum `2cos(iπ/(w+1)) + 2cos(jπ/(h+1))` (`1 ≤ i ≤ w`, `1 ≤ j ≤ h`) and Laplacian spectrum `4 − 2cos(iπ/w) − 2cos(jπ/h)` (`0 ≤ i < w`, `0 ≤ j < h`), the sums of the path spectra |
| **Anchored 1-smooth strips on `{1, 2, 3}`**, silver by width | transfer matrix `[[1, 1, 0], [1, 1, 1], [0, 1, 1]]` with spectral radius `1 + √2`; the count's own signed transfer matrix never has a `δ_a` eigenvalue (section 1) |
| **Golden and silver by spectrum** | adjacency spectral radius `φ` (the six `P_4` castles) or `1 + √2` (36 castles up to mirror image in the scan of [[castle-graph-spectral-radius](pages/castle-graph-spectral-radius.md)]) |
| **Weighted by area**, a factor `q^c` for a column of height `c`, in a family given by a primitive 0/1 rule `M` on `{1, …, h}` | the transfer matrix with entries `M[a][b]·q^b` is primitive for `q > 0`, so its largest eigenvalue is simple (Perron-Frobenius) and analytic in `q`, and there is no non-analytic point at fixed `h` |

## Related Concepts

- [[castle-classification-spectrum](pages/castle-classification-spectrum.md)] - the castle types each spectrum defines: tree, golden and silver by spectrum, isospectral, Ramanujan and sparse-spectrum castles.
- [[castle-classification](pages/castle-classification.md)] - the hub of the castle classification.
- [[castle-graph-spectral-radius](pages/castle-graph-spectral-radius.md)] - the metallic means in the transfer-matrix spectra and the spectral-radius census of castle graphs.
- [[castle-graph](pages/castle-graph.md)] - the castle graph, its cycle rank, and the tree castles.
- [[tower-parity-sectors](pages/tower-parity-sectors.md)] - `M̃_k`, `P(k, L) = e_0ᵀ M̃_k^L v`, and the factorization of `char_k`.
- [[eigenvalue-continued-fractions](pages/eigenvalue-continued-fractions.md)] - the continued fractions of the eigenvalues of the castle recurrences.
- [[project-euler-502-brute-force](pages/project-euler-502-brute-force.md)] - the column-height dynamic program, the matrix product of section 1.
- [[castle-counting-formula](pages/castle-counting-formula.md)] - the formula for `A^e(w, h)` and the generating functions `num_k/den_k` of `P(k, ·)`.
- [[castle-representations](pages/castle-representations.md)] - the column-height sequence the DFT transforms.
- [[castle-samplers](pages/castle-samplers.md)] - the Lindström-Gessel-Viennot sampler for parallelogram polyominoes.
- [[isospectral-castles](pages/isospectral-castles.md)] - the isospectral pairs to 16 cells.
- [[ramanujan-castles](pages/ramanujan-castles.md)] - the edge-cavity computation of `ρ(G)` and the Ramanujan census to 22 cells.
- [[castle-eigenvalues-by-example](pages/castle-eigenvalues-by-example.md)] - the adjacency eigenvalues of small castles worked by hand.
- [[hear-the-shape-seminar](pages/hear-the-shape-seminar.md)] - a seminar on what the spectrum of the castle graph determines.
- [[levy-flights](pages/levy-flights.md)] - the fractional Laplacian `L^α` of the castle graph and its random walk, whose return probabilities separate the 11-cell Laplacian-isospectral pair of trees.
- [[tone-castle-catalogue](pages/tone-castle-catalogue.md)] - section 3 applied to telephone tones: exact periods and divisor-class supports.
- [[sandpile-group](pages/sandpile-group.md)] - the sandpile group from the reduced Laplacian.
- [[castle-compression](pages/castle-compression.md)] - how many bits a castle takes to write down, by encoding.
- [[pell-castle-strip](pages/pell-castle-strip.md)] - the strips whose transfer matrix has spectral radius `1 + √2`.

## Footnotes

[^bf]: [[project-euler-502-brute-force](pages/project-euler-502-brute-force.md)] §"p_signed" L31 - "A new column of height b after a column of height a starts max(0, b - a) new runs, each contributing a factor of -1."
[^dft]: Verified by execution (2026-09-29), Python 3 with NumPy, SymPy and networkx. The cyclic energy identity and the eigenvalues `ω^k − 1` of the cyclic difference matrix (to `3 × 10^-15`) were checked on random skylines. The DCT-II eigenvectors and eigenvalues of the path Laplacian, the orthonormal DCT energy identity, and the horizontal-edge formula were checked on random skylines of widths 3 to 11. The support rule was checked on every skyline with `w ≤ 9, h ≤ 4` and `w = 10, h ≤ 3` (408,573 skylines, 0 violations, bins treated as zero below `10^-7`). At `w = 12`, sums of Ramanujan sums plus a constant realize all 32 unions, and Ramanujan sums are whole numbers to `2 × 10^-13` for `q ≤ 30`. Re-verified 2026-10-16: the homometric search over every composition of `n ≤ 12` (genuine pairs 0 up to 10 cells, 1 at 11, 4 at 12), the 11-cell pair's magnitudes and autocorrelations; over every castle with at most 16 cells (33,150 up to mirror image), the isomorphism classes by networkx, the 105 adjacency and 17 Laplacian cospectral groups (eigenvalues at 7 decimals), and the 44 and 4 magnitude-spectrum pairs, all related by cyclic shift or mirror image; the 10-cell characteristic polynomial.
[^bg]: https://arxiv.org/pdf/0808.0094 (U. Grimm and M. Baake, "Homometric point sets and inverse problems", read 2026-10-16) - abstract, p.1: "two point sets are called homometric when they share the same autocorrelation"; §2.1, p.3: "An interesting example of two polyominoes with the same covariogram" is "P1 = F1 + C and P2 = F2 + C", from the homometric finite point sets `F1, F2 ⊂ Z²` of §2, with `C` the unit square.
[^hr]: Verified by execution (2026-09-30, re-verified 2026-10-16), Python 3 with NumPy, SymPy and networkx. Bins computed with the column index running `j = 1..w`, as in the definition above; energy shares with the mean removed (bin 2: 169 of 179); orthonormal DCT-II (shares 0.659, 0.335, 0.006). The width-4 castles with autocorrelation `(135, 48, 130, 48)` are the eight shifts and mirror images of `(1, 7, 2, 9)`. The vanishing check covered every digit castle of 2 to 6 digits with digits 1 to 9: whenever the bins of the class of order `q` all vanish, `Φ_q(10)` divides `N`, with 0 exceptions (at 4 digits, 489 castles with bin 2 zero and 81 with bins 1 and 3 zero). Every composition of 19 (mirror images removed) was compared with `(1, 7, 2, 9)` by adjacency and Laplacian eigenvalues at 6 decimals; all 29 matches are isomorphic to it by networkx. Spanning trees by the matrix-tree theorem, the group `Z/15` by the Smith normal form of `L̃`; `λ_1 = 2.598215`, `λ_2 = 1.898131`, Fiedler value `0.046172`; the Rayleigh quotient `2.55596` on the subtree of non-backtracking walks of length at most 16 from the best root (1736 vertices) is a lower bound for `ρ`.
[^hps]: https://arxiv.org/pdf/1506.02335 (C. Hall, D. Puder and W. F. Sawin, *Ramanujan coverings of graphs*, read 2026-10-16) - §1.1 p.2: "λ(G) = max(λ2, −λn)", "Let ρ(G) be the spectral radius of the universal covering tree of G. For instance, if G is k-regular then ρ(G) = 2√(k−1)"; §2.1 p.12, Theorem 2.1 (Greenberg, in Cioabă's version): "λ(G) ≥ ρ − o_n(1)", and "graphs G satisfying λ(G) ≤ ρ(G) are considered to be optimal expanders. Following the terminology of [LPS88], they are called Ramanujan graphs."
