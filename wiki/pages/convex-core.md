---
title: The convex core of a castle
category: Analyses
summary: Every castle has a unique smallest convex (unimodal) skyline above it, its convex core, given by core(c)_i = min(max(c_1..c_i), max(c_i..c_w)). The castles over a core u are the castles that agree with u on its anchors (the first column of each rising plateau, the last column of each falling plateau, both ends of the top plateau) and lie below u elsewhere. The free columns of a plateau at level m are towers of height at most m − 1 hanging from it, so the castles over u number prod T(m − 1, free) = prod m^free and their signed sum is (−1)^h prod P(m − 1, free). Summed over the C(2h + w − 3, w − 1) cores these give A(w, h) = h^w − (h−1)^w and S(w, h) = P(h−2, w) − P(h−1, w), so A^e(w, h) is a sum over convex cores of products of tower counts. Below a castle there need not be a unique largest unimodal skyline: (2, 1, 2) has two maximal ones.
tags: [analysis, castle, convex, unimodal, tower, signed-tower-count, parity, verification, hull]
sources: [project-euler-502-representations, project-euler-502-solution]
created: 2026-09-20
updated: 2026-10-25
---

# The convex core of a castle

The Representations subpage of the Project Euler 502 solution sorts castles into rectangular castles, convex castles, and "variations on convex castles", obtained by inserting `D` and `U` steps into the runs of `R` in a convex castle's step word under rules meant to avoid duplicates.[^1] The Solution subpage records that the enumeration of these variations "never resolved into a formula".[^2] This page gives the per-column description of the castles over a convex castle: every castle lies under a unique smallest convex castle, its convex core, and the castles over a given core form a product of tower sets, one factor per plateau of the core, counted by the tower counts `T(k, L)` and `P(k, L)` ([[castle-counting-formula](pages/castle-counting-formula.md)], [[signed-tower-count](pages/signed-tower-count.md)]).

## The core

Write a castle of width `w` and height `h` as its skyline `c = (c_1, …, c_w)` ([[castle-polyomino](pages/castle-polyomino.md)]). Let `L_i = max(c_1, …, c_i)` be the running maximum from the left and `R_i = max(c_i, …, c_w)` the running maximum from the right.

**Proposition 1.** The skyline

```
core(c)_i  =  min(L_i, R_i)                                                     (1)
```

is unimodal, lies above `c`, and lies below every unimodal skyline that lies above `c`. So it is the unique smallest unimodal skyline above `c`, the **convex core** of `c`.

*Proof.* `L` is nondecreasing and `R` is nonincreasing, so `min(L, R)` follows `L` up to the first column of height `h` and `R` after the last one, and is unimodal. Both `L_i ≥ c_i` and `R_i ≥ c_i`. If `v ≥ c` is unimodal with its maximum at column `p`, then for `i ≤ p` the value `v_i` is at least every `v_j` with `j ≤ i`, hence at least `L_i`, and for `i ≥ p` it is at least `R_i`; so `v_i ≥ min(L_i, R_i)` at every `i`.

A castle is its own core exactly when it is unimodal, so the cores of the castles of width `w` and height `h` are the convex castles, `C(2h + w − 3, w − 1)` of them ([[convex-castle](pages/convex-castle.md)], [[convex-castle-binomial-identity](pages/convex-castle-binomial-identity.md)]). The columns with `c_i < core(c)_i` are the columns that are neither a weak left-to-right maximum (`c_i = L_i`) nor a weak right-to-left maximum (`c_i = R_i`), and on each maximal run of such columns both `L` and `R`, and so the core, are constant.

*Example.* The castle `(2, 1, 3, 1, 1, 2)` has `L = (2, 2, 3, 3, 3, 3)`, `R = (3, 3, 3, 2, 2, 2)` and core `(2, 2, 3, 2, 2, 2)`:

```
castle                    core
.  .  #  .  .  .          .  .  #  .  .  .
#  .  #  .  .  #          #  #  #  #  #  #
#  #  #  #  #  #          #  #  #  #  #  #
```

## The castles over a core

Fix a convex castle `u` of height `h` and split it into its **plateaus**, the maximal runs of equal height. Since `u` is unimodal, every plateau is rising (the next plateau is higher), falling (the previous plateau is higher), or the top plateau, at height `h`. The **anchors** of `u` are

- the first column of every rising plateau,
- the last column of every falling plateau,
- both end columns of the top plateau (one column if it has length 1).

**Proposition 2.** `core(c) = u` exactly when `c ≤ u` pointwise and `c` agrees with `u` on the anchors. So a plateau of length `l` at height `m` has `free = l − 1` free columns, or `free = max(l − 2, 0)` on the top plateau, each taking any height in `{1, …, m}`, and the castles over `u` number

```
|{c : core(c) = u}|  =  Π_{plateaus}  m^{free}                                  (2)
```

*Proof.* Suppose `core(c) = u`. Then `c ≤ u` by Proposition 1. At the first column `i` of a rising plateau at height `m`, `u_i = m` exceeds `u_{i−1}`, and `R_i ≥ h > m`, so `L_i = m > L_{i−1}` and `c_i = m`; symmetrically `c` equals `u` at the last column of each falling plateau and at both ends of the top plateau. Conversely, if `c ≤ u` and `c` agrees with `u` on the anchors, then `c` has the same running maxima `L` and `R` as `u`, since `u` takes each value of `L` and `R` first at an anchor and `c` is at most `u` everywhere else; so `core(c) = core(u) = u`.

In the example, the core `(2, 2, 3, 2, 2, 2)` has a rising plateau `(2, 2)` with one free column, the top plateau `(3)` with none, and a falling plateau `(2, 2, 2)` with two, so `2^1 · 2^2 = 8` castles lie over it: the skylines `(2, x, 3, y, z, 2)` with `x, y, z ∈ {1, 2}`.

In the cell of width 4 and height 2, the 15 castles lie over 10 cores. The rectangle `(2, 2, 2, 2)` carries 4 castles, `(2, 2, 2, 2)`, `(2, 1, 2, 2)`, `(2, 2, 1, 2)` and `(2, 1, 1, 2)`; the cores `(1, 2, 2, 2)` and `(2, 2, 2, 1)` carry 2 each; the other seven carry only themselves, and `4 + 2 + 2 + 7 = 15 = 2^4 − 1`.

**The rectangle has the largest fiber.** For `w ≥ 3` the rectangle `(h, …, h)` is the only core with `h^{w−2}` castles over it, and every other core has fewer. At `w = 2` every core carries one castle. A core other than the rectangle has a plateau below `h`, which carries an anchor. If the top plateau has length at least 2, the core has at least three anchors and at most `w − 3` free columns; if the top plateau has length 1, every free column lies below height `h`. Either way Equation (2) is at most `h^{w−3}` or `(h − 1)^{w−2}`, less than `h^{w−2}`.

## The fiber is a product of tower counts

The free columns of a plateau at height `m` are towers hanging from it: setting `y_i = m − c_i` on the `free` columns gives column heights in `{0, …, m − 1}`, towers of height at most `m − 1` on a base of length `free`. So `m^{free} = T(m − 1, free)`, and Equation (2) is a product of tower counts.

**Proposition 3.** For a castle `c` over the core `u`,

```
blocks(c)  =  h  +  Σ_{plateaus}  blocks(y),                                    (3)
```

with `y` the hanging towers of each plateau, so

```
Σ_{c : core(c) = u}  (−1)^{blocks(c)}  =  (−1)^h  Π_{plateaus}  P(m − 1, free).   (4)
```

*Proof.* The block count is the total ascent of the skyline from height 0 ([[castle-sign](pages/castle-sign.md)]), and a unimodal skyline of height `h` has total ascent `h`. The free columns `x_1, …, x_n` of a plateau at height `m` lie between columns of height at least `m`, so they add the total ascent of the closed walk `(m, x_1, …, x_n, m)` to the total ascent of the core. A closed walk has equal total ascent and total descent, and the total descent of `(m, x_1, …, x_n, m)` is the total ascent of `y = (m − x_1, …, m − x_n)` from 0, which is `blocks(y)`. The plateaus contribute independently, which gives Equation (4).

Equation (3) at a convex castle gives `blocks = h`, the minimum-block characterization of convex castles ([[convex-castle](pages/convex-castle.md)], section *Block count*).[^3] In the width-4, height-2 example, the four castles over the rectangle have `2, 3, 3, 3` blocks, and the signed sum `1 − 3 = −2` is `(−1)^2 P(1, 2)`.

Summing Equations (2) and (4) over the cores:

```
Σ_{convex u}  Π T(m − 1, free)            =  h^w − (h−1)^w  =  A(w, h)
(−1)^h  Σ_{convex u}  Π P(m − 1, free)    =  P(h−2, w) − P(h−1, w)  =  S(w, h)
A^e(w, h)  =  (1/2) Σ_{convex u} [ Π T(m − 1, free) + (−1)^h Π P(m − 1, free) ]   (5)
```

The first line says that the castles of width `w` and height `h` are partitioned by their cores, and the second is the signed count of the [[castle-counting-formula](pages/castle-counting-formula.md)] read plateau by plateau. At width 6 and height 4 the two sums are 3367 and 91, so `A^e(6, 4) = 1729`; at width 5 and height 3 they are 211 and −33, so `A^e(5, 3) = 89`. All of Equations (2) to (5) agree with enumeration for `2 ≤ w ≤ 6`, `2 ≤ h ≤ 5`.[^4]

## No unique largest unimodal skyline below

Below a castle there is no unique largest unimodal skyline. `(2, 1, 2)` has two maximal unimodal skylines below it, `(2, 1, 1)` and `(1, 1, 2)`, and neither lies below the other. It is the only castle of width 3 and height 2 with more than one; at width 6 and height 4, 2,905 of the 3,367 castles have more than one, and at width 6 and height 5, 10,242 of the 11,529.[^4]

## The source's insertion rules

The source inserts one `D`/`U` pair at a time into a run of `R` steps, with the rules that `D` comes first, that the steps come in pairs, and that a `D` and a `U` are never adjacent.[^1] Each insertion lowers a stretch of a plateau of the convex castle by one row. Proposition 2 replaces these insertions by a choice, for each free column independently, of a height in `{1, …, m}`, which counts every castle over the core exactly once.

## Reproduce

```python
def core(c):
    L = [max(c[:i+1]) for i in range(len(c))]
    R = [max(c[i:]) for i in range(len(c))]
    return tuple(min(a, b) for a, b in zip(L, R))

def fiber(u, P):                     # P(k, L): signed tower count, P(k, 0) = 1
    h, i, T, S = max(u), 0, 1, (-1) ** max(u)
    while i < len(u):
        j = i
        while j + 1 < len(u) and u[j+1] == u[i]: j += 1
        m, l = u[i], j - i + 1
        free = max(l - 2, 0) if m == h else l - 1
        T *= m ** free; S *= P(m - 1, free); i = j + 1
    return T, S                      # Equation (2), and Equation (4)
```

Enumerating `{1, …, h}^w` with maximum `h` and grouping by `core` reproduces both outputs for every core.[^4]

## Appearances in Sources

- [[project-euler-502-representations](pages/project-euler-502-representations.md)] - the rectangular, convex and variation classes and the `D`/`U` insertion rules.
- [[project-euler-502-solution](pages/project-euler-502-solution.md)] - the enumeration of variations as an approach that did not give a formula.

## Related Concepts

- [[convex-castle](pages/convex-castle.md)] - the convex castles, which are the cores, and a summary of this page's fiber count.
- [[convex-castle-binomial-identity](pages/convex-castle-binomial-identity.md)] - the number of cores, `C(2h + w − 3, w − 1)`.
- [[castle-counting-formula](pages/castle-counting-formula.md)] - the tower count `T(k, L) = (k+1)^L` and the formula for `A^e(w, h)` that Equation (5) refines.
- [[signed-tower-count](pages/signed-tower-count.md)] - `P(k, L)`, the factors of Equation (4).
- [[castle-sign](pages/castle-sign.md)] - the block count as total ascent and total descent.
- [[urd-step-strings](pages/urd-step-strings.md)] - the step words in which the source states its insertion rules.
- [[castle-classification-shape](pages/castle-classification-shape.md)] - the unimodal type, the castles with `core(c) = c`.
- [[weakly-unimodal-composition](pages/weakly-unimodal-composition.md)] - the convex castles by area, A001523.
- [[tower-spacing-castles](pages/tower-spacing-castles.md)] - skylines described by a running minimum over a window of `g` columns, another construction from running extrema.

## Footnotes

[^1]: [[project-euler-502-representations](pages/project-euler-502-representations.md)] §"Steps-Based Approach" L109, L117 - "we can classify all remaining castles as variations on convex castles. To construct variations on castles, we look for runs of RRRs of length 3 or more. Each pair of Rs creates a slot for additional U or D moves", "we MUST insert Ds first; if we insert Us first, we will construct a duplicate castle variation that would be covered by another convex castle. We must also insert Ds and Us in pairs, so as to keep the total height change 0. Last, we cannot insert Ds and Us next to one another."
[^2]: [[project-euler-502-solution](pages/project-euler-502-solution.md)] §"What was tried and did not work" L190 - "U/R/D convex-castle enumeration. Conceptually clean, but the case analysis to enumerate variations of a convex castle never resolved into a formula."
[^3]: [[project-euler-502-representations](pages/project-euler-502-representations.md)] §"Steps-Based Approach" L88-90, §"Step 1 Bare Minimum String" L153 [synthesis] - the word of a convex castle has a front with "No D steps" and a back with "No U steps", so one `U` per row, and "The bare minimum string consists of the minimum number of Us and Ds that the castle is required to have". Verified by execution (Python 3.11, 2026-10-25): every skyline of height `h` has at least `h` blocks, with equality exactly when it is unimodal, for `w ≤ 8`, `h ≤ 6` with `h^w ≤ 400000`.
[^4]: Verified by execution (Python 3.11, 2026-10-16): for every `2 ≤ w ≤ 6` and `2 ≤ h ≤ 5`, `core(c)` is unimodal for every castle, the cores are exactly the `C(2h + w − 3, w − 1)` convex castles, and Equations (2) and (4) hold for every core, with `P` summed over all towers; the two sums over cores at `(6, 4)` (3367, 91) and `(5, 3)` (211, −33); the rectangle as the unique largest fiber for `3 ≤ w ≤ 6`, `2 ≤ h ≤ 5` with `h^w ≤ 20000`, and all fibers equal to 1 at `w = 2`; the castles over `(2, 2, 3, 2, 2, 2)` (8); maximal unimodal minorants by brute force over all unimodal skylines below each castle, `(3, 2)`: 1 of 7, `(6, 4)`: 2,905 of 3,367, `(6, 5)`: 10,242 of 11,529.
