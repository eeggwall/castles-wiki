---
title: Castle entropy
category: Concepts
summary: How much information a castle carries, in two senses that agree — uniform entropy log₂ F(w,h) ≈ w·log₂ h − 1 (the even-parity constraint is worth exactly one bit), and entropy rate log₂ ρ (every growth constant the wiki has catalogued — metallic, plastic, tribonacci — is a topological entropy in disguise).
tags: [concept, castle, entropy, information-theory, counting, growth-constant, metallic-means, parity, pedagogy]
sources: [oeis-mining-pe502, project-euler-502-solution]
created: 2026-09-18
updated: 2026-09-19
---

# Castle entropy

## The question

How much information does a castle carry? Two precise senses, and they agree in the limit:

- **Uniform entropy.** If every valid castle of width `w` and exact height `h` is equally likely, one castle is worth `H(w,h) = log₂ F(w,h)` bits, where `F(w,h)` is the even-block count Project Euler 502 (PE 502) asks for ([[castle-counting-function](pages/castle-counting-function.md)], [[castle-counting-formula](pages/castle-counting-formula.md)]).
- **Entropy rate.** A castle *family* defined by a rule is a shift whose transfer matrix has Perron root `ρ` (its growth constant); the entropy rate is `log₂ ρ`.

The two coincide: fix `h` and grow `w`, and `(1/w)·log₂ F(w,h) → log₂ h`, which is exactly `log₂ ρ` for the unconstrained height-bounded family (`ρ = h`). The punchline: **every growth constant the wiki has catalogued is a topological entropy in disguise.**

## Uniform entropy: the parity is exactly one bit

The even-block count `F(w,h)` is the even half of the unsigned count `A(w,h) = h^w − (h−1)^w` (all castles, exact height `h`), split by the sign `P = Σ (−1)^blocks` ([[castle-sign](pages/castle-sign.md)]):[^1]

```
F(w,h) = (A(w,h) + P(w,h)) / 2,     with  |P| ≪ A  as  w → ∞.
```

`A` is the dominant term and `P` the subdominant signed sum, so in the limit

```
H(w,h) = log₂ F(w,h)  ≈  log₂ A − 1  ≈  w·log₂ h − 1.
```

Read it as: each column is one of `h` heights (`log₂ h` bits each, independent), and the even-block projector is worth **exactly one bit** — the `−1` is the price of the parity clause. Verified by brute force:[^2]

```
  w  h     F(w,h)     log₂ F    w·log₂ h − 1    residual
  8  2       120       6.907        7.000       −0.09
 12  2      2080      11.022       11.000       +0.02
 12  3    261615      17.997       18.020       −0.02
```

The residual is `log₂(1 + P/A)` — the subdominant sign — and it decays as `w` grows. The parity bit is exact in the limit, not merely approximate. (The `h = 3` row's `261615` is the twelfth term of [[new-sequence-fw3](pages/new-sequence-fw3.md)]; at `(w,h) = (13,10)`, `log₂ F ≈ 41.8` against `42.2`, the scale figure of [[project-euler-502-problem-setup](pages/project-euler-502-problem-setup.md)].)

## Entropy rate: log₂ of the growth constant

Drop the "exact height `h`" bookkeeping and ask about a family of castles of *growing width* under a fixed rule. Columns are a finite alphabet and the rule is a transition constraint, so the family is a shift; its transfer matrix `M` (0/1 for a hard constraint, nonnegative-integer for multiplicities) has a Perron root `ρ`, and the number of valid castles of width `w` grows as `ρ^w`. The entropy rate is

```
h(family) = lim_{w→∞} (1/w)·log₂(# valid castles of width w) = log₂ ρ.
```

This is the topological entropy of the constrained system, and it is the same number as the per-column uniform entropy above — both are `log₂ ρ`. Now read the Numbers Division through this lens: every growth constant it has pinned down is an entropy rate.[^3]

| family (rule) | growth constant ρ | entropy rate log₂ ρ |
|---|---|---|
| height-bounded skyline, no other rule | `h` | `log₂ h` |
| golden (`x² = x + 1`) | φ = 1.6180 | 0.694 bits/column |
| silver (`x² = 2x + 1`) | 1+√2 = 2.4142 | 1.272 |
| bronze | (3+√13)/2 = 3.3028 | 1.724 |
| copper (`δ₄ = φ³`) | 2+√5 = 4.2361 | 2.083 |
| plastic (`x³ = x + 1`) | ψ = 1.3247 | 0.406 |
| tribonacci (`x³ = x² + x + 1`) | t = 1.8393 | 0.879 |

The metallic ladder ([[metallic-means](pages/metallic-means.md)]), the plastic number ([[plastic-number](pages/plastic-number.md)]), and tribonacci ([[bounded-height-castles-nacci](pages/bounded-height-castles-nacci.md)]) are a ladder of entropies. A family of entropy rate `log₂ ρ` has `2^{w·log₂ ρ}` castles of width `w`; the growth constant *is* the base-2 measure of branching per column.

## Why the two senses are one

Uniform entropy and entropy rate are the same limit approached from two sides. Uniform entropy is a *finite* count's log (`log₂ F(w,h)`) that becomes a rate when divided by `w`; entropy rate is a *per-column* limit from the start. They meet because the transfer-matrix growth constant is the eigenvalue `ρ` that governs both the word count `~ ρ^w` and the per-column branching. The even-parity `−1` is a boundary correction — finite in size, so it vanishes in the rate — exactly as the signed sum `P` is subdominant to `A`.

## Related Concepts

- [[castle-counting-formula](pages/castle-counting-formula.md)] / [[castle-counting-function](pages/castle-counting-function.md)] — the exact `F(w,h)` whose log is the uniform entropy.
- [[castle-sign](pages/castle-sign.md)] — the `(A±P)/2` projector; the origin of the one-bit parity cost.
- [[castle-graph-spectral-radius](pages/castle-graph-spectral-radius.md)] — `λ₁(h) = h`, the Perron root behind `log₂ h`.
- [[metallic-means](pages/metallic-means.md)], [[plastic-number](pages/plastic-number.md)], [[bounded-height-castles-nacci](pages/bounded-height-castles-nacci.md)] — growth constants re-read as entropy rates.
- [[reachable-field-census](pages/reachable-field-census.md)], [[tower-spacing-castles](pages/tower-spacing-castles.md)], [[metallic-strip-realizability](pages/metallic-strip-realizability.md)] — the rule families whose Perron roots are the rungs of the entropy ladder.
- [[mod-p-observatory](pages/mod-p-observatory.md)] — the finite-field counterpart: growth/entropy over ℂ vs period/order mod p.
- [[castle-compression](pages/castle-compression.md)] — the dual view: entropy measures the information content, compression measures how cheaply it is written.
- [[song-as-castle](pages/song-as-castle.md)] - the parity bit measured at URL scale: `log₂ A(34,16) − log₂ F(34,16) = 1.000000`, and what the bit does not buy (a single-column corruption flips block parity only 44% of the time).
- [[castle-steganography](pages/castle-steganography.md)] - the parity bit as capacity: one message bit per castle, set with a one-cell edit at a strict local extremum, distribution unchanged.
- [[project-euler-502-observations](pages/project-euler-502-observations.md)] — the source's "the even-block clause is almost the entire difficulty," priced here at exactly one bit; [[project-euler-502-problem-setup](pages/project-euler-502-problem-setup.md)] — `F(13,10)` in bits.
- [[new-sequence-fw3](pages/new-sequence-fw3.md)] — `F(w,3)`, the sequence the `h = 3` row of the table is drawn from.
- [[aocp-permutations](pages/aocp-permutations.md)] — Stirling's `log₂ n! ≈ n·log₂ n − n·log₂ e`, the entropy of a uniform permutation, the permutation-side twin of `w·log₂ h − 1`.

## Appearances in Sources

- [[oeis-mining-pe502](pages/oeis-mining-pe502.md)] — the `P(k,·)` families and their growth constants, re-read here as entropy rates.
- [[project-euler-502-solution](pages/project-euler-502-solution.md)] — the `F(w,h)` count whose uniform entropy is `log₂ F`.

## Footnotes

[^1]: `F` even, `A − F` odd, so `P = Σ(−1)^blocks = F − (A−F) = 2F − A`, giving `F = (A + P)/2`. The projector on [[castle-sign](pages/castle-sign.md)] is the same `(T±P)/2` split stated in tower coordinates.
[^2]: Verified by execution (2026-09-18): brute-force `F(w,h)` via the [[castle-snippets](pages/castle-snippets.md)] `all_castles` + `blocks` predicates; the residual `log₂ F − (w·log₂ h − 1)` is `+0.022` at `(12,2)` and `−0.022` at `(12,3)`.
[^3]: Growth constants from [[metallic-means](pages/metallic-means.md)] and [[reachable-field-census](pages/reachable-field-census.md)]; `log₂` values computed to three places.
