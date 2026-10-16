---
title: Castle Gray code
category: Concepts
summary: The reflected Gray code on the cube {1..h}^w, which changes one column by ±1 per step, applied to castles: worked at (w, h) = (3, 2) for h = 2 and by the loopless Gray algorithm (Algorithm H of TAOCP §7.2.1.1) for every h. A one-column step changes the block count by at most 1, so the sign (−1)^blocks and the signed count S update in O(1) per step, and the tour lists the even-block castles of width w and height h, the A^e(w, h) of the cube's three parts (improper tuples, odd-block castles, even-block castles), at O(1) cost per tuple of the cube.
tags: [concept, castle, gray-code, generation, algorithm, mixed-radix, loopless, taocp]
sources: [aocp-generating-permutations-tuples, project-euler-502-brute-force]
created: 2026-09-20
updated: 2026-10-16
---

# Castle Gray code

The castles of width `w` and height `h` lie in the cube `{1..h}^w`, which [[aocp-generating-permutations-tuples](pages/aocp-generating-permutations-tuples.md)] lists in two orders: the **odometer** of Algorithm M, which adds one with carries, and the **reflected Gray code**, which changes one coordinate per step and which the source gives for binary tuples as Algorithm G.[^1] This page walks the Gray order on castles, proves that the block count moves by at most one per step, and reads off an `O(1)` update of the sign `(−1)^{blocks(c)}` of [[castle-sign](pages/castle-sign.md)] and of the signed count `S`. The result lists the cube in `O(1)` time per tuple and keeps the even-block castles as it passes them.

## Representation and filters

A tuple `c = (c_1, …, c_w) ∈ {1..h}^w` is a castle of height `h` when `max c = h`, and an even-block castle when also `blocks(c)` is even, where[^2]

```
blocks(c)  =  c_1 + Σ_{i≥2} max(0, c_i − c_{i−1}).
```

There are `A(w, h) = h^w − (h−1)^w` castles of width `w` and height `h`, and `A^e(w, h) = (A + S)/2` of them have an even number of blocks, where `S(w, h)` is the sum of `(−1)^{blocks(c)}` over the castles; `S(w, h) = P(h−2, w) − P(h−1, w)` ([[castle-counting-formula](pages/castle-counting-formula.md)], Equations (1) and (7)).

## The three parts of `{1..h}^w`

The cube splits into three disjoint parts:

- **improper tuples**, `max c < h`, which do not reach height `h`: `(h−1)^w` of them;
- **odd-block castles**, `max c = h` and `blocks(c)` odd: `A^o(w, h) = (A − S)/2`;
- **even-block castles**, `max c = h` and `blocks(c)` even: `A^e(w, h) = (A + S)/2`.

The Gray tour visits all `h^w` tuples, tests the two conditions in `O(1)` at each visit, and keeps the even-block castles. A tour that visits only the even-block castles is a different question, treated on [[castle-native-gray-tour](pages/castle-native-gray-tour.md)].

## Algorithm M: the odometer

The brute-force enumerator of [[project-euler-502-brute-force](pages/project-euler-502-brute-force.md)] is Algorithm M with every radix equal to `h`:

```python
from itertools import product
all_castles = [c for c in product(range(1, h+1), repeat=w) if max(c) == h]
```

At `(w, h) = (3, 2)` it visits the `2^3 = 8` tuples, `2^3 − 1^3 = 7` of them castles, with `c_3` changing fastest:

| step | `c` | castle? | `blocks` | `(−1)^{blocks}` |
|-----:|:----|:-------:|:--------:|:------:|
| 0 | (1,1,1) | no  | 1 | −1 |
| 1 | (1,1,2) | yes | 2 | +1 |
| 2 | (1,2,1) | yes | 2 | +1 |
| 3 | (1,2,2) | yes | 2 | +1 |
| 4 | (2,1,1) | yes | 2 | +1 |
| 5 | (2,1,2) | yes | 3 | −1 |
| 6 | (2,2,1) | yes | 2 | +1 |
| 7 | (2,2,2) | yes | 2 | +1 |

So `A(3, 2) = 7`, `A^e(3, 2) = 6` and `S(3, 2) = 6 − 1 = 5`. At `(3, 2)` every odometer step happens to change the block count by at most one, but a carry changes several columns at once, and the block count can jump: at `(3, 3)` the step `(2,1,3) → (2,2,1)` takes it from 4 to 2, and at `(4, 4)` the step `(1,2,1,4) → (1,2,2,1)` from 5 to 2.[^3]

## Algorithm G: the Gray tour

In the **reflected Gray code**, consecutive tuples of `{1..h}^w` differ in one position by `±1`. For `h = 2` it is given by the closed form `g(k) = k xor (k >> 1)`, or step by step: the step after the `k`-th tuple, `k = 1, 2, …`, changes position `ρ(k) = ν_2(k)` counted from the fastest position, where `ν_2(k)` is the exponent of 2 in `k` (OEIS A007814: 0, 1, 0, 2, 0, 1, 0, 3, …). For every `h` the loopless Gray algorithm of the section *The loopless Gray algorithm: general h* produces it in worst-case `O(1)` time per step.[^4]

At `(w, h) = (3, 2)`, with `c_3` the fastest position, so that the bit string `b_1 b_2 b_3` is the tuple `(b_1 + 1, b_2 + 1, b_3 + 1)`:

| step | `c` | changed | Δ `blocks` | `blocks` | `(−1)^{blocks}` |
|-----:|:----|:--------|:----------:|:--------:|:------:|
| 0 | (1,1,1) | -        | -  | 1 | −1 |
| 1 | (1,1,2) | `c_3` +1 | +1 | 2 | +1 |
| 2 | (1,2,2) | `c_2` +1 |  0 | 2 | +1 |
| 3 | (1,2,1) | `c_3` −1 |  0 | 2 | +1 |
| 4 | (2,2,1) | `c_1` +1 |  0 | 2 | +1 |
| 5 | (2,2,2) | `c_3` +1 |  0 | 2 | +1 |
| 6 | (2,1,2) | `c_2` −1 | +1 | 3 | −1 |
| 7 | (2,1,1) | `c_3` −1 | −1 | 2 | +1 |

Every change of the block count is in `{−1, 0, +1}`:

**Lemma (single-column block change).** Changing one column `c_i` by `±1` changes `blocks(c)` by `−1`, `0` or `+1`.

*Proof.* With `c_0 = c_{w+1} = 0`, `blocks(c) = Σ_{i=1}^{w} max(0, c_i − c_{i−1})`. Raising `c_i` by 1 raises `c_i − c_{i−1}` by 1 and lowers `c_{i+1} − c_i` by 1, and leaves every other difference alone. The term `max(0, c_i − c_{i−1})` gains `[c_i ≥ c_{i−1}]` and the term `max(0, c_{i+1} − c_i)` loses `[c_{i+1} > c_i]`, so the block count changes by `[c_i ≥ c_{i−1}] − [c_{i+1} > c_i] ∈ {−1, 0, +1}`. Lowering `c_i` by 1 is the reverse move. ∎[^3]

The proof uses only that one column changes by `±1`, so it holds along every reflected Gray order, binary or not.

## The loopless Gray algorithm: general `h`

For every `h` the reflected Gray code is produced in worst-case `O(1)` time per step by focus pointers, as in Algorithm H of TAOCP §7.2.1.1, "Loopless reflected mixed-radix Gray generation". The Python version below shifts the digits to `1..h`; it changes the fastest position `c_1` first.[^5]

```python
def loopless_gray(w, h):
    c, d, f = [1]*w, [+1]*w, list(range(w+1))
    while True:
        yield tuple(c)
        j = f[0]
        if j == w: return
        f[0] = 0
        c[j] += d[j]
        if c[j] in (1, h):
            d[j] = -d[j]
            f[j], f[j+1] = f[j+1], j+1
```

`f[0]` names the position to change next, `d[j] ∈ {+1, −1}` is the direction of position `j`, and when position `j` reaches an end of `{1, …, h}` its direction flips and it is spliced out of the chain of focus pointers, so the next step is again found in `O(1)`.

The walk at `(w, h) = (2, 3)`, nine tuples:

| step | `c` | changed | direction | end reached? |
|-----:|:----|:-------:|:---------:|:---------|
| 0 | (1,1) | -     | -  | -                     |
| 1 | (2,1) | `c_1` | +1 | no                    |
| 2 | (3,1) | `c_1` | +1 | yes (`c_1` at the top)    |
| 3 | (3,2) | `c_2` | +1 | no                    |
| 4 | (2,2) | `c_1` | −1 | no                    |
| 5 | (1,2) | `c_1` | −1 | yes (`c_1` at the bottom) |
| 6 | (1,3) | `c_2` | +1 | yes (`c_2` at the top)    |
| 7 | (2,3) | `c_1` | +1 | no                    |
| 8 | (3,3) | `c_1` | +1 | yes (`c_1` at the top)    |

Consecutive tuples differ in one position by `±1`, and the nine tuples are all of `{1..3}^2`. At the next step `f[0] = 2 = w`, and the generator stops.[^3]

## Incremental sign and `S`

By the Lemma, the sign and the signed count update in `O(1)` along the tour. Keep a running sign `s` and a running sum `S`; at each step

```python
s *= (-1)**db      # db = change of blocks, in {-1, 0, +1}
if proper:  S += s # sum only over tuples with max(c) == h
```

where `db = [c_i ≥ c_{i−1}] − [c_{i+1} > c_i]` for a raise of `c_i` (and its negative, read before the move, for a lowering) uses only the two neighbors of the changed column. So the tour runs in `O(h^w)` visits with `O(1)` work each. The odometer instead spends `Θ(w)` on a long carry.

[[project-euler-502-brute-force](pages/project-euler-502-brute-force.md)]'s `p_signed(k, L)` computes the totals `P(k, L)` by a dynamic program over the height of the last column, in `O(k²)` operations per column; the tour gives `blocks(c)` for every tuple, and the dynamic program gives only the sums.

## Filtering

Two `O(1)` tests run along the tour:

- **height `h` reached**: keep the number `m_h` of positions with `c_i = h`; a `±1` change moves `m_h` by at most 1, and `max c = h` exactly when `m_h ≥ 1`;
- **even block count**: the running sign `s = +1`.

The fraction of the cube that are castles of height `h` is `1 − ((h−1)/h)^w`, which tends to 1 as `w` grows, and among them the fraction with an even number of blocks is `A^e/A = (1 + S/A)/2`. `S/A` tends to 0 as `w` grows, since the spectral radius of the signed transfer matrix `M̃_{h−1}` is less than `h` ([[castle-graph-spectral-radius](pages/castle-graph-spectral-radius.md)]), so for fixed `h` and large `w` the tour keeps about half of the tuples it visits.

## Other generation methods for castles

- [[aocp-generating-permutations-tuples](pages/aocp-generating-permutations-tuples.md)] - Algorithms M and G as Knuth's notes state them.
- [[project-euler-502-brute-force](pages/project-euler-502-brute-force.md)] - `brute(w, h)`, Algorithm M with the castle and parity filters, and the dynamic program `p_signed`.
- [[castle-snippets](pages/castle-snippets.md)] - `all_castles(w, h)` in two lines.
- [[castle-count-algorithms](pages/castle-count-algorithms.md)] - the transfer-matrix and Kitamasa computations, which count castles without listing them.
- [[castle-native-gray-tour](pages/castle-native-gray-tour.md)] and [[castle-move-graph-zdd](pages/castle-move-graph-zdd.md)] - whether the even-block castles alone admit a Gray tour: at `(3, 2)` the castles of height 2 alone have a bump tour, the even-block ones need swaps as well, and at `(3, 3)` the three even-block castles are joined by no bump or swap.

Heap's algorithm and the Steinhaus-Johnson-Trotter algorithm list permutations, which reach castles through the correspondence of [[permutation-cycle-castle-analogy](pages/permutation-cycle-castle-analogy.md)] and [[castle-foata-transform](pages/castle-foata-transform.md)], not through the cube `{1..h}^w`.

## Entities & Concepts

- [[aocp-generating-permutations-tuples](pages/aocp-generating-permutations-tuples.md)] - Algorithms M and G and the ruler function `ρ(k)`.
- [[project-euler-502-brute-force](pages/project-euler-502-brute-force.md)] - the block-count formula and the dynamic program `p_signed`.
- [[castle-sign](pages/castle-sign.md)] - the sign `(−1)^{blocks}` and the split of a set into even-block and odd-block members.
- [[castle-counting-formula](pages/castle-counting-formula.md)] - `A^e(w, h) = (A + S)/2` with `A = h^w − (h−1)^w`.
- [[castle-snippets](pages/castle-snippets.md)] - `all_castles`, `blocks`, and the shape predicates.
- [[castle-count-algorithms](pages/castle-count-algorithms.md)] - the computations that count castles without listing them.

## Related Concepts

- [[castle-representations](pages/castle-representations.md)] - the column-height tuple on which the tour runs, beside the binary and step-string encodings.
- [[monotone-streak-factorization](pages/monotone-streak-factorization.md)] - the up-streaks, flat runs and down-streaks of a skyline; a single-column change edits at most the streaks at that column.
- [[castle-entropy](pages/castle-entropy.md)] - the information content of the even-block condition, `log₂ A^e = log₂ A − 1 + log₂(1 + S/A)`.
- [[block-count-constraints](pages/block-count-constraints.md)] - selecting castles by block count modulo `m`; the running `S` is the case `m = 2`.
- [[castle-samplers](pages/castle-samplers.md)] - the Gray walk as exhaustive ground truth for the random castle samplers.
- [[aocp-generating-partitions](pages/aocp-generating-partitions.md)] - a different Algorithm H, the Hindenburg algorithm of §7.2.1.4 for partitions into `m` parts.

## Footnotes

[^1]: [[aocp-generating-permutations-tuples](pages/aocp-generating-permutations-tuples.md)] §"Algorithm M" L35-39, §"Algorithm G" L143, L168-169 - "Algorithm M = mixed radix generation algorithm", "This algorithm visits all n-tuples by repeatedly adding 1 to the mixed-radix number until overflow occurs", "Algorithm G = gray binary generation algorithm", "after kth time performing this step, j = rho(k) (rho is the ruler function)". The notes treat only the binary Gray code.
[^2]: [[project-euler-502-brute-force](pages/project-euler-502-brute-force.md)] §"Column-height encoding" L18-24 - "column heights c_1, …, c_w ∈ {1, …, h} with max c = h", "#blocks = ∑_{r=1}^{h} #{runs of columns with c_i ≥ r} = c_1 + ∑_{i=2}^{w} max(0, c_i − c_{i−1})".
[^3]: Verified by execution (Python 3.11, 2026-10-16): both `(3, 2)` tables; the odometer jumps `4 → 2` at `(3, 3)` and `5 → 2` at `(4, 4)`; the Lemma, with the exact change `[c_i ≥ c_{i−1}] − [c_{i+1} > c_i]`, on every raise of every tuple for `w ≤ 6`, `h ≤ 4`; the `(2, 3)` walk; and, for `w ≤ 6`, `h ≤ 4`, that `loopless_gray` visits each tuple of `{1..h}^w` once with one position changing by `±1` per step.
[^4]: https://oeis.org/A007814 (read 2026-10-16) - "Exponent of highest power of 2 dividing n", `0, 1, 0, 2, 0, 1, 0, 3, …` from `n = 1`. In the `(3, 2)` table the steps 1 to 7 change the positions `c_3, c_2, c_3, c_1, c_3, c_2, c_3`, that is `ρ(k) = 0, 1, 0, 2, 0, 1, 0` counted from `c_3`.
[^5]: Knuth, *The Art of Computer Programming* Vol. 4A §7.2.1.1, Algorithm H, "Loopless reflected mixed-radix Gray generation" (quoted from a copy that is not in the repository and was not re-read): focus pointers `f_0, …, f_n` and directions `o_1, …, o_n`; at each step `j ← f_0`, stop if `j = n`, else `f_0 ← 0`, `a_j ← a_j + o_j`, and if `a_j` reaches an end, flip `o_j` and set `f_j ← f_{j+1}`, `f_{j+1} ← j + 1`. The Python version is checked by running it (footnote 3).
