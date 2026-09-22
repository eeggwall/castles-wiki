---
title: "Generating Functions (Sedgewick–Flajolet / Trotter)"
category: Sources
summary: A generating-function reference — OGF operations, recurrence→rational-GF worked examples (imaginary roots, difference-of-powers), the EGF parity trick, and an explicit "Application: Project Euler 502". Companion to [[analytic-combinatorics-ch1-ogfs]] (the definitive treatment) and [[aocp-generating-functions]] (Knuth Fibonacci-method).
tags: [generating-functions, ogf, egf, recurrence, parity, partial-fractions, source]
sources: [generating-functions-topic]
created: 2026-09-14
updated: 2026-09-19
---

# Generating Functions (Sedgewick–Flajolet / Trotter)

**Source:** https://charlesreid1.com/wiki/Generating_Functions
**Date ingested:** 2026-09-14
**Type:** article (MediaWiki topic page; the intuition-and-examples companion to [[aocp-generating-functions](pages/aocp-generating-functions.md)])

## Summary

The broad generating-function reference, drawing on Sedgewick–Flajolet's *Analysis of Algorithms* and Trotter's Chapter 8. It develops the **ordinary GF** operation toolkit — addition, differentiation/integration, the partial-sum operator `(1/(1−z))G(z)`, and multiplication as **convolution** — and the binomial-derivative ladder `1/(1−z)^{m+1} = ∑_{k} C(k+m,m) z^k`.[^1] It then works recurrence-to-closed-form examples, introduces **exponential generating functions** for order-sensitive counting, and — notably — ends with an explicit **"Application: Project Euler 502"** section.[^2]

Several of its worked examples are, in the general setting, exactly the machinery the castle solution uses (all re-verified during ingest):

- **Recurrence ⇒ rational GF, difference of powers.** `a_n = 5a_{n−1} − 6a_{n−2} → z/(1−5z+6z²) → 3^n − 2^n`[^3] — the shape of the castle's any-parity count `A(w,h) = h^w − (h−1)^w` (the difference-of-powers family, [[castle-counting-function](pages/castle-counting-function.md)]).
- **Imaginary roots.** `a_n = … → 1/(1+z²) → ½(iⁿ + (−i)ⁿ) = 1,0,−1,0,…`[^4] — the identical mechanism to the castle's `P(1,L) = Re((1+i)^{L+1})` (roots `±i`/`1±i`); see [[signed-tower-count](pages/signed-tower-count.md)].
- **EGF parity projector.** Counting length-*n* ternary strings with an **even number of 0s** uses `E_0 = (e^x + e^{−x})/2` to cancel the odd terms, giving `(e^{3x}+e^x)/2` and the count `(3^n + 1)/2`.[^5] This is the classical form of the **`(A ± P)/2` even/odd trick** the castle uses for even-block counting (see [[castle-sign](pages/castle-sign.md)]). *(The source's final line drops the `/2`; the correct count is `(3^n+1)/2`, verified.)*
- **"Every 4th term" via partial fractions.** `1/(1−x^4) = ∑ x^{4k}`, extracted by the `1 + (−1)^k + (iᵏ+(−i)ᵏ)` residues[^6] — the same residue-filtering that makes the height-2 castle counts "sum every 4th binomial" (the [[hyperbolic-sequence-family](pages/hyperbolic-sequence-family.md)]).
- **Triangular via `z/(1−z)³`.** The marbles example lands on `∑ C(n+1,2) x^n = 1,3,6,10,…`[^7] — the same binomial the convex height-2 castle count `C(w+1,2)` is ([[convex-castle-binomial-identity](pages/convex-castle-binomial-identity.md)]).

## The explicit PE 502 application

The page's own closing section states the castle payoff directly: the `P(k,L)` recursion of [[project-euler-502-solution](pages/project-euler-502-solution.md)] **lifts to a rational generating function** `F_k(x) = num_k(x)/den_k(x)` with level-by-level updates, and coefficient extraction becomes a linear recurrence with characteristic polynomial `den_k(x)` (reversed) — "exactly the setup where [[kitamasa](pages/kitamasa.md)]'s method applies." It frames the castle as the concrete pay-off of the Sedgewick/Trotter theory: a rational GF solving a hard combinatorial problem in code.[^8]

## Key Takeaways

- ordinary generating function (OGF) toolkit: add, differentiate/integrate, partial-sum `(1/(1−z))G`, convolution; the ladder `1/(1−z)^{m+1} = ∑ C(k+m,m) z^k`.[^1]
- **Recurrence ⇒ rational GF** worked both ways, including the **imaginary-roots** case `1/(1+z²) → ½(iⁿ+(−i)ⁿ)` — the `Re((1+i)^{L+1})` mechanism.[^4]
- **EGF parity projector** `(e^x+e^{−x})/2` counts even-0 ternary strings as `(3^n+1)/2` — the classical `(A±P)/2` even/odd trick.[^5]
- Explicit **Application: PE 502** — `P(k,L)` → rational GF → Kitamasa.[^8]

## Entities & Concepts

- [[generating-functions](pages/generating-functions.md)] — the concept page; this and [[aocp-generating-functions](pages/aocp-generating-functions.md)] are its two source treatments.
- [[signed-tower-count](pages/signed-tower-count.md)] — the imaginary-roots `Re((1+i)^{L+1})` closed form in action.
- [[castle-sign](pages/castle-sign.md)] — the `(A±P)/2` parity projector, here as the EGF even-0s trick.
- [[parity-via-roots-of-unity](pages/parity-via-roots-of-unity.md)] — the `(T±P)/2` trick generalized to block count mod m; this page's EGF projector is its index-side `m=2` twin.
- [[hyperbolic-sequence-family](pages/hyperbolic-sequence-family.md)] — "sum every 4th binomial" via the `1/(1−x^4)` residue mechanism.
- [[castle-counting-formula](pages/castle-counting-formula.md)] / [[kitamasa](pages/kitamasa.md)] — the `P_k = num_k/den_k` → linear-recurrence extraction the PE 502 section names.

Linked from the source: [[aocp-generating-functions](pages/aocp-generating-functions.md)] (ingested).
- [[block-count-constraints](pages/block-count-constraints.md)] — the residue / sparse / semigroup trichotomy on the block count; this page's `1/(1−x⁴)` and EGF projector are its index-side twins.

## Relation to Other Wiki Pages

The intuition-and-worked-examples companion to the AOCP treatment, and the page that makes the general theory's castle relevance explicit. Its examples are not analogies but the *same operations* the castle solution performs — recurrence-to-rational-GF, imaginary-root closed forms, the parity projector, and residue-filtered "every kth term" — with its own section pointing straight at the `P(k,L)` → Kitamasa pipeline.

**One of three GF source treatments in the wiki**, all complementary:

- [[analytic-combinatorics-ch1-ogfs](pages/analytic-combinatorics-ch1-ogfs.md)] — the definitive treatment (Flajolet & Sedgewick 2009); the *symbolic method* dictionary that recasts recurrence-⇒-rational-GF as the sequence (SEQ) / regular-language special case of a more general specification-to-OGF framework.
- [[aocp-generating-functions](pages/aocp-generating-functions.md)] — Knuth The Art of Computer Programming (TAOCP) Vol. 1; the Fibonacci-method and the recurrence-⇒-rational-GF core.
- This page — worked examples that hit *exactly* the castle's operations, with the explicit PE 502 application.

## Footnotes

[^1]: [[generating-functions-topic](pages/generating-functions-topic.md)] §"Ordinary Generating Functions"–"Multiplication" L7-39 — the OGF operations, the derivative ladder "z^m/(1-z)^{m+1} = sum C(k,m) z^k ... 1/(1-z)^{m+1} = sum C(k+m,m) z^k", the partial-sum "(1/(1-z)) G(z)", and convolution.
[^2]: [[generating-functions-topic](pages/generating-functions-topic.md)] §"Exponential Generating Functions" L95-107, §"Application: Project Euler 502" L121-126 — EGFs "when order matters" and the closing PE 502 application.
[^3]: [[generating-functions-topic](pages/generating-functions-topic.md)] §"Example: Two-Term Recurrence" L43-47 — "a_n = 5 a_{n-1} - 6 a_{n-2} ... G(z) = z/(1 - 5z + 6z^2) ... = 1/(1-3z) - 1/(1-2z), giving a_n = 3^n - 2^n"; coefficients re-verified during ingest (0,1,5,19,65,211,665).
[^4]: [[generating-functions-topic](pages/generating-functions-topic.md)] §"Example: Imaginary Roots" L55-60 — "G(z) = 1/(1 + z^2) ... = (1/2)(1/(1-iz) + 1/(1+iz)) ... a_n = (1/2)(i^n + (-i)^n) ... -> 1, 0, -1, 0, 1, 0, -1, 0, 1"; re-verified during ingest.
[^5]: [[generating-functions-topic](pages/generating-functions-topic.md)] §"EXAMPLE Counting Ternary Strings" L99-107 — "even number of 0s ... E_0(x) = (e^x + e^{-x})/2 ... E(x) = (e^{3x} + e^x)/2 = (1/2) sum (3^n + 1) x^n/n!"; count (3^n+1)/2 re-verified during ingest (1,2,5,14,41,122). The source's final "3^n + 1" omits the 1/2.
[^6]: [[generating-functions-topic](pages/generating-functions-topic.md)] §"Problem 3 / Part b" L115-118 — "1/(1-x^4) = (1-x)(1+x)(1+x^2) ... 1 + (-1)^k + ((-i)^k + i^k) ... leaves only k divisible by 4: G(x) = sum x^{4k}"; 1/(1-x^4) coefficients re-verified during ingest.
[^7]: [[generating-functions-topic](pages/generating-functions-topic.md)] §"Colored Marbles"/"Analysis"/"Taylor Series" L78-90 — "G(z) = z/(1-z)^3 ... = sum_{n>=1} C(n+1,2) x^n ... z + 3z^2 + 6z^3 + 10z^4 + ..."; z/(1-z)^3 = C(n+1,2) re-verified during ingest.
[^8]: [[generating-functions-topic](pages/generating-functions-topic.md)] §"Application: Project Euler 502" L121-126 — "The P(k, L) recursion ... lifts to a rational generating function F_k(x) = num_k(x)/den_k(x) with level-by-level update rules. Coefficient extraction reduces to a linear recurrence with characteristic polynomial den_k(x) (reversed), which is exactly the setup where Kitamasa's method applies."
