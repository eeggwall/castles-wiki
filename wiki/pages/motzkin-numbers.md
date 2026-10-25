---
title: Motzkin numbers
category: Concepts
summary: The Motzkin number M_n (OEIS A001006) counts the ways to draw nonintersecting chords among n points on a circle and the Motzkin paths of length n; 1, 1, 2, 4, 9, 21, 51, …, with M_n = M_{n−1} + Σ M_k M_{n−2−k} and M(x) = (1 − x − √(1 − 2x − 3x²))/(2x²). Deleting flat steps gives M_n = Σ_k C(n, 2k) C_k. On the castle side, M_{w−1} counts the castles with neighboring columns differing by at most 1 and both end columns at height 1, of all heights, and M_{n−1} the steep Dyck words of length 2n.
tags: [concept, motzkin, lattice-paths, q-analog, generating-functions]
sources: [motzkin-numbers, steep-polyominoes-q-motzkin-bessel, barry-2005-catalan-transform]
created: 2026-09-13
updated: 2026-10-25
---

# Motzkin numbers

## Definition

The **Motzkin number** `M_n` counts the ways to draw any number of nonintersecting chords joining `n` points on a circle, and the **Motzkin paths** of length `n`: lattice paths from `(0, 0)` to `(n, 0)` with up steps `(1, 1)`, flat steps `(1, 0)` and down steps `(1, −1)` that never go below the axis.[^1] *Example:* the four Motzkin paths of length 3 are `FFF`, `UDF`, `UFD` and `FUD`, with `U`, `F`, `D` the up, flat and down steps. The first values, for `n = 0, 1, …, 9`, are[^2]

```
1, 1, 2, 4, 9, 21, 51, 127, 323, 835.
```

A Motzkin path of length `n ≥ 1` starts either with a flat step, followed by a path of length `n − 1`, or with an up step, a path of length `k`, the down step that first returns to the axis, and a path of length `n − 2 − k`. So[^3]

```
M_0 = 1,        M_n  =  M_{n−1} + Σ_{k=0}^{n−2} M_k M_{n−2−k}        (n ≥ 1),
M(x)  =  Σ_n M_n x^n  =  (1 − x − √(1 − 2x − 3x²)) / (2x²),
```

the generating function being the root of `M = 1 + xM + x²M²` with `M(0) = 1`.

Deleting the flat steps of a Motzkin path leaves a Dyck path. Choosing the `2k` positions of the up and down steps and then a Dyck path of semilength `k` on them gives `M_n = Σ_k C(n, 2k) C_k`, with `C_k` the [[catalan-numbers](pages/catalan-numbers.md)]. Barry writes this as the binomial transform of the Catalan numbers placed on the even indices ([[binomial-transform](pages/binomial-transform.md)]).[^4] The values, the recurrence and this sum agree for `n ≤ 11`.[^5]

The source also notes that a q-analog `M_n(q)` refines the Motzkin numbers and appears in the count of steep Dyck words by a q-grammar.[^6] [[steep-polyominoes-q-motzkin-bessel](pages/steep-polyominoes-q-motzkin-bessel.md)] is the paper on these q-Motzkin numbers and steep polyominoes.

## Motzkin numbers and castles

- **Castles with steps of at most 1.** A castle whose neighboring columns differ in height by at most 1 and whose end columns both have height 1 is a Motzkin path of length `w − 1` raised by one row: the steps between columns are the steps of the path. So these castles of width `w`, over all heights, number `M_{w−1}`: at `w = 3` the castles `(1, 1, 1)` and `(1, 2, 1)` ([[motzkin-castles](pages/motzkin-castles.md)]).[^5]
- **Tower words.** The tower word of a castle, in the letters `U`, `R`, `D`, is a Motzkin path with no factor `UD` and no factor `DU` ([[tower-word-language](pages/tower-word-language.md)]). The tower grammar is the first-return decomposition above with one cut for each excluded factor: an empty interior makes `UD`, and a tail that starts with an up step makes `DU` ([[generalized-dyck-grammar](pages/generalized-dyck-grammar.md)]).
- **Steep Dyck words.** The steep Dyck words of length `2n`, with no factor `x x̄ x`, number `M_{n−1}` ([[dyck-words](pages/dyck-words.md)]).

## Appearances in Sources

- `raw/motzkin-numbers.wiki` (charlesreid1.com topic page) - the definition, the first values, the recurrence, the generating function, and the remark on the q-analog.
- [[steep-polyominoes-q-motzkin-bessel](pages/steep-polyominoes-q-motzkin-bessel.md)] - q-Motzkin numbers and steep polyominoes.
- [[barry-2005-catalan-transform](pages/barry-2005-catalan-transform.md)] - `M_n = Σ_k C(n, 2k) C_k` as a binomial transform, and the same transform taking the central binomial coefficients to the central trinomial coefficients `A002426`.

## Related Concepts

- [[motzkin-castles](pages/motzkin-castles.md)] - the castles counted by Motzkin numbers, their split by the parity of the block count (`A343386`, `A107587`), and Motzkin paths of bounded height.
- [[binomial-transform](pages/binomial-transform.md)] - the transform `Σ_k C(n, 2k) a_k`, which takes the Catalan numbers to the Motzkin numbers, applied to castle strips.
- [[catalan-numbers](pages/catalan-numbers.md)] - `C_k`, in `M_n = Σ_k C(n, 2k) C_k`.
- [[q-catalan-numbers](pages/q-catalan-numbers.md)] - the q-Catalan numbers, which reduce to the Catalan numbers at `q = 1`.
- [[tower-word-language](pages/tower-word-language.md)] - the tower words as a language of Motzkin paths.
- [[dyck-words](pages/dyck-words.md)] - the steep Dyck words, counted by `M_{n−1}`.
- [[castle-q-bessel-closed-form](pages/castle-q-bessel-closed-form.md)] - castles counted by area and blocks, through a ratio of q-Bessel series.
- [[marin-2024-polyominoes-in-rectangle](pages/marin-2024-polyominoes-in-rectangle.md)] - the row automaton for polyominoes with bounding box of width `w`, whose `A378947(w)` states are `M_{w+1} + 2M_w + M_{w−1} − 3` for `w > 0`.
- [[aocp-multinomial-coefficients](pages/aocp-multinomial-coefficients.md)] - the central trinomial coefficients `A002426`, which count the words in `U`, `R`, `D` of length `n` with as many `U` as `D`, without the condition of staying above the axis.

## Footnotes

[^1]: raw/motzkin-numbers.wiki §"Motzkin Numbers" L3 - "The Motzkin number M_n counts the ways to draw non-intersecting chords between n points on a circle, and the Motzkin paths: lattice paths from (0,0) to (n,0) using up, horizontal, and down steps that never drop below the x axis."; https://oeis.org/A001006 (read 2026-10-16) - "Motzkin numbers: number of ways of drawing any number of nonintersecting chords joining n (labeled) points on a circle."
[^2]: raw/motzkin-numbers.wiki §"Motzkin Numbers" L5-9 - "1, 1, 2, 4, 9, 21, 51, 127, 323, 835, ...".
[^3]: raw/motzkin-numbers.wiki §"Motzkin Numbers" L11-25 - "M_0 = 1, M_1 = 1", "M_n = M_{n-1} + \sum_{k=0}^{n-2} M_k M_{n-2-k}", and "M(x) = (1 - x - \sqrt{1 - 2x - 3x^2}) / (2x^2)".
[^4]: [[barry-2005-catalan-transform](pages/barry-2005-catalan-transform.md)] §7 [synthesis] L1105-L1130, L1174-L1186 - "Mn = Σ_{k=0}^{⌊n/2⌋} C(n, 2k) C(k) where Mn is the nth Motzkin number A001006", from `(1/(1 − x)) c(x²/(1 − x)²) = (1 − x − √(1 − 2x − 3x²))/(2x²)`; the transform is `Bin ∘ (1, x²)`.
[^5]: Verified by execution (Python 3.11, 2026-10-16): the recurrence, the sum `Σ_k C(n, 2k) C_k` and enumeration of Motzkin paths agree for `n ≤ 11` (paths enumerated for `n ≤ 8`); the castles with steps of at most 1 and both end columns at height 1 number `M_{w−1}` for `w ≤ 9`.
[^6]: raw/motzkin-numbers.wiki §"Motzkin Numbers" L27 - "The q-analog M_n(q) refines the Motzkin numbers and appears in the q-grammar count of steep Dyck Words."
