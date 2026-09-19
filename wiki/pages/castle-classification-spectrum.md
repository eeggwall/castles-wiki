---
title: Castle classification - spectral types
category: Concepts
summary: A classification of individual castles by the spectrum of a graph derived from them. Tree castles, golden- and silver-spectrum castles, Smith's-theorem completeness of golden-spectrum at four cells, isospectral pairs, and the Ramanujan castle via Greenberg's universal-cover definition.
tags: [concept, castle, classification, taxonomy, spectral, adjacency-matrix, laplacian, ramanujan, smith-theorem, dynkin, tree-castle, isospectral, single-castle-predicate]
sources: [castle-classification, oeis-mining-pe502]
created: 2026-09-19
updated: 2026-09-19
---

# Castle classification - spectral types

## Scope: single-castle graph predicates

Spectral types are **single-castle predicates**, the same scope as the shape types on [[castle-classification-shape](pages/castle-classification-shape.md)] but from a different feature. Where a shape predicate reads the skyline `(c_1, …, c_w)`, a spectral predicate reads the polyomino graph `G_c` on [[castle-graph](pages/castle-graph.md)]: cells as vertices, orthogonal neighbours as edges. The invariant is the spectrum of an operator on this graph - adjacency matrix, combinatorial Laplacian, non-backtracking / Ihara operator - and the predicate says whether that spectrum has a particular shape.

This turns "castle shape" into "graph spectrum" and lets number-theoretic and spectral-graph-theoretic predicates cut across the shape axes. The methods-side companion is [[spectral-analysis](pages/spectral-analysis.md)]: this page catalogues the *predicates*; that page the *methods for computing spectra*. A completed spectral method plus a satisfied predicate is a named castle type; the two evolve together.

**Two facts about castle graphs shape every type below.**

- **Bipartite.** Colour cells by `(i + j) mod 2`. Adjacency edges connect opposite colours, so the adjacency spectrum is symmetric about 0 (every eigenvalue `λ` has a mate `−λ`).
- **Almost never regular.** The leftmost cell of the top row has at most two neighbours, so a regular castle graph has degree at most 2 and is a path or a cycle. The only castle graphs that qualify are the single cell, the domino `(1, 1)` = `P_2`, the three-cell path `(1, 1, 1)` = `P_3`, and the `2 × 2` square `(2, 2)` = `C_4`; a longer cycle would enclose a hole, which a bottom-aligned column-convex shape cannot. Every castle graph with more than four cells is irregular, with corner cells of degree 2, edge cells of degree 3, and interior cells of degree 4.

The irregularity forces the Ramanujan definition to use Greenberg's universal-cover form rather than the regular-graph definition; the bipartite structure means the adjacency spectrum's second-largest eigenvalue in absolute value is really `max(λ_2, |λ_n|)`, and for bipartite graphs `λ_n = −λ_1` always, so the "non-trivial" spectrum is what sits between `−λ_1` and `λ_1` strictly.

## Tree castle

**Predicate.** The castle graph is a tree, i.e. has no cycles.

**Skyline equivalent.** No `2 × 2` filled block, i.e. no two horizontally adjacent columns both have height at least 2. This is the simplest spectral type: single-castle, structural (a skyline predicate), and graph-theoretic (`G_c` is a tree) simultaneously.

**Counts.** By width, the transfer matrix `T_h(w + 2) = T_h(w + 1) + (h − 1) T_h(w)` gives growth constant `(1 + √(4h − 3)) / 2`, and the count hits named OEIS sequences at every height:

- `h = 2`: `T_2(w) = F_{w + 2}` (**Fibonacci**, A000045).
- `h = 3`: `T_3(w) = J_{w + 2}` (**Jacobsthal**, A001045).
- `h ≥ 4`: A006130, A006131, and so on.

Tree castles of height 2 are a **golden width growth castle** in the class-level terminology of [[castle-classification-growth](pages/castle-classification-growth.md)] - a rung on the metallic ladder without leaving spectral territory. Counted by *area* ([[tree-castle-by-area](pages/tree-castle-by-area.md)]) tree castles instead realize the non-metallic **cubic-Pisot** growth constants - supergolden at `h = 2` (Narayana's cows A000930), plastic-squared `ψ²` at `h → ∞` (A005251). The unrestricted (non-tree) counterpart, all castles of height `≤ h` by area, is the **n-nacci** family - the tree constraint is exactly what turns the n-nacci constants into the term-skipping cubic-Pisot ones.

Full details on [[castle-graph](pages/castle-graph.md)] and [[tree-castle-by-area](pages/tree-castle-by-area.md)].

## Golden-spectrum, silver-spectrum, and `φ²`-spectrum castles

**Predicates.** A castle is a **golden-spectrum castle** if its adjacency spectral radius is `φ = (1 + √5) / 2`, a **silver-spectrum castle** if it is `1 + √2`, and a **`φ²`-spectrum castle** if it is `φ² = (3 + √5) / 2`.

**Census** over all castles with `w ≤ 6, h ≤ 6` and `w = 7, h ≤ 5` on [[castle-graph-spectral-radius](pages/castle-graph-spectral-radius.md)]:

- **Golden.** Six 4-cell castles: `(4)`, `(1, 3)`, `(3, 1)`, `(1, 1, 2)`, `(2, 1, 1)`, `(1, 1, 1, 1)`. All draw as the path graph `P_4`.
- **Silver.** The `3 × 2` rectangle `(2, 2, 2)` (`P_2 × P_3`) and three non-rectangular mirror pairs: `(1, 2, 3, 1, 2, 3)`, `(2, 1, 6, 2, 1, 3)`, `(1, 1, 2, 4, 1, 3, 1)`. Each has `x² − 2x − 1` dividing its characteristic polynomial exactly.
- **`φ²`.** `(4, 4)` (`P_2 × P_4`) and `(1, 3, 2, 3, 1)`.

**No castle of any size is golden-spectrum outside the list above.** By **Smith's theorem**, a connected graph with largest eigenvalue below 2 is one of the simply-laced Dynkin diagrams `A_n = P_n`, `D_n`, `E_6`, `E_7`, `E_8`.[^1] All five families occur as castle graphs: `A_n` as any path-shaped castle, `D_n` as `(1, 2, 1, 1, …, 1)` (a degree-3 cell at the base of a one-cell tower next to the left end), `E_6, E_7, E_8` as `(1, 1, 2, 1, 1)`, `(1, 1, 2, 1, 1, 1)`, `(1, 1, 2, 1, 1, 1, 1)`. Their spectral radii are `2 cos(π / (n + 1))`, `2 cos(π / (2n − 2))`, `2 cos(π / 12)`, `2 cos(π / 18)`, `2 cos(π / 30)`, and `φ = 2 cos(π / 5)` is hit only by `A_4 = P_4`. Verified by enumeration to 9 cells: 171 castles have spectral radius below 2, every radius among them is a Dynkin value, and exactly the six `P_4` castles have radius `φ`.

**Metallic means beyond copper are impossible for castle graphs.** Copper is `2 + √5 = 4.236` and every higher metallic mean exceeds 4. A castle graph has maximum degree 4 (each cell has at most 4 orthogonal neighbours), so its spectral radius is bounded above by 4. Bronze `3.303` is open - absent up to the scanned size but not ruled out by any obstruction.

The metallic means reach individual castles only through their polyomino graphs. **Project Euler 502's own signed transfer matrix never has a metallic eigenvalue** ([[castle-graph-spectral-radius](pages/castle-graph-spectral-radius.md)]): its eigenvalues are twice algebraic units and never metallic. The class-level growth constants on [[castle-classification-growth](pages/castle-classification-growth.md)] and the single-castle adjacency spectral radii here are different operators; when they happen to produce the same eigenvalue (`φ` appears in both settings), it is a structural coincidence worth investigating case by case.

## Isospectral castles

**Predicate (pair).** Two non-isomorphic castles have the same spectrum. This is a *pair* predicate, not a single-castle predicate: no castle is isospectral by itself.

**Populated** on [[isospectral-castles](pages/isospectral-castles.md)]:

- Smallest **adjacency-isospectral** pair: 10 cells, `(1, 1, 1, 2, 3, 2)` and `(1, 1, 2, 2, 3, 1)`. Both share the ten-eigenvalue spectrum `±2.583181, ±1.627286, ±1.000000, ±0.824085, 0, 0`.
- Smallest **Laplacian-isospectral** pair: 11 cells, two trees, `(1, 1, 1, 2, 1, 1, 2, 1, 1)` and `(1, 1, 3, 1, 1, 1, 2, 1)`.
- Smallest pair **isospectral for both operators**: 16 cells.

The search is exhaustive to 16 cells, with 50 adjacency groups already at 16. Isospectral pairs are common from 12 cells on, so the spectrum is an *invariant* rather than a *classifier* at that scale.

## Ramanujan castle

**The regular-graph definition has no content on castles.** A Ramanujan graph in the usual (regular) sense has every eigenvalue other than `±d` satisfying `|λ| ≤ 2√(d − 1)`. Castle graphs beyond four cells are never regular, so `d` is not a single number, and for a connected irregular graph the spectral radius `λ_1` is strictly below `d_max`. Excluding `λ = ±d_max` excludes nothing, and the bound would be tested against `λ_1` itself.

The **Alon-Boppana theorem** is what motivates the definition: for large `d`-regular graphs the largest **non-trivial** eigenvalue `λ(G) = max(λ_2, |λ_n|)` is at least `2√(d − 1) − ε`.[^2] "Ramanujan" then means "as small as this bound allows".

**The well-posed definition for irregular graphs is Greenberg's, via the universal cover.**[^3] Let `T` be the universal covering tree of `G_c` and `ρ(T)` its spectral radius (`2√(d − 1)` when `G_c` is `d`-regular). Greenberg's theorem says finite graphs covered by `T` have `λ(G) ≥ ρ − o(1)`, and `G_c` is **Ramanujan** iff every eigenvalue other than `±λ_1` satisfies `|λ| ≤ ρ(T)`. Castle graphs are bipartite, so this is the bipartite-Ramanujan condition `λ_2 ≤ ρ(T)`.

**Three consequences.**

- **The threshold is castle-dependent.** `ρ(T)` must be computed from the castle's own covering tree. A tree of maximum degree `Δ` has spectral radius at most `2√(Δ − 1)`, so `λ_2 ≤ 2√(d_max − 1)` is a necessary condition only: `2√3 ≈ 3.464` for castles with an interior cell, `2√2 ≈ 2.828` for castles whose every cell is on the boundary.
- **Tree castles are Ramanujan for free.** A finite tree is its own universal cover, so `ρ(T) = λ_1 ≥ λ_2` and the condition holds. The Ramanujan predicate only bites on castles with at least one `2 × 2` block, i.e. positive cycle rank.
- **No census exists yet.** The first non-trivial cases are the boxcastle (spectrum `2 cos(iπ / (w + 1)) + 2 cos(jπ / (h + 1))`, so `λ_2` is explicit and only `ρ(T)` needs computing) and the crenellated type ([[castle-classification-shape](pages/castle-classification-shape.md)] Axis 7), whose repeated local structure makes its covering tree tractable.

The Ihara / non-backtracking version transfers the same condition to the spectrum of the non-backtracking operator, which is the form that connects to the Ihara-zeta seminar on `IDEAS.md`; see [[spectral-analysis](pages/spectral-analysis.md)] §5.

## Sketched additional spectral types

Not yet populated, but the following predicates would sit here when they land.

- **Sparse-spectrum castle** - a predicate on the skyline discrete Fourier transform (DFT) `ĉ_k`: the individual castle has `supp(ĉ) ⊆ S` for some fixed small set `S`. The Axis-7 **crenellated** type on [[castle-classification-shape](pages/castle-classification-shape.md)] is exactly the two-atom DFT-support case (energy at `k = w/2`). The general sparse-spectrum classification (which sparse-support sequences are valid castles?) hooks into compressed sensing and turnpike reconstruction. See the S-Division `Skyline DFT - individual-castle signatures` thread.
- **Low-pass / high-pass castle** - a soft version of sparse-spectrum: the castle's DFT energy is concentrated in low-`k` modes (smooth mountain-shaped skyline) or high-`k` modes (jagged crenellation). Not a hard predicate but a natural spectral-concentration classifier.
- **Ihara-Ramanujan castle** - the Ramanujan condition on the non-backtracking operator rather than the adjacency operator. Arithmetic-combinatorial invariant analogous to Selberg zeta for hyperbolic surfaces. Longer-horizon; see the S-Division `Ramanujan castles / Ihara zeta` thread.

## Open threads

1. **Ramanujan census.** Compute `ρ(T)` for the universal covers of small castles with a `2 × 2` block and run the predicate; boxcastles and crenellated castles first.
2. **Bronze-spectrum castles.** Absent among 4.87 million castles on [[castle-graph-spectral-radius](pages/castle-graph-spectral-radius.md)]; open beyond the scanned size.
3. **Sparse-spectrum, low/high-pass, Ihara-Ramanujan.** The three sketched types; S-Division seminar targets on `IDEAS.md`. Each waits for its method on [[spectral-analysis](pages/spectral-analysis.md)] to land before it can be populated with worked members.
4. **Non-adjacency operators.** The Laplacian isospectral pair at 11 cells is one worked example; a full Laplacian census (or a Ihara-adjacency census) at small size would give the tree/golden/silver/`φ²` list its non-adjacency companions.

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

## Footnotes

[^1]: https://aeb.win.tue.nl/2WF02/spectra.pdf (Brouwer and Haemers, *Spectra of Graphs*) §3.1.1 Theorem 3.1.3 (Smith) - "each connected graph with largest eigenvalue less than 2 is a subgraph of one of the above graphs, i.e., one of the graphs `A_n = P_n`, the path with `n` vertices (`n ≥ 1`), or `D_n`, `E_6`, `E_7`, `E_8`". The graphs with largest eigenvalue exactly 2 are the extended Dynkin diagrams `Â_n`, `D̂_n`, `Ê_6`, `Ê_7`, `Ê_8`.
[^2]: https://en.wikipedia.org/wiki/Ramanujan_graph §"Extremality of Ramanujan graphs" - "the Alon-Boppana bound states that for every `d` and `ε > 0`, there exists `n` such that all `d`-regular graphs `G` with at least `n` vertices satisfy `λ(G) > 2√(d − 1) − ε`", where `λ(G)` is the largest absolute value of a non-trivial eigenvalue.
[^3]: https://arxiv.org/abs/1506.02335 (Hall, Puder, Sawin, *Ramanujan coverings of graphs*) §1 and §2.1 [synthesis] - `λ(G) = max(λ_2, −λ_n)` is the largest non-trivial eigenvalue in absolute value; `ρ(G)` is the spectral radius of the universal covering tree, equal to `2√(k − 1)` for `k`-regular `G`; Theorem 2.1 (Greenberg, in Cioabă's form) gives `λ(G) ≥ ρ − o(1)` for finite quotients of a fixed tree; "graphs `G` satisfying `λ(G) ≤ ρ(G)` are considered to be optimal expanders. Following the terminology of [LPS88], they are called Ramanujan graphs"; for bipartite `G` the condition is that `λ_2, …, λ_{n − 1}` lie in `[−ρ(G), ρ(G)]`.
