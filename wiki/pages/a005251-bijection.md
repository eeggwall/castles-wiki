---
title: The A005251 bijection - compositions ↔ no-010 strings
category: Analyses
summary: The tree castles of area n, of any height, are the compositions of n with no two neighboring parts at least 2, A005251(n + 2) of them. The standard map from compositions of n to binary strings of length n − 1, a part c becoming 0^{c−1} and the parts joined by single 1s, sends them onto the strings with no factor 010, which number A005251(n + 2) as well; proved, and checked for n ≤ 14. A three-state automaton counts the strings directly, with characteristic polynomial x³ − 2x² + x − 1 and generating function (1 + x²)/(1 − 2x + x² − x³), and the bijection matches it with the area generating function of the tree skylines. Composed with the column map of tree-castle-by-area, a column of height c ≥ 2 becoming a run 1^c, it gives an explicit bijection from the strings of length n − 1 with no 010 onto the strings of length n with no isolated 1. Matched with the tree castles of area n, the compositions of n + 1 avoiding the part 2, the binary strings of length n with no isolated 1 and the tower-spacing skylines of width n − 1 and height at most 2 correspond to them by explicit bijections, and the even-sector signed towers P_even(6, n − 1)/2^{n−1} have the same count by a change of basis. Under the gap map a tree castle's width, height and number of blocks are one more than the number of 1s, the longest run of zeros and the number of zeros, so height at most h means also avoiding 0^h, and Σ (−1)^{blocks} over the tree castles of area n is (−1)^n A000931(n − 1), a signed Padovan number.
tags: [analysis, castle, bijection, a005251, plastic-number, composition, binary-string, hardin, tree-castle, tower-spacing, padovan, parity, verification]
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

## Counting the strings

The strings without `010` can be counted directly. Read a string from left to right and record how much of `010` its end has begun: state `a` when the string is empty or ends in a `1` not preceded by `0`, state `b` when it ends in `0`, and state `c` when it ends in `01`. Appending `0` sends `a` and `b` to `b` and is forbidden at `c`, which would complete `010`; appending `1` sends `a` to `a`, `b` to `c` and `c` to `a`. With rows and columns in the order `a, b, c`, the transfer matrix is

```
M  =  [ 1 1 0 ]        a:  0 → b,  1 → a
      [ 0 1 1 ]        b:  0 → b,  1 → c
      [ 1 0 0 ]        c:          1 → a

det(x·I − M)  =  x(x − 1)² − 1  =  x³ − 2x² + x − 1.
```

The number `s(N)` of strings of length `N` without `010` is the sum of row `a` of `M^N`, so

```
Σ_{N≥0} s(N) x^N  =  (1 + x²) / (1 − 2x + x² − x³)  =  1 + 2x + 4x² + 7x³ + 12x⁴ + 21x⁵ + ⋯ .        (1)
```

By the Cayley-Hamilton theorem, `s(N) = 2s(N−1) − s(N−2) + s(N−3)` for `N ≥ 3`, the cubic recurrence of A005251, and `s(0), s(1), s(2) = 1, 2, 4` are `A005251(3), A005251(4), A005251(5)`; so `s(N) = A005251(N + 3)` for every `N`.[^1] The automaton reaches the cubic, the minimal polynomial of `ψ²`, directly, with no factor `x + 1` to discard. The OEIS entry lists `M` among four `3 × 3` matrices whose `n`-th power has top left entry `A005251(n + 1)` (R. J. Mathar); for `M`, that entry counts the strings of length `n` without `010` that end in state `a`.

On the castle side, [[tree-castle-by-area](pages/tree-castle-by-area.md)] derives the generating function of the tree skylines by area, the empty skyline included, from their columns: `G_∞(q) = (1 − q + q²)/(1 − 2q + q² − q³)`. With Equation (1) at `x = q`, the two satisfy

```
G_∞(q)  =  1 + q · Σ_{N≥0} s(N) q^N,
```

which is the bijection read coefficient by coefficient: the `1` is the empty skyline, and a tree castle of area `n` carries `q^n` while its string has length `n − 1`. Both counts are derived independently, one from the columns and one from the strings, and the bijection is a combinatorial proof of this identity.[^3]

## Strings with no isolated 1

The section *Compositions* of [[tree-castle-by-area](pages/tree-castle-by-area.md)] sends a tree castle of area `n` to a binary string of length `n`: a column of height 1 becomes `0`, and a column of height `c ≥ 2` becomes a run `1^c`. Its image is the set of strings of length `n` with no isolated `1`, those whose runs of ones all have length at least 2. Composed with the inverse of the gap map, it carries the strings without `010` onto these strings directly.

**Proposition.** Split a binary string of length `n − 1` with no factor `010` at its `1`s into blocks of zeros, some of them empty. Replacing each empty block by `0` and each block `0^r` with `r ≥ 1` by `1^{r+1}`, and dropping the `1`s between the blocks, is a bijection onto the binary strings of length `n` with no isolated `1`.

*Proof.* The block `0^r` is the image under the gap map of a part `r + 1`, and it is replaced by `r + 1` symbols, so the result has length `n`. Two nonempty blocks are never neighbors, since the `1` between them would be the middle of a factor `010`; so each run `1^{r+1}` has a `0` or an end of the string on either side, and every run of ones has length at least 2. Conversely, read each `0` as an empty block and each maximal run `1^m` as the block `0^{m−1}`, and join the blocks with `1`s. Each run has length `m ≥ 2`, so its block is nonempty, and two runs are separated by at least one `0`, so two nonempty blocks are separated by at least two `1`s and the joined string has no `010`. The two maps are inverse to each other. ∎

At `n = 5`, the strings `1111`, `1000` and `0110` of the table above become `00000`, `01111` and `11011`, the column strings of the castles `(1, 1, 1, 1, 1)`, `(1, 4)` and `(2, 1, 2)`. The map is checked for every `n ≤ 14`.[^4]

## The readings at one index

Each object below is taken at the size matched with the tree castles of area `n`, so each is counted by `A005251(n + 2)`. The second column gives the count in the object's own size variable. The third gives the map from the tree castles, or says *equal counts* when the count is proved equal with no map between the objects.[^5]

| object, at the size matched with area `n` | count at its own index | map from the tree castles | where |
|---|---|---|---|
| compositions of `n` with no two neighboring parts at least 2 | `A005251(n + 2)` | the column heights, read left to right | section *Two readings of A005251* |
| binary strings of length `N = n − 1` with no factor `010` | `A005251(N + 3)` | the gap map | section *The bijection* |
| binary strings of length `N = n` with no isolated `1`, `W_1(N)` | `A005251(N + 2)` | a column of height 1 becomes `0`, a column of height `c ≥ 2` becomes `1^c` | section *Strings with no isolated 1*, [[tree-castle-by-area](pages/tree-castle-by-area.md)] section *Compositions* |
| compositions of `m = n + 1` with no part equal to 2 | `A005251(m + 1)` | a column of height 1 put in front, then each column of height 1 followed by a column of height `j ≥ 2` merged into one part `1 + j` | [[tree-castle-by-area](pages/tree-castle-by-area.md)], section *Compositions* |
| skylines of width `w = n − 1` on `{1, 2}` with tower spacing at least 2, `spacing_2(w, 2)` | `A005251(w + 3)` | the gap map, then each `0` a column of height 2 and each `1` a column of height 1 | [[tower-spacing-castles](pages/tower-spacing-castles.md)] |
| even-sector signed towers `P_even(6, L)/2^L` with `L = n − 1` | `A005251(L + 3)` | equal counts, `P_even(6, L) = 2^L W_1(L + 1)` | [[hardin-word-identity](pages/hardin-word-identity.md)], [[tower-parity-sectors](pages/tower-parity-sectors.md)] |

The skyline map turns a column of height `c` into `c − 1` columns of height 2 and puts one column of height 1 between neighboring columns of the castle. Row 2 of the skyline is the complement of the string, so it has no factor `101`, which is the tower-spacing condition at height 2; the castles of height 2 among these skylines, all but the flat row, number `A005251(w + 3) − 1`. The even sector is the one reading without a map: [[hardin-word-identity](pages/hardin-word-identity.md)] proves its count by a change of basis between transfer matrices. The OEIS entry carries the readings by compositions (Joerg Arndt), by strings without `010` (David Callan), and by strings with no isolated zero (Milan Janjic) or with no run of ones of length 1 (Félix Balado).[^1][^6]

The snippets `encode`, `decode` and the check that the image is the set of strings without `010` are on [[castle-snippets-strips](pages/castle-snippets-strips.md)].

## Castle statistics on the strings

The gap map carries three statistics of a tree castle `(c_1, …, c_w)` of area `n` to its string of length `n − 1`:

| tree castle | string without `010` |
|---|---|
| width `w` | one more than the number of `1`s |
| height `max c_j` | one more than the longest run of zeros |
| number of blocks, `1 + n − w` | one more than the number of zeros |

Each `1` separates two parts, and each part `c_j` is a run of `c_j − 1` zeros, which gives the first two rows. The bottom row of a tree castle is one block and every cell above it is a block by itself, so a tree castle has `1 + n − w` blocks ([[castle-graph](pages/castle-graph.md)]), and the zeros number `Σ (c_j − 1) = n − w`.[^7]

**Height.** A tree castle has height at most `h` exactly when its string has no run of `h` zeros. So the tree skylines of height at most `h` and area `n` correspond to the strings of length `n − 1` that avoid both `010` and `0^h`, and the row `h` of Table 1 on [[tree-castle-by-area](pages/tree-castle-by-area.md)] counts these strings. At `h = 2` they are the strings with neither `00` nor `010`, counted by Narayana's cows.

**Parity.** Project Euler 502 counts the castles with an even number of blocks. A tree castle has an even number of blocks exactly when its string has an odd number of zeros. A tree castle of area `n` and width `w` has sign `(−1)^{blocks} = −(−1)^{n−w}`, so replacing `q` by `−q` and `x` by `−1` in Equation (1) of [[tree-castle-by-area](pages/tree-castle-by-area.md)] with the height unrestricted, changing the sign and leaving out the empty skyline, gives the signed count by area:

```
Σ_{n≥1} ( Σ_{tree castles of area n} (−1)^{blocks} ) q^n  =  −q(1 − q²) / (1 − q² + q³).        (2)
```

The Padovan numbers `A000931(m)` have generating function `(1 − x²)/(1 − x² − x³)`,[^8] and the right side of Equation (2) is that function at `x = −q`, multiplied by `−q`. So, for every `n ≥ 1`,

```
Σ_{tree castles of area n} (−1)^{blocks}  =  (−1)^n · A000931(n − 1).
```

The Padovan numbers grow like `ψ^n`,[^8] and the tree castles like `ψ^{2n}`, so the even-block and odd-block tree castles of area `n` are each about half of them. The first counts:

| `n` | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| tree castles, `A005251(n + 2)` | 1 | 2 | 4 | 7 | 12 | 21 | 37 | 65 | 114 | 200 | 351 | 616 | 1081 | 1897 |
| even number of blocks | 0 | 1 | 2 | 4 | 6 | 11 | 18 | 33 | 56 | 101 | 174 | 310 | 538 | 952 |
| odd number of blocks | 1 | 1 | 2 | 3 | 6 | 10 | 19 | 32 | 58 | 99 | 177 | 306 | 543 | 945 |
| `(−1)^n A000931(n − 1)` | −1 | 0 | 0 | 1 | 0 | 1 | −1 | 1 | −2 | 2 | −3 | 4 | −5 | 7 |

Padovan numbers also correct the count up to mirror image: [[castle-graph](pages/castle-graph.md)] counts the tree castles of area `n` up to mirror image as `(A005251(n + 2) + A000931(n + 6))/2`, the palindromic ones numbering `A000931(n + 6)` ([[padovan-families](pages/padovan-families.md)]).

## Related Concepts

- [[tree-castle-by-area](pages/tree-castle-by-area.md)] - the tree castles and tree skylines counted by area, with the row of unbounded height `A005251(A + 2)`, and the column map onto the strings with no isolated `1`.
- [[castle-graph](pages/castle-graph.md)] - tree castles, those whose castle graph is a tree, their `1 + n − w` blocks and their count up to mirror image.
- [[padovan-families](pages/padovan-families.md)] - the Padovan numbers `A000931`, which count the palindromic tree castles by area.
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
[^3]: Verified by execution (Python 3.11 with SymPy 1.14, 2026-10-25): the characteristic polynomial of `M` is `x³ − 2x² + x − 1`; row `a` of `(I − xM)^{−1}`, summed, is Equation (1), whose coefficients equal `A005251(N + 3)` for `N < 30`; and `G_∞(q) − 1 − q·Σ s(N) q^N` simplifies to 0; the top left entry of `M^n` is `A005251(n + 1)` for `n < 15`. https://oeis.org/A005251 (read 2026-10-25) - "a(n+1) is the top left entry of the n-th power of any of the 3 X 3 matrices [1, 1, 0; 0, 1, 1; 1, 0, 0] or [1, 0, 1; 1, 1, 0; 0, 1, 0] or [1, 1, 0; 0, 0, 1; 1, 0, 1] or [1, 0, 1; 1, 0, 0; 0, 1, 1]. - R. J. Mathar, Feb 03 2014".
[^4]: Verified by execution (Python 3.11, 2026-10-25): for every `n ≤ 14`, the map of the Proposition sends the binary strings of length `n − 1` without `010` one-to-one onto the binary strings of length `n` with no isolated `1`, and on the gap string of every tree castle of area `n` it agrees with the column map of the table in the section *The readings at one index*.
[^5]: Verified by execution (Python 3.11, 2026-10-25): for every `n ≤ 14`, the tree castles of area `n` number `A005251(n + 2)`, and the column map, the leading-column map and the skyline map of the table send them one-to-one onto the binary strings of length `n` with no isolated `1`, the compositions of `n + 1` without the part 2 and the skylines in `{1, 2}^{n−1}` with tower spacing at least 2 (in row 2, every run of empty cells between two filled cells has length at least 2).
[^6]: https://oeis.org/A005251 (read 2026-10-16) - "For n >= 2, a(n) is the number of (n-2)-length binary words with no isolated zeros. - Milan Janjic, Mar 07 2015", "For n>=3, a(n) is the number of binary strings of length n-2 without any maximal runs of ones of length 1. - Félix Balado, Aug 25 2025".
[^7]: Verified by execution (Python 3.11 with SymPy 1.14, 2026-10-25): for every `n ≤ 14`, the width, height and block count of every tree castle of area `n` against the three string statistics; for `2 ≤ h ≤ 6` and `n ≤ 14`, the tree castles of area `n` and height at most `h` against the strings of length `n − 1` avoiding `010` and `0^h`; the signed count by enumeration against `(−1)^n A000931(n − 1)` for `n ≤ 20`, and the table for `n ≤ 14`; Equation (2) from Equation (1) of tree-castle-by-area with `P_∞(q) = q²/(1 − q)`, and its difference from `−q(1 − q²)/(1 − q² + q³)` simplified to 0.
[^8]: https://oeis.org/A000931 (read 2026-10-25) - "Padovan sequence (or Padovan numbers): a(n) = a(n-2) + a(n-3) with a(0) = 1, a(1) = a(2) = 0.", "G.f.: (1-x^2)/(1-x^2-x^3).", "a(n) is asymptotic to r^n / (2*r+3) where r = 1.3247179572447... = A060006, the real root of x^3 = x + 1."
