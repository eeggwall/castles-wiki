---
title: Stack polyomino generating function
category: Concepts
summary: A stack polyomino — column heights that weakly rise then weakly fall around a single peak — is a castle tower with one peak. Its OGF `S(z) = ∑_{k≥1} z^k/(1−z^k) · 1/((1−z)(1−z²)···(1−z^{k−1}))²` (OEIS A001523) is built directly by the [[symbolic-method]] from a Durfee-square-style geometric decomposition.
tags: [concept, polyomino, stack-polyomino, generating-functions, symbolic-method, durfee-square, castle-tower]
sources: [analytic-combinatorics-ch1-ogfs]
created: 2026-09-15
updated: 2026-09-22
---

# Stack polyomino generating function

## Description

A **stack polyomino** is the diagram of a composition whose column heights weakly rise to a single peak and then weakly fall: `1 ≤ x_1 ≤ x_2 ≤ … ≤ x_j ≥ x_{j+1} ≥ … ≥ x_ℓ ≥ 1` for some `j, ℓ`.[^1] Read this as a castle-style pile of columns on a common baseline where the skyline is unimodal — a **single-peak tower**. Flajolet & Sedgewick construct its ordinary generating function (OGF) directly by the [[symbolic-method](pages/symbolic-method.md)] (Example I.8, pp. 45-46 of [[analytic-combinatorics-ch1-ogfs](pages/analytic-combinatorics-ch1-ogfs.md)]), from the Durfee-square-style geometric decomposition[^1]

```
Stack ≅ ⋃_{k≥1} ( SEQ_{≥1}(Z^k) × P^{1..k−1} × P^{1..k−1} )
```

— identify the (fixed) peak column of height `k`, prepend a partition with parts `≤ k−1` (the ascending side) and append another (the descending side). Translating each piece into an OGF via the dictionary gives[^1]

```
S(z) = ∑_{k≥1}  z^k/(1 − z^k)  ·  1/((1−z)(1−z²)···(1−z^{k−1}))²

     = z + 2z² + 4z³ + 8z⁴ + 15z⁵ + 27z⁶ + 47z⁷ + 79z⁸ + …
```

= **Online Encyclopedia of Integer Sequences (OEIS) A001523** (unimodal compositions).[^1] Coefficients confirmed against A001523 during ingest.

## The direct castle tie

A **castle tower** — the tower half of the wiki's [[castle-polyomino](pages/castle-polyomino.md)], as counted by the unsigned tower OGF `E_k(x) = 1/(1−(k+1)x)` on [[project-euler-502-representations](pages/project-euler-502-representations.md)] — has strictly more freedom than a stack polyomino: castle blocks can rise and fall repeatedly across width, so the skyline is a general unrestricted composition, not a unimodal one. In other words:

- **Stack polyominoes are the unimodal-skyline sub-family of castle towers.** Every stack polyomino, positioned on a full-width base and constrained to castle heights, is a castle tower with one peak. Not every castle tower is a stack polyomino — a castle whose skyline dips in the middle and rises again is not unimodal.
- **The construction style matches the wiki's approach.** [[column-convex-polyomino](pages/column-convex-polyomino.md)] and the castle both build the polyomino by gluing columns; Example I.8 is exactly this style, executed as a specification rather than an add-a-column functional equation.

This is the closest Analytic Combinatorics (AC)-native construction to the castle we have so far: it treats a castle-like polyomino as a *specification* over classes of columns, and reads the OGF off the specification without ever writing a recurrence.

## Relation to convex-castle counting

The [[convex-castle](pages/convex-castle.md)] enforces a *skyline* unimodality on the castle (the [[convex-castle-binomial-identity](pages/convex-castle-binomial-identity.md)] `C(2H+W−3, W−1)` counts these), which is essentially the stack-polyomino condition plus the castle's own no-overhang / no-same-row-adjacency / even-block rules. The stack-polyomino OGF is thus the natural "unimodal but unweighted, unrestricted heights" reference count against which the convex castle's stricter binomial can be read as a specialization.

## Related asymptotics thread

The book's own note (p. 46) points from Example I.8 forward to Example IX.14 p. 660: **parallelogram polyominoes counted by area give a q-Bessel generating function** — the same q-Bessel / q-Motzkin thread that appears in [[steep-polyominoes-q-motzkin-bessel](pages/steep-polyominoes-q-motzkin-bessel.md)] and [[polyominoes](pages/polyominoes.md)]'s Ferrers-diagram remark on q-Bessel / q-Catalan.[^2] The stack polyomino is thus a middle link between the AC symbolic-method construction of a castle-shaped polyomino and the q-graded asymptotic story that the wiki has begun tracking separately.

## Appearances in Sources

- [[analytic-combinatorics-ch1-ogfs](pages/analytic-combinatorics-ch1-ogfs.md)] — Example I.8 pp. 45-46, "The Durfee square of partitions and stack polyominoes."

## Related Concepts

- [[symbolic-method](pages/symbolic-method.md)] — the method the OGF is derived by.
- [[polyominoes](pages/polyominoes.md)] / [[column-convex-polyomino](pages/column-convex-polyomino.md)] — the taxonomic hosts.
- [[castle-polyomino](pages/castle-polyomino.md)] / [[tower-heap](pages/tower-heap.md)] — the castle tower, of which the stack polyomino is the unimodal-skyline sub-family.
- [[convex-castle](pages/convex-castle.md)] — the castle's own skyline-convex sub-family; a specialization of stack polyominoes to castle rules.
- [[steep-polyominoes-q-motzkin-bessel](pages/steep-polyominoes-q-motzkin-bessel.md)] — the downstream q-Bessel thread the book points to.
- [[generating-functions](pages/generating-functions.md)] — the concept page.
- [[convex-polyomino](pages/convex-polyomino.md)], [[convex-polyomino-by-area](pages/convex-polyomino-by-area.md)] - stacks as the two-bottom-corner convex polyominoes, and their place on the area ladder below parallelogram, directed convex, and convex.

## Footnotes

[^1]: [[analytic-combinatorics-ch1-ogfs](pages/analytic-combinatorics-ch1-ogfs.md)] Example I.8 pp. 45-46 — "A stack polyomino is the diagram of a composition such that for some j, ℓ, one has 1 ≤ x_1 ≤ x_2 ≤ … ≤ x_j ≥ x_{j+1} ≥ … ≥ x_ℓ ≥ 1 ... The diagram representation of stack polyominoes ... translates immediately into the OGF S(z) = ∑_{k≥1} z^k/(1−z^k) · 1/((1−z)(1−z²)···(1−z^{k−1}))² ... a bona fide algorithm for computing the initial values of the number of stack polyominoes (EIS A001523): S(z) = z + 2z² + 4z³ + 8z⁴ + 15z⁵ + 27z⁶ + 47z⁷ + 79z⁸ + ⋯." Values confirmed against OEIS A001523 during ingest.
[^2]: [[analytic-combinatorics-ch1-ogfs](pages/analytic-combinatorics-ch1-ogfs.md)] p.46 — "The book of van Rensburg [592] describes many such constructions and their relation to models of statistical physics, especially polyominoes. For instance, related 'q-Bessel' functions appear in the enumeration of parallelogram polyominoes (Example IX.14, p. 660)."
