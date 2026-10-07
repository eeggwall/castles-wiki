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

OEIS requires human authorship; the drafts are checked starting points to reword and
sign, not to submit verbatim. OEIS allows **3 open edits at a time**, and each takes a
while to review, so the queue runs as a pipeline: when a review slot opens, submit the top
item of "Ready to submit". Keep stages 2-4 stocked while waiting. Signatures use a
two-digit day (`Oct 04 2026`). See `wiki/pages/oeis-cross-referencing.md`; the
mathematical status of each sequence (known / interlink / novel-candidate / unchecked)
lives on `wiki/pages/castle-sequence-catalogue.md`.

### 1. In review (max 3)

- [~] **A146559 castle comment** `a(n) = P(1, n−1)` (signed tower count at `k = 1`),
  submitted 2026-10-04 (resubmitted with the date as `Oct 04 2026`). Comment only, exact
  height: `a(n) − 1` = odd − even castles of height 2: `raw/oeis-pe502/xrefs/A146559-signed.md`
  (`wiki/pages/castle-sequence-catalogue.md`, `wiki/pages/signed-tower-count.md`).
- [~] **A009545 castle comment** (submitted 2026-10-06). Comment only, width `n`, no `− 1`:
  `a(n)` = even-block − odd-block castles of width `n` and height 2 whose last column reaches
  height 2, for `n >= 1`, with the PE 502 citation; the optional runs sentence was dropped for
  length: `raw/oeis-pe502/xrefs/A009545-signed.md` (`wiki/pages/signed-tower-count.md`,
  `wiki/pages/tower-parity-sectors.md`).
- [~] **A226136 → A003410** (submitted 2026-10-06). Formula line "Conjecture: a(n) =
  A003410(n) for n >= 4", equivalent to Barker's conjectured g.f. (A003410's g.f. minus
  `1 + x + x^2 + x^3`), and `Cf. A003410`: `raw/oeis-pe502/xrefs/A226136-A003410.md`
  (`wiki/pages/fibonacci-castles-sub-families.md`).

### 2. Ready to submit (drafted and checked, in order)

1. [ ] **Tower/heap = Narayana-polynomial interpretation** (formerly tier 2) on A005891 /
   A063490 / A160747, and the numerator formula on A001263 (`raw/oeis-pe502/xrefs/*-tower.md`;
   `wiki/pages/tower-narayana-polynomial.md`). The A063490 draft notes an offset shift.
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
   entry's rows 0-8 and as an identity for `k ≤ 11` (2026-10-06). **Before drafting:** read
   Finch, arXiv:1802.04615 (linked from the entry) to see whether the column g.f. is already
   there, and cite it if so (`wiki/pages/1-smooth-castles.md` §3.2-3.3, §3.5).
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
- A005408 (towers of width 2): its draft recommends skipping by default (dense entry, marginal
  reading); `raw/oeis-pe502/xrefs/A005408-tower.md`.

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
