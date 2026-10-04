---
title: Continued fractions of the tower word
category: Concepts
summary: The tower word is a peakless-valleyless Motzkin path — OEIS A004149 by length, growth √2+1 — read against Flajolet's combinatorial continued fractions; graded by width at bounded height its recursion 1/E_k = 1/E_{k−1} − x telescopes to 1/(1−(k+1)x), where the Motzkin J-fraction nests.
tags: [concept, castle, tower-word, continued-fraction, flajolet, motzkin, algebraic, oeis, generating-functions]
sources: [project-euler-502-representations]
created: 2026-09-14
updated: 2026-10-04
---

# Continued fractions of the tower word

## The tower word is a peakless-valleyless Motzkin path

The **tower word** ([[tower-word-language](pages/tower-word-language.md)], [[generalized-dyck-grammar](pages/generalized-dyck-grammar.md)]) is the skyline of a tower read as a word over `{U, R, D}` with `U = +1`, `R = 0`, `D = −1`: a **Motzkin path** that stays `≥ 0` and returns to `0`, carrying one extra **run constraint** — no `UD`, no `DU`.[^1] In path language those two forbidden factors are exactly a **peak** (`UD`) and a **valley** (`DU`), so a tower word is a **peakless-valleyless Motzkin path**: vertical steps come in maximal runs, and any two vertical runs of opposite direction are separated by at least one flat (`R`).[^1]

## Flajolet: continued fractions count Motzkin paths

The framework is Flajolet's *Combinatorial aspects of continued fractions*: the universal **Stieltjes–Jacobi continued fraction** is the generating function of **labelled paths in the plane** — height-weighted Motzkin paths — and the paper derives continued-fraction expansions for the Catalan, Bell/Stirling, tangent/secant, and Euler/Eulerian numbers from this one correspondence.[^2] Dyck paths (no flats) give **S-fractions**, general Motzkin paths give **J-fractions**. Two classical examples, both re-derived here:[^3]

- **Catalan S-fraction.** `C(z) = 1/(1 − z/(1 − z/(1 − z/(…)))) = (1 − √(1−4z))/(2z)` counts Dyck paths; the coefficients are the Catalan numbers `1, 1, 2, 5, 14, 42, 132, …`.[^3]
- **Motzkin J-fraction.** `M(z) = 1/(1 − z − z²/(1 − z − z²/(1 − …))) = (1 − z − √(1−2z−3z²))/(2z²)` counts plain Motzkin paths; coefficients `1, 1, 2, 4, 9, 21, 51, 127, …`.[^3]

The simplest continued fraction of a number, `1 + 1/(1 + 1/(1 + …))`, is the **golden ratio** `φ = (1+√5)/2`: its convergents are the Fibonacci ratios `F_{n+1}/F_n = 2, 3/2, 5/3, 8/5, 13/8, …`.[^3] Fibonacci's Binet form `F_n = (φ^n − φ̂^n)/√5` is on [[aocp-generating-functions](pages/aocp-generating-functions.md)], and Fibonacci appears in prime-castle counting as `2^{n−1} − F_{n−1}` (see [[castle-by-area](pages/castle-by-area.md)]).

## The tower word by steps is A004149

Mark each step `U, R, D` by `z` (total length), so a tower word of width `L` and `b` blocks is worth `z^{L + 2b}`. Each length then has finitely many tower words, and the count is **Online Encyclopedia of Integer Sequences (OEIS) A004149**, "generalized Catalan numbers", whose entry states the object verbatim: *"Number of Motzkin paths of length n−1 (n≥1) with no peaks and no valleys, i.e., no UD's and no DU's, where U=(1,1) and D=(1,−1)."* (Emeric Deutsch, 2004).[^4] So **tower words of length `n` number A004149(`n+1`)**: `1, 1, 1, 2, 4, 8, 16, 33, 69, 146, 312, 673, 1463, 3202, 7050, …`, recomputed here two independent ways (direct enumeration and iterating the grammar) with the same result.[^4]

The generating function is **algebraic, not rational** — the bounded-height language is regular, but the unbounded-height tower word is context-free (see [[tower-word-language](pages/tower-word-language.md)]). The Pell numbers (`P⋆_n = 2P⋆_{n−1} + P⋆_{n−2}`, OEIS A000129, [[pell-numbers](pages/pell-numbers.md)]) also grow like `(1 + √2)^n`, the silver-ratio counterpart of Fibonacci/`φ`, and a castle strip counted by them is on [[pell-castle-strip](pages/pell-castle-strip.md)]. Reading the tower grammar with each step marked by `z` gives the fixed-point equation

```
E(z) = (1 + z²(E − 1)) / (1 − z − z³(E − 1))   ⟹   z³E² − (1 − z − z² + z³)E + (1 − z²) = 0,
```

a quadratic with discriminant `(z−1)(z+1)(z²+1)(z²+2z−1)`.[^5] The singularity nearest the origin is `z* = √2 − 1`, so the tower-word counts grow like `(√2 + 1)^n ≈ 2.4142^n`.[^5] The growth constant `√2 + 1 = [2; 2, 2, …]` is a quadratic unit with a purely periodic continued fraction ([[eigenvalue-continued-fractions](pages/eigenvalue-continued-fractions.md)]).

A004149's references include **Barry**, *Generalized Catalan recurrences, Riordan arrays, elliptic curves, and orthogonal polynomials* (orthogonal polynomials correspond to J-fractions), and **Asinowski–Banderier–Roitner**, *Generating functions for lattice paths with several forbidden patterns* ("no UD, no DU" is a forbidden-pattern condition).[^6]

## Width grading and the J-fraction

The tower word is a Motzkin path with the no-`UD`/no-`DU` run constraint added. **Drop the constraint** and the tower grammar becomes the plain Motzkin first-return grammar — the interior `V` may be empty (admitting the `UD` peak) and the tail may restart immediately (admitting the `DU` valley) — so the unconstrained tower word is a Motzkin path, counted by the J-fraction above.[^1]

With **bounded height `k`** the tower word is a regular language, and its width generating function is rational: the grammar reads off the recurrence `E_k = E_{k−1}/(1 − x·E_{k−1})`, which collapses to `E_k = 1/(1 − (k+1)x)`, i.e. `T(k,L) = (k+1)^L` ([[castle-counting-formula](pages/castle-counting-formula.md)]).[^7] In reciprocal form the recurrence is `1/E_k = 1/E_{k−1} − x`, which telescopes from `1/E_0 = 1 − x` to `1/E_k = 1 − (k+1)x`: each level of height subtracts one `x`. Counting by width in this way needs the run constraint, since without it `UD` pairs could be inserted freely and the words with `L` flats would be infinite in number. The Motzkin J-fraction, graded by length, nests instead: `M_k = 1/(1 − z − z²·M_{k−1})`. Both are rational at bounded height and algebraic without a height bound.

## Open

A J-fraction for A004149 with explicit coefficients is not worked out here; A004149 lists Barry's paper on Riordan arrays and orthogonal polynomials, the side such an expansion would come from. Area-graded continued fractions for castles are on [[prellberg-brak-1995-cluster-models](pages/prellberg-brak-1995-cluster-models.md)] (eq. 3.12) and [[deutsch-elizalde-2016-bargraphs-cornerless-motzkin](pages/deutsch-elizalde-2016-bargraphs-cornerless-motzkin.md)] (§3.14).

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
- [[deutsch-elizalde-2016-bargraphs-cornerless-motzkin](pages/deutsch-elizalde-2016-bargraphs-cornerless-motzkin.md)] - peakless-valleyless Motzkin paths are its "cornerless" paths, in bijection with bargraphs (castles); its §3.14 area continued fraction is a second area-graded expansion.
- [[prodinger-2025-cornerless-motzkin-bargraphs](pages/prodinger-2025-cornerless-motzkin-bargraphs.md)] - the kernel-method GF of Motzkin paths by length with peaks and valleys weighted; at both weights 0 its returning series is A004149, the tower word by length, and its prefixes (any final height) are A308435.
- [[prellberg-brak-1995-cluster-models](pages/prellberg-brak-1995-cluster-models.md)] — an area-graded continued fraction for castles. Their bar-graph equation (3.11) is the castle GF by width, blocks and area, and iterating it gives a continued fraction in the q-shifted width variable (eq. 3.12).[^8]
- [[generating-function-gallery](pages/generating-function-gallery.md)] / [[closed-form-hunting](pages/closed-form-hunting.md)] — the rational GFs and characteristic polynomials of `P(k,L)`; their roots' continued fractions are on [[eigenvalue-continued-fractions](pages/eigenvalue-continued-fractions.md)].
- [[pell-numbers](pages/pell-numbers.md)] / [[pell-castle-strip](pages/pell-castle-strip.md)] — the integer-sequence and castle-strip realizations of the growth constant `1 + √2`.
- [[metallic-means](pages/metallic-means.md)] — `1 + √2` is the silver rung of this family.
- [[aocp-combinatorics](pages/aocp-combinatorics.md)] — the inversion statistic and the q-factorial.
- [[castle-compression](pages/castle-compression.md)] — bounded height makes the language regular and the GF rational: the "rule-generated" tier of the compressibility axis.

## Footnotes

[^1]: [[project-euler-502-representations](pages/project-euler-502-representations.md)] §"The tower word" L221-230 — "A tower above a length-L block uses exactly L R's, never drops below the base, and returns to it," and "no UD ... and no DU."

[^2]: Philippe Flajolet, *Combinatorial aspects of continued fractions*, Discrete Mathematics 32 (1980) 125–161; doi:10.1016/0012-365X(80)90050-3. The Stieltjes–Jacobi continued fraction as the characteristic series of labelled (Motzkin) paths, with continued-fraction expansions for Catalan, Bell/Stirling, tangent/secant, and Euler/Eulerian numbers. (Cited bibliographically; the paper is not read here.)

[^3]: Catalan S-fraction `1/(1 − z/(1 − z/(…)))` and Motzkin J-fraction `1/(1 − z − z²/(1 − z − …))` re-derived with SymPy and matched to the Catalan (`1,1,2,5,14,42,132,429`) and Motzkin (`1,1,2,4,9,21,51,127,323,835`) sequences; golden-ratio convergents `2, 3/2, 5/3, 8/5, 13/8, 21/13, 34/21, 55/34` → `(1+√5)/2`.

[^4]: OEIS A004149, comment by Emeric Deutsch (Jan 08 2004): "Number of Motzkin paths of length n-1 (n>=1) with no peaks and no valleys, i.e., no UD's and no DU's, where U=(1,1) and D=(1,-1)." The tower-word count by total steps, recomputed by direct enumeration and by iterating `E_k`, gives `1,1,1,2,4,8,16,33,69,146,312,673,1463,3202,7050,15605` for lengths `0..15` = A004149(`L+1`).

[^5]: The fixed point `E = (1 + z²(E−1))/(1 − z − z³(E−1))` simplifies to `z³E² − (1−z−z²+z³)E + (1−z²) = 0`, discriminant `(z−1)(z+1)(z²+1)(z²+2z−1)`, singularity `√2−1`, growth constant `1/(√2−1) = √2+1` — verified with SymPy.

[^6]: Paul Barry, *Generalized Catalan recurrences, Riordan arrays, elliptic curves, and orthogonal polynomials*, arXiv:1910.00875 (2019); Andrei Asinowski, Cyril Banderier, Valerie Roitner, *Generating functions for lattice paths with several forbidden patterns* (2019) — both listed as references on OEIS A004149.

[^7]: [[project-euler-502-representations](pages/project-euler-502-representations.md)] §"Unsigned count" L297-309 — "E_k = 1/(1-(k+1)x)" and "T(k,L) = (k+1)^L".

[^8]: [[prellberg-brak-1995-cluster-models](pages/prellberg-brak-1995-cluster-models.md)] `prellberg-brak-1995-partially-directed-cluster-models.txt` §3.1 L473-479 - "This equation can be solved for B(x, y, q) and leads to a continued-fraction representation of the generating function, given by iteration of" eq. (3.12).
