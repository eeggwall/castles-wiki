---
title: Metallic means
category: Concepts
summary: The family of quadratic irrationals `δ_a = (a + √(a²+4))/2` for a = 1, 2, 3, … — the roots of `x² − ax − 1 = 0`. Each is a norm-`−1` reduced surd with purely periodic continued fraction `[a; a, a, …]`; the first two are golden (`φ`) and silver (`1+√2`), the family the wiki's continued-fraction and eigenvalue threads sit inside.
tags: [concept, metallic-mean, golden-ratio, silver-ratio, pell, fibonacci, continued-fraction, quadratic-irrational, norm-minus-one]
sources: [pe502-pell-castle-strip, calugareanu-hamburg-exercises-basic-ring-theory]
created: 2026-09-15
updated: 2026-10-10
---

# Metallic means

## Definition

The **metallic means** are the family of positive real numbers

```
δ_a  =  (a + √(a² + 4)) / 2,      a = 1, 2, 3, 4, 5, …,
```

each the positive root of the monic quadratic `x² − a·x − 1 = 0`. The family and its name are due to Vera W. de Spinadel, who defined it more broadly, as the positive roots of `x² − p·x − q` for natural numbers `p` and `q`; the `q = 1` line is this page's `δ_a`, with `a = p`.[^1] On this wiki "metallic means" means the `q = 1` line only.

Each member `δ_a` is a **norm-`−1` reduced quadratic surd** — its conjugate `(a − √(a²+4))/2` sits in `(−1, 0)` — so by Galois' theorem (see [[eigenvalue-continued-fractions](pages/eigenvalue-continued-fractions.md)]) its continued-fraction expansion is **purely periodic of period one**:

```
δ_a  =  [a; a, a, a, …].
```

The members share the Fibonacci-like recurrence `x_n = a·x_{n−1} + x_{n−2}` (integer sequence realization) and the characteristic polynomial `x² − a·x − 1` (algebraic side), with `a` the only parameter.[^2]

## The named members

| `a` | `δ_a` | de Spinadel's name | Integer sequence (`x_0 = 0, x_1 = 1`) | Online Encyclopedia of Integer Sequences (OEIS) |
|---|---|---|---|---|
| 1 | `(1+√5)/2 ≈ 1.6180` | **Golden** | 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, … — Fibonacci | [A000045](https://oeis.org/A000045) |
| 2 | `1+√2 ≈ 2.4142` | **Silver** | 0, 1, 2, 5, 12, 29, 70, 169, 408, 985, … — Pell | [A000129](https://oeis.org/A000129) |
| 3 | `(3+√13)/2 ≈ 3.3028` | **Bronze** | 0, 1, 3, 10, 33, 109, 360, 1189, 3927, 12970, … | [A006190](https://oeis.org/A006190) |
| 4 | `2+√5 ≈ 4.2361` | — | 0, 1, 4, 17, 72, 305, 1292, 5473, 23184, 98209, … | [A001076](https://oeis.org/A001076) |
| 5 | `(5+√29)/2 ≈ 5.1926` | — | 0, 1, 5, 26, 135, 701, 3640, 18901, 98145, 509626, … | [A052918](https://oeis.org/A052918) (offset: `A052918(n) = x_{n+1}`) |

All five OEIS identifications are verified offset-exact against the OEIS data (2026-09-16, on [[castle-eigenvalue-oeis-crosswalk](pages/castle-eigenvalue-oeis-crosswalk.md)]); A052918 lists `1, 5, 26, …`, i.e. `x_{n+1}`. Companion sequences (`y_0 = 2, y_1 = a, y_n = a·y_{n−1} + y_{n−2}`) - Lucas A000032 for `a=1`, companion Pell A002203 for `a=2` (A001333, the numerators of the convergents of `√2`, is its half), A006497 / A014448 / A087130 for `a = 3, 4, 5` - are the `δ_a^n + δ̂_a^n` traces of the same characteristic polynomial. The convergents `p_n/q_n` of `[a; a, a, …]` are `x_{n+2}/x_{n+1}` - numerator and denominator are the *same* sequence, one step apart - and the trace appears as `p_n + q_{n−1}`; see the crosswalk page for the full table.[^3]

## Names

De Spinadel names five members of her two-parameter family by `(p, q)`, the roots of `x² − p x − q`: golden `(1, 1)`, silver `(2, 1)`, bronze `(3, 1)`, copper `(1, 2)` and nickel `(1, 3)`.[^4][^10] Golden, silver and bronze are the rungs `δ_1, δ_2, δ_3` of this page. Her copper and nickel are not rungs: copper is the root of `x² − x − 2`, the whole number 2, and nickel is the root of `x² − x − 3`, `(1 + √13)/2 ≈ 2.3028`, which is bronze minus 1. She gives `(4, 1)` no metal name, only noting its link to odd powers of the golden mean, and names no rung above it.

So the wiki names only golden, silver and bronze, and writes `δ_a` for every rung from `a = 4` on. De Spinadel's copper and nickel are the pairs `(p1, p2) = (1, 2)` and `(1, 3)` on [[quadratic-min-height](pages/quadratic-min-height.md)], where `(1, 3)` first appears at height 4. Her symbols are `φ` for golden and `σ` with the element as subscript for the others (`σ_Ag`, `σ_Br`, `σ_Cu`, `σ_Ni`); the wiki writes `δ_a` throughout.

## The `a=4` coincidence: δ_4 = φ³

`δ_4 = 2 + √5 = φ³` (since `φ² = φ + 1`, so `φ³ = 2φ + 1 = 1 + √5 + 1 = 2 + √5`).[^5] So the `a=4` member is a power of the golden ratio in `Q(√5)`, and it generates the smaller ring `Z[√5]` (index 2 in `Z[φ]`). The `a=4` integer sequence 0, 1, 4, 17, 72, 305, 1292, 5473, 23184, 98209 is `F_{3n}/2` (every third Fibonacci number, halved). It is the first of an infinite family of such coincidences: whenever `δ_a` is an odd power of a smaller rung it shares that rung's field, as `δ_11 = φ⁵` (also in `Q(√5)`) and `δ_14 = (1 + √2)³` (in `Q(√2)`) do; for `a ≤ 100` the full list is `a = 4, 11, 14, 29, 36, 76, 82` (see "Which ring each rung generates" below). The rungs `a = 1, 2, 3, 5, 6, 7, 8, 9, 10` all sit in distinct real quadratic fields.

## The family on the wiki

Two members appear on the wiki independently:

- **`δ_1 = φ`** is the growth constant of Fibonacci, which appears in the castle count as the `F_{n−1}` prime castles and `2^{n−1} − F_{n−1}` composite castles of [[prime-castles](pages/prime-castles.md)]. The Fibonacci method for turning a recurrence into a rational generating function (GF) is the archetype of [[aocp-generating-functions](pages/aocp-generating-functions.md)].
- **`δ_2 = 1+√2`** is the growth constant of the tower word ([[tower-word-continued-fraction](pages/tower-word-continued-fraction.md)]), and appears as the count-sequence growth of the anchored 1-smooth height-3 strip on [[pell-castle-strip](pages/pell-castle-strip.md)], whose width generating function is exactly `1/(1 − 2x − x²)`. The integer realization is the [[pell-numbers](pages/pell-numbers.md)].

Both are treated in parallel on [[eigenvalue-continued-fractions](pages/eigenvalue-continued-fractions.md)] as "the castle's two norm-`−1` reduced quadratics". The family also gives a **classification axis** for castle sub-families: a castle class is a **"`<metal>` `<axis>` growth castle"** iff its count sequence, graded by the chosen size axis, grows at rate `δ_a`. This is Axis 8 of [[castle-classification-growth](pages/castle-classification-growth.md)]; the naming convention (`<metal>` ∈ {golden, silver, bronze}, then `δ_4`, `δ_5`, …; `<axis>` ∈ {width, vertical, area, block}) is developed there.

## Structural facts about the family

- **Binet-style formula.** Every member's recurrence-realization satisfies `x_n = (δ_a^n − δ̂_a^n) / (δ_a − δ̂_a)` with `δ̂_a = (a − √(a²+4))/2` the conjugate root. Growth is `x_{n+1}/x_n → δ_a`; the conjugate contribution decays because `|δ̂_a| < 1` for every `a ≥ 1`.
- **Purely periodic continued fraction.** `δ_a = [a; a, a, …]` since `δ_a = a + 1/δ_a` (i.e. `δ_a` is a fixed point of `x ↦ a + 1/x`), which [[eigenvalue-continued-fractions](pages/eigenvalue-continued-fractions.md)] develops. The conjugate `δ̂_a` sits in `(−1, 0)` for every `a ≥ 1`, so all members are Galois-reduced (norm `−1`, sum of roots `= a > 0`, product `= −1`), hence purely periodic.
- **Fundamental units.** Each `δ_a` is a unit of norm `−1`, and it is the fundamental unit of the ring it generates, `Z[δ_a]`. It is also the fundamental unit of its field `Q(√(a²+4))` unless it is an odd power of a smaller rung: `δ_4 = φ³` is a cube in `Q(√5)`, whose fundamental unit is `φ`. Conversely every norm `−1` unit greater than 1 in a real quadratic field is some `δ_t`, so the metallic means include the fundamental unit of every real quadratic field whose fundamental unit has norm `−1` ("Which ring each rung generates" below).[^6]
- **Root symmetry.** The roots of `x² − a·x − 1` multiply to `−1` (norm `−1`), so `x ↦ −1/x` swaps them (`x² p(−1/x) = −p(x)`), and the conjugate `−1/δ_a` lies in `(−1, 0)`, which is why the fraction is purely periodic ([[eigenvalue-continued-fractions](pages/eigenvalue-continued-fractions.md)] Step 3).

## Which ring each rung generates

A metallic mean generates more than a field. It generates a *ring*, `Z[δ_a] = Z[x]/(x² − a x − 1)`, the integer combinations of powers of `δ_a`, and two rungs can share a field without sharing a ring. The textbook way to tell rings apart is to ask which equations they can solve. An isomorphism of rings carries solutions of `x² = 1 + 1` to solutions, so `Z[√2]` (which has one) is not isomorphic to `Z[√3]` (which does not).[^7]

**The ring is an order of conductor `f`.** `disc(x² − a x − 1) = a² + 4 = f² · D0` with `D0` a fundamental discriminant. `Z[δ_a]` is the full ring of integers of `Q(√D0)` exactly when `f = 1`, and otherwise it sits inside with index `f`:[^8]

| `a` | `a² + 4` | field `Q(√D0)` | index `f` | note |
|---|---|---|---|---|
| 1, 2, 3, 5, 6, 7, 9, 10, 13 | 5, 8, 13, 29, 40, 53, 85, 104, 173 | each its own | 1 | full ring of integers |
| 4 | 20 | `Q(√5)` | 2 | `δ_4 = φ³`, ring `Z[√5]` |
| 8 | 68 | `Q(√17)` | 2 | not a power of a smaller rung |
| 11 | 125 | `Q(√5)` | 5 | `δ_11 = φ⁵` |
| 12 | 148 | `Q(√37)` | 2 | |
| 14 | 200 | `Q(√2)` | 5 | `δ_14 = (1 + √2)³` |

**Powers give Fibonacci-type indices.** If `δ = δ_b` and `n` is odd, `δ^n` has norm `−1` and trace `t`, so `δ^n = δ_t` is itself a rung. Writing `δ^n = U_n δ + U_{n−1}` (with `U_n` the Fibonacci numbers `F_n` for `b = 1` and the Pell numbers `P⋆_n` for `b = 2`), the ring it generates is `Z[δ^n] = Z + U_n δ Z`, of index `U_n` in `Z[δ]`. So `δ_4 = φ³` has index `F_3 = 2` in `Z[φ]`, `φ⁵ = δ_11` has index `F_5 = 5`, and `(1 + √2)³ = δ_14` has index `P⋆_3 = 5` in `Z[√2]`.[^8]

**Same field, different rings.** Golden `δ_1` and `δ_4` both live in `Q(√5)`, but `x² = x + 1` has the solution `φ` in `Z[φ]` and no solution in `Z[√5]` (its roots `(1 ± √5)/2` have half-integer coordinates). By the argument above, `Z[δ_1] ≇ Z[δ_4]`.

**Which rungs are fundamental units.** Every unit of norm `−1` that is greater than 1 in a real quadratic field is a metallic mean: if `ε = (t + u√D0)/2` has norm `−1` then `t² + 4 = u² D0`, so `ε = (t + √(t² + 4))/2 = δ_t`. So `δ_a` is the fundamental unit of its field unless it is an odd power of a smaller rung. For `a ≤ 100` that happens exactly for `a = 4, 11, 14, 29, 36, 76, 82` (`φ³, φ⁵, (1 + √2)³, φ⁷, δ_3³, φ⁹ = δ_4³, (1 + √2)⁵`).[^9]

## Castle classification: the Axis-8 realization

[[castle-classification-growth](pages/castle-classification-growth.md)] Axis 8 defines the meta-classification **`<metal>` `<axis>` growth castle**, with:

- **`<metal>`** ∈ {golden (`a=1`, `φ`), silver (`a=2`, `1+√2`), bronze (`a=3`, `(3+√13)/2`)}, then `δ_4` (`2+√5`), `δ_5` (`(5+√29)/2`), … by symbol — one per member of this family.
- **`<axis>`** ∈ {width, vertical, area, block} — the size parameter being graded, always stated explicitly.

The rungs with castle realizations:

1. **Silver width growth castle** — count sequence graded by width `w` grows at `1+√2`. Two known members: the **1-smooth height-3 strip** (`|c_{i+1} − c_i| ≤ 1`), whose denominator factors as `(1 − x)(1 − 2x − x²)` ([[metallic-strip-realizability](pages/metallic-strip-realizability.md)]) and which, anchored at height 1, is the [[pell-castle-strip](pages/pell-castle-strip.md)] with generating function exactly `1/(1 − 2x − x²)` and Pell-number counts (`p_1 = 2, p_2 = 1`), and the ridge castles at height 3, ridge rule `R_3 = J − D` (item 3 below). The tower word ([[tower-word-continued-fraction](pages/tower-word-continued-fraction.md)], algebraic GF, A004149) also grows at `1 + √2`, by word length rather than width.
2. **Golden width growth castle** — count sequence graded by `w` grows at `φ`. Known member: the height-2 tree castles ([[castle-graph](pages/castle-graph.md)]) — `{0,1}`-skyline above the base with no two adjacent raised columns and at least one, `F_{w+2} − 1` of them (Fibonacci, the `p_1 = 1, p_2 = 1` denominator). The prime castles, `F_{n−1}` of them by area with the height unrestricted ([[prime-castles](pages/prime-castles.md)]), are a **golden area growth castle** (a different axis); at a fixed exact height they grow more slowly (plastic at height 3, supergolden at height 4).

3. **Bronze, `δ_4`, `δ_5`, … width growth castles** — all realized, by **one named rule**: the **ridge rule** ([[ridge-castle](pages/ridge-castle.md)]) (adjacent columns differ in height unless both equal the max `h`; its castles of exact height `h` are the **ridge castles**, [[castle-classification-shape](pages/castle-classification-shape.md)] Axis 2), transfer matrix `R_h = J − D`, char poly `(x+1)^{h−2}(x² − (h−1)x − 1)`, Perron root `δ_{h−1}` ([[metallic-strip-realizability](pages/metallic-strip-realizability.md)]). So rung `a` sits at height `h = a + 1`: **bronze** at `h = 4`, `δ_4` at `h = 5`, `δ_5` at `h = 6`, and so on up the whole ladder. The `h = 5` rung is `δ_4 = 2 + √5 = φ³`, and its free ridge-strip count is `F_{3n+5}` (`n = 0, 1, 2, …` for width `n + 1`), a **Fibonacci trisection**.

**Realizability.** A castle-strip denominator `1 − p_1·x − p_2·x²` grows at `(p_1 + √(p_1² + 4·p_2))/2`, a metallic mean iff `p_2 = 1`, but `p_1` is not the number of states per column: `p_1` (forward states) and `p_2` (length-2 return loops) are *coupled* in symmetric height-`h` rules, so widening the alphabet drifts `p_2` off `1` (a 0/1 matrix on 3 states has spectral radius at most 3, below bronze's 3.30; the no-adjacent-ceiling height-3 rule gives the non-metallic `1 + √3`). The ridge rule `R_h = J − D` is the decoupling that keeps `p_2 = 1` at every height. The vertical and block axes have no known members; the area axis has the n-nacci and cubic-Pisot families of [[castle-classification-growth](pages/castle-classification-growth.md)].

**Cross-axis statements.** The tower word, a Motzkin-path type with a run constraint (Axis 3), grows at the silver ratio by word length (width plus twice the blocks), so it is a silver growth class on the word-length axis: its algebraic GF has its singularity at `√2 − 1`. The tree ban (Axis 9) lowers the area growth constant from tribonacci to golden at height 3. See [[castle-classification](pages/castle-classification.md)] for more.

## Appearances in Sources

- [[pe502-pell-castle-strip](pages/pe502-pell-castle-strip.md)] - the silver member's generating function `1/(1 − 2x − x²)`.
- [[calugareanu-hamburg-exercises-basic-ring-theory](pages/calugareanu-hamburg-exercises-basic-ring-theory.md)] - Ex. 4.11, the ring-isomorphism test behind "Same field, different rings".

The rest is standard number theory, verified by direct calculation. The definition and the metal names come from de Spinadel's two papers in footnotes 1, 4 and 10, both read.

## Related Concepts

- [[pell-numbers](pages/pell-numbers.md)] — the `a=2` integer sequence; the silver-mean member.
- [[golden-silver-bronze-plastic-castles](pages/golden-silver-bronze-plastic-castles.md)] — golden, silver and bronze beside the plastic number on every castle axis: all are width growth constants, only golden is an area one, and only the metallic means can be spectral radii of graphs.
- [[pell-castle-strip](pages/pell-castle-strip.md)] — the anchored 1-smooth height-3 strip realizing `δ_2 = 1+√2` with Pell-number counts.
- [[metallic-strip-realizability](pages/metallic-strip-realizability.md)] — which metallic means are actually castle-strip Perron roots: the `p_1`/`p_2` coupling obstruction, silver's third realization, and bronze needing four states.
- [[eigenvalue-continued-fractions](pages/eigenvalue-continued-fractions.md)] — the two members `φ` and `1+√2` already treated as the castle's norm-`−1` reduced quadratics; this page names the ladder they sit on.
- [[tower-word-continued-fraction](pages/tower-word-continued-fraction.md)] — where `1+√2` appears as the tower-word growth constant.
- [[aocp-generating-functions](pages/aocp-generating-functions.md)] — the Fibonacci / `φ` archetype (the `a=1` member).
- [[prime-castles](pages/prime-castles.md)] — the `F_{n−1}` prime castles by area, where Fibonacci / `φ` enters the castle count.
- [[algebraic-transcendental-wall](pages/algebraic-transcendental-wall.md)] — the metallic means are algebraic (quadratic), the exact irrationals that C-finite castle counts *can* carry.
- [[spectral-analysis](pages/spectral-analysis.md)] / [[castle-graph-spectral-radius](pages/castle-graph-spectral-radius.md)] - where the metallic means do and do not appear as eigenvalues: never in Project Euler 502 (PE 502)'s own signed transfer matrix (its eigenvalues are twice the roots of an integer polynomial with leading coefficient 2), but as spectral radii of class transfer matrices (Axis 8) and of individual castle graphs (`φ` for the 4-cell paths, `1 + √2` for the `3×2` rectangle and three non-rectangular castles).
- [[castle-eigenvalue-oeis-crosswalk](pages/castle-eigenvalue-oeis-crosswalk.md)] - the convergent numerator/denominator/trace sequences of every rung `a = 1..5` matched to OEIS, and the mod-`p` signature of norm `−1` (`δ_a^{p+1} = −1` at inert primes).
- [[block-count-constraints](pages/block-count-constraints.md)] - the coin branch touches the ladder: numerical semigroups counted by genus (A007323: 1, 1, 2, 4, 7, 12, 23, 39, …) grow at the golden ratio (Zhai 2013).

- [[hardy-ramanujan-castle](pages/hardy-ramanujan-castle.md)] - Ramanujan's near-miss family `x^3 + y^3 = z^3 +- 1` (the recurrence behind `9^3 + 10^3 = 12^3 + 1`) grows by `delta_9^2 = (83 + 9 sqrt 85)/2`, the ninth metallic mean squared; `delta_9 = [9; 9, 9, ...]` (norm `-1`) against `delta_9^2 = [82; 1, 81, 1, 81, ...]` (norm `+1`).
- [[fractional-recurrences](pages/fractional-recurrences.md)] - the ladder is a discrete slice through a continuum. The fractional-Fibonacci `∇^α a_n = a_{n-1}` has growth `g(α) = 1/r*(α)` a continuous bijection `[0,∞) → [1,∞)`, and the ladder crosses this curve at rational-`α` **only for golden** (`α = 1/2` exactly, because `δ_1 - 1 = 1/δ_1` is a unit while `N(δ_a - 1) = -a` for `a ≥ 2`). Silver, bronze, `δ_4`, `δ_5` land at transcendental orders `α ≈ 1.65, 3.31, 5.36, 7.70`.
- [[exact-height-castle-by-area](pages/exact-height-castle-by-area.md)] - the n-nacci growth constants `α_h` sit near but *off* the metallic ladder for `h ≥ 3`: `α_2 = δ_1` is golden, but tribonacci / tetranacci / … are not metallic.
- [[calugareanu-hamburg-exercises-basic-ring-theory](pages/calugareanu-hamburg-exercises-basic-ring-theory.md)] - Ex. 4.11 (isomorphisms preserve solutions of `x² = 2`, so `Z[√2] ≇ Z[√3]`), the tool behind "same field, different rings".
- [[castle-snippets-number-theory](pages/castle-snippets-number-theory.md)] - `metallic_ring(a)` computes the field and index of `Z[δ_a]`.

## Footnotes

[^1]: https://www.mi.sanu.ac.rs/vismath/spinadel/ §3 "The family of metallic means" — Vera W. de Spinadel, *The family of metallic means*, Visual Mathematics 1(3), 1999: "The metallic means family (MMF) is the set of positive eigenvalues of the matricial equation (3.1) for different values of p and q (natural numbers)." The paper's §2 builds the sequences `a, b, pb + qa, p(pb + qa) + qb, …`, so the members are the positive roots of `x² − p x − q`. Her *New Smarandache sequences: the family of metallic means* (https://fs.unm.edu/SNJ/NewSmarandacheSequences-8.pdf p.2, Abstract) states the same family as "the positive solution of algebraic equations of the types" `x² − n x − 1 = 0` and `x² − x − n = 0`.
[^2]: The reduced-quadratic-surd theory (Lagrange periodicity, Galois pure periodicity) applied to `x² − a·x − 1` for arbitrary integer `a ≥ 1` is a direct specialization of the general treatment on [[eigenvalue-continued-fractions](pages/eigenvalue-continued-fractions.md)]. The identity `δ_a = a + 1/δ_a`, which forces `δ_a = [a; a, a, …]`, was verified for `a = 1, 2, 3, 4, 5` during ingest by fixed-point iteration.
[^3]: The recurrence `x_n = a·x_{n−1} + x_{n−2}` with `x_0 = 0, x_1 = 1` was iterated for `a = 1..5` during ingest; the first ten values in the table match direct computation, and the ratio `x_29 / x_28` matches `δ_a` to ten decimal places for each `a` (Fibonacci: `1.6180339888` vs. `1.6180339887`; Pell: `2.4142135624` for both; and analogously for `a = 3, 4, 5`). The companion sequences (`y_0 = 2, y_1 = a`) were also iterated and identified for `a=1` (Lucas A000032) and `a=2` (companion Pell A002203 = `2, 2, 6, 14, 34, …`; A001333 = `1, 1, 3, 7, 17, …` is `y_n/2`). All five `a` were verified offset-exact against OEIS on 2026-09-16 ([[castle-eigenvalue-oeis-crosswalk](pages/castle-eigenvalue-oeis-crosswalk.md)]).
[^4]: https://www.mi.sanu.ac.rs/vismath/spinadel/ §3 — "if p = 2 y q = 1 we obtain the Silver Mean"; "If p = 3 and q = 1, we get the Bronze Mean". Her symbols `σ_Ag`, `σ_Br`, `σ_Cu`, `σ_Ni` are in https://fs.unm.edu/SNJ/NewSmarandacheSequences-8.pdf pp.5, 10 (the PDF's text layer is OCR; read against the page images).
[^5]: `φ² = φ + 1` (defining property of the golden ratio) gives `φ³ = φ·φ² = φ² + φ = 2φ + 1 = 1 + √5 + 1 = 2 + √5 = δ_4`; verified numerically during ingest (`φ³ = 4.2360679…`, matching `2 + √5 = 4.2360679…`). Consequence: the `a=4` integer sequence `x_n = 0, 1, 4, 17, 72, 305, 1292, 5473, 23184, 98209` equals `F_{3n}/2` where `F_n` is Fibonacci — `F_3 = 2, F_6 = 8, F_9 = 34, F_12 = 144, F_15 = 610, …`, divided by 2 gives `1, 4, 17, 72, 305, …`, matching exactly (re-verified during ingest against the Fibonacci sequence). So the `a=4` recurrence is a decimated / scaled Fibonacci, and the sequence sits inside `Q(√5)`, not in an independent quadratic field.
[^6]: The fundamental unit of `Z[φ]` (the ring of integers of `Q(√5)`) is the golden ratio `φ`, and the fundamental unit of the smaller ring `Z[√5]` is `φ³ = 2 + √5`, since `φ ∉ Z[√5]`; the fundamental unit of `Z[√2]` is `1 + √2` (both well-known). Dirichlet's unit theorem gives rank 1 for every real quadratic order. That `δ_a` is the fundamental unit of `Z[δ_a]`, and of its field exactly when it is not an odd power of a smaller rung, follows from the norm `−1` argument in "Which ring each rung generates"; the list of exceptions for `a ≤ 100` is verified there.
[^7]: [[calugareanu-hamburg-exercises-basic-ring-theory](pages/calugareanu-hamburg-exercises-basic-ring-theory.md)] Ex. 4.11 p.21; solution p.109 [synthesis] - a ring isomorphism preserves elements with `x² = 1 + 1`; `Z[√2]` has one and `Z[√3]` does not (`a² + 3b² = 2, 2ab = 0` has no integer solution); generalized there to `Z[√d] ≇ Z[√e]` for distinct squarefree `d, e`.
[^8]: Verified by execution (Python 3.10, SymPy, 2026-09-26): `a² + 4 = f² D0` for `a = 1..20` (table rows are the `a ≤ 14` entries; `a = 16, 20` also have `f = 2`); `φ³ = 2 + √5`, `φ⁵ = (11 + 5√5)/2`, `(1 + √2)³ = 7 + 5√2` by `sp.expand`; indices `U_3 = 2`, `U_5 = 5` (`b = 1`) and `U_3 = 5` (`b = 2`) from `U_n = b U_{n−1} + U_{n−2}`. Pinned under `metallic_ring` on [[castle-snippets-number-theory](pages/castle-snippets-number-theory.md)].
[^9]: Verified by execution (Python 3.10, 2026-09-26): traces `V_n = b V_{n−1} + V_{n−2}` (`V_0 = 2`, `V_1 = b`) of `δ_b^n` for odd `n ≥ 3` and `b ≤ 100`, keeping `V_n ≤ 100`: exactly `{4, 11, 14, 29, 36, 76, 82}`. The norm `−1` argument is standard (a unit of norm `−1` in `Z[(1 + √D0)/2]` has the form `(t + u√D0)/2`).
[^10]: https://www.mi.sanu.ac.rs/vismath/spinadel/ §3 — "If p = 1 and q = 2, we obtain the Copper Mean"; "If p = 1 and q = 3, we get the Nickel Mean"; "For p = 4; q = 1, the metallic mean is a striking result related to the continued fraction expansion of uneven powers of the Golden Mean." The same assignments, with the sequences `1, 1, 3, 5, 11, 21, 43, 85, …` (copper) and `1, 1, 4, 7, 19, 40, 97, …` (nickel), are in https://fs.unm.edu/SNJ/NewSmarandacheSequences-8.pdf p.10, eqs. (3.9)-(3.10).
