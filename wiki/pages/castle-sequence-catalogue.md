---
title: Castle sequence catalogue
category: Analyses
summary: Hand-curated catalogue of every castle-counting sequence, by the castle object it counts, with first terms, growth, and a novelty status (known / interlink / novel-candidate / unchecked); also the OEIS submission priority list.
tags: [analysis, oeis, castle, sequence, catalogue, novelty, submission-candidate, interlink]
sources: [oeis-mining-pe502]
created: 2026-09-17
updated: 2026-09-20
---

# Castle sequence catalogue

## What this is

This page is the wiki's **castle-native catalogue of sequences**, organized around the *sequences castles produce* rather than around OEIS A-numbers. Every distinct castle-counting sequence gets a record with first terms, recurrence or generating function (GF), growth constant, and a **novelty status**, so the wiki tracks not only which sequences match the Online Encyclopedia of Integer Sequences (OEIS) but also which ones look genuinely new. Even if none are ever submitted, this is the wiki's internal record of castle sequences. It is hand-curated: every status below records an actual search or verification, with its date.

The mechanical companion, a script-generated directory of every A-number cited anywhere on the wiki with the citing pages and mention counts, is [[oeis-index](pages/oeis-index.md)]. The method for identifying an OEIS match and the discipline for verifying it live on [[oeis-cross-referencing](pages/oeis-cross-referencing.md)]; the source workspace where the first mining pass was carried out is [[oeis-mining-pe502](pages/oeis-mining-pe502.md)]; the height-2 hyperbolic interlink (a high-value candidate for submission) lives on [[oeis-height2-hyperbolic-castles](pages/oeis-height2-hyperbolic-castles.md)].

## Novelty status convention

Every castle sequence carries one of four status tags:

- **`known`** — matches an existing OEIS sequence that already has this (or an equivalent) interpretation. The A-number is cited.
- **`interlink`** — matches an existing OEIS sequence, but the castle reading is a *new* interpretation of it (a comment/formula worth submitting). These are the highest-value OEIS contributions — a known number gaining a castle meaning.
- **`novel-candidate`** — computed and **searched against OEIS with no match**. A candidate for a genuinely new submission (human authorship required). Dated, so a later re-search is possible.
- **`unchecked`** — computed on the wiki but **not yet OEIS-searched**. A to-do, not a claim of novelty.

The status is the discipline: *novel-candidate* means someone actually searched and found nothing on that date, not merely that the wiki hasn't mentioned an A-number.


## Submission status (updated 2026-09-19)

From [[oeis-cross-referencing](pages/oeis-cross-referencing.md)]: OEIS requires human authorship, so the wiki accumulates *verified matches* and drafts submission text elsewhere (`raw/oeis-pe502/`). One submission has been filed — the height-2 castle interlink (A038503/A038505), on 2026-09-18. **Interlink** candidates (a known OEIS sequence gaining a castle interpretation) in rough priority order:

1. **A038505 and A038503** — **submitted 2026-09-18.** The height-2 hyperbolic interlink (`F(w,2) = A038505(w+1)`, `odd(w,2) = A038503(w+1) − 1`) is now in both entries: A038503 states it directly as "height ≤ 2, odd blocks" (no `−1`), and the decomposition formulas `a(n) = A000225(n−1) − A038505(n) + 1` and `a(n) = A038505(n) + A146559(n)` were added. See [[oeis-height2-hyperbolic-castles](pages/oeis-height2-hyperbolic-castles.md)].
2. **A146559**: the `a(n) = P(1, n − 1)` comment is still unsubmitted, but the derived `A146559 = A038503 − A038505` identity is now in OEIS — as `a(n) = A038503(n) − A038505(n)` on A146559 itself and as `a(n) = A038505(n) + A146559(n)` on A038503 (both 2026-09-18, [[signed-tower-count](pages/signed-tower-count.md)]).
3. **A005251, A202882, A203094, A203184**: the Hardin word identity gives each an interpretation as `2^{−L}` times an even-last-column signed tower count and proves their empirical recurrences ([[hardin-word-identity](pages/hardin-word-identity.md)]); the `g=2` minimum-tower-spacing castles ([[tower-spacing-castles](pages/tower-spacing-castles.md)]) give each a second, unsigned geometric interpretation. For **A005251** specifically, an explicit bijection ([[a005251-bijection](pages/a005251-bijection.md)]) unifies four castle readings (tree-castle / Hardin / tower-spacing / signed-tower) into one — the strongest form of this candidate; see the multi-interpretation hub below.
4. **A000073, A000078, A001591** (and A000045 by area): the n-nacci numbers as *bounded-height castles by area* ([[bounded-height-castles-nacci](pages/bounded-height-castles-nacci.md)]) — clean compositions-into-`{1..h}` interpretation, high-value for the tribonacci/tetranacci/pentanacci entries.
5. **A217878 / A217879 / A217880 / A217881, A217949 / A217950 / A217951 / A217952, A228457 / A228458, and the tables A217883 / A217954 / A228461**: the whole tower-spacing family ([[tower-spacing-castles](pages/tower-spacing-castles.md)]) is Hardin's "minimum of `g` adjacent elements" arrays, with a proof (running minimum, morphological closing); one comment per entry, plus the `h=2` row **A005252 / A005253 / A005689 / A098574** joining A005251 as height-2 castles with towers `>= g` apart and the closed form `Sum_k C(w+g-(g-1)k, 2k)`. The six unfiled cells `h in {5,6}`, `g in {4,5,6}` are new sequences (below).
6. **A001045**: tree castles of height 3 is a new castle interpretation of Jacobsthal ([[castle-graph](pages/castle-graph.md)]).
7. **A006130, A006131**: tree castles of height 4 and 5 land in the k-Fibonacci family ([[castle-graph](pages/castle-graph.md)]).
8. **A001263, A005408, A005891, A063490, A160747**: the tower / Narayana rows ([[tower-narayana-polynomial](pages/tower-narayana-polynomial.md)]).
9. **A001523, A115981, A332578**: convex / non-convex / valley castles by area ([[castle-by-area](pages/castle-by-area.md)]).
10. **A352116**: `|P(k,4)|` = partial sums of odd triangular numbers ([[castle-eigenvalue-oeis-crosswalk](pages/castle-eigenvalue-oeis-crosswalk.md)]).

**Phase 2 plan (2026-09-18,** `~/code/oeis/pe502/plan-phase-2.md`**).** Phase 1 (items 1–2) is submitted; phase 2 is the next bundle. Tier 2 is the **tower = Narayana** interlink (item 8), submitted in order **A160747 → A005891 → A063490 → A001263** — skipping **A005408** (densest entry, weakest of the set) and minding that **A063490 is offset 1** (the only width-row shift). Tier 3 is the fillers: the difference-of-powers castle counts `A(w,h) = h^w − (h−1)^w` as one comment each on **A000225 / A001047 / A005061 / A005060 / A005062**, and the area synonyms (item 9) each cross-referencing the phase-1 sequences **A038505 / A038503 / A146559**. New sequences ([[new-sequence-fw3](pages/new-sequence-fw3.md)] `F(w,3)` and siblings) follow once the account's edit throttle lifts.

**Novel-candidate** submissions (no OEIS match, genuinely new): the **signed tower count `P(k,·)` rows for `k = 2..6`** ([[signed-tower-count](pages/signed-tower-count.md)]) — a clean C-finite family with a Pell/Chebyshev closed form, the even-`k` all-positive rows (`P(2,·)`, `P(4,·)`, `P(6,·)`) being the most submission-ready; the even-block proper-castle bronze `1,7,25,70,209,697,…` and copper `0,0,10,104,604,…` rows ([[proper-castle-projection](pages/proper-castle-projection.md)]); and the parity-refined area sequences ([[castle-by-area](pages/castle-by-area.md)]). See the sections below for the full status-tagged listing.

**`F(w,3)`** ([[new-sequence-fw3](pages/new-sequence-fw3.md)]) is now also novel-candidate: an oeis.org search for `3, 21, 89, 307, 977, 3031` on 2026-09-19 returned no sequence. Its draft submission package already exists in `raw/oeis-pe502/`.

## Catalogue

Every distinct castle-counting sequence, organized by the castle object it counts, each with first terms, recurrence/GF, growth constant, and a **novelty status** (`known` / `interlink` / `novel-candidate` / `unchecked`, see the convention above). This is where "which castle sequences are genuinely new" is tracked, independent of whether an A-number exists.

### Multi-interpretation hubs

Some sequences appear as *several distinct castle objects*, and where those objects are linked by an explicit bijection the interpretations become one story — the highest-value cross-references.

- **A005251** (plastic-squared `ψ²`; canonical `0, 1, 1, 1, 2, 4, 7, 12, 21, 37, …`) is the wiki's most-interpreted sequence, with **four linked castle readings**, all offset-verified and unified by an explicit bijection ([[a005251-bijection](pages/a005251-bijection.md)]):

  | castle object | count | A005251 offset |
  |---|---|---|
  | tree castles of area `n`, unlimited height (= compositions of `n`, no two adjacent parts `≥ 2`) | `1, 2, 4, 7, 12, …` | `A005251(n+2)` |
  | avoid-`010` binary strings, length `N` | `1, 2, 4, 7, 12, …` | `A005251(N+3)` |
  | minimum-tower-spacing `(h=2, g=2)` castles, width `w` | `2, 4, 7, 12, 21, …` | `A005251(w+3)` |
  | Hardin no-isolated-1 words / signed even-column towers `P_even(6,L)/2^L` | `1, 2, 4, 7, …` | `A005251(L+3)` (`= #{(L+1)`-bit no-isolated-1`}`) |

  The **[[a005251-bijection](pages/a005251-bijection.md)]** connects the first two term-for-term (composition of `n` ↔ avoid-`010` string of length `n−1`, "no adjacent parts `≥ 2`" ⟺ "no factor `010`"); the third (tower-spacing) is literally the second (avoid-010) in row 2; the fourth (Hardin no-isolated-1) is the same count one bit-length over. Status: **interlink** — a clean, high-value OEIS comment candidate (a known sequence gaining four unified castle interpretations). See [[plastic-number](pages/plastic-number.md)].

### Bounded-height castles by area — the n-nacci family

All castles of height `≤ h` graded by total area `A` ([[bounded-height-castles-nacci](pages/bounded-height-castles-nacci.md)]); count = `h`-step Fibonacci, GF `1/(1 − x − ⋯ − x^h)`.

| object | first terms (`A = 1…`) | growth | status |
|---|---|---|---|
| height `≤ 2` by area | `1, 2, 3, 5, 8, 13, 21, 34` | `φ` | **interlink** → [A000045](https://oeis.org/A000045) Fibonacci (new: `=F_{A+1}` as a castle-by-area count) |
| height `≤ 3` by area | `1, 2, 4, 7, 13, 24, 44, 81` | tribonacci `1.8393` | **interlink** → [A000073](https://oeis.org/A000073) (`=A000073(A+2)`) |
| height `≤ 4` by area | `1, 2, 4, 8, 15, 29, 56, 108` | tetranacci | **interlink** → [A000078](https://oeis.org/A000078) (`=A000078(A+3)`) |
| height `≤ 5` by area | `1, 2, 4, 8, 16, 31, 61, 120` | pentanacci | **interlink** → [A001591](https://oeis.org/A001591) (`=A001591(A+4)`) |

*(Every rung is an interlink: a known n-nacci number gaining a "castles bounded by height, by area" reading. OEIS-verified 2026-09-18.)*

### Minimum-tower-spacing castles

Height-`h` castles where every valley between raised regions is `≥ g` columns wide ([[tower-spacing-castles](pages/tower-spacing-castles.md)]); a column-sweep transfer matrix counts them.

| object | first terms | growth | status |
|---|---|---|---|
| `(h=2, g=2)` towers `≥2` apart | `2, 4, 7, 12, 21, 37, 65` | `ψ²` `1.7549` | **interlink** → [A005251](https://oeis.org/A005251) (one node of the four-reading hub above; = the no-isolated-1 object in row 2, [[a005251-bijection](pages/a005251-bijection.md)]) |
| `(h=3, g=2)` | `3, 9, 22, 51, 121, 292, 704` | `2.4022` (quintic) | **interlink** → [A202882](https://oeis.org/A202882) (`=A202882(w+1)`; the **Hardin word family**, geometric route) |
| `(h=4, g=2)` | `4, 16, 50, 144, 422, 1268` | `2.9972` | **interlink** → [A203094](https://oeis.org/A203094) (Hardin) |
| `(h=5, g=2)` | `5, 25, 95, 325, 1121, 3985` | `3.5589` | **interlink** → [A203184](https://oeis.org/A203184) (Hardin) |
| `(h=6, g=2)` | `6, 36, 161, 636, 2507, 10213` | `4.0967` | **interlink** → [A203050](https://oeis.org/A203050) (`=A203050(w+1)`, Hardin) |
| `(h=2, g=3)` towers `>=3` apart | `2, 4, 7, 11, 17, 27, 44` | `φ` `1.6180` | **interlink** → [A005252](https://oeis.org/A005252) (`=A005252(w+3)`) |
| `(h=2, g=4)` | `2, 4, 7, 11, 16, 23, 34` | `1.5289` | **interlink** → [A005253](https://oeis.org/A005253) (`=A005253(w+3)`) |
| `(h=2, g=5)` | `2, 4, 7, 11, 16, 22, 30` | `1.4656` | **interlink** → [A005689](https://oeis.org/A005689) Twopins positions (`=A005689(w+6)`) |
| `(h=2, g=6)` | `2, 4, 7, 11, 16, 22, 29` | `1.4178` | **interlink** → [A098574](https://oeis.org/A098574) (`=A098574(w+6)`) |
| `(h=3, g=3)` | `3, 9, 22, 46, 91, 183, 383` | `2.1069` | **interlink** → [A217878](https://oeis.org/A217878) (0..2 "min of 3 adjacent" arrays) |
| `(h=3, g=4)` | `3, 9, 22, 46, 86, 153, 274` | `1.9274` | **interlink** → [A217879](https://oeis.org/A217879) (0..2 "min of 4 adjacent") |
| `(h=3, g=5)` | `3, 9, 22, 46, 86, 148, 244` | `1.8051` | **interlink** → [A217880](https://oeis.org/A217880) (0..2 "min of 5 adjacent") |
| `(h=3, g=6)` | `3, 9, 22, 46, 86, 148, 239` | `1.7157` | **interlink** → [A217881](https://oeis.org/A217881) (0..2 "min of 6 adjacent") |
| `(h=4, g=3)` | `4, 16, 50, 130, 310, 736` | `2.5398` | **interlink** → [A217949](https://oeis.org/A217949) (0..3 "min of 3 adjacent") |
| `(h=4, g=4)` | `4, 16, 50, 130, 296, 624, 1289` | `2.2733` | **interlink** → [A217950](https://oeis.org/A217950) (0..3 "min of 4 adjacent") |
| `(h=4, g=5)` | `4, 16, 50, 130, 296, 610, 1177` | `2.0966` | **interlink** → [A217951](https://oeis.org/A217951) (0..3 "min of 5 adjacent") |
| `(h=4, g=6)` | `4, 16, 50, 130, 296, 610, 1163` | `1.9697` | **interlink** → [A217952](https://oeis.org/A217952) (0..3 "min of 6 adjacent") |
| `(h=5, g=3)` | `5, 25, 95, 295, 821, 2227, 6254` | `2.9392` | **interlink** → [A228457](https://oeis.org/A228457) (0..4 "maxima of 3 adjacent") |
| `(h=6, g=3)` | `6, 36, 161, 581, 1847, 5615, 17487` | `3.3154` | **interlink** → [A228458](https://oeis.org/A228458) (0..5 "maxima of 3 adjacent") |
| `(h=5, g=4)` | `5, 25, 95, 295, 791, 1927, 4496, 10606` | `2.5888` | **novel-candidate** (no OEIS match, searched 2026-09-20; order 17) |
| `(h=5, g=5)` | `5, 25, 95, 295, 791, 1897, 4196, 8848` | `2.3608` | **novel-candidate** (no OEIS match, searched 2026-09-20; order 21) |
| `(h=5, g=6)` | `5, 25, 95, 295, 791, 1897, 4166, 8548` | `2.1991` | **novel-candidate** (no OEIS match, searched 2026-09-20; order 25) |
| `(h=6, g=4)` | `6, 36, 161, 581, 1792, 4955, 12889, 33279` | `2.8839` | **novel-candidate** (no OEIS match, searched 2026-09-20; order 21) |
| `(h=6, g=5)` | `6, 36, 161, 581, 1792, 4900, 12229, 28681` | `2.6069` | **novel-candidate** (no OEIS match, searched 2026-09-20; order 26) |
| `(h=6, g=6)` | `6, 36, 161, 581, 1792, 4900, 12174, 28021` | `2.4123` | **novel-candidate** (no OEIS match, searched 2026-09-20; order 31) |

*(The whole family is one thing: a tower-spacing-`g` castle is a skyline whose 0-based heights are the window-`g` running minimum of some array, so the `(h,g)` count is Hardin's "0..(h-1) arrays, each element the minimum of `g` adjacent elements", proved on [[tower-spacing-castles](pages/tower-spacing-castles.md)]. The `h=3` row is his table [A217883](https://oeis.org/A217883), the `h=4` row [A217954](https://oeis.org/A217954), the `g=3` column [A228461](https://oeis.org/A228461); the `h=2` row is the A005251 / A005252 / A005253 / A005689 / A098574 run with closed form `Sum_k C(w+g-(g-1)k, 2k)`. Every cell with `h, g <= 6` is now searched (2026-09-20, 24-term alignment on each match): nineteen interlinks, six novel-candidates. Minimal recurrence order is `(h-1)g + 1` in every cell.)*

### The Pell castle strip - 1-smooth height-3 strips

Skylines over `{1, 2, 3}` with adjacent heights differing by at most 1 ([[pell-castle-strip](pages/pell-castle-strip.md)]); the boundary condition picks the sequence.

| object | first terms (`w = 1…`) | growth | status |
|---|---|---|---|
| 1-smooth, first column at height 1 | `1, 2, 5, 12, 29, 70, 169, 408` | `1+√2` | **interlink** → [A000129](https://oeis.org/A000129) Pell (`=P_{w+1}`; GF exactly `1/(1−2x−x²)`) |
| 1-smooth, free first column | `3, 7, 17, 41, 99, 239, 577, 1393` | `1+√2` | **interlink** → [A001333](https://oeis.org/A001333) companion Pell |
| 1-smooth, both end columns at height 1 | `1, 1, 2, 4, 9, 21, 50, 120` | `1+√2` | **unchecked** |

*(Verified by enumeration and by `e_1ᵀ(I − xM)^{−1}𝟙` on the 3×3 transfer matrix, 2026-09-19.)*

### Proper-castle (max=h + even-block) metallic ladder

The `J − D` metallic-strip counts, and their projection to proper Project Euler 502 (PE 502) castles ([[proper-castle-projection](pages/proper-castle-projection.md)]).

| object | first terms | growth | status |
|---|---|---|---|
| silver free strip (`h=3`) | `3, 7, 17, 41, 99, 239, 577` | `1+√2` | **interlink** → [A001333](https://oeis.org/A001333) Pell–Lucas (companion, not primary Pell) |
| bronze free strip (`h=4`) | `4, 13, 43, 142, 469, 1549` | `(3+√13)/2` | **interlink** → [A003688](https://oeis.org/A003688) |
| copper free strip (`h=5`) | `5, 21, 89, 377, 1597, 6765` | `φ³` | **interlink** → [A015448](https://oeis.org/A015448) (`=F_{3n+5}` trisection) |
| bronze **even-block** proper | `1, 7, 25, 70, 209, 697, 2390` | `(3+√13)/2` | **novel-candidate** (no OEIS match, searched 2026-09-18) |
| copper **even-block** proper | `0, 0, 10, 104, 604, 2836, 12630` | `φ³` | **novel-candidate** (no OEIS match, searched 2026-09-18) |

### Signed tower count P(k,·) rows

The signed tower count `P(k,L) = Σ (−1)^blocks` in the `L`-direction at fixed `k` ([[signed-tower-count](pages/signed-tower-count.md)]); C-finite of order `k+1`. Even-`k` rows are all-positive; odd-`k` rows alternate in sign.

| object | first terms (`L = 0…`) | order | growth | status |
|---|---|---|---|---|
| `P(1, L)` | `1, 0, −2, −4, −4, 0, 8, 16, …` | 2 | `√2` (`1±i`) | **interlink** → [A146559](https://oeis.org/A146559) (`= Re((1+i)^{L+1})`) |
| `P(2, L)` | `1, 1, 3, 9, 19, 33, 59, 121, 259, 529` | 3 | `2` | **novel-candidate** (no match, 2026-09-18) |
| `P(3, L)` | `1, 0, −4, −16, −40, −64, −32, 192, 832, …` | 4 | `2.193` (`\|r\|`) | **novel-candidate** (signed and `\|·\|` both no match, 2026-09-18) |
| `P(4, L)` | `1, 1, 5, 25, 85, 225, 541, 1385, 3973` | 5 | `2.796` | **novel-candidate** (no match, 2026-09-18) |
| `P(5, L)` | `1, 0, −6, −36, −140, −384, −680, −112, 5040, …` | 6 | `2.892` (`\|r\|`) | **novel-candidate** (signed and `\|·\|` both no match, 2026-09-18) |
| `P(6, L)` | `1, 1, 7, 49, 231, 833, 2583, 7889, 26503, …` | 7 | `2ψ² = 3.5098` | **novel-candidate** (no match, 2026-09-18); char poly factors `(x³−4x²+4x−8)(x⁴−3x³+8x²−4x+8)`, dominant root `2ψ²` ([[plastic-number](pages/plastic-number.md)]) |

*(**All of `P(2..6, ·)` are novel** — no OEIS match in signed or absolute-value form, searched 2026-09-18. Even-`k` rows are all-positive and their char polys factor (dominant root `2` / `2.796` / `2ψ²`); odd-`k` rows alternate in sign with irreducible char polys and complex dominant roots. The whole family has a Pell/Chebyshev closed-form denominator — `den_k = A·r_+^k + B·r_−^k`, roots `−x ± √(x²+1)` — on [[generating-function-gallery](pages/generating-function-gallery.md)]. The even-`k` positive rows are the cleanest submission candidates.)*

### Strip Perron-root sequences (reachable-field census)

Width-graded counts of the 0/1 transfer-matrix strips ([[reachable-field-census](pages/reachable-field-census.md)], [[metallic-strip-realizability](pages/metallic-strip-realizability.md)]). The plastic strip (`x³−x−1`) and the non-metallic quadratic strips (`Q(√17)`, `Q(√21)`, …) generate count sequences that are mostly **unchecked** against OEIS — a mining target.

- Plastic strip (height-3, rule `1→3, 2→1, 3→{1,2}`), the Padovan/Perrin-rate count — **unchecked**.
- The non-metallic quadratic strips `Q(√17)`, `Q(√21)`, `Q(√6)`, `Q(√7)`, `Q(√33)` — **unchecked**.

### Legacy generation candidates (pre-catalogue, statuses to refresh)

Computed earlier and listed as candidates before the status convention; most are **unchecked** pending an OEIS search on current terms.

- `F(w, 3)`: even-block castles of height exactly 3, `0, 0, 3, 21, 89, 307, 977, 3031, …` ([[new-sequence-fw3](pages/new-sequence-fw3.md)]) — **novel-candidate** (no OEIS match, searched 2026-09-19).
- `F(w, 4…6)`: the taller rows ([[new-sequence-fw3](pages/new-sequence-fw3.md)]) — **unchecked**.
- Fixed-width columns ([[sum-of-three-cubes-castles](pages/sum-of-three-cubes-castles.md)]): `F(3, 2m) = 10m^2 - 5m + 1 = 5·Hex(m) + 1`, `6, 31, 76, 141, 226, 331, 456, 601, 766, 951, …` — **novel-candidate** (no OEIS match by terms or formula, searched 2026-09-20; it is A080860 at negative index). `odd(3, 2n+1) = 10n^2 + 5n + 1`, `1, 16, 51, 106, 181, 276, …` — **interlink** → [A080860](https://oeis.org/A080860) (exact, offset 0). `F(3, 2m+1) = odd(3, 2m) = C(2m+1, 2)` and `C(2m, 2)` — **known**, triangular numbers A000217. The interleaved columns `F(3,h)` (`6, 3, 31, 10, 76, 21, …`), `odd(3,h)`, and `F(4,h)` (`10, 21, 117, 122, 448, 367, 1131, 820, …`) — **novel-candidate** (searched 2026-09-20, no match); `F(4,h)` is the quasi-polynomial `(4h-3)(4h^2-3h+2)/6` at even `h`, `(h-1)(8h^2-4h+3)/6` at odd `h`.
- `|P(k, L)|` in the *k*-direction at fixed `L ≥ 5` ([[castle-eigenvalue-oeis-crosswalk](pages/castle-eigenvalue-oeis-crosswalk.md)]) — **unchecked**. *(The L-direction `P(k,·)` rows for `k = 2..6` are no longer here — they are searched and confirmed **novel-candidate** in the "Signed tower count P(k,·) rows" section above.)*
- Parity-refined area sequences (even/odd-area convex, `strict_valley`) ([[castle-by-area](pages/castle-by-area.md)]) — **novel-candidate** (noted "none in OEIS" on that page).
- Higher tower rows `w ≥ 6` in the Narayana table ([[tower-narayana-polynomial](pages/tower-narayana-polynomial.md)]) — **unchecked**.
- Jacobi-Perron convergent denominators of `2ψ²` ([[castle-eigenvalue-oeis-crosswalk](pages/castle-eigenvalue-oeis-crosswalk.md)]) — **unchecked**.

## Appearances in Sources

- [[oeis-mining-pe502](pages/oeis-mining-pe502.md)] - the source workspace where the mining passes were carried out; the interlink candidates in the submission list trace back to veins there.

## Related Concepts

- [[oeis-index](pages/oeis-index.md)] - the script-generated A-number directory: every OEIS number cited on the wiki, grouped by role, with citing pages and mention counts.
- [[oeis-cross-referencing](pages/oeis-cross-referencing.md)] - the method: verify against OEIS data with offsets, distinguish interlinking from generation, honor the human-authorship rule.
- [[oeis-height2-hyperbolic-castles](pages/oeis-height2-hyperbolic-castles.md)] - the highest-value submission candidate.
- [[hyperbolic-sequence-family](pages/hyperbolic-sequence-family.md)] - the A038503 / A038504 / A038505 / A000749 family collectively.
- [[metallic-means](pages/metallic-means.md)] / [[pell-numbers](pages/pell-numbers.md)] / [[plastic-number](pages/plastic-number.md)] - the number-family threads whose OEIS sequences populate this catalogue.
- [[castle-graph](pages/castle-graph.md)] - the tree-castle counts on Fibonacci / Jacobsthal / k-Fibonacci.
- [[castle-eigenvalue-oeis-crosswalk](pages/castle-eigenvalue-oeis-crosswalk.md)] - the metallic-mean convergent tables.
- [[hardin-word-identity](pages/hardin-word-identity.md)] - the Hardin sequences A202882 / A203094 / A203184 and their proved recurrences.
- [[new-sequence-fw3](pages/new-sequence-fw3.md)] - the leading generation candidate.
- [[bounded-height-castles-nacci](pages/bounded-height-castles-nacci.md)] - the n-nacci-by-area interlinks (A000073 / A000078 / A001591).
- [[tower-spacing-castles](pages/tower-spacing-castles.md)] - the tower-spacing family whose g=2 column is the Hardin sequences and g=3 the "min of 3 adjacent" family.
- [[proper-castle-projection](pages/proper-castle-projection.md)] - the even-block proper-castle rows, the novel-candidate entries.
- [[reachable-field-census](pages/reachable-field-census.md)] - the strip Perron-root sequences, mostly unchecked against OEIS.
- [[a005251-bijection](pages/a005251-bijection.md)] - the explicit bijection unifying A005251's four castle readings; the multi-interpretation hub's centerpiece.
