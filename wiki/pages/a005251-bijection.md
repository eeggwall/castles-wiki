---
title: The A005251 bijection - compositions ↔ no-010 strings
category: Analyses
summary: The tree castles of area n, of any height, are the compositions of n with no two neighboring parts at least 2, A005251(n + 2) of them. The standard map from compositions of n to binary strings of length n − 1, a part c becoming 0^{c−1} and the parts joined by single 1s, sends them onto the strings with no factor 010, which number A005251(n + 2) as well; proved, and checked for n ≤ 14. The same sequence counts the compositions avoiding the part 2, the tower-spacing skylines of height at most 2 (spacing_2(w, 2) = A005251(w + 3)), the binary strings with no isolated 1 (A005251(N + 2) at length N), and the even-sector signed towers P_even(6, L)/2^L = A005251(L + 3).
tags: [analysis, castle, bijection, a005251, plastic-number, composition, binary-string, hardin, tree-castle, tower-spacing, verification]
sources: [oeis-encyclopedia]
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

## Other readings

| object | count | link |
|---|---|---|
| compositions of `n` with no two neighboring parts at least 2, the tree castles of area `n` | `A005251(n + 2)` | section *The bijection* |
| binary strings of length `N` with no factor `010` | `A005251(N + 3)` | section *The bijection* |
| compositions of `n` with no part equal to 2 | `A005251(n + 1)` | the tree castles of area `n − 1` with a column of height 1 put in front, [[tree-castle-by-area](pages/tree-castle-by-area.md)] |
| skylines of width `w` on `{1, 2}` with tower spacing at least 2, `spacing_2(w, 2)` | `A005251(w + 3)` | row 2 has no factor `101`, the complement of `010`, [[tower-spacing-castles](pages/tower-spacing-castles.md)] |
| binary strings of length `N` with no isolated `1`, `W_1(N)` | `A005251(N + 2)` | [[hardin-word-identity](pages/hardin-word-identity.md)] |
| even-sector signed towers `P_even(6, L)/2^L` | `A005251(L + 3)` | `= W_1(L + 1)`, [[hardin-word-identity](pages/hardin-word-identity.md)], [[tower-parity-sectors](pages/tower-parity-sectors.md)] |

The strings without `101` of length `w` are the complements of the strings without `010`, so the spacing skylines of width `w` correspond to the strings without `010` of length `w`; the castles of height 2 among them number `A005251(w + 3) − 1`. The strings with no isolated `1` of length `N + 1` and the strings without `010` of length `N` both number `A005251(N + 3)`. The OEIS entry carries the readings by compositions (Joerg Arndt), by strings without `010` (David Callan), and by strings with no isolated zero (Milan Janjic) or with no run of ones of length 1 (Félix Balado).[^1][^3]

The snippets `encode`, `decode` and the check that the image is the set of strings without `010` are on [[castle-snippets-strips](pages/castle-snippets-strips.md)].

## Related Concepts

- [[tree-castle-by-area](pages/tree-castle-by-area.md)] - the tree castles and tree skylines counted by area, with the row of unbounded height `A005251(A + 2)`.
- [[castle-graph](pages/castle-graph.md)] - tree castles, those whose castle graph is a tree.
- [[hardin-word-identity](pages/hardin-word-identity.md)] - `P_even(4m + 2, L) = 2^L W_m(L + 1)`, with `W_1` the strings with no isolated `1`.
- [[tower-spacing-castles](pages/tower-spacing-castles.md)] - skylines with tower spacing at least `g`, and `spacing_2(w, h) = W_{h−1}(w + 1)`.
- [[plastic-number](pages/plastic-number.md)] - `ψ²`, the growth constant of A005251.
- [[castle-by-area](pages/castle-by-area.md)] - castles of area `n` as compositions of `n`.
- [[binary-string-bijection](pages/binary-string-bijection.md)] - the blocks in the row above a block of length `L` as binary strings of length `L`, a different encoding.
- [[unique-tournament](pages/unique-tournament.md)] - the tree skylines of height at most 4, counted by A000570 through compositions into `{1, 3, 4, 5}`.
- [[hardin-identity-seminar](pages/hardin-identity-seminar.md)] - Stop 7 lists these readings of A005251.
- [[oeis-mining-pe502](pages/oeis-mining-pe502.md)] - the signed tower counts `P(k, ·)`; their even sector at `k = 6` is `2^L A005251(L + 3)` ([[tower-parity-sectors](pages/tower-parity-sectors.md)]).

## Footnotes

[^1]: https://oeis.org/A005251 (read 2026-10-16) - "a(0) = 0, a(1) = a(2) = a(3) = 1; thereafter, a(n) = a(n-1) + a(n-2) + a(n-4)", "a(n) = 2*a(n-1) - a(n-2) + a(n-3)", "a(n+2) is the number of compositions (ordered partitions) of n where no two adjacent parts are != 1, see example. - Joerg Arndt, Jan 26 2013", "a(n+3) is the number of n-bit sequences that avoid 010. Example: For n=4 the 12 sequences are all 4-bit sequences except 0100, 0101, 0010, 1010. - David Callan, Mar 25 2004", "a(n+1) is the number of compositions of n avoiding the part 2. - Joerg Arndt, Jul 13 2014".
[^2]: Verified by execution (Python 3.11, 2026-10-16): for every `n ≤ 14`, the image of the compositions of `n` with no two neighboring parts at least 2 equals the set of binary strings of length `n − 1` without `010`, with `A005251(n + 2)` elements; the compositions of `n` without the part 2 number `A005251(n + 1)`; for `N ≤ 13`, the strings of length `N` with no isolated `1` number `A005251(N + 2)` and those without `101` number `A005251(N + 3)`; for `w ≤ 11`, the skylines in `{1, 2}^w` whose row 2 has no factor `101` number `A005251(w + 3)`; `x⁴ − x³ − x² − 1 = (x + 1)(x³ − 2x² + x − 1)`.
[^3]: https://oeis.org/A005251 (read 2026-10-16) - "For n >= 2, a(n) is the number of (n-2)-length binary words with no isolated zeros. - Milan Janjic, Mar 07 2015", "For n>=3, a(n) is the number of binary strings of length n-2 without any maximal runs of ones of length 1. - Félix Balado, Aug 25 2025".
