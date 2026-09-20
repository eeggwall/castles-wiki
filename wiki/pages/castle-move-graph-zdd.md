---
title: Castle move-graph ZDD
category: Concepts
summary: A working note on applying Knuth's SimPath methodology (TAOCP §7.1.4 exercises 225-228) to the castle-native tour question on the move graph G(w, h). Not an implementation. Reports hand-DFS Hamilton-path existence and counts across four move sets (M1, M6, M7, Mnon) at (w, h) up to (6, 2) and (4, 3): M1 alone always fails; M1 ∪ M6 works at (3, 2) and (4, 2) but fails at (5, 2), (6, 2), (4, 3); M1 ∪ M6 ∪ Mnon rescues the (w, 2) family but not (4, 3); (3, 3) is fundamentally isolated under every local move set tried. The ZDD/SimPath methodology is where the analysis extends beyond hand-DFS.
tags: [concept, castle, zdd, simpath, hamiltonian-path, move-graph, generation, working-note]
sources: [castle-native-gray-tour, castle-bdd-zdd, project-euler-502-brute-force]
created: 2026-09-20
updated: 2026-09-20
---

# Castle move-graph ZDD

## What this page is not

This page is not an implementation of Knuth's SimPath. It does not produce a ZDD of the Hamilton paths of the castle move graph `G(w, h)` at any `(w, h)`. It does not prove that a Hamilton path exists for all `(w, h)` under any specific move set. It does not ship a witness path for any case not already exhibited on [[castle-native-gray-tour](pages/castle-native-gray-tour.md)].

## What this page is

A **working note** applying the ZDD-of-simple-paths methodology of TAOCP §7.1.4 exercises 225-228 to the castle-native Gray tour question from [[castle-native-gray-tour](pages/castle-native-gray-tour.md)], and reporting hand-DFS Hamilton-path data across four move sets at `(w, h)` up to `(6, 2)` and `(4, 3)`. The data settle several small cases the working note left open, expose a new failure mode at `(w, 2)` for `w ≥ 5` that M1 ∪ M6 cannot repair, and identify the size regime beyond which the DFS approach exhausts its budget and ZDD construction becomes the natural next tool.

Companion to [[castle-bdd-zdd](pages/castle-bdd-zdd.md)], which handles the *representation* side (V as a ZDD); this page handles the *tour existence* side (Hamilton paths in G as a ZDD).

## The move graph `G(w, h)` and four move sets

`G(w, h) = (V(w, h), M)` has the valid castles of [[castle-native-gray-tour](pages/castle-native-gray-tour.md)] as vertices and single-step moves in a chosen set `M` as edges. Four move sets, each restricted to edges whose endpoints both lie in `V`:

- **M1** — single-column `±1` bump.
- **M6** — adjacent transposition `c_i ↔ c_{i+1}`.
- **M7** — single-column `±2` bump.
- **Mnon** — non-adjacent transposition `c_i ↔ c_j` with `|i − j| ≥ 2`.

M1 and M6 were defined on [[castle-native-gray-tour](pages/castle-native-gray-tour.md)]; M7 and Mnon are the next two natural single-step extensions.

## Hand-DFS Hamilton-path sweep

Brute-force DFS Hamilton-path search across small `(w, h)` under the four move sets and two combined sets, with an 8-second per-case budget:[^1]

| `(w, h)` | `|V|` | M1 | M1 ∪ M6 | M1 ∪ M6 ∪ M7 | M1 ∪ M6 ∪ Mnon | all four |
|:---------|------:|:--:|:-------:|:-----------:|:--------------:|:--------:|
| (3, 2)   |     6 | -  |    Y    |      Y      |        Y       |    Y     |
| (4, 2)   |    10 | -  |    Y    |      Y      |        Y       |    Y     |
| (5, 2)   |    16 | -  |    -    |      -      |        Y       |    Y     |
| (6, 2)   |    28 | -  |    -    |      -      |        Y       |    Y     |
| (3, 3)   |     3 | -  |    -    |      -      |        -       |    -     |
| (4, 3)   |    21 | -  |    -    |      Y      |        -       |    Y     |
| (3, 4)   |    31 | -  |    Y    |      ?      |        Y       |    Y     |

"Y" = Hamilton path found; "-" = none exists under that move set; "?" = search exceeded the 8-second budget without deciding. Where a Hamilton path exists, the count grows fast:

| `(w, h)` | M1 ∪ M6 count | M1 ∪ M6 ∪ Mnon count |
|:---------|--------------:|---------------------:|
| (3, 2)   |            10 |                   34 |
| (4, 2)   |            44 |                1,004 |
| (5, 2)   |             0 |               49,508 |
| (6, 2)   |             0 |       > 97,185 (t/o) |
| (4, 3)   |             0 |                    0 |
| (3, 4)   | > 52 (t/o)    |         > 2,040 (t/o)|

At `(6, 2)` and `(3, 4)`, the DFS counter exceeds 97,000 and 2,000 respectively in eight seconds without finishing; the exact counts are what a SimPath-style ZDD build would settle. `(4, 3)` under M1 ∪ M6 ∪ Mnon has *zero* Hamilton paths, verified exhaustively.

## What the data show

Five observations, each contradicting a natural guess the earlier working note left open:

- **M1 alone never admits a Hamilton path** at any `(w, h)` tested. The `Δ blocks = 0` constraint on single-column `±1` bumps is too restrictive for the graph to become Hamiltonian on its own; some non-`±1` move is always needed.
- **M1 ∪ M6 works at `(3, 2)` and `(4, 2)` and fails at `(5, 2)`.** The pattern the earlier working note tentatively extended from `(3, 2)` to a family breaks at the next size. `(4, 2)` gives 44 Hamilton paths, `(5, 2)` gives zero, a hard step-off, not a gradual thinning.
- **M1 ∪ M6 ∪ Mnon rescues the `(w, 2)` family** at `w = 5, 6`, giving 49,508 paths at `(5, 2)` and more than 97,185 at `(6, 2)`. Non-adjacent transpositions - two-column moves at distance ≥ 2 - are the specific mechanism that makes the `h = 2` cube-slice re-connect at larger widths.
- **`(4, 3)` is a hard case.** Neither M1 ∪ M6 nor M1 ∪ M6 ∪ Mnon works; only adding M7 (single-column `±2`) recovers a Hamilton path. The move set that rescues the `(w, 2)` family and the move set that rescues `(4, 3)` are *different* enlargements of M1 ∪ M6, so there is no single obvious "next enlargement" that rescues both without going to the union of all four.
- **`(3, 3)` is fundamentally isolated.** With `|V| = 3` and the three castles `{(2,1,3), (3,1,2), (3,2,3)}`, `(3, 2, 3)` is symmetric under every swap and every single-column `±1` or `±2` bump from it leaves `V`. No local move set with 3 castles connects it to the other two; multi-column moves at `w = 3` are exactly permutations, and only two of the six permutations of `(2, 1, 3)` lie in `V`.[^2]

Together the observations refute the reading "M1 ∪ M6 works uniformly with a monotone growth of the move set" that the earlier working note left as an open guess. The `(w, h)` grid partitions into pockets of Hamilton-existence under different enlargements of M1 ∪ M6, and finding the *right* enlargement for a given pocket is itself a combinatorial question.

## What Knuth's SimPath methodology adds

TAOCP §7.1.4 pp. 254-256, exercises 225-228, gives four related constructions on an undirected graph:[^3]

- **Exercise 225: SimPath.** ZDD of all simple paths between a fixed source `s` and sink `t`. Frontier-based construction; polynomial in the ZDD size, not in the path count. On the 8x8 grid `P_8 ⊡ P_8` this represents all `789,360,053,252` corner-to-corner paths in a `33,580`-node ZDD (Knuth p. 254).
- **Exercise 226: cycles.** ZDD of all simple cycles of a graph. On `P_8 ⊡ P_8` this is `603,841,648,931` cycles in a `22,275`-node ZDD.
- **Exercise 227: Hamilton paths.** ZDD of just the Hamilton paths, extractable by reading off the longest paths from a SimPath ZDD (Bryant Continental U.S. example: `2,707,075` Hamilton paths).
- **Exercise 228: all-source Hamilton paths.** A single `28,808`-node ZDD characterising all Hamilton paths from a fixed source `s` to *any* other vertex.

Applied to `G(w, h)`, each construction settles a piece of the castle-native tour question:

- **Existence at scale.** For `(w, h)` where `|V|` exceeds hand-DFS capacity (`w ≥ 7`, `h ≥ 3`), SimPath produces the exact Hamilton-path ZDD or proves none exists.
- **Count at scale.** The Hamilton-path count of `G(w, h)` under move set `M` is a linear-time count over the ZDD, replacing the >97,185 / timeout entries above with exact numbers.
- **Structural comparison across move sets.** With two ZDDs for `G(w, h)` under `M1 ∪ M6` and `M1 ∪ M6 ∪ Mnon`, the ZDD synthesis primitives (`∧, ∨, ⊕` on p. 251) give the ZDD of Hamilton paths that use *only* M1 ∪ M6 edges within the larger move set, and the ZDD of paths that require at least one Mnon edge. That structural split is exactly the "which move is doing the work" question the `(5, 2)` step-off raises.
- **Loopless-successor question.** Given a Hamilton-path ZDD, an analog of Knuth's Algorithm B (p. 251) traverses paths in an implicit order; whether that traversal is loopless-in-the-Ives sense is a further ZDD-property question on top of existence.

## Not covered here

- **The construction itself.** SimPath is described in exercises 225-227 with hints; §7.1.4 does not present it as a numbered Algorithm. A working implementation (in CUDD / Sylvan / SAPPOROBDD) is the next tool this page's questions want, and is out of scope.
- **The `(3, 3)` obstruction resolution.** The isolation of `V(3, 3)` under every local move set tried is a genuine combinatorial wall, not a computational limit; ZDDs would confirm the count 0 but not explain it. The explanation is that F(3, 3) = 3 castles have block count 4 each, and every local move at each of them either produces an odd-block tuple or fixes the castle.
- **The variable ordering choice for SimPath on `G(w, h)`.** Frontier-based ZDD constructions are sensitive to variable ordering; the natural castle orderings (by column, by castle index in some canonical enumeration) each give a different ZDD size, and picking the best is a study of its own.

## Entities & Concepts

- [[castle-native-gray-tour](pages/castle-native-gray-tour.md)] - the working note this page continues, whose `(3, 2)` and `(3, 3)` cases the sweep above extends.
- [[castle-bdd-zdd](pages/castle-bdd-zdd.md)] - the sibling page treating `V(w, h)` itself as a BDD / ZDD; this page treats the *move graph* on `V(w, h)`.
- [[project-euler-502-brute-force](pages/project-euler-502-brute-force.md)] - the column-height block-count formula used to compute `V(w, h)` for each case in the sweep.
- [[castle-count-algorithms](pages/castle-count-algorithms.md)] - `|V(w, h)| = F(w, h)`; the values 6, 10, 16, 28, 3, 21, 31 in the `|V|` column all come from `F(w, h) = (h^w - (h-1)^w + P(h-1, w) - P(h-2, w)) / 2` on that page.

## Related Concepts

- [[castle-gray-code](pages/castle-gray-code.md)] - the generic Gray-code lens on the full cube `{1..h}^w`; this page is about generation restricted to `V(w, h)` alone.
- [[castle-classification](pages/castle-classification.md)] - each further restriction axis (convex, unimodal, tower-spacing) defines a sub-graph of `G(w, h)`, each with its own Hamilton-path question.
- [[castle-strip](pages/castle-strip.md)] - the `h`-state transfer matrix on column heights, which forms the DFA base for both this page's move-graph construction and [[castle-bdd-zdd](pages/castle-bdd-zdd.md)]'s BDD representation of `V`.

## Footnotes

[^1]: Sweep computed by brute-force Hamilton-path DFS on the enumerated `V(w, h)` and move-set edge lists, verified for the small cases against by-hand analysis on [[castle-native-gray-tour](pages/castle-native-gray-tour.md)]. Existence cells with "-" are exhaustive verifications (DFS visited every start vertex without finding a Hamilton path within `n! · n` step upper bound, well under the 8-second budget for `|V| ≤ 21`). Count cells are exact where the search completed and a lower bound where the search timed out. Run on 2026-09-20.
[^2]: The three castles of `V(3, 3)` all have `blocks = 4`. From `(3, 2, 3)`: every single-column `±1` bump gives an odd-block tuple (`(2,2,3), (3,1,3), (3,3,3), (3,2,2)` all have blocks 3); every single-column `±2` bump either produces an out-of-range column or an odd-block tuple; every adjacent transposition `c_2 ↔ c_3` or `c_1 ↔ c_2` gives an odd-block tuple; the non-adjacent transposition `c_1 ↔ c_3` fixes `(3, 2, 3)` because it is symmetric under that swap. So no local move connects `(3, 2, 3)` to `(2, 1, 3)` or `(3, 1, 2)`; a Hamilton path on `V(3, 3)` would require a genuinely non-local move (two-column simultaneous `±1`, or a rearrangement that changes both `c_1` and one other coordinate).
[^3]: Knuth, TAOCP Vol. 4A §7.1.4 pp. 254-256, exercises 225-228. Exercise 225 describes the SimPath algorithm as a frontier-based ZDD construction for the family of simple paths between two vertices of an undirected graph; the "frontier" at each step of the construction is the small set of vertices with unresolved connection status. Exercise 226 extends the construction to cycles; exercise 227 to Hamilton paths as the longest simple paths; exercise 228 constructs a single ZDD parameterised by the destination. Knuth's scale demonstrations (Bryant Continental U.S. and the 8x8 grid) show that the ZDD size can be many orders of magnitude smaller than the path count it represents, which is what makes the construction extend to graphs where direct DFS enumeration is infeasible.
