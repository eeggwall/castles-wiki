---
title: Diffusion on tree castles
category: Concepts
summary: The graph of a tree castle is a comb, with the bottom row as the backbone and the cells above row 1 of each column as a tooth, and a castle's graph is a comb only when the castle is a tree castle; so "castle comb" names a tree castle seen as a medium for diffusion, and there is no separate family of comb castles. For the simple random walk on the castle graph, the horizontal moves are the simple random walk on the backbone reflected at the end columns, so the mean-square displacement of the walker's column equals the expected number hor(t) of horizontal moves until the walk can reach an end column. A stationary step is horizontal with probability rate(c) = (w − 1)/(n − 1) = (w − 1)/(w + b − 2), with n cells and b blocks, the coefficient of normal diffusion that the comb papers compute. On the battlement, which alternates columns of heights 1 and h, the displacement grows like (4√(2/π) + o(1))√t while the teeth look infinite, the order-1/2 regime of the comb equation of Arkhincheev and Baskin, and like 2t/(h + 1) at long times; the two asymptotes meet at t = 8(h + 1)²/π. On a castle the order-1/2 regime is a window: the teeth have at most h − 1 cells, and the shape sets where the window closes and the long-time rate. The rate depends on the skyline, not only the graph: the six skylines with one graph in isospectral-castles have rates 1/2 to 4/5.
tags: [concept, castle, tree-castle, comb, random-walk, anomalous-diffusion, subdiffusion, fractional-calculus, mean-square-displacement, battlement, block-count, castle-graph, verification]
sources: [arkhincheev-baskin-1991-comb-model, mendez-iomin-campos-horsthemke-2015-random-walks-on-combs, yuste-abad-baumgaertner-2016-random-comb-model, pach-tardos-2013-range-of-random-walk-on-comb]
created: 2026-10-29
updated: 2026-10-29
---

# Diffusion on tree castles

## Tree castles are combs

A castle of width `w` and height `h` is a skyline `(c_1, …, c_w)` with `1 ≤ c_i ≤ h` and some `c_i = h` ([[castle-polyomino](pages/castle-polyomino.md)]). Its graph has the cells as vertices and an edge between two cells that share a side, and a **tree castle** is a castle whose graph is a tree, which happens exactly when no two neighboring columns both have height at least 2 ([[castle-graph](pages/castle-graph.md)], section *Tree castles*).

**Theorem 1.** The graph of a castle is a comb, the path of the `w` cells of row 1 with the `c_i − 1` cells above row 1 of column `i` as a vertical path standing on its `i`-th cell, exactly when the castle is a tree castle.

*Proof.* In every castle the edges of row 1 and the edges inside the columns form a spanning tree, a comb whose teeth are the columns, and each further edge joins two neighboring columns above row 1 and closes one `2 × 2` square ([[castle-graph](pages/castle-graph.md)], the proof that the squares are an integer basis of the cycles). A castle has no such edge exactly when no two neighboring columns both have height at least 2. ∎

The path of row 1 is the **backbone**, and the `c_i − 1` cells above row 1 of column `i` are its **tooth**, empty when `c_i = 1`; the backbone and the teeth are the words of the comb papers.[^pt-teeth] So a **castle comb** is a tree castle, read as a medium for diffusion, and there is no separate family of comb castles. Theorem 1 agrees with brute force on every castle with `w ≤ 8` and `h ≤ 5`, 4,824 of them tree castles.[^exec1]

**How a castle comb differs from the comb of the papers.** The combs of the sources have a tooth at every site of an unbounded backbone, on both sides in Pach and Tardos and in Méndez et al. and on one side in Yuste et al., and in the basic model the teeth are unbounded.[^combs] A castle comb is finite: `w` backbone cells and teeth of at most `h − 1` cells. Its teeth stand on one side, and never on neighboring backbone cells, since two neighboring teeth would close a `2 × 2` square. So a castle comb carries a tooth on at most every other backbone cell, and a **battlement**, which alternates columns of heights 1 and `h`, carries one of `h − 1` cells on every other cell; the battlements are tree castles ([[castle-avalanches](pages/castle-avalanches.md)]).

**What the tree-castle pages give.** Counting castle combs is counting tree castles: `A_tree(w, h) = T_h(w) − T_{h−1}(w)` with `T_h(w + 2) = T_h(w + 1) + (h − 1)T_h(w)`, growing like `((1 + √(4h − 3))/2)^w` ([[castle-graph](pages/castle-graph.md)]), and by area in [[tree-castle-by-area](pages/tree-castle-by-area.md)]. A tree castle with `n` cells has `b = 1 + n − w` blocks ([[castle-graph](pages/castle-graph.md)], Equation (3)): one for the backbone and one for each tooth cell. Every tree castle also has one spanning tree, a trivial sandpile group ([[sandpile-group](pages/sandpile-group.md)]) and the Ramanujan property ([[ramanujan-castles](pages/ramanujan-castles.md)]); none of these enters the walk below.

## Notation used on this page

| symbol | meaning |
|---|---|
| `n`, `w`, `b` | the number of cells, the width and the number of blocks of a castle `c` |
| `d(v)` | the number of neighbors of the cell `v` |
| `col(t)` | the column of the walker after `t` steps |
| `hor(t)` | the number of horizontal steps among the first `t` steps |
| `msd(t)` | the mean-square displacement `E[(col(t) − col(0))²]` |
| `rate(c)` | `(w − 1)/(n − 1)`, the probability that a stationary step is horizontal |
| `stat(v)` | the stationary probability of the cell `v` |

## The walk and its horizontal moves

The walk on a castle is the simple random walk on its graph: from a cell `v` it moves to each of the `d(v)` neighbors with probability `1/d(v)`, which is how Pach and Tardos define the random walk on a graph.[^pt-walk] In a tree castle every horizontal edge lies in row 1, so a step changes the column exactly when it runs along the backbone.

**Theorem 2.** In a tree castle of width `w ≥ 2`, the columns at the horizontal steps form the simple random walk on `1, …, w` reflected at the ends: from column `i`, `1 < i < w`, the next horizontal step goes to `i − 1` or `i + 1` with probability 1/2 each, from column 1 to 2 and from column `w` to `w − 1`. If the walk starts in column `i_0` and `d = min(i_0 − 1, w − i_0)` is the distance to the nearer end column, then

```
msd(t)  =  E hor(t)        for 0 ≤ t ≤ d.        (1)
```

*Proof.* A horizontal step leaves from a backbone cell. From the backbone cell of column `i` the walk moves to each horizontal neighbor with probability `1/d(v)`, or into the tooth, a path hanging from that cell, from which it can only come back to it. So the next horizontal step goes to each horizontal neighbor with the same probability, whatever happened before. This is the reduction of Pach and Tardos, who drop the steps that do not change a coordinate and obtain a standard random walk on the line for each projection.[^pt-reduce] For (1), let `Y_k` be the column after the `k`-th horizontal step, `Y_0 = i_0`. Each of the first `d` horizontal steps leaves from a column at distance at most `d − 1` from `i_0`, which is not an end column, so `(Y_k − i_0)² − k` is a martingale up to `k = d`. Up to time `t ≤ d` the walk makes `hor(t) ≤ d` horizontal steps, and `hor(t)` is a stopping time for them, so optional stopping gives `E[(Y_{hor(t)} − i_0)²] = E hor(t)`, and `Y_{hor(t)} = col(t)`. ∎

Equation (1) is exact on all eight tree castles of width 13 tested from the foot of column 7, where `d = 6`, and fails first at `t = 7` on each of them.[^exec2] On a comb that repeats without end in both directions, such as an extended battlement, no column is an end and (1) holds for every `t`.

**Theorem 3.** In a tree castle with `n ≥ 2` cells, `stat(v) = d(v)/(2(n − 1))` is a stationary distribution of the walk, and a stationary step is horizontal with probability

```
rate(c)  =  (w − 1)/(n − 1)  =  (w − 1)/(w + b − 2).        (2)
```

So `E_stat hor(t) = t · rate(c)` for every `t`, for the walk started from `stat`.

*Proof.* A tree with `n` cells has `n − 1` edges, so `Σ_v d(v) = 2(n − 1)`. For each cell `v`, `Σ_{u ~ v} stat(u)/d(u) = d(v)/(2(n − 1)) = stat(v)`, so `stat` is stationary. A stationary step runs along each of the `2(n − 1)` directed edges with probability `stat(v)/d(v) = 1/(2(n − 1))`, and `2(w − 1)` of them are horizontal. The second form of (2) uses `n − w = b − 1`. ∎

From the bottom-left cell, `E hor(t)/t` at `t = 10^7` agrees with `rate(c)` to `10^{−5}` on the four castles tested, as the ergodic theorem for a walk on a finite connected graph predicts.[^exec3] Since `w + b` is the semi-perimeter `s` of [[castle-perimeter](pages/castle-perimeter.md)], `rate(c) = (w − 1)/(s − 2)`. At a fixed width each block beyond the first is one more tooth cell and lowers the rate, from `(w − 1)/(w + b − 2)` to `(w − 1)/(w + b − 1)`.

**The coefficients of the comb papers are this count.** On the comb of Méndez et al., with branches of `N` nodes crossing the backbone at every node, the unbiased walk with one time unit per step has `⟨t⟩ = 1 + 2N` and `D = 1/(2⟨t⟩)` by their Equations (3.3) and (3.7), so `x²(t) = 2Dt = t/(1 + 2N)`: one horizontal edge among the `1 + 2N` edges of a period.[^mendez] On the comb of Yuste et al. with a tooth of `ℓ` cells at every site, a walker at the foot of a tooth that enters it with probability `θ = 1/3` and steps back at its end makes a backbone step after `τ(ℓ) = 1 + θ t_R(ℓ)/(1 − θ) = 1 + ℓ` steps on average, with `t_R(ℓ) = 2ℓ`, so `⟨x²⟩ = t/(1 + ℓ)`, one horizontal edge among `1 + ℓ`.[^yuste-tau] Arkhincheev and Baskin give `⟨x²(t)⟩ ∝ D_1 t/L` for ribs of average length `L`.[^ab-finite] The same computation as for castles reproduces both exact coefficients.[^exec6]

## The battlement: the order-1/2 window

On the battlement extended in both directions, the walk on each period is the same, and `msd(t) = E hor(t)` for every `t` by Theorem 2, checked for `h = 2, 3, 7` and `t ≤ 300`.[^exec5] A battlement of finite width started in the middle has exactly the same walk up to time `d`, the distance to the nearer end column, because up to then the walk only uses cells that are not in an end column.

**Proposition 4.** On the extended battlement, started at a cell of height 1:

- `E hor(t)/t → 2/(h + 1)`;
- if the teeth are unbounded, `E hor(t) = (4√(2/π) + o(1)) √t`.

*Proof.* Reduced to one period, the walk moves on `h + 1` cells joined by `h + 1` edges, the two horizontal edges between the cell of height 1 and the foot of the tooth and the `h − 1` edges of the tall column, and the count in the proof of Theorem 3 gives the first part. For the second, follow Pach and Tardos's Lemma 2 and stop the walk at its `n`-th vertical move.[^pt-lemma2] Without the horizontal moves, the vertical moves are the simple random walk on `0, 1, 2, …` reflected at 0, since from the bottom row the only vertical move is up and inside an unbounded tooth both vertical moves have probability 1/2. Its visits to 0 are those of the simple random walk on the line, `(√(2/π) + o(1)) √n` on average in `n` steps by their Equation (2). At each visit the walker stands at the foot of a tooth, where with probability 2/3 it makes two horizontal moves, to a cell of height 1 and on to the foot of a tooth, and with probability 1/3 it enters the tooth; so it makes `2j` horizontal moves with probability `(2/3)^j/3`, 4 on average, independently of the vertical walk. With the first move from the start cell, the walk makes `1 + 4(√(2/π) + o(1)) √n` horizontal moves on average up to its `n`-th vertical move. These are `O(√n)` moves, so, as Pach and Tardos pass from vertical moves to steps, the count at time `t` is `(4√(2/π) + o(1)) √t`. ∎

With teeth of `h − 1` cells the walk is the same as with unbounded teeth until the walker reaches the top of a tooth, at least `h` steps after the start, and the computed displacement follows `4√(2t/π)` until `t` is of the order of `h²`. The two asymptotes `4√(2t/π)` and `2t/(h + 1)` are equal at

```
t  =  8(h + 1)²/π.        (3)
```

At this time the computed `msd(t)` is 1.25 to 1.26 times their common value, and its local exponent `d ln msd/d ln t` is 0.79 to 0.80, for `h = 101, 1001` and `2001`. At `h = 1001`, where (3) is `2.557 · 10^6`, with the local exponent taken over a factor 1.1 on either side:[^exec5]

| `t` | `msd(t)` | local exponent | `msd(t)/(4√(2t/π))` | `msd(t) (h + 1)/(2t)` |
|---|---|---|---|---|
| `10^2` | 25.9197 | 0.5977 | 0.8121 | 129.8575 |
| `10^3` | 94.2522 | 0.5337 | 0.9339 | 47.2203 |
| `10^4` | 312.258 | 0.5109 | 0.9784 | 15.6441 |
| `10^5` | 1002.29 | 0.5035 | 0.9931 | 5.0215 |
| `10^6` | 3319.06 | 0.6104 | 1.0400 | 1.6629 |
| `10^7` | 21289.1 | 0.9375 | 2.1094 | 1.0666 |
| `10^8` | 200930 | 0.9934 | 6.2957 | 1.0067 |
| `10^9` | `1.99734 · 10^6` | 0.9993 | 19.7903 | 1.0007 |

So the comb equation of Arkhincheev and Baskin, whose time derivative has order 1/2 and whose displacement grows like `t^{1/2}`, is derived for ribs going to infinity and describes a castle comb only inside the window `1 ≪ t ≪ h²`.[^ab-order] After the window the castle comb diffuses normally, as Arkhincheev and Baskin and Méndez et al. state for finite ribs, at the rate (2).[^ab-finite][^mendez] The exponent 1/2 needs teeth longer than the walker's excursions into them; what the shape of the castle sets is where the window closes, near `(h + 1)²`, and the long-time rate. On a castle of finite width `msd(t) ≤ (w − 1)²`, since the column stays in `1, …, w`, so the normal regime ends too.

## Other tooth lengths

Yuste et al. restate the exponents of the random comb, teeth drawn independently with `P(ℓ) ∼ ℓ^{−(1+α)}`: `⟨x²⟩ ∼ t^{(1+α)/2}` for `0 < α < 1`, `t/ln t` at `α = 1` and normal diffusion for `α > 1`.[^yuste-exp] A tree castle of height `h` has teeth of at most `h − 1` cells, so every tooth-length distribution on castles of bounded height has a finite mean, the side of normal diffusion, and on a wide tree castle the spreading after the window is normal, at the rate (2), until the width stops it. The exponents `(1 + α)/2 < 1` need teeth of unbounded length; on castles they can appear only as windows along a family whose height grows. A castle with a `2 × 2` square is not a comb, since the walker can change column above row 1, and Theorem 2 does not apply to it.

## The skyline, not the graph

The walk depends only on the graph, but `col(t)`, `hor(t)` and `rate(c)` depend on which edges are horizontal, and the skyline decides that. The six skylines of class `A` in [[isospectral-castles](pages/isospectral-castles.md)], `(1,1,1,2,1,1,2,1,1)`, `(1,1,1,2,1,1,3,1)`, `(1,1,2,1,1,2,1,2)`, `(1,1,2,1,1,4,1)`, `(1,3,1,1,2,1,2)` and `(1,3,1,1,4,1)`, have one graph and widths 9, 8, 8, 7, 7 and 6, so their rates are `4/5`, `7/10`, `7/10`, `3/5`, `3/5` and `1/2`; each lays the same tree out with a different path as its bottom row. The castle `B = (1,1,3,1,1,1,2,1)`, which has the same Laplacian spectrum as `A` and another graph, has rate `7/10`, the rate of two skylines of class `A`, so the rate does not separate the pair either.[^exec7]

## Related Concepts

- [[castle-graph](pages/castle-graph.md)] - the castle graph, the tree castles, the comb spanning tree of every castle, and the counts and the block count of the tree castles.
- [[tree-castle-by-area](pages/tree-castle-by-area.md)] - the tree castles counted by area.
- [[castle-perimeter](pages/castle-perimeter.md)] - the semi-perimeter `s = w + b`, in which the rate is `(w − 1)/(s − 2)`.
- [[castle-avalanches](pages/castle-avalanches.md)] - the battlements, tree castles with a tooth of `h − 1` cells on every other column.
- [[isospectral-castles](pages/isospectral-castles.md)] - the 11-cell pair `A`, `B` and the six skylines of class `A`.
- [[levy-flights](pages/levy-flights.md)] - the space-fractional Laplacian of the castle graph, long jumps instead of trapping in teeth.
- [[castle-notation](pages/castle-notation.md)] - `hor(t)`, `msd(t)` and `rate(c)`.
- [[half-derivative-seminar](pages/half-derivative-seminar.md)] - a seminar on castle operations at order 1/2, of which this page is the last stop.
- [[arkhincheev-baskin-1991-comb-model](pages/arkhincheev-baskin-1991-comb-model.md)], [[mendez-iomin-campos-horsthemke-2015-random-walks-on-combs](pages/mendez-iomin-campos-horsthemke-2015-random-walks-on-combs.md)], [[yuste-abad-baumgaertner-2016-random-comb-model](pages/yuste-abad-baumgaertner-2016-random-comb-model.md)], [[pach-tardos-2013-range-of-random-walk-on-comb](pages/pach-tardos-2013-range-of-random-walk-on-comb.md)] - the comb model, its order-1/2 equation, its coefficients and its reduced projections.

## Footnotes

[^pt-teeth]: [[pach-tardos-2013-range-of-random-walk-on-comb](pages/pach-tardos-2013-range-of-random-walk-on-comb.md)] §3 p.3 L125-L127 - "The vertices and edges of the comb C2 that belong to the x-axis form the backbone. The connected components of the graph obtained from C2 after the removal of the backbone are called teeth."
[^combs]: [[pach-tardos-2013-range-of-random-walk-on-comb](pages/pach-tardos-2013-range-of-random-walk-on-comb.md)] §1 p.1 L34-L36 - "The 2-dimensional comb C2 is a spanning tree of the integer grid Z2 obtained by removing all of its "horizontal" edges (that is, edges parallel to the x-axis) that do not belong to the x-axis."; [[mendez-iomin-campos-horsthemke-2015-random-walks-on-combs](pages/mendez-iomin-campos-horsthemke-2015-random-walks-on-combs.md)] §II p.2 L99-L102 - "identical branches that cross the backbone perpendicularly at each node"; [[yuste-abad-baumgaertner-2016-random-comb-model](pages/yuste-abad-baumgaertner-2016-random-comb-model.md)] §II pp.6-7 L222-L224 - "We attached a tooth of integer length ℓk = ⌊r^{−α}⌋ to each backbone site k"; [[arkhincheev-baskin-1991-comb-model](pages/arkhincheev-baskin-1991-comb-model.md)] p.161 L60-L61 - "FIG. 1. Comb structure: the conducting axis (y = 0) has ribs going to infinity."
[^pt-walk]: [[pach-tardos-2013-range-of-random-walk-on-comb](pages/pach-tardos-2013-range-of-random-walk-on-comb.md)] §1 p.1 L27-L30 - "To obtain a random walk in a locally finite graph G with vertex set V(G), we start at any vertex v ∈ V(G) and in the next step we move to one of its neighbors, independently of all previous events, with probability 1/d(v)."
[^pt-reduce]: [[pach-tardos-2013-range-of-random-walk-on-comb](pages/pach-tardos-2013-range-of-random-walk-on-comb.md)] §3 p.3 L128-L133 - "First, we reduce these one-dimensional walks by getting rid of the steps when the value does not change. In this way, horizontal steps contribute only to the reduced projection (Xi′) and vertical steps contribute only to the reduced projection (Yi′). Note that with probability 1 both reduced walks are infinite and they are distributed as the standard random walk on the line."
[^pt-lemma2]: [[pach-tardos-2013-range-of-random-walk-on-comb](pages/pach-tardos-2013-range-of-random-walk-on-comb.md)] §§2-3 pp.3-4 L106-L116, L133-L160 [synthesis] - Equation (2), `E[A_n] = Σ_{m≤n} p_{m,0} = (√(2/π) + o(1))√n`; "Let us consider the random walk on the comb up to (and including) the nth vertical move."; Lemma 2 and "W has d chances to make horizontal moves. At each chance, it makes precisely i consecutive horizontal moves with probability 2^{−i−1}."; and p.6 L311-L313, "our estimates for the expectation of Vn′ carry over to the expectation of Vn, as |Vn′ − Vn| ≤ a and E[a] = O(√n)".
[^mendez]: [[mendez-iomin-campos-horsthemke-2015-random-walks-on-combs](pages/mendez-iomin-campos-horsthemke-2015-random-walks-on-combs.md)] §III.A pp.4-5 L276-L318 - "If the random walk inside the branches is isotropic, q = 1/2, one obtains by the L'Hopital's rule from (3.2) lim_{q→1/2} ⟨t⟩ = (1 + 2N) t̄."; "the MSD along the backbone corresponds to normal diffusion x²(t) = 2Dt. The diffusion coefficient is given by D = a²/(2⟨t⟩)"; "The transport is diffusive for finite N, regardless q and the specific form of φ0(τ), as long as it has finite moments."
[^yuste-tau]: [[yuste-abad-baumgaertner-2016-random-comb-model](pages/yuste-abad-baumgaertner-2016-random-comb-model.md)] §IV.C pp.16-18 L677-L747 [synthesis] - Equation (24), `D_0 = Σ²/τ`; Equation (26), `τ(ℓ) = 1 + θ t_R(ℓ)/(1 − θ)`, with θ the probability of entering the tooth; "this boundary condition corresponds to treating a tooth of length ℓ like a ring with 2ℓ sites. Correspondingly, one has tR(ℓ) = 2ℓ"; `Σ² = 1` for nearest-neighbor backbone steps (L735-L737).
[^ab-finite]: [[arkhincheev-baskin-1991-comb-model](pages/arkhincheev-baskin-1991-comb-model.md)] §2.1 p.163 L141-L148 - "The transition to the conventional diffusion also occurs when the average length of the ribs L is finite. Then, for long times t ≫ L²/D2, we obtain ⟨x²(t)⟩ ∝ D1t/L." (the formula read from the page image).
[^ab-order]: [[arkhincheev-baskin-1991-comb-model](pages/arkhincheev-baskin-1991-comb-model.md)] §2.1 p.162 L64-L139 [synthesis] - Equation (10), `⟨x²(t)⟩ = D_1 (πt/D_2)^{1/2}`, and Equation (14), `(∂^{1/2}/∂t^{1/2} − (D_1/(2D_2^{1/2})) ∂²/∂x²) n(x, 0, t) = 0`, read from the page image, for the comb of Figure 1, whose ribs go to infinity.
[^yuste-exp]: [[yuste-abad-baumgaertner-2016-random-comb-model](pages/yuste-abad-baumgaertner-2016-random-comb-model.md)] §II p.6 L208-L216 - "the length ℓ may be chosen independently for each tooth by drawing its value from a distribution whose asymptotic behavior is P(ℓ) ∼ ℓ^{−(1+α)}, where α > 0"; "the system exhibits anomalous subdiffusion along the backbone axis for 0 < α < 1, i.e., one has ⟨x²(t)⟩ ∼ t^γ with γ = (1 + α)/2. In contrast, for α > 1 there is a crossover to normal diffusion, that is, ⟨x²(t)⟩ ∼ t. At the crossover value α = 1 there is a logarithmic correction, and hence ⟨x²(t)⟩ ∼ t/ln(t)."
[^exec1]: Verified by execution (Python 3.11, 2026-10-29): `bin/python/tree_castle_diffusion.py` item [1], run log `bin/python/tree_castle_diffusion-run.log`. For every castle with `w ≤ 8` and `h ≤ 5`: the graph of each of the 4,824 tree castles is its backbone and teeth, with `b = 1 + n − w`; each of the 483,456 other castles contains them as a proper spanning tree, with one more edge per `2 × 2` square.
[^exec2]: Verified by execution (Python 3.11, 2026-10-29): `bin/python/tree_castle_diffusion.py` items [3] and [4], run log `bin/python/tree_castle_diffusion-run.log`. The direction of the next horizontal step, solved exactly in rational arithmetic from every column of the 888 tree castles with `2 ≤ w ≤ 7` and `h ≤ 4`; the exact distributions of eight tree castles of width 13 with random columns of heights 1 to 5 at odd positions and 1 at even ones, from the foot of column 7, for `t ≤ 10`.
[^exec3]: Verified by execution (Python 3.11 with NumPy, 2026-10-29): `bin/python/tree_castle_diffusion.py` item [2], run log `bin/python/tree_castle_diffusion-run.log`. Stationarity of `stat` and the one-step probability (2), exactly, on the 892 tree castles with `w ≤ 7` and `h ≤ 4`; `E hor(10^7)/10^7` from the cell `(1, 1)` of `(1, 3, 1, 1, 4, 1)`, `(2, 1, 2, 1, 2)`, `(1, 1, 1, 2, 1, 1, 2, 1, 1)` and `(5, 1, 1, 3, 1, 2, 1, 1, 4)`, from the spectrum of the walk.
[^exec5]: Verified by execution (Python 3.11 with NumPy, 2026-10-29): `bin/python/tree_castle_diffusion.py` item [5], run log `bin/python/tree_castle_diffusion-run.log`. The joint distribution of cell and displacement on the extended battlement for `h = 2, 3, 7`, `t ≤ 300`, against `E hor(t)`; `E hor(t)` from the spectrum of the walk on one period, a path of `h + 1` cells, for `h = 11, 101, 1001, 2001` and `t` up to `10^9`; the slope of `E hor(t)` in `√t` between `t = 10^4` and `10^5` at `h = 2001`, `3.19121`, against `4√(2/π) = 3.19154`, with `E hor(t) − 4√(2t/π)` near `−7` at `t = 10^3, 10^4, 10^5`.
[^exec6]: Verified by execution (Python 3.11 with NumPy, 2026-10-29): `bin/python/tree_castle_diffusion.py` item [6], run log `bin/python/tree_castle_diffusion-run.log`. The fraction of horizontal steps at `t = 10^8` equals `1/(1 + 2N)` for `N = 2, 3, 6, 20` and `1/(1 + ℓ)` for `ℓ = 1, 2, 5, 30`, to `10^{−6}`; with branches of 4000 nodes on both sides, the slope of `E hor(t)` in `√t` is `0.79788 = √(2/π)`, the infinite-branch law of Méndez et al. and the count of Pach and Tardos's Lemma 2.
[^exec7]: Verified by execution (Python 3.11 with NetworkX, 2026-10-29): `bin/python/tree_castle_diffusion.py` item [7], run log `bin/python/tree_castle_diffusion-run.log`. The six skylines of class `A` have isomorphic graphs, not isomorphic to that of `B`, and the rates `(w − 1)/(n − 1)` given.
