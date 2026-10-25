---
title: Prime convex castles - unimodal compositions with no part 1
category: Analyses
summary: "A prime convex castle is a convex castle with no column of height 1, a unimodal composition into parts at least 2. By area they number U = 1, 1, 2, 3, 5, 8, 12, 19, 28, 42, ... (n >= 2), which agrees with the Fibonacci numbers until the castle (3, 2, 3) at area 8. U is the second difference of A001523, by removing a height-1 column from each end, and it is the convex castle g.f. K(q, z) at z = q, the convex castles raised one row. The first difference of A001523, the convex castles whose first column is not 1, is A342528(n - 1), compositions with alternating parts weakly decreasing (checked through area 120). The ratio 3n U(n)/(pi^2 A001523(n)) is 0.724 to 0.898 for n = 100 to 1000. A prime convex castle of height h has h blocks, so the parity split of U is the split by the parity of the height."
tags: [analysis, castle, area, composition, prime-castle, convex-castle, unimodal, stack-polyomino, fibonacci, asymptotics, parity, q-series, oeis]
sources: [oeis-encyclopedia]
created: 2026-09-22
updated: 2026-10-25
---

# Prime convex castles

On [[prime-castles](pages/prime-castles.md)], castles that begin and end with a height-1 column form a free monoid under gluing at a shared height-1 column, and its primes are the padded castles `(1, X, 1)` with `X` a castle with no height-1 column. A [[convex-castle](pages/convex-castle.md)] has its height-1 columns only in an initial run and a final run, `C = (1^a, X, 1^b)`, so its padded form factors as

```
(1, C, 1)  =  (1, 1)^a ∘ (1, X, 1) ∘ (1, 1)^b
```

It has at most one nontrivial prime factor, `(1, X, 1)`, and `X` is convex. This page counts those `X`, the **prime convex castles**: convex castles with no column of height 1. By area they are the weakly unimodal compositions with every part at least 2 ([[weakly-unimodal-composition](pages/weakly-unimodal-composition.md)]). The flat row `(1^n)` is the one convex castle with no nontrivial prime factor.

*Example.* The castle `(1, 2, 3, 3, 1)` is `(1^1, X, 1^1)` with the prime convex castle `X = (2, 3, 3)`, and `(3, 2, 3)` is the smallest composition into parts at least 2 that is not unimodal.

## The sequence

| `n` | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| prime convex `U(n)` | 1 | 1 | 2 | 3 | 5 | 8 | 12 | 19 | 28 | 42 | 61 | 90 | 127 | 183 | 257 | 361 | 500 | 694 | 948 |
| all prime, `F_{n-1}` | 1 | 1 | 2 | 3 | 5 | 8 | 13 | 21 | 34 | 55 | 89 | 144 | 233 | 377 | 610 | 987 | 1597 | 2584 | 4181 |
| difference `F_{n-1} − U(n)` | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 2 | 6 | 13 | 28 | 54 | 106 | 194 | 353 | 626 | 1097 | 1890 | 3233 |

`U(1) = 0`, and `U(n)` continues `1298, 1757, 2374, 3184, 4262, 5661, 7508, 9899, 13016, 17033` for `n = 21, …, 30`.[^1] The compositions into parts at least 2 number `F_{n-1}`, and every one of them is unimodal through `n = 7`, so `U(n) = F_{n-1}` there; at `n = 8` the composition `(3, 2, 3)` is the first that dips. `F_{n-1}` grows like `φ^n` and `U(n)` subexponentially, so almost every prime castle is not convex.

## Three descriptions of U

**1. A stack generating function without parts 1.** Split a unimodal composition with largest part `k` at the first occurrence of `k`. On the left is a weakly increasing sequence of parts in `[2, k − 1]`, a partition; then one or more copies of `k`; then a weakly decreasing sequence of parts in `[2, k − 1]`, another partition. So

```
U(q)  =  Σ_{k ≥ 2}  q^k / ( (1 − q^k) (q^2; q)_{k−2}^2 ),        (q^2; q)_{k−2} = (1 − q^2)(1 − q^3) ⋯ (1 − q^{k−1}),     (1)
```

the stack generating function of [[stack-polyomino-gf](pages/stack-polyomino-gf.md)] with `(q; q)_{k−1}` replaced by `(q^2; q)_{k−2}`. Equation (1) agrees with brute force through area 18.[^1]

**2. The second difference of A001523.** For `n ≥ 2`, with `a = A001523` and `a(0) = 1`,

```
U(n)  =  a(n) − 2a(n−1) + a(n−2).                                              (2)
```

*Proof.* Putting a height-1 column in front, `C ↦ (1, C)`, keeps a castle convex and is a bijection from the convex castles of area `n − 1` onto the convex castles of area `n` that begin with a height-1 column, so `a(n) − a(n−1)` counts the convex castles whose first column is not 1. The same step at the right end removes those that end with a height-1 column and leaves `U(n)`.

Equation (2) holds at every `2 ≤ n ≤ 1000` (computed).[^1] Equivalently,

```
A001523(q) − 1  =  q/(1 − q)  +  U(q)/(1 − q)^2,
```

the convex castles being `(1^a, X, 1^b)` with `X` prime and `a, b ≥ 0`, or the flat rows, `q/(1 − q)`.

**3. Convex castles raised one row.** Subtracting 1 from every part maps the unimodal compositions of `n` into `w` parts at least 2 onto the unimodal compositions of `n − w` into `w` parts. So with `K(q, z)` the generating function of convex castles by area and width ([[castle-notation](pages/castle-notation.md)]), `U(q) = K(q, q)`, the convex case of [[castle-row-raising-equation](pages/castle-row-raising-equation.md)]. By width, `U(n, w)` is the number of convex castles of area `n − w` and width `w`:

```
n =  2:  1
n =  4:  1  1
n =  6:  1  3  1
n =  8:  1  5  5  1
n = 10:  1  7 12  7  1
n = 12:  1  9 21 20  9  1
n = 14:  1 11 33 42 28 11  1
```

These are the even rows, with columns `w = 1, 2, 3, …`. The odd rows are `1; 1 2; 1 4 3; 1 6 8 4; 1 8 16 12 5; 1 10 27 30 16 6` for `n = 3, 5, …, 13`. The `w = 2` column is `n − 3`, since every pair of parts is unimodal; the `w = 3` column counts the triples of parts at least 2 with no strict dip in the middle.[^1]

## The first difference is A342528

The middle step of the proof of Equation (2), `a(n) − a(n−1)`, the convex castles of area `n` whose first column is not 1, is

```
1, 2, 4, 7, 12, 20, 32, 51, 79, 121, 182, 272, 399, 582, 839, …        (n = 2, 3, 4, …)
```

This is `A342528(n − 1)`, "Number of compositions with alternating parts weakly decreasing (or weakly increasing)", for all 43 terms OEIS lists, and through area 120 it agrees with Howroyd's generating function there, `Σ_k ([y^k] P)([y^k] (1 + y) P)` with `P = Π_k 1/(1 − y x^k)`.[^2]

## Asymptotics

Auluck's asymptotic for stacks, as given on OEIS A001523, is[^3]

```
a(n)  ~  exp(2π sqrt(n/3)) / (8 · 3^{3/4} · n^{5/4}).
```

To first order, a second difference multiplies `exp(c sqrt(n))` by `(c / (2 sqrt(n)))^2`, which at `c = 2π/sqrt(3)` is `π^2/(3n)`. The computed ratio `3n U(n) / (π^2 a(n))` is `0.724, 0.811, 0.861, 0.898` at `n = 100, 250, 500, 1000`, and `(1 − ratio) · sqrt(n)` is `2.76, 2.99, 3.12, 3.21` there.[^1] At `n = 100` a convex castle of area 100 is prime with probability `U(100)/a(100) = 2.38%`, against `π^2/300 = 3.29%`.

## Parity

Adding a height-1 column at either end adds no block, so the proof of Equation (2) keeps the block count, and for `n ≥ 3` the even-block and odd-block prime convex castles are the second differences of the convex parity split `cev`, `cod` of [[castle-by-area](pages/castle-by-area.md)]. A convex castle of height `h` has exactly `h` blocks ([[convex-castle](pages/convex-castle.md)]), so the even-block prime convex castles are those of even height. With `n = 2, …, 18`:

| `n` | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| even blocks | 1 | 0 | 2 | 0 | 4 | 2 | 8 | 6 | 18 | 16 | 36 | 38 | 72 | 82 | 141 | 166 | 268 |
| odd blocks | 0 | 1 | 0 | 3 | 1 | 6 | 4 | 13 | 10 | 26 | 25 | 52 | 55 | 101 | 116 | 195 | 232 |
| even − odd | 1 | −1 | 2 | −3 | 3 | −4 | 4 | −7 | 8 | −10 | 11 | −14 | 17 | −19 | 25 | −29 | 36 |

A convex castle has the block parity of its prime factor, so

```
cev − cod  =  −q/(1 − q)  +  (U_even − U_odd)/(1 − q)^2,
```

where the first term is the flat rows `(1^n)`, each with one block; this agrees with enumeration through area 18. At `n = 18` the convex castles split evenly, `cev = cod = 2752`.[^1]

## Computation

Equation (2) and the A342528 comparison, through area 120:

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

## Related Concepts

- [[prime-castles](pages/prime-castles.md)] - the gluing monoid, and the factorization of a convex castle.
- [[castle-by-area](pages/castle-by-area.md)] - A001523 and the convex parity split `cev`, `cod`.
- [[stack-polyomino-gf](pages/stack-polyomino-gf.md)], [[weakly-unimodal-composition](pages/weakly-unimodal-composition.md)] - the stack generating function that Equation (1) restricts.
- [[convex-castle](pages/convex-castle.md)] - the convex castles counted by area and width in description 3, and their block count `h`.
- [[castle-row-raising-equation](pages/castle-row-raising-equation.md)] - raising a castle one row, `z → qz`.
- [[signed-prime-castles](pages/signed-prime-castles.md)] - the sign as a character of the gluing monoid.
- [[castle-sequence-catalogue](pages/castle-sequence-catalogue.md)] - the sequences on this page.

## Footnotes

[^1]: Verified by execution (Python 3.11, 2026-10-16): unimodal compositions by area, width and block parity by brute force through area 18, and the stack generating functions for parts at least 1 and at least 2 through area 1000 (the Computation block with `N` raised); Equation (2) at every `2 ≤ n ≤ 1000`; the width triangle; the parity rows and the identity for `cev − cod` through area 18, `cev = cod = 2752` at `n = 18`; the ratios at `n = 100, 250, 500, 1000` and `U(100)/a(100) = 0.023826`.
[^2]: https://oeis.org/A342528 (read 2026-10-16) - name "Number of compositions with alternating parts weakly decreasing (or weakly increasing)", data `1, 1, 2, 4, 7, 12, 20, 32, 51, 79, 121, ...` (43 terms, offset 0), and Howroyd's formula "G.f.: Sum_{k>=0} ([y^k] P(x,y))*([y^k] (1 + y)*P(x,y)), where P(x,y) = Product_{k>=1} 1/(1 - y*x^k)". Compared by execution, 2026-10-16: `A001523(n) − A001523(n−1) = A342528(n−1)` for `2 ≤ n ≤ 44` against the listed data and for `2 ≤ n ≤ 120` against Howroyd's generating function.
[^3]: https://oeis.org/A001523 (read 2026-10-16) - name "Number of stacks, or planar partitions of n; also number of weakly unimodal compositions of n", and "a(n) ~ exp(2*Pi*sqrt(n/3)) / (8 * 3^(3/4) * n^(5/4)) [Auluck, 1951]. - Vaclav Kotesovec, Jun 22 2015".
