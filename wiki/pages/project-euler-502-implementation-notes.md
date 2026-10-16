---
title: "PE 502: Implementation Notes"
category: Sources
summary: The Implementation Notes subpage maps Problem502.java to the mathematics of the Solution subpage - the dispatch on (mod, h, w), the rational-function path with its power-series and Kitamasa extractors, the Berlekamp-Massey path in the tower height, the numerics (division by 2 modulo p ≠ 2), a table of the path and cost of each target, and a list of what the code does not build.
tags: [project-euler, castle, implementation, java, algorithms, source, subpage]
sources: [project-euler-502-implementation-notes]
created: 2026-09-13
updated: 2026-10-16
---

# Project Euler 502 (PE 502): Implementation Notes

**Source:** https://charlesreid1.com/wiki/Project_Euler/502/Implementation_Notes
**Date ingested:** 2026-09-13
**Type:** article (MediaWiki subpage of [[project-euler-502](pages/project-euler-502.md)])

## Summary

This subpage maps each branch of the Java program `Problem502.java`, about 540 lines in one class, to the mathematics of [[project-euler-502-solution](pages/project-euler-502-solution.md)]. The source writes `F(w, h)` for the even-block count, which the wiki writes `A^e(w, h)`. `main` runs four checks, `A^e(4, 2)`, `A^e(13, 10)`, `A^e(10, 13)` and `A^e(100, 100)` modulo `10^9 + 7`, and then the target sum, under a deadline of 5 minutes enforced by running the target sum on a single-threaded `ExecutorService` and calling `future.get(remainingNanos, …)`.[^1]

The program dispatches on `(mod, h, w)`, following the paths of [[castle-count-algorithms](pages/castle-count-algorithms.md)]:[^2]

```
mod == 0                     -> solveExact
mod > 0, h <= 15000          -> computeViaRationalFunction
mod > 0, h > 15000, w <= 500 -> computePviaKBoth
mod > 0, h > 15000, w > 500  -> computePviaKBoth   (the same branch)
```

The source says the two branches for `h > 15000` are identical and are kept separate as a placeholder for a third.

## The two paths, in code

**Rational-function path** (`computeViaRationalFunction`), the update of `num_k` and `den_k` ([[castle-counting-formula](pages/castle-counting-formula.md)], Equation (5)):[^3]

- State: polynomial arrays `num[]` and `den[]` of size `maxK + 3`, with `den[0] = 1` kept by `newDen[0] = den[0]`. All arithmetic is modulo `p`, and `−x` is stored as `p − 1`.
- Extraction: at `k = maxK − 1` a copy is saved, or, when `w·min(w, k+1) > 10^6`, the extraction is launched as a Java `Future`; at `k = maxK`, `P(h−1, w)` is extracted.
- Extractors: `extractCoeff` chooses between the power series and Kitamasa's method ([[kitamasa](pages/kitamasa.md)]). `extractCoeffDirect` is unrolled by 8 with `int[]` coefficients, which is safe because `p < 2^30`, so 8 products, each below `p²`, stay under `Long.MAX_VALUE`. `extractCoeffMatExp`, `kitamasa` and `polyMulMod` run Kitamasa's method on the characteristic polynomial `x^d − Σ rec[i] x^{d−1−i}` taken from `−den[1..D]`.[^4]

**Berlekamp-Massey path** (`computePviaKBoth`), [[berlekamp-massey](pages/berlekamp-massey.md)] followed by Kitamasa's method:[^5]

1. Compute `seq[0..maxN−1]`, the values `P(k, w)` for `k < maxN`, with the `g[]` recurrence, the inner loop of `solveExact` reduced modulo `p`.
2. If `k1 = h − 1 < maxN`, return the values from `seq`.
3. Otherwise `berlekampMassey(seq, p)` returns the recurrence `rec` and its `order`.
4. `kitamasa(rec, order, k2, p)` returns `poly2`, the reduction for `P(h−2, w)`.
5. `poly1 = poly2 · x mod charPoly`, computed in place, gives `P(h−1, w)` without a second call to Kitamasa's method.
6. Combining `poly1` and `poly2` with `seq[0..order−1]` gives both values.

The source calls `berlekampMassey` a textbook implementation. `matmul` and `matpow` exist for `computePviaK`, which computes one value; `computePviaKBoth` uses Kitamasa's method, so matrix exponentiation is not used on the path of the target sum.[^6]

## Other details

- **Cache of the target terms.** When the first term of the target sum, `A^e(10^12, 100)`, arrives, the other two are submitted to `ForkJoinPool.commonPool()` and their `Future<Long>` stored under `cacheKey(w, h, mod)`; later calls to `solve` take the stored result. The three terms run in parallel on several cores and in sequence on one, with the same result. The source notes that `cacheKey = w·2 000 000 007 + h·1 000 003 + mod` is not a serious hash, and that the three inputs are far apart in it.[^7]
- **Numerics.** `modpow` is binary exponentiation, used for the inverse of 2 and for `h^w mod p`. The prime `p = 10^9 + 7` comes from the test table in `main`, not from a field of the class. `solveMod` accepts any prime `p`, but the division by 2 in Equation (1) of [[castle-counting-formula](pages/castle-counting-formula.md)] is multiplication by the inverse of 2, which needs `p ≠ 2`.[^8]

## Paths and costs of the three targets

The source tabulates the path, extractor and dominant cost of each term:[^9]

| term | `h ≤ 15000` | `w ≤ 500` | path | extractor | dominant cost, as the source gives it |
|---|---|---|---|---|---|
| `A^e(10^12, 100)` | yes | no | rational function | Kitamasa's method | `D = 101`, `O(D² log w) ≈ 4 × 10^5` |
| `A^e(10^4, 10^4)` | yes | no | rational function | power series | `O(w·D) ≈ 10^8` |
| `A^e(100, 10^12)` | no | yes | Berlekamp-Massey in `k` | Kitamasa's method | Berlekamp-Massey on about 428 terms, `O(w² log k)` |

The degree `D` of `den_{h−1}` is `h`, so `D = 100` for the first term; `100² · log₂(10^12) = 3.99 × 10^5`. [[castle-count-algorithms](pages/castle-count-algorithms.md)] gives the routing with these degrees.

## What is not in the code

The code builds no transfer matrix as a matrix, computes no `T(k, L)` directly, and enumerates no binary string, integer tuple or step word.[^10] The encodings of [[castle-representations](pages/castle-representations.md)], the [[binary-string-bijection](pages/binary-string-bijection.md)] and the [[generalized-dyck-grammar](pages/generalized-dyck-grammar.md)] are used to derive the recurrences; the program runs only the recurrences: the update of `num_k` and `den_k`, the sequence `P(k, w)` in `k`, Berlekamp-Massey and Kitamasa's method. [[project-euler-502-representations](pages/project-euler-502-representations.md)] says the same of the solution.

## Entities & Concepts

- [[castle-count-algorithms](pages/castle-count-algorithms.md)] - the two paths and the routing of the three targets.
- [[berlekamp-massey](pages/berlekamp-massey.md)], [[kitamasa](pages/kitamasa.md)] - the two recurrence algorithms the program runs.
- [[castle-counting-formula](pages/castle-counting-formula.md)] - the update of `num_k` and `den_k`, and the division by 2 in Equation (1).
- [[castle-representations](pages/castle-representations.md)], [[binary-string-bijection](pages/binary-string-bijection.md)], [[generalized-dyck-grammar](pages/generalized-dyck-grammar.md)] - the encodings the program does not build.
- Sibling subpages of [[project-euler-502](pages/project-euler-502.md)]: [[project-euler-502-problem-setup](pages/project-euler-502-problem-setup.md)], [[project-euler-502-representations](pages/project-euler-502-representations.md)], [[project-euler-502-castle-factoring](pages/project-euler-502-castle-factoring.md)], [[project-euler-502-observations](pages/project-euler-502-observations.md)], [[project-euler-502-solution](pages/project-euler-502-solution.md)], [[project-euler-502-brute-force](pages/project-euler-502-brute-force.md)].

Also linked from the source: [[generating-functions-topic](pages/generating-functions-topic.md)].

## Footnotes

[^1]: [[project-euler-502-implementation-notes](pages/project-euler-502-implementation-notes.md)] §"File and entry point" L7-8 - "main runs four sanity checks (F(4,2), F(13,10), F(10,13), F(100,100) mod), then the composite. Wall-clock deadline of 5 minutes on the composite. The composite is submitted to a single-threaded ExecutorService so the deadline is enforced with future.get(remainingNanos, ...)."
[^2]: [[project-euler-502-implementation-notes](pages/project-euler-502-implementation-notes.md)] §"Dispatch" L13-19 - "mod == 0 -> solveExact", "mod > 0, h <= 15000 -> computeViaRationalFunction", "mod > 0, h > 15000, w <= 500 -> computePviaKBoth", "mod > 0, h > 15000, w > 500 -> computePviaKBoth (same branch)", "The two else bodies are identical; the code keeps them separate as a placeholder for a future third branch."
[^3]: [[project-euler-502-implementation-notes](pages/project-euler-502-implementation-notes.md)] §"Rational-function path" L33-35 - "two polynomial arrays num[], den[], each of size maxK + 3. den[0] = 1 is invariant", "newDen[0] = den[0] preserves the invariant. Everything mod p; -x is stored as p - 1", "at k = maxK - 1, a copy is saved (or the extraction is launched in a Future for the expensive case where w * min(w, k+1) > 10^6). At k = maxK, P(h-1, w) is extracted."
[^4]: [[project-euler-502-implementation-notes](pages/project-euler-502-implementation-notes.md)] §"Rational-function path" L39-41 - "extractCoeff - the direct-vs-Kitamasa switch", "extractCoeffDirect - unrolled by 8 for cache locality; coefficients cast to int[] since p < 2^{30} and 8 products of < p^2 stay under Long.MAX_VALUE", "extractCoeffMatExp + kitamasa + polyMulMod - standard Kitamasa on the characteristic polynomial x^d - ∑ rec[i] x^{d-1-i} derived from -den[1..D]".
[^5]: [[project-euler-502-implementation-notes](pages/project-euler-502-implementation-notes.md)] §"k-direction BM path" L45-52 - "Generate seq[0..maxN-1] by running the g[] recurrence (same inner loop as solveExact, reduced mod p). If k1 = h-1 < maxN, return directly from seq. Else berlekampMassey(seq, p) gives rec, order. kitamasa(rec, order, k2, p) gives poly2 for P(h-2, w). poly1 is computed as poly2 * x mod charPoly in-line, saving a second Kitamasa call for P(h-1, w). Fold with seq[0..order-1] to get both values."
[^6]: [[project-euler-502-implementation-notes](pages/project-euler-502-implementation-notes.md)] §"k-direction BM path" L54, §"Matrix helpers" L58 - "berlekampMassey is textbook" and "matmul and matpow exist for computePviaK (the single-value variant). computePviaKBoth uses Kitamasa instead, so matrix exponentiation is unused on the composite path."
[^7]: [[project-euler-502-implementation-notes](pages/project-euler-502-implementation-notes.md)] §"Speculative composite cache" L23-27 - "the other two are eagerly submitted to ForkJoinPool.commonPool(), and their Future<Long> are stored under cacheKey(w, h, mod)", "on a multi-core box the three sub-problems run in parallel; on a single core it degrades to serial with no correctness impact", "cacheKey = w * 2_000_000_007L + h * 1_000_003L + mod. Not a serious hash; the three (w, h) inputs used are far apart in the key space."
[^8]: [[project-euler-502-implementation-notes](pages/project-euler-502-implementation-notes.md)] §"Numerics" L62-63 - "modpow is standard binary exponentiation, used for modular inverse and for h^w mod p", "p = 10^9+7 is hardcoded via the main test table, not a field. solveMod accepts any prime p, but division by 2 assumes p ≠ 2."
[^9]: [[project-euler-502-implementation-notes](pages/project-euler-502-implementation-notes.md)] §"Regime table" L71-75 - "F(10^{12}, 100) || yes || no || RationalFunction || Kitamasa || D=101, O(D^2 log w) ≈ 4 × 10^5", "F(10^4, 10^4) || yes || no || RationalFunction || Direct || O(w · D) ≈ 10^8", "F(100, 10^{12}) || no || yes || KBoth || Kitamasa || BM on ~428 terms, O(w^2 log k)".
[^10]: [[project-euler-502-implementation-notes](pages/project-euler-502-implementation-notes.md)] §"What is NOT in the code" L80 - "No transfer matrix built as a matrix. No T(k,L) computed directly. No enumeration of any binary string, integer tuple, or U/R/D word. The mathematical objects on Project Euler/502/Solution are the scaffolding used to derive the recurrences; only the recurrences appear in the code."
