---
title: q-thread seminar - castles by area
category: Concepts
summary: A seminar on castles graded by area, with one castle (2, 1, 3, 3, 1, 1, 2) carried through. A castle of area n is a composition of n, so there are 2^{n−1} of them. On the ladder of convex-polyomino families by area the castles are the bar graphs and the convex castles are the stacks (A001523). Convex and valley castles tie in every cell (w, h) at C(2h + w − 3, w − 1) but differ by area from n = 4 (8 against 7). Cutting at height-1 columns makes castles a free monoid whose primes are castles raised one row (F_{n−1} by area). The sign (−1)^{blocks−1} is a character of that monoid, so the signed count obeys the row-raising equation 1 + qz(2 − E(z)) = 1/(1 − qz E(qz)) and is 0.0985 (−1.62383)^n up to a relative error O(0.7508^n). The closed form is a sequence of parallelograms, Π/(1 − x − Π), over the Bousquet-Mélou-Fédou q-Bessel series, the Pólya q-Catalan family, and the pole is the first zero q_0 = −0.61583 of the q-Bessel denominator M, whose second zero q_1 = −0.82027 sets the error. With the height bounded, the counts by area are rational.
tags: [concept, castle, seminar, pedagogy, teaching, area, q-analog, q-catalan, q-motzkin, q-bessel, prime-castles, signed-count, polyomino, composition]
sources: [bousquet-melou-fedou-1995-convex-polyominoes, steep-polyominoes-q-motzkin-bessel, prellberg-brak-1995-cluster-models]
created: 2026-09-27
updated: 2026-10-16
---

# q-thread seminar - castles by area

**Thesis.** Count castles by their number of cells instead of by width and height, and the castle joins the classical polyomino literature. Area alone gives nothing new, since every composition is a castle. Area together with the block sign does: the sign is a character of a free monoid of prime castles, that gives a q-shift equation, and the equation is solved by the q-Bessel series that count parallelogram polyominoes, the Pólya q-Catalan family.

**Structure.** Eight stops (0 to 7), one castle carried through: `(2, 1, 3, 3, 1, 1, 2)`, area 13, width 7, 5 blocks. The pages behind it are [[castle-by-area](pages/castle-by-area.md)], [[convex-polyomino-by-area](pages/convex-polyomino-by-area.md)], [[prime-castles](pages/prime-castles.md)], [[signed-prime-castles](pages/signed-prime-castles.md)], [[castle-row-raising-equation](pages/castle-row-raising-equation.md)] and [[castle-q-bessel-closed-form](pages/castle-q-bessel-closed-form.md)]. The Snippet at the end computes every value that is not quoted from one of those pages. Notation follows [[castle-notation](pages/castle-notation.md)]: `q` marks area, `z` or `u` width, and `x` blocks.

## Stop 0 - area as the second variable

A castle is its skyline of column heights `(c_1, …, c_w)`, each at least 1, and its area is `n = c_1 + ⋯ + c_w`. So a castle of area `n` is a **composition** of `n`, every composition is a castle, and there are `2^{n−1}` of them.[^1]

Area alone therefore carries no information. Graded by width `u` and area `q` at unit block weight, the towers have generating function `1/(1 − u/(1 − q))`, each column height chosen independently ([[castle-q-bessel-closed-form](pages/castle-q-bessel-closed-form.md)], section *The graded grammar*). The block count is the vertical half-perimeter ([[castle-perimeter](pages/castle-perimeter.md)]), and the Project Euler condition "an even number of blocks" is the second statistic this seminar puts next to area.

*Idea:* area alone is trivial on castles, so it is paired with blocks.

## Stop 1 - the ladder

Each convex-polyomino family has a classical count by area, and the castles sit on two rungs of that ladder ([[convex-polyomino-by-area](pages/convex-polyomino-by-area.md)]):

```
 n     Ferrers   stack = convex castle   parallelogram   convex   bar graph = castle   column-convex
 4        5             8                     9            19            8                 19
 8       22            79                   242          1374          128               2017
12       77           512                  6842         57279         2048             212980
```

- **Stacks are convex castles**, A001523, the weakly unimodal compositions ([[weakly-unimodal-composition](pages/weakly-unimodal-composition.md)], [[stack-polyomino-gf](pages/stack-polyomino-gf.md)]). They grow subexponentially.
- **Parallelograms**, A006958, are the Pólya q-Catalan numbers ([[q-catalan-numbers](pages/q-catalan-numbers.md)]). The parallelogram, directed convex and convex polyominoes grow at the same constant `2.30914` by area ([[convex-polyomino-by-area](pages/convex-polyomino-by-area.md)]).
- **Castles are bar graphs**, `2^{n−1}`. They sit inside the directed column-convex polyominoes (`F_{2n−1}`, growth `φ² = 2.618`) and inside the column-convex ones (A001169, growth `3.20557`) ([[column-convex-ladder-by-area](pages/column-convex-ladder-by-area.md)]).

Two changes move a family between rungs. Give a stack a bottom boundary of its own that falls and then rises, and it becomes a convex polyomino: the growth jumps from subexponential to `2.309^n`. Keep the base flat but drop the unimodality of the top, as a castle does, and the growth is `2^n`.

*Idea:* place a new family among known ones and find the rule that separates it from its neighbors.

## Stop 2 - convex and valley: the same cells, different areas

A **convex** castle rises weakly and then falls weakly. A **valley** castle falls weakly and then rises weakly. At fixed width and height they have the same count in every cell ([[convex-castle-binomial-identity](pages/convex-castle-binomial-identity.md)], [[castle-by-area](pages/castle-by-area.md)]):

```
convex(w, h)  =  valley(w, h)  =  C(2h + w − 3, w − 1)          checked at (3,2) 6, (4,3) 35, (5,3) 70, (6,4) 462
```

By area they differ from `n = 4`:

```
 n        1  2  3  4   5   6   7   8    9   10   11   12
convex    1  2  4  8  15  27  47  79  130  209  330  512     A001523
valley    1  2  4  7  13  21  36  57   91  140  217  323     A332578
```

At `n = 4` all 8 compositions are convex, but the castle `(1, 2, 1)` is not a valley castle.[^1] So no bijection between the convex and the valley castles of each cell `(w, h)` also preserves the area.

*Idea:* equal counts in one grading ask for a bijection, and a second grading shows which statistics the bijection can keep.

## Stop 3 - primes: cutting at the ground floor

Pad the running castle with a height-1 column at each end, `(1, 2, 1, 3, 3, 1, 1, 2, 1)`, and cut at every interior height-1 column. The pieces are

```
(1, 2, 1)  ∘  (1, 3, 3, 1)  ∘  (1, 1)  ∘  (1, 2, 1)
```

glued by merging the last column of one piece with the first column of the next. Gluing loses exactly one cell, one column and one block, since the two bottom rows merge and nothing higher can touch across a height-1 column. Every padded castle factors this way in exactly one way, so the padded castles form a **free monoid** ([[prime-castles](pages/prime-castles.md)]):

- the **primes** are `(1, X, 1)` with `X` a castle having no height-1 column, and the trivial prime `(1, 1)`;
- by area the nonempty `X` are the compositions into parts `≥ 2`, which number `F_{n−1}`: `1, 1, 2, 3, 5, 8, 13, 21, …` from `n = 2`;
- a castle with `k` height-1 columns has `k + 1` prime factors. The running castle has three height-1 columns and four factors.

**The primes are castles raised one row.** An `X` with no height-1 column is a castle `Y` with a full row slid under it. Raising keeps the width, adds `width(Y)` cells and adds exactly one block.[^2] So the sequence construction reads "castles are sequences of castles raised one row", and with width `z` and area `q`, raising is the substitution `z → qz`. The prime generating function is `π(q) = q·B(q, q)`, with `B(q, z)` the castle generating function by area and width ([[prime-castles](pages/prime-castles.md)]).

*Idea:* find where an object can be cut so that the pieces glue back uniquely, and a free monoid turns the count into `1/(1 − primes)`.

## Stop 4 - the sign is a character

Under gluing, `blocks − 1` is additive: for the running castle, `5 − 1 = 4 = 1 + 2 + 0 + 1` over its four factors. So the sign `(−1)^{blocks − 1}` is a **character** of the monoid, a homomorphism to `{±1}` ([[signed-prime-castles](pages/signed-prime-castles.md)]), and a character passes through the sequence construction. With `E(q, z)` the signed castle generating function by area and width, empty castle included, the free monoid gives

```
1 + qz (2 − E(z))  =  1 / (1 − qz E(qz))
```

The `2` comes from the empty castle, counted `+1` in `E` but entering the monoid as `(1, 1)` with sign `+1` instead of `−1`. The right side at area `n + 1` uses `E` only through area `n − 1`, so this is a **recursion**: it computes the signed count one area at a time ([[castle-row-raising-equation](pages/castle-row-raising-equation.md)]). The identity holds through area 12 against enumeration.[^2] With `even(n)` and `odd(n)` the castles of area `n` with an even and an odd number of blocks,

```
even(n) − odd(n),  n = 1..16:   −1, 0, 0, 2, 0, 2, −4, 2, −12, 10, −20, 38, −44, 98, −136, 230

even(n) − odd(n)  ~  C (−ρ)^n,     ρ = 1.6238296740...,   C = 0.0985091749...
```

At `n = 16`, `C ρ^16 = 230.2` against `230`.[^3] The sign does not halve the growth exponent by area, since `√2 = 1.414` is below `ρ`; by semi-perimeter it does, `τ² → τ` ([[castle-perimeter](pages/castle-perimeter.md)]). Area, width, blocks and the number of height-1 columns, each minus one, and the number of peaks are additive over the factorization, so each gives a character; the number of left-to-right maxima and the height are not additive.[^2]

*Idea:* a statistic that is additive over a free factorization passes straight into the generating function; check additivity before looking for a formula.

## Stop 5 - castles are sequences of parallelograms

Grade the tower grammar by width `u`, blocks `x` and area `q`. With `E_∞(u)` the towers and `B(u)` the castles, the empty castle included, it becomes the q-shift equation `E_∞(u) = B(u)/(1 − u B(u))`, `B(u) = 1 − x + x E_∞(uq)`, whose recursion for `B` is a Möbius map, so it linearizes ([[castle-q-bessel-closed-form](pages/castle-q-bessel-closed-form.md)]):

```
castles(u, x, q)  =  Π / (1 − x − Π),          Π = Y J_1 / J_0  at width X = (1 − x)u, height Y = x

J_0(X, Y) = Σ_{n≥0} (−1)^n X^n q^{C(n+1,2)} / ((q)_n (Yq)_n)         (Bousquet-Mélou-Fédou)
```

`Π` is the generating function of the **parallelogram polyominoes** by width `X`, height `Y` and area `q`, a quotient of two q-analogues of Bessel functions.[^4] So `1 + castles` is the sequence construction on parallelograms, each weighted `u^w (1 − x)^{w − 1} x^h q^{area}`; the weight `(1 − x)^{w−1}` has negative coefficients, so this is an identity of series, not a weight-preserving bijection. Of the three q-Catalan families (Carlitz by inversions, MacMahon, Krattenthaler and Gessel by the down set, Pólya and Gessel by area), the one that appears is the Pólya-Gessel family, parallelograms by area, with width and height kept apart.[^5]

At the block sign `x = −1` and `u = 1` the formula is `N(q)/M(q) − 1`, with `N` and `M` q-series analytic in the unit disk. The signed count is **meromorphic** there, and its dominant pole is the first zero of `M`:

```
q_0 = −0.6158281351848...      −1/q_0 = 1.6238296740... = ρ
q_1 = −0.8202719776...         q_0/q_1 = 0.7508
```

The first zero gives the `ρ` of Stop 4 a second way. The second zero is real, and the relative error of `C(−ρ)^n` is `O(0.7508^n)`.[^3]

*Idea:* a Möbius q-shift equation linearizes; here the linear pieces are the Bousquet-Mélou-Fédou q-Bessel series.

## Stop 6 - the add-a-column equation, and q-Motzkin numbers

Unsigned, the castles by area have a rational generating function (`2^{n−1}`), and so do the column-convex polyominoes (A001169). Adding a column and recording the height of the new first column, both obey the Bousquet-Mélou add-a-column equation ([[castle-add-a-column-equation](pages/castle-add-a-column-equation.md)], [[column-convex-polygon-enumeration](pages/column-convex-polygon-enumeration.md)]). A column of height `l` can sit next to a column of height `k` in `k + l − 1` vertical positions in a column-convex polyomino, and in one position in a castle, with both bottoms on row 1. The kernel `k + l − 1` has rank 2 and the castle kernel `1` has rank 1, and each closes over that many moments to a rational generating function. The block weight `y^{max(0, l − k)}` depends on the sign of `l − k`, no finite set of moments closes it, and the equation stays a q-shift equation ([[castle-add-a-column-equation](pages/castle-add-a-column-equation.md)]).

Barcucci, Del Lungo, Fédou and Pinzani define three q-analogues of the Motzkin numbers, and relate the first to the steep parallelogram polyominoes by width, perimeter and area, again as a quotient of two q-Bessel functions.[^6] On the castle side, the tower word of a castle is a Motzkin path with no factor `UD` or `DU`, a cornerless Motzkin path ([[motzkin-castles](pages/motzkin-castles.md)], [[deutsch-elizalde-2016-bargraphs-cornerless-motzkin](pages/deutsch-elizalde-2016-bargraphs-cornerless-motzkin.md)]). Prodinger's weights `τ` on each `UD` and `σ` on each `DU` give the cornerless paths at `τ = σ = 0` and all Motzkin paths at `τ = σ = 1` ([[prodinger-2025-cornerless-motzkin-bargraphs](pages/prodinger-2025-cornerless-motzkin-bargraphs.md)]).

*Idea:* in the add-a-column equation, a kernel of finite rank gives a rational series, and the block weight is not of finite rank.

## Stop 7 - fix the height

With the height bounded, the counts by area are rational and their growth constants are algebraic numbers. The tree skylines by area (no `2 × 2` block of cells, height at most `h`) give one C-finite sequence per height: A000930 (Narayana's cows) at `h = 2`, A006498 at `h = 3`, A000570, the tournaments determined by their score vectors, at `h = 4`, and A005251, growth `ψ²`, with the height unrestricted; the tree castles of height `h` are the differences of consecutive rows ([[tree-castle-by-area](pages/tree-castle-by-area.md)]). Over all 0/1 strip rules, [[area-growth-census](pages/area-growth-census.md)] finds that the growth constant by area of a rule on height `h` is at most the `h`-nacci constant, below 2, and that the smallest one above 1 is the root of `z^T − z − 1` with `T = h(h+1)/2`. All ten smallest Pisot numbers appear by height 4, and Lehmer's number first appears at height 5.

*Idea:* bounded height turns counting by area into a finite transfer matrix, and the growth constants that occur are algebraic numbers with a smallest height each.

## Summary table

| grading | what castles are | number |
|---|---|---|
| area alone | compositions | `2^{n−1}` |
| area on the ladder | bar graphs; convex castles are stacks | A011782, A001523; growth 2, between the stacks and `2.309` |
| area against `(w, h)` | convex and valley castles tie in each cell and differ by area | `C(2h + w − 3, w − 1)`; 8 against 7 at `n = 4` |
| gluing | a free monoid of castles raised one row | primes `F_{n−1}` |
| area with the sign | a character, a q-shift recursion | `even − odd ~ 0.0985 (−1.62383)^n` |
| closed form | sequences of parallelograms | `Π/(1 − x − Π)`, Pólya q-Catalan, poles at `q_0 = −0.61583`, `q_1 = −0.82027` |
| tower words | cornerless Motzkin paths | Prodinger's weights at `τ = σ = 0` |
| bounded height | a finite transfer matrix | growth at most the `h`-nacci constant; smallest root of `z^T − z − 1` |

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

def cell(pred, w, h):                      # castles of width w and height h satisfying pred
    return sum(pred(c) for c in product(range(1, h + 1), repeat=w) if max(c) == h)

def additive(f):                           # f(padded) - 1 == sum of f(prime) - 1 over the factors
    return all(f((1,) + c + (1,)) - 1 == sum(f((1,) + x + (1,)) - 1 for x in primes(c))
               for n in range(1, 12) for c in comps(n))

def ltr_maxima(c):
    m = k = 0
    for v in c:
        if v > m: k, m = k + 1, v
    return k
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
>>> [additive(f) for f in (sum, len, blocks, lambda p: p.count(1), ltr_maxima, max)]
[True, True, True, True, False, False]
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

## Exercises

1. Factor `(3, 1, 1, 2, 2, 1)` into primes, and check that `blocks − 1` adds up over the factors.
2. Show that raising a castle one row adds exactly one block, and explain why Stop 4 needs exactly one rather than at least one.
3. List the eight compositions of 4 and find the one that is not a valley castle. Then explain why no bijection from convex to valley castles can keep both `(w, h)` and area.
4. Read off `even(5) − odd(5) = 0` from the row-raising recursion by hand, using `E` through area 3.

## Appearances in Sources

- [[bousquet-melou-fedou-1995-convex-polyominoes](pages/bousquet-melou-fedou-1995-convex-polyominoes.md)] - the parallelogram generating function `y J_1/J_0` over q-Bessel series, used in Stop 5.
- [[steep-polyominoes-q-motzkin-bessel](pages/steep-polyominoes-q-motzkin-bessel.md)] - three q-analogues of the Motzkin numbers, the first a quotient of q-Bessel functions, in Stop 6.
- [[prellberg-brak-1995-cluster-models](pages/prellberg-brak-1995-cluster-models.md)] - the linearization of q-shift equations of the shape of Stop 4's equation by writing the unknown as a ratio of solutions of a linear one.

## Related Concepts

- [[castle-by-area](pages/castle-by-area.md)], [[convex-polyomino-by-area](pages/convex-polyomino-by-area.md)], [[column-convex-ladder-by-area](pages/column-convex-ladder-by-area.md)] - the counts and the ladder of Stops 0 to 2.
- [[prime-castles](pages/prime-castles.md)], [[prime-convex-castles](pages/prime-convex-castles.md)], [[signed-prime-castles](pages/signed-prime-castles.md)], [[castle-row-raising-equation](pages/castle-row-raising-equation.md)] - the monoid, the character and the recursion of Stops 3 and 4.
- [[castle-q-bessel-closed-form](pages/castle-q-bessel-closed-form.md)], [[q-catalan-numbers](pages/q-catalan-numbers.md)], [[castle-add-a-column-equation](pages/castle-add-a-column-equation.md)] - the closed form, the q-Catalan families and the kernel ranks of Stops 5 and 6.
- [[motzkin-castles](pages/motzkin-castles.md)] - cornerless Motzkin paths and the castles counted by Motzkin numbers.
- [[tree-castle-by-area](pages/tree-castle-by-area.md)], [[area-growth-census](pages/area-growth-census.md)], [[castles-of-height-h-by-area](pages/castles-of-height-h-by-area.md)] - bounded height by area, Stop 7.
- [[fractional-block-count](pages/fractional-block-count.md)] - a statistic that interpolates between area and block count.
- [[castle-notation](pages/castle-notation.md)] - the area-grading symbols `B(q, z)`, `E(q, z)`, `N(q)`, `M(q)`, `Π`, `J_0`, `J_1`.
- [[tower-recursion-master-class](pages/tower-recursion-master-class.md)], [[hardin-identity-seminar](pages/hardin-identity-seminar.md)], [[hear-the-shape-seminar](pages/hear-the-shape-seminar.md)], [[oeis-mining-seminar](pages/oeis-mining-seminar.md)], [[one-bit-seminar](pages/one-bit-seminar.md)], [[sandcastle-seminar](pages/sandcastle-seminar.md)], [[castle-fibers-char-2-walkthrough](pages/castle-fibers-char-2-walkthrough.md)] - the other seminar pages.
- [[pell-castle-strip](pages/pell-castle-strip.md)], [[castle-cryptography](pages/castle-cryptography.md)], [[song-as-castle](pages/song-as-castle.md)] - the seminar pages on the Pell strip, castle cryptography, and audio as castles.

## Footnotes

[^1]: Verified by execution (Python 3.11, 2026-10-16): all compositions of `n ≤ 12`, the convex and valley counts by area, and the cells `(3, 2), (4, 3), (5, 3), (6, 4)` against `C(2h + w − 3, w − 1)`, as in the Snippet. The rows by area are the A001523 and A332578 rows of [[castle-by-area](pages/castle-by-area.md)] and [[convex-polyomino-by-area](pages/convex-polyomino-by-area.md)].
[^2]: Verified by execution (Python 3.11, 2026-10-16): `Σ (blocks(prime) − 1) = blocks − 1` over the prime factorization of every composition of `n ≤ 14`; raising adds one block for every composition of `n ≤ 12`; the prime counts `F_{n−1}`; area, width, blocks and height-1 columns, each minus one, additive over the factors for `n ≤ 11`, and left-to-right maxima and height not; `1 + qz(2 − E(z)) = 1/(1 − qz E(qz))` as a bivariate series through `q^12` with `E` by enumeration.
[^3]: Verified by execution (Python 3.11, 2026-10-16): the column dynamic program agrees with enumeration for `n ≤ 16`, and its ratio at `n = 120` is `−1.62382967400459`; bisection on `M(q)` truncated at `k = 60` gives `q_0 = −0.6158281351848058` and `q_1 = −0.820271977584318`, as on [[castle-q-bessel-closed-form](pages/castle-q-bessel-closed-form.md)] and [[castle-row-raising-equation](pages/castle-row-raising-equation.md)], whose `C` is used for the `n = 16` check.
[^4]: [[bousquet-melou-fedou-1995-convex-polyominoes](pages/bousquet-melou-fedou-1995-convex-polyominoes.md)] p.56 L151-160 [synthesis] - "Their generating function is the quotient of two q-analogues of Bessel-like functions", eq. (1) `X = y J_1/J_0` with the series `J_1` and `J_0`, as transcribed on that page and on [[castle-q-bessel-closed-form](pages/castle-q-bessel-closed-form.md)].
[^5]: raw/q-catalan-numbers.wiki §"q-Catalan Numbers" L7-9 - "Carlitz q-Catalan numbers count inversions of Dyck Words and Catalan permutations ... MacMahon, Krattenthaler, Gessel ... enumerate Dyck words by parameters of the down set ... Polya, Gessel ... count parallelogram polyominoes by area."
[^6]: [[steep-polyominoes-q-motzkin-bessel](pages/steep-polyominoes-q-motzkin-bessel.md)] p.1 (Abstract) - "We introduce three definitions of the q-analogs of Motzkin numbers ... We relate the first class of q-numbers to the steep parallelogram polyominoes' generating function according to their width, perimeter and area ... this generating function is the quotient of two q-Bessel functions."
