---
title: Stack polyomino generating function
category: Concepts
summary: A stack polyomino — column heights that weakly rise then weakly fall around a single peak — is a castle tower with one peak. Its OGF `S(z) = ∑_{k≥1} z^k/(1−z^k) · 1/((1−z)(1−z²)···(1−z^{k−1}))²` (OEIS A001523) is built directly by the [[symbolic-method]] from a Durfee-square-style geometric decomposition.
tags: [concept, polyomino, stack-polyomino, generating-functions, symbolic-method, durfee-square, castle-tower]
sources: [analytic-combinatorics-ch1-ogfs, klarner-rivest-1974-convex-n-ominoes, algebraic-languages-and-polyominoes-enumeration, bender-1974-convex-n-ominoes]
created: 2026-09-15
updated: 2026-09-23
---

# Stack polyomino generating function

## Description

A **stack polyomino** is the diagram of a composition whose column heights weakly rise to a single peak and then weakly fall: `1 ≤ x_1 ≤ x_2 ≤ … ≤ x_j ≥ x_{j+1} ≥ … ≥ x_ℓ ≥ 1` for some `j, ℓ`.[^1] Read this as a castle-style pile of columns on a common baseline where the skyline is unimodal — a **single-peak tower**. Flajolet & Sedgewick construct its ordinary generating function (OGF) directly by the [[symbolic-method](pages/symbolic-method.md)] (Example I.8, pp. 45-46 of [[analytic-combinatorics-ch1-ogfs](pages/analytic-combinatorics-ch1-ogfs.md)]), from the Durfee-square-style geometric decomposition[^1]

```
Stack ≅ ⋃_{k≥1} ( SEQ_{≥1}(Z^k) × P^{1..k−1} × P^{1..k−1} )
```

— identify the (fixed) peak column of height `k`, prepend a partition with parts `≤ k−1` (the ascending side) and append another (the descending side). Translating each piece into an OGF via the dictionary gives[^1]

```
S(z) = ∑_{k≥1}  z^k/(1 − z^k)  ·  1/((1−z)(1−z²)···(1−z^{k−1}))²

     = z + 2z² + 4z³ + 8z⁴ + 15z⁵ + 27z⁶ + 47z⁷ + 79z⁸ + …
```

= **Online Encyclopedia of Integer Sequences (OEIS) A001523** (unimodal compositions).[^1] Coefficients confirmed against A001523 during ingest.

## The direct castle tie

A **castle tower** — the tower half of the wiki's [[castle-polyomino](pages/castle-polyomino.md)], as counted by the unsigned tower OGF `E_k(x) = 1/(1−(k+1)x)` on [[project-euler-502-representations](pages/project-euler-502-representations.md)] — has strictly more freedom than a stack polyomino: castle blocks can rise and fall repeatedly across width, so the skyline is a general unrestricted composition, not a unimodal one. In other words:

- **Stack polyominoes are the unimodal-skyline sub-family of castle towers.** Every stack polyomino, positioned on a full-width base and constrained to castle heights, is a castle tower with one peak. Not every castle tower is a stack polyomino — a castle whose skyline dips in the middle and rises again is not unimodal.
- **The construction style matches the wiki's approach.** [[column-convex-polyomino](pages/column-convex-polyomino.md)] and the castle both build the polyomino by gluing columns; Example I.8 is exactly this style, executed as a specification rather than an add-a-column functional equation.
- **The add-a-column route, by perimeter and area.** [[column-convex-polygon-enumeration](pages/column-convex-polygon-enumeration.md)] uses stacks as its worked example. Applying its construction A to stacks gives a one-shift q-equation in the left-column-height variable (Lemma 2.4), and its Lemma 2.3 solves that in closed form (Lemma 2.5). So the wiki has three constructions of one class: this specification, the Fibonacci-word coding by perimeter below, and the q-shift equation.[^8]

This is the closest Analytic Combinatorics (AC)-native construction to the castle we have so far: it treats a castle-like polyomino as a *specification* over classes of columns, and reads the OGF off the specification without ever writing a recurrence.

## Relation to convex-castle counting

The [[convex-castle](pages/convex-castle.md)] is the castle with a unimodal skyline, and it is exactly a stack polyomino. On a unimodal skyline every row is a single run, so the no-overhang and same-row-gap rules hold automatically, and the only castle rule left is PE 502's even-block clause, which is a parity filter (a convex castle has exactly `h` blocks). One class, three gradings: `C(2H+W−3, W−1)` by bounding box ([[convex-castle-binomial-identity](pages/convex-castle-binomial-identity.md)]), A001523 by area (this OGF), and Fibonacci by perimeter (below).

## By perimeter: Fibonacci words (Delest-Viennot)

Stack polyominoes graded by **perimeter** have a simpler count than by area. Delest and Viennot code a stack of perimeter `2n+4` by a *Fibonacci word*. Follow the upper boundary from the bottom-left corner to the bottom-right corner, writing `a` for each vertical step and `xx` for each East step. Then delete the first and last `a` and one `xx` from the top plateau. The result is a word of length `2n` in `{a, xx}*` with an even number of `a`'s, and there are `F_{2n}` such words (`F_0 = F_1 = 1`):[^3]

```
Σ_n F_{2n} t^{2n} = (1 - t^2) / ((1 - t - t^2)(1 + t - t^2))      1, 2, 5, 13, 34, 89, ...
```

The perimeter of a stack in a `w × h` box is `2(w+h)`, and stacks are the [[convex-castle](pages/convex-castle.md)] shapes. So this count is the anti-diagonal sum `Σ_{w+h=n+2} C(2h+w-3, w-1) = F_{2n}` of the convex-castle binomial (checked for `n = 1..14` during ingest).[^4] The two gradings of the same class give A001523 by area and Fibonacci (A001519) by semi-perimeter. The joint area-and-perimeter GF is Wright's "Stacks" (1968), which Delest-Viennot cite as the solved q-analog for this class but which is not ingested here.[^5]

## Stacks inside every convex polyomino

Bender's 1974 count of convex polyominoes uses stacks under the name **trapezoids**: rows each lying inside the row below (`l_i <= l_{i+1}`, `r_i >= r_{i+1}`), counted by area and base length as[^6]

```
T(x, y) = sum_{k>=1} x^k y (1 - x^k y) / prod_{n=1..k} (1 - x^n y)^2
```

At `y = 1` the factor `(1 - x^k)` cancels one copy of the last denominator factor, which leaves `S(z)` above term by term. The coefficients agree with A001523 through area 20 (own check). Nested rows over a full bottom row are the same thing as a unimodal skyline of columns on that row, so a trapezoid is a stack polyomino as drawn. Every convex polyomino is a bottom trapezoid, a parallelogram, and an inverted top trapezoid ([[convex-polyomino](pages/convex-polyomino.md)]), so the stack series is a factor in every convex polyomino's generating function. It contributes no exponential growth: `T(x, 1)` has radius of convergence 1, and the growth `2.30914^n` comes from the parallelogram.[^7]

## Related asymptotics thread

The book's own note (p. 46) points from Example I.8 forward to Example IX.14 p. 660: **parallelogram polyominoes counted by area give a q-Bessel generating function** — the same q-Bessel / q-Motzkin thread that appears in [[steep-polyominoes-q-motzkin-bessel](pages/steep-polyominoes-q-motzkin-bessel.md)] and [[polyominoes](pages/polyominoes.md)]'s Ferrers-diagram remark on q-Bessel / q-Catalan.[^2] The stack polyomino is thus a middle link between the AC symbolic-method construction of a castle-shaped polyomino and the q-graded asymptotic story that the wiki has begun tracking separately.

## Appearances in Sources

- [[analytic-combinatorics-ch1-ogfs](pages/analytic-combinatorics-ch1-ogfs.md)] — Example I.8 pp. 45-46, "The Durfee square of partitions and stack polyominoes."
- [[klarner-rivest-1974-convex-n-ominoes](pages/klarner-rivest-1974-convex-n-ominoes.md)] p.33 - Wright's stacks, `s(3) = 4`, injected into parallelograms (`s(n) <= p(n)`); every convex polyomino is two stacks glued to the ends of a parallelogram, which is why stacks cost only a polynomial factor in the convex count.
- [[algebraic-languages-and-polyominoes-enumeration](pages/algebraic-languages-and-polyominoes-enumeration.md)] - Lemma 3.2: stacks by perimeter are Fibonacci words; stacks are the two outer pieces of every convex polyomino's trisection.
- [[bender-1974-convex-n-ominoes](pages/bender-1974-convex-n-ominoes.md)] - the same series as Bender's trapezoid generating function (3), the end pieces of his convex-polyomino decomposition.

## Related Concepts

- [[symbolic-method](pages/symbolic-method.md)] — the method the OGF is derived by.
- [[polyominoes](pages/polyominoes.md)] / [[column-convex-polyomino](pages/column-convex-polyomino.md)] — the taxonomic hosts.
- [[castle-polyomino](pages/castle-polyomino.md)] / [[tower-heap](pages/tower-heap.md)] — the castle tower, of which the stack polyomino is the unimodal-skyline sub-family.
- [[convex-castle](pages/convex-castle.md)] - the castle's own skyline-convex sub-family, the same class as the stack polyominoes (even-block clause aside).
- [[steep-polyominoes-q-motzkin-bessel](pages/steep-polyominoes-q-motzkin-bessel.md)] — the downstream q-Bessel thread the book points to.
- [[generating-functions](pages/generating-functions.md)] — the concept page.
- [[convex-polyomino](pages/convex-polyomino.md)], [[convex-polyomino-by-area](pages/convex-polyomino-by-area.md)] - stacks as the two-bottom-corner convex polyominoes, and their place on the area ladder below parallelogram, directed convex, and convex.

## Footnotes

[^1]: [[analytic-combinatorics-ch1-ogfs](pages/analytic-combinatorics-ch1-ogfs.md)] Example I.8 pp. 45-46 — "A stack polyomino is the diagram of a composition such that for some j, ℓ, one has 1 ≤ x_1 ≤ x_2 ≤ … ≤ x_j ≥ x_{j+1} ≥ … ≥ x_ℓ ≥ 1 ... The diagram representation of stack polyominoes ... translates immediately into the OGF S(z) = ∑_{k≥1} z^k/(1−z^k) · 1/((1−z)(1−z²)···(1−z^{k−1}))² ... a bona fide algorithm for computing the initial values of the number of stack polyominoes (EIS A001523): S(z) = z + 2z² + 4z³ + 8z⁴ + 15z⁵ + 27z⁶ + 47z⁷ + 79z⁸ + ⋯." Values confirmed against OEIS A001523 during ingest.
[^2]: [[analytic-combinatorics-ch1-ogfs](pages/analytic-combinatorics-ch1-ogfs.md)] p.46 — "The book of van Rensburg [592] describes many such constructions and their relation to models of statistical physics, especially polyominoes. For instance, related 'q-Bessel' functions appear in the enumeration of parallelogram polyominoes (Example IX.14, p. 660)."
[^3]: [[algebraic-languages-and-polyominoes-enumeration](pages/algebraic-languages-and-polyominoes-enumeration.md)] pp.180-181 §3 (16)-(18), Lemma 3.2 [synthesis] - "writing the letter 'a' (respectively the factor xx) each time one meets a North or South step (respectively an East step)"; delete "the first and last letter of w, and a factor xx ... between the pth and (p+1)st a's"; "The number of stack polyominoes with perimeter 2n+4 is the Fibonacci number F_{2n} with generating function (1-t^2)/((1-t-t^2)(1+t-t^2))."
[^4]: [[algebraic-languages-and-polyominoes-enumeration](pages/algebraic-languages-and-polyominoes-enumeration.md)] p.178 [synthesis] - stack polyomino defined by "S(P) = W'(P) and S'(P) = E(P)" (full bottom edge), which with a unimodal top is the convex-castle shape; the anti-diagonal identity is own reasoning, verified numerically n = 1..14 during ingest.
[^5]: [[algebraic-languages-and-polyominoes-enumeration](pages/algebraic-languages-and-polyominoes-enumeration.md)] p.204 §12(8) - "This has been done for stack polyominoes [42] and parallelogram polyominoes [30, 12, 18]", with [42] = E.M. Wright, "Stacks", Quart. J. Math. Oxford (2) 19 (1968) 313-320 (cited via Delest-Viennot, not read).
[^6]: [[bender-1974-convex-n-ominoes](pages/bender-1974-convex-n-ominoes.md)] p.220 §2 eq. (3) - "a trapezoid is defined by a sequence such that l_i ≤ l_{i+1} and r_i ≥ r_{i+1}. Let T(x, y) be the generating function for trapezoids such that the number with n cells and base length b is the coefficient of x^n y^b ... T(x, y) = Σ_{k=1}^∞ x^k y(1 − x^k y) / Π_{n=1}^k (1 − x^n y)^2."
[^7]: [[bender-1974-convex-n-ominoes](pages/bender-1974-convex-n-ominoes.md)] pp.222-223 §4 - "Since T(x, 1) has radius of convergence 1 which exceeds r, it follows that c(n) ~ 2c*(n)."
[^8]: [[column-convex-polygon-enumeration](pages/column-convex-polygon-enumeration.md)] `bousquet-melou-1996-column-convex-polygons.txt` §2.3 L500-525 - "Example: stack polygons ... Lemma 2.4. Let S(s, t, x, y, q) be the generating function for stack polygons ... Proof. Applying construction A to the set of stack polygons provides all the stack polygons of width at least 2 ... Lemma 2.5. The generating function S(s, t, x, y, q) for stack polyominoes is given by (4) ... Proof. Apply Lemma 2.3."
