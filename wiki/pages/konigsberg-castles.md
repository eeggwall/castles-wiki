---
title: Königsberg castles
category: Concepts
summary: Join one ground vertex to every bottom cell of the castle graph. A Königsberg castle is a castle whose graph with its ground has every degree even, so that by Euler's theorem one closed stroke crosses every side between two cells and every side on the ground exactly once; the Königsberg castles are exactly the double staircases (1, 2, …, k, k, …, 2, 1), one at each even width, with k blocks. Whether a cell has odd degree depends only on the heights of the two neighboring columns, so an open-stroke castle, with exactly two odd vertices, has at most two defect columns and at most 6h + 2 columns. At odd widths the open-stroke castles of height h number h² + 3h − 2, in five families; with the even widths they number 3, 33, 137, 377, 831, … at h = 1, 2, 3, …, which for h ≤ 12 is (2h⁴ + 11h³ − 5h² − 2h + 3)/3.
tags: [concept, castle, konigsberg-castle, open-stroke-castle, castle-graph, eulerian-graph, euler, degree, parity, double-staircase, convex-castle, block-count, verification]
sources: [project-euler-502-brute-force]
created: 2026-10-28
updated: 2026-10-28
---

# Königsberg castles

## Definition

The castle graph of a castle `c = (c_1, …, c_w)` has the cells as vertices and an edge between two cells that share a side ([[castle-graph](pages/castle-graph.md)]). The **castle graph with its ground** has one more vertex, the **ground**, joined to every cell of the bottom row. Read as Euler's map of Königsberg, the cells and the ground are the land masses, and the sides shared by two cells or by a bottom cell and the ground are the bridges; Euler asked for a walk that crosses each bridge once and not more than once.[^euler-problem]

**Euler's theorem.** A connected graph has a closed walk that uses every edge exactly once if and only if every vertex has even degree, and a walk that uses every edge exactly once and ends where it did not start if and only if exactly two vertices have odd degree; such a walk starts at one of them and ends at the other. Euler proved that the degree conditions are necessary and stated that they suffice, which Hierholzer proved in 1873.[^eulerian] The castle graph with its ground is connected, since every cell is joined through its column to the bottom row.

- A **Königsberg castle** is a castle whose graph with its ground has every degree even: it can be traced in one closed stroke.
- An **open-stroke castle** is a castle whose graph with its ground has exactly two vertices of odd degree: it can be traced in one stroke from one of them to the other, and in no closed stroke.

*Examples.* The degrees of the cells of `(1, 2, 2, 1)`, drawn row by row from the top, and of `(1, 1, 1, 1)`:

```
(1, 2, 2, 1)                     (1, 1, 1, 1)

. 2 2 .
2 4 4 2      ground: 4           2 3 3 2      ground: 4
```

Every degree of `(1, 2, 2, 1)` is even, so it is a Königsberg castle. The flat castle `(1, 1, 1, 1)` has its two middle cells of degree 3 and every other degree even, so it is an open-stroke castle.[^exec1]

## The parity of a degree

Write `c_0 = c_{w+1} = 0` for the ground beyond the end columns. Cell `(i, r)`, in column `i` and row `r`, is joined to the cell below it or, when `r = 1`, to the ground; to the cell above it when `r < c_i`; and to the cells of row `r` in columns `i − 1` and `i + 1` when those columns reach row `r`. So with `a = c_{i−1}`, `x = c_i` and `b = c_{i+1}`,

```
deg(i, r)  =  1 + [r < x] + [a ≥ r] + [b ≥ r],
```

and the ground has degree `w`.

**Lemma 1.** (a) A cell below the top of its column has even degree exactly when both neighboring columns reach its row or neither does. (b) The top cell of a column has even degree exactly when one neighboring column is at least as tall as the column and the other is not. (c) A column of height `x` between columns of heights `a` and `b` has

```
d(a, x, b)  =  |min(a, x − 1) − min(b, x − 1)|  +  [ (a ≥ x) = (b ≥ x) ]
```

cells of odd degree, its **defect**, and the castle graph with its ground has `Σ_i d(c_{i−1}, c_i, c_{i+1}) + [w odd]` vertices of odd degree.

*Proof.* (a) and (b) are the degree formula at `r < x` and at `r = x`. For (c), a row `r < x` is reached by exactly one neighboring column when `r` lies above one of `min(a, x − 1)` and `min(b, x − 1)` and not above the other, and there are `|min(a, x − 1) − min(b, x − 1)|` such rows; the top cell adds 1 when it is odd, by (b).[^exec1]

A column of defect 0 has, by (b), one neighbor at least as tall and the other lower, and by (a) the lower one is exactly one lower. Call it **rising** when the lower neighbor is on the left (`a = x − 1`, `b ≥ x`) and **falling** when it is on the right (`b = x − 1`, `a ≥ x`).

**Lemma 2 (runs).** In a run of consecutive columns of defect 0, a rising column of height `x` is followed by a rising column of height `x + 1` or a falling column of height `x`, and a falling column of height `x` is followed by a falling column of height `x − 1`. A run that begins at the left end begins with a rising column of height 1, and a run that ends at the right end ends with a falling column of height 1.

*Proof.* A rising column of height `x` has a right neighbor of height `y ≥ x`, whose left neighbor is the column of height `x`. If `y = x + 1` that neighbor is one lower, so the column of height `y` is rising; if `y = x` it is at least as tall, so the column is falling; if `y ≥ x + 2` it is neither, and the column has positive defect. A falling column of height `x` has a right neighbor of height `x − 1`, whose left neighbor is taller, so it is falling. The first column has the ground, height 0, on its left, which cannot be at least as tall, so the first column is rising with `c_1 = 1`; in the same way the last column is falling with `c_w = 1`.

So a run climbs by one column at a time, repeats its top once and falls by one at a time: a ramp `t, t + 1, …, p`, then `p, p − 1, …, q`, where either part may be missing.

## The Königsberg castles

**Theorem.** The Königsberg castles are exactly the double staircases

```
(1, 2, …, k, k, …, 2, 1),    k ≥ 1,
```

of width `2k`, height `k` and area `k(k + 1)`: `(1, 1)`, `(1, 2, 2, 1)`, `(1, 2, 3, 3, 2, 1)`, ….

*Proof.* In a Königsberg castle every column has defect 0, so the castle is one run from the left end to the right end. By Lemma 2 it climbs from 1 to some height `k`, repeats `k` once, and falls back to 1. Its width `2k` is even, so the ground has even degree too. Conversely, in a double staircase every column of the climb is rising, every column of the fall is falling, and the ground has degree `2k`.[^exec2]

So there is one Königsberg castle at each even width and none at an odd width, whose ground has odd degree. A double staircase rises and then falls, so it is a convex castle and has `k` blocks, one per row ([[convex-castle](pages/convex-castle.md)]): it is an even-block castle exactly when `k` is even.

## Castles traced in one open stroke

By Lemma 1 an open-stroke castle has `Σ d + [w odd] = 2`. At an odd width the ground is odd, so exactly one column has defect 1 and the others have defect 0. At an even width either two columns have defect 1 or one column has defect 2.

**The defect columns.** For a column of height `x` with neighbors of heights `a` and `b`, the formula of Lemma 1 gives:

| defect | the column of height `x` | example, the middle column of |
|---|---|---|
| 1 | **dip**: both neighbors at least as tall, `a, b ≥ x` | `(2, 1, 2)` |
| 1 | **spike**: both neighbors lower and equal, `a = b < x` | `(1, 3, 1)` |
| 1 | **step of 2**: one neighbor exactly two lower, the other at least as tall | `(1, 3, 3)` |
| 2 | spike whose neighbors differ by one: `a, b < x`, `\|a − b\| = 1` | `(1, 3, 2)` |
| 2 | step of 3: one neighbor exactly three lower, the other at least as tall | `(1, 4, 4)` |

These are all the columns of defect 1 and 2: the top cell is odd exactly when both neighbors are at least as tall or both are lower; if both are at least as tall the first term of `d` is 0, if both are lower it is `|a − b|`, and if one is at least as tall and the other, of height `a`, is lower, it is `x − 1 − a`.

**Finitely many at each height.** An open-stroke castle has at most two columns of positive defect, so at most three runs, and a run has at most `2h` columns, since its rising columns have distinct heights and so do its falling ones. So an open-stroke castle of height `h` has at most `6h + 2` columns, and there are finitely many. For `h ≤ 12` the widest have width `6h − 2`, one at each height: three double staircases that share their end columns, such as `(1, 2, 2, 1, 2, 2, 1, 2, 2, 1)` at height 2, whose two shared columns are dips.[^exec4]

### Odd widths

**Theorem.** At an odd width, the open-stroke castles of height `h` are the castles of the five families below, each castle in one family, and there are `h² + 3h − 2` of them.

| family | castles of height `h` | width | number |
|---|---|---|---|
| dip between two ramps | `(1, …, h, h, h, h − 1, …, 1)` | `2h + 1` | 1 |
| dip between a ramp and a hill | `(1, …, x, x, x + 1, …, h, h, h − 1, …, 1)` and its mirror image, `1 ≤ x ≤ h − 1` | `2h + 1` | `2(h − 1)` |
| dip between two hills | `(1, …, p, p, p − 1, …, x + 1, x, x + 1, …, q, q, q − 1, …, 1)` with `max(p, q) = h`, `1 ≤ x < min(p, q)` | `2p + 2q − 2x + 1` | `(h − 1)²` |
| spike | `(1, …, p, h, p, …, 1)`, `0 ≤ p ≤ h − 1` | `2p + 1` | `h` |
| step of 2 | `(1, …, h − 2, h, h, h − 1, …, 1)`, and `(1, …, p, p + 2, p + 3, …, h, h, h − 1, …, 1)` for `0 ≤ p ≤ h − 3`, and their mirror images | `2h − 1` | `2(h − 1)` |

The family is named by its defect column and the runs on either side of it. At `h = 4` the five families have 1, 6, 9, 4 and 6 castles, 26 in all.[^exec5]

*Proof.* One column `D`, of height `x`, has defect 1. The columns before `D` are a run that begins at the left end, or there are none, and by Lemma 2 that run is a **ramp** `(1, …, p)`, whose last column is rising and so needs `x ≥ p`, or a **hill** `(1, …, p, p, …, x + 1)`, whose last column is falling and so needs `D` to be one lower. The columns after `D` are the mirror image: a ramp `(p, …, 1)` with `p ≤ x`, or a hill `(x + 1, …, p, p, …, 1)`. So each neighbor of `D` has height 0 (no run), `p ≤ x` (a ramp) or `x + 1` (a hill), and the type of `D` decides the rest:

- A dip needs both neighbors at least as tall: on each side a ramp of height exactly `x` or a hill. Ramps on both sides make `x = h`; a ramp on one side and a hill on the other make the hill's top `h`; and with hills on both sides the taller top is `h`.
- A spike needs both neighbors lower and equal: no runs at all, or ramps of the same height `p < x` on both sides. The spike is the tallest column, `x = h`.
- A step of 2 rising to the right has a left neighbor two lower, either the ground (no run, `x = 2`) or a ramp of height `x − 2`, and a right neighbor at least as tall, either a ramp of height `x`, which makes `x = h`, or a hill with top `h`. Its mirror images are the steps of 2 falling to the right.

Counting the parameters gives the numbers in the table, and `1 + 2(h − 1) + (h − 1)² + h + 2(h − 1) = h² + 3h − 2`.[^exec5]

The widths in the table settle the odd widths one at a time: below `2h − 1` only the spikes occur, one castle at each odd width; at `2h − 1` the widest spike and the `2(h − 1)` steps of 2 make `2h − 1`; at `2h + 1` the dips between two ramps and between a ramp and a hill make `2h − 1`; and the dips between two hills fill the odd widths from `2h + 3` to `4h − 1`. Every castle of the first, second, fourth and fifth families rises and then falls, so it is convex with `h` blocks; a dip between two hills has `h + min(p, q) − x` blocks, its total ascent.[^exec5]

### All widths

At an even width two columns of defect 1, or one of defect 2, separate up to three runs, and they combine in many more ways. A left-to-right scan whose state is the last two column heights, the number of odd vertices so far and the block parity counts them:[^exec3][^exec4]

| `h` | open-stroke castles | odd widths | even widths | even-block | odd-block |
|---|---|---|---|---|---|
| 1 | 3 | 2 | 1 | 0 | 3 |
| 2 | 33 | 8 | 25 | 23 | 10 |
| 3 | 137 | 16 | 121 | 49 | 88 |
| 4 | 377 | 26 | 351 | 225 | 152 |
| 5 | 831 | 38 | 793 | 354 | 477 |
| 6 | 1593 | 52 | 1541 | 887 | 706 |
| 7 | 2773 | 68 | 2705 | 1259 | 1514 |
| 8 | 4497 | 86 | 4411 | 2417 | 2080 |
| 9 | 6907 | 106 | 6801 | 3236 | 3671 |
| 10 | 10161 | 128 | 10033 | 5351 | 4810 |
| 11 | 14433 | 152 | 14281 | 6885 | 7548 |
| 12 | 19913 | 178 | 19735 | 10353 | 9560 |

By width, the open-stroke castles of height 2 number `1, 3, 3, 6, 3, 10, 1, 5, 0, 1` for `w = 1, …, 10`, and those of height 3 number `1, 2, 1, 12, 5, 22, 5, 35, 3, 29, 1, 15, 0, 5, 0, 1` for `w = 1, …, 16`.

For `h ≤ 12`, by computation and with no proof yet, the even widths total `(2h⁴ + 11h³ − 8h² − 11h + 9)/3`, so with the odd widths all open-stroke castles of height `h` number `(2h⁴ + 11h³ − 5h² − 2h + 3)/3`; and the open-stroke castles of height `h` number `m(m + 1)` at each even width `2m ≤ 2h − 4`, `3(h − 1)²` at width `2h − 2`, and `(5h − 4)(h − 1)` at width `2h`.[^exec4]

## Related Concepts

- [[castle-graph](pages/castle-graph.md)] - the castle graph, to which the ground is added here.
- [[convex-castle](pages/convex-castle.md)] - the castles of height `h` with `h` blocks, among them the double staircases.
- [[valley-castles](pages/valley-castles.md)] - valleys of castles; a dip with both neighbors taller is the floor of a valley of span 1.
- [[euler-castles](pages/euler-castles.md)] - the castles that fall by 0 or 1 at each step to height 1; the falling half `(k, …, 2, 1)` of a double staircase is one.
- [[castle-sign](pages/castle-sign.md)] - the sign `(−1)^blocks` of the parity split.
- [[castle-notation](pages/castle-notation.md)] - the symbols of this page.

## Footnotes

[^euler-problem]: L. Euler, "Solutio problematis ad geometriam situs pertinentis", *Commentarii academiae scientiarum Petropolitanae* 8 (1741), 128-140 (publication data from https://scholarlycommons.pacific.edu/euler-works/53/, read 2026-10-28); English translation of §1-9 at https://www.math.stonybrook.edu/~tony/archive/336s20/documents/Euler-Koenigsberg-translation.pdf (read 2026-10-28) §2 - "in Königsberg in Prussia is an island A called der Kneiphof, and the river surrounding it divides into two branches, as can be seen from the figure: the branches of this river are crossed by seven bridges, a, b, c, d, e, f, and g. Concerning these bridges the question was asked, whether someone would be able to devise such a path, so as to cross each bridge once and not more than once."
[^eulerian]: https://en.wikipedia.org/wiki/Eulerian_path (read 2026-10-28) - "Euler proved that a necessary condition for the existence of Eulerian circuits is that all vertices in the graph have an even degree, and stated without proof that connected graphs with all vertices of even degree have an Eulerian circuit. The first complete proof of this latter claim was published posthumously in 1873 by Carl Hierholzer." and §Properties, "An undirected graph has an Eulerian trail if and only if exactly zero or two vertices have odd degree, and all of its vertices with nonzero degree belong to a single connected component"; "If there are exactly two vertices of odd degree, all Eulerian trails start at one of them and end at the other."
[^exec1]: Verified by execution (Python 3.11, 2026-10-28): `bin/python/konigsberg_castles.py` item [1], run log `bin/python/konigsberg_castles-run.log`. For every castle with `w ≤ 7`, `h ≤ 5`, the odd vertices of the castle graph with its ground, from an explicit adjacency list, number `Σ d + [w odd]`; the two examples.
[^exec2]: Verified by execution (Python 3.11, 2026-10-28): `bin/python/konigsberg_castles.py` item [2], run log `bin/python/konigsberg_castles-run.log`. The castles with every degree even are the double staircases, by brute force for `w ≤ 8`, `h ≤ 5` and by the column scan for `w ≤ 30`, `h ≤ 15`.
[^exec3]: Verified by execution (Python 3.11, 2026-10-28): `bin/python/konigsberg_castles.py` item [3], run log `bin/python/konigsberg_castles-run.log`. The column scan against brute force, with the block parity, for `w ≤ 8`, `h ≤ 5`, `h^w ≤ 400000`.
[^exec4]: Verified by execution (Python 3.11, 2026-10-28): `bin/python/konigsberg_castles.py` item [4], run log `bin/python/konigsberg_castles-run.log`. The table for `h ≤ 12` by the column scan over every width up to `6h + 3`; the widest castles, of width `6h − 2`, by exhaustive search for `h ≤ 7`; the polynomials, fitted on `h ≤ 5` and checked on `h ≤ 12`; the counts at the widths `2m ≤ 2h − 4`, `2h − 2` and `2h`, and at the odd widths below `2h − 1`, for `h ≤ 12`.
[^exec5]: Verified by execution (Python 3.11, 2026-10-28): `bin/python/konigsberg_castles.py` item [5], run log `bin/python/konigsberg_castles-run.log`. The five families equal the set of open-stroke castles of odd width found by exhaustive search for `h ≤ 7`, with no castle in two families, and their count `h² + 3h − 2` matches the column scan for `h ≤ 12`; every castle outside the dips between two hills has `h` blocks, and the dips between two hills have `h + min(p, q) − x`, for `h ≤ 7`; the widths of the families for `h ≤ 7`.
