---
title: Castle-native Gray tour
category: Concepts
summary: Whether a Gray tour exists on the valid-castle subset V(w, h) = {c : max c = h, blocks(c) even}, worked at small sizes; no castle-native Gray code is known. At (3, 2) the proper filter alone admits a Hamilton path under M1 (single-column pm-1); the even filter alone coincides with V at h = 2; V itself has no M1 Hamilton path (two pendant castles) but has one under M1 union M6 (adding adjacent transpositions). At (3, 3), V is three castles that no local move set tried connects. No general pattern is visible at these sizes; castle-move-graph-zdd extends the sweep.
tags: [concept, castle, gray-code, ruskey, hamiltonian-path, generation, algorithm, open-problem]
sources: [aocp-generating-permutations-tuples, project-euler-502-brute-force]
created: 2026-09-20
updated: 2026-10-02
---

# Castle-native Gray tour

> Larger cases are on [[castle-move-graph-zdd](pages/castle-move-graph-zdd.md)]: a move-set × `(w, h)` Hamilton-path sweep up to `(6, 2)` and `(4, 3)`, where M1 ∪ M6 fails from `(5, 2)` on and `(w, 2)` and `(4, 3)` need different enlargements.

## Scope

No castle-native Gray code on `V(w, h)` is known, and this page gives no successor rule. [[castle-gray-code](pages/castle-gray-code.md)] uses Knuth's Algorithm G (`h = 2`) and the loopless Gray algorithm (general `h`; Knuth's §7.2.1.1 Algorithm H) on the full cube `{1..h}^w`. For a restricted family such as `V(w, h)` there is no universal procedure: Ruskey's *Combinatorial Generation* is a set of techniques (recursive splits, boundary concatenation, exchange lemmas, loopless pointer implementations) applied family by family.[^1] This page works the question at `(3, 2)` and `(3, 3)`.

## The object

The valid-castle subset:

```
V(w, h) = { c ∈ {1..h}^w : max c = h  and  blocks(c) even },       |V| = F(w, h)
```

`V` is the intersection of two filters:

- **`V_proper(w, h) = { c : max c = h }`**, size `A(w, h) = h^w - (h-1)^w`.
- **`V_even(w, h) = { c ∈ {1..h}^w : blocks(c) even }`**, no proper-height constraint.

A **castle-native Gray tour** on `V(w, h)` is a Hamilton path in the graph `G(w, h)` whose vertices are `V(w, h)` and whose edges are single-step moves in a chosen move set. The choice of move set is part of the design; the candidates here are

- **M1**: single-column `±1` bump, both endpoints in the target subset.
- **M6**: adjacent transposition `c_i ↔ c_{i+1}`, both endpoints in the target subset.
- **M7**: single-column `±2` bump, both endpoints in the target subset (relevant only for `h ≥ 3`).

M1 is the restriction of Knuth's Gray step from the cube; M6 preserves the multiset of column heights, and M7 is the next single-column step.

## The three subsets at `(3, 2)`

Enumerating `{1..2}^3 = {1, 2}^3`, eight tuples, with block counts:[^2]

| tuple    | blocks | proper? | in V? |
|:---------|:------:|:-------:|:-----:|
| (1,1,1)  | 1      | no      | no    |
| (1,1,2)  | 2      | yes     | yes   |
| (1,2,1)  | 2      | yes     | yes   |
| (1,2,2)  | 2      | yes     | yes   |
| (2,1,1)  | 2      | yes     | yes   |
| (2,1,2)  | 3      | yes     | no    |
| (2,2,1)  | 2      | yes     | yes   |
| (2,2,2)  | 2      | yes     | yes   |

`|V_proper(3, 2)| = 7`, `|V_even(3, 2)| = 6`, `|V(3, 2)| = 6`. The improper tuple `(1,1,1)` has odd block count, so it is excluded by *both* filters; `V_even(3, 2)` and `V(3, 2)` happen to coincide. That is a coincidence of `h = 2`, not a theorem: at `h = 3`, `V_even` contains improper tuples with even blocks (the tuple `(1, 2, 1)` at `h = 3` has blocks 2 and max 2, so improper and even).

## `V_proper(3, 2)` alone under M1

Under M1 restricted to `V_proper`, the tour needs to avoid the one improper tuple `(1,1,1)` but is otherwise unconstrained by parity. The seven proper tuples plus the M1 edges give nine edges, no pendants, degree sequence `2, 2, 3, 2, 3, 3, 3`. A Hamilton path:[^3]

```
(1,1,2) → (2,1,2) → (2,1,1) → (2,2,1) → (2,2,2) → (1,2,2) → (1,2,1)
   c_1: 1→2   c_3: 2→1   c_2: 1→2   c_3: 1→2   c_1: 2→1   c_3: 2→1
```

Every step is a single-column `±1` bump landing on another proper tuple, so the proper filter alone does not obstruct a Gray tour at `(3, 2)` under M1.

## `V_even(3, 2)` alone at `h = 2`

`V_even(3, 2) = V(3, 2)` for the coincidence noted above (the single improper tuple `(1,1,1)` is also odd-block, so no proper-improper distinction is visible within the even sector at `h = 2`). The analysis of `V_even(3, 2)` under M1 is therefore identical to the both-filters case in the next section. To isolate the even-only filter as its own family one needs `h ≥ 3`, where `V_even` acquires improper even-block tuples (e.g. `(1, 2, 1)` at `h = 3`).

## `V(3, 2)` under M1

Six castles, six edges. Label:

```
A = (1,1,2)   B = (1,2,1)   C = (1,2,2)   D = (2,1,1)   E = (2,2,1)   F = (2,2,2)
```

All six castles have `blocks = 2`. The M1 edges:

| edge     | column bumped     | endpoints of the bump             |
|:---------|:------------------|:----------------------------------|
| A - C    | `c_2: 1 → 2`      | `(1,1,2) → (1,2,2)`               |
| B - C    | `c_3: 1 → 2`      | `(1,2,1) → (1,2,2)`               |
| B - E    | `c_1: 1 → 2`      | `(1,2,1) → (2,2,1)`               |
| C - F    | `c_1: 1 → 2`      | `(1,2,2) → (2,2,2)`               |
| D - E    | `c_2: 1 → 2`      | `(2,1,1) → (2,2,1)`               |
| E - F    | `c_3: 1 → 2`      | `(2,2,1) → (2,2,2)`               |

Degrees `A = 1, B = 2, C = 3, D = 1, E = 3, F = 2`. Two pendants (`A` and `D`), and any Hamilton path must have those two as endpoints. Exhaustive DFS from `A`:

```
A - C - B - E - D          F unvisited                         fail
A - C - B - E - F          D unvisited, F has no D-edge        fail
A - C - F - E - B          D unvisited                         fail
A - C - F - E - D          B unvisited                         fail
```

No Hamilton path in `(V(3,2), M1)`. The proper filter alone does not obstruct M1; adding the parity filter removes the connecting tuple `(2,1,2)` (odd-block, proper), which leaves `A` and `D` each with a single neighbour.

## `V(3, 2)` under M1 ∪ M6

Add adjacent transpositions preserving `V`:[^4]

| edge     | swap              | endpoints                          |
|:---------|:------------------|:-----------------------------------|
| A - B    | `c_2 ↔ c_3`       | `(1,1,2) ↔ (1,2,1)`                |
| B - D    | `c_1 ↔ c_2`       | `(1,2,1) ↔ (2,1,1)`                |

All other adjacent swaps at `(3, 2)` either fix `c` or exit `V`. Two new edges promote the pendants. A Hamilton path:

```
A → B → D → E → F → C
```

Edge by edge: `A-B` (M6, `c_2 ↔ c_3`), `B-D` (M6, `c_1 ↔ c_2`), `D-E` (M1, `c_2: 1→2`), `E-F` (M1, `c_3: 1→2`), `F-C` (M1, `c_1: 2→1`). All six castles visited exactly once.

## `V(3, 3)` under every local move set tried

At `(w, h) = (3, 3)`, `A(3, 3) = 3^3 - 2^3 = 19`, but `F(3, 3) = 3`. The three castles of `V(3, 3)`, each with `blocks = 4`:[^5]

```
V(3, 3) = { (2, 1, 3),  (3, 1, 2),  (3, 2, 3) }
```

Enumerating edges under every local move set considered:

| move set             | edges                                    |
|:---------------------|:-----------------------------------------|
| M1 (single-column `±1`) | none                                  |
| M6 (adjacent transposition) | none                              |
| M7 (single-column `±2`)  | none                                 |
| non-adjacent swap `c_1 ↔ c_3` | `(2,1,3) - (3,1,2)` only        |

`(3, 2, 3)` is isolated under every move set tried; it is symmetric under `c_1 ↔ c_3`, and every single-column `±1` or `±2` from it lands on an odd-block tuple. No Hamilton path on three vertices with at most one edge. At `(3, 3)` the obstruction is sparseness: the parity filter leaves three castles, and no local move set tried connects them.

## Summary of the small cases

- `V_proper(3, 2)` under M1: Hamilton path exists.
- `V(3, 2)` under M1: Hamilton path does not exist (pendants). Under M1 ∪ M6: Hamilton path exists.
- `V(3, 3)` under every local move set tried: no Hamilton path (at most the one edge `(2,1,3) - (3,1,2)`).

At `h = 2` the M1 graph on `V(3, 2)` is connected but has two pendant castles, and adding adjacent transpositions repairs it. At `(3, 3)` the three castles are far apart and no local move set tried relates them. No pattern is visible at these sizes; a Ruskey-style argument would need families of `(w, h)` with a recursion or a boundary concatenation.

[[castle-move-graph-zdd](pages/castle-move-graph-zdd.md)] extends the sweep to `(w, h)` up to `(6, 2)` and `(4, 3)` under four move sets (M1, M6, M7, Mnon), and finds that M1 ∪ M6, which works at `(3, 2)` and `(4, 2)`, has no Hamilton path at `(5, 2)`. Adding non-adjacent transpositions (M1 ∪ M6 ∪ Mnon) gives Hamilton paths at `(5, 2)` and `(6, 2)`, while `(4, 3)` needs a different enlargement (adding M7). That page also outlines what Knuth's SimPath methodology (TAOCP §7.1.4 exercises 225-228) would settle beyond DFS.

## What such a tour would give

A castle-native Gray tour on `V(w, h)` under any move set would have three properties the cube tour lacks.

- **No wasted visits.** The tour lands on `F(w, h)` castles in exactly `F(w, h)` steps.
- **Sign invariant.** `s(c) = +1` throughout, so the tour length is `F(w, h)`, with no `(T ± P)/2` projection ([[castle-sign](pages/castle-sign.md)]).
- **Local incremental structure.** Adjacent castles differ by one move in the chosen set, which a delta encoding can use ([[castle-compression](pages/castle-compression.md)]).

At `(3, 3)` no local move set tried gives such a tour.

## Open

- **Higher `h` at fixed `w = 3`.** Whether `V(3, h)` becomes connected under a local move set as `h` grows.
- **A recursion.** A split of `V(w, h)` by `c_1 = a`, by rightmost-peak position, or by [[castle-foata-transform](pages/castle-foata-transform.md)] record structure that the parity constraint lifts onto.
- **Loopless successor.** A Ruskey-style construction gives a Hamilton path as a sequence; whether a castle-native tour also admits an O(1)-per-step successor is a separate question.

## Entities & Concepts

- [[castle-move-graph-zdd](pages/castle-move-graph-zdd.md)] - the move-set × `(w, h)` Hamilton-path sweep and the Knuth SimPath methodology outline.
- [[castle-gray-code](pages/castle-gray-code.md)] - the tour on the full cube, the counterpart this page's object is filtered from.
- [[project-euler-502-brute-force](pages/project-euler-502-brute-force.md)] - the column-height block-count formula and the `F(w, h)` values used above (`F(3, 2) = 6`, `F(3, 3) = 3`, `F(4, 2) = 10`).
- [[aocp-generating-permutations-tuples](pages/aocp-generating-permutations-tuples.md)] - Knuth's Algorithms M / G / H on the cube; the universal counterpart Ruskey-methodology restricts.
- [[castle-sign](pages/castle-sign.md)] - `s(c) = (-1)^{blocks(c)}` and the `(T ± P)/2` projector; sign is invariant on `V`.
- [[castle-counting-formula](pages/castle-counting-formula.md)] - `F(w, h)`, the length a tour on `V` would have.

## Related Concepts

- [[castle-classification](pages/castle-classification.md)] / [[castle-representations](pages/castle-representations.md)] - each further castle-restriction axis (convex, tower-spacing, tree, unimodal) gives a subset of `V` with its own castle-native Gray-tour question.
- [[monotone-streak-factorization](pages/monotone-streak-factorization.md)] - the streak view relates single-coordinate bumps to the local block structure, useful for characterising M1 edges intrinsically.
- [[castle-foata-transform](pages/castle-foata-transform.md)] - the records / peaks decomposition is a natural axis for a Ruskey-style recursion on `V`.
- [[castle-compression](pages/castle-compression.md)] - delta encodings, which a castle-native tour would support.
- [[castle-samplers](pages/castle-samplers.md)] - the same fragmentation seen by Markov chains: `V(w, h)` has 191 components under single-column `±1` moves at `(8, 4)`, so chains run on the cube and filter at emit.

## Footnotes

[^1]: Frank Ruskey, *Combinatorial Generation*, a draft book from the University of Victoria (versions circa 2003 onward). Not a single algorithm but a collection of techniques - recursive family decomposition, boundary concatenation, reflection lemmas, exchange lemmas, loopless pointer-array implementations - applied case-by-case to specific restricted families (combinations, compositions, bounded partitions, Catalan objects, trees). Each specific family gets a designed algorithm proved correct for that family (e.g. "CoolLex" for combinations); there is no meta-algorithm that takes an arbitrary restricted family as input and produces a Gray code. Cited, not read.
[^2]: [[project-euler-502-brute-force](pages/project-euler-502-brute-force.md)] §"Column-height encoding" - `#blocks = c_1 + ∑_{i=2}^{w} max(0, c_i - c_{i-1})`; the eight-tuple table above was computed by hand from this formula on 2026-09-20, matching the six-castle `V(3, 2)` enumeration.
[^3]: `V_proper(3, 2)`, its nine M1 edges, and the Hamilton path `(1,1,2) → (2,1,2) → (2,1,1) → (2,2,1) → (2,2,2) → (1,2,2) → (1,2,1)` were computed by hand on 2026-09-20 and cross-verified by exhaustive DFS.
[^4]: `V(3, 2)`, its M1 and M6 edges, the M1 pendant/degree analysis, the exhaustive M1 search from `A`, and the `M1 ∪ M6` Hamilton path `A → B → D → E → F → C` were computed by hand on 2026-09-20. Each of the six castles was independently verified as proper and even-block via the column-height block-count formula; each of the eight edges was verified as either a single-column `±1` bump (M1) or an adjacent transposition (M6) both of whose endpoints lie in `V`.
[^5]: `V(3, 3)` was enumerated by hand from the nineteen proper tuples with `max = 3` and their block counts (block counts `3`, `4` and `5`, computed via the column-height formula); the three even-block castles are `(2, 1, 3)`, `(3, 1, 2)`, `(3, 2, 3)`. The M1, M6, M7 and non-adjacent-swap edge search was exhaustive over every such move from the three castles and confirmed by an independent brute pass on 2026-09-20 and again on 2026-09-28; the only surviving edge is `(2, 1, 3) - (3, 1, 2)` under the non-adjacent swap `c_1 ↔ c_3`.
