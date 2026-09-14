---
title: "PE 502: Solution"
category: Sources
summary: The full mathematical solution — the binary-string bijection, the induction proof of T(k,L)=(k+1)^L, the F(w,h) formula, the P recursion, two computational paths with regime thresholds, and what didn't work.
tags: [project-euler, castle, solution, generating-functions, algorithms, source, subpage]
sources: [project-euler-502-solution]
created: 2026-09-13
updated: 2026-09-13
---

# PE 502: Solution

**Source:** https://charlesreid1.com/wiki/Project_Euler/502/Solution
**Date ingested:** 2026-09-13
**Type:** article (MediaWiki subpage of [[project-euler-502](pages/project-euler-502.md)])

## Summary

This is the authoritative mathematical solution the other subpages point to. It fixes notation, proves the counting closed form, gives the recursion for the signed count, and specifies exactly how the large-parameter values are computed.

The notation is worth adopting wiki-wide: **`A(w,h)`** is the number of castles with bottom block of length *w* and height *exactly* *h*, counting **all** parities; **`F(w,h)`** is `A(w,h)` restricted to an even total block count — the quantity Project Euler 502 asks for.[^1] Everything above the mandatory bottom block (Rule 4) is a "tower," counted unsigned by `T(k,L)` and with sign `(−1)^{blocks}` by `P(k,L)`.[^1]

The engine is the **[[binary-string-bijection](pages/binary-string-bijection.md)]**: configurations of non-overlapping, non-adjacent sub-blocks within a length-*L* block biject with length-*L* binary strings via maximal runs of 1s, so a block holds `2^L` configurations and a string with *r* runs gives *r* sub-blocks.[^2] Combined with sibling independence, an induction on *k* proves `T(k,L) = (k+1)^L`, whose corollary `T(h−1,w) = h^w` counts all height-≤*h* castles.[^3] Height-exactly-*h* and the even-block projection then give the [[castle-counting-formula](pages/castle-counting-formula.md)] `F(w,h) = [h^w − (h−1)^w − P(h−1,w) + P(h−2,w)]/2`.[^4]

The signed count obeys the run-product recursion `P(k,L) = ∑_b (−1)^{runs(b)} ∏_{runs of length l} P(k−1,l)`, with two structural facts: for fixed *k*, `P(k,·)` is a linear recurrence in *L* of order ~*k* (a sum of ≤ *k*+1 exponentials, `O(k² log L)`); for fixed *L*, a linear recurrence in *k* of order ~2*L* (`O(L² log k)` once [[berlekamp-massey](pages/berlekamp-massey.md)] finds it).[^5] The `k=1` case reduces to counting `(−1)^{runs}` over binary strings, a 2×2 transfer matrix with eigenvalues `1±i`, giving `P(1,L) = Re((1+i)^{L+1})` — verified here (`P(1,4) = −4`, both by the formula and by a 6-even/10-odd brute-force count).[^6]

Operationally, the solution routes each target through one of two paths (see [[castle-count-algorithms](pages/castle-count-algorithms.md)]): a rational-function path for `h ≤ 15000` (extract `[x^w]` of `num_k/den_k` by direct power series or [[kitamasa](pages/kitamasa.md)], chosen by a crossover rule) and a *k*-direction [[berlekamp-massey](pages/berlekamp-massey.md)] path for `h > 15000`.[^7] It also records **what did not work** — a rare and valuable negative-results section — and cites three papers from the polyomino / column-convex / transfer-matrix literature.[^8][^9]

## Key Takeaways

- **Notation:** `A(w,h)` = all castles (any parity) of exact height *h*; `F(w,h)` = the even-block restriction of `A`.[^1] (The odd-block count is left unnamed for now; it is `A − F`.)
- **[[binary-string-bijection](pages/binary-string-bijection.md)]:** length-*L* block configs ↔ length-*L* binary strings (maximal runs of 1s); `2^L` configs; *r* runs ↔ *r* sub-blocks.[^2]
- **`T(k,L) = (k+1)^L`**, proved by induction on *k* via the bijection plus sibling independence; corollary `T(h−1,w) = h^w` (e.g. `2^4 = 16` for the height-≤2, w=4 case).[^3]
- **`F(w,h) = [h^w − (h−1)^w − P(h−1,w) + P(h−2,w)]/2`**, with `F(4,2)=10` worked from `P(0,4)=1`, `P(1,4)=−4`.[^4][^6]
- **`P(k,L)` recursion** with two directions (linear recurrence in *L* of order ~*k*; in *k* of order ~2*L*); `P(1,L) = Re((1+i)^{L+1})`; small cases `P(k,2)=(−1)^k(k+1)`, `P(k,3)=(−1)^k(k+1)²` (all verified during ingest).[^5][^6][^10]
- **Two computational paths with explicit regime thresholds** route the three PE 502 targets (see [[castle-count-algorithms](pages/castle-count-algorithms.md)]): `F(10000,10000)`→direct extractor, `F(10^12,100)`→Kitamasa, `F(100,10^12)`→*k*-direction Berlekamp–Massey.[^7]
- **What did not work:** direct enumeration; binary strings without the independence insight; U/R/D convex-castle variation enumeration; L-direction transfer matrix as the primary solve.[^8]

## Entities & Concepts

- [[binary-string-bijection](pages/binary-string-bijection.md)] — the block↔binary-string bijection, the solution's engine.
- [[castle-count-algorithms](pages/castle-count-algorithms.md)] — the two computational paths and how each target is routed.
- [[kitamasa](pages/kitamasa.md)], [[berlekamp-massey](pages/berlekamp-massey.md)] — the fast linear-recurrence toolkit.
- [[castle-counting-formula](pages/castle-counting-formula.md)], [[castle-counting-function](pages/castle-counting-function.md)], [[castle-sign](pages/castle-sign.md)], [[generalized-dyck-grammar](pages/generalized-dyck-grammar.md)] — machinery this page proves and ratifies.

Related topics now ingested: [[polyominoes](pages/polyominoes.md)], [[dyck-words](pages/dyck-words.md)], [[lattice-paths](pages/lattice-paths.md)], [[generating-functions](pages/generating-functions.md)], [[project-euler-502-implementation-notes](pages/project-euler-502-implementation-notes.md)]. Still not yet ingested: Combinatorics. The three reference papers are ingested separately (see [[steep-polyominoes-q-motzkin-bessel](pages/steep-polyominoes-q-motzkin-bessel.md)], [[column-convex-polygon-enumeration](pages/column-convex-polygon-enumeration.md)], [[counting-horizontally-convex-polyominoes](pages/counting-horizontally-convex-polyominoes.md)]).

## What did not work (negative results)

The source records approaches that failed, each a thread worth following into the broader domain:[^8]

- **Direct enumeration** of castles — killed by `F(13,10) ~ 4×10^12`.
- **Column-wise binary strings without the runs/independence insight** — the right encoding, wrong decomposition: no way to count without independence.
- **U/R/D [[convex-castle](pages/convex-castle.md)] variation enumeration** — conceptually clean, but the case analysis to enumerate variations never resolved into a formula.
- **L-direction transfer matrix as the primary solve** — works, but slower: matrix power costs `O(D³ log w)` versus Kitamasa's `O(D² log w)`.

## The answer

The composite target `(F(10^12,100) + F(10000,10000) + F(100,10^12)) mod (10^9+7)` is recorded on the source only in obfuscated form, as the base64 checksum token `NzQ5NDg1MjE3` at the end of its References section.[^9] Following Project Euler etiquette (and the source's own choice to obfuscate), this wiki does not reproduce the decoded final answer; the checksum token is preserved as-is on the source page.

## References (from the source)

Three papers, ingested here as their own source pages:[^9]

- Barcucci, Del Lungo, Fédou, Pinzani, *Steep polyominoes, q-Motzkin numbers and q-Bessel functions* — [[steep-polyominoes-q-motzkin-bessel](pages/steep-polyominoes-q-motzkin-bessel.md)]
- Bousquet-Mélou, *A method for the enumeration of various classes of column-convex polygons* — [[column-convex-polygon-enumeration](pages/column-convex-polygon-enumeration.md)]
- Hickerson, *Counting Horizontally Convex Polyominoes* — [[counting-horizontally-convex-polyominoes](pages/counting-horizontally-convex-polyominoes.md)]

Also cited: the Java implementation and the **Implementation Notes** subpage (not yet ingested).

## Relation to Other Wiki Pages

This page is the trunk from which the earlier subpages branch: it proves `T(k,L)=(k+1)^L` (the [[castle-counting-formula](pages/castle-counting-formula.md)] had it from the grammar; here it is the binary-string induction), states the [[binary-string-bijection](pages/binary-string-bijection.md)] precisely, and specifies the [[castle-count-algorithms](pages/castle-count-algorithms.md)] that make the trillion-scale targets computable. Its "what did not work" list and its three reference papers are the launch points for following every solution thread — successful and failed — outward into the broader polyomino and combinatorics literature.

## Footnotes

[^1]: [[project-euler-502-solution](pages/project-euler-502-solution.md)] §"Notation" L5-10 — "A(w, h) - number of castles with bottom block of length w and height exactly h. F(w, h) - A(w, h) restricted to even total block count ... T(k, L) - number of towers of height at most k ... P(k, L) - the signed version of T ... (-1)^{blocks in tower}" and "the bottom row is always one block of length w (Rule 4). Everything else is a 'tower'."
[^2]: [[project-euler-502-solution](pages/project-euler-502-solution.md)] §"The binary-string bijection" L14-19 — "Configurations within a block of length L ... biject with binary strings of length L: map each string to the configuration whose sub-blocks are its maximal runs of 1s ... The number of configurations in a length-L block is 2^L ... a binary string has r maximal runs of 1s, the corresponding configuration has r sub-blocks."
[^3]: [[project-euler-502-solution](pages/project-euler-502-solution.md)] §"T(k, L) = (k+1)^L" L23-37 — "Proof by induction on k. Base: T(0, L) = 1 ... Two sibling blocks in the same row generate towers that never interact ... T(k, L) = ... = (1 + k)^L. Corollary ... T(h-1, w) = h^w. Verify on w=4, h=2: 2^4 = 16."
[^4]: [[project-euler-502-solution](pages/project-euler-502-solution.md)] §"The main formula" L46-66 — "#castles(w, h exact, any parity) = h^w - (h-1)^w ... (T + P)/2 counts towers with even block count and (T - P)/2 counts odd ... F(w, h) = (h^w - (h-1)^w - P(h-1, w) + P(h-2, w))/2".
[^5]: [[project-euler-502-solution](pages/project-euler-502-solution.md)] §"Recursion for P(k, L)" L76-84 — "P(k, L) = ∑_b (-1)^{runs(b)} ∏_{runs of length l} P(k-1, l) ... For fixed k, P(k, L) satisfies a linear recurrence in L of order roughly k ... O(k^2 log L) ... For fixed L ... a linear recurrence in k of order at most about 2L ... O(L^2 log k) after Berlekamp-Massey."
[^6]: [[project-euler-502-solution](pages/project-euler-502-solution.md)] §"Recursion for P(k, L)" L96-113 — the a_L/b_L split, matrix [[1,1],[-1,1]] with eigenvalues 1±i, "P(1, L) = Re((1+i)^{L+1})", "(1+i)^5 = -4 - 4i ... P(1, 4) = -4", and "of the 16 length-4 strings, 6 have an even number of runs and 10 have odd, so P(1, 4) = 6 - 10 = -4"; all re-verified during ingest.
[^7]: [[project-euler-502-solution](pages/project-euler-502-solution.md)] §"Two ways to compute P" L122-165 — the rational-function path (h ≤ 15000) with direct vs Kitamasa extractors and the regime matches "F(10000, 10000) ... direct extractor" / "F(10^12, 100) ... Kitamasa"; the k-direction Berlekamp-Massey path (h > 15000) with "N = 4(w+2) + 20" and "F(100, 10^12): w = 100, so N ≈ 428."
[^8]: [[project-euler-502-solution](pages/project-euler-502-solution.md)] §"What was tried and did not work" L188-191 — "Direct enumeration of castles. Killed by F(13,10) ~ 4 × 10^12. Column-wise binary strings without the runs/independence insight ... U/R/D convex-castle enumeration ... never resolved into a formula. L-direction transfer matrix as the primary solve ... O(D^3 log w) versus O(D^2 log w) for Kitamasa."
[^9]: [[project-euler-502-solution](pages/project-euler-502-solution.md)] §"References" L195-205 — the three uploaded PDFs ("step polyominoes, motzkin numbers, and bessel functions"; "a method for the enumeration of classes of column-convex polygons"; "construction procedure for parallel polyomino transfer matrices"), the Java source, and "checksum NzQ5NDg1MjE3".
[^10]: [[project-euler-502-solution](pages/project-euler-502-solution.md)] §"Recursion for P(k, L)" L117-118 — "P(k, 2) = (-1)^k (k+1), satisfying (λ+1)^2 = 0. P(k, 3) = (-1)^k (k+1)^2, satisfying (λ+1)^3 = 0"; both re-verified during ingest.
