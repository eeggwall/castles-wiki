---
title: Convex polyominoes by area - the ladder from rectangles to 2.30913^n
category: Analyses
summary: Every convex-polyomino family counted by area n on one ladder - rectangles d(n), Ferrers p(n), stacks = convex castles A001523, parallelograms A006958, directed convex A067676, convex A067675 - with the castle's own bar graphs (2^{n-1}) and column-convex polyominoes (A001169) beside it. Each rung has an "adding a slice" generating function. The last three are quotients over one q-Bessel denominator J_0 (Bousquet-Mélou-Fédou: y J_1/J_0, y M_1/J_0, and the Theorem 3.1 convex formula) and share the growth constant 2.3091385933... (A276994), with prefactors 0.29745, 0.65896 and 2.91960. With the PE 502 parity clause carried over (on row-convex shapes, blocks = height), signed Ferrers are (-1)^n A000700 by conjugation and signed parallelograms are -q/(1 + q^3/(1 + q^5/(1 + ...))) = -A049346, because the height variable at y = -1 cancels the linear terms of Flajolet's festoon J-fraction; the even/odd splits of stacks, directed convex and convex have no OEIS match. Verified by column-sweep enumeration to area 40 (parallelograms) and 32 (convex).
tags: [analysis, polyomino, convex, area, q-analog, generating-function, parity, ferrers, stack-polyomino, parallelogram-polyomino, directed-convex, continued-fraction, oeis, verification]
sources: [analytic-combinatorics-ch1-ogfs, column-convex-polygon-enumeration, counting-horizontally-convex-polyominoes, castle-by-area, bousquet-melou-fedou-1995-convex-polyominoes, klarner-rivest-1974-convex-n-ominoes]
created: 2026-09-22
updated: 2026-09-22
---

# Convex polyominoes by area

The Q Department grades castles by area. This page sets the classical baseline it grades against: every [[convex-polyomino](pages/convex-polyomino.md)] family counted by area `n` (the number of cells), on one ladder, with the castle's own families beside it. It is the polyomino-side foundation for [[castle-by-area](pages/castle-by-area.md)], [[stack-polyomino-gf](pages/stack-polyomino-gf.md)], and the q-polyomino zoo in `IDEAS.md`.

## The ladder

Fixed polyominoes (translations identified, rotations and reflections distinct), `n = 1..16`:

| n | rect | Ferrers | stack = convex castle | parallelogram | directed convex | convex | bar graph = castle | column-convex | all |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| 3 | 2 | 3 | 4 | 4 | 5 | 6 | 4 | 6 | 6 |
| 4 | 3 | 5 | 8 | 9 | 13 | 19 | 8 | 19 | 19 |
| 5 | 2 | 7 | 15 | 20 | 33 | 59 | 16 | 61 | 63 |
| 6 | 4 | 11 | 27 | 46 | 82 | 176 | 32 | 196 | 216 |
| 7 | 2 | 15 | 47 | 105 | 200 | 502 | 64 | 629 | 760 |
| 8 | 4 | 22 | 79 | 242 | 481 | 1374 | 128 | 2017 | 2725 |
| 9 | 3 | 30 | 130 | 557 | 1144 | 3630 | 256 | 6466 | 9910 |
| 10 | 4 | 42 | 209 | 1285 | 2699 | 9312 | 512 | 20727 | 36446 |
| 11 | 2 | 56 | 330 | 2964 | 6329 | 23320 | 1024 | 66441 | 135268 |
| 12 | 6 | 77 | 512 | 6842 | 14775 | 57279 | 2048 | 212980 | 505861 |
| 13 | 2 | 101 | 784 | 15793 | 34381 | 138536 | 4096 | 682721 | 1903890 |
| 14 | 4 | 135 | 1183 | 36463 | 79819 | 331032 | 8192 | 2188509 | 7204874 |
| 15 | 4 | 176 | 1765 | 84187 | 185001 | 783630 | 16384 | 7015418 | 27394666 |
| 16 | 5 | 231 | 2604 | 194388 | 428290 | 1841867 | 32768 | 22488411 | 104592937 |
| OEIS | A000005 | A000041 | A001523 | A006958 | A067676 | A067675 | A011782 | A001169 | A001168 |

The six convex columns and the column-convex column were computed by the column sweep below and agree with the OEIS entries over every term computed.[^1] The last two columns and the OEIS row are cited.[^2]

Two readings the table makes plain:

- **The castle sits on two rungs.** Castles by area are bar graphs, and convex castles are stacks. Between stacks and convex polyominoes the only change is a floating base: the bottoms get their own anti-unimodal profile. That change alone moves the count from subexponential growth to exponential growth `2.309^n`. Stacks are subexponential because a stack is a peak column plus two partitions, so there are at most `n p(n)^2` of area `n`; the ratio is still falling at `1.369` at `n = 25`.
- **Column-convex by area is A001169.** Rotating a polyomino 90 degrees turns its rows into columns and keeps its area, so it maps horizontally (row-) convex polyominoes one-to-one onto column-convex polyominoes of the same area. The horizontally convex count on [[horizontally-convex-polyomino](pages/horizontally-convex-polyomino.md)] is also the column-convex count by area. Every castle is column-convex, so A001169 is the natural envelope for castle area counts, which `IDEAS.md` asks to compare castle recurrences against. The sweep reproduces it with the multiplicity `h + g - 1` for gluing a height-`g` column next to a height-`h` column, the same `k + l - 1` transfer weight Temperley used.[^3]

## One method: adding a slice

Flajolet and Sedgewick's "adding a slice" (Example III.22) is the add-a-column construction of [[column-convex-polygon-enumeration](pages/column-convex-polygon-enumeration.md)] written as a bivariate generating function (BGF). Let `F(z, u)` count objects with `z` marking area and `u` marking the size of the last slice (column). Then

```
F(z, u) = f(zu) + ( L[F(z, u)] )_{u -> zu},        L[u^j] = sum_{(j, k) in R} u^k,
```

where `f` is the one-column generating function and `R` is the set of allowed (old, new) slice pairs.[^4] Each ladder rung is a choice of `R` plus state:

| family | slice rule | generating function by area |
|---|---|---|
| bar graph (castle) | any `k >= 1` | `L[u^j] = u/(1-u)`, so `F(z,1) = z/(1-2z)`, giving `2^{n-1}` |
| Ferrers | `k >= j` (read right to left) | `sum_k z^k / ((1-z)...(1-z^k))`, Euler's `prod 1/(1-z^k)` minus 1 [^4] |
| stack | two phases, `k >= j` then `k <= j` | `sum_k z^k/(1-z^k) * 1/((1-z)...(1-z^{k-1}))^2` [^5] |
| column-convex | any `k`, weight `j + k - 1` | `z(1-z)^3 / (1 - 5z + 7z^2 - 4z^3)`, rational [^3] |
| parallelogram | segment slices that lean right | `J_1(z,1) / J_0(z,1)`, a ratio of q-Bessel series [^6] |
| directed convex | bottoms rise, tops unimodal | `y M_1 / J_0` at `x = y = 1`, `q = z`: the q-analogue of the odd part of `J_1`, over the same denominator [^7] |
| convex | two boundaries, two phases each | `2y^2 M_1 (Jbar_1 beta - Kbar_1 alpha)/J_0 - y Jbar_1 b_1 + y Kbar_1 a_1` at `x = y = 1`, `q = z`, again over `J_0` [^7] |

The slice state grows with the family: none for bar graphs, the last height for Ferrers and stacks, and a slice length with left and right offsets for parallelograms. For convex polyominoes it is the whole last column plus a phase bit for each boundary. The column sweep below is this construction with the state written out explicitly. The last two rows come from a different construction: Bousquet-Mélou and Fédou solve a linear q-differential system from an algebraic-language encoding ([[q-differential-system](pages/q-differential-system.md)]), and the full series and verification are on [[bousquet-melou-fedou-1995-convex-polyominoes](pages/bousquet-melou-fedou-1995-convex-polyominoes.md)].

## One growth constant

Parallelogram and convex polyominoes both grow like `c mu^n` with the same

```
mu = 2.30913 85933 30494 73...     (OEIS A276994, the Klarner-Rivest constant)
1/mu = 0.43306 19231 29...         the smallest positive zero of J_0(z, 1) = sum_n (-1)^n z^{n(n+1)/2} / ((1-z)...(1-z^n))^2
```

Klarner and Rivest proved that the convex and parallelogram limits exist and coincide: every convex polyomino cuts into a stack, a parallelogram and an inverted stack, so `p(n) <= c(n) <= (n+2)^4 p(n)`. They then bracketed the common limit to `2.309138...` by truncating the parallelogram row-to-row kernel `min{m, n}` from both sides.[^16] The prefactors are `0.29745...` for parallelograms and `2.91959...` for convex polyominoes.[^8] For directed convex polyominoes it is `0.6589555418`, from the Bousquet-Mélou-Fédou series at area 120. OEIS A067676 does not list it. The same computation reproduces `2.9195985097` for convex, while the paper itself prints `C ≃ 2.67564`, a value its own generating function does not give.[^15] Bender obtained the parallelogram asymptotic from the singularity of the generating function, and Flajolet and Sedgewick follow his analysis in Example IX.14.[^6][^14] The printed digits there end `...331230`, which OEIS flags as wrong; the value above is the corrected one.[^8] Directed convex polyominoes sit between the two (parallelogram ⊂ directed convex ⊂ convex), so their growth rate is squeezed to the same `mu`. It is also visible in the formulas: all three generating functions are quotients over the same `J_0`, so the zero of `J_0` sets their common growth rate.[^7] Numerically the parallelogram ratio `a(n+1)/a(n)` is already `2.30914` at `n = 25`, while the directed-convex (`2.30924`) and convex (`2.3093`) ratios approach it more slowly.[^1]

The castle's fixed-`h` growth constants are algebraic Perron roots of a finite transfer matrix. This `mu` is instead the reciprocal of the first zero of a q-series with no finite transfer matrix behind it, so no Perron-root argument makes it algebraic, and the question on [[algebraic-transcendental-wall](pages/algebraic-transcendental-wall.md)] is open for it.

## The parity clause on convex polyominoes

A castle block is a maximal run of cells in one row. On a row-convex shape every row is one run, so **blocks = height**, and the Project Euler 502 even-block clause becomes even height ([[convex-polyomino](pages/convex-polyomino.md)]). The signed count `S(n) = even(n) - odd(n) = sum (-1)^height` over area-`n` polyominoes is the `u = -1` specialization the castle wiki runs everywhere ([[castle-sign](pages/castle-sign.md)]).

| n | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| convex even | 0 | 1 | 4 | 10 | 28 | 84 | 244 | 686 | 1820 | 4675 | 11684 | 28677 | 69292 | 165529 | 391780 | 920885 | 2152976 | 5014008 | 11643968 | 26987283 |
| convex odd | 1 | 1 | 2 | 9 | 31 | 92 | 258 | 688 | 1810 | 4637 | 11636 | 28602 | 69244 | 165503 | 391850 | 920982 | 2153196 | 5014268 | 11644426 | 26987676 |
| S, Ferrers | -1 | 0 | -1 | 1 | -1 | 1 | -1 | 2 | -2 | 2 | -2 | 3 | -3 | 3 | -4 | 5 | -5 | 5 | -6 | 7 |
| S, stack | -1 | 0 | 0 | 2 | 1 | 3 | 1 | 3 | -2 | 1 | -6 | -2 | -12 | -5 | -17 | -4 | -20 | 0 | -18 | 12 |
| S, parallelogram | -1 | 0 | 0 | 1 | 0 | 0 | -1 | 0 | -1 | 1 | 0 | 2 | -1 | 1 | -3 | 2 | -3 | 4 | -4 | 6 |
| S, directed convex | -1 | 0 | 1 | 1 | 1 | -2 | -2 | -3 | 0 | -1 | 5 | 3 | 7 | -3 | 3 | -6 | 8 | -12 | 7 | -19 |
| S, convex | -1 | 0 | 2 | 1 | -3 | -8 | -14 | -2 | 10 | 38 | 48 | 75 | 48 | 26 | -70 | -97 | -220 | -260 | -458 | -393 |

The stack row's `even` and `odd` are the `cev(n)` and `cod(n)` of [[castle-by-area](pages/castle-by-area.md)], so this table extends that parity split up the ladder.[^9]

**Ferrers: closed, by conjugation.** Transposing a Ferrers diagram exchanges height (largest part) with number of parts, so `sum (-1)^height q^area = prod_{k>=1} 1/(1 + q^k)`. That product is the generating function of partitions into distinct odd parts at `-q`, so `S_Ferrers(n) = (-1)^n A000700(n)`.[^10]

**Parallelograms: closed, by the festoon J-fraction.** Flajolet's report on Pólya's parallelogram result gives a continued fraction in which `x` marks width, `y` marks height and `q` marks area.[^11] The scanned text of the fraction is partly illegible. The form below was reconstructed from its legible fragments together with the `x = y = 1` case printed on OEIS A006958, and it is confirmed by enumeration at `y = 1` and `y = -1`. It was not read cleanly from the source:

```
C(x, y; q) = xyq / (1 - (x+y)q - xyq^3 / (1 - (x+y)q^2 - xyq^5 / (1 - (x+y)q^3 - ...)))
```

At `x = 1, y = -1` the diagonal terms `(x+y) q^k` all vanish and `xy = -1`, leaving

```
sum (-1)^height q^area = -q / (1 + q^3 / (1 + q^5 / (1 + q^7 / ...)))
                       = -q + q^4 - q^7 - q^9 + q^10 + 2q^12 - q^13 + ...
```

These are the coefficients of `-A049346`, equivalently `(-1)^n A227310(n)`, whose generating function OEIS gives as `1 + q/(1 - q^3/(1 - q^5/...))`.[^12] Two consequences:

- **Near-perfect balance.** `|S(n)|` grows like `1.23729^n` (A227310's asymptotic) against `2.30914^n` for the total, so even- and odd-height parallelograms are equinumerous up to a relative error of order `(0.5358)^n`.[^12] What the parity clause does to the continued fraction is cancel its diagonal terms.
- **Width parity gives the same series,** since `C` is symmetric in `x` and `y`.

The same object has an S-fraction form that makes the height variable visible on every other numerator, `1 + P(q, y) = 1/(1 - yq/(1 - q/(1 - yq^2/(1 - q^2/(1 - yq^3/...)))))`, which matches the full height distribution through area 28.[^1]

**Stacks, directed convex, convex: open.** None of these signed or even/odd rows is in OEIS.[^13] Their signed counts oscillate with empirical growth near `1.18^n` (stack, directed convex) and `1.3^n` (convex), so they are also close to balanced. Finding the height-marked analogue of the festoon J-fraction for them is the next Q-Department question this page opens.

## The column sweep

Every count on this page came from this enumerator, a direct transcription of the column-interval definition on [[convex-polyomino](pages/convex-polyomino.md)]. Area 32 for all four families runs in a few seconds.

```python
from collections import defaultdict

def convex_by_area(N, bottoms="free", tops="unimodal"):
    """[even-height, odd-height] counts by area 1..N; bottoms in {fixed, rising, free}."""
    out = [[0, 0] for _ in range(N + 1)]
    cur = defaultdict(int)    # (b, t, top_falling, bottom_rising, min_b, max_t, area)
    for h in range(1, N + 1):
        cur[(0, h - 1, False, False, 0, h - 1, h)] = 1
    while cur:
        nxt = defaultdict(int)
        for (b, t, tf, br, lo, hi, a), c in cur.items():
            out[a][(hi - lo + 1) % 2] += c
            for nb in range(b - (N - a), t + 1):
                for nt in range(max(nb, b), nb + N - a):
                    if (nt > t and tf) or (nb < b and br):
                        continue                      # row-convexity
                    if bottoms == "fixed" and nb != b: continue
                    if bottoms == "rising" and nb < b: continue
                    if tops == "rising" and nt < t: continue
                    nxt[(nb, nt, tf or nt < t, br or nb > b,
                         min(lo, nb), max(hi, nt), a + nt - nb + 1)] += c
        cur = nxt
    return out[1:]

# convex: defaults; directed convex: bottoms="rising"; stack: bottoms="fixed";
# parallelogram: bottoms="rising", tops="rising"
```

## Sources not yet read

These appear in OEIS link lists and in the reference list of [[bousquet-melou-fedou-1995-convex-polyominoes](pages/bousquet-melou-fedou-1995-convex-polyominoes.md)], and were not read. Nothing on this page rests on them; they are leads for the next ingest.

- E. A. Bender, "Convex n-ominoes", Discrete Math. 8 (1974) 219-226 - listed on A006958 and A276994; the asymptotic analysis behind `mu`.
- M.-P. Delest and G. Viennot, "Algebraic languages and polyominoes enumeration", Theoretical Computer Sci. 34 (1984) 169-206 - listed on A005436; the perimeter count.

## Related

- [[convex-polyomino](pages/convex-polyomino.md)] - definitions, the corner taxonomy, and why blocks = height.
- [[castle-by-area](pages/castle-by-area.md)] - the castle rungs (`2^{n-1}`, A001523) and their parity splits.
- [[stack-polyomino-gf](pages/stack-polyomino-gf.md)] - the stack rung's symbolic-method generating function.
- [[horizontally-convex-polyomino](pages/horizontally-convex-polyomino.md)] - A001169, which by rotation is the column-convex rung.
- [[steep-polyominoes-q-motzkin-bessel](pages/steep-polyominoes-q-motzkin-bessel.md)], [[q-catalan-numbers](pages/q-catalan-numbers.md)] - the q-Bessel and q-Catalan families the parallelogram rung belongs to.
- [[castle-sign](pages/castle-sign.md)] - the `(-1)^blocks` specialization used in the parity section.
- [[bousquet-melou-fedou-1995-convex-polyominoes](pages/bousquet-melou-fedou-1995-convex-polyominoes.md)], [[q-differential-system](pages/q-differential-system.md)] - the directed-convex and convex generating functions and the method that found them.
- [[klarner-rivest-1974-convex-n-ominoes](pages/klarner-rivest-1974-convex-n-ominoes.md)] - the source of `mu`: existence, the stack-parallelogram-stack trisection, and the kernel bounds.

## Footnotes

[^1]: Verified by execution, 2026-09-22, with the enumerator in "The column sweep". Totals by area agree with OEIS for rectangles, Ferrers, stacks, parallelograms, directed convex and convex through `n = 26`; parallelograms alone through `n = 40`, and convex, directed convex and stacks with parity through `n = 32`. The column-convex column comes from a separate sweep with state (last column height, area) and weight `h + g - 1`, and matches A001169 through `n = 14`. The stack even/odd rows match `cev`/`cod` of [[castle-by-area](pages/castle-by-area.md)] through `n = 12`. The signed parallelogram row equals the `x = 1, y = -1` specialization of the J-fraction of footnote 11 through `n = 40`, and the `y = 1` specialization reproduces A006958 through `n = 40`. The height-marked S-fraction reproduces the complete height distribution of parallelograms through `n = 28`. Prefactor estimates at `n = 36` (same enumerator, run 2026-09-22): convex `c(n)/mu^n = 2.919696`, parallelogram `p(n)/mu^n = 0.297454`, with convex decreasing from `2.9206` at `n = 26`. Ratios `a(n+1)/a(n)` at `n = 25`: parallelogram 2.30914, directed convex 2.30924, convex 2.3093, stack 1.369.
[^2]: https://oeis.org/A001168 and https://oeis.org/A011782 (fetched 2026-09-22) - "Number of fixed polyominoes with n cells", data "1,1,2,6,19,63,216,760,2725,9910,36446,135268,505861,1903890,7204874,27394666,104592937"; bar graphs are the compositions of n, `2^{n-1}`, per [[castle-by-area](pages/castle-by-area.md)]. OEIS names of the other columns (fetched 2026-09-22): A067675 "Number of fixed convex polyominoes with n cells", A067676 "Number of fixed directed convex polyominoes with n cells", A006958 "Number of parallelogram polyominoes with n cells", A001169 "Number of board-pile polyominoes with n cells".
[^3]: https://algo.inria.fr/flajolet/Publications/book.pdf Example V.20 pp.365-367 (read from a local copy of the 2009 edition; the URL is the public copy and was not fetched) - "The transition from one T[k] to a T[ℓ] has a multiplicity equal to k + ℓ − 1 ... T(z) = z(1 − z)^3 / (1 − 5z + 7z^2 − 4z^3) ... is EIS A001169 ('Number of board-pile polyominoes with n cells')."
[^4]: raw/analytic-combinatorics-part-a.pdf Example III.22 pp.199-200 - "F(z, u) = f(zu) + (L[F(z, u)])_{u→zu} ... L[u^j] := Σ_{(j,k)∈R} u^k ... describes inductively objects as comprising either one column (f(zu)) or else as being formed by adding a new column to an existing one"; the partition case R1 gives (63) "F(z, u) = zu/(1−z) + z^2u^2/((1−z)(1−z^2)) + ..."
[^5]: [[analytic-combinatorics-ch1-ogfs](pages/analytic-combinatorics-ch1-ogfs.md)] Example I.8 pp.45-46 - "S(z) = Σ_{k≥1} z^k/(1−z^k) · 1/((1−z)(1−z²)···(1−z^{k−1}))² ... the number of stack polyominoes (EIS A001523)."
[^6]: https://algo.inria.fr/flajolet/Publications/book.pdf Example IX.14 pp.660-662 (read from a local copy of the 2009 edition; the URL is the public copy and was not fetched) - "The ordinary BGF of parallelograms, with z marking area and u marking perimeter is F(z, u) = u J_1(z, u)/J_0(z, u) ... This is the method of 'adding a slice' introduced in Chapter III, p. 199 ... Our presentation follows an early article of Bender [38]"; "F(z, 1) = z + 2z^2 + 4z^3 + 9z^4 + 20z^5 + 46z^6 + ..., corresponding to EIS A006958."
[^7]: [[bousquet-melou-fedou-1995-convex-polyominoes](pages/bousquet-melou-fedou-1995-convex-polyominoes.md)] eq. (3) p.56 and Theorem 3.1 p.62 - "Y(x, y, q) = y M_1/J_0" and "The generating function of convex polyominoes is Z = 2y^2 M_1(Jbar_1 β - Kbar_1 α)/J_0 - y Jbar_1 b_1 + y Kbar_1 a_1" (read from the page images); the series `M_1, Jbar_1, Kbar_1, alpha, beta, a_1, b_1` are transcribed on that page. At `x = y = 1` they reproduce A067676 and A067675 through `n = 120` (verification there). That the shared denominator fixes the shared growth rate is this page's reading.
[^8]: https://oeis.org/A276994, https://oeis.org/A006958, https://oeis.org/A067675 (fetched 2026-09-22) - A276994 "Decimal expansion of the Klarner-Rivest polyomino constant ... 1/A276994 = 0.4330619231293906645846169654189837... is the smallest positive root of the equation Sum_{n>=0} ((-1)^n * z^(n*(n+1)/2) / (Product_{k=1..n} 1-z^k)^2) = 0 ... Analytic Combinatorics (Flajolet and Sedgewick, 2009, p. 662) has a wrong value of this constant (2.309138593331230...)"; A006958 "a(n) ~ c * d^n, where d = A276994 = 2.3091385933304947... c = 0.2974535058111219..."; A067675 "a(n) ~ c * d^n, where d = A276994 ... c = 2.9195985097136070...".
[^9]: [[castle-by-area](pages/castle-by-area.md)] `vein9-area.md` §"Parity splits" L41-48 - "`cev(n)` 0, 1, 2, 5, 8, 15, 24, 41, 64, 105, 162, 255 ... `cod(n)` 1, 1, 2, 3, 7, 12, 23, 38, 66, 104, 168, 257".
[^10]: https://oeis.org/A000700 (fetched 2026-09-22) - "number of partitions of n into distinct odd parts ... G.f.: 1/Product_{i>=1} (1 + (-x)^i)." Substituting `x = -q` gives `prod 1/(1 + q^i)` with coefficients `(-1)^n A000700(n)`; the conjugation step is common knowledge.
[^11]: P. Flajolet, "Polya Festoons", INRIA Research Report 1507 (1991), https://inria.hal.science/inria-00075055 (PDF downloaded and read as OCR text, 2026-09-22; not yet in `raw/`), Theorem 1 and closing paragraph [synthesis] - C_{m,n,k} counts "diagonally convex lattice polygons having area k, comprising 2m steps parallel to the x-axis and 2n steps parallel to the y-axis", and "In relation to the continued fraction approach of [6], one derives the representation" of `C(x, y; q)` as the J-fraction shown. The scanned text of the fraction is partly illegible; the form here is the one consistent with OEIS A006958's "C(1, 1;q) = q/(1-2*q-q^3/(1-2*q^2-q^5/(1-2*q^3-q^7/...)))", and it was checked against enumeration at `(x, y) = (1, 1)` and `(1, -1)` (footnote 1).
[^12]: https://oeis.org/A227310 and https://oeis.org/A049346 (fetched 2026-09-22) - A227310 "G.f.: 1 + q/(1 - q^3/(1 - q^5/(1 - q^7/ (...))))" and "a(n) ~ c * d^n, where d = 1.23729141259673487...", data "1,1,0,0,1,0,0,1,0,1,1,0,2,1,1,3,2,3,4,4,6,7,8,11,13,16,20"; A049346 "a(0) = 1 and a(n) = abs(A049346(n)) for n>=1" (from A227310), data "0,1,0,0,-1,0,0,1,0,1,-1,0,-2,1,-1,3,-2,3,-4,4,-6".
[^13]: OEIS search, 2026-09-22 - no results for the convex even row "1,4,10,28,84,244,686,1820", the convex odd row "1,2,9,31,92,258,688,1810", the directed-convex even and odd rows, or the unsigned directed-convex and convex signed rows; the stack rows were already recorded as new on [[castle-by-area](pages/castle-by-area.md)].
[^14]: P. Flajolet, "Polya Festoons", INRIA Research Report 1507 (1991), https://inria.hal.science/inria-00075055 (PDF downloaded and read as OCR text, 2026-09-22), closing section - "Bender [1] proved [q^n] C(1, 1; q) = 0.29745 · 2.30913859330^n, by considering singularities of the GF (6)" (OCR spelling normalized).
[^15]: [[bousquet-melou-fedou-1995-convex-polyominoes](pages/bousquet-melou-fedou-1995-convex-polyominoes.md)] §"Verification" and p.59 [synthesis] - `a(n)/mu^n` at `n = 120` from the paper's series gives 0.2974535058 (parallelogram), 0.6589555418 (directed convex) and 2.9195985097 (convex), stable from `n = 80`; the paper prints "C ≃ 2.67564 and a ≃ 2.30914" for convex, citing Bender and Klarner-Rivest.
[^16]: [[klarner-rivest-1974-convex-n-ominoes](pages/klarner-rivest-1974-convex-n-ominoes.md)] §2 and §4-5 [synthesis] L69-124,L226-344 - the trisection into "two stacks and one parallelogram", (3) `c(n) <= (n+2)^4 p(n)`, (5) `lim c(n)^{1/n} = lim p(n)^{1/n} = gamma`, and the kernel bounds of Table 1 giving "(32) gamma = lim_{n->oo} (c(n))^{1/n} = 2.309138...".
