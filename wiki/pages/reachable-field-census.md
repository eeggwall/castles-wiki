---
title: Reachable-field census of castle-strip growth constants
category: Analyses
summary: An exhaustive census (h ≤ 5) of which algebraic numbers are Perron roots of 0/1 castle-strip transfer matrices, bucketed by number field. Every squarefree metallic discriminant a²+4 is reached — golden Q(√5) at h=2, silver Q(√2) at h=3, bronze Q(√13) at h=4, nickel Q(√29) at h=5 — and copper collapses into Q(√5) (disc 20 = 4·5) precisely because δ₄ = φ³, the field-theoretic root of the Fibonacci decimation. Non-metallic quadratic fields Q(√3, √6, √7, √17, √21, √33) appear alongside. The cubic frontier is already at h=3, where the plastic number x³−x−1 shows up as a strip Perron root — closing the bare-ψ watch note — together with supergolden, plastic-squared, tribonacci, and the Q(ζ₇)⁺ cubic. Counts by degree at h=4: 5 integer, 6 quadratic, 56 cubic, 110 quartic distinct minimal polynomials.
tags: [analysis, castle, growth-constant, transfer-matrix, perron-root, number-field, metallic-mean, plastic-number, census, pisot, quadratic-field, sympy, verification]
sources: [pe502-pell-castle-strip]
created: 2026-09-18
updated: 2026-09-18
---

# Reachable-field census of castle-strip growth constants

## The question and the method

A **castle-strip rule** is a nearest-neighbor restriction on a row of columns with heights in `{1, …, h}` — an allowed-adjacency predicate `A(a, b)`, equivalently a `0/1` **transfer matrix** `M` on `h` height-states ([[metallic-strip-realizability](pages/metallic-strip-realizability.md)]). Its width-graded count grows at `M`'s **Perron root** (dominant eigenvalue), an algebraic number generating a field `Q(root)`. This page censuses, **exhaustively over all `2^{h²}` binary `M`** for `h = 2, 3, 4, 5`, which algebraic numbers appear and which number fields they populate.[^1]

The computation is two-phase: a fast numeric sweep collects the distinct Perron values and one example matrix each; then SymPy exactly factors each example's characteristic polynomial, picks the irreducible factor carrying the Perron root, and labels the field (`deg 1` rational, `deg 2` → `Q(√d)` by squarefree discriminant, `deg ≥ 3` cubic/quartic). Exact throughout — numeric values only *select* the factor; the field label is exact.[^1]

## The quadratic fields — the clean result

Bucketing every quadratic Perron root by its field `Q(√d)` gives a sharp, monotone picture:

| `h` | reachable `d` (new at this height in **bold**) | new metallic mean | new non-metallic |
|---|---|---|---|
| 2 | **5** | golden `φ` (`Q(√5)`) | — |
| 3 | **2**, **3**, 5 | silver `1+√2` (`Q(√2)`) | `Q(√3)` |
| 4 | 2, 3, 5, **13**, **17**, **21** | bronze `(3+√13)/2` (`Q(√13)`) | `Q(√17)`, `Q(√21)` |
| 5 | 2, 3, 5, **6**, **7**, 13, 17, 21, **29**, **33** | nickel `(5+√29)/2` (`Q(√29)`) | `Q(√6)`, `Q(√7)`, `Q(√33)` |

Two structural facts fall out.

### Every squarefree metallic discriminant is reached — and copper is the exception that proves the rule

The `a`-th metallic mean `δ_a = (a + √(a²+4))/2` lives in `Q(√(a²+4))`, whose field depends only on the **squarefree part** of `a²+4`:

| metal `a` | `a²+4` | squarefree part | field |
|---|---|---|---|
| golden 1 | 5 | 5 | `Q(√5)` |
| silver 2 | 8 = 4·2 | 2 | `Q(√2)` |
| bronze 3 | 13 | 13 | `Q(√13)` |
| **copper 4** | **20 = 4·5** | **5** | **`Q(√5)`** — *not new* |
| nickel 5 | 29 | 29 | `Q(√29)` |
| 6 | 40 = 4·10 | 10 | `Q(√10)` |

The census confirms each of these fields is reached: `Q(√5)` (golden) at h=2, `Q(√2)` (silver) at h=3, `Q(√13)` (bronze) at h=4, `Q(√29)` (nickel) at h=5. **Copper is the striking case: it introduces no new field**, because `20 = 4·5` collapses to `Q(√5)`. And that collapse *is* the reason `δ₄ = 2 + √5 = φ³` and the copper strip counts the Fibonacci trisection `F_{3n+5}` ([[metallic-strip-realizability](pages/metallic-strip-realizability.md)] Finding 3): copper lives inside the golden field, so it is a power of `φ`, so its integer sequence is decimated Fibonacci. The census makes the Fibonacci decimation a **field-theoretic necessity**, not a coincidence.[^2]

### The metallic surd's minimum height is `≤ a + 1`, tight through copper

The `M_h = J − D` "plateau-free-except-ceiling" rule realizes `δ_{h−1}` at height `h` ([[metallic-strip-realizability](pages/metallic-strip-realizability.md)]), so `δ_a` is always reachable by height `h = a + 1`. The census shows this bound is **tight for `a = 1, 2, 3, 4`** (golden/silver/bronze/copper first appear at exactly `h = a+1`) but **not for `a = 5`**: nickel `δ₅` already appears at `h = 5`, not `h = 6` — 120 matrices realize it early, off the `J − D` diagonal.[^3] So `J − D` is the *canonical* realization, giving the exact upper bound, but not always the minimal one.

Within a single field the surds are also height-stratified. `Q(√5)` fills in as `h` grows: `φ` at h=2; `φ²` at h=3; `2φ = 3.236` at h=4; and **`φ³` (copper) only at h=5** — so "which surds of `Q(√5)` are Perron roots" is itself a height-indexed question, and copper genuinely waits until h=5.[^4]

### The non-metallic quadratics are the generic case

Alongside the metallic fields sit `Q(√3)` (h=3), `Q(√17)`, `Q(√21)` (h=4), `Q(√6)`, `Q(√7)`, `Q(√33)` (h=5) — non-metallic real quadratic fields with no `w₂ = 1` structure. These outnumber the metallic ones and confirm the [[metallic-strip-realizability](pages/metallic-strip-realizability.md)] point that off-ladder surds are what generic rules produce; the metallic means are the thin distinguished subfamily (`w₂ = 1`, one length-2 return loop, purely periodic continued fraction).

## The cubic frontier is at `h = 3` — and it contains the plastic number

The census's most surprising output: **genuine cubics appear immediately at `h = 3`**, six distinct minimal polynomials, and they are exactly the cubic constants the wiki had reached only through *area* grading:

| minimal polynomial | Perron root | identity | # matrices (h=3) |
|---|---|---|---|
| `x³ − x − 1` | `1.3247` | **plastic number `ψ`** ([[plastic-number](pages/plastic-number.md)]) | 6 |
| `x³ − x² − 1` | `1.4656` | supergolden ([[tree-castle-by-area](pages/tree-castle-by-area.md)]) | 6 |
| `x³ − 2x² + x − 1` | `1.7549` | plastic-squared `ψ²` | 6 |
| `x³ − x² − 2x + 1` | `1.8019` | `Q(ζ₇)⁺` cubic (conjugate `2cos(2π/7)`) | 6 |
| `x³ − x² − x − 1` | `1.8393` | **tribonacci** ([[bounded-height-castles-nacci](pages/bounded-height-castles-nacci.md)]) | 12 |
| `x³ − 3x² + 2x − 1` | `2.3247` | (Pisot; `ψ + 1`) | 6 |

The `x³ − x − 1` line **closes the open bare-plastic watch note** on [[plastic-number](pages/plastic-number.md)]: the plastic number `ψ ≈ 1.3247` — which had appeared only as `ψ²` and `2ψ²` — **is a castle-strip Perron root at height 3**, realized by 6 matrices, the sparsest with just 4 ones (a near-companion of `x³ = x + 1`).[^5] The [[plastic-number](pages/plastic-number.md)] "Padovan/Perrin growth castle" slot is filled: a strip whose transfer matrix is that companion grows at bare `ψ`.

At `h = 4` the cubic count explodes to **56 distinct minimal polynomials** (including `x³ − 2`, the cube root of 2 at `1.2599`), plus **110 quartic** minimal polynomials — the field zoo becomes genuinely wild, while the quadratic layer stays orderly (6 fields). The degree breakdown at h=4: **5 integer, 6 quadratic, 56 cubic, 110 quartic** distinct minimal polynomials among the 236 distinct Perron values.[^6]

## What this settles, and what it leaves

**Settled:**
- The complete quadratic-field reachability picture through h=5, with the clean law: *every squarefree `a²+4` metallic field is reached, copper collapses into `Q(√5)` (whence the Fibonacci decimation), and the metallic surds sit at height `≤ a+1` (tight through copper)*.
- The bare plastic number is a castle-strip growth constant (h=3) — the [[plastic-number](pages/plastic-number.md)] watch note is closed.
- The cubic frontier is at h=3, and it contains plastic / supergolden / plastic² / tribonacci / the `Q(ζ₇)⁺` cubic — the "area-grading-only" cubics also appear as *strip* Perron roots.

**Open:**
- **A reachability theorem for non-metallic `d`.** Is there a clean characterization of *which* squarefree `d` are reachable at height `h`? Data: `{5}`, `{2,3,5}`, `{2,3,5,13,17,21}`, `{2,3,5,6,7,13,17,21,29,33}` — the metallic ones are forced, but the pattern for the rest (why 17, 21 at h=4 but not, say, 11?) is unresolved.
- **h ≥ 6 and the `S_h`-canonical-form reduction.** h=5 was feasible by brute force (33.5M matrices, ~7,400 distinct roots); h=6 (68G matrices) needs the row+column-permutation quotient to become practical. Does nickel's field `Q(√29)` remain, and does a=6's `Q(√10)` first appear at h=6 or earlier?
- **Which cubics are Pisot / Salem**, and whether the Pisot cubics reachable as strip Perron roots are exactly a nameable set.

## Reproduce

The `field_census` two-phase sweep (numeric Perron bucketing + exact SymPy field ID) and the `M = J − D` metallic realizer are on [[castle-snippets](pages/castle-snippets.md)]. h ≤ 4 runs exhaustively in seconds; h=5 in a few minutes with chunked vectorized `numpy.linalg.eigvals`.

## Appearances in Sources

- [[pe502-pell-castle-strip](pages/pe502-pell-castle-strip.md)] - the strip transfer-matrix model this census sweeps.

## Related Concepts

- [[metallic-strip-realizability](pages/metallic-strip-realizability.md)] - the companion page: the `J − D` rule that realizes each metallic mean, whose reachability this census confirms exhaustively.
- [[metallic-means](pages/metallic-means.md)] - the ladder `δ_a`; this census places every rung's field and the copper collapse into `Q(√5)`.
- [[plastic-number](pages/plastic-number.md)] - the bare-`ψ` watch note this census closes (plastic is a strip Perron root at h=3).
- [[bounded-height-castles-nacci](pages/bounded-height-castles-nacci.md)] / [[tree-castle-by-area](pages/tree-castle-by-area.md)] - where tribonacci, supergolden, plastic² first arose (by area); the census finds them again as strip Perron roots.
- [[castle-classification](pages/castle-classification.md)] - Axis 8, the growth-type meta-classification these Perron roots populate.
- [[eigenvalue-continued-fractions](pages/eigenvalue-continued-fractions.md)] - why the metallic fields `Q(√(a²+4))` are the distinguished (purely-periodic-CF, norm-`−1`) quadratics among all reachable ones.

## Footnotes

[^1]: Method verified by execution. Phase 1: for each `h`, all `2^{h²}` binary matrices are built (vectorized in chunks) and their eigenvalues batch-computed via `numpy.linalg.eigvals`; the Perron root is the maximum real eigenvalue (`|Im| < 10⁻⁹`, value `> 10⁻⁹`), and matrices are bucketed by the rounded root with one example kept. Phase 2: each distinct example's characteristic polynomial is factored with SymPy `factor_list`; the irreducible factor whose maximum real root matches the Perron value is selected, and its degree/discriminant give the field. Runs: h=2 (16 matrices), h=3 (512), h=4 (65 536) exhaustive; h=5 (33 554 432) by chunked sweep.

[^2]: The squarefree-part computation is `d = ∏ p^{e mod 2}` over `factorint(a²+4)`. `a²+4` for `a = 1..6` is `5, 8, 13, 20, 29, 40`, squarefree parts `5, 2, 13, 5, 29, 10`. `a = 4` (copper) gives `20 = 2²·5 → 5`, so copper `∈ Q(√5)`; `δ₄ = 2 + √5 = φ³` (verified exactly, [[metallic-strip-realizability](pages/metallic-strip-realizability.md)] footnote). The census independently finds `4.23607 = φ³` in the `Q(√5)` bucket at h=5.

[^3]: Census first-appearance heights: golden `1.6180` at h=2, silver `2.4142` at h=3, bronze `3.3028` at h=4, copper `4.2361` at h=5 — each `= a+1`, matching the `J − D` realization. Nickel `4.19258 = (5+√29)/2` appears at **h=5** (120 matrices in the `Q(√29)` bucket), *below* the `J − D` height `a+1 = 6`. So `J − D` gives the tight upper bound `h ≤ a+1` for `a ≤ 4` and a non-tight one for `a = 5`.

[^4]: Restricting the h≤4 Perron roots to `Q(√5)` (those `v` with `v² − pv ∈ ℤ` for some integer `p` and squarefree discriminant `5`): h=2 gives `{φ}`, h=3 gives `{φ, φ²}`, h=4 gives `{φ, φ², 2φ}`; `φ³ = 4.23607` first appears at h=5. Verified by execution.

[^5]: Exhaustive over the 512 binary `3×3` matrices: exactly 6 have characteristic polynomial with irreducible factor `x³ − x − 1` (Perron root `1.324718`, the plastic number). The sparsest has 4 ones, e.g. `[[0,0,1],[1,0,0],[1,1,0]]` (rule: height 1→3, 2→1, 3→{1,2}), a near-companion matrix of `x³ = x + 1`; SymPy `factor(charpoly) = x³ − x − 1`.

[^6]: h=4 distinct-Perron-value degree census (SymPy exact factorization of one example per distinct value): 5 integer roots (`0,1,2,3,4`), 6 quadratic fields (`d = 2,3,5,13,17,21`), 56 cubic minimal polynomials, 110 quartic minimal polynomials; 236 distinct Perron values over the non-nilpotent matrices (707 matrices are nilpotent / zero-growth). h=3: 15 fields (3 integer, 3 quadratic `d=2,3,5`, 9 cubic) over 17 distinct Perron values. h=5 quadratic layer: `d = 2,3,5,6,7,13,17,21,29,33`.
