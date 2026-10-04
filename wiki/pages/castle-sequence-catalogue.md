---
title: Castle sequence catalogue
category: Analyses
summary: Hand-curated catalogue of every castle-counting sequence, by the castle object it counts, with first terms, growth, and a novelty status (known / interlink / novel-candidate / unchecked); also the OEIS submission priority list.
tags: [analysis, oeis, castle, sequence, catalogue, novelty, submission-candidate, interlink]
sources: [oeis-mining-pe502]
created: 2026-09-17
updated: 2026-10-04
---

# Castle sequence catalogue

## What this is

This page is the wiki's **castle-native catalogue of sequences**, organized around the *sequences castles produce* rather than around OEIS A-numbers. Every distinct castle-counting sequence gets a record with first terms, recurrence or generating function (GF), growth constant, and a **novelty status**, so the wiki tracks both which sequences match the Online Encyclopedia of Integer Sequences (OEIS) and which do not. Even if none are ever submitted, this is the wiki's internal record of castle sequences. It is hand-curated: every status below records an actual search or verification, with its date.

The mechanical companion, a script-generated directory of every A-number cited anywhere on the wiki with the citing pages and mention counts, is [[oeis-index](pages/oeis-index.md)]. The method for identifying an OEIS match and the discipline for verifying it live on [[oeis-cross-referencing](pages/oeis-cross-referencing.md)]; the source workspace where the first mining pass was carried out is [[oeis-mining-pe502](pages/oeis-mining-pe502.md)]; the height-2 hyperbolic interlink lives on [[oeis-height2-hyperbolic-castles](pages/oeis-height2-hyperbolic-castles.md)].

## Novelty status convention

Every castle sequence carries one of four status tags:

- **`known`** — matches an existing OEIS sequence that already has this (or an equivalent) interpretation. The A-number is cited.
- **`interlink`** — matches an existing OEIS sequence, but the castle reading is a *new* interpretation of it (a comment/formula to submit).
- **`novel-candidate`** — computed and **searched against OEIS with no match**. A candidate for a new submission (human authorship required). Dated, so a later re-search is possible.
- **`unchecked`** — computed on the wiki and **not yet searched against OEIS**; no novelty is claimed.

The status is the discipline: *novel-candidate* means someone actually searched and found nothing on that date, not merely that the wiki hasn't mentioned an A-number.


## Submission status

From [[oeis-cross-referencing](pages/oeis-cross-referencing.md)]: OEIS requires human authorship, so the wiki accumulates *verified matches* and drafts submission text elsewhere (`raw/oeis-pe502/`). The height-2 castle interlink (A038503/A038505/A146559) is approved and in the OEIS entries. **Interlink** candidates (a known OEIS sequence gaining a castle interpretation) in rough priority order:

1. **A038505 and A038503** — **on OEIS** (entered 2026-09-18, proposed 2026-09-26, approved; revised Oct 03 2026). The height-2 hyperbolic interlink (`F(w,2) = A038505(w+1)`, `odd(w,2) = A038503(w+1) − 1`) is a comment on both entries: the A038503 comment is worded "height at most 2" (it counts the `r = 0` term `C(n, 0)` as a castle) and a correction to the exact-height statement `a(n) − 1 = odd(n−1, 2)` was submitted 2026-10-04; the entry carries the decomposition formulas `a(n) = A000225(n−1) − A038505(n) + 1` and `a(n) = A038505(n) + A146559(n)`. See [[oeis-height2-hyperbolic-castles](pages/oeis-height2-hyperbolic-castles.md)].
2. **A146559**: the castle comment (`a(n) − 1` = odd-block minus even-block castles of width `n−1` and height 2, i.e. `a(n) = P(1, n − 1)`) was submitted 2026-10-04 and awaits approval. The identity `a(n) = A038503(n) − A038505(n)` is approved on A146559 and the equivalent `a(n) = A038505(n) + A146559(n)` on A038503 (both signed Sep 26 2026; [[signed-tower-count](pages/signed-tower-count.md)]).
3. **A005251, A202882, A203094, A203184**: the Hardin word identity gives each an interpretation as `2^{−L}` times an even-last-column signed tower count and proves their empirical recurrences ([[hardin-word-identity](pages/hardin-word-identity.md)]); the `g=2` minimum-tower-spacing castles ([[tower-spacing-castles](pages/tower-spacing-castles.md)]) give each a second, unsigned geometric interpretation. For **A005251** specifically, an explicit bijection ([[a005251-bijection](pages/a005251-bijection.md)]) relates four castle readings (tree-castle / Hardin / tower-spacing / signed-tower); see the multi-interpretation hub below.
4. **A000073, A000078, A001591** (and A000071 for castles of height 2 by area): the n-nacci numbers as *bounded-height castles by area* ([[exact-height-castle-by-area](pages/exact-height-castle-by-area.md)]), through compositions into `{1..h}`.
5. **A217878 / A217879 / A217880 / A217881, A217949 / A217950 / A217951 / A217952, A228457 / A228458, and the tables A217883 / A217954 / A228461**: the whole tower-spacing family ([[tower-spacing-castles](pages/tower-spacing-castles.md)]) is Hardin's "minimum of `g` adjacent elements" arrays, with a proof (running minimum, morphological closing); one comment per entry, plus the `h=2` row **A005252 / A005253 / A005689 / A098574** joining A005251 as height-2 castles with towers `>= g` apart and the closed form `Sum_k C(w+g-(g-1)k, 2k)`. The six unfiled cells `h in {5,6}`, `g in {4,5,6}` are new sequences (below).
6. **A001045**: tree castles of height at most 3, by width, are the Jacobsthal numbers ([[castle-graph](pages/castle-graph.md)]).
7. **A006130, A006131**: tree castles of height 4 and 5 land in the k-Fibonacci family ([[castle-graph](pages/castle-graph.md)]).
8. **A001263, A005408, A005891, A063490, A160747**: the tower / Narayana rows ([[tower-narayana-polynomial](pages/tower-narayana-polynomial.md)]).
9. **A001523, A115981, A332578**: convex / non-convex / valley castles by area ([[castle-by-area](pages/castle-by-area.md)]).
10. **A352116**: `|P(k,4)|` = partial sums of odd triangular numbers ([[castle-eigenvalue-oeis-crosswalk](pages/castle-eigenvalue-oeis-crosswalk.md)]).
11. **A343386, A107587, A343773, A171842, A005773**: the Motzkin-path castle and its PE 502 parity split (even-block = odd Motzkin paths), the height-`≤ 3` Motzkin strip, and the Motzkin prefixes ([[motzkin-castles](pages/motzkin-castles.md)]).

**Order after the height-2 interlink.** The **tower = Narayana** rows (the tower / Narayana entry above) in the order **A160747 → A005891 → A063490 → A001263**, leaving out **A005408** (the densest entry) and minding that **A063490 is offset 1** (the only width-row shift). Then the difference-of-powers castle counts `A(w,h) = h^w − (h−1)^w`, one comment each on **A000225 / A001047 / A005061 / A005060 / A005062**, and the area synonyms (convex / non-convex / valley by area, above), each cross-referencing **A038505 / A038503 / A146559**. New sequences ([[new-sequence-fw3](pages/new-sequence-fw3.md)] `F(w,3)` and siblings) come after.

**Novel-candidate** submissions (no OEIS match): the **signed tower count `P(k,·)` rows for `k = 2..6`** ([[signed-tower-count](pages/signed-tower-count.md)]), a C-finite family with a Pell/Chebyshev closed-form denominator, whose even-`k` rows (`P(2,·)`, `P(4,·)`, `P(6,·)`) are positive; the even-block proper-castle bronze `1,7,25,70,209,697,…` and copper `0,0,10,104,604,…` rows ([[proper-castle-projection](pages/proper-castle-projection.md)]); and the parity-refined area sequences ([[castle-by-area](pages/castle-by-area.md)]). See the sections below for the full status-tagged listing.

**`F(w,3)`** ([[new-sequence-fw3](pages/new-sequence-fw3.md)]) is novel-candidate: an oeis.org search for `3, 21, 89, 307, 977, 3031` on 2026-09-19 returned no sequence. Its draft submission is in `raw/oeis-pe502/`.

## Catalogue

Every distinct castle-counting sequence, organized by the castle object it counts, each with first terms, recurrence/GF, growth constant, and a **novelty status** (`known` / `interlink` / `novel-candidate` / `unchecked`, see the convention above). This is where the wiki records which castle sequences are new, independent of whether an A-number exists.

### Multi-interpretation hubs

Some sequences count *several distinct castle objects*, linked by explicit bijections.

- **A005251** (plastic-squared `ψ²`; canonical `0, 1, 1, 1, 2, 4, 7, 12, 21, 37, …`) has **four linked castle readings**, all offset-verified, related by an explicit bijection ([[a005251-bijection](pages/a005251-bijection.md)]):

  | castle object | count | A005251 offset |
  |---|---|---|
  | tree castles of area `n`, unlimited height (= compositions of `n`, no two adjacent parts `≥ 2`) | `1, 2, 4, 7, 12, …` | `A005251(n+2)` |
  | avoid-`010` binary strings, length `N` | `1, 2, 4, 7, 12, …` | `A005251(N+3)` |
  | minimum-tower-spacing `(h=2, g=2)` castles, width `w` | `2, 4, 7, 12, 21, …` | `A005251(w+3)` |
  | Hardin no-isolated-1 words / signed even-column towers `P_even(6,L)/2^L` | `1, 2, 4, 7, …` | `A005251(L+3)` (`= #{(L+1)`-bit no-isolated-1`}`) |

  The **[[a005251-bijection](pages/a005251-bijection.md)]** connects the first two term-for-term (composition of `n` ↔ avoid-`010` string of length `n−1`, "no adjacent parts `≥ 2`" ⟺ "no factor `010`"); the third (tower-spacing, towers `≥ 2` apart, width `w`) is a raised-column string of length `w` with no factor `101`, which complementing the bits turns into the second; the fourth (Hardin no-isolated-1) has the same count one bit-length longer. Status: **interlink** (a known sequence gaining four castle interpretations). See [[plastic-number](pages/plastic-number.md)].

### Bounded-height castles by area — the n-nacci family

All castles of height `≤ h` graded by total area `A` ([[exact-height-castle-by-area](pages/exact-height-castle-by-area.md)]); count = `h`-step Fibonacci, GF `1/(1 − x − ⋯ − x^h)`. The height-2 row counts castles of height 2: `F_{A+1} − 1`.

| object | first terms (`A = 1…`) | growth | status |
|---|---|---|---|
| height 2 by area | `0, 1, 2, 4, 7, 12, 20, 33` | `φ` | **interlink** → [A000071](https://oeis.org/A000071) (`= A000071(A+1) = F_{A+1} − 1`; brute force `A = 1..14`, 2026-10-04) |
| height `≤ 3` by area | `1, 2, 4, 7, 13, 24, 44, 81` | tribonacci `1.8393` | **interlink** → [A000073](https://oeis.org/A000073) (`=A000073(A+2)`) |
| height `≤ 4` by area | `1, 2, 4, 8, 15, 29, 56, 108` | tetranacci | **interlink** → [A000078](https://oeis.org/A000078) (`=A000078(A+3)`) |
| height `≤ 5` by area | `1, 2, 4, 8, 16, 31, 61, 120` | pentanacci | **interlink** → [A001591](https://oeis.org/A001591) (`=A001591(A+4)`) |

*(Every rung is an interlink: a known n-nacci number gaining a "castles bounded by height, by area" reading. OEIS-verified 2026-09-18.)*

### Minimum-tower-spacing castles

Height-`h` castles where every valley between raised regions is `≥ g` columns wide ([[tower-spacing-castles](pages/tower-spacing-castles.md)]); a column-sweep transfer matrix counts them.

| object | first terms | growth | status |
|---|---|---|---|
| `(h=2, g=2)` towers `≥2` apart | `2, 4, 7, 12, 21, 37, 65` | `ψ²` `1.7549` | **interlink** → [A005251](https://oeis.org/A005251) (one node of the four-reading hub above) |
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

*(The family has one description: a tower-spacing-`g` castle is a skyline whose 0-based heights are the window-`g` running minimum of some array, so the `(h,g)` count is Hardin's "0..(h-1) arrays, each element the minimum of `g` adjacent elements", proved on [[tower-spacing-castles](pages/tower-spacing-castles.md)]. The `h=3` row is his table [A217883](https://oeis.org/A217883), the `h=4` row [A217954](https://oeis.org/A217954), the `g=3` column [A228461](https://oeis.org/A228461); the `h=2` row is the A005251 / A005252 / A005253 / A005689 / A098574 run with closed form `Sum_k C(w+g-(g-1)k, 2k)`. Every cell with `h, g <= 6` is searched (2026-09-20, 24-term alignment on each match): nineteen interlinks, six novel-candidates. Minimal recurrence order is `(h-1)g + 1` in every cell.)*

### The Pell castle strip - 1-smooth height-3 strips

Skylines over `{1, 2, 3}` with adjacent heights differing by at most 1 ([[pell-castle-strip](pages/pell-castle-strip.md)]); the boundary condition picks the sequence.

| object | first terms (`w = 1…`) | growth | status |
|---|---|---|---|
| 1-smooth, first column at height 1 | `1, 2, 5, 12, 29, 70, 169, 408` | `1+√2` | **interlink** → [A000129](https://oeis.org/A000129) Pell (`= P_w`; width GF `x/(1−2x−x²)`) |
| 1-smooth, free first column | `3, 7, 17, 41, 99, 239, 577, 1393` | `1+√2` | **interlink** → [A001333](https://oeis.org/A001333) Pell-Lucas |
| 1-smooth, both end columns at height 1 | `1, 1, 2, 4, 9, 21, 50, 120` | `1+√2` | **interlink** → [A171842](https://oeis.org/A171842) (`=a(w−1)`, "Motzkin n-paths of height <= 2"; searched 2026-09-26, 16 terms, see [[motzkin-castles](pages/motzkin-castles.md)]) |

*(Verified by enumeration and by `e_1ᵀ(I − xM)^{−1}𝟙` on the 3×3 transfer matrix, 2026-09-19.)*

### Motzkin castles

The Motzkin family in castle counts ([[motzkin-castles](pages/motzkin-castles.md)]). A **Motzkin-path castle** is 1-smooth (`|c_{i+1} − c_i| ≤ 1`) with both end columns at height 1; its skyline minus one is a Motzkin path of length `w − 1`, and its block count is `1 + #up-steps`, so the PE 502 parity clause splits the Motzkin numbers into odd/even Motzkin paths. All rows aligned against OEIS data on 2026-09-26 (16 terms by width, 21 by semi-perimeter).

| object | first terms | growth | status |
|---|---|---|---|
| Motzkin-path castles by width | `1, 1, 2, 4, 9, 21, 51, 127, 323, 835` | `3` | **known** → [A001006](https://oeis.org/A001006) (`=M_{w−1}`) |
| even-block Motzkin-path castles (PE 502 parity, all heights) | `0, 0, 1, 3, 6, 10, 20, 56, 168, 456, 1137, 2827` | `3` | **interlink** → [A343386](https://oeis.org/A343386) (`=a(w−1)`, odd Motzkin paths; castle reading absent) |
| odd-block Motzkin-path castles | `1, 1, 1, 1, 3, 11, 31, 71, 155, 379, 1051, 2971` | `3` | **interlink** → [A107587](https://oeis.org/A107587) (`=a(w−1)`, even Motzkin paths) |
| signed `Σ(−1)^blocks` | `−1, −1, 0, 2, 3, −1, −11, −15, 13, 77, 86, −144` | `\|1±2i\| = √5` | **interlink** → [A343773](https://oeis.org/A343773) (`=−a(w−1)`; `= ±A007440`, reversion of Fibonacci) |
| Motzkin-path castles, heights `≤ 4` | `1, 1, 2, 4, 9, 21, 51, 127, 322, 826` | `φ²` | **known** → [A005207](https://oeis.org/A005207) (`=a(w−1) = (F(2w−3)+F(w))/2`; Kociemba's bounded-walk comment is the castle family) |
| Motzkin-path castles, heights `≤ 5` | `1, 1, 2, 4, 9, 21, 51, 127, 323, 835, 2187` | `1+√3` | **known** → [A094286](https://oeis.org/A094286) (`=a(w−1)`, same comment with `< 6`) |
| 1-smooth, first column at height 1, by width | `1, 2, 5, 13, 35, 96, 267, 750` | `3` | **interlink** → [A005773](https://oeis.org/A005773) (`=a(w)`, Motzkin left factors / directed animals) |
| drops of at most 1, last column at height 1, by width | `1, 2, 5, 14, 42, 132, 429` | `4` | **interlink** → [A000108](https://oeis.org/A000108) (`=C_w`) |
| Motzkin-path castles by semi-perimeter (`s = 2…`) | `1, 1, 1, 2, 4, 7, 13, 26, 52, 104, 212, 438` | - | **interlink** → [A023431](https://oeis.org/A023431) (`=a(s−2)`, Motzkin paths with no `UD`, no `UU`) |
| drops of at most 1, last column at height 1, by semi-perimeter | `1, 1, 2, 4, 8, 17, 37, 82, 185, 423, 978` | - | **interlink** → [A004148](https://oeis.org/A004148) (`=a(s−1)`, peakless Motzkin paths; the no-double-rise mirror is Deutsch-Elizalde's RNA-secondary-structure bijection, [[deutsch-elizalde-2016-bargraphs-cornerless-motzkin](pages/deutsch-elizalde-2016-bargraphs-cornerless-motzkin.md)]) |
| drops of at most 1, any ends, by semi-perimeter | `1, 2, 5, 12, 29, 71, 175, 434, 1082, 2709, 6807, 17157` | - | **novel-candidate** (no OEIS match, searched 2026-09-27); = valleyless Motzkin meanders of length `s−2` by an explicit bijection, the sequence [[prodinger-2025-cornerless-motzkin-bargraphs](pages/prodinger-2025-cornerless-motzkin-bargraphs.md)] reports as not in OEIS; refined by last-column height and spires ([[motzkin-castles](pages/motzkin-castles.md)] §7) |
| 1-smooth, first column at height 1, by semi-perimeter | `1, 1, 2, 4, 8, 16, 33, 69, 145, 307, 655, 1405, 3027` | - | **novel-candidate** (no OEIS match, searched 2026-09-26) |
| 1-smooth, free ends, by semi-perimeter | `1, 2, 5, 11, 24, 52, 113, 246, 537, 1176, 2583, 5688` | - | **novel-candidate** (no OEIS match, searched 2026-09-26) |

*(All castles by semi-perimeter, A082582, are cornerless Motzkin paths graded by `#flats + #ups` and are equinumerous with skew Motzkin paths; that row stays under "Castles by semi-perimeter" below. Its first five terms `1, 2, 5, 13, 35` coincide with A005773 before `97 ≠ 96`.)*

### Ridge castles: the metallic ladder (free strip, max=h, even-block)

The ridge rule: adjacent columns differ in height unless both equal the ceiling `h`, transfer matrix `R_h = J − D` ([[castle-classification-shape](pages/castle-classification-shape.md)] Axis 2). Free-strip counts (heights in `1..h`, `max = h` not imposed), ridge castles of exact height `h`, and their even-block part, the proper Project Euler 502 (PE 502) count ([[proper-castle-projection](pages/proper-castle-projection.md)]).

| object | first terms | growth | status |
|---|---|---|---|
| silver free ridge strip (`h=3`) | `3, 7, 17, 41, 99, 239, 577` | `1+√2` | **interlink** → [A001333](https://oeis.org/A001333) Pell–Lucas (companion, not primary Pell) |
| bronze free ridge strip (`h=4`) | `4, 13, 43, 142, 469, 1549` | `(3+√13)/2` | **interlink** → [A003688](https://oeis.org/A003688) |
| copper free ridge strip (`h=5`) | `5, 21, 89, 377, 1597, 6765` | `φ³` | **interlink** → [A015448](https://oeis.org/A015448) (`=F_{3n+5}` trisection) |
| bronze ridge castles (`h=4`, max=h) | `1, 7, 31, 118, 421, 1453, 4924` | `(3+√13)/2` | **novel-candidate** (no OEIS match, searched 2026-09-18) |
| bronze **even-block** ridge castles | `1, 7, 25, 70, 209, 697, 2390` | `(3+√13)/2` | **novel-candidate** (no OEIS match, searched 2026-09-18) |
| copper **even-block** ridge castles | `0, 0, 10, 104, 604, 2836, 12630` | `φ³` | **novel-candidate** (no OEIS match, searched 2026-09-18) |

### Signed tower count P(k,·) rows

The signed tower count `P(k,L) = Σ (−1)^blocks` in the `L`-direction at fixed `k` ([[signed-tower-count](pages/signed-tower-count.md)]); C-finite of order `k+1`. Even-`k` rows are positive (checked `k ≤ 12`, `L < 40`); odd-`k` rows change sign in runs, their dominant eigenvalues being a complex pair.

| object | first terms (`L = 0…`) | order | growth | status |
|---|---|---|---|---|
| `P(1, L)` | `1, 0, −2, −4, −4, 0, 8, 16, …` | 2 | `√2` (`1±i`) | **interlink** → [A146559](https://oeis.org/A146559) (`= Re((1+i)^{L+1})`) |
| `P(2, L)` | `1, 1, 3, 9, 19, 33, 59, 121, 259, 529` | 3 | `2` | **novel-candidate** (no match, 2026-09-18) |
| `P(3, L)` | `1, 0, −4, −16, −40, −64, −32, 192, 832, …` | 4 | `2.193` (`\|r\|`) | **novel-candidate** (signed and `\|·\|` both no match, 2026-09-18) |
| `P(4, L)` | `1, 1, 5, 25, 85, 225, 541, 1385, 3973` | 5 | `2.796` | **novel-candidate** (no match, 2026-09-18) |
| `P(5, L)` | `1, 0, −6, −36, −140, −384, −680, −112, 5040, …` | 6 | `2.892` (`\|r\|`) | **novel-candidate** (signed and `\|·\|` both no match, 2026-09-18) |
| `P(6, L)` | `1, 1, 7, 49, 231, 833, 2583, 7889, 26503, …` | 7 | `2ψ² = 3.5098` | **novel-candidate** (no match, 2026-09-18); char poly factors `(x³−4x²+4x−8)(x⁴−3x³+8x²−4x+8)`, dominant root `2ψ²` ([[plastic-number](pages/plastic-number.md)]) |

*(**None of `P(2..6, ·)` has an OEIS match**, in signed or absolute-value form, searched 2026-09-18. Even-`k` rows are positive and their char polys factor (dominant root `2` / `2.796` / `2ψ²`); odd-`k` rows change sign in runs, with char polys irreducible in every case checked and complex dominant roots. The whole family has a Pell/Chebyshev closed-form denominator, `den_k = A·r_+^k + B·r_−^k` with `r_± = −x ± √(x²+1)`, on [[generating-function-gallery](pages/generating-function-gallery.md)].)*

### Strip Perron-root sequences (reachable-field census)

Width-graded counts of the 0/1 transfer-matrix strips ([[reachable-field-census](pages/reachable-field-census.md)], [[metallic-strip-realizability](pages/metallic-strip-realizability.md)]). The plastic strip (`x³−x−1`) and the non-metallic quadratic strips (`Q(√17)`, `Q(√21)`, …) generate count sequences that are mostly **unchecked** against OEIS.

- Plastic strip (height-3, rule `1→3, 2→1, 3→{1,2}`), the Padovan/Perrin-rate count — **unchecked**.
- The non-metallic quadratic strips `Q(√17)`, `Q(√21)`, `Q(√6)`, `Q(√7)`, `Q(√33)` — **unchecked**.

### Castles by semi-perimeter

A castle's semi-perimeter is `w + #blocks` ([[castle-perimeter](pages/castle-perimeter.md)]), so these are the castle counts in Delest-Viennot's perimeter grading, with the PE 502 parity split. All GFs are algebraic (convex: rational) and were checked against a skyline DP through `s = 30`.

| object | first terms (`s = 2…`) | GF | growth | status |
|---|---|---|---|---|
| all castles (bargraphs) | `1, 2, 5, 13, 35, 97, 275, 794, 2327` | `(1-2t-t²-√(1-4t+2t²+t⁴))/(2t)` | `τ² = 3.38298` (tribonacci squared) | **interlink** → [A082582](https://oeis.org/A082582) (bargraphs by semiperimeter; castle reading absent) |
| castles by `(s, w)` | rows `1; 1,1; 1,3,1; 1,5,6,1; …` | tower Narayana re-indexed | - | **interlink** → [A271942](https://oeis.org/A271942) (Narayana tower form absent) |
| even-block castles | `0, 1, 3, 7, 17, 47, 137, 400, 1168, 3450, 10338` | `(B + B_s)/2` | `τ²` | **novel-candidate** (no match, 2026-09-22) |
| signed castles `Σ(-1)^blocks` | `-1, 0, 1, 1, -1, -3, -1, 6, 9, -5, -29, -20, 55` | `(1+t²-√((1+t)(1-t+3t²+t³)))/(2t)` | `τ` (complex pair, modulus `1/τ`) | **novel-candidate** (signed, negated, and `\|·\|` no match, 2026-09-22) |
| convex castles | `1, 2, 5, 13, 34, 89, 233` | `t²(1-t)/(1-3t+t²)` | `φ²` | **known** → [A001519](https://oeis.org/A001519) (Delest-Viennot stacks by perimeter) |
| even-block convex castles | `0, 1, 3, 7, 17, 44, 116, 305, 799, 2091` | `t³(1-t)/((1-3t+t²)(1-t+t²))` | `φ²` | **novel-candidate** (no match, 2026-09-22) |
| signed convex castles | `-1, 0, 1, 1, 0, -1` (period 6) | `-t²(1-t)/(1-t+t²)` | periodic | trivial (not searched) |
| palindromic castles | `1, 2, 3, 5, 9, 15, 27, 46, 83` | symmetric-bargraph GF ([[deutsch-elizalde-2016-bargraphs-cornerless-motzkin](pages/deutsch-elizalde-2016-bargraphs-cornerless-motzkin.md)] §4.1) | - | **known** → [A273905](https://oeis.org/A273905) (symmetric bargraphs = palindromic castles; checked by brute force 2026-09-26) |
| prime castles (no height-1 column) | `0, 1, 2, 5, 13, 35, 97, 275, 794, 2327` | `t·B(t)` | `τ²` | **known** → [A082582](https://oeis.org/A082582)(`s − 1`) (row-deletion bijection, [[deutsch-elizalde-2016-bargraphs-cornerless-motzkin](pages/deutsch-elizalde-2016-bargraphs-cornerless-motzkin.md)] §3.9; checked 2026-09-26) |

### Prime castles by area

Castles glued at a shared height-1 column form a free monoid whose primes are the castles with no height-1 column ([[prime-castles](pages/prime-castles.md)]). A convex castle has at most one nontrivial prime ([[prime-convex-castles](pages/prime-convex-castles.md)]). Terms from `n = 2`.

| object | first terms | GF / formula | status |
|---|---|---|---|
| prime castles | `1, 1, 2, 3, 5, 8, 13, 21` | `q^2/(1-q-q^2)` | **known** → [A000045](https://oeis.org/A000045) (compositions into parts `≥ 2`) |
| prime convex castles `U` | `1, 1, 2, 3, 5, 8, 12, 19, 28, 42, 61, 90` | `Δ^2 A001523`; `sum_k q^k/((1-q^k)(q^2;q)_{k-2}^2)` | **novel-candidate** (no match, 2026-09-22) |
| non-convex prime castles `F_{n-1} - U` | `1, 2, 6, 13, 28, 54, 106, 194` (from `n = 8`) | | **novel-candidate** (no match, 2026-09-22) |
| `U` by width | rows `1; 1; 1,1; 1,2; 1,3,1; 1,4,3; 1,5,5,1` | convex castles of area `n-w`, width `w` | **novel-candidate** (no match, 2026-09-22) |
| convex castles, first column not 1 | `1, 2, 4, 7, 12, 20, 32, 51, 79` | `Δ A001523` | **interlink** → [A342528](https://oeis.org/A342528) (verified through area 120; neither entry cites the other) |
| castles per multiset of primes | `1, 2, 3, 5, 9, 15, 26, 45, 78` (from `n = 1`) | Euler transform of the prime counts | **novel-candidate** (no match, 2026-09-22), [[signed-prime-castles](pages/signed-prime-castles.md)] |
| prime parity splits (all and convex) | see the two pages | | **novel-candidate** (no match, 2026-09-22) |
| signed castles by area `even - odd` | `-1, 0, 0, 2, 0, 2, -4, 2, -12, 10, -20, 38` (from `n = 1`, 300 terms computed) | row-raising recursion; `~ C(-rho)^n` | **novel-candidate** (no match, 2026-09-22), [[castle-row-raising-equation](pages/castle-row-raising-equation.md)] |
| signed growth constant `rho` and prefactor `C` | `1.62382967400459...`, `0.09850917497311...` | pole at `q E(q,q) = 1`, the first zero of `M(q)` on [[castle-q-bessel-closed-form](pages/castle-q-bessel-closed-form.md)] | **novel-candidate** decimal expansions (no match, 2026-09-22) |
| second signed singularity `q_1` | `-0.82027198` | second zero of `M(q)`; correction `O(0.7508^n)` | **novel-candidate** (not searched), [[castle-q-bessel-closed-form](pages/castle-q-bessel-closed-form.md)] |
| castles by area and peaks | rows `1; 1,1; 1,3; 1,7; 1,14,1; 1,26,5` | `(1-q-q^2+tq^2)/(1-2q+q^3-tq^3)` | **novel-candidate** (no match, 2026-09-22) |
| one-peak castles | `1, 3, 7, 14, 26, 46, 79, 133` | `q^2/((1-q)^2(1-q-q^2))` | **interlink** → [A001924](https://oeis.org/A001924) (no composition reading on the entry) |

### Zoo sub-families of castles by area

The classical polyomino families intersected with the castles ([[castle-add-a-column-equation](pages/castle-add-a-column-equation.md)]): a monotone castle is a Ferrers or reverse-Ferrers skyline. Terms from `n = 1`, checked by enumerating compositions through `n = 20`.

| object | first terms | GF / formula | status |
|---|---|---|---|
| monotone castles (weakly increasing or weakly decreasing) | `1, 2, 4, 7, 12, 18, 28, 40, 57, 80, 110, 148` | `2p(n) - d(n)` | **interlink** → [A329398](https://oeis.org/A329398) (defined by Lyndon factorizations; the monotone reading and `2 A000041 - A000005` are a conjecture on the entry; agreement checked through `n = 20`) |
| non-monotone castles | `0, 0, 0, 1, 4, 14, 36, 88, 199, 432` | `2^(n-1) - 2p(n) + d(n)` | **known** → [A332834](https://oeis.org/A332834) (compositions neither weakly increasing nor weakly decreasing) |
| signed monotone castles `even - odd` | `-1, 0, 0, 1, 0, 2, 0, 2, -1, 4, -2, 4, -4, 6` | `2(-1)^n A000700(n) - sum_{d\|n} (-1)^d` | **novel-candidate** (signed, negated and `\|·\|` no match, 2026-09-23) |

### Odd count, parity-refined area, and joint block tables

The residue of the first mining pass, with full terms and the 2026-09-26 searches on [[odd-castles-and-block-tables](pages/odd-castles-and-block-tables.md)].

| object | first terms | GF / formula | status |
|---|---|---|---|
| `odd(w, h)` rows, `h = 3..7` | `h = 3`: `1, 5, 16, 44, 122, 358, 1082, 3274` | `(A + P(h-1,w) - P(h-2,w))/2`; order 5, 9, 11, 13, 15 | **novel-candidate** (no match, 2026-09-26) |
| `odd(4..6, h)`, `F(5, h)`, `F(6, h)` columns | `odd(4, h)`: `1, 5, 44, 58, 247, 223, 738, 564` | quasi-polynomial in `h` | **novel-candidate** (no match, 2026-09-26) |
| `even`, `odd`, `cev`, `cod`, `valley_even/odd`, `nc_even/odd`, `sv_even/odd` by area, and their signed differences | see the page | `cev + cod = A001523`, `valley_even + valley_odd = A332578`, `nc_even + nc_odd = A115981` | **novel-candidate** (no match, 2026-09-26) |
| castles by area and blocks, triangle | rows `1; 1,1; 1,2,1; 1,4,2,1; 1,6,6,2,1` | column `b` rational for `b <= 4` | **novel-candidate** (no match, 2026-09-26) |
| two-block castles by area | `1, 2, 4, 6, 9, 12, 16, 20, 25` | `q^2/((1-q)^2(1-q^2))` | **interlink** → [A002620](https://oeis.org/A002620) quarter-squares (`= A002620(n)`) |
| three-block one-peak castles by area | `1, 2, 5, 9, 16, 25, 39, 56, 80` | `q^3/((1-q)^2(1-q^2)^2(1-q^3))` | **interlink** → [A097701](https://oeis.org/A097701) (`= A097701(n-3)`, verified through area 40) |
| three-block two-peak castles by area | `1, 3, 8, 16, 30, 50, 80, 120, 175` | `q^5/((1-q)^3(1-q^2)^2)` | **interlink** → [A002624](https://oeis.org/A002624) (`= A002624(n-5)`, verified through area 40) |
| three-, four- and five-block columns; other blocks and peaks cells | see the page | rational | **novel-candidate** (no match, 2026-09-26) |
| `(w, h)` castles with `h + 1` blocks | `h = 3`: `3, 21, 84, 252, 630, 1386` | `(2h-3) C(w+2h-3, 2h)` | **interlink** → [A253943](https://oeis.org/A253943) at `h = 3` (`3 C(n+1, 6)`, `n = w + 2`); `h >= 4` **novel-candidate** |
| `(w, h)` block-count triangles `h = 3, 4`, and the `h + 2` column | `h = 3` rows `1; 5; 15,3,1; 35,21,9; 70,84,51,5,1` | first three columns in closed form | **novel-candidate** (no match, 2026-09-26) |

### Half-sum rows

The order-`1/2` fractional partial sum of `F(w, h)` in the width ([[half-sum-castles](pages/half-sum-castles.md)]), as the binomial half-sum `K_h(w) = sum_k C(2k, k) F(w - k, h)`, GF `G_h(x)/sqrt(1 - 4x)`. Terms from the first nonzero width.

| object | first terms | growth | status |
|---|---|---|---|
| `K_2` | `1, 5, 18, 60, 202, 702, 2508, 9136, 33742, 125934` | `4` | **novel-candidate** (no match, 2026-09-23) |
| `K_3` | `3, 27, 149, 671, 2755, 10833, 41679, 158465, 598681` | `4` | **novel-candidate** (no match, 2026-09-23) |
| `K_4` | `1, 9, 51, 241, 1069, 4671, 20353, 88383, 381583, 1635893` | `4`, `~ 4^w sqrt(w/pi)`; `pi = lim w 16^w / K_4(w)^2` | **novel-candidate** (no match, 2026-09-23) |
| `K_5` | `10, 142, 1210, 8222, 49806, 283570, 1557158, 8354490` | `5` | **novel-candidate** (no match, 2026-09-23) |
| dyadic half-sum `4^w H_h(w)`, `h = 2..5`, and the `H_2` numerators `1, 7, 63, 231, 3131, 10929` | see the page | `4h` | **novel-candidate** (no match, 2026-09-23) |

### Tree castles by area at fixed height

Tree castles (no `2 × 2` block) of height at most `h` for `h ≥ 3`, and of height 2 in the first row, counted by area `A` ([[tree-castle-by-area](pages/tree-castle-by-area.md)]). For `h ≥ 3` the count at area `A` is the number of compositions of `A + 1` into parts `{1, 3, 4, …, h + 1}`; at height 2 it is the compositions of `A + 1` into `{1, 3}` that use a 3. Terms from `A = 1`. The unlimited-height row is A005251, in the multi-interpretation hub above.

| object | first terms | GF / formula | status |
|---|---|---|---|
| height 2 | `0, 1, 2, 3, 5, 8, 12, 18, 27, 40` | parts `{1, 3}`, using a 3; `A000930(A+1) − 1` | **interlink** → [A077868](https://oeis.org/A077868) (`= A077868(A−2)`, `A ≥ 2`; brute force `A = 2..14`, 2026-10-04) |
| `h <= 3` | `1, 2, 4, 6, 9, 15, 25, 40, 64, 104` | parts `{1, 3, 4}` | **interlink** → [A006498](https://oeis.org/A006498) (`= A006498(A+1)`) |
| `h <= 4` | `1, 2, 4, 7, 11, 18, 31, 53, 89, 149` | parts `{1, 3, 4, 5}` | **interlink** → [A000570](https://oeis.org/A000570) tournaments determined by their score vectors (`= A000570(A+1)`) |
| `h <= 5` | `1, 2, 4, 7, 12, 20, 34, 59, 102, 175` | parts `{1, 3, …, 6}` | **interlink** → [A079816](https://oeis.org/A079816) (`= A079816(A+1)`, all 37 listed terms, 2026-09-26) |
| `h <= 6` | `1, 2, 4, 7, 12, 21, 36, 62, 108, 188` | parts `{1, 3, …, 7}` | **interlink** → [A189593](https://oeis.org/A189593) (`= A189593(A+1)`; the composition reading proves the entry's empirical recurrence) |
| `h <= 7` | `1, 2, 4, 7, 12, 21, 37, 64, 111, 194` | parts `{1, 3, …, 8}` | **interlink** → [A189600](https://oeis.org/A189600) (`= A189600(A+1)`) |
| `h <= 8` | `1, 2, 4, 7, 12, 21, 37, 65, 113, 197, 345, 604, 1056, 1846` | parts `{1, 3, …, 9}` | **novel-candidate** (no match, 2026-09-26) |

### Sandpile groups

The sandpile groups of every castle to 16 cells in both models, `K_sink` (one sink cell) and `K_tide` (the bottom row as the sink), mirror images removed ([[sandpile-census](pages/sandpile-census.md)]). Terms by cell count from `n = 1`.

| object | first terms | GF / formula | status |
|---|---|---|---|
| castles with trivial group (tree castles, both models) | `1, 2, 3, 5, 8, 13, 22, 37, 63, 108, 186, 322, 559, 973, 1697, 2964` | `(A005251(n+2) + A000931(n+6))/2` | **interlink** → [A005683](https://oeis.org/A005683) Twopins positions (agreement through `n = 26`, 2026-09-26) |
| palindromic tree castles | `1, 2, 2, 3, 4, 5, 7, 9, 12, 16, 21, 28, 37, 49, 65, 86` | `A000931(n+6)` | **interlink** → [A000931](https://oeis.org/A000931) Padovan (checked through `n = 16`) |
| castles with cyclic `K_sink` | `1, 2, 3, 6, 10, 20, 36, 72, 134, 264, 503, 997, 1933, 3791, 7338, 14329` | | **novel-candidate** (no match, 2026-09-26) |
| distinct groups `K_sink` among castles of `n` cells | `1, 1, 1, 2, 2, 3, 3, 4, 6, 8, 10, 13, 18, 25, 34, 48` | | **novel-candidate** (no match, 2026-09-26) |
| castles with cyclic `K_tide` | `1, 2, 3, 6, 10, 20, 36, 72, 135, 268, 513, 1015, 1975, 3902, 7631, 15028` | | **novel-candidate** (no match, 2026-09-26) |
| distinct groups `K_tide` among castles of `n` cells | `1, 1, 1, 2, 2, 4, 4, 7, 9, 14, 18, 27, 38, 56, 78, 113` | | **novel-candidate** (no match, 2026-09-26) |
| `|K_sink|` of the 2-wide ladder, lying down `(2, …, 2)` by width or standing up `(h, h)` by height | `1, 4, 15, 56, 209, 780` | `a(n) = 4a(n−1) − a(n−2)`, cyclic | **known** → [A001353](https://oeis.org/A001353) (spanning trees of the `2 × n` grid) |
| `|K_tide|` of the 2-wide ladder lying down `(2, …, 2)` by width | `1, 3, 8, 21, 55, 144` | `a(n) = 3a(n−1) − a(n−2)`, cyclic | **interlink** → [A001906](https://oeis.org/A001906) `F(2n)` (`= A001906(w)`; every block on the ground) |
| `|K_tide|` of the 2-wide ladder standing up `(h, h)` by height | `1, 3, 11, 41, 153, 571` | `a(n) = 4a(n−1) − a(n−2)`, cyclic | **interlink** → [A001835](https://oeis.org/A001835) (`= A001835(h)`; one block on the ground) |

### Fibonacci castle sub-families

Fibonacci castles cut out by a rule on the tower, counted as castles of width `w` and exact height 2, terms from `w = 1` ([[fibonacci-castles-sub-families](pages/fibonacci-castles-sub-families.md)]).

| object | first terms | GF / formula | status |
|---|---|---|---|
| Fibonacci-word castles (tower a factor of the Fibonacci word) | `1, 2, 4, 5, 6, 7, 8, 9` | `w + 1` for `w ≥ 3` (Sturmian complexity) | **known** (linear; no entry needed) |
| balanced castles | `1, 2, 4, 7, 12, 18, 27, 38, 52, 68, 89, 112` | `A005598(w)/2`, `~ w³/(2π²)` | **interlink** → [A049703](https://oeis.org/A049703) (`= A049703(w)`; the entry is defined only as `A005598(n)/2`, no combinatorial reading; brute force `w ≤ 15`, 2026-10-04) |
| maximal castles (no column can be raised) | `1, 2, 2, 3, 4, 5, 7, 9, 12, 16, 21, 28` | `x(1+x)^2/(1-x^2-x^3)` | **known** → [A000931](https://oeis.org/A000931) (`= A000931(w+6)`; the entry lists maximal independent vertex sets of the path graph) |
| spaced castles (height-2 columns ≥ 3 apart) | `1, 2, 3, 5, 8, 12, 18, 27, 40, 59` | `A000930(w+2) - 1` | **known** → [A077868](https://oeis.org/A077868) (`= A077868(w-1)`); the bijection with Fibonacci castles of `w + 1` cells is on the page |
| `(1, 3)`-RLL castles (MFM constraint) | `1, 2, 4, 7, 10, 15, 22, 32, 47, 69` | `x(1+x+x^2+x^3)^2/(1-x^2-x^3-x^4)` | **unchecked** |
| `(1, 7)`, `(2, 7)`, `(2, 10)`-RLL castles | see the page | gap generating function | **unchecked** |

### Other generation candidates

Further candidates with their current status; several are **unchecked**.

- `F(w, 3)`: even-block castles of height exactly 3, `0, 0, 3, 21, 89, 307, 977, 3031, …` ([[new-sequence-fw3](pages/new-sequence-fw3.md)]) — **novel-candidate** (no OEIS match, searched 2026-09-19).
- `F(w, 4…6)`: the taller rows ([[new-sequence-fw3](pages/new-sequence-fw3.md)]) — **unchecked**.
- Fixed-width columns ([[sum-of-three-cubes-castles](pages/sum-of-three-cubes-castles.md)]): `F(3, 2m) = 10m^2 - 5m + 1 = 5·Hex(m) + 1`, `6, 31, 76, 141, 226, 331, 456, 601, 766, 951, …` — **novel-candidate** (no OEIS match by terms or formula, searched 2026-09-20; it is A080860 at negative index). `odd(3, 2n+1) = 10n^2 + 5n + 1`, `1, 16, 51, 106, 181, 276, …` — **interlink** → [A080860](https://oeis.org/A080860) (exact, offset 0). `F(3, 2m+1) = odd(3, 2m) = C(2m+1, 2)` and `C(2m, 2)` — **known**, triangular numbers A000217. The interleaved columns `F(3,h)` (`6, 3, 31, 10, 76, 21, …`), `odd(3,h)`, and `F(4,h)` (`10, 21, 117, 122, 448, 367, 1131, 820, …`) — **novel-candidate** (searched 2026-09-20, no match); `F(4,h)` is the quasi-polynomial `(4h-3)(4h^2-3h+2)/6` at even `h`, `(h-1)(8h^2-4h+3)/6` at odd `h`.
- `|P(k, L)|` in the *k*-direction at fixed `L ≥ 5` ([[castle-eigenvalue-oeis-crosswalk](pages/castle-eigenvalue-oeis-crosswalk.md)]) — **unchecked**. *(The L-direction rows `P(k,·)`, `k = 2..6`, are in the "Signed tower count P(k,·) rows" section above.)*
- Parity-refined area sequences (even/odd, convex, valley, non-convex, `strict_valley`) ([[castle-by-area](pages/castle-by-area.md)]) — **novel-candidate**, searched 2026-09-26; terms in the section above.
- Higher tower rows `w ≥ 6` in the Narayana table ([[tower-narayana-polynomial](pages/tower-narayana-polynomial.md)]) — **unchecked**.
- Jacobi-Perron convergent denominators of `2ψ²` ([[castle-eigenvalue-oeis-crosswalk](pages/castle-eigenvalue-oeis-crosswalk.md)]) — **unchecked**.

## Appearances in Sources

- [[oeis-mining-pe502](pages/oeis-mining-pe502.md)] - the source workspace where the mining passes were carried out; the interlink candidates in the submission list trace back to veins there.

## Related Concepts

- [[oeis-index](pages/oeis-index.md)] - the script-generated A-number directory: every OEIS number cited on the wiki, grouped by role, with citing pages and mention counts.
- [[oeis-cross-referencing](pages/oeis-cross-referencing.md)] - the method: verify against OEIS data with offsets, distinguish interlinking from generation, honor the human-authorship rule.
- [[oeis-height2-hyperbolic-castles](pages/oeis-height2-hyperbolic-castles.md)] - the height-2 interlink.
- [[hyperbolic-sequence-family](pages/hyperbolic-sequence-family.md)] - the A038503 / A038504 / A038505 / A000749 family collectively.
- [[metallic-means](pages/metallic-means.md)] / [[pell-numbers](pages/pell-numbers.md)] / [[plastic-number](pages/plastic-number.md)] - the number-family threads whose OEIS sequences populate this catalogue.
- [[castle-graph](pages/castle-graph.md)] - the tree-castle counts on Fibonacci / Jacobsthal / k-Fibonacci.
- [[castle-eigenvalue-oeis-crosswalk](pages/castle-eigenvalue-oeis-crosswalk.md)] - the metallic-mean convergent tables.
- [[hardin-word-identity](pages/hardin-word-identity.md)] - the Hardin sequences A202882 / A203094 / A203184 and their proved recurrences.
- [[new-sequence-fw3](pages/new-sequence-fw3.md)] - the `F(w,3)` generation candidate.
- [[exact-height-castle-by-area](pages/exact-height-castle-by-area.md)] - the n-nacci-by-area interlinks (A000073 / A000078 / A001591).
- [[tower-spacing-castles](pages/tower-spacing-castles.md)] - the tower-spacing family whose g=2 column is the Hardin sequences and g=3 the "min of 3 adjacent" family.
- [[proper-castle-projection](pages/proper-castle-projection.md)] - the even-block proper-castle rows, the novel-candidate entries.
- [[reachable-field-census](pages/reachable-field-census.md)] - the strip Perron-root sequences, mostly unchecked against OEIS.
- [[odd-castles-and-block-tables](pages/odd-castles-and-block-tables.md)] - the odd-count rows, the dated parity-area searches, and the area / blocks / peaks and `(w, h)` / blocks tables.
- [[a005251-bijection](pages/a005251-bijection.md)] - the explicit bijection relating A005251's castle readings.
- [[oeis-mining-seminar](pages/oeis-mining-seminar.md)] - the seminar that walks one catalogue row through the whole method.
- [[motzkin-castles](pages/motzkin-castles.md)] - the Motzkin-family rows: cornerless Motzkin paths, the parity split of `M_{w−1}`, the bounded-height Motzkin ladder, and the semi-perimeter relatives.
