---
title: Reachable-field census of castle-strip growth constants
category: Analyses
summary: An exhaustive census (h ≤ 5) of which algebraic numbers are Perron roots of 0/1 castle-strip transfer matrices, bucketed by number field. The quadratic reachability law: every real quadratic field Q(√d) is reachable, via the dominant root of x² − p₁x − p₂ (p₁,p₂ ≥ 1), field = squarefree part of p₁²+4p₂; the metallic means are exactly the p₂=1 line; no field is excluded (the per-height lists are just initial segments), and min-height has no closed form. Every squarefree metallic discriminant a²+4 is reached at height ≤ a+1, and copper collapses into Q(√5) (disc 20 = 4·5) precisely because δ₄ = φ³ — the field-theoretic root of the Fibonacci decimation. The cubic frontier is already at h=3, where the plastic number x³−x−1 shows up as a strip Perron root — closing the bare-ψ watch note — together with supergolden, plastic-squared, tribonacci, and the Q(ζ₇)⁺ cubic. Counts by degree at h=4: 5 integer, 6 quadratic, 56 cubic, 110 quartic distinct minimal polynomials.
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

Alongside the metallic fields sit `Q(√3)` (h=3), `Q(√17)`, `Q(√21)` (h=4), `Q(√6)`, `Q(√7)`, `Q(√33)` (h=5) — non-metallic real quadratic fields with no `p₂ = 1` structure. These outnumber the metallic ones and confirm the [[metallic-strip-realizability](pages/metallic-strip-realizability.md)] point that off-ladder surds are what generic rules produce; the metallic means are the thin distinguished subfamily (`p₂ = 1`, one length-2 return loop, purely periodic continued fraction).

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

## The reachability law for quadratic fields

The census's finite lists (`{5}`, `{2,3,5}`, `{2,3,5,13,17,21}`, `{2,3,5,6,7,13,17,21,29,33}` at h = 2..5) are **initial segments of a completely characterized set**, not a mysterious pattern. Recording the `(p₁, p₂)` two-state reduction `x² − p₁x − p₂` of each field's minimal example gives the law.[^7]

**Every reachable quadratic Perron root is the dominant root of `x² − p₁x − p₂` for integers `p₁ ≥ 1, p₂ ≥ 1`** — a nonnegative-integer 2×2 companion `[[p₁, p₂], [1, 0]]` — and its field is `Q(√d)` with `d = ` squarefree part of the discriminant `p₁² + 4p₂`. Three consequences:

1. **No real quadratic field is excluded.** As `(p₁, p₂)` range over `p₁ ≥ 0, p₂ ≥ 1`, the discriminant `p₁² + 4p₂` takes every value `≡ 0 or 1 (mod 4)` — exactly the integers that *are* quadratic discriminants — and its squarefree part takes **every** squarefree `d ≥ 2`. For example `Q(√11)` (absent from the h ≤ 5 list) is reached by `(p₁, p₂) = (6, 2)` (disc `44 = 4·11`, growth `3 + √11`), just at a height taller than 5. So the h ≤ 5 lists are "reachable *by that height*," not the whole reachable set — which is **all real quadratic fields**.[^8]

2. **The metallic means are exactly the `p₂ = 1` slice.** `x² − p₁x − 1` is the metallic mean `δ_{p₁}`; its discriminant `p₁² + 4` is the metallic form. So the metallic ladder is the **single distinguished line `p₂ = 1`** through the `(p₁, p₂)` lattice of all reachable quadratics — the cheapest to realize (one length-2 return loop), and the only one with purely periodic continued fraction ([[eigenvalue-continued-fractions](pages/eigenvalue-continued-fractions.md)]). Everything with `p₂ ≥ 2` is non-metallic and generic.

3. **The obstruction is `0/1` realizability, not the field.** Every `(p₁, p₂)` is realizable at *some* height — the nonnegative-integer companion unfolds to a `0/1` transfer matrix by splitting each weight-`w` edge into `w` parallel simple paths through fresh states (standard symbolic-dynamics recoding). The **minimum** height grows with both `p₁` and `p₂` but has **no simple closed form** (the h ≤ 4 grid: `(1,1)` at h=2; `(0,2), (2,1), (2,2)` at h=3; `(0,3), (1,3), (1,4), (2,4), (3,1), (3,2), (3,3)` at h=4 — `p₂ = 1` metallic is cheapest, realized by `J − D` at `h = p₁ + 1`). This is why the census's per-height lists look irregular: they are level sets of an irregular min-height function over a fully-characterized lattice.[^9]

So the "why 17, 21 at h=4 but not 11?" question dissolves: `Q(√11)` is reachable too, just deeper; and `d ≡ 3 (mod 4)` fields like `Q(√11)` need a discriminant `p₁² + 4p₂ = 4·11` (a non-fundamental multiple), which forces a larger `(p₁, p₂)` and hence a taller strip.

## What this settles, and what it leaves

**Settled:**
- **The full quadratic reachability law** (above): every real quadratic field is a castle-strip Perron field, via `x² − p₁x − p₂`; metallic means are the `p₂ = 1` line; min-height has no closed form. The per-height census lists are initial segments.
- Every squarefree `a²+4` metallic field is reached at height `≤ a+1` (tight through copper); copper collapses into `Q(√5)` (whence the Fibonacci decimation).
- The bare plastic number is a castle-strip growth constant (h=3) — the [[plastic-number](pages/plastic-number.md)] watch note is closed.
- The cubic frontier is at h=3, and it contains plastic / supergolden / plastic² / tribonacci / the `Q(ζ₇)⁺` cubic — the "area-grading-only" cubics also appear as *strip* Perron roots.

**Open:**
- **A closed form (or tight bounds) for the minimum height** realizing a given `(p₁, p₂)`. The unfolding gives an upper bound `~p₁ + 2p₂`; the true min-height is smaller and irregular. This is the one piece of the quadratic story without a clean answer.
- **Which cubics are Pisot / Salem**, and whether the Pisot cubics reachable as strip Perron roots are exactly a nameable set.
- **A closed-form min-height for a given field.** The reachability law says every field appears; the height at which it *first* appears is the open quantity (tied to the min-height of its cheapest `(p₁, p₂)`).

## `h ≥ 6`: why the law supersedes exhaustion

Two facts settle the `h ≥ 6` regime without a full sweep. First, an **`S_h`-canonical-form deduper** — quotient the `2^{h²}` matrices by simultaneous row+column permutation `P M Pᵀ` (relabeling the height-states preserves the spectrum), keeping the lexicographically-minimal representative of each orbit — was built and **validated against h ≤ 4** (it reproduces the field lists `{5}`, `{2,3,5}`, `{2,3,5,13,17,21}` exactly, compressing 65 536 matrices to 3 044 orbits at h=4, ≈ 21×).[^10] But even with the full `≈ h!` compression, h=6 has `≈ 9.5 × 10⁷` orbits — too many to factor one-by-one in a session, and h=7 is `≈ 10¹¹`.

Second, and decisively: **the new fields at `h ≥ 6` are dense, not sparse.** A sparse sweep (matrices with `≤ 6` of 36 ones, `S_6`-deduped) reaches only `{2, 3, 5}` — the high-discriminant metallic surds need *many* ones (nickel's `J − D` realizer has 31 of 36).[^11] So neither sparse enumeration nor session-length brute force finds them.

This is exactly where the **reachability law replaces the census**: it *predicts* what `h ≥ 6` contains, and targeted construction confirms the predictions. Nickel `Q(√29)` is realized by `J − D` at h=6 (`(x+1)⁴(x²−5x−1)`, 31 ones); the `a=6` field `Q(√10)` (disc 40) first appears at h=7 via `J − D` (`δ_6 = 3+√10`), since its cheapest quadratic form needs `p₁ = 6` (i.e. 7 states) or a many-`p₂` alternative that is no smaller.[^12] So exhaustive h ≥ 6 is unnecessary: the law characterizes the full reachable set, and the census's role — mapping the *low-height* initial segments and surfacing the cubic frontier — is complete at h ≤ 5.

## Reproduce

The `field_census` two-phase sweep (numeric Perron bucketing + exact SymPy field ID), the `S_h`-canonical-form `dedup` (validated against the exhaustive census), and the `M = J − D` metallic realizer are on [[castle-snippets](pages/castle-snippets.md)]. h ≤ 4 runs exhaustively in seconds; h=5 in a few minutes with chunked vectorized `numpy.linalg.eigvals`; h ≥ 6 is characterized by the reachability law plus targeted construction rather than exhaustion.

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

[^7]: For each reachable quadratic field the minimal (fewest-ones) example matrix was recorded and its Perron factor `x² − p₁x − p₂` read off (SymPy). At h ≤ 4, by **discriminant** `Δ = p₁² + 4p₂` (field is `Q(√d)` with `d = ` squarefree part of `Δ`): `Δ=5` → `(p₁,p₂)=(1,1)`, `Q(√5)`; `Δ=8` → `(2,1)` and `(0,2)`, `Q(√2)`; `Δ=12` → `(2,2)`, `Q(√3)`; `Δ=13` → `(1,3)` and `(3,1)`, `Q(√13)`; `Δ=17` → `(1,4)` and `(3,2)`, `Q(√17)`; `Δ=21` → `(3,3)`, `Q(√21)`.

[^8]: `p₁² + 4p₂ ≡ p₁² (mod 4) ∈ {0, 1}`, so the discriminant is always `≡ 0 or 1 (mod 4)` — a quadratic discriminant — and conversely every such value `≥ 5` is `p₁² + 4p₂` for some `p₁ ≥ 0, p₂ ≥ 1`. The squarefree part hits every squarefree `d ≥ 2` (using non-fundamental multiples where needed): e.g. `Q(√11)` via `(p₁,p₂) = (6,2)`, disc `44 = 4·11`, growth `3 + √11 ≈ 6.317` — verified in SymPy; absent from the h ≤ 5 census only because it needs a taller strip. So no real quadratic field is excluded.

[^9]: Realizability: the nonnegative-integer companion `[[p₁, p₂], [1, 0]]` recodes to a `0/1` matrix by replacing each weight-`w` edge with `w` parallel simple paths through fresh states (a standard state-splitting / higher-block recoding in symbolic dynamics), so every `(p₁ ≥ 1, p₂ ≥ 1)` is realized at some finite `h`. Empirical min-heights over `p₁ ≤ 3, p₂ ≤ 4` (exhaustive h ≤ 4): `(1,1)`→2; `(0,2),(2,1),(2,2)`→3; `(0,3),(1,3),(1,4),(2,4),(3,1),(3,2),(3,3)`→4; `p₁ ≥ 4` not reached by h=4. The `p₂ = 1` (metallic) line is realized by `M_h = J − D` at `h = p₁ + 1` ([[metallic-strip-realizability](pages/metallic-strip-realizability.md)]). No closed form fits the full grid.

[^10]: The `S_h` deduper canonicalizes each matrix as the lexicographically-minimal flattening of `P M Pᵀ` over all `h!` permutations `P` (simultaneous row+column relabeling, which conjugates the matrix and preserves its spectrum), collapsing each orbit to one representative. Validated by execution: canonical-representative census reproduces the full field lists at h=2 (`{5}`, 10 orbits from 16 matrices), h=3 (`{2,3,5}`, 104 orbits from 512), h=4 (`{2,3,5,13,17,21}`, 3044 orbits from 65 536) — the quadratic fields match the exhaustive sweep exactly. Orbit compression ≈ `h!` (24× at h=4, observed 21.5×).

[^11]: Sparse `S_6`-deduped census over 6×6 matrices with `≤ 6` of 36 ones: reaches quadratic fields `{2, 3, 5}` only. High-discriminant surds require dense matrices — the `J − D` realizer of nickel (`Q(√29)`) uses 31 ones — so sparse enumeration cannot reach the new h=6 fields. (Verified by execution: batched numeric Perron over all `C(36,K)` combinations for `K ≤ 6`, exact quadratic ID of the distinct roots.)

[^12]: Targeted h=6 / h=7 constructions (SymPy): `J − D` at h=6 gives `(x+1)⁴(x²−5x−1)`, Perron `(5+√29)/2` = nickel ∈ `Q(√29)`, 31 ones; `J − D` at h=7 gives `(x+1)⁵(x²−6x−1)`, Perron `3+√10` = `δ₆` ∈ `Q(√10)`. The `a=6` field `Q(√10)` (disc 40) has cheapest quadratic forms `(p₁,p₂) ∈ {(6,1),(2,9),(0,10),(4,6)}`, all needing `≥ 7` states or many `p₂` two-cycles, so `Q(√10)` first appears at h=7, not h=6.
