---
title: Castle samplers
category: Concepts
summary: Ten ways to draw random castles and the objects beside them, each implemented and checked by execution - rejection, the transfer-matrix sampler (exact, O(wh) per draw), Fisher-Yates and Sattolo with the Foata map (permutations, whose cycle counts have exact laws), the Gray walk (exhaustive ground truth), rank/unrank, heat-bath Markov chain Monte Carlo on the cube, coupling from the past (monotone for block weight t <= 1, and for t > 1 after reversing the order on odd columns), Wilson's spanning-tree sampler and the Lindström-Gessel-Viennot sampler for parallelogram polyominoes, Wang-Landau for the block profile, and random transfer-matrix rules. The even-block castles V(w, h) fall into many components under single-column ±1 moves (191 at (8, 4)), so the Markov chains run on the whole cube and keep the castles of V as they pass them.
tags: [concept, castle, sampling, monte-carlo, transfer-matrix, rejection-sampling, rank-unrank, gray-code, mcmc, coupling-from-the-past, wilson-algorithm, spanning-tree, lgv, wang-landau, random-matrix, sattolo, foata, verification]
sources: [project-euler-502-brute-force, project-euler-502-castle-factoring, aocp-generating-permutations-tuples]
created: 2026-09-27
updated: 2026-10-22
---

# Castle samplers

A limit law for a castle statistic is a statement about a random castle, and testing one needs random castles drawn with known probabilities at widths far beyond enumeration. This page collects ten samplers. Each is implemented, and each claim about exactness or cost on this page was checked by running it.[^exec]

Seven of the samplers draw castles. The other three draw objects beside them: permutations (the other side of [[permutation-cycle-castle-analogy](pages/permutation-cycle-castle-analogy.md)]), spanning trees of the castle graph and parallelogram polyominoes, and the 0/1 rules of [[castle-strip](pages/castle-strip.md)].

## The target measures

A castle of width `w` and height `h` is a skyline `c = (c_1, …, c_w)` with `1 ≤ c_i ≤ h` and `max c = h`, and its block count is[^blocks]

```
blocks(c) = c_1 + Σ_{i=2}^{w} max(0, c_i − c_{i−1}).
```

`V(w, h)` is the set of even-block castles, so `|V(w, h)| = A^e(w, h)` ([[castle-notation](pages/castle-notation.md)]). The samplers aim at one of three measures:

| measure | probability of `c` | lives on |
|---|---|---|
| uniform on `V(w, h)` | `1 / A^e(w, h)` | the even-block castles of width `w` and height `h` |
| uniform on castles | `1 / A(w, h)` | the castles of width `w` and height `h`, both parities |
| weighted by blocks and area | `t^{blocks(c)} · q^{area(c)} / Z`, with `Z` the sum of the weights | `V(w, h)`, or the whole cube `{1..h}^w` |

`t` is the block weight and `q` the area weight of [[castle-notation](pages/castle-notation.md)]; `t = q = 1` gives the uniform measure. `t < 1` favors skylines with few blocks and `t > 1` skylines with many.

The weighted measure is local: column `i` enters `blocks(c)` only through `max(0, c_i − c_{i−1})` and `max(0, c_{i+1} − c_i)`, so the weight of a skyline is a product of factors on neighboring columns. So a transfer matrix samples it exactly, and a Markov-chain update of one column needs only its two neighbors.

## The ten at a glance

| # | sampler | draws from | exact? | cost per draw | main use |
|---|---|---|---|---|---|
| 1 | rejection | `V(w, h)` | yes | about 2 tries | the reference implementation |
| 2 | transfer matrix | `V(w, h)`, any `t`, `q` | yes | `O(wh)` after an `O(wh²)` table | large `w` |
| 3 | Fisher-Yates, Sattolo, Foata | permutations and cycles; castle peaks | yes | `O(n)` | calibration: the permutation side has exact laws |
| 4 | Gray walk | every tuple of `{1..h}^w` in turn | exhaustive | `O(1)` per step | exact moments at small `(w, h)` |
| 5 | rank/unrank | `V(w, h)`, from a uniform integer | yes | `O(wh)` | indexing, stratified and quasi-random draws |
| 6 | heat-bath chain | the cube, any `t`, `q`; kept on `V` | in the limit | one column per step | weights that do not factor column by column |
| 7 | coupling from the past | the cube, any `t`, `q`; kept on `V` | yes | 128 to 2,048 column updates at `w ≤ 80` | exact draws from a Markov chain |
| 8 | Wilson and LGV | spanning trees of a castle graph; parallelogram polyominoes | yes | loop-erased walks / `O(m + n)` steps | determinantal measures |
| 9 | Wang-Landau | the block profile of the castles of width `w` and height `h` | estimate | flat-histogram walk | rare block counts |
| 10 | random rules | 0/1 transfer matrices | yes | one eigenvalue problem | random growth constants and spectra |

## 1. Rejection

Draw `c` uniformly from `{1..h}^w` and keep it if `max c = h` and `blocks(c)` is even; the acceptance rate is `A^e(w, h) / h^w`. A better version first draws a uniform castle of height `h`, by unranking a uniform integer with the decomposition by the first column of height `h` of [[song-as-castle](pages/song-as-castle.md)], and keeps it if its block count is even; its acceptance rate is `A^e / A`.[^exec]

| cell | `A^e(w, h)` | `A^e / h^w` | `A^e / A` |
|---|---|---|---|
| `(4, 2)` | 10 | 0.625 | 0.667 |
| `(6, 3)` | 307 | 0.421 | 0.462 |
| `(8, 4)` | 29,201 | 0.446 | 0.495 |
| `(12, 5)` | 113,548,062 | 0.465 | 0.499 |
| `(20, 10)` | 4.39 × 10¹⁹ | 0.439 | 0.500000 |

`A^e / A = (1 + S/A)/2`, and `S/A` tends to 0 as `w` grows because the spectral radius of the signed transfer matrix `M̃_{h−1}` is less than `h` ([[castle-graph-spectral-radius](pages/castle-graph-spectral-radius.md)], [[castle-entropy](pages/castle-entropy.md)]). So the two-stage sampler needs about two tries: at `(10, 4)`, 100,000 draws took 2.002 tries on average against `A / A^e = 2.005`, and the cube version 2.118 against `4^10 / A^e = 2.124`. On the 307 castles of `(6, 3)`, 200,000 draws of each version passed a chi-square test for uniformity (`p = 0.43` and `p = 0.99`).[^exec]

Rejection cannot aim at a weighted measure without paying for the full range of weights. It is obviously correct, so it is the check for the other samplers.

## 2. The transfer-matrix sampler

This sampler reuses the three-part state of [[castle-bdd-zdd](pages/castle-bdd-zdd.md)]: the height of the last column, the block count modulo 2, and whether height `h` has been reached. A table `N_i(state)` holds the weighted number of ways to finish a castle with `i` columns still to place, and the castle is drawn left to right, each column chosen with probability proportional to its weight times the number of completions from the state it leads to.

```python
def build(w, h, t=1, q=1):
    # N[i][(c, b, r)]: weighted completions with i columns left, from last height c,
    # block parity b, reached-h flag r; accept at the end iff r = 1 and b = 0
    states = [(c, b, r) for c in range(h+1) for b in (0, 1) for r in (0, 1)]
    def moves(s):
        c, b, r = s
        for a in range(1, h+1):
            rise = max(0, a - c)
            yield a, (a, (b + rise) % 2, r | (a == h)), t**rise * q**a
    N = [{s: int(s[2] == 1 and s[1] == 0) for s in states}]
    for i in range(1, w+1):
        N.append({s: sum(wt * N[i-1][s2] for _, s2, wt in moves(s)) for s in states})
    return N, moves

def sample(w, N, moves, rng):
    s, out = (0, 0, 0), []
    for i in range(w, 0, -1):
        opts = [(a, s2, wt * N[i-1][s2]) for a, s2, wt in moves(s)]
        x = rng.random() * sum(o[2] for o in opts)   # use rng.randrange(total) for big-integer weights
        for a, s2, wgt in opts:
            x -= wgt
            if x < 0: break
        out.append(a); s = s2
    return tuple(out)
```

`N_w(start)` is `A^e(w, h)` when `t = q = 1`, and it agrees with enumeration for every `w ≤ 7`, `h ≤ 5`. Exactness was checked in rational arithmetic: the product of the step probabilities along every castle of `V(4, 2)`, `V(5, 3)`, `V(6, 3)` and `V(5, 4)` is exactly `1/A^e`, and on `V(5, 3)` with `t = 1/2`, `q = 2/3` it is exactly `t^{blocks} q^{area} / Z`.[^exec]

**Cost.** The table has `4(h + 1)` states per column and `h` moves per state, so building it costs `O(wh²)` operations and each draw `O(wh)`. With uniform weights the entries are exact integers, and drawing with `rng.randrange(total)` avoids floating-point overflow at any width. The table is the ZDD of [[castle-bdd-zdd](pages/castle-bdd-zdd.md)] read from the top, and its sums are the strip counts of [[castle-strip](pages/castle-strip.md)].

**What it gives.** Block count, area, peaks, perimeter and the skyline itself for castles with `w` in the thousands, drawn exactly from `V(w, h)` or from any measure weighted by blocks and area.

## 3. Fisher-Yates, Sattolo and Foata: the permutation side

[[castles-as-upgraded-cycle-count](pages/castles-as-upgraded-cycle-count.md)] pairs the castle sign, the castle Foata transform and the streak factorization with constructions on permutations, and the permutation side has two exact samplers.

- **Fisher-Yates** (Durstenfeld's shuffle): for `i = n−1` down to `1`, swap position `i` with a uniform position `j ≤ i`. The `n!` choice sequences correspond one to one with the permutations of `n` points.[^durstenfeld]
- **Sattolo's algorithm**: the same loop with `j < i`. The `(n−1)!` choice sequences correspond one to one with the cyclic permutations, so the output is a uniform `n`-cycle.[^sattolo]

Both correspondences were checked exhaustively, Sattolo's for `n = 2, …, 8` and Fisher-Yates's for `n ≤ 7`.[^exec]

**The Foata map.** Write each cycle with its largest element first, order the cycles by these leaders, and erase the parentheses. This is a bijection on permutations under which the number of cycles becomes the number of left-to-right maxima (checked on all permutations of `n ≤ 8` points).[^exec] On the castle side, the castle Foata transform sends the peaks of a skyline, its maximal runs of columns with `c_i ≥ 2` (the positive runs of the towers `c_i − 1`), to its records, the columns where the towers leave the base ([[castle-foata-transform](pages/castle-foata-transform.md)]); peaks and records agree on every tuple with `w ≤ 7`, `h ≤ 4`.[^foata][^exec]

**Exact laws.** The cycle count of a uniform permutation of `n` points has mean `H_n` and variance `H_n − H_n^{(2)}`, with `H_n = Σ_{i ≤ n} 1/i` and `H_n^{(2)} = Σ_{i ≤ n} 1/i²`, both checked exactly for `n ≤ 8`. So `variance − ln n → γ − π²/6 = −1.067718`, and at `n = 10^6` the left side is `−1.067717`.[^exec] The castle peak count instead grows linearly in the width. Over the cube `{1..h}^w` its mean is

```
E[peaks]  =  (h − 1)/h  +  (w − 1)(h − 1)/h²,
```

the probability that column 1 is a peak's first column plus `w − 1` times the probability that column `i ≥ 2` is (checked exactly at `(5, 3)` and `(6, 4)`). 2,000 transfer-matrix draws from `V(200, 4)` gave 0.1900 peaks per column (standard error 0.0005), against the cube value `(0.75 + 199 · 3/16)/200 = 0.1903`.[^exec]

## 4. The Gray walk: exhaustive ground truth

The reflected mixed-radix Gray code visits every tuple of `{1..h}^w` once and changes one column by `±1` per step ([[castle-gray-code](pages/castle-gray-code.md)], by the loopless Gray algorithm, Algorithm H of TAOCP §7.2.1.1). A `±1` change at column `i` touches only the terms `max(0, c_i − c_{i−1})` and `max(0, c_{i+1} − c_i)` of the block count, so `blocks(c)` is carried along in `O(1)` per step. The walk visits each tuple once with a correct running block count at `(3, 2)`, `(4, 3)`, `(5, 4)` and `(6, 3)`.[^exec]

Keeping the castles of `V(w, h)` as the walk passes them gives every moment of every statistic on `V(w, h)` exactly. On `V(8, 4)`, with 29,201 castles, the mean block count is `205920/29201 = 7.05181` and the variance `2.30248`; these are the exact values in the section *Cross-check*.[^exec]

## 5. Rank/unrank

The completion table of the transfer-matrix sampler also ranks. Order `V(w, h)` lexicographically. To unrank `n`, go through the columns and, at each one, pass over the castles whose next column is smaller, whose numbers are the completion counts; ranking runs the same walk backwards. This is a bijection `V(w, h) ↔ {0, …, A^e − 1}` in `O(wh)` per query, and it lists `V` in sorted order at `(5, 3)`, `(6, 3)` and `(6, 4)`.[^exec] The version for all castles of height `h`, by the first column of height `h`, is the one on [[song-as-castle](pages/song-as-castle.md)] and [[hardy-ramanujan-castle](pages/hardy-ramanujan-castle.md)].

The transfer-matrix sampler unranks a uniform random integer, one column at a time. Rank/unrank adds control over which integers are used: evenly spaced ranks give a stratified sample of the lexicographic order, a low-discrepancy sequence of ranks a quasi-Monte Carlo sample, and a single rank names a single castle. 200,000 unranked draws passed a chi-square test on `(6, 3)` (`p = 0.39`), and across 60 runs of 40,000 draws on `(8, 4)` the z-scores of the mean block count had mean 0.04 and standard deviation 1.02.[^exec]

## 6. Heat-bath chain

A heat-bath step picks a column `i` and redraws `c_i` from its law given the neighbors `a = c_{i−1}` and `b = c_{i+1}`:

```
P(c_i = x | a, b)  ∝  t^{max(0, x − a) + max(0, b − x)} · q^x,      x = 1, …, h,
```

with `a = 0` at the left wall and `b = 0` at the right wall, where the term `max(0, b − x)` vanishes. The chain is reversible for the weight `t^{blocks} q^{area}` on the cube.

**Run it on the cube, not on `V`.** A chain that stays inside `V(w, h)` does not work, because `V(w, h)` falls into many components under single-column `±1` moves:[^exec]

| cell | `A^e(w, h)` | components under `±1` moves | largest | components under single-column redraws |
|---|---|---|---|---|
| `(3, 3)` | 3 | 3 | 1 | 3 |
| `(4, 3)` | 21 | 3 | 7 | 1 |
| `(6, 3)` | 307 | 8 | 84 | 1 |
| `(5, 4)` | 439 | 35 | 210 | 2 |
| `(6, 4)` | 1,729 | 35 | 462 | 1 |
| `(8, 4)` | 29,201 | 191 | 3,003 | 1 |

A `±1` move changes the block count by at most 1, so a move between two castles of `V` keeps the block count. Redrawing a whole column does better, but the castle `(3, 2, 4, 2, 3)` in `V(5, 4)` is still isolated: every change of one of its columns makes the block count odd or loses the height. The same fragmentation blocks a Gray tour of `V` ([[castle-native-gray-tour](pages/castle-native-gray-tour.md)], [[castle-move-graph-zdd](pages/castle-move-graph-zdd.md)]). So the chain runs on the whole cube, where it is irreducible, and keeps the states that land in `V`; at `t = q = 1` that is a fraction `A^e / h^w`, between 0.42 and 0.50 in the cells above. On `(6, 3)`, 600,000 steps reproduced the exact block-count distribution on `V` to total-variation distance 0.0003 at `t = 1/2` and 0.0008 at `t = 2`.[^exec]

Where a transfer matrix exists, the chain is the slower way to reach the same measure. It is for weights that do not factor column by column, such as a factor per spanning tree, per sandpile recurrent configuration, or per unit of spectral radius.

## 7. Coupling from the past

Propp and Wilson's coupling from the past turns a monotone Markov chain into an exact sampler: run the chain from time `−T` to 0 from the top and the bottom state with the same random numbers, and double `T` until the two runs agree at time 0; the common state is an exact draw from the stationary law.[^cftp]

The heat-bath chain is monotone in one of two ways:[^exec]

- **`t ≤ 1`: monotone.** Raising a neighbor makes the law of `c_i` stochastically larger. The top state is all `h` and the bottom state all 1.
- **`t > 1`: antimonotone.** Raising a neighbor makes the law of `c_i` stochastically smaller. The columns form a path, which is bipartite, so reversing the order on the odd-numbered columns makes the chain monotone. The top state is then `(h, 1, h, 1, …)`.

Both hold for every pair of neighbors at `h = 2, 3, 4, 6`, `t ∈ {0.1, 0.5, 0.9, 1, 1.1, 2, 5}` and `q ∈ {0.5, 1, 1.5}`; `q` does not matter, since its factor does not involve the neighbors. Kept on `V`, 40,000 draws of coupling from the past passed a chi-square test against the weights on the 89 castles of `V(5, 3)` (`p = 0.88` at `t = 1/2`, `p = 0.17` at `t = 2`). Over 40 runs per cell, the median coalescence time was 256, 512 and 1,536 column updates at widths 20, 40 and 80 with `h = 5`, `t = 1/2`; 2,048 at `(40, 10)`; and 768 at `(40, 5)` with `t = 2`. The doubling schedule makes each run's time a power of 2.[^exec]

A block weight in one dimension does not need this sampler, since the transfer matrix draws it exactly. It applies when the weight stops being one-dimensional but stays monotone, such as a field of castles on a grid.

## 8. Wilson and LGV: determinantal samplers

Two objects beside castles are counted by determinants, and each has an exact sampler.

**Wilson's algorithm on the castle graph.** A spanning tree of the castle graph ([[castle-graph](pages/castle-graph.md)]) is built by loop-erased random walks: from each vertex not yet in the tree, walk at random until the tree is hit, erase the loops, and add the path.[^wilson] The root is the sink of a sandpile model of [[sandpile-group](pages/sandpile-group.md)]: the bottom-left cell in the sink model, or the whole bottom row merged into one vertex in the tide model. The number of trees is `det L̃`, the order of the sandpile group. In every case below the sampler hit exactly that many distinct trees, uniformly (chi-square `p` from 0.20 to 0.62, 200 draws per tree):[^exec]

| castle | sink-model trees | tide-model trees |
|---|---|---|
| `(2, 2, 2)` | 15 | 8 |
| `(1, 3, 2, 3, 1)` | 15 | 8 |
| `(3, 3, 3)` | 192 | 95 |
| `(2, 4, 3, 4)` | 712 | 244 |

These are the group orders on [[sandpile-census](pages/sandpile-census.md)]: `Z/15` and `Z/8` for the castle `(2, 2, 2)`, which is silver by spectrum. The tree edges form a determinantal process whose kernel is the transfer-current matrix built from `L̃⁻¹` (Burton and Pemantle).[^bp] Two consequences were checked on 60,000 trees each. An edge lies in the tree with probability equal to the effective resistance across it; the empirical frequencies agreed with the resistances to within 0.0032 on `(2, 3, 2)` in the sink model and on `(3, 3, 3)` and `(1, 3, 2, 3, 1)` in the tide model. The probability that the two edges at the sink cell of `(2, 3, 2)` both lie in the tree is a `2 × 2` minor of the kernel, 0.4667, against 0.4659 measured.[^exec]

**The LGV sequential sampler.** A parallelogram polyomino in an `m × n` box is a pair of vertex-disjoint lattice paths, from `(0, 1)` to `(m−1, n)` and from `(1, 0)` to `(m, n−1)`. By the Lindström-Gessel-Viennot lemma the number of such pairs is a `2 × 2` determinant of binomial coefficients.[^lgv] It equals the Narayana number `N(m + n − 1, m)`, and the sum over the boxes with `m + n = s` is the Catalan number `C_{s−1}` ([[narayana-numbers](pages/narayana-numbers.md)], [[catalan-numbers](pages/catalan-numbers.md)]). The sampler advances both paths one step at a time and chooses the joint step with probability proportional to the determinant from the new positions, the number of non-crossing completions; it is the transfer-matrix sampler with a determinant in place of the matrix power. Every pair in the `(3, 3)`, `(4, 3)`, `(4, 4)` and `(5, 3)` boxes has probability exactly `1/det`, checked in rational arithmetic, and the determinant equals the brute-force count and the Narayana number for every `m, n ≤ 5`.[^exec]

Fomin extended the determinant formula of the lemma to walks in planar graphs that need not be acyclic, through loop-erased walks,[^fomin] and the castle graph is planar. A castle is bounded by a single path, its skyline, so the lemma counts no castles ([[spectral-analysis](pages/spectral-analysis.md)], section 2), and the LGV sampler draws parallelogram polyominoes.

## 9. Wang-Landau: the block profile

Wang-Landau estimates a density of states, here `g(b)`, the number of castles of width `w` and height `h` with `b` blocks.[^wl] A walk over these castles proposes single-column redraws and accepts them with probability `min(1, g(b_old)/g(b_new))` under its running estimate of `g`; a redraw that removes the last column of height `h` is rejected. After each step it raises `ln g(b)` by `ln f`, and it halves `ln f`, starting from 1, each time the visit histogram is flat, every level above 80% of the mean (checked every 1,000 steps). Normalized so that `Σ_b g(b) = A(w, h)`, the estimate gives every level of the block profile, and the even levels give `A^e`.

| cell | block levels | largest/smallest level | median / max relative error | `A^e/A` exact | `A^e/A` estimated | steps |
|---|---|---|---|---|---|---|
| `(8, 4)` | 10 | 648 | 2.4% / 15.2% | 0.495142 | 0.497020 | 0.14 million |
| `(12, 5)` | 21 | 8.0 × 10⁵ | 4.8% / 20.6% | 0.499412 | 0.496517 | 0.75 million |
| `(20, 6)` | 46 | 4.0 × 10¹² | 1.3% / 7.1% | 0.500000 | 0.499776 | 7.0 million |

(Final `ln f` below `10⁻⁶`; exact profiles from a block-weighted transfer matrix.)[^exec] At `(20, 6)` the rarest block count has 101 castles out of `3.6 × 10¹⁵`, a level that uniform sampling would essentially never reach. The errors stay at the percent level as `ln f` shrinks: the estimate of the mean block count on `V(8, 4)` is 7.060 against the exact 7.052. Belardinelli and Pereyra trace this saturation to the halving schedule and remove it by shrinking `ln f` as a power law in the number of steps.[^bp07]

For the block profile itself the block-weighted transfer matrix is exact, so Wang-Landau is for profiles of statistics that no transfer matrix tracks, such as spanning-tree counts, spectral radii and sandpile clock periods.

## 10. Random rules

This sampler draws the rule instead of the castle. A strip rule is an `h × h` 0/1 matrix saying which column heights may follow which ([[castle-strip](pages/castle-strip.md)]), and its Perron root is the growth constant of its strips by width. Two priors on rules:

- **Uniform over all rules on `h` heights.** There are `2^{h²}` of them, 66,066 for `h ≤ 4` in all, which [[area-growth-census](pages/area-growth-census.md)] lists. At `h = 3` the 512 rules have 18 distinct Perron roots: 1 for 219 rules, the golden mean for 96, 2 for 75 and 0 for 25, with mean 1.418.[^exec]
- **Bernoulli rules for large `h`.** Each entry is 1 with probability `p`, independently, and the rule is a random matrix. Apart from the Perron root, about `ph`, the spectrum follows the limit laws of random matrices.

At `h = 1000` and `2000` a Bernoulli rule behaved as those laws predict:[^exec]

| rule | Perron root | rest of the spectrum, scaled by `√(h p (1 − p))` | check |
|---|---|---|---|
| any rule, `h = 1000`, `p = 1/2` | 499.73 (`ph = 500`) | the unit disk (circular law) | fraction with `\|z\| < 1/2`: 0.2513 (law: 0.25); mean `\|z\|²`: 0.5013 (0.5) |
| symmetric rule, `h = 1000`, `p = 1/2` | 501.02 | `[−2, 2]` (semicircle law) | fraction in `[−1, 1]`: 0.6076 (law: 0.6090) |
| any rule, `h = 2000`, `p = 0.3` | 599.97 (`ph = 600`) | the unit disk | 0.2481 and 0.5002 |
| symmetric rule, `h = 2000`, `p = 0.3` | 599.97 | `[−2, 2]` | 0.6088 |

A symmetric rule lets a column of height `a` follow one of height `b` exactly when `b` may follow `a`. The semicircle density at 0 is `1/π = 0.3183`, against 0.320 and 0.315 measured. The circular law for matrices with independent entries is Tao and Vu's theorem.[^tv] With a random rule in place of the castle rule, the transfer-matrix sampler draws its strips.

## Cross-check

The mean block count over `V(8, 4)` is exactly `205920/29201 = 7.0518` (section 4). With 100,000 draws each at `t = q = 1`:[^exec]

| sampler | estimate | naive standard error |
|---|---|---|
| 1. rejection (castle of height 4, then parity) | 7.0476 | 0.0048 |
| 2. transfer matrix | 7.0460 | 0.0048 |
| 5. unrank of a uniform rank | 7.0497 | 0.0048 |
| 6. heat-bath chain on the cube, kept on `V` (every 8th step) | 7.0457 | 0.0048 (too small: the draws are correlated) |
| 7. coupling from the past, kept on `V` | 7.0571 | 0.0048 |
| 9. Wang-Landau, even levels of the profile | 7.060 | (saturated schedule) |

The first five are within 1.3 standard errors of the exact value, and the Wang-Landau estimate is 0.1% high.

## Related Concepts

- [[castle-strip](pages/castle-strip.md)] - the transfer matrix whose powers the sampler reads, and the rules that section 10 draws.
- [[castle-bdd-zdd](pages/castle-bdd-zdd.md)] - the three-part state, and the top-down sampling and ranking of the ZDD, implemented here.
- [[castle-gray-code](pages/castle-gray-code.md)] - the Gray walk used as exhaustive ground truth.
- [[castle-native-gray-tour](pages/castle-native-gray-tour.md)], [[castle-move-graph-zdd](pages/castle-move-graph-zdd.md)] - the fragmentation of `V(w, h)` under local moves.
- [[song-as-castle](pages/song-as-castle.md)] - rank/unrank on all castles of height `h` by the first column of height `h`.
- [[castle-foata-transform](pages/castle-foata-transform.md)], [[castles-as-upgraded-cycle-count](pages/castles-as-upgraded-cycle-count.md)] - peaks as records, and the pairing with permutations.
- [[castle-graph](pages/castle-graph.md)], [[sandpile-group](pages/sandpile-group.md)], [[sandpile-census](pages/sandpile-census.md)] - the graph and the two sink models on which Wilson's algorithm runs, and the tree counts it reproduces.
- [[spectral-analysis](pages/spectral-analysis.md)] - section 2, the Lindström-Gessel-Viennot determinant of parallelogram polyominoes.
- [[area-growth-census](pages/area-growth-census.md)] - the list of all rules that the uniform prior samples.
- [[castle-entropy](pages/castle-entropy.md)] - `log₂ A^e = log₂ A − 1 + log₂(1 + S/A)`, behind `A^e/A → 1/2`.
- [[castle-notation](pages/castle-notation.md)] - the block weight `t`, the area weight `q`, `V(w, h)`, `N_i(state)`, `g(b)` and `H_n`.
- [[aocp-generating-partitions](pages/aocp-generating-partitions.md)] - exercise 47, the Nijenhuis-Wilf uniform random-partition generator, which also draws from a table of completion counts.

## Footnotes

[^exec]: Verified by execution (Python 3.11 with NumPy; exact checks in `fractions.Fraction`; chi-square p-values from the regularized incomplete gamma function of mpmath; 2026-10-16). Exact: the transfer-matrix count against enumeration for `w ≤ 7`, `h ≤ 5`; the step-probability products on every castle of the stated cells; the rank/unrank bijections; the Sattolo and Fisher-Yates correspondences; the Foata bijection and the cycle-count moments; peaks = records for `w ≤ 7`, `h ≤ 4`; `E[peaks]`; the Gray walk with its running block count; the components of `V(w, h)` by graph search; the monotonicity of the heat-bath laws on the stated grid; the tree counts `det L̃`; the LGV determinants, their exact sampler and the Narayana and Catalan sums; the 512 rules on three heights. Random, with fixed seeds: Python `random` seeded 502 for the rejection tries and chi-square tests, the rank/unrank tests and the peak draws, and for the Wilson trees; NumPy generators seeded 11 and 12 (heat-bath distances), 21 and 22 (coupling-from-the-past chi-square), 31 to 35 (coalescence times), 41 to 43 (Wang-Landau), 502 (random rules), and 503 to 505 (cross-check).
[^blocks]: [[project-euler-502-brute-force](pages/project-euler-502-brute-force.md)] §"Column-height encoding" L18-27 - "column heights c_1, …, c_w ∈ {1, …, h} with max c = h ... #blocks = ∑_{r=1}^{h} #{runs of columns with c_i ≥ r} = c_1 + ∑_{i=2}^{w} max(0, c_i − c_{i−1}) ... Rule 6 (even block count) is applied by parity at the end."
[^foata]: [[project-euler-502-castle-factoring](pages/project-euler-502-castle-factoring.md)] §"The castle version" [synthesis] L143-157 - the peaks of the towers are the maximal positive runs of their column heights, and the map from a peak to the first column of its run is a bijection onto the record set `{ i : c_i > 0 and (i = 1 or c_{i−1} = 0) }`.
[^durstenfeld]: https://doi.org/10.1145/364520.364540 (1964) - R. Durstenfeld, "Algorithm 235: Random permutation", *Communications of the ACM* 7(7), p. 420.
[^sattolo]: https://doi.org/10.1016/0020-0190(86)90073-6 (1986) - S. Sattolo, "An algorithm to generate a random cyclic permutation", *Information Processing Letters* 22, 315-317.
[^cftp]: https://doi.org/10.1002/(SICI)1098-2418(199608/09)9:1/2%3C223::AID-RSA14%3E3.0.CO;2-O (1996) - J. G. Propp and D. B. Wilson, "Exact sampling with coupled Markov chains and applications to statistical mechanics", *Random Structures & Algorithms* 9, 223-252.
[^wilson]: https://doi.org/10.1145/237814.237880 (1996) - D. B. Wilson, "Generating random spanning trees more quickly than the cover time", *Proc. 28th ACM STOC*, 296-303.
[^bp]: https://doi.org/10.1214/aop/1176989121 (1993) - R. Burton and R. Pemantle, "Local characteristics, entropy and limit theorems for spanning trees and domino tilings via transfer-impedances", *Annals of Probability* 21(3), 1329-1371.
[^lgv]: https://doi.org/10.1016/0001-8708(85)90121-5 (1985) - I. Gessel and G. Viennot, "Binomial determinants, paths, and hook length formulae", *Advances in Mathematics* 58(3), 300-321.
[^fomin]: https://arxiv.org/abs/math/0004083 (abstract read 2026-10-16) - S. Fomin, "Loop-erased walks and total positivity", *Transactions of the AMS* 353 (2001), 3563-3583: "We consider matrices whose elements enumerate weights of walks in planar directed weighted graphs (not necessarily acyclic). These matrices are totally nonnegative ... A combinatorial explanation of this phenomenon involves loop-erased walks."
[^wl]: https://doi.org/10.1103/PhysRevLett.86.2050 (2001) - F. Wang and D. P. Landau, "Efficient, multiple-range random walk algorithm to calculate the density of states", *Physical Review Letters* 86, 2050-2053.
[^bp07]: https://doi.org/10.1063/1.2803061 (2007) - R. E. Belardinelli and V. D. Pereyra, "Wang-Landau algorithm: a theoretical analysis of the saturation of the error", *Journal of Chemical Physics* (arXiv cond-mat/0702414): the error saturates when the refinement parameter shrinks exponentially, and scaling it down as a power law removes the saturation.
[^tv]: https://arxiv.org/abs/0807.4898 (2010) - T. Tao and V. Vu, "Random matrices: universality of ESDs and the circular law", *Annals of Probability* 38(5), 2023-2065.
