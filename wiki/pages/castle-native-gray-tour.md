---
title: Castle-native Gray tour
category: Concepts
summary: Whether the even-block castles V(w, h) = {c : max c = h, blocks(c) even} admit a Gray tour, a Hamilton path under a set of local moves, worked at (3, 2) and (3, 3). At (3, 2) the proper castles alone have a Hamilton path under single-column ±1 bumps, V(3, 2) has none (two pendant castles) but has one once adjacent swaps are added, and at (3, 3) the three castles of V are joined by no single-column move or adjacent swap. No castle-native Gray code is known; castle-move-graph-zdd extends the search.
tags: [concept, castle, gray-code, hamiltonian-path, generation, algorithm, open-problem]
sources: [project-euler-502-brute-force]
created: 2026-09-20
updated: 2026-10-25
---

# Castle-native Gray tour

[[castle-gray-code](pages/castle-gray-code.md)] walks the whole cube `{1..h}^w` with one column changing by `±1` per step and keeps the even-block castles as it passes them. A tour that visits only the even-block castles would list `A^e(w, h)` castles in `A^e(w, h)` visits, with the sign `(−1)^{blocks}` equal to `+1` throughout. This page asks whether such a tour exists at small sizes; no castle-native Gray code is known. [[castle-move-graph-zdd](pages/castle-move-graph-zdd.md)] carries the search to every `(w, h)` with `w ≥ 3`, `h ≤ 10` and at most 600 castles.

## The object

The even-block castles of width `w` and height `h` are

```
V(w, h)  =  { c ∈ {1..h}^w : max c = h  and  blocks(c) even },        |V(w, h)| = A^e(w, h),
```

with `blocks(c) = c_1 + Σ_{i≥2} max(0, c_i − c_{i−1})` ([[castle-polyomino](pages/castle-polyomino.md)]).[^1] `V` is the intersection of two sets:

- the proper tuples `V_proper(w, h) = { c : max c = h }`, the castles of width `w` and height `h`, `A(w, h) = h^w − (h−1)^w` of them;
- the even tuples `V_even(w, h) = { c ∈ {1..h}^w : blocks(c) even }`, with no condition on the height.

A **castle-native Gray tour** on `V(w, h)` is a Hamilton path in the graph whose vertices are the castles of `V(w, h)` and whose edges join two castles that differ by one move from a chosen set. The moves considered here and on [[castle-move-graph-zdd](pages/castle-move-graph-zdd.md)]:

- a **bump** changes one column by `±1`, the step of the cube Gray code;
- a **swap** exchanges two neighboring columns, `c_i ↔ c_{i+1}`, and keeps the multiset of heights;
- a **double bump** changes one column by `±2`;
- a **far swap** exchanges two columns `c_i ↔ c_j` with `|i − j| ≥ 2`.

A move is an edge only when both of its ends lie in the set being toured.

## The three sets at `(3, 2)`

The eight tuples of `{1, 2}^3`:[^2]

| tuple | blocks | proper? | in `V`? |
|:---|:---:|:---:|:---:|
| (1,1,1) | 1 | no | no |
| (1,1,2) | 2 | yes | yes |
| (1,2,1) | 2 | yes | yes |
| (1,2,2) | 2 | yes | yes |
| (2,1,1) | 2 | yes | yes |
| (2,1,2) | 3 | yes | no |
| (2,2,1) | 2 | yes | yes |
| (2,2,2) | 2 | yes | yes |

So `|V_proper(3, 2)| = 7` and `|V_even(3, 2)| = |V(3, 2)| = 6`. At `h = 2` the one improper tuple `(1, 1, 1)` has one block, so `V_even(3, 2) = V(3, 2)`. At `h = 3` the two sets differ: the tuple `(1, 2, 1)` has 2 blocks and maximum 2, so it lies in `V_even(3, 3)` and not in `V(3, 3)`.

## `V_proper(3, 2)` under bumps

The seven proper tuples have nine bump edges, with degrees `2, 2, 3, 2, 3, 3, 3` in the order of the table, and a Hamilton path:[^2]

```
(1,1,2) → (2,1,2) → (2,1,1) → (2,2,1) → (2,2,2) → (1,2,2) → (1,2,1)
   c_1: 1→2   c_3: 2→1   c_2: 1→2   c_3: 1→2   c_1: 2→1   c_3: 2→1
```

So the height condition alone does not prevent a bump tour at `(3, 2)`.

## `V(3, 2)` under bumps

Label the six castles

```
A = (1,1,2)   B = (1,2,1)   C = (1,2,2)   D = (2,1,1)   E = (2,2,1)   F = (2,2,2)
```

All six have two blocks. The bump edges:[^2]

| edge | column bumped | ends |
|:---|:---|:---|
| A - C | `c_2: 1 → 2` | `(1,1,2) → (1,2,2)` |
| B - C | `c_3: 1 → 2` | `(1,2,1) → (1,2,2)` |
| B - E | `c_1: 1 → 2` | `(1,2,1) → (2,2,1)` |
| C - F | `c_1: 1 → 2` | `(1,2,2) → (2,2,2)` |
| D - E | `c_2: 1 → 2` | `(2,1,1) → (2,2,1)` |
| E - F | `c_3: 1 → 2` | `(2,2,1) → (2,2,2)` |

The degrees are `A = 1, B = 2, C = 3, D = 1, E = 3, F = 2`, so a Hamilton path would have to run from `A` to `D`. Every path from `A` begins `A - C`, and the four continuations fail:

```
A - C - B - E - D          F unvisited
A - C - B - E - F          D unvisited
A - C - F - E - B          D unvisited
A - C - F - E - D          B unvisited
```

So `V(3, 2)` has no Hamilton path under bumps. The castle removed by the parity condition, `(2, 1, 2)` with three blocks, is the one that joined `A` and `D` to the rest in `V_proper(3, 2)`. The area gives the same answer in one step: a bump changes the area by 1, so every bump edge joins `A`, `B`, `D` or `F`, of even area, to `C` or `E`, of odd area, and a path that alternates between a side of four castles and a side of two cannot visit all six ([[castle-move-graph-zdd](pages/castle-move-graph-zdd.md)], Theorem 1).

## `V(3, 2)` under bumps and swaps

Two swaps stay inside `V(3, 2)`:[^2]

| edge | swap | ends |
|:---|:---|:---|
| A - B | `c_2 ↔ c_3` | `(1,1,2) ↔ (1,2,1)` |
| B - D | `c_1 ↔ c_2` | `(1,2,1) ↔ (2,1,1)` |

Every other swap at `(3, 2)` fixes the tuple or leaves `V`. With these two edges there is a Hamilton path,

```
A → B → D → E → F → C
```

by the swaps `A - B` and `B - D` and the bumps `D - E` (`c_2: 1 → 2`), `E - F` (`c_3: 1 → 2`) and `F - C` (`c_1: 2 → 1`).

## `V(3, 3)`

At `(3, 3)` there are `A(3, 3) = 27 − 8 = 19` castles, with 3, 4 or 5 blocks, and `A^e(3, 3) = 3` of them have an even number:[^2]

```
V(3, 3)  =  { (2, 1, 3),  (3, 1, 2),  (3, 2, 3) },       each with 4 blocks.
```

| moves | edges in `V(3, 3)` |
|:---|:---|
| bumps | none |
| swaps | none |
| double bumps | none |
| far swap `c_1 ↔ c_3` | `(2,1,3) - (3,1,2)` only |

`(3, 2, 3)` is fixed by `c_1 ↔ c_3`, and every bump or double bump of it gives a tuple with 3 blocks: `(2,2,3)`, `(3,1,3)`, `(3,3,3)`, `(3,2,2)`, `(1,2,3)` and `(3,2,1)`. So it is isolated under all four kinds of move, and `V(3, 3)` has no Hamilton path under them. The same holds at every odd height: every castle of `V(3, h)` has a strict valley in the middle, and every move between two of them keeps the parity of the middle column, which separates `(3, 2, 3)` from the other two here ([[castle-move-graph-zdd](pages/castle-move-graph-zdd.md)], Theorem 3).

## Summary of the small cases

- `V_proper(3, 2)` under bumps: a Hamilton path exists.
- `V(3, 2)` under bumps: no Hamilton path, because of the two pendant castles `(1, 1, 2)` and `(2, 1, 1)`. Under bumps and swaps: a Hamilton path exists.
- `V(3, 3)` under all four kinds of move: no Hamilton path; the only edge is `(2,1,3) - (3,1,2)`.

[[castle-move-graph-zdd](pages/castle-move-graph-zdd.md)] finds that bumps and swaps give Hamilton paths at `(3, 2)`, `(4, 2)` and `(3, 4)` and not at `(5, 2)`, `(6, 2)` or `(4, 3)`; adding far swaps repairs `(5, 2)` and `(6, 2)`, and adding double bumps repairs `(4, 3)`. It proves that bumps alone give no Hamilton path at any width `w ≥ 3`, that at height 2 bumps and swaps give none from width 5 on, and that at width 3 and every odd height the four kinds of move together give none.

## Entities & Concepts

- [[castle-move-graph-zdd](pages/castle-move-graph-zdd.md)] - the Hamilton-path search over the four kinds of move up to `(6, 2)`, `(4, 3)` and `(3, 4)`, with exact path counts where they are computable.
- [[castle-gray-code](pages/castle-gray-code.md)] - the Gray code on the whole cube `{1..h}^w`, from which `V(w, h)` is filtered.
- [[project-euler-502-brute-force](pages/project-euler-502-brute-force.md)] - the block-count formula used for every table on this page.
- [[castle-counting-formula](pages/castle-counting-formula.md)] - `A^e(w, h)`, the number of castles a tour on `V(w, h)` would visit.
- [[castle-sign](pages/castle-sign.md)] - the sign `(−1)^{blocks}`, constant on `V(w, h)`.

## Related Concepts

- [[castle-samplers](pages/castle-samplers.md)] - the same fragmentation seen by Markov chains: `V(8, 4)` has 191 components under bumps, so the chains there run on the whole cube and keep the castles of `V` as they pass them.
- [[castle-compression](pages/castle-compression.md)] - delta codes, which a castle-native tour would give one move per castle.
- [[castle-bdd-zdd](pages/castle-bdd-zdd.md)] - `V(w, h)` as a decision diagram, which ranks and unranks its castles without a walking order.

## Footnotes

[^1]: [[project-euler-502-brute-force](pages/project-euler-502-brute-force.md)] §"Column-height encoding" L18-24 - "column heights c_1, …, c_w ∈ {1, …, h} with max c = h", "#blocks = ∑_{r=1}^{h} #{runs of columns with c_i ≥ r} = c_1 + ∑_{i=2}^{w} max(0, c_i − c_{i−1})".
[^2]: Verified by execution (Python 3.11, 2026-10-16): the block counts of all eight tuples of `{1, 2}^3`; the nine bump edges of `V_proper(3, 2)`, their degrees and the Hamilton path; the six bump edges and two swap edges of `V(3, 2)` and the path `A → B → D → E → F → C`; the 19 castles of width 3 and height 3 (block counts 3, 4, 5), the three of `V(3, 3)`, and its edges under bumps, swaps, double bumps and far swaps; `(1, 2, 1)` has 2 blocks.
