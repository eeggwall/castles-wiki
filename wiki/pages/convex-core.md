---
title: The convex core of a castle
category: Analyses
summary: Every castle has a unique minimal convex (unimodal) majorant, its convex core, given in one line by min(prefix max, suffix max). The castles sharing a core are exactly those that lower the non-anchor columns of its plateaus; the anchors are the first column of a rising plateau, the last column of a falling plateau, and both ends of the top plateau. The material lowered below a plateau at level m is an upside-down tower of height at most m-1, so the fiber over a core is a product of tower counts, prod T(m-1, free) = prod m^free unsigned and (-1)^h prod P(m-1, free) signed, with free = l-1 (l-2 on the top plateau). Summed over the C(2h+w-3, w-1) cores these give h^w - (h-1)^w and P(h-2,w) - P(h-1,w), so F(w,h) is a sum over convex cores of products of signed tower counts. The inside direction fails - the maximal convex minorant is not unique, (2,1,2) has two - and the source's D/U-pair insertion never closed because the freedom is per column, not per insertion. Verified for every cell 2 <= w <= 6, 2 <= h <= 5.
tags: [analysis, castle, convex, unimodal, tower, signed-tower-count, parity, verification, hull]
sources: [project-euler-502-representations, project-euler-502-solution, oeis-mining-pe502]
created: 2026-09-20
updated: 2026-09-20
---

# The convex core of a castle

## The claim in the source, and what is true

The Representations subpage of the Project Euler 502 (PE 502) solution organizes castles as rectangular, then convex, then "variations on convex castles": a convex castle's U/R/D word has runs of `R`s, and inserting `D`/`U` pairs into the slots of a run produces the non-convex castles.[^1] The Solution subpage records that enumerating these variations "never resolved into a formula".[^2] Two questions were left open on [[convex-castle](pages/convex-castle.md)]: is the convex castle behind a given castle unique, and if so what is the set of castles it generates?

Both close. Every castle has a unique smallest [[convex-castle](pages/convex-castle.md)] above it, its **convex core**, and the set of castles over a core is a product of the tower counts `T(k,L)` and `P(k,L)` of [[tower-recursion-master-class](pages/tower-recursion-master-class.md)] and [[signed-tower-count](pages/signed-tower-count.md)], one factor per plateau. The variation enumeration did not close because it counted insertions; the freedom is per column.[^4]

## The core in one line

Write the castle as its skyline `c = (c_1, ..., c_w)` with `1 <= c_i <= h` and `max c = h`. Let `L_i = max(c_1, ..., c_i)` be the running maximum from the left and `R_i = max(c_i, ..., c_w)` the running maximum from the right. The convex core is

```
core(c)_i = min(L_i, R_i)
```

`L` is nondecreasing and `R` is nonincreasing, so their pointwise minimum follows `L` up to the first column of height `h` and `R` after the last one: it is unimodal. It dominates `c` because both `L_i` and `R_i` do. And it is the smallest unimodal skyline dominating `c`: if `v >= c` is unimodal with peak at `p`, then for `i <= p` the value `v_i` is at least every `v_j` with `j <= i`, hence at least `L_i`, and for `i >= p` it is at least `R_i`; so `v_i >= min(L_i, R_i)` at every `i`. The core is the pointwise minimum of the set of unimodal majorants, so it is the unique minimal one. A castle is its own core iff it is unimodal, so the cores of the `(w,h)` cell are exactly the `C(2h+w-3, w-1)` convex castles of [[convex-castle-binomial-identity](pages/convex-castle-binomial-identity.md)].[^4]

Cutting the core out of a castle removes exactly the valleys. The columns where `c_i < core(c)_i` are the columns that are not a left record and not a right record, and on each maximal run of them the core is constant.

## The fiber over a core

Fix a convex core `u`. Which castles `c` have `core(c) = u`? Split `u` into its maximal plateaus, runs of equal height. Since `u` is unimodal every plateau is rising (a later plateau is higher), falling (an earlier plateau is higher), or the top plateau at level `h`. Then `core(c) = u` iff `c <= u` pointwise and `c` agrees with `u` on the **anchors**:

- the first column of every rising plateau (so `L` reaches the new level there),
- the last column of every falling plateau (so `R` does),
- both end columns of the top plateau (one column if the top plateau has length 1).

Every other column of a plateau at level `m` is **free**: it may take any height in `{1, ..., m}` without changing `L` or `R`, because a non-record column never enters a running maximum. So a plateau of length `l` at level `m` contributes `free = l - 1` free columns, or `l - 2` on the top plateau (`0` if the top has length 1), and the fiber over `u` has size

```
|fiber(u)| = prod over plateaus of m^free
```

Worked cell `(4,2)`: the 15 castles sit over 10 cores. The rectangle `(2,2,2,2)` has two free interior columns and carries 4 castles, `(2,2,2,2)`, `(2,1,2,2)`, `(2,2,1,2)`, `(2,1,1,2)`. The cores `(1,2,2,2)` and `(2,2,2,1)` carry 2 each. The other seven cores carry only themselves, so `4 + 2 + 2 + 7 = 15 = 2^4 - 1`.[^4] The largest fiber in every cell is the rectangle's, `h^(w-2)`.

## The fiber is a product of tower counts

The free columns of a plateau at level `m` are an upside-down tower. Set `y_i = m - c_i` on the `free` columns: `y_i` ranges over `{0, ..., m-1}`, exactly a tower of height at most `m - 1` above a block of length `free`, hanging from the plateau instead of standing on the base. So `m^free = (k+1)^L = T(m-1, free)`, the unsigned tower count with `k = m - 1`, `L = free`.

The block count follows the same reflection. A castle has `h + (extra)` blocks where `(extra)` is the total ascent of its skyline beyond the ascents of its core ([[convex-castle-binomial-identity](pages/convex-castle-binomial-identity.md)] gives `blocks = h` iff unimodal).[^3] On a plateau at level `m` the free columns sit between two columns of height at least `m`, so the extra ascent they add equals the total ascent of the closed walk `m, c_{i}, ..., c_{i+free-1}, m`, which equals its total descent, which is the block count of the reflected tower `y`. Hence the block-parity sign of a castle factors over the plateaus of its core, and

```
sum over c in fiber(u) of (-1)^blocks(c)  =  (-1)^h  prod over plateaus of P(m-1, free)
```

with `P(k, L)` the signed tower count. The `(4,2)` rectangle checks: its four castles have `2, 3, 3, 3` blocks, so the signed sum is `1 - 3 = -2 = (-1)^2 P(1, 2)`.[^4]

Summing over cores recovers both halves of the [[castle-counting-formula](pages/castle-counting-formula.md)]:

```
sum over convex u of  prod T(m-1, free)          =  h^w - (h-1)^w
(-1)^h  sum over convex u of  prod P(m-1, free)  =  P(h-2, w) - P(h-1, w)
F(w,h) = (1/2) sum over convex u of [ prod T(m-1, free) + (-1)^h prod P(m-1, free) ]
```

The first identity says the `h^w - (h-1)^w` skylines are partitioned by their cores. The second is the parity clause read plateau by plateau. Both hold in every cell `2 <= w <= 6`, `2 <= h <= 5`, and the plateau signed sum `P(m-1, free)` was also checked directly against the tower definition for `m <= 5`, `free <= 5`.[^4] So the even-block clause does refine the fiber, and the refinement is the existing `P(k,L)` family: the same signed transfer matrix that counts towers standing on the base counts the towers hanging in a plateau, and the core decomposition is the dual of the tower recursion, convex hull outside and inverted towers inside instead of a base block below and towers above.

## The inside direction fails

If "convex skeleton" is read as the largest convex castle *inside* a given castle, there is no unique answer. `(2,1,2)` has two maximal unimodal minorants, `(2,1,1)` and `(1,1,2)`, and neither dominates the other. Non-uniqueness is the common case: in the `(6,4)` cell 2,905 of the 3,367 castles have more than one maximal convex minorant, and in `(6,5)` 10,242 of 11,529.[^4] The hull direction is canonical because running maxima are; the skeleton direction is not.

## Why the insertion enumeration did not close

The source inserts one `D`/`U` pair at a time into a run of `R`s, with the rules "insert `D` first", "in pairs", "never adjacent".[^1] Each insertion lowers a stretch of a plateau by one. A valley of depth two, or two valleys side by side, or a bump inside a valley, is reached by several insertion sequences, and the rules above remove only some of the duplicates. The per-column description has none: a free column is chosen once, from `{1, ..., m}`, independently of every other free column. The case analysis that would not close is the product formula above, and its parity refinement is `P(k,L)`.

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
    return T, S                      # |fiber|, and sum of (-1)^blocks over it
```

Brute force over `{1..h}^w` with `max = h`, grouped by `core`, reproduces both outputs cell by cell.

## Appearances in Sources

- [[project-euler-502-representations](pages/project-euler-502-representations.md)] - the rectangular / convex / variations taxonomy and the `D`/`U`-pair insertion rules this page replaces with a per-column description.
- [[project-euler-502-solution](pages/project-euler-502-solution.md)] - records the variation enumeration as the route that never resolved into a formula.
- [[oeis-mining-pe502](pages/oeis-mining-pe502.md)] - `blocks >= h` with equality iff unimodal, the fact that makes the parity refinement a tower count.

## Related Concepts

- [[convex-castle](pages/convex-castle.md)] - the cores; every convex castle is its own core and the cores of a cell are exactly the convex castles.
- [[convex-castle-binomial-identity](pages/convex-castle-binomial-identity.md)] - the number of cores, `C(2h+w-3, w-1)`, and the minimum-block characterization.
- [[urd-step-strings](pages/urd-step-strings.md)] - the encoding whose variation taxonomy this page completes.
- [[tower-recursion-master-class](pages/tower-recursion-master-class.md)] - `T(k,L) = (k+1)^L`; the fiber's unsigned factors are these counts for the inverted towers.
- [[signed-tower-count](pages/signed-tower-count.md)] - `P(k,L)`; the fiber's signed factors, so `P` counts towers hanging from a plateau as well as towers standing on the base.
- [[castle-counting-formula](pages/castle-counting-formula.md)] - both terms of `F(w,h)` as sums over cores.
- [[castle-sign](pages/castle-sign.md)] - the sign `(-1)^blocks`, which factors over the plateaus of the core.
- [[castle-representations](pages/castle-representations.md)] - the cycle-forest form is the same vertical nesting read recursively; the core is its first level.
- [[castle-classification-shape](pages/castle-classification-shape.md)] - the unimodal type, here the fixed points of `core`.
- [[weakly-unimodal-composition](pages/weakly-unimodal-composition.md)] - the cores by area, A001523.
- [[tower-spacing-castles](pages/tower-spacing-castles.md)] - the other closing operator on skylines (window-`g` running minimum); the core is the running-maximum closing from both ends.

## Footnotes

[^1]: [[project-euler-502-representations](pages/project-euler-502-representations.md)] §"Steps-Based Approach" L109,L117 - "we can classify all remaining castles as variations on convex castles. To construct variations on castles, we look for runs of RRRs of length 3 or more. Each pair of Rs creates a slot for additional U or D moves ... we MUST insert Ds first; if we insert Us first, we will construct a duplicate castle variation that would be covered by another convex castle. We must also insert Ds and Us in pairs, so as to keep the total height change 0. Last, we cannot insert Ds and Us next to one another."

[^2]: [[project-euler-502-solution](pages/project-euler-502-solution.md)] §"What was tried and did not work" L190 - "U/R/D convex-castle enumeration. Conceptually clean, but the case analysis to enumerate variations of a convex castle never resolved into a formula."

[^3]: [[oeis-mining-pe502](pages/oeis-mining-pe502.md)] `binomial-vandermonde-identity.md` §1 L25-33 - "#blocks >= max(c) = h, with equality iff the profile is unimodal. Hence a convex castle of height h has exactly h blocks, and convex castles are exactly the minimum-block castles of height h."

[^4]: Verified by execution, 2026-09-20. For every cell `2 <= w <= 6`, `2 <= h <= 5` (largest cell `(6,5)`, 11,529 castles): `min(L, R)` is unimodal, dominates the castle, and is pointwise below every unimodal majorant found by brute force; the number of castles over each core equals `prod m^free`; the signed sum over each fiber equals `(-1)^h prod P(m-1, free)`; and the two sums over cores equal `h^w - (h-1)^w` and `P(h-2,w) - P(h-1,w)` (for example `(6,4)`: 3367 and 91, so `F = 1729`; `(5,3)`: 211 and -33, so `F = 89`). The plateau signed sum, `sum over x in {1..m}^n of (-1)^(total ascent of (m, x, m))`, equals `P(m-1, n)` by direct enumeration for `m <= 5`, `n <= 5`. Maximal unimodal minorants counted by brute force over all unimodal skylines below the castle: `(3,2)` has 1 castle of 7 with more than one (`(2,1,2)`), `(6,4)` has 2,905 of 3,367, `(6,5)` has 10,242 of 11,529.
