---
title: Chinese Remainder Theorem (rings)
category: Concepts
summary: For pairwise comaximal ideals I_1, …, I_n of a ring with identity, R/∩I_i ≅ ∏ R/I_i, equivalently every system r ≡ a_i (mod I_i) has a solution. In F_p[x] it splits the castle ring F_p[x]/(char_k mod p) along the factorization of char_k mod p into fields and local rings, which gives the unit group R^* ≅ ∏ Z/(p^{d_i} − 1) for squarefree char_k mod p, the mod-p period of P(k, ·) as an lcm, and the two CRT steps of Pohlig-Hellman. Over Q it splits Q[x]/(char_k) into the two parity sectors for even k, and the split needs only 1/2. The inverse map is built from orthogonal idempotents.
tags: [concept, ring, chinese-remainder-theorem, comaximal-ideals, quotient-ring, finite-field, castle]
sources: [calugareanu-hamburg-exercises-basic-ring-theory]
created: 2026-09-26
updated: 2026-10-16
---

# Chinese Remainder Theorem (rings)

## Statement

Two ideals `I, J` of a ring `R` with identity are **comaximal** if `I + J = R`, that is, some `a ∈ I` and `b ∈ J` satisfy `a + b = 1`. For finitely many pairwise comaximal ideals `I_1, …, I_n`, the canonical map

```
R / (I_1 ∩ … ∩ I_n)   →   R/I_1 × … × R/I_n ,      r ↦ (r + I_1, …, r + I_n)
```

is a ring isomorphism; equivalently, every system `r ≡ a_i (mod I_i)` has a solution. The map is injective for any ideals, and pairwise comaximality is what makes it surjective.[^1] For `R = Z` and `I_i = (n_i)` this is the integer theorem: `Z → Z/3 × Z/5`, `x ↦ (x mod 3, x mod 5)`, is surjective because `2·3 − 1·5 = 1`, with kernel `15Z`, so `Z/15 ≅ Z/3 × Z/5`.[^2]

**In `F_p[x]`.** Two ideals `(f)` and `(g)` are comaximal exactly when `gcd(f, g) = 1`: `F_p[x]` is a principal ideal domain, and Bézout's identity gives `uf + vg = 1`. For pairwise comaximal ideals the intersection is the product. So if `Q = g_1^{m_1} ⋯ g_r^{m_r}` with the `g_i` distinct monic irreducibles of degrees `d_i`, the ideals `(g_i^{m_i})` are pairwise comaximal and

```
F_p[x]/(Q)   ≅   ∏_i  F_p[x]/(g_i^{m_i}) .
```

A factor with `m_i = 1` is the field `F_{p^{d_i}}` ([[finite-fields](pages/finite-fields.md)]). A factor with `m_i ≥ 2` is a local ring, whose unit group is `F_{p^{d_i}}^*` times a `p`-group of order `p^{d_i(m_i − 1)}` ([[castle-ring-invariant-factors](pages/castle-ring-invariant-factors.md)], section 4).

**The inverse map.** The inverse of the CRT map is `(a_1, …, a_n) ↦ Σ a_i e_i`, where `e_i ≡ 1 (mod I_i)` and `e_i ≡ 0 (mod I_j)` for `j ≠ i`. The `e_i` are **orthogonal idempotents**: `e_i² = e_i`, `e_i e_j = 0` for `i ≠ j`, and `Σ e_i = 1` ([[idempotent-decomposition](pages/idempotent-decomposition.md)]).

**Over `Q` and over `Z[1/2]`.** For even `k`, `char_k = f·g` over `Q`, with `f` and `g` the two parity-sector factors of [[tower-parity-sectors](pages/tower-parity-sectors.md)], both irreducible for even `k ≤ 40` (computed). So `Q[x]/(char_k) ≅ Q[x]/(f) × Q[x]/(g)`, a product of two number fields, and each projection `Q[x]/(char_k) → Q[x]/(f)` is surjective with maximal kernel, since `f` is irreducible.[^3] Over `Z`, `(f)` and `(g)` fail to be comaximal exactly at the primes `p` where `f` and `g` share a factor mod `p`, the primes dividing the resultant `Res(f, g)`. For every even `k ≤ 30`, `Res(f, g) = 2^{k(k+2)/4}` (computed), so the split holds over `Z[1/2]` and survives reduction mod every odd prime.[^4] The idempotent that performs it has only powers of 2 in its denominators, `2^{v_2(k!) + 1}` at most, for every even `k ≤ 40` (computed); at `k = 2` it is `(x² − x + 2)/4`, which is `1` on the sector `x − 2` and `0` on the sector `x² − x + 2`. Over `Z` there is no such idempotent, because the two sectors meet at the prime `(2, x)` ([[castle-ring-spectrum](pages/castle-ring-spectrum.md)], section 5).

## In the castle work

Let `R = F_p[x]/(char_k mod p)`, the ring in which multiplication by `x` is the recurrence of the signed tower count `P(k, ·)` mod `p` ([[castle-cryptography-ring](pages/castle-cryptography-ring.md)], section 3). The theorem enters in four places.

- **Periods.** The period of `P(k, ·) mod p` divides the order of `x` in `R^*`, with equality when `num_k` and `den_k` are coprime mod `p`, as in every case on this page (computed). Under the CRT split the order of `x` is the lcm of the orders of its images in the factors ([[mod-p-observatory](pages/mod-p-observatory.md)], [[castle-ring-invariant-factors](pages/castle-ring-invariant-factors.md)], section 1).
- **Unit groups.** For squarefree `char_k mod p`, `R^* ≅ ∏_i Z/(p^{d_i} − 1)`. A repeated factor gives a local factor whose `p`-group multiplies the period by a power of `p` ([[castle-ring-invariant-factors](pages/castle-ring-invariant-factors.md)], section 4).
- **Pohlig-Hellman.** The attack on the castle Diffie-Hellman uses the theorem twice: once on `R`, and once on the integers, to combine the discrete logarithms found modulo the prime powers dividing the order of `x` ([[castle-cryptography-round-two](pages/castle-cryptography-round-two.md)]).
- **A worked split.** At `p = 101`, `char_2 = (x − 2)(x² − x + 2)` with `x² − x + 2` irreducible (its discriminant `−7` is not a square mod 101), so `R ≅ F_101 × F_{101²}`. The projections are evaluation at `x = 2` and reduction mod `x² − x + 2` ([[castle-cryptography-ring](pages/castle-cryptography-ring.md)], section 4), and the idempotents that invert the split are on [[idempotent-decomposition](pages/idempotent-decomposition.md)].

## Appearances in Sources

- [[calugareanu-hamburg-exercises-basic-ring-theory](pages/calugareanu-hamburg-exercises-basic-ring-theory.md)] - Ex. 17.20, the equivalence of pairwise comaximality, solvability of congruence systems and the product isomorphism; Ex. 4.4, the integer map `Z → Z/3 × Z/5`; Ex. 14.4, quotient maps `Q[X]/(f) → Q[X]/(g)` with maximal kernel.

## Related Concepts

- [[idempotent-decomposition](pages/idempotent-decomposition.md)] - the idempotents that invert the CRT map; a ring is a product of two nonzero rings exactly when it has an idempotent other than `0` and `1`.
- [[castle-ring-invariant-factors](pages/castle-ring-invariant-factors.md)] - the unit group `R^*`, factor by factor, and the order of `x` in it.
- [[castle-cryptography-ring](pages/castle-cryptography-ring.md)] - section 4, the projections of `R` onto its factors, computed.
- [[finite-fields](pages/finite-fields.md)] - the fields `F_{p^d}` that the squarefree factors give.
- [[mod-p-observatory](pages/mod-p-observatory.md)] - the periods of the castle counts mod `p` as lcms over the factors.
- [[castle-cryptography-round-two](pages/castle-cryptography-round-two.md)] - Pohlig-Hellman on the castle Diffie-Hellman.
- [[larger-prime-periodicity](pages/larger-prime-periodicity.md)] - the factorizations of `char_k` at `p = 10⁹ + 7`.
- [[castle-snippets-number-theory](pages/castle-snippets-number-theory.md)] - the snippets `crt_idempotents(Q, p)` and `sector_resultant(k)`.
- [[castle-ring-spectrum](pages/castle-ring-spectrum.md)] - the parity sectors as the components of `Spec Z[x]/(char_k)`, and section 5 on why the sector split needs `1/2`.

## Footnotes

[^1]: [[calugareanu-hamburg-exercises-basic-ring-theory](pages/calugareanu-hamburg-exercises-basic-ring-theory.md)] Ex. 17.20 p.76; solution p.193 [synthesis] - pairwise comaximality ⇔ every congruence system solvable ⇔ `R/∩I_i → ∏ R/I_i` an isomorphism; the map is injective by construction and surjective iff the congruences are solvable.
[^2]: [[calugareanu-hamburg-exercises-basic-ring-theory](pages/calugareanu-hamburg-exercises-basic-ring-theory.md)] Ex. 4.4 p.20; solutions pp.107-108 [synthesis] - surjectivity from `2·3 − 1·5 = 1`, kernel `3Z ∩ 5Z = 15Z`; generalized to coprime moduli.
[^3]: [[calugareanu-hamburg-exercises-basic-ring-theory](pages/calugareanu-hamburg-exercises-basic-ring-theory.md)] Ex. 14.4 p.60; solution p.169 [synthesis] - for `g | f` in `Q[X]` the map `Q[X]/(f) → Q[X]/(g)` is a well-defined surjective ring homomorphism, with maximal kernel when `g` is irreducible.
[^4]: Verified by execution (Python 3.11 with SymPy, 2026-10-16): for the two factors `f, g` of `char_k` returned by `sp.factor_list`, `|Res(f, g)| = 2^{k(k+2)/4}` for every even `k` from 2 to 30; `char_k` has exactly two irreducible factors over `Q` for every even `k ≤ 40`; the sector idempotent `g·(g^{−1} mod f) mod char_k` has coefficient denominators that are powers of 2, the largest `2^{v_2(k!) + 1}`, for every even `k ≤ 40`; `num_k` and `den_k` are coprime mod `p` for the pairs `(k, p)` used on this page and on [[castle-ring-invariant-factors](pages/castle-ring-invariant-factors.md)].
