---
title: Generating functions
category: Concepts
summary: A generating function is a formal power series whose coefficients are the counts of a problem, so that computing a count becomes extracting a coefficient. The castle instances are the tower generating functions E_k(x) = 1/(1 − (k+1)x) and P_k(x) = num_k(x)/den_k(x), which give A^e(w, h), and the negative binomial series of the convex castle count. Three sources treat the method; the operation used most is reading a linear recurrence and its initial terms off a rational generating function by matching coefficients.
tags: [concept, generating-functions, combinatorics, method, symbolic-method]
sources: [project-euler-502-problem-setup, project-euler-502-representations, project-euler-502-castle-factoring, aocp-generating-functions, generating-functions-topic, analytic-combinatorics-ch1-ogfs, pe502-pell-castle-strip]
created: 2026-09-13
updated: 2026-10-16
---

# Generating functions

## Description

A **generating function** of a counting problem is a formal power series, in one or more variables, whose coefficients are the counts. The source describes it as a multivariate polynomial whose variables are the dimensions of the problem, width and height or other variables, and whose coefficients are the solutions; computing one count then becomes evaluating one coefficient.[^1]

*Example.* The towers of height at most 1 on a base of length `L` are the binary strings of length `L`, so `T(1, L) = 2^L` and

```
E_1(x)  =  Σ_{L≥0} T(1, L) x^L  =  1 + 2x + 4x² + 8x³ + ⋯  =  1/(1 − 2x).
```

On the wiki, generating functions compute the castle counts `A^e(w, h)` of the [[castle-counting-function](pages/castle-counting-function.md)] (the `F(w, h)` of the problem statement) at sizes where enumerating the [[castle-polyomino](pages/castle-polyomino.md)] configurations is impossible.

## The castle generating functions

**Towers.** The tower grammar of [[generalized-dyck-grammar](pages/generalized-dyck-grammar.md)] gives two generating functions in the base length, `x` marking one column ([[castle-counting-formula](pages/castle-counting-formula.md)], Equations (2) to (5)):[^2]

- the tower count, `E_k(x) = Σ_L T(k, L) x^L = 1/(1 − (k+1)x)`, so `T(k, L) = (k+1)^L`;
- the signed tower count, `P_k(x) = Σ_L P(k, L) x^L = num_k(x)/den_k(x)`, a rational function with a denominator of degree `k + 1`, built by a polynomial update from `P_0(x) = 1/(1 − x)`. For example `P_1(x) = (1 − 2x)/(1 − 2x + 2x²)`.

`A^e(w, h)` uses two coefficients of `P_k(x)`, `P(h−1, w)` and `P(h−2, w)` ([[castle-counting-formula](pages/castle-counting-formula.md)], Equation (1)).

**Convex castles.** The negative binomial series `1/(1 − z)^{n+1} = Σ_j C(n + j, n) z^j` counts the convex castles. Write a castle as a word in `U` (up one row), `R` (one column) and `D` (down one row), with one `R` per column at the column's height, starting and ending at height 0 ([[generalized-dyck-grammar](pages/generalized-dyck-grammar.md)]). A convex castle of height `h`, one whose skyline rises and then falls, has the word `U^h R D^h` with its other `w − 1` letters `R` placed in `2h − 1` slots: the `h − 1` slots between consecutive `U`s, the `h − 1` slots between consecutive `D`s, and the slot beside the middle `R`.[^3] Placing `w − 1` letters in `2h − 1` slots, repetition allowed, gives

```
C(2h + w − 3, w − 1)  =  [z^{w−1}] (1 − z)^{−(2h−1)}
```

convex castles of width `w` and height `h` ([[convex-castle](pages/convex-castle.md)], [[convex-castle-binomial-identity](pages/convex-castle-binomial-identity.md)]).[^4] At `w = h = 2` this is `C(3, 1) = 3`: the skylines `(1, 2)`, `(2, 1)` and `(2, 2)`.

## Three source treatments

**The symbolic method.** Flajolet and Sedgewick's Chapter I ([[analytic-combinatorics-ch1-ogfs](pages/analytic-combinatorics-ch1-ogfs.md)], [[symbolic-method](pages/symbolic-method.md)]) translates a specification of a combinatorial class directly into its ordinary generating function. Six constructions, disjoint union `+`, cartesian product `×`, sequence `SEQ`, multiset `MSET`, powerset `PSET` and cycle `CYC`, built from the neutral class `E` and an atom `Z`, each have a fixed operator on generating functions (Theorem I.1, p. 27), and the generating function of a recursively specified class is a component of a system of functional equations (Theorem I.2).[^5] The tower grammar is such a recursive specification: translating its alternatives by the sum and product rules gives Equation (2) of [[castle-counting-formula](pages/castle-counting-formula.md)], and a weight `−1` per block gives Equation (3).

**Recurrences and rational functions.** Knuth's treatment in *The Art of Computer Programming*, Vol. 1 ([[aocp-generating-functions](pages/aocp-generating-functions.md)]) supplies the Fibonacci method (posit the series, find its rational generating function, expand in partial fractions, read off a closed form) and the fact that a linear recurrence with constant coefficients has a rational generating function `N(z)/(1 − Σ c_k z^k)`. Flajolet and Sedgewick's Proposition I.2 states the related fact for regular languages: their ordinary generating functions are rational.[^6] `P_k(x)` is rational by Equation (4) of [[castle-counting-formula](pages/castle-counting-formula.md)], and partial fractions of `P_1(x)` give `P(1, L) = Re((1+i)^{L+1})` ([[signed-tower-count](pages/signed-tower-count.md)]).

**Worked examples.** [[generating-functions-topic](pages/generating-functions-topic.md)] works examples of ordinary generating functions with imaginary roots, the exponential generating function `(e^x + e^{−x})/2` that keeps the even-indexed terms, and the extraction of every fourth term, and ends with a section "Application: Project Euler 502".

## From a rational generating function to its recurrence

If `G(x) = Σ_n a_n x^n = N(x)/Q(x)` with polynomials `N` and `Q`, then `Q(x)·G(x) = N(x)`. Matching the coefficients of `x^n` on both sides, with `a_n = 0` for `n < 0` since a power series has no negative powers, gives the recurrence and its initial terms from one equation.[^7]

*Example.* For `D(x) = 1/(1 − 2x − x²) = Σ_i a_i x^i`, clear the denominator:

```
(1 − 2x − x²) · D(x)  =  1.
```

- `[x^0]`: `a_0 = 1`.
- `[x^1]`: `a_1 − 2·a_0 = 0`, so `a_1 = 2`.
- `[x^n]` for `n ≥ 2`: `a_n − 2·a_{n−1} − a_{n−2} = 0`.

With `a_{−1} = a_{−2} = 0` the three lines are one equation,

```
a_n − 2·a_{n−1} − a_{n−2}  =  [n = 0],
```

and the initial terms `a_0 = 1`, `a_1 = 2` are this equation at `n = 0` and `n = 1`.[^7] The coefficients are `1, 2, 5, 12, 29, 70, 169, …`, the Pell numbers `a_n = P⋆_{n+1}` ([[pell-numbers](pages/pell-numbers.md)]).

When `Q(0) = 1`, the coefficients of `1 − Q(x)` are the weights of the recurrence: here `Q(x) = 1 − 2x − x²` gives the weights 2 and 1. The recurrences of `P(k, ·)` come from `den_k(x)·P_k(x) = num_k(x)` in this way ([[castle-counting-formula](pages/castle-counting-formula.md)], Equation (6)), as do the recurrences found by Berlekamp-Massey on [[recurrence-discovery](pages/recurrence-discovery.md)]. [[pell-castle-strip](pages/pell-castle-strip.md)] starts from the example of this section and finds the castle strip whose generating function is `1/(1 − 2x − x²)`.

## Appearances in Sources

- [[project-euler-502-problem-setup](pages/project-euler-502-problem-setup.md)] - the generating function as a polynomial in the dimensions of the problem, proposed as the way to count castles instead of enumerating them.
- [[project-euler-502-representations](pages/project-euler-502-representations.md)] - the tower generating functions `E_k(x)` and `P_k(x)`, derived from the tower grammar.
- [[project-euler-502-castle-factoring](pages/project-euler-502-castle-factoring.md)] - the step word of a skyline used for the convex castle count.
- [[analytic-combinatorics-ch1-ogfs](pages/analytic-combinatorics-ch1-ogfs.md)] - Flajolet and Sedgewick's symbolic method: the six constructions, their operators, and rational generating functions of regular languages.
- [[aocp-generating-functions](pages/aocp-generating-functions.md)] - Knuth's Fibonacci method, rational generating functions of linear recurrences, the operations on generating functions, and the negative binomial series.
- [[generating-functions-topic](pages/generating-functions-topic.md)] - worked examples and the section "Application: Project Euler 502".
- [[pe502-pell-castle-strip](pages/pe502-pell-castle-strip.md)] - coefficient matching on `1/(1 − 2x − x²)`.

## Related Concepts

- [[symbolic-method](pages/symbolic-method.md)] - the constructions and operators of the symbolic method.
- [[castle-counting-function](pages/castle-counting-function.md)] - the counts `A`, `A^e` and `A^o` that the generating functions compute.
- [[castle-counting-formula](pages/castle-counting-formula.md)] - the derivation of `E_k(x)` and `P_k(x)` and the formula for `A^e(w, h)`.
- [[generalized-dyck-grammar](pages/generalized-dyck-grammar.md)] - the tower grammar, a recursive specification in the sense of the symbolic method.
- [[signed-tower-count](pages/signed-tower-count.md)] - the recurrences and closed forms of `P(k, ·)`.
- [[convex-castle-binomial-identity](pages/convex-castle-binomial-identity.md)] - the binomial count of convex castles.
- [[pell-castle-strip](pages/pell-castle-strip.md)] - the anchored 1-smooth strip of height 3, whose generating function is `1/(1 − 2x − x²)` with `x` marking one column after the first.
- [[pell-numbers](pages/pell-numbers.md)] - the coefficients of `1/(1 − 2x − x²)`.
- [[recurrence-discovery](pages/recurrence-discovery.md)] - the recurrences of `P(k, L)` in `L` and in `k` found by Berlekamp-Massey, of orders `k + 1` and `2L − 2`.

## Footnotes

[^1]: [[project-euler-502-problem-setup](pages/project-euler-502-problem-setup.md)] §"Generating functions" L15-16 - "come up with a multivariate polynomial whose variables are dimensions of the problem (width and height, or some other variables if they are more convenient) and whose coefficients are the solutions to our problem. This turns the problem of finding a solution for a particular problem into evaluating a particular term of the generating function (where each term is implemented using a recursive function or a similar method)."
[^2]: [[project-euler-502-representations](pages/project-euler-502-representations.md)] §"Unsigned count" L282-310 and §"Signed count" L316-340 [synthesis] - `E_k = 1/(1 − (k+1)x)` and `T(k, L) = (k+1)^L` from the grammar, and the signed generating function `P_k = (2 − P_{k−1})/(1 − 2x + x P_{k−1})`, `P_0 = 1/(1 − x)`, with its `num`/`den` update.
[^3]: [[project-euler-502-representations](pages/project-euler-502-representations.md)] §"Step 2 Enumerating Convex Castles" L169-194 - "There are H-1 possible slots between each U character, since the castle string can't start with an R. There are another H-1 possible slots between each D character, since the castle string can't end with a D. And last, there is one slot between the string of Us and string of Ds, where there is already at least one R - more Rs can be added there as well", "CCC = C(2(H-1)+W-1, W-1) = C(2H+W-3, W-1)".
[^4]: Verified by execution (Python 3.11, 2026-10-16): the number of unimodal skylines of width `w` and height `h` equals `C(2h + w − 3, w − 1)` for `w ≤ 6`, `h ≤ 5`.
[^5]: [[analytic-combinatorics-ch1-ogfs](pages/analytic-combinatorics-ch1-ogfs.md)] Theorem I.1 p.27 and Theorem I.2 pp. 33-34 - "The constructions of union, cartesian product, sequence, powerset, multiset, and cycle are all admissible ... Symbolic method, unlabelled universe. The generating function of a constructible class is a component of a system of functional equations whose terms are built from 1, z, +, ×, Q, Exp, Exp̄, Log."
[^6]: [[analytic-combinatorics-ch1-ogfs](pages/analytic-combinatorics-ch1-ogfs.md)] Proposition I.2 p.52 - "Any S-regular language has an OGF that is a rational function. This OGF is obtained from a regular specification of the language by translating each letter into the variable z, disjoint unions into sums, cartesian products into products, and sequences into quasi-inverses, (1−·)^{−1}."
[^7]: [[pe502-pell-castle-strip](pages/pe502-pell-castle-strip.md)] §"Where the recurrence comes from" L9-19 - "Matching coefficients on (1 - 2x - x^2) D(x) = 1: [x^0]: a_0 = 1; [x^1]: a_1 - 2a_0 = 0, so a_1 = 2; [x^{n+2}] for n ≥ 0: a_{n+2} - 2a_{n+1} - a_n = 0", "Uniformly: a_n - 2a_{n-1} - a_{n-2} = [n = 0] with a_{-1} = a_{-2} = 0. The base cases a_0 = 1, a_1 = 2 are the same recurrence evaluated at n = 0, 1 with those zeros substituted."
