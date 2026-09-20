---
title: Castle-native Gray tour
category: Concepts
summary: A Gray tour on the valid-castle subset V(w,h) = {c : max c = h, blocks(c) even} directly, no wasted visits on improper or odd-block tuples; single-column ±1 preserving V admits no Hamilton path at (3,2), but the enlarged move set with adjacent transpositions does; sign is invariant along the tour so F(w,h) is read off directly, not via (A+P)/2. Open beyond (3,2). In the style of Ruskey's Combinatorial Generation.
tags: [concept, castle, gray-code, ruskey, hamiltonian-path, generation, algorithm]
sources: [aocp-generating-permutations-tuples, project-euler-502-brute-force]
created: 2026-09-20
updated: 2026-09-20
---

# Castle-native Gray tour

The [[castle-gray-code](pages/castle-gray-code.md)] page tours all `h^w` tuples of the mixed-radix cube `{1..h}^w` in Knuth-Gray order and applies the two castle filters (`max c = h`, `s(c) = +1`) as O(1) predicates at emit. That works, but it visits every improper ("too short") tuple and every proper odd-block tuple along the way - roughly half the total for large `w`. A **castle-native Gray tour** removes those wasted visits by moving *only within the valid-castle subset*:

```
V(w, h) = { c ∈ {1..h}^w : max c = h  and  blocks(c) even },       |V| = F(w, h)
```

The tour is a Hamilton path in the graph `G(w, h)` whose vertices are `V(w, h)` and whose edges are the admitted single-step moves (a design choice, chosen below). The question is whether such a Hamilton path exists, for what move sets, and for which `(w, h)`. This is a combinatorial-generation question in the style of Ruskey's *Combinatorial Generation*, distinct from Knuth's algorithms on the full cube: Knuth generates *unrestricted* families, Ruskey builds Gray codes for *restricted* families by recursive decomposition and boundary-concatenation.[^1]

## The naive move set at `(3, 2)`

Start with the most restrictive move set:

- **M1**: single-column `±1` bump, both endpoints in `V`.

A single-column `±1` bump changes `blocks(c)` by `{-1, 0, +1}` (the lemma on [[castle-gray-code](pages/castle-gray-code.md)]), and only `Δ blocks = 0` preserves parity. So an M1 edge is a single-column `±1` bump that introduces no new block and merges no run, and whose result is still proper.

At `(w, h) = (3, 2)`, `F(3, 2) = 6`,[^2] and

```
V(3, 2) = { A=(1,1,2), B=(1,2,1), C=(1,2,2), D=(2,1,1), E=(2,2,1), F=(2,2,2) }
```

All six castles have `blocks = 2` (each has one full column at height 2 and two shorter columns whose contribution is either a rise or fall of 1). Enumerating the M1 edges by trying every `±1` bump at every position and keeping those whose target is in `V`:

| edge     | column bumped     | endpoints of the bump             |
|:---------|:------------------|:----------------------------------|
| A - C    | `c_2: 1 → 2`      | `(1,1,2) → (1,2,2)`               |
| B - C    | `c_3: 1 → 2`      | `(1,2,1) → (1,2,2)`               |
| B - E    | `c_1: 1 → 2`      | `(1,2,1) → (2,2,1)`               |
| C - F    | `c_1: 1 → 2`      | `(1,2,2) → (2,2,2)`               |
| D - E    | `c_2: 1 → 2`      | `(2,1,1) → (2,2,1)`               |
| E - F    | `c_3: 1 → 2`      | `(2,2,1) → (2,2,2)`               |

Six edges. Degrees: `A = 1, B = 2, C = 3, D = 1, E = 3, F = 2`. Two pendants (`A` and `D`), so any Hamilton path must have `A` at one end and `D` at the other. Exhaustive search from `A`:

```
A - C - B - E - D          F unvisited                         fail
A - C - B - E - F          D unvisited, F has no D-neighbour   fail
A - C - F - E - B          D unvisited                         fail
A - C - F - E - D          B unvisited                         fail
```

**No Hamilton path exists in `(V(3,2), M1)`.** The single-column `±1` move set is too restrictive: the two pendants `A = (1,1,2)` and `D = (2,1,1)` each have only one M1-neighbour, so a single Hamilton walk cannot leave both of them via the same neighbour and still cover the rest.

## Adjacent transpositions: `(3, 2)` under `M1 ∪ M6`

Enlarge the move set with the next simplest structure-preserving move:

- **M6**: adjacent transposition `c_i ↔ c_{i+1}`, both endpoints in `V`.

A transposition leaves the multiset of column heights unchanged, so `max c = h` is preserved; parity is preserved when the local re-cut of the two adjacent runs happens to leave the total block count fixed. At `(3, 2)`, enumerating adjacent swaps that stay in `V`:

| edge     | swap              | endpoints                          |
|:---------|:------------------|:-----------------------------------|
| A - B    | `c_2 ↔ c_3`       | `(1,1,2) ↔ (1,2,1)`                |
| B - D    | `c_1 ↔ c_2`       | `(1,2,1) ↔ (2,1,1)`                |

All other adjacent swaps at `(3, 2)` either fix `c` (equal neighbours) or exit `V` (e.g. `(2,2,1)` with `c_2 ↔ c_3` gives `(2,1,2)`, block count 3, odd).

Two new edges, promoting the two pendants `A` and `D` to degree 2 each. Combined edge set:

```
{ A-B, A-C, B-C, B-D, B-E, C-F, D-E, E-F }
```

with degrees `A = 2, B = 4, C = 3, D = 2, E = 3, F = 2`. A Hamilton path:

```
A - B - D - E - F - C
```

Verifying each step is a legal move whose result is in `V`:

- `A - B`: `c_2 ↔ c_3`, `(1,1,2) → (1,2,1)`, M6.
- `B - D`: `c_1 ↔ c_2`, `(1,2,1) → (2,1,1)`, M6.
- `D - E`: `c_2: 1 → 2`, `(2,1,1) → (2,2,1)`, M1.
- `E - F`: `c_3: 1 → 2`, `(2,2,1) → (2,2,2)`, M1.
- `F - C`: `c_1: 2 → 1`, `(2,2,2) → (1,2,2)`, M1.

All six castles of `V(3, 2)` visited exactly once. A castle-native Gray tour on `(V(3, 2), M1 ∪ M6)` exists.[^3]

## No wasted visits, no sign update

Every step of the castle-native tour lands on a valid castle, so the [[castle-sign](pages/castle-sign.md)] `s(c) = +1` is *invariant* along the tour. There is no O(1) sign update, because the tour never leaves the even-block sector; and there is no signed sum to accumulate, because the emit is the castle itself. `F(w, h)` is read off directly as the tour length. The `(T ± P)/2` projector of [[castle-sign](pages/castle-sign.md)] and the `p_signed` column-height DP of [[project-euler-502-brute-force](pages/project-euler-502-brute-force.md)] are two other routes to `F`; the castle-native tour is a third.

The comparison with the [[castle-gray-code](pages/castle-gray-code.md)] tour on the full cube is direct:

- **Generic Gray on the cube.** Visits `h^w` tuples. Sign `s(c)` updated in O(1) per step. Emits `F(w, h)` castles after filtering. Wasted-visit fraction `((h-1)/h)^w + 1/2 \cdot (1 - P/A)`, tending to `1/2` as `w → ∞`. Loopless: closed via Ives' Algorithm H.
- **Castle-native Gray on `V`.** Visits `F(w, h)` castles. Sign invariant. No wasted visits. Loopless: open, depends on whether a move set + successor rule with worst-case O(1) exists.

The castle-native tour trades the "walk-and-filter" cost of the cube tour for the harder combinatorial cost of finding an admissible move set on `V(w, h)`.

## Open questions

- **Existence beyond `(3, 2)`.** Does `M1 ∪ M6` admit a Hamilton path in `V(w, h)` for all `(w, h)`, or only some? `(4, 2)` has `F(4, 2) = 10` castles;[^2] a hand search or a small brute check would settle that case, and `(w, 2)` for `w = 5, 6, …` gives a family of test cases.
- **Higher `h`.** At `h ≥ 3`, `Δ blocks = 0` under a single-column `±1` occurs more often (the interior term `max(0, c_{i+1} - c_i)` has more room to absorb the bump), so M1 alone may already be enough at some `(w, h)`. The `(3, 2)` failure is partly an artifact of the tight `h = 2` case.
- **Minimum move set.** Is there a subset of `M1 ∪ M6`, or an alternative move set (`c_i ↔ c_{i+2}`, single-column `±2`, coordinated two-column moves), that admits a Hamilton path with fewer degrees of freedom?
- **Loopless successor.** If a Hamilton path exists uniformly in `(w, h)`, does it admit a worst-case O(1) successor rule à la Ives' Algorithm H on the cube ([[castle-gray-code](pages/castle-gray-code.md)]), or is the algorithm inherently non-loopless (backtracking, recursion-depth memory)?
- **Ruskey-style recursion.** Split `V(w, h)` by `c_1 = a` (or by rightmost-peak position, or by the [[castle-foata-transform](pages/castle-foata-transform.md)] record structure) and construct a Gray tour on each sub-family, concatenating at boundary elements. Which split makes both filters lift cleanly onto the sub-families?

## Entities & Concepts

- [[castle-gray-code](pages/castle-gray-code.md)] - the tour on the full cube; this page is the castle-native counterpart living on `V(w, h)` alone.
- [[project-euler-502-brute-force](pages/project-euler-502-brute-force.md)] - the column-height block-count formula and the `F(w, h)` checkpoints (`F(3, 2) = 6`, `F(4, 2) = 10`) used above.
- [[aocp-generating-permutations-tuples](pages/aocp-generating-permutations-tuples.md)] - Knuth's Algorithms M / G / H on the full cube, the counterpart Ruskey's methodology restricts.
- [[castle-sign](pages/castle-sign.md)] - `s(c) = (-1)^{blocks(c)}` and the `(T ± P)/2` projector; invariant along this tour.
- [[castle-counting-formula](pages/castle-counting-formula.md)] - `F(w, h) = (A + P)/2` with `A = h^w - (h-1)^w`; the tour length.

## Related Concepts

- [[castle-classification](pages/castle-classification.md)] / [[castle-representations](pages/castle-representations.md)] - each further castle-restriction axis (convex, tower-spacing, tree, unimodal) is a sub-subset of `V` with its own castle-native Gray-tour question.
- [[monotone-streak-factorization](pages/monotone-streak-factorization.md)] - the streak view relates single-coordinate bumps to the local block structure, useful for characterising `M1` edges intrinsically.
- [[castle-foata-transform](pages/castle-foata-transform.md)] - the records / peaks decomposition is a natural axis for a Ruskey-style recursion on `V`.

## Footnotes

[^1]: Frank Ruskey, *Combinatorial Generation*, a draft book from the University of Victoria (versions circa 2003 onward): chapters on Gray codes for restricted objects (combinations, compositions, bounded partitions, trees) build the recursive-decomposition and boundary-concatenation methodology that this page applies to `V(w, h)`. Not yet ingested into the wiki as a source page; the framing above adapts the methodology to the castle object. Recommended for the reader who wants the general theory of Gray codes on restricted families.
[^2]: [[project-euler-502-brute-force](pages/project-euler-502-brute-force.md)] §"Verification" - `F(3, 2) = 6` from `F(w, h) = (A + P)/2` with `A(3, 2) = 2^3 - 1^3 = 7` and `P(1, 3) = 5` (six even, one odd, matching the `V(3, 2)` enumeration above); `F(4, 2) = 10` is the first checkpoint on [[project-euler-502-brute-force](pages/project-euler-502-brute-force.md)] and re-verified during that ingest.
[^3]: `V(3, 2)`, its M1 and M6 edges, the M1 pendant/degree analysis, the exhaustive M1 search from `A`, and the `M1 ∪ M6` Hamilton path `A → B → D → E → F → C` were computed by hand on 2026-09-20. Each of the six castles was independently verified as proper and even-block via the column-height block-count formula; each of the eight edges was verified as a single-column `±1` bump (M1) or an adjacent transposition (M6) both of whose endpoints lie in `V`.
