---
title: Ridge castle
category: Concepts
summary: The ridge castles of height h are the castles of height h whose neighboring columns differ in height unless both have height h. Their transfer matrix R_h = J − D has characteristic polynomial (x + 1)^{h−2}(x² − (h−1)x − 1), so the ridge strips number x_{w+1} + x_w, with x_n the metallic sequence of order a = h − 1, and the ridge castles number A_ridge(w, h) = x_{w+1} + x_w − (h−1)(h−2)^{w−1}; at height 5 this is F_{3w+2} − 4·3^{w−1}. They grow at the metallic mean δ_{h−1}, golden, silver and bronze by width at h = 2, 3, 4. At height 2, exchanging the heights 1 and 2 maps the ridge castles onto the Fibonacci castles and the flat row. The signed transfer matrix R̃_h has spectral radius below δ_{h−1}, so the even-block ridge castles grow at δ_{h−1} as well.
tags: [concept, castle, castle-type, ridge-castle, metallic-mean, transfer-matrix, growth-constant, golden, silver, bronze, fibonacci, parity, blocks]
sources: [project-euler-502]
created: 2026-10-03
updated: 2026-10-16
---

# Ridge castle

## Definition

A castle of width `w` and height `h` is a skyline `(c_1, …, c_w)` with `1 ≤ c_i ≤ h` and some `c_i = h` ([[castle-polyomino](pages/castle-polyomino.md)]).[^pe]

The **ridge rule** at height `h` allows a column of height `a` to be followed by one of height `b` when

```
a ≠ b,   or   a = b = h.
```

A **ridge strip** of height `h` is a skyline in `{1, …, h}^w` that obeys the ridge rule. It need not reach `h`, so a ridge strip is not a castle of height `h`. A **ridge castle** of height `h` is a ridge strip with some column of height `h`; `A_ridge(w, h)` is their number at width `w`. Below the ceiling the skyline steps up or down at every column, and flat runs occur only at height `h`.

- **Construction rule.** Choose `c_1`, then give each next column any height other than the current one, or `h` again when the current one is `h`. Keep the skylines in which some column has height `h`.
- **Example.** At `h = 4`, `w = 12`, the skyline `(3, 1, 3, 4, 4, 1, 4, 4, 1, 4, 2, 1)` is a ridge castle with 12 blocks.
- **Non-example.** The skyline `(3, 1, 1, 4)` is not one: its second and third columns both have height 1, below the ceiling.
- **Small case.** The five ridge castles of height 3 and width 2 are `(1, 3)`, `(2, 3)`, `(3, 1)`, `(3, 2)` and `(3, 3)`.
- **Not crenellated.** The crenellated castles of [[castle-classification-shape](pages/castle-classification-shape.md)] alternate between two heights, `(a, h, a, h, …)`. Ridge castles may use every height and may repeat `h`.

On [[castle-classification-shape](pages/castle-classification-shape.md)] the ridge castles are listed among the rate-of-change types, as the plateau-free castles with one exception at the ceiling.

## The transfer matrix

With states the heights `1, …, h`, the ridge rule has transfer matrix

```
R_h  =  J − D,          J the h × h all-ones matrix,   D = diag(1, …, 1, 0),
```

so entry `(a, b)` is 1 when `a ≠ b` or `a = b = h`. Its characteristic polynomial is

```
det(xI − R_h)  =  (x + 1)^{h−2} · (x² − (h − 1)x − 1).                                 (1)
```

*Proof.* Write `R_h = J − I + e_h e_hᵀ`, with `e_h` the `h`-th unit vector and `𝟙` the all-ones vector. On the `(h − 2)`-dimensional space of vectors `v` with `Σ_i v_i = 0` and `v_h = 0`, both `J` and `e_h e_hᵀ` vanish, so `R_h v = −v`. The plane spanned by `𝟙` and `e_h` is invariant: `R_h 𝟙 = (h − 1)𝟙 + e_h` and `R_h e_h = 𝟙`. On that plane `R_h` acts by the matrix `[[h − 1, 1], [1, 0]]`, with characteristic polynomial `x² − (h − 1)x − 1`.[^exec]

The Perron root is the metallic mean `δ_{h−1} = ((h − 1) + √((h − 1)² + 4))/2` of order `a = h − 1`, de Spinadel's `σ_{h−1}^1` ([[metallic-means](pages/metallic-means.md)]). The other eigenvalues are `−1`, with multiplicity `h − 2`, and `−1/δ_{h−1}`.

## Counting

Let `x_n` be the metallic sequence of order `a = h − 1`: `x_0 = 0`, `x_1 = 1`, `x_n = a·x_{n−1} + x_{n−2}` (the Fibonacci numbers at `a = 1`, the Pell numbers at `a = 2`).

**Ridge strips.** By the proof of Equation (1), `R_h^n 𝟙 = x_{n+1} 𝟙 + x_n e_h`, by induction on `n`. So the ridge strips of width `w` number

```
𝟙ᵀ R_h^{w−1} 𝟙  =  h·x_w + x_{w−1}  =  x_{w+1} + x_w,                                    (2)
```

with no contribution from the eigenvalue `−1`. These are `F_{w+2}` at `h = 2`, `A001333(w + 1)` at `h = 3`, `A003688(w + 1)` at `h = 4` and `A015448(w + 1)` at `h = 5`.[^oeis]

**Ridge castles.** Subtract the strips that do not reach `h`. On the heights `1, …, h − 1` the ridge rule says only that neighbors differ, which allows `(h − 1)(h − 2)^{w−1}` skylines. So

```
A_ridge(w, h)  =  x_{w+1} + x_w − (h − 1)(h − 2)^{w−1},                                  (3)
```

which for `h ≥ 3` satisfies the order-3 recurrence with characteristic polynomial `(x² − (h − 1)x − 1)(x − (h − 2))`. At `h = 2` the subtracted term is 1 at `w = 1` and 0 after, so `A_ridge(w, 2) = F_{w+2}` for `w ≥ 2`.[^exec]

**Height 5.** At `a = 4`, `x_n = F_{3n}/2`, the sequence `A001076`.[^oeis] Since `F_{3w+3} + F_{3w} = (F_{3w+2} + F_{3w+1}) + F_{3w} = 2F_{3w+2}`, Equation (2) gives `F_{3w+2}` ridge strips of height 5, and Equation (3) gives

```
A_ridge(w, 5)  =  F_{3w+2} − 4·3^{w−1}.
```

| `h` | ridge castles of height `h`, `A_ridge(w, h)` for `w = 1, …, 10` |
|---|---|
| 2 | `1, 3, 5, 8, 13, 21, 34, 55, 89, 144` |
| 3 | `1, 5, 15, 39, 97, 237, 575, 1391, 3361, 8117` |
| 4 | `1, 7, 31, 118, 421, 1453, 4924, 16513, 55039, 182782` |
| 5 | `1, 9, 53, 269, 1273, 5793, 25741, 112645, 487985, 2099577` |
| 6 | `1, 11, 81, 516, 3061, 17421, 96566, 525851, 2828221, 15076556` |

[[castle-sequence-catalogue](pages/castle-sequence-catalogue.md)] records the OEIS status of these rows.

## Growth

Since `δ_{h−1} > h − 1 > h − 2`, `A_ridge(w, h)` grows like a constant times `δ_{h−1}^w`: the ridge castles of height `h` are `δ_{h−1}` by width ([[castle-classification-growth](pages/castle-classification-growth.md)]). One rule gives every metallic mean `δ_a`, at height `h = a + 1`:

| `h` | growth `δ_{h−1}` | metallic mean | `x² − (h − 1)x − 1` |
|---|---|---|---|
| 2 | `φ ≈ 1.6180` | golden | `x² − x − 1` |
| 3 | `1 + √2 ≈ 2.4142` | silver | `x² − 2x − 1` |
| 4 | `(3 + √13)/2 ≈ 3.3028` | bronze | `x² − 3x − 1` |
| 5 | `2 + √5 = φ³ ≈ 4.2361` | `δ_4` | `x² − 4x − 1` |
| 6 | `(5 + √29)/2 ≈ 5.1926` | `δ_5` | `x² − 5x − 1` |

- **Minimum height.** A 0/1 matrix with `h` rows has spectral radius at most its largest row sum, at most `h`. Since `δ_a > a`, no strip rule on fewer than `a + 1` heights grows at `δ_a`, and the ridge rule reaches `δ_a` at height `a + 1` ([[quadratic-min-height](pages/quadratic-min-height.md)], [[reachable-field-census](pages/reachable-field-census.md)]). In particular bronze, `δ_3 ≈ 3.30`, needs four heights. Of the 65,536 0/1 matrices of size 4, 192 have bronze as an eigenvalue, `R_4` among them.[^exec]
- **Height 3.** The 1-smooth rule on three heights also grows at silver, through its quadratic factor `1 − 2x − x²` ([[metallic-strip-realizability](pages/metallic-strip-realizability.md)], [[pell-castle-strip](pages/pell-castle-strip.md)]).
- **Height 5.** `δ_4 = 2 + √5 = φ³`, since `φ³ = φ² + φ = 2φ + 1`, so the ridge strips of height 5 are every third Fibonacci number.
- **Entropy.** The ridge castles of height `h` carry `log₂ δ_{h−1}` bits per column ([[castle-entropy](pages/castle-entropy.md)]).

## Height 2: the Fibonacci castles

At `h = 2` the ridge rule forbids two neighboring columns of height 1. Exchanging the heights 1 and 2 turns a ridge castle of height 2 and width `w ≥ 2` into a skyline with no two neighboring columns of height 2: a [[fibonacci-castle](pages/fibonacci-castle.md)], or the flat row `(1, …, 1)`, which comes from the castle `(2, …, 2)`. So for `w ≥ 2` there are `F_{w+2}` ridge castles of height 2, one more than the `F_{w+2} − 1` Fibonacci castles. At `w = 1` each family has one member, the castle `(2)`. The exchange does not preserve blocks: `(2, 2)` has two blocks and `(1, 1)` one. Above height 2 the two families separate: the tree castles of height `h`, which extend the Fibonacci castles, grow at `σ_1^{h−1} = (1 + √(4h − 3))/2` ([[castle-graph](pages/castle-graph.md)]).

## Blocks and the even-block count

The block count is the total rise `c_1 + Σ_{i≥2} max(0, c_i − c_{i−1})` ([[castle-sign](pages/castle-sign.md)]), so the sign `(−1)^{blocks}` factors over the steps. Let `R̃_h` be the signed transfer matrix, `R̃_h[a][b] = (−1)^{max(0, b − a)} R_h[a][b]`, and `v_a = (−1)^a`. The signed count of the ridge castles of height `h` is

```
S_ridge(w, h)  =  vᵀ R̃_h^{w−1} 𝟙  −  (the same sum over the plateau-free skylines on 1, …, h − 1),
```

and `A^e_ridge = (A_ridge + S_ridge)/2` ([[proper-castle-projection](pages/proper-castle-projection.md)]). The subtracted sum is at most `(h − 1)(h − 2)^{w−1}` in absolute value. For `h ≤ 6` the spectral radius of `R̃_h` is below `δ_{h−1}`, so `A^e_ridge(w, h)` is half of `A_ridge(w, h)` up to a smaller term and is `δ_{h−1}` by width:[^exec]

| `h` | `ρ(R̃_h)` | `δ_{h−1}` | even-block ridge castles, `A^e_ridge(w, h)` for `w = 1, …, 10` |
|---|---|---|---|
| 2 | 1.000 | 1.618 | `1, 3, 4, 4, 5, 9, 17, 29, 46, 72` |
| 3 | 1.575 | 2.414 | `0, 0, 3, 16, 44, 104, 265, 674, 1640, 3972` |
| 4 | 1.768 | 3.303 | `1, 7, 25, 70, 209, 697, 2390, 8169, 27565, 91762` |
| 5 | 2.242 | 4.236 | `0, 0, 10, 104, 604, 2836, 12630, 55668, 242744, 1047448` |
| 6 | 2.413 | 5.193 | `1, 11, 66, 320, 1601, 8661, 47807, 261401, 1411224, 7537448` |

At width 1 the only ridge castle is the skyline `(h)`, with `h` blocks, so the first entry is 1 for even `h` and 0 for odd `h`.

## Computation

The counts, Equation (3) and Equation (1), checked against brute force for small widths:

```python
import sympy as sp
from itertools import product
x = sp.symbols('x')
def ok(a, b, h): return a != b or a == b == h
def blocks(c): return c[0] + sum(max(0, c[i] - c[i-1]) for i in range(1, len(c)))
def ridge(h, w):                        # (all, even-block) ridge castles of height h and width w
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

- [[metallic-strip-realizability](pages/metallic-strip-realizability.md)] - the growth constants of the natural strip rules on three heights, and the ridge rule as the rule that reaches every `δ_a`.
- [[proper-castle-projection](pages/proper-castle-projection.md)] - the subtraction of the strips that do not reach `h`, and the even-block counts through the signed transfer matrix.
- [[metallic-means](pages/metallic-means.md)] - de Spinadel's family `σ_p^q` and its `q = 1` row `δ_a`.
- [[castle-classification-shape](pages/castle-classification-shape.md)] - the ridge castles among the rate-of-change types.
- [[castle-classification-growth](pages/castle-classification-growth.md)] - the growth types by width, among them `δ_{h−1}` by width.
- [[fibonacci-castle](pages/fibonacci-castle.md)] - the castles of height 2 with no two neighboring columns of height 2, which the exchange of heights 1 and 2 relates to the ridge castles of height 2.
- [[1-smooth-pell-castles-by-area](pages/1-smooth-pell-castles-by-area.md)] - a table of the 1-smooth, Fibonacci and ridge neighbor rules at height 2.
- [[quadratic-min-height](pages/quadratic-min-height.md)], [[reachable-field-census](pages/reachable-field-census.md)] - the smallest height at which a strip rule grows at a given quadratic number; for `δ_a` it is `a + 1`.
- [[castle-strip](pages/castle-strip.md)] - strips, transfer matrices, and growth by width.
- [[castle-notation](pages/castle-notation.md)] - the ridge castle entry, `R_h`, and the tilde for signed transfer matrices.

## Footnotes

[^pe]: https://projecteuler.net/problem=502 (Project Euler, Problem 502 "Counting Castles", fetched 2026-10-03) - rules "The bottom row is occupied by a block of length w.", "The maximum achieved height of the entire castle is exactly h.", "The castle is made from an even number of blocks."
[^oeis]: https://oeis.org/A001333, https://oeis.org/A003688, https://oeis.org/A015448, https://oeis.org/A001076 (read 2026-10-16) - A001333 "Pell-Lucas numbers: numerators of continued fraction convergents to sqrt(2)" (1, 1, 3, 7, 17, 41, …); A003688 "a(n) = 3*a(n-1) + a(n-2), with a(1)=1 and a(2)=4" (1, 4, 13, 43, 142, …); A015448 "a(0) = 1, a(1) = 1, and a(n) = 4*a(n-1) + a(n-2) for n >= 2" (1, 1, 5, 21, 89, 377, …); A001076 "Denominators of continued fraction convergents to sqrt(5)" (0, 1, 4, 17, 72, 305, …).
[^exec]: Verified by execution (Python 3.11 with SymPy and NumPy, 2026-10-16): for `h = 2..6`, a transfer recurrence that tracks the height, whether `h` has been reached and the block parity gives both tables for `w ≤ 12`, and agrees with brute force over all skylines for `h ≤ 4`, `w ≤ 6`; Equation (3) matches every entry for `w ≤ 12`, and `A_ridge(w, 5) = F_{3w+2} − 4·3^{w−1}` for `w ≤ 12`; Equation (1) holds symbolically for `h = 2..6`; `ρ(R̃_h)` is computed numerically; of the `2^9` 0/1 matrices of size 3 none, and of the `2^{16}` of size 4 exactly 192, have an eigenvalue within `10^{−9}` of `(3 + √13)/2`; the example castle obeys the rule and has 12 blocks; the code block runs and prints the line shown.
