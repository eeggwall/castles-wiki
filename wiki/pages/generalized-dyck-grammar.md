---
title: Generalized Dyck grammar for castles
category: Concepts
summary: The tower-word grammar E_k → empty | R E_k | U V D (empty | R E_k) that recasts the castle rules as a Dyck first-return split with a nested interior tower.
tags: [concept, castle, dyck, grammar, generating-functions]
sources: [project-euler-502-representations]
created: 2026-09-13
updated: 2026-09-13
---

# Generalized Dyck grammar for castles

## Description

The [[urd-step-strings](pages/urd-step-strings.md)] generalize a Dyck path, and the connection is structural, not merely a shape analogy: the castle rules can be recast as a **grammar** over these strings, and the grammar yields the recurrence and [[generating-functions](pages/generating-functions.md)] that count castles — the route that replaces enumeration with a count.[^1]

## The tower word

A castle is read as `U (tower) D`: the outer `U…D` pair is the bottom block of width *L*, and the **tower** is everything stacked on top of it.[^2] The tower's skyline is a word over `{U, R, D}` (`U` = up one row, `R` = right one column, `D` = down one row). A tower above a length-*L* block uses exactly *L* `R`s, never drops below the base, and returns to it.[^3] Two facts drive the whole argument:[^3]

- blocks in the tower = number of `D`s = number of `U`s (each `D` completes a block);
- a valid tower word contains no `UD` (a zero-width block) and no `DU` (two touching blocks).

No-overhang needs no separate rule: each `R` is spent once — as a gap or as part of a sub-block — so a child block always sits inside its parent's span.[^4]

## The grammar

Let `E_k` denote the towers of height at most *k*. A tower is empty, starts with a gap, or starts with a peak — one production per case:[^5]

```
E_k -> empty
     | R E_k
     | U V D ( empty | R E_k )
```

Reading the alternatives:[^6]

- `empty` — the empty tower, nothing above the base.
- `R E_k` — one empty column (a gap), then the rest of the tower.
- `U V D (empty | R E_k)` — a **peak**: up onto a sub-block, the interior tower `V` sitting on it, down off it; then either stop, or a gap column and the next peak.

Here `V` is a whole tower of height at most *k*−1 (one row lower, since the sub-block itself uses a row) and is **nonempty**. Nonempty `V` is exactly what keeps the sub-block width positive (forbids `UD`); the `empty | R E_k` tail is what keeps two peaks from touching (forbids `DU`) — the same-row gap rule.[^7]

This is precisely the **Dyck first-return split** `U w₁ D w₂` with one extra letter: because `U` and `D` are *vertical* here, the interior `V` is a whole tower rather than a single matched step.[^8] Small worked examples: the tower word `URDRURD` (two width-1 sub-blocks with one gap) becomes the full castle `UURDRURDD`; the tower word `UURDD` (a width-1 sub-block carrying another) becomes `UUURDDD` — in each, the outer `U…D` pair supplies the baseline block.[^9]

The grammar is the object that the [[castle-counting-formula](pages/castle-counting-formula.md)] reads its generating functions off of — the unsigned count `T(k,L) = (k+1)^L` and the signed count `P_k` that encodes the even-block rule.

## Appearances in Sources

- [[project-euler-502-representations](pages/project-euler-502-representations.md)] — states the tower-word reading, the grammar, and its identification as a generalized Dyck first-return split.

## Related Concepts

- [[urd-step-strings](pages/urd-step-strings.md)] — the strings the grammar is defined over.
- [[castle-counting-formula](pages/castle-counting-formula.md)] — the counts read off this grammar.
- [[generating-functions](pages/generating-functions.md)] — the tool the grammar feeds.
- **Dyck Words**, **Lattice Paths** — the classical objects generalized here (not yet ingested; to be linked when added).

## Footnotes

[^1]: [[project-euler-502-representations](pages/project-euler-502-representations.md)] §"Generalized Dyck Grammar for Castles" L217 — "The U/R/D strings generalize the Dyck path, but the connection runs deeper than a shape analogy. The castle rules re-cast as a grammar over these strings, and the grammar yields the recurrence and the generating function that count castles."
[^2]: [[project-euler-502-representations](pages/project-euler-502-representations.md)] §"The tower word" L221 — "A castle is U (tower) D. The bottom block is the outer U...D pair, and the tower is everything stacked on top of it."
[^3]: [[project-euler-502-representations](pages/project-euler-502-representations.md)] §"The tower word" L227-230 — "A tower above a length-L block uses exactly L R's, never drops below the base, and returns to it," plus "blocks in the tower = number of D's = number of U's, because each D move completes a block" and "no UD ... and no DU".
[^4]: [[project-euler-502-representations](pages/project-euler-502-representations.md)] §"The tower word" L232 — "No-overhang needs no separate rule. Each R is spent once, as a gap or as part of a sub-block, so a child block always sits inside its parent's span."
[^5]: [[project-euler-502-representations](pages/project-euler-502-representations.md)] §"The grammar" L258-263 — "Let E_k be the towers of height at most k ... E_k -> empty | R E_k | U V D ( empty | R E_k )".
[^6]: [[project-euler-502-representations](pages/project-euler-502-representations.md)] §"The grammar" L267-269 — "empty is the empty tower ... R E_k is one empty column (one R), then the rest ... U V D ( empty | R E_k ) is a peak."
[^7]: [[project-euler-502-representations](pages/project-euler-502-representations.md)] §"The grammar" L276 — "V is one row lower ... and V is nonempty. Nonempty V is what keeps the sub-block width positive (no UD). The empty | R E_k tail is what keeps two peaks from touching (no DU), the same-row gap rule."
[^8]: [[project-euler-502-representations](pages/project-euler-502-representations.md)] §"The grammar" L278 — "This is the Dyck first-return split U w_1 D w_2 with one extra letter. The only change is that U and D are vertical here, so the interior V is a whole tower rather than a single matched step."
[^9]: [[project-euler-502-representations](pages/project-euler-502-representations.md)] §"The grammar" L240-256 [synthesis] — the worked tower words URDRURD → full castle UURDRURDD and UURDD → full castle UUURDDD, "with the outer U...D pair ... being the baseline block."
