---
title: Castle move-graph ZDD
category: Concepts
summary: Hamilton paths in the castle move graph G(w, h) on the valid castles V(w, h), for the castle-native Gray tour question, with Knuth's SimPath methodology (TAOCP §7.1.4 exercises 225-228) as the route to larger sizes; no ZDD is built here. A search over four move sets (M1, M6, M7, Mnon) at (w, h) up to (6, 2), (4, 3) and (3, 4): M1 alone never gives a Hamilton path in the sweep; M1 ∪ M6 works at (3, 2), (4, 2) and (3, 4) and fails at (5, 2), (6, 2) and (4, 3); adding Mnon gives Hamilton paths at (5, 2) and (6, 2) but not (4, 3), which needs M7; V(3, 3) is three castles that no local move set tried connects.
tags: [concept, castle, zdd, simpath, hamiltonian-path, move-graph, generation, open-problem]
sources: [castle-native-gray-tour, castle-bdd-zdd, project-euler-502-brute-force]
created: 2026-09-20
updated: 2026-10-02
---

# Castle move-graph ZDD

This page extends the castle-native Gray tour question of [[castle-native-gray-tour](pages/castle-native-gray-tour.md)] from `(3, 2)` and `(3, 3)` to a Hamilton-path search over four move sets at `(w, h)` up to `(6, 2)`, `(4, 3)` and `(3, 4)`, and outlines how Knuth's ZDD-of-simple-paths methodology (TAOCP §7.1.4 exercises 225-228) would settle larger cases. It builds no ZDD and proves no general existence result. The companion [[castle-bdd-zdd](pages/castle-bdd-zdd.md)] treats `V` itself as a ZDD; this page treats Hamilton paths in the move graph on `V`.

## The move graph `G(w, h)` and four move sets

`G(w, h) = (V(w, h), M)` has the valid castles of [[castle-native-gray-tour](pages/castle-native-gray-tour.md)] as vertices and single-step moves in a chosen set `M` as edges. Four move sets, each restricted to edges whose endpoints both lie in `V`:

- **M1** — single-column `±1` bump.
- **M6** — adjacent transposition `c_i ↔ c_{i+1}`.
- **M7** — single-column `±2` bump.
- **Mnon** — non-adjacent transposition `c_i ↔ c_j` with `|i − j| ≥ 2`.

M1 and M6 were defined on [[castle-native-gray-tour](pages/castle-native-gray-tour.md)]; M7 and Mnon are two further single-step moves.

## Hamilton-path sweep

Hamilton-path search across small `(w, h)` under M1 and four combined move sets:[^1]

| `(w, h)` | `|V|` | M1 | M1 ∪ M6 | M1 ∪ M6 ∪ M7 | M1 ∪ M6 ∪ Mnon | all four |
|:---------|------:|:--:|:-------:|:-----------:|:--------------:|:--------:|
| (3, 2)   |     6 | -  |    Y    |      Y      |        Y       |    Y     |
| (4, 2)   |    10 | -  |    Y    |      Y      |        Y       |    Y     |
| (5, 2)   |    16 | -  |    -    |      -      |        Y       |    Y     |
| (6, 2)   |    28 | -  |    -    |      -      |        Y       |    Y     |
| (3, 3)   |     3 | -  |    -    |      -      |        -       |    -     |
| (4, 3)   |    21 | -  |    -    |      Y      |        -       |    Y     |
| (3, 4)   |    31 | -  |    Y    |      Y      |        Y       |    Y     |

"Y" = Hamilton path exists; "-" = none exists under that move set. Adding moves only adds edges, so a "Y" carries over to every larger move set. The number of Hamilton paths (undirected):

| `(w, h)` | M1 ∪ M6 count | M1 ∪ M6 ∪ Mnon count |
|:---------|--------------:|---------------------:|
| (3, 2)   |            10 |                   34 |
| (4, 2)   |            44 |                1,004 |
| (5, 2)   |             0 |               49,508 |
| (6, 2)   |             0 |           ≥ 97,185 |
| (4, 3)   |             0 |                    0 |
| (3, 4)   |          ≥ 52 |              ≥ 2,040 |

The `≥` entries are the counts a DFS reached before it was stopped; the exact values are what a SimPath-style ZDD build would settle. `(4, 3)` under M1 ∪ M6 ∪ Mnon has zero Hamilton paths, verified exhaustively.

## What the data show

- **M1 alone never admits a Hamilton path** in the sweep. A single-column `±1` bump changes the block count by at most one, so an M1 edge inside `V` keeps the block count fixed, and the M1 graph splits into classes of equal block count (at `(3, 4)` it has four components).
- **M1 ∪ M6 works at `(3, 2)` and `(4, 2)` and fails at `(5, 2)` and `(6, 2)`.** At `h = 2` an adjacent transposition also changes the block count by at most one, so M1 ∪ M6 edges keep it fixed too. Through `w = 4` every castle in `V(w, 2)` has two blocks; from `w = 5` on `V` also holds four-block castles, and the M1 ∪ M6 graph is disconnected (at `(5, 2)` the castle `(2,1,2,1,2)` has no neighbour at all).
- **Adding non-adjacent transpositions** (M1 ∪ M6 ∪ Mnon) connects the `(w, 2)` graphs again and gives Hamilton paths at `w = 5, 6`: 49,508 at `(5, 2)` and at least 97,185 at `(6, 2)`.
- **`(4, 3)` needs M7.** Neither M1 ∪ M6 nor M1 ∪ M6 ∪ Mnon has a Hamilton path there; adding M7 (single-column `±2`) gives one. The enlargements that work for `(w, 2)` and for `(4, 3)` differ, and among those tested only the union of all four works in both.
- **`(3, 3)` is isolated.** `V(3, 3) = {(2,1,3), (3,1,2), (3,2,3)}`. From `(3, 2, 3)`, every single-column `±1` or `±2` bump and every adjacent transposition leaves `V`, and the swap `c_1 ↔ c_3` fixes it; among the permutations of `(2, 1, 3)`, only `(2, 1, 3)` and `(3, 1, 2)` lie in `V`.[^2]

Different `(w, h)` need different enlargements of M1 ∪ M6; which enlargement works for which `(w, h)` is open.

## What Knuth's SimPath methodology adds

TAOCP §7.1.4 pp. 254-256, exercises 225-228, gives four related constructions on an undirected graph:[^3]

- **Exercise 225: SimPath.** ZDD of all simple paths between a fixed source `s` and sink `t`. Frontier-based construction; polynomial in the ZDD size, not in the path count. On the 8x8 grid `P_8 ⊡ P_8` this represents all `789,360,053,252` corner-to-corner paths in a `33,580`-node ZDD (Knuth p. 254).
- **Exercise 226: cycles.** ZDD of all simple cycles of a graph. On `P_8 ⊡ P_8` this is `603,841,648,931` cycles in a `22,275`-node ZDD.
- **Exercise 227: Hamilton paths.** ZDD of just the Hamilton paths, extractable by reading off the longest paths from a SimPath ZDD (Bryant Continental U.S. example: `2,707,075` Hamilton paths).
- **Exercise 228: all-source Hamilton paths.** A single `28,808`-node ZDD characterising all Hamilton paths from a fixed source `s` to *any* other vertex.

Applied to `G(w, h)`:

- **Existence.** For larger `(w, h)`, a SimPath build gives the Hamilton-path ZDD, or shows it is empty, when the frontier stays small enough to fit.
- **Counts.** The Hamilton-path count under a move set `M` is a linear-time count over that ZDD, which would replace the `≥` entries above with exact numbers.
- **Comparison across move sets.** With ZDDs for `G(w, h)` under `M1 ∪ M6` and `M1 ∪ M6 ∪ Mnon`, the synthesis operations (`∧, ∨, ⊕`, p. 251) separate the Hamilton paths that use only M1 ∪ M6 edges from those that need an Mnon edge.
- **Loopless successor.** A Hamilton-path ZDD lists its paths in the ZDD's order; whether a castle-native tour admits a loopless successor like the loopless Gray algorithm of [[castle-gray-code](pages/castle-gray-code.md)] is a separate question.

## Not covered here

- **The construction itself.** SimPath is described in exercises 225-227 with hints; §7.1.4 does not present it as a numbered Algorithm. No implementation is given here; CUDD, Sylvan and SAPPOROBDD provide the ZDD primitives.
- **The variable ordering choice for SimPath on `G(w, h)`.** Frontier-based ZDD constructions are sensitive to variable ordering; the natural castle orderings (by column, by castle index in some canonical enumeration) each give a different ZDD size, and picking the best is a study of its own.

## Entities & Concepts

- [[castle-native-gray-tour](pages/castle-native-gray-tour.md)] - the `(3, 2)` and `(3, 3)` cases the sweep above extends.
- [[castle-bdd-zdd](pages/castle-bdd-zdd.md)] - the sibling page treating `V(w, h)` itself as a BDD / ZDD; this page treats the *move graph* on `V(w, h)`.
- [[project-euler-502-brute-force](pages/project-euler-502-brute-force.md)] - the column-height block-count formula used to compute `V(w, h)` for each case in the sweep.
- [[castle-count-algorithms](pages/castle-count-algorithms.md)] - `|V(w, h)| = F(w, h)`; the values 6, 10, 16, 28, 3, 21, 31 in the `|V|` column agree with `F(w, h) = (h^w - (h-1)^w - P(h-1, w) + P(h-2, w)) / 2` ([[castle-counting-formula](pages/castle-counting-formula.md)]).

## Related Concepts

- [[castle-gray-code](pages/castle-gray-code.md)] - the Gray code on the full cube `{1..h}^w`; this page is about generation restricted to `V(w, h)` alone.
- [[castle-classification](pages/castle-classification.md)] - each further restriction axis (convex, unimodal, tower-spacing) defines a sub-graph of `G(w, h)`, each with its own Hamilton-path question.
- [[castle-strip](pages/castle-strip.md)] - the `h`-state transfer matrix on column heights, the base of the DFA behind [[castle-bdd-zdd](pages/castle-bdd-zdd.md)]'s BDD representation of `V`.

## Footnotes

[^1]: Sweep computed on the enumerated `V(w, h)` and move-set edge lists on 2026-09-20 and re-run on 2026-09-28: for `|V| ≤ 21` by exhaustive subset dynamic programming over (visited set, endpoint), which also gives the exact counts; the "-" cells at `(6, 2)` are certified by the graph being disconnected; the "Y" cells at `(6, 2)` and `(3, 4)` by an explicit Hamilton path found by depth-first search. The `≥` counts are lower bounds from a stopped search. The small cases agree with [[castle-native-gray-tour](pages/castle-native-gray-tour.md)].
[^2]: The three castles of `V(3, 3)` all have `blocks = 4`. From `(3, 2, 3)`: every single-column `±1` bump gives an odd-block tuple (`(2,2,3), (3,1,3), (3,3,3), (3,2,2)` all have blocks 3); every single-column `±2` bump either produces an out-of-range column or an odd-block tuple; every adjacent transposition `c_2 ↔ c_3` or `c_1 ↔ c_2` gives an odd-block tuple; the non-adjacent transposition `c_1 ↔ c_3` fixes `(3, 2, 3)` because it is symmetric under that swap. So no local move connects `(3, 2, 3)` to `(2, 1, 3)` or `(3, 1, 2)`; a Hamilton path on `V(3, 3)` needs a two-column move, such as `(3, 2, 3) → (3, 1, 2)` (both `c_2` and `c_3` down by one).
[^3]: Knuth, TAOCP Vol. 4A §7.1.4 pp. 254-256, exercises 225-228. Exercise 225 describes the SimPath algorithm as a frontier-based ZDD construction for the family of simple paths between two vertices of an undirected graph; the "frontier" at each step of the construction is the small set of vertices with unresolved connection status. Exercise 226 extends the construction to cycles; exercise 227 to Hamilton paths as the longest simple paths; exercise 228 constructs a single ZDD parameterised by the destination. Knuth's scale demonstrations (Bryant Continental U.S. and the 8x8 grid) show that the ZDD size can be many orders of magnitude smaller than the path count it represents, which is what makes the construction extend to graphs where direct DFS enumeration is infeasible.
