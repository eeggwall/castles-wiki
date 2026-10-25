---
title: "Tower block-count = Narayana polynomial"
category: Sources
summary: OEIS-mining notes on towers with no height bound counted by blocks. Their generating function is Narayana_L(x)/(1 − x)^L with the Narayana polynomial Narayana_L(x) = Σ_k N(L, k) x^{k−1}, checked in the source for L ≤ 7 and proved on the tower-heap page from the tower grammar; the rows L = 2, 3, 4, 5 are A005408, A005891, A063490 (offset 1) and A160747. The identity behind A001263 is a generating-function identity: a refinement by peaks does not factor it, and the refinement by descents does.
tags: [oeis, tower, narayana, heap-of-pieces, generating-functions, cross-reference, source]
sources: [tower-narayana-polynomial]
created: 2026-09-13
updated: 2026-10-25
---

# Tower block-count = Narayana polynomial

**Source:** `raw/oeis-pe502/crosslink-avenues.md` §"Tier 2", with the notes `raw/oeis-pe502/xrefs/A001263-tower.md`, `A005408-tower.md`, `A005891-tower.md`, `A063490-tower.md` and `A160747-tower.md`
**Date ingested:** 2026-09-13
**Type:** OEIS-mining notes

## Summary

The notes count towers with no height bound: column heights `c_1, …, c_w ≥ 0` on a base of `w` columns, with blocks the maximal runs of columns in each row, `blocks = c_1 + Σ_{i≥2} max(0, c_i − c_{i−1})` ([[tower-heap](pages/tower-heap.md)]).[^1] The wiki writes the base length `L` and the number of towers on a base of length `L` with `b` blocks `T̂(L, b)`; the notes write `T(w, b)`, which the wiki keeps for the tower count `T(k, L)` of towers of height at most `k`. The notes state, and check against brute force for `w ≤ 7`,[^2]

```
T̂(L, b)              =  Σ_{k=1}^{L} N(L, k) C(b + L − k, L − 1),
Σ_{b≥0} T̂(L, b) x^b  =  Narayana_L(x) / (1 − x)^L,        Narayana_L(x)  =  Σ_{k=1}^{L} N(L, k) x^{k−1},
```

with `N(L, k) = (1/L) C(L, k) C(L, k−1)` the [[narayana-numbers](pages/narayana-numbers.md)], `A001263`. The rows of `T̂`:[^3]

| `L` | `T̂(L, b)`, `b = 0, 1, 2, 3, …` | OEIS |
|---|---|---|
| 2 | 1, 3, 5, 7, 9, 11, … | `A005408`, the odd numbers |
| 3 | 1, 6, 16, 31, 51, 76, … | `A005891`, the centered pentagonal numbers |
| 4 | 1, 10, 40, 105, 219, 396, … | `A063490(b + 1)` (offset 1) |
| 5 | 1, 15, 85, 295, 771, 1681, … | `A160747` |
| 6 | 1, 21, 161, 721, 2331, 6083, … | - |
| 7 | 1, 28, 280, 1582, 6244, 19348, … | - |

Every entry agrees with enumeration of all towers ([[tower-heap](pages/tower-heap.md)]).[^4] `A005408`, `A005891` and `A160747` have offset 0; `A160747` is named by its generating function `(1 + 10x + 20x² + 10x³ + x⁴)/(1 − x)^5`, which is `Narayana_5(x)/(1 − x)^5`.[^5]

The identity behind `A001263` is a generating-function identity and not a statement about peaks: "a direct peaks refinement was tested and does not factor this way".[^6] The refinement that does factor it is by descents: the `k`-th term counts the towers with `k − 1` descents ([[tower-heap](pages/tower-heap.md)], computed for `L ≤ 7`).

## Key Takeaways

- `T̂(L, b) = Σ_k N(L, k) C(b + L − k, L − 1)`, with generating function `Narayana_L(x)/(1 − x)^L`; checked in the source for `L ≤ 7`,[^2] and proved for every `L` on [[tower-heap](pages/tower-heap.md)] from the fixed point of the tower grammar's height map.
- The rows `L = 2, 3, 4, 5` are `A005408`, `A005891`, `A063490(b + 1)` and `A160747`.[^3]
- The `A001263` formula is a generating-function identity; a refinement by peaks does not factor it.[^6]
- A castle of width `L` with `b + 1` blocks stands on towers with `b` blocks, so `T̂(L, b)` counts the castles of semi-perimeter `L + b + 1` and width `L`, the triangle `A271942` ([[castle-perimeter](pages/castle-perimeter.md)]).

## Entities & Concepts

- [[tower-heap](pages/tower-heap.md)] - towers with no height bound, counted by blocks and by descents.
- [[narayana-numbers](pages/narayana-numbers.md)] - `N(n, k)` and its other counts.
- [[cho-huh-nam-sohn-2022-bounded-free-motzkin-paths](pages/cho-huh-nam-sohn-2022-bounded-free-motzkin-paths.md)] - the same numbers as the `(L+1)`-core partitions with `b` corners, with a second Narayana sum indexed by blocks, `Σ_i N(b, i) C(L + 1 + 2b − 2i, 2b)`.
- [[convex-castle-binomial-identity](pages/convex-castle-binomial-identity.md)] - the convex castles, counted by a binomial coefficient.
- [[oeis-mining-pe502](pages/oeis-mining-pe502.md)] - the mining pass these notes belong to.
- [[castle-conditional-entropy](pages/castle-conditional-entropy.md)] - the entropy of the block count of castles, and why the tower counts by blocks, which have no finite total at fixed base length, are not a model for it.

## Footnotes

[^1]: `raw/oeis-pe502/crosslink-avenues.md` §"Tier 2" L36-37 - "A **tower** of width w is column heights `c_1..c_w >= 0` (no full-bottom-row, no max-height, no parity). Blocks are maximal horizontal runs, `#blocks = c_1 + sum max(0, c_i − c_{i−1})`."
[^2]: `raw/oeis-pe502/crosslink-avenues.md` §"Tier 2" L41-47 - "Result (verified for w = 1..7 against brute force): T(w,b) = # towers of width w with exactly b blocks = sum_{k=1..w} Narayana(w,k) * C(b + w − k, w − 1) (Narayana-polynomial g.f.) g.f. = (Narayana_w(x)) / (1 − x)^w, Narayana_w(x) = sum_k Narayana(w,k) x^{k−1}. Narayana(w,k) = (1/w) C(w,k) C(w,k−1) = **A001263**."
[^3]: `raw/oeis-pe502/crosslink-avenues.md` §"Tier 2" L49-56 - the table of `T(w, b)` for `w = 2, …, 7`, with "A005408 (odd numbers)", "A005891 (centered pentagonal)", "A063490", "A160747", and "**new**" for `w = 6, 7`; `raw/oeis-pe502/xrefs/A063490-tower.md` §"Identity (verified, note the offset shift)" L8-10 - "A063490 = \"a(n) = (2n-1)(7n^2-7n+6)/6\", **offset 1** ... a(n) = T(4, n-1)".
[^4]: Verified by execution (Python 3.11, 2026-10-16): the table against enumeration of all towers for `L ≤ 6`, `b ≤ 7` and `L = 7`, `b ≤ 6`.
[^5]: https://oeis.org/A005408, https://oeis.org/A005891, https://oeis.org/A063490, https://oeis.org/A160747 (read 2026-10-16) - "The odd numbers: a(n) = 2*n + 1"; "Centered pentagonal numbers: (5n^2+5n+2)/2"; "a(n) = (2*n - 1)*(7*n^2 - 7*n + 6)/6", offset 1, "G.f.: x*(1+x)*(1+5*x+x^2)/(1-x)^4"; "Expansion of (1 + 10*x + 20*x^2 + 10*x^3 + x^4)/(1-x)^5", offset 0.
[^6]: `raw/oeis-pe502/xrefs/A001263-tower.md` §"Identity (verified)" L23-25 - "It is a generating-function identity, **not** a \"peaks\" bijection: a direct peaks refinement was tested and does not factor this way, so do not state a peaks interpretation."
