---
title: The castle row-raising equation - castles by area and width through z -> qz
category: Analyses
summary: "A prime castle is a castle raised one row, so the free gluing monoid of prime castles gives a q-shift functional equation for castles by area q and width z. Unsigned it is 1 + qz B(z) = 1/(1 - qz B(qz)); with the block sign it is 1 + qz(2 - E(z)) = 1/(1 - qz E(qz)), which determines E one area at a time and computes the signed count even(n) - odd(n) of castles by area to n = 300. The signed count is C(-rho)^n up to a relative error O(0.7508^n), with rho = 1.62382967400459366939460437600... and C = 0.0985091749731156224089366266361..., from the simple zero q_0 = -1/rho of the q-Bessel denominator of castle-q-bessel-closed-form. Marking peaks gives a rational generating function whose one-peak column is A001924(n - 1); the convex case is U(q) = K(q, q)."
tags: [analysis, castle, area, width, prime-castle, monoid, functional-equation, q-shift, q-series, parity, sign, peaks, asymptotics, residue, oeis]
sources: [oeis-mining-pe502, prellberg-brak-1995-cluster-models]
created: 2026-09-22
updated: 2026-10-23
---

# The castle row-raising equation

[[prime-castles](pages/prime-castles.md)] glues castles at a shared height-1 column. The result is a free monoid `𝓜`: its elements are the castles that begin and end with a height-1 column, the padded castles `(1, C, 1)` together with the identity `(1)`, and its primes are `(1, X, 1)` with `X` a castle having no height-1 column, together with the trivial prime `(1, 1)`. A nonempty `X` with no height-1 column is a castle `Y` with a full row slid under it, `X = (y_1 + 1, …, y_w + 1)`. So the primes are the castles again, raised one row, and freeness turns that into a functional equation. This page writes the equation with the width tracked, which makes it a `z → qz` recursion, and gives three specializations: unsigned, signed, and by peaks.

## The equation

Grade `𝓜` by reduced area `area − 1` (variable `q`) and reduced width `width − 1` (variable `z`), both additive under gluing. Raising `Y` one row keeps its width and adds `width(Y)` cells, so it is the substitution `z → qz`. With `B(q, z)` the castle generating function by area and width, the empty castle included ([[castle-notation](pages/castle-notation.md)]), and `π(q, z)` the generating function of the primes (written `π` because `P` is the signed tower count):

```
primes:    π(q, z)  =  qz · B(q, qz)          (the empty castle raised is (1, 1), weight qz)
padded:    𝓜        =  1 + qz · B(q, z)       (the identity (1), then (1, C, 1) for every castle C)
freeness:  𝓜        =  1 / (1 − π)

           1 + qz B(z)  =  1 / (1 − qz B(qz))                                     (1)
```

Unsigned, Equation (1) holds for the known `B(q, z) = (1 − q)/(1 − q − qz)`, the compositions by number of parts, and adds nothing. It carries information once a character of `𝓜`, a homomorphism to the nonzero numbers, weights the primes. [[signed-prime-castles](pages/signed-prime-castles.md)] shows that any statistic additive over the prime factors gives one, and the block count minus one is such a statistic.

## The signed equation

Let `E(q, z) = Σ (−1)^{blocks(C)} q^{area(C)} z^{width(C)}`, the empty castle included with weight `+1`. Gluing loses one block, so the sign character of `𝓜` is `χ = (−1)^{blocks − 1} = −(−1)^{blocks}` ([[signed-prime-castles](pages/signed-prime-castles.md)]). Raising adds one block, so a prime `(1, X, 1)` with `X` raised from `Y` carries `(−1)^{blocks(Y)}`, while a padded `(1, C, 1)` carries `−(−1)^{blocks(C)}`. The trivial prime `(1, 1)` carries `+1` either way. That gives

```
1 + qz (2 − E(z))  =  1 / (1 − qz E(qz))                                          (2)
```

The `2` comes from the empty castle, which is counted `+1` inside `E` but enters `𝓜` as `(1, 1)` with sign `+1` instead of `−1`. This is the signed identity of [[signed-prime-castles](pages/signed-prime-castles.md)], with the width kept. With `1` in place of `2` the identity fails.[^1]

**A recursion.** The right side of Equation (2) at area `n + 1` involves `E(qz)` only through area `n − 1`, because the factor `qz` and the shift each add area. So reading off the coefficient of `q^{n+1}` gives `−z E_n(z)`, the signed castles of area `n` by width, from lower terms, one area at a time. Write `even(n)` and `odd(n)` for the numbers of castles of area `n` with an even and with an odd number of blocks, as on [[castle-by-area](pages/castle-by-area.md)]. The recursion gives `even(n) − odd(n)` for `n ≤ 300`, and an independent column dynamic program over (area, last column height) gives the same value at every `n ≤ 300`:[^1]

```
even(n) − odd(n), n = 1..40:
−1, 0, 0, 2, 0, 2, −4, 2, −12, 10, −20, 38, −44, 98, −136, 230, −388, 582, −1008, 1590,
−2592, 4262, −6800, 11170, −18064, 29286, −47780, 77258, −125736, 204050, −331084,
538338, −873300, 1418778, −2303708, 3739942, −6074756, 9862434, −16016304, 26008230
```

For `n ≤ 12` these are the differences of the `even` and `odd` rows of [[castle-by-area](pages/castle-by-area.md)].

## The signed growth constant

At `z = 1` the right side of Equation (2) has a pole where `g(q) = q E(q, q) = 1`. `E(q, q)` is the signed generating function of the raised castles, with weight `q^{area + width}`. Its coefficients grow like `1.4574^n`, so it converges for `|q| < 0.686`, past the pole, and the pole is the dominant singularity of `E(q, 1)`.[^2] Near a simple zero `q_0` of `1 − g(q)`,

```
even(n) − odd(n)  ~  C · q_0^{−n},        C = −1 / (q_0² g′(q_0))

q_0  =  −0.615828135184805773627625720697...
ρ    =  −1/q_0  =  1.623829674004593669394604376006...
C    =  0.098509174973115622408936626636...
```

At `n = 16`, `C ρ^16 = 230.2` against `230`.

**Closed form.** The tower grammar graded by area and blocks gives `E(q, 1) = N(q)/M(q)` with explicit q-series `N` and `M` at block weight `−1`, built from the parallelogram series `J_0`, `J_1` ([[castle-q-bessel-closed-form](pages/castle-q-bessel-closed-form.md)]). `M` is analytic in `|q| < 1`, so the signed generating function is meromorphic there, and `q_0` is the first zero of `M`. The digits of `q_0`, `ρ` and `C` in this section come from the zero `q_0` of `M`, and `C = −N(q_0)/(q_0 M′(q_0))` is the residue. The second zero of `M` is `q_1 = −0.8202719776`, so the relative error of `C(−ρ)^n` is `O(|q_0/q_1|^n) = O(0.7508^n)`, about `4.5 × 10^{−38}` at `n = 300`; the ratio of consecutive terms at `n = 299, 300` agrees with `−ρ` in its first 38 significant digits.[^2]

**A Prellberg-Brak equation.** Clearing the denominator, Equation (1) reads `B(z)B(qz) − B(z)/(qz) + B(qz)/(qz) = 0` and Equation (2) reads `E(z)E(qz) − E(z)/(qz) − (2 + 1/(qz)) E(qz) + 2/(qz) = 0`. Both have the shape `G(x)G(qx) + a(x)G(x) + b(x)G(qx) + c(x) = 0`, which [[prellberg-brak-1995-cluster-models](pages/prellberg-brak-1995-cluster-models.md)] linearize with `G(x) = α H(qx)/H(x) − b(x)` into a three-term linear q-difference equation for `H`.[^3] Their bar-graph equation (3.11) is a second castle equation of this shape, with `x` marking width, `y` blocks and `q` area. Its series counts the castles by width, blocks and area, and at `y = −1`, with `E = 1 + B(z, −1, q)`, it satisfies Equation (2) through area 9.[^4]

**Sign and growth.** Unsigned, the castles of area `n` number `2^{n−1}`; the signed count grows like `ρ^n`, `ρ = 1.6238`. By semi-perimeter the sign halves the exponent, `τ² → τ` ([[castle-perimeter](pages/castle-perimeter.md)]). By area it does not: halving would give `√2 = 1.414`, below `ρ`. The parity is still a lower-order correction: `even(n)/odd(n) = 1 + O((ρ/2)^n)`.

## Peaks: a rational specialization

The peaks of a castle, its maximal runs of columns of height at least 2 ([[castle-foata-transform](pages/castle-foata-transform.md)]), are its nontrivial prime factors ([[prime-castles](pages/prime-castles.md)]). At `z = 1`, `B(q, q) − 1 = q²/(1 − q − q²)` is rational. Marking each nontrivial prime by `t` in Equation (1) gives

```
1 + q G(q, t)  =  1 / (1 − q − t q³/(1 − q − q²))

G(q, t)  =  (1 − q − q² + t q²) / (1 − 2q + q³ − t q³)                              (3)
```

`G` counts castles by area and peaks, with the empty castle as its constant term; at `t = 1` it is `(1 − q)/(1 − 2q)`. Its rows from area 1 are `1; 1 1; 1 3; 1 7; 1 14 1; 1 26 5; 1 46 17; 1 79 47 1; 1 133 115 7; …`, the coefficient of `t^k` counting the castles with `k` peaks, and they agree with enumeration through area 13.[^5] The one-peak column `1, 3, 7, 14, 26, 46, 79, 133, 221, …` is `A001924(n − 1)`, "Apply partial sum operator twice to Fibonacci numbers". A one-peak castle is `(1^a, X, 1^b)` with `a, b ≥ 0` and `X` a nonempty castle with no height-1 column. Such `X` are the compositions into parts `≥ 2`, `F_{m−1}` of area `m`, and the two runs of height-1 columns contribute the factor `(1 − q)^{−2}`, so the one-peak castles have generating function `q²/((1 − q − q²)(1 − q)²)`, the twice-summed Fibonacci numbers.[^5] The two-peak column is `1, 5, 17, 47, 115, 259, 550, 1118, …`.

The one-peak castles have the shape of the convex castles, with the unimodality of `X` dropped. The convex version of the row-raising substitution is `U(q) = K(q, q)`, the prime convex castles of [[prime-convex-castles](pages/prime-convex-castles.md)], where `K(q, z)` is the convex castle generating function by area and width.

Signed and by peaks together, the prime weight is `qz (1 + t (E(q, qz) − 1))`, and the generating function of `𝓜` by reduced area, reduced width, peaks and the sign character is `1/(1 − qz (1 + t(E(q, qz) − 1)))`, with the same recursion. It agrees with enumeration as a series in `q`, `z` and `t` through reduced area 10.[^5]

## Computation

The recursion of Equation (2) to area 300:

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

```
[-1, 0, 0, 2, 0, 2, -4, 2, -12, 10, -20, 38, -44, 98, -136, 230] -1.6238296740045937
```

## Relation to other pages

- [[prime-castles](pages/prime-castles.md)] - the gluing monoid, the prime generating function `π(q) = q B(q, q)`, and the primes as raised castles.
- [[signed-prime-castles](pages/signed-prime-castles.md)] - the sign and the peaks as characters of the monoid.
- [[castle-q-bessel-closed-form](pages/castle-q-bessel-closed-form.md)] - `E(q, 1) = N(q)/M(q)`, the zeros `q_0`, `q_1`, and the residue `C`.
- [[prime-convex-castles](pages/prime-convex-castles.md)] - `U = K(q, q)`, the convex case.
- [[castle-by-area](pages/castle-by-area.md)] - the `even` and `odd` rows to area 12, extended here to area 300.
- [[castle-perimeter](pages/castle-perimeter.md)] - castles by semi-perimeter, where the sign halves the exponent.
- [[castle-foata-transform](pages/castle-foata-transform.md)] - peaks.
- [[prellberg-brak-1995-cluster-models](pages/prellberg-brak-1995-cluster-models.md)] - the linearizable shape of Equations (1) and (2), and the bar-graph equation (3.11), the castle generating function by width, blocks and area.
- [[castle-sequence-catalogue](pages/castle-sequence-catalogue.md)] - the sequences and constants here.
- [[q-thread-seminar](pages/q-thread-seminar.md)] - a seminar on castles by area whose Stop 4 is this equation.

## Footnotes

[^1]: Verified by execution (Python 3.11 with SymPy, 2026-10-16): Equations (1) and (2) as bivariate series through area 11 against enumeration of all compositions, and Equation (2) with `1` in place of `2` fails; `B(q, z) = (1 − q)/(1 − q − qz)` to the same order; the recursion of the Computation section and a dynamic program over (area, last column height) with sign `(−1)^{Σ max(0, c_i − c_{i−1})}` give the same `even(n) − odd(n)` for `n ≤ 300`. The `n ≤ 12` values are the differences of raw/oeis-pe502/vein9-area.md §"Parity splits" L46-47 - "`even(n)` | 0, 1, 2, 5, 8, 17, 30, 65, 122, 261, 502, 1043 ... `odd(n)` | 1, 1, 2, 3, 8, 15, 34, 63, 134, 251, 522, 1005".
[^2]: Verified by execution (Python 3.11 with mpmath, 60 digits, 2026-10-16): the coefficients of `E(q, q)` from a dynamic program to weight 80, with ratio `1.45738` at weight 80; `q_0` and `q_1` by `findroot` on the series `M(q)` of [[castle-q-bessel-closed-form](pages/castle-q-bessel-closed-form.md)] truncated at `k = 200`, `ρ = −1/q_0`, and `C = −N(q_0)/(q_0 M′(q_0))`; `(q_0/q_1)^300 = 4.47 × 10^{−38}`; the ratio `t_300/t_299` agrees with `−ρ` in 38 significant digits, and `C ρ^16 = 230.21`.
[^3]: [[prellberg-brak-1995-cluster-models](pages/prellberg-brak-1995-cluster-models.md)] `prellberg-brak-1995-partially-directed-cluster-models.txt` §4 L673-682 - "the functional equations for bar-graph polygons, alternating bar-graph polygons, staircase polygons, and ZL walks can all be linearized, as they are of the form G(x) G(qx) + a(x) G(x) + b(x) G(qx) + c(x) = 0 (4.1) which can be linearized by use of the transformation G(x) = α H(qx)/H(x) - b(x) (4.2)". Checked by execution (SymPy, 2026-09-23): for both of Equations (1) and (2), substituting (4.2) and multiplying by `H(x)` gives their (4.3), `α² H(q²x) + α[a(x) − b(qx)] H(qx) + [c(x) − a(x) b(x)] H(x) = 0`, identically.
[^4]: [[prellberg-brak-1995-cluster-models](pages/prellberg-brak-1995-cluster-models.md)] `prellberg-brak-1995-partially-directed-cluster-models.txt` §3.1 L401-402, L473 - "bar-graph polygons, that is, column-convex polygons with a horizontal lower boundary"; "B(x,y,q)=B(qx, y, q) y + {1 + B(qx, y, q)} qx {y + B(x, y, q)} (3.11)". Verified by execution (SymPy, 2026-10-16): the castle generating function by width, blocks and area satisfies (3.11) through area 9, and `E = 1 + B(z, −1, q)` satisfies Equation (2) through area 9.
[^5]: Verified by execution (Python 3.11 with SymPy, 2026-10-16): the series of Equation (3) against castles of area `n ≤ 13` counted by peaks (maximal runs of columns of height `≥ 2`); the joint generating function of the signed and peak-marked monoid against enumeration of the padded castles through reduced area 10, with `t` symbolic. https://oeis.org/A001924 (read 2026-10-16) - "Apply partial sum operator twice to Fibonacci numbers", data `0, 1, 3, 7, 14, 26, 46, 79, 133, 221, 364, 596, 972, …` (offset 0).
