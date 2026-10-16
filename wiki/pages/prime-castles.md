---
title: Prime castles - the free gluing monoid by area
category: Analyses
summary: "Gluing two castles that begin and end with a height-1 column, by merging the last column of one with the first column of the other, makes a free monoid. Its primes, in Gessel and Li's sense, are the castles with no height-1 column, padded as (1, X, 1); by area they are the compositions into parts at least 2, F_{n-1} of them, golden by area, and the castles of height h among them grow like the largest root of x^h = x^{h-2} + ... + x + 1 (plastic by area at h = 3, supergolden by area at h = 4). A castle with k height-1 columns has k + 1 prime factors (A105422), and its peaks are its nontrivial prime factors. The prime generating function is π(q) = q(1 - q)/(1 - q - q^2) and 1/(1 - π) = (1 - q - q^2)/(1 - 2q). Deutsch and Elizalde's bijection from Dyck paths to bargraphs carries the factorization of Dyck paths into primes onto this one. Block parity is additive over prime factors."
tags: [analysis, castle, area, composition, prime-castle, monoid, factorization, fibonacci, convex-castle, parity, q-series, oeis]
sources: [oeis-mining-pe502, deutsch-elizalde-2017-bargraphs-dyck-paths]
created: 2026-09-22
updated: 2026-10-16
---

# Prime castles

[[castle-by-area](pages/castle-by-area.md)] reads a castle of area `n` as a composition `(c_1, ..., c_w)` of `n`, and every composition is a castle. This page factors castles, cutting them at their height-1 columns, and refines the area counts by the factorization. The block count is additive under the cut after a shift by one, so the parity split factors. The signed version is on [[signed-prime-castles](pages/signed-prime-castles.md)].

## The gluing monoid

Let `M` be the castles that begin and end with a height-1 column. Glue two of them by laying them side by side and merging the last column of the left one with the first column of the right one:

```
(1, 2, 1) ∘ (1, 3, 3, 1)  =  (1, 2, 1, 3, 3, 1)
```

The single column `(1)` is the identity, and gluing is associative. Area, width and block count each lose exactly one in the gluing:

```
area(x ∘ y)   = area(x)   + area(y)   - 1
width(x ∘ y)  = width(x)  + width(y)  - 1
blocks(x ∘ y) = blocks(x) + blocks(y) - 1
```

The block identity holds because the two bottom rows merge into one block, and nothing above the bottom row can touch across a height-1 column. Padding, `C ↦ (1, C, 1)`, adds two cells and no blocks, and together with `() ↦ (1, 1)` for the empty skyline it is a bijection from the castles, and the empty skyline, onto `M` without its identity.[^1]

**`M` is free.** Cut a padded castle at every interior height-1 column. The pieces are `(1, X, 1)` with `X` a castle having no height-1 column, or `X` empty, and gluing them back gives the castle again. No other factorization exists: a seam is a height-1 column, every interior height-1 column must be a seam, and a piece `(1, X, 1)` has no height-1 column inside it.

**Primes.** In a free monoid, the elements into which every element factors uniquely are its primes, and they are also its irreducible elements; Gessel and Li use the word this way for monoids of compositions under concatenation.[^2] The word has nothing to do with prime numbers. So:

- The primes of `M` are `(1, X, 1)` with `X` a castle with no height-1 column, the **prime castles**, and the trivial prime `(1, 1)`, with `X` empty. By area the prime castles are the compositions of `n` into parts `≥ 2`, which number `F_{n-1}`: `0, 1, 1, 2, 3, 5, 8, 13, 21, ...` for `n = 1, 2, 3, ...`, an identity Gessel and Li list from Stanley.[^2] With the height unrestricted, `F_{n-1} ~ φ^n/(φ√5)`, so the prime castles are golden by area ([[metallic-means](pages/metallic-means.md)]), while all castles of area `n` number `2^{n-1}`.[^3] At a fixed height the growth is smaller (section *Prime castles of height h*).
- The **composite castles**, those with at least one height-1 column, number `2^{n-1} - F_{n-1}`: `1, 1, 3, 6, 13, 27, 56, ...`.
- A castle with `k` height-1 columns has `k + 1` prime factors. For example `(2, 1, 3, 3, 1, 1, 2)` has three height-1 columns and four prime factors, and its padded form is `(1,2,1) ∘ (1,3,3,1) ∘ (1,1) ∘ (1,2,1)`.

These three statements and the three identities of the gluing were checked on every castle through area 16.[^1]

## The prime generating function

Grade `M` by reduced area, `area - 1`, so that gluing adds. A prime `(1, X, 1)` has reduced area `1 + area(X)`, and `X` ranges over the compositions with parts `≥ 2`, including the empty one. With `π(q)` the generating function of the primes by reduced area (written `π` because `P` is the signed tower count),

```
π(q)  =  q (1 + q²/(1 - q - q²))  =  q (1 - q)/(1 - q - q²)

1/(1 - π(q))  =  (1 - q - q²)/(1 - 2q)  =  1 + q + q · q/(1 - 2q)
```

On the right, `1` is the identity `(1)`, `q` is the padded empty skyline `(1, 1)`, and `q · q/(1 - 2q)` is the padded castles, the `2^{n-1}` castles of area `n` at reduced area `n + 1`. Without the identity this is the sequence construction `M − 1 = π/(1 − π)` of [[analytic-combinatorics-ch1-ogfs](pages/analytic-combinatorics-ch1-ogfs.md)], and it is the identity of Gessel and Li for a free monoid with an additive weight: the generating function of the monoid is `1/(1 − Σ_p x^{weight(p)})`, summed over its primes.[^2]

**The primes are castles raised one row.** A nonempty `X` with no height-1 column is a castle `Y` with a full row slid under it, and `area(X) = area(Y) + width(Y)`. So with `B(q, z)` the castle generating function by area and width, the empty skyline included ([[castle-notation](pages/castle-notation.md)]), `π(q) = q · B(q, q)`. Tracking the width as well gives a functional equation in `z → qz`, which [[castle-row-raising-equation](pages/castle-row-raising-equation.md)] derives, signed and weighted by peaks.

## Prime castles of height h

A prime castle of height `h` is a composition with every part in `{2, …, h}` and at least one part equal to `h`. Its count by area is the number of compositions into parts `{2, …, h}` minus the number into parts `{2, …, h − 1}`, and it grows like the largest root of

```
x^h = x^(h-2) + x^(h-3) + ... + x + 1,      equivalently   x^-2 + x^-3 + ... + x^-h = 1.
```

As `h → ∞` the left side of the second form tends to `1/(x(x − 1))`, so the equation tends to `x² = x + 1`: the constants increase towards `φ` and stay below it at every fixed height. At height 2 the only prime castles are the 2-high rectangles `(2, …, 2)`, one for each even area.[^4]

| `h` | prime castles of height `h` by area, `n = 2..15` | growth | polynomial |
|---|---|---|---|
| 3 | `0, 1, 0, 2, 1, 3, 3, 5, 6, 9, 11, 16, 20, 28` | `1.3247`, the plastic number `ψ` | `x³ − x − 1` |
| 4 | `0, 0, 1, 0, 2, 2, 4, 6, 10, 15, 24, 36, 56, 84` | `1.4656`, the supergolden ratio | `(x + 1)(x³ − x² − 1)` |
| 5 | `0, 0, 0, 1, 0, 2, 2, 5, 7, 13, 21, 35, 57, 93` | `1.5342` | `x⁵ − x³ − x² − x − 1` |
| 6 | `0, 0, 0, 0, 1, 0, 2, 2, 5, 8, 14, 24, 41, 69` | `1.5701` | `(x + 1)(x⁵ − x⁴ − x² − 1)` |
| 7 | `0, 0, 0, 0, 0, 1, 0, 2, 2, 5, 8, 15, 25, 44` | `1.5900` | `x⁷ − x⁵ − x⁴ − x³ − x² − x − 1` |
| 8 | `0, 0, 0, 0, 0, 0, 1, 0, 2, 2, 5, 8, 15, 26` | `1.6013` | `(x + 1)(x⁷ − x⁶ − x⁴ − x² − 1)` |
| unrestricted | `F_{n-1}` | `φ = 1.6180` | `x² − x − 1` |

So the prime castles of height 3 are plastic by area, and those of height 4 supergolden by area ([[castle-classification-growth](pages/castle-classification-growth.md)], [[plastic-number](pages/plastic-number.md)]).

## The same factorization on Dyck paths

Dyck paths form a free monoid under concatenation. Its primes are the paths `uPd` that touch the axis only at their two ends, and the number of prime factors of a path is its number of returns to the axis. Deutsch and Elizalde's bijection from Dyck paths to bargraphs, which are castles ([[deutsch-elizalde-2017-bargraphs-dyck-paths](pages/deutsch-elizalde-2017-bargraphs-dyck-paths.md)]), carries this factorization to the one on this page. They write the bijection `φ`; this page writes `φ_DE`, since `φ` is the golden ratio here. With `B ◦ B′` the concatenation of two bargraphs read as height sequences and `UBD` the bargraph `B` raised one row:[^5]

- `φ_DE(uPd)` is `φ_DE(P)` raised one row, so a prime Dyck path `uPd` with `P` nonempty goes to a castle with no height-1 column (Prop. 3.5(i)).
- `φ_DE(PP′)` is `φ_DE(P) ◦ (1) ◦ φ_DE(P′)` when both paths have height at least 2, and `φ_DE(P) ◦ φ_DE(P′)` otherwise (Prop. 3.5(ii)).
- A path of height at least 2 has one more return than its castle has height-1 columns (Thm. 3.2(g)).

So the prime Dyck paths of height at least 2 go exactly to the castles with no height-1 column, and a Dyck path of height at least 2 and its castle have the same number of prime factors, the castle's height-1 columns plus one. The only prime of height 1, `ud`, goes to the single column `(1)`. The map does not preserve size: the semilength of a path is the semi-perimeter of its castle minus the castle's number of peaks in Deutsch and Elizalde's sense, its plateaus higher than both neighbors (Thm. 3.2(a)), so the area counts on this page have no Dyck-path counterpart under `φ_DE`.[^6]

## Counting factors

The number of prime factors of a castle is one more than its number of height-1 columns, so the castles of area `n` counted by prime factors form the triangle A105422, "the number of compositions of n having exactly k parts equal to 1", shifted by one in `k`. The total number of height-1 columns over all castles of area `n` is `A045623(n − 1)`, the number of 1s in all compositions of `n`, equal to `(n + 2) 2^{n−3}` for `n ≥ 2`: `1, 2, 5, 12, 28, 64, 144, ...` for `n = 1, 2, 3, ...`. A castle of area `n ≥ 2`, chosen uniformly, therefore has `1 + (n + 2)/4 = (n + 6)/4` prime factors on average.[^7]

**Peaks count the nontrivial factors.** On [[castle-foata-transform](pages/castle-foata-transform.md)] a peak of a castle is a maximal run of columns with `c_i ≥ 2`. Every such run lies inside one nontrivial prime, and every nontrivial prime `(1, X, 1)` holds exactly one, since `X` has all heights `≥ 2`. So the number of peaks is the number of nontrivial prime factors, and a castle with `p` peaks and `k` height-1 columns has `k + 1 − p` trivial factors `(1, 1)`, one for each pair of neighboring height-1 columns in the padded castle. Checked through area 16.[^1]

## Convex castles

The height-1 columns of a [[convex-castle](pages/convex-castle.md)] form a run at each end, so `(1, C, 1) = (1,1)^a ∘ (1, X, 1) ∘ (1,1)^b`. **A convex castle has at most one nontrivial prime factor, and that factor is itself convex.** Convex castles are not closed under gluing, since `(1, X, 1) ∘ (1, Y, 1)` has a height-1 column between `X` and `Y`. They are the words with at most one nontrivial letter, that letter convex. The convex prime castles number `1, 1, 2, 3, 5, 8, 12, 19, ...` for `n = 2, 3, ...`, the second difference of A001523; [[prime-convex-castles](pages/prime-convex-castles.md)] proves this and gives their asymptotics, width triangle and parity split.

## Block parity of the primes

Blocks are additive after the shift by one, so the block parity of a castle is decided by its prime factors. The trivial prime `(1, 1)` has one block and contributes nothing to `blocks − 1`. The full signed statement is on [[signed-prime-castles](pages/signed-prime-castles.md)], and the convex case, where a castle has the parity of its one nontrivial prime, is on [[prime-convex-castles](pages/prime-convex-castles.md)]. The prime castles split by the parity of their block count, for `n = 1..16`:[^8]

| `n` | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| prime, even | 0 | 1 | 0 | 2 | 0 | 4 | 2 | 9 | 6 | 24 | 18 | 58 | 54 | 143 | 150 | 364 |
| prime, odd | 0 | 0 | 1 | 0 | 3 | 1 | 6 | 4 | 15 | 10 | 37 | 31 | 90 | 90 | 227 | 246 |

The two rows add up to `F_{n−1}`, and their difference is `0, 1, −1, 2, −3, 3, −4, 5, −9, 14, −19, 27, −36, 53, −77, 118`. Their OEIS status is on [[castle-sequence-catalogue](pages/castle-sequence-catalogue.md)].

## Computation

The factorization and the checks of this page, on every castle through area 16:

```python
def comps(n):                                   # compositions of n = castles of area n
    if n == 0: yield (); return
    for f in range(1, n + 1):
        for r in comps(n - f): yield (f,) + r
def blocks(c):                                  # maximal horizontal runs, summed over levels
    return sum(sum(1 for i in range(len(c)) if c[i] >= l and (i == 0 or c[i-1] < l))
               for l in range(1, max(c, default=0) + 1))
def primes(c):                                  # the X of each factor (1, X, 1) of (1, C, 1)
    segs, cur = [], []
    for x in c:
        if x == 1: segs.append(tuple(cur)); cur = []
        else: cur.append(x)
    return segs + [tuple(cur)]
for n in range(1, 17):
    for c in comps(n):
        fs = primes(c)
        assert blocks((1,) + c + (1,)) == blocks(c)
        assert sum(blocks((1,) + x + (1,)) - 1 for x in fs) == blocks(c) - 1
        assert len(fs) == c.count(1) + 1
    print(n, sum(1 for c in comps(n) if 1 not in c))     # F_{n-1}
```

## Relation to other pages

- [[castle-by-area](pages/castle-by-area.md)]: the castle counts by area, and their parity splits, refined here by prime factors.
- [[castle-row-raising-equation](pages/castle-row-raising-equation.md)]: the functional equation of the raised primes, signed and by peaks.
- [[deutsch-elizalde-2017-bargraphs-dyck-paths](pages/deutsch-elizalde-2017-bargraphs-dyck-paths.md)]: the bijection that carries the prime factorization of Dyck paths to this one.
- [[deutsch-elizalde-2016-bargraphs-cornerless-motzkin](pages/deutsch-elizalde-2016-bargraphs-cornerless-motzkin.md)]: raising a castle one row adds one block, so the prime castles of semi-perimeter `s` are the castles of semi-perimeter `s − 1` raised, `A082582(s − 1)` of them for `s ≥ 3` (`1, 2, 5, 13, 35, …` from `s = 3`), with the sign `(−1)^{blocks}` reversed.
- [[signed-prime-castles](pages/signed-prime-castles.md)]: the sign as a character of this monoid, the signed identity `π_χ/(1 − π_χ)` for the signed prime series `π_χ`, and the counts of castles per multiset of primes.
- [[prime-convex-castles](pages/prime-convex-castles.md)]: the one nontrivial prime of a convex castle, counted.
- [[convex-castle](pages/convex-castle.md)]: the convex castles.
- [[castle-foata-transform](pages/castle-foata-transform.md)]: peaks, which count the nontrivial prime factors.
- [[metallic-means](pages/metallic-means.md)], [[algebraic-transcendental-wall](pages/algebraic-transcendental-wall.md)]: the golden ratio as the growth constant of the prime castles by area.
- [[q-thread-seminar](pages/q-thread-seminar.md)]: a seminar on castles by area, whose Stop 3 is this factorization.

## Footnotes

[^1]: Checked by execution (Python 3, 2026-09-22; rerun 2026-10-16 with Python 3.11): every composition of `n ≤ 16` has padded block count equal to its own, satisfies `sum (blocks(prime) − 1) = blocks − 1` and `#factors = #height-1 columns + 1`, and has peak count equal to its number of nontrivial factors; the prime castles of area `n` number `F_{n−1}`. The even and odd totals of the same enumeration reproduce raw/oeis-pe502/vein9-area.md §"Parity splits" L46-47 [synthesis] - the `even(n)` and `odd(n)` rows for `n = 1..12`.
[^2]: https://cs.uwaterloo.ca/journals/JIS/VOL16/Gessel/gessel6.pdf (Gessel and Li, "Compositions and Fibonacci Identities", J. Integer Seq. 16 (2013), Article 13.4.5; read 2026-10-16) §"Free monoids" p.3 - "if M is a free monoid, then there exists a subset P of M such that every element of M has a unique factorization as a product of elements of P. We call P the set of primes of M."; "If L is a free monoid, then the factorization is always unique and the irreducible elements are the primes of L"; and the identity `Σ_{m∈M} x^{ω(m)} = (1 − Σ_{p∈P} x^{ω(p)})^{−1}` (their (3)) for a weight function `ω`. The Introduction, p.1, lists from Stanley's Enumerative Combinatorics, Vol. 1, "(ii) F_{n−1} is the number of compositions of n into parts greater than 1".
[^3]: Verified by execution (Python 3, 2026-10-04): `F_59/φ^60 = 0.27639320` against `1/(φ√5) = 0.27639320`; the compositions of `n` number `2^{n−1}`, and the composite castles `2^{n−1} − F_{n−1}`.
[^4]: Verified by execution (Python 3, SymPy, 2026-10-02; the table rerun by enumeration 2026-10-16): for `h = 3..8` the count from the two composition recurrences matches a count of the compositions of `n ≤ 16` with largest part `h` and no part 1; the polynomials were factored with SymPy and their largest real roots computed numerically; the successive ratios of the counts at `n = 200` agree with those roots (to five decimals for `h = 3, 4`, and approaching from above for larger `h`).
[^5]: [[deutsch-elizalde-2017-bargraphs-dyck-paths](pages/deutsch-elizalde-2017-bargraphs-dyck-paths.md)] §3 L155, L167, L236-245 - "(a) sl(P ) = sp(B) − pk(B)", "(g) ret(P ) = #H1 (B) + 1 (unless P and B have height 1, in which case ret(P ) = #H1 (B))", "the path U BD is the bargraph whose height sequence is obtained by adding one to each entry of the height sequence of B", "the expression B ◦ B ′ denotes the concatenation of B and B ′ viewed as height sequences", and Prop. 3.5 "(i) φ(uP d) = U BD", "(ii) φ(P P ′ ) = B ◦ 1 ◦ B′ if height(P ) ≥ 2 and height(P ′ ) ≥ 2, B ◦ B′ otherwise".
[^6]: Own reasoning from Prop. 3.5 and Thm. 3.2(g), verified by execution (Python 3, 2026-10-02): `φ_DE` implemented from its definition and applied to every Dyck path of semilength `≤ 11` is injective; every one-return path of semilength `≥ 2` goes to a castle with no height-1 column, and every castle in the image with no height-1 column comes from a one-return path; returns `=` height-1 columns `+ 1` for every path of height `≥ 2`; and semilength `=` semi-perimeter `−` peaks in the sense of Thm. 3.2(a) ([[deutsch-elizalde-2017-bargraphs-dyck-paths](pages/deutsch-elizalde-2017-bargraphs-dyck-paths.md)] §3 L155).
[^7]: https://oeis.org/A105422 and https://oeis.org/A045623 (read 2026-09-22) - A105422 "Triangle read by rows: T(n,k) is the number of compositions of n having exactly k parts equal to 1"; A045623 "Number of 1's in all compositions of n+1", offset 0. The totals `1, 2, 5, 12, 28, 64, 144, 320, 704` for `n = 1..9` recomputed by execution, 2026-10-16.
[^8]: Computed by execution (Python 3.11, 2026-10-16) over all castles through area 16; the rows agree with the 2026-09-22 computation.
