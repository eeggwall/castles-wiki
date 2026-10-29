---
title: Zig-zag castles
category: Concepts
summary: A zig-zag castle is a castle in which neighboring columns differ in height by exactly 1, the 1-smooth rule and the plateau-free rule imposed together. Imposing two strip rules at once multiplies their 0/1 matrices entrywise, and (I + A_path) ⊙ (J − I) = A_path, the adjacency matrix of the path on the heights, with characteristic polynomial U_h(x/2) and eigenvalues 2cos(πk/(h+1)). The zig-zag strips on the heights 1, …, h are the zig-zag paths in a rectangle of width h, counted by 27 OEIS entries, among them A153340 at h = 8, A090993 at h = 5 and the color splits of A153334 to A153373, and the step bits of a zig-zag castle of width w and height h are the (h − 1)-balanced binary strings of length w − 1 (A027383, A027557, A027559, A027560 at h = 3 to 6). A zig-zag castle has (c_1 + c_w + w − 1)/2 blocks, and the zig-zag castles of height h grow at 2cos(π/(h+1)) by width - √2 at h = 3, golden by width at h = 4.
tags: [concept, castle, zig-zag-castle, strip-rule, transfer-matrix, path-graph, chebyshev, balanced-strings, block-count, parity, golden, oeis, verification]
sources: [project-euler-502-brute-force]
created: 2026-10-27
updated: 2026-10-28
---

# Zig-zag castles

## Definition

A castle of width `w` and height `h` is a skyline `(c_1, …, c_w)` with `1 ≤ c_i ≤ h` and some `c_i = h` ([[castle-polyomino](pages/castle-polyomino.md)]). The **zig-zag rule** lets a column of height `a` stand next to a column of height `b` when `|a − b| = 1`. A **zig-zag castle** is a castle whose neighboring columns all obey the zig-zag rule: each column is one higher or one lower than the column before it. `A_zigzag(w, h)` is the number of zig-zag castles of width `w` and height `h`, and `A^e_zigzag(w, h)` and `A^o_zigzag(w, h)` count those with an even and with an odd number of blocks ([[castle-notation](pages/castle-notation.md)]).

The zig-zag rule is two rules of [[castle-strip](pages/castle-strip.md)] at once: the 1-smooth rule `|a − b| ≤ 1` and the plateau-free rule `a ≠ b`. The name follows the zig-zag paths of the OEIS, which are the zig-zag strips of the section *Zig-zag strips are zig-zag paths*.

*Example.* The zig-zag castles of width 4 and height 3 are the six skylines

```
(1, 2, 3, 2)   (2, 1, 2, 3)   (2, 3, 2, 1)   (2, 3, 2, 3)   (3, 2, 1, 2)   (3, 2, 3, 2)

  . . # .        . . . #        . # . .        . # . #        # . . .        # . # .
  . # # #        # . # #        # # # .        # # # #        # # . #        # # # #
  # # # #        # # # #        # # # #        # # # #        # # # #        # # # #
```

The skyline `(1, 2, 2, 3)` is not a zig-zag castle, since its second and third columns have the same height, and the skyline `(1, 3, 2)` is not one either, since its first two heights differ by 2.[^exec2]

A zig-zag castle is not a castle of the Zigzag type of [[castle-classification-shape](pages/castle-classification-shape.md)], whose differences `c_{i+1} − c_i` alternate in sign: the skyline `(1, 2, 3)` is a zig-zag castle and not of the Zigzag type, and the skyline `(1, 3, 2, 3, 1)` is of the Zigzag type and not a zig-zag castle. The Dyck-path castles of the same page are the zig-zag castles with both end columns at height 1.

## Two rules at once

A strip rule on the heights `1, …, h` is an `h × h` matrix of 0s and 1s, with a 1 in row `a` and column `b` when a column of height `a` may stand to the left of a column of height `b` ([[castle-strip](pages/castle-strip.md)]). A pair of neighboring heights obeys two rules at once when both matrices have a 1 in its place. So the matrix of two rules `M` and `M′` imposed together is their entrywise product `M ⊙ M′`, with entries `(M ⊙ M′)[a][b] = M[a][b] · M′[a][b]`.

The 1-smooth rule is the matrix `I + A_path`, with `I` the identity matrix and `A_path` the adjacency matrix of the path on the heights `1, …, h`, which has a 1 where `|a − b| = 1`. The plateau-free rule is `J − I`, with `J` the all-ones matrix. At `h = 3`:

```
  I + A_path         J − I           (I + A_path) ⊙ (J − I)

  [1 1 0]           [0 1 1]               [0 1 0]
  [1 1 1]     ⊙     [1 0 1]       =       [1 0 1]
  [0 1 1]           [1 1 0]               [0 1 0]
```

The zero diagonal of `J − I` removes the diagonal of `I + A_path`, and the other 1s of `I + A_path` lie off the diagonal and remain. So at every height

```
(I + A_path) ⊙ (J − I)  =  A_path,                                          (1)
```

and the zig-zag rule is the path on the heights.[^exec1]

## Zig-zag strips are zig-zag paths

A **zig-zag strip** of width `w` on the heights `1, …, h` is a skyline in `{1, …, h}^w` whose neighboring columns obey the zig-zag rule. A strip need not reach height `h`, so it need not be a castle of height `h`; the zig-zag strips that reach `h` are the zig-zag castles of height `h`. By Equation (1) of [[castle-strip](pages/castle-strip.md)], the number of zig-zag strips of width `w` is

```
zstrips(w, h)  =  𝟙ᵀ A_path^{w−1} 𝟙,                                       (2)
```

with `A_path` on the heights `1, …, h` and `𝟙` the all-ones vector of length `h`. Subtracting the strips that stay below `h`,

```
A_zigzag(w, h)  =  zstrips(w, h) − zstrips(w, h − 1).                      (3)
```

The OEIS counts the same skylines as zig-zag paths in a rectangle. A153340 is the "Number of zig-zag paths from top to bottom of a rectangle of width 8 with n rows", and Andrew Howroyd's comment on it counts the "words of length n using an 8-symbol alphabet where neighboring letters are neighbors in the alphabet".[^howroyd] With the heights `1, …, 8` as the letters, these words are the zig-zag strips on the heights `1, …, 8`. In the rectangle, the path's cell in row `i` is in column `c_i`: the rectangle's width is the number of heights `h`, and its number of rows is the strip's width `w`.

Several entries count only the paths whose cells have the color of the top right corner of a checkerboard, or only the others.[^colour] Each step of the path moves one row down and one column over, so every cell of the path has the color of its first cell, which is in column `c_1` of the top row. That cell has the color of the top right corner, in column `h`, exactly when `c_1` has the parity of `h`. Read this way, the entries below are counts of zig-zag strips:

| heights `h` | entry | the zig-zag strips counted by the `n`-th term |
|---|---|---|
| 5 | A090993 | all, of width `n + 1` |
| 5 | A153339 | `c_1` odd, of width `n` |
| 6 | A090995 | all, of width `n + 1` |
| 7 | A030436 | `c_1 = 1`, of width `n + 1`; also `c_1` even, of width `n − 2`, for `n ≥ 3` |
| 7 | A030435 | `c_1` odd, of width `n − 1`, for `n ≥ 2`; also `2·A030436(n)` |
| 8 | A153340 | all, of width `n` |
| 8 | A090992 | `c_1` even, of width `n + 1` |
| 9 | A153362; A153363, A153364 | all; `c_1` odd; `c_1` even; of width `n` |
| 9 | A153365; A153366, A153367 | `c_1` odd, of width `2n`; `c_1` odd and `c_1` even, of width `2n − 1` |
| 10 | A153360 | all, of width `n` |
| 10 | A090994 | `c_1` even, of width `n + 1` |
| 11 | A153368; A153369, A153370 | all; `c_1` odd; `c_1` even; of width `n` |
| 11 | A153371; A153372, A153373 | `c_1` odd, of width `2n`; `c_1` odd and `c_1` even, of width `2n − 1` |
| `n` | A153334, A153335 | the `n × n` square: of width `n`, `c_1` with the parity of `n`; `c_1` with the other parity |
| `2n` | A153336 | the `2n × 2n` square: of width `2n`, `c_1` even |
| `2n − 1` | A153337, A153338 | the `(2n − 1) × (2n − 1)` square: of width `2n − 1`, `c_1` odd; `c_1` even |

Every entry agrees with Equation (2) and its first-column restrictions on every term of its data field.[^exec3] A090992 to A090995 count the meaningful differential operations of order `n` on `R^7` to `R^10`, and their comments give the zig-zag and path-graph readings; A030436 counts, in a comment by Johannes W. Meijer, the "paths of length n, n>=0, starting at the initial node on the path graph P_7", whose `n + 1` vertices are the columns of a strip with `c_1 = 1`.[^paths]

## Castles of height h are balanced strings

The **step bits** of a zig-zag castle are the 0/1 string of length `w − 1` whose `i`-th letter is 1 when `c_{i+1} = c_i + 1` and 0 when `c_{i+1} = c_i − 1`. A 0/1 string is **`(h − 1)`-balanced** when in every factor, every run of consecutive letters, the number of 1s minus the number of 0s lies between `−(h − 1)` and `h − 1`. This is the k-balanced string of A027557 and its neighbors with `k = h − 1`.[^balanced]

**Theorem.** For `h ≥ 2` and `w ≥ 1`, the step bits map the zig-zag castles of width `w` and height `h` one-to-one onto the `(h − 1)`-balanced strings of length `w − 1`. So `A_zigzag(w, h)` is the number of `(h − 1)`-balanced strings of length `w − 1`.

*Proof.* The factor of the step bits from letter `i` to letter `j − 1` has `c_j − c_i` more 1s than 0s. So the step bits are `(h − 1)`-balanced exactly when any two columns of the skyline differ by at most `h − 1`, which holds for every skyline in `{1, …, h}^w`. Conversely, a 0/1 string of length `w − 1` determines the differences `c_{i+1} − c_i`, and so a skyline up to a vertical shift. Exactly one shift puts the tallest column at height `h`, and its shortest column is then at height at least 1 exactly when the tallest and shortest columns differ by at most `h − 1`, that is, when the string is `(h − 1)`-balanced. ∎

The counts, with the OEIS entries of the balanced strings:[^exec4]

| `h` | `A_zigzag(w, h)`, `w = 1, …, 12` | OEIS |
|---|---|---|
| 2 | `1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2` | - |
| 3 | `1, 2, 4, 6, 10, 14, 22, 30, 46, 62, 94, 126` | A027383(`w − 1`) |
| 4 | `1, 2, 4, 8, 14, 26, 44, 78, 130, 224, 370, 626` | A027557(`w − 1`) |
| 5 | `1, 2, 4, 8, 16, 30, 58, 106, 200, 360, 668, 1190` | A027559(`w − 1`) |
| 6 | `1, 2, 4, 8, 16, 32, 62, 122, 232, 450, 846, 1622` | A027560(`w − 1`) |

The zig-zag castles of height 2 of width `w ≥ 2` are the two skylines `(1, 2, 1, …)` and `(2, 1, 2, …)`. At height 3 the formula of A027383 gives

```
A_zigzag(w, 3)  =  3 · 2^{(w−1)/2} − 2    (w odd),        2^{(w+2)/2} − 2    (w even),
```

and at height 4 Max Alekseyev's formula on A027557 gives, with `F_n` the Fibonacci numbers,[^balanced]

```
A_zigzag(w, 4)  =  2 F_{w+2} − 2^{⌊(w+1)/2⌋} − 2^{⌊w/2⌋},
```

for example `2 · 13 − 8 − 4 = 14` at `w = 5`.

## Blocks

The block count of a castle is `blocks(c) = c_1 + Σ_{i=2}^{w} max(0, c_i − c_{i−1})`.[^blocks] In a zig-zag castle every rise is one step up, so `blocks(c)` is `c_1` plus the number of steps up. The `w − 1` steps go up or down by one, and the steps up outnumber the steps down by `c_w − c_1`, so there are `(w − 1 + c_w − c_1)/2` steps up and

```
blocks(c)  =  (c_1 + c_w + w − 1) / 2.                                      (4)
```

For the skyline `(1, 2, 3, 2)`, Equation (4) gives `(1 + 2 + 3)/2 = 3`, one block in each of the rows 1, 2 and 3. The six castles of the example have 3, 4, 3, 4, 4 and 4 blocks, so `A^e_zigzag(4, 3) = 4` and `A^o_zigzag(4, 3) = 2`. By Equation (4), a zig-zag castle has an even number of blocks exactly when `c_1 + c_w + w − 1` is divisible by 4, so the parity of the block count depends only on the width and the two end columns.

The even-block and odd-block counts, for `w = 1, …, 12`:[^exec5]

| `h` | `A^e_zigzag(w, h)` | `A^o_zigzag(w, h)` |
|---|---|---|
| 2 | `1, 2, 1, 0, 1, 2, 1, 0, 1, 2, 1, 0` | `0, 0, 1, 2, 1, 0, 1, 2, 1, 0, 1, 2` |
| 3 | `0, 0, 1, 4, 7, 6, 7, 16, 31, 30, 31, 64` | `1, 2, 3, 2, 3, 8, 15, 14, 15, 32, 63, 62` |
| 4 | `1, 2, 3, 4, 5, 12, 26, 42, 57, 104, 201, 334` | `0, 0, 1, 4, 9, 14, 18, 36, 73, 120, 169, 292` |
| 5 | `0, 0, 1, 4, 9, 16, 28, 50, 101, 188, 333, 574` | `1, 2, 3, 4, 7, 14, 30, 56, 99, 172, 335, 616` |
| 6 | `1, 2, 3, 4, 7, 16, 32, 60, 115, 230, 424, 792` | `0, 0, 1, 4, 9, 16, 30, 62, 117, 220, 422, 830` |

Every entry agrees with brute-force enumeration.

## Spectrum and growth

The characteristic polynomial of `A_path` on the heights `1, …, h` is `det(xI − A_path) = U_h(x/2)`, with `U_h` the Chebyshev polynomial of the second kind, and its eigenvalues are `2cos θ_k`, `θ_k = πk/(h+1)`, `k = 1, …, h`.[^exec1] They are the eigenvalues `λ_k = 1 + 2cos θ_k` of the 1-smooth matrix `I + A_path` minus one ([[1-smooth-castles](pages/1-smooth-castles.md)], [[motzkin-castles](pages/motzkin-castles.md)]).

The largest eigenvalue is `2cos(π/(h+1))`, so by Equation (2) of [[castle-strip](pages/castle-strip.md)] the zig-zag strips on the heights `1, …, h` grow at `2cos(π/(h+1))` by width. In Equation (3) the subtracted strips grow at the smaller `2cos(π/h)`, so the zig-zag castles of height `h` grow at `2cos(π/(h+1))` by width as well. The eigenvalues come in pairs `±2cos θ_k`, so the counts are compared two widths apart: `A_zigzag(w + 2, h)/A_zigzag(w, h)` tends to `4cos²(π/(h+1))`.[^exec6]

| `h` | growth by width `2cos(π/(h+1))` |
|---|---|
| 2 | `1` |
| 3 | `√2 = 1.41421…` |
| 4 | `φ = (1 + √5)/2 = 1.61803…`, golden by width |
| 5 | `√3 = 1.73205…` |
| 6 | `2cos(π/7) = 1.80194…` |
| `h → ∞` | `2` |

At height 4 the generating function of A027557 is `(1 + x − x²)/((1 − x − x²)(1 − 2x²))`:[^balanced] the factor `1 − x − x²` carries the golden mean of the strips on four heights, and `1 − 2x²` the growth `√2` of the strips on three heights that Equation (3) subtracts.

## Related Concepts

- [[castle-strip](pages/castle-strip.md)] - strip rules as 0/1 matrices; the zig-zag rule is its 1-smooth and plateau-free rules imposed together.
- [[motzkin-castles](pages/motzkin-castles.md)] - the 1-smooth strip `I + A_path`, with eigenvalues `1 + 2cos θ_k`, and the Motzkin strips on bounded heights.
- [[1-smooth-castles](pages/1-smooth-castles.md)] - the anchored 1-smooth castles and the determinants `χ_h(x) = det(I − x(I + A_path))`, written with `U_h`.
- [[castle-classification-shape](pages/castle-classification-shape.md)] - the zig-zag type among the rate-of-change types; the Zigzag type, with differences alternating in sign; the Dyck-path castles, the zig-zag castles with both end columns at height 1.
- [[castle-classification-growth](pages/castle-classification-growth.md)] - growth types by width; the zig-zag castles of height 4 are golden by width.
- [[dyck-words](pages/dyck-words.md)], [[catalan-numbers](pages/catalan-numbers.md)] - Dyck paths: lowering every column of a zig-zag castle with both end columns at height 1 by one gives a Dyck path of length `w − 1`.
- [[kernel-method](pages/kernel-method.md)] - walks with a finite set of jumps between two walls, here the jumps `−1` and `+1`, counted through the roots of the kernel instead of the transfer matrix.
- [[castle-graph-spectral-radius](pages/castle-graph-spectral-radius.md)] - the path eigenvalues `2cos(jπ/(n+1))` as spectral radii of castle graphs.
- [[hilbert-castles](pages/hilbert-castles.md)] - the dual rule `J − A_path`, which allows exactly the pairs the zig-zag rule forbids; by the Hilbert duality the Hilbert strips have the series `1/Z_h(−x)`, with `Z_h(x)` the series of the zig-zag strips, the empty strip included.
- [[castle-notation](pages/castle-notation.md)] - `A_path`, `θ_k`, `M ⊙ M′`, `zstrips(w, h)` and `A_zigzag(w, h)`.

## Footnotes

[^howroyd]: https://oeis.org/A153340 (read 2026-10-27) - "Number of zig-zag paths from top to bottom of a rectangle of width 8 with n rows.", and the comment "Number of words of length n using an 8-symbol alphabet where neighboring letters are neighbors in the alphabet. - _Andrew Howroyd_, Apr 17 2017". A153362, A153360, A153368 and A153361 carry the same name and comment at widths 9, 10, 11 and 12.
[^colour]: https://oeis.org/A153339 and https://oeis.org/A153334 (read 2026-10-27) - "Number of zig-zag paths from top to bottom of a rectangle of width 5 with n rows whose color is that of the top right corner." and "Number of zig-zag paths from top to bottom of an n X n square whose color is that of the top right corner."; A153335 to A153338 and A153363 to A153373 split the paths in the same way, with "whose color is not that of the top right corner" for the others.
[^paths]: https://oeis.org/A090992, https://oeis.org/A090993, https://oeis.org/A090994, https://oeis.org/A090995, https://oeis.org/A030435, https://oeis.org/A030436 (read 2026-10-27) - names "Number of meaningful differential operations of the n-th order on the space R^7." to "R^10."; comments "Also (starting 4,7,...) the number of zig-zag paths from top to bottom of a rectangle of width 8, whose color is that of the top right corner." (A090992), "Number of walks of length n on the path graph P_5." (A090993), "Also (starting 5,9,...) the number of zig-zag paths from top to bottom of a rectangle of width 10, whose color is that of the top right corner." (A090994), "Number of walks of length n on the path graph P_6." (A090995), "Also (starting 4,6,...) the number of zig-zag paths from top to bottom of a rectangle of width 7, whose color is that of the top right corner." (A030435), and "Counts all paths of length n, n>=0, starting at the initial node on the path graph P_7" (A030436, Johannes W. Meijer).
[^balanced]: https://oeis.org/A027383, https://oeis.org/A027557, https://oeis.org/A027559, https://oeis.org/A027560 (read 2026-10-27) - A027557: "Number of 3-balanced strings of length n: let d(S)= #(1)'s in S - #(0)'s, then S is k-balanced if every substring T has -k<=d(T)<=k; here k=3.", formulas "a(n) = 2*A000045(n+3) - 2^floor((n+2)/2) - 2^floor((n+1)/2). - _Max Alekseyev_, Jun 02 2005" and "g.f. (1+x-x^2) / (1-x-x^2)(1-2x^2)"; A027559 and A027560 the same with "k=4" and "k=5"; A027383: name "a(2*n) = 3*2^n - 2; a(2*n+1) = 2^(n+2) - 2.", comment "Number of balanced strings of length n: ... S is balanced if every substring T of S has -2 <= d(T) <= 2". The entries' `d(S)` is the number of 1s minus the number of 0s.
[^blocks]: [[project-euler-502-brute-force](pages/project-euler-502-brute-force.md)] §"brute" L24 - "= c_1 + \sum_{i=2}^{w} \max(0, c_i - c_{i-1})", the column-height block-count formula.
[^exec1]: Verified by execution (Python 3.10 with NumPy and SymPy, 2026-10-27): `bin/python/zig_zag_castles.py` item [1], run log `bin/python/zig_zag_castles-run.log`. Equation (1) for `h = 2, …, 12`; the characteristic polynomial `U_h(x/2)` and the eigenvalues `2cos(πk/(h+1))` for `h = 1, …, 12`.
[^exec2]: Verified by execution (Python 3.10, 2026-10-27): `bin/python/zig_zag_castles.py` item [2], run log `bin/python/zig_zag_castles-run.log`. The six zig-zag castles of width 4 and height 3, their drawings and block counts.
[^exec3]: Verified by execution (Python 3.10, 2026-10-27): `bin/python/zig_zag_castles.py` item [3], run log `bin/python/zig_zag_castles-run.log`. Each row of the table against every term of the entry's data field (22 to 38 terms).
[^exec4]: Verified by execution (Python 3.10, 2026-10-27): `bin/python/zig_zag_castles.py` item [4], run log `bin/python/zig_zag_castles-run.log`. Equation (3) against every term of A027383, A027557, A027559 and A027560 (33 to 43 terms); the bijection onto the `(h − 1)`-balanced strings for `h = 2, …, 7` and `w = 1, …, 13`; the closed forms at heights 2, 3 and 4 for `w < 60`.
[^exec5]: Verified by execution (Python 3.10, 2026-10-27): `bin/python/zig_zag_castles.py` item [5], run log `bin/python/zig_zag_castles-run.log`. Equation (4) on every zig-zag strip with `h ≤ 7` and `w ≤ 12`; the even-block and odd-block counts from Equation (4) against brute-force enumeration for `h = 2, …, 7` and `w ≤ 12`, and from Equation (4) alone for `w ≤ 16`.
[^exec6]: Verified by execution (Python 3.10, 2026-10-27): `bin/python/zig_zag_castles.py` item [6], run log `bin/python/zig_zag_castles-run.log`. `√(A_zigzag(4002, h)/A_zigzag(4000, h))` against `2cos(π/(h+1))` for `h = 2, …, 9`, equal to twelve decimals; `2cos(π/5) = φ`.
