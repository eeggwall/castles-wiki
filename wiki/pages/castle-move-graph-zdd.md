---
title: Castle move graph and Hamilton paths
category: Concepts
summary: Hamilton paths in the move graph on the even-block castles V(w, h), the castle-native Gray tour question, for (w, h) up to (6, 2), (4, 3) and (3, 4) under bumps (one column ±1), swaps (neighboring columns exchanged), double bumps (±2) and far swaps. Bumps alone never give a Hamilton path in this range; bumps and swaps give one at (3, 2), (4, 2) and (3, 4) and not at (5, 2), (6, 2) or (4, 3); adding far swaps repairs (5, 2) and (6, 2), and adding double bumps repairs (4, 3). Exact path counts are given where the subset dynamic program finishes.
tags: [concept, castle, hamiltonian-path, move-graph, generation, open-problem]
sources: [project-euler-502-brute-force]
created: 2026-09-20
updated: 2026-10-16
---

# Castle move graph and Hamilton paths

[[castle-native-gray-tour](pages/castle-native-gray-tour.md)] asks whether the even-block castles `V(w, h)` admit a Gray tour, and works the cases `(3, 2)` and `(3, 3)`. This page searches the same question at `(w, h)` up to `(6, 2)`, `(4, 3)` and `(3, 4)`, and counts the Hamilton paths where the count is computable. It proves no general result.

## The move graph

The move graph on `V(w, h)` has the castles of `V(w, h)` as vertices, `A^e(w, h)` of them, and an edge between two castles that differ by one move from a chosen set, both ends lying in `V(w, h)`. The four kinds of move, defined on [[castle-native-gray-tour](pages/castle-native-gray-tour.md)]:

- a **bump**: one column changes by `±1`;
- a **swap**: two neighboring columns are exchanged, `c_i ↔ c_{i+1}`;
- a **double bump**: one column changes by `±2`;
- a **far swap**: two columns `c_i ↔ c_j` with `|i − j| ≥ 2` are exchanged.

## Existence

"Y" means a Hamilton path exists and "-" that none exists:[^1]

| `(w, h)` | `\|V\|` | bumps | bumps + swaps | + double bumps | + far swaps | all four |
|:---|---:|:---:|:---:|:---:|:---:|:---:|
| (3, 2) | 6 | - | Y | Y | Y | Y |
| (4, 2) | 10 | - | Y | Y | Y | Y |
| (5, 2) | 16 | - | - | - | Y | Y |
| (6, 2) | 28 | - | - | - | Y | Y |
| (3, 3) | 3 | - | - | - | - | - |
| (4, 3) | 21 | - | - | Y | - | Y |
| (3, 4) | 31 | - | Y | Y | Y | Y |

The columns "+ double bumps" and "+ far swaps" add that kind of move to bumps and swaps. Adding moves only adds edges, so a "Y" holds for every larger set of moves. The values `|V| = A^e(w, h)` agree with the [[castle-counting-formula](pages/castle-counting-formula.md)].

## Counts

The number of Hamilton paths, each path counted once with either direction:[^1]

| `(w, h)` | bumps + swaps | + double bumps | + far swaps | all four |
|:---|---:|---:|---:|---:|
| (3, 2) | 10 | 10 | 34 | 34 |
| (4, 2) | 44 | 44 | 1,004 | 1,004 |
| (5, 2) | 0 | 0 | 49,508 | 49,508 |
| (4, 3) | 0 | 704 | 0 | 71,509 |
| (3, 4) | 2,912 | at least 2,912 | at least 2,912 | at least 2,912 |
| (6, 2) | 0 | 0 | at least 1 | at least 1 |

The "at least" entries are not counted: the dynamic program over (visited set, last castle) outgrows memory at `(6, 2)` and at `(3, 4)` with far swaps. A set of moves that contains bumps and swaps has at least the 2,912 paths of bumps and swaps at `(3, 4)`, and at `(6, 2)` a depth-first search finds a path.

## What the data show

- **Bumps alone never give a Hamilton path in this range.** A bump changes the block count by at most 1 ([[castle-gray-code](pages/castle-gray-code.md)], the Lemma in the section *Algorithm G: the Gray tour*), so a bump between two castles of `V` keeps the block count, and the bump graph falls apart by block count; at `(3, 4)` it has four components.
- **Bumps and swaps work at `(3, 2)` and `(4, 2)` and fail at `(5, 2)` and `(6, 2)`.** At height 2 a swap also changes the block count by at most 1, so these edges keep it too. Up to width 4 every castle of `V(w, 2)` has two blocks; from width 5 on, `V(w, 2)` also holds castles with four blocks, and the graph is disconnected: at `(5, 2)` the castle `(2, 1, 2, 1, 2)` has no neighbor under bumps or swaps.
- **Far swaps repair `(5, 2)` and `(6, 2)`**, with 49,508 Hamilton paths at `(5, 2)`.
- **Double bumps repair `(4, 3)`**, with 704 Hamilton paths; far swaps do not. Of the sets tried, only the set of all four kinds of move gives Hamilton paths at both `(6, 2)` and `(4, 3)`.
- **`V(3, 3)` has no Hamilton path under any of the four.** `V(3, 3) = {(2,1,3), (3,1,2), (3,2,3)}`, and `(3, 2, 3)` is isolated: each of its bumps and double bumps has 3 blocks, each swap of it has 3 blocks, and the far swap `c_1 ↔ c_3` fixes it. A Hamilton path on `V(3, 3)` needs a move of two columns at once, such as `(3, 2, 3) → (3, 1, 2)`.[^2]

## Entities & Concepts

- [[castle-native-gray-tour](pages/castle-native-gray-tour.md)] - the question, the four kinds of move, and the cases `(3, 2)` and `(3, 3)` worked by hand.
- [[castle-gray-code](pages/castle-gray-code.md)] - the Gray code on the whole cube `{1..h}^w`, and the Lemma that a bump changes the block count by at most 1.
- [[project-euler-502-brute-force](pages/project-euler-502-brute-force.md)] - the block-count formula used to list `V(w, h)`.
- [[castle-counting-formula](pages/castle-counting-formula.md)] - `A^e(w, h)`, the column `|V|` of the existence table.

## Related Concepts

- [[castle-samplers](pages/castle-samplers.md)] - the components of `V(w, h)` under bumps and under single-column redraws, up to `(8, 4)`.
- [[castle-bdd-zdd](pages/castle-bdd-zdd.md)] - `V(w, h)` itself as a decision diagram.

## Footnotes

[^1]: Verified by execution (Python 3.11, 2026-10-16), on `V(w, h)` listed with the block-count formula and the edges of each set of moves: Hamilton paths counted by a dynamic program over (visited set, last castle) for `|V| ≤ 21`, which also settles every "-" in those rows; the bump, bump-and-swap and bump-swap-and-double-bump graphs at `(6, 2)` are disconnected, and the bump graph at `(3, 4)` is disconnected; the other cells of `(6, 2)` and `(3, 4)` by a path found by depth-first search; the count 2,912 at `(3, 4)` by the same dynamic program, which finishes there; at height 2 a swap changes the block count by at most 1 for every castle of width at most 10 (it fails at height 3).
[^2]: The three castles of `V(3, 3)` have 4 blocks. From `(3, 2, 3)`, the bumps give `(2,2,3)`, `(3,1,3)`, `(3,3,3)`, `(3,2,2)`, the double bumps `(1,2,3)`, `(3,2,1)`, and the swaps `(2,3,3)`, `(3,3,2)`, all with 3 blocks; the far swap `c_1 ↔ c_3` fixes `(3, 2, 3)`. Among the rearrangements of `(2, 1, 3)`, only `(2, 1, 3)` and `(3, 1, 2)` lie in `V(3, 3)`.
