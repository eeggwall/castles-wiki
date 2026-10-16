---
title: Castle strips counted by area - the growth-constant census
category: Analyses
summary: Castle strips (skylines on the heights 1..h under a 0/1 rule saying which height may follow which) counted by area instead of width - which growth constants appear, and at what smallest height. The area generating function has denominator det(I − A diag(x, …, x^h)), which expands over the principal minors of the rule, so an exhaustive census of every rule up to height 4 (66,066 rules) is cheap. Heights 1 to 4 give 1, 3, 64 and 6,226 new growth constants, of degree up to the triangle number T = h(h+1)/2 (2,611 of the 6,226 at height 4 have the full degree 10). The smallest constant at each height is proved to be the root of z^T − z − 1 (1.3247, 1.1347, 1.0758 at heights 2, 3, 4), and the largest is the h-nacci constant. The census reaches all ten of the ten smallest Pisot numbers by height 4, every Salem number of degree 4 and 6 below the height-4 ceiling 1.9276, the smallest Salem number of degree at most 8 (1.280638), and five of the six Salem numbers below 1.3 of degree at most 10; Lehmer's number 1.17628 is not reached by height 4. At height 5 (33.5 million rules, 4,712,674 distinct denominators) Lehmer's number appears, with denominator Lehmer's polynomial times three cyclotomic factors at the full degree 15, and all 11 known Salem numbers below 1.3 of degree at most 14 appear by height 5. The larger of two lower bounds, the degree bound and the ceiling bound, is the exact minimum height for 96.8% of the constants through height 5; Lehmer's number is the smallest constant that needs more.
tags: [analysis, castle, castle-strip, area, generating-function, transfer-matrix, growth-constant, perron-number, pisot-number, salem-number, lehmer, mahler-measure, plastic-number, supergolden, n-nacci, census, exhaustive-search, min-height, implementation, verification]
sources: [verger-gaugry-2024-salem-minoration, pe502-pell-castle-strip]
created: 2026-09-25
updated: 2026-10-16
---

# Castle strips counted by area - the growth-constant census

## The question

A castle strip on the heights `1, …, h` is a skyline with column heights in `{1, …, h}`, under a rule given by an `h × h` matrix `A` of 0s and 1s: a 1 in row `a`, column `b` means a column of height `a` may be followed by one of height `b`. Strips need not reach height `h`, so they are not castles ([[castle-strip](pages/castle-strip.md)]). [[quadratic-min-height](pages/quadratic-min-height.md)] counts strips by **width**. This page counts them by **area**, the total number of cells, the grading of [[castle-by-area](pages/castle-by-area.md)].

The number of strips of area `n` grows like `ρ^n`, and `ρ` is the rule's **area growth constant**. The question: **which numbers `ρ` appear, and what is the smallest height at which each first appears?** The census is exhaustive through height 5.

## Terms used on this page

- **Minimal polynomial, conjugates** - the growth constant `ρ` is a root of an integer polynomial; the monic one of lowest degree is its minimal polynomial, and that polynomial's other roots are the conjugates of `ρ`. The golden ratio `1.618` has minimal polynomial `x² − x − 1` and one conjugate, `−0.618`.
- **Perron number** - 1, or a real algebraic integer `θ > 1` whose conjugates all have absolute value less than `θ`.[^verger-def] An area growth constant above 1 is the largest eigenvalue of a nonnegative integer matrix (the unrolled table `U` in the proof of the theorem), so no conjugate is larger in absolute value.
- **Pisot number** - a Perron number above 1 whose conjugates all lie strictly inside the unit circle. The smallest is the **plastic number** `1.3247`, the root of `x³ − x − 1` (Siegel), and the set of Pisot numbers is closed (Salem).[^verger-def] Its smallest limit point is the golden ratio, and Dufresnoy and Pisot determined every Pisot number below it.[^pisot] The [[plastic-number](pages/plastic-number.md)] page has the castle readings of the plastic number.
- **Salem number** - an algebraic integer `β > 1` whose conjugates all have absolute value at most 1, with at least one on the unit circle. Its conjugates are `1/β` and pairs of complex conjugates on the unit circle, its minimal polynomial is reciprocal, and its degree is even and at least 4.[^verger-def]
- **Lehmer's number** - `1.17628…`, the largest root of Lehmer's polynomial `x^10 + x^9 − x^7 − x^6 − x^5 − x^4 − x^3 + x + 1`, the smallest known Salem number, found by Lehmer in 1933.[^verger-def] Lehmer's conjecture states that the **Mahler measure** of an integer polynomial (the product of the absolute values of its roots outside the unit circle) is either 1 or at least some constant above 1, believed to be `1.17628`.[^lehmer] The restriction to Salem numbers, that they are bounded away from 1, is the Salem conjecture; a 2024 preprint claims the bound `1.08544` ([[verger-gaugry-2024-salem-minoration](pages/verger-gaugry-2024-salem-minoration.md)]), and other authors state it as a conjecture.[^verger-thm]

## The generating function

Weight a column of height `j` by `x^j`. The strips counted by area have a generating function with denominator

```
det( I − A · diag(x, x², …, x^h) )  =  Σ over subsets S of {1, …, h} of  (−1)^|S| · det(A_S) · x^(Σ S)        (1)
```

where `A_S` is the principal submatrix of `A` on the heights in `S`. The right side is the expansion of `det(I − M)` over principal minors, with the diagonal weights pulled out of each minor, so the denominator needs only integer determinants of 0/1 submatrices. Its degree is at most `1 + 2 + ⋯ + h = T`, the `h`-th triangle number. The growth constant is `1/x*`, where `x*` is the smallest positive root of the denominator: there the largest eigenvalue of the weighted matrix reaches 1.[^exec]

Two bounds hold for every rule on `h` heights:

- A rule on `h` heights counts a subset of the compositions (ordered sums) of the area with parts at most `h`, so its growth constant is at most the **`h`-nacci constant** of those compositions ([[exact-height-castle-by-area](pages/exact-height-castle-by-area.md)]): the golden ratio `1.618` at `h = 2`, the tribonacci constant `1.839` at 3, the tetranacci constant `1.928` at 4, always below 2. The all-ones rule attains it.
- The minimal polynomial of the growth constant has degree at most `T = h(h+1)/2`.

## The census through height 4

Every 0/1 rule of size 1 to 4 (2, 16, 512 and 65,536 rules) was expanded by Equation (1), the distinct denominators factored exactly, and the factor carrying `x*` reversed to give the minimal polynomial of `ρ`. The first height at which a constant appears is its minimum height.[^exec]

| height | distinct denominators | new growth constants | degrees of the new constants | new Pisot | new Salem |
|---|---|---|---|---|---|
| 1 | 2 | 1 (the growth constant 1) | 1 | - | - |
| 2 | 8 | 3 | 2, 3 | 3 | 0 |
| 3 | 105 | 64 | 3 (5), 4 (7), 5 (23), 6 (29) | 14 | 4 |
| 4 | 8,255 | 6,226 | 2 to 10; 2,611 of degree 10 | 74 | 29 |

Height 2 gives exactly the golden ratio, the plastic number and the supergolden constant `1.4656`, the root of `x³ − x² − 1`:

```
rule   growth                       denominator          reading
11     golden     1.618034          1 − x − x²           parts 1 and 2, anything goes
11
01     plastic    1.324718          1 − x² − x³          height 1 may not follow height 1
11
11     supergolden 1.465571         1 − x − x³           height 2 may not follow height 2
10
```

The largest constant at each height is the `h`-nacci constant: the tribonacci constant `1.839287` first at height 3 and the tetranacci constant `1.927562` first at height 4. The tribonacci constant cannot appear at height 2, because it exceeds the golden ratio, the ceiling at height 2.

## The smallest constant at each height

**Theorem.** For every height `h ≥ 2`, the smallest area growth constant above 1 of a rule on `h` heights is the root of

```
z^T − z − 1,     T = h(h+1)/2:
h = 2:  1.324718  (z³ − z − 1, the plastic number)
h = 3:  1.134724  (z⁶ − z − 1)
h = 4:  1.075766  (z^10 − z − 1)
h = 5:  1.048985  (z^15 − z − 1)
```

*Proof.* The proof has three steps.

*Unrolling.* Replace each height `j` by a chain of `j` states, one per cell, with a forced step from each cell to the next, and let the last cell of height `a` step to the first cell of height `b` whenever the rule allows `a → b`. This gives a 0/1 matrix `U` on `T` states, and a strip of area `n` is a walk through `n` states of `U`, so the area growth constant of the rule is the largest eigenvalue of `U`. The denominators agree too: `det(I − xU)` is a sum over sets of vertex-disjoint cycles, the cycles of `U` are the cycles of the rule with length equal to their area, and disjoint cycles stay disjoint, which gives Equation (1).[^exec]

*A lower bound for any 0/1 matrix.* Let `G` be a 0/1 matrix on `n` states with growth above 1. Its growth is that of one of its strongly connected parts, and that part is not a single cycle, since a single cycle grows at exactly 1. So it contains a cycle `C` together with an ear: a path that leaves `C` at one state and rejoins it at the same or another state, through states off `C`. The subgraph `H` formed by `C` and the ear has exactly two cycles, `C` of length `a` and the ear's cycle of length `b`, and they share a state. By the same cycle expansion `det(I − xH) = 1 − x^a − x^b`, so `H` grows at the root of `x^{−a} + x^{−b} = 1`, and `G` grows at least that fast.

- Both cycles lie in `H`, so `a ≤ n` and `b ≤ n`.
- They cannot both have length `n`. If `a = n`, the cycle `C` uses every state, so the ear has no state of its own and is a single step between two states of `C`; for its cycle to have length `n` as well, that step would join a state to its successor on `C`, repeating a step of `C`, which a 0/1 matrix cannot do.
- The root of `x^{−a} + x^{−b} = 1` decreases as `a` or `b` grows, so the smallest case is `(a, b) = (n, n − 1)`: the root of `x^n − x − 1`.

So every 0/1 matrix on `n` states with growth above 1 grows at least at the root of `x^n − x − 1`. Applied to `U`, which has `T` states, this is the lower bound.

*The bound is attained.* The rule `1 → 2 → ⋯ → h → 1` together with the step `h → 2` has two cycles, the full one (area `T`) and `2 → ⋯ → h → 2` (area `T − 1`), sharing heights, so its denominator is `1 − x^{T−1} − x^T` and its growth is the root of `z^T − z − 1`. ∎

The census's own minimizers have the same shape with the heights visited in another order: at height 4, `1 → 3`, `2 → {1, 3}`, `3 → 4`, `4 → 2`, with cycles `1 3 4 2` (area 10) and `3 4 2` (area 9) and denominator `1 − x⁹ − x^10`. At `n = 3` states the lower bound is the plastic number itself, which is the minimum at height 2, where the rule has three cells in all.

## The census and the classical lists

### The ten smallest Pisot numbers

The ten smallest Pisot numbers, from Dufresnoy and Pisot's determination of all Pisot numbers below the golden ratio,[^pisot] all appear by height 4:

| rank | Pisot number | minimal polynomial | first height |
|---|---|---|---|
| 1 | 1.324718 (plastic) | `x³ − x − 1` | 2 |
| 2 | 1.380278 | `x⁴ − x³ − 1` | 3 |
| 3 | 1.443269 | `x⁵ − x⁴ − x³ + x² − 1` | 3 |
| 4 | 1.465571 (supergolden) | `x³ − x² − 1` | 2 |
| 5 | 1.501595 | `x⁶ − x⁵ − x⁴ + x² − 1` | 3 |
| 6 | 1.534158 | `x⁵ − x³ − x² − x − 1` | 3 |
| 7 | 1.545216 | `x⁷ − x⁶ − x⁵ + x² − 1` | 4 |
| 8 | 1.561752 | `x⁶ − 2x⁵ + x⁴ − x² + x − 1` | 4 |
| 9 | 1.570147 | `x⁵ − x⁴ − x² − 1` | 3 |
| 10 | 1.573679 | `x⁸ − x⁷ − x⁶ + x² − 1` | 4 |

### Salem numbers of small degree

- **Degrees 4 and 6.** A Salem number below 2 has Mahler measure below 2, so the coefficients `a_k` of its minimal polynomial of degree `d` satisfy `|a_k| ≤ 2 C(d, k)`. A search of every reciprocal polynomial of degree 4 and 6 within these bounds finds exactly 2 Salem numbers of degree 4 below 2, and 11 of degree 6.[^exec] The census finds both of degree 4 (`1.722084` at height 3, `1.883204` at height 4), and the 7 of degree 6 below the height-4 ceiling `1.927562` (`1.401268`, `1.506136`, `1.556030` at height 3; `1.582347`, `1.635573`, `1.781644`, `1.831076` at height 4). The other four, `1.946856` to `1.987793`, lie above that ceiling, so no rule on 4 heights reaches them.
- **Degree at most 8.** The smallest Salem number of degree at most 8 is `1.280638`, the root of `x⁸ − x⁵ − x⁴ − x³ + 1`;[^verger] it appears at height 4.
- **Lehmer's four.** Lehmer's 1933 paper found four small Salem numbers, of degrees 4, 6, 8 and 10: `1.722084`, `1.401268`, `1.280638` and Lehmer's number.[^verger-lehmer] All four are area growth constants, first at heights 3, 3, 4 and 5.
- **Salem numbers below 1.3 of degree at most 10.** Mossinghoff's table lists the 47 known Salem numbers below 1.3.[^mossinghoff] Six of them have degree at most 10, the most that height 4 allows. The census finds five by height 4:

| rank in Mossinghoff's table | Salem number | degree | first height |
|---|---|---|---|
| 1 | 1.176281 (Lehmer's number) | 10 | 5 |
| 5 | 1.216392 | 10 | 4 |
| 7 | 1.230391 | 10 | 4 |
| 19 | 1.261231 | 10 | 4 |
| 23 | 1.280638 | 8 | 4 |
| 41 | 1.293486 | 10 | 4 |

The one that height 4 misses is the first entry, Lehmer's number. Its degree fits the bound of height 4 exactly, and it lies inside the range of constants at height 4, which go down to `1.0758`, but no rule on 4 heights grows at it.

## The census at height 5

Every 0/1 rule of size 5 (`2^25`, about 33.5 million rules) was expanded and the distinct denominators kept: 4,712,674 of them, of degree up to 15. Each was factored and reduced to the minimal polynomial of its growth constant, as at height 4.[^exec]

| | through height 4 | new at height 5 |
|---|---|---|
| distinct growth constants | 6,294 | 4,128,493 |
| of full degree (10 at height 4, 15 at height 5) | 2,611 | 1,652,655 |
| Pisot | 91 | 266 |
| Salem | 33 | 165 |

Every constant of heights 1 to 4 appears again at height 5, since a smaller rule sits inside a larger one with the extra height unused, and the smallest constant is `1.048985`, the root of `z^15 − z − 1`, as the theorem requires.

### Lehmer's number first appears at height 5

No rule on 4 heights produces Lehmer's number and some rule on 5 heights does, so **its minimum height is 5**. One such rule (row = height, 1 = may be followed by that height):

```
1 → 4                 00010
2 → 4, 5              00011
3 → 1, 2, 3, 5        11101
4 → 1, 2              11000
5 → 2                 01000

denominator  1 − x³ − x⁵ − x⁶ − x⁷ + x⁸ + x⁹ + x^10 + x^12 − x^15
          =  −(x − 1)(x² − x + 1)(x² + x + 1) · (x^10 + x⁹ − x⁷ − x⁶ − x⁵ − x⁴ − x³ + x + 1)
```

The denominator has the full degree 15: Lehmer's polynomial of degree 10 times three cyclotomic factors, whose roots are roots of unity and do not change the growth.[^exec]

### The Salem numbers below 1.3 of degree at most 14

Salem polynomials have even degree, so degree 15 allows Salem numbers of degree up to 14. Mossinghoff's table has 11 such entries below 1.3,[^mossinghoff] and **all 11 appear by height 5**:

| rank in Mossinghoff's table | Salem number | degree | first height |
|---|---|---|---|
| 1 | 1.176281 (Lehmer's number) | 10 | 5 |
| 3 | 1.200027 | 14 | 5 |
| 4 | 1.202617 | 14 | 5 |
| 5 | 1.216392 | 10 | 4 |
| 7 | 1.230391 | 10 | 4 |
| 12 | 1.240726 | 12 | 5 |
| 15 | 1.255094 | 14 | 5 |
| 19 | 1.261231 | 10 | 4 |
| 21 | 1.267296 | 14 | 5 |
| 23 | 1.280638 | 8 | 4 |
| 41 | 1.293486 | 10 | 4 |

Of the 23 Salem numbers of degree 8 below 2, found by a complete search as for degrees 4 and 6, 21 appear through height 5: 12 at height 4 and 9 at height 5.[^exec] The other two:

- `1.994004`, the root of `x⁸ − 2x⁷ + x⁶ − 2x⁵ + x⁴ − 2x³ + x² − 2x + 1`, lies above the all-compositions constant of every height through 7 (`1.991964` at height 7) and below that of height 8 (`1.996031`), so no rule below height 8 reaches it.
- `1.955302`, the root of `x⁸ − 2x⁷ − x⁵ + 3x⁴ − x³ − 2x + 1`, lies below the ceiling of height 5, `1.965948`, and has degree 8, so both lower bounds on the minimum height allow height 5, yet no rule on 5 heights produces it. Its minimum height is at least 6.

### Two lower bounds on the minimum height

Every growth constant `ρ` has two lower bounds on its minimum height, both proved on this page:

- **the degree bound** - the first height `h` with `h(h+1)/2 ≥ deg ρ`;
- **the ceiling bound** - the first height whose all-compositions constant (golden, tribonacci, tetranacci, pentanacci, …) is at least `ρ`.

Through height 5 the larger of the two is the exact minimum height for almost every constant:[^exec]

| constants | first height = bound | 1 above | 2 above | 3 above |
|---|---|---|---|---|
| all others | 4,002,348 (96.8%) | 131,332 | 550 | 1 |
| Pisot | 293 | 64 | - | - |
| Salem | 154 | 44 | - | - |

The two families of Pisot numbers converging to the golden ratio from below, the roots of `x^n(x² − x − 1) + 1` and of `x^n(x² − x − 1) + (x² − 1)`,[^pisot] meet the bound for every member through degree 15: each first appears at the first height whose degree bound allows it, degree 3 at height 2, degrees 4 to 6 at height 3, 7 to 10 at height 4, and 11 to 15 at height 5.[^exec]

**Lehmer's number is the smallest constant that misses the bound**: degree 10 allows height 4, and it needs 5. Every other Salem exception is at least `1.448423`, and every Pisot exception at least `1.561752`, the eighth-smallest Pisot number, of degree 6, first at height 4 against a bound of 3.

## Related Concepts

- [[quadratic-min-height](pages/quadratic-min-height.md)] - the same rules counted by width, where the growth constant is the largest eigenvalue of the rule matrix itself.
- [[castle-by-area](pages/castle-by-area.md)] - castles counted by area.
- [[exact-height-castle-by-area](pages/exact-height-castle-by-area.md)] - the `h`-nacci constants, the ceiling at each height.
- [[plastic-number](pages/plastic-number.md)] - the smallest Pisot number, here the area growth constant of the rule "height 1 may not follow height 1" on 2 heights.
- [[reachable-field-census](pages/reachable-field-census.md)] - the number fields of the strip growth constants by width.
- [[castle-strip](pages/castle-strip.md)] - castle strips and their 0/1 rule matrices.

## Appearances in Sources

- [[verger-gaugry-2024-salem-minoration](pages/verger-gaugry-2024-salem-minoration.md)] - the definitions of Perron, Pisot and Salem numbers, Siegel's minimum, Lehmer's number and polynomial, Lehmer's four small Salem numbers, the minimum `1.280638` over degree at most 8, and the claimed Salem bound `1.08544`.
- [[pe502-pell-castle-strip](pages/pe502-pell-castle-strip.md)] - the transfer-matrix model of strips whose rules the census enumerates.

## Footnotes

[^exec]: Census (2026-09-25): Python 3 with NumPy and SymPy for every 0/1 matrix of size 1 to 4; at height 5, a C program enumerating all `2^25` matrices, each denominator from its 32 principal minors by fraction-free elimination, deduplicated by hashing, and each distinct denominator factored with python-flint and classified by its roots. Rechecked by execution (Python 3.11 with NumPy, SymPy and mpmath, 2026-10-16): the full census through height 4 (2, 8, 105 and 8,255 distinct denominators; 1, 3, 64 and 6,226 new constants with the degrees and the Pisot and Salem counts of the table; the smallest constants 1.324718, 1.134724, 1.075766; the largest the `h`-nacci constants); the first heights of the ten smallest Pisot numbers and of every Salem number named on this page; the complete searches for Salem numbers below 2 of degree 4, 6 and 8 (2, 11 and 23, through trace polynomials with one root in `(2, 2.5)` and the rest in `(−2, 2)`); the 4,712,674 distinct denominators at height 5, and, by evaluating them at the reciprocals of the targets and confirming the smallest positive root, the first heights of Lehmer's number, of the 11 Salem numbers below 1.3 of degree at most 14, of the 23 Salem numbers of degree 8 below 2 (12 at height 4, 9 at height 5, `1.955302` and `1.994004` at neither) and of every member of the two Pisot families through degree 15; Lehmer's rule, expanded and factored with SymPy; the unrolling identity `det(I − xU)` equal to Equation (1) on 40 random rules of heights 2 to 4; the rule `1 → ⋯ → h → 1` plus `h → 2` with denominator `1 − x^(T−1) − x^T` for `h = 2..8`; the `h`-nacci constants for `h ≤ 8`. The height-5 factorization was not rerun, so the counts of new constants, of full degree, Pisot and Salem at height 5, the bound table and the smallest Pisot and Salem exceptions rest on the 2026-09-25 run.

[^verger-def]: [[verger-gaugry-2024-salem-minoration](pages/verger-gaugry-2024-salem-minoration.md)] §1 L50-56, L66-70, L121-132 - "A Salem number is an algebraic integer β > 1 such that its Galois conjugates β(i) satisfy: |β(i)| ≤ 1 for all i = 1, 2, . . ., m − 1, with m = deg(β) ≥ 4, β(0) = β and at least one conjugate β(i), i ≠ 0, on the unit circle", "All the Galois conjugates of a Salem number β lie on the unit circle, by pairs of complex conjugates, except 1/β", "The minimal polynomial Pβ(X) ∈ Z[X] of β is reciprocal"; "A Perron number is either 1 or a real algebraic integer θ > 1 such that the Galois conjugates θ(i), i ≠ 0, of θ(0) := θ satisfy: |θ(i)| < θ", "A Pisot number is a Perron number > 1 for which |θ(i)| < 1 for all i ≠ 0. The set of Pisot numbers admits the minorant Θ = 1.3247 . . ., unique root > 1 of X^3 − X − 1 by a result of Siegel"; "Salem [93] proved that the set S of Pisot numbers is closed"; "The smallest Salem number known is Lehmer's number τ := 1.17628 . . ., discovered by Lehmer in 1933 [63], with minimal polynomial (named \"Lehmer's polynomial\"): X^10 + X^9 − X^7 − X^6 − X^5 − X^4 − X^3 + X + 1."

[^pisot]: https://en.wikipedia.org/wiki/Pisot%E2%80%93Vijayaraghavan_number (read 2026-09-25) - "The smallest of them is the golden ratio" for the limit points, Dufresnoy and Pisot "determined all elements of S that are less than φ", the table "ten smallest Pisot numbers in increasing order", and the two families of Pisot numbers converging to the golden ratio.

[^lehmer]: https://en.wikipedia.org/wiki/Lehmer%27s_conjecture (read 2026-09-25) - the conjecture and Mahler measure, `M(P) = 1.176280818...` for Lehmer's polynomial, "It is widely believed that this example represents the true minimal value".

[^verger]: [[verger-gaugry-2024-salem-minoration](pages/verger-gaugry-2024-salem-minoration.md)] §3 p.9 L421-422 and Table 2 p.11 L496-504 - "The Salem numbers of degree ≤ 8 are all greater than 1.280638 . . . from [75]" (Mossinghoff's list); Table 2 lists `1.2806 . . .` with minimal polynomial `X⁸ − X⁵ − X⁴ − X³ + 1`.

[^verger-lehmer]: [[verger-gaugry-2024-salem-minoration](pages/verger-gaugry-2024-salem-minoration.md)] §3 p.11 Table 2 L496-504 - "The small Salem numbers, with their minimal polynomial, discovered by Lehmer in [63]": degrees 4, 6, 8, 10, `1.722 . . .`, `1.401 . . .`, `1.2806 . . .`, `1.17628 . . .`. The first heights are the census's own.

[^verger-thm]: [[verger-gaugry-2024-salem-minoration](pages/verger-gaugry-2024-salem-minoration.md)] §1 p.4 L152-155 - "Theorem 1.1 (ex-Lehmer conjecture for Salem numbers). The set T is bounded from below: β ∈ T ⟹ β > θ31⁻¹ = 1.08544 . . ." (arXiv v1 preprint); https://arxiv.org/pdf/2404.15927v2 (Douba and Huang, 2024; read 2026-10-09) p.2 - "Lehmer's conjecture for Salem numbers, or the Salem conjecture for short, asserts that the Salem numbers are bounded away from 1".

[^mossinghoff]: https://web.archive.org/web/20210509232916/http://www.cecm.sfu.ca/~mjm/Lehmer/lists/SalemList.html (Mossinghoff, "Small Salem Numbers"; read 2026-09-25) - "There are 47 known Salem numbers less than 1.3 ... This list is known to be complete for degree at most 44", with entries 1 (degree 10, 1.1762808182), 5 (10, 1.2163916611), 7 (10, 1.2303914344), 19 (10, 1.2612309611), 23 (8, 1.2806381562) and 41 (10, 1.2934859531) the only ones of degree at most 10.
