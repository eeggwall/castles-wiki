---
title: Castle-native Gray tour
category: Concepts
summary: A working note on the Ruskey-methodology question of whether a Gray tour exists on the valid-castle subset V(w, h) = {c : max c = h, blocks(c) even}. Not an algorithm. Small worked cases at (3, 2) - proper filter alone admits a Hamilton path under M1; even filter alone coincides with V at h=2; both filters need M1 union M6 (single-column pm-1 plus adjacent transposition). At (3, 3), V is three castles isolated under every local move set tried. No pattern is visible at the sizes hand-tractable here; the page records where the analysis hits a wall.
tags: [concept, castle, gray-code, ruskey, hamiltonian-path, generation, algorithm, working-note]
sources: [aocp-generating-permutations-tuples, project-euler-502-brute-force]
created: 2026-09-20
updated: 2026-09-20
---

# Castle-native Gray tour

## What this page is not

This page is not an algorithm. It gives no successor rule of the form "current castle in, next castle out." It does not exhibit a castle-native Gray code that works uniformly on `V(w, h)`. It does not close the question of whether such a code exists.

A reader arriving from [[castle-gray-code](pages/castle-gray-code.md)] expecting an Ives-style procedure will not find one. That page installs Knuth's Algorithm G (`h = 2`) and Ives' Algorithm H (general `h`) as off-the-shelf tools; those are single-recipe algorithms on the full cube `{1..h}^w`, universal and ~10 lines each. This page treats a different, harder object - the filtered subset `V(w, h)` - for which no such universal tool is known. Ruskey's *Combinatorial Generation* is a **methodology** (recursive splits, boundary concatenation, exchange lemmas, loopless pointer implementations), not a procedure; there is no meta-algorithm that takes an arbitrary restricted family as input and produces a Gray code as output. Each restricted family is its own case study.[^1]

## What this page is

A **working note** on that case study for `V(w, h)`. What follows:

- The setup - `V(w, h)`, the graph `G(w, h)`, the Hamilton-path question.
- The three subsets at `(3, 2)` - `V_proper`, `V_even`, and `V`; sizes and enumeration.
- Filter-in-isolation baby steps: `V_proper(3, 2)` admits a Hamilton path under M1 alone; `V_even(3, 2)` coincides with `V(3, 2)` at `h = 2` (a coincidence, not a theorem).
- Both-filters baby step at `(3, 2)`: M1 alone fails; the enlarged move set M1 ∪ M6 (adding adjacent transpositions) succeeds.
- A second both-filters baby step at `(3, 3)`: `V` shrinks to three castles that are isolated under every local move set attempted.
- A summary of where the analysis hits a wall.

If no pattern emerges beyond the small cases, this page has value as a research-note artifact recording what was tried, how far it went, and where it stopped.

## The object

The valid-castle subset:

```
V(w, h) = { c ∈ {1..h}^w : max c = h  and  blocks(c) even },       |V| = F(w, h)
```

`V` is the intersection of two filters:

- **`V_proper(w, h) = { c : max c = h }`**, size `A(w, h) = h^w - (h-1)^w`.
- **`V_even(w, h) = { c ∈ {1..h}^w : blocks(c) even }`**, no proper-height constraint.

A **castle-native Gray tour** on `V(w, h)` is a Hamilton path in the graph `G(w, h)` whose vertices are `V(w, h)` and whose edges are single-step moves in a chosen move set. The choice of move set is part of the design; the natural candidates are

- **M1**: single-column `±1` bump, both endpoints in the target subset.
- **M6**: adjacent transposition `c_i ↔ c_{i+1}`, both endpoints in the target subset.
- **M7**: single-column `±2` bump, both endpoints in the target subset (relevant only for `h ≥ 3`).

M1 is the smallest natural move and the direct restriction of Knuth's Gray step from the cube; M6 and M7 are the next simplest structure-preserving moves.

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

## Baby step: `V_proper(3, 2)` alone under M1

Under M1 restricted to `V_proper`, the tour needs to avoid the one improper tuple `(1,1,1)` but is otherwise unconstrained by parity. The seven proper tuples plus the M1 edges give nine edges, no pendants, degree sequence `2, 2, 3, 2, 3, 3, 3`. A Hamilton path:[^3]

```
(1,1,2) → (2,1,2) → (2,1,1) → (2,2,1) → (2,2,2) → (1,2,2) → (1,2,1)
   c_1: 1→2   c_3: 2→1   c_2: 1→2   c_3: 1→2   c_1: 2→1   c_3: 2→1
```

Every step is a single-column `±1` bump landing on another proper tuple. **The proper filter alone does not obstruct a castle-native Gray tour at `(3, 2)` under M1.**

## Baby step: `V_even(3, 2)` alone at `h = 2`

`V_even(3, 2) = V(3, 2)` for the coincidence noted above (the single improper tuple `(1,1,1)` is also odd-block, so no proper-improper distinction is visible within the even sector at `h = 2`). The analysis of `V_even(3, 2)` under M1 is therefore identical to the both-filters case in the next section. To isolate the even-only filter as its own family one needs `h ≥ 3`, where `V_even` acquires improper even-block tuples (e.g. `(1, 2, 1)` at `h = 3`).

## Baby step: `V(3, 2)` under M1

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

No Hamilton path in `(V(3,2), M1)`. **The composition of the two filters at `h = 2` obstructs M1 that neither filter alone obstructs.** The proper-only case was fine; adding the parity filter removes the connecting tuple `(2,1,2)` (odd-block, proper), leaving `A` and `D` each with a single neighbour.

## Baby step: `V(3, 2)` under M1 ∪ M6

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

## Baby step: `V(3, 3)` under every local move set tried

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

`(3, 2, 3)` is isolated under every move set tried; it is symmetric under `c_1 ↔ c_3`, and every single-column `±1` or `±2` from it lands on an odd-block tuple. No Hamilton path on three vertices with at most one edge. **The `(3, 3)` case fails for a different reason than `(3, 2)`: not "the parity filter creates pendants" but "the parity filter thins `V` so severely that no local move set connects it."**

## The wall

Three small cases, three different pictures:

- `V_proper(3, 2)` under M1: Hamilton path exists.
- `V(3, 2)` under M1: Hamilton path does not exist (pendants). Under M1 ∪ M6: Hamilton path exists.
- `V(3, 3)` under every local move set tried: no Hamilton path (three isolated castles, or at best one edge).

The `(3, 2)` and `(3, 3)` failures have different flavours. At `h = 2` the parity filter is sharp - it removes exactly the tuples whose block count is odd - and the graph is disconnected at pendants but locally dense elsewhere. At `h = 3` and small `w`, `V` is not merely disconnected but *sparse* - the even-block proper castles are combinatorially far apart, no local move relates them. There is no single move-set enlargement that repairs both failure modes uniformly.

No pattern is visible at these sizes. Ruskey-style analysis would need to work at families of `(w, h)` where a recursion or a boundary-concatenation argument can be made, and hand-analysis of `(4, 2)`, `(5, 2)`, and `(4, 3)` is the next step. This page pauses here.

## What such a tour would give, if it existed

For future reference: a castle-native Gray tour on `V(w, h)` under any move set would give three properties the cube tour does not.

- **No wasted visits.** The tour lands on `F(w, h)` castles in exactly `F(w, h)` steps.
- **Sign invariant.** `s(c) = +1` throughout, so `F(w, h)` is the tour length directly, a third route to `F` beyond the `(T ± P)/2` projector of [[castle-sign](pages/castle-sign.md)] and the `p_signed` DP of [[project-euler-502-brute-force](pages/project-euler-502-brute-force.md)].
- **Local incremental structure.** Adjacent castles differ by one move in the chosen set, which is exactly the kind of local structure the [[castle-compression](pages/castle-compression.md)] delta-encoding lens wants.

None of these is available at `(3, 3)` and above, on the evidence in this page.

## Further baby steps

Concrete next moves for someone continuing this work:

- **`(4, 2)` under M1 ∪ M6.** `F(4, 2) = 10` castles, ten-vertex Hamilton-path search still hand-feasible.
- **`(4, 3)` and `(5, 2)`.** Both larger and richer than the cases here; either reveal a pattern or extend the wall.
- **Higher `h` at fixed `w = 3`.** Recompute `V(3, h)` and its M1 edge count for `h = 4, 5, 6, ...`; the sparseness at `(3, 3)` may relax as `h` grows.
- **Ruskey-style recursion.** Split `V(w, h)` by `c_1 = a`, by rightmost-peak position, or by [[castle-foata-transform](pages/castle-foata-transform.md)] record structure. Verify (or refute) that the parity constraint lifts cleanly onto sub-families.
- **Minimum move set.** Under `M1 ∪ M6` at `(3, 2)`, the Hamilton path used two specific transpositions; is one of them redundant? Study the M6-edge role at `(4, 2)` and `(5, 2)`.
- **Loopless successor.** A Ruskey-style construction, if one exists, produces a Hamilton path as a sequence but not necessarily an O(1)-per-step successor. Whether the castle-native tour supports one is a separate combinatorial commitment on top of existence.

## Entities & Concepts

- [[castle-gray-code](pages/castle-gray-code.md)] - the tour on the full cube, the counterpart this page's object is filtered from.
- [[project-euler-502-brute-force](pages/project-euler-502-brute-force.md)] - the column-height block-count formula and the `F(w, h)` values used above (`F(3, 2) = 6`, `F(3, 3) = 3`, `F(4, 2) = 10`).
- [[aocp-generating-permutations-tuples](pages/aocp-generating-permutations-tuples.md)] - Knuth's Algorithms M / G / H on the cube; the universal counterpart Ruskey-methodology restricts.
- [[castle-sign](pages/castle-sign.md)] - `s(c) = (-1)^{blocks(c)}` and the `(T ± P)/2` projector; sign is invariant on `V`.
- [[castle-counting-formula](pages/castle-counting-formula.md)] - `F(w, h) = (A + P)/2` with `A = h^w - (h-1)^w`; the tour length a working tour would have.

## Related Concepts

- [[castle-classification](pages/castle-classification.md)] / [[castle-representations](pages/castle-representations.md)] - each further castle-restriction axis (convex, tower-spacing, tree, unimodal) is a sub-subset of `V` with its own castle-native Gray-tour question.
- [[monotone-streak-factorization](pages/monotone-streak-factorization.md)] - the streak view relates single-coordinate bumps to the local block structure, useful for characterising M1 edges intrinsically.
- [[castle-foata-transform](pages/castle-foata-transform.md)] - the records / peaks decomposition is a natural axis for a Ruskey-style recursion on `V`.
- [[castle-compression](pages/castle-compression.md)] - the delta-encoding lens that a working castle-native tour would supply.

## Footnotes

[^1]: Frank Ruskey, *Combinatorial Generation*, a draft book from the University of Victoria (versions circa 2003 onward). Not a single algorithm but a collection of techniques - recursive family decomposition, boundary concatenation, reflection lemmas, exchange lemmas, loopless pointer-array implementations - applied case-by-case to specific restricted families (combinations, compositions, bounded partitions, Catalan objects, trees). Each specific family gets a designed algorithm proved correct for that family (e.g. "CoolLex" for combinations); there is no meta-algorithm that takes an arbitrary restricted family as input and produces a Gray code. Not yet ingested into the wiki as a source page. Recommended for the reader who wants the general theory.
[^2]: [[project-euler-502-brute-force](pages/project-euler-502-brute-force.md)] §"Column-height encoding" - `#blocks = c_1 + ∑_{i=2}^{w} max(0, c_i - c_{i-1})`; the eight-tuple table above was computed by hand from this formula on 2026-09-20, matching the six-castle `V(3, 2)` enumeration.
[^3]: `V_proper(3, 2)`, its nine M1 edges, and the Hamilton path `(1,1,2) → (2,1,2) → (2,1,1) → (2,2,1) → (2,2,2) → (1,2,2) → (1,2,1)` were computed by hand on 2026-09-20 and cross-verified by exhaustive DFS.
[^4]: `V(3, 2)`, its M1 and M6 edges, the M1 pendant/degree analysis, the exhaustive M1 search from `A`, and the `M1 ∪ M6` Hamilton path `A → B → D → E → F → C` were computed by hand on 2026-09-20. Each of the six castles was independently verified as proper and even-block via the column-height block-count formula; each of the eight edges was verified as either a single-column `±1` bump (M1) or an adjacent transposition (M6) both of whose endpoints lie in `V`.
[^5]: `V(3, 3)` was enumerated by hand from the nineteen proper tuples with `max = 3` and their block counts (all four values `blocks ∈ {3, 4, 5}` computed via the column-height formula); the three even-block castles are `(2, 1, 3)`, `(3, 1, 2)`, `(3, 2, 3)`. The M1, M6, M7, and non-adjacent-swap edge search was exhaustive across all `3 · (2 · 3 + 2 + 2 + 1) = 33` candidate moves and confirmed by an independent brute pass on 2026-09-20; the only surviving edge is `(2, 1, 3) - (3, 1, 2)` under the non-adjacent swap `c_1 ↔ c_3`.
