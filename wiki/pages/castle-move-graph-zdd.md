---
title: Castle move graph and Hamilton paths
category: Concepts
summary: Hamilton paths, the castle-native Gray tours, in the move graph on the even-block castles V(w, h) under bumps (one column ±1), swaps (neighboring columns exchanged), double bumps (±2) and far swaps, for every (w, h) with w ≥ 3, h ≤ 10 and at most 600 castles. Proved for every size: bumps alone never give a Hamilton path, since a bump keeps the block count between castles of V and flips the parity of the area; at height 2 bumps and swaps give none from width 5 on, the components being the block-count classes of C(w + 1, 2k) castles with k runs of 2s; and at width 3 and odd height h = 2k + 1 the four moves together give none, since every castle is a strict valley and every move keeps the parity of the middle column, with A^e(3, 2k + 1) = k(2k + 1). Computed: the four moves together give a Hamilton path in every other cell; far swaps are needed at height 2 from width 5 and at (5, 4), and double bumps at width 4 and odd heights, where at (4, 3) an interior column of height 1 splits the castles; at width 3 and heights 6, 8 and 10 bumps and swaps fail the degree conditions of a Hamilton path. Exact counts of Hamilton paths and Hamilton cycles at (3, 2) to (6, 2), (3, 3), (4, 3) and (3, 4), by a ZDD built with Knuth's frontier method (TAOCP §7.1.4, exercises 225-228) and by inclusion-exclusion: up to 1,983,077,444 paths at (6, 2) and 47,449,883,300,690 at (3, 4), where bumps and swaps give 2,912 paths and no cycle.
tags: [concept, castle, hamiltonian-path, hamiltonian-cycle, move-graph, zdd, generation, open-problem]
sources: [project-euler-502-brute-force]
created: 2026-09-20
updated: 2026-10-25
---

# Castle move graph and Hamilton paths

[[castle-native-gray-tour](pages/castle-native-gray-tour.md)] asks whether the even-block castles `V(w, h)` admit a Gray tour, and works the cases `(3, 2)` and `(3, 3)`. This page searches the same question at every `(w, h)` with `w ≥ 3`, `h ≤ 10` and at most 600 castles, 24 cells, and counts the Hamilton paths and the Hamilton cycles in the cells `(3, 2)` to `(6, 2)`, `(3, 3)`, `(4, 3)` and `(3, 4)`. It proves that bumps alone never give a Hamilton path at any width `w ≥ 3`, that at height 2 bumps and swaps give none from width 5 on, and that at width 3 and every odd height the four kinds of move together give none; the other entries are computed.

## The move graph

The move graph on `V(w, h)` has the castles of `V(w, h)` as vertices, `A^e(w, h)` of them, and an edge between two castles that differ by one move from a chosen set, both ends lying in `V(w, h)`. The four kinds of move, defined on [[castle-native-gray-tour](pages/castle-native-gray-tour.md)]:

- a **bump**: one column changes by `±1`;
- a **swap**: two neighboring columns are exchanged, `c_i ↔ c_{i+1}`;
- a **double bump**: one column changes by `±2`;
- a **far swap**: two columns `c_i ↔ c_j` with `|i − j| ≥ 2` are exchanged.

## Existence

The table covers every `(w, h)` with `w ≥ 3`, `h ≤ 10` and at most 600 castles. "Y" means a Hamilton path exists, and "-" that none exists; the letter after each "-" names its obstruction in section *Obstructions*. Section *Counts* counts the paths in the cells `(3, 2)` to `(6, 2)`, `(3, 3)`, `(4, 3)` and `(3, 4)`.[^1][^6]

| `(w, h)` | `\|V\|` | bumps | bumps + swaps | + double bumps | + far swaps | all four |
|:---|---:|:---:|:---:|:---:|:---:|:---:|
| (3, 2) | 6 | - a | Y | Y | Y | Y |
| (4, 2) | 10 | - a | Y | Y | Y | Y |
| (5, 2) | 16 | - a | - b | - b | Y | Y |
| (6, 2) | 28 | - a | - b | - b | Y | Y |
| (7, 2) | 56 | - a | - b | - b | Y | Y |
| (8, 2) | 120 | - a | - b | - b | Y | Y |
| (9, 2) | 256 | - a | - b | - b | Y | Y |
| (10, 2) | 528 | - a | - b | - b | Y | Y |
| (3, 3) | 3 | - c | - c | - c | - c | - c |
| (4, 3) | 21 | - a | - d | Y | - d | Y |
| (5, 3) | 89 | - a | - e | Y | Y | Y |
| (6, 3) | 307 | - a | - e | Y | Y | Y |
| (3, 4) | 31 | - a | Y | Y | Y | Y |
| (4, 4) | 117 | - a | Y | Y | Y | Y |
| (5, 4) | 439 | - a | - e | - e | Y | Y |
| (3, 5) | 10 | - c | - c | - c | - c | - c |
| (4, 5) | 122 | - a | - e | Y | - e | Y |
| (3, 6) | 76 | - a | - f | Y | Y | Y |
| (4, 6) | 448 | - a | Y | Y | Y | Y |
| (3, 7) | 21 | - c | - c | - c | - c | - c |
| (4, 7) | 367 | - a | - e | Y | - e | Y |
| (3, 8) | 141 | - a | - f | Y | Y | Y |
| (3, 9) | 36 | - c | - c | - c | - c | - c |
| (3, 10) | 226 | - a | - f | Y | Y | Y |

The obstructions:

- **a**, bumps alone (Theorem 1);
- **b**, bumps, swaps and double bumps at height 2 (Theorem 2);
- **c**, width 3 at an odd height (Theorem 3);
- **d**, the interior columns of height 1 at `(4, 3)`;
- **e**, a disconnected move graph, found by computation;
- **f**, a connected move graph that fails the degree conditions of a Hamilton path, found by computation.

The columns "+ double bumps" and "+ far swaps" add that kind of move to bumps and swaps. Adding moves only adds edges, so a "Y" holds for every larger set of moves. The values `|V| = A^e(w, h)` agree with the [[castle-counting-formula](pages/castle-counting-formula.md)].

All four kinds of move together give a Hamilton path in every cell except width 3 at odd heights. The smallest sets that work:

| added to bumps and swaps | cells |
|---|---|
| nothing | (3, 2), (4, 2), (3, 4), (4, 4), (4, 6) |
| double bumps or far swaps, either one | (5, 3), (6, 3), (3, 6), (3, 8), (3, 10) |
| double bumps; far swaps do not suffice | (4, 3), (4, 5), (4, 7) |
| far swaps; double bumps do not suffice | (5, 2) to (10, 2), (5, 4) |
| no set of the four suffices | (3, 3), (3, 5), (3, 7), (3, 9) |

## Obstructions

Each "-" in the existence table has a reason that a reader can check without a search for paths: an invariant that no move of the set changes, which splits the move graph, or, at `(3, 2)` and `(4, 2)`, a count of the two parity sides of a bipartite graph.

### Bumps alone, and height 2, at every width

Two parts of the existence table hold at every width, beyond the range searched. Both proofs rest on two facts about bumps:

- A bump changes the block count by at most 1 ([[castle-gray-code](pages/castle-gray-code.md)], the Lemma in the section *Algorithm G: the Gray tour*). Two castles of `V` both have an even block count, so a bump between two castles of `V` keeps the block count.
- A bump changes the area, the sum of the column heights, by 1. So the bump graph is bipartite, with the castles of even area on one side and those of odd area on the other, and a Hamilton path, which alternates between the sides, needs the two sides to differ in size by at most 1.

**Lemma (swaps at height 2).** At height 2, exchanging two neighboring columns changes the block count by −1, 0 or +1.

*Proof.* At height 2 the bottom row is one block and each maximal run of 2s is one block of the second row, so the block count is 1 plus the number of runs of 2s. A swap that changes the castle moves one 2 by one place, say from position `i` to `i + 1`. Write `a` and `b` for the columns at `i − 1` and `i + 2`, counting a missing column as 1. Only the runs through these four columns change:

| `a`, `b` | runs in `(a, 2, 1, b)` | runs in `(a, 1, 2, b)` | change |
|---|---|---|---|
| 1, 1 | 1 | 1 | 0 |
| 1, 2 | 2 | 1 | −1 |
| 2, 1 | 1 | 2 | +1 |
| 2, 2 | 2 | 2 | 0 |

Moving a 2 from `i + 1` to `i` is the reverse. ∎

**Theorem 1.** For every width `w ≥ 3` and height `h ≥ 2`, the bump graph on `V(w, h)` has no Hamilton path.

*Proof.* Bumps keep the block count, so the bump graph is disconnected as soon as `V(w, h)` holds two block counts:

- for `h ≥ 4`, the castles `(a, 1, h, 1, …, 1)` with `a = 1, …, h` have `a + h − 1` blocks, the values `h` to `2h − 1`, which include two even numbers;
- for `h = 3` and `w ≥ 5`, `(2, 1, 3, 1, …, 1)` has 4 blocks and `(3, 1, 2, 1, 3, 1, …, 1)` has 6;
- for `h = 2` and `w ≥ 5`, `(2, 2, …, 2)` has 2 blocks and `(2, 1, 2, 1, 2, …, 2)` has 4.

That leaves four cells. At `(3, 3)` and `(4, 3)` the bump graph has three components. At `(3, 2)` and `(4, 2)` it is connected, and its sides have 4 and 2 castles, and 6 and 4, so no Hamilton path alternates between them.[^3] ∎

At `(3, 4)` the bump graph has four components.

**Theorem 2.** At height 2 and every width `w ≥ 5`, bumps, swaps and double bumps give no Hamilton path on `V(w, 2)`. The components are the sets of castles with the same block count: for each odd `k` with `2k − 1 ≤ w`, the castles with `k` runs of 2s, `C(w + 1, 2k)` of them.

*Proof.* At height 2 no column can change by 2, so the moves are bumps and swaps, and by the bump Lemma and the swap Lemma a move between two castles of `V` keeps the block count. For `w ≥ 5`, `V(w, 2)` holds castles with 2 and with 4 blocks (proof of Theorem 1), so the graph is disconnected. A castle with `k` runs of 2s is fixed by the `2k` places, among the `w + 1` gaps before, between and after the columns, where a run starts or ends, so there are `C(w + 1, 2k)` of them, and the block count `1 + k` is even exactly when `k` is odd. Each set is connected. Lowering an end of a run of length at least 2 shortens it without changing the block count, so bumps shrink every run to a single 2. Swaps then slide the single 2s to the left in order, the `j`-th to position `2j − 1`; each step moves a single 2 one place left past a 1, and the columns on either side of that pair are 1s or missing, so the block count stays the same by the first row of the table. Every castle with `k` runs reaches `(2, 1, 2, 1, …, 2, 1, …, 1)`. ∎

At `(5, 2)` the set with three runs is the single castle `(2, 1, 2, 1, 2)`, which has no neighbor. At widths 3 and 4, `V(w, 2)` is one set, and bumps and swaps give Hamilton paths there (section *Counts*).

### Width 3 at odd heights

At width 3 the block count of a castle `(x, y, z)` is `x + max(0, y − x) + max(0, z − y)`. Unless the middle column is a strict valley it equals the height: if `y ≥ x` it is `max(y, z)`, and if `y < x` and `y ≥ z` it is `x`. So at an odd height `h` every castle of `V(3, h)` is a strict valley, with `x + z − y` blocks:

```
V(3, h)  =  { (x, y, z) :  y < min(x, z),  max(x, z) = h,  x + z − y even },        h odd.
```

**Theorem 3.** For every odd height `h = 2k + 1 ≥ 3`, `V(3, h)` has no Hamilton path under bumps, swaps, double bumps and far swaps together. No move joins its castles with an even middle column, `k²` of them, to those with an odd middle column, `k(k + 1)` of them, so `A^e(3, 2k + 1) = k(2k + 1)`.

*Proof.* *Moves.* Between two castles of `V(3, h)`, every move keeps the parity of the middle column `y`:

- a bump of any column changes `x + z − y` by 1; if the result still has height `h`, its block count is odd, `x + z − y ± 1` if it is a strict valley and `h` if not, so either way the result is not in `V(3, h)`;
- a swap with the middle column moves the middle, the smallest column, to an end, `(y, x, z)` or `(x, z, y)`, and the new middle is then at least one of its neighbors, so the block count is `h`, odd;
- a double bump changes a column by 2, and a far swap exchanges `x` and `z`; neither changes the parity of `y`.

Both parities occur, since `(2, 1, h)` and `(3, 2, h)` lie in `V(3, h)`, each with `h + 1` blocks. So the move graph is disconnected and has no Hamilton path.

*Counts.* If `x = z = h`, the condition is that `y` is even: `k` castles, all with an even middle. If `x = h > z`, the condition is that `z − y` is odd, with `1 ≤ y < z ≤ 2k`: one of `y` and `z` is odd and the other even, and of these `k²` pairs, `k(k + 1)/2` have `y` odd and `k(k − 1)/2` have `y` even. The case `z = h > x` is the mirror image. So the odd middles number `k(k + 1)` and the even middles `k + k(k − 1) = k²`. ∎

At `(3, 3)` the two sets are `{(3, 2, 3)}` and `{(2, 1, 3), (3, 1, 2)}`: each bump and each double bump of `(3, 2, 3)` has 3 blocks, each swap of it has 3 blocks, and the far swap `c_1 ↔ c_3` fixes it.[^2] For `h = 3, 5, 7, 9, 11` each of the two sets is connected, so they are the two components.[^4] A move between them changes the parity of `y` and keeps `x + z − y` even, so it changes `x + z` by an odd amount as well: it moves the middle column and an outer one at once, as `(3, 2, 3) → (3, 1, 2)` does at `(3, 3)`. At even heights the castles that are not valleys have `h` blocks, an even number, and belong to `V`: 28 of the 31 castles of `V(3, 4)`.

### Interior columns of height 1 at `(4, 3)`

All 21 castles of `V(4, 3)` have 4 blocks, so the block count does not split them. Whether a castle has a column of height 1 inside, at position 2 or 3, does: the 7 castles with no interior 1 have all their neighbors under bumps, swaps and far swaps among themselves.[^5]

| castle | neighbors in `V(4, 3)` under bumps, swaps and far swaps |
|---|---|
| (1, 3, 2, 3) | (2, 3, 2, 3) |
| (2, 3, 2, 3) | (1, 3, 2, 3), (3, 2, 2, 3), (3, 3, 2, 3) |
| (3, 2, 2, 3) | (2, 3, 2, 3), (3, 2, 3, 2), (3, 2, 3, 3), (3, 3, 2, 3) |
| (3, 2, 3, 1) | (3, 2, 3, 2) |
| (3, 2, 3, 2) | (3, 2, 2, 3), (3, 2, 3, 1), (3, 2, 3, 3) |
| (3, 2, 3, 3) | (3, 2, 2, 3), (3, 2, 3, 2), (3, 3, 2, 3) |
| (3, 3, 2, 3) | (2, 3, 2, 3), (3, 2, 2, 3), (3, 2, 3, 3) |

So bumps and swaps, with or without far swaps, keep these 7 castles apart from the other 14, and the move graph has no Hamilton path. Two double bumps raise an interior 1 to 3 and cross over, `(2, 1, 2, 3) → (2, 3, 2, 3)` and `(3, 2, 1, 2) → (3, 2, 3, 2)`, which is why double bumps repair `(4, 3)` and far swaps do not.

### Obstructions found by computation

Where no theorem on this page applies, the move graph is disconnected in all but three cells:[^6]

| cell | moves | components | sizes |
|---|---|---|---|
| (5, 3) | bumps + swaps | 3 | 1, 30, 58; the single castle is (3, 1, 2, 1, 3) |
| (6, 3) | bumps + swaps | 2 | 106, 201 |
| (5, 4) | bumps + swaps | 16 | 15 single castles, such as (2, 1, 2, 1, 4), and 424 |
| (5, 4) | + double bumps | 2 | 1 and 438; the single castle is (3, 2, 4, 2, 3) |
| (4, 5) | bumps + swaps, with or without far swaps | 2 | 48, 74 |
| (4, 7) | bumps + swaps, with or without far swaps | 2 | 155, 212 |

At `(5, 4)` the far swaps of `(3, 2, 4, 2, 3)` reach `(4, 2, 3, 2, 3)`, `(2, 2, 4, 3, 3)`, `(3, 2, 3, 2, 4)` and `(3, 3, 4, 2, 2)`, which is why far swaps repair `(5, 4)` and double bumps do not. [[castle-samplers](pages/castle-samplers.md)] finds the same castle isolated under single-column redraws.

At width 3 and heights 6, 8 and 10, bumps and swaps give a connected move graph in which every castle has at least two neighbors, and still no Hamilton path. The degree conditions already fail: no set of edges of the move graph gives every castle exactly two of them except two castles with one, as the edges of a Hamilton path would. Equivalently, the move graph with one vertex added and joined to every castle has no 2-factor, a set of edges with exactly two at every vertex. Two methods decide the degree conditions independently: a SAT solver, and a perfect-matching test on the graph in which each vertex of degree `d` becomes `d` copies, one for each of its edges, all joined to `d − 2` further vertices, and the two copies that stand for the same edge are joined; that graph has a perfect matching exactly when the original graph has a 2-factor. A constraint solver that searches for a Hamilton cycle through the added vertex finds none either. At `(3, 4)` bumps and swaps give 2,912 Hamilton paths.

## Counts

The number of Hamilton paths, each path counted once with either direction:[^1]

| `(w, h)` | bumps + swaps | + double bumps | + far swaps | all four |
|:---|---:|---:|---:|---:|
| (3, 2) | 10 | 10 | 34 | 34 |
| (4, 2) | 44 | 44 | 1,004 | 1,004 |
| (5, 2) | 0 | 0 | 49,508 | 49,508 |
| (6, 2) | 0 | 0 | 1,983,077,444 | 1,983,077,444 |
| (4, 3) | 0 | 704 | 0 | 71,509 |
| (3, 4) | 2,912 | 570,725,224,704 | 76,930,390 | 47,449,883,300,690 |

A Hamilton cycle is a tour that also returns to its first castle in one move, a Gray cycle in Knuth's terms; a Gray code needs only a Hamilton path.[^knuth-gray] The number of Hamilton cycles:[^1]

| `(w, h)` | bumps + swaps | + double bumps | + far swaps | all four |
|:---|---:|---:|---:|---:|
| (3, 2) | 1 | 1 | 3 | 3 |
| (4, 2) | 1 | 1 | 40 | 40 |
| (5, 2) | 0 | 0 | 364 | 364 |
| (6, 2) | 0 | 0 | 9,631,546 | 9,631,546 |
| (4, 3) | 0 | 4 | 0 | 267 |
| (3, 4) | 0 | 3,325,463,390 | 220,010 | 321,274,300,952 |

At `(3, 4)` bumps and swaps give 2,912 Hamilton paths and no Hamilton cycle. Bumps alone give neither in any cell, and at `(3, 3)` no set of moves gives either.

### Counting by a ZDD

A ZDD (zero-suppressed decision diagram, [[castle-bdd-zdd](pages/castle-bdd-zdd.md)]) can hold every Hamilton cycle of a graph as a set of edges. Knuth builds one for the simple paths between two vertices: number the vertices so that the frontier between the vertices already decided and the rest stays small, and carry across it a table `mate` that records, for each frontier vertex, whether it is untouched, used up, or one end of a partial path, and where the other end is. The reachable tables, reduced, form the ZDD. Small changes give the simple cycles and the Hamiltonian paths, and a dummy vertex joined to every other vertex lets a Hamiltonian path end anywhere.[^knuth]

The same dummy vertex turns paths into cycles here. Join one new vertex to every castle: a Hamilton cycle of the larger graph leaves the new vertex for one end of a Hamilton path of the move graph and comes back from the other, so each Hamilton path is one Hamilton cycle. The ZDD counts every cell of both tables in under a minute except `(3, 4)` with all four kinds of move, where it outgrows memory. There the counts come from inclusion-exclusion over the sets `S` of castles: twice the number of Hamilton paths is

```
Σ over S ⊆ V of (−1)^(|V| − |S|) · W(S),        W(S) = the number of walks of |V| − 1 moves that stay in S,
```

and twice the number of Hamilton cycles is the same sum over the sets `S` that contain one fixed castle, with `W(S)` the walks of `|V|` moves from that castle back to it. The sum takes `2^|V|` terms but little memory. Where both methods were run, the path counts at `(6, 2)` with far swaps and at `(3, 4)` with double bumps and with far swaps, and the cycle count at `(3, 4)` with double bumps, they agree.[^1]

## Entities & Concepts

- [[castle-native-gray-tour](pages/castle-native-gray-tour.md)] - the question, the four kinds of move, and the cases `(3, 2)` and `(3, 3)` worked by hand.
- [[castle-gray-code](pages/castle-gray-code.md)] - the Gray code on the whole cube `{1..h}^w`, and the Lemma that a bump changes the block count by at most 1.
- [[project-euler-502-brute-force](pages/project-euler-502-brute-force.md)] - the block-count formula used to list `V(w, h)`.
- [[castle-counting-formula](pages/castle-counting-formula.md)] - `A^e(w, h)`, the column `|V|` of the existence table.

## Related Concepts

- [[castle-samplers](pages/castle-samplers.md)] - the components of `V(w, h)` under bumps and under single-column redraws, up to `(8, 4)`.
- [[castle-bdd-zdd](pages/castle-bdd-zdd.md)] - `V(w, h)` itself as a decision diagram.

## Footnotes

[^1]: Verified by execution on `V(w, h)` listed with the block-count formula and the edges of each set of moves. Python 3.11 with graphillion 2.1 (2026-10-25): every count in both tables except `(3, 4)` with all four kinds of move, as the Hamilton cycles of the move graph (cycles) and of the move graph with one vertex added and joined to every castle (paths), `GraphSet.cycles(is_hamilton=True)`. A dynamic program over (visited set, last castle) for `|V| ≤ 21`: the path counts (2026-10-16), equal to the ZDD counts, and the cycle counts (2026-10-25); it also settles every "-" in those rows. Inclusion-exclusion in C, in 64-bit arithmetic modulo `2^64`, exact because every count is below `2^64` (2026-10-25): the paths and the cycles at `(3, 4)` with all four kinds of move, the paths at `(6, 2)` with far swaps and at `(3, 4)` with double bumps and with far swaps, and the cycles at `(3, 4)` with double bumps. The bump, bump-and-swap and bump-swap-and-double-bump graphs at `(6, 2)` are disconnected, and the bump graph at `(3, 4)` is disconnected (2026-10-16); at height 2 a swap changes the block count by at most 1 for every castle of width at most 10 (it fails at height 3).
[^2]: The three castles of `V(3, 3)` have 4 blocks. From `(3, 2, 3)`, the bumps give `(2,2,3)`, `(3,1,3)`, `(3,3,3)`, `(3,2,2)`, the double bumps `(1,2,3)`, `(3,2,1)`, and the swaps `(2,3,3)`, `(3,3,2)`, all with 3 blocks; the far swap `c_1 ↔ c_3` fixes `(3, 2, 3)`. Among the rearrangements of `(2, 1, 3)`, only `(2, 1, 3)` and `(3, 1, 2)` lie in `V(3, 3)`.
[^3]: Verified by execution (Python 3.11, 2026-10-25): the block counts of the castles named in the proof of Theorem 1, for `w = 3, 4, 6` and `h = 4, 5, 6` and for the height-3 and height-2 castles; the area sides 4 and 2 at `(3, 2)` and 6 and 4 at `(4, 2)`; three bump components at `(3, 3)` and at `(4, 3)`; for `3 ≤ w ≤ 8` and `2 ≤ h ≤ 6` with `h^w ≤ 300,000`, that the bump graph on `V(w, h)` is disconnected or bipartite with sides differing by at least 2; and for `w ≤ 12`, that the components of `V(w, 2)` under bumps, swaps and double bumps are the block-count classes, with `C(w + 1, 2k)` castles each.
[^4]: Verified by execution (Python 3.11, 2026-10-25), for odd `h ≤ 15`: every castle of `V(3, h)` is a strict valley, and `V(3, h)` is the set displayed; the counts `k²` and `k(k + 1)` of even and odd middle columns, and `A^e(3, 2k + 1) = k(2k + 1)`; every edge under the four kinds of move keeps the parity of the middle column; and, for `h ≤ 11`, the two sets are the two components. At `h = 4`, 28 of the 31 castles of `V(3, 4)` are not valleys.
[^5]: Verified by execution (Python 3.11, 2026-10-25): the 21 castles of `V(4, 3)`, each with 4 blocks; the neighbors of the 7 castles with no interior column of height 1 under bumps, swaps and far swaps; that the other 14 likewise have all their neighbors among themselves; and that the two double bumps shown are the only edges between the two sets.
[^6]: Verified by execution (Python 3.11 with NetworkX 3.4, OR-Tools 9.15 and python-sat 1.9 with CaDiCaL 1.5.3, 2026-10-25), for the 24 cells and five sets of moves: the components of each move graph, with the sizes and single castles listed; for each connected graph a Hamilton path, found by a greedy walk with rotations and checked edge by edge, except at `(3, 2)` and `(4, 2)` under bumps (Theorem 1) and at `(3, 6)`, `(3, 8)` and `(3, 10)` under bumps and swaps; OR-Tools CP-SAT, with its circuit constraint on the move graph plus one vertex joined to every castle, feasible in exactly the cells marked "Y" and infeasible in every other; for `(3, 6)`, `(3, 8)` and `(3, 10)` under bumps and swaps, no spanning subgraph with degree 2 at every castle but two of degree 1, by CaDiCaL on the degree conditions and by a maximum matching (NetworkX) on the vertex-splitting graph for the 2-factors of the graph plus one vertex, both of which find such a subgraph in every control cell that has a Hamilton path; the far swaps of `(3, 2, 4, 2, 3)` in `V(5, 4)`; and the column `|V|` against Equation (1) of [[castle-counting-formula](pages/castle-counting-formula.md)] (SymPy).
[^knuth]: assets/knuth-taocp-4a.pdf (D. E. Knuth, *The Art of Computer Programming*, Vol. 4A, *Combinatorial Algorithms, Part 1*, Addison-Wesley, 2011; read 2026-10-25) §7.1.4 p.255, exercises 225-228 p.275-276, answers p.667-668 - "exercise 227 shows how to construct a smaller ZDD, of size 4726, which describes just the Hamiltonian paths from CA to ME"; "225. Design an algorithm that will produce a ZDD for all sets of edges that form a simple path from s to t, given a graph and two distinct vertices {s, t} of the graph"; "226. Modify the algorithm of exercise 225 so that it yields a ZDD for all of the simple cycles in a given graph"; "227. Similarly, modify it so that it considers only Hamiltonian paths from s to t"; "228. And mutate it once more, for Hamiltonian paths from s to any other vertex"; answer 225: "we try to number the vertices in such a way that the 'frontier' between early and late vertices remains fairly small", "Let mate[i] = i if vertex i is untouched so far; let mate[i] = 0 if vertex i has been touched twice already. Otherwise mate[i] = r and mate[r] = i, if previous edges form a simple path with endpoints {i, r}"; answer 228: "Add a dummy vertex d = n + 1, with new edges [from v to d] for all v ≠ s; accepting this new edge will mean 'end at v.'"
[^knuth-gray]: assets/knuth-taocp-4a.pdf §7.2.1.1 p.295 - "a Gray cycle is a Hamiltonian cycle on the vertices of the n-cube, but a Gray code is simply a Hamiltonian path on that graph."
