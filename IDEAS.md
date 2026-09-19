# Project and Seminar Ideas

Working list of project and seminar ideas for Project Euler 502 (Castles). This file drives new Analyses; the map of the whole wiki is `wiki/index.md` (generated) and `wiki/overview.md`.

Conventions: `[ ]` open, `[x]` has a page. Open items first, done items last, within each Division. A done item is one line: title link + one-sentence result; detail lives on the page and in git history. Any open follow-up is its own `[ ]` item, never a "Still open:" tail. Every item ends with an arc tag `(S1..S11)` naming the seminar it feeds; `(-)` for items outside any arc. Plain hyphens in new text, no em-dashes.

## Where we are (2026-09-19)

| Slice | Value |
|---|---|
| Pages | 106 (30 Sources / 51 Concepts / 25 Analyses) |
| Divisions (open + done) | Numbers 11+25, Enumeration 5+16, Q 5+0, S 5+5, T 7+0, Classification 4+4, Misc 6+0 |
| Items | 43 open, 50 done, 93 total |
| Arcs | 11 (5 deliverable, 3 one page short, 1 half built, 2 sketch) |
| Dates | wiki 2026-09-13, IDEAS 2026-09-14, last reorganize 2026-09-19 |

## Seminar program

Each arc is a titled subplot with a one-line thesis, a status, its spine pages in delivery order, and the open items it needs. Statuses: `deliverable` (spine end to end), `one page short` (spine exists, the seminar-shaped page does not), `half built`, `sketch`. Arc titles are hooks, not division names; wording may be adjusted during execution.

### S1. The castle counted on one blackboard
- Thesis: two ideas - towers are independent, parity is a sign - drive every algorithm the castle needs, from `T(k,L)=(k+1)^L` to trillion-scale Kitamasa jumps.
- Status: deliverable.
- Spine: [tower-recursion-master-class](wiki/pages/tower-recursion-master-class.md), [castle-sign](wiki/pages/castle-sign.md), [parity-via-roots-of-unity](wiki/pages/parity-via-roots-of-unity.md), [castles-as-upgraded-cycle-count](wiki/pages/castles-as-upgraded-cycle-count.md), [kitamasa](wiki/pages/kitamasa.md), [berlekamp-massey](wiki/pages/berlekamp-massey.md), [castle-count-algorithms](wiki/pages/castle-count-algorithms.md).
- Open items feeding it: from Misc, a general closed form for `P(k,L)` and minimality of the empirical recurrence orders.

### S2. From a textbook exercise to the metallic ladder
- Thesis: an Analytic Combinatorics end-of-chapter exercise opens onto the full metallic-ratio ladder and its reachable-field structure.
- Status: deliverable.
- Spine: [pell-castle-strip](wiki/pages/pell-castle-strip.md), [castle-strip](wiki/pages/castle-strip.md), [metallic-means](wiki/pages/metallic-means.md), [eigenvalue-continued-fractions](wiki/pages/eigenvalue-continued-fractions.md), [metallic-strip-realizability](wiki/pages/metallic-strip-realizability.md), [reachable-field-census](wiki/pages/reachable-field-census.md), [proper-castle-projection](wiki/pages/proper-castle-projection.md), [bounded-height-castles-nacci](wiki/pages/bounded-height-castles-nacci.md), [plastic-number](wiki/pages/plastic-number.md).
- Open items feeding it: from Numbers, silver-ratio observatory, larger-prime periodicity, the min-height law for `(p1,p2)`, Pisot/Salem cubics; from Classification, the horizontal-gap reachable-field census.

### S3. The Hardin word identity
- Thesis: `P_even(4m+2, L) = 2^L` times a word count; the two transfer matrices differ by one unimodular change of basis.
- Status: one page short. Spine exists; the seminar-shaped centerpiece page does not.
- Spine: [tower-parity-sectors](wiki/pages/tower-parity-sectors.md), [hardin-word-identity](wiki/pages/hardin-word-identity.md), [a005251-bijection](wiki/pages/a005251-bijection.md), [tree-castle-by-area](wiki/pages/tree-castle-by-area.md), [tetali-1998-unique-tournaments](wiki/pages/tetali-1998-unique-tournaments.md).
- Open items feeding it: from Numbers, the centerpiece itself, the sign-reversing involution, the two sector-assignment conjectures, `h>=5` tree-castle-by-area sequences.

### S4. Hear the shape of a castle
- Thesis: five spectra on a castle graph, with the 10-cell adjacency-isospectral pair as the punchline.
- Status: one page short. Spine exists; the seminar-shaped centerpiece page does not.
- Spine: [spectral-analysis](wiki/pages/spectral-analysis.md), [castle-graph](wiki/pages/castle-graph.md), [castle-graph-spectral-radius](wiki/pages/castle-graph-spectral-radius.md), [isospectral-castles](wiki/pages/isospectral-castles.md).
- Open items feeding it: from S, the centerpiece itself, the bronze hunt, skyline DFT, LGV kernel spectrum, Ihara zeta / Sunada for the 10-cell pair.

### S5. Castle cryptography: build, break, fix
- Thesis: build a public-key system on the castle ring, red-team it, blue-team the fixes; run the loop twice.
- Status: deliverable (run twice).
- Spine: [castle-cryptography](wiki/pages/castle-cryptography.md), [castle-cryptography-ring](wiki/pages/castle-cryptography-ring.md), [castle-cryptography-number-theory](wiki/pages/castle-cryptography-number-theory.md), [castle-cryptography-round-two](wiki/pages/castle-cryptography-round-two.md).
- Open items feeding it: from Numbers, round-three torus on `char_5`, shrinking-generator castle, the two `d=3` linear-complexity deficits.

### S6. The q-thread: castles by area
- Thesis: grade every castle sub-family by area and locate where q-Catalan, q-Motzkin, and q-Bessel meet the polyomino literature.
- Status: half built.
- Spine: [castle-by-area](wiki/pages/castle-by-area.md), [convex-castle-binomial-identity](wiki/pages/convex-castle-binomial-identity.md), [weakly-unimodal-composition](wiki/pages/weakly-unimodal-composition.md), [stack-polyomino-gf](wiki/pages/stack-polyomino-gf.md), [tree-castle-by-area](wiki/pages/tree-castle-by-area.md), [bounded-height-castles-nacci](wiki/pages/bounded-height-castles-nacci.md), [q-catalan-numbers](wiki/pages/q-catalan-numbers.md), [steep-polyominoes-q-motzkin-bessel](wiki/pages/steep-polyominoes-q-motzkin-bessel.md).
- Open items feeding it: from Q, prime castles, q-polyomino zoo (absorbs TODO's stack/Ferrers/parallelogram and A001169 threads), q-Catalan/q-Motzkin joins (absorbs the "find the q-equivalent" thread), convex/valley bijection, the `h=3` tree-vs-all bijection.

### S7. OEIS mining as a research method
- Thesis: sweep the brute enumerator, look up every sequence, and treat matches as new castle interpretations to submit.
- Status: deliverable.
- Spine: [oeis-cross-referencing](wiki/pages/oeis-cross-referencing.md), [oeis-mining-pe502](wiki/pages/oeis-mining-pe502.md), [oeis-index](wiki/pages/oeis-index.md), [oeis-height2-hyperbolic-castles](wiki/pages/oeis-height2-hyperbolic-castles.md), [castle-eigenvalue-oeis-crosswalk](wiki/pages/castle-eigenvalue-oeis-crosswalk.md), [new-sequence-fw3](wiki/pages/new-sequence-fw3.md).
- Open items feeding it: from Numbers, the castle sequence bank residue; from Classification, OEIS id of the tower-spacing 2D sequences and bounded-height rows. Submissions themselves are human action and stay in `TODO.md`.

### S8. One bit: the parity clause as information
- Thesis: the even-block clause is exactly one bit, and the entropy view re-reads every growth constant as a topological entropy.
- Status: one page short. Spine exists; the seminar-shaped synthesis does not.
- Spine: [castle-entropy](wiki/pages/castle-entropy.md), [castle-compression](wiki/pages/castle-compression.md), [castle-sign](wiki/pages/castle-sign.md).
- Open items feeding it: from Enumeration, conditional entropy given block count / area, a rule-generated-castle detector, and whether the parity bit survives object by object.

### S9. pi from a pile of blocks
- Thesis: castle samplers plus CLT / random-matrix / geometric-probability limits push transcendentals through combinatorial machinery.
- Status: sketch.
- Spine: [algebraic-transcendental-wall](wiki/pages/algebraic-transcendental-wall.md) (the wall), [spectral-analysis](wiki/pages/spectral-analysis.md) (LGV hook).
- Open items feeding it: from T, all six items; prerequisite the `castle-samplers` page (promoted to its own `[ ]` at the head of the T Division).

### S10. Knuth's algorithms in castle space
- Thesis: TAOCP Vol. 4 generation algorithms translated into the mixed-radix `{1..h}^w` space, with a castle Gray code as the payoff.
- Status: sketch.
- Spine: [aocp-generating-permutations-tuples](wiki/pages/aocp-generating-permutations-tuples.md), [project-euler-502-brute-force](wiki/pages/project-euler-502-brute-force.md), [castle-snippets](wiki/pages/castle-snippets.md).
- Open items feeding it: from Enumeration, castle Gray code / loopless enumerator (from TODO), Viennot heap theory via [tower-heap](wiki/pages/tower-heap.md) (from TODO).

### S11. The rule zoo: variations on the castle
- Thesis: change one rule, name the family, count it.
- Status: mixed.
- Spine: [castle-classification](wiki/pages/castle-classification.md), [castle-snippets](wiki/pages/castle-snippets.md), [tower-spacing-castles](wiki/pages/tower-spacing-castles.md), [castle-representations](wiki/pages/castle-representations.md).
- Open items feeding it: from Classification, rule-variation enumeration and the no-touching / vertical-spacing variants; from Misc, higher-dimensional castles, convex-core uniqueness, statistical-physics links, exact `(w,h)` enumeration of convex/unimodal castles with parity.

## Divisions

### Numbers Division

- [ ] **Castle sequence bank residue** - the mining pass covered F, T, P and every derived count; what remains is `F_odd = A - F` as its own bank entry, the parity-refined area sequences, and the block-count / peak / area joint distributions not yet enumerated. (S7)
- [ ] **Larger-prime periodicity** - extend the mod-p observatory to larger primes (and `10^9+7`); the periods become infeasible to enumerate, but the eigenvalue-order structure persists. (S2)
- [ ] **Seminar centerpiece: the Hardin word identity** - a 90-minute arc from "sum `(-1)^blocks` over towers" to "count words with no nonzero local maximum," every step on one blackboard. (S3)
- [ ] **Min-height law for `(p1,p2)`** - a closed form or tight bound for the minimum height realizing a given reachable pair; no clean formula fits so far. (S2)
- [ ] **Pisot/Salem classification of reachable cubics** - which reachable-field cubic Perron roots are Pisot or Salem numbers. (S2)
- [ ] **Round-three castle torus on `char_5`** - build on `char_5` (degree 6) with `p` chosen so `Phi_6(p) = p^2 - p + 1` has a large prime factor, then red-team against the real `F_{p^6}` index-calculus literature. (S5)
- [ ] **Shrinking-generator castle** - an irregularly clocked castle as the nonlinear variant that linearization does not cover. (S5)
- [ ] **Two `d=3` linear-complexity deficits** - trace the `8 vs 9` and `9 vs 10` gaps to specific root coincidences of `char_2`. (S5)
- [ ] **Sign-reversing involution for Hardin** - realize the `2^L` factor object by object; a common thread across [tower-parity-sectors](wiki/pages/tower-parity-sectors.md), [hardin-word-identity](wiki/pages/hardin-word-identity.md), and [a005251-bijection](wiki/pages/a005251-bijection.md). (S3)
- [ ] **Two sector-assignment conjectures** - the dominant root always lands in the even sector, and `H_{k/2}` is in the even sector iff `k ≡ 2 (mod 4)`. (S3)
- [ ] **`h>=5` tree-castle-by-area sequences** - no OEIS match yet; identify or submit as new. (S3)

- [x] **[Reachable-field census](wiki/pages/reachable-field-census.md)** - which number fields host castle-strip Perron roots; `h<=5` exhaustive, `h>=6` by the `(p1,p2)` reachability law; every real quadratic field is reachable. (S2)
- [x] **[Proper-castle projection](wiki/pages/proper-castle-projection.md)** - metallic growth constants survive the `max_i c_i = h` and `(A±P)/2` projections; the exact sequences are new (no OEIS match for `h>=3`). (S2)
- [x] **[Plastic / Padovan observatory](wiki/pages/plastic-number.md)** - the bare plastic number `psi` is a castle-strip Perron root at height 3, realized by 6 of 512 binary 3x3 matrices; the height-3 rule is Padovan / Perrin growth. (S2)
- [x] **[Bounded-height castles by area (n-nacci)](wiki/pages/bounded-height-castles-nacci.md)** - all castles of height `<=h` by area equal the h-step Fibonacci; Fibonacci, tribonacci, tetranacci on one ladder. (S6)
- [x] **[Metallic-ratio ladder](wiki/pages/metallic-means.md)** - the plateau-free-except-ceiling strip realizes the whole ladder (metal `a` at height `a+1`); copper `= delta_4 = phi^3` is the Fibonacci trisection. (S2)
- [x] **[Castle cryptography](wiki/pages/castle-cryptography.md)** - build / red-team / blue-team as three seminars; keypair is a castle, trapdoor is Kitamasa exponentiation, DLP splits via char-poly factorization. (S5)
- [x] **[Castle cryptography, seminar 1 (the ring)](wiki/pages/castle-cryptography-ring.md)** - the algebra baseline as a standalone page: recurrence encoding, mod-p periodicity, ring structure, CRT, Kitamasa cost, `castle_dh`. (S5)
- [x] **[Castle cryptography, round two](wiki/pages/castle-cryptography-round-two.md)** - toy ElGamal / Schnorr on castles, both round-one fixes broken (Pohlig-Hellman, linearization), sized to real 128-bit security. (S5)
- [x] **[Tetali 1998 tree-castle theorem](wiki/pages/tetali-1998-unique-tournaments.md)** - the A000570 identity for tree castles at `h=4` is Tetali's classification of score-unique tournaments in disguise; verified through `n=8`. (S3)
- [x] **[A005251 bijection](wiki/pages/a005251-bijection.md)** - no-isolated-1 strings, tree castles by area, and minimum-tower-spacing `(h=2,g=2)` castles all coincide via the classical gap-string map. (S3)
- [x] **[Hardin word identity](wiki/pages/hardin-word-identity.md)** - proved: `P_even(4m+2, L) = 2^L` times `(L+1)`-letter words with no nonzero strict local maximum, via an explicit unimodular change of basis. (S3)
- [x] **[Recurrence discovery](wiki/pages/recurrence-discovery.md)** - Berlekamp-Massey on `P(k,L)` in both directions; order `k+1` in L (confirmed), exactly `2L-2` in k for `L>=4`. (S1)
- [x] **[Closed-form hunting](wiki/pages/closed-form-hunting.md)** - `P(k,2) = (-1)^k (k+1)` and `P(k,3) = (-1)^k (k+1)^2`; no simple form for `L>=4`. (S1)
- [x] **[Generating-function gallery](wiki/pages/generating-function-gallery.md)** - `num_k / den_k` catalogue, denominator roots, the C-finite recurrences; dominant eigenvalue `rho_k ~ k / log k`. (S1)
- [x] **[Mod-p observatory](wiki/pages/mod-p-observatory.md)** - `F(w,h) mod p` is eventually periodic; period equals the lcm of eigenvalue orders (small primes). (S2)
- [x] **[Parity via signs](wiki/pages/parity-via-roots-of-unity.md)** - the `(T±P)/2` trick generalized to block count mod `m` via m-th roots of unity. (S1)
- [x] **[Continued fractions of the tower word](wiki/pages/tower-word-continued-fraction.md)** - the tower word is a peakless-valleyless Motzkin path (OEIS A004149); the run constraint collapses the CF to `1/(1-(k+1)x)`. (S2)
- [x] **[Eigenvalue continued fractions](wiki/pages/eigenvalue-continued-fractions.md)** - palindromic characteristic polynomials, Lagrange / Galois, and the two norm-`-1` quadratics `phi` and `sqrt(2)+1` as purely periodic CFs. (S2)
- [x] **[Metallic means](wiki/pages/metallic-means.md)** - the family `delta_a = (a + sqrt(a^2+4))/2`, all norm-`-1` reduced surds with CF `[a; a, a, ...]`; the axis for the metallic-growth meta-classification. (S2)
- [x] **[The algebraic / transcendental wall](wiki/pages/algebraic-transcendental-wall.md)** - C-finite counts carry only algebraic constants exactly; `e` and `pi` enter only through limits (Stirling, Catalan, log-growth). (S9)
- [x] **[Tower parity sectors](wiki/pages/tower-parity-sectors.md)** - why `char_k` factors for even `k`: the signed transfer matrix commutes with "reflect heights, flip signs," splitting `P(k,L)` by last-column parity. (S3)
- [x] **[Castle eigenvalues meet OEIS - the convergent crosswalk](wiki/pages/castle-eigenvalue-oeis-crosswalk.md)** - every metallic rung's convergents matched to OEIS; the k-direction char poly is `(x+1)^L (x-1)^{L-2}`, so `P(k,L)` is a quasi-polynomial in `k`. (S7)
- [x] **[Plastic number](wiki/pages/plastic-number.md)** - `psi`, real root of `x^3 = x + 1`; smallest Pisot; enters the castle as `rho_6 = 2 psi^2` with `H_3` the minimal polynomial of `psi^2`. (S2)
- [x] **[OEIS index](wiki/pages/oeis-index.md)** - script-generated directory of every A-number cited on the wiki, grouped by role (count / metallic / plastic / supporting), with citing pages and mention counts; regenerated by `bin/generate-oeis-index.py`, roles curated in `config/oeis-annotations.tsv`. (S7)
- [x] **[Castle sequence catalogue](wiki/pages/castle-sequence-catalogue.md)** - hand-curated catalogue of every castle-counting sequence with novelty status (known / interlink / novel-candidate / unchecked) and the submission priority list. (S7)

### Enumeration Division

- [ ] **Conditional entropy given block count and area** - refine the uniform-entropy `log_2 F(w,h)` view by conditioning on the two structural statistics. (S8)
- [ ] **Rule-generated-castle detector** - a predicate that identifies low-complexity-but-irregular castles without simulating the rule. (S8)
- [ ] **Parity-bit object-by-object survival** - does the "exactly one bit" story survive at the level of individual castles, not just uniform totals. (S8)
- [ ] **Castle Gray code / loopless enumerator** - a generation algorithm that changes one column height by one per step, with incremental `P` / parity updates, restricted to valid (exact-height, even-block) castles; imported from TODO. (S10)
- [ ] **Viennot heap theory via tower-heap** - the [tower-heap](wiki/pages/tower-heap.md) as a Viennot heap of pieces; its Narayana block-count structure via commutation-monoid / transfer-matrix machinery; imported from TODO. (S10)

- [x] **[Castle entropy and compression](wiki/pages/castle-entropy.md)** - information-theoretic view: uniform entropy `~ w log_2 h - 1`, growth constants as topological entropies, and the compressibility axis on [castle-compression](wiki/pages/castle-compression.md). (S8)
- [x] **[Transfer matrices vs Kitamasa](wiki/pages/castle-count-algorithms.md)** - Kitamasa is `O(D^2 log w)`, transfer-matrix is `O(D^3 log w)`; recorded as rejected as the primary route with the crossover analysis. (S1)
- [x] **[Asymptotics](wiki/pages/castle-graph-spectral-radius.md)** - the count `F(w,h)` grows like `h^w / 2`; per-target dominant costs across the fixed-`w`, fixed-`h`, and `w=h=n` regimes on [castle-count-algorithms](wiki/pages/castle-count-algorithms.md) and [project-euler-502-implementation-notes](wiki/pages/project-euler-502-implementation-notes.md). (S1)
- [x] **[Tower recursion master class](wiki/pages/tower-recursion-master-class.md)** - the two core ideas - towers are independent, parity is a sign - taught end to end to `F(w,h)`. (S1)
- [x] **[Two-direction enumeration](wiki/pages/castle-count-algorithms.md)** - the rational-function path vs the k-direction Berlekamp-Massey path and their tradeoffs. (S1)
- [x] **[Permutation cycles as castle peaks](wiki/pages/permutation-cycle-castle-analogy.md)** - a genuine factorization, not a metaphor. (S1)
- [x] **[Sign of a castle](wiki/pages/castle-sign.md)** - `s(C) = (-1)^blocks` and the `(T±P)/2` projector. (S1)
- [x] **[Castle Foata transformation](wiki/pages/castle-foata-transform.md)** - peaks are the maximal positive runs; `#peaks = #records`. (S1)
- [x] **[Monotone streak factorization](wiki/pages/monotone-streak-factorization.md)** - first differences into up / flat / down streaks, the fast algorithms' canonical form. (S1)
- [x] **[New representations](wiki/pages/castle-representations.md)** - excursion / gap word, cycle-forest form, and signed column-difference sequence. (-)
- [x] **[Encoding catalog](wiki/pages/castle-representations.md)** - binary strings, integer tuples, U/R/D step strings, tower words, skyline tuples. (-)
- [x] **[From Dyck words to castle towers](wiki/pages/generalized-dyck-grammar.md)** - the first-return grammar the castle U/R/D grammar generalizes. (-)
- [x] **[Algorithmic seminar](wiki/pages/kitamasa.md)** - Berlekamp-Massey plus Kitamasa for enormous indices, with companion [berlekamp-massey](wiki/pages/berlekamp-massey.md). (S1)
- [x] **[Formal language of tower words](wiki/pages/tower-word-language.md)** - the tower word as a Motzkin-path language, its unambiguous grammar, and the Dyck / Motzkin hierarchy. (-)
- [x] **[The `(n-1)!` cycle-count upgrade](wiki/pages/castles-as-upgraded-cycle-count.md)** - read PE 502 as the elementary `(n-1)!` labelled-cycle count upgraded step by step into the sign / Foata / streak triad. (S1)
- [x] **[The Pell castle strip](wiki/pages/pell-castle-strip.md)** - an AC end-of-chapter exercise on `D(x) = 1/(1-2x-x^2)`, its two-atom tiling reading, and the castle strip that realizes it (1-smooth, height <= 3, anchored at the base); counts are [pell-numbers](wiki/pages/pell-numbers.md), growth `1+sqrt(2)`. (S2)
- [x] **[Silver-ratio observatory](wiki/pages/pell-castle-strip.md)** - Pell (A000129) and companion Pell (A001333) both occur as castle-strip counts, in one family split by the boundary condition (anchored vs free 1-smooth height-3 strip); completes the Fibonacci/Pell symmetry on [pell-numbers](wiki/pages/pell-numbers.md). (S2)

### Q Division (q-numbers - castles by area)

- [ ] **Prime castles** - refine the area count by the indecomposable factorization (`c_i = 1` for some `i`); prime castles by area `= 2^{n-1} - F_{n-1}`. Richer targets: prime refinement of convex castles (A001523) and of the parity splits on [castle-by-area](wiki/pages/castle-by-area.md), and lining the prime GF up with the classical `A = P/(1-P)` prime-polyomino decomposition (Klarner). (S6)
- [ ] **q-polyomino zoo** - pull the area variable out of the Bousquet-Melou add-a-column perimeter+area GFs for each classical family (Ferrers, stack, parallelogram, column-convex, directed-convex) and read off q-area coefficients to locate castles (stacks -> A001523, non-convex -> A115981, valley -> A332578). (S6)
  - Sub (from TODO): castle recurrences vs A001169 (horizontally convex polyominoes) and the add-a-column functional equations of [column-convex-polygon-enumeration](wiki/pages/column-convex-polygon-enumeration.md).
  - Sub (from TODO): stack / Ferrers / parallelogram sub-families as castle sub-families.
- [ ] **q-Catalan / q-Motzkin joins and bi-statistics** - grade the tower word / generalized-Dyck grammar by area and check against Carlitz q-Catalan and Barcucci q-Motzkin / q-Bessel; push to joint statistics (area x block-count, area x peaks, area x records) hunting q-binomial and Narayana-q coefficients; absorbs the "find the q-equivalent" thread flagged on [q-catalan-numbers](wiki/pages/q-catalan-numbers.md) and [motzkin-numbers](wiki/pages/motzkin-numbers.md). (S6)
- [ ] **Convex to valley bijection** - convex and valley castles are equinumerous in every `(w,h)` cell (both `C(2h+w-3, w-1)`) under a peak/valley mirror; write up the explicit bijection. Imported from TODO. (S6)
- [ ] **`h=3` bounded-height tree-vs-all bijection** - a bijection between bounded-height `h=3` tree castles by area and bounded-height `h=3` all castles by area. (S6)

### S Division (spectral analysis - castles as 2D polyominoes)

Five spectra sit naturally on a castle: transfer-matrix, LGV kernel, skyline DFT, combinatorial Laplacian, Ihara zeta. Seminar targets below, roughly increasing effort.

- [ ] **Seminar centerpiece: hear the shape of a castle** - Kac's question with two drawings as the punchline: the 10-cell adjacency-isospectral pair `(1,1,1,2,3,2)` / `(1,1,2,2,3,1)` and the 11-cell Laplacian-isospectral tree pair; a Sunada-style construction for the 10-cell pair and whether Ihara zeta or the skyline DFT separates what adjacency does not are open inside the item. (S4)
- [ ] **Bronze-spectrum castle hunt** - is `(3+sqrt(13))/2 = 3.303` the adjacency spectral radius of any castle? None among 4.87M enumerated; next is a structured search (products, near-rectangles with notches) rather than more brute force. (S4)
- [ ] **Skyline DFT - individual-castle signatures** - the DFT of a column-height sequence is a complete individual invariant modulo cyclic shift; classify castles by spectral concentration (low-pass / high-pass / sparse-spectrum). Hooks into compressed sensing and turnpike reconstruction. (S4)
- [ ] **LGV kernel spectrum - determinantal universality** - eigenvalues of the non-crossing-path kernel `N(w; i, j)` in `[0,1]`; a sine-kernel bulk limit would put castles in the same universality class as random Young tableaux and GUE. (S4)
- [ ] **Ramanujan castles / Ihara zeta** - `zeta_C(u)` over prime closed walks on the castle graph; the Ramanujan castle as the spectrally most expander-like shape at given size; longer-horizon, hooks into arithmetic combinatorics. (S4)

- [x] **[Tree castle by area](wiki/pages/tree-castle-by-area.md)** - area-graded GF `T_h(x,q) = (1 + P_h(q) x) / (1 - qx - q P_h(q) x^2)`; `h=2` is Narayana's cows A000930, `h=3` is A006498, `h=4` is A000570, `h->inf` is A005251. (S6)
- [x] **[Isospectral castles](wiki/pages/isospectral-castles.md)** - exhaustive over castles with `<=16` cells; smallest non-isomorphic adjacency-isospectral pair at 10 cells, Laplacian-isospectral tree pair at 11, both at 16. (S4)
- [x] **[The castle graph](wiki/pages/castle-graph.md)** - polyomino graph off the skyline: cycle rank equals the number of 2x2 filled blocks, bipartite, planar; tree castles by height give Fibonacci, Jacobsthal, and the k-Fibonacci family. (S4)
- [x] **[Metallic means in castle spectra](wiki/pages/castle-graph-spectral-radius.md)** - `lambda_1(h) = h` for the count; the signed transfer matrix's eigenvalues are twice algebraic units and never metallic; golden and silver appear as adjacency spectral radii of individual castles. (S4)
- [x] **[Spectral analysis](wiki/pages/spectral-analysis.md)** - the centerpiece methods hub: five spectra, a construction-to-spectrum crosswalk, and immediate targets. (S4)

### T Division (transcendentals - pi and siblings)

Umbrella for approximating transcendental constants (pi first, then Catalan's `G`, `zeta(3)`, `gamma`, ...) via castle-native machinery. Ten sampler techniques (rejection, transfer-matrix, Sattolo-Foata, Gray-code, rank/unrank, MCMC, coupling-from-the-past, Wilson-on-LGV, Wang-Landau, random-rule ensembles) are the substrate.

- [ ] **`castle-samplers` page (prerequisite)** - the ten sampler techniques as one dedicated wiki page; every T-Division item depends on it. Promoted from a header parenthetical to a `[ ]` open item. (S9)
- [ ] **pi via CLT-style castle statistics** - pick a castle statistic `X(C)` (area, block count, peak count, tallest-peak position, ...), establish a CLT `(X - mu)/sigma -> N(0,1)`, and read pi off the mode density `1/(sigma sqrt(2 pi))`. Tier-1: area CLT via transfer-matrix sampler. (S9)
- [ ] **pi via castle spectral limit densities** - every RMT limit density carries pi (sine-kernel spacings, Wigner semicircle, Tracy-Widom, Airy edge, Marchenko-Pastur, Kesten-McKay); each is a direct hook into a [spectral-analysis](wiki/pages/spectral-analysis.md) method. (S9)
- [ ] **pi via castle geometric probability** - Buffon needle across skyline, Buffon-Laplace disk fit inside castle, random chord in bounding box, Barbier for uniform-rotation silhouettes; plus Ehrhart / lattice-point routes on the castle polytope. Tier-1: Buffon needle. (S9)
- [ ] **pi via classical asymptotic identities on castles** - Stirling on `(n-1)!` Foata forms, Basel from column-height autocorrelation, Wallis-like ratios from `(T±P)/2`; speculative since not every castle asymptotic yields a factorial or a `1/n^2` decay. (S9)
- [ ] **pi via random walks on castle graphs** - simple random walk return / cover / hitting times on the polyomino graph; loop-erased random walk with conformally invariant limit and pi-laden observables. (S9)
- [ ] **Other transcendentals** - Catalan's `G`, Apery's `zeta(3)`, Euler-Mascheroni `gamma` via the same machinery; placeholder, no concrete castle route inventoried yet. (S9)

### Classification and Variations

- [ ] **Rule-variation enumeration** - convex skeletons plus U/D insertions into runs of R; enumerate variations and study duplicate detection. (S11)
- [ ] **OEIS id of tower-spacing 2D sequences** - the 2D `(h,g)` count table from [tower-spacing-castles](wiki/pages/tower-spacing-castles.md); identify existing rows or submit as new. (S7)
- [ ] **Horizontal-gap reachable-field census** - which algebraic constants arise as `(h,g)` growth constants range; the horizontal-gap analogue of the height-adjacency [reachable-field-census](wiki/pages/reachable-field-census.md). (S2)
- [ ] **No-touching / vertical-spacing variants** - beyond min-gap `g`, the no-touching (diagonal exclusion) and vertical-spacing rule families. (S11)

- [x] **[Gap-rule variations / tower-spacing castles](wiki/pages/tower-spacing-castles.md)** - min-gap-`g` worked out via a column-sweep transfer matrix; at `h=2`, `g=2` is plastic-squared and `g=3` is golden. (S11)
- [x] **[Parity and block-count catalog](wiki/pages/parity-via-roots-of-unity.md)** - even / odd / any-residue block counts via character sums, the full selection trichotomy on [block-count-constraints](wiki/pages/block-count-constraints.md), and the block-count distribution as the Narayana polynomial on [tower-narayana-polynomial](wiki/pages/tower-narayana-polynomial.md). (-)
- [x] **[Castle classification](wiki/pages/castle-classification.md)** - 42-type framework (7 base plus 35 proposed) across 7 structural axes plus meta-axis 8 (metallic growth) and axis 9 (spectral predicates). (S11)
- [x] **[Castle snippets](wiki/pages/castle-snippets.md)** - living reference of short tested Python one-liners: enumeration, one predicate per Axis 1-7 type, metallic-means matcher, OEIS lookups. (S11)

### Miscellaneous

- [ ] **General closed form for `P(k,L)`** - for all `k` and all `L`. In `k`, `P(k,L) = (-1)^k A_L(k) + B_L(k)` with explicit `A_L, B_L` for `L<=12` on [castle-eigenvalue-oeis-crosswalk](wiki/pages/castle-eigenvalue-oeis-crosswalk.md); what remains is a uniform formula and a proof of the `(x+1)^L (x-1)^{L-2}` factorization. (S1)
- [ ] **Minimality of empirical recurrence orders** - prove the conjectured orders are minimal (`k+1` in `L`, exactly `2L-2` in `k`); the k-direction half reduces to `deg A_L = L-1` and `deg B_L = L-3`. (S1)
- [ ] **Convex / unimodal exact enumeration with parity** - the U/R/D route was attempted and failed; the area-graded split is done on [castle-by-area](wiki/pages/castle-by-area.md), the exact `(w,h)` enumeration remains open. (S11)
- [ ] **Higher-dimensional castles** - 3D blocks, multiple stacked rows per level, or blocks with integer height greater than 1. (S11)
- [ ] **Convex core uniqueness** - is every castle a variation of a unique convex core? Characterize the minimal convex skeleton. (S11)
- [ ] **Statistical physics links** - directed animals, column-convex polygons, hard-square type models. (S11)
