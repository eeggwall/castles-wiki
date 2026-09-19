---
title: Continued fractions of the tower word
category: Concepts
summary: The tower word is a peakless-valleyless Motzkin path — OEIS A004149 — and Flajolet's combinatorial continued fractions are its natural generating-function home; the no-UD/no-DU run constraint is exactly what collapses the bounded-height continued fraction to the rational 1/(1−(k+1)x).
tags: [concept, castle, tower-word, continued-fraction, flajolet, motzkin, algebraic, oeis, generating-functions]
sources: [project-euler-502-representations]
created: 2026-09-14
updated: 2026-09-19
---

# Continued fractions of the tower word

## The tower word is a peakless-valleyless Motzkin path

The **tower word** ([[tower-word-language](pages/tower-word-language.md)], [[generalized-dyck-grammar](pages/generalized-dyck-grammar.md)]) is the skyline of a tower read as a word over `{U, R, D}` with `U = +1`, `R = 0`, `D = −1`: a **Motzkin path** that stays `≥ 0` and returns to `0`, carrying one extra **run constraint** — no `UD`, no `DU`.[^1] In path language those two forbidden factors are exactly a **peak** (`UD`) and a **valley** (`DU`), so a tower word is a **peakless-valleyless Motzkin path**: vertical steps come in maximal runs, and any two vertical runs of opposite direction are separated by at least one flat (`R`).[^1] This is the "Motzkin plus a run constraint" reading, not a new family.[^1]

## Flajolet: continued fractions count Motzkin paths

The framework is Flajolet's *Combinatorial aspects of continued fractions*: the universal **Stieltjes–Jacobi continued fraction** is the generating function of **labelled paths in the plane** — height-weighted Motzkin paths — and the paper derives continued-fraction expansions for the Catalan, Bell/Stirling, tangent/secant, and Euler/Eulerian numbers from this one correspondence.[^2] Dyck paths (no flats) give **S-fractions**, general Motzkin paths give **J-fractions**. Two classical anchors, both re-derived during ingest:[^3]

- **Catalan S-fraction.** `C(z) = 1/(1 − z/(1 − z/(1 − z/(…)))) = (1 − √(1−4z))/(2z)` counts Dyck paths; the coefficients are the Catalan numbers `1, 1, 2, 5, 14, 42, 132, …`.[^3]
- **Motzkin J-fraction.** `M(z) = 1/(1 − z − z²/(1 − z − z²/(1 − …))) = (1 − z − √(1−2z−3z²))/(2z²)` counts plain Motzkin paths; coefficients `1, 1, 2, 4, 9, 21, 51, 127, …`.[^3]

The continued fraction the castle thread was drawn toward, `1 + 1/(1 + 1/(1 + …))`, is the **golden ratio** `φ = (1+√5)/2`: its convergents are the Fibonacci ratios `F_{n+1}/F_n = 2, 3/2, 5/3, 8/5, 13/8, …`.[^3] Fibonacci is already the castle's bedrock example — `F_n = (φ^n − φ̂^n)/√5` on [[aocp-generating-functions](pages/aocp-generating-functions.md)] — and appears in prime-castle counting as `2^{n−1} − F_{n−1}` (see [[castle-by-area](pages/castle-by-area.md)]).

## The tower word by steps is A004149

Mark each step `U, R, D` by `z` (total length), so a tower word of width `L` and `b` blocks is worth `z^{L + 2b}`. Each length then has finitely many tower words, and the count is **Online Encyclopedia of Integer Sequences (OEIS) A004149**, "generalized Catalan numbers", whose entry states the object verbatim: *"Number of Motzkin paths of length n−1 (n≥1) with no peaks and no valleys, i.e., no UD's and no DU's, where U=(1,1) and D=(1,−1)."* (Emeric Deutsch, 2004).[^4] So **tower words of length `L` = A004149(`L+1`)**: `1, 1, 1, 2, 4, 8, 16, 33, 69, 146, 312, 673, 1463, 3202, 7050, …`, recomputed here two independent ways (direct enumeration and iterating the grammar) with the same result.[^4]

The generating function is **algebraic, not rational** — the bounded-height language is regular, but the unbounded-height tower word is context-free (see [[tower-word-language](pages/tower-word-language.md)]). The **integer sequence realization** of the growth constant `1 + √2` is the [[pell-numbers](pages/pell-numbers.md)] (`P_n = 2P_{n−1} + P_{n−2}`, OEIS A000129) — the Pell/silver-ratio counterpart of Fibonacci/`φ`; a physical castle-strip mnemonic that produces Pell directly is on [[pell-castle-strip](pages/pell-castle-strip.md)]. Reading the tower grammar with each step marked by `z` gives the fixed-point equation

```
E(z) = (1 + z²(E − 1)) / (1 − z − z³(E − 1))   ⟹   z³E² − (1 − z − z² + z³)E + (1 − z²) = 0,
```

a quadratic with discriminant `(z−1)(z+1)(z²+1)(z²+2z−1)`.[^5] The singularity nearest the origin is `z* = √2 − 1`, so the tower-word counts grow like `(√2 + 1)^n ≈ 2.4142^n` — a `Q(√2)` fingerprint that rhymes with the signed count `P(1,L) = Re((1+i)^{L+1})`, whose magnitude is `|1+i|^L = (√2)^L` ([[signed-tower-count](pages/signed-tower-count.md)]).[^5] Both are quadratic: each root is a quadratic irrational, so each has an eventually-periodic continued fraction by Lagrange's theorem.

A004149's own references point straight back at continued fractions: **Barry**, *Generalized Catalan recurrences, Riordan arrays, elliptic curves, and orthogonal polynomials* (orthogonal polynomials ↔ J-fractions is exactly the continued-fraction correspondence), and **Asinowski–Banderier–Roitner**, *Generating functions for lattice paths with several forbidden patterns* ("no UD, no DU" is a forbidden-pattern condition).[^6]

## The run constraint collapses the continued fraction

The tower word is a Motzkin path with the no-`UD`/no-`DU` run constraint added. **Drop the constraint** and the tower grammar becomes the plain Motzkin first-return grammar — the interior `V` may be empty (admitting the `UD` peak) and the tail may restart immediately (admitting the `DU` valley) — so the unconstrained tower word *is* a Motzkin path, counted by the J-fraction above.[^1] The constraint is the whole difference.

With **bounded height `k`** the tower word is a regular language, and its width generating function is rational: the grammar reads off the recurrence `E_k = E_{k−1}/(1 − x·E_{k−1})`, which collapses to `E_k = 1/(1 − (k+1)x)`, i.e. `T(k,L) = (k+1)^L` ([[castle-counting-formula](pages/castle-counting-formula.md)]).[^7] That recurrence is the *collapsed remainder* of a continued fraction: the Motzkin J-fraction iterates `M_k = 1/(1 − z − z²·M_{k−1})` with a genuine nested `z²` (an up-and-down excursion) and a linear `z` (a flat), whereas the tower word's run constraint removes the nested `z²·M_{k−1}` term and leaves a pure geometric collapse. This is the structural reason the tower count `(k+1)^L` is so much simpler than the Motzkin count `M_n`: the no-`UD`/no-`DU` constraint demotes the tower word from the algebraic (infinite-continued-fraction) side to the rational side.

## A thread to follow

The open end is the tower word's *own* continued fraction. A004149 is a generalized-Catalan, Riordan-array sequence, so its continued fraction should come from the orthogonal-polynomial / Stieltjes-moment side (Barry's paper), not from the plain Motzkin J-fraction — a genuinely different Jacobi-type expansion than either `C(z)` or `M(z)`. The two natural sources to ingest next are **Flajolet 1980** (to turn this page's bibliographic citations into line-quoted footnotes) and **Barry's arXiv:1910.00875** (for the A004149 Riordan/orthogonal-polynomial connection). The area-graded version — the tower word refined by block count — is the q-analog, landing on q-S/J-continued fractions, the direction [[steep-polyominoes-q-motzkin-bessel](pages/steep-polyominoes-q-motzkin-bessel.md)] already gestures at with its q-Bessel ratio.

## Appearances in Sources

- [[tower-word-language](pages/tower-word-language.md)] / [[generalized-dyck-grammar](pages/generalized-dyck-grammar.md)] — the tower word as a Motzkin path with the no-`UD`/no-`DU` run constraint.
- [[castle-counting-formula](pages/castle-counting-formula.md)] — `E_k = 1/(1−(k+1)x)`, `T(k,L) = (k+1)^L`, and the `P_k` signed recurrence.
- [[signed-tower-count](pages/signed-tower-count.md)] — the quadratic `P(1,L) = Re((1+i)^{L+1})` and its `1±i` roots.

## Related Concepts

- [[motzkin-numbers](pages/motzkin-numbers.md)] — the `M_n` family the J-fraction counts; the tower word's unconstrained parent.
- [[dyck-words](pages/dyck-words.md)] / [[catalan-numbers](pages/catalan-numbers.md)] — the two-letter root and the S-fraction `C(z)`.
- [[aocp-generating-functions](pages/aocp-generating-functions.md)] — the Fibonacci/`φ` method, the golden ratio's algebraic home.
- [[castle-by-area](pages/castle-by-area.md)] — the area grading whose q-analog is the q-continued-fraction thread.
- [[steep-polyominoes-q-motzkin-bessel](pages/steep-polyominoes-q-motzkin-bessel.md)] — q-Motzkin and the q-Bessel ratio, the q-side of this correspondence.
- [[generating-function-gallery](pages/generating-function-gallery.md)] / [[closed-form-hunting](pages/closed-form-hunting.md)] — the rational GFs and characteristic polynomials whose (palindromic) roots are the periodic-continued-fraction side of the same story.
- [[pell-numbers](pages/pell-numbers.md)] / [[pell-castle-strip](pages/pell-castle-strip.md)] — the integer-sequence and castle-strip realizations of the growth constant `1 + √2`.
- [[aocp-combinatorics](pages/aocp-combinatorics.md)] — the inversion statistic and q-factorial, the classical statistic Flajolet's continued fractions carry as q-weights on Motzkin paths.
- [[castle-compression](pages/castle-compression.md)] — bounded height collapses the continued fraction to a rational GF, i.e. a regular language: the "rule-generated" tier of the compressibility axis.

## Footnotes

[^1]: [[project-euler-502-representations](pages/project-euler-502-representations.md)] §"The tower word" L221-230 — "A tower above a length-L block uses exactly L R's, never drops below the base, and returns to it," and "no UD ... and no DU."

[^2]: Philippe Flajolet, *Combinatorial aspects of continued fractions*, Discrete Mathematics 32 (1980) 125–161; doi:10.1016/0012-365X(80)90050-3. The Stieltjes–Jacobi continued fraction as the characteristic series of labelled (Motzkin) paths, with continued-fraction expansions for Catalan, Bell/Stirling, tangent/secant, and Euler/Eulerian numbers. (Source not yet ingested; cited bibliographically.)

[^3]: Catalan S-fraction `1/(1 − z/(1 − z/(…)))` and Motzkin J-fraction `1/(1 − z − z²/(1 − z − …))` re-derived with SymPy and matched to the Catalan (`1,1,2,5,14,42,132,429`) and Motzkin (`1,1,2,4,9,21,51,127,323,835`) sequences; golden-ratio convergents `2, 3/2, 5/3, 8/5, 13/8, 21/13, 34/21, 55/34` → `(1+√5)/2`.

[^4]: OEIS A004149, comment by Emeric Deutsch (Jan 08 2004): "Number of Motzkin paths of length n-1 (n>=1) with no peaks and no valleys, i.e., no UD's and no DU's, where U=(1,1) and D=(1,-1)." The tower-word count by total steps, recomputed by direct enumeration and by iterating `E_k`, gives `1,1,1,2,4,8,16,33,69,146,312,673,1463,3202,7050,15605` for lengths `0..15` = A004149(`L+1`).

[^5]: The fixed point `E = (1 + z²(E−1))/(1 − z − z³(E−1))` simplifies to `z³E² − (1−z−z²+z³)E + (1−z²) = 0`, discriminant `(z−1)(z+1)(z²+1)(z²+2z−1)`, singularity `√2−1`, growth constant `1/(√2−1) = √2+1` — verified with SymPy.

[^6]: Paul Barry, *Generalized Catalan recurrences, Riordan arrays, elliptic curves, and orthogonal polynomials*, arXiv:1910.00875 (2019); Andrei Asinowski, Cyril Banderier, Valerie Roitner, *Generating functions for lattice paths with several forbidden patterns* (2019) — both listed as references on OEIS A004149.

[^7]: [[project-euler-502-representations](pages/project-euler-502-representations.md)] §"Unsigned count" L297-309 — "E_k = 1/(1-(k+1)x)" and "T(k,L) = (k+1)^L".
