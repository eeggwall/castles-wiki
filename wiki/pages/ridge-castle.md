---
title: Ridge castle
category: Concepts
summary: A ridge castle is a castle of exact height h in which neighbouring columns differ in height unless both reach the ceiling h, so flat runs occur only at the ceiling. Its transfer matrix R_h = J − D has characteristic polynomial (x + 1)^{h−2}(x² − (h−1)x − 1), and the all-ones vector stays in the plane where R_h acts by the metallic recurrence, so the ridge castles of width w number x_{w+1} + x_w − (h−1)(h−2)^{w−1}, with x the metallic sequence x_n = (h−1)x_{n−1} + x_{n−2}. They grow like the metallic mean δ_{h−1} - golden at h = 2 (where swapping heights 1 and 2 gives the Fibonacci castles plus the flat row), silver at 3, bronze at 4, copper at 5 (where the strip count is the Fibonacci trisection F_{3w+2}), nickel at 6 - and are the only known realization of bronze and above, which need at least 4 height-states. The even-block counts keep the metallic growth because the signed transfer matrix is spectrally smaller, and have no OEIS match for h ≥ 3.
tags: [concept, castle, castle-type, ridge-castle, metallic-mean, transfer-matrix, growth-constant, golden, silver, bronze, copper, nickel, fibonacci, parity, blocks]
sources: [project-euler-502]
created: 2026-10-03
updated: 2026-10-07
---

# Ridge castle

## Definition

A castle is a skyline `(c_1, …, c_w)` on a full bottom row with maximum height exactly `h`, counted in PE 502 when its number of blocks is even.[^pe]

A **ridge castle** is a castle of exact height `h` in which neighbouring columns always differ in height, except that two neighbouring columns may both reach the ceiling:

```
c_i ≠ c_{i+1}   unless   c_i = c_{i+1} = h.
```

Flat runs occur only at the ceiling. Below it the skyline steps up or down at every column, and every height `1, …, h` may occur.

- **Construction rule.** Pick `c_1`, then give each next column any height other than the current one, or `h` again when the current one is `h`. Keep the skylines in which some column reaches `h`.
- **Example.** At `h = 4`, `w = 12`: `(3, 1, 3, 4, 4, 1, 4, 4, 1, 4, 2, 1)`, with 12 blocks.
- **Non-example.** `(3, 1, 1, 4)` breaks the rule: two neighbouring columns of height 1 below the ceiling.
- **Small case.** The five ridge castles of exact height 3 and width 2 are `(1, 3)`, `(2, 3)`, `(3, 1)`, `(3, 2)`, `(3, 3)`.
- **Not crenellated.** The crenellated type of [[castle-classification-shape](pages/castle-classification-shape.md)] (Axis 7) is the strict period-2 skyline `(a, h, a, h, …)`. Ridge castles may use every height and may repeat `h`.

The type sits in Axis 2 (rate of change) of [[castle-classification-shape](pages/castle-classification-shape.md)], as a plateau-free variant with a single ceiling exception.

## The transfer matrix

With states the heights `1, …, h`, the ridge rule has transfer matrix

```
R_h = J − D,     J the h × h all-ones matrix,   D = diag(1, …, 1, 0),
```

so entry `(a, b)` is 1 when `a ≠ b` or `a = b = h`. Its characteristic polynomial is

```
det(xI − R_h)  =  (x + 1)^{h−2} · (x² − (h − 1)x − 1).
```

**Why.** Write `R_h = J − I + e_h e_hᵀ`. On the `(h − 2)`-dimensional space of vectors `v` with `Σ_i v_i = 0` and `v_h = 0`, both `J` and `e_h e_hᵀ` vanish, so `R_h v = −v`. The plane spanned by the all-ones vector `𝟙` and `e_h` is invariant: `R_h 𝟙 = (h − 1)𝟙 + e_h` and `R_h e_h = 𝟙`. On that plane `R_h` acts by `[[h − 1, 1], [1, 0]]`, with characteristic polynomial `x² − (h − 1)x − 1`.[^exec]

The Perron root is the metallic mean `δ_{h−1} = ((h − 1) + √((h − 1)² + 4))/2` ([[metallic-means](pages/metallic-means.md)]); the other eigenvalues are `−1` (multiplicity `h − 2`) and `−1/δ_{h−1}`.

## Counting

**Skylines under the rule.** Because `𝟙` lies in the invariant plane, `𝟙ᵀ R_h^{w−1} 𝟙` satisfies the metallic recurrence exactly, with no contribution from the eigenvalue `−1`. With `x_n` the metallic sequence of order `a = h − 1` (`x_0 = 0`, `x_1 = 1`, `x_n = a x_{n−1} + x_{n−2}`: Fibonacci, Pell, …),

```
𝟙ᵀ R_h^{w−1} 𝟙  =  x_{w+1} + x_w        (h, h² − h + 1, … at w = 1, 2).
```

**Ridge castles.** Subtract the skylines that never reach `h`. On heights `1, …, h − 1` the rule says only that neighbours differ, which allows `(h − 1)(h − 2)^{w−1}` skylines (the plateau-free rule, `J − I`, not `R_{h−1}`). So

```
#{ridge castles of exact height h and width w}  =  x_{w+1} + x_w − (h − 1)(h − 2)^{w−1},
```

which for `h ≥ 3` satisfies the order-3 recurrence with characteristic polynomial `(x² − (h − 1)x − 1)(x − (h − 2))`. At `h = 2` the subtracted term is 1 at `w = 1` and 0 after, so the count is `F_{w+2}` from `w = 2` on.[^exec]

| `h` | metal | ridge castles of exact height `h`, `w = 1..10` |
|---|---|---|
| 2 | golden | `1, 3, 5, 8, 13, 21, 34, 55, 89, 144` |
| 3 | silver | `1, 5, 15, 39, 97, 237, 575, 1391, 3361, 8117` |
| 4 | bronze | `1, 7, 31, 118, 421, 1453, 4924, 16513, 55039, 182782` |
| 5 | copper | `1, 9, 53, 269, 1273, 5793, 25741, 112645, 487985, 2099577` |
| 6 | nickel | `1, 11, 81, 516, 3061, 17421, 96566, 525851, 2828221, 15076556` |

For `h ≥ 3` these sequences have no OEIS match ([[proper-castle-projection](pages/proper-castle-projection.md)]).

## Growth: the metallic ladder

The count grows like a constant times `δ_{h−1}^w`, since `δ_{h−1} > h − 1 > h − 2`. So the ridge castles of exact height `h` are a `δ_{h−1}` width growth castle ([[castle-classification-growth](pages/castle-classification-growth.md)]), and one rule covers the whole metallic ladder, metal `a = h − 1`:

| `h` | growth | metal | `x² − (h − 1)x − 1` |
|---|---|---|---|
| 2 | `φ ≈ 1.6180` | golden | `x² − x − 1` |
| 3 | `1 + √2 ≈ 2.4142` | silver | `x² − 2x − 1` |
| 4 | `(3 + √13)/2 ≈ 3.3028` | bronze | `x² − 3x − 1` |
| 5 | `2 + √5 = φ³ ≈ 4.2361` | copper | `x² − 4x − 1` |
| 6 | `(5 + √29)/2 ≈ 5.1926` | nickel | `x² − 5x − 1` |

- **Why the rule reaches the ladder.** A strip denominator `1 − p_1 x − p_2 x²` grows at a metallic mean exactly when `p_2 = 1`, and widening the height alphabet usually pushes `p_2` above 1. The ceiling exception keeps `p_2 = 1` while `p_1 = h − 1` grows ([[metallic-strip-realizability](pages/metallic-strip-realizability.md)]).
- **Bronze and above.** No 0/1 transfer matrix on 3 states has bronze as an eigenvalue; 192 of the 65,536 binary `4 × 4` matrices do.[^exec] So bronze needs at least four height-states, and for bronze, copper, nickel and higher the ridge castles are the only known realization. Silver and golden have others (the Pell castle strip, [[pell-castle-strip](pages/pell-castle-strip.md)]; the Fibonacci castles).
- **Minimum height.** Over all 0/1 strip rules, each metallic mean `δ_a` first appears at height `a + 1` ([[reachable-field-census](pages/reachable-field-census.md)], [[quadratic-min-height](pages/quadratic-min-height.md)]), the height at which the ridge rule reaches it.
- **Copper.** `δ_4 = 2 + √5 = φ³` lies in `Q(√5)`, and the strip count at `h = 5` is `x_{w+1} + x_w = F_{3w+2}` (`5, 21, 89, 377, …`), every third Fibonacci number ([[metallic-strip-realizability](pages/metallic-strip-realizability.md)]).
- **Entropy.** The rate is `log₂ δ_{h−1}` bits per column ([[castle-entropy](pages/castle-entropy.md)]).

## Height 2: the Fibonacci castles

At `h = 2` the rule forbids two neighbouring columns of height 1. Exchanging the heights 1 and 2 turns a ridge castle into a skyline with no two neighbouring height-2 columns: a [[fibonacci-castle](pages/fibonacci-castle.md)], or the all-1 row, which comes from the all-2 castle. So for `w ≥ 2` there are `F_{w+2}` ridge castles of exact height 2, one more than the `F_{w+2} − 1` Fibonacci castles. At `w = 1` both families are the single castle `(2)`. The exchange does not preserve blocks: `(2, 2)` has two blocks and `(1, 1)` one. Above height 2 the two families separate: the tree castles that extend the Fibonacci castles grow at the non-metallic `(1 + √(4h − 3))/2` ([[castle-graph](pages/castle-graph.md)]).

## Blocks and the even-block count

Blocks count the total rise from the ground, `c_1 + Σ max(0, c_i − c_{i−1})`, so the sign `(−1)^{blocks}` factors over the steps. The signed count is `vᵀ S_h^{w−1} 𝟙` with `v_a = (−1)^a` and the signed transfer matrix `S_h[a][b] = (−1)^{max(0, b − a)} R_h[a][b]`, minus the same signed count on the plateau-free skylines below the ceiling ([[proper-castle-projection](pages/proper-castle-projection.md)], [[castle-sign](pages/castle-sign.md)]). The spectral radius of `S_h` is below `δ_{h−1}` at every height checked, so the even-block count is half the total up to a smaller term and keeps the metallic growth:[^exec]

| `h` | `ρ(S_h)` | `δ_{h−1}` | even-block ridge castles, `w = 1..10` |
|---|---|---|---|
| 2 | 1.000 | 1.618 | `1, 3, 4, 4, 5, 9, 17, 29, 46, 72` |
| 3 | 1.575 | 2.414 | `0, 0, 3, 16, 44, 104, 265, 674, 1640, 3972` |
| 4 | 1.768 | 3.303 | `1, 7, 25, 70, 209, 697, 2390, 8169, 27565, 91762` |
| 5 | 2.242 | 4.236 | `0, 0, 10, 104, 604, 2836, 12630, 55668, 242744, 1047448` |
| 6 | 2.413 | 5.193 | `1, 11, 66, 320, 1601, 8661, 47807, 261401, 1411224, 7537448` |

At width 1 the only ridge castle is `(h)`, with `h` blocks, so the first entry is 1 for even `h` and 0 for odd `h`. The even-block sequences for `h ≥ 3` have no OEIS match ([[proper-castle-projection](pages/proper-castle-projection.md)]).

## Computation

The counts, the closed form and the characteristic polynomial, checked against brute force for small widths:

```python
import sympy as sp
from itertools import product
x = sp.symbols('x')
def ok(a, b, h): return a != b or a == b == h
def blocks(c): return c[0] + sum(max(0, c[i] - c[i-1]) for i in range(1, len(c)))
def ridge(h, w):                        # (all, even-block) ridge castles of exact height h, width w
    cs = [c for c in product(range(1, h + 1), repeat=w)
          if max(c) == h and all(ok(c[i], c[i+1], h) for i in range(w - 1))]
    return len(cs), sum(1 for c in cs if blocks(c) % 2 == 0)
for h in range(2, 6):
    a = h - 1; X = [0, 1]
    for _ in range(12): X.append(a * X[-1] + X[-2])
    assert all(ridge(h, w)[0] == X[w+1] + X[w] - (h-1) * (h-2)**(w-1) for w in range(1, 7))
    R = sp.Matrix(h, h, lambda i, j: 1 if (i != j or i == j == h - 1) else 0)
    assert sp.expand(R.charpoly(x).as_expr() - (x+1)**(h-2) * (x**2 - (h-1)*x - 1)) == 0
print([ridge(4, w) for w in range(1, 6)])   # [(1, 1), (7, 7), (31, 25), (118, 70), (421, 209)]
```

`ridge_R`, `ridge_count` and `proper_even` on [[castle-snippets-strips](pages/castle-snippets-strips.md)] compute the same quantities by transfer matrix.

## Related Concepts

- [[castle-classification-shape](pages/castle-classification-shape.md)] - the shape catalogue entry (Axis 2).
- [[metallic-strip-realizability](pages/metallic-strip-realizability.md)] - why the ridge rule reaches every metallic mean, and the state-count obstruction for bronze.
- [[proper-castle-projection](pages/proper-castle-projection.md)] - the exact-height and even-block projections in detail.
- [[metallic-means](pages/metallic-means.md)] - the ladder `δ_a`.
- [[castle-classification-growth](pages/castle-classification-growth.md)] - the width growth classes the ridge castles populate.
- [[fibonacci-castle](pages/fibonacci-castle.md)] - the height-2 case, after exchanging heights 1 and 2.
- [[1-smooth-pell-castles-by-area](pages/1-smooth-pell-castles-by-area.md)] - its height-2 comparison separates smooth, Fibonacci and ridge neighbour rules, and explains why exchanging heights does not preserve area.
- [[reachable-field-census](pages/reachable-field-census.md)], [[quadratic-min-height](pages/quadratic-min-height.md)] - the minimum height of each metallic mean over all strip rules.
- [[castle-strip](pages/castle-strip.md)] - the transfer-matrix object behind width growth constants.
- [[castle-notation](pages/castle-notation.md)] - the ridge castle entry and `R_h`.

## Footnotes

[^pe]: https://projecteuler.net/problem=502 (Project Euler, Problem 502 "Counting Castles", fetched 2026-10-03) - rules "The bottom row is occupied by a block of length w.", "The maximum achieved height of the entire castle is exactly h.", "The castle is made from an even number of blocks."
[^exec]: Verified by execution (Python 3, SymPy, NumPy, 2026-10-03): for `h = 2..6`, a transfer recurrence tracking height, whether the ceiling was reached, and block parity gives the tables above for `w ≤ 12`, and agrees with brute force over all skylines for `w ≤ 7` (`h ≤ 4`) and `w ≤ 5` (`h = 5, 6`); the closed form `x_{w+1} + x_w − (h−1)(h−2)^{w−1}` matches every entry for `w ≤ 12`; `det(xI − R_h)` equals `(x+1)^{h−2}(x² − (h−1)x − 1)` symbolically for `h = 2..6`; `ρ(S_h)` is computed numerically; the bronze search runs over all `2^9` binary `3 × 3` and all `2^{16}` binary `4 × 4` matrices (0 and 192 with an eigenvalue within `10^{−9}` of `(3 + √13)/2`); the example castle satisfies the rule and has 12 blocks.
