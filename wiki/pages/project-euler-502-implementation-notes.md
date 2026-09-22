---
title: "PE 502: Implementation Notes"
category: Sources
summary: A code-to-math map of Problem502.java — dispatch by (mod, h, w), the rational-function and k-direction BM paths, extractor switches, numerics, and what the code deliberately does NOT do.
tags: [project-euler, castle, implementation, java, algorithms, source, subpage]
sources: [project-euler-502-implementation-notes]
created: 2026-09-13
updated: 2026-09-19
---

# Project Euler 502 (PE 502): Implementation Notes

**Source:** https://charlesreid1.com/wiki/Project_Euler/502/Implementation_Notes
**Date ingested:** 2026-09-13
**Type:** article (MediaWiki subpage of [[project-euler-502](pages/project-euler-502.md)])

## Summary

This subpage maps every algorithmic branch of the Java solution (`Problem502.java`, ~540 lines, one class) back to the mathematics on [[project-euler-502-solution](pages/project-euler-502-solution.md)]. `main` runs the four sanity checks (`F(4,2)`, `F(13,10)`, `F(10,13)`, `F(100,100)` mod) then the composite, under a 5-minute wall-clock deadline enforced by submitting the composite to a single-threaded `ExecutorService` and calling `future.get(remainingNanos, …)`.[^1]

Computation dispatches on `(mod, h, w)`, realizing the [[castle-count-algorithms](pages/castle-count-algorithms.md)] in code:[^2]

```
mod == 0                     -> solveExact
mod > 0, h <= 15000          -> computeViaRationalFunction
mod > 0, h > 15000, w <= 500 -> computePviaKBoth
mod > 0, h > 15000, w > 500  -> computePviaKBoth   (identical branch; placeholder for a future third path)
```

The rest of the page details the two live paths, the extractor switch, the matrix helpers that go unused on the composite path, the numerics, and — usefully — a statement of what the code deliberately does *not* build.

## The two computational paths, in code

**Rational-function path** (`computeViaRationalFunction`) — the level-by-level `num/den` update from [[castle-counting-formula](pages/castle-counting-formula.md)]:[^3]

- State: polynomial arrays `num[]`, `den[]` of size `maxK+3`, with `den[0]=1` held invariant (`newDen[0]=den[0]`); all arithmetic mod `p`, with `−x` stored as `p−1`.
- Extraction: at `k = maxK−1` a copy is saved (or, for the expensive case `w·min(w,k+1) > 10^6`, launched in a `Future`); at `k = maxK`, `P(h−1,w)` is extracted.
- Extractors: `extractCoeff` is the direct-vs-[[kitamasa](pages/kitamasa.md)] switch; `extractCoeffDirect` is unrolled by 8 with `int[]` coefficients (safe because `p < 2^30`, so 8 products `< p^2` stay under `Long.MAX_VALUE`); `extractCoeffMatExp` + `kitamasa` + `polyMulMod` run Kitamasa on the characteristic polynomial `x^d − ∑ rec[i] x^{d−1−i}` derived from `−den[1..D]`.[^4]

**k-direction Berlekamp–Massey path** (`computePviaKBoth`) — [[berlekamp-massey](pages/berlekamp-massey.md)] + [[kitamasa](pages/kitamasa.md)]:[^5]

1. Generate `seq[0..maxN−1]` by running the `g[]` recurrence (the same inner loop as `solveExact`, reduced mod `p`).
2. If `k1 = h−1 < maxN`, return directly from `seq`.
3. Otherwise `berlekampMassey(seq, p)` gives `rec, order`.
4. `kitamasa(rec, order, k2, p)` gives `P(h−2,w)`.
5. `P(h−1,w)` is then computed as `poly2 · x mod charPoly` in-line — saving a second full Kitamasa call.
6. Fold with `seq[0..order−1]` to get both values.

`berlekampMassey` is a textbook implementation. `matmul`/`matpow` exist only for `computePviaK` (the single-value variant); `computePviaKBoth` uses Kitamasa instead, so matrix exponentiation is unused on the composite path.[^6]

## Engineering details

Operational specifics of the implementation, recorded for fidelity (not mathematical content):

- **Speculative composite cache.** When the first composite sub-problem (`F(10^12,100)`) arrives on the calling thread, the other two are eagerly submitted to `ForkJoinPool.commonPool()` and their `Future<Long>` stored under `cacheKey(w,h,mod)`; later `solve` calls hit the cache. Parallel on multi-core, gracefully serial on one core, no correctness impact. `cacheKey = w*2_000_000_007L + h*1_000_003L + mod` — not a serious hash, but the three inputs are far apart in key space.[^7]
- **Numerics.** `modpow` is binary exponentiation (used for the modular inverse and for `h^w mod p`). `p = 10^9+7` is supplied via the `main` test table, not a field; `solveMod` accepts any prime `p`, but the division by 2 in the `F` formula assumes `p ≠ 2` (it is a multiply by the modular inverse of 2).[^8]

## Regime table

Which path and extractor each composite sub-problem takes, with the dominant cost, is single-sourced on [[castle-count-algorithms](pages/castle-count-algorithms.md)] §"How the three targets are routed".[^9]

## What is not in the code

A clarifying point the subpage makes explicitly: the code builds **no transfer matrix as a matrix**, computes **no `T(k,L)` directly**, and enumerates **no binary string, integer tuple, or U/R/D word**.[^10] The mathematical objects developed across [[castle-representations](pages/castle-representations.md)], the [[binary-string-bijection](pages/binary-string-bijection.md)], and the [[generalized-dyck-grammar](pages/generalized-dyck-grammar.md)] are *scaffolding* used to derive the recurrences; only the recurrences (`num/den` update, the signed `P` sequence, BM + Kitamasa) actually run. This is the concrete confirmation of the representations subpage's remark that the winning solution manipulates none of the encodings directly.

## Key Takeaways

- Dispatch is on `(mod, h, w)`: exact for `mod==0`, rational-function for `h≤15000`, k-direction BM for `h>15000` (the `w≤500` split is a dead placeholder — both branches call `computePviaKBoth`).[^2]
- The rational-function path is the `num/den` update with a direct-vs-Kitamasa extractor switch (`extractCoeffDirect` unrolled by 8, `int[]` safe since `p<2^30`).[^3][^4]
- The BM path generates ~`maxN` terms, runs Berlekamp–Massey, then gets both `P(h−1,w)` and `P(h−2,w)` in one pass via `poly2·x mod charPoly`.[^5]
- `division by 2 assumes p ≠ 2` — the `/2` in the `F` formula is a multiply by the modular inverse of 2.[^8]
- The code runs only recurrences; the encodings and `T(k,L)` are derivation scaffolding, never built at runtime.[^10]

## Entities & Concepts

- [[castle-count-algorithms](pages/castle-count-algorithms.md)] — the two paths this code realizes, with the concrete dispatch thresholds.
- [[berlekamp-massey](pages/berlekamp-massey.md)], [[kitamasa](pages/kitamasa.md)] — the fast-recurrence routines and their code-level details.
- [[castle-counting-formula](pages/castle-counting-formula.md)] — the `num/den` update and the `/2` (mod inverse of 2) this implements.
- [[castle-representations](pages/castle-representations.md)], [[binary-string-bijection](pages/binary-string-bijection.md)], [[generalized-dyck-grammar](pages/generalized-dyck-grammar.md)] — the derivation scaffolding the code does not build.
- Sibling subpages of the [[project-euler-502](pages/project-euler-502.md)] hub: [[project-euler-502-problem-setup](pages/project-euler-502-problem-setup.md)], [[project-euler-502-representations](pages/project-euler-502-representations.md)], [[project-euler-502-castle-factoring](pages/project-euler-502-castle-factoring.md)], [[project-euler-502-observations](pages/project-euler-502-observations.md)], [[project-euler-502-solution](pages/project-euler-502-solution.md)], [[project-euler-502-brute-force](pages/project-euler-502-brute-force.md)].

## Relation to Other Wiki Pages

This subpage grounds the abstract [[castle-count-algorithms](pages/castle-count-algorithms.md)] in the actual `Problem502.java`, adding the real dispatch thresholds, the extractor internals, and the regime/cost table. Its "what is not in the code" section closes the loop opened on [[project-euler-502-representations](pages/project-euler-502-representations.md)]: the encodings and grammar are how the recurrences were *found*, not what the program *runs*.

## Footnotes

[^1]: [[project-euler-502-implementation-notes](pages/project-euler-502-implementation-notes.md)] §"File and entry point" L7-8 — "main runs four sanity checks (F(4,2), F(13,10), F(10,13), F(100,100) mod), then the composite. Wall-clock deadline of 5 minutes ... submitted to a single-threaded ExecutorService so the deadline is enforced with future.get(remainingNanos, ...)."
[^2]: [[project-euler-502-implementation-notes](pages/project-euler-502-implementation-notes.md)] §"Dispatch" L13-19 — "mod == 0 -> solveExact; mod > 0, h <= 15000 -> computeViaRationalFunction; mod > 0, h > 15000, w <= 500 -> computePviaKBoth; mod > 0, h > 15000, w > 500 -> computePviaKBoth ... The two else bodies are identical; ... a placeholder for a future third branch."
[^3]: [[project-euler-502-implementation-notes](pages/project-euler-502-implementation-notes.md)] §"Rational-function path" L33-37 — "num[], den[], each of size maxK + 3. den[0] = 1 is invariant ... Everything mod p; -x is stored as p - 1 ... at k = maxK - 1, a copy is saved (or ... a Future ... where w * min(w, k+1) > 10^6). At k = maxK, P(h-1, w) is extracted."
[^4]: [[project-euler-502-implementation-notes](pages/project-euler-502-implementation-notes.md)] §"Rational-function path" L39-41 — "extractCoeff - the direct-vs-Kitamasa switch. extractCoeffDirect - unrolled by 8 ... cast to int[] since p < 2^30 ... extractCoeffMatExp + kitamasa + polyMulMod - standard Kitamasa on the characteristic polynomial x^d - ∑ rec[i] x^{d-1-i} derived from -den[1..D]."
[^5]: [[project-euler-502-implementation-notes](pages/project-euler-502-implementation-notes.md)] §"k-direction BM path" L45-52 — "Generate seq[0..maxN-1] ... If k1 = h-1 < maxN, return directly ... berlekampMassey(seq, p) gives rec, order. kitamasa(rec, order, k2, p) gives poly2 for P(h-2, w). poly1 is computed as poly2 * x mod charPoly in-line, saving a second Kitamasa call ... Fold with seq[0..order-1] to get both values."
[^6]: [[project-euler-502-implementation-notes](pages/project-euler-502-implementation-notes.md)] §"k-direction BM path" L54, §"Matrix helpers" L58 — "berlekampMassey is textbook" and "matmul and matpow exist for computePviaK ... computePviaKBoth uses Kitamasa instead, so matrix exponentiation is unused on the composite path."
[^7]: [[project-euler-502-implementation-notes](pages/project-euler-502-implementation-notes.md)] §"Speculative composite cache" L23-27 — "the other two are eagerly submitted to ForkJoinPool.commonPool() ... stored under cacheKey(w, h, mod) ... on a multi-core box the three sub-problems run in parallel; on a single core it degrades to serial ... cacheKey = w * 2_000_000_007L + h * 1_000_003L + mod."
[^8]: [[project-euler-502-implementation-notes](pages/project-euler-502-implementation-notes.md)] §"Numerics" L62-63 — "modpow is standard binary exponentiation, used for modular inverse and for h^w mod p ... p = 10^9+7 is hardcoded ... solveMod accepts any prime p, but division by 2 assumes p ≠ 2."
[^9]: [[project-euler-502-implementation-notes](pages/project-euler-502-implementation-notes.md)] §"Regime table" L71-75 — "F(10^12, 100) ... RationalFunction ... Kitamasa ... D=101, O(D^2 log w) ≈ 4×10^5; F(10^4, 10^4) ... Direct ... O(w·D) ≈ 10^8; F(100, 10^12) ... KBoth ... BM on ~428 terms, O(w^2 log k)."
[^10]: [[project-euler-502-implementation-notes](pages/project-euler-502-implementation-notes.md)] §"What is NOT in the code" L80 — "No transfer matrix built as a matrix. No T(k,L) computed directly. No enumeration of any binary string, integer tuple, or U/R/D word. The mathematical objects ... are the scaffolding used to derive the recurrences; only the recurrences appear in the code."
