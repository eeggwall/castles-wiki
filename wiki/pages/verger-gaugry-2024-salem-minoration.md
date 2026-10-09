---
title: "A Non-Trivial Minoration for the Set of Salem Numbers (Verger-Gaugry, 2024)"
category: Sources
summary: Verger-Gaugry's preprint claims that every Salem number exceeds θ_31^{-1} = 1.08544, where θ_n is the root in (0, 1) of −1 + x + x^n, a lower bound for Salem numbers that would settle Lehmer's conjecture restricted to them; the proof runs through the dynamical zeta function of the β-transformation. The claim is an unrefereed arXiv v1, and a later paper by other authors still calls the Salem case a conjecture. Its introduction and §3 collect the facts the area-growth census uses. Pisot numbers have minorant 1.3247 (Siegel). Lehmer's number 1.17628 is the smallest known Salem number, with Lehmer's degree-10 polynomial. Mossinghoff's list holds the 47 known Salem numbers below 1.3, all of degree ≤ 44. The Salem numbers of degree ≤ 8 all exceed 1.280638. Table 2 gives Lehmer's four small Salem numbers of 1933, of degrees 4, 6, 8 and 10, which the area-growth census finds first at heights 3, 3, 4 and 5. Only §1 and §3 are summarized; the proof machinery of §§2 and 4 is not.
tags: [paper, source, preprint, salem-number, pisot-number, perron-number, lehmer, mahler-measure, mossinghoff, beta-expansion, parry-number, trinomial, plastic-number, supergolden]
sources: [verger-gaugry-2024-salem-minoration]
created: 2026-10-09
updated: 2026-10-09
---

# A Non-Trivial Minoration for the Set of Salem Numbers (Verger-Gaugry, 2024)

**Source:** `raw/verger-gaugry-2024-salem-minoration.pdf` (text layer at `raw/verger-gaugry-2024-salem-minoration.txt`, extracted with `pdftotext -layout`; the PDF is git-ignored, the text is tracked). arXiv:2401.05843v1 [math.NT], 11 January 2024, the only version on the abstract page (fetched 2026-10-09).[^1]
**Author:** Jean-Louis Verger-Gaugry (Univ. Grenoble Alpes, Univ. Savoie Mont Blanc, LAMA, CNRS UMR 5127).[^1]
**Date ingested:** 2026-10-09
**Type:** preprint (PDF, 29 pp.)

> **Scope.** Summarized here: §1 (introduction, pp. 2-4) and §3 (the small Salem numbers known, Tables 1 and 2, pp. 9-11). Not summarized: §2 (the dynamical zeta function of the Rényi-Parry numeration system, pp. 5-9) and §4 (the proof of Theorem 1.1, pp. 11-25), which have no castle content.

## Summary

**Definitions.** A **Salem number** is an algebraic integer `β > 1` whose other conjugates all have modulus at most 1, at least one of them exactly 1. Then all conjugates but `1/β` lie on the unit circle, the degree is even and at least 4, and the minimal polynomial is reciprocal.[^2] A **Perron number** is 1 or a real algebraic integer `θ > 1` whose other conjugates all have modulus `< θ`. A **Pisot number** is a Perron number `> 1` whose other conjugates all have modulus `< 1`. The Pisot numbers have the minorant `Θ = 1.3247…`, the root of `X³ − X − 1` (Siegel).[^3] `T` denotes the set of Salem numbers and `S` the Pisot numbers; Salem proved that `S` is closed and lies in the closure of `T`.[^4]

**Lehmer's number and Mossinghoff's list.** The smallest known Salem number is Lehmer's number `τ = 1.17628…`, found by Lehmer in 1933, with minimal polynomial `X¹⁰ + X⁹ − X⁷ − X⁶ − X⁵ − X⁴ − X³ + X + 1`.[^5] Mossinghoff's list (2001, with contributions by several authors) gives the primitive irreducible noncyclotomic integer polynomials of degree at most 180 and Mahler measure below 1.3; it is complete for degrees below 40, and it contains the 47 known smallest Salem numbers, all of degree at most 44.[^6] Citing that list, §3 states that the Salem numbers of degree at most 8 all exceed `1.280638…`.[^7]

**Lehmer's four small Salem numbers (Table 2).** Lehmer's 1933 paper gives four small Salem numbers:[^8]

| degree | Salem number | minimal polynomial |
|---|---|---|
| 4 | `1.722…` | `X⁴ − X³ − X² − X + 1` |
| 6 | `1.401…` | `X⁶ − X⁴ − X³ − X² + 1` |
| 8 | `1.2806…` | `X⁸ − X⁵ − X⁴ − X³ + 1` |
| 10 | `1.17628…` | Lehmer's polynomial |

**The trinomial scale.** For `n ≥ 2`, `θ_n` is the root in `(0, 1)` of `−1 + x + xⁿ`, and `θ_n^{-1}` is a Perron number. For `n ≥ 5` the sequence `θ_n^{-1}` strictly decreases to 1.[^9] Table 1 sorts the known Salem numbers below 1.3 of degree at most 44 that are Parry numbers into the intervals `(θ_n^{-1}, θ_{n−1}^{-1})`, `n = 5, …, 12`. It starts from `θ_5^{-1} = 1.324717`, the smallest Pisot number, and places Lehmer's number in `(θ_12^{-1}, θ_11^{-1}) = (1.172950, 1.184276)`. That interval holds no other known Salem number, and any other Salem number there would have degree above 180.[^10]

**The claimed theorem.** Theorem 1.1 states that every Salem number exceeds `θ_31^{-1} = 1.08544…`. The paper presents this as Lehmer's conjecture restricted to Salem numbers. Conjecture 1 adds that there is no Salem number in `(θ_31^{-1}, θ_12^{-1}) = (1.08544…, 1.17295…)`, so Lehmer's number would be the smallest.[^11] The proof assumes a Salem number below `θ_31^{-1}`. It then finds a non-real pole of the β-transformation's dynamical zeta function inside the unit disk and identifies it as a Galois conjugate of `β`, which a Salem number cannot have.[^12]

**Status.** The claim is an arXiv v1 preprint with no journal reference on its abstract page. Douba and Huang's 2024 paper on systoles of hyperbolic manifolds still states "Lehmer's conjecture for Salem numbers, or the Salem conjecture", that the Salem numbers are bounded away from 1, as a conjecture.[^13] The wiki records Theorem 1.1 as the paper's claim.

## The castle reading

[[area-growth-census](pages/area-growth-census.md)] counts castle strips by area. Its growth constants are Perron numbers, and the census meets the Pisot and Salem lists.

- **Lehmer's four Salem numbers.** All four from Table 2 are area growth constants of castle strips. The degree-4 and degree-6 numbers (`1.722084`, `1.401268`) first appear at height 3, the degree-8 number (`1.280638`) at height 4, and Lehmer's number at height 5. These are the census's own first heights. The four minimal polynomials above have largest roots `1.722084`, `1.401268`, `1.280638` and `1.176281`, with every other root on the unit circle except the reciprocal (computed here).[^exec]
- **The degree-8 bound.** The census's degree-8 entry `1.280638` is the bound of §3 itself. It is the smallest Salem number of degree at most 8, and Table 2 gives its polynomial.[^7][^8]
- **Two height-2 constants on the trinomial scale.** `θ_3^{-1} = 1.465571` is the supergolden ratio, root of `x³ − x² − 1`. `θ_5^{-1} = 1.324718` is the plastic number, since `x⁵ − x⁴ − 1 = (x² − x + 1)(x³ − x − 1)`. Both are area growth constants of height-2 rules on [[area-growth-census](pages/area-growth-census.md)] (computed here).[^exec]

## Key Takeaways

- The census's Salem entries are anchored to their sources. The degree ≤ 8 minimum `1.280638` comes from §3, citing Mossinghoff's list, with its polynomial in Table 2. Lehmer's number and its polynomial are in §1.
- Lehmer's four small Salem numbers of 1933 all occur as castle-strip area growth constants, at heights 3, 3, 4 and 5.
- Theorem 1.1's lower bound `1.08544` for Salem numbers is a preprint claim; the Salem conjecture is treated as open elsewhere.

## Entities & Concepts

- Salem, Pisot and Perron numbers; Lehmer's number and Lehmer's polynomial; Mossinghoff's list - [[area-growth-census](pages/area-growth-census.md)] "Terms used on this page".
- The plastic number `θ_5^{-1}` - [[plastic-number](pages/plastic-number.md)].

## Relation to Other Wiki Pages

The census on [[area-growth-census](pages/area-growth-census.md)] cites §3 for the degree ≤ 8 minimum and Table 2 for Lehmer's four small Salem numbers. Its definitions of Pisot and Salem numbers, Siegel's minimum and Lehmer's number agree with §1. The plastic number, the smallest Pisot number here and the smallest area growth constant of any height-2 rule, is on [[plastic-number](pages/plastic-number.md)].

## Footnotes

[^1]: [[verger-gaugry-2024-salem-minoration](pages/verger-gaugry-2024-salem-minoration.md)] title page L1-8 - "A NON-TRIVIAL MINORATION FOR THE SET OF SALEM NUMBERS", "JEAN-LOUIS VERGER-GAUGRY", "arXiv:2401.05843v1 [math.NT] 11 Jan 2024"; affiliation L1502; https://arxiv.org/abs/2401.05843 (fetched 2026-10-09) - "[v1] Thu, 11 Jan 2024", the only version listed.
[^2]: [[verger-gaugry-2024-salem-minoration](pages/verger-gaugry-2024-salem-minoration.md)] §1 p.2 L50-55 - "A Salem number is an algebraic integer β > 1 such that its Galois conjugates β(i) satisfy: |β(i)| ≤ 1 ... at least one conjugate β(i), i ≠ 0, on the unit circle"; "Salem numbers are of even degree ≥ 4. The minimal polynomial Pβ(X) ∈ Z[X] of β is reciprocal."
[^3]: [[verger-gaugry-2024-salem-minoration](pages/verger-gaugry-2024-salem-minoration.md)] §1 p.2 L66-70 - "A Perron number is either 1 or a real algebraic integer θ > 1 such that the Galois conjugates ... satisfy: |θ(i)| < θ"; "The set of Pisot numbers admits the minorant Θ = 1.3247 . . ., unique root > 1 of X³ − X − 1 by a result of Siegel [97]."
[^4]: [[verger-gaugry-2024-salem-minoration](pages/verger-gaugry-2024-salem-minoration.md)] §1 p.3 L121-122 [synthesis] - "Salem [93] proved that the set S of Pisot numbers is closed, and S ⊂ T" (with `T` the closure of the Salem numbers, set in the text as T with a bar).
[^5]: [[verger-gaugry-2024-salem-minoration](pages/verger-gaugry-2024-salem-minoration.md)] §1 p.3 L126-131 - "The smallest Salem number known is Lehmer's number (1.5) τ := 1.17628 . . ., discovered by Lehmer in 1933 [63], with minimal polynomial (named "Lehmer's polynomial"): (1.6) X¹⁰ + X⁹ − X⁷ − X⁶ − X⁵ − X⁴ − X³ + X + 1."
[^6]: [[verger-gaugry-2024-salem-minoration](pages/verger-gaugry-2024-salem-minoration.md)] §1 pp.3-4 L133-141 - "the list of Mossinghoff [75] (2001) ... gives primitive, irreducible, noncyclotomic integer polynomials of degree at most 180 and of Mahler measure less than 1.3 [76]; this list is complete for degrees less than 40, and, for Salem numbers, contains the list of the 47 known smallest Salem numbers, all of degree ≤ 44."
[^7]: [[verger-gaugry-2024-salem-minoration](pages/verger-gaugry-2024-salem-minoration.md)] §3 p.9 L421-422 - "The Salem numbers of degree ≤ 8 are all greater than 1.280638 . . . from [75]."
[^8]: [[verger-gaugry-2024-salem-minoration](pages/verger-gaugry-2024-salem-minoration.md)] §3 p.11 Table 2 L496-504 - "The small Salem numbers, with their minimal polynomial, discovered by Lehmer in [63]": degree 4 `1.722 . . .` `X⁴ − X³ − X² − X + 1`; 6 `1.401 . . .` `X⁶ − X⁴ − X³ − X² + 1`; 8 `1.2806 . . .` `X⁸ − X⁵ − X⁴ − X³ + 1`; 10 `1.17628 . . .` Lehmer's polynomial.
[^9]: [[verger-gaugry-2024-salem-minoration](pages/verger-gaugry-2024-salem-minoration.md)] §1 p.4 L147-149 - "For every n ≥ 5, let θn be the unique root of the trinomial −1 + x + xⁿ in (0, 1); its inverse θn⁻¹ > 1 is a Perron number. The sequence (θn⁻¹)n≥5 is strictly decreasing, and satisfies: limn→∞ θn⁻¹ = 1."
[^10]: [[verger-gaugry-2024-salem-minoration](pages/verger-gaugry-2024-salem-minoration.md)] §1 p.4 L158-160 and §3 p.10 Table 1 L429-485 [synthesis] - Table 1, "Smallest Salem numbers β < 1.3 of degree ≤ 44, which are Parry numbers", by intervals of the `θ_n^{-1}`, from "θ5⁻¹ = 1.324717 ... smallest Pisot number - Siegel" to "θ12⁻¹ = 1.172950", with Lehmer's number between `θ_12^{-1}` and `θ_11^{-1} = 1.184276`; "This interval does not contain any other known Salem number. If there is another one, its degree should be greater than 180."
[^11]: [[verger-gaugry-2024-salem-minoration](pages/verger-gaugry-2024-salem-minoration.md)] §1 p.4 L145-146, L152-155, L164-166 - "It is the proof that the Conjecture of Lehmer, restricted to Salem numbers, is true"; "Theorem 1.1 (ex-Lehmer conjecture for Salem numbers). The set T is bounded from below: β ∈ T ⟹ β > θ31⁻¹ = 1.08544 . . ."; "Conjecture 1. There is no Salem number in the interval (θ31⁻¹, θ12⁻¹) = (1.08544 . . ., 1.17295 . . .)."
[^12]: [[verger-gaugry-2024-salem-minoration](pages/verger-gaugry-2024-salem-minoration.md)] §1 p.4 L168-182 [synthesis] - outline of the proof: for `1 < β < θ_31^{-1}` the dynamical zeta function `ζ_β(z)` "systematically admits a lenticular pole which is non-real, of modulus < 1", identified via Kala-Vavra's theorem "as a Galois conjugate of 1/β, then of β"; "a Salem number β never admits a non-real conjugate in the open unit disk."
[^13]: https://arxiv.org/pdf/2404.15927v2 (S. Douba and J. Huang, "Density of systoles of hyperbolic manifolds", v2 12 Nov 2024; pp. 1-2 read 2026-10-09) p.2 - "Lehmer's conjecture for Salem numbers, or the Salem conjecture for short, asserts that the Salem numbers are bounded away from 1"; Corollary 2.1, "The Salem conjecture holds if and only if ... the set of systoles of closed arithmetic hyperbolic n-manifolds fails to be dense in (0, +∞)."
[^exec]: Verified by execution (2026-10-09, NumPy): the roots of the four Table 2 polynomials have largest modulus `1.722084`, `1.401268`, `1.280638`, `1.176281`, the reciprocal of it, and all others of modulus 1. The largest real roots of `xⁿ − xⁿ⁻¹ − 1` are `1.465571` (n = 3), `1.380278`, `1.324718` (n = 5), `1.285199`, `1.255423`, `1.232055`, `1.213150`, `1.197491`, `1.184276`, `1.172951` (n = 12), matching Table 1's `θ_n^{-1}`. The first heights are those of [[area-growth-census](pages/area-growth-census.md)].
