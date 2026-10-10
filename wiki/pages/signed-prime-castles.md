---
title: Signed prime castles - the block sign as a character of the prime-castle monoid
category: Analyses
summary: "On the free gluing monoid of prime castles, blocks - 1 is additive, so the sign (-1)^(blocks-1) is a character. It factors through the abelianization and is constant on the castles built from one multiset of primes. Since χ = −(−1)^blocks, the signed identity 1/(1 − π_χ), with π_χ the signed prime series, reproduces the parity split odd − even of castles by area (with width it becomes the recursion on castle-row-raising-equation). A multiset of primes with multiplicities m_i gives k!/prod m_i! castles, and the number of multisets by area, 1, 2, 3, 5, 9, 15, 26, 45, 78, 134, ..., is the Euler transform of the prime counts (no OEIS match). Area, width, blocks, height-1 columns, peaks and base-leaving records are characters. Left-to-right maxima, height and B_alpha for 0 < alpha < 1 are not."
tags: [analysis, castle, area, prime-castle, monoid, character, parity, block-count, sign, multinomial, peaks, records, fractional, q-series, oeis, novel-candidate]
sources: [oeis-mining-pe502]
created: 2026-09-22
updated: 2026-10-10
---

# Signed prime castles

[[prime-castles](pages/prime-castles.md)] builds the free monoid `𝓜` of castles glued at a shared height-1 column. Its primes are `(1, X, 1)` with `X` free of height-1 columns, and every castle `C` enters `𝓜` padded as `(1, C, 1)`. This page adds the sign. PE 502's parity clause is a statement about `(-1)^blocks` ([[block-count-constraints](pages/block-count-constraints.md)]), and in `𝓜` that sign, shifted by one block, is multiplicative.

## The sign is a character

Gluing merges the two bottom rows and nothing else, so `blocks(x ∘ y) = blocks(x) + blocks(y) - 1`. So `β = blocks - 1` is a monoid homomorphism `𝓜 → (Z, +)`, and

```
χ(C) = (-1)^(blocks(C) - 1)
```

is a one-dimensional character, `χ(x ∘ y) = χ(x) χ(y)`. It is the negative of the castle sign `(−1)^blocks` of [[castle-sign](pages/castle-sign.md)], `χ(C) = −(−1)^{blocks(C)}`, and the shift is needed: gluing loses a block, so `(−1)^blocks` itself satisfies `(−1)^{blocks(x ∘ y)} = −(−1)^{blocks(x)} (−1)^{blocks(y)}`. Sums weighted by `χ` therefore give `odd − even`, where the signed series `E(q, z)` of [[castle-row-raising-equation](pages/castle-row-raising-equation.md)] gives `even − odd`. Since `𝓜` is free, a character is the same as a choice of value on each prime. Any homomorphism to an abelian group factors through the abelianization, the free commutative monoid on the primes. So **`χ` depends only on the multiset of a castle's prime factors**, not on their order. `𝓜` itself is not commutative: `(1,2,1) ∘ (1,3,1) = (1,2,1,3,1)` and `(1,3,1,2,1)` are different castles.

## The signed identity

Grade by reduced area, `area - 1`, and let `π_χ(q)` be the signed prime series, `π_χ = sum over primes p of χ(p) q^(area(p) - 1)`. The unsigned series is `π(q)` of [[prime-castles](pages/prime-castles.md)]. Then freeness gives

```
sum_{x in 𝓜} χ(x) q^(area(x) - 1)  =  1/(1 - π_χ),     1/(1 - π_χ) - 1 without the identity
```

A padded castle `(1, C, 1)` has reduced area `area(C) + 1` and the same blocks as `C`. So `[q^(n+1)] 1/(1 - π_χ) = odd(n) - even(n)`, the parity split of [[castle-by-area](pages/castle-by-area.md)] with the sign of `(-1)^(blocks-1)`. The coefficients of `π_χ` from reduced area 1 are the trivial prime `(1,1)` and then the signed no-height-1-column castles:

```
π_χ    = q - q^3 + q^4 - 2q^5 + 3q^6 - 3q^7 + 4q^8 - 5q^9 + 9q^10 - 14q^11 + 19q^12 - ...
1/(1-π_χ), from q^2:   1, 0, 0, -2, 0, -2, 4, -2, 12, -10, 20, -38, 44, -98, 136, -230
even(n) - odd(n):     -1, 0, 0,  2, 0,  2, -4, 2, -12, 10, -20, 38, -44, 98, -136, 230
```

The second and third rows are negatives of each other for `n = 1..16`. On `n ≤ 12` the `even`/`odd` values are exactly the source table's.[^1]

**With width, it is a recursion.** A nontrivial prime is a castle raised one row, so tracking width turns this identity into a `z → qz` functional equation that fixes the signed GF one area at a time. That, the signed counts to area 300, and their growth constant `1.62383` are on [[castle-row-raising-equation](pages/castle-row-raising-equation.md)].

## Castles per multiset of primes

A castle is a word in the primes, and the words with a given multiset of letters are its orderings. A multiset with `k` letters and multiplicities `m_1, ..., m_r` gives the multinomial

```
k! / (m_1! ... m_r!)
```

castles ([[aocp-multinomial-coefficients](pages/aocp-multinomial-coefficients.md)], [[aocp-multisets](pages/aocp-multisets.md)]). All of them share area, width, block count, sign and peak count, since those are all characters (next section). The castles of one class are the rearrangements of the segments between height-1 columns. So

```
odd(n) - even(n)  =  sum over multisets μ of reduced area n + 1 of  χ(μ) · k(μ)! / prod m_i(μ)!
```

The number of classes, meaning castles of area `n` up to permuting prime factors, is the Euler transform of the prime counts. With `π_j` the number of primes of reduced area `j` (`π_1 = 1` for `(1,1)`, `π_2 = 0`, `π_j = F_{j-2}` for `j ≥ 3`):

```
sum_n classes(n) q^(n+1)  =  prod_{j >= 1} (1 - q^j)^(-π_j)  -  1

classes(n), n = 1..17:  1, 2, 3, 5, 9, 15, 26, 45, 78, 134, 233, 401, 693, 1195, 2061, 3546, 6107
```

The first 16 terms were counted directly as distinct sorted factor lists over all castles, and the product formula matches them. The sequence has no OEIS match, so it is a novel-candidate.[^2] The partitions of a multiset on [[bender-1974-partitions-of-multisets](pages/bender-1974-partitions-of-multisets.md)] would enter only for unordered groupings of a castle's primes, not for these classes.

## Which statistics are characters

A statistic `f` is a character, after a shift, when `f(x ∘ y) = f(x) + f(y) - f((1))` on all of `𝓜`. For a free monoid this holds exactly when `f` is a sum of prime values. Each row below was tested on every pair of padded castles through area 6, and each "no" comes with a witness.[^3]

| statistic | character? | value on a prime `(1, X, 1)` | why |
|---|---|---|---|
| area - 1 | yes | `1 + area(X)` | cells add, one shared column |
| width - 1 | yes | `1 + width(X)` | |
| blocks - 1 | yes | `blocks(X) - 1`, or `0` for `(1,1)` | bottom rows merge, nothing else touches |
| height-1 columns - 1 | yes | `1` | the seam is one shared height-1 column |
| peaks | yes | `1`, or `0` for `(1,1)` | a peak on [[castle-foata-transform](pages/castle-foata-transform.md)] is a run of `c_i ≥ 2`, which never crosses a seam |
| records, base-leaving | yes | same as peaks | [[castle-foata-transform](pages/castle-foata-transform.md)] proves `#records = #peaks` |
| left-to-right maxima | no | | `(1,3,1) ∘ (1,2,1)` has 2, but `2 + 2 - 1 = 3` |
| height | no | | `max`, not a sum |
| `B_alpha`, `0 < alpha < 1` | no | | at `alpha = 1/2`, `B(1,2,1,3,1) = 4.6875` but `B(1,2,1) + B(1,3,1) - B(1) = 5` |

So peaks and records are characters, provided "record" means a column leaving the base as on [[castle-foata-transform](pages/castle-foata-transform.md)]. Read as left-to-right maxima of the column heights, records compare against the whole prefix and fail. The fractional block count of [[fractional-block-count](pages/fractional-block-count.md)] fails for the same reason: `Delta^alpha c_i` averages over every earlier column with a power-law weight, so the right factor feels the left one through the seam. The two endpoints, `B_0 = area` and `B_1 = blocks`, are characters, and the interior of the family is not.

**Weighted generating functions.** Any list of characters weights the primes and passes through `1/(1 - π)`, with `π` weighted accordingly. Marking peaks this way gives a rational GF for castles by area and peaks, and marking peaks and sign together gives a joint recursion. Both are on [[castle-row-raising-equation](pages/castle-row-raising-equation.md)].

## Computation

The signed identity through area 16, on top of `comps`, `blocks` and `primes` from [[prime-castles](pages/prime-castles.md)]:

```python
N = 16
pi_chi = [0] * (N + 2)                          # π_χ: signed primes by reduced area
for k in range(N + 1):
    for X in comps(k):
        if 1 not in X: pi_chi[1 + k] += (-1) ** (blocks((1,) + X + (1,)) - 1)
inv = [1] + [0] * (N + 1)                       # 1/(1 - π_χ)
for m in range(1, N + 2): inv[m] = sum(pi_chi[j] * inv[m - j] for j in range(1, m + 1))
for n in range(1, N + 1):
    even = sum(1 for c in comps(n) if blocks(c) % 2 == 0)
    assert inv[n + 1] == 2 ** (n - 1) - 2 * even # odd - even
```

## Open

- A sign-reversing involution between multiset classes. Every castle in a class has the same sign, so all cancellation in `odd - even` happens between classes; which classes pair off is open.

## Relation to other pages

- [[prime-castles](pages/prime-castles.md)]: the free monoid, the unsigned `π/(1 - π)` identity, and the prime parity tables.
- [[castle-row-raising-equation](pages/castle-row-raising-equation.md)]: the signed identity with width, as a recursion, and its growth constant.
- [[castle-by-area](pages/castle-by-area.md)]: the `even`/`odd` split this identity reproduces.
- [[castle-foata-transform](pages/castle-foata-transform.md)]: the peak and record definitions under which both are characters.
- [[fractional-block-count](pages/fractional-block-count.md)]: `B_alpha`, a character only at its endpoints.
- [[bender-1974-partitions-of-multisets](pages/bender-1974-partitions-of-multisets.md)], [[aocp-multinomial-coefficients](pages/aocp-multinomial-coefficients.md)]: the multiset side of counting castles per class.
- [[q-thread-seminar](pages/q-thread-seminar.md)] - the castles-by-area seminar, which uses this page as one of its stops.

## Footnotes

[^1]: Checked by execution, 2026-09-22 (block above), over every composition of `n ≤ 16`. The `even(n)` values reproduce raw/oeis-pe502/vein9-area.md §"Parity splits" L46-47 - "`even(n)` | 0, 1, 2, 5, 8, 17, 30, 65, 122, 261, 502, 1043 ... `odd(n)` | 1, 1, 2, 3, 8, 15, 34, 63, 134, 251, 522, 1005".
[^2]: Computed by execution, 2026-09-22: distinct sorted prime-factor lists over all castles of area `n ≤ 16`, and the Euler-transform product through `n = 17`. OEIS search (https://oeis.org/search, JSON format, 2026-09-22) for `2,3,5,9,15,26,45,78,134,233` and for the 16-term form returned no results.
[^3]: Checked by execution, 2026-09-22, over all 4225 ordered pairs from the 65 elements of `𝓜` up to area 8 (the identity, `(1,1)`, and every padded castle of area `≤ 6`): area, width, blocks, height-1 columns and peaks satisfy the shifted additivity on every pair; left-to-right maxima fail on 2329 pairs, height on 3249, and `B_{1/2}` on 4096. `B_alpha` computed as `sum_i max(0, sum_{k=0}^{i-1} (-1)^k C(alpha, k) c_{i-k})`, the definition on [[fractional-block-count](pages/fractional-block-count.md)].
