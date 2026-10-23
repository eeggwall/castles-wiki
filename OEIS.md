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
two-digit day (`Oct 04 2026`). See `wiki/pages/oeis-cross-referencing.md`; the
mathematical status of each sequence (known / interlink / novel-candidate / unchecked)
lives on `wiki/pages/castle-sequence-catalogue.md`.

### 1. In review (max 3)

- [~] **A005891 castles of width 3 and 4-cores** (submitted 2026-10-21, #138–#141), the
  A160747 form at `t = 4`: `a(n)` = 4-cores with `n` corners = castles of width 3 with `n + 1`
  blocks. Formula block: Cho et al.'s Prop. 3.4 sum and `a(n) = A271942(n+4, 3)`; the Narayana
  row-3 line was cut in #140, Oct 21. Links to Cho et al. and PE 502; `A001263, A271942` added
  to the first Cf. line, and the t-core family line: `raw/oeis-pe502/xrefs/A005891-tower.md`.
  Still in review (checked 2026-10-23): Alper Ferudun (#142, Oct 21) added "without the rule
  that the number of blocks is even" to the castle comment and checked the counts and
  formulas; Chaz Reid (#146–#147, Oct 22) changed "castles" to "castle polyominoes"; back in
  proposed. Michel Marcus (#148–#149, Oct 23) edited the Mathematica section only.
- [~] **A001263 castles of width `n` with `m` blocks** (submitted 2026-10-23, #788–#789). One
  comment block: `Sum_{k=1..n} T(n,k)*binomial(m+n-k-1, n-1)` = castle polyominoes of width `n`
  with `m` blocks, of any height and without the even-blocks rule, with the column-height
  definition and `See A005408, A005891, A063490, A160747 for n = 2..5`; a proof line from
  Deutsch-Elizalde eq. (2). The Deutsch-Elizalde and PE 502 links; a Python program for
  `T(n,k)`: `raw/oeis-pe502/xrefs/A001263-tower.md`, checked by `bin/python/tower_t_cores.py`.
  Michel Marcus asked (Oct 23) why the castles of width `n` with `m` blocks are not submitted
  as a new array: they are A271942 (bargraphs by semiperimeter and width) at
  `(n + m, n)`, since the semiperimeter is the width plus the blocks.
- [~] **A283595 column g.f.** (submitted 2026-10-23, #42–#43). One formula block: the g.f. of
  column `k` is `z^k/(R_k*R_{k+1})` with `R_k` from the A097862 polynomials `P_k`, and the
  product form of `R_k` over odd `i`; submitted without the proof line. `Column k=2 gives
  A094706(n-1).` and a Python program: `raw/oeis-pe502/xrefs/A283595-column-gf.md`, checked
  by `bin/python/a283595_column_gf.py` (`wiki/pages/1-smooth-castles.md` §3.2-3.3).

### 2. Ready to submit (drafted and checked, in order)

1. [ ] **Reverse links**, one edit each, each adding only the lines shown. The first three
   point at approved entries; the last three answer the A001263 and A283595 edits, so they
   wait until those are approved.
   1. [ ] A003410: `Cf. A226136.` (A226136 is this sequence from `n = 4`, approved #29).
   2. [ ] A226274: `Cf. A226136.` (A226136's Cf. line cites A226274).
   3. [ ] A038505: `Cf. A146559.` (`A146559 = A038503 − A038505`; A038503 and A146559
      already link both ways).
   4. [ ] A271942: `Cf. A001263.` and `Columns k=2..5 give A005408(n-3), A005891(n-4),
      A063490(n-4), A160747(n-6).` (A001263's formula `= A271942(n+m, n)`; the width-2..5
      castle counts; checked against the A271942 b-file by `bin/python/tower_t_cores.py`).
   5. [ ] A097862: `Cf. A283595.` (A283595's column g.f. is built from A097862's `P_k`).
   6. [ ] A094706: `a(n) = A283595(n+1, 2) for n >= 1.` and `Cf. A283595.` (A283595's
      `Column k=2 gives A094706(n-1).`; checked by `bin/python/a283595_column_gf.py`).

   Not added: A005408 (the odd numbers, dense). The t-core family line there would assert a
   3-core reading the entry does not have, and its castle draft is skipped.
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

1. [ ] **A094706** (Convolution of Pell(n) and 2^n; the entry has no comments): the Pell
   castles (exact height 3, first column 1, neighbouring columns differing by at most 1) of
   width `w` number `A094706(w − 2) = P⋆_w − 2^{w−1}` (`P⋆_w` the Pell numbers), proved by
   the g.f. `x³/((1−2x−x²)(1−2x))` (`wiki/pages/pell-castle.md`). The formula
   `a(n) = A283595(n+1, 2)` and `Cf. A283595` are in the stage-2 reverse links
   (`wiki/pages/1-smooth-castles.md`).
2. [ ] **A077868**: two castle readings and the bijection between them. Spaced Fibonacci
   castles (height-2 columns at least 3 apart) of width `w` number `A077868(w − 1)`; tree
   castles of height 2 with area `A` (cells) number `A077868(A − 2)`; the domino-boundary map
   matches the Fibonacci castles with `w + 1` cells to the spaced castles of width `w`.
   Brute-force verified 2026-10-04
   (`wiki/pages/fibonacci-castles-sub-families.md`, `wiki/pages/tree-castle-by-area.md`).
3. [ ] **A049703**: balanced Fibonacci castles of width `w` number `A005598(w)/2 = A049703(w)`
   (towers balanced, i.e. finite Sturmian); the entry is defined only as `A005598(n)/2`, with
   no combinatorial reading. Brute-force verified `w ≤ 15`, 2026-10-04
   (`wiki/pages/fibonacci-castles-sub-families.md`).
4. [ ] **A106514**: the 1-smooth castles of exact height 3 (free first column) of width `w`
   number `A106514(w − 1)`, g.f. `x(1−x)/((1−2x)(1−2x−x²))`, proved; the entry has
   only convolution and eigensequence comments (`wiki/pages/pell-castle.md`).
5. [ ] **Tower-spacing new sequences** (`wiki/pages/tower-spacing-castles.md`): the six
   unfiled cells `(h,g)` for `h in {5,6}`, `g in {4,5,6}` (Hardin's "0..(h-1) arrays, each
   element the minimum of `g` adjacent elements", never filed at these parameters; no match
   2026-09-20).
6. [ ] **Tower-spacing table comments**: one comment each on the tables A217883 / A217954 /
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
  dense entries, and the array A047969 already has the reading (skipped below).
- A000071 (the Fibonacci castles of width `w`, `A000071(w+2)`; the castles of height 2 with
  area `A`, `A000071(A+1)`): the entry already has both, as "nonempty subsets of {1,2,...,n}
  that contain no consecutive elements" and Arndt's "compositions of n with maximal part 2".
- A047969 (castles of width `k+1` and height `n+1`, `h^w − (h−1)^w`): the entry already has
  Arnold's "a(n-1, k-1) is the number of ordered k-tuples of positive integers such that the
  largest of these integers is n", the column heights of those castles.
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
- [x] **A226136 → A003410** (submitted 2026-10-06, approved: A226136 #29, Oct 18 2026). Link
  to the proof PDF `a226136.pdf`; one "From _Chaz Reid_, Oct 11 2026" block with "Conjectures
  confirmed (see Reid link)", `a(n) = A003410(n)` for `n >= 4` (equivalent to Barker's g.f.)
  and `a(n) = 1 + Sum_{k=0..n-2} A226275(k)`; b-file `n = 1..1000`; the Kimberling–Moses
  link; the recurrence index entry, signature `(1,0,1)`; `Cf. A003410, A226274, A226275`.
  Jason Yuen extended DATA to 42 terms and added keyword `easy`; the stray `a226136.txt` is
  deleted: `raw/oeis-pe502/xrefs/A226136-A003410.md`
  (`wiki/pages/fibonacci-castles-sub-families.md`).
- [x] **A160747 castles of width 5 and 6-cores** (submitted 2026-10-16, approved: A160747 #62,
  Oct 22 2026). Comment block: 6-cores with `n` corners = castle polyominoes of width 5 with
  `n + 1` blocks (column heights `c(i) >= 1`, fixed Oct 18 after Alper Ferudun's note).
  Formula block: `Sum_{k=1..5} A001263(5,k)*binomial(n+5-k, 4)` (Sean A. Irvine cut the
  "row 5 of A001263" clause), Cho et al.'s Prop. 3.4 sum, `a(n) = A271942(n+6, 5)`. The PE 502
  link, `Cf. A001263, A271942` and the t-core family line:
  `raw/oeis-pe502/xrefs/A160747-tower.md` (`wiki/pages/tower-narayana-polynomial.md`).
- [x] **A063490 castles of width 4 and 5-cores** (submitted 2026-10-16, approved: A063490 #66,
  Oct 22 2026). Comment block: 5-cores with `n − 1` corners = castle polyominoes of width 4
  with `n` blocks. Formula block: `Sum_{k=1..4} A001263(4,k)*binomial(n+3-k, 3)` (Sean A.
  Irvine cut the "x times row 4 of A001263" clause), Cho et al.'s Prop. 3.4 sum,
  `a(n) = A271942(n+4, 4)`. The PE 502 link (Jason Yuen moved it from REFERENCES to LINKS),
  `Cf. A001263, A064788, A185505, A271942.` and the t-core family line:
  `raw/oeis-pe502/xrefs/A063490-tower.md`.

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
