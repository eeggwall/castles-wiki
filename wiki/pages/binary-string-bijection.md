---
title: Binary-string bijection
category: Concepts
summary: The configurations of blocks in the row directly above a block of length L, no two touching, correspond to the binary strings of length L, a 1 for each covered column; the blocks are the maximal runs of 1s. So there are 2^L configurations, a string with r runs of 1s gives r blocks, and the strings with r runs number C(L+1, 2r). The bijection is the step of the induction that proves T(k, L) = (k+1)^L and of the run recursion for the signed tower count P(k, L). Balado and Silvestre's census of runs in binary strings has C(L+1, 2r) as its eq. (69) and refines it by covered columns: m ≥ 1 blocks covering r columns in C(r − 1, m − 1) C(L − r + 1, m) ways.
tags: [concept, castle, bijection, binary-strings, combinatorics]
sources: [project-euler-502-solution, balado-silvestre-2026-runs-binary-strings]
created: 2026-09-13
updated: 2026-10-25
---

# Binary-string bijection

## Statement

Take a block of length `L`. A **configuration** in the row directly above it is a set of blocks in that row, each lying within the `L` columns of the block below, no two of them touching; the empty configuration, with no blocks, is included. Writing 1 for each covered column and 0 for each uncovered one gives a binary string of length `L`, and this is a bijection: the blocks of a configuration are the maximal runs of 1s of its string.[^1] In the other direction, the maximal runs of 1s of any string are blocks that lie within the block below and are separated by at least one 0, so they never touch.

Three counts follow. There are `2^L` configurations. A string with `r` maximal runs of 1s gives a configuration with `r` blocks.[^1] And the strings of length `L` with `r` runs of 1s number `C(L+1, 2r)`: the `2r` ends of the runs are `2r` distinct gaps among the `L + 1` gaps between and around the columns, and every choice of `2r` gaps, paired off from the left, gives `r` runs with at least one 0 between consecutive runs.[^2]

The same count is eq. (69) of [[balado-silvestre-2026-runs-binary-strings](pages/balado-silvestre-2026-runs-binary-strings.md)], a census of runs in binary strings, which credits it to Goulden and Jackson. Its eq. (201) splits it by the number of 1s: the strings of length `L` with `m ≥ 1` runs of 1s and `r` 1s in all number `C(r − 1, m − 1) C(L − r + 1, m)`. So the configurations above a block of length `L` with `m ≥ 1` blocks covering `r` columns number `C(r − 1, m − 1) C(L − r + 1, m)`, and so do the castles of width `L` and height 2 with `m + 1` blocks and area `L + r`. Summed over `r`, this is Vandermonde's convolution, which the paper uses to recover `C(L + 1, 2m)`.[^5][^6]

*Example.* Above a block of length 3, the eight configurations are the strings `000`, `100`, `010`, `001`, `110`, `011`, `111` and `101`. The first has no block, the next six have one, and `101` has two blocks, separated by the empty middle column. So `C(4, 0) = 1`, `C(4, 2) = 6` and `C(4, 4) = 1`.

This bijection is not the column-wise binary encoding of [[castle-representations](pages/castle-representations.md)], which writes each column of a castle of height `h` as `1^{c_i} 0^{h−c_i}`. Here there is one bit per column of one block, and the string describes one row above that block.

## Worked example: the castle (1, 7, 2, 9)

The skyline `(1, 7, 2, 9)`, the decimal digits of 1729, is a castle of width 4 and height 9 ([[hardy-ramanujan-castle](pages/hardy-ramanujan-castle.md)]). Row `r` of the castle covers the columns with `c_i ≥ r`:

| row(s) | four columns | blocks in the row |
|---|---|---|
| 1 | `1111` | one, columns 1 to 4 |
| 2 | `0111` | one, columns 2 to 4 |
| 3 to 7 | `0101` | two per row, columns 2 and 4 |
| 8 and 9 | `0001` | one per row, column 4 |

Row 2, above the bottom row of length 4, is the string `0111`, whose single run `111` is one block of length 3. Above that block, row 3 restricted to its columns 2 to 4 is the string `101`, two blocks of length 1 with the empty column 3 between them. Every row is read in the same way, relative to the blocks directly below it. The block count is `1 + 1 + 5·2 + 2·1 = 14`, which is also the total ascent `1 + 6 + 0 + 7` of the skyline, so the castle has an even number of blocks.[^2]

## The induction for T(k, L)

The towers of height at most `k` on a base of length `L` are a configuration in the first row above the base, given by a binary string `b`, together with towers of height at most `k − 1` on each block of that row. The towers on different blocks are chosen independently, since every block lies within the span of the block below it ([[generalized-dyck-grammar](pages/generalized-dyck-grammar.md)]). So, with `ones(b)` the number of 1s in `b`,[^3]

```
T(k, L)  =  Σ_{b ∈ {0,1}^L}  Π_{runs of 1s in b, of length l}  T(k−1, l)  =  Σ_b k^{ones(b)}  =  (k+1)^L,
```

by induction on `k` from `T(0, L) = 1` ([[castle-counting-formula](pages/castle-counting-formula.md)], the Lemma in the section *Tower count*). The blocks of the towers are the `runs(b)` blocks of the first row and the blocks of the towers above them, so the signed tower count satisfies the same recursion with a sign:[^4]

```
P(k, L)  =  Σ_{b ∈ {0,1}^L}  (−1)^{runs(b)}  Π_{runs of 1s in b, of length l}  P(k−1, l),        P(0, L)  =  1.
```

At `k = 1` every factor `P(0, l)` is 1, and `P(1, L) = Σ_b (−1)^{runs(b)} = Σ_r (−1)^r C(L+1, 2r) = Re((1+i)^{L+1})` ([[signed-tower-count](pages/signed-tower-count.md)], the section *The case k = 1*).[^4]

## Appearances in Sources

- [[project-euler-502-solution](pages/project-euler-502-solution.md)] - the statement of the bijection with its two counts, and its use in the induction for `T(k, L)` and the recursion for `P(k, L)`.
- [[balado-silvestre-2026-runs-binary-strings](pages/balado-silvestre-2026-runs-binary-strings.md)] - the strings by their runs of 1s: `C(L + 1, 2r)` (eq. 69), the split by the number of 1s (eq. 201), and the longest-run, shortest-run and total counts that give the castles of height 2 by their upper blocks.

## Related Concepts

- [[castle-representations](pages/castle-representations.md)] - the column-wise binary encoding of a castle, which is a different encoding.
- [[castle-counting-formula](pages/castle-counting-formula.md)] - the three proofs of `T(k, L) = (k+1)^L`, one of them by this induction.
- [[signed-tower-count](pages/signed-tower-count.md)] - `P(k, L)`, and the case `k = 1`, where the towers are the binary strings.
- [[castle-counting-function](pages/castle-counting-function.md)] - the castles of height 2, counted through `C(w+1, 2r)` as `A^e(w, 2) = A038505(w+1)` and `A^o(w, 2) = A038503(w+1) − 1`.
- [[block-count-constraints](pages/block-count-constraints.md)] - the block-count generating function of towers, which at height at most 1 is `Σ_r C(L+1, 2r) z^r`.
- [[generalized-dyck-grammar](pages/generalized-dyck-grammar.md)] - the tower grammar, in which every block lies within the span of the block below it.
- [[hardy-ramanujan-castle](pages/hardy-ramanujan-castle.md)] - the castles read off the digits of 1729 in several bases, among them `(1, 7, 2, 9)`.

## Footnotes

[^1]: [[project-euler-502-solution](pages/project-euler-502-solution.md)] §"The binary-string bijection" L14-19 - "Configurations within a block of length L (non-overlapping, non-adjacent integer-length sub-blocks, including the empty config) biject with binary strings of length L: map each string to the configuration whose sub-blocks are its maximal runs of 1s", "The number of configurations in a length-L block is 2^L", "If a binary string has r maximal runs of 1s, the corresponding configuration has r sub-blocks."
[^2]: Verified by execution (Python 3.11, 2026-10-16): the number of binary strings of length `L` with `r` runs of 1s is `C(L+1, 2r)` for `L ≤ 9`; the rows of `(1, 7, 2, 9)` and its block count 14; the run recursion for `P(k, L)` against the sum over all towers for `k ≤ 3`, `L ≤ 5`.
[^3]: [[project-euler-502-solution](pages/project-euler-502-solution.md)] §"T(k, L) = (k+1)^L" L25-35 - "Base: T(0, L) = 1 (only the empty tower)", "A tower of height ≤ k above a length-L block is a length-L binary string (choosing which columns have sub-blocks starting at the row directly above) plus, for each maximal run of length l, an independent tower of height ≤ k-1 above that sub-block", "T(k, L) = ∑_b ∏_{runs} T(k-1, l) = ∑_b k^{ones(b)} = (1 + k)^L".
[^4]: [[project-euler-502-solution](pages/project-euler-502-solution.md)] §"Recursion for P(k, L)" L75-79, L88-91, L108 - "P(k, L) = ∑_{b ∈ {0,1}^L} (-1)^{runs(b)} ∏_{runs of length l} P(k-1, l)", "Base: P(0, L) = 1", "P(1, L) = ∑_{b ∈ {0,1}^L} (-1)^{runs(b)}", "P(1, L) = Re((1+i)^{L+1})".
[^5]: [[balado-silvestre-2026-runs-binary-strings](pages/balado-silvestre-2026-runs-binary-strings.md)] §2.5.3 pp.25-26 L1274-1310 and §4.2 p.57 L2938-2948 [synthesis] - eq. (69), `w(n, m) = C(n + 1, 2m)`; Remark 12, "Goulden and Jackson [26, Sec. 2.4.4] found (69)", with the sum over the number of 1s, "a variation of Vandermonde’s convolution"; eq. (201), `w(n, m, r) = C(r − 1, m − 1) C(n − r + 1, m)`, "previously given by Stevens [63, Eq. (3.05)], Mood [44, Eq. (2.11)]".
[^6]: Verified by execution (Python 3.11, 2026-10-25): `C(L + 1, 2m)` for `L ≤ 12`, and `C(r − 1, m − 1) C(L − r + 1, m)` against the strings of length `L` with `m ≥ 1` runs of 1s and `r` 1s, for `L ≤ 12`.
