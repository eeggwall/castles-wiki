---
title: Castle classification
category: Concepts
summary: A classification framework for castle sub-families. Every castle is column-convex + bottom-aligned by construction, so a "castle type" is a further restriction on the skyline `(c_1, …, c_w)`. Catalogs 42 types (7 base from the polyomino literature, 35 proposed) organized into 7 structural axes plus a transversal metallic-mean growth-constant axis, each tied to the wiki thread that already touches it and marked with count status.
tags: [concept, castle, classification, taxonomy, skyline]
sources: [castle-classification]
created: 2026-09-15
updated: 2026-09-15
---

# Castle classification

## The framing

A **castle** is a valid stacked-block configuration on a `w × h` grid ([[castle-polyomino](pages/castle-polyomino.md)]), and is determined by its **skyline** — the sequence of column heights[^1]

```
c_1, c_2, …, c_w      with 1 ≤ c_i ≤ h and max_i c_i = h.
```

Every castle is automatically **column-convex** (each column is one contiguous vertical run) and **bottom-aligned** (row 1 is a full-width block). So a "**castle type**" is a **further restriction on the skyline** — a predicate on `(c_1, …, c_w)`. PE 502's even-block parity constraint is orthogonal to typing: each type is defined without reference to parity, and the even-block projector `(A ± P)/2` ([[castle-sign](pages/castle-sign.md)]) is applied on top when needed.[^1]

## Upstream source

The type catalog is hydrated from `charlesreid1.com/wiki/Project_Euler/502/Castle_Types` (fetched 2026-09-15; wikitext cached at `raw/castle-types.wiki`). That page defines 42 types — **7 base types** drawn from the polyomino literature (column-convex, unimodal, directed, parallelogram, Ferrers, staircase, m-disparate)[^2] and **35 proposed types** aggregated from adjacent literature or newly defined (convex/row-convex, reverse Ferrers, k-modal, m-smooth, Dyck-path, Motzkin-path, palindromic, self-conjugate, rainbow, hook, crenellated, moated, twin-peak, single-summit, single-valley, and so on).[^3] The upstream page states the types as skyline predicates only; this page organizes them into structural axes, ties each type to the wiki thread that already touches it, and marks which have counts, which are candidates, and which are open.

## What "classification" gives you

Three questions attach to every type:

1. **Is it counted?** Does the wiki already have a count (exact formula, generating function, or algorithm) for the type?
2. **What is its count's shape?** Growth constant, C-finite / algebraic / transcendental character, OEIS identification if any.
3. **How does it interact with the parity clause?** Does the parity-projected version have the same shape, or is parity locked out by the type's structure?

Every open (2) is a seminar topic; every open (3) is a research thread. The classification here does not answer these questions for the 42 types — it names them and marks which ones the wiki has answered, which are candidates, and which are genuinely open.

## The base 7 types and their wiki homes

The base types are all standard polyomino / composition families. Each corresponds to an existing wiki thread:[^2]

| Type | Definition (skyline predicate) | Wiki home | Count status |
|---|---|---|---|
| **Column-convex** | (automatic for castles) | [[column-convex-polyomino](pages/column-convex-polyomino.md)] | matches all castles; `A(w,h) = h^w − (h−1)^w` |
| **Unimodal** | `c_1 ≤ … ≤ c_p ≥ … ≥ c_w` | [[convex-castle](pages/convex-castle.md)] | `C(2h+w−3, w−1)` via [[convex-castle-binomial-identity](pages/convex-castle-binomial-identity.md)] |
| **Ferrers** | `c_1 ≥ c_2 ≥ … ≥ c_w` (weakly decreasing) | [[polyominoes](pages/polyominoes.md)], [[column-convex-polygon-enumeration](pages/column-convex-polygon-enumeration.md)] | classical; by area = partition GF; q-Catalan / q-Bessel refinement |
| **Staircase** | Ferrers with all `c_i` distinct | [[polyominoes](pages/polyominoes.md)] | classical (distinct-parts partitions) |
| **Parallelogram** | anti-diagonal sections connected | [[column-convex-polygon-enumeration](pages/column-convex-polygon-enumeration.md)] | classical (Bousquet-Mélou) |
| **Directed** | every cell reachable from `(1,1)` by east/north | [[polyominoes](pages/polyominoes.md)] | classical (directed polyominoes) |
| **m-disparate** | `|c_{i+1} − c_i| ≥ m` for all `i` | **not yet on the wiki** | open |

The first 6 rows tie the castle taxonomy directly to the polyomino literature. **m-disparate** is the one base type without an existing wiki thread — a natural target for the "gap-rule variations" idea on `IDEAS.md`.

## The 35 proposed types, grouped by structural axis

The proposed types cluster into a handful of structural axes, some of which the wiki has counts for.

### Axis 1: Convexity / modality

Types 1–6 and 30–31 restrict the shape of the skyline's local extrema:

| Type | Predicate | Wiki tie |
|---|---|---|
| **Convex (row-convex)** | every row is one contiguous run | equals unimodal for castles ([[convex-castle](pages/convex-castle.md)]); front/middle/back U/R/D form on [[project-euler-502-representations](pages/project-euler-502-representations.md)] |
| **Reverse Ferrers** | `c_1 ≤ … ≤ c_w` (weakly increasing) | Ferrers's mirror; same count by symmetry |
| **Strictly unimodal** | strict rise, one peak, strict fall | strengthens unimodal; count is a sub-count of [[convex-castle](pages/convex-castle.md)] |
| **Bimodal** | exactly two local maxima | *open* — natural refinement, no wiki count yet |
| **k-modal** | at most `k` local maxima | *open* — unimodal is `k=1`; parameterized family |
| **Anti-unimodal (V-shaped)** | weakly decrease then weakly increase | the "valley" family; on [[castle-by-area](pages/castle-by-area.md)] as valley castles, area-OEIS A332578; the [[convex-castle-binomial-identity](pages/convex-castle-binomial-identity.md)] valley bijection is an open thread |
| **Convex-skyline** | `c_{i−1} − 2c_i + c_{i+1} ≥ 0` (discrete convex) | *open* — a stronger sub-family of anti-unimodal |
| **Concave-skyline** | `c_{i−1} − 2c_i + c_{i+1} ≤ 0` (discrete concave) | *open* — a stronger sub-family of unimodal |

**Where the wiki already has counts:** unimodal and (by symmetry) reverse Ferrers, via the [[convex-castle-binomial-identity](pages/convex-castle-binomial-identity.md)]; anti-unimodal (valley) by area on [[castle-by-area](pages/castle-by-area.md)]. **Where the wiki has candidate counts but not proofs:** the convex⟺valley bijection.

### Axis 2: Rate of change (Lipschitz)

Types 7, 8, 9 and the base m-disparate:

| Type | Predicate | Wiki tie |
|---|---|---|
| **Plateau-free** | `c_i ≠ c_{i+1}` for all `i` | *open* — a Lipschitz lower bound on differences |
| **m-smooth (Lipschitz)** | `|c_{i+1} − c_i| ≤ m` | matches **Motzkin-path** at `m = 1`; the tower-word framing on [[tower-word-continued-fraction](pages/tower-word-continued-fraction.md)] |
| **Zigzag** | differences alternate in sign | *open* — a strong plateau-free variant |
| **m-disparate** | `|c_{i+1} − c_i| ≥ m` | *open* — the "no small step" restriction |

**Where the wiki already has counts:** 1-smooth castles collapse to the Motzkin-path family ([[motzkin-numbers](pages/motzkin-numbers.md)], [[tower-word-continued-fraction](pages/tower-word-continued-fraction.md)]); the tower word A004149 is the 1-smooth-with-no-UD-no-DU refinement. **Open:** the full m-smooth family for `m ≥ 2`, and m-disparate for any `m`.

### Axis 3: Path-like restrictions

Types 13 and 14 identify the skyline with a classical lattice path:

| Type | Predicate | Wiki tie |
|---|---|---|
| **Dyck-path** | `c_1 = c_w = 1`, `|c_{i+1} − c_i| = 1`, all `c_i ≥ 1` | [[dyck-words](pages/dyck-words.md)]; [[catalan-numbers](pages/catalan-numbers.md)] count |
| **Motzkin-path** | `|c_{i+1} − c_i| ≤ 1` (Dyck-path with flat steps allowed) | [[motzkin-numbers](pages/motzkin-numbers.md)]; [[tower-word-continued-fraction](pages/tower-word-continued-fraction.md)] is the run-constrained sub-family |

**Where the wiki already has counts:** both, from the classical lattice-path literature. The Dyck-path castle is Catalan; the Motzkin-path castle is Motzkin (with the run constraint further reducing to A004149).

### Axis 4: Symmetry

Types 11, 12, 21 impose symmetry on the skyline:

| Type | Predicate | Wiki tie |
|---|---|---|
| **Palindromic** | `c_i = c_{w+1−i}` | *open* — a natural symmetry restriction |
| **Centrally symmetric** | `c_i + c_{w+1−i} = h + 1` (180° rotation inside bounding box) | *open* |
| **Self-conjugate** | `c_i = #{j : c_j ≥ i}` (transpose invariance) | *open* — classical partition-conjugation, would require `w = h` |

**Open across the board.** The self-conjugate type is particularly interesting because it forces `w = h` and interacts with the wiki's Fibonacci-in-prime-castle count `2^{n−1} − F_{n−1}` on [[castle-by-area](pages/castle-by-area.md)].

### Axis 5: Value / extremum constraints

Types 15, 16, 24, 26, 27, 33, 35, and a few others restrict where extremes occur:

| Type | Predicate | Wiki tie |
|---|---|---|
| **Flat-top** | `h` attained in ≥ 2 consecutive columns | *open* |
| **Single-summit** | `h` attained in exactly one column | *open* — matches strictly-unimodal at the peak |
| **Twin-peak** | `h` attained in exactly two columns | *open* |
| **Single-valley** | height 1 attained in exactly one column | *open* — dual to single-summit |
| **Rainbow** | `w = h`, heights a permutation of `{1, …, h}` | *open* — direct link to permutation-based combinatorics ([[permutation-cycle-castle-analogy](pages/permutation-cycle-castle-analogy.md)]) |
| **Boxcastle** | `c_i = h` for all `i` | trivial: count is `1` |
| **Hook** | `c_1 = h`, `c_i = 1` for `i ≥ 2` | Young-diagram hook; count is `w` (choice of tower position × 1) after symmetry |

**Rainbow castles are the natural bridge to [[permutation-cycle-castle-analogy](pages/permutation-cycle-castle-analogy.md)]:** they are, by definition, in bijection with permutations of `{1, …, h}` — so the wiki's cycle-count / Foata / streak triad ([[castles-as-upgraded-cycle-count](pages/castles-as-upgraded-cycle-count.md)]) applies to them directly, not by upgrade. Rainbow castles are the "n! degenerate case" of the castle machinery.

### Axis 6: Parity and area

Types 10, 17, 18, 32:

| Type | Predicate | Wiki tie |
|---|---|---|
| **Alternating parity** | `c_i` alternates odd/even | *open* |
| **Even-area** | `∑ c_i ≡ 0 (mod 2)` | [[castle-by-area](pages/castle-by-area.md)] parity split |
| **Even-peak** | number of local maxima is even | [[castle-sign](pages/castle-sign.md)] sibling; peak count is on [[castle-foata-transform](pages/castle-foata-transform.md)] |
| **Triangular-area** | `∑ c_i = n(n+1)/2` | *open* — a curiosity restriction |

**The even-peak type is worth flagging.** The [[castle-sign](pages/castle-sign.md)] is `(−1)^blocks`, not `(−1)^peaks`; even-peak is a different parity constraint that the wiki hasn't investigated. The [[castle-foata-transform](pages/castle-foata-transform.md)] identifies `#peaks = #records`, so even-peak is "even-records" — a permutation-statistic parity condition.

### Axis 7: Value patterns

Types 19, 20, 22, 23, 25, 28, 29, 34:

| Type | Predicate | Wiki tie |
|---|---|---|
| **Equal-block** | all maximal horizontal blocks have the same length | *open* — heavy structure |
| **Two-level** | exactly two distinct height values | contains [[pell-castle-strip](pages/pell-castle-strip.md)] with `h = 2` |
| **Crenellated** | heights alternate `{a, h}` (battlements) | *open* — very restricted two-level |
| **Moated** | `c_1 = c_w = 1`, all interior `≥ 2` | *open* |
| **Fence-post** | `c_i = 1` for all even `i` | *open* |
| **Linear** | `c_i = a + (i−1)d` (arithmetic progression) | *open* — count is `O(h)` or `O(wh)` depending on parameters |
| **Prime-top** | `h` is prime | trivial family: all castles with prime `h` |
| **Integer-mean** | `w | ∑ c_i` | *open* |

### Growth-constant classification: silver, bronze, and beyond

The **[[metallic-means](pages/metallic-means.md)]** framework offers a **transversal classification axis** — one that groups castle sub-families not by skyline predicate but by the **growth constant of their count sequence**. From the [[pell-castle-strip](pages/pell-castle-strip.md)] mnemonic, a castle-strip family with denominator `1 − w_1·x − w_2·x²` grows at

```
δ = (w_1 + √(w_1² + 4·w_2)) / 2,
```

which is the metallic mean `δ_{w_1}` exactly when `w_2 = 1`. So each metallic mean `δ_a` (for `a = 1, 2, 3, …` = golden, silver, bronze, copper, …) is a **candidate growth constant** for castle sub-families with "how many states per column" = `a` and a fixed mandatory-gap rule.

- **`δ_1` = golden castle candidates** — families whose count grows like Fibonacci. Height-1 castles are trivially `F_{w+something}`, and the prime-castle count `2^{n−1} − F_{n−1}` on [[castle-by-area](pages/castle-by-area.md)] is a direct hit.
- **`δ_2` = silver castle candidates** — the [[pell-castle-strip](pages/pell-castle-strip.md)] is one instance; the tower-word growth ([[tower-word-continued-fraction](pages/tower-word-continued-fraction.md)]) is another.
- **`δ_3` = bronze castle candidates** — a natural target family would have "3 states per column, mandatory-gap rule fixed." The height-3 tower with a specific same-row-adjacency rule is a candidate; the growth would be `(3+√13)/2`.
- **Higher `δ_a`** — copper, nickel, and beyond, mapping to "state-count 4, 5, …" — genuinely open.

**Naming convention.** A castle sub-family whose count sequence grows at rate `δ_a` is a **"δ_a-castle"** or, informally, a **"silver / bronze / copper / … castle."** The names are shorthand; the substantive fact is the growth-constant identification. This is the classification axis the "Metallic-ratio ladder" thread on `IDEAS.md` tracks.

## Open threads this classification opens

The taxonomy makes explicit which sub-families the wiki has, which are candidates, and which are open. The largest open groupings, in rough order of tractability:

1. **k-modal** for `k ≥ 2` — a parametric family whose `k = 1` case is [[convex-castle](pages/convex-castle.md)] (binomial); `k = 2, 3, …` are genuinely open with no candidate closed form.
2. **m-smooth / m-disparate** for `m ≥ 2` — a paired family; `m = 1` collapses to Motzkin-path.
3. **Symmetry types** (palindromic, centrally symmetric, self-conjugate) — untouched.
4. **Rainbow** — direct permutation-classification tie, immediate seminar target for the [[castles-as-upgraded-cycle-count](pages/castles-as-upgraded-cycle-count.md)] triad.
5. **δ_a-castle identification** for `a ≥ 3` — the metallic-mean ladder growth constants realized in castle rule modifications; tied to [[metallic-means](pages/metallic-means.md)].
6. **Even-peak** — parity via peak count rather than block count; genuinely different from [[castle-sign](pages/castle-sign.md)]'s `(−1)^blocks`.

## Related Concepts

- [[castle-polyomino](pages/castle-polyomino.md)] — the base object.
- [[castle-representations](pages/castle-representations.md)] — the skyline `(c_1, …, c_w)` is the integer-tuple encoding this classification predicates on.
- [[convex-castle](pages/convex-castle.md)] / [[convex-castle-binomial-identity](pages/convex-castle-binomial-identity.md)] — the unimodal (row-convex) type.
- [[polyominoes](pages/polyominoes.md)] / [[column-convex-polyomino](pages/column-convex-polyomino.md)] / [[column-convex-polygon-enumeration](pages/column-convex-polygon-enumeration.md)] — the base-type home literature.
- [[stack-polyomino-gf](pages/stack-polyomino-gf.md)] — the unimodal-skyline (single-peak) family from AC Ex. I.8.
- [[dyck-words](pages/dyck-words.md)] / [[tower-word-continued-fraction](pages/tower-word-continued-fraction.md)] — the Dyck-path / Motzkin-path types.
- [[metallic-means](pages/metallic-means.md)] / [[pell-castle-strip](pages/pell-castle-strip.md)] — the growth-constant classification axis.
- [[castle-by-area](pages/castle-by-area.md)] — where several types (even-area, valley) are counted.
- [[castle-sign](pages/castle-sign.md)] / [[castle-foata-transform](pages/castle-foata-transform.md)] — the parity / peak-count / record statistics several types predicate on.
- [[castles-as-upgraded-cycle-count](pages/castles-as-upgraded-cycle-count.md)] — the framework the rainbow type maps onto directly.

## Footnotes

[^1]: raw/castle-types.wiki L1-L9 — "A castle on a w × h grid is determined by its skyline, the sequence of column heights c_1, c_2, …, c_w with 1 ≤ c_i ≤ h and max_i c_i = h. (Problem 502 also requires an even number of blocks; the types below mostly ignore, or independently re-impose, that parity rule.) Every castle is automatically column-convex and bottom-aligned, so each type is a further restriction on the skyline." (Source: https://charlesreid1.com/wiki/Project_Euler/502/Castle_Types, fetched 2026-09-15.)
[^2]: raw/castle-types.wiki §"Base types" L11-L19 — the 7 base types: column-convex, unimodal (`c_1 ≤ … ≤ c_p ≥ … ≥ c_w`), directed (every cell reachable from bottom-left by east/north path), parallelogram (perpendicular-to-main-diagonal sections are connected), Ferrers (`c_1 ≥ … ≥ c_w`), staircase (Ferrers with strict inequality — all distinct heights), m-disparate (`|c_{i+1} − c_i| ≥ m`).
[^3]: raw/castle-types.wiki §"Proposed additional types" L21-L57 — the 35 proposed types, numbered 1-35: convex/row-convex, reverse Ferrers, strictly unimodal, bimodal, k-modal, anti-unimodal (V-shaped), plateau-free, m-smooth (Lipschitz), zigzag, alternating parity, palindromic, centrally symmetric, Dyck-path, Motzkin-path, flat-top, single-summit, even-area, even-peak, equal-block, two-level, self-conjugate, crenellated, moated, rainbow, hook, twin-peak, single-valley, fence-post, linear, convex-skyline (second differences ≥ 0), concave-skyline (≤ 0), triangular-area, prime-top, integer-mean, boxcastle.
