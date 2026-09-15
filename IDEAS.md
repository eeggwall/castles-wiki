# Project and Seminar Ideas

A working list of project and seminar ideas for Project Euler problem 502 (Castles).

## Ideas with Wiki Pages

Ideas that have gotten some attention and have their own wiki pages.

- [x] **[Recurrence discovery](wiki/pages/recurrence-discovery.md)** — run Berlekamp–Massey on P(k,L) in both directions; order `k+1` in L (confirmed) and exactly `2L−2` in k for L ≥ 4.
- [x] **[Closed-form hunting](wiki/pages/closed-form-hunting.md)** — P(k,2) = (−1)^k(k+1) and P(k,3) = (−1)^k(k+1)²; no simple form for L ≥ 4.
- [x] **[Generating-function gallery](wiki/pages/generating-function-gallery.md)** — catalogue num_k/den_k, denominator roots, and the C-finite recurrences; dominant eigenvalue ρ_k ~ k/log k.
- [x] **[Mod-p observatory](wiki/pages/mod-p-observatory.md)** — F(w,h) mod p is eventually periodic; period = lcm of eigenvalue orders (small primes).

## Rough ideas

Partially-formed notions worth developing further.

### Numbers Division

- [ ] **Castle sequence bank** — count F, T, P, A, F_odd, etc., and mine OEIS for connections.
- [ ] **Larger-prime periodicity** — extend the mod-p observatory to larger primes (and 10^9+7); the periods become infeasible to enumerate, but the eigenvalue-order structure persists.

### Enumeration Division

- [ ] **Tower recursion master class** — proving T(k,L) = (k+1)^L from a binary-string bijection plus sub-block independence; then the derived signed P(k,L) recursion and F(w,h) formula; demonstrate the even and odd approaches.
- [ ] **Parity via signs** — the (T-P)/2 and (T+P)/2 trick, generalizing to block count modulo m using roots of unity.
- [ ] **Two-direction enumeration** — compare the rational-function path (fixed k, Kitamasa in w) with the k-direction BM path (fixed w, Kitamasa in k); cover the complexity tradeoffs.
- [ ] **Transfer matrices vs Kitamasa** — why the L-direction transfer matrix is O(D^3 log w) but the rational-function form is O(D^2 log w).
- [ ] **Asymptotics** — leading term h^w, corrections, and the regimes where w is fixed, h is fixed, or w = h = n.

### The Atlas

- [ ] **Taxonomy of castle classes** — column-convex, convex, unimodal, directed, parallelogram, Ferrers, staircase, bar chart; identify which PE 502 rules each class keeps/drops.
- [ ] **Gap-rule atlas** — no adjacency, minimum gap g, no touching allowed, all via maximal-runs-of-1s encoding.
- [ ] **Parity and block-count atlas** — even, odd, and any block counts; block-count distributions; area vs block count (column-height sum vs run count).
- [ ] **Encoding atlas** — binary strings, integer tuples, U/R/D step strings, tower words, and skyline tuples; catalog which encoding reveals which structure.
- [ ] **Variation atlas** — convex skeletons plus U/D insertions into runs of R; enumerate variations and study duplicate detection.

### Knuth

- [ ] **Permutation cycles ↔ castle peaks/excursions** — Knuth factors a permutation into disjoint cycles by repeatedly following i → σ(i) until it closes. The tower grammar does the same for a castle skyline. A tower factors as empty, or R-gap followed by a tower, or peak followed by stop or gap. Each peak is a cycle-like atom; disjoint cycles become disjoint peaks separated by R-gaps. A genuine factorization, not a metaphor.
- [ ] **Sign of a castle** — for a permutation, sign = (-1)^(n - number of cycles). For a castle, each D move completes a block, so the castle analogue of cycle count is the number of down-streaks, and the natural sign is (-1)^(number of blocks). The PE 502 even-block trick (unsigned - signed)/2 is exactly the standard even/odd permutation trick (total + signed)/2. This gives a clean seminar module connecting the signed tower recursion P(k,L) on the wiki to a permutation sign homomorphism.
- [ ] **Castle Foata transformation** — Knuth's canonical cycle form writes each cycle smallest-element-first, orders cycles by decreasing first element, writes singleton cycles explicitly, then erases parentheses to recover a one-line permutation. That flattening is Foata's fundamental transformation; it maps number of cycles to number of left-to-right maxima. Define and prove the castle analogue of this transform.
- [ ] **Monotone streak factorization and fast algorithms** — represent the castle by column heights c_i and take first differences d_i = c_{i+1} - c_i. Factoring d into maximal up-streaks, flat runs, and down-streaks enables run-length factorization. From the streak factorization, the existing fast algorithms read naturally as a "sum over canonical forms".
- [ ] **New representations worth writing up:**
  - **Excursion/gap word** — a tower is alternating unit U/D moves and R-runs, so encode it as (direction_1, gap_1, direction_2, gap_2, ...); validity becomes partial sums ≥ 0 and final sum 0.
  - **Cycle-forest form** — match each U with its D to get a rooted forest of blocks, the castle analogue of a permutation written as parenthesized cycles.
  - **Signed column-difference sequence** — the run-length-encoded difference sequence, where down-streaks are the atoms carrying sign.

### Miscellaneous

- [ ] **From Dyck words to castle towers via first-return grammar** — *potential opening seminar*.
- [ ] **General closed form for P(k,L)** — for all k and all L.
- [ ] **Minimality of empirical recurrence orders** — prove the conjectured orders are minimal (about k+1 in L, about 2L in k).
- [ ] **Convex/unimodal exact enumeration with parity** — enumerate convex and unimodal castles exactly with the parity constraint; the U/R/D route was attempted and failed, so this is open.
- [ ] **Block count mod m** — generalize the even-block rule to block count mod m using m-th roots of unity in the signed tower recursion.
- [ ] **q-analogs** — refine castle counts by area, block count, number of peaks, or perimeter; look for q-Catalan and q-Motzkin connections.
- [ ] **Higher-dimensional castles** — 3D blocks, multiple stacked rows per level, or blocks with integer height greater than 1.
- [ ] **Formal language of tower words** — prove the grammar is unambiguous, study its algebraic generating functions, and relate it to Dyck and Motzkin languages.
- [ ] **Convex core uniqueness** — is every castle a variation of a unique convex core? Characterize the minimal convex skeleton.
- [ ] **Statistical physics links** — directed animals, column-convex polygons, and hard-square type models.
- [ ] **Algorithmic seminar** — Berlekamp–Massey, Kitamasa, and linear-recurrence jumping for enormous indices modulo p.
