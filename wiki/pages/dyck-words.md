---
title: Dyck words
category: Sources
summary: The two-letter balanced words counted by the Catalan numbers, with path and plane-tree readings; steep Dyck words → Motzkin, and the first-return grammar that PE 502's castle U/R/D grammar generalizes. Under the [[symbolic-method]], the first-return grammar *is* a recursive specification `D = ε + x·D·x̄·D`.
tags: [dyck-words, catalan, motzkin, grammar, first-return, lattice-path, symbolic-method, source]
sources: [dyck-words]
created: 2026-09-13
updated: 2026-09-15
---

# Dyck words

**Source:** https://charlesreid1.com/wiki/Dyck_Words
**Date ingested:** 2026-09-13
**Type:** article (MediaWiki topic page)

## Summary

A **Dyck word** is a word over a two-letter alphabet `{x, x̄}` in which every left factor has at least as many `x` as `x̄` (the path never dips below the axis) and the whole word has equal counts (it returns to the axis).[^1] Reading `x` as an up (NE) step and `x̄` as a down (SE) step makes a Dyck word a lattice path from the axis back to it that never goes negative. The number of Dyck words of length `2n` is the *n*th Catalan number `C_n = (1/(n+1))binomial(2n,n)` (`1,1,2,5,14,42,132,…`), and enumerating them by **inversion number** leads to the [[q-catalan-numbers](pages/q-catalan-numbers.md)].[^2] This is the foundational object the castle's grammar generalizes — the conceptual root the wiki's many "Dyck" references point to.

The page develops several readings and connections:

- **Statistics.** An *inversion* is a pair `w_i = x̄`, `w_j = x` with `i<j`; the *down set* `D(w)` is the indices where a down step is immediately followed by an up step. The inversion number equals the area of the [[polyominoes](pages/polyominoes.md)] Ferrers diagram between `w` and the maximally-steep default path `x…x x̄…x̄`.[^3]
- **The tree reading.** Reading `x`/`x̄` as `(`/`)` and matching parentheses draws a plane forest of *n* nodes (a rooted plane tree of `n+1` nodes with a root added); `C_n` counts Dyck words, plane forests, and rooted plane trees alike.[^4] The path reading and tree reading are "two faces of the same word" that disagree on shape — the path grades by *area*, the tree by *nesting*.[^5]
- **Steep Dyck words** (see below) — the run-constrained sub-family that meets the Motzkin numbers.
- **Generalizing Dyck grammars** — the first-return decomposition that the castle's U/R/D grammar is an instance of (see below).

## Steep Dyck words and Motzkin

A Dyck word is **steep** if it is nonempty and contains no `x x̄ x` factor (no up-down-up) — every down step is preceded by, followed by, or ends the word.[^6] Removing exactly the offending production from the nonempty-Dyck grammar `D' → xx̄ | xx̄D' | xD'x̄ | xD'x̄D'` leaves the **steep grammar**[^7]

```
S → x x̄ | x S x̄ | x S x̄ S
```

whose generating function reads off as `G_SW(x) = x + x·G_SW(x) + x·G_SW(x)²` — the Motzkin functional equation — so **steep Dyck words of length `2n` are counted by the `(n−1)`th [[motzkin-numbers](pages/motzkin-numbers.md)]** (verified during ingest: `1,1,2,4,9,21,…`).[^7] Refined by inversion number via q-grammars, they give the q-Motzkin numbers — exactly the object of [[steep-polyominoes-q-motzkin-bessel](pages/steep-polyominoes-q-motzkin-bessel.md)], and the reason steep parallelogram polyominoes carry a q-Motzkin/q-Bessel generating function.[^8]

## The first-return grammar the castle generalizes

The page states the connection to the castle explicitly: the **first-return grammar generalizes** — keep the same "split at the first return to the base" decomposition but change the step set. In [[project-euler-502](pages/project-euler-502.md)] the steps become `U` (up a row), `R` (right a column), `D` (down a row), a castle tower is a word over these that stays above the base and returns to it, and the same first-return split gives the grammar whose generating function counts castles.[^9] This is precisely the [[generalized-dyck-grammar](pages/generalized-dyck-grammar.md)] — so the castle grammar is a *bona fide* generalization of the Dyck first-return split with one extra (horizontal) letter, not merely an analogy.

**The first-return grammar as a symbolic-method specification.** The Dyck grammar `D = ε + x·D·x̄·D` (empty word, or opening `x` + inner Dyck + closing `x̄` + trailing Dyck) is a recursive specification in the sense of [[analytic-combinatorics-part-a](pages/analytic-combinatorics-part-a.md)]: the [[symbolic-method](pages/symbolic-method.md)] translates it directly to `D(z) = 1 + z² · D(z)²` (with each of `x, x̄` marking size 1, so `x·x̄` contributes `z²`), and solving gives `D(z) = (1 − √(1−4z²))/(2z²) = ∑ C_n z^{2n}` — the Catalan generating function graded by half-length. AC's own §I.2 (pp. 33-35) develops the equivalent `G = Z × SEQ(G)` for general plane trees, which are in bijection with Dyck words; the castle's own first-return grammar is the same construction with a U/R/D alphabet and the U-and-D letters weight-marked separately.

## Key Takeaways

- Dyck word = balanced `{x, x̄}` word, path never negative; `#` of length `2n` is `C_n` ([[catalan-numbers](pages/catalan-numbers.md)]); by inversion number → q-Catalan.[^2]
- Path reading (area) and plane-tree reading (nesting) are two faces of the same word.[^5]
- **Steep Dyck words** (no `x x̄ x`) satisfy `S → xx̄ | xSx̄ | xSx̄S`, generating function `G = x + xG + xG²` → **length `2n` counted by the `(n−1)`th Motzkin number** (verified).[^7]
- The castle's U/R/D grammar is the **first-return grammar generalized** — the direct root of [[generalized-dyck-grammar](pages/generalized-dyck-grammar.md)].[^9]

## Entities & Concepts

- [[generalized-dyck-grammar](pages/generalized-dyck-grammar.md)] — the castle grammar, a first-return generalization of the Dyck grammar.
- [[catalan-numbers](pages/catalan-numbers.md)] — count Dyck words; [[q-catalan-numbers](pages/q-catalan-numbers.md)] — count them by inversion.
- [[motzkin-numbers](pages/motzkin-numbers.md)] — count steep Dyck words (length 2n → (n−1)th Motzkin).
- [[steep-polyominoes-q-motzkin-bessel](pages/steep-polyominoes-q-motzkin-bessel.md)] — steep Dyck words and their q-refinement.
- [[polyominoes](pages/polyominoes.md)] — Ferrers-diagram area = Dyck inversion number.
- [[permutation-inversions](pages/permutation-inversions.md)] — the inversion statistic (and its q-factorial g.f.) that grades Dyck words into q-Catalan / q-Motzkin.
- [[symbolic-method](pages/symbolic-method.md)] / [[analytic-combinatorics-part-a](pages/analytic-combinatorics-part-a.md)] — the framework that recasts the first-return grammar as a recursive specification.

Linked from the source but not yet ingested: Lattice Paths (ingested this round — see [[lattice-paths](pages/lattice-paths.md)]), Dyck Words/Lisp, Dyck Words/Examples, Combinatorics.

## Relation to Other Wiki Pages

This is the conceptual root of the castle's whole generating-function apparatus: the [[generalized-dyck-grammar](pages/generalized-dyck-grammar.md)] is a first-return Dyck grammar with a third letter, the steep sub-family is where the Motzkin/q-Motzkin thread of [[steep-polyominoes-q-motzkin-bessel](pages/steep-polyominoes-q-motzkin-bessel.md)] originates, and the Catalan/q-Catalan counts sit directly above it. Ingesting it resolves the "Dyck Words (not yet ingested)" placeholders across the wiki.

## Footnotes

[^1]: [[dyck-words](pages/dyck-words.md)] §"Preliminary Definitions" L37-43 — "Rule 1: for any left factor u of w, |u|_x ≥ |u|_{x̄} ... Rule 2: |w|_x = |w|_{x̄} ... x is an upward diagonal step and x̄ is a downward diagonal step. Rule 1 keeps the path from dipping below the x axis, and Rule 2 makes it return to the axis."
[^2]: [[dyck-words](pages/dyck-words.md)] §"Dyck Words Definitions" L61-69 — "The number of Dyck words of length 2n is the nth Catalan number, C_n = (1/(n+1)) binomial(2n,n) (1, 1, 2, 5, 14, 42, 132, ...). Enumerating words by inversion number leads to the q-Catalan numbers."
[^3]: [[dyck-words](pages/dyck-words.md)] §"Dyck Words Definitions" L53-81 — "An inversion is a pair w_i w_j with w_i = x̄, w_j = x, and i < j. The down set D(w) is the set of indices where a down step is immediately followed by an up step ... The inversion number of w equals the area of the Ferrers diagram between w and the 'default' path x x … x x̄ x̄ … x̄."
[^4]: [[dyck-words](pages/dyck-words.md)] §"The Tree Reading" L93-106 — "Read x as ( and x̄ as ) ... Each matched pair is a node ... A word of length 2n is a forest of n nodes ... C_n counts all of these: Dyck words of length 2n, plane forests of n nodes, and rooted plane trees of n+1 nodes."
[^5]: [[dyck-words](pages/dyck-words.md)] §"The Tree Reading" L108 — "The path reading above and the tree reading are two faces of the same word, and they disagree on shape. The path's area ranks the nested word ... lowest and the flat alternating word highest, while the tree records nesting exactly."
[^6]: [[dyck-words](pages/dyck-words.md)] §"Steep Dyck Words" L114 — "A Dyck word is steep if it is nonempty and contains no x x̄ x factor (no up-down-up) ... every down step is preceded by a down step, followed by a down step, or is the final step."
[^7]: [[dyck-words](pages/dyck-words.md)] §"Steep Dyck Words" L136-155 — the nonempty-Dyck grammar, removing the "x x̄ D'" rule to get "S → x x̄ | x S x̄ | x S x̄ S", and "G_{SW}(x) = x + x G_{SW}(x) + x G_{SW}(x)^2 ... steep Dyck words of length 2n are enumerated by the (n-1)th Motzkin number"; steep(2n) = (n−1)th Motzkin re-verified for n=1..6 during ingest.
[^8]: [[dyck-words](pages/dyck-words.md)] §"Steep Dyck Words" L124-156 — "Via q-grammars, the generating function of steep Dyck words of length 2n, counted by inversion number, equals the (n-1)th q-Motzkin number M_{n-1}(q) ... Getting the q-refinement requires the q-analog (w;q) of a Dyck word and q-grammars."
[^9]: [[dyck-words](pages/dyck-words.md)] §"Generalizing Dyck Grammars" L160 — "The first-return grammar generalizes ... In Project Euler/502 the up and right movements are split into U ..., R ..., and D ..., and a castle tower is a word over these that stays above the base and returns to it. The castle rules re-cast as a grammar with the same first-return split."
