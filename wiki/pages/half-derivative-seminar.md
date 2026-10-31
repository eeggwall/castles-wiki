---
title: Half-derivative seminar - castles at order 1/2
category: Concepts
summary: A seminar on four integer-order castle operations at order 1/2. The fractional block count B_α runs from the area at α = 0 to the block count at α = 1, and B_{1/2} separates the ten even-block castles of width 4 and height 2. The half-sum of a castle row tends to √(h/(h − 1)) times the row, with √π only in the remainder, and π = lim w 16^w/bhalf_4(w)² once the branch point sits on the pole. A^e(w, h) is real at real width for h ≤ 41 and complex at half-integer height, A^e(4, 2.5) = 16.75 + 6i, because the parity's eigenvalue −1 lies on the branch cut. Among the rules I + N with N acyclic, the nonnegative principal square roots are exactly the partial orders through height 6, and not at height 7. On the battlement (1, h, 1, h, …), the tree castle whose heights alternate 1 and h, the walk spreads like 4√(2t/π) while its teeth look infinite and like 2t/(h + 1) after t ≈ 8(h + 1)²/π.
tags: [concept, castle, seminar, pedagogy, teaching, fractional-calculus, grunwald-letnikov, riemann-liouville, half-sum, interpolation, branch-cut, square-root, partial-order, comb, random-walk, subdiffusion]
sources: [project-euler-502-solution, project-euler-502-brute-force, algebraic-languages-and-polyominoes-enumeration, arkhincheev-baskin-1991-comb-model, pach-tardos-2013-range-of-random-walk-on-comb]
created: 2026-10-29
updated: 2026-10-31
---

# Half-derivative seminar - castles at order 1/2

**Thesis.** Four operations the castle already uses have an integer order: the column difference whose positive parts count the blocks, the partial sum of a count sequence, the power of a transfer matrix that adds a column or a height, and the time step of a random walk on the castle graph. Each has a version of order 1/2, built from the series `(1 − x)^{±1/2}` or from an eigenvalue raised to a half-integer power.

**Structure.** Seven stops (0 to 6). The Snippet at the end reproduces the worked values;[^exec] the censuses and long computations are on the pages behind the stops, [[fractional-block-count](pages/fractional-block-count.md)] (Stop 1), [[half-sum-castles](pages/half-sum-castles.md)] (Stop 2), [[fractional-width-and-height](pages/fractional-width-and-height.md)] (Stops 3 to 5), and [[tree-castle-diffusion](pages/tree-castle-diffusion.md)] with [[levy-flights](pages/levy-flights.md)] (Stop 6). Notation follows [[castle-notation](pages/castle-notation.md)].

## Stop 0 - one series

A castle of width `w` and height `h` is a skyline `(c_1, …, c_w)` with heights in `1..h` and some column of height `h`; its blocks are the maximal runs of cells in each row, and `A^e(w, h)` counts the castles with an even number of blocks, the count of Project Euler 502 ([[castle-counting-function](pages/castle-counting-function.md)]). Write a skyline as the polynomial `𝒞(x) = Σ_i c_i x^i` and a count sequence as its generating function.

- The **column difference** `c_i − c_{i−1}` is multiplication by `(1 − x)`. The block count is the sum of its positive parts, the total ascent, since a column of height `b` after one of height `a` starts `max(0, b − a)` new blocks.[^bf]
- The **partial sum** of a count sequence is multiplication by `(1 − x)^{−1}`.
- **Adding a column** multiplies by a transfer matrix `M`, so width `w` is a power `M^{w−1}`, and the count is a combination of the powers `λ_j^w` of its eigenvalues.

The series `(1 − x)^α = Σ_k (−1)^k C(α, k) x^k`, with `C(α, k) = α(α − 1)⋯(α − k + 1)/k!` the generalized binomial coefficient (the binomial coefficient at whole `α`), gives the first two at every real order `α`, and `λ^w = exp(w log λ)` makes the third sense for real `w` once a branch of the logarithm is chosen. At order 1/2 the two series are

```
(1 − x)^{1/2}   :  1, −1/2, −1/8, −1/16, −5/128, −7/256, −21/1024, …
(1 − x)^{−1/2}  :  1,  1/2,  3/8,  5/16,  35/128, 63/256, 231/1024, …   =  C(2k, k)/4^k  ~  1/√(πk)
```

and their product is 1, so a half-difference followed by a half-sum gives the skyline back, and two half-sums give the ordinary partial sum. The partial sums of the second series, the half-sum of the constant sequence 1, are `(2n + 1) C(2n, n)/4^n ~ 2√(n/π)`. On a skyline every sum stops at the wall before column 1, and the laws survive: the operator multiplies by the series and drops the powers past `x^w`, and dropping commutes with multiplying.

*Idea:* an operation of order `α` is a power series in the shift, or an eigenvalue raised to a real power, and the order is a parameter that can be set between the integers.

## Stop 1 - between area and blocks

The Grunwald-Letnikov difference of order `α` at column `i` is `∇^α c_i = Σ_{k<i} (−1)^k C(α, k) c_{i−k}`, the coefficient of `x^i` in `(1 − x)^α 𝒞(x)`, and the **fractional block count** is `B_α = Σ_i max(0, ∇^α c_i)` ([[fractional-block-count](pages/fractional-block-count.md)]). At `α = 0` the weights are `1, 0, 0, …` and `B_0` is the area; at `α = 1` they are `1, −1, 0, …` and `B_1` is the total ascent, the block count. For `0 < α < 1` the weights after the first are negative with absolute values summing to 1, so the residual at column `i` is the amount by which `c_i` exceeds a power-law average of the columns to its left, the wall counting as height 0.

The castles `(1, 1, 1, 2)` and `(1, 1, 2, 1)` both have area 5 and two blocks. With the weights `1, −1/2, −1/8, −1/16` their residuals are `1, 1/2, 3/8, 21/16` and `1, 1/2, 11/8, −3/16`, so `B_{1/2} = 51/16 = 3.1875` and `23/8 = 2.875`; the second castle's last residual is negative and does not count. The ten even-block castles of width 4 and height 2 all have two blocks and four distinct areas, and `B_{1/2}` takes ten distinct values on them; over all 15 castles of that width and height it takes 14, and at the irrational order `√2 − 1` all 15.

On a box of `w` columns of height `h` the residuals are `h C(2j, j)/4^j` for `j < w`, so `B_{1/2}` is `h` times the half-sum of 1 at `n = w − 1`, `2hw C(2w, w)/4^w ~ 2h√(w/π)`. Reversing a skyline keeps its area and its block count but not `B_α`, since the memory runs from left to right: `(2, 1, 1, 1)` has `B_{1/2} = 5/2` against `51/16`.

*Idea:* a statistic that interpolates two integer statistics separates castles that both endpoints confuse, because its weights depend on where the cells are.

## Stop 2 - half a sum, and where the √π goes

The **half-sum** of the height-`h` row is ([[half-sum-castles](pages/half-sum-castles.md)])

```
half_h(w)  =  Σ_k  C(2k, k)/4^k · A^e(w − k, h),        Σ_w half_h(w) x^w  =  row_h(x)/√(1 − x),
```

with `row_h(x)` the rational generating function of the row. At `h = 4` it begins `1, 15/2, 279/8, 2167/16, 65483/128`.

The weight `C(2k, k)/4^k ~ 1/√(πk)` puts `√π` into the leading term of the half-sum of a sequence with radius of convergence 1, such as the constant 1 of Stop 0. A castle row grows like `h^w/2`, and its pole at `x = 1/h` dominates the branch point at `x = 1`: the half-sum scales each pole term by a constant, and

```
half_h(w)/A^e(w, h)  →  √(h/(h − 1)),
```

`√(4/3) = 1.1547005384` at `h = 4`, matched by `half_4(100)/A^e(100, 4)` to ten digits. The branch point leaves only the remainder `row_h(1)/√(πw)`, with `row_h(1) = 0, 1/2, 1/30, 1/20` for `h = 2..5`, and `row_h(1)` is minus the sum of the row continued to negative widths.

Moving the branch point onto the pole, with weights `C(2k, k)(h/4)^k`, puts `π` into the leading term: the simple pole and the branch point multiply into the leading singularity `(1 − hx)^{−3/2}`, whose coefficients grow like `2h^w√(w/π)`. At `h = 4` these weights are the integers `C(2k, k)`, and the binomial half-sum `bhalf_4(w) = Σ_k C(2k, k) A^e(w − k, 4) = 1, 9, 51, 241, 1069, 4671, 20353, …` gives

```
π  =  lim_{w → ∞}  w · 16^w / bhalf_4(w)²,
```

`3.17108` at `w = 200`, and `3.14158` at `w = 1600` after one Richardson step. `bhalf_4(w)` counts the pairs of a skyline of width `w` on the heights `1..4` and a cut, with an even-block castle of height 4 before the cut and as many columns of height 1 as of height 4 after it. Delest and Viennot's count of convex polyominoes with perimeter `2n + 8`, `(2n + 11)4^n − 4(2n + 1)C(2n, n)`, has its pole and branch point at the same place, `x = 1/4`, but the pole is double, so it wins and `√π` stays in the second term, as in `half_h`.[^dv]

*Idea:* on an exponentially growing count a fractional sum only rescales the dominant pole, and `√π` reaches the leading term when the branch point is moved onto that pole.

## Stop 3 - half a column in the width: real

The closed form `A^e(w, h) = (h^w − (h − 1)^w − P(h − 1, w) + P(h − 2, w))/2`, with `P(k, L)` the signed tower count, is a sum of exponentials in the width, `λ^w` over the roots of the characteristic polynomial `char_k` of `P(k, ·)` ([[fractional-width-and-height](pages/fractional-width-and-height.md)]).[^sol] For every `k ≤ 40`, `char_k` has no real root for odd `k` and exactly one, positive, for even `k`. The complex roots come in conjugate pairs with conjugate coefficients, and on the principal branch of the logarithm their powers stay conjugate at real `w`, so `A^e(w, h)` is a real function of real `w` for every `h ≤ 41`. Since no root lies on the negative real axis, the interpolant has exponential type below `π` in the imaginary direction, and by Carlson's theorem it is the only interpolant of type below `π`.

At height 2 the signed towers have the eigenvalues `1 ± i`, and

```
A^e(w, 2)  =  ( 2^{w+1} − 2^{(w+3)/2} cos(π(w + 1)/4) ) / 4,
```

which is `1, 3, 6, 10` at `w = 1, …, 4` and `4.382` at `w = 2.5`; the cosine is the conjugate pair `(1 ± i)^{w+1}`.

*Idea:* a sum of exponentials interpolates to a single real function when none of its eigenvalues lies on the negative real axis, the branch cut of the logarithm.

## Stop 4 - half a row in the height: complex

In the height the closed form has the eigenvalues `+1` and `−1` only: `P(k, L) = (−1)^k A_L(k) + B_L(k)` with polynomials `A_L` and `B_L` (fitted for `L ≤ 8` and checked for `k ≤ 33`), for example `A_4(k) = (k + 1)(2k + 1)(2k + 3)/6` and `B_4(k) = (k + 1)/2` ([[fractional-width-and-height](pages/fractional-width-and-height.md)]). The eigenvalue `−1` lies on the branch cut. On the principal branch `(−1)^k = e^{iπk}` is `i(−1)^m` at `k = m + 1/2`, so

```
A^e(4, 2.5)  =  16.75 + 6i,
```

whose imaginary part `(A_4(3/2) + A_4(1/2))/2 = (10 + 2)/2` comes from the part of the signed tower count that alternates with the height. The conjugate branch `e^{−iπk}` gives `16.75 − 6i`, and their average, `(−1)^k → cos(πk)`, gives the real `16.75`. The three interpolants differ by multiples of `sin(πk)` and all have type exactly `π`, so Carlson's theorem singles out none of them.

*Idea:* the eigenvalue `−1` that carries the parity lies on the branch cut, so at half-integer height the alternating part of the count turns imaginary, and no interpolant is preferred.

## Stop 5 - half a column

Is a strip rule `M` two steps of a rule `R`, `R² = M`? If `R` is 0/1, each step of `M` is exactly one two-step path of `R`, so the strips of width `w` under `M` are the strips of width `2w − 1` under `R` read at every other column, and `R` is a **half-column** rule; these `M` are the squares of 0/1 rules, 8, 88, 3245 at heights 2 to 4 ([[fractional-width-and-height](pages/fractional-width-and-height.md)]). A real square root with other entries is a weighted half-column.

The rules whose eigenvalues are all positive are the matrices `I + N` with `N` the adjacency matrix of an acyclic graph (McKay et al.), and their principal square root is the finite sum `Σ_k C(1/2, k) N^k`.[^dag] For a partial order, `(N^k)_{ac}` counts the chains `a < ⋯ < c` of `k` steps, so the entry `(a, c)` of the root is `1/2 − (two-step chains)/8 + (three-step chains)/16 − ⋯`: the direct edge `a < c`, which transitivity supplies, adds `+1/2` against `−1/8` for each middle `b`. The diamond `1 < 2 < 4`, `1 < 3 < 4` gets `1/2 − 2/8 = 1/4` on `1 < 4`, while the rule with the chain `2 → 1 → 3` and no `2 → 3` gets `−1/8` at `(2, 3)`. The nonnegative roots are exactly the partial orders, A001035, through height 6: 3, 19, 219, 4231, 130023 at heights 2 to 6. One edge pays for at most four middles, though: a bottom, five incomparable middles and a top give `1/2 − 5/8 = −1/8`, and at height 7, 882 of the 6129859 partial orders have a negative root, while every rule with a nonnegative root is still a partial order.[^posets] Outside the class `I + N` the free strip `J`, with eigenvalues `h, 0, 0, …`, has the nonnegative root `J/√h`.

The chain `1 < 2 < ⋯ < h` is the nondecreasing rule, and its root is the Toeplitz matrix of `(1 − x)^{−1/2}`, the series of Stop 0. For the nondecreasing castles, `C(w + h − 2, w − 1)` of them, the half-sum in the width is half a row in the height: `Σ_k C(2k, k)/4^k · C(w − k + h − 2, w − k − 1) = C(w + h − 3/2, w − 1)` ([[half-sum-castles](pages/half-sum-castles.md)]). A simple negative eigenvalue rules out any real root, so the Motzkin strip `I + A_path` of height `h ≥ 3` and every ridge rule `J − D` have none.

*Idea:* the root weighs each two-step chain `−1/8` against `+1/2` on the direct edge, so transitivity pays for up to four middles, enough for every partial order through height 6 and not for five incomparable middles at height 7.

## Stop 6 - half a derivative in time

The graph of a tree castle, one in which no two neighboring columns both have height at least 2, is a comb: the bottom row is the backbone and the cells above row 1 of each column are a tooth ([[tree-castle-diffusion](pages/tree-castle-diffusion.md)]). In the simple random walk on the castle graph, the horizontal moves are the simple random walk on the backbone reflected at the end columns, so `msd(t) = E hor(t)` until the walk can reach an end column, and a stationary step is horizontal with probability `rate(c) = (w − 1)/(n − 1) = (w − 1)/(w + b − 2)`, with `n` cells and `b` blocks. The reduction follows Pach and Tardos, who drop the steps that do not change a coordinate and obtain a standard random walk on the line for each projection.[^pt] The rate is not a spectral invariant: the 11-cell Laplacian-cospectral tree castles `(1, 1, 1, 2, 1, 1, 2, 1, 1)` and `(1, 1, 3, 1, 1, 1, 2, 1)` have rates `4/5` and `7/10`.

On a comb whose ribs go to infinity, Arkhincheev and Baskin show that the density on the axis obeys a diffusion equation whose time derivative has order 1/2, with mean-square displacement `D_1(πt/D_2)^{1/2}`, `D_1` and `D_2` the diffusion coefficients along the axis and along the ribs, and that ribs of finite average length `ℓ` (their `L`) restore conventional diffusion, `⟨x²(t)⟩ ∝ D_1 t/ℓ` for `t ≫ ℓ²/D_2`.[^ab] On the battlement, which alternates columns of heights 1 and `h`, `E hor(t)` is `(4√(2/π) + o(1))√t` while the teeth look infinite and `2t/(h + 1)` at long times, and the two asymptotes meet at `t = 8(h + 1)²/π`. At `h = 101` it is `25.9197, 94.2522, 324.4845` at `t = 10², 10³, 10⁴`, against `4√(2t/π) = 31.9154, 100.9253, 319.1538`. From `t ≈ 10⁴` on it lies above both asymptotes, 1.25 times their common value where they meet at `t = 26494`, and at `t = 10⁶` it is within 0.7% of `2t/(h + 1)` ([[tree-castle-diffusion](pages/tree-castle-diffusion.md)]). The order 1/2 is a window: the teeth have at most `h − 1` cells, and the shape of the castle sets where the window closes and the long-time rate.

The order can also be put on space instead of time. The fractional Laplacian `L^α` of [[levy-flights](pages/levy-flights.md)] generates a walk with long jumps; its heat trace depends only on the Laplacian spectrum, and its diagonal entries separate the same cospectral pair, by differences that tend to 0 as `α → 0`. Arkhincheev and Baskin draw the same line: dead ends lead to fractional time derivatives, a homogeneous medium to fractional spatial ones.[^ab-concl]

*Idea:* trapping in dead ends turns the time derivative into one of order 1/2, and teeth of at most `h − 1` cells make that a window that closes at a time of order `h²`.

## Summary table

| stop | integer operation | order 1/2 | what it shows |
|---|---|---|---|
| 1 | block count, the sum of positive column differences | `B_{1/2}` | separates the ten even-block castles of width 4 and height 2; a box gives `~ 2h√(w/π)` |
| 2 | partial sum in the width, `(1 − x)^{−1}` | `half_h`, weights `C(2k, k)/4^k` | `half_h/A^e → √(h/(h − 1))`; `√π` only in the remainder; `π = lim w 16^w/bhalf_4(w)²` |
| 3 | `λ^w` at integer width | real `w` | real for `h ≤ 41`; `A^e(2.5, 2) = 4.382` |
| 4 | `(−1)^k` at integer height | `h = m + 1/2` | `A^e(4, 2.5) = 16.75 + 6i` on the principal branch |
| 5 | one column, the rule `M` | `R` with `R² = M` | nonnegative principal roots of `I + N`: the partial orders through height 6, not at height 7 |
| 6 | one time step of the walk | a time derivative of order 1/2 | on the battlement `~ 4√(2t/π)` up to `t ≈ 8(h + 1)²/π`, then `2t/(h + 1)` |

## Snippet

```python
from fractions import Fraction as Fr
from itertools import product
from math import comb, cos, pi, sqrt
import cmath

def gl(alpha, n):                          # weights (-1)^k C(alpha, k) of (1 - x)^alpha, k < n
    w = [Fr(1)]
    for k in range(1, n):
        w.append(w[-1] * (k - 1 - alpha) / k)
    return w

def diff(alpha, c):                        # Grunwald-Letnikov difference of order alpha, stopped at the wall
    w = gl(alpha, len(c))
    return [sum(w[k] * c[i - k] for k in range(i + 1)) for i in range(len(c))]

def blocks(c):                             # each rise in the skyline starts new blocks
    return c[0] + sum(max(0, c[i] - c[i - 1]) for i in range(1, len(c)))

def B(c, alpha):                           # fractional block count: area at 0, blocks at 1
    return sum(max(Fr(0), d) for d in diff(alpha, c))

def P(k, L):                               # signed tower count, towers of height <= k on a base of length L
    dp = {0: 1}
    for _ in range(L):
        nd = {}
        for a, wt in dp.items():
            for b in range(k + 1):
                nd[b] = nd.get(b, 0) + wt * (-1) ** max(0, b - a)
        dp = nd
    return sum(dp.values())

def Ae(w, h):                              # the Project Euler 502 count of even-block castles
    return (h ** w - (h - 1) ** w - P(h - 1, w) + P(h - 2, w)) // 2 if w > 0 else 0

def half_sum(seq):                         # (1 - x)^(-1/2) applied to a sequence: weights C(2k, k)/4^k
    return [sum(Fr(comb(2 * k, k), 4 ** k) * seq[n - k] for k in range(n + 1)) for n in range(len(seq))]

def Ae4_height(h, branch=1):                # A^e(4, h) at real h, from P(k, 4) = (-1)^k A_4(k) + B_4(k)
    A4 = lambda k: (k + 1) * (2 * k + 1) * (2 * k + 3) / 6
    B4 = lambda k: (k + 1) / 2
    P4 = lambda k: cmath.exp(branch * 1j * pi * k) * A4(k) + B4(k)
    return (h ** 4 - (h - 1) ** 4 - P4(h - 1) + P4(h - 2)) / 2

def sqrt_I_plus_N(N):                      # principal square root of I + N for a nilpotent N: sum C(1/2, k) N^k
    n = len(N)
    mul = lambda X, Y: [[sum(X[i][t] * Y[t][j] for t in range(n)) for j in range(n)] for i in range(n)]
    R = [[Fr(int(i == j)) for j in range(n)] for i in range(n)]
    Nk, k, coef = N, 1, Fr(1)
    while any(any(row) for row in Nk):
        coef = coef * (Fr(1, 2) - k + 1) / k
        R = [[R[i][j] + coef * Nk[i][j] for j in range(n)] for i in range(n)]
        Nk, k = mul(Nk, N), k + 1
    return R

def battlement_hor(h, ts):                 # E hor(t) on the extended battlement (1, h, 1, h, ...), from a height-1 cell
    p = [1.0] + [0.0] * h                  # one period: a, b_0, b_1, ..., b_{h-1}
    out, E = [], 0.0
    for t in range(1, max(ts) + 1):
        E += p[0] + p[1] * 2 / 3           # a moves horizontally, b_0 with probability 2/3
        q = [0.0] * (h + 1)
        q[1] += p[0]
        q[0] += p[1] * 2 / 3
        if h >= 2:
            q[2] += p[1] / 3
        for j in range(2, h + 1):          # tooth cells: down, or up unless at the top
            if j < h:
                q[j - 1] += p[j] / 2
                q[j + 1] += p[j] / 2
            else:
                q[j - 1] += p[j]
        p = q
        if t in ts:
            out.append(round(E, 4))
    return out
```

```
>>> [str(x) for x in gl(Fr(1, 2), 7)]
['1', '-1/2', '-1/8', '-1/16', '-5/128', '-7/256', '-21/1024']
>>> [str(Fr(comb(2 * k, k), 4 ** k)) for k in range(7)]
['1', '1/2', '3/8', '5/16', '35/128', '63/256', '231/1024']
>>> c = (1, 3, 2, 2, 1, 4, 1)
>>> diff(Fr(-1, 2), diff(Fr(1, 2), c)) == list(c), diff(Fr(1, 2), diff(Fr(1, 2), c)) == diff(1, c)
(True, True)
>>> [(c, str(B(c, 0)), str(B(c, 1)), str(B(c, Fr(1, 2)))) for c in [(1, 1, 1, 2), (1, 1, 2, 1), (2, 1, 1, 1)]]
[((1, 1, 1, 2), '5', '2', '51/16'), ((1, 1, 2, 1), '5', '2', '23/8'), ((2, 1, 1, 1), '5', '2', '5/2')]
>>> ten = [c for c in product((1, 2), repeat=4) if max(c) == 2 and blocks(c) % 2 == 0]
>>> len(ten), len({B(c, Fr(1, 2)) for c in ten})
(10, 10)
>>> [B((3,) * w, Fr(1, 2)) == Fr(2 * 3 * w * comb(2 * w, w), 4 ** w) for w in range(1, 9)]
[True, True, True, True, True, True, True, True]
>>> row4 = [Ae(w, 4) for w in range(201)]
>>> half4 = half_sum(row4[:101])
>>> [str(x) for x in half4[1:6]], round(float(half4[100]) / row4[100], 10), round(sqrt(4 / 3), 10)
(['1', '15/2', '279/8', '2167/16', '65483/128'], 1.1547005384, 1.1547005384)
>>> bhalf4 = [sum(comb(2 * k, k) * row4[w - k] for k in range(w + 1)) for w in range(201)]
>>> bhalf4[1:8], round(200 * 16 ** 200 / bhalf4[200] ** 2, 5)
([1, 9, 51, 241, 1069, 4671, 20353], 3.17108)
>>> Ae2 = lambda w: (2 ** (w + 1) - 2 ** ((w + 3) / 2) * cos(pi * (w + 1) / 4)) / 4
>>> [round(Ae2(w), 3) for w in (1, 2, 2.5, 3, 4)], [Ae(w, 2) for w in (1, 2, 3, 4)]
([1.0, 3.0, 4.382, 6.0, 10.0], [1, 3, 6, 10])
>>> Ae4_height(2.5), Ae4_height(2.5, branch=-1), [round(Ae4_height(h).real) for h in (2, 3, 4)]
((16.75+6j), (16.75-6j), [10, 21, 117])
>>> diamond = [[0, 1, 1, 1], [0, 0, 0, 1], [0, 0, 0, 1], [0, 0, 0, 0]]        # 1 < 2 < 4, 1 < 3 < 4, and 1 < 4
>>> [[str(x) for x in row] for row in sqrt_I_plus_N(diamond)]
[['1', '1/2', '1/2', '1/4'], ['0', '1', '0', '1/2'], ['0', '0', '1', '1/2'], ['0', '0', '0', '1']]
>>> no_order = [[0, 0, 1], [1, 0, 0], [0, 0, 0]]                             # 1 -> 3 and 2 -> 1, no 2 -> 3
>>> [[str(x) for x in row] for row in sqrt_I_plus_N(no_order)]
[['1', '0', '1/2'], ['1/2', '1', '-1/8'], ['0', '0', '1']]
>>> five = [[int(i == 0 < j or 0 < i < 6 == j) for j in range(7)] for i in range(7)]   # 1 < 2..6 < 7, and 1 < 7
>>> str(sqrt_I_plus_N(five)[0][6])
'-1/8'
>>> battlement_hor(101, [100, 1000, 10000]), [round(4 * sqrt(2 * t / pi), 4) for t in (100, 1000, 10000)], round(8 * 102 ** 2 / pi)
([25.9197, 94.2522, 324.4845], [31.9154, 100.9253, 319.1538], 26494)
```

## Exercises

1. From the weights `1, −1/2, −1/8, −1/16`, compute the residuals and `B_{1/2}` of `(1, 1, 1, 2)` and `(1, 1, 2, 1)`, and check that the two castles have the same area and block count.
2. Show that the half-sum applied twice is the ordinary partial sum, and compute `half_4(2) = 15/2` from `A^e(1, 4) = 1` and `A^e(2, 4) = 7`.
3. From `A_4(k)` and `B_4(k)`, compute `A^e(4, 2.5)` on the principal branch, on the conjugate branch, and with `(−1)^k → cos(πk)`.
4. For the partial order with a bottom, `m` pairwise incomparable middles and a top, show that the root `Σ_k C(1/2, k) N^k` has `1/2 − m/8` from bottom to top, and find the smallest height at which it is negative.
5. On the battlement, show that a walker at the foot of a tooth makes `2j` horizontal moves before it enters a tooth with probability `(2/3)^j/3`, and that their mean is 4.
6. For a tree castle with semi-perimeter `s = w + b` ([[castle-perimeter](pages/castle-perimeter.md)]), show that `rate(c) = (w − 1)/(s − 2)`.

## Appearances in Sources

- [[project-euler-502-solution](pages/project-euler-502-solution.md)] - the closed form `A^e(w, h) = (h^w − (h − 1)^w − P(h − 1, w) + P(h − 2, w))/2` interpolated in Stops 3 and 4.
- [[project-euler-502-brute-force](pages/project-euler-502-brute-force.md)] - the block count as the total ascent, the endpoint `α = 1` of Stop 1.
- [[algebraic-languages-and-polyominoes-enumeration](pages/algebraic-languages-and-polyominoes-enumeration.md)] - the convex polyominoes by perimeter, with a double pole and a square-root branch point at one place, the pole winning as for `half_h` in Stop 2.
- [[arkhincheev-baskin-1991-comb-model](pages/arkhincheev-baskin-1991-comb-model.md)] - the comb equation with a time derivative of order 1/2 and its finite-rib limit, Stop 6.
- [[pach-tardos-2013-range-of-random-walk-on-comb](pages/pach-tardos-2013-range-of-random-walk-on-comb.md)] - the reduced projections of the walk on a comb, Stop 6.

## Related Concepts

- [[fractional-block-count](pages/fractional-block-count.md)], [[half-sum-castles](pages/half-sum-castles.md)], [[fractional-width-and-height](pages/fractional-width-and-height.md)], [[tree-castle-diffusion](pages/tree-castle-diffusion.md)] - the four operations of the seminar at fractional order.
- [[levy-flights](pages/levy-flights.md)] - the space-fractional Laplacian of the castle graph, against the time-fractional comb of Stop 6.
- [[power-law-memory-rules](pages/power-law-memory-rules.md)] - the weights of Stop 1 used in a strip rule instead of a statistic.
- [[fractional-recurrences](pages/fractional-recurrences.md)] - fractional difference operators applied to recurrences.
- [[castle-notation](pages/castle-notation.md)] - `A^e`, `P(k, L)`, `A_L`, `B_L`, `∇^α`, `B_α`, `𝒞(x)`, `half_h`, `row_h`, `bhalf_h`, `N`, `ℓ`, `hor(t)`, `msd(t)` and `rate(c)`.
- [[tower-recursion-master-class](pages/tower-recursion-master-class.md)], [[pell-castle-strip](pages/pell-castle-strip.md)], [[hardin-identity-seminar](pages/hardin-identity-seminar.md)], [[hear-the-shape-seminar](pages/hear-the-shape-seminar.md)], [[castle-cryptography](pages/castle-cryptography.md)], [[q-thread-seminar](pages/q-thread-seminar.md)], [[oeis-mining-seminar](pages/oeis-mining-seminar.md)], [[one-bit-seminar](pages/one-bit-seminar.md)], [[song-as-castle](pages/song-as-castle.md)], [[sandcastle-seminar](pages/sandcastle-seminar.md)], [[castle-fibers-char-2-walkthrough](pages/castle-fibers-char-2-walkthrough.md)] - the other seminar pages.

## Footnotes

[^bf]: [[project-euler-502-brute-force](pages/project-euler-502-brute-force.md)] §"Column-height encoding" L20-L24 - "A block is a maximal horizontal run of columns at a given level, so", "= c_1 + \sum_{i=2}^{w} \max(0, c_i - c_{i-1})".
[^dv]: [[algebraic-languages-and-polyominoes-enumeration](pages/algebraic-languages-and-polyominoes-enumeration.md)] p.169 Abstract - "we prove that the number of convex polyominoes with perimeter 2n+8 is (2n+11)4^n - 4(2n+1)C(2n,n)."
[^sol]: [[project-euler-502-solution](pages/project-euler-502-solution.md)] §"The main formula" L66 - "F(w, h) = \frac{h^w - (h-1)^w - P(h-1, w) + P(h-2, w)}{2}".
[^dag]: B. D. McKay, F. E. Oggier, G. F. Royle, N. J. A. Sloane, I. M. Wanless and H. S. Wilf, "Acyclic digraphs and eigenvalues of (0,1)-matrices", *J. Integer Sequences* 7 (2004), 04.3.3, https://arxiv.org/abs/math/0310423, Theorem 1, cited through [[fractional-width-and-height](pages/fractional-width-and-height.md)] (its footnote 8, read there 2026-10-16): "the number of acyclic directed graphs with n labeled vertices is equal to the number of n X n matrices of 0's and 1's whose eigenvalues are positive real numbers"; the proof there shows that such a matrix has all eigenvalues 1 and is `I + N` with `N` acyclic.
[^posets]: Verified by execution (Python 3.11 with NumPy and NetworkX, 2026-10-31): `bin/python/half_column_posets.py`, run log `bin/python/half_column_posets-run.log`. All strictly upper-triangular `N` for `h ≤ 7`, the root `Σ_k C(1/2, k) N^k` in exact integer arithmetic, the partial-order test, labeled counts as `Σ h!/e(N)` with `e(N)` the number of linear extensions, and the bottom-middles-top entries `1/2 − m/8`; https://oeis.org/A001035 (read 2026-10-31), data `1, 1, 3, 19, 219, 4231, 130023, 6129859, ...`, matches the labeled partial orders.
[^pt]: [[pach-tardos-2013-range-of-random-walk-on-comb](pages/pach-tardos-2013-range-of-random-walk-on-comb.md)] §3 p.3 L128-L133 - "First, we reduce these one-dimensional walks by getting rid of the steps when the value does not change. In this way, horizontal steps contribute only to the reduced projection (Xi′) and vertical steps contribute only to the reduced projection (Yi′). Note that with probability 1 both reduced walks are infinite and they are distributed as the standard random walk on the line."
[^ab]: [[arkhincheev-baskin-1991-comb-model](pages/arkhincheev-baskin-1991-comb-model.md)] §2.1 pp.162-163 L64-L148 [synthesis] - Equation (10), `⟨x²(t)⟩ = D_1 (πt/D_2)^{1/2}`, and Equation (14), `(∂^{1/2}/∂t^{1/2} − (D_1/(2D_2^{1/2})) ∂²/∂x²) n(x, 0, t) = 0`, read from the page image, for the comb of Figure 1, whose ribs go to infinity; "The transition to the conventional diffusion also occurs when the average length of the ribs L is finite. Then, for long times t ≫ L²/D2, we obtain ⟨x²(t)⟩ ∝ D1t/L."
[^ab-concl]: [[arkhincheev-baskin-1991-comb-model](pages/arkhincheev-baskin-1991-comb-model.md)] §4 p.164 L247-L254 - "For a homogeneous isotropic model with anomalous diffusion it is an equation with fractional spatial derivatives. In the present paper the example of a comb structure is used to show that the presence of "dead ends" leads to fractional time derivatives."
[^exec]: Verified by execution (Python 3.11, 2026-10-31): the Snippet, run as shown; every value it prints agrees with the page cited in the stop where it is quoted, whose own checks cover the rest (the 15 castles of Stop 1, the poles, remainders and Richardson table of Stop 2, the root counts of Stop 3, the polynomials `A_L`, `B_L` of Stop 4, the rule census of Stop 5, and the battlement computations of Stop 6).
