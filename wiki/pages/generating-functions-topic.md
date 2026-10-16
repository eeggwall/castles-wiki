---
title: "Generating Functions (Sedgewick-Flajolet, Trotter)"
category: Sources
summary: Notes on generating functions from Sedgewick and Flajolet's Analysis of Algorithms and Trotter's Chapter 8 - the operations on ordinary generating functions, recurrences solved by partial fractions (3^n − 2^n, n·2^{n−1}, a pair of imaginary roots, quicksort), counting with restricted parts (z/(1 − z)^3 for the marbles), the exponential generating function (e^x + e^{−x})/2 that keeps even counts, every fourth term of 1/(1 − x^4), and a closing note that the signed tower count P(k, L) has a rational generating function in L, evaluated by Kitamasa's method.
tags: [generating-functions, ogf, egf, recurrence, parity, partial-fractions, source]
sources: [generating-functions-topic]
created: 2026-09-14
updated: 2026-10-16
---

# Generating Functions (Sedgewick-Flajolet, Trotter)

**Source:** https://charlesreid1.com/wiki/Generating_Functions
**Date ingested:** 2026-09-14
**Type:** article (MediaWiki topic page)

## Summary

The page collects notes on generating functions from two books, Sedgewick and Flajolet's *Analysis of Algorithms* and Chapter 8 of Trotter.[^1] It lists the operations on an ordinary generating function `G(z) = Σ_k a_k z^k`, works recurrences and counting problems to closed forms, introduces exponential generating functions for counts in which order matters, and ends with a short section on Project Euler 502.[^2]

## Key Takeaways

- **Operations.** Sums of generating functions add coefficients; `z·G′(z)` multiplies `a_k` by `k`; integration divides `a_{k−1}` by `k`; `G(z)/(1 − z)` has the partial sums `a_0 + ⋯ + a_k` as coefficients; and the product of two generating functions has the convolution `Σ_{k≤m} a_k b_{m−k}` as coefficients. Differentiating `1/(1 − z)` gives[^3]

  ```
  1/(1 − z)^{m+1}  =  Σ_{k≥0} C(k+m, m) z^k.
  ```

- **Two-term recurrence.** `a_n = 5a_{n−1} − 6a_{n−2}` with `a_0 = 0`, `a_1 = 1` has `G(z) = z/(1 − 5z + 6z²) = 1/(1 − 3z) − 1/(1 − 2z)`, so `a_n = 3^n − 2^n`: `0, 1, 5, 19, 65, 211, 665, …`.[^4] These are the castles of width `n` and height 3, `A(n, 3) = 3^n − 2^n` ([[castle-counting-function](pages/castle-counting-function.md)]).
- **A double root.** `a_n = 5a_{n−1} − 8a_{n−2} + 4a_{n−3}` with `a_0 = 0`, `a_1 = 1`, `a_2 = 4` has `G(z) = z/(1 − 2z)²`, so `a_n = n·2^{n−1}`.[^4]
- **Imaginary roots.** `a_n = 2a_{n−1} − a_{n−2} + 2a_{n−3}` with `a_0 = 1`, `a_1 = 0`, `a_2 = −1` has `G(z) = (1 − 2z)/(1 − 2z + z² − 2z³)`. The denominator is `(1 − 2z)(1 + z²)`, so `G(z) = 1/(1 + z²) = ½(1/(1 − iz) + 1/(1 + iz))` and `a_n = ½(i^n + (−i)^n)`: `1, 0, −1, 0, 1, 0, −1, …`.[^5] The poles `±i` are complex conjugates, so the closed form is real. The same happens for `P_1(x) = (1 − 2x)/(1 − 2x + 2x²)`, whose denominator has the roots `(1 ± i)/2`, and gives `P(1, L) = Re((1+i)^{L+1})` ([[signed-tower-count](pages/signed-tower-count.md)]).
- **Quicksort.** The recurrence `C_n = n + 1 + (2/n) Σ_{k≤n} C_{k−1}` becomes the differential equation `C′(z) = 2/(1 − z)^3 + 2C(z)/(1 − z)`, solved by `C(z) = (2/(1 − z)²) ln(1/(1 − z))`, so `C_n = 2(n + 1)(H_{n+1} − 1)` with `H_n` the harmonic numbers.[^6]
- **Restricted parts.** Distributing apples to `n` children, each getting at least one, has generating function `z^n/(1 − z)^n`. Cans of marbles with at least one red, at most three blue, any number of yellow and a multiple of four green have generating function[^7]

  ```
  z/(1 − z) · (1 + z + z² + z³) · 1/(1 − z) · 1/(1 − z^4)  =  z/(1 − z)^3  =  Σ_{n≥1} C(n+1, 2) z^n,
  ```

  since `1 + z + z² + z³ = (1 − z^4)/(1 − z)`; a can of 20 marbles has `C(21, 2) = 210` fillings. The coefficients `C(n+1, 2)` are also the convex castles of width `n` and height 2, `C(2h + n − 3, n − 1)` at `h = 2` ([[convex-castle-binomial-identity](pages/convex-castle-binomial-identity.md)]).
- **Exponential generating functions.** The ternary strings of length `n` with an even number of 0s have exponential generating function `e^x · e^x · (e^x + e^{−x})/2 = (e^{3x} + e^x)/2`, one factor for each digit. The factor `(e^x + e^{−x})/2 = Σ_k x^{2k}/(2k)!` keeps only the even numbers of 0s, and the count is `(3^n + 1)/2`: `1, 2, 5, 14, 41, 122, …`.[^8] The castle split applies the same selection `(1 + (−1)^b)/2` to the block count `b`: `(T ± P)/2` over towers and `A^e, A^o = (A ± S)/2` over castles ([[castle-sign](pages/castle-sign.md)], [[parity-via-roots-of-unity](pages/parity-via-roots-of-unity.md)]).
- **Every fourth term.** In `1/(1 − x^4) = (1/4)/(1 − x) + (1/4)/(1 + x) + (1/2)/(1 + x²)`, the coefficient of `x^k` is `(1 + (−1)^k + i^k + (−i)^k)/4`, which is 1 when `4` divides `k` and 0 otherwise, so `1/(1 − x^4) = Σ_k x^{4k}`.[^9] The same average over the fourth roots of unity gives the sums of every fourth binomial coefficient, `A038503` and `A038505`, which count the castles of height 2 by block parity ([[hyperbolic-sequence-family](pages/hyperbolic-sequence-family.md)]).

## Project Euler 502

The closing section says that the recursion for `P(k, L)` lifts to a rational generating function `num_k(x)/den_k(x)`, built level by level, and that extracting its coefficients is a linear recurrence whose characteristic polynomial is `den_k` reversed, which is the setting of Kitamasa's method ([[kitamasa](pages/kitamasa.md)]).[^10] The source writes the generating function `F_k(x)`; the wiki writes `P_k(x) = Σ_L P(k, L) x^L` ([[castle-counting-formula](pages/castle-counting-formula.md)], Equations (4) and (5)).

## Entities & Concepts

- [[generating-functions](pages/generating-functions.md)] - the castle generating functions and coefficient matching.
- [[signed-tower-count](pages/signed-tower-count.md)] - `P(1, L) = Re((1+i)^{L+1})` and the characteristic polynomials `char_k`.
- [[castle-counting-formula](pages/castle-counting-formula.md)] - `P_k(x) = num_k(x)/den_k(x)` and the recurrence of `P(k, ·)`.
- [[kitamasa](pages/kitamasa.md)] - one term of a linear recurrence far out, by reducing `x^n` modulo the characteristic polynomial.
- [[castle-sign](pages/castle-sign.md)] - the split of towers and castles by block parity.
- [[parity-via-roots-of-unity](pages/parity-via-roots-of-unity.md)] - block counts modulo `m`, and the substitution `x → −x` that selects even indices.
- [[hyperbolic-sequence-family](pages/hyperbolic-sequence-family.md)] - the four sums of every fourth binomial coefficient.
- [[block-count-constraints](pages/block-count-constraints.md)] - selecting towers and castles by block count, through roots of unity, lacunary series and numerical semigroups.
- [[convex-castle-binomial-identity](pages/convex-castle-binomial-identity.md)] - the convex castle count `C(2h + w − 3, w − 1)`.

Linked from the source: [[aocp-generating-functions](pages/aocp-generating-functions.md)].

## Relation to Other Wiki Pages

[[aocp-generating-functions](pages/aocp-generating-functions.md)] covers Knuth's treatment of the same recurrence-to-closed-form method. [[analytic-combinatorics-ch1-ogfs](pages/analytic-combinatorics-ch1-ogfs.md)] reaches generating functions from a specification of the class instead of a recurrence ([[symbolic-method](pages/symbolic-method.md)]).

## Footnotes

[^1]: [[generating-functions-topic](pages/generating-functions-topic.md)] §"Notes" L5, L68 - "Sedgewick Flajolet: Analysis of Algorithms", "Trotter Chapter 8: Generating Functions".
[^2]: [[generating-functions-topic](pages/generating-functions-topic.md)] §"Exponential Generating Functions" L95-97 and §"Application: Project Euler 502" L121-126 - "When order matters, use EGFs", and the closing section on the `P(k, L)` recursion.
[^3]: [[generating-functions-topic](pages/generating-functions-topic.md)] §"Ordinary Generating Functions" to §"Multiplication" L7-37 - "z G'(z) = sum_{k>=1} k a_k z^k", "1/(1-z)^{m+1} = sum_{k>=0} C(k+m,m) z^k", "(1/(1-z)) G(z) -> a_0, (a_0+a_1), (a_0+a_1+a_2), ...", "Convolution: G_1(z) G_2(z) = sum_m (sum_{0<=k<=m} a_k b_{m-k}) z^m".
[^4]: [[generating-functions-topic](pages/generating-functions-topic.md)] §"Example: Two-Term Recurrence" L45-47 and §"Example: Three-Term Recurrence" L51-53 - "G(z) = z/(1 - 5z + 6z^2). Partial fractions: G(z) = 1/(1-3z) - 1/(1-2z), giving a_n = 3^n - 2^n", "G(z) = (z - z^2)/(1 - 5z + 8z^2 - 4z^3) = z(1-z)/((1-z)(1-2z)^2) = z/(1-2z)^2. Expanding: a_n = n 2^{n-1}". Both recomputed (SymPy, 2026-10-16).
[^5]: [[generating-functions-topic](pages/generating-functions-topic.md)] §"Example: Imaginary Roots" L57-60 - "a_n = 2 a_{n-1} - a_{n-2} + 2 a_{n-3}, a_0=1,a_1=0,a_2=-1. G(z) = (1-2z)/(1 - 2z + z^2 - 2z^3) = 1/(1 + z^2)", "a_n = (1/2)(i^n + (-i)^n) ... -> 1, 0, -1, 0, 1, 0, -1, 0, 1". The factorization `(1 − 2z)(1 + z²)` and the series recomputed (SymPy, 2026-10-16).
[^6]: [[generating-functions-topic](pages/generating-functions-topic.md)] §"Example: Quicksort Recurrence" L64-66 - "C'(z) = 2/(1-z)^3 + 2 C(z)/(1-z) ... C(z) = (2/(1-z)^2) ln(1/(1-z)), whence C_n = [z^n] C(z) = 2(n+1)(H_{n+1} - 1)".
[^7]: [[generating-functions-topic](pages/generating-functions-topic.md)] §"Alternative Generating Functions Introduction" to §"Taylor Series Analysis" L72-92 - "n children: G_n(z) = z^n/(1-z)^n", "G_r = z/(1-z); G_b = 1 + z + z^2 + z^3; G_y = 1/(1-z); G_g = 1/(1-z^4)", "Product simplifies to G(z) = z/(1-z)^3", "sum_{n>=1} C(n+1,2) x^n", "For a can of 20 marbles: 21 choose 2 = 210". The product and the coefficients recomputed (SymPy, 2026-10-16).
[^8]: [[generating-functions-topic](pages/generating-functions-topic.md)] §"EXAMPLE Counting Ternary Strings" L101-107 - "E_0 = (e^x + e^{-x})/2 = sum x^{2k}/(2k)! (the odd terms cancel; this is the parity-selecting trick)", "E(x) = E_0 E_1 E_2 = (e^x)(e^x)(e^x + e^{-x})/2 = (e^{3x} + e^x)/2 = (1/2) sum (3^n + 1) x^n/n!". The count checked against enumeration for `n ≤ 5`.
[^9]: [[generating-functions-topic](pages/generating-functions-topic.md)] §"Problem 3" L115-117 - "(1/4)/(1-x) + (1/4)/(1+x) + (1/2)/(1+x^2). The 1+(-1)^k and the imaginary ((-i)^k + i^k) terms leave only k divisible by 4: G(x) = sum x^{4k}".
[^10]: [[generating-functions-topic](pages/generating-functions-topic.md)] §"Application: Project Euler 502" L123-126 - "The P(k, L) recursion ... lifts to a rational generating function F_k(x) = num_k(x) / den_k(x) with level-by-level update rules. Coefficient extraction reduces to a linear recurrence with characteristic polynomial den_k(x) (reversed), which is exactly the setup where Kitamasa's method applies."
