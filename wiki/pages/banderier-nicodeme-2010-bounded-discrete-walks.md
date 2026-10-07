---
title: "Banderier & Nicodème (2010) - Bounded discrete walks"
category: Sources
summary: Banderier and Nicodème extend the kernel method to directed walks of bounded height with any finite set of jumps. Below one wall the generating function is algebraic and is written with the large roots of the kernel 1 − x·steps(u); between two walls it is rational and is written with all the roots, as quotients of alternants (antisymmetric Schur functions). With the jumps −m, …, m and walls at 0 and h − 1 this is exactly the anchored m-smooth castle strip, so the paper gives strips_m(w, h) in closed form in the kernel roots, where the band matrix has no explicit eigenvalues for m ≥ 2. Checked here against the transfer matrix for m ≤ 3, h ≤ 8; the printed two-wall closed form gives cumulative sums of the wall generating functions, and the no-ceiling meander and excursion formulas reproduce the anchored and pinned m-smooth counts (A005773 and the Motzkin numbers at m = 1).
tags: [source, paper, lattice-paths, kernel-method, generating-functions, m-smooth, 1-smooth, transfer-matrix, motzkin]
sources: [banderier-nicodeme-2010-bounded-discrete-walks]
created: 2026-10-07
updated: 2026-10-07
---

# Banderier & Nicodème (2010) - Bounded discrete walks

**Source:** `raw/banderier-nicodeme-2010-bounded-discrete-walks.pdf` (text layer at `raw/banderier-nicodeme-2010-bounded-discrete-walks.txt`, extracted with `pdftotext -layout`; the PDF is git-ignored, the text is tracked). C. Banderier and P. Nicodème, "Bounded discrete walks", AofA'10, DMTCS proc. AM, 2010, pp. 35-48, extended abstract; PDF from Banderier's homepage, https://lipn.univ-paris13.fr/~banderier/Papers/banderier_nicodeme2010.pdf.[^1]
**Date ingested:** 2026-10-07
**Type:** paper (PDF, 14 pp., extended abstract)

## Notation used on this page

The wiki uses `x` for the width variable, `F(w, h)` for the PE 502 count, `P(k, L)` for the signed tower count, `c_i` for column heights, and `h` for castle height ([[castle-notation](pages/castle-notation.md)]), so several of the paper's symbols are renamed here. Footnote quotes keep the paper's symbols.

| paper | meaning | written here as |
|---|---|---|
| `z` | marks walk length | `x` |
| `u` | marks the final altitude | `u` (altitude, not width) |
| `P(u) = Σ_{i=−c}^{d} p_i u^i` | step polynomial: one term per allowed jump | `steps(u)` |
| `c`, `d` | largest down-jump and largest up-jump | `m₋`, `m₊` |
| `u_1, …, u_c` / `v_1, …, v_d` | small and large roots of the kernel | `u_1, …, u_{m₋}` / `v_1, …, v_{m₊}` |
| `F^{[a,b]}(z, u)`, `F_k(z)` | walks from altitude 0 staying in `[a, b]`; those ending at altitude `k` | `strip^{[a,b]}(x, u)`, `strip_k(x)` |
| `W_k(z)` | unconstrained walks ending at altitude `k` | `free_k(x)` |
| `[−h_2, h]` | the strip between two walls | `[−h_low, h_top]` |
| `s_λ` | antisymmetric Schur function of all `c + d` roots | `alt_λ` |

## Summary

**The setting.** A directed walk starts at altitude 0 and at each time step adds a jump from a finite set of integers; `steps(u)` lists the allowed jumps, with weights. The generating function `strip(x, u)` marks length by `x` and final altitude by `u`. The kernel is `1 − x·steps(u)`. Its roots in `u` split into `m₋` small roots, which behave like `x^{1/m₋}` near `x = 0`, and `m₊` large roots, which behave like `x^{−1/m₊}`.[^2] The kernel method writes the functional equation for a constrained walk as `(kernel)·strip = (known terms) + (unknown boundary terms)`, and substitutes roots of the kernel for `u` to get extra equations for the unknowns.[^3]

**Without walls, and with one floor.** For walks on all of the integers the length count is `1/(1 − x·steps(1))`. For meanders, which stay at or above 0 and end anywhere, the generating function is `(1/(1 − x·steps(1)))·Π_i (1 − u_i)`, and for excursions, which also end at 0, it is `((−1)^{m₋−1}/(p_{−m₋} x))·Π_i u_i`, both products over the small roots. These are taken from Banderier and Flajolet's earlier paper.[^4]

**Below one wall.** For walks that stay at or below altitude `h_top` (no floor), `strip^{[−∞, h_top]}(x, u)` is algebraic. The proof writes the step-by-step decomposition, removes the jumps that would cross the wall, and substitutes the `m₊` large roots, which gives a linear system for the `m₊` unknown boundary functions; Cramer's rule solves it with Vandermonde-type determinants.[^5] Extracting a fixed final altitude `k` gives an expression in elementary symmetric functions of the large roots and the unconstrained `free_j(x)`.[^6]

**Between two walls.** For walks that stay in `[−h_low, h_top]`, the generating function is rational. The functional equation has `m₋` unknowns at the floor and `m₊` at the ceiling. Since the generating function is now a Laurent polynomial in `u`, all `m₋ + m₊` roots can be substituted, and Cramer's rule gives the unknowns as quotients of alternants `alt_λ` (determinants of powers of the roots) with explicit exponent vectors `λ`.[^7] The rational case can also be computed by matrix powering in `O((h_low + h_top)^ω log n)` operations, `ω ≈ 2.38`, or by recurrences of order less than `h_low + h_top`.[^8]

**On transfer matrices.** The authors present the kernel method as giving exact enumeration and higher-order asymptotics where other approaches, transfer matrices among them, would be of much higher complexity or would not give them.[^3]

## The castle reading

An anchored m-smooth castle of width `w` and its column heights `c_1 = 1, c_2, …, c_w` correspond to a walk of length `w − 1` with altitudes `c_i − 1`, jumps `−m, …, m` (all weights 1, so `steps(u) = u^{−m} + ⋯ + u^m` and `m₋ = m₊ = m`), floor 0 and ceiling `h − 1` ([[m-smooth-castles](pages/m-smooth-castles.md)]). So

```
Σ_w strips_m(w, h) x^w  =  x · strip^{[0, h−1]}(x, 1),
```

and the paper's two-wall theorem expresses the m-smooth strip, and so `smooth_m(w, h) = strips_m(w, h) − strips_m(w, h − 1)`, through the `2m` roots of `1 − x(u^{−m} + ⋯ + u^m)`. The band matrix has no explicit eigenvalues for `m ≥ 2` ([[m-smooth-castles](pages/m-smooth-castles.md)] §3.5), but the kernel roots are defined by a single polynomial equation of degree `2m` in `u`. Checks, by execution:[^9]

- **Two walls.** Substituting all `2m` kernel roots into the paper's functional equation and solving for the `2m` wall functions reproduces the transfer-matrix generating function `e_1ᵀ(I − x·band)^{−1}𝟙` for `m = 1, 2, 3` and `h ≤ 8`. At `m = 1` this is the strip of [[1-smooth-castles](pages/1-smooth-castles.md)].
- **The printed alternant formula.** With `h_low = 0`, the printed quotient labelled as the floor function at altitude `k` equals `(−1)^{m−1−k}·(strip_0 + ⋯ + strip_k)`, a cumulative sum rather than `strip_k` itself; the ceiling quotients behave the same way from the top once the exponent 0 is kept in the exponent vector. The individual wall functions follow by differences (checked for `m ≤ 3`).
- **No ceiling.** The meander formula reproduces the anchored m-smooth counts with no height bound, `1, 2, 5, 13, 35, 96, …` (A005773, [[motzkin-castles](pages/motzkin-castles.md)] §5) at `m = 1` and `1, 3, 12, 51, 226, 1025, 4724, …` at `m = 2`; the excursion formula reproduces the castles with both end columns at height 1 and no height bound, the Motzkin numbers at `m = 1` and `1, 1, 3, 9, 32, 120, 473, …` at `m = 2` (checked for `m ≤ 3`).

## Key Takeaways

- **The kernel method handles any step set.** Below one wall it needs the `m₊` large roots; between two walls it needs all roots, and the answer is rational.[^5][^7]
- **m-smooth strips in closed form.** With jumps `−m, …, m` and walls `0` and `h − 1`, the two-wall theorem is the m-smooth castle strip: an expression in the `2m` roots of a degree-`2m` polynomial, against a band matrix of size `h` (verified, `m ≤ 3`).[^9]
- **The no-ceiling limits.** Meanders and excursions are the anchored and the pinned m-smooth castles with no height bound.[^4][^9]
- **Read the closed form with care.** The printed alternant quotients give cumulative sums of the wall functions (verified).[^9]

## Entities & Concepts

- [[kernel-method](pages/kernel-method.md)] - the technique the paper extends to walls.
- [[m-smooth-castles](pages/m-smooth-castles.md)] - the castle family whose strips are the two-wall walks with jumps `−m, …, m`.
- [[1-smooth-castles](pages/1-smooth-castles.md)] - the case `m = 1`.
- [[motzkin-castles](pages/motzkin-castles.md)] - the no-ceiling `m = 1` counts (A005773, Motzkin numbers).
- [[castle-strip](pages/castle-strip.md)] - the transfer-matrix picture of the same strips.

## Relation to Other Wiki Pages

The wiki counts castle strips with transfer matrices on column heights ([[castle-strip](pages/castle-strip.md)]). For the 1-smooth rule the eigenvalues are explicit and give the Chebyshev formulas of [[1-smooth-castles](pages/1-smooth-castles.md)]; for the m-smooth rule with `m ≥ 2` they are not, and [[m-smooth-castles](pages/m-smooth-castles.md)] computes its generating functions from counts. This paper supplies the closed form for those strips in terms of the kernel roots. The kernel method also appears on [[prodinger-2025-cornerless-motzkin-bargraphs](pages/prodinger-2025-cornerless-motzkin-bargraphs.md)], applied to Motzkin paths on a three-layer automaton.

## Footnotes

[^1]: [[banderier-nicodeme-2010-bounded-discrete-walks](pages/banderier-nicodeme-2010-bounded-discrete-walks.md)] p.35 L1-L7 [synthesis] - the running header "DMTCS proc. AM, 2010, 35–48", the AofA'10 label, the title "Bounded discrete walks" and the authors C. Banderier (LIPN) and P. Nicodème (LIX).
[^2]: [[banderier-nicodeme-2010-bounded-discrete-walks](pages/banderier-nicodeme-2010-bounded-discrete-walks.md)] §2 L84-L92, §2.1 L150-L152 [synthesis] - each walk is encoded by the Laurent polynomial `P(u) = Σ_{i=−c}^{d} p_i u^i`, "where c is the size of the largest backward jump and d is the size of the largest upward jump"; Property 1: the kernel `1 − zP(u)` has `c` "small roots" behaving like `z^{1/c}` and `d` "large roots" behaving like `z^{−1/d}` at `z = 0`.
[^3]: [[banderier-nicodeme-2010-bounded-discrete-walks](pages/banderier-nicodeme-2010-bounded-discrete-walks.md)] §1 L62-L66, L77-L80 - "The kernel method consists in getting additional equations by plugging the roots u(z) of the 'kernel' K(z, u) in the initial equation, which in general is enough to solve the system."; "while other approaches (like e.g. transfer matrices or probability theory) would be either of much higher complexity, or would not give access to exact enumeration or to higher order asymptotics."
[^4]: [[banderier-nicodeme-2010-bounded-discrete-walks](pages/banderier-nicodeme-2010-bounded-discrete-walks.md)] §2 Fig. 1 L98-L142 [synthesis] - the generating functions of unconstrained walks `W(z) = 1/(1 − zP(1))`, meanders `M(z) = (1/(1 − zP(1))) Π_{i=1}^{c} (1 − u_i(z))` and excursions `E(z) = ((−1)^{c−1}/(p_{−c} z)) Π_{i=1}^{c} u_i(z)`, whose caption says the roots satisfy `1 − zP(u_i(z)) = 0` and that the constants "are made explicit in [4]", reference [4] being Banderier and Flajolet 2002.
[^5]: [[banderier-nicodeme-2010-bounded-discrete-walks](pages/banderier-nicodeme-2010-bounded-discrete-walks.md)] §3 Theorem 2 L191-L196 and proof L199-L239 [synthesis] - "The bivariate generating function of walks starting at 0, and remaining below the wall y = h is algebraic"; the proof removes "all jumps which sent us above the border h", plugs in "the d large roots vi", and solves the resulting "linear system of d equations with d unknowns ... with the Cramer formula", giving "Vandermonde-like determinants".
[^6]: [[banderier-nicodeme-2010-bounded-discrete-walks](pages/banderier-nicodeme-2010-bounded-discrete-walks.md)] §3 Theorem 3 L240-L249 [synthesis] - the generating function of walks of bounded height ending at altitude `k`, as `W_k(z)` minus a sum over the large roots of elementary symmetric functions `e_{d−1−m}` divided by `v_i^{h+1} Π_{j≠i}(v_i − v_j)`.
[^7]: [[banderier-nicodeme-2010-bounded-discrete-walks](pages/banderier-nicodeme-2010-bounded-discrete-walks.md)] §3 Theorem 4 L284-L298, proof L300-L343 [synthesis] - "The bivariate generating function of walks starting at 0, and remaining between the walls y = −h2 and y = h is rational"; substituting the roots is legitimate "since F is here a Laurent polynomial in u, and not a Laurent series" and "leads to a system with c + d unknowns; the Cramer formula gives the solutions of the system in terms of more complicated Vandermonde-like determinants", written with "the antisymmetric associated Schur function" `s_λ` and exponent vectors λ, λ'_k, λ''_k (eqs. 9-12).
[^8]: [[banderier-nicodeme-2010-bounded-discrete-walks](pages/banderier-nicodeme-2010-bounded-discrete-walks.md)] p.41 footnote (ii) L387-L390 [synthesis] - in the two-boundary (rational) case, binary exponentiation of matrices gives complexity `O((h + h2)^ω log n)` with `ω ≈ 2.38` (the text layer renders ω as `$`), improvable via D-finiteness to "recurrences of order less than h + h2".
[^9]: Verified by execution (Python 3, NumPy, 2026-10-07). For `steps(u) = u^{−m} + ⋯ + u^m` the `2m` roots of `u^m − x(1 + u + ⋯ + u^{2m}) = 0` were computed at `x = 0.02, 0.03, 0.05, 0.07, 0.09`. The paper's two-wall functional equation, with floor 0 and ceiling `h − 1`, was evaluated at every root and solved for the wall functions; `strip^{[0,h−1]}(x, 1)` then matched `e_1ᵀ(I − x·band)^{−1}𝟙` to `10^{−9}` for `m = 1, 2, 3`, `h = m + 2, …, 8`. The printed alternant quotients `s_{λ'_k}/(z s_λ)` equal `(−1)^{m−1−k}(F_0 + ⋯ + F_k)` for `m ≤ 3` and `h ∈ {m+3, m+6}`; with 0 restored in λ''_k the ceiling quotients match the cumulative sums from the top in absolute value. The meander and excursion formulas of Fig. 1, from the `m` small roots, matched the counts of anchored, respectively pinned, m-smooth walks with floor 0 and no ceiling, by dynamic program to length 59, for `m = 1, 2, 3`.
