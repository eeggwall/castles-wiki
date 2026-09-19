# Plan: restructure IDEAS.md into a program document (seminar layer over Divisions)

## Context

The wiki is at 106 pages (30 Sources, 51 Concepts, 25 Analyses), built in six days (2026-09-13 to 09-18).
`IDEAS.md` has been the driver for most of the Analyses, but it has drifted from a plan into a results ledger:

| Symptom | Evidence |
|---|---|
| Done items dominate | 49 of 74 checkboxes are `[x]`; the file is 6,045 words and the twelve longest items (150-340 words each) are all `[x]` results that restate their wiki page |
| Open work is hidden | 8 `[x]` items carry a "Still open:" tail holding ~20 discrete open threads that have no checkbox of their own (Hardin involution appears in three of them) |
| Two trackers overlap | `TODO.md` "Research threads" duplicates the Q Division (q-equivalent) and holds four research items IDEAS lacks: convex/valley bijection, Knuth generation algorithms seminar, Viennot heaps, castle recurrences vs A001169 / stack-Ferrers-parallelogram sub-families |
| Divisions are uneven | Enumeration 16/16 done, Numbers 22/26, Classification 4/5, S 5/10, Q 0/3, T 0/6, Misc 0/6 |
| "Seminar" has no home | 20 pages use the word in five senses (series, centerpiece, master class, algorithmic seminar, "seminar-shaped"); nothing lists the seminar program, though seminars are the wiki's stated mission in SCHEMA.md and overview.md |
| IDEAS is not a map | 48 of 106 pages are never referenced from IDEAS (all 30 Sources plus foundational Concepts). That is fine, but the file should say so and point to `wiki/index.md` / `overview.md` for the map |

User decisions (2026-09-19): keep the Divisions and add a seminar layer on top; collapse every `[x]` item to one line; fold TODO's research threads into IDEAS and leave TODO with OEIS submissions, ingestion queue, housekeeping; no new wiki page.

## Target shape of `IDEAS.md`

```
# Project and Seminar Ideas
  intro (3-4 lines) + conventions
## Where we are (2026-09-19)          <- 6-line snapshot table
## Seminar program                    <- NEW layer: ~10 arcs, one block each
## Divisions                          <- kept; every item tagged with its arc
   ### Numbers Division
   ### Enumeration Division
   ### Q Division
   ### S Division
   ### T Division
   ### Classification and Variations
   ### Miscellaneous
```

### 1. Intro and conventions (rewrite the two lines at the top)

- `[ ]` open, `[x]` has a page. Open items first, done items last, within each Division (unchanged).
- New: a done item is **one line**: `- [x] **[Title](wiki/pages/slug.md)** - one-sentence result.` The detail lives on the page and in git history.
- New: any open follow-up gets **its own `[ ]` item**; never a "Still open:" tail on a done item.
- New: every item ends with an arc tag like `(S2)` naming the seminar it feeds; `(-)` for items outside any arc.
- Pointer: this file drives new Analyses; the map of the whole wiki is `wiki/index.md` (generated) and `wiki/overview.md`.
- Use plain hyphens in new text, no em-dashes.

### 2. "Where we are" snapshot

One small table: pages by category (30/51/25), items open/done per Division after the restructure, and the three dates (wiki created 09-13, IDEAS created 09-14, last reorganize 09-16). Dated so it can be refreshed at the next introspection.

### 3. Seminar program (the new layer)

Each arc is one block: **title (a hook, not a theme)** - one-line thesis - status - spine pages in delivery order - open items (by Division tag). Statuses: `deliverable` (pages exist end to end), `one page short` (spine exists, the seminar-shaped page does not), `sketch` (ideas only).

| # | Arc title | Status | Spine pages (in order) | Open items feeding it |
|---|---|---|---|---|
| S1 | The castle counted on one blackboard | deliverable | tower-recursion-master-class, castle-sign, parity-via-roots-of-unity, castles-as-upgraded-cycle-count, kitamasa, berlekamp-massey, castle-count-algorithms | Misc: general closed form for P(k,L); minimality of recurrence orders |
| S2 | From a textbook exercise to the metallic ladder | deliverable | pell-castle-strip, castle-strip, metallic-means, eigenvalue-continued-fractions, metallic-strip-realizability, reachable-field-census, proper-castle-projection, bounded-height-castles-nacci, plastic-number | Numbers: silver-ratio observatory, larger-prime periodicity, min-height law for (p1,p2), Pisot/Salem cubics, horizontal-gap census (from tower-spacing) |
| S3 | The Hardin word identity | one page short | tower-parity-sectors, hardin-word-identity, a005251-bijection, tree-castle-by-area, tetali-1998-unique-tournaments | Numbers: the centerpiece itself (existing item), sign-reversing involution, two sector-assignment conjectures, h>=5 tree-castle sequences |
| S4 | Hear the shape of a castle | one page short | spectral-analysis, castle-graph, castle-graph-spectral-radius, isospectral-castles | S: centerpiece (existing item), bronze hunt, skyline DFT, LGV kernel, Ihara zeta, Sunada construction for the 10-cell pair |
| S5 | Castle cryptography: build, break, fix | deliverable (run twice) | castle-cryptography, castle-cryptography-ring, castle-cryptography-number-theory, castle-cryptography-round-two | Numbers: round-three torus on char_5, shrinking-generator castle, the two d=3 linear-complexity deficits |
| S6 | The q-thread: castles by area | half built | castle-by-area, convex-castle-binomial-identity, weakly-unimodal-composition, stack-polyomino-gf, tree-castle-by-area, bounded-height-castles-nacci, q-catalan-numbers, steep-polyominoes-q-motzkin-bessel | Q: prime castles, q-polyomino zoo (absorbs TODO stack/Ferrers and A001169 threads), q-Catalan/q-Motzkin joins (absorbs TODO q-equivalent), convex/valley bijection (from TODO), h=3 tree-vs-all bijection |
| S7 | OEIS mining as a research method | deliverable | oeis-cross-referencing, oeis-mining-pe502, oeis-index, oeis-height2-hyperbolic-castles, convergents-oeis-crosswalk, new-sequence-fw3 | Numbers: castle sequence bank residue; OEIS id of tower-spacing 2D sequences and bounded-height rows. Submissions stay in TODO.md (human action) |
| S8 | One bit: the parity clause as information | one page short | castle-entropy, castle-compression, castle-sign | Enumeration: conditional entropy given block count/area; rule-generated-castle detector; does the parity bit survive object by object |
| S9 | pi from a pile of blocks | sketch | algebraic-transcendental-wall (the wall), spectral-analysis (LGV hook) | T: all six items; prerequisite item: a `castle-samplers` page (currently a parenthetical in the T header, promote to `[ ]`) |
| S10 | Knuth's algorithms in castle space | sketch | aocp-generating-permutations-tuples, project-euler-502-brute-force, castle-snippets | Enumeration: castle Gray code / loopless enumerator (from TODO), Viennot heap theory via tower-heap (from TODO) |
| S11 | The rule zoo: variations on the castle | mixed | castle-classification, castle-snippets, tower-spacing-castles, castle-representations | Classification: rule-variation enumeration; Misc: higher-dimensional castles, convex core uniqueness, statistical physics links, convex/unimodal exact enumeration with parity |

Arc titles are hooks (a titled subplot), not division names. Adjust wording during execution but keep them as titles.

### 4. Divisions (kept, edited)

For every Division, in place:

1. **Collapse each `[x]` item** to one line (title link + one sentence). Representative before/after, `reachable-field-census` (337 words -> ~30):
   `- [x] **[Reachable-field census](wiki/pages/reachable-field-census.md)** - which number fields host castle-strip Perron roots, h<=5 exhaustive, h>=6 by the (p1,p2) reachability law; every real quadratic field is reachable. (S2)`
2. **Promote every hidden follow-up** to its own `[ ]` item, placed in the open block of the same Division with the arc tag. The list to promote (source item in parentheses):
   - Numbers: min-height closed form for `(p1,p2)`; Pisot/Salem classification of reachable cubics (census). Round-three torus on `char_5`; shrinking-generator castle; two `d=3` deficits (cryptography). Sign-reversing involution for Hardin (appears in three items, becomes **one** item); two sector-assignment conjectures (hardin). `h>=5` tree-castle-by-area sequences; bijection between the two A005251 readings is closed by a005251-bijection, so drop it (tree-castle). Castle sequence bank stays open, trimmed.
   - Enumeration: conditional entropy; rule-generated detector; parity-bit object-by-object (entropy). Plus imports from TODO: Knuth generation algorithms / castle Gray code; Viennot heap theory.
   - Q: existing three, plus imports from TODO: convex/valley bijection; merge TODO's "castle recurrences vs A001169" and "stack/Ferrers/parallelogram sub-families" into the q-polyomino zoo item as sub-bullets; merge TODO's "find the q-equivalent" into the q-Catalan/q-Motzkin item.
   - S: h=3 bounded-height tree-vs-all bijective story (bounded-height item) fits better under Q (S6); Sunada construction and Ihara/DFT separation are already inside the centerpiece item, leave them there.
   - T: promote the `castle-samplers` page prerequisite from the header parenthetical to a `[ ]` item.
   - Classification: OEIS id of tower-spacing sequences; horizontal-gap reachable-field census; no-touching / vertical-spacing variants (gap-rule item). The first two are tagged S7 / S2 respectively.
3. **Tag every item** with its arc.
4. Keep Division intro paragraphs (S and T have them) but shorten T's to two lines once the samplers item exists.

### 5. `TODO.md`

- Delete the "Research threads (mathematics)" section. Replace with two lines: research and seminar ideas live in `IDEAS.md`; this file holds the human-action and pipeline checklists.
- Keep OEIS submissions, ingestion queue, housekeeping unchanged. Update the header paragraph to match.

### 6. Small pointer edits

- `README.md` Layout block: add `IDEAS.md` beside `TODO.md` with a one-line description (currently only TODO is listed).
- `wiki/overview.md` Status paragraph: the sentence "Open work is tracked in TODO.md: ... research threads (q-equivalent, convex⟺valley bijection, Viennot heaps)" should point research threads at `IDEAS.md` and leave OEIS/ingest at `TODO.md`. Bump `updated:`.

## Files touched

- `IDEAS.md` (rewrite in place, same filename)
- `TODO.md` (remove one section, edit header)
- `README.md` (one line)
- `wiki/overview.md` (one sentence + `updated:`)

## Verification

1. Every `wiki/pages/<slug>.md` link in the new IDEAS.md resolves: `grep -o 'wiki/pages/[a-z0-9-]*\.md' IDEAS.md | sort -u | while read f; do [ -f "$f" ] || echo MISSING $f; done` prints nothing.
2. Coverage did not shrink: the 58 pages linked before are still linked (diff the sorted link lists against `/tmp/ideas_linked.txt`), and the four TODO research items appear in IDEAS.
3. No done item exceeds ~40 words: `grep '^- \[x\]' IDEAS.md | awk '{ if (NF>45) print NF, substr($0,1,60) }'` prints nothing.
4. No "Still open" tails remain on `[x]` lines: `grep '^- \[x\]' IDEAS.md | grep -ci 'still open\|open follow\|remains open'` is 0.
5. Counts land near: open items ~45 (was 25), done ~49, total words ~2,500 (was 6,045). Every item carries an arc tag `(S1..S11|-)`.
6. Every arc in the Seminar program table names at least one existing page and at least one open item, or says `deliverable` with none.
7. `python3 bin/lint-mechanical.py --staged` passes for the `overview.md` edit (IDEAS/TODO/README are outside `wiki/pages/` and are not linted).
8. Commit: `git commit --no-gpg-sign` with subject `docs(IDEAS): add seminar layer over Divisions, collapse done items, absorb TODO research threads` and trailer `Wiki-Op: update`.
