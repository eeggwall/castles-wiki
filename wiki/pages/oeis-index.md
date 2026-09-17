---
title: OEIS index - the wiki's cross-reference directory
category: Concepts
summary: A single-page directory of every OEIS A-number the wiki references and where it appears, 72 sequences across 41 citing pages. Grouped by role - castle count interpretations, continued-fraction / metallic-ladder neighborhood, plastic-number sequences, and supporting sequences. The wiki's method for turning castle counts into OEIS entries lives on [[oeis-cross-referencing]]; the source workspace lives on [[oeis-mining-pe502]]; this page is the lookup table.
tags: [concept, oeis, index, directory, cross-reference, castle, sequence]
sources: [oeis-mining-pe502]
created: 2026-09-17
updated: 2026-09-17
---

# OEIS index

## What this is

A directory of every OEIS A-number cited on the wiki: 72 sequences, appearing across 41 citing pages. This page is a *lookup table*, not a narrative. The method for identifying an OEIS match and the discipline for verifying it live on [[oeis-cross-referencing](pages/oeis-cross-referencing.md)]; the source workspace where the first mining pass was carried out is [[oeis-mining-pe502](pages/oeis-mining-pe502.md)]; the height-2 hyperbolic interlink (the highest-value candidate for submission) lives on [[oeis-height2-hyperbolic-castles](pages/oeis-height2-hyperbolic-castles.md)]. Use this page to find where an A-number is discussed, or to spot which sequences have accumulated multiple wiki appearances (a signal that the sequence has become central and its cross-reference is worth submitting).

## Counts by role

- **Castle count interpretations** (34) - sequences the wiki claims as counts of a castle-native object. These are the *interlinking targets*: candidates for submitting new OEIS comments or formulas that read the sequence as a castle count.
- **Continued fractions / metallic ladder** (22) - the [[metallic-means](pages/metallic-means.md)] `δ_a` family, its companion / trace sequences, and the OEIS convergent tables for `√(a²+4)`.
- **Plastic-number neighborhood** (3) - the sequences behind [[plastic-number](pages/plastic-number.md)] ψ.
- **Supporting sequences** (9) - cross-references, ambient polyomino counts, and OEIS entries that appear as neighbors or components of a castle result.

## Directory

A-numbers link to OEIS. "Pages" is where the number appears in this wiki, with the occurrence count in parentheses; the primary discussion is generally the page with the highest count.

### Castle count interpretations

| A-number | Name | Castle role | Pages |
|---|---|---|---|
| [A000045](https://oeis.org/A000045) | Fibonacci numbers: F(n) = F(n-1) + F(n-2) with F(0) = 0 and F(1) = 1. | tree castles of height 2 (T_2(w) = F_{w+2}); Fibonacci in prime-castle count | [[castle-graph](pages/castle-graph.md)] (3), [[convergents-oeis-crosswalk](pages/convergents-oeis-crosswalk.md)] (3), [[metallic-means](pages/metallic-means.md)] (2), [[eigenvalue-continued-fractions](pages/eigenvalue-continued-fractions.md)] (1), [[pell-numbers](pages/pell-numbers.md)] (1), [[plastic-number](pages/plastic-number.md)] (1) |
| [A000129](https://oeis.org/A000129) | Pell numbers: a(0) = 0, a(1) = 1; for n > 1, a(n) = 2*a(n-1) + a(n-2). | Pell castle strip; realization of 1 + √2 | [[pell-numbers](pages/pell-numbers.md)] (9), [[pe502-pell-castle-strip](pages/pe502-pell-castle-strip.md)] (5), [[convergents-oeis-crosswalk](pages/convergents-oeis-crosswalk.md)] (3), [[pell-castle-strip](pages/pell-castle-strip.md)] (3), [[eigenvalue-continued-fractions](pages/eigenvalue-continued-fractions.md)] (2), [[metallic-means](pages/metallic-means.md)] (2), [[castle-classification](pages/castle-classification.md)] (1), [[castle-counting-formula](pages/castle-counting-formula.md)] (1), [[castle-snippets](pages/castle-snippets.md)] (1), [[tower-word-continued-fraction](pages/tower-word-continued-fraction.md)] (1) |
| [PLACEHOLDER-A000225](https://oeis.org/PLACEHOLDER-A000225) | a(n) = 2^n - 1. (Sometimes called Mersenne numbers, although that name is usually reserved | total height-2 castles (Mersenne): F(w,2) + odd(w,2) = 2^w - 1 | [[oeis-height2-hyperbolic-castles](pages/oeis-height2-hyperbolic-castles.md)] (8), [[oeis-mining-pe502](pages/oeis-mining-pe502.md)] (3), [[castle-counting-function](pages/castle-counting-function.md)] (2), [[aocp-generating-functions](pages/aocp-generating-functions.md)] (1), [[hyperbolic-sequence-family](pages/hyperbolic-sequence-family.md)] (1) |
| [A000447](https://oeis.org/A000447) | a(n) = 1^2 + 3^2 + 5^2 + 7^2 + ... + (2*n-1)^2 = n*(4*n^2 - 1)/3. | |P(2m+1,4)| bisection: 4·A000447 = A199833 | [[convergents-oeis-crosswalk](pages/convergents-oeis-crosswalk.md)] (4) |
| [A001045](https://oeis.org/A001045) | Jacobsthal sequence (or Jacobsthal numbers): a(n) = a(n-1) + 2*a(n-2), with a(0) = 0, a(1) | tree castles of height 3: T_3(w) = J_{w+2} (Jacobsthal) | [[castle-graph](pages/castle-graph.md)] (3), [[castle-snippets](pages/castle-snippets.md)] (1) |
| [A001047](https://oeis.org/A001047) | a(n) = 3^n - 2^n. | h^w - (h-1)^w at h=3: total h=3 castles | [[new-sequence-fw3](pages/new-sequence-fw3.md)] (4), [[aocp-generating-functions](pages/aocp-generating-functions.md)] (2), [[oeis-mining-pe502](pages/oeis-mining-pe502.md)] (2), [[castle-counting-function](pages/castle-counting-function.md)] (1) |
| [A001263](https://oeis.org/A001263) | Triangle of Narayana numbers T(n,k) = C(n-1,k-1)*C(n,k-1)/k with 1 <= k <= n, read by rows | tower Narayana polynomial coefficients | [[tower-narayana-polynomial](pages/tower-narayana-polynomial.md)] (7), [[narayana-numbers](pages/narayana-numbers.md)] (6) |
| [A001523](https://oeis.org/A001523) | Number of stacks, or planar partitions of n; also number of weakly unimodal compositions o | convex castles by area (weakly unimodal compositions) | [[weakly-unimodal-composition](pages/weakly-unimodal-composition.md)] (15), [[castle-by-area](pages/castle-by-area.md)] (11), [[convex-castle](pages/convex-castle.md)] (7), [[oeis-mining-pe502](pages/oeis-mining-pe502.md)] (5), [[stack-polyomino-gf](pages/stack-polyomino-gf.md)] (5), [[analytic-combinatorics-part-a](pages/analytic-combinatorics-part-a.md)] (3), [[castle-counting-function](pages/castle-counting-function.md)] (3), [[castle-classification](pages/castle-classification.md)] (1), [[convex-castle-binomial-identity](pages/convex-castle-binomial-identity.md)] (1), [[oeis-cross-referencing](pages/oeis-cross-referencing.md)] (1), [[q-catalan-numbers](pages/q-catalan-numbers.md)] (1) |
| [A004149](https://oeis.org/A004149) | Generalized Catalan numbers: a(n+1) = a(n) + Sum_{k=2..n-1} a(k)*a(n-1-k). | tower word growth (algebraic GF, growth 1+√2) | [[tower-word-continued-fraction](pages/tower-word-continued-fraction.md)] (10), [[castle-classification](pages/castle-classification.md)] (3), [[metallic-means](pages/metallic-means.md)] (1) |
| [A005060](https://oeis.org/A005060) | a(n) = 5^n - 4^n. | h^w - (h-1)^w at h=5 | [[oeis-mining-pe502](pages/oeis-mining-pe502.md)] (2) |
| [A005061](https://oeis.org/A005061) | a(n) = 4^n - 3^n. | h^w - (h-1)^w at h=4 | [[oeis-mining-pe502](pages/oeis-mining-pe502.md)] (2) |
| [A005062](https://oeis.org/A005062) | a(n) = 6^n - 5^n. | h^w - (h-1)^w at h=6 | [[oeis-mining-pe502](pages/oeis-mining-pe502.md)] (2) |
| [A005251](https://oeis.org/A005251) | a(0) = 0, a(1) = a(2) = a(3) = 1; thereafter, a(n) = a(n-1) + a(n-2) + a(n-4). | Hardin words at m=1 (no-isolated-1 binary), P_even(6,L)/2^L | [[convergents-oeis-crosswalk](pages/convergents-oeis-crosswalk.md)] (6), [[hardin-word-identity](pages/hardin-word-identity.md)] (5), [[tower-parity-sectors](pages/tower-parity-sectors.md)] (5), [[castle-snippets](pages/castle-snippets.md)] (3), [[plastic-number](pages/plastic-number.md)] (3), [[signed-tower-count](pages/signed-tower-count.md)] (2) |
| [A005408](https://oeis.org/A005408) | The odd numbers: a(n) = 2*n + 1. | tower Narayana coefficient row | [[tower-narayana-polynomial](pages/tower-narayana-polynomial.md)] (7), [[narayana-numbers](pages/narayana-numbers.md)] (2), [[tower-heap](pages/tower-heap.md)] (2), [[oeis-mining-pe502](pages/oeis-mining-pe502.md)] (1) |
| [A005435](https://oeis.org/A005435) | Number of column-convex polyominoes with perimeter 2n+2. | column-convex polyominoes by perimeter (neighbor family) | [[castle-by-area](pages/castle-by-area.md)] (2) |
| [A005891](https://oeis.org/A005891) | Centered pentagonal numbers: (5n^2+5n+2)/2; crystal ball sequence for 3.3.3.4.4. planar ne | tower Narayana coefficient row | [[tower-narayana-polynomial](pages/tower-narayana-polynomial.md)] (6), [[narayana-numbers](pages/narayana-numbers.md)] (2), [[tower-heap](pages/tower-heap.md)] (2), [[oeis-mining-pe502](pages/oeis-mining-pe502.md)] (1) |
| [A006130](https://oeis.org/A006130) | a(n) = a(n-1) + 3*a(n-2) for n > 1, a(0) = a(1) = 1. | tree castles of height 4: T_4(w) = a(w+1) | [[castle-graph](pages/castle-graph.md)] (4), [[castle-classification](pages/castle-classification.md)] (1), [[castle-snippets](pages/castle-snippets.md)] (1) |
| [A006131](https://oeis.org/A006131) | a(n) = a(n-1) + 4*a(n-2), a(0) = a(1) = 1. | tree castles of height 5: T_5(w) = a(w+1) | [[castle-graph](pages/castle-graph.md)] (5), [[castle-classification](pages/castle-classification.md)] (1), [[castle-snippets](pages/castle-snippets.md)] (1) |
| [A009545](https://oeis.org/A009545) | Expansion of e.g.f. sin(x)*exp(x). | -P_odd(1,L): height-1 signed tower count with odd last column | [[signed-tower-count](pages/signed-tower-count.md)] (7), [[tower-parity-sectors](pages/tower-parity-sectors.md)] (5), [[oeis-mining-pe502](pages/oeis-mining-pe502.md)] (4), [[oeis-cross-referencing](pages/oeis-cross-referencing.md)] (1) |
| [A011782](https://oeis.org/A011782) | Coefficients of expansion of (1-x)/(1-2*x) in powers of x. | weakly unimodal compositions (unrestricted) | [[castle-by-area](pages/castle-by-area.md)] (3), [[oeis-mining-pe502](pages/oeis-mining-pe502.md)] (1), [[weakly-unimodal-composition](pages/weakly-unimodal-composition.md)] (1) |
| [A038503](https://oeis.org/A038503) | Sum of every 4th entry of row n in Pascal's triangle, starting at "n choose 0". | odd(w,2) + 1: odd-block height-2 castles | [[oeis-height2-hyperbolic-castles](pages/oeis-height2-hyperbolic-castles.md)] (16), [[hyperbolic-sequence-family](pages/hyperbolic-sequence-family.md)] (10), [[oeis-mining-pe502](pages/oeis-mining-pe502.md)] (4), [[castle-counting-function](pages/castle-counting-function.md)] (3), [[signed-tower-count](pages/signed-tower-count.md)] (3), [[oeis-cross-referencing](pages/oeis-cross-referencing.md)] (2), [[new-sequence-fw3](pages/new-sequence-fw3.md)] (1) |
| [A038505](https://oeis.org/A038505) | Sum of every 4th entry of row n in Pascal's triangle, starting at binomial(n,2). | F(w,2): even-block height-2 castles | [[oeis-height2-hyperbolic-castles](pages/oeis-height2-hyperbolic-castles.md)] (15), [[hyperbolic-sequence-family](pages/hyperbolic-sequence-family.md)] (10), [[oeis-mining-pe502](pages/oeis-mining-pe502.md)] (4), [[castle-counting-function](pages/castle-counting-function.md)] (3), [[signed-tower-count](pages/signed-tower-count.md)] (3), [[new-sequence-fw3](pages/new-sequence-fw3.md)] (2), [[oeis-cross-referencing](pages/oeis-cross-referencing.md)] (2), [[castle-graph-spectral-radius](pages/castle-graph-spectral-radius.md)] (1), [[castle-snippets](pages/castle-snippets.md)] (1) |
| [A063490](https://oeis.org/A063490) | a(n) = (2*n - 1)*(7*n^2 - 7*n + 6)/6. | tower Narayana coefficient row | [[tower-narayana-polynomial](pages/tower-narayana-polynomial.md)] (6), [[narayana-numbers](pages/narayana-numbers.md)] (2), [[tower-heap](pages/tower-heap.md)] (2), [[oeis-mining-pe502](pages/oeis-mining-pe502.md)] (1) |
| [A063496](https://oeis.org/A063496) | a(n) = (2*n - 1)*(8*n^2 - 8*n + 3)/3. | P(2m,4) bisection: C_3 lattice crystal-ball sequence | [[convergents-oeis-crosswalk](pages/convergents-oeis-crosswalk.md)] (2) |
| [A112742](https://oeis.org/A112742) | a(n) = n^2*(n^2 - 1)/3. | A_5(k): alternating part of P(k,5) quasi-polynomial | [[convergents-oeis-crosswalk](pages/convergents-oeis-crosswalk.md)] (2) |
| [A115981](https://oeis.org/A115981) | The number of compositions of n which cannot be viewed as stacks. | non-convex castles by area | [[castle-by-area](pages/castle-by-area.md)] (6), [[oeis-mining-pe502](pages/oeis-mining-pe502.md)] (2), [[weakly-unimodal-composition](pages/weakly-unimodal-composition.md)] (2) |
| [A146559](https://oeis.org/A146559) | Expansion of (1-x)/(1 - 2*x + 2*x^2). | P(1,L): signed tower count at k=1, Re((1+i)^{L+1}) | [[signed-tower-count](pages/signed-tower-count.md)] (12), [[hyperbolic-sequence-family](pages/hyperbolic-sequence-family.md)] (4), [[oeis-height2-hyperbolic-castles](pages/oeis-height2-hyperbolic-castles.md)] (4), [[tower-parity-sectors](pages/tower-parity-sectors.md)] (4), [[oeis-mining-pe502](pages/oeis-mining-pe502.md)] (3), [[new-sequence-fw3](pages/new-sequence-fw3.md)] (2), [[castle-counting-formula](pages/castle-counting-formula.md)] (1), [[castle-sign](pages/castle-sign.md)] (1), [[castle-snippets](pages/castle-snippets.md)] (1), [[finite-fields](pages/finite-fields.md)] (1), [[kitamasa](pages/kitamasa.md)] (1), [[oeis-cross-referencing](pages/oeis-cross-referencing.md)] (1) |
| [A160747](https://oeis.org/A160747) | Expansion of (1 + 10*x + 20*x^2 + 10*x^3 + x^4)/(1-x)^5. | tower Narayana coefficient row | [[tower-narayana-polynomial](pages/tower-narayana-polynomial.md)] (6), [[narayana-numbers](pages/narayana-numbers.md)] (2), [[tower-heap](pages/tower-heap.md)] (2), [[oeis-mining-pe502](pages/oeis-mining-pe502.md)] (1) |
| [A199833](https://oeis.org/A199833) | Number of -n..n arrays of 4 elements with zero sum and no two neighbors summing to zero. | |P(2m+1,4)|: signed height-1 towers on length-4 base, odd k | [[convergents-oeis-crosswalk](pages/convergents-oeis-crosswalk.md)] (2) |
| [A202882](https://oeis.org/A202882) | Number of n X 1 0..2 arrays with every nonzero element less than or equal to some horizont | Hardin words at m=2: P_even(10,L)/2^L | [[tower-parity-sectors](pages/tower-parity-sectors.md)] (5), [[hardin-word-identity](pages/hardin-word-identity.md)] (4), [[castle-snippets](pages/castle-snippets.md)] (1) |
| [A203094](https://oeis.org/A203094) | Number of nX1 0..3 arrays with every nonzero element less than or equal to some horizontal | Hardin words at m=3: P_even(14,L)/2^L | [[tower-parity-sectors](pages/tower-parity-sectors.md)] (5), [[hardin-word-identity](pages/hardin-word-identity.md)] (4) |
| [A203184](https://oeis.org/A203184) | Number of n X 1 0..4 arrays with every nonzero element less than or equal to some horizont | Hardin words at m=4: P_even(18,L)/2^L | [[tower-parity-sectors](pages/tower-parity-sectors.md)] (5), [[hardin-word-identity](pages/hardin-word-identity.md)] (4) |
| [A332578](https://oeis.org/A332578) | Number of compositions of n whose negation is unimodal. | valley castles by area | [[castle-by-area](pages/castle-by-area.md)] (6), [[oeis-mining-pe502](pages/oeis-mining-pe502.md)] (2), [[weakly-unimodal-composition](pages/weakly-unimodal-composition.md)] (2), [[castle-classification](pages/castle-classification.md)] (1) |
| [A332669](https://oeis.org/A332669) | Number of compositions of n whose negation is not unimodal. | not-unimodal compositions | [[castle-by-area](pages/castle-by-area.md)] (2) |
| [A352116](https://oeis.org/A352116) | Partial sums of the odd triangular numbers (A014493). | |P(k,4)|: partial sums of odd triangular numbers | [[convergents-oeis-crosswalk](pages/convergents-oeis-crosswalk.md)] (5), [[castle-snippets](pages/castle-snippets.md)] (2), [[closed-form-hunting](pages/closed-form-hunting.md)] (1) |

### Continued fractions and the metallic ladder

| A-number | Name | Castle role | Pages |
|---|---|---|---|
| [A000032](https://oeis.org/A000032) | Lucas numbers beginning at 2: L(n) = L(n-1) + L(n-2), L(0) = 2, L(1) = 1. | Lucas numbers (companion of Fibonacci) | [[convergents-oeis-crosswalk](pages/convergents-oeis-crosswalk.md)] (2), [[metallic-means](pages/metallic-means.md)] (2), [[plastic-number](pages/plastic-number.md)] (1) |
| [A001076](https://oeis.org/A001076) | Denominators of continued fraction convergents to sqrt(5). | denominators of CF convergents to √5; copper Fibonacci-3 sequence | [[convergents-oeis-crosswalk](pages/convergents-oeis-crosswalk.md)] (4), [[metallic-means](pages/metallic-means.md)] (2) |
| [A001077](https://oeis.org/A001077) | Numerators of continued fraction convergents to sqrt(5). | numerators of CF convergents to √5 | [[convergents-oeis-crosswalk](pages/convergents-oeis-crosswalk.md)] (2) |
| [A001333](https://oeis.org/A001333) | Pell-Lucas numbers: numerators of continued fraction convergents to sqrt(2). | numerators of CF convergents to √2 (Pell-Lucas) | [[convergents-oeis-crosswalk](pages/convergents-oeis-crosswalk.md)] (7), [[pell-numbers](pages/pell-numbers.md)] (5), [[metallic-means](pages/metallic-means.md)] (4), [[pe502-pell-castle-strip](pages/pe502-pell-castle-strip.md)] (2), [[castle-snippets](pages/castle-snippets.md)] (1) |
| [A002203](https://oeis.org/A002203) | Companion Pell numbers: a(n) = 2*a(n-1) + a(n-2), a(0) = a(1) = 2. | companion Pell (trace of Pell) | [[convergents-oeis-crosswalk](pages/convergents-oeis-crosswalk.md)] (4), [[metallic-means](pages/metallic-means.md)] (2) |
| [A006190](https://oeis.org/A006190) | a(n) = 3*a(n-1) + a(n-2), with a(0)=0, a(1)=1. | bronze metallic sequence: a(n) = 3a(n-1) + a(n-2) | [[convergents-oeis-crosswalk](pages/convergents-oeis-crosswalk.md)] (2), [[metallic-means](pages/metallic-means.md)] (2) |
| [A006497](https://oeis.org/A006497) | a(n) = 3*a(n-1) + a(n-2) with a(0) = 2, a(1) = 3. | trace sequence for bronze | [[convergents-oeis-crosswalk](pages/convergents-oeis-crosswalk.md)] (2), [[metallic-means](pages/metallic-means.md)] (1) |
| [A014448](https://oeis.org/A014448) | Even Lucas numbers: a(n) = L(3*n). | even Lucas: trace for copper (a=4) | [[convergents-oeis-crosswalk](pages/convergents-oeis-crosswalk.md)] (2), [[metallic-means](pages/metallic-means.md)] (1) |
| [A014493](https://oeis.org/A014493) | Odd triangular numbers. | odd triangular numbers (row of A352116) | [[convergents-oeis-crosswalk](pages/convergents-oeis-crosswalk.md)] (3), [[castle-snippets](pages/castle-snippets.md)] (1) |
| [A033887](https://oeis.org/A033887) | a(n) = Fibonacci(3*n + 1). | F(3n+1): copper-delta convergent numerators | [[convergents-oeis-crosswalk](pages/convergents-oeis-crosswalk.md)] (2) |
| [A041010](https://oeis.org/A041010) | Numerators of continued fraction convergents to sqrt(8). | numerators of CF convergents to √8 | [[convergents-oeis-crosswalk](pages/convergents-oeis-crosswalk.md)] (2) |
| [A041011](https://oeis.org/A041011) | Denominators of continued fraction convergents to sqrt(8). | denominators of CF convergents to √8 | [[convergents-oeis-crosswalk](pages/convergents-oeis-crosswalk.md)] (2) |
| [A041018](https://oeis.org/A041018) | Numerators of continued fraction convergents to sqrt(13). | numerators of CF convergents to √13 | [[convergents-oeis-crosswalk](pages/convergents-oeis-crosswalk.md)] (2) |
| [A041019](https://oeis.org/A041019) | Denominators of continued fraction convergents to sqrt(13). | denominators of CF convergents to √13 | [[convergents-oeis-crosswalk](pages/convergents-oeis-crosswalk.md)] (2) |
| [A041030](https://oeis.org/A041030) | Numerators of continued fraction convergents to sqrt(20). | numerators of CF convergents to √20 | [[convergents-oeis-crosswalk](pages/convergents-oeis-crosswalk.md)] (2) |
| [A041031](https://oeis.org/A041031) | Denominators of continued fraction convergents to sqrt(20). | denominators of CF convergents to √20 | [[convergents-oeis-crosswalk](pages/convergents-oeis-crosswalk.md)] (2) |
| [A041046](https://oeis.org/A041046) | Numerators of continued fraction convergents to sqrt(29). | numerators of CF convergents to √29 | [[convergents-oeis-crosswalk](pages/convergents-oeis-crosswalk.md)] (2) |
| [A041047](https://oeis.org/A041047) | Denominators of continued fraction convergents to sqrt(29). | denominators of CF convergents to √29 | [[convergents-oeis-crosswalk](pages/convergents-oeis-crosswalk.md)] (2) |
| [A052918](https://oeis.org/A052918) | a(0) = 1, a(1) = 5, a(n+1) = 5*a(n) + a(n-1). | nickel metallic sequence: a(n) = 5a(n-1) + a(n-2) | [[convergents-oeis-crosswalk](pages/convergents-oeis-crosswalk.md)] (4), [[metallic-means](pages/metallic-means.md)] (4) |
| [A052924](https://oeis.org/A052924) | Expansion of g.f.: (1-x)/(1 - 3*x - x^2). | bronze delta-1 CF numerators: (1-x)/(1-3x-x²) | [[convergents-oeis-crosswalk](pages/convergents-oeis-crosswalk.md)] (2) |
| [A087130](https://oeis.org/A087130) | a(n) = 5*a(n-1)+a(n-2) for n>1, a(0)=2, a(1)=5. | trace for nickel (a=5) | [[convergents-oeis-crosswalk](pages/convergents-oeis-crosswalk.md)] (2), [[metallic-means](pages/metallic-means.md)] (1) |
| [A100237](https://oeis.org/A100237) | Secondary diagonal of triangle A100235 divided by row number: a(n) = A100235(n+1,n)/(n+1)  | nickel delta-1 CF numerators: (1-x)/(1-5x-x²) | [[convergents-oeis-crosswalk](pages/convergents-oeis-crosswalk.md)] (3) |

### Plastic-number neighborhood

| A-number | Name | Castle role | Pages |
|---|---|---|---|
| [A000931](https://oeis.org/A000931) | Padovan sequence (or Padovan numbers): a(n) = a(n-2) + a(n-3) with a(0) = 1, a(1) = a(2) = | Padovan (plastic Fibonacci): a(n) = a(n-2) + a(n-3) | [[plastic-number](pages/plastic-number.md)] (4), [[convergents-oeis-crosswalk](pages/convergents-oeis-crosswalk.md)] (2) |
| [A001608](https://oeis.org/A001608) | Perrin sequence (or Perrin numbers, or Ondrej Such sequence): a(n) = a(n-2) + a(n-3) with  | Perrin (plastic Lucas / trace) | [[plastic-number](pages/plastic-number.md)] (3), [[convergents-oeis-crosswalk](pages/convergents-oeis-crosswalk.md)] (2) |
| [A060006](https://oeis.org/A060006) | Decimal expansion of real root of x^3 - x - 1 (the plastic constant). | decimal expansion of plastic constant ψ | [[convergents-oeis-crosswalk](pages/convergents-oeis-crosswalk.md)] (2), [[plastic-number](pages/plastic-number.md)] (2) |

### Supporting sequences

| A-number | Name | Castle role | Pages |
|---|---|---|---|
| [A000079](https://oeis.org/A000079) | Powers of 2: a(n) = 2^n. | powers of 2 (P_even(2,L) = 2^L) | [[castle-by-area](pages/castle-by-area.md)] (2) |
| [A000749](https://oeis.org/A000749) | a(n) = 4*a(n-1) - 6*a(n-2) + 4*a(n-3), n > 3, with a(0)=a(1)=a(2)=0, a(3)=1. | sum of every 4th binomial (hyperbolic family, k=3 residue) | [[hyperbolic-sequence-family](pages/hyperbolic-sequence-family.md)] (3), [[oeis-height2-hyperbolic-castles](pages/oeis-height2-hyperbolic-castles.md)] (1) |
| [A001168](https://oeis.org/A001168) | Number of fixed polyominoes with n cells. | fixed polyominoes | [[castle-by-area](pages/castle-by-area.md)] (2) |
| [A001169](https://oeis.org/A001169) | Number of board-pile polyominoes with n cells. | board-pile polyominoes (horizontally convex) | [[horizontally-convex-polyomino](pages/horizontally-convex-polyomino.md)] (4), [[counting-horizontally-convex-polyominoes](pages/counting-horizontally-convex-polyominoes.md)] (3) |
| [A010892](https://oeis.org/A010892) | Inverse of 6th cyclotomic polynomial. A period 6 sequence. | period-6 cyclotomic (P_odd(4,L)/2^L) | [[tower-parity-sectors](pages/tower-parity-sectors.md)] (4) |
| [A034839](https://oeis.org/A034839) | Triangular array formed by taking every other term of each row of Pascal's triangle. | Pascal every-other row (binomial identity) | [[convex-castle-binomial-identity](pages/convex-castle-binomial-identity.md)] (2) |
| [A038504](https://oeis.org/A038504) | Sum of every 4th entry of row n in Pascal's triangle, starting at "n choose 1". | sum of every 4th binomial (hyperbolic family, k=1 residue) | [[hyperbolic-sequence-family](pages/hyperbolic-sequence-family.md)] (3) |
| [A107920](https://oeis.org/A107920) | Lucas and Lehmer numbers with parameters (1 +- sqrt(-7))/2. | Lucas-Lehmer with (1±√-7)/2 (P_odd(2,L) at k=2) | [[tower-parity-sectors](pages/tower-parity-sectors.md)] (3) |
| [A202889](https://oeis.org/A202889) | T(n,k)=Number of nXk 0..2 arrays with every nonzero element less than or equal to some hor | 2D Hardin table (row axis of A202882) | [[tower-parity-sectors](pages/tower-parity-sectors.md)] (1) |

## Submission status (2026-09-17)

From [[oeis-cross-referencing](pages/oeis-cross-referencing.md)]: OEIS requires human authorship, so the wiki accumulates *verified matches* and drafts submission text elsewhere (`raw/oeis-pe502/`). No submissions have been filed yet from the wiki. Candidates in rough priority order:

1. **A038505 and A038503**: the height-2 hyperbolic interlink (`F(w,2) = A038505(w+1)`, `odd(w,2) = A038503(w+1) − 1`) is the highest-value candidate; both sequences are relatively isolated in the OEIS and gain a genuine geometric interpretation. See [[oeis-height2-hyperbolic-castles](pages/oeis-height2-hyperbolic-castles.md)].
2. **A146559**: `a(n) = P(1, n − 1)` and the derived `A146559 = A038503 − A038505` identity ([[signed-tower-count](pages/signed-tower-count.md)]).
3. **A005251, A202882, A203094, A203184**: the Hardin word identity gives each a second interpretation as `2^{−L}` times an even-last-column signed tower count, and proves their empirical recurrences ([[hardin-word-identity](pages/hardin-word-identity.md)]).
4. **A001045**: tree castles of height 3 is a new castle interpretation of Jacobsthal ([[castle-graph](pages/castle-graph.md)]).
5. **A006130, A006131**: tree castles of height 4 and 5 land in the k-Fibonacci family ([[castle-graph](pages/castle-graph.md)]).
6. **A001263, A005408, A005891, A063490, A160747**: the tower / Narayana rows ([[tower-narayana-polynomial](pages/tower-narayana-polynomial.md)]).
7. **A001523, A115981, A332578**: convex / non-convex / valley castles by area ([[castle-by-area](pages/castle-by-area.md)]).
8. **A352116**: `|P(k,4)|` = partial sums of odd triangular numbers ([[convergents-oeis-crosswalk](pages/convergents-oeis-crosswalk.md)]).

## Generation candidates (no OEIS match yet)

Sequences the wiki has computed and could submit as new OEIS entries. Human authorship required.

- `F(w, 3)`, `F(w, 4)`, `F(w, 5)`, `F(w, 6)`: the height-`h` castle counts for `h ≥ 3` ([[new-sequence-fw3](pages/new-sequence-fw3.md)], [[oeis-mining-pe502](pages/oeis-mining-pe502.md)]).
- `P(k, L)` rows for `k ≥ 2`: order-`(k+1)` C-finite family generalizing A146559 ([[signed-tower-count](pages/signed-tower-count.md)]).
- `P(k, L)` in `k` at fixed `L ≥ 5`: quasi-polynomial sequences `|P(k, 5)|, |P(k, 6)|, …` unmatched in OEIS ([[convergents-oeis-crosswalk](pages/convergents-oeis-crosswalk.md)]).
- Parity-refined area sequences (even-area / odd-area convex castles, `strict_valley`) ([[castle-by-area](pages/castle-by-area.md)]).
- Higher tower rows `w ≥ 6` in the Narayana table ([[tower-narayana-polynomial](pages/tower-narayana-polynomial.md)]).
- Jacobi-Perron convergent denominator sequences of `2ψ²` ([[convergents-oeis-crosswalk](pages/convergents-oeis-crosswalk.md)]).

## Appearances in Sources

- [[oeis-mining-pe502](pages/oeis-mining-pe502.md)] - the source workspace where the mining passes were carried out; every entry in the *Castle count interpretations* group above traces back to a vein there.

## Related Concepts

- [[oeis-cross-referencing](pages/oeis-cross-referencing.md)] - the method: verify against OEIS data with offsets, distinguish interlinking from generation, honor the human-authorship rule.
- [[oeis-height2-hyperbolic-castles](pages/oeis-height2-hyperbolic-castles.md)] - the highest-value submission candidate.
- [[hyperbolic-sequence-family](pages/hyperbolic-sequence-family.md)] - the A038503 / A038504 / A038505 / A000749 family collectively.
- [[metallic-means](pages/metallic-means.md)] / [[pell-numbers](pages/pell-numbers.md)] / [[plastic-number](pages/plastic-number.md)] - the number-family threads whose OEIS sequences populate this index.
- [[castle-graph](pages/castle-graph.md)] - the tree-castle counts on Fibonacci / Jacobsthal / k-Fibonacci.
- [[convergents-oeis-crosswalk](pages/convergents-oeis-crosswalk.md)] - the metallic-mean convergent tables.
- [[hardin-word-identity](pages/hardin-word-identity.md)] - the Hardin sequences A202882 / A203094 / A203184 and their proved recurrences.
- [[new-sequence-fw3](pages/new-sequence-fw3.md)] - the leading generation candidate.
