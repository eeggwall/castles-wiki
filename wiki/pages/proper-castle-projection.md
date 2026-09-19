---
title: Do metallic growth constants survive the proper-castle projection
category: Analyses
summary: The metallic-strip-realizability counts are free-height strip counts (𝟙ᵀM^L𝟙); imposing the two proper PE-502 clauses — max_i c_i = h and the even-block parity (A±P)/2 — leaves the metallic growth constant δ_{h−1} invariant, but the exact sequences are new. The signed transfer matrix S_h (entries (−1)^max(0,b−a)·M[a][b]) has spectral radius strictly below δ_{h−1} (1.000 / 1.575 / 1.768 / 2.242 / 2.413 for h = 2..6 vs δ = 1.618 / 2.414 / 3.303 / 4.236 / 5.193), so the parity projector (A±P)/2 preserves the leading term. The even-block proper-castle counts by width are a new family with no OEIS match for h ≥ 3: bronze (h=4) 1, 7, 25, 70, 209, 697, 2390, 8169, …; copper (h=5) 0, 0, 10, 104, 604, 2836, 12630, 55668, …. Even the free counts are not the primary metallic sequences — silver → A001333 (Pell–Lucas) not A000129, bronze → A003688 not A006190, copper → A015448 (the Fibonacci trisection F_{3n+5}) not A001076 — so neither the free nor the projected counts reproduce Pell / A006190 / A001076.
tags: [analysis, castle, metallic-mean, growth-constant, transfer-matrix, perron-root, parity, even-block, proper-castle, bronze, copper, silver, new-sequence, oeis, sympy, verification]
sources: [pe502-pell-castle-strip, project-euler-502-castle-factoring]
created: 2026-09-18
updated: 2026-09-19
---

# Do metallic growth constants survive the proper-castle projection

## The question

[[metallic-strip-realizability](pages/metallic-strip-realizability.md)] realizes the whole metallic ladder from one rule — the **plateau-free-except-ceiling** strip (`M_h = J − D`, char poly `(x+1)^{h−2}(x² − (h−1)x − 1)`, Perron root `δ_{h−1}`) — but its counts are *free-height strip* counts `𝟙ᵀM_h^L𝟙`: a row of columns with heights in `{1, …, h}`, no ground boundary, no `max = h`, no block parity. A **proper PE-502 castle** imposes two extra clauses:[^1]

1. **`max_i c_i = h`** — the castle actually reaches the ceiling (height exactly `h`, not `≤ h`).
2. **the even-block parity** — `even = (A + P)/2` where `A` is the unsigned count and `P = Σ (−1)^{blocks(c)}` the [[castle-sign](pages/castle-sign.md)] signed count.

Growth constants should be invariant under these lower-order corrections, but the *exact* sequences — and their Online Encyclopedia of Integer Sequences (OEIS) identities — can change. This page works out the projected counts for the `J−D` ladder (bronze / copper / …) and asks whether the metallic OEIS sequences (Pell A000129, A006190, A001076, …) or new ones appear.

## The two projections, precisely

A proper castle under the `J−D` rule is a skyline `c = (c_1, …, c_w) ∈ {1,…,h}^w` with (i) `c_i ≠ c_{i+1}` unless both equal `h`, (ii) `max c = h`, (iii) `blocks(c)` even, where `blocks(c) = c_1 + Σ_{i≥2} max(0, c_i − c_{i−1})` is the total ascent from the implicit ground `c_0 = 0` ([[castle-sign](pages/castle-sign.md)], [[castle-snippets](pages/castle-snippets.md)]).

**Projection 1 — `max = h`.** Subtract the strips that never reach height `h`. A `J−D` strip avoiding `h` satisfies "differ unless both `= h`", and since `h` is unreachable that is just *plateau-free* (`c_i ≠ c_{i+1}`), transfer matrix `J_{h−1} − I_{h−1}` — **not** the `J−D` matrix at height `h−1` (whose ceiling exception would wrongly re-admit `(h−1, h−1)`). So

```
u_proper(w)  =  𝟙ᵀ M_h^{w−1} 𝟙  −  𝟙ᵀ (J_{h−1} − I_{h−1})^{w−1} 𝟙 .
```

**Projection 2 — parity.** The sign factorizes over the skyline: `(−1)^{blocks} = (−1)^{c_1} · Π (−1)^{max(0, c_i − c_{i−1})}`. So the signed count is `vᵀ S_h^{w−1} 𝟙` with start vector `v[a] = (−1)^{a+1}` and signed transfer matrix[^2]

```
S_h[a][b]  =  (−1)^{max(0, b−a)} · M_h[a][b].
```

Then `even(w) = (u_proper(w) + s_proper(w))/2`, `odd(w) = (u_proper(w) − s_proper(w))/2`, with `s_proper` the same subtraction applied to the signed counts.

## Finding 1 — growth is invariant

`char(M_h) = (x+1)^{h−2}(x² − (h−1)x − 1)` has Perron root `δ_{h−1}`. The signed matrix `S_h` is spectrally *subdominant* at every height:[^3]

| `h` | spectral radius `ρ(S_h)` | `δ_{h−1}` |
|---|---|---|
| 2 | 1.000 | 1.618 |
| 3 | 1.575 | 2.414 |
| 4 | 1.768 | 3.303 |
| 5 | 2.242 | 4.236 |
| 6 | 2.413 | 5.193 |

Since `ρ(S_h) < δ_{h−1}`, the signed count `P` is `o(A)`, and `(A ± P)/2` keeps the leading term `~ C·δ_{h−1}^w`. Numerically the even-count tail ratios converge to the metal: `h=3 → 2.41426`, `h=4 → 3.30279`, `h=5 → 4.23657`, `h=6 → 5.1958` (→ nickel `5.1926`).[^4] **The metallic growth constant survives both projections**, as the lower-order-correction reading predicts.

## Finding 2 — the projected sequences are new

The even-block proper-castle counts by width, for each rung:[^5]

| rung | `even(w)`, `w = 1..12` | OEIS |
|---|---|---|
| golden `h=2` | 1, 3, 4, 4, 5, 9, 17, 29, 46, 72, 115, 187 | *(short / degenerate)* |
| silver `h=3` | 0, 0, 3, 16, 44, 104, 265, 674, 1640, 3972, 9687, 23512 | none |
| bronze `h=4` | 1, 7, 25, 70, 209, 697, 2390, 8169, 27565, 91762, 303541, 1002841 | none |
| copper `h=5` | 0, 0, 10, 104, 604, 2836, 12630, 55668, 242744, 1047448, 4489986, 19175568 | none |
| nickel `h=6` | 1, 11, 66, 320, 1601, 8661, 47807, 261401, 1411224, 7537448, 39939391, 210495659 | none |

None of these (nor their unsigned / odd / signed companions) matches OEIS on 12 terms; the unsigned `max=h` counts are likewise new for `h ≥ 3` (e.g. bronze `1, 7, 31, 118, 421, 1453, 4924, 16513, …`).[^6] The `max=h` projection alone changes the characteristic polynomial by one factor:

```
char(unsigned proper)  =  (x+1)^{h−2} · (x² − (h−1)x − 1) · (x − (h−2)),
```

the extra `(x − (h−2))` coming from the `J−I` plateau-free subtraction; the parity projection then mixes in `S_h`'s degree-`h` characteristic polynomial, so the even sequence is `(A + P)/2` over two C-finite sequences with *different* denominators — generally a new, higher-order recurrence.

## Finding 3 — the free counts are companion metallic sequences, not primary

Even *before* the projection, the free strip count `𝟙ᵀM_h^L𝟙` is not the "primary" metallic sequence `x_n = a·x_{n−1} + x_{n−2}`, `x_0 = 0, x_1 = 1` (Pell A000129, A006190, A001076, A052918 — the sequences tabulated on [[metallic-means](pages/metallic-means.md)]). The all-ones boundary picks a different linear combination of `δ_{h−1}^w` and its conjugate, plus `(−1)^w` corrections from the `(x+1)^{h−2}` factor:[^7]

| rung | free strip count | OEIS | primary metallic sequence |
|---|---|---|---|
| golden `h=2` | 2, 3, 5, 8, 13, 21, 34, 55 | **A000045** (Fibonacci) | A000045 (Fibonacci) |
| silver `h=3` | 3, 7, 17, 41, 99, 239, 577 | **A001333** (Pell–Lucas) | A000129 (Pell) |
| bronze `h=4` | 4, 13, 43, 142, 469, 1549, 5116 | **A003688** | A006190 |
| copper `h=5` | 5, 21, 89, 377, 1597, 6765, 28657 | **A015448** (= `F_{3n+5}` trisection) | A001076 (= `F_{3n}/2`) |
| nickel `h=6` | 6, 31, 161, 836, 4341, 22541, 117046 | *no match* | A052918 |

Only golden (`h = 2`) has its free count equal to its primary metallic sequence. **Copper** is the instructive case: `δ_4 = φ³`, so the free count is `A015448 = F_{3n+5}`, the *unhalved* Fibonacci trisection — already *not* the halved trisection `A001076 = F_{3n}/2` that [[metallic-means](pages/metallic-means.md)] lists as copper's sequence. The `max=h` and parity projections scramble it further, so the copper even count (`0, 0, 10, 104, 604, …`) is not a clean decimation of anything familiar.

## Answer

**Growth constants survive; the metallic sequences do not.** The `J−D` ladder's metallic growth `δ_{h−1}` is unchanged by `max = h` and `(A ± P)/2`, because the signed matrix `S_h` is spectrally subdominant (Finding 1). But the *exact* sequences are a genuinely new family (Finding 2), and the metallic OEIS entries Pell A000129 / A006190 / A001076 / A052918 appear in neither the free nor the projected counts — only golden's Fibonacci survives (Finding 3). The even-block proper-castle rows above are OEIS **submission candidates**, and the natural next questions are whether any of them satisfy a recognizable low-order recurrence (Berlekamp–Massey on the `even` rows) or admit a bijection to a known object.

## Related Concepts

- [[metallic-strip-realizability](pages/metallic-strip-realizability.md)] — the free-height strip counts this page projects onto proper castles; the `J−D` rule and `M_h = J − D`.
- [[castle-sign](pages/castle-sign.md)] — the sign `s(C) = (−1)^{blocks}` and the `(A ± P)/2` parity projector applied here.
- [[metallic-means](pages/metallic-means.md)] — the ladder whose *primary* sequences (A000129, A006190, A001076, …) the projected counts fail to reproduce.
- [[castle-snippets-strips](pages/castle-snippets-strips.md)] — the `proper_even` snippet computing these counts.
- [[reachable-field-census](pages/reachable-field-census.md)] — the sibling census (which *fields* the strips reach), to which this is the *sequences* complement.
- [[castle-by-area](pages/castle-by-area.md)] / [[bounded-height-castles-nacci](pages/bounded-height-castles-nacci.md)] — the other "new sequence from a castle count" precedents, the pattern these rows follow.
- [[castle-classification-growth](pages/castle-classification-growth.md)] — Axis 8, the `<metal> <axis> growth castle` meta-classification these projected metallic-ladder rows populate.
- [[pell-castle-strip](pages/pell-castle-strip.md)] — the anchored 1-smooth height-3 strip, where Pell proper (A000129) does appear; the free `J − D` silver strip here lands on companion A001333 instead, and the boundary condition is the whole difference.
- [[aocp-generating-permutations-tuples](pages/aocp-generating-permutations-tuples.md)] — the exact even-block counts are checked by Algorithm M enumeration of `{1..h}^w` with the two proper-castle filters.

## Footnotes

[^1]: [[metallic-strip-realizability](pages/metallic-strip-realizability.md)] §"Open, sharpened" — "the honest castle count imposes `max_i c_i = h` and the even-block parity clause"; this page is that open item resolved.

[^2]: The sign convention matches [[castle-sign](pages/castle-sign.md)]: `blocks(c)` is the total ascent from `c_0 = 0`, `s(C) = (−1)^{blocks}`, and `(A + P)/2 = even` (verified by direct `blocks(c) % 2 == 0` brute force below).

[^3]: `S_h` is the signed transfer matrix; `ρ(S_h)` is its spectral radius. SymPy `charpoly` gives `char(S_2) = x²−x+1` (primitive 6th roots of unity — the golden signed count is period-6), `char(S_3) = x³−x²+x−3`, `char(S_4) = x⁴−x³+2x²−x+7`, `char(S_5) = x⁵−x⁴+2x³−6x²−3x−17`, `char(S_6) = x⁶−x⁵+3x⁴−2x³+19x²+19x+41`.

[^4]: Even-count tail ratios (24 terms) converge to `δ_{h−1}` from above; the subdominant correction decays like `(ρ(S_h)/δ_{h−1})^w`.

[^5]: Transfer-matrix values, cross-checked term-for-term against brute-force enumeration of all skylines `{1..h}^w` (filter `max = h`, `J−D` adjacency, `blocks % 2 == 0`) for `h ≤ 6`, `w ≤ 12` — exact match throughout.

[^6]: OEIS search (2026-09-18, `oeis.org` JSON search on 12 terms) returns no match for any projected row at `h ≥ 3`; the unsigned bronze row `1, 7, 31, 118, 421, 1453, …` and copper row `1, 9, 53, 269, 1273, 5793, …` are also unmatched. Sanity checks: Pell `1,2,5,12,29,70,169,408` → A000129; copper free `5,21,89,377,1597,6765` → A015448.

[^7]: Free strip counts are `𝟙ᵀ M_h^{L} 𝟙` (with `L = w−1`); OEIS identifications offset-exact: silver `3,7,17,41,99,239,577` = A001333 (Pell–Lucas), bronze `4,13,43,142,469,1549,5116` = A003688 (`a(n) = 3a(n−1) + a(n−2)`, `a(1)=1, a(2)=4`), copper `5,21,89,377,…` = A015448 (`a(n) = 4a(n−1) + a(n−2)`), matching the `F_{3n+5}` trisection exactly ([[metallic-strip-realizability](pages/metallic-strip-realizability.md)] Finding 3).
