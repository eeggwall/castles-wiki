---
title: "The generating function of convex polyominoes (Bousquet-Mélou and Fédou, 1995)"
category: Sources
summary: Bousquet-Mélou and Fédou solve the three-equation linear q-differential system that characterizes convex polyominoes by width, height and area, giving Z = 2y^2 M_1(Jbar_1 beta - Kbar_1 alpha)/J_0 - y Jbar_1 b_1 + y Kbar_1 a_1, a quotient over the same q-Bessel denominator J_0 as the parallelogram (y J_1/J_0) and directed-convex (y M_1/J_0) rungs. The method is a q-analogue of variation of parameters, guided by the q = 1 Bessel ODE system. Verified here to area 120 against A006958, A067675 and A067676; the paper's printed convex prefactor C = 2.67564 does not match its own series, which gives 2.91960 (as OEIS has it), and the directed-convex prefactor comes out 0.65896.
tags: [source, paper, polyomino, convex, directed-convex, parallelogram-polyomino, q-analog, q-bessel, q-differential-system, generating-function, area, bousquet-melou, fedou, verification, oeis]
sources: [bousquet-melou-fedou-1995-convex-polyominoes]
created: 2026-09-22
updated: 2026-09-23
---

# The generating function of convex polyominoes (Bousquet-Mélou and Fédou, 1995)

**Source:** raw/bousquet-melou-fedou-1995-convex-polyominoes.pdf (also `raw/bousquet-melou-fedou-1995-convex-polyominoes.txt`, the scan's OCR text layer extracted with `pdftotext -layout`)
**Publication:** Mireille Bousquet-Mélou and Jean-Marc Fédou, "The generating function of convex polyominoes: the resolution of a q-differential system", Discrete Mathematics 137 (1995) 53-75. DOI `10.1016/0012-365X(93)E0161-V`. Received 9 February 1993.[^1]
**Date ingested:** 2026-09-22
**Type:** paper (23 pp., scanned)

The OCR text layer is reliable for prose and garbled in most displayed formulas. Every formula on this page was read from the rendered page images and is cited by page. Line ranges point at the surrounding prose in the `.txt`.

## Summary

The paper answers the area version of the convex-polyomino question on [[convex-polyomino-by-area](pages/convex-polyomino-by-area.md)]. It gives the generating function `Z(x, y, q)` of [[convex-polyomino](pages/convex-polyomino.md)]es with `x` marking width, `y` marking height and `q` marking area, in a form the authors call "beautiful": a quotient over the same q-Bessel denominator `J_0` that already appears in the parallelogram and directed-convex results, built from finitely many series, each expanded in `x`.[^2] Three earlier formulas existed for `Z`: two from heaps of pieces and the algebraic-language method, and a third by Lin. The authors reject all three because they involve complicated polynomials, are not expanded in `x`, or are infinite sums of series.[^3]

The starting point is Bousquet-Mélou's earlier Lemma 1.1. Encoding convex polyominoes as words of an algebraic language (Schützenberger's methodology) gives a linear q-differential system in which each series is evaluated at `x` and at `xq`. The system's three blocks are one scalar equation for parallelograms `X`, a 2×2 block for directed convex `Y, Y_1`, and a 3×3 block for convex `Z, Z_1, Z_3`.[^4] No general method integrates such q-equations. The authors' route is to take the `q -> 1` limit (after scaling `x -> x(1 - q)^2`), which turns the system into ordinary differential equations whose solutions are Bessel functions. They solve that ODE system in closed form by variation of parameters. Then they guess the "right" q-analogues of its solutions, and redo variation of parameters at the q level, with `log_q(x) = log(x)/log(q)` standing in for the logarithm.[^5] The method is written up as a concept on [[q-differential-system](pages/q-differential-system.md)].

Section 3 proves the theorem by direct verification against the system, with the q-series listed in Appendix A and the "elementary" q-equations they satisfy in Appendix B. Section 4 explains how the solution was found. Section 5 extracts the width-by-width rational functions and a table of counts by area to `n = 20`.[^6]

## The ladder of formulas

Notation: `(y)_n = (1 - y)(1 - yq)...(1 - yq^{n-1})`, so `(yq)_n = (1 - yq)...(1 - yq^n)` and `(q)_n = (1 - q)...(1 - q^n)`. `S(xq)` means `S(xq, y, q)`.[^7]

| family | generating function | source |
|---|---|---|
| Ferrers diagrams | `y sum_{n>=1} x^n q^n / (yq)_n` | classical, p.55 [^8] |
| parallelogram | `X = y J_1 / J_0` | eq. (1), p.56 [^9] |
| directed convex | `Y = y M_1 / J_0` | eq. (3), pp.56-57 [^10] |
| convex | `Z = 2y^2 M_1 (Jbar_1 beta - Kbar_1 alpha) / J_0 - y Jbar_1 b_1 + y Kbar_1 a_1` | Theorem 3.1, eq. (9), p.62 [^11] |

The series, from Appendix A (p.72):

```
J_0 = sum_{n>=0} (-1)^n x^n q^{C(n+1,2)} / ((q)_n (yq)_n)
J_1 = - sum_{n>=1} (-1)^n x^n q^{C(n+1,2)} / ((q)_{n-1} (yq)_n)
M_1 = sum_{n>=1} x^n q^n / (yq)_{n-1} * sum_{k=0}^{n-1} (-1)^k q^{C(k,2)} / ((q)_k (yq^{k+1})_{n-k})
M_0 = the same with (yq)_n in place of (yq)_{n-1}
Jbar_1 = sum_{n>=1} x^n q^n / ((q)_{n-1} (q)_n)
Kbar_1 = -1 + sum_{n>=1} x^n q^n / ((q)_{n-1} (q)_n) * ( sum_{k=1}^n 2q^k/(1-q^k) - q^n/(1-q^n) )
alpha  = sum_{n>=1} (-1)^n x^n q^{C(n+1,2)} / (q)_n * sum_{k=1}^n (-1)^k q^{C(k+1,2)} / ((q)_{k-1} (yq^k)_{n-k+1})
```

The barred series carry no `y`. At `q = 1` they become `Jbar_0 = sum x^n/n!^2` and `Jbar_1 = sum x^n/((n-1)! n!)`, with `J_0(x) = Jbar_0(-x)` and `J_1(x) = -Jbar_1(-x)` (p.61), so they are the Bessel solutions without the alternating signs. `beta`, `a_1` and `b_1` take half a page each in Appendix A (pp.73-74). Appendix B's defining q-equations say what they are more compactly (p.74):[^12]

```
alpha - (1 + y - xq) alpha(xq) + y alpha(xq^2) = xq^2 Jhat_0(xq^2)
beta - alpha - (1 + y - xq) beta(xq) + y (beta(xq^2) + alpha(xq^2)) = xq^2 Jhat_0(xq^2) + xq^2 Khat_0(xq^2)
a_0 - y a_0(xq) - a_1 = 0,        a_1 - y a_1(xq) - xq a_0 = xq (2y alpha - Jhat_0 + Jhat_1)
b_0 - y b_0(xq) - b_1 = y a_0(xq), b_1 - y b_1(xq) - xq b_0 = y a_1(xq) + xq (2y beta - Khat_0 + Khat_1)
```

The hatted series are `Jhat_0 = sum x^n q^{n(n+1)} / (q)_n^2` and `Jhat_1 = sum_{n>=1} x^n q^{n^2} / ((q)_{n-1} (q)_n)`, together with the `Khat` series formed as `Kbar` is. They are the barred series divided by `E = Jbar_1 Kbar_0 - Jbar_0 Kbar_1 = sum x^n q^n / (q)_n` (Property 3.2).[^13]

Three readings of the ladder:

- **One denominator for three rungs.** Parallelogram, directed convex and convex all divide by the same `J_0`. It is the q-analogue of the Bessel function `sum (-1)^n x^n / n!^2` that the `q = 1` limit produces (p.60). This is the structure behind the shared growth constant `mu = 2.30913...` on [[convex-polyomino-by-area](pages/convex-polyomino-by-area.md)]: at `x = y = 1`, `1/mu` is the smallest zero of `J_0`.[^14]
- **Each rung adds a harder numerator.** `J_1` (parallelogram) is a q-Bessel series. `M_1` (directed convex) is the q-analogue of the odd part of `J_1`, which the authors call "obviously more difficult to guess". The convex numerator needs the logarithmic (second-kind) solutions `Kbar_0, Kbar_1` as well.[^15]
- **Width by width it is rational.** Because every series is expanded in `x`, the coefficient of `x^n` in `Z` is a rational function of `y` and `q`. Section 5 gives it as `x^n y q^n P_n / ((1 - yq^n) prod_{i=1}^{n-1} (1 - yq^i)^{floor((n-2)/i) + 2})`. At `y = 1` the area generating function of width-`n` convex polyominoes is `x^n q^n Q_n / ([n-2]! (q)_{n-1} (q)_n)`, with `[n]! = (q)_n/(1-q)^n`.[^16]

## Other results reported in the paper

- **Height and width without area (Lin and Chang).** `Z(x, y, 1) = xy/Delta^2 (1 - 3x - 3y + 3x^2 + 3y^2 + 5xy - x^3 - y^3 - x^2 y - xy^2 - xy(x - y)^2) - 4x^2y^2/Delta^{3/2}` with `Delta = 1 - 2x - 2y - 2xy + x^2 + y^2`. It is algebraic and symmetric in `x, y`, and at `x = y` it refines the Delest-Viennot perimeter count ([[algebraic-languages-and-polyominoes-enumeration](pages/algebraic-languages-and-polyominoes-enumeration.md)]).[^17]
- **Parallelograms, symmetric form.** Multiplying by `(yq)_infinity` gives `X = xyq L(xq, yq) / L(x, y)` with `L(x, y) = sum_{n,m>=0} (-1)^{n+m} x^n y^m q^{C(n+m+1,2)} / ((q)_n (q)_m)`. This makes the `x <-> y` symmetry visible.[^9]
- **The width polynomials.** `Q_1 = 1`, `Q_2 = 1 + 2q + q^2`, `Q_3 = 1 + 6q + 12q^2 + 12q^3 + 7q^4 + 2q^5`, `Q_4 = 1 + 11q + 43q^2 + 95q^3 + 150q^4 + 186q^5 + 181q^6 + 137q^7 + 79q^8 + 33q^9 + 10q^10 + 2q^11`. The authors conjecture that every `Q_n` has positive coefficients and is unimodal.[^16]
- **Table 1** gives parallelogram, directed convex and convex counts by area for `n = 1..20`. It agrees term for term with the ladder on [[convex-polyomino-by-area](pages/convex-polyomino-by-area.md)].[^18]
- **Asymptotics as printed.** The paper cites Bender and Klarner-Rivest for "the number of convex polyominoes of area n is asymptotically C a^n, where C ≃ 2.67564 and a ≃ 2.30914".[^19] The growth rate `a` agrees with A276994. The prefactor does not agree with the paper's own generating function (next section).

## Verification

The Appendix A series were transcribed from the page images into truncated q-series arithmetic at `x = y = 1`, and Theorem 3.1 was evaluated from them.[^20]

- `y J_1/J_0`, `y M_1/J_0` and eq. (9) reproduce all three columns of Table 1 through `n = 20`. They also match the OEIS b-files A006958, A067676 and A067675 at every `n <= 120`.
- The width formulas for `Q_2, Q_3, Q_4` match an independent column sweep of width-2, 3 and 4 convex polyominoes through area 26.
- Expanding the Lin-Chang formula at `x = y = t` gives `t^2 + 2t^3 + 7t^4 + 28t^5 + 120t^6 + 528t^7 + 2344t^8 + 10416t^9 + ...`. These are the A005436 terms `1, 2, 7, 28, 120, 528, 2344, 10416`, with `t^{k}` counting semiperimeter `k`.
- **Prefactors.** `a(n)/mu^n` at `n = 120`, where the digits shown are stable from `n = 80` on:

| family | `a(n)/mu^n` | OEIS |
|---|---|---|
| parallelogram | `0.2974535058` | A006958 gives `0.2974535058111219...` |
| directed convex | `0.6589555418` | A067676 lists no asymptotic formula (checked 2026-09-22) |
| convex | `2.9195985097` | A067675 gives `2.9195985097136070...` |

The paper's printed convex prefactor, `C ≃ 2.67564`, is therefore not the constant of the series it derives. The value that fits is `2.91960`, the one OEIS records. The paper gives no derivation of its `C`. The number is from the abstract of Bender's paper ([[bender-1974-convex-n-ominoes](pages/bender-1974-convex-n-ominoes.md)]), whose own eq. (11) prints `2.67483`. Delest and Viennot had already quoted it ([[algebraic-languages-and-polyominoes-enumeration](pages/algebraic-languages-and-polyominoes-enumeration.md)]). Klarner and Rivest give no prefactor ([[klarner-rivest-1974-convex-n-ominoes](pages/klarner-rivest-1974-convex-n-ominoes.md)]).

The parallelogram and directed-convex rungs fit in a short block (`N` is the area cutoff):

```python
N = 30
def mul(a, b):
    r = [0] * (N + 1)
    for i, u in enumerate(a):
        if u:
            for j in range(N + 1 - i):
                r[i + j] += u * b[j]
    return r
def div(a, b):                      # b[0] == 1
    r = [0] * (N + 1)
    for n in range(N + 1):
        r[n] = a[n] - sum(b[k] * r[n - k] for k in range(1, n + 1))
    return r
def qpoch_inv(s, n):                # 1/((1-q^s)(1-q^{s+1})...(1-q^{s+n-1}))
    r = [1] + [0] * N
    for m in range(s, s + n):
        r = mul(r, [1 if i % m == 0 else 0 for i in range(N + 1)])
    return r
def mono(c, e, s):                  # c q^e s
    return [0] * e + [c * v for v in s[:N + 1 - e]] if e <= N else [0] * (N + 1)
def total(terms):
    return [sum(col) for col in zip(*terms)]
tri = lambda n: n * (n + 1) // 2
# Appendix A at x = y = 1; the n-th term carries q^n, so n <= N suffices
J0 = total(mono((-1)**n, tri(n), mul(qpoch_inv(1, n), qpoch_inv(1, n))) for n in range(N + 1))
J1 = total(mono(-(-1)**n, tri(n), mul(qpoch_inv(1, n - 1), qpoch_inv(1, n))) for n in range(1, N + 1))
M1 = total(mono(1, n, mul(qpoch_inv(1, n - 1), total(
         mono((-1)**k, k * (k - 1) // 2, mul(qpoch_inv(1, k), qpoch_inv(k + 1, n - k)))
         for k in range(n)))) for n in range(1, N + 1))
print(div(J1, J0)[1:])              # parallelogram, A006958
print(div(M1, J0)[1:])              # directed convex, A067676
```

## Key Takeaways

- The convex-polyomino generating function by width, height and area has a closed form over the q-Bessel denominator `J_0`, the same denominator as the parallelogram and directed-convex rungs.[^11]
- It is the unique power-series solution of a linear q-differential system with 1×1, 2×2 and 3×3 blocks, derived from an algebraic-language encoding.[^4]
- The solution was found by solving the `q = 1` ODE system with Bessel functions and variation of parameters, then q-analogizing each step, with `log_q` as a formal device ([[q-differential-system](pages/q-differential-system.md)]).[^5]
- Width-`n` convex polyominoes have a rational area generating function with an explicit denominator, and its numerators `Q_n` are conjectured unimodal.[^16]
- The printed prefactor `C ≃ 2.67564` does not match the formula. The formula's own series gives `2.91960`, and the directed-convex prefactor is `0.65896` (Verification).

## Entities & Concepts

- [[convex-polyomino](pages/convex-polyomino.md)] - the family solved, with the Fig. 2 subclasses.
- [[convex-polyomino-by-area](pages/convex-polyomino-by-area.md)] - the area ladder whose directed-convex and convex rungs this paper supplies.
- [[q-differential-system](pages/q-differential-system.md)] - the solution method.
- [[column-convex-polygon-enumeration](pages/column-convex-polygon-enumeration.md)] - Bousquet-Mélou's later add-a-column method, which recovers these generating functions by another route.
- [[steep-polyominoes-q-motzkin-bessel](pages/steep-polyominoes-q-motzkin-bessel.md)] - Fédou's q-Bessel quotients for steep parallelograms.
- [[klarner-rivest-1974-convex-n-ominoes](pages/klarner-rivest-1974-convex-n-ominoes.md)] - the first parallelogram-by-area generating function and the growth constant.
- [[bender-1974-convex-n-ominoes](pages/bender-1974-convex-n-ominoes.md)] - the asymptotics this paper cites, and the source of its printed `C`.
- [[algebraic-languages-and-polyominoes-enumeration](pages/algebraic-languages-and-polyominoes-enumeration.md)] - the algebraic-language method and the perimeter count. Its closing question, adding area, is the one this paper answers for convex polyominoes.
- [[castle-q-bessel-closed-form](pages/castle-q-bessel-closed-form.md)] - castles by width, blocks and area are `Π/(1 - x - Π)` with `Π = y J_1/J_0` at width `(1-x)u`, height `x`.
- [[viennot-heap-tower](pages/viennot-heap-tower.md)] - heaps of pieces, the combinatorial explanation of the quotient form the paper mentions for (1) and (3).

## Relation to Other Wiki Pages

Before this ingest, [[convex-polyomino-by-area](pages/convex-polyomino-by-area.md)] listed this paper under "Sources not yet read" and marked the directed-convex and convex generating functions as not derived. Both rungs now have a cited closed form, verified to area 120.

The castle's own area generating functions ([[castle-by-area](pages/castle-by-area.md)], [[stack-polyomino-gf](pages/stack-polyomino-gf.md)]) sit at the bottom of the same ladder. There the "denominator" is a finite product (`1 - 2z` for bar graphs, q-Pochhammer products for stacks), with no q-Bessel zero. The jump to `J_0` happens exactly when the bottoms stop being constant, at the parallelogram rung (own reasoning, from the table above).

The paper's Fig. 2 marks the bounding-box corners each subclass must contain: parallelograms at bottom-left and top-right, directed convex at bottom-left. This agrees with the corner taxonomy on [[convex-polyomino](pages/convex-polyomino.md)]. Its Ferrers diagram is drawn right-justified, so its third corner is top-right where the wiki's is top-left, a reflection only.[^21]

## Footnotes

[^1]: [[bousquet-melou-fedou-1995-convex-polyominoes](pages/bousquet-melou-fedou-1995-convex-polyominoes.md)] p.53 L3-12 - "Discrete Mathematics 137 (1995) 53 75 ... The generating function of convex polyominoes: the resolution of a q-differential system ... Received 9 February 1993" (OCR diacritics restored).
[^2]: [[bousquet-melou-fedou-1995-convex-polyominoes](pages/bousquet-melou-fedou-1995-convex-polyominoes.md)] Abstract and §1 p.53, p.59 L16-22, L313-315 - "We give a 'beautiful' though complex - formula for the generating function Z of convex polyominoes, according to their area, width and height"; "a 'beautiful' formula, that is, one which is of the same form as (1) and (3) and involves a finite number of series expanded in x."
[^3]: [[bousquet-melou-fedou-1995-convex-polyominoes](pages/bousquet-melou-fedou-1995-convex-polyominoes.md)] pp.57-59 L220-223, L301-305 - "we were able to determine two formulas for the trivariate distribution ... neither formula was totally satisfying"; "The series U, V and W involve rather complicated polynomials and are not expanded in x. Moreover, Expression (7) appears as an infinite sum of series. There exists a third formula for Z, which is still bigger [14]" (ref. [14] is Lin 1991).
[^4]: [[bousquet-melou-fedou-1995-convex-polyominoes](pages/bousquet-melou-fedou-1995-convex-polyominoes.md)] Lemma 1.1, eq. (6), p.58 L258-285 [synthesis] - "Let X (resp. Y, Z) be the generating function of parallelogram (resp. directed and convex, convex) polyominoes. Then, these three series are totally characterized by the following q-differential system"; the system (read from the page image) has blocks of size 1, 2 and 3 with the 3×3 matrix `((1, 2xq, x^2q^2), (1, 1+xq, xq), (1, 2, 1))`; "this q-differential system has a unique solution in terms of power series"; "based on Schützenberger's methodology [5]".
[^5]: [[bousquet-melou-fedou-1995-convex-polyominoes](pages/bousquet-melou-fedou-1995-convex-polyominoes.md)] §§2, 4.1-4.2, pp.59-61, 66-67 [synthesis] L77-83, L326-446, L670-715 - "there exists no general technique to integrate q-differential equations ... Our method is a sort of q-analogue of the classical method used to solve linear systems of ordinary differential equations"; the `q -> 1` limits use `x(1 - q)^2` (p.60); "the variation of parameters method gives, after a few integrations which are miraculously simple" (p.61); `log_q(x) = log(x)/log(q)` (p.67).
[^6]: [[bousquet-melou-fedou-1995-convex-polyominoes](pages/bousquet-melou-fedou-1995-convex-polyominoes.md)] pp.54, 62 L93-96, L108-109, L449-457 [synthesis] - "The main theorem is proved in Section 3: we check by direct computation that the expression we give is indeed a solution"; "we explain in Section 4 how we arrived at this formula"; Appendix A lists the series, Appendix B "the main identities (or q-equations) they satisfy".
[^7]: [[bousquet-melou-fedou-1995-convex-polyominoes](pages/bousquet-melou-fedou-1995-convex-polyominoes.md)] pp.56-57 L145-147, L225-226 - "Let n≥1, then (y)_n = prod_{i=0}^{n-1} (1 - yq^i)"; "for k in N, S(xq^k) instead of S(xq^k, y, q)" (formula read from the page image).
[^8]: [[bousquet-melou-fedou-1995-convex-polyominoes](pages/bousquet-melou-fedou-1995-convex-polyominoes.md)] p.55 L136-140 - "it is well-known that the generating function of Ferrers' diagrams is [1]: y sum_{n≥1} x^n q^n / (yq)_n" (formula read from the page image).
[^9]: [[bousquet-melou-fedou-1995-convex-polyominoes](pages/bousquet-melou-fedou-1995-convex-polyominoes.md)] p.56 L153-184 [synthesis] - "Their generating function is the quotient of two q-analogues of Bessel-like functions", eq. (1) `X = y J_1/J_0`; first obtained by Klarner and Rivest (area), then Delest-Fédou (area and width), Brak-Guttmann (area and perimeter), Bousquet-Mélou-Viennot (full); eq. (2), the symmetric form via `L(x, y)` (formulas read from the page image).
[^10]: [[bousquet-melou-fedou-1995-convex-polyominoes](pages/bousquet-melou-fedou-1995-convex-polyominoes.md)] pp.56-57 L185-204 - "Their generating function is the quotient of a q-analogue of the odd part f a Bessel-like function by a q-analogue of another Bessel-like function", eq. (3) `Y = y M_1/J_0`; "the coefficient of x^n in J_0, as well as in J_1 or in M_1, is an explicit series (actually, a rational fraction) in y and q" (formula read from the page image).
[^11]: [[bousquet-melou-fedou-1995-convex-polyominoes](pages/bousquet-melou-fedou-1995-convex-polyominoes.md)] Theorem 3.1, p.62 L467-488 - "The generating function of convex polyominoes is Z = 2y^2 M_1(Jbar_1 β - Kbar_1 α)/J_0 - y Jbar_1 b_1 + y Kbar_1 a_1" (formula read from the page image; the OCR at L469 is garbled).
[^12]: [[bousquet-melou-fedou-1995-convex-polyominoes](pages/bousquet-melou-fedou-1995-convex-polyominoes.md)] Appendices A-B, pp.72-74 L984-1131 [synthesis] - the displayed series and relations transcribed here from the page images; the OCR text of both appendices is largely illegible.
[^13]: [[bousquet-melou-fedou-1995-convex-polyominoes](pages/bousquet-melou-fedou-1995-convex-polyominoes.md)] Property 3.2, p.63 L499-512 - "Let E = Jbar_1 Kbar_0 - Jbar_0 Kbar_1. Then E has the very simple following expansion: E = sum_{n≥0} x^n q^n/(q)_n ... Jbar_1/E = Jhat_1, Jbar_0/E = Jhat_0, Kbar_1/E = Khat_1, Kbar_0/E = Khat_0" (read from the page image).
[^14]: [[bousquet-melou-fedou-1995-convex-polyominoes](pages/bousquet-melou-fedou-1995-convex-polyominoes.md)] p.60 L339-351 [synthesis] - the `q -> 1` limit of the parallelogram series is `J_1/J_0` with `J_0 = sum (-1)^n x^n / n!^2`. The link to `mu` is https://oeis.org/A276994 (fetched 2026-09-22) - "1/A276994 ... is the smallest positive root of the equation Sum_{n>=0} ((-1)^n * z^(n*(n+1)/2) / (Product_{k=1..n} 1-z^k)^2) = 0", which is `J_0` at `x = y = 1`. Reading the shared `mu` off the shared denominator is own reasoning, not the paper's; the prefactor fits in the Verification section are consistent with it.
[^15]: [[bousquet-melou-fedou-1995-convex-polyominoes](pages/bousquet-melou-fedou-1995-convex-polyominoes.md)] pp.60-61 L357-371, L416-433 - "so we now have to find the 'right' q-analogue of the odd part of the series J_1 ... which is obviously more difficult to guess than it was in the case of parallelogram polyominoes"; the homogeneous solutions (8) use `Ybar_0 = Kbar_0 + Jbar_0 log(x)`, `Ybar_1 = Kbar_1 + Jbar_1 log(x)` (read from the page image).
[^16]: [[bousquet-melou-fedou-1995-convex-polyominoes](pages/bousquet-melou-fedou-1995-convex-polyominoes.md)] §5, p.71 L914-949 - "It has been proved in [3] that the generating function for convex polyominoes of width n is a rational function"; eq. (14) and the `Q_n` list read from the page image; "We conjecture that the Q_n have positive coefficients and are unimodal."
[^17]: [[bousquet-melou-fedou-1995-convex-polyominoes](pages/bousquet-melou-fedou-1995-convex-polyominoes.md)] p.55 L117-135 - "the generating functions according to height and width are all algebraic series ... exemplified by the bivariate generating function on convex polyominoes for height and width, obtained by Lin and Chang [13]"; "the formula of Lin and Chang refines the perimeter generating function given by Delest and Viennot [10]" (formula read from the page image).
[^18]: [[bousquet-melou-fedou-1995-convex-polyominoes](pages/bousquet-melou-fedou-1995-convex-polyominoes.md)] Table 1, p.72 L954-979 - "The number of polyominoes with given area", columns Parallelogram, Directed and convex, Convex, `n = 1..20`, ending "20 5 526 198 12229 209 53974959".
[^19]: [[bousquet-melou-fedou-1995-convex-polyominoes](pages/bousquet-melou-fedou-1995-convex-polyominoes.md)] p.59 L305-308 - "There exists also an asymptotic result simultaneously proved by Bender on the one hand, Klarner and Rivest on the other hand [2, 12]: the number of convex polyominoes of area n is asymptotically Ca^n, where C ≃ 2.67564 and a ≃ 2.30914."
[^20]: Verified by execution, 2026-09-22. Theorem 3.1 (eq. 9) evaluated at `x = y = 1` from the Appendix A series to `q^120`; compared with https://oeis.org/A006958/b006958.txt, https://oeis.org/A067675/b067675.txt, https://oeis.org/A067676/b067676.txt (fetched 2026-09-22), no mismatch at any `n <= 120`. The prefactor column uses `mu = 1/0.4330619231293906645846169654189837` from https://oeis.org/A276994, and the OEIS prefactors are the `c` values on https://oeis.org/A006958 and https://oeis.org/A067675 (fetched 2026-09-22). The width check uses the column sweep of [[convex-polyomino-by-area](pages/convex-polyomino-by-area.md)] restricted to a fixed width. The A005436 terms are from https://oeis.org/A005436 (fetched 2026-09-22).
[^21]: [[bousquet-melou-fedou-1995-convex-polyominoes](pages/bousquet-melou-fedou-1995-convex-polyominoes.md)] Fig. 2, p.55 L100-106 - "Different subclasses of convex polyominoes"; the marked corners are read from the page image.
