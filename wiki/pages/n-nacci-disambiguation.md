---
title: n-nacci disambiguation - Fibonacci, tribonacci, tetranacci, … on the wiki
category: Concepts
summary: Every place the wiki meets the Fibonacci, tribonacci, tetranacci and higher n-nacci numbers or their growth constants, grouped by the mechanism that produces them, with a note on which appearances share a mechanism and which are unrelated. Fibonacci - the Fibonacci castles by width (F_{w+2} − 1), all castles of exact height 2 by area (F_{A+1} − 1, the same numbers through a width-to-area bijection), prime castles (F_{n−1}), the bisections A001519 and A001906 (stacks by perimeter, sandpile ladders, growth φ²), the copper trisection (φ³), φ inside larger counts, Fibonacci as a worked example, and lookalikes (k-Fibonacci, fractional Fibonacci, Narayana's cows). Tribonacci - all castles of exact height 3 by area, τ as the height-3 area ceiling, τ as a width growth constant through a forced-descent rule that extends the Fibonacci castle rule, and the unrelated τ² of castles by perimeter. Tetranacci and higher - exact height h by area, growth tending to 2.
tags: [concept, disambiguation, fibonacci, tribonacci, tetranacci, pentanacci, n-nacci, growth-constant, composition, index]
sources: [algebraic-languages-and-polyominoes-enumeration, dhar-ruelle-sen-verma-1995-algebraic-aspects, aocp-generating-functions, analytic-combinatorics-ch1-ogfs]
created: 2026-10-02
updated: 2026-10-02
---

# n-nacci disambiguation

The Fibonacci numbers and their higher-order relatives come up on many wiki pages, for different reasons. This page lists every appearance, grouped by the mechanism that produces it, and says for each group whether it is tied to the others or only shares the name.

Conventions: `F_1 = F_2 = 1`. `φ = 1.6180…` is the root of `x² = x + 1`, and `τ = 1.8393…` (the tribonacci constant) is the root of `x³ = x² + x + 1`. The `h`-nacci constant is the root in `(1, 2)` of `x^h = x^{h−1} + ⋯ + x + 1`. Every castle family is stated at exact height.

## The common spine

Most castle appearances of the n-nacci numbers come from one fact. A castle of area `A` is a composition of `A` (its column heights, [[castle-representations](pages/castle-representations.md)]), and the castles of exact height `h` are the compositions whose largest part is exactly `h`. Compositions with parts at most `h` are counted by the `h`-nacci numbers, so

```
#{castles of exact height h and area A}  =  (compositions of A, parts ≤ h)  −  (compositions of A, parts ≤ h − 1),
```

and the count grows like the `h`-nacci constant ([[bounded-height-castles-nacci](pages/bounded-height-castles-nacci.md)]). The first terms, `A = 1, 2, …`:[^exec]

| `h` | exact-height-`h` castles by area | closed form | growth |
|---|---|---|---|
| 2 | `0, 1, 2, 4, 7, 12, 20, 33, 54, 88, 143, 232` | `F_{A+1} − 1` | `φ` |
| 3 | `0, 0, 1, 2, 5, 11, 23, 47, 94, 185, 360, 694` | `A000073(A+2) − F_{A+1}` | `τ` |
| 4 | `0, 0, 0, 1, 2, 5, 12, 27, 59, 127, 269, 563` | `A000078(A+3) − A000073(A+2)` | `1.9276…` |
| 5 | `0, 0, 0, 0, 1, 2, 5, 12, 28, 63, 139, 303` | `A001591(A+4) − A000078(A+3)` | `1.9659…` |

With no height restriction the count is `2^{A−1}` and the growth is `2` ([[castle-by-area](pages/castle-by-area.md)]). The sections below mark the entries that sit on this spine.

## Fibonacci

### 1. A height-2 column must be followed by a height-1 column (on the spine)

These counts all come from the transfer matrix `[[1,1],[1,0]]` on heights `{1, 2}`, the first entry of [[reachable-field-census](pages/reachable-field-census.md)]. They are linked by explicit maps.

- **Fibonacci castles.** Exact height 2, no two adjacent height-2 columns. There are `F_{w+2} − 1` of width `w`, growing like `φ`. Defined on [[castle-classification-shape](pages/castle-classification-shape.md)] (Axis 2) and [[castle-notation](pages/castle-notation.md)]. They are the tree castles of exact height 2 ([[castle-graph](pages/castle-graph.md)], [[castle-classification-spectrum](pages/castle-classification-spectrum.md)]), and [[castle-classification-growth](pages/castle-classification-growth.md)] files them as a golden width growth class. [[tree-castle-by-area](pages/tree-castle-by-area.md)] splits them by the number of height-2 columns `t` into the triangle `C(w − t + 1, t)`, with the all-1 row as `t = 0`.
- **Ridge castles of exact height 2.** Exchanging heights 1 and 2 maps them onto the Fibonacci castles plus the all-1 row, so there are `F_{w+2}` of them for `w ≥ 2` ([[metallic-strip-realizability](pages/metallic-strip-realizability.md)], [[castle-classification-shape](pages/castle-classification-shape.md)]).
- **Trivial heaps on the path `P_w`.** Independent sets of `P_w` are the sets of height-2 columns in a Fibonacci castle (plus the empty set), `F_{w+2}` in all ([[viennot-heap-tower](pages/viennot-heap-tower.md)]).
- **All castles of exact height 2 by area.** `F_{A+1} − 1`, the `h = 2` row of the spine table ([[bounded-height-castles-nacci](pages/bounded-height-castles-nacci.md)], [[castle-snippets-strips](pages/castle-snippets-strips.md)]). The same numbers as the Fibonacci castles, shifted by one: append a height-1 column to a Fibonacci castle of width `w`, read each height-2 column together with the height-1 column after it as a part 2, and each remaining height-1 column as a part 1. This is a bijection from Fibonacci castles of width `w` onto the castles of exact height 2 and area `w + 1`. Example: `(1, 2, 1, 1, 2)` becomes `(1, 2, 1, 2)`.[^exec]
- **Single-block peaks.** In the (blocks, peaks) table by area on [[odd-castles-and-block-tables](pages/odd-castles-and-block-tables.md)], the diagonal "blocks = peaks + 1" (every peak a single block) has the count `F_{A+1}` by area, the exact-height-2 castles together with the all-1 row.

**Grading matters.** Fibonacci castles are named for their count by width, `F_{w+2} − 1`. Their count by area is `1, 2, 3, 5, 8, 12, 18, 27, 40, 59, 87, …` from area 2, one less than Narayana's cows (A000930), and grows like the supergolden constant `1.4656…` ([[tree-castle-by-area](pages/tree-castle-by-area.md)]).[^exec] The family whose count by area is `F_{A+1} − 1` is a larger one, all castles of exact height 2.

### 2. Castles with no height-1 column (a different composition class)

- **Prime castles.** Castles with no height-1 column are the primes of the gluing monoid, `F_{n−1}` of area `n`, and the composite castles number `2^{n−1} − F_{n−1}` ([[prime-castles](pages/prime-castles.md)], [[castle-by-area](pages/castle-by-area.md)]). These are compositions into parts `≥ 2`, a different class from section 1 with the same numbers after a shift. The growth `φ` needs the height unrestricted: at exact height `h` the growth is the largest root of `x^h = x^{h−2} + ⋯ + x + 1`, the plastic number at `h = 3` and supergolden at `h = 4`, increasing to `φ`.
- **One-peak castles.** A one-peak castle is a prime castle with runs of height-1 columns on both sides, so its count by area is A001924, the Fibonacci numbers summed twice ([[castle-row-raising-equation](pages/castle-row-raising-equation.md)]).
- **Prime convex castles.** By area they agree with `F_{n−1}` through `n = 7` and fall below from `n = 8`, where `(3, 2, 3)` is the first non-unimodal prime castle. The gap to `F_{n−1}` is a novel-candidate ([[prime-convex-castles](pages/prime-convex-castles.md)]).

### 3. Bisections: growth `φ²`

The odd-index and even-index halves of the Fibonacci sequence, each growing like `φ²`. The wiki has no map linking these to section 1.

- **Stacks by perimeter, A001519.** Convex castles (stack polyominoes) by semi-perimeter `s` are `1, 2, 5, 13, 34, …` from `s = 2`. Delest and Viennot code them by Fibonacci words and write the count as `F_{2n}` with `F_0 = F_1 = 1`, a shifted convention. Pages: [[algebraic-languages-and-polyominoes-enumeration](pages/algebraic-languages-and-polyominoes-enumeration.md)], [[convex-castle](pages/convex-castle.md)], [[convex-castle-binomial-identity](pages/convex-castle-binomial-identity.md)] (the anti-diagonal sums of `C(2h+w−3, w−1)`), [[stack-polyomino-gf](pages/stack-polyomino-gf.md)], [[castle-perimeter](pages/castle-perimeter.md)] (signed, the count has period 6), [[polyominoes](pages/polyominoes.md)], [[convex-polyomino](pages/convex-polyomino.md)].
- **Sandpile ladders, A001906.** The tide group of the castle `(2, 2, …, 2)` of width `w` has order `F_{2w}` ([[sandpile-group](pages/sandpile-group.md)]). The same numbers are the even-Fibonacci mode of the `L × 2` strip in Dhar, Ruelle, Sen and Verma, and they enter the sink group of the height-3 castle ([[dhar-ruelle-sen-verma-1995-algebraic-aspects](pages/dhar-ruelle-sen-verma-1995-algebraic-aspects.md)], [[sandpile-census](pages/sandpile-census.md)]). A001906 also appears in a failed heap-of-intervals model of the tower ([[viennot-heap-tower](pages/viennot-heap-tower.md)]).
- **Motzkin castles at height 4.** The height-4 rung of the bounded-height Motzkin ladder grows like `φ²`, because `1 + 2cos(π/5) = φ²`, and its count has the Fibonacci closed form A005207 ([[motzkin-castles](pages/motzkin-castles.md)]).

### 4. Trisection: copper, growth `φ³`

All from `δ_4 = 2 + √5 = φ³`, so copper lies in `Q(√5)`.

- The height-5 ridge transfer matrix gives `𝟙ᵀR_5^{w−1}𝟙 = F_{3w+2}` (`5, 21, 89, 377, …`, A015448) ([[metallic-strip-realizability](pages/metallic-strip-realizability.md)], [[proper-castle-projection](pages/proper-castle-projection.md)], [[reachable-field-census](pages/reachable-field-census.md)]).
- Copper's metallic sequence is `F_{3n}/2` (A001076) ([[metallic-means](pages/metallic-means.md)], [[castle-eigenvalue-oeis-crosswalk](pages/castle-eigenvalue-oeis-crosswalk.md)]).
- More generally, odd powers of a metallic mean are metallic means, so `δ_11 = φ⁵`. The index of `Z[δ_11]` in `Z[φ]` is `F_5 = 5` ([[metallic-means](pages/metallic-means.md)], [[castle-snippets-number-theory](pages/castle-snippets-number-theory.md)]).

### 5. `φ` or Fibonacci inside a larger count

These share the constant with section 1, but the wiki gives no castle-level map to it.

- **Tree castles of exact height 3 by area** grow like `φ`, because the area denominator factors as `(1 + q²)(1 − q − q²)`. The underlying sequence A006498 satisfies `A006498(2n) = F_{n+1}²` ([[tree-castle-by-area](pages/tree-castle-by-area.md)]). This is the tree ban lowering tribonacci to golden ([[castle-classification-growth](pages/castle-classification-growth.md)], [[metallic-means](pages/metallic-means.md)]).
- **Signed Motzkin castles.** The signed count A343773 is, up to sign, the reversion of the Fibonacci generating function, A007440 ([[motzkin-castles](pages/motzkin-castles.md)]).
- **Tower parity sectors.** `H_d(1) = (−1)^d F_{d−1}` and `H_d(−1) = (−1)^d F_{d+2}` ([[tower-parity-sectors](pages/tower-parity-sectors.md)]).
- **Second-difference strips.** The power-law memory rule at `α = 2`, height 2, admits Fibonacci-like columns and grows like `φ` ([[power-law-memory-rules](pages/power-law-memory-rules.md)]).
- **Numerical semigroups by genus** grow like `φ` (Zhai, proving a Bras-Amorós conjecture), on the numerical-semigroup branch of [[block-count-constraints](pages/block-count-constraints.md)].

### 6. Fibonacci as a worked example or algebraic tool

No castle count here. Fibonacci is the example used to teach a method, or a recurrence that shows up in the algebra.

- **Recurrence to rational generating function to closed form** (Knuth's Fibonacci method, Binet's formula): [[aocp-generating-functions](pages/aocp-generating-functions.md)], [[generating-functions](pages/generating-functions.md)], [[generating-functions-topic](pages/generating-functions-topic.md)], [[symbolic-method](pages/symbolic-method.md)], [[signed-tower-count](pages/signed-tower-count.md)], [[algebraic-transcendental-wall](pages/algebraic-transcendental-wall.md)].
- **Fast far-off terms:** [[kitamasa](pages/kitamasa.md)] is taught on Fibonacci by hand.
- **Continued fractions and convergents:** `φ = [1; 1, 1, …]` with Fibonacci convergents, and Lucas as the trace sequence: [[eigenvalue-continued-fractions](pages/eigenvalue-continued-fractions.md)], [[tower-word-continued-fraction](pages/tower-word-continued-fraction.md)], [[castle-eigenvalue-oeis-crosswalk](pages/castle-eigenvalue-oeis-crosswalk.md)].
- **The Pell parallel** (golden `a = 1` against silver `a = 2`): [[pell-numbers](pages/pell-numbers.md)], [[pell-castle-strip](pages/pell-castle-strip.md)], [[metallic-means](pages/metallic-means.md)].
- **Orders mod `p`** (Pisano-type periods): [[castle-eigenvalue-oeis-crosswalk](pages/castle-eigenvalue-oeis-crosswalk.md)], [[castle-snippets-number-theory](pages/castle-snippets-number-theory.md)].
- **Fibonacci recurrences in polynomial algebra:** the mod-2 reduction of the rescaled `char_k` is a Fibonacci recurrence over `F_2[y²]` ([[char-k-eisenstein-at-two](pages/char-k-eisenstein-at-two.md)]), and the mod-3 evaluation of `char_k` at `±1` is Fibonacci-like ([[mod-9-coset-lift](pages/mod-9-coset-lift.md)]).
- **Entropy:** `log₂ φ = 0.694` bits per column ([[castle-entropy](pages/castle-entropy.md)]).

### 7. Neighbouring recurrences with other growth constants

- **k-Fibonacci tree castles.** Tree castles of exact height `h ≥ 3` by width satisfy `a(n) = a(n−1) + (h−1)a(n−2)` (Jacobsthal at `h = 3`, then A006130, A006131), growing like `(1 + √(4h − 3))/2` ([[castle-graph](pages/castle-graph.md)]). This is one way to extend Fibonacci castles to higher `h`. It leads to quadratic constants, not to the n-nacci ones.
- **Ridge castles at `h ≥ 3`.** The other extension by width, through the metallic ladder: silver, bronze, copper, … ([[metallic-strip-realizability](pages/metallic-strip-realizability.md)]).
- **Fractional Fibonacci.** `∇^α a_n = a_{n−1}` is golden only at `α = 1/2`, and the Fibonacci-Pell interpolation is golden only at `α = 0` ([[fractional-recurrences](pages/fractional-recurrences.md)]).
- **Padovan and Perrin.** The "Fibonacci and Lucas" of the plastic number, with the lag recurrence `a(n) = a(n−2) + a(n−3)` ([[plastic-number](pages/plastic-number.md)]).
- **Narayana's cows.** `a(n) = a(n−1) + a(n−3)` (A000930), one more than the count of Fibonacci castles by area (section 1, "Grading matters").

## Tribonacci

### 1. All castles of exact height 3 by area (on the spine)

`A000073(A+2) − F_{A+1}` = `1, 2, 5, 11, 23, 47, 94, 185, …` from area 3, growing like `τ` ([[bounded-height-castles-nacci](pages/bounded-height-castles-nacci.md)]).[^exec] Code is in `bounded_castles_by_area` on [[castle-snippets-strips](pages/castle-snippets-strips.md)], which also notes that `nearest_metallic` wrongly reports golden for this sequence, since `τ` is cubic. The OEIS interlink is on [[castle-sequence-catalogue](pages/castle-sequence-catalogue.md)], the tribonacci area growth class on [[castle-classification-growth](pages/castle-classification-growth.md)] and [[castle-classification](pages/castle-classification.md)], and the entropy `log₂ τ = 0.879` bits on [[castle-entropy](pages/castle-entropy.md)].

### 2. The height-3 ceiling (on the spine)

Any height-3 strip rule counts a subset of the compositions with parts at most 3, so its area growth constant is at most `τ`. The all-ones rule attains it, and `τ` cannot occur at height 2 ([[area-growth-census](pages/area-growth-census.md)]). Banning 2×2 blocks lowers the constant from `τ` to `φ` (Fibonacci section 5).

### 3. `τ` as a width growth constant (on the spine)

[[reachable-field-census](pages/reachable-field-census.md)] lists tribonacci among the nine cubic Perron roots of 0/1 strip matrices at height 3, without naming a rule. One rule that realizes it extends the Fibonacci castle rule:

- **Rule.** Heights `1, 2, 3`. A column of height `k ≥ 2` must be followed by one of height `k − 1`. After a height-1 column any height may follow. So every tall column starts a forced descent `k, k−1, …, 1`, which may be cut off at the right end. Example of width 8: `(1, 3, 2, 1, 2, 1, 1, 3)`.
- **Transfer matrix.** The companion matrix of `x³ − x² − x − 1`, rows `1 → {1, 2, 3}`, `2 → {1}`, `3 → {2}`. Its Perron root is `τ`.
- **Count.** At exact height 3 by width, `1, 2, 4, 9, 18, 36, 71, 138, 266, 509, …`, and the ratio of successive terms is `1.83929` at `w = 79`. With the last column required to have height 1, each forced descent is one part, and the castles of width `w` correspond to the castles of exact height 3 and area `w` in section 1. There are `A000073(w+2) − F_{w+1}` of them.[^exec]
- **At height 2** the rule says that a height-2 column is followed by a height-1 column. That is the Fibonacci castle rule, and the end-at-height-1 bijection is the one in Fibonacci section 1 with the appended column. The same rule and bijection work at every height (checked through `h = 5`).[^exec]

[[fractional-recurrences](pages/fractional-recurrences.md)] asks whether a small rational order `α` hits `τ`. That is open.

### 4. Castles by perimeter: `τ²` and `τ` (not on the spine)

All castles by semi-perimeter (the bargraphs, A082582) grow like `τ²`. With the castle sign the growth drops to `τ` ([[castle-perimeter](pages/castle-perimeter.md)]). [[castle-sign-kms-matrix](pages/castle-sign-kms-matrix.md)] shows both cubics come from one norm form, and [[castle-sequence-catalogue](pages/castle-sequence-catalogue.md)] lists the series. Convex castles by perimeter grow like `φ²` (Fibonacci section 3), against `τ²` for all castles. No explanation is known for either constant through compositions, and [[castle-perimeter](pages/castle-perimeter.md)] records the link to the area `τ` as open.

## Tetranacci, pentanacci, and higher

- **All castles of exact height `h ≥ 4` by area.** Rows 4 and 5 of the spine table, growing like the tetranacci constant `1.9276…`, the pentanacci constant `1.9659…`, and so on, tending to `2` ([[bounded-height-castles-nacci](pages/bounded-height-castles-nacci.md)], [[castle-sequence-catalogue](pages/castle-sequence-catalogue.md)], [[castle-classification-growth](pages/castle-classification-growth.md)], [[castle-snippets-strips](pages/castle-snippets-strips.md)]).
- **The height-`h` ceiling.** The `h`-nacci constant bounds every height-`h` rule by area (tetranacci first appears at height 4). It is one of the two lower bounds on the minimum height of a growth constant ([[area-growth-census](pages/area-growth-census.md)]).
- **Width.** The forced-descent rule of tribonacci section 3 at height `h` has the `h`-nacci companion matrix as its transfer matrix.
- **Bounded summands in general.** Flajolet and Sedgewick's compositions with parts in `{1, …, r}`, OGF `(1 − z)/(1 − 2z + z^{r+1})` ([[analytic-combinatorics-ch1-ogfs](pages/analytic-combinatorics-ch1-ogfs.md)]). Enumeration by Knuth's Algorithm M with an area filter ([[aocp-generating-permutations-tuples](pages/aocp-generating-permutations-tuples.md)]).
- **Not n-nacci.** With the tree ban, the height-4 row by area is A000570 (tournaments) instead of tetranacci ([[unique-tournament](pages/unique-tournament.md)], [[tree-castle-by-area](pages/tree-castle-by-area.md)]). With no height limit, tree castles by area grow like plastic squared, not 2 ([[plastic-number](pages/plastic-number.md)]).

## Related Concepts

- [[bounded-height-castles-nacci](pages/bounded-height-castles-nacci.md)] - the spine: castles by area as compositions with bounded parts.
- [[metallic-means](pages/metallic-means.md)] - the quadratic ladder that Fibonacci (`a = 1`) starts and that the n-nacci constants for `h ≥ 3` sit outside.
- [[castle-classification-growth](pages/castle-classification-growth.md)] - Axis 8, where each constant above is a growth type.
- [[castle-notation](pages/castle-notation.md)] - `τ` and the Fibonacci castle entries.
- [[oeis-index](pages/oeis-index.md)] - every A-number above, with the pages that cite it.

## Footnotes

[^exec]: Verified by execution (Python 3, 2026-10-02), by brute force over skylines and compositions: the exact-height area counts for `h = 2..5` and `A ≤ 14` equal the difference of consecutive n-nacci composition counts; the append-a-column map is a bijection from Fibonacci castles of width `w` onto the castles of exact height 2 and area `w + 1` for `w ≤ 13`; Fibonacci castles by area are `1, 2, 3, 5, 8, 12, 18, 27, 40, 59, 87, 128, 188` for `A = 2..14` with successive ratio approaching `1.4656`; for `h = 2..5` and `w ≤ 11`, forced-descent castles of exact height `h` ending at height 1 number the compositions of `w` with largest part exactly `h`; and the free-end forced-descent count at `h = 3`, by transfer matrix through `w = 80`, has successive ratio `1.839295` at `w = 79`.
