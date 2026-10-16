---
title: Castle classification - spectral types
category: Concepts
summary: Predicates on a single castle read from a spectrum. From the castle graph (cells as vertices, edges between cells that share a side) - tree castles, whose graph is a tree (F_{w+2} − 1 of height 2, exactly the castles with a trivial sandpile group); castles golden by spectrum, spectral radius φ, which are exactly the six castles whose graph is the path P_4, by Smith's theorem; castles silver by spectrum, spectral radius 1 + √2, 36 up to mirror image in a scan of 4,868,525 castles; spectral radius φ²; isospectral pairs (smallest at 10 cells for the adjacency spectrum, 11 for the Laplacian); and Ramanujan castles in Greenberg's universal-cover form (every castle with at most 14 cells; the first failures have 15). From the skyline DFT, whose supports are bin 0 plus unions of divisor classes - sparse-spectrum castles, with support bin 0 and at most one class, crenellated castles at even width among them.
tags: [concept, castle, classification, taxonomy, spectral, adjacency-matrix, laplacian, ramanujan, smith-theorem, dynkin, tree-castle, isospectral, single-castle-predicate, dft, sparse-spectrum]
sources: [oeis-mining-pe502]
created: 2026-09-19
updated: 2026-10-16
---

# Castle classification - spectral types

## Scope: single-castle predicates on a spectrum

A spectral type is a predicate on one castle, as the shape types of [[castle-classification-shape](pages/castle-classification-shape.md)] are, but read from a spectrum instead of from the skyline `(c_1, …, c_w)`. Most read the castle graph `G_c` of [[castle-graph](pages/castle-graph.md)], with the cells as vertices and an edge between cells that share a side, through the spectrum of its adjacency matrix or of its Laplacian; the sparse-spectrum castles read the discrete Fourier transform of the skyline. [[spectral-analysis](pages/spectral-analysis.md)] describes how each spectrum is computed.

*Example.* The castle `(1, 1, 2)` has four cells and the castle graph `P_4`, a path, with adjacency eigenvalues `±φ` and `±1/φ`.

Two facts about castle graphs are used in the sections that follow.

- **Bipartite.** Coloring the cell in column `i` and row `j` by the parity of `i + j` gives neighboring cells opposite colors. So the adjacency spectrum is symmetric about 0, and the smallest eigenvalue is `−λ_1` (Brouwer and Haemers, Proposition 3.4.1).[^1]
- **Regular only up to four cells.** The leftmost cell of the top row has no neighbor to its left or above it, so it has at most two neighbors, and a regular castle graph has degree at most 2: a single cell, a path or a cycle. A path with more than two vertices has degree-1 ends and degree-2 middles. In a castle of width at least 3 whose cells all have two neighbors, the bottom cells of the inner columns already have two neighbors, so those columns have height 1; the bottom cell of an end column needs a cell above it, so the end column has height at least 2, and then its top cell has one neighbor, a contradiction; at width 2 only `(2, 2)` has every cell with two neighbors. So the only castle graph that is a cycle is the 4-cycle `(2, 2)`. The regular castle graphs are the single cell `(1)`, `P_2` (the castles `(1, 1)` and `(2)`) and the 4-cycle `(2, 2)`.

## Tree castles

**Predicate.** The castle graph is a tree.

**Skyline form.** No `2 × 2` square of cells, that is, no two neighboring columns of height at least 2 ([[castle-graph](pages/castle-graph.md)]). For example, `(2, 1, 2)` is a tree castle and `(2, 2)` is not.

**Counts.** Write `T_h(w)` for the tree skylines of width `w` with heights in `{1, …, h}`, which need not reach `h` and are not castles, and `A_tree(w, h) = T_h(w) − T_{h−1}(w)` for the tree castles of height `h`. The tree skylines satisfy `T_h(w + 2) = T_h(w + 1) + (h − 1) T_h(w)`, so both grow at `(1 + √(4h − 3))/2 = σ_1^{h−1}` ([[castle-graph](pages/castle-graph.md)]). The tree skylines are named OEIS sequences:[^2]

- `h = 2`: `T_2(w) = F_{w+2}`, so the tree castles of height 2, the Fibonacci castles, number `F_{w+2} − 1 = A000071(w + 2)` and are golden by width ([[castle-classification-growth](pages/castle-classification-growth.md)]);
- `h = 3`: `T_3(w) = A001045(w + 2)`, the Jacobsthal numbers;
- `h = 4, 5`: `T_4(w) = A006130(w + 1)` and `T_5(w) = A006131(w + 1)`.

By area, the tree skylines of height at most `h` have the generating function `G_h(q) = (1 + P_h(q))/(1 − q − q·P_h(q))` with `P_h(q) = q² + ⋯ + q^h`, so the denominator is `1 − q − q³ − ⋯ − q^{h+1}`; all skylines of height at most `h` have the denominator `1 − q − q² − ⋯ − q^h`, the `h`-nacci denominator ([[tree-castle-by-area](pages/tree-castle-by-area.md)], [[castles-of-height-h-by-area](pages/castles-of-height-h-by-area.md)]). The tree skylines by area grow at the supergolden ratio at `h = 2` (A000930), at `φ` at `h = 3` (A006498), and at `ψ²` without a height bound (A005251), `ψ` the plastic number.

**Sandpile group.** The tree castles are exactly the castles whose sandpile group is trivial, in the sink model and in the tide model ([[sandpile-census](pages/sandpile-census.md)]).

## Castles golden and silver by spectrum

**Predicates.** A castle is **golden by spectrum** when the spectral radius of its castle graph is `φ = (1 + √5)/2`, and **silver by spectrum** when it is `1 + √2`. The radius `φ² = (3 + √5)/2` is the third type of this kind; it is not one of de Spinadel's metallic means and has no name.

**Census.** Among all castles with `w ≤ 6` and `h ≤ 6` and with `w = 7` and `h ≤ 5` ([[castle-graph-spectral-radius](pages/castle-graph-spectral-radius.md)]):

- **Golden by spectrum.** The six 4-cell castles `(4)`, `(1, 3)`, `(3, 1)`, `(1, 1, 2)`, `(2, 1, 1)` and `(1, 1, 1, 1)`, whose graph is the path `P_4`.
- **Silver by spectrum.** The `3 × 2` rectangle in both orientations, `(2, 2, 2)` and `(3, 3)`, whose graph is `P_2 × P_3`, and three mirror pairs, `(1, 2, 3, 1, 2, 3)`, `(2, 1, 6, 2, 1, 3)` and `(1, 1, 2, 4, 1, 3, 1)`. Each has `x² − 2x − 1` dividing its characteristic polynomial. Over all castles with `w ≤ 8` and `h ≤ 7`, with `w = 9` and `h ≤ 5`, and with `w = 10` and `h ≤ 4`, there are 36 castles silver by spectrum up to mirror image, with 6 to 20 cells.
- **Spectral radius `φ²`.** `(4, 4)` and `(2, 2, 2, 2)`, both `P_2 × P_4`, and `(1, 3, 2, 3, 1)`; 11 castles up to mirror image in the larger scan.

**The six `P_4` castles are the only castles golden by spectrum.** Smith's theorem states that a connected graph with largest eigenvalue less than 2 is one of the Dynkin diagrams `A_n = P_n`, `D_n` (`n ≥ 4`), `E_6`, `E_7`, `E_8`, and their largest eigenvalues are `2cos(π/(n+1))`, `2cos(π/(2n−2))`, `2cos(π/12)`, `2cos(π/18)` and `2cos(π/30)` (Brouwer and Haemers, Theorem 3.1.3 and p.35).[^1] Since `φ = 2cos(π/5) < 2`, a castle golden by spectrum has one of these graphs, and among them only `A_4 = P_4` has largest eigenvalue `φ`, since `2n − 2 = 5` has no solution. Every family occurs among castle graphs: `A_n` as the castles whose graph is a path, `D_{w+1}` as `(1, 2, 1, …, 1)` of width `w ≥ 3`, a cell with three neighbors and arms of 1, 1 and `w − 2` cells, and `E_6`, `E_7`, `E_8` as `(1, 1, 2, 1, 1)`, `(1, 1, 2, 1, 1, 1)` and `(1, 1, 2, 1, 1, 1, 1)`. Among the castles with at most 9 cells, 171 (102 up to mirror image) have spectral radius below 2, every radius among them is one of the Dynkin values, and exactly the six `P_4` castles have radius `φ`.[^2]

**No castle graph has spectral radius `δ_4` or larger.** A connected graph that is not regular has largest eigenvalue below its maximum degree (Brouwer and Haemers, Proposition 3.1.2), every cell has at most 4 neighbors, and the regular castle graphs have spectral radius 0, 1 or 2, so every castle graph has spectral radius below 4.[^1] `δ_4 = 2 + √5 = 4.236` and every larger `δ_a` exceed it. Bronze, `(3 + √13)/2 = 3.303`, does not, and no castle in the searches of [[bronze-castle-hunt](pages/bronze-castle-hunt.md)] has it as its spectral radius.

The signed transfer matrix of the castle count has no `δ_a` among its eigenvalues; its dominant eigenvalue at `h = 3` is 2, copper `σ_1^2` ([[castle-graph-spectral-radius](pages/castle-graph-spectral-radius.md)], section 1). The growth constants of castle families on [[castle-classification-growth](pages/castle-classification-growth.md)] are spectral radii of transfer matrices, not of castle graphs.

## Isospectral castles

**Predicate (on pairs).** Two castles with non-isomorphic castle graphs and the same spectrum. This is a predicate on pairs of castles.

Among every castle with at most 16 cells, mirror images removed ([[isospectral-castles](pages/isospectral-castles.md)]):[^2]

- The smallest **adjacency-isospectral** pair has 10 cells: `(1, 1, 1, 2, 3, 2)` and `(1, 1, 2, 2, 3, 1)`, with the spectrum `±2.583181, ±1.627286, ±1, ±0.824085, 0, 0`. Both graphs have 15 spanning trees.
- The smallest **Laplacian-isospectral** pair has 11 cells and is a pair of trees: `(1, 1, 1, 2, 1, 1, 2, 1, 1)` and `(1, 1, 3, 1, 1, 1, 2, 1)`.
- The smallest pair isospectral for **both** operators has 16 cells.

The adjacency spectrum has 105 groups of non-isomorphic castle graphs with the same spectrum up to 16 cells (2 at 10 cells, 10 at 12, 6 at 13, 18 at 14, 19 at 15, 50 at 16), and the Laplacian spectrum 17. Invariants of the sandpile separate more of them: the sink-model clock spectrum separates 62 of the 105 adjacency groups ([[sandcastle-clock](pages/sandcastle-clock.md)]), and the sink avalanche profile separates all 105 adjacency and all 17 Laplacian groups ([[sandpile-identity](pages/sandpile-identity.md)]).

## Ramanujan castles

For a connected graph `G` with adjacency eigenvalues `λ_n ≤ ⋯ ≤ λ_2 ≤ λ_1`, Hall, Puder and Sawin write `λ(G) = max(λ_2, −λ_n)` for the largest absolute value of a non-trivial eigenvalue and `ρ(G)` for the spectral radius of the universal covering tree of `G`, which is `2√(k − 1)` when `G` is `k`-regular. Greenberg's theorem gives `λ(G) ≥ ρ − o(1)` for the finite graphs covered by a fixed tree, and the graphs with `λ(G) ≤ ρ(G)` are the Ramanujan graphs. A bipartite graph has `λ_n = −λ_1`, and it is bipartite-Ramanujan when `λ_2, …, λ_{n−1}` lie in `[−ρ(G), ρ(G)]`.[^3]

A **Ramanujan castle** is a castle whose castle graph is bipartite-Ramanujan; by the symmetry of the spectrum, the condition is `λ_2 ≤ ρ(G)`. A castle graph with more than four cells is not regular, so `ρ(G)` is computed for its own covering tree. A finite tree is its own universal cover, so every tree castle is Ramanujan, and the condition restricts only castles with a `2 × 2` square.

[[ramanujan-castles](pages/ramanujan-castles.md)] computes `ρ(G)` by an edge-cavity method and checks every castle with at most 22 cells: every castle with at most 14 cells is Ramanujan, and the smallest non-Ramanujan castles have 15 cells. Among rectangles, the smallest that fails is the `2 × 14` rectangle `(14, 14)`, with 28 cells.

## Sparse-spectrum castles

The support of a castle's skyline discrete Fourier transform `ĉ_k` is the set of bins with `ĉ_k ≠ 0`. Heights are whole numbers, so the possible supports are exactly `{0}` together with a union of the classes `D_d = {k : gcd(k, w) = d}`, `d` a proper divisor of `w` ([[spectral-analysis](pages/spectral-analysis.md)] §3). A castle is **sparse-spectrum** when its support is bin 0 together with at most one class and is not all `w` bins. The members, sparsest first:

- **Rectangles**, support `{0}`.
- **Crenellated castles** at even width, whose heights alternate between two values ([[castle-classification-shape](pages/castle-classification-shape.md)], the value-pattern types), support `{0, w/2}`. At odd width a skyline that alternates between two values has every bin nonzero.
- **One class.** A support that is bin 0 plus the single class `D_{w/q}` has, besides bin 0, as many bins as there are numbers from 1 to `q` coprime to `q`. Exactly two such bins occur only for `q = 3, 4, 6`; the crenellated castles are the case `q = 2`.
- **Prime width.** At prime width the only class besides `{0}` is every other bin, so every castle of prime width that is not a rectangle has all `w` bins nonzero, and only the rectangles are sparse-spectrum.

The telephone tone castles of [[tone-castle-catalogue](pages/tone-castle-catalogue.md)] put 99.997% to 99.999% of their mean-removed energy in the bins of their tones, yet 30 of the 35 have every bin nonzero and the other five lose only a few classes, so none is a sparse-spectrum castle.

## Related Concepts

- [[castle-classification](pages/castle-classification.md)] - the hub of the castle classification: shape, spectral and growth types.
- [[castle-classification-shape](pages/castle-classification-shape.md)] - the shape types, predicates on the skyline.
- [[bronze-castle-hunt](pages/bronze-castle-hunt.md)] - the search for a castle bronze by spectrum: none in twelve boxes, about `7.1 × 10¹¹` skylines counted with overlaps.
- [[castle-classification-growth](pages/castle-classification-growth.md)] - the growth types of castle families.
- [[castle-graph](pages/castle-graph.md)] - the castle graph, its cycle rank, and the tree castles.
- [[castle-graph-spectral-radius](pages/castle-graph-spectral-radius.md)] - the spectral-radius census behind the golden, silver and `φ²` types, and the metallic means in the transfer-matrix spectra.
- [[isospectral-castles](pages/isospectral-castles.md)] - the isospectral pairs to 16 cells.
- [[castle-eigenvalues-by-example](pages/castle-eigenvalues-by-example.md)] - the adjacency eigenvalues of small castles worked by hand.
- [[spectral-analysis](pages/spectral-analysis.md)] - how each spectrum is computed: transfer matrices, the skyline DFT, the Laplacian, and the adjacency matrix with the universal cover.
- [[tree-castle-by-area](pages/tree-castle-by-area.md)] - the tree skylines and tree castles counted by area.
- [[ramanujan-castles](pages/ramanujan-castles.md)] - the edge-cavity computation of `ρ(G)` and the Ramanujan census.
- [[castle-eigenvalue-oeis-crosswalk](pages/castle-eigenvalue-oeis-crosswalk.md)] - the eigenvalues of the castle recurrences set against the OEIS, with `ρ_6 = 2ψ²`.

## Footnotes

[^1]: https://aeb.win.tue.nl/2WF02/spectra.pdf (A. E. Brouwer and W. H. Haemers, *Spectra of Graphs*, monograph version of February 1, 2011, read 2026-10-16) - Theorem 3.1.3 (Smith), p.34: "each connected graph with largest eigenvalue less than 2 is a subgraph of one of the above graphs, i.e., one of the graphs An = Pn, the path with n vertices (n ≥ 1), or" Dn (n ≥ 4), E6, E7, E8; p.35: "The eigenvalues of An are 2cos iπ/(n+1)", "of Dn are 0 and 2cos iπ/(2n−2)", "of E6 are 2cos iπ/12", "of E7 are 2cos iπ/18", "of E8 are 2cos iπ/30", "in all cases the largest eigenvalue is 2cos π/h"; Proposition 3.1.2, p.33: "If Γ is regular of valency k, then θ1 = k. Otherwise, we have kmin < k̄ < θ1 < kmax"; Proposition 3.4.1(ii), p.38: "If Γ is connected with largest eigenvalue θ1, then Γ is bipartite if and only if −θ1 is an eigenvalue of Γ".
[^2]: Verified by execution (Python 3.11 with NumPy, SymPy and networkx, 2026-10-16): `T_2`, `T_3`, `T_4`, `T_5` against `F_{w+2}`, `A001045(w+2)`, `A006130(w+1)`, `A006131(w+1)` for `w ≤ 7, 7, 6, 5`; every castle with at most 9 cells, with the Dynkin radii of `(1, 2, 1, 1, 1)` and the three `E` castles; the spectral-radius censuses of [[castle-graph-spectral-radius](pages/castle-graph-spectral-radius.md)]; the cospectral groups of every castle with at most 16 cells (33,150 up to mirror image), grouped by isomorphism class with networkx and by adjacency and Laplacian eigenvalues at 7 decimals; the 10-cell spectrum, the spanning-tree counts and the 11-cell Laplacian spectra.
[^3]: https://arxiv.org/pdf/1506.02335 (C. Hall, D. Puder and W. F. Sawin, *Ramanujan coverings of graphs*, read 2026-10-16) - §1.1 p.2: "Denote by λ(G) the largest absolute value of a non-trivial eigenvalue, namely λ(G) = max(λ2, −λn)", "Let ρ(G) be the spectral radius of the universal covering tree of G. For instance, if G is k-regular then ρ(G) = 2√(k−1)", and the bipartite case "λn−1, λn−2, ..., λ2 ∈ [−ρ(G), ρ(G)]. We call a bipartite graph with this property a bipartite-Ramanujan graph"; §2.1 p.12, Theorem 2.1 (Greenberg, in Cioabă's version): "λ(G) ≥ ρ − o_n(1)", and "graphs G satisfying λ(G) ≤ ρ(G) are considered to be optimal expanders. Following the terminology of [LPS88], they are called Ramanujan graphs."
