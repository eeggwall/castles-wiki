---
title: Catalan numbers
category: Concepts
summary: The Catalan numbers C_n = C(2n, n)/(n + 1) (A000108; 1, 1, 2, 5, 14, 42, …) count the Dyck words of length 2n, the plane trees with n + 1 nodes and the triangulations of a convex (n + 2)-gon, with generating function c(x) = (1 − √(1 − 4x))/(2x). On the castle wiki, the Narayana numbers N(n, k) refine them, the parallelogram polyominoes by area grade them, and the first-return decomposition of Dyck words is the template of the tower grammar.
tags: [concept, catalan, dyck, narayana, generating-functions, combinatorics, symbolic-method]
sources: [analytic-combinatorics-ch1-ogfs, barry-2005-catalan-transform]
created: 2026-09-13
updated: 2026-10-25
---

# Catalan numbers

## Definition

The **Catalan numbers** are the sequence `A000108`,[^1][^2]

```
C_n  =  C(2n, n)/(n + 1)  =  C(2n, n) − C(2n, n + 1),        n ≥ 0,
     =  1, 1, 2, 5, 14, 42, 132, 429, 1430, 4862, 16796, …
```

The second form shows that `C_n` is an integer. They satisfy the convolution and ratio recurrences[^3]

```
C_0 = 1,        C_{n+1}  =  Σ_{i=0}^{n} C_i C_{n−i},        C_n  =  2(2n − 1)/(n + 1) · C_{n−1},
```

and their generating function `c(x) = Σ_n C_n x^n` is the root of `c = 1 + x c²` that is finite at `x = 0`:

```
c(x)  =  (1 − √(1 − 4x)) / (2x).
```

As `n → ∞`, `C_n ~ 4^n/(n^{3/2} √π)`; at `n = 2000` the ratio of the two sides is `0.99944`.[^3][^4]

`C_n` counts the Dyck words of length `2n`, the balanced parenthesizations with `n` pairs, the full binary trees with `n + 1` leaves, the non-crossing partitions of `{1, …, n}`, the lattice paths in an `n × n` grid that do not pass above the diagonal, the triangulations of a convex `(n + 2)`-gon, and the 123-avoiding permutations of `{1, …, n}`.[^5] At `n = 3` the five Dyck words, in the letters `U` (up) and `D` (down), are `UUUDDD`, `UUDUDD`, `UUDDUD`, `UDUUDD` and `UDUDUD` ([[dyck-words](pages/dyck-words.md)]).

## Specifications

A plane tree is a root node with a possibly empty sequence of subtrees, so the class `G` of plane trees, counted by nodes, satisfies `G = Z × SEQ(G)`, with `Z` the class of one node ([[symbolic-method](pages/symbolic-method.md)]). Its generating function satisfies `G(z) = z/(1 − G(z))`, that is `G² − G + z = 0`, so[^6]

```
G(z)  =  (1 − √(1 − 4z)) / 2  =  z + z² + 2z³ + 5z⁴ + 14z⁵ + 42z⁶ + ⋯,
```

and the plane trees with `n` nodes number `C_{n−1}`. Flajolet and Sedgewick note that for this reason "the term Catalan tree is often employed as synonymous to 'general (rooted unlabelled plane) tree'".[^6] A triangulation of a convex polygon splits into a root triangle and two triangulations, one on each side, so the class `T` of triangulations, counted by triangles, satisfies `T = {ε} + T × ∇ × T` with `∇` the root triangle, and `T(z) = 1 + z T(z)²`, which is the equation of `c(x)`.[^7]

A nonempty Dyck word factors uniquely as `U w_1 D w_2`, where `w_1` and `w_2` are Dyck words and `U w_1 D` is the part before the word first returns to height 0. This first-return decomposition gives `c = 1 + x c²` once more. With a third letter `R`, one per column, as a case of its own, the same decomposition is the first-return decomposition of Motzkin paths, and the tower grammar of castles is that decomposition with one cut for each excluded factor, `UD` and `DU` ([[generalized-dyck-grammar](pages/generalized-dyck-grammar.md)]).

## Castle appearances

- **Narayana numbers.** `N(n, k) = C(n, k) C(n, k − 1)/n` (`A001263`) counts the Dyck words of semilength `n` with `k` peaks, and `Σ_k N(n, k) = C_n` ([[narayana-numbers](pages/narayana-numbers.md)]). The towers of any height on a base of length `L`, counted by blocks, have generating function `Σ_k N(L, k) x^{k−1}/(1 − x)^L`, whose numerator is `C_L` at `x = 1` ([[tower-heap](pages/tower-heap.md)], [[tower-narayana-polynomial](pages/tower-narayana-polynomial.md)]).
- **Parallelogram polyominoes.** The parallelogram polyominoes of semi-perimeter `n + 1` number `C_n`, and counted by area they give the Pólya-Gessel `q`-Catalan numbers ([[q-catalan-numbers](pages/q-catalan-numbers.md)]). The castles counted by width, blocks and area are `Π/(1 − x − Π)`, with `Π` the generating function of the parallelogram polyominoes ([[castle-q-bessel-closed-form](pages/castle-q-bessel-closed-form.md)]).
- **Convex castles** are counted by the binomial coefficient `C(2h + w − 3, w − 1)` ([[convex-castle-binomial-identity](pages/convex-castle-binomial-identity.md)]).

## Appearances in Sources

- `raw/catalan-numbers-wikipedia.md`, a cached extract of Wikipedia, *Catalan number* - the closed forms, the recurrences, the generating function, the asymptotics and the interpretations.
- [[analytic-combinatorics-ch1-ogfs](pages/analytic-combinatorics-ch1-ogfs.md)] - the plane trees `G = Z × SEQ(G)` (§I.2.3, pp. 34-35), the triangulations `T = {ε} + T × ∇ × T` (pp. 35-36), and Figure I.2 (p. 20), "The prehistory of Catalan numbers", from Euler's letter of 1751 to Segner and Lamé.
- [[barry-2005-catalan-transform](pages/barry-2005-catalan-transform.md)] - the Catalan transform `A(x) → A(x c(x))`, the Riordan array `(1, x c(x))`, whose row sums are the `C_n`; the ballot numbers `(2k + 1)/(n + k + 1) · C(2n, n + k)` (`A039599`); and `M_n = Σ_k C(n, 2k) C_k`.

## Related Concepts

- [[narayana-numbers](pages/narayana-numbers.md)] - `N(n, k)`, the Dyck words of semilength `n` with `k` peaks, which sum to `C_n`.
- [[q-catalan-numbers](pages/q-catalan-numbers.md)] - the `q`-analogs of `C_n`, one of which counts the parallelogram polyominoes by area.
- [[dyck-words](pages/dyck-words.md)] - the Dyck words and their first-return decomposition.
- [[motzkin-numbers](pages/motzkin-numbers.md)] - the Motzkin numbers `M_n = Σ_k C(n, 2k) C_k`, the Dyck paths with flat steps inserted.
- [[binomial-transform](pages/binomial-transform.md)] - the aerated binomial transform that takes `C_k` to `M_n`; for the castles whose neighboring columns differ by at most 1 and whose end columns have height 1, it gives their count `M_{w−1}`.
- [[marin-2024-polyominoes-in-rectangle](pages/marin-2024-polyominoes-in-rectangle.md)] - `C_m` counts the non-crossing ways to group a row's `m` runs of cells into connected components, a factor of Marin's state count for the polyominoes in a rectangle.
- [[deutsch-elizalde-2017-bargraphs-dyck-paths](pages/deutsch-elizalde-2017-bargraphs-dyck-paths.md)] - the castles whose semi-perimeter minus number of peaks, in Deutsch and Elizalde's sense of peak, is `m` number `C_m`, through a map from Dyck paths.
- [[convex-castle-binomial-identity](pages/convex-castle-binomial-identity.md)] - the convex castle count `C(2h + w − 3, w − 1)` as a Vandermonde convolution.
- [[symbolic-method](pages/symbolic-method.md)] - the translation of `G = Z × SEQ(G)` into `G(z) = z/(1 − G(z))`.

## Footnotes

[^1]: raw/catalan-numbers-wikipedia.md §"Definition and closed forms", §"First values (n = 0..10)" L6-11 - "C_n = (1/(n+1)) * binomial(2n, n) = (2n)! / ((n+1)! * n!)", "C_n = binomial(2n, n) - binomial(2n, n+1) (shows integrality)", "1, 1, 2, 5, 14, 42, 132, 429, 1430, 4862, 16796". (Source: https://en.wikipedia.org/wiki/Catalan_number)
[^2]: https://oeis.org/A000108 (read 2026-10-16) - "Catalan numbers: C(n) = binomial(2n,n)/(n+1) = (2n)!/(n!(n+1)!)."
[^3]: raw/catalan-numbers-wikipedia.md §"Recurrences", §"Generating function", §"Asymptotics" L13-21 - "Convolution: C_0 = 1, C_{n+1} = sum_{i=0..n} C_i * C_{n-i}", "Ratio: C_0 = 1, C_n = (2(2n-1)/(n+1)) * C_{n-1}", "c(x) = sum_n C_n x^n satisfies c(x) = 1 + x*c(x)^2, so c(x) = (1 - sqrt(1-4x)) / (2x)", "C_n ~ 4^n / (n^(3/2) * sqrt(pi)) as n -> infinity".
[^4]: Verified by execution (Python 3.11 with SymPy, 2026-10-16): both closed forms for `n < 40`; the two recurrences for `n < 24`; the series of `c(x)` and of `G(z)` to twelve and nine terms; `C_2000` against the asymptotic (ratio `0.99944`); the Dyck words for `n ≤ 7` and the triangulations for `n ≤ 8` by enumeration; `Σ_k N(n, k) = C_n` for `n < 15`.
[^5]: raw/catalan-numbers-wikipedia.md §"Canonical interpretations (a selection)" L23-30 - "Dyck words of length 2n", "Balanced parentheses with n pairs", "Full binary trees with n+1 leaves", "Non-crossing partitions of {1..n}", "Monotonic lattice paths in an n x n grid not passing above the diagonal", "Triangulations of a convex (n+2)-gon", "Stack-sortable / 123-avoiding permutations of {1..n}".
[^6]: [[analytic-combinatorics-ch1-ogfs](pages/analytic-combinatorics-ch1-ogfs.md)] §I.2.3 pp.34-35 - "The recursive specification of general trees leads to an implicit definition of their OGF, G = Z × SEQ(G) ⟹ G(z) = z/(1−G(z))", "G − G² − z = 0", "G(z) = ½(1 − √(1−4z))", "For this reason the term Catalan tree is often employed as synonymous to 'general (rooted unlabelled plane) tree'."
[^7]: [[analytic-combinatorics-ch1-ogfs](pages/analytic-combinatorics-ch1-ogfs.md)] §I.2.3 pp.35-36 - "a triangulation decomposes into its root triangle and two subtriangulations (that may well be 'empty') appearing on the left and right sides of the root triangle", "The class T of all triangulations can be specified recursively as T = {ε} + (T × ∇ × T)", "the OGF T(z) satisfies the equation T(z) = 1 + zT(z)^2" (31).
