---
title: Castle representations
category: Concepts
summary: Three ways to encode a castle — binary strings, integer tuples, and U/R/D step strings — and how each castle rule becomes a constraint on the encoding.
tags: [concept, castle, representations, encoding, combinatorics]
sources: [project-euler-502-representations]
created: 2026-09-13
updated: 2026-09-13
---

# Castle representations

## Description

Before a [[castle-polyomino](pages/castle-polyomino.md)] can be counted, it must be encoded, and the castle rules must be translated into constraints on the encoding.[^1] Three encodings are used in the Project Euler 502 work. Each is exact (a bijection with castles on a fixed grid), and each makes different rules easy or hard to state. This page collects all three; the U/R/D step-string encoding has its own deeper treatment at [[urd-step-strings](pages/urd-step-strings.md)] because it is the one the solution grew from.

The three encodings, using the standard w=8, h=5 example castle throughout:

### 1. Binary strings

A **column-wise** binary encoding: read each of the *W* columns as a length-*H* binary block, `1` for a filled cell and `0` for empty, giving *W* blocks each of length *H*.[^2] The example castle is:

```
11000 11100 11111 11000 11100 10000 11111 11110
```

Castle rules become bit-level constraints:[^3]

- **Height exactly H** (there is a full-height column): at least one contiguous run of *H* ones.
- **Full base / bottom row continuous**: each length-*H* block begins with a `1`.
- **Even number of blocks**: obtained by a first-difference computation (below).

**Counting blocks from the bits.** Split the string into *W* blocks of size *H*, count the ones in each block, pad the sequence with a leading and trailing `0`, and take successive differences (entry *i* minus entry *i*−1). The total number of blocks equals the absolute value of the sum of the *negative* differences.[^4] For the example:

```
per-column one-counts:   2 3 5 2 3 1 5 4
padded:                0 2 3 5 2 3 1 5 4 0
differences:            +2 +1 +2 −3 +1 −2 +4 −1 −4
negative sum:          |(−3)+(−2)+(−1)+(−4)| = 10 blocks
```

The binary encoding did not lead to the solution, but it is not incidental: it supplies the bijection proof that a length-*L* block admits 2^L sub-configurations, used on the Solution subpage (queued).[^5]

### 2. Integer tuples

A more compact encoding for a castle of known width: the tuple of per-column heights — equivalently, the height reached between successive rightward steps.[^6] The same example castle of width 8 is:

```
2 3 5 2 3 1 5 4
```

This is exactly the per-column one-count from the binary encoding, so the block-count check (sum of negative first-differences, hence the even-block test) carries over directly.[^6] Two further rules are immediate in this form:[^7]

- **Height exactly H**: at least one entry equals *H*.
- **Never drops below the base**: every entry is > 0.

Like the binary encoding, integer tuples were not the path to the solution, but the representation recurs in later parts of the work.

### 3. U/R/D step strings

The step-based encoding writes a castle as a string of `U` (up), `R` (right), `D` (down) steps — the same device used for the **Lattice Paths** problem (not yet ingested). This is the encoding that produced the breakthroughs, and it has one especially convenient property: **each `D` completes a block**, so the even-block rule is just "an even number of Ds."[^8] Its full development — the rectangular/[[convex-castle](pages/convex-castle.md)]/variations taxonomy and the [[generalized-dyck-grammar](pages/generalized-dyck-grammar.md)] it leads to — is on [[urd-step-strings](pages/urd-step-strings.md)].

## Appearances in Sources

- [[project-euler-502-representations](pages/project-euler-502-representations.md)] — defines and works all three encodings on the w=8, h=5 example.

## Related Concepts

- [[urd-step-strings](pages/urd-step-strings.md)] — the U/R/D encoding in depth (the encoding that led to the solution).
- [[castle-polyomino](pages/castle-polyomino.md)] — the object being encoded.
- [[castle-counting-function](pages/castle-counting-function.md)] — the count these encodings are built to enable.

## Footnotes

[^1]: [[project-euler-502-representations](pages/project-euler-502-representations.md)] §"Representing Castles" L3 — "Before we can count castles, we have to find a way to represent them, and translate the rules for castles into rules for constructing representations."
[^2]: [[project-euler-502-representations](pages/project-euler-502-representations.md)] §"Binary String Representation" L16 — "a column-wise representation of the castle can be written as a binary string, with each column consisting of two blocks: a block of zeros (indicating no blocks) and ones (indicating blocks). This will create a set of W blocks, each block of length H."
[^3]: [[project-euler-502-representations](pages/project-euler-502-representations.md)] §"Binary String Representation" L28-32 — "there must be at least one contiguous block of H 1's" and "each block begins with a 1."
[^4]: [[project-euler-502-representations](pages/project-euler-502-representations.md)] §"Binary String Representation" L34-60 — the per-block one-counts "2 3 5 2 3 1 5 4", padded to "0 2 3 5 2 3 1 5 4 0", differenced to "+2 +1 +2 -3 +1 -2 +4 -1 -4", and "If we sum all of the negative integers, we get the total number of blocks: 10 = |(−3)+(−2)+(−1)+(−4)|".
[^5]: [[project-euler-502-representations](pages/project-euler-502-representations.md)] §"Which representation was actually used?" L213 — "The binary-string encoding is used only as the bijection proof that a length-L block admits 2^L sub-configurations."
[^6]: [[project-euler-502-representations](pages/project-euler-502-representations.md)] §"Integer Tuples" L64-72 — "represent a castle of known width by writing the number of up or down steps, or the height, between each rightward step", example "2 3 5 2 3 1 5 4", and "the number of blocks can be obtained by summing the negative numbers".
[^7]: [[project-euler-502-representations](pages/project-euler-502-representations.md)] §"Integer Tuples" L72 — "the castle should reach a height of exactly H by ensuring there is at least one integer with the value of H in the tuple, and ensure that the castle does not drop below the minimum height by ensuring all integers in the tuple are > 0."
[^8]: [[project-euler-502-representations](pages/project-euler-502-representations.md)] §"Steps-Based Approach" L76,L137 — "The representation that led to the most breakthroughs ... was the same representation used to solve the Lattice Paths problem" and "each D move completes a new block, so checking if there are an even number of blocks is as easy as checking if the number of Ds is even."
