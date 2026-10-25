---
title: The castle ring's spectrum - Spec Z[x]/(char_k) over Spec Z
category: Analyses
summary: The ring A_k = Z[x]/(char_k) as a family of rings over the primes. Its fiber over p is F_p[x]/(char_k mod p), whose points are the distinct irreducible factors of char_k mod p, and its fiber over Q has one point for odd k and two for even k, the parity sectors, which are the irreducible components. For every even k ≤ 30 the components meet at exactly one point, (2, x). At a prime dividing disc(char_k) the fiber has nilpotents, and the period of P(k, ·) mod p is the period in the reduced fiber times p^⌈log_p m⌉ at all seven such primes p < 200 with k ≤ 8. A fiber is semisimple exactly when char_k mod p is squarefree; A_k has no idempotents other than 0 and 1, the sector idempotent has denominator 2^(v_2(k!)+1) for every even k ≤ 40, and x is inverted only with 1/2^k. Frobenius on a fiber has rank Σ d_i ⌈m_i/p⌉ and a fixed space of dimension equal to the number of points. For k = 1, A_1 = Z[i]; the k = 4 minor sector gives Z[√−3], which rescaling by 2 turns into Z[ω].
tags: [analysis, castle, ring, spectrum, prime-ideal, nilradical, local-ring, finite-field, parity-sector, resultant, period, gaussian-integers, eisenstein-integers, sympy, verification]
sources: [calugareanu-hamburg-exercises-basic-ring-theory, oeis-mining-pe502]
created: 2026-09-26
updated: 2026-10-25
---

# The castle ring's spectrum - `Spec Z[x]/(char_k)` over `Spec Z`

## The picture

[[mod-p-observatory](pages/mod-p-observatory.md)] and [[larger-prime-periodicity](pages/larger-prime-periodicity.md)] factor `char_k mod p` one prime at a time, [[castle-ring-invariant-factors](pages/castle-ring-invariant-factors.md)] reads off the unit groups, and [[tower-parity-sectors](pages/tower-parity-sectors.md)] splits `char_k` over `Q`. All of these are statements about one ring, `A_k = Z[x]/(char_k)`, with `char_k` the characteristic polynomial of the signed tower count `P(k, ·)`, and about its set `Spec A_k` of prime ideals.

**Points and what they lie over.** A *point* of `Spec A_k` is a prime ideal `P` of `A_k`. Its intersection `P ∩ Z` is a prime ideal of `Z`: `(0)`, if `P` contains no nonzero integer, or `(p)` for the one prime `p` that `P` contains. `P` **lies over** `(0)` or over `(p)`. This is the map `Spec A_k → Spec Z`, `P ↦ P ∩ Z`, induced by the inclusion `Z → A_k`.[^1]

**Fibers.** The **fiber over `(p)`** is the set of points of `Spec A_k` lying over `(p)`. The primes of `A_k` that contain `p` correspond to the primes of `A_k/pA_k = F_p[x]/(char_k mod p)`. The fiber over `(0)` is computed with `Q` in place of `F_p`: its points are the primes of `Q[x]/(char_k)`. Each fiber is a finite set of points:

```
fiber over (0):  primes of Q[x]/(char_k)      =  the irreducible factors of char_k over Q
fiber over (p):  primes of F_p[x]/(char_k)    =  the distinct irreducible factors of char_k mod p
```

The second line is the statement that `(p, g)` is a prime of `Z[x]` exactly when `g` is irreducible mod `p`; the case `g = X` is exercise 13.16 of Călugăreanu and Hamburg, `(n, X)` prime iff `n` is prime.[^2] A fiber's **ring** `F_p[x]/(char_k mod p)` carries more than its set of points: when `char_k mod p` has a repeated factor, the ring has nonzero nilpotents that the point set does not see. Such a fiber is **fat** (section 3).

## 1. The fibers are the mod-`p` factorizations

Over an odd prime `p`, the fiber has one point for each distinct irreducible factor `g_i` of `char_k mod p`, and the point's residue field is `F_{p^{d_i}}`, `d_i = deg g_i`. For example `char_2 ≡ (x − 2)(x² − x + 2) (mod 101)` gives two points, with residue fields `F_101` and `F_{101²}`. The splitting of the fiber ring by the [[chinese-remainder-theorem](pages/chinese-remainder-theorem.md)] is the splitting into the local rings at the points, and the `2^r` idempotents of [[idempotent-decomposition](pages/idempotent-decomposition.md)] are `2^{(number of points)}`: a commutative ring is a product of two nonzero rings exactly when its spectrum is disconnected, exactly when it has an idempotent other than `0` and `1` (exercise 17.19).[^3]

## 2. The components are the parity sectors, and they meet only at `(2, x)`

Over `Q` the fiber has one point for odd `k`, since `char_k` is irreducible (proved for `k = 2^m − 1` on [[char-k-eisenstein-at-two](pages/char-k-eisenstein-at-two.md)], computed for odd `k ≤ 31`), and two points for even `k`, the two parity-sector factors `f`, `g` of [[tower-parity-sectors](pages/tower-parity-sectors.md)]. Their closures `V(f)` and `V(g)` are the two **irreducible components** of `Spec A_k`.

The two components meet over `p` exactly when `f` and `g` share a factor mod `p`, which is when `p` divides the resultant `Res(f, g)`. For every even `k ≤ 30`, `Res(f, g) = 2^{k(k+2)/4}` ([[chinese-remainder-theorem](pages/chinese-remainder-theorem.md)]), so the components can meet only over 2. Mod 2 the factors are powers of `x`, one of them times `x + 1`:[^4]

```
k = 2:    f ≡ x         g ≡ x (x + 1)
k = 4:    f ≡ x²        g ≡ x² (x + 1)
k = 2d:   f ≡ x^d       g ≡ x^d (x + 1)          (computed for every even k ≤ 30)
```

So for every even `k ≤ 30` the two parity sectors meet at exactly one point, `(2, x)`. The fiber over 2 has two points, `(2, x)`, on both components, and `(2, x + 1)`, on the `g`-component only. For odd `k` the fiber over 2 is the single point `(2, x)`, since `char_k ≡ x^{k+1} (mod 2)` ([[castle-ring-invariant-factors](pages/castle-ring-invariant-factors.md)], footnote 5).

## 3. Fat fibers: the nilradical carries the extra `p`

At a prime `p` dividing `disc(char_k)`, some factor repeats: `char_k ≡ ∏ g_i^{m_i} (mod p)` with some `m_i ≥ 2`. The fiber ring `R = F_p[x]/(char_k)` then has nonzero nilpotents. Its **nilradical** `N(R)`, the intersection of all its prime ideals, is its set of nilpotent elements (exercise 13.11), here the multiples of `∏ g_i`.[^5] Each local factor `F_p[x]/(g^m) = F_p[x]/M^m`, with `M = (g)` maximal, is a local ring (exercise 13.26), and `1 + a` is a unit for nilpotent `a` by the finite geometric series `(1 + a)(1 − a + a² − ⋯ ± a^{m−1}) = 1 ± a^m`.[^6]

Dividing out the nilradical leaves the **reduced fiber** `R/N(R) = F_p[x]/(∏ g_i)`, a product of fields. The units split as `R^* ≅ (R/N)^* × (1 + N)`, with coprime orders `∏ (p^{d_i} − 1)` and a power of `p`. The group `1 + N` has exponent `p^{⌈log_p m⌉}`, for `m` the largest multiplicity: every `a ∈ N` has `a^m = 0`, the image of `∏ g_i` has nonzero `(m − 1)`-th power, and `(1 + a)^{p^e} = 1 + a^{p^e}` in characteristic `p`, which is `1` for every `a ∈ N` exactly when `p^e ≥ m`. The period of `P(k, ·) mod p` is the order of `x` in `R^*` (`num_k` and `den_k` are coprime mod `p` in every row of the table), so it is the period in the reduced fiber times the order of the component of `x` in `1 + N`, which divides `p^{⌈log_p m⌉}`. At every odd prime `p < 200` dividing `disc(char_k)` for `2 ≤ k ≤ 8`, that component has the full order `p^{⌈log_p m⌉}`:[^7]

| `k` | `p` | factors (degree, multiplicity) | reduced period | `p^⌈log_p m⌉` | period |
|---|---|---|---|---|---|
| 2 | 7 | (1,1), (1,2) | 3 | 7 | 21 |
| 3 | 5 | (1,2), (2,1) | 24 | 5 | 120 |
| 4 | 3 | (1,2), (3,1) | 13 | 3 | 39 |
| 4 | 107 | (1,1), (1,2), (2,1) | 159 | 107 | 17013 |
| 5 | 53 | (1,1), (1,1), (1,2), (2,1) | 2808 | 53 | 148824 |
| 6 | 3 | (1,2), (2,1), (3,1) | 104 | 3 | 312 |
| 6 | 23 | (1,1)×3, (1,2), (2,1) | 264 | 23 | 6072 |

These are all such primes in that range: the discriminants are `−2⁴·7`, `2¹²·5`, `2¹⁶·3·107`, `−2³¹·53`, `−2³⁶·3·23·643`, `2⁵⁶·5449` and `2⁶⁴·257·49697` for `k = 2, …, 8`. Over `p = 3` the fat fibers occur exactly at `k ≡ 4` and `6 (mod 12)` for `k ≤ 200`, with repeated factor `(x − 1)²` or `(x + 1)²` and never a cube; [[mod-9-coset-lift](pages/mod-9-coset-lift.md)] maps them and proves that no linear factor occurs cubed.

This is the rule `per · p^{⌈log_p m⌉}` that [[larger-prime-periodicity](pages/larger-prime-periodicity.md)] applies, split into its two parts: the reduced fiber gives the lcm of the orders of the roots, and the nilradical gives the factor of `p`. In recurrence language the nilradical is where the terms `n^{j} λ^n`, `j < m`, of a repeated root live ([[finite-fields](pages/finite-fields.md)]).

## 4. Small cases are classical rings

- **`k = 1`: `A_1 = Z[x]/(x² − 2x + 2) ≅ Z[i]`** via `x ↦ 1 + i`. The prime `(2, x)` goes to `(2, 1 + i) = (1 + i)`, the Gaussian prime over 2, and `2 = −i(1 + i)²` is the total ramification at 2 that [[char-k-eisenstein-at-two](pages/char-k-eisenstein-at-two.md)] proves for every `k = 2^m − 1`. Over an odd prime `p` the fiber has two points when `p ≡ 1 (mod 4)`, where `char_1 = (x − 1)² + 1` splits, and one when `p ≡ 3 (mod 4)`, where `(p)` stays prime, as `(3)` does in exercise 13.1 ([[finite-fields](pages/finite-fields.md)]).[^8]
- **`k = 4`, minor sector `λ² − 2λ + 4`**, with roots `1 ± i√3`. Rescaled by `λ = 2μ` it is `4(μ² − μ + 1)`, and `H_2 = μ² − μ + 1` of [[tower-parity-sectors](pages/tower-parity-sectors.md)] has roots `−ω` and `−ω²` for a primitive cube root of unity `ω`, so `Z[μ]/(H_2) ≅ Z[ω]`, the Eisenstein integers. Mod 2, `H_2 ≡ μ² + μ + 1` is irreducible and `Z[ω]/(2) ≅ F_4` is a field (exercise 13.6).[^9] The unrescaled `λ² − 2λ + 4 ≡ λ² (mod 2)` is a fat point at `(2, λ)`. The rescaling by 2 that turns the fat point into a field is the substitution `x = 2y` of [[char-k-eisenstein-at-two](pages/char-k-eisenstein-at-two.md)].
- **The three quadratic rings.** The quadratic factors of `char_1, …, char_12` are exactly `x² − 2x + 2` (`k = 1`), `x² − x + 2` (`k = 2`) and `x² − 2x + 4` (`k = 4`), with discriminants `−4`, `−7` and `−12 = 2²·(−3)`, and they give `Z[x]/(x² − 2x + 2) = Z[i]`, `Z[x]/(x² − x + 2) = Z[(1 + √−7)/2]` and `Z[x]/(x² − 2x + 4) = Z[1 + √−3] = Z[√−3]`. They are pairwise non-isomorphic by the equation test of exercise 4.11: only the first has a solution of `y² = −1`, and only the second a solution of `y² − y + 2 = 0`.[^10] The first two are the full rings of integers of their fields. `Z[√−3]` has index 2 in `Z[ω]` and is not a unique factorization domain: `4 = 2·2 = (1 + √−3)(1 − √−3)`. The rescaling `λ = 2μ` of the previous item turns it into `Z[ω]`.[^11] Its roots `1 ± √−3 = 2e^{±iπ/3}`, twice the primitive sixth roots of unity, lower the linear complexity of round two's product filter at `k = 4` from 35 to 31 ([[castle-ring-invariant-factors](pages/castle-ring-invariant-factors.md)], section 5).

## 5. Semisimple fibers, and the idempotents of `A_k`

**Semisimple fibers.** A finite commutative ring is **semisimple** when it is a product of fields, with no nonzero nilpotents. `Z/1729 = Z/7 × Z/13 × Z/19` is semisimple because 1729 is squarefree, and `Z/9` is not, because `3² = 0` (exercise 12.6).[^12] A finite ring is semisimple exactly when its radical is zero (exercise 12.12), and for these rings the radical is the nilradical of section 3.[^13] So

```
F_p[x]/(char_k mod p) is semisimple   ⇔   char_k mod p is squarefree   ⇔   p ∤ disc(char_k)   ⇔   the fiber is not fat
```

**Ideals against idempotents.** In a semisimple ring every ideal is `Re` for an idempotent `e` (exercise 12.9).[^14] The ideals of `F_p[x]/(char_k)` correspond to the monic divisors of `char_k mod p`, so there are `∏ (m_i + 1)` of them, against `2^r` idempotents, and the two counts agree exactly on semisimple fibers. `char_2 mod 5` has 4 ideals and 4 idempotents. `char_2 mod 7 = (x − 2)(x + 3)²` has 6 ideals and 4 idempotents; the two ideals that no idempotent generates are `(x + 3)` and `((x − 2)(x + 3))`.[^15]

**Lifting idempotents.** Reducing coefficients mod `p` maps `A_k` onto the fiber. An idempotent `ē` of the fiber **lifts** to `A_k` if some `e ∈ A_k` with `e² = e` in `A_k` reduces to `ē`. In `Z/10 = Z/2 × Z/5`, `5² = 25 ≡ 5`, so `5` is an idempotent, but the only integers with `e² = e` are `0` and `1`, so it does not lift to `Z`. Exercise 12.19 has the same situation for `R = {m/n : gcd(n, 6) = 1}`, whose quotient `R/6R ≅ Z/2 × Z/3` has the idempotent `3` while `R` has only `0` and `1`.[^16]

**`A_k` has only the idempotents `0` and `1`.** For odd `k` with `char_k` irreducible, `A_k` is an integral domain. For even `k ≤ 30`, an idempotent other than `0` and `1` would split `Spec A_k` into two disjoint closed sets (exercise 17.19), but the two components meet at `(2, x)` (section 2), so `Spec A_k` is connected. So no fiber idempotent other than `0` and `1` lifts to `A_k`.

**The sector idempotent needs exactly `1/2`.** Over `Q`, the element that is `1` on one sector and `0` on the other is an idempotent of `Q[x]/(char_k)`. Its coefficients have only powers of 2 in their denominators, and the largest is `2^{v_2(k!) + 1}`, with `v_2(k!)` the exponent of 2 in `k!`, for every even `k ≤ 40` (computed):[^17]

```
k = 2:                   e = (x² − x + 2)/4                     denominator 2²
k = 4, 6, 8, 10, 12:     denominators 2⁴, 2⁵, 2⁸, 2⁹, 2¹¹
```

So the idempotent lies in `A_k[1/2]`. Since 2 is invertible mod every odd `p`, it reduces to an idempotent of every odd fiber; at `p = 101` it is `(x² − x + 2)·4^{−1} = 76x² + 25x + 51`, as on [[idempotent-decomposition](pages/idempotent-decomposition.md)]. At `p = 2` the division is impossible, which is the meeting point `(2, x)` in algebraic form. Since `v_2(k!) = k − s_2(k)`, with `s_2(k)` the number of 1s in the binary expansion of `k`, the denominator is at most `2^k`, with equality exactly when `k` is a power of 2. With the sector idempotent `e`, `A_k[1/2] ≅ Z[1/2][x]/(f) × Z[1/2][x]/(g)`, a product of two domains for even `k ≤ 40`, so its only idempotents are `0`, `1`, `e` and `1 − e`; for odd `k` with `char_k` irreducible, `A_k[1/2]` is a domain. The other fiber idempotents do not lift even with `1/2` inverted.

**Nilpotents and units.** A surjective ring map carries idempotents, nilpotents and units to idempotents, nilpotents and units, and none of the three converses holds: `3` is idempotent in `Z/6`, `2` is nilpotent in `Z/4`, `2` is a unit in `Z/5`, and none is so in `Z` (exercise 4.10).[^18] Reduction `A_k → F_p[x]/(char_k)` fails all three:

- *idempotents*: the sector idempotent needs `1/2`, and no other fiber idempotent lifts even with `1/2` inverted;
- *nilpotents*: a fat fiber has nonzero nilpotents, but `A_k` has none, because `char_k` is squarefree over `Q`;
- *units*: writing `char_k(x) − char_k(0) = x·h(x)` gives `x·h(x) = −char_k(0) = (−1)^k 2^k` in `A_k`, so `x` is a unit in every fiber over an odd prime but not in `A_k`, where its norm is `±2^k`; inverting it needs `1/2^k`.[^19]

The sector idempotent and the unit `x` fail only at the prime 2, and the nilpotents occur exactly at the primes dividing `disc(char_k)` (7 for `k = 2`).

## 6. Frobenius counts the points

In characteristic `p` the map `a ↦ a^p`, **Frobenius**, respects addition as well as multiplication, because the binomial coefficients `C(p, j)`, `0 < j < p`, are divisible by `p`. On a field it is an injective ring map, so `X^{p^n} − a` has at most one root there (exercise 5.14).[^20] It fixes `F_p`, so on a fiber `F_p[x]/(char_k mod p)` it is `F_p`-linear: a `(k+1) × (k+1)` matrix whose column `j` is `x^{jp} mod char_k`.

**Proposition.** On `F_p[x]/(char_k mod p)` with `char_k ≡ ∏ g_i^{m_i}`, `d_i = deg g_i`, Frobenius has rank `Σ_i d_i ⌈m_i/p⌉`, which is `k + 1` exactly when every `m_i = 1`, and its fixed space `{a : a^p = a}` has dimension `r`, the number of points.

*Proof.* By the Chinese Remainder Theorem it suffices to treat one factor `F_p[x]/(g^m)` with `deg g = d` and `q = p^d`. Since `g` is separable over `F_p`, Hensel's lemma lifts a root of `g` mod `g` to a root in `F_p[x]/(g^m)`, so the ring contains `F_q` and equals `F_q[y]/(y^m)` with `y = g(x)`. There `(Σ_j a_j y^j)^p = Σ_j a_j^p y^{jp}`, and `a ↦ a^p` is a bijection of `F_q`, so the image is spanned over `F_q` by the `y^{jp}` with `jp < m`, that is `j < m/p`: dimension `d⌈m/p⌉` over `F_p`. If `a^p = a`, then `a = a^{p^e}` for every `e`, and for `p^e ≥ m` this is `a_0^{p^e}`, a constant; so `a ∈ F_q` with `a^p = a`, that is `a ∈ F_p`: dimension 1.

The fixed space is the span of the `r` primitive idempotents, one copy of `F_p` per point. It is the kernel of `a ↦ a^p − a`, the map whose fibers over a field are the root sets `{u, u + 1, …, u + p − 1}` of `X^p − X − c` (exercise 5.16).[^21] Counting the factors of `char_k mod p` by the dimension of this kernel is the first step of Berlekamp's factoring algorithm. The twelve fibers of the following table agree with the Proposition:[^22]

| `k` | `p` | factors (degree, multiplicity) | rank of Frobenius | `Σ d_i ⌈m_i/p⌉` | dim `{a^p = a}` | points `r` |
|---|---|---|---|---|---|---|
| 1 | 3 | (2,1) | 2 | 2 | 1 | 1 |
| 1 | 5 | (1,1), (1,1) | 2 | 2 | 2 | 2 |
| 2 | 5 | (1,1), (2,1) | 3 | 3 | 2 | 2 |
| 2 | 7 | (1,1), (1,**2**) | 2 | 2 | 2 | 2 |
| 2 | 101 | (1,1), (2,1) | 3 | 3 | 2 | 2 |
| 3 | 3 | (4,1) | 4 | 4 | 1 | 1 |
| 3 | 5 | (1,**2**), (2,1) | 3 | 3 | 2 | 2 |
| 4 | 3 | (1,**2**), (3,1) | 4 | 4 | 2 | 2 |
| 4 | 5 | (1,1), (2,1), (2,1) | 5 | 5 | 3 | 3 |
| 5 | 3 | (6,1) | 6 | 6 | 1 | 1 |
| 6 | 3 | (1,**2**), (2,1), (3,1) | 6 | 6 | 3 | 3 |
| 6 | 5 | (1,1), (1,1), (2,1), (3,1) | 7 | 7 | 4 | 4 |

Frobenius maps each root `λ` of `g_i` to the root `λ^p` of `g_i`, of the same multiplicative order, so the root orders that [[mod-p-observatory](pages/mod-p-observatory.md)] combines into an lcm are one per point, not one per root. The identity `(1 + a)^{p^e} = 1 + a^{p^e}` of section 3 is Frobenius applied `e` times.

## Snippets

`reduced_period(k, p)`, `sectors_mod2(k)`, `fiber_ideal_count(k, p)`, `sector_idempotent(k)`, `frobenius_profile(k, p)` and `x_inverse(k)` on [[castle-snippets-number-theory](pages/castle-snippets-number-theory.md)] compute the table of section 3, the mod-2 sector factors of section 2, the ideal counts and denominators of section 5, and the Frobenius table of section 6.

## Appearances in Sources

- [[calugareanu-hamburg-exercises-basic-ring-theory](pages/calugareanu-hamburg-exercises-basic-ring-theory.md)] - Chapter 13: prime ideals of `Z[X]` (13.16), `Z[i]` and `Z[ω]` (13.1, 13.6), the nilradical (13.11), `Spec` and the Zariski topology (13.18-13.21), local rings `R/M^n` (13.23, 13.26); Chapter 12: `Z_n` semisimple iff squarefree (12.6), semisimple iff zero radical for Artinian rings (12.12), ideals as `Re` (12.9), idempotents that do not lift (12.19); Chapter 5: Frobenius (5.14), Artin-Schreier polynomials (5.16); Chapter 4: what surjective maps preserve (4.10), telling rings apart by the equations they solve (4.11); Chapter 17: disconnected spectrum and idempotents (17.19).
- [[oeis-mining-pe502](pages/oeis-mining-pe502.md)] - the family `char_k`.

## Related Concepts

- [[mod-p-observatory](pages/mod-p-observatory.md)] and [[larger-prime-periodicity](pages/larger-prime-periodicity.md)] - the fibers one prime at a time, and the periods there.
- [[castle-ring-invariant-factors](pages/castle-ring-invariant-factors.md)] - the unit group of each fiber; its `p`-group of section 4 is `1 + N` here.
- [[tower-parity-sectors](pages/tower-parity-sectors.md)] - the two components for even `k`.
- [[chinese-remainder-theorem](pages/chinese-remainder-theorem.md)] and [[idempotent-decomposition](pages/idempotent-decomposition.md)] - a fiber splitting into the local rings at its points.
- [[char-k-eisenstein-at-two](pages/char-k-eisenstein-at-two.md)] - the fiber over 2 for `k = 2^m − 1`, totally ramified.
- [[finite-fields](pages/finite-fields.md)] - the residue fields `F_{p^d}` of the points.
- [[mod-9-coset-lift](pages/mod-9-coset-lift.md)] - the fibers over 3: fat exactly for `k ≡ 4, 6 (mod 12)` up to `k = 200`, never with a cubed linear factor.
- [[castle-snippets-number-theory](pages/castle-snippets-number-theory.md)] - the snippets of the section *Snippets*.
- [[metallic-means](pages/metallic-means.md)] - the same question of which ring, not only which field, for the metallic means: `δ_4 = φ³` generates `Z[√5]`, of index 2 in `Z[φ]`.
- [[castle-fibers-char-2-walkthrough](pages/castle-fibers-char-2-walkthrough.md)] - a seminar on `char_2` across `p = 5, 101, 11, 7, 2`, then over `Q` and `Z`.

## Footnotes

[^1]: [[calugareanu-hamburg-exercises-basic-ring-theory](pages/calugareanu-hamburg-exercises-basic-ring-theory.md)] Exs. 13.18-13.21 pp.55-56; solutions pp.163-165 [synthesis] - `Spec(R)` with closed sets `V(X)`, the Zariski topology, and the continuous map `f*: Spec(R') → Spec(R)`, `P' ↦ f^{−1}(P')`, induced by a ring map; here `f` is `Z → A_k`. Exercise 13.19's answer lists `Spec(Z)` as the ideals `pZ`; the zero ideal, prime in any integral domain, is the point over `Q` used here.
[^2]: [[calugareanu-hamburg-exercises-basic-ring-theory](pages/calugareanu-hamburg-exercises-basic-ring-theory.md)] Ex. 13.16 p.55; solution p.163 [synthesis] - `(n, X)` is prime in `Z[X]` iff `n` is prime, via `Z[X]/(n, X) ≅ Z_n` (14.19).
[^3]: [[calugareanu-hamburg-exercises-basic-ring-theory](pages/calugareanu-hamburg-exercises-basic-ring-theory.md)] Ex. 17.19 p.75; solution pp.192-193 [synthesis] - `Spec(R)` disconnected ⇔ `R ≅ U × V` with nonzero factors ⇔ an idempotent other than `0` and `1`.
[^4]: Verified by execution (Python 3.11 with SymPy, 2026-10-16): for each even `k ≤ 30`, `char_k` has two irreducible factors over `Q`, their reductions mod 2 are `x^{k/2}` and `x^{k/2}(x + 1)`, and `|Res(f, g)| = 2^{k(k+2)/4}`.
[^5]: [[calugareanu-hamburg-exercises-basic-ring-theory](pages/calugareanu-hamburg-exercises-basic-ring-theory.md)] Ex. 13.11 p.55; solution p.161 [synthesis] - in a commutative ring the intersection of all prime ideals is the set of nilpotent elements; for a non-nilpotent `a`, a prime avoiding `{a, a², …}` exists by Zorn's lemma.
[^6]: [[calugareanu-hamburg-exercises-basic-ring-theory](pages/calugareanu-hamburg-exercises-basic-ring-theory.md)] Exs. 13.23, 13.25-13.26 pp.56-57; solutions pp.166-167 [synthesis] - a ring is local iff its non-units form an ideal; `R/M^n` is local for `M` maximal, because for `a ∈ M`, `(a + 1)(1 − a + a² − … + (−1)^{n−1} a^{n−1}) = 1 + (−1)^{n−1} a^n` makes `a + 1` a unit mod `M^n`.
[^7]: Verified by execution (Python 3.11 with SymPy, 2026-10-16): `disc(char_k)` factored for `k ≤ 8`; for each odd prime `p < 200` dividing it, the order of `x` in `F_p[x]/(char_k)` equals its order in `F_p[x]/(∏ g_i)` times `p^{⌈log_p m⌉}`, orders computed by stripping prime factors from `∏ (p^{d_i} − 1) p^{d_i(m_i − 1)}`; `num_k` and `den_k` are coprime mod `p` in all seven cases; the fat fibers over 3 for `k ≤ 60` are exactly `k ≡ 4, 6 (mod 12)`, with `(x − 1)²` or `(x + 1)²`.
[^8]: [[calugareanu-hamburg-exercises-basic-ring-theory](pages/calugareanu-hamburg-exercises-basic-ring-theory.md)] Ex. 13.1 p.54; solution p.159 [synthesis] - `(3)` and `(1 + i)` are prime in `Z[i]` and `(2)` is not; an odd prime `p` stays prime in `Z[i]` iff `a² + b² = p` has no integer solution. (The solution's opening claim that `x` is prime iff its norm is prime holds for the non-rational primes only; the book handles rational primes separately in the same solution.)
[^9]: [[calugareanu-hamburg-exercises-basic-ring-theory](pages/calugareanu-hamburg-exercises-basic-ring-theory.md)] Ex. 13.6 p.54; solution p.160 [synthesis] - `F_4` has characteristic 2, its two elements outside the prime field satisfy `x² = x + 1`, `(2)` is prime in `Z[ω]` with `ω² + ω + 1 = 0`, and `Z[ω]/(2) ≅ F_4`. That `H_2(μ) = μ² − μ + 1` has the roots `−ω, −ω²` is direct: `(−ω)² − (−ω) + 1 = ω² + ω + 1 = 0`.
[^10]: [[calugareanu-hamburg-exercises-basic-ring-theory](pages/calugareanu-hamburg-exercises-basic-ring-theory.md)] Ex. 4.11 p.21; solution p.109 [synthesis] - ring isomorphisms preserve solutions of polynomial equations with integer coefficients (the book uses `x² = 1 + 1` to separate `Z[√2]` from `Z[√3]`).
[^11]: Verified by execution (Python 3.11 with SymPy, 2026-10-16): the quadratic irreducible factors of `char_1, …, char_12` over `Q` are exactly `x² − 2x + 2`, `x² − x + 2` and `x² − 2x + 4`, with discriminants `−4`, `−7` and `−12 = 2²·(−3)`, so the first two generate maximal orders and the third has conductor 2. `4 = (1 + √−3)(1 − √−3)` with `1 ± √−3` irreducible in `Z[√−3]` is the standard example of non-unique factorization.
[^12]: [[calugareanu-hamburg-exercises-basic-ring-theory](pages/calugareanu-hamburg-exercises-basic-ring-theory.md)] Ex. 12.6 p.50; solution p.154 [synthesis] - `Z_n` is semisimple iff `n` is squarefree.
[^13]: [[calugareanu-hamburg-exercises-basic-ring-theory](pages/calugareanu-hamburg-exercises-basic-ring-theory.md)] Ex. 12.12 p.50; solutions pp.155-156 [synthesis] - a ring is left semisimple iff its radical is zero and it is left Artinian; finite rings are Artinian, and for a finite commutative ring the radical equals the nilradical (every prime of a finite ring is maximal).
[^14]: [[calugareanu-hamburg-exercises-basic-ring-theory](pages/calugareanu-hamburg-exercises-basic-ring-theory.md)] Ex. 12.9 p.50; solution p.154 [synthesis] - in a ring with identity, an ideal that is a direct summand is generated by a central idempotent, `A = eA = Ae`; in a semisimple ring every ideal is a direct summand.
[^15]: Verified by execution (Python 3.11 with SymPy, 2026-10-16): for `(k, p) ∈ {(1, 3), (2, 5), (2, 7), (3, 5), (4, 3)}`, `∏ (m_i + 1)` ideals against `2^r` idempotents: `2/2`, `4/4`, `6/4`, `6/4`, `6/4`.
[^16]: [[calugareanu-hamburg-exercises-basic-ring-theory](pages/calugareanu-hamburg-exercises-basic-ring-theory.md)] Ex. 12.19 p.51; solution p.158 [synthesis] - `R = {m/n ∈ Q : gcd(6, n) = 1}` has exactly the maximal ideals `2R, 3R`, `R/rad(R) = R/6R ≅ Z_2 × Z_3` is semisimple, and the idempotent `3 + 6R` has no idempotent preimage in `R`.
[^17]: Verified by execution (Python 3.11 with SymPy, 2026-10-16): for each even `k ≤ 40`, `e = g·(g^{−1} mod f) mod char_k` over `Q` for the two factors `f, g` of `char_k`; every coefficient denominator is a power of 2, and the largest is `2^{v_2(k!) + 1}`; at `k = 2`, `e = x²/4 − x/4 + 1/2`.
[^18]: [[calugareanu-hamburg-exercises-basic-ring-theory](pages/calugareanu-hamburg-exercises-basic-ring-theory.md)] Ex. 4.10 p.20; solution p.109 [synthesis] - surjective ring maps preserve idempotents, nilpotents and units; the converses fail for `Z → Z_6` (idempotent `3`), `Z → Z_4` (nilpotent `2`), `Z → Z_5` (units).
[^19]: Verified by execution (Python 3.11 with SymPy, 2026-10-16): `x·h(x) − char_k(x) = −char_k(0) = (−1)^k 2^k`, that is `−2, 4, −8, 16, −32` for `k = 1, …, 5`.
[^20]: [[calugareanu-hamburg-exercises-basic-ring-theory](pages/calugareanu-hamburg-exercises-basic-ring-theory.md)] Ex. 5.14 p.25; solution p.113 [synthesis] - in characteristic `p`, `x ↦ x^{p^n}` is a unital ring homomorphism of a field `K`, injective since its kernel is a proper ideal of a field, so `X^{p^n} − a` has at most one root in `K`.
[^21]: [[calugareanu-hamburg-exercises-basic-ring-theory](pages/calugareanu-hamburg-exercises-basic-ring-theory.md)] Ex. 5.16 p.25; solution p.113 [synthesis] - over a field of characteristic `p`, if `u` is a root of `X^p − X − a` then so are `u + 1, …, u + p − 1`, so the polynomial is irreducible or splits completely; two variants reduce to it by substitution.
[^22]: Verified by execution (Python 3.11 with SymPy `DomainMatrix` over `GF(p)`, 2026-10-16): for the 12 pairs `(k, p)` in the table, the Frobenius matrix (columns `x^{jp} mod char_k`, `j = 0, …, k`) has rank `Σ d_i ⌈m_i/p⌉`, and `M − I` has nullity equal to the number of distinct irreducible factors of `char_k mod p`.
