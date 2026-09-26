---
title: "Exercises in Basic Ring Theory (Călugăreanu, Hamburg 1998)"
category: Sources
summary: An exercise book with full solutions (17 chapters, mostly general and often noncommutative ring theory), read selectively for the algebra behind the castle ring F_p[x]/(char_k). Chapter 17 is ingested - CRT for comaximal ideals (17.20), idempotents as ring splittings (17.19, 17.8), Eisenstein over a UFD (17.21), functions on a finite field are polynomials (17.13), Z[i]/H finite (17.18). Eisenstein turned into a new result - char_k is irreducible for k = 2^m - 1. Chapters 14, 13, 12, 5, 4 are queued.
tags: [book, source, ring-theory, exercises, chinese-remainder-theorem, idempotent, eisenstein, finite-field, gaussian-integers, quotient-ring]
sources: [calugareanu-hamburg-exercises-basic-ring-theory]
created: 2026-09-26
updated: 2026-09-26
---

# Exercises in Basic Ring Theory (Călugăreanu, Hamburg 1998)

**Source:** `assets/ExercisesBasicRingTheory.pdf` (Grigore Călugăreanu and Peter Hamburg, *Exercises in Basic Ring Theory*, Kluwer Texts in the Mathematical Sciences, Kluwer Academic Publishers, Dordrecht, 1998; ISBN 0-7923-4918-0). The PDF is a scan with no text layer. Page numbers below are the book's printed pages: exercises in Part I (pp. 1-76), solutions in Part II (pp. 77-194).
**Date ingested:** 2026-09-26 (Chapter 17)
**Type:** book (exercises with solutions)

## Summary

This is a problem book in basic ring theory. Each of its 17 chapters opens with a few definitions and then lists exercises, and every exercise gets a full solution in Part II. Much of it is written for rings that need not be commutative or have an identity, with left and right ideals kept apart. Chapters 7-12 and 16 (division rings, tensor products, Artinian/Noetherian rings, radicals, semisimple rings, rings of continuous functions) are mostly outside what the castle work needs.

The wiki reads it for one object: the castle ring `R = F_p[x]/(char_k)` of [[castle-cryptography-ring](pages/castle-cryptography-ring.md)] and [[castle-ring-invariant-factors](pages/castle-ring-invariant-factors.md)]. Those pages already use the Chinese Remainder Theorem, local rings and unit groups. The book supplies clean statements and short proofs for those steps, plus a few tools the wiki had not used, notably idempotents and Eisenstein's criterion.

Chapter 17, "Special Problems", is the first chapter ingested. It collects results from across the book. About a third of it is commutative and applies directly to castles. The rest (17.1-17.7, 17.9-17.12, 17.14-17.16) is about noncommutative, von Neumann regular and Artinian rings and is not used here. Applying the Eisenstein exercise to `char_k` produced a new theorem, [[char-k-eisenstein-at-two](pages/char-k-eisenstein-at-two.md)].

## Chapter 17 - the exercises used

- **17.20, CRT for comaximal ideals.** For finitely many ideals `I_1, …, I_n` of a ring with identity, three conditions are equivalent: the ideals are pairwise comaximal (`I_i + I_j = R`); every system `r ≡ a_i (mod I_i)` has a solution; and the canonical map `R/∩I_i → ∏ R/I_i` is an isomorphism.[^1] See [[chinese-remainder-theorem](pages/chinese-remainder-theorem.md)].
- **17.19, disconnected spectrum ⇔ product ⇔ idempotent.** For a commutative ring with identity, `Spec(R)` is disconnected iff `R ≅ U × V` with both factors nonzero iff `R` has an idempotent other than `0, 1`. The splitting is explicit: from an idempotent `e`, the ideals `Re` and `R(1 − e)` are comaximal and meet in zero, so `R ≅ R/Re × R/R(1 − e)`. The book's worked application is `Z_{p^k}[X]/(X² − X + p^i)`.[^2] See [[idempotent-decomposition](pages/idempotent-decomposition.md)].
- **17.8, product of the nonzero idempotents.** In a finite commutative ring with `1 ≠ 0`, the product of all nonzero idempotents is `1` if `1` is the only one, and `0` otherwise, because they pair off as `e, 1 − e` with `e(1 − e) = 0`.[^3]
- **17.21, Eisenstein over a UFD.** If `R` is a UFD, `p` a prime element dividing every coefficient of `f` except the leading one, and `p²` does not divide the constant term, then `f` is irreducible over the fraction field. If `f` is also primitive, it is irreducible in `R[X]`. The solution passes between `R[X]` and `K[X]` by Gauss's lemma.[^4] Applied to `char_k`, this gives [[char-k-eisenstein-at-two](pages/char-k-eisenstein-at-two.md)].
- **17.13, every function on a finite field is a polynomial.** Lagrange interpolation over all of `K`: `P(X) = Σ_a f(a) ∏_{b ≠ a} (X − b)/(a − b)`.[^5] See [[finite-fields](pages/finite-fields.md)].
- **17.18, `Z[i]/H` is finite for every nonzero ideal `H`.** The proof divides with remainder by the norm, using that `Z[i]` is Euclidean. It connects to castles through `char_1 = x² − 2x + 2`, whose roots are `1 ± i`, so `Z[x]/(char_1) ≅ Z[i]` via `x ↦ 1 + i`. The residue rings `Z[i]/(p)` are then exactly `F_p[x]/(char_1)`.[^6]

## Key Takeaways

- The castle ring's CRT split is 17.20 applied to the ideals `(g_i^{m_i})` of `F_p[x]`, which are pairwise comaximal because the `g_i` are distinct irreducibles.[^1]
- Each CRT factor corresponds to an idempotent of `R` (17.19). So `F_p[x]/(char_k)` has exactly `2^r` idempotents, where `r` is the number of distinct irreducible factors of `char_k mod p`. By 17.8 their nonzero product is `0` unless `char_k mod p` is a power of a single irreducible. Worked examples are on [[idempotent-decomposition](pages/idempotent-decomposition.md)].[^2][^3]
- Eisenstein at the prime 2, after rescaling `x = 2y`, proves `char_k` irreducible over `Q` for all `k = 2^m − 1`, and exactly those `k` ([[char-k-eisenstein-at-two](pages/char-k-eisenstein-at-two.md)]).[^4]
- `P(1, ·)` lives in the Gaussian integers. The book's `Z[i]` exercises (17.18, and 4.5, 4.11, 15.2 elsewhere) are statements about `Z[x]/(char_1)`.[^6]

## Chapters queued for later ingests

Ch. 14 Polynomial Rings (factoring over `Z_3, Z_5, Z_7`; units and nilpotents of `R[X]`); Ch. 13 Prime Ideals, Local Rings (the nilradical, and `R/M^n` is local, which is the theory behind the discriminant-zero pieces `F_p[x]/(g^m)`); Ch. 12 Semisimple Rings (12.6: `Z_n` is semisimple iff `n` is squarefree); Ch. 5 Characteristics (5.14, 5.16: `X^p − X − a` and `X^{p^n} − a` in characteristic `p`); Ch. 4 Ring Homomorphisms (4.4, 4.8-4.9, and the `Z[√d]` exercises 4.5, 4.11).

## Entities & Concepts

- [[chinese-remainder-theorem](pages/chinese-remainder-theorem.md)] - 17.20.
- [[idempotent-decomposition](pages/idempotent-decomposition.md)] - 17.19, 17.8.
- [[char-k-eisenstein-at-two](pages/char-k-eisenstein-at-two.md)] - 17.21 applied to `char_k`.
- [[finite-fields](pages/finite-fields.md)] - 17.13.

## Relation to Other Wiki Pages

This book gives textbook proofs for the ring-theory steps that [[castle-cryptography-ring](pages/castle-cryptography-ring.md)] §4 and [[castle-ring-invariant-factors](pages/castle-ring-invariant-factors.md)] use without proof. It adds idempotents, a computable form of the CRT split, and it corrects [[tower-parity-sectors](pages/tower-parity-sectors.md)]: that page treated odd-`k` irreducibility as settled. It is now proved for `k = 2^m − 1` and only SymPy-verified otherwise. [[castle-cryptography-number-theory](pages/castle-cryptography-number-theory.md)] gets a proof for its `char_1` and `char_3` rows.

## Footnotes

[^1]: [[calugareanu-hamburg-exercises-basic-ring-theory](pages/calugareanu-hamburg-exercises-basic-ring-theory.md)] Ex. 17.20 p.76; solution p.193 [synthesis] - equivalence of pairwise comaximality, solvability of every congruence system, and the canonical map `R/∩I_i → ∏ R/I_i` being an isomorphism; the solution notes the map is always injective and surjective iff the congruences are solvable.
[^2]: [[calugareanu-hamburg-exercises-basic-ring-theory](pages/calugareanu-hamburg-exercises-basic-ring-theory.md)] Ex. 17.19 p.75; solution pp.192-193 [synthesis] - disconnected `Spec(R)` ⇔ `R ≅ U × V` ⇔ an idempotent `e ∉ {0, 1}`; the (c)⇒(b) step uses that `Re` and `R(1 − e)` are comaximal with zero intersection; application to `Z_{p^k}[X]/(X² − X + p^i)`. The `2^r` idempotent count and castle examples are verified on [[idempotent-decomposition](pages/idempotent-decomposition.md)].
[^3]: [[calugareanu-hamburg-exercises-basic-ring-theory](pages/calugareanu-hamburg-exercises-basic-ring-theory.md)] Ex. 17.8 p.74; solution p.190 [synthesis] - nonzero idempotents pair as `e, 1 − e` with `e(1 − e) = 0`, so the product is `1` if `1` is the only nonzero idempotent and `0` otherwise.
[^4]: [[calugareanu-hamburg-exercises-basic-ring-theory](pages/calugareanu-hamburg-exercises-basic-ring-theory.md)] Ex. 17.21 p.76; solution pp.193-194 [synthesis] - Eisenstein over a UFD `R`, irreducibility in `K[X]`, and in `R[X]` for primitive `f`; the proof goes through `R[X]` being a UFD and clears denominators to pass to `K[X]`.
[^5]: [[calugareanu-hamburg-exercises-basic-ring-theory](pages/calugareanu-hamburg-exercises-basic-ring-theory.md)] Ex. 17.13 p.75; solution p.191 [synthesis] - the interpolating polynomial `Σ_{a ∈ K} f(a) ∏_{b ≠ a} (X − b)/(a − b)` agrees with `f` at every `a ∈ K`.
[^6]: [[calugareanu-hamburg-exercises-basic-ring-theory](pages/calugareanu-hamburg-exercises-basic-ring-theory.md)] Ex. 17.18 p.75; solution p.192 [synthesis] - `Z[i]` is Euclidean for the norm, so every class mod `H = (a + bi)` has a representative of norm `< a² + b²`, a finite set. The castle link is by direct check (2026-09-26): `char_1(1 + i) = (1 + i)² − 2(1 + i) + 2 = 0`, and `char_1` is the minimal polynomial of `1 + i`, so `Z[x]/(char_1) ≅ Z[1 + i] = Z[i]`.
