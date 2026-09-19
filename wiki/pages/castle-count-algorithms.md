---
title: Castle-count algorithms
category: Analyses
summary: The two computational paths for F(w,h) — a rational-function path for h≤15000 (direct or Kitamasa extraction) and a k-direction Berlekamp–Massey path for h>15000 — and how each PE 502 target is routed.
tags: [analysis, castle, algorithms, generating-functions, kitamasa, berlekamp-massey]
sources: [project-euler-502-solution, project-euler-502-implementation-notes]
created: 2026-09-13
updated: 2026-09-19
---

# Castle-count algorithms

## Overview

Computing `F(w,h)` reduces to evaluating the signed count `P(k,L)` (the [[castle-counting-formula](pages/castle-counting-formula.md)]). The solution uses two computational paths, selected by the height *h* against a threshold of ~15000, plus an exact integer path for small sanity checks.[^1] The paths differ in which *direction* of the `P(k,L)` recurrence they exploit — *L* or *k* — and each of the three Project Euler 502 (PE 502) targets is routed to the path that suits its regime.

## The rational-function path (h ≤ 15000)

Work in the generating function `F_k(x) = ∑_L P(k,L) x^L`, starting from `F_0(x) = 1/(1−x)` (since `P(0,L)=1`) and applying the level-by-level rational update:[^2]

```
num_k(x) = 2·den_{k−1}(x) − num_{k−1}(x)
den_k(x) = den_{k−1}(x)·(1 − 2x) + num_{k−1}(x)·x
F_k(x)   = num_k(x) / den_k(x)
```

After `k = h−1` levels, extract `[x^w] F_{h−1}(x) = P(h−1,w)`. Two extractors, chosen by *w* against the denominator degree *D*:[^3]

- **Direct power series** — expand `c_n = num_n − ∑ den_i·c_{n−i}` for `n = 0..w`; cost `O(w·D)`.
- **[[kitamasa](pages/kitamasa.md)]** — compute `x^w mod charPoly`; cost `O(D² log w)`.

Direct wins when `w ≤ D+1` or `w·min(w,D) < 50D²`; otherwise Kitamasa — the crossover is where Kitamasa's `log w` saving beats its `D²` setup cost.[^3]

## The k-direction Berlekamp–Massey path (h > 15000)

For a fixed *w*, generate `P(0,w), P(1,w), …, P(N−1,w)` with `N = 4(w+2) + 20` (using the same inner recurrence, all mod a prime *p*), then:[^4]

1. [[berlekamp-massey](pages/berlekamp-massey.md)] finds the minimal linear recurrence (order at most ~2*w* empirically).
2. [[kitamasa](pages/kitamasa.md)] jumps directly to any index *k*.
3. Both `P(h−2,w)` and `P(h−1,w)` come out of one pass, saving a factor of 2.

Berlekamp–Massey discovers the recurrence so no proof is needed to *use* it; the transfer-matrix argument merely justifies that one exists.[^4]

## The exact path

For small *w, h* the same recurrence runs over integers with no modular reduction — usable only while `h^w` and `(h−1)^w` fit in a machine word. It handles the `F(4,2)`, `F(13,10)`, `F(10,13)` sanity checks.[^5]

## How the three targets are routed

| Target | *h* | Path | Extractor |
|---|---|---|---|
| `F(10000, 10000)` | 10000 ≤ 15000 | rational-function | direct (`D ≈ 10001`, `w = 10000`) |
| `F(10^12, 100)` | 100 ≤ 15000 | rational-function | Kitamasa (`D ≈ 101`, `w = 10^12`) |
| `F(100, 10^12)` | 10^12 > 15000 | *k*-direction Berlekamp–Massey | `N ≈ 428`, fast even at `k = 10^12` |

[^6]

**In the code.** `Problem502.java` dispatches on `(mod, h, w)`: `mod==0 → solveExact` (integers, no reduction), `h ≤ 15000 → computeViaRationalFunction`, `h > 15000 → computePviaKBoth`.[^7] The dispatch also has a `w ≤ 500` vs `w > 500` split under the `h > 15000` case, but both branches are identical — a dead placeholder for a future third path.[^7] Within the rational-function path the direct-vs-Kitamasa choice is the `extractCoeff` switch, and the extraction is deferred to a `Future` when it is expensive (`w·min(w,k+1) > 10^6`).[^8] See [[project-euler-502-implementation-notes](pages/project-euler-502-implementation-notes.md)] for the full code-to-math map and the per-target dominant costs (`F(10^12,100)` ≈ `4×10^5`, `F(10^4,10^4)` ≈ `10^8`).

**A thread to follow.** Both paths rest on `P(k,L)` being C-finite (linear-recurrent) in each direction — the same phenomenon by which other lattice-shape families collapse to short recurrences (e.g. horizontally convex polyominoes, [[counting-horizontally-convex-polyominoes](pages/counting-horizontally-convex-polyominoes.md)]). The choice of Kitamasa over an L-direction transfer-matrix power (`O(D² log w)` vs `O(D³ log w)`) is one of the suboptimal threads recorded on [[project-euler-502-solution](pages/project-euler-502-solution.md)].

## Appearances in Sources

- [[project-euler-502-solution](pages/project-euler-502-solution.md)] — specifies both paths, the extractor crossover, the `N = 4(w+2)+20` sample count, and the per-target routing.
- [[project-euler-502-implementation-notes](pages/project-euler-502-implementation-notes.md)] — the actual code dispatch on `(mod, h, w)`, extractor internals, and the regime/cost table.

## Related Concepts

- [[castle-counting-formula](pages/castle-counting-formula.md)] — the formula whose `P(k,L)` these paths evaluate.
- [[kitamasa](pages/kitamasa.md)], [[berlekamp-massey](pages/berlekamp-massey.md)] — the fast linear-recurrence tools the paths use.
- [[castle-counting-function](pages/castle-counting-function.md)] — the target values `F(10^12,100)`, `F(10000,10000)`, `F(100,10^12)`.
- [[monotone-streak-factorization](pages/monotone-streak-factorization.md)] — the canonical form underlying the recurrences.
- [[generating-function-gallery](pages/generating-function-gallery.md)] — the `num_k/den_k` catalogue behind the rational-function path.

## Footnotes

[^1]: [[project-euler-502-solution](pages/project-euler-502-solution.md)] §"Two ways to compute P" L120-122, §"The exact path" L167-169 — the two paths split at h ≤ 15000 / h > 15000, plus the exact integer path for small sanity checks.
[^2]: [[project-euler-502-solution](pages/project-euler-502-solution.md)] §"The rational-function path (h ≤ 15000)" L124-138 — "F_k(x) = ∑_L P(k, L) x^L ... F_0(x) = 1/(1 - x) ... num_k(x) = 2·den_{k-1}(x) - num_{k-1}(x); den_k(x) = den_{k-1}(x)·(1 - 2x) + num_{k-1}(x)·x; F_k(x) = num_k(x)/den_k(x)."
[^3]: [[project-euler-502-solution](pages/project-euler-502-solution.md)] §"The rational-function path (h ≤ 15000)" L143-147 — "Direct power series: ... Cost O(w · D). Kitamasa: ... O(D^2 log w). Direct wins when w ≤ D+1 or w · min(w, D) < 50 D^2; otherwise Kitamasa."
[^4]: [[project-euler-502-solution](pages/project-euler-502-solution.md)] §"The k-direction Berlekamp-Massey path (h > 15000)" L157-165 — "N = 4(w+2) + 20 ... Berlekamp-Massey finds the minimal linear recurrence. Kitamasa jumps directly to any index k. Both P(h-2, w) and P(h-1, w) are computed in one pass ... The recurrence order is at most about 2w empirically."
[^5]: [[project-euler-502-solution](pages/project-euler-502-solution.md)] §"The exact path" L167-169 — "the same recurrence runs over integers with no modular reduction. Only usable when h^w and (h-1)^w fit in a long. Handles the F(4,2), F(13,10), F(10,13) sanity checks."
[^6]: [[project-euler-502-solution](pages/project-euler-502-solution.md)] §"The rational-function path (h ≤ 15000)" L151-153 and §"The k-direction Berlekamp-Massey path (h > 15000)" L163 — "F(100, 10^12): h = 10^12, so this path is not taken. F(10000, 10000): h = 10000 ≤ 15000 ... D ≈ 10001, w = 10000 gives the direct extractor. F(10^12, 100): h = 100 ≤ 15000 ... D ≈ 101, w = 10^12 gives Kitamasa" and "F(100, 10^12): w = 100, so N ≈ 428. Fast even at k = 10^12."
[^7]: [[project-euler-502-implementation-notes](pages/project-euler-502-implementation-notes.md)] §"Dispatch" L13-19 — "mod == 0 -> solveExact; mod > 0, h <= 15000 -> computeViaRationalFunction; mod > 0, h > 15000, w <= 500 -> computePviaKBoth; mod > 0, h > 15000, w > 500 -> computePviaKBoth ... The two else bodies are identical; ... a placeholder for a future third branch."
[^8]: [[project-euler-502-implementation-notes](pages/project-euler-502-implementation-notes.md)] §"Rational-function path" L37, L39 — "at k = maxK - 1, a copy is saved (or the extraction is launched in a Future for the expensive case where w * min(w, k+1) > 10^6)" and "extractCoeff - the direct-vs-Kitamasa switch."
