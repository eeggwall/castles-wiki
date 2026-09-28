---
title: Castle classification - growth types
category: Concepts
summary: A class-level classification. A castle class - an infinite family defined by a construction rule - has a growth type, the growth constant of its count sequence along a stated size axis. Metallic slot (golden / silver / bronze / copper / nickel / …) for quadratic growth; non-metallic slot (tribonacci / tetranacci / supergolden / plastic-squared / …) for higher-degree algebraic growth.
tags: [concept, castle, classification, taxonomy, growth-constant, metallic-means, non-metallic, meta-classification, n-nacci, cubic-pisot, plastic-number, class-predicate]
sources: [castle-classification, oeis-mining-pe502]
created: 2026-09-19
updated: 2026-09-28
---

# Castle classification - growth types

## Scope: class predicates

The shape types on [[castle-classification-shape](pages/castle-classification-shape.md)] and the spectral types on [[castle-classification-spectrum](pages/castle-classification-spectrum.md)] are both **single-castle** predicates: given `(c_1, …, c_w)` you ask a question about that one castle. A growth type is different. The object it classifies is **a class**, an infinite family of castles defined by a construction rule, and the answer is the growth constant of that family's count sequence along a stated size axis.

Two consequences make this a **meta-classification**:

- **The invariant is not read from a single castle.** "Silver width growth castle" is not a property that a single castle either has or does not have; it is a property of the family. A single castle in a silver-width-growth class is still just a castle, and could sit in a completely different class with a different growth constant.
- **Two very different-looking classes can share a type.** The anchored 1-smooth height-3 strip ([[pell-castle-strip](pages/pell-castle-strip.md)]) and the ceiling-exception rule `J − D` at height 3 ([[metallic-strip-realizability](pages/metallic-strip-realizability.md)]) are different rules, but both are silver width growth castles.

The rest of this page names the growth types, states the wiki's naming convention, catalogues the known members on each axis, and lists cross-axis statements.

## The metallic and non-metallic slots

The main axis of growth constants is the [[metallic-means](pages/metallic-means.md)] family `δ_a = (a + √(a² + 4)) / 2` for `a = 1, 2, 3, …` - golden (`φ`), silver (`1 + √2`), bronze (`(3 + √13) / 2`), copper (`2 + √5 = φ³`), nickel (`(5 + √29) / 2`), and so on. A castle-strip family whose width generating function has denominator `1 − p_1 · x − p_2 · x²` grows at `(p_1 + √(p_1² + 4 p_2)) / 2`, which is a metallic mean iff `p_2 = 1` ([[metallic-strip-realizability](pages/metallic-strip-realizability.md)]).

Not every algebraic growth constant is a metallic mean. The wiki has two other families:

- **n-nacci constants**, roots of `x^h = x^{h − 1} + ⋯ + 1`: tribonacci at `h = 3`, tetranacci at `h = 4`, pentanacci, and so on to `2` in the limit.
- **cubic-Pisot constants**, roots of term-skipping cubics: supergolden (`x³ − x² − 1`), plastic-squared `ψ²` (`x³ − 2x² + x − 1`), and the plastic number `ψ` itself (`x³ − x − 1`), realized as a castle-strip area growth constant ([[area-growth-census](pages/area-growth-census.md)]).

These are the named slots. Other algebraic growth constants on the wiki have no family name: the degree-5 constant `α ≈ 1.6851` of the `h = 4` tree castles by area, the thousands of constants of [[area-growth-census](pages/area-growth-census.md)], and the non-metallic width constants below.

## Naming convention

A castle class is a **"`<constant>` `<axis>` growth castle"** iff its count sequence, graded by the chosen size axis, grows at rate `<constant>`. Three components:

- **`<constant>`.** When the growth constant is a metallic mean, use the metal: **golden** (`a = 1`, growth `φ`), **silver** (`a = 2`, growth `1 + √2`), **bronze** (`a = 3`), **copper** (`a = 4` = `φ³`), **nickel** (`a = 5`), and so on. When it is not a metallic mean, use the constant's own name: **tribonacci**, **tetranacci**, **pentanacci**, **supergolden**, **plastic-squared**, **plastic**.
- **`<axis>`.** The size parameter being graded:
  - **width** - the sequence is graded by width `w` (height `h` fixed or bounded).
  - **vertical** - by height `h` (width `w` fixed or bounded).
  - **area** - by total area `∑ c_i`.
  - **block** - by block count.
- **"growth castle"** - the noun, marking this as a class-level type.

**The axis is always stated explicitly.** A silver width growth castle and a silver vertical growth castle are different claims; there is no default axis. No shorthand like "silver castle" - the wiki uses the full form to keep the class-level meta-types unambiguous.

## Width growth castles

The width axis grades a class by `w` at fixed or bounded height. Every rung of the metallic ladder is realized. Non-metallic width constants also occur - the height-`h` tree castles grow at `(1 + √(4h − 3))/2`, non-metallic for `h ≥ 3` ([[castle-graph](pages/castle-graph.md)]), and the plateau-free rule at `h − 1` - but the named non-metallic constants of this page are on the area axis.

### Golden - `δ_1 = φ`

A class whose width-graded count sequence grows at `φ = (1 + √5) / 2`, equivalently whose width GF has dominant singularity at `1 / φ = φ − 1`. Known member:

- **The height-2 tree castles** ([[castle-graph](pages/castle-graph.md)]) - skylines with `c_i ∈ {0, 1}` above the base and no two adjacent raised columns, so every upper block has width 1. Count sequence: Fibonacci `F_{w + 2}`, generating function `(1 + x) / (1 − x − x²)`, the `p_1 = 1, p_2 = 1` denominator.

### Silver - `δ_2 = 1 + √2`

A class whose width-graded count sequence grows at `1 + √2 ≈ 2.4142`. Known members:

- **The anchored 1-smooth height-3 strip** ([[pell-castle-strip](pages/pell-castle-strip.md)]) - skylines over `{1, 2, 3}` with `|c_{i+1} − c_i| ≤ 1` and first column at height 1. Count sequence: Pell numbers `P_w` at width `w` (OEIS A000129), generating function `1 / (1 − 2x − x²)` with width `w` at `x^{w−1}`, the `p_1 = 2, p_2 = 1` denominator; with a free first column the count is companion Pell (A001333).
- **The ceiling-exception rule `J − D`** at height 3 ([[metallic-strip-realizability](pages/metallic-strip-realizability.md)]) - the same growth constant, a different construction.

The **tower word** ([[tower-word-continued-fraction](pages/tower-word-continued-fraction.md)]) also grows at `1 + √2`, but on a different axis: A004149 counts tower words by word length (width plus twice the block count), with an algebraic GF whose singularity is at `√2 − 1`. By width at bounded height the tower count is `(k + 1)^L`, an integer growth constant.

### Bronze, copper, nickel, and higher - realized by one rule

All higher rungs are realized by a single named predicate: the **plateau-free-except-ceiling** rule (adjacent columns differ in height unless both equal the max `h`), transfer matrix `M_h = J − D`, characteristic polynomial `(x + 1)^{h − 2} (x² − (h − 1) x − 1)`, Perron root the `(h − 1)`-th metallic mean `δ_{h − 1}` ([[metallic-strip-realizability](pages/metallic-strip-realizability.md)]). Metal `a` sits at height `h = a + 1`:

- **Bronze** (`δ_3 = (3 + √13) / 2 ≈ 3.303`) - ceiling exception at height 4; count `4, 13, 43, 142, 469, …`, growth in `Q(√13)`. (Three states per column do not give bronze - it is unreachable on ≤ 3 states, where natural rules land on non-metallic values such as `1 + √3`; the ceiling exception pins `p_2 = 1`.)
- **Copper** (`δ_4 = 2 + √5 = φ³`) - ceiling exception at height 5; because `δ_4 = φ³ ∈ Q(√5)`, its strip count is `F_{3n + 5}`, the **Fibonacci trisection**.
- **Nickel and beyond** (`δ_5, δ_6, …`) - the same rule at heights 6, 7, ….

Whether each rung has *other* natural realizations besides `M_h = J − D` (silver has several) is open.

## Area growth castles

The area axis grades by total cells `∑ c_i`. This is the axis with the richest inventory, mostly non-metallic.

**Golden area growth castle.** The prime castles by area, `F_{n − 1}` of them ([[prime-castles](pages/prime-castles.md)]), grow at `φ`. All castles of height `≤ 2` by area are the Fibonacci sequence A000045 ([[bounded-height-castles-nacci](pages/bounded-height-castles-nacci.md)]) - the `h = 2` rung of the n-nacci family below.

**The n-nacci area growth family.** All castles of height `≤ h`, graded by area, grow at the `h`-step Fibonacci constant with GF `1 / (1 − x − ⋯ − x^h)`:

| constant | `h` | growth | minimal polynomial | OEIS (by area) |
|---|---|---|---|---|
| **golden** (metallic `a = 1`) | 2 | `φ ≈ 1.6180` | `x² − x − 1` | A000045 Fibonacci |
| **tribonacci** | 3 | `≈ 1.8393` | `x³ − x² − x − 1` | A000073 |
| **tetranacci** | 4 | `≈ 1.9276` | `x⁴ − x³ − x² − x − 1` | A000078 |
| **pentanacci** | 5 | `≈ 1.9659` | `x⁵ − ⋯ − 1` | A001591 |
| - | ∞ | `2` | `x − 2` | A011782 |

Only the `h = 2` rung is metallic; every `h ≥ 3` rung is a non-metallic **`n`-nacci area growth castle** of degree `h`. The family is monotone increasing to `2`.

**The cubic-Pisot family.** Three cubic-Pisot constants, none metallic, have castle realizations by area; the first two come from the tree-castle-by-area family ([[tree-castle-by-area](pages/tree-castle-by-area.md)]), the `2 × 2`-block-free sub-family, a spectral type ([[castle-classification-spectrum](pages/castle-classification-spectrum.md)]):

| constant | growth | minimal polynomial | castle realization |
|---|---|---|---|
| **supergolden** | `≈ 1.4656` | `x³ − x² − 1` | `h = 2` tree castles by area = Narayana's cows A000930 |
| **plastic-squared** `ψ²` | `≈ 1.7549` | `x³ − 2x² + x − 1` | `h → ∞` tree castles by area = A005251 ([[plastic-number](pages/plastic-number.md)]) |
| **plastic** `ψ` | `≈ 1.3247` | `x³ − x − 1` | the smallest castle-strip area growth constant, height 2, rule "height 1 may not follow height 1" ([[area-growth-census](pages/area-growth-census.md)]) |

The `h = 4` tree row, A000570 (unique tournaments, [[unique-tournament](pages/unique-tournament.md)]), grows at `α ≈ 1.6851`, the dominant root of `x⁵ − x⁴ − x² − x − 1`, a quintic non-metallic constant between `φ` (`h = 3`) and `ψ²` (`h → ∞`).

The plastic number also enters the counting recurrence: the `k = 6` signed-tower eigenvalue is `ρ_6 = 2ψ²`, a *spectral* appearance distinct from the growth-castle realization above.

**A subexponential class.** Weakly unimodal compositions ([[weakly-unimodal-composition](pages/weakly-unimodal-composition.md)], A001523), the convex castles by area, grow like `exp(2π√(n/3)) / (8 · 3^{3/4} · n^{5/4})` (Auluck 1951, as listed on the OEIS entry), so their exponential growth constant is `1`.

## Vertical and block growth castles

The **vertical growth axis** grades by height (`h` varying, `w` fixed). At fixed width a class has at most `h^w` castles of height `≤ h`, so its count grows polynomially in `h` and the vertical growth constant is always `1`. For example, the k-direction signed count `P(k, L)` at fixed `L` has characteristic polynomial `(x + 1)^L (x − 1)^{L − 2}` ([[signed-tower-k-direction](pages/signed-tower-k-direction.md)]), a quasi-polynomial in `k`, and the count `F(w, h)` in `h` is annihilated by `(x² − 1)^w`.

The **block growth axis** grades by block count. [[tower-narayana-polynomial](pages/tower-narayana-polynomial.md)] gives the block-count GF structure; its growth-constant analysis is open.

## Cross-scope statements

Axis 8 allows statements of the form *"every class of type X is also of type Y"*, where X is a single-castle predicate (shape or spectrum) and Y is a growth type. Instances:

- **Every height-2 tree-castle class is a golden width growth castle.** Immediate: "no two adjacent raised columns" is the Fibonacci strip.
- **The tower word (a Motzkin-path-with-run-constraint shape type) grows at `1 + √2` by word length.** Its GF is algebraic with singularity at `√2 − 1`; the Motzkin-path type is an Axis-3 shape predicate on [[castle-classification-shape](pages/castle-classification-shape.md)].
- **Every height-`≤ h` castle class is an `h`-nacci area growth castle; the tree ban lowers the constant.** At `h = 3`, all-castles-by-area is tribonacci but tree-castles-by-area (the spectral tree predicate on [[castle-classification-spectrum](pages/castle-classification-spectrum.md)]) is A006498 with golden growth. At `h = 2` it drops Fibonacci to supergolden; at `h → ∞` it drops `2` to plastic-squared. The same single-castle predicate maps one growth type to another, differently at each height.

Relating the growth types of one class under different axes is open.

## Naming precedence and the wiki convention

- **Growth types are class-level.** They coexist with, do not replace, the shape and spectral types. A castle can be simultaneously "unimodal (a shape predicate) and a member of a silver width growth castle class"; the two are compatible descriptions from different scopes.
- **Always spell out the axis.** No "silver castle" as short form; the wiki uses "silver width growth castle" or the appropriate axis explicitly. This prevents ambiguity between the four growth axes.
- **Only known members get named types.** A rung with no known member is a valid empty class - it exists as a definition - but does not appear in the wiki's active vocabulary until a member is identified.

## Open threads

1. **Alternative realizations of the bronze / copper / nickel width growth castles.** Silver has several realizations; every higher rung has only `M_h = J − D`. Does any higher rung admit a second, structurally distinct castle-strip rule?
2. **Block growth axis** - no member known.
3. **Cross-axis statements** - relating growth types under different axes on the same class.

## Related Concepts

- [[castle-classification](pages/castle-classification.md)] - the hub, with a map of the three scopes.
- [[castle-classification-shape](pages/castle-classification-shape.md)] - single-castle shape predicates (Axes 1-7).
- [[castle-classification-spectrum](pages/castle-classification-spectrum.md)] - single-castle spectral predicates (Axis 9).
- [[metallic-means](pages/metallic-means.md)] / [[pell-castle-strip](pages/pell-castle-strip.md)] / [[metallic-strip-realizability](pages/metallic-strip-realizability.md)] - the metallic ladder side.
- [[castle-strip](pages/castle-strip.md)] - the construction-rule object (a skyline read left to right under a neighbor rule) whose transfer matrix supplies width growth constants.
- [[bounded-height-castles-nacci](pages/bounded-height-castles-nacci.md)] - the n-nacci area growth family.
- [[tree-castle-by-area](pages/tree-castle-by-area.md)] / [[plastic-number](pages/plastic-number.md)] - the cubic-Pisot area growth constants and the plastic number's spectral appearance.
- [[area-growth-census](pages/area-growth-census.md)] - realizes the bare plastic number `ψ` as a castle-strip area growth constant.
- [[unique-tournament](pages/unique-tournament.md)] - the A000570 growth constant `α ≈ 1.685` in the non-metallic slot.
- [[castle-eigenvalues-by-example](pages/castle-eigenvalues-by-example.md)] - the pedagogy page explaining what "eigenvalue" means at each scope.
- [[castle-snippets-strips](pages/castle-snippets-strips.md)] - the growth-constant probes.

## Footnotes

*(All identities above are cross-referenced and their derivations live on the linked pages; no footnotes needed on this hub-like page.)*
