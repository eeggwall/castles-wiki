---
title: Euler castles
category: Concepts
summary: An Euler castle is a castle whose column heights fall by 0 or 1 at each step and end at height 1, such as (3, 3, 2, 1, 1). Its rows are a partition of its area into distinct parts and its block count is the number of parts, so the Euler castles of area n number A000009(n), and Euler's pentagonal number theorem says that the even-block minus the odd-block Euler castles of area n is (−1)^k at n = k(3k ± 1)/2 and 0 at every other area. Franklin's proof of the theorem is a castle move that trades the summit row for the diagonal of the slope at the right end; it keeps the area and the semi-perimeter, changes the block count by one, and leaves unmatched only the pentagonal castles (k^k, k − 1, …, 1) and (k^{k+1}, k − 1, …, 1). Euler castles of width w and height h number C(w − 1, h − 1), and by semi-perimeter s they number F_{s−1}; turned on their side they are the staircase castles.
tags: [concept, castle, euler-castle, partitions, distinct-parts, pentagonal-number-theorem, franklin-involution, convex-castle, staircase, block-count, parity, semi-perimeter, fibonacci, verification]
sources: [project-euler-502-brute-force]
created: 2026-10-28
updated: 2026-10-28
---

# Euler castles

## Definition

A castle of width `w` and height `h` is a skyline `(c_1, …, c_w)` with `1 ≤ c_i ≤ h` and some `c_i = h` ([[castle-polyomino](pages/castle-polyomino.md)]). An **Euler castle** is a castle whose heights fall by 0 or 1 at each step and end at height 1:

```
c_i − c_{i+1}  ∈  {0, 1}   for 1 ≤ i < w,        c_w = 1.
```

So `c_1 = h`, and every height from `h` down to 1 occurs. The name is for Euler's pentagonal number theorem, which the Euler castles turn into a statement about the Project Euler 502 parity (section *The parity*).

*Examples.* `(3, 3, 2, 1, 1)` is an Euler castle of width 5, height 3 and area 10. The flat castle `(1, …, 1)` and the staircase `(k, k − 1, …, 1)` are Euler castles; `(3, 1, 1)` is not, since it falls by 2. The eight Euler castles of width 4 are

| `h` | Euler castles of width 4 |
|---|---|
| 1 | `(1, 1, 1, 1)` |
| 2 | `(2, 1, 1, 1)`, `(2, 2, 1, 1)`, `(2, 2, 2, 1)` |
| 3 | `(3, 2, 1, 1)`, `(3, 2, 2, 1)`, `(3, 3, 2, 1)` |
| 4 | `(4, 3, 2, 1)` |

**The rows are distinct parts.** Row `r` of a castle holds the columns of height at least `r`. An Euler castle never rises, so row `r` is the run of columns `1, …, λ_r`, with `λ_r` the number of columns of height at least `r`. The difference `λ_r − λ_{r+1}` is the number of columns of height exactly `r`, at least 1 because every height from 1 to `h` occurs. So the row lengths

```
w  =  λ_1  >  λ_2  >  …  >  λ_h  ≥  1
```

are distinct, and they add up to the area. Conversely, a partition `λ_1 > … > λ_h` into distinct parts is the list of row lengths of exactly one Euler castle: column `j` has height `#{r : λ_r ≥ j}`, neighboring columns `j` and `j + 1` differ by the number of parts equal to `j`, which is 0 or 1, and the last column, `j = λ_1`, has height 1. The castle `(3, 3, 2, 1, 1)` has rows of lengths 5, 3 and 2, and `10 = 5 + 3 + 2`.[^exec1]

**Blocks.** A block is a maximal horizontal run of columns at one level.[^bf] Each row of an Euler castle is one run starting at column 1, so an Euler castle has one block per row:

```
blocks  =  h  =  the number of parts of its row partition.
```

Euler castles are convex castles, the castles of height `h` with exactly `h` blocks ([[convex-castle](pages/convex-castle.md)]).

**Turned on its side.** Reading the rows of an Euler castle of width `w` and height `h` as columns, `(λ_1, …, λ_h)`, gives a skyline of width `h` and height `w` whose column heights strictly decrease: a staircase castle, one of the base types of [[castle-classification-shape](pages/castle-classification-shape.md)]. Every staircase castle arises once, so turning the castles on their side maps the Euler castles of width `w` and height `h` onto the staircase castles of width `h` and height `w`, and keeps the area.[^exec6] The two families count the same partitions; they differ in what the block count reads off, the number of parts for the Euler castle and the largest part for the staircase castle.

## Notation used on this page

| symbol | meaning |
|---|---|
| `λ_r` | the length of row `r` of an Euler castle, so `λ_1 = w` and `λ_h` is the length of the top row |
| `A_Euler(w, h)`, `A^e_Euler`, `A^o_Euler`, `S_Euler` | the Euler castles of width `w` and height `h`; the even-block and odd-block ones; `A^e_Euler − A^o_Euler` |
| `A_Euler(n)`, `A^e_Euler(n)`, `A^o_Euler(n)`, `S_Euler(n)` | the same counts over the Euler castles of area `n` |
| `pd(n)` | partitions of `n` into distinct parts, `A000009` ([[aocp-generating-partitions](pages/aocp-generating-partitions.md)]) |
| `F_n` | the Fibonacci numbers, `F_1 = F_2 = 1` |
| `a`, `b` | the summit length and the slope length of an Euler castle (section *Franklin's move*), Chapman's `a_λ` and `b_λ` |
| `s` | the semi-perimeter `w + blocks` ([[castle-perimeter](pages/castle-perimeter.md)]), which is `w + h` on an Euler castle |

## Counts

**By width and height.** An Euler castle is fixed by how many columns it has of each height `1, …, h`, each number at least 1, adding up to `w`: a composition of `w` into `h` parts. So

```
A_Euler(w, h)  =  C(w − 1, h − 1),        Σ_{w,h ≥ 1} A_Euler(w, h) x^w y^h  =  xy / (1 − x − xy),
```

and there are `2^{w−1}` Euler castles of width `w`, all eight of width 4 being listed above.[^exec2] Every Euler castle of height `h` has `h` blocks, so `A^e_Euler(w, h) = C(w − 1, h − 1)` for even `h` and 0 for odd `h`.

**By area.** By the row reading, the Euler castles of area `n` are the partitions of `n` into distinct parts, `A_Euler(n) = pd(n) = A000009(n)`, with generating function `Π_{k ≥ 1} (1 + q^k) − 1`:[^a000009][^exec2]

| `n` | Euler castles of area `n` (blocks) | `A_Euler(n)` | `S_Euler(n)` |
|---|---|---|---|
| 1 | `(1)` (1) | 1 | `−1` |
| 2 | `(1, 1)` (1) | 1 | `−1` |
| 3 | `(1, 1, 1)` (1), `(2, 1)` (2) | 2 | 0 |
| 4 | `(1, 1, 1, 1)` (1), `(2, 1, 1)` (2) | 2 | 0 |
| 5 | `(1, 1, 1, 1, 1)` (1), `(2, 1, 1, 1)` (2), `(2, 2, 1)` (2) | 3 | 1 |
| 6 | `(1, …, 1)` (1), `(2, 1, 1, 1, 1)` (2), `(2, 2, 1, 1)` (2), `(3, 2, 1)` (3) | 4 | 0 |
| 7 | `(1, …, 1)` (1), `(2, 1, 1, 1, 1, 1)` (2), `(2, 2, 1, 1, 1)` (2), `(2, 2, 2, 1)` (2), `(3, 2, 1, 1)` (3) | 5 | 1 |

From `n = 1` the counts are `1, 1, 2, 2, 3, 4, 5, 6, 8, 10, 12, 15, 18, 22, 27, 32`.

**By semi-perimeter.** The semi-perimeter of a castle is `w + blocks` ([[castle-perimeter](pages/castle-perimeter.md)]), which is `w + h` on an Euler castle. Setting `x = y = t` in the cell generating function gives `t²/(1 − t − t²)`, so the Euler castles of semi-perimeter `s` number `F_{s−1}`: `1, 1, 2, 3, 5, 8, 13, …` from `s = 2`.[^exec2]

## The parity: Euler's pentagonal number theorem

Euler's pentagonal number theorem is the expansion

```
Π_{k ≥ 1} (1 − q^k)  =  1 + Σ_{k ≥ 1} (−1)^k ( q^{k(3k−1)/2} + q^{k(3k+1)/2} )  =  1 − q − q² + q⁵ + q⁷ − q¹² − q¹⁵ + q²² + q²⁶ − ⋯.
```

Franklin (1881) attributes the expansion to Euler and reads its coefficient of `q^n` as the number of partitions of `n` into an even number of distinct parts minus the number into an odd number.[^franklin-problem][^franklin-identity] The exponents are the generalized pentagonal numbers `k(3k − 1)/2`, `k = 0, ±1, ±2, …`, which are `0, 1, 2, 5, 7, 12, 15, 22, 26, …` (`A001318`).[^a001318]

An Euler castle of area `n` with `h` blocks is a partition of `n` into `h` distinct parts, so the theorem is a statement about the Project Euler 502 parity of the Euler castles:

```
S_Euler(n)  =  A^e_Euler(n) − A^o_Euler(n)  =  (−1)^k   if n = k(3k − 1)/2 or n = k(3k + 1)/2 with k ≥ 1,
                                              0        otherwise.
```

These are the coefficients of `A010815` from `n = 1`.[^a010815] The even-block Euler castles of area `n` number `A067661(n)`, `0, 0, 1, 1, 2, 2, 3, 3, 4, 5, 6, 7, 9, 11, 13, 16` from `n = 1`, and the odd-block ones `A067659(n)`, `1, 1, 1, 1, 1, 2, 2, 3, 4, 5, 6, 8, 9, 11, 14, 16`; the two agree at every area outside the pentagonal numbers.[^a0676][^exec3] At `n = 5`, for example, the odd-block castle `(1, 1, 1, 1, 1)` is outnumbered by the two even-block castles `(2, 1, 1, 1)` and `(2, 2, 1)`, and 5 is the pentagonal number with `k = 2`.

## Franklin's move

Franklin proves the theorem by pairing the partitions of `n` into distinct parts so that the two partitions of a pair differ by one in their number of parts, which leaves exactly one partition unpaired at each pentagonal `n` and none elsewhere.[^franklin-rule] On an Euler castle the pairing is a move of cells from the top of the castle to its right end, or back.

**Summit and slope.** The **summit** of an Euler castle of height `h` is its run of `a ≥ 1` columns of height `h`: the top row, of length `a = λ_h`, the smallest part. Its **slope** is the longest final run of columns with heights `b, b − 1, …, 1`, one column of each height. The tops of the slope columns are the last cells of the bottom `b` rows, whose lengths `w, w − 1, …, w − b + 1` are the longest run of consecutive parts at the large end of the partition. In Franklin's notation, written on the parts in increasing order, `a` is his `r` ("le premier nombre") and `b` his `n` ("le nombre exact de nombres consécutifs à sa fin").[^franklin-rule] Chapman writes them `a_λ` and `b_λ`.[^chapman-def]

*Examples.* `(3, 3, 2, 1, 1)` has summit `a = 2` and slope `b = 1`: its last column has height 1, and the column before it also has height 1. `(5, 5, 4, 3, 2, 2, 1)` has `a = 2` and `b = 2`: its last two columns have heights 2 and 1, and the column before them has height 2, not 3.

**The move.**

1. If `a ≤ b`, take off the summit row and lay its `a` cells along the slope: the summit columns drop to `h − 1`, the last `a − 1` columns rise by one, and a new column of height 1 is added at the right. The width grows by one and the height drops by one.
2. If `a > b`, take the top cell off each slope column and lay the `b` cells on the summit as a new top row: the last `b` columns drop by one, so the last column, of height 1, disappears, and the first `b` columns rise to `h + 1`. The width drops by one and the height grows by one.

Franklin's first example is the partition `2 + 3 + 4 + 6 + 7`, which he sends to `3 + 4 + 7 + 8`.[^franklin-examples] As castles, `(5, 5, 4, 3, 2, 2, 1)` has `a = b = 2`, so case 1 applies, and the two summit cells `S` become the two new cells `+`:

```
(5, 5, 4, 3, 2, 2, 1)              (4, 4, 4, 3, 2, 2, 2, 1)

S S . . . . .
# # # . . . .                      # # # . . . . .
# # # # . . .                      # # # # . . . .
# # # # # # .                      # # # # # # + .
# # # # # # #                      # # # # # # # +
```

The castle on the right has summit `a = 3` and slope `b = 2`, so case 2 applies and returns the castle on the left. Franklin's other examples run the same way: `3 + 5 + 8 + 9` and `2 + 3 + 5 + 7 + 8`, `3 + 4 + 5 + 6` and `5 + 6 + 7`, `6 + 7 + 8 + 9` and `4 + 5 + 6 + 7 + 8`.[^franklin-examples][^exec4]

**The pentagonal castles.** Both cases give an Euler castle of the same area unless the slope reaches the summit, `b = h`, so that the castle is `(h, …, h, h − 1, …, 2, 1)` with `a` columns of height `h`, and `a` is `h` or `h + 1`. For `a = h`, case 1 would leave a rise from `h − 1` to `h` just after the lowered summit; for `a = h + 1`, case 2 would leave a fall by 2 from `h + 1` to `h − 1`. These are Franklin's exceptions, "si tous les nombres sont consécutifs et que `r = n` ou `r = n + 1`".[^franklin-rule] With `h = k` they are the **pentagonal castles**

```
(k, …, k, k − 1, …, 2, 1)   with k columns of height k:      width 2k − 1, area k² + k(k − 1)/2 = k(3k − 1)/2,
(k, …, k, k − 1, …, 2, 1)   with k + 1 columns of height k:  width 2k,     area k(k + 1) + k(k − 1)/2 = k(3k + 1)/2,
```

a `k × k` or `(k + 1) × k` box with a staircase of `k − 1` columns against its right side. Franklin's last examples, `4 + 5 + 6 + 7` and `5 + 6 + 7 + 8`, are the pentagonal castles `(4, 4, 4, 4, 3, 2, 1)` of area 22 and `(4, 4, 4, 4, 4, 3, 2, 1)` of area 26.[^franklin-examples]

On every other Euler castle the move is its own inverse, and it changes the block count, which is the height, by one. So the Euler castles of each area `n` pair off into an even-block and an odd-block castle, except the one pentagonal castle at a pentagonal area, which has `k` blocks; this is the formula for `S_Euler(n)`.[^exec4]

**What the move keeps.** Case 1 takes `(w, h)` to `(w + 1, h − 1)` and case 2 to `(w − 1, h + 1)`, so the move keeps `w + h`, the semi-perimeter, as well as the area: it keeps the perimeter of the castle and changes its block count by one. For partitions this is Chapman's observation that Franklin's map keeps the largest part plus the number of parts, from which Chapman obtains[^chapman-mn][^chapman-7]

```
Σ (−1)^{blocks} t^{s} q^{area}  =  Σ_{k ≥ 1} (−1)^k ( t^{3k−1} q^{k(3k−1)/2}  +  t^{3k} q^{k(3k+1)/2} ),
```

the sum running over all Euler castles. So at each area and semi-perimeter the even-block and odd-block Euler castles are equinumerous, except at the pentagonal castles: of semi-perimeter `3k − 1` at area `k(3k − 1)/2`, and `3k` at area `k(3k + 1)/2`.[^exec5] At `q = 1` the signed count by semi-perimeter is `−t²/(1 − t + t²)`, the cell generating function at `x = t`, `y = −t`, which repeats `−1, −1, 0, 1, 1, 0` with period 6 from `s = 2`, the negated `A010892(s − 2)`.[^exec5]

## Related Concepts

- [[convex-castle](pages/convex-castle.md)] - the castles of height `h` with exactly `h` blocks, which contain the Euler castles.
- [[castle-classification-shape](pages/castle-classification-shape.md)] - the catalogue entry for the Euler castles, and the staircase castles, which are the Euler castles turned on their side.
- [[castle-perimeter](pages/castle-perimeter.md)] - the semi-perimeter `w + blocks`, which Franklin's move keeps.
- [[aocp-generating-partitions](pages/aocp-generating-partitions.md)] - Knuth's section on partitions, with partitions into distinct parts and Euler's products.
- [[hoodoo-monadnock-castles](pages/hoodoo-monadnock-castles.md)] - two more castle types built from partitions into distinct parts, on the steps of each side.
- [[castle-sign](pages/castle-sign.md)] - the sign `(−1)^blocks`, which on an Euler castle is the sign of the pentagonal number theorem.
- [[castle-notation](pages/castle-notation.md)] - the symbols of this page.

## Footnotes

[^bf]: [[project-euler-502-brute-force](pages/project-euler-502-brute-force.md)] §"Column-height encoding" L20-27 - "A block is a maximal horizontal run of columns at a given level", and "two runs at the same level are always separated by a strictly lower column."
[^franklin-problem]: F. Franklin, "Sur le développement du produit infini `(1 − x)(1 − x²)(1 − x³)(1 − x⁴)…`", *Comptes rendus hebdomadaires des séances de l'Académie des sciences* 92 (1881), 448-450, transcribed at https://fr.wikisource.org/wiki/Page:Comptes_rendus_hebdomadaires_des_s%C3%A9ances_de_l%E2%80%99Acad%C3%A9mie_des_sciences,_tome_092,_1881.djvu/447 (read 2026-10-28), p.448 - "Euler a obtenu ce développement au moyen d'un arrangement spécial des opérations de multiplication. Je vais obtenir le terme général comme solution d'un problème de partitions." and "Le coefficient de `x^w` dans le développement est évidemment l'excès du nombre de manières dont on peut décomposer `w` en un nombre *pair* de parties entières et différentes sur le nombre de manières dont on peut le décomposer en un nombre *impair* de telles parties".
[^franklin-identity]: Franklin 1881, https://fr.wikisource.org/wiki/Page:Comptes_rendus_hebdomadaires_des_s%C3%A9ances_de_l%E2%80%99Acad%C3%A9mie_des_sciences,_tome_092,_1881.djvu/448 (read 2026-10-28), p.449 - "`(1−x)(1−x²)(1−x³)(1−x⁴)… = Σ(−1)^n x^{n(3n±1)/2} = 1−x−x²+x⁵+x⁷−x¹²−x¹⁵+x²²+x²⁶+…`".
[^franklin-rule]: Franklin 1881, https://fr.wikisource.org/wiki/Page:Comptes_rendus_hebdomadaires_des_s%C3%A9ances_de_l%E2%80%99Acad%C3%A9mie_des_sciences,_tome_092,_1881.djvu/449 (read 2026-10-28), p.450 - "Soient `r` le premier nombre de la partition donnée, `n` le nombre exact de nombres consécutifs à sa fin. Si `r ≦ n`, on obtient la partition conjuguée en effaçant `r` et augmentant de l'unité chacun des `r` derniers nombres ; si `r > n`, on l'obtient en diminuant de l'unité chacun des `n` derniers nombres et mettant `n` devant le premier nombre. Et l'on s'assure facilement que, par la même règle, la première partition est la conjuguée de la seconde. Mais, si tous les nombres sont consécutifs et que `r = n` ou `r = n+1`, on ne peut pas former la conjuguée, et c'est *seulement* dans ces cas qu'on ne peut pas la former." Franklin writes the parts "en ordre ascendant" (p.449).
[^franklin-examples]: Franklin 1881, https://fr.wikisource.org/wiki/Page:Comptes_rendus_hebdomadaires_des_s%C3%A9ances_de_l%E2%80%99Acad%C3%A9mie_des_sciences,_tome_092,_1881.djvu/449 (read 2026-10-28), p.450 - "Ainsi les conjuguées de `23467, 3589, 3456, 6789` sont `3478, 23578, 567, 45678` ; mais aux partitions `4567, 5678` on ne peut pas former de conjuguées."
[^chapman-def]: R. Chapman, "Franklin's argument proves an identity of Zagier", https://arxiv.org/pdf/math/0009036 (read 2026-10-28) p.2 §2 - "Denote its smallest part by `a_λ`. If the parts of `λ` are `λ_1 > λ_2 > λ_3 > ⋯` let `b = b_λ` denote the largest `b` such that `λ_b = λ_1 + 1 − b`".
[^chapman-mn]: https://arxiv.org/pdf/math/0009036 (read 2026-10-28) p.3 §2 - "In each case `m_λ′ + n_λ′ = m_λ + n_λ`.", after the two cases in which Franklin's map lowers the number of parts `n_λ` by one and raises the largest part `m_λ` by one, or the reverse (`n_λ` and `m_λ` defined on p.2).
[^chapman-7]: https://arxiv.org/pdf/math/0009036 (read 2026-10-28) p.4 §3, Equation (7) - "`Σ_{λ∈D} (−1)^{n_λ} x^{m_λ+n_λ} q^{N_λ} = 1 + Σ_{r=1}^∞ (−1)^r [x^{3r−1} q^{r(3r−1)/2} + x^{3r} q^{r(3r+1)/2}]`", with `D` the partitions into distinct parts, the empty one included, and `N_λ` the sum of the parts.
[^a000009]: https://oeis.org/A000009 (read 2026-10-28) - "Expansion of Product_{m >= 1} (1 + x^m); number of partitions of n into distinct parts; number of partitions of n into odd parts", offset 0, data `1, 1, 1, 2, 2, 3, 4, 5, 6, 8, 10, 12, 15, 18, 22, 27, 32`.
[^a001318]: https://oeis.org/A001318 (read 2026-10-28) - "Generalized pentagonal numbers: m*(3*m - 1)/2, m = 0, +-1, +-2, +-3, ....", data `0, 1, 2, 5, 7, 12, 15, 22, 26, 35, 40`.
[^a010815]: https://oeis.org/A010815 (read 2026-10-28) - "From Euler's Pentagonal Theorem: coefficient of q^n in Product_{m>=1} (1 - q^m).", offset 0, data `1, -1, -1, 0, 0, 1, 0, 1, 0, 0, 0, 0, -1, 0, 0, -1`.
[^a0676]: https://oeis.org/A067661, https://oeis.org/A067659 (read 2026-10-28) - "Number of partitions of n into distinct parts such that number of parts is even.", offset 0, data `1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 5, 6, 7, 9, 11, 13, 16`; "Number of partitions of n into distinct parts such that number of parts is odd.", offset 0, data `0, 1, 1, 1, 1, 1, 2, 2, 3, 4, 5, 6, 8, 9, 11, 14, 16`.
[^exec1]: Verified by execution (Python 3.11, 2026-10-28): `bin/python/euler_castles.py` item [1], run log `bin/python/euler_castles-run.log`. Every Euler castle with `w ≤ 8`, `h ≤ 5` has distinct row lengths, `h` blocks and bottom row `w`, and the row lengths are a one-to-one map onto the partitions into distinct parts of every area `n ≤ 40`.
[^exec2]: Verified by execution (Python 3.11, 2026-10-28): `bin/python/euler_castles.py` item [2], run log `bin/python/euler_castles-run.log`. `A_Euler(w, h) = C(w − 1, h − 1)` by filtering all `h^w` skylines with `w ≤ 8`, `h ≤ 5`; the counts by area against `Π (1 + q^k)` for `n ≤ 40` and against the `A000009` data; the counts by semi-perimeter, `F_{s−1}`, against the `A000045` data.
[^exec3]: Verified by execution (Python 3.11, 2026-10-28): `bin/python/euler_castles.py` item [3], run log `bin/python/euler_castles-run.log`. `S_Euler(n)` against the pentagonal formula and `Π (1 − q^k)` for `n ≤ 40`, and against the `A010815` data; the even-block and odd-block counts against the `A067661` and `A067659` data for `n ≤ 26`.
[^exec4]: Verified by execution (Python 3.11, 2026-10-28): `bin/python/euler_castles.py` item [4], run log `bin/python/euler_castles-run.log`. For every Euler castle of area `n ≤ 40`: the move gives an Euler castle of the same area, applied twice it returns the castle, it changes the height by one and keeps `w + blocks`, and on the row lengths it is Franklin's rule as he states it; it fails exactly once at each pentagonal area, on the pentagonal castle. Franklin's six examples reproduced.
[^exec5]: Verified by execution (Python 3.11, 2026-10-28): `bin/python/euler_castles.py` item [5], run log `bin/python/euler_castles-run.log`. The signed count by area and semi-perimeter for `n ≤ 40`; the signed count by semi-perimeter against `−A010892(s − 2)` for `s ≤ 19`.
[^exec6]: Verified by execution (Python 3.11, 2026-10-28): `bin/python/euler_castles.py` item [6], run log `bin/python/euler_castles-run.log`, for every castle with `w ≤ 8`, `h ≤ 5`.
