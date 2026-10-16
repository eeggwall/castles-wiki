---
title: Hoodoo and monadnock castles
category: Concepts
summary: "Two unimodal castle types of height h whose sides change step size strictly: on a hoodoo castle the rising steps strictly increase and the drops strictly decrease, on a monadnock castle the rising steps strictly decrease and the drops strictly increase. Each side is a partition into distinct parts of an integer in 1..h-1, so the Hindenburg algorithm (TAOCP 7.2.1.4 Algorithm H) with the staircase shift generates both families with no filtering, and reversing the steps of each side maps one family onto the other. A_hoodoo(w, h) = A_monadnock(w, h) counts ordered pairs of distinct-part partitions with at most w-1 parts in total; by width it is eventually (sum of A000009 over 1..h-1)^2, by height at fixed width a polynomial of degree w-1, and by height at large width about sqrt(3) e^{2 pi sqrt(N/3)} / (4 pi^2 sqrt N), N = h-1, which is (6/pi^2) sqrt(N) p(2N) to leading order."
tags: [concept, castle, classification, unimodal, distinct-parts, partitions, hindenburg-algorithm, generation, growth-constant, hoodoo-castle, monadnock-castle, implementation, verification]
sources: [aocp-generating-partitions]
created: 2026-10-02
updated: 2026-10-16
---

# Hoodoo and monadnock castles

## Definition

Both types are castles of height `h ≥ 2` made of three parts, read left to right: a **rising side** of at least one column below `h`, a **summit** of one or more columns at height `h`, and a **falling side** of at least one column below `h`. A side's steps are the height changes `c_{i+1} − c_i` from its first column up to the summit, or from the summit down to its last column; the steps onto and off the summit belong to the sides. Every step on a side is nonzero, and the only zero steps are inside the summit.

- **Hoodoo castle:** the rising steps strictly increase and the falling drops strictly decrease. Example, `h = 35`: `(2, 3, 6, 16, 35, 35, 25, 18, 14, 12)`, rising steps `1, 3, 10, 19`, drops `10, 7, 4, 2`.
- **Monadnock castle:** the rising steps strictly decrease and the falling drops strictly increase. Example, `h = 35`: `(2, 21, 31, 34, 35, 35, 33, 29, 22, 12)`, rising steps `19, 10, 3, 1`, drops `2, 4, 7, 10`.

Both are unimodal, so each has exactly `h` blocks ([[convex-castle](pages/convex-castle.md)]): the even-block ones are all of them when `h` is even and none when `h` is odd. Hoodoo and monadnock are names the wiki gives these two types; the catalogue entry, with the relation to the concave-skyline type, is in the convexity section of [[castle-classification-shape](pages/castle-classification-shape.md)].

## Notation used on this page

| symbol | meaning |
|---|---|
| `p(n)` | partitions of `n` |
| `pd(n)` | partitions of `n` into distinct parts (OEIS A000009; Knuth's `q(n)`, renamed because `q` marks area on the wiki) |
| `part(n, m)` | partitions of `n` into exactly `m` parts (Knuth's vertical-bar symbol) |
| `side(h, m)` | sides with `m` steps of a castle of height `h` |
| `A_hoodoo(w, h)`, `A_monadnock(w, h)` | hoodoo and monadnock castles of width `w` and height `h` |
| `N` | `h − 1`, the largest possible rise of one side |

## Sides are partitions into distinct parts

The steps of one side are distinct positive integers, and their sum, the side's rise, is `h` minus the side's outer column, a number from `1` to `h − 1`. Read as a set, a side is a partition into distinct parts of an integer in `1, …, N`. Each such partition gives exactly one hoodoo side, with the steps in increasing order, and exactly one monadnock side, in decreasing order. The same holds for falling sides, with the orders swapped.

So a hoodoo or monadnock castle of width `w` is an ordered pair of distinct-part partitions, each of sum at most `N`, with `a` and `b` parts, `a + b ≤ w − 1`, plus a summit of `w − a − b ≥ 1` columns. Reversing the steps of both sides maps the hoodoo castles onto the monadnock castles with the same `w`, `h`, end columns, side lengths and summit length. When some side has two or more steps, the hoodoo of the pair has the smaller area, because its sides lie below the chord between their ends and the monadnock's lie above it; when both sides are single steps the two castles coincide.

## Generating them: the Hindenburg algorithm

Knuth's §7.2.1.4 Algorithm H, here the **Hindenburg algorithm** after the eighteenth-century dissertation of C. F. Hindenburg that Knuth takes it from, visits the partitions of `n` into exactly `m` parts in colex order.[^1] Partitions into `m` distinct parts are partitions into `m` parts with the staircase `(m − 1, m − 2, …, 0)` added: the number of partitions of `n` into `m` distinct parts is `part(n − m(m − 1)/2, m)`.[^2] So one call of the Hindenburg algorithm per rise lists every side with `m` steps. Adding a fixed vector keeps colex order, and Theorem H bounds the algorithm's accumulated work by `3·part(n, m) + m`, so the sides come out in colex order at constant amortized cost.[^3]

The algorithm outputs parts largest first. Read that way, a side is a monadnock rising side or a hoodoo falling side; reversed, it is a hoodoo rising side or a monadnock falling side. The generator below builds each hoodoo castle and its monadnock partner from the same pair of partitions:

```python
def partitions_into(n, m):
    """Hindenburg algorithm (TAOCP 7.2.1.4 Algorithm H): partitions
    a_1 >= ... >= a_m >= 1 of n, in colex order."""
    if m == 1:
        if n >= 1: yield (n,)
        return
    if n < m: return
    a = [n - m + 1] + [1] * (m - 1) + [-1]          # H1, sentinel a_{m+1} = -1
    while True:
        yield tuple(a[:m])                           # H2
        if a[1] < a[0] - 1:                          # H3
            a[0] -= 1; a[1] += 1; continue
        j, s = 2, a[0] + a[1] - 1                    # H4 (j is 0-based here)
        while a[j] >= a[0] - 1:
            s += a[j]; j += 1
        if j + 1 > m: return                         # H5
        x = a[j] + 1; a[j] = x; j -= 1
        while j > 0:                                 # H6
            a[j] = x; s -= x; j -= 1
        a[0] = s

def sides(h, m):
    """All m-step sides at height h: m distinct steps, rise <= h - 1, largest first."""
    for rise in range(m * (m + 1) // 2, h):
        for p in partitions_into(rise - m * (m - 1) // 2, m):
            yield tuple(p[i] + (m - 1 - i) for i in range(m))   # add the staircase

def hoodoo_monadnock(w, h):
    """Yield (hoodoo, monadnock) pairs of width w and height h, matched by step reversal."""
    for a in range(1, w - 1):
        for b in range(1, w - a):
            top = w - a - b                           # summit columns, >= 1
            for up in sides(h, a):
                for dn in sides(h, b):
                    def build(rise, fall):
                        c = [h - sum(rise)]
                        for d in rise: c.append(c[-1] + d)
                        c += [h] * (top - 1)
                        for d in fall: c.append(c[-1] - d)
                        return tuple(c)
                    yield build(up[::-1], dn), build(up, dn[::-1])
```

`partitions_into(11, 4)` returns Knuth's list (7), `8111, 7211, 6311, 5411, 6221, 5321, 4421, 4331, 5222, 4322, 3332`.[^1] For every `h ≤ 7` and `3 ≤ w ≤ 8` (`w ≤ 7` at `h = 7`), the first and second components of `hoodoo_monadnock(w, h)` are exactly the hoodoo and monadnock castles found by filtering all `h^w` skylines with `is_hoodoo` and `is_monadnock` ([[castle-snippets](pages/castle-snippets.md)]).[^exec]

## Counting them

The number of `m`-step sides at height `h` is

```
side(h, m) = Σ_{n=1}^{N} part(n − m(m−1)/2, m),
```

and Knuth's recurrence `part(n, m) = part(n − 1, m − 1) + part(n − m, m)` and generating function `z^m / ((1 − z)(1 − z²)…(1 − z^m))` compute it.[^4] A side with `m` steps needs a rise of at least `1 + 2 + … + m`, so `m` is at most the largest integer whose triangular number is at most `N`. The first values:[^exec]

```
 h | side(h,1) side(h,2) side(h,3) side(h,4) side(h,5) | all sides | (all sides)^2
 4 |     3         1         .         .         .     |      4    |      16
 7 |     6         6         1         .         .     |     13    |     169
10 |     9        16         7         .         .     |     32    |    1024
11 |    10        20        11         1         .     |     42    |    1764
13 |    12        30        23         4         .     |     69    |    4761
16 |    15        49        53        18         1     |    136    |   18496
```

`side(h, 1) = h − 1`, and `side(h, 2) = ⌊(h − 2)²/4⌋` (checked for `h ≤ 16`). The castle count at width `w` is a sum over the two side lengths:

```
A_hoodoo(w, h)  =  A_monadnock(w, h)  =  Σ_{a, b ≥ 1, a + b ≤ w − 1} side(h, a) · side(h, b).
```

So `A_hoodoo(3, h) = (h − 1)²` and `A_hoodoo(4, h) = (h − 1)² + 2(h − 1)⌊(h − 2)²/4⌋`. In generating-function form, with `y` marking width, `A_hoodoo(w, h)` is the coefficient of `y^w` in `y/(1 − y) · B_h(y)²`, where `B_h(y) = Σ_{m≥1} side(h, m) y^m` collects the terms `y^m z^n` with `1 ≤ n ≤ N` of Euler's product `Π_{i≥1} (1 + y z^i)`; Knuth's (41) with the staircase shift is the coefficient of `y^m` in that product.[^4] The table of counts by width for `h ≤ 7` is on [[castle-classification-shape](pages/castle-classification-shape.md)].

## Growth on three axes

**By width, at fixed `h`: eventually constant.** Only the summit absorbs extra width. Once `w` is larger than twice the longest possible side, every pair of sides fits, and `A_hoodoo(w, h)` is `(Σ_{n=1}^{N} pd(n))²` for every larger `w`: `1, 4, 16, 36, 81, 169, 324, 576, 1024, 1764, …` for `h = 2, 3, 4, …`. So neither family grows with the width ([[castle-classification-growth](pages/castle-classification-growth.md)]).

**By height, at fixed `w`: polynomial of degree `w − 1`.** Knuth's exercise 34 gives `part(n, m) ≈ n^{m−1}/(m!(m − 1)!)`.[^2] Summing over rises up to `N` gives `side(h, m) ≈ N^m/(m!)²`. The terms with `a + b = w − 1` dominate, so

```
A_hoodoo(w, h)  ≈  N^{w−1} · Σ_{a+b=w−1, a,b≥1} 1/((a!)² (b!)²).
```

Convex castles number `C(2h + w − 3, w − 1) ≈ (2h)^{w−1}/(w − 1)!` ([[convex-castle](pages/convex-castle.md)]), so the hoodoo castles make up a fixed fraction of the convex castles of each width as `h` grows:

| `w` | 3 | 4 | 5 | 6 |
|---|---|---|---|---|
| limit `(w−1)!/2^{w−1} · Σ 1/((a!)²(b!)²)` | 0.5 | 0.375 | 0.1771 | 0.0651 |
| measured at `h = 400` | 0.4981 | 0.3722 | 0.1743 | 0.0632 |

**By height, at large `w`: the distinct-part partition rate.** The eventual count is the square of `Σ_{n=1}^{N} pd(n)`. With `pd(n) ≈ e^{π√(n/3)}/(4·3^{1/4} n^{3/4})`,[^5] the partial sum is about `3^{1/4} e^{π√(N/3)}/(2π N^{1/4})`, and

```
A_hoodoo(w, h)  ≈  √3 · e^{2π√(N/3)} / (4π² √N),        N = h − 1,  w large.
```

The exact count divided by this estimate is `1.33, 1.16, 1.08, 1.04` at `N = 10, 50, 200, 800`, approaching 1 at the expected `O(N^{−1/2})` rate.[^exec] The exponent `2π√(N/3)` equals `π√(2·2N/3)`, the exponent of `p(2N)` in Knuth's leading term `p(n) ≈ e^{π√(2n/3)}/(4n√3)`.[^6] Dividing the two estimates, the eventual count is `(6/π²)·√N·p(2N)` to leading order; the measured ratio of the eventual count to `√N·p(2N)` is `0.89, 0.74, 0.67, 0.64` at `N = 10, 50, 200, 800`, against `6/π² = 0.6079`. The agreement is between leading terms.

## Appearances in Sources

- [[aocp-generating-partitions](pages/aocp-generating-partitions.md)] - the Hindenburg algorithm, the staircase shift (exercise 34), the `part(n, m)` recurrence and generating function, and the `p(n)` asymptotics.

## Related Concepts

- [[castle-classification-shape](pages/castle-classification-shape.md)] - the catalogue entries, the count table by width for `h ≤ 7`, and the relation to the concave-skyline type.
- [[convex-castle](pages/convex-castle.md)] - the unimodal family both types sit inside; its binomial count is the denominator of the fixed-width fractions.
- [[castle-classification-growth](pages/castle-classification-growth.md)] - growth types by width, of which neither family has one: both counts are eventually constant in `w`.
- [[castle-snippets](pages/castle-snippets.md)] - the `is_hoodoo` and `is_monadnock` predicates used to check the generator.
- [[multiset-partitions](pages/multiset-partitions.md)] - partitions into distinct parts as Bender's `c*` count on a one-element multiset.
- [[castle-gray-code](pages/castle-gray-code.md)] - the loopless Gray algorithm (Knuth's §7.2.1.1 Algorithm H), not to be confused with the Hindenburg algorithm used here.

## Footnotes

[^1]: [[aocp-generating-partitions](pages/aocp-generating-partitions.md)] p.392 - "Algorithm H (Partitions of n into m parts)", from "C. F. Hindenburg's 18th-century dissertation", which "visits the partitions in colex order"; list (7): "8111, 7211, 6311, 5411, 6221, 5321, 4421, 4331, 5222, 4322, 3332".
[^2]: [[aocp-generating-partitions](pages/aocp-generating-partitions.md)] p.411 exercise 34 [synthesis] - the number of partitions of `n − m(m−1)/2` into `m` parts "is the number of partitions of n into m distinct parts", and the number of partitions of `n` into `m` parts is `n^{m−1}/(m!(m−1)!) (1 + O(m³/n))` "when m ≤ n^{1/3}".
[^3]: [[aocp-generating-partitions](pages/aocp-generating-partitions.md)] p.393 and p.404 Theorem H [synthesis] - "the total running time of Algorithm H is at most a small constant times the number of partitions visited, plus O(m)"; Theorem H bounds the cost measure `c_m(n)` by three times the number of partitions of `n` into `m` parts, plus `m`.
[^4]: [[aocp-generating-partitions](pages/aocp-generating-partitions.md)] p.399 eqs. (38)-(41) [synthesis] - the count of partitions of `n` into exactly `m` parts, its recurrence (39) by whether the smallest part is 1, and its generating function (41) `z^m/((1−z)(1−z²)…(1−z^m))`.
[^5]: https://oeis.org/A000009 (formula section) - "a(n) ~ exp(Pi*sqrt(n/3))/(4*3^(1/4)*n^(3/4)) * (1 + (Pi/(48*sqrt(3)) - 3*sqrt(3)/(8*Pi))/sqrt(n) + (Pi^2/13824 - 5/128 - 45/(128*Pi^2))/n)" (Vaclav Kotesovec, 2016).
[^6]: [[aocp-generating-partitions](pages/aocp-generating-partitions.md)] p.399 eq. (36) [synthesis] - `p(n) = e^{π√(2n/3)}/(4n√3) (1 + O(n^{−1/2}))`, the leading term of the Hardy-Ramanujan-Rademacher formula (32).
[^exec]: Verified by execution (Python 3.11, 2026-10-16): the generator of the code block against exhaustive filtering of `{1..h}^w`, as sets, for `h ≤ 7` and `3 ≤ w ≤ 8` (`w ≤ 7` at `h = 7`); the hoodoo castle of each reversal pair has the smaller area exactly when some side has at least two steps (`h ≤ 6`, `w ≤ 7`); `partitions_into(11, 4)` against Knuth's list (7); the table of `side(h, m)` by enumeration of distinct-part sets; `side(h, 2) = ⌊(h − 2)²/4⌋` for `h ≤ 16`; `A_hoodoo(3, h)` and `A_hoodoo(4, h)` for `h ≤ 14`; the eventual counts `1, 4, 16, 36, …, 1764`; the fixed-width fractions at `h = 400` and the large-width ratios at `N = 10, 50, 200, 800` with exact partition counts.
