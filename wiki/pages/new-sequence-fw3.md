---
title: "New sequence candidate: F(w,3)"
category: Sources
summary: The cleanest new-sequence candidate — even-block castles of height exactly 3; an order-6 C-finite sequence 0,0,3,21,89,307,… with recurrence, GF, and program, drafted for OEIS submission.
tags: [oeis, castle, new-sequence, c-finite, height-3, source]
sources: [new-sequence-fw3]
created: 2026-09-13
updated: 2026-09-19
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

The four components have characteristic polynomials `x − 3`, `x − 2`, `(x−2)(x² − x + 2)` (`P(2,·)`, order 3) and `x² − 2x + 2` (`P(1,·)`, order 2), degrees summing to 7; their least common multiple has degree 6 because `P(2,·)` shares the factor `(x−2)` with `2^w`, so the order is 6 (confirmed by Berlekamp–Massey on the brute-force terms).[^3] The same accounting gives order `2h + 1` for `F(w,h)` in general when nothing cancels - `9` at `h = 4`. The taller analogues `F(w,4)` (order 9), `F(w,5)` (order 11), the odd companions `odd(w,h≥3)`, and the column direction (`F(w,·)` quasi-polynomial, annihilated by `(x²−1)^w`) are sibling generation candidates.[^5]

## Where the pieces of `F(w,3)` live on the wiki

The characteristic polynomial `(x−3)(x−2)(x²−x+2)(x²−2x+2)` is assembled from parts that each have a page.

- **`x² − 2x + 2 = char_1`** (roots `1 ± i`) is `P(1,·)`, and **`(x−2)(x² − x + 2) = char_2`** is `P(2,·)` ([[signed-tower-count](pages/signed-tower-count.md)]). `char_2` is also the modulus of the toy castle cryptosystem: [[castle-cryptography-ring](pages/castle-cryptography-ring.md)] builds the ring `F_p[x]/(char_2)` and finds its period `3400` mod `101` from exactly these factors; [[castle-cryptography-number-theory](pages/castle-cryptography-number-theory.md)] explains why the reducible `char_2` splits the discrete log by Chinese Remainder Theorem (CRT); [[castle-cryptography-round-two](pages/castle-cryptography-round-two.md)] traces linear-complexity deficits to the root coincidence `λλ̄ = 2` of `x² − x + 2` - the same shared root `2` that drops this sequence's order from 7 to 6. Why `char_2` factors at all is on [[tower-parity-sectors](pages/tower-parity-sectors.md)].
- **Mod `p`.** `F(w,3) mod p` is eventually periodic with period the lcm of the orders of `3`, `2`, and the roots of the two quadratics ([[mod-p-observatory](pages/mod-p-observatory.md)], [[finite-fields](pages/finite-fields.md)]); the `x² − x + 2` factor has discriminant `−7`, so mod `7` it becomes `(x+3)²` and the period picks up a factor of `7` - the repeated-root mechanism the observatory documents for `char_2 mod 7`.
- **Extraction.** [[kitamasa](pages/kitamasa.md)] uses `P(2,·)` (recurrence `[3, −4, 4]`) as its worked order-3 example, jumping to `L = 10^6`; the rational GF `F_2(x) = num_2/den_2` behind `P(2,·)` is in the [[generating-function-gallery](pages/generating-function-gallery.md)]; and [[recurrence-discovery](pages/recurrence-discovery.md)] confirms the order-`(k+1)` recurrences by Berlekamp–Massey. The brute-force cross-check is `all_castles(w, 3)` on [[castle-snippets](pages/castle-snippets.md)] or the reference module on [[project-euler-502-brute-force](pages/project-euler-502-brute-force.md)].
- **Entropy.** The `w = 12` term, `261615`, is the `h = 3` row of the table on [[castle-entropy](pages/castle-entropy.md)]: `log₂ 261615 = 17.997` against `12·log₂ 3 − 1 = 18.02`, the even-block clause worth one bit.
- **Novelty status.** The catalogue on [[oeis-index](pages/oeis-index.md)] lists `F(w, 3…6)` as *unchecked*; a search of oeis.org for `3, 21, 89, 307, 977, 3031` on 2026-09-19 returned no results, so `F(w,3)` qualifies as **novel-candidate** as of that date.[^6] The `P(2,L)` row it is built from is itself novel-candidate there (searched 2026-09-18).

## Draft status

`new-sequence-F3.md` is a **checked, correct starting point** — name, definition, 50 terms, recurrence, GF, Python program, crossrefs — but per [[oeis-cross-referencing](pages/oeis-cross-referencing.md)] the prose must be reworded and signed by a human before submission (OEIS forbids AI-authored text), and new contributors are throttled, so the A038505/A038503 interlink ([[oeis-height2-hyperbolic-castles](pages/oeis-height2-hyperbolic-castles.md)]) is submitted first. The full draft lives in `raw/oeis-pe502/new-sequence-F3.md`.

## Key Takeaways

- `F(w,3)`: `0,0,3,21,89,307,977,3031,…`, no OEIS match — a genuine new sequence.[^1]
- Order-6 C-finite, char. poly `(x−3)(x−2)(x²−x+2)(x²−2x+2)`, with explicit recurrence and GF[^3]
- `a(n) = (3^n − 2^n − P(2,n) + P(1,n))/2`; `F(w,3) + odd(w,3) = 3^n − 2^n = A001047(n)`.[^4]
- Siblings (also new): `F(w,4)`, `F(w,5)`, `odd(w,h≥3)`, and the quasi-polynomial column direction.[^5]

## Entities & Concepts

- [[castle-counting-function](pages/castle-counting-function.md)] — `F(w,h)`, of which this is the `h=3` row.
- [[signed-tower-count](pages/signed-tower-count.md)] — `P(1,·)`, `P(2,·)` in the closed form.
- [[aocp-generating-functions](pages/aocp-generating-functions.md)] — the difference-of-powers / geometric-GF machinery behind `3^n − 2^n = A001047`.
- [[oeis-cross-referencing](pages/oeis-cross-referencing.md)] — the submission discipline (draft kept in raw/).
- [[hyperbolic-sequence-family](pages/hyperbolic-sequence-family.md)] — the `h=2` analogue F(w,2) = A038505(w+1).
- [[castle-cryptography-ring](pages/castle-cryptography-ring.md)] / [[castle-cryptography-number-theory](pages/castle-cryptography-number-theory.md)] / [[castle-cryptography-round-two](pages/castle-cryptography-round-two.md)] / [[tower-parity-sectors](pages/tower-parity-sectors.md)] — `char_2 = (x−2)(x²−x+2)`, the factor this sequence shares with the castle cryptosystem, and why it factors.
- [[mod-p-observatory](pages/mod-p-observatory.md)] / [[finite-fields](pages/finite-fields.md)] — `F(w,3) mod p` and the discriminant-`−7` double root.
- [[kitamasa](pages/kitamasa.md)] / [[generating-function-gallery](pages/generating-function-gallery.md)] / [[recurrence-discovery](pages/recurrence-discovery.md)] — extracting and confirming the `P(2,·)` component.
- [[castle-snippets](pages/castle-snippets.md)] / [[project-euler-502-brute-force](pages/project-euler-502-brute-force.md)] — brute-force cross-checks.
- [[castle-entropy](pages/castle-entropy.md)] — the `w = 12` term as an entropy data point.
- [[oeis-index](pages/oeis-index.md)] — catalogue status.

## Relation to Other Wiki Pages

The generation counterpart to the [[oeis-height2-hyperbolic-castles](pages/oeis-height2-hyperbolic-castles.md)] interlink: where `h=2` matched an existing family, `h=3` is new. It exercises the [[signed-tower-count](pages/signed-tower-count.md)] `P(2,·)` and the [[castle-counting-formula](pages/castle-counting-formula.md)] directly, and heads a family (`h≥3` rows, odd companions, quasi-poly columns) of further new sequences.

## Footnotes

[^1]: [[new-sequence-fw3](pages/new-sequence-fw3.md)] `new-sequence-F3.md` §"The sequence" L8-22 — "0, 0, 3, 21, 89, 307, 977, 3031, 9321, 28479, 86505, 261615, 788969, …"; re-verified against the brute definition during ingest (w=1..8).
[^2]: [[new-sequence-fw3](pages/new-sequence-fw3.md)] `new-sequence-F3.md` §"Data & offset" L31-33 — "offset 1 ... submit with the two leading zeros a(1) = a(2) = 0 — they are meaningful ... a width-1 or width-2 castle of height 3 always has max(c) = 3 blocks (odd), so none has an even block count."
[^3]: [[new-sequence-fw3](pages/new-sequence-fw3.md)] `new-sequence-F3.md` §"Formula" L63-68 — "a(n) = 8*a(n-1) - 27*a(n-2) + 54*a(n-3) - 70*a(n-4) + 56*a(n-5) - 24*a(n-6) ... Characteristic polynomial (x-3)(x-2)(x^2-x+2)(x^2-2x+2)"; and `mine-notes.md` §"Vein 3" L71-79 "F(w,3): order 6 ... loses one order because P(2,·) has x-2 as a factor, shared with 2^w."
[^4]: [[new-sequence-fw3](pages/new-sequence-fw3.md)] `new-sequence-F3.md` §"Formula" L56-57,L76 — "a(n) = (3^n - 2^n - P(2,n) + P(1,n)) / 2, where P(1,n) = Re((1+i)^(n+1)) = A146559(n+1) ... a(n) + odd(n,3) = 3^n - 2^n = A001047(n)."
[^5]: [[new-sequence-fw3](pages/new-sequence-fw3.md)] `mine-notes.md` §"Vein 3" L71-79 — "F(w,4): order 9 ... F(w,5): order 11 ... Columns (fixed w, varying h) are quasi-polynomials: F(w,h) is annihilated by (x^2-1)^w."
[^6]: https://oeis.org/search?q=3,21,89,307,977,3031 (2026-09-19) — the term search returns no matching sequence.
