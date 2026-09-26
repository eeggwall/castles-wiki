---
title: "Algebraic Numbers and Fourier Analysis (Salem 1963)"
category: Sources
summary: Raphael Salem's 1960 Brandeis lectures, the founding monograph on the Pisot numbers (his class S) and the Salem numbers (his class T), and their use in harmonic analysis. Chapter I defines class S, proves θ^n → 0 mod 1 through the integer trace, shows every real number field contains Pisot numbers, and proves the two converses (Σ‖λθ^n‖² < ∞, or θ algebraic with ‖λθ^n‖ → 0, forces θ into S) with the rational-series toolkit of Fatou's lemma and Kronecker's Hankel-determinant test.
tags: [book, source, pisot-number, salem-number, algebraic-integer, diophantine-approximation, uniform-distribution, rational-generating-function, hankel-determinant, fatou-lemma, fourier-analysis]
sources: [salem-1963-algebraic-numbers-fourier-analysis]
created: 2026-09-25
updated: 2026-09-25
---

# Algebraic Numbers and Fourier Analysis (Salem 1963)

**Source:** `raw/salem-1963-algebraic-numbers-fourier-analysis.txt`, the OCR text layer (`pdftotext`) of Raphael Salem, *Algebraic Numbers and Fourier Analysis*, Heath Mathematical Monographs, D. C. Heath and Company, Boston, 1963 (vii + 68 pp.). The local scan is `assets/salem-1963-algebraic-numbers-fourier-analysis.pdf` (not tracked). The OCR garbles most symbols (the nearest-integer distance `‖α‖` renders as `11 a 11`, `θ` as `0` or `(J`), so formula-bearing footnotes below are `[synthesis]` paraphrases with line ranges rather than quotes.
**Date ingested:** 2026-09-25
**Type:** book (lecture monograph, 7 chapters + unsolved problems + appendix)

## Summary

The book is the written form of lectures Salem gave at Brandeis University in the fall of 1960. Its subject had until then appeared only in pieces, partly in Zygmund's treatise and partly in original memoirs, and it closes with a list of unsolved problems aimed at research students.[^1] Salem died in Paris on 20 June 1963, a few days after seeing the final proofs.[^2]

The through-line is one special set of algebraic integers. Salem calls them **the class S**: real algebraic integers `θ > 1` whose other conjugates all lie strictly inside the unit circle. Today they are the **Pisot numbers** ([[pisot-number](pages/pisot-number.md)]).[^3] Chapters I-III build the arithmetic of S and of a second class, **T** (the Salem numbers), out of power series with integer coefficients. Chapters IV-VII turn that arithmetic on Fourier analysis: whether the Fourier-Stieltjes transform of a Cantor-type singular measure tends to 0 at infinity, and whether a symmetric perfect set of constant dissection ratio is a set of uniqueness for trigonometric series, both hinge on whether a ratio is in S.[^4]

**Chapter I, "A remarkable set of algebraic integers."** The motivating question is uniform distribution modulo 1. For polynomial and sub-linear growth the answers are known: `nξ` is uniformly distributed for irrational `ξ`, and so is any polynomial with an irrational non-constant coefficient. For exponential growth `ω^n`, Koksma proved uniform distribution for almost every `ω > 1`, yet "almost nothing is known" about any specific `ω`, not even whether `e^n` or `(3/2)^n` is dense mod 1.[^5] Salem turns the question around and studies the `θ` whose powers are as badly distributed as possible. The model is the golden ratio: `φ^n + φ'^n` is an integer and `|φ'| < 1`, so `φ^n` tends to 0 mod 1.[^6] Class S is the general form of that example. Theorem 1 says `‖θ^n‖ → 0` for `θ` in S, as fast as a geometric progression, because `θ^n` plus the conjugates' `n`-th powers is a rational integer. The same holds for `λθ^n` when `λ` is any algebraic integer of the field.[^7] Theorem 2 says every real algebraic field contains elements of S of full degree, by Minkowski's linear-forms theorem.[^8]

The chapter's substance is the converse. Suppose only that `‖λθ^n‖ → 0` for some real `λ ≠ 0`; must `θ` be in S? Salem calls this "important problem" still unsolved, and proves it under either of two extra hypotheses. **Theorem A**: if `Σ ‖λθ^n‖² < ∞`, then `θ` is in S and `λ` lies in `Q(θ)`. **Theorem B**: if `θ` is known to be algebraic, `‖λθ^n‖ → 0` already suffices.[^9] Both proofs show that the nearest integers `a_n` of `λθ^n` have a rational generating function `Σ a_n z^n = P(z)/Q(z)`, with four classical lemmas:

- **Lemma I**: a power series is rational if and only if its coefficients eventually satisfy a fixed linear recurrence.
- **Lemma II (Fatou)**: an integer-coefficient series that is rational is `P/Q` with `P, Q` integer polynomials and `Q(0) = 1`.
- **Lemma III (Kronecker)**: the series is rational if and only if its Hankel determinants `det(c_{i+j})` vanish from some order on.
- **Lemma IV (Hadamard)**: the determinant bound, used to force the Hankel determinants, which are integers, below 1 and hence to 0.[^10]

Once the series is rational, the only pole inside the unit disc is `1/θ` (from `λ/(1 − θz)`), and the square-summable (or merely `o(1)`) error rules out poles on the circle. The reciprocal of the denominator therefore has `θ` as its one root outside the unit circle.[^11] Theorem B skips Kronecker: the minimal equation of `θ`, applied to `λθ^N`, gives an integer combination of the `a_n` that tends to 0 and is therefore eventually exactly 0, a recurrence.[^12]

The chapter ends on the open case. The existence of a *transcendental* `θ` with `‖λθ^n‖ → 0` is open, and the one theorem known is that the set of all such `θ` is countable. Once the errors are small, `a_{n+2}` is determined by `a_n` and `a_{n+1}` (it is the integer nearest `a_{n+1}²/a_n`), so the whole integer sequence, and with it `θ = lim a_{n+1}/a_n`, is fixed by finitely many initial terms.[^13] Two exercises follow. Products of same-degree elements of S in one field stay in S (in particular `θ^q`), and Theorem A's hypothesis weakens to `Σ_{j ≤ n} ‖λθ^j‖² = o(n)`.[^14]

## Key Takeaways

- **Class S = Pisot numbers**: real algebraic integers `θ > 1` with every other conjugate of modulus `< 1`. Rational integers `> 1` belong trivially; `1` is excluded by convention.[^3]
- **Near-integer powers come from the integer trace.** `θ^n + Σ α_j^n` is a rational integer and the conjugate part decays geometrically, so `‖θ^n‖ → 0` (Theorem 1).[^7] This is the mechanism behind `ψ^n − Perrin(n) → 0` on [[plastic-number](pages/plastic-number.md)] and the trace sequences of [[metallic-means](pages/metallic-means.md)].
- **Every real field has Pisot numbers** of full degree (Theorem 2, via Minkowski).[^8]
- **Two converses.** `Σ‖λθ^n‖² < ∞` forces `θ` into S (Theorem A). For algebraic `θ`, `‖λθ^n‖ → 0` is enough (Theorem B).[^9] The unconditional converse, whether a transcendental `θ` can have `‖λθ^n‖ → 0`, is open. Such `θ` form a countable set.[^13]
- **The rational-series toolkit.** Linear recurrence ⇔ rational series (Lemma I). Integer coefficients force `Q(0) = 1` (Fatou). Eventually-vanishing Hankel determinants ⇔ rational (Kronecker).[^10] These are the theory behind reading a recurrence off a castle count ([[recurrence-discovery](pages/recurrence-discovery.md)], [[berlekamp-massey](pages/berlekamp-massey.md)]).

## Contents

| Chapter | Title | pp. |
|---|---|---|
| I | A remarkable set of algebraic integers (class S, Theorems 1, 2, A, B, the open problem) | 1-12 |
| II | A property of the set of numbers of the class S (S is closed) | 13-21 |
| III | Applications to the theory of power series; another class of algebraic integers (class T) | 22-35 |
| IV | A class of singular functions; behavior of their Fourier-Stieltjes transforms at infinity | 36-41 |
| V | The uniqueness of the expansion in trigonometric series; general principles | 42-52 |
| VI | Symmetrical perfect sets with constant ratio of dissection; their classification into M-sets and U-sets | 53-56 |
| VII | The case of general "homogeneous" sets | 57-61 |
| - | Some unsolved problems; Appendix (algebraic integers, Kronecker, Weyl's criterion, Minkowski) | 62-66 |

Page numbers are the book's own, from the table of contents.[^15]

## Entities & Concepts

- [[pisot-number](pages/pisot-number.md)] - class S; the chapter's central object.
- [[plastic-number](pages/plastic-number.md)] - a cubic element of S; `ψ^n − Perrin(n) → 0` is Theorem 1 for it.
- [[metallic-means](pages/metallic-means.md)] - the quadratic elements of S with norm `−1`, generalizing the golden-ratio example.
- [[recurrence-discovery](pages/recurrence-discovery.md)] / [[berlekamp-massey](pages/berlekamp-massey.md)] - the computational side of Lemmas I and III.
- [[generating-functions](pages/generating-functions.md)] - the rational-GF toolkit that Lemma I restates.

## Relation to Other Wiki Pages

The wiki was already using Pisot numbers without a foundation for them. [[plastic-number](pages/plastic-number.md)] asserts the Pisot property and its near-integer consequence. [[castle-eigenvalue-oeis-crosswalk](pages/castle-eigenvalue-oeis-crosswalk.md)] and [[tower-parity-sectors](pages/tower-parity-sectors.md)] test castle eigenvalues for it. [[castle-classification-growth](pages/castle-classification-growth.md)] names a "cubic-Pisot family" of growth castles. [[reachable-field-census](pages/reachable-field-census.md)] lists "which cubics are Pisot / Salem" as open. This book supplies the definition, the reason powers approach integers, and the existence theorem, and [[pisot-number](pages/pisot-number.md)] applies them to the census cubics.

On the generating-function side, the wiki's standing principle "linear recurrence ⇔ rational GF" ([[aocp-generating-functions](pages/aocp-generating-functions.md)], [[generating-functions](pages/generating-functions.md)]) is Salem's Lemma I. Two refinements are new here. Fatou's lemma explains why every integer castle count with a rational GF has a denominator with integer coefficients and constant term 1. Kronecker's Hankel test is the determinant form of the rank question that [[berlekamp-massey](pages/berlekamp-massey.md)] answers algorithmically.

## Footnotes

[^1]: [[salem-1963-algebraic-numbers-fourier-analysis](pages/salem-1963-algebraic-numbers-fourier-analysis.md)] Preface [synthesis] L25-32 - "the substance of the lectures I gave in the fall of 1960 at Brandeis University"; "some of the material contained in this book appears in the latest edition of Zygmund's treatise, the subject matter covered here has never until now been presented as a whole"; "the presentation of a number of problems which remain unsolved".
[^2]: [[salem-1963-algebraic-numbers-fourier-analysis](pages/salem-1963-algebraic-numbers-fourier-analysis.md)] Preface L45 - "Professor Raphael Salem died suddenly in Paris on the twentieth ofJune, 1963, a few days after seeing final proof of his work."
[^3]: [[salem-1963-algebraic-numbers-fourier-analysis](pages/salem-1963-algebraic-numbers-fourier-analysis.md)] Ch. I §2 p.2 [synthesis] L275-282 - the definition of class S (an algebraic integer all of whose conjugates, not itself, have moduli strictly less than 1), and the footnote: θ is necessarily real and taken positive; every natural integer belongs to S but 1 is excluded, "Thus, in the definition we can always assume () > 1."
[^4]: [[salem-1963-algebraic-numbers-fourier-analysis](pages/salem-1963-algebraic-numbers-fourier-analysis.md)] Contents [synthesis] L74-165 - chapter titles: class S and its closure (I-II), power series and "the class T of algebraic integers" (III), Fourier-Stieltjes transforms of singular functions "at infinity" (IV), uniqueness of trigonometric series (V), symmetrical perfect sets "into M-sets and U-sets" (VI) and homogeneous sets (VII); Ch. IV p.41 L2884-2886 - "() = ~-1 belongs to the class S. We have thus shown that r(u) -:;e 0(1) implies that () E S."; Ch. VI p.53 L3651-3652 - "A necessary and sufficient conditionfor E(~) to be a set of uniqueness is that I/~ be a number of the class S [14]."
[^5]: [[salem-1963-algebraic-numbers-fourier-analysis](pages/salem-1963-algebraic-numbers-fourier-analysis.md)] Ch. I §1 pp.1-2 [synthesis] L212-260 - definition of uniform distribution mod 1 (due to Weyl); `(nξ)` uniformly distributed for irrational ξ; polynomials with an irrational non-constant coefficient; "almost nothing is known when the growth of f(n) is exponential"; Koksma: `ω^n` uniformly distributed for almost all `ω > 1`; not known for `e^n` or `(3/2)^n`, nor whether they are everywhere dense.
[^6]: [[salem-1963-algebraic-numbers-fourier-analysis](pages/salem-1963-algebraic-numbers-fourier-analysis.md)] Ch. I §1 p.2 [synthesis] L262-273 - the quadratic example `ω = (1+√5)/2` with conjugate `ω'`: `ω^n + ω'^n ≡ 0 (mod 1)`, `|ω'| < 1`, so `ω^n → 0 (mod 1)`, a single limit point.
[^7]: [[salem-1963-algebraic-numbers-fourier-analysis](pages/salem-1963-algebraic-numbers-fourier-analysis.md)] Ch. I §2 Theorem 1 and Remark p.3 [synthesis] L289-315 - `θ^n + α_1^n + … + α_{k−1}^n` is a rational integer, bounded error `(k−1)ρ^n` with `ρ < 1`, so `θ^n → 0 (mod 1)` "in the same way as the general term of a convergent geometric progression"; the Remark extends this to `λθ^n` for `λ` an algebraic integer of the field of `θ`.
[^8]: [[salem-1963-algebraic-numbers-fourier-analysis](pages/salem-1963-algebraic-numbers-fourier-analysis.md)] Ch. I §2 Theorem 2 p.3 [synthesis] L316-347 - "In every real algebraic field, there exist numbers of the class S", proved with Minkowski's theorem on linear forms applied to an integral basis; footnote: "there exist numbers of S having the degree of the field".
[^9]: [[salem-1963-algebraic-numbers-fourier-analysis](pages/salem-1963-algebraic-numbers-fourier-analysis.md)] Ch. I §3 p.4 [synthesis] L357-392 - the question whether `‖λθ^n‖ → 0` forces θ into S; "This important problem is still unsolved"; the two sufficient extra conditions; Theorem A (`Σ‖λθ^n‖² < ∞` ⇒ θ in S, λ in the field of θ) and Theorem B (θ algebraic and `‖λθ^n‖ → 0` ⇒ the same).
[^10]: [[salem-1963-algebraic-numbers-fourier-analysis](pages/salem-1963-algebraic-numbers-fourier-analysis.md)] Ch. I §3 Lemmas I-IV pp.4-7 [synthesis] L393-661 - Lemma I (rational iff a fixed-order linear recurrence for `m > m_0`), Lemma II (Fatou: integer coefficients ⇒ `P, Q` integral with `Q(0) = 1`, proved via primitive series), Lemma III (Kronecker: rational iff the Hankel determinants are zero for `m > m_1`), Lemma IV (Hadamard's determinant inequality).
[^11]: [[salem-1963-algebraic-numbers-fourier-analysis](pages/salem-1963-algebraic-numbers-fourier-analysis.md)] Ch. I §3 proof of Theorem A pp.8-9 [synthesis] L663-771 - `Δ_n` is a rational integer tending to 0, hence eventually 0; `Σ a_n z^n = P/Q` with `Q(0) = 1`; `λ/(1 − θz) − P/Q` has radius of convergence at least 1, so `Q` has the one root `1/θ` inside the unit circle and none on it; the reciprocal polynomial has θ as its only root outside the unit circle; `−λ/θ = P(1/θ)/Q'(1/θ)` puts λ in the field of θ.
[^12]: [[salem-1963-algebraic-numbers-fourier-analysis](pages/salem-1963-algebraic-numbers-fourier-analysis.md)] Ch. I §3 proof of Theorem B p.10 [synthesis] L775-822 - multiplying the minimal equation `A_0 + A_1θ + … + A_kθ^k = 0` by `λθ^N` makes `A_0 a_N + … + A_k a_{N+k}` an integer tending to 0, hence 0 for `N > N_0`; Lemma I then gives rationality; footnote: a series with `o(1)` coefficients "cannot have a pole on the unit circle".
[^13]: [[salem-1963-algebraic-numbers-fourier-analysis](pages/salem-1963-algebraic-numbers-fourier-analysis.md)] Ch. I §4 p.11 [synthesis] L839-898 - "the problem that is open is the existence of transcendental numbers" θ with `‖λθ^n‖ → 0`; Theorem: the set of such θ is denumerable, because `a_n a_{n+2} − a_{n+1}²` over `a_n` tends to 0, so "the integer a_{n+2} is uniquely determined by the two preceding integers"; θ = lim `a_{n+1}/a_n`; the λ are denumerable too.
[^14]: [[salem-1963-algebraic-numbers-fourier-analysis](pages/salem-1963-algebraic-numbers-fourier-analysis.md)] Ch. I Exercises p.12 [synthesis] L905-927 - Exercise 1 (θθ' in S for same-degree θ, θ' of S in one field; θ^q in S), Exercise 2 (Theorem A holds under `Σ_{j=1}^{n} ‖λθ^j‖² = o(n)`).
[^15]: [[salem-1963-algebraic-numbers-fourier-analysis](pages/salem-1963-algebraic-numbers-fourier-analysis.md)] Contents [synthesis] L73-172 - chapter and section titles with their page numbers.
