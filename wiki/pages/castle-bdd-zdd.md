---
title: Castle BDD / ZDD
category: Concepts
summary: The valid-castle set V(w, h) as a Binary Decision Diagram or zero-suppressed BDD, built by lifting the castle-strip transfer matrix to a DFA on state (last-column height, blocks-mod-2, is-h-reached) and encoding each column in ceil(log2 h) Boolean variables. Size O(h * w * log h), Kitamasa-equivalent for counting F(w, h), plus four ZDD affordances the tuple / grammar / step-string encodings lack: uniform random sampling, rank/unrank, canonical-order enumeration, and free intersection with other castle-family ZDDs.
tags: [concept, castle, bdd, zdd, decision-diagram, representation, dfa, generation]
sources: [castle-count-algorithms, castle-representations, castle-strip]
created: 2026-09-20
updated: 2026-09-20
---

# Castle BDD / ZDD

A **binary decision diagram** (BDD) or **zero-suppressed BDD** (ZDD) is a compact directed-acyclic-graph representation of a Boolean function (BDD) or a family of sets (ZDD).[^1] This page constructs a BDD / ZDD for the valid-castle set

```
V(w, h) = { c ∈ {1..h}^w : max c = h  and  blocks(c) even },     |V| = F(w, h)
```

as a third representation alongside the tuple / grammar / step-string encodings of [[castle-representations](pages/castle-representations.md)], sized `O(h · w · log h)`. The construction is a small extension of the [[castle-strip](pages/castle-strip.md)] transfer matrix: promote the `h`-state height automaton to a DFA on state `(last-column height, blocks-mod-2 bit, is-h-reached bit)`, then lift that DFA to a BDD variable-by-variable. Beyond the Kitamasa-equivalent counting of `F(w, h)`, the ZDD form supports uniform random sampling, an explicit rank / unrank bijection with `{1, …, F(w, h)}`, canonical-order enumeration without listing V, and free intersection with any other castle-family ZDD.

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

**Size.** The three-bit state has at most `h · 2 · 2 = 4h` combinations; the constraint `r = 0 ⟹ c ≤ h - 1` removes `2h` of them, leaving at most `2h + 2(h - 1) = 4h - 2` non-initial states, plus `s_0`, for at most `4h - 1` reachable states. `O(h)` states, matching the [[castle-strip](pages/castle-strip.md)] transfer matrix order of magnitude.

## From DFA to BDD

Encode each column value `c_i ∈ {1..h}` in `⌈log_2 h⌉` Boolean variables, giving `w · ⌈log_2 h⌉` variables total in a column-by-column ordering (variables for `c_1` above variables for `c_2`, and so on). At each variable level the BDD carries at most one node per distinct DFA state reachable at that point, so the BDD size is bounded by

```
|BDD|  ≤  (number of reachable DFA states) · w · ⌈log_2 h⌉  =  O(h · w · log h)
```

The satisfying-assignment count of that BDD, computable in one linear pass, is `F(w, h)`. This is Kitamasa-equivalent in complexity to the rational-function path of [[castle-count-algorithms](pages/castle-count-algorithms.md)]; the BDD is another encoding of the same DFA, with the affordances listed below.[^3]

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

Sinks: `T` (satisfying) and `F` (non-satisfying). Reading the root gives the Boolean formula `V(3, 2) = (x_1 ∧ (x_2 ∨ ¬x_3)) ∨ (¬x_1 ∧ (x_2 ∨ x_3))`, whose six satisfying assignments correspond to the six castles of `V(3, 2)`. The two excluded tuples are `(1, 1, 1) = 000` (improper: `max = 1`) and `(2, 1, 2) = 101` (odd blocks). Total BDD size: 5 branch nodes + 2 sinks = 7, matching the bound `4h · w = 24` for `(w, h) = (3, 2)` with plenty of room to spare after BDD reduction.

## ZDDs: the family-of-sets reading

A BDD represents a Boolean function; a **zero-suppressed BDD** represents a *family of sets*.[^5] The two structures are related but the ZDD reduction rule is different (an `x`-node whose HI branch is `F` is deleted, rather than an `x`-node whose LO and HI branches are equal). The ZDD reading of `V(w, h)` is: each castle `c` becomes a set of "column-choice" atoms (one atom per `c_i = a` pair, so `w · h` possible atoms total); `V(w, h)` is the family of atom-sets that satisfy the two filters.

Under this reading, the ZDD synthesis primitives from TAOCP §7.1.4 p. 251 - conjunction `∧`, disjunction `∨`, symmetric difference `⊕` - operate on ZDDs the way Boolean operations operate on Boolean functions: given a ZDD for `V(w, h)` and another ZDD for a castle-restriction family (convex, unimodal, tower-spacing, castle-strip-width-`w`, and so on across [[castle-classification](pages/castle-classification.md)]), a single `∧` operation yields the ZDD for the intersection, from which the restricted count is a linear-time count over that ZDD.

## Affordances beyond counting

The ZDD gives four operations on `V(w, h)` that the tuple / grammar / step-string encodings do not:

- **Counting** `F(w, h)` in `O(|ZDD|) = O(h · w · log h)`, Kitamasa-equivalent.
- **Uniform random sampling** of `V(w, h)` in `O(|ZDD|)` per sample, by top-down probabilistic descent weighted by the number of accepting completions at each branch (analog of Knuth's Algorithm B on p. 251).
- **Rank / unrank** — an explicit bijection `V(w, h) ↔ {1, …, F(w, h)}` in `O(|ZDD|)` per query, useful for indexed enumeration and for the [[castle-cryptography](pages/castle-cryptography.md)] rank-based encoding thread.
- **Restricted `F` for free** — for any castle-restriction axis with its own ZDD, one `∧` gives `V ∩ (restriction)` and one count gives the restricted `F` value; the classification axes on [[castle-classification](pages/castle-classification.md)] all become ZDD-intersect one-liners once each has its own ZDD.

Knuth notes on p. 251 that ZDDs specifically outperform BDDs when the represented family is *sparse* (`νx` small when `f(x) = 1`), which is the regime `V(w, h) ⊂ {1..h}^w` sits in for large `h`: the proper fraction is `1 - ((h - 1)/h)^w`, the even-block sub-fraction is roughly `1/2`, so `|V| ~ h^w / 2` while the ambient cube is `h^w`, and each castle uses only `w` of the `w · h` atoms.

## Scale precedents from TAOCP §7.1.4

Knuth's demonstrations on p. 251 give a sense of what ZDDs can hold:

| family                                             | Boolean vars | ZDD size          | count               |
|:---------------------------------------------------|-------------:|------------------:|--------------------:|
| Tilings of the 8x8 chessboard by dominoes          |          112 |             2,300 |          12,988,816 |
| Independent sets of the contiguous-USA graph       |           49 |    177 (sifted 160) |               —     |
| Simple paths corner-to-corner on the 8x8 grid `P_8 ⊡ P_8` | ~112 |            33,580 |     789,360,053,252 |

The dominoes example is the closest structural analog to `V(w, h)`: a family of `112`-variable set-selections satisfying local constraints, compressed into a ZDD three orders of magnitude smaller than the family it represents. The `O(h · w · log h)` bound above is much tighter than these, because the castle DFA has bounded state complexity while the dominoes DFA does not.

## Not covered here

- **The explicit BDD / ZDD construction algorithm.** Knuth §7.1.4 pp. 216-248 covers this in detail (algorithms for building BDDs from truth tables, from Boolean expressions, and from computer programs); this page states the size bound and demonstrates the structure at `(3, 2)` but does not walk the general construction.
- **Working code.** No BDD / ZDD implementation is committed with this page; the CUDD / Sylvan / SAPPOROBDD libraries implement the primitives cited here and would be the practical starting point.
- **Comparison with the [[castle-count-algorithms](pages/castle-count-algorithms.md)] Kitamasa path on absolute performance.** Both are `O(h · w · log h)` in asymptotics for `F(w, h)`; the constants and the affordances-per-dollar differ, and this page argues the ZDD's non-counting affordances are what make the trade worthwhile, not counting speed.

## Entities & Concepts

- [[castle-strip](pages/castle-strip.md)] - the `h × h` transfer matrix on column heights this page extends into a DFA on `(c, b, r)`.
- [[castle-count-algorithms](pages/castle-count-algorithms.md)] - the rational-function / Kitamasa path to `F(w, h)`; the ZDD count is the same asymptotic complexity in a different data structure.
- [[castle-representations](pages/castle-representations.md)] - tuple / grammar / step-string encodings this page is a fourth alternative to.
- [[castle-classification](pages/castle-classification.md)] - the axes of restriction that lift to ZDD-intersect one-liners.
- [[project-euler-502-brute-force](pages/project-euler-502-brute-force.md)] - the column-height block-count formula the DFA transition uses.

## Related Concepts

- [[castle-counting-formula](pages/castle-counting-formula.md)] - `F(w, h) = (A + P)/2`; the ZDD counts `F` directly by satisfying assignments, skipping the `(A, P)` split.
- [[castle-cryptography](pages/castle-cryptography.md)] - the rank-based castle encoding thread that a ZDD's rank / unrank operations feed directly.
- [[castle-gray-code](pages/castle-gray-code.md)] / [[castle-native-gray-tour](pages/castle-native-gray-tour.md)] - the sibling generation-algorithm lens; the ZDD gives a compact representation, Gray codes give a walking order.
- [[castle-entropy](pages/castle-entropy.md)] - `w · log_2 h - 1` bits of entropy; the ZDD's rank operation realises this bit budget as a natural bijection.

## Footnotes

[^1]: Knuth, TAOCP Vol. 4A §7.1.4 "Binary Decision Diagrams" (book pp. 202-280). BDDs are introduced on p. 202 as "Reduced Ordered Binary Decision Diagrams": ordered means every root-to-sink path visits variables in a fixed order, reduced means no two nodes have the same `(V, LO, HI)` triple and no node has `LO = HI`. ZDDs are introduced on p. 249, credited to Shin-ichi Minato (1993), with the reduction rule "an `x`-node whose HI branch is the `⊥` sink is deleted"; p. 250 gives the family-of-sets reading: "The root node of a ZDD names the smallest element that appears in at least one of the sets; its HI and LO branches represent the residual subfamilies that do and don't contain that element."
[^2]: The block-count formula `blocks = c_1 + ∑_{i≥2} max(0, c_i - c_{i-1})` is verified on [[project-euler-502-brute-force](pages/project-euler-502-brute-force.md)] against the run-based definition for all skylines `w, h ≤ 6`; the DFA transition `(c, b, r) →_a (a, b ⊕ [max(0, a - c) mod 2], r ∨ [a = h])` is that formula read one column at a time. The `r = 0 ⟹ c ≤ h - 1` constraint holds because `r` is `1` iff some read column equals `h`, and if the *last* column is `h` then in particular some column equals `h`.
[^3]: The DFA-to-BDD lift is standard (Knuth §7.1.4 pp. 216-227 discusses BDD construction from various sources); the state count per variable level is bounded by the number of distinct sub-functions reachable at that level, which for a DFA of `D` states is at most `D`. Kitamasa complexity for `F(w, h)` is `O(D^2 log w)` with `D = 2(w+2)` empirically on [[castle-count-algorithms](pages/castle-count-algorithms.md)]; the BDD path here is `O(h · w · log h)`, which for the PE 502 regime (`h ≤ 15000`) is smaller because it depends on `h` not on the BM-discovered recurrence order `2w`. Not a claim that the BDD path is faster in practice on PE 502 - the affordances section is where the ZDD earns its keep.
[^4]: The `(3, 2)` DFA state list, transition table, and BDD structure were computed by hand on 2026-09-20 against the transition rule of footnote 2. `F(3, 2) = 6` matches the six-castle enumeration `V(3, 2) = {(1,1,2), (1,2,1), (1,2,2), (2,1,1), (2,2,1), (2,2,2)}` from [[castle-native-gray-tour](pages/castle-native-gray-tour.md)]; the two excluded tuples are `(1,1,1) = 000` (`max c = 1`, improper) and `(2,1,2) = 101` (`blocks = 3`, odd).
[^5]: Knuth, TAOCP Vol. 4A §7.1.4 pp. 249-260, ZDD subsection. The synthesis primitives `∧, ∨, ⊕` are described on p. 251: "When we know the ZDDs for `f` and `g`, we can synthesize them to obtain the ZDDs for `f ∧ g, f ∨ g, f ⊕ g,` etc., using algorithms that are very much like the methods we've used for BDDs. Furthermore we can count and/or optimize the solutions of `f`, with analogs of Algorithms C and B." Exercises 197-209 are called out on p. 251 as "the nuts and bolts of all the basic ZDD procedures." The scale precedents cited in the "Scale precedents" section above are from pp. 251 (dominoes-on-chessboard, contiguous-USA independent sets) and 254 (8x8 grid simple paths).
