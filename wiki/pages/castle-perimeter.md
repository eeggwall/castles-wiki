---
title: Castle perimeter - blocks are the vertical half-perimeter
category: Analyses
summary: A castle's semi-perimeter is `w + #blocks`, so the block count is Delest-Viennot's perimeter statistic and PE 502's even-block clause is a perimeter parity. The minimum-block theorem is "perimeter = bounding-box perimeter iff convex". Castles by semi-perimeter are the bargraphs A082582 with growth `τ²` (τ the tribonacci constant), by (semi-perimeter, width) they are A271942, and the signed count has algebraic GF `(1 + t² - sqrt((1+t)(1 - t + 3t² + t³)))/(2t)` with growth only `τ`. Convex castles by semi-perimeter are Fibonacci (A001519), signed they are periodic with period 6. The even-block splits have no OEIS match.
tags: [analysis, castle, perimeter, blocks, parity, bargraph, generating-function, algebraic, tribonacci, fibonacci, delest-viennot, oeis, novel-candidate]
sources: [algebraic-languages-and-polyominoes-enumeration, project-euler-502-brute-force, tower-narayana-polynomial]
created: 2026-09-22
updated: 2026-09-22
---

# Castle perimeter - blocks are the vertical half-perimeter

## The identity

Read a castle as its skyline `c_1..c_w` (all `c_i ≥ 1`, `max c = h`). The block count is the total rise from the base,[^1]

```
#blocks = c_1 + Σ_{i≥2} max(0, c_i - c_{i-1}).
```

The castle is a bargraph polyomino ([[castle-polyomino](pages/castle-polyomino.md)]), so its boundary has `2w` horizontal unit edges (the base plus the tops) and `c_1 + c_w + Σ |c_i - c_{i+1}|` vertical ones. The vertical boundary walks from the base up to the skyline and back down, so the total fall equals the total rise, and the vertical length is twice the rise. Hence

```
perimeter = 2(w + #blocks),        semi-perimeter s = w + #blocks.
```

Checked by brute force for every skyline with `w, h ≤ 6` during this analysis. Three consequences:

- **The parity clause is a perimeter parity.** PE 502's `F(w,h)` counts the castles in the `w × h` box whose semi-perimeter has the same parity as `w`. The block-count distribution of a fixed `(w,h)` cell *is* its perimeter distribution, shifted by `w`.
- **The minimum-block theorem is the convexity-perimeter fact.** [[convex-castle-binomial-identity](pages/convex-castle-binomial-identity.md)] proves `#blocks ≥ h` with equality iff the skyline is unimodal. Adding `w`, this says `s ≥ w + h`: the perimeter is at least the bounding-box perimeter, with equality iff the castle is convex. That is the classical characterization of convex polyominoes, and it is why Delest and Viennot can say a convex polyomino's perimeter is its box's (own reasoning; the equivalence was re-checked for all skylines `w ≤ 6`, heights `≤ 5`).
- **The castle's natural enumeration variable is Delest-Viennot's.** Their paper grades by perimeter.[^2] For castles that grading is width times blocks, which is exactly the bivariate statistic the tower-Narayana identity already tracks.

## Castles by semi-perimeter

Stripping the base block gives a tower (heights `≥ 0`) with one block fewer, so castles of width `w` with `b` blocks number `T(w, b-1) = Σ_k N(w,k) C(b-1+w-k, w-1)` ([[tower-narayana-polynomial](pages/tower-narayana-polynomial.md)]).[^3] Sum over `w + b = s`. The Narayana generating function `G(u,y) = Σ_{w,k} N(w,k) u^w y^k` satisfies `G = u(y + G)(1 + G)`. With `u = x/(1-y)` (the `1/(1-x)^w` factor) and `x = y = t`, this gives

```
t B² - (1 - 2t - t²) B + t² = 0
B(t) = (1 - 2t - t² - sqrt(1 - 4t + 2t² + t⁴)) / (2t)
     = t² + 2t³ + 5t⁴ + 13t⁵ + 35t⁶ + 97t⁷ + 275t⁸ + 794t⁹ + ...
```

This is **A082582**, "the number of bargraphs of semiperimeter n". The triangle by (semi-perimeter, width) is **A271942**, "bargraphs of semiperimeter n having width k", whose entries are the tower-Narayana identity re-indexed: `A271942(s, w) = T(w, s-w-1)` (rows `s = 2..8` matched).[^4] Neither entry has the PE 502 castle reading or the tower form `Σ_k N(w,k) C(s-k-1, w-1)`. A271942's formulas are its bivariate GF (the same quadratic as `B` with width marked), a hypergeometric form, and a triple binomial sum. A082582 links Baril, Flórez and Ramírez, "Generalized Narayana arrays, restricted Dyck paths, and related bijections" (2025), which may contain the Narayana form (cited via the OEIS entry, not read). Status: interlink candidate.

**Growth `τ²`.** The discriminant factors as `(1-t)(t³ + t² + 3t - 1)`, and at `t = 1/y` the cubic becomes `-(y³ - 3y² - y - 1)`, the minimal polynomial of `τ²`, where `τ = 1.83928...` is the tribonacci constant (`τ³ = τ² + τ + 1`). So castles by semi-perimeter grow like `τ^{2s} s^{-3/2}` with `τ² = 3.38297...` (resultant computation during this analysis; coefficient ratio 3.29999 at `s = 60`, consistent with the `1 - 3/(2s)` square-root correction). Whether this is already stated in the bargraph literature was not checked.

## The parity split

Weight each block by `-1` (the castle sign), i.e. `y = -t`, `u = t/(1+t)`:

```
t B_s² - (1 + t²) B_s - t² = 0
B_s(t) = (1 + t² - sqrt((1+t)(1 - t + 3t² + t³))) / (2t)
       = -t² + t⁴ + t⁵ - t⁶ - 3t⁷ - t⁸ + 6t⁹ + 9t¹⁰ - 5t¹¹ - 29t¹² - 20t¹³ + 55t¹⁴ + ...
```

The even-block castles by semi-perimeter are `(B + B_s)/2`:

```
s = 2..16:   0, 1, 3, 7, 17, 47, 137, 400, 1168, 3450, 10338, 31311, 95521, 293169, 904999
```

Both series match a direct DP over skylines through `s = 30`. **No OEIS match** for the even sequence or for the signed sequence, under either sign convention or as absolute values (searched 2026-09-22): novel-candidates.

**The sign halves the exponent.** At `t = -1/y` the signed cubic `t³ + 3t² - t + 1` becomes `-(y³ + y² + 3y - 1)`, the unsigned cubic again. So the signed singularities are `-τ²` and a complex pair of modulus exactly `1/τ`. The signed count therefore grows like `τ^s s^{-3/2}` with an oscillating factor (`|B_s[n]| n^{3/2} / τ^n` stays in `(0.07, 0.84)` for `n = 300..320`), against `τ^{2s}` for the unsigned count. The even and odd halves differ by the square root of their size. This is the perimeter-graded version of the wiki's standing theme that the parity clause is "almost the entire difficulty" but only a lower-order correction to the count.

## Convex castles by semi-perimeter

A convex castle has exactly `h` blocks, so `s = w + h` and the grading is the anti-diagonal one. From `Σ_{w,h} C(2h+w-3, w-1) x^w y^h = xy(1-x)/((1-x)² - y)`:

| series | GF in `t` (`x = y = t`) | terms from `s = 2` |
|---|---|---|
| all | `t²(1-t)/(1-3t+t²)` | 1, 2, 5, 13, 34, 89, ... = A001519, Delest-Viennot's `F_{2n}`[^5] |
| signed | `-t²(1-t)/(1-t+t²)` | -1, 0, 1, 1, 0, -1, repeating with period 6 |
| even `h` | `t³(1-t)/((1-3t+t²)(1-t+t²))` | 0, 1, 3, 7, 17, 44, 116, 305, 799, 2091, 5473, ... |

The signed convex count is periodic because `1 - t + t²` has its roots at primitive sixth roots of unity. The even-`h` sequence has no OEIS match (searched 2026-09-22, with and without the leading 0). It closes the "exact enumeration with parity" question for convex castles in the perimeter grading: `even = (A001519 + period-6)/2`. All three series were checked against the DP through `s = 30`.

## Relation to other pages

- [[algebraic-languages-and-polyominoes-enumeration](pages/algebraic-languages-and-polyominoes-enumeration.md)]: the perimeter grading and the grammar-to-algebraic-GF method. `B(t)` is algebraic (context-free) and becomes rational at bounded height, as [[tower-word-language](pages/tower-word-language.md)] explains.
- [[convex-castle](pages/convex-castle.md)], [[stack-polyomino-gf](pages/stack-polyomino-gf.md)]: convex castles = stacks, now with the parity split by perimeter.
- [[tower-narayana-polynomial](pages/tower-narayana-polynomial.md)], [[narayana-numbers](pages/narayana-numbers.md)]: the identity whose re-indexing is A271942. Its `k` is the number of descents plus one (verified `w, b ≤ 7`), recorded on those pages.
- [[convex-polyomino](pages/convex-polyomino.md)], [[bousquet-melou-fedou-1995-convex-polyominoes](pages/bousquet-melou-fedou-1995-convex-polyominoes.md)]: on a row-convex shape blocks = height, so a convex polyomino's semi-perimeter is `w + h`. Lin and Chang's convex generating function `Z(x, y, 1)`, with width and height marked, is the convex-polyomino counterpart of the (width, blocks) grading on this page (own reasoning).
- [[castle-sign](pages/castle-sign.md)]: the `(-1)^blocks` weight is `(-1)^{s-w}`.
- [[bounded-height-castles-nacci](pages/bounded-height-castles-nacci.md)]: tribonacci appears there in the area grading at height `≤ 3`. Here `τ²` is the unrestricted perimeter growth. Whether the two appearances are related is open.

## Footnotes

[^1]: [[project-euler-502-brute-force](pages/project-euler-502-brute-force.md)] §"brute" L24 - "= c_1 + \sum_{i=2}^{w} \max(0, c_i - c_{i-1})", the column-height block-count formula.
[^2]: [[algebraic-languages-and-polyominoes-enumeration](pages/algebraic-languages-and-polyominoes-enumeration.md)] p.169 Abstract - "we prove that the number of convex polyominoes with perimeter 2n+8 is (2n+11)4^n - 4(2n+1)C(2n,n)."
[^3]: [[tower-narayana-polynomial](pages/tower-narayana-polynomial.md)] `raw/oeis-pe502/xrefs/A001263-tower.md` L17-21 - "= ( sum_{k=1..w} N(w,k) x^{k-1} ) / (1 - x)^w" and "sum_{k=1..w} N(w,k) * C(b + w - k, w - 1)."
[^4]: https://oeis.org/A082582 and https://oeis.org/A271942 (fetched 2026-09-22) - A082582: "a(n) is the number of bargraphs of semiperimeter n (n>=2)", with links to Bousquet-Mélou and Rechnitzer, "The site-perimeter of bargraphs" (2003), and Baril-Flórez-Ramírez (2025), neither read; A271942: "Triangle read by rows: T(n,k) is the number of bargraphs of semiperimeter n having width k", data "1,1,1,1,3,1,1,5,6,1,1,7,16,10,1,1,9,31,40,15,1,1,11,51,105,85,21,1".
[^5]: [[algebraic-languages-and-polyominoes-enumeration](pages/algebraic-languages-and-polyominoes-enumeration.md)] p.181 Lemma 3.2 - "The number of stack polyominoes with perimeter 2n+4 is the Fibonacci number F_{2n} with generating function (1-t^2)/((1-t-t^2)(1+t-t^2))."
