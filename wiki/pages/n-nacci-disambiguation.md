---
title: n-nacci disambiguation - Fibonacci, tribonacci, tetranacci, … on the wiki
category: Concepts
summary: Every place the wiki meets the Fibonacci, tribonacci, tetranacci and higher n-nacci numbers or their growth constants, grouped by the mechanism that produces them, with a note on which appearances share a mechanism and which do not. Fibonacci - the Fibonacci castles (F_{w+2} − 1 at width w) and, with q marking area, the q-Fibonacci castles (different from the tiling q-Fibonacci polynomials), the castles of height 2 by area (F_{A+1} − 1, the same numbers through a width-to-area bijection), prime castles (F_{n−1}), the bisections A001519 and A001906 (stacks by perimeter, sandpile ladders, growth φ²), the trisection of δ_4 = φ³, φ inside larger counts, Fibonacci as a worked example, and neighboring recurrences (tree skylines, fractional recurrences, Narayana's cows). Tribonacci - the castles of height 3 by area, τ as the ceiling by area at height 3, τ as a growth constant by width through a forced-descent rule that extends the Fibonacci castle rule, and τ² for castles by semi-perimeter. Tetranacci and higher - castles of height h by area, growth tending to 2.
tags: [concept, disambiguation, fibonacci, tribonacci, tetranacci, pentanacci, n-nacci, growth-constant, composition, index]
sources: [algebraic-languages-and-polyominoes-enumeration, dhar-ruelle-sen-verma-1995-algebraic-aspects, aocp-generating-functions, analytic-combinatorics-ch1-ogfs]
created: 2026-10-02
updated: 2026-10-16
---

# n-nacci disambiguation

The Fibonacci numbers and their higher-order relatives come up on many wiki pages, for different reasons. This page lists every appearance, grouped by the mechanism that produces it, and says for each group whether it is tied to the others or only shares the numbers.

Conventions: `F_1 = F_2 = 1`. `φ = 1.6180…` is the root of `x² = x + 1`, and `τ = 1.8393…`, the tribonacci constant, is the real root of `x³ = x² + x + 1`. The `h`-nacci constant is the root in `(1, 2)` of `x^h = x^{h−1} + ⋯ + x + 1`. A castle of height `h` has a column of height `h`; skylines and strips on the heights `1, …, h` need not reach `h`.

## The common spine

Most castle appearances of the n-nacci numbers come from one fact. A castle of area `A` is a composition of `A`, its column heights read left to right ([[castle-representations](pages/castle-representations.md)]), and the castles of height `h` are the compositions whose largest part is `h`. Compositions with parts at most `h` are counted by the `h`-nacci numbers, so

```
#{castles of height h and area A}  =  (compositions of A, parts ≤ h)  −  (compositions of A, parts ≤ h − 1),
```

and the count grows like the `h`-nacci constant ([[exact-height-castle-by-area](pages/exact-height-castle-by-area.md)]). The first terms, `A = 1, 2, …`:[^exec]

| `h` | castles of height `h` by area | closed form | growth |
|---|---|---|---|
| 2 | `0, 1, 2, 4, 7, 12, 20, 33, 54, 88, 143, 232` | `F_{A+1} − 1` | `φ` |
| 3 | `0, 0, 1, 2, 5, 11, 23, 47, 94, 185, 360, 694` | `A000073(A+2) − F_{A+1}` | `τ` |
| 4 | `0, 0, 0, 1, 2, 5, 12, 27, 59, 127, 269, 563` | `A000078(A+3) − A000073(A+2)` | `1.9276…` |
| 5 | `0, 0, 0, 0, 1, 2, 5, 12, 28, 63, 139, 303` | `A001591(A+4) − A000078(A+3)` | `1.9659…` |

With no bound on the height the count is `2^{A−1}` and the growth is `2` ([[castle-by-area](pages/castle-by-area.md)]). The section headings marked "on the spine" are the entries that come from it.

## Fibonacci

### 1. A height-2 column is followed by a height-1 column (on the spine)

These counts all come from the transfer matrix `[[1, 1], [1, 0]]` on the heights `{1, 2}`, the first entry of [[reachable-field-census](pages/reachable-field-census.md)], and they are linked by explicit maps.

- **Fibonacci castles.** Height 2, no two adjacent height-2 columns. There are `F_{w+2} − 1` of width `w`, golden by width ([[fibonacci-castle](pages/fibonacci-castle.md)], [[castle-classification-shape](pages/castle-classification-shape.md)], [[castle-classification-growth](pages/castle-classification-growth.md)], [[castle-notation](pages/castle-notation.md)]). They are the tree castles of height 2 ([[castle-graph](pages/castle-graph.md)], [[castle-classification-spectrum](pages/castle-classification-spectrum.md)]). [[tree-castle-by-area](pages/tree-castle-by-area.md)] splits them by the number `t ≥ 1` of height-2 columns into the triangle `C(w − t + 1, t)`.
- **Ridge castles of height 2.** Exchanging the heights 1 and 2 maps them onto the Fibonacci castles together with the flat row `(1, …, 1)`, so there are `F_{w+2}` of them for `w ≥ 2` ([[ridge-castle](pages/ridge-castle.md)], [[metallic-strip-realizability](pages/metallic-strip-realizability.md)]).
- **Trivial heaps on the path `P_w`.** With the path-graph dependency of [[viennot-heap-tower](pages/viennot-heap-tower.md)], under which pieces at columns `i` and `j` are dependent when `|i − j| ≤ 1`, the trivial heaps are the independent sets of `P_w`: the sets of height-2 columns of the Fibonacci castles of width `w`, together with the empty set, `F_{w+2}` in all.
- **Castles of height 2 by area.** `F_{A+1} − 1`, the row `h = 2` of the spine table ([[exact-height-castle-by-area](pages/exact-height-castle-by-area.md)]). These are the Fibonacci castles shifted by one: append a height-1 column to a Fibonacci castle of width `w`, read each height-2 column together with the height-1 column after it as a part 2, and each remaining height-1 column as a part 1. This is a bijection from the Fibonacci castles of width `w` onto the castles of height 2 and area `w + 1`. Example: `(1, 2, 1, 1, 2)` becomes `(1, 2, 1, 2)`.[^exec]
- **Single-block peaks.** In the table of castles by area, blocks and peaks on [[odd-castles-and-block-tables](pages/odd-castles-and-block-tables.md)], the diagonal "blocks = peaks + 1", where every peak is a single block, consists of the skylines of height at most 2, `F_{A+1}` of area `A`: the castles of height 2 and the flat row.

**The q-Fibonacci castles count area.** Counting the Fibonacci castles with a variable `q` for area gives the q-Fibonacci castles ([[q-fibonacci-castle](pages/q-fibonacci-castle.md)]): at width `w` the polynomial is `q^w (f_w(q) − 1)` with `f_w(q) = Σ_m C(w − m + 1, m) q^m`. By number of cells there are `1, 2, 3, 5, 8, 12, 18, 27, 40, 59, 87, …` of them from 2 cells on, `A000930(n + 1) − 1` with `n` cells, one less than Narayana's cows, growing like the supergolden constant `1.4656…`.[^exec] These are different from the tiling q-Fibonacci polynomials (section 8).

### 2. Castles with no height-1 column (a different composition class)

- **Prime castles.** The castles with no height-1 column are the primes of the gluing monoid, `F_{n−1}` of area `n`, and the composite castles number `2^{n−1} − F_{n−1}` ([[prime-castles](pages/prime-castles.md)], [[castle-by-area](pages/castle-by-area.md)]). They are the compositions into parts at least 2, a different class from section 1 with the same numbers after a shift. The growth `φ` needs the height unbounded: the prime castles of height `h` by area grow like the largest root of `x^h = x^{h−2} + ⋯ + x + 1`, the plastic number at `h = 3` and the supergolden constant at `h = 4`, increasing to `φ`.[^exec]
- **One-peak castles.** A one-peak castle is a prime castle with a run of height-1 columns, possibly empty, on each side, so its count by area is `A001924(n − 1)`, the Fibonacci numbers summed twice ([[castle-row-raising-equation](pages/castle-row-raising-equation.md)]).
- **Prime convex castles.** By area they agree with `F_{n−1}` through `n = 7` and fall below from `n = 8`, where the skyline `(3, 2, 3)` is the smallest prime castle that is not unimodal ([[prime-convex-castles](pages/prime-convex-castles.md)]).

### 3. Bisections: growth φ²

The odd-index and even-index halves of the Fibonacci sequence, each growing like `φ²`. The wiki has no map linking these to section 1.

- **Stacks by perimeter, A001519.** Convex castles (stack polyominoes) by semi-perimeter `s` number `1, 2, 5, 13, 34, …` from `s = 2`, which is `A001519(s − 1) = F_{2s−3}`; Delest and Viennot code them by Fibonacci words and write the count as `F_{2n}` with `F_0 = F_1 = 1` ([[algebraic-languages-and-polyominoes-enumeration](pages/algebraic-languages-and-polyominoes-enumeration.md)], [[convex-castle](pages/convex-castle.md)], [[convex-castle-binomial-identity](pages/convex-castle-binomial-identity.md)], [[stack-polyomino-gf](pages/stack-polyomino-gf.md)], [[castle-perimeter](pages/castle-perimeter.md)], where the signed count has period 6, [[polyominoes](pages/polyominoes.md)], [[convex-polyomino](pages/convex-polyomino.md)]).
- **Sandpile ladders, A001906.** In the tide model the sandpile group of the castle `(2, 2, …, 2)` of width `w` has order `F_{2w}` ([[sandpile-group](pages/sandpile-group.md)]). The same numbers `m_x = F_{2x}` enter Dhar, Ruelle, Sen and Verma's group of the `L × 2` strip, the planar dual of the castle `(3, …, 3)` of width `L + 1` in the sink model ([[dhar-ruelle-sen-verma-1995-algebraic-aspects](pages/dhar-ruelle-sen-verma-1995-algebraic-aspects.md)], [[sandpile-census](pages/sandpile-census.md)]). The series `1/(1 − 3x + x²)` of A001906 is also the inverse of the Cartier-Foata series of the heaps of intervals in `[1, 2]` on [[viennot-heap-tower](pages/viennot-heap-tower.md)].
- **Motzkin-path strips on four heights.** The Motzkin-path strips on the heights `1, …, 4` (1-smooth, both end columns at height 1) grow like `φ²`, because `1 + 2cos(π/5) = φ²`, and number `A005207(w − 1)` ([[motzkin-castles](pages/motzkin-castles.md)]).

### 4. Trisection: δ_4 = φ³

All from `δ_4 = 2 + √5 = φ³`, which lies in `Q(√5)`.

- The ridge strips of height 5 number `𝟙ᵀR_5^{w−1}𝟙 = F_{3w+2} = A015448(w + 1)` (`5, 21, 89, 377, …`), and grow like `δ_4` ([[ridge-castle](pages/ridge-castle.md)], [[metallic-strip-realizability](pages/metallic-strip-realizability.md)], [[reachable-field-census](pages/reachable-field-census.md)]).
- The metallic sequence of `δ_4` is `F_{3n}/2`, A001076 ([[metallic-means](pages/metallic-means.md)], [[castle-eigenvalue-oeis-crosswalk](pages/castle-eigenvalue-oeis-crosswalk.md)]).
- An odd power of a metallic mean is a metallic mean: `δ_a^n` has trace an integer `b` and norm `−1`, so it is `δ_b`. So `φ⁵ = δ_11`, and since `φ⁵ = 5φ + 3`, the index of `Z[δ_11]` in `Z[φ]` is `F_5 = 5` ([[metallic-means](pages/metallic-means.md)], [[castle-snippets-number-theory](pages/castle-snippets-number-theory.md)]).

### 5. φ or Fibonacci inside a larger count

These share the constant with section 1, but the wiki gives no map to it at the level of castles.

- **Tree skylines by area.** The tree skylines of height at most 3 by area, `A006498(n + 1)`, grow like `φ`, because their denominator factors as `(1 + q²)(1 − q − q²)`, and `A006498(2n) = F_{n+1}²`; the tree castles of height 3 are their differences with the row of height at most 2 and grow at the same rate ([[tree-castle-by-area](pages/tree-castle-by-area.md)]). Banning `2 × 2` blocks lowers the growth by area at height 3 from `τ` to `φ` ([[castle-classification-growth](pages/castle-classification-growth.md)]).
- **Signed Motzkin castles.** The signed count is `A343773(n) = (−1)^n A007440(n + 1)`, where A007440 is the reversion of the Fibonacci generating function ([[motzkin-castles](pages/motzkin-castles.md)]).
- **Tower parity sectors.** The factors `H_d(μ) = Σ_i (−1)^i C(⌊(d + i)/2⌋, i) μ^{d−i}` of [[tower-parity-sectors](pages/tower-parity-sectors.md)] take Fibonacci values at `μ = ±1`: `H_d(1) = (−1)^d F_{d−1}` and `H_d(−1) = (−1)^d F_{d+2}`.[^exec]
- **The second-difference rule.** The strip rule `|c_n − 2c_{n−1} + c_{n−2}| ≤ 1` on the heights `{1, 2}`, the case `α = 2` of the power-law memory rules, grows like `φ` ([[power-law-memory-rules](pages/power-law-memory-rules.md)]).

### 6. Fibonacci as a worked example or an algebraic tool

No castle count here. Fibonacci is the example used to teach a method, or a recurrence that shows up in the algebra.

- **Recurrence to rational generating function to closed form** (Knuth's Fibonacci method, Binet's formula): [[aocp-generating-functions](pages/aocp-generating-functions.md)], [[generating-functions](pages/generating-functions.md)], [[generating-functions-topic](pages/generating-functions-topic.md)], [[symbolic-method](pages/symbolic-method.md)], [[signed-tower-count](pages/signed-tower-count.md)], [[algebraic-transcendental-wall](pages/algebraic-transcendental-wall.md)].
- **Fast far-off terms:** [[kitamasa](pages/kitamasa.md)] is taught on Fibonacci by hand.
- **Continued fractions and convergents:** `φ = [1; 1, 1, …]` with Fibonacci convergents, and the Lucas numbers as the traces of `φ^n`: [[eigenvalue-continued-fractions](pages/eigenvalue-continued-fractions.md)], [[castle-eigenvalue-oeis-crosswalk](pages/castle-eigenvalue-oeis-crosswalk.md)].
- **The Pell parallel** (golden, `a = 1`, against silver, `a = 2`): [[pell-numbers](pages/pell-numbers.md)], [[pell-castle-strip](pages/pell-castle-strip.md)], [[metallic-means](pages/metallic-means.md)].
- **Orders mod `p`** (Pisano-type periods): [[castle-eigenvalue-oeis-crosswalk](pages/castle-eigenvalue-oeis-crosswalk.md)], [[castle-snippets-number-theory](pages/castle-snippets-number-theory.md)].
- **Fibonacci recurrences in polynomial algebra:** modulo 2 the rescaled `char_k` satisfies the Fibonacci-type recurrence `q_{k+1} = q_k + t·q_{k−1}` over `F_2[t]`, `t = μ²` ([[char-k-eisenstein-at-two](pages/char-k-eisenstein-at-two.md)]), and the mod-3 evaluation of `char_k` at `±1` satisfies a Fibonacci-like scalar recurrence ([[mod-9-coset-lift](pages/mod-9-coset-lift.md)]).
- **Entropy:** `log₂ φ = 0.694` bits per column for the Fibonacci castles ([[castle-entropy](pages/castle-entropy.md)]).

### 7. Neighboring recurrences with other growth constants

- **Tree skylines of height at most `h` by width.** They satisfy `a(n) = a(n − 1) + (h − 1)a(n − 2)`, giving `A001045(w + 2)` (Jacobsthal) at `h = 3`, `A006130(w + 1)` at `h = 4` and `A006131(w + 1)` at `h = 5`, and grow like `σ_1^{h−1} = (1 + √(4h − 3))/2`; the tree castles of height `h` are the differences of consecutive rows and grow at the same rate ([[castle-graph](pages/castle-graph.md)], [[castle-classification-growth](pages/castle-classification-growth.md)]).[^exec] This is one way to extend the Fibonacci castles to higher `h`, and it leads to quadratic constants, not to the n-nacci ones.
- **Ridge castles of height `h ≥ 3`.** The other extension by width, through the metallic means: silver by width at `h = 3`, bronze at `h = 4`, `δ_4` at `h = 5` ([[ridge-castle](pages/ridge-castle.md)], [[metallic-strip-realizability](pages/metallic-strip-realizability.md)]).
- **Fractional recurrences.** With `∇^α` the Grunwald-Letnikov difference of order `α`, the recurrence `∇^α a_n = a_{n−1}` has growth `φ` exactly at `α = 1/2`, and the recurrence `∇^α a_n = a_{n−1} + a_{n−2}` is the Fibonacci recurrence at `α = 0` and the Pell recurrence at `α = 1`, with growth increasing from `φ` ([[fractional-recurrences](pages/fractional-recurrences.md)]).
- **Padovan and Perrin.** The impulse-response and trace sequences of the plastic number, as Fibonacci and Lucas are for `φ`, with the recurrence `a(n) = a(n − 2) + a(n − 3)` ([[plastic-number](pages/plastic-number.md)]).
- **Narayana's cows.** `a(n) = a(n − 1) + a(n − 3)` (A000930), one more than the number of q-Fibonacci castles with `n − 1` cells (section 1).

### 8. q-Fibonacci castles and the tiling q-Fibonacci polynomials

Two families of polynomials in `q` give Fibonacci numbers at `q = 1`, and both can be read on the second rows of Fibonacci castles (0/1 strings of length `w` with no two adjacent 1s), but `q` counts different things:

| | what `q` counts | polynomial (second rows of length `w`) | at `w = 3` | where |
|---|---|---|---|---|
| **q-Fibonacci castles** | area: the castle's cells, `w` plus the number of height-2 columns | `q^w f_w(q)`, `f_w = f_{w−1} + q f_{w−2}` | `q³(1 + 3q + q²)` | [[q-fibonacci-castle](pages/q-fibonacci-castle.md)] |
| **tiling q-Fibonacci polynomials** | the sum of the positions of the height-2 columns (a domino at position `i` weighs `q^i`) | `f^C_{w+2}(q)`, `f^C_{n+1} = f^C_n + q^{n−1} f^C_{n−1}` | `1 + q + q² + q³ + q⁴` | [[q-fibonacci-castle](pages/q-fibonacci-castle.md)] |

Lindgren, Ngo and Segroves call the second family "the standard q-analogue" of the Fibonacci numbers.[^tiling] On this wiki "q-Fibonacci castle" always means the area version, in line with the other area q-analogues such as the Pólya-Gessel q-Catalan numbers ([[q-catalan-numbers](pages/q-catalan-numbers.md)]).

## Tribonacci

### 1. Castles of height 3 by area (on the spine)

`A000073(A + 2) − F_{A+1} = 1, 2, 5, 11, 23, 47, 94, 185, …` from area 3, growing like `τ` ([[exact-height-castle-by-area](pages/exact-height-castle-by-area.md)]).[^exec] The skylines of height at most 3 by area, `A000073(A + 2)`, are computed by `bounded_castles_by_area` on [[castle-snippets-strips](pages/castle-snippets-strips.md)], which also shows that `nearest_metallic` returns golden for them at distance `0.222`, since `τ` is cubic and every `δ_a` quadratic. The OEIS status is on [[castle-sequence-catalogue](pages/castle-sequence-catalogue.md)], the growth type "tribonacci by area" on [[castle-classification-growth](pages/castle-classification-growth.md)] and [[castle-classification](pages/castle-classification.md)], and the entropy `log₂ τ = 0.879` bits per cell on [[castle-entropy](pages/castle-entropy.md)].

### 2. The ceiling by area at height 3 (on the spine)

A strip rule on the heights `1, 2, 3` counts a subset of the compositions with parts at most 3, so its growth constant by area is at most `τ`. The all-ones rule attains it, and `τ` cannot occur at height 2 ([[area-growth-census](pages/area-growth-census.md)]). Banning `2 × 2` blocks lowers the constant from `τ` to `φ` (Fibonacci, section 5).

### 3. τ as a growth constant by width (on the spine)

[[reachable-field-census](pages/reachable-field-census.md)] lists `τ` among the nine cubic Perron roots of 0/1 strip matrices at height 3. One rule that realizes it extends the Fibonacci castle rule:

- **Rule.** Heights `1, 2, 3`. A column of height `k ≥ 2` is followed by one of height `k − 1`; after a height-1 column any height may follow. So every tall column starts a forced descent `k, k − 1, …, 1`, which may be cut off at the right end. Example of width 8: the skyline `(1, 3, 2, 1, 2, 1, 1, 3)`.
- **Transfer matrix.** The companion matrix of `x³ − x² − x − 1`, with rows `1 → {1, 2, 3}`, `2 → {1}`, `3 → {2}`. Its Perron root is `τ`.
- **Count.** The castles of height 3 of this rule number `1, 2, 4, 9, 18, 36, 71, 138, 266, 509, …` at widths `1, 2, …`, and the ratio of successive terms is `1.839295` at `w = 79`. With the last column required to have height 1, each forced descent is one part, so the castles of width `w` correspond to the castles of height 3 and area `w` of section 1, `A000073(w + 2) − F_{w+1}` of them.[^exec]
- **At height 2** the rule says that a height-2 column is followed by a height-1 column. That is the Fibonacci castle rule, and the end-at-height-1 bijection is the one of Fibonacci section 1 with the appended column. The same rule and bijection work at every height (checked through `h = 5`).[^exec]

### 4. Castles by perimeter: τ² and τ (not on the spine)

The castles by semi-perimeter (the bargraphs, A082582) grow like `τ²`, and their signed count like `τ` ([[castle-perimeter](pages/castle-perimeter.md)]); [[castle-sign-kms-matrix](pages/castle-sign-kms-matrix.md)] obtains both cubics from one norm form, and [[castle-sequence-catalogue](pages/castle-sequence-catalogue.md)] lists the series. The convex castles by perimeter grow like `φ²` (Fibonacci, section 3). The wiki has no map from compositions to either of these constants.

## Tetranacci, pentanacci, and higher

- **Castles of height `h ≥ 4` by area.** The rows `h = 4` and `5` of the spine table, growing like the tetranacci constant `1.9276…`, the pentanacci constant `1.9659…`, and so on toward `2` ([[exact-height-castle-by-area](pages/exact-height-castle-by-area.md)], [[castle-sequence-catalogue](pages/castle-sequence-catalogue.md)], [[castle-classification-growth](pages/castle-classification-growth.md)], [[castle-snippets-strips](pages/castle-snippets-strips.md)]).
- **The ceiling at height `h`.** The `h`-nacci constant bounds the growth by area of every strip rule on `h` heights (the tetranacci constant first appears at height 4). So a constant by area needs at least the first height whose `h`-nacci constant reaches it, the ceiling bound, one of the two lower bounds on the minimum height on [[area-growth-census](pages/area-growth-census.md)].
- **Width.** The forced-descent rule of tribonacci section 3, on `h` heights, has the companion matrix of `x^h − x^{h−1} − ⋯ − 1` as its transfer matrix.
- **Bounded parts in general.** Flajolet and Sedgewick's compositions with parts in `{1, …, r}` have ordinary generating function `(1 − z)/(1 − 2z + z^{r+1})` ([[analytic-combinatorics-ch1-ogfs](pages/analytic-combinatorics-ch1-ogfs.md)]).
- **Not n-nacci.** With `2 × 2` blocks banned, the tree skylines of height at most 4 and area `n` number `A000570(n + 1)` (tournaments) instead of a tetranacci count ([[unique-tournament](pages/unique-tournament.md)], [[tree-castle-by-area](pages/tree-castle-by-area.md)]). With no bound on the height, the tree castles of area `n` number `A005251(n + 2)` and grow like `ψ²`, the square of the plastic number, not 2 ([[plastic-number](pages/plastic-number.md)]).[^exec]

## Related Concepts

- [[exact-height-castle-by-area](pages/exact-height-castle-by-area.md)] - the spine: castles by area as compositions with bounded parts.
- [[metallic-means](pages/metallic-means.md)] - de Spinadel's metallic means, whose first member is `φ` and which the n-nacci constants for `h ≥ 3` are not.
- [[castle-classification-growth](pages/castle-classification-growth.md)] - growth types such as "golden by width" and "tribonacci by area".
- [[castle-notation](pages/castle-notation.md)] - `τ` and the Fibonacci castle entries.
- [[oeis-index](pages/oeis-index.md)] - every A-number on this page, with the pages that cite it.

## Footnotes

[^exec]: Verified by execution (Python 3.11 with NumPy and SymPy, 2026-10-16), by brute force over skylines and compositions: the counts of castles of height `h = 2..5` by area for `A ≤ 14`, equal to the differences of consecutive n-nacci composition counts and to the closed forms; the append-a-column map, a bijection from the Fibonacci castles of width `w` onto the castles of height 2 and area `w + 1` for `w ≤ 13`; the ridge castles of height 2, `F_{w+2}` for `2 ≤ w ≤ 9`; the q-Fibonacci castles with `n = 2..14` cells, `1, 2, 3, 5, 8, 12, 18, 27, 40, 59, 87, 128, 188`, equal to `A000930(n + 1) − 1`; the growth of the prime castles of height 3, 4, 5 by area (`1.324718`, `1.465571`, `1.534158`); the forced-descent castles of height 3 by width for `w ≤ 10`, with the last column at height 1 equal to `A000073(w + 2) − F_{w+1}`, and by transfer matrix through `w = 80` with successive ratio `1.839295` at `w = 79`; the end-at-height-1 bijection with the compositions of `w` of largest part `h` for `h = 2, 3, 4` and `w ≤ 11`, and `h = 5` and `w ≤ 9`; `H_d(1) = (−1)^d F_{d−1}` and `H_d(−1) = (−1)^d F_{d+2}` for `d ≤ 11`; the tree skylines of height at most 3, 4, 5 by width for `w ≤ 7`, satisfying `a(n) = a(n − 1) + (h − 1)a(n − 2)`, with `A001045(w + 2)` at height 3; the tree skylines by area for `n ≤ 16`, of height at most 3 (`1, 2, 4, 6, 9, 15, 25, 40, 64, 104, 169, …`, denominator `1 − q − q³ − q⁴ = (1 + q²)(1 − q − q²)`), of height at most 4 (`A000570(n + 1)`) and of any height (`A005251(n + 2)`). OEIS offsets checked at https://oeis.org/A000930, https://oeis.org/A001924, https://oeis.org/A005251, https://oeis.org/A006130, https://oeis.org/A006131, https://oeis.org/A006498, https://oeis.org/A000570, https://oeis.org/A015448 and https://oeis.org/A343773.
[^tiling]: https://d31kydh6n6r5j5.cloudfront.net/uploads/sites/66/2019/04/Fibonacci_comps.pdf (E. Lindgren, M. A. Ngo, S. Segroves, "Weighted Tilings and q-Fibonacci Numbers", Carleton College, 2007) pp.1-2 - "A particular tiling's weight is the product of all q^i such that the tiling has a domino at position (i, i + 1)"; "we get the standard q-analogue: f_n+1(q) = f_n(q) + q^n−1 f_n−1(q), f_1(q) = f_2(q) = 1". The reading as the sum of the positions of the height-2 columns is verified on [[q-fibonacci-castle](pages/q-fibonacci-castle.md)].
