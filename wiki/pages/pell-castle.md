---
title: Pell castle
category: Concepts
summary: A Pell castle is a castle of height 3 whose first column has height 1 and whose neighboring columns differ in height by at most 1; height 3 is part of the definition. The Pell castles are the anchored 1-smooth strips on the heights {1, 2, 3} that reach height 3, so A_Pell(w) = P⋆_w − 2^{w−1} = 0, 0, 1, 4, 13, 38, 105, 280, … for w = 1, 2, 3, …, with generating function x³/((1 − 2x − x²)(1 − 2x)), and A_Pell(w) = A094706(w − 2) for w ≥ 2. They are silver by width (growth 1 + √2) and are the h = 3 case of the anchored 1-smooth castles, column 2 of A283595. Split by block parity, A^e_Pell = 0, 0, 0, 0, 2, 13, 51, 154, … and A^o_Pell = 0, 0, 1, 4, 11, 25, 54, 126, … satisfy a recurrence of order 8, and the signed count S_Pell = A^e_Pell − A^o_Pell one of order 5 with denominator (1 − x)(1 − 2x + 2x²)(1 − 2x + 3x²).
tags: [concept, castle, castle-type, pell, silver-ratio, transfer-matrix, 1-smooth, parity, oeis]
sources: [pe502-pell-castle-strip]
created: 2026-10-04
updated: 2026-10-16
---

# Pell castle

## Definition

A castle of height `h` is a skyline `(c_1, …, c_w)` with `1 ≤ c_i ≤ h` and some `c_i = h` ([[castle-polyomino](pages/castle-polyomino.md)]). A **Pell castle** of width `w` is a castle of height 3 whose first column has height 1 and whose neighboring columns differ in height by at most 1; height 3 is part of the definition:

```
c_1 = 1,      |c_{i+1} − c_i| ≤ 1  (1 ≤ i < w),      max_i c_i = 3.
```

- **Construction rule.** Start at height 1; at each step move up one, down one, or stay, never leaving `{1, 2, 3}`; and reach height 3 at least once.
- **Examples.** `(1, 2, 3, 2)` and `(1, 2, 2, 3, 3, 2, 1)` are Pell castles. The four Pell castles of width 4 are `(1, 1, 2, 3)`, `(1, 2, 2, 3)`, `(1, 2, 3, 2)`, `(1, 2, 3, 3)`.
- **Non-examples.** `(1, 2, 2, 1)` never reaches height 3; `(2, 3, 2)` starts at height 2; `(1, 3, 2)` rises by 2 in one step.

**From the Pell castle strip.** The Pell castle strip ([[pell-castle-strip](pages/pell-castle-strip.md)]) is the same rule without the ceiling requirement: the anchored 1-smooth skylines on heights `1, 2, 3`, which need not reach height 3. Strips need not reach their top height, so they need not be castles of height 3; the Pell castles are the Pell strips that reach height 3.

## Counting Pell castles

**The count.** The anchored 1-smooth strips of width `w` number the Pell numbers `P⋆_w` (`P⋆_1 = 1`, `P⋆_2 = 2`, `P⋆_{w} = 2P⋆_{w−1} + P⋆_{w−2}`; A000129), with width generating function `x/(1 − 2x − x²)` ([[pell-castle-strip](pages/pell-castle-strip.md)]). Those that never reach height 3 stay on `{1, 2}`, where every column after the first may be 1 or 2, so there are `2^{w−1}` of them. Hence

```
A_Pell(w)  =  P⋆_w − 2^{w−1},
Σ_w A_Pell(w) x^w  =  x/(1 − 2x − x²) − x/(1 − 2x)  =  x³ / ((1 − 2x − x²)(1 − 2x)).
```

`A_Pell(w)` is the number of Pell castles of width `w` ([[castle-notation](pages/castle-notation.md)]).

| `w` | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Pell strips `P⋆_w` | 1 | 2 | 5 | 12 | 29 | 70 | 169 | 408 | 985 | 2378 | 5741 | 13860 |
| never reaching 3, `2^{w−1}` | 1 | 2 | 4 | 8 | 16 | 32 | 64 | 128 | 256 | 512 | 1024 | 2048 |
| **Pell castles** `A_Pell(w)` | 0 | 0 | 1 | 4 | 13 | 38 | 105 | 280 | 729 | 1866 | 4717 | 11812 |

The `− 2^{w−1}` removes the strips that do not reach height 3, as the `− 1` does for the Fibonacci castles ([[fibonacci-castle](pages/fibonacci-castle.md)]) and the `(h − 1)^w` does in `A(w, h) = h^w − (h − 1)^w` for all castles.

**In the OEIS.** The generating function is `x²` times `x/((1 − 2x − x²)(1 − 2x))`, the generating function of A094706, "Convolution of Pell(n) and 2^n", so[^a094706][^exec]

```
A_Pell(w)  =  A094706(w − 2)      (w ≥ 2).
```

The same numbers are column 2 of the triangle A283595, Motzkin prefixes of length `w − 1` and height 2: lowering every column by 1 turns a Pell castle into such a prefix.[^a283595]

**Growth.** The root of smallest modulus of `(1 − 2x − x²)(1 − 2x)` is `1/(1 + √2)`, so the Pell castles grow like the silver mean `1 + √2 ≈ 2.4142`: they are silver by width ([[castle-classification-growth](pages/castle-classification-growth.md)], [[metallic-means](pages/metallic-means.md)]). The subtracted `2^{w−1}` grows more slowly, so the Pell castles are a fraction of the Pell strips that tends to 1.

**The other boundary conditions.** Dropping `c_1 = 1` gives the 1-smooth castles of height 3, `A001333(w + 1) − 2^w = 1, 3, 9, 25, 67, 175, 449, …` from the Pell-Lucas numbers A001333 ([[castle-classification-growth](pages/castle-classification-growth.md)]); their generating function is `x(1 − x)/((1 − 2x)(1 − 2x − x²))`, so they number exactly `A106514(w − 1)`, "Expansion of (1-x)/((1-2*x)*(1-2*x-x^2))".[^a106514] Requiring both end columns at height 1 gives `0, 0, 0, 0, 1, 5, 18, 56, 161, 441, …`, generating function `x⁵/((1 − x)(1 − 2x)(1 − 2x − x²))`: the partial sums of the Pell castles, shifted by 2, since the generating function is `x²/(1 − x)` times the Pell castles'. That row is column 2 of the triangle A097862 (Motzkin paths of length `w − 1` and height 2); its OEIS status as a sequence is on [[castle-sequence-catalogue](pages/castle-sequence-catalogue.md)].[^a097862] All three grow like `1 + √2`.[^exec]

## Blocks and parity

Project Euler 502 counts castles by the parity of their block count, `blocks(c) = Σ_{i=0}^{w} max(0, c_i − c_{i+1})` with `c_0 = c_{w+1} = 0`. Split by parity, with `A^e_Pell(w)` and `A^o_Pell(w)` the even-block and odd-block Pell castles of width `w` and `S_Pell(w) = A^e_Pell(w) − A^o_Pell(w)` the signed count:

| `w` | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `A^e_Pell(w)` | 0 | 0 | 0 | 0 | 2 | 13 | 51 | 154 | 400 | 969 | 2331 | 5742 |
| `A^o_Pell(w)` | 0 | 0 | 1 | 4 | 11 | 25 | 54 | 126 | 329 | 897 | 2386 | 6070 |
| `S_Pell(w)` | 0 | 0 | −1 | −4 | −9 | −12 | −3 | 28 | 71 | 72 | −55 | −328 |

The first even-block Pell castles have width 5: `(1, 2, 1, 2, 3)` and `(1, 2, 3, 2, 3)`, each with 4 blocks.[^exec] Both rows satisfy a linear recurrence of order 8 with denominator

```
(1 − x)(1 − 2x)(1 − 2x − x²)(1 − 2x + 2x²)(1 − 2x + 3x²),
```

and `S_Pell` one of order 5 with denominator `(1 − x)(1 − 2x + 2x²)(1 − 2x + 3x²)` (found by Berlekamp-Massey on 40 terms, [[berlekamp-massey](pages/berlekamp-massey.md)]). The roots of `1 − 2x + 2x²` are `1/(1 ± i)` and those of `1 − 2x + 3x²` are `1/(1 ± i√2)`, so `S_Pell` grows like `√3 < 1 + √2`, and `A^e_Pell = (A_Pell + S_Pell)/2` is half the Pell castles up to a smaller term, as `A^e = (A + S)/2` is for all castles ([[castle-counting-formula](pages/castle-counting-formula.md)]). The OEIS status of the three rows is on [[castle-sequence-catalogue](pages/castle-sequence-catalogue.md)].[^exec]

## Other ceilings

The same rule with ceiling `h` instead of 3 is followed on [[1-smooth-castles](pages/1-smooth-castles.md)], for `h = 2` to 12. The subtraction becomes `strips(w, h) − strips(w, h − 1)`, the anchored strips with ceiling `h` minus those with ceiling `h − 1`, and the generating function `x³/((1 − 2x − x²)(1 − 2x))` is the `h = 3` case of `x^h/(η_h(x)·η_{h−1}(x))`, where `η_h` is the reduced denominator of the strip generating function. At `h = 4` the strips are counted by the odd-indexed Fibonacci numbers and the castles grow like `φ²`; the Pell numbers and the silver ratio belong to `h = 3`.

Raising the step bound instead, to neighboring columns differing by at most `m`, keeps the Pell form on the diagonal `h = m + 2`: the strips have generating function `x/(1 − (m+1)x − m·x²)` and the castles `m·x³/((1 − (m+1)x − m·x²)(1 − (m+1)x))`, which is this page's generating function at `m = 1` ([[m-smooth-castles](pages/m-smooth-castles.md)] §3.6).

## Computation

```python
from collections import defaultdict
def pell_castles(W):
    """(even, odd) Pell castles of widths 1..W, by DP over (last height, block parity, reached 3).
    Blocks are counted as ascents from the floor: blocks = c_1 + sum max(0, c_{i+1} - c_i)."""
    dp, out = {(1, 1, False): 1}, []
    for w in range(1, W + 1):
        if w > 1:
            nd = defaultdict(int)
            for (a, p, r), v in dp.items():
                for b in (a - 1, a, a + 1):
                    if 1 <= b <= 3:
                        nd[(b, (p + max(0, b - a)) % 2, r or b == 3)] += v
            dp = nd
        out.append(tuple(sum(v for (a, p, r), v in dp.items() if r and p == q) for q in (0, 1)))
    return out
P = [0, 1]
for _ in range(40): P.append(2 * P[-1] + P[-2])
A094706 = [0, 1, 4, 13, 38, 105, 280, 729, 1866, 4717, 11812, 29365, 72590, 178641, 438064]
c = pell_castles(16)
assert all(e + o == P[w] - 2 ** (w - 1) for w, (e, o) in enumerate(c, start=1))
assert all(P[w] - 2 ** (w - 1) == A094706[w - 2] for w in range(2, 17))
print([e for e, o in c])    # 0, 0, 0, 0, 2, 13, 51, 154, 400, 969, 2331, 5742, ...
```

## Related Concepts

- [[1-smooth-pell-castles-by-area](pages/1-smooth-pell-castles-by-area.md)] - these same Pell castles by width and area together, with area growth `1.666301937...` rather than the silver ratio by width.
- [[1-smooth-castles](pages/1-smooth-castles.md)] - the anchored 1-smooth castles of height `h` for every `h`, with the Pell castles as `h = 3`.
- [[m-smooth-castles](pages/m-smooth-castles.md)] - step bound `m`; the Pell castles are the `m = 1` point of the diagonal `h = m + 2`.
- [[pell-castle-strip](pages/pell-castle-strip.md)] - the Pell castle strip, the superset without the ceiling requirement, and the seminar from the Analytic Combinatorics exercise.
- [[pell-numbers](pages/pell-numbers.md)] - `P⋆_w`, A000129.
- [[castle-classification-growth](pages/castle-classification-growth.md)] - the families silver by width, among them the Pell castles and the ridge castles of height 3.
- [[castle-classification-shape](pages/castle-classification-shape.md)] - the m-smooth type at `m = 1`.
- [[metallic-strip-realizability](pages/metallic-strip-realizability.md)] - the 1-smooth strip as the silver realization.
- [[fibonacci-castle](pages/fibonacci-castle.md)] - the Fibonacci castles, golden by width, where reaching height 2 subtracts 1.
- [[castle-notation](pages/castle-notation.md)] - the Pell castle entry and the family counts `A_X`, `A^e_X`, `A^o_X`, `S_X`.

## Footnotes

[^a094706]: https://oeis.org/A094706 (read 2026-10-16) - "Convolution of Pell(n) and 2^n."; "G.f.: x/((1-2*x-x^2)*(1-2*x))."; data `0, 1, 4, 13, 38, 105, 280, 729, 1866, 4717, 11812, 29365, …`, offset 0.
[^a283595]: https://oeis.org/A283595 (read 2026-10-16) - "Triangle read by rows: T(n,k) is the number of Motzkin prefixes (i.e., left factors of Motzkin paths) of length n and height k."; data `1, 1, 1, 1, 3, 1, 1, 7, 4, 1, 1, 15, 13, 5, 1, 1, 31, 38, 19, 6, 1, 1, 63, 105, 64, 26, 7, 1, 1, 127, 280, 202, 97, 34, 8, 1, …`, offset 0; column 2 reads `1, 4, 13, 38, 105, 280` from row 2.
[^a097862]: https://oeis.org/A097862 (read 2026-10-16) - "Triangle read by rows: T(n,k) is the number of Motzkin paths of length n and height k (n>=0, k>=0)."; data `1, 1, 1, 1, 1, 3, 1, 7, 1, 1, 15, 5, 1, 31, 18, 1, 1, 63, 56, 7, 1, 127, 161, 33, 1, 1, 255, 441, 129, 9, …`, offset 0; column 2 reads `1, 5, 18, 56, 161, 441` from row 4.
[^a106514]: https://oeis.org/A106514 (read 2026-10-16) - "Expansion of (1-x)/((1-2*x)*(1-2*x-x^2))."; comment "Convolution of A000079 and A001333."; data `1, 3, 9, 25, 67, 175, 449, 1137, 2851, …`, offset 0.
[^exec]: Verified by execution (Python 3.11 with SymPy, 2026-10-16): the Pell castles enumerated from the definition for `w ≤ 12` number `P⋆_w − 2^{w−1}`; `P⋆_w − 2^{w−1} = A094706(w − 2)` for `w ≤ 16` (and for all `w` by the generating-function identity); the parity rows by the dynamic program of the section *Computation* to width 45, and Berlekamp-Massey on them gives the denominators stated (orders 8, 8 and 5); the two even-block castles of width 5; the free-first-column row `1, 3, 9, 25, 67, …` and the both-ends row `0, 0, 0, 0, 1, 5, 18, 56, 161, 441, …`; A094706, A283595, A097862 and A106514 checked on oeis.org.
