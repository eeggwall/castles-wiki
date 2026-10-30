---
title: "Bala (2019) - The area beneath small Schröder paths"
category: Sources
summary: Peter Bala's notes on the triangle stacks of OEIS A224704 (Paul Tek's sequence), the decompositions of the area beneath a small Schröder path into unit up and down triangles, whose bottom row is a run of contiguous up triangles. Counting stacks by area q, up triangles in the bottom row u and down triangles d, and adapting Odlyzko and Wilf's method for fountains of coins, Bala splits a stack into a primitive stack (the bottom row carries its full complement of down triangles and the next row starts with the matching up triangles) and a remaining stack, which gives F = 1 + FG + qd(F − 1)G and the continued fraction F = 1/(1 − qu/(1 − q²ud − q³ud/(1 − q⁴ud² − q⁵ud²/(1 − ⋯)))). Specializations are A326453, A326454 and the small Schröder numbers A001003. Entry 6.3.1 of Ramanujan's lost notebook gives two more continued fractions and a ratio of q-series N/D, and singularity analysis at the simple zero x_0 = 0.53600 49695… of D gives A224704(n) ~ c x_0^(−n), c = 0.30516 69461…. A last section treats the stacks beneath Dyck paths. In castle terms a stack is a row of keystone castles side by side, so the keystone castles have generating function 1 − 1/F.
tags: [source, notes, oeis, triangle-stack, schroder-path, small-schroder, continued-fraction, ramanujan, q-series, asymptotics, fountain-of-coins, keystone-castle]
sources: [bala-2019-area-beneath-small-schroder-paths]
created: 2026-10-29
updated: 2026-10-29
---

# Bala (2019) - The area beneath small Schröder paths

**Source:** `raw/bala-2019-area-beneath-small-schroder-paths.pdf` (text layer at `raw/bala-2019-area-beneath-small-schroder-paths.txt`, extracted with `pdftotext -layout`; the PDF is git-ignored, the text is tracked). P. Bala, "The area beneath small Schröder paths: Notes on A224704, A326453 and A326454", July 14, 2019, an attachment to OEIS A224704, https://oeis.org/A224704/a224704.pdf.[^1] The figures are drawings without a text layer, and the text layer scatters exponents and continued fractions over several lines; the formulas below are read from the PDF.
**Date ingested:** 2026-10-29
**Type:** notes (PDF)

## Notation used on this page

| notes | meaning | castle reading |
|---|---|---|
| Schröder path | a path from the x-axis back to it, never below it, with steps `(1, 1)`, `(1, −1)` and the flat step `(2, 0)` | the outline of a castle on the triangular tiling |
| small Schröder path | a Schröder path with no flat step on the x-axis | the outline of a triangle stack |
| up / down triangle | the unit triangles with vertices `(x, y), (x + 1, y + 1), (x + 2, y)` and `(x, y), (x − 1, y + 1), (x + 1, y + 1)` | the cells |
| `(n, k, l)` triangle stack | `n` triangles, `k` up triangles in the bottom row, `l` down triangles in all | |
| `F(q, u, d)` | `Σ q^n u^k d^l` over all stacks, the empty stack included | |
| primitive stack, `G(q, u, d)` | a stack whose bottom row has all `k − 1` down triangles and whose next row starts with `k − 1` contiguous up triangles, and their generating function | |

## Summary

**Triangle stacks.** The notes open with the problem Odlyzko and Wilf solved for fountains of coins, whose method Bala follows for the stacks of A224704, contributed by Paul Tek.[^2] A small Schröder path has no flat step on the x-axis, and the small Schröder numbers `s(k) = 1, 1, 3, 11, 45, 197, 903, …` (A001003) count those that end at `(2k, 0)`. The area beneath a small Schröder path decomposes into unit triangles, up and down, and that decomposition is a triangle stack; its bottom row is a sequence of contiguous up triangles.[^3] Weighting an `(n, k, l)` stack by `q^n u^k d^l`, the table of stacks with at most 4 triangles gives

```
F(q, u, d)  =  1 + qu + q²u² + q³(u³ + u²d) + q⁴(u⁴ + 2u³d + u²d) + ⋯.
```

[^4]

**The continued fraction.** A primitive stack has `k ≥ 1` up triangles in its bottom row, the full complement of `k − 1` down triangles between them, and `k − 1` up triangles standing on those. Removing its bottom row of `2k − 1` triangles leaves a stack with `k − 1` up triangles in its bottom row, so `G(q, u, d) = qu F(q, q²ud, d)`.[^5] An arbitrary stack splits where its next-to-bottom row first has a gap: at that point the boundary path either steps down to the x-axis (type 1), and the stack is a primitive stack followed by a stack, or takes a flat step (type 2), and removing the down triangle above that point gives a primitive stack followed by a nonempty stack. The two types contribute `1 + FG` and `qd(F − 1)G`, so[^6]

```
F  =  1 + FG + qd(F − 1)G,
```

and iterating with `G = qu F(q, q²ud, d)` gives, after equivalence transformations,[^7]

```
F(q, u, d)  =  1 / (1 − qu / (1 − q²ud − q³ud / (1 − q⁴ud² − q⁵ud² / (1 − q⁶ud³ − ⋯)))).
```

At `d = 1` this counts stacks by area and bottom row (A326453), at `u = 1` by area and down triangles (A326454), and at `q = d = 1` it is a known continued fraction of the small Schröder numbers, since a small Schröder path to `(2k, 0)` is a stack with `k` up triangles in its bottom row.[^8]

**Ramanujan's continued fractions.** Entry 6.3.1 of Ramanujan's lost notebook, as given by Andrews and Berndt, states three continued fractions for the ratio `g(b; λq)/g(b; λ)` of the q-series `g(b; λ) = Σ_n λ^n q^{n²}/((1 − q)⋯(1 − q^n)(1 + bq)⋯(1 + bq^n))`. With `b → −u`, `λ → −qd/u`, `q → dq²` one of them becomes the continued fraction of `F`, and the other two give two more continued fractions for `F`.[^9] The same entry writes `F` as a ratio of q-series, and at `u = d = 1`[^10]

```
F(q, 1, 1)  =  N(q)/D(q),    N(q) = Σ_n (−1)^n q^{2n² + n} / ((1 − q²)⋯(1 − q^{2n}))²,
                              D(q) = Σ_n (−1)^n q^{2n² − n} / ((1 − q²)⋯(1 − q^{2n}))².
```

**Asymptotics.** `N` and `D` are analytic in the unit disc. The smallest real zero of `D` is `x_0 = 0.53600 49695 29708 61653…`, a simple zero, so `N/D` has a simple pole there, and singularity analysis (Flajolet and Sedgewick, Theorem IV.10) gives `A224704(n) ~ c x_0^{−n}` with `c = −N(x_0)/(x_0 D'(x_0)) = 0.30516 69461 42293…`.[^11]

**Stacks of Dyck type.** The stacks beneath Dyck paths, which have no flat steps, factor as a primitive stack followed by a stack, so `F_D = 1 + F_D G_D` with `G_D = qu F_D(q, q²ud, d)`, and `F_D = 1/(1 − qu/(1 − q³ud/(1 − q⁵ud²/(1 − ⋯))))`; at `d = 1` this is A239927 and at `q = 1` A227543.[^12]

## The castle reading

- **A stack is a row of keystone castles.** A down triangle in a stack sits between two up triangles of its row, and an up triangle above the bottom row rests on a down triangle, which is no overhang on the triangular tiling ([[keystone-castles](pages/keystone-castles.md)]). Where the boundary path returns to the x-axis, the bottom row has no down triangle between two neighboring up triangles, and the stack falls into pieces there. Each piece has a full bottom row, `k` up triangles and the `k − 1` down triangles between them, and is a keystone castle of width `k`. So `F = 1/(1 − K)`, with `K(q, u, d)` the keystone castles counted by cells, width and down triangles, and Bala's continued fraction gives

  ```
  K  =  1 − 1/F  =  qu / (1 − q²ud − q³ud / (1 − q⁴ud² − q⁵ud² / (1 − ⋯))).
  ```

  At `u = d = 1` this is `q` times the continued fraction of A393774, and the keystone castles by cells, `1, 0, 1, 1, 1, 2, 2, 4, 5, 7, 11, 15, …` from one cell, agree with `1 − 1/F` and with the A224704 data.[^exec]
- **Growth by cells.** `K = 1 − D/N` is meromorphic in the unit disc, with its poles at the zeros of `N`. The smallest positive zero of `N` is `y_0 = 0.68364 40770…`, and the keystone castles with `n + 1` and `n` cells have ratio `1.46274945` at `n = 99, 149, 199`, which is `1/y_0`.[^exec] The stacks grow faster, at `1/x_0 = 1.86565…`, because a stack is any sequence of keystone castles.
- **A primitive stack** is a keystone castle whose second row holds every up triangle it can, one on each of the `k − 1` down triangles of the bottom row.
- **Fountains.** The method is Odlyzko and Wilf's for fountains of coins, the castles on the brick wall of [[brick-wall-castles](pages/brick-wall-castles.md)]: each splits off an initial piece whose second row is full.

## Key Takeaways

- **Triangle stacks are the areas beneath small Schröder paths**, with a bottom row of contiguous up triangles.[^3]
- **`F = 1 + FG + qd(F − 1)G`**, solved by a continued fraction in `q`, `u` and `d`.[^6][^7]
- **Ramanujan's Entry 6.3.1** gives two more continued fractions and the ratio `N/D` of q-series.[^9][^10]
- **`A224704(n) ~ c x_0^{−n}`**, `x_0 = 0.53600…` the smallest zero of `D`.[^11]

## Entities & Concepts

- [[keystone-castles](pages/keystone-castles.md)] - the stacks with a full bottom row, of which every stack is a sequence.
- [[brick-wall-castles](pages/brick-wall-castles.md)] - the fountains of coins, whose continued fraction the method adapts.
- [[generating-functions](pages/generating-functions.md)] - the functional equation, the continued fractions and the ratio of q-series.

## Relation to Other Wiki Pages

[[bala-2019-triangle-stacks-large-schroder-type](pages/bala-2019-triangle-stacks-large-schroder-type.md)] builds the stacks on a bottom row of down triangles instead, which are the keystone castles with their bottom up triangles removed. [[endicott-may-shacklette-2018-stacks-of-spheres](pages/endicott-may-shacklette-2018-stacks-of-spheres.md)] and [[paule-prodinger-2003-fountains-histograms-q-identities](pages/paule-prodinger-2003-fountains-histograms-q-identities.md)] state the fountain results the method follows.

## Footnotes

[^1]: [[bala-2019-area-beneath-small-schroder-paths](pages/bala-2019-area-beneath-small-schroder-paths.md)] title L1-L5 - "The area beneath small Schröder paths: Notes", "on A224704, A326453 and A326454", "Peter Bala, Jul 14 2019".
[^2]: [[bala-2019-area-beneath-small-schroder-paths](pages/bala-2019-area-beneath-small-schroder-paths.md)] abstract p.1 L6-L12 - "Odlyzko and Wilf [3] found an elegant continued fraction representation for the generating function of the number of fountains of coins using n coins. By following the author's methods we obtain a continued fraction representation for the generating function of the number of stacks of n triangles (sequence A224704, contributed by Paul Tek)."
[^3]: [[bala-2019-area-beneath-small-schroder-paths](pages/bala-2019-area-beneath-small-schroder-paths.md)] §1 pp.1-2 L13-L43 [synthesis] - the Schröder path and its steps, "A small Schröder path is a Schröder path with no flat steps on the x-axis."; the small Schröder numbers `s(k)` (A001003); "The area between a small Schröder path and the x-axis can be decomposed into triangles each of unit area. We call such a decomposition of the area a triangle stack."; the up and down triangles; "Note that a triangle stack has a sequence of contiguous up triangles in its bottom row."
[^4]: [[bala-2019-area-beneath-small-schroder-paths](pages/bala-2019-area-beneath-small-schroder-paths.md)] §1 p.2 L45-L97 [synthesis] - the `(n, k, l)` stacks, the weight `q^n u^k d^l`, `F(q, u, d)`, "We assign a weight of 1 to the empty triangle stack (n = 0)."; the table of stacks for `n = 1, …, 4` and the first terms of `F`.
[^5]: [[bala-2019-area-beneath-small-schroder-paths](pages/bala-2019-area-beneath-small-schroder-paths.md)] §2 p.4 L155-L181 - "We define a primitive (n, k, l) triangle stack to be an (n, k, l) triangle stack such that its next-to bottom row begins with k−1 contiguous up triangles. A primitive (n, k, l) triangle stack thus has k ≥ 1 contiguous up triangles in its bottom row and in the spaces between these lie the full complement of k − 1 down triangles on which stand k − 1 up triangles."; "Removing the bottom row consisting of k up triangles and k − 1 down triangles from a primitive (n, k, l) triangle stack yields a triangle stack on n − (k + k − 1) triangles having k − 1 up triangles in its bottom row"; relation (3).
[^6]: [[bala-2019-area-beneath-small-schroder-paths](pages/bala-2019-area-beneath-small-schroder-paths.md)] §2 pp.5-7 L183-L254 [synthesis] - the split of a stack where its next-to-bottom row of `r − 1` up triangles ends: "either (1) a down step to the x-axis as in Figure 1 - in this case we refer to the stack T as a type 1 triangle stack, or (2) a flat step as in Figure 2"; the type-1 contribution, "the coefficient of the term q n uk dl in the series 1 + F G"; for type 2 "we replace the flat step at the lattice point (2r − 1, 1) with a down step to the x-axis and discard the down triangle above this point", contributing `qd(F − 1)G`; the functional relation (7).
[^7]: [[bala-2019-area-beneath-small-schroder-paths](pages/bala-2019-area-beneath-small-schroder-paths.md)] §2 pp.7-8 L255-L282 [synthesis] - the rewriting of (7) by (3) and an equivalence transformation, "Succesive iterations of the above identity lead to the formal continued fraction expansion", and the sign change of the partial denominators that gives (8).
[^8]: [[bala-2019-area-beneath-small-schroder-paths](pages/bala-2019-area-beneath-small-schroder-paths.md)] §1 p.3 L116-L143 [synthesis] - `d = 1`, "See A326453."; `u = 1`, "See A326454."; `q = d = 1`, "but this is simply a (known) representation of the generating function for the small Schröder numbers A001003, since a small Schröder path from the origin to the point (2k, 0) on the x-axis gives rise to a triangle stack with k contiguous up triangles in its bottom row and vice versa."
[^9]: [[bala-2019-area-beneath-small-schroder-paths](pages/bala-2019-area-beneath-small-schroder-paths.md)] §3 pp.8-9 L285-L337 [synthesis] - the q-series `g(b; λ)`; "Entry 6.3.1 in Ramanujan's lost notebook (see [1, p.159]) gives three formal continued fraction expressions for the ratio of q -series g(b; λq)/g(b; λ)"; the substitution that turns (10) into (8); the continued fractions (12) and (13).
[^10]: [[bala-2019-area-beneath-small-schroder-paths](pages/bala-2019-area-beneath-small-schroder-paths.md)] §3 p.9 L338-L375 [synthesis] - "Entry 6.3.1 also provides us with a representation for the generating function F (q, u, d) as a ratio of q -series"; `N(q, u, d)` (14) and `D(q, u, d)` (15); the specialization `u = d = 1`, (16).
[^11]: [[bala-2019-area-beneath-small-schroder-paths](pages/bala-2019-area-beneath-small-schroder-paths.md)] §3 pp.9-10 L377-L396 - "The functions N (q) and D(q) are analytic inside the unit disc. Calculation shows that the smallest real zero of the denominator series D(q) is located at x0 = 0.53600 49695 29708 61653"; "and is a simple zero"; "Singularity analysis [2, Theorem IV.10, p. 248] applied to the function N (q)/D(q) produces the asymptotic estimate"; (17), (18); "Calculation gives the value c = 0.30516 69461 42293".
[^12]: [[bala-2019-area-beneath-small-schroder-paths](pages/bala-2019-area-beneath-small-schroder-paths.md)] §4 pp.10-11 L398-L451 [synthesis] - "We call the triangle stack formed by the area between a Dyck path and the x-axis a triangle stack of Dyck type."; (20), "A primitive triangle stack of Dyck type factorises uniquely into an initial primitive triangle stack followed by a (possibly empty) triangle stack.", (21), the continued fraction (22); "See entry A239927 in the OEIS."; "See entry A227543."
[^exec]: Verified by execution (Python 3.11, 2026-10-29): `bin/python/keystone_castles.py` items [4] and [10], run log `bin/python/keystone_castles-run.log`. The keystone castles by cells, from a sweep over their outlines, against the data of A393774, `1/(1 − K)` against the data of A224704 and against Bala's continued fraction at `u = d = 1` for up to 60 cells; the smallest positive zero of `N(q)` by bisection, and the ratios of the counts at 100, 150 and 200 cells.
