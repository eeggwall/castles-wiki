---
title: U/R/D step strings
category: Concepts
summary: The step string of a castle, a word in U (up one row), R (one column) and D (down one row) with one R per column at the column's height. It starts with U, ends with D, contains neither UD nor DU, and has one D per block, so the even-block condition is an even number of D's. The source sorts castles into rectangular castles U^h R^w D^h, convex castles (every U before every D, C(2h + w − 3, w − 1) of them, each with h blocks) and variations of convex castles, and enumerates them in three steps; the source's Solution records that this enumeration never gave a formula.
tags: [concept, castle, representations, urd, dyck, lattice-paths]
sources: [project-euler-502-representations, project-euler-502-solution]
created: 2026-09-13
updated: 2026-10-16
---

# U/R/D step strings

## Definition

The **step string** of a [[castle-polyomino](pages/castle-polyomino.md)] with skyline `c = (c_1, …, c_w)` is a word in the letters `U` (up one row), `R` (one column) and `D` (down one row). Start at height 0. For each column `i`, move from height `c_{i−1}` to height `c_i` with `U`s or `D`s, with `c_0 = 0`, and write one `R` at height `c_i`. After the last column, write `D^{c_w}` to return to height 0. The source takes the device from the lattice paths of Project Euler 15 ([[lattice-paths](pages/lattice-paths.md)]), and calls it the representation "that led to the most breakthroughs".[^1]

*Example.* The skyline `(2, 1, 2)` has the step string `UURDRURDD`: up to 2, one column, down to 1, one column, up to 2, one column, down to 0.

The step string of a castle of width `w` has these properties, which follow from the construction:

- it has exactly `w` letters `R`, starts with `U` since `c_1 ≥ 1`, and ends with `D`;
- it contains neither `UD` nor `DU`, since every vertical move is followed by an `R`;
- its `D`s number the total descent `Σ_{i=0}^{w} max(0, c_i − c_{i+1})`, with `c_{w+1} = 0`, which is the block count; each `D` ends one block.[^2]

The skyline is read back off the heights at which the `R`s are written, so a castle and its step string determine each other. Since each `D` ends one block, a castle has an even number of blocks exactly when its step string has an even number of `D`s.[^3] Removing the outer `U … D`, the bottom row, leaves the word of the castle's towers ([[generalized-dyck-grammar](pages/generalized-dyck-grammar.md)], [[tower-word-language](pages/tower-word-language.md)]).

## Rectangular, convex, and variations

The source sorts castles by their step strings into three kinds.[^4]

- **Rectangular castles** are `U^h R^w D^h`, the skyline `(h, …, h)`. The rectangular castle of width 8 and height 4 is `UUUURRRRRRRRDDDD`.
- **Convex castles** ([[convex-castle](pages/convex-castle.md)]) are the castles whose step string has every `U` before every `D`: a front of `U`s and `R`s that climbs to height `h`, a middle of at least one `R` at height `h`, and a back of `D`s and `R`s that descends to 0.[^5] These are exactly the castles with a unimodal skyline. A convex castle of height `h` has `h` letters `D`, so it has exactly `h` blocks.
- **Variations of convex castles** are all other castles. The source builds them from convex castles by inserting pairs `D … U` between two `R`s of a run of `R`s, with at least one `R` between the two letters, and requires the `D` to come first, since a `U` first "will construct a duplicate castle variation that would be covered by another convex castle".[^6] [[convex-core](pages/convex-core.md)] states this precisely: every castle lies under a unique smallest convex castle, its convex core, and is obtained from it by lowering columns.

The convex castles of width `w` and height `h` number `C(2h + w − 3, w − 1)`: in the string `U^h R D^h`, the other `w − 1` letters `R` go into `2h − 1` slots, the `h − 1` slots between consecutive `U`s, the `h − 1` slots between consecutive `D`s, and the slot beside the middle `R` ([[convex-castle](pages/convex-castle.md)]).[^7]

## The source's enumeration procedure

The source assembles the castles of width `W` and height `H` in three steps:[^8]

1. Start from a bare-minimum string, the fewest `U`s and `D`s, separated by at least one `R`. At `H = 4` it is `U U U U R D D D D`, the skyline `(4)`.
2. Insert the remaining `R`s to reach width `W`; the source notes that this step counts the convex castles.
3. Insert pairs `U … D` or `D … U`, separated by at least one `R`, to produce the variations.

At odd `H` the string `U^H R D^H` has `H` blocks, an odd number, so the source inserts one more `U … D` pair and two more `R`s; at `H = 5` its bare-minimum string is `U U U U U R D R U R D D D D D`, the castle `(5, 4, 5)` with 6 blocks.[^9] Every convex castle of height `H` has exactly `H` blocks, so at odd `H` no convex castle has an even number of blocks.[^7]

The Solution subpage lists this enumeration among the approaches that did not work: "the case analysis to enumerate variations of a convex castle never resolved into a formula".[^10] The count of all castles comes instead from the grammar of the tower words ([[generalized-dyck-grammar](pages/generalized-dyck-grammar.md)]), which gives the [[castle-counting-formula](pages/castle-counting-formula.md)].

## Appearances in Sources

- [[project-euler-502-representations](pages/project-euler-502-representations.md)] - the step encoding, the rectangular, convex and varied castles, the bare-minimum strings and the three-step enumeration.
- [[project-euler-502-solution](pages/project-euler-502-solution.md)] - the step-string enumeration of convex castles and their variations, listed among the approaches that did not give a formula.

## Related Concepts

- [[castle-representations](pages/castle-representations.md)] - the three encodings of a castle: column-wise binary strings, skylines and step strings.
- [[convex-castle](pages/convex-castle.md)] - the castles with a unimodal skyline, their count `C(2h + w − 3, w − 1)`, and the proof that a castle has at least `h` blocks, with equality exactly for convex castles.
- [[convex-core](pages/convex-core.md)] - the smallest convex castle above a castle, and the castles that share it.
- [[generalized-dyck-grammar](pages/generalized-dyck-grammar.md)] - the grammar of the tower words, which counts all castles.
- [[tower-word-language](pages/tower-word-language.md)] - the tower words as cornerless Motzkin paths, and the proof that the grammar is unambiguous.
- [[lattice-paths](pages/lattice-paths.md)] - the step strings of Project Euler 15, from which the source takes the encoding.
- [[aocp-multinomial-coefficients](pages/aocp-multinomial-coefficients.md)] - the words with given numbers of `U`, `R` and `D`, counted by multinomial coefficients, and the trinomial coefficients `A027907` of the words of length `n` by final height.
- [[aocp-multisets](pages/aocp-multisets.md)] - Knuth's two-line arrays for permutations of a multiset, the form of a step string as a permutation of its letters.
- [[block-count-constraints](pages/block-count-constraints.md)] - castles and towers selected by block count, of which the even-block condition is the residue class 0 modulo 2.

## Footnotes

[^1]: [[project-euler-502-representations](pages/project-euler-502-representations.md)] §"Steps-Based Approach" L78 - "The representation that led to the most breakthroughs in progressing with PE 502 was the same representation used to solve the Lattice Paths problem in Project Euler/15. In that problem, we represented a path through a lattice using a string of letters like RRRDDD. We can do the same thing here to represent castles."
[^2]: [[project-euler-502-representations](pages/project-euler-502-representations.md)] §"The tower word" L227-230 - "A tower above a length-L block uses exactly L R's, never drops below the base, and returns to it", "blocks in the tower = number of D's = number of U's, because each D move completes a block", "a valid tower word has no UD (that would be a zero-width block) and no DU (two touching blocks)".
[^3]: [[project-euler-502-representations](pages/project-euler-502-representations.md)] §"Steps-Based Approach" L137 - "each D move completes a new block, so checking if there are an even number of blocks is as easy as checking if the number of Ds is even."
[^4]: [[project-euler-502-representations](pages/project-euler-502-representations.md)] §"Steps-Based Approach" [synthesis] L80-84, L86-107, L109 - rectangular castles "consist of Us, then Rs, then Ds"; convex castles; "we can classify all remaining castles as variations on convex castles".
[^5]: [[project-euler-502-representations](pages/project-euler-502-representations.md)] §"Steps-Based Approach" L88-91 - "The front of the castle consists of interspersed U and R steps, until the castle reaches its maximum height. No D steps are present in the front part. The middle of the castle consists of any R steps taken at the maximum height. There must be at least one R step in the middle. The back of the castle consists of interspersed D and R steps, until the castle reaches its base. No U steps are present in the back part. The convex castle must begin with a U and end with a D".
[^6]: [[project-euler-502-representations](pages/project-euler-502-representations.md)] §"Steps-Based Approach" L109-117 - "we look for runs of RRRs of length 3 or more. Each pair of Rs creates a slot for additional U or D moves", "we MUST insert Ds first; if we insert Us first, we will construct a duplicate castle variation that would be covered by another convex castle. We must also insert Ds and Us in pairs, so as to keep the total height change 0. Last, we cannot insert Ds and Us next to one another."
[^7]: Verified by execution (Python 3.11, 2026-10-16): for every castle with `h ≤ 4`, `w ≤ 5`, the step string has `w` letters `R`, starts with `U`, ends with `D`, has no `UD` or `DU`, and has as many `D`s as blocks; for `h ≤ 5`, `w ≤ 6`, the castles with every `U` before every `D` are exactly the unimodal ones, number `C(2h + w − 3, w − 1)`, and have `h` blocks each; `(5, 4, 5)` has the step string `UUUUURDRURDDDDD` and 6 blocks; the source's variation strings contain no `UD` or `DU`.
[^8]: [[project-euler-502-representations](pages/project-euler-502-representations.md)] §"Procedure" L145-149, §"Step 1 Bare Minimum String" L153-157 - "Start with a bare minimum string of U/R/D", "Insert the number of remaining Rs into the castle string needed to make the castle have width W. (This is the number of CONVEX CASTLES.)", "Insert pairs of U/D or D/U, separated by at least one R", and "for castles of height 4 and width 5, the bare minimum string would be 4 Us, 4 Ds, and one R to separate them".
[^9]: [[project-euler-502-representations](pages/project-euler-502-representations.md)] §"Step 1 Bare Minimum String" L159-165 - "the case where the height is odd requires a different bare minimum string, because the number of rows is odd, meaning the bare minimum string will not satisfy the requirement that castles must have an even number of blocks (an even number of Ds). To get around that, we insert an extra U and an extra D, and two extra Rs to separate them", with "U U U U U R D R U R D D D D D" for height 5.
[^10]: [[project-euler-502-solution](pages/project-euler-502-solution.md)] §"What was tried and did not work" L190 - "U/R/D convex-castle enumeration. Conceptually clean, but the case analysis to enumerate variations of a convex castle never resolved into a formula."
