---
title: Castle sign
category: Concepts
summary: s(C) = (-1)^blocks, the castle sign - the analogue of the permutation sign; (T +- P)/2 splits towers into even/odd-block classes, making P(k,L) a sign homomorphism.
tags: [concept, castle, sign, permutations, parity, generating-functions]
sources: [project-euler-502-castle-factoring, project-euler-502-observations, project-euler-502-brute-force, pe502-castle-cycle-permutations]
created: 2026-09-13
updated: 2026-09-19
---

# Castle sign

## Description

The **castle sign** is the castle analogue of the permutation sign, and it is what makes the even-block constraint tractable. A permutation sign is `sgn(σ) = (−1)^{n−c} = ∏_cycles (−1)^{|γ|−1}`, with *c* cycles.[^1] For a castle, each block is an excursion atom (a `U…D` pair) and each `D` completes one block, so weighting every block by −1 defines:[^1]

```
s(C) = (−1)^{blocks(C)}
```

In the column-height ([[castle-representations](pages/castle-representations.md)] integer-tuple) form, the block count is the total descent, so the sign is a function of the column heights directly:[^2]

```
blocks = ∑_{i=0}^{L} max(0, c_i − c_{i+1}),   c_0 = c_{L+1} = 0
s(C) = (−1)^{∑ max(0, c_i − c_{i+1})}
```

This is the total *descent* of the skyline. Equivalently, counting *ascents* (the [[project-euler-502-brute-force](pages/project-euler-502-brute-force.md)] form) gives the same block count `blocks = c_1 + ∑_{i≥2} max(0, c_i − c_{i−1})` — total ascent equals total descent for a sequence that starts and returns to 0. Both were verified against a direct run-count enumeration during ingest.[^6]

## The even/odd projector

Let `T` be the unsigned tower count and `P = ∑_C s(C)` the signed count. Then the sign separates towers into parity classes exactly as `(1 ± sgn)/2` separates permutations into even and odd:[^3]

```
(T + P)/2 = even-block towers
(T − P)/2 = odd-block towers
```

This is the meaning of the signed tower recursion `P(k,L)`: it is the castle analogue of the **sign homomorphism**.[^3] A full castle is `U (tower) D`, so its block count is the tower's plus one for the bottom block — "castle has even total blocks" means "tower has an odd number of blocks," which is the `(T−P)/2` term in the [[castle-counting-formula](pages/castle-counting-formula.md)]:[^4]

```
F(w,h) = [ h^w − (h−1)^w − P(h−1,w) + P(h−2,w) ] / 2
```

**A general technique, not a castle special case.** The Observations subpage frames this as "parity via signs": even-block-count `= (A + P)/2`, with `A` the unsigned total (this page's `T`) and `P` the `(−1)^{blocks}`-signed count — "a symmetry trick that recurs in many combinatorial-enumeration problems."[^5] It is worth recognizing the trick in the abstract, because it reappears wherever a parity or sign constraint must be projected out of an otherwise-easy total.

**The permutation-side identity.** In the symmetric group `S_n`, `(1 ± sgn(σ))/2` is the projector onto `A_n` (even permutations) or its complement, so `|A_n| = ½(n! + ∑_σ sgn(σ)) = n!/2` for `n ≥ 2` (the signed sum vanishes). The castle `(T ± P)/2` is the direct upgrade of this identity — same projector shape, with the castle sign in place of the permutation sign.[^7] This is the first of three upgrades on [[castles-as-upgraded-cycle-count](pages/castles-as-upgraded-cycle-count.md)] (the other two being the [[castle-foata-transform](pages/castle-foata-transform.md)] and the [[monotone-streak-factorization](pages/monotone-streak-factorization.md)]), which reads Project Euler 502 (PE 502) as the elementary `(n−1)!` cycle-count toolkit upgraded step-by-step.

## Appearances in Sources

- [[project-euler-502-castle-factoring](pages/project-euler-502-castle-factoring.md)] — defines `s(C) = (−1)^blocks`, gives the descent formula for the block count, and shows the `(T±P)/2` even/odd split.
- [[project-euler-502-observations](pages/project-euler-502-observations.md)] — frames the `(A+P)/2` parity-sign identity as a general recurring symmetry trick.
- [[project-euler-502-brute-force](pages/project-euler-502-brute-force.md)] — gives the ascent-side block-count formula and the `p_signed` dynamic program (DP) that verifies the sign directly.
- [[pe502-castle-cycle-permutations](pages/pe502-castle-cycle-permutations.md)] — identifies `(T ± P)/2` as the castle upgrade of the `(1 ± sgn)/2` projector that peels `A_n` from `S_n`.

## Related Concepts

- [[permutation-cycle-castle-analogy](pages/permutation-cycle-castle-analogy.md)] — the analogy in which the sign is the "sign atom."
- [[castle-counting-formula](pages/castle-counting-formula.md)] — where `P(k,L)` and the `(T−P)/2` term appear.
- [[tower-recursion-master-class](pages/tower-recursion-master-class.md)] — the sign trick taught as one of the two core ideas.
- [[parity-via-roots-of-unity](pages/parity-via-roots-of-unity.md)] — the sign generalized to mod m via m-th roots of unity.
- [[generating-functions-topic](pages/generating-functions-topic.md)] — the exponential generating function (EGF) `(e^x ± e^{−x})/2` projector, the same even/odd trick in the index register.
- [[monotone-streak-factorization](pages/monotone-streak-factorization.md)] — the block count as the sum of down-streak magnitudes.
- [[castle-counting-function](pages/castle-counting-function.md)] — the even-block count the sign isolates.
- [[signed-tower-count](pages/signed-tower-count.md)] — `P(k,L)` as a C-finite sequence family (and the `P(1,L)=A146559(L+1)` Online Encyclopedia of Integer Sequences (OEIS) identity).
- [[castles-as-upgraded-cycle-count](pages/castles-as-upgraded-cycle-count.md)] — the seminar synthesis reading `(T ± P)/2` as one of three upgrades of the `(n−1)!` cycle-count toolkit.

## Footnotes

[^1]: [[project-euler-502-castle-factoring](pages/project-euler-502-castle-factoring.md)] §"The sign of a castle" L92-101 — "sgn(σ) = (-1)^{n - c} = ∏ (-1)^{|γ|-1} ... Each block is an excursion atom (a U ... D pair), and each D move completes one block. Weight each block by -1 and define s(C) = (-1)^{blocks(C)}."
[^2]: [[project-euler-502-castle-factoring](pages/project-euler-502-castle-factoring.md)] §"The sign of a castle" L105-113 — "blocks = ∑_{i=0}^{L} max(0, c_i - c_{i+1}), c_0 = c_{L+1} = 0 ... s(C) = (-1)^{∑_i max(0, c_i - c_{i+1})}."
[^3]: [[project-euler-502-castle-factoring](pages/project-euler-502-castle-factoring.md)] §"The sign of a castle" L116-123 — "(T + P)/2 = even-block castles, (T - P)/2 = odd-block castles ... exactly the (1 ± sgn)/2 trick ... P(k,L) ... is the castle analogue of the sign homomorphism."
[^4]: [[project-euler-502-castle-factoring](pages/project-euler-502-castle-factoring.md)] §"The sign of a castle" L123-127 — "'castle has even total blocks' is therefore 'tower has an odd number of blocks', which is the (T-P)/2 term in F(w,h) = (h^w - (h-1)^w - P(h-1,w) + P(h-2,w))/2."
[^5]: [[project-euler-502-observations](pages/project-euler-502-observations.md)] §"Parity via signs" L13 — "Even-block-count is enforced by (A + P)/2, where A is the unsigned total and P is the signed count with (-1)^{blocks}. A symmetry trick that recurs in many combinatorial-enumeration problems."
[^6]: [[project-euler-502-brute-force](pages/project-euler-502-brute-force.md)] §"Column-height encoding" L24, §"p_signed" L31 — "#blocks = ... = c_1 + ∑_{i=2}^{w} max(0, c_i − c_{i−1})" and "A new column of height b after a column of height a starts max(0, b − a) new runs, each contributing a factor of −1"; both re-verified against direct run-count enumeration during ingest (w,h ≤ 6; DP vs brute for w,h ≤ 5)."
[^7]: [[pe502-castle-cycle-permutations](pages/pe502-castle-cycle-permutations.md)] §"Connection 1: Castle sign ↔ (1 ± sgn)/2 trick" L38 — "Weight each castle by (−1)^blocks, splitting the total count T into even- and odd-block halves via (T ± P)/2. This is exactly the (1 ± sgn)/2 trick used to peel A_n out of S_n."
