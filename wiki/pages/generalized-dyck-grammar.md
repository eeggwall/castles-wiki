---
title: Tower grammar
category: Concepts
summary: The grammar E_k → empty | R E_k | U V D (empty | R E_k) of the words in U, R, D that write towers of height at most k, with V the nonempty towers of height at most k − 1 on a block, which the Project Euler 502 notes call the generalized Dyck grammar. It is the first-return grammar of Motzkin paths, M → empty | R M | U M D M, with one cut for each factor a tower word excludes: an empty interior makes UD, and a tail starting with U makes DU. It generates each tower word exactly once, without the height bound it is Deutsch and Elizalde's decomposition of cornerless Motzkin paths, and its generating function by width and blocks is a Möbius map in the height, one 2 × 2 matrix whose specializations y = 1 and y = −1 give the tower count T(k, L) = (k+1)^L and the signed tower count P(k, L).
tags: [concept, castle, motzkin, cornerless, dyck, grammar, first-return, generating-functions]
sources: [project-euler-502-representations, project-euler-502-castle-factoring, project-euler-502-observations, dyck-words, deutsch-elizalde-2016-bargraphs-cornerless-motzkin, prodinger-2025-cornerless-motzkin-bargraphs]
created: 2026-09-13
updated: 2026-10-25
---

# Tower grammar

The castle rules can be written as a grammar over words in the steps `U`, `R` and `D` ([[urd-step-strings](pages/urd-step-strings.md)]), and the generating functions read off the grammar count castles ([[castle-counting-formula](pages/castle-counting-formula.md)]).[^1] Read as steps `+1`, `0` and `−1`, the words are the Motzkin paths with no `UD` and no `DU`, and the grammar is the first-return grammar of Motzkin paths with one cut for each excluded factor (section *From the Motzkin grammar*). [[project-euler-502-representations](pages/project-euler-502-representations.md)] calls it the generalized Dyck grammar.[^1]

## The tower word

The letters are `U` (up one row), `R` (one column to the right, at the current height) and `D` (down one row). A castle is written `U (towers) D`: the outer `U … D` is the bottom row, and the towers on it are written in between.[^2] Towers with column heights `c = (c_1, …, c_L)` above a base of length `L` are written column by column, with `c_0 = 0`: move from height `c_{i−1}` to height `c_i` with `U`s or `D`s, write one `R`, and after the last column write `D^{c_L}` to return to the base. So the word of towers on a base of length `L` has exactly `L` letters `R`, never drops below the base, and ends on it.[^3]

*Example.* The towers `(1, 0, 1)` on a base of length 3 are written `URDRURD`, with heights `0, 1, 1, 0, 0, 1, 1, 0` after each letter: up onto a block of width 1, across it, off it, across a gap column, then up, across and off a second block. The castle on them, the skyline `(2, 1, 2)`, is `UURDRURDD`. The towers `(2)` on a base of length 1, a block of width 1 carrying another, are written `UURDD`, and the castle on them, the skyline `(3)`, is `UUURDDD`.[^4]

Two facts about tower words are used throughout:[^3]

- the number of blocks is the number of `D`s, which equals the number of `U`s: each block is written as a matched `U … D`, and each `D` ends one block;
- a tower word contains no `UD`, which would be a block of width 0, and no `DU`, which would be two touching blocks in a row.

`URDRURD` has two `D`s and two blocks. The no-overhang rule needs no separate statement: a block is written between the `U` and the `D` of the block it rests on, so it lies within that block's columns.[^5]

Conversely, the heights at which the `R`s stand determine the word, since between two consecutive `R`s a change of direction would make `UD` or `DU` ([[tower-word-language](pages/tower-word-language.md)], *Lemma*). So the tower words of height at most `k` on a base of length `L` correspond to the tuples in `{0, …, k}^L` and number `(k+1)^L`; [[castle-counting-formula](pages/castle-counting-formula.md)], section *Tower count*, gives this proof and two others.

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

The grammar generates each tower word exactly once: the first letter decides the alternative, and the `D` that closes `U V D` is the first return to the base, and the section *From the Motzkin grammar* proves it. For `k ≤ 3` and `L ≤ 5`, the words it generates are the `(k+1)^L` words of the towers of height at most `k` on a base of length `L`, each with one parse.[^8]

## From the Motzkin grammar

[[project-euler-502-representations](pages/project-euler-502-representations.md)] describes the grammar as "the Dyck first-return split" with one extra letter.[^9] The Dyck grammar `D → empty | x D x̄ D` splits a word at its first return to the starting level ([[dyck-words](pages/dyck-words.md)]), and the extra letter `R` is the flat step of a Motzkin path. With `R` as a case of its own, the first-return grammar of Motzkin paths is

```
M  →  empty  |  R M  |  U M D M
```

A nonempty Motzkin path starts with `R` and a Motzkin path, or with `U`, a Motzkin path, the `D` of the first return to the starting level, and a Motzkin path; this is the recurrence `M_n = M_{n−1} + Σ_k M_k M_{n−2−k}` of the [[motzkin-numbers](pages/motzkin-numbers.md)].[^10] The first letter and the first return fix the parse, so each Motzkin path has one.

The tower words are the Motzkin paths with no `UD` and no `DU`, and each excluded factor comes from one place in this grammar:

- Every `U` opens a production `U M D M`, and the letter after it is `D` exactly when the interior `M` is empty. So the factors `UD` are the empty interiors.
- The letter after the `D` of `U M D M` is the first letter of the tail `M`. When the tail is empty it is a `D` or the end of the word, since an interior is followed by a `D`, and a production that is a tail or follows an `R` ends where the production containing it ends. So the factors `DU` are the tails that start with `U`.

Requiring a nonempty interior and restricting the tail to `empty | R M` are the two cuts, and bounding the height of the interior by `k − 1` gives `E_k`. The parse of a tower word of height at most `k` uses neither an empty interior nor a tail starting with `U`, so it survives the cuts; the cut grammar keeps only Motzkin parses, so it parses each word at most once. So `E_k` generates exactly the tower words of height at most `k`, each once.[^11]

The steep Dyck words, with no factor `x x̄ x`, come from the Dyck grammar the same way: in the grammar of nonempty Dyck words the factor comes only from the rule `D′ → x x̄ D′`, and removing it leaves `S → x x̄ | x S x̄ | x S x̄ S` ([[dyck-words](pages/dyck-words.md)]).[^12]

Without the height bound, the cut grammar is the decomposition Deutsch and Elizalde give for cornerless Motzkin paths, which "parallels the standard recursive decomposition of Motzkin paths": a nonempty path is `HA`, `UA′D` or `UA′DHA` with `A′` nonempty, where `H` is `R` and `A′` is `V` ([[deutsch-elizalde-2016-bargraphs-cornerless-motzkin](pages/deutsch-elizalde-2016-bargraphs-cornerless-motzkin.md)]).[^13] Prodinger counts Motzkin paths with a weight on each `UD` and a weight on each `DU`, so that both weights 0 give the cornerless paths and both weights 1 all Motzkin paths ([[prodinger-2025-cornerless-motzkin-bargraphs](pages/prodinger-2025-cornerless-motzkin-bargraphs.md)]).[^14] In the grammar these are weights on the two cuts, one on each empty interior and one on each tail that starts with `U`.[^11]

## Counts

Let `x` mark each `R` and `y` each block, so that towers on a base of length `L` with `b` blocks have weight `x^L y^b`, and let `E_k(x, y)` be the sum of the weights of the towers of height at most `k`. Each production gives one term, as in the [[symbolic-method](pages/symbolic-method.md)]: `1` for the empty word, `x E_k` for a gap column and the rest, and `y (E_{k−1} − 1)(1 + x E_k)` for a block, its nonempty towers `V` and its tail. So

```
E_k  =  1 + x E_k + y (E_{k−1} − 1)(1 + x E_k),        E_0  =  1/(1 − x),
```

and solving for `E_k`,

```
E_k  =  (y E_{k−1} + 1 − y) / (−xy E_{k−1} + 1 − x + xy).
```

This is a linear fractional (Möbius) map `E ↦ (aE + b)/(cE + d)` applied to `E_{k−1}`, so the height step is one 2 × 2 matrix acting on the numerator and the denominator:[^15]

```
A  =  [  y        1 − y    ]        det A  =  y,
      [ −xy    1 − x + xy  ]

(num_k, den_k)  =  A^k (1, 1 − x),        E_k  =  num_k / den_k.
```

The two counts of [[castle-counting-formula](pages/castle-counting-formula.md)] are its specializations:[^16]

- At `y = 1` the equation is Equation (2) there, and `A = [[1, 0], [−x, 1]]` gives `1/E_k = 1/E_{k−1} − x`, so `E_k = 1/(1 − (k+1)x)` and `T(k, L) = (k+1)^L`.
- At `y = −1` the equation is Equation (3) there, and `A = [[−1, 2], [x, 1 − 2x]]` is the update `num_k = 2 den_{k−1} − num_{k−1}`, `den_k = (1 − 2x) den_{k−1} + x num_{k−1}` of Equation (5), so `E_k(x, −1)` is the generating function `P_k(x)` of the signed tower count `P(k, L)`.

**The fixed point.** A tower with `b` blocks has height at most `b`, so the coefficient of `x^L y^b` in `E_k` is the same for all `k ≥ b`, and `E_k` converges coefficient by coefficient to the generating function `E_∞` of the towers of every height. `E_∞` is a fixed point of the height map:

```
xy E_∞²  −  (1 − x)(1 − y) E_∞  +  (1 − y)  =  0.
```

A castle is a bottom row `U … D` carrying towers on a base of length at least 1, so the castles by width and blocks have generating function `B = y(E_∞ − 1)`, and in `B` the fixed-point equation is

```
x B²  −  (1 − x − y − xy) B  +  xy  =  0,
```

Deutsch and Elizalde's equation for bargraphs counted by width and up steps ([[deutsch-elizalde-2016-bargraphs-cornerless-motzkin](pages/deutsch-elizalde-2016-bargraphs-cornerless-motzkin.md)]).[^17] So the castles of height at most `h` are `B_h = y(E_{h−1} − 1)`, the iterates of the map `B ↦ y[(1 + B)/(1 − x(1 + B)) − 1]` from `B_0 = 0`, and they converge to Deutsch and Elizalde's generating function.[^18] Deutsch and Elizalde count bargraphs by area with `M_area(t, x, y) = 1/(1/(1 + y(M_area(t, tx, y) − 1)) − x)` and iterate it into a continued fraction;[^19] at `t = 1` this is the height map, and for `t ≠ 1` each step substitutes `tx` for `x`, so the iterates are no longer powers of one matrix.

**The signed count in the height direction.** At `y = −1`, `A` has trace `−2x` and determinant `−1`, so `A² = −2x A + I` by the Cayley-Hamilton theorem, the numerators and the denominators each satisfy `s_{k+1} = −2x s_k + s_{k−1}`, the Pell-polynomial recurrence of [[generating-function-gallery](pages/generating-function-gallery.md)], and the eigenvalues are `−x ± √(1 + x²)`, which are `±1` at `x = 0`. Expanding `P_k` in these eigenvalues proves that for every `L ≥ 4` the shortest recurrence of `P(·, L)` in `k` has the eigenvalue `−1` with multiplicity `L` and `+1` with multiplicity `L − 2` ([[signed-tower-k-direction](pages/signed-tower-k-direction.md)], section *Proof of the multiplicities*). At `k = 1` the signed count also has a combinatorial proof, a sign-reversing involution that changes one column ([[signed-tower-count](pages/signed-tower-count.md)], section *The case k = 1*).

## Independence of the towers on different blocks

In the production `U V D (empty | R E_k)`, the towers `V` on a block come from their own copy of `E_{k−1}`, independent of the rest of the word. So the towers on different blocks of a row are independent, and the gap between two blocks of a row separates the towers above them as well.[^20] This independence makes the count multiply over the blocks, which is the induction proof of `T(k, L) = (k+1)^L` ([[castle-counting-formula](pages/castle-counting-formula.md)], section *Tower count*).

A Dyck word in `U` and `D` alone records how the blocks nest and their left-to-right order, but not their widths or the gaps between them. The letter `R` records the columns: the towers of height 0 on a base of length `L` are written `R^L`, and the gaps between neighboring blocks are `R`s. The cycle-forest form, which matches each `U` with the `D` that closes it and drops the `R`s, keeps only the nesting of the blocks and does not determine the towers ([[castle-representations](pages/castle-representations.md)]).[^21] The towers `(1, 0, 1)`, written `URDRURD`, and `(1, 1, 0, 0, 1)`, written `URRDRRURD`, have the same cycle forest, two blocks side by side.

## Appearances in Sources

- [[project-euler-502-representations](pages/project-euler-502-representations.md)] - the tower word, the grammar under the name generalized Dyck grammar, its two worked examples, and its description as the Dyck first-return split with one extra letter.
- [[project-euler-502-castle-factoring](pages/project-euler-502-castle-factoring.md)] - the grammar read as a factorization of a tower into blocks separated by `R` gaps, and the cycle-forest form.
- [[project-euler-502-observations](pages/project-euler-502-observations.md)] - the independence of the towers on two blocks of the same row.
- [[dyck-words](pages/dyck-words.md)] - the Dyck first-return grammar, and the steep Dyck words, made by removing the one rule that creates `x x̄ x`.
- [[deutsch-elizalde-2016-bargraphs-cornerless-motzkin](pages/deutsch-elizalde-2016-bargraphs-cornerless-motzkin.md)] - the decomposition `HA | UA′D | UA′DHA` of cornerless Motzkin paths, with `A′` nonempty: this grammar without the height bound, with `H` for `R` and `A′` for `V`, the bargraph equation as the fixed point of the height map, and the area continued fraction, which at `t = 1` iterates it.
- [[prodinger-2025-cornerless-motzkin-bargraphs](pages/prodinger-2025-cornerless-motzkin-bargraphs.md)] - Motzkin paths counted with a weight on each `UD` and each `DU`; both weights 0 give the tower words.

## Related Concepts

- [[urd-step-strings](pages/urd-step-strings.md)] - the step-string encoding of castles over which the grammar is defined.
- [[castle-counting-formula](pages/castle-counting-formula.md)] - the generating functions `E_k(x)` and `P_k(x)` read off the grammar, and the formula for `A^e(w, h)`.
- [[tower-word-language](pages/tower-word-language.md)] - the tower words as a language of Motzkin paths (`U`, `R`, `D` as steps `+1`, `0`, `−1`) without `UD` and `DU`, the lemma that the heights of the `R`s determine a tower word, and the language at fixed height (regular) and without a bound (algebraic).
- [[motzkin-numbers](pages/motzkin-numbers.md)] - the Motzkin paths and the first-return recurrence that the two cuts restrict.
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
[^9]: [[project-euler-502-representations](pages/project-euler-502-representations.md)] §"The grammar" L278 - "This is the Dyck first-return split U w_1 D w_2 with one extra letter."
[^10]: raw/motzkin-numbers.wiki §"Motzkin Numbers" L11-19 - "M_0 = 1, \qquad M_1 = 1" and "M_n = M_{n-1} + \sum_{k=0}^{n-2} M_k M_{n-2-k}".
[^11]: Verified by execution (Python 3.11, 2026-10-25): every word over `{U, R, D}` of length at most 11 has one parse by `M → empty | R M | U M D M` if it is a Motzkin path and none otherwise; in that parse the empty interiors are the factors `UD` of the word and the tails starting with `U` are its factors `DU`; and the cut grammar generates exactly the tower words, each once, with no height bound and with height at most `k` for `k ≤ 3`.
[^12]: [[dyck-words](pages/dyck-words.md)] §"Steep Dyck Words" L130-145 - "D′ → x x̄ | x x̄ D′ | x D′ x̄ | x D′ x̄ D′", "The forbidden x x̄ x sequence is produced only by the second rule", "S → x x̄ | x S x̄ | x S x̄ S".
[^13]: [[deutsch-elizalde-2016-bargraphs-cornerless-motzkin](pages/deutsch-elizalde-2016-bargraphs-cornerless-motzkin.md)] p.2 §2 L89-92 - "Cornerless Motzkin paths admit a very simple decomposition that parallels the standard recursive decomposition of Motzkin paths", "every nonempty path in M can be decomposed uniquely as HA, U A′ D, or U A′ DHA, where A is an arbitrary path in M and A′ is an arbitrary nonempty path".
[^14]: [[prodinger-2025-cornerless-motzkin-bargraphs](pages/prodinger-2025-cornerless-motzkin-bargraphs.md)] p.3 §1 L117-120 - "enumeration of Motzkin paths where peaks resp. valleys may occur but are counted using extra variables σ and τ", "if both variables are zero, we are in the cornerless world, and if σ = τ = 1, we have ordinary Motzkin paths".
[^15]: Verified by execution (Python 3.11 with SymPy, 2026-10-25): `det A = y`; for `k ≤ 5` and `L ≤ 7`, the coefficient of `x^L` in `num_k / den_k` with `(num_k, den_k) = A^k (1, 1 − x)` equals `Σ y^{blocks}` over the towers in `{0, …, k}^L`; at `y = 1`, `E_k = 1/(1 − (k+1)x)` for `k ≤ 5`; at `y = −1`, `A` reproduces Equation (5) of the counting formula for `k ≤ 8`.
[^16]: [[project-euler-502-representations](pages/project-euler-502-representations.md)] §"Unsigned count" L282-303, §"Signed count" L316-340 - "E_k = 1 + x E_k + (E_{k-1} - 1)(1 + x E_k)", "E_k = 1/(1 - (k+1)x)", "Weight each block, that is each D, by -1", "P_k = 1 + x P_k - (P_{k-1} - 1)(1 + x P_k)", "num_k = 2 den_{k-1} - num_{k-1}, den_k = den_{k-1}(1-2x) + x num_{k-1}".
[^17]: [[deutsch-elizalde-2016-bargraphs-cornerless-motzkin](pages/deutsch-elizalde-2016-bargraphs-cornerless-motzkin.md)] pp.2-3 §2 L94-101 [synthesis] - equation (1), `M = (1 + y(M − 1))(1 + xM)`, and with `B = y(M − 1)`, "a consequence of the bijection ∆", equation (2), `xB² − (1 − x − y − xy)B + xy = 0`.
[^18]: Verified by execution (Python 3.11 with SymPy, 2026-10-25): the fixed-point equation of the height map, and in `B = y(E − 1)` Deutsch and Elizalde's equation (2); the map in `B`; its iterates from `B_0 = 0` equal the castles of height at most `h` by width and blocks for `h ≤ 5`, `w ≤ 7`.
[^19]: [[deutsch-elizalde-2016-bargraphs-cornerless-motzkin](pages/deutsch-elizalde-2016-bargraphs-cornerless-motzkin.md)] pp.15-16 §3.14 L747-757 [synthesis] - `M_area(t, x, y) = (1 + y(M_area(t, tx, y) − 1))(1 + xM_area(t, x, y))`, solved as `1/(1/(1 + y(M_area(t, tx, y) − 1)) − x)`, and "Iterating this formula to get a continued fraction".
[^20]: [[project-euler-502-observations](pages/project-euler-502-observations.md)] §"Sub-block independence" L5 - "Two sibling blocks in the same row generate towers that never interact (the parent-row gap is automatic)."
[^21]: [[project-euler-502-castle-factoring](pages/project-euler-502-castle-factoring.md)] §"Cycle-forest form" L208-212 - "Match each U with the D that closes it (stack matching). Each matched pair is a block", "The forest is only the vertical nesting skeleton: it discards the R steps, so it does not recover the tower word", "Above a length-L base the tower with no blocks is R^L, a simple horizontal run with no vertical steps."
