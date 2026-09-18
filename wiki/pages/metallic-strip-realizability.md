---
title: Which metallic means are castle-strip growth constants
category: Analyses
summary: The Axis-8 "which metallic ratios does a castle rule produce" question, solved. A castle-strip growth constant is the Perron root of a 0/1 transfer matrix over h height-states, and metallicity of δ_a demands the strip denominator 1 − p₁x − p₂x² have p₂ = 1, which the naive "h states per column" coupling breaks. The resolution: ONE named predicate — "plateau-free except at the ceiling" (adjacent columns differ in height unless both equal the max h) — has transfer matrix M = J − D with char poly (x+1)^{h−2}(x² − (h−1)x − 1), so it realizes the WHOLE metallic ladder, metal a = h−1: golden (h=2), silver (h=3), bronze (h=4), copper (h=5), nickel (h=6), …. Bronze is thus a real named-predicate castle (also provably unreachable on ≤ 3 states, needing 4). Copper (h=5) = δ₄ = φ³, so its count is a Fibonacci trisection F_{3n+5} — the decimation made concrete. Silver also has a second realization (the 1-smooth height-3 strip, (x−1)(x²+2x−1)).
tags: [analysis, castle, metallic-mean, growth-constant, transfer-matrix, perron-root, bronze, copper, silver, fibonacci-decimation, axis-8, realizability, sympy, verification]
sources: [pe502-pell-castle-strip]
created: 2026-09-18
updated: 2026-09-18
---

# Which metallic means are castle-strip growth constants

## The question

[[castle-classification](pages/castle-classification.md)] Axis 8 names a class a **"`<metal>` width growth castle"** when its width-graded count grows at the metallic mean `δ_a = (a + √(a² + 4))/2` ([[metallic-means](pages/metallic-means.md)]). Golden (`a = 1`) and silver (`a = 2`) have known members ([[pell-castle-strip](pages/pell-castle-strip.md)] and the `{0,1}`-strip); bronze and above were marked "open." The open question, precisely stated: **which metallic means arise as growth constants of an actual castle-strip rule, and how?**

A **castle-strip rule** is a nearest-neighbor restriction on a row of columns with heights in `{1, …, h}`: an allowed-adjacency predicate `A(a, b)` on consecutive column heights. Its count-by-width sequence has growth constant equal to the **Perron root** (dominant eigenvalue) of the `h × h` 0/1 **transfer matrix** `M[a][b] = [A(a, b)]`, and its width generating function is `1 / det(I − xM)` up to the boundary term. So the question becomes: **which `δ_a` are Perron roots of 0/1 transfer matrices, and via which rules?**[^1]

## The two-knob parameterization and its trap

The [[pell-castle-strip](pages/pell-castle-strip.md)] mnemonic writes a two-state strip denominator as `1 − p₁·x − p₂·x²`, giving growth `(p₁ + √(p₁² + 4p₂))/2`. Here `p₁` and `p₂` are the **denominator's polynomial coefficients** — `p₁` is the coefficient on `x¹` and `p₂` the coefficient on `x²`; they are *not* widths (the strip has a single width, graded by the GF variable `x`). Read combinatorially, `p_k` is the weight (number of choices) of a tiling atom spanning `k` columns. This is a metallic mean **iff `p₂ = 1`**: only then does `p₁² + 4p₂ = p₁² + 4` match the metallic discriminant `a² + 4` with `a = p₁`. The Pell strip is `p₁ = 2, p₂ = 1` (silver); the `{0,1}`-strip is `p₁ = 1, p₂ = 1` (golden).

The **trap** is to read `p₁` as "number of per-column states" and expect `p₁ = 3` (height-3 columns) to give bronze. It does not, because **`p₁` and `p₂` are coupled in natural height-`h` rules**: widening the height alphabet also widens the gap/return structure, pushing `p₂` off `1`. Measured on concrete height-3 rules (each a 3×3 transfer matrix, denominator `det(I − xM)`):[^2]

| height-3 rule | `A(a, b)` | denominator `det(I − xM)` | growth | metallic? |
|---|---|---|---|---|
| all pairs | always | `1 − 3x` | `3` | no (integer) |
| plateau-free | `a ≠ b` | `1 − 3x² − 2x³` | `2` | no (integer) |
| no adjacent ceiling | not `a = b = 3` | `1 − 2x − 2x²` | `(1+√3)` ≈ `2.732` | no (`p₂ = 2`) |
| **1-smooth** | `|a − b| ≤ 1` | `1 − 3x + x² + x³ = (1−x)(1 − 2x − x²)` | **`1 + √2`** ≈ `2.414` | **yes — silver!** |
| decreasing-forbidden | `a ≤ b` | `(1 − x)³` | `1` | no |

Two things fall out immediately.

## Finding 1: silver has a second, independent castle realization

The **1-smooth height-3 strip** (`|c_{i+1} − c_i| ≤ 1`, a Motzkin-flavored rule) has denominator that factors as `(1 − x)(1 − 2x − x²)` - the silver factor `1 − 2x − x²` exactly, times a spurious `(1 − x)`.[^3] So its growth constant is `1 + √2`: it is a **silver width growth castle**, structurally distinct from both prior silver members.

This is a genuine new member of the silver class - a *third* independent realization alongside the [[pell-castle-strip](pages/pell-castle-strip.md)] (rational, Pell numbers) and the tower word ([[tower-word-continued-fraction](pages/tower-word-continued-fraction.md)], algebraic, A004149). Notably it lives at **height 3**, not height 2, and reaches silver by a rate-of-change rule (Axis 2, [[castle-classification](pages/castle-classification.md)]) rather than a per-column-state count - the meta-classification uniting differently-shaped families exactly as intended. The 1-smooth family is the Motzkin-path connection ([[motzkin-numbers](pages/motzkin-numbers.md)], [[tower-word-continued-fraction](pages/tower-word-continued-fraction.md)]); this locates its growth constant precisely on the metallic ladder.

## Finding 2: bronze needs four states, not three

None of the five natural height-3 rules produces bronze `(3 + √13)/2 ≈ 3.303`. This is not an accident of the sample - it is a **state-count obstruction**:

> **No 0/1 transfer matrix on `≤ 3` states has `(3 + √13)/2` as a Perron root.** Exhaustive search over all `2^9 = 512` binary `3×3` matrices finds zero whose spectrum contains the bronze value; over all `2^{16} = 65536` binary `4×4` matrices, **192** do.[^4]

So bronze is **reachable, but only with at least four height-states**. And there is a **named, natural rule** that realizes it — better still, one rule realizes the *entire* ladder (Finding 3 below). The bronze instance is:

```
"plateau-free except at the ceiling", h = 4:
adjacent columns must differ in height, UNLESS both are at the maximum height h.

transfer matrix M = J − D                allowed height-adjacency rule (heights 1..4)
[0 1 1 1]                                1↛1, 2↛2, 3↛3  (no equal-height neighbors below the top)
[1 0 1 1]                                4→4 allowed     (two ceiling columns may abut)
[1 1 0 1]
[1 1 1 1]
```

Its characteristic polynomial is `(x + 1)²(x² − 3x − 1)`, so the Perron root is bronze `(3 + √13)/2` exactly; the width count is `4, 13, 43, 142, 469, 1549, …` (growth ratio `→ 3.30278`).[^5] This is a real **bronze width growth castle** from a recognizable predicate — a **plateau-free variant** (Axis 2 of [[castle-classification](pages/castle-classification.md)]) with a single ceiling exception — not a synthetic matrix.

## Finding 3: one named rule realizes the whole metallic ladder

The plateau-free-except-ceiling rule is not a bronze one-off. At height `h` its transfer matrix is `M_h = J − D`, where `J` is the `h × h` all-ones matrix and `D = diag(1, …, 1, 0)` (identity with the last diagonal entry zeroed — the single ceiling exception). Its characteristic polynomial is, for every `h ≥ 2`,[^7]

```
char(M_h)  =  (x + 1)^{h−2} · (x² − (h−1)x − 1),
```

verified symbolically for `h = 2, …, 6`. The `(x + 1)^{h−2}` factor is spurious (eigenvalue `−1`, subdominant); the dominant root is the metallic mean

```
δ_{h−1}  =  ((h−1) + √((h−1)² + 4)) / 2.
```

So **one rule sweeps the entire ladder, metal `a = h − 1`**:

| `h` | growth (Perron root) | metal | `x² − (h−1)x − 1` |
|---|---|---|---|
| 2 | `φ ≈ 1.6180` | golden (`a = 1`) | `x² − x − 1` |
| 3 | `1 + √2 ≈ 2.4142` | silver (`a = 2`) | `x² − 2x − 1` |
| **4** | `(3+√13)/2 ≈ 3.3028` | **bronze** (`a = 3`) | `x² − 3x − 1` |
| **5** | `2 + √5 ≈ 4.2361` | **copper** (`a = 4`) | `x² − 4x − 1` |
| 6 | `(5+√29)/2 ≈ 5.1926` | nickel (`a = 5`) | `x² − 5x − 1` |
| `h` | `δ_{h−1}` | `(h−1)`-th metal | `x² − (h−1)x − 1` |

**Why this rule decouples `p₁` and `p₂`.** The `M = J − D` structure is exactly the decoupling Finding 2's obstruction demanded: `J` supplies all `h` forward states (a large `p₁`) while the ceiling exception `−D` removes all but *one* length-2 return loop (pinning `p₂ = 1`). The metallic discriminant `(h−1)² + 4` is the fingerprint. This is the general mechanism behind all three prior special cases — the `{0,1}`-strip (golden), the Pell strip (silver), and the 1-smooth strip (silver again) — reorganized under one predicate.

### Copper and the Fibonacci decimation (`δ₄ = φ³`)

The copper rung (`h = 5`) is special because `δ₄ = 2 + √5 = φ³` (since `φ² = φ + 1 ⟹ φ³ = 2φ + 1 = 2 + √5`; verified exactly).[^8] So copper lives in `Q(√5)`, and the copper strip's count is a **decimated Fibonacci** — literally every third Fibonacci number:

```
copper (h = 5) width count:  5, 21, 89, 377, 1597, 6765, 28657, 121393, 514229, …
                          =  F_5, F_8, F_11, F_14, …  =  F_{3n+5}.
```

That is the **Fibonacci decimation** in the most concrete possible form: because the growth constant is `φ³`, walking one column of the copper strip advances Fibonacci by three indices, so the count *is* the trisection of the Fibonacci sequence. The companion metallic integer sequence for `a = 4` is `A001076 = F_{3n}/2` ([[metallic-means](pages/metallic-means.md)] copper row); the strip realizes the un-halved trisection directly. Bronze (`h = 4`), by contrast, sits in `Q(√13)` — no such decimation, because only `a = 4` has the `φ³` coincidence ([[metallic-means](pages/metallic-means.md)]).

## Why the coupling happens, and what it means for the ladder

The structural reason `p₂` drifts from `1`: in a nearest-neighbor strip, `p₂` counts **length-2 return loops** in the transfer graph (paths `a → b → a` weighted into the `x²` coefficient of `det(I − xM)`), and widening the height alphabet multiplies the available return loops. Pinning `p₂ = 1` requires a rule with **exactly one** such return structure while still admitting `p₁` forward states - a decoupling that the symmetric "count the columns" rules do not provide, but that the ceiling-exception rule `M = J − D` provides at every height (Finding 3). The metallic discriminant `a² + 4` is the fingerprint of "one return loop"; anything richer lands in a different quadratic field.

Consequently the **off-ladder surds are the generic case** for rules that are *not* this one. Other natural rules produce, among others:

- `(1 + √3)` (`Q(√3)`) - the no-adjacent-ceiling height-3 rule (`p₂ = 2`);
- integers `h − 1` - the plateau-free height-`h` rule (real but not surd);
- and at height `h` with a gap tax scaling as `h − 1`, growth `(h + √(h² + 4(h−1)))/2`, which is `(3 + √17)/2 ∈ Q(√17)` at `h = 3` and `(4 + √28)/2 = 2 + √7 ∈ Q(√7)` at `h = 4` - neither metallic.[^6]

So the metallic ladder is **realizable but not naturally parameterized by the number of states per column**: `δ_a` is not "the `a`-states-per-column strip." The correct parameterization is the ceiling-exception rule `M_h = J − D` at height `h = a + 1` (Finding 3). Golden and silver additionally appear at small heights by *other* rules (the `{0,1}`-strip, Pell strip, 1-smooth strip); bronze and beyond appear only through the ceiling-exception rule (or another `p₂ = 1` decoupling). The clean "how many states per column" story of the Pell strip is a **low-rung coincidence**, not the general mechanism — the general mechanism is `J − D`.

## Open, sharpened

Bronze and copper are now **realized** (Finding 3) — one named predicate covers the whole ladder. What remains:

- **Uniqueness / other natural rules per rung.** Is `M_h = J − D` the *only* natural predicate hitting `δ_{h−1}`, or (as with silver's three realizations) are there others? A census of named Axis-1–7 predicates by their Perron root would answer this.
- **The proper-castle count, not just the strip.** The ceiling-exception counts above are *free-height strip* counts (`𝟙ᵀM^L𝟙`); the honest castle count imposes `max_i c_i = h` and the even-block parity clause. Does the metallic growth survive the `max = h` and `(A ± P)/2` projections, or only the leading asymptotics? (Growth constants are unchanged by these lower-order corrections, but the exact sequences and OEIS identities differ.)
- **The reachable-surd landscape.** Which real quadratic fields `Q(√d)` are hit by castle-strip Perron roots at all? Data so far: the metallic fields `Q(√(a²+4))` are *all* reached (via `J − D`); the non-metallic `Q(√3)`, `Q(√7)`, `Q(√17)` also appear. A full census by state count is the systematic version of this page.
- **The reachable-surd landscape.** Which real quadratic fields `Q(√d)` are hit by castle-strip Perron roots at all? The data so far: `Q(√5)` (golden), `Q(√2)` (silver), `Q(√3)`, `Q(√17)`, `Q(√7)` appear; `Q(√13)` (bronze) needs four states. A full census by state count is the systematic version of this page.

## Appearances in Sources

- [[pe502-pell-castle-strip](pages/pe502-pell-castle-strip.md)] - the `1 − p₁x − p₂x²` two-knob parameterization this page stress-tests.

## Related Concepts

- [[metallic-means](pages/metallic-means.md)] - the ladder whose realizability this page settles; the `p₂ = 1` metallicity criterion.
- [[pell-castle-strip](pages/pell-castle-strip.md)] - the silver `p₁ = 2, p₂ = 1` strip; the canonical low-rung case where the naive "states per column" reading works.
- [[castle-classification](pages/castle-classification.md)] - Axis 8 (the growth-type meta-classification these are members of) and Axes 1-7 (the rules tested here: 1-smooth is Axis 2, plateau-free is Axis 2).
- [[tower-word-continued-fraction](pages/tower-word-continued-fraction.md)] / [[motzkin-numbers](pages/motzkin-numbers.md)] - the 1-smooth / Motzkin family whose growth constant this page pins to silver.
- [[eigenvalue-continued-fractions](pages/eigenvalue-continued-fractions.md)] - why metallic means have periodic continued fractions and sit in the specific fields `Q(√(a²+4))`.
- [[castle-graph-spectral-radius](pages/castle-graph-spectral-radius.md)] - the sibling census on the *adjacency* spectra of individual castle graphs (where metallic means also appear, and copper+ are impossible for a different reason: max degree 4).

## Footnotes

[^1]: The width generating function of a nearest-neighbor strip with transfer matrix `M` and all-ones start/end vectors is `𝟙ᵀ(I − xM)⁻¹𝟙`, whose denominator is `det(I − xM)`; the growth constant is `1/ρ` where `ρ` is the smallest-modulus root of `det(I − xM)`, equivalently the Perron (dominant) eigenvalue of `M`. Standard transfer-matrix / analytic-combinatorics fact ([[symbolic-method](pages/symbolic-method.md)], rational SEQ case).

[^2]: Verified by execution (SymPy): for each rule, `M[i][j] = [A(i+1, j+1)]` over heights `{1,2,3}`, `denom = expand(det(eye(3) − x·M))`, dominant growth `= max |1/root|`. Denominators as tabulated; `no adjacent ceiling` gives `1 − 2x − 2x²` (growth `(2 + √12)/2 = 1 + √3 ≈ 2.732`), `1-smooth` gives `1 − 3x + x² + x³`.

[^3]: `factor(x³ + x² − 3x + 1) = (x − 1)(x² + 2x − 1)` (SymPy); the reversal of `x² + 2x − 1` is `1 − 2x − x²`, the silver denominator, so `det(I − xM) = (1 − x)(1 − 2x − x²)` and the dominant root is the silver ratio `1 + √2`. The `(1 − x)` factor contributes the subdominant eigenvalue `1` and does not affect growth.

[^4]: Exhaustive search (NumPy `eigvals`): over all `512` binary `3×3` matrices, none has an eigenvalue within `10⁻⁹` of `(3 + √13)/2 = 3.302775…`; over all `65536` binary `4×4` matrices, `192` do. So `3` states are provably insufficient and `4` suffice.

[^5]: The bronze rule at `h = 4` is `A(a, b) = [a ≠ b or a = b = 4]`, transfer matrix `M = [[0,1,1,1],[1,0,1,1],[1,1,0,1],[1,1,1,1]]`; SymPy `factor(M.charpoly()) = (x + 1)²(x² − 3x − 1)`, so `x² − 3x − 1` divides it exactly and the Perron root is `(3 + √13)/2`. Width counts `𝟙ᵀM^L𝟙 = 4, 13, 43, 142, 469, 1549, 5116, …` with ratio `→ 3.30278`. (A separate exhaustive scan confirms the *minimum-density* bronze matrix has 13 ones, e.g. `[[0,0,0,1],[1,1,1,1],[1,1,1,1],[1,1,1,1]]` with `charpoly = x²(x² − 3x − 1)`; the named `J − D` rule above uses 13 ones too and is the interpretable one.)

[^6]: The `p₂ = h − 1` gap-scaling model gives denominator `1 − h·x − (h−1)x²`, growth `(h + √(h² + 4(h−1)))/2`: at `h = 3`, `(3 + √17)/2 ≈ 3.5616 ∈ Q(√17)`; at `h = 4`, `(4 + √28)/2 = 2 + √7 ≈ 4.6458 ∈ Q(√7)`. Neither discriminant (`17`, `28`) has the metallic form `a² + 4`, so neither is a metallic mean. Verified numerically (SymPy).

[^7]: The ceiling-exception rule at height `h` has transfer matrix `M_h = J − D` where `J` is the `h × h` all-ones matrix and `D = diag(1, …, 1, 0)`. SymPy `factor(M_h.charpoly(x))` returns `(x + 1)^{h−2}·(x² − (h−1)x − 1)` for `h = 2, 3, 4, 5, 6` (exact symbolic match against the closed form; the `expand(...) == 0` difference check passes each time). The dominant root of `x² − (h−1)x − 1` is `δ_{h−1} = ((h−1) + √((h−1)²+4))/2`, the `(h−1)`-th metallic mean. Growth ratios `1.6180, 2.4142, 3.3028, 4.2361, 5.1926` for `h = 2..6` confirmed against the metallic values.

[^8]: `φ³ = 2 + √5` exactly: `φ² = φ + 1 ⟹ φ³ = φ² + φ = 2φ + 1 = 2 + √5` (SymPy `simplify(φ³ − (2+√5)) = 0`). So `δ₄ = 2 + √5 = φ³ ∈ Q(√5)`. The `h = 5` ceiling-exception strip width counts are `5, 21, 89, 377, 1597, 6765, 28657, 121393, 514229` = `F_{3n+5}` (verified index-exact against the Fibonacci sequence `F_5 = 5, F_8 = 21, F_11 = 89, …`), the trisection of Fibonacci — the concrete Fibonacci decimation forced by growth `= φ³`. The metallic companion `A001076 = 0, 1, 4, 17, 72, … = F_{3n}/2` is the halved trisection ([[metallic-means](pages/metallic-means.md)]).
