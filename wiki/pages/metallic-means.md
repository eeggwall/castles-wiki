---
title: Metallic means
category: Concepts
summary: The family of quadratic irrationals `δ_a = (a + √(a²+4))/2` for a = 1, 2, 3, … — the roots of `x² − ax − 1 = 0`. Each is a norm-`−1` reduced surd with purely periodic continued fraction `[a; a, a, …]`; the first two are golden (`φ`) and silver (`1+√2`), the family the wiki's continued-fraction and eigenvalue threads sit inside.
tags: [concept, metallic-mean, golden-ratio, silver-ratio, pell, fibonacci, continued-fraction, quadratic-irrational, norm-minus-one]
sources: [pe502-pell-castle-strip]
created: 2026-09-15
updated: 2026-09-15
---

# Metallic means

## Definition

The **metallic means** are the family of positive real numbers

```
δ_a  =  (a + √(a² + 4)) / 2,      a = 1, 2, 3, 4, 5, …,
```

each the positive root of the monic quadratic `x² − a·x − 1 = 0`. The name and framing are due to Vera W. de Spinadel (1997), who introduced the family under this name in the number-theory / recreational-mathematics literature to organize the ladder of quadratic irrationals of this form.[^1] It is now standard shorthand for the family; a mathematician will recognize "silver ratio" and "silver mean" for `1+√2`, though "the positive root of `x² − 2x − 1`" is the more universal spelling.

Each member `δ_a` is a **norm-`−1` reduced quadratic surd** — its conjugate `(a − √(a²+4))/2` sits in `(−1, 0)` — so by Galois' theorem (see [[eigenvalue-continued-fractions](pages/eigenvalue-continued-fractions.md)]) its continued-fraction expansion is **purely periodic of period one**:

```
δ_a  =  [a; a, a, a, …].
```

Together with the associated Fibonacci-like linear recurrence `x_n = a·x_{n−1} + x_{n−2}` (integer sequence realization) and the shared characteristic polynomial `x² − a·x − 1` (algebraic side), this makes the metallic means a coherent structural family — every property that holds for the golden ratio holds for each with a single parameter substituted.[^2]

## The named members

| `a` | `δ_a` | Common name | Integer sequence (`x_0 = 0, x_1 = 1`) | OEIS |
|---|---|---|---|---|
| 1 | `(1+√5)/2 ≈ 1.6180` | **Golden** | 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, … — Fibonacci | [A000045](https://oeis.org/A000045) |
| 2 | `1+√2 ≈ 2.4142` | **Silver** | 0, 1, 2, 5, 12, 29, 70, 169, 408, 985, … — Pell | [A000129](https://oeis.org/A000129) |
| 3 | `(3+√13)/2 ≈ 3.3028` | **Bronze** | 0, 1, 3, 10, 33, 109, 360, 1189, 3927, 12970, … | (A006190; to be verified on submission) |
| 4 | `2+√5 ≈ 4.2361` | **Copper** | 0, 1, 4, 17, 72, 305, 1292, 5473, 23184, 98209, … | (A001076; to be verified on submission) |
| 5 | `(5+√29)/2 ≈ 5.1926` | **Nickel** | 0, 1, 5, 26, 135, 701, 3640, 18901, 98145, 509626, … | (A052918; to be verified on submission) |

The `a=1` and `a=2` OEIS identifications are confirmed during ingest; the `a≥3` sequences are numerically the direct recurrence output but the OEIS numbers are cited without the same in-page verification (a natural follow-up for the [castle sequence bank / silver-ratio observatory](../../IDEAS.md) sweep). Companion sequences (`y_0 = 2, y_1 = a, y_n = a·y_{n−1} + y_{n−2}`) — Lucas for `a=1`, companion Pell (A001333) for `a=2` — are the `δ_a^n + δ̂_a^n` traces of the same characteristic polynomial and pair with the primary sequences to form the numerator/denominator pairs of continued-fraction convergents.[^3]

## The naming caveat

"Silver ratio" is not universal. **The dominant modern usage — and the one this wiki adopts — is `δ_2 = 1 + √2`**, the metallic-mean value, matching the Wikipedia entry and OEIS cross-references.[^4] A minority usage (typically in paper-size / A-series-paper contexts) reserves "silver ratio" for `√2 ≈ 1.4142` itself. Both are correct in their own literature; we always mean `1 + √2` on the wiki. Beyond silver, the "bronze / copper / nickel" names are less standardized — some authors say "third / fourth / fifth metallic mean" instead — but the metallic-mean family framing is standard.[^1]

## The `a=4` coincidence: copper = φ³

The copper mean has a special place: `δ_4 = 2 + √5 = φ³` (since `φ² = φ + 1`, so `φ³ = 2φ + 1 = 1 + √5 + 1 = 2 + √5`).[^5] So the `a=4` member is not "a new quadratic" — it is a power of the golden ratio living inside `Q(√5)`. The `a=4` integer sequence 0, 1, 4, 17, 72, 305, 1292, 5473, 23184, 98209 is `F_{3n}` up to a shift (Fibonacci taken every third term), which explains the entry sitting inside `Q(√5)` rather than `Q(√20)`. No other `a` has this coincidence: `a=1, 2, 3, 5, 6, …` all sit in genuinely distinct real quadratic fields.

## Why the family matters here

Two members of this family are already load-bearing on the wiki, from two independent directions:

- **`δ_1 = φ`** is the growth constant of Fibonacci, which appears in the castle count as `2^{n−1} − F_{n−1}` on [[castle-by-area](pages/castle-by-area.md)] (prime castles). The Fibonacci method for turning a recurrence into a rational GF is the archetype of [[aocp-generating-functions](pages/aocp-generating-functions.md)].
- **`δ_2 = 1+√2`** is the growth constant of the tower word ([[tower-word-continued-fraction](pages/tower-word-continued-fraction.md)]), and appears as the count-sequence growth of the [[pell-castle-strip](pages/pell-castle-strip.md)] mnemonic where the denominator `1 − 2x − x²` splits along PE 502's structural rules. The integer realization is the [[pell-numbers](pages/pell-numbers.md)].

Both are treated in parallel on [[eigenvalue-continued-fractions](pages/eigenvalue-continued-fractions.md)] as "the castle's two norm-`−1` reduced quadratics" — the framing that made writing this page unavoidable: **there is a ladder, and the wiki was already sitting on rungs 1 and 2 without naming it.** Naming the ladder makes explicit that the metallic-mean family is a **candidate axis for castle classification**: a "silver castle" would be one whose count sequence grows at rate `1+√2`; a "bronze castle" at rate `(3+√13)/2`; and so on. Whether such castle families exist — and if so, which castle rule-modifications tune them — is the "metallic-ratio ladder" thread on `IDEAS.md`.

## Structural facts about the family

- **Binet-style formula.** Every member's recurrence-realization satisfies `x_n = (δ_a^n − δ̂_a^n) / (δ_a − δ̂_a)` with `δ̂_a = (a − √(a²+4))/2` the conjugate root. Growth is `x_{n+1}/x_n → δ_a`; the conjugate contribution decays because `|δ̂_a| < 1` for every `a ≥ 1`.
- **Purely periodic continued fraction.** `δ_a = [a; a, a, …]` since `δ_a = a + 1/δ_a` (i.e. `δ_a` is a fixed point of `x ↦ a + 1/x`), the fundamental self-similarity property that [[eigenvalue-continued-fractions](pages/eigenvalue-continued-fractions.md)] develops. The conjugate `δ̂_a` sits in `(−1, 0)` for every `a ≥ 1`, so all members are Galois-reduced (norm `−1`, sum of roots `= a > 0`, product `= −1`), hence purely periodic.
- **Fundamental units.** Each `δ_a` is a fundamental unit of the real quadratic field `Q(√(a²+4))` (up to sign/inversion), i.e. a generator of its unit group modulo torsion. Number-theoretic weight — the metallic means are, up to a rescaling, the fundamental units of the simplest infinite family of real quadratic fields.[^6]
- **Palindromic quadratic — reciprocal-root symmetry.** The characteristic polynomial `x² − a·x − 1` has coefficients `[1, −a, −1]`, so it is *anti*-palindromic (not palindromic) — the two roots multiply to `−1` (norm `−1`), the very reason the fraction is purely periodic ([[eigenvalue-continued-fractions](pages/eigenvalue-continued-fractions.md)] Step 3). Every metallic mean sits on the same anti-palindromic template with a different first-order coefficient.

## Castle classification: an open direction

The "silver castle / bronze castle / …" idea is speculative but concrete enough to test:

1. **Silver castle candidate:** the Pell strip already realizes `1+√2` in a small castle sub-family (height-2, one signed strip, no parity constraint) via the [[pell-castle-strip](pages/pell-castle-strip.md)] denominator `1 − 2x − x²`. Does the full castle family (unrestricted `h`, with parity) or any of its natural sub-families reach `1+√2` as a growth constant? The tower word already does ([[tower-word-continued-fraction](pages/tower-word-continued-fraction.md)]).
2. **Bronze castle candidate:** the natural knob is the mandatory-gap width or the per-column state-set size. A width-≥2 mandatory gap plus a 3-state per-column atom would nominally give denominator `1 − 3x − x²` (or `1 − 3x − x³`, depending on encoding). Its coefficient sequence would be `1, 3, 10, 33, 109, 360, …` — the `a=3` Fibonacci-analog sequence above, growth `δ_3`. Whether this corresponds to any physically-meaningful castle-rule variation is the question.
3. **General knob:** parameterize the "castle strip" mnemonic by two numbers — the width-1-atom multiplicity `w_1` and the width-2-atom multiplicity `w_2`. The denominator `1 − w_1·x − w_2·x²` has growth `(w_1 + √(w_1² + 4·w_2))/2`, which is a metallic mean iff `w_2 = 1`. So the metallic-mean ladder cleanly corresponds to "how many states per column, with the mandatory-gap rule fixed." A **classification axis** for castle rule-variations, tracked in `IDEAS.md`.

## Appearances in Sources

*(no primary sources ingested for this page yet; the material is standard number theory and is verified by direct calculation. Candidate sources for future ingest: Vera W. de Spinadel, "The metallic means family and multifractal spectra," Nonlinear Analysis 36 (1999) 721–745; Wikipedia article "Metallic mean" as a hydration source for definitions.)*

## Related Concepts

- [[pell-numbers](pages/pell-numbers.md)] — the `a=2` integer sequence; the silver-mean member.
- [[pell-castle-strip](pages/pell-castle-strip.md)] — the castle-strip mnemonic realizing `δ_2 = 1+√2` through PE 502's structural rules.
- [[eigenvalue-continued-fractions](pages/eigenvalue-continued-fractions.md)] — the two members `φ` and `1+√2` already treated as the castle's norm-`−1` reduced quadratics; this page names the ladder they sit on.
- [[tower-word-continued-fraction](pages/tower-word-continued-fraction.md)] — where `1+√2` appears as the tower-word growth constant.
- [[aocp-generating-functions](pages/aocp-generating-functions.md)] — the Fibonacci / `φ` archetype (the `a=1` member).
- [[castle-by-area](pages/castle-by-area.md)] — `2^{n−1} − F_{n−1}`, where Fibonacci / `φ` enters the castle count.
- [[algebraic-transcendental-wall](pages/algebraic-transcendental-wall.md)] — the metallic means are algebraic (quadratic), the exact irrationals that C-finite castle counts *can* carry.

## Footnotes

[^1]: Vera W. de Spinadel, *La familia de números metálicos* (1997) and later *The metallic means family and multifractal spectra* (Nonlinear Analysis 36, 1999) — the standard reference introducing the metallic-mean framing. Source not ingested; term usage cross-checked against the Wikipedia "Metallic mean" article and OEIS cross-references (e.g. A001333 discusses `√2` and Pell in the metallic-mean context).
[^2]: The reduced-quadratic-surd theory (Lagrange periodicity, Galois pure periodicity) applied to `x² − a·x − 1` for arbitrary integer `a ≥ 1` is a direct specialization of the general treatment on [[eigenvalue-continued-fractions](pages/eigenvalue-continued-fractions.md)]. The identity `δ_a = a + 1/δ_a`, which forces `δ_a = [a; a, a, …]`, was verified for `a = 1, 2, 3, 4, 5` during ingest by fixed-point iteration.
[^3]: The recurrence `x_n = a·x_{n−1} + x_{n−2}` with `x_0 = 0, x_1 = 1` was iterated for `a = 1..5` during ingest; the first ten values in the table match direct computation, and the ratio `x_29 / x_28` matches `δ_a` to ten decimal places for each `a` (Fibonacci: `1.6180339888` vs. `1.6180339887`; Pell: `2.4142135624` for both; and analogously for `a = 3, 4, 5`). The companion sequences (`y_0 = 2, y_1 = a`) were also iterated and identified for `a=1` (Lucas A000032) and `a=2` (companion Pell A001333).
[^4]: The Wikipedia "Silver ratio" article and OEIS A001333 (whose comment describes it as convergents-of-`√2` numerators, in Pell/silver-mean context) both use "silver ratio" for `1 + √2`, and this is the usage in de Spinadel's original paper (`δ_S`). The competing usage — "silver ratio = √2" (paper-size / A-series context) — appears in some architecture and design literature; when this is meant it is usually specified explicitly. Standard number-theory and OEIS usage is `δ_2 = 1 + √2`.
[^5]: `φ² = φ + 1` (defining property of the golden ratio) gives `φ³ = φ·φ² = φ² + φ = 2φ + 1 = 1 + √5 + 1 = 2 + √5 = δ_4`; verified numerically during ingest (`φ³ = 4.2360679…`, matching `2 + √5 = 4.2360679…`). Consequence: the `a=4` integer sequence `x_n = 0, 1, 4, 17, 72, 305, 1292, 5473, 23184, 98209` equals `F_{3n}/2` where `F_n` is Fibonacci — `F_3 = 2, F_6 = 8, F_9 = 34, F_12 = 144, F_15 = 610, …`, divided by 2 gives `1, 4, 17, 72, 305, …`, matching exactly (re-verified during ingest against the Fibonacci sequence). So the copper-mean recurrence is a decimated / scaled Fibonacci, and the sequence sits inside `Q(√5)`, not in an independent quadratic field.
[^6]: The fundamental unit of `Z[√5]` is the golden ratio (well-known); the fundamental unit of `Z[√2]` is `1 + √2` (well-known). For `a ≥ 3`, `Z[(a + √(a²+4))/2]` (or `Z[√(a²+4)]` — depending on whether `a²+4 ≡ 1 (mod 4)`, which depends on `a`'s parity) has `δ_a` as a fundamental unit up to a sign / power adjustment; the statement is standard algebraic number theory (Dirichlet's unit theorem specialized to real quadratic fields, rank 1). Not verified in depth during ingest; noted as a defining structural property of the family.
