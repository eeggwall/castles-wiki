---
title: "Counting Horizontally Convex Polyominoes (Hickerson 1999)"
category: Sources
summary: Hickerson's proof that the number a(n) of horizontally convex n-ominoes (A001169) satisfies a(n) = 5a(n−1) − 7a(n−2) + 4a(n−3) for n ≥ 5, with a(n) ~ u v^n, v = 3.2055694304 the real root of v³ − 5v² + 7v − 4. Earlier proofs work with a(r, n), the polyominoes with r squares in the top row, and the weight r + s − 1 of (0.6); this proof uses four one-variable counts b, c, d, e of restricted polyominoes, related by adding and deleting single squares (Lemmas 0-4).
tags: [paper, polyomino, horizontally-convex, linear-recurrence, combinatorics, source]
sources: [counting-horizontally-convex-polyominoes]
created: 2026-09-13
updated: 2026-10-16
---

# Counting Horizontally Convex Polyominoes (Hickerson 1999)

**Source:** Dean Hickerson, *Counting Horizontally Convex Polyominoes*, Journal of Integer Sequences, Vol. 2 (1999), Article 99.1.8, https://cs.uwaterloo.ca/journals/JIS/HICK2/chcp.html (read 2026-10-16). The local copy `assets/PolyominoTransferMatrix.pdf` is not in every clone.
**Date ingested:** 2026-09-13
**Type:** paper (6 pp.)

## Summary

A **polyomino** is a finite union of closed unit squares with integer vertices whose interior is connected; an *n*-omino has area *n*, and polyominoes are counted up to translation. A polyomino is **horizontally convex** if every horizontal line meets it in a single segment or not at all.[^1] Let `a(n)` be the number of horizontally convex *n*-ominoes: `1, 2, 6, 19, 61, 196, 629, 2017, 6466, 20727, 66441, 212980, …` (A001169).[^2]

**Theorem.** For `n ≥ 5`,[^2]

```
a(n)  =  5 a(n−1) − 7 a(n−2) + 4 a(n−3).                                     (0.0)
```

From this, `a(n) ~ u v^n`, where `v = 3.2055694304…` is the unique real root of `v³ − 5v² + 7v − 4 = 0` and `u = (163 − 129v + 41v²)/944 = 0.1809155018…`.[^3]

Hickerson writes that (0.0) was apparently first proved by Pólya in 1938, whose proof seems not to have been published. The published proofs work with `a(r, n)`, the number of horizontally convex *n*-ominoes with exactly `r` squares in the top row, and[^4]

```
a(r, n)  =  Σ_{s=1}^{n−r} (r + s − 1) a(s, n − r),        1 ≤ r < n,              (0.6)
```

"since we may add a row of r squares to the top of a polyomino counted by a(s, n−r) in exactly r+s−1 ways". They derive (0.0) from (0.6) directly or through generating functions.

**The proof.** Hickerson introduces four counts of restricted horizontally convex *n*-ominoes:[^5]

- `b(n)`: the top row has exactly one square;
- `c(n)`: the top row has at least two squares, and its rightmost square is directly above the leftmost square of the second row;
- `d(n)`: the top row has exactly one square, not above the rightmost square of the second row;
- `e(n)`: as `d(n)`, and the rightmost square of the second row is above the leftmost square of the third row.

Adding or deleting one square gives five relations (Lemmas 0-4):[^5]

```
a(n) = a(n−1) + b(n) + c(n)         (n ≥ 2)        c(n) = c(n−1) + a(n−2)    (n ≥ 3)
b(n) = a(n−1) + d(n)                (n ≥ 2)        d(n) = b(n−1) + e(n)      (n ≥ 3)
e(n) = e(n−1) + c(n−1)              (n ≥ 2)
```

For Lemma 0, adding a square at the right end of the top row of a horizontally convex `(n−1)`-omino gives, exactly once each, the *n*-ominoes whose top row has at least two squares and whose rightmost top square is not above the leftmost square of the second row. Eliminating the four counts gives in turn `a(n) − 3a(n−1) = e(n)` for `n ≥ 3`, `a(n) − 4a(n−1) + 3a(n−2) = c(n−1)` for `n ≥ 4`, and (0.0) for `n ≥ 5`.[^5] Each of the four counts is a linear combination of `a(n), a(n−1), a(n−2)`, so each satisfies (0.0) for large `n`:[^6]

```
b(n) = 3a(n−1) − 4a(n−2)      c(n) = a(n) − 4a(n−1) + 4a(n−2)      d(n) = 2a(n−1) − 4a(n−2)      (n ≥ 4)
e(n) = a(n) − 3a(n−1)                                                                         (n ≥ 3)
```

The counts are A049219, A049220, A049221 and A049222.[^6]

## Key Takeaways

- Every value of the paper's table (`a` through `e` for `n ≤ 10`) agrees with brute-force enumeration of horizontally convex polyominoes, and so do (0.0) for `5 ≤ n ≤ 10` and the four linear combinations for `4 ≤ n ≤ 10`. (0.0) also holds on the paper's `a(1), …, a(12)`, and `v` and `u` agree with the root of (0.3) to the printed digits.[^7]
- The generating function of `a(n)` is `z(1 − z)³/(1 − 5z + 7z² − 4z³)`, whose expansion is the table ([[castle-add-a-column-equation](pages/castle-add-a-column-equation.md)]).[^7]
- A horizontally convex polyomino turned a quarter turn is column-convex, so A001169 also counts column-convex polyominoes by area ([[horizontally-convex-polyomino](pages/horizontally-convex-polyomino.md)], [[column-convex-polyomino](pages/column-convex-polyomino.md)]).

## Entities & Concepts

- [[horizontally-convex-polyomino](pages/horizontally-convex-polyomino.md)] - the counted object, and the castles among the horizontally convex polyominoes.
- [[castle-add-a-column-equation](pages/castle-add-a-column-equation.md)] - the weight `r + s − 1` of (0.6) as a column kernel of rank 2, against the castle kernel `1` of rank 1.
- [[column-convex-polygon-enumeration](pages/column-convex-polygon-enumeration.md)] - the add-a-column method, which counts column-convex polygons by area and perimeter.
- [[convex-polyomino](pages/convex-polyomino.md)] - the polyominoes convex in both directions.

## Relation to Other Wiki Pages

[[project-euler-502-solution](pages/project-euler-502-solution.md)] lists this paper among its references, under the file name `PolyominoTransferMatrix.pdf`.

## Footnotes

[^1]: https://cs.uwaterloo.ca/journals/JIS/HICK2/chcp.html §0 - "A finite union of closed unit squares whose vertices have integer coordinates is called a polyomino if its interior is connected. A polyomino of area n is called an n-omino. We will consider two polyominoes to be the same if one is a translate of the other. A polyomino P is horizontally convex if each horizontal line meets P in a single line segment, or not at all."
[^2]: https://cs.uwaterloo.ca/journals/JIS/HICK2/chcp.html §0 - the table "a(n) 1 2 6 19 61 196 629 2017 6466 20727 66441 212980" and "Theorem: For n ≥ 5, a(n) = 5 a(n-1) - 7 a(n-2) + 4 a(n-3). (0.0)"; https://oeis.org/A001169.
[^3]: https://cs.uwaterloo.ca/journals/JIS/HICK2/chcp.html §0 (0.1)-(0.4) - "v = 3.2055694304... is the unique real root of v^3 - 5 v^2 + 7 v - 4 = 0", "u = (163 - 129 v + 41 v^2)/944 = 0.1809155018...".
[^4]: https://cs.uwaterloo.ca/journals/JIS/HICK2/chcp.html §0 (0.5)-(0.6) - "The recurrence (0.0) was apparently first proved by Pólya in 1938, although his proof does not seem to have been published", "they introduce the function a(r,n), which is the number of horizontally convex n-ominoes with exactly r squares in the top row", "a(r,n) = SUM (r+s-1) a(s,n-r) for 1 ≤ r < n, since we may add a row of r squares to the top of a polyomino counted by a(s,n-r) in exactly r+s-1 ways", with the proofs [K0], [K1], [S0], [S1], [T].
[^5]: https://cs.uwaterloo.ca/journals/JIS/HICK2/chcp.html §1 [synthesis] - the definitions of b(n), c(n), d(n), e(n); Lemmas 0-4, (1.0)-(1.5), with their add-a-square and delete-a-square proofs; the combination "a(n) - 3 a(n-1) = e(n) for n ≥ 3", "a(n) - 4 a(n-1) + 3 a(n-2) = c(n-1)", and "a(n) - 5 a(n-1) + 7 a(n-2) - 3 a(n-3) = c(n-1) - c(n-2) = a(n-3)".
[^6]: https://cs.uwaterloo.ca/journals/JIS/HICK2/chcp.html §2 (2.0)-(2.3) - "b(n) = 3 a(n-1) - 4 a(n-2) for n ≥ 4", "c(n) = a(n) - 4 a(n-1) + 4 a(n-2) for n ≥ 4", "d(n) = 2 a(n-1) - 4 a(n-2) for n ≥ 4", "e(n) = a(n) - 3 a(n-1) for n ≥ 3", and the table of a(n) to e(n) for n ≤ 10 with A049219-A049222.
[^7]: Verified by execution (Python 3.11, 2026-10-16): all horizontally convex polyominoes of area at most 10 enumerated as stacks of overlapping row segments; `a, b, c, d, e` equal the paper's table for `n ≤ 10`; (0.0) holds for `5 ≤ n ≤ 10` and on the table to `n = 12`; (2.0)-(2.3) hold for `4 ≤ n ≤ 10`; the real root of `v³ − 5v² + 7v − 4` is `3.2055694304006` and `u = 0.1809155019`; `z(1 − z)³/(1 − 5z + 7z² − 4z³) = z + 2z² + 6z³ + 19z⁴ + 61z⁵ + 196z⁶ + 629z⁷ + 2017z⁸ + 6466z⁹ + …`.
