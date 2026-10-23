# Castles wiki — OEIS open threads & TODO

A running tracker of pending human actions (OEIS submissions, ingestion queue,
housekeeping) for the PE 502 castles wiki. This is a **hand-maintained** file (not a
generated artifact and not a wiki page — it lives at the repo root, outside
`wiki/pages/`, so it does not appear in the index).

Research and seminar ideas live in `IDEAS.md`; this file holds the human-action and
pipeline checklists.

Convention: `[ ]` open · `[~]` in progress · `[x]` done. Link wiki pages as
`wiki/pages/<slug>.md`.

---

## OEIS submissions (human action — drafts in `raw/oeis-pe502/`)

OEIS allows **3 open edits at a time**, and each takes a while to review, so the queue runs
as a pipeline: when a review slot opens, submit the top item of "Ready to submit". Keep stages 2-4 stocked while waiting. Signatures use a
two-digit day (`Oct 04 2026`). A tool may run the verification scripts, check offsets against the live entries and format data; only a person rewrites the draft prose, signs it and submits (`raw/oeis-pe502/SUBMISSION-NOTES.md` §4). See `wiki/pages/oeis-cross-referencing.md`; the
OEIS status of each castle sequence (known / interlink / novel-candidate / unchecked) is
kept here, in section 5; the wiki's `castle-sequence-catalogue` lists the sequences and the
entries they equal, with no status.

### 1. In review (max 3)

- [~] **A160747 castles of width 5 and 6-cores** (submitted 2026-10-16). One comment block:
  `a(n)` = 6-core partitions with `n` corners (Cho, Huh, Nam, and Sohn, arXiv:2205.15554,
  Prop. 3.4, already linked) = castles of width 5 with `n + 1` blocks, of any height, with the
  abacus bijection (their Theorem 3.3). One formula block: the g.f. numerator is row 5 of
  A001263, their Prop. 3.4 sum, `a(n) = A271942(n+6, 5)`. The PE 502 link and two new Cf.
  lines (A001263, A271942; the t-core family A005408 / A005891 / A063490):
  `raw/oeis-pe502/xrefs/A160747-tower.md`, checked by `bin/python/tower_t_cores.py`
  (`wiki/pages/tower-narayana-polynomial.md`).
- [~] **A063490 castles of width 4 and 5-cores** (submitted 2026-10-16), the A160747 form at
  `t = 5`; offset 1 needs no shift: `a(n)` = castles of width 4 with `n` blocks = 5-cores with
  `n − 1` corners. Formula block: the numerator `x(1 + 6x + 6x^2 + x^3)` (row 4 of A001263),
  Cho et al.'s Prop. 3.4 sum, `a(n) = A271942(n+4, 4)`. The PE 502 link, `Cf. A001263, A064788,
  A185505, A271942.` (extends the existing line) and the t-core family line:
  `raw/oeis-pe502/xrefs/A063490-tower.md`, checked by `bin/python/tower_t_cores.py`.
- [~] **A005891 castles of width 3 and 4-cores** (submitted 2026-10-21), the A160747 form at
  `t = 4`: `a(n)` = 4-cores with `n` corners = castles of width 3 with `n + 1` blocks.
  Formula block: Cho et al.'s Prop. 3.4 sum and `a(n) = A271942(n+4, 3)`, with no
  Narayana-numerator line, since the entry's "triangular numbers convolved with
  [1, 3, 1, 0, 0, 0, ...]" comment (Adamson and Povolotsky, May 29 2009) already states it.
  The Cho et al. and PE 502 links, `A001263, A271942` added to the first Cf. line, and the
  t-core family line: `raw/oeis-pe502/xrefs/A005891-tower.md`, checked by
  `bin/python/tower_t_cores.py`.

### 2. Ready to submit (drafted and checked, in order)

1. [ ] **A001263, castles by blocks for every width** (formerly tier 2), in the A160747 form
   (castle wording, PE 502 link, Cho et al.): castles of width `n` with `m` blocks number
   `Sum_k T(n,k) C(m+n-k-1, n-1)`, for every `n`, proved: `x -> x/(1-y)` in the g.f. of
   A001263 gives Deutsch-Elizalde's bargraph equation (2) (arXiv:1609.00088)
   (`raw/oeis-pe502/xrefs/A001263-tower.md`; `wiki/pages/tower-narayana-polynomial.md`).
2. [ ] **Dense-entry synonyms** (formerly tier 3) A001523 / A332578 / A115981
   (`raw/oeis-pe502/xrefs/*-castle.md`).
3. [ ] **The PE 502 count `F(w,h)` as an array, then its rows and columns** (OEIS rolls a
   two-parameter family into one array entry, with notable rows and columns as their own
   entries, cf. A217883 "Column 2 is A202882(n+1)"). In order:
   1. [ ] **Array `F(w,h)`**: even-block castles of width `w` and exact height `h`, square
      array read by antidiagonals (keyword `tabl`), with the general formula
      `F(w,h) = ½[h^w − (h−1)^w + P(h−2,w) − P(h−1,w)]`, the PE 502 link, the table in the
      Example section, and Cf. the all-parity array A047969 (`h^w − (h−1)^w`; A343237 is its
      transpose) and row 2 = A038505(w+1). Not on OEIS in either antidiagonal order (searched
      2026-10-04). **Draft not written.**
   2. [ ] **Row `h = 3`, `F(w,3)`** (`raw/oeis-pe502/new-sequence-F3.md`, crossrefs updated to
      point at the array; `wiki/pages/new-sequence-fw3.md`). No match (re-searched 2026-10-04).
   3. [ ] **Column `w = 3`, `F(3,h)`** = `0, 6, 3, 31, 10, 76, 21, 141, 36, 226, …`: `C(h,2)` at
      odd `h`, `5·C(h,2) + 1` at even `h` (`wiki/pages/sum-of-three-cubes-castles.md`). No match
      (searched 2026-10-04). **Draft not written.** The halves and the odd-block column, for
      the draft: the odd half is `F(3, 2m+1) = A014105(m)` (second hexagonal numbers); the
      even half is `F(3,2m) = 10m^2 − 5m + 1` (`6, 31, 76, 141, …`, no match 2026-09-20); and
      `odd(3, 2n+1) = A080860(n)` (`10n^2 + 5n + 1`), an interlink.
4. [ ] **A003410 castle comment** (optional edit 2 of the A226136 draft, lower priority): for
   `n >= 4`, `a(n)` = castles of width `n` and height 2 with no two adjacent columns at height
   2 and every run of height-1 columns of length at most 3 (the `(1,3)`-RLL Fibonacci
   castles): `raw/oeis-pe502/xrefs/A226136-A003410.md` §"Edit 2"
   (`wiki/pages/fibonacci-castles-sub-families.md`).

### 3. Needs a draft (verified, worth submitting; in submission order)

1. [ ] **A283595** (Motzkin prefixes of length `n` and height `k`; the entry has no formula
   section): castle comment, `T(n,k)` = castles of width `n+1` and exact height `k+1` whose
   first column is at height 1 and whose neighbouring columns differ by at most 1 (column 2
   is the Pell castles, A094706). Formula line: the g.f. of column `k` is
   `z^k/(R_k(z) R_{k+1}(z))` with `R_{2j} = P_j − z P_{j−1}` and
   `R_{2j+1} = P_{j+1} − z^2 P_{j−1}`, where `P_k` are the polynomials of A097862
   (`P_{−1} = 0`; the entry's own notation, not the Pell numbers). Proved on the wiki (only odd
   eigenvalue indices survive; the numerator is a single power of `z`), and checked against the
   entry's rows 0-8 and as an identity for `k ≤ 11` (2026-10-06). Finch, arXiv:1802.04615
   (linked from the entry), checked 2026-10-07: it works with ±1 walks and only refers to
   A283595 for the Motzkin-prefix counts, so there is no column g.f. to cite. Present the
   formula without a novelty claim; bounded-height path g.f.s are classical
   (`wiki/pages/1-smooth-castles.md` §3.2-3.3, §3.5). Two more formula lines (2026-10-22):
   the column g.f. is also `z^k/(R_{2k+2}(z) + z^{k+1})`, since `R_{k+1} R_k = R_{2k+2} + z^{k+1}`
   (§3.3, a product-to-sum identity for the Chebyshev polynomials of the first and third kinds);
   and for `k ≤ n ≤ 2k`, `T(n,k) = A027907(n,n+k) + A027907(n,n+k+1) − A027907(n,n+k+2)
   − A027907(n,n+k+3)`, by the reflection principle with only one reflection in the ceiling
   (§3.7), checked against the castle counts that match the b-file for `k ≤ 11`, `n ≤ 22`.
   - The diagonal **A283667** (`T(2n,n)`, Motzkin prefixes of length `2n` and height `n`) has
     only a recursion and an asymptotic; the second line gives
     `a(n) = A027907(2n,3n) + A027907(2n,3n+1) − A027907(2n,3n+2) − A027907(2n,3n+3)`,
     checked against all 24 terms of its data (2026-10-22). Submit with the A283595 edit.
2. [ ] **A094706** (Convolution of Pell(n) and 2^n; the entry has no comments): the Pell
   castles (exact height 3, first column 1, neighbouring columns differing by at most 1) of
   width `w` number `A094706(w − 2) = P⋆_w − 2^{w−1}` (`P⋆_w` the Pell numbers), proved by
   the g.f. `x³/((1−2x−x²)(1−2x))` (`wiki/pages/pell-castle.md`). Add the formula
   `a(n) = A283595(n+1, 2)` (column 2 of the Motzkin-prefix triangle: lowering a Pell castle
   by one row gives a Motzkin prefix of height 2) and `Cf. A283595`; pairs with the A283595
   item above (`wiki/pages/1-smooth-castles.md`).
3. [ ] **A077868**: two castle readings and the bijection between them. Spaced Fibonacci
   castles (height-2 columns at least 3 apart) of width `w` number `A077868(w − 1)`; tree
   castles of height 2 with area `A` (cells) number `A077868(A − 2)`; the domino-boundary map
   matches the Fibonacci castles with `w + 1` cells to the spaced castles of width `w`.
   Brute-force verified 2026-10-04
   (`wiki/pages/fibonacci-castles-sub-families.md`, `wiki/pages/tree-castle-by-area.md`).
4. [ ] **A000071**: the Fibonacci castles of width `w` number `F_{w+2} − 1`, the term
   `A000071(w+2)`; castles of height 2 with area `A` number `F_{A+1} − 1`, the term
   `A000071(A+1)`. Brute-force verified 2026-10-04
   (`wiki/pages/fibonacci-castle.md`, `wiki/pages/castle-graph.md`).
5. [ ] **A049703**: balanced Fibonacci castles of width `w` number `A005598(w)/2 = A049703(w)`
   (towers balanced, i.e. finite Sturmian); the entry is defined only as `A005598(n)/2`, with
   no combinatorial reading. Brute-force verified `w ≤ 15`, 2026-10-04
   (`wiki/pages/fibonacci-castles-sub-families.md`).
6. [ ] **A106514**: the 1-smooth castles of exact height 3 (free first column) of width `w`
   number `A106514(w − 1)`, g.f. `x(1−x)/((1−2x)(1−2x−x²))`, proved; the entry has
   only convolution and eigensequence comments (`wiki/pages/pell-castle.md`).
7. [ ] **A047969 castle comment** (replaces per-row comments on the dense rows A000225,
   A001047, …): the nexus-number array `a(n,k) = (n+1)^(k+1) − n^(k+1)` counts the castles
   of width `k+1` and exact height `n+1`, `h^w − (h−1)^w` with `h = n+1`, `w = k+1`. The
   stage-2 `F(w,h)` array item already gives `Cf. A047969`.
8. [ ] **Tower-spacing new sequences** (`wiki/pages/tower-spacing-castles.md`): the six
   unfiled cells `(h,g)` for `h in {5,6}`, `g in {4,5,6}` (Hardin's "0..(h-1) arrays, each
   element the minimum of `g` adjacent elements", never filed at these parameters; no match
   2026-09-20).
9. [ ] **Tower-spacing table comments**: one comment each on the tables A217883 / A217954 /
   A228461 giving the castle reading and the running-minimum proof. The nineteen matched
   cells are covered by the tables, so no per-cell comments
   (`wiki/pages/tower-spacing-castles.md`).

### 4. Candidates (found on the wiki, not yet assessed)

Each gets a verdict: submit (move to stage 3) or skip (move to "Skipped", with the reason).

- [ ] **Castles that never drop by two, by semi-perimeter** (moved from IDEAS.md): `1, 2, 5, 12, 29, 71, 175, 434, 1082, 2709, 6807, 17157, …`
  (columns never more than one lower than the column before, any ends) is absent from OEIS (searched 2026-09-27) and has two
  readings joined by a verified bijection: valleyless Motzkin meanders of length `s − 2`, which Prodinger prints as "not in" OEIS
  (`wiki/pages/motzkin-castles.md` §6-7). Draft package in `raw/oeis-pe502/`: terms to 30+, GF from the kernel solution, both
  readings, A004148 (the returning sub-count) as cross-reference. Strongest novel candidate of the Motzkin thread.
- [ ] **Tree castles by area, `h ≥ 8`** (moved from IDEAS.md): `wiki/pages/tree-castle-by-area.md` identifies `h = 5, 6, 7` as
  interlinks; `h = 8` has no match (searched 2026-09-26) and is a new-sequence candidate with the GF
  `(1 + P_h(q))/(1 − q − q·P_h(q))`, `P_h(q) = q² + ⋯ + q^h`.
- [ ] **New-sequence candidates**, each only if it brings its own formula
  (`wiki/pages/castle-sequence-catalogue.md`, "Other generation candidates"):
  - **The `F(w,h)` array:** rows `F(w,4)`, `F(w,5)`, `F(w,6)`; the odd-block rows
    `odd(w,3)`, `odd(w,4)` and `odd(w,h≥3)` generally; the column `F(4,h)` (`0, 10, 21,
    117, 122, 448, …`); further rows and columns. Searched rows and columns: no match
    2026-10-04. The `w = 3` column facts are under stage 2.
  - **Area:** the parity-refined area sequences (`cev+cod = A001523`), `strict_valley`.
  - **Towers and signed counts:** tower rows `w ≥ 6` (`w = 6, 7`: no match 2026-10-04); the
    `P(k,·)` families for `k ≥ 2`; `|P(k,5)|`, `|P(k,6)|`, the `k`-direction rows (no match
    2026-10-04).
  - **Fibonacci sub-families:** the `(1,7)`, `(2,7)`, `(2,10)`-RLL Fibonacci castle counts;
    the Jacobi-Perron denominators of `2ψ²` (no match 2026-10-04).
  - **Pell, 1-smooth and m-smooth** (`wiki/pages/1-smooth-castles.md`,
    `wiki/pages/m-smooth-castles.md`):
    - the Pell castle rows (even-block, odd-block, signed; no match 2026-10-04), which are
      column 2 of the A283595 parity triangles below;
    - the both-ends-at-height-1 Pell row `0, 0, 0, 0, 1, 5, 18, 56, …`, column 2 of A097862
      (not a standalone entry): only as a column entry with its own formula,
      `x⁵/((1−x)(1−2x)(1−2x−x²))`; its value at width `w` is `S(w − 4)`, where `S` is the
      running sum of A094706;
    - column 3 of A283595, the 1-smooth castles of exact height 4 with first column at
      height 1: `1, 5, 19, 64, 202, 612, …` from width 4, `= F_{2w−1} − P⋆_w`, g.f.
      `x⁴/((1−3x+x²)(1−2x−x²))`; no standalone match 2026-10-06. If A283595 gets its
      column g.f., a column entry may be redundant;
    - the PE 502 parity split of A283595 as two triangles (even-block, odd-block); no match
      2026-10-06; messy recurrences (order 11 at height 4);
    - the free-first-column 1-smooth castles of exact height 4: `1, 3, 9, 27, 79, 227, 643, …`;
      no match 2026-10-06;
    - the m-smooth diagonal castles `h = m + 2`, g.f.
      `m x³/((1−(m+1)x−m x²)(1−(m+1)x))` (`m = 1` gives `A094706(w − 2)`): the `m = 2` row
      `2, 12, 58, 252, 1034, …` from width 3 has no match (2026-10-06); `m = 3, 4` not
      searched;
    - the 2-smooth triangle by `(w, h)` (`1; 1, 1, 1; 1, 3, 5, 2, 1; 1, 7, 19, 12, 8, 3, 1;
      …`); no match 2026-10-06.
- [ ] **A014105** (second hexagonal numbers `n(2n+1)`): the odd half of the `F(3,h)` column,
  `F(3, 2m+1) = A014105(m)` (verified `m ≤ 11`, 2026-10-04), now also stated under the
  stage-2 `w = 3` column item. Open question: a separate comment on this dense entry, or
  only the column entry.
- [ ] **A004148** (generalized Catalan numbers; peakless Motzkin paths, RNA secondary
  structures): castle comment, the castles that drop by at most 1 and end at height 1, by
  semi-perimeter `s`, number `A004148(s − 1)` (`1, 1, 2, 4, 8, 17, 37, 82, 185, 423, 978`
  from `s = 2`; matched over 21 terms, 2026-09-26). Their mirror images are the bargraphs
  with no double rise, which Deutsch and Elizalde map bijectively to RNA secondary
  structures. Open question: whether the entry already carries the Deutsch-Elizalde
  bargraph reading, which would make the castle comment a restatement
  (`wiki/pages/motzkin-castles.md`,
  `wiki/pages/deutsch-elizalde-2016-bargraphs-cornerless-motzkin.md`).

**Skipped (assessed, with reason):**

- A000129 / A001333 / A171842 (the Pell castle strip under its three boundary conditions):
  dense entries, and a strip need not reach its ceiling, so it is not a castle family; the
  castle readings go on A094706, A106514 and A283595 (the castles of exact height 3). A171842
  already has the equivalent "Motzkin n-paths of height <= 2" reading.
- A001519 / A057960 / A085810 (anchored 1-smooth strips with ceilings 4, 5, 6) and A007482 /
  A015530 / A015537 (anchored m-smooth strips on the diagonal `h = m + 2`, `m = 2, 3, 4`):
  strips, not castle families, for the same reason; A057960 and A085810 already carry the
  equivalent corridor-path reading, and A001519 is dense. The castle readings go on A283595
  and the diagonal castle rows.
- A097862 castle comment (both end columns at height 1, neighbouring columns differing by at
  most 1): the entry already states the column g.f. `z^(2k)/[P_k*P_{k+1}]`, whose `P_k` are
  the 1-smooth determinants, and the castle reading is the Motzkin path raised one row.
- A000225 / A001047 / … (`h^w − (h−1)^w`, all castles of exact height `h`, one row per `h`):
  dense entries; the castle reading goes once on the array A047969 (stage 3).
- The plastic strip (rule `1→3, 2→1, 3→{1,2}`): its count is `A000931(w + 9)`, Padovan,
  which the entry already covers with word and automaton readings (Finch's `(1,2)`-RLL
  words, Deutsch's compositions into 2s and 3s). Draft written anyway, recommending skip:
  `raw/oeis-pe502/xrefs/A000931-plastic-strip.md`.
- A000931 (maximal Fibonacci castles, `A000931(w + 6)`): the entry already counts the maximal
  independent sets of the path graph, which is the same statement.
- The signed convex castles (period 6) and the digits of `q_1` (no match): nothing to submit.
- A000930 (spaced castles, `A000930(w + 2) − 1`): the entry already has the "at least two
  zeros between successive ones" comment; A077868 is the better home.
- A003849 / A001950 / A003622 (the 56-column castle from the Fibonacci word): a single castle,
  not a sequence interpretation.
- A005408 (castles of width 2, 3-cores): dense core entry, marginal reading; the draft is in
  castle form in case it is wanted: `raw/oeis-pe502/xrefs/A005408-tower.md`.

### 5. Search record (statuses of the castle sequences on the wiki)

The OEIS status of each castle sequence on `wiki/pages/castle-sequence-catalogue.md`, as last recorded: searches with no match (with their dates), near-misses, unsearched rows, and the entries that equal a castle count without stating the castle reading. The catalogue section is given for each row; its terms and formulas are on the catalogue page.

#### Searched with no match, near-misses, unsearched

| catalogue section | object | first terms | status as recorded |
|---|---|---|---|
| Tower-spacing skylines | `(h=5, g=4)` | `5, 25, 95, 295, 791, 1927, 4496, 10606` | **novel-candidate** (no match, 2026-10-16; order 17) |
| Tower-spacing skylines | `(h=5, g=5)` | `5, 25, 95, 295, 791, 1897, 4196, 8848` | **novel-candidate** (no match, 2026-10-16; order 21) |
| Tower-spacing skylines | `(h=5, g=6)` | `5, 25, 95, 295, 791, 1897, 4166, 8548` | **novel-candidate** (no match, 2026-10-16; order 25) |
| Tower-spacing skylines | `(h=6, g=4)` | `6, 36, 161, 581, 1792, 4955, 12889, 33279` | **novel-candidate** (no match, 2026-10-16; order 21) |
| Tower-spacing skylines | `(h=6, g=5)` | `6, 36, 161, 581, 1792, 4900, 12229, 28681` | **novel-candidate** (no match, 2026-10-16; order 26) |
| Tower-spacing skylines | `(h=6, g=6)` | `6, 36, 161, 581, 1792, 4900, 12174, 28021` | **novel-candidate** (no match, 2026-10-16; order 31) |
| The Pell castle strip: 1-smooth strips on {1, 2, 3} | **Pell castles**: first column at height 1, height 3 | `0, 0, 1, 4, 13, 38, 105, 280, 729` | **interlink** → [A094706](https://oeis.org/A094706) (`= A094706(w−2) = P⋆_w − 2^{w−1}`, g.f. `x³/((1−2x−x²)(1−2x))`, proved; the entry has no castle reading, 2026-10-16) and column 2 of [A283595](https://oeis.org/A283595) (Motzkin prefixes by height, row `w − 1`); [[pell-castle](pages/pell-castle.md)] |
| The Pell castle strip: 1-smooth strips on {1, 2, 3} | both end columns at height 1, height 3 | `0, 0, 0, 0, 1, 5, 18, 56, 161, 441` | **interlink** → column 2 of [A097862](https://oeis.org/A097862) (Motzkin paths by height, row `w − 1`; g.f. `x⁵/((1−x)(1−2x)(1−2x−x²))`, the partial sums of the Pell castles shifted by 2; no match as a sequence of its own, 2026-10-16) |
| The Pell castle strip: 1-smooth strips on {1, 2, 3} | even-block / odd-block Pell castles | `0, 0, 0, 0, 2, 13, 51, 154, …` / `0, 0, 1, 4, 11, 25, 54, 126, …` | **novel-candidate** (order 8 each; no match, 2026-10-16), [[pell-castle](pages/pell-castle.md)] |
| The Pell castle strip: 1-smooth strips on {1, 2, 3} | signed Pell castles (even − odd) | `0, 0, −1, −4, −9, −12, −3, 28, 71, 72, …` | **novel-candidate** (denominator `(1−x)(1−2x+2x²)(1−2x+3x²)`; no match, 2026-10-16) |
| 1-smooth castles of height h | `smooth(w, h)`, first column at height 1, height `h` | `h = 4`: `0, 0, 0, 1, 5, 19, 64, 202, 612`; one row per `h` on the concept page | **interlink** → column `h − 1` of [A283595](https://oeis.org/A283595) (Motzkin prefixes by height, row `w − 1`; checked for `h ≤ 7`, `w ≤ 14`). As a sequence of its own, the row `h = 4` agrees with [A378383](https://oeis.org/A378383) for `w ≤ 10` and differs at `w = 11` (5205 against 5206), so it has no match (2026-10-16); the row `h = 2` is [A000225](https://oeis.org/A000225)(`w − 1`); the row `h = 6` agrees with [A122611](https://oeis.org/A122611), the expansion of `1/η_12`, for `w = 6, …, 11` and differs at `w = 12` (6038 against 6039), because the g.f. is `x^h/(η_{2h} + x^h)`; the rows `h = 5…12` have no match (2026-10-22) |
| 1-smooth castles of height h | `strips(w, h)`, `h = 7…12` | `h = 7`: `1, 2, 5, 13, 35, 96, 267, 749, 2113, 5982` | **novel-candidate** (no match for `h = 7…12`, 2026-10-22); each agrees with [A005773](https://oeis.org/A005773) exactly for `w ≤ h` |
| 1-smooth castles of height h | even-block / odd-block, `h = 4` | `1, 5, 16, 42, 106, 287, 843, 2535` / `0, 0, 3, 22, 96, 325, 960, 2670` (from `w = 4`) | **novel-candidate** (order 11 each; no match, 2026-10-16) |
| 1-smooth castles of height h | even-block / odd-block / signed, `h = 5…12` | on the concept page | **novel-candidate** (no match for any of the 24 rows, nor for `h = 3, 4`, 2026-10-22); orders and signed growth for every `h` on the concept page |
| 1-smooth castles of height h | any first column, height `h = 4…12` | `h = 4`: `1, 3, 9, 27, 79, 227, 643, 1801, 4999` | **interlink** → [A188866](https://oeis.org/A188866)`(h − 1, w) − A188866(h − 2, w)`, the difference of two rows of the smooth-word table; as sequences of their own no match for `h = 4…12` (2026-10-22) |
| 1-smooth castles of height h | last column within 1 of the first (cyclic), height `h` | `A002426(w)` for `w ≤ 2h − 1`; `h = 3` from `w = 6`: `135, 351, 899, 2275, 5703` | **interlink** → [A002426](https://oeis.org/A002426)(`w`) for `w ≤ 2h − 1` (central trinomial coefficients); the rows `h = 3, 4` have no match from `w = 2h` on (2026-10-22) |
| m-smooth castles of height h | castles, `m = 2`, height 4 | `0, 0, 2, 12, 58, 252, 1034, 4092, 15802` | **novel-candidate** (g.f. `2x³/((1−3x−2x²)(1−3x))`; no match, 2026-10-16) |
| m-smooth castles of height h | castles, `m = 2`, triangle by `(w, h)` | `1; 1, 1, 1; 1, 3, 5, 2, 1; 1, 7, 19, 12, 8, 3, 1; …` | **novel-candidate** (no match, 2026-10-16) |
| m-smooth castles of height h | strips, `m = 2`, `h = 5` | `1, 3, 12, 47, 185, 728, 2865, 11275` | **interlink** → [A088132](https://oeis.org/A088132)(`w − 1`) (g.f. `(1 − x)/(1 − 4x + x³)`; the entry has no walk reading, 2026-10-22) |
| m-smooth castles of height h | castles of height `h ≥ m + 2`, other rows; their parity splits; rows with free and pinned ends | on the concept page | **novel-candidate** (no match for the `m = 2` castle rows `h = 4…12`, the `m = 2` parity rows at `h = 4`, the `m = 2` free and pinned rows at `h = 4, 5`, and the first rows at `m = 3, 4`, 2026-10-22) |
| Motzkin castles | even-block Motzkin-path castles | `0, 0, 1, 3, 6, 10, 20, 56, 168, 456, 1137, 2827` | **interlink** → [A343386](https://oeis.org/A343386) (`= A343386(w−1)`, odd Motzkin paths; no castle reading, 2026-10-16) |
| Motzkin castles | drops of at most 1, any ends, by semi-perimeter | `1, 2, 5, 12, 29, 71, 175, 434, 1082, 2709, 6807, 17157` | **novel-candidate** (no match, 2026-10-16); in bijection with the valleyless Motzkin meanders of length `s − 2`, which [[prodinger-2025-cornerless-motzkin-bargraphs](pages/prodinger-2025-cornerless-motzkin-bargraphs.md)] reports as absent from the OEIS; refined by last-column height and spires on [[motzkin-castles](pages/motzkin-castles.md)] |
| Motzkin castles | 1-smooth, first column at height 1, by semi-perimeter | `1, 1, 2, 4, 8, 16, 33, 69, 145, 307, 655, 1405, 3027` | **novel-candidate** (no match, 2026-10-16) |
| Motzkin castles | 1-smooth, any ends, by semi-perimeter | `1, 2, 5, 11, 24, 52, 113, 246, 537, 1176, 2583, 5688` | **novel-candidate** (no match, 2026-10-16) |
| Ridge strips and ridge castles | ridge castles of height 4 | `1, 7, 31, 118, 421, 1453, 4924` | **novel-candidate** (no match, 2026-10-16) |
| Ridge strips and ridge castles | even-block ridge castles of height 4 | `1, 7, 25, 70, 209, 697, 2390` | **novel-candidate** (no match, 2026-10-16) |
| Ridge strips and ridge castles | even-block ridge castles of height 5 | `0, 0, 10, 104, 604, 2836, 12630` | **novel-candidate** (no match, 2026-10-16) |
| Signed tower count P(k, ·) rows | `P(2, L)` | `1, 1, 3, 9, 19, 33, 59, 121, 259, 529` | **novel-candidate** (no match, 2026-10-16) |
| Signed tower count P(k, ·) rows | `P(3, L)` | `1, 0, −4, −16, −40, −64, −32, 192, 832, …` | **novel-candidate** (signed and absolute values, no match, 2026-10-16) |
| Signed tower count P(k, ·) rows | `P(4, L)` | `1, 1, 5, 25, 85, 225, 541, 1385, 3973` | **novel-candidate** (no match, 2026-10-16) |
| Signed tower count P(k, ·) rows | `P(5, L)` | `1, 0, −6, −36, −140, −384, −680, −112, 5040, …` | **novel-candidate** (signed and absolute values, no match, 2026-10-16) |
| Signed tower count P(k, ·) rows | `P(6, L)` | `1, 1, 7, 49, 231, 833, 2583, 7889, 26503, …` | **novel-candidate** (no match, 2026-10-16); `char_6 = (x³−4x²+4x−8)(x⁴−3x³+8x²−4x+8)`, largest root `2ψ²` ([[plastic-number](pages/plastic-number.md)]) |
| Castles by semi-perimeter | all castles (bargraphs) | `1, 2, 5, 13, 35, 97, 275, 794, 2327` | **interlink** → [A082582](https://oeis.org/A082582) (`= A082582(s)`, bargraphs by semi-perimeter; no castle reading, 2026-10-16) |
| Castles by semi-perimeter | castles by `(s, w)` | rows `1; 1,1; 1,3,1; 1,5,6,1; …` | **interlink** → [A271942](https://oeis.org/A271942) (rows checked for `s ≤ 16`; the entry does not give the Narayana form) |
| Castles by semi-perimeter | even-block castles | `0, 1, 3, 7, 17, 47, 137, 400, 1168, 3450, 10338` | **novel-candidate** (no match, 2026-10-16) |
| Castles by semi-perimeter | signed castles `Σ(-1)^blocks` | `-1, 0, 1, 1, -1, -3, -1, 6, 9, -5, -29, -20, 55` | **novel-candidate** (signed, negated and absolute values, no match, 2026-10-16) |
| Castles by semi-perimeter | even-block convex castles | `0, 1, 3, 7, 17, 44, 116, 305, 799, 2091` | **novel-candidate** (no match, 2026-10-16) |
| Castles by semi-perimeter | signed convex castles | `-1, 0, 1, 1, 0, -1` (period 6) | periodic, not searched |
| Castles by semi-perimeter | castles of height 5 with no 1 next to a 2 and no 4 next to a 5, silver by semi-perimeter | `1, 7, 26, 74, 196, 525, 1421, 3809, 10040, 26102, 67250` (from `s = 6`) | **novel-candidate** (no match, 2026-10-11 and 2026-10-22), [[semi-perimeter-growth-census](pages/semi-perimeter-growth-census.md)] |
| Prime castles by area | prime convex castles `U` | `1, 1, 2, 3, 5, 8, 12, 19, 28, 42, 61, 90` | **novel-candidate** (no match, 2026-10-16) |
| Prime castles by area | non-convex prime castles `F_{n−1} − U` | `1, 2, 6, 13, 28, 54, 106, 194` (from `n = 8`) | **novel-candidate** (no match, 2026-10-16) |
| Prime castles by area | `U` by width | rows `1; 1; 1,1; 1,2; 1,3,1; 1,4,3; 1,5,5,1` | **novel-candidate** (no match, 2026-10-16) |
| Prime castles by area | convex castles with first column not at height 1 | `1, 2, 4, 7, 12, 20, 32, 51, 79` | **interlink** → [A342528](https://oeis.org/A342528) (`= A342528(n−1) = A001523(n) − A001523(n−1)`, checked for `n ≤ 1001` against the two b-files; neither entry cites the other, 2026-10-16) |
| Prime castles by area | castles of area `n` up to rearranging prime factors | `1, 2, 3, 5, 9, 15, 26, 45, 78, 134, 233` (from `n = 1`) | **novel-candidate** (no match, 2026-10-16; [A228645](https://oeis.org/A228645) agrees for 10 terms and differs at the 11th, 232 against 233), [[signed-prime-castles](pages/signed-prime-castles.md)] |
| Prime castles by area | prime parity splits (all and convex) | on the two pages | **novel-candidate** (no match, 2026-09-22) |
| Prime castles by area | signed castles by area `even − odd` | `-1, 0, 0, 2, 0, 2, -4, 2, -12, 10, -20, 38` (from `n = 1`; 300 terms computed) | **novel-candidate** (no match, 2026-10-16), [[castle-row-raising-equation](pages/castle-row-raising-equation.md)] |
| Prime castles by area | signed growth constant `ρ` and prefactor `C` | `1.62382967400459...`, `0.09850917497311...` | **novel-candidate** decimal expansions (no match, 2026-10-16) |
| Prime castles by area | second signed singularity `q_1` | `-0.82027198` | **novel-candidate** (no match for the digits `8, 2, 0, 2, 7, 1, 9, 8`, 2026-10-16), [[castle-q-bessel-closed-form](pages/castle-q-bessel-closed-form.md)] |
| Prime castles by area | castles by area and peaks | rows `1; 1,1; 1,3; 1,7; 1,14,1; 1,26,5` | **novel-candidate** (no match, 2026-10-16) |
| Prime castles by area | one-peak castles | `1, 3, 7, 14, 26, 46, 79, 133` | **interlink** → [A001924](https://oeis.org/A001924) (`= A001924(n−1)`; the entry has no reading by compositions) |
| Classical polyomino families among castles, by area | signed monotone castles `even − odd` | `-1, 0, 0, 1, 0, 2, 0, 2, -1, 4, -2, 4, -4, 6` | **novel-candidate** (signed, negated and absolute values, no match, 2026-10-16) |
| Odd-block counts, parity-refined area, and joint block tables | `A^o(w, h)` rows, `h = 3..7` | `h = 3`: `1, 5, 16, 44, 122, 358, 1082, 3274` | **novel-candidate** (`h = 3, 4`: no match, 2026-10-16; `h = 5…7`: 2026-09-26) |
| Odd-block counts, parity-refined area, and joint block tables | columns `A^o(4..6, h)`, `A^e(5, h)`, `A^e(6, h)` | `A^o(4, h)`: `1, 5, 44, 58, 247, 223, 738, 564` | **novel-candidate** (`A^o(4, ·)`: no match, 2026-10-16; others: 2026-09-26) |
| Odd-block counts, parity-refined area, and joint block tables | even, odd, convex, valley, non-convex and strict-valley castles by area, split by parity, and their signed differences | on the page | **novel-candidate** (no match, 2026-09-26) |
| Odd-block counts, parity-refined area, and joint block tables | castles by area and blocks, triangle | rows `1; 1,1; 1,2,1; 1,4,2,1; 1,6,6,2,1` | **novel-candidate** (no match, 2026-10-16; [A319421](https://oeis.org/A319421) and [A092479](https://oeis.org/A092479) agree on the first five rows, and the sixth row is `1, 9, 12, 7, 2, 1`) |
| Odd-block counts, parity-refined area, and joint block tables | three-, four- and five-block columns; other cells by blocks and peaks | on the page | **novel-candidate** (no match, 2026-09-26) |
| Odd-block counts, parity-refined area, and joint block tables | castles of width `w` and height `h` with `h + 1` blocks | `h = 3`: `3, 21, 84, 252, 630, 1386` (from `w = 3`) | **interlink** → [A253943](https://oeis.org/A253943) at `h = 3` (`= A253943(w+2) = 3 C(w+3, 6)`); `h = 4`, `5, 45, 225, 825, 2475, 6435`: **novel-candidate** (no match, 2026-10-16) |
| Odd-block counts, parity-refined area, and joint block tables | castles of width `w` and height `h` by blocks, triangles `h = 3, 4`, and the column `h + 2` | `h = 3` rows from `b = 3`: `1; 5; 15,3,1; 35,21,9; 70,84,51,5,1` | **novel-candidate** (`h = 3`: no match, 2026-10-16) |
| Half-sum rows | `K_2` | `1, 5, 18, 60, 202, 702, 2508, 9136, 33742, 125934` | **novel-candidate** (no match, 2026-10-16) |
| Half-sum rows | `K_3` | `3, 27, 149, 671, 2755, 10833, 41679, 158465, 598681` | **novel-candidate** (no match, 2026-10-16) |
| Half-sum rows | `K_4` | `1, 9, 51, 241, 1069, 4671, 20353, 88383, 381583, 1635893` | **novel-candidate** (no match, 2026-10-16) |
| Half-sum rows | `K_5` | `10, 142, 1210, 8222, 49806, 283570, 1557158, 8354490` | **novel-candidate** (no match, 2026-10-16) |
| Half-sum rows | dyadic half-sum `4^w H_h(w)`, `h = 2..5`, and the numerators of `H_2`, `1, 7, 63, 231, 3131, 10929` | on the page | **novel-candidate** (numerators of `H_2`, checked against `Σ_k C(2k, k) 4^{−k} A^e(w − k, 2)`: no match, 2026-10-16; others: 2026-09-23) |
| Tree castles by area at fixed height | height at most 8 | `1, 2, 4, 7, 12, 21, 37, 65, 113, 197, 345, 604, 1056, 1846` | **novel-candidate** (no match, 2026-10-16) |
| Sandpile groups | castles with trivial group (the tree castles, in both models) | `1, 2, 3, 5, 8, 13, 22, 37, 63, 108, 186, 322, 559, 973, 1697, 2964` | **interlink** → [A005683](https://oeis.org/A005683) Twopins positions (`= A005683(n+2)`; the formula agrees with the b-file for `n ≤ 38`, 2026-10-16) |
| Sandpile groups | castles with cyclic `K_sink` | `1, 2, 3, 6, 10, 20, 36, 72, 134, 264, 503, 997, 1933, 3791, 7338, 14329` | **novel-candidate** (no match, 2026-10-16) |
| Sandpile groups | distinct groups `K_sink` among castles of `n` cells | `1, 1, 1, 2, 2, 3, 3, 4, 6, 8, 10, 13, 18, 25, 34, 48` | **novel-candidate** (no match, 2026-10-16) |
| Sandpile groups | castles with cyclic `K_tide` | `1, 2, 3, 6, 10, 20, 36, 72, 135, 268, 513, 1015, 1975, 3902, 7631, 15028` | **novel-candidate** (no match, 2026-10-16) |
| Sandpile groups | distinct groups `K_tide` among castles of `n` cells | `1, 1, 1, 2, 2, 4, 4, 7, 9, 14, 18, 27, 38, 56, 78, 113` | **novel-candidate** (no match, 2026-10-16) |
| Fibonacci castle sub-families | balanced castles | `1, 2, 4, 7, 12, 18, 27, 38, 52, 68, 89, 112` | **interlink** → [A049703](https://oeis.org/A049703) (`= A049703(w)`; the entry is defined only as `A005598(n)/2`, with no comments, 2026-10-16) |
| Fibonacci castle sub-families | `(1, 3)`-RLL castles | `1, 2, 4, 7, 10, 15, 22, 32, 47, 69` | **known** → [A003410](https://oeis.org/A003410) (`= A003410(w)` for `w ≥ 4` and `A003410(w) − 1` for `w ≤ 3`; the entry counts the binary words with no `11` and no `0000`, the towers); **interlink** → [A226136](https://oeis.org/A226136), whose 36 terms equal the castle counts and which gives the castle g.f. only as a conjecture (2026-10-16) |
| Fibonacci castle sub-families | `(1, 7)`-RLL castles | `1, 2, 4, 7, 12, 20, 33, 54, 86, 138, 221` | **novel-candidate** (no match, 2026-10-16) |
| Fibonacci castle sub-families | `(2, 7)`-RLL castles | `1, 2, 3, 5, 8, 12, 18, 27, 38, 54, 78` | **novel-candidate** (no match, 2026-10-16) |
| Fibonacci castle sub-families | `(2, 10)`-RLL castles | `1, 2, 3, 5, 8, 12, 18, 27, 40, 59, 87, 126, 183` | **novel-candidate** (no match, 2026-10-16) |
| Multi-interpretation hub | A005251, the four readings | - | **interlink**; the entry states none of the four readings (checked 2026-10-16) |
| Strip Perron-root sequences | quadratic strips off the line `p₂ = 1`, fields `Q(√17)`, `Q(√21)`, `Q(√6)`, `Q(√7)`, `Q(√33)` | - | **unchecked**; several strip matrices reach each field, so a field has no single count sequence to search |
| Other rows | `A^e(w, 3)`, the even-block castles of height 3, `0, 0, 3, 21, 89, 307, 977, 3031, …` ([[new-sequence-fw3](pages/new-sequence-fw3.md)]): **novel-candidate** (no match, 2026-10-16). | - | (status in the text) |
| Other rows | The rows `A^e(w, 4) = 1, 7, 31, 117, 439, 1729, 7063, 29201, …`, `A^e(w, 5) = 0, 0, 10, 122, 906, 5478, 30274, …` and `A^e(w, 6) = 1, 11, 76, 448, 2630, 16126, 101654, …` of the array `A^e(w, h)`: **novel-candidate** (no match, 2026-10-16). | - | (status in the text) |
| Other rows | The odd-block rows `A^o(w, 3) = 1, 5, 16, 44, 122, 358, 1082, 3274, …` and `A^o(w, 4) = 0, 0, 6, 58, 342, 1638, 7134, …`: **novel-candidate** (no match, 2026-10-16). | - | (status in the text) |
| Other rows | Columns of width 3 ([[sum-of-three-cubes-castles](pages/sum-of-three-cubes-castles.md)]): `A^e(3, 2m) = 10m² − 5m + 1 = 5m(2m − 1) + 1`, `6, 31, 76, 141, 226, 331, 456, 601, 766, 951, …`: **novel-candidate** (no match by terms, 2026-10-16; it is `A080860(−m)`). `A^o(3, 2n+1) = 10n² + 5n + 1`, `1, 16, 51, 106, 181, 276, …`: **interlink** → [A080860](https://oeis.org/A080860) (`= A080860(n)`). `A^e(3, 2m+1) = C(2m+1, 2) = m(2m+1)`: **known**, the second hexagonal numbers [A014105](https://oeis.org/A014105). `A^o(3, 2m) = C(2m, 2) = m(2m − 1)`: **known**, the hexagonal numbers [A000384](https://oeis.org/A000384). The interleaved columns `A^e(3, h)` (`6, 3, 31, 10, 76, 21, …` from `h = 2`), `A^o(3, h)` (`1, 1, 16, 6, 51, 15, …` from `h = 1`) and `A^e(4, h)` (`10, 21, 117, 122, 448, 367, 1131, 820, …` from `h = 2`): **novel-candidate** (no match, 2026-10-16). `A^e(4, h)` is `(4h−3)(4h²−3h+2)/6` at even `h` and `(h−1)(8h²−4h+3)/6` at odd `h` (checked `h < 30`). | - | (status in the text) |
| Other rows | `\|P(k, L)\|` in the tower height `k` at fixed `L ≥ 5` ([[castle-eigenvalue-oeis-crosswalk](pages/castle-eigenvalue-oeis-crosswalk.md)]): `\|P(k, 5)\| = 1, 0, 33, 64, 225, 384, 833, 1280, 2241, …` and `\|P(k, 6)\| = 1, 8, 59, 32, 541, 680, 2583, 3520, …` from `k = 0`: **novel-candidate** (no match, 2026-10-16). The rows in `L` are in the section *Signed tower count P(k, ·) rows*. | - | (status in the text) |
| Other rows | The parity-refined sequences by area (even and odd; convex, valley, non-convex and strict-valley) ([[castle-by-area](pages/castle-by-area.md)]): **novel-candidate**, searched 2026-09-26; terms on [[odd-castles-and-block-tables](pages/odd-castles-and-block-tables.md)]. | - | (status in the text) |
| Other rows | The towers of width `w ≥ 6` by number of blocks `b` ([[tower-narayana-polynomial](pages/tower-narayana-polynomial.md)]): `w = 6`: `1, 21, 161, 721, 2331, 6083, …`; `w = 7`: `1, 28, 280, 1582, 6244, 19348, …` from `b = 0`: **novel-candidate** (no match, 2026-10-16). | - | (status in the text) |
| Other rows | The denominators of the Jacobi-Perron convergents of `2ψ²` ([[castle-eigenvalue-oeis-crosswalk](pages/castle-eigenvalue-oeis-crosswalk.md)]): `1, 1, 2, 4, 47, 53, 104, 204, 2409, 2717, 5330, …`: **novel-candidate** (no match, 2026-10-16). | - | (status in the text) |

#### No match in the first mining pass (`raw/oeis-pe502/mine-notes.md`, `crosslink-avenues.md`, `vein9-area.md`)

- The rows `A^e(·, h)` for `h = 3, 4, 5` (recurrence orders 6, 9, 11) and the columns `A^e(w, ·)` for `w = 3, 4, 5`.
- The rows `A^o(·, h)` for `h = 3, 4, 5` (orders 5, 9, 11): "No OEIS match" (Vein 8).
- The block-count distribution of the castles of height `h ≥ 2`: "a new 2D table (no OEIS match)" (Vein 7).
- The towers by blocks, rows `w = 6, 7`: "new" (Tier 2).
- The castles by area split by block parity (even, odd, `cev`, `cod`: "four new sequences"), the strict-valley castles by area, `0, 0, 0, 0, 1, 3, 8, 17, 34, 60, 107, 175, 285, 445, 691, …` ("NEW sequence"), and "The 6 parity-refined variants ... are all new" (Veins 9, 9b).

#### Equal to an entry that does not state the castle reading (interlinks)

| catalogue section | object | entry, as recorded |
|---|---|---|
| Castles by area with bounded height: the n-nacci family | height 2 | **interlink** → [A000071](https://oeis.org/A000071) (`= A000071(n+1) = F_{n+1} − 1`) |
| Castles by area with bounded height: the n-nacci family | height at most 3 | **interlink** → [A000073](https://oeis.org/A000073) (`= A000073(n+2)`) |
| Castles by area with bounded height: the n-nacci family | height at most 4 | **interlink** → [A000078](https://oeis.org/A000078) (`= A000078(n+3)`) |
| Castles by area with bounded height: the n-nacci family | height at most 5 | **interlink** → [A001591](https://oeis.org/A001591) (`= A001591(n+4)`) |
| Tower-spacing skylines | `(h=2, g=2)` | **interlink** → [A005251](https://oeis.org/A005251) (`= A005251(w+3)`; the section *Multi-interpretation hub*) |
| Tower-spacing skylines | `(h=3, g=2)` | **interlink** → [A202882](https://oeis.org/A202882) (`= A202882(w+1)`; Hardin) |
| Tower-spacing skylines | `(h=4, g=2)` | **interlink** → [A203094](https://oeis.org/A203094) (`= A203094(w+1)`; Hardin) |
| Tower-spacing skylines | `(h=5, g=2)` | **interlink** → [A203184](https://oeis.org/A203184) (`= A203184(w+1)`; Hardin) |
| Tower-spacing skylines | `(h=6, g=2)` | **interlink** → [A203050](https://oeis.org/A203050) (`= A203050(w+1)`; Hardin) |
| Tower-spacing skylines | `(h=2, g=3)` | **interlink** → [A005252](https://oeis.org/A005252) (`= A005252(w+3)`) |
| Tower-spacing skylines | `(h=2, g=4)` | **interlink** → [A005253](https://oeis.org/A005253) (`= A005253(w+3)`) |
| Tower-spacing skylines | `(h=2, g=5)` | **interlink** → [A005689](https://oeis.org/A005689) Twopins positions (`= A005689(w+6)`) |
| Tower-spacing skylines | `(h=2, g=6)` | **interlink** → [A098574](https://oeis.org/A098574) (`= A098574(w+6)`) |
| Tower-spacing skylines | `(h=3, g=3)` | **interlink** → [A217878](https://oeis.org/A217878) (0..2 arrays, "minimum of 3 adjacent elements") |
| Tower-spacing skylines | `(h=3, g=4)` | **interlink** → [A217879](https://oeis.org/A217879) (0..2, minimum of 4) |
| Tower-spacing skylines | `(h=3, g=5)` | **interlink** → [A217880](https://oeis.org/A217880) (0..2, minimum of 5) |
| Tower-spacing skylines | `(h=3, g=6)` | **interlink** → [A217881](https://oeis.org/A217881) (0..2, minimum of 6) |
| Tower-spacing skylines | `(h=4, g=3)` | **interlink** → [A217949](https://oeis.org/A217949) (0..3, minimum of 3) |
| Tower-spacing skylines | `(h=4, g=4)` | **interlink** → [A217950](https://oeis.org/A217950) (0..3, minimum of 4) |
| Tower-spacing skylines | `(h=4, g=5)` | **interlink** → [A217951](https://oeis.org/A217951) (0..3, minimum of 5) |
| Tower-spacing skylines | `(h=4, g=6)` | **interlink** → [A217952](https://oeis.org/A217952) (0..3, minimum of 6) |
| Tower-spacing skylines | `(h=5, g=3)` | **interlink** → [A228457](https://oeis.org/A228457) (0..4 arrays, "maxima of three adjacent elements") |
| Tower-spacing skylines | `(h=6, g=3)` | **interlink** → [A228458](https://oeis.org/A228458) (0..5, maxima of three) |
| The Pell castle strip: 1-smooth strips on {1, 2, 3} | first column at height 1 | **interlink** → [A000129](https://oeis.org/A000129) Pell numbers (`= P⋆_w`; width g.f. `x/(1−2x−x²)`) |
| The Pell castle strip: 1-smooth strips on {1, 2, 3} | any first column | **interlink** → [A001333](https://oeis.org/A001333) Pell-Lucas numbers (`= A001333(w+1)`) |
| The Pell castle strip: 1-smooth strips on {1, 2, 3} | both end columns at height 1 | **interlink** → [A171842](https://oeis.org/A171842) (`= A171842(w−1)`, "Motzkin n-paths of height <= 2"; [[motzkin-castles](pages/motzkin-castles.md)]) |
| The Pell castle strip: 1-smooth strips on {1, 2, 3} | **Pell castles**: first column at height 1, height 3 | **interlink** → [A094706](https://oeis.org/A094706) (`= A094706(w−2) = P⋆_w − 2^{w−1}`, g.f. `x³/((1−2x−x²)(1−2x))`, proved; the entry has no castle reading, 2026-10-16) and column 2 of [A283595](https://oeis.org/A283595) (Motzkin prefixes by height, row `w − 1`); [[pell-castle](pages/pell-castle.md)] |
| The Pell castle strip: 1-smooth strips on {1, 2, 3} | any first column, height 3 | **interlink** → [A106514](https://oeis.org/A106514) (`= A106514(w−1)`, g.f. `x(1−x)/((1−2x)(1−2x−x²))`, proved) |
| The Pell castle strip: 1-smooth strips on {1, 2, 3} | both end columns at height 1, height 3 | **interlink** → column 2 of [A097862](https://oeis.org/A097862) (Motzkin paths by height, row `w − 1`; g.f. `x⁵/((1−x)(1−2x)(1−2x−x²))`, the partial sums of the Pell castles shifted by 2; no match as a sequence of its own, 2026-10-16) |
| 1-smooth castles of height h | `smooth(w, h)`, first column at height 1, height `h` | **interlink** → column `h − 1` of [A283595](https://oeis.org/A283595) (Motzkin prefixes by height, row `w − 1`; checked for `h ≤ 7`, `w ≤ 14`). As a sequence of its own, the row `h = 4` agrees with [A378383](https://oeis.org/A378383) for `w ≤ 10` and differs at `w = 11` (5205 against 5206), so it has no match (2026-10-16); the row `h = 2` is [A000225](https://oeis.org/A000225)(`w − 1`); the row `h = 6` agrees with [A122611](https://oeis.org/A122611), the expansion of `1/η_12`, for `w = 6, …, 11` and differs at `w = 12` (6038 against 6039), because the g.f. is `x^h/(η_{2h} + x^h)`; the rows `h = 5…12` have no match (2026-10-22) |
| 1-smooth castles of height h | `strips(w, 4)` | **interlink** → [A001519](https://oeis.org/A001519) (`= A001519(w) = F_{2w−1}`) |
| 1-smooth castles of height h | `strips(w, 5)` | **interlink** → [A057960](https://oeis.org/A057960) (`= A057960(w−1)`) |
| 1-smooth castles of height h | `strips(w, 6)` | **interlink** → [A085810](https://oeis.org/A085810) (`= A085810(w)`, corridor of height 5) |
| 1-smooth castles of height h | even-block / odd-block / signed, `h = 2` | **interlink** → [A038505](https://oeis.org/A038505)(`w`), [A038503](https://oeis.org/A038503)(`w`) `− 1` and [A077860](https://oeis.org/A077860)(`w − 2`): deleting the first column gives all castles of height 2 and width `w − 1`, which the comments on A038505 and A038503 count by parity |
| 1-smooth castles of height h | both end columns at height 1, height `h` | **interlink** → column `h − 1` of [A097862](https://oeis.org/A097862) (row `w − 1`, checked for `h ≤ 7`, `w ≤ 14`; g.f. `x^{2h−1}/(χ_h χ_{h−1})`) |
| 1-smooth castles of height h | any first column, height `h = 4…12` | **interlink** → [A188866](https://oeis.org/A188866)`(h − 1, w) − A188866(h − 2, w)`, the difference of two rows of the smooth-word table; as sequences of their own no match for `h = 4…12` (2026-10-22) |
| 1-smooth castles of height h | last column within 1 of the first (cyclic), height `h` | **interlink** → [A002426](https://oeis.org/A002426)(`w`) for `w ≤ 2h − 1` (central trinomial coefficients); the rows `h = 3, 4` have no match from `w = 2h` on (2026-10-22) |
| m-smooth castles of height h | strips on the diagonal `h = m + 2`, `m = 2` | **interlink** → [A007482](https://oeis.org/A007482) (`= A007482(w−1)`, g.f. `1/(1−3x−2x²)`) |
| m-smooth castles of height h | strips, `h = m + 2`, `m = 3` | **interlink** → [A015530](https://oeis.org/A015530) (`= A015530(w)`, "Expansion of x/(1 - 4*x - 3*x^2)") |
| m-smooth castles of height h | strips, `h = m + 2`, `m = 4` | **interlink** → [A015537](https://oeis.org/A015537) (`= A015537(w)`, "Expansion of x/(1 - 5*x - 4*x^2)") |
| m-smooth castles of height h | strips, `m = 2`, `h = 5` | **interlink** → [A088132](https://oeis.org/A088132)(`w − 1`) (g.f. `(1 − x)/(1 − 4x + x³)`; the entry has no walk reading, 2026-10-22) |
| m-smooth castles of height h | first column at height 1, no ceiling, `m = 2` / both end columns at height 1, no ceiling, `m = 2` | **interlink** → [A180898](https://oeis.org/A180898)(`w`) and [A104184](https://oeis.org/A104184)(`w − 1`), walks with steps `−2, …, 2` above the axis ([[banderier-nicodeme-2010-bounded-discrete-walks](pages/banderier-nicodeme-2010-bounded-discrete-walks.md)]) |
| Motzkin castles | even-block Motzkin-path castles | **interlink** → [A343386](https://oeis.org/A343386) (`= A343386(w−1)`, odd Motzkin paths; no castle reading, 2026-10-16) |
| Motzkin castles | odd-block Motzkin-path castles | **interlink** → [A107587](https://oeis.org/A107587) (`= A107587(w−1)`, even Motzkin paths) |
| Motzkin castles | signed `Σ(−1)^blocks` | **interlink** → [A343773](https://oeis.org/A343773) (`= −A343773(w−1)`; `A343773(n) = (−1)^n A007440(n+1)`, the reversion of the Fibonacci g.f.) |
| Motzkin castles | 1-smooth, first column at height 1, by width | **interlink** → [A005773](https://oeis.org/A005773) (`= A005773(w)`, Motzkin left factors and directed animals) |
| Motzkin castles | drops of at most 1, last column at height 1, by width | **interlink** → [A000108](https://oeis.org/A000108) (`= C_w`) |
| Motzkin castles | Motzkin-path castles by semi-perimeter (`s = 2…`) | **interlink** → [A023431](https://oeis.org/A023431) (`= A023431(s−2)`, Motzkin paths with no `UD` and no `UU`) |
| Motzkin castles | drops of at most 1, last column at height 1, by semi-perimeter | **interlink** → [A004148](https://oeis.org/A004148) (`= A004148(s−1)`, peakless Motzkin paths; the mirror image without double rises is Deutsch-Elizalde's RNA-secondary-structure bijection, [[deutsch-elizalde-2016-bargraphs-cornerless-motzkin](pages/deutsch-elizalde-2016-bargraphs-cornerless-motzkin.md)]) |
| Ridge strips and ridge castles | ridge strips, `h = 3` | **interlink** → [A001333](https://oeis.org/A001333) Pell-Lucas numbers (`= A001333(w+1)`) |
| Ridge strips and ridge castles | ridge strips, `h = 4` | **interlink** → [A003688](https://oeis.org/A003688) (`= A003688(w+1)`) |
| Ridge strips and ridge castles | ridge strips, `h = 5` | **interlink** → [A015448](https://oeis.org/A015448) (`= A015448(w+1) = F_{3w+2}`) |
| Signed tower count P(k, ·) rows | `P(1, L)` | **interlink** → [A146559](https://oeis.org/A146559) (`= A146559(L+1) = Re((1+i)^{L+1})`) |
| Castles by semi-perimeter | all castles (bargraphs) | **interlink** → [A082582](https://oeis.org/A082582) (`= A082582(s)`, bargraphs by semi-perimeter; no castle reading, 2026-10-16) |
| Castles by semi-perimeter | castles by `(s, w)` | **interlink** → [A271942](https://oeis.org/A271942) (rows checked for `s ≤ 16`; the entry does not give the Narayana form) |
| Prime castles by area | convex castles with first column not at height 1 | **interlink** → [A342528](https://oeis.org/A342528) (`= A342528(n−1) = A001523(n) − A001523(n−1)`, checked for `n ≤ 1001` against the two b-files; neither entry cites the other, 2026-10-16) |
| Prime castles by area | one-peak castles | **interlink** → [A001924](https://oeis.org/A001924) (`= A001924(n−1)`; the entry has no reading by compositions) |
| Odd-block counts, parity-refined area, and joint block tables | two-block castles by area | **interlink** → [A002620](https://oeis.org/A002620) quarter-squares (`= A002620(n)`) |
| Odd-block counts, parity-refined area, and joint block tables | three-block castles with one peak, by area | **interlink** → [A097701](https://oeis.org/A097701) (`= A097701(n−3)`) |
| Odd-block counts, parity-refined area, and joint block tables | three-block castles with two peaks, by area | **interlink** → [A002624](https://oeis.org/A002624) (`= A002624(n−5)`) |
| Odd-block counts, parity-refined area, and joint block tables | castles of width `w` and height `h` with `h + 1` blocks | **interlink** → [A253943](https://oeis.org/A253943) at `h = 3` (`= A253943(w+2) = 3 C(w+3, 6)`); `h = 4`, `5, 45, 225, 825, 2475, 6435`: **novel-candidate** (no match, 2026-10-16) |
| Tree castles by area at fixed height | height 2 | **interlink** → [A077868](https://oeis.org/A077868) (`= A077868(n−2)`, `n ≥ 2`) |
| Tree castles by area at fixed height | height at most 3 | **interlink** → [A006498](https://oeis.org/A006498) (`= A006498(n+1)`) |
| Tree castles by area at fixed height | height at most 4 | **interlink** → [A000570](https://oeis.org/A000570), tournaments determined by their score vectors (`= A000570(n+1)`) |
| Tree castles by area at fixed height | height at most 5 | **interlink** → [A079816](https://oeis.org/A079816) (`= A079816(n+1)`) |
| Tree castles by area at fixed height | height at most 6 | **interlink** → [A189593](https://oeis.org/A189593) (`= A189593(n+1)`; the composition reading proves the entry's empirical recurrence) |
| Tree castles by area at fixed height | height at most 7 | **interlink** → [A189600](https://oeis.org/A189600) (`= A189600(n+1)`) |
| Sandpile groups | castles with trivial group (the tree castles, in both models) | **interlink** → [A005683](https://oeis.org/A005683) Twopins positions (`= A005683(n+2)`; the formula agrees with the b-file for `n ≤ 38`, 2026-10-16) |
| Sandpile groups | palindromic tree castles | **interlink** → [A000931](https://oeis.org/A000931) Padovan |
| Sandpile groups | `\ | **interlink** → [A001906](https://oeis.org/A001906) `F_{2n}` (`= A001906(w)`; every block on the ground) |
| Sandpile groups | `\ | **interlink** → [A001835](https://oeis.org/A001835) (`= A001835(h)`; one block on the ground) |
| Fibonacci castle sub-families | balanced castles | **interlink** → [A049703](https://oeis.org/A049703) (`= A049703(w)`; the entry is defined only as `A005598(n)/2`, with no comments, 2026-10-16) |


### Done (live on OEIS)

- [x] **A038505 / A038503 / A146559** — the height-2 hyperbolic interlink
  (`raw/oeis-pe502/oeis-xref-draft.md`; `wiki/pages/oeis-height2-hyperbolic-castles.md`).
  Approved and live (checked 2026-10-04: A038503 #93, Oct 03 2026; A038505 #140, Oct 04 2026;
  A146559 #152, Sep 28 2026): castle comments, the A000225 decomposition formulas,
  `A146559 = A038503 − A038505`, `Cf. A000225` on both, the PE 502 link on A038505.
- [x] A038505 typo fix, "Project 502" → "Problem 502" (A038505 #140, Oct 04 2026).
- [x] **A038503 exact-height correction** (submitted 2026-10-04, approved; confirmed
  2026-10-06). The "height at most 2" comment, which counted the `r = 0` term `C(n,0)` as a
  castle, is replaced by `a(n) − 1` = odd-block castles of width `n−1` and height 2:
  `raw/oeis-pe502/xrefs/A038503-exact-height.md`.
- [x] **A146559 castle comment** `a(n) = P(1, n−1)` (signed tower count at `k = 1`),
  submitted 2026-10-04, approved (A146559 #167, Oct 11 2026). Comment only, exact height:
  `a(n) − 1` = odd − even castles of height 2: `raw/oeis-pe502/xrefs/A146559-signed.md`
  (`wiki/pages/castle-sequence-catalogue.md`, `wiki/pages/signed-tower-count.md`).
- [x] **A009545 castle comment** (submitted 2026-10-06, approved: A009545 #203, Oct 14 2026).
  Comment only, width `n`, no `− 1`: `a(n)` = even-block − odd-block castles of width `n` and
  height 2 whose last column reaches height 2, for `n >= 1`, then a sentence defining the
  castle, and the PE 502 link: `raw/oeis-pe502/xrefs/A009545-signed.md`
  (`wiki/pages/signed-tower-count.md`, `wiki/pages/tower-parity-sectors.md`).
- [x] **A226275 recurrence** (submitted 2026-10-11, approved: A226275 #26, Oct 15 2026). Link
  to the A226136 proof (Theorem 1(b)); one "From _Chaz Reid_, Oct 11 2026" block with "Above
  formula proven in Reid link", `a(n) = a(n-1) + a(n-3)` for `n >= 6` and
  `a(n) = A226136(n+2) − A226136(n+1)`; a Python program.
- [x] **A226136 → A003410** (submitted 2026-10-06, major edit 2026-10-11, approved: A226136
  #29, Oct 18 2026). Link to the proof PDF `a226136.pdf` "Proof of Barker's Conjecture for
  A226136"; one "From _Chaz Reid_, Oct 11 2026: (Start) … (End)" block with "Conjectures
  confirmed (see Reid link)", `a(n) = A003410(n)` for `n >= 4` (A003410's g.f. minus
  `1 + x + x^2 + x^3`) and `a(n) = 1 + Sum_{k=0..n-2} A226275(k)`; b-file `n = 1..1000`
  (terms 1..35 from Kimberling); the Kimberling–Moses Fibonacci Quarterly 52 (2014) link
  (Example 4.2); the linear-recurrence index entry, signature `(1,0,1)`; a Python program;
  `Cf. A003410` and `Cf. A226274, A226275`. Jason Yuen's 2026-10-13 edit extended DATA to 42
  terms and added keyword `easy`: `raw/oeis-pe502/xrefs/A226136-A003410.md`
  (`wiki/pages/fibonacci-castles-sub-families.md`).

## Ingestion queue (wiki pages not yet ingested)

- [x] **Dyck Words** — done (`wiki/pages/dyck-words.md`). The first-return grammar the
  castle U/R/D grammar generalizes; steep Dyck words → Motzkin (verified).
- [x] **Lattice Paths** — done (`wiki/pages/lattice-paths.md`). Origin of the U/R/D
  encoding; stars-and-bars `C(W+H,H)`.
- [x] **AOCP/Combinatorics** — done (`wiki/pages/aocp-combinatorics.md`). Knuth's
  inversions + the q-factorial generating function `∏(1−z^k)/(1−z)^n`; seeds
  `wiki/pages/permutation-inversions.md`, a concrete foundation for the q-equivalent thread.
- [x] **AOCP/Permutations** — done (`wiki/pages/aocp-permutations.md`). TAOCP Vol. 1
  basics: n!, the insert-into-slots construction (stars-and-bars root), Stirling &
  Legendre (verified).
- [x] **AOCP/Generating Functions** — done (`wiki/pages/aocp-generating-functions.md`).
  The Fibonacci method, linear-recurrence ⇒ rational GF, the operation algebra, and the
  negative binomial — the methodological bedrock of the castle's rational GFs.
- [x] **AOCP/Generating Permutations and Tuples** — done
  (`wiki/pages/aocp-generating-permutations-tuples.md`). Mixed-radix add-one (Algorithm M =
  the castle brute-force) and reflected Gray code; seeds the "generation algorithms in
  castle space" seminar thread above.
- [x] **AOCP/Binomial Coefficients** — done (`wiki/pages/aocp-binomial-coefficients.md`).
  Vandermonde's convolution (closes the convex-castle count), hockey-stick, negate-upper-index,
  2^n / alternating sum, Stirling numbers.
- [x] **AOCP/Multisets** — done (`wiki/pages/aocp-multisets.md`). Multinomial permutations,
  two-line arrays, Foata intercalation, and the unique cycle factorization that grounds the
  castle's permutation-cycle analogy.
- [x] **AOCP/Multinomial Coefficients** — done (`wiki/pages/aocp-multinomial-coefficients.md`).
  The multinomial coefficient, the multinomial theorem, and the telescoping-into-binomials
  factorization (the higher-D lattice-path count). Completes the AOCP web the castle references.
- [x] The general **Generating Functions** topic page (distinct from
  AOCP/Generating Functions) — the concept page `wiki/pages/generating-functions.md` is
  seeded; this standalone source is still queued.
- [x] **Dyck Words/Examples** — worked enumeration examples (by hand, Python, SymPy) for
  Dyck and steep Dyck words; referenced by Castle Factoring. Newly surfaced.
- [x] **Dyck Words/Lisp** — Dyck words as Lisp S-expression skeletons. Newly surfaced.
- [x] **AOCP/Multisets** — referenced by AOCP/Combinatorics and Lattice Paths; the
  multiset-permutation / multichoose machinery. Newly surfaced.
- [x] **Generating Functions** (general topic page) — done
  (`wiki/pages/generating-functions-topic.md`). Sedgewick–Flajolet/Trotter reference with
  an explicit PE 502 application; the imaginary-roots / EGF-parity / every-4th-term examples
  are the same operations the castle uses.
- [x] **Combinatorics** — the general umbrella topic page (distinct from AOCP/Combinatorics).

## Housekeeping

- [x] Setup note / README for collaborators — done (`README.md`): what the wiki is, its
  layout and conventions, and the fresh-clone setup (re-run `git config core.hooksPath
  bin/hooks`, MCP config paths are machine-specific, `assets/` PDFs are git-ignored and
  re-fetchable from charlesreid1.com).
- [x] Remote for backup/sharing — done. `origin` → github.com/eeggwall/castles-wiki
  (SSH); `main` tracks `origin/main`.
