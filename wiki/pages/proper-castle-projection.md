---
title: From ridge strips to even-block ridge castles
category: Analyses
summary: The ridge strips of metallic-strip-realizability need not reach their ceiling h and carry no parity. Restricting to the ridge castles of height h and then to their even-block part keeps the growth constant δ_{h−1}, because the signed transfer matrix R̃_h has spectral radius below δ_{h−1} (1.000, 1.575, 1.768, 2.242, 2.413 against 1.618, 2.414, 3.303, 4.236, 5.193 for h = 2..6), so A^e_ridge = (A_ridge + S_ridge)/2 is half of A_ridge up to a smaller term. The even-block counts satisfy linear recurrences of order 4, 8, 10, 12, 14 for h = 2..6 (computed). The ridge strip counts are A001333(w+1), A003688(w+1), A015448(w+1), A015449(w+1) for h = 3..6, not the primary metallic sequences A000129, A006190, A001076, A052918; only h = 2 gives the Fibonacci numbers.
tags: [analysis, castle, ridge-castle, metallic-mean, growth-constant, transfer-matrix, perron-root, parity, even-block, bronze, silver, oeis, sympy, verification]
sources: [project-euler-502]
created: 2026-09-18
updated: 2026-10-16
---

# From ridge strips to even-block ridge castles

## The question

The ridge rule says that neighboring columns differ in height unless both have height `h`; its transfer matrix on the heights `1, …, h` is `R_h = J − D`, with `J` the all-ones matrix and `D = diag(1, …, 1, 0)`, characteristic polynomial `(x + 1)^{h−2}(x² − (h − 1)x − 1)` and Perron root `δ_{h−1}` ([[ridge-castle](pages/ridge-castle.md)], [[metallic-strip-realizability](pages/metallic-strip-realizability.md)]). [[metallic-strip-realizability](pages/metallic-strip-realizability.md)] counts ridge strips, `𝟙ᵀ R_h^{w−1} 𝟙` of width `w`. A strip need not reach height `h`, so a ridge strip is not a castle of height `h`, and it carries no block parity. The Project Euler castles of height `h` add two conditions: some column has height `h`, and the castle has an even number of blocks.[^1] This page asks whether the growth constant `δ_{h−1}` and the metallic sequences survive the two conditions.

*Example.* At `h = 3` and `w = 3` there are 17 ridge strips. Two of them, the skylines `(1, 2, 1)` and `(2, 1, 2)`, do not reach height 3, so they are not castles of height 3; the other 15 are the ridge castles of width 3 and height 3. Three of these have an even number of blocks: `(2, 1, 3)`, `(3, 1, 2)` and `(3, 2, 3)`, with 4 blocks each.

## The two restrictions

**Reaching height `h`.** A ridge strip that never reaches `h` has all heights in `{1, …, h − 1}`, where the ridge rule says that neighboring columns always differ. These plateau-free skylines number `(h − 1)(h − 2)^{w−1}`, so the ridge castles of height `h` number ([[ridge-castle](pages/ridge-castle.md)], Equation (3))

```
A_ridge(w, h)  =  𝟙ᵀ R_h^{w−1} 𝟙  −  (h − 1)(h − 2)^{w−1}.
```

**Parity.** The block count is the total rise `c_1 + Σ_{i≥2} max(0, c_i − c_{i−1})` ([[castle-sign](pages/castle-sign.md)]), so the sign `(−1)^{blocks}` factors over the steps. With the signed transfer matrix and start vector

```
R̃_h[a][b]  =  (−1)^{max(0, b − a)} · R_h[a][b],        v_a  =  (−1)^a,
```

the signed count of the ridge castles of height `h` is

```
S_ridge(w, h)  =  vᵀ R̃_h^{w−1} 𝟙  −  (the same signed sum over the plateau-free skylines on {1, …, h − 1}),
```

and the even-block and odd-block ridge castles number `A^e_ridge = (A_ridge + S_ridge)/2` and `A^o_ridge = (A_ridge − S_ridge)/2`.[^2]

## The growth constant survives

The spectral radius of `R̃_h` is below `δ_{h−1}` for `h ≤ 6` (computed):[^3]

| `h` | `ρ(R̃_h)` | `δ_{h−1}` |
|---|---|---|
| 2 | 1.000 | 1.618 |
| 3 | 1.575 | 2.414 |
| 4 | 1.768 | 3.303 |
| 5 | 2.242 | 4.236 |
| 6 | 2.413 | 5.193 |

The subtracted plateau-free terms grow at most like `(h − 2)^w < δ_{h−1}^w`. So `S_ridge(w, h)` is `o(A_ridge(w, h))`, and `A^e_ridge(w, h)` is `A_ridge(w, h)/2` up to a smaller term: the even-block ridge castles of height `h` are `δ_{h−1}` by width, like the ridge strips. At `w = 40` the ratios `A^e_ridge(40, h)/A^e_ridge(39, h)` are `2.41421`, `3.30278`, `4.23607`, `5.19263` for `h = 3, 4, 5, 6`.[^4]

## The counts

The even-block ridge castles of height `h`, by width:[^5]

| `h` | `A^e_ridge(w, h)`, `w = 1, …, 12` |
|---|---|
| 2 | 1, 3, 4, 4, 5, 9, 17, 29, 46, 72, 115, 187 |
| 3 | 0, 0, 3, 16, 44, 104, 265, 674, 1640, 3972, 9687, 23512 |
| 4 | 1, 7, 25, 70, 209, 697, 2390, 8169, 27565, 91762, 303541, 1002841 |
| 5 | 0, 0, 10, 104, 604, 2836, 12630, 55668, 242744, 1047448, 4489986, 19175568 |
| 6 | 1, 11, 66, 320, 1601, 8661, 47807, 261401, 1411224, 7537448, 39939391, 210495659 |

For `h ≥ 3`, `A_ridge(·, h)` satisfies the recurrence of order 3 with characteristic polynomial `(x² − (h − 1)x − 1)(x − (h − 2))` ([[ridge-castle](pages/ridge-castle.md)]); at `h = 4` it is `1, 7, 31, 118, 421, 1453, 4924, 16513, …`. The even-block counts `A^e_ridge(·, h)` satisfy linear recurrences of order 4, 8, 10, 12, 14 for `h = 2, …, 6` (Berlekamp-Massey on 60 terms, computed). Each characteristic polynomial contains the factors `x² − (h − 1)x − 1` and `char(R̃_h)`; at `h = 3` it is `(x − 1)(x² + 1)(x² − 2x − 1)(x³ − x² + x − 3)`.[^5] [[castle-sequence-catalogue](pages/castle-sequence-catalogue.md)] records the OEIS status of these rows.

## The ridge strips give the companion sequences

The ridge strip count `𝟙ᵀ R_h^{w−1} 𝟙` is not the primary metallic sequence `x_n = (h − 1)x_{n−1} + x_{n−2}`, `x_0 = 0`, `x_1 = 1`, of [[metallic-means](pages/metallic-means.md)]. `R_h` preserves the plane spanned by `𝟙` and `e_h` and acts on it with characteristic polynomial `x² − (h − 1)x − 1`, so the eigenvalue `−1` does not contribute and the ridge strips of width `w` number `x_{w+1} + x_w` ([[ridge-castle](pages/ridge-castle.md)]):[^6]

| `h` | ridge strips, `w = 1, 2, …` | OEIS | primary metallic sequence |
|---|---|---|---|
| 2 | 2, 3, 5, 8, 13, 21, 34 | `F_{w+2}`, A000045 | A000045, Fibonacci |
| 3 | 3, 7, 17, 41, 99, 239, 577 | `A001333(w + 1)`, Pell-Lucas | A000129, Pell |
| 4 | 4, 13, 43, 142, 469, 1549, 5116 | `A003688(w + 1)` | A006190 |
| 5 | 5, 21, 89, 377, 1597, 6765, 28657 | `A015448(w + 1) = F_{3w+2}` | A001076, `F_{3n}/2` |
| 6 | 6, 31, 161, 836, 4341, 22541, 117046 | `A015449(w + 1)` | A052918 |

Only at `h = 2` is the strip count a shift of the primary sequence. Neither the ridge strips nor the ridge castles of height `h ≥ 3` give A000129, A006190, A001076 or A052918; the Pell numbers `P⋆_w` appear instead as the anchored 1-smooth strips on `{1, 2, 3}` ([[pell-castle-strip](pages/pell-castle-strip.md)]).

## Related Concepts

- [[ridge-castle](pages/ridge-castle.md)] - the ridge rule, `A_ridge(w, h)`, `R̃_h` and the even-block table.
- [[metallic-strip-realizability](pages/metallic-strip-realizability.md)] - the ridge strips as the realization of every metallic mean `δ_a`, at height `a + 1`.
- [[castle-sign](pages/castle-sign.md)] - the sign `(−1)^{blocks}` and the split `A^e = (A + S)/2`.
- [[metallic-means](pages/metallic-means.md)] - the primary metallic sequences A000129, A006190, A001076, A052918.
- [[castle-snippets-strips](pages/castle-snippets-strips.md)] - the `proper_even` snippet, which computes `A^e_ridge(w, h)`.
- [[reachable-field-census](pages/reachable-field-census.md)] - the fields reached by the growth constants of strip rules.
- [[castle-classification-growth](pages/castle-classification-growth.md)] - growth types by width, by height and by area.
- [[pell-castle-strip](pages/pell-castle-strip.md)] - the anchored 1-smooth strips on `{1, 2, 3}`, counted by the Pell numbers; its free strips and the ridge strips of height 3 are both `A001333(w + 1)`.

## Footnotes

[^1]: [[project-euler-502](pages/project-euler-502.md)] §"Project 502: Castle Polyominoes" L19-20 - "The maximum achieved height of the entire castle is exactly h." and "The castle is made from an even number of blocks."
[^2]: The sign convention is that of [[castle-sign](pages/castle-sign.md)]: `blocks(c)` is the total rise from `c_0 = 0`, and the start vector carries the factor `(−1)^{c_1}`.
[^3]: Characteristic polynomials of the signed matrices (SymPy): `char(R̃_2) = x² − x + 1`, whose roots are primitive sixth roots of unity; `char(R̃_3) = x³ − x² + x − 3`; `char(R̃_4) = x⁴ − x³ + 2x² − x + 7`; `char(R̃_5) = x⁵ − x⁴ + 2x³ − 6x² − 3x − 17`; `char(R̃_6) = x⁶ − x⁵ + 3x⁴ − 2x³ + 19x² + 19x + 41`.
[^4]: Verified by execution (Python 3.11, 2026-10-16): the even-block counts by a dynamic program over (last height, whether `h` has been reached, block parity) for `w ≤ 40`, and their successive ratios.
[^5]: Verified by execution (Python 3.11 with SymPy, 2026-10-16): the table by the dynamic program for `w ≤ 12` and `2 ≤ h ≤ 6`, and against enumeration of all skylines in `{1, …, h}^w` (filter: the ridge rule, some column of height `h`, an even block count) for `h ≤ 4`, `w ≤ 7`; the characteristic polynomials of `R_h` and `R̃_h` and their spectral radii; the recurrences of `A_ridge` and `A^e_ridge` by Berlekamp-Massey on 60 terms (orders 3 and 4, 8, 10, 12, 14), with the factored characteristic polynomials.
[^6]: https://oeis.org/A001333, https://oeis.org/A003688, https://oeis.org/A015448, https://oeis.org/A015449 (read 2026-10-16) - A001333 "Pell-Lucas numbers: numerators of continued fraction convergents to sqrt(2)" (1, 1, 3, 7, 17, …); A003688 "a(n) = 3*a(n-1) + a(n-2), with a(1)=1 and a(2)=4" (1, 4, 13, 43, …); A015448 "a(0) = 1, a(1) = 1, and a(n) = 4*a(n-1) + a(n-2) for n >= 2" (1, 1, 5, 21, 89, …); A015449 "Expansion of (1-4*x)/(1-5*x-x^2)" (1, 1, 6, 31, 161, …). The strip counts recomputed from `𝟙ᵀ R_h^{w−1} 𝟙` for `w ≤ 7`.
