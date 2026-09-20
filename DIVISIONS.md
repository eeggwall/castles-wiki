# Divisions

Nine Divisions partition the castle wiki's research surface. Each Division has a one-line descriptor in four parts, a conceptual coverage list, and a set of crossovers with the other Divisions. R gathers the representation pages. F has no pages yet. X gathers the keystream, steganography, and commitment pages that the other Divisions only glanced at.

Crossovers are written `home/lens`: `E/R` and `R/E` are different subplots. Crossover names are hooks (a titled subplot), not descriptions of theme.

## Descriptors

- **R - Representations:** encodings, equivalences, grammars, and what survives translation.
- **E - Enumeration:** counting methods, generating functions, recurrences, and sampling.
- **N - Numbers:** sequences, exact arithmetic, difficult scales, and numerical patterns.
- **Z - Zoo:** specimens, taxonomy, comparative morphology, and public interpretation.
- **Q - q-Analogues:** area gradings, q-generating functions, joint statistics, and the bijections that preserve area.
- **S - Spectra:** castle graphs, transfer and kernel eigenvalues, isospectral pairs, and what a castle sounds like.
- **T - Transcendentals:** samplers, limit laws, geometric probability, and pi pulled out of castle ensembles.
- **F - Fractional:** non-integer orders, power-law memory, interpolated statistics, and dense operators where the integer castle has sparse ones.
- **X - Ciphers:** keystreams, hidden payloads, commitments, and what survives an adversary.

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
- The Hardin word identity, A005251, and the missing sign-reversing involution.

### Z - Zoo

- Taxonomy: geometric versus non-geometric classification, and the sub-family lattice (convex, valley, tree, stack, Ferrers, parallelogram, prime).
- Rule variations: tower spacing, gap rules, no-touching, vertical spacing, higher dimensions.
- Specimens: the 10-cell and 11-cell isospectral pairs, the golden and silver castles, the bronze hole.
- Comparative morphology: convex core uniqueness, unimodal versus convex, statistical-physics cousins.
- Public interpretation: eigenvalues-by-example and the other pedagogy tours; the seminar layer draws its exhibits here.

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

### F - Fractional

- The three definitions on three castle objects: Grunwald-Letnikov on skylines (binomially weighted column differences), Riemann-Liouville on generating functions (`(1 - x)^{-alpha}`), Caputo on recurrences (initial terms preserved).
- Interpolated statistics: the fractional block count `B_alpha` with area and block count as its endpoints; `Z(q, alpha)` joining the area GF to the Narayana block polynomial.
- Interpolated arguments: fractional width via `M^{w-1}`, fractional height via the quasi-polynomial in `k`; the parity clause as a branch cut; the half-column embedding problem.
- Fractional sums and transforms: Cesaro half-sums and the `sqrt(pi)` in `Gamma(1/2)`; Mittag-Leffler GFs between OGF and EGF; fractional recurrences and the constants no strip realizes.
- Anomalous diffusion on the castle graph: the comb model and time-fractional order `1/2`; Levy flights and the space-fractional Laplacian; fractional heat traces.
- Long memory: Hurst exponents and ARFIMA order of real skylines; power-law memory strip rules and their dense truncated transfer matrices.
- Fractional powers in finite rings: roots of `x^w` in `F_p[x] / (char)` and the half-step oracle.

### X - Ciphers

- Castle keystreams: LFSR, ring arithmetic over `F_p[x]`, linear complexity, and the round-two / round-three breaks.
- Steganography on skylines: LSB payloads, block-parity carriers, and per-castle capacity.
- The castle as a channel: real image rows read as carriers, and degradation under crop, scale, and reencoding.
- Commitments: whether the parity clause makes a castle a natural commitment scheme, and which invariants an opening reveals.
- Adversarial models: what a distinguisher sees when castles are drawn from two rules with the same spectrum, and when isospectrality becomes a security parameter.
- Hardness candidates: castle problems (isospectrality census, height reconstruction, turnpike) as sources of one-way functions.

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
| F/Q | one statistic, two orders | area at `alpha = 0`, block count at `alpha = 1`, and the partition function that joins them |
| F/E | half a column | fractional width, the branch cut the parity clause forces, and which rules are two steps of a finer rule |
| F/T | the `sqrt(pi)` door | half-sums carry `Gamma(1/2)` in an exact coefficient; a second way through the algebraic wall |
| F/N | the rungs between rungs | growth constants of fractional recurrences as the complement of the reachable-field census |
| F/S | the castle is a comb | subdiffusion at order `1/2` on tree castles, Levy flights on the polyomino graph, fractional heat traces |
| F/R | the Hurst exponent of a skyline | ARFIMA order as the compressibility knob and a rule-detector statistic |
| F/Z | long-memory specimens | real skylines (image rows, audio, tones) placed by their fractional integration order |
| F/X | fractional Kitamasa | fractional powers `x^{w/n}` in `F_p[x] / (Q)` as root extraction, and the half-step oracle for the DH red-team |
| X/N | keystream on the ladder | LFSR ring arithmetic over `F_p`, linear complexity, and the round-two / round-three breaks |
| X/R | the castle as a channel | steganography, LSB payloads, and block-parity carriers as R's entropy bullet meeting an adversary |
| X/S | the spectrum as a leak | isospectral pairs as an adversary's ambiguity; skyline DFT as a fingerprint the eavesdropper reads |
| X/E | rank as a key | Algorithm M and unrank as an addressing function keyed by a secret |
| X/Z | key castles | the sub-zoo of carriers, keystream generators, and commitment shapes |
| X/T | hardness at the wall | one-way functions as concrete sightings of the algebraic-transcendental wall |

Not yet named: Q/S has no page behind it, and Q/T exists only through area CLTs, which already sit in T/E. X/Q and X/F are open too.

