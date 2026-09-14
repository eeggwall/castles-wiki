---
title: U/R/D step strings
category: Concepts
summary: The up/right/down step-string encoding of a castle — the representation that led to the solution; organizes castles as rectangular, convex, and variations.
tags: [concept, castle, representations, urd, dyck, lattice-paths]
sources: [project-euler-502-representations]
created: 2026-09-13
updated: 2026-09-13
---

# U/R/D step strings

## Description

A **U/R/D step string** encodes a [[castle-polyomino](pages/castle-polyomino.md)] as a walk in three step types — `U` (up one row), `R` (right one column), `D` (down one row) — tracing the castle's outline. It is the same device used to encode paths for the [[lattice-paths](pages/lattice-paths.md)] problem (Project Euler 15), reused here for castles.[^1] Among the three [[castle-representations](pages/castle-representations.md)], this is the one that produced the breakthroughs toward the Project Euler 502 solution.[^1]

Its defining convenience: **each `D` move completes a block**, so the even-block rule is equivalent to "the number of Ds is even."[^2]

## Castle taxonomy in U/R/D

The encoding organizes castles into three tiers of increasing generality.[^3]

- **Rectangular castles** — all `U`s, then all `R`s, then all `D`s. A 4×8 rectangular castle is `UUUURRRRRRRRDDD`.[^3]
- **[[convex-castle](pages/convex-castle.md)]** — split into *front* (interspersed `U`/`R`, no `D`, climbing to max height), *middle* (≥1 `R` steps at max height), and *back* (interspersed `D`/`R`, no `U`, descending to base); begins with `U`, ends with `D`.[^4]
- **Variations on convex castles** — all remaining castles. Found by locating runs of three or more `R`s and inserting `D`/`U` pairs into the slots between `R` pairs, subject to three rules: insert `D` before `U` (inserting `U` first would duplicate a castle already covered by another convex castle), insert in pairs (net height change zero), and never place a `D` and `U` adjacent.[^5]

## Enumeration procedure

To assemble a castle of width *W* and height *H*, a three-step process:[^6]

1. Start from a **bare-minimum string** — the fewest `U`s and `D`s required, separated by at least one `R`. For *H*=4, *W*=5: `U U U U R D D D D`. When *H* is **odd**, the plain bare-minimum string would have an odd block count (odd number of `D`s), violating the even-block rule; the fix is to insert an extra `U` and `D` (with two extra `R`s to separate them) — e.g. for *H*=5, *W*=10: `U U U U U R D R U R D D D D D`.[^7]
2. Insert the remaining `R`s to reach width *W* — this produces the [[convex-castle](pages/convex-castle.md)] count.
3. Insert `U`/`D` (or `D`/`U`) pairs, separated by at least one `R`, to produce the variations.[^6]

This taxonomy and procedure are the enumeration reading of castles; the *counting* reading — replacing enumeration with a closed form — comes from recasting the same U/R/D strings as a [[generalized-dyck-grammar](pages/generalized-dyck-grammar.md)], which yields the [[castle-counting-formula](pages/castle-counting-formula.md)].

## Appearances in Sources

- [[project-euler-502-representations](pages/project-euler-502-representations.md)] — introduces the U/R/D encoding, the rectangular/convex/variations taxonomy, and the three-step enumeration procedure.

## Related Concepts

- [[castle-representations](pages/castle-representations.md)] — the encoding collection this belongs to.
- [[convex-castle](pages/convex-castle.md)] — the central class in the taxonomy.
- [[generalized-dyck-grammar](pages/generalized-dyck-grammar.md)] — the grammar these strings support, giving the count.
- [[lattice-paths](pages/lattice-paths.md)] — the source of the U/R/D device.

## Footnotes

[^1]: [[project-euler-502-representations](pages/project-euler-502-representations.md)] §"Steps-Based Approach" L76 — "The representation that led to the most breakthroughs in progressing with PE 502 was the same representation used to solve the Lattice Paths problem in Project Euler/15 ... a string of letters like RRRDDD. We can do the same thing here to represent castles."
[^2]: [[project-euler-502-representations](pages/project-euler-502-representations.md)] §"Steps-Based Approach" L137 — "each D move completes a new block, so checking if there are an even number of blocks is as easy as checking if the number of Ds is even."
[^3]: [[project-euler-502-representations](pages/project-euler-502-representations.md)] §"Steps-Based Approach" L80-82 — "Let's start with the simplest castles: rectangular castles. These castles consist of Us, then Rs, then Ds ... The 4 x 8 rectangular castle would be: UUUURRRRRRRRDDD".
[^4]: [[project-euler-502-representations](pages/project-euler-502-representations.md)] §"Steps-Based Approach" L86-91 — the front ("interspersed U and R steps, until the castle reaches its maximum height. No D steps"), middle ("any R steps taken at the maximum height. There must be at least one R step"), back ("interspersed D and R steps ... No U steps"), and "must begin with a U and end with a D".
[^5]: [[project-euler-502-representations](pages/project-euler-502-representations.md)] §"Steps-Based Approach" L103-107 — "we look for runs of RRRs of length 3 or more ... we MUST insert Ds first; if we insert Us first, we will construct a duplicate castle ... We must also insert Ds and Us in pairs, so as to keep the total height change 0. Last, we cannot insert Ds and Us next to one another."
[^6]: [[project-euler-502-representations](pages/project-euler-502-representations.md)] §"Procedure" L145-149 — "Start with a bare minimum string of U/R/D ... Insert the number of remaining Rs ... (This is the number of CONVEX CASTLES.) ... Insert pairs of U/D or D/U, separated by at least one R."
[^7]: [[project-euler-502-representations](pages/project-euler-502-representations.md)] §"Step 1 Bare Minimum String" L153-165 — the H=4,W=5 minimum "U U U U R D D D D", the odd-height problem ("the number of rows is odd ... will not satisfy the requirement that castles must have an even number of blocks"), and the H=5,W=10 fix "U U U U U R D R U R D D D D D".
