---
title: Castle entropy
category: Concepts
summary: Two information measures for castles. The uniform entropy log₂ A^e(w, h) of one even-block castle is log₂ A(w, h) − 1 + log₂(1 + S/A), so the even-block condition costs one bit up to a correction that tends to 0 as w grows (for 2 ≤ h ≤ 16, computed); the estimate w·log₂ h − 1 carries a second correction from the height condition, 0.42 bits at (13, 10). The entropy rate of a family given by a transfer matrix is log₂ of its Perron root, in bits per column: log₂ h for all castles of height h, 0.694 for the Fibonacci castles, 1.272, 1.724 and 2.083 for the ridge castles of heights 3, 4, 5, 0.406 for the maximal castles.
tags: [concept, castle, entropy, information-theory, counting, growth-constant, metallic-means, parity, pedagogy]
sources: [project-euler-502-solution, oeis-mining-pe502]
created: 2026-09-18
updated: 2026-10-16
---

# Castle entropy

A uniform choice among `N` objects carries `log₂ N` bits. The wiki uses two measures of this kind for castles:

- the **uniform entropy** `H(w, h) = log₂ A^e(w, h)`, the information in one castle chosen uniformly among the castles of width `w` and height `h` with an even number of blocks. `A^e(w, h)` is the Project Euler 502 count, which the problem statement writes `F(w, h)` ([[castle-counting-function](pages/castle-counting-function.md)]);
- the **entropy rate** `log₂ ρ` of a family of skylines defined by a rule on neighboring columns, where `ρ` is the Perron root of the rule's transfer matrix, in bits per column (section *Entropy rate*).

## Uniform entropy and the parity bit

Write `A(w, h) = h^w − (h−1)^w` for all castles of width `w` and height `h`, and `S(w, h) = A^e(w, h) − A^o(w, h)` for the signed count, so that `A^e = (A + S)/2` ([[castle-sign](pages/castle-sign.md)]). Then[^1]

```
log₂ A^e(w, h)  =  log₂ A(w, h) − 1 + log₂(1 + S(w, h)/A(w, h))              (1)
log₂ A(w, h)    =  w·log₂ h + log₂(1 − ((h−1)/h)^w)                          (2)
```

At fixed `h`, both corrections tend to 0 as `w` grows. In Equation (2) this is because `((h−1)/h)^w → 0`. In Equation (1), `S(w, h) = P(h−2, w) − P(h−1, w)` ([[castle-counting-formula](pages/castle-counting-formula.md)], Equation (7)), and `P(k, ·)` grows like the largest modulus of a root of its characteristic polynomial `char_k` ([[signed-tower-count](pages/signed-tower-count.md)]). For `k ≤ 15` that modulus is below `k + 1`: it is `√2` at `k = 1`, `2` at `k = 2` and `3.51` at `k = 6`.[^2] So for `2 ≤ h ≤ 16`, `S(w, h)/A(w, h) → 0` exponentially in `w`, and the even-block condition costs one bit, up to the correction `log₂(1 + S/A)`.

The estimate `w·log₂ h − 1` also drops the correction of Equation (2), which comes from the condition that some column reaches height `h`:[^3]

| `(w, h)` | `A^e(w, h)` | `log₂ A^e` | `log₂ A − 1` | `w·log₂ h − 1` | `S/A` |
|---|---|---|---|---|---|
| `(8, 2)` | 120 | 6.907 | 6.994 | 7.000 | `−5.9·10⁻²` |
| `(12, 2)` | 2 080 | 11.022 | 11.000 | 11.000 | `1.6·10⁻²` |
| `(12, 3)` | 261 615 | 17.997 | 18.008 | 18.020 | `−7.8·10⁻³` |
| `(13, 10)` | 3 729 050 610 636 | 41.762 | 41.762 | 42.185 | `−4.4·10⁻⁶` |
| `(40, 3)` | 6 078 831 630 016 984 399 | 62.398 | 62.398 | 62.399 | `−9.0·10⁻⁸` |

At `(13, 10)` the parity correction is below `10⁻⁵` bits, while `log₂(1 − 0.9^{13}) = −0.42` bits.

## Entropy rate

A rule on neighboring columns, with 0/1 transfer matrix `M` on the heights `{1, …, h}`, allows `N(w) = 𝟙ᵀ M^{w−1} 𝟙` skylines of width `w`, where `𝟙` is the all-ones vector ([[castle-strip](pages/castle-strip.md)]). The infinite sequences that obey such a rule form a shift of finite type, a set of sequences over a finite alphabet defined by forbidding finitely many blocks of letters, and its entropy rate is

```
lim_{w→∞} (1/w)·log₂ N(w)  =  log₂ ρ(M),                                     (3)
```

where `ρ(M)` is the Perron root of `M`, its largest eigenvalue, which is real and nonnegative for a nonnegative matrix. Equation (3) holds because `N(w)` is the sum of the entries of `M^{w−1}`, which for a nonnegative matrix is a matrix norm, and by Gelfand's formula the `n`-th root of any matrix norm of `M^n` tends to the spectral radius `ρ(M)`.

For the families below, the castles, the skylines of the rule that reach the top height, have the same growth by width as all the skylines of the rule.[^4]

| family | castles of width `w` | growth by width `ρ` | `log₂ ρ`, bits per column |
|---|---|---|---|
| all castles of height `h` | `h^w − (h−1)^w` | `h` | `log₂ h` |
| Fibonacci castles, height 2 ([[fibonacci-castle](pages/fibonacci-castle.md)]) | `F_{w+2} − 1` | golden, `φ = 1.6180` | 0.694 |
| ridge castles, height 3 ([[ridge-castle](pages/ridge-castle.md)]) | `𝟙ᵀR_3^{w−1}𝟙 − 2` | silver, `1 + √2 = 2.4142` | 1.272 |
| ridge castles, height 4 | `𝟙ᵀR_4^{w−1}𝟙 − 3·2^{w−1}` | bronze, `(3 + √13)/2 = 3.3028` | 1.724 |
| ridge castles, height 5 | `𝟙ᵀR_5^{w−1}𝟙 − 4·3^{w−1}` | `δ_4 = 2 + √5 = φ³ = 4.2361` | 2.083 |
| maximal castles, height 2 ([[fibonacci-castles-sub-families](pages/fibonacci-castles-sub-families.md)]) | `A000931(w + 6)` | plastic, `ψ = 1.3247` | 0.406 |

Here `R_h` is the ridge rule's transfer matrix, `F_n` the Fibonacci numbers, and `A000931` the Padovan numbers; `ψ` is the real root of `ψ³ = ψ + 1` ([[plastic-number](pages/plastic-number.md)]), and the metallic means `δ_a` are on [[metallic-means](pages/metallic-means.md)].

A growth constant along another axis is not a rate per column. Counted by area, the castles of height 3 grow like the tribonacci constant `τ = 1.8393`, the real root of `τ³ = τ² + τ + 1`, which is `log₂ τ = 0.879` bits per cell ([[exact-height-castle-by-area](pages/exact-height-castle-by-area.md)]); counted by semi-perimeter, all castles grow like `τ²` ([[castle-perimeter](pages/castle-perimeter.md)]).

The two measures meet for the family of all castles of height `h`: by Equations (1) and (2), `(1/w)·log₂ A^e(w, h) → log₂ h`, its entropy rate, and the parity bit contributes `−1/w` to the rate.

## Appearances in Sources

- [[project-euler-502-solution](pages/project-euler-502-solution.md)] - the counts `A(w, h)` and `F(w, h)`, the wiki's `A^e(w, h)`, and the formula through `P(h−1, w)` and `P(h−2, w)`.
- [[oeis-mining-pe502](pages/oeis-mining-pe502.md)] - the characteristic polynomials `char_1` to `char_5` of the signed tower counts.

## Related Concepts

- [[one-bit-seminar](pages/one-bit-seminar.md)] - a seminar on the even-block condition as one bit: in aggregate, for a single castle, under noise and as a channel.
- [[castle-conditional-entropy](pages/castle-conditional-entropy.md)] - the uniform entropy conditioned on the block count and the area, which together remove about `log₂ w + c(h)` bits, with `c(h)` computed for `h = 3, 4, 5`.
- [[castle-sign](pages/castle-sign.md)] - the split `A^e, A^o = (A ± S)/2` behind Equation (1).
- [[signed-tower-count](pages/signed-tower-count.md)] - the characteristic polynomials `char_k` and their roots of largest modulus.
- [[castle-strip](pages/castle-strip.md)] - transfer matrices, strip counts and Perron roots.
- [[castle-graph-spectral-radius](pages/castle-graph-spectral-radius.md)] - the growth constant `h` of `A^e(·, h)`, against the eigenvalues of the signed transfer matrix.
- [[metallic-means](pages/metallic-means.md)], [[plastic-number](pages/plastic-number.md)], [[exact-height-castle-by-area](pages/exact-height-castle-by-area.md)] - the growth constants of the tables.
- [[reachable-field-census](pages/reachable-field-census.md)], [[metallic-strip-realizability](pages/metallic-strip-realizability.md)], [[tower-spacing-castles](pages/tower-spacing-castles.md)] - the Perron roots of strip rules, and so their entropy rates.
- [[castle-compression](pages/castle-compression.md)] - how short a description of a castle can be, against how many bits a uniform castle carries.
- [[song-as-castle](pages/song-as-castle.md)] - the parity bit at `(17, 16)`, where `log₂ A − log₂ A^e` agrees with 1 to six decimal places, and the probability 0.4272 that a uniform one-column edit of a uniform castle changes the block parity (0.4236 if the edit must keep the height).
- [[castle-steganography](pages/castle-steganography.md)] - one message bit per castle, set by a one-cell edit at a strict local maximum or minimum, which changes the block count by one.
- [[castle-cryptography-round-two](pages/castle-cryptography-round-two.md)] - linear complexity: a product of `e` shifted terms of a recurrence of order `d` satisfies a recurrence of order at most `C(d + e − 1, e)`.
- [[project-euler-502-problem-setup](pages/project-euler-502-problem-setup.md)] - `log₂ A^e(13, 10) = 41.8` bits, the size argument against enumeration.
- [[new-sequence-fw3](pages/new-sequence-fw3.md)] - the row `A^e(·, 3)`, which contains the `(12, 3)` entry of the first table.
- [[mod-p-observatory](pages/mod-p-observatory.md)] - the periods of `A^e(w, h)` modulo a prime, set by the orders of the roots of `char_k` modulo `p`.
- [[aocp-permutations](pages/aocp-permutations.md)] - Stirling's formula, which gives the uniform entropy `log₂ n! ≈ n·log₂ n − n·log₂ e` of a permutation of `n` points.
- [[castle-notation](pages/castle-notation.md)] - the symbols `A`, `A^e`, `A^o`, `S` and `P`.

## Footnotes

[^1]: Equation (1) is the logarithm of `A^e = (A + S)/2 = (A/2)(1 + S/A)`, and Equation (2) the logarithm of `h^w − (h−1)^w = h^w (1 − ((h−1)/h)^w)`.
[^2]: Verified by execution (Python 3.11 with SymPy and NumPy, 2026-10-16): the largest root modulus of `char_k` for `k = 1, …, 15` is `1.414, 2.000, 2.193, 2.796, 2.892, 3.510, 3.541, 4.174, 4.156, 4.804, 4.746, 5.409, 5.315, 5.994, 5.868`, each below `k + 1`.
[^3]: Verified by execution (Python 3.11, 2026-10-16): `A^e(w, h)` from the formula of [[castle-counting-formula](pages/castle-counting-formula.md)] with `P` from the column-height dynamic program; the entries at `(8, 2)`, `(12, 2)` and `(12, 3)` also by enumeration of all skylines.
[^4]: Verified by execution (Python 3.11, 2026-10-16): the ridge counts against enumeration for `2 ≤ h ≤ 5`, `w ≤ 7`, and the characteristic polynomial `(x + 1)^{h−2}(x² − (h−1)x − 1)` of `R_h`; the maximal castles of height 2 against `A000931(w + 6)` for `w ≤ 14`; the base-2 logarithms to three decimal places.
