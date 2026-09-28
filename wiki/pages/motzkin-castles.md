---
title: Motzkin castles - where the Motzkin numbers meet the castle
category: Analyses
summary: Hub for the exact appearances of the Motzkin family in castles. Every castle is a cornerless Motzkin path (Deutsch-Elizalde's bargraph bijection, read on the tower word). The Motzkin-path castles (1-smooth, end columns at height 1) number M_{w-1}, and PE 502's even-block clause splits them into odd/even Motzkin paths (A343386 / A107587), signed excess A343773. The sign sets the up-step weight to -1, moving the growth constant from 3 to the Gaussian integers 1 ± 2i and the bounded-height spectrum from 1 + 2cos to 1 + 2i·cos. Bounded height gives the ladder 2, 1+√2, φ², 1+√3, … → 3 (A171842 at h ≤ 3). Motzkin prefixes (A005773), semi-perimeter relatives (A082582, A023431, A004148), and a bijection from castles that never drop by more than one to valleyless Motzkin meanders (Prodinger's not-in-OEIS sequence 1, 2, 5, 12, 29, 71, …).
tags: [analysis, castle, motzkin, lattice-paths, cornerless, bargraph, parity, sign, gaussian-integers, transfer-matrix, chebyshev, metallic, semi-perimeter, oeis, hub]
sources: [motzkin-numbers, project-euler-502-representations, project-euler-502-brute-force, deutsch-elizalde-2016-bargraphs-cornerless-motzkin, prodinger-2025-cornerless-motzkin-bargraphs]
created: 2026-09-26
updated: 2026-09-28
---

# Motzkin castles - where the Motzkin numbers meet the castle

## Scope

The Motzkin numbers `M_n = 1, 1, 2, 4, 9, 21, 51, 127, 323, 835, …` (OEIS A001006) count lattice paths from `(0,0)` to `(n,0)` with up, flat, and down steps that never go below the axis.[^1] They turn up all over the wiki: the tower word is a Motzkin path with a run constraint ([[tower-word-language](pages/tower-word-language.md)], [[tower-word-continued-fraction](pages/tower-word-continued-fraction.md)]), steep Dyck words are counted by `M_{n-1}` ([[dyck-words](pages/dyck-words.md)]), the 1-smooth strip is called the "Motzkin strip" ([[castle-strip](pages/castle-strip.md)]), and q-Motzkin numbers appear in the area thread ([[steep-polyominoes-q-motzkin-bessel](pages/steep-polyominoes-q-motzkin-bessel.md)]). This page collects the places where the Motzkin family appears **exactly** in castle counts and follows each one to its OEIS entry.

Throughout, a castle is a skyline `c_1, …, c_w` with every `c_i ≥ 1`, and its block count is the total rise from the base,[^2]

```
#blocks = c_1 + Σ_{i≥2} max(0, c_i - c_{i-1}).
```

Every such skyline is a castle (a bargraph, [[castle-polyomino](pages/castle-polyomino.md)]), and its semi-perimeter is `s = w + #blocks` ([[castle-perimeter](pages/castle-perimeter.md)]). All counts below were checked by a skyline transfer-matrix DP (widths to 16, semi-perimeters to 22) and aligned against the OEIS data on 2026-09-26; offsets are stated explicitly.

## 1. Every castle is a cornerless Motzkin path

Lower every column by one. What is left is the tower above the full-width bottom block, and its skyline read left to right is the **tower word** over `{U, R, D}`: exactly `w` `R`s, never below the base, returning to it, with no `UD` and no `DU`.[^3] With `U = +1`, `R = 0`, `D = -1` this is a Motzkin path with no peak (`UD`) and no valley (`DU`), called a **cornerless** Motzkin path. The map is a bijection between castles and nonempty cornerless Motzkin paths, and it carries the castle statistics as

```
width  w       = number of flat steps R
blocks b       = 1 + number of up steps U
semi-perimeter = #R + #U + 1
path length    = w + 2(b - 1)
```

(checked by enumerating both sides for all paths of length `≤ 10`).

This is the bijection `Δ` of Deutsch and Elizalde ([[deutsch-elizalde-2016-bargraphs-cornerless-motzkin](pages/deutsch-elizalde-2016-bargraphs-cornerless-motzkin.md)]). Their `Δ` adds an up step at the front and a down step at the back of a cornerless path and reads the result as a bargraph, so it is the inverse of lowering every column, and it sends paths with `#U + #H = n − 1` to bargraphs of semiperimeter `n`.[^4] Their first-return decomposition, `HA | UA′D | UA′DHA` with `A′` nonempty, gives `M = (1 + y(M − 1))(1 + xM)`. That is the wiki's tower grammar `E_k → ε | R·E_k | U V D (ε | R·E_k)` without the height bound, so the wiki's tower recursion is their decomposition at bounded height. With `x` marking width and `y` marking blocks, the castle GF is the quadratic `xB² − (1 − x − y − xy)B + xy = 0`, and the PE 502 sign is `y → −y`.[^4] Prodinger ([[prodinger-2025-cornerless-motzkin-bargraphs](pages/prodinger-2025-cornerless-motzkin-bargraphs.md)]) continues the line with the kernel method, counting `UD` and `DU` occurrences and extending to skew Motzkin paths and to prefixes.[^5] In castle terms `UD` is a zero-width block and `DU` is two touching blocks, the two things the tower word forbids, so his corner weights relax the castle rules: both at 0 is the castle, both at 1 is an arbitrary Motzkin path.

The bijection relates two gradings on the wiki. Counted by **path length**, cornerless Motzkin paths are A004149 ([[tower-word-continued-fraction](pages/tower-word-continued-fraction.md)]). Counted by **`#R + #U`**, which is semi-perimeter, they are the bargraphs A082582 ([[castle-perimeter](pages/castle-perimeter.md)]). The two sequences come from one set of paths with two different step weights (`D` costs `z` in the first grading and nothing in the second). A082582 also records that it counts **skew Motzkin paths** of length `n` (steps `U`, `D`, `F` and an anti-down step `A = (-1, 1)`, with down and anti-down steps not overlapping).[^6] So castles by semi-perimeter are equinumerous with skew Motzkin paths (skew paths of length `n`, castles of semi-perimeter `n + 1`), and Prodinger's §3 gives the skew GF refined by peaks and valleys.[^14] A castle-to-skew-path bijection is open.

## 2. The Motzkin-path castle and the parity split

Add the **1-smooth** rule `|c_{i+1} - c_i| ≤ 1` and pin both end columns to height 1. Then the skyline minus one is a Motzkin path of length `w - 1`, so these castles number `M_{w-1}` (A001006, offset `w - 1`). This type is already on [[castle-classification-shape](pages/castle-classification-shape.md)] (Axis 3), with the fixed-height refinement A097862.

**The PE 502 parity clause splits `M_{w-1}`.** On a Motzkin-path castle every rise is a single up step, so `#blocks = 1 + #U`. Even-block castles, the parity PE 502 keeps, are therefore the **odd** Motzkin paths (an odd number of up steps), and odd-block castles are the **even** Motzkin paths:

| width `w` | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| all, `M_{w-1}` | 1 | 1 | 2 | 4 | 9 | 21 | 51 | 127 | 323 | 835 | 2188 | 5798 |
| even-block (PE 502 parity) | 0 | 0 | 1 | 3 | 6 | 10 | 20 | 56 | 168 | 456 | 1137 | 2827 |
| odd-block | 1 | 1 | 1 | 1 | 3 | 11 | 31 | 71 | 155 | 379 | 1051 | 2971 |
| `Σ (-1)^blocks` | -1 | -1 | 0 | 2 | 3 | -1 | -11 | -15 | 13 | 77 | 86 | -144 |

The even-block row is **A343386**(`w - 1`), "Number of odd Motzkin n-paths, i.e., Motzkin n-paths with an odd number of up steps"; the odd-block row is **A107587**(`w - 1`); and the signed row is **−A343773**(`w - 1`), where A343773 is the "Excess of the number of even Motzkin n-paths (A107587) over the odd ones (A343386)" (all three matched over 16 terms).[^7] A343773 equals `(-1)^n A007440(n+1)`, the reversion of the Fibonacci generating function, so the signed Motzkin castle count is, up to sign, a series reversion of Fibonacci.[^7] None of the three entries has the castle reading.

## 3. The sign puts `i` into the up-step weight

Mark length by `x` and up steps by `t`. The first-return decomposition gives the Motzkin equation with a weight,

```
m = 1 + x·m + t·x²·m²,     discriminant (1 - x)² - 4t·x² = (1 - (1 + 2√t)x)·(1 - (1 - 2√t)x).
```

At `t = 1` the dominant singularity is `x = 1/3`, the Motzkin growth constant `3`. The castle sign is `t = -1` (each up step is one block), so `√t = i` and the discriminant becomes `1 - 2x + 5x² = (1 - (1+2i)x)(1 - (1-2i)x)`. The signed Motzkin castle count is governed by the **Gaussian integers `1 ± 2i`**: it oscillates with modulus growth `|1 + 2i| = √5 ≈ 2.236` against the unsigned `3` (own derivation; the coefficients of `m(x, -1)` reproduce A343773, and `|a_n|^{1/n}` over `n = 350..400` is consistent with `√5` after the `n^{-3/2}` correction).

The same substitution works at bounded height. The Motzkin strip of height `h` has the `h × h` transfer matrix with `1` on the diagonal and on both off-diagonals. Weighting the up-diagonal by `t` gives eigenvalues `1 + 2√t·cos(πj/(h+1))`, `j = 1..h`, because the matrix is similar to a scaled path-graph adjacency matrix. So

```
unsigned (t = 1):   1 + 2cos(πj/(h+1))       real, Perron root → 3
signed  (t = -1):   1 + 2i·cos(πj/(h+1))     all on the line Re = 1
```

(checked numerically for `h = 2..6`). At `h = 2` the signed eigenvalues are `1 ± i`. Every castle of height `≤ 2` is automatically 1-smooth, so this is the signed height-2 count, and it matches the `1 ± i` of the signed tower count `P(1, L) = Re((1+i)^{L+1})` on [[signed-tower-count](pages/signed-tower-count.md)] (castle sign = `-`(tower sign), because the base block adds one). So the `1 ± i` of `P(1, L)` is the `h = 2` case of this pattern. The general signed tower count `P(k, L)` has the same description: with a weight `t` per block, the unrestricted height-`k` transfer matrix is diagonally similar to the Kac-Murdock-Szegő matrix `ρ^|a−b|` with `ρ = √t`, whose tridiagonal part is this strip, and the sign is `ρ = i` ([[castle-sign-kms-matrix](pages/castle-sign-kms-matrix.md)]).

## 4. Bounded height: the Motzkin strip ladder

The unsigned Perron roots `1 + 2cos(π/(h+1))` of the height-`h` Motzkin strip climb toward the Motzkin constant through the metallic and Chebyshev numbers:

| `h` | Perron root | name | Motzkin castles, `c_1 = c_w = 1`, heights `≤ h`, `w = 1…` | OEIS |
|---|---|---|---|---|
| 1 | `1` | - | `1, 1, 1, 1, …` | - |
| 2 | `2` | - | `1, 1, 2, 4, 8, 16, 32, …` | powers of 2 |
| 3 | `1 + √2` | silver | `1, 1, 2, 4, 9, 21, 50, 120, 289, 697` | **A171842**(`w - 1`) |
| 4 | `1 + φ = φ²` | golden squared | `1, 1, 2, 4, 9, 21, 51, 127, 322, 826` | **A005207**(`w - 1`) |
| 5 | `1 + √3` | - | `1, 1, 2, 4, 9, 21, 51, 127, 323, 835, 2187` | **A094286**(`w - 1`) |
| `∞` | `3` | Motzkin | `M_{w-1}` | A001006(`w - 1`) |

The `h = 3` row is the silver strip of [[pell-castle-strip](pages/pell-castle-strip.md)] with both ends pinned. It is **A171842**(`w - 1`), whose entry states "a(n) is the number of Motzkin n-paths of height <= 2" (matched over 16 terms).[^8] So the pinned Pell castle strip is a bounded-height Motzkin strip. The `h = 4` rung has growth `φ²`, the golden ratio squared, because `2cos(π/5) = φ`, and a Fibonacci closed form to match: A005207(`n`) `= (F(2n-1) + F(n+1))/2`, so height-`≤ 4` Motzkin castles number `(F(2w-3) + F(w))/2` for `w ≥ 2` (e.g. `w = 5`: `(13 + 5)/2 = 9`). The `h = 4` and `h = 5` entries carry Kociemba's comment "Number of (s(0), s(1), ..., s(n)) such that 0 < s(i) < 5 [resp. 6] and |s(i) - s(i-1)| <= 1 ..., s(0) = 1, s(n) = 1", which is this castle family written as a sequence.[^12] The whole ladder is the path-graph spectrum `2cos(πj/(h+1))` shifted by one, the same spectrum that [[castle-graph-spectral-radius](pages/castle-graph-spectral-radius.md)] (path-graph castles) and [[bronze-castle-hunt](pages/bronze-castle-hunt.md)] (rectangle castles) meet from the castle-graph side.

## 5. Motzkin prefixes and a near miss

Pin only the first column to height 1 and keep the 1-smooth rule. The skyline minus one is a Motzkin *prefix* of length `w - 1` (it may end at any height), and the count by width is `1, 2, 5, 13, 35, 96, 267, 750, 2123, …` = **A005773**(`w`), the Motzkin prefixes / directed animals (matched over 16 terms).[^9] At height `≤ 3` the same boundary condition gives the Pell numbers ([[pell-castle-strip](pages/pell-castle-strip.md)]).

The unrestricted castles by semi-perimeter, A082582, begin `1, 2, 5, 13, 35, 97, 275, …`. That agrees with A005773 for five terms and then separates, **97 against 96**. The agreement is a small-numbers coincidence between two different objects, and the growth constants differ (`τ² ≈ 3.383` for A082582, see [[castle-perimeter](pages/castle-perimeter.md)], against `3` for A005773). It illustrates [[oeis-cross-referencing](pages/oeis-cross-referencing.md)]'s rule that a match needs a long alignment.

## 6. Relatives in the semi-perimeter grading

Grading by semi-perimeter `s = w + #blocks` instead of width sends several castle families to Motzkin-type sequences. The table gives each count at `s = 2, 3, 4, …`.

| castle family | first terms (`s = 2…`) | OEIS |
|---|---|---|
| all castles | `1, 2, 5, 13, 35, 97, 275, 794` | **A082582**(`s`): bargraphs; also skew Motzkin paths[^6] |
| Motzkin-path castles (1-smooth, `c_1 = c_w = 1`) | `1, 1, 1, 2, 4, 7, 13, 26, 52, 104, 212, 438` | **A023431**(`s - 2`): Motzkin paths with no `UD` and no `UU`[^10] |
| drops of at most 1, `c_w = 1` | `1, 1, 2, 4, 8, 17, 37, 82, 185, 423, 978` | **A004148**(`s - 1`): peakless Motzkin paths, RNA secondary structures[^11] |
| drops of at most 1, any ends | `1, 2, 5, 12, 29, 71, 175, 434, 1082, 2709, 6807` | no OEIS match (searched 2026-09-27); = valleyless Motzkin meanders of length `s - 2`, Prodinger's "not in OEIS" row (§7)[^15] |
| 1-smooth, `c_1 = 1` | `1, 1, 2, 4, 8, 16, 33, 69, 145, 307, 655, 1405, 3027` | no OEIS match (searched 2026-09-26) |
| 1-smooth, free ends | `1, 2, 5, 11, 24, 52, 113, 246, 537, 1176, 2583, 5688` | no OEIS match (searched 2026-09-26) |

The A023431 row follows directly from section 2: a Motzkin-path castle of width `w` with `u` up steps has `s = w + 1 + u`, so it is a Motzkin path of length `w - 1` in which each up step costs one extra unit. That is the entry's "lattice paths … using only steps H=(1,0), U=(1,1) and D=(2,-1)" read backwards (reversal swaps the roles of up and down).[^10] The "drops of at most 1" family ends at height 1 and never falls more than one level per column, so its bargraph has no double fall `DD`. Its mirror image has no double rise, and Deutsch and Elizalde give a bijection from no-double-rise bargraphs of semiperimeter `n + 1` to RNA secondary structures on `n` vertices, which is why A004148 appears.[^13] By width it is the **Catalan** numbers `C_w` (A000108, matched over 12 terms), and by semi-perimeter it is a Motzkin-family sequence, which puts a Catalan object and a peakless-Motzkin object on the same set of castles.

## 7. Castles that never drop by two: valleyless meanders

Drop the end condition from the "drops of at most 1" family: the castles in which every column is at most one lower than the column before it, with any first and last column. By semi-perimeter they number

```
s = 2, 3, 4, …:   1, 2, 5, 12, 29, 71, 175, 434, 1082, 2709, 6807, 17157, 43359, 109830, …
```

which is the sequence Prodinger prints for Motzkin meanders (prefixes, any final height) with no valley `DU`, and reports as not in OEIS.[^15] The agreement holds to 24 terms, and it comes from a bijection. Write a castle `c_1, …, c_w` in this family as the word

```
U^(c_1 - 1),  then for each column i ≥ 2:   D           if c_i = c_{i-1} - 1,
                                            H U^(c_i - c_{i-1})   otherwise.
```

Each column boundary contributes exactly one `H` or `D`, and the `U`s add up to `#blocks − 1`, so the word has length `(w − 1) + (#blocks − 1) = s − 2`. It tracks the height `c_i − 1 ≥ 0` and ends at height `c_w − 1`. A `D` is always followed by `D` or `H`, never by `U`, so the word has no valley. Conversely, a valleyless meander parses uniquely: its initial `U`-run gives `c_1`, and every later `U`-run follows an `H`, because `DU` is forbidden. So this is a bijection between these castles of semi-perimeter `s` and valleyless meanders of length `s − 2`, and it sends last-column height `c_w` to final height `c_w − 1`. Checked by enumeration for every castle with `s ≤ 11` (4520 castles, all valleyless meanders of length `≤ 9` hit once each).

The bijection carries two refinements:

- **Returning meanders** (final height 0) are the castles ending in a height-1 column, which is the A004148 row of §6. So the RNA-structure count of Deutsch-Elizalde is also a valleyless-path count.
- **Peaks.** A factor `UD` of the word is a column that rose and then drops. So the peak count of the meander is the number of *spires*: non-final columns strictly taller than both neighbours, with the first column compared against height 1 on its left. Checked on the same range. Prodinger's corner-weighted GF, with the valley weight at 0, is therefore the GF of these castles by semi-perimeter, last-column height, and spires.

By mirror symmetry the same numbers count castles whose columns never *rise* by more than one, graded the same way. The sequence has no OEIS entry; it is a novel candidate with two readings and a bijection between them ([[castle-sequence-catalogue](pages/castle-sequence-catalogue.md)]).

## Open

- **Castle readings of the Deutsch-Elizalde statistics.** Their §3 table (first-column height, double rises, corners, horizontal segments, columns of height `h`, least column height, area, …) is a list of castle statistics with quadratic GFs in `(width, blocks)`; each has a PE 502 parity split at `y → −y` ([[deutsch-elizalde-2016-bargraphs-cornerless-motzkin](pages/deutsch-elizalde-2016-bargraphs-cornerless-motzkin.md)]), mostly not computed.
- **A bijection castles ↔ skew Motzkin paths** by semi-perimeter; the two are equinumerous (A082582). Prodinger's peak- and valley-refined skew GF says which castle statistics such a map would have to carry.
- **The spectrum of `K(i)`.** For the three gradings on the wiki the sign acts as `√t = i` ([[castle-sign-kms-matrix](pages/castle-sign-kms-matrix.md)]): `P(k, L)` is the KMS matrix at `ρ = i`, and the signed semi-perimeter discriminant is the unsigned one at `√y → i√y`. A closed form for the eigenvalues of `K(i)` is open.
- **q-Motzkin castles.** The Motzkin-path castle graded by area is a q-Motzkin number of the kind [[steep-polyominoes-q-motzkin-bessel](pages/steep-polyominoes-q-motzkin-bessel.md)] studies; with the sign, it is a joint `(q, -1)` specialization.
- **OEIS.** The three parity-split entries (A343386, A107587, A343773) and A171842, A005773 are interlink candidates. The two unmatched semi-perimeter rows are novel candidates.

## Appearances in Sources

- [[motzkin-numbers](pages/motzkin-numbers.md)] - the definition, first values, and generating function.
- [[deutsch-elizalde-2016-bargraphs-cornerless-motzkin](pages/deutsch-elizalde-2016-bargraphs-cornerless-motzkin.md)] - the bargraph ↔ cornerless Motzkin bijection, the castle GF by width and blocks, and the RNA bijection.
- [[prodinger-2025-cornerless-motzkin-bargraphs](pages/prodinger-2025-cornerless-motzkin-bargraphs.md)] - corner-weighted Motzkin meanders and skew paths; the valleyless-meander count of §7.
- [[project-euler-502-representations](pages/project-euler-502-representations.md)] - the tower word and its no-`UD`/no-`DU` rule, which is what makes it cornerless.
- [[project-euler-502-brute-force](pages/project-euler-502-brute-force.md)] - the skyline block-count formula.

## Related Concepts

- [[motzkin-numbers](pages/motzkin-numbers.md)] - the family itself.
- [[tower-word-language](pages/tower-word-language.md)] / [[tower-word-continued-fraction](pages/tower-word-continued-fraction.md)] - the tower word as a Motzkin language, by length A004149.
- [[castle-perimeter](pages/castle-perimeter.md)] - semi-perimeter = width + blocks, A082582, and the signed perimeter count.
- [[castle-classification-shape](pages/castle-classification-shape.md)] - the Motzkin-path and Dyck-path castle types and their fixed-height triangles.
- [[pell-castle-strip](pages/pell-castle-strip.md)] / [[castle-strip](pages/castle-strip.md)] - the silver rung of the Motzkin strip ladder.
- [[signed-tower-count](pages/signed-tower-count.md)] / [[castle-sign](pages/castle-sign.md)] - the `1 ± i` of `P(1, L)`, the `h = 2` signed Motzkin strip.
- [[metallic-means](pages/metallic-means.md)] / [[castle-graph-spectral-radius](pages/castle-graph-spectral-radius.md)] - the `2cos(π/n)` spectrum behind the ladder.
- [[dyck-words](pages/dyck-words.md)] / [[catalan-numbers](pages/catalan-numbers.md)] - steep Dyck words (`M_{n-1}`) and the Catalan "drops at most 1" family.
- [[steep-polyominoes-q-motzkin-bessel](pages/steep-polyominoes-q-motzkin-bessel.md)] - the q-Motzkin direction.
- [[castle-sequence-catalogue](pages/castle-sequence-catalogue.md)] - the status-tagged record of every sequence on this page.
- [[castle-notation](pages/castle-notation.md)] - the symbol conventions; the Motzkin-path castle, the Motzkin strip (castle heights `1, …, h`), `M_n`, `B(x, y)` and `s` are recorded there.
- [[prime-castles](pages/prime-castles.md)] - the same castle bivariate generating function manipulated by the same width-variable substitution.

## Footnotes

[^1]: [[motzkin-numbers](pages/motzkin-numbers.md)] §"Motzkin Numbers" L3, L8 - "the Motzkin paths: lattice paths from (0,0) to (n,0) using up, horizontal, and down steps that never drop below the x axis" and "1, 1, 2, 4, 9, 21, 51, 127, 323, 835, ...".
[^2]: [[project-euler-502-brute-force](pages/project-euler-502-brute-force.md)] §"brute" L24 - "= c_1 + \sum_{i=2}^{w} \max(0, c_i - c_{i-1})", the column-height block-count formula.
[^3]: [[project-euler-502-representations](pages/project-euler-502-representations.md)] §"The tower word" L221-230 - "A castle is U (tower) D", "A tower above a length-L block uses exactly L R's, never drops below the base, and returns to it", "blocks in the tower = number of D's = number of U's", and "a valid tower word has no UD ... and no DU".
[^4]: [[deutsch-elizalde-2016-bargraphs-cornerless-motzkin](pages/deutsch-elizalde-2016-bargraphs-cornerless-motzkin.md)] pp.2-3 §2 L72-77, L89-101 [synthesis] - `Δ : M_{n−1} → B_n` inserts "an up step at the beginning and a down step at the end"; nonempty cornerless paths decompose "uniquely as HA, U A′ D, or U A′ DHA", giving `M = (1 + y(M − 1))(1 + xM)` and `xB² − (1 − x − y − xy)B + xy = 0` with `x` marking `H` and `y` marking `U`.
[^5]: [[prodinger-2025-cornerless-motzkin-bargraphs](pages/prodinger-2025-cornerless-motzkin-bargraphs.md)] pp.1-4 Abstract, §1 L10-18, L144-160 [synthesis] - "Deutsch and Elizalde have linked cornerless Motzkin paths and bargraphs bijectly", "instead of prefixes of bargraphs one might consider prefixes of cornerless Motzkin paths", occurrences of `UD` and `DU` counted by their own variables, extended to skew Motzkin paths by "generating functions and the kernel method".
[^6]: https://oeis.org/A082582 (fetched 2026-09-26) - comments "a(n) is the number of bargraphs of semiperimeter n (n>=2)" and "a(n) is the number of skew Motzkin paths of length n. A skew Motzkin path is a path in the first quadrant which begins at the origin, ends on the x-axis, consists of steps U=(1,1) (up), D=(1,-1) (down), F=(1,0) (flat) and A=(-1,1) (anti-down) so that down and anti-down steps do not overlap."
[^7]: https://oeis.org/A343386, https://oeis.org/A107587, https://oeis.org/A343773 (fetched 2026-09-26) - A343386: "Number of odd Motzkin n-paths, i.e., Motzkin n-paths with an odd number of up steps"; A343773: "Excess of the number of even Motzkin n-paths (A107587) over the odd ones (A343386)", data "1,1,0,-2,-3,1,11,15,-13,-77,-86,144,595,495,-1520,-4810,-2485", formula "a(n) = (-1)^n * A007440(n+1)"; A007440: "Reversion of g.f. for Fibonacci numbers 1, 1, 2, 3, 5, ....".
[^8]: https://oeis.org/A171842 (fetched 2026-09-26) - "a(n) is the number of Motzkin n-paths of height <= 2", and "a(n) is the top left entry of the n-th power of the 3 X 3 matrix [1, 1, 0; 1, 1, 1; 0, 1, 1]"; data "1,1,2,4,9,21,50,120,289,697,1682,4060,…".
[^9]: https://oeis.org/A005773 (fetched 2026-09-26) - "Number of directed animals of size n", with the comment "Also number of paths in an n X n grid from (0,0) to the line x=n-1, using only steps U=(1,1), H=(1,0) and D=(1,-1) (i.e., left factors of length n-1 of Motzkin paths ...)"; a width-`w` castle is a left factor of length `w - 1`, and the counts align with `a(w)` over 16 terms.
[^10]: https://oeis.org/A023431 (fetched 2026-09-26) - "Number of lattice paths in the first quadrant from (0,0) to (n,0) using only steps H=(1,0), U=(1,1) and D=(2,-1)" and "Also number of peakless Motzkin paths of length n with no double rises; in other words, Motzkin paths of length n with no UD's and no UU's".
[^11]: https://oeis.org/A004148 (fetched 2026-09-26) - "Generalized Catalan numbers: a(n+1) = a(n) + Sum_{k=1..n-1} a(k)*a(n-1-k)", with the comment "Enumerates peak-less Motzkin paths of length n"; castle counts align starting at `a(1)` over 21 terms.
[^12]: https://oeis.org/A005207 and https://oeis.org/A094286 (fetched 2026-09-26) - A005207: "a(n) = (F(2*n-1) + F(n+1))/2 where F(n) is a Fibonacci number", with the comment "Number of (s(0), s(1), ..., s(n)) such that 0 < s(i) < 5 and |s(i) - s(i-1)| <= 1 for i = 1,2,...,n, s(0) = 1, s(n) = 1"; A094286: the same with "0 < s(i) < 6". Both align with `a(w - 1)` over 16 terms.
[^13]: [[deutsch-elizalde-2016-bargraphs-cornerless-motzkin](pages/deutsch-elizalde-2016-bargraphs-cornerless-motzkin.md)] p.6 §3.2 L254-271 [synthesis] - the no-double-rise GF "agrees with the generating function for RNA secondary structure numbers" with exponents shifted by one, and a bijection "between bargraphs of semiperimeter n + 1 with no double rises and secondary structures on n vertices"; double rises and double falls are equidistributed "By symmetry" (L239-240).
[^14]: [[prodinger-2025-cornerless-motzkin-bargraphs](pages/prodinger-2025-cornerless-motzkin-bargraphs.md)] p.11 §3 L443-454 [synthesis] - the returning skew series "1 + z + (τ + 1)z^2 + (3 + 2τ)z^3 + (τ^2σ + 7 + 5τ)z^4 + · · ·", which at both weights 1 is "sequence A082582".
[^15]: [[prodinger-2025-cornerless-motzkin-bargraphs](pages/prodinger-2025-cornerless-motzkin-bargraphs.md)] p.8 §2 L321-322 - "we obtain a sequence that is not in [10]", "1 + 2z + 5z^2 + 12z^3 + 29z^4 + 71z^5 + 175z^6 + 434z^7 + 1082z^8 + 2709z^9 + 6807z^10 + · · ·"; in the paper's formulas the zeroed weight for this row marks `DU`, so the paths are valleyless ([[prodinger-2025-cornerless-motzkin-bargraphs](pages/prodinger-2025-cornerless-motzkin-bargraphs.md)]).
