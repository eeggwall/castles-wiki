---
title: Orbital castles
category: Concepts
summary: An orbital castle of order N repeats a period of N distinct heights from its first column, at width at least 2N, so every height appears at least twice, such as (1, 2, 3, 1, 2, 3). Each height has one successor, and the castle is the orbit of its first column. The orbital castles of order N and height h number C(h − 1, N − 1) N! at every width w ≥ 2N, and all orders together number A001339(h − 1) = 1, 3, 11, 49, 261, … from w = 2h on, the arrangements of {1, …, h} containing h. Each period adds the cyclic rise rise(c) to the block count, which lies between max − min and the sum of the top half of the period's heights minus the bottom half (N − 1 and ⌊N²/4⌋ on 1, …, N), so the block parity flips every period exactly when rise(c) is odd. The box is the orbital castle of order 1 and the crenellated castles, the battlement among them, are those of order 2; the battlements are the only orbital tree castles, and the orbital castles that begin and end at height 1 are powers of one prime castle.
tags: [concept, castle, orbital-castle, periodic-castle, cyclic-permutation, arrangement, a001339, rise, block-count, parity, battlement, tree-castle, prime-castle, verification]
sources: [project-euler-502-brute-force]
created: 2026-10-31
updated: 2026-10-31
---

# Orbital castles

## Definition

A castle of width `w` and height `h` is a skyline `(c_1, …, c_w)` with `1 ≤ c_i ≤ h` and some `c_i = h` ([[castle-polyomino](pages/castle-polyomino.md)]). An **orbital castle of order `N`** repeats a period of `N` distinct heights from its first column, with width at least `2N`:

```
c_{i+N}  =  c_i   for 1 ≤ i ≤ w − N,        c_1, …, c_N distinct,        w  ≥  2N.
```

Each height in the period is followed by the next one, and the last by the first, so every height has one successor and the castle is the orbit of its first column under that cycle. The order `N` is the number of distinct heights. The width bound `w ≥ 2N` makes every height appear at least twice, so the castle shows its whole cycle at least once; the last period may stop part of the way, as in `(1, 2, 3, 1, 2, 3, 1)`. The period contains `h`, since some column has height `h`.

*Examples.*

- **Order 1:** the box `(h, h, …, h)`.
- **Order 2:** the crenellated castles `(a, h, a, h, …)` and `(h, a, h, a, …)` with `a < h`, among them the battlements `(1, h, 1, h, …)` and `(h, 1, h, 1, …)`.
- **Order 3:** `(1, 2, 3, 1, 2, 3)`, and `(1, 2, 3, 1, 2, 3, 1)`, which ends partway through a period.
- **Order 7:** `(8, 1, 7, 2, 6, 3, 5)` repeated three times, a castle of width 21 and height 8.

*Non-examples.* `(1, 2, 1, 3)` is not orbital, since height 1 is followed once by 2 and once by 3. `(1, 2, 3, 1, 2)` repeats a period of three heights but has width 5 < 6, so height 3 appears once. `(2, 1, 3, 3, 3)` has one successor for each height, but its first column never comes back: it reaches a cycle only after a lead-in.

## Notation used on this page

| symbol | meaning |
|---|---|
| `N` | the order of an orbital castle, the number of distinct heights in its period |
| `A_orbital(w, h)`, `A_orbital(w, h; N)` | the orbital castles of width `w` and height `h`, and those of order `N` |
| `A^e_orbital(w, h)` | the even-block ones |
| `rise(c)` | the cyclic rise of the period `(c_1, …, c_N)`, `Σ max(0, c_{i+1} − c_i)` around the cycle, the step from `c_N` back to `c_1` included ([[tone-castle-catalog](pages/tone-castle-catalog.md)]) |
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

The OEIS reads A001339 as "Number of arrangements of {1, 2, ..., n, n + 1} containing the element 1".[^a001339] That is the period: an orbital castle of height `h` and width at least `2h` is an arrangement of some of the heights `1, …, h` that contains `h`, written out to the width, and reflecting the heights, `c ↦ h + 1 − c`, turns it into an arrangement containing 1 with `n = h − 1`.[^exec2]

## The rise per period

The **cyclic rise** `rise(c)` of the period counts the rises around the cycle once. A period's rises and falls balance, so `rise(c)` is half the cyclic total variation `Σ |c_{i+1} − c_i|`, and it is bounded by the heights the period uses. With `N` heights `s_1 < … < s_N`:

```
s_N − s_1   ≤   rise(c)   ≤   (s_N + s_{N−1} + ⋯ + s_{N−⌊N/2⌋+1})  −  (s_1 + s_2 + ⋯ + s_{⌊N/2⌋}).
```

*Proof.* The cycle climbs from `s_1` to `s_N` and comes back, so it rises by at least `s_N − s_1`, with equality exactly when it climbs once and falls once; each of the `N − 2` other heights then lies on the way up or the way down, so `2^{N−2}` cyclic orders reach the minimum. For the upper bound, write the total variation as `Σ (larger − smaller)` over the `N` steps of the cycle. Each height is an end of two steps, so it enters the sum with coefficient `+2`, `0` or `−2`, and the coefficients add up to 0; the sum is largest when the top `⌊N/2⌋` heights get `+2` and the bottom `⌊N/2⌋` get `−2`, which an alternating high-low order achieves. ∎

On the heights `1, …, N` the bounds are `N − 1` and `⌊N/2⌋ ⌈N/2⌉ = ⌊N²/4⌋`, the quarter-squares `1, 2, 4, 6, 9, 12` for `N = 2, …, 7` (A002620).[^a002620] The period `(8, 1, 7, 2, 6, 3, 5)` alternates high and low on the heights `{1, 2, 3, 5, 6, 7, 8}` and has `rise = 6 + 4 + 2 + 3 = 15 = (8 + 7 + 6) − (1 + 2 + 3)`, the largest rise of the 720 cyclic orders of those heights; 72 of them reach it.[^exec3]

## Blocks and parity

The block count of a castle is `c_1 + Σ max(0, c_{i+1} − c_i)`, its first column plus its rises.[^bf] A castle of width `w` takes `w − 1` steps; with `w − 1 = qN + t` and `0 ≤ t < N`, the steps go `q` times around the cycle and then `t` steps more, so

```
blocks  =  c_1  +  q · rise(c)  +  (the rises of the first t steps of the period).
```

For `r` whole periods that start at height `h`, this is the tone-burst count `blocks = c_w + r · rise(c)` of [[tone-castle-catalog](pages/tone-castle-catalog.md)]; the castle `(8, 1, 7, 2, 6, 3, 5)` repeated three times has `5 + 3 · 15 = 50` blocks.[^exec4] Each added period adds `rise(c)` blocks, so **the block parity flips with every period exactly when `rise(c)` is odd**, and it never changes when `rise(c)` is even.

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

**The box, the crenellated castles and the battlement.** The box `(h, …, h)` is the orbital castle of order 1. The orbital castles of order 2 are the crenellated castles `(a, h, a, h, …)` and `(h, a, h, a, …)` with `a < h` ([[castle-classification-shape](pages/castle-classification-shape.md)], Axis 7), `2(h − 1)` of them at each width `w ≥ 4`, and the battlements `(1, h, 1, h, …)` and `(h, 1, h, 1, …)` are the two with `a = 1` ([[castle-notation](pages/castle-notation.md)], the battlement row).

**Tree castles.** A tree castle has no two neighboring columns both of height at least 2 ([[castle-graph](pages/castle-graph.md)]). The orbital tree castles are exactly the two battlements, at every width `w ≥ 4` and height `h ≥ 2`, and `(1, …, 1)` at height 1. A period of order `N ≥ 3` holds at most one height 1, so its other `N − 1` heights sit next to each other around the cycle, and the castle shows that pair; at order 2 the heights `{a, h}` give a tree castle only for `a = 1`. In the other direction most tree castles are not orbital: `(1, 2, 1, 3, 1)` is a tree castle, but height 1 is followed by both 2 and 3.[^exec5]

**Prime castles.** The castles that begin and end with a height-1 column form a free monoid under gluing at a shared height-1 column, and its primes are the castles `(1, X, 1)` with no height-1 column in `X` ([[prime-castles](pages/prime-castles.md)]). An orbital castle whose period has no height 1 has no height-1 column, so it is not in the monoid. An orbital castle begins and ends at height 1 exactly when `c_1 = 1` and `N` divides `w − 1`; it is then `k = (w − 1)/N` copies of the prime castle `(1, c_2, …, c_N, 1)` glued together, and `k ≥ 2`, so it is never prime itself, apart from `(1, 1)`. Of order `N ≥ 2` there are `C(h − 2, N − 2) · (N − 1)!` of them at each such width, one for each prime castle `(1, c_2, …, c_N, 1)` whose inner heights are distinct and include `h`. The block count minus one adds up under gluing, and the prime castle has `rise(c) + 1` blocks, so

```
blocks − 1  =  k · rise(c),        χ  =  (−1)^{k · rise(c)}  =  χ(1, c_2, …, c_N, 1)^k,
```

the per-period parity rule as the sign character of [[signed-prime-castles](pages/signed-prime-castles.md)] on a power of one prime.[^exec6]

**Periodic castles.** A periodic castle repeats a period that may use a height more than once, as the tone castles of [[tone-castle-catalog](pages/tone-castle-catalog.md)] do; the orbital castles are the periodic castles whose period uses each of its heights once, written out to at least two periods.

## Related Concepts

- [[tone-castle-catalog](pages/tone-castle-catalog.md)] - the cyclic rise `rise(c)` and the block count `c_w + r · rise(c)` of a tone burst.
- [[prime-castles](pages/prime-castles.md)], [[signed-prime-castles](pages/signed-prime-castles.md)] - the gluing monoid, its primes, and the sign character.
- [[castle-graph](pages/castle-graph.md)] - the tree castles, which meet the orbital castles in the battlements.
- [[castle-classification-shape](pages/castle-classification-shape.md)] - the shape types, among them the orbital castles.
- [[castle-notation](pages/castle-notation.md)] - `A_X(w, h)`, `rise(c)`, the battlement, and `N` as the order of an orbital castle.

## Footnotes

[^bf]: [[project-euler-502-brute-force](pages/project-euler-502-brute-force.md)] §"Column-height encoding" L20-L24 - "A block is a maximal horizontal run of columns at a given level, so", "= c_1 + \sum_{i=2}^{w} \max(0, c_i - c_{i-1})".
[^a001339]: https://oeis.org/A001339 (read 2026-10-31) - "a(n) = Sum_{k=0..n} (k+1)! binomial(n,k).", data `1, 3, 11, 49, 261, 1631, 11743, 95901, 876809, ...`, and "Number of arrangements of {1, 2, ..., n, n + 1} containing the element 1. - _Emeric Deutsch_, Oct 11 2001".
[^a121757]: https://oeis.org/A121757 (read 2026-10-31) - "Triangle read by rows: multiply Pascal's triangle by 1,2,6,24,120,720,... = A000142.", offset 0, data `1, 1, 2, 1, 4, 6, 1, 6, 18, 24, ...`, and "Row sums are 1,3,11,49,261,1631,... = A001339".
[^a002620]: https://oeis.org/A002620 (read 2026-10-31) - "Quarter-squares: a(n) = floor(n/2)*ceiling(n/2). Equivalently, a(n) = floor(n^2/4).", offset 0, data `0, 0, 1, 2, 4, 6, 9, 12, 16, 20, ...`.
[^exec1]: Verified by execution (Python 3.11, 2026-10-31): `bin/python/orbital_castles.py` item [1], run log `bin/python/orbital_castles-run.log`. Every castle with `h ≤ 4`, `w ≤ 10` and `h = 5`, `w ≤ 8`: the orbital castles of order `N` number `C(h − 1, N − 1) N!` when `w ≥ 2N`, and each comes from exactly one period.
[^exec2]: Verified by execution (Python 3.11, 2026-10-31): `bin/python/orbital_castles.py` item [2]. The totals for `w ≥ 2h` against A001339 for `h ≤ 9`, and against the arrangements of `{1, …, h}` containing 1 for `h ≤ 6`.
[^exec3]: Verified by execution (Python 3.11, 2026-10-31): `bin/python/orbital_castles.py` item [3]. Every set of 2 to 7 heights from `{1, …, 8}` over all its cyclic orders: the minimum, the maximum, and `2^{N−2}` orders at the minimum; the heights `1, …, N` for `N ≤ 7`; and the 720 cyclic orders of `{1, 2, 3, 5, 6, 7, 8}`.
[^exec4]: Verified by execution (Python 3.11, 2026-10-31): `bin/python/orbital_castles.py` item [4]. Every orbital castle with `h ≤ 5`, `w ≤ 12`, and the castle `(8, 1, 7, 2, 6, 3, 5)` repeated three times (item [3]).
[^exec5]: Verified by execution (Python 3.11, 2026-10-31): `bin/python/orbital_castles.py` item [5], for `h ≤ 5`, `w ≤ 10`.
[^exec6]: Verified by execution (Python 3.11, 2026-10-31): `bin/python/orbital_castles.py` item [6], for `2 ≤ h ≤ 5`, `4 ≤ w ≤ 12`.
[^exec7]: Verified by execution (Python 3.11, 2026-10-31): `bin/python/orbital_castles.py` item [7]. The table for `h ≤ 6`, `w ≤ 12`, and the period `2 lcm(1, …, h)` over two periods from `w = 2h` for `h ≤ 5`.
