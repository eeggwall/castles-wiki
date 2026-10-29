---
title: "Pach and Tardos (2013) - The range of a random walk on a comb"
category: Sources
summary: Pach and Tardos prove that the simple random walk on the two-dimensional comb, the grid Z × Z without the horizontal edges off the x-axis, visits (1/(2√(2π)) + o(1)) √n log n distinct vertices on average in n steps (Theorem 1), against the n^{3/4} claimed by Weiss and Havlin. The proof drops the steps that do not change a coordinate: each reduced projection is the standard random walk on the line. Up to the n-th vertical move the walk makes (√(2/π) + o(1)) √n horizontal moves on average (Lemma 2), one run of mean length 1 at each of its visits to the backbone, and reaches Θ(n^{1/4}) backbone sites; the visited sites are then counted by their distance from the backbone. The introduction recalls that the horizontal deviation is roughly n^{1/4} and that a walker spends most of her time on a tooth.
tags: [source, paper, comb-model, random-walk, range, simple-random-walk, recurrence, tree-castle]
sources: [pach-tardos-2013-range-of-random-walk-on-comb]
created: 2026-10-29
updated: 2026-10-29
---

# Pach and Tardos (2013) - The range of a random walk on a comb

**Source:** `raw/pach-tardos-2013-range-of-random-walk-on-comb.pdf` (git-ignored) and its text layer `raw/pach-tardos-2013-range-of-random-walk-on-comb.txt` (tracked, extracted with `pdftotext -layout`). János Pach and Gábor Tardos, "The Range of a Random Walk on a Comb", arXiv:1309.6360v1 [math.PR], 24 September 2013, https://arxiv.org/abs/1309.6360; the journal version is in *The Electronic Journal of Combinatorics* 20(3) (2013), P59, https://www.combinatorics.org/ojs/index.php/eljc/article/download/v20i3p59/pdf. The arXiv version was the one read.[^1]
**Date ingested:** 2026-10-29
**Type:** paper (8 pp.)

## Notation used on this page

| paper | meaning | written here as |
|---|---|---|
| `C_2` | the two-dimensional comb | the same |
| `W_n = (X_n, Y_n)` | the position of the walker after `n` steps | the same |
| `V_n` | the number of vertices visited in the first `n` steps | the same |
| `X′_i`, `Y′_i` | the reduced projections, with the steps that do not change the coordinate removed | the same |
| `a`, `c`, `d` | for the walk `W` up to its `n`-th vertical move: the number of horizontal moves, of backbone sites reached, and of arrivals on the backbone | the same |
| `p_{n,i}`, `A_n` | for the walk on `Z`: the probability of being at `i` after `n` steps, and the number of visits to 0 in the first `n` steps | the same |

## Summary

**The walk and the comb.** "To obtain a random walk in a locally finite graph `G` with vertex set `V(G)`, we start at any vertex `v ∈ V(G)` and in the next step we move to one of its neighbors, independently of all previous events, with probability `1/d(v)`." The two-dimensional comb `C_2` is "a spanning tree of the integer grid `Z²` obtained by removing all of its 'horizontal' edges (that is, edges parallel to the `x`-axis) that do not belong to the `x`-axis"; its vertices have degree 2, except those on the `x`-axis, which have degree 4. The vertices and edges on the `x`-axis form the backbone, and the components left when it is removed are the teeth.[^2]

**History.** The study of random walks on the comb "was initiated by Weiss and Havlin [WeH86], as a model of 'anomalous diffusion on fractal structures'", and extended to higher-dimensional combs by Gerl and by Cassi and Regina. Krishnapur and Peres proved that two independent walkers on `C_2` meet only finitely often, although the walk is recurrent; the estimates of Bertacchi and Zucca and of Bertacchi "suggested that a walker spends most of her time moving vertically along a 'tooth' of the comb"; Csáki, Csörgő, Földes and Révész proved strong limit theorems. Almost surely the horizontal projection deviates by roughly `n^{1/4}` and the vertical projection by order `n^{1/2}`, which suggests `n^{1/4} · n^{1/2} = n^{3/4}` visited sites, as Weiss and Havlin stated.[^3]

**Theorem 1.** The expected number of vertices visited in the first `n` steps is

```
E[V_n]  =  ( 1/(2√(2π)) + o(1) ) √n log n,
```

which "contradicts a claim of Weiss and Havlin": "the truth is closer `n^{1/2}`, than to `n^{3/4}`."[^4]

**The reduced projections.** "we reduce these one-dimensional walks by getting rid of the steps when the value does not change. In this way, horizontal steps contribute only to the reduced projection `(X′_i)` and vertical steps contribute only to the reduced projection `(Y′_i)`. Note that with probability 1 both reduced walks are infinite and they are distributed as the standard random walk on the line." From the walk on `Z` the proof uses `p_{n,i} = C(n, (n + i)/2)/2^n`, the expected number of visits to 0 in `n` steps, `E[A_n] = Σ_{m≤n} p_{m,0} = (√(2/π) + o(1))√n` (2), the expected number of sites visited, `(2√(2/π) + o(1))√n` (3), and the probability `r_j = 1/(2j)` of reaching `j` before returning to 0 (4).[^5]

**Lemma 2.** For the walk `W` up to its `n`-th vertical move, the number `a` of horizontal moves and the number `c` of backbone sites reached satisfy

```
E[a]  =  ( √(2/π) + o(1) ) n^{1/2},        E[c]  =  Θ(n^{1/4}).
```

The walk arrives on the backbone `d` times, distributed as `A_{n−1}`, and "At each chance, it makes precisely `i` consecutive horizontal moves with probability `2^{−i−1}`", so `E[a] = E[d] = E[A_{n−1}]`. Given `a`, the number of backbone sites reached is distributed as the number of sites a walk on `Z` visits in `a` steps.[^6]

**The rest of the proof.** For the upper bound, the sites are classified as close (`|j| < n^{1/4}`), far (`|j| > 2n^{1/2} log^{1/2} n`) and intermediate; the close ones number `O(√n)` on average by Lemma 2, the far ones at most 1 by a Chernoff bound, and an intermediate site at height `j` is reached for the last time by a vertical move with probability at most `p_{i,j}/j`, which sums to `(√(2/π)/4 + o(1)) √n log n` (6). Lemma 3 bounds the probability `u_j` of reaching `(0, j)` by `O(n^{1/4} log n/(|j| + 1))`, and the matching lower bound comes from summing `q_{i,j} ≥ 2p_{i,j} r_j (1 − u_j)` (8) over `n^{1/4} log² n < j < n^{1/2}/log n`.[^7]

## The castle reading

The graph of a tree castle is a comb whose backbone is the bottom row and whose teeth stand on one side, at most `h − 1` cells tall ([[tree-castle-diffusion](pages/tree-castle-diffusion.md)]). The reduction of the projections applies to it: the horizontal moves of the simple random walk on a tree castle are the simple random walk on the backbone, reflected at the end columns, so the mean-square displacement of the walker's column equals the expected number of horizontal moves until the walk can reach an end. Lemma 2's count adapts to the battlement, which alternates columns of heights 1 and `h`: each return of the vertical reduced walk to the bottom row starts a run of horizontal moves of mean length 4 instead of 1, and the expected number of horizontal moves grows like `4√(2/π) √t` while the walker has not reached the top of a tooth.[^8]

## Key Takeaways

- **Theorem 1**: `E[V_n] = (1/(2√(2π)) + o(1)) √n log n` on the two-dimensional comb, against the `n^{3/4}` claimed by Weiss and Havlin.[^4]
- **The reduced projections are standard random walks on the line.**[^5]
- **Lemma 2**: `(√(2/π) + o(1)) √n` horizontal moves up to the `n`-th vertical move, and `Θ(n^{1/4})` backbone sites.[^6]

## Entities & Concepts

- [[tree-castle-diffusion](pages/tree-castle-diffusion.md)] - the reduced horizontal walk on a tree castle, and Lemma 2's count of horizontal moves on the battlement.

## Relation to Other Wiki Pages

[[mendez-iomin-campos-horsthemke-2015-random-walks-on-combs](pages/mendez-iomin-campos-horsthemke-2015-random-walks-on-combs.md)] treats the same comb with branches of finite length and finds the mean-square displacement `√(2t/π)` for infinite unbiased branches, the count of Lemma 2. [[arkhincheev-baskin-1991-comb-model](pages/arkhincheev-baskin-1991-comb-model.md)] also credits the model to Weiss and Havlin and rejects their Gaussian Green's function.

## Footnotes

[^1]: [[pach-tardos-2013-range-of-random-walk-on-comb](pages/pach-tardos-2013-range-of-random-walk-on-comb.md)] p.1 L1-L19, L37-L43 [synthesis] - the title "The Range of a Random Walk on a Comb", the authors "János Pach" (EPFL, Lausanne and Rényi Institute, Budapest) and "Gábor Tardos" (Rényi Institute, Budapest), "arXiv:1309.6360v1 [math.PR] 24 Sep 2013" and the abstract.
[^2]: [[pach-tardos-2013-range-of-random-walk-on-comb](pages/pach-tardos-2013-range-of-random-walk-on-comb.md)] §§1, 3 pp.1-3 L27-L36, L47, L125-L127 - "To obtain a random walk in a locally finite graph G with vertex set V(G), we start at any vertex v ∈ V(G) and in the next step we move to one of its neighbors, independently of all previous events, with probability 1/d(v)."; "The 2-dimensional comb C2 is a spanning tree of the integer grid Z2 obtained by removing all of its "horizontal" edges (that is, edges parallel to the x-axis) that do not belong to the x-axis. In this graph, all vertices (or "sites") (x, y) have degree 2, except for the vertices of the form (x, 0), which have degree 4."; "The vertices and edges of the comb C2 that belong to the x-axis form the backbone. The connected components of the graph obtained from C2 after the removal of the backbone are called teeth."
[^3]: [[pach-tardos-2013-range-of-random-walk-on-comb](pages/pach-tardos-2013-range-of-random-walk-on-comb.md)] §1 p.2 L49-L69 - "The study of random walks on the comb was initiated by Weiss and Havlin [WeH86], as a model of "anomalous diffusion on fractal structures.""; "Krishnapur and Peres [KrP04] proved that, on the 2-dimensional comb, with probability 1, two independent walkers meet only a finite number of times."; "whose asymptotic estimates suggested that a walker spends most of her time moving vertically along a "tooth" of the comb"; "It is not hard to see that almost surely the deviation of the horizontal projection Xn of the walk is roughly n^{1/4}, while the expected length of the vertical projection is of order n^{1/2}."
[^4]: [[pach-tardos-2013-range-of-random-walk-on-comb](pages/pach-tardos-2013-range-of-random-walk-on-comb.md)] p.1 L16-L19 and p.2 L61-L78 - "This contradicts a claim of Weiss and Havlin."; "According to the main result in [WeH86], the expected value of Vn is asymptotically proportional to n^{3/4}, for large n."; "The aim of this note is to show that the truth is closer n^{1/2}, than to n^{3/4}."; Theorem 1.
[^5]: [[pach-tardos-2013-range-of-random-walk-on-comb](pages/pach-tardos-2013-range-of-random-walk-on-comb.md)] §§2-3 pp.2-3 L80-L133 - Equations (1)-(4); "First, we reduce these one-dimensional walks by getting rid of the steps when the value does not change. In this way, horizontal steps contribute only to the reduced projection (Xi′) and vertical steps contribute only to the reduced projection (Yi′). Note that with probability 1 both reduced walks are infinite and they are distributed as the standard random walk on the line."
[^6]: [[pach-tardos-2013-range-of-random-walk-on-comb](pages/pach-tardos-2013-range-of-random-walk-on-comb.md)] §3 pp.3-4 L133-L182 - "Let us consider the random walk on the comb up to (and including) the nth vertical move. We call this walk W."; Lemma 2; "Let d denote the number of times W moves from a tooth to a position on the backbone, including the starting position at the origin, but not including the final position after the last move, even if it satisfies this condition. Clearly, d is distributed as An−1. W has d chances to make horizontal moves. At each chance, it makes precisely i consecutive horizontal moves with probability 2^{−i−1}."; "Obviously, the conditional distribution of c, given a, is the same as the distribution of Ba".
[^7]: [[pach-tardos-2013-range-of-random-walk-on-comb](pages/pach-tardos-2013-range-of-random-walk-on-comb.md)] §3 pp.4-6 L184-L314 [synthesis] - the close, far and intermediate sites, the bound (6), Lemma 3 and its proof, inequality (8) and the lower bound.
[^8]: Verified by execution (Python 3.11 with NumPy, 2026-10-29): `bin/python/tree_castle_diffusion.py` items [3], [4] and [5], run log `bin/python/tree_castle_diffusion-run.log`. The reduced horizontal walk on the 888 tree castles with `2 ≤ w ≤ 7` and `h ≤ 4`; the equality of the mean-square displacement and the expected number of horizontal moves; on the battlement with `h = 2001`, the slope of the expected number of horizontal moves in `√t` between `t = 10^4` and `10^5`, `3.19121`, against `4√(2/π) = 3.19154`.
