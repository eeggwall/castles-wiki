---
title: Narayana numbers
category: Concepts
summary: The Narayana numbers N(n, k) = (1/n) C(n, k) C(n, k−1) (OEIS A001263) count the Dyck paths of semilength n with k peaks and the parallelogram polyominoes of semi-perimeter n + 1 and width k, and sum over k to the Catalan number C_n. On the castle side they are the numerator of the generating function of towers counted by blocks, Σ_b T̂(L, b) x^b = Σ_k N(L, k) x^{k−1} / (1 − x)^L (proved from the tower grammar), and, as Dyck paths by peaks, the terms of the second sum T̂(L, b) = Σ_i N(b, i) C(L + 1 + 2b − 2i, 2b), indexed by blocks.
tags: [concept, narayana, catalan, oeis, tower, generating-functions]
sources: [algebraic-languages-and-polyominoes-enumeration, cho-huh-nam-sohn-2022-bounded-free-motzkin-paths]
created: 2026-09-13
updated: 2026-10-25
---

# Narayana numbers

## Definition

The **Narayana numbers** are

```
N(n, k)  =  (1/n) C(n, k) C(n, k−1),        1 ≤ k ≤ n,
```

the triangle A001263, read by rows `1; 1, 1; 1, 3, 1; 1, 6, 6, 1; 1, 10, 20, 10, 1; …`.[^1] They refine the [[catalan-numbers](pages/catalan-numbers.md)]: `Σ_k N(n, k) = C_n`, which gives `1, 2, 5, 14, 42, 132, 429` for `n = 1, …, 7`.

`N(n, k)` counts the Dyck paths of semilength `n` with `k` peaks, a peak being a step `U` followed by a step `D`. *Example:* the five Dyck paths of semilength 3 are `UUUDDD` with one peak, `UUDUDD`, `UUDDUD` and `UDUUDD` with two, and `UDUDUD` with three, so `N(3, 1) = 1`, `N(3, 2) = 3` and `N(3, 3) = 1`.

`N(n, k)` also counts the parallelogram polyominoes of perimeter `2n + 2`, that is of semi-perimeter `n + 1`, and width `k`. Delest and Viennot obtain this from a `2 × 2` determinant and carry it to the Dyck paths by peaks through their bijection β, which sends the peaks of a Dyck path to the columns of a parallelogram polyomino ([[parallelogram-polyomino-dyck-bijection](pages/parallelogram-polyomino-dyck-bijection.md)]).[^2] Both counts agree with enumeration for `n ≤ 7`.[^3]

## Towers counted by blocks

Write `T̂(L, b)` for the number of towers on a base of length `L` with `b` blocks, of any height ([[tower-heap](pages/tower-heap.md)]). The hat distinguishes it from the tower count `T(k, L)`, whose first argument is a height bound; the sources write `T(w, b)`. The Narayana numbers give its generating function in `b`:[^4]

```
Σ_{b≥0} T̂(L, b) x^b  =  Narayana_L(x) / (1 − x)^L,        Narayana_L(x)  =  Σ_{k=1}^{L} N(L, k) x^{k−1},
T̂(L, b)              =  Σ_{k=1}^{L} N(L, k) C(b + L − k, L − 1).
```

This agrees with enumeration for `L ≤ 6`, `b ≤ 7`, and for `L = 7`, `b ≤ 6`,[^3] and [[tower-heap](pages/tower-heap.md)] proves it: the substitution `x = z(1 − y)` turns the fixed point of the tower grammar's height map into the first-return equation of Dyck paths counted by peaks. The `k`-th term counts the towers whose column heights have `k − 1` descents (computed over the same range). At `L = 2`, `T̂(2, b) = C(b + 1, 1) + C(b, 1) = 2b + 1`: of the `2b + 1` towers `(c_1, c_2)` with `max(c_1, c_2) = b`, the `b + 1` with `c_1 ≤ c_2` have no descent and the `b` with `c_1 > c_2` have one. [[tower-heap](pages/tower-heap.md)] treats these counts, and [[tower-narayana-polynomial](pages/tower-narayana-polynomial.md)] records the source and the OEIS rows.

The Narayana numbers also enter with the index on the blocks, through Dyck paths by peaks. Cho, Huh, Nam and Sohn prove, for `b ≥ 1`,[^5]

```
T̂(L, b)  =  Σ_{i=1}^{min(b, ⌊(L+1)/2⌋)}  N(b, i) · C(L + 1 + 2b − 2i, 2b).
```

Deleting the flat steps of a tower word with `b` blocks leaves a Dyck path of semilength `b`, and `N(b, i)` of these have `i` peaks. The binomial counts the ways to put the `L` flat steps back with at least one at each peak and each valley. Term `i` counts the towers with `i` plateaus higher than the columns on both sides, with height 0 outside the base (checked for `L ≤ 7`).[^6] At `L = 2` the only term is `i = 1`, `N(b, 1) C(2b + 1, 2b) = 2b + 1`. The same paper reads `T̂(L, b)` as the number of `(L+1)`-core partitions with `b` corners ([[cho-huh-nam-sohn-2022-bounded-free-motzkin-paths](pages/cho-huh-nam-sohn-2022-bounded-free-motzkin-paths.md)], [[tower-heap](pages/tower-heap.md)]).

The convex castles are counted by a binomial coefficient, not by Narayana numbers ([[convex-castle-binomial-identity](pages/convex-castle-binomial-identity.md)]).

## Appearances in Sources

- [[algebraic-languages-and-polyominoes-enumeration](pages/algebraic-languages-and-polyominoes-enumeration.md)] - Remark 4.4: parallelogram polyominoes by width are counted by `N(n, k)`, and β carries this to Dyck paths by peaks.
- [[baril-florez-ramirez-2026-generalized-narayana-arrays](pages/baril-florez-ramirez-2026-generalized-narayana-arrays.md)] - `N(n, k)` refined by the heights of the `k` peaks (type-1 and type-2 Narayana arrays).
- [[cho-huh-nam-sohn-2022-bounded-free-motzkin-paths](pages/cho-huh-nam-sohn-2022-bounded-free-motzkin-paths.md)] - Proposition 3.4: the `t`-cores with `m` corners, which are the towers on a base of length `t − 1` with `m` blocks, counted by `Σ_i N(m, i) C(t + 2m − 2i, 2m)`.

## Related Concepts

- [[tower-heap](pages/tower-heap.md)] - towers counted by blocks, with the refinement by descents.
- [[catalan-numbers](pages/catalan-numbers.md)] - the row sums `Σ_k N(n, k) = C_n`.
- [[parallelogram-polyomino-dyck-bijection](pages/parallelogram-polyomino-dyck-bijection.md)] - Delest-Viennot's β, under which the width of a parallelogram polyomino is the number of peaks of a Dyck path.
- [[convex-castle-binomial-identity](pages/convex-castle-binomial-identity.md)] - the binomial count of the convex castles.
- [[castle-perimeter](pages/castle-perimeter.md)] - the castles counted by semi-perimeter and width, A271942, which are the numbers `T̂(L, b)` re-indexed.
- [[tower-narayana-polynomial](pages/tower-narayana-polynomial.md)] - the generating function of towers counted by blocks, and its rows in the OEIS.
- [[oeis-mining-pe502](pages/oeis-mining-pe502.md)] - the castle counts matched to OEIS entries, the tower block-count rows among them.

## Footnotes

[^1]: https://oeis.org/A001263 (read 2026-10-16) - "Triangle of Narayana numbers T(n,k) = C(n-1,k-1)*C(n,k-1)/k with 1 <= k <= n, read by rows. Also called the Catalan triangle."
[^2]: [[algebraic-languages-and-polyominoes-enumeration](pages/algebraic-languages-and-polyominoes-enumeration.md)] p.184 Remark 4.4 - "the number b_{n,k} of parallelogram polyominoes with perimeter 2n+2 and width k is given by the 2 × 2 determinant ... This determinant is equal to (1/n)C(n,k)C(n,k-1) and using Proposition 4.1, we deduce the well-known formula for the number of Dyck words of length 2n having k peaks."
[^3]: Verified by execution (Python 3.11, 2026-10-16): Dyck paths of semilength `n` by peaks and parallelogram polyominoes of semi-perimeter `n + 1` by width against `N(n, k)` for `n ≤ 7`; `T̂(L, b)` and its refinement by descents against enumeration of all towers for `L ≤ 6`, `b ≤ 7` and `L = 7`, `b ≤ 6`.
[^4]: Verified by execution (Python 3.11 with SymPy, 2026-10-25): with `x` marking width and `y` blocks, the coefficients of `x^L` in the power-series root of the tower grammar's fixed-point equation `xyE² − (1 − x)(1 − y)E + (1 − y) = 0` equal `Narayana_L(y)/(1 − y)^L` for `L ≤ 10`.
[^5]: [[cho-huh-nam-sohn-2022-bounded-free-motzkin-paths](pages/cho-huh-nam-sohn-2022-bounded-free-motzkin-paths.md)] p.14 Proposition 3.4 and proof L785-801 - "The number of t-core partitions with m corners is given by cc(t, m) := Σ_{i=1}^{min(m,⌊t/2⌋)} N(m, i) C(t + 2m − 2i, 2m)", with "we have to insert at least one flat steps at the positions of i peaks and i − 1 valleys"; the cores with `m` corners are the towers on a base of length `t − 1` with `m` blocks by its Theorem 3.3, so `t = L + 1` and `m = b`.
[^6]: Verified by execution (Python 3.10, 2026-10-17): `bin/python/bounded_t_cores.py`, run log `bin/python/bounded_t_cores-run.log`; the sum and its terms against enumeration of all towers for `L ≤ 6`, `b ≤ 7` and `L = 7`, `b ≤ 6`.
