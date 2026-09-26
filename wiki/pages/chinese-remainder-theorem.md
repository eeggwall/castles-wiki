---
title: Chinese Remainder Theorem (rings)
category: Concepts
summary: For pairwise comaximal ideals I_1..I_n, R/∩I_i ≅ ∏ R/I_i, equivalently every congruence system r ≡ a_i mod I_i has a solution. For the castle ring it splits F_p[x]/(char_k) along the factorization char_k = ∏ g_i^{m_i} mod p into fields and local rings. It underlies the mod-p period as an lcm, the unit group R^* ≅ ∏ Z/(p^{d_i} − 1), and Pohlig-Hellman. The inverse map is built from idempotents.
tags: [concept, ring, chinese-remainder-theorem, comaximal-ideals, quotient-ring, finite-field, castle]
sources: [calugareanu-hamburg-exercises-basic-ring-theory]
created: 2026-09-26
updated: 2026-09-26
---

# Chinese Remainder Theorem (rings)

## Description

Two ideals `I, J` of a ring `R` with identity are **comaximal** if `I + J = R`, that is, some `a ∈ I` and `b ∈ J` satisfy `a + b = 1`. For finitely many ideals `I_1, …, I_n` that are pairwise comaximal, the canonical map

```
R / (I_1 ∩ … ∩ I_n)   →   R/I_1 × … × R/I_n ,      r ↦ (r + I_1, …, r + I_n)
```

is a ring isomorphism. Equivalently, every system `r ≡ a_i (mod I_i)` has a solution. The map is always injective; comaximality is exactly what makes it surjective.[^1] For `R = Z` and `I_i = (n_i)` this is the integer CRT from number theory: for example `Z → Z_3 × Z_5`, `x ↦ (x mod 3, x mod 5)`, is surjective with kernel `15Z`, so `Z/15 ≅ Z_3 × Z_5`.[^2]

**In `F_p[x]`.** Two ideals `(f), (g)` are comaximal iff `gcd(f, g) = 1`, because `F_p[x]` is a principal ideal domain and Bézout gives `uf + vg = 1`. For comaximal ideals `∩ = ∏`. So if `Q = g_1^{m_1} ⋯ g_r^{m_r}` with the `g_i` distinct irreducibles, the ideals `(g_i^{m_i})` are pairwise comaximal and

```
F_p[x]/(Q)   ≅   ∏_i  F_p[x]/(g_i^{m_i}) .
```

Each factor with `m_i = 1` is the field `F_{p^{d_i}}` ([[finite-fields](pages/finite-fields.md)]). Each factor with `m_i ≥ 2` is a local ring whose unit group is `F_{p^{d_i}}^*` times a `p`-group ([[castle-ring-invariant-factors](pages/castle-ring-invariant-factors.md)] §4).

**Going backwards.** A CRT isomorphism is only useful computationally if you can invert it. The inverse is a sum `r = Σ a_i e_i`, where `e_i` is the element with `e_i ≡ 1 (mod I_i)` and `e_i ≡ 0 (mod I_j)` for `j ≠ i`. These `e_i` are the **orthogonal idempotents** of the splitting: `e_i² = e_i`, `e_i e_j = 0`, `Σ e_i = 1`. They are the subject of [[idempotent-decomposition](pages/idempotent-decomposition.md)].

**Over `Q`, and over `Z[1/2]`.** CRT works before reducing mod `p` too. For even `k`, `char_k = f·g` with `f, g` the two parity-sector factors, both irreducible over `Q` ([[tower-parity-sectors](pages/tower-parity-sectors.md)]). Then `Q[x]/(char_k) ≅ Q[x]/(f) × Q[x]/(g)`, a product of two number fields, and each projection is a surjection `Q[x]/(char_k) → Q[x]/(f)` whose kernel is maximal because `f` is irreducible.[^3] Over the integers the split is obstructed only where `f` and `g` can share a root, measured by the resultant `Res(f, g)`: it equals `2^{k(k+2)/4}` for every even `k ≤ 30`, so the sector split holds over `Z[1/2]` and survives reduction mod every odd prime (unproved in general; filed in IDEAS).[^4] Concretely, the idempotent that performs the split has coefficients with pure powers of 2 in the denominators: `(x² − x + 2)/4` at `k = 2`, and `2^{v_2(k!) + 1}` in general (every even `k ≤ 40`). Over `Z` itself there is no such idempotent, because the two sectors meet at `(2, x)` ([[castle-ring-spectrum](pages/castle-ring-spectrum.md)] §5).

## In the castle work

`R = F_p[x]/(char_k mod p)` is the ring in which the signed tower count `P(k, ·)` runs mod `p` ([[castle-cryptography-ring](pages/castle-cryptography-ring.md)] §3). Everything the wiki does with it goes through CRT:

- **Periods.** The mod-`p` period of `P(k, ·)` is `ord(x)` in `R^*`, and under CRT that is the `lcm` of the orders of `x`'s images in each factor ([[mod-p-observatory](pages/mod-p-observatory.md)], [[castle-ring-invariant-factors](pages/castle-ring-invariant-factors.md)] §1).
- **Unit groups.** For squarefree `Q`, `R^* ≅ ∏ Z/(p^{d_i} − 1)`. With a repeated factor, the corresponding CRT factor is local and adds a `p`-group, which is the extra `p` in the observatory's periods ([[castle-ring-invariant-factors](pages/castle-ring-invariant-factors.md)] §4).
- **Attacks.** Pohlig-Hellman on the castle Diffie-Hellman uses CRT twice: once on the ring `R` and once on the integers when combining the discrete logs from each prime-power part ([[castle-cryptography-round-two](pages/castle-cryptography-round-two.md)]).
- **Worked split.** At `p = 101`, `char_2 = (x − 2)(x² − x + 2)` and `R ≅ F_101 × F_{101²}`. The projections are "evaluate at `x = 2`" and "reduce mod `x² − x + 2`" ([[castle-cryptography-ring](pages/castle-cryptography-ring.md)] §4). The explicit idempotents that invert this split are computed on [[idempotent-decomposition](pages/idempotent-decomposition.md)].

## Appearances in Sources

- [[calugareanu-hamburg-exercises-basic-ring-theory](pages/calugareanu-hamburg-exercises-basic-ring-theory.md)] - Ex. 17.20, CRT as the equivalence of comaximality, solvability of congruences, and the product isomorphism; Ex. 14.4, quotient maps `Q[X]/(f) → Q[X]/(g)` with maximal kernel.

## Related Concepts

- [[idempotent-decomposition](pages/idempotent-decomposition.md)] - the inverse of the CRT map; a ring splits as a product exactly when it has a nontrivial idempotent.
- [[castle-ring-invariant-factors](pages/castle-ring-invariant-factors.md)] - CRT applied to `R^*`, factor by factor.
- [[castle-cryptography-ring](pages/castle-cryptography-ring.md)] - §4, the computable projections.
- [[finite-fields](pages/finite-fields.md)] - what the squarefree factors are.
- [[mod-p-observatory](pages/mod-p-observatory.md)] - periods as `lcm` over CRT factors.
- [[castle-cryptography-round-two](pages/castle-cryptography-round-two.md)] - Pohlig-Hellman, CRT on the exponent side.
- [[larger-prime-periodicity](pages/larger-prime-periodicity.md)] - the same split at `p = 10⁹ + 7`.
- [[castle-snippets-number-theory](pages/castle-snippets-number-theory.md)] - `crt_idempotents(Q, p)` and `sector_resultant(k)`, runnable and pinned.
- [[castle-ring-spectrum](pages/castle-ring-spectrum.md)] - the sectors as components of `Spec Z[x]/(char_k)`; §5 on why the sector split needs the `1/2`.

## Footnotes

[^1]: [[calugareanu-hamburg-exercises-basic-ring-theory](pages/calugareanu-hamburg-exercises-basic-ring-theory.md)] Ex. 17.20 p.76; solution p.193 [synthesis] - pairwise comaximality ⇔ every congruence system solvable ⇔ `R/∩I_i → ∏ R/I_i` an isomorphism; the map is injective by construction and surjective iff the congruences are solvable.
[^2]: [[calugareanu-hamburg-exercises-basic-ring-theory](pages/calugareanu-hamburg-exercises-basic-ring-theory.md)] Ex. 4.4 p.20; solutions pp.107-108 [synthesis] - surjectivity from `2·3 − 1·5 = 1`, kernel `3Z ∩ 5Z = 15Z`; generalized to coprime moduli.
[^3]: [[calugareanu-hamburg-exercises-basic-ring-theory](pages/calugareanu-hamburg-exercises-basic-ring-theory.md)] Ex. 14.4 p.60; solution p.169 [synthesis] - for `g | f` in `Q[X]` the map `Q[X]/(f) → Q[X]/(g)` is a well-defined surjective ring homomorphism with maximal kernel when `g` is irreducible.
[^4]: Verified by execution (Python 3.10, SymPy, 2026-09-26): `sp.resultant(f, g, x) == 2**(k*(k+2)//4)` for the two `sp.factor_list` factors of `char_k`, every even `k` from 2 to 30; values for `k ≤ 12` pinned under `sector_resultant` on [[castle-snippets-number-theory](pages/castle-snippets-number-theory.md)].
