---
title: Convex castle
category: Concepts
summary: A castle whose U/R/D word splits into a climbing front, a flat middle at max height, and a descending back; counted by CCC = C(2H+W−3, W−1).
tags: [concept, castle, convex, combinatorics, stars-and-bars]
sources: [project-euler-502-representations, project-euler-502-solution]
created: 2026-09-13
updated: 2026-09-13
---

# Convex castle

## Description

A **convex castle** is a class of [[castle-polyomino](pages/castle-polyomino.md)] sitting between the simplest (rectangular) castles and the fully general ones in the [[urd-step-strings](pages/urd-step-strings.md)] taxonomy. In its U/R/D word, a convex castle splits into three portions:[^1]

- **front** — interspersed `U` and `R` steps climbing to the castle's maximum height, with no `D` steps;
- **middle** — any `R` steps taken at the maximum height, with at least one `R`;
- **back** — interspersed `D` and `R` steps descending to the base, with no `U` steps.

A convex castle begins with a `U` and ends with a `D`.[^1] Intuitively, its silhouette rises monotonically to a plateau and then descends monotonically — it never dips back down and climbs again. All remaining castles are generated as *variations* on convex castles (by inserting `D`/`U` pairs into runs of `R`s), which is why the convex castles are the structural backbone of the enumeration.[^2]

## Counting convex castles

The number of convex castles on a grid of width *W* and height *H* is counted by a **stars-and-bars** argument. Starting from the bare-minimum string, one inserts the remaining `W−1` `R`s into `2(H−1)+1` partition slots: `H−1` slots between the `U`s, `H−1` between the `D`s, and one slot between the `U`-run and `D`-run (which already holds at least one `R`).[^3] This gives the count of convex castles:[^4]

```
CCC = C(2(H−1)+W−1, W−1) = C(2H+W−3, W−1)
```

where `C(m,k) = m!/(k!(m−k)!)` is the binomial coefficient. For example, at *H*=4, *W*=5: `CCC = C(2·4+5−3, 5−1) = C(10, 4) = 210` convex castles.[^5]

Convex castles are flagged for deeper standalone treatment in later work; this page collects the definition and the closed-form count established in the representations subpage.

**A thread that did not close (yet).** Enumerating *all* castles as variations on convex castles is conceptually clean, but the Solution subpage records that this route "never resolved into a formula" — the case analysis for the variations did not close, and the winning solution instead counts via the [[binary-string-bijection](pages/binary-string-bijection.md)] and independence.[^6] That the convex castles themselves count so cleanly (`C(2H+W−3, W−1)`) while their variations resist a closed form is a thread worth following into the column-convex-polygon literature (see [[column-convex-polygon-enumeration](pages/column-convex-polygon-enumeration.md)]).

## Appearances in Sources

- [[project-euler-502-representations](pages/project-euler-502-representations.md)] — defines the front/middle/back structure and derives `CCC = C(2H+W−3, W−1)` by stars and bars.
- [[project-euler-502-solution](pages/project-euler-502-solution.md)] — records that convex-castle *variation* enumeration never resolved into a formula (a failed solution route).

## Related Concepts

- [[urd-step-strings](pages/urd-step-strings.md)] — the encoding whose taxonomy contains convex castles.
- [[castle-polyomino](pages/castle-polyomino.md)] — the general object convex castles specialize.
- [[castle-counting-formula](pages/castle-counting-formula.md)] — the full count of all castles, of which convex castles are the backbone.
- [[column-convex-polygon-enumeration](pages/column-convex-polygon-enumeration.md)] — the column-convex-polygon literature this convexity connects to.

## Footnotes

[^1]: [[project-euler-502-representations](pages/project-euler-502-representations.md)] §"Steps-Based Approach" L84-91 — "what we will call a convex castle ... split into three portions: the front, the middle, and the back" with the front ("interspersed U and R ... No D steps"), middle ("R steps taken at the maximum height. There must be at least one R"), back ("interspersed D and R ... No U steps"), and "must begin with a U and end with a D".
[^2]: [[project-euler-502-representations](pages/project-euler-502-representations.md)] §"Steps-Based Approach" L101 — "we can classify all remaining castles as variations on convex castles."
[^3]: [[project-euler-502-representations](pages/project-euler-502-representations.md)] §"Step 2 Enumerating Convex Castles" L169-183 — "inserting W-1 different Rs into the bare minimum string ... H-1 possible slots between each U ... another H-1 ... between each D ... one slot between the string of Us and string of Ds ... equivalent to the 'stars and bars' problem."
[^4]: [[project-euler-502-representations](pages/project-euler-502-representations.md)] §"Step 2 Enumerating Convex Castles" L194 — "CCC = C(2(H-1)+W-1, W-1) = C(2H+W-3, W-1)".
[^5]: [[project-euler-502-representations](pages/project-euler-502-representations.md)] §"Step 2 Enumerating Convex Castles" L206-208 — "CCC = C(2H + W - 3, W-1) = C(2*4 + 5 - 3, 5-1) = C(10, 4) = 210 ... there are 210 convex castles."
[^6]: [[project-euler-502-solution](pages/project-euler-502-solution.md)] §"What was tried and did not work" L190 — "U/R/D convex-castle enumeration. Conceptually clean, but the case analysis to enumerate variations of a convex castle never resolved into a formula."
