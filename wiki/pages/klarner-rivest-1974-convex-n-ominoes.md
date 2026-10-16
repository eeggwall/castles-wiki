---
title: "Asymptotic Bounds for the Number of Convex n-Ominoes (Klarner & Rivest 1974)"
category: Sources
summary: Klarner and Rivest prove that c(n)^{1/n} converges, for the number c(n) of convex polyominoes of area n, to the same limit gamma as for the parallelogram polyominoes, by cutting every convex polyomino into a stack, a parallelogram and an upside-down stack (c(n) <= (n+2)^4 p(n)). They count parallelograms by area as a transfer sum with kernel min{m, n}, and bound gamma between the largest roots of two families of polynomials from separable truncations of that kernel, concluding gamma = 2.309138... The paper gives no asymptotic prefactor. OEIS A276994 names gamma the Klarner-Rivest polyomino constant.
tags: [paper, source, polyomino, convex, parallelogram-polyomino, stack-polyomino, row-convex, area, growth-constant, integral-equation, q-analog]
sources: [klarner-rivest-1974-convex-n-ominoes]
created: 2026-09-22
updated: 2026-10-16
---

# Asymptotic Bounds for the Number of Convex n-Ominoes (Klarner & Rivest 1974)

**Source:** `raw/klarner-rivest-1974-convex-n-ominoes.txt`, a hand transcription of the scanned paper, which has no usable text layer: D. A. Klarner and R. L. Rivest, "Asymptotic bounds for the number of convex n-ominoes", *Discrete Mathematics* 8 (1974) 31-40. The scan is the PDF on Rivest's publications page (https://people.csail.mit.edu/rivest/pubs/KR74.pdf), with a local copy in the git-ignored `assets/`; equation (1) and the cubic on p. 32, and `Q_2`, `Q_3`, `Q_4` and Table 1 on p. 38, were read from it and agree with the transcription.
**Date ingested:** 2026-09-22
**Type:** paper (10 pp.)

## Summary

The paper answers a question Donald Knuth put to the authors: how fast does the number `c(n)` of convex n-ominoes grow?[^1] An n-omino is a polyomino of area `n` taken up to translation, and it is convex when every row and every column is one strip of cells.[^2] The comparison families at the time were the row-convex polyominoes, `b(n)` of area `n` with growth constant `β = 3.20…`, and all polyominoes, `t(n)` of area `n`, whose growth constant `θ` was known to lie in `3.72 < θ < 4.65`.[^3]

The paper prints the row-convex generating function (1) as `x(1 − x)^3/(1 − 4x + 7x² − 5x³)`, and `β` as "the largest real root of `y³ − 4y² + 7y − 5 = 0`; that is, `β = 3.20…`" (p. 32); the transcription copies both. The two printed polynomials have the coefficients 4 and 5 exchanged. The printed denominator gives the coefficients `1, 1, 0, −3, …`, and the printed cubic has only one real root, `1.5698…`, beside a complex pair of modulus `1.7847…`, so the printed `β = 3.20…` is not a root of it. The row-convex generating function is `x(1 − x)^3/(1 − 5x + 7x² − 4x³)`, A001169, and `β = 3.2055694304…` is the largest root of `y³ − 5y² + 7y − 4`, the value the paper states ([[horizontally-convex-polyomino](pages/horizontally-convex-polyomino.md)]).[^3][^4]

**The trisection.** Cutting a convex polyomino along two rows splits it into an upper **stack**, a middle **parallelogram** and a lower upside-down stack (Fig. 2).[^5] A stack has a left boundary that climbs to the right and a right boundary that climbs to the left, so its columns stand on its bottom row with a unimodal skyline (Wright's stacks; `s(3) = 4`). A parallelogram has both boundaries climbing to the right.[^6] Stacks inject into parallelograms (`s(n) ≤ p(n)`), parallelograms are supermultiplicative (`p(m)p(n) ≤ p(m + n)`), and gluing the three pieces back gives[^7]

```
c(n)  ≤  2n² Σ_{(i,j,k)} s(i) p(j) s(k)  ≤  2n² C(n + 2, 2) p(n)  ≤  (n + 2)^4 p(n),        (3)
```

the sum over the compositions `(i, j, k)` of `n` into non-negative parts. With `p(n) ≤ c(n)`, the limits of `c(n)^{1/n}` and `p(n)^{1/n}` exist and are equal; call the common limit `γ`.[^7]

**The kernel.** The parallelograms with rows of `m` and `n` cells number `f(m, n) = min{m, n}`, and those with row lengths `a_1, …, a_k` number `f(a_1, a_2) f(a_2, a_3) ⋯ f(a_{k−1}, a_k)` (14).[^8] Klarner's theory of 1968 (reference [4] of the paper) turns such a transfer sum into a contour-integral equation that "runs parallel to that of the Fredholm integral equation" (10). The paper writes `B(x, y)` for the generating function with `x` marking area and `y` the length of the first row; the wiki writes `Π(x, y)`, since `B(x, y)` is the castle generating function by width and blocks. With `F(x, y) = xy/((1 − x)(1 − y)(1 − xy))` and `G(x) = x/(1 − x)`, the equation becomes[^8]

```
Π(x, y)  =  xy/(1 − xy)  +  xy/(1 − xy)² · ( Π(x, 1) − Π(x, xy) ),                    (17)
```

whose iteration gives `Π(x, 1) = Σ p(n) x^n` as a ratio of two alternating q-series (19). Expanded, (19) gives `p(n) = 1, 2, 4, 9, 20, 46, 105, 242, 557, 1285, …` for `n = 1, 2, …`, which is A006958(n). The authors write that they could not use (19) to estimate `p(n)`.[^9]

**The bounds.** Truncating the kernel to `m, n ≤ k` gives a lower bound `F_k` for `F`, and the generating function becomes rational with a denominator `Q_k(x)`, the determinant (21) with entries `min(i, j)` and diagonal `i − x^i`, which satisfies

```
Q_k(x)  =  (1 − x^{k−1} − x^k) Q_{k−1}(x) − x^{2k−2} Q_{k−2}(x),        Q_0 = 1,  Q_1 = 1 − x.        (22)
```

The lower bounds `γ_k` are the largest real roots of `Q_k(1/x)`. Capping the kernel the other way gives separable upper bounds; the generating function is again rational, with a denominator `D_k = 1 − 3x + x² + x²V_1 + ⋯ + x^{k+1}V_k` (30), where `V_{r+1} = (2x − x^{r+1})V_r − x²V_{r−1}`, `V_1 = x`, `V_2 = 2x² − x³` (31). The paper writes `Q_r` for `V_r`, a second use of the letter. The upper bounds `β_k` are the largest real roots of `D_k(1/x)`.[^10] Table 1 runs `k = 1, …, 10`: the lower bound reaches `2.30913859` at `k = 5` and the upper bound `2.30913864` at `k = 10`, and the paper concludes `γ = 2.309138…` (32).[^11]

**What the paper does not give.** It proves that `c(n)^{1/n}` converges to `γ` and bounds `γ`; it gives no asymptotic `c(n) ~ C γ^n` and no prefactor `C`. Bender's paper of the same year gives `p(n) ~ 0.29745 γ^n` and the form of the convex prefactor ([[bender-1974-convex-n-ominoes](pages/bender-1974-convex-n-ominoes.md)]); the exact series give `C = 2.9195985097…` (A067675). Bousquet-Mélou and Fédou attribute the asymptotic `C a^n` to Bender and to this paper together, and quote `C ≃ 2.67564`, which is not this constant ([[bousquet-melou-fedou-1995-convex-polyominoes](pages/bousquet-melou-fedou-1995-convex-polyominoes.md)]).[^12]

## Key Takeaways

- **One growth constant.** `lim c(n)^{1/n} = lim p(n)^{1/n} = γ`, by the trisection and (3).[^7]
- **Stacks are the thin part.** Stacks sit at both ends of every convex polyomino and contribute at most the factor in (3). They grow subexponentially: the stacks of area `n` are A001523(n) ~ `exp(2π√(n/3)) / (8·3^{3/4} n^{5/4})` ([[stack-polyomino-gf](pages/stack-polyomino-gf.md)]).[^13]
- **Parallelograms by area through the kernel `min{m, n}`**, Equation (17), and the q-series (19), whose coefficients are A006958.[^9]
- **Two-sided bounds from separable kernels**, the polynomials `Q_k` and `D_k`, give `γ = 2.309138…`; OEIS A276994 names `γ` the Klarner-Rivest polyomino constant, and [[convex-polyomino-by-area](pages/convex-polyomino-by-area.md)] gives its digits and the q-series zero whose reciprocal it is.[^11][^14]

## Checked by execution

On 2026-10-16 (Python 3.11 with SymPy):

- The determinant (21) agrees with the recurrence (22) for `k ≤ 7`, and gives `Q_2`, `Q_3`, `Q_4` as printed.
- The recurrence (31) with `V_1 = x`, `V_2 = 2x² − x³`, inserted in (30), gives `D_1`, `D_2`, `D_3` as printed.
- The largest real roots of `Q_k(1/x)` and `D_k(1/x)` for `k = 1, …, 10`, truncated to eight decimals, are every entry of Table 1 (rounded, `β_5` and `β_6` would end in `…712` and `…791`).
- The expansion of (19) agrees with the parallelograms enumerated by rows through area 9, and with A006958 through area 14; the row-length counts (14) and `f(m, n) = min{m, n}` agree with the enumeration.
- The expansions of the printed and the OEIS row-convex generating functions, and the roots of their denominators (section *Summary*).

## Entities & Concepts

- [[convex-polyomino](pages/convex-polyomino.md)] - the polyominoes counted, their sub-families by bounding-box corners, and the trisection.
- [[stack-polyomino-gf](pages/stack-polyomino-gf.md)], [[convex-castle](pages/convex-castle.md)] - the stacks, which are the convex castles.
- [[convex-polyomino-by-area](pages/convex-polyomino-by-area.md)] - the convex sub-families counted by area, with `γ` as the growth constant of the parallelogram, directed convex and convex counts.
- [[horizontally-convex-polyomino](pages/horizontally-convex-polyomino.md)], [[column-convex-polyomino](pages/column-convex-polyomino.md)] - the row-convex count `b(n)`, A001169.
- [[polyominoes](pages/polyominoes.md)] - the polyominoes in general, counted by `t(n)` with growth constant `θ`.
- [[parallelogram-polyomino-dyck-bijection](pages/parallelogram-polyomino-dyck-bijection.md)] - the kernel `min{m, n}` by columns, as a count of trough heights of Dyck words.
- [[bender-1974-convex-n-ominoes](pages/bender-1974-convex-n-ominoes.md)], [[bousquet-melou-fedou-1995-convex-polyominoes](pages/bousquet-melou-fedou-1995-convex-polyominoes.md)], [[algebraic-languages-and-polyominoes-enumeration](pages/algebraic-languages-and-polyominoes-enumeration.md)] - three later papers that use this one.

## Relation to Other Wiki Pages

The paper is the primary source for the growth constant on [[convex-polyomino-by-area](pages/convex-polyomino-by-area.md)]. The truncated kernel `F_k` counts the parallelograms with every row of at most `k` cells, a transfer sum over `k` row lengths, so each `γ_k` and each `β_k` is an algebraic number, and `γ` is their common limit.

The growth constant `θ` of all polyominoes is Klarner's constant. The paper records the bounds `3.72` (Klarner 1967) and `4.65` (Klarner and Rivest 1973).[^3] Bousquet-Mélou 1996 quotes `3.87 < K < 4.65` for the same constant ([[column-convex-polygon-enumeration](pages/column-convex-polygon-enumeration.md)]), and the OEIS entry for all polyominoes gives `3.9801` and `4.6496`, the upper bound being the 1973 one.[^15]

**Three later papers.**

- **Bender** ([[bender-1974-convex-n-ominoes](pages/bender-1974-convex-n-ominoes.md)]) writes the parallelogram series as `P_1/(1 − P_2)` and truncates the alternating series `P_2`, which gives `γ = 2.30913859330` and `p(n) ~ 0.29745 γ^n` from series of the kind of (19).
- **Bousquet-Mélou and Fédou** ([[bousquet-melou-fedou-1995-convex-polyominoes](pages/bousquet-melou-fedou-1995-convex-polyominoes.md)]) credit this paper with the first area generating function of parallelograms.[^12] Their `y J_1/J_0` at width and height weight 1 and this paper's (19) both expand to A006958.
- **Delest and Viennot** ([[algebraic-languages-and-polyominoes-enumeration](pages/algebraic-languages-and-polyominoes-enumeration.md)]) cut along the vertical lines through two extreme boundary points instead of along rows, so their stacks stand "up to 90° rotation".

Equation (17) has the form `X(s) = x e(s) + x f(s) X(1) + x g(s) X(sq)` of Lemma 2.3 of Bousquet-Mélou 1996, with `s = y`, `q = x`, `e(s) = s/(1 − xs)`, `f(s) = s/(1 − xs)²` and `g(s) = −s/(1 − xs)²`; that paper credits this one with the area case of its parallelogram theorem ([[column-convex-polygon-enumeration](pages/column-convex-polygon-enumeration.md)]).[^16]

## Footnotes

[^1]: [[klarner-rivest-1974-convex-n-ominoes](pages/klarner-rivest-1974-convex-n-ominoes.md)] p.32 §1 L59-61 - "Recently, Donald Knuth wrote us and asked us if the number c(n) of convex n-ominoes had been investigated. This paper is entirely motivated by Knuth's question."
[^2]: [[klarner-rivest-1974-convex-n-ominoes](pages/klarner-rivest-1974-convex-n-ominoes.md)] p.31 Abstract L16-21 - "Two n-ominoes are considered the same if one is mapped onto the other by some translation of the plane. An n-omino is convex if all cells in a row or column form a connected strip."
[^3]: [[klarner-rivest-1974-convex-n-ominoes](pages/klarner-rivest-1974-convex-n-ominoes.md)] p.32 §1 L40-58 - "the best lower bound (given in [3]) is 3.72 < theta, while the best upper bound (given in [5]) is theta < 4.65"; "(1) x(1-x)^3 / (1 - 4x + 7x^2 - 5x^3) = sum_{n>=1} b(n) x^n ... beta which is equal to the largest real root of y^3 - 4y^2 + 7y - 5 = 0; that is, beta = 3.20...".
[^4]: https://oeis.org/A001169 (read 2026-10-16) - "Number of board-pile polyominoes with n cells", "G.f.: x*(1-x)^3/(1 - 5*x + 7*x^2 - 4*x^3)", and the limit ratio "3.20556943040... = A246773"; the printed denominator expanded and its roots computed (Python 3.11, 2026-10-16).
[^5]: [[klarner-rivest-1974-convex-n-ominoes](pages/klarner-rivest-1974-convex-n-ominoes.md)] p.32-33 §2 L69-80 - "A convex n-omino may be split into three parts by making two cuts between certain rows so that the upper and lower parts are roughly trapezoids and the middle part is roughly a parallelogram ... Fig. 2. Trisection of a convex 28-omino."
[^6]: [[klarner-rivest-1974-convex-n-ominoes](pages/klarner-rivest-1974-convex-n-ominoes.md)] p.33 §2 L82-91 - "A convex n-omino whose left boundary climbs to the right and whose right boundary climbs to the left corresponds to a partition of n called a stack by Wright [9] ... s(3) = 4. A convex n-omino whose left and right boundaries both climb to the right is called a parallelogram ... s(n) <= p(n) for all n".
[^7]: [[klarner-rivest-1974-convex-n-ominoes](pages/klarner-rivest-1974-convex-n-ominoes.md)] p.33-34 §2 L89-124 [synthesis] - supermultiplicativity `p(m)p(n) <= p(m+n)` gives (2); "every convex n-omino splits into two stacks and one parallelogram" gives (3); (4)-(5) conclude `lim c(n)^{1/n} = lim p(n)^{1/n} = gamma`.
[^8]: [[klarner-rivest-1974-convex-n-ominoes](pages/klarner-rivest-1974-convex-n-ominoes.md)] p.34-36 §3 L128-199 [synthesis] - the double sequence (6), the contour equation (10), "The theory of (10) runs parallel to that of the Fredholm integral equation"; "the number of (m+n)-celled parallelograms having m cells in one row and n cells in a second row is (13) f(m, n) = min{m, n}" and the product (14); (15) `F(x, y) = xy/((1-x)(1-y)(1-xy))`, (16) `G(x) = x/(1-x)`, and (17).
[^9]: [[klarner-rivest-1974-convex-n-ominoes](pages/klarner-rivest-1974-convex-n-ominoes.md)] p.36-37 §3 L201-220 - the iterated solution (18) and its `y = 1` form (19); "We have been unable to make use of (19) in estimating p(n)." https://oeis.org/A006958 (read 2026-10-16) - "Number of parallelogram polyominoes with n cells", offset 1.
[^10]: [[klarner-rivest-1974-convex-n-ominoes](pages/klarner-rivest-1974-convex-n-ominoes.md)] §4-5 L222-341 [synthesis] - truncated kernel (20) and determinant (21), recurrence (22), `gamma_k` "the largest real root of Q_k(1/x) = 0"; capped kernel (23)-(24), the system (25)-(28) with `B^k_r = P_r + Q_r B^k(x, 1)`, (30)-(31), and `beta_k` "the largest real root of D_k(1/x) = 0", computed "using the Newton-Raphson method".
[^11]: [[klarner-rivest-1974-convex-n-ominoes](pages/klarner-rivest-1974-convex-n-ominoes.md)] p.38 Table 1 L253-270 and p.40 (32) L342-344 - "the sequence (gamma_i) converges very quickly to the value 2.30913859..., our best lower bound for gamma"; `beta_10 = 2.30913864`; "(32) gamma = lim_{n->oo} (c(n))^{1/n} = 2.309138...".
[^12]: [[bousquet-melou-fedou-1995-convex-polyominoes](pages/bousquet-melou-fedou-1995-convex-polyominoes.md)] p.56 L153-184 [synthesis] and p.59 L305-308 - the parallelogram generating function (1) was first obtained "by Klarner and Rivest" for area; "There exists also an asymptotic result simultaneously proved by Bender on the one hand, Klarner and Rivest on the other hand [2, 12]: the number of convex polyominoes of area n is asymptotically Ca^n, where C ≃ 2.67564 and a ≃ 2.30914"; https://oeis.org/A067675 (read 2026-10-16) - "a(n) ~ c * d^n, where d = A276994 ..., c = 2.91959850971360705...".
[^13]: https://oeis.org/A001523 (read 2026-10-16) - "a(n) ~ exp(2*Pi*sqrt(n/3)) / (8 * 3^(3/4) * n^(5/4)) [Auluck, 1951]".
[^14]: https://oeis.org/A276994 (read 2026-10-16) - "Decimal expansion of the Klarner-Rivest polyomino constant", 2.3091385933304947….
[^15]: https://oeis.org/A001168 (read 2026-10-16) - "The currently best-known lower and upper bounds on this constant are 3.9801 (Barequet et al., 2006) and 4.6496 (Klarner and Rivest, 1973), respectively."
[^16]: [[column-convex-polygon-enumeration](pages/column-convex-polygon-enumeration.md)] `bousquet-melou-1996-column-convex-polygons.txt` p.12 Remark (2) after Theorem 3.2 L587-588 - "Special important cases of this theorem were proved by Klarner and Rivest [22] (area generating function)"; Lemma 2.3 at L459-461, "X(s) = xe(s) + xf(s)X(1) + xg(s)X(sq)".
