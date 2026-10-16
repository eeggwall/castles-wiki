---
title: Kernel method
category: Concepts
summary: The kernel method solves a functional equation K(x, u)·G(x, u) = A(x, u) + (unknown boundary terms) for a lattice-path generating function by substituting roots u(x) of the kernel K into it, which gives equations for the unknown boundary functions. For directed walks whose jumps are listed by steps(u), the kernel is 1 − x·steps(u); below one wall the large roots solve the system and the generating function is algebraic, between two walls all roots do and it is rational. At m = 1 with a floor, the small root gives the Motzkin numbers for excursions and A005773 for meanders. For castles, the jumps −m, …, m between the walls 0 and h − 1 give the anchored m-smooth strips, in closed form in the 2m kernel roots.
tags: [concept, kernel-method, lattice-paths, generating-functions, m-smooth, transfer-matrix, technique]
sources: [banderier-nicodeme-2010-bounded-discrete-walks]
created: 2026-10-07
updated: 2026-10-16
---

# Kernel method

## Description

A walk starts at altitude 0 and adds a jump from a finite set at each time step. Its generating function `strip(x, u)` has `x` marking the length and `u` the final altitude, and `steps(u)` lists the allowed jumps, one term `u^j` per jump `j`. Adding one step multiplies by `x·steps(u)`. When walls forbid some jumps, the step-by-step decomposition gives a functional equation

```
(1 − x·steps(u)) · strip(x, u)  =  1  −  (terms in the unknown generating functions of walks ending next to a wall),
```

and `1 − x·steps(u)` is the **kernel**. Substituting for `u` a root `u(x)` of the kernel, for which `strip(x, u(x))` is a well-defined series, makes the left side vanish and leaves an equation between the unknowns. Enough roots give a linear system for them.[^1]

*Example: jumps of size at most 1 and one floor.* Take the jumps `−1, 0, 1`, so `steps(u) = u^{−1} + 1 + u`, and forbid altitudes below 0. A step down from altitude 0 is the one forbidden move, so

```
(1 − x(u^{−1} + 1 + u)) · strip(x, u)  =  1 − x·u^{−1}·strip(x, 0).
```

The kernel times `u` is `u − x(1 + u + u²)`, whose small root `u_1(x) = (1 − x − √((1 − x)² − 4x²))/(2x) = x + x² + 2x³ + 4x⁴ + ⋯` is a power series in `x`. Substituting it gives `strip(x, 0) = u_1(x)/x = 1 + x + 2x² + 4x³ + 9x⁴ + ⋯`, the Motzkin numbers, which count the excursions, the walks that end at 0. Setting `u = 1` then gives the meanders, which end anywhere, `strip(x, 1) = (1 − u_1(x))/(1 − 3x) = 1 + 2x + 5x² + 13x³ + 35x⁴ + ⋯` (A005773).[^2]

- **Below one wall** (a ceiling and no floor), substituting the large roots, those that grow like `x^{−1/m₊}` near `x = 0`, gives as many equations as unknowns, and the generating function is algebraic.[^3]
- **Between two walls**, the generating function is a Laurent polynomial in `u`, so all roots can be substituted; Cramer's rule solves the system and the generating function is rational.[^4]

## For castles

A strip rule that depends only on the difference `c_{i+1} − c_i` of neighboring columns is a step set, and its strips are walks: a skyline read left to right is a sequence of altitudes ([[castle-strip](pages/castle-strip.md)]). Rules that depend on the heights themselves, such as the ridge rule, are not step sets. The anchored m-smooth strip is the walk with jumps `−m, …, m` between floor 0 and ceiling `h − 1`. The wiki counts it with an `h × h` band matrix ([[m-smooth-castles](pages/m-smooth-castles.md)]); the kernel method counts it with the `2m` roots of `u^m − x(1 + u + ⋯ + u^{2m})`, which do not depend on `h`. The two agree for `m ≤ 3`, `h ≤ 8` ([[banderier-nicodeme-2010-bounded-discrete-walks](pages/banderier-nicodeme-2010-bounded-discrete-walks.md)], section *The castle reading*). With the floor kept and the ceiling removed, the `m` small roots count the anchored m-smooth castles of every height, and those with both end columns at height 1; at `m = 1` these are the meanders and excursions of the example, A005773 and the Motzkin numbers ([[motzkin-castles](pages/motzkin-castles.md)]).

[[prodinger-2025-cornerless-motzkin-bargraphs](pages/prodinger-2025-cornerless-motzkin-bargraphs.md)] applies the method to Motzkin paths and their prefixes counted by their factors `UD` and `DU`, on an automaton whose states are heights in three layers by the type of the last step.

## Appearances in Sources

- [[banderier-nicodeme-2010-bounded-discrete-walks](pages/banderier-nicodeme-2010-bounded-discrete-walks.md)] - the method for walks below one wall and between two walls, with any finite set of jumps.
- [[prodinger-2025-cornerless-motzkin-bargraphs](pages/prodinger-2025-cornerless-motzkin-bargraphs.md)] - the method on a three-layer automaton for Motzkin paths and prefixes.

## Related Concepts

- [[m-smooth-castles](pages/m-smooth-castles.md)] - the strips the two-wall case counts, for jumps `−m, …, m`.
- [[1-smooth-castles](pages/1-smooth-castles.md)] - the case `m = 1`, where the band matrix has explicit eigenvalues.
- [[castle-strip](pages/castle-strip.md)] - the transfer-matrix picture of the same strips.
- [[motzkin-castles](pages/motzkin-castles.md)] - the `m = 1` counts with no ceiling, A005773 and the Motzkin numbers.
- [[generating-functions](pages/generating-functions.md)] - generating functions, and the rational ones with the recurrences of their coefficients.

## Footnotes

[^1]: [[banderier-nicodeme-2010-bounded-discrete-walks](pages/banderier-nicodeme-2010-bounded-discrete-walks.md)] §1 L62-L66 - the kernel method solves a functional equation `K(z, u)F(z, u) = A(z, u) + B(z, u)G(z)` "where F and G are the unknowns one wishes to determine"; "The kernel method consists in getting additional equations by plugging the roots u(z) of the 'kernel' K(z, u) in the initial equation, which in general is enough to solve the system."
[^2]: Verified by execution (Python 3.11 with SymPy, 2026-10-16): the series of `u_1(x)`, `u_1(x)/x` and `(1 − u_1(x))/(1 − 3x)` to order 7, against a dynamic program over walks with jumps `−1, 0, 1` and floor 0 (excursions `1, 1, 2, 4, 9, 21, 51`, meanders `1, 2, 5, 13, 35, 96, 267`); A001006 and A005773 on oeis.org.
[^3]: [[banderier-nicodeme-2010-bounded-discrete-walks](pages/banderier-nicodeme-2010-bounded-discrete-walks.md)] §3 Theorem 2 and proof L191-L226 [synthesis] - walks below the wall `y = h` have an algebraic g.f.; "plugging the d large roots vi in this equation" (legitimate because the large roots behave like `z^{−1/d}`) "leads to a linear system of d equations with d unknowns".
[^4]: [[banderier-nicodeme-2010-bounded-discrete-walks](pages/banderier-nicodeme-2010-bounded-discrete-walks.md)] §3 Theorem 4 and proof L284-L318 [synthesis] - walks between the walls `y = −h2` and `y = h` have a rational g.f.; substituting all the roots is legitimate "since F is here a Laurent polynomial in u, and not a Laurent series" and "leads to a system with c + d unknowns; the Cramer formula gives the solutions".
