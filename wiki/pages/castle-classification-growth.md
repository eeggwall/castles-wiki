---
title: Castle classification - growth types
category: Concepts
summary: Growth types classify families of castles, not single castles; upper bounds hold for every family, and existence and first-height statements are about rules, 0/1 tables of which height may follow which, since every constant below the ceiling of an axis is the growth constant of some family. A family is "X by width" (or by height, by area, by semi-perimeter) when its count, graded by that axis, grows like X^n. Metallic growth constants are de Spinadel's σ_p^q, the roots of x² − px − q, named golden, silver, bronze, copper (= 2) and nickel and otherwise written by symbol; by width the ridge castles realize the q = 1 row δ_a = σ_a^1 and the tree castles of height h the p = 1 column σ_1^{h−1}. Three Padovan-counted families are plastic by width. By area every family grows at most 2, so none is silver or bronze; the castles of height h grow at the h-nacci constants, and tree, prime and ridge castles at supergolden, plastic and ψ². By semi-perimeter all castles grow at τ², τ the tribonacci constant; silver first occurs at height 5, no family of height at most 21 is bronze (computed), and whether a rule of height 22 or more is bronze is open. Across the three axes, tree castles have semi-perimeter A + 1 and so grow alike by area and by semi-perimeter, prime castles of height h by semi-perimeter are the castles of height h − 1, and the Pell castles, silver by width, are copper by semi-perimeter.
tags: [concept, castle, classification, taxonomy, growth-constant, metallic-means, ridge-castle, non-metallic, meta-classification, n-nacci, cubic-pisot, plastic-number, class-predicate]
sources: [de-spinadel-1999-family-of-metallic-means, balado-silvestre-2026-runs-binary-strings]
created: 2026-09-19
updated: 2026-10-26
---

# Castle classification - growth types

## Scope

The shape types of [[castle-classification-shape](pages/castle-classification-shape.md)] and the spectral types of [[castle-classification-spectrum](pages/castle-classification-spectrum.md)] are predicates on a single castle `(c_1, …, c_w)`. A growth type classifies a **family** of castles, an infinite set of castles, by the growth constant of its count along a size axis. A single castle has no growth type, and it belongs to many families with different growth constants.

Most families on this page come from a **rule**, a 0/1 table on the heights `1, …, h` that says which column height may follow which ([[castle-strip](pages/castle-strip.md)]): the family is the castles of height `h` whose neighboring columns all obey it, sometimes with a condition on the first column, as for the Pell castles. A rule's count has a rational generating function along each axis, so its growth constant is an algebraic number. The two kinds of statement on this page hold for different classes:

- **Upper bounds hold for every family.** A family of castles of height at most `h` is a subset of all of them and grows no faster: no family grows faster than 2 by area, and no family of height at most 21 grows faster than `3.3002…` by semi-perimeter.
- **Existence and first-height statements are about rules.** Every constant `X ≥ 1` below the growth constant of all castles of height `h` along an axis is the growth constant of some family of castles of height `h`: for each size `n`, take the first `⌊X^n⌋` castles of size `n` in lexicographic order, or all of them when there are fewer. So a statement that a constant does or does not occur, or first occurs at some height, is about rules: "no rule on three heights is bronze by width", "no rule of height at most 4 is silver by semi-perimeter".

Two different rules can give the same growth type: the Pell castles ([[pell-castle](pages/pell-castle.md)]) and the ridge castles of height 3 ([[ridge-castle](pages/ridge-castle.md)]) are both silver by width.

## Naming

A family of castles is **X by width** when the number of its castles of width `w`, at a fixed height `h`, grows like `X^w` up to a subexponential factor; likewise **by height** (width fixed), **by area** (the number of cells `c_1 + ⋯ + c_w`) and **by semi-perimeter** (`w` plus the number of blocks, [[castle-perimeter](pages/castle-perimeter.md)]). The axis is always named, so "silver by width" and "silver by area" are different statements, and a growth word is never a family name.

The constant `X` takes its literature name where it has one:

- **Metallic means** ([[metallic-means](pages/metallic-means.md)]): de Spinadel's family `σ_p^q = (p + √(p² + 4q))/2`, the positive roots of `x² − px − q` for natural `p, q`, with the names golden (`σ_1^1 = φ`), silver (`σ_2^1 = 1 + √2`), bronze (`σ_3^1 = (3 + √13)/2`), copper (`σ_1^2 = 2`) and nickel (`σ_1^3 = (1 + √13)/2`) ([[de-spinadel-1999-family-of-metallic-means](pages/de-spinadel-1999-family-of-metallic-means.md)]). The members with `q = 1` are `δ_a = σ_a^1`; the others are written by symbol, as `δ_4 = 2 + √5` and `σ_2^2 = 1 + √3`. A strip family whose width generating function has denominator `1 − p_1 x − p_2 x²` with `p_1, p_2 ≥ 1` grows at `σ_{p_1}^{p_2}` ([[metallic-strip-realizability](pages/metallic-strip-realizability.md)]).
- **n-nacci constants**, the positive roots of `x^h = x^{h−1} + ⋯ + x + 1`: tribonacci at `h = 3`, tetranacci at `h = 4`, pentanacci at `h = 5`, increasing to 2.
- **Cubic Pisot numbers**: supergolden, the real root of `x³ = x² + 1`;[^crilly] the plastic number `ψ`, the real root of `x³ = x + 1`; and `ψ²`, the real root of `x³ − 2x² + x − 1`.

Other algebraic growth constants are written by value and minimal polynomial, as `1.685137…`, the root of `x⁵ − x⁴ − x² − x − 1`.

## By width

At a fixed height, every member of the row `δ_a` is realized by the ridge castles, and every member of the column `σ_1^q` with `q = h − 1` by the tree castles of height `h`; the plastic number is realized at heights 2 and 3. The plateau-free castles of height `h ≥ 3`, in which neighboring columns always differ, grow at `h − 1 = σ_1^{(h−1)(h−2)}`, the largest eigenvalue of `J − I` on `h` heights; at `h = 3` that is copper.[^1]

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

### Plastic, `ψ`

These families are plastic by width, each counted by shifted Padovan numbers A000931 ([[plastic-number](pages/plastic-number.md)], [[golden-silver-bronze-plastic-castles](pages/golden-silver-bronze-plastic-castles.md)], [[padovan-families](pages/padovan-families.md)]):[^1]

- **The maximal castles** of height 2, in which neighboring columns of height 2 are separated by one or two columns of height 1 and each end has at most one column of height 1 ([[fibonacci-castles-sub-families](pages/fibonacci-castles-sub-families.md)]): `A000931(w + 6)`, for example `(2, 1, 1, 2, 1)`.
- **The `(1, 2)`-RLL castles**, the same with at most two columns of height 1 at each end: `A000931(w + 8)` for `w ≥ 3`, for example `(1, 1, 2, 1, 2)`.
- **The rule `1 → 2 → 3 → {1, 2}`** at height 3, in which each column is one higher than the one before, except that a 3 is followed by a 1 or a 2: with first column 1, `A000931(w + 4)` for `w ≥ 3`, for example `(1, 2, 3, 2, 3, 1)`. Its transfer matrix has characteristic polynomial `x³ − x − 1`.

A 0/1 matrix on `n` states with largest eigenvalue above 1 has largest eigenvalue at least the root of `x^n = x + 1` ([[area-growth-census](pages/area-growth-census.md)], section *The smallest constant at each height*). So at every height `h ≥ 2` the smallest growth constant above 1 by width of a rule is the root of `x^h = x + 1`, attained by the rule `1 → 2 → ⋯ → h → 1` with the extra step `h → 2`, whose two cycles of lengths `h` and `h − 1` give the characteristic polynomial `x^h − x − 1`:[^1] `φ` at height 2, and `ψ` at height 3, where this rule is the third family.

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

Two of these constants are metallic means: golden at `h = 2`, and copper `σ_1^2 = 2` with the height unrestricted. Since all castles of area `A` number `2^{A−1}`, every family of castles grows at most 2 by area, and golden and copper are the only metallic means at most 2, so no family is silver or bronze by area.

**Cubic Pisot growth by area.**

| constant | value | minimal polynomial | families of castles |
|---|---|---|---|
| supergolden | `1.4656…` | `x³ − x² − 1` | the tree castles of height 2, `A077868(A − 2)` ([[tree-castle-by-area](pages/tree-castle-by-area.md)], [[q-fibonacci-castle](pages/q-fibonacci-castle.md)]); the prime castles of height 4 ([[prime-castles](pages/prime-castles.md)]) |
| `ψ²` | `1.7549…` | `x³ − 2x² + x − 1` | the tree castles of any height, `A005251(A + 2)` ([[tree-castle-by-area](pages/tree-castle-by-area.md)], [[plastic-number](pages/plastic-number.md)]) |
| plastic `ψ` | `1.3247…` | `x³ − x − 1` | the ridge castles of height 2, with no two neighboring columns of height 1, `A000931(A + 5)` for `A ≥ 2` ([[golden-silver-bronze-plastic-castles](pages/golden-silver-bronze-plastic-castles.md)]), whose rule "height 1 may not follow height 1" has the smallest growth constant above 1 by area of a strip rule at height 2 ([[area-growth-census](pages/area-growth-census.md)]); the prime castles of height 3 ([[prime-castles](pages/prime-castles.md)]) |

The tree castles of height 3 are golden by area, and those of height 4 grow at `1.685137…`, the root of `x⁵ − x⁴ − x² − x − 1`; the tree skylines of height at most 4 are counted by A000570, the tournaments determined by their score vectors ([[tree-castle-by-area](pages/tree-castle-by-area.md)], [[unique-tournament](pages/unique-tournament.md)]).[^1]

**Subexponential growth.** The convex castles by area are the weakly unimodal compositions, A001523 ([[weakly-unimodal-composition](pages/weakly-unimodal-composition.md)]), with `a(n) ~ exp(2π√(n/3)) / (8·3^{3/4}·n^{5/4})` (Auluck 1951, as the OEIS entry gives it), so their growth constant by area is 1.[^2]

## By height and by semi-perimeter

**By height.** At a fixed width there are `h^w − (h − 1)^w` castles of height `h`, a polynomial in `h` of degree `w − 1`, so every family grows at most polynomially by height, and no family has a growth constant above 1 on this axis. The counts are often quasi-polynomials: `A^e(w, h)`, as a sequence in `h`, is annihilated by `(x² − 1)^w`, and the signed tower count `P(k, L)` at a fixed `L` has the characteristic polynomial `(x + 1)^L (x − 1)^{L−2}` in `k` for every `L ≥ 4` (both proved on [[signed-tower-k-direction](pages/signed-tower-k-direction.md)]).[^1]

**By semi-perimeter.** The number of blocks alone does not bound the width, since every flat row `(1, …, 1)` has one block, so the block axis is taken together with the width as the semi-perimeter `w + blocks`. By semi-perimeter all castles grow at `τ² = 3.3830…`, the square of the tribonacci constant, and their signed count grows only at `τ` ([[castle-perimeter](pages/castle-perimeter.md)]). Families with named growth constants by semi-perimeter `s` ([[semi-perimeter-growth-census](pages/semi-perimeter-growth-census.md)], [[golden-silver-bronze-plastic-castles](pages/golden-silver-bronze-plastic-castles.md)]):[^1]

- **Golden**: the castles of height 3 with every column 1 or 3, `A130578(s − 1)`, for example `(3, 1, 1, 3)` with `s = 9`.
- **Silver**: the castles of height 5 with no column of height 1 next to one of height 2 and no column of height 4 next to one of height 5, for example `(3, 5, 3, 1, 4)` with `s = 13`. No rule of height at most 4 is silver by semi-perimeter, and 601 of the `2^25` rules of height 5 are (computed).
- **Plastic**: the castles of height 9 with every column 1 or 9, for example `(1, 9, 1)` with `s = 12`, and the rule `1 → 2`, `2 → {2, 3}`, `3 → 1` at height 3.
- **Supergolden**: the Fibonacci castles and the ridge castles of height 2, both with denominator `1 − x − x³`.
- **`ψ²`**: all castles of height 2, `A077855(s − 3)`, for example `(1, 2, 1)` with `s = 5`.
- **`φ²`**: the convex castles, `A001519(s − 1)` ([[castle-perimeter](pages/castle-perimeter.md)]).

The two-height families `{1, h}` in this list (the golden `{1, 3}` castles, the `ψ²` castles of height 2, the plastic `{1, 9}` castles) correspond one-to-one to the nonzero binary strings of length `s − 1` whose runs of 1s are all at least `h` long, by deleting the bottom row and lengthening each run of height-`h` columns by `h − 1` ([[balado-silvestre-2026-runs-binary-strings](pages/balado-silvestre-2026-runs-binary-strings.md)], [[golden-silver-bronze-plastic-castles](pages/golden-silver-bronze-plastic-castles.md)]).[^runs]

All castles of height at most 21 grow at `3.3002…` by semi-perimeter, below bronze `δ_3 = 3.3028…`, so no family of castles of height at most 21 is bronze by semi-perimeter (computed). All castles of height 22 grow faster than bronze, so some family of castles of height 22 is bronze by semi-perimeter (section *Scope*), and the question is whether some rule is. A rule is bronze by semi-perimeter exactly when the spectral radius of its matrix `M(x)`, with a step from height `a` to height `b` weighted `x^{1 + max(0, b − a)}` ([[semi-perimeter-growth-census](pages/semi-perimeter-growth-census.md)]), is 1 at `x = 1/δ_3 = (√13 − 3)/2`; then `det(I − M(x))` vanishes there, which can be checked exactly in `Q(√13)`. Removing a step from a rule does not raise the spectral radius, and at `x = 1/δ_3` the rule of height 22 that allows every step has spectral radius `1.001999`, so a bronze rule of height 22 is that rule with steps removed that together lower the spectral radius at `1/δ_3` from `1.001999` to exactly 1.[^1] Whether a rule of height 22 or more is bronze by semi-perimeter is open.

## Statements across scopes

A shape or spectral predicate defines a family, and the family has a growth type:

- **The Fibonacci castles, the tree castles of height 2, are golden by width**: the rule "no two neighboring columns of height 2" has transfer matrix `[[1, 1], [1, 0]]`.
- **The tree predicate lowers the growth by area.** At height 3, all castles are tribonacci by area and the tree castles golden by area; at height 2 the constant drops from `φ` to supergolden, and with the height unrestricted from 2 to `ψ²`. The table below shows the same drop by width and by semi-perimeter.

The same family has a growth constant on each axis:[^axes]

| family | by width | by area | by semi-perimeter |
|---|---|---|---|
| all castles, height 2 | copper 2 | golden `φ` | `ψ²` |
| all castles, height 3 | 3 | tribonacci | `2.205569…`, `x³ − 2x² − 1` |
| Fibonacci castles (tree castles, height 2) | golden `φ` | supergolden | supergolden |
| tree castles, height 3 | copper 2 | golden `φ` | golden `φ` |
| tree castles, height 4 | nickel `σ_1^3` | `1.685137…`, `x⁵ − x⁴ − x² − x − 1` | `1.685137…`, `x⁵ − x⁴ − x² − x − 1` |
| ridge castles, height 2 | golden `φ` | plastic `ψ` | supergolden |
| ridge castles, height 3 | silver `δ_2` | `1.503862…`, `x⁶ − 2x³ − x² − x − 1` | `1.803707…`, `x⁵ − x⁴ − 2x² − 2` |
| ridge castles, height 4 | bronze `δ_3` | `1.613479…`, `x⁹ − x⁸ + x⁷ − 2x⁶ − 2x⁴ − x³ − x² − 1` | `2.038180…`, `x⁷ − x⁶ − 3x⁴ − 4x² − x − 4` |
| Pell castles | silver `δ_2` | `1.666302…`, `x⁵ − x³ − 2x² − x − 1` | copper 2 |
| plateau-free castles, height 3 | copper 2 | `1.424054…`, `x⁵ − x⁴ + x³ − 2x² + x − 2` | `1.521380…`, `x³ − x − 2` |
| prime castles, height 3 | copper 2 | plastic `ψ` | `ψ²` |

- **Tree castles grow at the same constant by area and by semi-perimeter.** In a tree castle every column of height `c ≥ 2` has neighbors of height 1, so row 1 is one block and each of the `c − 1` cells above row 1 in that column is a block of its own. A tree castle of width `w` and area `A` therefore has `1 + (A − w)` blocks and semi-perimeter `A + 1`, and its count by semi-perimeter is its count by area shifted by one. The table of [[tree-castle-by-area](pages/tree-castle-by-area.md)] is a table by semi-perimeter too, and the tree castles of any height are `ψ²` by semi-perimeter as well as by area.
- **The prime castles of height `h` by semi-perimeter are the castles of height `h − 1`.** Removing the bottom row of a castle with no column of height 1 leaves a castle of height `h − 1` and the same width with one block fewer, and adding a row inverts this, so the prime castles of height `h` and semi-perimeter `s` correspond one-to-one to the castles of height `h − 1` and semi-perimeter `s − 1`.
- **The Pell castles, silver by width, are copper by semi-perimeter.** The 1-smooth rule on the heights 1, 2, 3 has semi-perimeter denominator `(1 − x)(1 − 2x)(1 + x²)`, and on the heights 1, 2 it allows every step, with denominator `1 − 2x + x² − x³` and growth `ψ² < 2`. The 1-smooth castles with a free first column have the same three constants as the Pell castles.

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
- [[area-growth-census](pages/area-growth-census.md)] - the growth constants by area of all strip rules through height 5.
- [[castle-perimeter](pages/castle-perimeter.md)] - castles by semi-perimeter.
- [[semi-perimeter-growth-census](pages/semi-perimeter-growth-census.md)] - the growth constants by semi-perimeter of all strip rules up to height 4, silver at height 5, and the bound that excludes bronze below height 22.
- [[golden-silver-bronze-plastic-castles](pages/golden-silver-bronze-plastic-castles.md)] - golden, silver, bronze and plastic side by side by width, area, semi-perimeter and spectrum.
- [[padovan-families](pages/padovan-families.md)] - the families counted by Padovan numbers and the bijections between them.
- [[unique-tournament](pages/unique-tournament.md)] - A000570 and the growth constant `1.685…`.
- [[castle-eigenvalues-by-example](pages/castle-eigenvalues-by-example.md)] - eigenvalues of castle graphs, transfer matrices and recurrences, worked on small castles.
- [[castle-snippets-strips](pages/castle-snippets-strips.md)] - code that computes growth constants of strip rules.

## Footnotes

[^1]: Verified by execution (Python 3.11 with NumPy and SymPy, 2026-10-16): by enumeration of all skylines, the Fibonacci castles and their generating function for `w ≤ 11`; the ridge castles of height 2 for `w ≤ 10`, height 3 for `w ≤ 8`, height 4 for `w ≤ 7` and height 5 for `w ≤ 6` against `F_{3w+2} − 4·3^{w−1}`, and `𝟙ᵀR_5^{w−1}𝟙 = F_{3w+2}` for `w ≤ 7`; the Pell castles for `w ≤ 10` and the free-first-column count for `w ≤ 10` against https://oeis.org/A106514 (read 2026-10-16); the tree castles of heights 3 and 4 against the differences of A001045, A006130 and the Fibonacci numbers, and the failure of `a(n) = a(n−1) + 2a(n−2)` for the tree castles of height 3; the largest eigenvalue `h − 1` of `J − I` for `h = 3, 4, 5`; the 192 matrices among all `2^16` 0/1 matrices of size 4; the n-nacci counts for `A ≤ 10` and their constants; the tree-castle growth constants by area from the generating functions `(1 + P_h(q))/(1 − q − q·P_h(q))`; `(x² − 1)^w` against `A^e(w, h)` for `w ≤ 6` and `h ≤ 6w + 7`; the maximal castles and the `(1, 2)`-RLL castles for `w ≤ 14`, the rule `1 → 2 → 3 → {1, 2}` with first column 1 for `w ≤ 19` and the ridge castles of height 2 for `A ≤ 25`, by enumeration, against https://oeis.org/A000931 (read 2026-10-16, offset 0, "1, 0, 0, 1, 0, 1, 1, 1, 2, 2, 3, 4, 5, 7, 9, 12, …"); by a dynamic program over semi-perimeter, the castles of height 3 with every column 1 or 3 and all castles of height 2 for `s ≤ 18` against https://oeis.org/A130578 (read 2026-10-16, offset 1, "Number of different possible rows (or columns) in an n X n crossword puzzle", `0, 0, 1, 3, 6, 10, 16, 26, 43, …`) and https://oeis.org/A077855 (read 2026-10-16, offset 0, "Expansion of 1/((1-2*x+x^2-x^3)*(1-x))", `1, 3, 6, 11, 20, 36, 64, 113, …`), the ratio of consecutive counts of the castles of height 9 with every column 1 or 9 (`1.32472` at `s = 120`), of the plastic rule of height 3 (`1.32472`), of the Fibonacci castles and the ridge castles of height 2 (`1.465571` at `s = 150`) and of the silver rule of height 5 (`1, 7, 26, 74, 196, 525, …` for `s = 6, 7, …`); the spectral radius of `M(x)[a][b] = x^{1 + max(0, b − a)}` on all heights at `x = 1/δ_3`, `0.998657` at height 21 and `1.001999` at height 22. The census of rules by semi-perimeter is on [[semi-perimeter-growth-census](pages/semi-perimeter-growth-census.md)] and was not rerun. The rule `1 → 2 → ⋯ → h → 1` with the extra step `h → 2` has characteristic polynomial `x^h − x − 1` for `h = 2..8` (SymPy, 2026-10-25).
[^axes]: Verified by execution (Python 3.11 with SymPy, 2026-10-26): each entry from the generating function of the family on that axis, the strips of the rule on the heights `1, …, h` minus those on `1, …, h − 1` (on `2, …, h` minus `2, …, h − 1` for the prime castles), with the step to a column of height `b` after one of height `a` weighted `x` by width, `x^b` by area and `x^{1 + max(0, b − a)}` by semi-perimeter, `a = 0` before the first column; the smallest positive pole found exactly, and its irreducible factor reversed to give the minimal polynomial; every constant also against the ratio of consecutive counts from a dynamic program to size 700. The semi-perimeter `A + 1` of every tree castle, and the shift by one block of every prime castle, by enumeration of all castles of height at most 5 and width at most 8 (width at most 7 for the prime castles).
[^2]: https://oeis.org/A001523 (read 2026-10-16) - "a(n) ~ exp(2*Pi*sqrt(n/3)) / (8 * 3^(3/4) * n^(5/4)) [Auluck, 1951]. - Vaclav Kotesovec, Jun 22 2015".
[^crilly]: https://www.jstor.org/stable/3620208 (T. Crilly, "A supergolden rectangle", *The Mathematical Gazette* 78 (1994) 320-325, read 2026-10-11) - p.322: "x must satisfy the cubic equation x³ − x² − 1 = 0", for a rectangle cut into a square and two smaller rectangles similar to it; p.323: "in the case of the supergolden ratio ψ we have the cubic x³ = x² + 1". Crilly's symbol `ψ` is the wiki's symbol for the plastic number, so the wiki writes this constant by name. The printed value `1.465567…` differs from the root `1.4655712…` in the fifth decimal.
[^runs]: [[balado-silvestre-2026-runs-binary-strings](pages/balado-silvestre-2026-runs-binary-strings.md)] §2.7 p.31 L1550-1554 and §2.7.4 p.33 L1664-1670 [synthesis] - eq. (87), the `n`-strings with at least one 1 whose nonnull runs all have length at least `k`, "We subtract one both in (87) and in (88) to discount the all-zeros n-string"; "w≥2 (n + 2) is A077855", "w≥3 (n) is A130578", "w≥4 (n) is A209231". https://oeis.org/A209231 (read 2026-10-25) - "Number of binary words of length n such that there is at least one 0  and every run of consecutive 0's is of length >= 4", offset 0, data `0, 0, 0, 0, 1, 3, 6, 10, 15, 22, 33, 51, …`. Verified by execution (Python 3.11 with SymPy, 2026-10-25): the lengthening map, a bijection from the castles of height `h` with every column 1 or `h` (every castle of height 2 at `h = 2`) and semi-perimeter `s` onto the nonzero binary strings of length `s − 1` whose runs of 1s are all at least `h` long, for `h ≤ 5`, `s ≤ 14`; the count `spacing_h(s − h, 2) − 1` for `h ≤ 9`, `s ≤ h + 11`; `A209231(s − 1)` at `h = 4` for `s ≤ 14`; `(1 − x)² − x^{10} = −(x² − x + 1)(x³ + x² − 1)(x⁵ − x + 1)`.
