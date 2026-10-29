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

**Procedure.**

- The OEIS allows **3 open edits at a time**, and each takes days to review. Stage 1 lists
  the open edits. When one is approved, move it to *Done* with its revision number, the
  approval date and any change the editor made, then submit the top item of stage 2.
- An entry takes one open edit at a time: a follow-up edit to an entry in stage 1 waits for
  that edit's approval.
- Keep stages 2 to 4 stocked while waiting: draft the top of stage 3 into stage 2, and give
  each stage-4 candidate a verdict (stage 3, or *Skipped* with the reason).
- A tool may run the verification scripts, check offsets against the live entries and
  format data; only a person rewrites the draft prose, signs it and submits
  (`raw/oeis-pe502/SUBMISSION-NOTES.md` §4). Signatures use a two-digit day (`Oct 04 2026`).
- Editors' changes so far, to follow in new drafts: links go in alphabetical order by
  author, after the b-file and before the Index link (Stefano Spezia, A160747); a formula
  line is the bare formula, with at most a citation in parentheses, and any explanation goes
  in a comment (Sean A. Irvine removed the words after the Narayana-numerator formulas on
  A160747 and A063490).
- The OEIS status of each castle sequence (known / interlink / novel-candidate / unchecked)
  is kept in *Search record* at the end of this file; the wiki's `castle-sequence-catalogue`
  lists the sequences and the entries they equal, with no status.

**Next step (2026-10-23).** Stage 1 is full: A005891, A001263, A283595. When a slot opens,
submit the first reverse link of stage 2, A003410 back to A226136. When A283595 #43 is
approved, its follow-up (the first item of stage 3) can be drafted.

### 1. In review (max 3)

- [~] **A005891 castles of width 3 and 4-cores** (submitted 2026-10-21, #138–#141), the
  A160747 form at `t = 4`: `a(n)` = 4-cores with `n` corners = castles of width 3 with `n + 1`
  blocks. Formula block: Cho et al.'s Prop. 3.4 sum and `a(n) = A271942(n+4, 3)`; the Narayana
  row-3 line was cut in #140, Oct 21, since the entry's "triangular numbers convolved with
  [1, 3, 1, 0, 0, 0, ...]" comment (Adamson and Povolotsky, May 29 2009) already states it.
  Links to Cho et al. and PE 502; `A001263, A271942` added to the first Cf. line, and the
  t-core family line: `raw/oeis-pe502/xrefs/A005891-tower.md`, checked by
  `bin/python/tower_t_cores.py`.
  Still in review (checked 2026-10-23): Alper Ferudun (#142, Oct 21) added "without the rule
  that the number of blocks is even" to the castle comment and checked the counts and
  formulas; Chaz Reid (#146–#147, Oct 22) changed "castles" to "castle polyominoes"; back in
  proposed. Michel Marcus (#148–#149, Oct 23) edited the Mathematica section only.
- [~] **A001263 castles of width `n` with `m` blocks** (submitted 2026-10-23, #788–#789). One
  comment block: `Sum_{k=1..n} T(n,k)*binomial(m+n-k-1, n-1)` = castle polyominoes of width `n`
  with `m` blocks, of any height and without the even-blocks rule, with the column-height
  definition and `See A005408, A005891, A063490, A160747 for n = 2..5`; a proof line from
  Deutsch-Elizalde eq. (2). The Deutsch-Elizalde and PE 502 links; a Python program for
  `T(n,k)`: `raw/oeis-pe502/xrefs/A001263-tower.md` (`wiki/pages/tower-narayana-polynomial.md`),
  checked by `bin/python/tower_t_cores.py`.
  Michel Marcus asked (Oct 23) why the castles of width `n` with `m` blocks are not submitted
  as a new array: they are A271942 (bargraphs by semiperimeter and width) at
  `(n + m, n)`, since the semiperimeter is the width plus the blocks. Chaz Reid (#790–#791,
  Oct 23) added the formula `Sum_{k=1..n} T(n,k)*binomial(m+n-k-1, n-1) = A271942(n+m, n)`
  for `n, m >= 1` and `Cf. A005408, A005891, A063490, A160747, A271942.`, and answered in the
  discussion; back in proposed.
- [~] **A283595 column g.f.** (submitted 2026-10-23, #42–#43). One formula block: the g.f. of
  column `k` is `z^k/(R_k*R_{k+1})` with `R_{2j} = P_j − z*P_{j−1}`,
  `R_{2j+1} = P_{j+1} − z^2*P_{j−1}` (`P_k` of A097862), and the product form
  `R_k = Product_{i=1..k, i odd} (1 − (1 + 2*cos(i*Pi/(k+1)))*z)`; submitted without the proof
  line. `Column k=2 gives A094706(n-1).` and a Python program:
  `raw/oeis-pe502/xrefs/A283595-column-gf.md`, checked by `bin/python/a283595_column_gf.py`
  (`wiki/pages/1-smooth-castles.md` §3.2-3.3). The castle comment and the other formula lines
  are the first item of stage 3.

### 2. Ready to submit (drafted and checked, in order)

- [ ] **Reverse links**, one edit each, each adding only the lines shown. The first three
  point at approved entries; the last three answer the A001263 and A283595 edits, so they
  wait until those are approved.
  - [ ] **A003410 → A226136** (the link back for the approved A226136 edit, #29): the formula
    `a(n) = A226136(n) for n >= 4` and `Cf. A226136`. No castle comment: the castle's second
    row is Deutsch's binary word, so it would restate Deutsch's comment:
    `raw/oeis-pe502/xrefs/A226136-A003410.md` §"Edit 2"
    (`wiki/pages/fibonacci-castles-sub-families.md`).
  - [ ] A226274: `Cf. A226136.` (A226136's Cf. line cites A226274).
  - [ ] A038505: `Cf. A146559.` (`A146559 = A038503 − A038505`; A038503 and A146559
    already link both ways).
  - [ ] A271942: `Cf. A001263.` and `Columns k=2..5 give A005408(n-3), A005891(n-4),
    A063490(n-4), A160747(n-6).` (A001263's formula `= A271942(n+m, n)`; the width-2..5
    castle counts; checked against the A271942 b-file by `bin/python/tower_t_cores.py`).
  - [ ] A097862: `Cf. A283595.` (A283595's column g.f. is built from A097862's `P_k`).
  - [ ] A094706: `a(n) = A283595(n+1, 2) for n >= 1.` and `Cf. A283595.` (A283595's
    `Column k=2 gives A094706(n-1).`; checked by `bin/python/a283595_column_gf.py`).
- [ ] **A005408 3-cores by corners**: one comment, `a(n)` = 3-core partitions with `n`
  corners (Cho et al., Proposition 3.4, p. 14 "cc(3, m) = 2m + 1"), the Cho et al. link
  (after Hongwei Chen) and the t-core family Cf. line, which A160747 and A063490 already
  carry with A005408 as `t = 3`. The width-2 castle reading is left out: it is the `w = 2`
  case of `h^w − (h−1)^w`, which goes once on A047969: `raw/oeis-pe502/xrefs/A005408-tower.md`.
- [ ] **A001523 castles with as many blocks as rows**: one comment, the castles with `n` cells
  whose number of blocks equals their height are the stacks, since every row holds at least
  one block and exactly one when the column heights are weakly unimodal; the PE 502 link
  (after Flórez, Ramírez, and Villamizar): `raw/oeis-pe502/xrefs/A001523-castle.md`.
- [ ] **A115981 castles with more blocks than rows** (after or with A001523, which it
  refers to): the complementary comment and the PE 502 link (after Weisstein):
  `raw/oeis-pe502/xrefs/A115981-castle.md`.
- [ ] **New sequence `F(w,3)`**, the even-block castles of width `n` and height 3,
  `0, 0, 3, 21, 89, 307, …` (no match, nor for the odd-block companion, 2026-10-23): the
  factored g.f., the order-6 recurrence, `a(n) = (3^n − 2^(n+1) + A146559(n+1) +
  A107920(n))/2`, the width-3 example, a linear-time Python program from the definition,
  `Cf. A001047, A038505, A107920, A146559`. Standalone: the array (stage 3) can follow it:
  `raw/oeis-pe502/new-sequence-F3.md` (`wiki/pages/new-sequence-fw3.md`).

### 3. Needs a draft (verified, worth submitting; in submission order)

- [ ] **A283595 follow-up** (after #43 is approved): the castle comment, `T(n,k)` = castles
  of width `n+1` and height `k+1` whose first column is at height 1 and whose neighboring
  columns differ by at most 1 (column 2 is the Pell castles, A094706); and two formula lines,
  the column g.f. `z^k/(R_{2k+2}(z) + z^{k+1})`, since `R_{k+1} R_k = R_{2k+2} + z^{k+1}`
  (a product-to-sum identity for the Chebyshev polynomials of the first and third kinds), and
  for `k ≤ n ≤ 2k`, `T(n,k) = A027907(n,n+k) + A027907(n,n+k+1) − A027907(n,n+k+2) −
  A027907(n,n+k+3)` (the reflection principle with one reflection in the ceiling), checked
  against the castle counts that match the b-file for `k ≤ 11`, `n ≤ 22`
  (`wiki/pages/1-smooth-castles.md` §3.3, §3.7). Present the formulas without a novelty
  claim; bounded-height path g.f.s are classical.
  - [ ] **A283667 closed form** (a separate entry; it can go before the follow-up): the
    entry has only a recursion and an asymptotic, and `a(n) = A027907(2n,3n) +
    A027907(2n,3n+1) − A027907(2n,3n+2) − A027907(2n,3n+3)`, checked against all 24 terms
    of its data (2026-10-22; `wiki/pages/1-smooth-castles.md` §3.7).
- [ ] **A094706** (Convolution of Pell(n) and 2^n; the entry has no comments): the Pell
  castles (exact height 3, first column 1, neighboring columns differing by at most 1) of
  width `w` number `A094706(w − 2) = P⋆_w − 2^{w−1}` (`P⋆_w` the Pell numbers), proved by
  the g.f. `x³/((1−2x−x²)(1−2x))` (`wiki/pages/pell-castle.md`). The formula
  `a(n) = A283595(n+1, 2)` and `Cf. A283595` are in the stage-2 reverse links
  (`wiki/pages/1-smooth-castles.md`).
- [ ] **A077868**: two castle readings and the bijection between them. Spaced Fibonacci
  castles (height-2 columns at least 3 apart) of width `w` number `A077868(w − 1)`; tree
  castles of height 2 with area `A` (cells) number `A077868(A − 2)`; the domino-boundary map
  matches the Fibonacci castles with `w + 1` cells to the spaced castles of width `w`.
  Brute-force verified 2026-10-04
  (`wiki/pages/fibonacci-castles-sub-families.md`, `wiki/pages/tree-castle-by-area.md`).
- [ ] **A049703**: balanced Fibonacci castles of width `w` number `A005598(w)/2 = A049703(w)`
  (towers balanced, i.e. finite Sturmian); the entry is defined only as `A005598(n)/2`, with
  no combinatorial reading. Brute-force verified `w ≤ 15`, 2026-10-04
  (`wiki/pages/fibonacci-castles-sub-families.md`).
- [ ] **A106514**: the 1-smooth castles of exact height 3 (free first column) of width `w`
  number `A106514(w − 1)`, g.f. `x(1−x)/((1−2x)(1−2x−x²))`, proved; the entry has
  only convolution and eigensequence comments (`wiki/pages/pell-castle.md`). The same
  castles are the Mersenne castles of height 3, whose neighboring heights are in ratio 1, 2
  or 3/2 (a unison, an octave or a fifth), since on the heights 1, 2, 3 those are the steps
  of at most 1 (`wiki/pages/mersenne-castles.md`); the comment can give both readings.
- [ ] **The PE 502 count `F(w,h)` as an array, and its column `w = 3`** (OEIS rolls a
  two-parameter family into one array entry, with notable rows and columns as their own
  entries, cf. A217883 "Column 2 is A202882(n+1)"; the row `h = 3` is in stage 2). In order:
  - [ ] **Array `F(w,h)`**: even-block castles of width `w` and exact height `h`, square
    array read by antidiagonals (keyword `tabl`), with the general formula
    `F(w,h) = ½[h^w − (h−1)^w + P(h−2,w) − P(h−1,w)]`, the PE 502 link, the table in the
    Example section, and Cf. the all-parity array A047969 (`h^w − (h−1)^w`; A343237 is its
    transpose), row 2 = A038505(w+1) and row 3 = the stage-2 `F(w,3)` entry. Not on OEIS in
    either antidiagonal order (searched
    2026-10-04). **Draft not written.**
  - [ ] **Column `w = 3`, `F(3,h)`** = `0, 6, 3, 31, 10, 76, 21, 141, 36, 226, …`: `C(h,2)` at
    odd `h`, `5·C(h,2) + 1` at even `h` (`wiki/pages/sum-of-three-cubes-castles.md`). No match
    (searched 2026-10-04). **Draft not written.** The halves and the odd-block column, for
    the draft: the odd half is `F(3, 2m+1) = A014105(m)` (second hexagonal numbers); the
    even half is `F(3,2m) = 10m^2 − 5m + 1` (`6, 31, 76, 141, …`, no match 2026-09-20); and
    `odd(3, 2n+1) = A080860(n)` (`10n^2 + 5n + 1`), an interlink.
- [ ] **Tower-spacing new sequences** (`wiki/pages/tower-spacing-castles.md`): the six
  unfiled cells `(h,g)` for `h in {5,6}`, `g in {4,5,6}` (Hardin's "0..(h-1) arrays, each
  element the minimum of `g` adjacent elements", never filed at these parameters; no match
  2026-09-20).
- [ ] **Tower-spacing table comments**: one comment each on the tables A217839 / A217883 /
  A217954 / A228461 giving the castle reading and the running-minimum proof (A217839 is the
  row `h = 2`). The twenty matched cells, with `(h, g) = (2, 7)` = A217838, are covered by
  the tables, so no per-cell comments (`wiki/pages/tower-spacing-castles.md`).

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
  (the *Search record* at the end of this file, "Other rows"):
  - **The `F(w,h)` array:** rows `F(w,4)`, `F(w,5)`, `F(w,6)`; the odd-block rows
    `odd(w,3)`, `odd(w,4)` and `odd(w,h≥3)` generally; the column `F(4,h)` (`0, 10, 21,
    117, 122, 448, …`); further rows and columns. Searched rows and columns: no match
    2026-10-04. The `w = 3` column facts are under stage 3.
  - **Area:** the parity-refined area sequences (`cev+cod = A001523`), `strict_vee`.
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
  stage-3 `w = 3` column item. Open question: a separate comment on this dense entry, or
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

- [ ] **A388547 castle comment** (`wiki/pages/golden-silver-bronze-plastic-castles.md`,
  `wiki/pages/semi-perimeter-growth-census.md`): for `k ≥ 2`, `T(n, k)` is the number of
  castles of height `k` whose columns all have height 1 or `k`, with semi-perimeter `n + 1`
  (width plus blocks): delete the bottom row and lengthen each run of height-`k` columns by
  `k − 1`. Column 2, `A077855(n − 2)`, is then all castles of height 2 by semi-perimeter, and
  columns 3 and 4 are A130578 and A209231. None of the four entries states a castle reading
  (read 2026-10-26). Checked against enumeration for every row `n ≤ 12` of the data. One
  comment on the table, as for the tower-spacing tables.

- [ ] **Mersenne castles** (`wiki/pages/mersenne-castles.md`): castles whose neighboring
  heights are in ratio 1, 2, 3/2 or 4/3, or the inverse. The count at height `h` equals the
  count at `h₀`, the largest divisor of `h` of the form `2^a 3^b`, so the family is the rows
  `h₀ = 4, 6, 8, 9, 12, …` (heights 2 and 3 are A000225 and A106514). The row `h₀ = 4`,
  `1, 5, 21, 79, 281, 965, 3239, 10703, …`, brings its own g.f.
  `x(1 − x)/((1 − 2x − x²)(1 − 4x + 2x² + 2x³))` and grows at `3.17008…`, the largest root of
  `x³ − 4x² + 2x + 2`. No row, parity split, signed row or growth constant has a match
  (searched 2026-10-28; *Search record*). Open questions: one entry for the `h₀ = 4` row, or
  an array over `(w, h₀)` (the array over `(w, h)` repeats its rows); whether the rows
  `h₀ ≥ 6` have g.f.s short enough to state; and whether `ρ_cons(4)` is worth a constant entry.

**Skipped (assessed, with reason):**

- A048004 / A000100 / A000102 / A006979 / A006980 (the castles of area `n` and exact height
  `h`, `T(n − 1, h − 1)`, and the columns `h = 3, …, 6`): every entry already counts the
  compositions of `n` by largest part, which are the castles by area (A048004:
  "Equivalently, number of compositions of n+1 having largest part (exactly) k+1"; A006980
  is the 6th column of A048004).
- A000225 / A002662 / A002664 / A001792 (the towers of height at most 1 with at least 1, 2
  and 3 blocks, and their total block count): dense binomial-sum entries, and A002664 and
  A001792 already state the run readings ("at least three runs of ones", "the number of runs
  of consecutive 1's in all binary sequences of length (n+1)"), which are the towers' block
  counts.

- A000129 / A001333 / A171842 (the Pell castle strip under its three boundary conditions):
  dense entries, and a strip need not reach its ceiling, so it is not a castle family; the
  castle readings go on A094706, A106514 and A283595 (the castles of exact height 3). A171842
  already has the equivalent "Motzkin n-paths of height <= 2" reading.
- A001519 / A057960 / A085810 (anchored 1-smooth strips with ceilings 4, 5, 6) and A007482 /
  A015530 / A015537 (anchored m-smooth strips on the diagonal `h = m + 2`, `m = 2, 3, 4`):
  strips, not castle families, for the same reason; A057960 and A085810 already carry the
  equivalent corridor-path reading, and A001519 is dense. The castle readings go on A283595
  and the diagonal castle rows.
- A097862 castle comment (both end columns at height 1, neighboring columns differing by at
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
  words, Deutsch's compositions into 2s and 3s), and the rule is the wiki's own:
  `raw/oeis-pe502/xrefs/A000931-plastic-strip.md`.
- A000931 (maximal Fibonacci castles, `A000931(w + 6)`): the entry already counts the maximal
  independent sets of the path graph, which is the same statement.
- The signed convex castles (period 6) and the digits of `q_1` (no match): nothing to submit.
- A000930 (spaced castles, `A000930(w + 2) − 1`): the entry already has the "at least two
  zeros between successive ones" comment; A077868 is the better home.
- A003849 / A001950 / A003622 (the 56-column castle from the Fibonacci word): a single castle,
  not a sequence interpretation.
- A332578 (compositions whose negation is unimodal, the vee castles by area): the entry
  already defines them and links A001523; no castle statistic sets them apart (a vee castle
  has `c(1) + c(w) − min(c)` blocks), so a comment would rename the definition:
  `raw/oeis-pe502/xrefs/A332578-castle.md`.
- A003586 / A071521 (the heights `2^i 3^j ≤ h`, the class of height 1 under the consonance
  rule of the Mersenne castles, and their number): dense entries, and the class is the
  3-smooth numbers by definition, reached from 1 by octaves and fifths; A003586 already notes
  the music-theory history (de Vitry's harmonic numbers, the Pythagorean comma).

### Done (live on OEIS)

- [x] **A160747 castles of width 5 and 6-cores** (submitted 2026-10-16, approved: A160747 #62,
  Oct 22 2026, Sean A. Irvine). Comment block: 6-cores with `n` corners = castle polyominoes of
  width 5 with `n + 1` blocks (column heights `c(i) >= 1`, fixed Oct 18 after Alper Ferudun's
  note), with the 6-abacus bijection of Cho et al. Formula block:
  `Sum_{k=1..5} A001263(5,k)*binomial(n+5-k, 4)`, Cho et al.'s Prop. 3.4 sum,
  `a(n) = A271942(n+6, 5)`; the editor removed the words after the formulas, including the
  "row 5 of A001263" clause. The PE 502 link (placed after Haws, before the Index link, at
  Stefano Spezia's request), `Cf. A001263, A271942` and the t-core family line:
  `raw/oeis-pe502/xrefs/A160747-tower.md` (`wiki/pages/tower-narayana-polynomial.md`).
- [x] **A063490 castles of width 4 and 5-cores** (submitted 2026-10-16, approved: A063490 #66,
  Oct 22 2026, Sean A. Irvine). Comment block: 5-cores with `n − 1` corners = castle polyominoes
  of width 4 with `n` blocks, with the 5-abacus bijection; Jason Yuen tidied the comment block
  and moved the PE 502 reference from REFERENCES to LINKS (Oct 18). Formula block:
  `Sum_{k=1..4} A001263(4,k)*binomial(n+3-k, 3)`, Cho et al.'s Prop. 3.4 sum,
  `a(n) = A271942(n+4, 4)`; the editor removed the words after the formulas, including the
  "x times row 4 of A001263" clause. `Cf. A001263, A064788, A185505, A271942.` and the t-core
  family line: `raw/oeis-pe502/xrefs/A063490-tower.md`.
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
  terms and added keyword `easy`; the stray `a226136.txt` is deleted:
  `raw/oeis-pe502/xrefs/A226136-A003410.md`
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

---

## Search record (statuses of the castle sequences on the wiki)

The OEIS status of each castle sequence on `wiki/pages/castle-sequence-catalogue.md`, as last recorded: searches with no match (with their dates), near-misses, unsearched rows, and the entries that equal a castle count without stating the castle reading. The catalog section is given for each row; its terms and formulas are on the catalog page.

### Searched with no match, near-misses, unsearched

| catalog section | object | first terms | status as recorded |
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
| Mersenne castles | castles of height `h₀ = 4, 6, 8, 9, 12, 16, 18` (by `A_Mersenne(w, h) = A_Mersenne(w, h₀)` every height repeats the row of its `h₀`, and `h₀ = 1, 2, 3` give 1, A000225, A106514) | `h₀ = 4`: `1, 5, 21, 79, 281, 965, 3239, 10703, 34981, 113433` | **novel-candidate** (no match for any of the 7 rows, 2026-10-28); g.f. at `h₀ = 4` `x(1 − x)/((1 − 2x − x²)(1 − 4x + 2x² + 2x³))`, [[mersenne-castles](pages/mersenne-castles.md)] |
| Mersenne castles | even-block / odd-block, `h₀ = 3, 4, 6, 8, 9, 12, 16, 18` | `h₀ = 4`: `1, 5, 18, 56, 169, 523, 1671, 5421` / `0, 0, 3, 23, 112, 442, 1568, 5282` | **novel-candidate** (no match for any of the 16 rows, 2026-10-28); `h₀ = 3` is the parity split of the 1-smooth castles of height 3 with any first column |
| Mersenne castles | signed (even − odd), `h₀ = 3, 4, 6, 8, 9, 12, 16, 18` | `h₀ = 4`: `1, 5, 15, 33, 57, 81, 103, 139, 225, 377, 499, 303, −599` | **novel-candidate** (signed values for all 8 rows, absolute values for `h₀ = 3, 4, 9`, no match, 2026-10-28) |
| Mersenne castles | the array `A_Mersenne(w, h)` read by antidiagonals `w + h` | `1, 1, 1, 1, 3, 1, 1, 3, 7, 1, 1, 5, 9, 15, 1` | **novel-candidate** (no match, 2026-10-28); its rows repeat by the reduction to `h₀` |
| Mersenne castles | growth constants `ρ_cons(h₀)`, `h₀ = 4, 6, 8` | `3.17008648662…`, `3.64118647619…`, `3.9809365881…` | **novel-candidate** decimal expansions (no match, 2026-10-28); `ρ_cons(4)` is the largest root of `x³ − 4x² + 2x + 2`, `ρ_cons(6)` of `x⁴ − 5x³ + 4x² + 4x − 2` |
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
| Odd-block counts, parity-refined area, and joint block tables | even, odd, convex, vee, non-convex and strict-vee castles by area, split by parity, and their signed differences | on the page | **novel-candidate** (no match, 2026-09-26) |
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
| Other rows | The parity-refined sequences by area (even and odd; convex, vee, non-convex and strict-vee) ([[castle-by-area](pages/castle-by-area.md)]): **novel-candidate**, searched 2026-09-26; terms on [[odd-castles-and-block-tables](pages/odd-castles-and-block-tables.md)]. | - | (status in the text) |
| Other rows | The towers of width `w ≥ 6` by number of blocks `b` ([[tower-narayana-polynomial](pages/tower-narayana-polynomial.md)]): `w = 6`: `1, 21, 161, 721, 2331, 6083, …`; `w = 7`: `1, 28, 280, 1582, 6244, 19348, …` from `b = 0`: **novel-candidate** (no match, 2026-10-16). | - | (status in the text) |
| Other rows | The denominators of the Jacobi-Perron convergents of `2ψ²` ([[castle-eigenvalue-oeis-crosswalk](pages/castle-eigenvalue-oeis-crosswalk.md)]): `1, 1, 2, 4, 47, 53, 104, 204, 2409, 2717, 5330, …`: **novel-candidate** (no match, 2026-10-16). | - | (status in the text) |

### No match in the first mining pass (`raw/oeis-pe502/mine-notes.md`, `crosslink-avenues.md`, `vein9-area.md`)

- The rows `A^e(·, h)` for `h = 3, 4, 5` (recurrence orders 6, 9, 11) and the columns `A^e(w, ·)` for `w = 3, 4, 5`.
- The rows `A^o(·, h)` for `h = 3, 4, 5` (orders 5, 9, 11): "No OEIS match" (Vein 8).
- The block-count distribution of the castles of height `h ≥ 2`: "a new 2D table (no OEIS match)" (Vein 7).
- The towers by blocks, rows `w = 6, 7`: "new" (Tier 2).
- The castles by area split by block parity (even, odd, `cev`, `cod`: "four new sequences"), the strict-vee castles by area, `0, 0, 0, 0, 1, 3, 8, 17, 34, 60, 107, 175, 285, 445, 691, …` ("NEW sequence"), and "The 6 parity-refined variants ... are all new" (Veins 9, 9b).

### Equal to an entry that does not state the castle reading (interlinks)

| catalog section | object | entry, as recorded |
|---|---|---|
| Castles by area with bounded height: the n-nacci family | height 2 | **interlink** → [A000071](https://oeis.org/A000071) (`= A000071(n+1) = F_{n+1} − 1`) |
| Castles by area with bounded height: the n-nacci family | height at most 3 | **interlink** → [A000073](https://oeis.org/A000073) (`= A000073(n+2)`) |
| Castles by area with bounded height: the n-nacci family | height at most 4 | **interlink** → [A000078](https://oeis.org/A000078) (`= A000078(n+3)`) |
| Castles by area with bounded height: the n-nacci family | height at most 5 | **interlink** → [A001591](https://oeis.org/A001591) (`= A001591(n+4)`) |
| Castles by area with bounded height: the n-nacci family | height exactly 3 | **interlink** → [A000100](https://oeis.org/A000100) (`= A000100(n)`; compositions with largest part 3) |
| Castles by area with bounded height: the n-nacci family | height exactly 4 | **interlink** → [A000102](https://oeis.org/A000102) (`= A000102(n)`) |
| Castles by area with bounded height: the n-nacci family | height exactly 5 | **interlink** → [A006979](https://oeis.org/A006979) (`= A006979(n)`) |
| Castles by area with bounded height: the n-nacci family | height exactly 6 | **interlink** → [A006980](https://oeis.org/A006980) (`= A006980(n)`, offset 6) |
| Castles by area with bounded height: the n-nacci family | exact height, by `(n, h)` | **interlink** → [A048004](https://oeis.org/A048004) (`T(n − 1, h − 1)`, through the run reading: a column of height `c` as a run of `c − 1` 1s) |
| Tower-spacing skylines | `(h=2, g=2)` | **interlink** → [A005251](https://oeis.org/A005251) (`= A005251(w+3)`; the section *Multi-interpretation hub*) |
| Tower-spacing skylines | `(h=3, g=2)` | **interlink** → [A202882](https://oeis.org/A202882) (`= A202882(w+1)`; Hardin) |
| Tower-spacing skylines | `(h=4, g=2)` | **interlink** → [A203094](https://oeis.org/A203094) (`= A203094(w+1)`; Hardin) |
| Tower-spacing skylines | `(h=5, g=2)` | **interlink** → [A203184](https://oeis.org/A203184) (`= A203184(w+1)`; Hardin) |
| Tower-spacing skylines | `(h=6, g=2)` | **interlink** → [A203050](https://oeis.org/A203050) (`= A203050(w+1)`; Hardin) |
| Tower-spacing skylines | `(h=2, g=3)` | **interlink** → [A005252](https://oeis.org/A005252) (`= A005252(w+3)`) |
| Tower-spacing skylines | `(h=2, g=4)` | **interlink** → [A005253](https://oeis.org/A005253) (`= A005253(w+3)`) |
| Tower-spacing skylines | `(h=2, g=5)` | **interlink** → [A005689](https://oeis.org/A005689) Twopins positions (`= A005689(w+6)`) |
| Tower-spacing skylines | `(h=2, g=6)` | **interlink** → [A098574](https://oeis.org/A098574) (`= A098574(w+6)`) |
| Tower-spacing skylines | `(h=2, g=7)` | **interlink** → [A217838](https://oeis.org/A217838) (`= A217838(w)`; 0..1 arrays, "minimum of 7 adjacent elements") |
| Tower-spacing skylines | the row `h = 2`, by `(w, g)` | **interlink** → [A217839](https://oeis.org/A217839) (`T(w, g) = spacing_g(w, 2)`; Hardin's 0..1 minimum-filter table) |
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
| Mersenne castles | castles of height 3, the 1-smooth castles of height 3 with any first column | **interlink** → [A106514](https://oeis.org/A106514) (`= A106514(w − 1)`; the entry has neither the 1-smooth nor the consonance reading, 2026-10-28) |
| Ridge strips and ridge castles | ridge strips, `h = 3` | **interlink** → [A001333](https://oeis.org/A001333) Pell-Lucas numbers (`= A001333(w+1)`) |
| Ridge strips and ridge castles | ridge strips, `h = 4` | **interlink** → [A003688](https://oeis.org/A003688) (`= A003688(w+1)`) |
| Ridge strips and ridge castles | ridge strips, `h = 5` | **interlink** → [A015448](https://oeis.org/A015448) (`= A015448(w+1) = F_{3w+2}`) |
| Signed tower count P(k, ·) rows | `P(1, L)` | **interlink** → [A146559](https://oeis.org/A146559) (`= A146559(L+1) = Re((1+i)^{L+1})`) |
| Castles by semi-perimeter | all castles (bargraphs) | **interlink** → [A082582](https://oeis.org/A082582) (`= A082582(s)`, bargraphs by semi-perimeter; no castle reading, 2026-10-16) |
| Castles by semi-perimeter | castles by `(s, w)` | **interlink** → [A271942](https://oeis.org/A271942) (rows checked for `s ≤ 16`; the entry does not give the Narayana form) |
| Castles by semi-perimeter | castles of height 2 | **interlink** → [A077855](https://oeis.org/A077855) (`= A077855(s − 3)`; binary words whose runs of 0s are all at least 2 long; no castle reading, 2026-10-26) |
| Castles by semi-perimeter | height 3, every column 1 or 3 | **interlink** → [A130578](https://oeis.org/A130578) (`= A130578(s − 1)`; crossword rows) |
| Castles by semi-perimeter | height 4, every column 1 or 4 | **interlink** → [A209231](https://oeis.org/A209231) (`= A209231(s − 1)`) |
| Castles by semi-perimeter | height `h`, every column 1 or `h`, by `(s, h)` | **interlink** → [A388547](https://oeis.org/A388547) (`T(s − 1, h)` for `h ≥ 2`) |
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
