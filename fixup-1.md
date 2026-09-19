I read all 15 pages and checked the formulas by hand and by computation. The selection was by total link degree (in-links plus
out-links) over the 106 pages.

  ┌────────────────────────────┬─────┬─────┬───────┬──────────────────────────────────────────────┐
  │            page            │ in  │ out │ words │                   verdict                    │
  ├────────────────────────────┼─────┼─────┼───────┼──────────────────────────────────────────────┤
  │ castle-snippets            │ 21  │ 46  │ 8,760 │ split; pinned outputs not all true           │
  ├────────────────────────────┼─────┼─────┼───────┼──────────────────────────────────────────────┤
  │ castle-counting-formula    │ 40  │ 19  │ 2,148 │ sound core; one grafted paragraph is wrong   │
  ├────────────────────────────┼─────┼─────┼───────┼──────────────────────────────────────────────┤
  │ oeis-index                 │ 8   │ 49  │ 4,539 │ split directory from catalogue               │
  ├────────────────────────────┼─────┼─────┼───────┼──────────────────────────────────────────────┤
  │ castle-classification      │ 20  │ 33  │ 5,618 │ split; several stale or ill-posed statements │
  ├────────────────────────────┼─────┼─────┼───────┼──────────────────────────────────────────────┤
  │ castle-sign                │ 34  │ 15  │ 1,116 │ correct; tighten                             │
  ├────────────────────────────┼─────┼─────┼───────┼──────────────────────────────────────────────┤
  │ oeis-mining-pe502          │ 31  │ 18  │ 997   │ fine                                         │
  ├────────────────────────────┼─────┼─────┼───────┼──────────────────────────────────────────────┤
  │ signed-tower-count         │ 31  │ 15  │ 917   │ correct; one wording error                   │
  ├────────────────────────────┼─────┼─────┼───────┼──────────────────────────────────────────────┤
  │ convex-castle              │ 25  │ 16  │ 1,378 │ correct; duplicated paragraphs               │
  ├────────────────────────────┼─────┼─────┼───────┼──────────────────────────────────────────────┤
  │ project-euler-502-solution │ 23  │ 18  │ 1,505 │ good; stale housekeeping                     │
  ├────────────────────────────┼─────┼─────┼───────┼──────────────────────────────────────────────┤
  │ generalized-dyck-grammar   │ 25  │ 15  │ 1,573 │ cleanest of the 15                           │
  ├────────────────────────────┼─────┼─────┼───────┼──────────────────────────────────────────────┤
  │ generating-functions       │ 24  │ 14  │ 1,355 │ ok; one wrong claim                          │
  ├────────────────────────────┼─────┼─────┼───────┼──────────────────────────────────────────────┤
  │ castle-polyomino           │ 26  │ 10  │ 728   │ expand                                       │
  ├────────────────────────────┼─────┼─────┼───────┼──────────────────────────────────────────────┤
  │ castle-representations     │ 22  │ 14  │ 1,572 │ good                                         │
  ├────────────────────────────┼─────┼─────┼───────┼──────────────────────────────────────────────┤
  │ castle-counting-function   │ 21  │ 14  │ 1,039 │ good                                         │
  ├────────────────────────────┼─────┼─────┼───────┼──────────────────────────────────────────────┤
  │ convergents-oeis-crosswalk │ 14  │ 20  │ 7,094 │ split off Part 3                             │
  └────────────────────────────┴─────┴─────┴───────┴──────────────────────────────────────────────┘

The one real mathematical error, and how far it spread

The Pell castle strip story is false as a statement about Project Euler 502 castles. The claim is that the denominator of 1/(1 − 2x
− x²) splits along the castle rules: the 2x term is the per-column binary state of a height-2 tower and the x² term is the
"mandatory-gap tax" of rule 3, so Pell numbers count height-2 castle strips under rule 3. Three independent checks say otherwise.

- Height-2 castles are counted by exactly 2^w. I enumerated skylines with heights in {1,2} under the actual rules. Counts for widths
  1 to 7 are 2, 4, 8, 16, 32, 64, 128. Pell gives 1, 2, 5, 12, 29, 70, 169. Rule 3 costs nothing because blocks are maximal runs,
  so the gap is automatic. The wiki's own generalized-dyck-grammar page says this ("No-overhang needs no separate rule").
- The k=1 member of the wiki's recurrence is not Pell. Running the stated update from P_0 = 1/(1−x) gives den_1 = 1 − 2x + 2x²
  (roots 1 ± i, the A146559 sequence), not 1 − 2x − x². The Pell page's "num_0 = x" is also wrong; num_0 = 1.
- No two-state 0/1 transfer matrix can produce 1 − 2x − x². The six possible determinants for 2×2 0/1 matrices are 1, 1−x, 1−2x,
  1−x², (1−x)², and 1−x−x². The smallest 0/1 realization is 3×3, so the castle-strip page's "states are the heights 1..h" framing
  cannot host the Pell strip at h=2.

The same error appears in the {0,1}-strip example: a {0,1} skyline "with rule-3 gap" has 2^w members, not Fibonacci. Fibonacci needs
the stronger rule "no two adjacent raised columns", which is what the snippet is_zero_one_strip actually tests. The two
descriptions on the wiki disagree with each other.

The claim propagates into 5 of the 15 hubs (castle-counting-formula "Atomic reading" paragraph, generating-functions,
castle-classification Axis 8, castle-strip, castle-snippets) and six more pages (pell-castle-strip, pell-numbers,
metallic-strip-realizability, tower-spacing-castles, wiki/overview.md, IDEAS.md). The tell is already in IDEAS.md: the open
"Silver-ratio observatory" item asks for "a Pell-in-castle-somewhere result", which concedes Pell has not been found in a castle
count. The generic content survives: 1/(1 − 2x − x²) is a fine SEQ-over-two-atoms exercise, coefficient matching is right, the
silver-ratio growth is right, and the 1-smooth height-3 strip on metallic-strip-realizability is a legitimate silver realization.
What has to go is the identification of the atoms with rule 3 and the "baby case k=1" framing.

Cross-cutting issues

- OEIS is expanded on one page out of 46 that use it (oeis-cross-referencing). "PE 502" appears before "Project Euler" on 7 of the
  15 hubs. OGF, EGF, DP, GF, CF, DFT, and C-finite are used unexpanded across the set. generating-functions lists SEQ, MSET, PSET,
  CYC without saying sequence, multiset, powerset, cycle.
- Stale text from later growth. castle-polyomino and overview.md still say "42 types across 7 structural axes" (there are 9).
  project-euler-502-solution says Combinatorics and Implementation Notes are "not yet ingested" while linking to both.
  castle-classification's "Open threads" lists bronze/copper identification as open and Axis-9 types as "none populated", both
  contradicted higher on the same page.
- Frontmatter summaries carry legacy [[slug]] links and run to paragraph length on castle-sign, generating-functions,
  castle-classification, oeis-index. Summaries feed the index, so these bloat wiki/index.md.
- "Every output pinned" is not true. castle-snippets shows castle_graph((2,1,2)) with the cell above column 3 adjacent to column 2's
  cell. Rerunning the snippet gives a different matrix. castle_dlp and castle_schnorr call one() and gen(), which are defined
  nowhere on the page. H(d) uses mu and c[6] undefined. convergents-oeis-crosswalk likewise uses num6, series_coefficients_of,
  jpa_convergents, pre, per without definition.

Page by page

- castle-snippets. A code appendix that now spans every seminar arc, which is why it has 46 out-links. Split by arc: enumeration and
  predicates, strips and growth, number theory (convergents, mod p, quasi-split, sectors), cryptography. Fix the wrong pinned
  matrix and the undefined helpers. The is_zero_one_strip docstring contradicts the Pell page's reading of the same object.
- castle-counting-formula. The derivation is right end to end. I rechecked the E_k and P_k recurrences, the num/den update, the k=1
  and k=2 recurrences, the F(4,2) evaluation, and the parity argument. The "Atomic reading of the den_k update" paragraph is a later
  graft carrying the Pell error and reads as speculation stated as fact; remove it. The unsigned count is proved three ways in a
  row without saying so. Consider moving this page from Analyses to Concepts, since it is the wiki's core derivation.
- oeis-index. Two pages in one. The A-number directory with occurrence counts will go stale on every edit and should be
  script-generated. The novelty-status catalogue is hand-curated and valuable. Split them. The category Concepts fits neither.
- castle-classification. Axes 8 and 9 are each a page's worth and were bolted onto a skyline-predicate catalogue. The Ramanujan
  definition is ill-posed for irregular graphs: excluding λ = ±d_max excludes nothing, and Alon–Boppana bounds the second
  eigenvalue, not the spectral radius. The "path or star" justification for spectral radius below 2 is wrong (Smith's theorem gives
  the Dynkin diagrams), though the conclusion that only P_4 has radius φ holds. The Dyck-path and Motzkin-path counts are stated as
  Catalan and Motzkin without the endpoint and height-bound conditions those need. The hook count is given as both 1 and w. "Every
  silver width growth castle has a dominant eigenvalue in Q(√2)" is a tautology, and "parity is orthogonal to typing" is
  contradicted by convex castles having exactly h blocks.
- castle-sign. Correct. The (T−P)/2 explanation is made three times in six paragraphs; one would do.
- oeis-mining-pe502. Fine as a source summary. The vein numbering skips 5 and 8 with no explanation.
- signed-tower-count. Correct; I confirmed the P(2), P(3), P(4), P(6) rows and the constant terms. "Leading coefficient −(k+1)"
  should read "coefficient of x^k" since the polynomials are monic. The paragraph at line 41 carries five separate results and
  should be a list.
- convex-castle. Correct, including the min-block characterization and the parity consequence. The two "thread to follow" paragraphs
  at lines 32 and 48 say the same thing. Uses W, H where the rest of the wiki uses w, h. cev/cod are used without definition.
- project-euler-502-solution. Good, and its small claims check out (P(k,2), P(k,3), P(1,4) by brute count). Remove the two stale
  "not yet ingested" notes.
- generalized-dyck-grammar. The best-written page in the set. "A plain Dyck word is U…U D…D" describes only the fully nested word.
  The independence point is made three times.
- generating-functions. The coefficient-matching section is exactly right. The claim that the negative binomial "shows up as the
  tower and any-parity counts" is wrong; it appears in the convex count C(2h+w−3, w−1), not in (k+1)^L or h^w − (h−1)^w. The
  Description mixes definition with a comparison of three sources.
- castle-polyomino. The most under-built page relative to its 26 in-links. It never states the one fact every other page uses: a
  castle is a skyline (c_1, …, c_w) with 1 ≤ c_i ≤ h and max h, blocks are maximal runs so the block count is the total descent, and
  the any-parity count is h^w − (h−1)^w. castle-classification and castle-strip each restate the skyline definition because this
  page does not. It should also name the castle as a bargraph (a column-convex polyomino on a full base), which is the
  polyomino-literature hook. The rule-1 wording is garbled.
- castle-representations. Good. Same W/H notation drift.
- castle-counting-function. Good. The "G is reserved for generating functions" aside is chatty.
- convergents-oeis-crosswalk. Strong content, four essays long. Part 3 (the k-direction of P is a period-2 quasi-polynomial with
  characteristic polynomial (x+1)^L (x−1)^{L−2}) is a real result cited from signed-tower-count and castle-classification for that
  fact alone; give it its own Concept page. I checked the A_4, B_4 forms against the table and the ψ² minimal polynomial. Terms such
  as inert, split, Frobenius, Ehrhart, and Pisot get no gloss.
