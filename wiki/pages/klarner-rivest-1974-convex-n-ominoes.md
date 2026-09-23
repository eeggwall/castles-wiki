---
title: "Asymptotic Bounds for the Number of Convex n-Ominoes (Klarner & Rivest 1974)"
category: Sources
summary: Klarner and Rivest prove that the number c(n) of convex n-ominoes has a growth constant gamma = lim c(n)^{1/n}, show it equals the parallelogram constant by trisecting every convex polyomino into stack + parallelogram + stack, and squeeze it to gamma = 2.309138... with separable kernel truncations of a Fredholm-type integral equation for parallelograms counted by area. The source of the name "Klarner-Rivest constant" (A276994) and of the stack-as-convex-building-block picture.
tags: [paper, source, polyomino, convex, parallelogram-polyomino, stack-polyomino, row-convex, area, growth-constant, integral-equation, q-analog]
sources: [klarner-rivest-1974-convex-n-ominoes]
created: 2026-09-22
updated: 2026-09-23
---

# Asymptotic Bounds for the Number of Convex n-Ominoes (Klarner & Rivest 1974)

**Source:** `raw/klarner-rivest-1974-convex-n-ominoes.txt` (hand transcription of the scanned PDF, which has no usable text layer), from D. A. Klarner and R. L. Rivest, "Asymptotic bounds for the number of convex n-ominoes", *Discrete Mathematics* 8 (1974) 31-40. The local scan is `_klarner1974.pdf` (not tracked).
**Date ingested:** 2026-09-22
**Type:** paper (10 pp.)

## Summary

The paper answers a question Donald Knuth put to the authors: how fast does the number `c(n)` of convex n-ominoes grow?[^1] An n-omino here is a fixed polyomino (translations identified), and convex means every row and every column is one connected strip.[^2] The comparison points at the time were the row-convex count `b(n)`, with rational generating function and growth `beta = 3.20...`, and the count `t(n)` of all polyominoes, whose limit `theta` was then known only to lie in `3.72 < theta < 4.65`.[^3]

The first result is structural. Cutting a convex polyomino along two rows splits it into an upper **stack**, a middle **parallelogram** and a lower (upside-down) stack (Fig. 2).[^4] Here a stack has a left boundary that climbs right and a right boundary that climbs left (Wright's stacks, `s(3) = 4`), and a parallelogram has both boundaries climbing right.[^5] Stacks inject into parallelograms, parallelograms are supermultiplicative (`p(m)p(n) <= p(m+n)`), and gluing the three pieces back loses at most a polynomial factor. So `p(n) <= c(n) <= (n+2)^4 p(n)`, and convex and parallelogram polyominoes share one growth constant `gamma`.[^6]

The second result is numerical. Parallelograms counted by area are a transfer sum over consecutive row lengths with kernel `f(m, n) = min{m, n}` (the number of ways to stack a row of `n` on a row of `m` so that both boundaries climb right). That turns the area generating function into the solution of Klarner's contour-integral equation, whose theory "runs parallel to that of the Fredholm integral equation".[^7] The exact solution is an explicit ratio of alternating q-series (19), which the authors could not use for estimates.[^8] Instead they bracket the kernel. Truncating `min{m, n}` to `m, n <= k` gives separable lower bounds, and capping it the other way gives separable upper bounds. Each bound makes the generating function rational, so the growth constant is squeezed between the largest real roots of two explicit polynomial families (`Q_k` by a determinant and recurrence, `D_k` by a second recurrence).[^9] Table 1 runs `k = 1..10`, and the conclusion is `gamma = 2.309138...`.[^10]

## Key Takeaways

- **Existence and equality.** `lim c(n)^{1/n} = lim p(n)^{1/n} = gamma`, by the stack-parallelogram-stack trisection and `c(n) <= (n+2)^4 p(n)`.[^6]
- **Stacks are the thin part.** Stacks sit at both ends of every convex polyomino and inject into parallelograms (`s(n) <= p(n)`), so they add only a polynomial factor.[^4][^5] That fits the wiki's picture of stacks as subexponential ([[convex-polyomino-by-area](pages/convex-polyomino-by-area.md)]).
- **Parallelograms by area = a row-to-row transfer with kernel `min{m, n}`.** `F(x, y) = xy/((1-x)(1-y)(1-xy))` and `G(x) = x/(1-x)`. Iterating the resulting functional equation `B(x, y) = xy/(1-xy) + xy/(1-xy)^2 (B(x, 1) - B(x, xy))` gives the q-series (19) for `sum p(n) x^n`.[^7][^8] Re-expanded during this ingest, (19) gives `1, 2, 4, 9, 20, 46, 105, 242, 557, 1285, ...` (A006958).[^11]
- **Two-sided bounds from separable kernels.** Lower bounds `gamma_k` are the largest real roots of `Q_k(1/x)`, with `Q_k = (1 - x^{k-1} - x^k) Q_{k-1} - x^{2k-2} Q_{k-2}`. Upper bounds `beta_k` are the largest real roots of `D_k(1/x)`. The lower bound has settled at `2.30913859` by `k = 5`, and the upper bound reaches `2.30913864` at `k = 10`.[^9][^10]
- **Result:** `gamma = 2.309138...`.[^10] OEIS A276994 names this the Klarner-Rivest polyomino constant (see [[convex-polyomino-by-area](pages/convex-polyomino-by-area.md)] for its full digits and the q-Bessel zero it is the reciprocal of).

## Checked during ingest

All by execution on 2026-09-22 (own computation, not from the paper):

- The determinant (21) with entries `min(i, j)` and diagonal `i - x^i` reproduces `Q_2, Q_3, Q_4` as printed, and recurrence (22) matches the determinant through `k = 7`.
- Recurrence (31) with `Q_1 = x`, `Q_2 = 2x^2 - x^3` inserted in (30) reproduces `D_1, D_2, D_3` as printed.
- The largest real roots of `Q_k(1/x)` for `k = 1..5` and of `D_k(1/x)` for `k = 1..10` reproduce Table 1 to the printed eight decimals, except `beta_5` and `beta_6`, which come out one unit higher in the last place (`2.30934712`, `2.30917791`).
- **Misprint in (1).** The paper prints the row-convex generating function as `x(1-x)^3/(1 - 4x + 7x^2 - 5x^3)` with `beta` the largest real root of `y^3 - 4y^2 + 7y - 5`.[^12] That cubic's only real root is `1.5698`, while `y^3 - 5y^2 + 7y - 4` has real root `3.2056`, matching the paper's own `beta = 3.20...` and Hickerson's recurrence `a(n) = 5a(n-1) - 7a(n-2) + 4a(n-3)` ([[counting-horizontally-convex-polyominoes](pages/counting-horizontally-convex-polyominoes.md)]). The denominator should read `1 - 5x + 7x^2 - 4x^3`, as the wiki already has it on [[convex-polyomino-by-area](pages/convex-polyomino-by-area.md)].

## Entities & Concepts

- [[convex-polyomino](pages/convex-polyomino.md)] - the object counted; the paper's trisection realizes the corner taxonomy as a gluing.
- [[stack-polyomino-gf](pages/stack-polyomino-gf.md)] / [[convex-castle](pages/convex-castle.md)] - the paper's stacks, which the wiki identifies with convex castles.
- [[convex-polyomino-by-area](pages/convex-polyomino-by-area.md)] - the area ladder, on which the parallelogram and convex rungs carry this paper's `gamma`.
- [[horizontally-convex-polyomino](pages/horizontally-convex-polyomino.md)] / [[column-convex-polyomino](pages/column-convex-polyomino.md)] - the row-convex comparison family `b(n)`, A001169.
- [[polyominoes](pages/polyominoes.md)] - the general polyomino count `t(n)` and its constant `theta`.
- [[bender-1974-convex-n-ominoes](pages/bender-1974-convex-n-ominoes.md)], [[bousquet-melou-fedou-1995-convex-polyominoes](pages/bousquet-melou-fedou-1995-convex-polyominoes.md)], [[algebraic-languages-and-polyominoes-enumeration](pages/algebraic-languages-and-polyominoes-enumeration.md)] - the three later papers that build on this one (below).
- [[parallelogram-polyomino-dyck-bijection](pages/parallelogram-polyomino-dyck-bijection.md)] - the Dyck-word reading of the kernel `min{m, n}`.

## Relation to Other Wiki Pages

The paper is the primary source for the growth constant on [[convex-polyomino-by-area](pages/convex-polyomino-by-area.md)]. Its trisection gives a proof-level reason why the stack rung (convex castles, A001523) is subexponential while the rungs above it are not: every convex polyomino is a parallelogram with a stack glued to each end.

For castles by area the useful object is the kernel `min{m, n}`. It is a row-to-row transfer operator on the area-graded count, which is the castle's transfer-matrix idea with the finite matrix replaced by an infinite kernel. The paper's lower-bound truncation `F_k` keeps only rows of length at most `k`, which is a finite `k x k` transfer matrix, and `gamma_k` is an algebraic number (a root of `Q_k(1/x)`). That makes `gamma` a limit of algebraic numbers from below and above, a concrete handle on the open question for this constant on [[algebraic-transcendental-wall](pages/algebraic-transcendental-wall.md)] (this reading is this wiki's, not the paper's).

The companion constant in the same paragraph is `theta` for all polyominoes (Klarner's constant). This paper records the 1974 bounds, `3.72` below (Klarner 1967) and `4.65` above (Klarner and Rivest 1973).[^3] The `3.87 < K < 4.65` quoted on [[column-convex-polygon-enumeration](pages/column-convex-polygon-enumeration.md)] bounds the same constant after a later improvement of the lower end. The upper end is the same 1973 number.[^13]

**What the three later papers did with it.**

- **Bender** ([[bender-1974-convex-n-ominoes](pages/bender-1974-convex-n-ominoes.md)]) adapted this paper's procedure to write the parallelogram series as `P_1/(1 - P_2)`. He then truncated the alternating series `P_2` directly, which gave `gamma = 2.30913859330` and `p(n) ~ 0.29745 gamma^n` out of the kind of series (19) that this paper could not use for estimates. The convex prefactor `2.67564` that later papers attribute to "Bender, and Klarner and Rivest" is Bender's. This paper gives no prefactor, and OEIS A067675 gives `2.91960`.
- **Bousquet-Mélou and Fédou** ([[bousquet-melou-fedou-1995-convex-polyominoes](pages/bousquet-melou-fedou-1995-convex-polyominoes.md)]) credit this paper as the first to give the area generating function of parallelograms.[^14] Their `X = y J_1/J_0` at `x = y = 1` and this paper's (19) both expand to A006958.
- **Delest and Viennot** ([[algebraic-languages-and-polyominoes-enumeration](pages/algebraic-languages-and-polyominoes-enumeration.md)]) cite this paper. Their trisection cuts along the vertical lines through two extreme boundary points rather than along rows, so their stacks stand "up to 90° rotation".
- **The kernel is a Dyck-word statistic** (own reasoning). Under Delest-Viennot's bijection β, peak heights are the parallelogram's column heights, and the trough between peaks of heights `m` and `n` can take any of `min{m, n}` values ([[parallelogram-polyomino-dyck-bijection](pages/parallelogram-polyomino-dyck-bijection.md)]). So the `min{m, n}` transfer sum counts Dyck words by the sum of their peak heights, grouped by peak-height sequence.[^15]
- **The recursion is a q-shift equation** (own reasoning). `B(x, y) = xy/(1-xy) + xy/(1-xy)^2 (B(x, 1) - B(x, xy))` relates `B` at `y` to `B` at `xy`. It is a one-unknown instance of the systems on [[q-differential-system](pages/q-differential-system.md)], 21 years before the three-block convex system. It is also the shape of Lemma 2.3 of [[column-convex-polygon-enumeration](pages/column-convex-polygon-enumeration.md)], one shift and no derivative term, whose parallelogram theorem credits this paper with the area case.[^16]

## Footnotes

[^1]: [[klarner-rivest-1974-convex-n-ominoes](pages/klarner-rivest-1974-convex-n-ominoes.md)] p.32 §1 L59-61 - "Recently, Donald Knuth wrote us and asked us if the number c(n) of convex n-ominoes had been investigated. This paper is entirely motivated by Knuth's question."
[^2]: [[klarner-rivest-1974-convex-n-ominoes](pages/klarner-rivest-1974-convex-n-ominoes.md)] p.31 Abstract L16-21 - "Two n-ominoes are considered the same if one is mapped onto the other by some translation of the plane. An n-omino is convex if all cells in a row or column form a connected strip."
[^3]: [[klarner-rivest-1974-convex-n-ominoes](pages/klarner-rivest-1974-convex-n-ominoes.md)] p.32 §1 [synthesis] L40-58 - `t(n)^{1/n} -> theta` with "the best lower bound (given in [3]) is 3.72 < theta, while the best upper bound (given in [5]) is theta < 4.65"; row-convex `b(n)` has the rational GF (1) and `b(n)^{1/n}` "tends to a limit beta ... beta = 3.20...".
[^4]: [[klarner-rivest-1974-convex-n-ominoes](pages/klarner-rivest-1974-convex-n-ominoes.md)] p.32-33 §2 L69-80 - "A convex n-omino may be split into three parts by making two cuts between certain rows so that the upper and lower parts are roughly trapezoids and the middle part is roughly a parallelogram ... Fig. 2. Trisection of a convex 28-omino."
[^5]: [[klarner-rivest-1974-convex-n-ominoes](pages/klarner-rivest-1974-convex-n-ominoes.md)] p.33 §2 L82-90 - "A convex n-omino whose left boundary climbs to the right and whose right boundary climbs to the left corresponds to a partition of n called a stack by Wright [9] ... s(3) = 4. A convex n-omino whose left and right boundaries both climb to the right is called a parallelogram ... s(n) <= p(n) for all n".
[^6]: [[klarner-rivest-1974-convex-n-ominoes](pages/klarner-rivest-1974-convex-n-ominoes.md)] p.33-34 §2 [synthesis] L89-124 - supermultiplicativity `p(m)p(n) <= p(m+n)` gives (2); "every convex n-omino splits into two stacks and one parallelogram" gives (3) `c(n) <= ... <= (n+2)^4 p(n)`; (4)-(5) conclude `lim c(n)^{1/n} = lim p(n)^{1/n} = gamma`.
[^7]: [[klarner-rivest-1974-convex-n-ominoes](pages/klarner-rivest-1974-convex-n-ominoes.md)] p.35-36 §3 [synthesis] L151-202 - the contour equation (10), "The theory of (10) runs parallel to that of the Fredholm integral equation"; "the number of (m+n)-celled parallelograms having m cells in one row and n cells in a second row is (13) f(m, n) = min{m, n}"; (15) `F(x, y) = xy/((1-x)(1-y)(1-xy))`, (16) `G(x) = x/(1-x)`, and the reduced form (17).
[^8]: [[klarner-rivest-1974-convex-n-ominoes](pages/klarner-rivest-1974-convex-n-ominoes.md)] p.36-37 §3 L204-220 - the iterated solution (18) and its `y = 1` form (19); "We have been unable to make use of (19) in estimating p(n)."
[^9]: [[klarner-rivest-1974-convex-n-ominoes](pages/klarner-rivest-1974-convex-n-ominoes.md)] §4-5 [synthesis] L226-339 - truncated kernel (20) and determinant (21), recurrence (22), `gamma_k` "the largest real root of Q_k(1/x) = 0"; capped kernel (23)-(24), the system (25)-(28), and `beta_k` "the largest real root of D_k(1/x) = 0", computed "using the Newton-Raphson method".
[^10]: [[klarner-rivest-1974-convex-n-ominoes](pages/klarner-rivest-1974-convex-n-ominoes.md)] p.38 Table 1 L253-270 and p.40 (32) L342-344 - "the sequence (gamma_i) converges very quickly to the value 2.30913859..., our best lower bound for gamma"; `beta_10 = 2.30913864`; "(32) gamma = lim_{n->oo} (c(n))^{1/n} = 2.309138...".
[^11]: [[klarner-rivest-1974-convex-n-ominoes](pages/klarner-rivest-1974-convex-n-ominoes.md)] p.37 (19) [synthesis] L211-217 - the ratio of alternating q-series; series-expanded by execution during ingest (2026-09-22) through `x^13`, agreeing with the parallelogram column of [[convex-polyomino-by-area](pages/convex-polyomino-by-area.md)].
[^12]: [[klarner-rivest-1974-convex-n-ominoes](pages/klarner-rivest-1974-convex-n-ominoes.md)] p.32 (1) L53-58 - "(1) x(1-x)^3 / (1 - 4x + 7x^2 - 5x^3) = sum b(n) x^n ... the largest real root of y^3 - 4y^2 + 7y - 5 = 0; that is, beta = 3.20...".
[^13]: https://oeis.org/A001168 (fetched 2026-09-22) - "The currently best-known lower and upper bounds on this constant are 3.9801 (Barequet et al., 2006) and 4.6496 (Klarner and Rivest, 1973), respectively."
[^14]: [[bousquet-melou-fedou-1995-convex-polyominoes](pages/bousquet-melou-fedou-1995-convex-polyominoes.md)] p.56 L153-184 [synthesis] - the parallelogram generating function (1) was first obtained "by Klarner and Rivest" for area, then refined by Delest-Fédou, Brak-Guttmann and Bousquet-Mélou-Viennot.
[^15]: Verified by execution, 2026-09-22 (own computation): summing `prod_i min(a_i, a_{i+1})` over all compositions `(a_1, ..., a_k)` of `n` gives `1, 2, 4, 9, 20, 46, 105, 242, 557, 1285, ...` through `n = 20`, which is A006958 and matches the parallelogram column of [[bousquet-melou-fedou-1995-convex-polyominoes](pages/bousquet-melou-fedou-1995-convex-polyominoes.md)] Table 1 (`5526198` at `n = 20`).
[^16]: [[column-convex-polygon-enumeration](pages/column-convex-polygon-enumeration.md)] `bousquet-melou-1996-column-convex-polygons.txt` p.12 Remark (2) after Theorem 3.2 L587-588 - "Special important cases of this theorem were proved by Klarner and Rivest [22] (area generating function)"; Lemma 2.3 at L459-461, "X(s) = xe(s) + xf(s)X(1) + xg(s)X(sq)".
