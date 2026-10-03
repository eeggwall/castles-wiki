---
title: Castle classification - growth types
category: Concepts
summary: A class-level classification. A castle class - an infinite family defined by a construction rule - has a growth type, the growth constant of its count sequence along a stated size axis. Metallic slot (golden / silver / bronze / copper / nickel / …) for quadratic growth; non-metallic slot (tribonacci / tetranacci / supergolden / plastic-squared / …) for higher-degree algebraic growth.
tags: [concept, castle, classification, taxonomy, growth-constant, metallic-means, ridge-castle, non-metallic, meta-classification, n-nacci, cubic-pisot, plastic-number, class-predicate]
sources: [castle-classification, oeis-mining-pe502]
created: 2026-09-19
updated: 2026-10-02
---

# Castle classification - growth types

## Scope: class predicates

The shape types on [[castle-classification-shape](pages/castle-classification-shape.md)] and the spectral types on [[castle-classification-spectrum](pages/castle-classification-spectrum.md)] are both **single-castle** predicates: given `(c_1, …, c_w)` you ask a question about that one castle. A growth type is different. The object it classifies is **a class**, an infinite family of castles defined by a construction rule, and the answer is the growth constant of that family's count sequence along a stated size axis.

Two consequences make this a **meta-classification**:

- **The invariant is not read from a single castle.** "Silver width growth castle" is not a property that a single castle either has or does not have; it is a property of the family. A single castle in a silver-width-growth class is still just a castle, and could sit in a completely different class with a different growth constant.
- **Two very different-looking classes can share a type.** The anchored 1-smooth castles of exact height 3 ([[pell-castle-strip](pages/pell-castle-strip.md)]) and the ridge castles of exact height 3 (ridge rule `R_3 = J − D`, [[metallic-strip-realizability](pages/metallic-strip-realizability.md)]) are different rules, but both are silver width growth castles.

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
  - **width** - the sequence is graded by width `w` (exact height `h` fixed).
  - **vertical** - by height `h` (width `w` fixed or bounded).
  - **area** - by total area `∑ c_i`.
  - **block** - by block count.
- **"growth castle"** - the noun, marking this as a class-level type.

**The axis is always stated explicitly.** A silver width growth castle and a silver vertical growth castle are different claims; there is no default axis. No shorthand like "silver castle" - the wiki uses the full form to keep the class-level meta-types unambiguous.

## Width growth castles

The width axis grades a class by `w` at a fixed exact height. Every rung of the metallic ladder is realized. Non-metallic width constants also occur - the tree castles of exact height `h` grow at `(1 + √(4h − 3))/2`, non-metallic for `h ≥ 3` ([[castle-graph](pages/castle-graph.md)]), and the plateau-free rule at `h − 1` - but the named non-metallic constants of this page are on the area axis.

### Golden - `δ_1 = φ`

A class whose width-graded count sequence grows at `φ = (1 + √5) / 2`, equivalently whose width GF has dominant singularity at `1 / φ = φ − 1`. Known member:

- **The Fibonacci castles** ([[castle-classification-shape](pages/castle-classification-shape.md)] Axis 2, [[castle-graph](pages/castle-graph.md)]) - the tree castles of exact height 2: no two adjacent height-2 columns, so every upper block has width 1, and at least one height-2 column. Count `F_{w + 2} − 1`, generating function `x / ((1 − x)(1 − x − x²))`, with the `p_1 = 1, p_2 = 1` denominator `1 − x − x²` carrying the growth.
- **The ridge castles of exact height 2** ([[castle-classification-shape](pages/castle-classification-shape.md)] Axis 2) - no two adjacent columns of height 1. Exchanging the heights 1 and 2 maps them onto the Fibonacci castles plus the all-1 row, so there are `F_{w + 2}` of them for `w ≥ 2`. This is the `h = 2` rung of the ridge rule below.

### Silver - `δ_2 = 1 + √2`

A class whose width-graded count sequence grows at `1 + √2 ≈ 2.4142`. Known members:

- **The anchored 1-smooth castles of exact height 3** ([[pell-castle-strip](pages/pell-castle-strip.md)]) - first column at height 1, neighbouring columns differing by at most 1, some column at height 3. Count `P_w − 2^{w−1}` (`0, 0, 1, 4, 13, 38, 105, 280, …`), where the Pell numbers `P_w` (OEIS A000129, denominator `1 − 2x − x²`, the `p_1 = 2, p_2 = 1` case) count the same rule on the Pell castle strip without the requirement to reach height 3, and `2^{w−1}` removes the skylines that stay at heights 1 and 2. With a free first column the count is `A001333(w + 1) − 2^w` (`1, 3, 9, 25, 67, 175, …`, from the Pell-Lucas numbers A001333). Both grow like `1 + √2`.[^exact]
- **The ridge castles of exact height 3** (ridge rule `R_3 = J − D`, [[castle-classification-shape](pages/castle-classification-shape.md)] Axis 2, [[metallic-strip-realizability](pages/metallic-strip-realizability.md)]) - the same growth constant, a different construction. Ridge castles of exact height 3: `1, 5, 15, 39, 97, 237, 575, …`.

The **tower word** ([[tower-word-continued-fraction](pages/tower-word-continued-fraction.md)]) also grows at `1 + √2`, but on a different axis: A004149 counts tower words by word length (width plus twice the block count), with an algebraic GF whose singularity is at `√2 − 1`. By width, all castles of exact height `h` number `h^w − (h − 1)^w`, an integer growth constant `h`.

### Bronze, copper, nickel, and higher - realized by ridge castles

All higher rungs are realized by a single named predicate: the **ridge rule** (adjacent columns differ in height unless both equal the max `h`; its castles of exact height `h` are the **ridge castles**, [[castle-classification-shape](pages/castle-classification-shape.md)] Axis 2), transfer matrix `R_h = J − D`, characteristic polynomial `(x + 1)^{h − 2} (x² − (h − 1) x − 1)`, Perron root the `(h − 1)`-th metallic mean `δ_{h − 1}` ([[metallic-strip-realizability](pages/metallic-strip-realizability.md)]). Metal `a` sits at height `h = a + 1`:

- **Bronze** (`δ_3 = (3 + √13) / 2 ≈ 3.303`) - ridge castles of exact height 4, `1, 7, 31, 118, 421, …`, growth in `Q(√13)`. (Three states per column do not give bronze - it is unreachable on ≤ 3 states, where natural rules land on non-metallic values such as `1 + √3`; the ridge rule's ceiling exception pins `p_2 = 1`.)
- **Copper** (`δ_4 = 2 + √5 = φ³`) - ridge castles of exact height 5; because `δ_4 = φ³ ∈ Q(√5)`, the transfer matrix gives `𝟙ᵀR_5^{w−1}𝟙 = F_{3w + 2}`, the **Fibonacci trisection**.
- **Nickel and beyond** (`δ_5, δ_6, …`) - ridge castles of exact heights 6, 7, ….

Whether each rung has *other* natural realizations besides the ridge rule `R_h = J − D` (silver has several) is open.

## Area growth castles

The area axis grades by total cells `∑ c_i`. This is the axis with the richest inventory, mostly non-metallic.

**Golden area growth castle.** The prime castles by area with the height unrestricted, `F_{n − 1}` of them ([[prime-castles](pages/prime-castles.md)]), grow at `φ`. At a fixed exact height they grow more slowly: plastic at height 3, supergolden at height 4, increasing towards `φ`. All castles of exact height 2 by area number `F_{A+1} − 1` and grow at `φ` ([[bounded-height-castles-nacci](pages/bounded-height-castles-nacci.md)]) - the `h = 2` rung of the n-nacci family below.

**The n-nacci area growth family.** All castles of exact height `h`, graded by area, are the compositions with largest part exactly `h`, with GF `1 / (1 − x − ⋯ − x^h) − 1 / (1 − x − ⋯ − x^{h−1})`, and grow at the `h`-nacci constant:

| constant | `h` | growth | minimal polynomial | count by area |
|---|---|---|---|---|
| **golden** (metallic `a = 1`) | 2 | `φ ≈ 1.6180` | `x² − x − 1` | `F_{A+1} − 1` (A000045) |
| **tribonacci** | 3 | `≈ 1.8393` | `x³ − x² − x − 1` | `A000073(A+2) − F_{A+1}` |
| **tetranacci** | 4 | `≈ 1.9276` | `x⁴ − x³ − x² − x − 1` | `A000078(A+3) − A000073(A+2)` |
| **pentanacci** | 5 | `≈ 1.9659` | `x⁵ − ⋯ − 1` | `A001591(A+4) − A000078(A+3)` |
| - | unrestricted | `2` | `x − 2` | `2^{A−1}` (A011782) |

Only the `h = 2` rung is metallic; every `h ≥ 3` rung is a non-metallic **`n`-nacci area growth castle** of degree `h`. The family is monotone increasing to `2`.

**The cubic-Pisot family.** Three cubic-Pisot constants, none metallic, have castle realizations by area; the first two come from the tree-castle-by-area family ([[tree-castle-by-area](pages/tree-castle-by-area.md)]), the `2 × 2`-block-free sub-family, a spectral type ([[castle-classification-spectrum](pages/castle-classification-spectrum.md)]):

| constant | growth | minimal polynomial | castle realization |
|---|---|---|---|
| **supergolden** | `≈ 1.4656` | `x³ − x² − 1` | tree castles of exact height 2 (the Fibonacci castles) by area, one less than Narayana's cows A000930; prime castles of exact height 4 by area ([[prime-castles](pages/prime-castles.md)]) |
| **plastic-squared** `ψ²` | `≈ 1.7549` | `x³ − 2x² + x − 1` | tree castles by area with the height unrestricted, A005251 ([[plastic-number](pages/plastic-number.md)]) |
| **plastic** `ψ` | `≈ 1.3247` | `x³ − x − 1` | the smallest castle-strip area growth constant, height 2, rule "height 1 may not follow height 1" ([[area-growth-census](pages/area-growth-census.md)]); prime castles of exact height 3 by area ([[prime-castles](pages/prime-castles.md)]) |

Tree castles of exact height 4 by area grow at `α ≈ 1.6851`, the dominant root of `x⁵ − x⁴ − x² − x − 1` (the sequence A000570, unique tournaments, [[unique-tournament](pages/unique-tournament.md)], counts them together with the lower heights), a quintic non-metallic constant between `φ` (exact height 3) and `ψ²` (height unrestricted).[^exact]

The plastic number also enters the counting recurrence: the `k = 6` signed-tower eigenvalue is `ρ_6 = 2ψ²`, a *spectral* appearance distinct from the growth-castle realization above.

**A subexponential class.** Weakly unimodal compositions ([[weakly-unimodal-composition](pages/weakly-unimodal-composition.md)], A001523), the convex castles by area, grow like `exp(2π√(n/3)) / (8 · 3^{3/4} · n^{5/4})` (Auluck 1951, as listed on the OEIS entry), so their exponential growth constant is `1`.

## Vertical and block growth castles

The **vertical growth axis** grades by height (`h` varying, `w` fixed). At fixed width there are `h^w − (h − 1)^w` castles of exact height `h`, a polynomial in `h`, so every class's count grows polynomially in `h` and the vertical growth constant is always `1`. For example, the k-direction signed count `P(k, L)` at fixed `L` has characteristic polynomial `(x + 1)^L (x − 1)^{L − 2}` ([[signed-tower-k-direction](pages/signed-tower-k-direction.md)]), a quasi-polynomial in `k`, and the count `F(w, h)` in `h` is annihilated by `(x² − 1)^w`.

The **block growth axis** grades by block count. [[tower-narayana-polynomial](pages/tower-narayana-polynomial.md)] gives the block-count GF structure; its growth-constant analysis is open.

## Cross-scope statements

Axis 8 allows statements of the form *"every class of type X is also of type Y"*, where X is a single-castle predicate (shape or spectrum) and Y is a growth type. Instances:

- **The tree castles of exact height 2 (the Fibonacci castles) are a golden width growth castle.** Immediate: "no two adjacent height-2 columns" has the Fibonacci transfer matrix `[[1, 1], [1, 0]]`.
- **The tower word (a Motzkin-path-with-run-constraint shape type) grows at `1 + √2` by word length.** Its GF is algebraic with singularity at `√2 − 1`; the Motzkin-path type is an Axis-3 shape predicate on [[castle-classification-shape](pages/castle-classification-shape.md)].
- **All castles of exact height `h` are an `h`-nacci area growth castle; the tree ban lowers the constant.** At exact height 3, all castles by area grow at tribonacci but tree castles by area (the spectral tree predicate on [[castle-classification-spectrum](pages/castle-classification-spectrum.md)]) grow at `φ`. At exact height 2 it drops `φ` to supergolden; with the height unrestricted it drops `2` to plastic-squared. The same single-castle predicate maps one growth type to another, differently at each height.

Relating the growth types of one class under different axes is open.

## Naming precedence and the wiki convention

- **Growth types are class-level.** They coexist with, do not replace, the shape and spectral types. A castle can be simultaneously "unimodal (a shape predicate) and a member of a silver width growth castle class"; the two are compatible descriptions from different scopes.
- **Always spell out the axis.** No "silver castle" as short form; the wiki uses "silver width growth castle" or the appropriate axis explicitly. This prevents ambiguity between the four growth axes.
- **Only known members get named types.** A rung with no known member is a valid empty class - it exists as a definition - but does not appear in the wiki's active vocabulary until a member is identified.

## Open threads

1. **Alternative realizations of the bronze / copper / nickel width growth castles.** Silver has several realizations; every higher rung has only the ridge rule `R_h = J − D`. Does any higher rung admit a second, structurally distinct castle-strip rule?
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

*(Except where footnoted, the identities above are cross-referenced and their derivations live on the linked pages.)*

[^exact]: Verified by execution (Python 3, 2026-10-02): the anchored 1-smooth skylines over `{1, 2, 3}` reaching height 3 were enumerated for `w ≤ 10` and equal `P_w − 2^{w−1}`; with a free first column they equal `A001333(w + 1) − 2^w` (`1, 3, 9, 25, 67, 175, 449, 1137, 2851, 7095`); tree castles of exact height 4 by area, by a transfer recurrence to area 400, have successive ratio `1.685137`. The other exact-height area counts are verified on [[bounded-height-castles-nacci](pages/bounded-height-castles-nacci.md)].
