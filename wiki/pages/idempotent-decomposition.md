---
title: Idempotent decomposition
category: Concepts
summary: An idempotent e (e² = e) other than 0 and 1 splits a commutative ring as R ≅ Re × R(1 − e), and every splitting arises this way. In the castle ring F_p[x]/(char_k) the idempotents are exactly the 0/1 patterns on the CRT factors, so there are 2^r of them (r = distinct irreducible factors of char_k mod p), and the primitive ones project the recurrence onto one eigenvalue sector. At k = 2, p = 101 the idempotent for the dominant root 2 is (x² − x + 2)/4, and x^L acts on it as 2^L. Checked by brute force on eight (k, p) cases, including repeated-factor ones.
tags: [concept, ring, idempotent, chinese-remainder-theorem, quotient-ring, finite-field, eigenvalue, projection, castle]
sources: [calugareanu-hamburg-exercises-basic-ring-theory]
created: 2026-09-26
updated: 2026-09-26
---

# Idempotent decomposition

## Description

An element `e` of a ring is **idempotent** if `e² = e`. `0` and `1` always are. In a commutative ring with identity, if `e` is idempotent then so is `1 − e`, and `e(1 − e) = 0`. The ideals `Re` and `R(1 − e)` are then comaximal (`e + (1 − e) = 1`) and meet only in `0`, so by the [[chinese-remainder-theorem](pages/chinese-remainder-theorem.md)]

```
R  ≅  R/R(1 − e)  ×  R/Re  ≅  Re × R(1 − e),       r ↦ (re, r(1 − e)).
```

Conversely, if `R ≅ U × V` with both factors nonzero, `(1, 0)` is an idempotent other than `0, 1`. So **a commutative ring is a nontrivial product exactly when it has a nontrivial idempotent**. The book adds a third equivalent condition: the prime spectrum `Spec(R)` is disconnected.[^1] Splitting a ring into factors and finding its idempotents are the same problem.

An idempotent `e ≠ 0` is **primitive** if it is not a sum of two nonzero orthogonal idempotents (`e = u + v`, `uv = 0`).[^2] A finite commutative ring is the product of the rings `Re_i` over its primitive idempotents `e_1, …, e_r`, and these are orthogonal (`e_i e_j = 0`) and sum to `1`. Every idempotent is a sum of a subset of them, so there are exactly `2^r`. Pairing `e` with `1 − e` shows that the product of all nonzero idempotents is `1` when `r = 1` (only `e = 1`) and `0` when `r ≥ 2`.[^3]

## In the castle ring

Take `R = F_p[x]/(Q)` with `Q = char_k mod p = ∏_{i=1}^r g_i^{m_i}` ([[castle-cryptography-ring](pages/castle-cryptography-ring.md)]). By CRT, `R ≅ ∏ F_p[x]/(g_i^{m_i})`. Each factor is a field or a local ring, and a local ring's only idempotents are `0` and `1`. So:

- **`R` has exactly `2^r` idempotents**, where `r` counts *distinct* irreducible factors. Repeated factors do not add idempotents; they add nilpotents instead.
- **The primitive idempotent `e_i`** is the element that is `1` in the `g_i` factor and `0` in the others. It is the CRT inverse of a unit vector, computed as `e_i = N_i · (N_i^{−1} mod g_i^{m_i})` with `N_i = Q/g_i^{m_i}`.
- **Multiplying by `x` respects the split.** Multiplication by `x` is one step of the recurrence ([[castle-cryptography-ring](pages/castle-cryptography-ring.md)] §3), and it commutes with every `e_i`. So `e_i` picks out the part of the sequence that comes from the eigenvalues that are roots of `g_i`. For a linear factor `g_i = x − λ`, `x^L e_i = λ^L e_i`.

**Worked example - `k = 2`, `p = 101`.** Here `char_2 = (x − 2)(x² − x + 2)`, `r = 2`, and `R` has four idempotents `0, e_1, e_2, 1`:[^4]

```
e_1  =  (x² − x + 2) / 4  =  76x² + 25x + 51      (1 at x = 2;  0 mod x² − x + 2)
e_2  =  1 − e_1           =  25x² − 25x + 51      (0 at x = 2;  1 mod x² − x + 2)
e_1 + e_2 = 1,    e_1 · e_2 = 0 (mod char_2, p = 101)
```

The formula for `e_1` is Lagrange interpolation: the other factor, divided by its value at the root `2`, and `4^{−1} = 76 (mod 101)`. Since `x·(x² − x + 2) ≡ 2·(x² − x + 2) (mod char_2)`, `x^L e_1 = 2^L e_1`. So `e_1` isolates the **dominant eigenvalue `2`** of `P(2, ·)`, the `+1` parity sector of [[tower-parity-sectors](pages/tower-parity-sectors.md)], and `e_2` isolates the complex pair `(1 ± √−7)/2`. The eigenvalue sectors that [[tower-parity-sectors](pages/tower-parity-sectors.md)] finds over `Q` show up mod `p` as idempotents.

**Brute-force check.** The table below counts every idempotent of `F_p[x]/(char_k)` over all `p^{k+1}` elements, and takes the product of the nonzero ones:[^4]

| `k` | `p` | factor (degree, multiplicity) | idempotents | `2^r` | product of nonzero idempotents |
|---|---|---|---|---|---|
| 1 | 3 | (2,1) | 2 | 2 | 1 |
| 1 | 5 | (1,1), (1,1) | 4 | 4 | 0 |
| 2 | 3 | (1,1), (2,1) | 4 | 4 | 0 |
| 2 | 5 | (1,1), (2,1) | 4 | 4 | 0 |
| 2 | 7 | (1,1), (1,**2**) | 4 | 4 | 0 |
| 3 | 3 | (4,1) | 2 | 2 | 1 |
| 3 | 5 | (1,**2**), (2,1) | 4 | 4 | 0 |
| 4 | 3 | (1,**2**), (3,1) | 4 | 4 | 0 |

The repeated-factor rows (`char_2 mod 7`, `char_3 mod 5`, `char_4 mod 3`, the discriminant-zero cases of [[castle-ring-invariant-factors](pages/castle-ring-invariant-factors.md)] §4) still have `2^r` idempotents. The multiplicity shows up only in the local factor's `p`-group of units, never in the idempotents. The irreducible rows (`char_1 mod 3`, `char_3 mod 3`) have only `0, 1`: `R` is a field, and the product in 17.8 is `1`.

## Why it is worth having on the wiki

- It gives the CRT split as **explicit elements of `R`**. The projections of [[castle-cryptography-ring](pages/castle-cryptography-ring.md)] §4 become multiplication by `e_i`, and lifting back is `Σ a_i e_i`.
- It connects the combinatorial sector split over `Q` ([[tower-parity-sectors](pages/tower-parity-sectors.md)]) with the arithmetic split mod `p` ([[castle-ring-invariant-factors](pages/castle-ring-invariant-factors.md)]).
- [[parity-via-roots-of-unity](pages/parity-via-roots-of-unity.md)] uses a different kind of idempotent: the character-sum projectors `(1/m) Σ_j ω^{−jr} ω^{j·b}` (which pick out `b ≡ r mod m`) in the group algebra of the cyclic group of order `m`. Those split a *statistic* by residue class, where the idempotents here split the *ring*. Both are instances of "idempotent = projector onto a direct factor".

## Appearances in Sources

- [[calugareanu-hamburg-exercises-basic-ring-theory](pages/calugareanu-hamburg-exercises-basic-ring-theory.md)] - Ex. 17.19 (splitting ⇔ idempotent ⇔ disconnected spectrum), Ex. 17.8 (product of nonzero idempotents), Ex. 17.10 (the definition of primitive idempotent in the chapter preamble).

## Related Concepts

- [[chinese-remainder-theorem](pages/chinese-remainder-theorem.md)] - the idempotents are the CRT inverse of the unit vectors.
- [[castle-cryptography-ring](pages/castle-cryptography-ring.md)] - the ring and its §4 CRT projections.
- [[castle-ring-invariant-factors](pages/castle-ring-invariant-factors.md)] - the unit group of each factor; repeated factors change units, not idempotents.
- [[tower-parity-sectors](pages/tower-parity-sectors.md)] - the eigenvalue sectors over `Q` that the idempotents realize mod `p`.
- [[parity-via-roots-of-unity](pages/parity-via-roots-of-unity.md)] - character-sum idempotents in a group algebra; the same idea applied to a statistic.
- [[finite-fields](pages/finite-fields.md)] - the field factors.

## Footnotes

[^1]: [[calugareanu-hamburg-exercises-basic-ring-theory](pages/calugareanu-hamburg-exercises-basic-ring-theory.md)] Ex. 17.19 p.75; solution pp.192-193 [synthesis] - disconnected `Spec(R)` ⇔ `R ≅ U × V` with nonzero factors ⇔ an idempotent `e ∉ {0, 1}`; from `e`, `Re` and `R(1 − e)` are comaximal proper ideals with zero intersection, giving `R ≅ R/Re × R/R(1 − e)`.
[^2]: [[calugareanu-hamburg-exercises-basic-ring-theory](pages/calugareanu-hamburg-exercises-basic-ring-theory.md)] Ch. 17 preamble p.73 and Ex. 17.10 p.74 [synthesis] - a nonzero idempotent is primitive if it is not the sum of two orthogonal idempotents; 17.10 characterizes this as `eRe` having no idempotents besides `0` and `e`.
[^3]: [[calugareanu-hamburg-exercises-basic-ring-theory](pages/calugareanu-hamburg-exercises-basic-ring-theory.md)] Ex. 17.8 p.74; solution p.190 [synthesis] - in a finite commutative ring with `1 ≠ 0`, nonzero idempotents pair as `e, 1 − e` with `e(1 − e) = 0`, so their product is `1` if `1` is the only one and `0` otherwise.
[^4]: Verified by execution (Python 3.10, SymPy, 2026-09-26). (i) `char_2 mod 101` factors as `(x − 2)(x² − x + 2)`; the CRT idempotents computed as `N_i · (N_i^{−1} mod g_i)` are `−25x² + 25x − 50 ≡ 76x² + 25x + 51` and `25x² − 25x − 50 ≡ 25x² − 25x + 51`; each satisfies `e² − e ≡ 0 mod (char_2, 101)`, their sum is `1` and their product is `0`. (ii) For each `(k, p)` in the table, all `p^{k+1}` residues `e` were tested for `e² ≡ e mod char_k`; the count equals `2^r` with `r = len(sp.factor_list(char_k, modulus=p)[1])`, and the product of the nonzero idempotents is as shown.
