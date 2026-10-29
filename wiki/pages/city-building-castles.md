---
title: City-building castles
category: Concepts
summary: A city-building castle is a castle in which, with the ground in front as a column of height 0, every column sees exactly as many of the columns before it as its height, under the visibility rule of the city-building sequence A400000 (an earlier top is seen when every top between is on or below the segment joining the two). The prefixes of A400000 are the city-building castles built by always taking the lowest legal column. Each height has finitely many, of width at most 2! + 3! + … + (h + 1)!, and cutting a castle at its columns of height h makes the runs between them independent; the city-building castles of height h = 1, …, 5 number 2, 12, 600, 965952 and 31776964193520, and the widest have widths 2, 7, 18, 44 and 111.
tags: [concept, castle, city-building-castle, visibility, oeis, a400000, finiteness, block-count, parity, valley, verification]
sources: [project-euler-502-brute-force]
created: 2026-10-25
updated: 2026-10-29
---

# City-building castles

## Definition

A castle of width `w` and height `h` is a skyline `(c_1, …, c_w)` with `1 ≤ c_i ≤ h` and some `c_i = h` ([[castle-polyomino](pages/castle-polyomino.md)]). Put the ground in front of it as a column 0 of height `c_0 = 0`, and draw each column `i` as its top, the point `(i, c_i)`. The top of column `j` **sees** an earlier column `i < j` when every top strictly between them is on or below the segment from `(i, c_i)` to `(j, c_j)`. This is the rule of the city-building sequence A400000, which calls the columns buildings.[^rule] Two neighboring columns always see each other, and ties count as seen.

A **city-building castle** is a castle in which every column `j` sees exactly `c_j` of the columns `0, 1, …, j − 1`. The name follows A400000, "the city-building sequence".[^name]

*Examples.* In every city-building castle `c_1 = 1`, since column 1 sees only the ground. The castle `(1, 2)` is city-building: its second column sees column 1 and, since the top `(1, 1)` lies on the segment from `(0, 0)` to `(2, 2)`, the ground. The castle `(1, 1, 1)` is not: its third column sees columns 2 and 1, since the top `(2, 1)` lies on the flat segment between them. The widest city-building castle of height 2 is `(1, 1, 2, 1, 2, 2, 1)`.[^exec-ex]

A city-building castle with its last column removed is again city-building, since each column's condition looks only to its left.

## The city-building sequence

A400000 builds a skyline one column at a time: `a(1) = 0`, and `a(n)` is the lowest height `k ≥ 0` at which a new column sees exactly `k` of the columns before it.[^name] So `a(1)` is the ground, every later term is at least 1, and for each width `w` the terms `a(2), …, a(w + 1)` form a city-building castle `C_w`, of height the largest term so far. The `C_w` are the city-building castles obtained by always taking the lowest legal next column. A spike of the sequence is a castle with no low continuation: `C_14 = (1, 1, 2, 1, 2, 1, 3, 1, 2, 1, 3, 1, 2, 1)` has height 3 and no legal next column of height 1 to 9, so `a(16) = 10`.[^exec1]

Rémy Sigrist proved in the entry that the sequence is infinite and unbounded.[^sigrist] A city-building castle need not take the lowest legal column, and the castles below count all of them.

## Notation used on this page

| symbol | meaning |
|---|---|
| `A_city(w, h)` | the city-building castles of width `w` and height `h`; `A^e_city`, `A^o_city` the even-block and odd-block ones |
| `first_h(v)` | the first runs (defined in *Cutting at the columns of height h*) from whose end a column of height `h` sees exactly `v` columns, the ground included |
| `wall_h(v)` | the walled runs from whose end a column of height `h` sees exactly `v` columns of the run |
| `walled_h` | the number of walled runs, the empty run included |

## Finitely many at each height

**Theorem.** A city-building castle of height `h` has width at most `2! + 3! + ⋯ + (h + 1)!`.

*Flat step.* A column of height `m` sees every earlier column of height `m` that has no taller column between them, because the segment between the two tops is flat at height `m`. This is the last step of Sigrist's proof that A400000 is unbounded.[^sigrist] In a castle of height `h`, nothing is taller than `h`, so the `k`-th column of height `h` sees at least `k − 1` columns, and a castle of height `h` has at most `h + 1` columns of height `h`.

*Wall step.* Take a run of columns of height at most `m` that starts right after a column taller than `m`. The `k`-th column of height `m` in the run sees that taller column, since the segment falls from above `m` to `m` and every top between is at most `m`, and it sees the `k − 1` earlier columns of height `m` of the run by the flat step. So the run has at most `m` columns of height `m`.

*Recursion.* Removing those columns splits the run into at most `m + 1` runs of height at most `m − 1`, each starting right after a column taller than `m − 1`. A run of height at most 0 is empty, so by induction such a run has at most `m + (m + 1)(m! − 1) = (m + 1)! − 1` columns. A castle of height `h` is a first run of height at most `h − 1`, which is a city-building castle of height at most `h − 1`, followed by at most `h + 1` columns of height `h`, each followed by a run of height at most `h − 1` with at most `h! − 1` columns. So the width bound grows by at most `(h + 1) + (h + 1)(h! − 1) = (h + 1)!` from height `h − 1` to height `h`, and it is `0` at height 0.[^exec3]

The widest city-building castles of heights 1 to 5 have widths 2, 7, 18, 44 and 111, against the bounds 2, 8, 32, 152 and 872.[^exec4]

## Cutting at the columns of height h

Cut a city-building castle of height `h` at its columns of height `h`. It is a **first run**, a city-building castle of height at most `h − 1` or the empty run, followed by `t` columns of height `h`, with `1 ≤ t ≤ h + 1`, each followed by a **walled run**: a run of columns of height at most `h − 1` in which every column sees exactly its height among the column of height `h` before the run and the earlier columns of the run. Three facts make the runs independent:

- **A column lower than `h` never sees past the nearest column of height `h` to its left.** The segment from a top below `h` to any earlier top passes strictly below `h` over every column between, so a column of height `h` there rises above it.
- **A column of height `h` sees every earlier column of height `h`, and of the other columns only those after the last earlier column of height `h`.** The first part is the flat step; the second is the first fact with the roles of the ends exchanged.
- **So each column's condition involves only its own run** and the column of height `h` before it (for the first run, the ground), and the `k`-th column of height `h` sees the `k − 1` earlier ones and some columns of the run just before it.

The column of height `h` before a walled run is not always seen from inside the run: the four widest city-building castles of height 3 end in `3, 1, 2, 2, 1`, and their last column does not see the `3`: the segment from its top to the top of the `3` passes below the top of the column of height 2 next to it.[^exec5] So a walled run depends on the height `h` of its wall, not only on its own columns.

With `first_h`, `wall_h` and `walled_h` as in the notation table, the conditions on the columns of height `h` give

```
Σ_w A_city(w, h)  =  first_h(h) · walled_h · Σ_{t=1}^{h+1} Π_{k=2}^{t} wall_h(h − k + 1),
```

where the empty product is 1 and the factor `walled_h` counts the last run, which no column of height `h` follows. The same product with each run weighted by its width and by the parity of its block count gives `A^e_city(w, h)` and `A^o_city(w, h)`: the block count adds over the pieces, plus the rise from the end of each run up to the next column of height `h`. At height 5 the first runs are the 966,567 city-building castles of height at most 4 and the empty run, and the walled runs number 3,389.[^exec4]

The cut does not reach height 6 in the same way. Its first runs are all the city-building castles of height at most 5, and a column of height 6 can see over a column of height 5, so what it sees in a first run is not decided by that run's own cut.

## Counts

| `h` | city-building castles | even-block | odd-block | widest |
|---|---|---|---|---|
| 1 | 2 | 0 | 2 | 2 |
| 2 | 12 | 4 | 8 | 7 |
| 3 | 600 | 300 | 300 | 18 |
| 4 | 965,952 | 482,008 | 483,944 | 44 |
| 5 | 31,776,964,193,520 | 15,888,512,606,734 | 15,888,451,586,786 | 111 |

By width, for `w = 1, 2, …` up to the widest:[^exec4]

| `h` | `A_city(w, h)` | `A^e_city(w, h)` |
|---|---|---|
| 2 | `0, 1, 2, 2, 3, 3, 1` | `0, 1, 2, 1, 0, 0, 0` |
| 3 | `0, 0, 2, 3, 5, 12, 18, 23, 39, 56, 65, 81, 90, 78, 61, 43, 20, 4` | `0, 0, 0, 0, 4, 9, 9, 10, 19, 29, 36, 44, 44, 35, 28, 21, 10, 2` |

The rows for heights 4 and 5 are in the run log. Over all heights, the city-building castles of width `w = 1, …, 14` number `1, 2, 4, 8, 18, 43, 96, 197, 416, 917, 1984, 4232, 9037, 19264`.[^exec2] The totals by height, the widest widths, the counts by width over all heights and the width rows at heights 3 and 5 had no match in the OEIS on 2026-10-25.

## Valleys

A valley of a castle is a pair of columns `i < j − 1` with every column between lower than both ([[valley-castles](pages/valley-castles.md)]). Every column between is then below the segment joining the two tops, so the walls of a valley see each other. In a city-building castle, a column `j ≥ 2` therefore sees at least its left neighbor and the left wall of every valley whose right wall is `j`:

```
c_j  ≥  1 + (the number of valleys with right wall j),          j ≥ 2.
```

With `c_1 = 1`, adding over the columns gives `Σ c_j ≥ w + val(c)`: a city-building castle has area at least its width plus its number of valleys.[^exec6]

## Related Concepts

- [[valley-castles](pages/valley-castles.md)] - valleys and the horizontally visible pairs, a stricter visibility than the city-building rule; the bound of the section *Valleys*.
- [[castle-classification-shape](pages/castle-classification-shape.md)] - the catalog entry for the city-building type.
- [[castle-notation](pages/castle-notation.md)] - the two visibility rules on the wiki.
- [[castle-polyomino](pages/castle-polyomino.md)] - castles as skylines.

## Footnotes

[^rule]: https://oeis.org/A400000 (read 2026-10-25) - "A building a(j) "sees" an earlier building a(i) if every intermediate building a(k), i < k < j, has its top (k, a(k)) on or below the straight line joining (i, a(i)) and (j, a(j))."
[^name]: https://oeis.org/A400000 (read 2026-10-25) - "The city-building sequence: a(n) = the height h of the shortest building which can see exactly h earlier buildings."; data "0,1,1,2,1,2,1,3,1,2,1,3,1,2,1,10,…".
[^sigrist]: https://oeis.org/A400000 (read 2026-10-25), comment of Rémy Sigrist, Sep 16 2026 - "The sequence is infinite", "The sequence is unbounded", and "the (m+2)-th occurrence of m beyond s sees the m+1 prior m's: a contradiction."
[^exec-ex]: Verified by execution (Python 3.10, 2026-10-25): `bin/python/city_building_castles.py` item [7], run log `bin/python/city_building_castles-run.log`. The examples `(1, 2)` and `(1, 1, 2, 1, 2, 2, 1)` are city-building, `(1, 1, 1)` is not, and `(1, 1, 2, 1, 2, 2, 1)` is the only city-building castle of height 2 and width 7.
[^exec1]: Verified by execution (Python 3.10, 2026-10-25): `bin/python/city_building_castles.py` item [1], run log `bin/python/city_building_castles-run.log`. The lowest-choice rule gives the 84 terms of A400000's data field; every term after the first is at least 1, every `C_w` in that range is city-building, and `C_14` has no legal next column of height 0 to 9.
[^exec2]: Verified by execution (Python 3.10, 2026-10-25): `bin/python/city_building_castles.py` item [2], run log `bin/python/city_building_castles-run.log`, by a search over all city-building castles of width at most 14.
[^exec3]: Verified by execution (Python 3.10, 2026-10-25): `bin/python/city_building_castles.py` item [3], run log `bin/python/city_building_castles-run.log`. For every city-building castle of height at most 4: at most `h + 1` columns of height `h`, and at most `m` columns of height `m` in each run of heights at most `m` that follows a taller column.
[^exec4]: Verified by execution (Python 3.10, 2026-10-25): `bin/python/city_building_castles.py` item [4], run log `bin/python/city_building_castles-run.log`. The cut against a direct search of all city-building castles, by width and block parity: at every width for `h ≤ 4`, and for `w ≤ 22` at `h = 5`; the totals, parity splits, widest widths and width rows for `h ≤ 5` from the cut.
[^exec5]: Verified by execution (Python 3.10, 2026-10-25): `bin/python/city_building_castles.py` item [5], run log `bin/python/city_building_castles-run.log`.
[^exec6]: Verified by execution (Python 3.10, 2026-10-25): `bin/python/city_building_castles.py` item [6], run log `bin/python/city_building_castles-run.log`, for every city-building castle of height at most 4.
