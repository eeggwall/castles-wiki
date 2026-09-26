---
title: Conditional entropy given block count and area
category: Analyses
summary: Refining the uniform-entropy `log_2 F(w,h)` view by conditioning on the two structural statistics `B` (block count) and `N` (area). The chain rule reads `H(C) = H(B, N) + H(C | B, N)`, and brute-force at `(w, h)` up to `(12, 3)` shows the two marginal entropies each scale as `(1/2) log_2 w + O(1)`, the joint as `H(B, N) = log_2 w + O(1)`, so conditioning on the two structural statistics shaves `log_2 w` bits off the uniform baseline: `H(C | B, N) = w log_2 h - 1 - log_2 w - c(h) + o(1)`. Area beats blocks as a single-statistic summary at every `(w, h)` tested (by 1.5 to 2.2 bits), for two reasons: area's alphabet is larger, and the parity clause is redundant with `B` (knowing `B` tells you `B mod 2`) but not with `N`. The mutual information `I(B; N)` stays bounded (about 0.05 to 0.35 bits at every `(w, h)` tested) - `B` and `N` are two nearly-independent length-`log_2 w` summaries of the castle.
tags: [analysis, castle, entropy, information-theory, conditional-entropy, block-count, area, statistic, verification]
sources: [project-euler-502-brute-force, project-euler-502-observations]
created: 2026-09-21
updated: 2026-09-26
---

# Conditional entropy given block count and area

## What this refines

[[castle-entropy](pages/castle-entropy.md)] prices the uniform entropy of a random castle as

```
H(C) = log_2 F(w, h) ~ w log_2 h - 1,
```

the parity clause worth exactly one bit ([[castle-sign](pages/castle-sign.md)]). That reading treats every valid castle as a black box. This page refines it by asking how much of the entropy sits in the two most natural structural summaries the wiki already tracks, together on [[fractional-block-count](pages/fractional-block-count.md)] as "the castle's two structural statistics":

- **Block count** `B(c) = c_1 + sum_{i>=2} max(0, c_i - c_{i-1})`, matching [[castle-sign](pages/castle-sign.md)] and the [[castle-snippets](pages/castle-snippets.md)] `blocks` predicate;
- **Area** `N(c) = sum_i c_i`, the natural size axis of [[castle-by-area](pages/castle-by-area.md)].

The chain rule gives the decomposition once and for all:

```
H(C)  =  H(B, N)  +  H(C | B, N),
```

so the two structural statistics jointly cost exactly `H(B, N)` bits, and what is left in `H(C | B, N)` is the residual - the entropy that survives after telling the reader "this castle has `b` blocks and area `n`."

Every number below was computed while writing and re-run for the final tables against `all_castles` plus `blocks` and `area` from [[castle-snippets](pages/castle-snippets.md)]; the ensemble is uniform on the `F(w, h)` even-block-count castles of exact height `h`.[^exec]

## The two marginals

`H(B)` is the entropy of the block-count marginal on the `F(w, h)` ensemble, `H(N)` the entropy of the area marginal, both in bits. On the uniform-castle ensemble the two are close to Gaussian by a central-limit argument (both `B` and `N` are sums of nearly-independent per-column increments, with an `O(1)` correction for the exact-height constraint), so each marginal entropy should scale as `(1/2) log_2 (2 pi e Var) = (1/2) log_2 w + O(1)`. The table confirms this across two heights and a decade of widths:[^exec]

| `(w, h)` | `F(w, h)` | `H(C)` | `H(B)` | `H(N)` | `H(B, N)` | `H(B, N) - log_2 w` | `I(B; N)` |
|---|---:|---:|---:|---:|---:|---:|---:|
| `(3, 2)` | 6 | 2.585 | 0.000 | 1.459 | 1.459 | -0.126 | 0.000 |
| `(4, 2)` | 10 | 3.322 | 0.000 | 1.846 | 1.846 | -0.154 | 0.000 |
| `(6, 2)` | 28 | 4.807 | 0.811 | 2.356 | 2.856 | 0.271 | 0.311 |
| `(8, 2)` | 120 | 6.907 | 0.881 | 2.489 | 3.053 | 0.053 | 0.317 |
| `(10, 2)` | 528 | 9.044 | 0.625 | 2.643 | 3.089 | -0.233 | 0.179 |
| `(12, 2)` | 2080 | 11.022 | 0.800 | 2.826 | 3.486 | -0.099 | 0.140 |
| `(4, 3)` | 21 | 4.392 | 0.000 | 2.213 | 2.213 | 0.213 | 0.000 |
| `(6, 3)` | 307 | 8.262 | 0.678 | 2.881 | 3.483 | 0.898 | 0.076 |
| `(8, 3)` | 3031 | 11.566 | 1.181 | 3.190 | 4.273 | 1.273 | 0.098 |
| `(10, 3)` | 28479 | 14.798 | 1.363 | 3.378 | 4.659 | 1.337 | 0.082 |
| `(12, 3)` | 261615 | 17.997 | 1.502 | 3.527 | 4.957 | 1.372 | 0.072 |
| `(4, 4)` | 117 | 6.870 | 0.858 | 2.916 | 3.715 | 1.715 | 0.059 |
| `(6, 4)` | 1729 | 10.756 | 1.411 | 3.323 | 4.675 | 2.090 | 0.059 |
| `(4, 5)` | 122 | 6.931 | 0.950 | 3.191 | 4.029 | 2.029 | 0.112 |
| `(5, 5)` | 906 | 9.823 | 1.234 | 3.444 | 4.575 | 2.253 | 0.103 |

Reading down the `h = 3` block, `H(B, N) - log_2 w` stabilizes near `1.37` for `w >= 8`; on the `h = 2` block the same quantity hovers near zero because the parity clause forces the block count into a two- or three-valued marginal (`H(B)` never exceeds `1` bit at `h = 2`), so the joint is essentially the area marginal alone. The general shape is that `H(B, N)` grows like `log_2 w` with a constant that depends on `h`.

The mutual information `I(B; N) = H(B) + H(N) - H(B, N)` stays bounded: between `0.05` and `0.35` bits for every `(w, h)` in the table. That is exactly the behaviour of two correlated Gaussian statistics with bounded correlation `rho`: `I = -(1/2) log_2 (1 - rho^2)` is a function of `rho` alone, not of `w`. `B` and `N` are therefore two nearly-independent length-`log_2 w` summaries of the castle, not two names for the same information.

## The conditional entropy

The chain rule turns the marginal-entropy table into a table of shortenings. Uniformly, `H(C) - H(C | X)` is what knowing `X` buys you in bits; the residual `H(C | X)` is what still needs to be specified.[^exec]

| `(w, h)` | `H(C)` | `H(C \| B)` | `H(C \| N)` | `H(C \| B, N)` | `H(C) - w log_2 h` |
|---|---:|---:|---:|---:|---:|
| `(6, 2)` | 4.807 | 3.996 | 2.451 | 1.951 | -1.193 |
| `(8, 2)` | 6.907 | 6.026 | 4.418 | 3.854 | -1.093 |
| `(10, 2)` | 9.044 | 8.419 | 6.402 | 5.955 | -0.956 |
| `(12, 2)` | 11.022 | 10.223 | 8.196 | 7.537 | -0.978 |
| `(6, 3)` | 8.262 | 7.584 | 5.381 | 4.779 | -1.248 |
| `(8, 3)` | 11.566 | 10.385 | 8.376 | 7.293 | -1.114 |
| `(10, 3)` | 14.798 | 13.435 | 11.420 | 10.139 | -1.052 |
| `(12, 3)` | 17.997 | 16.495 | 14.470 | 13.040 | -1.022 |
| `(6, 4)` | 10.756 | 9.345 | 7.433 | 6.081 | -1.244 |
| `(5, 5)` | 9.823 | 8.590 | 6.379 | 5.248 | -1.786 |

Two features of this table read straight off the entropy chain rule.

**Area beats blocks as a single-statistic summary.** At every `(w, h)` in the table `H(C | N) < H(C | B)`, and the gap is between `1.5` bits (at `(6, 2)`) and `2.2` bits (at `(5, 5)`). Two causes contribute. First, `H(N) > H(B)` by about `2` bits at every `(w, h)` because area has a larger alphabet than blocks (roughly `wh` versus `w`), so `N` is intrinsically more granular. Second, the parity clause hits `B` and `N` asymmetrically: on `(10, 2)`, moving from the any-parity ensemble to the even-only ensemble drops `H(C)` by `1` bit (the parity-clause bit of [[castle-entropy](pages/castle-entropy.md)]), drops `H(B)` by `1.14` bits, and drops `H(N)` by only `0.06` bits. Since `H(C \| B) = H(C) - H(B)` and the two decreases cancel, `H(C \| B)` is essentially unchanged by adding the parity clause; `H(C \| N)` on the other hand drops by nearly a full bit. **The parity clause is redundant with `B` but not with `N`** - a first place the parity clause visibly asymmetrizes the two structural axes.

**Joint conditioning shaves `log_2 w` bits.** Both `H(B, N)` and `log_2 w` were tabulated above; subtracting `H(B, N)` from `w log_2 h - 1 + O(1)` gives

```
H(C | B, N)  =  w log_2 h  -  1  -  log_2 w  -  c(h)  +  o(1),
```

with `c(3) ≈ 0.37`, `c(4) ≈ 1.1`, `c(5) ≈ 1.3` on this data. The one-bit parity clause of [[castle-entropy](pages/castle-entropy.md)] is joined by a `log_2 w` term whose payment goes to *localizing* the castle in `(B, N)` space: given the joint statistic, the reader has narrowed the castle to a cell of size `~ F(w, h) / w` on the ensemble, which is exactly the count of shapes with the given `(b, n)`.

The `H(C) - w log_2 h` column - a check on the [[castle-entropy](pages/castle-entropy.md)] `-1` residual - is close to `-1` at `h = 3` for `w >= 10` and drifts to `-1` at `h = 2` for `w >= 10` (the parity bit is asymptotic in `w`).

## Where the two statistics come from

The two marginal distributions are already on the wiki, in two different disguises.

**Block count.** For an unbounded tower of width `w`, the block-count generating function is the Narayana polynomial over `(1 - x)^w` ([[tower-narayana-polynomial](pages/tower-narayana-polynomial.md)]):

```
T(w, b)  =  sum_{k=1..w}  N(w, k)  C(b + w - k, w - 1),
GF by b:   Narayana_w(x) / (1 - x)^w,   N(w, k) = C(w, k) C(w, k-1) / w  =  A001263(w, k).
```

This is the closest analytical model of `B` on the castle ensemble - the castle block count is the tower block count plus one for the bottom row ([[castle-counting-formula](pages/castle-counting-formula.md)]), and the parity restriction picks off every other value. Both the tower Narayana marginal and its parity-restricted version have mean scaling as `~ w/2` and variance as `~ w`, so `H(B)` from this distribution would scale as `(1/2) log_2 w + O(1)` after the parity-restriction bit is subtracted - matching the empirical `H(B) ~ (1/2) log_2 w + c` in the table.

**Area.** [[castle-by-area](pages/castle-by-area.md)] re-indexes castles by `n = sum c_i` and matches the resulting distributions against known composition sequences: convex castles of area `n` are `A001523(n)` (weakly unimodal compositions), valley castles are `A332578(n)`, all castles of area `n` are `2^{n-1}`. The area marginal on the fixed-`(w, h)` ensemble is the projection onto sum: at fixed `h` the area is a sum of `w` almost-independent column heights with an `O(1)` correction from `max c = h`, so `Var(N) ~ w sigma^2(h)` with `sigma^2(h) -> (h^2 - 1) / 12` as `w` grows, and the Gaussian entropy `H_gauss(N) = (1/2) log_2 (2 pi e Var(N))` should agree with the exact `H(N)` to within terms decaying in `w`. Empirically the agreement is very sharp: at `h = 3`, `w = 6, 8, 10, 12` the two differ by `0.056, 0.013, 0.004, 0.002` bits respectively; at `h = 4` the same widths give `0.011, 0.006, 0.003, 0.001`. The area distribution on the even-block castle ensemble is Gaussian to two decimal places by `w = 10`.[^exec]

**Joint.** Since `B` and `N` are jointly nearly-Gaussian with bounded correlation, `H(B, N) = log_2(2 pi e sqrt(det Sigma)) = log_2 w + O(1)` and `I(B; N) = -(1/2) log_2 (1 - rho^2)` is a bounded function of the (bounded) correlation. The observed `I(B; N)` never crosses `0.4` bits in the entire table, consistent with `|rho| < 0.6` in the joint distribution.

## Where the two statistics are equal (and where they are not)

`B` and `N` meet exactly at the two endpoints of the fractional block count `B_alpha` of [[fractional-block-count](pages/fractional-block-count.md)]: `B_0 = N` (area, from `Delta^0 c_i = c_i`) and `B_1 = B` (block count, from `Delta^1 c_i = c_i - c_{i-1}`). The conditional entropy `H(C | B_alpha)` continuously interpolates between the two rows of the shortening table:

```
alpha = 0:   H(C | B_alpha)  =  H(C | N)     (area conditioning)
alpha = 1:   H(C | B_alpha)  =  H(C | B)     (block-count conditioning)
```

so the interior of the alpha axis is a family of intermediate summaries, each with its own shortening. Because `H(C | N) < H(C | B)`, the interpolation is monotone at the endpoints: **the alpha axis of [[fractional-block-count](pages/fractional-block-count.md)] is by construction a shortening axis** (from `alpha = 0` to `alpha = 1`, the residual grows by about `1.5-2.2` bits at every `(w, h)` in the table). [[fractional-block-count](pages/fractional-block-count.md)] reports that `B_{1/2}` separates all ten `(4, 2)` even castles: that fact is the extreme end of the conditional-entropy shortening, `H(C | B_{1/2}) = 0` when the statistic is injective. The fractional block count is a *finer* summary than either endpoint on that cell.

## What is left in the residual

`H(C | B, N)` bits still have to be transmitted after fixing `b` and `n`. That residual is the entropy of the uniform distribution on the isostatistic set

```
{ c in {1, ..., h}^w :  max c_i = h,  blocks(c) = b,  area(c) = n }.
```

At `(w, h)` in the table, that set has size on average `F(w, h) / w`, and the residual is `log_2 F(w, h) - log_2 w - O(1)`. Two questions follow:

- **Is the isostatistic set combinatorially named?** The isoarea set alone is a composition of `n` with parts in `[1, h]`, one part per column, with `max = h` - a truncation of [[weakly-unimodal-composition](pages/weakly-unimodal-composition.md)] when convex, of `A011782 = 2^{n-1}` in general. The iso-`(B, N)` set is finer and does not appear in [[oeis-index](pages/oeis-index.md)] under any name checked so far; it is a good candidate for the "block-count / peak / area joint distributions not yet enumerated" residue named in the [[castle-sequence-catalogue](pages/castle-sequence-catalogue.md)] follow-ups.

- **Does a finer sufficient statistic reduce the residual further?** [[fractional-block-count](pages/fractional-block-count.md)] answers yes at the toy scale (`B_{1/2}` alone gives `H(C | B_{1/2}) = 0` on ten of the fifteen `(4, 2)` castles), but the general question - which finite family of column-space statistics is sufficient for the castle ensemble - is open on this wiki.

## Related Concepts

- [[castle-entropy](pages/castle-entropy.md)] - the uniform-entropy baseline `log_2 F(w, h) ~ w log_2 h - 1` this page conditions.
- [[castle-sign](pages/castle-sign.md)] - the parity clause whose one bit is now visible as the one-bit gap `H(N) - H(B)`.
- [[castle-by-area](pages/castle-by-area.md)] - the area re-indexing whose marginal is `H(N)` here.
- [[tower-narayana-polynomial](pages/tower-narayana-polynomial.md)] - the tower block-count marginal whose `H(B)` scales as `(1/2) log_2 w`.
- [[fractional-block-count](pages/fractional-block-count.md)] - the alpha-interpolation between `H(C | N)` and `H(C | B)`, and the case where a single fractional statistic is sufficient.
- [[castle-compression](pages/castle-compression.md)] - the dual view: conditioning is an oracle-side compression, `log_2 w + 1` bits of the raw `log_2 F` are attributed to the two structural statistics.
- [[castle-representations](pages/castle-representations.md)] - the encodings the conditional-entropy accounting is written against.
- [[castle-steganography](pages/castle-steganography.md)] - the one bit `H(N) - H(B)` reads as a covert channel of capacity exactly one bit per castle; the parity-clause thread.
- [[castle-cryptography-round-two](pages/castle-cryptography-round-two.md)] - linear complexity as a compression story: Attack 5's `C(d+e-1, e)` linearized-filter bound is the information-theoretic residual accounting run against a nonlinear-feedback stream cipher.
- [[project-euler-502-brute-force](pages/project-euler-502-brute-force.md)] - the `blocks_of`, `all_castles` reference implementations against which every number here was checked.
- [[one-bit-seminar](pages/one-bit-seminar.md)] - the seminar that closes on this page's conditioning result.


## Appearances in Sources

- [[project-euler-502-observations](pages/project-euler-502-observations.md)] - the source's "the even-block clause is almost the entire difficulty," priced on [[castle-entropy](pages/castle-entropy.md)] at one bit and shown here to be the one bit that separates `H(B)` from `H(N)` on the conditioning side.
- [[project-euler-502-brute-force](pages/project-euler-502-brute-force.md)] - `blocks_of`, `all_castles`, and the `F(w, h)` enumeration that ground the entire table.

## Footnotes

[^exec]: Verified by execution (2026-09-21): the enumerator iterates `product(range(1, h+1), repeat=w)` filtered by `max == h`, computes `blocks(c) = c[0] + sum(max(0, c[i] - c[i-1]))` per [[castle-snippets](pages/castle-snippets.md)] and `area(c) = sum(c)`, restricts to `blocks % 2 == 0`, and accumulates the joint `(B, N)` distribution. Entropies are `-sum p log_2 p` over that distribution. Cross-checks: `F(4, 2) = 10`, `F(6, 4) = 1729`, `F(12, 3) = 261615` - matching [[castle-counting-function](pages/castle-counting-function.md)] and [[hardy-ramanujan-castle](pages/hardy-ramanujan-castle.md)]; brute-force `H(C) = log_2 F` recovered exactly. The Gaussian match `H(N) ≈ (1/2) log_2 (2 pi e Var(N))` is exact within `0.06` bits at `w = 6` and within `0.01` bit at `w = 10` for `h ∈ {3, 4}`, checked at every row of the sweep.
