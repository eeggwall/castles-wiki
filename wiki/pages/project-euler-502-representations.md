---
title: "PE 502: Representations"
category: Sources
summary: The representations subpage — three castle encodings, the convex-castle taxonomy, and the generalized Dyck grammar that yields the closed-form F(w,h).
tags: [project-euler, castle, representations, dyck, generating-functions, source, subpage]
sources: [project-euler-502-representations]
created: 2026-09-13
updated: 2026-09-13
---

# PE 502: Representations

**Source:** https://charlesreid1.com/wiki/Project_Euler/502/Representations
**Date ingested:** 2026-09-13
**Type:** article (MediaWiki subpage of [[project-euler-502](pages/project-euler-502.md)])

## Summary

This subpage is the mathematical core of the Project Euler 502 solution. It first sets up three ways to encode a [[castle-polyomino](pages/castle-polyomino.md)] — binary strings, integer tuples, and U/R/D step strings — and translates the castle rules into constraints on each encoding.[^1] It then develops the U/R/D encoding into a taxonomy (rectangular → [[convex-castle](pages/convex-castle.md)] → variations) and, crucially, recasts the castle rules as a **[[generalized-dyck-grammar](pages/generalized-dyck-grammar.md)]** over tower words. That grammar yields a generating function and, from it, the closed-form **[[castle-counting-formula](pages/castle-counting-formula.md)]** for `F(w,h)` — replacing enumeration with a direct count.[^2]

The three encodings are collected on [[castle-representations](pages/castle-representations.md)]. The step-based U/R/D form (detailed on [[urd-step-strings](pages/urd-step-strings.md)]) is the one that led to the breakthrough, in part because of one convenient property: each `D` move completes a block, so the even-block rule reduces to "an even number of Ds."[^3] The binary-string and integer-tuple encodings did not lead to the solution, but they carry structure used elsewhere in the solution (the binary encoding, for instance, supplies the bijection that a length-*L* block admits 2^L sub-configurations).[^4]

A candid section, "Which representation was actually used?", notes that the winning solution does not enumerate any of these representations directly: the binary encoding serves only as a bijection proof, and U/R/D is the mental model that revealed sub-block independence, not what the code manipulates.[^4] The concrete derivation on this page produces a formula that reproduces the problem's known checkpoints exactly — verified by running the source's own Python: `F(4,2)=10`, `F(13,10)=3729050610636`, `F(10,13)=37959702514`.[^5]

## Key Takeaways

- **Three encodings**, each translating the castle rules into constraints (see [[castle-representations](pages/castle-representations.md)]): binary strings (column-wise bits), integer tuples (per-column heights), and U/R/D step strings.[^1]
- In the **U/R/D encoding** (see [[urd-step-strings](pages/urd-step-strings.md)]), each `D` completes a block, so the even-block rule becomes "even number of Ds"; castles are organized as rectangular, [[convex-castle](pages/convex-castle.md)], and variations on convex castles.[^3]
- The number of **convex castles** on a *w*×*h* grid is `CCC = C(2H+W−3, W−1)` by a stars-and-bars argument (e.g. 210 for w=5, h=4).[^6]
- The **[[generalized-dyck-grammar](pages/generalized-dyck-grammar.md)]** `E_k → empty | R E_k | U V D (empty | R E_k)` encodes the castle rules; its unsigned generating function gives `T(k,L) = (k+1)^L` towers of height ≤ *k* above a length-*L* block.[^7]
- The **even-block rule enters as a sign** (weight each `D` by −1), giving a signed generating function `P_k` and the closed form `F(w,h) = [h^w − (h−1)^w − P(h−1,w) + P(h−2,w)] / 2` — the [[castle-counting-formula](pages/castle-counting-formula.md)], verified against all three checkpoints.[^8]

## Entities & Concepts

- [[castle-representations](pages/castle-representations.md)] — the three castle encodings collected: binary strings, integer tuples, U/R/D step strings.
- [[urd-step-strings](pages/urd-step-strings.md)] — the U/R/D step-string encoding and its castle taxonomy.
- [[convex-castle](pages/convex-castle.md)] — the front/middle/back castle class and its count.
- [[generalized-dyck-grammar](pages/generalized-dyck-grammar.md)] — the tower-word grammar recasting the castle rules.
- [[castle-counting-formula](pages/castle-counting-formula.md)] — the closed form for `F(w,h)`, with the signed/unsigned tower generating functions.
- [[castle-polyomino](pages/castle-polyomino.md)], [[castle-counting-function](pages/castle-counting-function.md)], [[generating-functions](pages/generating-functions.md)] — updated by this source.

Linked from the source but not yet ingested (later ingests): Dyck Words, Dyck Words/Examples, Lattice Paths, Project Euler/15, Project Euler/502/Solution, Project Euler/502/Implementation Notes.

## Relation to Other Wiki Pages

This page supplies the derivation that the hub [[project-euler-502](pages/project-euler-502.md)] and the [[castle-counting-function](pages/castle-counting-function.md)] pointed to. It gives [[generating-functions](pages/generating-functions.md)] its concrete instance for the castle problem and connects castles to Dyck paths and lattice paths (pages still queued). The Solution and Implementation Notes subpages (queued) describe what the code actually computes; this page establishes *why* the formula is correct.

## Footnotes

[^1]: [[project-euler-502-representations](pages/project-euler-502-representations.md)] §"Representing Castles" L1-10 [synthesis] — introduces the three encodings (binary strings, integer tuples, step-based strings) and the goal of translating castle rules into rules for constructing representations.
[^2]: [[project-euler-502-representations](pages/project-euler-502-representations.md)] §"Generalized Dyck Grammar for Castles" L215-217 — "The castle rules re-cast as a grammar over these strings, and the grammar yields the recurrence and the generating function that count castles. This is the route that replaces enumeration with a count."
[^3]: [[project-euler-502-representations](pages/project-euler-502-representations.md)] §"Steps-Based Approach" L137 — "each D move completes a new block, so checking if there are an even number of blocks is as easy as checking if the number of Ds is even."
[^4]: [[project-euler-502-representations](pages/project-euler-502-representations.md)] §"Which representation was actually used?" L213 — "The winning solution does not enumerate any of these directly. The binary-string encoding is used only as the bijection proof that a length-L block admits 2^L sub-configurations ... The U/R/D form is the mental model that unlocked the sub-block independence; it is not what the code manipulates."
[^5]: [[project-euler-502-representations](pages/project-euler-502-representations.md)] §"The main formula" L406-411 — the source's Python prints "F(4,2) = 10 / F(13,10) = 3729050610636 / F(10,13) = 37959702514"; re-run during ingest, all three reproduce exactly.
[^6]: [[project-euler-502-representations](pages/project-euler-502-representations.md)] §"Step 2 Enumerating Convex Castles" L194,L206 — "CCC = C(2(H-1)+W-1, W-1) = C(2H+W-3, W-1)" and the worked example "C(2*4 + 5 - 3, 5-1) = C(10, 4) = 210".
[^7]: [[project-euler-502-representations](pages/project-euler-502-representations.md)] §"Unsigned count" L303-309 — "E_k = 1/(1-(k+1)x)" so "T(k,L) = (k+1)^L", read off the grammar E_k → empty | R E_k | U V D (empty | R E_k).
[^8]: [[project-euler-502-representations](pages/project-euler-502-representations.md)] §"The main formula" L367 — "F(w,h) = (h^w - (h-1)^w - P(h-1,w) + P(h-2,w))/2", with the even-block rule entering as the −1 weight per D in the signed count P_k (§"Signed count" L316-333).
