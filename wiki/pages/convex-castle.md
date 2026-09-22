---
title: Convex castle
category: Concepts
summary: A castle with a unimodal (up-then-down) skyline — equivalently column-convex AND row-convex; the umbrella for castle convexity, counted by CCC = C(2h+w−3, w−1).
tags: [concept, castle, convex, unimodal, column-convex, row-convex, combinatorics, stars-and-bars]
sources: [project-euler-502-representations, project-euler-502-solution, project-euler-502-brute-force, oeis-mining-pe502]
created: 2026-09-13
updated: 2026-09-20
---

# Convex castle

## Description

A **convex castle** is a class of [[castle-polyomino](pages/castle-polyomino.md)] sitting between the simplest (rectangular) castles and the fully general ones in the [[urd-step-strings](pages/urd-step-strings.md)] taxonomy. In its U/R/D word, a convex castle splits into three portions:[^1]

- **front** — interspersed `U` and `R` steps climbing to the castle's maximum height, with no `D` steps;
- **middle** — any `R` steps taken at the maximum height, with at least one `R`;
- **back** — interspersed `D` and `R` steps descending to the base, with no `U` steps.

A convex castle begins with a `U` and ends with a `D`.[^1] Intuitively, its silhouette rises monotonically to a plateau and then descends monotonically — it never dips back down and climbs again. All remaining castles are generated as *variations* on convex castles (by inserting `D`/`U` pairs into runs of `R`s), which is why the convex castles are the structural backbone of the enumeration.[^2] The convex castle behind a given castle is unique: its **convex core** is the pointwise minimum of the prefix and suffix running maxima of the skyline, and the castles over a core are counted by a product of tower counts, one per plateau ([[convex-core](pages/convex-core.md)]).

## Convexity: unimodal = column-convex ∧ row-convex

This page is the umbrella for castle convexity, and the three convexity notions coincide here. On the column-height side a castle is a skyline `c_1…c_w`, and the convex castle is exactly the **unimodal** skyline — the heights ascend then descend, `is_unimodal(c)` — which the brute-force module identifies as **column-convex AND row-convex**.[^7] The equivalence with the U/R/D "front / middle / back" description above is immediate: an up-then-down skyline is precisely a word of `U`/`R`s (rising), then `R`s at the top, then `D`/`R`s (falling).

- **Column-convex** (each column a contiguous vertical run) holds for *every* castle by construction (columns are stacks on the base) — see [[column-convex-polyomino](pages/column-convex-polyomino.md)]. So among castles, convexity is really the *row*-convexity condition.
- **Row-convex** ([[horizontally-convex-polyomino](pages/horizontally-convex-polyomino.md)]) is the binding constraint: each row a single contiguous segment, i.e. no same-row gaps, which for a castle forces the unimodal skyline.

So *convex castle = unimodal castle = column-convex ∧ row-convex castle*, and this is the class the U/R/D variation-enumeration tried and **failed** to count directly.[^8] The brute-force enumerator tallies these separately as `conv_even` / `conv_odd`.[^7]

## Counting convex castles

The number of convex castles on a grid of width *w* and height *h* is counted by a **stars-and-bars** argument. Starting from the bare-minimum string, one inserts the remaining `w−1` `R`s into `2(h−1)+1` partition slots: `h−1` slots between the `U`s, `h−1` between the `D`s, and one slot between the `U`-run and `D`-run (which already holds at least one `R`).[^3] This gives the count of convex castles:[^4]

```
CCC = C(2(h−1)+w−1, w−1) = C(2h+w−3, w−1)
```

where `C(m,k) = m!/(k!(m−k)!)` is the binomial coefficient. For example, at *h*=4, *w*=5: `CCC = C(2·4+5−3, 5−1) = C(10, 4) = 210` convex castles.[^5]

**Minimum-block characterization, and why the count is binomial.** The Online Encyclopedia of Integer Sequences (OEIS) mining pass sharpened this: for *any* castle `#blocks ≥ h`, with equality **iff** it is unimodal — so a convex castle has *exactly h* blocks, and convex castles are the *minimum-block* castles.[^9] The binomial (rather than Catalan) form has a clean reason — the ascending front and descending back are independent, and a generalized Vandermonde convolution closes the sum; the full derivation is [[convex-castle-binomial-identity](pages/convex-castle-binomial-identity.md)].[^10] Consequently the even-parity convex count is `C(2h+w−3, w−1)` when *h* is even and `0` when *h* is odd (every convex castle has *h* blocks).

**By area, convex castles are A001523.** Re-indexed by total cells, a convex castle of area *n* is exactly a [[weakly-unimodal-composition](pages/weakly-unimodal-composition.md)] of *n* — OEIS `A001523` ("stacks") — and the parity split `cev(n) + cod(n) = A001523(n)` — where CEV and COD are the counts of convex-even and convex-odd castles by area, i.e. convex castles split by block parity — is a new refinement (see [[castle-by-area](pages/castle-by-area.md)]).[^11] The mirror **valley** castles are equinumerous with convex ones in every (w,h) cell (same binomial, different sets) — a candidate bijection.[^11]

**Every castle over its convex core.** The Solution subpage records that enumerating all castles as `D`/`U`-pair insertions into convex castles "never resolved into a formula", and the winning solution instead counts via the [[binary-string-bijection](pages/binary-string-bijection.md)] and independence.[^6] The per-column form of the same idea does close: every castle has a unique minimal convex majorant `min(prefix max, suffix max)`, the castles sharing it lower the non-anchor columns of its plateaus, and the fiber is `prod m^(l-1)` over plateaus unsigned and `(-1)^h prod P(m-1, l-1)` signed, so `F(w,h)` is a sum over convex castles of products of signed tower counts ([[convex-core](pages/convex-core.md)]). That the convex castles themselves count so cleanly (`C(2h+w−3, w−1)`) while their variations resist a closed form, and that they sit exactly at the intersection of two convexity classes with rich literatures ([[column-convex-polygon-enumeration](pages/column-convex-polygon-enumeration.md)], [[counting-horizontally-convex-polyominoes](pages/counting-horizontally-convex-polyominoes.md)]), makes the `conv_*` sequences from the brute enumerator prime candidates for further OEIS mining and for a correspondence with the classical stack / parallelogram families.

## Appearances in Sources

- [[project-euler-502-representations](pages/project-euler-502-representations.md)] — defines the front/middle/back structure and derives `CCC = C(2h+w−3, w−1)` by stars and bars.
- [[project-euler-502-solution](pages/project-euler-502-solution.md)] — records that convex-castle *variation* enumeration never resolved into a formula (a failed solution route).
- [[project-euler-502-brute-force](pages/project-euler-502-brute-force.md)] — identifies the convex castle as the unimodal (column-convex ∧ row-convex) skyline and tallies `conv_even`/`conv_odd`.
- [[oeis-mining-pe502](pages/oeis-mining-pe502.md)] — the minimum-block characterization, the binomial (Vandermonde) count, and the area↔A001523 match.

## Related Concepts

- [[urd-step-strings](pages/urd-step-strings.md)] — the encoding whose taxonomy contains convex castles.
- [[convex-core](pages/convex-core.md)] - the unique minimal convex majorant of any castle, and the tower-count product for the castles above each convex core.
- [[castle-polyomino](pages/castle-polyomino.md)] — the general object convex castles specialize.
- [[castle-counting-formula](pages/castle-counting-formula.md)] — the full count of all castles, of which convex castles are the backbone.
- [[convex-castle-binomial-identity](pages/convex-castle-binomial-identity.md)] — why `C(2h+w−3, w−1)` is binomial, not Catalan.
- [[weakly-unimodal-composition](pages/weakly-unimodal-composition.md)] — convex castles by area = A001523.
- [[column-convex-polyomino](pages/column-convex-polyomino.md)] — the column-convexity every castle already has.
- [[horizontally-convex-polyomino](pages/horizontally-convex-polyomino.md)] — the row-convexity that (with column-convexity) defines the convex castle.
- [[column-convex-polygon-enumeration](pages/column-convex-polygon-enumeration.md)] — the column-convex-polygon literature this convexity connects to.
- [[castle-classification-shape](pages/castle-classification-shape.md)] — the framework that names this class the **unimodal type**, one of the 7 base castle types.
- [[aocp-binomial-coefficients](pages/aocp-binomial-coefficients.md)] — the home of Vandermonde's convolution (Knuth eq (21)), the identity that closes the count; [[aocp-multinomial-coefficients](pages/aocp-multinomial-coefficients.md)] — the multinomial as the general form of the stars-and-bars mechanism.
- [[stack-polyomino-gf](pages/stack-polyomino-gf.md)] — the AC-native OGF for the unimodal-skyline A001523 sub-family, built directly by the symbolic method.

## Footnotes

[^1]: [[project-euler-502-representations](pages/project-euler-502-representations.md)] §"Steps-Based Approach" L84-91 — "what we will call a convex castle ... split into three portions: the front, the middle, and the back" with the front ("interspersed U and R ... No D steps"), middle ("R steps taken at the maximum height. There must be at least one R"), back ("interspersed D and R ... No U steps"), and "must begin with a U and end with a D".
[^2]: [[project-euler-502-representations](pages/project-euler-502-representations.md)] §"Steps-Based Approach" L101 — "we can classify all remaining castles as variations on convex castles."
[^3]: [[project-euler-502-representations](pages/project-euler-502-representations.md)] §"Step 2 Enumerating Convex Castles" L169-183 [synthesis] — the source (in its own W/H notation) inserts the remaining w−1 `R`s into the bare-minimum string, with h−1 slots between the `U`s, h−1 between the `D`s, and one slot between the `U`-run and `D`-run, and identifies this with the stars-and-bars problem.
[^4]: [[project-euler-502-representations](pages/project-euler-502-representations.md)] §"Step 2 Enumerating Convex Castles" L194 [synthesis] — states the count `CCC = C(2(h−1)+w−1, w−1) = C(2h+w−3, w−1)` (in the source's W/H notation).
[^5]: [[project-euler-502-representations](pages/project-euler-502-representations.md)] §"Step 2 Enumerating Convex Castles" L206-208 [synthesis] — evaluates the count at h=4, w=5 as `C(2·4+5−3, 5−1) = C(10, 4) = 210` and concludes there are 210 convex castles (in the source's W/H notation).
[^6]: [[project-euler-502-solution](pages/project-euler-502-solution.md)] §"What was tried and did not work" L190 — "U/R/D convex-castle enumeration. Conceptually clean, but the case analysis to enumerate variations of a convex castle never resolved into a formula."
[^7]: [[project-euler-502-brute-force](pages/project-euler-502-brute-force.md)] §"brute" L54, §"brute" L60-66 — "conv_even, conv_odd - the same, restricted to unimodal skylines (column-convex AND row-convex)" and the is_unimodal test (walk up, then down, accept iff the walk covers the whole tuple).
[^8]: [[project-euler-502-brute-force](pages/project-euler-502-brute-force.md)] §"Why keep a brute enumerator" L92 — "Unimodal castles are the ones the U/R/D convex-castle attempt tried and failed to enumerate directly."
[^9]: [[oeis-mining-pe502](pages/oeis-mining-pe502.md)] `binomial-vandermonde-identity.md` §1 L25-33 — "#blocks >= max(c) = h, with equality iff the profile is unimodal ... a convex castle of height h has exactly h blocks, and convex castles are exactly the minimum-block castles"; re-verified for w,h ≤ 5 during ingest.
[^10]: [[oeis-mining-pe502](pages/oeis-mining-pe502.md)] `binomial-vandermonde-identity.md` §§2-4 L35-96 — the up/down decomposition, the generalized Vandermonde convolution giving `C(2h+w-3, w-1)`, and "The two halves are independent ... Catalan / Narayana counts arise when a non-crossing or ballot constraint couples the two halves."
[^11]: [[oeis-mining-pe502](pages/oeis-mining-pe502.md)] `vein9-area.md` §"The main finding"/"Parity splits" L21-52 and `vein9b-concave.md` §"Concave counts by (w, h)" L100-118 — "conv(n) = A001523(n) ... cev(n) + cod(n) = A001523(n)" and "valley(w, h) = convex(w, h) ... same cardinality in each (w, h) cell but different sets ... a candidate bijection."
