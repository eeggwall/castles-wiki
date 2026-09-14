---
title: "PE 502: Brute Force"
category: Sources
summary: The Python reference module (castle.py) — exact-integer F/F_odd/F_any, a column-height p_signed DP, full enumeration by parity and unimodality, and OEIS mining for further structure.
tags: [project-euler, castle, brute-force, python, verification, oeis, source, subpage]
sources: [project-euler-502-brute-force]
created: 2026-09-13
updated: 2026-09-13
---

# PE 502: Brute Force

**Source:** https://charlesreid1.com/wiki/Project_Euler/502/Brute_Force (module: `castle.py`)
**Date ingested:** 2026-09-13
**Type:** article (MediaWiki subpage of [[project-euler-502](pages/project-euler-502.md)]) documenting a Python module

## Summary

`castle.py` is the exact-integer Python reference that cross-checks the Java solver ([[project-euler-502-implementation-notes](pages/project-euler-502-implementation-notes.md)]) — no modular reduction, no Berlekamp–Massey, no Kitamasa. It is fast enough to run the full-enumeration `brute` for `w,h ≲ 15` and the exact `F(w,h)` checks over the full checkpoint range.[^1] Running it during ingest reproduced every self-test and the brute-vs-formula cross-check exactly.

It exposes several counting functions:[^2]

- `F(w,h)` — even-block castles, via the same closed form as the [[castle-counting-formula](pages/castle-counting-formula.md)].
- `F_odd(w,h)` — odd-block castles; the complement of `F` (this wiki names the odd count `A − F`, deliberately unsymbolized — see [[castle-counting-function](pages/castle-counting-function.md)]).
- `F_any(w,h) = h^w − (h−1)^w` — height exactly *h*, any parity; this is the general count `A(w,h)`.
- `p_signed(k,L)` — the signed sum `P(k,L)` by an `O(k²L)` last-column-height DP.
- `brute(w,h)` — full enumeration of column-height tuples `c ∈ {1..h}^w` with `max c = h`, tallied by parity and by unimodality.
- `block_poly(w,h)` — the block-count distribution over height ≤ *h*.

Two pieces of new machinery are worth extracting. First, a clean **column-height block-count formula**: reading a castle as a skyline `c_1…c_w ∈ {1..h}^w` with `max c = h`, the number of blocks is[^3]

```
#blocks = ∑_{r=1}^{h} #{runs of columns with c_i ≥ r} = c_1 + ∑_{i=2}^{w} max(0, c_i − c_{i−1})
```

(verified during ingest to match the run-based definition for all skylines with `w,h ≤ 6`). Rule 3 (same-row gaps) is automatic in the run decomposition; Rule 6 (even count) is imposed by parity at the end.[^3] Second, `p_signed` is a **third route to `P`** (alongside the grammar generating function and the streak factorization): a new column of height `b` after height `a` starts `max(0, b−a)` new runs, each weighted `−1`, giving an `O(k²)` transition on a length-`(k+1)` last-height state.[^4]

`brute` additionally separates **unimodal** skylines — column-convex *and* row-convex — into `conv_even`/`conv_odd`, exactly the [[convex-castle](pages/convex-castle.md)] whose direct variation-enumeration failed.[^5] And the module frames **OEIS mining** as a research method: sweeping `brute` over a `(w,h)` rectangle yields sequences (even, odd, unimodal, block-count distributions) to look up in the OEIS for further structure.[^6]

## Verification

Re-run during ingest, all exact:[^7]

- Checkpoints: `F(4,2)=10`, `F(13,10)=3729050610636`, `F(10,13)=37959702514`, `F(100,100) mod (10^9+7) = 841913936`.
- Brute cross-check for all `w,h ≤ 5`: `brute["even"] == F`, `brute["even"] + brute["odd"] == F_any`.
- The column-height block-count formula matches the run-based count for all `w,h ≤ 6`.

These are the same four checkpoints that head the Java `main`.[^7]

## Key Takeaways

- Exact-integer reference (`F`, `F_odd`, `F_any = A`, `p_signed`, `brute`) that is the ground truth for the DP: any change to `p_signed` is validated against `brute` on `w,h ≤ 5` before touching the solver.[^8]
- **Block-count formula on column heights:** `#blocks = c_1 + ∑_{i≥2} max(0, c_i − c_{i−1})` — verified.[^3]
- `p_signed` gives a **third, column-height DP** computation of `P`, `O(k²L)`.[^4]
- **Unimodal skyline = column-convex ∧ row-convex = the [[convex-castle](pages/convex-castle.md)]**; the brute `conv_*` counts are exactly the class the U/R/D convex-castle attempt failed to enumerate directly.[^5]
- **OEIS mining** — brute over a `(w,h)` rectangle produces sequences to look up for further structure; a concrete research method for this wiki's mission.[^6]

## Entities & Concepts

- [[convex-castle](pages/convex-castle.md)] — the unimodal (column-convex ∧ row-convex) class the `conv_*` counts measure.
- [[castle-counting-function](pages/castle-counting-function.md)] — `F`, and `F_any` as the general count `A(w,h)`.
- [[castle-counting-formula](pages/castle-counting-formula.md)], [[castle-sign](pages/castle-sign.md)], [[monotone-streak-factorization](pages/monotone-streak-factorization.md)] — the formula, the block-count/descent, and the third `p_signed` route.
- [[horizontally-convex-polyomino](pages/horizontally-convex-polyomino.md)], [[column-convex-polyomino](pages/column-convex-polyomino.md)] — the two convexities whose intersection is the unimodal castle.

## Relation to Other Wiki Pages

This module is the empirical backstop for the whole solution: it independently confirms `F`, `P`, and the `A = F + F_odd` decomposition by direct enumeration. It also supplies two threads — the explicit column-height block-count formula (feeding [[castle-sign](pages/castle-sign.md)] and [[monotone-streak-factorization](pages/monotone-streak-factorization.md)]) and the unimodal/`conv_*` counts (feeding [[convex-castle](pages/convex-castle.md)]) — plus the OEIS-mining method that turns brute output into lookups against the wider combinatorics literature.

## Footnotes

[^1]: [[project-euler-502-brute-force](pages/project-euler-502-brute-force.md)] §"Brute Force" L5 — "A small Python module used to cross-check the Java solver ... Exact integer arithmetic, no modular reduction, no BM, no Kitamasa. Fast enough for w, h ≤ 15 or so on the brute enumerator, and for the full range of the exact F(w, h) checks on the DP path."
[^2]: [[project-euler-502-brute-force](pages/project-euler-502-brute-force.md)] §"What it computes" L9-14 — the list of functions: F (even, exact), F_odd (odd, complement of F), F_any (any parity, h^w − (h−1)^w), p_signed(k,L) (the signed sum P by an O(k·L·k) DP), brute(w,h) (full enumeration), block_poly(w,h).
[^3]: [[project-euler-502-brute-force](pages/project-euler-502-brute-force.md)] §"Column-height encoding" L18-27 — "column heights c_1, …, c_w ∈ {1, …, h} with max c = h ... #blocks = ∑_{r=1}^{h} #{runs of columns with c_i ≥ r} = c_1 + ∑_{i=2}^{w} max(0, c_i − c_{i−1}) ... Rule 3 ... is automatic in the run decomposition ... Rule 6 ... applied by parity at the end"; formula re-verified against the run definition for all skylines w,h ≤ 6 during ingest.
[^4]: [[project-euler-502-brute-force](pages/project-euler-502-brute-force.md)] §"p_signed" L31-47 — "A new column of height b after a column of height a starts max(0, b − a) new runs, each contributing a factor of −1 ... State is a length-(k+1) vector indexed by the last column height. The transition is O(k^2), so O(k^2 L) total."; the DP re-run against brute during ingest, exact.
[^5]: [[project-euler-502-brute-force](pages/project-euler-502-brute-force.md)] §"brute" L54, §"Why keep a brute enumerator" L92 — "conv_even, conv_odd - the same, restricted to unimodal skylines (column-convex AND row-convex)" and "Unimodal castles are the ones the U/R/D convex-castle attempt tried and failed to enumerate directly."
[^6]: [[project-euler-502-brute-force](pages/project-euler-502-brute-force.md)] §"Why keep a brute enumerator" L93 — "OEIS mining. Running brute over a rectangle of (w, h) produces sequences (even, odd, unimodal, block-count distributions) that can be looked up in the OEIS to reveal further structure."
[^7]: [[project-euler-502-brute-force](pages/project-euler-502-brute-force.md)] §"Self-test" L74-83 — "F(4, 2) = 10 ... F(13, 10) = 3 729 050 610 636 ... F(10, 13) = 37 959 702 514 ... F(100, 100) mod (10^9 + 7) = 841 913 936" plus "brute(w, h)['even'] == F(w, h) ... brute(w, h)['even'] + brute(w, h)['odd'] == F_any(w, h)"; all re-run exact during ingest.
[^8]: [[project-euler-502-brute-force](pages/project-euler-502-brute-force.md)] §"Why keep a brute enumerator" L91 — "Ground truth for the DP. Any change to p_signed is validated against brute on w, h ≤ 5 before touching the Java solver."
