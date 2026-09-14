---
title: Permutation inversions (and the q-factorial)
category: Concepts
summary: The inversion statistic on permutations, whose generating function ∏(1−z^k)/(1−z)^n is the q-factorial — the prototype of the inversion-graded generating functions that q-Catalan and q-Motzkin numbers are.
tags: [concept, inversions, permutations, q-factorial, q-analog, generating-functions]
sources: [aocp-combinatorics]
created: 2026-09-13
updated: 2026-09-13
---

# Permutation inversions (and the q-factorial)

## Description

An **inversion** of a permutation `a_1…a_n` is a pair `(a_i, a_j)` with `i < j` and `a_i > a_j` — an out-of-order pair.[^1] The number of permutations of *n* with exactly *k* inversions, `I_n(k)`, is the coefficient sequence of a single clean generating function, the **q-factorial**:[^2]

```
G_n(z) = Σ_k I_n(k) z^k = ∏_{k=1}^{n} (1 + z + … + z^{k−1}) = ∏_{k=1}^{n} (1 − z^k)/(1 − z) = [n]_z!
```

Properties (all verified by brute enumeration for `n ≤ 6`):[^3]

- Row sum `G_n(1) = n!` — every permutation has *some* inversion count.
- Symmetric: `I_n(k) = I_n(binomial(n,2) − k)` — reversing a permutation complements its inversions, and the maximum is `binomial(n,2)`.
- Recurrence `I_n(k) = I_n(k−1) + I_{n−1}(k)`.

Because `g_n(z) = G_n(z)/n! = ∏_k (1+…+z^{k−1})/k`, the inversion count of a *random* permutation is a **sum of independent uniform** variables (each `h_k` uniform on `{0,…,k−1}`), so its mean and variance add across factors.[^4] Inversions are also captured by the **inversion table** `b_1…b_n` (`b_j` = elements left of *j* exceeding it, `0 ≤ b_j ≤ n−j`), a bounded-integer-tuple encoding that uniquely determines the permutation — the same "encode by an independent-coordinate tuple" idea as the castle's [[binary-string-bijection](pages/binary-string-bijection.md)].[^1]

## Why it matters for the castle

The inversion statistic is the **q-analog hinge**. The q-factorial `∏(1−z^k)/(1−z)^n` is the prototype of every inversion-graded generating function the wiki reaches for:

- **Dyck words by inversions → q-Catalan** (Carlitz), and **steep Dyck words by inversions → q-Motzkin** — see [[dyck-words](pages/dyck-words.md)], [[q-catalan-numbers](pages/q-catalan-numbers.md)], [[steep-polyominoes-q-motzkin-bessel](pages/steep-polyominoes-q-motzkin-bessel.md)]. Inversion number also equals the **area** of the Ferrers diagram between a Dyck path and the default steep path — linking the inversion grading to the *area* grading the castle already uses ([[castle-by-area](pages/castle-by-area.md)]).
- **The q-graded castle count.** A castle q-refinement — the open "find the q-equivalent" thread — would be built from exactly this q-factorial / Gaussian-binomial machinery. The castle's ordinary generating functions are C-finite ([[signed-tower-count](pages/signed-tower-count.md)]); the inversion prototype shows the form a *q*-refinement takes.

## Appearances in Sources

- [[aocp-combinatorics](pages/aocp-combinatorics.md)] — Knuth's development of inversions, inversion tables, and the inversion generating function.

## Related Concepts

- [[dyck-words](pages/dyck-words.md)] — inversion number = Ferrers-diagram area; the q-graded object.
- [[q-catalan-numbers](pages/q-catalan-numbers.md)], [[steep-polyominoes-q-motzkin-bessel](pages/steep-polyominoes-q-motzkin-bessel.md)] — inversions as the q-statistic.
- [[binary-string-bijection](pages/binary-string-bijection.md)] — the castle's bounded-tuple encoding, analogous to inversion tables.
- [[generating-functions](pages/generating-functions.md)] — the method.
- [[aocp-permutations](pages/aocp-permutations.md)] — the permutation/factorial basics (the same permutations, built by insertion rather than encoded by inversion counts).

## Footnotes

[^1]: [[aocp-combinatorics](pages/aocp-combinatorics.md)] §"Permutations and Inversions" L13-38 — "If i < j and a_i > a_j, then (a_i, a_j) is an inversion ... b_j is the number of elements to the left of j that are greater than j ... 0 ≤ b_j ≤ n-j ... Hall (1956) showed that inversion tables uniquely determine permutations."
[^2]: [[aocp-combinatorics](pages/aocp-combinatorics.md)] §"Counting Inversions with Generating Functions" L71-96 — "G_n(z) = Σ_{k≥0} I_n(k) z^k ... G_n(z) = (1 + z + ... + z^{n-1}) G_{n-1}(z) ... = (1-z^n)(...)(1-z^2)(1-z) / (1-z)^n."
[^3]: [[aocp-combinatorics](pages/aocp-combinatorics.md)] §"Counting Inversions with Generating Functions" L69, L84, L96 — the recurrence "I_n(k) = I_n(k-1) + I_{n-1}(k)", the product form, and the symmetry "I_n(k) = I_n(C(n,2) - k)"; product form, symmetry, and row-sum = n! re-verified by brute enumeration for n=1..6 during ingest.
[^4]: [[aocp-combinatorics](pages/aocp-combinatorics.md)] §"Knuth Goes To Outer Space" L104-134 — "G_n(z)/n! = g_n(z) ... h_k(z) = (1+z+...+z^{k-1})/k ... g_n(z) = h_1(z) ... h_n(z) ... E(g_n) = Σ E(h_k), Var(g_n) = Σ Var(h_k)."
