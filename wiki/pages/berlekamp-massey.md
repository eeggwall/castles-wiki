---
title: Berlekamp–Massey
category: Concepts
summary: The Berlekamp-Massey algorithm returns the shortest linear recurrence satisfied by the first N terms of a sequence over a field; when the sequence satisfies a linear recurrence of order at most N/2, that is its shortest recurrence (Massey 1969, Theorems 1 and 3). The castle count runs it on N = 4(w + 2) + 20 values of P(·, w) modulo 10^9 + 7 to evaluate A^e(100, 10^12).
tags: [concept, algorithm, linear-recurrence, berlekamp-massey, method]
sources: [project-euler-502-observations, project-euler-502-solution, project-euler-502-implementation-notes]
created: 2026-09-13
updated: 2026-10-16
---

# Berlekamp–Massey

## What it computes

The **Berlekamp-Massey algorithm** takes the first `N` terms `s_0, …, s_{N−1}` of a sequence with entries in a field and returns a shortest linear recurrence that they satisfy,

```
s_j + C_1 s_{j−1} + ⋯ + C_L s_{j−L}  =  0,        j = L, L + 1, …, N − 1,           (1)
```

with its order `L`, written `L_N`. Massey states it as the synthesis of the shortest linear feedback shift register that generates the `N` terms; such a register of length `L` with connection polynomial `C(D) = 1 + C_1 D + ⋯ + C_L D^L` is the recurrence (1).[^1] Each of the `N` steps computes one discrepancy, the left-hand side of (1) at the next index, and updates `C(D)`, so the algorithm takes `O(N²)` field operations.[^2]

Two theorems of Massey's paper say when the output is the recurrence of the whole sequence:[^1][^2]

- **Theorem 1.** If a recurrence of order `L` generates `s_0, …, s_{N−1}` but not `s_N`, then every recurrence that generates `s_0, …, s_N` has order at least `N + 1 − L`.
- **Theorem 3.** If `2L_N ≤ N`, the shortest recurrence of the first `N` terms is unique.

**Corollary.** If the whole sequence satisfies a linear recurrence of order at most `N/2`, and `L*` is the order of its shortest one, the algorithm applied to `s_0, …, s_{N−1}` returns a recurrence of order `L*` that generates the whole sequence.

*Proof.* The output has order `L_N ≤ L*`. Suppose it fails at some first index `M ≥ N`. By Theorem 1, the recurrence of order `L*`, which generates `s_0, …, s_M`, has `L* ≥ M + 1 − L_N ≥ N + 1 − L*`, so `2L* ≥ N + 1`, against `L* ≤ N/2`. So the output generates the whole sequence, and since `L*` is the shortest order, `L_N = L*`.

Without a proved bound on the order, the output is a recurrence of the computed terms only. [[project-euler-502-observations](pages/project-euler-502-observations.md)] names the algorithm as a lesson of the solution: it "turns 'I have a sequence, I don't know the recurrence' into a solved problem."[^3]

## How the castle count uses it

The source routes the castle counts with `h > 15000`, among the Project Euler targets only `A^e(100, 10^12)`, to a path in the tower height `k`. For fixed `w`, the source computes `P(0, w), …, P(N − 1, w)` modulo `p = 10^9 + 7` with `N = 4(w + 2) + 20`, finds a recurrence in `k` with Berlekamp-Massey, and evaluates it at `k = h − 2` and `k = h − 1` with [[kitamasa](pages/kitamasa.md)]'s method; at `w = 100`, `N = 428`.[^4] [[project-euler-502-implementation-notes](pages/project-euler-502-implementation-notes.md)] describes the code, `computePviaKBoth`, in which the remainder for `k = h − 1` is `x` times the remainder for `k = h − 2`, reduced once more.

By the Corollary, the output is the recurrence of `P(·, w)` modulo `p` when that sequence satisfies a recurrence of order at most `N/2 = 2w + 14`. The source says that "the recurrence order is at most about 2w empirically" and that "Berlekamp-Massey discovers the recurrence, so no proof is required to use it".[^5] Run over the rationals, Berlekamp-Massey finds the order `2L − 2` in `k` for `4 ≤ L ≤ 12`, with characteristic polynomial `(x + 1)^L (x − 1)^{L−2}`, which has integer coefficients and so also gives a recurrence modulo `p` ([[recurrence-discovery](pages/recurrence-discovery.md)], computed). For these `L` the order is below `N/2`; at `L = 100` no bound is proved on the wiki.

## Appearances in Sources

- [[project-euler-502-observations](pages/project-euler-502-observations.md)] - Berlekamp-Massey as a lesson of the solution.
- [[project-euler-502-solution](pages/project-euler-502-solution.md)] - the path in `k`: `N = 4(w + 2) + 20` terms modulo `p`, an order "at most about 2w empirically", and one pass for `P(h−2, w)` and `P(h−1, w)`.
- [[project-euler-502-implementation-notes](pages/project-euler-502-implementation-notes.md)] - the steps of `computePviaKBoth` and the shift `poly2 · x mod charPoly`.

## Related Concepts

- [[kitamasa](pages/kitamasa.md)] - the method that evaluates the recurrence at a far index.
- [[castle-count-algorithms](pages/castle-count-algorithms.md)] - the path in `k`, used when `h > 15000`.
- [[recurrence-discovery](pages/recurrence-discovery.md)] - Berlekamp-Massey over the rationals on `P(k, L)`: order `k + 1` in `L`, and `2L − 2` in `k` for `4 ≤ L ≤ 12`.
- [[closed-form-hunting](pages/closed-form-hunting.md)] - the closed forms `P(k, 2) = (−1)^k (k+1)` and `P(k, 3) = (−1)^k (k+1)²`, whose recurrences in `k` Berlekamp-Massey recovers.
- [[castle-counting-formula](pages/castle-counting-formula.md)] - the formula for `A^e(w, h)` through `P(h−1, w)` and `P(h−2, w)`.
- [[castle-counting-function](pages/castle-counting-function.md)] - the Project Euler target and its three terms.
- [[castle-compression](pages/castle-compression.md)] - the order `L` returned by the algorithm, the linear complexity, as a measure of how far a sequence is generated by a linear rule.
- [[castle-snippets-cryptography](pages/castle-snippets-cryptography.md)] - `bm_modp`, an implementation over the integers modulo a prime, and the linear complexity of filtered castle registers.

## Footnotes

[^1]: https://crypto.stanford.edu/~mironov/cs359/massey.pdf (read 2026-10-16) - J. L. Massey, "Shift-Register Synthesis and BCH Decoding", IEEE Transactions on Information Theory IT-15(1) (1969), 122-127, p.122: "the problem of finding the shortest linear feedback shift register that can generate a given finite sequence of digits", the recursion "s_j = − Σ_{i=1}^{L} c_i s_{j−i}, j = L, L + 1, L + 2, …", and "Theorem 1: If some LFSR of length L generates the sequence s_0, s_1, …, s_{N−1} but not the sequence s_0, s_1, …, s_{N−1}, s_N, then any LFSR that generates the latter sequence has length L′, satisfying L′ ≥ N + 1 − L."
[^2]: https://crypto.stanford.edu/~mironov/cs359/massey.pdf (read 2026-10-16) - Massey 1969, p.124: the LFSR Synthesis Algorithm, whose step 2 computes "d = s_N + Σ c_i s_{N−i}" and whose steps 4 and 5 update "C(D)" once per `N`; "the minimal-length LFSR is unique if and only if 2L_N(s) ≤ N"; and "Theorem 3: ... If 2L ≤ n, then C(D) is the connection polynomial of the unique minimal-length L LFSR that generates the sequence." The count `O(N²)` is the wiki's, from these steps.
[^3]: [[project-euler-502-observations](pages/project-euler-502-observations.md)] §"Lessons learned" L38 - "Berlekamp-Massey turns \"I have a sequence, I don't know the recurrence\" into a solved problem."
[^4]: [[project-euler-502-solution](pages/project-euler-502-solution.md)] §"The k-direction Berlekamp-Massey path (h > 15000)" L157-163 - "For fixed w, generate P(0, w), P(1, w), …, P(N-1, w) for N = 4(w+2) + 20 using the same inner recurrence the exact path uses, all mod p", "Berlekamp-Massey finds the minimal linear recurrence. Kitamasa jumps directly to any index k. Both P(h-2, w) and P(h-1, w) are computed in one pass", "F(100, 10^12): w = 100, so N ≈ 428".
[^5]: [[project-euler-502-solution](pages/project-euler-502-solution.md)] §"The k-direction Berlekamp-Massey path (h > 15000)" L165 - "The recurrence order is at most about 2w empirically. Berlekamp-Massey discovers the recurrence, so no proof is required to use it, but the transfer-matrix argument justifies why one exists."
