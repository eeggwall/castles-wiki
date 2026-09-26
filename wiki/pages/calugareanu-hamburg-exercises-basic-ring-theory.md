---
title: "Exercises in Basic Ring Theory (Călugăreanu, Hamburg 1998)"
category: Sources
summary: An exercise book with full solutions (17 chapters, mostly general and often noncommutative ring theory), read selectively for the algebra behind the castle ring F_p[x]/(char_k). Chapter 17 is ingested - CRT for comaximal ideals (17.20), idempotents as ring splittings (17.19, 17.8), Eisenstein over a UFD (17.21), functions on a finite field are polynomials (17.13), Z[i]/H finite (17.18). Eisenstein turned into a new result - char_k is irreducible for k = 2^m - 1. Chapter 14 is ingested - quotient maps Q[X]/(f) → Q[X]/(g) (14.4), hand factoring over Z_3, Z_5, Z_7 (14.7-14.9), polynomials vs polynomial functions (14.10), units and nilpotents of R[X] (14.15-14.16), R[X]/(X²+1) ≅ C (14.18). Chapter 13 is ingested - Spec, the nilradical, local rings R/M^n, Z[i] and Z[ω] - and gave castle-ring-spectrum. Chapters 12, 5, 4 are queued.
tags: [book, source, ring-theory, exercises, chinese-remainder-theorem, idempotent, eisenstein, finite-field, gaussian-integers, quotient-ring]
sources: [calugareanu-hamburg-exercises-basic-ring-theory]
created: 2026-09-26
updated: 2026-09-26
---

# Exercises in Basic Ring Theory (Călugăreanu, Hamburg 1998)

**Source:** `assets/ExercisesBasicRingTheory.pdf` (Grigore Călugăreanu and Peter Hamburg, *Exercises in Basic Ring Theory*, Kluwer Texts in the Mathematical Sciences, Kluwer Academic Publishers, Dordrecht, 1998; ISBN 0-7923-4918-0). The PDF is a scan with no text layer. Page numbers below are the book's printed pages: exercises in Part I (pp. 1-76), solutions in Part II (pp. 77-194).
**Date ingested:** 2026-09-26 (Chapters 17, 14 and 13)
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

## Chapter 14 - the exercises used

Chapter 14 (Polynomial Rings, exercises pp. 59-61, solutions pp. 169-172) is short and concrete: 19 exercises on zeros, factorization over small fields, ideals of `Z[X]`, and units and nilpotents of `R[X]`. None of them gives a new castle theorem on its own the way 17.21 did. They supply worked examples and the facts behind a few existing statements.

- **14.4, quotient maps between quotient rings.** If `g` divides `f` in `Q[X]`, then `h + (f) ↦ h + (g)` is a well-defined surjection `Q[X]/(f) → Q[X]/(g)`, and its kernel is maximal exactly when `Q[X]/(g)` is a field, i.e. when `g` is irreducible.[^7] For even `k` the two parity-sector factors of `char_k` are irreducible, so `Q[x]/(char_k)` is a product of two number fields and each sector projection is a map of this kind ([[chinese-remainder-theorem](pages/chinese-remainder-theorem.md)]).
- **14.7-14.9, factoring over `Z_3`, `Z_5`, `Z_7` by hand.** Divisibility and irreducibility are settled by finding roots and matching coefficients. Two details land close to castles: 14.8 factors `X³ + X + 2` as `(X + 1)(X² − X + 2)` (already over `Z`), and `X² − X + 2` is exactly the quadratic factor of `char_2`; 14.9 shows `X⁴ + aX + 1` is reducible over `F_5` for every `a` (a root when `a ≠ 0`, and `X⁴ + 1 = (X² + 2)(X² + 3)` when `a = 0`).[^8]
- **14.10, a polynomial is not its function.** `X⁵ + X³ + X` and `X⁵ + 2X` are different polynomials over `F_3` that define the same function, because their difference `X³ − X` vanishes at every point of `F_3`.[^9] With 17.13 this identifies the ring of functions `F_p → F_p` with `F_p[x]/(x^p − x)`, whose idempotents are the Lagrange indicators ([[idempotent-decomposition](pages/idempotent-decomposition.md)], [[finite-fields](pages/finite-fields.md)]).
- **14.15-14.16, units and nilpotents of `R[X]`.** Over a commutative ring, `f = a_0 + a_1X + … + a_nX^n` is a unit iff `a_0` is a unit and `a_1, …, a_n` are nilpotent, and `f` is nilpotent iff every coefficient is. So `R[X]` has a unit of positive degree exactly when `R` has a nonzero nilpotent, witnessed by `(1 + aX)(1 − aX + a²X² − …)`.[^10] The same "unit plus nilpotent is a unit" fact builds the `p`-group `1 + (g)/(g^m)` of [[castle-ring-invariant-factors](pages/castle-ring-invariant-factors.md)] §4.
- **14.17-14.18, `R[X]/(X² + 1) ≅ C` but `C[X]/(X² + 1)` is not a domain.** The first is the evaluation map at `i`, the second fails because `X² + 1 = (X + i)(X − i)` has two coprime factors.[^11] For castles: `R[x]/(char_1) ≅ C` by `x ↦ 1 + i`, and over `Q(i)` every odd-`k` `char_k` splits as `g·ḡ` ([[tower-parity-sectors](pages/tower-parity-sectors.md)]), the 14.17 phenomenon.
- **14.11-14.13, 14.19, ideals of `Z[X]`.** `Z[X]/(n, X) ≅ Z_n`, and `(2, X)` is a non-principal ideal of `Z[X]`.[^12] The castle version is the reduction mod 2: `char_k ≡ x^{k+1}` (odd `k`) or `x^k(x + 1)` (even `k`) mod 2, so `(2, x)` is a prime of `Z[x]/(char_k)` containing `x`, and `x` is never a unit mod 2 ([[castle-ring-invariant-factors](pages/castle-ring-invariant-factors.md)] footnote 5).

## Chapter 13 - the exercises used

Chapter 13 (Prime Ideals, Local Rings, exercises pp. 53-57, solutions pp. 159-167) covers prime and maximal ideals, the nilradical, the prime spectrum with its Zariski topology, and local rings. Read against the castle ring it gives the geometric picture on [[castle-ring-spectrum](pages/castle-ring-spectrum.md)]: `Z[x]/(char_k)` as a family of rings over the primes, whose fibers are the mod-`p` factorizations.

- **13.16, primes of `Z[X]` over `p`.** `(n, X)` is prime iff `n` is prime, via `Z[X]/(n, X) ≅ Z_n`.[^13] More generally `(p, g)` is prime when `g` is irreducible mod `p`, so the primes of `Z[x]/(char_k)` over `p` are the distinct irreducible factors of `char_k mod p`.
- **13.18-13.21, `Spec` and the Zariski topology.** Closed sets `V(X)`, basic open sets `U_r = Spec(R) \ V(r)` (empty iff `r` is nilpotent, everything iff `r` is a unit), and the continuous map `Spec(R') → Spec(R)` induced by a ring map.[^14] For castles, the map `Spec Z[x]/(char_k) → Spec Z` has the observatory's factor signatures as fibers.
- **13.11, the nilradical is the set of nilpotents.** The intersection of all prime ideals of a commutative ring is exactly its nilpotent elements.[^15] At a discriminant-zero prime the castle fiber has a nonzero nilradical, and it accounts for exactly the extra `p` in the period: `per = (reduced period) · p^⌈log_p m⌉` in all 7 cases tested ([[castle-ring-spectrum](pages/castle-ring-spectrum.md)] §3).
- **13.23, 13.25-13.26, local rings.** A ring is local iff its non-units form an ideal, and `R/M^n` is local for `M` maximal: for `a ∈ M`, `a + 1` is inverted mod `M^n` by a finite geometric series.[^16] This is the missing reference for the repeated-factor pieces `F_p[x]/(g^m)` of [[castle-ring-invariant-factors](pages/castle-ring-invariant-factors.md)] §4.
- **13.1, 13.6, `Z[i]` and `Z[ω]`.** `(3)` and `(1 + i)` are prime in `Z[i]` but `(2)` is not, and `Z[ω]/(2) ≅ F_4`.[^17] Both are castle rings: `Z[x]/(char_1) ≅ Z[i]`, where the castle prime `(2, x)` is `(1 + i)`, and the `k = 4` minor sector rescaled by `λ = 2μ` is `Z[μ]/(μ² − μ + 1) ≅ Z[ω]`, whose reduction mod 2 is the field `F_4`.

The rest (13.3, 13.7-13.8, 13.10: noncommutative or identity-free counterexamples; 13.14-13.15: ideals of `C[X, Y]`, `Q[X, Y]`; 13.17, 13.22: Boolean rings; 13.24: `Q^(p)`) is not used here.

## Key Takeaways

- The castle ring's CRT split is 17.20 applied to the ideals `(g_i^{m_i})` of `F_p[x]`, which are pairwise comaximal because the `g_i` are distinct irreducibles.[^1]
- Each CRT factor corresponds to an idempotent of `R` (17.19). So `F_p[x]/(char_k)` has exactly `2^r` idempotents, where `r` is the number of distinct irreducible factors of `char_k mod p`. By 17.8 their nonzero product is `0` unless `char_k mod p` is a power of a single irreducible. Worked examples are on [[idempotent-decomposition](pages/idempotent-decomposition.md)].[^2][^3]
- Eisenstein at the prime 2, after rescaling `x = 2y`, proves `char_k` irreducible over `Q` for all `k = 2^m − 1`, and exactly those `k` ([[char-k-eisenstein-at-two](pages/char-k-eisenstein-at-two.md)]).[^4]
- Chapter 14 turns two castle facts into textbook exercises: over `Q`, even-`k` `Q[x]/(char_k)` is a product of two number fields (14.4), and the ring of functions `F_p → F_p` is `F_p[x]/(x^p − x)` with Lagrange idempotents (14.10 with 17.13). Snippets for both are on [[castle-snippets-number-theory](pages/castle-snippets-number-theory.md)].[^7][^9]
- Chapter 13 gives the geometric picture: `Spec Z[x]/(char_k)` over `Spec Z` has the mod-`p` factorizations as fibers, the even-`k` parity sectors as its two components meeting only at `(2, x)`, and nilradicals at discriminant primes that carry exactly the extra `p` in the periods ([[castle-ring-spectrum](pages/castle-ring-spectrum.md)]).[^14][^15]
- `P(1, ·)` lives in the Gaussian integers. The book's `Z[i]` exercises (17.18, and 4.5, 4.11, 15.2 elsewhere) are statements about `Z[x]/(char_1)`.[^6]

## Chapters queued for later ingests

Ch. 12 Semisimple Rings (12.6: `Z_n` is semisimple iff `n` is squarefree); Ch. 5 Characteristics (5.14, 5.16: `X^p − X − a` and `X^{p^n} − a` in characteristic `p`); Ch. 4 Ring Homomorphisms (4.4, 4.8-4.9, and the `Z[√d]` exercises 4.5, 4.11).

## Entities & Concepts

- [[chinese-remainder-theorem](pages/chinese-remainder-theorem.md)] - 17.20.
- [[idempotent-decomposition](pages/idempotent-decomposition.md)] - 17.19, 17.8.
- [[char-k-eisenstein-at-two](pages/char-k-eisenstein-at-two.md)] - 17.21 applied to `char_k`.
- [[castle-ring-spectrum](pages/castle-ring-spectrum.md)] - Chapter 13 applied to `Z[x]/(char_k)`.
- [[finite-fields](pages/finite-fields.md)] - 17.13, 14.10.
- [[castle-snippets-number-theory](pages/castle-snippets-number-theory.md)] - runnable versions of the CRT idempotents, the Lagrange idempotents, the mod-2 shape of `char_k`, and the sector resultant.

## Relation to Other Wiki Pages

This book gives textbook proofs for the ring-theory steps that [[castle-cryptography-ring](pages/castle-cryptography-ring.md)] §4 and [[castle-ring-invariant-factors](pages/castle-ring-invariant-factors.md)] use without proof. It adds idempotents, a computable form of the CRT split, and it corrects [[tower-parity-sectors](pages/tower-parity-sectors.md)]: that page treated odd-`k` irreducibility as settled. It is now proved for `k = 2^m − 1` and only SymPy-verified otherwise. [[castle-cryptography-number-theory](pages/castle-cryptography-number-theory.md)] gets a proof for its `char_1` and `char_3` rows.

## Footnotes

[^1]: [[calugareanu-hamburg-exercises-basic-ring-theory](pages/calugareanu-hamburg-exercises-basic-ring-theory.md)] Ex. 17.20 p.76; solution p.193 [synthesis] - equivalence of pairwise comaximality, solvability of every congruence system, and the canonical map `R/∩I_i → ∏ R/I_i` being an isomorphism; the solution notes the map is always injective and surjective iff the congruences are solvable.
[^2]: [[calugareanu-hamburg-exercises-basic-ring-theory](pages/calugareanu-hamburg-exercises-basic-ring-theory.md)] Ex. 17.19 p.75; solution pp.192-193 [synthesis] - disconnected `Spec(R)` ⇔ `R ≅ U × V` ⇔ an idempotent `e ∉ {0, 1}`; the (c)⇒(b) step uses that `Re` and `R(1 − e)` are comaximal with zero intersection; application to `Z_{p^k}[X]/(X² − X + p^i)`. The `2^r` idempotent count and castle examples are verified on [[idempotent-decomposition](pages/idempotent-decomposition.md)].
[^3]: [[calugareanu-hamburg-exercises-basic-ring-theory](pages/calugareanu-hamburg-exercises-basic-ring-theory.md)] Ex. 17.8 p.74; solution p.190 [synthesis] - nonzero idempotents pair as `e, 1 − e` with `e(1 − e) = 0`, so the product is `1` if `1` is the only nonzero idempotent and `0` otherwise.
[^4]: [[calugareanu-hamburg-exercises-basic-ring-theory](pages/calugareanu-hamburg-exercises-basic-ring-theory.md)] Ex. 17.21 p.76; solution pp.193-194 [synthesis] - Eisenstein over a UFD `R`, irreducibility in `K[X]`, and in `R[X]` for primitive `f`; the proof goes through `R[X]` being a UFD and clears denominators to pass to `K[X]`.
[^5]: [[calugareanu-hamburg-exercises-basic-ring-theory](pages/calugareanu-hamburg-exercises-basic-ring-theory.md)] Ex. 17.13 p.75; solution p.191 [synthesis] - the interpolating polynomial `Σ_{a ∈ K} f(a) ∏_{b ≠ a} (X − b)/(a − b)` agrees with `f` at every `a ∈ K`.
[^6]: [[calugareanu-hamburg-exercises-basic-ring-theory](pages/calugareanu-hamburg-exercises-basic-ring-theory.md)] Ex. 17.18 p.75; solution p.192 [synthesis] - `Z[i]` is Euclidean for the norm, so every class mod `H = (a + bi)` has a representative of norm `< a² + b²`, a finite set. The castle link is by direct check (2026-09-26): `char_1(1 + i) = (1 + i)² − 2(1 + i) + 2 = 0`, and `char_1` is the minimal polynomial of `1 + i`, so `Z[x]/(char_1) ≅ Z[1 + i] = Z[i]`.
[^7]: [[calugareanu-hamburg-exercises-basic-ring-theory](pages/calugareanu-hamburg-exercises-basic-ring-theory.md)] Ex. 14.4 p.60; solution p.169 [synthesis] - for `g | f` in `Q[X]` (the book's example is `f = X⁴ − 4`, `g = X² + 2`), `F(h + (f)) = h + (g)` is well defined and surjective, `(Q[X]/(f))/ker F ≅ Q[X]/(g)`, and the kernel is maximal because `g` is irreducible.
[^8]: [[calugareanu-hamburg-exercises-basic-ring-theory](pages/calugareanu-hamburg-exercises-basic-ring-theory.md)] Exs. 14.7-14.9 p.60; solutions p.170 [synthesis] - `X³ + X² + X + 1 = (X² + 1)(X + 1)` and `X² + 3X + 2 = (X + 2)(X + 1)` (divisible over `Z_5` only); `X² + 1` irreducible over `Z_3`, `(X + 2)(X + 3)` over `Z_5`; `X³ + X + 2 = (X + 1)(X² − X + 2)`; `X⁴ + aX + 1` always reducible over `Z_5`. The `a`-by-`a` factorizations were re-checked with `sp.factor_list(..., modulus=5)` (2026-09-26).
[^9]: [[calugareanu-hamburg-exercises-basic-ring-theory](pages/calugareanu-hamburg-exercises-basic-ring-theory.md)] Ex. 14.10 p.60; solution p.170 [synthesis] - `f = X⁵ + X³ + X` and `g = X⁵ + 2X` agree at `0, 1, 2` in `Z_3`.
[^10]: [[calugareanu-hamburg-exercises-basic-ring-theory](pages/calugareanu-hamburg-exercises-basic-ring-theory.md)] Exs. 14.15-14.16 p.61; solutions pp.171-172 [synthesis] - units of `R[X]` are the polynomials with unit constant term and nilpotent higher coefficients; nilpotents are the polynomials with all coefficients nilpotent; `R` is reduced iff every unit of `R[X]` has degree 0, the converse witnessed by `(1 + a^{n−1}X)(1 − a^{n−1}X) = 1` when `a^n = 0 ≠ a^{n−1}`.
[^11]: [[calugareanu-hamburg-exercises-basic-ring-theory](pages/calugareanu-hamburg-exercises-basic-ring-theory.md)] Exs. 14.17-14.18 p.61; solution p.172 [synthesis] - `C[X]/(X² + 1)` has zero divisors `X ± i`; evaluation at `i` gives `R[X]/(X² + 1) ≅ C`.
[^12]: [[calugareanu-hamburg-exercises-basic-ring-theory](pages/calugareanu-hamburg-exercises-basic-ring-theory.md)] Exs. 14.12-14.13, 14.19 pp.60-61; solutions pp.170-172 [synthesis] - `(n, X)` is principal in `Z[X]` iff `n ∈ {−1, 0, 1}`; the even-constant-term ideal `(2, X)` is not principal; `Z[X]/(n, X) ≅ Z_n` via `a_0 + a_1X + … ↦ a_0 mod n`.
[^13]: [[calugareanu-hamburg-exercises-basic-ring-theory](pages/calugareanu-hamburg-exercises-basic-ring-theory.md)] Ex. 13.16 p.55; solution p.163 [synthesis] - `(n, X)` prime in `Z[X]` iff `n` prime, reduced via `Z[X]/(n, X) ≅ Z_n` (14.19) to `Z_n` being a domain.
[^14]: [[calugareanu-hamburg-exercises-basic-ring-theory](pages/calugareanu-hamburg-exercises-basic-ring-theory.md)] Exs. 13.18-13.21 pp.55-56; solutions pp.163-165 [synthesis] - `V(X)` closed sets and the Zariski topology; `U_r` form a base, `U_r = ∅` iff `r` nilpotent, `U_r = Spec(R)` iff `r` a unit; `f*: Spec(R') → Spec(R)` continuous, a homeomorphism onto `V(ker f)` for surjective `f`.
[^15]: [[calugareanu-hamburg-exercises-basic-ring-theory](pages/calugareanu-hamburg-exercises-basic-ring-theory.md)] Ex. 13.11 p.55; solution p.161 [synthesis] - the prime radical of a commutative ring is its nilradical; a non-nilpotent `a` is avoided by some prime maximal with respect to missing `{a, a², …}`.
[^16]: [[calugareanu-hamburg-exercises-basic-ring-theory](pages/calugareanu-hamburg-exercises-basic-ring-theory.md)] Exs. 13.23, 13.25-13.26 pp.56-57; solutions pp.166-167 [synthesis] - local iff the non-units form an ideal; if `a + 1` is a unit for all `a` in a maximal `M` then `R` is local; `R/M^n` is local via `(a + 1)(1 − a + … + (−1)^{n−1} a^{n−1}) = 1 + (−1)^{n−1} a^n`.
[^17]: [[calugareanu-hamburg-exercises-basic-ring-theory](pages/calugareanu-hamburg-exercises-basic-ring-theory.md)] Exs. 13.1, 13.6 p.54; solutions pp.159-160 [synthesis] - `(3)` and `(1 + i)` prime in `Z[i]`, `(2)` not (`2 = (1 + i)(1 − i)`); `F_4` of characteristic 2 with `x² = x + 1`, `(2)` prime in `Z[ω]`, `Z[ω]/(2) ≅ F_4`.
