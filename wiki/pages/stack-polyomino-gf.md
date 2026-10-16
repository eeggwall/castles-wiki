---
title: Stack polyomino generating function
category: Concepts
summary: A stack polyomino is the diagram of a composition whose parts weakly rise and then weakly fall, the shape of a convex castle. Flajolet and Sedgewick read its generating function by area, St(z) = Σ_{k≥1} z^k/(1 − z^k) · 1/((1 − z)(1 − z²)⋯(1 − z^{k−1}))², off a decomposition at the first tallest column; its coefficients are A001523. The same series is Bender's trapezoid series at y = 1 and Bousquet-Mélou's stack series at s = t = x = y = 1. By semi-perimeter the stacks are counted by A001519.
tags: [concept, polyomino, stack-polyomino, generating-functions, symbolic-method, durfee-square, castle-tower]
sources: [analytic-combinatorics-ch1-ogfs, klarner-rivest-1974-convex-n-ominoes, algebraic-languages-and-polyominoes-enumeration, bender-1974-convex-n-ominoes, column-convex-polygon-enumeration]
created: 2026-09-15
updated: 2026-10-16
---

# Stack polyomino generating function

## Definition and generating function

A **stack polyomino** is the diagram of a composition `(x_1, …, x_ℓ)` whose parts rise weakly to a maximum and then fall weakly: `1 ≤ x_1 ≤ ⋯ ≤ x_j ≥ x_{j+1} ≥ ⋯ ≥ x_ℓ ≥ 1` for some `j`.[^1] Drawn as columns of heights `x_1, …, x_ℓ` on a common base, a stack polyomino is a castle with a unimodal skyline, a [[convex-castle](pages/convex-castle.md)]. The stacks of area 3 are the skylines `(3)`, `(1, 2)`, `(2, 1)` and `(1, 1, 1)`; the skyline `(2, 1, 2)` has area 5 and is not a stack.

Cut a stack at its first column of maximal height `k`. The columns before it form a partition into parts at most `k − 1`, and the columns after it a partition into parts at most `k`, since a later column may again have height `k`. In the symbolic method, with `P^{1..k}` the class of partitions into parts at most `k` ([[symbolic-method](pages/symbolic-method.md)]), this is the decomposition[^1]

```
Stack  ≅  ⋃_{k≥1}  P^{1..k−1} × Z^k × P^{1..k}.
```

The generating function of `P^{1..k}` by size is `1/((1 − z)(1 − z²)⋯(1 − z^k))`, so the generating function of the stacks by area is[^1]

```
St(z)  =  Σ_{k≥1}  z^k/(1 − z^k) · 1/((1 − z)(1 − z²)⋯(1 − z^{k−1}))²
       =  z + 2z² + 4z³ + 8z⁴ + 15z⁵ + 27z⁶ + 47z⁷ + 79z⁸ + ⋯
```

Flajolet and Sedgewick write this series `S(z)` (Example I.8, pp. 45-46 of [[analytic-combinatorics-ch1-ogfs](pages/analytic-combinatorics-ch1-ogfs.md)]); the wiki writes `St(z)`, since `S` is the signed castle count ([[castle-notation](pages/castle-notation.md)]). Its coefficients are `A001523`, the number of stacks, or weakly unimodal compositions, of `n` ([[weakly-unimodal-composition](pages/weakly-unimodal-composition.md)]).[^2]

## Stacks and castles

The castles of area `n` are the compositions of `n`, `2^{n−1}` of them ([[castle-by-area](pages/castle-by-area.md)]), and the stacks of area `n` are the castles of area `n` with a unimodal skyline. A convex castle of height `h` has exactly `h` blocks, since each of its rows is one run of columns ([[convex-castle](pages/convex-castle.md)]). So the convex castles carry three countings: `A_convex(w, h) = C(2h + w − 3, w − 1)` by width and height ([[convex-castle-binomial-identity](pages/convex-castle-binomial-identity.md)]), `A001523` by area, and `A001519` by semi-perimeter (section *By semi-perimeter*).

## Two more derivations of the same series

**Bender's trapezoids.** Bender counts the stacks under the name trapezoids: sequences of rows with left ends `l_i ≤ l_{i+1}` and right ends `r_i ≥ r_{i+1}`, each row inside the row below. With `x` marking area and `y` the length of the base row,[^3]

```
T(x, y)  =  Σ_{k≥1}  x^k y (1 − x^k y) / Π_{n=1}^{k} (1 − x^n y)².
```

At `y = 1` the factor `1 − x^k` cancels one of the two factors `1 − x^k` of the denominator, so `T(x, 1) = St(x)` term by term. Bender cuts every convex polyomino into an upright trapezoid, a parallelogram and an inverted trapezoid, and `T(x, 1)` has radius of convergence 1, so the growth `2.30914…^n` of the convex polyominoes by area comes from the parallelograms ([[bender-1974-convex-n-ominoes](pages/bender-1974-convex-n-ominoes.md)]).[^4]

**Bousquet-Mélou's add-a-column equation.** [[column-convex-polygon-enumeration](pages/column-convex-polygon-enumeration.md)] builds the stacks lying on their left column, a quarter turn from the upright stack, by adding a new first column that contains the old first column (Lemma 2.4). Lemma 2.3 of that paper solves the resulting equation (Lemma 2.5):[^5]

```
St(s, t, x, y, q)  =  sty Σ_{n≥1}  x^n q^n / ((syq; q)_{n−1}² (1 − styq^n)),
```

with `s`, `t` marking the left and right column heights, `x` the width, `y` the vertical half-perimeter and `q` the area, and `(a; q)_n = (1 − a)(1 − aq)⋯(1 − aq^{n−1})`. At `s = t = x = y = 1` it is `Σ_n q^n/((q; q)_{n−1}² (1 − q^n)) = St(q)` term by term.

## By semi-perimeter

Delest and Viennot code a stack polyomino of perimeter `2n + 4` by a Fibonacci word. Follow the upper boundary from the bottom-left corner to the bottom-right corner, writing `a` for each vertical step and `xx` for each East step, then delete the first and the last `a` and one `xx` from the top plateau. The result is a word of length `2n` in `{a, xx}*` with an even number of letters `a`.[^6] Delest and Viennot count these words as `F_{2n}` with `F_0 = F_1 = 1`; in the standard indexing `F_1 = F_2 = 1` this is `F_{2n+1} = A001519(n + 1)`:

```
Σ_{n≥0} F_{2n+1} t^{2n}  =  (1 − t²) / ((1 − t − t²)(1 + t − t²))  =  1 + 2t² + 5t⁴ + 13t⁶ + 34t⁸ + ⋯
```

A stack in a `w × h` bounding box has perimeter `2(w + h)`, so this count is the antidiagonal sum of the convex-castle counts,

```
Σ_{w+h=n+2}  C(2h + w − 3, w − 1)  =  F_{2n+1},
```

which holds for `n ≤ 14` (computed).[^7] Delest and Viennot state that the generating function of the stacks by perimeter and area had been found, and cite E. M. Wright's paper *Stacks* (1968) for it.[^8]

## Appearances in Sources

- [[analytic-combinatorics-ch1-ogfs](pages/analytic-combinatorics-ch1-ogfs.md)] - Example I.8, pp. 45-46: the decomposition at the first tallest column and the series `S(z)`, written `St(z)` here.
- [[bender-1974-convex-n-ominoes](pages/bender-1974-convex-n-ominoes.md)] - the trapezoid series `T(x, y)`, eq. (3), and the radius of convergence of `T(x, 1)`.
- [[column-convex-polygon-enumeration](pages/column-convex-polygon-enumeration.md)] - the stack polygons by left and right height, width, vertical half-perimeter and area, Lemmas 2.4 and 2.5.
- [[algebraic-languages-and-polyominoes-enumeration](pages/algebraic-languages-and-polyominoes-enumeration.md)] - Lemma 3.2: the stacks of perimeter `2n + 4` coded by Fibonacci words; the stacks as the two end pieces of a convex polyomino.
- [[klarner-rivest-1974-convex-n-ominoes](pages/klarner-rivest-1974-convex-n-ominoes.md)] - p. 33: Wright's stacks, `s(3) = 4`, the injection of stacks into parallelograms, and the split of every convex polyomino into two stacks and a parallelogram, which gives `c(n) ≤ (n + 2)^4 p(n)`.

## Related Concepts

- [[convex-castle](pages/convex-castle.md)] - the castles with a unimodal skyline, which are the stack polyominoes; their counts by width and height, area and semi-perimeter.
- [[symbolic-method](pages/symbolic-method.md)] - the dictionary from the decomposition to `St(z)`.
- [[weakly-unimodal-composition](pages/weakly-unimodal-composition.md)] - the compositions counted by `A001523`.
- [[castle-polyomino](pages/castle-polyomino.md)] - the castles, of which the stacks are those with a unimodal skyline.
- [[polyominoes](pages/polyominoes.md)] and [[column-convex-polyomino](pages/column-convex-polyomino.md)] - the families that contain the stacks.
- [[convex-polyomino](pages/convex-polyomino.md)] and [[convex-polyomino-by-area](pages/convex-polyomino-by-area.md)] - the stacks as the convex polyominoes that contain both bottom corners of their bounding box, and their place among the parallelogram, directed convex and convex polyominoes by area.
- [[steep-polyominoes-q-motzkin-bessel](pages/steep-polyominoes-q-motzkin-bessel.md)] - steep parallelogram polyominoes, whose generating function is a quotient of q-Bessel functions. After Example I.8, Flajolet and Sedgewick point to the q-Bessel functions that count the parallelogram polyominoes by area.[^9]

## Footnotes

[^1]: [[analytic-combinatorics-ch1-ogfs](pages/analytic-combinatorics-ch1-ogfs.md)] Example I.8 pp. 45-46 - "A stack polyomino is the diagram of a composition such that for some j, ℓ, one has 1 ≤ x_1 ≤ x_2 ≤ … ≤ x_j ≥ x_{j+1} ≥ … ≥ x_ℓ ≥ 1 ... The diagram representation of stack polyominoes [k ⟼ P^{1,…,k−1} × Z^k × P^{1,…,k}] translates immediately into the OGF S(z) = ∑_{k≥1} z^k/(1−z^k) · 1/((1−z)(1−z²)···(1−z^{k−1}))² ... a bona fide algorithm for computing the initial values of the number of stack polyominoes (EIS A001523): S(z) = z + 2z² + 4z³ + 8z⁴ + 15z⁵ + 27z⁶ + 47z⁷ + 79z⁸ + ⋯."
[^2]: https://oeis.org/A001523 (read 2026-10-16) - "Number of stacks, or planar partitions of n; also number of weakly unimodal compositions of n", `1, 1, 2, 4, 8, 15, 27, 47, 79, 130, …` from `n = 0`. The series `St(z)` and enumeration of the unimodal compositions agree with these terms for `n ≤ 16`, and `St(z)` with the OEIS terms for `n ≤ 20` (Python 3.11, 2026-10-16).
[^3]: [[bender-1974-convex-n-ominoes](pages/bender-1974-convex-n-ominoes.md)] p.220 §2 eq. (3) - "a trapezoid is defined by a sequence such that l_i ≤ l_{i+1} and r_i ≥ r_{i+1}. Let T(x, y) be the generating function for trapezoids such that the number with n cells and base length b is the coefficient of x^n y^b ... T(x, y) = Σ_{k=1}^∞ x^k y(1 − x^k y) / Π_{n=1}^k (1 − x^n y)^2."
[^4]: [[bender-1974-convex-n-ominoes](pages/bender-1974-convex-n-ominoes.md)] pp.222-223 §4 - "Since T(x, 1) has radius of convergence 1 which exceeds r, it follows that c(n) ~ 2c*(n)."
[^5]: [[column-convex-polygon-enumeration](pages/column-convex-polygon-enumeration.md)] `bousquet-melou-1996-column-convex-polygons.txt` §2.3 L500-525, pp. 10-11 (formulas read from the PDF) - Lemma 2.4 "S(s) = xstyq/(1 − styq) + x/(1 − syq)² S(sq)", "Applying construction A to the set of stack polygons provides all the stack polygons of width at least 2", and Lemma 2.5 "S(s, t, x, y, q) = sty Σ_{n≥1} x^n q^n/((syq)²_{n−1}(1 − styq^n))", "Proof. Apply Lemma 2.3." Lemma 2.5 agrees with enumeration of the polygons with nested columns through area 7 (Python 3.11, 2026-10-16).
[^6]: [[algebraic-languages-and-polyominoes-enumeration](pages/algebraic-languages-and-polyominoes-enumeration.md)] pp.180-181 §3 (16)-(18), Lemma 3.2 [synthesis] - "writing the letter 'a' (respectively the factor xx) each time one meets a North or South step (respectively an East step)"; delete "the first and last letter of w, and a factor xx ... between the pth and (p+1)st a's"; "The number of stack polyominoes with perimeter 2n+4 is the Fibonacci number F_{2n} with generating function (1-t^2)/((1-t-t^2)(1+t-t^2))."
[^7]: Verified by execution (Python 3.11, 2026-10-16): the antidiagonal sums of `C(2h + w − 3, w − 1)` equal `F_{2n+1}` for `1 ≤ n ≤ 14`; `A001519` checked on oeis.org.
[^8]: [[algebraic-languages-and-polyominoes-enumeration](pages/algebraic-languages-and-polyominoes-enumeration.md)] p.204 §12(8) - "This has been done for stack polyominoes [42] and parallelogram polyominoes [30, 12, 18]", with [42] = E.M. Wright, "Stacks", Quart. J. Math. Oxford (2) 19 (1968) 313-320 in their reference list.
[^9]: [[analytic-combinatorics-ch1-ogfs](pages/analytic-combinatorics-ch1-ogfs.md)] p.46 - "For instance, related 'q–Bessel' functions appear in the enumeration of parallelogram polyominoes (Example IX.14, p. 660)."
