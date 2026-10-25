---
title: "Tower block-count = Narayana polynomial"
category: Analyses
summary: Towers with no height bound counted by blocks have generating function Narayana_L(x)/(1 − x)^L, with the Narayana polynomial Narayana_L(x) = Σ_k N(L, k) x^{k−1}, proved on the tower-heap page from the tower grammar and checked by enumeration for L ≤ 7. The rows L = 2, 3, 4, 5 are A005408, A005891, A063490 (offset 1) and A160747, and the entries A063490 and A160747 state the castle reading. The identity is one of generating functions: its k-th term counts the towers with k − 1 descents, and the count by peaks does not factor it.
tags: [oeis, tower, narayana, heap-of-pieces, generating-functions, cross-reference, analysis]
sources: [project-euler-502-brute-force, oeis-encyclopedia]
created: 2026-09-13
updated: 2026-10-25
---

# Tower block-count = Narayana polynomial

## The identity

Towers with no height bound have column heights `c_1, …, c_L ≥ 0` on a base of `L` columns, and their blocks are the maximal runs of columns in each row, `blocks = c_1 + Σ_{i≥2} max(0, c_i − c_{i−1})` ([[tower-heap](pages/tower-heap.md)]).[^1] Write `T̂(L, b)` for the number of towers on a base of length `L` with `b` blocks; the hat keeps `T(k, L)` for the towers of height at most `k` ([[castle-notation](pages/castle-notation.md)]). Then

```
T̂(L, b)              =  Σ_{k=1}^{L} N(L, k) C(b + L − k, L − 1),
Σ_{b≥0} T̂(L, b) x^b  =  Narayana_L(x) / (1 − x)^L,        Narayana_L(x)  =  Σ_{k=1}^{L} N(L, k) x^{k−1},
```

with `N(L, k) = (1/L) C(L, k) C(L, k−1)` the [[narayana-numbers](pages/narayana-numbers.md)], `A001263`. [[tower-heap](pages/tower-heap.md)] proves the identity from the fixed point of the tower grammar's height map (*Proof of the identity*), and it agrees with enumeration of all towers for `L ≤ 6`, `b ≤ 7` and for `L = 7`, `b ≤ 6`.[^2] The rows of `T̂`:[^3]

| `L` | `T̂(L, b)`, `b = 0, 1, 2, 3, …` | OEIS |
|---|---|---|
| 2 | 1, 3, 5, 7, 9, 11, … | `A005408`, the odd numbers |
| 3 | 1, 6, 16, 31, 51, 76, … | `A005891`, the centered pentagonal numbers |
| 4 | 1, 10, 40, 105, 219, 396, … | `A063490(b + 1)` (offset 1) |
| 5 | 1, 15, 85, 295, 771, 1681, … | `A160747` |
| 6 | 1, 21, 161, 721, 2331, 6083, … | - |
| 7 | 1, 28, 280, 1582, 6244, 19348, … | - |

`A005408`, `A005891` and `A160747` have offset 0 and `A063490` offset 1, so `T̂(4, b) = A063490(b + 1)`. `A160747` is named by its generating function `(1 + 10x + 20x² + 10x³ + x⁴)/(1 − x)^5`, which is `Narayana_5(x)/(1 − x)^5`, and `A005891` has the generating function `(1 + 3x + x²)/(1 − x)³ = Narayana_3(x)/(1 − x)³`. The entries `A063490` and `A160747` also state the castle reading: `A063490(n)` counts the castles of width 4 with `n` blocks and `A160747(n)` the castles of width 5 with `n + 1` blocks, of any height, which stand on the towers with one block fewer.[^4]

The identity is one of generating functions. Its `k`-th term counts the towers with `k − 1` descents, positions `i` with `c_i > c_{i+1}` ([[tower-heap](pages/tower-heap.md)]). The count of towers by peaks, plateaus higher than the columns on both sides with height 0 outside the base, matches its terms neither with `k` nor with `k − 1` peaks. The peaks factor the other Narayana sum, `T̂(L, b) = Σ_i N(b, i) C(L + 1 + 2b − 2i, 2b)`, indexed by blocks, its `i`-th term counting the towers with `i` peaks ([[cho-huh-nam-sohn-2022-bounded-free-motzkin-paths](pages/cho-huh-nam-sohn-2022-bounded-free-motzkin-paths.md)]).[^5]

## Key Takeaways

- `T̂(L, b) = Σ_k N(L, k) C(b + L − k, L − 1)`, with generating function `Narayana_L(x)/(1 − x)^L`, proved for every `L` on [[tower-heap](pages/tower-heap.md)] and checked by enumeration for `L ≤ 7`.[^2]
- The rows `L = 2, 3, 4, 5` are `A005408`, `A005891`, `A063490(b + 1)` and `A160747`.[^3][^4]
- The refinement by descents factors the identity term by term, and the refinement by peaks does not.[^5]
- A castle of width `L` with `b + 1` blocks stands on towers with `b` blocks, so `T̂(L, b)` counts the castles of semi-perimeter `L + b + 1` and width `L`, the triangle `A271942` ([[castle-perimeter](pages/castle-perimeter.md)]).

## Related Concepts

- [[tower-heap](pages/tower-heap.md)] - towers with no height bound, counted by blocks and by descents, and the proof of the identity.
- [[narayana-numbers](pages/narayana-numbers.md)] - `N(n, k)` and its other counts.
- [[cho-huh-nam-sohn-2022-bounded-free-motzkin-paths](pages/cho-huh-nam-sohn-2022-bounded-free-motzkin-paths.md)] - the same numbers as the `(L+1)`-core partitions with `b` corners, with a second Narayana sum indexed by blocks, `Σ_i N(b, i) C(L + 1 + 2b − 2i, 2b)`.
- [[viennot-heap-tower](pages/viennot-heap-tower.md)] - the identity read off a transfer matrix on the previous column height, and the descents.
- [[convex-castle-binomial-identity](pages/convex-castle-binomial-identity.md)] - the convex castles, counted by a binomial coefficient.
- [[oeis-mining-pe502](pages/oeis-mining-pe502.md)] - the other matches of castle counts against the OEIS.
- [[castle-conditional-entropy](pages/castle-conditional-entropy.md)] - the entropy of the block count of castles, and why the tower counts by blocks, which have no finite total at fixed base length, are not a model for it.

## Footnotes

[^1]: [[project-euler-502-brute-force](pages/project-euler-502-brute-force.md)] §"p_signed" L31-47 - "A new column of height b after a column of height a starts max(0, b - a) new runs, each contributing a factor of -1".
[^2]: Verified by execution (Python 3.11 with SymPy, 2026-10-25): `T̂(L, b)` and the formula against enumeration of all towers for `L ≤ 6`, `b ≤ 7` and for `L = 7`, `b ≤ 6`; the coefficients of `x^L` in the power-series root of the tower grammar's fixed-point equation equal `Narayana_L(y)/(1 − y)^L` for `L ≤ 10`.
[^3]: Verified by execution (Python 3.11, 2026-10-25): the rows `L = 2, …, 7` by enumeration of all towers; the rows `L = 2, 3, 4, 5` against the first eight terms of `A005408`, `A005891`, `A063490` (from `n = 1`) and `A160747` on oeis.org.
[^4]: https://oeis.org/A005408, https://oeis.org/A005891, https://oeis.org/A063490, https://oeis.org/A160747 (read 2026-10-25) - "The odd numbers: a(n) = 2*n + 1", offset 0; "Centered pentagonal numbers: (5n^2+5n+2)/2", "G.f.: (1 + 3*x + x^2)/(1 - x)^3", offset 0; "a(n) = (2*n - 1)*(7*n^2 - 7*n + 6)/6", offset 1, and "a(n) is also the number of castle polyominoes of width 4 with n blocks, of any height"; "Expansion of (1 + 10*x + 20*x^2 + 10*x^3 + x^4)/(1-x)^5", offset 0, and "a(n) is also the number of castle polyominoes of width 5 with n + 1 blocks, of any height".
[^5]: Verified by execution (Python 3.11, 2026-10-25), for `L ≤ 6`, `b ≤ 7` and `L = 7`, `b ≤ 6`: the towers with `k − 1` descents number `N(L, k) C(b + L − k, L − 1)`; the towers with `i ≥ 1` peaks number `N(b, i) C(L + 1 + 2b − 2i, 2b)`; and for each `L` from 2 to 7 the counts by peaks differ from the terms `N(L, k) C(b + L − k, L − 1)`, indexed by `k` peaks and by `k − 1` peaks.
