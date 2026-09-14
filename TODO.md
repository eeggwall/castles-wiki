# Castles wiki — open threads & TODO

A running tracker of open research threads and pending actions for the PE 502 castles
wiki. This is a **hand-maintained** file (not a generated artifact and not a wiki page —
it lives at the repo root, outside `wiki/pages/`, so it does not appear in the index).
The authoritative discussion of each thread lives on the linked wiki page; this file is
the checklist view.

Convention: `[ ]` open · `[~]` in progress · `[x]` done. Link wiki pages as
`wiki/pages/<slug>.md`.

---

## Research threads (mathematics)

- [ ] **Find the q-equivalent — a q-graded (area-tracking) castle count.** The recurring
  "next step." The castle is counted cleanly by *area* (`wiki/pages/castle-by-area.md`:
  convex ↔ A001523); grading that count by `q` is the natural way the castle meets the
  q-analog world. Anchors: q-Motzkin appears in the q-grammar count of steep Dyck words
  (`wiki/pages/motzkin-numbers.md`), q-Catalan (Polya/Gessel) count parallelogram
  polyominoes by area (`wiki/pages/q-catalan-numbers.md`), and Ferrers-polyomino area
  g.f.s relate to q-Bessel / q-Catalan (`wiki/pages/polyominoes.md`). The steep-polyomino
  paper's q-Bessel-ratio generating function is the template
  (`wiki/pages/steep-polyominoes-q-motzkin-bessel.md`).

- [ ] **Convex ⟺ valley bijection.** Convex and valley castles are equinumerous in every
  `(w,h)` cell (both `C(2h+w−3, w−1)`, different sets) under a peak↔valley mirror. Write
  up the explicit bijection. See `wiki/pages/castle-by-area.md`,
  `wiki/pages/convex-castle.md`.

- [ ] **Knuth's generation algorithms in castle space (seminar candidate).** Translate
  TAOCP Vol. 4 combinatorial-generation algorithms into the castle's mixed-radix `{1..h}^w`
  space. Algorithm M (mixed-radix add-one) is already the castle brute-force; a **castle
  Gray code** would change one column height by one per step (bounded block-count / sign
  deltas → a loopless enumerator, incremental `P`/parity updates). The twist Knuth's generic
  algorithms don't handle: restricting to *valid* castles (exact max height *h*, even-block
  filter). Accessible, self-contained, good for external collaborators.
  See `wiki/pages/aocp-generating-permutations-tuples.md`.
- [ ] **Viennot heap theory.** The tower is a heap of pieces
  (`wiki/pages/tower-heap.md`); its block-count Narayana structure invites the
  commutation-monoid / transfer-matrix machinery. Untraced.

- [ ] **Castle recurrences vs. the outside literature.** Do the castle's C-finite
  recurrences relate to A001169 (horizontally convex polyominoes,
  `wiki/pages/counting-horizontally-convex-polyominoes.md`) or to the add-a-column
  functional equations of `wiki/pages/column-convex-polygon-enumeration.md`?

- [ ] **Stack / Ferrers / parallelogram ↔ castle sub-families.** Do the classical
  directed-convex families correspond to castle sub-families? (`wiki/pages/polyominoes.md`,
  `wiki/pages/column-convex-polygon-enumeration.md`.)

## OEIS submissions (human action — drafts in `raw/oeis-pe502/`)

OEIS requires human authorship; the drafts below are checked starting points to reword
and sign, not to submit verbatim. New contributors are throttled — lead with tier 1.
See `wiki/pages/oeis-cross-referencing.md`.

- [ ] **Tier 1 (submit first):** A038505 / A038503 / A146559 — the height-2 hyperbolic
  interlink (`raw/oeis-pe502/oeis-xref-draft.md`;
  `wiki/pages/oeis-height2-hyperbolic-castles.md`). Add the `Cf. A000225` link.
- [ ] **Tier 2:** tower/heap = Narayana-polynomial interpretation on A005408 / A005891 /
  A063490 / A160747, and the numerator formula on A001263
  (`raw/oeis-pe502/xrefs/*-tower.md`; `wiki/pages/tower-narayana-polynomial.md`).
- [ ] **Tier 3:** difference-of-powers fillers (A000225, A001047, …) and the dense-entry
  synonyms A001523 / A332578 / A115981 (`raw/oeis-pe502/xrefs/*-castle.md`).
- [ ] **New sequence:** `F(w,3)` (`raw/oeis-pe502/new-sequence-F3.md`;
  `wiki/pages/new-sequence-fw3.md`). Then siblings: `F(w,4)`, `F(w,5)`, `odd(w,h≥3)`,
  parity-refined area sequences (`cev+cod = A001523`), `strict_valley`, tower rows `w≥6`,
  and the `P(k,·)` families for `k≥2`.

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
- [ ] (Deferred) The general **Generating Functions** topic page (distinct from
  AOCP/Generating Functions) — the concept page `wiki/pages/generating-functions.md` is
  seeded; this standalone source is still queued.
- [ ] **Dyck Words/Examples** — worked enumeration examples (by hand, Python, SymPy) for
  Dyck and steep Dyck words; referenced by Castle Factoring. Newly surfaced.
- [ ] **Dyck Words/Lisp** — Dyck words as Lisp S-expression skeletons. Newly surfaced.
- [ ] **AOCP/Multisets** — referenced by AOCP/Combinatorics and Lattice Paths; the
  multiset-permutation / multichoose machinery. Newly surfaced.
- [x] **Generating Functions** (general topic page) — done
  (`wiki/pages/generating-functions-topic.md`). Sedgewick–Flajolet/Trotter reference with
  an explicit PE 502 application; the imaginary-roots / EGF-parity / every-4th-term examples
  are the same operations the castle uses.
- [ ] **Combinatorics** — the general umbrella topic page (distinct from AOCP/Combinatorics).

## Housekeeping

- [ ] Add a short setup note / README for collaborators: MCP config paths in `.mcp.json`
  are machine-specific; the `assets/` PDFs are git-ignored and re-fetchable from
  charlesreid1.com; after a fresh clone re-run `git config core.hooksPath bin/hooks`.
- [x] Remote for backup/sharing — done. `origin` → github.com/eeggwall/castles-wiki
  (SSH); `main` tracks `origin/main`.
