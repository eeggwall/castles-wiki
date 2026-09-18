---
title: Castle cryptography - the number theory, for engineers
category: Analyses
summary: A from-scratch, engineer-facing explainer for the three terms the castle cryptosystem leans on — characteristic polynomial, irreducible (= prime, for polynomials), and the discrete logarithm problem (DLP) — grounded in the running castle_dh code rather than lemmas. Char poly = the recurrence's tap polynomial (same as an LFSR feedback polynomial); it is the modulus Q of the ring F_p[x]/(Q). Irreducible is the polynomial version of prime: a reducible Q lets the DLP split into cheap sub-problems by CRT/Pohlig-Hellman (structure is a liability), while an irreducible Q forces the full-size discrete log in one field F_{p^d} (less degenerate). Honest caveats: irreducible ≠ secure (small-degree finite fields have subexponential index-calculus attacks), and Berlekamp-Massey breaks any linear output regardless of Q. Companion to the castle-cryptography seminar series.
tags: [analysis, cryptography, number-theory, characteristic-polynomial, irreducible-polynomial, discrete-logarithm, finite-field, pedagogy, engineer, castle]
sources: [oeis-mining-pe502]
created: 2026-09-18
updated: 2026-09-18
---

# Castle cryptography — the number theory, for engineers

The [[castle-cryptography](pages/castle-cryptography.md)] seminar series leans on three terms that trip up anyone who has built toy crypto but isn't a number theorist. This page unpacks them from scratch, grounded in the running `castle_dh` code, not in lemmas.

## "char poly" — the characteristic polynomial

In `castle_dh`, the modulus was `Q = [-4, 4, -3, 1]`, i.e. `Q(x) = x³ − 3x² + 4x − 4`. That is the **characteristic polynomial** of the castle. It comes from the castle's count sequence `P(2,L) = 1, 1, 3, 9, 19, 33, 59, …`, which obeys a **linear recurrence**:

```
P(2,L)  =  3·P(2,L−1)  −  4·P(2,L−2)  +  4·P(2,L−3).
```

The char poly just encodes those recurrence coefficients as a polynomial: `x³ − 3x² + 4x − 4`. If you've built **LFSRs**, this *is* the feedback (tap) polynomial — same object, same role. It is the "DNA" of the sequence: from the char poly you can regenerate the whole sequence and (via [[kitamasa](pages/kitamasa.md)]) jump far ahead fast.

In the cryptosystem, `Q` is the **modulus**: all arithmetic happens "mod `Q`", meaning whenever a polynomial reaches degree 3 you apply the rewrite `x³ → 3x² − 4x + 4` to fold it back below degree 3. That rewrite *is* the recurrence, applied to polynomials instead of to numbers. The ring is `F_p[x]/(Q)` — polynomials of degree < 3, coefficients mod `p`.

## "irreducible" — yes, it's "prime" for polynomials

The instinct is right. **Irreducible = prime, but for polynomials.**

- A **prime integer** doesn't factor into smaller integers > 1: `7` is prime, `12 = 3·4` is not.
- An **irreducible polynomial** doesn't factor into smaller-degree polynomials over the given field: `x² + 1` is irreducible over the reals, `x² − 1 = (x−1)(x+1)` is not.

For the castle char polys, the split is by parity of `k`:[^1]

| | char poly | factors? |
|---|---|---|
| **even `k`** (used in the toy) | `char_2 = x³−3x²+4x−4 = (x−2)(x²−x+2)` | **reducible** (composite) |
| | `char_4 = (x²−2x+4)(x³−3x²+2x−4)` | reducible |
| | `char_6 = (x³−4x²+4x−8)(x⁴−3x³+8x²−4x+8)` | reducible |
| **odd `k`** | `char_1 = x²−2x+2` | **irreducible** (prime) |
| | `char_3 = x⁴−4x³+8x²−8x+8` | irreducible |
| | `char_5 = x⁶−6x⁵+18x⁴−32x³+48x²−32x+32` | irreducible |

One honest caveat: "irreducible" depends on *which field* you work over. The table is irreducibility over the rationals `ℚ`. When you reduce mod a specific prime `p`, an over-`ℚ`-irreducible poly can still split (that's the quadratic-reciprocity story, [[finite-fields](pages/finite-fields.md)]). But the over-`ℚ` factorization is the first-order signal, and it drives the toy's main weakness.

## "DLP" — the discrete logarithm problem

This is the hard problem the whole system's security rests on. It has the shape every toy-crypto builder knows: **easy one way, hard the other.**

In `castle_dh`:

- **Easy (forward):** given a secret exponent `a`, compute the public key `A = x^a mod Q`. That's `powmod` — about 40 multiplications even for `a = 10¹²`. Fast.
- **Hard (backward):** given `A` and `Q`, recover `a`. That's the **discrete logarithm** — "which power of `x` gives `A`?" No fast general method (in a good group), so an attacker would grind exponents.

Same shape as classic Diffie–Hellman (forward `g^a mod p` easy, backward "find `a`" hard). The only difference: instead of multiplying **numbers mod a prime**, you multiply **polynomials mod `Q`**. "Discrete" means you're in a finite set (a finite group), so "logarithm" means "which exponent," not the calculus log.

## Why irreducible `Q` gives a "less-degenerate DLP"

This is the payoff — the reason Seminar 3's first fix swaps an even-`k` `Q` for an odd-`k` one.

**Reducible `Q` (even-`k`, the toy): the DLP splits.** Because `char_2 = (x−2)(x²−x+2)`, the ring `F_p[x]/(Q)` breaks apart by the **Chinese Remainder Theorem** (the same CRT you'd use to speed up RSA) into one ring per factor:

- the `(x−2)` factor is **degree 1** → lives in `F_p` → an ordinary discrete log mod `p`;
- the `(x²−x+2)` factor is **degree 2** → lives in `F_{p²}`.

The attacker solves the two *small* discrete logs separately and recombines them (**Pohlig–Hellman**) — never facing the full degree-3 problem. Concretely, with a small `p = 101`:

```
reducible:   pieces of group order ~ (p−1)=100  and  ~(p²−1)=10200   (attacker faces 10200)
irreducible (deg 4):   one group of order  p⁴−1 = 104,060,400        (attacker faces the whole thing)
```

**Irreducible `Q` (odd-`k`): one big piece, no split.** With no factors, `F_p[x]/(Q)` is (generically) the single field `F_{p^d}`, and the DLP is the full-size discrete log in `F_{p^d}^*`, order `p^d − 1`. There is no CRT shortcut; the attacker eats the whole thing.

The engineer's one-liner: **a composite structure is only as strong as its weakest piece.** Reducible = composite = weak; irreducible = "prime" = the attacker faces the whole discrete log. It's the same reason RSA's modulus must stay unfactored — knowing the factorization *is* the break.

| | reducible `Q` (even-`k`, toy) | irreducible `Q` (odd-`k`) |
|---|---|---|
| `Q` factors? | yes, `(x−2)(x²−x+2)` | no — "prime" |
| ring `F_p[x]/(Q)` | **splits** into small pieces (CRT) | one big field `F_{p^d}` |
| attacker's job | several *small* DLPs, recombine | one *full-size* DLP |
| analogy | breaking `12` because you know `12 = 3·4` | facing a genuine large prime |

## Two caveats a builder must not skip

1. **Irreducible ≠ secure.** For `F_{p^d}` with small `d` (these char polys are degree 2–7), the discrete log has a **subexponential** attack (**index calculus**). Real finite-field crypto uses `d` huge, or elliptic curves instead, precisely because small-degree finite fields are breakable. So irreducible `Q` is *less degenerate*, not *strong*.
2. **Berlekamp–Massey doesn't care about `Q`.** It reconstructs *any* linear recurrence from its output ([[berlekamp-massey](pages/berlekamp-massey.md)]), irreducible or not. If a scheme ever leaks a stream of count terms, the castle is recovered in one line regardless of `Q`. That's why the deeper blue-team fix is *nonlinear* output, not a better modulus — see [[castle-cryptography](pages/castle-cryptography.md)] Seminar 3, Fix 2.

## Appearances in Sources

- [[oeis-mining-pe502](pages/oeis-mining-pe502.md)] - the `P(k,·)` families and their characteristic polynomials.

## Related Concepts

- [[castle-cryptography](pages/castle-cryptography.md)] - the build / red-team / blue-team seminar series this page supports.
- [[finite-fields](pages/finite-fields.md)] - `F_{p^d}`, cyclic groups, and why over-`ℚ`-irreducible polys can still split mod `p`.
- [[kitamasa](pages/kitamasa.md)] - `x^a mod Q` by binary exponentiation, the "easy forward" trapdoor direction.
- [[berlekamp-massey](pages/berlekamp-massey.md)] - recovers the char poly from the output; the linearity attack no modulus choice fixes.
- [[signed-tower-count](pages/signed-tower-count.md)] / [[generating-function-gallery](pages/generating-function-gallery.md)] - where the `char_k` characteristic polynomials come from, and the even/odd factorization pattern.
- [[tower-parity-sectors](pages/tower-parity-sectors.md)] - why even-`k` `char_k` factors (the structural fact that becomes the reducibility weakness).

## Footnotes

[^1]: Verified by execution (SymPy `Poly.is_irreducible` over `ℚ`, 2026-09-18): `char_1, char_3, char_5` (odd `k`) are irreducible; `char_2 = (x−2)(x²−x+2)`, `char_4 = (x²−2x+4)(x³−3x²+2x−4)`, `char_6 = (x³−4x²+4x−8)(x⁴−3x³+8x²−4x+8)` (even `k`) factor. The even-`k` factorization is the tower-parity-sector structure ([[tower-parity-sectors](pages/tower-parity-sectors.md)]); the `x³−4x²+4x−8` factor of `char_6` is the plastic-number factor (`2ψ²`, [[plastic-number](pages/plastic-number.md)]).
