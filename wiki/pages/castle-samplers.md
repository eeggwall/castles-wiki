---
title: Castle samplers
category: Concepts
summary: Ten ways to draw random castles and the objects around them, each implemented and checked by execution - rejection, the transfer-matrix sampler (exact, O(wh) per draw, the workhorse), Sattolo-Foata (the permutation side of the cycle analogy, with exactly known laws), the Gray walk (exhaustive ground truth), rank/unrank, heat-bath MCMC on the cube, coupling from the past (monotone for block weight t <= 1, monotone after flipping odd columns for t > 1), Wilson's spanning-tree sampler plus the LGV sequential sampler for non-crossing path pairs, Wang-Landau for the block profile, and random-rule ensembles. The valid set V(w, h) is badly disconnected under single-column +-1 moves (191 components at (8, 4)), so the Markov-chain samplers run on the full cube and filter at emit.
tags: [concept, castle, sampling, monte-carlo, transfer-matrix, rejection-sampling, rank-unrank, gray-code, mcmc, coupling-from-the-past, wilson-algorithm, spanning-tree, lgv, wang-landau, random-matrix, sattolo, foata, verification]
sources: [project-euler-502-brute-force, project-euler-502-castle-factoring, aocp-generating-permutations-tuples]
created: 2026-09-27
updated: 2026-09-27
---

# Castle samplers

Every exact castle count is C-finite, so `e` and `π` can reach the castle only through limits ([[algebraic-transcendental-wall](pages/algebraic-transcendental-wall.md)]). A limit law is a statement about a random castle, and to test one you need a way to draw random castles, with known probabilities, at widths far beyond enumeration. This page collects ten such samplers. Each one is implemented, and each claim about exactness or cost below was checked by running it.[^exec]

The samplers do not all draw the same thing. Seven draw castles. The other three draw from the objects next to castles on the wiki: permutations (the other side of [[permutation-cycle-castle-analogy](pages/permutation-cycle-castle-analogy.md)]), spanning trees of the castle graph, and the 0/1 rules of [[castle-strip](pages/castle-strip.md)].

## The target measures

A castle is a skyline `c = (c_1, …, c_w)` with `1 ≤ c_i ≤ h` and `max c = h`, and its block count is[^blocks]

```
blocks(c) = c_1 + Σ_{i=2}^{w} max(0, c_i − c_{i−1})
```

`V(w, h)` is the set of even-block castles, so `|V(w, h)| = F(w, h)`. The samplers aim at one of these measures:

| measure | probability of `c` | lives on |
|---|---|---|
| uniform on `V(w, h)` | `1 / F(w, h)` | even-block castles of width `w`, height exactly `h` |
| uniform on proper castles | `1 / A(w, h)` | both parities |
| block- and area-weighted | `t^blocks(c) · q^area(c) / Z`, with `Z` the sum of the weights | `V(w, h)`, or the whole cube `{1..h}^w` |

`t` is the block weight and `q` the area weight of [[castle-notation](pages/castle-notation.md)]. `t = 1, q = 1` gives the uniform measure back. `t < 1` favours smooth skylines with few blocks, and `t > 1` favours jagged ones.

The weighted measure is local. Column `i` enters `blocks(c)` only through `max(0, c_i − c_{i−1})` and `max(0, c_{i+1} − c_i)`, so the weight of a castle is a product of nearest-neighbour factors. That is why a transfer matrix samples it exactly, and why a single-column Markov-chain update needs only the two neighbours.

## The ten at a glance

| # | sampler | draws from | exact? | cost per draw | main use |
|---|---|---|---|---|---|
| 1 | rejection | `V(w, h)` | yes | about 2 tries | the reference implementation |
| 2 | transfer matrix | `V(w, h)`, any `t`, `q` | yes | `O(wh)` after an `O(wh²)` table | the workhorse for large `w` |
| 3 | Sattolo-Foata | cyclic and general permutations; castle peaks | yes | `O(n)` | calibration: the permutation side has closed-form laws |
| 4 | Gray walk | every tuple of `{1..h}^w` in turn | exhaustive | `O(1)` per step | exact moments at small `(w, h)` |
| 5 | rank/unrank | `V(w, h)`, via a uniform integer | yes | `O(wh)` | indexing, stratified and quasi-random draws |
| 6 | heat-bath MCMC | the cube, any `t`, `q`; filtered to `V` | asymptotically | one site per step | weights no transfer matrix handles |
| 7 | coupling from the past | the cube, any `t`, `q`; filtered to `V` | yes | hundreds to thousands of site updates at `w ≤ 80` | exact draws from a Markov chain |
| 8 | Wilson and LGV | spanning trees of a castle; non-crossing path pairs | yes | walk cover / `O(m + n)` steps | determinantal ensembles |
| 9 | Wang-Landau | the block profile of the cell | estimate | flat-histogram walk | rare block counts, parity from the profile |
| 10 | random-rule ensembles | 0/1 transfer matrices, then strips | yes | one eigenvalue problem | random growth constants and random-matrix spectra |

## 1. Rejection

Draw `c` uniformly from `{1..h}^w` and keep it if `max c = h` and `blocks(c)` is even. The acceptance rate is `F(w, h) / h^w`. A better version draws a uniform proper castle first, with the rank/unrank bijection of [[song-as-castle](pages/song-as-castle.md)] (decompose by the first full-height column), and then keeps it if the block count is even. Its acceptance rate is `F / A`.[^exec]

| cell | `F(w, h)` | `F / h^w` | `F / A` |
|---|---|---|---|
| `(4, 2)` | 10 | 0.625 | 0.667 |
| `(6, 3)` | 307 | 0.421 | 0.462 |
| `(8, 4)` | 29,201 | 0.446 | 0.495 |
| `(12, 5)` | 113,548,062 | 0.465 | 0.499 |
| `(20, 10)` | 4.39 × 10¹⁹ | 0.439 | 0.500000 |

`F / A` goes to `1/2` because the parity clause is one bit ([[castle-entropy](pages/castle-entropy.md)]). So the two-stage sampler needs about two tries, whatever the cell: at `(10, 4)` the measured mean was 2.018 tries against `A / F = 2.005`, and the cube version 2.132 against `4^10 / F = 2.124`. Both samplers passed a chi-square test for uniformity on all 307 castles of `(6, 3)` (200,000 draws each, `p = 0.36` and `0.81`).[^exec]

Rejection cannot aim at a weighted measure without paying for the full range of weights, and it tells you nothing you could not get faster from the transfer matrix. Its value is that it is obviously correct, so it is the check for everything else.

## 2. The transfer-matrix sampler

This is the sampler to use for large castles. It reuses the three-part state of [[castle-bdd-zdd](pages/castle-bdd-zdd.md)]: the last column height, the block count mod 2, and whether height `h` has been reached. A table `N_i(state)` holds the weighted number of ways to finish a castle with `i` columns still to place. Then the castle is drawn left to right, choosing each column with probability proportional to its weight times the number of completions from the state it leads to.

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

`N_w(start)` is `F(w, h)` when `t = q = 1`. It agreed with brute force for every `w ≤ 7`, `h ≤ 5`. Exactness was checked in rational arithmetic, not statistically: the product of the step probabilities along every castle of `(4, 2)`, `(5, 3)`, `(6, 3)` and `(5, 4)` is exactly `1/F`, and on `(5, 3)` with `t = 1/2`, `q = 2/3` it is exactly `t^blocks q^area / Z`.[^exec]

**Cost.** The table has `4(h + 1)` states per column and `h` moves per state, so building it costs `O(wh²)` and each draw costs `O(wh)`. With uniform weights the entries are exact big integers, and drawing with `rng.randrange(total)` avoids floating-point overflow at any width. A plain-Python run drew width-1000, height-10 castles in 0.02 s each. The same table is the ZDD of [[castle-bdd-zdd](pages/castle-bdd-zdd.md)] read top-down, and its sums are the strip counts of [[castle-strip](pages/castle-strip.md)].

**What it gives.** Block count, area, peaks, perimeter and the skyline itself of castles with `w` in the thousands, drawn exactly from `V(w, h)` or from any block- and area-weighted measure. Every limit-law experiment on a single castle statistic starts here.

## 3. Sattolo-Foata: the permutation side

The castle is an upgrade of the `(n−1)!` cycle count ([[castles-as-upgraded-cycle-count](pages/castles-as-upgraded-cycle-count.md)]), and the permutation end of that upgrade has its own two exact samplers.

- **Fisher-Yates** (Durstenfeld's shuffle): for `i = n−1` down to `1`, swap position `i` with a uniform position `j ≤ i`. The `n!` choice sequences map one to one onto the permutations.[^durstenfeld]
- **Sattolo's algorithm**: the same loop with `j < i` strictly. The `(n−1)!` choice sequences map one to one onto the `n`-cycles, so the output is a uniform cyclic permutation.[^sattolo] This is the `(n−1)!` count turned into an algorithm, one factor per step.

Both bijections were checked exhaustively, Sattolo for `n = 2, …, 8` and Fisher-Yates for `n ≤ 7`.[^exec]

**The Foata step.** Write each cycle with its largest element first, order the cycles by those leaders, and erase the parentheses. This is a bijection on permutations, and the number of cycles becomes the number of left-to-right maxima (checked on all of `S_n`, `n ≤ 8`).[^exec] On the castle side, the castle Foata transform sends the peaks of a skyline (the maximal positive runs of the tower `c_i − 1`) to its records, the columns where the tower leaves the base ([[castle-foata-transform](pages/castle-foata-transform.md)]); peaks and records agreed on every tuple with `w ≤ 7`, `h ≤ 4`.[^foata][^exec]

**Why it is a sampler worth having.** The permutation side has exact laws. The cycle count of a uniform permutation has mean `H_n` and variance `H_n − H_n^{(2)}`, where `H_n = Σ 1/i` and `H_n^{(2)} = Σ 1/i²`; both were checked exactly on `S_n` for `n ≤ 8`. So `variance − ln n → γ − π²/6 = −1.06772`, and at `n = 10^6` the left side is `−1.067717`.[^exec] Euler's `γ` and the Basel constant are already in the calibration run. The castle side is different in kind: the peak count is a sum of nearly independent local indicators, so it grows linearly in the width, not logarithmically. Over the cube `{1..h}^w` its mean is exactly

```
E[peaks] = (h − 1)/h + (w − 1)(h − 1)/h²
```

(checked at `(5, 3)` and `(6, 4)`), and transfer-matrix draws from `V(200, 4)` gave 0.1905 peaks per column against the cube value `(0.75 + 199 · 3/16)/200 = 0.1903`.[^exec] The cycle and peak counts correspond one to one as statistics, but their scaling laws differ. That difference is the first thing a limit law along the analogy has to explain.

## 4. The Gray walk: exhaustive ground truth

The reflected mixed-radix Gray code visits every tuple of `{1..h}^w` once, changing one column by `±1` per step ([[castle-gray-code](pages/castle-gray-code.md)]; TAOCP's loopless Algorithm H).[^gray] A `±1` change at column `i` touches only the two terms `max(0, c_i − c_{i−1})` and `max(0, c_{i+1} − c_i)` of the block count, so `blocks(c)` is carried along in `O(1)` per step. The walk was checked to be a Hamilton path with a correct running block count on `(3, 2)`, `(4, 3)`, `(5, 4)` and `(6, 3)`.[^exec]

This is not random, but it plays the role of a sampler with zero variance: filter at emit and every moment of every statistic on `V(w, h)` comes out exactly. On `V(8, 4)` (29,201 castles) the mean block count is `205920/29201 = 7.05181` and the variance `2.30248`. Those exact values are the benchmark in the cross-check table below.[^exec]

## 5. Rank/unrank

The completion table of the transfer-matrix sampler also ranks. Order `V(w, h)` lexicographically. To unrank `n`, walk the columns and, at each one, skip past the blocks of castles that start with a smaller column value, whose sizes are the completion counts. Rank is the same walk run backwards. This gives a bijection `V(w, h) ↔ {0, …, F − 1}` in `O(wh)` per query. It was checked to be a bijection, and to list `V` in sorted order, on `(5, 3)`, `(6, 3)` and `(6, 4)`.[^exec] The proper-castle version (all `A(w, h)` castles, by the first full-height column) is the one on [[song-as-castle](pages/song-as-castle.md)] and [[hardy-ramanujan-castle](pages/hardy-ramanujan-castle.md)]. Incidentally, the `(6, 4)` cell used in the rank checks is the one with `F(6, 4) = 1729`.

The transfer-matrix sampler is unranking a uniform random integer, done lazily one column at a time. Rank/unrank adds one thing: control over which integers are fed in. Evenly spaced ranks give a stratified sample of the lexicographic order, a low-discrepancy sequence of ranks gives a quasi-Monte Carlo sample, and a single rank names a single castle reproducibly. A chi-square test on `(6, 3)` passed (`p = 0.67`), and across 60 independent runs of 40,000 draws on `(8, 4)` the z-scores of the mean block count had mean 0.11 and standard deviation 1.00, as they should.[^exec]

## 6. Heat-bath MCMC

A heat-bath (Glauber) step picks a column `i` and redraws `c_i` from its conditional law given the neighbours `a = c_{i−1}` and `b = c_{i+1}`:

```
P(c_i = x | a, b)  ∝  t^{max(0, x − a) + max(0, b − x)} · q^x,      x = 1, …, h
```

with `a = 0` at the left wall and no `b`-term at the right wall. The chain is reversible for `t^blocks q^area` on the cube.

**Run it on the cube, not on `V`.** The natural alternative, a chain that stays inside `V(w, h)`, does not work. Under single-column `±1` moves, `V(w, h)` falls apart:[^exec]

| cell | `F(w, h)` | components under `±1` moves | largest | components under single-column redraws |
|---|---|---|---|---|
| `(3, 3)` | 3 | 3 | 1 | 3 |
| `(4, 3)` | 21 | 3 | 7 | 1 |
| `(6, 3)` | 307 | 8 | 84 | 1 |
| `(5, 4)` | 439 | 35 | 210 | 2 |
| `(6, 4)` | 1,729 | 35 | 462 | 1 |
| `(8, 4)` | 29,201 | 191 | 3,003 | 1 |

A `±1` move changes the block count by at most 1, and only some of the moves that change it by 0 stay inside `V`. Redrawing a whole column does better, but `(3, 2, 4, 2, 3)` in `(5, 4)` is still isolated: every single-column change of it breaks either the parity or the height. This is the same fragmentation that blocks a castle-native Gray tour ([[castle-native-gray-tour](pages/castle-native-gray-tour.md)], [[castle-move-graph-zdd](pages/castle-move-graph-zdd.md)]). The fix is the one the Gray walk already uses: run the chain on the whole cube, where it is irreducible, and keep the states that land in `V`. At `t = q = 1` that is the fraction `F / h^w`, between 0.42 and 0.50 in the cells above. On `(6, 3)` with 600,000 steps the filtered chain reproduced the exact block-count distribution on `V` to total-variation distance 0.0003 at `t = 1/2` and 0.0014 at `t = 2`.[^exec]

Wherever a transfer matrix exists, MCMC is the slower way to reach the same measure. It is on the list for weights that are not nearest-neighbour: a factor per spanning tree, per sandpile recurrent configuration, or per unit of spectral radius, none of which factor column by column.

## 7. Coupling from the past

Propp and Wilson's coupling from the past turns a monotone Markov chain into an exact sampler. Run the chain from time `−T` to 0 from the top and bottom states, reusing the same random numbers, and double `T` until the two runs agree at time 0. The common state is then an exact draw from the stationary law.[^cftp]

The heat-bath chain above is monotone, with a twist.[^exec]

- **`t ≤ 1`: monotone.** Raising either neighbour makes the conditional law of `c_i` stochastically larger. The top state is all `h` and the bottom state all 1.
- **`t > 1`: antimonotone.** Raising a neighbour makes `c_i` stochastically smaller. The column graph is a path, which is bipartite, so reversing the order on the odd columns makes the chain monotone again. The top state is then `(h, 1, h, 1, …)`.

Both were checked for every neighbour pair at `h = 2, 3, 4, 6` over a grid of `t` and `q`. `q` never matters here, because its factor does not involve the neighbours. Filtered to `V` at emit, coupling from the past passed per-castle chi-square tests on all 89 castles of `(5, 3)` (40,000 draws; `p = 0.69` at `t = 1/2`, `p = 0.17` at `t = 2`). The median coalescence time grew faster than linearly in the width: 256, 512 and 2,048 single-site updates at widths 20, 40 and 80 with `h = 5`, `t = 1/2` (the doubling schedule makes every median a power of two, so the growth rate is coarse). It also grew with `h` (2,048 at `(40, 10)`) and with `t > 1` (1,024 at `(40, 5)`, `t = 2`).[^exec]

A one-dimensional block weight does not need this sampler, since the transfer matrix already draws it exactly. It is here because it keeps working when the weight stops being one-dimensional, as long as it stays attractive: a castle field on a grid, or castles coupled by a shared height profile.

## 8. Wilson and LGV: determinantal samplers

Two objects next to castles are counted by determinants. Each has an exact sampler whose output law is determinantal.

**Wilson's algorithm on the castle graph.** A spanning tree of the castle graph ([[castle-graph](pages/castle-graph.md)]) is built by loop-erased random walks: from each vertex not yet in the tree, walk at random until you hit the tree, erase the loops, and add the path.[^wilson] The root is the sink of either sandpile model of [[sandpile-group](pages/sandpile-group.md)]: the bottom-left cell (sink model), or the whole bottom row merged into one vertex (tide model). The number of trees is `det L̃`, which is the order of the sandpile group. In every case tested, the sampler hit exactly that many distinct trees, uniformly (chi-square `p` from 0.36 to 0.98, 200 draws per tree):[^exec]

| castle | sink trees | tide trees |
|---|---|---|
| `(2, 2, 2)` | 15 | 8 |
| `(1, 3, 2, 3, 1)` | 15 | 8 |
| `(3, 3, 3)` | 192 | 95 |
| `(2, 4, 3, 4)` | 712 | 244 |

These match the group orders on [[sandpile-census](pages/sandpile-census.md)] (`Z/15` and `Z/8` for the silver rectangle `(2, 2, 2)`). The tree edges form a determinantal process whose kernel is the transfer-current matrix built from `L̃⁻¹`.[^bp] Two consequences were checked. An edge is in the tree with probability equal to the effective resistance across it; empirical and theoretical values agreed to within 0.004 on `(2, 3, 2)` (sink model) and on `(3, 3, 3)` and `(1, 3, 2, 3, 1)` (tide model), with 60,000 trees each. And the probability that two given edges are both in the tree is the 2 × 2 minor of the kernel (0.4652 measured against 0.4667 on `(2, 3, 2)`).[^exec]

**The LGV sequential sampler.** A parallelogram polyomino in an `m × n` box is a pair of vertex-disjoint lattice paths, from `(0, 1)` to `(m−1, n)` and from `(1, 0)` to `(m, n−1)`. By the Lindström-Gessel-Viennot lemma the number of such pairs is a 2 × 2 determinant of binomial coefficients.[^lgv] It equals the Narayana number `N(m + n − 1, m)`, and summing over the boxes with `m + n = s` gives the Catalan number `C_{s−1}` ([[narayana-numbers](pages/narayana-numbers.md)], [[catalan-numbers](pages/catalan-numbers.md)]). The sampler advances both paths one step at a time and chooses the joint step with probability proportional to the LGV determinant from the new positions, which is the number of non-crossing completions. It is the transfer-matrix sampler with a determinant in place of the matrix power. Every pair in the `(3, 3)`, `(4, 3)`, `(4, 4)` and `(5, 3)` boxes has probability exactly `1/det`, checked in rational arithmetic; the determinant matched brute force and Narayana for every `m, n ≤ 5`.[^exec]

**The bridge between them.** The branches of Wilson's tree are loop-erased walks, and Fomin proved that the LGV determinant formula extends to loop-erased walks on planar graphs.[^fomin] The castle graph is planar, so one determinantal framework covers both halves of this sampler. A castle itself is a single-path object (its skyline is one `U`/`R`/`D` path), so the LGV half serves the two-path neighbours of castles: parallelogram polyominoes, and any two-path reading of castles that [[spectral-analysis](pages/spectral-analysis.md)] §2 brings in later.

## 9. Wang-Landau: the block profile

Wang-Landau estimates a density of states, here `g(b)`, the number of castles in the cell with `b` blocks.[^wl] A walk over proper castles proposes single-column redraws and accepts them with probability `min(1, g(b_old)/g(b_new))`, using its running estimate of `g`; a redraw that removes the last full-height column is rejected. After each visit it raises `ln g(b)` by `ln f`, and it halves `ln f` each time the visit histogram is flat (every level above 80% of the mean). Normalized so that `Σ_b g(b) = A(w, h)`, the estimate gives every level of the block profile at once, and the even levels give `F`.

| cell | block levels | largest/smallest level | median / max relative error | `F/A` exact | `F/A` estimated |
|---|---|---|---|---|---|
| `(8, 4)` | 10 | 648 | 1.2% / 7.1% | 0.495142 | 0.494101 |
| `(12, 5)` | 21 | 8.0 × 10⁵ | 3.1% / 13.4% | 0.499412 | 0.502668 |
| `(20, 6)` | 46 | 4.0 × 10¹² | 2.0% / 27.4% | 0.500000 | 0.499747 |

(Final `ln f = 10⁻⁶`; 0.3, 0.9 and 4.8 million steps. Exact profiles from a block-weighted transfer matrix.)[^exec] The point is the dynamic range: at `(20, 6)` the rarest block count has 101 castles out of `3.6 × 10¹⁵`, and a uniform sampler would essentially never draw one. The price is accuracy. With the halving schedule the error stops shrinking at the percent level, and the estimate of the mean block count on `V(8, 4)` is 7.029 against the exact 7.052. Shrinking `ln f` as a power law in the step count instead of halving it is the known remedy.[^bp07]

For the block profile itself the block-weighted transfer matrix is exact, so Wang-Landau is here for profiles of statistics that no transfer matrix tracks: spanning-tree counts, spectral radius, sandpile clock periods.

## 10. Random-rule ensembles

The other samplers draw castles under the castle rule. This one draws the rule. A strip rule is an `h × h` 0/1 matrix saying which column heights may follow which ([[castle-strip](pages/castle-strip.md)]), and its Perron root is the growth constant of its strips. Two priors on rules:

- **Uniform over all rules of height `h`.** There are `2^{h²}` of them, and at `h ≤ 4` all 66,066 are small enough to list, as [[area-growth-census](pages/area-growth-census.md)] does. At `h = 3` the 512 rules have 18 distinct Perron roots: 1 for 219 rules, the golden ratio for 96, 2 for 75 and 0 for 25, with mean 1.418.[^exec]
- **Bernoulli rules at large `h`.** Each entry is 1 with probability `p`, independently, and the result is a random matrix. Once the Perron root (about `ph`) is set aside, the rest of the spectrum follows the random-matrix limit laws.

At `h = 1000` and `2000` a Bernoulli rule behaved as those laws predict:[^exec]

| rule | Perron root | bulk, scaled by `√(h p (1 − p))` | check |
|---|---|---|---|
| any rule, `h = 1000`, `p = 1/2` | 499.54 (`ph = 500`) | fills the unit disk (circular law) | fraction with `\|z\| < 1/2`: 0.2543 (law: 0.25); mean `\|z\|²`: 0.5003 (0.5) |
| symmetric rule, `h = 1000`, `p = 1/2` | 500.73 | fills `[−2, 2]` (semicircle) | fraction in `[−1, 1]`: 0.6076 (law: 0.6090) |
| any rule, `h = 2000`, `p = 0.3` | 600.18 (`ph = 600`) | unit disk | 0.2501 and 0.4993 |
| symmetric rule, `h = 2000`, `p = 0.3` | 600.65 | `[−2, 2]` | 0.6083 |

A symmetric rule is one where a height-`a` column may follow a height-`b` column exactly when `b` may follow `a`. Its bulk density at 0 is `1/π`, and the measured density, 0.320 and 0.318, puts `π` at 3.12 and 3.15. The circular law for matrices with independent entries is Tao and Vu's theorem.[^tv] With a random rule drawn first, any sampler above can be run under it: the transfer-matrix sampler needs only the rule matrix in place of the castle rule.

## Cross-check: seven samplers, one number

The mean block count over `V(8, 4)` is exactly `205920/29201 = 7.0518` (the Gray walk). The castle samplers, with 100,000 draws each at `t = q = 1`:[^exec]

| sampler | estimate | naive standard error |
|---|---|---|
| 1. rejection (proper castle, then parity) | 7.0485 | 0.0048 |
| 2. transfer matrix | 7.0574 | 0.0048 |
| 5. unrank of a uniform rank | 7.0527 | 0.0048 |
| 6. heat-bath chain on the cube, filtered (every 8th step) | 7.0453 | 0.0048 (understated: draws are correlated) |
| 7. coupling from the past, filtered | 7.0485 | 0.0048 |
| 9. Wang-Landau, even levels of the profile | 7.029 | (saturated schedule) |

Everything is within 1.4 standard errors of the exact value except Wang-Landau, whose bias of −0.3% matches its saturated schedule.

## Open problems

- **A chain that lives on `V`.** Which move set makes `V(w, h)` connected with moves that stay local, and what is its mixing time? This is the same question as the castle-native Gray tour, asked for random walks instead of Hamilton paths.
- **Coalescence time.** Find the growth rate in `w` of the coalescence time of the block-weighted chain (the measurements above cannot tell `w log w` from `w^{3/2}`), and how it depends on `h` and `t`. The antimonotone case `t > 1` is slower at the same `(w, h)`.
- **Peaks against cycles.** The cycle count of a permutation is logarithmic with a Gaussian limit whose variance carries `γ − π²/6`. The castle peak count is linear. Is there a statistic on the castle side whose law matches the cycle count's, not just its combinatorics?
- **A two-path reading of castles.** The LGV sampler draws parallelogram polyominoes, not castles. A bijection that turns castles, or pairs of castles, into non-crossing path families would put castles themselves into the determinantal framework.
- **Priors on rules.** Uniform and Bernoulli priors ignore what makes the castle rule special (all transitions allowed, and parity recorded by the rises). A prior concentrated near the castle rule, such as random perturbations of the all-ones matrix, would say which spectral features of the castle are stable.

## Related Concepts

- [[castle-strip](pages/castle-strip.md)] - the transfer matrix whose powers the sampler reads, and the rules that random-rule ensembles draw.
- [[castle-bdd-zdd](pages/castle-bdd-zdd.md)] - the three-part state and the top-down sampling and ranking of the ZDD, implemented here.
- [[castle-gray-code](pages/castle-gray-code.md)] - the Gray walk used as exhaustive ground truth.
- [[castle-native-gray-tour](pages/castle-native-gray-tour.md)], [[castle-move-graph-zdd](pages/castle-move-graph-zdd.md)] - the fragmentation of `V(w, h)` under local moves, the reason MCMC runs on the cube.
- [[song-as-castle](pages/song-as-castle.md)] - rank/unrank on proper castles by the first full-height column.
- [[castle-foata-transform](pages/castle-foata-transform.md)], [[castles-as-upgraded-cycle-count](pages/castles-as-upgraded-cycle-count.md)] - peaks as records, and the `(n−1)!` anchor that Sattolo samples.
- [[castle-graph](pages/castle-graph.md)], [[sandpile-group](pages/sandpile-group.md)], [[sandpile-census](pages/sandpile-census.md)] - the graph and the two sink models Wilson's algorithm runs on, and the tree counts it reproduces.
- [[spectral-analysis](pages/spectral-analysis.md)] - the LGV kernel section, the determinantal counterpart of the LGV sampler.
- [[area-growth-census](pages/area-growth-census.md)] - the exhaustive rule census that the uniform rule prior samples.
- [[castle-entropy](pages/castle-entropy.md)] - the one-bit parity clause behind `F/A → 1/2`.
- [[algebraic-transcendental-wall](pages/algebraic-transcendental-wall.md)] - why transcendental constants need limits, and so samplers.
- [[castle-notation](pages/castle-notation.md)] - the block weight `t`, area weight `q`, and the symbols introduced here.

## Footnotes

[^exec]: Verified by execution (2026-09-27): Python 3.10 with NumPy 2.2 and SciPy 1.15; exact checks in `fractions.Fraction`. Transfer-matrix `F(w, h)` against brute force for `w ≤ 7`, `h ≤ 5`; step-probability products equal to `1/F` (and to `t^blocks q^area / Z` at `t = 1/2`, `q = 2/3`) on every castle of the stated cells; rank/unrank and proper-castle unrank bijections; chi-square uniformity tests (200,000 draws per sampler on `(6, 3)`); Sattolo and Fisher-Yates choice-sequence bijections; Foata cycles-to-maxima bijection and the exact mean and variance of the cycle count on `S_n`; peaks = records on all tuples `w ≤ 7`, `h ≤ 4`; `E[peaks]` exactly at `(5, 3)` and `(6, 4)`; Gray walk and running block count; components of `V(w, h)` under `±1` moves and single-column redraws by graph search; heat-bath stochastic monotonicity for every neighbour pair at `h ∈ {2, 3, 4, 6}`, `t ∈ {0.1, 0.5, 0.9, 1, 1.1, 2, 5}`, `q ∈ {0.5, 1, 1.5}`; coupling-from-the-past chi-square and coalescence times (40 runs per cell); Wilson tree counts against `det L̃` and effective-resistance edge marginals from `L̃⁻¹`; LGV determinant against brute-force enumeration of disjoint path pairs and Narayana for `m, n ≤ 5`; Wang-Landau profiles against exact block-weighted transfer-matrix profiles; random-rule spectra with `numpy.linalg.eigvals` / `eigvalsh`. Random seeds fixed per experiment.
[^blocks]: [[project-euler-502-brute-force](pages/project-euler-502-brute-force.md)] §"Column-height encoding" L18-27 — "column heights c_1, …, c_w ∈ {1, …, h} with max c = h ... #blocks = ∑_{r=1}^{h} #{runs of columns with c_i ≥ r} = c_1 + ∑_{i=2}^{w} max(0, c_i − c_{i−1}) ... Rule 6 (even block count) is applied by parity at the end."
[^foata]: [[project-euler-502-castle-factoring](pages/project-euler-502-castle-factoring.md)] §"The castle version" L143-157 [synthesis] — the peaks of the tower are the maximal positive runs of `c`, and peak ↦ first column of its run is a bijection onto the record set `{ i : c_i > 0 and (i = 1 or c_{i−1} = 0) }`.
[^gray]: [[aocp-generating-permutations-tuples](pages/aocp-generating-permutations-tuples.md)] §"Gray Binary Code Generation Algorithm" L83-91 [synthesis] — the reflected Gray code changes one digit per step and is defined recursively by reflection; the mixed-radix generalization and Algorithm H are installed on castle-gray-code.
[^durstenfeld]: https://doi.org/10.1145/364520.364540 (1964) — R. Durstenfeld, "Algorithm 235: Random permutation", *Communications of the ACM* 7(7), p. 420.
[^sattolo]: https://doi.org/10.1016/0020-0190(86)90073-6 (1986) — S. Sattolo, "An algorithm to generate a random cyclic permutation", *Information Processing Letters* 22, 315-317.
[^cftp]: https://doi.org/10.1002/(SICI)1098-2418(199608/09)9:1/2%3C223::AID-RSA14%3E3.0.CO;2-O (1996) — J. G. Propp and D. B. Wilson, "Exact sampling with coupled Markov chains and applications to statistical mechanics", *Random Structures & Algorithms* 9, 223-252.
[^wilson]: https://doi.org/10.1145/237814.237880 (1996) — D. B. Wilson, "Generating random spanning trees more quickly than the cover time", *Proc. 28th ACM STOC*, 296-303.
[^bp]: https://doi.org/10.1214/aop/1176989121 (1993) — R. Burton and R. Pemantle, "Local characteristics, entropy and limit theorems for spanning trees and domino tilings via transfer-impedances", *Annals of Probability* 21(3), 1329-1371.
[^lgv]: https://doi.org/10.1016/0001-8708(85)90121-5 (1985) — I. Gessel and G. Viennot, "Binomial determinants, paths, and hook length formulae", *Advances in Mathematics* 58(3), 300-321.
[^fomin]: https://arxiv.org/abs/math/0004083 (2001) — S. Fomin, "Loop-erased walks and total positivity", *Transactions of the AMS* 353, 3563-3583.
[^wl]: https://doi.org/10.1103/PhysRevLett.86.2050 (2001) — F. Wang and D. P. Landau, "Efficient, multiple-range random walk algorithm to calculate the density of states", *Physical Review Letters* 86, 2050-2053.
[^bp07]: https://doi.org/10.1063/1.2803061 (2007) — R. E. Belardinelli and V. D. Pereyra, "Wang-Landau algorithm: a theoretical analysis of the saturation of the error", *Journal of Chemical Physics* (arXiv cond-mat/0702414): the error saturates when the refinement parameter shrinks exponentially, and scaling it down as a power law removes the saturation.
[^tv]: https://arxiv.org/abs/0807.4898 (2010) — T. Tao and V. Vu, "Random matrices: universality of ESDs and the circular law", *Annals of Probability* 38(5), 2023-2065.
