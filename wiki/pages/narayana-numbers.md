---
title: Narayana numbers
category: Concepts
summary: The Narayana numbers N(n, k) = (1/n) C(n, k) C(n, k−1) (OEIS A001263) count the Dyck paths of semilength n with k peaks and the parallelogram polyominoes of semi-perimeter n + 1 and width k, and sum over k to the Catalan number C_n. On the castle side they are the numerator of the generating function of towers counted by blocks, Σ_b T̂(L, b) x^b = Σ_k N(L, k) x^{k−1} / (1 − x)^L.
tags: [concept, narayana, catalan, oeis, tower, generating-functions]
sources: [oeis-mining-pe502, tower-narayana-polynomial, algebraic-languages-and-polyominoes-enumeration]
created: 2026-09-13
updated: 2026-10-16
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

This agrees with enumeration for `L ≤ 6`, `b ≤ 7`, and for `L = 7`, `b ≤ 6`; it is not proved on the wiki.[^3] The `k`-th term counts the towers whose column heights have `k − 1` descents (computed over the same range). At `L = 2`, `T̂(2, b) = C(b + 1, 1) + C(b, 1) = 2b + 1`: of the `2b + 1` towers `(c_1, c_2)` with `max(c_1, c_2) = b`, the `b + 1` with `c_1 ≤ c_2` have no descent and the `b` with `c_1 > c_2` have one. [[tower-heap](pages/tower-heap.md)] treats these counts, and [[tower-narayana-polynomial](pages/tower-narayana-polynomial.md)] records the source and the OEIS rows.

The convex castles are counted by a binomial coefficient, not by Narayana numbers ([[convex-castle-binomial-identity](pages/convex-castle-binomial-identity.md)]).

## Appearances in Sources

- [[tower-narayana-polynomial](pages/tower-narayana-polynomial.md)] - the generating function of towers counted by blocks, and its rows in the OEIS.
- [[oeis-mining-pe502](pages/oeis-mining-pe502.md)] - the mining pass in which the identity was found.
- [[algebraic-languages-and-polyominoes-enumeration](pages/algebraic-languages-and-polyominoes-enumeration.md)] - Remark 4.4: parallelogram polyominoes by width are counted by `N(n, k)`, and β carries this to Dyck paths by peaks.
- [[baril-florez-ramirez-2026-generalized-narayana-arrays](pages/baril-florez-ramirez-2026-generalized-narayana-arrays.md)] - `N(n, k)` refined by the heights of the `k` peaks (type-1 and type-2 Narayana arrays).

## Related Concepts

- [[tower-heap](pages/tower-heap.md)] - towers counted by blocks, with the refinement by descents.
- [[catalan-numbers](pages/catalan-numbers.md)] - the row sums `Σ_k N(n, k) = C_n`.
- [[parallelogram-polyomino-dyck-bijection](pages/parallelogram-polyomino-dyck-bijection.md)] - Delest-Viennot's β, under which the width of a parallelogram polyomino is the number of peaks of a Dyck path.
- [[convex-castle-binomial-identity](pages/convex-castle-binomial-identity.md)] - the binomial count of the convex castles.
- [[castle-perimeter](pages/castle-perimeter.md)] - the castles counted by semi-perimeter and width, A271942, which are the numbers `T̂(L, b)` re-indexed.

## Footnotes

[^1]: https://oeis.org/A001263 (read 2026-10-16) - "Triangle of Narayana numbers T(n,k) = C(n-1,k-1)*C(n,k-1)/k with 1 <= k <= n, read by rows. Also called the Catalan triangle."
[^2]: [[algebraic-languages-and-polyominoes-enumeration](pages/algebraic-languages-and-polyominoes-enumeration.md)] p.184 Remark 4.4 - "the number b_{n,k} of parallelogram polyominoes with perimeter 2n+2 and width k is given by the 2 × 2 determinant ... This determinant is equal to (1/n)C(n,k)C(n,k-1) and using Proposition 4.1, we deduce the well-known formula for the number of Dyck words of length 2n having k peaks."
[^3]: Verified by execution (Python 3.11, 2026-10-16): Dyck paths of semilength `n` by peaks and parallelogram polyominoes of semi-perimeter `n + 1` by width against `N(n, k)` for `n ≤ 7`; `T̂(L, b)` and its refinement by descents against enumeration of all towers for `L ≤ 6`, `b ≤ 7` and `L = 7`, `b ≤ 6`.
[^4]: `raw/oeis-pe502/crosslink-avenues.md` §"Tier 2" L41-47 - "T(w,b) = # towers of width w with exactly b blocks = sum_{k=1..w} Narayana(w,k) * C(b + w − k, w − 1) (Narayana-polynomial g.f.) g.f. = (Narayana_w(x)) / (1 − x)^w, Narayana_w(x) = sum_k Narayana(w,k) x^{k−1}", "Narayana(w,k) = (1/w) C(w,k) C(w,k−1) = A001263".
