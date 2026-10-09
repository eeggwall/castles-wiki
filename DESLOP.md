# DESLOP - removing rhetorical filler from the wiki

Plan and tracker for stripping pseudo-poetic prose, unprovable asides and planning residue out of `wiki/`. Hand-maintained, outside `wiki/pages/`, never linked from the wiki. Conventions: `[ ]` not started, `[~]` spot fixes only (still needs a full read), `[x]` fully read and cleaned. Plain hyphens, no em-dashes.

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

The seminar stage directions ("Exercises for the room", "at one blackboard", "About 60 minutes") are on the retired list since batch 34, when the last seminar pages were revisited.

## Order of work

The topical order below was the original plan and is kept for reference.

0. **Revisit the 21 finished pages** under the owner decisions: stage directions on the seminar pages (hear-the-shape, hardin-identity, oeis-mining, one-bit, q-thread, sandcastle, castle-fibers-char-2-walkthrough, tower-recursion-master-class, pell-castle-strip, castle-cryptography), and the relevance of *The Wire*, the CD story and the 2600 Hz aside on song-as-castle.
1. **overview.md**, the entry page.
2. **Cryptography cluster**: castle-cryptography-ring, -number-theory, -round-two, -round-three, castle-snippets-cryptography. Seminar-shaped, and the same voice as castle-cryptography, which was the worst page fixed so far.
3. **Sandpile / spectral cluster**: sandcastle-clock, sandpile-identity, sandpile-census, sandpile-group, castle-avalanches, isospectral-castles, levy-flights, castle-graph, castle-graph-spectral-radius, ramanujan-castles.
4. **Remaining Analyses**, by scan score.
5. **Concepts**, by scan score. The seminar-adjacent ones first (castle-eigenvalues-by-example, castle-gray-code, castle-native-gray-tour).
6. **Sources**, with a different check: the page is a synthesis of a source. Keep attributed quotes verbatim and short, and check that the synthesis says no more than the source does.

## Owner decisions (2026-09-28)

- **Order of work is by page age**, oldest first by git history, replacing the topical order.
- **Metaphors that double as terms stay.** "veins" (OEIS mining), "ladder" / "rungs" (metallic means, polyomino families, encodings), "tiers" (castle-compression), "ratchet" (power-law-memory-rules), "threads" and the like are the wiki's vocabulary. Do not replace or flag them. Slop is a metaphor doing rhetorical work in a sentence, not a named term.
- **Historical anecdotes stay only when relevant.** They anchor the mathematics in reality but must not get cute. Keep one only if the page's mathematics uses it. The 1729 taxi story is key color and stays. *The Wire*'s pager code on song-as-castle is a candidate to cut. Check the Red Book CD story and the Cap'n Crunch / 2600 Hz aside against the same test.
- **Neutralize seminar stage directions.** "Exercises for the room", "at one blackboard", "About 60 minutes", "Format." paragraphs about the room, "on the board", "the room leaves with". Keep the structure (stops, *Idea:* lines, board table, snippet, exercises) with plain headings: "Exercises", not "Exercises for the room". Drop duration and blackboard framing.
