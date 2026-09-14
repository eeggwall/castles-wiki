---
title: Generating functions
category: Concepts
summary: A multivariate polynomial whose variables are the problem's dimensions and whose coefficients are the counts — the intended tool for computing F(w,h).
tags: [concept, generating-functions, combinatorics, method]
sources: [project-euler-502-problem-setup, project-euler-502-representations]
created: 2026-09-13
updated: 2026-09-13
---

# Generating functions

## Description

A **generating function** for the castle-counting problem is a multivariate polynomial (or formal power series) whose variables are the dimensions of the problem — width and height, or some other change of variables if more convenient — and whose coefficients are the counts the problem asks for.[^1] Encoding the problem this way converts "find the count for particular parameters" into "evaluate a particular term of the generating function," where each term can be computed by a recursive function or similar method.[^1]

In the context of this wiki, the generating function is the intended tool for computing the [[castle-counting-function](pages/castle-counting-function.md)] `F(w,h)` at parameter values far too large for direct enumeration of [[castle-polyomino](pages/castle-polyomino.md)] configurations.

**The concrete instance for castles.** The representations subpage supplies the actual generating functions for the castle problem, read off the [[generalized-dyck-grammar](pages/generalized-dyck-grammar.md)]: an *unsigned* tower generating function `E_k(x) = 1/(1−(k+1)x)`, giving `T(k,L) = (k+1)^L`, and a *signed* generating function `P_k` (each block/`D` weighted −1) that encodes the even-block rule via a rational-function recurrence in `x`. These combine into the [[castle-counting-formula](pages/castle-counting-formula.md)] for `F(w,h)`, where `P(k,L)` is exactly "the coefficient of `x^L` in the generating function" — the "evaluate a particular term" step, realized.

The charlesreid1.com wiki also has a dedicated *Generating Functions* page (not yet ingested here) that the source credits with substantial development during the problem's study; this page will be further enriched when it is ingested.

## Appearances in Sources

- [[project-euler-502-problem-setup](pages/project-euler-502-problem-setup.md)] — describes the generating-function approach in the abstract and names it the intended method for the count.
- [[project-euler-502-representations](pages/project-euler-502-representations.md)] — gives the concrete unsigned and signed generating functions for castles, derived from the Dyck grammar.

## Related Concepts

- [[castle-counting-function](pages/castle-counting-function.md)] — the count `F(w,h)` that a generating function is meant to produce.
- [[castle-counting-formula](pages/castle-counting-formula.md)] — the closed form these generating functions yield.
- [[generalized-dyck-grammar](pages/generalized-dyck-grammar.md)] — the grammar the castle generating functions are read off.
- [[castle-polyomino](pages/castle-polyomino.md)] — the object whose configurations are being counted.

## Footnotes

[^1]: [[project-euler-502-problem-setup](pages/project-euler-502-problem-setup.md)] §"Generating functions" L17-20 — "come up with a multivariate polynomial whose variables are dimensions of the problem (width and height, or some other variables if they are more convenient) and whose coefficients are the solutions to our problem. This turns the problem of finding a solution for a particular problem into evaluating a particular term of the generating function (where each term is implemented using a recursive function or a similar method)."
