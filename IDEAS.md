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
- [x] **[Encoding atlas](wiki/pages/castle-representations.md)** — binary strings, integer tuples, U/R/D step strings, tower words, skyline tuples.
- [x] **[From Dyck words to castle towers](wiki/pages/generalized-dyck-grammar.md)** — the first-return grammar.
- [x] **[Algorithmic seminar](wiki/pages/kitamasa.md)** — Berlekamp–Massey + Kitamasa for enormous indices ([berlekamp-massey](wiki/pages/berlekamp-massey.md)).
- [x] **[Formal language of tower words](wiki/pages/tower-word-language.md)** — the tower word as a Motzkin-path language, its unambiguous grammar, and the Dyck/Motzkin hierarchy.
- [x] **[Continued fractions of the tower word](wiki/pages/tower-word-continued-fraction.md)** — the tower word is a peakless-valleyless Motzkin path (OEIS A004149); Flajolet's Catalan S-fraction / Motzkin J-fraction framework, and the run constraint as the collapse to `1/(1−(k+1)x)`.
- [x] **[Eigenvalue continued fractions](wiki/pages/eigenvalue-continued-fractions.md)** — the castle's self-reciprocal (palindromic/anti-palindromic) characteristic polynomials, Lagrange/Galois, and the two norm-−1 quadratics φ and √2+1 as purely periodic continued fractions.
- [x] **[The algebraic/transcendental wall](wiki/pages/algebraic-transcendental-wall.md)** — C-finite counts carry only algebraic constants exactly; e and π are locked out of closed forms and enter only through limits (Stirling, Catalan, natural-log growth).
- [x] **[Castles as an upgrade of the (n−1)! cycle count](wiki/pages/castles-as-upgraded-cycle-count.md)** — seminar-shaped analysis: the elementary `(n−1)!` warm-up (quotient-by-rotation, fix-a-starting-point) upgraded step-by-step into the castle's [castle-sign](wiki/pages/castle-sign.md) / [castle-foata-transform](wiki/pages/castle-foata-transform.md) / [monotone-streak-factorization](wiki/pages/monotone-streak-factorization.md) triad; `F(4,2)=10` hand-checked twice.

## Rough ideas

Partially-formed notions worth developing further.

### Numbers Division

- [ ] **Castle sequence bank** — count F, T, P, A, F_odd, etc., and mine OEIS for connections.
- [ ] **Larger-prime periodicity** — extend the mod-p observatory to larger primes (and 10^9+7); the periods become infeasible to enumerate, but the eigenvalue-order structure persists.

### Enumeration Division

- [ ] **Transfer matrices vs Kitamasa** — why the L-direction transfer matrix is O(D^3 log w) but the rational-function form is O(D^2 log w).
- [ ] **Asymptotics** — leading term h^w, corrections, and the regimes where w is fixed, h is fixed, or w = h = n.

### Q Division (q-numbers — castles by area)

- [ ] **Prime castles** — refine the area count by the indecomposable factorization: a castle is **prime** if no full-width horizontal cut splits it into two non-empty castles, which for a castle-as-composition `c = (c_1,…,c_w)` means some `c_i = 1` (a cut exists iff every column has height ≥ 2). Every castle factors uniquely into a stack of unit full-width rows on top of a prime castle, so prime castles by area = `2^{n−1} − F_{n−1}` — all compositions minus the parts-≥2 compositions, which are Fibonacci (`F_{n−1}`) — worth verifying against OEIS. The richer targets are the prime refinement of the convex castles (A001523) and of the parity splits on [castle-by-area](wiki/pages/castle-by-area.md) (likely new), and lining the prime g.f. `P(q)` up with the classical `A = P/(1−P)` prime-polyomino decomposition (Klarner).

- [ ] **q-polyomino zoo** — pull the area variable out of the Bousquet-Mélou add-a-column perimeter+area g.f.s ([column-convex-polygon-enumeration](wiki/pages/column-convex-polygon-enumeration.md)) for each classical family — Ferrers, stack, parallelogram, column-convex, directed-convex — and read off the q-area coefficients to locate castles (stacks ↔ A001523, non-convex ↔ A115981, valley ↔ A332578). A "which restricted polyomino class = which castle class" table, each graded by area.

- [ ] **q-Catalan / q-Motzkin joins and bi-statistics** — grade the tower word / generalized-Dyck grammar by area (column-height sum) and check against the Carlitz q-Catalan and the Barcucci q-Motzkin / q-Bessel families ([steep-polyominoes-q-motzkin-bessel](wiki/pages/steep-polyominoes-q-motzkin-bessel.md)); `q = 1` must land on the [castle-by-area](wiki/pages/castle-by-area.md) sequences. Then push to joint statistics (area × block-count, area × peaks, area × records) hunting q-binomial / Gaussian-binomial and Narayana-q coefficients — the open "q-equivalent thread" flagged on [q-catalan-numbers](wiki/pages/q-catalan-numbers.md) and [motzkin-numbers](wiki/pages/motzkin-numbers.md).

### The Atlas

- [ ] **Gap-rule atlas** — no adjacency, minimum gap g, no touching allowed, all via maximal-runs-of-1s encoding.
- [ ] **Parity and block-count atlas** — even, odd, and any block counts; block-count distributions; area vs block count (column-height sum vs run count).
- [ ] **Variation atlas** — convex skeletons plus U/D insertions into runs of R; enumerate variations and study duplicate detection.
- [ ] **Taxonomy of castle classes** (and determining which rules each type drops, and counting them): https://charlesreid1.com/wiki/Project_Euler/502/Castle_Types

### Miscellaneous

- [ ] **General closed form for P(k,L)** — for all k and all L.
- [ ] **Minimality of empirical recurrence orders** — prove the conjectured orders are minimal (about k+1 in L, about 2L in k).
- [ ] **Convex/unimodal exact enumeration with parity** — enumerate convex and unimodal castles exactly with the parity constraint; the U/R/D route was attempted and failed, so this is open.
- [ ] **q-analogs** — refine castle counts by area, block count, number of peaks, or perimeter; look for q-Catalan and q-Motzkin connections.
- [ ] **Higher-dimensional castles** — 3D blocks, multiple stacked rows per level, or blocks with integer height greater than 1.
- [ ] **Convex core uniqueness** — is every castle a variation of a unique convex core? Characterize the minimal convex skeleton.
- [ ] **Statistical physics links** — directed animals, column-convex polygons, and hard-square type models.
