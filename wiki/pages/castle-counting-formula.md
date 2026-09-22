---
title: Castle counting formula
category: Concepts
summary: The wiki's core derivation. F(w,h) = [h^w − (h−1)^w − P(h−1,w) + P(h−2,w)]/2 from the unsigned tower count (k+1)^L (proved three independent ways) and the signed count P_k; verified on all checkpoints.
tags: [concept, castle, generating-functions, closed-form, dyck, proof]
sources: [project-euler-502-representations, project-euler-502-castle-factoring, project-euler-502-observations, project-euler-502-solution, project-euler-502-implementation-notes, project-euler-502-brute-force]
created: 2026-09-13
updated: 2026-09-19
---

# Castle counting formula

## Overview

This is the closed-form derivation of the [[castle-counting-function](pages/castle-counting-function.md)] `F(w,h)`, read off the [[generalized-dyck-grammar](pages/generalized-dyck-grammar.md)] for castles. It replaces enumeration with a direct count and reproduces the problem's known checkpoints exactly. It has two ingredients — an **unsigned** tower count and a **signed** tower count that encodes the even-block rule — combined into the formula for `F(w,h)`. The unsigned count is proved three independent ways below; the signed count is reached by three independent routes.

## Unsigned count: T(k,L) = (k+1)^L

Three independent proofs give the same count: a generating-function recurrence read off the grammar, a product form over column heights, and an induction on *k* through the binary-string bijection. Each is short enough to give in full.

**Proof 1: generating-function recurrence.** Mark each `R` step by a variable *x*, so a tower of *L* columns is worth `x^L`. Writing `E_k(x)` for the generating function of towers of height at most *k*, the grammar `E_k → empty | R E_k | U V D (empty | R E_k)` reads off term-by-term as:[^1]

```
E_k = 1 + x·E_k + (E_{k−1} − 1)(1 + x·E_k)
```

where `1` is the empty tower, `x·E_k` a gap column then the rest, `(E_{k−1} − 1)` the nonempty interior tower `V`, and `(1 + x·E_k)` the "stop, or gap and continue" tail; the vertical `U`/`D` add no *x*.[^1] Collecting terms gives `E_k = E_{k−1} / (1 − x·E_{k−1})`, with base case `E_0 = 1/(1−x)` (a height-0 skyline is any number of empty columns). Unwinding the recurrence:[^2]

```
E_k = 1 / (1 − (k+1)x)      ⟹      T(k,L) = (k+1)^L
```

**Proof 2: product form over column heights.** The castle-factoring reading gives the same `(k+1)^L` without solving a generating-function recurrence: reading a tower as its column heights `c_1…c_L` (the integer-tuple [[castle-representations](pages/castle-representations.md)]), each `c_i` ranges *independently* over `{0,…,k}`, and the tower word is recovered invertibly from the heights — so `T(k,L) = (k+1)^L` is immediate as a product form.[^10] That independence of the columns is exactly the crux the Observations subpage names — sibling towers never interact — captured structurally on [[generalized-dyck-grammar](pages/generalized-dyck-grammar.md)]; it "took years to see."[^13]

**Proof 3: induction on *k*.** The Solution subpage proves the same closed form by a clean induction on *k*: the [[binary-string-bijection](pages/binary-string-bijection.md)] plus sibling independence makes the count factor over runs, `T(k,L) = ∑_b ∏_{runs} T(k−1,l) = ∑_b k^{ones(b)} = (1+k)^L`.[^16]

All three land on the same statement: the number of towers of height at most *k* above a length-*L* block is `(k+1)^L`, with corollary `T(h−1,w) = h^w`.[^16]

## Signed count: the even-block rule as a sign

The even-block rule is the hard constraint, and it enters as a **sign**: weight each block — that is, each `D` — by −1. Since a peak `U V D` adds one block on top of `V`, it flips the sign of everything inside it. With `P_k` the signed tower generating function, the grammar picks up a single minus on the peak production, giving:[^3]

```
P_k = 1 + x·P_k − (P_{k−1} − 1)(1 + x·P_k)
```

which solves to the rational recurrence (with `P_0 = 1/(1−x)`):[^4]

```
P_k = (2 − P_{k−1}) / (1 − 2x + x·P_{k−1})
```

Writing `P_k = num_k / den_k`, this is a polynomial update:[^5]

```
num_k = 2·den_{k−1} − num_{k−1}
den_k = den_{k−1}·(1 − 2x) + x·num_{k−1}
```

For fixed *k*, `P_k` is rational with denominator of degree *k*+1, so `P(k,L)` obeys an order-(*k*+1) linear recurrence in *L*. Two small cases:[^6]

- *k*=1: `P(1,L) = 2P(1,L−1) − 2P(1,L−2)`, closed form `P(1,L) = Re((1+i)^{L+1})` — the Online Encyclopedia of Integer Sequences (OEIS) sequence `A146559(L+1)` (see [[signed-tower-count](pages/signed-tower-count.md)]).
- *k*=2: `P(2,L) = 3P(2,L−1) − 4P(2,L−2) + 4P(2,L−3)`.

The full C-finite `P(k,·)` family (order `k+1`, characteristic polynomials with constant term `(−1)^{k−1}2^k`) is catalogued on [[signed-tower-count](pages/signed-tower-count.md)].

**Why `P` is the right signed object.** `P(k,L) = ∑_{c ∈ {0,…,k}^L} (−1)^{descent(c)}` is the [[castle-sign](pages/castle-sign.md)] `s(C) = (−1)^{blocks}` summed over all towers — the castle analogue of the permutation sign homomorphism. The `(T ± P)/2` combination is the `(1 ± sgn)/2` even/odd class projector, which is exactly why it isolates the even-block castles.[^11]

**A third route to `P`.** Besides the generating-function recurrence (above) and the [[monotone-streak-factorization](pages/monotone-streak-factorization.md)], `P(k,L)` can be computed by a direct `O(k²L)` dynamic program over the last column height: carry a length-`(k+1)` state indexed by the previous column's height, and on appending a column of height `b` after `a` multiply by `(−1)^{max(0, b−a)}` (the new runs each contribute `−1`). This is the [[project-euler-502-brute-force](pages/project-euler-502-brute-force.md)] `p_signed`, used as exact-integer ground truth for the formula.[^18]

**Evaluating at trillion scale.** For the large-parameter cases the recurrence in *L* is run with fast linear-recurrence methods: **Kitamasa** gives `O(k² log L)` in the *L* direction, and **Berlekamp–Massey** works in the *k* direction — the route the Solution subpage uses for `F(10^12, 100)` and `F(100, 10^12)`.[^12]

## The main formula

A full castle is `U (tower) D`, so its block count is the tower's block count plus one (the bottom block); **even total blocks means an odd number of blocks in the tower.**[^7] Since `T(h−1,w) = h^w` counts towers of height ≤ *h*−1 of any parity and `P(h−1,w)` is the signed version, `(T − P)/2` counts towers of *odd* block count. That expression `(h^w − P(h−1,w))/2` still includes every height from 0 to *h*−1, so subtracting the height ≤ *h*−2 case forces height exactly *h*:[^8]

```
F(w,h) = [ h^w − (h−1)^w − P(h−1,w) + P(h−2,w) ] / 2
```

The division by 2 is exact over the integers, but when computing modulo `p` it is a multiply by the modular inverse of 2 — so the modular evaluation assumes `p ≠ 2` (fine for `p = 10^9+7`).[^17]

## Verification

The source gives Python that builds `P(k,L)` as the coefficient of `x^L` in `num_k/den_k` (via the polynomial recurrence above) and evaluates `F(w,h)`.[^9] Re-running it during ingest reproduces all three problem checkpoints exactly:

```
F(4,2)   = 10
F(13,10) = 3729050610636
F(10,13) = 37959702514
```

matching the values on [[castle-counting-function](pages/castle-counting-function.md)].[^9]

The two integer values also have clean factorizations (confirmed by factoring during ingest): `F(13,10) = 3729050610636 = 2²·3·13·1163·20553887` and `F(10,13) = 37959702514 = 2·102859·184523`.[^14]

**The parity clause is the whole difficulty.** Almost all of the formula's complexity — the signed count `P` — is there to enforce the even-block rule. Drop that rule and the count collapses to the unsigned baseline `h^w − (h−1)^w` (all castles of height ≤ *h* minus those of height ≤ *h*−1), i.e. the `P` terms vanish. The even-block clause is "almost the entire difficulty."[^15]

## Appearances in Sources

- [[project-euler-502-representations](pages/project-euler-502-representations.md)] — derives the unsigned count `(k+1)^L`, the signed count `P_k`, and the closed form for `F(w,h)`, with verifying Python.
- [[project-euler-502-castle-factoring](pages/project-euler-502-castle-factoring.md)] — gives the product-form proof of `(k+1)^L`, the sign-homomorphism reading of `P`, and the Kitamasa/Berlekamp–Massey evaluation.
- [[project-euler-502-observations](pages/project-euler-502-observations.md)] — names the column independence as the crux, the `h^w−(h−1)^w` unconstrained baseline, and the verified factorizations.
- [[project-euler-502-solution](pages/project-euler-502-solution.md)] — proves `T(k,L)=(k+1)^L` by induction via the binary-string bijection, and specifies the algorithms that evaluate `P` at large parameters.
- [[project-euler-502-implementation-notes](pages/project-euler-502-implementation-notes.md)] — the `/2` as a modular inverse (assumes `p ≠ 2`) and the code that runs the recurrences.
- [[project-euler-502-brute-force](pages/project-euler-502-brute-force.md)] — the `p_signed` DP (a third route to `P`) and the direct-enumeration cross-check of the whole formula.

## Related Concepts

- [[castle-counting-function](pages/castle-counting-function.md)] — the function `F(w,h)` this formula computes.
- [[generalized-dyck-grammar](pages/generalized-dyck-grammar.md)] — the grammar the generating functions are read off.
- [[binary-string-bijection](pages/binary-string-bijection.md)] — the base of the Solution's induction proof of `T(k,L)`.
- [[generating-functions](pages/generating-functions.md)] — the method embodied here.
- [[castle-sign](pages/castle-sign.md)] — the sign-homomorphism meaning of the signed count `P`.
- [[castle-count-algorithms](pages/castle-count-algorithms.md)] — how `P(h−1,w)` and `P(h−2,w)` are evaluated at scale.
- [[monotone-streak-factorization](pages/monotone-streak-factorization.md)] — the canonical form the fast evaluation sums over.
- [[convex-castle](pages/convex-castle.md)] — the enumeration-side backbone, complementary to this counting-side formula.
- [[tower-recursion-master-class](pages/tower-recursion-master-class.md)] — the two-idea pedagogical version of this derivation.
- [[pell-castle-strip](pages/pell-castle-strip.md)] / [[pell-numbers](pages/pell-numbers.md)] — a coefficient-matching companion to the recurrences above.
- [[project-euler-502-problem-setup](pages/project-euler-502-problem-setup.md)] — the pre-solution framing whose `F(13,10)` scale argument this closed form answers; [[project-euler-502-observations](pages/project-euler-502-observations.md)] — the source's own statement of the crux and of `(A + P)/2` as a recurring symmetry trick.
- [[new-sequence-fw3](pages/new-sequence-fw3.md)] — the `h = 3` row `F(w,3) = (3^w − 2^w − P(2,w) + P(1,w))/2` as a standalone order-6 sequence.
- [[castles-as-upgraded-cycle-count](pages/castles-as-upgraded-cycle-count.md)] — the seminar-shape derivation of this formula as the `(n−1)!` cycle-count toolkit upgraded three times, ending on the same `F(4,2) = 10` hand-check the Verification here uses.

## Footnotes

[^1]: [[project-euler-502-representations](pages/project-euler-502-representations.md)] §"Unsigned count" L286-292 — "Let x mark one R step ... E_k = 1 + x E_k + (E_{k-1} - 1)(1 + x E_k)" with the term-by-term reading (empty, gap, nonempty interior V, tail; vertical U/D add no x).
[^2]: [[project-euler-502-representations](pages/project-euler-502-representations.md)] §"Unsigned count" L297-309 — "E_k = E_{k-1}/(1 - x E_{k-1})", base "E_0 ... 1/(1-x)", unwinding to "E_k = 1/(1-(k+1)x)" and "T(k,L) = (k+1)^L", "the closed form already on Project Euler/502/Solution."
[^3]: [[project-euler-502-representations](pages/project-euler-502-representations.md)] §"Signed count" L316-329 — "The even-block rule is the hard constraint, and it enters as a sign. Weight each block, that is each D, by -1 ... one minus sign on the peak ... P_k = 1 + x P_k - (P_{k-1} - 1)(1 + x P_k)".
[^4]: [[project-euler-502-representations](pages/project-euler-502-representations.md)] §"Signed count" L333 — "P_k = (2 - P_{k-1})/(1 - 2x + x P_{k-1}), P_0 = 1/(1-x)".
[^5]: [[project-euler-502-representations](pages/project-euler-502-representations.md)] §"Signed count" L338-339 — "num_k = 2 den_{k-1} - num_{k-1}, den_k = den_{k-1}(1-2x) + x num_{k-1}".
[^6]: [[project-euler-502-representations](pages/project-euler-502-representations.md)] §"Signed count" L343-345 — "k=1: P(1,L) = 2P(1,L-1) - 2P(1,L-2), closed form P(1,L) = Re((1+i)^{L+1}); k=2: P(2,L) = 3P(2,L-1) - 4P(2,L-2) + 4P(2,L-3)".
[^7]: [[project-euler-502-representations](pages/project-euler-502-representations.md)] §"The main formula" L350 — "The full castle is U (tower) D, so its block count is the tower's block count plus one for the bottom block. Even total blocks means an odd number of blocks in the tower."
[^8]: [[project-euler-502-representations](pages/project-euler-502-representations.md)] §"The main formula" L352-367 — "h^w = T(h-1,w) counts towers ... any parity. P(h-1,w) is the signed version, so (T - P)/2 counts towers with an odd block count ... subtract the height ≤ h-2 case to force height exactly h", giving "F(w,h) = (h^w - (h-1)^w - P(h-1,w) + P(h-2,w))/2".
[^9]: [[project-euler-502-representations](pages/project-euler-502-representations.md)] §"The main formula" L372-411 — the Python building P(k,L) from the num/den recurrence and F(w,h) from the formula, printing "F(4,2) = 10 / F(13,10) = 3729050610636 / F(10,13) = 37959702514"; re-run during ingest, all three reproduce exactly.
[^10]: [[project-euler-502-castle-factoring](pages/project-euler-502-castle-factoring.md)] §"A column-height factorization" L72-89 — "each c_i ranges independently over {0, …, k}, and the tower word is recovered by [the invertible procedure] ... T(k,L) = (k+1)^L ... each of the L columns independently chooses one of k+1 heights. This is the product-form proof."
[^11]: [[project-euler-502-castle-factoring](pages/project-euler-502-castle-factoring.md)] §"Monotone streak factorization and fast algorithms" L185, §"The sign of a castle" L119-121 — "P(k,L) = ∑_{c ∈ {0,…,k}^L} (-1)^{descent(c)}" and "(T + P)/2 = even-block ... (T - P)/2 = odd-block ... exactly the (1 ± sgn)/2 trick ... the castle analogue of the sign homomorphism."
[^12]: [[project-euler-502-castle-factoring](pages/project-euler-502-castle-factoring.md)] §"Monotone streak factorization and fast algorithms" L192 — "evaluated in O(k^2 log L) by Kitamasa in the L direction, or in the k direction by Berlekamp-Massey, which is how [Solution] computes F(10^12, 100) and F(100, 10^12)."
[^13]: [[project-euler-502-observations](pages/project-euler-502-observations.md)] §"Sub-block independence" L5 — "Two sibling blocks in the same row generate towers that never interact ... This is the single fact that makes the problem tractable, and it took years to see."
[^14]: [[project-euler-502-observations](pages/project-euler-502-observations.md)] §"Useful factorizations" L25-31 — "F(13,10) = 3729050610636 = 2^2 × 3 × 1163 × 13 × 20553887" and "F(10,13) = 37959702514 = 2 × 102859 × 184523"; both re-factored during ingest and confirmed.
[^15]: [[project-euler-502-observations](pages/project-euler-502-observations.md)] §"The \"even number of blocks\" clause is almost the entire difficulty" L17 — "Without it, the answer is just h^w - (h-1)^w: all castles of height at most h minus those of height at most h-1."
[^16]: [[project-euler-502-solution](pages/project-euler-502-solution.md)] §"T(k, L) = (k+1)^L" L23-37 — "Proof by induction on k ... a length-L binary string ... plus, for each maximal run of length l, an independent tower of height ≤ k-1 ... T(k, L) = ∑_b ∏_{runs} T(k-1, l) = ∑_b k^{ones(b)} = (1 + k)^L. Corollary ... T(h-1, w) = h^w."
[^17]: [[project-euler-502-implementation-notes](pages/project-euler-502-implementation-notes.md)] §"Numerics" L63 — "solveMod accepts any prime p, but division by 2 assumes p ≠ 2."
[^18]: [[project-euler-502-brute-force](pages/project-euler-502-brute-force.md)] §"p_signed" L31-47 — "A new column of height b after a column of height a starts max(0, b − a) new runs, each contributing a factor of −1 ... State is a length-(k+1) vector indexed by the last column height. The transition is O(k^2), so O(k^2 L) total."; DP re-run against brute during ingest, exact."
