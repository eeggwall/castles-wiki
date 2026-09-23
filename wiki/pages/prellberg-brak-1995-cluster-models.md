---
title: "Critical exponents for partially directed cluster models (Prellberg-Brak, 1995)"
category: Sources
summary: Prellberg-Brak derive nonlinear (quadratic) functional equations for staircase, bar-graph, directed-column-convex, and ZL-walk cluster models, and a universal linearization G(x) = α H(qx)/H(x) - b(x) turning them into linear q-difference equations with q-Bessel solutions. The bar-graph GF by (horizontal, vertical, area) has functional equation B = B(qx) y + {1 + B(qx)} qx {y + B(x)} (eq. 3.11) with continued-fraction form eq. 3.12; the paper shows the linearization works but writes out the closed q-Bessel form explicitly only for staircase (eq. 4.9). By taking the continuum limit they derive an Airy-equation scaling function and prove all five models are in one universality class with γ_u = -1/2, γ_t = -1/3, φ = 2/3.
tags: [paper, source, bar-graph, polyomino, cluster-model, functional-equation, q-shift, q-bessel, airy-function, universality, critical-exponent, temperley, staircase, directed-column-convex, ZL-walks, continuum-limit, source]
sources: [prellberg-brak-1995-cluster-models]
created: 2026-09-23
updated: 2026-09-23
---

# Critical exponents for partially directed cluster models (Prellberg-Brak, 1995)

**Source:** `raw/prellberg-brak-1995-partially-directed-cluster-models.pdf` (OCR text layer at `raw/prellberg-brak-1995-partially-directed-cluster-models.txt`, extracted with `pdftotext -layout`; original PDF is a scanned image, so page-image quotes are lightly cleaned OCR).
**Publication:** T. Prellberg and R. Brak, "Critical exponents from nonlinear functional equations for partially directed cluster models," *Journal of Statistical Physics* **78** (1995) 701-730. Received 23 May 1994.[^1]
**Date ingested:** 2026-09-23
**Type:** paper (PDF, 30 pp.)

## Summary

The paper enumerates five partially directed cluster models on the square lattice - **staircase**, **directed-column-convex**, **column-convex**, **bar-graph**, and **ZL walks** - and their common critical scaling function, from a starting point that Bousquet-Mélou 1996 does not use: **quadratically nonlinear functional equations** for the trivariate generating function `G(x, y, q)` counting configurations by horizontal step weight `x`, vertical step weight `y`, and area `q`.[^2] The novelty is not the enumeration - staircase and directed-column-convex were already known - but the framing: nonlinear rather than linear equations, and a route to critical asymptotics via a continuum limit that avoids fighting the q-Bessel functions directly.[^3]

The functional equations come from a "column-inflation + one-column-of-height-1" decomposition, one per model. For **bar-graph polygons** (§3.1, Fig. 4):[^4]

```
B(x, y, q) = B(qx, y, q) y + {1 + B(qx, y, q)} qx {y + B(x, y, q)}         (3.11)
```

This is quadratic in `B` (both `B(x)` and `B(qx)` appear multiplicatively). Iterating gives a continued fraction (eq. 3.12). **Staircase** (§3.2, eq. 3.14): `S(x, y, q) = {S(qx, y, q) + qx}{y + S(x, y, q)}`, the polynomial form of the same shape. **Directed-column-convex** (§3.3, eqs. 3.24, 3.28): a coupled pair or a cubic single equation; not `Riccati` at first sight, but linearised by the same trick. **ZL walks** (§3.4, eq. 3.29) have a form very similar to bar-graphs and share the continuum limit.[^5]

**Universal linearization (§4).** Any equation of shape

```
G(x) G(qx) + a(x) G(x) + b(x) G(qx) + c(x) = 0         (4.1)
```

linearises via `G(x) = α H(qx)/H(x) - b(x)`, giving a linear q-difference equation `α² H(q²x) + α [a(x) - b(qx)] H(qx) + [c(x) - a(x)b(x)] H(x) = 0` (eq. 4.3). If this collapses further to `α H(qx) + sum_k α_k H(q^k x) = 0` with `sum_k α_k = 0`, the regular solution at `x = 0` is the explicit q-series

```
H(x) = sum_{n≥0} (-x)^n q^{C(n, 2)} / prod_{m=1..n} A(q^m),   A(t) = sum_k α_k t^k
```

(eq. 4.5).[^6] Applied to staircase (eq. 4.6-4.9) this reproduces the Klarner-Rivest-Bousquet-Mélou-Fédou result `S(x) = y(T(qx)/T(x) - 1)` with `T(x) = sum_n (-qx)^n q^{C(n, 2)} / (q, qy; q)_n`, which is (a variant of) `J_0`. The paper explicitly says this "calculation easily generalises for the other models with quadratic functional equations," so bar-graphs and ZL walks fall to the same linearization by inspection, though the explicit q-Bessel form for bar-graphs is not written out.[^7] Directed-column-convex is a "cubic" equation and gets a three-term q-Bessel solution (eq. 4.11-4.13). The paper closes by noting that the same `α H(qx)/H(x) - b` form is the same as Viennot's heap-of-pieces bijection produces for staircase polygons, hinting at a similar bijection for directed-column-convex.[^8]

**Continuum limit and Airy universality (§§5-7).** Inserting a lattice spacing `a` into `y = e^{-τ}`, `q = e^{-ε}` and taking `a → 0` turns each nonlinear q-shift equation into a nonlinear differential equation. For staircase it is a Riccati equation `2λ t ∂G/∂t = t - G + G²` (eq. 5.10) with solution `G(t) = √t J'_{1/λ}(2√(t/λ)) / J_{1/λ}(2√(t/λ))` (eq. 5.17), whose asymptotic behaviour is Olver's Airy-uniform form. All five models are shown by the method of dominant balance to have the same scaling function, the logarithmic derivative of the Airy function:[^9]

```
f(z) = -(b/c)^{1/3} Ai'((cb)^{1/3} z) / Ai((cb)^{1/3} z)
γ_u = -1/2,   γ_t = -1/3,   φ = 2/3,   ψ = 3/2
```

The bar-graph case is checked by formal perturbation theory (§6): the same gap exponent `Δ = 3/2` emerges from expanding `B(x, x, q)` in `ε = -log q` around `q = 1`.[^10] So bar-graphs share the Airy scaling function with staircase, directed-column-convex, column-convex and ZL walks - one universality class from one functional-equation shape.

## Why it matters for Project Euler 502 (PE 502)

- **Bar-graph polygons are castles.** A bar-graph polygon is a column-convex polyomino with a horizontal lower boundary (§2, Fig. 1d) - identical to a [[castle-polyomino](pages/castle-polyomino.md)] on `w` columns of heights `c_1, ..., c_w ≥ 1`, blocks equal to the vertical half-perimeter ([[castle-perimeter](pages/castle-perimeter.md)]). Their eq. 3.11 is therefore a castle equation, in different variables from ours: their `x` marks half a horizontal boundary step, `y` marks a vertical boundary step, `q` marks area.
- **The linearization trick is the method behind our closed form.** The `G(x) = α H(qx)/H(x) - b(x)` transformation (eq. 4.2) is a Möbius map on q-shift equations, and this is precisely the map that [[castle-q-bessel-closed-form](pages/castle-q-bessel-closed-form.md)] uses to turn the tower-grammar q-shift into `A = N/M`. That we then get the parallelogram q-Bessel series is the direct analogue of PB's staircase route producing `T`.
- **The bar-graph closed form is implied here but not written out.** The paper's §4 says the staircase calculation "easily generalises" to bar-graphs but does not display the closed form. Our page fills in the missing packaging by identifying `N` with the Bousquet-Mélou-Fédou `J_0(x, y, q)` at width `(1-x)u`, height `x`.
- **Eq. 3.11 is the castle generating function, variable for variable.** Iterated as a power series, `x` marks width, `y` marks blocks and `q` marks area. Area 3 gives `x³y + 2x²y² + xy³`, the castles `(1,1,1)`, `(1,2)`, `(2,1)`, `(3)`. At `x = y = 1` the area counts are `1, 2, 4, 8, 16, 32, 64`, the compositions of [[castle-by-area](pages/castle-by-area.md)]. At `y = -1` they are `-1, 0, 0, 2, 0, 2, -4`, the signed counts on [[castle-row-raising-equation](pages/castle-row-raising-equation.md)], and the series satisfies that page's signed equation through area 7 (own computation, 2026-09-23).
- **Airy universality is a new open question for castles.** The critical exponents `γ_u = -1/2, γ_t = -1/3, φ = 2/3` are for the perimeter+area tricritical point at `q = 1`, `y = y_c(1)`. Our meromorphy-in-|q|<1 result on [[castle-q-bessel-closed-form](pages/castle-q-bessel-closed-form.md)] is a different limit (signed count as `q → q_0`, not `q → 1`). Whether the two are compatible - do the signed-castle `q_0` singularity and the bar-graph Airy scaling function fit together - is worth writing down.

## Key Takeaways

- **Five models, one universality class.** Staircase, DC, CC, bar-graph, and ZL walks all have Airy scaling function `f(z) = Ai'/Ai` and critical exponents `γ_u = -1/2, γ_t = -1/3, φ = 2/3`.[^9]
- **Bar-graph functional equation is quadratic** (eq. 3.11): `B(x) = B(qx) y + {1 + B(qx)} qx {y + B(x)}`.[^4]
- **Universal linearization** (eq. 4.2): `G(x) = α H(qx)/H(x) - b(x)` turns quadratic q-shift equations into linear ones with q-series solutions.[^6]
- **Staircase closed form** (eq. 4.9): `S(x) = y(T(qx)/T(x) - 1)` with `T(x) = sum_n (-qx)^n q^{C(n, 2)} / (q, qy; q)_n`, the same shape as `y J_1/J_0` in Bousquet-Mélou-Fédou.[^7]
- **Bar-graph closed form is implied but not written out** here; §4 says the derivation "easily generalises" but only staircase is displayed.[^7]
- **Continuum limit → Airy equation.** Semicontinuous models satisfy Riccati equations that linearise to Bessel or Airy equations, giving the scaling function exactly.[^9]

## Entities & Concepts

- [[castle-polyomino](pages/castle-polyomino.md)] - the castle IS a bar-graph polygon.
- [[castle-perimeter](pages/castle-perimeter.md)] - the vertical half-perimeter of a bar-graph is the castle's block count.
- [[castle-q-bessel-closed-form](pages/castle-q-bessel-closed-form.md)] - the closed-form packaging of the castle bar-graph GF that PB implies but does not display; it uses the same Möbius / linearization trick as this paper's eq. 4.2.
- [[bousquet-melou-fedou-1995-convex-polyominoes](pages/bousquet-melou-fedou-1995-convex-polyominoes.md)] - the `J_0, J_1` series this paper's staircase result matches term by term.
- [[column-convex-polygon-enumeration](pages/column-convex-polygon-enumeration.md)] - the same-era systematic derivation via *linear* q-shift equations; PB gives the *nonlinear* companion.
- [[q-differential-system](pages/q-differential-system.md)] - the harder cousin, where the q-shift closes only as a coupled linear system in three unknowns; the PB approach avoids it for the five families it treats.
- [[generalized-dyck-grammar](pages/generalized-dyck-grammar.md)] - the castle grammar whose area grading reduces to this paper's quadratic form via first-return.
- [[algebraic-transcendental-wall](pages/algebraic-transcendental-wall.md)] - PB's Airy scaling and non-holonomic q-Bessel functions land bar-graph GFs firmly on the transcendental side of the wall in area-and-perimeter.
- [[convex-polyomino-by-area](pages/convex-polyomino-by-area.md)] - the Klarner-Rivest `1/μ = 0.43306...` is a point on PB's phase diagram (Fig. 2): the area singularity `q_c(y)` of staircase polygons at `y = 1`, on the branch away from the tricritical point `(q, y) = (1, y_c(1))` where the Airy scaling holds.[^11]
- [[castle-row-raising-equation](pages/castle-row-raising-equation.md)] - the prime-castle `z → qz` equation, signed and unsigned, has PB's linearizable shape (4.1), and eq. 3.11 at `y = -1` reproduces its signed counts.
- [[castle-by-area](pages/castle-by-area.md)] - eq. 3.11 at `x = y = 1` gives the `2^(n-1)` castles of area `n`.
- [[tower-word-continued-fraction](pages/tower-word-continued-fraction.md)] - eq. 3.12 is an area-graded continued fraction for castles, next to the tower word's Motzkin J-fraction.

## Relation to Other Wiki Pages

Cited on [[castle-q-bessel-closed-form](pages/castle-q-bessel-closed-form.md)] as the primary literature source for the linearization method used there, and on [[castle-perimeter](pages/castle-perimeter.md)] as the bar-graph functional equation source (perimeter and area together). The Airy universality result is a candidate Open on [[castle-q-bessel-closed-form](pages/castle-q-bessel-closed-form.md)]: does the signed-castle meromorphy picture in `|q| < 1` (dominated by `q_0 = -0.6158`) join up with the `q → 1` Airy scaling PB proves for bar-graphs? Same paper, but different critical direction. The linearization-heap connection (§4 closing paragraphs) rhymes with [[viennot-heap-tower](pages/viennot-heap-tower.md)] and [[tower-heap](pages/tower-heap.md)]: their equation `G = α H(qx)/H(x) - b` "can be explained via a bijection with heaps," suggesting a heap-of-pieces derivation of the castle q-Bessel form is also available.

## Footnotes

[^1]: [[prellberg-brak-1995-cluster-models](pages/prellberg-brak-1995-cluster-models.md)] `prellberg-brak-1995-partially-directed-cluster-models.txt` L1-8 - "Journal of Statistical Physics, Vol. 78, Nos. 3/4, 1995 ... Critical Exponents from Nonlinear Functional Equations for Partially Directed Cluster Models ... T. Prellberg and R. Brak ... Received May 23, 1994."
[^2]: [[prellberg-brak-1995-cluster-models](pages/prellberg-brak-1995-cluster-models.md)] `prellberg-brak-1995-partially-directed-cluster-models.txt` §"Introduction" L10-25 [synthesis] - "a method for the derivation of the generating function and computation of critical exponents for several cluster models (staircase, bar-graph, and directed column-convex polygons, as well as partially directed self-avoiding walks), starting with nonlinear functional equations ... all the above models are in the same universality class with exponents γ_u = -1/2, γ_t = -1/3, and φ = 2/3."
[^3]: [[prellberg-brak-1995-cluster-models](pages/prellberg-brak-1995-cluster-models.md)] `prellberg-brak-1995-partially-directed-cluster-models.txt` §"Introduction" L82-113 [synthesis] - "The principal purpose of this paper is to 'solve' this asymptotic problem without a direct assault on the q-functions. If only the asymptotics of the generating function is required, then a direct assault on the q-functions is a wasted effort ... we use nonlinear functional equations. This form of the functional equation is more suited to the limit q → q_c."
[^4]: [[prellberg-brak-1995-cluster-models](pages/prellberg-brak-1995-cluster-models.md)] `prellberg-brak-1995-partially-directed-cluster-models.txt` §"3.1 Bar-Graph Polygons" - eq. 3.11 `B(x, y, q) = B(qx, y, q) y + {1 + B(qx, y, q)} qx {y + B(x, y, q)}` and continued-fraction eq. 3.12 (`B(x, y, q) = qx / {1 - y - qx - qxB(qx)/(1 - qx - qxB(qx)) - qx/(1 - qx)}`); the partitioning into B_1..B_5 subsets and the sum B = B_1 + B_2 + B_3 + B_4 + B_5.
[^5]: [[prellberg-brak-1995-cluster-models](pages/prellberg-brak-1995-cluster-models.md)] `prellberg-brak-1995-partially-directed-cluster-models.txt` §§3.2-3.4 [synthesis] - staircase eq. 3.14 `S(x, y, q) = {S(qx, y, q) + qx}{y + S(x, y, q)}`; directed-column-convex eqs. 3.24-3.28, coupled/cubic; ZL walks eq. 3.29, "very similar to the bar-graph equation."
[^6]: [[prellberg-brak-1995-cluster-models](pages/prellberg-brak-1995-cluster-models.md)] `prellberg-brak-1995-partially-directed-cluster-models.txt` §"4. Solution of the Functional Equations" - "the functional equations for bar-graph polygons, alternating bar-graph polygons, staircase polygons, and ZL walks can all be linearized, as they are of the form G(x)G(qx) + a(x)G(x) + b(x)G(qx) + c(x) = 0 which can be linearized by use of the transformation G(x) = α H(qx)/H(x) - b(x)"; eq. 4.5 `H(x) = sum_n (-x)^n q^{C(n,2)} / prod A(q^m)`.
[^7]: [[prellberg-brak-1995-cluster-models](pages/prellberg-brak-1995-cluster-models.md)] `prellberg-brak-1995-partially-directed-cluster-models.txt` §4 eqs. 4.6-4.9 - "We now apply this method in the case of staircase polygons ... We get the solution T(x) = sum_{n=0} (-qx)^n q^{n(n-1)/2} / (q, qy; q)_n. The function T(x) = T(x, y, q) is a q-deformation of a Bessel function. This calculation easily generalizes for the other models with quadratic functional equations."
[^8]: [[prellberg-brak-1995-cluster-models](pages/prellberg-brak-1995-cluster-models.md)] `prellberg-brak-1995-partially-directed-cluster-models.txt` §4 closing paragraph - "in the case of staircase polygons, this structure can also be explained via a bijection with heaps, which indicates that in the case of directed column-convex polygons there might be a similar bijection."
[^9]: [[prellberg-brak-1995-cluster-models](pages/prellberg-brak-1995-cluster-models.md)] `prellberg-brak-1995-partially-directed-cluster-models.txt` §§5-7 [synthesis] - eqs. 1.10-1.14, 5.10, 5.17, 7.1-7.6 - the Riccati form `f' = c f² - b z` for the scaling function, its linearisation to the Airy equation `d²h/dz² = b²z h`, and the resulting `f(z) = -(b/c)^{1/3} Ai'/Ai((cb)^{1/3} z)`, `γ_u = -1/2, γ_t = -1/3, φ = 2/3, ψ = 3/2`.
[^10]: [[prellberg-brak-1995-cluster-models](pages/prellberg-brak-1995-cluster-models.md)] `prellberg-brak-1995-partially-directed-cluster-models.txt` §6 "Formal Perturbation Theory" - "One can use the functional equations (3.11), (3.13), (3.14), and (3.25) to derive the critical exponents ... Applied to bar-graph polygons, this method gives identical results."
[^11]: [[prellberg-brak-1995-cluster-models](pages/prellberg-brak-1995-cluster-models.md)] `prellberg-brak-1995-partially-directed-cluster-models.txt` §1 L118-150 [synthesis] - "Alternatively one can fix y and consider G as a function of q with radius of convergence qc(y). Then for polygon models the generating function is singular along the line q = 1 between y = 0 and some point y_t = y_c(1) ... The point (q_t, y_t) is an example of a 'tricritical' point"; `q_c(1)` for staircase polygons at unit perimeter weight is the parallelogram area singularity `1/μ`.
