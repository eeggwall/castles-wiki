---
title: "Paule and Prodinger (2003) - Fountains, histograms, and q-identities"
category: Sources
summary: Peter Paule and Helmut Prodinger's note on Merlini and Sprugnoli's count of fountains and histograms. A p-histogram is a sequence of columns whose first column has height 1 to p and each column at most p higher than the one before; the fountains of coins are equivalent to the 1-histograms, and Merlini and Sprugnoli counted the p-histograms by area in two forms, through polynomials D_m and E_m with E_n = E_{n−1} − q^n E_{n−p}, and as a quotient of two q-series. The note solves the recursion S_n = S_{n−1} + t q^{n−p} S_{n−p} with noncommuting variables x η = q η x, gives E_n and D_n as explicit sums of q-binomial coefficients, so the limits are the two series, and verifies the recurrences with certificates from Riese's qZeil. Checked by execution, the displayed quotient at parameter p is 1 plus the area generating function of the histograms whose columns rise by at most p − 1, so the fountains by coins are its case p = 2, Σ (−1)^k q^{k(k+1)}/(q)_k over Σ (−1)^k q^{k²}/(q)_k. In castle terms a 1-histogram is the sheared skyline of a castle on the brick wall.
tags: [source, paper, fountain-of-coins, histogram, q-series, q-binomial, schur-polynomials, area, computer-algebra, continued-fraction]
sources: [paule-prodinger-2003-fountains-histograms-q-identities]
created: 2026-10-29
updated: 2026-10-29
---

# Paule and Prodinger (2003) - Fountains, histograms, and q-identities

**Source:** `raw/paule-prodinger-2003-fountains-histograms-q-identities.pdf` (text layer at `raw/paule-prodinger-2003-fountains-histograms-q-identities.txt`, extracted with `pdftotext -layout`; the PDF is git-ignored, the text is tracked). P. Paule and H. Prodinger, "Fountains, histograms, and q-identities", *Discrete Mathematics and Theoretical Computer Science* 6 (2003), 101-106, doi:10.46298/dmtcs.336, https://dmtcs.episciences.org/336.[^1] The text layer scatters the exponents of the q-series over several lines; the formulas below are read from the PDF.
**Date ingested:** 2026-10-29
**Type:** paper (PDF)

## Notation used on this page

| note | meaning |
|---|---|
| fountain with `n` coins | coins in rows, each coin in a higher row touching exactly two coins in the next lower row |
| `p`-histogram | a sequence of columns, the first of height `r` with `1 ≤ r ≤ p`, each column of height at most `k + p` when the one before has height `k` |
| `f_n^{[p]}`, `F^{[p]}(q)` | the `p`-histograms of area `n`, and their generating function `Σ_n f_n^{[p]} q^n` |
| `(x)_n` | `(1 − x)(1 − xq)⋯(1 − xq^{n−1})`, so `(q)_k = (1 − q)⋯(1 − q^k)` |
| `[n k]` | the q-binomial coefficient `(q)_n/((q)_k (q)_{n−k})` |

## Summary

**Fountains and histograms.** The note reviews Merlini and Sprugnoli's *Fountains and histograms* (J. Algorithms 44, 2002). A fountain with `n` coins is an arrangement of `n` coins in rows such that each coin in a higher row touches exactly two coins in the next lower row. A `p`-histogram is a sequence of columns in which the first column has height `r` with `1 ≤ r ≤ p` and each column is at most `p` higher than the one before. The note states that counting the coins in a fountain is equivalent to counting the 1-histograms, and that Merlini and Sprugnoli count the `p`-histograms by area, the number of cells, in two forms: as a limit `lim_{m→∞} D_m/E_m` of a ratio of polynomials, and as the quotient[^2]

```
Σ_{k≥0} (−1)^k q^{p C(k+1, 2)} / (q)_k   ⁄   Σ_{k≥0} (−1)^k q^{k + p C(k, 2)} / (q)_k.
```

Merlini had asked for a direct argument that the two answers coincide, which is the subject of the note.[^2]

**The polynomials.** For fixed `p ≥ 1`,

```
E_n = E_{n−1} − q^n E_{n−p}  (n ≥ p),   E_0 = ⋯ = E_{p−1} = 1,
D_n = D_{n−1} − q^n D_{n−p}  (n ≥ p),   D_i = 1 − Σ_{j=1}^{i} q^j  (i = 0, …, p − 1),
```

which the note compares with Schur's polynomials, the case `p = 2`, `q = −1`. The two series of the quotient are the limits `E_∞` and `D_∞` that Merlini and Sprugnoli wanted proved.[^3]

**The method.** The note solves the generic recursion `S_n = S_{n−1} + t q^{n−p} S_{n−p}` with arbitrary initial values, a recursion that Andrews studied for `p = 2` in the context of Schur polynomials, and mentions Cigler's independent combinatorial method for such recursions. Lemma 1 expands `(x + x^p η)^n` for noncommuting variables with `x η = q η x`, as a sum of q-binomial coefficients times powers of `q`; reading `η` as the operator `f(x) ↦ f(qx)` turns the recursion into an equation for `F(x) = Σ S_n x^n`, and the lemma solves it.[^4] With `t = −q^p` this gives

```
E_n = Σ_{k≥0} [n − (p − 1)k  k] q^{p C(k+1, 2)} (−1)^k,
D_n = Σ_{k≥0} [n − (p − 1)(k − 1)  k] q^{k + p C(k, 2)} (−1)^k,
```

from which the limits `E_∞` and `D_∞` are immediate; a telescoping lemma, Lemma 2, rewrites `D_n` as `1 − Σ_k (−1)^k q^{p C(k+1, 2)} q^{k+1} [n − (p − 1)k  k + 1]`.[^5]

**Computer algebra.** From the two sum representations, Riese's package qZeil returns the recurrences `S_n = S_{n−1} − q^n S_{n−p}` for each fixed `p`, with a certificate function that makes the proof a check of rational functions; the pattern for general `p` is guessed from `p = 1, 2, 3`, and Theorem 3.1 states it for `E_n`.[^6]

**Which histograms the quotient counts.** Checked by execution, the displayed quotient at parameter `p` is 1 plus the area generating function of the histograms whose first column has height 1 to `p − 1` and whose columns rise by at most `p − 1`, for `p = 2, 3, 4` and area up to 16, and at `p = 1` the quotient is 1.[^exec] So the 1-histograms, and with them the fountains by coins, are the quotient at `p = 2`:

```
1 + q + q² + 2q³ + 3q⁴ + 5q⁵ + 9q⁶ + ⋯  =  Σ_k (−1)^k q^{k(k+1)} / (q)_k   ⁄   Σ_k (−1)^k q^{k²} / (q)_k,
```

the fountains of `n` coins, A005169.[^exec]

## The castle reading

- **A 1-histogram is a sheared brick-wall castle** ([[brick-wall-castles](pages/brick-wall-castles.md)]). A 1-histogram is a square-grid skyline whose first column has height 1 and whose columns rise by at most 1, the slant heights of a fountain in [[thomas-may-2022-mountain-counting](pages/thomas-may-2022-mountain-counting.md)]. A fountain is a castle on the brick wall, each brick resting on both bricks below ([[endicott-may-shacklette-2018-stacks-of-spheres](pages/endicott-may-shacklette-2018-stacks-of-spheres.md)]), so the area of a 1-histogram is the number of cells of that castle. Mirrored, the 1-histograms are the castles that drop by at most 1 and end at height 1 of [[motzkin-castles](pages/motzkin-castles.md)], and the quotient at `p = 2` counts them by area.
- **The `p`-histograms are castles with bounded rises.** For `p ≥ 2` a `p`-histogram is a square-grid castle whose first column is at most `p` and whose columns rise by at most `p`. Castles counted by area are compositions ([[castle-by-area](pages/castle-by-area.md)]), and the `p`-histograms are the compositions whose first part is at most `p` and whose parts rise by at most `p`.

## Key Takeaways

- **Fountains are 1-histograms**, counted by area.[^2]
- **Two forms for the area count of `p`-histograms**, a limit of polynomial ratios and a quotient of q-series, and the note's explicit q-binomial sums for the polynomials.[^2][^5]
- **The fountains by coins are the quotient at `p = 2`**, `Σ (−1)^k q^{k(k+1)}/(q)_k` over `Σ (−1)^k q^{k²}/(q)_k`.[^exec]

## Entities & Concepts

- [[brick-wall-castles](pages/brick-wall-castles.md)] - the 1-histograms as sheared castles on the brick wall.
- [[thomas-may-2022-mountain-counting](pages/thomas-may-2022-mountain-counting.md)] - the slant heights of a fountain, its 1-histogram.
- [[endicott-may-shacklette-2018-stacks-of-spheres](pages/endicott-may-shacklette-2018-stacks-of-spheres.md)] - fountains of coins and their continued fraction.
- [[motzkin-castles](pages/motzkin-castles.md)] - the mirror images of the 1-histograms.
- [[castle-by-area](pages/castle-by-area.md)] - castles as compositions, counted by area.

## Footnotes

[^1]: [[paule-prodinger-2003-fountains-histograms-q-identities](pages/paule-prodinger-2003-fountains-histograms-q-identities.md)] p.101 L1-L25 [synthesis] - "Discrete Mathematics and Theoretical Computer Science 6, 2003, 101–106", "Fountains, histograms, and q–identities", "Peter Paule1† and Helmut Prodinger2‡", "received Jan 14, 2003, accepted Aug 15, 2003.", the abstract, "Keywords: q–identities, fountains, histograms, Schur polynomials".
[^2]: [[paule-prodinger-2003-fountains-histograms-q-identities](pages/paule-prodinger-2003-fountains-histograms-q-identities.md)] §1 pp.101-102 L30-L66 - "Merlini and Sprugnoli [6] discuss fountains and histograms; for the reader’s convenience, we review a few key issues here."; "A fountain with n coins is an arrangement of n coins in rows such that each coin in a higher row touches exactly two coins in the next lower row."; "A p-histogram is a sequence of columns in which the height of the ( j + 1)st column is at most k + p, if k is the height of column j; the first column has height r, with 1 ≤ r ≤ p."; "It can be shown that the enumeration of coins in a fountain is equivalent with the enumeration of 1-histograms. The paper [6] addresses the enumeration of p-histograms with respect to area (=number of cells)."; the two forms, `lim D_m/E_m` and the displayed quotient; "According to [5], it would be nice to have a direct argument that these two answers coincide. This is the subject of the present note."
[^3]: [[paule-prodinger-2003-fountains-histograms-q-identities](pages/paule-prodinger-2003-fountains-histograms-q-identities.md)] §2 p.102 L68-L91 [synthesis] - the definitions of `E_n` and `D_n`; "They can be compared with the classical Schur polynomials [8], which occur for p = 2 and q = −1. Then Merlini and Sprugnoli want a direct proof of the formulæ", `E_∞` and `D_∞` as the two series of the quotient.
[^4]: [[paule-prodinger-2003-fountains-histograms-q-identities](pages/paule-prodinger-2003-fountains-histograms-q-identities.md)] §2 pp.102-103 L92-L173 [synthesis] - "It should be mentioned that Cigler [4] developed independently a combinatorial method to deal with recursions as ours, but also more general ones."; the generic recursion `S_n = S_{n−1} + t q^{n−p} S_{n−p}`, "For p = 2, these polynomials were studied by Andrews (and others) in the context of Schur polynomials"; the noncommutative variables with `x η = q η x`; Lemma 1 and its proof; "Note that we can alternatively view η as an operator, defined by η f (x) = f (qx)."; the equation for `F(x)`.
[^5]: [[paule-prodinger-2003-fountains-histograms-q-identities](pages/paule-prodinger-2003-fountains-histograms-q-identities.md)] §2 pp.103-104 L174-L266 [synthesis] - the expansion of `F(x)` by Lemma 1 and the explicit formula for `S_n`; "Now we specialize this to our instance. Here, t = −q p"; the sums for `E_n` and `D_n`, "From this, the limit of En is immediate."; Lemma 2 and the telescoping computation of `D_n`.
[^6]: [[paule-prodinger-2003-fountains-histograms-q-identities](pages/paule-prodinger-2003-fountains-histograms-q-identities.md)] §3 p.105 L269-L321 [synthesis] - "if p is chosen as a specific positive integer, Riese’s package qZeil [7] returns the recurrences Sn = Sn−1 − qn Sn−p (n ≥ p) together with a certificate function Cert for independent verification. Despite the fact that for general “generic” integer parameter p there is no algorithm available, a general pattern can be easily guessed from running the algorithm for p = 1, p = 2, and p = 3, say."; Theorem 3.1 and its proof by rational functions; the certificate for `D_n`.
[^exec]: Verified by execution (Python 3.11, 2026-10-29): `bin/python/brick_wall_castles.py` items [5] and [6], run log `bin/python/brick_wall_castles-run.log`. The displayed quotient expanded to `q^16` at `p = 1, 2, 3, 4` against brute-force counts of the histograms with first column at most `r` and rises at most `r`, `r = 1, 2, 3`, by area; the castles on the brick wall by number of cells against A005169 for up to 18 cells.
