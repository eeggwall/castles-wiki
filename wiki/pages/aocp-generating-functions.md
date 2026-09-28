---
title: "AOCP Generating Functions (Knuth TAOCP Vol. 1)"
category: Sources
summary: Knuth's generating-function toolkit — the Fibonacci method (guess series → rational GF → partial fractions → closed form), linear-recurrence ⇒ polynomial/(1−Σc_k z^k), the operation algebra, and the negative-binomial 1/(1−z)^{n+1}.
tags: [knuth, taocp, generating-functions, c-finite, rational, partial-fractions, source]
sources: [aocp-generating-functions]
created: 2026-09-13
updated: 2026-09-28
---

# The Art of Computer Programming (AOCP) Generating Functions (Knuth The Art of Computer Programming (TAOCP) Vol. 1)

**Source:** https://charlesreid1.com/wiki/AOCP/Generating_Functions (notes on Knuth, *The Art of Computer Programming*, Vol. 1, §1.2.9)
**Date ingested:** 2026-09-13
**Type:** article (MediaWiki notes page)

## Summary

Knuth's treatment of generating functions (complementing the concept page [[generating-functions](pages/generating-functions.md)]). Its main worked example is the **Fibonacci example**: posit the series `G(z) = ∑ F_n z^n`, multiply by `z` and `z²`, and the recurrence collapses the sum to a **rational function** `G(z) = z/(1 − z − z²)`; the roots of the denominator (here `φ, φ̂`) give, via **partial fractions**, the closed form `F_n = (φ^n − φ̂^n)/√5`.[^1] Verified during ingest (the GF's coefficients reproduce `0,1,1,2,3,5,8,13,21`).

Generalized: **a linear recurrence yields a rational generating function**:[^2]

```
a_n = c_1 a_{n−1} + … + c_m a_{n−m}   ⟹   G(z) = polynomial / (1 − c_1 z − … − c_m z^m)
```

The page then works the operation algebra: **addition** (superpose sequences), **shifting** (`×z^k` shifts coefficients), **multiplication** (coefficient **convolution** `s_n = ∑_k a_k b_{n−k}`), the partial-sum operator (`G(z)/(1−z)` sums the sequence), **exponential** generating functions for binomial-convolution recurrences (`c_n = ∑_k C(n,k) a_k b_{n−k}`), and calculus on GFs.[^3] It lists the standard known GFs — the binomial theorem `(1+z)^r = ∑ C(r,k) z^k` with its negative-integer special case, the exponential and logarithm series:[^4]

```
1/(1−z)^{n+1} = ∑_{k≥0} C(n+k, n) z^k      (the negative binomial)
```

A worked exercise finds the GF of `⟨2^n + 3^n⟩ = 2,5,13,35,…` as `1/(1−2z) + 1/(1−3z) = (2−5z)/(1−5z+6z²)`, extracting `2^n+3^n` as the *n*th coefficient — verified during ingest.[^5]

## Relevance to the castle

The castle solution uses these tools:

- **Linear recurrence ⇒ rational GF** is the castle's [[castle-counting-formula](pages/castle-counting-formula.md)]: the signed tower count is `P_k = num_k/den_k`, a rational function whose denominator is the characteristic polynomial of an order-`(k+1)` linear recurrence ([[signed-tower-count](pages/signed-tower-count.md)]). The C-finiteness that [[kitamasa](pages/kitamasa.md)] and [[berlekamp-massey](pages/berlekamp-massey.md)] exploit is this "recurrence ⇔ rational GF" equivalence.
- **The Fibonacci partial-fractions → roots → closed form** procedure that gives `F_n = (φ^n − φ̂^n)/√5` also turns `P(1,L)`'s recurrence (roots `1±i`) into `Re((1+i)^{L+1})` (see [[signed-tower-count](pages/signed-tower-count.md)]).
- **The negative binomial `1/(1−z)^{n+1} = ∑ C(n+k,n) z^k`** is the denominator shape of the [[tower-narayana-polynomial](pages/tower-narayana-polynomial.md)] block-count GF, a Narayana polynomial over `(1−x)^w`, and gives the [[convex-castle](pages/convex-castle.md)] count `C(2h+w−3, w−1) = [z^{w−1}](1−z)^{−(2h−1)}`. The unsigned tower GF `E_k = 1/(1−(k+1)x)` is geometric.
- **The `⟨2^n+3^n⟩` exercise** has the structure of the castle's any-parity count `A(w,h) = h^w − (h−1)^w` (the difference-of-powers family `A000225`, `A001047`, …): a combination of two geometric GFs `1/(1−az)`.

## Key Takeaways

- **Fibonacci method:** posit the series, use the recurrence to get a rational GF, partial-fraction by the denominator roots, read off the closed form (`F_n = (φ^n−φ̂^n)/√5`).[^1]
- **Linear recurrence ⇒ `G(z) = poly / (1 − ∑ c_k z^k)`** — the castle's `P_k = num_k/den_k` is an instance.[^2]
- Operation algebra: add / shift / convolve (multiply) / partial-sum (`/(1−z)`) / exponential generating function (EGF) for binomial convolutions / differentiate-integrate.[^3]
- Negative binomial `1/(1−z)^{n+1} = ∑ C(n+k,n) z^k` — the Narayana-denominator and convex-castle structure; `⟨2^n+3^n⟩ → 1/(1−2z)+1/(1−3z)` has the shape of the castle's any-parity count.[^4][^5]

## Entities & Concepts

- [[generating-functions](pages/generating-functions.md)] — the concept page this source grounds.
- [[castle-counting-formula](pages/castle-counting-formula.md)] / [[signed-tower-count](pages/signed-tower-count.md)] — the castle's rational GFs and partial-fraction closed forms.
- [[tower-narayana-polynomial](pages/tower-narayana-polynomial.md)] — the negative-binomial / `(1−x)^w` denominator in action.
- [[new-sequence-fw3](pages/new-sequence-fw3.md)] — `F(w,3)`, with `F(w,3) + odd(w,3) = 3^w − 2^w = A001047`, this page's difference-of-powers family.
- [[kitamasa](pages/kitamasa.md)] / [[berlekamp-massey](pages/berlekamp-massey.md)] — tools that exploit the recurrence ⇔ rational-GF equivalence.

Linked from the source: Analytic Combinatorics ([[analytic-combinatorics-ch1-ogfs](pages/analytic-combinatorics-ch1-ogfs.md)], Chapter I).
- [[aocp-binomial-coefficients](pages/aocp-binomial-coefficients.md)] — the sibling Knuth page: the negative binomial `1/(1−z)^{n+1}` via negating the upper index, and the `2^n` / alternating-sum identities.
- [[recurrence-discovery](pages/recurrence-discovery.md)] — the empirical confirmation of "linear recurrence ⇒ rational GF" run in both directions on the castle's `P(k,L)` array.

## Relation to Other Wiki Pages

The rational generating functions and closed forms of the castle solution use the techniques here. The page shows why the castle's counts are C-finite (linear recurrence ⇔ rational GF), why partial fractions produce the `Re((1+i)^{L+1})`-style closed forms, why the Narayana block-count GF has a negative-binomial denominator, and why the any-parity count is a difference of geometric series.

## Footnotes

[^1]: [[aocp-generating-functions](pages/aocp-generating-functions.md)] §"Knuth's Fibonacci Example"/"Partial Fraction Expansion"/"Closed Form" L14-92 — "G(z) = F_0 + F_1 z + ... multiply by z and z^2 ... (1 - z - z^2) G(z) = z, G(z) = z/(1 - z - z^2) ... G(z) = (1/√5)(1/(1-φz) - 1/(1-φ̂z)) ... F_n = (1/√5)(φ^n - φ̂^n)"; GF coefficients (0,1,1,2,3,5,8,13,21) re-verified during ingest.
[^2]: [[aocp-generating-functions](pages/aocp-generating-functions.md)] §"Generating Functions for Linearly Recurrent Series" L120-135 — "Given any linearly recurrent sequence ... a_n = c_1 a_{n-1} + ... + c_m a_{n-m} the resulting generating function is a polynomial divided by (1 - c_1 z - ... - c_m z^m) ... 1/(1-z) = 1 + z + z^2 + ..."
[^3]: [[aocp-generating-functions](pages/aocp-generating-functions.md)] §§"Addition"–"Calculus" L106-176 — shifting (×z^k), multiplication convolution "s_n = ∑_{k=0}^{n} a_k b_{n-k}", "1/(1-z) G(z)" as the partial-sum GF, the EGF product "c_n = ∑_k C(n,k) a_k b_{n-k}", and the derivative/integral formulas.
[^4]: [[aocp-generating-functions](pages/aocp-generating-functions.md)] §"Binomial Theorem"/"Exponential"/"Logarithm" L180-202 — "(1 + z)^r = ∑ C(r,k) z^k ... 1/(1-z)^{n+1} = ∑_{k≥0} C(n+k, n) z^k ... e^z = ∑ z^k/k! ... ln(1/(1-z)) = ∑ z^k/k."
[^5]: [[aocp-generating-functions](pages/aocp-generating-functions.md)] §"Knuth AOCP Section 1.2.9 Exercise 1" L206-216 — "generating function for <2^n + 3^n> = {2, 5, 13, 35, ...} ... G_{2^n}(z) = 1/(1-2z) ... G(z) = 1/(1-2z) + 1/(1-3z) = (2-5z)/(1-5z+6z^2)"; GF and coefficients (2,5,13,35,97,275) re-verified during ingest.
