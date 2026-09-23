---
title: Linear q-differential systems and their q = 1 shadow
category: Concepts
summary: A linear q-differential system relates a vector of series at x to the same vector at xq, F(x) = y M(x) F(xq) + C(x). This is the shape the area-counting equations for convex polyominoes take. There is no general integration method, but Bousquet-Mélou and Fédou solve one by working in its q = 1 limit, an ordinary differential system with Bessel solutions, and then lifting the ODE recipe back to q. The recipe is to find a homogeneous solution matrix W with W = M W(xq), substitute F = W G, and solve the resulting scalar equations g(x) - y g(xq) = h coefficientwise as g_n = h_n/(1 - yq^n), with log_q(x) = log x / log q standing in for the logarithm.
tags: [concept, q-analog, q-differential-system, q-bessel, variation-of-parameters, generating-function, polyomino, convex, functional-equation]
sources: [bousquet-melou-fedou-1995-convex-polyominoes]
created: 2026-09-22
updated: 2026-09-22
---

# Linear q-differential systems and their q = 1 shadow

## Description

A **linear q-differential system** is a vector equation

```
F(x) = y M(x) F(xq) + C(x)
```

where `F` is a vector of unknown power series in `x` (with `y` and `q` as parameters), `M` is a matrix of known series, and `C` is a known inhomogeneous term. The "derivative" is the q-shift `x -> xq`: the equation relates each series to itself at `xq`. Area-counting equations for polyominoes take this form. Adding a column of height `k` multiplies the area weight by `q^k`, and summing over `k` lands the generating function at a shifted argument.[^1] For parallelogram, directed convex and convex polyominoes, Bousquet-Mélou's algebraic-language encoding gives a system of this form with blocks of size 1, 2 and 3.[^2] Its power-series solution is unique, but, in the paper's words, "there exists no general technique to integrate q-differential equations".[^3]

## The q = 1 shadow

Bousquet-Mélou and Fédou's approach is to solve the ordinary differential system that the q-system tends to, and use it as a template.[^4]

1. **Scale and take the limit.** With `y = 1` the generating functions diverge as `q -> 1`. Substituting `x -> x(1 - q)^2` and dividing by the right power of `1 - q` gives series with a limit. The parallelogram equation becomes the Riccati equation `X' = 1 + X^2/x`.[^5]
2. **Solve the ODE.** The substitution `X = -x f'/f` linearizes it, giving `X = J_1/J_0` with the Bessel series `J_0 = sum (-1)^n x^n / n!^2` and `J_1 = -sum (-1)^n x^n / ((n-1)! n!)`. The full convex system is a 3×3 linear system. Its homogeneous solutions are the products `Jbar_1^2, Jbar_0 Jbar_1, Jbar_0^2` and their counterparts built from the second-kind solutions `Ybar_i = Kbar_i + Jbar_i log x`, with Wronskian 1. Variation of parameters then produces closed forms "after a few integrations which are miraculously simple".[^6]
3. **q-analogize.** Guess q-series whose `q = 1` limits are these solutions and that satisfy the q-system. For parallelograms the guess is immediate. For directed convex, the q-analogue of the odd part of `J_1` is "obviously more difficult to guess".[^7]
4. **Variation of parameters at the q level.** Find an invertible `W` with `W = M W(xq)` and put `F = W G`. Then `G - y G(xq) = W^{-1} C`, which is three scalar equations of the form `g(x) - y g(xq) = h`. When `h = sum h_n x^n` is expanded in `x` this is solved coefficientwise:[^8]

```
g = sum_n h_n / (1 - y q^n) x^n
```

The logarithm has no power-series q-analogue. What the method needs is a function with `f(xq) - f(x) = 1`, and `log_q(x) = log(x)/log(q)` is used as a formal device for it. Working with the "power series part" of `W` instead yields a triangular system with the same calculations.[^9]

## Why it worked here

The 3×3 matrix of the convex block, `((1, 2xq, x^2q^2), (1, 1+xq, xq), (1, 2, 1))`, is the symmetric square of the 2×2 matrix `((1, 1), (xq, 1))`. By Property 3.3, if `(U_0, U_1)` and `(V_0, V_1)` both solve `(S_0, S_1)(x) = 1/(1 - xq) ((1, 1), (xq, 1)) (S_0, S_1)(xq)`, then `(2U_1V_1, U_1V_0 + U_0V_1, 2U_0V_0)` solves the 3×3 homogeneous system. So the 3×3 problem reduces to a 2×2 one "close to the differential system which defines the Bessel functions of the first and second type".[^10] The authors call the method "not universal", but say it "suggests a systematic approach for integrating q-equations".[^11]

At the inhomogeneous step the `q = 1` template ran out: "we could no longer 'copy' the form of the solution that we found in the case q = 1". The inhomogeneous term contains `S = M_1 Jhat_0 - M_0 Jhat_1` and `T = M_1 Yhat_0 - M_0 Yhat_1`, which are not written over `J_0`. The hatted series are the barred ones divided by `E = sum x^n q^n/(q)_n`, and `det W = E^3`. The authors "were able to rewrite S and T in a more suitable form" (Lemma 4.1), and they describe this rewriting as "a miracle".[^12]

## Where the castle wiki meets it

Own reasoning, not from the source:

- **Fixed height is the finite case.** A castle of bounded height has a finite transfer matrix and a rational generating function ([[bounded-height-castles-nacci](pages/bounded-height-castles-nacci.md)]). Letting height be unbounded while marking area is what turns the column recurrence into a q-shift equation like the ones above. On the area ladder, Ferrers diagrams and stacks still solve as sums of q-products. The parallelogram rung, `y J_1/J_0`, is the first whose solution is a ratio of q-series.
- **The scalar step is the adding-a-slice step.** `g_n = h_n/(1 - yq^n)` is the same geometric-series resolution that the "adding a slice" construction on [[convex-polyomino-by-area](pages/convex-polyomino-by-area.md)] performs when one column height is iterated. The method's added power is the solution matrix `W`, which keeps track of several interacting boundary phases at once.

## Appearances in Sources

- [[bousquet-melou-fedou-1995-convex-polyominoes](pages/bousquet-melou-fedou-1995-convex-polyominoes.md)] - the method, applied to the 1×1 + 2×2 + 3×3 system for parallelogram, directed convex and convex polyominoes.

## Related Concepts

- [[convex-polyomino-by-area](pages/convex-polyomino-by-area.md)] - the area ladder whose top three rungs this method solves.
- [[column-convex-polygon-enumeration](pages/column-convex-polygon-enumeration.md)] - Bousquet-Mélou's later add-a-column functional equations, a different route to the same generating functions.
- [[steep-polyominoes-q-motzkin-bessel](pages/steep-polyominoes-q-motzkin-bessel.md)] - q-Bessel quotients from another polyomino family.
- [[klarner-rivest-1974-convex-n-ominoes](pages/klarner-rivest-1974-convex-n-ominoes.md)] - an early one-unknown instance (own reasoning): parallelograms by area satisfy `B(x, y) = xy/(1-xy) + xy/(1-xy)^2 (B(x, 1) - B(x, xy))`, a shift `y -> xy`, which Klarner and Rivest solved by iteration as a ratio of alternating q-series.
- [[prellberg-brak-1995-cluster-models](pages/prellberg-brak-1995-cluster-models.md)] - the *nonlinear* companion. Quadratic q-shift equations for the same families, linearised by `G(x) = α H(qx)/H(x) - b(x)`; the closed forms are q-Bessel ratios of the same shape but the linearisation route bypasses the 3×3 system this page describes for convex polyominoes.
- [[castle-q-bessel-closed-form](pages/castle-q-bessel-closed-form.md)] - a one-step-q-shift closing case: the castle grammar graded by area is `E(u) = A/(1 - uA)`, `A(u) = 1 - x + x E(uq)`, and the linearisation closes to `A = N/M` in one Möbius step rather than the coupled 3×3 system needed for convex polyominoes.
- [[aocp-generating-functions](pages/aocp-generating-functions.md)] - ordinary generating-function background.

## Footnotes

[^1]: Own reasoning, from the column-by-column construction on [[convex-polyomino-by-area](pages/convex-polyomino-by-area.md)]; the substitution `u -> zu` in Flajolet and Sedgewick's "adding a slice" is the same shift, raw/analytic-combinatorics-part-a.pdf Example III.22 pp.199-200 - "F(z, u) = f(zu) + (L[F(z, u)])_{u→zu}".
[^2]: [[bousquet-melou-fedou-1995-convex-polyominoes](pages/bousquet-melou-fedou-1995-convex-polyominoes.md)] Lemma 1.1, p.58 L258-285 [synthesis] - "these three series are totally characterized by the following q-differential system", with blocks for `X`, `(Y, Y_1)` and `(Z, Z_1, Z_3)` (read from the page image); "It is not difficult to see that this q-differential system has a unique solution in terms of power series."
[^3]: [[bousquet-melou-fedou-1995-convex-polyominoes](pages/bousquet-melou-fedou-1995-convex-polyominoes.md)] p.54 L80-83 - "Unfortunately, there exists no general technique to integrate q-differential equations. Nevertheless, we succeeded recently in solving this system. Our method is a sort of q-analogue of the classical method used to solve linear systems of ordinary differential equations."
[^4]: [[bousquet-melou-fedou-1995-convex-polyominoes](pages/bousquet-melou-fedou-1995-convex-polyominoes.md)] p.60 L372-376 - "In the most favourable cases, we get some very precise indications about the form of the solution. Being less optimistic, we can all the same hope that solving the ordinary equations will be a sort of guide for solving the q-equations."
[^5]: [[bousquet-melou-fedou-1995-convex-polyominoes](pages/bousquet-melou-fedou-1995-convex-polyominoes.md)] §2, pp.59-60 L326-344 - "since the generating function X(x, 1, q) diverges when q→1, we have to do a change of variables first. Towards this end, let X̂ = X(x(1 - q)^2, 1, q)/(1 - q)"; the limit "satisfies the ordinary differential equation X̃' = 1 + X̃^2/x" (formula read from the page image).
[^6]: [[bousquet-melou-fedou-1995-convex-polyominoes](pages/bousquet-melou-fedou-1995-convex-polyominoes.md)] pp.60-61 L345-446 [synthesis] - "We solve this last equation by searching a solution of the form -xf'/f"; the homogeneous system "has the following three solutions, which are linearly independent, and whose Wronskian is 1", eq. (8); "the variation of parameters method gives, after a few integrations which are miraculously simple" (formulas read from the page images).
[^7]: [[bousquet-melou-fedou-1995-convex-polyominoes](pages/bousquet-melou-fedou-1995-convex-polyominoes.md)] p.60 L355-371 - "This is quite easy in the case of parallelogram polyominoes ... we now have to find the 'right' q-analogue of the odd part of the series J_1 ... which is obviously more difficult to guess than it was in the case of parallelogram polyominoes."
[^8]: [[bousquet-melou-fedou-1995-convex-polyominoes](pages/bousquet-melou-fedou-1995-convex-polyominoes.md)] §4.1, p.66 L672-692 - "a linear q-differential system can (theoretically) be solved just as if it were an ordinary linear differential system ... the problem will reduce to three equations of the following form: f(x) - yf(xq) = g ... if g = sum g_n x^n, then f = sum g_n/(1 - yq^n) x^n."
[^9]: [[bousquet-melou-fedou-1995-convex-polyominoes](pages/bousquet-melou-fedou-1995-convex-polyominoes.md)] §4.2 Remark (2), p.67 L735-750 - "The logarithm is just a formal tool: we need a function f which satisfies f(xq) - f(x) = 1 ... which is the 'power series part' of W ... the following triangular system ... which involves only power series. But the calculations would eventually have been exactly the same."
[^10]: [[bousquet-melou-fedou-1995-convex-polyominoes](pages/bousquet-melou-fedou-1995-convex-polyominoes.md)] Property 3.3 p.63 and §4.2 Remark (1) p.67 L528-538, L718-734 [synthesis] - the product-vector identity for the 3×3 matrix, and "the integration of the homogeneous system reduces to the integration of a smaller system, which is of an especially convenient form, since it is close to the differential system which defines the Bessel functions of the first and second type" (matrices read from the page images; the "symmetric square" name is this page's).
[^11]: [[bousquet-melou-fedou-1995-convex-polyominoes](pages/bousquet-melou-fedou-1995-convex-polyominoes.md)] p.55 L108-109 - "Although not universal, the method we used suggests a systematic approach for integrating q-equations."
[^12]: [[bousquet-melou-fedou-1995-convex-polyominoes](pages/bousquet-melou-fedou-1995-convex-polyominoes.md)] §4.2 Remark (3) and §4.3, p.68 L754-801 - "The determinant of W is E^3, with the series E defined as in Property 3.2"; "At this point, we could no longer 'copy' the form of the solution that we found in the case q = 1"; "the main difficulty comes from the fact that neither S nor T are expressed in terms of J_0. But here a miracle occurs, we were able to rewrite S and T in a more suitable form"; Lemma 4.1 (formulas read from the page image).
