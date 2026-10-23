---
title: Reachable-field census of castle-strip growth constants
category: Analyses
summary: An exhaustive census, for h ≤ 5, of the Perron roots of the 2^{h²} 0/1 transfer matrices of castle strips on the heights 1..h, sorted by number field. Every real quadratic field Q(√d) is reached at some height, through the larger root of x² − p₁x − p₂ with p₁ ≥ 0, p₂ ≥ 1, whose field is set by the squarefree part of p₁² + 4p₂; Perron roots with p₂ < 0 also occur (φ², from x² − 3x + 1, at h = 3). The roots with p₁, p₂ ≥ 1 are de Spinadel's metallic means σ_{p₁}^{p₂}, and the δ_a are the line p₂ = 1: every δ_a first appears at height a + 1, and δ_4 = φ³ lies in Q(√5). The fields reached by heights 2, 3, 4, 5 are {5}, {2, 3, 5}, {2, 3, 5, 13, 17, 21}, {2, 3, 5, 6, 7, 13, 17, 21, 29, 33}. Nine cubic Perron roots appear at h = 3, among them the plastic number, the supergolden constant, ψ², the tribonacci constant and two cubics of Q(ζ₇)⁺. At h = 4 the 184 distinct positive Perron roots are 4 integers, 14 quadratic (6 fields), 56 cubic and 110 quartic; at h = 5 the 5,978 are 5, 29 (10 fields), 253, 1,355 and 4,336 of degrees 1 to 5.
tags: [analysis, castle, growth-constant, transfer-matrix, perron-root, number-field, metallic-mean, plastic-number, census, pisot, quadratic-field, sympy, verification]
sources: [pe502-pell-castle-strip]
created: 2026-09-18
updated: 2026-10-16
---

# Reachable-field census of castle-strip growth constants

## The question and the method

Which algebraic numbers are the growth rates of castle strips, and which number fields do they lie in?

**Castle strips.** A strip on the heights `1, …, h` is a skyline whose column heights lie in `{1, …, h}`, under a rule saying which height may follow which. Strips need not reach height `h`, so they need not be castles of height `h`; the strips that reach `h` are the castles of height `h` of the rule's family ([[castle-strip](pages/castle-strip.md)]). The rule is a 0/1 **transfer matrix** `M`, with `M[a][b] = 1` when a column of height `a` may be followed by one of height `b`.

**The growth rate.** The number of strips of width `w` is `N(w) = 𝟙ᵀ M^{w−1} 𝟙`, the sum of the entries of `M^{w−1}`, and by Gelfand's formula `N(w)^{1/w} → ρ(M)`, the largest eigenvalue of `M`, its **Perron root**.

**The number field.** `ρ` is a root of the characteristic polynomial of `M`, an integer polynomial, so it is an algebraic integer. Its **minimal polynomial** is the irreducible factor of the characteristic polynomial that has `ρ` as a root, and its **number field** is `Q(ρ)`. A quadratic `ρ` has `Q(ρ) = Q(√d)` for a squarefree integer `d`, and the field is named by `d`.

*Example, `h = 2`.* The rule "no two adjacent height-2 columns" is `M = [[1, 1], [1, 0]]`, with characteristic polynomial `x² − x − 1`, Perron root the golden ratio `φ`, field `Q(√5)`, and `N(w) = F_{w+2}` strips of width `w`.

The census runs over all `2^{h²}` 0/1 matrices for `h = 2, 3, 4, 5`. For each matrix it computes the characteristic polynomial exactly; for each distinct polynomial it factors over the integers, takes the irreducible factor whose largest real root is the Perron root, and reads the field from that factor: degree 1 is rational, degree 2 gives `Q(√d)` with `d` the squarefree part of the discriminant, degree 3 or more gives a cubic, quartic or quintic field. The factorization and the field are exact; floating point only selects the factor carrying the Perron root.[^1]

## In one function

The step behind the census, from a rule to its Perron root and field, is a short function:

```python
import sympy as sp
x = sp.Symbol('x')

def strip_field(M):
    """Perron root and number field of ONE 0/1 strip transfer matrix."""
    p = sp.Matrix(M).charpoly(x).as_expr()
    rho, f = -sp.oo, None
    for g, _ in sp.factor_list(p)[1]:               # factor first: irreducible factors have simple roots
        g = sp.Poly(g, x)
        rr = [complex(z).real for z in sp.nroots(g, n=25) if abs(complex(z).imag) < 1e-8]
        if rr and max(rr) > rho:
            rho, f = max(rr), g
    d = f.degree()
    if d == 1: return sp.N(rho, 8), "Q"
    if d == 2:
        a, b, c = f.all_coeffs()                    # a x^2 + b x + c
        D = b*b - 4*a*c
        sq = sp.Mul(*[q for q, e in sp.factorint(D).items() if e % 2])   # squarefree part of D
        return sp.N(rho, 8), f"Q(sqrt({sq}))" if sq != 1 else "Q"
    return sp.N(rho, 8), f"deg {d} ({f.as_expr()})"
```

```
>>> strip_field([[1,1],[1,0]])                              # golden, h=2: no two adjacent height-2 columns
(1.6180340, 'Q(sqrt(5))')
>>> strip_field([[0,1,1],[1,0,1],[1,1,1]])                  # silver, h=3: ridge R_3 = J - D
(2.4142136, 'Q(sqrt(2))')
>>> strip_field([[0,1,1,1],[1,0,1,1],[1,1,0,1],[1,1,1,1]])  # bronze, h=4: ridge R_4 = J - D
(3.3027756, 'Q(sqrt(13))')
>>> strip_field([[0,0,1],[1,0,0],[1,1,0]])                  # plastic, h=3: the companion of x^3 - x - 1, relabeled
(1.3247180, 'deg 3 (x**3 - x - 1)')
```

The census loops this step over all `2^{h²}` matrices and sorts the results; `strip_field_census` on [[castle-snippets-strips](pages/castle-snippets-strips.md)] is that loop.

## The quadratic fields

Sorting every quadratic Perron root by its field `Q(√d)`:

| `h` | `d` reached by height `h` (new at `h` in **bold**) | new `δ_a` | new fields off the line `p₂ = 1` |
|---|---|---|---|
| 2 | **5** | golden `φ` (`Q(√5)`) | - |
| 3 | **2**, **3**, 5 | silver `1 + √2` (`Q(√2)`) | `Q(√3)` |
| 4 | 2, 3, 5, **13**, **17**, **21** | bronze `(3 + √13)/2` (`Q(√13)`) | `Q(√17)`, `Q(√21)` |
| 5 | 2, 3, 5, **6**, **7**, 13, 17, 21, **29**, **33** | `δ_4 = 2 + √5` (`Q(√5)`, not new) | `Q(√6)`, `Q(√7)`, `Q(√29)` (through `(3 + √29)/2`), `Q(√33)` |

### The fields of the δ_a; δ_4 adds none

The metallic mean `δ_a = (a + √(a² + 4))/2` lies in `Q(√(a² + 4))`, whose field depends only on the squarefree part of `a² + 4`:[^2]

| `a` | `a² + 4` | squarefree part | field |
|---|---|---|---|
| 1 (golden) | 5 | 5 | `Q(√5)` |
| 2 (silver) | 8 = 4·2 | 2 | `Q(√2)` |
| 3 (bronze) | 13 | 13 | `Q(√13)` |
| 4 | 20 = 4·5 | 5 | `Q(√5)`, not new |
| 5 | 29 | 29 | `Q(√29)` |
| 6 | 40 = 4·10 | 10 | `Q(√10)` |

The census reaches each of these fields: `Q(√5)` at `h = 2`, `Q(√2)` at `h = 3`, `Q(√13)` at `h = 4`, and the field of `δ_5`, `Q(√29)`, at `h = 5` through `σ_3^5 = (3 + √29)/2 = 4.1926`, the root of `x² − 3x − 5`; `δ_5 = 5.1926` itself first appears at `h = 6`. `δ_4` adds no field, since `20 = 4·5`. Every `δ_a` is a unit of norm `−1`, the units of `Z[φ]` are `±φ^n`, and `δ_4 = 2 + √5 = 1 + 2φ` lies in `Z[φ]`, so `δ_4 = φ³`. The ridge strips of height 5, whose growth constant is `δ_4`, number `F_{3w+2}` at width `w` ([[metallic-strip-realizability](pages/metallic-strip-realizability.md)], [[ridge-castle](pages/ridge-castle.md)]).[^3]

### The minimum height of δ_a is a + 1

The ridge rule `R_h = J − D`, with `J` the all-ones matrix and `D = diag(1, …, 1, 0)`, lets neighboring columns have equal height only at the ceiling `h`; its Perron root is `δ_{h−1}` ([[ridge-castle](pages/ridge-castle.md)], [[metallic-strip-realizability](pages/metallic-strip-realizability.md)]). So `δ_a` is reached by height `a + 1`. No smaller height reaches it: a 0/1 matrix of size `h` has Perron root at most its largest row sum, which is at most `h`, and `a < δ_a < a + 1`, so `δ_a` needs `h ≥ a + 1`. [[quadratic-min-height](pages/quadratic-min-height.md)] has the minimum height of every quadratic Perron root through height 6.[^3]

The elements of `Q(√5)` that are Perron roots also depend on the height. The census finds `φ` at `h = 2`; `φ² = (3 + √5)/2` at `h = 3`; `2φ = 1 + √5` at `h = 4`; and `√5`, `(5 + √5)/2` and `φ³ = δ_4` at `h = 5`.[^4]

### The quadratic fields off the line p₂ = 1

Besides the fields of the `δ_a`, the census reaches `Q(√3)` at `h = 3`, `Q(√17)` and `Q(√21)` at `h = 4`, and `Q(√6)`, `Q(√7)` and `Q(√33)` at `h = 5`, through roots of `x² − p₁x − p₂` with `p₂ ≠ 1`. Those with `p₁, p₂ ≥ 1` are de Spinadel's metallic means `σ_{p₁}^{p₂}` ([[de-spinadel-1999-family-of-metallic-means](pages/de-spinadel-1999-family-of-metallic-means.md)]), such as `σ_2^2 = 1 + √3` in `Q(√3)`; those with `p₁ = 0` (`√p₂`) or `p₂ < 0` (such as `φ²`) are outside the family. `Q(√17)` contains `δ_8 = 4 + √17`, since `8² + 4 = 4·17`, which no height up to 5 reaches. The other five fields contain no `δ_a`: `a² + 4 ≡ 0` has no solution mod 3, since 2 is not a square mod 3, and none mod 7, since 3 is not a square mod 7, so neither 3 nor 7 divides the squarefree part of any `a² + 4`.

## Cubics at h = 3, including the plastic number

Nine cubic minimal polynomials occur at `h = 3`:[^5]

| minimal polynomial | Perron root | | matrices (`h = 3`) |
|---|---|---|---|
| `x³ − x − 1` | `1.3247` | the plastic number `ψ` ([[plastic-number](pages/plastic-number.md)]) | 6 |
| `x³ − x² − 1` | `1.4656` | the supergolden constant ([[tree-castle-by-area](pages/tree-castle-by-area.md)]) | 6 |
| `x³ − 2x² + x − 1` | `1.7549` | `ψ²` | 6 |
| `x³ − x² − 2x + 1` | `1.8019` | `2cos(π/7)`, in `Q(ζ₇)⁺` | 6 |
| `x³ − x² − x − 1` | `1.8393` | the tribonacci constant ([[castles-of-height-h-by-area](pages/castles-of-height-h-by-area.md)]) | 12 |
| `x³ − x² − 2x − 1` | `2.1479` | | 6 |
| `x³ − 2x² − 1` | `2.2056` | | 6 |
| `x³ − 2x² − x + 1` | `2.2470` | `1 + 2cos(2π/7)`, in `Q(ζ₇)⁺` | 12 |
| `x³ − 3x² + 2x − 1` | `2.3247` | `ψ + 1 = ψ³`, a Pisot number | 6 |

The plastic number is the Perron root of 6 matrices at `h = 3`. The sparsest has 4 ones, the rule `1 → 3`, `2 → 1`, `3 → {1, 2}`, which is the companion matrix of `x³ − x − 1` with the heights relabeled (as `2 → 1 → 3 → {2, 1}`), so the strips of this rule are plastic by width ([[plastic-number](pages/plastic-number.md)]). It has `3, 4, 5, 7, 9, 12, 16, 21, 28, …` strips of width `w`, the Padovan numbers `A000931(w + 9)`, the same numbers as the maximal Fibonacci castles of width `w + 3` ([[fibonacci-castles-sub-families](pages/fibonacci-castles-sub-families.md)]).[^5]

At `h = 4` there are 184 distinct positive Perron roots: 4 integers, 14 quadratic (in 6 fields), 56 cubic (among them `2^{1/3} = 1.2599`, the root of `x³ − 2`) and 110 quartic. At `h = 5` there are 5,978: 5 integers, 29 quadratic (in 10 fields), 253 cubic, 1,355 quartic and 4,336 quintic.[^6]

## Every real quadratic field is reached

Write the minimal polynomial of a quadratic Perron root as `x² − p₁x − p₂`. The Perron root is the larger root, and its field is `Q(√d)` with `d` the squarefree part of the discriminant `p₁² + 4p₂`. `p₂` can be negative: `φ²`, the root of `x² − 3x + 1`, is a Perron root at `h = 3`, and `(p₁, p₂) = (4, −2)` and `(4, −1)` occur at `h = 4`.[^7]

1. **Every real quadratic field occurs as the field of some pair.** For `p₁ = 0` the discriminant is `4p₂`, whose squarefree part is that of `p₂`, so the pairs `(0, d)` give every squarefree `d ≥ 2`. Over all `p₁ ≥ 0, p₂ ≥ 1` the discriminant `p₁² + 4p₂ ≡ p₁² (mod 4)` takes every value `≥ 4` that is `≡ 0` or `1 (mod 4)`.[^8]
2. **The metallic means are the quadrant `p₁, p₂ ≥ 1`, and the `δ_a` are its line `p₂ = 1`.** The larger root of `x² − p₁x − p₂` with `p₁, p₂ ≥ 1` is `σ_{p₁}^{p₂}`, and `p₂ = 1` gives `δ_{p₁}`: the roots of norm `−1`, with continued fraction `[a; a, a, …]` ([[eigenvalue-continued-fractions](pages/eigenvalue-continued-fractions.md)]).
3. **Every pair with `p₁ ≥ 0, p₂ ≥ 1` is the Perron root of a 0/1 matrix.** The multigraph with adjacency matrix `[[p₁, p₂], [1, 0]]` has `p₁ + p₂ + 1` edges; the 0/1 matrix with one state per edge, and a 1 from edge `e` to edge `f` when `f` starts where `e` ends, has the same nonzero eigenvalues, a standard recoding of symbolic dynamics. So every real quadratic field is the field of a castle-strip Perron root at some height. The minimum height of a pair is computed exactly through height 6, and proved on the line `p₂ = 1`, on the line `p₁ = 0` and on the triangle `1 ≤ p₂ ≤ p₁`, on [[quadratic-min-height](pages/quadratic-min-height.md)]; the per-height field lists of this page are its level sets.[^9]

`Q(√11)` is not reached by height 5. The smallest discriminant with squarefree part 11 is 44, since `11 ≡ 3 (mod 4)` is not a discriminant, and its pairs are `(0, 11)`, `(2, 10)`, `(4, 7)` and `(6, 2)`; `(4, 7)` has minimum height 6 ([[quadratic-min-height](pages/quadratic-min-height.md)]), so `Q(√11)` first appears at height 6, with the Perron root `2 + √11`.

## Results

- Every real quadratic field is the field of a castle-strip Perron root, through `x² − p₁x − p₂` with `p₂ ≥ 1`. The roots with `p₁, p₂ ≥ 1` are the metallic means `σ_{p₁}^{p₂}`, and the `δ_a` are the line `p₂ = 1`.
- Every `δ_a` first appears at height `a + 1`; `δ_4 = φ³` lies in `Q(√5)`.
- The plastic number is a castle-strip Perron root at `h = 3`.
- Nine cubic Perron roots appear at `h = 3`: the plastic number, the supergolden constant, `ψ²`, the tribonacci constant, `ψ³`, two cubics of `Q(ζ₇)⁺` and two others. The supergolden constant, `ψ²` and the tribonacci constant are also growth constants by area.

## Heights 6 and above

The spectrum of a matrix is unchanged by relabeling the heights, `M → PMPᵀ` for a permutation matrix `P`, so the census could keep one matrix per orbit. Keeping the lexicographically smallest member of each orbit reproduces the field lists `{5}`, `{2, 3, 5}` and `{2, 3, 5, 13, 17, 21}` for `h ≤ 4`, with 3,044 orbits among the 65,536 matrices at `h = 4`.[^10] At `h = 6` there are at least `2^{36}/720 ≈ 9.5 × 10⁷` orbits, and at `h = 7` at least `2^{49}/5040 ≈ 1.1 × 10^{11}`. [[quadratic-min-height](pages/quadratic-min-height.md)] instead enumerates the 1.28 billion `6 × 6` matrices with rows sorted by number of ones and finds every quadratic Perron root through height 6.

The new fields at `h = 6` need dense matrices: the matrices with at most 6 ones among their 36 entries reach only the fields `{2, 3, 5}`, while the ridge matrix `R_6 = J − D`, whose Perron root is `δ_5`, has 31 ones.[^11] The ridge matrices give `δ_5 ∈ Q(√29)` at `h = 6`, with characteristic polynomial `(x + 1)⁴(x² − 5x − 1)`, and `δ_6 = 3 + √10` at `h = 7`. The field `Q(√10)` first appears at `h = 6`, through `(p₁, p₂) = (4, 6)` (`2 + √10`) and `(2, 9)` (`1 + √10`), while `(6, 1)` and `(0, 10)` need height 7.[^12]

## Reproduce

`strip_field` (the field of one rule's Perron root), `strip_field_census` (the sweep, with the Perron roots sorted numerically and the fields identified exactly), `sh_canonical` (one matrix per relabeling orbit, checked against the full census) and `ridge_R` (the ridge matrix `R_h = J − D`) are on [[castle-snippets-strips](pages/castle-snippets-strips.md)].

## Appearances in Sources

- [[pe502-pell-castle-strip](pages/pe502-pell-castle-strip.md)] - the transfer-matrix model of strips that the census sweeps.

## Related Concepts

- [[quadratic-min-height](pages/quadratic-min-height.md)] - the minimum height of each quadratic Perron root `(p₁, p₂)`: exact through height 6, proved on the lines `p₂ = 1` and `p₁ = 0` and on the triangle `1 ≤ p₂ ≤ p₁`.
- [[metallic-strip-realizability](pages/metallic-strip-realizability.md)] - the ridge rule `R_h = J − D`, whose Perron root is `δ_{h−1}`.
- [[ridge-castle](pages/ridge-castle.md)] - the ridge castles, with the ridge strip counts `A001333(w + 1)`, `A003688(w + 1)`, `A015448(w + 1)` at heights 3, 4, 5.
- [[metallic-means](pages/metallic-means.md)] - de Spinadel's family `σ_p^q`, with `δ_a = σ_a^1`; this census places the field of each `δ_a`.
- [[plastic-number](pages/plastic-number.md)] - the plastic number and `ψ²`, Perron roots of 0/1 strip matrices at `h = 3`.
- [[castles-of-height-h-by-area](pages/castles-of-height-h-by-area.md)] and [[tree-castle-by-area](pages/tree-castle-by-area.md)] - the tribonacci constant, the supergolden constant and `ψ²` as growth constants by area.
- [[castle-classification-growth](pages/castle-classification-growth.md)] - growth types of castle families, "X by width" and by the other axes.
- [[eigenvalue-continued-fractions](pages/eigenvalue-continued-fractions.md)] - the `δ_a` as the norm `−1` quadratics with continued fraction `[a; a, a, …]`.
- [[fractional-recurrences](pages/fractional-recurrences.md)] - the growth constant `g(α)` of `∇^α a_n = a_{n−1}`, a continuous increasing curve that passes through three of this page's cubics at rational `α` (the supergolden constant at `1/3`, `ψ²` at `2/3`, `ψ³` at `3/2`). At an algebraic irrational `α`, `g(α)` is transcendental by the Gelfond-Schneider theorem, so no 0/1 matrix has it as its Perron root.
- [[power-law-memory-rules](pages/power-law-memory-rules.md)] - at `h = 2` the Perron roots `ρ(α, K)` of the truncated fractional rules include the plastic number, the supergolden constant and `ψ²`, three of the cubics at `h = 3` here; they are nondecreasing in `K` and at most 2.

## Footnotes

[^1]: Method verified by execution (Python 3.11 with NumPy and SymPy, 2026-10-16): for each `h ≤ 5`, all `2^{h²}` binary matrices, characteristic polynomials computed exactly in 64-bit integers by the Faddeev-LeVerrier recursion and deduplicated; each distinct polynomial factored with SymPy `factor_list`, the irreducible factor carrying the largest real root selected numerically, and its degree and discriminant giving the field.

[^2]: The squarefree part is `d = ∏ p^{e mod 2}` over the factorization of `a² + 4`; `a² + 4` for `a = 1, …, 6` is `5, 8, 13, 20, 29, 40`, with squarefree parts `5, 2, 13, 5, 29, 10`.

[^3]: Verified by execution (2026-10-16): the first heights of golden, silver, bronze and `δ_4` in the census are 2, 3, 4 and 5; the `Q(√29)` root at `h = 5` is `(3 + √29)/2 = 4.19258`, the root of `x² − 3x − 5`; the ridge matrices `R_3, …, R_7` have characteristic polynomials `(x + 1)^{h−2}(x² − (h − 1)x − 1)`; the ridge strips of height 5 number `𝟙ᵀR_5^{w−1}𝟙 = F_{3w+2}` for `w ≤ 7`. `δ_5` first appears at `h = 6` by the height-6 census on [[quadratic-min-height](pages/quadratic-min-height.md)].

[^4]: Verified by execution (2026-10-16): the Perron roots in `Q(√5)` are `{φ}` at `h = 2`, `{φ, φ²}` at `h = 3`, `{φ, φ², 1 + √5}` at `h = 4`, and at `h = 5` these together with `√5`, `(5 + √5)/2` and `φ³ = 4.23607`.

[^5]: Verified by execution over the 512 binary `3 × 3` matrices (2026-10-16): the nine cubic minimal polynomials and their matrix counts as in the table; SymPy factors the characteristic polynomial of `[[0,0,1],[1,0,0],[1,1,0]]` as `x³ − x − 1`; its strip counts `𝟙ᵀM^{w−1}𝟙` equal `A000931(w + 9)` for `w ≤ 40`.

[^6]: Verified by execution (2026-10-16): `h = 3`: 32 distinct characteristic polynomials, 25 nilpotent matrices, 17 distinct positive Perron roots (3 integer, 5 quadratic in `d = 2, 3, 5`, 9 cubic). `h = 4`: 333 characteristic polynomials, 543 nilpotent matrices, 184 Perron roots (4 integer, 14 quadratic in `d = 2, 3, 5, 13, 17, 21`, 56 cubic, 110 quartic). `h = 5`: 8,927 characteristic polynomials, 29,281 nilpotent matrices, 5,978 Perron roots (5 integer, 29 quadratic in `d = 2, 3, 5, 6, 7, 13, 17, 21, 29, 33`, 253 cubic, 1,355 quartic, 4,336 quintic). The nilpotent counts are the numbers of acyclic directed graphs, 25, 543, 29,281.

[^7]: The 14 quadratic Perron minimal polynomials at `h ≤ 4` (2026-10-16), by discriminant `p₁² + 4p₂`: 5: `x² − x − 1`, `x² − 3x + 1`; 20: `x² − 2x − 4`; 8: `x² − 2`, `x² − 2x − 1`, `x² − 4x + 2`; 12: `x² − 3`, `x² − 2x − 2`, `x² − 4x + 1`; 13: `x² − x − 3`, `x² − 3x − 1`; 17: `x² − x − 4`, `x² − 3x − 2`; 21: `x² − 3x − 3`.

[^8]: `p₁² + 4p₂ ≡ p₁² (mod 4)`, which is 0 or 1. Every multiple of 4 that is at least 4 is `4p₂` with `p₁ = 0`, and every value `≡ 1 (mod 4)` that is at least 5 is `1 + 4p₂` with `p₁ = 1`.

[^9]: Verified by execution (2026-10-16): the edge-graph matrices of `[[p₁, p₂], [1, 0]]` for `(2, 3)`, `(0, 5)`, `(6, 2)` and `(1, 4)` have characteristic polynomials `x⁴(x − 3)(x + 1)`, `x⁴(x² − 5)`, `x⁷(x² − 6x − 2)` and `x⁴(x² − x − 4)`. The pairs reached first at `h = 3` are `(0, 2), (2, 1), (2, 2), (3, −1)`, and at `h = 4` they are `(0, 3), (1, 3), (1, 4), (2, 4), (3, 1), (3, 2), (3, 3), (4, −2), (4, −1)`.

[^10]: The orbit representative is the lexicographically smallest flattening of `PMPᵀ` over all `h!` permutations. Verified by execution (2026-10-16): 10 orbits from 16 matrices at `h = 2`, 104 from 512 at `h = 3`, 3,044 from 65,536 at `h = 4`; the orbit representatives give the same quadratic fields as the full sweep (code on [[castle-snippets-strips](pages/castle-snippets-strips.md)]).

[^11]: Verified by execution (2026-10-16): the characteristic polynomials of all 2,391,496 matrices of size 6 with at most 6 ones among their 36 entries, 95 distinct, whose quadratic Perron roots lie in the fields `d = 2, 3, 5`.

[^12]: Verified by execution (SymPy, 2026-10-16): `R_6 = J − D` has characteristic polynomial `(x + 1)⁴(x² − 5x − 1)` and 31 ones; `R_7 = J − D` has `(x + 1)⁵(x² − 6x − 1)`, Perron root `3 + √10 = δ_6`. The height-6 realizations of `(4, 6)` and `(2, 9)`, and the heights 7 of `(6, 1)` and `(0, 10)`, are from [[quadratic-min-height](pages/quadratic-min-height.md)].
