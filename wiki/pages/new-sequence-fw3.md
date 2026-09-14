---
title: "New sequence candidate: F(w,3)"
category: Sources
summary: The cleanest new-sequence candidate — even-block castles of height exactly 3; an order-6 C-finite sequence 0,0,3,21,89,307,… with recurrence, g.f., and program, drafted for OEIS submission.
tags: [oeis, castle, new-sequence, c-finite, height-3, source]
sources: [new-sequence-fw3]
created: 2026-09-13
updated: 2026-09-13
---

# New sequence candidate: F(w,3)

**Source:** `~/code/oeis/pe502/new-sequence-F3.md`, copied to `raw/oeis-pe502/`
**Date ingested:** 2026-09-13
**Type:** draft new-sequence submission package (verified)

## Summary

`F(w,3)` — the number of [[castle-polyomino](pages/castle-polyomino.md)] of width *w* and height **exactly 3** with an **even** number of blocks — is the cleanest generation candidate from the [[oeis-mining-pe502](pages/oeis-mining-pe502.md)] pass: no OEIS match, but a clean C-finite structure. The sequence (offset 1, `a(w) = F(w,3)`) begins[^1]

```
0, 0, 3, 21, 89, 307, 977, 3031, 9321, 28479, 86505, 261615, 788969, …
```

(re-verified against the definition during ingest; the two leading zeros are meaningful — a width-1 or width-2 castle of height 3 always has 3 blocks, which is odd, so none has an even block count).[^2] It is **C-finite of order 6**, with characteristic polynomial `(x−3)(x−2)(x²−x+2)(x²−2x+2)` and recurrence[^3]

```
a(n) = 8a(n−1) − 27a(n−2) + 54a(n−3) − 70a(n−4) + 56a(n−5) − 24a(n−6)   (n ≥ 7)
```

and generating function `A(x) = (3x³ − 3x⁴ + 2x⁵) / (1 − 8x + 27x² − 54x³ + 70x⁴ − 56x⁵ + 24x⁶)`. The closed form ties it to the machinery: `a(n) = (3^n − 2^n − P(2,n) + P(1,n))/2` with `P(1,n) = Re((1+i)^{n+1}) = A146559(n+1)` and `P(2,n)` the order-3 [[signed-tower-count](pages/signed-tower-count.md)]; the complement gives `F(w,3) + odd(w,3) = 3^n − 2^n = A001047(n)`.[^4]

The order is 6 rather than the naive 9 because `P(2,·)` shares the factor `(x−2)` with `2^w`.[^3] The taller analogues `F(w,4)` (order 9), `F(w,5)` (order 11), the odd companions `odd(w,h≥3)`, and the column direction (`F(w,·)` quasi-polynomial, annihilated by `(x²−1)^w`) are sibling generation candidates.[^5]

## Draft status

`new-sequence-F3.md` is a **checked, correct starting point** — name, definition, 50 terms, recurrence, g.f., Python program, crossrefs — but per [[oeis-cross-referencing](pages/oeis-cross-referencing.md)] the prose must be reworded and signed by a human before submission (OEIS forbids AI-authored text), and new contributors are throttled, so the A038505/A038503 interlink ([[oeis-height2-hyperbolic-castles](pages/oeis-height2-hyperbolic-castles.md)]) is submitted first. The full draft lives in `raw/oeis-pe502/new-sequence-F3.md`.

## Key Takeaways

- `F(w,3)`: `0,0,3,21,89,307,977,3031,…`, no OEIS match — a genuine new sequence.[^1]
- Order-6 C-finite, char. poly `(x−3)(x−2)(x²−x+2)(x²−2x+2)`, with explicit recurrence and g.f.[^3]
- `a(n) = (3^n − 2^n − P(2,n) + P(1,n))/2`; `F(w,3) + odd(w,3) = 3^n − 2^n = A001047(n)`.[^4]
- Siblings (also new): `F(w,4)`, `F(w,5)`, `odd(w,h≥3)`, and the quasi-polynomial column direction.[^5]

## Entities & Concepts

- [[castle-counting-function](pages/castle-counting-function.md)] — `F(w,h)`, of which this is the `h=3` row.
- [[signed-tower-count](pages/signed-tower-count.md)] — `P(1,·)`, `P(2,·)` in the closed form.
- [[oeis-cross-referencing](pages/oeis-cross-referencing.md)] — the submission discipline (draft kept in raw/).
- [[hyperbolic-sequence-family](pages/hyperbolic-sequence-family.md)] — the `h=2` analogue F(w,2) = A038505(w+1).

## Relation to Other Wiki Pages

The generation counterpart to the [[oeis-height2-hyperbolic-castles](pages/oeis-height2-hyperbolic-castles.md)] interlink: where `h=2` matched an existing family, `h=3` is new. It exercises the [[signed-tower-count](pages/signed-tower-count.md)] `P(2,·)` and the [[castle-counting-formula](pages/castle-counting-formula.md)] directly, and heads a family (`h≥3` rows, odd companions, quasi-poly columns) of further new sequences.

## Footnotes

[^1]: [[new-sequence-fw3](pages/new-sequence-fw3.md)] `new-sequence-F3.md` §"The sequence" — "0, 0, 3, 21, 89, 307, 977, 3031, 9321, 28479, 86505, 261615, 788969, …"; re-verified against the brute definition during ingest (w=1..8).
[^2]: [[new-sequence-fw3](pages/new-sequence-fw3.md)] `new-sequence-F3.md` §"Data & offset" — "offset 1 ... submit with the two leading zeros a(1) = a(2) = 0 — they are meaningful ... a width-1 or width-2 castle of height 3 always has max(c) = 3 blocks (odd), so none has an even block count."
[^3]: [[new-sequence-fw3](pages/new-sequence-fw3.md)] `new-sequence-F3.md` §"Formula" — "a(n) = 8*a(n-1) - 27*a(n-2) + 54*a(n-3) - 70*a(n-4) + 56*a(n-5) - 24*a(n-6) ... Characteristic polynomial (x-3)(x-2)(x^2-x+2)(x^2-2x+2)"; and `mine-notes.md` §"Vein 3" L71-79 "F(w,3): order 6 ... loses one order because P(2,·) has x-2 as a factor, shared with 2^w."
[^4]: [[new-sequence-fw3](pages/new-sequence-fw3.md)] `new-sequence-F3.md` §"Formula" — "a(n) = (3^n - 2^n - P(2,n) + P(1,n)) / 2, where P(1,n) = Re((1+i)^(n+1)) = A146559(n+1) ... a(n) + odd(n,3) = 3^n - 2^n = A001047(n)."
[^5]: [[new-sequence-fw3](pages/new-sequence-fw3.md)] `mine-notes.md` §"Vein 3" L71-79 — "F(w,4): order 9 ... F(w,5): order 11 ... Columns (fixed w, varying h) are quasi-polynomials: F(w,h) is annihilated by (x^2-1)^w."
