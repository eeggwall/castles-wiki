---
title: Castle representations
category: Concepts
summary: Three ways to encode a castle — binary strings, integer tuples, and U/R/D step strings — and how each castle rule becomes a constraint on the encoding.
tags: [concept, castle, representations, encoding, combinatorics]
sources: [project-euler-502-representations, project-euler-502-castle-factoring, project-euler-502-solution]
created: 2026-09-13
updated: 2026-09-19
---

# Castle representations

## Description

Before a [[castle-polyomino](pages/castle-polyomino.md)] can be counted, it must be encoded, and the castle rules must be translated into constraints on the encoding.[^1] Three encodings are used in the Project Euler 502 work. Each is exact (a bijection with castles on a fixed grid), and each makes different rules easy or hard to state. This page collects all three; the U/R/D step-string encoding has its own deeper treatment at [[urd-step-strings](pages/urd-step-strings.md)] because it is the one the solution grew from.

The three encodings, using the standard w=8, h=5 example castle throughout:

### 1. Binary strings

A **column-wise** binary encoding: read each of the *w* columns as a length-*h* binary block, `1` for a filled cell and `0` for empty, giving *w* blocks each of length *h*.[^2] The example castle is:

```
11000 11100 11111 11000 11100 10000 11111 11110
```

Castle rules become bit-level constraints:[^3]

- **Height exactly h** (there is a full-height column): at least one contiguous run of *h* ones.
- **Full base / bottom row continuous**: each length-*h* block begins with a `1`.
- **Even number of blocks**: obtained by a first-difference computation (below).

**Counting blocks from the bits.** Split the string into *w* blocks of size *h*, count the ones in each block, pad the sequence with a leading and trailing `0`, and take successive differences (entry *i* minus entry *i*−1). The total number of blocks equals the absolute value of the sum of the *negative* differences.[^4] For the example:

```
per-column one-counts:   2 3 5 2 3 1 5 4
padded:                0 2 3 5 2 3 1 5 4 0
differences:            +2 +1 +2 −3 +1 −2 +4 −1 −4
negative sum:          |(−3)+(−2)+(−1)+(−4)| = 10 blocks
```

The binary encoding did not lead to the solution, but it is not incidental: it supplies the [[binary-string-bijection](pages/binary-string-bijection.md)] — a length-*L* block admits `2^L` sub-configurations, and a string with *r* runs of 1s gives *r* sub-blocks — which is the base of the induction proving `T(k,L)=(k+1)^L`.[^5] The Solution subpage is explicit that binary strings *alone* were a dead end: "the right encoding, wrong decomposition" — there is no way to count without also having the sibling-independence insight (the [[generalized-dyck-grammar](pages/generalized-dyck-grammar.md)] crux).[^13]

### 2. Integer tuples

A more compact encoding for a castle of known width: the tuple of per-column heights — equivalently, the height reached between successive rightward steps.[^6] The same example castle of width 8 is:

```
2 3 5 2 3 1 5 4
```

This is exactly the per-column one-count from the binary encoding, so the block-count check (sum of negative first-differences, hence the even-block test) carries over directly.[^6] Two further rules are immediate in this form:[^7]

- **Height exactly h**: at least one entry equals *h*.
- **Never drops below the base**: every entry is > 0.

Integer tuples were not the path to the *first* breakthrough, but the representation is the workhorse of the cycle-factorization reading (see [[project-euler-502-castle-factoring](pages/project-euler-502-castle-factoring.md)]): reading the tuple as **column heights** `c_1…c_L` above the base yields the product-form proof `T(k,L)=(k+1)^L` (each `c_i` independent over `{0,…,k}`), the descent formula for the block count that defines the [[castle-sign](pages/castle-sign.md)], the [[castle-foata-transform](pages/castle-foata-transform.md)] (peaks = positive runs of `c`), and — via first differences `d_i = c_{i+1}−c_i` — the [[monotone-streak-factorization](pages/monotone-streak-factorization.md)].

### 3. U/R/D step strings

The step-based encoding writes a castle as a string of `U` (up), `R` (right), `D` (down) steps — the same device used for the [[lattice-paths](pages/lattice-paths.md)] problem. This is the encoding that produced the breakthroughs, and it has one especially convenient property: **each `D` completes a block**, so the even-block rule is just "an even number of Ds."[^8] Its full development — the rectangular/[[convex-castle](pages/convex-castle.md)]/variations taxonomy and the [[generalized-dyck-grammar](pages/generalized-dyck-grammar.md)] it leads to — is on [[urd-step-strings](pages/urd-step-strings.md)].

## Further encodings

The castle-factoring work sketches three additional encodings, each a re-view of the tower word:[^9]

- **Excursion/gap word.** The no-`UD`/no-`DU` rules force a tower word to alternate vertical and horizontal runs, so it can be written as `(direction₁, gap₁, direction₂, gap₂, …)` — each *direction* a signed vertical-run length, each *gap* an `R`-run length. Validity is a Motzkin-like condition: every prefix of the signed directions has sum ≥ 0, and the total is 0.[^10]
- **Cycle-forest form.** Stack-match each `U` with the `D` that closes it; each matched pair is a block, and a block nested directly inside another is its child, giving a rooted forest of blocks (roots on the base). It is the castle analogue of a permutation as parenthesized cycles — but it is only the *vertical nesting skeleton*: it discards the `R` steps and so does not recover the tower word. A bare parenthesization is a two-letter Dyck word (`U` open, `D` close) and cannot record horizontal moves; the tower needs the third letter `R`. This is exactly why the model uses the three-letter [[generalized-dyck-grammar](pages/generalized-dyck-grammar.md)] rather than a bare Dyck word.[^11]
- **Signed column-difference sequence.** The run-length encoding of the first-difference sequence `d` into up-streaks, flat runs, and down-streaks — the signed form of the castle, with the down-streaks as the sign-carrying atoms and the flat runs recording gap and sub-block widths. This is the [[monotone-streak-factorization](pages/monotone-streak-factorization.md)].[^12]

## Appearances in Sources

- [[project-euler-502-representations](pages/project-euler-502-representations.md)] — defines and works all three primary encodings on the w=8, h=5 example.
- [[project-euler-502-castle-factoring](pages/project-euler-502-castle-factoring.md)] — makes the integer-tuple/column-height encoding the workhorse and sketches the three further encodings.
- [[project-euler-502-solution](pages/project-euler-502-solution.md)] — formalizes the binary encoding as the [[binary-string-bijection](pages/binary-string-bijection.md)], and notes binary-strings-without-independence as a failed route.

## Related Concepts

- [[urd-step-strings](pages/urd-step-strings.md)] — the U/R/D encoding in depth (the encoding that led to the solution).
- [[binary-string-bijection](pages/binary-string-bijection.md)] — the binary encoding formalized as an exact bijection.
- [[castle-polyomino](pages/castle-polyomino.md)] — the object being encoded.
- [[castle-counting-function](pages/castle-counting-function.md)] — the count these encodings are built to enable.
- [[monotone-streak-factorization](pages/monotone-streak-factorization.md)], [[castle-sign](pages/castle-sign.md)], [[castle-foata-transform](pages/castle-foata-transform.md)] — built on the column-height encoding.
- [[castle-snippets](pages/castle-snippets.md)] — tested Python one-liners for enumerating and predicating on the column-height (skyline) encoding.

## Footnotes

[^1]: [[project-euler-502-representations](pages/project-euler-502-representations.md)] §"Representing Castles" L3 — "Before we can count castles, we have to find a way to represent them, and translate the rules for castles into rules for constructing representations."
[^2]: [[project-euler-502-representations](pages/project-euler-502-representations.md)] §"Binary String Representation" L16 [synthesis] — describes the column-wise binary string: each column is a block of zeros (no cells) followed by ones (filled cells), giving w blocks each of length h (in the source's W/H notation).
[^3]: [[project-euler-502-representations](pages/project-euler-502-representations.md)] §"Binary String Representation" L28-32 [synthesis] — the height rule as at least one contiguous run of h ones (in the source's W/H notation), and the base rule as "each block begins with a 1."
[^4]: [[project-euler-502-representations](pages/project-euler-502-representations.md)] §"Binary String Representation" L34-60 — the per-block one-counts "2 3 5 2 3 1 5 4", padded to "0 2 3 5 2 3 1 5 4 0", differenced to "+2 +1 +2 -3 +1 -2 +4 -1 -4", and "If we sum all of the negative integers, we get the total number of blocks: 10 = |(−3)+(−2)+(−1)+(−4)|".
[^5]: [[project-euler-502-representations](pages/project-euler-502-representations.md)] §"Which representation was actually used?" L213 — "The binary-string encoding is used only as the bijection proof that a length-L block admits 2^L sub-configurations."
[^6]: [[project-euler-502-representations](pages/project-euler-502-representations.md)] §"Integer Tuples" L64-72 — "represent a castle of known width by writing the number of up or down steps, or the height, between each rightward step", example "2 3 5 2 3 1 5 4", and "the number of blocks can be obtained by summing the negative numbers".
[^7]: [[project-euler-502-representations](pages/project-euler-502-representations.md)] §"Integer Tuples" L72 [synthesis] — height exactly h is enforced by requiring at least one tuple entry equal to h (in the source's W/H notation), and never dropping below the base by requiring every entry to be > 0.
[^8]: [[project-euler-502-representations](pages/project-euler-502-representations.md)] §"Steps-Based Approach" L76,L137 — "The representation that led to the most breakthroughs ... was the same representation used to solve the Lattice Paths problem" and "each D move completes a new block, so checking if there are an even number of blocks is as easy as checking if the number of Ds is even."
[^9]: [[project-euler-502-castle-factoring](pages/project-euler-502-castle-factoring.md)] §"New representations worth writing up" L194 [synthesis] — introduces three further encodings worth writing up.
[^10]: [[project-euler-502-castle-factoring](pages/project-euler-502-castle-factoring.md)] §"Excursion/gap word" L196-204 — "a run of Us or Ds is followed by a run of Rs and vice versa ... encode it as (direction_1, gap_1, direction_2, gap_2, …) ... Validity is a Motzkin-like condition ... every prefix of the signed directions has sum ≥ 0 and the total is 0."
[^11]: [[project-euler-502-castle-factoring](pages/project-euler-502-castle-factoring.md)] §"Cycle-forest form" L206-210 — "Match each U with the D that closes it ... a rooted forest of blocks ... only the vertical nesting skeleton: it discards the R steps ... A bare parenthesization is a two-letter Dyck word ... and cannot record the horizontal moves; the tower needs the third letter R."
[^12]: [[project-euler-502-castle-factoring](pages/project-euler-502-castle-factoring.md)] §"Signed column-difference sequence" L214-216 — "The run-length encoding of the d sequence into up-streaks, flat runs, and down-streaks is the signed form of the castle. The down-streaks are the sign-carrying atoms ... and the flat runs record the gap and sub-block widths."
[^13]: [[project-euler-502-solution](pages/project-euler-502-solution.md)] §"What was tried and did not work" L189 — "Column-wise binary strings without the runs/independence insight. Right encoding, wrong decomposition: no way to count without independence."
