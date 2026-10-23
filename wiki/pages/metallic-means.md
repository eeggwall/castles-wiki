---
title: Metallic means
category: Concepts
summary: De Spinadel's metallic means σ_p^q = (p + √(p² + 4q))/2, the positive roots of x² − px − q for natural p and q, the growth rates of the recurrences x_n = p·x_{n−1} + q·x_{n−2}. The named members are golden σ_1^1 = φ, silver σ_2^1 = 1 + √2, bronze σ_3^1 = (3 + √13)/2, copper σ_1^2 = 2 and nickel σ_1^3 = (1 + √13)/2. The members δ_a = σ_a^1 are units of norm −1 with continued fraction [a; a, a, …]; every unit of norm −1 greater than 1 in a real quadratic field is one of them. On castles, the ridge castles of height h grow like δ_{h−1} by width and the tree castles of height h like σ_1^{h−1}, and a strip denominator 1 − p_1x − p_2x² grows at σ_{p_1}^{p_2}.
tags: [concept, metallic-mean, golden-ratio, silver-ratio, pell, fibonacci, continued-fraction, quadratic-irrational, norm-minus-one]
sources: [pe502-pell-castle-strip, calugareanu-hamburg-exercises-basic-ring-theory, de-spinadel-1999-family-of-metallic-means]
created: 2026-09-15
updated: 2026-10-22
---

# Metallic means

## Definition

The **metallic means** are Vera W. de Spinadel's Metallic Means Family: for natural numbers `p` and `q`, the positive root

```
σ_p^q  =  (p + √(p² + 4q)) / 2
```

of `x² − p·x − q = 0`. If `x_n = p·x_{n−1} + q·x_{n−2}` with positive starting values, then `x_{n+1}/x_n → σ_p^q` ([[de-spinadel-1999-family-of-metallic-means](pages/de-spinadel-1999-family-of-metallic-means.md)]).[^1] For example, `p = q = 1` gives the Fibonacci numbers `0, 1, 1, 2, 3, 5, 8, …`, whose ratios tend to the golden mean `σ_1^1 = (1 + √5)/2 = φ`.

The wiki writes the members with `q = 1`, the positive roots of `x² − a·x − 1`, as

```
δ_a  =  σ_a^1  =  (a + √(a² + 4)) / 2,        a = 1, 2, 3, …
```

## The named members

De Spinadel names five members.[^1] The wiki uses these names and no others, and writes every other member by its symbol. The table gives the named members and the `δ_a` for `a ≤ 5`, with the sequence `x_n = p·x_{n−1} + q·x_{n−2}` from `x_0 = 0`, `x_1 = 1`:

| `(p, q)` | member | value | continued fraction | name | `x_n` for `n = 0, 1, 2, …` | OEIS |
|---|---|---|---|---|---|---|
| (1, 1) | `σ_1^1 = δ_1` | `(1 + √5)/2 ≈ 1.6180` | `[1; 1, 1, …]` | golden | `0, 1, 1, 2, 3, 5, 8, 13, 21, 34, …` (Fibonacci) | `A000045` |
| (2, 1) | `σ_2^1 = δ_2` | `1 + √2 ≈ 2.4142` | `[2; 2, 2, …]` | silver | `0, 1, 2, 5, 12, 29, 70, 169, 408, 985, …` (Pell) | `A000129` |
| (3, 1) | `σ_3^1 = δ_3` | `(3 + √13)/2 ≈ 3.3028` | `[3; 3, 3, …]` | bronze | `0, 1, 3, 10, 33, 109, 360, 1189, 3927, 12970, …` | `A006190` |
| (4, 1) | `σ_4^1 = δ_4` | `2 + √5 ≈ 4.2361` | `[4; 4, 4, …]` | | `0, 1, 4, 17, 72, 305, 1292, 5473, 23184, 98209, …` | `A001076` |
| (5, 1) | `σ_5^1 = δ_5` | `(5 + √29)/2 ≈ 5.1926` | `[5; 5, 5, …]` | | `0, 1, 5, 26, 135, 701, 3640, 18901, 98145, 509626, …` | `A052918(n−1)` |
| (1, 2) | `σ_1^2` | `2` | `[2]` | copper | `0, 1, 1, 3, 5, 11, 21, 43, …` (Jacobsthal) | `A001045` |
| (1, 3) | `σ_1^3` | `(1 + √13)/2 ≈ 2.3028` | `[2; 3, 3, …]` | nickel | `0, 1, 1, 4, 7, 19, 40, 97, …` | `A006130(n−1)` |

Every sequence agrees with the OEIS data at the stated offsets.[^2] Copper is an integer, and the members with `p = 1` include every integer `n ≥ 2`, as `σ_1^{n² − n} = n`: `x² − x − (n² − n) = (x − n)(x + n − 1)`, so `q = 2, 6, 12, 20, …`.[^3] Copper and nickel are not of the form `δ_a`. Nickel is bronze minus 1, so it lies in the field `Q(√13)` of bronze.

The silver mean is `1 + √2`, de Spinadel's `σ_2^1`, and the wiki uses "silver" only for it.[^4]

## Continued fractions and units

Each `δ_a` satisfies `δ_a = a + 1/δ_a`, so its continued fraction is `[a; a, a, …]`. The other root of `x² − a·x − 1` is `δ̂_a = −1/δ_a = (a − √(a² + 4))/2`, which lies in `(−1, 0)`. A quadratic irrational greater than 1 whose conjugate lies in `(−1, 0)` is called reduced, and by Galois's theorem a quadratic irrational has a purely periodic continued fraction exactly when it is reduced ([[eigenvalue-continued-fractions](pages/eigenvalue-continued-fractions.md)]).[^5]

The sequence `x_n` of `δ_a` from `x_0 = 0`, `x_1 = 1` is

```
x_n  =  (δ_a^n − δ̂_a^n) / (δ_a − δ̂_a),
```

and since `|δ̂_a| < 1`, `x_{n+1}/x_n → δ_a`. The convergents `p_n/q_n` of `[a; a, a, …]` are `x_{n+2}/x_{n+1}`: numerator and denominator are the same sequence, one step apart. The Lucas sequence of the second kind `y_n = V_n(a, −1)`, with `y_0 = 2`, `y_1 = a` and `y_n = a·y_{n−1} + y_{n−2}`, is the trace `δ_a^n + δ̂_a^n`, equal to `p_n + q_{n−1}`. It is the Lucas numbers `A000032` at `a = 1`, the companion Pell numbers `A002203` at `a = 2` (whose half is `A001333`, the numerators of the convergents of `√2`), and `A006497`, `A014448`, `A087130` at `a = 3, 4, 5`.[^6] [[castle-eigenvalue-oeis-crosswalk](pages/castle-eigenvalue-oeis-crosswalk.md)] tabulates the convergents of each `δ_a` for `a ≤ 5`.

**`δ_4 = φ³`.** Since `φ² = φ + 1`, `φ³ = 2φ + 1 = 2 + √5 = δ_4`, and de Spinadel records the same identity.[^7] So `δ_4` lies in `Q(√5)`, the field of `φ`, and its sequence `0, 1, 4, 17, 72, 305, …` is `F_{3n}/2`, half of every third Fibonacci number.[^8] More generally, if `δ = δ_b` and `n` is odd, then `δ^n` has norm `(−1)^n = −1`, so `δ^n = δ_t` with `t` its trace. For `a ≤ 100` the `δ_a` that are odd powers of a smaller `δ_b` are those with `a = 4, 11, 14, 29, 36, 76, 82`: `φ³`, `φ⁵`, `(1 + √2)³`, `φ⁷`, `δ_3³`, `φ⁹ = δ_4³` and `(1 + √2)⁵`.[^9] The `δ_a` with `a = 1, 2, 3, 5, 6, 7, 8, 9, 10` lie in nine different fields, `Q(√5)`, `Q(√2)`, `Q(√13)`, `Q(√29)`, `Q(√10)`, `Q(√53)`, `Q(√17)`, `Q(√85)` and `Q(√26)`.

**Every unit of norm `−1` is a metallic mean.** If `ε > 1` is a unit of norm `−1` in a real quadratic field of fundamental discriminant `D0`, then `ε = (t + u√D0)/2` with `t² − u²D0 = −4`, so `ε = (t + √(t² + 4))/2 = δ_t`. A unit `u + vδ_a > 1` of `Z[δ_a]` has `v ≥ 1` and trace at least `a`, so `δ_a` is the fundamental unit of the ring `Z[δ_a]`. It is the fundamental unit of its field unless it is an odd power of a smaller `δ_b`, as `δ_4 = φ³` is in `Q(√5)`, whose fundamental unit is `φ`.[^10]

## The ring of each δ_a

`δ_a` generates the ring `Z[δ_a] = Z[x]/(x² − a·x − 1)` of integer combinations of its powers, and two `δ_a` can share a field without generating isomorphic rings. A ring isomorphism carries solutions of an equation to solutions, so rings can be told apart by the equations they solve: `x² = 1 + 1` has a solution in `Z[√2]` and none in `Z[√3]`, so `Z[√2] ≇ Z[√3]`.[^11]

Write the discriminant of `x² − a·x − 1` as `a² + 4 = f²·D0` with `D0` a fundamental discriminant. Then `Z[δ_a]` is the subring of index `f`, the conductor, in the ring of integers of `Q(√D0)`, and it is the whole ring of integers exactly when `f = 1`:[^12]

| `a` | `a² + 4` | field `Q(√D0)` | index `f` | |
|---|---|---|---|---|
| 1, 2, 3, 5, 6, 7, 9, 10, 13 | 5, 8, 13, 29, 40, 53, 85, 104, 173 | nine different fields | 1 | the whole ring of integers |
| 4 | 20 | `Q(√5)` | 2 | `δ_4 = φ³`, the ring `Z[√5]` |
| 8 | 68 | `Q(√17)` | 2 | not a power of a smaller `δ_b` |
| 11 | 125 | `Q(√5)` | 5 | `δ_11 = φ⁵` |
| 12 | 148 | `Q(√37)` | 2 | |
| 14 | 200 | `Q(√2)` | 5 | `δ_14 = (1 + √2)³` |

If `δ = δ_b` and `n` is odd, write `δ^n = U_n δ + U_{n−1}`, with `U_n` the Fibonacci numbers `F_n` for `b = 1` and the Pell numbers `P⋆_n` for `b = 2`. Then `Z[δ^n] = Z + U_n δ Z` has index `U_n` in `Z[δ]`: `δ_4 = φ³` has index `F_3 = 2` in `Z[φ]`, `δ_11 = φ⁵` index `F_5 = 5`, and `δ_14 = (1 + √2)³` index `P⋆_3 = 5` in `Z[√2]`.[^12]

Golden and `δ_4` both lie in `Q(√5)`, but `x² = x + 1` has the solution `φ` in `Z[φ]` and none in `Z[√5]`, where its roots `(1 ± √5)/2` would need half-integer coordinates. So `Z[δ_1] ≇ Z[δ_4]`.

## Metallic means on castles

A family of castles, or of strips, is **golden by width** when its counts by width grow like `φ^w`, and the same for the other members and the other axes: area, blocks, or the length of a word ([[castle-classification-growth](pages/castle-classification-growth.md)]). Strips need not reach their top height, so they need not be castles of that height.

- **Golden.** The Fibonacci castles, the castles of height 2 with no two neighboring columns of height 2, number `F_{w+2} − 1` and are golden by width ([[fibonacci-castle](pages/fibonacci-castle.md)]). The prime castles, those with no column of height 1, number `F_{n−1}` at area `n` and are golden by area ([[prime-castles](pages/prime-castles.md)]).
- **Silver.** The 1-smooth strips on the heights `{1, 2, 3}` with first column at height 1 number `P⋆_w`, with generating function `1/(1 − 2x − x²)`, and are silver by width ([[pell-castle-strip](pages/pell-castle-strip.md)], [[pell-numbers](pages/pell-numbers.md)]). The ridge castles of height 3 are silver by width (next item). The tower words, counted by their total number of steps `U`, `R` and `D`, are `A004149` and silver by that length ([[tower-word-continued-fraction](pages/tower-word-continued-fraction.md)]).
- **`δ_{h−1}`: ridge castles.** The ridge rule allows neighboring columns of equal height only at the top height `h` ([[ridge-castle](pages/ridge-castle.md)]). Its transfer matrix `R_h = J − D`, with `J` the all-ones matrix and `D = diag(1, …, 1, 0)`, has characteristic polynomial `(x + 1)^{h−2}(x² − (h−1)x − 1)` and largest eigenvalue `δ_{h−1}` ([[metallic-strip-realizability](pages/metallic-strip-realizability.md)]). The ridge castles of height `h` number `𝟙ᵀ R_h^{w−1} 𝟙 − (h − 1)(h − 2)^{w−1}`, the ridge strips minus those that stay below `h`, so they are `δ_{h−1}` by width: silver at `h = 3` (`1, 5, 15, 39, 97, …`), bronze at `h = 4` (`1, 7, 31, 118, 421, …`), and `δ_4 = φ³` at `h = 5`, where the ridge strips number `F_{3w+2}` and the ridge castles of height 5 number `F_{3w+2} − 4·3^{w−1}` (`1, 9, 53, 269, 1273, …`).[^13]
- **`σ_1^{h−1}`: tree castles.** The tree castles of height `h`, those with no two neighboring columns of height at least 2, grow like `σ_1^{h−1} = (1 + √(4h − 3))/2` by width: golden at `h = 2`, copper at `h = 3` and nickel at `h = 4`. The tree skylines of height at most 3 and 4 are the Jacobsthal numbers `3, 5, 11, 21, 43, …` and `4, 7, 19, 40, 97, …` (`A006130`) ([[castle-graph](pages/castle-graph.md)], section *Counting tree castles by width*).[^14]

**Strip denominators.** A strip whose generating function has the denominator `1 − p_1 x − p_2 x²`, with `p_1, p_2 ≥ 1`, grows at `σ_{p_1}^{p_2}`, which is a `δ_a` exactly when `p_2 = 1`. On the heights `{1, 2, 3}`, the unrestricted rule gives `3 = σ_1^6`, the rule with no two neighboring columns at height 3 gives `1 + √3 = σ_2^2` (characteristic polynomial `x(x² − 2x − 2)`), and the 1-smooth rule gives silver ([[metallic-strip-realizability](pages/metallic-strip-realizability.md)]).[^13] A 0/1 matrix of size 3 has largest eigenvalue at most 3, below bronze `δ_3 ≈ 3.303`, so no rule on three heights is bronze. The ridge matrix `R_h` has the quadratic factor `x² − (h−1)x − 1`, with `p_2 = 1`, at every height. [[quadratic-min-height](pages/quadratic-min-height.md)] gives, for each pair `(p_1, p_2)`, the fewest heights on which some rule grows at the larger root of `x² − p_1 x − p_2`: `δ_a` needs `a + 1` heights, and nickel `σ_1^3` needs 4.

By area, the castles of height at most 3 grow at the tribonacci constant, and the tree skylines of height at most 3, counted by `A006498`, at `φ`: their denominator `1 − q − q³ − q⁴` factors as `(1 + q²)(1 − q − q²)` ([[tree-castle-by-area](pages/tree-castle-by-area.md)]).

## Appearances in Sources

- [[de-spinadel-1999-family-of-metallic-means](pages/de-spinadel-1999-family-of-metallic-means.md)] - the Metallic Means Family `σ_p^q`, its five named members, its integer members, and `σ_4^1 = φ³`.
- [[pe502-pell-castle-strip](pages/pe502-pell-castle-strip.md)] - the generating function `1/(1 − 2x − x²)` of the silver strip.
- [[calugareanu-hamburg-exercises-basic-ring-theory](pages/calugareanu-hamburg-exercises-basic-ring-theory.md)] - Exercise 4.11, the ring-isomorphism test of the section *The ring of each δ_a*.

## Related Concepts

- [[pell-numbers](pages/pell-numbers.md)] - the sequence `x_n` of silver.
- [[pell-castle-strip](pages/pell-castle-strip.md)] - the anchored 1-smooth strips on `{1, 2, 3}`, counted by the Pell numbers.
- [[metallic-strip-realizability](pages/metallic-strip-realizability.md)] - which metallic means are the largest eigenvalues of strip transfer matrices, and the ridge rule.
- [[ridge-castle](pages/ridge-castle.md)] - the ridge castles of height `h`, which grow like `δ_{h−1}` by width.
- [[castle-graph](pages/castle-graph.md)] - the tree castles and their growth `σ_1^{h−1}`.
- [[castle-classification-growth](pages/castle-classification-growth.md)] - the classification of castle families by growth.
- [[golden-silver-bronze-plastic-castles](pages/golden-silver-bronze-plastic-castles.md)] - golden, silver, bronze and the plastic number `ψ` compared by width, area, semi-perimeter and adjacency spectrum: of the three metallic means only golden occurs by area, and `ψ` is the spectral radius of no castle graph.
- [[quadratic-min-height](pages/quadratic-min-height.md)] - the fewest heights on which a strip rule grows at a given quadratic constant.
- [[eigenvalue-continued-fractions](pages/eigenvalue-continued-fractions.md)] - continued fractions of quadratic irrationals, the theorems of Lagrange and Galois, and the continued fractions of `φ` and `1 + √2`.
- [[castle-eigenvalue-oeis-crosswalk](pages/castle-eigenvalue-oeis-crosswalk.md)] - the convergents and traces of `δ_a` for `a ≤ 5` matched to the OEIS, and `δ_a^{p+1} = −1` modulo a prime `p` that is inert in `Q(√(a² + 4))`.
- [[tower-word-continued-fraction](pages/tower-word-continued-fraction.md)] - the tower words, silver by length.
- [[prime-castles](pages/prime-castles.md)] - the prime castles, golden by area.
- [[aocp-generating-functions](pages/aocp-generating-functions.md)] - Knuth's method for the generating function of the Fibonacci numbers.
- [[castle-graph-spectral-radius](pages/castle-graph-spectral-radius.md)] - metallic means as spectral radii of castle graphs: `φ` for the six castles whose graph is the path on 4 vertices, and `1 + √2` for 36 castles up to mirror image in a scan to width 10.
- [[spectral-analysis](pages/spectral-analysis.md)] - the spectral methods used on castles.
- [[algebraic-transcendental-wall](pages/algebraic-transcendental-wall.md)] - the algebraic constants in the closed forms of C-finite castle counts.
- [[hardy-ramanujan-castle](pages/hardy-ramanujan-castle.md)] - Ramanujan's solutions of `x³ + y³ = z³ ± 1` grow term to term by `δ_9² = (83 + 9√85)/2`, whose continued fraction is `[82; 1, 81, 1, 81, …]`.
- [[fractional-recurrences](pages/fractional-recurrences.md)] - the growth of the recurrence `∇^α a_n = a_{n−1}` as a function of its order `α`, which equals `φ` at `α = 1/2`.
- [[castles-of-height-h-by-area](pages/castles-of-height-h-by-area.md)] - castles of height `h` by area, which grow at the `h`-nacci constants; only the case `h = 2`, golden, is a metallic mean.
- [[castle-snippets-number-theory](pages/castle-snippets-number-theory.md)] - `metallic_ring(a)`, which computes `D0` and `f` for `Z[δ_a]`.

## Footnotes

[^1]: [[de-spinadel-1999-family-of-metallic-means](pages/de-spinadel-1999-family-of-metallic-means.md)] §1 L27, §3 L137-205 - "Let me introduce you to the Metallic Means Family (MMF). Their members have, among other common characteristics, the property of carrying the name of a metal"; the family is the positive solutions of `x² − px − q = 0` for natural `p`, `q`; "if p = 2 y q = 1 we obtain the Silver Mean", "If p = 3 and q = 1, we get the Bronze Mean", `σ_4^1 = 2 + √5` unnamed, "If p = 1 and q = 2, we obtain the Copper Mean", "If p = 1 and q = 3, we get the Nickel Mean" `(1 + √13)/2` (formulas transcribed from the page's images). The Bridges 2003 paper (https://archive.bridgesmathart.org/2003/bridges2003-415.pdf, read 2026-10-09, p.420) gives the same copper and nickel means. De Spinadel's *New Smarandache sequences: the family of metallic means* (https://fs.unm.edu/SNJ/NewSmarandacheSequences-8.pdf, read 2026-10-10 against the page images, since the text layer is OCR) states the family on p.2 as "the positive solution of algebraic equations of the types" `x² − n x − 1 = 0` and `x² − x − n = 0`, and gives on p.10, eqs. (3.9)-(3.10), the copper and nickel sequences `1, 1, 3, 5, 11, 21, 43, 85, …` and `1, 1, 4, 7, 19, 40, 97, …`.
[^2]: https://oeis.org/A000045, A000129, A006190, A001076, A052918, A001045, A006130 (read 2026-10-16): `A052918` starts `1, 5, 26, …` and `A006130` starts `1, 1, 4, 7, …`, so `x_n = A052918(n−1)` and `x_n = A006130(n−1)` for `n ≥ 1`; the other five start at `x_0 = 0`. The sequences were iterated from the recurrences (Python 3.11, 2026-10-16).
[^3]: [[de-spinadel-1999-family-of-metallic-means](pages/de-spinadel-1999-family-of-metallic-means.md)] §3 L206-209 - "the integer metallic means ... appear in quite a regular way. The first for q = 2 ..., the second for q = 6 ..., the third for q = 12 ..., the forth for q = 20".
[^4]: [[de-spinadel-1999-family-of-metallic-means](pages/de-spinadel-1999-family-of-metallic-means.md)] §3 L165 - "if p = 2 y q = 1 we obtain the Silver Mean", `σ_Ag = [2̄] = 1 + √2` (transcribed).
[^5]: The theorems of Lagrange (a real number has an eventually periodic continued fraction exactly when it is a quadratic irrational) and Galois (purely periodic exactly when reduced) are stated on [[eigenvalue-continued-fractions](pages/eigenvalue-continued-fractions.md)]. `δ_a = a + 1/δ_a` and the bound `−1 < δ̂_a < 0` hold for every `a ≥ 1`, since `δ_a > 1`.
[^6]: Verified by execution (Python 3.11, 2026-10-16): the sequences `V_n(a, −1)` for `a ≤ 5` against https://oeis.org/A000032, A002203, A001333, A006497, A014448 and A087130 (read 2026-10-16); `x_29/x_28` against `δ_a` to ten decimal places for `a ≤ 5`.
[^7]: [[de-spinadel-1999-family-of-metallic-means](pages/de-spinadel-1999-family-of-metallic-means.md)] §3 L175-182 - "For p = 4; q = 1, the metallic mean" `σ_4^1 = 2 + √5 = [4̄] = φ³` (transcribed), "a striking result related to the continued fraction expansion of uneven powers of the Golden Mean."
[^8]: Verified by execution (Python 3.11, 2026-10-16): the first ten terms of `x_n = 4x_{n−1} + x_{n−2}` equal `F_{3n}/2`.
[^9]: Verified by execution (Python 3.11, 2026-10-16): the traces `V_n = b·V_{n−1} + V_{n−2}` (`V_0 = 2`, `V_1 = b`) of `δ_b^n` for odd `n ≥ 3` and `b ≤ 100` that are at most 100 are exactly `4, 11, 14, 29, 36, 76, 82`; the squarefree parts of `a² + 4` for `a ≤ 10`.
[^10]: A unit of norm `−1` in the ring of integers of `Q(√D0)` has the form `(t + u√D0)/2` with integers `t`, `u`. The fundamental unit of `Z[φ]` is `φ`, and the fundamental unit of `Z[√2]` is `1 + √2`.
[^11]: [[calugareanu-hamburg-exercises-basic-ring-theory](pages/calugareanu-hamburg-exercises-basic-ring-theory.md)] Ex. 4.11 p.21; solution p.109 [synthesis] - a ring isomorphism preserves elements with `x² = 1 + 1`; `Z[√2]` has one and `Z[√3]` does not (`a² + 3b² = 2, 2ab = 0` has no integer solution); generalized there to `Z[√d] ≇ Z[√e]` for distinct squarefree `d, e`.
[^12]: Verified by execution (Python 3.10, SymPy, 2026-09-26): `a² + 4 = f² D0` for `a = 1..20` (the table rows are the `a ≤ 14` entries; `a = 16, 20` also have `f = 2`); `φ³ = 2 + √5`, `φ⁵ = (11 + 5√5)/2`, `(1 + √2)³ = 7 + 5√2` by `sp.expand`; indices `U_3 = 2`, `U_5 = 5` (`b = 1`) and `U_3 = 5` (`b = 2`) from `U_n = b U_{n−1} + U_{n−2}`. Pinned under `metallic_ring` on [[castle-snippets-number-theory](pages/castle-snippets-number-theory.md)].
[^13]: Verified by execution (Python 3.11 with SymPy, 2026-10-16): the characteristic polynomial of `R_5`, `(x + 1)³(x² − 4x − 1)`; the ridge castles of heights 3, 4 and 5 for `w ≤ 6` by enumeration against the formula; `𝟙ᵀ R_5^{w−1} 𝟙 = F_{3w+2}` for `w ≤ 8`; the characteristic polynomial `x(x² − 2x − 2)` of the rule on `{1, 2, 3}` with no two neighboring columns at height 3.
[^14]: [[tree-castle-by-area](pages/tree-castle-by-area.md)] gives `T_h(w, q) = q·T_h(w−1, q) + q·P_h(q)·T_h(w−2, q)` with `P_h(1) = h − 1`. Verified by execution (2026-10-09 and 2026-10-16): the tree skylines by width, `w = 1..8`, are `3, 5, 11, 21, 43, 85, 171, 341` at height at most 3 (`A001045` from `n = 3`) and `4, 7, 19, 40, 97, 217, 508, 1159` at height at most 4 (`A006130` from `n = 2`); https://oeis.org/A001045 and https://oeis.org/A006130 (fetched 2026-10-09) - "Jacobsthal sequence ... a(n) = a(n-1) + 2*a(n-2)" and "a(n) = a(n-1) + 3*a(n-2) for n > 1, a(0) = a(1) = 1".
