---
title: "The Pell castle strip - from an AC exercise to the silver ratio in castle space"
category: Analyses
summary: A seminar-shaped analysis. Start with an Analytic Combinatorics end-of-chapter exercise - "extract the recurrence from D(x) = 1/(1−2x−x²)" - read it as a two-atom tiling scheme, and find the castle strip whose width generating function is exactly D(x) - 1-smooth skylines of height at most 3 anchored at the base, counted by the Pell numbers, with silver-ratio growth.
tags: [analysis, castle, pell, generating-functions, coefficient-matching, seminar, pedagogy, silver-ratio, transfer-matrix]
sources: [pe502-pell-castle-strip]
created: 2026-09-15
updated: 2026-09-19
---

# The Pell castle strip - from an Analytic Combinatorics (AC) exercise to the silver ratio in castle space

## The pedagogy is the point

An Analytic Combinatorics (AC) chapter closes with an exercise that looks like nothing: **given the generating function `D(x) = 1/(1 − 2x − x²)`, produce the recurrence and its base cases**. It is a five-line calculation. But it is also the doorway to a seminar on Project Euler (PE) 502 castles: the rational function is a two-atom tiling scheme, its coefficients are the Pell numbers, its growth constant is the silver ratio the wiki already tracks, and there is a castle sub-family - the 1-smooth strip of height at most 3, anchored at the base - whose width generating function is exactly this `D(x)`. Ninety minutes of blackboard from one line of a textbook.

This page is that seminar in written form. It runs a slightly larger loop than the underlying working note [[pe502-pell-castle-strip](pages/pe502-pell-castle-strip.md)] to make each step teachable: the "where does the base case come from" resolution, the two-atom composition scheme, the transfer matrix that realizes it, the silver-ratio thread. The point is not the answer (a rational function and a Pell recurrence). The point is that **a textbook end-of-chapter question about extracting a recurrence spirals into polyomino theory** if you ask what its atoms are counting.

## Act I - Coefficient matching, and where the "base cases" hide

The exercise: given

```
D(x) = 1/(1 − 2x − x²)  =  ∑_{i≥0} a_i · x^i,
```

find the recurrence for `a_n` and its base cases. Multiply through:

```
(1 − 2x − x²) · D(x)  =  1.
```

The left side is a product of two power series; each coefficient of `x^n` on the right must match the corresponding coefficient on the left. Coefficient extraction is mechanical:[^1]

- `[x^0]`: `a_0 = 1`.
- `[x^1]`: `a_1 − 2·a_0 = 0`, so `a_1 = 2`.
- `[x^{n+2}]` for `n ≥ 0`: `a_{n+2} − 2·a_{n+1} − a_n = 0`.

The **"base cases" have no independent existence**. Written uniformly with the "negative index equals zero" convention (a power series has no negative powers), the recurrence and the boundary are the same object:[^1]

```
a_n − 2·a_{n−1} − a_{n−2}  =  [n = 0],       a_{−1} = a_{−2} = 0.
```

At `n = 0`, this reads `a_0 − 2·0 − 0 = 1`, so `a_0 = 1`. At `n = 1`, it reads `a_1 − 2·a_0 − 0 = 0`, so `a_1 = 2`. **Base cases are the recurrence evaluated at the boundary.** The "special-case argument" a student expects at the start never appears because it was never needed.

**Why this matters for the wiki.** The [[castle-counting-formula](pages/castle-counting-formula.md)] carries recurrences whose base cases *look* argued for, but under the same coefficient-matching lens they are the recurrence evaluated at `k = 0` or `L = 0` with zeros substituted. The technique is the shortcut, and it is recorded on [[generating-functions](pages/generating-functions.md)] as the general GF-to-recurrence method.

## Act II - Two-atom composition: what is the rational function counting?

`1/(1 − 2x − x²)` is one of the simplest **rational** generating functions after the geometric series `1/(1 − x)` and its weighted cousin `1/(1 − 2x)`. Read symbolically: it is a `SEQ` (sequence) construction (see [[symbolic-method](pages/symbolic-method.md)]) over two atoms combined into an alphabet of weight `2x + x²`.[^2]

- **Width-1 atom of weight 2** - the `2x` term. Two distinguishable copies of a size-1 building block.
- **Width-2 atom of weight 1** - the `x²` term. One copy of a size-2 building block.

Any word `a_1 a_2 … a_k` over this alphabet has total weight `2^{#(width-1 atoms)}` and total width `∑ |a_i| = n`, and the generating function `∑_{words} (weight)·(x^{width})` is exactly `∑_k (2x + x²)^k = 1/(1 − 2x − x²)`. So `a_n` is the total weight of all strip tilings of length `n` under this alphabet. The recurrence `a_n = 2·a_{n−1} + a_{n−2}` is the "peel off the last atom" argument: either the strip ends in a width-1 atom (2 choices, leaving a strip of length `n−1`) or in a width-2 atom (1 choice, leaving `n−2`).[^2]

## Act III - The castle strip: 1-smooth, height at most 3, anchored at the base

A castle strip is a skyline read left to right under a neighbor rule, and the rule is an `h × h` 0/1 transfer matrix whose states are the column heights ([[castle-strip](pages/castle-strip.md)]). Take the **1-smooth** rule on heights `{1, 2, 3}`: adjacent columns differ in height by at most 1 (`|c_{i+1} − c_i| ≤ 1`, the Motzkin-flavoured Axis-2 predicate of [[castle-classification-geometric](pages/castle-classification-geometric.md)]). Its transfer matrix and characteristic polynomial are

```
        to 1  to 2  to 3
from 1 [  1     1     0  ]
from 2 [  1     1     1  ]          det(xI − M) = (x − 1)(x² − 2x − 1)
from 3 [  0     1     1  ]
```

so the growth constant is `1 + √2`. The count depends on the boundary condition, and the boundary is where the exercise's `D(x)` appears:[^4]

| strips of width `w`, 1-smooth on `{1,2,3}` | `w = 1, 2, 3, …` | width generating function | sequence |
|---|---|---|---|
| **first column at height 1** (anchored at the base) | `1, 2, 5, 12, 29, 70, 169, 408` | `1/(1 − 2x − x²)` | **Pell `P_{w+1}`**, A000129 |
| any first column | `3, 7, 17, 41, 99, 239, 577, 1393` | `(3 + x)/(1 − 2x − x²)` | companion Pell, A001333 |
| first and last column at height 1 | `1, 1, 2, 4, 9, 21, 50, 120` | `(1 − 2x)/((1 − x)(1 − 2x − x²))` | unchecked against Online Encyclopedia of Integer Sequences (OEIS) |

The anchored row is the **Pell castle strip**: `e_1ᵀ (I − xM)^{−1} 𝟙 = 1/(1 − 2x − x²)` exactly, the `(1 − x)` factor of the free strip's denominator cancelling against the numerator when the walk starts at height 1. So the two atoms of Act II count castles: `a_w` is the number of skylines of width `w` that start on the base, never jump by more than one row, and never exceed height 3. Anchoring at the base is natural for a castle (the skyline begins where the bottom block begins), and it is what selects Pell proper rather than the companion sequence. Restricting to castles of height *exactly* 3 subtracts the height-≤2 anchored strips (`2^{w−1}` of them) and gives `P_{w+1} − 2^{w−1} = 0, 0, 1, 4, 13, 38, 105, 280, …`.

The smallest 0/1 transfer matrix with `det(I − xM) = 1 − 2x − x²` is `3×3`: over `2×2` 0/1 matrices the determinant takes only the six values `1`, `1 − x`, `1 − 2x`, `1 − x²`, `(1 − x)²`, `1 − x − x²`.[^4] The Pell strip is a height-3 object.

## Act IV - The Pell fingerprint

The counts

```
a_n  =  1, 2, 5, 12, 29, 70, 169, 408, 985, 2378, 5741, 13860, …
```

are **Pell numbers, OEIS [A000129](https://oeis.org/A000129) shifted** (`a_n = P_{n+1}`).[^3] See [[pell-numbers](pages/pell-numbers.md)] for the linear-recurrence definition and its Binet form. The dominant characteristic root of `x² − 2x − 1` is `1 + √2 ≈ 2.4142`, so `a_n ~ C · (1 + √2)^n` - the growth rate is the **silver ratio**.

`1 + √2` is not a fresh entrant; the wiki already tracks it prominently. On [[eigenvalue-continued-fractions](pages/eigenvalue-continued-fractions.md)] it is one of two **norm-`−1` reduced quadratic surds** with purely periodic continued fraction: `1 + √2 = [2; 2, 2, 2, …]`. On [[tower-word-continued-fraction](pages/tower-word-continued-fraction.md)] it is the **tower-word growth constant** - the singularity of the algebraic generating function for tower words counted by total steps sits at `√2 − 1`, growth rate `1/(√2 − 1) = √2 + 1`.

So silver has three castle faces: the tower word (algebraic generating function, A004149), the 1-smooth height-3 strip (rational, Pell or companion Pell by boundary), and the ceiling-exception rule `J − D` at height 3 ([[metallic-strip-realizability](pages/metallic-strip-realizability.md)], companion Pell `3, 7, 17, 41, …` as a free strip). Pell is what the surd `1 + √2` looks like as an integer sequence, in exactly the way Fibonacci is what `φ` looks like ([[aocp-generating-functions](pages/aocp-generating-functions.md)]); on the castle side, Fibonacci counts the height-2 tree castles ([[castle-graph](pages/castle-graph.md)]) and Pell counts the anchored 1-smooth height-3 strip.

## The seminar shape

Suggested outline for a talk:

1. **Cold open:** put `D(x) = 1/(1 − 2x − x²)` on the board and ask the audience for its recurrence. Solicit "base case" answers, then run coefficient matching to show the base cases *are* the recurrence.
2. **Act II: what is it counting?** Introduce the two-atom composition scheme. Explain the pattern `1/(1 − ∑ (weight)·x^(width))` = strip tilings under a general SEQ. This is the [[symbolic-method](pages/symbolic-method.md)] in miniature.
3. **Act III: find the castle.** Write the 1-smooth `3×3` matrix, compute `e_1ᵀ (I − xM)^{−1} 𝟙`, and watch `D(x)` appear with the `(1 − x)` cancelled. Compare the three boundary conditions. This is where the audience realizes the exercise was never abstract.
4. **Act IV: pull the growth rate.** Compute a few Pell numbers, take ratios, identify `1 + √2`. Sketch the continued-fraction expansion `[2; 2, 2, …]`. Mention Fibonacci / `φ` as the parallel case.
5. **Close:** the audience walked in expecting a five-line homework and leaves with coefficient extraction, the symbolic method, a transfer matrix, and a growth constant that is a unit of `Q(√2)`. **The exercise was the seminar.**

## The general pedagogy claim

A rational generating function's denominator is a factored inventory of atoms. Whether those atoms are the **structural rules** of a given combinatorial object is a theorem, and its proof is a bijection or a transfer matrix whose determinant reproduces the denominator. In a well-designed exercise the denominator is small and the atoms are legible; if you are lucky, a transfer matrix at another scale reproduces it exactly. The Pell castle strip is that lucky case: `1 − 2x − x²` is short, its two atoms are legible, and the anchored 1-smooth strip is the object at the other scale. This is what turns AC textbook exercises into seminars - reading the atoms, then finding the matrix.

## Appearances in Sources

- [[pe502-pell-castle-strip](pages/pe502-pell-castle-strip.md)] - the working note that seeded this seminar arc: the coefficient-matching mechanic and the two-atom reading.

## Related Concepts

- [[castle-strip](pages/castle-strip.md)] - the from-scratch bridge: what a castle strip is, and how a neighbor rule becomes a transfer matrix whose states are the column heights. Read it first if the transfer-matrix language in Act III is unfamiliar.
- [[metallic-strip-realizability](pages/metallic-strip-realizability.md)] - the 1-smooth height-3 matrix and its `(1 − x)(1 − 2x − x²)` denominator, and the `J − D` rule that realizes the whole metallic ladder.
- [[pell-numbers](pages/pell-numbers.md)] - the integer sequence and its silver-ratio growth.
- [[generating-functions](pages/generating-functions.md)] - the coefficient-matching technique and the symbolic-method context.
- [[symbolic-method](pages/symbolic-method.md)] - the `SEQ` construction the two-atom scheme is an instance of.
- [[castle-counting-formula](pages/castle-counting-formula.md)] - the wiki's rational recurrences, whose base cases the coefficient-matching lens dissolves the same way.
- [[castle-graph](pages/castle-graph.md)] - the height-2 tree castles, the Fibonacci partner of the Pell strip.
- [[eigenvalue-continued-fractions](pages/eigenvalue-continued-fractions.md)] - where `1 + √2 = [2;2,2,…]` is developed.
- [[tower-word-continued-fraction](pages/tower-word-continued-fraction.md)] - where `1 + √2` also appears, as the tower-word growth constant.
- [[aocp-generating-functions](pages/aocp-generating-functions.md)] - the Fibonacci / `φ` companion (same story with `a = 1`).
- [[castle-classification-geometric](pages/castle-classification-geometric.md)] - Axis 2 (the 1-smooth predicate); [[castle-classification-non-geometric](pages/castle-classification-non-geometric.md)] - Axis 8, for which the anchored 1-smooth strip is the canonical **silver width growth castle** example.

## Footnotes

[^1]: [[pe502-pell-castle-strip](pages/pe502-pell-castle-strip.md)] §"Where the recurrence comes from" L9-L19 - coefficient-matching mechanics, and the uniform recurrence `a_n − 2a_{n−1} − a_{n−2} = [n = 0]` with `a_{−1} = a_{−2} = 0`. Re-verified during ingest by evaluating the recurrence at the boundary and matching against direct series expansion of `1/(1−2x−x²)`.
[^2]: [[pe502-pell-castle-strip](pages/pe502-pell-castle-strip.md)] §"The castle reading" L23-L28 - the two-atom composition scheme and its "peel off the last atom" recurrence. Under the SEQ construction (see [[symbolic-method](pages/symbolic-method.md)] Theorem I.1), `SEQ(2·Z + Z²)` has ordinary generating function (OGF) `1/(1 − 2z − z²)`.
[^3]: The sequence `1, 2, 5, 12, 29, 70, 169, 408, 985, 2378, 5741, 13860` (produced by the recurrence with `a_0 = 1, a_1 = 2`) was numerically matched against OEIS A000129 = `0, 1, 2, 5, 12, 29, 70, 169, …` during ingest, confirming `a_n = P_{n+1}`. The growth ratio `a_{n+1}/a_n → 2.41421… = 1 + √2` verified for `n = 5..11`.
[^4]: Verified by execution (Python 3, SymPy), 2026-09-19. With `M = [[1,1,0],[1,1,1],[0,1,1]]` (1-smooth on heights `{1,2,3}`), `e_1ᵀ (I − xM)^{−1} 𝟙 = 1/(1 − 2x − x²)`, `𝟙ᵀ (I − xM)^{−1} 𝟙 = (3 + x)/(1 − 2x − x²)`, `e_1ᵀ (I − xM)^{−1} e_1 = (1 − 2x)/((1 − x)(1 − 2x − x²))`, and `det(xI − M) = (x − 1)(x² − 2x − 1)`. Brute-force enumeration of 1-smooth skylines over `{1,2,3}` for `w = 1..8` gives `1, 2, 5, 12, 29, 70, 169, 408` (first column 1), `3, 7, 17, 41, 99, 239, 577, 1393` (any first column), and `1, 1, 2, 4, 9, 21, 50, 120` (both end columns 1); the anchored count restricted to `max c = 3` is `0, 0, 1, 4, 13, 38, 105, 280 = P_{w+1} − 2^{w−1}`. `det(I − xM)` over all sixteen `2×2` 0/1 matrices takes exactly the six values `1, 1 − x, 1 − 2x, 1 − x², (1 − x)², 1 − x − x²`. The free-strip denominator `(1 − x)(1 − 2x − x²)` is footnote 3 of [[metallic-strip-realizability](pages/metallic-strip-realizability.md)].
