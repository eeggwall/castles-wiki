---
title: Pell castle
category: Concepts
summary: A Pell castle is a castle of exact height 3 whose first column has height 1 and whose neighbouring columns differ in height by at most 1. These are the anchored 1-smooth strips of the Pell castle strip that reach their ceiling, so they number P_w − 2^{w−1} = 0, 0, 1, 4, 13, 38, 105, 280, … (the Pell number minus the 2^{w−1} anchored strips that stay at heights 1 and 2), with generating function x³/((1 − 2x − x²)(1 − 2x)), which is A094706(w − 2) (Convolution of Pell(n) and 2^n); they grow like the silver ratio 1 + √2, a silver width growth castle. Split by PE 502's block parity, the even-block and odd-block Pell castles (0, 0, 0, 0, 2, 13, 51, 154, … and 0, 0, 1, 4, 11, 25, 54, 126, …) satisfy an order-8 recurrence, their difference an order-5 one with denominator (1 − x)(1 − 2x + 2x²)(1 − 2x + 3x²); none of the three is in OEIS.
tags: [concept, castle, castle-type, pell, silver-ratio, transfer-matrix, 1-smooth, exact-height, parity, oeis]
sources: [pe502-pell-castle-strip]
created: 2026-10-04
updated: 2026-10-04
---

# Pell castle

## Definition

A castle is a skyline `(c_1, …, c_w)` of columns standing on a full bottom row, with maximum height exactly `h` ([[castle-polyomino](pages/castle-polyomino.md)]). A **Pell castle** of width `w` is a castle of exact height 3 whose first column has height 1 and whose neighbouring columns differ in height by at most 1:

```
c_1 = 1,      |c_{i+1} − c_i| ≤ 1  (1 ≤ i < w),      max_i c_i = 3.
```

- **Construction rule.** Start at height 1; at each step move up one, down one, or stay, never leaving `{1, 2, 3}`; and reach height 3 at least once.
- **Examples.** `(1, 2, 3, 2)` and `(1, 2, 2, 3, 3, 2, 1)` are Pell castles. The four Pell castles of width 4 are `(1, 1, 2, 3)`, `(1, 2, 2, 3)`, `(1, 2, 3, 2)`, `(1, 2, 3, 3)`.
- **Non-examples.** `(1, 2, 2, 1)` never reaches height 3; `(2, 3, 2)` starts at height 2; `(1, 3, 2)` rises by 2 in one step.

**From the Pell castle strip.** The Pell castle strip ([[pell-castle-strip](pages/pell-castle-strip.md)]) is the same rule without the ceiling requirement: the anchored 1-smooth skylines on heights `1, 2, 3`, which need not reach height 3. A Pell castle is a Pell strip that reaches its ceiling, so the strip is the superset and the Pell castles are its exact-height-3 part.

## Counting Pell castles

**The count.** The anchored 1-smooth strips of width `w` number the Pell numbers `P_w` (`P_1 = 1`, `P_2 = 2`, `P_{w} = 2P_{w−1} + P_{w−2}`; A000129), with width generating function `x/(1 − 2x − x²)` ([[pell-castle-strip](pages/pell-castle-strip.md)]). Those that never reach height 3 stay on `{1, 2}`, where every column after the first may be 1 or 2, so there are `2^{w−1}` of them. Hence

```
#{Pell castles of width w}  =  P_w − 2^{w−1},
Σ_w #{Pell castles of width w} x^w  =  x/(1 − 2x − x²) − x/(1 − 2x)  =  x³ / ((1 − 2x − x²)(1 − 2x)).
```

| `w` | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Pell strips `P_w` | 1 | 2 | 5 | 12 | 29 | 70 | 169 | 408 | 985 | 2378 | 5741 | 13860 |
| never reaching 3, `2^{w−1}` | 1 | 2 | 4 | 8 | 16 | 32 | 64 | 128 | 256 | 512 | 1024 | 2048 |
| **Pell castles** | 0 | 0 | 1 | 4 | 13 | 38 | 105 | 280 | 729 | 1866 | 4717 | 11812 |

The `− 2^{w−1}` is the exact-height condition, in the same way as the `− 1` for the Fibonacci castles ([[fibonacci-castle](pages/fibonacci-castle.md)]) and the `(h − 1)^w` in `h^w − (h − 1)^w` for all castles.

**In the OEIS.** The generating function is `x²` times `x/((1 − 2x − x²)(1 − 2x))`, the generating function of A094706, "Convolution of Pell(n) and 2^n", so

```
#{Pell castles of width w}  =  A094706(w − 2)      (w ≥ 2).
```

A094706 has no castle reading.[^a094706][^exec]

**Growth.** The dominant root of `(1 − 2x − x²)(1 − 2x)` is `1/(1 + √2)`, so the Pell castles grow like the silver ratio `1 + √2 ≈ 2.4142`: they are a silver width growth castle ([[castle-classification-growth](pages/castle-classification-growth.md)], [[metallic-means](pages/metallic-means.md)]). The subtracted `2^{w−1}` grows more slowly, so the Pell castles are a fraction of the Pell strips that tends to 1.

**The other boundary conditions.** Dropping `c_1 = 1` gives the 1-smooth castles of exact height 3, `A001333(w + 1) − 2^w = 1, 3, 9, 25, 67, 175, 449, …` from the Pell-Lucas numbers A001333 ([[castle-classification-growth](pages/castle-classification-growth.md)]); their generating function is `x(1 − x)/((1 − 2x)(1 − 2x − x²))`, so they number exactly `A106514(w − 1)`, "Expansion of (1-x)/((1-2*x)*(1-2*x-x^2))".[^a106514] Requiring both end columns at height 1 gives `0, 0, 0, 0, 1, 5, 18, 56, 161, 441, …`, generating function `x⁵/((1 − x)(1 − 2x)(1 − 2x − x²))`: the partial sums of the Pell castles, shifted by 2, since the generating function is `x²/(1 − x)` times the Pell castles'. That row has no OEIS match (searched 2026-10-04). All three grow like `1 + √2`.[^exec]

## Blocks and parity

PE 502 counts castles by the parity of their block count, `blocks(c) = Σ_{i=0}^{w} max(0, c_i − c_{i+1})` with `c_0 = c_{w+1} = 0`. Split by parity, the Pell castles of width `w` are

| `w` | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| even-block Pell castles | 0 | 0 | 0 | 0 | 2 | 13 | 51 | 154 | 400 | 969 | 2331 | 5742 |
| odd-block Pell castles | 0 | 0 | 1 | 4 | 11 | 25 | 54 | 126 | 329 | 897 | 2386 | 6070 |
| even − odd | 0 | 0 | −1 | −4 | −9 | −12 | −3 | 28 | 71 | 72 | −55 | −328 |

The first even-block Pell castles have width 5: `(1, 2, 1, 2, 3)` and `(1, 2, 3, 2, 3)`, each with 4 blocks.[^exec] Both rows satisfy a linear recurrence of order 8 with denominator

```
(1 − x)(1 − 2x)(1 − 2x − x²)(1 − 2x + 2x²)(1 − 2x + 3x²),
```

and the signed count, even minus odd, one of order 5 with denominator `(1 − x)(1 − 2x + 2x²)(1 − 2x + 3x²)` (found by Berlekamp-Massey on 40 terms, [[berlekamp-massey](pages/berlekamp-massey.md)]). The roots of `1 − 2x + 2x²` are `1/(1 ± i)` and those of `1 − 2x + 3x²` are `1/(1 ± i√2)`, so the signed count grows like `√3 < 1 + √2` and each parity class is half the Pell castles up to a smaller term, the shape of the castle counting formula ([[castle-counting-formula](pages/castle-counting-formula.md)]). The even-block, odd-block and signed rows have no OEIS match (searched 2026-10-04); they are novel candidates on [[castle-sequence-catalogue](pages/castle-sequence-catalogue.md)].[^exec]

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

- [[pell-castle-strip](pages/pell-castle-strip.md)] - the Pell castle strip, the superset without the ceiling requirement, and the seminar from the Analytic Combinatorics exercise.
- [[pell-numbers](pages/pell-numbers.md)] - `P_w`, A000129.
- [[castle-classification-growth](pages/castle-classification-growth.md)] - silver width growth castles, where the Pell castles sit beside the ridge castles of exact height 3.
- [[castle-classification-shape](pages/castle-classification-shape.md)] - the m-smooth type at `m = 1`.
- [[metallic-strip-realizability](pages/metallic-strip-realizability.md)] - the 1-smooth strip as the silver realization.
- [[fibonacci-castle](pages/fibonacci-castle.md)] - the golden counterpart, where the exact-height condition is `− 1`.
- [[castle-notation](pages/castle-notation.md)] - the Pell castle entry.

## Footnotes

[^a094706]: https://oeis.org/A094706 (fetched 2026-10-04) - "Convolution of Pell(n) and 2^n."; "G.f.: x/((1-2*x-x^2)*(1-2*x))."; data `0, 1, 4, 13, 38, 105, 280, 729, 1866, 4717, 11812, 29365, …`, offset 0.
[^a106514]: https://oeis.org/A106514 (fetched 2026-10-04) - "Expansion of (1-x)/((1-2*x)*(1-2*x-x^2))."; comment "Convolution of A000079 and A001333."; data `1, 3, 9, 25, 67, 175, 449, 1137, 2851, …`, offset 0.
[^exec]: Verified by execution (Python 3, SymPy, 2026-10-04), block above and a brute-force enumeration: the generating functions of the three boundary conditions at exact height 3 from the transfer matrix `[[1,1,0],[1,1,1],[0,1,1]]` (free, anchored, both ends) minus those of the strips on `{1, 2}`, matching brute force for `w ≤ 12`; for `w ≤ 14` the Pell castles enumerated from the definition number `P_w − 2^{w−1}` and match the dynamic program, and their parity split is as tabulated; `P_w − 2^{w−1} = A094706(w − 2)` for `w ≤ 16` (and for all `w` by the generating-function identity); Berlekamp-Massey on 40 terms of the even, odd and signed rows gives the denominators stated.
