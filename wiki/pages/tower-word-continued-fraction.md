---
title: Continued fractions of the tower word
category: Concepts
summary: Flajolet's theorem identifies the Jacobi continued fraction with the generating function of weighted Motzkin paths. The tower words are the Motzkin paths with no UD and no DU; counted by length they are A004149, whose generating function satisfies a quadratic with discriminant (z−1)(z+1)(z²+1)(z²+2z−1), so they grow like (1 + √2)^n with a square-root singularity, and OEIS lists a continued fraction for them. Counted by width at height at most k, 1/E_k = 1/E_{k−1} − x telescopes to 1/(1 − (k+1)x), while the Motzkin paths of height at most k are the convergents of the Motzkin J-fraction.
tags: [concept, castle, tower-word, continued-fraction, flajolet, motzkin, algebraic, oeis, generating-functions]
sources: [project-euler-502-representations]
created: 2026-09-14
updated: 2026-10-22
---

# Continued fractions of the tower word

## Tower words as Motzkin paths

A **tower word** is the word of the towers on a base of length `L`, in the letters `U` (up one row), `R` (one column, written once per column at the column's height) and `D` (down one row). It starts and ends at height 0, never goes below 0, and contains neither `UD` nor `DU`.[^1] With `U = +1`, `R = 0` and `D = −1` it is a Motzkin path with no peak `UD` and no valley `DU`, a cornerless Motzkin path ([[tower-word-language](pages/tower-word-language.md)]). For example `URDRURD` is the word of the towers `(1, 0, 1)`.

## Flajolet: continued fractions count paths

Flajolet proves that the Jacobi continued fraction is the generating function of Motzkin paths in which each step is weighted by its type and by the height it starts from: a rise from height `j` by `a_j`, a fall from height `j` by `b_j`, and a flat step at height `j` by `c_j`, so that the fraction is `1/(1 − c_0 − a_0 b_1/(1 − c_1 − a_1 b_2/(1 − ⋯)))` (Theorem 1, p.129).[^2] Setting the flat weights to 0 leaves the Dyck paths and the Stieltjes continued fraction. With every weight 1, the coefficients of the Jacobi fraction sum to the Motzkin numbers and those of the Stieltjes fraction to the Catalan numbers (p.131).[^2] The two simplest cases, with `z` marking length:[^3]

- the **Catalan S-fraction** `C(z) = 1/(1 − z/(1 − z/(1 − ⋯))) = (1 − √(1 − 4z))/(2z)`, with coefficients `1, 1, 2, 5, 14, 42, 132, …`, counting Dyck paths with `z` marking each pair `UD`;
- the **Motzkin J-fraction** `M(z) = 1/(1 − z − z²/(1 − z − z²/(1 − ⋯))) = (1 − z − √(1 − 2z − 3z²))/(2z²)`, with coefficients `1, 1, 2, 4, 9, 21, 51, 127, …`, counting Motzkin paths.

Truncating a continued fraction at depth `k` gives the paths of height at most `k`; for these Flajolet notes that the set of paths is regular, so the convergents are rational (proof of Theorem 1, p.129).[^2] For Motzkin paths, with `M_0(z) = 1/(1 − z)`,[^3]

```
M_k(z)  =  1/(1 − z − z²·M_{k−1}(z))
```

counts the Motzkin paths of height at most `k`.

## The tower words by length

Mark each step by `z`, so a tower word with `L` letters `R` and `b` blocks has weight `z^{L + 2b}`. Each length has finitely many tower words, and the tower words of length `n` number `A004149(n + 1)`:[^3][^4]

```
1, 1, 1, 2, 4, 8, 16, 33, 69, 146, 312, 673, 1463, 3202, 7050, 15605, …        (n = 0, 1, 2, …)
```

OEIS describes `A004149(n)` as the "Number of Motzkin paths of length n-1 (n>=1) with no peaks and no valleys, i.e., no UD's and no DU's".[^4] At `n = 3` the tower words are `RRR` and `URD`.

Reading the tower grammar with every step marked by `z` gives, for the generating function `E(z)` of the tower words by length,[^3]

```
E(z)  =  1 + z·E(z) + z²(E(z) − 1)(1 + z·E(z)),
z³E² − (1 − z − z² + z³)E + (1 − z²)  =  0,                                   (1)
```

with discriminant `(z − 1)(z + 1)(z² + 1)(z² + 2z − 1)`. With `g(z) = 1 + z·E(z)`, Equation (1) is equivalent to the equation `z²g² − (1 − z + z² + z³)g + 1 = 0` of the OEIS entry.[^4] The discriminant has a simple zero at `z = √2 − 1`, the zero of smallest modulus, so `E(z)` has a square-root singularity there and is algebraic but not rational. The tower words grow like `(√2 + 1)^n`, so they are silver by length; OEIS gives `A004149(n) ~ (1 + √2)^{n+1/2}/(√π n^{3/2})`.[^4] The silver mean `1 + √2 = [2; 2, 2, …]` is `δ_2` of [[metallic-means](pages/metallic-means.md)], and its continued fraction is on [[eigenvalue-continued-fractions](pages/eigenvalue-continued-fractions.md)].

OEIS lists a continued fraction for the generating function of `A004149`, due to Barry:[^4]

```
g(z)  =  1/(1 − z − z⁴/(1 − z − z² − z³ − z⁴/(1 − z − z² − z³ − z⁴/(1 − ⋯)))),
```

whose expansion agrees with `A004149` through `n = 15`.[^3] Its references include Barry's *Generalized Catalan recurrences, Riordan arrays, elliptic curves, and orthogonal polynomials* and Asinowski, Banderier and Roitner's *Generating functions for lattice paths with several forbidden patterns*, and Prodinger's paper on cornerless Motzkin paths ([[prodinger-2025-cornerless-motzkin-bargraphs](pages/prodinger-2025-cornerless-motzkin-bargraphs.md)]).[^4]

## The tower words by width

Without the conditions on `UD` and `DU`, the tower grammar becomes the first-return grammar of Motzkin paths: the inner word `V` may be empty, which allows `UD`, and a `U` may follow the closing `D`, which allows `DU`. The tower words are therefore a subset of the Motzkin paths.

With the height bounded by `k` and `x` marking each `R`, the grammar gives `E_k(x) = E_{k−1}(x)/(1 − x·E_{k−1}(x))` with `E_0(x) = 1/(1 − x)` ([[castle-counting-formula](pages/castle-counting-formula.md)], the section *Tower count*).[^5] In reciprocal form,

```
1/E_k(x)  =  1/E_{k−1}(x) − x,
```

which telescopes from `1/E_0(x) = 1 − x` to `1/E_k(x) = 1 − (k+1)x`: each row of height subtracts one `x`. So `T(k, L) = (k+1)^L`. Counting by width needs the conditions on `UD` and `DU`, since without them the factors `UD` add length but no `R`, and each `L` has infinitely many words. The Motzkin paths of height at most `k`, counted by length, instead nest as the convergents `M_k(z)` of the Motzkin J-fraction (section *Flajolet: continued fractions count paths*). Without a height bound, the tower words with `L` letters `R` are infinite in number, while the tower words and the Motzkin paths counted by length have the algebraic generating functions `E(z)` and `M(z)`.

## Appearances in Sources

- [[project-euler-502-representations](pages/project-euler-502-representations.md)] - the tower word, its two excluded factors, and the grammar from which `E_k(x)` and Equation (1) are read off.

## Related Concepts

- [[tower-word-language](pages/tower-word-language.md)] - the tower words as a formal language, the bijection with column heights, and the proof that the grammar is unambiguous.
- [[generalized-dyck-grammar](pages/generalized-dyck-grammar.md)] - the tower grammar.
- [[castle-counting-formula](pages/castle-counting-formula.md)] - `E_k(x) = 1/(1 − (k+1)x)` and the signed version `P_k(x)`.
- [[motzkin-numbers](pages/motzkin-numbers.md)] - the Motzkin numbers counted by the J-fraction.
- [[dyck-words](pages/dyck-words.md)] and [[catalan-numbers](pages/catalan-numbers.md)] - Dyck words and the Catalan numbers counted by the S-fraction.
- [[deutsch-elizalde-2016-bargraphs-cornerless-motzkin](pages/deutsch-elizalde-2016-bargraphs-cornerless-motzkin.md)] - bargraphs as cornerless Motzkin paths, and a continued fraction for bargraphs by area from the first-return decomposition.
- [[prellberg-brak-1995-cluster-models](pages/prellberg-brak-1995-cluster-models.md)] - the functional equation (3.11) for bargraphs by width, blocks and area, and the continued fraction (3.12) obtained by iterating it.[^6]
- [[prodinger-2025-cornerless-motzkin-bargraphs](pages/prodinger-2025-cornerless-motzkin-bargraphs.md)] - Motzkin paths counted with a weight for each `UD` and each `DU`; with both weights 0, the paths returning to 0 are `A004149` and the paths ending at any height are `A308435`.
- [[castle-by-area](pages/castle-by-area.md)] - castles counted by area.
- [[steep-polyominoes-q-motzkin-bessel](pages/steep-polyominoes-q-motzkin-bessel.md)] - steep Dyck words and the q-Motzkin numbers.
- [[generating-function-gallery](pages/generating-function-gallery.md)] and [[closed-form-hunting](pages/closed-form-hunting.md)] - the rational generating functions of `P(k, L)` and the roots of their characteristic polynomials.
- [[pell-numbers](pages/pell-numbers.md)] and [[pell-castle-strip](pages/pell-castle-strip.md)] - the Pell numbers, which also grow like `(1 + √2)^n`, and the strips they count.

## Footnotes

[^1]: [[project-euler-502-representations](pages/project-euler-502-representations.md)] §"The tower word" L227-230 - "A tower above a length-L block uses exactly L R's, never drops below the base, and returns to it", "a valid tower word has no UD (that would be a zero-width block) and no DU (two touching blocks)".
[^2]: https://algo.inria.fr/flajolet/Publications/Flajolet80b.pdf (read 2026-10-16) - P. Flajolet, "Combinatorial aspects of continued fractions", Discrete Mathematics 32 (1980) 125-161: abstract p.125, "the universal continued fraction of the Stieltjes-Jacobi type is equivalent to the characteristic series of labelled paths in the plane"; Theorem 1 p.129, "the characteristic series of labelled paths is equal to this infinite continued fraction", with "For each h, the set P^[h] is a regular or rational set" in its proof; p.131, the Stieltjes type "appears when we set formally the c_j's to 0", and "the sum of the coefficients of R_n is the nth Motzkin number, and the sum of the coefficients of R'_2n is the nth Catalan number".
[^3]: Verified by execution (Python 3.11 with SymPy, 2026-10-16): the S-fraction and J-fraction expansions against the Catalan and Motzkin numbers; `M_k(z)` against enumeration of Motzkin paths of height at most `k` for `k ≤ 3`, length at most 8; the tower words of length `n ≤ 11` by enumeration, equal to `A004149(n+1)`, and the series of the root of Equation (1) through `n = 11`; the factorization of the discriminant; Barry's continued fraction against `A004149` through `n = 15`.
[^4]: https://oeis.org/A004149 (read 2026-10-16) - "Number of Motzkin paths of length n-1 (n>=1) with no peaks and no valleys, i.e., no UD's and no DU's, where U=(1,1) and D=(1,-1)" (Emeric Deutsch, Jan 08 2004); "G.f. g(x) satisfies x^2*g^2 - (1-x+x^2+x^3)*g + 1 = 0" (Robert Israel); "a(n) ~ (1+sqrt(2))^(n+1/2)/(sqrt(Pi)*n^(3/2))" (Vaclav Kotesovec); "G.f.: 1/(1-x-x^4/(1-x-x^2-x^3-x^4/(1-x-x^2-x^3-x^4/(1-... (continued fraction)" (Paul Barry, May 22 2009); references to Barry (arXiv:1910.00875), Asinowski, Banderier and Roitner (2019), and Prodinger (arXiv:2501.13645).
[^5]: [[project-euler-502-representations](pages/project-euler-502-representations.md)] §"Unsigned count" L294-310 - "E_k = E_{k-1}/(1 - x E_{k-1})", "The base case E_0 ... 1/(1-x)", "E_k = 1/(1 - (k+1)x)", "T(k,L) = (k+1)^L".
[^6]: [[prellberg-brak-1995-cluster-models](pages/prellberg-brak-1995-cluster-models.md)] `prellberg-brak-1995-partially-directed-cluster-models.txt` §3.1 L473-480 - "This equation can be solved for B(x, y, q) and leads to a continued-fraction representation of the generating function, given by iteration of" eq. (3.12).
