---
title: Castle classification - growth types
category: Concepts
summary: Growth types classify families of castles, not single castles. A family is "X by width" (or by height, by area, by semi-perimeter) when its count, graded by that axis, grows like X^n. Metallic growth constants are de Spinadel's σ_p^q, the roots of x² − px − q, named golden, silver, bronze, copper (= 2) and nickel and otherwise written by symbol; by width the ridge castles realize the q = 1 row δ_a = σ_a^1 and the tree castles of height h the p = 1 column σ_1^{h−1}. By area the castles of height h grow at the h-nacci constants, and tree and prime castles at supergolden, plastic and ψ²; by semi-perimeter all castles grow at τ², τ the tribonacci constant.
tags: [concept, castle, classification, taxonomy, growth-constant, metallic-means, ridge-castle, non-metallic, meta-classification, n-nacci, cubic-pisot, plastic-number, class-predicate]
sources: [de-spinadel-1999-family-of-metallic-means]
created: 2026-09-19
updated: 2026-10-16
---

# Castle classification - growth types

## Scope

The shape types of [[castle-classification-shape](pages/castle-classification-shape.md)] and the spectral types of [[castle-classification-spectrum](pages/castle-classification-spectrum.md)] are predicates on a single castle `(c_1, …, c_w)`. A growth type classifies a **family** of castles, an infinite set defined by a construction rule, by the growth constant of its count along a size axis. A single castle has no growth type, and it belongs to many families with different growth constants.

Two different rules can give the same growth type: the Pell castles ([[pell-castle](pages/pell-castle.md)]) and the ridge castles of height 3 ([[ridge-castle](pages/ridge-castle.md)]) are both silver by width.

## Naming

A family of castles is **X by width** when the number of its castles of width `w`, at a fixed height `h`, grows like `X^w` up to a subexponential factor; likewise **by height** (width fixed), **by area** (the number of cells `c_1 + ⋯ + c_w`) and **by semi-perimeter** (`w` plus the number of blocks, [[castle-perimeter](pages/castle-perimeter.md)]). The axis is always named, so "silver by width" and "silver by area" are different statements, and a growth word is never a family name.

The constant `X` takes its literature name where it has one:

- **Metallic means** ([[metallic-means](pages/metallic-means.md)]): de Spinadel's family `σ_p^q = (p + √(p² + 4q))/2`, the positive roots of `x² − px − q` for natural `p, q`, with the names golden (`σ_1^1 = φ`), silver (`σ_2^1 = 1 + √2`), bronze (`σ_3^1 = (3 + √13)/2`), copper (`σ_1^2 = 2`) and nickel (`σ_1^3 = (1 + √13)/2`) ([[de-spinadel-1999-family-of-metallic-means](pages/de-spinadel-1999-family-of-metallic-means.md)]). The members with `q = 1` are `δ_a = σ_a^1`; the others are written by symbol, as `δ_4 = 2 + √5` and `σ_2^2 = 1 + √3`. A strip family whose width generating function has denominator `1 − p_1 x − p_2 x²` with `p_1, p_2 ≥ 1` grows at `σ_{p_1}^{p_2}` ([[metallic-strip-realizability](pages/metallic-strip-realizability.md)]).
- **n-nacci constants**, the positive roots of `x^h = x^{h−1} + ⋯ + x + 1`: tribonacci at `h = 3`, tetranacci at `h = 4`, pentanacci at `h = 5`, increasing to 2.
- **Cubic Pisot numbers**: supergolden, the real root of `x³ = x² + 1`; the plastic number `ψ`, the real root of `x³ = x + 1`; and `ψ²`, the real root of `x³ − 2x² + x − 1`.

Other algebraic growth constants are written by value and minimal polynomial, as `1.685137…`, the root of `x⁵ − x⁴ − x² − x − 1`.

## By width

At a fixed height, every member of the row `δ_a` is realized by the ridge castles, and every member of the column `σ_1^q` with `q = h − 1` by the tree castles of height `h`. The plateau-free castles of height `h ≥ 3`, in which neighboring columns always differ, grow at `h − 1 = σ_1^{(h−1)(h−2)}`, the largest eigenvalue of `J − I` on `h` heights; at `h = 3` that is copper.[^1]

### Golden, `φ = δ_1`

- **The Fibonacci castles**, the tree castles of height 2: no two neighboring columns of height 2 ([[fibonacci-castle](pages/fibonacci-castle.md)], [[castle-graph](pages/castle-graph.md)]). They number `F_{w+2} − 1`, with generating function `x/((1 − x)(1 − x − x²))`.
- **The ridge castles of height 2**: no two neighboring columns of height 1. Exchanging the heights 1 and 2 maps them onto the Fibonacci castles and the flat row `(1, …, 1)`, so there are `F_{w+2}` of them for `w ≥ 2`.[^1]

### Silver, `δ_2 = 1 + √2`

- **The Pell castles** ([[pell-castle](pages/pell-castle.md)], [[pell-castle-strip](pages/pell-castle-strip.md)]): first column at height 1, neighboring columns differing by at most 1, height 3. They number `A_Pell(w) = P⋆_w − 2^{w−1}` (`0, 0, 1, 4, 13, 38, 105, 280, …`, `A094706(w − 2)`), where `P⋆_w`, the Pell numbers (A000129), count the same skylines without the condition of reaching height 3, and `2^{w−1}` counts those that stay at heights 1 and 2. With a free first column there are `A001333(w + 1) − 2^w = A106514(w − 1)` of them (`1, 3, 9, 25, 67, 175, …`), from the Pell-Lucas numbers A001333.[^1]
- **The ridge castles of height 3** ([[ridge-castle](pages/ridge-castle.md)], [[metallic-strip-realizability](pages/metallic-strip-realizability.md)]): `1, 5, 15, 39, 97, 237, 575, …`.[^1]

The tower words of [[tower-word-continued-fraction](pages/tower-word-continued-fraction.md)] also grow at `1 + √2`, counted by word length: A004149, whose generating function has its singularity at `√2 − 1`. All castles of height `h` number `h^w − (h−1)^w` and grow at the integer `h` by width.

### Bronze and the higher `δ_a`: ridge castles

The **ridge rule** lets neighboring columns have equal heights only at the maximum `h`; its castles of height `h` are the **ridge castles** ([[ridge-castle](pages/ridge-castle.md)]). The transfer matrix `R_h = J − D`, with `D = diag(1, …, 1, 0)`, has characteristic polynomial `(x + 1)^{h−2}(x² − (h − 1)x − 1)` and largest eigenvalue `δ_{h−1}` ([[metallic-strip-realizability](pages/metallic-strip-realizability.md)]), so the ridge castles of height `a + 1` are `δ_a` by width:

- **Bronze**, `δ_3 = (3 + √13)/2 = 3.3028…`: the ridge castles of height 4, `1, 7, 31, 118, 421, …`. No rule on three heights is bronze by width, since a 0/1 matrix of size 3 has largest eigenvalue at most 3; among the 0/1 matrices of size 4, 192 have largest eigenvalue `δ_3`.[^1]
- **`δ_4 = 2 + √5 = φ³`**: the ridge castles of height 5. The ridge strips of height 5, which need not reach height 5, number `𝟙ᵀ R_5^{w−1} 𝟙 = F_{3w+2}`, and the ridge castles of height 5 number `F_{3w+2} − 4·3^{w−1}`.[^1]
- **`δ_5, δ_6, …`**: the ridge castles of heights 6, 7, ….

### Copper, nickel and the column `σ_1^{h−1}`: tree castles

The **tree skylines** of height at most `h`, with no two neighboring columns of height at least 2, number `T_h(w)` with `T_h(w+2) = T_h(w+1) + (h − 1)·T_h(w)`, so they grow at `σ_1^{h−1} = (1 + √(4h − 3))/2`. The tree castles of height `h` number `A_tree(w, h) = T_h(w) − T_{h−1}(w)`, which for `h ≥ 3` satisfies the recurrence of order 4 with characteristic polynomial `(x² − x − (h − 1))(x² − x − (h − 2))`, not the recurrence of `T_h`; since `σ_1^{h−1} > σ_1^{h−2}`, they also grow at `σ_1^{h−1}` ([[castle-graph](pages/castle-graph.md)]):

- **Copper**, `σ_1^2 = 2`: the tree castles of height 3, `A001045(w + 2) − F_{w+2}` = `1, 2, 6, 13, 30, 64, 137, 286, …`, the Jacobsthal numbers A001045 minus the Fibonacci numbers. The plateau-free castles of height 3 are copper by width too.
- **Nickel**, `σ_1^3 = (1 + √13)/2 = 2.3028…`: the tree castles of height 4, `A006130(w + 1) − A001045(w + 2)` = `1, 2, 8, 19, 54, 132, 337, 818, …`. Nickel lies in `Q(√13)`, the field of bronze.
- **`σ_1^4 = (1 + √17)/2` and beyond**: the tree castles of heights 5, 6, ….

Members with `p, q ≥ 2` also occur, for instance `σ_2^2 = 1 + √3` for the height-3 rule of [[metallic-strip-realizability](pages/metallic-strip-realizability.md)] that forbids two neighboring columns at the ceiling.

## By area

**Golden by area.** The prime castles, the castles with no column of height 1, number `F_{n−1}` by area with the height unrestricted ([[prime-castles](pages/prime-castles.md)]); at a fixed height they grow more slowly, at the root of `x^h = x^{h−2} + ⋯ + 1`: plastic at height 3, supergolden at height 4, increasing to `φ`. The castles of height 2 number `F_{A+1} − 1` by area, the compositions of `A` into 1s and 2s with at least one 2 ([[castles-of-height-h-by-area](pages/castles-of-height-h-by-area.md)]).

**The n-nacci family.** The castles of height `h` by area are the compositions of the area with largest part `h`, with generating function `1/(1 − x − ⋯ − x^h) − 1/(1 − x − ⋯ − x^{h−1})`, so they grow at the `h`-nacci constant:[^1]

| `h` | growth by area | minimal polynomial | count at area `A` |
|---|---|---|---|
| 2 | golden, `1.6180…` | `x² − x − 1` | `F_{A+1} − 1` (A000045) |
| 3 | tribonacci, `1.8393…` | `x³ − x² − x − 1` | `A000073(A + 2) − F_{A+1}` |
| 4 | tetranacci, `1.9276…` | `x⁴ − x³ − x² − x − 1` | `A000078(A + 3) − A000073(A + 2)` |
| 5 | pentanacci, `1.9659…` | `x⁵ − x⁴ − x³ − x² − x − 1` | `A001591(A + 4) − A000078(A + 3)` |
| unrestricted | `2` | `x − 2` | `2^{A−1}` (A011782) |

Only the row `h = 2` is metallic.

**Cubic Pisot growth by area.**

| constant | value | minimal polynomial | families of castles |
|---|---|---|---|
| supergolden | `1.4656…` | `x³ − x² − 1` | the tree castles of height 2, `A077868(A − 2)` ([[tree-castle-by-area](pages/tree-castle-by-area.md)], [[q-fibonacci-castle](pages/q-fibonacci-castle.md)]); the prime castles of height 4 ([[prime-castles](pages/prime-castles.md)]) |
| `ψ²` | `1.7549…` | `x³ − 2x² + x − 1` | the tree castles of any height, `A005251(A + 2)` ([[tree-castle-by-area](pages/tree-castle-by-area.md)], [[plastic-number](pages/plastic-number.md)]) |
| plastic `ψ` | `1.3247…` | `x³ − x − 1` | the smallest growth constant by area of a strip rule, at height 2 with "height 1 may not follow height 1" ([[area-growth-census](pages/area-growth-census.md)]); the prime castles of height 3 ([[prime-castles](pages/prime-castles.md)]) |

The tree castles of height 3 are golden by area, and those of height 4 grow at `1.685137…`, the root of `x⁵ − x⁴ − x² − x − 1`; the tree skylines of height at most 4 are counted by A000570, the tournaments determined by their score vectors ([[tree-castle-by-area](pages/tree-castle-by-area.md)], [[unique-tournament](pages/unique-tournament.md)]).[^1]

**Subexponential growth.** The convex castles by area are the weakly unimodal compositions, A001523 ([[weakly-unimodal-composition](pages/weakly-unimodal-composition.md)]), with `a(n) ~ exp(2π√(n/3)) / (8·3^{3/4}·n^{5/4})` (Auluck 1951, as the OEIS entry gives it), so their growth constant by area is 1.[^2]

## By height and by semi-perimeter

**By height.** At a fixed width there are `h^w − (h − 1)^w` castles of height `h`, a polynomial in `h` of degree `w − 1`, so every family grows at most polynomially by height, and no family has a growth constant above 1 on this axis. The counts are often quasi-polynomials: `A^e(w, h)`, as a sequence in `h`, is annihilated by `(x² − 1)^w` (computed for `w ≤ 6`), and the signed tower count `P(k, L)` at a fixed `L` has the characteristic polynomial `(x + 1)^L (x − 1)^{L−2}` in `k` for `4 ≤ L ≤ 12` ([[signed-tower-k-direction](pages/signed-tower-k-direction.md)]).[^1]

**By semi-perimeter.** The number of blocks alone does not bound the width, since every flat row `(1, …, 1)` has one block, so the block axis is taken together with the width as the semi-perimeter `w + blocks`. By semi-perimeter all castles grow at `τ² = 3.3830…`, the square of the tribonacci constant, and their signed count grows only at `τ` ([[castle-perimeter](pages/castle-perimeter.md)]).

## Statements across scopes

A shape or spectral predicate defines a family, and the family has a growth type:

- **The Fibonacci castles, the tree castles of height 2, are golden by width**: the rule "no two neighboring columns of height 2" has transfer matrix `[[1, 1], [1, 0]]`.
- **The tree predicate lowers the growth by area.** At height 3, all castles are tribonacci by area and the tree castles golden by area; at height 2 the constant drops from `φ` to supergolden, and with the height unrestricted from 2 to `ψ²`.

The plastic number also appears in the signed tower count, as the largest eigenvalue `2ψ²` of `char_6` ([[signed-tower-count](pages/signed-tower-count.md)]), an eigenvalue of a recurrence and not the growth constant of a family.

## Related Concepts

- [[castle-classification](pages/castle-classification.md)] - the hub of the classifications by shape, spectrum and growth.
- [[castle-classification-shape](pages/castle-classification-shape.md)] - predicates on single castles by shape.
- [[castle-classification-spectrum](pages/castle-classification-spectrum.md)] - predicates on single castles by the spectrum of the castle graph.
- [[metallic-means](pages/metallic-means.md)] - de Spinadel's family `σ_p^q` and its named members.
- [[metallic-strip-realizability](pages/metallic-strip-realizability.md)] - which metallic means are growth constants of strip rules by width, and the ridge matrix `R_h`.
- [[pell-castle-strip](pages/pell-castle-strip.md)] - the strips counted by the Pell numbers, silver by width.
- [[castle-strip](pages/castle-strip.md)] - skylines read one column at a time under a rule on neighboring columns, whose transfer matrices give the growth by width.
- [[castle-graph](pages/castle-graph.md)] - tree skylines and tree castles by width.
- [[castles-of-height-h-by-area](pages/castles-of-height-h-by-area.md)] - the castles of height `h` by area, the n-nacci family.
- [[tree-castle-by-area](pages/tree-castle-by-area.md)] - tree skylines and tree castles by area.
- [[prime-castles](pages/prime-castles.md)] - castles with no column of height 1, by area.
- [[area-growth-census](pages/area-growth-census.md)] - the growth constants by area of all strip rules up to height 4.
- [[castle-perimeter](pages/castle-perimeter.md)] - castles by semi-perimeter.
- [[unique-tournament](pages/unique-tournament.md)] - A000570 and the growth constant `1.685…`.
- [[castle-eigenvalues-by-example](pages/castle-eigenvalues-by-example.md)] - eigenvalues of castle graphs, transfer matrices and recurrences, worked on small castles.
- [[castle-snippets-strips](pages/castle-snippets-strips.md)] - code that computes growth constants of strip rules.

## Footnotes

[^1]: Verified by execution (Python 3.11 with NumPy and SymPy, 2026-10-16): by enumeration of all skylines, the Fibonacci castles and their generating function for `w ≤ 11`; the ridge castles of height 2 for `w ≤ 10`, height 3 for `w ≤ 8`, height 4 for `w ≤ 7` and height 5 for `w ≤ 6` against `F_{3w+2} − 4·3^{w−1}`, and `𝟙ᵀR_5^{w−1}𝟙 = F_{3w+2}` for `w ≤ 7`; the Pell castles for `w ≤ 10` and the free-first-column count for `w ≤ 10` against https://oeis.org/A106514 (read 2026-10-16); the tree castles of heights 3 and 4 against the differences of A001045, A006130 and the Fibonacci numbers, and the failure of `a(n) = a(n−1) + 2a(n−2)` for the tree castles of height 3; the largest eigenvalue `h − 1` of `J − I` for `h = 3, 4, 5`; the 192 matrices among all `2^16` 0/1 matrices of size 4; the n-nacci counts for `A ≤ 10` and their constants; the tree-castle growth constants by area from the generating functions `(1 + P_h(q))/(1 − q − q·P_h(q))`; `(x² − 1)^w` against `A^e(w, h)` for `w ≤ 6` and `h ≤ 6w + 7`.
[^2]: https://oeis.org/A001523 (read 2026-10-16) - "a(n) ~ exp(2*Pi*sqrt(n/3)) / (8 * 3^(3/4) * n^(5/4)) [Auluck, 1951]. - Vaclav Kotesovec, Jun 22 2015".
