---
title: q-Catalan numbers
category: Concepts
summary: Polynomial q-analogs C_n(q) of the Catalan numbers with C_n(1) = C_n, in three families by statistic - Carlitz (inversions of Dyck words and Catalan permutations), MacMahon-Krattenthaler-Gessel (parameters of the down set), Pólya-Gessel (parallelogram polyominoes by area). Under Delest-Viennot's bijection the area of a parallelogram polyomino is the sum of the peak heights of its Dyck word; at semi-perimeter 4 the area polynomial is 4q³ + q⁴. The castles by width, blocks and area are Π/(1 − x − Π), with Π the parallelogram series.
tags: [concept, q-catalan, q-analog, catalan, dyck-words, polyomino]
sources: [algebraic-languages-and-polyominoes-enumeration]
created: 2026-09-13
updated: 2026-10-16
---

# q-Catalan numbers

## Families

The **q-Catalan numbers** are polynomial `q`-analogs `C_n(q)` of the [[catalan-numbers](pages/catalan-numbers.md)], with `C_n(1) = C_n`. Different authors track different statistics, and the source lists three families:[^1][^2]

- **Carlitz:** inversions of Dyck words and of Catalan permutations.
- **MacMahon, Krattenthaler, Gessel:** Dyck words by parameters of the down set.
- **Pólya, Gessel:** parallelogram polyominoes by area.

## Parallelogram polyominoes by area

A parallelogram polyomino is bounded by two paths of north and east steps that meet only at their ends; read by columns, the bottoms and the tops of its columns are both weakly increasing, and neighboring columns overlap ([[parallelogram-polyomino-dyck-bijection](pages/parallelogram-polyomino-dyck-bijection.md)]). Those with semi-perimeter `n + 1` number `C_n`. Delest and Viennot's bijection β sends the Dyck words of length `2n` onto them, and the area of the polyomino is the sum of the peak heights of the word.[^3] So the Pólya-Gessel family is the Dyck words graded by the sum of their peak heights. Counted by area:[^4]

| `n` | parallelogram polyominoes of semi-perimeter `n + 1`, by area |
|---|---|
| 1 | `q` |
| 2 | `2q²` |
| 3 | `4q³ + q⁴` |
| 4 | `8q⁴ + 4q⁵ + 2q⁶` |

*Example: `n = 3`.* The five parallelogram polyominoes of semi-perimeter 4 are the row of three cells, the column of three cells, the `2 × 2` square, and the two three-cell shapes in a `2 × 2` box whose columns are `[0, 0], [0, 1]` and `[0, 1], [1, 1]` in rows. β reads the column heights as peak heights and the overlaps of neighboring columns, less one, as the heights of the troughs between them, so their Dyck words are `UDUDUD`, `UUUDDD`, `UUDUDD`, `UDUUDD` and `UUDDUD`, with peak heights summing to `3, 3, 4, 3, 3`.

Counted by area alone, over all semi-perimeters, the parallelogram polyominoes of area `n` are `A006958`: `1, 2, 4, 9, 20, 46, 105, 242, …`.[^4][^5]

## Castles and related polyomino families

- **Castles.** Counted by width `u`, blocks `x` and area `q`, the castles are `Π/(1 − x − Π)`, where `Π` is the generating function of the parallelogram polyominoes at width `(1 − x)u` and height `x` ([[castle-q-bessel-closed-form](pages/castle-q-bessel-closed-form.md)]). The castles counted by area alone are the compositions of `n`, and the convex castles of area `n` are `A001523` ([[castle-by-area](pages/castle-by-area.md)]).
- **Steep polyominoes.** The steep parallelogram polyominoes, whose lower boundary has no two consecutive east steps, are counted by width, perimeter and area by a quotient of two `q`-Bessel functions. Carlitz's statistic, inversions, restricted to the steep Dyck words gives a `q`-analog of the Motzkin numbers ([[steep-polyominoes-q-motzkin-bessel](pages/steep-polyominoes-q-motzkin-bessel.md)]).
- **Convex polyominoes.** Delest and Viennot counted the convex polyominoes by perimeter (`A005436`) and posed the problem of a `q`-analog, counting by area as well; in 1984 the area was known for stack and parallelogram polyominoes.[^6] Bousquet-Mélou and Fédou gave the generating function of the convex polyominoes by width, height and area ([[bousquet-melou-fedou-1995-convex-polyominoes](pages/bousquet-melou-fedou-1995-convex-polyominoes.md)]).

## Appearances in Sources

- `raw/q-catalan-numbers.wiki` (charlesreid1.com topic page) - the three families and their statistics.
- [[algebraic-languages-and-polyominoes-enumeration](pages/algebraic-languages-and-polyominoes-enumeration.md)] - the bijection β, with area equal to the sum of the peak heights, and the open problem of a `q`-analog of the convex count.

## Related Concepts

- [[catalan-numbers](pages/catalan-numbers.md)] - `C_n = C_n(1)`.
- [[parallelogram-polyomino-dyck-bijection](pages/parallelogram-polyomino-dyck-bijection.md)] - the bijection β and its reading of area, width and overlaps.
- [[dyck-words](pages/dyck-words.md)] - the Dyck words, whose inversions give the Carlitz family and, restricted to steep words, a `q`-Motzkin family.
- [[motzkin-numbers](pages/motzkin-numbers.md)] - the Motzkin numbers, whose `q`-analogs count the steep families.
- [[steep-polyominoes-q-motzkin-bessel](pages/steep-polyominoes-q-motzkin-bessel.md)] - the steep parallelogram polyominoes by width, perimeter and area.
- [[castle-q-bessel-closed-form](pages/castle-q-bessel-closed-form.md)] - the castles by width, blocks and area through the parallelogram series and the `q`-Bessel series `J_0`, `J_1`.
- [[castle-by-area](pages/castle-by-area.md)] - the castles counted by area.
- [[permutation-inversions](pages/permutation-inversions.md)] - the inversion statistic on permutations and its generating function, the `q`-factorial `Π_{k=1}^{n} (1 − z^k)/(1 − z)`.
- [[polyominoes](pages/polyominoes.md)] - the topic page whose `q`-Bessel and `q`-Catalan statements concern the parallelogram polyominoes.
- [[q-thread-seminar](pages/q-thread-seminar.md)] - a seminar on castles by area, in which the parallelogram polyominoes (`A006958`) are one stop.

## Footnotes

[^1]: raw/q-catalan-numbers.wiki §"q-Catalan Numbers" L5 - "The q-Catalan numbers are polynomial q-analogs of the ordinary Catalan Numbers: each C_n(q) reduces to C_n at q = 1. Different authors track different statistics, so there is more than one family."
[^2]: raw/q-catalan-numbers.wiki §"q-Catalan Numbers" L7-9 - "Carlitz q-Catalan numbers count inversions of Dyck Words and Catalan permutations", "q-Catalan numbers (MacMahon, Krattenthaler, Gessel) enumerate Dyck words by parameters of the down set", "q-Catalan numbers (Polya, Gessel) count parallelogram polyominoes by area".
[^3]: [[algebraic-languages-and-polyominoes-enumeration](pages/algebraic-languages-and-polyominoes-enumeration.md)] p.183 Prop 4.1 - "The map β defined above is a bijection from Dyck words of length 2n onto parallelogram polyominoes of perimeter 2n+2. The area of P is the sum of the height of the peaks."
[^4]: Verified by execution (Python 3.11, 2026-10-16): for `n ≤ 7`, the parallelogram polyominoes of semi-perimeter `n + 1` counted by area equal the Dyck words of length `2n` counted by the sum of their peak heights (totals `C_n` up to 429); the parallelogram polyominoes of area `n ≤ 12` against `A006958`.
[^5]: https://oeis.org/A006958 (read 2026-10-16) - "Number of parallelogram polyominoes with n cells (also called staircase polyominoes, although that term is overused)", data "1, 2, 4, 9, 20, 46, 105, 242, 557, 1285, 2964, 6842, …".
[^6]: [[algebraic-languages-and-polyominoes-enumeration](pages/algebraic-languages-and-polyominoes-enumeration.md)] p.204 §12(8) - "A major problem would be to introduce the area of the polyomino in our computation. This has been done for stack polyominoes [42] and parallelogram polyominoes [30, 12, 18] ... The problem is to make a q-analog of what we have done."
