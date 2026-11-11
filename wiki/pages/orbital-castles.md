---
title: Orbital castles
category: Concepts
summary: An orbital castle of order N repeats a period of N distinct heights from its first column, at width at least 2N, so every height appears at least twice, such as (1, 2, 3, 1, 2, 3). Each height has one successor, and the castle is the orbit of its first column. The orbital castles of order N and height h number C(h − 1, N − 1) N! at every width w ≥ 2N, and all orders together number A001339(h − 1) = 1, 3, 11, 49, 261, … from w = 2h on, the arrangements of {1, …, h} containing h. Each period adds the cyclic rise of the period, rise(c_1, …, c_N), to the block count, which lies between max − min and the sum of the top half of the period's heights minus the bottom half (N − 1 and ⌊N²/4⌋ on 1, …, N), so the block parity flips every period exactly when that rise is odd. Up to the starting column they are the cyclic orders, A000522(h − 1) = 1, 2, 5, 16, 65, …. The sign-alternating ones are those whose period alternates around its cycle, so N = 2m is even, and the alternating cyclic orders of 2m heights number the tangent numbers A000182(m) = 1, 2, 16, 272, …; at even N the periods of largest rise are among them. Every orbital castle of order at least 2 is plateau-free, the two-level ones are the order 2, the zig-zag ones lie on {h − 1, h}, and the palindromic ones are the box and the order 2 at odd width. The box is the orbital castle of order 1 and the crenellated castles of width at least 4, the battlement among them, are those of order 2; the battlements are the only orbital tree castles of height h ≥ 2, and the orbital castles that begin and end at height 1 are powers of one prime: a padded prime castle, or at height 1 the trivial prime (1, 1).
tags: [concept, castle, orbital-castle, periodic-castle, cyclic-permutation, arrangement, a001339, a000522, rise, alternating-permutation, tangent-number, a000182, zigzag, shape-type, block-count, parity, battlement, tree-castle, prime-castle, verification]
sources: [project-euler-502-brute-force]
created: 2026-10-31
updated: 2026-11-10
---

# Orbital castles

## Definition

A castle of width `w` and height `h` is a skyline `(c_1, …, c_w)` with `1 ≤ c_i ≤ h` and some `c_i = h` ([[castle-polyomino](pages/castle-polyomino.md)]). An **orbital castle of order `N`** repeats a period of `N` distinct heights from its first column, with width at least `2N`:

```
c_{i+N}  =  c_i   for 1 ≤ i ≤ w − N,        c_1, …, c_N distinct,        w  ≥  2N.
```

Each height in the period is followed by the next one, and the last by the first, so every height has one successor and the castle is the orbit of its first column under that cycle. As a strip rule on the heights of the period, a transfer matrix that is the permutation matrix of the cycle, it has one strip from each starting height at every width, so its growth by width is 1. The order `N` is the number of distinct heights. The width bound `w ≥ 2N` makes every height appear at least twice, so the castle shows its cycle repeating, where a width of `N + 1` would show each step of the cycle only once; the last period may stop part of the way, as in `(1, 2, 3, 1, 2, 3, 1)`. The period contains `h`, since some column has height `h`.

*Examples.*

- **Order 1:** the box `(h, h, …, h)`.
- **Order 2:** at width at least 4, the crenellated castles `(a, h, a, h, …)` and `(h, a, h, a, …)` with `a < h`, among them the battlements `(1, h, 1, h, …)` and `(h, 1, h, 1, …)`.
- **Order 3:** `(1, 2, 3, 1, 2, 3)`, and `(1, 2, 3, 1, 2, 3, 1)`, which ends partway through a period.
- **Order 7:** `(8, 1, 7, 2, 6, 3, 5)` repeated three times, a castle of width 21 and height 8.

*Non-examples.* `(1, 2, 1, 3)` is not orbital, since height 1 is followed once by 2 and once by 3. `(1, 2, 3, 1, 2)` repeats a period of three heights but has width 5 < 6, so height 3 appears once. `(2, 1, 3, 3, 3)` has one successor for each height, but its first column never comes back: it reaches a cycle only after a lead-in.

## Notation used on this page

| symbol | meaning |
|---|---|
| `N` | the order of an orbital castle, the number of distinct heights in its period |
| `A_orbital(w, h)`, `A_orbital(w, h; N)` | the orbital castles of width `w` and height `h`, and those of order `N` |
| `A^e_orbital(w, h)` | the even-block ones |
| `rise(c_1, …, c_N)` | the cyclic rise of the period, `Σ max(0, c_{i+1} − c_i)` for `i = 1, …, N` with `c_{N+1} = c_1`: the cyclic rise of [[tone-castle-catalog](pages/tone-castle-catalog.md)] taken over one period, not over the whole castle |
| `r` | the number of whole periods, the repeat count of a periodic castle |
| `χ` | the sign `(−1)^{blocks − 1}` of a castle that begins and ends at height 1 ([[signed-prime-castles](pages/signed-prime-castles.md)]) |

## Counts

The first `N` columns of an orbital castle of order `N` are `N` distinct heights, `h` among them, and they determine the castle. Choosing the other `N − 1` heights from `{1, …, h − 1}` and ordering all `N` gives

```
A_orbital(w, h; N)  =  C(h − 1, N − 1) · N!     for w ≥ 2N,  and 0 for w < 2N,
```

at every width from `2N` on. These are the entries of the triangle A121757, Pascal's triangle multiplied by `1, 2, 6, 24, 120, …`, at row `h − 1` and column `N − 1`.[^a121757] Different periods give different castles, since the period is the first `N` columns, so[^exec1]

```
A_orbital(w, h)  =  Σ_{N ≤ min(h, ⌊w/2⌋)}  C(h − 1, N − 1) · N!.
```

| `h` \ `w` | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| 2 | 1 | 1 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| 3 | 1 | 1 | 5 | 5 | 11 | 11 | 11 | 11 | 11 | 11 | 11 |
| 4 | 1 | 1 | 7 | 7 | 25 | 25 | 49 | 49 | 49 | 49 | 49 |
| 5 | 1 | 1 | 9 | 9 | 45 | 45 | 141 | 141 | 261 | 261 | 261 |
| 6 | 1 | 1 | 11 | 11 | 71 | 71 | 311 | 311 | 911 | 911 | 1631 |

A new order joins at every even width up to `2h`, and from `w = 2h` on the count no longer depends on the width:

```
A_orbital(w, h)  =  Σ_{k=0}^{h−1}  (k + 1)! · C(h − 1, k)  =  A001339(h − 1)  =  1, 3, 11, 49, 261, 1631, 11743, …     (w ≥ 2h).
```

The OEIS reads A001339 as "Number of arrangements of {1, 2, ..., n, n + 1} containing the element 1".[^a001339] That is the period: an orbital castle of height `h` and width at least `2h` is an arrangement of some of the heights `1, …, h` that contains `h`, written out to the width, and reflecting the heights, `x ↦ h + 1 − x`, turns it into an arrangement containing 1 with `n = h − 1`.[^exec2]

**Up to the starting column.** The `N` rotations of a period, `(c_j, …, c_N, c_1, …, c_{j−1})`, give `N` different orbital castles on the same cycle. Up to rotation an orbital castle of order `N` is a cyclic order of its heights, `C(h − 1, N − 1) · (N − 1)!` of them, and from `w = 2h` on

```
Σ_{k=0}^{h−1}  C(h − 1, k) · k!  =  A000522(h − 1)  =  1, 2, 5, 16, 65, 326, 1957, …     (w ≥ 2h).
```

Started at `h`, a cyclic order is `h` followed by an ordered list of distinct heights from `{1, …, h − 1}`, which the OEIS reads as the "Total number of permutations of all subsets of an n-set", with `n = h − 1`.[^a000522][^exec10]

## The rise per period

The **cyclic rise** `rise(c_1, …, c_N)` of the period counts the rises around the cycle once. A period's rises and falls balance, so it is half the cyclic total variation `Σ |c_{i+1} − c_i|`, and it is bounded by the heights the period uses. With `N` heights `s_1 < … < s_N`:

```
s_N − s_1   ≤   rise(c_1, …, c_N)   ≤   (s_N + s_{N−1} + ⋯ + s_{N−⌊N/2⌋+1})  −  (s_1 + s_2 + ⋯ + s_{⌊N/2⌋}).
```

*Proof.* The cycle climbs from `s_1` to `s_N` and comes back, so it rises by at least `s_N − s_1`, with equality exactly when it climbs once and falls once. For `N ≥ 2` each of the `N − 2` other heights then lies on the way up or the way down, so `2^{N−2}` cyclic orders reach the minimum. For the upper bound, write the total variation as `Σ (larger − smaller)` over the `N` steps of the cycle. Each height is an end of two steps, so it enters the sum with coefficient `+2` when it is larger than both of its neighbors, `−2` when it is smaller than both, and `0` otherwise. Every step has one larger and one smaller end, so the coefficients add up to 0: as many heights get `+2` as get `−2`, at most `⌊N/2⌋` of each, and the sum is at most twice the sum of the top `⌊N/2⌋` heights minus twice the sum of the bottom `⌊N/2⌋`. An alternating order reaches it: the top `⌊N/2⌋` heights alternate with the bottom `⌊N/2⌋`, and for odd `N` the median sits between a top height and a bottom one, with coefficient `0`. ∎

On the heights `1, …, N` the bounds are `N − 1` and `⌊N/2⌋ ⌈N/2⌉ = ⌊N²/4⌋`, the quarter-squares `1, 2, 4, 6, 9, 12` for `N = 2, …, 7` (A002620).[^a002620] The period `(8, 1, 7, 2, 6, 3, 5)` alternates high and low on the heights `{1, 2, 3, 5, 6, 7, 8}`, with the median 5 between 3 and 8, and has rise `6 + 4 + 2 + 3 = 15 = (8 + 7 + 6) − (1 + 2 + 3)`, the largest rise of the 720 cyclic orders of those heights; 72 of them reach it.[^exec3]

## Alternating periods

A period **alternates** when its cyclic steps alternate in sign, so that every height is above both of its neighbors around the cycle or below both. It then has as many rises as falls, so `N = 2m` is even. Cut at its top height, an alternating cyclic order of `2m` heights leaves the other `2m − 1` in an up-down order `p_1 < p_2 > p_3 < ⋯ > p_{2m−1}`, and every up-down order closes up into an alternating cycle through the top height. So the alternating cyclic orders of `2m` heights are counted by the up-down permutations of `2m − 1` letters, the tangent numbers:

```
A000111(2m − 1)  =  A000182(m)  =  1, 2, 16, 272, 7936, …     (N = 2m = 2, 4, 6, 8, 10, …).
```

A000111 counts "half the number of alternating permutations on n letters" for `n ≥ 2`, the up-down half, and its odd-indexed terms are A000182, the tangent numbers, with e.g.f. `tan(x)`.[^a000111][^a000182] An orbital castle shows every step of its cycle, so it is of the sign-alternating type, its differences `c_{i+1} − c_i` alternating in sign, exactly when its period alternates. Among these, the alternating castles, `c_1 > c_2 < c_3 > ⋯ < c_w` at odd width (the castles of plane trees, [[von-neumann-castles](pages/von-neumann-castles.md)]), are the ones whose period starts on a fall, half the rotations of each alternating period. At order `N = 2m` and width `w ≥ 2N`:[^exec9]

```
sign-alternating:  C(h − 1, 2m − 1) · 2m · A000182(m),
alternating:       C(h − 1, 2m − 1) · m · A000182(m)     (w odd).
```

At order 2 the sign-alternating ones are the crenellated castles, and the alternating ones are the `h − 1` that start at `h`, `(h, a, h, …, h)` at odd width. At order 4 and height 4 the two alternating cycles `(4, 1, 3, 2)` and `(4, 2, 3, 1)` give four alternating castles at each odd width `w ≥ 9`, the rotations that start on a fall; at `w = 9` they are `(4, 1, 3, 2, 4, 1, 3, 2, 4)`, `(4, 2, 3, 1, 4, 2, 3, 1, 4)`, `(3, 1, 4, 2, 3, 1, 4, 2, 3)` and `(3, 2, 4, 1, 3, 2, 4, 1, 3)`, beside the three of order 2.[^exec9] No odd order gives any, since an odd cycle steps the same way twice in a row somewhere: `(1, 2, 3)` rises from 1 to 2 to 3, and the period `(8, 1, 7, 2, 6, 3, 5)` from 3 to 5 to 8.

**At even order, the periods of largest rise alternate.** In the proof above, a period with `k` heights at coefficient `+2` and `k` at `−2` has total variation at most twice the sum of its top `k` heights minus twice the sum of its bottom `k`. For `k < N/2` that falls short of the bound, so a period of largest rise has `k = N/2`, every height above or below both neighbors. The alternating periods that reach the bound are exactly those whose heights above both neighbors are the top `N/2`.[^exec9]

## Blocks and parity

The block count of a castle is `c_1 + Σ max(0, c_{i+1} − c_i)`, its first column plus its rises.[^bf] A castle of width `w` takes `w − 1` steps; with `w − 1 = qN + t` and `0 ≤ t < N`, the steps go `q` times around the cycle and then `t` steps more, so

```
blocks  =  c_1  +  q · rise(c_1, …, c_N)  +  (the rises of the first t steps of the period).
```

For `r` whole periods that start at height `h`, this is the tone-burst count `blocks = c_w + r · rise(c_1, …, c_N)` of [[tone-castle-catalog](pages/tone-castle-catalog.md)]; the castle `(8, 1, 7, 2, 6, 3, 5)` repeated three times has `5 + 3 · 15 = 50` blocks.[^exec4] Each added period adds `rise(c_1, …, c_N)` blocks, so **the block parity flips with every period exactly when the period's rise is odd**, and it never changes when that rise is even.

For a fixed period of order `N`, the parity of its castle of width `w` depends only on `(w − 1) mod 2N`, so from `w = 2h` on the even-block count `A^e_orbital(w, h)` repeats in the width with a period dividing `2 lcm(1, …, h)`:[^exec7]

| `h` \ `w` | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 2 | 1 | 1 | 1 | 2 | 3 | 2 | 1 | 2 | 3 | 2 | 1 |
| 3 | 0 | 0 | 2 | 1 | 2 | 3 | 4 | 3 | 2 | 3 | 4 |
| 4 | 1 | 1 | 3 | 5 | 13 | 15 | 25 | 31 | 33 | 27 | 25 |
| 5 | 0 | 0 | 4 | 2 | 16 | 14 | 52 | 46 | 92 | 98 | 108 |
| 6 | 1 | 1 | 5 | 8 | 35 | 44 | 149 | 188 | 455 | 512 | 853 |

At heights 2 and 3 the period is 4, `1, 2, 3, 2` and `2, 3, 4, 3` from `w = 2h`.

## Overlaps with other families

**The box, the crenellated castles and the battlement.** The box `(h, …, h)` is the orbital castle of order 1. The orbital castles of order 2 are the crenellated castles `(a, h, a, h, …)` and `(h, a, h, a, …)` with `a < h` ([[castle-classification-shape](pages/castle-classification-shape.md)], Axis 7) of width at least 4, `2(h − 1)` of them at each width `w ≥ 4`; the crenellated castles of widths 2 and 3 are too short to be orbital, and the battlements `(1, h, 1, h, …)` and `(h, 1, h, 1, …)` are the two with `a = 1` ([[castle-notation](pages/castle-notation.md)], the battlement row).

**Tree castles.** A tree castle has no two neighboring columns both of height at least 2 ([[castle-graph](pages/castle-graph.md)]). The orbital tree castles are exactly the two battlements, at every width `w ≥ 4` and height `h ≥ 2`, and `(1, …, 1)` at height 1. A period of order `N ≥ 3` holds at most one height 1, so its other `N − 1` heights sit next to each other around the cycle, and the castle shows that pair; at order 2 the heights `{a, h}` give a tree castle only for `a = 1`. In the other direction, at each width `w ≥ 4` and height `h ≥ 2` every tree castle but the two battlements is not orbital: `(1, 2, 1, 3, 1)` is a tree castle, but height 1 is followed by both 2 and 3.[^exec5]

**Prime castles.** The castles that begin and end with a height-1 column form a free monoid under gluing at a shared height-1 column. Its primes are the padded prime castles `(1, X, 1)`, with `X` a castle that has no height-1 column, and the trivial prime `(1, 1)` ([[prime-castles](pages/prime-castles.md)]). An orbital castle whose period has no height 1 has no height-1 column, so it is not in the monoid. An orbital castle begins and ends at height 1 exactly when `c_1 = 1` and `N` divides `w − 1`; it is then `k = (w − 1)/N` copies of `(1, c_2, …, c_N, 1)` glued together. For `N ≥ 2` that is a padded prime castle and `k ≥ 2`, so the orbital castle is a power of one padded prime castle and never prime itself; of order `N ≥ 2` there are `C(h − 2, N − 2) · (N − 1)!` of them at each such width, one for each padded prime castle `(1, c_2, …, c_N, 1)` whose inner heights are distinct and include `h`. For `N = 1`, at height 1, the castle `(1, …, 1)` of width `w` is `w − 1` copies of the trivial prime `(1, 1)` glued together. The block count minus one adds up under gluing, and `(1, c_2, …, c_N, 1)` has `rise(c_1, …, c_N) + 1` blocks, so

```
blocks − 1  =  k · rise(c_1, …, c_N),        χ  =  (−1)^{k · rise(c_1, …, c_N)}  =  χ(1, c_2, …, c_N, 1)^k,
```

the per-period parity rule as the sign character of [[signed-prime-castles](pages/signed-prime-castles.md)] on a power of one prime.[^exec6]

**Periodic castles.** A periodic castle has `c_{i+p} = c_i` for `1 ≤ i ≤ w − p` with some period `p ≤ w/2`, so it runs for at least two periods, the last one possibly unfinished; the period may use a height more than once. An orbital castle is periodic, and its shortest period `(c_1, …, c_N)` uses each of its heights once; conversely, a skyline whose shortest period uses each of its heights once, and which runs for at least two periods, the last one possibly unfinished, is an orbital castle.

**Shape types.** The orbital castles meet the shape types of [[castle-classification-shape](pages/castle-classification-shape.md)] as follows, at every width `w ≥ 2N`:[^exec8]

- **Plateau-free**, `c_i ≠ c_{i+1}`: every orbital castle of order `N ≥ 2`, since neighboring columns are different heights of the period. The box is the only orbital castle with a plateau.
- **Two-level**, exactly two distinct heights: the orbital castles of order 2.
- **Zig-zag**, `|c_{i+1} − c_i| = 1`: only the two castles of order 2 on the heights `{h − 1, h}`, `(h − 1, h, h − 1, …)` and `(h, h − 1, h, …)`. A walk on distinct heights with steps `±1` never turns back, so its cycle closes only at `N = 2`.
- **Sign-alternating**, the differences alternating in sign: the orbital castles with an alternating period, `C(h − 1, 2m − 1) · 2m · A000182(m)` of order `2m` (section *Alternating periods*).
- **Palindromic**, `c_i = c_{w+1−i}`: only the box, and the orbital castles of order 2 at odd width. Read backwards, an orbital castle follows the inverse cycle, which differs from the cycle from order 3 on.
- **Fence-post**, `c_i = 1` at every even `i`: only the battlement `(h, 1, h, 1, …)`, and `(1, …, 1)` at height 1.
- **Moated**, `c_1 = c_w = 1` and every other `c_i ≥ 2`: only `(1, 1)`, since an orbital castle of order `N ≥ 2` that starts at height 1 returns to it at column `N + 1 < w`. The moated castles are the primes of the gluing monoid, `(1, 1)` the trivial one, and the orbital castles in the monoid are powers of one prime (paragraph *Prime castles*).

## Related Concepts

- [[tone-castle-catalog](pages/tone-castle-catalog.md)] - the cyclic rise of a skyline and the block count of a tone burst of whole periods.
- [[prime-castles](pages/prime-castles.md)], [[signed-prime-castles](pages/signed-prime-castles.md)] - the gluing monoid, its primes, and the sign character.
- [[castle-graph](pages/castle-graph.md)] - the tree castles, which meet the orbital castles in the battlements.
- [[castle-classification-shape](pages/castle-classification-shape.md)] - the shape types, among them the orbital castles, and the plateau-free, zig-zag, sign-alternating, palindromic, two-level, fence-post and moated types they meet.
- [[castle-notation](pages/castle-notation.md)] - `A_X(w, h)`, the cyclic rise, the battlement, and `N` as the order of an orbital castle.
- [[castle-classification](pages/castle-classification.md)] - the hub of the castle classification, where the orbital type sits among the shape types.

## Footnotes

[^bf]: [[project-euler-502-brute-force](pages/project-euler-502-brute-force.md)] §"Column-height encoding" L20-L24 - "A block is a maximal horizontal run of columns at a given level, so", "= c_1 + \sum_{i=2}^{w} \max(0, c_i - c_{i-1})".
[^a001339]: https://oeis.org/A001339 (read 2026-10-31) - "a(n) = Sum_{k=0..n} (k+1)! binomial(n,k).", data `1, 3, 11, 49, 261, 1631, 11743, 95901, 876809, ...`, and "Number of arrangements of {1, 2, ..., n, n + 1} containing the element 1. - _Emeric Deutsch_, Oct 11 2001".
[^a121757]: https://oeis.org/A121757 (read 2026-10-31) - "Triangle read by rows: multiply Pascal's triangle by 1,2,6,24,120,720,... = A000142.", offset 0, data `1, 1, 2, 1, 4, 6, 1, 6, 18, 24, ...`, and "Row sums are 1,3,11,49,261,1631,... = A001339".
[^a000522]: https://oeis.org/A000522 (read 2026-10-31) - "Total number of ordered k-tuples (k=0..n) of distinct elements from an n-element set: a(n) = Sum_{k=0..n} n!/k!.", offset 0, data `1, 2, 5, 16, 65, 326, 1957, 13700, 109601, ...`, and "Total number of permutations of all subsets of an n-set."
[^a000111]: https://oeis.org/A000111 (read 2026-10-31) - "Euler or up/down numbers: e.g.f. sec(x) + tan(x). Also for n >= 2, half the number of alternating permutations on n letters (A001250).", offset 0, data `1, 1, 1, 2, 5, 16, 61, 272, 1385, 7936, ...`.
[^a000182]: https://oeis.org/A000182 (read 2026-10-31) - "Tangent (or "Zag") numbers: e.g.f. tan(x), also (up to signs) e.g.f. tanh(x).", offset 1, data `1, 2, 16, 272, 7936, 353792, 22368256, ...`.
[^a002620]: https://oeis.org/A002620 (read 2026-10-31) - "Quarter-squares: a(n) = floor(n/2)*ceiling(n/2). Equivalently, a(n) = floor(n^2/4).", offset 0, data `0, 0, 1, 2, 4, 6, 9, 12, 16, 20, ...`.
[^exec1]: Verified by execution (Python 3.11, 2026-10-31): `bin/python/orbital_castles.py` item [1], run log `bin/python/orbital_castles-run.log`. Every castle with `h ≤ 4`, `w ≤ 10` and `h = 5`, `w ≤ 8`: the orbital castles of order `N` number `C(h − 1, N − 1) N!` when `w ≥ 2N`, and each comes from exactly one period.
[^exec2]: Verified by execution (Python 3.11, 2026-10-31): `bin/python/orbital_castles.py` item [2]. The totals for `w ≥ 2h` against A001339 for `h ≤ 9`, and against the arrangements of `{1, …, h}` containing 1 for `h ≤ 6`.
[^exec3]: Verified by execution (Python 3.11, 2026-10-31): `bin/python/orbital_castles.py` item [3]. Every set of 2 to 7 heights from `{1, …, 8}` over all its cyclic orders: the minimum, the maximum, and `2^{N−2}` orders at the minimum; the heights `1, …, N` for `N ≤ 7`; and the 720 cyclic orders of `{1, 2, 3, 5, 6, 7, 8}`.
[^exec4]: Verified by execution (Python 3.11, 2026-10-31): `bin/python/orbital_castles.py` item [4]. Every orbital castle with `h ≤ 5`, `w ≤ 12`, and the castle `(8, 1, 7, 2, 6, 3, 5)` repeated three times (item [3]).
[^exec5]: Verified by execution (Python 3.11, 2026-10-31): `bin/python/orbital_castles.py` item [5], for `h ≤ 5`, `w ≤ 10`.
[^exec6]: Verified by execution (Python 3.11, 2026-10-31): `bin/python/orbital_castles.py` item [6], for `2 ≤ h ≤ 5`, `4 ≤ w ≤ 12`.
[^exec7]: Verified by execution (Python 3.11, 2026-10-31): `bin/python/orbital_castles.py` item [7]. The table for `h ≤ 6`, `w ≤ 12`, the period `2 lcm(1, …, h)` over two periods from `w = 2h` for `h ≤ 5`, and the shortest period 4 at `h = 2` and `3`.
[^exec8]: Verified by execution (Python 3.11, 2026-10-31): `bin/python/orbital_castles.py` item [8], every orbital castle with `h ≤ 5`, `w ≤ 10`.
[^exec9]: Verified by execution (Python 3.11, 2026-10-31): `bin/python/orbital_castles.py` item [9]. The alternating cyclic orders of 2, 4, 6 and 8 heights against A000182; the sign-alternating and alternating counts for `h ≤ 5`, `w ≤ 10`, and the alternating castles of orders 2 and 4 at `w = 9`, `h = 4`; and the periods of largest rise over every set of 2, 4 or 6 heights from `{1, …, 8}`.
[^exec10]: Verified by execution (Python 3.11, 2026-10-31): `bin/python/orbital_castles.py` item [10]. The sum against A000522 for `h ≤ 8`, and the rotation classes of the periods at `w = 2h` for `h ≤ 6`.
