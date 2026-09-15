---
title: Finite fields for the castle count
category: Concepts
summary: Why reducing char_k mod p turns aperiodic eigenvalues into periodic ones — F_{p^d} and its cyclic multiplicative group, built up from F_5 to F_49 to the general rule.
tags: [concept, finite-field, modular-arithmetic, periodicity, pedagogy]
sources: [oeis-mining-pe502]
created: 2026-09-14
updated: 2026-09-14
---

# Finite fields for the castle count

## The core idea

The signed tower count is, over ℚ, a sum of eigenvalue powers `P(k,L) = Σ c_i λ_i^L` — and **aperiodic**, because a complex eigenvalue like `1+i` has infinite order: no positive power of `1+i` ever equals 1. Reduce mod p, and the eigenvalues stop being complex numbers and become elements of a **finite field** `F_{p^d}`, whose nonzero elements form a cyclic group of order `p^d − 1`. In a finite group, every element has finite order — so `λ^L` is now *periodic*, and so is the whole sequence. This page builds that up from the smallest case.

## Step 1 — Over ℚ: aperiodic

`P(1,L) = Re((1+i)^{L+1})` has characteristic polynomial `char_1 = x² − 2x + 2`, with eigenvalues `1 ± i`.[^1] Its values wander and never repeat:

```
P(1,L) = 1, 0, −2, −4, −4, 0, 8, 16, …     (aperiodic over ℚ)
```

The eigenvalue `1+i` has `|1+i| = √2 ≠ 1`, so its powers spiral out to infinity: no period.

## Step 2 — Mod 5: the eigenvalue becomes a root of unity

Reduce mod 5. Does `i = √(−1)` exist in `F_5`? We need `i² = −1 ≡ 4`, and `2² = 4` — so **yes**: `i = ±2`, and the eigenvalues `1±i` become `1±2 = 3, 4`, plain elements of `F_5`.

Now the key fact: the nonzero elements `F_5^* = {1, 2, 3, 4}` form a **cyclic group of order 4** under multiplication, so `3⁴ = 1` and `4² = 1`. The eigenvalue powers `3^L` (period 4) and `4^L` (period 2) combine to give

```
P(1,L) mod 5 = 1, 0, 3, 1, 1, 0, 3, 1, …    (period 4 = lcm(4, 2))
```

The aperiodic sequence became periodic the moment its eigenvalues landed in a finite group.

## Step 3 — Mod 7: adjoining a square root

Mod 7, `−1 ≡ 6` is **not** a square (the squares are `{1, 2, 4}`), so `i ∉ F_7`. We adjoin it — exactly as one adjoins `√(−1)` to ℝ to build ℂ — giving the field `F_7[i] = F_{7²} = F_49`, with `7² = 49` elements. The eigenvalues `1±i` live there, and `F_49^*` is a cyclic group of order `49 − 1 = 48`, so each eigenvalue has order dividing 48 (in fact 24):

```
P(1,L) mod 7  has period 24.
```

The lesson: **the degree of the extension is the degree of the irreducible factor.** A quadratic that splits puts its roots in `F_p` (order dividing `p−1`); a quadratic that doesn't split puts them in `F_{p²}` (order dividing `p²−1`).

## Step 4 — The general rule: F_{p^d}

Reduce `char_k` mod p and factor it into irreducibles. An irreducible factor `g` of degree `d` has its `d` roots in the unique field `F_{p^d}` with `p^d` elements. Its nonzero elements `F_{p^d}^*` form a cyclic group of order `p^d − 1`, so by Lagrange every element's order divides the group order:

1. each eigenvalue has finite order dividing `p^d − 1`;
2. `λ^L` is periodic with period `ord(λ)`;
3. the sequence's period is the **lcm** of these orders.

This is the entire mechanism behind the [[mod-p-observatory](pages/mod-p-observatory.md)]: `period = lcm of eigenvalue orders`, each order dividing some `p^d − 1`.

## Step 5 — The real power

From this one picture, everything about the mod-p periods follows:

- **Splitting = the degree `d`.** A factor that splits has `d = 1` (roots in `F_p`, orders dividing `p−1`); one that stays quadratic has `d = 2` (roots in `F_{p²}`, orders dividing `p²−1`); and so on. For `char_1 = x²−2x+2` the decision is quadratic reciprocity: it splits iff `−1` is a square mod p, i.e. **`p ≡ 1 (mod 4)`** — so it splits mod 5 but stays irreducible mod 3 and 7.

- **Repeated roots add a factor p.** A repeated factor `g^m` contributes a solution term `n^{m−1}λ^n`; the polynomial part `n^{m−1}` is periodic mod p with period `p`, so a double root multiplies the period by p (`char_2 mod 7` has `(x+3)²`, hence `F(w,4) mod 7` has period `8400 = 1200 × 7`).

- **Primitive roots give the maximal period.** If a root is a *generator* of `F_{p^d}^*` (a primitive element), its order is the full `p^d − 1`. For an irreducible `char_k` of degree `k+1` that is `p^{k+1} − 1` — the reason the period of `F(w,h) mod p` can reach `~p^h`, and why the `10^9+7` observatory can *name* the orders but never *print* a period.

So the finite field does all the work: it replaces "infinite-order complex eigenvalue" with "element of a cyclic group," and periodicity is the automatic consequence.

## Appearances in Sources

- [[oeis-mining-pe502](pages/oeis-mining-pe502.md)] — the `char_k` family and `P(1,L) = Re((1+i)^{L+1})`.

## Related Concepts

- [[mod-p-observatory](pages/mod-p-observatory.md)] — the periods this field structure produces.
- [[generating-function-gallery](pages/generating-function-gallery.md)] — the `char_k` polynomials whose roots reduce mod p.
- [[signed-tower-count](pages/signed-tower-count.md)] — `P(1,L) = Re((1+i)^{L+1})` over ℚ.

## Footnotes

[^1]: [[oeis-mining-pe502](pages/oeis-mining-pe502.md)] `mine-notes.md` §"Vein 1" L19-37 [synthesis] — "P(1,L) = Re((1+i)^{L+1}) = A146559(L+1)" and the `char_k` family ("P(1): x^2 - 2x + 2 ...").
