---
title: The castle strip - bridge to transfer matrices
category: Concepts
summary: A castle strip is a castle read left-to-right as a sequence of columns, one column at a time. The rule "which column heights may sit next to which" is an h×h 0/1 transfer matrix M whose rows and columns are indexed by the allowed heights {1, …, h}: M[a][b] = 1 means a height-a column may be immediately followed by a height-b column. Counting strips of width w is then matrix powers (𝟙ᵀM^{w−1}𝟙), the width generating function has denominator dividing det(I − xM), and the growth constant is M's largest eigenvalue (Perron root). The metallic-mean and reachable-field results are about this object; the states are the heights.
tags: [concept, castle, transfer-matrix, strip, height, perron-root, growth-constant, generating-function, pedagogy, bridge]
sources: [pe502-pell-castle-strip]
created: 2026-09-18
updated: 2026-09-28
---

# The castle strip - bridge to transfer matrices

## Purpose

Several wiki pages — [[pell-castle-strip](pages/pell-castle-strip.md)], [[metallic-strip-realizability](pages/metallic-strip-realizability.md)], [[reachable-field-census](pages/reachable-field-census.md)] — talk about "castle strips," "transfer matrices," and "height-states," and derive growth constants from the eigenvalues of small 0/1 matrices. This page builds that machinery from scratch: what a strip is, why a matrix describes it, and that **the matrix's rows and columns are the allowed column heights**, which the other pages assume.

## What a castle strip is

A **castle** is a skyline `c = (c_1, …, c_w)` — a row of `w` columns, column `i` having integer height `c_i` between `1` and `h` ([[castle-representations](pages/castle-representations.md)]). A **castle strip** is the same object read **left to right, one column at a time**, together with a **rule** saying which heights are allowed to be neighbors.

The rule is a yes/no question about each *adjacent pair* of columns:

> given a column of height `a`, is a column of height `b` allowed immediately to its right?

Call that predicate `A(a, b)` (`A` for "allowed"). A castle strip of width `w` is any sequence `c_1, c_2, …, c_w` of heights in `{1, …, h}` such that every adjacent pair passes the rule: `A(c_1, c_2)`, `A(c_2, c_3)`, …, all true. Different rules carve out different families:

- `A(a, b) =` **always true** → *every* skyline is allowed (the unrestricted strip).
- `A(a, b) = (a ≠ b)` → no two equal-height neighbors (the "plateau-free" strip).
- `A(a, b) = (|a − b| ≤ 1)` → heights change by at most 1 (the "1-smooth" / Motzkin strip).

The word "strip" emphasizes that we walk along one dimension (left to right, the **width**), deciding each next column from the current one — a one-dimensional sweep across the castle.

## The transfer matrix: the states are the heights

A rule `A(a, b)` on heights `{1, …, h}` is exactly an **`h × h` matrix `M` of 0s and 1s**, where

```
M[a][b] = 1   if a column of height a may be followed by a column of height b   (i.e. A(a, b) is true),
M[a][b] = 0   otherwise.
```

**Row `a` and column `b` are indexed by the heights themselves**: the `h` "states" of the transfer matrix are the `h` possible column heights `1, 2, …, h`. When a later page says "a 0/1 transfer matrix on `h` height-states," it means exactly this `h × h` matrix, and "`h = 4`" means "column heights run 1 to 4."

Entry `M[a][b]` reads as a sentence: **"can a height-`a` column stand next to a height-`b` column?"** — 1 for yes, 0 for no. The matrix is just the rule's truth table laid out as a grid.

## A worked example you can check by hand

Take `h = 2` (heights `1` and `2`) and the rule "**anything may follow anything**" — every pair allowed. The matrix is

```
        to height 1   to height 2
from 1 [     1             1      ]
from 2 [     1             1      ]
```

`M = [[1, 1], [1, 1]]`. Now count strips of each width by hand and check the matrix reproduces them:

- **width 1:** heights `1` or `2` → **2** strips.
- **width 2:** any of `(1,1), (1,2), (2,1), (2,2)` — all allowed → **4** strips.
- **width 3:** `2 × 2 × 2` = **8** strips.

The matrix machinery gives the same counts. The number of allowed width-`w` strips is

```
(number of width-w strips)  =  𝟙ᵀ M^{w−1} 𝟙,
```

where `𝟙` is the all-ones column vector (length `h`) and `𝟙ᵀ` its transpose. Reading it: start in any height (`𝟙` on the right picks all `h` starting heights), take `w − 1` steps (each `M` multiply appends one more allowed column), and total over all ending heights (`𝟙ᵀ` on the left). For `M = [[1,1],[1,1]]`:

- `w = 1`: `𝟙ᵀ𝟙 = 2` ✓
- `w = 2`: `𝟙ᵀ M 𝟙 = 4` ✓
- `w = 3`: `𝟙ᵀ M² 𝟙 = 8` ✓

Change the rule and the matrix changes. "No two equal neighbors" (`a ≠ b`) at `h = 2` is `M = [[0, 1], [1, 0]]`: from height 1 you must go to 2 and vice versa, so the only strips are the alternating ones `1,2,1,2,…` and `2,1,2,1,…` — exactly **2 strips of every width**, which `𝟙ᵀ M^{w−1} 𝟙 = 2` confirms.

## Reading the growth constant and the generating function

Two quantities fall straight out of `M`, and they are what the advanced pages actually use.

**Growth constant = largest eigenvalue.** As the width `w` grows, the strip count `𝟙ᵀ M^{w−1} 𝟙` grows like `λ^w`, where `λ` is the **largest eigenvalue of `M`** — its **Perron root** (largest eigenvalue of a nonnegative matrix, guaranteed real and positive when the strip is "connected"). For `M = [[1,1],[1,1]]` the eigenvalues are `2` and `0`, so the count grows like `2^w` — matching `2, 4, 8, …`. This `λ` is the **growth constant** that [[metallic-means](pages/metallic-means.md)] and [[reachable-field-census](pages/reachable-field-census.md)] study: which numbers `λ` arise this way, from a 0/1 rule matrix.

**Generating function: denominator `det(I − xM)`.** Packaging the width counts into one power series `∑_{w ≥ 1} (\text{count}) x^{w−1}` gives the rational function `𝟙ᵀ (I − xM)^{−1} 𝟙`, whose denominator divides `det(I − xM)` (a factor can cancel, as the `(1 − x)` of the 1-smooth strip does on [[pell-castle-strip](pages/pell-castle-strip.md)]). The denominator's degree, roots, and coefficients are the strip's C-finite fingerprint ([[generating-functions](pages/generating-functions.md)]); the growth constant `λ` is `1/ρ` for `ρ` the smallest-modulus root of `det(I − xM)`. For the two-height examples the denominators have degree at most 2, so their growth constants are integers or quadratic irrationals, as in the metallic-means pages ([[metallic-strip-realizability](pages/metallic-strip-realizability.md)]).

## How the strip relates to a real castle

The strip is a **rule-restricted, single-height-band slice** of the castle world, and it connects to Project Euler 502 (PE 502)'s actual castles in two ways:

- **The unrestricted `h`-height strip is "all castles of height ≤ h" graded by width.** With `A(a,b)` always true, `M` is the all-ones `h × h` matrix `J`, growth constant `h` (its Perron root), count `h^w`. That is the full count of castles of height at most `h`: PE 502's rules 1-5 impose no neighbor restriction, because blocks are the maximal runs of each row and the rule-3 gap is automatic ([[castle-counting-formula](pages/castle-counting-formula.md)]).
- **Named sub-families are specific strips.** The 1-smooth rule `|a − b| ≤ 1` on heights `{1, 2, 3}`, started at height 1, is the Pell strip `1/(1 − 2x − x²)` ([[pell-castle-strip](pages/pell-castle-strip.md)]); the tower word, a Motzkin-path language ([[tower-word-continued-fraction](pages/tower-word-continued-fraction.md)]), has the same silver growth. A "castle-strip rule" is thus a **candidate castle sub-family** — pick a neighbor rule, and its growth constant is a Perron root you can compute from the matrix.

The [[castle-graph](pages/castle-graph.md)] reads eigenvalues off an individual castle's cell adjacency; the strip reads a growth constant off a *class's* height-adjacency rule.

## Vocabulary crosswalk

Because several pages use compressed phrasings, here is the plain-language key:

| phrase you'll see | what it means here |
|---|---|
| "transfer matrix on `h` height-states" | the `h × h` 0/1 rule matrix; states = heights `1..h` |
| "`M[a][b] = 1`" | height-`a` column may be followed by height-`b` column |
| "Perron root of `M`" | largest eigenvalue = width-growth constant of the strip |
| "denominator `det(I − xM)`" | the strip's generating-function denominator (C-finite recurrence) |
| "`p₁, p₂`" (in `1 − p₁x − p₂x²`) | coefficients of a quadratic strip denominator (not widths, not states) ([[metallic-strip-realizability](pages/metallic-strip-realizability.md)]) |
| "minimum height for a growth constant" | smallest `h` (= smallest matrix / fewest distinct heights) whose 0/1 rule matrix has that Perron root |
| "`J − D` rule / ceiling exception" | a specific rule matrix (all-ones minus near-identity) realizing the metallic means ([[metallic-strip-realizability](pages/metallic-strip-realizability.md)]) |

## Reproduce

The one-line strip counter and growth-constant / field probes are on [[castle-snippets-strips](pages/castle-snippets-strips.md)] (`strip_field_census`, `ceiling_exception_ladder`, `sh_canonical`). The minimal counter is just `numpy`: build `M` from your rule, then `ones @ numpy.linalg.matrix_power(M, w-1) @ ones` for the width-`w` count, or `max(numpy.linalg.eigvals(M).real)` for the growth constant.

## Related Concepts

- [[pell-castle-strip](pages/pell-castle-strip.md)] - the worked seminar: the anchored 1-smooth height-3 strip is `1/(1 − 2x − x²)`, growth `1 + √2` (silver).
- [[metallic-strip-realizability](pages/metallic-strip-realizability.md)] - which growth constants `λ` are strip Perron roots; the `p₁/p₂` two-knob reduction and the `J − D` metallic realizer.
- [[reachable-field-census](pages/reachable-field-census.md)] - the exhaustive census of strip Perron roots by number field; the reachability law.
- [[metallic-means](pages/metallic-means.md)] - the ladder of growth constants `δ_a` these strips realize.
- [[castle-graph](pages/castle-graph.md)] - the sibling bridge: individual-castle cell-adjacency and its spectrum (Axis 9), as opposed to the strip's class-level height-adjacency.
- [[castle-representations](pages/castle-representations.md)] - the skyline `(c_1, …, c_w)` a strip walks along.
- [[generating-functions](pages/generating-functions.md)] - why `1/det(I − xM)` is the width GF and how its denominator encodes the recurrence.
- [[castle-classification-growth](pages/castle-classification-growth.md)] - Axis 8, where a strip's growth constant classifies its castle class ("`<metal>` width growth castle").
- [[aocp-generating-permutations-tuples](pages/aocp-generating-permutations-tuples.md)] - the other way to walk `{1..h}^w`: Algorithm M visits skylines one at a time (the odometer), the strip's transfer matrix counts them all at once (the automaton).
- [[castle-compression](pages/castle-compression.md)] - a strip rule is the "tiny state machine" of the compressibility axis' Tier 1: skylines that look irregular but are generated by a handful of matrix ones.
- [[power-law-memory-rules](pages/power-law-memory-rules.md)] - the non-Markov generalization: replace `A(a, b)` on one adjacent pair with a Grunwald-Letnikov constraint reaching back over every prior column, K-truncate to an `h^{K-1}`-state 0/1 transfer matrix, and its Perron root ratchets through the reachable-field census as `K` grows.
- [[steep-polyominoes-q-motzkin-bessel](pages/steep-polyominoes-q-motzkin-bessel.md)] - Motzkin and q-Motzkin objects on the polyomino side; the 1-smooth strip's height sequence is a Motzkin-type path (steps −1, 0, +1).
- [[castle-samplers](pages/castle-samplers.md)] - drawing strips at random from the transfer matrix, and drawing random rules (random 0/1 matrices) whose bulk spectra follow the circular and semicircle laws.
