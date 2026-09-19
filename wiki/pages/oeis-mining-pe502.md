---
title: "OEIS mining of PE 502 castles (first pass)"
category: Sources
summary: A local research workspace mining the castle object against the OEIS — the vein structure, verified matches (height-2 hyperbolic, tower-Narayana, area↔A001523), corrections, and new-sequence candidates.
tags: [oeis, castle, research, mining, cross-reference, source]
sources: [oeis-mining-pe502]
created: 2026-09-13
updated: 2026-09-19
---

# Online Encyclopedia of Integer Sequences (OEIS) mining of Project Euler 502 (PE 502) castles (first pass)

**Source:** `~/code/oeis/pe502/` (local research workspace; notes copied to `raw/oeis-pe502/`, chiefly `README.md` and `mine-notes.md`)
**Date ingested:** 2026-09-13
**Type:** research notes + verified computation (Python: `castle.py`, `tower.py`, `vein9_area.py`, `vein9b_concave.py`; data `tables.json`, `terms_50.txt`)

> **See also:** [[oeis-index](pages/oeis-index.md)] - the wiki's OEIS directory (every A-number and its wiki pages, grouped by role).

## Summary

This is the first-pass **OEIS mining** of the [[castle-polyomino](pages/castle-polyomino.md)]: taking the castle counts and finding the existing OEIS A-numbers whose integers they reproduce (interlinking), and identifying counts with no match (generation candidates). It is exactly the [[project-euler-502-brute-force](pages/project-euler-502-brute-force.md)] OEIS-mining method, carried out systematically and verified — every accepted match was checked against the actual OEIS data *with offsets*, not just leading terms.[^1] All identities below were re-verified by direct enumeration during this ingest.

The work is organized into **veins**, each a thread from the castle out to a family of sequences:[^2]

- **Vein 1 — the signed count.** `P(1,L) = Re((1+i)^{L+1}) = A146559(L+1)`, correcting a plan error that had claimed A009545 (which is the *imaginary* part `Im((1+i)^n)`, the companion, not `P`). The general `P(k,·)` is C-finite of order `k+1`. See [[signed-tower-count](pages/signed-tower-count.md)].
- **Vein 2 — any-parity = difference of powers.** `h^w − (h−1)^w` gives `A000225` (h=2), `A001047` (h=3), `A005061/A005060/A005062` — trivial but real interpretations.
- **Vein 3 — the even count `F(w,h)`.** Height 2 is a genuine match: `F(w,2) = A038505(w+1)`, `odd(w,2) = A038503(w+1) − 1`, into the order-4 [[hyperbolic-sequence-family](pages/hyperbolic-sequence-family.md)]; see [[oeis-height2-hyperbolic-castles](pages/oeis-height2-hyperbolic-castles.md)]. Heights h ≥ 3 are new C-finite sequences (rows), and columns are quasi-polynomials annihilated by `(x²−1)^w`.
- **Vein 4 — convex castles are binomial, not Catalan.** `convex(w,h) = C(2h+w−3, w−1)`, proved via [[convex-castle-binomial-identity](pages/convex-castle-binomial-identity.md)]; convex ⟺ unimodal ⟺ exactly `h` blocks.
- **Veins 6/7 — the tower block-count is a Narayana polynomial.** This is where the Catalan/Narayana thread actually lives (not the convex count): see [[tower-narayana-polynomial](pages/tower-narayana-polynomial.md)].
- **Veins 9/9b — castles by area.** Re-indexing by total cells: convex ↔ `A001523`, all ↔ `2^{n−1}`, valley ↔ `A332578`, non-convex ↔ `A115981`; plus new parity-refined and strict-valley sequences. See [[castle-by-area](pages/castle-by-area.md)].

## Results at a glance

| Object | OEIS | Status |
|---|---|---|
| `P(1,L)` signed towers | `A146559(L+1)` | match — corrects a plan error (A009545 is the imaginary part) |
| any-parity, height *h* | `A000225, A001047, A005061, A005060, A005062` | match (trivial: `h^w−(h−1)^w`) |
| `F(w,2)` even castles, h=2 | `A038505(w+1) = Σ C(w+1, 4k+2)` | **match (the real win)** |
| `odd(w,2)` odd castles, h=2 | `A038503(w+1) − 1` | **match (the real win)** |
| `convex(w,h)` any parity | binomial `C(2h+w−3, w−1)` | match (binomial, **not** Catalan) |
| tower block-count rows w=2..5 | `A005408, A005891, A063490, A160747` | match (Narayana polynomial) |
| convex castles by area | `A001523(n)` | match (weakly unimodal compositions) |
| valley castles by area | `A332578(n)` | match (negation-unimodal compositions) |
| non-convex castles by area | `A115981(n)` (= `A011782 − A001523`) | match |
| `F(w,h)`, h≥3 rows; columns; `odd(w,h)` h≥3 | — | **NEW** (C-finite / quasi-poly) |
| tower rows w≥6 | — | **NEW** (Narayana-polynomial triangle) |
| area sequences (even/odd/cev/cod, strict-valley, parity splits) | — | **NEW** (`cev+cod = A001523`) |

## Key facts worth remembering

- **Height 2 is the order-4 "hyperbolic" family.** The height-2 castle gives `{A038503, A038505}` a geometric reading, decomposing `2^w−1` by block-count parity.[^3]
- **Convex ⟺ unimodal ⟺ exactly `h` blocks** — so convex castles are the *minimum-block* castles, counted by the binomial `C(2h+w−3, w−1)`.[^4]
- **No Catalan in the natural (w,h) parameterizations** — the gap, parity, and convexity constraints are all *binomial* (see [[convex-castle-binomial-identity](pages/convex-castle-binomial-identity.md)]). The Catalan/Narayana thread instead lives in the **tower** block-count.[^5]
- **Verify against OEIS data with offsets.** The A009545/A146559 mixup (real vs imaginary part of `(1+i)^n`) was caught precisely this way; short-term false positives were rejected.[^1]

## Entities & Concepts

- [[oeis-cross-referencing](pages/oeis-cross-referencing.md)] — the interlinking method and discipline this work follows.
- [[signed-tower-count](pages/signed-tower-count.md)], [[hyperbolic-sequence-family](pages/hyperbolic-sequence-family.md)], [[narayana-numbers](pages/narayana-numbers.md)], [[tower-heap](pages/tower-heap.md)], [[weakly-unimodal-composition](pages/weakly-unimodal-composition.md)], [[castle-by-area](pages/castle-by-area.md)] — the concepts these veins introduce.
- [[convex-castle](pages/convex-castle.md)], [[castle-counting-function](pages/castle-counting-function.md)], [[castle-counting-formula](pages/castle-counting-formula.md)] — castle machinery the mining reads against.

The verified findings are elaborated on their own source pages: [[oeis-height2-hyperbolic-castles](pages/oeis-height2-hyperbolic-castles.md)], [[tower-narayana-polynomial](pages/tower-narayana-polynomial.md)], [[castle-by-area](pages/castle-by-area.md)], [[convex-castle-binomial-identity](pages/convex-castle-binomial-identity.md)], [[new-sequence-fw3](pages/new-sequence-fw3.md)]. Submission-ready OEIS drafts live in `raw/oeis-pe502/` (kept as drafts; OEIS requires human authorship — see [[oeis-cross-referencing](pages/oeis-cross-referencing.md)]).

## Relation to Other Wiki Pages

This is the wiki's first turn from *documenting the solution* to *research outward*: it operationalizes the mission's OEIS-mining thread, connects the castle to eight-plus existing OEIS sequences and to Narayana/Viennot heap theory, and produces concrete new-sequence candidates. It builds directly on [[castle-counting-function](pages/castle-counting-function.md)] (the `A`/`F` counts), [[convex-castle](pages/convex-castle.md)], and [[castle-sign](pages/castle-sign.md)] (the signed count `P`).

## Footnotes

[^1]: [[oeis-mining-pe502](pages/oeis-mining-pe502.md)] `mine-notes.md` §"Method notes" L175-186 — "Every accepted match ... was checked against the actual OEIS data with offsets, not just the first few terms. The plan's own 'A009545' was caught this way (real vs imaginary)."; identities re-verified by direct enumeration during ingest.
[^2]: [[oeis-mining-pe502](pages/oeis-mining-pe502.md)] `mine-notes.md` §"Vein 1"–"Vein 9b" L19-150 [synthesis] — the vein structure (signed count, difference of powers, F(w,h), convex/binomial, block distribution, odd complement, castles by area, concave castles).
[^3]: [[oeis-mining-pe502](pages/oeis-mining-pe502.md)] `mine-notes.md` §"Vein 3" L55-64 — "F(w,2) = A038505(w+1) = sum_k C(w+1, 2+4k) ... odd(w,2) = A038503(w+1) - 1 ... total = A000225(w) = 2^w - 1 ... two of the four order-4 'hyperbolic' sequences"; re-verified during ingest (F(w,2), odd(w,2) for w=1..7).
[^4]: [[oeis-mining-pe502](pages/oeis-mining-pe502.md)] `mine-notes.md` §"Vein 4" L84-92 — "every convex castle of height h has EXACTLY h blocks ... #blocks >= h with equality iff convex ... convex(w,h) = C(2h + w - 3, w - 1)"; re-verified during ingest (all w,h ≤ 5: binomial match and blocks==h).
[^5]: [[oeis-mining-pe502](pages/oeis-mining-pe502.md)] `README.md` §"Key facts worth remembering" — "No Catalan anywhere in the natural parameterisations ... But the tower block-count has a Narayana-polynomial generating function."
