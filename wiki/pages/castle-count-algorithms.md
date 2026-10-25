---
title: Castle-count algorithms
category: Analyses
summary: How the Project Euler 502 values A^e(w, h) are computed. A^e needs P(h−1, w) and P(h−2, w). For h ≤ 15000 they come from the rational generating function num_k/den_k of degree D = h, by power-series expansion in O(w·D) or by Kitamasa's method in O(D² log w); for h > 15000, from a recurrence in the tower height found by Berlekamp-Massey on N = 4(w + 2) + 20 terms. A^e(10^12, 100) takes Kitamasa's method, A^e(10000, 10000) the power series, and A^e(100, 10^12) the Berlekamp-Massey path.
tags: [analysis, castle, algorithms, generating-functions, kitamasa, berlekamp-massey]
sources: [project-euler-502-solution, project-euler-502-implementation-notes]
created: 2026-09-13
updated: 2026-10-25
---

# Castle-count algorithms

## Overview

The count `A^e(w, h)` of castles of width `w` and height `h` with an even number of blocks, the `F(w, h)` of the problem statement, is

```
A^e(w, h)  =  [ h^w − (h−1)^w − P(h−1, w) + P(h−2, w) ] / 2
```

([[castle-counting-formula](pages/castle-counting-formula.md)], Equation (1)), so computing it reduces to the two values `P(h−1, w)` and `P(h−2, w)` of the signed tower count. Project Euler 502 asks for `A^e(10^12, 100) + A^e(10000, 10000) + A^e(100, 10^12)` modulo `10^9 + 7` ([[castle-counting-function](pages/castle-counting-function.md)]), and the source's program uses two paths, chosen by `h` against the threshold 15000, plus an exact path for small checks.[^1] The first path works with the recurrence of `P(k, ·)` in the base length `L`, the second with its recurrence in the tower height `k`.

## The rational-function path, h ≤ 15000

The generating function `P_k(x) = Σ_L P(k, L) x^L` is `num_k(x)/den_k(x)`, built from `num_0 = 1`, `den_0 = 1 − x` by the update[^2]

```
num_k  =  2·den_{k−1} − num_{k−1}
den_k  =  (1 − 2x)·den_{k−1} + x·num_{k−1}
```

(the source writes `F_k(x)` for `P_k(x)`). After `h − 1` steps, `P(h−1, w)` is the coefficient of `x^w` in `num_{h−1}/den_{h−1}`, and `P(h−2, w)` is read from the previous step. The denominator `den_{h−1}` has degree `D = h` ([[castle-counting-formula](pages/castle-counting-formula.md)], the Proposition in the section *Signed tower count*). Two extractors compute the coefficient:[^3]

- **Power series.** Since `den_k(0) = 1`, the coefficients `c_n` of `num/den` follow from `c_n = num_n − Σ_{i=1}^{D} den_i c_{n−i}` for `n = 0, …, w`, in `O(w·D)` operations.
- **Kitamasa's method** ([[kitamasa](pages/kitamasa.md)]). Reduce `x^w` modulo the characteristic polynomial and read `c_w` off as a combination of the first `D` terms, in `O(D² log w)` operations.

The program uses the power series when `w ≤ D + 1` or `w·min(w, D) < 50D²`, and Kitamasa's method otherwise.[^3]

## The Berlekamp-Massey path, h > 15000

For fixed `w`, the program computes `P(0, w), …, P(N − 1, w)` modulo the prime `p` for `N = 4(w + 2) + 20`, then:[^4]

1. the [[berlekamp-massey](pages/berlekamp-massey.md)] algorithm returns the shortest linear recurrence in `k` that generates these `N` terms;
2. Kitamasa's method reaches `k = h − 2`;
3. one more step of the reduction, multiplication by `x` and one reduction modulo the characteristic polynomial, gives `k = h − 1`, so both values come from one pass.

The output is the recurrence of `P(·, w)` when that sequence satisfies a recurrence of order at most `N/2 = 2w + 14` ([[berlekamp-massey](pages/berlekamp-massey.md)], the Corollary). For every `L ≥ 4` the order is `2L − 2`, computed for `L ≤ 12` ([[recurrence-discovery](pages/recurrence-discovery.md)]) and proved for every `L` ([[signed-tower-k-direction](pages/signed-tower-k-direction.md)]), so at `L = w = 100` the order is 198, below `N/2 = 214`. The source states the order as "at most about 2w empirically" and that "no proof is required to use it".[^4]

## The exact path

For small `w` and `h`, the same update runs over the integers with no modular reduction, while `h^w` fits in a 64-bit integer. It gives the checkpoints `A^e(4, 2) = 10`, `A^e(13, 10) = 3 729 050 610 636` and `A^e(10, 13) = 37 959 702 514`.[^5]

## The three targets

| target | `h ≤ 15000` | path | extractor | dominant cost |
|---|---|---|---|---|
| `A^e(10^12, 100)` | yes, `h = 100` | rational function | Kitamasa's method | `D = 100`, `D² log₂ w ≈ 4 × 10^5` |
| `A^e(10000, 10000)` | yes, `h = 10000` | rational function | power series | `D = 10000`, `w·D = 10^8` |
| `A^e(100, 10^12)` | no, `h = 10^12` | Berlekamp-Massey in `k` | Kitamasa's method | Berlekamp-Massey on `N = 428` terms, then `O(w² log k)` for Kitamasa's method on a recurrence of order about `2w` |

At `A^e(10000, 10000)`, `w ≤ D + 1`, so the power series is used; at `A^e(10^12, 100)`, `w·min(w, D) = 10^14` exceeds `50D² = 5 × 10^5`, so Kitamasa's method is used.[^6]

**In the code.** `Problem502.java` dispatches on `(mod, h, w)`: `mod == 0` goes to `solveExact`, `h ≤ 15000` to `computeViaRationalFunction`, and `h > 15000` to `computePviaKBoth`. Under `h > 15000` the program splits at `w ≤ 500` and `w > 500`, but both branches call `computePviaKBoth`.[^7] On the rational-function path the choice of extractor is `extractCoeff`, and the extraction is launched as an asynchronous task (a Java `Future`) when `w·min(w, k+1) > 10^6`.[^8] [[project-euler-502-implementation-notes](pages/project-euler-502-implementation-notes.md)] maps each routine to the mathematics.

The source lists the transfer matrix in the `L` direction as an approach it did not use: its matrix power costs `O(D³ log w)`, against `O(D² log w)` for Kitamasa's method ([[project-euler-502-solution](pages/project-euler-502-solution.md)]).

## Appearances in Sources

- [[project-euler-502-solution](pages/project-euler-502-solution.md)] - the two paths, the extractor rule, the sample count `N = 4(w + 2) + 20`, and the routing of the three targets.
- [[project-euler-502-implementation-notes](pages/project-euler-502-implementation-notes.md)] - the dispatch on `(mod, h, w)` in `Problem502.java`, the extractors, and the table of paths and costs.

## Related Concepts

- [[castle-counting-formula](pages/castle-counting-formula.md)] - Equation (1) for `A^e(w, h)`, and the degree of `den_k`.
- [[kitamasa](pages/kitamasa.md)] - the reduction of `x^n` modulo the characteristic polynomial, and its costs.
- [[berlekamp-massey](pages/berlekamp-massey.md)] - the algorithm, and when its output is the recurrence of the whole sequence.
- [[recurrence-discovery](pages/recurrence-discovery.md)] - the orders of the recurrences of `P(k, L)` in `L` and in `k`, computed.
- [[signed-tower-k-direction](pages/signed-tower-k-direction.md)] - the characteristic polynomials of the recurrences in `k`, for `L ≤ 12`.
- [[castle-counting-function](pages/castle-counting-function.md)] - the checkpoints and the Project Euler target.
- [[generating-function-gallery](pages/generating-function-gallery.md)] - the rational functions `num_k/den_k` and their denominators.
- [[counting-horizontally-convex-polyominoes](pages/counting-horizontally-convex-polyominoes.md)] - another polyomino count with a short linear recurrence: the horizontally convex `n`-ominoes satisfy `a(n) = 5a(n−1) − 7a(n−2) + 4a(n−3)` for `n ≥ 5`.
- [[marin-2024-polyominoes-in-rectangle](pages/marin-2024-polyominoes-in-rectangle.md)] - polyominoes with bounding box `w × h`, whose counts satisfy a linear recurrence in `h` for every fixed `w`, proved with a row automaton.

## Footnotes

[^1]: [[project-euler-502-solution](pages/project-euler-502-solution.md)] §"Two ways to compute P" L120-122, §"The exact path" L167-169 [synthesis] - the rational-function path for `h ≤ 15000`, the Berlekamp-Massey path for `h > 15000`, and the exact path for the small checks.
[^2]: [[project-euler-502-solution](pages/project-euler-502-solution.md)] §"The rational-function path (h ≤ 15000)" L124-138 - "F_k(x) = ∑_L P(k, L) x^L", "F_0(x) = 1/(1 - x)", "num_k(x) = 2 · den_{k-1}(x) - num_{k-1}(x)", "den_k(x) = den_{k-1}(x) · (1 - 2x) + num_{k-1}(x) · x", "F_k(x) = num_k(x)/den_k(x)".
[^3]: [[project-euler-502-solution](pages/project-euler-502-solution.md)] §"The rational-function path (h ≤ 15000)" L140-147 - "After k = h-1 levels, extract [x^w] F_{h-1}(x) to get P(h-1, w)", "Direct power series: expand c_n = num_n - ∑ den_i · c_{n-i} for n = 0..w. Cost O(w · D)", "Kitamasa: turn the recurrence into \"compute x^w mod charPoly\", then O(D^2 log w)", "Direct wins when w ≤ D+1 or w · min(w, D) < 50 D^2; otherwise Kitamasa."
[^4]: [[project-euler-502-solution](pages/project-euler-502-solution.md)] §"The k-direction Berlekamp-Massey path (h > 15000)" L157-165 - "For fixed w, generate P(0, w), P(1, w), …, P(N-1, w) for N = 4(w+2) + 20", "Berlekamp-Massey finds the minimal linear recurrence. Kitamasa jumps directly to any index k. Both P(h-2, w) and P(h-1, w) are computed in one pass", "The recurrence order is at most about 2w empirically. Berlekamp-Massey discovers the recurrence, so no proof is required to use it".
[^5]: [[project-euler-502-solution](pages/project-euler-502-solution.md)] §"The exact path" L167-169 - "For small w, h, the same recurrence runs over integers with no modular reduction. Only usable when h^w and (h-1)^w fit in a long. Handles the F(4,2), F(13,10), F(10,13) sanity checks."
[^6]: [[project-euler-502-solution](pages/project-euler-502-solution.md)] §"The rational-function path (h ≤ 15000)" [synthesis] L149-153, §"The k-direction Berlekamp-Massey path (h > 15000)" L163 - the routing of the three targets, which the source gives with `D ≈ 10001`, `D ≈ 101` and `N ≈ 428`; the degree of `den_{h−1}` is `h`, and `4(100 + 2) + 20 = 428`. Costs recomputed: `100² · log₂(10^12) = 3.99 × 10^5`.
[^7]: [[project-euler-502-implementation-notes](pages/project-euler-502-implementation-notes.md)] §"Dispatch" L13-19 - "mod == 0 -> solveExact", "mod > 0, h <= 15000 -> computeViaRationalFunction", "mod > 0, h > 15000, w <= 500 -> computePviaKBoth", "mod > 0, h > 15000, w > 500 -> computePviaKBoth (same branch)", "The two else bodies are identical; the code keeps them separate as a placeholder for a future third branch."
[^8]: [[project-euler-502-implementation-notes](pages/project-euler-502-implementation-notes.md)] §"Rational-function path" L35, L39 - "at k = maxK - 1, a copy is saved (or the extraction is launched in a Future for the expensive case where w * min(w, k+1) > 10^6)" and "extractCoeff - the direct-vs-Kitamasa switch."
