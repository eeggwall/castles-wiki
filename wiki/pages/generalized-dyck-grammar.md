---
title: Generalized Dyck grammar for castles
category: Concepts
summary: The grammar E_k → empty | R E_k | U V D (empty | R E_k) of the words in U, R, D that write towers of height at most k, with V the nonempty towers of height at most k − 1 on a block. It is the first-return decomposition of Dyck words with a third letter R for columns, it generates each tower word exactly once, and its generating functions give the tower count T(k, L) = (k+1)^L and the signed tower count P(k, L).
tags: [concept, castle, dyck, grammar, generating-functions]
sources: [project-euler-502-representations, project-euler-502-castle-factoring, project-euler-502-observations]
created: 2026-09-13
updated: 2026-10-16
---

# Generalized Dyck grammar for castles

The castle rules can be written as a grammar over words in the steps `U`, `R` and `D` ([[urd-step-strings](pages/urd-step-strings.md)]), and the generating functions read off the grammar count castles ([[castle-counting-formula](pages/castle-counting-formula.md)]).[^1] The grammar is the first-return decomposition of Dyck words with a third letter.

## The tower word

The letters are `U` (up one row), `R` (one column to the right, at the current height) and `D` (down one row). A castle is written `U (towers) D`: the outer `U … D` is the bottom row, and the towers on it are written in between.[^2] Towers with column heights `c = (c_1, …, c_L)` above a base of length `L` are written column by column, with `c_0 = 0`: move from height `c_{i−1}` to height `c_i` with `U`s or `D`s, write one `R`, and after the last column write `D^{c_L}` to return to the base. So the word of towers on a base of length `L` has exactly `L` letters `R`, never drops below the base, and ends on it.[^3]

*Example.* The towers `(1, 0, 1)` on a base of length 3 are written `URDRURD`, with heights `0, 1, 1, 0, 0, 1, 1, 0` after each letter: up onto a block of width 1, across it, off it, across a gap column, then up, across and off a second block. The castle on them, the skyline `(2, 1, 2)`, is `UURDRURDD`. The towers `(2)` on a base of length 1, a block of width 1 carrying another, are written `UURDD`, and the castle on them, the skyline `(3)`, is `UUURDDD`.[^4]

Two facts about tower words are used throughout:[^3]

- the number of blocks is the number of `D`s, which equals the number of `U`s: each block is written as a matched `U … D`, and each `D` ends one block;
- a tower word contains no `UD`, which would be a block of width 0, and no `DU`, which would be two touching blocks in a row.

`URDRURD` has two `D`s and two blocks. The no-overhang rule needs no separate statement: a block is written between the `U` and the `D` of the block it rests on, so it lies within that block's columns.[^5]

## The grammar

Let `E_k` be the set of words of towers of height at most `k`. A tower word is empty, or starts with a gap column, or starts with a block:[^6]

```
E_k  →  empty
     |  R E_k
     |  U V D ( empty | R E_k )
```

The alternatives read:[^7]

- `empty` is the word of the towers on a base of length 0.
- `R E_k` is one column of height 0 above the base, then the rest.
- `U V D (empty | R E_k)` is a block in the first row above the base, which the source calls a peak: up onto the block, the word `V` of the towers on it, and down off it; then either the end, or a gap column followed by the rest.

`V` is a nonempty word in `E_{k−1}`, one row lower because the block uses one row. `V` nonempty keeps the width of the block positive, which excludes `UD`, and the tail `empty | R E_k` keeps two blocks of a row from touching, which excludes `DU`; this is the same-row gap rule.[^7] In the example, `URDRURD` parses as the block `U R D`, with `V = R`, followed by the tail `R E_k` with `E_k = URD`, a second block with `V = R` and an empty tail.

The grammar generates each tower word exactly once: the first letter decides the alternative, and the `D` that closes `U V D` is the first return to the base ([[tower-word-language](pages/tower-word-language.md)]). For `k ≤ 3` and `L ≤ 5`, the words it generates are the `(k+1)^L` words of the towers of height at most `k` on a base of length `L`, each with one parse.[^8]

**First return.** The Dyck words `D → empty | x D x̄ D` are split at the first return of the path to its starting level ([[dyck-words](pages/dyck-words.md)]). The castle grammar makes the same split, `U V D` followed by a tail, with one extra letter `R`; since `U` and `D` are vertical steps, the interior `V` is a whole tower word rather than a Dyck word.[^9] Unlike the Dyck tail, the castle tail is empty or starts with `R`.

**Counts.** Let `x` mark each `R`, so that towers on a base of length `L` have weight `x^L`. The grammar gives the generating function `E_k(x)` of the tower count `T(k, L)` and, with each block weighted by `−1`, the generating function `P_k(x)` of the signed tower count `P(k, L)` ([[castle-counting-formula](pages/castle-counting-formula.md)], Equations (2) and (3)). Solving them gives `T(k, L) = (k+1)^L` and the recurrence of `P_k(x)` in `k`.

## Independence of the towers on different blocks

In the production `U V D (empty | R E_k)`, the towers `V` on a block come from their own copy of `E_{k−1}`, independent of the rest of the word. So the towers on different blocks of a row are independent, and the gap between two blocks of a row separates the towers above them as well.[^10] This independence makes the count multiply over the blocks, which is the induction proof of `T(k, L) = (k+1)^L` ([[castle-counting-formula](pages/castle-counting-formula.md)], section *Tower count*).

A Dyck word in `U` and `D` alone records how the blocks nest and their left-to-right order, but not their widths or the gaps between them. The letter `R` records the columns: the towers of height 0 on a base of length `L` are written `R^L`, and the gaps between neighboring blocks are `R`s. The cycle-forest form, which matches each `U` with the `D` that closes it and drops the `R`s, keeps only the nesting of the blocks and does not determine the towers ([[castle-representations](pages/castle-representations.md)]).[^11] The towers `(1, 0, 1)`, written `URDRURD`, and `(1, 1, 0, 0, 1)`, written `URRDRRURD`, have the same cycle forest, two blocks side by side.

## Appearances in Sources

- [[project-euler-502-representations](pages/project-euler-502-representations.md)] - the tower word, the grammar, its two worked examples, and its description as the Dyck first-return split with one extra letter.
- [[project-euler-502-castle-factoring](pages/project-euler-502-castle-factoring.md)] - the grammar read as a factorization of a tower into blocks separated by `R` gaps, and the cycle-forest form.
- [[project-euler-502-observations](pages/project-euler-502-observations.md)] - the independence of the towers on two blocks of the same row.
- [[deutsch-elizalde-2016-bargraphs-cornerless-motzkin](pages/deutsch-elizalde-2016-bargraphs-cornerless-motzkin.md)] - the decomposition `HA | UA′D | UA′DHA` of cornerless Motzkin paths, with `A′` nonempty: this grammar without the height bound, with `H` for `R` and `A′` for `V`.

## Related Concepts

- [[urd-step-strings](pages/urd-step-strings.md)] - the step-string encoding of castles over which the grammar is defined.
- [[castle-counting-formula](pages/castle-counting-formula.md)] - the generating functions `E_k(x)` and `P_k(x)` read off the grammar, and the formula for `A^e(w, h)`.
- [[tower-word-language](pages/tower-word-language.md)] - the tower words as a language of Motzkin paths (`U`, `R`, `D` as steps `+1`, `0`, `−1`) without `UD` and `DU`, and the proof that the grammar is unambiguous.
- [[dyck-words](pages/dyck-words.md)] - Dyck words and their first-return grammar.
- [[lattice-paths](pages/lattice-paths.md)] - shortest lattice paths written as step strings, where the `U`/`R`/`D` encoding comes from.
- [[symbolic-method](pages/symbolic-method.md)] - the translation of a recursive specification such as `E_k = ε + R·E_k + U·V·D·(ε + R·E_k)` into an equation for its ordinary generating function, as in [[analytic-combinatorics-ch1-ogfs](pages/analytic-combinatorics-ch1-ogfs.md)].
- [[generating-functions](pages/generating-functions.md)] - generating functions as the method for counting castles.
- [[narayana-numbers](pages/narayana-numbers.md)] and [[tower-heap](pages/tower-heap.md)] - towers of unbounded height on a base of length `w` counted by blocks, with generating function a Narayana polynomial over `(1 − x)^w`.
- [[permutation-cycle-castle-analogy](pages/permutation-cycle-castle-analogy.md)] - the blocks of the first row above the base set beside the cycles of a permutation.

## Footnotes

[^1]: [[project-euler-502-representations](pages/project-euler-502-representations.md)] §"Generalized Dyck Grammar for Castles" L217 - "The castle rules re-cast as a grammar over these strings, and the grammar yields the recurrence and the generating function that count castles."
[^2]: [[project-euler-502-representations](pages/project-euler-502-representations.md)] §"The tower word" L221-225 - "A castle is U (tower) D. The bottom block is the outer U...D pair, and the tower is everything stacked on top of it", with "U is up one row, vertical", "R is right one column", "D is down one row, vertical".
[^3]: [[project-euler-502-representations](pages/project-euler-502-representations.md)] §"The tower word" L227-230 - "A tower above a length-L block uses exactly L R's, never drops below the base, and returns to it", "blocks in the tower = number of D's = number of U's, because each D move completes a block", "a valid tower word has no UD (that would be a zero-width block) and no DU (two touching blocks)".
[^4]: [[project-euler-502-representations](pages/project-euler-502-representations.md)] §"The grammar" L236-252 - "Take a length-3 base block, put a width-1 sub-block in column 1 and another in column 3, and leave column 2 empty ... U R D R U R D", "The full castle for this example is U U R D R U R D D", "height sequence 0,1,1,0,0,1,1,0", and "In UURDD, a width-1 sub-block carries a width-1 block on top ... as a full castle it is UUURDDD".
[^5]: [[project-euler-502-representations](pages/project-euler-502-representations.md)] §"The tower word" L232 - "No-overhang needs no separate rule. Each R is spent once, as a gap or as part of a sub-block, so a child block always sits inside its parent's span."
[^6]: [[project-euler-502-representations](pages/project-euler-502-representations.md)] §"The grammar" L259-268 - "V = a whole tower of height at most k-1", "Let E_k be the towers of height at most k. A tower is empty, or it starts with a gap, or it starts with a peak. One rule per case: E_k -> empty | R E_k | U V D ( empty | R E_k )".
[^7]: [[project-euler-502-representations](pages/project-euler-502-representations.md)] §"The grammar" L272-276 - "empty is the empty tower, nothing above the base", "R E_k is one empty column (one R), then the rest of the tower", "U V D ( empty | R E_k ) is a peak: up onto a sub-block, the tower V above it, down off it, then stop, or a gap column and the next peak", "V is one row lower because the sub-block itself uses one row, and V is nonempty. Nonempty V is what keeps the sub-block width positive (no UD). The empty | R E_k tail is what keeps two peaks from touching (no DU), the same-row gap rule."
[^8]: Verified by execution (Python 3.11, 2026-10-16): for `k ≤ 3` and `L ≤ 5`, the list of words generated by the grammar, with multiplicity, equals the list of words of all towers in `{0, …, k}^L`; the words of the examples and of the cycle-forest example.
[^9]: [[project-euler-502-representations](pages/project-euler-502-representations.md)] §"The grammar" L278 - "This is the Dyck first-return split U w_1 D w_2 with one extra letter. The only change is that U and D are vertical here, so the interior V is a whole tower rather than a single matched step."
[^10]: [[project-euler-502-observations](pages/project-euler-502-observations.md)] §"Sub-block independence" L5 - "Two sibling blocks in the same row generate towers that never interact (the parent-row gap is automatic)."
[^11]: [[project-euler-502-castle-factoring](pages/project-euler-502-castle-factoring.md)] §"Cycle-forest form" L208-212 - "Match each U with the D that closes it (stack matching). Each matched pair is a block", "The forest is only the vertical nesting skeleton: it discards the R steps, so it does not recover the tower word", "Above a length-L base the tower with no blocks is R^L, a simple horizontal run with no vertical steps."
