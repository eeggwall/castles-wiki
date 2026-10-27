---
title: The castle strip - bridge to transfer matrices
category: Concepts
summary: A castle strip is a skyline (c_1, …, c_w) with heights in {1, …, h} in which every pair of neighboring columns obeys a rule; a strip need not reach height h, so it is not a castle of height h, and the strips that do reach h are the castles of height h of the rule's family. The rule is an h × h 0/1 transfer matrix M whose states are the heights (M[a][b] = 1 when a column of height a may be followed by one of height b). There are 𝟙ᵀM^{w−1}𝟙 strips of width w, their generating function has a denominator dividing det(I − xM), and their growth by width is the Perron root of M.
tags: [concept, castle, transfer-matrix, strip, height, perron-root, growth-constant, generating-function, pedagogy, bridge]
sources: [pe502-pell-castle-strip]
created: 2026-09-18
updated: 2026-10-27
---

# The castle strip - bridge to transfer matrices

[[pell-castle-strip](pages/pell-castle-strip.md)], [[metallic-strip-realizability](pages/metallic-strip-realizability.md)] and [[reachable-field-census](pages/reachable-field-census.md)] count skylines with transfer matrices and read growth constants off the eigenvalues of small 0/1 matrices. This page defines the strips, the matrices and the two quantities those pages use, the strip count and the Perron root.

## Strips

Fix a height bound `h` and a **rule**: for each pair of heights `a, b` in `{1, …, h}`, whether a column of height `a` may stand immediately to the left of a column of height `b`. A **castle strip** of width `w` under the rule is a skyline `(c_1, …, c_w)` with every `c_i` in `{1, …, h}` such that every pair of neighboring columns `(c_i, c_{i+1})` is allowed. A strip need not reach height `h`, so a strip is not a castle of height `h`. The strips that reach height `h` are castles of height `h` ([[castle-polyomino](pages/castle-polyomino.md)]), and they make up the castles of height `h` of the rule's family.

Four rules:

- every pair allowed: every skyline in `{1, …, h}^w` is a strip;
- `a ≠ b`, the plateau-free rule: no two neighboring columns of equal height;
- `|a − b| ≤ 1`, the 1-smooth rule: neighboring heights differ by at most 1. Its strips on `{1, …, h}` form the Motzkin strip of height `h` ([[motzkin-castles](pages/motzkin-castles.md)]);
- `|a − b| = 1`, the zig-zag rule: neighboring heights differ by exactly 1. It is the 1-smooth rule and the plateau-free rule imposed together ([[zig-zag-castles](pages/zig-zag-castles.md)]).

*Example.* At `h = 3` under the 1-smooth rule, the skyline `(1, 2, 3, 2)` is a strip that reaches height 3, so it is a castle of height 3; the skyline `(1, 2, 2, 1)` is a strip that is not a castle of height 3; and the skyline `(1, 3, 2)` is not a strip, since its first two heights differ by 2.

## The transfer matrix

A rule on the heights `{1, …, h}` is an `h × h` matrix `M` of 0s and 1s with

```
M[a][b]  =  1   if a column of height a may be followed by a column of height b,
M[a][b]  =  0   otherwise.
```

Its rows and columns are indexed by the heights themselves: the `h` states of the transfer matrix are the column heights `1, …, h`. "A 0/1 transfer matrix on `h` height states" on the other pages means this matrix.

Two rules `M` and `M′` imposed together allow a pair of heights exactly when both allow it, so their matrix is the entrywise product `M ⊙ M′`, with entries `M[a][b] · M′[a][b]`. The 1-smooth rule is `I + A_path` and the plateau-free rule is `J − I`, with `I` the identity matrix, `J` the all-ones matrix and `A_path` the adjacency matrix of the path on the heights, which has a 1 where `|a − b| = 1`. Their product is `(I + A_path) ⊙ (J − I) = A_path`, the zig-zag rule ([[zig-zag-castles](pages/zig-zag-castles.md)]).

With `𝟙` the all-ones column vector of length `h`, the number of strips of width `w` is

```
N(w)  =  𝟙ᵀ M^{w−1} 𝟙.                                                       (1)
```

The entry `(a, b)` of `M^{w−1}` counts the strips of width `w` that start at height `a` and end at height `b`, since each factor `M` appends one column, and the two vectors `𝟙` sum over the first and last heights.

*Example: `h = 2`.* With every pair allowed, `M = [[1, 1], [1, 1]]`, and Equation (1) gives `N(1) = 2`, `N(2) = 4`, `N(3) = 8`: the skylines `(1)`, `(2)`; the four skylines in `{1, 2}²`; and the eight in `{1, 2}³`. Under the plateau-free rule, `M = [[0, 1], [1, 0]]`, and the only strips are the alternating skylines `(1, 2, 1, …)` and `(2, 1, 2, …)`, so `N(w) = 2` for every `w`, as Equation (1) gives.

## Growth constant and generating function

**Growth constant.** The **Perron root** `ρ(M)` is the largest eigenvalue of `M`, which is real and nonnegative because `M` is nonnegative (Perron-Frobenius theorem); when every height can be reached from every height under the rule, it is positive and a simple eigenvalue. `N(w)` is the sum of the entries of `M^{w−1}`, which for a nonnegative matrix is a matrix norm, so by Gelfand's formula

```
lim_{w→∞} N(w)^{1/w}  =  ρ(M).                                               (2)
```

This is the growth by width of the strips. For `M = [[1, 1], [1, 1]]` the eigenvalues are 2 and 0, and `N(w) = 2^w`. [[metallic-means](pages/metallic-means.md)] and [[reachable-field-census](pages/reachable-field-census.md)] ask which numbers arise as the Perron root of a 0/1 matrix.

**Generating function.** Summing Equation (1) over `w`,

```
Σ_{w≥1} N(w) x^{w−1}  =  𝟙ᵀ (I − xM)^{−1} 𝟙,                                (3)
```

a rational function whose denominator divides `det(I − xM)`, since by Cramer's rule every entry of `(I − xM)^{−1}` is a polynomial divided by `det(I − xM)`. A factor can cancel, as the factor `1 − x` of the 1-smooth rule on `{1, 2, 3}` does on [[pell-castle-strip](pages/pell-castle-strip.md)]. The coefficients of the reduced denominator give the linear recurrence of `N(w)` ([[generating-functions](pages/generating-functions.md)]), and by Equation (2) its root of smallest modulus is `1/ρ(M)`. For `h = 2` the denominator has degree at most 2, so the growth constant is an integer or a quadratic irrational ([[metallic-strip-realizability](pages/metallic-strip-realizability.md)]).

## Strips and the Project Euler castles

- **Every pair allowed.** Then `M` is the all-ones matrix `J`, with Perron root `h`, and `N(w) = h^w` counts the castles of width `w` and height at most `h`. The Project Euler rules impose no condition on neighboring columns, since the blocks are the maximal runs of each row and the gap rule holds for every skyline ([[castle-polyomino](pages/castle-polyomino.md)]). The strips that reach `h` number `A(w, h) = h^w − (h−1)^w`.
- **Named families.** The 1-smooth rule on `{1, 2, 3}` with the first column at height 1 gives the Pell castle strip, `Σ_w N(w) x^{w−1} = 1/(1 − 2x − x²)`, silver by width; its strips that reach height 3 are the Pell castles ([[pell-castle-strip](pages/pell-castle-strip.md)]). The ridge rule gives the ridge castles ([[ridge-castle](pages/ridge-castle.md)]). The zig-zag rule gives the zig-zag castles, whose strips on `{1, …, h}` are the zig-zag paths of the OEIS in a rectangle of width `h`, with Perron root `2cos(π/(h+1))` ([[zig-zag-castles](pages/zig-zag-castles.md)]). Each rule defines a family of castles, the strips that reach the top height, and its Perron root is computed from `M`.

[[castle-graph](pages/castle-graph.md)] takes eigenvalues of a single castle's cell adjacency matrix; a strip rule's Perron root is the growth constant of a whole family.

## Vocabulary

| phrase on other pages | meaning |
|---|---|
| "transfer matrix on `h` height states" | the `h × h` 0/1 rule matrix, with states the heights `1, …, h` |
| "`M[a][b] = 1`" | a column of height `a` may be followed by a column of height `b` |
| "Perron root of `M`" | the largest eigenvalue, the growth by width of the strips |
| "denominator `det(I − xM)`" | a multiple of the denominator of the generating function (3) |
| "`p₁, p₂`" (in `1 − p₁x − p₂x²`) | the coefficients of a quadratic strip denominator ([[metallic-strip-realizability](pages/metallic-strip-realizability.md)]) |
| "minimum height for a growth constant" | the smallest `h` for which some 0/1 matrix of size `h` has that Perron root |
| "zig-zag rule", "`M ⊙ M′`" | neighboring heights differ by exactly 1, with matrix `A_path`; the entrywise product of two rule matrices, the two rules imposed together ([[zig-zag-castles](pages/zig-zag-castles.md)]) |
| "ridge rule", "`R_h = J − D`" | neighboring heights differ unless both equal `h`; `J` is the all-ones matrix and `D = diag(1, …, 1, 0)`. Its strips that reach `h` are the ridge castles of height `h`, and its Perron root is the metallic mean `δ_{h−1}` ([[ridge-castle](pages/ridge-castle.md)], [[metallic-strip-realizability](pages/metallic-strip-realizability.md)]) |

## Computation

[[castle-snippets-strips](pages/castle-snippets-strips.md)] has the strip counter and the probes for Perron roots and their number fields (`strip_field_census`, `ridge_R`, `ridge_count`, `sh_canonical`). With NumPy, `ones @ numpy.linalg.matrix_power(M, w - 1) @ ones` is Equation (1), and `max(abs(numpy.linalg.eigvals(M)))` is the Perron root.

## Related Concepts

- [[kernel-method](pages/kernel-method.md)] - the same strips counted through the roots of the kernel `1 − x·steps(u)` instead of a transfer matrix ([[banderier-nicodeme-2010-bounded-discrete-walks](pages/banderier-nicodeme-2010-bounded-discrete-walks.md)]).
- [[pell-castle-strip](pages/pell-castle-strip.md)] - the anchored 1-smooth strips on `{1, 2, 3}`, with generating function `1/(1 − 2x − x²)` and growth `1 + √2`.
- [[metallic-strip-realizability](pages/metallic-strip-realizability.md)] - which growth constants are Perron roots of 0/1 matrices; the reduction to the two coefficients `p₁, p₂`, and the ridge rule.
- [[reachable-field-census](pages/reachable-field-census.md)] - the census of strip Perron roots by number field.
- [[metallic-means](pages/metallic-means.md)] - de Spinadel's metallic means `σ_p^q`, among them the Perron roots `δ_a` of the ridge rules.
- [[castle-classification-growth](pages/castle-classification-growth.md)] - the growth type of a family of castles, the growth constant of its count along a stated axis.
- [[castle-graph](pages/castle-graph.md)] - the cell adjacency matrix of a single castle and its spectrum.
- [[castle-representations](pages/castle-representations.md)] - the skyline encoding of a castle.
- [[generating-functions](pages/generating-functions.md)] - rational generating functions and the linear recurrences of their coefficients.
- [[aocp-generating-permutations-tuples](pages/aocp-generating-permutations-tuples.md)] - Knuth's Algorithm M, which lists the skylines in `{1, …, h}^w` one at a time, where Equation (1) counts them.
- [[castle-compression](pages/castle-compression.md)] - the castles of the first compression tier, generated by a strip rule with few allowed pairs.
- [[power-law-memory-rules](pages/power-law-memory-rules.md)] - the 1-smooth rule replaced by a Grünwald-Letnikov constraint over all earlier columns; truncated to `K` columns, it is a strip rule on `h^{K−1}` states.
- [[steep-polyominoes-q-motzkin-bessel](pages/steep-polyominoes-q-motzkin-bessel.md)] - Motzkin and q-Motzkin objects among polyominoes; the heights of a 1-smooth strip form a path with steps `−1, 0, +1`.
- [[inscribed-polyomino](pages/inscribed-polyomino.md)], [[marin-2024-polyominoes-in-rectangle](pages/marin-2024-polyominoes-in-rectangle.md)] - the transfer matrix of all polyominoes with bounding box `w × h`, whose states are the `A378947(h)` row states of Marin's automaton (99 at `h = 5`), where a strip needs the `h` heights.
- [[castle-samplers](pages/castle-samplers.md)] - drawing strips at random from a transfer matrix, and the spectra of random 0/1 rule matrices.
- [[zig-zag-castles](pages/zig-zag-castles.md)] - the zig-zag rule, the 1-smooth and plateau-free rules imposed together; its strips are the zig-zag paths of the OEIS, and its castles of height `h` correspond to the `(h − 1)`-balanced strings.
