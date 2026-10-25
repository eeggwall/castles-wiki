---
title: The A005251 bijection - compositions ↔ no-010 strings
category: Analyses
summary: The tree castles of area n, of any height, are the compositions of n with no two neighboring parts at least 2, A005251(n + 2) of them. The standard map from compositions of n to binary strings of length n − 1, a part c becoming 0^{c−1} and the parts joined by single 1s, sends them onto the strings with no factor 010, which number A005251(n + 2) as well; proved, and checked for n ≤ 14. Composed with the column map of tree-castle-by-area, a column of height c ≥ 2 becoming a run 1^c, it gives an explicit bijection from the strings of length n − 1 with no 010 onto the strings of length n with no isolated 1. Matched with the tree castles of area n, the compositions of n + 1 avoiding the part 2, the binary strings of length n with no isolated 1 and the tower-spacing skylines of width n − 1 and height at most 2 correspond to them by explicit bijections, and the even-sector signed towers P_even(6, n − 1)/2^{n−1} have the same count by a change of basis.
tags: [analysis, castle, bijection, a005251, plastic-number, composition, binary-string, hardin, tree-castle, tower-spacing, verification]
sources: [oeis-mining-pe502]
created: 2026-09-18
updated: 2026-10-25
---

# The A005251 bijection

## Two readings of A005251

`A005251` is `0, 1, 1, 1, 2, 4, 7, 12, 21, 37, 65, 114, …` (offset 0), with `a(n) = a(n−1) + a(n−2) + a(n−4)` for `n ≥ 4`.[^1] Since `x⁴ − x³ − x² − 1 = (x + 1)(x³ − 2x² + x − 1)` and the initial terms give the root `−1` no weight, also `a(n) = 2a(n−1) − a(n−2) + a(n−3)`; the cubic is the minimal polynomial of `ψ²`, the square of the plastic number ([[plastic-number](pages/plastic-number.md)]). Two of its readings are:

- **Tree castles by area.** A castle is a tree castle when its castle graph is a tree, which happens exactly when no two neighboring columns both have height at least 2 ([[castle-graph](pages/castle-graph.md)]). Read as a composition of its area `n`, a tree castle of any height is a composition of `n` with no two neighboring parts at least 2. These number `A005251(n + 2)`.[^1]
- **Strings without 010.** The binary strings of length `N` with no factor `010` number `A005251(N + 3)`. Of the 16 strings of length 4, exactly `0100`, `0101`, `0010` and `1010` contain `010`, which leaves 12.[^1]

With `N = n − 1` the two counts agree, and a bijection carries one constraint onto the other.

## The bijection

Place `n` unit cells in a row, with `n − 1` gaps between neighboring cells. A composition of `n` chooses which gaps are part boundaries; write `1` at each boundary and `0` at every other gap. So part `c_j` becomes `c_j − 1` zeros, and the blocks of zeros are joined by single `1`s:

```
(c_1, …, c_w)   ↦   0^{c_1−1} 1 0^{c_2−1} 1 ⋯ 1 0^{c_w−1}                    (length n − 1).
```

The inverse splits a string at its `1`s and reads each maximal run of `r` zeros as a part `r + 1`. This is the standard bijection between the compositions of `n` and the binary strings of length `n − 1`.

**Proposition.** The map sends the compositions of `n` with no two neighboring parts at least 2 onto the binary strings of length `n − 1` with no factor `010`.

*Proof.* A part `c_j ≥ 2` gives a nonempty block of zeros. Two neighboring parts both at least 2 put a `0` on each side of the `1` between them, a factor `010`. Conversely, the middle `1` of a factor `010` is a boundary between two parts whose blocks of zeros are nonempty, so both parts are at least 2. ∎

The image is exactly the set of strings without `010` for every `n ≤ 14`, with `1, 2, 4, 7, 12, 21, 37, 65, 114, 200, 351, 616, 1081, 1897` elements.[^2] At `n = 5`, the twelve compositions and their strings:

| composition | string | | composition | string |
|---|---|---|---|---|
| `(1,1,1,1,1)` | `1111` | | `(1,4)` | `1000` |
| `(1,1,1,2)` | `1110` | | `(2,1,1,1)` | `0111` |
| `(1,1,2,1)` | `1101` | | `(2,1,2)` | `0110` |
| `(1,1,3)` | `1100` | | `(3,1,1)` | `0011` |
| `(1,2,1,1)` | `1011` | | `(4,1)` | `0001` |
| `(1,3,1)` | `1001` | | `(5)` | `0000` |

The composition `(2, 2, 1)`, with two neighboring parts equal to 2, is excluded; it maps to `0101`, which contains `010`.

## Strings with no isolated 1

The section *Compositions* of [[tree-castle-by-area](pages/tree-castle-by-area.md)] sends a tree castle of area `n` to a binary string of length `n`: a column of height 1 becomes `0`, and a column of height `c ≥ 2` becomes a run `1^c`. Its image is the set of strings of length `n` with no isolated `1`, those whose runs of ones all have length at least 2. Composed with the inverse of the gap map, it carries the strings without `010` onto these strings directly.

**Proposition.** Split a binary string of length `n − 1` with no factor `010` at its `1`s into blocks of zeros, some of them empty. Replacing each empty block by `0` and each block `0^r` with `r ≥ 1` by `1^{r+1}`, and dropping the `1`s between the blocks, is a bijection onto the binary strings of length `n` with no isolated `1`.

*Proof.* The block `0^r` is the image under the gap map of a part `r + 1`, and it is replaced by `r + 1` symbols, so the result has length `n`. Two nonempty blocks are never neighbors, since the `1` between them would be the middle of a factor `010`; so each run `1^{r+1}` has a `0` or an end of the string on either side, and every run of ones has length at least 2. Conversely, read each `0` as an empty block and each maximal run `1^m` as the block `0^{m−1}`, and join the blocks with `1`s. Each run has length `m ≥ 2`, so its block is nonempty, and two runs are separated by at least one `0`, so two nonempty blocks are separated by at least two `1`s and the joined string has no `010`. The two maps are inverse to each other. ∎

At `n = 5`, the strings `1111`, `1000` and `0110` of the table above become `00000`, `01111` and `11011`, the column strings of the castles `(1, 1, 1, 1, 1)`, `(1, 4)` and `(2, 1, 2)`. The bijection holds for every `n ≤ 14`.[^5]

## The readings at one index

Each object below is taken at the size matched with the tree castles of area `n`, so each is counted by `A005251(n + 2)`. The second column gives the count in the object's own size variable, as the linked pages state it. The third gives the map from the tree castles, or says *equal counts* when the count is proved equal with no map between the objects.[^4]

| object, at the size matched with area `n` | count at its own index | map from the tree castles | where |
|---|---|---|---|
| compositions of `n` with no two neighboring parts at least 2 | `A005251(n + 2)` | the column heights, read left to right | section *Two readings of A005251* |
| binary strings of length `N = n − 1` with no factor `010` | `A005251(N + 3)` | the gap map | section *The bijection* |
| binary strings of length `N = n` with no isolated `1`, `W_1(N)` | `A005251(N + 2)` | a column of height 1 becomes `0`, a column of height `c ≥ 2` becomes `1^c` | section *Strings with no isolated 1*, [[tree-castle-by-area](pages/tree-castle-by-area.md)] section *Compositions* |
| compositions of `m = n + 1` with no part equal to 2 | `A005251(m + 1)` | a column of height 1 put in front, then each column of height 1 followed by a column of height `j ≥ 2` merged into one part `1 + j` | [[tree-castle-by-area](pages/tree-castle-by-area.md)], section *Compositions* |
| skylines of width `w = n − 1` on `{1, 2}` with tower spacing at least 2, `spacing_2(w, 2)` | `A005251(w + 3)` | the gap map, then each `0` a column of height 2 and each `1` a column of height 1 | [[tower-spacing-castles](pages/tower-spacing-castles.md)] |
| even-sector signed towers `P_even(6, L)/2^L` with `L = n − 1` | `A005251(L + 3)` | equal counts, `P_even(6, L) = 2^L W_1(L + 1)` | [[hardin-word-identity](pages/hardin-word-identity.md)], [[tower-parity-sectors](pages/tower-parity-sectors.md)] |

The skyline map turns a column of height `c` into `c − 1` columns of height 2 and puts one column of height 1 between neighboring columns of the castle. Row 2 of the skyline is the complement of the string, so it has no factor `101`, which is the tower-spacing condition at height 2; the castles of height 2 among these skylines, all but the flat row, number `A005251(w + 3) − 1`. The even sector is the one reading without a map: [[hardin-word-identity](pages/hardin-word-identity.md)] proves its count by a change of basis between transfer matrices. The OEIS entry carries the readings by compositions (Joerg Arndt), by strings without `010` (David Callan), and by strings with no isolated zero (Milan Janjic) or with no run of ones of length 1 (Félix Balado).[^1][^3]

The snippets `encode`, `decode` and the check that the image is the set of strings without `010` are on [[castle-snippets-strips](pages/castle-snippets-strips.md)].

## Appearances in Sources

- [[oeis-mining-pe502](pages/oeis-mining-pe502.md)] - the signed tower counts `P(k, ·)`; their even sector at `k = 6` is `2^L A005251(L + 3)` ([[tower-parity-sectors](pages/tower-parity-sectors.md)]).

## Related Concepts

- [[tree-castle-by-area](pages/tree-castle-by-area.md)] - the tree castles and tree skylines counted by area, with the row of unbounded height `A005251(A + 2)`, and the column map onto the strings with no isolated `1`.
- [[castle-graph](pages/castle-graph.md)] - tree castles, those whose castle graph is a tree.
- [[hardin-word-identity](pages/hardin-word-identity.md)] - `P_even(4m + 2, L) = 2^L W_m(L + 1)`, with `W_1` the strings with no isolated `1`.
- [[tower-spacing-castles](pages/tower-spacing-castles.md)] - skylines with tower spacing at least `g`, and `spacing_2(w, h) = W_{h−1}(w + 1)`.
- [[plastic-number](pages/plastic-number.md)] - `ψ²`, the growth constant of A005251.
- [[castle-by-area](pages/castle-by-area.md)] - castles of area `n` as compositions of `n`.
- [[binary-string-bijection](pages/binary-string-bijection.md)] - the blocks in the row above a block of length `L` as binary strings of length `L`, a different encoding.
- [[unique-tournament](pages/unique-tournament.md)] - the tree skylines of height at most 4, counted by A000570 through compositions into `{1, 3, 4, 5}`.
- [[hardin-identity-seminar](pages/hardin-identity-seminar.md)] - Stop 7 lists these readings of A005251.

## Footnotes

[^1]: https://oeis.org/A005251 (read 2026-10-16) - "a(0) = 0, a(1) = a(2) = a(3) = 1; thereafter, a(n) = a(n-1) + a(n-2) + a(n-4)", "a(n) = 2*a(n-1) - a(n-2) + a(n-3)", "a(n+2) is the number of compositions (ordered partitions) of n where no two adjacent parts are != 1, see example. - Joerg Arndt, Jan 26 2013", "a(n+3) is the number of n-bit sequences that avoid 010. Example: For n=4 the 12 sequences are all 4-bit sequences except 0100, 0101, 0010, 1010. - David Callan, Mar 25 2004", "a(n+1) is the number of compositions of n avoiding the part 2. - Joerg Arndt, Jul 13 2014".
[^2]: Verified by execution (Python 3.11, 2026-10-16): for every `n ≤ 14`, the image of the compositions of `n` with no two neighboring parts at least 2 equals the set of binary strings of length `n − 1` without `010`, with `A005251(n + 2)` elements; the compositions of `n` without the part 2 number `A005251(n + 1)`; for `N ≤ 13`, the strings of length `N` with no isolated `1` number `A005251(N + 2)` and those without `101` number `A005251(N + 3)`; for `w ≤ 11`, the skylines in `{1, 2}^w` whose row 2 has no factor `101` number `A005251(w + 3)`; `x⁴ − x³ − x² − 1 = (x + 1)(x³ − 2x² + x − 1)`.
[^3]: https://oeis.org/A005251 (read 2026-10-16) - "For n >= 2, a(n) is the number of (n-2)-length binary words with no isolated zeros. - Milan Janjic, Mar 07 2015", "For n>=3, a(n) is the number of binary strings of length n-2 without any maximal runs of ones of length 1. - Félix Balado, Aug 25 2025".
[^4]: Verified by execution (Python 3.11, 2026-10-25): for every `n ≤ 14`, the tree castles of area `n` number `A005251(n + 2)`, and the column map, the leading-column map and the skyline map of the table send them one-to-one onto the binary strings of length `n` with no isolated `1`, the compositions of `n + 1` without the part 2 and the skylines in `{1, 2}^{n−1}` with tower spacing at least 2 (in row 2, every run of empty cells between two filled cells has length at least 2).
[^5]: Verified by execution (Python 3.11, 2026-10-25): for every `n ≤ 14`, the map of the Proposition sends the binary strings of length `n − 1` without `010` one-to-one onto the binary strings of length `n` with no isolated `1`, and on the gap string of every tree castle of area `n` it agrees with the column map of the table in the section *The readings at one index*.
