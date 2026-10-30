---
title: "Endicott, May and Shacklette (2018) - Enumeration of stacks of spheres"
category: Sources
summary: Lauren Endicott, Russell May and Sienna Shacklette count stacks of spheres, each sphere resting on four spheres below, by the size of their rectangular base, as a three-dimensional version of Odlyzko and Wilf's fountains of coins. The introduction restates the fountain results - an (n, k) fountain has n coins, k contiguous coins in the bottom row and every higher coin on two coins below; the continued fraction 1/(1 − xy/(1 − x²y/(1 − x³y/…))) counts fountains by coins and bottom row; by bottom row alone they are the Catalan numbers; Wilf's block fountains, one block per row, have generating function (1 − 2y)/(1 − 3y + y²), the odd-indexed Fibonacci numbers. A fountain splits at the first missing coin of its second row, g_m = Σ g_{m'−1} g_{m−m'}. Pyramidal stacks (one rectangle per level) have a rational generating function and a binomial sum; Dominican stacks, built by a split modeled on the fountain split, have an algebraic generating function with a square root. In castle terms a fountain whose bottom row has w coins is a castle on the brick wall, and the block fountains are its convex members.
tags: [source, paper, fountain-of-coins, stacks-of-spheres, catalan, continued-fraction, block-fountain, fibonacci, generating-functions, three-dimensional]
sources: [endicott-may-shacklette-2018-stacks-of-spheres]
created: 2026-10-29
updated: 2026-10-29
---

# Endicott, May and Shacklette (2018) - Enumeration of stacks of spheres

**Source:** `raw/endicott-may-shacklette-2018-stacks-of-spheres.pdf` (text layer at `raw/endicott-may-shacklette-2018-stacks-of-spheres.txt`, extracted with `pdftotext -layout`; the PDF is git-ignored, the text is tracked). L. Endicott, R. May and S. Shacklette, "Enumeration of stacks of spheres", *Involve* 11:5 (2018), 867-875, doi:10.2140/involve.2018.11.867, https://msp.org/involve/2018/11-5/p11.xhtml.[^1] The text layer drops summation signs and stacks some fractions on separate lines; the formulas below are read from the PDF.
**Date ingested:** 2026-10-29
**Type:** paper (PDF)

## Notation used on this page

| paper | meaning | castle reading |
|---|---|---|
| `(n, k)` fountain | `n` coins in rows, `k` contiguous coins in the bottom row, every higher coin sitting on two coins of the row below | a castle on the brick wall with `k` bricks in its bottom row and `n` bricks in all |
| `f_{n,k}` | the number of `(n, k)` fountains | the same castles counted by width and cells |
| `g_k` | the fountains with `k` coins in the bottom row | the brick-wall castles of width `k` |
| `b_k` | the block fountains, every row one contiguous block | the brick-wall castles with one block per row |
| `(ℓ, m, n)` stack | `ℓ` spheres on an `m × n` rectangular base, every higher sphere sitting on four spheres of the level below | |
| `p_{m,n}`, `d_{m,n}` | the pyramidal and the Dominican stacks on an `m × n` base | |

The paper also writes `g_m` in §3 for the block fountains; this page keeps `b_m` for them.

## Summary

**Fountains.** The paper opens with the fountains of coins analyzed by Odlyzko and Wilf (1988): an `(n, k)` fountain is an arrangement of `n` coins in rows whose bottom row is `k` contiguous coins, and every coin in a higher row sits on two coins of the row beneath it. The authors state Odlyzko and Wilf's main result as the continued fraction[^2]

```
F(x, y)  =  Σ_{n,k} f_{n,k} x^n y^k  =  1 / (1 − xy / (1 − x²y / (1 − x³y / (1 − ⋯)))).
```

Counted by the bottom row alone, `G(y) = Σ_k g_k y^k = F(1, y)` satisfies `G(y) − y G(y)² = 1`, so the `g_k` are the Catalan numbers. Wilf's *generatingfunctionology* (Example 2.12) counts the block fountains, in which every row is one contiguous block of coins, with generating function `B(y) = (1 − 2y)/(1 − 3y + y²)`, "the generating function for the Fibonacci numbers with odd indices"; the paper prints that fraction in `x`.[^3] The coefficient of `y^m` is `F_{2m−1}`, with `F_1 = F_2 = 1` and the empty fountain as the constant term, and §3 writes the same number as the sum `Σ_ℓ C(m + ℓ − 1, m − ℓ − 1)`.[^4] Both were checked by execution.[^exec]

**The split at the first missing coin.** A fountain with `m` coins in its bottom row splits at the first position `m'` of its second row where a coin is missing. To the left is a fountain on `m'` coins whose second row is full, so it carries a fountain on `m' − 1` coins; to the right is a fountain on `m − m'` coins. Hence `g_m = Σ_{m'} g_{m'−1} g_{m−m'}`.[^5]

**Stacks of spheres.** An `(ℓ, m, n)` stack is `ℓ` spheres in levels whose bottom level is an `m × n` grid and in which every higher sphere sits on four spheres of the level beneath, as oranges are stacked in grocery stores.[^6]

- *Pyramidal stacks* have one rectangle per level. A pyramidal stack on an `m × n` base is the base alone or the base carrying a pyramidal stack on an `m' × n'` base, `m' < m`, `n' < n`, in one of `(m − m')(n − n')` positions, so `p_{m,n} = 1 + Σ (m − m')(n − n') p_{m',n'}`. This gives
  ```
  P(x, y)  =  Σ p_{m,n} x^m y^n  =  xy(1 − x)(1 − y) / ((1 − x)²(1 − y)² − xy),
  p_{m,n}  =  Σ_{ℓ≥0} C(m + ℓ − 1, m − ℓ − 1) C(n + ℓ − 1, n − ℓ − 1),
  ```
  a sum of `min(m − 1, n − 1)` terms, with Table 1 for `m, n ≤ 7`.[^7] The block-fountain count is the one-factor version of this sum, so the authors call pyramidal stacks a direct generalization of block fountains.[^4]
- *Dominican stacks* generalize the fountain split. A multilevel Dominican stack on an `m × n` base has a column `m'` and a row `n'` with no sphere on the second level; the second level is full over `[1, m'] × [1, n']` and carries a smaller Dominican stack there, the part over `[m' + 1, m] × [n' + 1, n]` is Dominican, and the two remaining regions are single levels. The name comes from the flag of the Dominican Republic, which the pattern resembles seen from above.[^8] The recurrence for `d_{m,n}` turns into a quadratic equation for `D(x, y) = Σ d_{m,n} x^m y^n`, solved by a generating function with a square root, which the authors view as a generalization of the Catalan generating function; Table 2 gives `d_{m,n}` for `m, n ≤ 7`.[^9]

**Further problems.** The square pyramidal stacks have generating function `x(1 − x)³/(1 − 4x + 2x² − x³)`, and "many geometrical variants with triangles, hexagons, etc." give one-variable generating functions. With the base width fixed, the general stacks have `A_1(x) = 1/(1 − x)`, `A_2(x) = x/(1 − 2x)` and `A_3(x) = x(1 − x)/(1 − 5x + 3x²)`. The enumeration of general stacks is open, and the authors expect it to be harder than the two-dimensional fountains, whose generating function by coins is already a continued fraction.[^10]

## The castle reading

- **A fountain is a castle on the brick wall** ([[brick-wall-castles](pages/brick-wall-castles.md)]). Coins in rows, each higher coin touching two coins below, are bricks laid in running bond, each brick resting on both bricks below it. A fountain whose bottom row has `w` coins is a brick-wall castle of width `w`, its coins are the castle's cells, and the maximal runs of coins in a row are its blocks. So `g_w = C_w` counts the brick-wall castles of width `w`, and the continued fraction counts them by cells and width; the coefficients agree with enumeration for up to 18 cells.[^exec]
- **Block fountains are convex.** A fountain with one block per row is a brick-wall castle with `h` blocks at height `h`. Sheared onto a square-grid skyline by Thomas and May's slants ([[thomas-may-2022-mountain-counting](pages/thomas-may-2022-mountain-counting.md)]), it becomes a convex castle in the sense of [[convex-castle](pages/convex-castle.md)], a unimodal skyline with `h` blocks at height `h`.
- **The split has the Catalan recurrence.** `g_m = Σ g_{m'−1} g_{m−m'}` is the recurrence of the Catalan numbers, which the first-return decomposition of Dyck words gives on [[dyck-words](pages/dyck-words.md)] and [[catalan-numbers](pages/catalan-numbers.md)].
- **A stack of spheres is a castle on a two-dimensional base.** Each sphere rests on four spheres below, so a level of a stack plays the part of a row of a castle. A block count for castles on a two-dimensional base, the number of connected components of each level, is on [[image-as-castle](pages/image-as-castle.md)].

## Key Takeaways

- **Fountains by bottom row are the Catalan numbers**, and by coins and bottom row they are the coefficients of Odlyzko and Wilf's continued fraction.[^2][^3]
- **Block fountains are the odd-indexed Fibonacci numbers**, `(1 − 2y)/(1 − 3y + y²)`.[^3]
- **A fountain splits at the first missing coin of its second row**, and the Dominican stacks carry that split to three dimensions.[^5][^8]
- **Pyramidal stacks have a rational generating function and Dominican stacks an algebraic one**; general stacks are open.[^7][^9][^10]

## Entities & Concepts

- [[brick-wall-castles](pages/brick-wall-castles.md)] - the fountains of coins as castles on the brick wall.
- [[catalan-numbers](pages/catalan-numbers.md)] - the fountains counted by bottom row.
- [[dyck-words](pages/dyck-words.md)] - the first-return decomposition behind the recurrence of the split.
- [[convex-castle](pages/convex-castle.md)] - the block fountains, sheared onto the square grid.
- [[generating-functions](pages/generating-functions.md)] - the continued fraction, the rational `P(x, y)` and the algebraic `D(x, y)`.
- [[image-as-castle](pages/image-as-castle.md)] - a block count for castles on a two-dimensional base.

## Relation to Other Wiki Pages

[[thomas-may-2022-mountain-counting](pages/thomas-may-2022-mountain-counting.md)] continues this paper with the general stacks, which it calls mountains, by slicing them into fountains. [[paule-prodinger-2003-fountains-histograms-q-identities](pages/paule-prodinger-2003-fountains-histograms-q-identities.md)] counts fountains by coins through the 1-histograms.

## Footnotes

[^1]: [[endicott-may-shacklette-2018-stacks-of-spheres](pages/endicott-may-shacklette-2018-stacks-of-spheres.md)] title page and p.867 L1-L25 [synthesis] - "Enumeration of stacks of spheres", "Lauren Endicott, Russell May and Sienna Shacklette", "2018 vol. 11, no. 5", "INVOLVE 11:5 (2018)", "dx.doi.org/10.2140/involve.2018.11.867", "(Communicated by Glenn Hurlbert)".
[^2]: [[endicott-may-shacklette-2018-stacks-of-spheres](pages/endicott-may-shacklette-2018-stacks-of-spheres.md)] §1 p.867 L35-L53 - "Odlyzko and Wilf [1988] analyzed fountains of coins. An (n, k) fountain is an arrangement of n coins into rows so that the bottom row consists of k contiguous coins and each coin in higher rows sits on two coins in the row beneath it."; "Their goal was to enumerate the numbers f n,k of (n, k) fountains, and their main result was that the bivariate generating function F(x, y) = n,k f n,k x n y k was the continued fraction", displayed as (1).
[^3]: [[endicott-may-shacklette-2018-stacks-of-spheres](pages/endicott-may-shacklette-2018-stacks-of-spheres.md)] §1 p.867 L54-L65 - "If the fountains are enumerated only by the number of coins in the bottom row, gk = n f n,k , then the generating function G(y) = k gk y k = F(1, y) is much simpler. It is straightforward from (1) that the generating function satisfies G(y)− yG 2 (y) = 1, and so the gk are the Catalan numbers. Wilf [2006, Example 2.12] also considered a restricted class of “block” fountains having the property that each row must be a contiguous block of coins. If bk is the number of block fountains with k coins in the bottom row, then B(y) = k bk y k turns out to be (1 − 2x)/(1 − 3x + x 2 ), which is the generating function for the Fibonacci numbers with odd indices."
[^4]: [[endicott-may-shacklette-2018-stacks-of-spheres](pages/endicott-may-shacklette-2018-stacks-of-spheres.md)] §3 p.871 L244-L250 [synthesis] - the number of block fountains with `m` coins in the bottom row is a Fibonacci number with odd index, "also expressible as the sum" `Σ_ℓ C(m + ℓ − 1, m − ℓ − 1)`; "Therefore, pyramidal stacks of spheres can be viewed as a direct generalization of block fountains of coins."
[^5]: [[endicott-may-shacklette-2018-stacks-of-spheres](pages/endicott-may-shacklette-2018-stacks-of-spheres.md)] §4 pp.871-872 L258-L275 - "A fountain with m coins in the bottom row can be uniquely decomposed into two subfountains by locating the first position in the second row, say at m 0, where a coin is missing."; "Thus, a general fountain consists of the subfountain on the left with a base of m 0 coins, whose second row is full and so consists of an even smaller subfountain with a diminished base of m 0 − 1 coins, and a subfountain on the right with a base of m − m 0 coins. So, the recurrence relation gm = m 0 gm 0 −1 · gm−m 0 holds for fountains of coins."
[^6]: [[endicott-may-shacklette-2018-stacks-of-spheres](pages/endicott-may-shacklette-2018-stacks-of-spheres.md)] §1 p.868 L90-L95 - "An (`, m, n) stack of spheres is an arrangement of ` spheres into levels so that the bottom level consists of spheres in an m × n rectangular grid and each sphere in higher levels sits on four spheres in the level beneath it."; "In grocery stores, fruits like oranges and cantaloupes are often arranged into such stacks."
[^7]: [[endicott-may-shacklette-2018-stacks-of-spheres](pages/endicott-may-shacklette-2018-stacks-of-spheres.md)] §3 pp.869-871 L156-L243 [synthesis] - the pyramidal stacks, "a stack where each level consists of a single rectangular grid of spheres"; Table 1 of `p_{m,n}` for `m, n ≤ 7`; the second level "can be shifted horizontally to m − m 0 positions and vertically to n − n 0 positions", the recurrence `p_{m,n} = 1 + Σ (m − m')(n − n') p_{m',n'}`, the rational generating function (3) and the binomial sum, "a sum with min(m − 1, n − 1) terms".
[^8]: [[endicott-may-shacklette-2018-stacks-of-spheres](pages/endicott-may-shacklette-2018-stacks-of-spheres.md)] §4 pp.872-873 L276-L330 [synthesis] - the inductive definition of a Dominican stack (a column `m'` and a row `n'` devoid of spheres on the second level; "Bottom left", "Top right", "Bottom right and top left"); "a stack of spheres is called Dominican because of its resemblance to the flag of the Dominican Republic".
[^9]: [[endicott-may-shacklette-2018-stacks-of-spheres](pages/endicott-may-shacklette-2018-stacks-of-spheres.md)] §4 pp.873-874 L331-L378 [synthesis] - Table 2 of `d_{m,n}` for `m, n ≤ 7`; the recurrence (4a)-(4c); "This relation is quadratic in D(x, y) with coefficients that are polynomials in x, y."; the generating function (5) with a radical; "D(x, y) can be viewed as a generalization of the generating function for the Catalan numbers."
[^10]: [[endicott-may-shacklette-2018-stacks-of-spheres](pages/endicott-may-shacklette-2018-stacks-of-spheres.md)] §5 pp.874-875 L380-L413 [synthesis] - the square pyramids with generating function `x(1 − x)³/(1 − 4x + 2x² − x³)`; "Many geometrical variants with triangles, hexagons, etc., can be formed in this manner and result in single-variable generating functions."; `A_1`, `A_2`, `A_3` for general stacks of base width 1, 2, 3; "However, the main problem of enumerating general stacks of spheres remains unsolved."; "since the generating function of a general fountain of coins (based on the total number of coins) in two dimensions is already significant in complexity as a continued fraction, one must expect the generating function of a general stack of spheres in three dimensions to be an order of difficulty harder."
[^exec]: Verified by execution (Python 3.11, 2026-10-29): `bin/python/brick_wall_castles.py` items [1], [2], [5] and [7], run log `bin/python/brick_wall_castles-run.log`. The brick-wall castles of width `w ≤ 10` against their shear and the column sweep; their count by cells and width against the coefficients of the continued fraction for up to 18 cells; the castles with one block per row against `F_{2w−1}`, the coefficients of `(1 − 2y)/(1 − 3y + y²)` and `Σ_ℓ C(w + ℓ − 1, w − ℓ − 1)` for `w ≤ 14`.
