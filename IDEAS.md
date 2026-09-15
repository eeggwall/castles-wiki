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

## Rough ideas

Partially-formed notions worth developing further.

### Numbers Division

- [ ] **Castle sequence bank** — count F, T, P, A, F_odd, etc., and mine OEIS for connections.
- [ ] **Larger-prime periodicity** — extend the mod-p observatory to larger primes (and 10^9+7); the periods become infeasible to enumerate, but the eigenvalue-order structure persists.

### Enumeration Division

- [ ] **Transfer matrices vs Kitamasa** — why the L-direction transfer matrix is O(D^3 log w) but the rational-function form is O(D^2 log w).
- [ ] **Asymptotics** — leading term h^w, corrections, and the regimes where w is fixed, h is fixed, or w = h = n.

### The Atlas

- [ ] **Taxonomy of castle classes** — column-convex, convex, unimodal, directed, parallelogram, Ferrers, staircase, bar chart; identify which PE 502 rules each class keeps/drops.
- [ ] **Gap-rule atlas** — no adjacency, minimum gap g, no touching allowed, all via maximal-runs-of-1s encoding.
- [ ] **Parity and block-count atlas** — even, odd, and any block counts; block-count distributions; area vs block count (column-height sum vs run count).
- [ ] **Variation atlas** — convex skeletons plus U/D insertions into runs of R; enumerate variations and study duplicate detection.

### Miscellaneous

- [ ] **General closed form for P(k,L)** — for all k and all L.
- [ ] **Minimality of empirical recurrence orders** — prove the conjectured orders are minimal (about k+1 in L, about 2L in k).
- [ ] **Convex/unimodal exact enumeration with parity** — enumerate convex and unimodal castles exactly with the parity constraint; the U/R/D route was attempted and failed, so this is open.
- [ ] **q-analogs** — refine castle counts by area, block count, number of peaks, or perimeter; look for q-Catalan and q-Motzkin connections.
- [ ] **Higher-dimensional castles** — 3D blocks, multiple stacked rows per level, or blocks with integer height greater than 1.
- [ ] **Formal language of tower words** — prove the grammar is unambiguous, study its algebraic generating functions, and relate it to Dyck and Motzkin languages.
- [ ] **Convex core uniqueness** — is every castle a variation of a unique convex core? Characterize the minimal convex skeleton.
- [ ] **Statistical physics links** — directed animals, column-convex polygons, and hard-square type models.
