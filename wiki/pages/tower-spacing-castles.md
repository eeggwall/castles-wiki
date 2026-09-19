---
title: Minimum-tower-spacing castles
category: Analyses
summary: A castle sub-family from a horizontal-gap variation of PE 502's rule 3: require every valley between raised regions to be at least g columns wide, equivalently every row's internal empty-runs have length ≥ g. This is a tower-spacing rule (towers poking above a valley must be ≥ g apart), distinct from the height-adjacency strip rules of metallic-strip-realizability. A column-by-column transfer matrix (states track, per row, how long since the last filled cell, capped at g) counts them exactly. At height 2 the family is "height-2 towers spaced ≥ g apart", with a clean parity split: even g gives the irreducible denominator 1 − 2x + x² − x^{g+1} (g=2 is plastic-squared ψ²), odd g = 2k−1 factors as (x^k − x + 1)(x^k + x − 1) with growth the root of x^k + x − 1 (g=3 is golden φ). Growth constants decrease toward 1 as g grows. For g ≥ 2, h ≥ 3 the growth constants are a non-metallic two-parameter algebraic family; e.g. (h=3, g=2) grows at 2.4022 (root of an irreducible quintic), not silver. The g=2 column turns out to be the Hardin word sequences (A202882 / A203094 / A203184) — tower-spacing-2 forbids an isolated peak, exactly Hardin's "no strict local maximum" — giving those sequences a third, geometric castle interpretation.
tags: [analysis, castle, gap-rule, tower-spacing, transfer-matrix, growth-constant, plastic-number, golden-ratio, generating-function, rule-3, sympy, verification]
sources: [pe502-pell-castle-strip]
created: 2026-09-18
updated: 2026-09-19
---

# Minimum-tower-spacing castles

## The rule variation

Project Euler 502 (PE 502)'s **rule 3** says that within any row, two neighboring filled blocks must be separated by at least one empty cell ([[castle-polyomino](pages/castle-polyomino.md)]). The **minimum-tower-spacing** variation strengthens the "at least one" to **at least `g`**: in every row, each *internal* run of empty cells (a run with filled cells on both sides) must have length `≥ g`.

Geometrically this is a **tower-spacing rule**. In a castle skyline `c = (c_1, …, c_w)`, row `r` is filled exactly at the columns `i` with `c_i ≥ r`; two "towers" that both reach row `r`, separated by a valley of columns shorter than `r`, produce a filled-empty-filled pattern `1…10…01…1` in that row. The rule says the valley — the `0`-run — must be at least `g` wide. So towers poking above a common level must stand at least `g` columns apart.[^1]

The bottom row of a castle is always solid (bottom-aligned, `c_i ≥ 1`), so it has no internal gaps and the rule never constrains it. The rule bites only on rows `2, …, h`, i.e. only where there is a valley between raised sections — exactly the shapes like `(2, 1, 2)` (row 2 = `101`, a width-1 valley) that `g = 2` forbids.

**This is a horizontal-gap variation, distinct from the height-adjacency strips of [[metallic-strip-realizability](pages/metallic-strip-realizability.md)].** There the transfer matrix's states are the *column heights* and the rule restricts which heights may be *neighbors*; here the rule restricts the *horizontal spacing* of towers across a valley. Different knob, same transfer-matrix / growth-constant methodology ([[castle-strip](pages/castle-strip.md)]).

## The transfer matrix

Sweep the castle **column by column**. A column is a single height value `c_i ∈ {1, …, h}` (rows `1..c_i` filled). The state must record, **for each constrained row `r = 2, …, h`**, how the gap constraint stands:

- `pre` — no filled cell seen yet in this row (a leading run of empties; unconstrained);
- `fill` — the previous column filled this row;
- `g1, …, g_{g−1}` — currently `k` consecutive empty cells since the last fill, with `k < g` (an internal gap still too short to allow a refill).

Once an empty run reaches length `g` it is "safe" — a later fill is legal — so it collapses back to the `pre` state. The transition for a new column of height `c_i`: row `r` is filled iff `c_i ≥ r`; a fill is **forbidden** (kills the transition) precisely when the row is in a `g_k` state with `k < g` (that would close a gap shorter than `g`). This gives an exact `s × s` nonnegative-integer transfer matrix `M`, where `s` is the number of legal per-row-state tuples, and the width-`w` count is `𝟙ᵀ M^w` summed over states.[^2]

The construction was verified against brute-force enumeration for `(h, g) ∈ {(2,2), (3,2), (3,3), (4,2)}`, matching term for term through width 7.[^2]

## Height 2: towers spaced `≥ g` apart

At `h = 2` only row 2 is constrained, so the object is clean: **place height-2 towers along a width-`w` base so that consecutive towers are separated by at least `g` empty (height-1) columns.** The counts and their growth constants split by the parity of `g`:[^3]

| `g` | denominator `det(I − xM)` | growth | identity |
|---|---|---|---|
| 2 | `1 − 2x + x² − x³` | `1.75488` | **plastic-squared `ψ²`** ([[plastic-number](pages/plastic-number.md)]) |
| 3 | `(x² − x + 1)(x² + x − 1)` | `1.61803` | **golden `φ`** (`x² + x − 1` factor) |
| 4 | `1 − 2x + x² − x⁵` | `1.52895` | root of the irreducible quintic |
| 5 | `(x³ − x + 1)(x³ + x − 1)` | `1.46557` | root of `x³ + x − 1` |
| 6 | `1 − 2x + x² − x⁷` | `1.41780` | → `√2` from above |
| 7 | `(x⁴ − x + 1)(x⁴ + x − 1)` | `1.38028` | root of `x⁴ + x − 1` |

The pattern is exact:

- **Even `g`:** the denominator is `1 − 2x + x² − x^{g+1}`, irreducible for `g ≥ 4`; at `g = 2` it is the plastic-squared denominator `1 − 2x + x² − x³` (reverse of `x³ − x² + 2x − 1`), so height-2 castles with towers `≥ 2` apart satisfy the **A005251** recurrence `a(n) = 2a(n−1) − a(n−2) + a(n−3)` — a *third* castle appearance of the plastic-squared sequence, joining the Hardin word count and the `h → ∞` tree castles by area ([[tree-castle-by-area](pages/tree-castle-by-area.md)]), and reached here by an entirely different (horizontal-spacing) mechanism.[^4]
- **Odd `g = 2k − 1`:** the denominator factors as `(x^k − x + 1)(x^k + x − 1)`, and the growth constant is the dominant root of `x^k + x − 1`. At `k = 1` (`g = 1`, the trivial rule) this degenerates; at `k = 2` (`g = 3`) it is `x² + x − 1`, the **golden ratio** `φ`; at `k = 3` (`g = 5`) it is `x³ + x − 1 ≈ 1.4656`; and so on.[^3]

The growth constant **decreases monotonically toward `1`** as `g → ∞`: forcing towers ever farther apart makes valid configurations ever sparser, so the count grows ever more slowly.

## The full family: a two-parameter algebraic zoo

For general height `h` and spacing `g`, the transfer-matrix Perron root gives:[^5]

| `h \ g` | 2 | 3 | 4 | 5 |
|---|---|---|---|---|
| 2 | 1.7549 | 1.6180 | 1.5289 | 1.4656 |
| 3 | 2.4022 | 2.1069 | 1.9274 | 1.8051 |
| 4 | 2.9972 | 2.5398 | 2.2733 | 2.0966 |
| 5 | 3.5589 | 2.9392 | 2.5888 | 2.3608 |

- **`g = 1`** (not shown) is the trivial rule — every skyline is allowed, growth `= h`, count `h^w` ([[castle-strip](pages/castle-strip.md)]).
- **For `g ≥ 2, h ≥ 3` every growth constant is non-metallic** — none is a metallic mean `(a + √(a²+4))/2`. For instance `(h=3, g=2)` grows at `2.40219`, the root of the irreducible quintic reversing `x⁵ − x⁴ + 4x³ − 3x² + 3x − 1` — deceptively close to silver `1 + √2 = 2.41421` but a genuinely different degree-5 algebraic number.[^6]

So minimum-tower-spacing castles are a **new two-parameter family of C-finite castle counts**, indexed by `(h, g)`, whose growth constants form an algebraic zoo passing through several wiki-tracked constants (`φ`, `ψ²`) at small parameters and running to non-metallic higher-degree numbers as `h, g` grow. The state count grows quickly (`(h=5, g=4)` needs 625 states), so the family is best explored by the transfer matrix rather than brute force.

## The `g = 2` column is the Hardin word family (a third route)

The `g = 2` sequences are **not new** — they are exactly the **Hardin word sequences** already on the wiki, now with a clean geometric meaning:[^7]

| `(h, g=2)` | first terms | Online Encyclopedia of Integer Sequences (OEIS) |
|---|---|---|
| `h = 3` | `3, 9, 22, 51, 121, 292, 704, …` | **A202882** (offset by one) |
| `h = 4` | `4, 16, 50, 144, 422, 1268, 3823, …` | **A203094** |
| `h = 5` | `5, 25, 95, 325, 1121, 3985, 14288, …` | **A203184** |

The reason is structural, not coincidental. Spacing `g = 2` forbids a **width-1 valley** — a single raised cell with lower columns on both sides — in every row. That is exactly an **isolated strict local maximum**, and the Hardin sequences count `0..(h−1)` arrays "with every nonzero element `≤` some neighbor," i.e. **no strict local maximum** ([[hardin-word-identity](pages/hardin-word-identity.md)]). So a height-`h` tower-spacing-`2` castle is a Hardin `0..(h−1)` word, cell for cell. This is a **third castle appearance** of the Hardin family: the [[hardin-word-identity](pages/hardin-word-identity.md)] reaches them as `2^{−L}` times a *signed* even-last-column tower count; the tower-spacing family reaches them as a plain *unsigned* geometric castle count — arguably the most transparent of the three. It also explains *why* Hardin's condition connects to castles at all: "no isolated peak" is "towers stand at least 2 apart."

## Open threads

- **OEIS identification of the `g ≥ 3` 2D sequences** — the `g = 2` column is the Hardin family (above), but e.g. `(h=3, g=3) = 3, 9, 22, 46, 91, 183, 383, 819, 1749, …` = **A217878** ("n-element 0..2 arrays, each element the minimum of 3 adjacent elements") — another interlink to chase across the `g ≥ 3` table. Which `(h, g)` cells are genuinely new versus reinterpretations is tracked on [[castle-sequence-catalogue](pages/castle-sequence-catalogue.md)].
- **The reachable-field question, gap-flavored:** which algebraic numbers arise as tower-spacing growth constants, as `(h, g)` range? This is the horizontal-gap analogue of the [[reachable-field-census](pages/reachable-field-census.md)] (which censused height-adjacency strips). The `h = 2` column already gives the `x^k + x − 1` and `1 − 2x + x² − x^{g+1}` families; the full 2D reachable set is open.
- **Parity projection:** the counts here are raw (no even-block clause); imposing PE 502's `(A ± P)/2` parity ([[castle-sign](pages/castle-sign.md)]) gives the honest even-block tower-spacing counts, whose growth is unchanged but whose sequences differ (cf. [[proper-castle-projection](pages/proper-castle-projection.md)]).
- **The "no-touching" / "no-adjacency" variants** from the gap-rule IDEAS item — vertical or diagonal spacing rules — are further knobs the same transfer-matrix method reaches.

## Reproduce

The column-by-column transfer matrix (`build(h, g)`) and the growth/denominator extraction are short NumPy/SymPy; the construction and its brute-force check are pinned on [[castle-snippets](pages/castle-snippets.md)].

## Appearances in Sources

- [[pe502-pell-castle-strip](pages/pe502-pell-castle-strip.md)] - the strip-tiling note this gap-rule family grew out of.

## Related Concepts

- [[castle-strip](pages/castle-strip.md)] - the transfer-matrix bridge; this page is a horizontal-gap cousin of the height-adjacency strips defined there.
- [[metallic-strip-realizability](pages/metallic-strip-realizability.md)] / [[reachable-field-census](pages/reachable-field-census.md)] - the height-adjacency rule family and its reachable growth constants; the tower-spacing family is the parallel horizontal-gap axis.
- [[plastic-number](pages/plastic-number.md)] - `ψ²` appears as the `(h=2, g=2)` growth constant (A005251 recurrence), a third castle route to the plastic-squared sequence.
- [[pell-castle-strip](pages/pell-castle-strip.md)] - the sibling strip family (a height-adjacency rule rather than a horizontal-gap rule) with silver growth.
- [[tree-castle-by-area](pages/tree-castle-by-area.md)] - the other two A005251 castle interpretations the `(h=2, g=2)` count joins.
- [[castle-classification](pages/castle-classification.md)] - the m-disparate / m-smooth (Axis 2) neighborhood this variation extends into the horizontal-gap direction.
- [[castle-sign](pages/castle-sign.md)] / [[proper-castle-projection](pages/proper-castle-projection.md)] - the even-block parity projection that turns these raw counts into proper PE 502 castle counts.

## Footnotes

[^1]: The rule, stated on the skyline: for every level `r ∈ {2, …, h}`, the indicator string `s_r = (𝟙[c_i ≥ r])_{i=1..w}`, after stripping leading and trailing zeros, contains no run of zeros shorter than `g`. Equivalently, consecutive columns that reach height `≥ r` are either adjacent-in-the-same-block or separated by `≥ g` columns below `r`. `g = 1` recovers PE 502's rule 3 as applied to towers; the base row `r = 1` is always solid and unconstrained.

[^2]: Verified by execution. The transfer matrix `M` is built over per-row state tuples for rows `2..h` (states `pre`, `fill`, `g1..g_{g−1}`; a fill from a `g_k` state with `k < g` is illegal; an empty from `fill`/`g_k` advances the gap counter, collapsing to `pre` at length `g`). Width-`w` counts `𝟙ᵀ M^w` match brute-force enumeration over all `h^w` skylines with the gap predicate for `(h,g) = (2,2), (3,2), (3,3), (4,2)` through `w = 7`: e.g. `(3,2)` gives `3, 9, 22, 51, 121, 292, 704` both ways.

[^3]: Denominators computed as `det(I − xM)` and factored in SymPy for `g = 2..7` at `h = 2`. Even `g`: `1 − 2x + x² − x^{g+1}` (a single irreducible factor for `g ≥ 4`; `g = 2` is `1 − 2x + x² − x³`). Odd `g = 2k−1`: `(x^k − x + 1)(x^k + x − 1)`, growth = dominant root of `x^k + x − 1` (`g=3` → `x²+x−1`, golden `φ = 1.61803`; `g=5` → `x³+x−1`, `1.46557`; `g=7` → `x⁴+x−1`, `1.38028`). Growth constants `1.75488, 1.61803, 1.52895, 1.46557, 1.41780, 1.38028` for `g = 2..7`, monotone decreasing toward 1.

[^4]: `1 − 2x + x² − x³` is the reverse of `x³ − x² + 2x − 1`, and `x³ − 2x² + x − 1` is the minimal polynomial of `ψ²` ([[plastic-number](pages/plastic-number.md)]); the growth `1.754878` matches `ψ² = 1.7548776662…`. The `(h=2,g=2)` sequence `2, 4, 7, 12, 21, 37, 65, 114, 200, 351` satisfies `a(n) = 2a(n−1) − a(n−2) + a(n−3)` (verified), the A005251 recurrence, with its own initial conditions.

[^5]: Growth constants are the numeric Perron roots (largest real eigenvalue) of `build(h, g)`, `h = 2..5`, `g = 2..5` (NumPy `eigvals`). `g = 1` gives the all-ones-per-column matrix, Perron root `h`. The state count is bounded by the number of legal per-row state tuples; `(h=5, g=4)` has 625 states.

[^6]: The `(h=3, g=2)` count `3, 9, 22, 51, 121, 292, 704, 1691, 4059, 9749, 23422` has minimal linear recurrence of order 5 with denominator reversing `x⁵ − x⁴ + 4x³ − 3x² + 3x − 1` (irreducible over `ℚ`), dominant root `2.402209`. `1 + √2 = 2.414214` is close but the polynomial is degree 5, not `x² − 2x − 1`, so the constant is non-metallic. Checked that no metallic mean `(a + √(a²+4))/2` matches any `(h≥3, g≥2)` growth constant to `10⁻⁵`.

[^7]: Verified against OEIS (fetched 2026-09-18): the `g=2` tower-spacing counts match the Hardin word sequences term for term — `(h=3,g=2) = 3,9,22,51,121,292,704,1691,4059` = A202882 (whose data is `1,3,9,22,51,…`, so `= A202882(w+1)`); `(h=4,g=2) = 4,16,50,144,422,1268,3823` = A203094; `(h=5,g=2) = 5,25,95,325,1121,3985,14288` = A203184. And `(h=3,g=3) = 3,9,22,46,91,183,383,819,1749` = A217878 exactly. The `g=2 ↔` Hardin identity is structural: `g=2` forbids a width-1 internal gap in each row = an isolated raised cell = a strict local maximum, and A202882/A203094/A203184 count `0..m` arrays with no nonzero strict local maximum ([[hardin-word-identity](pages/hardin-word-identity.md)]).
