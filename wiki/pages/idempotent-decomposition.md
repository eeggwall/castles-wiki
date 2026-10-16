---
title: Idempotent decomposition
category: Concepts
summary: An idempotent e (e² = e) other than 0 and 1 splits a commutative ring R as Re × R(1 − e), and every splitting into two nonzero factors arises this way. In the castle ring F_p[x]/(char_k), with r distinct irreducible factors of char_k mod p, the idempotents are the 2^r sums of the primitive idempotents e_i, one per factor; e_i picks out the part of the recurrence of P(k, ·) that comes from the roots of its factor, and a repeated factor adds nilpotents, not idempotents (brute force on eight (k, p)). At k = 2, p = 101, e_1 = (x² − x + 2)/4 isolates the root 2, the +1 parity sector, and x^L e_1 = 2^L e_1. r is the dimension of the fixed space of Frobenius. For odd k ≤ 31 and even k ≤ 30 no fiber idempotent other than 0 and 1 lifts to Z[x]/(char_k); for even k ≤ 40 the sector idempotent lies in Z[1/2][x]/(char_k), with denominator 2^{v_2(k!)+1}.
tags: [concept, ring, idempotent, chinese-remainder-theorem, quotient-ring, finite-field, eigenvalue, projection, castle]
sources: [calugareanu-hamburg-exercises-basic-ring-theory]
created: 2026-09-26
updated: 2026-10-16
---

# Idempotent decomposition

An element `e` of a ring is **idempotent** if `e² = e`; `0` and `1` always are. This page splits the castle ring `F_p[x]/(char_k)`, in which multiplication by `x` is one step of the recurrence of the signed tower count `P(k, ·)` ([[castle-cryptography-ring](pages/castle-cryptography-ring.md)], section 3), into its factors by idempotents, and determines which of them come from idempotents of `Z[x]/(char_k)`.

## Idempotents and splittings

In a commutative ring `R` with identity, if `e` is idempotent then so is `1 − e`, and `e(1 − e) = 0`. The ideals `Re` and `R(1 − e)` are comaximal, since `e + (1 − e) = 1`, and meet only in `0`: if `a = re = s(1 − e)`, then `a = ae = s(1 − e)e = 0`. So by the [[chinese-remainder-theorem](pages/chinese-remainder-theorem.md)]

```
R  ≅  R/R(1 − e)  ×  R/Re  ≅  Re × R(1 − e),       r ↦ (re, r(1 − e)).
```

Conversely, if `R ≅ U × V` with both factors nonzero, `(1, 0)` is an idempotent other than `0` and `1`. So a commutative ring is a product of two nonzero rings exactly when it has an idempotent other than `0` and `1`. Călugăreanu and Hamburg add a third equivalent condition: the prime spectrum `Spec(R)` is disconnected.[^1]

An idempotent `e ≠ 0` is **primitive** if it is not a sum `e = u + v` of two nonzero idempotents with `uv = 0`.[^2] A finite commutative ring is the product of the rings `Re_i` over its primitive idempotents `e_1, …, e_r`, which are orthogonal (`e_i e_j = 0` for `i ≠ j`) and sum to `1`. Every idempotent is the sum of a subset of them, so there are exactly `2^r`. Pairing each `e` with `1 − e` shows that the product of all the nonzero idempotents is `1` when `r = 1`, where `1` is the only one, and `0` when `r ≥ 2`.[^3]

## In the castle ring

Take `R = F_p[x]/(Q)` with `Q = char_k mod p = ∏_{i=1}^{r} g_i^{m_i}`, the `g_i` distinct monic irreducible polynomials over `F_p`. By the Chinese remainder theorem `R ≅ ∏_i F_p[x]/(g_i^{m_i})`. Each factor is a local ring, a field when `m_i = 1`, and a local ring has no idempotents other than `0` and `1`: of `e` and `1 − e`, which sum to `1`, one is a unit, and `e(1 − e) = 0` then forces the other to be `0`. Therefore:

- `R` has exactly `2^r` idempotents, with `r` the number of distinct irreducible factors of `char_k mod p`. A repeated factor adds nilpotents, not idempotents.
- The primitive idempotent `e_i` is `1` in the factor of `g_i` and `0` in the others: `e_i = N_i · (N_i^{−1} mod g_i^{m_i})` with `N_i = Q/g_i^{m_i}`.
- Every sequence mod `p` satisfying the recurrence of `char_k` is `s_L = ℓ(x^L)` for an `F_p`-linear map `ℓ : R → F_p`, and `s_L = Σ_i ℓ(x^L e_i)` splits it into one sequence per factor, the `i`-th satisfying the recurrence of `g_i^{m_i}`. For a linear factor `g_i = x − λ`, `x^L e_i = Σ_{j < m_i} C(L, j) λ^{L−j} (x − λ)^j e_i`, since `x = λ + (x − λ)` and `(x − λ)^{m_i} e_i = 0`; when `m_i = 1` this is `x^L e_i = λ^L e_i`.

**Worked example: `k = 2`, `p = 101`.** Here `char_2 = (x − 2)(x² − x + 2)`, `r = 2`, and `R` has the four idempotents `0, e_1, e_2, 1`:[^exec]

```
e_1  =  (x² − x + 2) / 4  =  76x² + 25x + 51      (1 at x = 2;  0 mod x² − x + 2)
e_2  =  1 − e_1           =  25x² − 25x + 51      (0 at x = 2;  1 mod x² − x + 2)
e_1 + e_2 = 1,    e_1 · e_2 = 0 (mod char_2, p = 101)
```

`e_1` is the other factor `x² − x + 2` divided by its value 4 at the root `2`, with `4^{−1} = 76 (mod 101)`. Since `x · (x² − x + 2) = char_2 + 2 · (x² − x + 2)`, `x e_1 = 2 e_1` and `x^L e_1 = 2^L e_1`. So `e_1` isolates the root `2` of `char_2`, its root of largest modulus. This is the `+1` sector of [[tower-parity-sectors](pages/tower-parity-sectors.md)], the signed count of the towers whose last column has even height; at `k = 2` that count is `2^L`, since it satisfies the recurrence of the sector polynomial `x − 2` and equals `1` at `L = 0`. `e_2` isolates the roots `(1 ± √−7)/2` of `x² − x + 2`, which lie in `F_{101²}` because `101 ≡ 3 (mod 7)` and so `−7` is not a square mod 101. The CRT projections `R → F_101 × F_{101²}` of [[castle-cryptography-ring](pages/castle-cryptography-ring.md)] (section 4) are inverted by `(a_1, a_2) ↦ a_1 e_1 + a_2 e_2`.

**Brute-force check.** The table counts the idempotents of `F_p[x]/(char_k)` among all `p^{k+1}` elements, and gives the product of the nonzero ones:[^exec]

| `k` | `p` | factors (degree, multiplicity) | idempotents | `2^r` | product of nonzero idempotents |
|---|---|---|---|---|---|
| 1 | 3 | (2,1) | 2 | 2 | 1 |
| 1 | 5 | (1,1), (1,1) | 4 | 4 | 0 |
| 2 | 3 | (1,1), (2,1) | 4 | 4 | 0 |
| 2 | 5 | (1,1), (2,1) | 4 | 4 | 0 |
| 2 | 7 | (1,1), (1,**2**) | 4 | 4 | 0 |
| 3 | 3 | (4,1) | 2 | 2 | 1 |
| 3 | 5 | (1,**2**), (2,1) | 4 | 4 | 0 |
| 4 | 3 | (1,**2**), (3,1) | 4 | 4 | 0 |

The rows `char_2 mod 7`, `char_3 mod 5` and `char_4 mod 3` have a repeated factor, at a prime dividing `disc(char_k)` ([[castle-ring-invariant-factors](pages/castle-ring-invariant-factors.md)], section 4), and still have `2^r` idempotents. The multiplicity enlarges the nilradical and the `p`-group of units of the local factor, and leaves the idempotents unchanged. In the rows `char_1 mod 3` and `char_3 mod 3`, `char_k` is irreducible and `R` is a field, with only the idempotents `0` and `1`, so the product of the nonzero idempotents is `1`.

## Finding the idempotents without factoring

On `R = F_p[x]/(char_k mod p)` the Frobenius map `a ↦ a^p` is `F_p`-linear. Its fixed space `{a : a^p = a}` is the span of the primitive idempotents, one copy of `F_p` per distinct irreducible factor, so it has dimension `r` whatever the multiplicities ([[castle-ring-spectrum](pages/castle-ring-spectrum.md)], section 6, where the Proposition is proved and checked on twelve fibers).[^4] So `r`, and with it the number `2^r` of idempotents, is the nullity of the `(k + 1) × (k + 1)` matrix of Frobenius minus the identity, and needs no factorization of `char_k`; this is the first step of Berlekamp's factoring algorithm. The fixed space has dimension `r` at every `(k, p)` of the table and at `k = 2`, `p = 101` (computed).[^exec] `frobenius_profile(k, p)` on [[castle-snippets-number-theory](pages/castle-snippets-number-theory.md)] computes the rank and the fixed-space dimension.

## Lifting to the integers

Write `A_k = Z[x]/(char_k)`. Reducing coefficients mod `p` maps `A_k` onto the fiber `F_p[x]/(char_k)`, and an idempotent `ē` of the fiber **lifts** if some `e ∈ A_k` with `e² = e` reduces to `ē`.

For odd `k ≤ 31` and even `k ≤ 30`, `A_k` has only the idempotents `0` and `1` ([[castle-ring-spectrum](pages/castle-ring-spectrum.md)], section 5). For odd `k` it is an integral domain, since `char_k` is irreducible; for even `k` its spectrum is connected, because the two parity-sector components meet at the prime `(2, x)`. So for these `k` no fiber idempotent other than `0` and `1` lifts, at any odd prime `p`. In `Z/10` the same happens: `5² = 25 ≡ 5 (mod 10)` splits `Z/10 ≅ Z/2 × Z/5`, and no integer other than `0` and `1` squares to itself.[^5] Multiplication by 5 preserves sums and products but sends `1` to `5`; it is the projection of `Z/10` onto its factor `5Z/10 ≅ Z/2`. The maps `Z/10 → Z/10` that preserve sums and products are exactly the multiplications by the four idempotents `0, 1, 5, 6` (computed).[^6]

For even `k`, `Q[x]/(char_k)` is the product of the rings of the two parity-sector factors of `char_k`, and its idempotent `e` that is `1` on the `+1` sector and `0` on the other has only powers of 2 in its denominators. The largest is `2^{v_2(k!) + 1}` for every even `k ≤ 40` ([[castle-ring-spectrum](pages/castle-ring-spectrum.md)], section 5; recomputed).[^exec] At `k = 2`, `e = (x² − x + 2)/4`, which reduces mod 101 to the `e_1` of the worked example. So `e` lies in `A_k[1/2]` and reduces to an idempotent of every fiber over an odd prime, while `A_k` has no idempotent other than `0` and `1`.

Within one fiber, reduction from `R` to the reduced fiber `R/N(R) = F_p[x]/(∏ g_i)`, with `N(R)` the nilradical, is a bijection on idempotents: both rings have `2^r` of them, and `e_i` reduces to the primitive idempotent of `g_i`.

## The ring of functions on F_p

Over `F_p` two different polynomials can define the same function (`x^5 + x^3 + x` and `x^5 + 2x` agree at every point of `F_3`), and every function `F_p → F_p` is given by a polynomial, so the ring of functions `F_p → F_p` is `F_p[x]/(x^p − x)`.[^7] Since `x^p − x = ∏_{a ∈ F_p} (x − a)` has `p` distinct linear factors, the Chinese remainder theorem splits this ring as `F_p^p`, and its `p` primitive idempotents are the indicator polynomials

```
δ_a(x)  =  1 − (x − a)^{p−1},        δ_a(b) = 1 if b = a, else 0      (Fermat: (b − a)^{p−1} = 1 for b ≠ a).
```

They are orthogonal and sum to `1` mod `x^p − x` (checked for `p = 3, 5, 7`).[^exec] When `char_k mod p` is a product of distinct linear factors `x − λ_i`, the primitive idempotents of `F_p[x]/(char_k)` are the Lagrange polynomials `e_i = ∏_{j ≠ i} (x − λ_j)/(λ_i − λ_j)`, which is `N_i/N_i(λ_i)` with `N_i = ∏_{j ≠ i} (x − λ_j)`; the `e_1` of the worked example is `N_1/N_1(2)` with the other factor `N_1 = x² − x + 2` irreducible. `crt_idempotents(Q, p)` and `lagrange_idempotents(p)` on [[castle-snippets-number-theory](pages/castle-snippets-number-theory.md)] compute both.

The roots-of-unity filter of [[parity-via-roots-of-unity](pages/parity-via-roots-of-unity.md)] is the complex counterpart. With `ω = e^{2πi/m}`, the polynomial `t^m − 1` has the `m` distinct roots `ω^j`, so `C[t]/(t^m − 1) ≅ C^m`, with primitive idempotents

```
ε_j  =  (1/m) Σ_{b=0}^{m−1} ω^{−jb} t^b,        ε_j(ω^i)  =  [i = j],        t ε_j  =  ω^j ε_j.
```

The value `ε_j(ω^i) = [i = j]` is the orthogonality relation `(1/m) Σ_b ω^{b(i − j)} = [i ≡ j (mod m)]` with which that page counts towers by block count mod `m` (checked for `m = 3, 4, 5`).[^exec]

## Appearances in Sources

- [[calugareanu-hamburg-exercises-basic-ring-theory](pages/calugareanu-hamburg-exercises-basic-ring-theory.md)] - Ex. 17.19 (splitting ⇔ idempotent ⇔ disconnected spectrum), Ex. 17.8 (product of nonzero idempotents), Ex. 17.10 (the definition of primitive idempotent in the chapter preamble), Ex. 14.10 with 17.13 (functions on `F_p` as `F_p[x]/(x^p − x)`).

## Related Concepts

- [[chinese-remainder-theorem](pages/chinese-remainder-theorem.md)] - the splitting of `F_p[x]/(char_k)` into the rings `F_p[x]/(g_i^{m_i})`, whose inverse is `(a_i) ↦ Σ a_i e_i`.
- [[castle-cryptography-ring](pages/castle-cryptography-ring.md)] - the ring `F_p[x]/(char_k)` (section 3) and its CRT projections at `k = 2`, `p = 101`, inverted by `e_1` and `e_2` (section 4).
- [[castle-ring-invariant-factors](pages/castle-ring-invariant-factors.md)] - the unit groups of the local factors; a repeated factor adds a `p`-group of units and no idempotents.
- [[tower-parity-sectors](pages/tower-parity-sectors.md)] - the two sector factors of `char_k` for even `k`; at `k = 2` the `+1` sector is the root `2` that `e_1` isolates.
- [[parity-via-roots-of-unity](pages/parity-via-roots-of-unity.md)] - the roots-of-unity filter, whose orthogonality relation gives the idempotents `ε_j` of `C[t]/(t^m − 1)`.
- [[finite-fields](pages/finite-fields.md)] - the field factors `F_p[x]/(g_i) ≅ F_{p^{d_i}}`.
- [[castle-snippets-number-theory](pages/castle-snippets-number-theory.md)] - `crt_idempotents(Q, p)`, `lagrange_idempotents(p)` and `frobenius_profile(k, p)`, with their outputs.
- [[castle-ring-spectrum](pages/castle-ring-spectrum.md)] - section 5: `A_k` has only the idempotents `0` and `1`, and the sector idempotent has denominator `2^{v_2(k!) + 1}`; section 6: the fixed space of Frobenius has dimension `r`.

## Footnotes

[^1]: [[calugareanu-hamburg-exercises-basic-ring-theory](pages/calugareanu-hamburg-exercises-basic-ring-theory.md)] Ex. 17.19 p.75; solution pp.192-193 [synthesis] - disconnected `Spec(R)` ⇔ `R ≅ U × V` with nonzero factors ⇔ an idempotent `e ∉ {0, 1}`; from `e`, `Re` and `R(1 − e)` are comaximal proper ideals with zero intersection, giving `R ≅ R/Re × R/R(1 − e)`.
[^2]: [[calugareanu-hamburg-exercises-basic-ring-theory](pages/calugareanu-hamburg-exercises-basic-ring-theory.md)] Ch. 17 preamble p.73 and Ex. 17.10 p.74 [synthesis] - a nonzero idempotent is primitive if it is not the sum of two orthogonal idempotents; 17.10 characterizes this as `eRe` having no idempotents besides `0` and `e`.
[^3]: [[calugareanu-hamburg-exercises-basic-ring-theory](pages/calugareanu-hamburg-exercises-basic-ring-theory.md)] Ex. 17.8 p.74; solution p.190 [synthesis] - in a finite commutative ring with `1 ≠ 0`, nonzero idempotents pair as `e, 1 − e` with `e(1 − e) = 0`, so their product is `1` if `1` is the only one and `0` otherwise.
[^4]: [[calugareanu-hamburg-exercises-basic-ring-theory](pages/calugareanu-hamburg-exercises-basic-ring-theory.md)] Ex. 5.16 p.25; solution p.113 [synthesis] - the Artin-Schreier map `a ↦ a^p − a` has kernel `F_p` on a field, which is why its kernel on a product of fields and local rings is one `F_p` per factor; the castle check is in [[castle-ring-spectrum](pages/castle-ring-spectrum.md)], section 6.
[^5]: [[calugareanu-hamburg-exercises-basic-ring-theory](pages/calugareanu-hamburg-exercises-basic-ring-theory.md)] Ex. 12.19 p.51; solution p.158 [synthesis] - the book's example of idempotents that do not lift: `R = {m/n : gcd(6, n) = 1}` has only `0, 1`, while `R/6R ≅ Z_2 × Z_3` has the idempotent `3`. The `Z/10` example is the same phenomenon for `Z`.
[^6]: [[calugareanu-hamburg-exercises-basic-ring-theory](pages/calugareanu-hamburg-exercises-basic-ring-theory.md)] Ex. 4.8 p.20; solutions pp.108-109 [synthesis] - the ring endomorphisms of `Z_n` are the translations `x ↦ e·x` by the idempotents `e` of `Z_n`.
[^7]: [[calugareanu-hamburg-exercises-basic-ring-theory](pages/calugareanu-hamburg-exercises-basic-ring-theory.md)] Ex. 14.10 p.60; solution p.170, with Ex. 17.13 p.75; solution p.191 [synthesis] - `X⁵ + X³ + X` and `X⁵ + 2X` induce the same function on `Z_3`; every function on a finite field is given by the Lagrange interpolation polynomial. The kernel of polynomials → functions is `(x^p − x)` because a polynomial vanishing on all of `F_p` is divisible by `∏ (x − a) = x^p − x`.
[^exec]: Verified by execution (Python 3.11 with SymPy, 2026-10-16). (i) `char_2 mod 101 = (x − 2)(x² − x + 2)`; `e_1 = 76x² + 25x + 51` and `e_2 = 25x² − 25x + 51` satisfy `e² ≡ e`, `e_1 + e_2 ≡ 1`, `e_1 e_2 ≡ 0` and `x e_1 ≡ 2 e_1` mod `(char_2, 101)`, and `76 (x² − x + 2) ≡ e_1`. (ii) For each `(k, p)` of the table, all `p^{k+1}` residues `e` tested for `e² ≡ e mod char_k`; the count equals `2^r` with `r` the number of distinct factors from `sp.factor_list`, and the products of the nonzero idempotents are as shown. (iii) The nullity of Frobenius minus the identity over `F_p` equals `r` for the eight table cases and `(2, 101)`. (iv) For each even `k ≤ 40`, `char_k` factored over `Q` into two irreducible factors, the sector idempotent computed by the extended Euclidean algorithm, and the lcm of its coefficient denominators equal to `2^{v_2(k!) + 1}`; the signed count of the towers of height at most 2 with last column of even height is `2^L` for `L ≤ 6` by enumeration. (v) The maps `a ↦ ca` of `Z/10` preserving products are `c = 0, 1, 5, 6`. (vi) For `p = 3, 5, 7`, `δ_a² ≡ δ_a`, `δ_a δ_b ≡ 0` (`a ≠ b`) and `Σ δ_a ≡ 1` mod `x^p − x`; `x^5 + x^3 + x − (x^5 + 2x) ≡ 0 mod x^3 − x` over `F_3`. (vii) `(1/m) Σ_b ω^{b(i − j)} = [i = j]` for `m = 3, 4, 5`.
