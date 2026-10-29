---
title: Mersenne castles
category: Concepts
summary: A Mersenne castle is a castle whose neighboring columns, read as strings whose lengths are the column heights (Mersenne's law, frequency inversely proportional to length), sound a perfect consonance - heights in ratio 1, 2, 3/2 or 4/3, or the inverse (unison, octave, fifth, fourth). At height 2 they are all castles (2^w − 1, A000225), at height 3 the 1-smooth castles (A106514, silver by width), at height 4 they grow at 3.1701, the root of x³ − 4x² + 2x + 2. Every consonance keeps the part of a height prime to 6, so A_Mersenne(w, h) = A_Mersenne(w, h₀) for h₀ the largest divisor of h of the form 2^a 3^b (only the flat castles at h = 5, 7, 11, …). On the heights 2^i 3^j the rule is the triangular lattice with a loop at each point, since a fourth and a fifth make an octave. The Mersenne castles of height h grow by width at ρ_cons(h₀), the largest eigenvalue of the rule on the heights 2^i 3^j ≤ h₀, which is below 7 and tends to 7, with 7 − ρ_cons(h₀) = O(1/log h₀).
tags: [concept, castle, mersenne-castle, transfer-matrix, consonance, music, 3-smooth-numbers, triangular-lattice, perron-root, block-count, parity, silver, oeis, verification]
sources: [project-euler-502-brute-force]
created: 2026-10-28
updated: 2026-10-29
---

# Mersenne castles

## Definition

The first of Mersenne's laws, published in *Harmonie universelle* (1636), says that the frequency of a stretched string is inversely proportional to its length; the relation is older and is credited to Pythagoras.[^mersenne] Read each column of a castle as a string whose length is the column's height. Two neighboring columns of heights `a` and `b` then sound the interval with frequency ratio `b : a`, the shorter column the higher note. The perfect consonances are the unison, the octave, the fifth and the fourth,[^consonance] with frequency ratios `1 : 1`, `2 : 1`, `3 : 2` and `4 : 3`.[^pythagoras]

A castle of width `w` and height `h` is a skyline `(c_1, …, c_w)` with `1 ≤ c_i ≤ h` and some `c_i = h` ([[castle-polyomino](pages/castle-polyomino.md)]). The **consonance rule** lets a column of height `a` stand next to a column of height `b` when `b/a` is one of the seven ratios

```
1  (unison),    2, 1/2  (octave),    3/2, 2/3  (fifth),    4/3, 3/4  (fourth).        (1)
```

A **Mersenne castle** is a castle whose neighboring columns all obey the consonance rule. `A_Mersenne(w, h)` is the number of Mersenne castles of width `w` and height `h`, and `A^e_Mersenne(w, h)` and `A^o_Mersenne(w, h)` count those with an even and with an odd number of blocks ([[castle-notation](pages/castle-notation.md)]).

The rule takes the four perfect consonances within an octave and none of their compounds: the heights 1 and 3 sound a twelfth, an octave and a fifth together, and may not stand side by side. The major third `5 : 4`, an imperfect consonance,[^consonance] is not in the rule either.

*Example.* The skyline `(2, 3, 4, 2, 1)` is a Mersenne castle of height 4. Its steps are a fifth (`3/2`), a fourth (`4/3`), an octave (`2/4`) and an octave (`1/2`), and it has 4 blocks:

```
(2, 3, 4, 2, 1)

  . . # . .
  . # # . .
  # # # # .
  # # # # #
```

No Mersenne castle has neighboring columns of heights 1 and 3, or 4 and 5.[^exec2]

## Counting by transfer matrix

On the heights `1, …, h` the consonance rule is the symmetric `h × h` matrix `M_cons(h)`, with a 1 in row `a` and column `b` when `b/a` is in the list (1). At `h = 4`:

```
          1  2  3  4
     1  [ 1  1  0  0 ]
     2  [ 1  1  1  1 ]
     3  [ 0  1  1  1 ]
     4  [ 0  1  1  1 ]
```

Entry `(a, b)` of `M_cons(h)^{w−1}` counts the skylines of width `w` with every column in `{1, …, h}`, first column `a` and last column `b`, whose neighboring columns obey the rule. Such a skyline is a Mersenne castle of height `h` exactly when some column reaches `h`, so subtracting those with every column below `h` leaves

```
A_Mersenne(w, h)  =  𝟙ᵀ M_cons(h)^{w−1} 𝟙  −  𝟙ᵀ M_cons(h − 1)^{w−1} 𝟙,        (2)
```

with `𝟙` the all-ones vector.

The list (1) has seven ratios, so a height has at most 7 consonant heights. A height `a` has all seven exactly when `a/2`, `2a/3` and `3a/4` are whole numbers, that is, when 12 divides `a`: the height 12 is consonant with 6, 8, 9, 12, 16, 18 and 24.[^exec1]

## Heights 2, 3 and 4

- **Height 2.** The pairs `(1, 1)`, `(1, 2)`, `(2, 2)` are a unison, an octave and a unison, so every castle of height 2 is a Mersenne castle, and `A_Mersenne(w, 2) = A(w, 2) = 2^w − 1`, A000225(`w`).
- **Height 3.** The heights 1 and 2 are an octave apart and 2 and 3 a fifth, while 1 and 3 are a twelfth apart. So on `{1, 2, 3}` the consonance rule is `|a − b| ≤ 1`, the 1-smooth rule, and the Mersenne castles of height 3 are exactly the 1-smooth castles of height 3, with any first column ([[1-smooth-castles](pages/1-smooth-castles.md)]). They number A106514(`w − 1`) `= 1, 3, 9, 25, 67, 175, 449, …` ([[pell-castle](pages/pell-castle.md)]), with generating function `Σ_w A_Mersenne(w, 3) x^w = x(1 − x)/((1 − 2x)(1 − 2x − x²))`.[^a106514] The characteristic polynomial of `M_cons(3)` is `(x − 1)(x² − 2x − 1)`, and the Mersenne castles of height 3 are silver by width, growing at `δ_2 = 1 + √2` ([[metallic-means](pages/metallic-means.md)]).
- **Height 4.** The octave `2 : 4` and the fourth `3 : 4` join the rule; the heights 1 and 4 (two octaves) and 1 and 3 are not consonant. The characteristic polynomial of `M_cons(4)` is `x(x³ − 4x² + 2x + 2)`, and the generating function is

```
Σ_w A_Mersenne(w, 4) x^w  =  x(1 − x) / ((1 − 2x − x²)(1 − 4x + 2x² + 2x³)).
```

The Mersenne castles of height 4 grow at `3.17008…` by width, the largest root of `x³ − 4x² + 2x + 2`; the factor `1 − 2x − x²` comes from the second term of Equation (2).[^exec3]

## Octaves and fifths: the classes of heights

Every ratio in the list (1) is `2^i 3^j` for integers `i` and `j`. The heights of the form `2^i 3^j` are the 3-smooth numbers, A003586, which Philippe de Vitry called harmonic numbers in the fourteenth century.[^vitry] (This sense of smooth, no prime factor above 3, is unrelated to the 1-smooth castles.) Write `𝒱(n)` for the set of heights `2^i 3^j ≤ n`.

**Theorem 1.** In `{1, …, h}`, a chain of consonant heights joins `a` to `b` exactly when `a` and `b` have the same part `m` prime to 6. The class of the heights with part `m` is `m · 𝒱(⌊h/m⌋)`.

*Proof.* Each ratio in the list (1) is a product of powers of 2 and 3, so a consonance keeps the part of a height prime to 6. Conversely, `m · 2^i 3^j` is joined to `m` by steps that never rise above it: halve down to `m · 3^j` by octaves, then go from `m · 3^k` to `m · 2 · 3^{k−1}` by a fifth and to `m · 3^{k−1}` by an octave, until `m` is reached. ∎

**Theorem 2.** Write `h = m · h₀`, with `h₀ = 2^a 3^b` and `m` prime to 6. Then `A_Mersenne(w, h) = A_Mersenne(w, h₀)`, and the same holds for `A^e_Mersenne` and `A^o_Mersenne`.

*Proof.* A Mersenne castle of height `h` has a column of height `h`, and every column is joined to it by a chain of consonances, so by Theorem 1 every column lies in `m · 𝒱(h₀)`. Dividing every column by `m` keeps the consonance rule, which depends only on ratios, and gives a Mersenne castle of height `h₀`; multiplying by `m` reverses it. The block count is `blocks(c) = c_1 + Σ_{i=2}^{w} max(0, c_i − c_{i−1})`,[^blocks] so multiplying every column by `m` multiplies the block count by `m`, which is odd, and keeps its parity. ∎

So the Mersenne castles of height 5, or of any height prime to 6, are the flat castles `(h, …, h)`, one at each width. The Mersenne castles of height 10 are the `2^w − 1` skylines on `{5, 10}` that reach 10, as at height 2, and height 60 counts as height 12.[^exec4] It suffices to count at the heights `2^a 3^b`:

| `h₀` | `A_Mersenne(w, h₀)`, `w = 1, …, 10` |
|---|---|
| 1 | `1, 1, 1, 1, 1, 1, 1, 1, 1, 1` |
| 2 | `1, 3, 7, 15, 31, 63, 127, 255, 511, 1023` |
| 3 | `1, 3, 9, 25, 67, 175, 449, 1137, 2851, 7095` |
| 4 | `1, 5, 21, 79, 281, 965, 3239, 10703, 34981, 113433` |
| 6 | `1, 5, 23, 101, 423, 1717, 6815, 26605, 102559, 391477` |
| 8 | `1, 5, 25, 119, 547, 2447, 10727, 46301, 197439, 833797` |
| 9 | `1, 3, 13, 57, 255, 1131, 4977, 21733, 94289, 406821` |
| 12 | `1, 7, 39, 205, 1041, 5155, 25043, 119855, 566869, 2655597` |

Every entry agrees with brute-force enumeration.[^exec7]

## The triangular lattice of octaves and fifths

Write the height `2^i 3^j` as the point `(i, j)`. The octave up is the step `(1, 0)`, the fifth up, `×3/2`, is `(−1, 1)`, and the fourth up, `×4/3`, is `(2, −1)`. An octave is a fourth and a fifth,[^philolaus] and so the fourth step is the octave step minus the fifth step. With `u` the octave step and `v` the fifth step, the six steps other than the unison are `±u`, `±v` and `±(u − v)`, the six neighbors of a point of the triangular lattice. On the heights `2^i 3^j` the consonance rule is therefore the triangular lattice with a loop at each point, the unison. `𝒱(h)` is the set of lattice points in the triangle `i ≥ 0`, `j ≥ 0`, `i ln 2 + j ln 3 ≤ ln h`, and the rule on `𝒱(h)` joins two of them exactly when the lattice does.

At `h = 32`, with `2^i 3^j` placed at column `2i + 3j` and row `j`, so that the octave runs across, the fifth up and to the right, and the fourth down and to the right:

```
                           27
                         /
                  9  -- 18
                /  \  /  \
         3  -- 6  -- 12 -- 24
       /  \  /  \  /  \  /  \
1  -- 2  -- 4  -- 8  -- 16 -- 32
```

The number of heights in `𝒱(h)` is A071521(`h`), which grows like `(ln h)²/(2 ln 2 ln 3)`.[^a071521] The height `n = 2^i 3^j` has all seven consonant heights inside `𝒱(h)` exactly when `i ≥ 2`, `j ≥ 1` and `2n ≤ h`: the six heights other than `n` are whole numbers exactly when `i ≥ 2` and `j ≥ 1` (`3n/4` needs `i ≥ 2`, and `2n/3` and `4n/3` need `j ≥ 1`), and they are at most `h` exactly when the largest, `2n`, is. The other heights lie along the edges of the triangle.[^exec5]

## Spectrum and growth

Write `ρ_cons(n)` for the largest eigenvalue of the consonance rule on the heights `𝒱(n)`.

**Theorem 3.** The Mersenne castles of height `h` grow at `ρ_cons(h₀)` by width.

*Proof.* By Theorem 2 the castles of height `h` are counted as those of height `h₀`. Their columns lie in `𝒱(h₀)` and some column reaches `h₀`, so as in Equation (2), `A_Mersenne(w, h₀) = 𝟙ᵀ M^{w−1} 𝟙 − 𝟙ᵀ M′^{w−1} 𝟙`, with `M` the rule on `𝒱(h₀)` and `M′` the rule on `𝒱(h₀)` without `h₀`. `M` is irreducible by Theorem 1 and has 1s on its diagonal, so by the Perron-Frobenius theorem `𝟙ᵀ M^{w−1} 𝟙` grows like a positive multiple of `ρ_cons(h₀)^w`. `M′` is a proper principal submatrix of an irreducible nonnegative matrix, so its largest eigenvalue is strictly smaller. ∎

The factor of the characteristic polynomial that has `ρ_cons(h₀)` as a root, irreducible over the rationals:[^exec6]

| `h₀` | `\|𝒱(h₀)\|` | factor | `ρ_cons(h₀)` |
|---|---|---|---|
| 2 | 2 | `x − 2` | `2` |
| 3 | 3 | `x² − 2x − 1` | `1 + √2 = 2.41421…` |
| 4 | 4 | `x³ − 4x² + 2x + 2` | `3.17008…` |
| 6 | 5 | `x⁴ − 5x³ + 4x² + 4x − 2` | `3.64118…` |
| 8 | 6 | `x⁵ − 5x⁴ + 2x³ + 8x² + x − 1` | `3.98093…` |
| 9 | 7 | `x⁵ − 6x⁴ + 6x³ + 10x² − 8x − 6` | `4.05356…` |
| 12 | 8 | `x⁶ − 8x⁵ + 16x⁴ + 6x³ − 31x² + 2x + 15` | `4.41199…` |
| 16 | 9 | degree 7 | `4.58118…` |
| 18 | 10 | degree 10 | `4.70938…` |
| 24 | 11 | degree 8 | `4.94225…` |
| 27 | 12 | degree 8 | `4.96089…` |
| 32 | 13 | degree 12 | `5.04571…` |

**Theorem 4.** For every height `h = 2^a 3^b`, `ρ_cons(h) < 7`, and for `h ≥ 2`

```
7 − ρ_cons(h)  ≤  12 (log₂ h + 3 log₃ h + 4) / (log₂ h · log₃ h).                (3)
```

So the growth of the Mersenne castles of height `h = 2^a 3^b` by width tends to 7, with `7 − ρ_cons(h) = O(1/log h)`. By Theorem 3, at every height the growth is `ρ_cons(h₀) < 7`; it tends to 7 along every sequence of heights whose part `h₀` tends to infinity, and it is 1 at every height prime to 6.

*Proof.* *Upper bound.* The largest eigenvalue of an irreducible nonnegative matrix is at most its largest row sum, and equals it only when all row sums are equal. Each row of the rule on `𝒱(h)` sums to at most 7, by the list (1), and the row of the height 1 sums to at most 2, so `ρ_cons(h) < 7`.

*Lower bound.* The rule is symmetric, so `ρ_cons(h) ≥ 𝟙ᵀ M 𝟙 / 𝟙ᵀ 𝟙`, the average number `d̄(h)` of consonant heights within `𝒱(h)`. Let `D(h)` be the heights of `𝒱(h)` with fewer than 7. By the criterion of the last section, `n = 2^i 3^j` is in `D(h)` only when `i ≤ 1`, `j = 0`, or `2n > h`. At most `2(log₃ h + 1)` heights have `i ≤ 1` and at most `log₂ h + 1` have `j = 0`, and for each `j` at most one `i` has `2^i 3^j ≤ h < 2^{i+1} 3^j`, so at most `log₃ h + 1` heights are of the last kind. Hence `|D(h)| ≤ log₂ h + 3 log₃ h + 4`. Each height of `D(h)` keeps its unison and loses at most 6 consonant heights, so `d̄(h) ≥ 7 − 6 |D(h)| / |𝒱(h)|`.

*Counting.* The unit squares `[i, i+1) × [j, j+1)` with corner `(i, j)` in the triangle cover the triangle, so `|𝒱(h)|` is at least its area, `(ln h)²/(2 ln 2 ln 3) = ½ log₂ h · log₃ h`. Combining the three bounds gives Inequality (3). ∎

Inequality (3) is far from the truth:[^exec6]

| `h` | `\|𝒱(h)\|` | `\|D(h)\|` | `d̄(h)` | `ρ_cons(h)` | `(7 − ρ_cons(h))(ln h)²` | Inequality (3) |
|---|---|---|---|---|---|---|
| `2^5` | 13 | 12 | `4.385` | `5.04571` | `23.47` | `14.05` |
| `2^7` | 22 | 18 | `5.000` | `5.68014` | `31.07` | `9.41` |
| `2^10` | 41 | 27 | `5.488` | `6.19481` | `38.69` | `6.26` |
| `2^16` | 95 | 44 | `5.968` | `6.61288` | `47.61` | `3.74` |
| `2^20` | 143 | 55 | `6.175` | `6.73312` | `51.29` | `2.94` |
| `2^30` | 309 | 84 | `6.430` | `6.86873` | `56.76` | `1.92` |
| `2^40` | 538 | 113 | `6.561` | `6.92237` | `59.68` | `1.42` |

At `h = 2^40`, `7 − ρ_cons(h) = 0.078` and the bound gives `1.42`. The exact rate of `7 − ρ_cons(h)` is open; the column `(7 − ρ_cons(h))(ln h)²` is still rising at `h = 2^40`.

## Blocks

By Theorem 2 the even-block and odd-block counts at every height are those at the heights `2^a 3^b`. For `w = 1, …, 10`:[^exec7]

| `h₀` | `A^e_Mersenne(w, h₀)` | `A^o_Mersenne(w, h₀)` |
|---|---|---|
| 2 | `1, 3, 6, 10, 16, 28, 56, 120, 256, 528` | `0, 0, 1, 5, 15, 35, 71, 135, 255, 495` |
| 3 | `0, 0, 1, 7, 29, 91, 243, 597, 1433, 3483` | `1, 3, 8, 18, 38, 84, 206, 540, 1418, 3612` |
| 4 | `1, 5, 18, 56, 169, 523, 1671, 5421, 17603, 56905` | `0, 0, 3, 23, 112, 442, 1568, 5282, 17378, 56528` |
| 6 | `1, 5, 20, 72, 256, 942, 3568, 13634, 51956, 196958` | `0, 0, 3, 29, 167, 775, 3247, 12971, 50603, 194519` |
| 8 | `1, 5, 25, 109, 445, 1771, 7025, 28049, 112940, 457788` | `0, 0, 0, 10, 102, 676, 3702, 18252, 84499, 376009` |
| 9 | `0, 0, 1, 9, 65, 373, 1898, 9056, 41631, 186785` | `1, 3, 12, 48, 190, 758, 3079, 12677, 52658, 220036` |

Every entry agrees with brute-force enumeration. The row `h₀ = 2` is the even-block and odd-block split of all castles of height 2.

## Related Concepts

- [[1-smooth-castles](pages/1-smooth-castles.md)], [[pell-castle](pages/pell-castle.md)] - the 1-smooth rule, which is the consonance rule on the heights 1, 2, 3; the 1-smooth castles of height 3 with any first column, A106514.
- [[metallic-means](pages/metallic-means.md)] - the silver mean `δ_2 = 1 + √2`, the growth of the Mersenne castles of height 3.
- [[castle-classification-shape](pages/castle-classification-shape.md)] - the Mersenne type among the rate-of-change types.
- [[castle-classification-growth](pages/castle-classification-growth.md)] - growth types by width; the Mersenne castles of height 4 grow at the cubic `3.17008…`.
- [[castle-notation](pages/castle-notation.md)] - `M_cons(h)`, `A_Mersenne(w, h)`, `h₀`, `𝒱(n)` and `ρ_cons(n)`.

## Footnotes

[^mersenne]: https://en.wikipedia.org/wiki/Mersenne%27s_laws (read 2026-10-28) - "The equation was first proposed by French mathematician and music theorist Marin Mersenne in his 1636 work Harmonie universelle."; "The natural frequency is: a) Inversely proportional to the length of the string (the law of Pythagoras)"; and, quoting Gozza, "Mersenne investigated and refined these relationships by experiment but did not himself originate them".
[^consonance]: https://en.wikipedia.org/wiki/Consonance_and_dissonance (read 2026-10-28) §Definitions, Music theory - "Perfect consonances: unisons and octaves, perfect fourths and perfect fifths"; "Imperfect consonances: major thirds and minor sixths, minor thirds and major sixths".
[^pythagoras]: https://en.wikipedia.org/wiki/Musical_system_of_ancient_Greece (read 2026-10-28) §The Pythagoreans - "Pythagoras construed the intervals arithmetically, allowing for 1:1 = Unison, 2:1 = Octave, 3:2 = Fifth, 4:3 = Fourth."
[^philolaus]: https://en.wikipedia.org/wiki/Musical_system_of_ancient_Greece (read 2026-10-28) §The Pythagoreans - "Philolaus recognizes that, if the interval of a fourth goes up from any given note, and then up the interval of a fifth, the final note is an octave above the first note. Thus, the octave is made up of a fourth and a fifth."
[^vitry]: https://oeis.org/A003586 (read 2026-10-28) - "3-smooth numbers: numbers of the form 2^i*3^j with i, j >= 0.", comment "These numbers were once called "harmonic numbers", see Lenstra links. - _N. J. A. Sloane_, Jul 03 2015"; and I. Peterson, "Medieval Harmony", Science News MathTrek (1999-01-23), https://web.archive.org/web/20130930182203/http://www.sciencenews.org/pages/sn_arc99/1_23_99/mathland.htm (read 2026-10-28) - "Philippe de Vitry (1291-1361) was one of the most prominent figures in medieval music." and "One of de Vitry's observations concerned numbers that can be written as a power of 2 multiplied by a power of 3. ... He called them harmonic numbers."
[^a106514]: https://oeis.org/A106514 (read 2026-10-28) - "Expansion of (1-x)/((1-2*x)*(1-2*x-x^2)).", data `1, 3, 9, 25, 67, 175, 449, 1137, 2851, …`, offset 0.
[^a071521]: https://oeis.org/A071521 (read 2026-10-28) - "Number of 3-smooth numbers <= n."; formula "Asymptotically: let a=1/(2*log(2)*log(3)), b=sqrt(6), then from Ramanujan a(n) ~ a*log(2*n)*log(3*n) or equivalently a(n) ~ a*log(b*n)^2."
[^blocks]: [[project-euler-502-brute-force](pages/project-euler-502-brute-force.md)] §"Column-height encoding" L24 - "= c_1 + \sum_{i=2}^{w} \max(0, c_i - c_{i-1})", the column-height block-count formula.
[^exec1]: Verified by execution (Python 3.11 with SymPy, 2026-10-28): `bin/python/mersenne_castles.py` item [1], run log `bin/python/mersenne_castles-run.log`. `M_cons(4)`; symmetry for `h ≤ 400`; at most 7 consonant heights, and 7 exactly when 12 divides the height, for heights up to 400.
[^exec2]: Verified by execution (Python 3.11, 2026-10-28): `bin/python/mersenne_castles.py` item [2], run log `bin/python/mersenne_castles-run.log`. The example, its steps, drawing and block count; the pairs `(1, 3)` and `(4, 5)` break the rule.
[^exec3]: Verified by execution (Python 3.11, 2026-10-28): `bin/python/mersenne_castles.py` item [3], run log `bin/python/mersenne_castles-run.log`. Every castle of height 2 obeys the rule for `w ≤ 14`, and `A_Mersenne(w, 2) = 2^w − 1` for `w ≤ 40`; the rule on `{1, 2, 3}` is the 1-smooth rule, and `A_Mersenne(w, 3) = A106514(w − 1)` on all 28 terms of the data field; the characteristic polynomials at `h = 3, 4`; the generating function at `h = 4` for `w ≤ 60`; `A_Mersenne(401, h)/A_Mersenne(400, h)` equals `1 + √2` and `3.170086486626` at `h = 3, 4`.
[^exec4]: Verified by execution (Python 3.11, 2026-10-28): `bin/python/mersenne_castles.py` item [4], run log `bin/python/mersenne_castles-run.log`. The classes of Theorem 1 for every `h ≤ 300`; Theorem 2 for the counts and the signed counts at `h ≤ 72`, `w ≤ 8`; the heights 5, 10 and 60; `blocks(m c) = m · blocks(c)` for `m = 5, 7` on the Mersenne castles of height 6 with `w ≤ 6`.
[^exec5]: Verified by execution (Python 3.11, 2026-10-28): `bin/python/mersenne_castles.py` item [5], run log `bin/python/mersenne_castles-run.log`. The exponent steps of the six consonances and the identity fourth = octave − fifth; `|𝒱(h)| = A071521(h)` on all 75 terms of the data field; the drawing at `h = 32`; the criterion for seven consonant heights for every `h = 2^a 3^b ≤ 2^20`.
[^exec6]: Verified by execution (Python 3.11 with SymPy, 2026-10-28): `bin/python/mersenne_castles.py` item [6], run log `bin/python/mersenne_castles-run.log`. The characteristic polynomials, factored over the rationals by SymPy, and `ρ_cons(h₀)` by Collatz-Wielandt bounds to `10^{−13}`; the table of the bound (3); `d̄(h) ≤ ρ_cons(h) < 7`, `|D(h)| ≤ log₂ h + 3 log₃ h + 4` and `|𝒱(h)| ≥ ½ log₂ h · log₃ h` for every `h = 2^a 3^b ≤ 10^6` and the table rows; `A_Mersenne(1001, h)/A_Mersenne(1000, h)` equals `ρ_cons(h₀)` to ten decimals at `h = 4, 5, 6, 10, 12, 24, 30, 36`.
[^exec7]: Verified by execution (Python 3.11, 2026-10-28): `bin/python/mersenne_castles.py` item [7], run log `bin/python/mersenne_castles-run.log`. A depth-first search over the consonant heights, counting blocks by the block-count formula, against Equation (2) and the signed transfer matrix for `h ∈ {1, 2, 3, 4, 6, 8, 9, 12}` and `w ≤ 10`; the search against every skyline in `{1, …, h}^w` with `h^w ≤ 300000`.
