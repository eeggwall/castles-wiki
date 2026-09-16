# Project and Seminar Ideas

A working list of project and seminar ideas for Project Euler problem 502 (Castles).

## Ideas with Wiki Pages

Ideas that have gotten some attention and have their own wiki pages.

- [x] **[Recurrence discovery](wiki/pages/recurrence-discovery.md)** — run Berlekamp–Massey on P(k,L) in both directions; order `k+1` in L (confirmed) and exactly `2L−2` in k for L ≥ 4.
- [x] **[Closed-form hunting](wiki/pages/closed-form-hunting.md)** — P(k,2) = (−1)^k(k+1) and P(k,3) = (−1)^k(k+1)²; no simple form for L ≥ 4.
- [x] **[Generating-function gallery](wiki/pages/generating-function-gallery.md)** — catalogue num_k/den_k, denominator roots, and the C-finite recurrences; dominant eigenvalue ρ_k ~ k/log k.
- [x] **[Mod-p observatory](wiki/pages/mod-p-observatory.md)** — F(w,h) mod p is eventually periodic; period = lcm of eigenvalue orders (small primes).
- [x] **[Tower recursion master class](wiki/pages/tower-recursion-master-class.md)** — the two core ideas — towers are independent and parity is a sign — taught end-to-end to F(w,h).
- [x] **[Parity via signs](wiki/pages/parity-via-roots-of-unity.md)** — the (T±P)/2 trick generalized to block count mod m via m-th roots of unity (also the "block count mod m" thread).
- [x] **[Two-direction enumeration](wiki/pages/castle-count-algorithms.md)** — the rational-function path vs the k-direction Berlekamp–Massey path and their tradeoffs.
- [x] **[Permutation cycles ↔ castle peaks/excursions](wiki/pages/permutation-cycle-castle-analogy.md)** — a genuine factorization, not a metaphor.
- [x] **[Sign of a castle](wiki/pages/castle-sign.md)** — s(C) = (−1)^blocks and the (T±P)/2 projector.
- [x] **[Castle Foata transformation](wiki/pages/castle-foata-transform.md)** — peaks are the maximal positive runs; #peaks = #records.
- [x] **[Monotone streak factorization](wiki/pages/monotone-streak-factorization.md)** — first differences into up/flat/down streaks, the fast algorithms' canonical form.
- [x] **[New representations](wiki/pages/castle-representations.md)** — excursion/gap word, cycle-forest form, and signed column-difference sequence.
- [x] **[Encoding catalog](wiki/pages/castle-representations.md)** — binary strings, integer tuples, U/R/D step strings, tower words, skyline tuples.
- [x] **[From Dyck words to castle towers](wiki/pages/generalized-dyck-grammar.md)** — the first-return grammar.
- [x] **[Algorithmic seminar](wiki/pages/kitamasa.md)** — Berlekamp–Massey + Kitamasa for enormous indices ([berlekamp-massey](wiki/pages/berlekamp-massey.md)).
- [x] **[Formal language of tower words](wiki/pages/tower-word-language.md)** — the tower word as a Motzkin-path language, its unambiguous grammar, and the Dyck/Motzkin hierarchy.
- [x] **[Continued fractions of the tower word](wiki/pages/tower-word-continued-fraction.md)** — the tower word is a peakless-valleyless Motzkin path (OEIS A004149); Flajolet's Catalan S-fraction / Motzkin J-fraction framework, and the run constraint as the collapse to `1/(1−(k+1)x)`.
- [x] **[Eigenvalue continued fractions](wiki/pages/eigenvalue-continued-fractions.md)** — the castle's self-reciprocal (palindromic/anti-palindromic) characteristic polynomials, Lagrange/Galois, and the two norm-−1 quadratics φ and √2+1 as purely periodic continued fractions.
- [x] **[The algebraic/transcendental wall](wiki/pages/algebraic-transcendental-wall.md)** — C-finite counts carry only algebraic constants exactly; e and π are locked out of closed forms and enter only through limits (Stirling, Catalan, natural-log growth).
- [x] **[Castles as an upgrade of the (n−1)! cycle count](wiki/pages/castles-as-upgraded-cycle-count.md)** — seminar-shaped analysis: the elementary `(n−1)!` warm-up (quotient-by-rotation, fix-a-starting-point) upgraded step-by-step into the castle's [castle-sign](wiki/pages/castle-sign.md) / [castle-foata-transform](wiki/pages/castle-foata-transform.md) / [monotone-streak-factorization](wiki/pages/monotone-streak-factorization.md) triad; `F(4,2)=10` hand-checked twice.
- [x] **[The Pell castle strip](wiki/pages/pell-castle-strip.md)** — seminar-shaped: an Analytic Combinatorics end-of-chapter exercise on `D(x) = 1/(1−2x−x²)` opens directly onto PE 502's structural rules. The denominator splits into `2x` (per-column binary state, `T(1,L) = 2^L`) and `x²` (the mandatory-gap rule-3 tax); the counts are [pell-numbers](wiki/pages/pell-numbers.md) (OEIS A000129 shifted), growth constant `1 + √2 = [2;2,2,…]`.
- [x] **[Metallic means](wiki/pages/metallic-means.md)** — the family `δ_a = (a + √(a²+4))/2` (Fibonacci/Pell/bronze/copper/…), all norm-`−1` reduced surds with purely periodic continued fractions `[a; a, a, …]`; the axis for the "`<metal>` `<axis>` growth castle" meta-classification (Axis 8 of [castle-classification](wiki/pages/castle-classification.md)).
- [x] **[Castle classification](wiki/pages/castle-classification.md)** — the 42-type framework (7 base from the polyomino literature, 35 proposed; hydrated from `charlesreid1.com/wiki/Project_Euler/502/Castle_Types`), organized into 7 structural axes (convexity/modality, rate-of-change, path-like, symmetry, extremum, parity/area, value-pattern) plus a transversal metallic-mean growth-constant axis; ties each type to the wiki thread that already touches it.
- [x] **[Castle snippets](wiki/pages/castle-snippets.md)** — a living reference of short, tested Python one-liners for enumeration, classification predicates (one per Axis 1-7 wiki-tracked type), growth-constant probes ([metallic-means](wiki/pages/metallic-means.md) matcher), and OEIS lookups. Discipline enforced: every snippet was executed during ingest and its printed output pinned in the page.
- [x] **[Spectral analysis](wiki/pages/spectral-analysis.md)** — the centerpiece methods hub for spectral analysis of castles as 2D polyominoes. Five spectra (transfer-matrix, LGV kernel, skyline DFT, combinatorial Laplacian, Ihara zeta), a construction-↔-spectrum crosswalk connecting each Axes 1-8 type to its forced spectral consequence, and two sketched immediate targets (`λ_1(h)` for `h = 2..5`, isospectral-castle hunt). Toolkit-side companion to [castle-classification](wiki/pages/castle-classification.md) Axis 9.

## Rough ideas

Partially-formed notions worth developing further.

### Numbers Division

- [ ] **Castle sequence bank** — count F, T, P, A, F_odd, etc., and mine OEIS for connections.
- [ ] **Larger-prime periodicity** — extend the mod-p observatory to larger primes (and 10^9+7); the periods become infeasible to enumerate, but the eigenvalue-order structure persists.
- [ ] **Silver-ratio observatory** — sweep the wiki's castle sub-families (by area, by parity, by block/peak count, prime castles, convex/valley) for Pell (A000129) and companion Pell (A001333). The tower-word growth constant is already `1+√2` ([tower-word-continued-fraction](wiki/pages/tower-word-continued-fraction.md)); the [pell-castle-strip](wiki/pages/pell-castle-strip.md) shows one physical realization. Natural pair to the Fibonacci-in-`castle-by-area` result `2^{n−1} − F_{n−1}` — a Pell-in-castle-somewhere result would complete the Fibonacci/Pell symmetry on [pell-numbers](wiki/pages/pell-numbers.md).
- [ ] **[Metallic-ratio ladder](wiki/pages/metallic-means.md)** — φ (a=1) and 1+√2 (a=2) are the first two roots of `x² − ax − 1`; the "silver, bronze, copper…" ladder continues with `(3+√13)/2, (4+√20)/2, …` — each with its own linear-recurrence integer sequence, its own `[a; a, a, …]` continued fraction, and its own norm-−1 reduced surd. **Which castle rule-modifications produce which metallic ratios as growth constants?** The [pell-castle-strip](wiki/pages/pell-castle-strip.md) concrete knob: a denominator `1 − w_1·x − w_2·x²` grows at `(w_1 + √(w_1² + 4·w_2))/2`, which is a metallic mean iff `w_2 = 1`. So the ladder cleanly corresponds to "how many states per column with a fixed mandatory-gap rule" — the Axis-8 meta-classification "`<metal>` width growth castle" of [castle-classification](wiki/pages/castle-classification.md), with golden and silver populated and bronze/copper/nickel open.
- [ ] **Convergents-to-castle OEIS crosswalk** — every eigenvalue on [eigenvalue-continued-fractions](wiki/pages/eigenvalue-continued-fractions.md) has convergents that are rational approximations, whose numerator and denominator sequences are integer sequences in their own right. Fibonacci convergents to φ = A000045; Pell convergents to `1+√2` = A000129/A001333. The higher-degree castle eigenvalues (order `2L−2`) lose Lagrange periodicity but keep the reciprocal-root symmetry — do their multi-variable "convergents" hit any OEIS sequences? A concrete quantitative link between the CF-period side and the mod-p-order side the [eigenvalue-continued-fractions](wiki/pages/eigenvalue-continued-fractions.md) page draws in the abstract.

### Enumeration Division

- [ ] **Transfer matrices vs Kitamasa** — why the L-direction transfer matrix is O(D^3 log w) but the rational-function form is O(D^2 log w).
- [ ] **Asymptotics** — leading term h^w, corrections, and the regimes where w is fixed, h is fixed, or w = h = n.
- [x] **The (n−1)! cycle-count upgrade** — read PE 502 as the elementary `(n−1)!` labelled-cycle count (quotient-by-rotation, fix-a-starting-point) upgraded step-by-step into the castle's [castle-sign](wiki/pages/castle-sign.md) / [castle-foata-transform](wiki/pages/castle-foata-transform.md) / [monotone-streak-factorization](wiki/pages/monotone-streak-factorization.md) triad; written up as [castles-as-upgraded-cycle-count](wiki/pages/castles-as-upgraded-cycle-count.md).
- [x] **The Pell castle strip** — an AC end-of-chapter exercise on `D(x) = 1/(1−2x−x²)` spirals into PE 502's structural rules (`2x` = per-column binary state, `x²` = mandatory-gap rule 3), with [pell-numbers](wiki/pages/pell-numbers.md) as the count sequence and `1+√2` as the growth constant; written up as [pell-castle-strip](wiki/pages/pell-castle-strip.md).

### Q Division (q-numbers — castles by area)

- [ ] **Prime castles** — refine the area count by the indecomposable factorization: a castle is **prime** if no full-width horizontal cut splits it into two non-empty castles, which for a castle-as-composition `c = (c_1,…,c_w)` means some `c_i = 1` (a cut exists iff every column has height ≥ 2). Every castle factors uniquely into a stack of unit full-width rows on top of a prime castle, so prime castles by area = `2^{n−1} − F_{n−1}` — all compositions minus the parts-≥2 compositions, which are Fibonacci (`F_{n−1}`) — worth verifying against OEIS. The richer targets are the prime refinement of the convex castles (A001523) and of the parity splits on [castle-by-area](wiki/pages/castle-by-area.md) (likely new), and lining the prime g.f. `P(q)` up with the classical `A = P/(1−P)` prime-polyomino decomposition (Klarner).

- [ ] **q-polyomino zoo** — pull the area variable out of the Bousquet-Mélou add-a-column perimeter+area g.f.s ([column-convex-polygon-enumeration](wiki/pages/column-convex-polygon-enumeration.md)) for each classical family — Ferrers, stack, parallelogram, column-convex, directed-convex — and read off the q-area coefficients to locate castles (stacks ↔ A001523, non-convex ↔ A115981, valley ↔ A332578). A "which restricted polyomino class = which castle class" table, each graded by area.

- [ ] **q-Catalan / q-Motzkin joins and bi-statistics** — grade the tower word / generalized-Dyck grammar by area (column-height sum) and check against the Carlitz q-Catalan and the Barcucci q-Motzkin / q-Bessel families ([steep-polyominoes-q-motzkin-bessel](wiki/pages/steep-polyominoes-q-motzkin-bessel.md)); `q = 1` must land on the [castle-by-area](wiki/pages/castle-by-area.md) sequences. Then push to joint statistics (area × block-count, area × peaks, area × records) hunting q-binomial / Gaussian-binomial and Narayana-q coefficients — the open "q-equivalent thread" flagged on [q-catalan-numbers](wiki/pages/q-catalan-numbers.md) and [motzkin-numbers](wiki/pages/motzkin-numbers.md).

### S Division (spectral analysis — castles as 2D polyominoes)

Five different spectra sit naturally on a castle, each classifying different things. Seminar targets, roughly increasing effort:

- [ ] **λ_1(h) for small h — the transfer-matrix growth spectrum** — the signed transfer matrix M(x) has dominant eigenvalue λ_1(h) governing F(w, h) ~ c(h)·λ_1(h)^w. Compute the characteristic polynomial and root λ_1(h) for h = 2, 3, 4, 5 symbolically (almost certainly named algebraic numbers with clean minimal polynomials). h = 2 already known: λ_1 = 1+√2 (silver, matches [pell-castle-strip](wiki/pages/pell-castle-strip.md) / [metallic-means](wiki/pages/metallic-means.md)). Explicit values for h = 3, 4, 5 would classify castle families by growth type at a glance and directly populate the [metallic-means](wiki/pages/metallic-means.md) ladder or reveal non-metallic algebraic growth constants.
- [ ] **Isospectral castles — hear the shape of a castle** — Kac's "hear the shape of a drum" for the castle setting. Treat filled cells as graph vertices with orthogonal-adjacency edges, compute the combinatorial Laplacian L = D − A, look for pairs of non-isomorphic castles with identical spectrum. Enumerate castles up to size ≤ 20 (via [castle-snippets](wiki/pages/castle-snippets.md) primitives), compute Laplacian spectra, hash for collisions, report the smallest isospectral pair. Both computational and clean-statement outcomes; pure combinatorics.
- [ ] **Skyline DFT — individual-castle signatures** — the DFT of a column-height sequence c_1, …, c_w is a complete individual invariant (modulo cyclic shift). Classify castles by spectral concentration: low-pass (smooth, mountain-shaped) vs high-pass (jagged/crenellated) vs sparse-spectrum (periodic "battlement" castles). The battlement / crenellated type of [castle-classification](wiki/pages/castle-classification.md) Axis 7 falls out as "two-atom DFT support" here. Hooks into compressed sensing and turnpike reconstruction — hard sub-problem: which sparse-spectrum sequences correspond to valid castles?
- [ ] **LGV kernel spectrum — determinantal universality** — the non-crossing-path kernel N(w; i, j) from the LGV determinant framework has eigenvalues in [0, 1] interpretable as local-configuration probabilities. Castles are a determinantal point process iff N is a projection kernel (all eigenvalues 0 or 1). **Prediction to test:** a sine-kernel bulk limit would put castles in the same universality class as random Young tableaux, GUE, and Aztec diamonds — peak positions would exhibit `sin(π(x−y))/(π(x−y))` spacing statistics. Hooks into random matrix universality.
- [ ] **Ramanujan castles / Ihara zeta** — the Ihara zeta function ζ_C(u) = ∏_{[γ]}(1 − u^|γ|)^{−1} over prime closed walks on the castle graph is a rational function whose poles are the spectrum of a modified edge-adjacency operator — a Selberg-zeta analog for castles. A castle is **Ramanujan** if its non-trivial adjacency spectrum lies in [−2√(d−1), 2√(d−1)] (max degree d): the "spectrally most expander-like" castle shape at given size. Now Axis 9's first named type on [castle-classification](wiki/pages/castle-classification.md). Longer-horizon program; hooks into arithmetic combinatorics.

### Classification and Variations

- [ ] **Gap-rule variations** — no adjacency, minimum gap g, no touching allowed, all via maximal-runs-of-1s encoding. Corresponds directly to the m-disparate / m-smooth axis of [castle-classification](wiki/pages/castle-classification.md).
- [ ] **Parity and block-count catalog** — even, odd, and any block counts; block-count distributions; area vs block count (column-height sum vs run count).
- [ ] **Rule-variation enumeration** — convex skeletons plus U/D insertions into runs of R; enumerate variations and study duplicate detection.
- [x] **[Taxonomy of castle classes](wiki/pages/castle-classification.md)** — the 42-type catalog from https://charlesreid1.com/wiki/Project_Euler/502/Castle_Types, organized into 7 structural axes (convexity/modality, rate-of-change, path-like, symmetry, extremum, parity/area, value-pattern) plus a transversal growth-constant axis via [metallic-means](wiki/pages/metallic-means.md).

### Miscellaneous

- [ ] **General closed form for P(k,L)** — for all k and all L.
- [ ] **Minimality of empirical recurrence orders** — prove the conjectured orders are minimal (about k+1 in L, about 2L in k).
- [ ] **Convex/unimodal exact enumeration with parity** — enumerate convex and unimodal castles exactly with the parity constraint; the U/R/D route was attempted and failed, so this is open.
- [ ] **q-analogs** — refine castle counts by area, block count, number of peaks, or perimeter; look for q-Catalan and q-Motzkin connections.
- [ ] **Higher-dimensional castles** — 3D blocks, multiple stacked rows per level, or blocks with integer height greater than 1.
- [ ] **Convex core uniqueness** — is every castle a variation of a unique convex core? Characterize the minimal convex skeleton.
- [ ] **Statistical physics links** — directed animals, column-convex polygons, and hard-square type models.
