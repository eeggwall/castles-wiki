# Castles wiki — open threads & TODO

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

- [~] **A038503 exact-height correction** (submitted 2026-10-04). The live comment says
  "height at most 2", which counts the `r = 0` term `C(n,0)` as a castle. Replaced with the
  exact-height statement `a(n) − 1` = odd-block castles of width `n−1` and height 2, same
  definition sentence as A038505: `raw/oeis-pe502/xrefs/A038503-exact-height.md`.
- [~] **A146559 castle comment** `a(n) = P(1, n−1)` (signed tower count at `k = 1`),
  submitted 2026-10-04 (resubmitted with the date as `Oct 04 2026`). Comment only, exact
  height: `a(n) − 1` = odd − even castles of height 2: `raw/oeis-pe502/xrefs/A146559-signed.md`
  (`wiki/pages/castle-sequence-catalogue.md`, `wiki/pages/signed-tower-count.md`).
- (third slot held open: A009545 goes in once the two above clear)

### 2. Ready to submit (drafted and checked, in order)

1. [ ] **A009545** (`Im((1+i)^n)`, e.g.f. `sin(x)exp(x)`): castle comment from the `k = 1`
   parity split, `A009545(w) = −P_odd(1,w)` = (even-block − odd-block castles of width `w`,
   exact height 2, last column at height 2); verified `w = 0..14` on 2026-10-04, no castle
   text on the live entry (#193, Jul 27 2026). Comment only; width `n`, no `− 1`:
   `raw/oeis-pe502/xrefs/A009545-signed.md` (`wiki/pages/signed-tower-count.md`,
   `wiki/pages/tower-parity-sectors.md`).
2. [ ] **Tower/heap = Narayana-polynomial interpretation** (formerly tier 2) on A005891 /
   A063490 / A160747, and the numerator formula on A001263 (`raw/oeis-pe502/xrefs/*-tower.md`;
   `wiki/pages/tower-narayana-polynomial.md`). The A063490 draft notes an offset shift.
3. [ ] **Dense-entry synonyms** (formerly tier 3) A001523 / A332578 / A115981
   (`raw/oeis-pe502/xrefs/*-castle.md`).
4. [ ] **New sequence `F(w,3)`** (`raw/oeis-pe502/new-sequence-F3.md`;
   `wiki/pages/new-sequence-fw3.md`). Re-searched oeis.org 2026-09-19: still no match.

### 3. Needs a draft (verified, worth submitting)

- [ ] **A077868** (planned for the week of 2026-10-05): two castle readings and the bijection
  between them. Spaced Fibonacci castles (height-2 columns at least 3 apart) of width `w`
  number `A077868(w − 1)`; tree castles of height 2 with area `A` (cells) number
  `A077868(A − 2)`; the domino-boundary map matches the Fibonacci castles with `w + 1`
  cells to the spaced castles of width `w`. Brute-force verified 2026-10-04
  (`wiki/pages/fibonacci-castles-sub-families.md`, `wiki/pages/tree-castle-by-area.md`).
- [ ] **A000071** (planned for the week of 2026-10-05): the Fibonacci castles of width `w`
  number `F_{w+2} − 1`, the term `A000071(w+2)`; castles of height 2 with area `A` number
  `F_{A+1} − 1`, the term `A000071(A+1)`. Brute-force verified 2026-10-04
  (`wiki/pages/fibonacci-castle.md`, `wiki/pages/castle-graph.md`).
- [ ] **A049703**: balanced Fibonacci castles of width `w` number `A005598(w)/2 = A049703(w)`
  (towers balanced, i.e. finite Sturmian); the entry is defined only as `A005598(n)/2`, with
  no combinatorial reading. Brute-force verified `w ≤ 15`, 2026-10-04
  (`wiki/pages/fibonacci-castles-sub-families.md`).
- [ ] **Difference-of-powers fillers** (formerly tier 3) A000225, A001047, … (`h^w − (h−1)^w`
  all castles of exact height `h`).
- [ ] **New-sequence siblings** of `F(w,3)`: `F(w,4)`, `F(w,5)`, `odd(w,h≥3)`, parity-refined
  area sequences (`cev+cod = A001523`), `strict_valley`, tower rows `w≥6`, and the `P(k,·)`
  families for `k≥2`. Also the fixed-width columns from `wiki/pages/sum-of-three-cubes-castles.md`:
  new sequence `F(3,2m) = 10m^2-5m+1` (`6, 31, 76, 141, …`, no match 2026-09-20) and the
  interlink `odd(3,2n+1) = A080860(n)`.
- [ ] **Tower-spacing table** (`wiki/pages/tower-spacing-castles.md`): the six unfiled cells
  `(h,g)` for `h in {5,6}`, `g in {4,5,6}` as new sequences (Hardin's "0..(h-1) arrays, each
  element the minimum of `g` adjacent elements", never filed at these parameters; no match
  2026-09-20), and one comment each on the nineteen matched cells and the tables
  A217883 / A217954 / A228461 giving the castle reading and the running-minimum proof.

### 4. Candidates (found on the wiki, not yet assessed)

Each gets a verdict: submit (move to stage 3) or skip (move to "Skipped", with the reason).

- [ ] **`(d, k)`-RLL Fibonacci castle counts** for `(1,3)`, `(1,7)`, `(2,7)`, `(2,10)`
  (`1, 2, 4, 7, 10, 15, 22, 32, …` for `(1,3)`; the rest on
  `wiki/pages/fibonacci-castles-sub-families.md`): search OEIS; interlink if matched, new
  sequence if not.

**Skipped (assessed, with reason):**

- A000931 (maximal Fibonacci castles, `A000931(w + 6)`): the entry already counts the maximal
  independent sets of the path graph, which is the same statement.
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
