---
title: The castle ring's spectrum - Spec Z[x]/(char_k) over Spec Z
category: Analyses
summary: Read Z[x]/(char_k) as a family of rings over the primes. The fiber over p is F_p[x]/(char_k mod p), whose points are the distinct irreducible factors - exactly the mod-p observatory's factor signatures. The fiber over Q has one point for odd k and two for even k (the parity sectors, the irreducible components). The two sector components meet at exactly one point, (2, x), because the sector factors reduce mod 2 to x^(k/2) and x^(k/2)(x+1) - the geometric reading of their resultant 2^(k(k+2)/4). Fibers at discriminant primes carry nilpotents, and the nilradical accounts for exactly the extra p in the periods - per = (reduced period) · p^⌈log_p m⌉ at all 7 discriminant-zero primes tested. Small cases are classical rings - Z[i] for k = 1 (the castle prime (2, x) is the Gaussian prime (1 + i)) and Z[ω] for the k = 4 minor sector (mod 2 it is the field F_4).
tags: [analysis, castle, ring, spectrum, prime-ideal, nilradical, local-ring, finite-field, parity-sector, resultant, period, gaussian-integers, eisenstein-integers, sympy, verification]
sources: [calugareanu-hamburg-exercises-basic-ring-theory, oeis-mining-pe502]
created: 2026-09-26
updated: 2026-09-26
---

# The castle ring's spectrum - `Spec Z[x]/(char_k)` over `Spec Z`

## The picture

The wiki studies the castle ring `F_p[x]/(char_k)` one prime at a time: [[mod-p-observatory](pages/mod-p-observatory.md)] and [[larger-prime-periodicity](pages/larger-prime-periodicity.md)] factor `char_k mod p`, [[castle-ring-invariant-factors](pages/castle-ring-invariant-factors.md)] reads off unit groups, [[tower-parity-sectors](pages/tower-parity-sectors.md)] splits `char_k` over `Q`. All of these are views of a single ring, `A_k = Z[x]/(char_k)`, and its set of prime ideals `Spec A_k`.

**Points and what they lie over.** A *point* of `Spec A_k` is a prime ideal `P` of `A_k`. Intersecting it with the integers, `P ∩ Z`, gives a prime ideal of `Z`: either `(0)`, if `P` contains no nonzero integer, or `(p)` for the one prime number `p` that `P` contains. We say `P` **lies over** `(0)` or over `(p)`. This is the map `Spec A_k → Spec Z`, `P ↦ P ∩ Z`, induced by the inclusion `Z → A_k`.[^1]

**Fiber.** The **fiber over `(p)`** is the set of all points of `Spec A_k` that lie over `(p)`, the preimage of the single point `(p)` under that map. It is the same idea as the fiber of any map: everything upstairs that lands on one point downstairs. Algebraically the fiber is computed by setting `p = 0`. The primes of `A_k` containing `p` correspond to the primes of `A_k/pA_k = Z[x]/(p, char_k) = F_p[x]/(char_k mod p)`. The fiber over `(0)` works the same way with `Q` in place of `F_p`: its points are the primes of `A_k ⊗ Q = Q[x]/(char_k)`. So `Spec A_k` sits over `Spec Z = {(0), (2), (3), (5), …}` like a curve over a line, and each fiber is a finite set of points:

```
fiber over (0):  primes of Q[x]/(char_k)      = the irreducible factors of char_k over Q
fiber over (p):  primes of F_p[x]/(char_k)    = the distinct irreducible factors of char_k mod p
```

A fiber's **ring** `F_p[x]/(char_k mod p)` carries more than its set of points. When `char_k mod p` has a repeated factor, the fiber ring has nonzero nilpotents that the point set does not see. Such a fiber is called **fat** (§3).

The second line of the table is the statement that `(p, g)` is a prime of `Z[x]` exactly when `g` is irreducible mod `p`. The book's case `g = X` is exercise 13.16, `(n, X)` prime iff `n` is prime.[^2] Everything below is a reading of this picture.

## 1. The fibers are the observatory's factor signatures

Over an odd prime `p`, the fiber has one point per distinct irreducible factor `g_i` of `char_k mod p`, and the point's residue field is `F_{p^{d_i}}`. The factor-degree multisets that [[larger-prime-periodicity](pages/larger-prime-periodicity.md)] tabulates (for example `(x − 2)(x² − x + 2)` for `char_2 mod 101`: two points, residue fields `F_101` and `F_{101²}`) are the fiber shapes of `Spec A_k`. The CRT split of [[chinese-remainder-theorem](pages/chinese-remainder-theorem.md)] is the fiber falling apart into its points, and the [[idempotent-decomposition](pages/idempotent-decomposition.md)] count `2^r` is `2^(number of points)`. A ring splits into a product exactly when its spectrum is disconnected (exercise 17.19).[^3]

## 2. Components are parity sectors, and they meet only at `(2, x)`

Over `Q` the fiber has one point for odd `k` (`char_k` irreducible - proved for `k = 2^m − 1` on [[char-k-eisenstein-at-two](pages/char-k-eisenstein-at-two.md)], verified to `k = 31`) and two for even `k`: the two parity-sector factors `f, g` of [[tower-parity-sectors](pages/tower-parity-sectors.md)]. Their closures `V(f)` and `V(g)` are the two **irreducible components** of `Spec A_k`.

Two components meet over `p` exactly when `f` and `g` share a factor mod `p`, which happens exactly when `p` divides the resultant `Res(f, g)`. That resultant is `2^{k(k+2)/4}` for every even `k ≤ 30` ([[chinese-remainder-theorem](pages/chinese-remainder-theorem.md)]), so the components can only meet over 2. Over 2 both factors are pure powers of `x` up to one extra `(x + 1)`:[^4]

```
k = 2:   f ≡ x         g ≡ x (x + 1)
k = 4:   f ≡ x²        g ≡ x² (x + 1)
k = 2d:  f ≡ x^d       g ≡ x^d (x + 1)          (checked every even k ≤ 30)
```

So **the two parity sectors of `Spec A_k` meet at exactly one point, `(2, x)`**, and nowhere else. The fiber over 2 has two points, `(2, x)` (on both components) and `(2, x + 1)` (on the `g`-component only). For odd `k` the fiber over 2 is the single point `(2, x)`, since `char_k ≡ x^{k+1}` (mod 2) ([[castle-ring-invariant-factors](pages/castle-ring-invariant-factors.md)] footnote 5).

## 3. Fat fibers: the nilradical carries the extra `p`

At a prime `p | disc(char_k)`, some factor repeats: `char_k ≡ ∏ g_i^{m_i}` with some `m_i ≥ 2`. The fiber ring `R = F_p[x]/(char_k)` then has nonzero nilpotents. Its **nilradical** `N(R)`, the intersection of all its primes, is exactly its set of nilpotent elements (exercise 13.11), here the multiples of `∏ g_i` mod `char_k`.[^5] Each local piece `F_p[x]/(g^m) = F_p[x]/M^m` with `M = (g)` maximal is a local ring (exercise 13.26), and `1 + a` is a unit for nilpotent `a` by the finite geometric series `(1 + a)(1 − a + a² − … ± a^{m−1}) = 1 ± a^m`.[^6]

Dividing out the nilradical leaves the **reduced fiber** `R/N(R) = F_p[x]/(∏ g_i)`, a product of fields. Units split as `R^* ≅ (R/N)^* × (1 + N)`, with orders coprime (`∏ (p^{d_i} − 1)` against a power of `p`), and `1 + N` has exponent `p^⌈log_p m⌉` for `m` the largest multiplicity, because `(1 + a)^{p^e} = 1 + a^{p^e}` in characteristic `p`. The period of `P(k, ·) mod p` is `ord(x)` in `R^*`, so it is the reduced period times the order of `x`'s component in `1 + N`, which divides `p^⌈log_p m⌉`. **At every discriminant-zero prime tested, that component has the full order:**[^7]

| `k` | `p` | factors (degree, multiplicity) | reduced period | `× p^⌈log_p m⌉` | full period |
|---|---|---|---|---|---|
| 2 | 7 | (1,1), (1,2) | 3 | 7 | 21 |
| 3 | 5 | (1,2), (2,1) | 24 | 5 | 120 |
| 4 | 3 | (1,2), (3,1) | 13 | 3 | 39 |
| 4 | 107 | (1,1), (1,2), (2,1) | 159 | 107 | 17013 |
| 5 | 53 | (1,1), (1,1), (1,2), (2,1) | 2808 | 53 | 148824 |
| 6 | 3 | (1,2), (2,1), (3,1) | 104 | 3 | 312 |
| 6 | 23 | (1,1)×3, (1,2), (2,1) | 264 | 23 | 6072 |

This is the "multiplicity-inflation" rule `per · p^⌈log_p m⌉` that [[larger-prime-periodicity](pages/larger-prime-periodicity.md)] applies. Here it is split into its two ring-theoretic parts: the reduced fiber gives the `lcm` of eigenvalue orders, and the nilradical gives the factor of `p`. In recurrence language the nilradical is where the `n^{m−1} λ^n` terms of [[finite-fields](pages/finite-fields.md)] live. That `x`'s unipotent part always has the *maximal* order `p^⌈log_p m⌉`, not a proper divisor of it, is verified in these seven cases but not proved.

## 4. Small castles are classical rings

- **`k = 1`: `A_1 = Z[x]/(x² − 2x + 2) ≅ Z[i]`** via `x ↦ 1 + i`. The castle prime `(2, x)` goes to `(2, 1 + i) = (1 + i)`, the Gaussian prime over 2, and `2 = −i(1 + i)²` is the total ramification that [[char-k-eisenstein-at-two](pages/char-k-eisenstein-at-two.md)] proves for every `k = 2^m − 1`. The primes of `Z[i]` over odd `p` are the fibers of [[finite-fields](pages/finite-fields.md)] Step 5: two points when `p ≡ 1 (mod 4)` (`char_1` splits), one when `p ≡ 3 (mod 4)` (`(p)` stays prime, exercise 13.1's `(3)`).[^8]
- **`k = 4`, minor sector: `λ² − 2λ + 4`**, roots `1 ± i√3`. Rescaled by `λ = 2μ` it is `H_2 = μ² − μ + 1` ([[tower-parity-sectors](pages/tower-parity-sectors.md)]), roots `−ω, −ω²` for `ω` a primitive cube root of unity, so `Z[μ]/(H_2) ≅ Z[ω]`, the Eisenstein integers. Mod 2, `H_2 ≡ μ² + μ + 1` is irreducible and `Z[ω]/(2) ≅ F_4` is a field (exercise 13.6).[^9] The unrescaled `λ² − 2λ + 4 ≡ λ²` mod 2 is instead a fat point at `(2, λ)`. Rescaling by 2 turns the fat point into a field, which is the same move that makes Eisenstein work on [[char-k-eisenstein-at-two](pages/char-k-eisenstein-at-two.md)].

## What this settles and what it opens

**Settled.**
- The fiber of `Spec Z[x]/(char_k)` over each prime is the observatory's factor signature, and the CRT and idempotent structure is that fiber's decomposition into points.
- For even `k ≤ 30` the two parity-sector components meet only over 2, and there only at the single point `(2, x)`.
- The period inflation at discriminant primes is the nilradical: `per = (reduced period) · p^⌈log_p m⌉` in all 7 tested cases.

**Open.**
- Prove that `x`'s component in `1 + N(R)` always has full order `p^⌈log_p m⌉` at discriminant-zero primes (equivalently: that the multiplicity-inflation rule is an equality, not just a divisibility).
- Prove the resultant formula `2^{k(k+2)/4}`, which would make "sectors meet only at `(2, x)`" a theorem for all even `k`.
- For odd `k` not of the form `2^m − 1`, `A_k` is not the full ring of integers at 2 (the 2-adic Newton polygon has several segments, [[char-k-eisenstein-at-two](pages/char-k-eisenstein-at-two.md)]); describe the primes of the normalization above 2.

## Snippets

`reduced_period(k, p)` and `sectors_mod2(k)` on [[castle-snippets-number-theory](pages/castle-snippets-number-theory.md)] reproduce the table in §3 and the mod-2 sector factors in §2.

## Appearances in Sources

- [[calugareanu-hamburg-exercises-basic-ring-theory](pages/calugareanu-hamburg-exercises-basic-ring-theory.md)] - Chapter 13: prime ideals of `Z[X]` (13.16), `Z[i]` and `Z[ω]` (13.1, 13.6), the nilradical (13.11), Spec and the Zariski topology (13.18-13.21), local rings `R/M^n` (13.23, 13.26).
- [[oeis-mining-pe502](pages/oeis-mining-pe502.md)] - the `char_k` family.

## Related Concepts

- [[mod-p-observatory](pages/mod-p-observatory.md)] / [[larger-prime-periodicity](pages/larger-prime-periodicity.md)] - the fibers, one prime at a time.
- [[castle-ring-invariant-factors](pages/castle-ring-invariant-factors.md)] - unit groups of each fiber; §4's `p`-group is `1 + N` here.
- [[tower-parity-sectors](pages/tower-parity-sectors.md)] - the two components for even `k`.
- [[chinese-remainder-theorem](pages/chinese-remainder-theorem.md)] / [[idempotent-decomposition](pages/idempotent-decomposition.md)] - a fiber splitting into its points.
- [[char-k-eisenstein-at-two](pages/char-k-eisenstein-at-two.md)] - the fiber over 2 for `k = 2^m − 1`, totally ramified.
- [[finite-fields](pages/finite-fields.md)] - residue fields `F_{p^d}` of the points.
- [[castle-snippets-number-theory](pages/castle-snippets-number-theory.md)] - `reduced_period`, `sectors_mod2`.

## Footnotes

[^1]: [[calugareanu-hamburg-exercises-basic-ring-theory](pages/calugareanu-hamburg-exercises-basic-ring-theory.md)] Exs. 13.18-13.21 pp.55-56; solutions pp.163-165 [synthesis] - `Spec(R)` with closed sets `V(X)`, the Zariski topology, and the continuous map `f*: Spec(R') → Spec(R)`, `P' ↦ f^{−1}(P')`, induced by a ring map; here `f` is `Z → A_k`, and `f*` sends each prime of `A_k` to the prime of `Z` it lies over. Exercise 13.19's answer lists `Spec(Z)` as the ideals `pZ`; the zero ideal, prime in any integral domain, is the extra "generic" point over `Q` used here.
[^2]: [[calugareanu-hamburg-exercises-basic-ring-theory](pages/calugareanu-hamburg-exercises-basic-ring-theory.md)] Ex. 13.16 p.55; solution p.163 [synthesis] - `(n, X)` is prime in `Z[X]` iff `n` is prime, via `Z[X]/(n, X) ≅ Z_n` (14.19).
[^3]: [[calugareanu-hamburg-exercises-basic-ring-theory](pages/calugareanu-hamburg-exercises-basic-ring-theory.md)] Ex. 17.19 p.75; solution pp.192-193 [synthesis] - `Spec(R)` disconnected ⇔ `R ≅ U × V` with nonzero factors ⇔ a nontrivial idempotent.
[^4]: Verified by execution (Python 3.10, SymPy, 2026-09-26): for each even `k ≤ 30`, `sp.factor_list(char_k)` returns two factors whose reductions mod 2 are `x^{k/2}` and `x^{k/2}(x + 1)`; `k = 2, 4, 6` pinned under `sectors_mod2` on [[castle-snippets-number-theory](pages/castle-snippets-number-theory.md)]. The resultant `2^{k(k+2)/4}` for even `k ≤ 30` is verified on [[chinese-remainder-theorem](pages/chinese-remainder-theorem.md)].
[^5]: [[calugareanu-hamburg-exercises-basic-ring-theory](pages/calugareanu-hamburg-exercises-basic-ring-theory.md)] Ex. 13.11 p.55; solution p.161 [synthesis] - in a commutative ring the intersection of all prime ideals equals the set of nilpotent elements; the solution builds, for a non-nilpotent `a`, a prime avoiding `{a, a², …}` by Zorn's lemma.
[^6]: [[calugareanu-hamburg-exercises-basic-ring-theory](pages/calugareanu-hamburg-exercises-basic-ring-theory.md)] Exs. 13.23, 13.25-13.26 pp.56-57; solutions pp.166-167 [synthesis] - a ring is local iff its non-units form an ideal; `R/M^n` is local for `M` maximal, because for `a ∈ M`, `(a + 1)(1 − a + a² − … + (−1)^{n−1} a^{n−1}) = 1 + (−1)^{n−1} a^n` makes `a + 1` a unit mod `M^n`.
[^7]: Verified by execution (Python 3.10, SymPy, 2026-09-26): for every odd prime `p < 200` dividing `disc(char_k)`, `2 ≤ k ≤ 8`, with a repeated factor mod `p`, `ord(x)` in `F_p[x]/(char_k)` equals `ord(x)` in `F_p[x]/(∏ g_i)` times `p^⌈log_p m_max⌉`; orders computed by stripping prime factors from the unit-group order `∏ (p^{d_i} − 1) p^{d_i(m_i − 1)}`. Four rows pinned under `reduced_period` on [[castle-snippets-number-theory](pages/castle-snippets-number-theory.md)]. The `k = 2, 3, 4` full periods match [[mod-p-observatory](pages/mod-p-observatory.md)] (21, 120, 39).
[^8]: [[calugareanu-hamburg-exercises-basic-ring-theory](pages/calugareanu-hamburg-exercises-basic-ring-theory.md)] Ex. 13.1 p.54; solution p.159 [synthesis] - `(3)` and `(1 + i)` are prime in `Z[i]` and `(2)` is not; an odd prime `p` stays prime in `Z[i]` iff `a² + b² = p` has no integer solution. (The solution's opening claim that `x` is prime iff its norm is prime holds for the non-rational primes only; the book handles rational primes separately in the same solution.) `char_1(1 + i) = 0` is checked on the source page.
[^9]: [[calugareanu-hamburg-exercises-basic-ring-theory](pages/calugareanu-hamburg-exercises-basic-ring-theory.md)] Ex. 13.6 p.54; solution p.160 [synthesis] - `F_4` has characteristic 2, its two non-prime-field elements satisfy `x² = x + 1`, `(2)` is prime in `Z[ω]` with `ω² + ω + 1 = 0`, and `Z[ω]/(2) ≅ F_4`. The identification `H_2(μ) = μ² − μ + 1` with roots `−ω, −ω²` (so `Z[μ]/(H_2) = Z[ω]`) is direct: `(−ω)² − (−ω) + 1 = ω² + ω + 1 = 0`.
