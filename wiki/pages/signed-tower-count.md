---
title: Signed tower count P(k,L)
category: Concepts
summary: P(k,L) = Σ (−1)^blocks over towers of height ≤ k above a length-L block; a C-finite family of order k+1, with P(1,L) = Re((1+i)^{L+1}) = A146559(L+1).
tags: [concept, castle, signed-count, c-finite, oeis, generating-functions]
sources: [oeis-mining-pe502, project-euler-502-solution]
created: 2026-09-13
updated: 2026-10-06
---

# Signed tower count P(k,L)

## Description

`P(k,L)` is the signed tower count — the sum of `(−1)^{blocks}` over all towers of height at most *k* above a length-*L* block — the object that encodes the even-block rule in the [[castle-counting-formula](pages/castle-counting-formula.md)] and plays the role of the permutation sign sum on [[castle-sign](pages/castle-sign.md)]. This page collects its sequence structure as surfaced by the [[oeis-mining-pe502](pages/oeis-mining-pe502.md)] pass. The width `L` is indexed from 0 — the empty tower (zero columns, zero blocks) is a tower — so `P(k,0) = 1` for every `k`; the sequences below begin at `L = 0`, whereas the OEIS notes quoted in the footnotes list them starting at `L = 1`.

**Indexing.** `k` counts layers above the castle's bottom row: a tower with tallest column `k` plus the bottom row is a castle of height `k + 1`. `P(k, ·)` sums over all towers with column heights in `{0, …, k}` and enters the castle formula as `P(h−1, w)` and `P(h−2, w)`, so it is a parity ingredient of `F(w, k+1)` and `F(w, k+2)`; `P(0, L) = 1` is the trivial case. `P(1, L)` enters `F(w, 2)` and `F(w, 3)` ([[castle-notation](pages/castle-notation.md)]).

For fixed *k*, `P(k,·)` is **C-finite** (satisfies a linear recurrence) of order `k+1`, with characteristic polynomials:[^1]

```
P(1):  x² − 2x + 2                        (eigenvalues 1 ± i)
P(2):  x³ − 3x² + 4x − 4    = (x−2)(x²−x+2)
P(3):  x⁴ − 4x³ + 8x² − 8x + 8
P(4):  x⁵ − 5x⁴ + 12x³ − 20x² + 16x − 16
P(5):  x⁶ − 6x⁵ + 18x⁴ − 32x³ + 48x² − 32x + 32
```

Each is monic, with coefficient of `x^k` equal to `−(k+1)` and constant term `(−1)^{k−1} 2^k`. This is the C-finiteness that [[berlekamp-massey](pages/berlekamp-massey.md)]/[[kitamasa](pages/kitamasa.md)] exploit to evaluate `P` at trillion scale.

## The k = 1 case

At `k = 1`, `P(1,L) = ∑_b (−1)^{runs(b)}` over binary strings, which is the real part of a complex power:[^2]

```
P(1,L) = Re((1+i)^{L+1}) = A146559(L+1)      (A146559: GF (1−x)/(1−2x+2x²))
```

with values `P(1,L) = 1, 0, −2, −4, −4, 0, 8, 16, 16, 0, −32, …` from `L = 0` (re-verified during ingest). Its companion **A009545 is the imaginary part `Im((1+i)^n)`**, and `P(1,L) = A009545(L+3)/2` is a shifted, halved copy, which is why [[oeis-cross-referencing](pages/oeis-cross-referencing.md)] checks matches against OEIS data with offsets.[^2]

**At height 2, odd minus even is not constant.** At height 2, the number of castles of width `w` with an odd number of blocks minus the number with an even number is `P(1,w) − 1 = A146559(w+1) − 1`. The `−1` removes the all-zero string, which has no column at height 2. Each castle of height 2 has a fixed sign `(−1)^{blocks}`, but no pairing of the height-2 castles cancels these signs down to a constant. The castles of height 2 and width 2 show this. There are three, with top rows ■□, □■ and ■■. Each has 2 blocks (the bottom block and one block in row 2), so all three are even, and odd minus even is `−3 = A146559(3) − 1`.[^5]

For castles of height 2 and any width `L`, the sign sum is `P(1,L)`: the sum of `(−1)^r` over the binary strings of length `L`, where the 1s mark the columns at height 2 and `r` is the number of runs of 1s (the number of blocks in row 2). For this height-2 sum, read a string left to right and track two signed counts: strings ending in 0 and strings ending in 1. Appending a 0 to either kind gives a string ending in 0. Appending a 1 continues a run after a 1, or starts a new run after a 0, which flips the sign. At height 2, one column therefore multiplies the pair by the matrix `[[1,1],[−1,1]]`, whose eigenvalues are `1 ± i`, and this gives `P(1,L) = Re((1+i)^{L+1})`.[^6] It is the real-part half of the A146559 comment `(1+i)^n = a(n) + A009545(n)·i`.[^7] Since `1 + i = √2·e^{iπ/4}`, `P(1,L) = 2^{(L+1)/2} cos((L+1)π/4)`. At height 2, each unit of width turns the angle by 45°, so the signs of `P(1,L)` repeat with period 8 (`+, 0, −, −, −, 0, +, +` from `L = 0`). The modulus of `P(1,L)` grows by `√2` per unit of width, a factor of 2 every two units; exactly, `(1+i)^4 = −4` gives `P(1,L+4) = −4·P(1,L)`. For `w ≥ 1` the value `P(1,w)` is never 2, so at height 2 odd minus even is never 1. At height 2 it is −1 when `w ≡ 1 (mod 4)`, where `P(1,w) = 0`.

Both components are castle counts. Splitting `P(1,L)` by the parity of the last column height gives `P_even(1,L) = Re((1+i)^L) = A146559(L)` and `P_odd(1,L) = −Im((1+i)^L) = −A009545(L)`: A009545(w) is the number of castles of width `w` and height 2 whose last column reaches height 2 with an even number of blocks, minus those with an odd number. The split is the `k = 1` case of the sector decomposition on [[tower-parity-sectors](pages/tower-parity-sectors.md)], which for even `k` is what factors `char_k`.

## OEIS status of the family

The mining pass left five results about the `P(k,·)` rows:

- **`A146559` and the height-2 pair.** `a(n) = P(1,n−1)`, the real part of `(1+i)^n` read as a signed castle count, and the formula `A146559(n) = A038503(n) − A038505(n)` tying the signed vein to the height-2 [[hyperbolic-sequence-family](pages/hyperbolic-sequence-family.md)].[^3] A146559 carries `a(n) = A038503(n) − A038505(n)` and A038503 carries the equivalent `a(n) = A038505(n) + A146559(n)` ([[oeis-height2-hyperbolic-castles](pages/oeis-height2-hyperbolic-castles.md)], [[castle-sequence-catalogue](pages/castle-sequence-catalogue.md)]).
- **`P(2..6, ·)` have no OEIS match.** The `k ≥ 2` rows generalize A146559 and have no OEIS match, in signed or absolute-value form, searched 2026-09-18 ([[castle-sequence-catalogue](pages/castle-sequence-catalogue.md)]).[^4]
- **The even-`k` rows are positive** (checked `k ≤ 12`, `L < 40`). `P(2,·): 1,1,3,9,19,33,59,…` (order 3), `P(4,·): 1,1,5,25,85,225,541,…` (order 5), `P(6,·): 1,1,7,49,231,833,2583,…` (order 7, char poly factoring with dominant root `2ψ²` — the plastic connection).
- **The odd-`k` rows change sign in runs**, because their dominant eigenvalues are a complex pair: `P(3,·): 1,0,−4,−16,−40,−64,−32,192,…` and `P(5,·): 1,0,−6,−36,−140,…`. Their characteristic polynomials are irreducible over `Q` in every case checked, which is proved only for `k = 2^m − 1` ([[char-k-eisenstein-at-two](pages/char-k-eisenstein-at-two.md)]).
- **The whole family has a Pell/Chebyshev closed-form denominator** (the `num`/`den` update matrix has eigenvalues `−x ± √(x²+1)`), worked out on [[generating-function-gallery](pages/generating-function-gallery.md)].

## Appearances in Sources

- [[oeis-mining-pe502](pages/oeis-mining-pe502.md)] — vein 1: the C-finite `P(k,·)` family, `P(1,L)=A146559(L+1)`, and the A009545 correction.
- [[project-euler-502-solution](pages/project-euler-502-solution.md)] — defines `P(k,L)` and derives the `k=1` case `Re((1+i)^{L+1})`.

## Related Concepts

- [[castle-sign](pages/castle-sign.md)] — `P` as the castle analogue of the permutation sign sum.
- [[castle-counting-formula](pages/castle-counting-formula.md)] — where `P(h−1,w)`, `P(h−2,w)` enter `F`.
- [[hyperbolic-sequence-family](pages/hyperbolic-sequence-family.md)] — `A146559 = A038503 − A038505` links the signed vein to height 2.
- [[oeis-cross-referencing](pages/oeis-cross-referencing.md)] — matching with offsets, as between A146559 and A009545.
- [[aocp-generating-functions](pages/aocp-generating-functions.md)] — why a linear recurrence gives a rational generating function (GF), and the partial-fractions → `Re((1+i)^{L+1})` closed form (the Fibonacci method).
- [[generating-functions-topic](pages/generating-functions-topic.md)] — the imaginary-roots worked example `1/(1+z²) → ½(iⁿ+(−i)ⁿ)`, the mechanism of `Re((1+i)^{L+1})`.
- [[recurrence-discovery](pages/recurrence-discovery.md)] — the orders `k+1` (L-direction) and `2L−2` (k-direction, L ≥ 4), verified by Berlekamp–Massey.
- [[generating-function-gallery](pages/generating-function-gallery.md)] — the `num_k/den_k` rational GFs and their roots (the characteristic polynomials above).
- [[castle-sign-kms-matrix](pages/castle-sign-kms-matrix.md)] - with block weight `t` the transfer matrix is diagonally similar to the KMS matrix `ρ^|a−b|`, `ρ = √t`; `P(k, L)` is the point `ρ = i`, and `P(1, L) = Re((1+i)^{L+1})` is its `2 × 2` case.
- [[tower-parity-sectors](pages/tower-parity-sectors.md)] - `P = P_even + P_odd` by last-column parity; the sectors are the factors of `char_k`, `P_even(6,L) = 2^L·A005251(L+3)`, and `P_even(4m+2, L)/2^L` are Hardin's word counts.
- [[castle-eigenvalue-oeis-crosswalk](pages/castle-eigenvalue-oeis-crosswalk.md)] - the k-direction characteristic polynomial is `(x+1)^L (x−1)^{L−2}`, so `P(·,L)` is a quasi-polynomial in `k`; and the exact split `P(6,L) = 2^L·A005251(L+3) + (order-4 remainder)`, tying the `k = 6` row to the plastic number `ψ` via its dominant eigenvalue `2ψ²`.
- [[block-count-constraints](pages/block-count-constraints.md)] - `P(1,L) = G_{1,L}(−1) = Σ_r (−1)^r C(L+1, 2r)`, the `m = 2` character sum on the height-1 block's block-count GF; the residue / sparse / semigroup trichotomy that generalizes the sign.
- [[new-sequence-fw3](pages/new-sequence-fw3.md)] - `F(w,3) = (3^w − 2^w − P(2,w) + P(1,w))/2`, the first castle row in which `P(2,·)` enters a public count.
- [[convex-core](pages/convex-core.md)] - `P(m-1, L)` is also the signed count of the `L` free columns hanging below a plateau at level `m` of a convex core, so `P(h-2,w) - P(h-1,w) = (-1)^h` times a sum over convex castles of products of `P`.
- [[oeis-mining-seminar](pages/oeis-mining-seminar.md)] - Stop 5 of the seminar uses the A009545 / A146559 pair as its offset example; P(1, L) = A009545(L+3)/2 is the halved relative.
- [[tower-heap](pages/tower-heap.md)] - the unsigned twin: the same tower's block count as a Narayana polynomial, rather than the signed count `P(k,L)`.


## Footnotes

[^1]: [[oeis-mining-pe502](pages/oeis-mining-pe502.md)] `mine-notes.md` §"Vein 1" L31-37 — "The general P(k,·) family is C-finite of order k+1: P(1): x^2 - 2x + 2 ... P(5): x^6 - 6x^5 + 18x^4 - 32x^3 + 48x^2 - 32x + 32 (constant term = (-1)^{k-1} 2^k; leading coeff -(k+1))."
[^2]: [[oeis-mining-pe502](pages/oeis-mining-pe502.md)] `mine-notes.md` §"Vein 1" L19-29 — "A009545 is the imaginary part of (1+i)^n ... P(1,L) = Re((1+i)^{L+1}) = A146559(L+1) ... P(1,L) = 0,-2,-4,-4,0,8,16,16,..."; re-verified during ingest.
[^3]: [[oeis-mining-pe502](pages/oeis-mining-pe502.md)] `crosslink-avenues.md` §"Tier 1 / 3. A146559" L25-32 — "a(n) = P(1, n−1) ... a(n) = A038503(n) − A038505(n) (verified: Re((1+i)^n) = Σ_{j≡0} − Σ_{j≡2} binomial)."
[^4]: [[oeis-mining-pe502](pages/oeis-mining-pe502.md)] `crosslink-avenues.md` §"Generation material" L104-105 — "P(k,L) signed towers, k ≥ 2 — new C-finite family (P(2,·): 1,3,9,19,33,59,… order 3; P(4,·): 1,5,25,85,225,541,… order 5), generalizing A146559."
[^5]: raw/oeis-pe502/xrefs/A146559-signed.md §"Identity (verified)" [synthesis] L23-28,L36-41 — `a(n) − 1 = odd(n−1, 2) − F(n−1, 2)` for `n ≥ 2` at height 2 only, verified by brute force over castles of height 2 for `w = 1..14`, with `−3` at `n = 3`; the castles of height 2 and width 2 were listed by hand and re-enumerated for `w = 1..12` on 2026-10-05.
[^6]: [[project-euler-502-solution](pages/project-euler-502-solution.md)] §"Recursion for P(k, L)" L94,L103,L108 — the `k = 1` (height-2) case `P(1, L)` only: "Split the strings by their last bit ... Appending a 0 never changes the run count; appending a 1 starts a new run exactly when the previous bit is 0." / "The matrix \begin{pmatrix}1 & 1 \\ -1 & 1\end{pmatrix} has eigenvalues 1 + i and 1 - i." / "P(1, L) = \operatorname{Re}((1+i)^{L+1})"
[^7]: https://oeis.org/A146559 (2026-10-05) — "(1+i)^n = a(n) + A009545(n)*i where i = sqrt(-1)" (Philippe Deléham, Feb 2013).
