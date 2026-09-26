---
title: Castle strips counted by area - the growth-constant census
category: Analyses
summary: Count castle strips (a 0/1 rule saying which column heights may follow which) by total area instead of width, and ask which growth constants appear and at what smallest height. The area generating function has denominator det(I - A diag(x, ..., x^h)), which expands over principal minors of the 0/1 rule, so an exhaustive census of every rule up to height 4 (66,066 rules) is cheap. Heights 1 to 4 give 1, 3, 64 and 6,226 new growth constants, of degree up to the triangle number T = h(h+1)/2 (2,611 of the 6,226 at height 4 have the full degree 10). The smallest constant at each height is the root of z^T - z - 1 (1.3247, 1.1347, 1.0758 at heights 2, 3, 4), realized by a cycle through every height plus a cycle skipping height 1; the largest is the h-nacci constant of all compositions with parts at most h. The census meets two classical lists. All ten of the ten smallest Pisot numbers (Dufresnoy-Pisot) appear by height 4 - plastic and supergolden at 2, five more at 3, three at 4. Among Salem numbers it finds every one of degree 4 and 6 below the height-4 ceiling 1.9276 (2 of degree 4, 7 of degree 6, checked against a complete search), the smallest Salem number of degree at most 8 (1.280638), and five of the six known Salem numbers below 1.3 of degree at most 10 - the one missing is Lehmer's number 1.17628, the smallest known Salem number, whose degree 10 fits at height 4 but which no height-4 rule produces.
tags: [analysis, castle, castle-strip, area, generating-function, transfer-matrix, growth-constant, perron-number, pisot-number, salem-number, lehmer, mahler-measure, plastic-number, supergolden, n-nacci, census, exhaustive-search, min-height, implementation, verification]
sources: [oeis-mining-pe502]
created: 2026-09-25
updated: 2026-09-25
---

# Castle strips counted by area - the growth-constant census

## The question in plain words

A **castle strip** is a row of columns with heights `1..h` and a rule saying which heights may stand next to each other: an `h x h` table `A` of 0s and 1s, with a 1 in row `a`, column `b` meaning "height `a` may be followed by height `b`" ([[castle-strip](pages/castle-strip.md)]). [[quadratic-min-height](pages/quadratic-min-height.md)] counted strips by **width**. This page counts them by **area** - the total number of cells, the sum of the column heights - the grading of [[castle-by-area](pages/castle-by-area.md)].

The number of strips of area `n` grows like `ρ^n`, and `ρ` is the rule's **area growth constant**. The question: **which numbers `ρ` appear, and what is the smallest height `h` at which each one first appears?** This page is the first stage, an exhaustive census of every rule up to height 4.

## Terms used on this page

- **Minimal polynomial, conjugates** - a growth constant `ρ` is a root of an integer polynomial; the lowest-degree monic one is its minimal polynomial, and that polynomial's other roots are the conjugates of `ρ`. The golden ratio `1.618` has minimal polynomial `x^2 - x - 1` and one conjugate, `-0.618`.
- **Perron number** - a real algebraic integer above 1 whose conjugates are all strictly smaller in size. Every growth constant above 1 of a 0/1 rule is the largest eigenvalue of a nonnegative integer matrix (see the unrolling under What comes next), so its conjugates are at most as large; Pisot and Salem numbers are the special cases where they are pinned inside or on the unit circle.
- **Pisot number** - an algebraic integer above 1 whose conjugates all lie strictly inside the unit circle.[^pisot] Their powers come exponentially close to whole numbers, because the power sums of all the roots are integers and the conjugates' powers vanish; Pisot proved that this near-integer property essentially characterizes them. The set of Pisot numbers is closed (Salem), its smallest member is the **plastic number** `1.3247`, root of `x^3 - x - 1` (Siegel), its smallest limit point is the golden ratio, and Dufresnoy and Pisot found every Pisot number below the golden ratio.[^pisot] The [[plastic-number](pages/plastic-number.md)] page has the castle side of the plastic number.
- **Salem number** - an algebraic integer above 1 whose conjugates all have size at most 1, with at least one of size exactly 1.[^salem] The minimal polynomial is then palindromic (it reads the same backwards), `1/ρ` is also a root, and every other root lies on the unit circle; the degree is even and at least 4. Salem numbers sit on the border between "powers approach integers" and "powers spread out", which is why they matter in Diophantine approximation and harmonic analysis, and every Pisot number is a limit of Salem numbers.[^pisot][^salem]
- **Lehmer's number** - `1.17628...`, the largest root of `x^10 + x^9 - x^7 - x^6 - x^5 - x^4 - x^3 + x + 1`, the smallest Salem number known.[^salem] **Lehmer's conjecture** (open since 1933) says nothing smaller exists, in a stronger form: every integer polynomial whose roots are not all roots of unity has **Mahler measure** (the product of the sizes of its roots outside the unit circle) at least some fixed constant above 1, believed to be exactly `1.17628`. By Lind's work the answer decides whether a class of dynamical systems, automorphisms of compact groups, can have arbitrarily small positive entropy.[^lehmer]

## The generating function, and why the census is cheap

Weight a column of height `j` by `x^j`. The strips counted by area have generating function with denominator

```
det( I - A · diag(x, x^2, ..., x^h) )  =  sum over subsets S of {1..h} of  (-1)^|S| · det(A restricted to S) · x^(sum of S)
```

The second form is the expansion of `det(I - M)` over principal minors, with the diagonal weights pulled out of each minor. So the denominator needs only integer determinants of 0/1 submatrices. Its degree is at most `1 + 2 + ... + h = T`, the `h`-th triangle number. The growth constant is `1/x*`, where `x*` is the smallest positive root: that is where the weighted rule table's largest eigenvalue reaches 1, and the series stops converging.[^exec]

Two bounds hold for every rule at height `h`:

- A height-`h` rule counts a subset of the compositions (ordered sums) of the area into parts at most `h`, so its growth constant is at most the **h-nacci constant** of those compositions ([[bounded-height-castles-nacci](pages/bounded-height-castles-nacci.md)]): `1.618` (golden) at `h = 2`, `1.839` (tribonacci) at 3, `1.928` (tetranacci) at 4, always below 2. The all-ones rule attains it.
- The minimal polynomial has degree at most `T = h(h+1)/2`.

## The census through height 4

Every 0/1 rule of size 1 to 4 (2, 16, 512 and 65,536 rules) was expanded, the distinct denominators factored exactly, and the factor carrying `x*` reversed to give the minimal polynomial of `ρ`. The first height at which a constant appears is its minimum height, for every constant reached by height 4.

| height | distinct denominators | new growth constants | degrees of the new constants | new Pisot | new Salem |
|---|---|---|---|---|---|
| 1 | 2 | 1 (growth 1) | 1 | - | - |
| 2 | 8 | 3 | 2, 3 | 3 | 0 |
| 3 | 105 | 64 | 3 (5), 4 (7), 5 (23), 6 (29) | 14 | 4 |
| 4 | 8,255 | 6,226 | 2 to 10; 2,611 of degree 10 | 74 | 29 |

Height 2 gives exactly the golden ratio, the plastic number and the supergolden ratio `1.4656` (root of `x^3 - x^2 - 1`):

```
rule   growth                       denominator          reading
11     golden     1.618034          1 - x - x^2          parts 1 and 2, anything goes
11
01     plastic    1.324718          1 - x^2 - x^3        height 1 may not follow height 1
11
11     supergolden 1.465571         1 - x - x^3          height 2 may not follow height 2
10
```

The largest constant at each height is the h-nacci constant (tribonacci `1.839287` first at height 3, tetranacci `1.927562` first at height 4). Tribonacci cannot appear at height 2, because `1 - x - x^2 - x^3` would need a 2 in the rule table.

The count explodes with height: most constants at height 4 have the full degree 10. That growth is what makes a height-5 census (degree up to 15, 33.5 million rules) a separate decision.

## The smallest constant at each height

The smallest growth constant above 1 at each height is the root of

```
z^T - z - 1,     T = h(h+1)/2
h = 2:  1.324718  (z^3 - z - 1, the plastic number)
h = 3:  1.134724  (z^6 - z - 1)
h = 4:  1.075766  (z^10 - z - 1)
```

The rules that realize it have one shape: a cycle through every height (area `T`) and a second cycle that skips height 1 (area `T - 1`). The denominator is `1 - x^(T-1) - x^T`. At height 4 the rule is `1 -> 3`, `2 -> 1 or 3`, `3 -> 4`, `4 -> 2`: the cycle `1 3 4 2` has area 10, and `3 4 2` has area 9. That this is the minimum at every height is observed through height 4, not yet proved.

## The census meets the classical lists

### The ten smallest Pisot numbers

Wikipedia lists the ten smallest Pisot numbers, from Dufresnoy and Pisot's determination of all Pisot numbers below the golden ratio.[^pisot] All ten appear by height 4:

| rank | Pisot number | minimal polynomial | first height |
|---|---|---|---|
| 1 | 1.324718 (plastic) | `x^3 - x - 1` | 2 |
| 2 | 1.380278 | `x^4 - x^3 - 1` | 3 |
| 3 | 1.443269 | `x^5 - x^4 - x^3 + x^2 - 1` | 3 |
| 4 | 1.465571 (supergolden) | `x^3 - x^2 - 1` | 2 |
| 5 | 1.501595 | `x^6 - x^5 - x^4 + x^2 - 1` | 3 |
| 6 | 1.534158 | `x^5 - x^3 - x^2 - x - 1` | 3 |
| 7 | 1.545216 | `x^7 - x^6 - x^5 + x^2 - 1` | 4 |
| 8 | 1.561752 | `x^6 - 2x^5 + x^4 - x^2 + x - 1` | 4 |
| 9 | 1.570147 | `x^5 - x^4 - x^2 - 1` | 3 |
| 10 | 1.573679 | `x^8 - x^7 - x^6 + x^2 - 1` | 4 |

### Salem numbers of small degree

- **Degree 4 and 6, completely.** A search of every palindromic polynomial of degree 4 and 6 with coefficients inside the proven bound `|a_k| <= 2 C(d, k)` (the Mahler-measure bound for a Salem number below 2) finds exactly 2 Salem numbers of degree 4 below 2 and 11 of degree 6.[^exec] The census finds both of degree 4 (`1.722084` at height 3, `1.883204` at height 4) and the 7 of degree 6 below the height-4 ceiling `1.927562` (`1.401268`, `1.506136`, `1.556030` at height 3; `1.582347`, `1.635573`, `1.781644`, `1.831076` at height 4). The four it misses, `1.946856` to `1.987793`, all lie above that ceiling, so no height-4 rule can reach them.
- **Degree at most 8.** The smallest Salem number of degree at most 8 is `1.280638`, root of `x^8 - x^5 - x^4 - x^3 + 1`;[^verger] it appears at height 4.
- **The small Salem numbers of degree at most 10.** Mossinghoff's table lists the 47 known Salem numbers below 1.3 ("small" Salem numbers).[^mossinghoff] Six of them have degree at most 10, the most that height 4 allows. The census finds five:

| rank in Mossinghoff's table | Salem number | degree | first height |
|---|---|---|---|
| 1 | 1.176280 (Lehmer's number) | 10 | **not by height 4** |
| 5 | 1.216391 | 10 | 4 |
| 7 | 1.230391 | 10 | 4 |
| 19 | 1.261230 | 10 | 4 |
| 23 | 1.280638 | 8 | 4 |
| 41 | 1.293485 | 10 | 4 |

The one it misses is the first entry, Lehmer's number. Its degree fits the height-4 bound exactly, and it lies well inside the range of height-4 constants (which go down to `1.0758`), yet no height-4 rule grows at it. So Lehmer's number first appears at height 5 or later, or castle rules never produce it.

## What comes next

- **Proofs on the height-4 data.** Prove that `z^T - z - 1` is the smallest constant at every height; state the unrolling that turns an area count into a width count (each column of height `c` becomes `c` forced steps, giving a 0/1 table with up to `T` states); and see whether a min-height pattern emerges for families such as the Pisot sequences converging to the golden ratio.
- **Height 5.** The census at height 5 reaches degree 15 and would settle whether Lehmer's number appears there.
- **Lehmer's number.** Its min height, or a proof that no castle rule produces it.

## Related Concepts

- [[quadratic-min-height](pages/quadratic-min-height.md)] - the same rules counted by width, where growth constants are the rule table's largest eigenvalue.
- [[castle-by-area](pages/castle-by-area.md)] - castles graded by area.
- [[bounded-height-castles-nacci](pages/bounded-height-castles-nacci.md)] - the h-nacci constants, the ceiling at each height.
- [[plastic-number](pages/plastic-number.md)] - the smallest Pisot number, here the area constant of the height-2 rule "1 may not follow 1".
- [[reachable-field-census](pages/reachable-field-census.md)] - the width-graded census of which number fields castle strips reach.
- [[castle-strip](pages/castle-strip.md)] - castle strips and their 0/1 rule tables.

## Appearances in Sources

- [[oeis-mining-pe502](pages/oeis-mining-pe502.md)] - the castle count sequences whose rule tables this census enumerates.

## Footnotes

[^exec]: Verified by execution (2026-09-25): Python 3 with NumPy and SymPy. For every 0/1 matrix of size 1 to 4, the denominator was built from its principal minors as above and deduplicated; each distinct denominator was factored over the integers, the smallest positive real root found per factor at 30 digits, and the factor carrying it reversed to the minimal polynomial of the growth constant. Pisot and Salem classes were read from the sizes of the other roots at 30 digits. Salem search: every monic palindromic integer polynomial of degree 4 and 6 with `|a_k| <= 2 C(d, k)`, tested for one real root above 1, a root on the unit circle, no other roots outside, and irreducibility. All quoted numbers are the programs' printed output.

[^pisot]: https://en.wikipedia.org/wiki/Pisot%E2%80%93Vijayaraghavan_number (read 2026-09-25) - definition ("a real algebraic integer greater than 1, all of whose Galois conjugates are less than 1 in absolute value"), the near-integer powers and Pisot's converse, Salem's closedness, Siegel's minimal element "the positive root of the equation x3 − x − 1 = 0", "The smallest of them is the golden ratio" for the limit points, Dufresnoy and Pisot "determined all elements of S that are less than φ", "It has been proved that S is contained in the set T' of the limit points of T", and the table "ten smallest Pisot numbers in increasing order".

[^salem]: https://en.wikipedia.org/wiki/Salem_number (read 2026-09-25) - definition ("whose conjugate roots all have absolute value no greater than 1, and at least one of which has absolute value exactly 1"), the reciprocal minimal polynomial, and "The smallest known Salem number is the largest real root of Lehmer's polynomial", about `1.17628`.

[^lehmer]: https://en.wikipedia.org/wiki/Lehmer%27s_conjecture (read 2026-09-25) - the conjecture and Mahler measure, `M(P) = 1.176280818...` for Lehmer's polynomial, "It is widely believed that this example represents the true minimal value", and Lind's observation that the set of entropy values of ergodic compact group automorphisms "is either all of (0, ∞] or a countable set depending on the solution to Lehmer's problem".

[^verger]: https://arxiv.org/pdf/2401.05843v1.pdf (Verger-Gaugry; seen as a search-result excerpt 2026-09-25, full paper not read) - "The Salem numbers of degree ≤8 are all greater than 1.280638...".

[^mossinghoff]: https://web.archive.org/web/20210509232916/http://www.cecm.sfu.ca/~mjm/Lehmer/lists/SalemList.html (Mossinghoff, "Small Salem Numbers"; read 2026-09-25) - "There are 47 known Salem numbers less than 1.3 ... This list is known to be complete for degree at most 44", with entries 1 (degree 10, 1.1762808182), 5 (10, 1.2163916611), 7 (10, 1.2303914344), 19 (10, 1.2612309611), 23 (8, 1.2806381562) and 41 (10, 1.2934859531) the only ones of degree at most 10.
