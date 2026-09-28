---
title: Castle BDD / ZDD
category: Concepts
summary: The valid-castle set V(w, h) as a Binary Decision Diagram or zero-suppressed BDD, built by lifting the castle-strip transfer matrix to a DFA on state (last-column height, blocks-mod-2, is-h-reached) and encoding each column in ceil(log2 h) Boolean variables. Size O(h * w * log h); counting F(w, h) on it is one linear pass (linear in w, where Kitamasa is logarithmic). The ZDD form also supports uniform random sampling, rank/unrank and canonical-order enumeration (which run on the DFA directly too) and intersection with other castle-family ZDDs by the ZDD AND operation.
tags: [concept, castle, bdd, zdd, decision-diagram, representation, dfa, generation]
sources: [castle-count-algorithms, castle-representations, castle-strip]
created: 2026-09-20
updated: 2026-09-28
---

# Castle BDD / ZDD

A **binary decision diagram** (BDD) or **zero-suppressed BDD** (ZDD) is a compact directed-acyclic-graph representation of a Boolean function (BDD) or a family of sets (ZDD).[^1] This page constructs a BDD / ZDD for the valid-castle set

```
V(w, h) = { c ∈ {1..h}^w : max c = h  and  blocks(c) even },     |V| = F(w, h)
```

as a further representation alongside the encodings of [[castle-representations](pages/castle-representations.md)], of size `O(h · w · log h)`. The construction is a small extension of the [[castle-strip](pages/castle-strip.md)] transfer matrix: promote the `h`-state height automaton to a DFA on state `(last-column height, blocks-mod-2 bit, is-h-reached bit)`, then lift that DFA to a BDD variable-by-variable. Besides counting `F(w, h)`, the ZDD form supports uniform random sampling, an explicit rank / unrank bijection with `{1, …, F(w, h)}`, canonical-order enumeration without listing V, and intersection with any other castle-family ZDD.

## The DFA of V(w, h)

The [[castle-strip](pages/castle-strip.md)] transfer matrix is an `h × h` 0/1 matrix whose rows and columns are the allowed column heights `1..h`; the states *are* the heights. To capture `V(w, h)` and not just the ambient `h^w` tuples, add two bookkeeping bits:

```
state = ( last-column height c ∈ {1..h},
         blocks-mod-2 bit    b ∈ {0, 1},
         is-h-reached bit    r ∈ {0, 1} )
```

subject to `r = 0 ⟹ c ≤ h - 1` (if the top row has not yet been reached, the last column cannot be `h`).[^2]

**Transitions.** Reading column value `c_i = a` from state `(c, b, r)` gives new state `(a, b ⊕ [max(0, a - c) mod 2], r ∨ [a = h])`, following the column-height block-count formula `blocks = c_1 + ∑_{i≥2} max(0, c_i - c_{i-1})` on [[project-euler-502-brute-force](pages/project-euler-502-brute-force.md)]. The initial state is a sentinel `s_0 = (0, 0, 0)`; transitions from `s_0` on `a` produce `(a, a mod 2, [a = h])`, since prepending `c_0 = 0` makes the first-column contribution `max(0, a - 0) = a`.

**Acceptance.** After reading `w` columns the tuple is a valid castle iff the current state has `r = 1 and b = 0`.

**Size.** The three-bit state has at most `h · 2 · 2 = 4h` combinations; the constraint `r = 0 ⟹ c ≤ h - 1` removes the two with `r = 0` and `c = h`, leaving at most `4h - 2` non-initial states (all reachable for `h ≥ 3`), plus `s_0`, for at most `4h - 1` states. `O(h)` states, matching the [[castle-strip](pages/castle-strip.md)] transfer matrix order of magnitude.

## From DFA to BDD

Encode each column value `c_i ∈ {1..h}` in `⌈log_2 h⌉` Boolean variables, giving `w · ⌈log_2 h⌉` variables total in a column-by-column ordering (variables for `c_1` above variables for `c_2`, and so on). At a column boundary a BDD node is fixed by the DFA state. Inside a column, after `t` of its `b = ⌈log_2 h⌉` bits are read, a node is fixed by the bits read so far and by how the DFA state compares with the `2^{b−t}` values still possible for the column, which gives `O(h · b)` nodes per column, so

```
|BDD|  =  O(h · w · log h)
```

Measured on the reduced BDD, the growth per added column is `28, 90, 248, 630` nodes at `h = 4, 8, 16, 32`, the `h · log h` rate.[^6]

The satisfying-assignment count of that BDD, computable in one linear pass, is `F(w, h)`. That pass is linear in `w`, like the direct extractor of [[castle-count-algorithms](pages/castle-count-algorithms.md)]; the Kitamasa path there is logarithmic in `w` and is the practical route at `w = 10^12`. The BDD is another encoding of the same DFA, with the affordances listed below.[^3]

## Worked example: `(w, h) = (3, 2)`

At `h = 2` the state space has at most `4 · 2 - 1 = 7` reachable states. A BFS from `s_0` reaches six (one bookkeeping combination is empty at `h = 2` because a run of `1`s always ends at `blocks = 1`, so `(c = 1, b = 0, r = 0)` never appears):[^4]

| state         | on `c = 1`        | on `c = 2`        |
|:--------------|:------------------|:------------------|
| `s_0`         | `(1, 1, 0)`       | `(2, 0, 1)`       |
| `(1, 1, 0)`   | `(1, 1, 0)`       | `(2, 0, 1)`       |
| `(2, 0, 1)`   | `(1, 0, 1)`       | `(2, 0, 1)`       |
| `(1, 0, 1)`   | `(1, 0, 1)`       | `(2, 1, 1)`       |
| `(2, 1, 1)`   | `(1, 1, 1)`       | `(2, 1, 1)`       |
| `(1, 1, 1)`   | `(1, 1, 1)`       | `(2, 0, 1)`       |

Accept states are those with `r = 1 and b = 0`: `(1, 0, 1)` and `(2, 0, 1)`. Counting paths of length three from `s_0` ending in an accept state by dynamic programming gives `F(3, 2) = 6`, matching [[project-euler-502-brute-force](pages/project-euler-502-brute-force.md)].

**The BDD.** Encode `c_i ∈ {1, 2}` as `x_i ∈ {0, 1}` with `c_i = x_i + 1`. Reducing the DFA sub-function at each variable level gives a five-branch, seven-node BDD:

| node    | variable | LO branch (`x = 0`) | HI branch (`x = 1`) |
|:--------|:--------:|:--------------------|:--------------------|
| root    | `x_1`    | `n_1`               | `n_2`               |
| `n_1`   | `x_2`    | `n_3`               | `T`                 |
| `n_2`   | `x_2`    | `n_4`               | `T`                 |
| `n_3`   | `x_3`    | `F`                 | `T`                 |
| `n_4`   | `x_3`    | `T`                 | `F`                 |

Sinks: `T` (satisfying) and `F` (non-satisfying). Reading the root gives the Boolean formula `V(3, 2) = (x_1 ∧ (x_2 ∨ ¬x_3)) ∨ (¬x_1 ∧ (x_2 ∨ x_3))`, whose six satisfying assignments correspond to the six castles of `V(3, 2)`. The two excluded tuples are `(1, 1, 1) = 000` (improper: `max = 1`) and `(2, 1, 2) = 101` (odd blocks). Total BDD size: 5 branch nodes and 2 sinks, 7 nodes.

## ZDDs: the family-of-sets reading

A BDD represents a Boolean function; a **zero-suppressed BDD** represents a *family of sets*.[^5] The two structures are related but the ZDD reduction rule is different (an `x`-node whose HI branch is `F` is deleted, rather than an `x`-node whose LO and HI branches are equal). The ZDD reading of `V(w, h)` is: each castle `c` becomes a set of "column-choice" atoms (one atom per `c_i = a` pair, so `w · h` possible atoms total); `V(w, h)` is the family of atom-sets that satisfy the two filters. With the atoms in column order, the node at atom `(i, a)` is fixed by the DFA state before column `i` (the atoms `(i, 1), …, (i, a−1)` were all skipped), so this ZDD has at most `4h` nodes per atom level and `O(w · h²)` nodes in all.

Under this reading, the ZDD synthesis primitives from TAOCP §7.1.4 p. 251 - conjunction `∧`, disjunction `∨`, symmetric difference `⊕` - operate on ZDDs the way Boolean operations operate on Boolean functions: given a ZDD for `V(w, h)` and another ZDD for a castle-restriction family (convex, unimodal, tower-spacing, castle-strip-width-`w`, and so on across [[castle-classification](pages/castle-classification.md)]), one `∧` operation yields the ZDD for the intersection, at a cost of at most the product of the two ZDD sizes, and the restricted count is a linear-time count over the result.

## Affordances beyond counting

The ZDD gives four operations on `V(w, h)`. The first three also run directly on the DFA's completion counts, as the transfer-matrix sampler and rank/unrank on [[castle-samplers](pages/castle-samplers.md)] do; the fourth needs a ZDD for the other family.

- **Counting** `F(w, h)` in `O(|ZDD|)`, one linear pass.
- **Uniform random sampling** of `V(w, h)` in `O(|ZDD|)` per sample, by top-down descent weighted by the number of accepting completions at each branch (the per-node solution counts of Knuth's Algorithm C, p. 251).
- **Rank / unrank** - an explicit bijection `V(w, h) ↔ {1, …, F(w, h)}` in `O(|ZDD|)` per query, used for indexed enumeration (see [[castle-samplers](pages/castle-samplers.md)] and [[song-as-castle](pages/song-as-castle.md)]).
- **Restricted counts** - for a castle-restriction axis with its own ZDD, one `∧` gives `V ∩ (restriction)` and one count gives the restricted `F`; this applies to each classification axis on [[castle-classification](pages/castle-classification.md)] that has a ZDD.

Knuth notes on p. 251 that ZDDs beat BDDs when every set in the family is small (`νx` small whenever `f(x) = 1`). In the atom reading each castle uses `w` of the `w · h` atoms, so that is the regime of large `h`.

## Scale precedents from TAOCP §7.1.4

Knuth's demonstrations on p. 251 give a sense of what ZDDs can hold:

| family                                             | Boolean vars | ZDD size          | count               |
|:---------------------------------------------------|-------------:|------------------:|--------------------:|
| Tilings of the 8x8 chessboard by dominoes          |          112 |             2,300 |          12,988,816 |
| Independent sets of the contiguous-USA graph       |           49 |    177 (sifted 160) |               —     |
| Simple paths corner-to-corner on the 8x8 grid `P_8 ⊡ P_8` | 112 |            33,580 |     789,360,053,252 |

The dominoes example is the closest structural analog to `V(w, h)`: a family of `112`-variable set-selections satisfying local constraints, in a ZDD more than three orders of magnitude smaller than the family. The castle diagrams stay polynomial in `w` and `h` because the castle DFA has `O(h)` states; a domino tiling's frontier state grows exponentially with the board width.

## Not covered here

- **The explicit BDD / ZDD construction algorithm.** Knuth §7.1.4 pp. 216-248 covers this in detail (algorithms for building BDDs from truth tables, from Boolean expressions, and from computer programs); this page states the size bound and demonstrates the structure at `(3, 2)` but does not walk the general construction.
- **Working code.** No BDD / ZDD implementation is given here; the CUDD, Sylvan and SAPPOROBDD libraries implement the primitives cited. The top-down sampling and ranking are implemented on the DFA on [[castle-samplers](pages/castle-samplers.md)].
- **Large `w`.** Counting on the BDD is linear in `w`, so for the `w = 10^12` target only the Kitamasa path of [[castle-count-algorithms](pages/castle-count-algorithms.md)] (`O(D² log w)`) is practical; the ZDD's use is in sampling, ranking and intersection.

## Entities & Concepts

- [[castle-strip](pages/castle-strip.md)] - the `h × h` transfer matrix on column heights this page extends into a DFA on `(c, b, r)`.
- [[castle-count-algorithms](pages/castle-count-algorithms.md)] - the rational-function / Kitamasa path to `F(w, h)`; the ZDD count is linear in `w`, like the direct extractor there, where Kitamasa is logarithmic.
- [[castle-representations](pages/castle-representations.md)] - the encodings this page adds to.
- [[castle-classification](pages/castle-classification.md)] - restriction axes that can be intersected with `V` as ZDDs.
- [[project-euler-502-brute-force](pages/project-euler-502-brute-force.md)] - the column-height block-count formula the DFA transition uses.

## Related Concepts

- [[castle-counting-formula](pages/castle-counting-formula.md)] - the closed form for `F(w, h)`; the ZDD counts `F` directly by satisfying assignments, with no split into `A` and a signed sum.
- [[song-as-castle](pages/song-as-castle.md)] - rank / unrank on proper castles, the kind of bijection a ZDD's rank operation gives.
- [[castle-gray-code](pages/castle-gray-code.md)] / [[castle-native-gray-tour](pages/castle-native-gray-tour.md)] - generation orders; the ZDD gives a compact representation, Gray codes give a walking order.
- [[castle-entropy](pages/castle-entropy.md)] - `log_2 F(w, h) ≈ w · log_2 h - 1`; a ZDD rank is an index of that many bits.
- [[castle-samplers](pages/castle-samplers.md)] - the top-down sampling and rank/unrank of this page implemented on the DFA state, with exactness checked in rational arithmetic; one of ten castle samplers.

## Footnotes

[^1]: Knuth, TAOCP Vol. 4A §7.1.4 "Binary Decision Diagrams" (book pp. 202-280). BDDs are introduced on p. 202 as "Reduced Ordered Binary Decision Diagrams": ordered means every root-to-sink path visits variables in a fixed order, reduced means no two nodes have the same `(V, LO, HI)` triple and no node has `LO = HI`. ZDDs are introduced on p. 249, credited to Shin-ichi Minato (1993), with the reduction rule "an `x`-node whose HI branch is the `⊥` sink is deleted"; p. 250 gives the family-of-sets reading: "The root node of a ZDD names the smallest element that appears in at least one of the sets; its HI and LO branches represent the residual subfamilies that do and don't contain that element."
[^2]: The block-count formula `blocks = c_1 + ∑_{i≥2} max(0, c_i - c_{i-1})` is verified on [[project-euler-502-brute-force](pages/project-euler-502-brute-force.md)] against the run-based definition for all skylines `w, h ≤ 6`; the DFA transition `(c, b, r) →_a (a, b ⊕ [max(0, a - c) mod 2], r ∨ [a = h])` is that formula read one column at a time. The `r = 0 ⟹ c ≤ h - 1` constraint holds because `r` is `1` iff some read column equals `h`, and if the *last* column is `h` then in particular some column equals `h`.
[^3]: The DFA-to-BDD lift is standard (Knuth §7.1.4 pp. 216-227 discusses BDD construction from various sources); the node count at a variable level is the number of distinct sub-functions reachable there. On [[castle-count-algorithms](pages/castle-count-algorithms.md)] the rational-function path costs `O(D² log w)` with `D ≈ h + 1` (Kitamasa) or `O(w · D)` (direct extractor), and the `k`-direction Berlekamp–Massey path has recurrence order about `2w`; the BDD count is `O(h · w · log h)`, linear in `w`.
[^4]: The `(3, 2)` DFA state list, transition table, and BDD structure were computed by hand on 2026-09-20 against the transition rule of footnote 2. `F(3, 2) = 6` matches the six-castle enumeration `V(3, 2) = {(1,1,2), (1,2,1), (1,2,2), (2,1,1), (2,2,1), (2,2,2)}` from [[castle-native-gray-tour](pages/castle-native-gray-tour.md)]; the two excluded tuples are `(1,1,1) = 000` (`max c = 1`, improper) and `(2,1,2) = 101` (`blocks = 3`, odd).
[^6]: Reduced OBDD built by memoized recursion over `(column, bit, DFA state, prefix)` from the transition rule of footnote 2, with the column bits most significant first; sizes at `w = 10` and `w = 20` are `199, 479` (`h = 4`), `641, 1541` (`h = 8`), `1759, 4239` (`h = 16`) and `4437, 10737` (`h = 32`), and `(3, 2)` gives the 5 branch nodes above. The reachable non-initial DFA states number `4h − 2` for `h ≥ 3` (`5` at `h = 2`). Computed 2026-09-28.
[^5]: Knuth, TAOCP Vol. 4A §7.1.4 pp. 249-260, ZDD subsection. The synthesis primitives `∧, ∨, ⊕` are described on p. 251: "When we know the ZDDs for `f` and `g`, we can synthesize them to obtain the ZDDs for `f ∧ g, f ∨ g, f ⊕ g,` etc., using algorithms that are very much like the methods we've used for BDDs. Furthermore we can count and/or optimize the solutions of `f`, with analogs of Algorithms C and B." Exercises 197-209 are called out on p. 251 as "the nuts and bolts of all the basic ZDD procedures." The scale precedents cited in the "Scale precedents" section above are from pp. 251 (dominoes-on-chessboard, contiguous-USA independent sets) and 254 (8x8 grid simple paths).
