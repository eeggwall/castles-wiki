---
title: Prime castles - the free gluing monoid by area
category: Analyses
summary: "Gluing castles at a shared height-1 column makes a free monoid, and its primes, in Gessel and Li's sense (the unique generating set of a free monoid), are the castles with no height-1 column, F_{n-1} of them by area. The factorization is the prime factorization of Dyck paths carried over by the Deutsch-Elizalde bijection, which sends prime Dyck paths of height at least 2 to exactly these castles. The composite castles, those with a height-1 column, are 2^{n-1} - F_{n-1}. The castle GF is 1/(1 - P) with P = q(1-q)/(1-q-q^2), and P is itself the castle GF raised one row. A castle has 1 + (number of height-1 columns) prime factors (A105422, A045623), and its peak count is the number of nontrivial factors. A convex castle has at most one nontrivial prime (counted on prime-convex-castles). Block parity is decided by the primes, and the prime parity splits are novel-candidates."
tags: [analysis, castle, area, composition, prime-castle, monoid, factorization, fibonacci, convex-castle, parity, q-series, oeis, novel-candidate]
sources: [oeis-mining-pe502, deutsch-elizalde-2017-bargraphs-dyck-paths]
created: 2026-09-22
updated: 2026-10-02
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

The block identity holds because the two bottom rows merge into one block, and nothing above the bottom row can touch across a height-1 column. Every castle `C` lives in `M` after padding, `C ↦ (1, C, 1)`, which adds two cells and no blocks. The padding is a bijection from castles, together with the empty castle `() ↦ (1, 1)`, onto `M` without its identity.[^1]

**`M` is free.** Cut a padded castle at every interior height-1 column. The pieces are `(1, X, 1)` with `X` a castle having no height-1 column (possibly empty), and gluing them back gives the castle again. No other factorization exists, since every interior height-1 column must be a seam: a seam is a height-1 column, and a prime has none inside it.

**"Prime" is the free-monoid term.** In a free monoid the elements that every element factors into, uniquely, are called its primes; they are also exactly its irreducible elements. Gessel and Li use the word this way for monoids of compositions under concatenation, and "compositions of `n` into parts greater than 1, `F_{n-1}` of them" is one of the identities they derive from it.[^gl] It has nothing to do with prime numbers. So:

- **The prime castles are the castles with no height-1 column**, plus the empty castle, whose padded form `(1, 1)` is the one trivial prime. By area they are the compositions of `n` into parts `≥ 2`, which number `F_{n-1}`: `0, 1, 1, 2, 3, 5, 8, 13, 21, ...` for `n = 1, 2, 3, ...`. Their growth constant is the golden ratio, the golden area growth castle on [[metallic-means](pages/metallic-means.md)].
- **The composite castles are the castles with at least one height-1 column**, `2^{n-1} - F_{n-1}`: `1, 1, 3, 6, 13, 27, 56, ...`.
- A castle with `k` height-1 columns has `k + 1` prime factors. For example `(2, 1, 3, 3, 1, 1, 2)` has three height-1 columns and four prime factors, and its padded form is `(1,2,1) ∘ (1,3,3,1) ∘ (1,1) ∘ (1,2,1)`.

All three statements, and the three identities above, were checked on every castle through area 16.[^1]

## The `P/(1-P)` identity

Grade `M` by reduced area, `area - 1`, so that gluing adds. A prime `(1, X, 1)` has reduced area `1 + area(X)`, and `X` ranges over the compositions with parts `≥ 2`, including the empty one:

```
P(q) = q (1 + q^2/(1 - q - q^2)) = q (1 - q)/(1 - q - q^2)

1/(1 - P) = (1 - q - q^2)/(1 - 2q) = 1 + q + q · q/(1 - 2q)
```

On the right, `1` is the identity `(1)`, `q` is the empty castle `(1, 1)`, and `q · q/(1 - 2q)` is the padded castles, the `2^{n-1}` of [[castle-by-area](pages/castle-by-area.md)] shifted by one. Without the identity this is the sequence construction `M - 1 = P/(1 - P)` of [[analytic-combinatorics-ch1-ogfs](pages/analytic-combinatorics-ch1-ogfs.md)], and it is the identity Gessel and Li write down for any free monoid with an additive weight: the generating function of the monoid is `1/(1 - Σ_p x^{weight(p)})`, summed over its primes.[^gl]

**The primes are castles raised one row.** A nonempty `X` with no height-1 column is a castle with a full row slid under it, so `P = q (1 + A(q, q))`, with `A(q, z)` the castle GF by area and width. With width tracked, the factorization becomes a `z → qz` functional equation. That equation is trivial unsigned, but signed or weighted by peaks it has content. It is on [[castle-row-raising-equation](pages/castle-row-raising-equation.md)].

## The same factorization on Dyck paths

Dyck paths form a free monoid under concatenation. Its primes are the paths `uPd` that touch the axis only at their two ends, and a path's returns to the axis are its prime factors. Deutsch and Elizalde's bijection `φ` from Dyck paths to bargraphs, which are castles ([[deutsch-elizalde-2017-bargraphs-dyck-paths](pages/deutsch-elizalde-2017-bargraphs-dyck-paths.md)]), carries this factorization to the one on this page:

- `φ(uPd)` is `φ(P)` raised one row, so a prime Dyck path `uPd` with `P` nonempty goes to a castle with no height-1 column (Prop. 3.5(i)).
- `φ(PP')` is `φ(P)`, a height-1 column, `φ(P')` when both have height at least 2, and `φ(P)φ(P')` otherwise (Prop. 3.5(ii)).
- A path of height at least 2 has one more return than its castle has height-1 columns (Thm. 3.2(g)).[^de]

So the prime Dyck paths of height at least 2 are exactly the castles with no height-1 column, and a Dyck path and its castle have the same number of prime factors, height-1 columns plus one. The only height-1 prime, `ud`, goes to the single column `(1)`. The map does not preserve size: it sends the semilength of a path to the semiperimeter of its castle minus the castle's peaks, so the area counts on this page have no Dyck-path counterpart under `φ`.[^de-exec]

## Counting factors

The number of prime factors of a castle is one more than its number of height-1 columns, so the factor-count triangle is OEIS A105422, "the number of compositions of n having exactly k parts equal to 1". The total number of height-1 columns over all castles of area `n` is A045623, `(n + 2) 2^{n-3}` for `n ≥ 2`: `2, 5, 12, 28, 64, 144, ...`. A random castle of area `n ≥ 2` therefore has `(n + 6)/4` prime factors on average.[^2]

**Peaks count the nontrivial factors.** On [[castle-foata-transform](pages/castle-foata-transform.md)] a peak is a maximal run of columns above the base row, meaning `c_i ≥ 2`. Every such run lies inside one nontrivial prime, and every nontrivial prime `(1, X, 1)` holds exactly one, since `X` has all heights `≥ 2`. So `#peaks = #nontrivial prime factors`, and a castle with `p` peaks and `k` height-1 columns has `k + 1 - p` trivial factors `(1, 1)`, one for each pair of adjacent height-1 columns or height-1 column at an end. Checked through area 16.[^1]

## Convex castles

A [[convex-castle](pages/convex-castle.md)] has its height-1 columns only at its two ends, so `(1, C, 1) = (1,1)^a ∘ (1, X, 1) ∘ (1,1)^b`. **A convex castle has at most one nontrivial prime factor, and that factor is itself convex.** Convex castles are not closed under gluing, since `(1, X, 1) ∘ (1, Y, 1)` has a dip between `X` and `Y`. They are the words with at most one nontrivial letter, and that letter convex. The count of those letters, `U = 1, 1, 2, 3, 5, 8, 12, 19, ...`, is the second difference of A001523. Its asymptotics, its width triangle, its parity split, and the A342528 match of the first difference are on [[prime-convex-castles](pages/prime-convex-castles.md)].

## Prime refinement of the parity splits

Blocks are additive after the shift, so the block parity of a castle is decided by its prime factors. The trivial prime `(1, 1)` has one block and contributes nothing to `blocks - 1`. The full signed statement is on [[signed-prime-castles](pages/signed-prime-castles.md)], and the convex case, where a castle has the parity of its one nontrivial prime, is on [[prime-convex-castles](pages/prime-convex-castles.md)]. The parity split of all primes, with `n = 1..16` and even meaning an even block count as on [[castle-by-area](pages/castle-by-area.md)]:

| `n` | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| prime, even | 0 | 1 | 0 | 2 | 0 | 4 | 2 | 9 | 6 | 24 | 18 | 58 | 54 | 143 | 150 | 364 |
| prime, odd | 0 | 0 | 1 | 0 | 3 | 1 | 6 | 4 | 15 | 10 | 37 | 31 | 90 | 90 | 227 | 246 |

These are the `cev`/`cod` analogue for the Fibonacci count, with `even + odd = F_{n-1}`. Neither row, nor the difference `1, -1, 2, -3, 3, -4, 5, -9, 14, ...`, has an OEIS match, so all are novel-candidates.[^3]

## Computation

The factorization and the checks above, on every castle through area 16:

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

## Open

- Castles per multiset of prime factors, and which statistics besides area and blocks are additive over factors: on [[signed-prime-castles](pages/signed-prime-castles.md)].
- The prime refinement of the valley castles (A332578) and of `strict_valley` on [[castle-by-area](pages/castle-by-area.md)]. A valley castle can have height-1 columns in its interior, so it can have many nontrivial factors, unlike a convex castle.
- A product or q-series closed form for the prime parity GFs.

## Relation to other pages

- [[castle-by-area](pages/castle-by-area.md)]: the area counts and the `even`/`odd`/`cev`/`cod` splits refined here.
- [[castle-row-raising-equation](pages/castle-row-raising-equation.md)]: the functional equation the raised primes give, signed and by peaks.
- [[deutsch-elizalde-2017-bargraphs-dyck-paths](pages/deutsch-elizalde-2017-bargraphs-dyck-paths.md)]: the bijection that carries the prime factorization of Dyck paths to this one.
- [[deutsch-elizalde-2016-bargraphs-cornerless-motzkin](pages/deutsch-elizalde-2016-bargraphs-cornerless-motzkin.md)]: the raising map is its least-column-height bijection at `h = 1`, so by semi-perimeter the primes are all castles shifted by one (`0, 1, 2, 5, 13, 35, 97, …`, A082582(`s − 1`)), with the sign flipped.
- [[signed-prime-castles](pages/signed-prime-castles.md)]: the sign as a character of this monoid, the signed `P_s/(1 - P_s)` identity, and counts per multiset of primes.
- [[prime-convex-castles](pages/prime-convex-castles.md)]: the one nontrivial prime of a convex castle, counted.
- [[convex-castle](pages/convex-castle.md)]: the convex castles.
- [[castle-foata-transform](pages/castle-foata-transform.md)]: peaks, which count the nontrivial prime factors.
- [[metallic-means](pages/metallic-means.md)], [[algebraic-transcendental-wall](pages/algebraic-transcendental-wall.md)]: the golden ratio as the growth constant of the prime count.
- [[motzkin-castles](pages/motzkin-castles.md)]: the same castle bivariate generating function manipulated by the same width-variable substitution.
- [[q-thread-seminar](pages/q-thread-seminar.md)] - the castles-by-area seminar, which uses this page as one of its stops.

## Footnotes

[^1]: Checked by execution, 2026-09-22 (block above): every composition of `n ≤ 16` has padded block count equal to its own, satisfies `sum (blocks(prime) - 1) = blocks - 1` and `#factors = #height-1 columns + 1`, and has peak count equal to its number of nonempty factors; the prime counts are `F_{n-1}`. The `even`/`odd` totals of the same enumeration reproduce raw/oeis-pe502/vein9-area.md §"Parity splits" L46-47 [synthesis] - the `even(n)` / `odd(n)` rows for `n = 1..12`.
[^2]: https://oeis.org/A105422, https://oeis.org/A045623 (searched 2026-09-22, JSON format) - A105422 "Triangle read by rows: T(n,k) is the number of compositions of n having exactly k parts equal to 1"; A045623 "Number of 1's in all compositions of n+1". The triangle rows and the totals `1, 2, 5, 12, 28, 64, 144, 320, 704, 1536, 3328, 7168` for `n = 1..12` computed by execution, 2026-09-22.
[^3]: Computed by execution, 2026-09-22, over all castles through area 16. OEIS searches (https://oeis.org/search, JSON format, 2026-09-22) returned no results for either parity row or for the difference (as signed terms and as absolute values).
[^gl]: https://cs.uwaterloo.ca/journals/JIS/VOL16/Gessel/gessel6.pdf §2 "Free monoids" p.3 - "if M is a free monoid, then there exists a subset P of M such that every element of M has a unique factorization as a product of elements of P. We call P the set of primes of M."; "If L is a free monoid, then the factorization is always unique and the irreducible elements are the primes of L"; and the identity `Σ_{m∈M} x^{ω(m)} = (1 − Σ_{p∈P} x^{ω(p)})^{−1}` (their (3)) for a weight function `ω`. The list of Fibonacci identities in their §1 includes "F_{n−1} is the number of compositions of n into parts greater than 1".
[^de]: [[deutsch-elizalde-2017-bargraphs-dyck-paths](pages/deutsch-elizalde-2017-bargraphs-dyck-paths.md)] §3 L167, L236-245 - "(g) ret(P ) = #H1 (B) + 1 (unless P and B have height 1, in which case ret(P ) = #H1 (B))"; Prop. 3.5 "(i) φ(uP d) = U BD", "(ii) φ(P P ′ ) = B ◦ 1 ◦ B′ if height(P ) ≥ 2 and height(P ′ ) ≥ 2, B ◦ B′ otherwise", with `U BD` the bargraph "whose height sequence is obtained by adding one to each entry of the height sequence of B".
[^de-exec]: Own reasoning from Prop. 3.5 and Thm. 3.2(g), verified by execution (Python 3, 2026-10-02): `φ` implemented from its definition and applied to every Dyck path of semilength `≤ 11` is injective; every one-return path of semilength `≥ 2` goes to a castle with no height-1 column and every castle in the image with no height-1 column comes from a one-return path; returns `=` height-1 columns `+ 1` for every path of height `≥ 2`; and semilength `=` semiperimeter `−` peaks (their Thm. 3.2(a), [[deutsch-elizalde-2017-bargraphs-dyck-paths](pages/deutsch-elizalde-2017-bargraphs-dyck-paths.md)] §3 L155).
