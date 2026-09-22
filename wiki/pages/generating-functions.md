---
title: Generating functions
category: Concepts
summary: A multivariate polynomial whose variables are the problem's dimensions and coefficients are the counts - the intended tool for computing F(w,h); framed under the symbolic method, with linear-recurrence-to-rational-GF as its most-used case.
tags: [concept, generating-functions, combinatorics, method, symbolic-method]
sources: [project-euler-502-problem-setup, project-euler-502-representations, aocp-generating-functions, generating-functions-topic, analytic-combinatorics-part-a, pe502-pell-castle-strip]
created: 2026-09-13
updated: 2026-09-19
---

# Generating functions

## Description

A **generating function** (GF) for the castle-counting problem is a multivariate polynomial (or formal power series) whose variables are the dimensions of the problem - width and height, or some other change of variables if more convenient - and whose coefficients are the counts the problem asks for.[^1] Encoding the problem this way converts "find the count for particular parameters" into "evaluate a particular term of the generating function," where each term can be computed by a recursive function or similar method.[^1]

In the context of this wiki, the generating function is the intended tool for computing the [[castle-counting-function](pages/castle-counting-function.md)] `F(w,h)` at parameter values far too large for direct enumeration of [[castle-polyomino](pages/castle-polyomino.md)] configurations.

## The concrete instance for castles

The representations subpage supplies the actual generating functions for the castle problem, read off the [[generalized-dyck-grammar](pages/generalized-dyck-grammar.md)]: an *unsigned* tower generating function `E_k(x) = 1/(1−(k+1)x)`, giving `T(k,L) = (k+1)^L`, and a *signed* generating function `P_k` (each block/`D` weighted −1) that encodes the even-block rule via a rational-function recurrence in `x`. These combine into the [[castle-counting-formula](pages/castle-counting-formula.md)] for `F(w,h)`, where `P(k,L)` is exactly "the coefficient of `x^L` in the generating function" - the "evaluate a particular term" step, realized.

The **negative binomial** `1/(1−z)^{n+1} = ∑_k C(n+k, n) z^k` also appears, but not in `(k+1)^L` (unsigned tower) or `h^w − (h−1)^w` (any-parity) - both of those are pure exponentials in width. It appears in the **[[convex-castle](pages/convex-castle.md)] count** `C(2h+w−3, w−1) = [z^{w−1}] (1−z)^{−(2h−1)}`: with `2h−1` up steps and `2h−1` down steps interleaving the `w−1` extra `R`s, the negative-binomial expansion is exactly the stars-and-bars generating function for the front and back halves of a convex castle ([[convex-castle-binomial-identity](pages/convex-castle-binomial-identity.md)]).

## Three source treatments

The wiki has ingested three complementary references, each attacking generating functions from a different level.

**The general framing - the [[symbolic-method](pages/symbolic-method.md)].** Flajolet & Sedgewick's specification-to-ordinary generating function (OGF) dictionary ([[analytic-combinatorics-part-a](pages/analytic-combinatorics-part-a.md)], Chapter I) sits above the recurrence-first apparatus below: six admissible constructions - `+`, `×`, `SEQ`, `MSET`, `PSET`, `CYC` - each with a mechanical OGF operator, over the neutral / atomic ground classes `E` and `Z`.[^2] Describe a combinatorial class as a *specification* built from these primitives, and the OGF is a component of a system of functional equations, read off automatically.[^2] The castle's own [[generalized-dyck-grammar](pages/generalized-dyck-grammar.md)] is a recursive specification in exactly this style - a first-return decomposition of a tower - and the tower OGFs on [[project-euler-502-representations](pages/project-euler-502-representations.md)] are what the SEQ operator, plus a `(−1)`-weighting for the even-block projector, translates the grammar to.

**The method toolkit - the rational / SEQ case.** [[aocp-generating-functions](pages/aocp-generating-functions.md)] (Knuth's *The Art of Computer Programming* (TAOCP) Vol. 1) supplies the machinery for the rational-GF case: the Fibonacci method (posit the series → rational GF → partial fractions → closed form) and the key structural fact that a **linear recurrence yields a rational generating function** `poly / (1 − ∑ c_k z^k)`. Under the symbolic-method framing this is the "SEQ over a finite atomic alphabet" special case - regular languages have rational OGFs (Prop. I.2 of [[analytic-combinatorics-part-a](pages/analytic-combinatorics-part-a.md)]).[^3] This is exactly why the castle's `P_k = num_k/den_k` is rational and why partial fractions give the `Re((1+i)^{L+1})`-style closed forms.

**The intuition-and-examples one.** [[generating-functions-topic](pages/generating-functions-topic.md)] (Sedgewick–Flajolet / Trotter) is the reference to reach for when the reader wants worked examples rather than a framework - imaginary-roots CF expansions, exponential generating function (EGF) parity projectors, every-4th-term OGFs - together with an explicit "Application: Project Euler 502 (PE 502)" section.

The last two work at the level of *"you have a recurrence, here is the OGF"*; the first works at the level of *"you have a specification, here is the OGF."*

## GF → recurrence: the coefficient-matching mechanic

The everyday operation the castle-counting apparatus depends on — read a linear recurrence off a rational generating function — is a **five-line mechanical procedure** that doesn't need "base cases" as a separate argument. If `G(x) = ∑ a_n x^n = N(x)/D(x)`, clear the denominator to get `D(x)·G(x) = N(x)`, then match coefficients of `x^n` on both sides. Every `a_i` with negative index is `0` by convention (a power series has no negative powers), so the recurrence *and* the boundary conditions come out of the same equation, evaluated at successive `n`.[^4]

**Worked example** — the [[pell-castle-strip](pages/pell-castle-strip.md)] exercise. For `D(x) = 1/(1 − 2x − x²) = ∑ a_i x^i`, clear the denominator:

```
(1 − 2x − x²) · D(x) = 1.
```

- `[x^0]`: `a_0 = 1`.
- `[x^1]`: `a_1 − 2·a_0 = 0`, so `a_1 = 2`.
- `[x^{n}]` for `n ≥ 2`: `a_n − 2·a_{n−1} − a_{n−2} = 0`.

Uniformly (with `a_{−1} = a_{−2} = 0`):

```
a_n − 2·a_{n−1} − a_{n−2}  =  [n = 0].
```

The "base cases" `a_0 = 1, a_1 = 2` are this recurrence evaluated at `n = 0, 1` with the negative-index zeros substituted. No separate argument.[^4]

**Why this matters.** Every rational generating function in the castle machinery — `E_k = 1/(1 − (k+1)x)`, `P_k = num_k/den_k`, the C-finite recurrences on [[recurrence-discovery](pages/recurrence-discovery.md)] — is reached the same way. Coefficient matching is the shortcut that makes "read the recurrence off the denominator" fully mechanical: the coefficients of `−D(x)` (excluding the constant `1`) are the recurrence weights. This is also the opening mechanic of the [[pell-castle-strip](pages/pell-castle-strip.md)] seminar arc, where a textbook end-of-chapter exercise on this technique leads to a castle strip (the 1-smooth height-3 strip anchored at the base) whose width generating function is exactly `1/(1 − 2x − x²)`.

## Appearances in Sources

- [[project-euler-502-problem-setup](pages/project-euler-502-problem-setup.md)] — describes the generating-function approach in the abstract and names it the intended method for the count.
- [[project-euler-502-representations](pages/project-euler-502-representations.md)] — gives the concrete unsigned and signed generating functions for castles, derived from the Dyck grammar.
- [[analytic-combinatorics-part-a](pages/analytic-combinatorics-part-a.md)] — Flajolet–Sedgewick's symbolic-method framework: the general specification-to-OGF dictionary above the recurrence-first apparatus of the other two sources.
- [[aocp-generating-functions](pages/aocp-generating-functions.md)] — Knuth's general toolkit: recurrence ⇒ rational GF, partial fractions, convolution, the negative binomial.
- [[generating-functions-topic](pages/generating-functions-topic.md)] — the Sedgewick–Flajolet/Trotter reference, with the imaginary-roots / exponential generating function (EGF)-parity / every-4th-term examples and an explicit PE 502 section.
- [[pe502-pell-castle-strip](pages/pe502-pell-castle-strip.md)] — worked coefficient-matching example (the Pell strip mnemonic).

## Related Concepts

- [[symbolic-method](pages/symbolic-method.md)] — the general framework the recurrence apparatus is a special case of.
- [[castle-counting-function](pages/castle-counting-function.md)] — the count `F(w,h)` that a generating function is meant to produce.
- [[castle-counting-formula](pages/castle-counting-formula.md)] — the closed form these generating functions yield.
- [[generalized-dyck-grammar](pages/generalized-dyck-grammar.md)] — the grammar the castle generating functions are read off; a recursive specification in the symbolic-method style.
- [[aocp-generating-functions](pages/aocp-generating-functions.md)] — the general generating-function method (Fibonacci example, linear-recurrence ⇒ rational GF).
- [[castle-polyomino](pages/castle-polyomino.md)] — the object whose configurations are being counted.
- [[pell-castle-strip](pages/pell-castle-strip.md)] — the seminar-shaped worked example of "coefficient matching → two-atom tiling → the castle strip that realizes it → silver-ratio thread."
- [[pell-numbers](pages/pell-numbers.md)] — the integer sequence that mnemonic produces.
- [[recurrence-discovery](pages/recurrence-discovery.md)] — the empirical companion: Berlekamp-Massey run in both directions of `P(k,L)`, pinning k-direction order to `2L−2`.

## Footnotes

[^1]: [[project-euler-502-problem-setup](pages/project-euler-502-problem-setup.md)] §"Generating functions" L17-20 — "come up with a multivariate polynomial whose variables are dimensions of the problem (width and height, or some other variables if they are more convenient) and whose coefficients are the solutions to our problem. This turns the problem of finding a solution for a particular problem into evaluating a particular term of the generating function (where each term is implemented using a recursive function or a similar method)."
[^2]: [[analytic-combinatorics-part-a](pages/analytic-combinatorics-part-a.md)] Theorem I.1 p.27 and Theorem I.2 pp. 33-34 — "The constructions of union, cartesian product, sequence, powerset, multiset, and cycle are all admissible ... Symbolic method, unlabelled universe. The generating function of a constructible class is a component of a system of functional equations whose terms are built from 1, z, +, ×, Q, Exp, Exp̄, Log."
[^3]: [[analytic-combinatorics-part-a](pages/analytic-combinatorics-part-a.md)] Proposition I.2 p.52 — "Any S-regular language has an OGF that is a rational function. This OGF is obtained from a regular specification of the language by translating each letter into the variable z, disjoint unions into sums, cartesian products into products, and sequences into quasi-inverses, (1−·)^{−1}."
[^4]: [[pe502-pell-castle-strip](pages/pe502-pell-castle-strip.md)] §"Where the recurrence comes from" L9-L19 — the coefficient-matching mechanic worked on `D(x) = 1/(1 − 2x − x²)`: "Matching coefficients on (1 − 2x − x²) D(x) = 1: [x^0]: a_0 = 1; [x^1]: a_1 − 2a_0 = 0, so a_1 = 2; [x^{n+2}] for n ≥ 0: a_{n+2} − 2a_{n+1} − a_n = 0. ... Uniformly: a_n − 2a_{n−1} − a_{n−2} = [n = 0] with a_{−1} = a_{−2} = 0. The base cases a_0 = 1, a_1 = 2 are the same recurrence evaluated at n = 0, 1 with those zeros substituted. Nothing special about them." Recurrence and coefficient sequence `1, 2, 5, 12, 29, 70, 169, …` re-verified during ingest.
