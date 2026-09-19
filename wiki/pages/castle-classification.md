---
title: Castle classification
category: Concepts
summary: Hub for the castle-type taxonomy. Three scopes with different classifying scales: shape types (Axes 1-7, skyline predicates on individual castles), spectral types (single-castle graph-spectrum predicates), and growth types (class-level, count-sequence growth constants). Compressibility is a fourth invariant living on castle-compression.
tags: [concept, castle, classification, taxonomy, hub, scope, shape, spectral, growth]
sources: [castle-classification]
created: 2026-09-15
updated: 2026-09-19
---

# Castle classification

The wiki classifies castles at three different **scopes**, each answering a different question. The three scopes need three pages because each has its own machinery, its own set of named types, and its own open threads. This page is the hub that maps them.

## The framing

A **castle** is a valid stacked-block configuration on a `w × h` grid ([[castle-polyomino](pages/castle-polyomino.md)]), determined by its **skyline** - the sequence of column heights[^1]

```
c_1, c_2, …, c_w      with 1 ≤ c_i ≤ h and max_i c_i = h.
```

Every castle is automatically **column-convex** (each column is one contiguous vertical run) and **bottom-aligned** (row 1 is a full-width block). A **castle type** is a further restriction beyond those two, and the restrictions come in three kinds.

## Map of the three scopes

| Scope | Object classified | Invariant | Named types | Page |
|---|---|---|---|---|
| **Shape** | one castle | skyline predicate on `(c_1, …, c_w)` | unimodal, Ferrers, staircase, palindromic, Dyck-path, Motzkin-path, rainbow, hook, crenellated, m-smooth, m-disparate, … (42 types on 7 axes) | [[castle-classification-shape](pages/castle-classification-shape.md)] |
| **Spectrum** | one castle | spectrum of a graph derived from it ([[castle-graph](pages/castle-graph.md)]) | tree, golden-spectrum, silver-spectrum, `φ²`-spectrum, isospectral (pair predicate), Ramanujan | [[castle-classification-spectrum](pages/castle-classification-spectrum.md)] |
| **Growth** | a whole class of castles under a construction rule | growth constant of the class's count sequence along a stated size axis | golden / silver / bronze / copper / nickel `<axis>` growth castle, tribonacci / tetranacci / supergolden / plastic-squared `<axis>` growth castle | [[castle-classification-growth](pages/castle-classification-growth.md)] |

A fourth invariant, **compressibility** - the length of the shortest description that produces the castle - is not classified by shape, spectrum, or growth. It sits on its own page [[castle-compression](pages/castle-compression.md)], with three tiers (parametric, rule-generated, generic) that cross-cut all three scopes above.

## Reading the scope column

The **shape** and **spectrum** scopes both classify a single castle, but they read different features of it. A shape predicate looks at the skyline `(c_1, …, c_w)` directly - is it unimodal? does it have a palindromic pattern? does it have exactly two peaks? A spectral predicate builds the polyomino graph (cells as vertices, orthogonal neighbours as edges) and reads eigenvalues off some operator on it. Two castles with different shapes can share a spectrum (isospectral pairs); two castles with the same shape trivially share every graph invariant, so the spectral predicate is *coarser* on the shape side but sees structure the shape cannot see (walks, mixing, expander behaviour).

The **growth** scope is fundamentally different. It classifies not a single castle but an entire family - a construction rule (a neighbour rule read left to right, a ceiling exception, a tree ban, or any other predicate defining an infinite class of castles) - and asks how fast the count sequence grows. "Silver width growth castle" is not a property a single castle either has or does not have; it is a property of an infinite family and the rule that defines it.

The **cross-scope** interactions are where classification stops being bookkeeping and becomes theorem-shaped: a shape predicate defines a class, and the class has a growth type; a spectral predicate can coincide with a shape one (the tree-castle condition "no `2 × 2` filled block" is both a shape restriction and a graph-theoretic one); the same class can be classified twice, at different scopes, and the two answers are related by real theorems, not by definition. [[castle-classification-growth](pages/castle-classification-growth.md)] closes with a section of cross-scope theorems the meta-classification licenses.

## What "classification" gives you

Three questions attach to every type:

1. **Is it counted?** Does the wiki already have a count (exact formula, generating function, algorithm) for the type?
2. **What is its count's shape?** Growth constant, C-finite / algebraic / transcendental character, OEIS identification if any.
3. **How does it interact with the parity clause?** Does the parity-projected version have the same shape, or is parity locked out by the type's structure?

Every open (2) is a seminar topic; every open (3) is a research thread. Question (2) is where the shape and growth pages meet: answering it for a shape type places that type's class on the growth axis.

**Parity.** Project Euler 502 (PE 502) requires an even number of blocks. Each type is defined without reference to that clause, and the even-block projector `(A ± P) / 2` ([[castle-sign](pages/castle-sign.md)]) is applied on top when needed.[^1] The clause is not independent of typing: a convex (unimodal) castle of height `h` has exactly `h` blocks, one per row, so every convex castle has the block parity of `h` and the projector keeps all of them or none.[^2]

## Upstream source

The shape-type catalogue is hydrated from `charlesreid1.com/wiki/Project_Euler/502/Castle_Types` (fetched 2026-09-15; wikitext cached at `raw/castle-types.wiki`). That page defines 42 types - 7 base types drawn from the polyomino literature (column-convex, unimodal, directed, parallelogram, Ferrers, staircase, m-disparate) and 35 proposed types aggregated from adjacent literature or newly defined.[^3] The upstream page states the types as skyline predicates only; the shape page organizes them into the seven structural axes and ties each type to the wiki thread that already touches it. The spectrum, growth, and compressibility scopes are the wiki's own additions.

## Open threads

Each scope's page carries its own detailed open list; the largest open items across all three:

1. **k-modal for `k ≥ 2`** (shape) - the parametric family whose `k = 1` case is [[convex-castle](pages/convex-castle.md)] (binomial).
2. **Symmetry types** (shape) - palindromic, centrally symmetric, self-conjugate - untouched.
3. **Rainbow** (shape) - direct permutation-classification tie, immediate seminar target for the [[castles-as-upgraded-cycle-count](pages/castles-as-upgraded-cycle-count.md)] triad.
4. **Ramanujan castles** (spectrum) - the universal-cover definition is stated on [[castle-classification-spectrum](pages/castle-classification-spectrum.md)]; the census over small castles with a `2 × 2` block has not been run.
5. **Bronze-spectrum castles** (spectrum) - absent among 4.87 million castles on [[castle-graph-spectral-radius](pages/castle-graph-spectral-radius.md)]; open beyond the scanned size.
6. **Sparse-spectrum, low / high-pass, Ihara-Ramanujan** (spectrum) - S-Division seminar targets on `IDEAS.md`.
7. **Alternative realizations of the bronze / copper / nickel width growth castles** (growth) - does any higher rung admit a second, structurally distinct rule the way silver does?
8. **The bare plastic number `ψ` as an area growth constant** (growth) - the one open slot in the cubic-Pisot family ([[plastic-number](pages/plastic-number.md)]).
9. **Vertical and block growth axes** (growth) - no member known for either.
10. **Compressibility** as a classifier in its own right ([[castle-compression](pages/castle-compression.md)]).

## Related Concepts

- [[castle-classification-shape](pages/castle-classification-shape.md)] - shape-based catalogue (Axes 1-7).
- [[castle-classification-spectrum](pages/castle-classification-spectrum.md)] - spectral catalogue (tree, golden-spectrum, isospectral, Ramanujan, …).
- [[castle-classification-growth](pages/castle-classification-growth.md)] - class-level growth-type catalogue (metallic and non-metallic slots).
- [[castle-compression](pages/castle-compression.md)] - compressibility as a fourth invariant.
- [[castle-polyomino](pages/castle-polyomino.md)] - the base object.
- [[castle-representations](pages/castle-representations.md)] - the skyline `(c_1, …, c_w)` the shape predicates read.
- [[castle-graph](pages/castle-graph.md)] - the polyomino graph the spectral predicates read.
- [[castle-strip](pages/castle-strip.md)] - the construction-rule object whose growth constant places a class on the growth axis.
- [[castle-eigenvalues-by-example](pages/castle-eigenvalues-by-example.md)] - a pedagogy page that walks through the different "eigenvalues" appearing at each scope.
- [[castle-sign](pages/castle-sign.md)] - the parity projector applied on top of any type.
- [[convex-castle](pages/convex-castle.md)] - the type whose block count is fixed by its shape.
- [[spectral-analysis](pages/spectral-analysis.md)] - the methods hub paired with the spectral predicates.
- [[castle-snippets](pages/castle-snippets.md)] - tested Python one-liners for the shape predicates and the castle-graph primitives.

## Footnotes

[^1]: raw/castle-types.wiki L1-L9 - "A castle on a w × h grid is determined by its skyline, the sequence of column heights c_1, c_2, …, c_w with 1 ≤ c_i ≤ h and max_i c_i = h. (Problem 502 also requires an even number of blocks; the types below mostly ignore, or independently re-impose, that parity rule.) Every castle is automatically column-convex and bottom-aligned, so each type is a further restriction on the skyline." (Source: https://charlesreid1.com/wiki/Project_Euler/502/Castle_Types, fetched 2026-09-15.)
[^2]: [[oeis-mining-pe502](pages/oeis-mining-pe502.md)] `binomial-vandermonde-identity.md` §1 L25-33 - "#blocks >= max(c) = h, with equality iff the profile is unimodal ... a convex castle of height h has exactly h blocks, and convex castles are exactly the minimum-block castles".
[^3]: raw/castle-types.wiki §"Base types" L11-L19 and §"Proposed additional types" L21-L57 [synthesis] - the 7 base types and the 35 numbered proposed types, all stated as skyline predicates.
