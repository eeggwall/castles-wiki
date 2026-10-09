---
title: "The Pell castle strip - from an AC exercise to the silver ratio in castle space"
category: Analyses
summary: A seminar-shaped analysis. Start with an Analytic Combinatorics end-of-chapter exercise - "extract the recurrence from D(x) = 1/(1−2x−x²)" - read it as a two-atom tiling scheme, and find the castle strip whose width generating function is exactly D(x) - 1-smooth skylines of height at most 3 anchored at the base, counted by the Pell numbers, with silver-ratio growth.
tags: [analysis, castle, pell, generating-functions, coefficient-matching, seminar, pedagogy, silver-ratio, transfer-matrix]
sources: [pe502-pell-castle-strip, barry-2005-catalan-transform]
created: 2026-09-15
updated: 2026-10-08
---

# The Pell castle strip - from an Analytic Combinatorics (AC) exercise to the silver ratio in castle space

## Overview

An Analytic Combinatorics (AC) chapter ends with an exercise: **given the generating function `D(x) = 1/(1 − 2x − x²)`, produce the recurrence and its base cases**. It is a five-line calculation, and it leads to Project Euler (PE) 502 castles: the rational function is a two-atom tiling scheme, its coefficients are the Pell numbers, its growth constant is the silver ratio the wiki already tracks, and there is a castle sub-family - the 1-smooth strip of height at most 3, anchored at the base - whose width generating function is exactly this `D(x)`.

The strip need not reach height 3; the strips that do are the Pell castles, a castle type of exact height 3 ([[pell-castle](pages/pell-castle.md)]). This page is a seminar built on that exercise. It extends the working note [[pe502-pell-castle-strip](pages/pe502-pell-castle-strip.md)]: where the base cases come from, the two-atom composition scheme, the transfer matrix that realizes it, and the silver ratio.

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

The **base cases are part of the recurrence**. Written uniformly with the "negative index equals zero" convention (a power series has no negative powers), the recurrence and the boundary are the same object:[^1]

```
a_n − 2·a_{n−1} − a_{n−2}  =  [n = 0],       a_{−1} = a_{−2} = 0.
```

At `n = 0`, this reads `a_0 − 2·0 − 0 = 1`, so `a_0 = 1`. At `n = 1`, it reads `a_1 − 2·a_0 − 0 = 0`, so `a_1 = 2`. **Base cases are the recurrence evaluated at the boundary.**

**Castle recurrences.** The `L`-direction recurrences on [[castle-counting-formula](pages/castle-counting-formula.md)] come from `den_k · P_k = num_k` the same way: matching coefficients gives the recurrence for `n` past the degree of `num_k` and the initial terms below it. The method is recorded on [[generating-functions](pages/generating-functions.md)] as the general GF-to-recurrence method.

## Act II - Two-atom composition: what is the rational function counting?

Read symbolically, `1/(1 − 2x − x²)` is a `SEQ` (sequence) construction (see [[symbolic-method](pages/symbolic-method.md)]) over two atoms combined into an alphabet of weight `2x + x²`.[^2]

- **Width-1 atom of weight 2** - the `2x` term. Two distinguishable copies of a size-1 building block.
- **Width-2 atom of weight 1** - the `x²` term. One copy of a size-2 building block.

Any word `a_1 a_2 … a_k` over this alphabet has total weight `2^{#(width-1 atoms)}` and total width `∑ |a_i| = n`, and the generating function `∑_{words} (weight)·(x^{width})` is exactly `∑_k (2x + x²)^k = 1/(1 − 2x − x²)`. So `a_n` is the total weight of all strip tilings of length `n` under this alphabet. The recurrence `a_n = 2·a_{n−1} + a_{n−2}` is the "peel off the last atom" argument: either the strip ends in a width-1 atom (2 choices, leaving a strip of length `n−1`) or in a width-2 atom (1 choice, leaving `n−2`).[^2]

## Act III - The castle strip: 1-smooth, height at most 3, anchored at the base

A castle strip is a skyline read left to right under a neighbor rule, and the rule is an `h × h` 0/1 transfer matrix whose states are the column heights ([[castle-strip](pages/castle-strip.md)]). Take the **1-smooth** rule on heights `{1, 2, 3}`: adjacent columns differ in height by at most 1 (`|c_{i+1} − c_i| ≤ 1`, the Axis-2 predicate of [[castle-classification-shape](pages/castle-classification-shape.md)]). Its transfer matrix and characteristic polynomial are

```
        to 1  to 2  to 3
from 1 [  1     1     0  ]
from 2 [  1     1     1  ]          det(xI − M) = (x − 1)(x² − 2x − 1)
from 3 [  0     1     1  ]
```

so the growth constant is `1 + √2`. The count depends on the boundary condition, and the boundary is where the exercise's `D(x)` appears:[^4]

| strips of width `w`, 1-smooth on `{1,2,3}` | `w = 1, 2, 3, …` | width generating function | sequence |
|---|---|---|---|
| **first column at height 1** (anchored at the base) | `1, 2, 5, 12, 29, 70, 169, 408` | `1/(1 − 2x − x²)` | **Pell `P⋆_w`**, A000129 |
| any first column | `3, 7, 17, 41, 99, 239, 577, 1393` | `(3 + x)/(1 − 2x − x²)` | Pell-Lucas, A001333 |
| first and last column at height 1 | `1, 1, 2, 4, 9, 21, 50, 120` | `(1 − 2x)/((1 − x)(1 − 2x − x²))` | Online Encyclopedia of Integer Sequences (OEIS) **A171842**`(w − 1)`, "Motzkin n-paths of height <= 2" (16 terms, searched 2026-09-26; [[motzkin-castles](pages/motzkin-castles.md)], [[castle-sequence-catalogue](pages/castle-sequence-catalogue.md)]) |

The anchored row is the **Pell castle strip**: `e_1ᵀ (I − xM)^{−1} 𝟙 = 1/(1 − 2x − x²)` exactly. The `(1 − x)` factor of `det(I − xM)` cancels whenever the last column is free, because the eigenvalue-1 eigenvector `(−1, 0, 1)` is orthogonal to `𝟙`; pinning the last column at height 1 as well keeps it. So the two atoms of Act II count castles: `a_{w−1} = P⋆_w` is the number of skylines of width `w` that start at height 1, never jump by more than one row, and never exceed height 3. Starting the walk at height 1 selects Pell proper rather than the companion sequence. Restricting to castles of height *exactly* 3 subtracts the `2^{w−1}` anchored strips that do not reach height 3 and gives `P⋆_w − 2^{w−1} = 0, 0, 1, 4, 13, 38, 105, 280, …`. These are the **Pell castles** ([[pell-castle](pages/pell-castle.md)]): the Pell castle strip is the superset, and requiring it to reach its ceiling 3 turns it into a castle family of exact height 3, counted by `A094706(w − 2)`.

**By last column.** Writing `M = I + A`, a strip is a set of column boundaries where the height changes and a flat-free skeleton walk of `±1` steps ([[binomial-transform](pages/binomial-transform.md)]). On `{1, 2, 3}` a skeleton step away from height 2 has two choices and a step back to 2 has one. So the anchored strips split by their last column into Paul Barry's two Pell sums ([[barry-2005-catalan-transform](pages/barry-2005-catalan-transform.md)]):[^barry]

```
last column at 2:        Σ_k C(w − 1, 2k + 1)·2^k  =  P⋆_{w−1}
last column at 1 or 3:   Σ_k C(w − 1, 2k)·2^k      =  A001333(w − 1)
all anchored strips:     P⋆_{w−1} + A001333(w − 1)  =  P⋆_w
```

The strips with both end columns at height 2 also number `A001333(w − 1)`, and adding a height-2 column at each end is a bijection from the free strips of width `w` to these strips of width `w + 2`, which is why the free row above is `A001333(w + 1)`.

The smallest 0/1 transfer matrix with `det(I − xM) = 1 − 2x − x²` is `3×3`: over `2×2` 0/1 matrices the determinant takes only the six values `1`, `1 − x`, `1 − 2x`, `1 − x²`, `(1 − x)²`, `1 − x − x²`.[^4] The Pell strip is a height-3 object.

## Act IV - The Pell fingerprint

The counts

```
a_n  =  1, 2, 5, 12, 29, 70, 169, 408, 985, 2378, 5741, 13860, …
```

are **Pell numbers, OEIS [A000129](https://oeis.org/A000129) shifted** (`a_n = P⋆_{n+1}`).[^3] See [[pell-numbers](pages/pell-numbers.md)] for the linear-recurrence definition and its Binet form. The dominant characteristic root of `x² − 2x − 1` is `1 + √2 ≈ 2.4142`, so `a_n ~ C · (1 + √2)^n` - the growth rate is the **silver ratio**.

`1 + √2` appears elsewhere on the wiki. On [[eigenvalue-continued-fractions](pages/eigenvalue-continued-fractions.md)] it is one of two **norm-`−1` reduced quadratic surds** with purely periodic continued fraction: `1 + √2 = [2; 2, 2, 2, …]`. On [[tower-word-continued-fraction](pages/tower-word-continued-fraction.md)] it is the **tower-word growth constant** - the singularity of the algebraic generating function for tower words counted by total steps sits at `√2 − 1`, growth rate `1/(√2 − 1) = √2 + 1`.

Silver appears in three castle constructions: the tower word (algebraic generating function, A004149), the 1-smooth height-3 strip (rational, Pell or Pell-Lucas by boundary), and the ridge castles at height 3, ridge rule `R_3 = J − D` ([[metallic-strip-realizability](pages/metallic-strip-realizability.md)], Pell-Lucas `3, 7, 17, 41, …` as a free strip). The Pell numbers relate to `1 + √2` as the Fibonacci numbers relate to `φ` (Binet form, [[aocp-generating-functions](pages/aocp-generating-functions.md)]); on the castle side, Fibonacci counts the height-2 tree castles ([[castle-graph](pages/castle-graph.md)]) and Pell counts the anchored 1-smooth height-3 strip.

## Seminar outline

1. **Coefficient matching.** Extract the recurrence from `D(x) = 1/(1 − 2x − x²)`; the base cases are the recurrence at the boundary.
2. **The two-atom scheme.** `1/(1 − ∑ (weight)·x^(width))` counts strip tilings under a general SEQ, the [[symbolic-method](pages/symbolic-method.md)] in its simplest case.
3. **The castle.** The 1-smooth `3×3` matrix, `e_1ᵀ (I − xM)^{−1} 𝟙 = D(x)`, and the three boundary conditions.
4. **The growth rate.** Ratios of Pell numbers converge to `1 + √2 = [2; 2, 2, …]`; Fibonacci and `φ` are the parallel case.
5. **Summary.** Coefficient extraction, the symbolic method, the transfer matrix, and the growth constant `1 + √2`, a unit of `Q(√2)`.

## Atoms and transfer matrices

Read as `SEQ(2Z + Z²)`, the denominator `1 − 2x − x²` lists two atoms. The anchored 1-smooth strip is a transfer matrix whose generating function reproduces it, with the extra `(1 − x)` factor of `det(I − xM)` cancelled.

## Appearances in Sources

- [[pe502-pell-castle-strip](pages/pe502-pell-castle-strip.md)] - the working note this seminar is built on: the coefficient-matching mechanic and the two-atom reading.
- [[barry-2005-catalan-transform](pages/barry-2005-catalan-transform.md)] - the sums `Σ C(n, 2k + 1) 2^k = P⋆_n` and `Σ C(n, 2k) 2^k = A001333(n)`, read here as the anchored strip by last column.

## Related Concepts

- [[pell-castle](pages/pell-castle.md)] - the Pell castles: the anchored 1-smooth strips that reach height 3, `P⋆_w − 2^{w−1}` of them, the castle type the strip leads to.
- [[1-smooth-castles](pages/1-smooth-castles.md)] - the anchored 1-smooth strip with ceiling `h` for every `h`; the two-atom reading of Act II belongs to `h = 3`.
- [[m-smooth-castles](pages/m-smooth-castles.md)] - step bound `m`: at ceiling `h = m + 2` the strip is `1/(1 − (m+1)x − m·x²)`, the two-atom reading with atoms of weight `m + 1` and `m`.

- [[castle-strip](pages/castle-strip.md)] - the from-scratch bridge: what a castle strip is, and how a neighbor rule becomes a transfer matrix whose states are the column heights. Read it first if the transfer-matrix language in Act III is unfamiliar.
- [[metallic-strip-realizability](pages/metallic-strip-realizability.md)] - the 1-smooth height-3 matrix and its `(1 − x)(1 − 2x − x²)` denominator, and the ridge rule `R_h = J − D` that realizes the whole metallic ladder.
- [[pell-numbers](pages/pell-numbers.md)] - the integer sequence and its silver-ratio growth.
- [[binomial-transform](pages/binomial-transform.md)] - the strip as a binomial transform of its skeleton; Barry's Pell and Pell-Lucas sums as the strips by last column ([[barry-2005-catalan-transform](pages/barry-2005-catalan-transform.md)]).
- [[generating-functions](pages/generating-functions.md)] - the coefficient-matching technique and the symbolic-method context.
- [[symbolic-method](pages/symbolic-method.md)] - the `SEQ` construction the two-atom scheme is an instance of.
- [[castle-counting-formula](pages/castle-counting-formula.md)] - the wiki's rational recurrences, whose initial terms coefficient matching produces the same way.
- [[castle-graph](pages/castle-graph.md)] - the height-2 tree castles, the Fibonacci partner of the Pell strip.
- [[eigenvalue-continued-fractions](pages/eigenvalue-continued-fractions.md)] - where `1 + √2 = [2;2,2,…]` is developed.
- [[tower-word-continued-fraction](pages/tower-word-continued-fraction.md)] - where `1 + √2` also appears, as the tower-word growth constant.
- [[aocp-generating-functions](pages/aocp-generating-functions.md)] - the Fibonacci / `φ` companion (same story with `a = 1`).
- [[castle-classification-shape](pages/castle-classification-shape.md)] - Axis 2 (the 1-smooth predicate); [[castle-classification-growth](pages/castle-classification-growth.md)] - Axis 8, for which the anchored 1-smooth strip is the canonical **silver width growth castle** example.
- [[hear-the-shape-seminar](pages/hear-the-shape-seminar.md)] / [[one-bit-seminar](pages/one-bit-seminar.md)] / [[hardin-identity-seminar](pages/hardin-identity-seminar.md)] / [[oeis-mining-seminar](pages/oeis-mining-seminar.md)] / [[sandcastle-seminar](pages/sandcastle-seminar.md)] / [[castle-fibers-char-2-walkthrough](pages/castle-fibers-char-2-walkthrough.md)] / [[tower-recursion-master-class](pages/tower-recursion-master-class.md)] / [[castle-cryptography](pages/castle-cryptography.md)] / [[song-as-castle](pages/song-as-castle.md)] - the other seminar pages.

## Footnotes

[^1]: [[pe502-pell-castle-strip](pages/pe502-pell-castle-strip.md)] §"Where the recurrence comes from" L9-L19 - coefficient-matching mechanics, and the uniform recurrence `a_n − 2a_{n−1} − a_{n−2} = [n = 0]` with `a_{−1} = a_{−2} = 0`. Re-verified during ingest by evaluating the recurrence at the boundary and matching against direct series expansion of `1/(1−2x−x²)`.
[^2]: [[pe502-pell-castle-strip](pages/pe502-pell-castle-strip.md)] §"The castle reading" L23-L28 - the two-atom composition scheme and its "peel off the last atom" recurrence. Under the SEQ construction (see [[symbolic-method](pages/symbolic-method.md)] Theorem I.1), `SEQ(2·Z + Z²)` has ordinary generating function (OGF) `1/(1 − 2z − z²)`.
[^3]: The sequence `1, 2, 5, 12, 29, 70, 169, 408, 985, 2378, 5741, 13860` (produced by the recurrence with `a_0 = 1, a_1 = 2`) was numerically matched against OEIS A000129 = `0, 1, 2, 5, 12, 29, 70, 169, …` during ingest, confirming `a_n = P⋆_{n+1}`. The growth ratio `a_{n+1}/a_n → 2.41421… = 1 + √2` verified for `n = 5..11`.
[^4]: Verified by execution (Python 3, SymPy), 2026-09-19. With `M = [[1,1,0],[1,1,1],[0,1,1]]` (1-smooth on heights `{1,2,3}`), `e_1ᵀ (I − xM)^{−1} 𝟙 = 1/(1 − 2x − x²)`, `𝟙ᵀ (I − xM)^{−1} 𝟙 = (3 + x)/(1 − 2x − x²)`, `e_1ᵀ (I − xM)^{−1} e_1 = (1 − 2x)/((1 − x)(1 − 2x − x²))`, and `det(xI − M) = (x − 1)(x² − 2x − 1)`. Brute-force enumeration of 1-smooth skylines over `{1,2,3}` for `w = 1..8` gives `1, 2, 5, 12, 29, 70, 169, 408` (first column 1), `3, 7, 17, 41, 99, 239, 577, 1393` (any first column), and `1, 1, 2, 4, 9, 21, 50, 120` (both end columns 1); the anchored count restricted to `max c = 3` is `0, 0, 1, 4, 13, 38, 105, 280 = P⋆_w − 2^{w−1}`. `det(I − xM)` over all sixteen `2×2` 0/1 matrices takes exactly the six values `1, 1 − x, 1 − 2x, 1 − x², (1 − x)², 1 − x − x²`. The free-strip denominator `(1 − x)(1 − 2x − x²)` is footnote 3 of [[metallic-strip-realizability](pages/metallic-strip-realizability.md)].
[^barry]: [[barry-2005-catalan-transform](pages/barry-2005-catalan-transform.md)] §7 L1142-L1157 [synthesis] - "Σ C(n, 2k) 2^k = 1, 1, 3, 7, 17, . . . = ((1 + √2)^n + (1 − √2)^n)/2 which is the sequence A001333" and "the following formula for the Pell numbers A000129, Σ C(n, 2k + 1) 2^k = Pell(n)". The castle reading was verified by execution (2026-10-08): strips on `{1, 2, 3}` from 1 to 2, from 1 to `{1, 3}`, from 2 to 2, all anchored, and free, against `P⋆_{w−1}`, `A001333(w − 1)`, `A001333(w − 1)`, `P⋆_w` and the width-`(w + 2)` strips from 2 to 2, for `w ≤ 13`.
