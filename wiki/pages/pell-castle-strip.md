---
title: "The Pell castle strip - from 1/(1 − 2x − x²) to the silver ratio"
category: Analyses
summary: A seminar-shaped analysis. Coefficient matching on D(x) = 1/(1 − 2x − x²) gives the Pell recurrence with its initial terms; read as a sequence of two atoms, D(x) counts tilings; and the anchored 1-smooth strips on the heights {1, 2, 3} realize it, P⋆_w of width w with Σ P⋆_w x^{w−1} = D(x). Strips need not reach height 3; those that do are the Pell castles, P⋆_w − 2^{w−1} = A094706(w − 2) of them. The anchored strips are silver by width.
tags: [analysis, castle, pell, generating-functions, coefficient-matching, seminar, pedagogy, silver-ratio, transfer-matrix]
sources: [pe502-pell-castle-strip, barry-2005-catalan-transform]
created: 2026-09-15
updated: 2026-10-16
---

# The Pell castle strip - from 1/(1 − 2x − x²) to the silver ratio

## Overview

The source note works the following exercise, which it records as an end-of-chapter exercise of Analytic Combinatorics ([[pe502-pell-castle-strip](pages/pe502-pell-castle-strip.md)]): *given the generating function `D(x) = 1/(1 − 2x − x²)`, find the recurrence for its coefficients and the initial terms.* This page follows the exercise to a family of skylines. Coefficient matching gives the recurrence and the initial terms from one equation (section 1). Read as a sequence construction, `D(x)` counts tilings by two atoms (section 2). The 1-smooth rule on the heights `{1, 2, 3}`, with the first column at height 1, gives skylines whose generating function is exactly `D(x)`, and their counts are the Pell numbers `P⋆_w` (section 3). Their growth constant is the silver ratio `1 + √2` (section 4).

## 1. Coefficient matching

Write

```
D(x)  =  1/(1 − 2x − x²)  =  Σ_{i≥0} a_i x^i,
```

and multiply through:

```
(1 − 2x − x²) · D(x)  =  1.
```

Matching the coefficients of `x^n` on both sides gives[^1]

- `[x^0]`: `a_0 = 1`;
- `[x^1]`: `a_1 − 2·a_0 = 0`, so `a_1 = 2`;
- `[x^{n+2}]` for `n ≥ 0`: `a_{n+2} − 2·a_{n+1} − a_n = 0`.

A power series has no negative powers, so with `a_{−1} = a_{−2} = 0` the three lines are one equation:[^1]

```
a_n − 2·a_{n−1} − a_{n−2}  =  [n = 0].                                        (1.1)
```

At `n = 0` it reads `a_0 − 0 − 0 = 1`, and at `n = 1` it reads `a_1 − 2·a_0 − 0 = 0`. The initial terms are Equation (1.1) at `n = 0` and `n = 1`.

The recurrences of the signed tower counts arise the same way: matching coefficients in `den_k(x)·P_k(x) = num_k(x)` gives the recurrence of `P(k, ·)` past the degree of `num_k` and its initial terms below it ([[castle-counting-formula](pages/castle-counting-formula.md)], Equation (6)). [[generating-functions](pages/generating-functions.md)] states the method for any rational generating function.

## 2. Two atoms

In the symbolic method, `1/(1 − B(x))` is the generating function of the sequences of objects counted by `B(x)` ([[symbolic-method](pages/symbolic-method.md)]). With `B(x) = 2x + x²` there are two atoms:[^2]

- an atom of width 1 in two kinds, the term `2x`;
- an atom of width 2 in one kind, the term `x²`.

A tiling of a strip of length `n` by these atoms is a sequence of atoms of total width `n`, and the tilings of length `n` number `a_n`, since `Σ_{j≥0} (2x + x²)^j = 1/(1 − 2x − x²)`. Removing the last atom proves `a_n = 2·a_{n−1} + a_{n−2}`: a tiling of length `n` ends in a width-1 atom, in 2 kinds, after a tiling of length `n − 1`, or in the width-2 atom after a tiling of length `n − 2`.[^2] For `n = 2` the tilings are the two kinds of width-1 atom in each of two places, `2·2 = 4` tilings, and the width-2 atom, so `a_2 = 5`.

## 3. The strip: 1-smooth on the heights {1, 2, 3}, anchored at height 1

A castle strip is a skyline read left to right under a rule on neighboring columns, and the rule is a 0/1 transfer matrix `M` whose states are the allowed column heights: `M[a][b] = 1` when a column of height `a` may be followed by one of height `b` ([[castle-strip](pages/castle-strip.md)]). A strip on the heights `{1, …, h}` need not reach height `h`, so a strip is not a castle of height `h`.

Take the **1-smooth** rule on `{1, 2, 3}`: neighboring columns differ in height by at most 1, `|c_{i+1} − c_i| ≤ 1` (the 1-smooth type of [[castle-classification-shape](pages/castle-classification-shape.md)]). Its transfer matrix and characteristic polynomial are[^3]

```
        to 1  to 2  to 3
from 1 [  1     1     0  ]
from 2 [  1     1     1  ]          det(λI − M)  =  (λ − 1)(λ² − 2λ − 1)
from 3 [  0     1     1  ]
```

A strip is **anchored** when its first column has height 1. The anchored strips of width 3 are the five skylines `(1, 1, 1)`, `(1, 1, 2)`, `(1, 2, 1)`, `(1, 2, 2)` and `(1, 2, 3)`; only the skyline `(1, 2, 3)` reaches height 3.

With `N(w)` strips of width `w` from the start vector `u` to the end vector `v`, `N(w) = uᵀ M^{w−1} v`, so `Σ_{w≥1} N(w) x^{w−1} = uᵀ (I − xM)^{−1} v`. Three choices of boundary give:[^3]

| strips of width `w`, 1-smooth on `{1, 2, 3}` | `N(w)` for `w = 1, 2, 3, …` | `Σ_{w≥1} N(w) x^{w−1}` | sequence |
|---|---|---|---|
| first column at height 1 (anchored) | `1, 2, 5, 12, 29, 70, 169, 408` | `1/(1 − 2x − x²)` | Pell numbers `P⋆_w`, A000129 |
| any first column | `3, 7, 17, 41, 99, 239, 577, 1393` | `(3 + x)/(1 − 2x − x²)` | Pell-Lucas numbers `A001333(w + 1)` |
| first and last column at height 1 | `1, 1, 2, 4, 9, 21, 50, 120` | `(1 − 2x)/((1 − x)(1 − 2x − x²))` | `A171842(w − 1)`, the Motzkin paths of length `w − 1` and height at most 2 |

The anchored row is the **Pell castle strip**: `e_1ᵀ (I − xM)^{−1} 𝟙 = D(x)`, so the anchored strips of width `w` number `P⋆_w = a_{w−1}`. The factor `1 − x` of `det(I − xM)` cancels whenever the last column is free: `M` is symmetric, its eigenvector for the eigenvalue 1 is `(−1, 0, 1)`, and this vector is orthogonal to `𝟙`. Pinning the last column at height 1 keeps the factor, since `(−1, 0, 1)` is not orthogonal to `e_1`. The strips with both end columns at height 1 are Motzkin paths shifted up by one, which is the comment on `A171842` ([[motzkin-castles](pages/motzkin-castles.md)]).[^4]

**Pell castles.** The anchored strips that do not reach height 3 use only the heights 1 and 2, and every sequence in `{1, 2}` starting at 1 is 1-smooth, so there are `2^{w−1}` of them. The anchored strips that reach height 3 are the **Pell castles**, which have height 3 by definition ([[pell-castle](pages/pell-castle.md)]):[^3]

```
A_Pell(w)  =  P⋆_w − 2^{w−1}  =  0, 0, 1, 4, 13, 38, 105, 280, …   (w = 1, 2, 3, …)
           =  A094706(w − 2)      for w ≥ 2.
```

At `w = 3` the one Pell castle is the skyline `(1, 2, 3)`. `A094706` is the convolution of the Pell numbers with the powers of 2.[^5]

**By last column.** A strip of width `w` is determined by the set of boundaries between neighboring columns at which the height changes, and by its skeleton, the walk of `±1` steps taken at those boundaries ([[binomial-transform](pages/binomial-transform.md)]). From height 1 a skeleton alternates a step to height 2, one choice, and a step away from height 2, to 1 or 3, two choices. So a skeleton with `j` steps from height 1 is one of `2^{⌊j/2⌋}`, and it ends at height 2 exactly when `j` is odd. Summing over `j` splits the anchored strips by their last column into Barry's two sums ([[barry-2005-catalan-transform](pages/barry-2005-catalan-transform.md)]):[^6]

```
last column at height 2:        Σ_k C(w − 1, 2k + 1)·2^k  =  P⋆_{w−1}
last column at height 1 or 3:   Σ_k C(w − 1, 2k)·2^k      =  A001333(w − 1)
all anchored strips:            P⋆_{w−1} + A001333(w − 1)  =  P⋆_w
```

The strips with both end columns at height 2 also number `A001333(w − 1)`, since a skeleton from height 2 ends at height 2 exactly when `j` is even and is one of `2^{j/2}`. Adding a column of height 2 at each end maps the strips of width `w` with free ends one-to-one onto these strips of width `w + 2`, since height 2 may neighbor every height. So the strips with free ends number `A001333(w + 1)`, the second row of the table.

**Two heights are not enough.** For a 0/1 matrix `M` of size 2, `det(I − xM) = 1 − (tr M)x + (det M)x²` with `tr M ∈ {0, 1, 2}`, and it takes exactly the six values `1`, `1 − x`, `1 − 2x`, `1 − x²`, `(1 − x)²` and `1 − x − x²`.[^3] The generating function of a strip has a denominator that divides `det(I − xM)`, so no rule on two heights gives the denominator `1 − 2x − x²`.

## 4. The silver ratio

The coefficients

```
a_n  =  1, 2, 5, 12, 29, 70, 169, 408, 985, 2378, 5741, 13860, …
```

are the Pell numbers shifted by one, `a_n = P⋆_{n+1}` ([[pell-numbers](pages/pell-numbers.md)]).[^7] The roots of `λ² − 2λ − 1` are `1 ± √2`, and

```
P⋆_n  =  ( (1 + √2)^n − (1 − √2)^n ) / (2√2),
```

so `P⋆_n ~ (1 + √2)^n / (2√2)`, and the anchored strips are silver by width. This is the case `a = 2` of the Binet formula for the roots of `λ² − aλ − 1`, whose case `a = 1` gives the Fibonacci numbers and the golden ratio `φ` ([[aocp-generating-functions](pages/aocp-generating-functions.md)], [[metallic-means](pages/metallic-means.md)]). On the castle side, the Fibonacci castles, the tree castles of height 2, number `F_{w+2} − 1` and are golden by width ([[castle-graph](pages/castle-graph.md)]).

The silver ratio `1 + √2 = [2; 2, 2, …]` has a purely periodic continued fraction because it is a reduced quadratic surd, a unit of norm `−1` ([[eigenvalue-continued-fractions](pages/eigenvalue-continued-fractions.md)]). It is also the growth constant of two other castle constructions:

- the tower words counted by their total number of steps, `A004149`, whose generating function has its singularity nearest 0 at `√2 − 1` ([[tower-word-continued-fraction](pages/tower-word-continued-fraction.md)]);
- the ridge strips on the heights `{1, 2, 3}`, with transfer matrix `R_3 = J − D`, `J` the all-ones matrix and `D = diag(1, 1, 0)`, which with free ends number `3, 7, 17, 41, …`, the Pell-Lucas numbers again ([[metallic-strip-realizability](pages/metallic-strip-realizability.md)]).[^3]

## Seminar outline

1. **Coefficient matching.** Extract the recurrence from `D(x) = 1/(1 − 2x − x²)`; the initial terms are Equation (1.1) at `n = 0, 1`.
2. **Two atoms.** `1/(1 − 2x − x²)` is the sequence construction over an atom of width 1 in two kinds and an atom of width 2.
3. **The strip.** The 1-smooth matrix on `{1, 2, 3}`, `e_1ᵀ (I − xM)^{−1} 𝟙 = D(x)`, the three boundary conditions, and the Pell castles `P⋆_w − 2^{w−1}`.
4. **The growth constant.** Ratios of consecutive Pell numbers converge to `1 + √2 = [2; 2, 2, …]`; the Fibonacci numbers and `φ` are the case `a = 1`.
5. **Summary.** Coefficient extraction, the sequence construction, the transfer matrix, and the growth constant `1 + √2`, a unit of `Q(√2)`.

## Appearances in Sources

- [[pe502-pell-castle-strip](pages/pe502-pell-castle-strip.md)] - the note this page builds on: coefficient matching on `D(x)` and the two-atom reading.
- [[barry-2005-catalan-transform](pages/barry-2005-catalan-transform.md)] - the sums `Σ_k C(n, 2k + 1) 2^k = P⋆_n` and `Σ_k C(n, 2k) 2^k = A001333(n)`, which count the anchored strips by last column.

## Related Concepts

- [[pell-castle](pages/pell-castle.md)] - the Pell castles, the anchored 1-smooth strips that reach height 3, `P⋆_w − 2^{w−1}` of width `w`.
- [[1-smooth-castles](pages/1-smooth-castles.md)] - the anchored 1-smooth strips and castles on the heights `{1, …, h}` for every `h`; `h = 3` is this page.
- [[m-smooth-castles](pages/m-smooth-castles.md)] - neighboring columns differing by at most `m`; on the heights `{1, …, m + 2}` the anchored strips have generating function `x/(1 − (m+1)x − m·x²)`, with `x` marking width, a sequence of two atoms in `m + 1` and `m` kinds.
- [[castle-strip](pages/castle-strip.md)] - castle strips and their transfer matrices, with the column heights as states.
- [[metallic-strip-realizability](pages/metallic-strip-realizability.md)] - the growth constants of strip rules: the 1-smooth matrix on three heights with `det(I − xM) = (1 − x)(1 − 2x − x²)`, and the ridge rule `R_h = J − D`, whose growth constants are the metallic means `δ_{h−1}`.
- [[pell-numbers](pages/pell-numbers.md)] - the Pell numbers `P⋆_n`, their recurrence and Binet formula.
- [[binomial-transform](pages/binomial-transform.md)] - a strip count as the binomial transform of its skeleton count, and Barry's sums as the strips by last column.
- [[generating-functions](pages/generating-functions.md)] - coefficient matching for any rational generating function.
- [[symbolic-method](pages/symbolic-method.md)] - the sequence construction of section 2.
- [[castle-counting-formula](pages/castle-counting-formula.md)] - the recurrences of `P(k, ·)` from `den_k·P_k = num_k`.
- [[castle-graph](pages/castle-graph.md)] - the tree castles; at height 2 they are the Fibonacci castles, `F_{w+2} − 1` of width `w`.
- [[eigenvalue-continued-fractions](pages/eigenvalue-continued-fractions.md)] - the continued fraction `1 + √2 = [2; 2, 2, …]` and why it is purely periodic.
- [[tower-word-continued-fraction](pages/tower-word-continued-fraction.md)] - the tower words, `A004149`, with growth constant `√2 + 1`.
- [[aocp-generating-functions](pages/aocp-generating-functions.md)] - the Fibonacci method and the Binet formula, the case `a = 1`.
- [[castle-classification-growth](pages/castle-classification-growth.md)] - growth constants of castle families along a size axis; the Pell castles and the ridge castles of height 3 are both silver by width.
- [[hear-the-shape-seminar](pages/hear-the-shape-seminar.md)], [[one-bit-seminar](pages/one-bit-seminar.md)], [[hardin-identity-seminar](pages/hardin-identity-seminar.md)], [[oeis-mining-seminar](pages/oeis-mining-seminar.md)], [[sandcastle-seminar](pages/sandcastle-seminar.md)], [[castle-fibers-char-2-walkthrough](pages/castle-fibers-char-2-walkthrough.md)], [[tower-recursion-master-class](pages/tower-recursion-master-class.md)], [[castle-cryptography](pages/castle-cryptography.md)], [[song-as-castle](pages/song-as-castle.md)] - the other seminar pages.

## Footnotes

[^1]: [[pe502-pell-castle-strip](pages/pe502-pell-castle-strip.md)] §"Where the recurrence comes from" L9-19 - "Matching coefficients on (1 - 2x - x^2) D(x) = 1: [x^0]: a_0 = 1; [x^1]: a_1 - 2a_0 = 0, so a_1 = 2; [x^{n+2}] for n ≥ 0: a_{n+2} - 2a_{n+1} - a_n = 0", "Uniformly: a_n - 2a_{n-1} - a_{n-2} = [n = 0] with a_{-1} = a_{-2} = 0. The base cases a_0 = 1, a_1 = 2 are the same recurrence evaluated at n = 0, 1 with those zeros substituted."
[^2]: [[pe502-pell-castle-strip](pages/pe502-pell-castle-strip.md)] §"The castle reading" L23-28 - "Read it as counting tilings of a 1 × n strip using: a width-1 atom with weight 2, a width-2 atom with weight 1. Then a_n is the total weight of such tilings, and a_n = 2 a_{n-1} + a_{n-2} is just \"peel off the last atom.\""
[^3]: Verified by execution (Python 3.11 with SymPy, 2026-10-16): with `M = [[1,1,0],[1,1,1],[0,1,1]]`, `det(λI − M) = (λ − 1)(λ² − 2λ − 1)`, `e_1ᵀ (I − xM)^{−1} 𝟙 = 1/(1 − 2x − x²)`, `𝟙ᵀ (I − xM)^{−1} 𝟙 = (3 + x)/(1 − 2x − x²)` and `e_1ᵀ (I − xM)^{−1} e_1 = (1 − 2x)/((1 − x)(1 − 2x − x²))`; enumeration of the 1-smooth skylines on `{1, 2, 3}` for `w ≤ 8` gives the three rows of the table and `P⋆_w − 2^{w−1}` for the anchored ones that reach height 3; the strips from 1 to 2, from 1 to `{1, 3}` and from 2 to 2 have generating functions `x/(1 − 2x − x²)` and `(1 − x)/(1 − 2x − x²)` twice; the sixteen `2 × 2` 0/1 matrices give exactly the six values of `det(I − xM)`; the free ridge strips on `{1, 2, 3}` number `3, 7, 17, 41, 99, 239` for `w ≤ 6`.
[^4]: https://oeis.org/A171842 (read 2026-10-16) - "a(n) is the top left entry of the n-th power of the 3 X 3 matrix [1, 1, 0; 1, 1, 1; 0, 1, 1]", "a(n) is the number of Motzkin n-paths of height <= 2", "G.f.: (1-2*x)/((1-x)*(1-2*x-x^2))"; and https://oeis.org/A001333 - "Pell-Lucas numbers: numerators of continued fraction convergents to sqrt(2)".
[^5]: https://oeis.org/A094706 (read 2026-10-16) - "Convolution of Pell(n) and 2^n", data `0, 1, 4, 13, 38, 105, 280, 729, …`.
[^6]: [[barry-2005-catalan-transform](pages/barry-2005-catalan-transform.md)] §7 L1142-1157 [synthesis] - the sums `Σ_k C(n, 2k) 2^k = 1, 1, 3, 7, 17, … = ((1 + √2)^n + (1 − √2)^n)/2`, "which is the sequence A001333", and "the following formula for the Pell numbers A000129", `Σ_k C(n, 2k + 1) 2^k = Pell(n)`. The castle reading was checked by enumeration for `w ≤ 13` (2026-10-08).
[^7]: https://oeis.org/A000129 (read 2026-10-16) - "Pell numbers: a(0) = 0, a(1) = 1; for n > 1, a(n) = 2*a(n-1) + a(n-2)", data `0, 1, 2, 5, 12, 29, 70, 169, 408, 985, 2378, 5741, 13860, …`.
