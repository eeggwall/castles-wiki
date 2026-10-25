---
title: Castles by width, blocks and area - a sequence of parallelograms over q-Bessel series
category: Analyses
summary: "Graded by width u, blocks x and area q, the tower grammar gives E_∞(u) = B(u)/(1 − uB(u)) with B(u) = 1 − x + x E_∞(uq), where B(u) − 1 counts the castles. The recursion for B is a Möbius map, so B = N/M with explicit q-series N and M, and castles = N/M − 1 = Π/(1 − x − Π), where Π = Y J_1/J_0 is the parallelogram-polyomino series at width (1 − x)u and height x. Checked as an exact identity through area 13 and through area 12 against two enumerations. At x = −1, u = 1 the signed count of castles by area is N(q)/M(q) − 1 with M analytic in |q| < 1, so it is meromorphic there; the zero q_0 = −0.6158281351848... of M gives the growth constant and prefactor to 30 digits, and the next zero q_1 = −0.8202719776 gives the correction O(0.7508^n). Counted by descents, towers of width w give q-binomials in the cells with no descent and with w − 1 descents, and for w = 3, 4 the other cells are not multiples of the matching q-binomial."
tags: [analysis, castle, area, blocks, perimeter, q-analog, q-series, q-bessel, q-catalan, parallelogram-polyomino, grammar, functional-equation, q-shift, parity, sign, asymptotics, narayana, descents, q-binomial]
sources: [bousquet-melou-fedou-1995-convex-polyominoes, prellberg-brak-1995-cluster-models, column-convex-polygon-enumeration, project-euler-502-representations, aocp-generating-partitions]
created: 2026-09-23
updated: 2026-10-25
---

# Castles by width, blocks and area

The [[generalized-dyck-grammar](pages/generalized-dyck-grammar.md)] counts towers by width and blocks. This page grades it by area as well. The grammar becomes a q-shift equation whose recursion is a Möbius map, so it linearizes, and the castle generating function (GF) is a ratio of q-series. The series are those of the parallelogram polyominoes, and the castles come out as a sequence of parallelograms, counted with signed weights (Equation (5)). At block weight `−1` the closed form gives the signed count of castles by area and its singularities (section *The signed count by area*).

The derivation is the wiki's own, checked by execution. The series `J_0`, `J_1` and the parallelogram GF `Π = y J_1/J_0` are from [[bousquet-melou-fedou-1995-convex-polyominoes](pages/bousquet-melou-fedou-1995-convex-polyominoes.md)] and Theorem 3.2 of [[column-convex-polygon-enumeration](pages/column-convex-polygon-enumeration.md)]. Linearizing a q-shift equation by writing its unknown as a ratio of solutions of a linear one is the method that [[prellberg-brak-1995-cluster-models](pages/prellberg-brak-1995-cluster-models.md)] use for the functional equations of staircase, bar-graph and directed column-convex polygons; their §4 solves the staircase case and says the calculation "easily generalizes for the other models with quadratic functional equations".[^1] [[castle-add-a-column-equation](pages/castle-add-a-column-equation.md)] reaches the same `N/M` from the castles' linear add-a-column equation by Lemma 2.3 of Bousquet-Mélou 1996.

## The graded grammar

Mark width by `u`, blocks by `x` and area (cells) by `q`. A tower is empty, starts with a gap column `R`, or starts with a peak `U V D`, a block carrying nonempty towers `V`.[^2] Let `E_∞(u) = E_∞(u, x, q)` be the GF of all towers, of any height, with the empty tower counted as 1; it is the limit of the tower GFs `E_k` of [[castle-counting-formula](pages/castle-counting-formula.md)], now also graded by blocks and area. It is not the signed castle GF `E(q, z)` of [[castle-row-raising-equation](pages/castle-row-raising-equation.md)].

In a peak, the block under `V` is one block with `width(V)` cells, and `V` keeps its own weight. So a peak contributes `x (E_∞(uq) − 1)`: the substitution `u → uq` adds one cell for each column of `V`, and `−1` removes the empty tower. The grammar `E = 1 + uE + peak · (1 + uE)` then reads

```
E_∞(u)  =  B(u) / (1 − u B(u)),        B(u)  =  1 − x + x E_∞(uq).                       (1)
```

A castle is its towers with a bottom row of their width added, one block and one cell per column, so the castles have GF `x (E_∞(uq) − 1) = B(u) − 1`. So `B(u) = B(u, x, q)` is the castle GF with the empty castle counted once. At `x = 1` it is the unsigned castle GF `B(q, u)` of [[castle-row-raising-equation](pages/castle-row-raising-equation.md)], and at `x = −1` the signed one, `E(q, u)` there ([[castle-notation](pages/castle-notation.md)]).

**Area alone.** At `x = 1`, Equation (1) gives `1/E_∞(u) = 1/E_∞(uq) − u`, which telescopes to `E_∞(u) = 1/(1 − u/(1 − q))`: each column height is chosen independently. Then `B(1) − 1 = q/(1 − 2q)`, the `2^{n−1}` compositions of [[castle-by-area](pages/castle-by-area.md)]. The block count is the vertical half-perimeter ([[castle-perimeter](pages/castle-perimeter.md)]), and area enters nontrivially only together with it.

## Linearizing

Substituting `E_∞(uq) = B(uq)/(1 − uq B(uq))` into Equation (1) gives a Möbius map from `B(uq)` to `B(u)`:

```
B(u)  =  ( (x − (1 − x) uq) B(uq) + (1 − x) ) / ( 1 − uq B(uq) ).                         (2)
```

At `q = 1` Equation (1) is the fixed-point equation of the height map of the [[generalized-dyck-grammar](pages/generalized-dyck-grammar.md)] (section *Counts*), with `u` for width and `x` for blocks, and the matrix of Equation (2) has the trace `1 + x − u + ux` and the determinant `x` of that height step. The shift `u → uq` is what replaces its powers by q-series.

Write `B = N/M`, with `(N, M)(u) = [[x − (1 − x)uq, 1 − x], [−uq, 1]] (N, M)(uq)`. With `n_k`, `m_k` the coefficients of `u^k` in `N`, `M`, the two rows give `m_k (1 − q^k) = −q^k n_{k−1}` and `n_k (1 − x q^k) = −(1 − x) q^k n_{k−1} + (1 − x) q^k m_k`, so `n_k = −(1 − x) q^k n_{k−1} / ((1 − q^k)(1 − x q^k))`. With `n_0 = m_0 = 1` and `(a)_k = (1 − a)(1 − aq)⋯(1 − aq^{k−1})`:

```
N(u)  =  Σ_{k≥0} (−1)^k (1 − x)^k     q^{C(k+1,2)} u^k / ((q)_k (xq)_k)
M(u)  =  1 + Σ_{k≥1} (−1)^k (1 − x)^{k−1} q^{C(k+1,2)} u^k / ((q)_k (xq)_{k−1})            (3)

castles(u, x, q)  =  N(u)/M(u) − 1,        towers  E_∞(u)  =  N(u) / (M(u) − u N(u)).
```

## Castles are a sequence of parallelograms

Bousquet-Mélou and Fédou write the GF of the parallelogram polyominoes, with `X` marking width, `Y` height and `q` area, as `Π(X, Y) = Y J_1/J_0`, where[^3]

```
J_0(X, Y)  =  Σ_{n≥0} (−1)^n X^n q^{C(n+1,2)} / ((q)_n (Yq)_n)
J_1(X, Y)  =  Σ_{n≥1} (−1)^{n−1} X^n q^{C(n+1,2)} / ((q)_{n−1} (Yq)_n).
```

Put `X = (1 − x)u` and `Y = x`. Then `N = J_0` term by term, and `N − M = (Y/(1 − Y)) J_1`, because `(1 − x)/(1 − x q^k) − 1 = −x (1 − q^k)/(1 − x q^k)`. Dividing by `J_0`,

```
castles(u, x, q)  =  Π / (1 − x − Π),        Π  =  Π((1 − x)u, x),                         (4)

1 + castles  =  1 / (1 − Π̃),        Π̃  =  Σ_p  u^{w(p)} (1 − x)^{w(p)−1} x^{h(p)} q^{a(p)},     (5)
```

where the sum runs over the parallelogram polyominoes `p` with width `w(p)`, height `h(p)` and area `a(p)`. So `1 + castles` is the sequence construction on parallelograms, each weighted `(1 − x)^{w − 1} x^h`. A parallelogram of width 1 is a single column of height `h`, with weight `x^h q^h u`: the castle `(h)` with its `h` blocks. The weight `(1 − x)^{w − 1}` has negative coefficients, so Equation (5) is not a weight-preserving bijection between castles and sequences of parallelograms. At `q = 1`, `Π` is the Narayana GF of the parallelograms by width and height ([[parallelogram-polyomino-dyck-bijection](pages/parallelogram-polyomino-dyck-bijection.md)]), as in [[tower-narayana-polynomial](pages/tower-narayana-polynomial.md)].

The q-Catalan family that appears is the one of Pólya and Gessel, the parallelograms by area, with width and height kept apart; the Carlitz family, which counts inversions of Dyck words, does not.[^4] Its denominator `J_0` is the numerator `N` of the castle GF, and the castle denominator `M = J_0 − (Y/(1 − Y)) J_1` is a second combination of the same series.

**Checks.** `N/M − 1` equals the sum over all compositions of `n ≤ 13`, as series in `u` and `q`, at the 15 block weights `x = −7, …, 7`. The block count is at most the area, so the coefficients are polynomials in `x` of degree at most 13, and Equation (3) is an exact identity through area 13. Independently, Equation (4) built from the parallelograms enumerated by area, whose counts are `A006958`, equals the castles through area 12 at 13 block weights, an exact identity to that order.[^5]

## The signed count by area

The block sign is `x = −1`. At `u = 1`, `(q)_k (−q)_k = (q²; q²)_k`, and

```
N(q)  =  Σ_{k≥0} (−2)^k q^{C(k+1,2)} / (q²; q²)_k
M(q)  =  1 + Σ_{k≥1} (−1)^k 2^{k−1} q^{C(k+1,2)} / ((q²; q²)_{k−1} (1 − q^k))

Σ_{n≥1} (even-block castles of area n − odd-block castles of area n) q^n  =  N(q)/M(q) − 1.
```

The series agrees with the recursion of [[castle-row-raising-equation](pages/castle-row-raising-equation.md)] at every `n ≤ 40`.[^5] Both `N` and `M` converge in `|q| < 1`, so the signed count is meromorphic in the unit disk, and its singularities there are zeros of `M`. By the argument principle, `M` has exactly one zero in `|q| < 0.8` and eight in `|q| < 0.84`:[^6]

```
q_0  =  −0.615828135184805773627625720698        1/q_0  =  −1.62382967400459366939460437601
C    =  −N(q_0) / (q_0 M'(q_0))  =  0.0985091749731156224089366266361

q_1  =  −0.8202719776,   then  0.64813 ± 0.51516i  (|q| = 0.82793),  −0.41543 ± 0.71641i  (0.82815),  0.00215 ± 0.83183i  (0.83183)
```

`q_0` and `C` agree with the values of [[castle-row-raising-equation](pages/castle-row-raising-equation.md)] to 30 digits. The second zero is real, so the signed count of area `n` is `C (1/q_0)^n (1 + O((q_0/q_1)^n))` with `q_0/q_1 = 0.75076`. At `n = 300`, `(q_0/q_1)^{300} = 4.5 × 10^{−38}`, the order of the difference `1.7 × 10^{−37}` between consecutive ratios at `n = 299, 300` on that page. In parallelogram terms, the pole is where `1 − x − Π = 0` at `x = −1`, that is `Π(2, −1) = 2`: the parallelograms weighted `2^w (−1)^h q^{area}` sum to 2.

## By descents: q-binomials in two cells only

Write `descents(c)` for the number of `i < w` with `c_i > c_{i+1}`. At `q = 1`, the towers of width `w` with `b` blocks and `k − 1` descents number `N(w, k) C(b + w − k, w − 1)`, with `N(w, k)` the Narayana numbers ([[narayana-numbers](pages/narayana-numbers.md)]). With area:[^7]

- **`k = 1`**: no descent, so the column heights weakly increase and `c_w = b`. The cell is `q^b [b + w − 1, w − 1]_q`, a partition in a box (Cauchy's Theorem C, [[aocp-generating-partitions](pages/aocp-generating-partitions.md)]).
- **`k = w`**: the column heights strictly decrease and `c_1 = b`. The cell is `q^{b + C(w−1, 2)} [b, w − 1]_q`, a partition into distinct parts.
- **`1 < k < w`**: for `w = 3, 4` and `b ≤ 6`, the cell divided by `[b + w − k, w − 1]_q` is a polynomial only when `b = k − 1`, where the q-binomial is 1. So the cells do not factor as a q-Narayana number times this q-binomial.

The GF of the towers of width `w` by blocks and area agrees. For `w = 3, 4` its reduced denominator is `(1 − qx) Π_{j=1}^{w} (1 − q^j x)`, with the factor `1 − qx` twice, and its numerator has negative coefficients; at `w = 3` the numerator is `1 + qx + q²x − q²x² − q³x² − q⁴x³`. So there is no form with a positive numerator over `Π_{j=1}^{w} (1 − q^j x)`.[^7]

## Computation

Signed castles by area from Equation (3) at `x = −1`, `u = 1` (exact rationals, about a second):

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

## Relation to other pages

- [[generalized-dyck-grammar](pages/generalized-dyck-grammar.md)] and [[tower-word-language](pages/tower-word-language.md)] - the grammar graded here.
- [[bousquet-melou-fedou-1995-convex-polyominoes](pages/bousquet-melou-fedou-1995-convex-polyominoes.md)] - the series `J_0`, `J_1` and the parallelogram GF `Y J_1/J_0`.
- [[column-convex-polygon-enumeration](pages/column-convex-polygon-enumeration.md)] - Theorem 3.2 with the same series, and Lemma 2.3, which solves the castles' add-a-column equation.
- [[castle-add-a-column-equation](pages/castle-add-a-column-equation.md)] - the same `N/M` from the add-a-column equation by Lemma 2.3, with `E(1) = N − M` and `1 − F(1) = M` term by term.
- [[castle-row-raising-equation](pages/castle-row-raising-equation.md)] - the signed series by area from a recursion; this page gives its closed form and its second singularity.
- [[prellberg-brak-1995-cluster-models](pages/prellberg-brak-1995-cluster-models.md)] - the functional equation (3.11) of bar-graph polygons and the linearizing substitution.
- [[q-catalan-numbers](pages/q-catalan-numbers.md)] - the families of q-Catalan numbers, among them the parallelograms by area.
- [[steep-polyominoes-q-motzkin-bessel](pages/steep-polyominoes-q-motzkin-bessel.md)] - steep parallelogram polyominoes, whose GF is another quotient of q-Bessel functions.
- [[castle-perimeter](pages/castle-perimeter.md)] - the block count as the vertical half-perimeter, so this page counts castles by width, perimeter and area.
- [[q-differential-system](pages/q-differential-system.md)] - the linear q-differential system of the convex polyominoes, which Bousquet-Mélou and Fédou solve.
- [[convex-polyomino-by-area](pages/convex-polyomino-by-area.md)] - the parallelogram polyominoes by area and the growth constant from the first zero of `J_0`.
- [[q-thread-seminar](pages/q-thread-seminar.md)] - the seminar on castles by area, with this page as one of its stops.
- [[aocp-generating-partitions](pages/aocp-generating-partitions.md)] - Knuth's partitions in a box and the Gaussian binomial (Theorem C).

## Footnotes

[^1]: [[prellberg-brak-1995-cluster-models](pages/prellberg-brak-1995-cluster-models.md)] `raw/prellberg-brak-1995-partially-directed-cluster-models.txt` §3.1 eq. (3.11) and §4 L714-760 [synthesis] - the bar-graph equation `B(x, y, q) = B(qx, y, q) y + {1 + B(qx, y, q)} qx {y + B(x, y, q)}`; the linearization and the staircase solution `T(x) = Σ_n (−qx)^n q^{n(n−1)/2}/(q, qy; q)_n`, "This calculation easily generalizes for the other models with quadratic functional equations"; and for directed column-convex polygons "a \"cubic\" equation", which the same transformation (4.11) makes linear.
[^2]: [[project-euler-502-representations](pages/project-euler-502-representations.md)] §"The grammar" L262-268, L276 - "Let E_k be the towers of height at most k. A tower is empty, or it starts with a gap, or it starts with a peak", "E_k -> empty | R E_k | U V D ( empty | R E_k )"; "V is one row lower because the sub-block itself uses one row, and V is nonempty."
[^3]: [[bousquet-melou-fedou-1995-convex-polyominoes](pages/bousquet-melou-fedou-1995-convex-polyominoes.md)] p.56 L153-184 and Appendix A p.72 L984-1131 [synthesis] - eq. (1) `X = y J_1/J_0`, "the quotient of two q-analogues of Bessel-like functions", and the series `J_0`, `J_1` as transcribed on that page; the same series are Theorem 3.2 of [[column-convex-polygon-enumeration](pages/column-convex-polygon-enumeration.md)] at `s = t = 1`.
[^4]: raw/q-catalan-numbers.wiki §"q-Catalan Numbers" L7-9 - "Carlitz q-Catalan numbers count inversions of Dyck Words and Catalan permutations", "q-Catalan numbers (Polya, Gessel) count parallelogram polyominoes by area".
[^5]: Verified by execution (Python 3.11, exact rational arithmetic, 2026-10-16): Equation (3) against all compositions of `n ≤ 13` weighted `u^{width} x^{blocks} q^{area}` at `x = −7, …, 7`; Equation (4), with the parallelograms enumerated as columns `[b_i, t_i]` with `b_i ≤ b_{i+1} ≤ t_i ≤ t_{i+1}` (area counts `1, 2, 4, 9, 20, 46, 105, 242, 557, 1285, 2964` = `A006958`), against the castles through area 12 at `x = −6, …, 7`, `x ≠ 1`; the computation block, whose output equals both enumeration through area 14 and the 40 terms on [[castle-row-raising-equation](pages/castle-row-raising-equation.md)].
[^6]: Verified by execution (Python 3.11 with mpmath, 2026-10-16): `q_0` and `C` by `findroot` and a numerical derivative at 40 digits; `q_1` by bisection on `[−0.825, −0.815]`; the complex zeros by `findroot`; the zero counts of `M` on the circles `|q| = 0.6, 0.62, 0.8, 0.82, 0.83, 0.84` by the argument principle (`0, 1, 1, 1, 6, 8`), with the series truncated at `k = 60`.
[^7]: Verified by execution (Python 3.11 with SymPy, 2026-10-16): towers of width `w = 2, 3, 4` with `b ≤ 6` by blocks, descents and area, against `N(w, k) C(b + w − k, w − 1)` and the two end-cell formulas, and each middle cell divided by `[b + w − k, w − 1]_q`; the GF of the towers of width 3 (to `q^34`) and width 4 (to `q^26`) times `(1 − qx) Π_j (1 − q^j x)` is a polynomial coprime to that product, and with one factor `1 − qx` removed the product is not a polynomial.
