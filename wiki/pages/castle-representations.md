---
title: Castle representations
category: Concepts
summary: Three ways to encode a castle of width w and height h - column-wise binary strings, the skyline tuple of column heights, and U/R/D step strings - with each castle rule written as a constraint on the encoding and the block count read off each one; plus the excursion/gap word, the cycle-forest form, the signed column-difference sequence, and the BDD/ZDD of the whole set of castles.
tags: [concept, castle, representations, encoding, combinatorics]
sources: [project-euler-502-representations, project-euler-502-castle-factoring, project-euler-502-solution]
created: 2026-09-13
updated: 2026-10-16
---

# Castle representations

## Description

To count [[castle-polyomino](pages/castle-polyomino.md)] configurations, the source first encodes them and translates the castle rules into rules on the encoding.[^1] It uses three encodings, each a bijection with the castles of width `w` and height `h`: column-wise binary strings, integer tuples, and step strings. All three are worked here on the sample castle of the problem statement, of width 8 and height 5, the skyline `(2, 3, 5, 2, 3, 1, 5, 4)`. The step-string encoding is developed further on [[urd-step-strings](pages/urd-step-strings.md)].

### 1. Binary strings

Write each column, bottom to top, as a word of length `h`, with `1` for a filled cell and `0` for an empty one; a column of height `c_i` is `1^{c_i} 0^{h − c_i}`. The castle is the `w` column words in order.[^2] The sample castle is

```
11000 11100 11111 11000 11100 10000 11111 11110
```

The castle rules become rules on the bits:[^3]

- **Height `h`:** some column word is `11…1`, with `h` ones.
- **Full bottom row:** every column word begins with `1`.
- **No overhangs:** every column word is a run of `1`s followed by a run of `0`s.
- **Even number of blocks:** read off the number of blocks, as follows.

**Counting blocks from the bits.** Count the ones in each column word, pad the list with a 0 at each end, and take successive differences, entry `i` minus entry `i − 1`. The number of blocks is the absolute value of the sum of the negative differences, the total descent of the skyline.[^4] For the sample castle:

```
ones per column:          2 3 5 2 3 1 5 4
padded:                 0 2 3 5 2 3 1 5 4 0
differences:             +2 +1 +2 −3 +1 −2 +4 −1 −4
blocks:                 |(−3) + (−2) + (−1) + (−4)| = 10
```

The sample castle has 10 blocks, an even number.

The [[binary-string-bijection](pages/binary-string-bijection.md)] uses binary strings in another way: one bit for each column of a block, marking the columns that carry a block in the next row up. Its strings with `r` runs of 1s give `r` blocks, and it is the base of the induction proof of `T(k, L) = (k+1)^L`.[^5] The source lists column-wise binary strings without the independence of the towers on different blocks among the approaches that did not work.[^13]

### 2. Integer tuples

For a castle of known width, the integer tuple is the skyline, the column heights `(c_1, …, c_w)`, equivalently the heights of the successive `R` steps of the step string.[^6] The sample castle is

```
2 3 5 2 3 1 5 4
```

These are the counts of ones per column from the binary encoding, so the block count of the binary section applies unchanged.[^6] Two rules are immediate:[^7]

- **Height `h`:** some entry equals `h`.
- **Full bottom row:** every entry is at least 1.

[[project-euler-502-castle-factoring](pages/project-euler-502-castle-factoring.md)] works with the column heights of the towers, `c_i − 1` for a castle. On them it gives the product-form proof of `T(k, L) = (k+1)^L`, with each column height chosen independently in `{0, …, k}`; the block count as total descent, the basis of the [[castle-sign](pages/castle-sign.md)]; the [[castle-foata-transform](pages/castle-foata-transform.md)], whose peaks are the maximal runs of positive column heights; and, through the first differences `d_i = c_{i+1} − c_i`, the [[monotone-streak-factorization](pages/monotone-streak-factorization.md)].

### 3. U/R/D step strings

The step encoding writes a castle as a word in the steps `U` (up one row), `R` (one column to the right) and `D` (down one row), the encoding of the [[lattice-paths](pages/lattice-paths.md)] problem.[^8] Each column contributes one `R` at its height, and the vertical steps between columns move from one height to the next. The sample castle is

```
UURURUURDDDRURDDRUUUURDRDDDD
```

Each `D` ends one block, so the castle has an even number of blocks exactly when the word has an even number of `D`s; the sample word has 10.[^8] [[urd-step-strings](pages/urd-step-strings.md)] sorts castles into rectangular castles, convex castles ([[convex-castle](pages/convex-castle.md)]) and their variations in this encoding, and [[generalized-dyck-grammar](pages/generalized-dyck-grammar.md)] gives the grammar of the words.

## Further encodings

The castle-factoring source adds three encodings, each a rewriting of the tower word, the step word of the towers on the bottom row:[^9]

- **Excursion/gap word.** A tower word has no `UD` and no `DU`, so its vertical runs are all `U`s or all `D`s and alternate with runs of `R`s. It can be written `(direction₁, gap₁, direction₂, gap₂, …)`, each direction the signed length of a vertical run and each gap the length of an `R`-run. A valid word has signed directions whose prefix sums are nonnegative and whose total is 0.[^10] The towers `(1, 0, 1)`, written `URDRURD`, give `(+1, 1, −1, 1, +1, 1, −1)`, with prefix sums `1, 0, 1, 0`.
- **Cycle-forest form.** Match each `U` with the `D` that closes it. Each matched pair is a block, and a block nested directly inside another is its child, so the blocks form a rooted forest with its roots on the base. The forest drops the `R` steps and does not recover the tower word: the towers `R^L`, with no blocks, all have the empty forest. A word in `U` and `D` alone is a Dyck word and records no horizontal moves; the towers need the third letter `R`.[^11]
- **Signed column-difference sequence.** The first differences `d` of the column heights, cut into up-streaks, flat runs and down-streaks. The magnitudes of the down-streaks add up to the block count, so the sign of the castle is `(−1)` to that sum, and the flat runs record the widths of gaps and blocks. This is the [[monotone-streak-factorization](pages/monotone-streak-factorization.md)].[^12]

A Binary Decision Diagram (BDD), or its zero-suppressed form (ZDD), encodes the whole set `V(w, h)` of even-block castles of width `w` and height `h`. It lifts the [[castle-strip](pages/castle-strip.md)] transfer matrix to an automaton whose state is the height of the last column, the block count modulo 2, and whether height `h` has been reached, and writes each column height in `⌈log_2 h⌉` Boolean variables, for a diagram of size `O(h · w · log h)`. The ZDD supports counting, uniform random sampling, ranking and unranking, and intersection with the ZDDs of other families of castles ([[castle-bdd-zdd](pages/castle-bdd-zdd.md)]).

## The skyline as a sampled signal

The integer tuple is also a sampled signal: column `i` is sample `i`, its height a quantized amplitude, and `h` the number of quantization levels. A 16-bit audio waveform, peak-normalized so that some sample reaches the top level, is a castle of height 65536 with one sample per column ([[song-as-castle](pages/song-as-castle.md)]). A row of an 8-bit grayscale image is a skyline with heights in `{1, …, 256}`, a castle of height 256 when the row contains the value 255 ([[image-as-castle](pages/image-as-castle.md)]). A pair of tones of `f_1` and `f_2` hertz, in whole hertz, sampled 8000 times per second, repeats every `8000/gcd(8000, f_1, f_2)` samples, the width of its periodic castle ([[tone-castle-catalog](pages/tone-castle-catalog.md)]). The discrete Fourier transform of the skyline is the spectrum of [[spectral-analysis](pages/spectral-analysis.md)] §3, and [[castle-phone-line](pages/castle-phone-line.md)] sends castles, played as tones, through a simulated telephone line.

## Appearances in Sources

- [[project-euler-502-representations](pages/project-euler-502-representations.md)] - the three encodings, worked on the sample castle of width 8 and height 5, with the castle rules translated into each.
- [[project-euler-502-castle-factoring](pages/project-euler-502-castle-factoring.md)] - the column heights of towers, and the excursion/gap word, cycle-forest form and signed column-difference sequence.
- [[project-euler-502-solution](pages/project-euler-502-solution.md)] - the [[binary-string-bijection](pages/binary-string-bijection.md)], and column-wise binary strings without independence among the approaches that did not work.

## Related Concepts

- [[urd-step-strings](pages/urd-step-strings.md)] - the step-string encoding, with rectangular castles, convex castles and their variations.
- [[generalized-dyck-grammar](pages/generalized-dyck-grammar.md)] - the grammar of tower words.
- [[binary-string-bijection](pages/binary-string-bijection.md)] - the configurations of blocks on a block of length `L` as binary strings of length `L`.
- [[castle-polyomino](pages/castle-polyomino.md)] - the castle definition and the block count.
- [[castle-counting-function](pages/castle-counting-function.md)] - the counts `A`, `A^e` and `A^o` of castles.
- [[monotone-streak-factorization](pages/monotone-streak-factorization.md)], [[castle-sign](pages/castle-sign.md)] and [[castle-foata-transform](pages/castle-foata-transform.md)] - constructions on the column heights of towers.
- [[castle-snippets](pages/castle-snippets.md)] - tested Python snippets that enumerate skylines and check classification predicates.
- [[block-count-constraints](pages/block-count-constraints.md)] - castles selected by block count through the generating function of the block count, starting from the run count of binary strings.

## Footnotes

[^1]: [[project-euler-502-representations](pages/project-euler-502-representations.md)] §"Representing Castles" L3 - "Before we can count castles, we have to find a way to represent them, and translate the rules for castles into rules for constructing representations."
[^2]: [[project-euler-502-representations](pages/project-euler-502-representations.md)] §"Binary String Representation" L14-24 - "a column-wise representation of the castle can be written as a binary string ... This will create a set of W blocks, each block of length H", and the sample castle "11000 11100 11111 11000 11100 10000 11111 11110".
[^3]: [[project-euler-502-representations](pages/project-euler-502-representations.md)] §"Binary String Representation" L26-28 - "castles of height H must have at least one column of height H is a restriction on the binary digits that there must be at least one contiguous block of H 1's", and "The rule that the bottom row is one continuous block ... is equivalent to saying that each block begins with a 1."
[^4]: [[project-euler-502-representations](pages/project-euler-502-representations.md)] §"Binary String Representation" L30-60 - the counts of ones "2 3 5 2 3 1 5 4", padded to "0 2 3 5 2 3 1 5 4 0", differenced to "+2 +1 +2 -3 +1 -2 +4 -1 -4", and "If we sum all of the negative integers, we get the total number of blocks: 10 = |(-3)+(-2)+(-1)+(-4)|".
[^5]: [[project-euler-502-representations](pages/project-euler-502-representations.md)] §"Which representation was actually used?" L213 - "The binary-string encoding is used only as the bijection proof that a length-L block admits 2^L sub-configurations."
[^6]: [[project-euler-502-representations](pages/project-euler-502-representations.md)] §"Integer Tuples" L64-74 - "we can represent a castle of known width by writing the number of up or down steps, or the height, between each rightward step", "This castle of width 8 can be represented with 8 integers: 2 3 5 2 3 1 5 4", "the number of blocks can be obtained by summing the negative numbers".
[^7]: [[project-euler-502-representations](pages/project-euler-502-representations.md)] §"Integer Tuples" L74 - "reach a height of exactly H by ensuring there is at least one integer with the value of H in the tuple, and ensure that the castle does not drop below the minimum height by ensuring all integers in the tuple are > 0."
[^8]: [[project-euler-502-representations](pages/project-euler-502-representations.md)] §"Steps-Based Approach" L78, L137 - "the same representation used to solve the Lattice Paths problem in Project Euler/15" and "each D move completes a new block, so checking if there are an even number of blocks is as easy as checking if the number of Ds is even." The step word of the sample castle was computed from its skyline (Python 3.11, 2026-10-16).
[^9]: [[project-euler-502-castle-factoring](pages/project-euler-502-castle-factoring.md)] §"New representations worth writing up" [synthesis] L194-216 - three further encodings of the tower word.
[^10]: [[project-euler-502-castle-factoring](pages/project-euler-502-castle-factoring.md)] §"Excursion/gap word" L198-204 - "a run of Us or Ds is followed by a run of Rs and vice versa (the no-UD, no-DU rules force the alternation)", "(direction_1, gap_1, direction_2, gap_2, …) where each direction is a signed vertical-run length and each gap is an R-run length", "every prefix of the signed directions has sum ≥ 0 and the total is 0."
[^11]: [[project-euler-502-castle-factoring](pages/project-euler-502-castle-factoring.md)] §"Cycle-forest form" L208-212 - "Match each U with the D that closes it (stack matching). Each matched pair is a block, and a block nested directly inside another is its child", "The forest is only the vertical nesting skeleton: it discards the R steps, so it does not recover the tower word. A bare parenthesization is a two-letter Dyck word (U for open, D for close) and cannot record the horizontal moves; the tower needs the third letter R", "the tower with no blocks is R^L".
[^12]: [[project-euler-502-castle-factoring](pages/project-euler-502-castle-factoring.md)] §"Signed column-difference sequence" L216 - "The run-length encoding of the d sequence into up-streaks, flat runs, and down-streaks is the signed form of the castle. The down-streaks are the sign-carrying atoms: the sign is (-1)^{sum of down-streak magnitudes}, and the flat runs record the gap and sub-block widths."
[^13]: [[project-euler-502-solution](pages/project-euler-502-solution.md)] §"What was tried and did not work" L189 - "Column-wise binary strings without the runs/independence insight. Right encoding, wrong decomposition: no way to count without independence."
