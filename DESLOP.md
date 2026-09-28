# DESLOP - removing rhetorical filler from the wiki

Plan and tracker for stripping pseudo-poetic prose, unprovable asides and planning residue out of `wiki/`. Hand-maintained, outside `wiki/pages/`, never linked from the wiki. Conventions: `[ ]` not started, `[~]` spot fixes only (still needs a full read), `[x]` fully read and cleaned. Plain hyphens, no em-dashes.

## Where we are (2026-09-28)

| Slice | Value |
|---|---|
| Pages | 194 (85 Concepts / 64 Analyses / 44 Sources / overview) |
| Fully read and cleaned | 40 (song-as-castle and the 20 pages linking to it; batches 1-2, the 19 oldest pages) |
| Spot fixes only | 20 (one phrase each: "arc" vocabulary, "in disguise", backlink text) |
| Not started | 134 |
| Words still to read | about 348,000 |
| Commits so far | `908bada`, `69807cf`, `71fe27f`, `762a938`, `0a3e953` (wiki), `d33b48e`, `a7c53c3`; `acc4300` (IDEAS) |

## What the first pass found

Eleven kinds of slop, with real examples from the pages fixed so far. The examples are here so the patterns can be recognized. They are not to be quoted back in chat.

1. **Claims about motive or perception.** "Beethoven picked the melody because it is the smallest such castle a chorus can sing"; "which is precisely why humans hear it as *musical* and not *mechanical*". Unprovable and usually false. Always cut.
2. **Rhetorical closers and slogans.** "one object at every scale"; "The exercise was the seminar."; "the same castle, seen at ten scales at once"; "Same 'silver' loudest note, different sandcastle". A paragraph that ends on a slogan usually ends one sentence early without it.
3. **Audience narration on seminar pages.** "build it and trust it, then break that trust, then earn it back"; "free of the 'but is it secure?' anxiety"; "the room leaves with ... one deliberately unanswered question"; "the audience realizes the exercise was never abstract". A seminar page describes the mathematics and the order of stops, not how the room feels.
4. **Rhetorical questions.** "But what does the bit *buy*?"; "What is the even-block bit?". Replace with the statement the question was setting up.
5. **"X is the Y of Z" analogies and emphasis words.** "in disguise"; "made physical"; "a castle analogue of a PRNG ... tiny Kolmogorov complexity"; "Chomsky's hierarchy is the description-tier ladder for languages"; "Spectral is a promiscuous word"; "every method here is a lens". Keep an analogy only when it is a precise mathematical correspondence stated as such.
6. **Overclaims and "firsts".** "the first single-number castle statistic on the wiki that knows which end of the castle is which"; "Two castle families are asymptotically equivalent iff their transfer-matrix eigenvalue sequences agree"; "every growth constant the wiki has catalogued is a topological entropy". Either prove it, scope it, or cut it.
7. **Aphorisms in *Idea:* lines.** "an order is a clock"; "a thread to pull"; "Rates measure the rule, and boundary terms measure the question asked about it"; "Robustness runs opposite to how much of the object a statistic depends on" (false: the histogram depends on every column and survives everything). An *Idea:* line states the mathematical takeaway of its stop in one plain sentence.
8. **Anthropomorphism.** "`B_alpha` knows *where* a castle's mass sits"; "the round-three castle torus item ... wants to be prime-heavy"; "the ear does not yet know it is D minor". Exception: "hear" is Kac's technical vocabulary on the hear-the-shape pages and stays.
9. **Numerology and trivia.** "Two coincidences worth naming as coincidences"; "the `(6, 4)` cell ... is the one with `F(6, 4) = 1729`" dropped in as an aside; "Feynman's party trick"; "recent celebrities". Keep a number only if it is used.
10. **Contested history stated as cause.** "the recording whose length set the size of the Compact Disc", when the page's own footnote says the story is disputed. State it as disputed or leave it out.
11. **Planning residue inside the wiki.** IDEAS vocabulary ("the q-thread arc", "Arc 14's slogan", "the item's suggestion"); effort columns (Days / Weeks / Months); dead working-note paths (`/Users/creid/tmp/pe502-nomography.md`, which exists nowhere); "pending ingest", "not yet added", "when its content lands"; a "sketched approach" for a search that has since been run. The wiki states results and open problems in its own words.

## What was hiding under it

Every flourish sat next to a mathematical claim, and a large share of those claims were wrong. Errors found only by rechecking the sentence a flourish decorated:

- a 128-bit fingerprint was "the same castle as the URL" (it is `w = 17` at `h = 256`; the URL is `w = 9`)
- "nearly unimodal" for a phrase with two peaks; "exact period" for a two-tone skyline with an irrational frequency ratio
- the DFT as "a complete invariant modulo cyclic shift" (it is invertible; only `|c_k|` is shift-invariant)
- Parseval "fixes energy at the area-squared scale" (it splits `sum c_j^2`)
- "wide spectral gap -> O(1) fluctuations" (a gap gives the usual `O(sqrt w)` CLT)
- a "spectral phase transition at some critical beta" for a finite positive matrix (its Perron root is analytic; no transition at fixed `h`)
- Laplacian gap `Theta(1/w)` for unimodal castles (a box already gives `Theta(1/w^2)`)
- Pell strip count `P_{w+1}` where the table's own numbers are `P_w`
- signed sum written `P` where the page defines it as `S`
- "about 40 squarings to reach `a = 10^12`, no matter how large `a` is"
- Berlekamp-Massey "from ten numbers" after feeding it twelve
- growth "back up to a positive value" at `alpha = 2` (it is `phi`; every growth constant is at least 1)

Lesson: cleaning prose is also an audit. Recompute every claim a flourish was attached to.

## Rules for the rewrite

1. **Cut, don't hedge.** Delete the flourish. Do not replace it with a softer flourish or a qualifying paragraph. One short edit per issue.
2. **Keep every number, definition, result and citation.** Deslopping removes rhetoric, not content. No new mathematics goes in.
3. **Recompute before rewording.** If a sentence carries a number or a claim, check it in a scratch script before keeping it. Record corrections in the commit message.
4. **Seminar structure stays** (Thesis / Stops / *Idea:* / Board / Snippet / Exercises), but each part carries mathematics. Stage directions are neutralized (see Owner decisions).
5. **Summaries count.** The frontmatter `summary:` is the page's most-read text (it feeds `wiki/index.md`). Clean it together with the body.
6. **Don't quote the slop back** in chat or commit messages beyond a short identifying fragment.
7. **Keep planning files out of the wiki.** No IDEAS, Divisions, arc, item or effort vocabulary on wiki pages.

## Per-page procedure

1. Read the whole page: summary, body, tables, footnotes, backlink lines. Skip code blocks only for prose, not for numbers quoted from them.
2. List the flourishes and the claims next to them.
3. Recompute each nearby claim (scratch script in the session scratchpad).
4. Apply the edits: exact string replacements, each asserted to match once.
5. Run the regression check (below). It must report zero hits.
6. Regenerate `wiki/index.md` with `bin/generate-index.py`, and `wiki/pages/oeis-index.md` with `bin/generate-oeis-index.py` if the hook asks.
7. Tick the page here.

## Detection

Reading is the method. A keyword scan (a throwaway script in the first pass, not in the repo: about 45 regexes such as `in disguise`, `the point is`, `for free`, `honest`, `the room`, `the audience`, `\barcs?\b`, rhetorical `?`, "is the X of") is only a pre-filter for ordering the queue. It misses most slop: the ARFIMA aside and the phase-transition claim scored nothing. It also flags defined terms, which are not slop: "veins" on oeis-mining-pe502 (30 hits) and "hear" on the Kac pages. Drop such terms from the pattern list.

**Step 0 (done):** the scan is `bin/slop-scan.py`, with two modes:

- `--rank`: pattern density per 1000 prose words (code, frontmatter and footnotes skipped), used to order a batch.
- `--regress`: fails if any retired phrase reappears in `wiki/overview.md` or `wiki/pages/`. `--regress --staged` scans the git index and runs in the pre-commit hook. The retired list holds every phrase quoted in "What the first pass found", `arc` / `the item's` / `IDEAS` / effort columns, and each phrase a later batch cuts. Add phrases as they are retired.

The seminar stage directions ("Exercises for the room", "at one blackboard", "About 60 minutes") go on the retired list once the seminar pages have been revisited; until then they would block every commit.

## Order of work

Batches of 8 to 10 pages **in order of first commit, oldest first** (owner decision, 2026-09-28), one wiki commit per batch (`fix: deslop <batch>`, with corrections listed in the body). Pages first committed together were ingested together, so age order keeps related pages in one batch. List the queue with `git log --diff-filter=A --follow --format=%ad --date=iso -- <page> | tail -1` per page. A finished seminar page gets its stage-direction revisit (item 0 below) when it comes up in age order.

The topical order below was the original plan and is kept for reference.

0. **Revisit the 21 finished pages** under the owner decisions: stage directions on the seminar pages (hear-the-shape, hardin-identity, oeis-mining, one-bit, q-thread, sandcastle, castle-fibers-char-2-walkthrough, tower-recursion-master-class, pell-castle-strip, castle-cryptography), and the relevance of *The Wire*, the CD story and the 2600 Hz aside on song-as-castle.
1. **overview.md**, the entry page.
2. **Cryptography cluster**: castle-cryptography-ring, -number-theory, -round-two, -round-three, castle-snippets-cryptography. Seminar-shaped, and the same voice as castle-cryptography, which was the worst page fixed so far.
3. **Sandpile / spectral cluster**: sandcastle-clock, sandpile-identity, sandpile-census, sandpile-group, castle-avalanches, isospectral-castles, levy-flights, castle-graph, castle-graph-spectral-radius, ramanujan-castles.
4. **Remaining Analyses**, by scan score.
5. **Concepts**, by scan score. The seminar-adjacent ones first (castle-eigenvalues-by-example, castle-gray-code, castle-native-gray-tour).
6. **Sources**, with a different check: the page is a synthesis of a source. Keep attributed quotes verbatim and short, and check that the synthesis says no more than the source does.

After each batch, update "Where we are".

## Owner decisions (2026-09-28)

- **Order of work is by page age**, oldest first by git history, replacing the topical order.
- **Metaphors that double as terms stay.** "veins" (OEIS mining), "ladder" / "rungs" (metallic means, polyomino families, encodings), "tiers" (castle-compression), "ratchet" (power-law-memory-rules), "threads" and the like are the wiki's vocabulary. Do not replace or flag them. Slop is a metaphor doing rhetorical work in a sentence, not a named term.
- **Historical anecdotes stay only when relevant.** They anchor the mathematics in reality but must not get cute. Keep one only if the page's mathematics uses it. The 1729 taxi story is key color and stays. *The Wire*'s pager code on song-as-castle is a candidate to cut. Check the Red Book CD story and the Cap'n Crunch / 2600 Hz aside against the same test.
- **Neutralize seminar stage directions.** "Exercises for the room", "at one blackboard", "About 60 minutes", "Format." paragraphs about the room, "on the board", "the room leaves with". Keep the structure (stops, *Idea:* lines, board table, snippet, exercises) with plain headings: "Exercises", not "Exercises for the room". Drop duration and blackboard framing.

## Checklist

Scan score in parentheses: retired-pattern density per 1000 words, higher first. Scores include hits on defined terms ("veins", "hear"), so oeis-mining-pe502 and the Kac pages are inflated.

### Concepts (85 pages, 25 fully read)

- [x] hear-the-shape-seminar (9.9)
- [ ] hyperbolic-sequence-family (6.2)
- [ ] narayana-numbers (5.7)
- [x] sandcastle-seminar (5.5)
- [x] berlekamp-massey (5.5)
- [ ] sandcastle-clock (4.9)
- [ ] castle-classification (4.8)
- [ ] castle-graph (4.7)
- [ ] finite-fields (4.6)
- [ ] sandpile-identity (4.5)
- [ ] signed-tower-count (4.2)
- [~] eigenvalue-continued-fractions (4.1)
- [ ] weakly-unimodal-composition (4.0)
- [x] castle-fibers-char-2-walkthrough (3.8)
- [ ] castle-eigenvalues-by-example (3.7)
- [x] spectral-analysis (3.5)
- [~] castle-gray-code (3.4)
- [ ] permutation-inversions (3.3)
- [x] tower-recursion-master-class (3.3)
- [x] hardin-identity-seminar (3.2)
- [x] castle-polyomino (3.2)
- [x] oeis-mining-seminar (3.2)
- [ ] sandpile-group (3.0)
- [ ] castle-native-gray-tour (3.0)
- [ ] block-count-constraints (3.0)
- [ ] column-convex-polyomino (3.0)
- [ ] parity-via-roots-of-unity (3.0)
- [x] castle-counting-function (2.8)
- [ ] multiset-partitions (2.7)
- [x] one-bit-seminar (2.7)
- [ ] plastic-number (2.6)
- [x] castle-entropy (2.5)
- [x] castle-representations (2.5)
- [x] q-thread-seminar (2.5)
- [x] castle-samplers (2.4)
- [ ] idempotent-decomposition (2.3)
- [~] castle-by-area (2.3)
- [x] urd-step-strings (2.1)
- [ ] kitamasa (2.1)
- [ ] castle-classification-spectrum (1.9)
- [ ] stack-polyomino-gf (1.9)
- [x] castle-sign (1.9)
- [ ] binary-string-bijection (1.8)
- [ ] ramanujan-castles (1.7)
- [ ] castle-snippets-cryptography (1.7)
- [ ] mod-9-coset-lift (1.6)
- [~] q-catalan-numbers (1.6)
- [ ] oeis-cross-referencing (1.6)
- [x] castle-compression (1.5)
- [ ] metallic-means (1.4)
- [~] castle-snippets (1.4)
- [ ] castle-bdd-zdd (1.3)
- [x] generalized-dyck-grammar (1.3)
- [ ] castle-classification-growth (1.2)
- [ ] castle-notation (1.2)
- [ ] castle-strip (1.1)
- [ ] sums-of-three-cubes (1.1)
- [ ] castle-classification-shape (1.1)
- [ ] signed-tower-k-direction (1.1)
- [ ] tower-heap (1.1)
- [x] castle-counting-formula (1.0)
- [ ] castle-move-graph-zdd (0.9)
- [ ] algebraic-transcendental-wall (0.8)
- [ ] pell-numbers (0.8)
- [ ] tower-word-language (0.7)
- [x] generating-functions (0.7)
- [ ] parallelogram-polyomino-dyck-bijection (0.6)
- [ ] tower-word-continued-fraction (0.6)
- [ ] convex-polyomino (0.6)
- [x] castle-foata-transform (0.6)
- [ ] q-differential-system (0.6)
- [ ] castle-snippets-number-theory (0.5)
- [ ] unique-tournament (0.0)
- [ ] symbolic-method (0.0)
- [ ] simple-tournament (0.0)
- [x] permutation-cycle-castle-analogy (0.0)
- [ ] motzkin-numbers (0.0)
- [x] monotone-streak-factorization (0.0)
- [ ] horizontally-convex-polyomino (0.0)
- [ ] forcibly-simple-score-vector (0.0)
- [x] convex-castle (0.0)
- [ ] chinese-remainder-theorem (0.0)
- [ ] catalan-numbers (0.0)
- [ ] castle-snippets-strips (0.0)
- [ ] acronyms (0.0)

### Analyses (64 pages, 9 fully read)

- [x] castle-cryptography (5.1)
- [ ] isospectral-castles (4.9)
- [ ] castle-cryptography-number-theory (4.4)
- [~] castle-cryptography-ring (4.0)
- [ ] sandpile-census (3.8)
- [~] castle-cryptography-round-two (3.6)
- [x] pell-castle-strip (3.4)
- [ ] castle-graph-spectral-radius (3.3)
- [ ] castles-as-upgraded-cycle-count (3.2)
- [ ] mod-p-observatory (3.0)
- [ ] levy-flights (2.9)
- [~] fractional-recurrences (2.8)
- [~] castle-eigenvalue-oeis-crosswalk (2.8)
- [x] castle-phone-line (2.7)
- [x] song-as-castle (2.6)
- [x] power-law-memory-rules (2.6)
- [~] prime-castles (2.3)
- [x] image-as-castle (2.3)
- [x] hardy-ramanujan-castle (2.2)
- [ ] metallic-strip-realizability (2.1)
- [ ] convex-core (2.0)
- [ ] larger-prime-periodicity (1.9)
- [ ] castle-perimeter (1.9)
- [ ] castle-count-algorithms (1.8)
- [ ] tower-spacing-castles (1.8)
- [ ] char-k-eisenstein-at-two (1.8)
- [ ] proper-castle-projection (1.8)
- [ ] a005251-bijection (1.7)
- [ ] castle-ring-spectrum (1.6)
- [ ] column-convex-ladder-by-area (1.6)
- [ ] fractional-width-and-height (1.6)
- [ ] tree-castle-by-area (1.5)
- [x] castle-steganography (1.5)
- [ ] motzkin-castles (1.5)
- [~] mod-9-equidistribution (1.4)
- [~] signed-klarner-decomposition (1.4)
- [x] fractional-block-count (1.4)
- [ ] reachable-field-census (1.4)
- [ ] castle-sequence-catalogue (1.3)
- [ ] bounded-height-castles-nacci (1.3)
- [ ] castle-add-a-column-equation (1.3)
- [ ] bronze-castle-hunt (1.3)
- [ ] castle-ring-invariant-factors (1.2)
- [ ] tower-parity-sectors (1.1)
- [ ] viennot-heap-tower (1.1)
- [ ] closed-form-hunting (1.1)
- [ ] generating-function-gallery (1.1)
- [ ] convex-castle-binomial-identity (1.0)
- [ ] recurrence-discovery (1.0)
- [ ] quadratic-min-height (1.0)
- [~] castle-sign-kms-matrix (1.0)
- [ ] area-growth-census (0.9)
- [ ] half-sum-castles (0.8)
- [ ] castle-conditional-entropy (0.8)
- [~] convex-polyomino-by-area (0.7)
- [ ] castle-avalanches (0.6)
- [ ] hardin-word-identity (0.6)
- [ ] prime-convex-castles (0.5)
- [ ] sum-of-three-cubes-castles (0.5)
- [~] castle-row-raising-equation (0.5)
- [~] castle-cryptography-round-three (0.4)
- [ ] odd-castles-and-block-tables (0.0)
- [ ] convex-castle-cap-factor (0.0)
- [~] castle-q-bessel-closed-form (0.0)

### Sources (44 pages, 5 fully read)

- [ ] oeis-mining-pe502 (25.6)
- [ ] oeis-height2-hyperbolic-castles (5.9)
- [ ] new-sequence-fw3 (4.3)
- [ ] aocp-generating-permutations-tuples (3.4)
- [ ] steep-polyominoes-q-motzkin-bessel (3.4)
- [ ] lattice-paths (3.2)
- [ ] dhar-ruelle-sen-verma-1995-algebraic-aspects (3.2)
- [ ] aocp-generating-functions (3.1)
- [ ] prodinger-2025-cornerless-motzkin-bargraphs (2.9)
- [ ] aocp-permutations (2.8)
- [ ] tower-narayana-polynomial (2.5)
- [~] pe502-pell-castle-strip (2.3)
- [ ] algebraic-languages-and-polyominoes-enumeration (2.3)
- [ ] bousquet-melou-fedou-1995-convex-polyominoes (2.2)
- [ ] counting-horizontally-convex-polyominoes (2.1)
- [ ] deutsch-elizalde-2016-bargraphs-cornerless-motzkin (2.0)
- [ ] polyominoes (2.0)
- [ ] bender-1974-partitions-of-multisets (1.7)
- [ ] calugareanu-hamburg-exercises-basic-ring-theory (1.6)
- [ ] aocp-combinatorics (1.5)
- [ ] rossin-2000-group-of-a-sandpile (1.3)
- [~] chau-cheng-1991-deterministic-soc-sandpile (1.1)
- [ ] dyck-words (1.1)
- [x] project-euler-502-problem-setup (1.1)
- [ ] analytic-combinatorics-ch1-ogfs (1.1)
- [ ] generating-functions-topic (0.9)
- [ ] chau-1993-abelian-sandpile-model (0.9)
- [ ] aocp-multisets (0.9)
- [ ] column-convex-polygon-enumeration (0.9)
- [ ] prellberg-brak-1995-cluster-models (0.9)
- [ ] aocp-binomial-coefficients (0.9)
- [x] project-euler-502-castle-factoring (0.9)
- [x] project-euler-502-observations (0.8)
- [~] bak-tang-wiesenfeld-1988-self-organized-criticality (0.8)
- [ ] project-euler-502-solution (0.7)
- [ ] tetali-1998-unique-tournaments (0.5)
- [ ] bender-1974-convex-n-ominoes (0.5)
- [ ] klarner-rivest-1974-convex-n-ominoes (0.5)
- [x] project-euler-502-representations (0.0)
- [ ] project-euler-502-implementation-notes (0.0)
- [ ] project-euler-502-brute-force (0.0)
- [x] project-euler-502 (0.0)
- [ ] dhar-1990-self-organized-critical-sandpile (0.0)
- [ ] aocp-multinomial-coefficients (0.0)

### Top level (1 page, 1 fully read)

- [x] overview (3.5)
