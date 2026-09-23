---
title: The castle row-raising equation - castles by area and width through z -> qz
category: Analyses
summary: "A prime castle is a castle raised one row, so the free gluing monoid of prime castles gives a q-shift functional equation for castles by area q and width z. Unsigned it is 1 + qz B(z) = 1/(1 - qz B(qz)). With the block sign it is 1 + qz(2 - E(z)) = 1/(1 - qz E(qz)), and it determines E order by order, which computes the signed count of castles by area to 300 in seconds (checked against a column DP). The signed count even(n) - odd(n) grows like C·(-rho)^n with rho = 1.62382967400459366939... and C = 0.09850917497311562240..., a simple pole where q E(q,q) = 1; none of the constants or the sequence is in OEIS. Marking peaks gives a rational GF whose one-peak column is A001924 (interlink); the convex case is U = K(q,q)."
tags: [analysis, castle, area, width, prime-castle, monoid, functional-equation, q-shift, q-series, parity, sign, peaks, asymptotics, residue, oeis, interlink, novel-candidate]
sources: [oeis-mining-pe502]
created: 2026-09-22
updated: 2026-09-23
---

# The castle row-raising equation

[[prime-castles](pages/prime-castles.md)] glues castles at a shared height-1 column. The result is a free monoid `M`: its elements are the padded castles `(1, C, 1)`, and its primes are `(1, X, 1)` with `X` a castle having no height-1 column. Such an `X` is a castle `Y` with a full row slid under it: `X = (y_1 + 1, ..., y_w + 1)`. So the primes are the castles again, raised one row, and freeness turns that into a functional equation. This page writes the equation with width tracked. That makes it a genuine `z → qz` recursion rather than a one-variable identity. It then reads off the three specializations: unsigned, signed, and by peaks.

## The equation

Grade `M` by reduced area `area - 1` (variable `q`) and reduced width `width - 1` (variable `z`), both additive under gluing. Raising `Y` one row keeps its width and adds `width(Y)` to its area, so it is the substitution `z → qz`. With `B(q, z)` the castle GF by area and width, including the empty castle:

```
primes:    P = qz · B(q, qz)               ((1,1) is the empty castle raised, weight qz)
padded:    M = 1 + qz · B(q, z)            (the identity (1), then (1, C, 1) for every castle C)
freeness:  M = 1/(1 - P)

           1 + qz B(z)  =  1 / (1 - qz B(qz))
```

Unsigned, this is a true identity with no content: `B = 1 + qz/(1 - q - qz)`, the compositions by parts. It becomes useful once a character of `M` rides along. [[signed-klarner-decomposition](pages/signed-klarner-decomposition.md)] shows that any statistic additive over prime factors does, and the block sign is one.

## The signed equation

Let `E(q, z) = sum (-1)^blocks(C) q^area(C) z^width(C)`, including the empty castle with weight `+1`. Raising adds one block. In `M` the sign character is `(-1)^(blocks - 1)`, so a prime `(1, X, 1)` with `X` raised from `Y` carries `(-1)^blocks(Y)`, while a padded `(1, C, 1)` carries `-(-1)^blocks(C)`. The trivial prime `(1, 1)` carries `+1` either way. That gives

```
1 + qz (2 - E(z))  =  1 / (1 - qz E(qz))
```

The `2` is the empty castle, which is counted `+1` inside `E` but enters `M` as `(1, 1)` with sign `+1` instead of `-1`. This is the same identity as `1/(1 - P_s)` on [[signed-klarner-decomposition](pages/signed-klarner-decomposition.md)], now with width.

**It is a recursion.** The right side at area `n + 1` involves `E(qz)` only through areas `≤ n - 1`, because `qz` and the shift each add area. So reading off `[q^(n+1)]` gives `-z E_n(z)` from lower terms, one area at a time, with no enumeration. The computation below reaches area 300 in about 15 seconds. An independent column DP (block count = total ascent, one pass per area) gives the same `even(n) - odd(n)` at every `n ≤ 300`, and brute-force enumeration gives the same width polynomials through area 12. At `n ≤ 12` the values agree with the `even`/`odd` table on [[castle-by-area](pages/castle-by-area.md)].[^1]

```
even(n) - odd(n), n = 1..40:
-1, 0, 0, 2, 0, 2, -4, 2, -12, 10, -20, 38, -44, 98, -136, 230, -388, 582, -1008, 1590,
-2592, 4262, -6800, 11170, -18064, 29286, -47780, 77258, -125736, 204050, -331084,
538338, -873300, 1418778, -2303708, 3739942, -6074756, 9862434, -16016304, 26008230
```

The sequence has no OEIS match, as signed terms or absolute values, so it is a novel-candidate.[^2]

## The signed growth constant

At `z = 1` the right side has a pole where `q E(q, q) = 1`. `E(q, q)` is the signed GF of the raised castles, with weight `q^(area + width)`. Its coefficients grow only like `1.45^n`, so it converges past the pole, and the pole is the dominant singularity of `E(q, 1)`. Near a simple zero `q_0` of `1 - q E(q, q)`,

```
even(n) - odd(n)  ~  C · q_0^(-n),     C = -1 / (q_0^2 g'(q_0)),   g(q) = q E(q, q)

q_0  = -0.61582813518480577362...
rho  = -1/q_0 = 1.62382967400459366939460437600637793850...
C    =  0.09850917497311562240893662663614881010...
```

The ratio `t_n / t_(n-1)` of successive terms converges to `-rho` fast. Consecutive ratios at `n = 299, 300` differ by `1.7 × 10^(-37)`, so the error term is exponentially smaller, which is consistent with a simple pole. The digits above come from those ratios. Solving `q E(q, q) = 1` directly, with `E(q, q)` truncated at `q^300`, gives `q_0` to 15 digits and `C` from the residue to 12, in agreement. The digits of `rho`, `1/rho` and `C` have no OEIS match. These are novel-candidate constants.[^2] Already at `n = 16`, `C rho^16 = 230.2` against the true `230`.

**Closed form.** The same signed series has a closed form, from the tower grammar graded by area and blocks on [[castle-q-bessel-closed-form](pages/castle-q-bessel-closed-form.md)]: `E(q, 1) = N(q)/M(q)` with `N`, `M` explicit q-Bessel series at block weight `-1`, built from the parallelogram series `J_0`, `J_1`. `M` is analytic in `|q| < 1`, so the signed GF is meromorphic there. `q_0` is the first zero of `M`, and it reproduces `rho` and `C` above to 30 digits. The second zero is `q_1 = -0.82027198`, so the relative error of `C(-rho)^n` is `O(0.7508^n)`, about `3 × 10^(-38)` at `n = 300`.

**What the sign does to the growth.** Unsigned castles by area grow like `2^n`, and the signed count like `1.6238^n`. By semi-perimeter, [[castle-perimeter](pages/castle-perimeter.md)] finds that the sign halves the exponent, `τ^2 → τ`. By area it does not: `sqrt(2) = 1.414` is well below `rho`. The signed dominant singularity is a pole of a q-series, not an algebraic branch point (own observation). The parity clause is still a lower-order correction, `even/odd = 1 + O((rho/2)^n)`.

## Peaks: a rational specialization

The peaks of [[castle-foata-transform](pages/castle-foata-transform.md)] are the nontrivial prime factors ([[prime-castles](pages/prime-castles.md)]). So marking each nontrivial prime by `t` in the unsigned equation, at `z = 1` where `B(q, q) - 1 = q^2/(1 - q - q^2)` is rational, gives

```
1 + q G(q, t)  =  1 / (1 - q - t q^3/(1 - q - q^2))

G(q, t)  =  (1 - q - q^2 + t q^2) / (1 - 2q + q^3 - t q^3)
```

`G` counts castles by area and peaks, including the empty castle as its constant term (at `t = 1` it is `(1 - q)/(1 - 2q)`). Its rows from area 1 are `1; 1 1; 1 3; 1 7; 1 14 1; 1 26 5; 1 46 17; 1 79 47 1; ...`. The rows match brute force through area 12. The triangle has no OEIS match, and neither does its two-peak column `1, 5, 17, 47, 115, 259, 550, 1118`.[^3] The one-peak column `1, 3, 7, 14, 26, 46, 79, 133, 221, ...` is A001924(n - 1), "Apply partial sum operator twice to Fibonacci numbers". That is forced: a one-peak castle is `(1^a, X, 1^b)` with `X` any castle free of height-1 columns, `F` placed in `(1 - q)^-2` ways. A001924's comments give subset and bit-string readings but no composition reading, so this is an **interlink**.[^3]

The one-peak castles have the same shape as the convex castles, with the unimodality of `X` dropped. The convex version of the row-raising substitution is `U(q) = K(q, q)`, the prime convex castles on [[prime-convex-castles](pages/prime-convex-castles.md)], where `K(q, z)` is the convex castle GF by area and width.

Signed and by peaks together, the prime weight is `qz (1 + t (E(q, qz) - 1))`. The joint GF of area, width, peaks and sign is `1/(1 - qz(1 + t(E(qz) - 1)))`, with the same order-by-order recursion. This is written out and checked only at `t = 1`.

## Computation

The signed recursion to area 300 (about 15 seconds):

```python
N = 300
def mul(a, b):                                  # polynomials in z
    r = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b): r[i + j] += x * y
    return r
def add(a, b):
    a, b = (a, b) if len(a) >= len(b) else (b, a)
    return [x + (b[i] if i < len(b) else 0) for i, x in enumerate(a)]
E, X, Y = [ [1] ], [ [0] ], [ [1] ]                 # E[n] = signed castles of area n, by width
for n in range(1, N + 1):
    while len(X) <= n + 1:                      # [q^m] of qz E(qz), needs E up to area m - 2
        m = len(X)
        X.append([0] + [E[m-1-w][w] if m-1-w < len(E) and w < len(E[m-1-w]) else 0 for w in range(m)])
    while len(Y) <= n + 1:                      # 1/(1 - qz E(qz))
        m = len(Y)
        acc = [0]
        for j in range(1, m + 1): acc = add(acc, mul(X[j], Y[m - j]))
        Y.append(acc)
    E.append([-c for c in Y[n + 1][1:]])        # -qz E(z) = [q^(n+1)] of the right side
t = [sum(e) for e in E]
print(t[1:17], t[300] / t[299])                 # even - odd; ratio -> -rho
```

## Open

- The signed prime convex series: the convex case of the signed equation, which would give `cev - cod` on [[castle-by-area](pages/castle-by-area.md)] in closed form.

## Relation to other pages

- [[prime-castles](pages/prime-castles.md)]: the monoid, and the primes as raised castles.
- [[signed-klarner-decomposition](pages/signed-klarner-decomposition.md)]: the sign and the peaks as characters, which is what lets them ride through the equation.
- [[prime-convex-castles](pages/prime-convex-castles.md)]: `U = K(q, q)`, the convex case.
- [[castle-by-area](pages/castle-by-area.md)]: the `even`/`odd` split extended here from area 18 to area 300.
- [[castle-perimeter](pages/castle-perimeter.md)]: the semi-perimeter version, where the sign halves the exponent.
- [[castle-foata-transform](pages/castle-foata-transform.md)]: peaks.
- [[castle-sequence-catalogue](pages/castle-sequence-catalogue.md)]: statuses for the sequences and constants here.

## Footnotes

[^1]: Computed by execution, 2026-09-22: the recursion above through area 300; an independent DP over (area, last column height) with sign `(-1)^(sum max(0, c_i - c_{i-1}))` through area 300, equal at every `n`; brute-force enumeration of compositions with signed width polynomials through area 12, equal. The table values reproduce raw/oeis-pe502/vein9-area.md §"Parity splits" L46-47 - "`even(n)` | 0, 1, 2, 5, 8, 17, 30, 65, 122, 261, 502, 1043 ... `odd(n)` | 1, 1, 2, 3, 8, 15, 34, 63, 134, 251, 522, 1005".
[^2]: OEIS searches (https://oeis.org/search, JSON format, 2026-09-22) returned no results for `1,-1,0,0,2,0,2,-4,2,-12,10,-20,38,-44,98,-136,230,-388` (with the leading empty-castle term), for its absolute values, or for the digit strings of `rho` (`1,6,2,3,8,2,9,6,7,4,0,0,4,5,9`), `1/rho` (`6,1,5,8,2,8,1,3,5,1,8,4,8,0,6`) and `C` (`9,8,5,0,9,1,7,4,9,7,3,1,3`). Constants computed by execution, 2026-09-22 (mpmath, 50 digits): the successive ratios `t_300/t_299` and `t_299/t_298`, `C = t_n/(-rho)^n` at `n = 298..300`, and `findroot` on `q E(q, q) = 1` with the series truncated at `q^300`.
[^3]: Computed by execution, 2026-09-22 (sympy series of `G`, and brute-force counts of maximal runs of parts `≥ 2` through area 12). https://oeis.org/A001924 (fetched 2026-09-22) - "Apply partial sum operator twice to Fibonacci numbers", data `0, 1, 3, 7, 14, 26, 46, 79, 133, 221, 364, 596, ...` (offset 0); its comments give rook-polynomial, subset, and bit-string readings. OEIS searches (JSON format, 2026-09-22) returned no results for the triangle by rows (`1,1,1,1,3,1,7,1,14,1,1,26,5,1,46,17,1,79,47,1`) or for `1,5,17,47,115,259,550,1118`.
