---
title: The convex-castle cap factor - convex prefactors as residues at 1/mu
category: Analyses
summary: "The three area prefactors of the convex ladder are one parallelogram residue times powers of one cap factor: parallelogram p = 0.29745350581112195108, directed convex p·κ = 0.65895554185211895992, convex 2p·κ² = 2.91959850971360705538, with κ = 2.21532282853826847652 the expected weight of convex castles (stacks) hung under the base of a large random parallelogram. The directed-convex constant has no OEIS asymptotic; none of p, κ, K, pκ is an OEIS decimal expansion. Bender's 1974 formula (11) is correct - evaluated with his own K it gives A067675's 2.919598509713607055 - and the printed 2.67564 comes entirely from a slip in K (printed 1.02934, true 1.07524214134071812420). His base variance 0.57609 is also off (exact counts give 1.70541)."
tags: [analysis, polyomino, convex, directed-convex, parallelogram-polyomino, stack-polyomino, convex-castle, asymptotics, residue, prefactor, q-series, bender, verification, oeis, novel-candidate]
sources: [bender-1974-convex-n-ominoes, bousquet-melou-fedou-1995-convex-polyominoes, klarner-rivest-1974-convex-n-ominoes]
created: 2026-09-22
updated: 2026-09-22
---

# The convex-castle cap factor

[[convex-polyomino-by-area](pages/convex-polyomino-by-area.md)] gives each rung of the area ladder a growth constant and a prefactor, `a(n) ~ c mu^n` with `mu = 2.30913...`. For the parallelogram, directed-convex and convex rungs the prefactors are `0.29745`, `0.65896` and `2.91960`, read there from long series. This page gets all three as residues at the first zero `r = 1/mu` of `J_0`, and finds that they are one number times powers of a second number:

| rung | prefactor | as a residue | caps |
|---|---|---|---|
| parallelogram | `p = 0.29745350581112195108` | `P_1(r) / (r P_2'(r))` | none |
| directed convex | `0.65895554185211895992` | `M_1(r) / (r P_2'(r))` | `p · κ` |
| convex | `2.91959850971360705538` | `2K^2 / (r P_1(r) P_2'(r))` | `2p · κ^2` |

with the **cap factor**

```
κ = K / P_1(r) = 2.21532282853826847652
K = 1.07524214134071812420          (Bender's K, recomputed)
mu = 1/r = 2.30913859333049473110   (A276994)
```

The parallelogram and convex values agree with OEIS A006958's `0.2974535058111219...` and A067675's `2.9195985097136070...` in every digit OEIS prints.[^1] OEIS A067676 has no asymptotic for directed convex. An OEIS search for the digits of `pκ`, `κ`, `K` and `p` finds nothing, while the same search on `mu`'s digits finds A276994. So these are novel-candidate constants for decimal-expansion entries.[^2]

## The residues

Here `P_1 = J_1` and `1 - P_2 = J_0` are Bender's alternating q-series (5a), (5b) at `x = y_1 = y_2 = t = 1`, with `q = x` marking area:[^3]

```
P_2(x) = sum_{k>=1} (-1)^{k+1} x^{k(k+1)/2} / ((1-x)...(1-x^k))^2
P_1(x) = sum_{k>=1} (-1)^{k+1} x^{k(k+1)/2} / ((1-x)...(1-x^{k-1}))^2 / (1 - x^k)
```

These are the parallelogram rung `J_1/J_0` of [[bousquet-melou-fedou-1995-convex-polyominoes](pages/bousquet-melou-fedou-1995-convex-polyominoes.md)] at `x = y = 1`. A simple zero `r` of `J_0 = 1 - P_2` gives `[q^n] N/J_0 ~ N(r) / (r P_2'(r)) · r^{-n}` for any numerator `N` analytic past `r`. This is the parallelogram prefactor for `N = P_1` (Bender's (7a)),[^4] and the directed-convex prefactor for `N = M_1`, the Bousquet-Mélou-Fédou numerator of `Y = y M_1/J_0`.[^5]

For the convex rung, Bender's residue formula (10) splits the prefactor into three factors: the pole, `2/(r P_2'(r))`, and one cap factor for each end,[^6]

```
f = 2/(r P_2') × C(y^0, S(r, y) P_1(r, 1, 1, 1/y)) × C(y^0, S(r, y) P_2(r, 1, 1/y))
  = 2K^2 / (r P_1(r) P_2'(r))                                              (11)
```

Here `C(y^0, ·)` takes the constant term, and `S(r, y) = T(r, y) y/(1-y)^2 + 1/(1-y)`. `T(x, y)` is his trapezoid series (3) with `y` marking the base. Bender turns the first cap into `K` by residues at `y = r^k`, and a 180-degree rotation turns the second into `K/P_1(r)`.[^7] Both factors, computed directly as Laurent constant terms, agree with these closed forms to 40 digits. So the convex prefactor is `2 · p · κ^2` with `κ = K/P_1(r)`, and the directed-convex residue equals `p · κ` to 27 digits.

## Where Bender's 8% went

Bender printed `K = 1.02934` and `f = 2.67564` (abstract) or `f = 2.67483` (eq. (11)).[^6] Evaluated as written, his own sum for `K` gives `1.07524214134...`, and his own eq. (11) then gives `2.919598509713607055`, the A067675 value. So the whole discrepancy is in the number `K`, and the formula is right.

- `2K^2/(r P_1 P_2')` with `K = 1.02934` gives `2.675644`, the abstract's `2.67564`. Eq. (11)'s `2.67483` would need `K = 1.02918`, so it looks like the same `K` with other factors rounded.
- The `K` sum alternates. Its partial sums run `1.415, 1.040, 1.0766, 1.07522, 1.075242, ...`, and none of them is near `1.029`. The obvious misreadings of `S` fail too: dropping the `1/(1-y)` term gives `0.590`, and shifting the power of `y` on `T` gives `1.678` or `0.756`. The slip is in the arithmetic, and which step produced it cannot be recovered.
- This is the `2.67564` that Delest-Viennot 1984 and Bousquet-Mélou-Fédou 1995 later quote ([[bender-1974-convex-n-ominoes](pages/bender-1974-convex-n-ominoes.md)]).

Following OEIS, the value is `2.91960`, now with Bender's own derivation behind it.

A second printed constant is also off. Bender gives the base length of a parallelogram (its bottom row) mean `2.06030` and variance `0.57609`.[^8] The limiting base distribution is `pi_b = [y^b] P_1(r, 1, 1, y) / P_1(r)`, which is positive and sums to 1. Its mean is `2.0603013436`, matching Bender, but its variance is `1.7054123579`. Exact counts agree with `pi_b`: summing Klarner-Rivest's `min{m, n}` transfer over row sequences ([[klarner-rivest-1974-convex-n-ominoes](pages/klarner-rivest-1974-convex-n-ominoes.md)]) gives mean `2.06030134` and variance `1.70541236` at areas 60 and 90.

## The castle reading

`κ` is a convex-castle number. Bender's trapezoids are stacks, and stacks are convex castles: `T(x, 1)` is A001523, and `T(x, y)` counts stacks by area and base width, as checked by brute force through area 14.[^9] `S_b = 1 + sum_{b' < b} (b - b') T_{b'}(r)` is the weight, at `q = r`, of all ways to hang a convex castle of base `b' < b` under a base of length `b` in one of `b - b'` positions. The `1` is the empty cap.[^7] Then

```
κ = sum_b pi_b S_b = E[ S_B ],     B ~ pi, the base length of a large random parallelogram
```

(own reasoning; the identity `sum_b pi_b S_b = K/P_1(r)` is numerical, to 40 digits). So:

- **A directed-convex polyomino of area `n` is, asymptotically, a parallelogram with one convex castle hung on it,** and **a convex polyomino is a parallelogram with a castle at each end, in either slant.** The prefactors `p`, `pκ`, `2pκ^2` count exactly that. The directed-convex identity is numerical here, to 27 digits. A cut-and-glue proof in Bender's style, with one trapezoid instead of two, is the open step.
- The castles in the cap carry no exponential growth, since `T(x, 1)` converges out to radius 1. They set only the constant: at `q = r` the whole stack series is `T(r, 1) = 2.26779719786`, and `κ` averages the base-weighted version over the parallelogram's base.
- The two convex constants share `K`, so `2.91960 / 0.65896 = 2κ = 4.43065` and `2.91960 / 0.29745 = 2κ^2 = 9.81532`. By area, about `1/(2κ^2) = 10.2%` of convex polyominoes are parallelograms of one slant, or `20.4%` counting both slants.

## Computation

Everything above in 24 lines (`mpmath`, 30 digits, about one second). The printed residues agree with the paired cap forms to 20 digits at this precision:

```python
from mpmath import mp, findroot, diff
mp.dps = 30
M = 60                                   # q-series terms; r^(k(k+1)/2) is negligible well before this
def qp(x, s, n):                         # (1 - x^s)(1 - x^(s+1))...(1 - x^(s+n-1))
    p = mp.mpf(1)
    for i in range(n): p *= 1 - x**(s + i)
    return p
P2 = lambda x: sum((-1)**(k+1) * x**(k*(k+1)//2) / qp(x, 1, k)**2 for k in range(1, M))
P1 = lambda x: sum((-1)**(k+1) * x**(k*(k+1)//2) / (qp(x, 1, k) * qp(x, 1, k-1)) for k in range(1, M))
r = findroot(lambda x: P2(x) - 1, 0.433)            # 1/mu, the first zero of J_0 = 1 - P_2
c = [(-1)**(k+1) * r**(k*(k+1)//2) / qp(r, 1, k-1)**2 for k in range(M)]
def S(y):                                           # Bender's cap series S(r, y)
    T = sum(r**k * y * (1 - r**k * y) / mp.fprod((1 - r**n * y)**2 for n in range(1, k+1))
            for k in range(1, M))                   # trapezoids = stacks, y marking the base
    return T * y / (1 - y)**2 + 1 / (1 - y)
K = sum(c[k] * (S(r**k) - 1) / r**k for k in range(1, M))   # Bender p.224
dP2 = diff(P2, r)
p = P1(r) / (r * dP2)                                # parallelogram prefactor
kappa = K / P1(r)
M1 = sum(r**n / qp(r, 1, n-1) * sum((-1)**k * r**(k*(k-1)//2) / (qp(r, 1, k) * qp(r, k+1, n-k))
         for k in range(n)) for n in range(1, M))    # Bousquet-Melou-Fedou M_1 at x = y = 1, q = r
print(1/r, p, K, kappa)
print(M1 / (r * dP2), p * kappa)                     # directed convex: residue vs one cap
print(2 * K**2 / (r * P1(r) * dP2), 2 * p * kappa**2)   # convex: Bender (11) with this K, two caps
```

## Open

- A cut-and-glue proof that directed-convex prefactor = `p · κ`.
- A q-series closed form for `K` or `κ` in the Bousquet-Mélou-Fédou basis (`Jbar_1`, `Kbar_1`, `alpha`, `beta`). The convex numerator `2 M_1 (Jbar_1 beta - Kbar_1 alpha)` evaluated at `r` must equal `2K^2 / P_1(r)`, which would make it a product of two copies of one cap.
- The height-parity split of the prefactors. The signed counts on [[convex-polyomino-by-area](pages/convex-polyomino-by-area.md)] grow like `1.18^n` to `1.3^n`, so even and odd height share the prefactor `c/2` to leading order. The next term is the open one.

## Relation to other pages

- [[bender-1974-convex-n-ominoes](pages/bender-1974-convex-n-ominoes.md)]: the formula (10)-(11), `K`, and the trapezoid series. This page recomputes them.
- [[bousquet-melou-fedou-1995-convex-polyominoes](pages/bousquet-melou-fedou-1995-convex-polyominoes.md)]: `J_0`, `J_1`, `M_1`, and the area-120 prefactor fits these residues extend.
- [[klarner-rivest-1974-convex-n-ominoes](pages/klarner-rivest-1974-convex-n-ominoes.md)]: `mu`, the stack-parallelogram-stack trisection, and the `min{m, n}` kernel used for the base check.
- [[convex-polyomino](pages/convex-polyomino.md)], [[convex-castle](pages/convex-castle.md)], [[stack-polyomino-gf](pages/stack-polyomino-gf.md)]: the caps are convex castles.
- [[convex-polyomino-by-area](pages/convex-polyomino-by-area.md)]: the ladder whose prefactor column this page explains.

## Footnotes

[^1]: https://oeis.org/A006958, https://oeis.org/A067675, https://oeis.org/A276994 (fetched 2026-09-22) - A006958 "c = 0.2974535058111219..."; A067675 "c = 2.9195985097136070..."; A276994 "2.3091385933304947...". Values on this page computed by execution, 2026-09-22 (block above, and a 40-digit rerun with 80 series terms).
[^2]: OEIS searches by execution, 2026-09-22 (https://oeis.org/search, JSON format): no results for the digit strings of `0.6589555418`, `2.2153228285`, `1.0752421413`, `2.9745350581`, or `2.2677971978`; the control search on `2.3091385933` returned A276994. https://oeis.org/A067676 (fetched 2026-09-22) has no asymptotic formula.
[^3]: [[bender-1974-convex-n-ominoes](pages/bender-1974-convex-n-ominoes.md)] p.221 eqs. (5a), (5b) - `P_1` and `P_2` as alternating sums with `x^{k(k+1)/2}` numerators; "Hence P(x, t, 1, y_2) = P_1(x, t, 1, y_2)/(1 - P_2(x, t, 1))" (read from the page image of the local PDF).
[^4]: [[bender-1974-convex-n-ominoes](pages/bender-1974-convex-n-ominoes.md)] p.222 §3 - "We also obtained P_1(r, 1, 1, 1)/(rP_2'(r, 1, 1)) = 0.29745. Thus (7a) p(n) ~ 0.29745γ^n since the pole is simple" (read from the page image).
[^5]: [[bousquet-melou-fedou-1995-convex-polyominoes](pages/bousquet-melou-fedou-1995-convex-polyominoes.md)] eq. (3) pp.56-57 and Appendix A p.72 - `Y = y M_1/J_0` and the series `M_1`, as transcribed on that page.
[^6]: [[bender-1974-convex-n-ominoes](pages/bender-1974-convex-n-ominoes.md)] p.219 abstract, p.223 eqs. (9)-(10), p.224 eq. (11) - "c(n) ~ fγ^n, where γ = 2.30914 and f = 2.67564"; "(10) f = (-2r^{-1} Res_{x=r} (1 - P_2(x, 1, 1))^{-1}) × C(y_2^0, S(r, y_2)P_1(r, 1, 1, y_2^{-1})) × C(y_1^0, S(r, y_1)P_2(r, 1, y_1^{-1}))"; "K = ... = 1.02934"; "(11) f = 2K^2/(rP_1(r, 1, 1, 1)P_2'(r, 1, 1)) = 2.67483" (read from the page images).
[^7]: [[bender-1974-convex-n-ominoes](pages/bender-1974-convex-n-ominoes.md)] pp.223-224 - (8) "A trapezoid of base b_T and a parallelogram of base b_P can be joined in one way if b_T = 0 and b_P - b_T ways otherwise", with "S(x, y) = T(x, y) y/(1 - y)^2 + 1/(1 - y)"; K as a sum over the residues at `y = r^k` and `y = 0`; "By rotating the plane 180° ... Hence the third factor in (10) is K/P_1(r, 1, 1, 1)" (read from the page images). The cap reading of `S_b` and `κ` is this page's.
[^8]: [[bender-1974-convex-n-ominoes](pages/bender-1974-convex-n-ominoes.md)] p.225 §5 - "the base has mean and variance μ(n) = p_1(n)/p_0(n) ~ 2.06030, σ^2(n) = p_2(n)/p_0(n) - μ(n)^2 ~ 0.57609". Recomputed by execution, 2026-09-22: exact bottom-row distribution of parallelograms from the `min{m, n}` row transfer at areas 30, 60, 90 (mean `2.06030134`, variance `1.70541236` from area 60 on).
[^9]: [[bender-1974-convex-n-ominoes](pages/bender-1974-convex-n-ominoes.md)] p.220 eq. (3) - "T(x, y) = sum_{k>=1} x^k y(1 - x^k y) / prod_{n=1}^k (1 - x^n y)^2" (read from the page image); checked by execution, 2026-09-22, against brute-force unimodal compositions by area and width, every coefficient through area 14.
