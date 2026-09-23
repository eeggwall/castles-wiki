---
title: Prime convex castles - unimodal compositions with no part 1
category: Analyses
summary: "A prime convex castle is a convex castle with no height-1 column, a unimodal composition into parts >= 2. By area they are U = 1, 1, 2, 3, 5, 8, 12, 19, 28, 42, ... (n >= 2), which follows Fibonacci until (3,2,3) at n = 8 and has no OEIS match. U is exactly the second difference of A001523, by stripping a height-1 column from each end, and it is the convex castle GF by area and width at z = q, the convex castles raised one row. So U(n) ~ π^2/(3n) · A001523(n), with the ratio approaching 1 like 1 - O(n^-1/2). The first difference of A001523, convex castles whose first column is not 1, is A342528, compositions with alternating parts weakly decreasing, checked through area 120 but not noted on either OEIS entry. The Fibonacci gap F_{n-1} - U, the width triangle and the parity splits are novel-candidates."
tags: [analysis, castle, area, composition, prime-castle, convex-castle, unimodal, stack-polyomino, fibonacci, asymptotics, parity, q-series, oeis, interlink, novel-candidate]
sources: [oeis-mining-pe502]
created: 2026-09-22
updated: 2026-09-22
---

# Prime convex castles

On [[prime-castles](pages/prime-castles.md)], castles glued at a shared height-1 column form a free monoid whose primes are the castles with no height-1 column. A [[convex-castle](pages/convex-castle.md)] has its height-1 columns only in an initial run and a final run, `C = (1^a, X, 1^b)`, so its factorization is

```
(1, C, 1) = (1,1)^a ∘ (1, X, 1) ∘ (1,1)^b
```

It has at most one nontrivial prime, `X`, and `X` is convex. This page counts those `X`: the **prime convex castles**, convex castles with no height-1 column. They are the [[weakly-unimodal-composition](pages/weakly-unimodal-composition.md)]s with every part `≥ 2`. The all-ones castle `(1^n)` is the one convex castle with no nontrivial prime.

## The sequence

| `n` | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| prime convex `U(n)` | 1 | 1 | 2 | 3 | 5 | 8 | 12 | 19 | 28 | 42 | 61 | 90 | 127 | 183 | 257 | 361 | 500 | 694 | 948 |
| all prime, `F_{n-1}` | 1 | 1 | 2 | 3 | 5 | 8 | 13 | 21 | 34 | 55 | 89 | 144 | 233 | 377 | 610 | 987 | 1597 | 2584 | 4181 |
| gap `F_{n-1} - U(n)` | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 2 | 6 | 13 | 28 | 54 | 106 | 194 | 353 | 626 | 1097 | 1890 | 3233 |

`U(n) = 0` at `n = 1`. It continues `1298, 1757, 2374, 3184, 4262, 5661, 7508, 9899, 13016, 17033` for `n = 21..30`.[^1] Every composition into parts `≥ 2` is unimodal through `n = 7`, so `U` is Fibonacci up to there. At `n = 8`, `(3, 2, 3)` is the first one that dips, and from then on the gap takes over. `F_{n-1}` grows like `φ^n` and `U` grows subexponentially, so almost every prime castle is non-convex. `U`, the gap, and `U` without its leading term have no OEIS match. All are novel-candidates.[^2]

## Three descriptions of `U`

**1. A stack GF with the 1s removed.** Split a unimodal composition at the first occurrence of its largest part `k`. On the left is a partition into parts in `[2, k - 1]`, then one or more copies of `k`, then another partition into parts in `[2, k - 1]` on the right:

```
U(q)  =  sum_{k >= 2}  q^k / ((1 - q^k) (q^2; q)_{k-2}^2)
```

This is the stack GF of [[stack-polyomino-gf](pages/stack-polyomino-gf.md)] with `(q; q)_{k-1}` replaced by `(q^2; q)_{k-2}` (own derivation; checked against brute force through area 18).

**2. The second difference of A001523.** For `n ≥ 2`,

```
U(n)  =  a(n) - 2 a(n-1) + a(n-2),        a = A001523, a(0) = 1
```

Proof: putting a height-1 column in front, `C ↦ (1, C)`, keeps a castle convex and is a bijection from the convex castles of area `n - 1` onto the convex castles of area `n` that begin with a height-1 column. So `a(n) - a(n-1)` counts the convex castles whose first column is not 1. Doing the same at the right end takes away the ones that end in a height-1 column, which leaves `U(n)`. Checked through area 1000.[^1] Equivalently, `A001523(q) - 1 = q/(1 - q) + U(q)/(1 - q)^2`, which counts the ways to place the prime `X` inside runs of height-1 columns. The `q/(1 - q)` term is the all-ones castles.

**3. Convex castles raised one row.** Subtracting 1 from every part turns a unimodal composition of `n` into `w` parts `≥ 2` into a unimodal composition of `n - w` into `w` parts. So with `K(q, z)` the convex castle GF by area and width, `U(q) = K(q, q)`. This is the convex case of the row-raising substitution `z → q` on [[prime-castles](pages/prime-castles.md)]. By width `w`, `U(n, w)` is the number of convex castles of area `n - w` and width `w`:

```
n =  2:  1
n =  4:  1  1
n =  6:  1  3  1
n =  8:  1  5  5  1
n = 10:  1  7 12  7  1
n = 12:  1  9 21 20  9  1
n = 14:  1 11 33 42 28 11  1
```

These are the even rows, with the columns `w = 1, 2, 3, ...`. The odd rows are `1; 1 2; 1 4 3; 1 6 8 4; 1 8 16 12 5; 1 10 27 30 16 6` for `n = 3, 5, ..., 13`. The `w = 2` column is `n - 3` because every pair is unimodal. The `w = 3` column counts triples `≥ 2` without a strict dip. The triangle has no OEIS match, so it is a novel-candidate.[^2]

## The first difference is A342528

The middle step of the proof above, `a(n) - a(n-1)` = convex castles whose first column is not 1, is

```
1, 2, 4, 7, 12, 20, 32, 51, 79, 121, 182, 272, 399, 582, 839, ...    (n = 2, 3, 4, ...)
```

This is A342528(n - 1), "Number of compositions with alternating parts weakly decreasing (or weakly increasing)", term by term for all 43 terms OEIS lists. Through area 120 it also agrees with Howroyd's generating function there, `sum_k ([y^k] P)([y^k] (1 + y) P)` with `P = prod 1/(1 - y x^k)`.[^3] Neither A342528 nor A001523 points to the other. So this is an **interlink**: a castle reading of A342528, and a cross-reference between the two entries. No bijection is known here. A convex castle not starting with 1 has one unimodal constraint, and an A342528 composition has two interleaved weakly decreasing chains. Matching the peak split `left | k^m | right` of description 1 against the odd and even subsequences is the natural first attempt.

## Asymptotics

Auluck's asymptotic for stacks, as given on OEIS A001523, is[^4]

```
a(n) ~ exp(2π sqrt(n/3)) / (8 · 3^(3/4) · n^(5/4))
```

A second difference of `exp(c sqrt(n))` multiplies it by `(c / (2 sqrt(n)))^2`, which here is `π^2 / (3n)`. So

```
U(n)  ~  (π^2 / (3n)) · a(n)  ~  π^2 exp(2π sqrt(n/3)) / (24 · 3^(3/4) · n^(9/4))
```

(own reasoning, not a proof). The ratio `3n U(n) / (π^2 a(n))` is `0.724, 0.811, 0.861, 0.898` at `n = 100, 250, 500, 1000`. The shortfall times `sqrt(n)` is about `2.8, 3.0, 3.1, 3.2`, consistent with a `1 - O(n^{-1/2})` approach. Convergence is slow, as it already is for Auluck's formula itself.[^1]

So a random convex castle of area `n` is prime with probability about `π^2/(3n)`. The exact value at `n = 100` is `2.38%`, against `3.29%` from the leading term.

## Parity

Adding a height-1 column at either end adds no block, so the second-difference proof keeps the block count. For `n ≥ 3`, `U_even = Δ^2 cev` and `U_odd = Δ^2 cod`, with `cev`/`cod` the convex parity split on [[castle-by-area](pages/castle-by-area.md)]. With `n = 2..18`:

| `n` | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| even blocks | 1 | 0 | 2 | 0 | 4 | 2 | 8 | 6 | 18 | 16 | 36 | 38 | 72 | 82 | 141 | 166 | 268 |
| odd blocks | 0 | 1 | 0 | 3 | 1 | 6 | 4 | 13 | 10 | 26 | 25 | 52 | 55 | 101 | 116 | 195 | 232 |
| even - odd | 1 | -1 | 2 | -3 | 3 | -4 | 4 | -7 | 8 | -10 | 11 | -14 | 17 | -19 | 25 | -29 | 36 |

A convex castle has the block parity of its prime. So `cev - cod = -q/(1 - q) + (U_even - U_odd)/(1 - q)^2`, where the first term is the one-block castles `(1^n)`. Checked through area 18. The signed prime count alternates and stays far below `U`: `36` against `500` at `n = 18`. At `n = 18` the full convex split is exactly balanced, `cev = cod = 2752`. None of the three rows has an OEIS match, as signed terms or absolute values.[^2]

## Computation

The second difference and the A342528 comparison, through area 120:

```python
N = 120
def div(a, j):                                   # a / (1 - q^j)
    a = a[:]
    for i in range(j, N + 1): a[i] += a[i - j]
    return a
def stacks(lo):                                  # unimodal compositions, parts >= lo
    tot, pref = [0] * (N + 1), [1] + [0] * N
    for k in range(lo, N + 1):
        t = div([0] * k + pref[:N + 1 - k], k)   # q^k/(1 - q^k) · prefix
        tot = [x + y for x, y in zip(tot, t)]
        pref = div(div(pref, k), k)              # 1/(1 - q^k)^2 for the next peak
    return tot
a, U = stacks(1), stacks(2); a[0] = 1
assert all(U[n] == a[n] - 2 * a[n - 1] + a[n - 2] for n in range(2, N + 1))
print([a[n] - a[n - 1] for n in range(2, 20)])   # A342528 from offset 1
```

## Open

- A bijection between convex castles whose first column is not 1 and A342528's compositions with alternating parts weakly decreasing.
- The second term of the asymptotic, the `c/sqrt(n)` correction with `c ≈ 3.3`, from the second term of Auluck's expansion.
- A closed form for `U_even - U_odd`. By description 3 it is minus the signed convex castle GF by area and width at `z = q`, since raising a castle one row adds one block.

## Relation to other pages

- [[prime-castles](pages/prime-castles.md)]: the free monoid, and the fact that a convex castle has at most one nontrivial prime.
- [[castle-by-area](pages/castle-by-area.md)]: A001523 and the `cev`/`cod` split whose second differences are computed here.
- [[stack-polyomino-gf](pages/stack-polyomino-gf.md)], [[weakly-unimodal-composition](pages/weakly-unimodal-composition.md)]: the stack GF that `U` restricts.
- [[convex-castle](pages/convex-castle.md)]: the convex castles counted by area and width in description 3.
- [[signed-klarner-decomposition](pages/signed-klarner-decomposition.md)]: the sign as a character, of which the convex parity here is the case with one letter.
- [[castle-sequence-catalogue](pages/castle-sequence-catalogue.md)]: statuses for the sequences on this page.

## Footnotes

[^1]: Computed by execution, 2026-09-22: brute-force unimodal compositions by area and width through area 18, and the stack GFs for parts `≥ 1` and `≥ 2` through area 1000 (block above, with `N` raised). The second-difference identity holds at every `2 ≤ n ≤ 1000`, and the parity versions at `3 ≤ n ≤ 18`. The asymptotic ratios are from the same run.
[^2]: OEIS searches (https://oeis.org/search, JSON format, 2026-09-22) returned no results for `U` (`1,1,2,3,5,8,12,19,28,42,61,90,...`, 11 and 17 terms, and `12,19,28,...,948` without the Fibonacci prefix), for the gap `1,2,6,13,28,54,106,194,353,626,1097`, for the width triangle read by rows (`1,1,1,1,1,2,1,3,1,1,4,3,1,5,5,1,1,6,8,4`), or for the parity rows and their difference (signed and absolute).
[^3]: https://oeis.org/A342528 (fetched 2026-09-22) - name "Number of compositions with alternating parts weakly decreasing (or weakly increasing)"; formula "G.f.: Sum_{k>=0} ([y^k] P(x,y))*([y^k] (1 + y)*P(x,y)), where P(x,y) = Product_{k>=1} 1/(1 - y*x^k). - Andrew Howroyd, Jan 16 2025"; data `1, 1, 2, 4, 7, 12, 20, 32, 51, 79, 121, ...` (43 terms, offset 0). Compared by execution, 2026-09-22: `A001523(n) - A001523(n-1) = A342528(n-1)` for `2 ≤ n ≤ 44` against the listed data and for `2 ≤ n ≤ 120` against Howroyd's GF. The A342528 comments, formulas and cross-references do not mention A001523.
[^4]: https://oeis.org/A001523 (fetched 2026-09-22) - "a(n) ~ exp(2*Pi*sqrt(n/3)) / (8 * 3^(3/4) * n^(5/4)) [Auluck, 1951]. - Vaclav Kotesovec, Jun 22 2015".
