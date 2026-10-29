---
title: Sum of three cubes castles
category: Analyses
summary: Which castle counts are sums of three cubes. With signed cubes, under Heath-Brown's conjecture a count is a sum of three cubes exactly when it is not 4 or 5 modulo 9, and A^e(w, h) mod 9 is periodic in the width (periods 24, 24, 240, 3120, 2184, 2184, 2184, 10920, 21840, 21840, 11514360 for h = 2..12, all proved minimal) and in the height (period 2 * 3^(1 + ceil(log_3 w)) for 2 <= w <= 10 and w = 100, computed), since P(k, w) is a polynomial of degree at most w in k on each parity class. In each row h >= 4 about 2/9 of the residues are 4 or 5 (20.5% of the A^e(w, h) with w >= 4 and A <= 10^9), and the three Project Euler targets A^e(10^12, 100), A^e(10000, 10000), A^e(100, 10^12) are 6, 7, 6 mod 9. Closed forms settle three families - A^e(w, 2) = 2^(w-1) + eps 2^floor((w-1)/2) is a cube at w = 1 (mod 12), twice a cube at w = 5 and four times a cube, hence excluded, at w = 9 (mod 12); the width-3 column is triangular numbers interleaved with 5 C(h, 2) + 1, excluded iff h = 4, 6 (mod 18); A(3m, h) is a difference of two cubes. With positive cubes, 56 of the 552 even-block counts with w >= 4 below 10^8 are sums of three positive cubes against 55.7 expected. Even perfect numbers are A^o(3, 2^p), and A^e(2p, 2) for p = 3 (mod 4).
tags: [analysis, castle, sum-of-cubes, mod-9, periodicity, kitamasa, closed-form, height-2, perfect-numbers, taxicab, booker-sutherland, worked-example, computation]
sources: [project-euler-502-solution, project-euler-502]
created: 2026-09-20
updated: 2026-10-25
---

# Sum of three cubes castles

[[hardy-ramanujan-castle](pages/hardy-ramanujan-castle.md)] has `A^e(6, 4) = 1729 = 1^3 + 12^3 = 9^3 + 10^3`: the number of even-block castles of width 6 and height 4 is a sum of two cubes in two ways, hence a sum of three cubes with a zero cube, and `9^3 + 10^3 + (−12)^3 = 1` besides. This page asks which castle counts are sums of three cubes. Every count has a closed form ([[castle-counting-formula](pages/castle-counting-formula.md)]), and the [[sums-of-three-cubes](pages/sums-of-three-cubes.md)] problem has one known obstruction, `n ≡ 4, 5 (mod 9)`, conjectured by Heath-Brown to be the only one. So the question has three parts: which castle counts are not sums of three cubes, a computation of residues; which admissible counts have an explicit representation; and which counts are sums of three positive cubes, where the tower count `T(k, 3) = (k+1)^3` turns each identity into a statement about towers.

The counts are those of [[castle-notation](pages/castle-notation.md)]: `A(w, h) = h^w − (h−1)^w` castles of width `w` and height `h`, of which `A^e(w, h)` have an even and `A^o(w, h)` an odd number of blocks. `A^e(w, h)` is the count the Project Euler problem writes `F(w, h)`. The censuses on this page leave out the cells with `w ≤ 2` unless they name them: a castle `(a, b)` of width 2 has `max(a, b)` blocks, so every castle of width 2 and height `h` has `h` blocks, `A^e(2, h) = 2h − 1` for even `h` and `0` for odd `h`, and the values `2h − 1` with `h` even are all `n ≡ 3 (mod 4)` with `n ≥ 3`.[^exec]

## The residue test

Under Heath-Brown's conjecture, `A^e(w, h)` is a sum of three cubes exactly when `A^e(w, h) mod 9` is not `4` or `5`.[^1] The residues are periodic in both directions.

- **Width.** For fixed `h`, `A^e(·, h)` is a combination of `h^w`, `(h−1)^w`, `P(h−1, w)` and `P(h−2, w)`, so it satisfies a linear recurrence with integer coefficients ([[castle-counting-formula](pages/castle-counting-formula.md)], Equation (6)). Modulo 9 its state takes finitely many values, so the residues are eventually periodic ([[mod-p-observatory](pages/mod-p-observatory.md)] treats the periods modulo a prime).
- **Height.** For fixed `w`, `P(k, w)` is a polynomial in `k` of degree at most `w` on each class of `k` modulo 2. Write the towers `c ∈ {0, …, k}^w` by the distinct values `0 = v_0 < v_1 < ⋯ < v_m` of `(0, c_1, …, c_w)`, with `m ≤ w`. The sign `(−1)^{blocks(c)}` depends only on which positions take which value and on the parities of the `v_j`, since `blocks(c)` is the total ascent. For fixed positions and parities, the gaps `v_j − v_{j−1} ≥ 1` have prescribed parities, and the number of choices with `v_m ≤ k` is `C(⌊(k − R)/2⌋ + m, m)` for a constant `R ≤ 2m`, a polynomial of degree `m` in `k` on each parity class. So `A^e(w, ·) mod 9` is periodic in `h`. On [[signed-tower-k-direction](pages/signed-tower-k-direction.md)] the exact characteristic polynomial `(x+1)^w (x−1)^{w−2}` is computed for `4 ≤ w ≤ 12`.

The periods in the width, each checked to be a period and to be minimal:[^exec]

| `h` | period of `A^e(·, h) mod 9` in `w` | residues `4, 5` per period | excluded fraction | first excluded `w` |
|---|---|---|---|---|
| 2 | 24 | 2 | 0.083 | 9, 21 |
| 3 | 24 | 3 | 0.125 | 7, 21, 24 |
| 4 | 240 | 54 | 0.225 | 3, 8, 13, 18 |
| 5 | 3120 | 692 | 0.222 | 4, 14, 22, 24 |
| 6 | 2184 | 496 | 0.227 | 3, 10, 11, 14 |
| 7 | 2184 | 439 | 0.201 | 9, 13, 14, 18 |
| 8 | 2184 | 478 | 0.219 | 6, 9, 10, 15 |
| 9 | 10920 | 2422 | 0.222 | 5, 6, 15, 17 |
| 10 | 21840 | 4859 | 0.222 | 9, 20, 36, 39 |
| 11 | 21840 | 4748 | 0.217 | 10, 11, 15, 18 |
| 12 | 11514360 | 2557075 | 0.222 | 2, 12, 27, 34 |

Every row is periodic from `w = 2`, and the rows `h = 2, 5, 8, 9, 10, 11` from `w = 1`. Modulo 3 the periods at `h = 2, 3, 4, 5` are `8, 8, 80, 3120`, so the mod-9 periods are three times as long at `h = 2, 3, 4` and equal at `h = 5`. From `h = 4` on the excluded fraction is near `2/9 = 0.222`; `h = 2` and `h = 3` are lower, for the reasons in the section *Three families with closed forms*, and `h = 7` has `439/2184 = 0.201` over its full period.

The periods in the height:[^exec]

| `w` | period of `A^e(w, ·) mod 9` in `h` | excluded fraction |
|---|---|---|
| 1 | 2 | 0 |
| 2 | 18 | `2/18` |
| 3 | 18 | `2/18` |
| 4 | 54 | `12/54` |
| 5 | 54 | `8/54` |
| 6 | 54 | `12/54` |
| 7 | 54 | `10/54` |
| 8 | 54 | `6/54` |
| 9 | 54 | `15/54` |
| 10 | 162 | `36/162` |

For `2 ≤ w ≤ 10` the period is `2 · 3^{1 + ⌈log_3 w⌉}`, and at `w = 100` it is `1458 = 2 · 3^6`, the same formula; `P(k, 100) mod 9` also has period 1458 in `k`. The formula is the mod-p rule `2 p^{⌈log_p L⌉}` for the period of `P(k, L) mod p` on [[mod-p-observatory](pages/mod-p-observatory.md)], with one more factor of 3 for the modulus `3^2`.[^exec]

**Over all cells with `A(w, h) ≤ 10^9`** (19,131 cells, `3 ≤ w ≤ 29`, `h ≥ 2`): `A^e` has 18,256 entries at `w = 3`, of which 2,029 (11.1%) are excluded, and 875 at `w ≥ 4`, of which 179 (20.5%) are excluded. `A` is never excluded at `w = 3`, a fact proved in the next section, and is excluded 225 times of 875 (25.7%) at `w ≥ 4`; `A^o` is excluded 2,028 times at `w = 3` (11.1%) and 184 times at `w ≥ 4` (21.0%). The three tables have 57,347 distinct positive values up to `10^9`, of which 4,643 (8.1%) are excluded; the integers from 1 to `10^9` that pass the residue test number 777,777,778. Most of the castle counts come from the width-3 column, about 18,000 values in each table.[^exec]

## Three families with closed forms

**`A` at widths divisible by 3.** `A(3m, h) = h^{3m} − (h−1)^{3m} = (h^m)^3 − ((h−1)^m)^3` is a difference of two cubes, hence a sum of three cubes with a zero cube, for every `h`. `A(6, 4) = 16^3 − 9^3` on [[hardy-ramanujan-castle](pages/hardy-ramanujan-castle.md)] is the case `m = 2`. Modulo 9 a difference of two cubes is in `{0, ±1, ±2}`, never `±4`, so `A(3, h)` is never excluded. Nothing of the kind holds for `A^e` and `A^o`: at `(6, 4)` they are `(16^3 − 9^3 ± (4^3 + 3^3))/2`, the plus sign for `A^e`, since `S(6, 4) = P(2, 6) − P(3, 6) = 59 + 32 = 91`.

**The row of height 2.** By Equation (1) of [[castle-counting-formula](pages/castle-counting-formula.md)] and `P(1, L) = Re((1+i)^{L+1})` ([[signed-tower-count](pages/signed-tower-count.md)]), `A^e(w, 2) = 2^{w−1} − Re((1+i)^{w+1})/2`. Since `(1+i)^{w+1} = 2^{(w+1)/2} e^{i(w+1)π/4}`, its real part is `0` for `w ≡ 1 (mod 4)`, `−2^{⌊(w−1)/2⌋+1}` for `w ≡ 2, 3, 4 (mod 8)` and `+2^{⌊(w−1)/2⌋+1}` for `w ≡ 6, 7, 0 (mod 8)`, so

```
A^e(w, 2)  =  2^{w−1} + ε_w · 2^{⌊(w−1)/2⌋},      ε_w = 0   for w ≡ 1 (mod 4)
                                                  ε_w = +1  for w ≡ 2, 3, 4 (mod 8)
                                                  ε_w = −1  for w ≡ 6, 7, 0 (mod 8)
```

For `w ≡ 1 (mod 4)` the count is the power of two `2^{w−1}`, which is a cube, twice a cube or four times a cube according to `w − 1` modulo 3:

| `w mod 12` | `A^e(w, 2)` | cube reading | mod 9 | sum of three cubes |
|---|---|---|---|---|
| 1 | `2^{w−1} = (16^{(w−1)/12})^3` | a cube: `A^e(13, 2) = 16^3`, `A^e(25, 2) = 256^3`, `A^e(37, 2) = 4096^3` | 1 | yes, `c^3 + 0^3 + 0^3` |
| 5 | `2^{w−1} = 2 (2^{(w−2)/3})^3` | twice a cube: `A^e(5, 2) = 2 · 2^3`, `A^e(17, 2) = 2 · 32^3`, `A^e(29, 2) = 2 · 512^3` | 7 | yes, `c^3 + c^3 + 0^3` |
| 9 | `2^{w−1} = 4 (2^{(w−3)/3})^3` | four times a cube: `A^e(9, 2) = 4 · 4^3`, `A^e(21, 2) = 4 · 64^3`, `A^e(33, 2) = 4 · 1024^3` | 4 | no |

Four times a cube prime to 3 is `±4 (mod 9)`. Over the period 24 of the row the excluded widths are `w = 9, 21`, so the classes `w ≡ 9 (mod 12)` are the only excluded entries of the row, and its excluded fraction is `1/12`. Two more classes are sums of two cubes: at `w ≡ 19 (mod 24)`, `A^e(w, 2) = 2^{w−1} + 2^{(w−1)/2} = (2^{(w−1)/3})^3 + (2^{(w−1)/6})^3`, as `A^e(19, 2) = 262656 = 64^3 + 8^3` and `A^e(43, 2) = 16384^3 + 128^3`; at `w ≡ 7 (mod 24)` the same with a minus sign, as `A^e(7, 2) = 56 = 4^3 − 2^3` and `A^e(31, 2) = 1024^3 − 32^3`. The cube `A^e(13, 2) = 4096` equals `T(15, 3) = 16^3`, the number of towers of height at most 15 on a base of length 3.[^exec]

**Perfect numbers.** For `w = 2p` with `p ≡ 3 (mod 4)`, `w ≡ 6 (mod 8)` and `A^e(2p, 2) = 2^{2p−1} − 2^{p−1} = 2^{p−1}(2^p − 1)`. When `2^p − 1` is a Mersenne prime this is an even perfect number: `28 = A^e(6, 2)`, `8128 = A^e(14, 2)`, `137438691328 = A^e(38, 2)`, `2^{126}(2^{127} − 1) = A^e(254, 2)`. The identity needs `p ≡ 3 (mod 4)`, not primality; for `p ≡ 1 (mod 4)` the sign flips and `A^e(2p, 2) = 2^{p−1}(2^p + 1)`, as `A^e(10, 2) = 528`. Every even perfect number `2^{p−1}(2^p − 1)` is also the triangular number `C(2^p, 2)`, and `A^o(3, h) = C(h, 2)` for even `h` (the paragraph **The width-3 column** of this section), so `6 = A^o(3, 4)`, `28 = A^o(3, 8)`, `496 = A^o(3, 32)`, `8128 = A^o(3, 128)`: every even perfect number is the odd-block count of the cell `(3, 2^p)`. `8128 = 4^3 + 4^3 + 20^3` is also a sum of three positive cubes.[^exec]

**The width-3 column.** The Solution subpage gives `P(k, 3) = (−1)^k (k+1)^2` ([[signed-tower-count](pages/signed-tower-count.md)]; checked for `k < 60`). With `A(3, h) = 3h^2 − 3h + 1`, Equation (1) of [[castle-counting-formula](pages/castle-counting-formula.md)] gives

```
A^e(3, h)  =  C(h, 2)          (h odd)          5 C(h, 2) + 1     (h even)
A^o(3, h)  =  5 C(h, 2) + 1    (h odd)          C(h, 2)           (h even)
A(3, h)    =  6 C(h, 2) + 1  =  h^3 − (h−1)^3
```

checked against the dynamic program for `h ≤ 200`.[^exec] At odd height the even-block counts are `A^e(3, 2m+1) = m(2m+1) = 0, 3, 10, 21, 36, 55, …`, the second hexagonal numbers A014105, every other triangular number of A000217. At even height they are `A^e(3, 2m) = 10m^2 − 5m + 1 = 5 m(2m − 1) + 1 = 6, 31, 76, 141, 226, 331, …`, five times a hexagonal number of A000384 plus one. The other half of the odd column, `A^o(3, 2n+1) = 10n^2 + 5n + 1 = 1, 16, 51, 106, 181, 276, …`, is A080860, and `A^e(3, 2m)` is the same quadratic at `n = −m`.[^2]

Triangular numbers are `0, 1, 3, 6 (mod 9)`, never `4` or `5`. And `5 C(h, 2) + 1 ≡ 4 (mod 9)` exactly when `C(h, 2) ≡ 6 (mod 9)`, that is `h ≡ 4, 6 (mod 9)`, while `5 C(h, 2) + 1 ≡ 5` would need `C(h, 2) ≡ 8`, which never happens. Therefore

- `A^e(3, h)` is excluded exactly when `h ≡ 4, 6 (mod 18)`: `A^e(3, 4) = 31`, `A^e(3, 6) = 76`, `A^e(3, 22) = 1156`, `A^e(3, 24) = 1381`, …;
- `A^o(3, h)` is excluded exactly when `h ≡ 13, 15 (mod 18)`;
- `A(3, h)` is never excluded,

which is `1/9` of each of the columns `A^e(3, ·)` and `A^o(3, ·)`, the entry `2/18` of the table of periods in the height. The width-2 cell behaves the same way: `A^e(2, h) = 2h − 1` (even `h`) is excluded exactly when `h ≡ 12, 16 (mod 18)`.

## The three Project Euler targets

The problem asks for `A^e(10^12, 100) + A^e(10000, 10000) + A^e(100, 10^12)` modulo `10^9 + 7` ([[project-euler-502](pages/project-euler-502.md)]). Modulo 9:[^exec]

| target | `mod 9` | computation |
|---|---|---|
| `A^e(10^12, 100)` | 6 | powers of the signed transfer matrices on the tower heights `0, …, 99` and `0, …, 98` over `Z/9` |
| `A^e(10000, 10000)` | 7 | the column-height dynamic program for `P(9999, 10^4)` and `P(9998, 10^4)` over `Z/9` |
| `A^e(100, 10^12)` | 6 | the parity polynomials of `P(·, 100)`, of degree at most 100, interpolated from `P(k, 100)` for `k ≤ 201` and evaluated exactly at `k = 10^12 − 1` and `10^12 − 2` |

The same computations give `A^e(4, 2), A^e(13, 10), A^e(10, 13), A^e(100, 100) ≡ 1, 3, 7, 8 (mod 9)`, the residues of the exact values. None of the three targets is `4` or `5`, so all three pass the residue test and, under Heath-Brown's conjecture, are sums of three cubes. Their sum is `≡ 1 (mod 9)`; the problem's answer, the sum modulo `10^9 + 7`, does not determine this residue. Kitamasa's method also works over `Z/9` ([[kitamasa](pages/kitamasa.md)], [[castle-cryptography-ring](pages/castle-cryptography-ring.md)]): the reduction of `x^L` needs only a monic characteristic polynomial, and `char_k` is monic because `den_k(0) = 1`.

## The even-block counts below 1000

`A^e` has fifty entries below 1000 with `w ≥ 3` and `h ≥ 2`, forty-six distinct values. For each, the residue and a representation with `max(|x|, |y|, |z|) ≤ 1000` where one exists:[^exec]

| `A^e` | cell | mod 9 | three cubes | positive |
|---|---|---|---|---|
| 3 | `(3, 3)` | 3 | `1^3 + 1^3 + 1^3` | yes |
| 6 | `(3, 2)` | 6 | `(-1)^3 + (-1)^3 + 2^3` |  |
| 10 | `(3, 5)`, `(4, 2)` | 1 | `1^3 + 1^3 + 2^3` | yes |
| 16 | `(5, 2)` | 7 | `0^3 + 2^3 + 2^3` |  |
| 21 | `(3, 7)`, `(4, 3)` | 3 | `(-11)^3 + (-14)^3 + 16^3` |  |
| 28 | `(6, 2)` | 1 | `0^3 + 1^3 + 3^3` |  |
| 31 | `(3, 4)` | 4 | **no** |  |
| 36 | `(3, 9)` | 0 | `1^3 + 2^3 + 3^3` | yes |
| 55 | `(3, 11)` | 1 | `1^3 + 3^3 + 3^3` | yes |
| 56 | `(7, 2)` | 2 | `0^3 + (-2)^3 + 4^3` |  |
| 76 | `(3, 6)` | 4 | **no** |  |
| 78 | `(3, 13)` | 6 | `26^3 + 53^3 + (-55)^3` |  |
| 89 | `(5, 3)` | 8 | `6^3 + 6^3 + (-7)^3` |  |
| 105 | `(3, 15)` | 6 | `(-4)^3 + (-7)^3 + 8^3` |  |
| 117 | `(4, 4)` | 0 | `0^3 + (-2)^3 + 5^3` |  |
| 120 | `(8, 2)` | 3 | `(-2)^3 + 4^3 + 4^3` |  |
| 122 | `(4, 5)` | 5 | **no** |  |
| 136 | `(3, 17)` | 1 | `2^3 + 4^3 + 4^3` | yes |
| 141 | `(3, 8)` | 6 | `2^3 + 2^3 + 5^3` | yes |
| 171 | `(3, 19)` | 0 | `(-5)^3 + (-6)^3 + 8^3` |  |
| 210 | `(3, 21)` | 3 | `(-2)^3 + (-5)^3 + 7^3` |  |
| 226 | `(3, 10)` | 1 | `2^3 + (-5)^3 + 7^3` |  |
| 253 | `(3, 23)` | 1 | `4^3 + 4^3 + 5^3` | yes |
| 256 | `(9, 2)` | 4 | **no** (`4 · 4^3`) |  |
| 300 | `(3, 25)` | 3 | `34^3 + 55^3 + (-59)^3` |  |
| 307 | `(6, 3)` | 1 | `(-5)^3 + 6^3 + 6^3`; also `3^3 + 4^3 + 6^3` | yes |
| 331 | `(3, 12)` | 7 | `0^3 + (-10)^3 + 11^3` |  |
| 351 | `(3, 27)` | 0 | `0^3 + 2^3 + 7^3` |  |
| 367 | `(4, 7)` | 7 | none with `max ≤ 50000` |  |
| 406 | `(3, 29)` | 1 | `(-1)^3 + 4^3 + 7^3` |  |
| 439 | `(5, 4)` | 7 | none with `max ≤ 50000` |  |
| 448 | `(4, 6)` | 7 | `0^3 + (-4)^3 + 8^3` |  |
| 456 | `(3, 14)` | 6 | `2^3 + (-4)^3 + 8^3` |  |
| 465 | `(3, 31)` | 6 | `11^3 + 11^3 + (-13)^3` |  |
| 528 | `(3, 33)`, `(10, 2)` | 6 | `2^3 + 2^3 + 8^3` | yes |
| 595 | `(3, 35)` | 1 | `21^3 + 37^3 + (-39)^3` |  |
| 601 | `(3, 16)` | 7 | `(-4)^3 + (-4)^3 + 9^3` |  |
| 666 | `(3, 37)` | 0 | `1^3 + (-4)^3 + 9^3` |  |
| 741 | `(3, 39)` | 3 | `(-5)^3 + (-11)^3 + 13^3` |  |
| 766 | `(3, 18)` | 1 | `(-3)^3 + 4^3 + 9^3` |  |
| 820 | `(3, 41)`, `(4, 9)` | 1 | `(-5)^3 + 6^3 + 9^3`; also `3^3 + 4^3 + 9^3` | yes |
| 903 | `(3, 43)` | 3 | none with `max ≤ 50000` |  |
| **906** | **`(5, 5)`** | 6 | `(-74924259395610397)^3 + 72054089679353378^3 + 35961979615356503^3` |  |
| 951 | `(3, 20)` | 6 | `(-10)^3 + (-25)^3 + 26^3` |  |
| 977 | `(7, 3)` | 5 | **no** |  |
| 990 | `(3, 45)` | 0 | `(-5)^3 + (-6)^3 + 11^3` |  |

Five of the fifty entries are excluded (`31, 76, 122, 256, 977`). Three of them are in the families of the previous section: `31 = A^e(3, 4)` and `76 = A^e(3, 6)` at `h = 4, 6`, and `256 = A^e(9, 2) = 4 · 4^3`; `122 = A^e(4, 5)` and `977 = A^e(7, 3)` come from the table of periods in the width. Forty-one entries have a representation with `max(|x|, |y|, |z|) ≤ 1000`. Of the other four, `367`, `439` and `903` have no representation with `max(|x|, |y|, |z|) ≤ 50000`; all three are solved in the literature, since every `n < 1000` not `4` or `5` modulo 9 has a known representation except `114, 390, 627, 633, 732, 921, 975`.[^1] And `906 = A^e(5, 5)` was among the open cases below 1000 in 2009; the representation in the table is the one Booker presented in 2019.[^1]

**The seven unsolved numbers.** None of `114, 390, 627, 633, 732, 921, 975` is a value of `A`, `A^e` or `A^o` with `w ≥ 3` and `h ≥ 2`; the scan covers every cell with `A ≤ 20000`, and so every count below 1000. In the cells of width 2, `627 = A^e(2, 314)`, `975 = A^e(2, 488)`, `633 = A^o(2, 317)` and `921 = A^o(2, 461)`. The even numbers `114, 390, 732` are castle counts at no width, since `A(1, h) = 1` and `A(2, h) = 2h − 1` are odd and the cells of width 1 and 2 have `A^e` and `A^o` equal to `0` or `A`.[^exec]

**From 1000 to 20000.** `A^e` has 141 entries with `w ≥ 3` in this range. Eleven are excluded modulo 9, and of the 130 admissible ones, 105 have a representation with `max(|x|, |y|, |z|) ≤ 1000`. Five more have one with `max ≤ 15000`: `A^e(3, 61) = 1830 = (−8993)^3 + 9076^3 + (−2729)^3`, `A^e(3, 89) = 3916 = (−9719)^3 + 9867^3 + (−3492)^3`, `A^e(4, 12) = 4065 = (−1591)^3 + 1490^3 + 896^3`, `A^e(3, 50) = 6126 = (−6592)^3 + 6677^3 + (−2239)^3` and `A^e(3, 56) = 7701 = (−5755)^3 + 5651^3 + 2165^3`. The remaining twenty, `1131, 1626, 2481, 2630, 2775, 3741, 5050, 6555, 8445, 9321, 9591, 9870, 11391, 11490, 12246, 12561, 14196, 15801, 16653, 17391`, have none with `max ≤ 15000`.[^exec]

## Sums of three positive cubes

With positive cubes each search is finite. The sums of three positive cubes have density `0.10098` below `10^8` ([[sums-of-three-cubes](pages/sums-of-three-cubes.md)]). Every castle count up to `10^8` with `h ≥ 2`, tested:[^exec]

| table, cells | entries `≤ 10^8` | sums of three positive cubes | expected at `0.10098` |
|---|---|---|---|
| `A^e`, `w ≥ 4` | 552 | 56 | 55.7 |
| `A^e`, `w = 3` | 10232 | 1387 (13.6%) | 1033.3 |
| `A`, `w ≥ 4` | 446 | 69 | 45.0 |
| `A^o`, `w ≥ 4` | 555 | 58 | 56.0 |

The even-block counts with `w ≥ 4` are sums of three positive cubes at the background rate. The width-3 column is higher; its entries are small, two quadratics in `h`, and the density of sums of three positive cubes is `0.126` below 1000. `A` is also higher at `w ≥ 4`, with 44 of its 69 hits at `w = 4`.

Since `a^3 = T(a − 1, 3)`, each of the 56 even-block hits with `w ≥ 4` says that `A^e(w, h) = T(a−1, 3) + T(b−1, 3) + T(c−1, 3)`: the even-block castles of the cell are as many as the towers on a base of length 3 of heights at most `a − 1`, `b − 1` and `c − 1` together ([[castle-counting-formula](pages/castle-counting-formula.md)], the Lemma in the section *Tower count*). The first ten:

| `A^e(w, h)` | cell | `a^3 + b^3 + c^3` | towers |
|---|---|---|---|
| 10 | `(4, 2)` | `1^3 + 1^3 + 2^3` | `2 T(0, 3) + T(1, 3)`: twice the empty towers, and the 8 towers of height at most 1 |
| 307 | `(6, 3)` | `3^3 + 4^3 + 6^3` | `T(2, 3) + T(3, 3) + T(5, 3)` |
| 528 | `(10, 2)` | `2^3 + 2^3 + 8^3` | `2 T(1, 3) + T(7, 3)` |
| 820 | `(4, 9)` | `3^3 + 4^3 + 9^3` | `T(2, 3) + T(3, 3) + T(8, 3)` |
| 6572 | `(4, 14)` | `10^3 + 13^3 + 15^3` | `T(9, 3) + T(12, 3) + T(14, 3)` |
| 8128 | `(14, 2)` | `4^3 + 4^3 + 20^3` | the perfect number, `2 T(3, 3) + T(19, 3)` |
| 9037 | `(5, 8)` | `13^3 + 14^3 + 16^3` | `T(12, 3) + T(13, 3) + T(15, 3)` |
| 54757 | `(4, 35)` | `2^3 + 16^3 + 37^3` | `T(1, 3) + T(15, 3) + T(36, 3)` |
| 86505 | `(11, 3)` | `2^3 + 26^3 + 41^3` | `T(1, 3) + T(25, 3) + T(40, 3)` |
| 190630 | `(4, 42)` | `15^3 + 31^3 + 54^3` | `T(14, 3) + T(30, 3) + T(53, 3)` |

The other 46 are at `(4, h)` for `h` in `{52, 80, 93, 118, 122, 143, 149, 155, 163, 182, 187, 191, 210, 214, 233, 236, 249, 251, 258, 260, 272, 295, 307, 322, 347, 379, 387, 413}`, at `(5, h)` for `h` in `{26, 27, 35, 40, 60, 61, 67}`, at `(6, 14)`, `(6, 16)`, `(7, 8)`, `(7, 9)`, `(7, 17)`, `(16, 3)`, and at height 2 at `(19, 2)`, `(20, 2)`, `(22, 2)`, `(25, 2)` and `(26, 2)`.[^exec]

## Cubes, two cubes, cubes plus one

Over all cells with `A ≤ 10^9` and `w ≥ 3`:[^exec]

- **Cubes.** The only cubes among the values of `A`, `A^e` and `A^o` are `A^e(13, 2) = 16^3`, `A^e(25, 2) = 256^3` and `A^o(3, 2) = 1`; the cubes `A^e(12k + 1, 2) = (16^k)^3` of the row of height 2 are the only ones above 1.
- **Sums of two positive cubes** among the `A^e` with `w ≥ 4`: `16 = A^e(5, 2)`, `28 = A^e(6, 2)`, `1729 = A^e(6, 4)`, `65536 = A^e(17, 2)`, `262656 = A^e(19, 2)`, `804482 = A^e(4, 85) = 5^3 + 93^3` and `268435456 = A^e(29, 2)`. The ones of height 2 are in the classes of the section *Three families with closed forms*. Outside height 2 there are two, `A^e(6, 4) = 1^3 + 12^3 = 9^3 + 10^3` and `A^e(4, 85) = 5^3 + 93^3`, and 1729 is the only one with two representations.
- **Cubes plus or minus one** among the `A^e`: `28 = 3^3 + 1 = A^e(6, 2)`, `1729 = 12^3 + 1 = A^e(6, 4)`, `4095 = 16^3 − 1 = A^e(3, 91)` and `8001 = 20^3 + 1 = A^e(3, 127)`; the last two are the triangular numbers `C(91, 2)` and `C(127, 2)`, and `4095 = A(12, 2)` as well.
- **Differences of two positive cubes** among the `A^e` below `10^7` off height 2: 25 counts, three with `w ≥ 4`, `A^e(4, 4) = 117 = 5^3 − 2^3`, `A^e(4, 6) = 448 = 8^3 − 4^3` and `A^e(4, 144) = 7880087 = 199^3 − 8^3`, and 22 at `w = 3`, beginning `A^e(3, 12) = 331 = 11^3 − 10^3`, `A^e(3, 91) = 4095 = 16^3 − 1^3`, `A^e(3, 109) = 5886 = 21^3 − 15^3`, `A^e(3, 135) = 9045 = 21^3 − 6^3`, `A^e(3, 190) = 89776 = 51^3 − 35^3` and `A^e(3, 209) = 21736 = 28^3 − 6^3`.

## Summary

- Under Heath-Brown's conjecture, `A^e(w, h)` is a sum of three cubes exactly when it is not `4` or `5` modulo 9; the residues are periodic in the width and in the height (section *The residue test*), and in each row `h ≥ 4` about `2/9` of the residues are excluded (20.5% of the counts with `w ≥ 4` and `A ≤ 10^9`). [[mod-9-equidistribution](pages/mod-9-equidistribution.md)] treats the limit `2/9` of the excluded fraction.
- `A(3m, h)` is a difference of two cubes; `A^e(w, 2)` is a cube at `w ≡ 1`, twice a cube at `w ≡ 5` and four times a cube, the only exclusions of the row, at `w ≡ 9 (mod 12)`; `A^e(3, h)` is triangular at odd `h` and `5 C(h, 2) + 1` at even `h`, excluded exactly when `h ≡ 4, 6 (mod 18)` (section *Three families with closed forms*).
- `A^e(10^12, 100)`, `A^e(10000, 10000)` and `A^e(100, 10^12)` are `6, 7, 6 (mod 9)` (section *The three Project Euler targets*).
- `A^e(5, 5) = 906` was solved in 2019, and none of the seven unsolved `n < 1000` is a castle count with `w ≥ 3` (section *The even-block counts below 1000*).
- The even-block counts with `w ≥ 4` are sums of three positive cubes at the background rate, 56 of 552 against 55.7 (section *Sums of three positive cubes*).
- Even perfect numbers are `A^o(3, 2^p)`, and `A^e(2p, 2)` for `p ≡ 3 (mod 4)` (section *Three families with closed forms*).

## Appearances in Sources

- [[project-euler-502-solution](pages/project-euler-502-solution.md)] - `T(k, L) = (k+1)^L`, `P(k, 3) = (−1)^k (k+1)^2`, and the evaluation of `P(h−1, w)`, `P(h−2, w)` at the targets.
- [[project-euler-502](pages/project-euler-502.md)] - the three targets.

## Related Concepts

- [[sums-of-three-cubes](pages/sums-of-three-cubes.md)] - the problem: the obstruction modulo 9, Heath-Brown's conjecture, the 2019 representations, and the density of sums of three positive cubes.
- [[mod-9-equidistribution](pages/mod-9-equidistribution.md)] - the fraction of castle counts in the residues 4 and 5 modulo 9 and its limit `2/9`.
- [[mod-9-coset-lift](pages/mod-9-coset-lift.md)] - the 3-adic divisibility of the row and column periods and the proof that the column `w = 4` hits every residue modulo 9 equally often over 54 consecutive heights.
- [[hardy-ramanujan-castle](pages/hardy-ramanujan-castle.md)] - `A^e(6, 4) = 1729` and `A(6, 4) = 16^3 − 9^3`.
- [[castle-counting-formula](pages/castle-counting-formula.md)] and [[castle-counting-function](pages/castle-counting-function.md)] - the formula for `A^e(w, h)` and the counts `A`, `A^e`, `A^o`.
- [[mod-p-observatory](pages/mod-p-observatory.md)] - the periods of the castle counts modulo a prime, which divide the lcm of the periods of their factors.
- [[signed-tower-count](pages/signed-tower-count.md)] - `P(1, L) = Re((1+i)^{L+1})` and `P(k, 3) = (−1)^k (k+1)^2`.
- [[signed-tower-k-direction](pages/signed-tower-k-direction.md)] - the characteristic polynomial `(x+1)^L (x−1)^{L−2}` of `P(·, L)` in `k`, proved for every `L ≥ 4`.
- [[kitamasa](pages/kitamasa.md)] and [[castle-cryptography-ring](pages/castle-cryptography-ring.md)] - the reduction of `x^L` modulo `char_k`, which works over `Z/9`.
- [[oeis-height2-hyperbolic-castles](pages/oeis-height2-hyperbolic-castles.md)] and [[hyperbolic-sequence-family](pages/hyperbolic-sequence-family.md)] - `A^e(w, 2) = A038505(w + 1)`.
- [[castle-snippets](pages/castle-snippets.md)] - `all_castles` and the block count for brute-force checks.
- [[castle-sequence-catalog](pages/castle-sequence-catalog.md)] and [[oeis-index](pages/oeis-index.md)] - the width-3 columns, and the A-numbers cited here.
- [[oeis-mining-pe502](pages/oeis-mining-pe502.md)] - the tables of castle counts, with `1729 = A^e(6, 4)`, `906 = A^e(5, 5)` and the powers of two in the row of height 2.

## Footnotes

[^1]: https://en.wikipedia.org/wiki/Sums_of_three_cubes (read 2026-10-16) - the obstruction modulo 9 and "It is unknown whether this necessary condition is sufficient"; Elsenhans and Jahnel (2009) left "only 33, 42, 74, 114, 165, 390, 579, 627, 633, 732, 795, 906, 921, and 975 as open problems in 2009 for n ≤ 1000"; Heath-Brown (1992) "conjectured that every n unequal to 4 or 5 modulo 9 has infinitely many representations as sums of three cubes"; "Booker also presented a representation for 906" with the triple in the table; "The only remaining unsolved cases up to 1,000 are the seven numbers 114, 390, 627, 633, 732, 921, and 975".
[^2]: https://oeis.org/A080860, https://oeis.org/A014105, https://oeis.org/A000384, https://oeis.org/A000217 (read 2026-10-16) - "a(n) = 10*n^2 + 5*n + 1" with data `1, 16, 51, 106, 181, 276, …`; "Second hexagonal numbers: a(n) = n*(2*n + 1)"; "Hexagonal numbers: a(n) = n*(2*n-1)"; "Triangular numbers".
[^exec]: Verified by execution (Python 3.11 with NumPy and SymPy, 2026-10-16). `P(k, L)` by the column-height dynamic program with prefix sums, checked against enumeration of all towers for `k ≤ 3`, `L ≤ 5`; `A^e(w, h)` from Equation (1) of castle-counting-formula; `P(k, 3) = (−1)^k (k+1)^2` for `k < 60`, the width-3 closed forms for `h ≤ 200`, the height-2 form for `w ≤ 60`. Periods in the width: the state of the dynamic programs for `P(h−1, ·)`, `P(h−2, ·)`, `h^w` and `(h−1)^w` evolves linearly over `Z/9`; each period `N` was checked by testing `c·T^j (T^N − I) s = 0` for `j` up to the state dimension (enough by the Cayley-Hamilton theorem, since the characteristic polynomial of `T` is monic) and minimality by the same test at `N/q` for each prime `q | N`; residue counts from the sequence over one period (11,514,360 terms at `h = 12`); the mod-3 periods the same way. Periods in the height: `P(k, w)` on each parity class from the Newton expansion of its values at `k ≤ 2w + 1` (differences of order `w + 1` vanish; checked against the dynamic program beyond the interpolation range for `w ≤ 8`), the period of `A^e(w, ·) mod 9` read off a sequence of twelve candidate periods. Census: all 19,131 cells with `A ≤ 10^9`, `w ≥ 3`, `h ≥ 2`. Targets: matrix powers over `Z/9` for `A^e(10^12, 100)`, the dynamic program over `Z/9` for `A^e(10000, 10000)`, exact Newton evaluation of the degree-100 parity polynomials for `A^e(100, 10^12)`. Representations: `x^3 + y^3` for `|x| ≤ |y| ≤ 1000` probed at `n − z^3`; deeper searches with `max(|x|, |y|, |z|) ≤ 15000` and `≤ 50000` through `x + y = d`, `d | n − z^3`, `x y = (d^2 − (n − z^3)/d)/3` and an exact square-root test; every printed triple re-multiplied exactly. Positive cubes: a boolean sieve of `a^3 + b^3 + c^3 ≤ 10^8`; the set of `x^3 + y^3 ≤ 10^9` for two cubes; exact cube roots; differences `y^3 − x^3 < 10^7`.
