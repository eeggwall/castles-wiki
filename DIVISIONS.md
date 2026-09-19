# Divisions

Seven letters partition the castle wiki's research surface. Each Division has a one-line descriptor in four parts, a conceptual coverage list, and a set of crossovers with the other letters. The Divisions here supersede the Division headings in `IDEAS.md`: Numbers -> N, Enumeration -> E, Q -> Q, S -> S, T -> T, and Classification and Miscellaneous both -> Z. R is new and gathers the representation pages that no earlier Division claimed.

Crossovers are written `home/lens`: `E/R` and `R/E` are different subplots. Crossover names are hooks (a titled subplot), not descriptions of theme.

## Descriptors

- **R - Representations:** encodings, equivalences, grammars, and what survives translation.
- **E - Enumeration:** counting methods, generating functions, recurrences, and sampling.
- **N - Numbers:** sequences, exact arithmetic, difficult scales, and numerical patterns.
- **Z - Zoo:** specimens, taxonomy, comparative morphology, and public interpretation.
- **Q - q-Analogues:** area gradings, q-generating functions, joint statistics, and the bijections that preserve area.
- **S - Spectra:** castle graphs, transfer and kernel eigenvalues, isospectral pairs, and what a castle sounds like.
- **T - Transcendentals:** samplers, limit laws, geometric probability, and pi pulled out of castle ensembles.

## Conceptual coverage

### R - Representations

- Column-height vectors, w/h notation, and the tower word / generalized Dyck grammar.
- Lattice-path and permutation-cycle readings, with the two-line array and Foata intercalation as the source-level grounding.
- Polyomino embedding and the castle graph as an encoding rather than an object.
- Substructures: strips, snippets, and proper projections between heights.
- Compression and entropy: what the parity clause costs in bits and whether it survives object by object.
- Equivalences and translation loss: which invariants each encoding keeps or drops.

### E - Enumeration

- Tower recursion and the transfer matrix as the one-blackboard count.
- Sign and parity via roots of unity; the castle as an upgraded cycle count.
- Recurrence machinery: Kitamasa, Berlekamp-Massey, minimal recurrence order, closed forms for `P(k,L)`.
- Convex counting by Vandermonde and the insert-into-every-slot mechanism.
- Generation: Knuth's Algorithm M, castle Gray codes, loopless enumerators, rank and unrank.
- Brute force as ground truth: the PE 502 enumerator and its limits.

### N - Numbers

- Metallic means, the Pell strip, and the metallic ladder of realizable strips.
- Perron roots, reachable number fields, and the Pisot/Salem question for cubics.
- Continued fractions, convergents, and the eigenvalue-to-OEIS crosswalk.
- Bounded-height nacci sequences and periodicity modulo primes.
- Exact arithmetic at scale: PE 502 targets and modular reduction.
- Cryptography: ring, LFSR, linear complexity, and the round-two / round-three breaks.
- The Hardin word identity, A005251, and the missing sign-reversing involution.

### Z - Zoo

- Taxonomy: geometric versus non-geometric classification, and the sub-family lattice (convex, valley, tree, stack, Ferrers, parallelogram, prime).
- Rule variations: tower spacing, gap rules, no-touching, vertical spacing, higher dimensions.
- Specimens: the 10-cell and 11-cell isospectral pairs, the golden and silver castles, the bronze hole.
- Comparative morphology: convex core uniqueness, unimodal versus convex, statistical-physics cousins.
- Public interpretation: eigenvalues-by-example and the other pedagogy tours; the seminar layer draws its exhibits here.

Z absorbs both the Classification and Miscellaneous Divisions from `IDEAS.md`. The two pages `castle-classification-geometric` and `castle-classification-non-geometric` are its natural first split.

### Q - q-Analogues

- Area as a grading: castle-by-area, tree-castle-by-area, bounded-height rows by area.
- Prime castles and the Klarner `A = P/(1-P)` decomposition.
- The q-polyomino zoo: Bousquet-Melou add-a-column GFs read off at the area variable; A001169 and A001523 as landmarks.
- Classical q-families: Carlitz q-Catalan, Barcucci q-Motzkin and q-Bessel, weakly unimodal compositions, steep polyominoes.
- Bistatistics: area with block count, peaks, records; hunting q-binomial and Narayana-q coefficients.
- Area-preserving bijections: convex to valley, and `h=3` tree versus all.

### S - Spectra

- The five spectra: transfer matrix, LGV kernel, skyline DFT, combinatorial Laplacian, Ihara zeta.
- The castle graph: cycle rank equals the number of 2x2 blocks, bipartite, planar; tree castles by height.
- Spectral radius: `lambda_1 = h` for the count; metallic radii of individual castles; the bronze hunt.
- Isospectrality: Kac's drum, the exhaustive census to 16 cells, Sunada constructions.
- Universality: sine-kernel bulk, GUE, random Young tableaux via the LGV kernel.
- Expanders and zeta: Ramanujan castles, prime closed walks, arithmetic combinatorics.
- Signals: skyline DFT as a complete invariant, compressed sensing, turnpike reconstruction.

### T - Transcendentals

- The sampler substrate: ten techniques from rejection to coupling-from-the-past and Wang-Landau.
- CLT routes: a castle statistic, its normal limit, pi from the mode density.
- RMT routes: semicircle, Tracy-Widom, Airy edge, Marchenko-Pastur, Kesten-McKay.
- Geometric probability: Buffon needle across a skyline, Barbier, Ehrhart on the castle polytope.
- Classical identities on castle asymptotics: Stirling, Basel, Wallis.
- Random walks on castle graphs: return, cover, hitting times; loop-erased walk and conformal invariance.
- Beyond pi: Catalan's `G`, `zeta(3)`, `gamma`; and the algebraic-transcendental wall as the reason any of this is hard.

## Crossovers

| Pair | Hook | Subplot |
|---|---|---|
| E/N | extreme dimensions | counting at the scales where exact arithmetic becomes the obstacle |
| E/Z | sampling and addresses | drawing specimens from the zoo and naming where each one sits |
| E/R | beyond parity | counts refined past the even-block clause by other statistics |
| R/E | altered rules | representations under changed castle rules and what still counts |
| Q/E | the second variable | bivariate GFs and q-transfer matrices; area rides along with the count |
| Q/N | coefficients at q | the area-graded sequences (A001523, A115981, A332578) as OEIS targets in their own right |
| Q/Z | prime factorization of shapes | prime castles and sub-family refinements as taxonomy done by area |
| Q/R | bijections that keep the area | convex to valley, tree versus all, as translations with a conserved quantity |
| S/N | the ladder heard twice | metallic means as Perron roots of counts versus as spectral radii of single castles; why signed eigenvalues are never metallic |
| S/Z | same drum, different castle | isospectral pairs as the zoo's twin exhibits |
| S/R | the castle as a signal | skyline DFT and castle graph as encodings, and what each spectrum forgets |
| S/E | the count is an eigenvalue | the transfer-matrix spectrum is the enumeration, `lambda_1 = h` |
| T/S | pi in the spectrum | every RMT limit density carries pi; the LGV kernel as the bridge |
| T/E | counting turned into drawing | rank/unrank, Gray codes, and transfer matrices as samplers |
| T/N | the algebraic wall | castle constants are algebraic units, pi is not; where the two worlds touch |
| T/Z | needles dropped on the zoo | random-rule ensembles and geometric probability across variant families |

Not yet named: Q/S has no page behind it, and Q/T exists only through area CLTs, which already sit in T/E.
