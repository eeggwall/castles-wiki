---
title: "Bala (2019) - Triangle stacks of large Schröder type"
category: Sources
summary: Peter Bala's notes on triangle stacks built on a bottom row of k contiguous down triangles instead of the up triangles of A224704; up triangles stand on some, all or none of the down triangles, down triangles fill gaps between neighboring up triangles, and so on. Each such stack is the area under a large Schröder path, which makes the stacks on k down triangles the large Schröder numbers A006318. Splitting a stack by the first step of its path, a flat step (a bare down triangle) or an up-step (a primitive stack, whose next row is full), gives F = 1 + qbd F + G F with G = q²bud F(q, q²bud, u, d), and the continued fraction F = 1/(1 − qbd − q²bud/(1 − q³bud² − q⁴bu²d²/(1 − q⁵bu²d³ − ⋯))); by area alone the stacks are A088352, which had no combinatorial interpretation, and by up and down triangles they have row sums A088354. Ramanujan's Entry 6.3.1 again gives a ratio of q-series and another continued fraction. In castle terms a stack on k down triangles is a keystone castle of width k + 1 with its bottom up triangles removed, so the fraction at b = q, u = d = 1 is A393774 and counts the keystone castles by cells.
tags: [source, notes, oeis, triangle-stack, schroder-path, large-schroder, continued-fraction, ramanujan, q-series, keystone-castle]
sources: [bala-2019-triangle-stacks-large-schroder-type]
created: 2026-10-29
updated: 2026-10-29
---

# Bala (2019) - Triangle stacks of large Schröder type

**Source:** `raw/bala-2019-triangle-stacks-large-schroder-type.pdf` (text layer at `raw/bala-2019-triangle-stacks-large-schroder-type.txt`, extracted with `pdftotext -layout`; the PDF is git-ignored, the text is tracked). P. Bala, "Triangle stacks of large Schröder type", July 30, 2019, an attachment to OEIS A326676, https://oeis.org/A326676/a326676.pdf.[^1] The figures have no text layer, and the continued fractions are read from the PDF.
**Date ingested:** 2026-10-29
**Type:** notes (PDF)

## Notation used on this page

| notes | meaning | castle reading |
|---|---|---|
| `(n, k, k_u, k_d)` stack | `n` triangles, `k` contiguous down triangles in the bottom row, `k_u` up and `k_d` down triangles in all | a keystone castle of width `k + 1` with `n + k + 1` cells, without its bottom up triangles |
| `F(q, b, u, d)` | `Σ q^n b^k u^{k_u} d^{k_d}` over all stacks, the empty stack included | |
| primitive stack, `G` | a stack whose next-to-bottom row has `k` up triangles on the `k` bottom down triangles and the `k − 1` down triangles between them | |

## Summary

**The stacks.** Bala recalls that the stacks of A224704 begin with a bottom row of contiguous up triangles, down triangles may be placed in the gaps between neighboring up triangles, further up triangles on those, and so on. These notes start instead from a bottom row of `k` contiguous down triangles. A stack of large Schröder type is counted up to translation, and its upper boundary is a large Schröder path, a bijection that names the stacks.[^2]

**Primitive stacks.** A primitive stack, `k ≥ 1`, has `k` up triangles resting on the `k` down triangles of its bottom row and no empty position in that next row, so `k − 1` down triangles there as well; its path begins with an up-step and first returns to the x-axis at its end. Removing the bottom row and the `k` up triangles on it leaves a stack on `n − 2k` triangles with `k − 1` down triangles in its bottom row, so `G(q, b, u, d) = q²bud F(q, q²bud, u, d)`.[^3]

**The continued fraction.** A nonempty stack whose path begins with a flat step starts with a down triangle carrying no up triangle, followed by any stack; one whose path begins with an up-step is a primitive stack followed by any stack. So `F = 1 + qbd F + G F`, `F = 1/(1 − qbd − q²bud F(q, q²bud, u, d))`, and iterating,[^4]

```
F(q, b, u, d)  =  1 / (1 − qbd − q²bud / (1 − q³bud² − q⁴bu²d² / (1 − q⁵bu²d³ − q⁶bu³d³ / (1 − ⋯)))).
```

**Specializations.** At `q = u = d = 1` the fraction is a known one for the large Schröder numbers `1, 2, 6, 22, 90, 394, …` (A006318), the bijection between large Schröder paths of semilength `k` and the stacks on `k` down triangles. At `b = u = d = 1` it counts the stacks by area, `1, 1, 2, 3, 5, 9, 16, 28, …`, which Bala identifies with A088352, then without a combinatorial interpretation. At `q = b = 1` it counts them by down and up triangles, an array whose row sums `1, 2, 4, 10, 24, 60, 150, …` are A088354.[^5]

**Ramanujan's Entry 6.3.1.** As in [[bala-2019-area-beneath-small-schroder-paths](pages/bala-2019-area-beneath-small-schroder-paths.md)], Entry 6.3.1 of Ramanujan's lost notebook gives continued fractions for the ratio `g(b; λq)/g(b; λ)`. A substitution turns one of them into the continued fraction of `F`, its other side gives `F` as a ratio `N/D` of q-series, and a second continued fraction follows from another part of the entry.[^6]

## The castle reading

- **A stack on `k` down triangles is a keystone castle without its bottom up triangles.** A keystone castle of width `w`, a castle on the triangular tiling with no overhang, has a full bottom row of `w` up triangles and the `w − 1` down triangles between them, and above it every up triangle rests on a down triangle and every down triangle sits between two up triangles. Removing the `w` bottom up triangles leaves a stack of large Schröder type on `k = w − 1` down triangles, and every such stack comes back by adding them. The castle's outline is `U P D`, with `P` the large Schröder path of the stack, which is why the keystone castles of width `w` number the large Schröder number `r_{w−1}`.
- **The keystone castles by cells.** The castle has `n + k + 1` cells, so the keystone castles by cells have generating function `q F(q, q, 1, 1)`, and at `b = q`, `u = d = 1` Bala's fraction is `1/(1 − q² − q³/(1 − q⁴ − q⁵/(1 − q⁶ − ⋯)))`, the continued fraction of A393774. The keystone castles by cells agree with `q F(q, q, 1, 1)` for up to 60 cells.[^exec]
- **A primitive stack** is a keystone castle whose second row is full, `w − 1` up triangles and the `w − 2` down triangles between them.

## Key Takeaways

- **Stacks on a bottom row of down triangles are the large Schröder paths**, counted by A006318.[^2][^5]
- **`F = 1 + qbd F + GF`**, with the primitive stacks `G = q²bud F(q, q²bud, u, d)`, gives a continued fraction in `q`, `b`, `u` and `d`.[^3][^4]
- **By area the stacks are A088352.**[^5]

## Entities & Concepts

- [[bala-2019-area-beneath-small-schroder-paths](pages/bala-2019-area-beneath-small-schroder-paths.md)] - the stacks on a bottom row of up triangles, A224704.
- [[generating-functions](pages/generating-functions.md)] - the functional equation and the continued fraction.

## Footnotes

[^1]: [[bala-2019-triangle-stacks-large-schroder-type](pages/bala-2019-triangle-stacks-large-schroder-type.md)] title L1-L2 - "TRIANGLE STACKS OF LARGE SCHRÖDER TYPE", "Peter Bala, Jul 30 2019".
[^2]: [[bala-2019-triangle-stacks-large-schroder-type](pages/bala-2019-triangle-stacks-large-schroder-type.md)] §1 pp.1-2 L4-L38 [synthesis] - "The construction of a triangle stack of the type considered in A224704 begins with a bottom row of contiguous up-triangles. Down-triangles may be placed in the gaps between adjacent up-triangles. Further up-triangles may then be placed on these down-triangles and the process continued."; "In these notes we vary the construction of a triangle stack by starting with the bottom row of the stack consisting of contiguous down-triangles."; the `(n, k, k_u, k_d)` stacks; "Two triangle stacks are considered the same if one is mapped onto the other by some translation of the plane."; "There is a bijection between large Schröder paths and triangle stacks of large Schröder type (hence the choice of name)."
[^3]: [[bala-2019-triangle-stacks-large-schroder-type](pages/bala-2019-triangle-stacks-large-schroder-type.md)] §2 pp.2-3 L61-L101 [synthesis] - "We say an (n, k, ku , kd ) triangle stack, with k ≥ 1, is a primitive triangle stack if its next-to-bottom row has k up-triangles resting on the k down- triangles in the bottom row, and has no empty positions (i.e., contains k − 1 down-triangles)."; "A primitive stack corresponds to a large Schröder path that begins with an upstep and makes its first returns to the x-axis at the end of the stack."; the removal of the bottom row with the `k` up triangles on it, `g(n, k, k_u, k_d) = f(n − 2k, k − 1, k_u − k, k_d − k)`, and relation (1).
[^4]: [[bala-2019-triangle-stacks-large-schroder-type](pages/bala-2019-triangle-stacks-large-schroder-type.md)] §3 pp.3-4 L104-L147 [synthesis] - Case 1, "the Schröder path associated with the stack L may begin with a flat step. In this case L begins with a down-triangle (of weight qbd) with no up-triangle resting on it, followed by an arbitrary triangle stack of large Schröder type"; Case 2, an initial primitive stack followed by an arbitrary stack; `F = 1 + qbd F + G F`; the continued fraction (2).
[^5]: [[bala-2019-triangle-stacks-large-schroder-type](pages/bala-2019-triangle-stacks-large-schroder-type.md)] §4 pp.4-5 L149-L188 [synthesis] - "This is a known representation for the generating function of the sequence of large Schröder numbers A006318, and simply reflects the bijection between large Schröder paths of semilength n and triangle stacks of large Schröder type with a bottom row of n down-triangles."; the stacks by area, "The coefficient sequence [1, 1, 2, 3, 5, 9, 16, 28, ...] is already in the OEIS as entry A088352, but without a combinatorial interpretation."; the array by down and up triangles, "The sequence of row sums of the array [1, 2, 4, 10, 24, 60, 150, ...] is A088354."
[^6]: [[bala-2019-triangle-stacks-large-schroder-type](pages/bala-2019-triangle-stacks-large-schroder-type.md)] §5 pp.5-6 L189-L275 [synthesis] - the q-series `g(b; λ)` and "Entry 6.3.1 in Ramanujan's lost notebook (see [1, p. 159]) gives three formal continued fraction expressions for the q -series ratio g(b ; λq)/g(b ; λ)"; the identity (6) and the substitution that turns its right-hand side into (2); the ratio `N/D`, (7)-(9); the continued fraction (10) from (3).
[^exec]: Verified by execution (Python 3.11, 2026-10-29): `bin/python/keystone_castles.py` items [1] and [2], run log `bin/python/keystone_castles-run.log`. The outline `U P D` of every keystone castle of width `w ≤ 6` over the large Schröder paths of semilength `w − 1`; the bottom row of `w` up and `w − 1` down triangles; the keystone castles by cells against `q` times the fraction at `b = q`, `u = d = 1` for up to 60 cells.
