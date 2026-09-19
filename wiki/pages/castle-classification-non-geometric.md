---
title: Castle classification - non-geometric types
category: Concepts
summary: Castle classification that does not read the shape. Axis 8 types a castle class by the growth constant of its count under a construction rule (metallic and non-metallic slots); Axis 9 types an individual castle by the spectrum of its polyomino graph (tree, golden-/silver-spectrum, isospectral, Ramanujan); compressibility types it by description length.
tags: [concept, castle, classification, taxonomy, growth-constant, metallic-means, spectral, ramanujan, smith-theorem, dynkin, tree-castle, fibonacci, tribonacci, n-nacci, plastic-number, supergolden, compressibility]
sources: [castle-classification]
created: 2026-09-19
updated: 2026-09-19
---

# Castle classification - non-geometric types

The geometric types on [[castle-classification-geometric](pages/castle-classification-geometric.md)] ask what a castle looks like: is the skyline `(c_1, …, c_w)` unimodal, Ferrers, palindromic? The types on this page classify by something that is not read off the shape:

- **Axis 8, growth type.** The object classified is a **class** of castles, defined by a construction rule (a neighbor rule read left to right, a ceiling exception, a tree ban), and the invariant is the growth constant of its count sequence along a stated size axis. Two classes with different-looking members can share a type.
- **Axis 9, spectral type.** The object classified is an **individual castle**, but the invariant is the spectrum of a graph derived from it ([[castle-graph](pages/castle-graph.md)]: filled cells as vertices, orthogonal neighbors as edges). Two castles with different skylines can share a spectrum ([[isospectral-castles](pages/isospectral-castles.md)]).
- **Compressibility.** The invariant is the length of the shortest description that produces the castle ([[castle-compression](pages/castle-compression.md)]), which separates rule-generated irregularity from generic irregularity in a way no skyline predicate can.

The framing, the geometric / non-geometric split, and the consolidated open-thread list are on the hub page [[castle-classification](pages/castle-classification.md)].

## Axis 8: Growth-type meta-classification

Axes 1-7 are **predicates on individual castles**: given `(c_1, …, c_w)`, is this castle unimodal? Ferrers? palindromic? Axis 8 is a **predicate on castle classes** - a property of a *sequence of counts*, not of a single castle. This makes it a **meta-classification**: golden growth castle status is not a shape a given castle has, it is a growth rate a given class has.

The framework is the [[metallic-means](pages/metallic-means.md)] family `δ_a = (a + √(a² + 4))/2` for `a = 1, 2, 3, …` - golden (`φ`), silver (`1+√2`), bronze (`(3+√13)/2`), copper, nickel, and so on. A castle-strip family whose width generating function has denominator `1 − p_1·x − p_2·x²` grows at `(p_1 + √(p_1² + 4·p_2))/2`, which is a metallic mean iff `p_2 = 1` ([[metallic-strip-realizability](pages/metallic-strip-realizability.md)]). The metallic-mean ladder is thus a natural axis of count growth constants along which real castle classes fall, and the non-metallic algebraic constants (n-nacci, cubic Pisot) extend it.

### The naming convention

A castle class is a **"`<metal>` `<axis>` growth castle"** iff its count sequence, graded by the chosen size axis, grows at rate `δ_a` (the metallic mean for that metal). The three parts:

- **`<metal>`** - golden (`a=1`, growth `φ`), silver (`a=2`, growth `1+√2`), bronze (`a=3`, growth `(3+√13)/2`), copper (`a=4`, growth `2+√5 = φ³`), nickel (`a=5`, growth `(5+√29)/2`), and so on. See [[metallic-means](pages/metallic-means.md)].
- **`<axis>`** - the size parameter being graded:
  - **width** - the sequence is graded by width `w` (height `h` fixed or bounded)
  - **vertical** - the sequence is graded by height `h` (width `w` fixed or bounded)
  - **area** - the sequence is graded by total area `∑ c_i`
  - **block** - the sequence is graded by block count
- **"growth castle"** - the noun, marking this as an Axis-8 meta-type.

**The axis is always stated explicitly.** A silver width growth castle and a silver vertical growth castle are different claims; there is no default axis. The full form ("silver width growth castle") is used throughout - no shorthand like "silver castle" - to keep meta-types unambiguous. When the growth constant is not a metallic mean, the constant's own name takes the metal slot: "tribonacci area growth castle", "supergolden area growth castle".

### Golden width growth castle - the `δ_1 = φ` family

A class whose width-graded count sequence has growth constant `φ = (1+√5)/2`, equivalently whose width GF has dominant singularity at `1/φ = φ − 1`. Known member:

- **The height-2 tree castles** ([[castle-graph](pages/castle-graph.md)]) - skylines with `c_i ∈ {0, 1}` above the base and no two adjacent raised columns, so every upper block has width 1. Count sequence: Fibonacci `F_{w+2}`, generating function `1/(1 − x − x²)`, the `p_1 = 1, p_2 = 1` denominator.

The prime-castle count `2^{n−1} − F_{n−1}` on [[castle-by-area](pages/castle-by-area.md)] is Fibonacci-flavored in `Q(√5)` but graded by area, so it is a golden **area** growth castle, not a width one.

### Silver width growth castle - the `δ_2 = 1 + √2` family

A class whose width-graded count sequence has growth constant `1 + √2 ≈ 2.4142`. Known members:

- **The anchored 1-smooth height-3 strip** ([[pell-castle-strip](pages/pell-castle-strip.md)]) - skylines over `{1, 2, 3}` with `|c_{i+1} − c_i| ≤ 1` and first column at height 1 (an Axis-2 predicate plus a boundary condition). Count sequence: Pell numbers `P_{w+1}` (OEIS A000129), generating function exactly `1/(1 − 2x − x²)`, the `p_1 = 2, p_2 = 1` denominator; with a free first column the count is companion Pell (A001333). The ceiling-exception rule `J − D` at height 3 ([[metallic-strip-realizability](pages/metallic-strip-realizability.md)]) realizes the same growth constant.
- **The tower word** ([[tower-word-continued-fraction](pages/tower-word-continued-fraction.md)]) - count sequence A004149, algebraic (not rational) generating function with singularity at `√2 − 1`, so growth `1/(√2 − 1) = √2 + 1`. Structurally very different from the Pell strip (context-free rather than regular), but the same growth constant - so both are silver width growth castles.

**Two structurally different classes, one growth type.** This is the meta-classification working: silver width growth castle is a property that holds across differently-shaped families, uniting them by their asymptotic count behavior rather than by their skyline predicates.

### Bronze / copper / nickel width growth castles - realized by one rule

All higher rungs are **realized by a single named predicate** - the **plateau-free-except-ceiling** rule (adjacent columns differ in height unless both equal the max `h`), transfer matrix `M_h = J − D`, char poly `(x+1)^{h−2}(x² − (h−1)x − 1)`, Perron root the `(h−1)`-th metallic mean `δ_{h−1}` ([[metallic-strip-realizability](pages/metallic-strip-realizability.md)]). Metal `a` sits at height `h = a + 1`:

- **Bronze width growth castle** (`δ_3 = (3+√13)/2 ≈ 3.303`) - the ceiling-exception rule at **height 4**; count `4, 13, 43, 142, 469, …`, growth `(3+√13)/2` in `Q(√13)`. (The naive "three states per column" does *not* give bronze - it is provably unreachable on ≤ 3 states and lands on non-metallic surds like `1 + √3` and `(3+√17)/2`; the ceiling exception is the decoupling that pins `p_2 = 1`.)
- **Copper width growth castle** (`δ_4 = 2 + √5 = φ³`) - the ceiling-exception rule at **height 5**; because `δ_4 = φ³ ∈ Q(√5)`, its strip count is `F_{3n+5}` = the **Fibonacci trisection**, the decimation made concrete.
- **Nickel and beyond** (`δ_5`, `δ_6`, …) - the same rule at heights 6, 7, …; the ladder is swept in full.

Whether each rung has *other* natural realizations besides `M_h = J − D` (silver has three) is open; see [[metallic-strip-realizability](pages/metallic-strip-realizability.md)].

### Non-metallic growth castles - the n-nacci and cubic-Pisot families

The metallic ladder is not the whole story. The wiki has accumulated a second, structurally coherent family of growth constants that are **algebraic but not metallic means** - roots of `x^k = x^{k−1} + ⋯ + 1` (the "`k`-step Fibonacci" / **n-nacci** constants) and of the term-skipping cubics (the **cubic-Pisot** constants). A class is a **"`<constant>` `<axis>` growth castle"** where `<constant>` names the algebraic growth rate directly (tribonacci, tetranacci, supergolden, plastic-squared, …).

**The n-nacci area growth family.** All castles of height `≤ h`, graded by area, grow at the `h`-step Fibonacci constant with GF `1/(1 − x − ⋯ − x^h)` ([[bounded-height-castles-nacci](pages/bounded-height-castles-nacci.md)]):

| `<constant>` | `h` | growth | minimal polynomial | OEIS (by area) |
|---|---|---|---|---|
| **golden** (metallic `a=1`) | 2 | `φ ≈ 1.6180` | `x² − x − 1` | A000045 Fibonacci |
| **tribonacci** | 3 | `≈ 1.8393` | `x³ − x² − x − 1` | A000073 |
| **tetranacci** | 4 | `≈ 1.9276` | `x⁴ − x³ − x² − x − 1` | A000078 |
| **pentanacci** | 5 | `≈ 1.9659` | `x⁵ − ⋯ − 1` | A001591 |
| - | ∞ | `2` | `x − 2` | A011782 (`2^{A−1}`) |

Only the `h = 2` rung (golden) is metallic; every `h ≥ 3` rung is a genuine degree-`h` non-metallic **tribonacci / tetranacci / … area growth castle**. The family is monotone increasing to `2`.

**The cubic-Pisot family.** The tree-castle-by-area family ([[tree-castle-by-area](pages/tree-castle-by-area.md)]) - the 2×2-block-free sub-family, an Axis-9 structural type graded by area - realizes the three cubic-Pisot constants, none metallic:

| `<constant>` | growth | minimal polynomial | castle realization |
|---|---|---|---|
| **supergolden** | `≈ 1.4656` | `x³ − x² − 1` | `h = 2` tree castles by area = Narayana's cows A000930 |
| **plastic-squared** `ψ²` | `≈ 1.7549` | `x³ − 2x² + x − 1` | `h → ∞` tree castles by area = A005251 ([[plastic-number](pages/plastic-number.md)]) |
| **plastic** `ψ` | `≈ 1.3247` | `x³ − x − 1` | **not yet realized** as a plain count - the open watch-note on [[plastic-number](pages/plastic-number.md)] |

Between those rows sits the `h = 4` tree row, `A000570` (unique tournaments, [[unique-tournament](pages/unique-tournament.md)]), growing at `α ≈ 1.6851`, the dominant root of `x⁵ − x⁴ − x² − x − 1` - a quintic, non-metallic constant filling the slot between `φ` (`h = 3`) and `ψ²` (`h → ∞`).

The plastic number `ψ` itself (`x³ = x + 1`, [[plastic-number](pages/plastic-number.md)]) also enters as the `k = 6` signed-tower eigenvalue `ρ_6 = 2ψ²`, but that is a *spectral* appearance, not a growth-castle count. The bare-`ψ` growth castle (a Padovan/Perrin-rate count) is the one open slot in the cubic-Pisot family.

**Why the split matters.** The metallic naming (`<metal> <axis>`) and the non-metallic naming (`<constant> <axis>`) are the same meta-classification - a growth rate for a class along a stated axis - just with different name-sources: the metallic means `δ_a` for the quadratic ladder, the constant's own name for everything else. The deciding question is only whether the growth constant is a metallic mean (`x² − a x − 1`, purely-periodic continued fraction (CF), `p_2 = 1` in the strip denominator) or a higher-degree algebraic number. See [[metallic-means](pages/metallic-means.md)] for the quadratic side and [[bounded-height-castles-nacci](pages/bounded-height-castles-nacci.md)] / [[tree-castle-by-area](pages/tree-castle-by-area.md)] for the non-metallic side.

### Vertical / area / block growth castles

The **vertical growth axis** grades by height (`h` varying, `w` fixed). No member is known. The natural candidate, the k-direction signed count `P(k, L)` at fixed `L`, is not one: its characteristic polynomial is `(x+1)^L (x−1)^{L−2}` ([[signed-tower-k-direction](pages/signed-tower-k-direction.md)]), so it is a quasi-polynomial in `k` with no exponential growth at all. The count `F(w, h)` in `h` is likewise a quasi-polynomial (annihilated by `(x²−1)^w`). A vertical growth castle with a metallic constant would have to come from a rule modification.

The **area growth axis** grades by `∑ c_i`, and this is the axis where the wiki has the richest inventory - most of it **non-metallic**. Instances:

- **Golden area growth castle** - the prime-castle-by-area count `2^{n−1} − F_{n−1}` ([[castle-by-area](pages/castle-by-area.md)], Fibonacci-dominated in `Q(√5)`), and **all castles of height ≤ 2 by area** = Fibonacci A000045 ([[bounded-height-castles-nacci](pages/bounded-height-castles-nacci.md)]). The latter is the `h = 2` rung of the n-nacci family.
- **Non-metallic area growth castles** (the large majority): the **n-nacci family** - all castles of height `≤ h` by area, growing at the `h`-step Fibonacci constant, of which `h = 3` is the **tribonacci constant** `≈ 1.8393` ([[bounded-height-castles-nacci](pages/bounded-height-castles-nacci.md)]) - and the **cubic-Pisot** area growth constants of the tree-castle family: **supergolden** `≈ 1.4656` (Narayana's cows, `h = 2` tree castles) and **plastic-squared** `ψ² ≈ 1.7549` (`h → ∞` tree castles, [[tree-castle-by-area](pages/tree-castle-by-area.md)], [[plastic-number](pages/plastic-number.md)]). None of these is a metallic mean.
- **Transcendental negative example** - [[weakly-unimodal-composition](pages/weakly-unimodal-composition.md)] (`A001523`) has an area growth constant that is *not even algebraic* (transcendental, from the partition-function saddle-point analysis), so weakly-unimodal castles by area are not a growth castle for any algebraic constant - the outer boundary of the area axis.

The **block growth axis** grades by block count. [[tower-narayana-polynomial](pages/tower-narayana-polynomial.md)] gives the block-count generating function structure; growth-constant analysis pending.

### What the meta-classification enables

**Cross-type theorems become stateable.** The interesting move Axis 8 licenses is statements of the form *"every class of type X is also of type Y"* where X is a structural (Axis 1-7 or Axis 9) type and Y is a growth type. Some concrete instances:

- **Every height-2 tree-castle class is a golden width growth castle.** (Immediate - "no two adjacent raised columns" is the Fibonacci strip.)
- **The tower word (a Motzkin-path-with-run-constraint type) is a silver width growth castle.** (Non-trivial - algebraic GF, singularity at `√2 − 1`; the Motzkin-path type is Axis 3 and the silver growth type is Axis 8, so the two axes are linked by a real theorem, not a definition.)
- **Every height-`≤ h` castle class is an `h`-nacci area growth castle; imposing the Axis-9 tree constraint changes the growth constant.** (The tree ban strictly lowers the area growth rate: at `h = 3`, all-castles-by-area is **tribonacci** `≈ 1.8393` but tree-castles-by-area is A006498 with **golden** growth `φ`; at `h = 2` it drops Fibonacci to supergolden; at `h → ∞` it drops `2` to plastic-squared `ψ²`. So the same structural predicate (tree, Axis 9) maps one Axis-8 growth type to another, differently at each height - a real cross-axis interaction, not a definition.)

Cross-axis-8 theorems (relating growth types under different axes) are the frontier: for instance, *"does every silver width growth castle become a bronze area growth castle when re-graded?"* - likely false, but stateable and testable.

### Naming precedence and the wiki convention

- **Meta-types are Axis 8.** They coexist with, do not replace, the geometric axes. A castle can be simultaneously "unimodal (Axis 1) + a member of a silver width growth castle class (Axis 8)"; the two are compatible descriptions from independent axes.
- **Always spell out the axis.** No "silver castle" as short form; the wiki uses "silver width growth castle" or the appropriate axis explicitly. Prevents the ambiguity between the four growth axes.
- **Only known members get named types.** A rung with no known member is a valid empty class - it exists as a definition - but does not appear in the wiki's active vocabulary until a member is identified.

This is the classification axis the "Metallic-ratio ladder" thread on `IDEAS.md` tracks.

## Axis 9: Spectral predicates on the castle's polyomino graph

Axis 9 predicates on the **spectrum of a graph derived from the individual castle** - treat the filled cells as vertices with orthogonal-adjacency edges ([[castle-graph](pages/castle-graph.md)]) and read off eigenvalues of the adjacency matrix, combinatorial Laplacian, or a related operator. This turns "castle shape" into "graph spectrum" and lets number-theoretic and spectral-graph-theoretic predicates cut across the geometric axes. Each type is a **single-castle predicate** (or, for isospectrality, a pair predicate), distinct from Axis 8's per-class growth predicates. [[spectral-analysis](pages/spectral-analysis.md)] is the methods-side companion: this section catalogs the *predicates*, that page the *methods for computing spectra*.

Two facts about castle graphs shape every type below. They are **bipartite** (color cells by `(i + j) mod 2`), so the adjacency spectrum is symmetric about 0. And they are **almost never regular**: the leftmost cell of the top row has at most two neighbors, so a regular castle graph has degree at most 2 and is a path or a cycle, and the only castle graphs that qualify are the single cell, the domino, and the `2×2` square (a longer cycle would enclose a hole, which a bottom-aligned column-convex shape cannot). Every castle graph with more than four cells is irregular, with corner cells of degree 2, edge cells of degree 3, and interior cells of degree 4.

### Tree castle

A castle graph is a tree iff no `2×2` block is fully filled, iff no two horizontally adjacent columns both have height at least 2. Tree castles are Axis 9's simplest named type: single-castle, structural (a skyline predicate), and graph-theoretic (`G_c` is a tree). Counted **by width** by the transfer matrix `T_h(w+2) = T_h(w+1) + (h−1) T_h(w)` with growth constant `(1 + √(4h − 3))/2`, they hit named OEIS sequences at every height: **Fibonacci** at `h = 2` (`T_2(w) = F_{w+2}`), **Jacobsthal** at `h = 3` (`T_3(w) = J_{w+2}`), then A006130, A006131, … . Tree castles of height 2 are a **golden width growth castle** in Axis 8's terminology, giving the tree-castle family a rung on the metallic ladder without leaving Axis 9. Counted **by area** ([[tree-castle-by-area](pages/tree-castle-by-area.md)]) they instead realize the non-metallic **cubic-Pisot** growth constants - supergolden at `h = 2` (Narayana's cows A000930), plastic-squared `ψ²` at `h → ∞` (A005251) - so tree castles are supergolden / plastic-squared **area growth castles** (Axis 8 non-metallic slot). The unrestricted (non-tree) counterpart, all castles of height `≤ h` by area, is the **n-nacci** family (tribonacci at `h = 3`; [[bounded-height-castles-nacci](pages/bounded-height-castles-nacci.md)]) - the tree constraint is exactly what turns the n-nacci constants into the term-skipping cubic-Pisot ones. Full details on [[castle-graph](pages/castle-graph.md)].

### Golden-spectrum and silver-spectrum castles

The first Axis 9 types with computed members ([[castle-graph-spectral-radius](pages/castle-graph-spectral-radius.md)]). A castle is a **golden-spectrum castle** if its adjacency spectral radius is `φ`, a **silver-spectrum castle** if it is `1 + √2`, and a **golden-squared-spectrum castle** if it is `φ²`. Census over all castles with `w ≤ 6, h ≤ 6` and `w = 7, h ≤ 5`:

- golden: the six 4-cell castles whose graph is the path `P_4` - `(4)`, `(1,3)`, `(3,1)`, `(1,1,2)`, `(2,1,1)`, `(1,1,1,1)`.
- silver: the `3×2` rectangle `(3,3) = (2,2,2)` (`P_2 × P_3`) and three non-rectangular mirror pairs, `(1,2,3,1,2,3)`, `(2,1,6,2,1,3)`, `(1,1,2,4,1,3,1)`, each with `x² − 2x − 1` dividing its characteristic polynomial exactly.
- golden-squared: `(4,4)` (`P_2 × P_4`) and `(1,3,2,3,1)`.

**No castle of any other size is golden-spectrum.** By Smith's theorem, a connected graph with largest eigenvalue below 2 is one of the simply-laced Dynkin diagrams `A_n = P_n`, `D_n`, `E_6`, `E_7`, `E_8`.[^1] All five families occur as castle graphs: `A_n` as any path-shaped castle, `D_n` as `(1,2,1,1,…,1)` (a degree-3 cell at the base of a one-cell tower next to the left end), `E_6`, `E_7`, `E_8` as `(1,1,2,1,1)`, `(1,1,2,1,1,1)`, `(1,1,2,1,1,1,1)`. Their spectral radii are `2cos(π/(n+1))`, `2cos(π/(2n−2))`, `2cos(π/12)`, `2cos(π/18)`, `2cos(π/30)`, and `φ = 2cos(π/5)` is hit only by `A_4 = P_4`. (Checked by enumeration to 9 cells: 171 castles have spectral radius below 2, every radius among them is a Dynkin value, and exactly the six `P_4` castles have radius `φ`.)

Copper `2 + √5 = 4.236` and every higher metallic mean are impossible for any castle graph (maximum degree 4, spectral radius below 4). Bronze `3.303` is open - absent up to the scanned size. These are single-castle predicates, distinct from Axis 8's per-class growth constants: PE 502's own signed transfer matrix never has a metallic eigenvalue, so the metallic means reach individual castles only through their polyomino graphs.

### Isospectral castles

A *pair* predicate: two non-isomorphic castles with the same spectrum. Populated on [[isospectral-castles](pages/isospectral-castles.md)]: the smallest adjacency-isospectral pair has 10 cells (`(1,1,1,2,3,2)` and `(1,1,2,2,3,1)`), the smallest Laplacian-isospectral pair 11 cells (two trees, `(1,1,1,2,1,1,2,1,1)` and `(1,1,3,1,1,1,2,1)`), the smallest pair isospectral for both operators 16 cells; exhaustive to 16 cells, with 50 adjacency groups already at 16. Isospectral pairs are common from 12 cells on, so the spectrum is an Axis 9 *invariant*, not a *classifier*.

### Ramanujan castle

The regular-graph definition of a Ramanujan graph - every eigenvalue other than `±d` has `|λ| ≤ 2√(d − 1)` - has no content on castles, because castle graphs beyond four cells are never regular. For a connected irregular graph the spectral radius `λ_1` is strictly below `d_max`, so excluding `λ = ±d_max` excludes nothing, and the bound would then be tested against `λ_1` itself. The Alon-Boppana theorem does not bound `λ_1`: it says that for large `d`-regular graphs the largest **non-trivial** eigenvalue `λ(G) = max(λ_2, −λ_n)` is at least `2√(d − 1) − ε`.[^2]

The well-posed definition for irregular graphs is Greenberg's, via the universal cover.[^3] Let `T` be the universal covering tree of `G_C` and `ρ(T)` its spectral radius (`2√(d − 1)` when `G_C` is `d`-regular). Greenberg's theorem says finite graphs covered by `T` have `λ(G) ≥ ρ(T) − o(1)`, and `G_C` is **Ramanujan** iff every eigenvalue other than `±λ_1` satisfies `|λ| ≤ ρ(T)`. Castle graphs are bipartite, so this is the bipartite-Ramanujan condition `λ_2 ≤ ρ(T)`. Three consequences:

- **The threshold is castle-dependent.** `ρ(T)` must be computed from the castle's own covering tree. It is at most `2√(d_max − 1)` (a tree of maximum degree `Δ` has spectral radius at most `2√(Δ − 1)`), so `λ_2 ≤ 2√(d_max − 1)` is a necessary condition only: `2√3 ≈ 3.464` for castles with an interior cell, `2√2 ≈ 2.828` for castles whose every cell is on the boundary.
- **Tree castles are Ramanujan for free.** A finite tree is its own universal cover, so `ρ(T) = λ_1 ≥ λ_2` and the condition holds. The predicate only bites on castles with at least one `2×2` block, i.e. positive cycle rank ([[castle-graph](pages/castle-graph.md)]).
- **No census exists yet.** The first non-trivial cases are the boxcastle (spectrum `2cos(iπ/(w+1)) + 2cos(jπ/(h+1))`, so `λ_2` is explicit and only `ρ(T)` needs computing) and the crenellated type, whose repeated local structure makes its covering tree tractable.

The Ihara / non-backtracking version transfers the same condition to the spectrum of the non-backtracking operator, which is the form that connects to the Ihara-zeta seminar on `IDEAS.md`; see [[spectral-analysis](pages/spectral-analysis.md)] §5.

### Sketched additional Axis-9 types (S-Division seminar targets)

Not yet populated on the wiki, but the following spectral predicates would sit here when they land:

- **Sparse-spectrum castle** - a predicate on the skyline discrete Fourier transform (DFT) `ĉ_k`: the individual castle has `supp(ĉ) ⊆ S` for some fixed small set `S`. The Axis-7 **crenellated** type is exactly the two-atom DFT-support case (energy at `k = w/2`). The general sparse-spectrum classification (which sparse-support sequences are valid castles?) hooks into compressed sensing and turnpike reconstruction. See the S-Division `Skyline DFT - individual-castle signatures` thread.
- **Low-pass / high-pass castle** - a soft version of sparse-spectrum: the castle's DFT energy is concentrated in low-k modes (smooth mountain-shaped skyline) or high-k modes (jagged crenellation). Not a hard predicate but a natural spectral-concentration classifier.
- **Ihara-Ramanujan castle** - the Ramanujan condition on the non-backtracking operator rather than the adjacency operator. Arithmetic-combinatorial invariant analogous to Selberg zeta for hyperbolic surfaces. Longer-horizon; see the S-Division `Ramanujan castles / Ihara zeta` thread.

A completed spectral method on [[spectral-analysis](pages/spectral-analysis.md)] plus a satisfied predicate here is a named castle type; the two pages evolve together.

## Compressibility

[[castle-compression](pages/castle-compression.md)] classifies a castle by the length of the shortest program that produces it: **parametric** (box, hook, staircase, crenellated - a handful of numbers), **rule-generated** (a short neighbor rule plus a seed), and **generic** (no description shorter than the skyline itself). This is non-geometric in the same sense as Axis 9 - two castles of identical size and block count can sit in different tiers - and it cross-cuts the geometric axes: it separates "irregular because generated by a short rule" from "irregular because generic," a distinction no skyline predicate expresses.

## Open non-geometric threads

1. **Alternative realizations of the bronze / copper / nickel width growth castles** - the ceiling-exception rule `J − D` at height `h = a + 1` realizes the whole metallic ladder (silver has three realizations; bronze and above have only that one so far). Do any of the higher rungs admit a second, structurally distinct castle-strip rule the way silver does?
2. **The bare plastic number `ψ`** as an area growth constant - the one open slot in the cubic-Pisot family ([[plastic-number](pages/plastic-number.md)]).
3. **Vertical and block growth axes** - no member known for either; the natural vertical candidate is a quasi-polynomial.
4. **Ramanujan castles** - compute `ρ(T)` for the universal covers of small castles with a `2×2` block and run the census; boxcastles and crenellated castles first.
5. **Bronze-spectrum castles** - absent among 4.87 million castles on [[castle-graph-spectral-radius](pages/castle-graph-spectral-radius.md)]; open beyond the scanned size.
6. **Sparse-spectrum, low/high-pass, Ihara-Ramanujan** - the three sketched Axis-9 types; S-Division seminar targets on `IDEAS.md`.

## Related Concepts

- [[castle-classification](pages/castle-classification.md)] - the hub: framing, the geometric / non-geometric split, and the consolidated open-thread list.
- [[castle-classification-geometric](pages/castle-classification-geometric.md)] - the shape-based catalogue (Axes 1-7).
- [[metallic-means](pages/metallic-means.md)] / [[pell-castle-strip](pages/pell-castle-strip.md)] / [[metallic-strip-realizability](pages/metallic-strip-realizability.md)] - the metallic (quadratic) side of Axis 8.
- [[castle-strip](pages/castle-strip.md)] - the construction-rule object (a skyline read left to right under a neighbor rule) whose transfer matrix supplies width growth constants.
- [[bounded-height-castles-nacci](pages/bounded-height-castles-nacci.md)] - the n-nacci area growth family (Fibonacci, tribonacci, tetranacci, …), the non-metallic side of Axis 8.
- [[tree-castle-by-area](pages/tree-castle-by-area.md)] / [[plastic-number](pages/plastic-number.md)] - the cubic-Pisot area growth constants (supergolden, plastic-squared) and the plastic number's spectral appearance.
- [[unique-tournament](pages/unique-tournament.md)] - the `A000570` growth constant `α ≈ 1.685` in the non-metallic Axis-8 slot.
- [[castle-graph](pages/castle-graph.md)] / [[castle-graph-spectral-radius](pages/castle-graph-spectral-radius.md)] / [[isospectral-castles](pages/isospectral-castles.md)] - the Axis 9 object and its populated types.
- [[spectral-analysis](pages/spectral-analysis.md)] - the methods hub paired with Axis 9's spectral predicates.
- [[castle-compression](pages/castle-compression.md)] - compressibility as a cross-cutting non-geometric axis.
- [[castle-snippets-strips](pages/castle-snippets-strips.md)] / [[castle-snippets](pages/castle-snippets.md)] - growth-constant probes and the castle-graph primitives every Axis 9 spectrum starts from.

## Footnotes

[^1]: https://aeb.win.tue.nl/2WF02/spectra.pdf (Brouwer and Haemers, *Spectra of Graphs*) §3.1.1 Theorem 3.1.3 (Smith) - "each connected graph with largest eigenvalue less than 2 is a subgraph of one of the above graphs, i.e., one of the graphs A_n = P_n, the path with n vertices (n ≥ 1), or" `D_n`, `E_6`, `E_7`, `E_8`; the graphs with largest eigenvalue exactly 2 are the extended Dynkin diagrams `Â_n`, `D̂_n`, `Ê_6`, `Ê_7`, `Ê_8`.
[^2]: https://en.wikipedia.org/wiki/Ramanujan_graph §"Extremality of Ramanujan graphs" - "the Alon-Boppana bound states that for every d and ε > 0, there exists n such that all d-regular graphs G with at least n vertices satisfy λ(G) > 2√(d−1) − ε", where `λ(G)` is the largest absolute value of a non-trivial eigenvalue.
[^3]: https://arxiv.org/abs/1506.02335 (Hall, Puder, Sawin, *Ramanujan coverings of graphs*) §1 and §2.1 [synthesis] - `λ(G) = max(λ_2, −λ_n)` is the largest non-trivial eigenvalue in absolute value; `ρ(G)` is the spectral radius of the universal covering tree, equal to `2√(k−1)` for `k`-regular `G`; Theorem 2.1 (Greenberg, in Cioabă's form) gives `λ(G) ≥ ρ − o(1)` for finite quotients of a fixed tree; "graphs G satisfying λ(G) ≤ ρ(G) are considered to be optimal expanders. Following the terminology of [LPS88], they are called Ramanujan graphs"; for bipartite `G` the condition is that `λ_2, …, λ_{n−1}` lie in `[−ρ(G), ρ(G)]`.
