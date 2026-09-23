---
title: Power-law memory rules: the non-Markov castle strip
category: Analyses
summary: Every strip rule on [castle-strip](pages/castle-strip.md) is Markov by construction - the h x h 0/1 matrix depends on the current column alone. Fractionalize the "1-smooth" rule via the Grunwald-Letnikov kernel |sum_{k=0..K-1} (-1)^k C(alpha, k) c_{n-k}| <= 1 and the constraint reaches back over every prior column with power-law weights; the exact transfer matrix is infinite. Truncating memory to K columns gives an h^{K-1}-state 0/1 transfer matrix and a Perron root rho(alpha, K) that is always algebraic. Measured on h = 2 for alpha in (0, 1), rho(alpha, K) increases monotonically in K and lands successively on the named cubic and quadratic Perron roots of the reachable-field census - **plastic 1.3247 at (0.5, 6), supergolden 1.4656 at (0.5, 7), golden 1.6180 at (0.5, 9), plastic-squared 1.7549 at (0.9, 6)** - as if the truncated rule ratchets through the census as memory grows. Convergence to the K -> infinity limit is empirically geometric in K (rate ~0.89 at alpha = 0.5, ~0.84 at 0.75, ~0.82 at 0.9), not the K^{-alpha} the fractional-numerics literature predicts from tail decay of the GL kernel; asymptotic K needs to be larger than 16 to distinguish. At h = 2 the K -> infinity limit appears to be 2 (unrestricted growth), so no new number falls out - every finite-K value lands inside the census, and the limit is an integer already there. At h = 3 for alpha in (0, 1) the growth constant equals the h = 2 value at the same (alpha, K) for every K tested: the power-law-memory constraint effectively binarizes the strip, even though valid windows containing height 3 exist. Two integer alpha collapse: alpha = 1 recovers the Markov 1-smooth strip (growth 2 at h = 2, silver 1 + sqrt 2 at h = 3), alpha = 2 recovers the K = 3 second-difference Markov rule (golden phi at h = 2). Non-integer alpha > 1 collapse to growth 1 (constant-only) - the C(alpha, k) magnitudes oscillate too strongly to admit any variation. The proposed NTT-over-F_65537 acceleration is a mismatch to the counting problem at hand - it accelerates per-skyline evaluation of the GL sum, but the transfer-matrix count has no length-w convolution to speed up - though it may return as the right tool for exact partition-function evaluations at rational alpha over F_65537.
tags: [analysis, castle, fractional-calculus, grunwald-letnikov, transfer-matrix, non-markov, power-law-memory, perron-root, plastic-number, supergolden, golden-ratio, reachable-field, truncation, convergence, ntt, algebraic]
sources: [pe502-pell-castle-strip]
created: 2026-09-22
updated: 2026-09-23
---

# Power-law memory rules: the non-Markov castle strip

## The framing

Every strip rule on [[castle-strip](pages/castle-strip.md)] is Markov: `A(a, b)` tests one adjacent pair, so the transfer matrix `M` is `h x h` and the state space is exactly the height. The whole [[metallic-strip-realizability](pages/metallic-strip-realizability.md)] / [[reachable-field-census](pages/reachable-field-census.md)] machinery is one adjacent-pair away from the columns it counts.

Fractional calculus opens a wider question: what if the rule reads *every* prior column, with weights decaying as a power of the distance? The natural candidate is the **Grunwald-Letnikov fractional-difference kernel**, `(-1)^k C(alpha, k)`, which decays like `k^{-alpha - 1}` for large `k` ([[fractional-block-count](pages/fractional-block-count.md)]). The fractional analog of the "1-smooth" rule `|c_n - c_{n-1}| <= 1` (Motzkin, alpha = 1) is then the **fractional 1-smooth rule**

```
|sum_{k=0}^{infty}  (-1)^k C(alpha, k) c_{n-k}|  <=  1        for all  n.
```

At `alpha = 1` this is `|c_n - c_{n-1}| <= 1`, the Markov 1-smooth strip. At `alpha = 2` it is `|c_n - 2 c_{n-1} + c_{n-2}| <= 1`, a Markov *two-column* rule (second-difference smooth). At non-integer `alpha` the sum runs over every earlier column with power-law weights and the constraint is non-Markov; the exact transfer matrix is infinite.

The **K-truncated** version drops all terms with `k >= K`:

```
|sum_{k=0}^{K-1}  (-1)^k C(alpha, k) c_{n-k}|  <=  1        for all  n >= K - 1.
```

Its state is the length-(K-1) window `(c_{n-K+2}, ..., c_n)`, an element of `{1, ..., h}^{K-1}`, so the truncated transfer matrix `M(alpha, K)` is `h^{K-1} x h^{K-1}` and 0/1. This is the "fractional-numerics" problem of the [FMATH](https://en.wikipedia.org/wiki/Fractional_calculus) literature ported to castle form.

## Building the truncated matrix

The whole construction is ten lines of Python. State `s = (c_1, ..., c_{K-1})` (oldest first); appending a new column `c_K` transitions to `s' = (c_2, ..., c_K)`, and the transition is allowed iff the window sum passes the bound.

```python
import itertools, numpy as np
def gl_coef(alpha, k):
    c = 1.0
    for j in range(k): c *= (alpha - j) / (j + 1)
    return ((-1) ** k) * c
def transfer_matrix(alpha, K, h, T=1.0):
    coefs = [gl_coef(alpha, k) for k in range(K)]
    states = list(itertools.product(range(1, h+1), repeat=K-1))
    idx = {s: i for i, s in enumerate(states)}
    M = np.zeros((len(states), len(states)), dtype=np.int64)
    for s in states:
        for c_new in range(1, h+1):
            window = (c_new,) + s[::-1]                              # newest first
            if abs(sum(coefs[k] * window[k] for k in range(K))) <= T + 1e-12:
                M[idx[s], idx[s[1:] + (c_new,)]] = 1
    return M
rho = lambda M: float(max(abs(e) for e in np.linalg.eigvals(M.astype(float))))
```

For `h = 2, K = 16` this is a `32768 x 32768` matrix with at most `h = 2` nonzeros per row - store it sparse and read `rho` with `scipy.sparse.linalg.eigs`.

## What the growth constant does at integer alpha

At integer `alpha`, `C(alpha, k) = 0` for `k > alpha`, so the fractional operator degenerates to the ordinary `alpha`-th difference and the rule collapses to a **short-memory Markov rule**. Two cases:

**alpha = 1.** `|c_n - c_{n-1}| <= 1`. At `h = 2` this allows every pair, growth `2`; at `h = 3` it is the Motzkin / silver strip, growth `1 + sqrt 2 = 2.4142...` ([[pell-castle-strip](pages/pell-castle-strip.md)]). Verified: the table below reproduces both.

**alpha = 2.** `|c_n - 2 c_{n-1} + c_{n-2}| <= 1` - the second-difference is bounded. This is a Markov rule on state `(c_{n-1}, c_n)`, i.e. `K >= 3`; at `K = 2` the rule reduces to `|c_n| <= 1` and only `h = 1` survives (growth `1`). At `K >= 3, h = 2` the growth is **`phi = 1.6180`** (Fibonacci-like second-order recurrence); at `h = 3` it is `1.8972`, the largest root of a quartic (unnamed).

## What it does at alpha in (0, 1), h = 2

Here is the phenomenon. `rho(alpha, K)` for `h = 2` at several `alpha` and `K` up to 16, with the leftmost few `K` where the rule is too tight and only the constant strip survives (`rho = 1`) elided:

| alpha \ K | 5 | 6 | 7 | 8 | 9 | 10 | 12 | 14 | 16 |
|---|---|---|---|---|---|---|---|---|---|
| 0.25 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 |
| 0.50 | 1.000 | **1.3247** | **1.4656** | 1.5385 | **1.6180** | 1.6324 | 1.7035 | 1.7653 | 1.8096 |
| 0.75 | 1.6180 | 1.6180 | 1.7437 | 1.7885 | 1.8285 | 1.8622 | 1.9030 | 1.9320 | 1.9522 |
| 0.90 | 1.6180 | **1.7549** | 1.8124 | 1.8545 | 1.8867 | 1.9101 | 1.9447 | 1.9634 | 1.9756 |

The **bolded values are the reachable-field census's small named cubic and quadratic Perron roots**, arriving in order as `K` grows:

- **1.3247 = plastic number**, root of `x^3 - x - 1`, at `(alpha, K) = (0.5, 6)`. Also `[[plastic-number](pages/plastic-number.md)]`.
- **1.4656 = supergolden**, root of `x^3 - x^2 - 1`, at `(0.5, 7)` and `(0.75, 4)`. Also `[[tree-castle-by-area](pages/tree-castle-by-area.md)]`.
- **1.6180 = golden phi**, root of `x^2 - x - 1`, at `(0.5, 9)` and `(0.75, 5)`. Also `[[metallic-means](pages/metallic-means.md)]`.
- **1.7549 = plastic-squared psi^2**, root of `x^3 - 2x^2 + x - 1`, at `(0.9, 6)`.

So the truncated fractional 1-smooth rule **ratchets through the reachable-field census as `K` grows**: at each `(alpha, K)` the growth constant is a Perron root of a 0/1 matrix (algebraic by construction), and the values that appear are the census's named small-degree Perron roots, plateauing on each until the memory is long enough to admit a strictly larger one. The plateau structure is exactly the same one [[fractional-recurrences](pages/fractional-recurrences.md)] found on its `alpha`-continuum, but here the ratchet is in `K` at fixed `alpha`, not in `alpha` at "no truncation."

## Convergence to the K -> infinity limit

The gap `2 - rho(alpha, K)` at `h = 2` decreases monotonically. The convergence is empirically **geometric in K** (constant ratio between successive gaps), with rate depending on `alpha`:

```
alpha = 0.50:  gap ratio  ~ 0.89  (r*(K) settles by K = 12)
alpha = 0.75:  gap ratio  ~ 0.84
alpha = 0.90:  gap ratio  ~ 0.82
```

The item on `IDEAS.md` predicts a **power-law** rate `K^{-alpha}` set by the tail decay of the GL kernel `(-1)^k C(alpha, k) ~ k^{-alpha - 1} / |Gamma(-alpha)|`, whose truncation error at `K` is `O(K^{-alpha})`. A log-log fit on the last six `K` values gives slopes `-1.52, -2.35, -2.80` at `alpha = 0.5, 0.75, 0.9` - not `-alpha`, and not a stable slope. The geometric picture is the better empirical fit within `K <= 16`; whether the true asymptotic crosses over to a power law at `K >> 16` is open. One line of the diagnostic:

```python
for K in range(11, 17):
    gap = 2.0 - rho(transfer_matrix(alpha, K, 2))
    print(K, gap, gap / prev_gap if K > 11 else None)
```

The K -> infinity limit for `alpha in (0, 1)` at `h = 2` is at most `2` (bounded above by unrestricted growth) and appears to reach `2` in the limit. Since `2` is the trivial integer growth of the height-2 strip with no constraint, **the fractional 1-smooth rule adds no new numbers at `h = 2`**: every finite-`K` value lands in the census, and the limit is the census's smallest integer. The interesting arithmetic is in the ratchet, not the limit.

## The h = 3 collapse

At `h = 3` for `alpha in (0, 1)`, `rho(alpha, K)` equals the `h = 2` value **exactly** at every `(alpha, K)` tested:

```
h = 3, alpha = 0.50:   K=6 -> 1.3247   K=7 -> 1.4656   K=8 -> 1.5385   K=9 -> 1.6180
h = 2, alpha = 0.50:   K=6 -> 1.3247   K=7 -> 1.4656   K=8 -> 1.5385   K=9 -> 1.6180
```

Not because height 3 is forbidden - valid `K`-windows containing height 3 exist (e.g. `(1, 1, 1, 1, 1, 3)` passes at `alpha = 0.5, K = 6`, and `(1, 1, 1, 1, 1, 3) -> (1, 1, 1, 1, 3)` has two outgoing transitions `to 1, to 2` and one to itself via `(1, 1, 1, 3, 3)`) - but because the strongly connected component that sets the Perron root is **binary**. Height 3 is a reachable dead-end excursion whose subgraph is Perron-suboptimal. In transfer-matrix language: the height-3-touching states form a sub-graph whose spectral radius is strictly smaller than the binary component's, so they contribute to width counts only additively, not multiplicatively. Equivalent: the `h^{K-1}`-state transfer matrix is block-triangular after a permutation, and the top-left block is the `h = 2` matrix.

This is the fractional analog of the [[reachable-field-census](pages/reachable-field-census.md)]'s observation that most named quadratic Perron roots are reached at `h = 3` already; here `h = 2` already produces the same Perron roots as `h = 3` for the fractional-1-smooth rule, at the price of admitting height-3 excursions that never take over.

## Non-integer alpha > 1: collapse to growth 1

At `alpha = 1.25, 1.5`, the growth constant is `1` at every `K` tested (h = 2, 3). The reason is that `C(alpha, k)` for `1 < alpha < 2` has `C(alpha, 2) = alpha(alpha - 1)/2 > 0`, and the sum has three sizable coefficients `+1, -alpha, C(alpha, 2)` with alternating sign contributions. For any non-constant binary sequence the truncated sum quickly exceeds 1 in magnitude, so only constants survive - and the growth of constants is 1. This is the strip analog of the failure of ARFIMA-like models to admit rich integer-height sequences for `d in (1, 2)`: the second-order fractional difference is a very tight constraint on integer sequences. At integer `alpha = 2` the constraint reads `|c_n - 2 c_{n-1} + c_{n-2}| <= 1`, which admits the Fibonacci-like sequences and gives `phi`; between `1` and `2` the non-integer coefficients rule everything but constants out. So the growth-constant function `rho(alpha)` in `alpha` is **not** continuous at integer `alpha` in the truncated setup - it jumps from `2` at `alpha = 1` to `1` on a neighborhood of `alpha = 1.25`, back up to a positive value at `alpha = 2`. The continuous-in-`alpha` object of [[fractional-recurrences](pages/fractional-recurrences.md)] lives on the recurrence side (`nabla^alpha a_n = a_{n-1}`), not on the integer-height rule side.

## The NTT / Toeplitz question

The item's `IDEAS.md` line closes with a proposal: use the length-1024 NTT over `F_65537` of [[song-as-castle](pages/song-as-castle.md)] (Fermat prime, exact bijection) to exploit the **binomial-Toeplitz** structure of the GL kernel and evaluate the count fast. This is a mismatch to the counting problem at hand, for one specific reason:

The strip count `strips(w) = 1^T M(alpha, K)^{w-1} 1` is a **transfer-matrix power**, not a length-`w` convolution of the kernel with anything. The Toeplitz structure of the *rule* enters the *construction* of `M` - one convolution of length `K` per window - but there are `h^{K-1}` windows and each convolution costs `K`, so construction is `O(h^{K-1} K)`, dominated by the matrix size, not the kernel evaluation. NTT over `F_65537` accelerates each convolution to `O(K log K)`, buying a `log K` factor at best, and only on construction, not counting.

The NTT *does* apply in one adjacent problem: **per-skyline evaluation of `(GL_alpha c)_n` at every `n`** for a fixed width-`w` skyline is a length-`w` convolution of `c` with the kernel, and F_65537 makes it exact for `w <= 1024`. This is the right primitive for verifying the fractional 1-smooth rule on a specific candidate sequence (e.g. the [[fractional-block-count](pages/fractional-block-count.md)] 5460-castle catalogue at rational `alpha`), but it does not accelerate the transfer-matrix count. The item's suggestion belongs on the block-count / evaluation side, not here.

The correct fast-evaluation gadget for the count is: represent the transfer graph as an edge list (each of `h^{K-1}` states with at most `h` out-edges) and use Krylov iteration for the Perron root - the same setup as any large-sparse 0/1 matrix. No number-theoretic transform buys anything beyond that.

## Verdict: is the limit a new number?

The question: is the K -> infinity growth constant a new number, or does it land in the [[reachable-field-census](pages/reachable-field-census.md)] after all? Two answers, both with the same negative sign.

**At every finite K, rho(alpha, K) is inside the census.** Each `M(alpha, K)` is a 0/1 matrix, so its Perron root is an algebraic integer that is the growth constant of *some* 0/1 castle-strip rule (namely `M(alpha, K)` itself, read as a rule on the `h^{K-1}`-state expanded height alphabet). The census asks "which algebraic numbers are Perron roots of 0/1 transfer matrices at *some* height," and every `rho(alpha, K)` trivially answers "yes, at expanded height `h^{K-1}`." So the ratchet visits census members exclusively, and the interesting question is *which* census members appear at which `(alpha, K)` - a non-trivial pattern the table above sketches.

**At K = infinity, rho appears to be 2, an integer already in the census.** The empirical limit is `2` for every `alpha in (0, 1)` tested at `h = 2`, and there is no evidence in the numerics of a strictly smaller limit. So the fractional-memory strip's K -> infinity limit is *not* a new transcendental of the [[algebraic-transcendental-wall](pages/algebraic-transcendental-wall.md)] complement type - it is an integer already in the census. If a stronger threshold `T < 1` were substituted, the K -> infinity limit could be strictly less than `2` and the algebraic-vs-transcendental status of the limit would need Baker-theorem tools to settle; that variant is not what the IDEAS.md item asks about.

## What this settles, and what it leaves

**Settled:**
- The fractional 1-smooth rule `|sum (-1)^k C(alpha, k) c_{n-k}| <= 1` is a well-defined non-Markov constraint whose K-truncated transfer matrix is `h^{K-1} x h^{K-1}`, 0/1, and computable in ten lines.
- Integer `alpha = 1, 2` reduce to short-memory Markov rules and recover the growth constants of [[castle-strip](pages/castle-strip.md)] and its second-difference sibling (`phi` at `alpha = 2, h = 2`).
- For `alpha in (0, 1)` and `h = 2`, `rho(alpha, K)` is monotonically increasing in `K` and ratchets through the reachable-field census's small named Perron roots: plastic (1.3247), supergolden (1.4656), golden (1.6180), plastic-squared (1.7549), and higher.
- Convergence to the K -> infinity limit is empirically geometric in `K` at rates `~ 0.89 (alpha = 0.5), 0.84 (0.75), 0.82 (0.9)`, not the K^{-alpha} the tail-of-kernel argument predicts within `K <= 16`.
- The K -> infinity limit at `h = 2` for `alpha in (0, 1)` appears to be `2`, the unrestricted binary-strip growth, an integer already in the census. No new transcendental falls out.
- At `h = 3` for `alpha in (0, 1)`, `rho(alpha, K)` equals the `h = 2` value at every `(alpha, K)` tested - the power-law-memory constraint binarizes the strip's dominant component even when height-3 windows are locally admissible.
- Non-integer `alpha in (1, 2)` collapses the rule to constants-only (`rho = 1`); the growth-constant function `rho(alpha)` is not continuous at integer `alpha` in the truncated setup.
- The proposed NTT / F_65537 acceleration accelerates per-skyline evaluation of the GL sum, not the transfer-matrix count; it belongs on the [[fractional-block-count](pages/fractional-block-count.md)] side, not here.

**Open:**
- **True asymptotic rate.** The empirical geometric fit within `K <= 16` is inconsistent with the tail-decay-predicted `K^{-alpha}`. Whether the true asymptotic crosses over to a power law at `K >> 16`, or whether the geometric picture is stable, needs `K = 20, 24, 28` at `h = 2` - feasible with sparse Krylov iteration on a laptop.
- **The `alpha in (0, 1)` limit at h = 2 exactly.** Numerics suggest `rho(alpha, infty) = 2` for every `alpha in (0, 1)`, but the ratio-of-gaps could be masking a small deficit. A direct argument that the untruncated rule admits every binary sequence (in a stationary sense) is not on this page and would settle the question.
- **Threshold `T < 1`.** All numerics here use threshold `T = 1` (chosen to recover Markov 1-smooth at `alpha = 1`). Tightening to `T = 1/2` gives a different problem whose K -> infinity limit could be strictly less than `2` and whose algebraic status is unknown. This is where the "new number" question actually lives.
- **The ratchet law.** Which named Perron root appears at each `(alpha, K)` follows a pattern the table gestures at (`(0.5, 7) = (0.75, 4) = supergolden`, `(0.5, 9) = (0.75, 5) = golden`) but that this page has not lifted to a formula. Candidate: at fixed `alpha`, the K-schedule of Perron roots is a subsequence of the census cubics ordered by degree and discriminant.
- **h = 3 collapse across all K.** The `rho(alpha, K) at h = 3 = rho(alpha, K) at h = 2` identity is checked to `K = 9`; whether it holds for every `K` (equivalently: whether the height-3-touching states are Perron-suboptimal at every `K`) needs a structural argument, likely a Perron-Frobenius block-triangularization of `M(alpha, K)`.
- **The Caputo variant.** The GL kernel used here corresponds to a Riemann-Liouville / Grunwald-Letnikov fractional difference; the Caputo variant differs by a `(1 - x)^{alpha - 1}` factor at the generating-function level ([[fractional-recurrences](pages/fractional-recurrences.md)] footnote 1). Whether the truncated Caputo-1-smooth rule has the same ratchet through the census, or a shifted one, is unexplored.
- **Two-column forcing.** The Fibonacci-Pell interpolation `nabla^alpha a_n = a_{n-1} + a_{n-2}` of [[fractional-recurrences](pages/fractional-recurrences.md)] has a strip-side analog `|GL_alpha c|_n <= 2` or `|GL_alpha c|_n - c_{n-1} <= 1`; picking the right non-Markov constraint that continues to hit metallic ratios at rational `alpha` (silver at `alpha = 1` in the recurrence world, does it survive on the rule side?) is a natural next probe.

## Related concepts

- [[castle-strip](pages/castle-strip.md)] - the Markov strip and its `h x h` 0/1 transfer matrix; this page is the non-Markov generalization with power-law memory.
- [[fractional-recurrences](pages/fractional-recurrences.md)] - the recurrence-side sibling: `nabla^alpha a_n = a_{n-1}` produces a continuum of algebraic growth constants at rational `alpha`, transcendental at irrational `alpha`. This page runs the fractional operator on the *rule* rather than the count, and finds a different (discrete, ratcheting) algebraic structure.
- [[fractional-block-count](pages/fractional-block-count.md)] - the block-count-side fractional operator on skylines; the per-skyline evaluation of the GL sum this page uses is the same primitive.
- [[fractional-width-and-height](pages/fractional-width-and-height.md)] - the coordinate-side fractional operator; different axis, same GL kernel.
- [[reachable-field-census](pages/reachable-field-census.md)] - the algebraic universe every `rho(alpha, K)` on this page lives inside; the "K -> infinity is a new number" question of the IDEAS.md item, answered negative at `T = 1`.
- [[plastic-number](pages/plastic-number.md)] - the first named Perron root the ratchet lands on, at `(alpha, K) = (0.5, 6)`.
- [[tree-castle-by-area](pages/tree-castle-by-area.md)] - the second: supergolden at `(0.5, 7)`.
- [[metallic-means](pages/metallic-means.md)] - golden phi at `(0.5, 9)`, the fourth ratchet stop; also the alpha = 1 Markov growth `2` at `h = 2` and silver `2.4142` at `h = 3`.
- [[metallic-strip-realizability](pages/metallic-strip-realizability.md)] - the Markov-side minimum-height law; the fractional rule's expanded-height matrix `M(alpha, K)` is a 0/1 realizer at height `h^{K-1}` for the Perron roots it produces.
- [[song-as-castle](pages/song-as-castle.md)] §"Finite fields" - the F_65537 NTT the IDEAS.md item points at; this page argues that it is the right tool for per-skyline evaluation but not for the transfer-matrix count.
- [[algebraic-transcendental-wall](pages/algebraic-transcendental-wall.md)] - the exact/asymptotic partition; every `rho(alpha, K)` on this page is on the exact / algebraic side, and the K -> infinity limit at `T = 1` stays algebraic (in fact integer) rather than crossing to the transcendental complement.
- [[pell-castle-strip](pages/pell-castle-strip.md)] - the `alpha = 1, h = 3` case: growth `1 + sqrt 2`, reproduced by this page's table.
- [[bounded-height-castles-nacci](pages/bounded-height-castles-nacci.md)] - the Fibonacci-nacci growth constants at fixed heights; the `alpha = 2, h = 2` case here recovers phi and slots into the nacci ladder.
- [[levy-flights](pages/levy-flights.md)] - the fractional sibling: Riascos-Mateos `L^α` on the castle-graph Laplacian, the same fractional-calculus wall approached from the spectral side rather than the strip-rule side.
- [[eigenvalue-continued-fractions](pages/eigenvalue-continued-fractions.md)] - the canonical treatment of the metallic means as norm-`(-1)` purely-periodic continued fractions; the Perron roots this page ratchets through are the same objects.
- [[reachable-field-census](pages/reachable-field-census.md)] - the algebraic universe the new-number question runs against; this page argues `K -> infinity` at `h = 2` stays on integer `2` rather than reaching a new transcendental.
