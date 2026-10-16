---
title: "Convex n-ominoes (Bender, 1974)"
category: Sources
summary: Bender's eight-page Discrete Math. paper on convex polyominoes counted by area. It computes the Klarner-Rivest growth constant gamma = 2.30913859330 (A276994) and the parallelogram asymptotic 0.29745 gamma^n (A006958), and writes the convex asymptotic c(n) ~ f gamma^n with f a residue (eq. (11)), whose value is A067675's 2.9195985097. Every convex polyomino is cut into an upright trapezoid, a parallelogram and an inverted trapezoid; the trapezoids are the stack polyominoes, which are the convex castles, and their series at y = 1 is A001523. A typical convex n-omino is a rod tilted 45 degrees, about 2.376 cells thick.
tags: [source, paper, polyomino, convex, parallelogram-polyomino, stack-polyomino, asymptotics, growth-constant, klarner-rivest, bender, discrete-math, a276994, a006958, a067675, a001523]
sources: [bender-1974-convex-n-ominoes]
created: 2026-09-22
updated: 2026-10-16
---

# Convex n-ominoes (Bender, 1974)

**Source:** raw/bender-1974-convex-n-ominoes.pdf, a local copy that is git-ignored and not in every clone; the quotations in the footnotes were taken from it and were not re-read for the current version of this page.
**Publication:** Edward A. Bender, "Convex n-ominoes," Discrete Mathematics 8 (1974) 219-226, doi:10.1016/0012-365X(74)90134-4. Received 19 April 1973; original version received 13 February 1973.[^1]
**Date ingested:** 2026-09-22
**Type:** paper

## Summary

Klarner and Rivest ([[klarner-rivest-1974-convex-n-ominoes](pages/klarner-rivest-1974-convex-n-ominoes.md)]) had defined a convex animal (every horizontal or vertical line meets it in an interval) and shown that `c(n)^{1/n}` tends to a constant `γ`, with an effective procedure for computing it; here `c(n)` is the number of convex polyominoes of area `n`. Bender sharpens this to `c(n) ~ f γ^n` and describes the typical shape.[^2] The building blocks are two row-by-row families, with `l_i` and `r_i` the left and right ends of row `i`. A **trapezoid** has each row inside the one below (`l_i ≤ l_{i+1}`, `r_i ≥ r_{i+1}`). A **parallelogram** slanting to the right has both row ends moving weakly right (`l_i ≤ l_{i+1} < r_i ≤ r_{i+1}`).[^3] Using Klarner's Fredholm-integral method, Bender gets the trapezoid generating function in closed form and the parallelogram one as a ratio `P = P_1/(1 − P_2)` of two alternating q-series (the paper's `P`, the parallelogram series by area; not the signed tower count of the wiki).[^4]

The growth constant is `1/r`, where `r` is the first pole of the parallelogram series: the simple root of `P_2(x, 1, 1) = 1`. Because `P_2` is an alternating series with decreasing terms, truncating it brackets the root, and ten terms give `γ = 2.30913859330`.[^5] The same pole gives `p(n) ~ 0.29745 γ^n` parallelograms of area `n` slanting one way, and `2p(n) ~ 0.59491 γ^n` counting both slants.[^6]

Bender cuts a convex polyomino at the rows `I = max{i : l_i > l_{i+1}}` and `J = min{j : r_{j−1} > r_j}` (Fig. 1 of the paper). The result is two trapezoids, one upright and one inverted, with a parallelogram between them. The trapezoid series has radius of convergence 1, larger than `r`, so asymptotically only the parallelogram part matters, and `c(n) ~ 2c*(n)`, where `c*(n)` counts the convex n-ominoes with a nonempty middle slanting to the northeast.[^7] A residue computation expresses the prefactor `f` in closed form (eq. (11)), and a local limit theorem gives the shape: the height of a parallelogram is asymptotically normal, so a typical convex n-omino is a thin rod tilted 45 degrees.[^8]

## Key Takeaways

- **`γ = 2.30913859330`**, from the first ten terms of (5b).[^5] It agrees with A276994, "the Klarner-Rivest polyomino constant" (`2.3091385933304947...`), in every printed digit.[^9]
- **Parallelograms: `p(n) ~ 0.29745 γ^n`** (7a), and `2p(n) ~ 0.59491 γ^n` for both slants (7b).[^6] A006958's constant is `0.29745350581112...`.[^9]
- **The convex prefactor.** Equation (11) writes `f = 2K²/(r P_1(r, 1, 1, 1) P_2′(r, 1, 1))`, a residue at the parallelogram pole.[^10] With Bender's sum for `K` evaluated, it gives `2.9195985097136`, A067675's constant ([[convex-castle-cap-factor](pages/convex-castle-cap-factor.md)]),[^9] and the exact counts give `c(40)/γ^40 = 2.91962` ([[convex-polyomino-by-area](pages/convex-polyomino-by-area.md)]). Bousquet-Mélou and Fédou quote `C ≃ 2.67564` for this prefactor, citing this paper and Klarner-Rivest; that value is not the constant of the counts ([[bousquet-melou-fedou-1995-convex-polyominoes](pages/bousquet-melou-fedou-1995-convex-polyominoes.md)]).
- **Parallelogram share.** Parallelograms of both slants make up the fraction `2p(n)/c(n) → 0.59491/2.91960 = 0.2038` of the convex polyominoes of area `n`.
- **Trapezoids are stacks.** Equation (3) at `y = 1` is[^4]

  ```
  T(x, 1)  =  Σ_{k≥1} x^k (1 − x^k) / Π_{n≤k} (1 − x^n)²  =  Σ_{k≥1} x^k / ((1 − x^k) Π_{n<k} (1 − x^n)²),
  ```

  the stack-polyomino series A001523, `1, 2, 4, 8, 15, 27, 47, 79, 130, 209, …`, checked through area 20.[^11] (`T` here is the paper's trapezoid series, not the tower count `T(k, L)`.) The rows of a trapezoid are nested above its bottom row, so its columns stand on the bottom row with a unimodal skyline: a trapezoid is a stack polyomino, and so a [[convex-castle](pages/convex-castle.md)].
- **Typical shape.** The height of a random parallelogram of area `n` is asymptotically normal, with mean `0.42088n` and variance `0.20806n`, so the average width is `n/μ_n = 2.37597`.[^12] The exact counts reproduce both slopes (0.42088 and 0.20806 between areas 100 and 120).[^11] For the base (bottom row) of a parallelogram the paper gives mean `2.06030` and variance `0.57609`.[^13] The mean agrees with the exact counts, `2.0603013436`, but the variance of the base length computed from the counts is `1.7054123579` at areas 60 and 90, so `0.57609` is not the variance of the base length ([[convex-castle-cap-factor](pages/convex-castle-cap-factor.md)]).[^11] For convex polyominoes only the bases change, since that is where the trapezoids attach; there the base mean is `K^{−1}` times a coefficient `3.13352`.[^13] Bender states, without proof, that every row away from the ends likely has mean length equal to the average width.[^14] The slope is within `f(n)` of 45 degrees for almost all parallelograms whenever `f(n)/√n → ∞`.[^15]

## Entities & Concepts

- [[convex-polyomino](pages/convex-polyomino.md)] - the class Bender counts, with Bender's cut into two trapezoids and a parallelogram (section *Bender's three pieces*).
- [[convex-polyomino-by-area](pages/convex-polyomino-by-area.md)] - the convex, directed convex, parallelogram and stack polyominoes counted by area, with the growth constant `γ` and their prefactors.
- [[stack-polyomino-gf](pages/stack-polyomino-gf.md)] - the stack series, Bender's trapezoid series at `y = 1`.
- [[convex-castle](pages/convex-castle.md)] - the stacks as castles: each trapezoid of Bender's cut is a convex castle, upright or upside down.
- [[klarner-rivest-1974-convex-n-ominoes](pages/klarner-rivest-1974-convex-n-ominoes.md)] - the paper this one sharpens: the same cut (their stacks are these trapezoids) and the same `γ`, bracketed there by kernel truncations.
- [[bousquet-melou-fedou-1995-convex-polyominoes](pages/bousquet-melou-fedou-1995-convex-polyominoes.md)] - the exact generating function of convex polyominoes, whose series gives the prefactor `2.9195985097`.
- [[algebraic-languages-and-polyominoes-enumeration](pages/algebraic-languages-and-polyominoes-enumeration.md)] - a three-piece cut along vertical lines, graded by perimeter.
- [[bender-1974-partitions-of-multisets](pages/bender-1974-partitions-of-multisets.md)] - Bender's other 1974 Discrete Math. paper, whose "blocks" are blocks of a partition.
- [[convex-castle-cap-factor](pages/convex-castle-cap-factor.md)] - Bender's `K = 1.07524…` and eq. (11) evaluated, the cap factor `κ = K/P_1(r) = 2.21532…`, and the three prefactors `p`, `pκ` and `2pκ²` of the parallelogram, directed convex and convex polyominoes.
- [[steep-polyominoes-q-motzkin-bessel](pages/steep-polyominoes-q-motzkin-bessel.md)] - steep polyominoes and q-Bessel functions; Bender's `P_1` and `1 − P_2` are the parallelogram q-Bessel series `J_1` and `J_0` at unit weights.

## Relation to Other Wiki Pages

- **Castle tie.** A convex polyomino is an upright and an upside-down convex castle glued to the ends of a parallelogram. The castle pieces have radius of convergence 1 and carry none of the exponential growth, which comes from the parallelogram.
- **Exact generating functions.** Bender gives asymptotics, and an exact generating function only for `c*(n)`, written as a constant-term extraction (8). The exact generating functions of the directed convex and convex polyominoes are Bousquet-Mélou and Fédou's ([[bousquet-melou-fedou-1995-convex-polyominoes](pages/bousquet-melou-fedou-1995-convex-polyominoes.md)]).
- **What Klarner and Rivest did not use.** Klarner and Rivest had the parallelogram area series as a ratio of alternating q-series (their (19)), wrote that they were "unable to make use of (19) in estimating p(n)", and bracketed `γ` with kernel truncations ([[klarner-rivest-1974-convex-n-ominoes](pages/klarner-rivest-1974-convex-n-ominoes.md)]). Bender gets `P = P_1/(1 − P_2)` by adapting their procedure, and because `P_2` alternates with decreasing terms, ten terms give eleven digits.[^4][^5]

## Footnotes

[^1]: [[bender-1974-convex-n-ominoes](pages/bender-1974-convex-n-ominoes.md)] p.219 - "DISCRETE MATHEMATICS 8 (1974) 219-226 ... Received 19 April 1973 ... Original version received 13 February 1973."
[^2]: [[bender-1974-convex-n-ominoes](pages/bender-1974-convex-n-ominoes.md)] p.219 §1 - "Klarner and Rivest [4] have defined a convex animal to be an animal such that every intersection with a vertical or horizontal line is a (possibly empty) interval ... Klarner and Rivest showed that c(n)^{1/n} ~ γ and found an effective procedure for calculating γ. We will study the typical shape of convex animals and obtain improved asymptotic results for c(n)."
[^3]: [[bender-1974-convex-n-ominoes](pages/bender-1974-convex-n-ominoes.md)] p.220 §2 - "a trapezoid is defined by a sequence such that l_i ≤ l_{i+1} and r_i ≥ r_{i+1}. A parallelogram (to the right) is defined by a sequence such that l_i ≤ l_{i+1} < r_i ≤ r_{i+1}."
[^4]: [[bender-1974-convex-n-ominoes](pages/bender-1974-convex-n-ominoes.md)] pp.220-221 §2 eqs. (3), (5a), (5b), (6) [synthesis] - applies "the method of [3]" (Klarner's Fredholm-integral formula) to get T(x, y) as the sum (3) and P as P_1 + P_1 P_2/(1 - P_2), "a simple adaptation of the procedure Klarner and Rivest used to obtain P(x, 1, y, 1)."
[^5]: [[bender-1974-convex-n-ominoes](pages/bender-1974-convex-n-ominoes.md)] pp.221-222 §3 - "It was shown in [4] that γ = r^{-1}, where r is the radius of convergence of P(x) ... Because the series (5b) for P_2(x, 1, 1) is an alternating series with strictly decreasing terms ... upper and lower bounds can be found ... by truncating the series ... We found r^{-1} = γ = 2.30913859330 by using the first ten terms in (5b)."
[^6]: [[bender-1974-convex-n-ominoes](pages/bender-1974-convex-n-ominoes.md)] p.222 §3 eqs. (7a), (7b) - "p(n) ~ 0.29745γ^n since the pole is simple. The total number of parallelograms is asymptotic to 2p(n) ~ 0.59491γ^n."
[^7]: [[bender-1974-convex-n-ominoes](pages/bender-1974-convex-n-ominoes.md)] pp.222-223 §4 and Fig. 1 - "Let c*(n) be the number of convex n-ominoes with J > I + 1, i.e., those animals with a non-empty parallelogram part slanting to the northeast. Since T(x, 1) has radius of convergence 1 which exceeds r, it follows that c(n) ~ 2c*(n)."
[^8]: [[bender-1974-convex-n-ominoes](pages/bender-1974-convex-n-ominoes.md)] p.219 abstract - "When viewed from a distance, most convex n-ominoes resemble rods tilted 45° from the vertical with horizontal (and vertical) thickness roughly equal to 2.37597."
[^9]: https://oeis.org/A276994, https://oeis.org/A006958, https://oeis.org/A067675 (read 2026-10-16) - A276994 "Decimal expansion of the Klarner-Rivest polyomino constant", "2.309138593330494731..."; A006958 "a(n) ~ c * d^n ... c = 0.29745350581112195107..."; A067675 "c = 2.91959850971360705538...".
[^10]: [[bender-1974-convex-n-ominoes](pages/bender-1974-convex-n-ominoes.md)] p.224 eq. (11) - "(11) f = 2K^2/(rP_1(r, 1, 1, 1)P_2'(r, 1, 1))".
[^11]: Verified by execution (Python 3.11, 2026-10-16): the trapezoid series at `y = 1` against weakly unimodal compositions through area 20 (A001523); parallelograms by area from the transfer `min(a_i, a_{i+1})` between consecutive row lengths (A006958 through area 11 checked), with the height mean and variance slopes `0.4208810` and `0.2080627` between areas 100 and 120, and the base-length mean `2.0603013436` and variance `1.7054123579` at areas 60 and 90; `0.59491/2.91960 = 0.2038`. The convex counts and `c(40)/γ^40 = 2.91962` are on [[convex-polyomino-by-area](pages/convex-polyomino-by-area.md)].
[^12]: [[bender-1974-convex-n-ominoes](pages/bender-1974-convex-n-ominoes.md)] pp.224-225 §5 - "the probability that the height is less than h_n converges to a normal distribution with mean μ_n ~ 0.42088n and variance σ_n^2 ~ 0.20806n ... the average width is n/μ_n ~ 2.37597."
[^13]: [[bender-1974-convex-n-ominoes](pages/bender-1974-convex-n-ominoes.md)] p.225 §5 and pp.225-226 §6 - "the base has mean and variance μ(n) = p_1(n)/p_0(n) ~ 2.06030, σ^2(n) = p_2(n)/p_0(n) − μ(n)^2 ~ 0.57609"; for convex animals "All the results are the same except for the length of the bases to which the trapezoids are attached", with "c_k(n)/c_0(n) ~ K^{-1} C(y^0, P_1^{[k]}(r, 1, 1, y^{-1})S(r, y))" and "In particular C(y^0, P_1^{[1]}(r, 1, 1, y^{-1})S(r, y)) = ... = 3.13352".
[^14]: [[bender-1974-convex-n-ominoes](pages/bender-1974-convex-n-ominoes.md)] p.226 §6 - "it is likely that all widths except those near the top and bottom have a mean equal to the average width. I have not been able to prove this."
[^15]: [[bender-1974-convex-n-ominoes](pages/bender-1974-convex-n-ominoes.md)] p.225 §5 - "if f(n)/√n → ∞, then the fraction of parallelograms whose slope is within ±f(n) of ±45° goes to 1 as n → ∞."
