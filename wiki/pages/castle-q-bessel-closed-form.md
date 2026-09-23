---
title: Castles by width, blocks and area - a sequence of parallelograms over q-Bessel series
category: Analyses
summary: "Grading the tower-word first-return grammar by area turns it into the q-shift equation E(u) = A/(1 - uA), A(u) = 1 - x + x E(uq), a Möbius recursion that linearizes to closed q-series. With u marking width, x blocks and q area, castles are Π/(1 - x - Π), where Π = y J_1/J_0 is the Bousquet-Mélou-Fédou parallelogram-polyomino GF (the Pólya q-Catalan family with width and height split) evaluated at width (1 - x)u and height x. Checked as an exact polynomial identity through area 12-13 against two independent enumerations. At x = -1, u = 1 the denominator is an explicit series M(q) analytic in the unit disk, so the signed castle count is meromorphic there; its zero q_0 = -0.6158281351848... reproduces the row-raising constants rho and C to 30 digits, and the next zero q_1 = -0.8202720 gives the correction O(0.7508^n). By descents, the zero-descent and all-descent cells are q-binomials, but the middle cells do not factor as q-Narayana times q-binomial."
tags: [analysis, castle, area, blocks, perimeter, q-analog, q-series, q-bessel, q-catalan, parallelogram-polyomino, grammar, functional-equation, q-shift, parity, sign, asymptotics, narayana, descents, q-binomial, novel-candidate]
sources: [bousquet-melou-fedou-1995-convex-polyominoes, project-euler-502-representations]
created: 2026-09-23
updated: 2026-09-23
---

# Castles by width, blocks and area

The [[generalized-dyck-grammar](pages/generalized-dyck-grammar.md)] counts towers by width and blocks. This page adds area to it. Graded by area, the grammar becomes a q-shift equation. The equation is a Möbius recursion, so it linearizes, and its solution is a ratio of q-Bessel series. The series are the ones Bousquet-Mélou and Fédou use for parallelogram polyominoes, and the castle generating function (GF) comes out as a sequence of parallelograms. That puts castles next to the Pólya q-Catalan family on [[q-catalan-numbers](pages/q-catalan-numbers.md)] and the q-Bessel ratios of [[steep-polyominoes-q-motzkin-bessel](pages/steep-polyominoes-q-motzkin-bessel.md)].

Everything on this page is own derivation, checked by execution. The ingredients are literature-standard: the `J_0, J_1` series and the parallelogram GF `Π = y J_1/J_0` are from [[bousquet-melou-fedou-1995-convex-polyominoes](pages/bousquet-melou-fedou-1995-convex-polyominoes.md)], and a `GF = Π̃/(1 - x - Π̃)` shape (bargraphs as a sequence of staircase excursions) is the standard first-return decomposition Feretić and Bousquet-Mélou use for column-convex polygons. The specific trivariate closed form here - `Π` evaluated at width `(1-x)u` and height `x`, and the signed `N(q)/M(q)` specialization - was not found in the bargraph-enumeration papers reachable from an informed literature check (Bousquet-Mélou 1996 "A method for the enumeration of various classes of column-convex polygons"; Prellberg-Brak 1995; Blecher-Brennan-Knopfmacher on bargraphs by perimeter and area, mid-2010s). No direct arXiv / MathSciNet retrieval was run.[^7]

## The graded grammar

A tower is empty, starts with a gap `R`, or starts with a peak `U V D`, where `V` is a nonempty tower sitting on a sub-block.[^1] Mark width by `u`, blocks by `x` and area (cells) by `q`. Two facts make the grading work:

- Area is a cell count, so raising a shape does not change it. The interior tower `V` keeps its own weight when it sits on the sub-block.
- The sub-block under `V` has width `width(V)`, so it contributes one block and `width(V)` cells. That is the substitution `u → uq` on `V`.

So a peak is `x (E(uq) - 1)`, the `-1` removing the width-0 tower, and the grammar `E = 1 + uE + P (1 + uE)` reads

```
E(u) = A(u) / (1 - u A(u)),        A(u) = 1 - x + x E(uq)
```

`E(u) = E(u, x, q)` counts towers (column heights `≥ 0`) with the empty tower as `1`. A castle is a tower with a full base block slid under it, so castles are `x (E(uq) - 1) = A(u) - 1`.

**Unsigned area alone carries no information.** At `x = 1`, `1/E(u) = 1/E(uq) - u` telescopes to `E = 1/(1 - u/(1 - q))`, every height vector counted once, which is the `2^(n-1)` compositions of [[castle-by-area](pages/castle-by-area.md)]. The area enters nontrivially only jointly with blocks, which are the perimeter ([[castle-perimeter](pages/castle-perimeter.md)]).

## Linearizing

Substituting `E(uq) = A(uq)/(1 - uq A(uq))` gives a Möbius map from `A(uq)` to `A(u)`:

```
A(u) = ((x - (1 - x) uq) A(uq) + (1 - x)) / (1 - uq A(uq))
```

Write `A = N/M`. The matrix recursion `(N, M)(u) = [[x - (1-x)uq, 1-x], [-uq, 1]] (N, M)(uq)` has coefficient recursions that close in one step, `n_k = -(1-x) q^k n_(k-1) / ((1 - q^k)(1 - x q^k))`. With `(a)_k = (1 - a)(1 - aq)...(1 - aq^(k-1))`:

```
N(u) = sum_{k>=0} (-1)^k (1-x)^k     q^C(k+1,2) u^k / ((q)_k (xq)_k)
M(u) = 1 + sum_{k>=1} (-1)^k (1-x)^(k-1) q^C(k+1,2) u^k / ((q)_k (xq)_(k-1))

castles(u, x, q) = N(u)/M(u) - 1,        towers E(u) = N(u) / (M(u) - u N(u))
```

## Castles are a sequence of parallelograms

Bousquet-Mélou and Fédou write the parallelogram GF (`x` width, `y` height, `q` area) as `y J_1/J_0`, with[^2]

```
J_0 = sum_{n>=0} (-1)^n x^n q^C(n+1,2) / ((q)_n (yq)_n)
J_1 = - sum_{n>=1} (-1)^n x^n q^C(n+1,2) / ((q)_(n-1) (yq)_n)
```

Put `X = (1 - x)u` in their width slot and `Y = x` in their height slot. Then `N = J_0(X, Y)` term by term, and `N - M = (Y/(1 - Y)) J_1(X, Y)`, because `(1-x)/(1 - xq^k) - 1 = -x(1 - q^k)/(1 - xq^k)`. Dividing through by `J_0`, with `Π = Y J_1/J_0` the parallelogram GF:

```
castles(u, x, q)  =  Π / (1 - x - Π),        Π = Π(width (1-x)u, height x, area q)

1 + castles  =  1 / (1 - Π~),     Π~ = sum over parallelograms p of  u^w(p) (1-x)^(w(p)-1) x^h(p) q^area(p)
```

So `1 + castles` is the sequence construction on parallelograms, each weighted `(1-x)^(w-1) x^h` in place of `x^h`. A width-1 parallelogram is a single column of height `h`. It gets weight `x^h q^h`, which is the height-`h` one-column castle with its `h` blocks. The signed weights say the correspondence is an inclusion-exclusion, not a bijection. A combinatorial reading of `(1-x)^(w-1)` as "each of the `w - 1` internal column joins either merges blocks or is cancelled" is a guess, not worked out. At `q = 1`, `Π` is the Narayana GF of parallelograms by width and height ([[parallelogram-polyomino-dyck-bijection](pages/parallelogram-polyomino-dyck-bijection.md)]), which is the same Narayana thread as [[tower-narayana-polynomial](pages/tower-narayana-polynomial.md)], now carried to all `q`.

This answers the q-Catalan question for castles. The q-analogue that castles meet is the Pólya/Gessel one, parallelograms by area, with width and height kept separate. Its q-Bessel denominator `J_0` is the numerator `N` of the castle GF. The castle denominator `M = J_0 - (Y/(1-Y)) J_1` is a second q-Bessel combination. The Carlitz inversion family does not appear in the formula.[^3]

**Checks.** `N/M - 1` equals brute force over all compositions of `n ≤ 13`, as bivariate series in `u` and `q`, at 15 integer values `x = -7..7`. Block counts are at most the area, so the coefficients are polynomials in `x` of degree `≤ 13`, and 15 values make this an exact identity through area 13. Independently, `Π/(1 - x - Π)` built from brute-force parallelograms (their area counts reproduce A006958) equals brute-force castles through area 12 at 13 values of `x`, again an exact identity to that order.[^4]

## The signed specialization

The block sign is `x = -1`. At `u = 1`, `(q)_k (-q)_k = (q^2; q^2)_k`, and

```
N(q) = sum_{k>=0} (-2)^k q^C(k+1,2) / (q^2; q^2)_k
M(q) = 1 + sum_{k>=1} (-1)^k 2^(k-1) q^C(k+1,2) / ((q^2; q^2)_(k-1) (1 - q^k))

sum_n (even(n) - odd(n)) q^n  =  N(q)/M(q) - 1
```

The series reproduce the row-raising recursion on [[castle-row-raising-equation](pages/castle-row-raising-equation.md)] at every `n ≤ 40` computed here.[^4] Both series converge in `|q| < 1`, so the signed count is **meromorphic in the unit disk**, and its singularities there are zeros of `M`. Counted by the argument principle, `M` has exactly one zero in `|q| < 0.8`, and 8 by `|q| = 0.84`:

```
q_0  = -0.615828135184805773627625720698      1/q_0 = -1.62382967400459366939460437601
C    = -N(q_0) / (q_0 M'(q_0)) = 0.0985091749731156224089366266361

q_1  = -0.82027198,   then  0.64813 ± 0.51516 i  (|q| = 0.82793),  -0.41543 ± 0.71641 i  (0.82815),  0.00215 ± 0.83183 i  (0.83183)
```

`q_0` and `C` agree with the row-raising values to all 30 digits. The second zero is real, so `even(n) - odd(n) = C (1/q_0)^n (1 + O((q_0/q_1)^n))` with `q_0/q_1 = 0.7508`. At `n = 300` that is `0.75^300 ≈ 3 × 10^(-38)`, which matches the `1.7 × 10^(-37)` spread of consecutive ratios seen there. In parallelogram terms, the pole is where `Π(width 2, height -1; q) = 2`: parallelograms weighted `2^w (-1)^h q^area` sum to 2. The digits of `q_1` are a novel-candidate constant, in line with `q_0` (not searched in OEIS).[^5]

## By descents: q-binomials at the ends only

At `q = 1`, towers of width `w` with `b` blocks and `k - 1` descents number `N(w,k) C(b+w-k, w-1)` ([[narayana-numbers](pages/narayana-numbers.md)]). With area:

- **`k = 1`** (weakly increasing, `c_w = b`): `q^b [b+w-1, w-1]_q`, a partition in a box.
- **`k = w`** (strictly decreasing, `c_1 = b`): `q^(b + C(w-1,2)) [b, w-1]_q`, distinct parts.
- **`1 < k < w`**: the cell polynomial divided by `[b+w-k, w-1]_q` is not a polynomial from `b = 2` on (`w = 3, 4`, `b ≤ 6`), so there is no `q`-Narayana × `q`-binomial factorization by area.

The width-`w` GF by blocks and area agrees. For `w = 3, 4` its reduced denominator is `(1 - qx) prod_{j=1..w} (1 - q^j x)`, which has a repeated `1 - qx` factor, and the numerator has negative coefficients. So there is no positive "`q`-Narayana over `prod (1 - q^j x)`" form.[^6] The descent-Narayana bijection, if one exists, does not carry area to a single statistic on the parallelogram side.

## Computation

Signed castles by area from the closed form (exact rationals, about a second):

```python
from fractions import Fraction
Q = 40                                              # castles by area to q^Q, u = 1
def smul(a, b): return [sum(a[i] * b[n - i] for i in range(n + 1)) for n in range(Q + 1)]
def sinv(a):                                        # a[0] != 0
    r = [Fraction(1, a[0])] + [0] * Q
    for n in range(1, Q + 1): r[n] = -sum(a[i] * r[n - i] for i in range(1, n + 1)) / a[0]
    return r
def poch(c, k):                                     # 1/(c q; q)_k as a q-series
    s = [1] + [0] * Q
    for i in range(1, k + 1):
        for n in range(i, Q + 1): s[n] += c * s[n - i]
    return s
def castles(x):                                     # N/M - 1 at u = 1, blocks weighted x
    N, M = [0] * (Q + 1), [1] + [0] * Q
    for k in range(Q + 1):
        e = k * (k + 1) // 2
        if e > Q: break
        a = smul(poch(1, k), poch(x, k))
        b = smul(poch(1, k), poch(x, k - 1)) if k else None
        for n in range(Q + 1 - e):
            N[n + e] += (-1) ** k * (1 - x) ** k * a[n]
            if k: M[n + e] += (-1) ** k * (1 - x) ** (k - 1) * b[n]
    P = smul(N, sinv(M)); P[0] -= 1
    return [int(c) for c in P]
print(castles(-1)[1:])                              # even - odd by area
```

## Open

- A combinatorial proof of `1 + castles = 1/(1 - Π~)`: which cancellations the `(1-x)^(w-1)` weights encode.
- A proof that `q_0` is the only zero of `M` in `|q| < 0.82` (the argument-principle count is numerical).
- The joint statistics the grammar also carries: area with peaks, and area with left-to-right records, graded the same way.

## Relation to other pages

- [[generalized-dyck-grammar](pages/generalized-dyck-grammar.md)] / [[tower-word-language](pages/tower-word-language.md)]: the grammar graded here.
- [[bousquet-melou-fedou-1995-convex-polyominoes](pages/bousquet-melou-fedou-1995-convex-polyominoes.md)]: the `J_0`, `J_1` series and the parallelogram GF `y J_1/J_0`.
- [[q-catalan-numbers](pages/q-catalan-numbers.md)] / [[motzkin-numbers](pages/motzkin-numbers.md)]: the q-analogue threads; castles meet the Pólya/Gessel family.
- [[steep-polyominoes-q-motzkin-bessel](pages/steep-polyominoes-q-motzkin-bessel.md)]: another polyomino family whose GF is a q-Bessel ratio.
- [[castle-row-raising-equation](pages/castle-row-raising-equation.md)]: the same signed series by recursion; this page gives its closed form and second singularity.
- [[castle-perimeter](pages/castle-perimeter.md)]: blocks are the vertical half-perimeter, so this is castles by width, perimeter and area.
- [[q-differential-system](pages/q-differential-system.md)]: the harder convex case, where the q-shift system does not close in one step.
- [[convex-polyomino-by-area](pages/convex-polyomino-by-area.md)]: the parallelogram rung and its `J_0` growth constant.

## Footnotes

[^1]: [[project-euler-502-representations](pages/project-euler-502-representations.md)] §"The grammar" L258-263, L276 - "Let E_k be the towers of height at most k ... E_k -> empty | R E_k | U V D ( empty | R E_k )"; "V is one row lower ... and V is nonempty."
[^2]: [[bousquet-melou-fedou-1995-convex-polyominoes](pages/bousquet-melou-fedou-1995-convex-polyominoes.md)] p.56 L153-184 and Appendix A p.72 L984-1131 [synthesis] - eq. (1) `X = y J_1/J_0`, "the quotient of two q-analogues of Bessel-like functions", and the `J_0`, `J_1` series as transcribed from the page images on that page.
[^3]: [[q-catalan-numbers](pages/q-catalan-numbers.md)] §"q-Catalan Numbers" L7-9 - "Carlitz q-Catalan numbers count inversions of Dyck Words and Catalan permutations ... Polya, Gessel ... count parallelogram polyominoes by area."
[^4]: Computed by execution, 2026-09-23: the `N/M - 1` series as exact integer series in `(u, q)` against all compositions of `n ≤ 13` with weight `x^blocks`, at `x = -7..7`; brute-force parallelograms (columns `[b_i, t_i]` with `b_i ≤ b_(i+1) ≤ t_i ≤ t_(i+1)`, area counts `1, 2, 4, 9, 20, 46, 105, 242, 557, 1285, 2964, 6842` = A006958) substituted into `Π/(1 - x - Π)` against castles through area 12 at `x = -6..7`, `x ≠ 1`; the computation block above, whose output equals the 40 listed terms on [[castle-row-raising-equation](pages/castle-row-raising-equation.md)].
[^5]: Computed by execution, 2026-09-23: `q_0` and `C` by mpmath `findroot` and numerical derivative at 30 digits; zero counts of `M` by the argument principle on circles `|q| = 0.6, 0.62, 0.7, 0.75, 0.8, 0.81, 0.82, 0.83, 0.84` (counts `0, 1, 1, 1, 1, 1, 1, 6, 8`); the zeros by Newton's method from a polar grid over `0.79 ≤ |q| ≤ 0.86`, series truncated at `k = 200`.
[^6]: Computed by execution, 2026-09-23: brute-force towers `w ≤ 4`, `b ≤ 6` by (blocks, descents, area), cells divided by `[b+w-k, w-1]_q` with sympy; width-`w` GF by blocks and area multiplied by `prod_l (1 - q^l x)^(w+1-l)` and reduced, `w = 3, 4`, blocks `≤ 14`.
[^7]: Literature status via a Synapse informed-opinion pass, 2026-09-23 (synapse: cited-via-not-read): "the building blocks are 100% literature-standard (Bousquet-Mélou-Fédou 1995, Bousquet-Mélou 1996, Prellberg-Brak 1995), but the specific trivariate closed form ... particularly with 'blocks' defined exactly as vertical half-perimeter and packaged as Π/(1-x-Π) ... I cannot confirm as appearing verbatim in any paper I know of. I'd treat it as likely new in this exact packaged form, built from well-known components." No arXiv or MathSciNet retrieval was run.
