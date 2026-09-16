---
title: Generating functions
category: Concepts
summary: A multivariate polynomial whose variables are the problem's dimensions and whose coefficients are the counts — the intended tool for computing F(w,h). Framed under the [[symbolic-method]] at the top, with recurrence-⇒-rational-GF as its most-used special case.
tags: [concept, generating-functions, combinatorics, method, symbolic-method]
sources: [project-euler-502-problem-setup, project-euler-502-representations, aocp-generating-functions, generating-functions-topic, analytic-combinatorics-part-a]
created: 2026-09-13
updated: 2026-09-15
---

# Generating functions

## Description

A **generating function** for the castle-counting problem is a multivariate polynomial (or formal power series) whose variables are the dimensions of the problem — width and height, or some other change of variables if more convenient — and whose coefficients are the counts the problem asks for.[^1] Encoding the problem this way converts "find the count for particular parameters" into "evaluate a particular term of the generating function," where each term can be computed by a recursive function or similar method.[^1]

In the context of this wiki, the generating function is the intended tool for computing the [[castle-counting-function](pages/castle-counting-function.md)] `F(w,h)` at parameter values far too large for direct enumeration of [[castle-polyomino](pages/castle-polyomino.md)] configurations.

**The concrete instance for castles.** The representations subpage supplies the actual generating functions for the castle problem, read off the [[generalized-dyck-grammar](pages/generalized-dyck-grammar.md)]: an *unsigned* tower generating function `E_k(x) = 1/(1−(k+1)x)`, giving `T(k,L) = (k+1)^L`, and a *signed* generating function `P_k` (each block/`D` weighted −1) that encodes the even-block rule via a rational-function recurrence in `x`. These combine into the [[castle-counting-formula](pages/castle-counting-formula.md)] for `F(w,h)`, where `P(k,L)` is exactly "the coefficient of `x^L` in the generating function" — the "evaluate a particular term" step, realized.

**The general framing — the [[symbolic-method](pages/symbolic-method.md)].** Above the recurrence-first apparatus below sits Flajolet & Sedgewick's specification-to-OGF dictionary ([[analytic-combinatorics-part-a](pages/analytic-combinatorics-part-a.md)], Chapter I): six admissible constructions — `+`, `×`, `SEQ`, `MSET`, `PSET`, `CYC` — each with a mechanical OGF operator, over the neutral / atomic ground classes `E` and `Z`.[^2] Describe a combinatorial class as a *specification* built from these primitives, and the OGF is a component of a system of functional equations, read off automatically.[^2] The castle's own [[generalized-dyck-grammar](pages/generalized-dyck-grammar.md)] is a recursive specification in exactly this style — a first-return decomposition of a tower — and the tower OGFs on [[project-euler-502-representations](pages/project-euler-502-representations.md)] are what the SEQ operator, plus a `(−1)`-weighting for the even-block projector, translates the grammar to.

**The method toolkit (SEQ / rational case).** [[aocp-generating-functions](pages/aocp-generating-functions.md)] (Knuth TAOCP Vol. 1) supplies the machinery for the rational-GF case: the Fibonacci method (posit the series → rational GF → partial fractions → closed form) and the key structural fact that a **linear recurrence yields a rational generating function** `poly / (1 − ∑ c_k z^k)`. Under the symbolic-method framing this is the "SEQ over a finite atomic alphabet" special case — regular languages have rational OGFs (Prop. I.2 of [[analytic-combinatorics-part-a](pages/analytic-combinatorics-part-a.md)]).[^3] That is exactly why the castle's `P_k = num_k/den_k` is rational, why partial fractions give the `Re((1+i)^{L+1})`-style closed forms, and why the negative binomial `1/(1−z)^{n+1} = ∑ C(n+k,n) z^k` shows up as the tower and any-parity counts.

The three source treatments are complementary: [[analytic-combinatorics-part-a](pages/analytic-combinatorics-part-a.md)] (Flajolet–Sedgewick, the general symbolic-method framework), [[aocp-generating-functions](pages/aocp-generating-functions.md)] (Knuth, the Fibonacci-method / rational-GF flavor), and [[generating-functions-topic](pages/generating-functions-topic.md)] (Sedgewick–Flajolet / Trotter, the intuition-and-examples one with an explicit "Application: PE 502" section). The last two work at the level of *"you have a recurrence, here is the OGF"*; the first works at the level of *"you have a specification, here is the OGF."*

## Appearances in Sources

- [[project-euler-502-problem-setup](pages/project-euler-502-problem-setup.md)] — describes the generating-function approach in the abstract and names it the intended method for the count.
- [[project-euler-502-representations](pages/project-euler-502-representations.md)] — gives the concrete unsigned and signed generating functions for castles, derived from the Dyck grammar.
- [[analytic-combinatorics-part-a](pages/analytic-combinatorics-part-a.md)] — Flajolet–Sedgewick's symbolic-method framework: the general specification-to-OGF dictionary above the recurrence-first apparatus of the other two sources.
- [[aocp-generating-functions](pages/aocp-generating-functions.md)] — Knuth's general toolkit: recurrence ⇒ rational GF, partial fractions, convolution, the negative binomial.
- [[generating-functions-topic](pages/generating-functions-topic.md)] — the Sedgewick–Flajolet/Trotter reference, with the imaginary-roots / EGF-parity / every-4th-term examples and an explicit PE 502 section.

## Related Concepts

- [[symbolic-method](pages/symbolic-method.md)] — the general framework the recurrence apparatus is a special case of.
- [[castle-counting-function](pages/castle-counting-function.md)] — the count `F(w,h)` that a generating function is meant to produce.
- [[castle-counting-formula](pages/castle-counting-formula.md)] — the closed form these generating functions yield.
- [[generalized-dyck-grammar](pages/generalized-dyck-grammar.md)] — the grammar the castle generating functions are read off; a recursive specification in the symbolic-method style.
- [[aocp-generating-functions](pages/aocp-generating-functions.md)] — the general generating-function method (Fibonacci example, linear-recurrence ⇒ rational GF).
- [[castle-polyomino](pages/castle-polyomino.md)] — the object whose configurations are being counted.

## Footnotes

[^1]: [[project-euler-502-problem-setup](pages/project-euler-502-problem-setup.md)] §"Generating functions" L17-20 — "come up with a multivariate polynomial whose variables are dimensions of the problem (width and height, or some other variables if they are more convenient) and whose coefficients are the solutions to our problem. This turns the problem of finding a solution for a particular problem into evaluating a particular term of the generating function (where each term is implemented using a recursive function or a similar method)."
[^2]: [[analytic-combinatorics-part-a](pages/analytic-combinatorics-part-a.md)] Theorem I.1 p.27 and Theorem I.2 pp. 33-34 — "The constructions of union, cartesian product, sequence, powerset, multiset, and cycle are all admissible ... Symbolic method, unlabelled universe. The generating function of a constructible class is a component of a system of functional equations whose terms are built from 1, z, +, ×, Q, Exp, Exp̄, Log."
[^3]: [[analytic-combinatorics-part-a](pages/analytic-combinatorics-part-a.md)] Proposition I.2 p.52 — "Any S-regular language has an OGF that is a rational function. This OGF is obtained from a regular specification of the language by translating each letter into the variable z, disjoint unions into sums, cartesian products into products, and sequences into quasi-inverses, (1−·)^{−1}."
