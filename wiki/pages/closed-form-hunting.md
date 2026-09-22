---
title: Closed-form hunting for P(k,L)
category: Analyses
summary: Closed forms of P(k,L) in k for small L — P(k,2) = (−1)^k(k+1) (proved), P(k,3) = (−1)^k(k+1)² — and why the pattern stops at L=3, the order jumping to 2L−2 for L ≥ 4.
tags: [analysis, castle, closed-form, c-finite, verification]
sources: [project-euler-502-castle-factoring, oeis-mining-pe502]
created: 2026-09-14
updated: 2026-09-19
---

# Closed-form hunting for P(k,L)

## Overview

`P(k,L)` — the [[castle-sign](pages/castle-sign.md)] signed tower count — has a **closed form in `k`** for the smallest widths `L`, and this page hunts for how far that goes. The result: the pattern extends through `L = 1, 2, 3`, then **stops** — for `L ≥ 4` the order of `P(·,L)` jumps to `2L−2` and no polynomial-in-`k` form exists. This page is the closed-form sibling of [[recurrence-discovery](pages/recurrence-discovery.md)] (which tabulates the orders); the computation — the column-height dynamic program (DP) for `P(k,L)` plus Berlekamp–Massey for the minimal recurrence — is that page's program, and everything below is verified by execution.

## The small-L closed forms

In the *k*-direction (fixed `L`, vary the height), `P(k,L)` collapses for `L ≤ 3`:

| L | P(k,L) | characteristic polynomial |
|---|---|---|
| 1 | `(1 + (−1)^k) / 2` | `1 − x²` |
| 2 | `(−1)^k (k+1)` | `(1 + x)²` |
| 3 | `(−1)^k (k+1)²` | `(1 + x)³` |

`P(k,1) = ∑_{c=0}^{k} (−1)^c = (1 + (−1)^k)/2` is the alternating sum of `1`s. `P(k,2)` and `P(k,3)` are the two forms the hunt set out from — except that the usual statement of `P(k,2)` as `(−1)^{k(k+1)}` is wrong: `k(k+1)` is always even, so that expression is identically `1`. The correct form is `(−1)^k(k+1)`, proved next.

## The P(k,2) = (−1)^k(k+1) proof

A width-2 tower is its two column heights `a, b ∈ {0,…,k}`, and its block count (the total descent, with `c_0 = c_3 = 0`) is[^1]

```
blocks = max(0, a − b) + b = max(a, b).
```

So `P(k,2) = ∑_{a,b} (−1)^{max(a,b)}`. Group the `(k+1)²` pairs by `m = max(a,b)`: for `m ≥ 1` there are `2m+1` pairs (`(m, 0..m)` and `(0..m−1, m)`), and `m = 0` contributes the single pair `(0,0)` — `2m+1` pairs for every `m = 0..k`. Hence

```
P(k,2) = ∑_{m=0}^{k} (2m+1)(−1)^m = (−1)^k (k+1),
```

using `∑_{m=0}^{k} (−1)^m = (1+(−1)^k)/2` and `∑_{m=0}^{k} m(−1)^m = ((−1)^k(2k+1)−1)/4`. Verified for all `k ≤ 12`, and by the `(1+x)²` recurrence for all `k`.

`P(k,3) = (−1)^k(k+1)²` has characteristic polynomial `(1+x)³` and is verified the same way (Berlekamp–Massey finds the minimal order-3 recurrence), but is not derived here.

## The single-polynomial form stops at L = 3

The `(1+x)^L` characteristic polynomial — which would give `P(k,L) = (−1)^k(k+1)^{L−1}` — holds only for `L = 2, 3` (`L = 1` is the degenerate parity form). At `L = 4` it breaks: the minimal recurrence has order **6, not 4**, so there is no `(1+x)⁴ = (−1)^k(k+1)³` closed form. The order then grows as `2L−2` for every `L ≥ 4`, and the characteristic polynomial factors over the integers as `(x+1)^L (x−1)^{L−2}` for every `L` up to 12 tested - palindromic for even `L`, anti-palindromic for odd `L` (the reciprocal-symmetry signature of the transfer matrix):

```
L=4: [1, 2, −1, −4, −1, 2, 1]     = (x+1)⁴(x−1)²
L=5: [1, 2, −2, −6, 0, 6, 2, −2, −1] = (x+1)⁵(x−1)³
L=6: [1, 2, −3, −8, 2, 12, 2, −8, −3, 2, 1] = (x+1)⁶(x−1)⁴
```

with orders `6, 8, 10` respectively (`2L−2 = L + (L−2)`, the multiplicity sum).[^2] Every k-direction eigenvalue is `±1`, so `P(k,L)` *does* have a closed form in `k` for every `L` - a period-2 **quasi-polynomial** `P(k,L) = (−1)^k A_L(k) + B_L(k)` with `deg A_L = L−1` and `deg B_L = L−3`:

```
P(k,4) = (−1)^k (k+1)(2k+1)(2k+3)/6 + (k+1)/2
P(k,5) = (−1)^k k(k+1)²(k+2)/3     + (k+1)²
```

What stops at `L = 3` is the *single-polynomial* form `(−1)^k (k+1)^{L−1}`: from `L = 4` on, a non-alternating part `B_L` appears and the alternating part `A_L` stops being a pure power. The full `A_L, B_L` table to `L = 8`, the Online Encyclopedia of Integer Sequences (OEIS) hits (`|P(k,4)|` is A352116, the partial sums of the odd triangular numbers) and the code are on [[signed-tower-k-direction](pages/signed-tower-k-direction.md)].

## Conclusion

There is **no single-polynomial closed form** for `P(k,L)` as a function of `k` beyond `L = 3`: the forms `(−1)^k(k+1)` and `(−1)^k(k+1)²` exist exactly for `L = 2, 3` (plus the parity form at `L = 1`). From `L = 4` onward the closed form is a **two-polynomial quasi-polynomial** - even `k` and odd `k` each follow their own degree-`(L−1)` polynomial - which is the same thing as the order-`(2L−2)` recurrence with characteristic polynomial `(x+1)^L (x−1)^{L−2}`. A uniform formula for the pair `A_L, B_L` is still open ([[signed-tower-k-direction](pages/signed-tower-k-direction.md)]). The *L*-direction is the opposite: it has clean closed forms (`P(1,L) = Re((1+i)^{L+1})`, and a degree-`(k+1)` rational generating function (GF) for every `k`), collected on [[signed-tower-count](pages/signed-tower-count.md)].[^2]

## Appearances in Sources

- [[project-euler-502-castle-factoring](pages/project-euler-502-castle-factoring.md)] — the descent formula for the block count used in the `P(k,2)` proof.
- [[oeis-mining-pe502](pages/oeis-mining-pe502.md)] — the `P(k,·)` C-finite family and its order-`(k+1)` characteristic polynomials.

## Related Concepts

- [[recurrence-discovery](pages/recurrence-discovery.md)] — the orders in both directions that this page's closed forms live inside.
- [[signed-tower-count](pages/signed-tower-count.md)] — `P(k,L)` as a C-finite family; the L-direction closed forms.
- [[castle-sign](pages/castle-sign.md)] — the definition of `P` as the signed tower count.
- [[berlekamp-massey](pages/berlekamp-massey.md)] — the tool that recovers the `(1+x)^L` and palindromic polynomials.
- [[signed-tower-k-direction](pages/signed-tower-k-direction.md)] - the `(x+1)^L (x−1)^{L−2}` factorization, the quasi-polynomial table `A_L, B_L`, and its OEIS hits.
- [[aocp-binomial-coefficients](pages/aocp-binomial-coefficients.md)] — `Σ_k (−1)^k C(n,k) = 0`, the alternating sum whose degenerate case `P(k,1) = (1 + (−1)^k)/2` opens the hunt.

## Footnotes

[^1]: [[project-euler-502-castle-factoring](pages/project-euler-502-castle-factoring.md)] §"The sign of a castle" L105-113 — "blocks = ∑_{i=0}^{L} max(0, c_i - c_{i+1}), c_0 = c_{L+1} = 0."
[^2]: [[oeis-mining-pe502](pages/oeis-mining-pe502.md)] `mine-notes.md` §"Vein 1" L31-37 — "The general P(k,·) family is C-finite of order k+1 ..."; the k-direction orders and the palindromic/anti-palindromic polynomials are verified by execution (see [[recurrence-discovery](pages/recurrence-discovery.md)]).
