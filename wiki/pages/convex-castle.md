---
title: Convex castle
category: Concepts
summary: A castle whose skyline is unimodal, rising weakly to its maximum and then falling weakly; equivalently a castle that is row-convex as well as column-convex, or a castle of height h with exactly h blocks. The convex castles of width w and height h number A_convex(w, h) = C(2h+w−3, w−1). By area they are the weakly unimodal compositions (A001523), by semi-perimeter they are the stack polyominoes, and every castle lies over a unique convex castle, its convex core.
tags: [concept, castle, convex, unimodal, column-convex, row-convex, combinatorics, stars-and-bars]
sources: [project-euler-502-representations, project-euler-502-solution, project-euler-502-brute-force, oeis-encyclopedia, algebraic-languages-and-polyominoes-enumeration, bender-1974-convex-n-ominoes]
created: 2026-09-13
updated: 2026-10-29
---

# Convex castle

## Definition

A **convex castle** is a [[castle-polyomino](pages/castle-polyomino.md)] whose skyline is unimodal: for some column `p`,

```
c_1  ≤  c_2  ≤  ⋯  ≤  c_p  ≥  c_{p+1}  ≥  ⋯  ≥  c_w.
```

`A_convex(w, h)` is the number of convex castles of width `w` and height `h`.

*Example.* The skyline `(1, 2, 2, 3, 1)` is a convex castle of width 5 and height 3. The skyline `(2, 1, 2)` is a castle of height 2 that is not convex.

The source defines convex castles by their words in the steps `U` (up one row), `R` (one column) and `D` (down one row), in which a castle of width `w` has `w` letters `R` ([[urd-step-strings](pages/urd-step-strings.md)]). The word of a convex castle splits into three parts: a **front** of `U` and `R` steps up to the maximum height, with no `D`; a **middle** of `R` steps at the maximum height, at least one; and a **back** of `D` and `R` steps down to the base, with no `U`. The word begins with `U` and ends with `D`.[^1] For the skyline `(1, 2, 2, 3, 1)` the word is

```
U R U R R U   R   D D R D
   front     middle  back
```

The source classifies every other castle as a variation of a convex castle, made by inserting pairs of `D` and `U` steps into runs of `R` steps;[^2] the enumeration of the variations never closed into a formula.[^3]

## Convexity

Every castle is column-convex: each column is one vertical run of cells from row 1 ([[column-convex-polyomino](pages/column-convex-polyomino.md)]). A castle is row-convex, each row a single block ([[horizontally-convex-polyomino](pages/horizontally-convex-polyomino.md)]), exactly when its skyline is unimodal: the columns with `c_i ≥ r` form an interval for every `r` if and only if the skyline is unimodal. So the convex castles are the castles that are both row-convex and column-convex.[^4] The brute-force module counts them by block parity.[^5]

## Block count

**Proposition.** A castle of height `h` has at least `h` blocks, with equality exactly when it is convex.[^6]

*Proof.* Let `p` be the first column of height `h`, and `c_0 = 0`. The block count is the total ascent `Σ_{i=1}^{w} max(0, c_i − c_{i−1})` ([[castle-polyomino](pages/castle-polyomino.md)], section *Blocks*). The terms with `i ≤ p` add up to at least `c_p − c_0 = h`, with equality exactly when `c_1 ≤ ⋯ ≤ c_p`, and the terms with `i > p` are nonnegative, with sum 0 exactly when `c_p ≥ ⋯ ≥ c_w`.

So the convex castles are the castles of height `h` with the fewest blocks, and every convex castle of height `h` has `h` blocks. Hence `A^e_convex(w, h) = A_convex(w, h)` and `A^o_convex(w, h) = 0` for even `h`, and the reverse for odd `h`. The semi-perimeter of a castle is `w + blocks` ([[castle-perimeter](pages/castle-perimeter.md)]), so the Proposition says that a castle's perimeter is at least `2(w + h)`, the perimeter of its bounding box, with equality exactly when it is convex.

## Count

**Theorem.** `A_convex(w, h) = C(2h + w − 3, w − 1)`, where `C(m, k) = m! / (k! (m − k)!)`.

*Proof.* The word of a convex castle of width `w` and height `h` has `h` letters `U`, `h` letters `D` and `w` letters `R`, and one `R` stands in the middle. Start from the word `U^h R D^h` and place the other `w − 1` letters `R` in `2h − 1` slots: the `h − 1` gaps between consecutive `U`s, the middle, and the `h − 1` gaps between consecutive `D`s. No `R` goes before the first `U` or after the last `D`. Placing `w − 1` identical letters in `2h − 1` slots, with repetition, can be done in `C(w − 1 + 2h − 2, w − 1)` ways.[^7]

At `w = 5`, `h = 4` this gives `C(10, 4) = 210`.[^8] [[convex-castle-binomial-identity](pages/convex-castle-binomial-identity.md)] gives a second proof, by splitting the skyline at its first column of height `h`.

| `A_convex(w, h)` | `h = 1` | `h = 2` | `h = 3` | `h = 4` | `h = 5` |
|---|---|---|---|---|---|
| `w = 1` | 1 | 1 | 1 | 1 | 1 |
| `w = 2` | 1 | 3 | 5 | 7 | 9 |
| `w = 3` | 1 | 6 | 15 | 28 | 45 |
| `w = 4` | 1 | 10 | 35 | 84 | 165 |
| `w = 5` | 1 | 15 | 70 | 210 | 495 |

Every entry agrees with brute-force enumeration.[^9]

## Other gradings

**Area.** A convex castle of area `n` is a weakly unimodal composition of `n`, so the convex castles of area `n` number `A001523(n)`, the stacks or weakly unimodal compositions ([[weakly-unimodal-composition](pages/weakly-unimodal-composition.md)]). [[castle-by-area](pages/castle-by-area.md)] splits them by block parity.[^10]

**Perimeter.** A convex castle is a stack polyomino in the sense of Delest and Viennot: a convex polyomino that contains both bottom corners of its bounding box ([[convex-polyomino](pages/convex-polyomino.md)]). They code stacks by Fibonacci words, writing `a` for each vertical step and `xx` for each East step, and the word of a convex castle is its `U`/`R`/`D` word with `U` and `D` written `a` and `R` written `xx`.[^11] Their Lemma 3.2 counts the stacks of perimeter `2n + 4` by the Fibonacci number they write `F_{2n}`, with `F_0 = F_1 = 1`; in the usual indexing `F_1 = F_2 = 1` this is `F_{2n+1}`.[^12] A convex castle of width `w` and height `h` has perimeter `2(w + h)`, so for `n ≥ 1`

```
Σ_{w + h = n + 2}  C(2h + w − 3, w − 1)  =  F_{2n+1}  =  A001519(n + 1):    2, 5, 13, 34, 89, …
```

which agrees with the binomial sums for `n ≤ 14`.[^9] With the block sign, the signed count of convex castles of semi-perimeter `s = w + h` is `Σ_{w+h=s} (−1)^h C(2h + w − 3, w − 1)`, with generating function `−t²(1 − t)/(1 − t + t²)`: the values `−1, 0, 1, 1, 0, −1` from `s = 2`, repeating with period 6. The even-block convex castles of semi-perimeter `s` are half the sum of `A001519(s − 1)` and the signed count: `0, 1, 3, 7, 17, 44, 116, 305, …` for `s = 2, 3, 4, …` ([[castle-perimeter](pages/castle-perimeter.md)]).[^9]

Delest and Viennot cut every convex polyomino by two vertical lines into a parallelogram polyomino and two stacks ([[stack-polyomino-gf](pages/stack-polyomino-gf.md)], [[bender-1974-convex-n-ominoes](pages/bender-1974-convex-n-ominoes.md)]).

## Castles over a convex core

Every castle `c` lies under a unique smallest convex castle, its **convex core** `u`, with `u_i = min(max(c_1, …, c_i), max(c_i, …, c_w))`. The core of `(2, 1, 2)` is `(2, 2, 2)`. On a plateau of `u`, a maximal run of `l` columns at height `m`, the castles over `u` may lower `l − 1` columns, or `max(l − 2, 0)` on the plateau at height `h`, to any height in `{1, …, m}`. So the castles over `u` number `Π m^{free}` over the plateaus, with `free` the number of columns that may be lowered, and the sum of `(−1)^{blocks}` over them is `(−1)^h Π P(m − 1, free)`. Summing over the `C(2h + w − 3, w − 1)` cores gives `A(w, h)` and the signed count `S(w, h)` ([[convex-core](pages/convex-core.md)]).[^9]

## Appearances in Sources

- [[project-euler-502-representations](pages/project-euler-502-representations.md)] - the front, middle and back of a convex castle's word, the count `C(2h + w − 3, w − 1)` by stars and bars, and the other castles as variations of convex castles.
- [[project-euler-502-solution](pages/project-euler-502-solution.md)] - the enumeration of the variations of convex castles, which never resolved into a formula.
- [[project-euler-502-brute-force](pages/project-euler-502-brute-force.md)] - the unimodality test and the counts of unimodal skylines by block parity.
- [[oeis-encyclopedia](pages/oeis-encyclopedia.md)] - `A001523`, the weakly unimodal compositions, which are the convex castles by area.
- [[algebraic-languages-and-polyominoes-enumeration](pages/algebraic-languages-and-polyominoes-enumeration.md)] - stack polyominoes, their Fibonacci words, and their count by perimeter.
- [[bender-1974-convex-n-ominoes](pages/bender-1974-convex-n-ominoes.md)] - trapezoids, rows nested over a full bottom row, which are the convex castles.

## Related Concepts

- [[convex-castle-binomial-identity](pages/convex-castle-binomial-identity.md)] - the proof of `A_convex(w, h) = C(2h + w − 3, w − 1)` by splitting the skyline and the Vandermonde convolution.
- [[convex-core](pages/convex-core.md)] - the convex core of a castle, and the castles over a core counted by products of `T` and `P`.
- [[castle-polyomino](pages/castle-polyomino.md)] - the castle definition and the block count.
- [[brick-wall-castles](pages/brick-wall-castles.md)] - the block fountains, the brick-wall castles with one block per row, are the convex castles among the sheared walls, `F_{2w−1}` of width `w`.
- [[urd-step-strings](pages/urd-step-strings.md)] - the `U`/`R`/`D` words of castles, sorted into rectangular castles, convex castles and their variations.
- [[castle-classification-shape](pages/castle-classification-shape.md)] - the shape types of castles, among them the unimodal type, which is the convex castles.
- [[weakly-unimodal-composition](pages/weakly-unimodal-composition.md)] - the convex castles of area `n`, counted by `A001523(n)`.
- [[stack-polyomino-gf](pages/stack-polyomino-gf.md)] - the generating function of `A001523` from a decomposition at the first tallest column, by the symbolic method.
- [[castle-perimeter](pages/castle-perimeter.md)] - the semi-perimeter `w + blocks`, and castles and convex castles counted by semi-perimeter, unsigned and signed.
- [[column-convex-polyomino](pages/column-convex-polyomino.md)] - the column-convexity that every castle has.
- [[horizontally-convex-polyomino](pages/horizontally-convex-polyomino.md)] - the row-convexity that makes a castle convex.
- [[convex-polyomino](pages/convex-polyomino.md)] - polyominoes that are row-convex and column-convex; the convex castles are its stacks, and a row-convex shape has as many blocks as rows.
- [[convex-polyomino-by-area](pages/convex-polyomino-by-area.md)] - the families of convex polyominoes counted by area, with the convex castles as the stacks.
- [[column-convex-polygon-enumeration](pages/column-convex-polygon-enumeration.md)] - the add-a-column method, which counts stacks by perimeter and area (its Lemmas 2.4 and 2.5).
- [[hoodoo-monadnock-castles](pages/hoodoo-monadnock-castles.md)] - two families of convex castles whose sides are partitions into distinct parts; at fixed width they are a fraction of the convex castles that tends to a constant as `h` grows.
- [[euler-castles](pages/euler-castles.md)] - the convex castles that fall by 0 or 1 at each step to height 1, whose rows are partitions into distinct parts; their block parity by area is Euler's pentagonal series.
- [[aocp-binomial-coefficients](pages/aocp-binomial-coefficients.md)] - Vandermonde's convolution, Knuth's equation (21).
- [[aocp-multinomial-coefficients](pages/aocp-multinomial-coefficients.md)] - the multinomial coefficient, of which the stars-and-bars count is a case.

## Footnotes

[^1]: [[project-euler-502-representations](pages/project-euler-502-representations.md)] §"Steps-Based Approach" L86-91 - "The next type of castle is what we will call a convex castle. This type of castle can be split into three portions: the front, the middle, and the back", "The front of the castle consists of interspersed U and R steps, until the castle reaches its maximum height. No D steps are present in the front part. The middle of the castle consists of any R steps taken at the maximum height. There must be at least one R step in the middle. The back of the castle consists of interspersed D and R steps, until the castle reaches its base. No U steps are present in the back part. The convex castle must begin with a U and end with a D".
[^2]: [[project-euler-502-representations](pages/project-euler-502-representations.md)] §"Steps-Based Approach" L109 - "Finally, we can classify all remaining castles as variations on convex castles. To construct variations on castles, we look for runs of RRRs of length 3 or more."
[^3]: [[project-euler-502-solution](pages/project-euler-502-solution.md)] §"What was tried and did not work" L190 - "U/R/D convex-castle enumeration. Conceptually clean, but the case analysis to enumerate variations of a convex castle never resolved into a formula."
[^4]: [[project-euler-502-brute-force](pages/project-euler-502-brute-force.md)] §"brute" L54 - "conv_even, conv_odd - the same, restricted to unimodal skylines (column-convex AND row-convex)". Verified by execution (Python 3.11, 2026-10-25): a skyline is row-convex exactly when it is unimodal, for `w ≤ 8`, `h ≤ 6` with `h^w ≤ 400000`.
[^5]: [[project-euler-502-brute-force](pages/project-euler-502-brute-force.md)] §"brute" L54-67 - "conv_even, conv_odd - the same, restricted to unimodal skylines (column-convex AND row-convex)" and the test "walk up, then walk down; accept iff the walk covers the whole tuple".
[^6]: [[project-euler-502-representations](pages/project-euler-502-representations.md)] §"Steps-Based Approach" L88-90, §"Step 1 Bare Minimum String" L153 [synthesis] - the word of a convex castle has a front with "No D steps" and a back with "No U steps", so one `U` per row, and "The bare minimum string consists of the minimum number of Us and Ds that the castle is required to have". Verified by execution (Python 3.11, 2026-10-25): every skyline of height `h` has at least `h` blocks, with equality exactly when it is unimodal, for `w ≤ 8`, `h ≤ 6` with `h^w ≤ 400000`.
[^7]: [[project-euler-502-representations](pages/project-euler-502-representations.md)] §"Step 2 Enumerating Convex Castles" L169-194 [synthesis] - the source starts from the bare-minimum string, inserts `W − 1` letters `R` into `2(H − 1) + 1` partitions (`H − 1` between the `U`s, `H − 1` between the `D`s, one between the two runs), counts them by stars and bars, and states "CCC = C(2(H-1)+W-1, W-1) = C(2H+W-3, W-1)", with `W`, `H` for `w`, `h`.
[^8]: [[project-euler-502-representations](pages/project-euler-502-representations.md)] §"Step 2 Enumerating Convex Castles" L206-209 - "CCC = C(2H + W - 3, W-1) = C(2*4 + 5 - 3, 5-1) = C(10, 4) = 210 Meaning, on a grid of height 4 and width 5, there are 210 convex castles."
[^9]: Verified by execution (Python 3.11, 2026-10-16): `A_convex(w, h)` against enumeration of all skylines for `w ≤ 7`, `h ≤ 6` with `h^w ≤ 300000`, which also checks the Proposition; the anti-diagonal sums against `F_{2n+1}` for `n ≤ 14`; the signed count by semi-perimeter for `s ≤ 15` against the series of `−t²(1 − t)/(1 − t + t²)`, and the even-block counts for `s ≤ 11`; the convex cores, the count `Π m^{free}` and the signed sum `(−1)^h Π P(m − 1, free)` over every core for `w ≤ 6`, `2 ≤ h ≤ 4`.
[^10]: https://oeis.org/A001523 (read 2026-10-25) - "Number of stacks, or planar partitions of n; also number of weakly unimodal compositions of n." Verified by execution (Python 3.11, 2026-10-25): the unimodal compositions of `n` number `A001523(n)` for `n ≤ 15`.
[^11]: [[algebraic-languages-and-polyominoes-enumeration](pages/algebraic-languages-and-polyominoes-enumeration.md)] pp.180-181 (16)-(18), Fig. 7 [synthesis] - Φ writes "the letter 'a' (respectively the factor xx) each time one meets a North or South step (respectively an East step)", "the first (respectively last) letter of w is 'a'", and there is "a factor xx" after the rising a's; the identification with the `U`/`R`/`D` word is own reasoning.
[^12]: [[algebraic-languages-and-polyominoes-enumeration](pages/algebraic-languages-and-polyominoes-enumeration.md)] p.181 Lemma 3.2 - "The number of stack polyominoes with perimeter 2n+4 is the Fibonacci number F_{2n}"; the sum over `w + h = n + 2` is own reasoning from the perimeter `2(w + h)`.
