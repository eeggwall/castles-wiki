---
title: Castle classification - spectral types
category: Concepts
summary: A classification of individual castles by the spectrum of a graph derived from them. Tree castles, golden- and silver-spectrum castles, Smith's-theorem completeness of golden-spectrum at four cells, isospectral pairs, and the Ramanujan castle via Greenberg's universal-cover definition.
tags: [concept, castle, classification, taxonomy, spectral, adjacency-matrix, laplacian, ramanujan, smith-theorem, dynkin, tree-castle, isospectral, single-castle-predicate]
sources: [castle-classification, oeis-mining-pe502]
created: 2026-09-19
updated: 2026-09-28
---

# Castle classification - spectral types

## Scope: single-castle graph predicates

Spectral types are **single-castle predicates**, the same scope as the shape types on [[castle-classification-shape](pages/castle-classification-shape.md)] but from a different feature. Where a shape predicate reads the skyline `(c_1, …, c_w)`, a spectral predicate reads the polyomino graph `G_c` on [[castle-graph](pages/castle-graph.md)]: cells as vertices, orthogonal neighbours as edges. The invariant is the spectrum of an operator on this graph - adjacency matrix, combinatorial Laplacian, non-backtracking / Ihara operator - and the predicate says whether that spectrum has a particular shape.

This turns "castle shape" into "graph spectrum" and lets number-theoretic and spectral-graph-theoretic predicates cut across the shape axes. The methods-side companion is [[spectral-analysis](pages/spectral-analysis.md)]: this page catalogues the *predicates*; that page the *methods for computing spectra*. A computed spectral method plus a satisfied predicate is a named castle type.

**Two facts about castle graphs shape every type below.**

- **Bipartite.** Colour cells by `(i + j) mod 2`. Adjacency edges connect opposite colours, so the adjacency spectrum is symmetric about 0 (every eigenvalue `λ` has a mate `−λ`).
- **Almost never regular.** The leftmost cell of the top row has at most two neighbours, so a regular castle graph has degree at most 2 and is a path or a cycle. The only castle graphs that qualify are the single cell, the domino (`(1, 1)` or `(2)`, both `P_2`), and the `2 × 2` square `(2, 2)` = `C_4`; a longer path has ends of degree 1 and middle cells of degree 2, and a longer cycle would enclose a hole, which a bottom-aligned column-convex shape cannot. Every other castle graph is irregular.

The irregularity forces the Ramanujan definition to use Greenberg's universal-cover form rather than the regular-graph definition; for bipartite graphs `λ_n = −λ_1`, so the non-trivial spectrum excludes both `±λ_1`, and by the `±` symmetry its largest absolute value is `λ_2`.

## Tree castle

**Predicate.** The castle graph is a tree, i.e. has no cycles.

**Skyline equivalent.** No `2 × 2` filled block, i.e. no two horizontally adjacent columns both have height at least 2. It is a skyline predicate and a graph-theoretic one (`G_c` is a tree) at once.

**Counts.** By width, the transfer matrix `T_h(w + 2) = T_h(w + 1) + (h − 1) T_h(w)` gives growth constant `(1 + √(4h − 3)) / 2`, and the count is a named OEIS sequence at each height:

- `h = 2`: `T_2(w) = F_{w + 2}` (**Fibonacci**, A000045).
- `h = 3`: `T_3(w) = J_{w + 2}` (**Jacobsthal**, A001045).
- `h ≥ 4`: A006130, A006131, and so on.

Tree castles of height 2 are a **golden width growth castle** in the class-level terminology of [[castle-classification-growth](pages/castle-classification-growth.md)]. Counted by *area* ([[tree-castle-by-area](pages/tree-castle-by-area.md)]) tree castles grow at supergolden at `h = 2` (Narayana's cows A000930), golden at `h = 3` (A006498), and plastic-squared `ψ²` as `h → ∞` (A005251). The unrestricted counterpart, all castles of height `≤ h` by area, is the **n-nacci** family ([[bounded-height-castles-nacci](pages/bounded-height-castles-nacci.md)]); the tree constraint removes the `q²` term from the denominators.

Tree castles are also exactly the castles with a trivial sandpile group, in both the sink and the tide model ([[sandpile-census](pages/sandpile-census.md)]).

Full details on [[castle-graph](pages/castle-graph.md)] and [[tree-castle-by-area](pages/tree-castle-by-area.md)].

## Golden-spectrum, silver-spectrum, and `φ²`-spectrum castles

**Predicates.** A castle is a **golden-spectrum castle** if its adjacency spectral radius is `φ = (1 + √5) / 2`, a **silver-spectrum castle** if it is `1 + √2`, and a **`φ²`-spectrum castle** if it is `φ² = (3 + √5) / 2`.

**Census** over all castles with `w ≤ 6, h ≤ 6` and `w = 7, h ≤ 5` on [[castle-graph-spectral-radius](pages/castle-graph-spectral-radius.md)]:

- **Golden.** Six 4-cell castles: `(4)`, `(1, 3)`, `(3, 1)`, `(1, 1, 2)`, `(2, 1, 1)`, `(1, 1, 1, 1)`. All draw as the path graph `P_4`.
- **Silver.** The `3 × 2` rectangle in both orientations, `(2, 2, 2)` and `(3, 3)` (`P_2 × P_3`), and three non-rectangular mirror pairs: `(1, 2, 3, 1, 2, 3)`, `(2, 1, 6, 2, 1, 3)`, `(1, 1, 2, 4, 1, 3, 1)`. Each has `x² − 2x − 1` dividing its characteristic polynomial. The larger scan to width 10 on [[castle-graph-spectral-radius](pages/castle-graph-spectral-radius.md)] finds 36 silver mirror classes.
- **`φ²`.** `(4, 4)` and `(2, 2, 2, 2)` (both `P_2 × P_4`) and `(1, 3, 2, 3, 1)`.

**No castle of any size is golden-spectrum outside the list above.** By **Smith's theorem**, a connected graph with largest eigenvalue below 2 is one of the simply-laced Dynkin diagrams `A_n = P_n`, `D_n`, `E_6`, `E_7`, `E_8`.[^1] All five families occur as castle graphs: `A_n` as any path-shaped castle, `D_n` as `(1, 2, 1, 1, …, 1)` (a degree-3 cell at the base of a one-cell tower next to the left end), `E_6, E_7, E_8` as `(1, 1, 2, 1, 1)`, `(1, 1, 2, 1, 1, 1)`, `(1, 1, 2, 1, 1, 1, 1)`. Their spectral radii are `2 cos(π / (n + 1))`, `2 cos(π / (2n − 2))`, `2 cos(π / 12)`, `2 cos(π / 18)`, `2 cos(π / 30)`, and `φ = 2 cos(π / 5)` is hit only by `A_4 = P_4`. Verified by enumeration to 9 cells: 171 castles (102 up to mirror image) have spectral radius below 2, every radius among them is a Dynkin value, and exactly the six `P_4` castles have radius `φ`.

**Copper and higher metallic means are impossible for castle graphs.** Copper is `2 + √5 = 4.236` and every higher metallic mean exceeds 4. A castle graph has maximum degree 4 (each cell has at most 4 orthogonal neighbours), so its spectral radius is at most 4. Bronze `3.303` is open - absent up to the scanned size but not ruled out by any obstruction.

The metallic means reach individual castles only through their polyomino graphs. **Project Euler 502's own signed transfer matrix never has a metallic eigenvalue** ([[castle-graph-spectral-radius](pages/castle-graph-spectral-radius.md)]): its eigenvalues are twice the roots of an integer polynomial with leading coefficient 2, so never metallic. The class-level growth constants on [[castle-classification-growth](pages/castle-classification-growth.md)] and the single-castle adjacency spectral radii here come from different operators; `φ` appears in both.

## Isospectral castles

**Predicate (pair).** Two non-isomorphic castles have the same spectrum. This is a *pair* predicate, not a single-castle predicate: no castle is isospectral by itself.

**Populated** on [[isospectral-castles](pages/isospectral-castles.md)]:

- Smallest **adjacency-isospectral** pair: 10 cells, `(1, 1, 1, 2, 3, 2)` and `(1, 1, 2, 2, 3, 1)`. Both share the ten-eigenvalue spectrum `±2.583181, ±1.627286, ±1.000000, ±0.824085, 0, 0`.
- Smallest **Laplacian-isospectral** pair: 11 cells, two trees, `(1, 1, 1, 2, 1, 1, 2, 1, 1)` and `(1, 1, 3, 1, 1, 1, 2, 1)`.
- Smallest pair **isospectral for both operators**: 16 cells.

The search is exhaustive to 16 cells, with 50 adjacency groups already at 16. Isospectral pairs are common from 12 cells on, so the spectrum is an *invariant* rather than a *classifier* at that scale. Non-spectral invariants go further: the sink-model clock spectrum separates 62 of the 105 adjacency groups ([[sandcastle-clock](pages/sandcastle-clock.md)]), and the sink avalanche profile separates all 122 cospectral groups, with no two non-isomorphic castle graphs sharing one up to 13 cells ([[sandpile-identity](pages/sandpile-identity.md)]).

## Ramanujan castle

A castle is a **Ramanujan castle** iff every non-trivial eigenvalue of its adjacency matrix is bounded by `rho(T)`, the spectral radius of the universal covering tree - Greenberg's extension of the standard Ramanujan condition to irregular graphs. Bipartite castles reduce this to `lam_2 <= rho(T)`.

The full write-up - definition, the edge-cavity method for computing `rho(T)`, verification against known graphs, worked small examples, and the census to 22 cells, whose **smallest non-Ramanujan castles have 15 cells** (the smallest failing rectangle is `2 x 14`, `(14, 14)`, at 28 cells) - is on [[ramanujan-castles](pages/ramanujan-castles.md)].

Two shape-agnostic facts stay useful here:

- **Trees are Ramanujan.** A finite tree is its own universal cover, so the condition holds trivially. The predicate only bites on castles with a `2 x 2` block (positive cycle rank).
- **The regular-graph definition does not apply.** Castle graphs beyond four cells are never regular, so there is no `d` for the classical `|lam| <= 2*sqrt(d - 1)` condition; the universal-cover form is used instead.


## Defined types without members

These predicates have no computed members yet.

- **Sparse-spectrum castle** - a predicate on the skyline discrete Fourier transform (DFT) `ĉ_k`: the individual castle has `supp(ĉ) ⊆ S` for some fixed small set `S`. The Axis-7 **crenellated** type on [[castle-classification-shape](pages/castle-classification-shape.md)] is exactly the two-atom DFT-support case (energy at `k = w/2`). The general sparse-spectrum classification (which sparse-support sequences are valid castles) connects to compressed sensing and turnpike reconstruction.
- **Low-pass / high-pass castle** - a soft version of sparse-spectrum: the castle's DFT energy is concentrated in low-`k` modes (smooth mountain-shaped skyline) or high-`k` modes (jagged crenellation). A soft classifier by spectral concentration.
- **Ihara-Ramanujan castle** - the Ramanujan condition on the non-backtracking operator rather than the adjacency operator. The Ihara zeta is the graph analogue of the Selberg zeta of a hyperbolic surface.

## Open threads

1. **Ramanujan census beyond 22 cells.** [[ramanujan-castles](pages/ramanujan-castles.md)] finds every castle with at most 14 cells Ramanujan and the first failures at 15 cells; the pattern of failures beyond 22 cells is open.
2. **Bronze-spectrum castles.** Absent among 4.87 million castles on [[castle-graph-spectral-radius](pages/castle-graph-spectral-radius.md)]; open beyond the scanned size.
3. **Sparse-spectrum, low/high-pass, Ihara-Ramanujan.** The three types above; each needs its method on [[spectral-analysis](pages/spectral-analysis.md)] computed before it has members.
4. **Non-adjacency operators.** The Laplacian-cospectral census to 16 cells is on [[isospectral-castles](pages/isospectral-castles.md)] (17 groups), with the sandpile invariants of the same castles on [[sandpile-census](pages/sandpile-census.md)]; an Ihara census at small size would give the tree/golden/silver/`φ²` list its non-adjacency companions.

## Related Concepts

- [[castle-classification](pages/castle-classification.md)] - the hub, with the map of the three scopes.
- [[castle-classification-shape](pages/castle-classification-shape.md)] - the other single-castle scope: shape predicates on the skyline.
- [[castle-classification-growth](pages/castle-classification-growth.md)] - the class-level scope: growth constants of count sequences.
- [[castle-graph](pages/castle-graph.md)] - the polyomino graph the operators here act on.
- [[castle-graph-spectral-radius](pages/castle-graph-spectral-radius.md)] - the adjacency spectral-radius census (golden / silver / `φ²`), with the Smith / Dynkin argument.
- [[isospectral-castles](pages/isospectral-castles.md)] - the worked isospectral pairs (adjacency, Laplacian, both).
- [[castle-eigenvalues-by-example](pages/castle-eigenvalues-by-example.md)] - the pedagogy page that walks through small-castle adjacency eigenvalues by hand.
- [[spectral-analysis](pages/spectral-analysis.md)] - the methods hub whose five spectra feed these predicates.
- [[tree-castle-by-area](pages/tree-castle-by-area.md)] - the tree predicate's counting story.
- [[castle-eigenvalue-oeis-crosswalk](pages/castle-eigenvalue-oeis-crosswalk.md)] - the analytic side of the spectral-type framework: `ρ_6 = 2ψ²` and the metallic-means convergent crosswalk pinned quantitatively.

## Footnotes

[^1]: https://aeb.win.tue.nl/2WF02/spectra.pdf (Brouwer and Haemers, *Spectra of Graphs*) §3.1.1 Theorem 3.1.3 (Smith) - "each connected graph with largest eigenvalue less than 2 is a subgraph of one of the above graphs, i.e., one of the graphs `A_n = P_n`, the path with `n` vertices (`n ≥ 1`), or `D_n`, `E_6`, `E_7`, `E_8`". The graphs with largest eigenvalue exactly 2 are the extended Dynkin diagrams `Â_n`, `D̂_n`, `Ê_6`, `Ê_7`, `Ê_8`.
[^2]: https://en.wikipedia.org/wiki/Ramanujan_graph §"Extremality of Ramanujan graphs" - "the Alon-Boppana bound states that for every `d` and `ε > 0`, there exists `n` such that all `d`-regular graphs `G` with at least `n` vertices satisfy `λ(G) > 2√(d − 1) − ε`", where `λ(G)` is the largest absolute value of a non-trivial eigenvalue.
[^3]: https://arxiv.org/abs/1506.02335 (Hall, Puder, Sawin, *Ramanujan coverings of graphs*) §1 and §2.1 [synthesis] - `λ(G) = max(λ_2, −λ_n)` is the largest non-trivial eigenvalue in absolute value; `ρ(G)` is the spectral radius of the universal covering tree, equal to `2√(k − 1)` for `k`-regular `G`; Theorem 2.1 (Greenberg, in Cioabă's form) gives `λ(G) ≥ ρ − o(1)` for finite quotients of a fixed tree; "graphs `G` satisfying `λ(G) ≤ ρ(G)` are considered to be optimal expanders. Following the terminology of [LPS88], they are called Ramanujan graphs"; for bipartite `G` the condition is that `λ_2, …, λ_{n − 1}` lie in `[−ρ(G), ρ(G)]`.
