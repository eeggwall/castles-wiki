---
title: Dyck words
category: Sources
summary: Dyck words over {x, x̄}, counted by the Catalan numbers, read as lattice paths graded by inversion number (the area above the path, leading to the q-Catalan numbers) and as plane forests. Steep Dyck words, with no factor x x̄ x, have the grammar S → x x̄ | x S x̄ | x S x̄ S and are counted by the Motzkin numbers. The source states that the castle tower grammar generalizes the Dyck first-return split.
tags: [dyck-words, catalan, motzkin, grammar, first-return, lattice-path, symbolic-method, source]
sources: [dyck-words, algebraic-languages-and-polyominoes-enumeration]
created: 2026-09-13
updated: 2026-10-25
---

# Dyck words

**Source:** https://charlesreid1.com/wiki/Dyck_Words
**Date ingested:** 2026-09-13
**Type:** article (MediaWiki topic page)

## Summary

A **Dyck word** is a word over the two-letter alphabet `{x, x̄}` in which every left factor has at least as many `x` as `x̄`, and the whole word has as many `x` as `x̄`.[^1] Read `x` as an up step and `x̄` as a down step: a Dyck word is a lattice path that starts on the axis, never goes below it, and ends on it. The Dyck words of length `2n` number `C_n = (1/(n+1)) C(2n, n)`, the Catalan numbers `1, 1, 2, 5, 14, 42, 132, …`, and counting them by inversion number gives the [[q-catalan-numbers](pages/q-catalan-numbers.md)].[^2] For `n = 2` the Dyck words are `x x x̄ x̄` and `x x̄ x x̄`.

The source develops the following:

- **Statistics.** An *inversion* of `w = w_1 ⋯ w_{2n}` is a pair `i < j` with `w_i = x̄` and `w_j = x`, and the *down set* `D(w)` is the set of indices `i` where `w_i = x̄` and `w_{i+1} = x`. The inversion number of `w` is the area of the Ferrers diagram between `w` and the path `x ⋯ x x̄ ⋯ x̄` ([[polyominoes](pages/polyominoes.md)]).[^3] The word `x x̄ x x̄` has one inversion, and `x x x̄ x̄` has none.
- **The tree reading.** Read `x` as `(` and `x̄` as `)`, and match each `(` with the `)` that closes it. Each matched pair is a node and a pair nested inside another is its child, so a Dyck word of length `2n` is a plane forest of `n` nodes, and adding a root gives a rooted plane tree of `n + 1` nodes. `C_n` counts all three.[^4] The inversion number ranks the nested word `x ⋯ x x̄ ⋯ x̄` lowest and the alternating word `x x̄ x x̄ ⋯` highest, while the tree records the nesting.[^5]
- **Steep Dyck words**, counted by the Motzkin numbers (next section).
- **Generalizing Dyck grammars**: the first-return decomposition, which the castle tower grammar generalizes (section *The first-return grammar the castle generalizes*).

## Steep Dyck words and Motzkin

A Dyck word is **steep** if it is nonempty and has no factor `x x̄ x`. In path terms, every down step is preceded by a down step, followed by a down step, or is the last step.[^6] The steep Dyck words of length 6 are `x x x x̄ x̄ x̄` and `x x x̄ x̄ x x̄`.

The nonempty Dyck words have the grammar `D′ → x x̄ | x x̄ D′ | x D′ x̄ | x D′ x̄ D′`, and the factor `x x̄ x` comes only from the rule `D′ → x x̄ D′`. Removing that rule leaves the grammar of the steep Dyck words,[^7]

```
S  →  x x̄  |  x S x̄  |  x S x̄ S
```

With `S_n` the number of steep Dyck words of length `2n` and `G_SW(z) = Σ_{n≥1} S_n z^n` (the source writes `x` for both the letter and the variable), the grammar gives

```
G_SW(z)  =  z + z·G_SW(z) + z·G_SW(z)²,
```

so the steep Dyck words of length `2n` are counted by the `(n−1)`th [[motzkin-numbers](pages/motzkin-numbers.md)]: `1, 1, 2, 4, 9, 21, 51, …` for `n = 1, 2, 3, …`.[^7][^12] Counted by inversion number through q-grammars, they give the q-Motzkin numbers `M_{n−1}(q)`, the subject of [[steep-polyominoes-q-motzkin-bessel](pages/steep-polyominoes-q-motzkin-bessel.md)]. The source relates them to steep parallelogram polyominoes through the classical bijection between parallelogram polyominoes and Dyck words.[^8]

## The first-return grammar the castle generalizes

The source states that the first-return grammar generalizes: with other steps, the same decomposition still builds the words. For Project Euler 502 the steps are `U` (up one row), `R` (one column to the right) and `D` (down one row), a castle tower is a word in them that stays at or above the base and returns to it, and the castle rules become a grammar with the same first-return split, whose generating function gives the counts.[^9] This is the [[generalized-dyck-grammar](pages/generalized-dyck-grammar.md)]. With the extra horizontal letter `R` the split is the first-return split of Motzkin paths, and the castle rules cut it twice, once for each excluded factor `UD` and `DU`, as the steep Dyck words cut one rule from the Dyck grammar.

**As a symbolic-method specification.** This reading is the wiki's; the source does not state it. The Dyck grammar `D → ε | x D x̄ D`, as Delest and Viennot write it,[^13] splits a Dyck word at its first return to the axis: the empty word, or `x`, a Dyck word, `x̄`, and a Dyck word. As a recursive specification in the sense of [[analytic-combinatorics-ch1-ogfs](pages/analytic-combinatorics-ch1-ogfs.md)], with `z` marking each letter, the [[symbolic-method](pages/symbolic-method.md)] turns it into `D(z) = 1 + z² D(z)²`, so

```
D(z)  =  (1 − √(1 − 4z²)) / (2z²)  =  Σ_{n≥0} C_n z^{2n}.
```

The castle tower grammar is the same construction over the letters `U`, `R`, `D`, with only `R` marked, so that a word is weighted by its number of columns.

## Dyck words in Delest and Viennot

Delest and Viennot's enumeration of convex polyominoes codes them by words built from Dyck words: their type I and type III languages come from the Dyck language by rational transductions and intersection with a rational language, so the generating functions of types I and III are rational in `t` and in the Catalan generating function `c(t)`. In their words, the algebraicity is "concentrated" in the Dyck language.[^10] Their bijection β ([[parallelogram-polyomino-dyck-bijection](pages/parallelogram-polyomino-dyck-bijection.md)]) gives a second area statistic on Dyck words besides the inversion number: the sum of the heights of the peaks equals the area of the corresponding parallelogram polyomino, and the number of peaks equals its width.[^11] The two statistics differ: the inversion number is the area of the Ferrers diagram between the path and `x ⋯ x x̄ ⋯ x̄`, while the sum of peak heights is the area of the stack of columns that β builds from the peaks.

## Key Takeaways

- The Dyck words of length `2n` number `C_n` ([[catalan-numbers](pages/catalan-numbers.md)]); counted by inversion number they give the q-Catalan numbers.[^2]
- A Dyck word reads as a lattice path, graded by inversion number, and as a plane forest, which records nesting.[^5]
- The steep Dyck words, with no factor `x x̄ x`, have the grammar `S → x x̄ | x S x̄ | x S x̄ S` and generating function `G_SW = z + z G_SW + z G_SW²`; those of length `2n` are counted by the `(n−1)`th Motzkin number.[^7]
- Under Delest-Viennot's β, the sum of peak heights is the area of a parallelogram polyomino and the number of peaks its width, which gives the Narayana numbers.[^11]
- The castle tower grammar is the Dyck first-return grammar with a third letter,[^9] which makes it the Motzkin first-return grammar cut twice ([[generalized-dyck-grammar](pages/generalized-dyck-grammar.md)]).

## Entities & Concepts

- [[generalized-dyck-grammar](pages/generalized-dyck-grammar.md)] - the castle tower grammar, the Motzkin first-return split in the letters `U`, `R`, `D` with two cuts.
- [[catalan-numbers](pages/catalan-numbers.md)] - the number of Dyck words; [[q-catalan-numbers](pages/q-catalan-numbers.md)] - the Dyck words counted by inversion number and other statistics.
- [[motzkin-numbers](pages/motzkin-numbers.md)] - the number of steep Dyck words of length `2n` is the `(n−1)`th Motzkin number.
- [[steep-polyominoes-q-motzkin-bessel](pages/steep-polyominoes-q-motzkin-bessel.md)] - steep Dyck words and steep polyominoes counted by three q-Motzkin analogs.
- [[polyominoes](pages/polyominoes.md)] - Ferrers diagrams, whose area is the inversion number of a Dyck word.
- [[permutation-inversions](pages/permutation-inversions.md)] - the inversion statistic on permutations and its generating function, the q-factorial.
- [[parallelogram-polyomino-dyck-bijection](pages/parallelogram-polyomino-dyck-bijection.md)] and [[algebraic-languages-and-polyominoes-enumeration](pages/algebraic-languages-and-polyominoes-enumeration.md)] - Dyck words as parallelogram polyominoes, with area the sum of peak heights, and as the core of the convex-polyomino count.
- [[symbolic-method](pages/symbolic-method.md)] and [[analytic-combinatorics-ch1-ogfs](pages/analytic-combinatorics-ch1-ogfs.md)] - recursive specifications and their ordinary generating functions.

Also linked from the source: [[lattice-paths](pages/lattice-paths.md)].

## Relation to Other Wiki Pages

The [[generalized-dyck-grammar](pages/generalized-dyck-grammar.md)] is the Dyck first-return grammar with a third letter, that is the Motzkin first-return grammar, cut twice the way the steep Dyck grammar is cut once. The steep Dyck words lead to the q-Motzkin numbers of [[steep-polyominoes-q-motzkin-bessel](pages/steep-polyominoes-q-motzkin-bessel.md)], and the Dyck words counted by inversion number to the q-Catalan numbers of [[q-catalan-numbers](pages/q-catalan-numbers.md)].

## Footnotes

[^1]: [[dyck-words](pages/dyck-words.md)] §"Preliminary Definitions" L37-43 - "Rule 1: for any left factor u of w, |u|_x ≥ |u|_{x̄}", "Rule 2: |w|_x = |w|_{x̄}", "x is an upward diagonal step and x̄ is a downward diagonal step. Rule 1 keeps the path from dipping below the x axis, and Rule 2 makes it return to the axis."
[^2]: [[dyck-words](pages/dyck-words.md)] §"Dyck Words Definitions" L61-69 - "The number of Dyck words of length 2n is the nth Catalan number, C_n = \dfrac{1}{n+1} \binom{2n}{n} (1, 1, 2, 5, 14, 42, 132, ...). Enumerating words by inversion number leads to the q-Catalan numbers."
[^3]: [[dyck-words](pages/dyck-words.md)] §"Dyck Words Definitions" L53-81 - "An inversion is a pair w_i w_j with w_i = x̄, w_j = x, and i < j", "The down set D(w) is the set of indices where a down step is immediately followed by an up step", "The inversion number of w equals the area of the Ferrers diagram between w and the \"default\" path x x … x x̄ x̄ … x̄."
[^4]: [[dyck-words](pages/dyck-words.md)] §"The Tree Reading" L93-106 - "Read x as ( and x̄ as ), then match each ( with the ) that closes it. Each matched pair is a node, and a pair nested inside another is its child", "A word of length 2n is a forest of n nodes", "C_n counts all of these: Dyck words of length 2n, plane forests of n nodes, and rooted plane trees of n+1 nodes."
[^5]: [[dyck-words](pages/dyck-words.md)] §"The Tree Reading" L108 - "The path's area ranks the nested word x x … x x̄ x̄ … x̄ lowest and the flat alternating word highest, while the tree records nesting exactly."
[^6]: [[dyck-words](pages/dyck-words.md)] §"Steep Dyck Words" L114 - "A Dyck word is steep if it is nonempty and contains no x x̄ x factor (no up-down-up)", "every down step is preceded by a down step, followed by a down step, or is the final step."
[^7]: [[dyck-words](pages/dyck-words.md)] §"Steep Dyck Words" L130-154 - "D′ → x x̄ | x x̄ D′ | x D′ x̄ | x D′ x̄ D′", "The forbidden x x̄ x sequence is produced only by the second rule", "S → x x̄ | x S x̄ | x S x̄ S", "G_{SW}(x) = x + x G_{SW}(x) + x G_{SW}(x)^2", "so steep Dyck words of length 2n are enumerated by the (n-1)th Motzkin number."
[^8]: [[dyck-words](pages/dyck-words.md)] §"Steep Dyck Words" L118-124 - "There is a classical bijection between parallelogram polyominoes and Dyck words", "Via q-grammars, the generating function of steep Dyck words of length 2n, counted by inversion number, equals the (n-1)th q-Motzkin number M_{n-1}(q)".
[^9]: [[dyck-words](pages/dyck-words.md)] §"Generalizing Dyck Grammars" L160 - "The first-return grammar generalizes: change the steps and the same decomposition still builds words", "a castle tower is a word over these that stays above the base and returns to it. The castle rules re-cast as a grammar with the same first-return split".
[^10]: [[algebraic-languages-and-polyominoes-enumeration](pages/algebraic-languages-and-polyominoes-enumeration.md)] p.189 Remark 6.2 and p.203 §12(6) [synthesis] - "The pigmented Dyck is algebraic because V is obtained from the Dyck language D using the operations rational transduction and intersection with a rational language"; "the algebraicity has been 'concentrated' in the Dyck language. The generating functions p_I(t) and p_III(t) are rational expressions in term of t and c(t)."
[^11]: [[algebraic-languages-and-polyominoes-enumeration](pages/algebraic-languages-and-polyominoes-enumeration.md)] p.183 Prop 4.1, p.184 Remark 4.4 - "The area of P is the sum of the height of the peaks"; width-k parallelogram polyominoes number (1/n)C(n,k)C(n,k-1), "the well-known formula for the number of Dyck words of length 2n having k peaks."
[^12]: Verified by execution (Python 3.11, 2026-10-16): enumeration of all Dyck words for `n ≤ 7` gives `C_n`; the steep ones number `1, 1, 2, 4, 9, 21, 51`; the inversion number equals half the summed height difference from `x ⋯ x x̄ ⋯ x̄`, the number of unit cells of the Ferrers diagram, for `n ≤ 6`; the examples at `n = 2` and `n = 3`.
[^13]: [[algebraic-languages-and-polyominoes-enumeration](pages/algebraic-languages-and-polyominoes-enumeration.md)] pp.172-175 §2, Examples 2.1-2.3 [synthesis] - the Dyck grammar `D → xDx̄D, D → e`.
