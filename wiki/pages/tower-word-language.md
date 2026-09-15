---
title: Tower word language
category: Concepts
summary: The tower words as a formal language — a Motzkin-path language (U/R/D = +1/0/−1) with a run constraint, its unambiguous first-return grammar, and where it sits among Dyck and Motzkin.
tags: [concept, castle, formal-language, motzkin, dyck, grammar, chomsky-schutzenberger, pedagogy]
sources: [dyck-words, project-euler-502-representations]
created: 2026-09-14
updated: 2026-09-14
---

# Tower word language

## The reframing

The [[generalized-dyck-grammar](pages/generalized-dyck-grammar.md)] was invented as "the Dyck grammar with a third letter." This page gives it its proper name in formal-language terms: the tower words are a **Motzkin-path language**. Read `U = +1`, `R = 0`, `D = −1`, and a tower word is a Motzkin path — up/flat/down steps that stay `≥ 0` and return to `0` — carrying one extra **run constraint**: no `UD`, no `DU` (vertical steps come in maximal runs, separated by flats). That constraint is what makes the grammar unambiguous and the counting easy.

## The language and its grammar

A tower word over `{U, R, D}` has exactly `L` `R`s, never dips below 0, returns to 0, and has no `UD` (zero-width block) and no `DU` (two touching blocks).[^1] The grammar for towers of height ≤ *k* is[^1]

```
E_k → empty | R·E_k | U V D (empty | R·E_k),      V ∈ E_{k−1} nonempty.
```

This is the **first-return decomposition** of a Motzkin path: split at the first return to the base. Because the first step is `R` or `U` (never `D`, which would go below 0), and the `D` that closes a `U…D` peak is the *first* return, every tower word has exactly one parse — **the grammar is unambiguous.** (That uniqueness is the formal-language content of "sibling sub-blocks never interact": the first-return split cannot be made in two ways.)

## Why the generating function is rational

For **fixed *k*** the height is bounded, so the language is *regular*: a finite automaton with `k+1` states (the current height) tracks it, and "no `UD`/`DU`" is a local condition. A regular language has a rational generating function — and indeed[^2]

```
E_k(x) = 1/(1 − (k+1)x),   so   T(k,L) = (k+1)^L.
```

This is a stronger fact than the general formal-language theorem. **Chomsky–Schützenberger** says an *unambiguous context-free* grammar has an *algebraic* generating function; here the bounded height promotes the language to *regular*, so the algebraic function collapses to a rational one. (Unbounded height — all tower words, any *k* — is genuinely context-free, like Dyck and Motzkin, and its generating function is algebraic but not rational.)

## The Dyck–Motzkin–tower hierarchy

The three languages line up by step set:

| language | steps | constraint | count |
|---|---|---|---|
| Dyck | `U`/`D` (`+1/−1`) | balanced, never below 0 | Catalan `C_n` |
| Motzkin | `U`/`R`/`D` (`+1/0/−1`) | never below 0, return to 0 | Motzkin `M_n` |
| **tower word** | `U`/`R`/`D` | + **no `UD`, no `DU`** | `(k+1)^L` (by height ≤ k, width L) |

So the "generalized Dyck grammar" is **Motzkin plus a run constraint**, not a new family: `R` is exactly the Motzkin flat step, and the whole castle grammar sits inside Motzkin paths.

Two precise relationships anchor it:

- **Dyck is Motzkin with no flat steps** (`M_n`'s Catalan relatives).
- **Steep Dyck words ↔ Motzkin paths.** A Dyck word is *steep* if it contains no `UDU` factor (no up-down-up); removing the offending production from the Dyck grammar leaves `S → xx̄ | xSx̄ | xSx̄S`, whose functional equation `G = x + xG + xG²` is the Motzkin one — so steep Dyck words of length `2n` are counted by the `(n−1)`th Motzkin number.[^3]

The tower's "no `UD`/`DU`" is a *stricter* run constraint than steep's "no `UDU`" (it forbids all vertical-step adjacency, not just the `UDU` sandwich), which is precisely why the tower count `(k+1)^L` is simpler than the Motzkin `M_n`. The `R` (flat step) is doing the work: it is what lets the vertical runs sit apart, and the run constraint is what turns an algebraic Motzkin count into a rational one.

## Appearances in Sources

- [[project-euler-502-representations](pages/project-euler-502-representations.md)] — the tower word and the grammar.
- [[dyck-words](pages/dyck-words.md)] — the Dyck first-return grammar and the steep-Dyck → Motzkin bijection.

## Related Concepts

- [[generalized-dyck-grammar](pages/generalized-dyck-grammar.md)] — the grammar this page re-frames as Motzkin.
- [[motzkin-numbers](pages/motzkin-numbers.md)] — the `M_n` family (and its q-analog).
- [[dyck-words](pages/dyck-words.md)] — the two-letter root; [[steep-polyominoes-q-motzkin-bessel](pages/steep-polyominoes-q-motzkin-bessel.md)] — steep Dyck words and q-Motzkin.
- [[urd-step-strings](pages/urd-step-strings.md)] — the `U`/`R`/`D` encoding; [[castle-representations](pages/castle-representations.md)] — the column-height form the tower words encode.
- [[tower-recursion-master-class](pages/tower-recursion-master-class.md)] — the counting that the unambiguity makes legitimate.

## Footnotes

[^1]: [[project-euler-502-representations](pages/project-euler-502-representations.md)] §"The tower word" L221-230, §"The grammar" L258-269 — "A tower above a length-L block uses exactly L R's, never drops below the base, and returns to it," plus "no UD ... and no DU," and "E_k -> empty | R E_k | U V D ( empty | R E_k )" with "V ... one row lower ... and V is nonempty."
[^2]: [[project-euler-502-representations](pages/project-euler-502-representations.md)] §"Unsigned count" L297-309 — "E_k = 1/(1-(k+1)x)" and "T(k,L) = (k+1)^L".
[^3]: [[dyck-words](pages/dyck-words.md)] §"Steep Dyck Words" L114, L136-155 — "A Dyck word is steep if it is nonempty and contains no x x̄ x factor," the steep grammar "S → x x̄ | x S x̄ | x S x̄ S", and "steep Dyck words of length 2n are enumerated by the (n-1)th Motzkin number."
