---
title: Castles of height h by area - the n-nacci family
category: Analyses
summary: The castles of height h and area n are the compositions of n with largest part h, so they number the compositions of n into parts at most h minus those into parts at most h − 1, with generating function 1/(1 − x − ⋯ − x^h) − 1/(1 − x − ⋯ − x^{h−1}). They grow like the h-nacci constant, the real root above 1 of x^h = x^{h−1} + ⋯ + x + 1 - golden by area at h = 2 (F_{n+1} − 1 castles), tribonacci 1.8393 at h = 3 (A000073(n+2) − F_{n+1}), 1.9276 at h = 4, 1.9659 at h = 5 - tending to 2, the growth of all castles by area. The tree castles of height h grow more slowly by area (1.4656, φ, 1.6851 at h = 2, 3, 4, and ψ² with the height unrestricted). Writing each column of height c as a run of c − 1 1s, with single 0s between columns, sends the castles of area n and height h onto the binary strings of length n − 1 whose longest run of 1s has length h − 1, the entry T(n − 1, h − 1) of A048004; the rows h = 3, 4, 5, 6 are A000100, A000102, A006979 and A006980.
tags: [analysis, castle, area, generating-function, oeis, fibonacci, tribonacci, tetranacci, n-nacci, composition, growth-constant]
sources: [oeis-encyclopedia, balado-silvestre-2026-runs-binary-strings]
created: 2026-09-17
updated: 2026-10-27
---

# Castles of height `h` by area

## The count

A castle of height `h` is a skyline `(c_1, …, c_w)` with `1 ≤ c_i ≤ h` and some `c_i = h` ([[castle-polyomino](pages/castle-polyomino.md)]), and its area is `n = c_1 + ⋯ + c_w`. So a castle of area `n` is a composition of `n`, every composition of `n` is a castle, and the castles of area `n` number `2^{n−1}` ([[castle-by-area](pages/castle-by-area.md)]).[^1] The castles of height `h` and area `n` are the compositions of `n` with largest part `h`. The compositions with every part in `{1, …, h}` satisfy the `h`-nacci recurrence `a(n) = a(n−1) + ⋯ + a(n−h)`, since the last part is one of `1, …, h`. So

```
#{castles of height h and area n}
    =  #{compositions of n into parts {1, …, h}}  −  #{compositions of n into parts {1, …, h − 1}},       (1)
```

with ordinary generating function[^2]

```
Σ_n (count) x^n  =  1 / (1 − x − ⋯ − x^h)  −  1 / (1 − x − ⋯ − x^{h−1}).                               (2)
```

*Example.* The castles of height 2 and area 4 are the skylines `(2, 1, 1)`, `(1, 2, 1)`, `(1, 1, 2)` and `(2, 2)`: the five compositions of 4 into parts 1 and 2, less `(1, 1, 1, 1)`.

The first term of Equation (2) has the larger dominant root, so the count grows like the `h`-nacci constant, the real root above 1 of `x^h = x^{h−1} + ⋯ + x + 1`, which lies in `(1, 2)`.

## The table

| `h` | castles of height `h` and area `n`, `n = 1..12` | closed form | growth constant |
|---|---|---|---|
| 2 | `0, 1, 2, 4, 7, 12, 20, 33, 54, 88, 143, 232` | `F_{n+1} − 1` (A000045) | `φ = 1.6180` |
| 3 | `0, 0, 1, 2, 5, 11, 23, 47, 94, 185, 360, 694` | `A000073(n+2) − F_{n+1}` | `τ = 1.8393`, the root of `x³ = x² + x + 1` |
| 4 | `0, 0, 0, 1, 2, 5, 12, 27, 59, 127, 269, 563` | `A000078(n+3) − A000073(n+2)` | `1.9276`, the root of `x⁴ = x³ + x² + x + 1` |
| 5 | `0, 0, 0, 0, 1, 2, 5, 12, 28, 63, 139, 303` | `A001591(n+4) − A000078(n+3)` | `1.9659` |
| unrestricted | `1, 2, 4, 8, 16, 32, 64, …` | `2^{n−1}` (A011782) | `2` |

Every entry agrees with enumeration of the compositions for `n ≤ 14`.[^2] The closed forms use the OEIS offsets: A000073 has generating function `x²/(1 − x − x² − x³)`, so the compositions of `n` into parts `{1, 2, 3}` number `A000073(n+2)`; A000078 has `x³/(1 − x − x² − x³ − x⁴)`, giving `A000078(n+3)`; and A001591 gives `A001591(n+4)` for parts up to 5.[^3] The `h`-nacci constants increase from `φ` toward `2` (`1.9836` at `h = 6`, `1.9920` at `h = 7`).

## The run reading

Write each column of height `c` as a run of `c − 1` 1s and put a single 0 between neighboring columns. This sends a castle `(c_1, …, c_w)` of area `n` to the binary string `1^{c_1−1} 0 1^{c_2−1} 0 ⋯ 0 1^{c_w−1}` of length `n − 1`, and every binary string of length `n − 1` comes from exactly one castle of area `n`: the 0s cut it back into runs. It is the map of [[a005251-bijection](pages/a005251-bijection.md)] with 0s and 1s exchanged. A column of height 1 becomes a run of length 0, a null run in the terms of [[balado-silvestre-2026-runs-binary-strings](pages/balado-silvestre-2026-runs-binary-strings.md)], and the height of the castle is one more than the longest run of its string. *Example.* `(2, 1, 1, 3)`, of area 7 and height 3, becomes `1 0 0 0 11`, a string of length 6 whose longest run has length 2.[^7]

So the castles of area `n` and height `h` are the binary strings of length `n − 1` whose longest run of 1s has length `h − 1`, the entry `T(n − 1, h − 1)` of the triangle A048004, "number of binary vectors of length n whose longest run of consecutive 1's has length k". The rows of the table above are its columns: `h = 2` is `F_{n+1} − 1`, and `h = 3, 4, 5, 6` are `A000100(n)`, `A000102(n)`, `A006979(n)` and `A006980(n)`, the compositions of `n` whose largest part is 3, 4, 5 and 6.[^5][^6] Balado and Silvestre's Remark 30 states the general form: the compositions of `n` with exactly `m` parts in `[a, b]` correspond to the strings of length `n − 1` with exactly `m` runs of 1s of length in `[a − 1, b − 1]`, null runs included (their eq. (273)). Since `1/(1 − x − ⋯ − x^h) = (1 − x)/(1 − 2x + x^{h+1})`, Equation (2) is

```
x^h (1 − x)² / ((1 − 2x + x^h)(1 − 2x + x^{h+1})),
```

Riordan's generating function for the compositions with largest part `h`, their eq. (275), and the castles of height at most `h` by area have Riordan's `(x − x^{h+1})/(1 − 2x + x^{h+1})`, eq. (274).[^5][^7]

## Tree castles of height h by area

A **tree castle** has no `2 × 2` block of cells: no two adjacent columns both have height at least 2 ([[castle-graph](pages/castle-graph.md)], [[tree-castle-by-area](pages/tree-castle-by-area.md)]). The tree castles of height `h` grow more slowly by area:[^2]

| `h` | castles of height `h` | tree castles of height `h` |
|---|---|---|
| 2 | `φ = 1.6180` | `1.4656`, the root of `x³ = x² + 1`; the count is `A000930(n+1) − 1` |
| 3 | `τ = 1.8393` | `φ`; the denominator of A006498 has the factor `1 − q − q²` |
| 4 | `1.9276` | `1.6851`, the root of `x⁵ = x⁴ + x² + x + 1` (A000570) |
| unrestricted | `2` | `ψ² = 1.7549`, the root of `x³ − 2x² + x − 1`, with `ψ` the plastic number (A005251) |

The OEIS sequences in the right column count the tree skylines of height at most `h`, which need not reach `h` and so need not be castles of height `h`. The tree castles of height `h` are the difference of consecutive rows, and since the growth constants increase with `h` they have the same growth constant as the row for `h`. At each `h = 2, 3, 4`, the castles and the tree castles of height `h` agree in number through area `h + 1` and differ from area `h + 2` on, where the composition `(h, 2)` is the first with two adjacent parts at least 2.[^2]

The tree skylines of height at most `h` have area generating function `(1 + P_h(q))/(1 − q − q P_h(q))` with `P_h(q) = q² + ⋯ + q^h` ([[tree-castle-by-area](pages/tree-castle-by-area.md)]), and its denominator `1 − q − q³ − ⋯ − q^{h+1}` has no `q²` term: except at the end, a column of height `j ≥ 2` is followed by a column of height 1, and the denominator counts the sequences of single columns of height 1 (the term `q`) and of such pairs, each of area `j + 1 ≥ 3` (the term `q P_h(q)`). The compositions into parts at most `h` have the denominator `1 − x − x² − ⋯ − x^h`, with the `x²` term.

## Fibonacci and tribonacci

- **Height 2.** The castles of height 2 and area `n` are the compositions of `n` into parts 1 and 2 with at least one 2, `F_{n+1} − 1` of them. They grow like `(φ/√5)·φ^n ≈ 0.7236·φ^n`, so they are golden by area, although by width they number `2^w − 1`.[^4] The same numbers count the Fibonacci castles of width `n − 1` ([[fibonacci-castle](pages/fibonacci-castle.md)]): append a column of height 1 to a Fibonacci castle of width `n − 1`, read each column of height 2 together with the column after it, which has height 1, as a part 2, and each other column as a part 1. This gives every composition of `n` into parts 1 and 2 with at least one 2, exactly once. The prime castles of area `n`, the compositions into parts at least 2, are a different Fibonacci count, `F_{n−1}` ([[prime-castles](pages/prime-castles.md)]).
- **Height 3.** The castles of height 3 and area `n` number `A000073(n+2) − F_{n+1}` and grow like `τ = 1.8393`. Three cubic constants occur as growth by area of these families: `1.4656` for the tree castles of height 2 (the Fibonacci castles counted by area, [[q-fibonacci-castle](pages/q-fibonacci-castle.md)]), `τ` for the castles of height 3, and `ψ²` for the tree castles with the height unrestricted ([[plastic-number](pages/plastic-number.md)]).

## The metallic means

For `3 ≤ h ≤ 20` the polynomial `x^h − x^{h−1} − ⋯ − x − 1` is irreducible over the rationals (computed), so the `h`-nacci constant has degree `h ≥ 3` and is not one of de Spinadel's metallic means `σ_p^q`, which are quadratic ([[metallic-means](pages/metallic-means.md)]).[^2] At `h = 2` the growth is the golden mean `φ = σ_1^1`. Among the tree castles by area, those of height 3 are golden by area, and the constants at `h = 2` and `h = 4` have degrees 3 and 5.

## Reproduce

The snippet `bounded_castles_by_area(h, A_max)` on [[castle-snippets-strips](pages/castle-snippets-strips.md)] counts the compositions of each area with parts at most `h`, with a brute-force cross-check against skylines. The counts of castles of height `h` are `bounded_castles_by_area(h, ·)` minus `bounded_castles_by_area(h − 1, ·)`.

## Related Concepts

- [[oeis-mining-pe502](pages/oeis-mining-pe502.md)] - the castles of area `n` as the `2^{n−1}` compositions of `n`, among the first OEIS matches.
- [[n-nacci-disambiguation](pages/n-nacci-disambiguation.md)] - the Fibonacci, tribonacci and higher n-nacci appearances on the wiki, grouped by the mechanism that produces them.
- [[balado-silvestre-2026-runs-binary-strings](pages/balado-silvestre-2026-runs-binary-strings.md)] - binary strings by their runs of 1s; through the run reading, the castles by area by their column heights.
- [[a005251-bijection](pages/a005251-bijection.md)] - the same map from compositions to binary strings, with 0s and 1s exchanged.
- [[tree-castle-by-area](pages/tree-castle-by-area.md)] - the tree skylines of height at most `h` and the tree castles of height `h` by area.
- [[castle-by-area](pages/castle-by-area.md)] - all castles by area, `2^{n−1}`, and the convex and vee families.
- [[plastic-number](pages/plastic-number.md)] - the plastic number `ψ` and `ψ²`, the growth of the tree castles by area with the height unrestricted.
- [[metallic-means](pages/metallic-means.md)] - de Spinadel's family `σ_p^q`, to which `φ` belongs and the `h`-nacci constants for `h ≥ 3` do not.
- [[castle-graph](pages/castle-graph.md)] - the tree castles by width.
- [[weakly-unimodal-composition](pages/weakly-unimodal-composition.md)] - the convex castles of area `n` as the weakly unimodal compositions of `n`.
- [[aocp-generating-permutations-tuples](pages/aocp-generating-permutations-tuples.md)] - Knuth's mixed-radix generation (Algorithm M), which enumerates the skylines.
- [[area-growth-census](pages/area-growth-census.md)] - every 0/1 strip rule through height 5 by area; the growth constant of a rule on `h` heights is at most the `h`-nacci constant, which the all-ones rule attains, so a constant first appears no earlier than the first height whose `h`-nacci constant reaches it.

## Footnotes

[^1]: https://oeis.org/A011782 (read 2026-10-25) - "Number of compositions (ordered partitions) of n", "a(0) = 1, a(n) = 2^(n-1)".
[^2]: Verified by execution (Python 3.11 with SymPy, 2026-10-16): the castles of height `h = 2..5` and area `n ≤ 14` by enumeration of compositions, against Equations (1) and (2) and the closed forms; the dominant roots of `x^h − x^{h−1} − ⋯ − 1` for `h ≤ 7`, and their irreducibility for `h ≤ 20`; the tree castles of height `h = 2, 3, 4` by enumeration for `n ≤ 16`, the first area at which they differ from all castles of height `h` (4, 5, 6), and the factorizations of the tree-skyline denominators, `x³ − x² − 1`, `(x² − x − 1)(x² + 1)`, `x⁵ − x⁴ − x² − x − 1`; the Fibonacci castles of width `n − 1` against the castles of height 2 and area `n` for `n ≤ 11`.
[^3]: https://oeis.org/A000073 (read 2026-09-17) - tribonacci, "a(n) = a(n-1) + a(n-2) + a(n-3)", g.f. `x²/(1 − x − x² − x³)`, data `0, 0, 1, 1, 2, 4, 7, 13, 24, 44, 81, 149, 274`, comment "number of compositions of n-2 with no part greater than 3"; https://oeis.org/A000078 - tetranacci, g.f. `x³/(1 − x − x² − x³ − x⁴)`, "number of compositions of n-3 with no part greater than 4"; https://oeis.org/A001591 (read 2026-10-16) - "Pentanacci numbers: a(n) = a(n-1) + a(n-2) + a(n-3) + a(n-4) + a(n-5), a(0)=a(1)=a(2)=a(3)=0, a(4)=1"; https://oeis.org/A011782 (read 2026-10-16) - "Coefficients of expansion of (1-x)/(1-2*x) in powers of x"; https://oeis.org/A000930 (read 2026-10-16) - "Narayana's cows sequence: a(0) = a(1) = a(2) = 1; thereafter a(n) = a(n-1) + a(n-3)".
[^4]: Verified by execution (Python 3, 2026-10-04): `(F_61 − 1)/φ^60 = 0.72360680` against `φ/√5 = 0.72360680`.
[^5]: [[balado-silvestre-2026-runs-binary-strings](pages/balado-silvestre-2026-runs-binary-strings.md)] §2.6.4 p.30 L1518-1523 and Remark 30 pp.74-75 L3785-3828 [synthesis] - "wj (n − 1) for j = 2, 3 and 4 are A000100, A000102 and A006979, respectively (number of compositions of n in which the maximal part is j + 1) for n ≥ 1", "w5 (n − 1) is A006980 for n ≥ 6", "wk (n) is the kth column of A048004"; eq. (273), `C_{a≤b}(x, y) = x W_{(a−1)≤(b−1)}(x, y)`; eq. (274), "which was also given by Riordan [53, Eq. (40)]"; eq. (275), "which was given by Riordan as well [53, p. 155]".
[^6]: https://oeis.org/A048004, https://oeis.org/A000100, https://oeis.org/A000102, https://oeis.org/A006979, https://oeis.org/A006980 (read 2026-10-25) - A048004 "Triangular array read by rows: T(n,k) = number of binary vectors of length n whose longest run of consecutive 1's has length k, for n >= 0, 0 <= k <= n", "Equivalently, number of compositions of n+1 having largest part (exactly) k+1"; A000100 "a(n) is the number of compositions of n in which the maximal part is 3", offset 0; A000102 "number of compositions of n in which the maximum part size is 4", offset 0; A006979 "the number of compositions of n in which the maximum part size is 5", offset 0; A006980 "Compositions: 6th column of A048004", offset 6.
[^7]: Verified by execution (Python 3.11 with SymPy, 2026-10-25): the run map, a bijection from the compositions of `n` onto the binary strings of length `n − 1` with the largest part one more than the longest run and the parts equal to `j` sent to the runs of length `j − 1`, for `n ≤ 14`; the castles of height 3, 4, 5 and area `n ≤ 14` against the terms of A000100, A000102 and A006979, and of height 6 against A006980; Equation (2) equal to `x^h (1 − x)²/((1 − 2x + x^h)(1 − 2x + x^{h+1}))` and `1/(1 − x − ⋯ − x^k) − 1` equal to `(x − x^{k+1})/(1 − 2x + x^{k+1})`, symbolically for `h, k ≤ 9`.
