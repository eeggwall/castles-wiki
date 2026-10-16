---
title: Tree castle by area - Narayana's cows, A006498, tournaments, and plastic
category: Analyses
summary: Tree skylines (no two neighboring columns of height at least 2) of height at most h, counted by width and area, have generating function (1 + P_h(q)x)/(1 − qx − qP_h(q)x²) with P_h(q) = q² + ⋯ + q^h. By area alone they are the compositions of A + 1 into parts {1, 3, 4, …, h + 1}, so their counts are A000930 (Narayana's cows) at h = 2, A006498 at h = 3, A000570 (tournaments determined by their score vectors) at h = 4, A079816, A189593, A189600 at h = 5, 6, 7, and A005251 with the height unrestricted, all with index shift A + 1 (A + 2 for A005251). The tree castles of height 2 by area are A077868. By area the tree skylines of height at most 2 are supergolden, those of height at most 3 golden, and those of any height grow at ψ²; the other growth constants have degree 5 or 6. At h = 4, Tetali's classification of the tournaments determined by their score vectors gives a bijection between these tree skylines and those tournaments, through compositions into {1, 3, 4, 5}, rechecked here by enumeration of all tournaments on at most 8 vertices.
tags: [analysis, castle, tree-castle, area, generating-function, q-analogue, oeis, narayana-cows, plastic-number, supergolden, fibonacci, sympy, verification]
sources: [tetali-1998-unique-tournaments]
created: 2026-09-17
updated: 2026-10-16
---

# Tree castle by area

A **tree skyline** of height at most `h` is a skyline in `{1, …, h}^w` in which no two neighboring columns both have height at least 2. It need not reach height `h`; the tree skylines that do are the **tree castles** of height `h`, the castles whose castle graph is a tree ([[castle-graph](pages/castle-graph.md)]). With the height unrestricted, every tree skyline is a tree castle of its own height. This page counts both by **area**, the number of cells `c_1 + ⋯ + c_w`.

*Example.* The tree skylines of area 4 are `(1, 1, 1, 1)`, `(1, 1, 2)`, `(1, 2, 1)`, `(2, 1, 1)`, `(1, 3)`, `(3, 1)` and `(4)`. Three of them are tree castles of height 2, two of height 3 and one of height 4.

## The generating function

Write `P_h(q) = q² + q³ + ⋯ + q^h` for the area weights of one column of height at least 2, and `T_h(w, q)` for the sum of `q^{area}` over the tree skylines of width `w` and height at most `h`, with `T_h(0, q) = 1` for the empty skyline. A tree skyline is an optional first column of height at least 2, followed by a sequence of columns of height 1, each followed or not by one column of height at least 2, so[^1]

```
Σ_{w≥0} T_h(w, q) x^w  =  (1 + P_h(q)·x) / (1 − q·x − q·P_h(q)·x²).                (1)
```

Equivalently, by the last column,

```
T_h(w, q)  =  q·T_h(w−1, q) + q·P_h(q)·T_h(w−2, q),        T_h(0, q) = 1,   T_h(1, q) = q + P_h(q).      (2)
```

At `q = 1`, Equation (2) is Equation (1) of [[castle-graph](pages/castle-graph.md)], `T_h(w+2) = T_h(w+1) + (h−1)·T_h(w)`, with `T_h(w) = F_{w+2}`, `A001045(w+2)`, `A006130(w+1)` and `A006131(w+1)` at `h = 2, 3, 4, 5`. The tree castles of width `w` and height `h` have the area polynomial `T_h(w, q) − T_{h−1}(w, q)`.

## The triangle at height 2

The tree castles of height 2, by width `w` and by the number `t = area − w` of columns of height 2, `t ≥ 1`:

| w \ t | 1 | 2 | 3 | 4 | 5 | row sum |
|---|---|---|---|---|---|---|
| 1 | 1 | | | | | 1 |
| 2 | 2 | | | | | 2 |
| 3 | 3 | 1 | | | | 4 |
| 4 | 4 | 3 | | | | 7 |
| 5 | 5 | 6 | 1 | | | 12 |
| 6 | 6 | 10 | 4 | | | 20 |
| 7 | 7 | 15 | 10 | 1 | | 33 |
| 8 | 8 | 21 | 20 | 5 | | 54 |
| 9 | 9 | 28 | 35 | 15 | 1 | 88 |
| 10 | 10 | 36 | 56 | 35 | 6 | 143 |

Choosing `t` pairwise non-adjacent columns among `w` can be done in `C(w − t + 1, t)` ways, which is each entry, and the row sums are `F_{w+2} − 1 = A000071(w+2)`, the Fibonacci castles of [[fibonacci-castle](pages/fibonacci-castle.md)]. Every entry agrees with brute-force enumeration.[^2]

## By area at fixed height

Setting `x = 1` in Equation (1) gives the generating function of the tree skylines of height at most `h` by area, with the empty skyline as the constant term:

```
G_h(q)  =  (1 + P_h(q)) / (1 − q − q·P_h(q)).                                       (3)
```

**Table 1.** Tree skylines of height at most `h` with area `A`, the coefficient of `q^A` in `G_h(q)`:

| `h` | `A = 1, 2, …, 14` | OEIS | reversed denominator | growth constant |
|---|---|---|---|---|
| 2 | `1, 2, 3, 4, 6, 9, 13, 19, 28, 41, 60, 88, 129, 189` | `A000930(A + 1)`, Narayana's cows | `x³ − x² − 1` | supergolden, `1.465571…` |
| 3 | `1, 2, 4, 6, 9, 15, 25, 40, 64, 104, 169, 273, 441, 714` | `A006498(A + 1)` | `(x² + 1)(x² − x − 1)` | golden, `φ = 1.618034…` |
| 4 | `1, 2, 4, 7, 11, 18, 31, 53, 89, 149, 251, 424, 715, 1204` | `A000570(A + 1)` | `x⁵ − x⁴ − x² − x − 1` | `1.685137…` |
| 5 | `1, 2, 4, 7, 12, 20, 34, 59, 102, 175, 300, 515, 885, 1521` | `A079816(A + 1)` | `x⁶ − x⁵ − x³ − x² − x − 1` | `1.717830…` |
| 6 | `1, 2, 4, 7, 12, 21, 36, 62, 108, 188, 326, 565, 980, 1700` | `A189593(A + 1)` | `(x² − x + 1)(x⁵ − x³ − 2x² − 2x − 1)` | `1.734691…` |
| 7 | `1, 2, 4, 7, 12, 21, 37, 64, 111, 194, 339, 591, 1030, 1796` | `A189600(A + 1)` | `(x² + 1)(x⁶ − x⁵ − x⁴ − x − 1)` | `1.743700…` |
| 8 | `1, 2, 4, 7, 12, 21, 37, 65, 113, 197, 345, 604, 1056, 1846` | | `x⁹ − x⁸ − x⁶ − x⁵ − ⋯ − 1` | |
| ∞ | `1, 2, 4, 7, 12, 21, 37, 65, 114, 200, 351, 616, 1081, 1897` | `A005251(A + 2)` | `x³ − 2x² + x − 1` | `ψ² = 1.754878…` |

Every entry agrees with brute-force enumeration for `A ≤ 10` and with Equation (3) for `A ≤ 14`, and the OEIS identifications hold for every listed term of each entry.[^3] The reversed denominator is `x^d D(1/x)` for the denominator `D(q)` of Equation (3), and the growth constant is its root of largest modulus. [[castle-sequence-catalogue](pages/castle-sequence-catalogue.md)] records the OEIS status of the row `h = 8`.

**Table 2.** Tree castles of height `h` with area `A`, the coefficient of `q^A` in `G_h(q) − G_{h−1}(q)`:

| `h` | `A = 1, 2, …, 14` | OEIS | growth constant |
|---|---|---|---|
| 2 | `0, 1, 2, 3, 5, 8, 12, 18, 27, 40, 59, 87, 128, 188` | `A077868(A − 2)` for `A ≥ 2`, `= A000930(A + 1) − 1` | supergolden |
| 3 | `0, 0, 1, 2, 3, 6, 12, 21, 36, 63, 109, 185, 312, 525` | | golden |
| 4 | `0, 0, 0, 1, 2, 3, 6, 13, 25, 45, 82, 151, 274, 490` | | `1.685137…` |

The growth constant of `G_h` increases with `h`, so the tree castles of height `h` grow at the rate of the tree skylines of height at most `h`. In the terms of [[castle-classification-growth](pages/castle-classification-growth.md)], the tree castles of height 2 are supergolden by area, those of height 3 golden by area, and the tree castles of any height grow at `ψ²` by area. The `h = 3` constant is golden because the denominator factors as `(1 + q²)(1 − q − q²)`; the counts are not Fibonacci numbers, but `A006498(2n) = F_{n+1}²` and `A006498(2n − 1) = F_{n+1}·F_n`.[^3]

Apart from `φ` at `h = 3`, none of these growth constants is a metallic mean: each is a root of an irreducible polynomial of degree 3, 5 or 6 (the factor carrying the largest root in Table 1), while every metallic mean `σ_p^q` is a root of `x² − px − q` ([[metallic-means](pages/metallic-means.md)]).

## Compositions

Let `C_h(q) = 1/(1 − q − q³ − q⁴ − ⋯ − q^{h+1})`, the generating function of the compositions into parts `{1, 3, 4, …, h + 1}`. Since `q·P_h(q) = q³ + ⋯ + q^{h+1}`,

```
G_h(q)  =  (C_h(q) − 1) / q,                                                        (4)
```

so the tree skylines of height at most `h` and area `A` number the compositions of `A + 1` into parts `{1, 3, 4, …, h + 1}`, for every `h ≥ 2`. At `h = 2` the parts are `{1, 3}`, and Narayana's cows `A000930` count these compositions.

**The bijection.** Put a column of height 1 in front of the skyline. Then read left to right: a column of height 1 followed by a column of height `j ≥ 2` becomes one part `1 + j`, and every other column of height 1 becomes a part 1. The parts are in `{1, 3, …, h + 1}` and add up to `A + 1`. Conversely, a part `k ≥ 3` expands to the columns `(1, k − 1)` and a part 1 to the column `(1)`, and the leading column is dropped. The map is a bijection for `h ≤ 6` and `A ≤ 10` (checked).[^4] The smallest cases:

| skyline | area | with the leading column | composition | of |
|---|---|---|---|---|
| `(1)` | 1 | `(1, 1)` | `(1, 1)` | 2 |
| `(1, 1)` | 2 | `(1, 1, 1)` | `(1, 1, 1)` | 3 |
| `(2)` | 2 | `(1, 2)` | `(3)` | 3 |
| `(1, 1, 1)` | 3 | `(1, 1, 1, 1)` | `(1, 1, 1, 1)` | 4 |
| `(1, 2)` | 3 | `(1, 1, 2)` | `(1, 3)` | 4 |
| `(2, 1)` | 3 | `(1, 2, 1)` | `(3, 1)` | 4 |
| `(3)` | 3 | `(1, 3)` | `(4)` | 4 |

**Bit strings.** Replacing each column of height 1 by a `0` and each column of height `j ≥ 2` by a run of `j` ones maps the tree skylines of area `n` and height at most `h` one-to-one onto the binary strings of length `n` in which every run of 1s has length between 2 and `h`. A tree skyline has no two neighboring columns of height at least 2, so the runs of ones it produces are separated by zeros, and the inverse reads each maximal run back as one column. Finch calls the strings with no run of length 1 **multus** bitstrings; the comments on A000570, A079816, A189593 and A189600 count the multus bitstrings of length `n` with no run of `h + 1` ones as `a(n + 1)`, which is the row `h = 4, 5, 6, 7` of Table 1.[^5] With the height unrestricted, the multus bitstrings of length `n` number `A005251(n + 2)`. The bijection is checked for `h ∈ {2, 3, 4, 5}` and with the height unrestricted, for `n ≤ 13`.[^4]

**Permutations.** A079816, A189593 and A189600 count permutations with restricted displacements. A permutation `p` of `{1, …, n}` with `p(i) − i ∈ {−h, …, −2, 0, 1}` splits into fixed points and cycles `i → i + 1 → ⋯ → j → i` with `j − i ∈ {2, …, h}`: a displacement `+1` moves one step right, and the only way back is one jump of `−(j − i)`, which is at least 2 since `−1` is excluded. So these permutations correspond to the compositions of `n` into parts `{1, 3, …, h + 1}`, the lengths of the cycles. This argument is the page's own; it is the case `h = 6` of Table 1 for A189593, whose recurrence `a(n) = a(n−1) + a(n−3) + ⋯ + a(n−7)` the OEIS lists as empirical, and the case `h = 7` for A189600, whose recurrence the OEIS records as proved by Robert Israel. A079816 is defined by the displacements `{−1, 0, 2, 3, 4, 5}`, the inverses of the case `h = 5`.[^5]

## Height unrestricted: A005251

With `P_∞(q) = q²/(1 − q)`, Equation (3) becomes

```
G_∞(q)  =  (1 + q²/(1 − q)) / (1 − q − q³/(1 − q))  =  (1 − q + q²) / (1 − 2q + q² − q³),
```

and the tree castles of area `A` number `A005251(A + 2)`. The reversed denominator `x³ − 2x² + x − 1` has the root `ψ²`, where `ψ` is the plastic number, the real root of `ψ³ = ψ + 1` ([[plastic-number](pages/plastic-number.md)]); in the variable `μ`, it is the factor `H_3(μ)` of [[tower-parity-sectors](pages/tower-parity-sectors.md)].

A005251 has two other castle readings. The even sector of the signed tower count at `k = 6` is `P_even(6, L) = 2^L·A005251(L + 3)` ([[tower-parity-sectors](pages/tower-parity-sectors.md)], [[hardin-word-identity](pages/hardin-word-identity.md)]), and the binary strings of length `L + 1` with no isolated 1 also number `A005251(L + 3)` (the bit-string bijection of the section *Compositions*, with the height unrestricted). And [[a005251-bijection](pages/a005251-bijection.md)] maps the tree skylines of area `A` to the binary strings of length `A − 1` with no factor `010`: the skyline `(c_1, …, c_w)` goes to `0^{c_1 − 1} 1 0^{c_2 − 1} 1 ⋯ 1 0^{c_w − 1}`, in which a column of height at least 2 is a nonempty run of zeros, so two neighboring such columns are exactly a factor `010`. This map is checked onto the strings avoiding `010` for `A ≤ 12`.[^4]

[[tower-spacing-castles](pages/tower-spacing-castles.md)] gives the castles of height 2 and minimum tower spacing 2, also counted by A005251.

## Tournaments at height 4

A **tournament** on `n` vertices has exactly one directed edge between any two distinct vertices; its **score vector** lists the out-degrees. A tournament is **unique** if every tournament with the same score vector is isomorphic to it, and **strong** if every vertex can reach every other along directed edges. A000570 counts the unique tournaments on `n` vertices.[^6] On 3 vertices both tournaments are unique: the transitive one, with score vector `(0, 1, 2)`, which is not strong, and the 3-cycle, `(1, 1, 1)`, which is.

**Theorem (Tetali 1998, Theorem 1).** There are exactly four strong unique tournaments, on 1, 3, 4 and 5 vertices, with score vectors `(0)`, `(1, 1, 1)`, `(1, 1, 2, 2)` and `(2, 2, 2, 2, 2)`; the strong components of every other unique tournament are among these four.[^7]

The proof combines two theorems of Muller et al., as Tetali paraphrases them: a score vector of a strong tournament on `n ≠ 4` vertices is also the score vector of a simple tournament ([[simple-tournament](pages/simple-tournament.md)]), so a strong unique tournament on `n ≠ 4` vertices has a forcibly simple score vector ([[forcibly-simple-score-vector](pages/forcibly-simple-score-vector.md)]), and the forcibly simple score vectors are `(0)`, `(0, 1)`, `(1, 1, 1)`, `(2, 2, 2, 2, 2)` and `(3, 3, 3, 3, 3, 3, 3)`. The vector `(0, 1)` is not strong, and `(3, 3, 3, 3, 3, 3, 3)` has three non-isomorphic strong realizers; the strong tournament on 4 vertices, `(1, 1, 2, 2)`, is added by inspection.[^8]

The strong components of a tournament are totally ordered, so a unique tournament on `n` vertices is a sequence of the four basic tournaments with sizes adding up to `n`, and Tetali derives the recurrence `u_n = u_{n−1} + u_{n−3} + u_{n−4} + u_{n−5}` for `n > 5` with `u_1, …, u_5 = 1, 1, 2, 4, 7`, and `u_n ~ c·α^n` with `c ≈ 0.48`, `α ≈ 1.685`.[^7] Khovanova states the same decomposition as a one-to-one correspondence between unique tournaments and concatenations of the strings `0`, `001`, `0011`, `00101`, of lengths 1, 3, 4, 5.[^9] With the bijection of the section *Compositions*:

**Proposition.** For every `n ≥ 1`, the unique tournaments on `n` vertices, the compositions of `n` into parts `{1, 3, 4, 5}` and the tree skylines of height at most 4 and area `n − 1` are equinumerous, `A000570(n)` of each, with explicit bijections through the compositions.

*Proof.* Sending a unique tournament to the sizes of its strong components, in their order, is injective by Tetali's Theorem 1, since each size in `{1, 3, 4, 5}` has one basic tournament; Tetali's recurrence is the recurrence of the compositions of `n` into `{1, 3, 4, 5}`, with the same initial terms, so the map is onto. The castle side is the bijection of the section *Compositions* at `h = 4`. The OEIS generating function of A000570, `(1 + x² + x³ + x⁴)/(1 − x − x³ − x⁴ − x⁵)`, is `G_4(x)` of Equation (3).[^6]

| size | strong tournaments (A051337) | strong unique tournaments | score vector |
|---|---|---|---|
| 1 | 1 | 1 | `(0)` |
| 2 | 0 | 0 | |
| 3 | 1 | 1 | `(1, 1, 1)` |
| 4 | 1 | 1 | `(1, 1, 2, 2)` |
| 5 | 6 | 1 | `(2, 2, 2, 2, 2)` |
| 6 | 35 | 0 | |
| 7 | 353 | 0 | |
| 8 | 6008 | 0 | |

The column of strong unique tournaments, the unique tournaments `1, 1, 2, 4, 7, 11, 18, 31` for `n ≤ 8` and the score vectors `1, 1, 2, 4, 9, 22, 59, 167` (A000571) agree with an enumeration of all tournaments on at most 8 vertices.[^10]

## Snippets

```python
import sympy as sp
x, q = sp.symbols('x q')

def P_h(h):
    return sum(q**i for i in range(2, h+1)) if h >= 2 else sp.Integer(0)

def tree_area_gf(h, W):
    """T_h(w, q) for w = 0..W, from Equation (1)."""
    T = sp.series((1 + P_h(h)*x) / (1 - q*x - q*P_h(h)*x**2), x, 0, W+1).removeO()
    return [sp.expand(T.coeff(x, w)) for w in range(W+1)]

def tree_area_by_area(h, A_max):
    """Coefficient of q^A in G_h(q): tree skylines of height <= h and area A, any width."""
    Ph = P_h(h)
    S = sp.series((1 + Ph) / (1 - q - q*Ph), q, 0, A_max+1).removeO()
    return [int(S.coeff(q, A)) for A in range(A_max+1)]
```

```
>>> tree_area_gf(2, 4)
[1, q**2 + q, 2*q**3 + q**2, q**5 + 3*q**4 + q**3, 3*q**6 + 4*q**5 + q**4]
>>> tree_area_by_area(2, 15)              # A000930(A + 1), Narayana's cows
[1, 1, 2, 3, 4, 6, 9, 13, 19, 28, 41, 60, 88, 129, 189, 277]
>>> tree_area_by_area(3, 15)              # A006498(A + 1)
[1, 1, 2, 4, 6, 9, 15, 25, 40, 64, 104, 169, 273, 441, 714, 1156]
```

```python
def castle_to_composition(c):
    aug = [1] + list(c); parts = []; i = 0
    while i < len(aug):
        if i + 1 < len(aug) and aug[i] == 1 and aug[i + 1] >= 2:
            parts.append(1 + aug[i + 1]); i += 2
        else:
            parts.append(aug[i]); i += 1
    return tuple(parts)

def composition_to_castle(parts):
    aug = []
    for p in parts:
        if p == 1: aug.append(1)
        elif p >= 3: aug.extend([1, p - 1])
        else: raise ValueError(f"unexpected part {p}")
    return tuple(aug[1:])
```

```
>>> castle_to_composition((2, 1))
(3, 1)
>>> composition_to_castle((3, 1))
(2, 1)
>>> castle_to_composition((1, 2, 1))
(1, 3, 1)
```

The functions are also filed on [[castle-snippets-strips](pages/castle-snippets-strips.md)].

## Appearances in Sources

- [[tetali-1998-unique-tournaments](pages/tetali-1998-unique-tournaments.md)] - Theorem 1, the four strong unique tournaments, its proof from two theorems of Muller et al., and the recurrence for A000570.

## Related Concepts

- [[castle-graph](pages/castle-graph.md)] - tree castles and tree skylines, and their counts by width.
- [[q-fibonacci-castle](pages/q-fibonacci-castle.md)] - the tree castles of height 2, the Fibonacci castles, counted with `q` marking area: `q^w (f_w(q) − 1)` at width `w`.
- [[fibonacci-castle](pages/fibonacci-castle.md)] - the tree castles of height 2 by width, `F_{w+2} − 1`.
- [[plastic-number](pages/plastic-number.md)] - `ψ`, and the growth `ψ²` of the tree castles of any height by area.
- [[tower-parity-sectors](pages/tower-parity-sectors.md)] and [[hardin-word-identity](pages/hardin-word-identity.md)] - `P_even(6, L) = 2^L·A005251(L + 3)`.
- [[a005251-bijection](pages/a005251-bijection.md)] - the tree skylines of area `A` and the binary strings of length `A − 1` with no factor `010`.
- [[tower-spacing-castles](pages/tower-spacing-castles.md)] - castles of height 2 with minimum tower spacing 2, counted by A005251.
- [[castle-classification-growth](pages/castle-classification-growth.md)] - families of castles by growth, with the tree castles by area.
- [[metallic-means](pages/metallic-means.md)] - the quadratic constants `σ_p^q`, of which `φ` at `h = 3` is the only one in Table 1.
- [[castle-by-area](pages/castle-by-area.md)] - convex, valley and other castles counted by area.
- [[unique-tournament](pages/unique-tournament.md)], [[simple-tournament](pages/simple-tournament.md)], [[forcibly-simple-score-vector](pages/forcibly-simple-score-vector.md)] - the tournament properties in Tetali's theorem.
- [[sandpile-group](pages/sandpile-group.md)] and [[sandpile-census](pages/sandpile-census.md)] - tree castles are the castles with a trivial sandpile group; the census counts the 5,842 tree castles of area 16 as 2,964 up to mirror image.
- [[castle-snippets-strips](pages/castle-snippets-strips.md)] - `tree_area_gf`, `tree_area_by_area`, `castle_to_composition`, `composition_to_castle`.
- [[oeis-index](pages/oeis-index.md)] - the pages citing A000930, A006498, A000570 and A005251.

## Footnotes

[^1]: Verified by execution (Python 3.11 with SymPy, 2026-10-16): the coefficients of Equation (1) against `Σ q^{area}` over all tree skylines of width `w ≤ 7` for `h ∈ {2, 3, 4, 5}`, and Equation (2) for `w ≤ 7`.
[^2]: Verified by execution (Python 3.11, 2026-10-16): the number of tree castles of height 2, width `w` and `t` columns of height 2 equals `C(w − t + 1, t)` for `w ≤ 11`; row sums against https://oeis.org/A000071.
[^3]: Verified by execution (Python 3.11 with SymPy, 2026-10-16): Table 1 by enumeration of tree skylines for `h ∈ {2, 3, 4}`, `A ≤ 10`, and every row from the coefficients of Equation (3) for `A ≤ 14`; Table 2 as differences of rows; the reversed denominators factored over the rationals and their roots of largest modulus; `A006498(2n) = F_{n+1}²` for `n ≤ 9` and `A006498(2n − 1) = F_{n+1}F_n` for `n ≤ 9`. Every listed term of A000930, A006498, A000570, A079816, A189593, A189600, A005251 and A077868 matches the counts at its shift. OEIS data read 2026-10-16: https://oeis.org/A000930 ("Narayana's cows sequence", offset 0), https://oeis.org/A077868 (offset 0), https://oeis.org/A006498 (offset 0), https://oeis.org/A000570 (offset 1), https://oeis.org/A079816 (offset 0), https://oeis.org/A189593 (offset 1), https://oeis.org/A189600 (offset 1), https://oeis.org/A005251 (offset 0).
[^4]: Verified by execution (Python 3.11, 2026-10-16): `castle_to_composition` maps the tree skylines of height at most `h` and area `A` onto the compositions of `A + 1` into `{1, 3, …, h + 1}`, and `composition_to_castle` inverts it, for `2 ≤ h ≤ 6` and `A ≤ 10`; the bit-string map onto the strings with all runs of ones of length 2 to `h` for `h ∈ {2, 3, 4, 5}` and unrestricted, `n ≤ 13`; the map to binary strings of length `A − 1` avoiding `010` for `A ≤ 12`; the snippet outputs.
[^5]: https://oeis.org/A000570, https://oeis.org/A079816, https://oeis.org/A189593, https://oeis.org/A189600 (read 2026-10-16) - Steven Finch's comments "a(n+1) is the number of multus bitstrings of length n with no runs of 5 ones" (A000570; 6, 7 and 8 ones on the others); A079816 "Number of permutations satisfying -k <= p(i)-i <= r and p(i)-i not in I, i=1..n, with k=1, r=5, I={1}"; A189593 "Number of permutations of 1..n with displacements restricted to {-6,-5,-4,-3,-2,0,1}" with "Empirical: a(n) = a(n-1) +a(n-3) +a(n-4) +a(n-5) +a(n-6) +a(n-7)"; A189600 with "Empirical recurrence verified (see link). - Robert Israel, Jan 27 2019".
[^6]: https://oeis.org/A000570 (read 2026-10-16) - "Number of tournaments on n nodes determined by their score vectors", "G.f.: (1+x^2+x^3+x^4)/(1-x-x^3-x^4-x^5). - Harvey P. Dale, May 05 2011".
[^7]: [[tetali-1998-unique-tournaments](pages/tetali-1998-unique-tournaments.md)] p.157 L39-41 - "Theorem 1. There are exactly four (basic) strong tournaments in Unique (see Fig. 1); any other (nonstrong) tournament in Unique can be decomposed into strong components, each of which is one of the four basic tournaments."; p.157 L30-34 and p.159 L111-115 [synthesis] - the values `u_1, …, u_5 = 1, 1, 2, 4, 7`, the recurrence `u_n = u_{n−1} + u_{n−3} + u_{n−4} + u_{n−5}` for `n > 5`, and `u_n ~ c·α^n` with `c ≈ 0.48`, `α ≈ 1.685` (the OCR text garbles the formulas).
[^8]: [[tetali-1998-unique-tournaments](pages/tetali-1998-unique-tournaments.md)] p.158-159 L72-110 [synthesis] - Theorem 2 and Theorem 3 of Muller et al. as paraphrased by Tetali, the five forcibly simple score vectors, the exclusion of `(0, 1)` and of `(3, 3, 3, 3, 3, 3, 3)` ("three nonisomorphic strong tournaments"), and "the unique strong tournament on four vertices with the score vector (1, 1, 2, 2)".
[^9]: https://arxiv.org/abs/0712.1621 (read 2026-09-28) - Tanya Khovanova, "Unique Tournaments and Radar Tracking" (2007), §5: "Any initial-loss non-tracking binary string is a concatenation of strings of 4 basic types: 0, 001, 0011, 00101" and "we established a one-to-one correspondence between unique tournaments and initial-loss non-tracking binary strings."
[^10]: Verified by execution (Python 3.11 with NumPy, 2026-10-16): all `2^{C(n,2)}` labeled tournaments on `n ≤ 8` vertices grouped by score vector; a score vector is unique when the permutations within its classes of equal scores carry one realizer onto all of them; strong connectivity by reachability in both directions. Score vectors `1, 1, 2, 4, 9, 22, 59, 167` (https://oeis.org/A000571), unique `1, 1, 2, 4, 7, 11, 18, 31` (A000570), strong unique only at `n = 1, 3, 4, 5`, with the four score vectors of Tetali's theorem. The strong tournaments column is https://oeis.org/A051337 (read 2026-10-16).
