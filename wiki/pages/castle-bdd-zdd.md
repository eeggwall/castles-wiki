---
title: Castle BDD / ZDD
category: Concepts
summary: The even-block castles V(w, h) as a binary decision diagram (BDD) or zero-suppressed BDD (ZDD), built by lifting the castle-strip transfer matrix to a deterministic finite automaton on (last column height, block count mod 2, height h reached) and encoding each column in ceil(log2 h) Boolean variables. The reduced BDD has O(h w log h) nodes (measured growth 28, 90, 248, 630 nodes per column at h = 4, 8, 16, 32), and counting its satisfying assignments gives A^e(w, h) in one pass, linear in w where Kitamasa's method is logarithmic. The ZDD also supports uniform sampling, rank/unrank and intersection with the ZDD of another castle family.
tags: [concept, castle, bdd, zdd, decision-diagram, representation, dfa, generation]
sources: [castle-count-algorithms, castle-representations, castle-strip]
created: 2026-09-20
updated: 2026-10-16
---

# Castle BDD / ZDD

A **binary decision diagram** (BDD) or **zero-suppressed BDD** (ZDD) is a compact directed-acyclic-graph representation of a Boolean function (BDD) or a family of sets (ZDD).[^1] This page constructs a BDD and a ZDD for the set of even-block castles of width `w` and height `h`

```
V(w, h) = { c ∈ {1..h}^w : max c = h  and  blocks(c) even },     |V| = A^e(w, h)
```

as a further representation alongside the encodings of [[castle-representations](pages/castle-representations.md)], of size `O(h · w · log h)`. The construction is a small extension of the [[castle-strip](pages/castle-strip.md)] transfer matrix: promote the `h`-state height automaton to a deterministic finite automaton (DFA) on the state `(last-column height, blocks-mod-2 bit, is-h-reached bit)`, then lift that DFA to a BDD variable-by-variable. Besides counting the `A^e(w, h)` castles, the ZDD supports uniform random sampling, a rank / unrank bijection with `{1, …, A^e(w, h)}`, and intersection with the ZDD of another castle family.

## The DFA of V(w, h)

The [[castle-strip](pages/castle-strip.md)] transfer matrix is an `h × h` 0/1 matrix whose rows and columns are the allowed column heights `1..h`; the states *are* the heights. To capture `V(w, h)` and not just the ambient `h^w` tuples, add two bookkeeping bits:

```
state = ( last-column height c ∈ {1..h},
         blocks-mod-2 bit    b ∈ {0, 1},
         is-h-reached bit    r ∈ {0, 1} )
```

subject to `r = 0 ⟹ c ≤ h - 1` (if the top row has not yet been reached, the last column cannot be `h`).[^2]

**Transitions.** Reading column value `c_i = a` from state `(c, b, r)` gives new state `(a, b ⊕ [max(0, a - c) mod 2], r ∨ [a = h])`, following the column-height block-count formula `blocks = c_1 + ∑_{i≥2} max(0, c_i - c_{i-1})` on [[project-euler-502-brute-force](pages/project-euler-502-brute-force.md)]. The initial state is a sentinel `s_0 = (0, 0, 0)`; transitions from `s_0` on `a` produce `(a, a mod 2, [a = h])`, since prepending `c_0 = 0` makes the first-column contribution `max(0, a - 0) = a`.

**Acceptance.** After reading `w` columns the tuple is an even-block castle of height `h` exactly when the state has `r = 1` and `b = 0`.

**Size.** The three-bit state has at most `h · 2 · 2 = 4h` combinations; the constraint `r = 0 ⟹ c ≤ h - 1` removes the two with `r = 0` and `c = h`, leaving at most `4h - 2` non-initial states (all reachable for `h ≥ 3`), plus `s_0`, for at most `4h - 1` states. `O(h)` states, matching the [[castle-strip](pages/castle-strip.md)] transfer matrix order of magnitude.

## From DFA to BDD

Encode each column value `c_i ∈ {1..h}` in `⌈log_2 h⌉` Boolean variables, giving `w · ⌈log_2 h⌉` variables total in a column-by-column ordering (variables for `c_1` above variables for `c_2`, and so on). At a column boundary a BDD node is fixed by the DFA state. Inside a column, after `t` of its `b = ⌈log_2 h⌉` bits are read, a node is fixed by the bits read so far and by how the DFA state compares with the `2^{b−t}` values still possible for the column, which gives `O(h · b)` nodes per column, so

```
|BDD|  =  O(h · w · log h)
```

Measured on the reduced BDD, the growth per added column is `28, 90, 248, 630` nodes at `h = 4, 8, 16, 32`, the `h · log h` rate.[^3]

The number of satisfying assignments of that BDD, computed in one pass over its nodes, is `A^e(w, h)`. That pass is linear in `w`, like the direct extractor of [[castle-count-algorithms](pages/castle-count-algorithms.md)]; the Kitamasa path there is logarithmic in `w` and is the practical route at `w = 10^12`. The BDD is another encoding of the same DFA, with the affordances listed below.[^4]

## Worked example: `(w, h) = (3, 2)`

At `h = 2` the state space has at most `4 · 2 - 1 = 7` reachable states. A BFS from `s_0` reaches six (one bookkeeping combination is empty at `h = 2` because a run of `1`s always ends at `blocks = 1`, so `(c = 1, b = 0, r = 0)` never appears):[^5]

| state         | on `c = 1`        | on `c = 2`        |
|:--------------|:------------------|:------------------|
| `s_0`         | `(1, 1, 0)`       | `(2, 0, 1)`       |
| `(1, 1, 0)`   | `(1, 1, 0)`       | `(2, 0, 1)`       |
| `(2, 0, 1)`   | `(1, 0, 1)`       | `(2, 0, 1)`       |
| `(1, 0, 1)`   | `(1, 0, 1)`       | `(2, 1, 1)`       |
| `(2, 1, 1)`   | `(1, 1, 1)`       | `(2, 1, 1)`       |
| `(1, 1, 1)`   | `(1, 1, 1)`       | `(2, 0, 1)`       |

Accept states are those with `r = 1 and b = 0`: `(1, 0, 1)` and `(2, 0, 1)`. Counting the paths of length three from `s_0` that end in an accept state gives `A^e(3, 2) = 6`, the six castles of [[castle-native-gray-tour](pages/castle-native-gray-tour.md)].

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

A BDD represents a Boolean function; a **zero-suppressed BDD** represents a *family of sets*.[^6] The two structures are related but the ZDD reduction rule is different (an `x`-node whose HI branch is `F` is deleted, rather than an `x`-node whose LO and HI branches are equal). The ZDD reading of `V(w, h)` is: each castle `c` becomes a set of "column-choice" atoms (one atom per `c_i = a` pair, so `w · h` possible atoms total); `V(w, h)` is the family of atom-sets that satisfy the two filters. With the atoms in column order, the node at atom `(i, a)` is fixed by the DFA state before column `i` (the atoms `(i, 1), …, (i, a−1)` were all skipped), so this ZDD has at most `4h` nodes per atom level and `O(w · h²)` nodes in all.

Under this reading, the ZDD synthesis primitives from TAOCP §7.1.4 p. 251 - conjunction `∧`, disjunction `∨`, symmetric difference `⊕` - operate on ZDDs the way Boolean operations operate on Boolean functions: given a ZDD for `V(w, h)` and one for a castle family, such as the convex castles ([[castle-classification](pages/castle-classification.md)]), one `∧` gives the ZDD of the intersection, at a cost of at most the product of the two sizes, and the count of the result is one pass.

## Affordances beyond counting

The ZDD gives four operations on `V(w, h)`. The first three also run directly on the DFA's completion counts, as the transfer-matrix sampler and rank/unrank on [[castle-samplers](pages/castle-samplers.md)] do; the fourth needs a ZDD for the other family.

- **Counting** `A^e(w, h)` in `O(|ZDD|)`, one pass.
- **Uniform random sampling** of `V(w, h)` in `O(|ZDD|)` per sample, by top-down descent weighted by the number of accepting completions at each branch (the per-node solution counts of Knuth's Algorithm C, p. 251).
- **Rank / unrank** - a bijection `V(w, h) ↔ {1, …, A^e(w, h)}` in `O(|ZDD|)` per query, used for indexed enumeration ([[castle-samplers](pages/castle-samplers.md)], [[song-as-castle](pages/song-as-castle.md)]).
- **Restricted counts** - for a castle family with its own ZDD, one `∧` gives the intersection with `V` and one count gives its even-block castles, `A^e_X(w, h)` ([[castle-classification](pages/castle-classification.md)]).

Knuth notes on p. 251 that ZDDs beat BDDs when every set in the family is small (`νx` small whenever `f(x) = 1`). In the atom reading each castle uses `w` of the `w · h` atoms, so that is the regime of large `h`.

## Scale precedents from TAOCP §7.1.4

Knuth's examples on pp. 251 and 254, quoted from the same copy; the two counts are `A004003(4)`, the domino tilings of the `8 × 8` square, and `A007764(8)`, the corner-to-corner self-avoiding paths on the `8 × 8` grid of points (both checked on oeis.org):

| family                                             | Boolean vars | ZDD size          | count               |
|:---------------------------------------------------|-------------:|------------------:|--------------------:|
| Tilings of the 8x8 chessboard by dominoes          |          112 |             2,300 |          12,988,816 |
| Independent sets of the contiguous-USA graph       |           49 |    177 (sifted 160) |               —     |
| Simple paths corner-to-corner on the 8x8 grid `P_8 ⊡ P_8` | 112 |            33,580 |     789,360,053,252 |

The castle diagrams have `O(h)` nodes per variable level because the castle automaton has `O(h)` states.

## Entities & Concepts

- [[castle-strip](pages/castle-strip.md)] - the `h × h` transfer matrix on column heights this page extends into a DFA on `(c, b, r)`.
- [[castle-count-algorithms](pages/castle-count-algorithms.md)] - the rational-function and Kitamasa computation of `A^e(w, h)`; the ZDD count is linear in `w`, like the direct extractor there, where Kitamasa's method is logarithmic.
- [[castle-representations](pages/castle-representations.md)] - the encodings this page adds to.
- [[castle-classification](pages/castle-classification.md)] - restriction axes that can be intersected with `V` as ZDDs.
- [[project-euler-502-brute-force](pages/project-euler-502-brute-force.md)] - the column-height block-count formula the DFA transition uses.

## Related Concepts

- [[castle-counting-formula](pages/castle-counting-formula.md)] - the closed form `A^e = (A + S)/2`; the ZDD counts `A^e` directly, without the split into `A` and the signed count `S`.
- [[song-as-castle](pages/song-as-castle.md)] - rank / unrank on proper castles, the kind of bijection a ZDD's rank operation gives.
- [[castle-gray-code](pages/castle-gray-code.md)], [[castle-native-gray-tour](pages/castle-native-gray-tour.md)] - walking orders on the cube and on `V(w, h)`.
- [[castle-entropy](pages/castle-entropy.md)] - `log₂ A^e = log₂ A − 1 + log₂(1 + S/A)`, the number of bits of a ZDD rank.
- [[castle-samplers](pages/castle-samplers.md)] - the top-down sampling and rank/unrank of this page implemented on the automaton, with exactness checked in rational arithmetic.

## Footnotes

[^1]: Knuth, *The Art of Computer Programming* Vol. 4A §7.1.4, "Binary Decision Diagrams" (pp. 202-280; quoted from a copy that is not in the repository and was not re-read). BDDs are introduced on p. 202 as "Reduced Ordered Binary Decision Diagrams": ordered means every root-to-sink path visits the variables in a fixed order, reduced means no two nodes have the same `(V, LO, HI)` and no node has `LO = HI`. ZDDs are introduced on p. 249, credited to Shin-ichi Minato (1993), with the reduction rule "an `x`-node whose HI branch is the `⊥` sink is deleted"; p. 250 gives the family-of-sets reading: "The root node of a ZDD names the smallest element that appears in at least one of the sets; its HI and LO branches represent the residual subfamilies that do and don't contain that element."
[^2]: The block-count formula `blocks = c_1 + ∑_{i≥2} max(0, c_i - c_{i-1})` is verified on [[project-euler-502-brute-force](pages/project-euler-502-brute-force.md)] against the run-based definition for all skylines `w, h ≤ 6`; the DFA transition `(c, b, r) →_a (a, b ⊕ [max(0, a - c) mod 2], r ∨ [a = h])` is that formula read one column at a time. The `r = 0 ⟹ c ≤ h - 1` constraint holds because `r` is `1` iff some read column equals `h`, and if the *last* column is `h` then in particular some column equals `h`.
[^3]: Verified by execution (Python 3.11, 2026-10-16): the reduced ordered BDD built by memoized recursion over (column, bit, automaton state, bits read), with the column bits most significant first and the values `h, …, 2^b − 1` of a column sent to the false sink, has `199, 479` branch nodes at `w = 10, 20` for `h = 4`, `641, 1541` for `h = 8`, `1759, 4239` for `h = 16` and `4437, 10737` for `h = 32`, and 5 at `(3, 2)`; the reachable non-initial automaton states number `4h − 2` for `3 ≤ h ≤ 8` and 5 at `h = 2`.
[^4]: On [[castle-count-algorithms](pages/castle-count-algorithms.md)] the rational-function path costs `O(D² log w)` by Kitamasa's method or `O(w · D)` by direct extraction, with `D = h` the degree of `den_{h−1}`, and the Berlekamp-Massey path in the tower height uses a recurrence of order `2w − 2`, computed for `4 ≤ w ≤ 12`; the BDD count costs `O(h · w · log h)`, linear in `w`.
[^5]: Verified by execution (Python 3.11, 2026-10-16): the `(3, 2)` automaton reached from `s_0` by the transition rule of footnote 2, its transition table, the reduced BDD with five branch nodes, and `A^e(3, 2) = 6` from the six accepted tuples; the excluded tuples are `(1, 1, 1)` (height 1) and `(2, 1, 2)` (3 blocks).
[^6]: Knuth, TAOCP Vol. 4A §7.1.4 pp. 249-260, the ZDD subsection (same copy, not re-read). The synthesis primitives are described on p. 251: "When we know the ZDDs for `f` and `g`, we can synthesize them to obtain the ZDDs for `f ∧ g, f ∨ g, f ⊕ g,` etc., using algorithms that are very much like the methods we've used for BDDs. Furthermore we can count and/or optimize the solutions of `f`, with analogs of Algorithms C and B." The examples of the section *Scale precedents from TAOCP §7.1.4* are from pp. 251 and 254.
