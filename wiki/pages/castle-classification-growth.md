---
title: Castle classification - growth types
category: Concepts
summary: A class-level classification. A castle class - an infinite family defined by a construction rule - has a growth type, the growth constant of its count sequence along a stated size axis. Metallic slot (golden / silver / bronze / copper / nickel / …) for quadratic growth; non-metallic slot (tribonacci / tetranacci / supergolden / plastic-squared / …) for higher-degree algebraic growth.
tags: [concept, castle, classification, taxonomy, growth-constant, metallic-means, non-metallic, meta-classification, n-nacci, cubic-pisot, plastic-number, class-predicate]
sources: [castle-classification, oeis-mining-pe502]
created: 2026-09-19
updated: 2026-09-25
---

# Castle classification - growth types

## Scope: class predicates

The shape types on [[castle-classification-shape](pages/castle-classification-shape.md)] and the spectral types on [[castle-classification-spectrum](pages/castle-classification-spectrum.md)] are both **single-castle** predicates: given `(c_1, …, c_w)` you ask a question about that one castle. A growth type is different. The object it classifies is **a class**, an infinite family of castles defined by a construction rule, and the answer is the growth constant of that family's count sequence along a stated size axis.

Two consequences make this a **meta-classification** rather than a classification of the same shape as the others:

- **The invariant is not read from a single castle.** "Silver width growth castle" is not a property that a single castle either has or does not have; it is a property of the family. A single castle in a silver-width-growth class is still just a castle, and could sit in a completely different class with a different growth constant.
- **Two very different-looking classes can share a type.** The anchored 1-smooth height-3 strip ([[pell-castle-strip](pages/pell-castle-strip.md)]) and the tower word ([[tower-word-continued-fraction](pages/tower-word-continued-fraction.md)]) are structurally different families - one rational, one algebraic - but both are silver width growth castles. Same growth constant, different constructions.

The rest of this page names the growth types, states the wiki's naming convention, catalogues the known members on each axis, and closes with the cross-axis theorems the meta-classification licenses.

## The metallic and non-metallic slots

The main axis of growth constants is the [[metallic-means](pages/metallic-means.md)] family `δ_a = (a + √(a² + 4)) / 2` for `a = 1, 2, 3, …` - golden (`φ`), silver (`1 + √2`), bronze (`(3 + √13) / 2`), copper (`2 + √5 = φ³`), nickel (`(5 + √29) / 2`), and so on. A castle-strip family whose width generating function has denominator `1 − p_1 · x − p_2 · x²` grows at `(p_1 + √(p_1² + 4 p_2)) / 2`, which is a metallic mean iff `p_2 = 1` ([[metallic-strip-realizability](pages/metallic-strip-realizability.md)]).

Not every algebraic growth constant is a metallic mean. The wiki has two other families:

- **n-nacci constants**, roots of `x^h = x^{h − 1} + ⋯ + 1`: tribonacci at `h = 3`, tetranacci at `h = 4`, pentanacci, and so on to `2` in the limit.
- **cubic-Pisot constants** ([[pisot-number](pages/pisot-number.md)]), roots of term-skipping cubics: supergolden (`x³ − x² − 1`), plastic-squared `ψ²` (`x³ − 2x² + x − 1`), and the still-unrealized plastic number `ψ` (`x³ − x − 1`).

Together the metallic ladder and these two families cover every algebraic growth constant on the wiki so far. Transcendental growth constants do occur - weakly-unimodal-composition area growth is one - and they fall outside the classification (no named slot).

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

The width axis grades a class by `w` at fixed or bounded height. Every rung of the metallic ladder is realized, and the non-metallic rungs are empty here (the non-metallic constants appear on the area axis instead).

### Golden - `δ_1 = φ`

A class whose width-graded count sequence grows at `φ = (1 + √5) / 2`, equivalently whose width GF has dominant singularity at `1 / φ = φ − 1`. Known member:

- **The height-2 tree castles** ([[castle-graph](pages/castle-graph.md)]) - skylines with `c_i ∈ {0, 1}` above the base and no two adjacent raised columns, so every upper block has width 1. Count sequence: Fibonacci `F_{w + 2}`, generating function `1 / (1 − x − x²)`, the `p_1 = 1, p_2 = 1` denominator.

### Silver - `δ_2 = 1 + √2`

A class whose width-graded count sequence grows at `1 + √2 ≈ 2.4142`. Known members:

- **The anchored 1-smooth height-3 strip** ([[pell-castle-strip](pages/pell-castle-strip.md)]) - skylines over `{1, 2, 3}` with `|c_{i+1} − c_i| ≤ 1` and first column at height 1. Count sequence: Pell numbers `P_{w + 1}` (OEIS A000129), generating function exactly `1 / (1 − 2x − x²)`, the `p_1 = 2, p_2 = 1` denominator; with a free first column the count is companion Pell (A001333).
- **The ceiling-exception rule `J − D`** at height 3 ([[metallic-strip-realizability](pages/metallic-strip-realizability.md)]) - the same growth constant, a different construction.
- **The tower word** ([[tower-word-continued-fraction](pages/tower-word-continued-fraction.md)]) - count sequence A004149, algebraic (not rational) GF with singularity at `√2 − 1`, so growth `1 / (√2 − 1) = √2 + 1`. Structurally very different from the two above (context-free rather than regular), but the same growth constant.

Three structurally different classes, one growth type. This is what a meta-classification is doing: uniting differently-shaped families by asymptotic behaviour rather than by shape predicates.

### Bronze, copper, nickel, and higher - realized by one rule

All higher rungs are realized by a single named predicate: the **plateau-free-except-ceiling** rule (adjacent columns differ in height unless both equal the max `h`), transfer matrix `M_h = J − D`, characteristic polynomial `(x + 1)^{h − 2} (x² − (h − 1) x − 1)`, Perron root the `(h − 1)`-th metallic mean `δ_{h − 1}` ([[metallic-strip-realizability](pages/metallic-strip-realizability.md)]). Metal `a` sits at height `h = a + 1`:

- **Bronze** (`δ_3 = (3 + √13) / 2 ≈ 3.303`) - ceiling exception at height 4; count `4, 13, 43, 142, 469, …`, growth in `Q(√13)`. (The naive "three states per column" does *not* give bronze - it is provably unreachable on ≤ 3 states and lands on non-metallic surds like `1 + √3` and `(3 + √17) / 2`; the ceiling exception is the decoupling that pins `p_2 = 1`.)
- **Copper** (`δ_4 = 2 + √5 = φ³`) - ceiling exception at height 5; because `δ_4 = φ³ ∈ Q(√5)`, its strip count is `F_{3n + 5}` = the **Fibonacci trisection**, the decimation made concrete.
- **Nickel and beyond** (`δ_5, δ_6, …`) - the same rule at heights 6, 7, …; the ladder is swept in full.

Whether each rung has *other* natural realizations besides `M_h = J − D` (silver has three) is open.

## Area growth castles

The area axis grades by total cells `∑ c_i`. This is the axis with the richest inventory, mostly non-metallic.

**Golden area growth castle.** The prime-castle-by-area count `2^{n − 1} − F_{n − 1}` ([[castle-by-area](pages/castle-by-area.md)]) is Fibonacci-dominated in `Q(√5)` and grows at `φ` by area. All castles of height `≤ 2` by area are the Fibonacci sequence A000045 ([[bounded-height-castles-nacci](pages/bounded-height-castles-nacci.md)]) - the `h = 2` rung of the n-nacci family below.

**The n-nacci area growth family.** All castles of height `≤ h`, graded by area, grow at the `h`-step Fibonacci constant with GF `1 / (1 − x − ⋯ − x^h)`:

| constant | `h` | growth | minimal polynomial | OEIS (by area) |
|---|---|---|---|---|
| **golden** (metallic `a = 1`) | 2 | `φ ≈ 1.6180` | `x² − x − 1` | A000045 Fibonacci |
| **tribonacci** | 3 | `≈ 1.8393` | `x³ − x² − x − 1` | A000073 |
| **tetranacci** | 4 | `≈ 1.9276` | `x⁴ − x³ − x² − x − 1` | A000078 |
| **pentanacci** | 5 | `≈ 1.9659` | `x⁵ − ⋯ − 1` | A001591 |
| - | ∞ | `2` | `x − 2` | A011782 |

Only the `h = 2` rung is metallic; every `h ≥ 3` rung is a genuine degree-`h` non-metallic **`n`-nacci area growth castle**. The family is monotone increasing to `2`.

**The cubic-Pisot family.** The tree-castle-by-area family ([[tree-castle-by-area](pages/tree-castle-by-area.md)]) - the `2 × 2`-block-free sub-family, a spectral type ([[castle-classification-spectrum](pages/castle-classification-spectrum.md)]) graded by area - realizes the three cubic-Pisot constants, none metallic:

| constant | growth | minimal polynomial | castle realization |
|---|---|---|---|
| **supergolden** | `≈ 1.4656` | `x³ − x² − 1` | `h = 2` tree castles by area = Narayana's cows A000930 |
| **plastic-squared** `ψ²` | `≈ 1.7549` | `x³ − 2x² + x − 1` | `h → ∞` tree castles by area = A005251 ([[plastic-number](pages/plastic-number.md)]) |
| **plastic** `ψ` | `≈ 1.3247` | `x³ − x − 1` | **not yet realized** as a plain count - the open watch-note on [[plastic-number](pages/plastic-number.md)] |

Between the cubic-Pisot rows sits the `h = 4` tree row, A000570 (unique tournaments, [[unique-tournament](pages/unique-tournament.md)]), growing at `α ≈ 1.6851`, the dominant root of `x⁵ − x⁴ − x² − x − 1` - a quintic, non-metallic, **non-Pisot** constant (a conjugate of modulus `1.0325`; [[pisot-number](pages/pisot-number.md)]) filling the slot between `φ` (`h = 3`) and `ψ²` (`h → ∞`).

The plastic number `ψ` itself (`x³ = x + 1`) also enters as the `k = 6` signed-tower eigenvalue `ρ_6 = 2ψ²`, but that is a *spectral* appearance in the counting recurrence, not a growth-castle count. The bare-`ψ` growth castle (a Padovan/Perrin-rate count) is the one open slot in the cubic-Pisot family.

**A transcendental boundary.** [[weakly-unimodal-composition](pages/weakly-unimodal-composition.md)] (A001523) has an area growth constant that is *not even algebraic* (transcendental, from the partition-function saddle-point analysis). Weakly-unimodal castles by area are a growth castle for no named constant - the outer boundary of the area axis.

## Vertical and block growth castles

The **vertical growth axis** grades by height (`h` varying, `w` fixed). No member is known. The natural candidate, the k-direction signed count `P(k, L)` at fixed `L`, is not one: its characteristic polynomial is `(x + 1)^L (x − 1)^{L − 2}` ([[signed-tower-k-direction](pages/signed-tower-k-direction.md)]), so it is a quasi-polynomial in `k` with no exponential growth at all. The count `F(w, h)` in `h` is likewise a quasi-polynomial (annihilated by `(x² − 1)^w`). A vertical growth castle with a metallic constant would have to come from a rule modification.

The **block growth axis** grades by block count. [[tower-narayana-polynomial](pages/tower-narayana-polynomial.md)] gives the block-count GF structure; growth-constant analysis pending.

## What the meta-classification enables

**Cross-scope theorems become stateable.** The interesting move Axis 8 licenses is statements of the form *"every class of type X is also of type Y"* where X is a single-castle predicate (shape or spectrum) and Y is a growth type. Concrete instances:

- **Every height-2 tree-castle class is a golden width growth castle.** Immediate: "no two adjacent raised columns" is the Fibonacci strip.
- **The tower word (a Motzkin-path-with-run-constraint shape type) is a silver width growth castle.** Non-trivial: algebraic GF, singularity at `√2 − 1`; the Motzkin-path type is an Axis-3 shape predicate on [[castle-classification-shape](pages/castle-classification-shape.md)] and silver growth is the class-level type, so the two are linked by a real theorem rather than a definition.
- **Every height-`≤ h` castle class is an `h`-nacci area growth castle; the tree ban lowers the constant.** At `h = 3`, all-castles-by-area is tribonacci but tree-castles-by-area (the spectral tree predicate on [[castle-classification-spectrum](pages/castle-classification-spectrum.md)]) is A006498 with golden growth. At `h = 2` it drops Fibonacci to supergolden; at `h → ∞` it drops `2` to plastic-squared. The same single-castle predicate maps one growth type to another, differently at each height.

Cross-growth theorems - relating types under different axes - are the frontier: *does every silver width growth castle become a bronze area growth castle when re-graded?* Likely false, but stateable and testable.

## Naming precedence and the wiki convention

- **Growth types are class-level.** They coexist with, do not replace, the shape and spectral types. A castle can be simultaneously "unimodal (a shape predicate) and a member of a silver width growth castle class"; the two are compatible descriptions from different scopes.
- **Always spell out the axis.** No "silver castle" as short form; the wiki uses "silver width growth castle" or the appropriate axis explicitly. This prevents ambiguity between the four growth axes.
- **Only known members get named types.** A rung with no known member is a valid empty class - it exists as a definition - but does not appear in the wiki's active vocabulary until a member is identified.

## Open threads

1. **Alternative realizations of the bronze / copper / nickel width growth castles.** Silver has three realizations; every higher rung has only `M_h = J − D`. Does any higher rung admit a second, structurally distinct castle-strip rule?
2. **The bare plastic number `ψ`** as an area growth constant - the one open slot in the cubic-Pisot family ([[plastic-number](pages/plastic-number.md)]).
3. **Vertical and block growth axes** - no member known for either; the natural vertical candidate is a quasi-polynomial.
4. **Cross-growth-axis theorems** - the frontier: relating growth types under different axes on the same class.

## Related Concepts

- [[castle-classification](pages/castle-classification.md)] - the hub, with a map of the three scopes.
- [[castle-classification-shape](pages/castle-classification-shape.md)] - single-castle shape predicates (Axes 1-7).
- [[castle-classification-spectrum](pages/castle-classification-spectrum.md)] - single-castle spectral predicates (Axis 9).
- [[metallic-means](pages/metallic-means.md)] / [[pell-castle-strip](pages/pell-castle-strip.md)] / [[metallic-strip-realizability](pages/metallic-strip-realizability.md)] - the metallic ladder side.
- [[castle-strip](pages/castle-strip.md)] - the construction-rule object (a skyline read left to right under a neighbor rule) whose transfer matrix supplies width growth constants.
- [[bounded-height-castles-nacci](pages/bounded-height-castles-nacci.md)] - the n-nacci area growth family.
- [[pisot-number](pages/pisot-number.md)] - what "Pisot" means and why it makes powers near-integers; the Pisot test on the castle-strip cubics.
- [[tree-castle-by-area](pages/tree-castle-by-area.md)] / [[plastic-number](pages/plastic-number.md)] - the cubic-Pisot area growth constants and the plastic number's spectral appearance.
- [[unique-tournament](pages/unique-tournament.md)] - the A000570 growth constant `α ≈ 1.685` in the non-metallic slot.
- [[castle-eigenvalues-by-example](pages/castle-eigenvalues-by-example.md)] - the pedagogy page explaining what "eigenvalue" means at each scope.
- [[castle-snippets-strips](pages/castle-snippets-strips.md)] - the growth-constant probes.

## Footnotes

*(All identities above are cross-referenced and their derivations live on the linked pages; no footnotes needed on this hub-like page.)*
