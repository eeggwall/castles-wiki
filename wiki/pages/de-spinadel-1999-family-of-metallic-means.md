---
title: "The Family of Metallic Means (de Spinadel, 1999)"
category: Sources
summary: Vera W. de Spinadel introduces the Metallic Means Family, the positive roots σ_p^q of x² − px − q = 0 for natural p and q, each the limit of ratios of a generalized secondary Fibonacci sequence G(n+1) = pG(n) + qG(n−1). With q = 1 the paper names the golden (p = 1), silver (p = 2, σ_Ag = 1 + √2) and bronze (p = 3, σ_Br = (3 + √13)/2) means; σ_4^1 = 2 + √5 = φ³ is noted, not named, and σ_p^1 = [p̄] for every p. With p = 1 it names the copper mean σ_Cu = 2 (q = 2) and the nickel mean σ_Ni = (1 + √13)/2 (q = 3). So copper and nickel are the q = 2 and q = 3 members with p = 1. The wiki uses this whole family, writes its q = 1 members as δ_a = σ_a^1, and uses only these five names. Summarized: §§1-3 and the quadratic-Pisot remark of §7; not the design, architecture and sculpture sections.
tags: [paper, source, metallic-mean, golden-ratio, silver-ratio, bronze-ratio, continued-fraction, quadratic-irrational, generalized-fibonacci, pisot-number, naming]
sources: [de-spinadel-1999-family-of-metallic-means]
created: 2026-10-09
updated: 2026-10-16
---

# The Family of Metallic Means (de Spinadel, 1999)

**Source:** `raw/de-spinadel-1999-family-of-metallic-means.md`, the text of the archived web edition (`web.archive.org/web/20230326024031/http://www.mi.sanu.ac.rs/vismath/spinadel/index.html`, fetched 2026-10-09). The page sets its formulas as images. The raw file transcribes the formula images it needs inside ⟦ ⟧, so those transcriptions are this wiki's and the surrounding text is the paper's. Each transcribed continued fraction was checked against a direct computation.[^exec] The page carries no volume or date. Other authors cite it as *Visual Mathematics* 1(3) (1999).[^cite]
**Author:** Vera W. de Spinadel (Centro de Matemática y Diseño, Facultad de Arquitectura, Diseño y Urbanismo, Universidad de Buenos Aires).[^1]
**Date ingested:** 2026-10-09
**Type:** paper (web edition, 8 sections)

> **Scope.** Summarized here: §1 (introduction), §2 (generalized secondary Fibonacci sequences), §3 (the family and its named members) and §7's statement on quadratic Pisot numbers. Not summarized: §4's additive property beyond one line, §5 (proportional systems in architecture), §6 (St. George sculptures), §8 (conclusions).

## Summary

**Generalized secondary Fibonacci sequences.** A sequence with `G(n+1) = p G(n) + q G(n−1)`, `p` and `q` natural numbers, is a generalized secondary Fibonacci sequence. Theorem 1 shows that the ratio `G(n+1)/G(n)` converges to the positive root of `x² − px − q = 0`, for any starting pair.[^2]

**The family.** The Metallic Means Family is the set of these positive roots, written `σ_p^q`, over all natural `p` and `q`. De Spinadel says its members are named after metals.[^3]

**`q = 1`: the purely periodic members.** For `x² − px − 1 = 0`:[^4]

| `p` | member | value | continued fraction |
|---|---|---|---|
| 1 | Golden Mean `φ` | `(1 + √5)/2` | `[1̄]` |
| 2 | Silver Mean `σ_Ag` | `1 + √2` | `[2̄]` |
| 3 | Bronze Mean `σ_Br` | `(3 + √13)/2` | `[3̄]` |
| 4 | `σ_4^1` (no name) | `2 + √5 = φ³` | `[4̄]` |
| 5-10 | `σ_5^1, …, σ_10^1` (no names) | `(p + √(p² + 4))/2` | `[p̄]` |

The paper calls `σ_4^1 = φ³` "a striking result related to the continued fraction expansion of uneven powers of the Golden Mean". All `q = 1` members have purely periodic expansions `[p̄]`, and the golden mean converges most slowly of them.[^4]

**`p = 1`: the copper and nickel means.** For `x² − x − q = 0`, `q = 1` gives the golden mean again:[^5]

| `q` | member | value | continued fraction |
|---|---|---|---|
| 2 | Copper Mean `σ_Cu` | `2` | `[2, 0̄]` (as a continued fraction, `2 = [2]`) |
| 3 | Nickel Mean `σ_Ni` | `(1 + √13)/2` | `[2, 3̄]` |
| 4-12 | `σ_1^4, …, σ_1^12` | `(1 + √(1 + 4q))/2` | `[2, 1̄,1̄,3̄]`, …, `σ_1^6 = 3`, …, `σ_1^12 = 4` |

An overline marks the period. The integer members `σ_1^q = 2, 3, 4, …` occur at `q = 2, 6, 12, 20, 30, …`. For the other members, write `m` for the first term of the expansion, the integer part of `σ_1^q`; the period is palindromic apart from its last term, which is `2m − 1` (checked for `q < 40`).[^6][^exec]

**Additive and Pisot properties.** The members of the family are the only positive quadratic irrationals whose generalized secondary Fibonacci sequences are also geometric progressions.[^7] The `q = 1` members, with purely periodic expansions, are quadratic Pisot numbers.[^8]

De Spinadel's Bridges 2003 paper names the same members: the silver mean `[2]`, the bronze mean `[3]`, the copper mean `2 = [2, 0̄]` and the nickel mean `(1 + √13)/2 = [2, 3̄]`.[^bridges]

## The castle reading

The wiki's metallic means ([[metallic-means](pages/metallic-means.md)]) are this family `σ_p^q`, with `δ_a = σ_a^1` for the `q = 1` members. Golden, silver and bronze are de Spinadel's names for `a = 1, 2, 3`, and the paper's `σ_4^1 = 2 + √5 = φ³` is the case `n = 3` of `δ_{L_n} = φ^n` for odd `n`, with `L_n` the Lucas numbers, which [[metallic-strip-realizability](pages/metallic-strip-realizability.md)] proves: `δ_a` is a power of `φ` exactly for `a = 1, 4, 11, 29, …`.

- **Copper and nickel.** De Spinadel's copper mean is `σ_1^2 = 2` and the nickel mean is `σ_1^3 = (1 + √13)/2`. Neither is a `δ_a`, and the paper gives `σ_4^1` and `σ_5^1` no names, so the wiki writes them `δ_4` and `δ_5`. The tree skylines of height at most `h` satisfy `T_h(w) = T_h(w − 1) + (h − 1)·T_h(w − 2)`, whose growth is the root `σ_1^{h−1}` of `x² − x − (h − 1)`, and the tree castles of height `h`, the differences `T_h − T_{h−1}`, grow at the same rate: golden by width at `h = 2`, copper at `h = 3`, nickel at `h = 4` ([[castle-graph](pages/castle-graph.md)], [[metallic-means](pages/metallic-means.md)]).
- **The wider family on castle strips.** A strip whose width generating function has denominator `1 − p_1 x − p_2 x²`, with `p_1, p_2 ≥ 1`, grows at `(p_1 + √(p_1² + 4 p_2))/2 = σ_{p_1}^{p_2}`, on the `q = 1` row exactly when `p_2 = 1` ([[metallic-strip-realizability](pages/metallic-strip-realizability.md)]). The rule on the heights `{1, 2, 3}` with no two neighboring columns of height 3 has denominator `1 − 2x − 2x²` and grows at `σ_2^2 = 1 + √3`.
- **Pisot.** §7 states that the `q = 1` members, the wiki's `δ_a`, are quadratic Pisot numbers.[^8]

## Entities & Concepts

- [[metallic-means](pages/metallic-means.md)] - the metallic means `σ_p^q` and `δ_a`, their continued fractions, and the named members.
- [[metallic-strip-realizability](pages/metallic-strip-realizability.md)], [[ridge-castle](pages/ridge-castle.md)] - the growth constants `σ_{p_1}^{p_2}` of castle strips, the ridge strips growing at `δ_{h−1}`, and the powers of `φ` among the `δ_a`.
- [[castle-graph](pages/castle-graph.md)] - the tree skylines and tree castles, which grow at `σ_1^{h−1}`.
- [[eigenvalue-continued-fractions](pages/eigenvalue-continued-fractions.md)] - the continued fractions of quadratic irrationals, and Galois's criterion for pure periodicity.

## Relation to Other Wiki Pages

[[metallic-means](pages/metallic-means.md)] takes its definition, its five names, the integer members and `σ_4^1 = φ³` from this paper. [[castle-classification-growth](pages/castle-classification-growth.md)] names growth types by its members, in the form "golden by width".

## Footnotes

[^1]: [[de-spinadel-1999-family-of-metallic-means](pages/de-spinadel-1999-family-of-metallic-means.md)] title block L9-21 - "THE FAMILY OF METALLIC MEANS", "Vera W. de Spinadel", "Centro de Matemática y Diseño -Facultad de Arquitectura, Diseño y Urbanismo", "Universidad de Buenos Aires".
[^cite]: https://arxiv.org/pdf/1807.04360v1 (Özkan and Yılmaz; search-result excerpt 2026-10-09), reference [23] - "The family of metallic means, Vis. Math. 1, 3(1999)"; https://www.heldermann-verlag.de/jgg/jgg13/j13h2spin.pdf (de Spinadel and Redondo Buitrago, J. Geom. Graphics 13 (2009); search-result excerpt 2026-10-09), reference [12] - "V.W. de Spinadel: The family of Metallic Means. Visual Mathematics 1/3 (1999)".
[^2]: [[de-spinadel-1999-family-of-metallic-means](pages/de-spinadel-1999-family-of-metallic-means.md)] §2 L29-131 [synthesis] - the "generalized secondary Fibonacci sequence" GSFS "that satisfy relations of the type (2.2) G(n+1) = p G(n) + q G(n − 1)", "p and q are natural numbers", the limit "x² − px − q = 0", Theorem 1 (the limit exists and is a real positive number), and "If, instead of choosing G(0) = G(1) = 1 we begin with two arbitrary values a and b ... the result is the same".
[^3]: [[de-spinadel-1999-family-of-metallic-means](pages/de-spinadel-1999-family-of-metallic-means.md)] §1 L27 and §3 L137-147 - "Let me introduce you to the Metallic Means Family (MMF). Their members have, among other common characteristics, the property of carrying the name of a metal"; "Definition: The metallic means family (MMF) is the set of positive eigenvalues of the matricial equation (3.1) ... for different values of p and q (natural numbers)", positive solutions of `x² − px − q = 0` (transcribed).
[^4]: [[de-spinadel-1999-family-of-metallic-means](pages/de-spinadel-1999-family-of-metallic-means.md)] §3 L148-188 - "if p = q = 1 ... the Golden Mean" `⟦x = (1+√5)/2 = [1̄] = φ⟧`; "if p = 2 y q = 1 we obtain the Silver Mean" `⟦σ_Ag = … = [2̄]⟧`; "If p = 3 and q = 1, we get the Bronze Mean" `⟦σ_Br = … = (3+√13)/2 = [3̄]⟧`; "For p = 4; q = 1, the metallic mean" `⟦σ_4^1 = 2+√5 = [4̄] = φ³⟧` "a striking result related to the continued fraction expansion of uneven powers of the Golden Mean"; "all of them are of the form [n̄]"; "The slowest converging one of all them is the Golden Mean". Formula text in ⟦ ⟧ is transcribed.
[^5]: [[de-spinadel-1999-family-of-metallic-means](pages/de-spinadel-1999-family-of-metallic-means.md)] §3 L190-205 - "If, instead, we consider equation" `⟦x² − x − q = 0⟧` "we have for q = 1, again the Golden Mean. If p = 1 and q = 2, we obtain the Copper Mean" `⟦σ_Cu = 2 = [2, 0̄]⟧`; "If p = 1 and q = 3, we get the Nickel Mean," `⟦σ_Ni = … = (1+√13)/2 = [2, 3̄]⟧`; the expansions of `σ_1^4, …, σ_1^12` (transcribed).
[^6]: [[de-spinadel-1999-family-of-metallic-means](pages/de-spinadel-1999-family-of-metallic-means.md)] §3 L207-215 [synthesis] - "the integer metallic means ... appear in quite a regular way. The first for q = 2 ..., the second for q = 6 ..., the third for q = 12 ..., the forth for q = 20 ..., the fifth for q = 30"; "The continued fraction expansions of the non integer metallic means are "palindromic" ... with the exception of the last digit of the period that is equal to 2m-1."
[^7]: [[de-spinadel-1999-family-of-metallic-means](pages/de-spinadel-1999-family-of-metallic-means.md)] §4 L249 - "The members of the MMF are the only positive quadratic irrational numbers that originate GSFS (with additive properties), which are, simultaneously, geometric progressions."
[^8]: [[de-spinadel-1999-family-of-metallic-means](pages/de-spinadel-1999-family-of-metallic-means.md)] §7 L353-355 - "the metallic means which expansion in continued fractions is purely periodic are quadratic Pisot numbers because they are the positive solution of quadratic equations of the form" `⟦x² − px − 1 = 0⟧` "p natural number."
[^bridges]: https://archive.bridgesmathart.org/2003/bridges2003-415.pdf (de Spinadel, "Number Theory and Art", Bridges 2003; PDF read 2026-10-09) p.415 abstract - "The Metallic Means Family (MMF), was introduced by the author [1]"; p.420 - "σ_Ag = [2,2,...] = [2̄] = 1+√2, the Bronze Mean σ_Br = (3+√13)/2 = [3̄]", "Other relatives are the Copper Mean σ_Cu = 2 = [2, 0̄], the Nickel Mean σ_Ni = (1+√13)/2 = [2, 3̄]".
[^exec]: Verified by execution (2026-10-09, SymPy `continued_fraction_periodic`): `(p + √(p² + 4))/2 = [p̄]` for `p = 1..10`, and `(1 + √(1 + 4q))/2` for `q = 1..12` gives `[1̄]`, `2`, `[2, 3̄]`, `[2, 1̄,1̄,3̄]`, `[2, 1̄,3̄]`, `3`, `[3, 5̄]`, `[3, 2̄,1̄,2̄,5̄]`, `[3, 1̄,1̄,5̄]`, `[3, 1̄,2̄,2̄,1̄,5̄]`, `[3, 1̄,5̄]`, `4`, matching the transcribed expansions; `1 + √3` is the positive root of `x² − 2x − 2`; on 2026-10-16 (Python 3.11, SymPy), for every non-integer `σ_1^q` with `q < 40` the period is palindromic apart from its last term, which is `2m − 1` with `m` the first term, and `δ_a` is a power of `φ` for `a < 40` exactly at `a = 1, 4, 11, 29`.
