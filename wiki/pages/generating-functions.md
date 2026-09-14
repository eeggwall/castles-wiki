---
title: Generating functions
category: Concepts
summary: A multivariate polynomial whose variables are the problem's dimensions and whose coefficients are the counts — the intended tool for computing F(w,h).
tags: [concept, generating-functions, combinatorics, method]
sources: [project-euler-502-problem-setup]
created: 2026-09-13
updated: 2026-09-13
---

# Generating functions

## Description

A **generating function** for the castle-counting problem is a multivariate polynomial (or formal power series) whose variables are the dimensions of the problem — width and height, or some other change of variables if more convenient — and whose coefficients are the counts the problem asks for.[^1] Encoding the problem this way converts "find the count for particular parameters" into "evaluate a particular term of the generating function," where each term can be computed by a recursive function or similar method.[^1]

In the context of this wiki, the generating function is the intended tool for computing the [[castle-counting-function](pages/castle-counting-function.md)] `F(w,h)` at parameter values far too large for direct enumeration of [[castle-polyomino](pages/castle-polyomino.md)] configurations.

This page currently reflects only the setup-stage description of the method. The charlesreid1.com wiki has a dedicated *Generating Functions* page (not yet ingested here) that the source credits with substantial development during the problem's study; the concrete generating function actually used, and its derivation, belong to the Solution subpage. Both are on the ingestion queue, and this page will be enriched from them.

## Appearances in Sources

- [[project-euler-502-problem-setup](pages/project-euler-502-problem-setup.md)] — describes the generating-function approach in the abstract and names it the intended method for the count.

## Related Concepts

- [[castle-counting-function](pages/castle-counting-function.md)] — the count `F(w,h)` that a generating function is meant to produce.
- [[castle-polyomino](pages/castle-polyomino.md)] — the object whose configurations are being counted.

## Footnotes

[^1]: [[project-euler-502-problem-setup](pages/project-euler-502-problem-setup.md)] §"Generating functions" L17-20 — "come up with a multivariate polynomial whose variables are dimensions of the problem (width and height, or some other variables if they are more convenient) and whose coefficients are the solutions to our problem. This turns the problem of finding a solution for a particular problem into evaluating a particular term of the generating function (where each term is implemented using a recursive function or a similar method)."
