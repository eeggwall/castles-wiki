---
title: Block-count constraints: a trichotomy
category: Concepts
summary: Three ways to select castles by block count — residue classes (roots of unity), sparse sets (lacunary series), and numerical semigroups (coin-change series) — all extractions from one generating function G(z).
tags: [concept, castle, generating-functions, roots-of-unity, coin-problem, pedagogy]
sources: [project-euler-502-castle-factoring]
created: 2026-09-14
updated: 2026-09-14
---

# Block-count constraints: a trichotomy

## The one object

Every "count the castles whose block count satisfies …" is an extraction from a single generating function. Let

```
G_{k,L}(z) = Σ_{towers of height ≤ k, length L} z^{blocks}.
```

The block count of a tower is its number of runs (sub-blocks), so for height ≤ 1 (binary strings) this is `G_{1,L}(z) = Σ_r C(L+1, 2r) z^r`. Set `z = 1` and you get the unsigned count `T`; set `z = −1` and you get the signed count `P`.[^1] The three methods below are three ways to *extract a subset* from `G`, and the right method is decided entirely by the **shape of the set S** of allowed block counts:

| shape of S | tool | example |
|---|---|---|
| **residue class** (or finite union, mod m) | roots of unity | even; divisible by 7; ≡ 3 mod 4 |
| **sparse set** (thin, no period) | lacunary series | powers of 2; squares |
| **numerical semigroup** (coin denominations) | coin-change series + constant term | `{5,7}`; `{5,10,25}` |

Call it the **residue / sparse / semigroup trichotomy.**

## 1. Residue constraints — roots of unity

**General construction.** The indicator `[b ≡ r (mod m)]` is the character sum `(1/m) Σ_j ω^{j(b−r)}` with `ω = e^{2πi/m}`. Substituting into `Σ_b [z^b]G · [b ≡ r]` and interchanging the sums gives

```
# { blocks ≡ r (mod m) } = (1/m) Σ_{j=0}^{m−1} ω^{−jr} · G(ω^j).
```

**Why it trims.** Character orthogonality `(1/m) Σ_j ω^{j(b−r)}` is `1` exactly when `b ≡ r` and `0` otherwise — so evaluating `G` at the `m` roots of unity and averaging *cancels* every block count outside the chosen residue class. (Full treatment on [[parity-via-roots-of-unity](pages/parity-via-roots-of-unity.md)].)

**Simple case (reduces).** `m = 2`, `ω = −1`: `# { even } = ½(G(1) + G(−1)) = (T+P)/2` and `# { odd } = (T−P)/2` — the two evaluations are the unsigned and signed counts themselves.

**Less simple.** `m = 4`, `ω = i`: `# { not divisible by 4 } = T − ¼(G(1)+G(i)+G(−1)+G(−i)) = (3T − P − 2·Re(G(i)))/4` — one genuinely new value, the real part `Re(G(i))`, beyond `T` and `P`.

## 2. Sparse constraints — lacunary series

**General construction.** For a thin set `S` with no period (powers of 2, squares), the indicator has no character decomposition, so you extract coefficients directly against the **lacunary** series `L(z) = Σ_{b ∈ S} z^b`:

```
# { blocks ∈ S } = Σ_{b ∈ S} [z^b] G(z) = [z^0] G(z) · L(1/z).
```

**Why it trims.** `L(z)` has coefficient `1` on `S` and `0` everywhere else, so the dot product of coefficient sequences (the `z^0` term of `G·L(1/z)`) keeps only the `b ∈ S` terms.

**Simple case (reduces).** `S = {1}` (exactly one block): `# = [z^1]G`. For height ≤ 1 that is `C(L+1, 2) = (L+1)L/2` towers.

**Less simple.** `S = {1, 2, 4, 8, …}` (powers of 2): `# = Σ_k [z^{2^k}] G`, i.e. dot `G` against `z + z² + z⁴ + z⁸ + ⋯`. There is no roots-of-unity shortcut — this is the honest generating-function answer, and the lacunary series is what makes it hard. (Concretely: height ≤ 1, length 4, runs are `{0,1,2}` with counts `1, 10, 5`, so "blocks a power of 2" = runs `{1,2}` = 15 towers.)

## 3. Semigroup constraints — coin-change series

**General construction.** "Blocks is a nonnegative combination of denominations `D`" means `blocks ∈ ⟨D⟩`, a numerical semigroup. Its indicator is a coefficient of the **coin-change** generating function

```
C(z) = ∏_{d ∈ D} 1/(1 − z^d),      so      [b ∈ ⟨D⟩] = [z^b] C(z)  (a count ≥ 1 iff representable).
```

Then the count is the **Hadamard product** — the constant term of `G` against `C`:

```
# { blocks ∈ ⟨D⟩ } = Σ_b [z^b]G · [z^b]C = [z^0] G(z) · C(1/z).
```

**Why it trims.** `[z^b]C` is the number of ways to make change for `b`, which is positive exactly on the semigroup — so `[z^0] G·C(1/z)` sums only the block counts that are representable.

**Simple case (reduces).** `D = {5}`: `C(z) = 1/(1−z⁵)`, so `[b ∈ ⟨5⟩] = [5 | b]`. The semigroup `5ℤ` *is* the residue class `0 mod 5`, and the coin method collapses back to `(1/5) Σ_j G(ω^j)`. This is precisely why "divisible by 5, 10, 25, 50, or 100" is a residue condition, not a coin problem — all those denominations share the divisor 5.

**Less simple.** `D = {5, 7}`: `C(z) = 1/((1−z⁵)(1−z⁷))`, and `⟨5,7⟩ = {0, 5, 7, 10, 12, 14, 15, …}` has Frobenius number `5·7−5−7 = 23` (every integer ≥ 24 is representable, 23 is not). This is *not* a finite union of residue classes, so the constant term `[z^0] G(z)/((1−z⁻⁵)(1−z⁻⁷))` is the only handle. (Concretely: height ≤ 1, length 10, runs are `{0,1,2,3,4,5}` with counts `C(11, 2r)`, and `⟨5,7⟩ ∩ {0..5} = {0,5}`, so the count is `C(11,0) + C(11,10) = 1 + 11 = 12`.)

## The boundary, restated

Look at the **shape of S** and pick the tool:

- **periodic / residue** → roots of unity (a finite character sum);
- **thin, no period** → lacunary series (coefficient extraction);
- **additively closed (coin denominations)** → coin-change series (constant term).

A coin semigroup *degenerates* to a residue class exactly when `gcd(D)` is itself one of the denominations (so the semigroup is a single arithmetic progression) — that is when a "coin problem" quietly turns back into a character sum. Otherwise it genuinely needs the generating function.

## Appearances in Sources

- [[project-euler-502-castle-factoring](pages/project-euler-502-castle-factoring.md)] — the sign and the signed count `P = G(−1)` that the residue method's `m=2` case uses.

## Related Concepts

- [[parity-via-roots-of-unity](pages/parity-via-roots-of-unity.md)] — the residue method in full (the character-sum machinery).
- [[castle-sign](pages/castle-sign.md)] — the `m=2` sign `(−1)^blocks`.
- [[tower-recursion-master-class](pages/tower-recursion-master-class.md)] — where `G(z)` comes from (the tower recursion).
- [[generating-functions](pages/generating-functions.md)] — the coefficient-extraction toolkit the sparse and coin methods use.

## Footnotes

[^1]: [[project-euler-502-castle-factoring](pages/project-euler-502-castle-factoring.md)] §"The sign of a castle" L92-123 — the sign `s(C) = (−1)^{blocks}` and the signed total `P = Σ (−1)^{blocks}`, i.e. `G(−1)`; `G(1) = T` is the unsigned tower count.
