---
title: Signed prime castles - the block sign as a character of the prime-castle monoid
category: Analyses
summary: "On the free monoid of castles glued at a shared height-1 column, blocks − 1 is additive, so the sign χ = (−1)^(blocks − 1) is a character. It depends only on the multiset of a castle's prime factors. With π_χ(q) the signed prime series by reduced area, Σ χ(x) q^(area(x) − 1) = 1/(1 − π_χ) over the monoid, and its coefficients are the odd − even split of the castles by area, checked through area 16. A multiset of primes with multiplicities m_i gives k!/Π m_i! castles, and the number of such classes by area, 1, 2, 3, 5, 9, 15, 26, 45, 78, 134, …, is the Euler transform of the prime counts. Area, width, blocks, height-1 columns, peaks and base-leaving records are characters; left-to-right maxima, height and B_α for 0 < α < 1 are not."
tags: [analysis, castle, area, prime-castle, monoid, character, parity, block-count, sign, multinomial, peaks, records, fractional, q-series, oeis]
sources: [oeis-mining-pe502]
created: 2026-09-22
updated: 2026-10-16
---

# Signed prime castles

[[prime-castles](pages/prime-castles.md)] builds the free monoid `M` of castles glued at a shared height-1 column: `x ∘ y` merges the last column of `x` with the first column of `y`, both of height 1. Its primes are the castles `(1, X, 1)` with `X` free of height-1 columns, and every castle `C` enters `M` padded as `(1, C, 1)`. The identity is the castle `(1)`. This page adds the sign `(−1)^{blocks}` that the even-block condition of Project Euler 502 is about ([[block-count-constraints](pages/block-count-constraints.md)]).

## The sign is a character

Gluing merges the two bottom rows into one block and leaves every other block as it was, since the shared column has height 1. So `blocks(x ∘ y) = blocks(x) + blocks(y) − 1`, and `β = blocks − 1` is a monoid homomorphism `M → (Z, +)`. Hence

```
χ(C) = (−1)^{blocks(C) − 1}
```

is a character of `M`, a homomorphism to `{±1}`: `χ(x ∘ y) = χ(x) χ(y)`. Since `M` is free, a character is the same as a choice of value on each prime. Any homomorphism to an abelian group factors through the free commutative monoid on the primes, so **`χ` depends only on the multiset of a castle's prime factors**, not on their order. `M` itself is not commutative: `(1, 2, 1) ∘ (1, 3, 1) = (1, 2, 1, 3, 1)` and `(1, 3, 1) ∘ (1, 2, 1) = (1, 3, 1, 2, 1)` are different castles.

## The signed identity

Grade `M` by reduced area, `area − 1`, so that gluing adds reduced areas. Let

```
π_χ(q) = Σ_{primes p} χ(p) q^{area(p) − 1},
```

the signed prime series; it is written `π_χ` because `P` is the signed tower count and `A` the castle count, and `π` is the unsigned prime series of [[prime-castles](pages/prime-castles.md)]. Since `M` is free and `χ` is a character,

```
Σ_{x ∈ M} χ(x) q^{area(x) − 1}  =  1 / (1 − π_χ(q)),                                        (1)
```

and the sum without the identity is `π_χ/(1 − π_χ)`. A padded castle `(1, C, 1)` has reduced area `area(C) + 1` and the same number of blocks as `C`, so the coefficient of `q^{n+1}` in Equation (1) is `A^o(n) − A^e(n)`, the odd-block minus the even-block castles of area `n` ([[castle-by-area](pages/castle-by-area.md)]). The coefficients of `π_χ`, from reduced area 1, are the trivial prime `(1, 1)` and then the signed sums over the castles with no height-1 column:

```
π_χ                     = q − q³ + q⁴ − 2q⁵ + 3q⁶ − 3q⁷ + 4q⁸ − 5q⁹ + 9q¹⁰ − 14q¹¹ + 19q¹² − …
1/(1 − π_χ), from q²:     1, 0, 0, −2, 0, −2, 4, −2, 12, −10, 20, −38, 44, −98, 136, −230
A^e(n) − A^o(n):         −1, 0, 0,  2, 0,  2, −4, 2, −12, 10, −20, 38, −44, 98, −136, 230
```

The second and third rows are negatives of each other for `n = 1, …, 16`, and for `n ≤ 12` the even-block and odd-block counts are those of the source table.[^1]

**With width, it is a recursion.** A nontrivial prime is a castle raised one row, so marking width turns Equation (1) into a functional equation with `z → qz` that fixes the signed generating function one area at a time. That equation, the signed counts to area 300 and their growth constant `1.62383` are on [[castle-row-raising-equation](pages/castle-row-raising-equation.md)].

## Castles per multiset of primes

A castle is a word in the primes, and the words with a given multiset of letters are its rearrangements. A multiset with `k` letters and multiplicities `m_1, …, m_r` gives the multinomial coefficient

```
k! / (m_1! ⋯ m_r!)
```

castles ([[aocp-multinomial-coefficients](pages/aocp-multinomial-coefficients.md)], [[aocp-multisets](pages/aocp-multisets.md)]). All of them have the same area, width, block count, sign and number of peaks, since those are characters (section *Which statistics are characters*). The castles of one class are the rearrangements of the segments between height-1 columns. So

```
A^o(n) − A^e(n)  =  Σ_{multisets μ of reduced area n + 1}  χ(μ) · k(μ)! / Π_i m_i(μ)!
```

The number of classes, the castles of area `n` up to rearranging their prime factors, is the Euler transform of the prime counts. Let `π_j` be the number of primes of reduced area `j`: `π_1 = 1` for `(1, 1)`, `π_2 = 0`, and `π_j = F_{j−2}` for `j ≥ 3`, since `X` is a composition of `j − 1` into parts at least 2. Then

```
Σ_n classes(n) q^{n+1}  =  Π_{j ≥ 1} (1 − q^j)^{−π_j}  −  1

classes(n), n = 1, …, 17:   1, 2, 3, 5, 9, 15, 26, 45, 78, 134, 233, 401, 693, 1195, 2061, 3546, 6107
```

The first 14 terms agree with a direct count of the distinct sorted factor lists over all castles, and the product formula gives all 17.[^2] [[castle-sequence-catalogue](pages/castle-sequence-catalogue.md)] records the OEIS status of this sequence. The partitions of a multiset on [[bender-1974-partitions-of-multisets](pages/bender-1974-partitions-of-multisets.md)] count unordered groupings of a castle's primes, not these classes.

## Which statistics are characters

A statistic `f` is a character after a shift when `f(x ∘ y) = f(x) + f(y) − f((1))` on all of `M`. For a free monoid this holds exactly when `f` is a sum of values on the prime factors. Each row of the table was tested on every pair of padded castles through area 6, and each "no" comes with a witness.[^3]

| statistic | character? | value on a prime `(1, X, 1)` | reason |
|---|---|---|---|
| area − 1 | yes | `1 + area(X)` | cells add, with one shared column |
| width − 1 | yes | `1 + width(X)` | |
| blocks − 1 | yes | `blocks(X) − 1`, or `0` for `(1, 1)` | the bottom rows merge, and nothing else touches |
| height-1 columns − 1 | yes | `1` | the seam is one shared height-1 column |
| peaks | yes | `1`, or `0` for `(1, 1)` | a peak on [[castle-foata-transform](pages/castle-foata-transform.md)] is a maximal run of columns with `c_i ≥ 2`, which never crosses a seam |
| records leaving the base | yes | as for peaks | [[castle-foata-transform](pages/castle-foata-transform.md)] proves that their number equals the number of peaks |
| left-to-right maxima | no | | `(1, 3, 1) ∘ (1, 2, 1)` has 2, but `2 + 2 − 1 = 3` |
| height | no | | the height of a product is a maximum, not a sum |
| `B_α`, `0 < α < 1` | no | | at `α = 1/2`, `B(1, 2, 1, 3, 1) = 4.6875` but `B(1, 2, 1) + B(1, 3, 1) − B(1) = 5` |

Records are characters when a record means a column that leaves the base, as on [[castle-foata-transform](pages/castle-foata-transform.md)]; read as left-to-right maxima of the column heights they compare against the whole prefix and are not. The fractional block count `B_α` of [[fractional-block-count](pages/fractional-block-count.md)] is not a character for `0 < α < 1`, because `Δ^α c_i` is a weighted sum over all earlier columns, so the terms of the right factor depend on the left one. Its endpoints `B_0 = area` and `B_1 = blocks` are characters.

**Weighted generating functions.** For characters `f_1, …, f_r`, weighting each prime `p` by `t_1^{f_1(p)} ⋯ t_r^{f_r(p)}` turns Equation (1) into the weighted sum over `M`. Marking peaks gives a rational generating function for the castles by area and peaks, and marking peaks and the sign together gives a joint recursion; both are on [[castle-row-raising-equation](pages/castle-row-raising-equation.md)].

## Computation

The signed identity through area 16, with `comps`, `blocks` and `primes` from [[prime-castles](pages/prime-castles.md)]:

```python
N = 16
Ps = [0] * (N + 2)                              # signed primes by reduced area: pi_chi
for k in range(N + 1):
    for X in comps(k):
        if 1 not in X: Ps[1 + k] += (-1) ** (blocks((1,) + X + (1,)) - 1)
Ms = [1] + [0] * (N + 1)                        # 1/(1 - pi_chi)
for m in range(1, N + 2): Ms[m] = sum(Ps[j] * Ms[m - j] for j in range(1, m + 1))
for n in range(1, N + 1):
    even = sum(1 for c in comps(n) if blocks(c) % 2 == 0)
    assert Ms[n + 1] == 2 ** (n - 1) - 2 * even  # odd - even
```

## Relation to other pages

- [[prime-castles](pages/prime-castles.md)] - the free monoid, the unsigned identity `π/(1 − π)`, and the prime parity tables.
- [[castle-row-raising-equation](pages/castle-row-raising-equation.md)] - the signed identity with width, as a recursion, and its growth constant.
- [[castle-by-area](pages/castle-by-area.md)] - the even-block and odd-block castles by area, which Equation (1) reproduces.
- [[castle-foata-transform](pages/castle-foata-transform.md)] - the definitions of peaks and records under which both are characters.
- [[fractional-block-count](pages/fractional-block-count.md)] - `B_α`, a character only at `α = 0` and `α = 1`.
- [[bender-1974-partitions-of-multisets](pages/bender-1974-partitions-of-multisets.md)], [[aocp-multinomial-coefficients](pages/aocp-multinomial-coefficients.md)] - the multiset side of counting the castles in a class.
- [[q-thread-seminar](pages/q-thread-seminar.md)] - the seminar on castles by area, one of whose stops is this page.

## Footnotes

[^1]: Verified by execution (Python 3.11, 2026-10-16), over every composition of `n ≤ 16`: the coefficients of `π_χ` and of `1/(1 − π_χ)`, and `A^e(n) − A^o(n)`. The values for `n ≤ 12` reproduce raw/oeis-pe502/vein9-area.md §"Parity splits" L46-47 - "`even(n)` | 0, 1, 2, 5, 8, 17, 30, 65, 122, 261, 502, 1043 ... `odd(n)` | 1, 1, 2, 3, 8, 15, 34, 63, 134, 251, 522, 1005".
[^2]: Verified by execution (Python 3.11, 2026-10-16): the distinct sorted prime-factor lists over all castles of area `n ≤ 14`, and the Euler-transform product with `π_j = F_{j−2}` through `n = 17`.
[^3]: Verified by execution (Python 3.11, 2026-10-16), over all 4225 ordered pairs from the 65 elements of `M` up to area 8 (the identity `(1)`, `(1, 1)`, and every padded castle of area at most 6): area, width, blocks, height-1 columns and peaks satisfy the shifted additivity on every pair; left-to-right maxima fail on 2329 pairs, height on 3249, and `B_{1/2}` on 4096. `B_α` is computed as `Σ_i max(0, Σ_{k=0}^{i−1} (−1)^k C(α, k) c_{i−k})`, the definition on [[fractional-block-count](pages/fractional-block-count.md)].
