---
title: Castle classification
category: Concepts
summary: A classification framework for castle sub-families. Axes 1-7 are structural skyline predicates on individual castles; Axis 8 is a growth-type meta-classification on castle *classes* (named as "<metal> <axis> growth castle"); Axis 9 is a spectral-type predicate on individual castles' polyomino graphs (Ramanujan castle, golden- and silver-spectrum castles with computed members, others sketched). Catalogs 42 structural types plus the Axis-8 golden and silver width growth families and the Axis-9 Ramanujan type.
tags: [concept, castle, classification, taxonomy, skyline, spectral, ramanujan]
sources: [castle-classification]
created: 2026-09-15
updated: 2026-09-16
---

# Castle classification

## The framing

A **castle** is a valid stacked-block configuration on a `w × h` grid ([[castle-polyomino](pages/castle-polyomino.md)]), and is determined by its **skyline** — the sequence of column heights[^1]

```
c_1, c_2, …, c_w      with 1 ≤ c_i ≤ h and max_i c_i = h.
```

Every castle is automatically **column-convex** (each column is one contiguous vertical run) and **bottom-aligned** (row 1 is a full-width block). So a "**castle type**" is a **further restriction on the skyline** — a predicate on `(c_1, …, c_w)`. PE 502's even-block parity constraint is orthogonal to typing: each type is defined without reference to parity, and the even-block projector `(A ± P)/2` ([[castle-sign](pages/castle-sign.md)]) is applied on top when needed.[^1]

## Upstream source

The type catalog is hydrated from `charlesreid1.com/wiki/Project_Euler/502/Castle_Types` (fetched 2026-09-15; wikitext cached at `raw/castle-types.wiki`). That page defines 42 types — **7 base types** drawn from the polyomino literature (column-convex, unimodal, directed, parallelogram, Ferrers, staircase, m-disparate)[^2] and **35 proposed types** aggregated from adjacent literature or newly defined (convex/row-convex, reverse Ferrers, k-modal, m-smooth, Dyck-path, Motzkin-path, palindromic, self-conjugate, rainbow, hook, crenellated, moated, twin-peak, single-summit, single-valley, and so on).[^3] The upstream page states the types as skyline predicates only; this page organizes them into structural axes, ties each type to the wiki thread that already touches it, and marks which have counts, which are candidates, and which are open.

## What "classification" gives you

Three questions attach to every type:

1. **Is it counted?** Does the wiki already have a count (exact formula, generating function, or algorithm) for the type?
2. **What is its count's shape?** Growth constant, C-finite / algebraic / transcendental character, OEIS identification if any.
3. **How does it interact with the parity clause?** Does the parity-projected version have the same shape, or is parity locked out by the type's structure?

Every open (2) is a seminar topic; every open (3) is a research thread. The classification here does not answer these questions for the 42 types — it names them and marks which ones the wiki has answered, which are candidates, and which are genuinely open.

## The base 7 types and their wiki homes

The base types are all standard polyomino / composition families. Each corresponds to an existing wiki thread:[^2]

| Type | Definition (skyline predicate) | Wiki home | Count status |
|---|---|---|---|
| **Column-convex** | (automatic for castles) | [[column-convex-polyomino](pages/column-convex-polyomino.md)] | matches all castles; `A(w,h) = h^w − (h−1)^w` |
| **Unimodal** | `c_1 ≤ … ≤ c_p ≥ … ≥ c_w` | [[convex-castle](pages/convex-castle.md)] | `C(2h+w−3, w−1)` via [[convex-castle-binomial-identity](pages/convex-castle-binomial-identity.md)] |
| **Ferrers** | `c_1 ≥ c_2 ≥ … ≥ c_w` (weakly decreasing) | [[polyominoes](pages/polyominoes.md)], [[column-convex-polygon-enumeration](pages/column-convex-polygon-enumeration.md)] | classical; by area = partition GF; q-Catalan / q-Bessel refinement |
| **Staircase** | Ferrers with all `c_i` distinct | [[polyominoes](pages/polyominoes.md)] | classical (distinct-parts partitions) |
| **Parallelogram** | anti-diagonal sections connected | [[column-convex-polygon-enumeration](pages/column-convex-polygon-enumeration.md)] | classical (Bousquet-Mélou) |
| **Directed** | every cell reachable from `(1,1)` by east/north | [[polyominoes](pages/polyominoes.md)] | classical (directed polyominoes) |
| **m-disparate** | `|c_{i+1} − c_i| ≥ m` for all `i` | **not yet on the wiki** | open |

The first 6 rows tie the castle taxonomy directly to the polyomino literature. **m-disparate** is the one base type without an existing wiki thread — a natural target for the "gap-rule variations" idea on `IDEAS.md`.

## The 35 proposed types, grouped by structural axis

The proposed types cluster into a handful of structural axes, some of which the wiki has counts for.

### Axis 1: Convexity / modality

Types 1–6 and 30–31 restrict the shape of the skyline's local extrema:

| Type | Predicate | Wiki tie |
|---|---|---|
| **Convex (row-convex)** | every row is one contiguous run | equals unimodal for castles ([[convex-castle](pages/convex-castle.md)]); front/middle/back U/R/D form on [[project-euler-502-representations](pages/project-euler-502-representations.md)] |
| **Reverse Ferrers** | `c_1 ≤ … ≤ c_w` (weakly increasing) | Ferrers's mirror; same count by symmetry |
| **Strictly unimodal** | strict rise, one peak, strict fall | strengthens unimodal; count is a sub-count of [[convex-castle](pages/convex-castle.md)] |
| **Bimodal** | exactly two local maxima | *open* — natural refinement, no wiki count yet |
| **k-modal** | at most `k` local maxima | *open* — unimodal is `k=1`; parameterized family |
| **Anti-unimodal (V-shaped)** | weakly decrease then weakly increase | the "valley" family; on [[castle-by-area](pages/castle-by-area.md)] as valley castles, area-OEIS A332578; the [[convex-castle-binomial-identity](pages/convex-castle-binomial-identity.md)] valley bijection is an open thread |
| **Convex-skyline** | `c_{i−1} − 2c_i + c_{i+1} ≥ 0` (discrete convex) | *open* — a stronger sub-family of anti-unimodal |
| **Concave-skyline** | `c_{i−1} − 2c_i + c_{i+1} ≤ 0` (discrete concave) | *open* — a stronger sub-family of unimodal |

**Where the wiki already has counts:** unimodal and (by symmetry) reverse Ferrers, via the [[convex-castle-binomial-identity](pages/convex-castle-binomial-identity.md)]; anti-unimodal (valley) by area on [[castle-by-area](pages/castle-by-area.md)]. **Where the wiki has candidate counts but not proofs:** the convex⟺valley bijection.

### Axis 2: Rate of change (Lipschitz)

Types 7, 8, 9 and the base m-disparate:

| Type | Predicate | Wiki tie |
|---|---|---|
| **Plateau-free** | `c_i ≠ c_{i+1}` for all `i` | *open* — a Lipschitz lower bound on differences |
| **m-smooth (Lipschitz)** | `|c_{i+1} − c_i| ≤ m` | matches **Motzkin-path** at `m = 1`; the tower-word framing on [[tower-word-continued-fraction](pages/tower-word-continued-fraction.md)] |
| **Zigzag** | differences alternate in sign | *open* — a strong plateau-free variant |
| **m-disparate** | `|c_{i+1} − c_i| ≥ m` | *open* — the "no small step" restriction |

**Where the wiki already has counts:** 1-smooth castles collapse to the Motzkin-path family ([[motzkin-numbers](pages/motzkin-numbers.md)], [[tower-word-continued-fraction](pages/tower-word-continued-fraction.md)]); the tower word A004149 is the 1-smooth-with-no-UD-no-DU refinement. **Open:** the full m-smooth family for `m ≥ 2`, and m-disparate for any `m`.

### Axis 3: Path-like restrictions

Types 13 and 14 identify the skyline with a classical lattice path:

| Type | Predicate | Wiki tie |
|---|---|---|
| **Dyck-path** | `c_1 = c_w = 1`, `|c_{i+1} − c_i| = 1`, all `c_i ≥ 1` | [[dyck-words](pages/dyck-words.md)]; [[catalan-numbers](pages/catalan-numbers.md)] count |
| **Motzkin-path** | `|c_{i+1} − c_i| ≤ 1` (Dyck-path with flat steps allowed) | [[motzkin-numbers](pages/motzkin-numbers.md)]; [[tower-word-continued-fraction](pages/tower-word-continued-fraction.md)] is the run-constrained sub-family |

**Where the wiki already has counts:** both, from the classical lattice-path literature. The Dyck-path castle is Catalan; the Motzkin-path castle is Motzkin (with the run constraint further reducing to A004149).

### Axis 4: Symmetry

Types 11, 12, 21 impose symmetry on the skyline:

| Type | Predicate | Wiki tie |
|---|---|---|
| **Palindromic** | `c_i = c_{w+1−i}` | *open* — a natural symmetry restriction |
| **Centrally symmetric** | `c_i + c_{w+1−i} = h + 1` (180° rotation inside bounding box) | *open* |
| **Self-conjugate** | `c_i = #{j : c_j ≥ i}` (transpose invariance) | *open* — classical partition-conjugation, would require `w = h` |

**Open across the board.** The self-conjugate type is particularly interesting because it forces `w = h` and interacts with the wiki's Fibonacci-in-prime-castle count `2^{n−1} − F_{n−1}` on [[castle-by-area](pages/castle-by-area.md)].

### Axis 5: Value / extremum constraints

Types 15, 16, 24, 26, 27, 33, 35, and a few others restrict where extremes occur:

| Type | Predicate | Wiki tie |
|---|---|---|
| **Flat-top** | `h` attained in ≥ 2 consecutive columns | *open* |
| **Single-summit** | `h` attained in exactly one column | *open* — matches strictly-unimodal at the peak |
| **Twin-peak** | `h` attained in exactly two columns | *open* |
| **Single-valley** | height 1 attained in exactly one column | *open* — dual to single-summit |
| **Rainbow** | `w = h`, heights a permutation of `{1, …, h}` | *open* — direct link to permutation-based combinatorics ([[permutation-cycle-castle-analogy](pages/permutation-cycle-castle-analogy.md)]) |
| **Boxcastle** | `c_i = h` for all `i` | trivial: count is `1` |
| **Hook** | `c_1 = h`, `c_i = 1` for `i ≥ 2` | Young-diagram hook; count is `w` (choice of tower position × 1) after symmetry |

**Rainbow castles are the natural bridge to [[permutation-cycle-castle-analogy](pages/permutation-cycle-castle-analogy.md)]:** they are, by definition, in bijection with permutations of `{1, …, h}` — so the wiki's cycle-count / Foata / streak triad ([[castles-as-upgraded-cycle-count](pages/castles-as-upgraded-cycle-count.md)]) applies to them directly, not by upgrade. Rainbow castles are the "n! degenerate case" of the castle machinery.

### Axis 6: Parity and area

Types 10, 17, 18, 32:

| Type | Predicate | Wiki tie |
|---|---|---|
| **Alternating parity** | `c_i` alternates odd/even | *open* |
| **Even-area** | `∑ c_i ≡ 0 (mod 2)` | [[castle-by-area](pages/castle-by-area.md)] parity split |
| **Even-peak** | number of local maxima is even | [[castle-sign](pages/castle-sign.md)] sibling; peak count is on [[castle-foata-transform](pages/castle-foata-transform.md)] |
| **Triangular-area** | `∑ c_i = n(n+1)/2` | *open* — a curiosity restriction |

**The even-peak type is worth flagging.** The [[castle-sign](pages/castle-sign.md)] is `(−1)^blocks`, not `(−1)^peaks`; even-peak is a different parity constraint that the wiki hasn't investigated. The [[castle-foata-transform](pages/castle-foata-transform.md)] identifies `#peaks = #records`, so even-peak is "even-records" — a permutation-statistic parity condition.

### Axis 7: Value patterns

Types 19, 20, 22, 23, 25, 28, 29, 34:

| Type | Predicate | Wiki tie |
|---|---|---|
| **Equal-block** | all maximal horizontal blocks have the same length | *open* — heavy structure |
| **Two-level** | exactly two distinct height values | contains [[pell-castle-strip](pages/pell-castle-strip.md)] with `h = 2` |
| **Crenellated** | heights alternate `{a, h}` (battlements) | *open* — very restricted two-level |
| **Moated** | `c_1 = c_w = 1`, all interior `≥ 2` | *open* |
| **Fence-post** | `c_i = 1` for all even `i` | *open* |
| **Linear** | `c_i = a + (i−1)d` (arithmetic progression) | *open* — count is `O(h)` or `O(wh)` depending on parameters |
| **Prime-top** | `h` is prime | trivial family: all castles with prime `h` |
| **Integer-mean** | `w | ∑ c_i` | *open* |

## Axis 8: Growth-type meta-classification

Axes 1-7 above are all **predicates on individual castles**: given `(c_1, …, c_w)`, is this castle unimodal? Ferrers? palindromic? Axis 8 is different: it is a **predicate on castle classes** — a property of a *sequence of counts*, not of a single castle. This makes it a **meta-classification**: golden growth castle status is not a shape a given castle has, it is a growth-rate a given class has.

The framework is the [[metallic-means](pages/metallic-means.md)] family `δ_a = (a + √(a² + 4))/2` for `a = 1, 2, 3, …` — golden (`φ`), silver (`1+√2`), bronze (`(3+√13)/2`), copper, nickel, and so on. From the [[pell-castle-strip](pages/pell-castle-strip.md)] mnemonic, a castle-strip family with denominator `1 − w_1·x − w_2·x²` grows at `(w_1 + √(w_1² + 4·w_2))/2`, which is a metallic mean iff `w_2 = 1`. The metallic-mean ladder is thus a natural axis of count growth-constants along which real castle classes fall.

### The naming convention

A castle class is a **"`<metal>` `<axis>` growth castle"** iff its count sequence, graded by the chosen size axis, grows at rate `δ_a` (the metallic mean for that metal). The three parts:

- **`<metal>`** — golden (`a=1`, growth `φ`), silver (`a=2`, growth `1+√2`), bronze (`a=3`, growth `(3+√13)/2`), copper (`a=4`, growth `2+√5 = φ³`), nickel (`a=5`, growth `(5+√29)/2`), and so on. See [[metallic-means](pages/metallic-means.md)].
- **`<axis>`** — the size parameter being graded:
  - **width** — the sequence is graded by width `w` (height `h` fixed or bounded)
  - **vertical** — the sequence is graded by height `h` (width `w` fixed or bounded)
  - **area** — the sequence is graded by total area `∑ c_i`
  - **block** — the sequence is graded by block count
- **"growth castle"** — the noun, marking this as an Axis-8 meta-type.

**The axis is always stated explicitly.** A silver width growth castle and a silver vertical growth castle are different claims; there is no default axis. The full form ("silver width growth castle") is used throughout — no shorthand like "silver castle" — to keep meta-types unambiguous.

### Golden width growth castle — the `δ_1 = φ` axis-1 family

A class whose width-graded count sequence has growth constant `φ = (1+√5)/2`, equivalently whose width GF has dominant singularity at `1/φ = φ − 1`. Known members:

- **The {0, 1}-skyline castle strip** — a castle with `c_i ∈ {0, 1}` above the base and rule-3 mandatory gap. Count sequence: Fibonacci `F_{w+2}`, generating function `1/(1 − x − x²)`. This is the `w_1 = 1, w_2 = 1` case of the general `1 − w_1·x − w_2·x²` strip mnemonic.
- **The prime-castle count** `2^{n−1} − F_{n−1}` on [[castle-by-area](pages/castle-by-area.md)] — Fibonacci-flavored in `Q(√5)`, so its Fibonacci component makes it a golden growth castle by area (not width — the area grading is what puts Fibonacci in this sequence).

### Silver width growth castle — the `δ_2 = 1 + √2` axis-2 family

A class whose width-graded count sequence has growth constant `1 + √2 ≈ 2.4142`. Known members:

- **The [[pell-castle-strip](pages/pell-castle-strip.md)]** — the canonical instance. Count sequence: Pell numbers shifted `P_{n+1}` (OEIS A000129), generating function `1/(1 − 2x − x²)`. Height ≤ 2, two states per column, rule-3 mandatory gap. This is the `w_1 = 2, w_2 = 1` case.
- **The tower word** ([[tower-word-continued-fraction](pages/tower-word-continued-fraction.md)]) — count sequence A004149, algebraic (not rational) generating function with singularity at `√2 − 1`, so growth `1/(√2 − 1) = √2 + 1`. Structurally very different from the Pell strip (context-free rather than regular), but the same growth constant — so both are silver width growth castles.

**Two structurally different classes, one growth type.** This is the meta-classification working: silver width growth castle is a property that holds across differently-shaped families, uniting them by their asymptotic count behavior rather than by their skyline predicates.

### Bronze / copper / nickel width growth castles — candidates

- **Bronze width growth castle** (`δ_3 = (3+√13)/2 ≈ 3.303`) — the `w_1 = 3, w_2 = 1` strip case is a candidate: three states per column above the base plus rule-3 gap, count sequence `1, 3, 10, 33, 109, 360, …`, growth `(3+√13)/2`. Whether any physically-natural castle class (height ≤ 3 tower under a specific same-row-adjacency rule?) instantiates this is open.
- **Copper width growth castle** (`δ_4 = 2 + √5 = φ³`) — because `δ_4 = φ³`, any copper width growth castle lives in `Q(√5)` and is a "Fibonacci-decimated" family; its count sequence would be `F_{3n}/2` for the strip case. Candidates open.
- **Nickel and beyond** — genuinely open.

### Vertical / area / block growth castles

The **vertical growth axis** grades by height (`h` varying, `w` fixed). No member is known. The natural candidate, the k-direction signed count `P(k, L)` at fixed `L`, is not one: its characteristic polynomial is `(x+1)^L (x−1)^{L−2}` ([[convergents-oeis-crosswalk](pages/convergents-oeis-crosswalk.md)]), so it is a quasi-polynomial in `k` with no exponential growth at all. The count `F(w, h)` in `h` is likewise a quasi-polynomial (annihilated by `(x²−1)^w`). A vertical growth castle with a metallic constant would have to come from a rule modification.

The **area growth axis** grades by `∑ c_i`. Instances: the prime-castle-by-area count `2^{n−1} − F_{n−1}` is golden area growth castle (Fibonacci-dominated); [[weakly-unimodal-composition](pages/weakly-unimodal-composition.md)] (`A001523`) has area growth constant that is *not* a metallic mean (transcendental, from the partition-function saddle-point analysis) — so weakly-unimodal castles by area are *not* a `δ_a`-castle for any `a`, useful negative example.

The **block growth axis** grades by block count. [[tower-narayana-polynomial](pages/tower-narayana-polynomial.md)] gives the block-count generating function structure; growth-constant analysis pending.

### What the meta-classification enables

**Cross-type theorems become stateable.** The interesting move Axis 8 licenses is statements of the form *"every class of type X is also of type Y"* where X is a structural (Axis 1-7) type and Y is a growth-type. Some concrete instances:

- **Every {0, 1}-skyline strip is a golden width growth castle.** (Immediate — it's the Fibonacci strip.)
- **Every silver width growth castle has a dominant eigenvalue in `Q(√2)`.** (Immediate from Lagrange — periodic-in-CF means quadratic irrational; growth constant `1 + √2` sits in `Q(√2)`.)
- **The tower word (a Motzkin-path-with-run-constraint type) is a silver width growth castle.** (Non-trivial — algebraic GF, singularity at `√2 − 1`; the Motzkin-path type is Axis 3 and the silver growth type is Axis 8, so the two axes are linked by a real theorem, not a definition.)

Cross-axis-8 theorems (relating growth types under different axes) are the frontier: for instance, *"does every silver width growth castle become a bronze area growth castle when re-graded?"* — likely false, but stateable and testable.

### Naming precedence and the wiki convention

- **Meta-types are Axis 8.** They coexist with, do not replace, Axes 1-7. A castle can be simultaneously "unimodal (Axis 1) + silver width growth castle (Axis 8)"; the two are compatible descriptions from independent axes.
- **Always spell out the axis.** No "silver castle" as short form; the wiki uses "silver width growth castle" or the appropriate axis explicitly. Prevents the ambiguity between the four growth axes.
- **Only known members get named types.** If nothing on the wiki grows like copper, "copper width growth castle" is a valid empty class — it exists as a definition — but does not appear in the wiki's active vocabulary until a member is identified.

This is the classification axis the "Metallic-ratio ladder" thread on `IDEAS.md` tracks.

## Axis 9: Spectral predicates on the castle's polyomino graph

Axes 1-7 predicate on the **skyline** `(c_1, …, c_w)`; Axis 8 predicates on a **class's growth constant**. Axis 9 predicates on the **spectrum of a graph derived from the individual castle** — treat the filled cells as vertices with orthogonal-adjacency edges, and read off eigenvalues of the adjacency matrix, combinatorial Laplacian, or a related operator. This turns "castle shape" into "graph spectrum" and lets number-theoretic and spectral-graph-theoretic predicates cut across the structural axes.

Axis 9 is not fully written up yet — this section stubs the axis, populates its first named type (Ramanujan castle), and forward-links the four other spectral methods identified in the S-Division seminar plan on `IDEAS.md`. Each expected member is a **single-castle predicate**, distinct from Axis 8's per-class growth predicates.

### Ramanujan castle

A castle `C` is a **Ramanujan castle** iff, treating its filled cells as a graph with orthogonal-adjacency edges, its non-trivial adjacency eigenvalues `λ` (i.e. `λ ≠ ± d_max`) satisfy

```
|λ|  ≤  2 · √(d − 1)
```

where `d` is the maximum vertex degree. The bound is the **Alon-Boppana threshold** — the smallest asymptotic spectral radius achievable by an infinite family of `d`-regular graphs, and the defining property of Ramanujan graphs in arithmetic combinatorics (Lubotzky, Phillips, Sarnak; Margulis). Ramanujan castles are, informally, "the spectrally most expander-like castles at given size" — their adjacency graphs are as close to the theoretical mixing-optimum as possible.

The castle graph is not regular in general (interior cells have degree 4, edge cells have degree 3, corner cells degree 2), so the strict definition invokes the **max-degree** form of the bound; refinements to the bipartite-Ramanujan condition or to spectra of the non-backtracking / Ihara-adjacency operator (see the Ihara-zeta seminar on `IDEAS.md`) are the natural generalizations. Structural-axis castles whose Ramanujan status is worth checking first:

- **Boxcastle** (Axis 5) — the full `w × h` rectangle graph. Its spectrum is known: `2·(cos(iπ/(w+1)) + cos(jπ/(h+1)))` for `1 ≤ i ≤ w, 1 ≤ j ≤ h`. Whether it hits the Ramanujan bound depends on `w, h`.
- **Hook** (Axis 5) — the L-shape. Small, spectrum computable by hand.
- **Ferrers / staircase** (Axis 1) — the standard partition-shape polyominoes; their Laplacian spectra have partial classical results.
- **Crenellated / battlement** (Axis 7) — alternating heights; highly regular local structure, likely a Ramanujan candidate for suitable `w, h`.

**The Ramanujan castle is a photogenic classification target.** A "smallest Ramanujan castle" or "smallest non-trivial Ramanujan castle at each `(w, h)`" would be a clean result — pure combinatorics, small computer search, and directly ties castle shape to a deep number-theoretic notion of graph optimality.

### Golden-spectrum and silver-spectrum castles

The first Axis 9 types with computed members ([[castle-graph-spectral-radius](pages/castle-graph-spectral-radius.md)]). A castle is a **golden-spectrum castle** if its adjacency spectral radius is `φ`, a **silver-spectrum castle** if it is `1 + √2`, and a **golden-squared-spectrum castle** if it is `φ²`. Census over all castles with `w ≤ 6, h ≤ 6` and `w = 7, h ≤ 5`:

- golden: the six 4-cell castles whose graph is the path `P_4` - `(4)`, `(1,3)`, `(3,1)`, `(1,1,2)`, `(2,1,1)`, `(1,1,1,1)`; no other size can qualify (a connected graph with spectral radius below 2 is a path or a star).
- silver: the `3×2` rectangle `(3,3) = (2,2,2)` (`P_2 × P_3`) and three non-rectangular mirror pairs, `(1,2,3,1,2,3)`, `(2,1,6,2,1,3)`, `(1,1,2,4,1,3,1)`, each with `x² − 2x − 1` dividing its characteristic polynomial exactly.
- golden-squared: `(4,4)` (`P_2 × P_4`) and `(1,3,2,3,1)`.

Copper `2 + √5 = 4.236` and every higher metallic mean are impossible for any castle graph (maximum degree 4, spectral radius below 4). Bronze `3.303` is open - absent up to the scanned size. These are single-castle predicates, distinct from Axis 8's per-class growth constants: PE 502's own signed transfer matrix never has a metallic eigenvalue, so the metallic means reach individual castles only through their polyomino graphs.

### Sketched additional Axis-9 types (S-Division seminar targets)

Not yet populated on the wiki, but the following spectral predicates would sit here when they land:

- **Isospectral castles** - a *pair* predicate (two non-isomorphic castles with the same spectrum), now populated on [[isospectral-castles](pages/isospectral-castles.md)]: the smallest adjacency-isospectral pair has 10 cells (`(1,1,1,2,3,2)` and `(1,1,2,2,3,1)`), the smallest Laplacian-isospectral pair 11 cells (two trees, `(1,1,1,2,1,1,2,1,1)` and `(1,1,3,1,1,1,2,1)`), the smallest pair isospectral for both operators 16 cells; exhaustive to 16 cells, with 50 adjacency groups already at 16.
- **Sparse-spectrum castle** — a predicate on the skyline DFT `ĉ_k`: the individual castle has `supp(ĉ) ⊆ S` for some fixed small set `S`. The Axis-7 **crenellated** type is exactly the two-atom DFT-support case (energy at `k = w/2`). The general sparse-spectrum classification (which sparse-support sequences are valid castles?) hooks into compressed sensing and turnpike reconstruction. See the S-Division `Skyline DFT — individual-castle signatures` thread.
- **Low-pass / high-pass castle** — a soft version of sparse-spectrum: the castle's DFT energy is concentrated in low-k modes (smooth mountain-shaped skyline) or high-k modes (jagged crenellation). Not a hard predicate but a natural spectral-concentration classifier.
- **Ihara-Ramanujan castle** — the Ramanujan condition transferred to the spectrum of the Ihara / non-backtracking operator rather than the adjacency operator. Arithmetic-combinatorial invariant analogous to Selberg zeta for hyperbolic surfaces. Longer-horizon; see the S-Division `Ramanujan castles / Ihara zeta` thread.

[[spectral-analysis](pages/spectral-analysis.md)] is the toolkit-side companion to this axis — this axis catalogs the *predicates on individual castles*; that page catalogs the *methods for computing spectra*. The two evolve together: a completed spectral method + a satisfied predicate = a named castle type. Ramanujan castle is the current live pairing (method: Ihara / adjacency-spectrum; predicate: Alon-Boppana bound).

## Open threads this classification opens

The taxonomy makes explicit which sub-families the wiki has, which are candidates, and which are open. The largest open groupings, in rough order of tractability:

1. **k-modal** for `k ≥ 2` — a parametric family whose `k = 1` case is [[convex-castle](pages/convex-castle.md)] (binomial); `k = 2, 3, …` are genuinely open with no candidate closed form.
2. **m-smooth / m-disparate** for `m ≥ 2` — a paired family; `m = 1` collapses to Motzkin-path.
3. **Symmetry types** (palindromic, centrally symmetric, self-conjugate) — untouched.
4. **Rainbow** — direct permutation-classification tie, immediate seminar target for the [[castles-as-upgraded-cycle-count](pages/castles-as-upgraded-cycle-count.md)] triad.
5. **Bronze / copper / nickel width growth castle identification** — Axis-8 meta-types past silver; the metallic-mean ladder growth constants realized in castle rule modifications; tied to [[metallic-means](pages/metallic-means.md)].
6. **Even-peak** — parity via peak count rather than block count; genuinely different from [[castle-sign](pages/castle-sign.md)]'s `(−1)^blocks`.
7. **Ramanujan castles** (Axis 9) — the first named spectral-graph-theoretic type: castles whose non-trivial adjacency eigenvalues satisfy the Alon-Boppana bound `|λ| ≤ 2√(d−1)`. Photogenic seminar target; small computer search over structural sub-families (boxcastle, hook, staircase, crenellated) is the natural first pass.
8. **Axis-9 spectral types generally** — isospectral pairs, sparse-spectrum, low/high-pass, Ihara-Ramanujan. The S-Division seminar targets on `IDEAS.md`; all currently sketched, none populated.

## Related Concepts

- [[castle-polyomino](pages/castle-polyomino.md)] — the base object.
- [[castle-representations](pages/castle-representations.md)] — the skyline `(c_1, …, c_w)` is the integer-tuple encoding this classification predicates on.
- [[convex-castle](pages/convex-castle.md)] / [[convex-castle-binomial-identity](pages/convex-castle-binomial-identity.md)] — the unimodal (row-convex) type.
- [[polyominoes](pages/polyominoes.md)] / [[column-convex-polyomino](pages/column-convex-polyomino.md)] / [[column-convex-polygon-enumeration](pages/column-convex-polygon-enumeration.md)] — the base-type home literature.
- [[stack-polyomino-gf](pages/stack-polyomino-gf.md)] — the unimodal-skyline (single-peak) family from AC Ex. I.8.
- [[dyck-words](pages/dyck-words.md)] / [[tower-word-continued-fraction](pages/tower-word-continued-fraction.md)] — the Dyck-path / Motzkin-path types.
- [[metallic-means](pages/metallic-means.md)] / [[pell-castle-strip](pages/pell-castle-strip.md)] — the growth-constant classification axis.
- [[castle-by-area](pages/castle-by-area.md)] — where several types (even-area, valley) are counted.
- [[castle-sign](pages/castle-sign.md)] / [[castle-foata-transform](pages/castle-foata-transform.md)] — the parity / peak-count / record statistics several types predicate on.
- [[castles-as-upgraded-cycle-count](pages/castles-as-upgraded-cycle-count.md)] — the framework the rainbow type maps onto directly.
- [[castle-snippets](pages/castle-snippets.md)] — tested Python one-liners for each of the classification predicates on this page.
- [[spectral-analysis](pages/spectral-analysis.md)] — the methods hub paired with Axis 9's spectral predicates.

## Footnotes

[^1]: raw/castle-types.wiki L1-L9 — "A castle on a w × h grid is determined by its skyline, the sequence of column heights c_1, c_2, …, c_w with 1 ≤ c_i ≤ h and max_i c_i = h. (Problem 502 also requires an even number of blocks; the types below mostly ignore, or independently re-impose, that parity rule.) Every castle is automatically column-convex and bottom-aligned, so each type is a further restriction on the skyline." (Source: https://charlesreid1.com/wiki/Project_Euler/502/Castle_Types, fetched 2026-09-15.)
[^2]: raw/castle-types.wiki §"Base types" L11-L19 — the 7 base types: column-convex, unimodal (`c_1 ≤ … ≤ c_p ≥ … ≥ c_w`), directed (every cell reachable from bottom-left by east/north path), parallelogram (perpendicular-to-main-diagonal sections are connected), Ferrers (`c_1 ≥ … ≥ c_w`), staircase (Ferrers with strict inequality — all distinct heights), m-disparate (`|c_{i+1} − c_i| ≥ m`).
[^3]: raw/castle-types.wiki §"Proposed additional types" L21-L57 — the 35 proposed types, numbered 1-35: convex/row-convex, reverse Ferrers, strictly unimodal, bimodal, k-modal, anti-unimodal (V-shaped), plateau-free, m-smooth (Lipschitz), zigzag, alternating parity, palindromic, centrally symmetric, Dyck-path, Motzkin-path, flat-top, single-summit, even-area, even-peak, equal-block, two-level, self-conjugate, crenellated, moated, rainbow, hook, twin-peak, single-valley, fence-post, linear, convex-skyline (second differences ≥ 0), concave-skyline (≤ 0), triangular-area, prime-top, integer-mean, boxcastle.
