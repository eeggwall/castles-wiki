---
title: q-thread seminar - castles by area
category: Concepts
summary: The seminar walk-through for "The q-thread" arc - castles graded by area, one castle (2,1,3,3,1,1,2) carried through. A castle of area n is a composition of n, so there are 2^{n-1} of them, and area alone says nothing new. Area becomes informative only together with the block sign. On the convex-polyomino ladder the castle sits on two rungs (bar graphs 2^{n-1}, convex castles = stacks A001523). Convex and valley castles tie in every (w,h) cell at C(2h+w-3, w-1), but by area they already differ at n = 4 (8 against 7). Cutting at height-1 columns makes castles a free monoid whose primes are castles raised one row (F_{n-1} by area). The sign (-1)^{blocks-1} is a character of that monoid, so the signed count obeys the row-raising equation 1 + qz(2 - E(z)) = 1/(1 - qz E(qz)) and grows like 0.0985 (-1.62383)^n. The closed form is a sequence of parallelograms, Π/(1 - x - Π), over the Bousquet-Mélou-Fédou q-Bessel series. That is where the Pólya q-Catalan numbers meet the castle, and the pole is the first zero q_0 = -0.61583 of a q-Bessel denominator whose second zero q_1 = -0.82027 sets the error. q-Motzkin is the one meeting left open, through the cornerless-Motzkin reading and the corner weights. One runnable block pins every new value.
tags: [concept, castle, seminar, pedagogy, teaching, area, q-analog, q-catalan, q-motzkin, q-bessel, prime-castles, signed-count, polyomino, composition]
sources: [bousquet-melou-fedou-1995-convex-polyominoes, steep-polyominoes-q-motzkin-bessel]
created: 2026-09-27
updated: 2026-09-27
---

# q-thread seminar - castles by area

**Thesis.** Count castles by the number of cells instead of by width and height, and the castle joins the classical polyomino literature. Area alone gives nothing new: every composition is a castle. The structure comes from area together with the block sign. The sign is a character of a free monoid of prime castles. That gives a q-shift equation, and the equation solves in the same q-Bessel series that count parallelogram polyominoes, the Pólya q-Catalan family. The q-Motzkin family is the one meeting still open.

**Format.** About 75 minutes, eight stops, one castle carried through: `(2, 1, 3, 3, 1, 1, 2)`, area 13, width 7, 5 blocks. The research pages behind it are [[castle-by-area](pages/castle-by-area.md)], [[convex-polyomino-by-area](pages/convex-polyomino-by-area.md)], [[prime-castles](pages/prime-castles.md)], [[signed-klarner-decomposition](pages/signed-klarner-decomposition.md)], [[castle-row-raising-equation](pages/castle-row-raising-equation.md)] and [[castle-q-bessel-closed-form](pages/castle-q-bessel-closed-form.md)]. Every new computation is pinned by the Snippet block at the end. Values quoted from a research page link to it. Notation follows [[castle-notation](pages/castle-notation.md)]: `q` marks area, `z` or `u` width, and `x` blocks.

## Stop 0 - area as the second variable

A castle is read column by column as its heights `(c_1, ..., c_w)`, each at least 1. Its area is `n = c_1 + ... + c_w`. So a castle of area `n` is exactly a **composition** of `n`, and every composition is a castle. There are `2^{n-1}` of them.[^1]

Read that way, area carries no information on its own. The graded tower grammar on [[castle-q-bessel-closed-form](pages/castle-q-bessel-closed-form.md)] telescopes to `1/(1 - u/(1 - q))` at unit block weight, which is every height vector counted once. Area gets interesting only jointly with blocks, and blocks are the vertical half-perimeter ([[castle-perimeter](pages/castle-perimeter.md)]). The PE 502 question, "even number of blocks", is therefore the natural second statistic to put next to area.

*Idea:* area alone is trivial on castles, so it is paired with blocks.

## Stop 1 - the ladder

Every convex-polyomino family has a classical count by area, and the castle sits on two rungs of that ladder ([[convex-polyomino-by-area](pages/convex-polyomino-by-area.md)]):

```
 n     Ferrers   stack = convex castle   parallelogram   convex   bar graph = castle   column-convex
 4        5             8                     9            19            8                 19
 8       22            79                   242          1374          128               2017
12       77           512                  6842         57279         2048             212980
```

- **Stacks are convex castles**, A001523, the weakly unimodal compositions ([[weakly-unimodal-composition](pages/weakly-unimodal-composition.md)], [[stack-polyomino-gf](pages/stack-polyomino-gf.md)]). They grow subexponentially: a peak column plus two partitions.
- **Parallelograms**, A006958, are the Pólya q-Catalan numbers ([[q-catalan-numbers](pages/q-catalan-numbers.md)]). They, the directed convex and the convex polyominoes share one growth constant `2.30914`, because they share one q-Bessel denominator.
- **Castles are bar graphs**, `2^{n-1}`. They sit inside the directed column-convex polyominoes (`F_{2n-1}`, growth `φ² = 2.618`) and inside the column-convex ones (A001169, growth `3.20557`) ([[column-convex-ladder-by-area](pages/column-convex-ladder-by-area.md)]).

Two rules move the count between rungs. Free the bottoms of a stack to their own anti-unimodal profile and it becomes a convex polyomino: the growth jumps from subexponential to `2.309^n`. Keep the base flat but free the tops from unimodality, as a castle does, and the growth is `2^n`.

*Idea:* place a new family among known ones and identify the rule that separates it from its neighbours.

## Stop 2 - convex and valley: the same cells, different areas

A **convex** castle rises weakly and then falls weakly. A **valley** castle falls and then rises. At fixed width and height they tie in every cell ([[convex-castle-binomial-identity](pages/convex-castle-binomial-identity.md)], [[castle-by-area](pages/castle-by-area.md)]):

```
convex(w, h)  =  valley(w, h)  =  C(2h + w - 3, w - 1)          checked at (3,2) 6, (4,3) 35, (5,3) 70, (6,4) 462
```

By area they split at once:

```
 n        1  2  3  4   5   6   7   8    9   10   11   12
convex    1  2  4  8  15  27  47  79  130  209  330  512     A001523
valley    1  2  4  7  13  21  36  57   91  140  217  323     A332578
```

At `n = 4` all 8 compositions are convex, but `(1, 2, 1)` is not a valley.[^1] So the bijection the cell counts ask for, still open, cannot also keep the area. Area is a statistic the two families do not share, even though width and height are.

*Idea:* equal counts in one grading are a question for a bijection, and a second grading is the quickest way to rule a bijection in or out.

## Stop 3 - primes: cutting at the ground floor

Take the running castle and pad it with a height-1 column at each end: `(1, 2, 1, 3, 3, 1, 1, 2, 1)`. Cut at every interior height-1 column. The pieces are

```
(1, 2, 1)  ∘  (1, 3, 3, 1)  ∘  (1, 1)  ∘  (1, 2, 1)
```

glued by merging the last column of one piece with the first column of the next. Gluing loses exactly one cell, one column and one block, since the two bottom rows merge and nothing higher can touch across a height-1 column. Every padded castle factors this way in exactly one way, so padded castles form a **free monoid** ([[prime-castles](pages/prime-castles.md)]):

- the **primes** are `(1, X, 1)` with `X` a castle having no height-1 column, plus the trivial prime `(1, 1)`;
- by area the nonempty `X` are the compositions into parts `≥ 2`, which number `F_{n-1}`: `1, 1, 2, 3, 5, 8, 13, 21, ...` from `n = 2`;
- a castle with `k` height-1 columns has `k + 1` prime factors. The running castle has three height-1 columns and four factors.

**The primes are castles raised one row.** An `X` with no height-1 column is some castle `Y` with a full row slid under it. Raising keeps the width, adds `width(Y)` cells and adds exactly one block.[^2] So the sequence construction reads "castles are sequences of castles raised one row". With width `z` and area `q`, raising is the substitution `z → qz`.

*Idea:* find where an object can be cut so that the pieces glue back uniquely, and a free monoid turns the count into `1/(1 - primes)`.

## Stop 4 - the sign is a character

Under gluing, `blocks - 1` is additive: the running castle has `5 - 1 = 4 = 1 + 2 + 0 + 1`. So the sign `(-1)^{blocks - 1}` is a **character** of the monoid, a homomorphism to `{±1}` ([[signed-klarner-decomposition](pages/signed-klarner-decomposition.md)]). A character rides through the sequence construction. With `E(q, z)` the signed castle GF by area and width, empty castle included, the free monoid gives

```
1 + qz (2 - E(z))  =  1 / (1 - qz E(qz))
```

The `2` is the empty castle, counted `+1` in `E` but entering the monoid as `(1, 1)` with sign `+1` instead of `-1`. The right side at area `n + 1` uses `E` only through area `n - 1`, so this is a **recursion**. It computes the signed count one area at a time with no enumeration ([[castle-row-raising-equation](pages/castle-row-raising-equation.md)]). The identity holds through area 12 against brute force.[^2] The count is

```
even(n) - odd(n),  n = 1..16:   -1, 0, 0, 2, 0, 2, -4, 2, -12, 10, -20, 38, -44, 98, -136, 230

even(n) - odd(n)  ~  C (-ρ)^n,     ρ = 1.6238296740...,   C = 0.0985091750...
```

Already at `n = 16`, `C ρ^16 = 230.2` against the true `230`.[^3] The sign does not halve the growth exponent: `√2 = 1.414` is well below `ρ`. By semi-perimeter it does, `τ² → τ` ([[castle-perimeter](pages/castle-perimeter.md)]). Which statistics are characters is a short list: area, width, blocks, height-1 columns, peaks and base-leaving records are, while left-to-right maxima and height are not.

*Idea:* a statistic that is additive over a free factorization passes straight into the generating function. Check additivity before looking for a formula.

## Stop 5 - castles are sequences of parallelograms

Grade the tower grammar by area as well as blocks. It becomes the q-shift equation `E(u) = A/(1 - uA)`, `A = 1 - x + x E(uq)`, a Möbius recursion that linearizes. Its solution packages as ([[castle-q-bessel-closed-form](pages/castle-q-bessel-closed-form.md)])

```
castles(u, x, q)  =  Π / (1 - x - Π),          Π = Y J_1 / J_0  at width X = (1 - x)u, height Y = x

J_0(X, Y) = Σ_{n≥0} (-1)^n X^n q^{C(n+1,2)} / ((q)_n (Yq)_n)         (Bousquet-Mélou-Fédou)
```

`Π` is the generating function of **parallelogram polyominoes** by width, height and area, a quotient of two q-analogues of Bessel functions.[^4] So `1 + castles` is a sequence of parallelograms, each weighted `(1 - x)^{w - 1} x^h`. This is where the q-Catalan thread lands. Of the three q-Catalan families (Carlitz by inversions, MacMahon by the down set, Pólya-Gessel by area), the castle meets the Pólya-Gessel one, parallelograms by area, with width and height kept apart.[^5] The Carlitz family does not appear.

At the block sign `x = -1` the formula is `N(q)/M(q) - 1`, with `N` and `M` q-series that converge in the whole unit disk. The signed count is **meromorphic** there, and its poles are the zeros of `M`:

```
q_0 = -0.6158281351848...      -1/q_0 = 1.6238296740... = ρ
q_1 = -0.8202719776...         q_0/q_1 = 0.7508
```

The first zero is the `ρ` of Stop 4, found a second way. The second zero is real, so the relative error of `C(-ρ)^n` is `O(0.7508^n)`.[^3]

*Idea:* a Möbius q-shift equation linearizes; here the linear pieces are the Bousquet-Mélou–Fédou q-Bessel series.

## Stop 6 - why a q-series, and the q-Motzkin door

Unsigned, castles by area are rational (`2^{n-1}`), and so are column-convex polyominoes (A001169). Add a column, recording the height of the new first column, and both obey the Bousquet-Mélou add-a-column equation ([[castle-add-a-column-equation](pages/castle-add-a-column-equation.md)], [[column-convex-polygon-enumeration](pages/column-convex-polygon-enumeration.md)]). A castle keeps 1 of Temperley's `k + l - 1` ways to place a column next to the last one, an area kernel of rank 1 against A001169's rank 2. The block weight `y^{max(0, l - k)}` has **no finite rank**, and that is why the signed count is a q-series rather than a rational function.

The third classical q-family is **q-Motzkin**. Barcucci, Del Lungo, Fédou and Pinzani give three q-Motzkin analogues. The first counts steep parallelogram polyominoes by width, perimeter and area, again as a quotient of two q-Bessel functions.[^6] On the castle side, a castle is a cornerless Motzkin path ([[motzkin-castles](pages/motzkin-castles.md)], [[deutsch-elizalde-2016-bargraphs-cornerless-motzkin](pages/deutsch-elizalde-2016-bargraphs-cornerless-motzkin.md)]). Restoring the corners with Prodinger's weights ([[prodinger-2025-cornerless-motzkin-bargraphs](pages/prodinger-2025-cornerless-motzkin-bargraphs.md)]) walks from castles to all Motzkin paths. Doing that walk with area tracked would join the castle q-Bessel form to a q-Motzkin number directly. That join has not been done.

*Idea:* the rank of the kernel separates rational generating functions from q-series.

## Stop 7 - fix the height

Bounding the height keeps everything rational, and the area grading then tests the number theory of the growth constants. Tree castles by area (no `2 × 2` block) give one C-finite sequence per height: Narayana's cows at `h = 2`, A006498 at `h = 3`, the score-determined tournaments A000570 at `h = 4`, and A005251, growth `ψ²`, as `h → ∞` ([[tree-castle-by-area](pages/tree-castle-by-area.md)]). Over all 0/1 strip rules, [[area-growth-census](pages/area-growth-census.md)] finds that the growth constants by area lie in `(1, 2)`. The smallest one at height `h` is the root of `z^T - z - 1` with `T = h(h+1)/2`. All ten smallest Pisot numbers appear by height 4, and Lehmer's number first appears at height 5.

*Idea:* bounded height turns area counting into a finite transfer matrix. The question then moves from "what is the series" to "which algebraic numbers are reachable".

## The board

| grading | what castles are | number |
|---|---|---|
| area alone | compositions | `2^{n-1}`, no information |
| area on the ladder | bar graphs; convex castles are stacks | A011782, A001523; growth 2 between stacks and `2.309` |
| area vs `(w, h)` | convex and valley tie in cells, split by area | `C(2h+w-3, w-1)` vs 8 against 7 at `n = 4` |
| gluing | a free monoid of castles raised one row | primes `F_{n-1}` |
| area with the sign | a character, a q-shift recursion | `even - odd ~ 0.0985 (-1.62383)^n` |
| closed form | sequences of parallelograms | `Π/(1 - x - Π)`, Pólya q-Catalan, poles at `q_0 = -0.61583`, `q_1 = -0.82027` |
| q-Motzkin | cornerless Motzkin paths | open: corner weights with area |
| bounded height | a finite transfer matrix | growth in `(1, 2)`, smallest root of `z^T - z - 1` |

## Snippet

```python
from itertools import product
from math import comb

def comps(n):                              # compositions of n = castles of area n
    if n == 0: yield (); return
    for f in range(1, n + 1):
        for r in comps(n - f): yield (f,) + r

def blocks(c):                             # each rise in the skyline starts new blocks
    return sum(max(0, b - a) for a, b in zip((0,) + c, c))

def convex(c):                             # weakly up, then weakly down
    i = 0
    while i + 1 < len(c) and c[i+1] >= c[i]: i += 1
    return all(c[j+1] <= c[j] for j in range(i, len(c) - 1))
valley = lambda c: convex(tuple(-x for x in c))

def primes(c):                             # the X of each factor (1, X, 1) of (1, C, 1)
    segs, cur = [], []
    for x in c:
        if x == 1: segs.append(tuple(cur)); cur = []
        else: cur.append(x)
    return segs + [tuple(cur)]

def signed(N):                             # even - odd by area, column DP on (area, last height)
    dp = [dict() for _ in range(N + 1)]; dp[0][0] = 1
    for n in range(N):
        for a, wt in dp[n].items():
            for b in range(1, N - n + 1):
                dp[n + b][b] = dp[n + b].get(b, 0) + wt * (-1)**max(0, b - a)
    return [sum(d.values()) for d in dp]

def E_brute(N):                            # signed castles by (area, width), empty castle included
    E = {(0, 0): 1}
    for n in range(1, N + 1):
        for c in comps(n): E[n, len(c)] = E.get((n, len(c)), 0) + (-1)**blocks(c)
    return E

def mul(a, b, N):                          # bivariate series in (q, z), truncated at q^N
    r = {}
    for (i, j), x in a.items():
        for (k, l), y in b.items():
            if i + k <= N: r[i + k, j + l] = r.get((i + k, j + l), 0) + x * y
    return r

def row_raising_holds(N):                  # 1 + qz(2 - E(z)) == 1/(1 - qz E(qz)) through q^N
    E = E_brute(N)
    lhs = {(0, 0): 1, (1, 1): 2}
    for (n, w), c in E.items():
        if n + 1 <= N: lhs[n + 1, w + 1] = lhs.get((n + 1, w + 1), 0) - c
    X = {(n + w + 1, w + 1): c for (n, w), c in E.items() if n + w + 1 <= N}   # qz E(qz)
    rhs, term = {(0, 0): 1}, {(0, 0): 1}
    for _ in range(N):
        term = mul(term, X, N)
        for k, v in term.items(): rhs[k] = rhs.get(k, 0) + v
    clean = lambda d: {k: v for k, v in d.items() if v}
    return clean(lhs) == clean(rhs)

def M(q, K=60):                            # the q-Bessel denominator of the signed count (x = -1, u = 1)
    s, p2 = 1.0, 1.0                       # p2 = (q^2; q^2)_(k-1)
    for k in range(1, K):
        s += (-1)**k * 2**(k - 1) * q**(k*(k+1)//2) / (p2 * (1 - q**k))
        p2 *= 1 - q**(2*k)
    return s

def root(f, a, b):                         # bisection
    for _ in range(200):
        m = (a + b) / 2
        a, b = (m, b) if f(a) * f(m) > 0 else (a, m)
    return a

def cell(pred, w, h):                      # castles of width w, height exactly h satisfying pred
    return sum(pred(c) for c in product(range(1, h + 1), repeat=w) if max(c) == h)
```

```
>>> all(sum(1 for _ in comps(n)) == 2**(n - 1) for n in range(1, 13))
True
>>> [sum(convex(c) for c in comps(n)) for n in range(1, 13)]
[1, 2, 4, 8, 15, 27, 47, 79, 130, 209, 330, 512]
>>> [sum(valley(c) for c in comps(n)) for n in range(1, 13)]
[1, 2, 4, 7, 13, 21, 36, 57, 91, 140, 217, 323]
>>> [(w, h, cell(convex, w, h), cell(valley, w, h), comb(2*h + w - 3, w - 1)) for w, h in [(3, 2), (4, 3), (5, 3), (6, 4)]]
[(3, 2, 6, 6, 6), (4, 3, 35, 35, 35), (5, 3, 70, 70, 70), (6, 4, 462, 462, 462)]
>>> C = (2, 1, 3, 3, 1, 1, 2); sum(C), blocks(C), primes(C)
(13, 5, [(2,), (3, 3), (), (2,)])
>>> [sum(1 for c in comps(n) if 1 not in c) for n in range(1, 13)]
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
>>> all(sum(blocks((1,) + x + (1,)) - 1 for x in primes(c)) == blocks(c) - 1 for n in range(1, 15) for c in comps(n))
True
>>> all(blocks(tuple(x + 1 for x in c)) == blocks(c) + 1 for n in range(1, 13) for c in comps(n))
True
>>> row_raising_holds(12)
True
>>> t = signed(120); t[1:17]
[-1, 0, 0, 2, 0, 2, -4, 2, -12, 10, -20, 38, -44, 98, -136, 230]
>>> t[1:17] == [sum((-1)**blocks(c) for c in comps(n)) for n in range(1, 17)]
True
>>> t[120] / t[119]
-1.6238296740045883
>>> q0, q1 = root(M, -0.7, -0.5), root(M, -0.83, -0.81); q0, -1/q0, q1, q0/q1
(-0.6158281351848058, 1.6238296740045934, -0.820271977584318, 0.7507609085932759)
>>> round(0.0985091749731156 * (-1/q0)**16, 1)
230.2
```

## Exercises for the room

1. Factor `(3, 1, 1, 2, 2, 1)` into primes, and check that `blocks - 1` adds up over the factors.
2. Show that raising a castle one row adds exactly one block. Why does it matter for Stop 4 that it adds exactly one, not "at least one"?
3. List the eight compositions of 4 and find the one that is not a valley. Then explain why no bijection from convex to valley castles can keep both `(w, h)` and area.
4. Read off `even(5) - odd(5) = 0` from the row-raising recursion by hand, using `E` through area 3.
5. (Open.) Write down an explicit bijection between convex and valley castles in each `(w, h)` cell. The peak/valley mirror suggests one, and Exercise 3 says it must move the area.
6. (Open.) Put Prodinger's corner weights and area into one equation, and decide whether the q-kernel still cancels one root. At both corner weights 1 this is Motzkin paths by area, a q-Motzkin number of the kind Barcucci et al. study.

## What is still open

The open problems that bear on this seminar:

- **Convex to valley bijection**, in every `(w, h)` cell (Exercise 5).
- **`h = 3` bounded-height tree-vs-all bijection** by area.
- **Area with the corner weights**, the q-Motzkin join of Stop 6 (Exercise 6).
- **Descents Narayana bijection.** By descents only the end cells are q-binomials, so area does not factor as q-Narayana times q-binomial ([[castle-q-bessel-closed-form](pages/castle-q-bessel-closed-form.md)]).
- **Convex / unimodal exact enumeration with parity** at fixed `(w, h)`.
- **Min height for every algebraic area constant**, and its perimeter counterpart (Stop 7).

## Appearances in Sources

- [[bousquet-melou-fedou-1995-convex-polyominoes](pages/bousquet-melou-fedou-1995-convex-polyominoes.md)] - the parallelogram GF `y J_1/J_0` over q-Bessel series, used in Stop 5.
- [[steep-polyominoes-q-motzkin-bessel](pages/steep-polyominoes-q-motzkin-bessel.md)] - three q-Motzkin analogues, the first a q-Bessel quotient, in Stop 6.
- [[prellberg-brak-1995-cluster-models](pages/prellberg-brak-1995-cluster-models.md)] - the Möbius linearization of quadratic q-shift equations behind Stop 5.

## Related Concepts

- [[castle-by-area](pages/castle-by-area.md)] / [[convex-polyomino-by-area](pages/convex-polyomino-by-area.md)] / [[column-convex-ladder-by-area](pages/column-convex-ladder-by-area.md)] - the counts and the ladder of Stops 0-2.
- [[prime-castles](pages/prime-castles.md)] / [[prime-convex-castles](pages/prime-convex-castles.md)] / [[signed-klarner-decomposition](pages/signed-klarner-decomposition.md)] / [[castle-row-raising-equation](pages/castle-row-raising-equation.md)] - the monoid, the character and the recursion of Stops 3-4.
- [[castle-q-bessel-closed-form](pages/castle-q-bessel-closed-form.md)] / [[q-catalan-numbers](pages/q-catalan-numbers.md)] / [[castle-add-a-column-equation](pages/castle-add-a-column-equation.md)] - the closed form, the q-Catalan families and the rank argument of Stops 5-6.
- [[motzkin-castles](pages/motzkin-castles.md)] - the Motzkin arc, whose corner weights are the q-Motzkin door of Stop 6.
- [[tree-castle-by-area](pages/tree-castle-by-area.md)] / [[area-growth-census](pages/area-growth-census.md)] - bounded height by area, Stop 7.
- [[fractional-block-count](pages/fractional-block-count.md)] - a statistic that interpolates between area and block count.
- [[castle-notation](pages/castle-notation.md)] - the area-layer symbols `E(q, z)`, `N(q)`, `M(q)`, `Π`, `J_0`, `J_1`.
- [[tower-recursion-master-class](pages/tower-recursion-master-class.md)] / [[hardin-identity-seminar](pages/hardin-identity-seminar.md)] / [[hear-the-shape-seminar](pages/hear-the-shape-seminar.md)] / [[oeis-mining-seminar](pages/oeis-mining-seminar.md)] / [[one-bit-seminar](pages/one-bit-seminar.md)] / [[sandcastle-seminar](pages/sandcastle-seminar.md)] / [[castle-fibers-char-2-walkthrough](pages/castle-fibers-char-2-walkthrough.md)] - the other seminar pages.
- [[pell-castle-strip](pages/pell-castle-strip.md)] / [[castle-cryptography](pages/castle-cryptography.md)] / [[song-as-castle](pages/song-as-castle.md)] - the seminar pages of the silver-ratio strip, the castle cryptography series, and audio as castles.

## Footnotes

[^1]: Verified by execution (Python 3.10, 2026-09-27): all compositions of `n ≤ 12` enumerated, the convex and valley counts by area and the `(w, h)` cells at `(3, 2), (4, 3), (5, 3), (6, 4)` against `C(2h + w - 3, w - 1)`, as pinned in the Snippet. The by-area rows agree with the A001523 and A332578 terms on [[castle-by-area](pages/castle-by-area.md)] and [[convex-polyomino-by-area](pages/convex-polyomino-by-area.md)].
[^2]: Verified by execution (Python 3.10, 2026-09-27): the prime factorization of every composition of `n ≤ 14` satisfies `Σ (blocks(prime) − 1) = blocks − 1`; raising adds one block for every composition of `n ≤ 12`; the prime counts are `F_{n-1}`; and `1 + qz(2 − E(z)) = 1/(1 − qz E(qz))` holds as a bivariate series through `q^12`, with `E` from brute force. As a control, the same check with `1` in place of `2` returns `False`.
[^3]: Verified by execution (Python 3.10, 2026-09-27): the column DP agrees with brute force for `n ≤ 16`, and its ratio at `n = 120` gives `−1.62382967400459`. Bisection on the q-Bessel series `M(q)` (truncated at `k = 60`) gives `q_0 = −0.6158281351848058` and `q_1 = −0.820271977584318`. These agree with the 30-digit values on [[castle-q-bessel-closed-form](pages/castle-q-bessel-closed-form.md)] and [[castle-row-raising-equation](pages/castle-row-raising-equation.md)], whose `C` is used for the `n = 16` check.
[^4]: [[bousquet-melou-fedou-1995-convex-polyominoes](pages/bousquet-melou-fedou-1995-convex-polyominoes.md)] p.56 L153-184 and Appendix A p.72 L984-1131 [synthesis] - eq. (1) `X = y J_1/J_0`, "the quotient of two q-analogues of Bessel-like functions", and the `J_0`, `J_1` series as transcribed from the page images on that page.
[^5]: raw/q-catalan-numbers.wiki §"q-Catalan Numbers" L7-9 - "Carlitz q-Catalan numbers count inversions of Dyck Words and Catalan permutations ... MacMahon, Krattenthaler, Gessel ... enumerate Dyck words by parameters of the down set ... Polya, Gessel ... count parallelogram polyominoes by area."
[^6]: [[steep-polyominoes-q-motzkin-bessel](pages/steep-polyominoes-q-motzkin-bessel.md)] p.1 (Abstract) - "We introduce three definitions of the q-analogs of Motzkin numbers ... We relate the first class of q-numbers to the steep parallelogram polyominoes' generating function according to their width, perimeter and area ... this generating function is the quotient of two q-Bessel functions."
