---
title: Catalan numbers
category: Concepts
summary: C_n = binomial(2n,n)/(n+1) (1,1,2,5,14,42,…) — the counting sequence of Dyck paths, triangulations, non-crossing structures; refined by the Narayana numbers and q-deformed by the q-Catalan numbers. Canonical symbolic-method example: `G = Z × SEQ(G)` → `G(z) = (1−√(1−4z))/2`.
tags: [concept, catalan, dyck, narayana, generating-functions, combinatorics, symbolic-method]
sources: [catalan-numbers, analytic-combinatorics-ch1-ogfs]
created: 2026-09-13
updated: 2026-09-19
---

# Catalan numbers

> Hydrated from [Wikipedia: Catalan number](https://en.wikipedia.org/wiki/Catalan_number); all formulas and values re-verified during ingest.

## Description

The **Catalan numbers** `C_n` are one of the most ubiquitous sequences in enumerative combinatorics:[^1]

```
C_n = binomial(2n, n) / (n+1) = binomial(2n, n) − binomial(2n, n+1)
    = 1, 1, 2, 5, 14, 42, 132, 429, 1430, 4862, 16796, …   (n = 0, 1, 2, …)
```

(the second closed form makes integrality manifest). They satisfy a **convolution recurrence** `C_{n+1} = Σ_{i=0}^{n} C_i C_{n−i}` (`C_0 = 1`) and a **ratio recurrence** `C_n = 2(2n−1)/(n+1) · C_{n−1}`, with generating function `c(x) = (1 − √(1−4x))/(2x)` (the root of `c = 1 + x c²`) and growth `C_n ~ 4^n / (n^{3/2}√π)`.[^2] All re-verified during ingest.

Canonical objects counted by `C_n` include Dyck words / balanced parentheses of length 2n, monotone lattice paths staying weakly below the diagonal, triangulations of a convex (n+2)-gon, full binary trees with n+1 leaves, non-crossing partitions, and 123-avoiding permutations.[^3] The common thread is a **non-crossing / ballot constraint** — a path or matching that must stay on one side of a boundary.

**Canonical symbolic-method derivation.** The Catalan generating function falls out of a one-line recursive specification for general plane (rooted) trees ([[analytic-combinatorics-ch1-ogfs](pages/analytic-combinatorics-ch1-ogfs.md)] §I.2 pp. 33-35): a plane tree is a node with a possibly-empty sequence of subtrees, so `G = Z × SEQ(G)`, which the [[symbolic-method](pages/symbolic-method.md)] translates directly to `G(z) = z/(1 − G(z))`; solving the quadratic `G − G² − z = 0` gives `G(z) = ½(1 − √(1−4z)) = z + z² + 2z³ + 5z⁴ + 14z⁵ + 42z⁶ + …`, so `G_n = C_{n−1}`.[^4] "Catalan tree" is used synonymously with "general (rooted, unlabelled) plane tree." The same specification underlies triangulations (`T = ε + T × ∇ × T`) and, generalizing the alphabet, the castle's [[generalized-dyck-grammar](pages/generalized-dyck-grammar.md)] — the castle grammar is a first-return specification in exactly this style, with a third letter.

## Relevance to the castle

Catalan numbers are the reference point for two castle threads:

- **They are refined by the [[narayana-numbers](pages/narayana-numbers.md)]:** `∑_k N(n,k) = C_n` (verified). The castle's [[tower-heap](pages/tower-heap.md)] block-count generating function has the *Narayana polynomial* as numerator, so the Catalan/Narayana structure enters the castle world through the tower — see [[tower-narayana-polynomial](pages/tower-narayana-polynomial.md)].
- **They are q-deformed by the [[q-catalan-numbers](pages/q-catalan-numbers.md)]** (which reduce to `C_n` at `q=1`), one family of which counts parallelogram polyominoes by area — the q-graded direction the castle points toward.

**Why the castle is *not* Catalan.** The ballot/non-crossing constraint is exactly what the castle lacks. A convex castle's ascending front and descending back are chosen *independently*, so its count is **binomial**, not Catalan — the point made precisely on [[convex-castle-binomial-identity](pages/convex-castle-binomial-identity.md)]. Catalan appears in the castle world only where a genuine non-crossing coupling exists (via Narayana, in the tower), never in the natural `(w,h)` counts.

## Appearances in Sources

- Wikipedia, *Catalan number* (cached to `raw/catalan-numbers-wikipedia.md`) — the standard definitions, closed forms, recurrences, generating function, and canonical interpretations.
- [[analytic-combinatorics-ch1-ogfs](pages/analytic-combinatorics-ch1-ogfs.md)] — §I.2 pp. 33-35 gives the canonical symbolic-method derivation `G = Z × SEQ(G)` → `G(z) = (1−√(1−4z))/2`; Figure I.2 p.20 recounts the prehistory (Euler, Segner, Lamé, Catalan).

## Related Concepts

- [[narayana-numbers](pages/narayana-numbers.md)] — the refinement `∑_k N(n,k) = C_n`; where Catalan enters the castle (the tower).
- [[q-catalan-numbers](pages/q-catalan-numbers.md)] — the q-deformation; the area-graded castle thread.
- [[motzkin-numbers](pages/motzkin-numbers.md)] — the up/flat/down cousin.
- [[convex-castle-binomial-identity](pages/convex-castle-binomial-identity.md)] — why the castle count is binomial, not Catalan.
- [[symbolic-method](pages/symbolic-method.md)] — the framework that gives the tree-spec → Catalan-ordinary generating function (OGF) derivation in one line.

## Footnotes

[^1]: raw/catalan-numbers-wikipedia.md §"Definition and closed forms"/"First values" L9-16 — "C_n = (1/(n+1)) * binomial(2n, n) ... = binomial(2n, n) - binomial(2n, n+1)" and "1, 1, 2, 5, 14, 42, 132, 429, 1430, 4862, 16796"; both closed forms and the values re-verified during ingest. (Source: https://en.wikipedia.org/wiki/Catalan_number)
[^2]: raw/catalan-numbers-wikipedia.md §"Recurrences"/"Generating function"/"Asymptotics" L18-27 — convolution "C_{n+1} = sum_{i=0..n} C_i * C_{n-i}", ratio "C_n = (2(2n-1)/(n+1)) * C_{n-1}", "c(x) = (1 - sqrt(1-4x)) / (2x)" satisfying "c(x) = 1 + x*c(x)^2", "C_n ~ 4^n / (n^(3/2) * sqrt(pi))"; recurrences re-verified during ingest.
[^3]: raw/catalan-numbers-wikipedia.md §"Canonical interpretations" L29-37 — "Dyck words of length 2n ... Balanced parentheses ... Full binary trees with n+1 leaves ... Non-crossing partitions ... Monotonic lattice paths ... not passing above the diagonal ... Triangulations of a convex (n+2)-gon ... 123-avoiding permutations."
[^4]: [[analytic-combinatorics-ch1-ogfs](pages/analytic-combinatorics-ch1-ogfs.md)] §I.2 pp. 33-35 — "The recursive specification of general trees leads to an implicit definition of their OGF, G = Z × SEQ(G) ⟹ G(z) = z/(1−G(z)) ... G − G² − z = 0 ... G(z) = ½(1 − √(1−4z)) = z + z² + 2z³ + 5z⁴ + 14z⁵ + 42z⁶ + 132z⁷ + 429z⁸ + ⋯ = ∑_{n≥1} (1/n)C(2n−2,n−1) z^n ... For this reason the term Catalan tree is often employed as synonymous to 'general (rooted unlabelled plane) tree'."
