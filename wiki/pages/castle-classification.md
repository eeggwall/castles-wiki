---
title: Castle classification
category: Concepts
summary: Hub for the castle-type taxonomy. Geometric types (Axes 1-7, skyline predicates on individual castles) are catalogued on castle-classification-geometric; non-geometric types (Axis 8 growth type of a class, Axis 9 spectrum of the castle graph, compressibility) on castle-classification-non-geometric.
tags: [concept, castle, classification, taxonomy, skyline, geometric, non-geometric, spectral, growth-constant]
sources: [castle-classification]
created: 2026-09-15
updated: 2026-09-19
---

# Castle classification

## The framing

A **castle** is a valid stacked-block configuration on a `w × h` grid ([[castle-polyomino](pages/castle-polyomino.md)]), and is determined by its **skyline** - the sequence of column heights[^1]

```
c_1, c_2, …, c_w      with 1 ≤ c_i ≤ h and max_i c_i = h.
```

Every castle is automatically **column-convex** (each column is one contiguous vertical run) and **bottom-aligned** (row 1 is a full-width block). A **castle type** is a further restriction, and the restrictions come in two kinds:

- **Geometric (shape-based) types** are predicates on the skyline of one castle: unimodal, Ferrers, palindromic, Dyck-path, rainbow, hook. The 42 types from the upstream catalogue are all of this kind, and they are organized into seven structural axes on [[castle-classification-geometric](pages/castle-classification-geometric.md)].
- **Non-geometric types** classify by something not read off the shape. A **growth type** (Axis 8) belongs to a *class* of castles defined by a construction rule, and is the growth constant of its count along a stated size axis - golden, silver, tribonacci, supergolden. A **spectral type** (Axis 9) belongs to an individual castle but is read from the spectrum of its polyomino graph - tree, golden-spectrum, isospectral, Ramanujan. **Compressibility** is read from the length of the shortest description that produces the castle. These are on [[castle-classification-non-geometric](pages/castle-classification-non-geometric.md)].

The two kinds interact. A geometric predicate defines a class, and that class has a growth type: the height-2 tree castles (a geometric ban on adjacent raised columns) are a golden width growth castle. A spectral predicate can coincide with a geometric one: the tree-castle condition "no `2×2` filled block" is both. The wiki's convention is that a statement linking a type of one kind to a type of the other is a theorem, not a definition, and is written down as such.

**Parity.** Project Euler 502 (PE 502) requires an even number of blocks. Each type is defined without reference to that clause, and the even-block projector `(A ± P)/2` ([[castle-sign](pages/castle-sign.md)]) is applied on top when needed.[^1] The clause is not independent of typing, though: a convex (unimodal) castle of height `h` has exactly `h` blocks, one per row, so every convex castle has the block parity of `h` and the projector keeps all of them or none.[^2] Whether a type's parity-projected count has the same shape as its full count is one of the three questions below.

## Upstream source

The type catalogue is hydrated from `charlesreid1.com/wiki/Project_Euler/502/Castle_Types` (fetched 2026-09-15; wikitext cached at `raw/castle-types.wiki`). That page defines 42 types - **7 base types** drawn from the polyomino literature (column-convex, unimodal, directed, parallelogram, Ferrers, staircase, m-disparate) and **35 proposed types** aggregated from adjacent literature or newly defined.[^3] The upstream page states the types as skyline predicates only; the geometric page organizes them into structural axes and ties each to the wiki thread that already touches it. The non-geometric axes are the wiki's own.

## What "classification" gives you

Three questions attach to every type:

1. **Is it counted?** Does the wiki already have a count (exact formula, generating function, or algorithm) for the type?
2. **What is its count's shape?** Growth constant, C-finite / algebraic / transcendental character, Online Encyclopedia of Integer Sequences (OEIS) identification if any.
3. **How does it interact with the parity clause?** Does the parity-projected version have the same shape, or is parity locked out by the type's structure?

Every open (2) is a seminar topic; every open (3) is a research thread. Question (2) is where the geometric and non-geometric pages meet: answering it for a geometric type places that type's class on Axis 8.

## Map of the axes

| Axis | Kind | Predicates on | Examples | Page |
|---|---|---|---|---|
| 1 Convexity / modality | geometric | skyline extrema | unimodal, k-modal, valley | [[castle-classification-geometric](pages/castle-classification-geometric.md)] |
| 2 Rate of change | geometric | adjacent differences | m-smooth, m-disparate, plateau-free | same |
| 3 Path-like | geometric | skyline as lattice path | Dyck-path, Motzkin-path | same |
| 4 Symmetry | geometric | skyline symmetries | palindromic, centrally symmetric, self-conjugate | same |
| 5 Extremum | geometric | where `h` and 1 occur | single-summit, twin-peak, rainbow, hook | same |
| 6 Parity / area | geometric | `∑ c_i`, peak count | even-area, even-peak | same |
| 7 Value patterns | geometric | height multiset / pattern | two-level, crenellated, linear | same |
| 8 Growth type | non-geometric | a class's count sequence | golden / silver width growth castle, tribonacci area growth castle | [[castle-classification-non-geometric](pages/castle-classification-non-geometric.md)] |
| 9 Spectral | non-geometric | the castle graph's spectrum | tree, golden-spectrum, isospectral, Ramanujan | same |
| Compressibility | non-geometric | description length | parametric, rule-generated, generic | [[castle-compression](pages/castle-compression.md)] |

## Open threads

The taxonomy makes explicit which sub-families the wiki has, which are candidates, and which are open. The largest open groupings, in rough order of tractability; each page carries the detailed list.

1. **k-modal** for `k ≥ 2` - the parametric family whose `k = 1` case is [[convex-castle](pages/convex-castle.md)] (binomial).
2. **m-smooth / m-disparate** for `m ≥ 2` - a paired family; 1-smooth is strip-counted.
3. **Symmetry types** (palindromic, centrally symmetric, self-conjugate) - untouched.
4. **Rainbow** - direct permutation-classification tie, immediate seminar target for the [[castles-as-upgraded-cycle-count](pages/castles-as-upgraded-cycle-count.md)] triad.
5. **Alternative realizations of the bronze / copper / nickel width growth castles** - the ceiling-exception rule realizes the whole ladder; does any higher rung admit a second, structurally distinct rule the way silver does?
6. **Even-peak** - parity via peak count rather than block count.
7. **Ramanujan castles** - the universal-cover definition is stated; the census over small castles with a `2×2` block has not been run.
8. **Remaining Axis-9 spectral types** - sparse-spectrum, low/high-pass, Ihara-Ramanujan; the S-Division seminar targets on `IDEAS.md`.
9. **Compressibility** - the description-tier axis of [[castle-compression](pages/castle-compression.md)] as a classifier in its own right.

## Related Concepts

- [[castle-classification-geometric](pages/castle-classification-geometric.md)] - the shape-based catalogue: base 7 types and 35 proposed types across Axes 1-7.
- [[castle-classification-non-geometric](pages/castle-classification-non-geometric.md)] - growth-type (Axis 8), spectral (Axis 9), and compressibility classification.
- [[castle-polyomino](pages/castle-polyomino.md)] - the base object.
- [[castle-representations](pages/castle-representations.md)] - the skyline `(c_1, …, c_w)` is the integer-tuple encoding the geometric predicates read.
- [[castle-graph](pages/castle-graph.md)] - the polyomino graph the spectral predicates read.
- [[castle-strip](pages/castle-strip.md)] - the construction-rule object whose growth constant places a class on Axis 8.
- [[castle-sign](pages/castle-sign.md)] - the parity projector applied on top of any type.
- [[convex-castle](pages/convex-castle.md)] - the type whose block count is fixed by its shape.
- [[spectral-analysis](pages/spectral-analysis.md)] - the methods hub paired with the spectral predicates.
- [[castle-compression](pages/castle-compression.md)] - compressibility as a cross-cutting axis.
- [[castle-snippets](pages/castle-snippets.md)] - tested Python one-liners for the geometric predicates and the castle-graph primitives.

## Footnotes

[^1]: raw/castle-types.wiki L1-L9 - "A castle on a w × h grid is determined by its skyline, the sequence of column heights c_1, c_2, …, c_w with 1 ≤ c_i ≤ h and max_i c_i = h. (Problem 502 also requires an even number of blocks; the types below mostly ignore, or independently re-impose, that parity rule.) Every castle is automatically column-convex and bottom-aligned, so each type is a further restriction on the skyline." (Source: https://charlesreid1.com/wiki/Project_Euler/502/Castle_Types, fetched 2026-09-15.)
[^2]: [[oeis-mining-pe502](pages/oeis-mining-pe502.md)] `binomial-vandermonde-identity.md` §1 L25-33 - "#blocks >= max(c) = h, with equality iff the profile is unimodal ... a convex castle of height h has exactly h blocks, and convex castles are exactly the minimum-block castles".
[^3]: raw/castle-types.wiki §"Base types" L11-L19 and §"Proposed additional types" L21-L57 [synthesis] - the 7 base types and the 35 numbered proposed types, all stated as skyline predicates.
