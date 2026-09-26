---
title: Salem number (class T)
category: Concepts
summary: A real algebraic integer τ > 1 whose other conjugates lie on or inside the unit circle, at least one on it (Salem's class T). The minimal polynomial is palindromic of even degree ≥ 4, τ is a unit, and y = z + 1/z halves it to a totally real polynomial. Every Pisot number is a two-sided limit of Salem numbers through zᵐP ± Q; applied to the plastic number at m = 8 this gives Lehmer's polynomial exactly, and the same construction on castle cubics produces most small Salem numbers the castle censuses find. Powers of τ are dense mod 1 but not uniformly distributed.
tags: [concept, salem-number, pisot-number, algebraic-integer, reciprocal-polynomial, palindromic, lehmer, mahler-measure, uniform-distribution, castle, growth-constant, plastic-number]
sources: [salem-1963-algebraic-numbers-fourier-analysis]
created: 2026-09-25
updated: 2026-09-25
---

# Salem number (class T)

## Description

A **Salem number** is a real algebraic integer `τ > 1` whose other conjugates all lie inside or on the unit circle, with at least one actually on it. Otherwise it would be Pisot ([[pisot-number](pages/pisot-number.md)]). Salem calls the set **the class T**.[^1]

**The shape is forced.** A conjugate `α` on the circle is not `±1`, so `ᾱ = 1/α` is also a root. Irreducibility then makes the minimal polynomial `P` **reciprocal** (palindromic). So:[^2]

- `1/τ` is a root too, and it is the only root inside the circle; `τ` is the only root outside;
- the roots on the circle come in conjugate pairs, so the degree is even and at least 4;
- `τ` is a unit.

**The trace polynomial.** Writing `y = z + 1/z` turns the degree-`2k` polynomial `P` into a degree-`k` polynomial `R(y)` with all roots real. One root, `τ + 1/τ`, is above 2, and the rest lie in `(−2, 2)`: each is `2cos(2πω)` for a unit-circle pair.[^2] So a Salem number is the lift of a totally real algebraic integer with exactly one conjugate outside `[−2, 2]`. Compare the `Q(ζ₇)⁺` cubic `2cos(π/7)` on [[pisot-number](pages/pisot-number.md)], which is totally real with every conjugate inside `(−2, 2)`.

The castle censuses have their own Salem numbers. Width-graded strip rules have 7 Salem quartics at height 4 ([[reachable-field-census](pages/reachable-field-census.md)]). Area-graded rules have 4 new Salem constants at height 3 and 29 at height 4, among them most of the small Salem numbers known ([[area-growth-census](pages/area-growth-census.md)]).

## Salem's theorems about class T

- **Characterization (Theorem III).** For real `τ > 1`, there is a real `μ ≠ 0` such that `Σ {μτ^n} z^n` has real part bounded above in the unit disc, without lying in the Hardy space `H²`, if and only if `τ` is a Salem number. Here `{α}` is the signed distance to the nearest integer. `μ` is then algebraic in `Q(τ)`. This is the Salem-number counterpart of the Pisot characterization `Σ‖λθ^n‖² < ∞`.[^3]
- **Every Pisot number is a limit of Salem numbers from both sides (Theorem IV).** Let `P` be the minimal polynomial of a Pisot `θ` (not a quadratic unit) and `Q(z) = z^p P(1/z)` its reversal. By Rouché's theorem, `R_m = z^m P + Q` has exactly one root outside the unit circle, which tends to `θ` from one side. `(z^m P − Q)/(z − 1)` gives roots from the other side. Both polynomials are reciprocal, so for large `m` the roots are Salem numbers, of unbounded degree. Quadratic units use Chebyshev polynomials instead: `(x − r)T_m(x) ∓ 1` with `y + 1/y = x`.[^4]
- **Open (Salem's unsolved problem 2).** Whether Salem numbers have any limit points besides Pisot numbers.[^5]
- **Powers are dense but not uniform (§5, Theorem V).** Modulo 1, `τ^m ≡ −τ^{−m} − Σ 2cos(2πmω_j)`, where `ω_1, …, ω_{k−1}, 1` are linearly independent (an argument Salem credits to Pisot). Kronecker's theorem then makes the powers dense mod 1. They are not uniformly distributed, because the distribution function of `2cos 2πx` mod 1 is not linear, witnessed by `∫₀¹ e^{2πih·2cos 2πx} dx = J₀(4πh) ≠ 0`.[^6] So Pisot numbers have powers converging to integers, Salem numbers have powers that are dense without being uniform, and almost every real number has uniformly distributed powers (Koksma).
- **Exercise.** Every Salem number is a quotient `θ/θ'` of two Pisot numbers from its own field.[^7]

## Theorem IV on castle Pisot numbers

Running Salem's construction on four castle cubics: the plastic number `ψ`, supergolden, tribonacci and `ψ²`. For each `m`, the table gives the dominant root of the irreducible factor carrying it. `+` is `z^m P + Q`, approaching `θ` from above. `−` is `(z^m P − Q)/(z − 1)`, approaching from below. `·` means the quotient has no root outside the unit circle at that `m` (it is a product of cyclotomic factors).[^exec]

| `m` | plastic `ψ = 1.3247` `+` / `−` | supergolden `1.4656` `+` / `−` | tribonacci `1.8393` `+` / `−` | `ψ² = 1.7549` `+` / `−` |
|---|---|---|---|---|
| 1 | **`2.081019`** / · | **`2.296630`** / · | **`2.890054`** / · | Pisot `φ²` / · |
| 2 | **`1.722084`** / · | **`1.883204`** / · | **`2.296630`** / · | **`2.153721`** / · |
| 3 | **`1.582347`** / · | **`1.722084`** / · | **`2.081019`** / · | `1.974819` / · |
| 4 | **`1.506136`** / · | **`1.635573`** / · | `1.974819` / **`1.582347`** | **`1.883204`** / **`1.506136`** |
| 5 | `1.457987` / · | **`1.582347`** / · | `1.916498` / **`1.722084`** | **`1.831076`** / **`1.635573`** |
| 6 | `1.425005` / · | `1.547197` / **`1.280638`** | **`1.883204`** / **`1.781644`** | `1.800172` / `1.693507` |
| 7 | **`1.401268`** / · | `1.523060` / `1.360000` | `1.864060` / `1.809789` | **`1.781644`** / **`1.722084`** |
| 8 | `1.383637` / `1.176281` (Lehmer) | **`1.506136`** / **`1.401268`** | `1.853128` / `1.823835` | `1.770569` / `1.736942` |
| 9 | `1.370268` / **`1.230391`** | `1.494151` / `1.425005` | `1.846956` / **`1.831076`** | `1.764006` / `1.744922` |
| 10 | `1.360000` / **`1.261231`** | `1.485642` / `1.439399` | `1.843509` / `1.834885` | `1.760155` / `1.749299` |
| 11 | `1.352050` / **`1.280638`** | `1.479609` / `1.448423` | `1.841601` / `1.836914` | `1.757914` / `1.751732` |
| 12 | `1.345869` / **`1.293486`** | `1.475348` / `1.454212` | `1.840551` / `1.838003` | `1.756619` / `1.753097` |

Bold entries are Salem numbers that also appear as castle growth constants: among the Salem values [[area-growth-census](pages/area-growth-census.md)] tabulates by height 4, or among the height-4 width-census quartics ([[reachable-field-census](pages/reachable-field-census.md)]). Unbolded values may still be among the area census's 33 Salem constants that it does not list individually.

- **Lehmer's number is the plastic number's `m = 8` descendant.** Exactly:

  ```
  (x^8 (x^3 − x − 1) + x^3 + x^2 − 1) / (x − 1)  =  x^10 + x^9 − x^7 − x^6 − x^5 − x^4 − x^3 + x + 1
  ```

  That is Lehmer's polynomial, whose root `1.176280…` is the smallest Salem number known. [[area-growth-census](pages/area-growth-census.md)] finds no height-4 area rule growing at it, while the plastic number itself is already a height-2 area constant. So Lehmer's number is one Salem-construction step from a castle constant, even though the census has not realized it. The identity was verified here by exact expansion; it is likely classical, and no literature source for it has been read.[^exec]
- **The rest of the small Salem list descends the same way.** The plastic number's minus side at `m = 9..12` gives `1.230391`, `1.261231`, `1.280638`, `1.293486`, four of the five small Salem numbers the area census does realize. Of the degree-4 and degree-6 area-census Salem numbers (`1.401268` through `1.883204`), all but `1.556030` come from these four cubics at small `m`.
- **Six of the seven width-census Salem quartics are `m ≤ 3` outputs** of these four cubics (`1.722084`, `1.883204`, `2.081019`, `2.153721`, `2.296630`, `2.890054`). The seventh, `2.369205` (`x⁴ − x³ − 3x² − x + 1`), is not among them.
- **Collisions.** `1.722084` descends from all four Pisot parents: `ψ` (`m = 2`), supergolden (`m = 3`), tribonacci (`m = 5`, minus side) and `ψ²` (`m = 7`, minus side). Theorem IV sequences cross, which is why a Salem number does not remember one Pisot parent.

```python
import sympy as sp
x = sp.Symbol('x')
def salem_step(P, m, sign=+1):
    """Theorem IV: z^m P + Q (sign=+1) or (z^m P - Q)/(z - 1) (sign=-1); Q is P reversed."""
    Q = sp.expand(x**sp.degree(P, x) * P.subs(x, 1/x))
    return sp.factor(sp.expand(x**m*P + Q) if sign > 0 else sp.cancel((x**m*P - Q)/(x - 1)))
salem_step(x**3 - x - 1, 8, -1)   # x**10 + x**9 - x**7 - x**6 - x**5 - x**4 - x**3 + x + 1
```

## Appearances in Sources

- [[salem-1963-algebraic-numbers-fourier-analysis](pages/salem-1963-algebraic-numbers-fourier-analysis.md)] - Chapter III: definition and structure of class T, Theorems III-V, the Pisot-quotient exercise; unsolved problem 2.

## Related Concepts

- [[pisot-number](pages/pisot-number.md)] - class S, the limit points of class T.
- [[area-growth-census](pages/area-growth-census.md)] - Salem numbers as area growth constants; Lehmer's number as its open min-height question.
- [[reachable-field-census](pages/reachable-field-census.md)] - the 7 Salem quartics among the height-4 width growth constants.
- [[plastic-number](pages/plastic-number.md)] - the Pisot parent of Lehmer's number under Theorem IV.
- [[bounded-height-castles-nacci](pages/bounded-height-castles-nacci.md)] - tribonacci, one of the four parents in the table.
- [[tree-castle-by-area](pages/tree-castle-by-area.md)] - supergolden and `ψ²`, the other parents.

## Footnotes

[^1]: [[salem-1963-algebraic-numbers-fourier-analysis](pages/salem-1963-algebraic-numbers-fourier-analysis.md)] Ch. III §3 p.26 L1740-1742 [synthesis] - "A number T belongs to the class T if it is an algebraic integer whose conjugates all lie inside or on the unit circle, assuming that some conjugates lie actually on the unit circle (for otherwise T would belong to the class S)."
[^2]: [[salem-1963-algebraic-numbers-fourier-analysis](pages/salem-1963-algebraic-numbers-fourier-analysis.md)] Ch. III §3 p.26 [synthesis] L1743-1756 - roots `α` and `1/α` on the unit circle; "P is a reciprocal polynomial; T is its only root outside, and 1/T its only root inside, the unit circle"; even degree "at least equal to 4"; "T is a unit"; with `y = z + 1/z`, `R(y)` of degree k with all roots real, `τ + τ^{−1}` "larger than 2, and all others lie between −2 and +2".
[^3]: [[salem-1963-algebraic-numbers-fourier-analysis](pages/salem-1963-algebraic-numbers-fourier-analysis.md)] Ch. III §3 Theorem III pp.27-29 [synthesis] L1768-2064 - a real `μ ≠ 0` with the real part of `Σ{μτ^n}z^n` bounded above "(without belonging to the class H2)" exists iff τ is in class T; μ algebraic in the field of τ; sufficiency via Minkowski and a Pisot number of the field of `τ + 1/τ`.
[^4]: [[salem-1963-algebraic-numbers-fourier-analysis](pages/salem-1963-algebraic-numbers-fourier-analysis.md)] Ch. III §4 Theorem IV pp.30-31 [synthesis] L2066-2160 - "Every number of the class S is a limit point of numbers of the class T on both sides"; `R_m(z) = z^m P(z) + Q(z)`, Rouché, the root `τ_m → θ`; "there exist numbers of the class T of arbitrarily large degree"; `(z^m P − Q)/(z − 1)` "which is also reciprocal" for the other side; quadratic units via `(x − r)T_m(x) ∓ 1` with the Chebyshev polynomial `T_m`.
[^5]: [[salem-1963-algebraic-numbers-fourier-analysis](pages/salem-1963-algebraic-numbers-fourier-analysis.md)] Ch. III §4 p.31 L2161 - "We do not know whether numbers of T have limit points other than numbers of S."; restated as unsolved problem 2, L4188-4190.
[^6]: [[salem-1963-algebraic-numbers-fourier-analysis](pages/salem-1963-algebraic-numbers-fourier-analysis.md)] Ch. III §5 pp.32-35 [synthesis] L2167-2484 - the powers of τ "are, modulo 1, everywhere dense in the interval (0, 1)"; linear independence of `ω_1, …, ω_{k−1}, 1` ("This argument is due to Pisot"); Kronecker's theorem; Theorem V (not uniformly distributed); the distribution-function lemma; `∫ e^{2πih·2cos 2πx} dx = J_0(4πh)`.
[^7]: [[salem-1963-algebraic-numbers-fourier-analysis](pages/salem-1963-algebraic-numbers-fourier-analysis.md)] Ch. III Exercise p.35 L2486-2487 - "Show that any number T of the class T is the quotient θ/θ' of two numbers of the class S belonging to the field of T."
[^exec]: Verified by execution (2026-09-25, own computation; SymPy 1.14 `factor_list`, roots at 30 digits, Salem = one root outside the circle, one inside, the rest of modulus 1 within `10⁻⁷`): Theorem IV for the four cubics, `m = 1..12`, both sides; Lehmer's polynomial checked by exact expansion (`sp.cancel` of the `m = 8` minus-side quotient equals it identically). Bold marks by comparison with the Salem values tabulated on [[area-growth-census](pages/area-growth-census.md)] and the height-4 width census (65 536 binary `4×4` matrices, quartic factors carrying the Perron root: 7 Salem, 41 Pisot, 62 neither).
