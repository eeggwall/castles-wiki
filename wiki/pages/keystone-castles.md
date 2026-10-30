---
title: Keystone castles
category: Concepts
summary: A keystone castle is a castle on the triangular tiling {3,6} with no overhang - a full bottom row of w up triangles and the w − 1 down triangles between them, every higher up triangle resting on a down triangle, and every down triangle held, like a keystone, by the two up triangles beside it in its row. Its outline is a path U 𝒫 D with 𝒫 a large Schröder path of semilength w − 1, the height of the castle the height of the path, its blocks the up-steps and its cells the area, so the keystone castles of width w number the large Schröder number r_(w−1) (A006318), by blocks A088617, by width plus blocks the Motzkin numbers, at height 2 F_(2w−1) − 1, and by cells A393774(n − 1), the continued fraction 1/(1 − q² − q³/(1 − q⁴ − ⋯)) of Bala's stacks of large Schröder type, growing at 1.46275. Every triangle stack of A224704 is a row of keystone castles side by side. Read along the 60-degree rows a keystone castle is a composition with s_1 = 1 and 2 ≤ s_(i+1) ≤ s_i + 1 + (s_i mod 2), and its up triangles form a brick-wall castle. Exactly half the keystone castles of each width w ≥ 2 have an even block count, and the signed count at height at most h has generating function −x(1 − (−x)^h)/(1 − (−x)^(h+1)), periodic in the width. By width they grow at (1 + √2)², silver squared, and at height 2 they grow by cells at a Salem number of degree 6, 1.40127. The counts by height are a new triangle.
tags: [concept, castle, keystone-castle, triangular-tiling, triangle-stack, schroder-path, motzkin, parity, continued-fraction, composition, brick-wall-castle]
sources: [bala-2019-area-beneath-small-schroder-paths, bala-2019-triangle-stacks-large-schroder-type]
created: 2026-10-29
updated: 2026-10-30
---

# Keystone castles

The triangular tiling `{3,6}`, in which every cell is a triangle and six triangles meet at each vertex, falls into rows when one family of its edges is horizontal, and each row alternates up triangles and down triangles. An up triangle rests along its base on the down triangle below it. A down triangle meets the row below only at its lowest vertex, and its two lower sides lie on the up triangles beside it in its row, so "no overhang" asks that both of those be present: the down triangle is held between them as a keystone is held in an arch.

## Definition

A **keystone castle** of width `w` is a set of triangles of the triangular tiling with

- a full bottom row of `w` up triangles and the `w − 1` down triangles between them,
- every up triangle above the bottom row resting on the down triangle below it, and
- every down triangle above the bottom row lying between two up triangles of its row.

These rules are exactly "no overhang": every point of a triangle has triangles of the castle below it down to the bottom row. The **blocks** are the maximal runs of triangles in a row, the **height** `h` is the number of rows, and the **cells** are the triangles. `A_key(w, h)` counts the keystone castles of width `w` and height `h`, `A^e_key` and `A^o_key` its even-block and odd-block parts, and `S_key = A^e_key − A^o_key` its signed count; without `h` they run over all heights.

*All keystone castles of width 3.* Drawn one character per triangle, `▲` up and `▼` down, each row over the one below so that an up triangle sits over the down triangle it rests on, there are six:

```
(a)          (b)          (c)          (d)          (e)          (f)
                                                                   ▲
              ▲              ▲          ▲ ▲          ▲▼▲          ▲▼▲
▲▼▲▼▲        ▲▼▲▼▲        ▲▼▲▼▲        ▲▼▲▼▲        ▲▼▲▼▲        ▲▼▲▼▲
```

with heights 1, 2, 2, 2, 2, 3 and blocks 1, 2, 2, 3, 2, 3.

## The outline is a Schröder path

**Proposition (the outline).** Draw the triangles with side 2 and height 1, and follow the top of a keystone castle from its left corner to its right corner. The outline is a lattice path with up-steps `U = (1, 1)`, down-steps `D = (1, −1)` and flat steps `H = (2, 0)`, and it is `U 𝒫 D` with `𝒫` a large Schröder path of semilength `w − 1`, a path from level 1 back to level 1 that never goes below it. Every such path arises from exactly one keystone castle of width `w`. The height of the castle is the height of its outline, its blocks are the up-steps of the outline, `1 + #U(𝒫)`, and its cells are the area under the outline in unit triangles.

*Proof.* The top of the castle consists of the left and right sides of up triangles, which are up-steps and down-steps, and the top edges of down triangles, which are flat steps of length 2. The outline starts up the left side of the first bottom triangle and ends down the right side of the last, and in between it stays at level 1 or above because the bottom row has all its down triangles, whose tops are at level 1. No overhang makes the castle everything below its outline. Conversely, the triangles below a path `U 𝒫 D` form a keystone castle: an up triangle below the path has the down triangle under it below the path as well, and a down triangle below the path has its top edge below the path, so the apexes of the two up triangles beside it are below the path too. The castle reaches the level of the highest point of the path. A run of row `r` begins where the outline rises from level `r − 1` to `r`, and every such up-step begins a run, so the blocks are the up-steps.

The six castles of width 3 have outlines `U HH D`, `U UDH D`, `U HUD D`, `U UDUD D`, `U UHD D` and `U UUDD D`. Checked for `w ≤ 6`.[^exec] Bala's stacks of large Schröder type are these castles without their bottom up triangles: a stack on a bottom row of `w − 1` down triangles whose boundary is the large Schröder path `𝒫` ([[bala-2019-triangle-stacks-large-schroder-type](pages/bala-2019-triangle-stacks-large-schroder-type.md)]).[^bl-stack]

## Counts

| keystone castles counted by | count | OEIS | from |
|---|---|---|---|
| width `w` | `r_{w−1}`, the large Schröder numbers `1, 2, 6, 22, 90, 394, …` | A006318 | the outline; Bala's stacks of large Schröder type[^bl-count] |
| width and blocks `b` | `A088617(w − 1, b − 1) = C(w + b − 2, w − 1) C(w − 1, b − 1)/b`, the Schröder paths by up-steps | A088617 | the outline |
| width + blocks `s` | `M_{s−2}`, the Motzkin numbers | A001006 | below |
| height 2 | `F_{2w−1} − 1` | A027941 | below |
| cells `n` | `A393774(n − 1)`, `1, 0, 1, 1, 1, 2, 2, 4, 5, 7, 11, 15, …` from one cell | A393774 | below |

Every row agrees with a sweep over the Schröder paths, which agrees with brute-force enumeration of the castles for `w ≤ 6`: width and blocks for `w ≤ 14`, width + blocks for `s ≤ 20`, height 2 for `w ≤ 14`, cells for up to 60 cells, and the cells against the OEIS data of A393774.[^exec]

**Width plus blocks.** A Schröder path of semilength `n` with `k` up-steps has `n − k` flat steps and `n + k` steps in all, so `w + b − 2 = (w − 1) + #U(𝒫)` is the number of steps of `𝒫`. Read with every step of length 1, `𝒫` is a Motzkin path of that length, and every Motzkin path arises once, so the keystone castles with `w + b = s` number the Motzkin numbers `M_{s−2}`: `1, 1, 2, 4, 9, 21, 51, 127, 323, 835, …` ([[motzkin-numbers](pages/motzkin-numbers.md)]).

**Height 2.** A castle of height at most 2 has a path `𝒫` of height at most 1, a sequence of flat steps at level 1 and excursions `U H^j D`, with generating function `1/(1 − x − x/(1 − x)) = (1 − x)/(1 − 3x + x²)` by semilength. Its coefficients are `F_{2n+1}`, and removing the flat path `H^{w−1}` leaves `F_{2w−1} − 1` castles of height 2, `φ²` by width. By cells the castles of height at most 2 have generating function `q/(1 − q² − q³/(1 − q⁴))`, the continued fraction below cut at its second level, and those of height 2 grow at `1.40126834`, the largest root of `z⁶ − z⁴ − z³ − z² + 1`. That polynomial is palindromic, `y = z + 1/z` satisfies the irreducible cubic `y³ − 4y − 1 = 0`, and the two roots of the cubic in `(−2, 2)` put four conjugates of `z` on the unit circle, so the growth constant is a Salem number of degree 6. By width plus blocks the castles of height 2 number `2^{s−3} − 1`.[^exec]

**Cells.** The keystone castles by cells have generating function `q F_large(q, q, 1, 1)`, with `F_large(q, b, u, d)` the continued fraction of Bala's stacks of large Schröder type, since the castle adds its `w` bottom up triangles to a stack on `w − 1` down triangles. At `b = q` that fraction is[^bl-cf]

```
1 / (1 − q² − q³ / (1 − q⁴ − q⁵ / (1 − q⁶ − q⁷ / (1 − ⋯)))),
```

the continued fraction of A393774, so the keystone castles with `n` cells number `A393774(n − 1)`; they grow by cells at `1.46274945`, the ratio of the counts with 200 and 199 cells, and by width at `3 + 2√2 = (1 + √2)²`, the square of the silver mean, the growth of the large Schröder numbers.[^exec]

**By height.** The keystone castles by width and height are the Schröder paths of semilength `w − 1` by height `h − 1`:

| `A_key(w, h)` | `h = 1` | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|
| `w = 1` | 1 | | | | | |
| 2 | 1 | 1 | | | | |
| 3 | 1 | 4 | 1 | | | |
| 4 | 1 | 12 | 8 | 1 | | |
| 5 | 1 | 33 | 43 | 12 | 1 | |
| 6 | 1 | 88 | 197 | 91 | 16 | 1 |
| 7 | 1 | 232 | 833 | 564 | 155 | 20 |
| 8 | 1 | 609 | 3367 | 3133 | 1188 | 235 |

The Schröder paths of height at most `k` have generating function `Sch_k(x) = 1/(1 − x − x Sch_{k−1}(x))`, `Sch_0(x) = 1/(1 − x)`, by the first-return decomposition, so column `h` is `x(Sch_{h−1}(x) − Sch_{h−2}(x))` with `Sch_{−1} = 0`. The entries for `w ≤ 6` agree with brute-force enumeration and the rest come from the sweep.[^exec]

## Triangle stacks are rows of keystone castles

The triangle stacks of A224704, contributed by Paul Tek, are the decompositions of the area beneath a small Schröder path into unit triangles; their bottom row is a run of contiguous up triangles, with down triangles in some of its gaps, and above it they follow the same rules ([[bala-2019-area-beneath-small-schroder-paths](pages/bala-2019-area-beneath-small-schroder-paths.md)]).[^bs-stack] Where the boundary returns to the x-axis the bottom row has no down triangle, and the stack falls apart there into pieces with full bottom rows, which are keystone castles. So every stack is a sequence of keystone castles side by side, and with `K_key(q, u, d)` the keystone castles by cells, width and down triangles, and `F_stack(q, u, d)` Bala's generating function of the stacks,

```
F_stack = 1/(1 − K_key),    K_key = 1 − 1/F_stack = qu / (1 − q²ud − q³ud / (1 − q⁴ud² − q⁵ud² / (1 − q⁶ud³ − ⋯))),
```

by Bala's continued fraction for `F_stack`.[^bs-cf] At `u = d = 1`, `1/(1 − K_key)` agrees with the A224704 data and with Bala's fraction for up to 60 triangles.[^exec] Bala writes `F_stack` as a ratio of two q-series. The stacks grow at `1/x_0 = 1.86565…`, with `x_0` the smallest zero of the denominator series, and the keystone castles, `1 − 1/F_stack`, at `1/y_0 = 1.46275…`, with `y_0 = 0.68364 40770…` the smallest positive zero of the numerator series.[^bs-asym][^exec]

## The 60-degree rows

The triangular tiling has rows in three directions, and a keystone castle can be read along the rows that climb to the right at 60 degrees. Each such row alternates up and down triangles, starting from an up triangle of the bottom row.

**Proposition (60-degree rows).** Number those rows `1, …, w` from the right and let `s_i` be the number of triangles of the castle in row `i`. Then `(s_1, …, s_w)` is a composition of the cells with

```
s_1 = 1,    2 ≤ s_{i+1} ≤ s_i + 1 + (s_i mod 2),
```

and every such composition comes from exactly one keystone castle of width `w`.

*Proof.* Going up a 60-degree row, an up triangle rests on the down triangle before it, and a down triangle needs the up triangle before it and, on its other side, the up triangle at the same place in the next row to the right. So each 60-degree row is filled from its bottom without gaps. The `j`-th down triangle of row `i + 1` needs the `j`-th up triangle of row `i`: a row `i + 1` that ends in a down triangle, `s_{i+1} = 2j`, needs `s_i ≥ 2j − 1`, and one that ends in an up triangle, `s_{i+1} = 2j + 1`, needs the down triangle below it, `s_i ≥ 2j − 1`. So `s_{i+1} ≤ s_i + 1` when `s_{i+1}` is even and `s_{i+1} ≤ s_i + 2` when it is odd, which is `s_{i+1} ≤ s_i + 1 + (s_i mod 2)`. The rightmost row holds only the last bottom up triangle, and every other row holds a bottom up triangle and the bottom down triangle after it, so `s_1 = 1` and `s_{i+1} ≥ 2`.

The six castles of width 3 read `(1, 2, 2)`, `(1, 2, 3)`, `(1, 3, 2)`, `(1, 3, 3)`, `(1, 3, 4)` and `(1, 3, 5)`, in the order (a) to (f). Without the condition `s_{i+1} ≥ 2` the same rule is Tek's description of the stacks of A224704 as compositions of `n` with `a(1) = 1` and `a(i + 1) ≤ a(i) + 1 + (a(i) mod 2)`,[^tek] the 60-degree reading of a stack. Checked for `w ≤ 6`.[^exec] On the brick wall the same reading is the shear of [[brick-wall-castles](pages/brick-wall-castles.md)], where the slants of a fountain rise by at most 1.

## The up triangles are a brick wall

An up triangle above the bottom row rests on a down triangle, which lies between two up triangles of the row below. Read as bricks, each up triangle above the bottom row rests on both up triangles diagonally below it, so the up triangles of a keystone castle of width `w` form a brick-wall castle of width `w` ([[brick-wall-castles](pages/brick-wall-castles.md)]), and every brick-wall castle arises. Over a brick-wall castle `B` the down triangles that carry an up triangle are forced, and each down triangle above the bottom row between two neighboring bricks with no brick on it is free, so `2^{f(B)}` keystone castles have the up triangles `B`, with `f(B)` the number of such places, and `Σ_B 2^{f(B)} = r_{w−1}`. Checked for `w ≤ 6`.[^exec]

## Parity

**Proposition (half even).** For every width `w ≥ 2`, exactly half the keystone castles have an even block count: `S_key(w) = 0`.

*Proof.* The blocks are `1 + #U(𝒫)`. Let `Sch(x, t)` count the large Schröder paths by semilength and up-steps. A nonempty path begins with a flat step or with an excursion `U 𝒫′ D`, so `Sch = 1 + x Sch + t x Sch²`. At `t = −1`, `Sch = 1 + x Sch − x Sch²`, whose power-series solution is `Sch = 1`, so `Σ (−1)^{#U(𝒫)}` over the paths of semilength `n ≥ 1` is 0.

A pairing proves it directly: swap the first flat step or the first peak `UD` of `𝒫`, whichever comes first, `H ↔ UD`. The swap is its own inverse and changes the up-steps by one, and on the castle it puts an up triangle on a down triangle whose top is exposed, or takes one away. Checked for `w ≤ 14`, and the pairing on the paths of semilength at most 8.[^exec] The pairing can change the height, and at a fixed height the split is not even: at width 4 and height 2, 7 castles have an even block count and 5 an odd one.

**Proposition (signed counts at bounded height).**

```
Σ_{w≥1} S_key,≤h(w) x^w  =  −x (1 − (−x)^h) / (1 − (−x)^{h+1}),
```

with `S_key,≤h(w)` the signed count of the keystone castles of width `w` and height at most `h`. The coefficients satisfy `S_key,≤h(w + h + 1) = (−1)^{h+1} S_key,≤h(w)` for `w ≥ 1`, so they repeat with period `h + 1` for odd `h` and `2(h + 1)` for even `h`.

*Proof.* The Schröder paths of height at most `k`, with `t` marking up-steps, have generating function `Sch_k(x, t) = 1/(1 − x − t x Sch_{k−1}(x, t))`, `Sch_0 = 1/(1 − x)`. At `t = −1`, `Sch_k = 1/(1 − x + x Sch_{k−1})`. With `e_j = 1 − (−x)^j`, the identity `(1 − x) e_{k+1} + x e_k = e_{k+2}` (expand both sides) and `Sch_0 = e_1/e_2` give `Sch_k(x, −1) = e_{k+1}/e_{k+2}` by induction. A castle of height at most `h` has `𝒫` of height at most `h − 1` and the sign `−(−1)^{#U(𝒫)}`, which gives the formula with `k = h − 1`. Its numerator `−x(1 − (−x)^h)` has degree `h + 1` and no constant term, so from `x^1` on each coefficient is `(−1)^{h+1}` times the one `h + 1` places before.

At height at most 2 the signed counts are `−1, 0, 1, 1, 0, −1, −1, 0, …`, and at height 2 they are `S_key(w, 2) = 0, 1, 2, 2, 1, 0` repeated. Checked for `h ≤ 8`, `w ≤ 40`.[^exec] The signed counts on the brick wall grow with the width ([[brick-wall-castles](pages/brick-wall-castles.md)]); on the triangular tiling they stay bounded at every height.

**Fixed height.** The keystone version of the Project Euler 502 count is `A^e_key(w, h)`. At height 2, `A^e_key(w, 2) = (F_{2w−1} − 1 + S_key(w, 2))/2`:

| `A^e_key(w, h)` | `w = 1` | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `h = 1` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 2 | 0 | 1 | 3 | 7 | 17 | 44 | 116 | 305 | 799 | 2091 | 5473 | 14328 |
| 3 | 0 | 0 | 0 | 3 | 21 | 99 | 417 | 1683 | 6621 | 25602 | 97878 | 371382 |
| 4 | 0 | 0 | 0 | 1 | 7 | 46 | 282 | 1567 | 8145 | 40563 | 196169 | 928999 |
| 5 | 0 | 0 | 0 | 0 | 0 | 7 | 77 | 594 | 3982 | 24531 | 142777 | 798515 |
| 6 | 0 | 0 | 0 | 0 | 0 | 1 | 11 | 118 | 1066 | 8294 | 58370 | 383215 |

| `S_key(w, h)` | `w = 1` | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `h = 1` | −1 | −1 | −1 | −1 | −1 | −1 | −1 | −1 | −1 | −1 | −1 | −1 |
| 2 | 0 | 1 | 2 | 2 | 1 | 0 | 0 | 1 | 2 | 2 | 1 | 0 |
| 3 | 0 | 0 | −1 | −2 | −1 | 1 | 1 | −1 | −2 | −1 | 0 | 0 |
| 4 | 0 | 0 | 0 | 1 | 2 | 1 | 0 | 1 | 1 | −1 | −1 | 1 |
| 5 | 0 | 0 | 0 | 0 | −1 | −2 | −1 | 0 | 0 | 1 | 1 | −1 |
| 6 | 0 | 0 | 0 | 0 | 0 | 1 | 2 | 1 | 0 | 0 | 0 | 1 |

The entries for `w ≤ 6` agree with brute-force enumeration and the rest come from the sweep.[^exec]

## Appearances in Sources

- [[bala-2019-area-beneath-small-schroder-paths](pages/bala-2019-area-beneath-small-schroder-paths.md)] - the triangle stacks of A224704, the rows of keystone castles, their continued fraction, the ratio `N/D` of q-series and the growth of the stacks.
- [[bala-2019-triangle-stacks-large-schroder-type](pages/bala-2019-triangle-stacks-large-schroder-type.md)] - the keystone castles without their bottom up triangles, the large Schröder count and the continued fraction that counts the castles by cells.

## Related Concepts

- [[brick-wall-castles](pages/brick-wall-castles.md)] - the castles on the hexagonal tiling, which the up triangles of a keystone castle form, with the Dyck paths in the place of the Schröder paths.
- [[castle-polyomino](pages/castle-polyomino.md)] - the castles on the square grid and their blocks.
- [[motzkin-numbers](pages/motzkin-numbers.md)] - the keystone castles by width plus blocks.
- [[prime-castles](pages/prime-castles.md)] - the square-grid castles factored into primes, as the triangle stacks factor into keystone castles.
- [[castle-sign](pages/castle-sign.md)] - the signed count `S` and the parity split on the square grid.

## Footnotes

[^bl-stack]: [[bala-2019-triangle-stacks-large-schroder-type](pages/bala-2019-triangle-stacks-large-schroder-type.md)] §1 pp.1-2 L15-L38 [synthesis] - "we vary the construction of a triangle stack by starting with the bottom row of the stack consisting of contiguous down-triangles"; "Each triangle stack of large Schröder type is associated in a obvious way with a large Schröder path"; "There is a bijection between large Schröder paths and triangle stacks of large Schröder type (hence the choice of name)."
[^bl-count]: [[bala-2019-triangle-stacks-large-schroder-type](pages/bala-2019-triangle-stacks-large-schroder-type.md)] §4 p.4 L151-L161 - "This is a known representation for the generating function of the sequence of large Schröder numbers A006318, and simply reflects the bijection between large Schröder paths of semilength n and triangle stacks of large Schröder type with a bottom row of n down-triangles."
[^bl-cf]: [[bala-2019-triangle-stacks-large-schroder-type](pages/bala-2019-triangle-stacks-large-schroder-type.md)] §3 p.4 L141-L147 [synthesis] - "Succesive iterations of this identity lead to a formal continued fraction expansion for the generating function of the number of weighted triangle stacks of large Schröder type", (2), `1/(1 − qbd − q²bud/(1 − q³bud² − q⁴bu²d²/(1 − q⁵bu²d³ − q⁶bu³d³/(1 − ⋯))))`, with `q` marking the area and `b` the down triangles of the bottom row.
[^bs-stack]: [[bala-2019-area-beneath-small-schroder-paths](pages/bala-2019-area-beneath-small-schroder-paths.md)] §1 pp.1-2 L13-L43 [synthesis] - "A small Schröder path is a Schröder path with no flat steps on the x-axis."; "The area between a small Schröder path and the x-axis can be decomposed into triangles each of unit area. We call such a decomposition of the area a triangle stack."; "Note that a triangle stack has a sequence of contiguous up triangles in its bottom row."
[^bs-cf]: [[bala-2019-area-beneath-small-schroder-paths](pages/bala-2019-area-beneath-small-schroder-paths.md)] §2 pp.7-8 L268-L282 [synthesis] - the continued fraction (8) of Bala's `F(q, u, d)`, the page's `F_stack`, `1/(1 − qu/(1 − q²ud − q³ud/(1 − q⁴ud² − q⁵ud²/(1 − q⁶ud³ − ⋯))))`, with `q` marking the area, `u` the up triangles of the bottom row and `d` the down triangles.
[^bs-asym]: [[bala-2019-area-beneath-small-schroder-paths](pages/bala-2019-area-beneath-small-schroder-paths.md)] §3 pp.9-10 L364-L396 [synthesis] - the ratio `N(q)/D(q)` of q-series at `u = d = 1`, (16); "the smallest real zero of the denominator series D(q) is located at x0 = 0.53600 49695 29708 61653", "a simple zero", and `A224704(n) ~ c/x_0^n`.
[^tek]: https://oeis.org/A224704 (read 2026-10-29) - "A stack is formed by starting with a row of triangles pointing upwards, and then additional triangles pointing downwards can be inserted between adjacent triangles pointing upwards, and additional triangles pointing upwards can be put on top of triangles pointing downwards."; "Number of compositions of n with a(1) = 1 and a(i+1) <= a(i) + 1 + mod(a(i),2)."
[^exec]: Verified by execution (Python 3.11, 2026-10-29): `bin/python/keystone_castles.py`, run log `bin/python/keystone_castles-run.log`. Item [1], the outline `U 𝒫 D` of every keystone castle of width `w ≤ 6`, a bijection onto the large Schröder paths with height, blocks and cells as stated; [2], the bottom row and the cells against `q F_large(q, q, 1, 1)` for up to 60 cells; [3], the counts by width, blocks, height 2 and width plus blocks, and the sweep against brute force; [4], the cells against A393774 and `1/(1 − K)` against A224704 and Bala's fraction (8); [5], the 60-degree rows for `w ≤ 6`; [6], the up triangles as brick-wall castles and the `2^{f(B)}` keystone castles over each; [7], the signed count over all heights for `w ≤ 14` and the pairing; [8], the signed counts at height at most `h ≤ 8` for `w ≤ 40` and their period; [9], the tables of `A_key`, `A^e_key` and `S_key` for `h ≤ 6`, `w ≤ 14`, and the height-2 even-block formula for `w ≤ 24`; [10], the zero `y_0` of Bala's numerator series and the ratios of the counts by cells; [11], the castles of height 2 by cells against `q/(1 − q² − q³/(1 − q⁴)) − q/(1 − q²)` and by width plus blocks against `2^{s−3} − 1`, their growth by cells, the factorization of `z⁶ − z⁴ − z³ − z² + 1` through `y³ − 4y − 1` and the moduli of its roots, and the ratio of the counts by width against `3 + 2√2`.
