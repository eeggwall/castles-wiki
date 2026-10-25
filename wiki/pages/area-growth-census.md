---
title: Castle strips counted by area - the growth-constant census
category: Analyses
summary: Castle strips (skylines on the heights 1..h under a 0/1 rule saying which height may follow which) counted by area instead of width - which growth constants appear, and at what smallest height. The area generating function has denominator det(I − A diag(x, …, x^h)), which expands over the principal minors of the rule, so the census of every rule through height 5 (33.6 million rules) is exhaustive. Three lower bounds predict the minimum height of a constant - the degree bound (degree at most the triangle number T = h(h+1)/2), the ceiling bound (at most the h-nacci constant) and the norm bound (the norm divides the top coefficient of the denominator, at most 1, 1, 2, 3, 5 in absolute value at heights 1 to 5). The smallest constant above 1 at height h is proved to be the root of z^T − z − 1 (1.3247, 1.1347, 1.0758, 1.0490 at heights 2 to 5), and by Selmer's irreducibility theorem it first appears exactly at height h. Heights 1 to 5 give 1, 3, 64, 6,226 and 4,128,491 new growth constants. The census reaches all ten of the ten smallest Pisot numbers by height 4 and all 11 known Salem numbers below 1.3 of degree at most 14 by height 5; Lehmer's number 1.17628 first appears at height 5, with denominator Lehmer's polynomial times three cyclotomic factors at the full degree 15. Allowing a step never lowers the growth, so a search from the all-ones rule settles the Salem numbers near the ceiling beyond height 5: 1.955302, 1.963553 and 1.974819 first appear at height 6, 1.987793 at 7 and 1.994004 at 8, and every Salem number of degree 4, 6 or 8 below 2 (2, 11 and 23 of them) has a known minimum height. The largest of the three bounds is the exact minimum height for 96.8% of the constants and no constant needs more than two extra heights; Lehmer's number is the smallest Salem number that needs one. Against complete lists the bounds are far from sufficient: of the Perron numbers in (1, 2) they allow by height 5, 10 of 29 cubic and 34 of 288 quartic ones appear. The 1,112 periodic constants through height 5, with minimal polynomial in z^p, are the only ones that are not Perron numbers.
tags: [analysis, castle, castle-strip, area, generating-function, transfer-matrix, growth-constant, perron-number, pisot-number, salem-number, lehmer, mahler-measure, norm, plastic-number, supergolden, n-nacci, selmer, census, exhaustive-search, min-height, implementation, verification]
sources: [verger-gaugry-2024-salem-minoration, pe502-pell-castle-strip]
created: 2026-09-25
updated: 2026-10-25
---

# Castle strips counted by area - the growth-constant census

## The question

A castle strip on the heights `1, …, h` is a skyline with column heights in `{1, …, h}`, under a rule given by an `h × h` matrix `A` of 0s and 1s: a 1 in row `a`, column `b` means a column of height `a` may be followed by one of height `b`. Strips need not reach height `h`, so they need not be castles of height `h` ([[castle-strip](pages/castle-strip.md)]). [[quadratic-min-height](pages/quadratic-min-height.md)] counts strips by **width**. This page counts them by **area**, the total number of cells, the grading of [[castle-by-area](pages/castle-by-area.md)].

The number of strips of area `n` grows like `ρ^n`, and `ρ` is the rule's **area growth constant**. The question: **which numbers `ρ` appear, and what is the smallest height at which each first appears?** The census is exhaustive through height 5.

Three lower bounds on the minimum height, from the degree of `ρ`, from the `h`-nacci ceiling and from the norm of `ρ`, predict the answer. At the bottom of each height's range the prediction is a theorem: the smallest constant above 1 at height `h` is the root of `z^T − z − 1`, `T = h(h+1)/2`, and it first appears at height `h`. Through height 5 the census tests the prediction on every constant and against the classical lists of Pisot and Salem numbers: it is exact for 96.8% of the constants, no constant needs more than two extra heights, and Lehmer's number is the smallest Salem number that needs one. Beyond height 5, a search that stays close to the all-ones rule settles the Salem numbers near the ceiling, so every Salem number of degree 4, 6 or 8 below 2 has a known minimum height, up to 8. Tested from the other side, against every Perron number of degree 3 and 4 below 2, the bounds are far from sufficient: of the Perron numbers they allow by height 5, 10 of 29 cubic and 34 of 288 quartic ones appear.

## Terms used on this page

- **Minimal polynomial, conjugates** - the growth constant `ρ` is a root of an integer polynomial; the monic one of lowest degree is its minimal polynomial, and that polynomial's other roots are the conjugates of `ρ`. The golden mean `1.618` has minimal polynomial `x² − x − 1` and one conjugate, `−0.618`.
- **Norm** - the product of `ρ` and its conjugates, which is `±` the constant term of its minimal polynomial. The golden mean has norm `1.618 × (−0.618) = −1`.
- **Perron number** - 1, or a real algebraic integer `θ > 1` whose conjugates all have absolute value less than `θ`.[^verger-def] An area growth constant above 1 is the largest eigenvalue of a nonnegative integer matrix (the unrolled table `U` in the proof of the theorem), so no conjugate is larger in absolute value. Through height 5 every one is a Perron number except the periodic constants, which have a conjugate of the same absolute value.
- **Pisot number** - a Perron number above 1 whose conjugates all lie strictly inside the unit circle. The smallest is the **plastic number** `1.3247`, the root of `x³ − x − 1` (Siegel), and the set of Pisot numbers is closed (Salem).[^verger-def] Its smallest limit point is the golden mean, and Dufresnoy and Pisot determined every Pisot number below it.[^pisot] The [[plastic-number](pages/plastic-number.md)] page has the castle readings of the plastic number.
- **Salem number** - an algebraic integer `β > 1` whose conjugates all have absolute value at most 1, with at least one on the unit circle. Its conjugates are `1/β` and pairs of complex conjugates on the unit circle, its minimal polynomial is reciprocal, and its degree is even and at least 4.[^verger-def]
- **Lehmer's number** - `1.17628…`, the largest root of Lehmer's polynomial `x^10 + x^9 − x^7 − x^6 − x^5 − x^4 − x^3 + x + 1`, the smallest known Salem number, found by Lehmer in 1933.[^verger-def] Lehmer's conjecture states that the **Mahler measure** of an integer polynomial (the product of the absolute values of its roots outside the unit circle) is either 1 or at least some constant above 1, believed to be `1.17628`.[^lehmer] The restriction to Salem numbers, that they are bounded away from 1, is the Salem conjecture; a 2024 preprint claims the bound `1.08544` ([[verger-gaugry-2024-salem-minoration](pages/verger-gaugry-2024-salem-minoration.md)]), and other authors state it as a conjecture.[^verger-thm]

## The generating function

Weight a column of height `j` by `x^j`. The strips counted by area have a generating function with denominator

```
det( I − A · diag(x, x², …, x^h) )  =  Σ over subsets S of {1, …, h} of  (−1)^|S| · det(A_S) · x^(Σ S)        (1)
```

where `A_S` is the principal submatrix of `A` on the heights in `S`. The right side is the expansion of `det(I − M)` over principal minors, with the diagonal weights pulled out of each minor, so the denominator needs only integer determinants of 0/1 submatrices. Its degree is at most `1 + 2 + ⋯ + h = T`, the `h`-th triangle number. The growth constant is `1/x*`, where `x*` is the smallest positive root of the denominator: there the largest eigenvalue of the weighted matrix reaches 1.[^exec]

## Three lower bounds on the minimum height

A rule on `h` heights limits the size, the degree and the norm of its growth constant, so every constant has a smallest height at which it can appear:

- **The ceiling bound.** A rule on `h` heights counts a subset of the compositions (ordered sums) of the area with parts at most `h`, so its growth constant is at most the **`h`-nacci constant** of those compositions ([[castles-of-height-h-by-area](pages/castles-of-height-h-by-area.md)]): the golden mean `1.618` at `h = 2`, the tribonacci constant `1.839` at 3, the tetranacci constant `1.928` at 4, the pentanacci constant `1.966` at 5, always below 2. The all-ones rule attains it. A constant `ρ` first appears no earlier than the first height whose `h`-nacci constant is at least `ρ`.
- **The degree bound.** The minimal polynomial of the growth constant is the reversal of a factor of the denominator (1), so its degree is at most `T = h(h+1)/2`. A constant `ρ` first appears no earlier than the first height `h` with `T ≥ deg ρ`.
- **The norm bound.** The norm of the growth constant divides the top coefficient of the denominator (1), its coefficient of the highest power of `x` (proved in this section). A constant `ρ` first appears no earlier than the first height whose rules reach a top coefficient at least the norm of `ρ` in absolute value.

**Proposition.** The norm of a rule's growth constant `ρ > 1` divides the top coefficient of the rule's denominator (1).

*Proof.* Let `m(z)` be the minimal polynomial of `ρ`, of degree `d`, and `f(x) = x^d m(1/x)` its reversal. Since `m` is monic, `f` has integer coefficients, constant term 1 and leading coefficient `m(0)`, which is `±` the norm. The polynomial `f` is irreducible and vanishes at `1/ρ`, a root of the denominator `Q(x)`, so it divides `Q` over the rationals, and by Gauss's lemma over the integers, since its constant term 1 makes it primitive: `Q = f · g` with `g` an integer polynomial. Comparing leading coefficients, the top coefficient of `Q` is `m(0)` times the leading coefficient of `g`. ∎

The top coefficient is a signed sum of principal minors of `A`, so it stays small at small heights. The census gives its largest absolute value over all rules on `h` heights, and each value is the norm of some constant first at that height:[^exec]

| height | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|
| largest top coefficient, in absolute value | 1 | 1 | 2 | 3 | 5 |

So a constant of norm `±3` cannot appear before height 4. The Perron number `1.574743`, the root of `z³ − z² + z − 3`, has degree 3 and lies below the golden mean, so its degree and ceiling bounds both give height 2, but its norm 3 puts its predicted height at 4.

The largest of the three bounds is the **predicted height** of `ρ`. The `h`-nacci constant first appears at its predicted height `h`, since it exceeds the ceiling of every lower height. The next section proves the same for the smallest constant at each height, through the degree bound.

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

**Corollary.** For every `h ≥ 2`, the root of `z^T − z − 1` has degree `T` and first appears at height `h`, its predicted height.

*Proof.* Selmer proved that `z^n − z − 1` is irreducible over the rationals for every `n ≥ 2`,[^selmer] so the root has degree `T`. A rule on fewer than `h` heights has a denominator of degree at most `T − h` by Equation (1), less than `T`. ∎

The census's own minimizers have the same shape with the heights visited in another order: at height 4, `1 → 3`, `2 → {1, 3}`, `3 → 4`, `4 → 2`, with cycles `1 3 4 2` (area 10) and `3 4 2` (area 9) and denominator `1 − x⁹ − x^10`. At `n = 3` states the lower bound is the plastic number itself, which is the minimum at height 2, where the rule has three cells in all.

## The census through height 5

Every 0/1 rule of size 1 to 5 (2, 16, 512, 65,536 and `2^25` rules, the last about 33.5 million) was expanded by Equation (1), the distinct denominators factored exactly, and the factor carrying `x*` reversed to give the minimal polynomial of `ρ`. The first height at which a constant appears is its minimum height. A smaller rule sits inside a larger one with the extra heights unused, so every constant appears again at every larger height.[^exec]

| height | distinct denominators | new growth constants | degrees of the new constants | of full degree `T` | new Pisot | new Salem |
|---|---|---|---|---|---|---|
| 1 | 2 | 1 (the growth constant 1) | 1 | 1 | - | - |
| 2 | 8 | 3 | 2, 3 | 2 | 3 | 0 |
| 3 | 105 | 64 | 3 (5), 4 (7), 5 (23), 6 (29) | 29 | 14 | 4 |
| 4 | 8,255 | 6,226 | 2 to 10 | 2,611 | 74 | 29 |
| 5 | 4,712,674 | 4,128,491 | 4 to 15 | 1,652,655 | 266 | 165 |

Through height 5 there are 4,134,785 distinct growth constants, 91 Pisot and 33 Salem numbers among them by height 4, and 357 Pisot and 198 Salem numbers by height 5.

Height 2 gives exactly the golden mean, the plastic number and the supergolden constant `1.4656`, the root of `x³ − x² − 1`:

```
rule   growth                       denominator          reading
11     golden     1.618034          1 − x − x²           parts 1 and 2, anything goes
11
01     plastic    1.324718          1 − x² − x³          height 1 may not follow height 1
11
11     supergolden 1.465571         1 − x − x³           height 2 may not follow height 2
10
```

The largest constant at each height is the `h`-nacci constant: the tribonacci constant `1.839287` first at height 3, the tetranacci constant `1.927562` first at height 4 and the pentanacci constant `1.965948` first at height 5. The tribonacci constant cannot appear at height 2, because it exceeds the golden mean, the ceiling at height 2. The smallest constant above 1 at height 5 is `1.048985`, the root of `z^15 − z − 1`, as the theorem requires.

### Periodic constants

A growth constant whose minimal polynomial is a polynomial in `z^p` for some `p ≥ 2` is **periodic**. With `ρ` its minimal polynomial also has the root `ρ · e^{2πi/p}`, of the same absolute value, so a periodic constant is not a Perron number. At height 3 the rule `1 → 2`, `2 → {1, 3}`, `3 → 1` has the two cycles `1 2` (area 3) and `1 2 3` (area 6), which share heights, so its denominator is `1 − x³ − x⁶`, a polynomial in `x³`: the growth constant is `1.173985`, the cube root of the golden mean, with minimal polynomial `z⁶ − z³ − 1`. The new constant of degree 2 at height 4 is `√2`, from the rule `1 → 3`, `2, 3, 4 → {1, 2, 4}`, with denominator `1 − x² − 2x⁴ = (1 + x²)(1 − 2x²)`.

Through height 5 there are 1,112 periodic constants: 5 new at height 3, 45 at height 4 and 1,062 at height 5. For 898 of them `p = 2`, for 173 `p = 3`, and the largest `p` is 12. Every other constant through height 5 is a Perron number.[^exec]

## The census and the classical lists

### The ten smallest Pisot numbers

The ten smallest Pisot numbers, from Dufresnoy and Pisot's determination of all Pisot numbers below the golden mean,[^pisot] all appear by height 4:

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

- **Degrees 4 and 6.** A Salem number below 2 has Mahler measure below 2, so the coefficients `a_k` of its minimal polynomial of degree `d` satisfy `|a_k| ≤ 2 C(d, k)`. A search of every reciprocal polynomial of degree 4 and 6 within these bounds finds exactly 2 Salem numbers of degree 4 below 2, and 11 of degree 6.[^exec] The census finds both of degree 4 (`1.722084` at height 3, `1.883204` at height 4), and the 7 of degree 6 below the height-4 ceiling `1.927562` (`1.401268`, `1.506136`, `1.556030` at height 3; `1.582347`, `1.635573`, `1.781644`, `1.831076` at height 4). The other four, `1.946856`, `1.963553`, `1.974819` and `1.987793`, lie above that ceiling, so no rule on 4 heights reaches them; they first appear at heights 5, 6, 6 and 7 (section *Salem numbers near the ceiling*).
- **Degree 8.** The same search finds 23 Salem numbers of degree 8 below 2, and 21 of them appear through height 5: 12 at height 4 and 9 at height 5.[^exec] The smallest Salem number of degree at most 8 is `1.280638`, the root of `x⁸ − x⁵ − x⁴ − x³ + 1`;[^verger] it appears at height 4. The other two:
  - `1.994004`, the root of `x⁸ − 2x⁷ + x⁶ − 2x⁵ + x⁴ − 2x³ + x² − 2x + 1`, lies above the all-compositions constant of every height through 7 (`1.991964` at height 7) and below that of height 8 (`1.996031`), so no rule below height 8 reaches it. It first appears at height 8.
  - `1.955302`, the root of `x⁸ − 2x⁷ − x⁵ + 3x⁴ − x³ − 2x + 1`, lies below the ceiling of height 5, `1.965948`, and has degree 8, so its predicted height is 5, yet no rule on 5 heights produces it. It first appears at height 6.
- **Lehmer's four.** Lehmer's 1933 paper found four small Salem numbers, of degrees 4, 6, 8 and 10: `1.722084`, `1.401268`, `1.280638` and Lehmer's number.[^verger-lehmer] All four are area growth constants, first at heights 3, 3, 4 and 5.

### Salem numbers near the ceiling

Six Salem numbers of degree 6 and 8 below 2 lie above the tetranacci ceiling `1.927562`. The census through height 5 finds one of them, `1.946856`; three lie above the pentanacci ceiling `1.965948`, and two lie below it but do not appear by height 5. A search that stays close to the all-ones rule settles all six.

**Lemma.** Allowing one more step never lowers the growth constant of a rule.

*Proof.* Every strip of the old rule is a strip of the new one, so the number of strips of each area can only grow. ∎

So if a rule on `h` heights grows at least as fast as a target `β`, so does every rule that allows more steps. A depth-first search from the all-ones rule that turns 1s into 0s in a fixed order of the entries, and backtracks as soon as the growth falls below `β`, visits each such rule exactly once. The growth is at least `β` exactly when the weighted matrix `A · diag(x, x², …, x^h)` at `x = 1/β` has largest eigenvalue at least 1. A visited rule grows at exactly `β` when that eigenvalue is 1, and each such rule is confirmed by exact division of its denominator (1) by the minimal polynomial of `β`. Near the ceiling the visited set is small:[^exec]

| Salem number | degree | predicted height | height searched | rules with growth at least `β` | rules with growth `β` |
|---|---|---|---|---|---|
| 1.946856 | 6 | 5 | 5 | 208 | 6 |
| 1.955302 | 8 | 5 | 5 | 44 | 0 |
| | | | 6 | 308,963 | 34 |
| 1.963553 | 6 | 5 | 5 | 2 | 0 |
| | | | 6 | 62,092 | 32 |
| 1.974819 | 6 | 6 | 6 | 1,960 | 8 |
| 1.987793 | 6 | 7 | 7 | 29,970 | 20 |
| 1.994004 | 8 | 8 | 8 | 773,528 | 20 |

Out of `2^25`, `2^36`, `2^49` and `2^64` rules at heights 5 to 8, no search visits more than 773,528. So `1.955302` and `1.963553` first appear at height 6, one height after their predicted height 5, and the other four first appear at their predicted heights.

Four of the six, and both Salem numbers of degree 4 below 2, come from one family of rules. The all-ones rule on `h` heights without the step `1 → h` (height `h` may not follow height 1) has denominator `1 − x − x² − ⋯ − x^h + x^(h+1)`, and its growth constant is a Salem number at every height from 3 to 10:[^exec]

| `h` | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|
| growth constant | 1.722084 | 1.883204 | 1.946856 | 1.974819 | 1.987793 | 1.994004 | 1.997032 | 1.998525 |
| degree | 4 | 4 | 6 | 6 | 6 | 8 | 10 | 10 |

Each lies above the ceiling of height `h − 1`, so each first appears at height `h`, its predicted height. With the census, every Salem number of degree 4, 6 or 8 below 2 has a minimum height:

| degree | Salem numbers below 2 | first at height 3 | 4 | 5 | 6 | 7 | 8 | after the predicted height |
|---|---|---|---|---|---|---|---|---|
| 4 | 2 | 1 | 1 | - | - | - | - | 0 |
| 6 | 11 | 3 | 4 | 1 | 2 | 1 | - | 5 |
| 8 | 23 | - | 12 | 9 | 1 | - | 1 | 10 |

### The Salem numbers below 1.3

Mossinghoff's table lists the 47 known Salem numbers below 1.3.[^mossinghoff] Salem polynomials have even degree, so the degree bound allows Salem numbers of degree up to 10 at height 4 and up to 14 at height 5. The table has 11 entries of degree at most 14, and **all 11 appear by height 5**. Six of them have degree at most 10, and height 4 has five of those:

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

The one of degree at most 10 that height 4 misses is Lehmer's number. Its degree fits the bound of height 4 exactly, and it lies inside the range of constants at height 4, which go down to `1.0758`, but no rule on 4 heights grows at it.

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

## How well the bounds predict

Through height 5 the predicted height is the exact minimum height of 96.8% of the 4,134,784 constants above 1, and no constant first appears more than two heights after it:[^exec]

| constants | at the predicted height | 1 height later | 2 heights later |
|---|---|---|---|
| Pisot | 293 | 64 | - |
| Salem | 154 | 44 | - |
| all others | 4,003,168 | 130,617 | 444 |

The norm bound moves 820 constants onto their predicted height. With the degree and ceiling bounds alone, the last row reads 4,002,348, 131,332 and 549.

The two families of Pisot numbers converging to the golden mean from below, the roots of `x^n(x² − x − 1) + 1` and of `x^n(x² − x − 1) + (x² − 1)`,[^pisot] first appear at their predicted heights for every member through degree 15: degree 3 at height 2, degrees 4 to 6 at height 3, 7 to 10 at height 4, and 11 to 15 at height 5.[^exec]

The constants that first appear late start well below Lehmer's number. The smallest is `1.060063`, the root of `z^10 + z^8 − z^4 − z^2 − 1`, of degree 10, which first appears at height 5 against a predicted 4. It is periodic: its square `1.123733`, the root of `z⁵ + z⁴ − z² − z − 1`, first appears at height 4 against a predicted 3. The smallest Perron number among them is `1.081529`, the root of `z⁹ + z⁸ − z⁶ − z⁵ + z³ − z − 1`, also predicted at height 4 and first at 5. In all, 93 constants below Lehmer's number first appear late, 92 of them by one height, and 21 of the 93 are periodic.

**Lehmer's number is the smallest Salem number that first appears late**: degree 10 predicts height 4, and it needs 5. Every other Salem exception is at least `1.448423`, and every Pisot exception at least `1.561752`, the eighth-smallest Pisot number, of degree 6, first at height 4 against a predicted 3.

### Which Perron numbers appear

The predicted-height table counts only the constants that some rule produces, so it cannot see a number that the bounds allow and no rule reaches. A complete list of Perron numbers tests the prediction from that side. A Perron number below 2 has all its conjugates below 2 in absolute value, so the coefficients `a_k` of its minimal polynomial of degree `d` satisfy `|a_k| ≤ 2^k C(d, k)`, and a search of that box finds every one: 31 of degree 3 in `(1, 2)` and 444 of degree 4.[^exec]

| degree | Perron numbers in `(1, 2)` | predicted height at most 5 | appear by height 5 | at the predicted height | later |
|---|---|---|---|---|---|
| 3 | 31 | 29 | 10 | 6 | 4 |
| 4 | 444 | 288 | 34 | 14 | 20 |

Most of the Perron numbers that the bounds allow do not appear by height 5: 19 of the 29 cubic ones and 254 of the 288 quartic ones. The norm separates the cubic ones almost completely. The ten that appear have norm `±1` or `±2`. Of the 19 that the bounds allow and no rule produces, 18 have norm 3, 4 or 5 in absolute value, and the other is the unit `1.879385 = 2 cos 20°`, the root of `z³ − 3z − 1`, predicted at height 4. The quartic ones that appear have norm at most 3 in absolute value, but 103 of the absent quartic ones have norm `±1` or `±2`.

The ten cubic Perron numbers that are area growth constants through height 5:

| Perron number | minimal polynomial | norm | predicted height | first height |
|---|---|---|---|---|
| 1.324718 (plastic) | `z³ − z − 1` | 1 | 2 | 2 |
| 1.353210 | `z³ − z² + z − 2` | 2 | 3 | 4 |
| 1.465571 (supergolden) | `z³ − z² − 1` | 1 | 2 | 2 |
| 1.521380 | `z³ − z − 2` | 2 | 3 | 3 |
| 1.543689 | `z³ − 2z² + 2z − 2` | 2 | 3 | 4 |
| 1.695621 | `z³ − z² − 2` | 2 | 3 | 3 |
| 1.754878 | `z³ − 2z² + z − 1` | 1 | 3 | 3 |
| 1.769292 | `z³ − 2z − 2` | 2 | 3 | 4 |
| 1.801938 | `z³ − z² − 2z + 1` | −1 | 3 | 4 |
| 1.839287 (tribonacci) | `z³ − z² − z − 1` | 1 | 3 | 3 |

## Related Concepts

- [[quadratic-min-height](pages/quadratic-min-height.md)] - the same rules counted by width, where the growth constant is the largest eigenvalue of the rule matrix itself.
- [[castle-by-area](pages/castle-by-area.md)] - castles counted by area.
- [[castles-of-height-h-by-area](pages/castles-of-height-h-by-area.md)] - the `h`-nacci constants, the ceiling at each height.
- [[plastic-number](pages/plastic-number.md)] - the smallest Pisot number, here the area growth constant of the rule "height 1 may not follow height 1" on 2 heights.
- [[reachable-field-census](pages/reachable-field-census.md)] - the number fields of the strip growth constants by width.
- [[castle-strip](pages/castle-strip.md)] - castle strips and their 0/1 rule matrices.

## Appearances in Sources

- [[verger-gaugry-2024-salem-minoration](pages/verger-gaugry-2024-salem-minoration.md)] - the definitions of Perron, Pisot and Salem numbers, Siegel's minimum, Lehmer's number and polynomial, Lehmer's four small Salem numbers, the minimum `1.280638` over degree at most 8, and the claimed Salem bound `1.08544`.
- [[pe502-pell-castle-strip](pages/pe502-pell-castle-strip.md)] - the transfer-matrix model of strips whose rules the census enumerates.

## Footnotes

[^exec]: Census (2026-10-25): a C program enumerating every 0/1 matrix of size 1 to 5, each denominator from its principal minors by fraction-free elimination, keeping the distinct denominators (2, 8, 105, 8,255 and 4,712,674); each distinct denominator factored with python-flint 0.9.0 and the factor carrying `x*` chosen by certified complex root isolation. Every growth constant rechecked against the largest eigenvalue modulus of the reversed denominator (NumPy): all agree to within `10⁻⁶` except 65 whose minimal polynomial divides the denominator three to five times, where the eigenvalue solver loses precision. From this census: the counts of new constants, degrees, full degrees, Pisot and Salem numbers; the smallest and largest constants at each height; the first heights of the ten smallest Pisot numbers, of every Salem number named on this page and of every member of the two Pisot families through degree 15, each looked up by its exact minimal polynomial; the predicted-height table and the late constants; the largest top coefficient at each height, over every rule; the norms; the periodic constants, whose minimal polynomials have exponents with a common factor `p ≥ 2`, and for every other constant a largest root strictly larger in absolute value than all its conjugates (NumPy). The complete lists of Perron numbers of degree 3 and 4 in `(1, 2)` come from every monic integer polynomial in the coefficient box, kept when it is irreducible (python-flint) with a real root in `(1, 2)` strictly larger in absolute value than every other root, and are matched to the census by exact minimal polynomial. The complete searches for Salem numbers below 2 of degree 4, 6 and 8 (2, 11 and 23) run through trace polynomials with one root in `(2, 2.5)` and the rest in `(−2, 2)`. Lehmer's rule expanded and factored with python-flint; the unrolling identity `det(I − xU)` equal to Equation (1) on 200 random rules of heights 2 to 5; the rule `1 → ⋯ → h → 1` plus `h → 2` with denominator `1 − x^(T−1) − x^T` for `h = 2..8`; the `h`-nacci constants for `h ≤ 9`; `z^n − z − 1` irreducible for `n = 3, 6, 10, 15, 21, 28, 36` (SymPy). The search near the ceiling: depth-first from the all-ones rule, entries removed in row-major order, growth at least `β` tested by the largest eigenvalue modulus of `A · diag(1/β, …, 1/β^h)` against 1 with tolerance `10⁻¹²` (NumPy), and each rule within `10⁻⁹` of 1 checked by exact division of its denominator by the minimal polynomial of `β` (python-flint); its results at height 5 agree with the census. The rule without `1 → h` expanded for `h = 3..10`, each denominator equal to `1 − x − ⋯ − x^h + x^(h+1)`, and the factor carrying the largest root reciprocal with every root except that root and its reciprocal on the unit circle.

[^selmer]: https://journals.msp.org/mscand/article/view/2841 (E. S. Selmer, "On the irreducibility of certain trinomials", Math. Scand. 4 (1956) 287-302; read 2026-10-25) §3 p.289 - "Theorem 1. The polynomials f₁(x) = xⁿ − x − 1 are irreducible for all n."

[^verger-def]: [[verger-gaugry-2024-salem-minoration](pages/verger-gaugry-2024-salem-minoration.md)] §1 L50-56, L66-70, L121-132 - "A Salem number is an algebraic integer β > 1 such that its Galois conjugates β(i) satisfy: |β(i)| ≤ 1 for all i = 1, 2, . . ., m − 1, with m = deg(β) ≥ 4, β(0) = β and at least one conjugate β(i), i ≠ 0, on the unit circle", "All the Galois conjugates of a Salem number β lie on the unit circle, by pairs of complex conjugates, except 1/β", "The minimal polynomial Pβ(X) ∈ Z[X] of β is reciprocal"; "A Perron number is either 1 or a real algebraic integer θ > 1 such that the Galois conjugates θ(i), i ≠ 0, of θ(0) := θ satisfy: |θ(i)| < θ", "A Pisot number is a Perron number > 1 for which |θ(i)| < 1 for all i ≠ 0. The set of Pisot numbers admits the minorant Θ = 1.3247 . . ., unique root > 1 of X^3 − X − 1 by a result of Siegel"; "Salem [93] proved that the set S of Pisot numbers is closed"; "The smallest Salem number known is Lehmer's number τ := 1.17628 . . ., discovered by Lehmer in 1933 [63], with minimal polynomial (named \"Lehmer's polynomial\"): X^10 + X^9 − X^7 − X^6 − X^5 − X^4 − X^3 + X + 1."

[^pisot]: https://en.wikipedia.org/wiki/Pisot%E2%80%93Vijayaraghavan_number (read 2026-09-25) - "The smallest of them is the golden ratio" for the limit points, Dufresnoy and Pisot "determined all elements of S that are less than φ", the table "ten smallest Pisot numbers in increasing order", and the two families of Pisot numbers converging to the golden mean.

[^lehmer]: https://en.wikipedia.org/wiki/Lehmer%27s_conjecture (read 2026-09-25) - the conjecture and Mahler measure, `M(P) = 1.176280818...` for Lehmer's polynomial, "It is widely believed that this example represents the true minimal value".

[^verger]: [[verger-gaugry-2024-salem-minoration](pages/verger-gaugry-2024-salem-minoration.md)] §3 p.9 L421-422 and Table 2 p.11 L496-504 - "The Salem numbers of degree ≤ 8 are all greater than 1.280638 . . . from [75]" (Mossinghoff's list); Table 2 lists `1.2806 . . .` with minimal polynomial `X⁸ − X⁵ − X⁴ − X³ + 1`.

[^verger-lehmer]: [[verger-gaugry-2024-salem-minoration](pages/verger-gaugry-2024-salem-minoration.md)] §3 p.11 Table 2 L496-504 - "The small Salem numbers, with their minimal polynomial, discovered by Lehmer in [63]": degrees 4, 6, 8, 10, `1.722 . . .`, `1.401 . . .`, `1.2806 . . .`, `1.17628 . . .`. The first heights are the census's own.

[^verger-thm]: [[verger-gaugry-2024-salem-minoration](pages/verger-gaugry-2024-salem-minoration.md)] §1 p.4 L152-155 - "Theorem 1.1 (ex-Lehmer conjecture for Salem numbers). The set T is bounded from below: β ∈ T ⟹ β > θ31⁻¹ = 1.08544 . . ." (arXiv v1 preprint); https://arxiv.org/pdf/2404.15927v2 (Douba and Huang, 2024; read 2026-10-09) p.2 - "Lehmer's conjecture for Salem numbers, or the Salem conjecture for short, asserts that the Salem numbers are bounded away from 1".

[^mossinghoff]: https://web.archive.org/web/20210509232916/http://www.cecm.sfu.ca/~mjm/Lehmer/lists/SalemList.html (Mossinghoff, "Small Salem Numbers"; read 2026-10-25) - "There are 47 known Salem numbers less than 1.3 ... This list is known to be complete for degree at most 44", with entries 1 (degree 10, 1.1762808182), 3 (14, 1.2000265239), 4 (14, 1.2026167436), 5 (10, 1.2163916611), 7 (10, 1.2303914344), 12 (12, 1.2407264236), 15 (14, 1.2550935167), 19 (10, 1.2612309611), 21 (14, 1.2672964425), 23 (8, 1.2806381562) and 41 (10, 1.2934859531) the only ones of degree at most 14.
