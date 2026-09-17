---
title: Signed tower count P(k,L)
category: Concepts
summary: P(k,L) = Σ (−1)^blocks over towers of height ≤ k above a length-L block; a C-finite family of order k+1, with P(1,L) = Re((1+i)^{L+1}) = A146559(L+1).
tags: [concept, castle, signed-count, c-finite, oeis, generating-functions]
sources: [oeis-mining-pe502, project-euler-502-solution]
created: 2026-09-13
updated: 2026-09-16
---

# Signed tower count P(k,L)

## Description

`P(k,L)` is the signed tower count — the sum of `(−1)^{blocks}` over all towers of height at most *k* above a length-*L* block — the object that encodes the even-block rule in the [[castle-counting-formula](pages/castle-counting-formula.md)] and is read as a sign homomorphism on [[castle-sign](pages/castle-sign.md)]. This page collects its sequence structure as surfaced by the [[oeis-mining-pe502](pages/oeis-mining-pe502.md)] pass. The width `L` is indexed from 0 — the empty tower (zero columns, zero blocks) is a tower — so `P(k,0) = 1` for every `k`; the sequences below begin at `L = 0`, whereas the OEIS notes quoted in the footnotes list them starting at `L = 1`.

For fixed *k*, `P(k,·)` is **C-finite** (satisfies a linear recurrence) of order `k+1`, with characteristic polynomials:[^1]

```
P(1):  x² − 2x + 2                        (eigenvalues 1 ± i)
P(2):  x³ − 3x² + 4x − 4    = (x−2)(x²−x+2)
P(3):  x⁴ − 4x³ + 8x² − 8x + 8
P(4):  x⁵ − 5x⁴ + 12x³ − 20x² + 16x − 16
P(5):  x⁶ − 6x⁵ + 18x⁴ − 32x³ + 48x² − 32x + 32
```

(constant term `(−1)^{k−1} 2^k`, leading coefficient `−(k+1)`). This is the C-finiteness that [[berlekamp-massey](pages/berlekamp-massey.md)]/[[kitamasa](pages/kitamasa.md)] exploit to evaluate `P` at trillion scale.

## The k = 1 case and an OEIS correction

At `k = 1`, `P(1,L) = ∑_b (−1)^{runs(b)}` over binary strings, which is the real part of a complex power:[^2]

```
P(1,L) = Re((1+i)^{L+1}) = A146559(L+1)      (A146559: g.f. (1−x)/(1−2x+2x²))
```

with values `P(1,L) = 1, 0, −2, −4, −4, 0, 8, 16, 16, 0, −32, …` from `L = 0` (re-verified during ingest). A parent plan had claimed `P(1,L) = A009545`, but **A009545 is the imaginary part `Im((1+i)^n)`** — the companion, not `P`. The mixup is a textbook case for [[oeis-cross-referencing](pages/oeis-cross-referencing.md)]'s "verify against OEIS data with offsets" rule: the two sequences agree in magnitude pattern but are the real vs. imaginary components of the same `(1+i)^n`.[^2]

Both components are castle counts. Splitting `P(1,L)` by the parity of the last column height gives `P_even(1,L) = Re((1+i)^L) = A146559(L)` and `P_odd(1,L) = −Im((1+i)^L) = −A009545(L)`: A009545 is minus the signed count of height-`≤1` towers whose last column has height 1. The split is the `k = 1` case of the sector decomposition on [[tower-parity-sectors](pages/tower-parity-sectors.md)], which for even `k` is what factors `char_k`.

`A146559` is a proposed cross-link target: `a(n) = P(1,n−1)`, the real part of `(1+i)^n` read as a signed castle count, with the genuinely new formula `A146559(n) = A038503(n) − A038505(n)` tying the signed vein to the height-2 [[hyperbolic-sequence-family](pages/hyperbolic-sequence-family.md)].[^3] The `P(k,·)` families for `k ≥ 2` (e.g. `P(2,·): 1,1,3,9,19,33,59,…` order 3; `P(4,·): 1,1,5,25,85,225,541,…` order 5) are new-sequence candidates generalizing A146559.[^4]

## Appearances in Sources

- [[oeis-mining-pe502](pages/oeis-mining-pe502.md)] — vein 1: the C-finite `P(k,·)` family, `P(1,L)=A146559(L+1)`, and the A009545 correction.
- [[project-euler-502-solution](pages/project-euler-502-solution.md)] — defines `P(k,L)` and derives the `k=1` case `Re((1+i)^{L+1})`.

## Related Concepts

- [[castle-sign](pages/castle-sign.md)] — `P` as the sign homomorphism.
- [[castle-counting-formula](pages/castle-counting-formula.md)] — where `P(h−1,w)`, `P(h−2,w)` enter `F`.
- [[hyperbolic-sequence-family](pages/hyperbolic-sequence-family.md)] — `A146559 = A038503 − A038505` links the signed vein to height 2.
- [[oeis-cross-referencing](pages/oeis-cross-referencing.md)] — the discipline that caught the real/imaginary error.
- [[aocp-generating-functions](pages/aocp-generating-functions.md)] — why a linear recurrence gives a rational GF, and the partial-fractions → `Re((1+i)^{L+1})` closed form (the Fibonacci method).
- [[generating-functions-topic](pages/generating-functions-topic.md)] — the imaginary-roots worked example `1/(1+z²) → ½(iⁿ+(−i)ⁿ)`, the exact mechanism of `Re((1+i)^{L+1})`.
- [[recurrence-discovery](pages/recurrence-discovery.md)] — the orders `k+1` (L-direction) and `2L−2` (k-direction, L ≥ 4), verified by Berlekamp–Massey.
- [[generating-function-gallery](pages/generating-function-gallery.md)] — the `num_k/den_k` rational GFs and their roots (the characteristic polynomials above).
- [[tower-parity-sectors](pages/tower-parity-sectors.md)] - `P = P_even + P_odd` by last-column parity; the sectors are the factors of `char_k`, `P_even(6,L) = 2^L·A005251(L+3)`, and `P_even(4m+2, L)/2^L` are Hardin's word counts.
- [[convergents-oeis-crosswalk](pages/convergents-oeis-crosswalk.md)] - the k-direction characteristic polynomial is `(x+1)^L (x−1)^{L−2}`, so `P(·,L)` is a quasi-polynomial in `k`; and the exact split `P(6,L) = 2^L·A005251(L+3) + (order-4 remainder)`, tying the `k = 6` row to the plastic number `ψ` via its dominant eigenvalue `2ψ²`.

## Footnotes

[^1]: [[oeis-mining-pe502](pages/oeis-mining-pe502.md)] `mine-notes.md` §"Vein 1" L31-37 — "The general P(k,·) family is C-finite of order k+1: P(1): x^2 - 2x + 2 ... P(5): x^6 - 6x^5 + 18x^4 - 32x^3 + 48x^2 - 32x + 32 (constant term = (-1)^{k-1} 2^k; leading coeff -(k+1))."
[^2]: [[oeis-mining-pe502](pages/oeis-mining-pe502.md)] `mine-notes.md` §"Vein 1" L19-29 — "The plan states P(1,L) = A009545(L+1). This is wrong. A009545 is the imaginary part of (1+i)^n ... P(1,L) = Re((1+i)^{L+1}) = A146559(L+1) ... P(1,L) = 0,-2,-4,-4,0,8,16,16,..."; re-verified during ingest.
[^3]: [[oeis-mining-pe502](pages/oeis-mining-pe502.md)] `crosslink-avenues.md` §"Tier 1 / 3. A146559" L25-32 — "a(n) = P(1, n−1) ... a genuinely new Formula ... a(n) = A038503(n) − A038505(n) (verified: Re((1+i)^n) = Σ_{j≡0} − Σ_{j≡2} binomial)."
[^4]: [[oeis-mining-pe502](pages/oeis-mining-pe502.md)] `crosslink-avenues.md` §"Generation material" L104-105 — "P(k,L) signed towers, k ≥ 2 — new C-finite family (P(2,·): 1,3,9,19,33,59,… order 3; P(4,·): 1,5,25,85,225,541,… order 5), generalizing A146559."
