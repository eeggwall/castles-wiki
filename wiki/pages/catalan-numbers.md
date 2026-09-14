---
title: Catalan numbers
category: Concepts
summary: C_n = binomial(2n,n)/(n+1) (1,1,2,5,14,42,…) — the counting sequence of Dyck paths, triangulations, non-crossing structures; refined by the Narayana numbers and q-deformed by the q-Catalan numbers.
tags: [concept, catalan, dyck, narayana, generating-functions, combinatorics]
sources: [catalan-numbers]
created: 2026-09-13
updated: 2026-09-13
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

## Relevance to the castle

Catalan numbers are the reference point for two castle threads:

- **They are refined by the [[narayana-numbers](pages/narayana-numbers.md)]:** `∑_k N(n,k) = C_n` (verified). The castle's [[tower-heap](pages/tower-heap.md)] block-count generating function has the *Narayana polynomial* as numerator, so the Catalan/Narayana structure enters the castle world through the tower — see [[tower-narayana-polynomial](pages/tower-narayana-polynomial.md)].
- **They are q-deformed by the [[q-catalan-numbers](pages/q-catalan-numbers.md)]** (which reduce to `C_n` at `q=1`), one family of which counts parallelogram polyominoes by area — the q-graded direction the castle points toward.

**Why the castle is *not* Catalan.** The ballot/non-crossing constraint is exactly what the castle lacks. A convex castle's ascending front and descending back are chosen *independently*, so its count is **binomial**, not Catalan — the point made precisely on [[convex-castle-binomial-identity](pages/convex-castle-binomial-identity.md)]. Catalan appears in the castle world only where a genuine non-crossing coupling exists (via Narayana, in the tower), never in the natural `(w,h)` counts.

## Appearances in Sources

- Wikipedia, *Catalan number* (cached to `raw/catalan-numbers-wikipedia.md`) — the standard definitions, closed forms, recurrences, generating function, and canonical interpretations.

## Related Concepts

- [[narayana-numbers](pages/narayana-numbers.md)] — the refinement `∑_k N(n,k) = C_n`; where Catalan enters the castle (the tower).
- [[q-catalan-numbers](pages/q-catalan-numbers.md)] — the q-deformation; the area-graded castle thread.
- [[motzkin-numbers](pages/motzkin-numbers.md)] — the up/flat/down cousin.
- [[convex-castle-binomial-identity](pages/convex-castle-binomial-identity.md)] — why the castle count is binomial, not Catalan.

## Footnotes

[^1]: raw/catalan-numbers-wikipedia.md §"Definition and closed forms"/"First values" L9-16 — "C_n = (1/(n+1)) * binomial(2n, n) ... = binomial(2n, n) - binomial(2n, n+1)" and "1, 1, 2, 5, 14, 42, 132, 429, 1430, 4862, 16796"; both closed forms and the values re-verified during ingest. (Source: https://en.wikipedia.org/wiki/Catalan_number)
[^2]: raw/catalan-numbers-wikipedia.md §"Recurrences"/"Generating function"/"Asymptotics" L18-27 — convolution "C_{n+1} = sum_{i=0..n} C_i * C_{n-i}", ratio "C_n = (2(2n-1)/(n+1)) * C_{n-1}", "c(x) = (1 - sqrt(1-4x)) / (2x)" satisfying "c(x) = 1 + x*c(x)^2", "C_n ~ 4^n / (n^(3/2) * sqrt(pi))"; recurrences re-verified during ingest.
[^3]: raw/catalan-numbers-wikipedia.md §"Canonical interpretations" L29-37 — "Dyck words of length 2n ... Balanced parentheses ... Full binary trees with n+1 leaves ... Non-crossing partitions ... Monotonic lattice paths ... not passing above the diagonal ... Triangulations of a convex (n+2)-gon ... 123-avoiding permutations."
