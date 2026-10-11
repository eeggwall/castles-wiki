---
title: Growth constants by semi-perimeter
category: Analyses
summary: Count castle strips (a 0/1 rule saying which column heights may follow which) by semi-perimeter s = width + blocks and ask which growth constants appear and at what smallest height. The denominator is det(I − M(x)) with a step from height a to height b weighted x^(1 + max(0, b − a)). Exact census through height 4 - 2, 34 and 2,106 new constants at heights 2, 3, 4. Supergolden and ψ² first appear at height 2, golden, plastic and tribonacci at 3, silver at 5 (601 of the 2^25 rules, confirmed exactly), and bronze cannot appear below height 22 - all castles of height at most 21 grow more slowly than bronze by semi-perimeter - so it is open. Castles using only two heights d apart grow at the root of (y − 1)² y^d = 1: ψ² at d = 1, golden at 2, supergolden at 4, plastic at 8, never silver or bronze. A natural silver family is height 5 with no 1 next to a 2 and no 4 next to a 5.
tags: [analysis, castle, castle-strip, semi-perimeter, perimeter, generating-function, transfer-matrix, growth-constant, census, exhaustive-search, min-height, metallic-means, plastic-number, supergolden, golden-ratio, silver-ratio, bronze, oeis, sympy, verification]
sources: [project-euler-502]
created: 2026-10-11
updated: 2026-10-11
---

# Growth constants by semi-perimeter

## The question in plain words

A castle's **semi-perimeter** is half the length of its outline, `s = w + #blocks` (width plus block count, [[castle-perimeter](pages/castle-perimeter.md)]). All castles together grow like `τ²^s` with `τ² ≈ 3.383` (`τ` the tribonacci constant). This page restricts the castles by a **rule**, a 0/1 table saying which column height may follow which ([[castle-strip](pages/castle-strip.md)]), and asks which growth constants the count by semi-perimeter can have, and at what smallest height each first appears. It is the semi-perimeter counterpart of [[area-growth-census](pages/area-growth-census.md)] (area) and [[quadratic-min-height](pages/quadratic-min-height.md)] (width).

## Terms used on this page

- **Semi-perimeter** `s`. Reading left to right with `c_0 = 0`, the block count grows by `max(0, c_i − c_{i−1})` at each column, so a column of height `b` after one of height `a` adds `1 + max(0, b − a)` to `s`.
- **Growth constant** - the number `g` with the count growing like `g^s`; it is `1/x*`, where `x*` is the smallest positive root of the denominator below.
- **Height of a rule** - the number `h` of column heights `1..h` it uses.

## The generating function

Weight the step from height `a` to height `b` by `x^(1 + max(0, b − a))`. The strips counted by semi-perimeter have denominator

```
det( I − M(x) ),     M[a][b] = (1 if b may follow a, else 0) · x^(1 + max(0, b − a)).
```

Requiring the castle to reach height `h` subtracts the strips that stay below it, which never grow faster; the census below lists the growth of the full rule, and for every family named on this page the castles that reach height `h` were counted directly and grow at the same rate.[^exec]

## The census through height 4

Every rule on 1 to 4 heights (2, 16, 512 and 65,536 rules) was expanded exactly, the distinct denominators factored, and the factor carrying `x*` reversed to give the minimal polynomial of the growth constant.[^exec]

| height | distinct denominators | new growth constants | degrees of the new constants | smallest new | largest |
|---|---|---|---|---|---|
| 1 | 2 | 1 (growth 1) | 1 | `1` | `1` |
| 2 | 6 | 2 | 3, 3 | `1.465571` (supergolden) | `1.754878` (`ψ²`) |
| 3 | 58 | 34 | 1, 2, 3 (6), 4 (6), 5 (20) | `1.167304` (`z⁵ − z − 1`) | `2.205569` (`z³ − 2z² − 1`) |
| 4 | 2,914 | 2,106 | 3 (6), 4 (34), 5 (152), 6 (400), 7 (708), 8 (806) | `1.104873` (`z⁸ − z² − 1`) | `2.494691` |

Height 2 gives only supergolden (`z³ − z² − 1`, the rule "no two adjacent 1s" or "no two adjacent 2s") and `ψ²` (`z³ − 2z² + z − 1`, all castles of height 2). Height 3 adds golden, the plastic number `ψ` (`z³ − z − 1`), tribonacci (`z³ − z² − z − 1`), `2^{1/3}`, `2`, and the real root `2.2056` of `z³ = 2z² + 1`, which is the growth of all castles of height 3.

## The ceiling at each height

A rule at height `h` counts a subset of the castles of height at most `h`, so its growth is at most that of all castles of exact height `h`. That ceiling rises with `h` towards `τ² ≈ 3.383`:[^exec]

| `h` | 2 | 3 | 4 | 5 | 6 | 8 | 10 | 15 | 20 | 21 | 22 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| all castles of height `h` | `1.7549` | `2.2056` | `2.4947` | `2.6902` | `2.8281` | `3.0046` | `3.1087` | `3.2374` | `3.2930` | `3.3002` | `3.3066` |

**No family of castles of height at most 21 grows at bronze `(3 + √13)/2 = 3.3028` by semi-perimeter.** Every such family is a subset of the castles of height at most 21, whose growth is `3.3002`. At `x = 1/bronze` the spectral radius of `M(x)` for all castles of height 21 is `0.99866 < 1`, and for height 22 it is `1.00200 > 1`, both computed to 50 digits. Bronze is therefore possible only from height 22, where an exhaustive census is out of reach; whether it occurs is open. Silver `2.4142` is below the height-4 ceiling.

## The named constants and their first heights

| constant | value | first height | how many rules there | a family |
|---|---|---|---|---|
| supergolden | `1.4656` | 2 | - | ridge castles or Fibonacci castles of exact height 2 |
| `ψ²` | `1.7549` | 2 | 1 | all castles of exact height 2 |
| golden `φ` | `1.6180` | 3 | 26 | every column 1 or 3 |
| plastic `ψ` | `1.3247` | 3 | 10 | every column 1 or 9 (height 9; below) |
| tribonacci | `1.8393` | 3 | - | - |
| silver `1 + √2` | `2.4142` | 5 | 601 | exact height 5, no 1 next to a 2, no 4 next to a 5 |
| bronze `(3 + √13)/2` | `3.3028` | at least 22 | - | open |

The rule counts at heights 3 and 5 are from an exhaustive scan of all rules at that height; none of golden, plastic or silver occurs at a lower height.[^exec]

## Two-height castles

Castles whose columns take only two heights `a < b`, in any order, have a two-state rule; with `d = b − a` the denominator is `(1 − x)² − x^{d+2}`, so the growth `y` is the root above 1 of

```
(y − 1)² · y^d = 1.
```

It depends only on the gap `d`, and it falls as `d` grows:

| gap `d` | equation | growth |
|---|---|---|
| 1 | `y³ − 2y² + y − 1 = 0` | `ψ² = 1.7549` |
| 2 | `y² − y − 1 = 0` | golden |
| 4 | `y³ − y² − 1 = 0` | supergolden |
| 8 | `y⁵ − y⁴ − 1 = (y³ − y − 1)(y² − y + 1) = 0` | plastic |

For even `d = 2k` the equation is `(y − 1) y^k = 1`. The plastic case is the identity `ψ − 1 = 1/ψ⁴`, which follows from `ψ³ = ψ + 1`. So "every column 1 or 9" is a plastic family by semi-perimeter, as "every column 1 or 3" is a golden one. No two-height family is silver or bronze: the largest growth, at `d = 1`, is `ψ² < 1 + √2`.[^exec]

## Silver at height 5

Silver first appears at height 5: of the `2^25` rules, 601 grow at exactly `1 + √2`. Each was confirmed by exact division of its denominator by `1 − 2x − x²` and an exact count showing no smaller positive root.[^exec] The rule with the plainest description allows a step exactly when it allows the reverse step, so its castles are closed under reading right to left:

- **exact height 5; no column of height 1 next to one of height 2, and no column of height 4 next to one of height 5.** Example: `(3, 5, 3, 1, 4)`, semi-perimeter `5 + 3 + 2 + 3 = 13`.

Its denominator is `(1 − x)² (1 + x²)(1 − 2x − x²)(1 − x + x² + x³)`, up to sign, and its castles of exact height 5 number `1, 7, 26, 74, 196, 525, 1421, 3809, 10040, 26102, 67250` at `s = 6, …, 16` (no OEIS match, searched 2026-10-11). The ratios approach silver slowly (`2.426` near `s = 56`), because the castles of this rule that stay below height 5 grow at `2.3138`, close to silver.

## Open threads

1. **Bronze from height 22.** The ceiling allows it from height 22 on; a construction, or a reason no rule reaches it, is open.
2. **The census at height 5.** Silver is settled at height 5 by a targeted scan; the full list of constants first appearing at height 5 (33.5 million rules) is not done.
3. **The smallest constant at each height.** `1.4656`, `1.1673`, `1.1049` at heights 2, 3, 4 (roots of `z³ − z² − 1`, `z⁵ − z − 1`, `z⁸ − z² − 1`); a general form, like the area census's `z^T − z − 1`, is open.

## Related Concepts

- [[castle-perimeter](pages/castle-perimeter.md)] - the semi-perimeter, and all castles by semi-perimeter at `τ²`.
- [[area-growth-census](pages/area-growth-census.md)] - the same question by area.
- [[quadratic-min-height](pages/quadratic-min-height.md)] - the same question by width, for quadratic constants.
- [[golden-silver-bronze-plastic-castles](pages/golden-silver-bronze-plastic-castles.md)] - the four constants on every axis; this page fills its semi-perimeter row.
- [[metallic-means](pages/metallic-means.md)] - golden, silver, bronze.
- [[plastic-number](pages/plastic-number.md)] - `ψ`, `ψ²`.

## Footnotes

[^exec]: Verified by execution (2026-10-11): `bin/python/semi_perimeter_census.py`, run log `bin/python/semi_perimeter_census-run.log`. Census: every rule of size 1 to 4, denominator by exact Berkowitz determinant in SymPy, factor carrying the smallest positive root found by exact real-root isolation, minimal polynomial by reversal. Ceiling: growth of the all-ones rule by bisection on the spectral radius of `M(x)`; the bronze comparison at heights 21 and 22 in mpmath at 50 digits. Scans: all `2^(h²)` rules at heights 3, 4, 5 batched through `numpy.linalg.eigvals`, keeping spectral radius of `M(1/g)` within `10^{-7}` of 1 (26 golden and 10 plastic at height 3, 3,669 golden at height 4, no silver at height 4, 601 silver candidates at height 5); each silver candidate confirmed by exact division by `1 − 2x − x²` and `count_roots` on `[0, 0.41421356]`. Two-height denominators by `sp.factor`. Counts of the silver family by brute force for `s ≤ 16` and by transfer matrix to `s = 60`; castles of exact height 9 with every column 1 or 9 by transfer matrix to `s = 90` (ratio `1.32471` at `s = 89`).
