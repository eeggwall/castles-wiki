---
title: Power-law memory strip rules
category: Analyses
summary: The 1-smooth strip rule |c_n − c_{n−1}| <= 1 with the first difference replaced by the Grunwald-Letnikov difference of order alpha, truncated to the last K columns, |sum_{k<K} (−1)^k C(alpha, k) c_{n−k}| <= 1. Its transfer matrix M(alpha, K) is a 0/1 matrix on the h^{K−1} windows of K − 1 columns, so its Perron root rho(alpha, K) is algebraic. At h = 2, rho(alpha, K) is nondecreasing in K for K <= 16 and takes, as exact minimal polynomials show, the plastic number at (1/2, 6), the supergolden constant at (1/2, 7) and (3/4, 4), the golden ratio at (1/2, 9), (3/4, 5), (3/4, 6), (9/10, 4) and (9/10, 5), and psi^2 at (9/10, 6). It is at most 2, and the gaps 2 − rho(alpha, K) shrink by factors of about 0.89, 0.84 and 0.82 per step at alpha = 1/2, 3/4, 9/10 for 11 <= K <= 16. At h = 3 and alpha = 1/2, 3/4, 9/10 the Perron root equals the h = 2 value for K <= 8, because every cyclic component of windows containing height 3 has a smaller Perron root. At alpha = 1 the rule is the 1-smooth strip, at alpha = 2 a rule on second differences (golden at h = 2), and at alpha = 5/4, 3/2 only the constant strips survive.
tags: [analysis, castle, fractional-calculus, grunwald-letnikov, transfer-matrix, non-markov, power-law-memory, perron-root, plastic-number, supergolden, golden-ratio, reachable-field, truncation, algebraic]
sources: [pe502-pell-castle-strip]
created: 2026-09-22
updated: 2026-10-16
---

# Power-law memory strip rules

A strip rule of [[castle-strip](pages/castle-strip.md)] is a condition on neighboring columns, so its transfer matrix has one state per height. The 1-smooth rule, for instance, is `|c_n − c_{n−1}| ≤ 1`. This page replaces the first difference in that rule by the Grunwald-Letnikov difference of order `α`, Equation (1) of [[fractional-block-count](pages/fractional-block-count.md)]. For `0 < α < 1` its weights `(−1)^k C(α, k)` are nonzero for every `k` and of size about `k^{−α−1}`, so the condition involves every earlier column. Truncated to the last `K` columns, the rule on the heights `{1, …, h}` is

```
| Σ_{k=0}^{K−1} (−1)^k C(α, k) c_{n−k} |  ≤  1        for every n ≥ K − 1.            (1)
```

Its state is the window `(c_{n−K+2}, …, c_n)` of the last `K − 1` columns, so its transfer matrix `M(α, K)` is a 0/1 matrix of size `h^{K−1}`, and the growth constant of its strips is the Perron root `ρ(α, K)` of `M(α, K)`, an algebraic number.

*Example.* At `α = 1/2` and `K = 6` the weights are `1, −1/2, −1/8, −1/16, −5/128, −7/256`. A column of height 2 after five columns of height 1 gives `2 − 0.75390625 = 1.24609375 > 1`, so the window `(1, 1, 1, 1, 1, 2)` is forbidden; a second column of height 2 after it, the window `(1, 1, 1, 1, 2, 2)`, gives `0.74609375` and is allowed.[^exec]

```python
import itertools
from fractions import Fraction

def gl_weights(alpha, K):
    w = [Fraction(1)]
    for k in range(1, K):
        w.append(w[-1] * (k - 1 - alpha) / k)
    return w

def transfer_edges(alpha, K, h):
    """Edges of M(alpha, K) on the windows (c_{n-K+2}, ..., c_n), oldest first."""
    w = gl_weights(alpha, K)
    edges = []
    for s in itertools.product(range(1, h + 1), repeat=K - 1):
        for c in range(1, h + 1):
            window = (c,) + s[::-1]                     # newest first
            if abs(sum(w[k] * window[k] for k in range(K))) <= 1:
                edges.append((s, s[1:] + (c,)))
    return edges
```

`ρ(α, K)` is the largest of the Perron roots of the strongly connected components of the graph of these edges.

## Integer orders

At an integer `α` the weights vanish for `k > α`, and Equation (1) is a condition on `α + 1` consecutive columns.

- **`α = 1`** is the 1-smooth rule `|c_n − c_{n−1}| ≤ 1`. At `h = 2` it allows every pair, growth 2. At `h = 3` it is the 1-smooth strip on `{1, 2, 3}`, growth `1 + √2`, the root of `λ² − 2λ − 1`, for every `K ≥ 2` ([[pell-castle-strip](pages/pell-castle-strip.md)]).[^1][^exec]
- **`α = 2`** bounds the second difference, `|c_n − 2c_{n−1} + c_{n−2}| ≤ 1`, for `K ≥ 3`; at `K = 2` the truncated condition is `|c_n − 2c_{n−1}| ≤ 1`, whose growth is 1 at `h = 2` and `h = 3`. For `K ≥ 3` the growth is `φ`, the root of `λ² − λ − 1`, at `h = 2`, and `1.897179`, the root of the irreducible quartic `λ⁴ − 2λ³ + λ² − λ − 1`, at `h = 3`.[^exec]

## Orders between 0 and 1, at height 2

`ρ(α, K)` at `h = 2`:[^exec]

| `α` \ `K` | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 12 | 14 | 16 |
|---|---|---|---|---|---|---|---|---|---|---|
| 1/4 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| 1/2 | 1 | 1 | **1.3247** | **1.4656** | 1.5385 | **1.6180** | 1.6324 | 1.7035 | 1.7653 | 1.8096 |
| 3/4 | **1.4656** | **1.6180** | **1.6180** | 1.7437 | 1.7885 | 1.8285 | 1.8622 | 1.9030 | 1.9320 | 1.9522 |
| 9/10 | **1.6180** | **1.6180** | **1.7549** | 1.8124 | 1.8545 | 1.8867 | 1.9101 | 1.9447 | 1.9634 | 1.9756 |

The bold entries are named algebraic numbers. Berlekamp-Massey on the strip counts gives the minimal polynomial of each Perron root exactly:[^exec]

- `1.3247` at `(1/2, 6)` is a root of `λ³ − λ − 1`, the plastic number `ψ` ([[plastic-number](pages/plastic-number.md)]);
- `1.4656` at `(1/2, 7)` and `(3/4, 4)` is a root of `λ³ − λ² − 1`, the supergolden constant ([[tree-castle-by-area](pages/tree-castle-by-area.md)]);
- `1.6180` at `(1/2, 9)`, `(3/4, 5)`, `(3/4, 6)`, `(9/10, 4)` and `(9/10, 5)` is a root of `λ² − λ − 1`, the golden ratio `φ` ([[metallic-means](pages/metallic-means.md)]);
- `1.7549` at `(9/10, 6)` is a root of `λ³ − 2λ² + λ − 1`, `ψ²`;
- `1.5385` at `(1/2, 8)` is a root of the irreducible sextic `λ⁶ − λ⁵ − λ³ − 1`.

The plastic number, the supergolden constant and `ψ²` are also Perron roots of 0/1 strip matrices on three heights ([[reachable-field-census](pages/reachable-field-census.md)], the section *Cubics at h = 3*). At `α = 1/4`, only the two constant strips survive for every `K ≤ 16`.

**Growth in `K`.** In every row of the table `ρ(α, K)` is nondecreasing in `K`, so the Perron root ratchets upward as the memory grows. At `h = 2` every window has at most two successors, so every row sum of `M(α, K)` is at most 2 and `ρ(α, K) ≤ 2`. The gaps `2 − ρ(α, K)` for `11 ≤ K ≤ 16` shrink by nearly constant factors:[^exec]

| `α` | `2 − ρ(α, 16)` | ratio of successive gaps, `K = 11` to `16` | log-log slope |
|---|---|---|---|
| 1/2 | `0.190` | `0.887, 0.885, 0.894, 0.893, 0.909` | `−1.52` |
| 3/4 | `0.048` | `0.843, 0.836, 0.839, 0.837, 0.840` | `−2.35` |
| 9/10 | `0.024` | `0.784, 0.800, 0.826, 0.816, 0.820` | `−2.80` |

The weights of the truncated tail decay like `k^{−α−1}`, so the truncation changes the left side of Equation (1) by `O(K^{−α})`. The log-log slopes are not `−α`, and over `K ≤ 16` the gaps fit a geometric decrease better than a power of `K`. The limit of `ρ(α, K)` as `K → ∞` is not determined by these values.

## Height 3

At `h = 3`, `ρ(α, K)` equals the value at `h = 2` for `α = 1/2` and `3 ≤ K ≤ 9`, and for `α = 3/4, 9/10` and `3 ≤ K ≤ 7`.[^exec] Windows containing height 3 do pass Equation (1): at `α = 1/2` and `K = 6`, 399 of the allowed windows contain a 3, among them the constant window `(3, 3, 3, 3, 3, 3)`, with value `0.738`. The strongly connected components that contain height 3 have smaller Perron roots than the component on the heights `{1, 2}`, which is the rule at `h = 2`:

| `α` | `K` | largest Perron root of a component containing height 3 | `ρ(α, K)` |
|---|---|---|---|
| 1/2 | 4 to 8 | 1 (the single window `(3, …, 3)`) | |
| 3/4 | 6, 7, 8 | `1.3247`, `1.4656`, `1.6013` | `1.6180`, `1.7437`, `1.7885` |
| 9/10 | 5, 6, 7, 8 | `1.4656`, `1.6180`, `1.6180`, `1.6536` | `1.6180`, `1.7549`, `1.8124`, `1.8545` |

So the windows containing a 3 add strips but do not change the growth constant in this range.

## Orders between 1 and 2

At `α = 5/4` and `α = 3/2` the Perron root is 1 for every `K ≤ 11` at `h = 2` and every `K ≤ 7` at `h = 3`: only the constant strips survive.[^exec] For fixed `K` and `h`, `M(α, K)` takes finitely many values as `α` varies, so `ρ(α, K)` is a step function of `α`; at `h = 2` it is 2 at `α = 1`, 1 at `α = 5/4` and `3/2`, and `φ` at `α = 2`. The growth constants of [[fractional-recurrences](pages/fractional-recurrences.md)], which vary continuously in `α`, belong to recurrences in the order `α`, not to strip rules.

## Appearances in Sources

- [[pe502-pell-castle-strip](pages/pe502-pell-castle-strip.md)] - the generating function `1/(1 − 2x − x²)` and its growth rate `1 + √2`, the growth of the 1-smooth strip on three heights.

## Related Concepts

- [[castle-strip](pages/castle-strip.md)] - strip rules on neighboring columns and their transfer matrices, of which Equation (1) is the version with memory `K`.
- [[fractional-block-count](pages/fractional-block-count.md)] - the same Grunwald-Letnikov difference applied to one skyline as a statistic.
- [[fractional-recurrences](pages/fractional-recurrences.md)] - recurrences of real order, whose growth constants form a continuous curve through the metallic means.
- [[fractional-width-and-height](pages/fractional-width-and-height.md)] - the castle counts interpolated to real width and height.
- [[reachable-field-census](pages/reachable-field-census.md)] - the Perron roots of 0/1 strip matrices on at most five heights, by number field.
- [[plastic-number](pages/plastic-number.md)] - `ψ` and `ψ²`, the Perron roots at `(1/2, 6)` and `(9/10, 6)`.
- [[tree-castle-by-area](pages/tree-castle-by-area.md)] - the supergolden constant as the growth by area of the tree skylines of height at most 2.
- [[metallic-means](pages/metallic-means.md)] - the golden ratio, and the silver mean `1 + √2` of the case `α = 1`, `h = 3`.
- [[pell-castle-strip](pages/pell-castle-strip.md)] - the 1-smooth strip on `{1, 2, 3}`, the case `α = 1`, `h = 3`.
- [[metallic-strip-realizability](pages/metallic-strip-realizability.md)] - which metallic means are Perron roots of strip rules on a given number of heights.
- [[eigenvalue-continued-fractions](pages/eigenvalue-continued-fractions.md)] - continued fractions of the castle eigenvalues, `φ` among them.

## Footnotes

[^1]: [[pe502-pell-castle-strip](pages/pe502-pell-castle-strip.md)] §"The generating function", §"The Pell fingerprint" [synthesis] L5, L52-54 - `D(x) = 1/(1 − 2x − x²)`, with coefficients `1, 2, 5, 12, 29, 70, 169, …` and "growth rate 1 + √2".
[^exec]: Verified by execution (Python 3.11 with NumPy and SymPy, 2026-10-16), with the weights in exact rational arithmetic: the example windows; the table of `ρ(α, K)` at `h = 2` for `α = 1/4, 1/2, 3/4, 9/10` and `4 ≤ K ≤ 16`, from the strongly connected components (eigenvalues for small components, power iteration on `A + I` for large ones); the minimal polynomials of the bold entries and of `ρ(1/2, 8)` by Berlekamp-Massey on the strip counts `1^T M^m 1` and factorization; `α = 1` at `h = 2, 3` and `α = 2` at `h = 2, 3` for `K ≤ 5`; the gap ratios and log-log slopes for `11 ≤ K ≤ 16`; the equality of the `h = 3` and `h = 2` values for the stated ranges, the counts of allowed windows containing a 3, and the Perron roots of the components containing a 3 (`K ≤ 8`); `ρ = 1` at `α = 5/4, 3/2` for `K ≤ 11` at `h = 2` and `K ≤ 7` at `h = 3`.
