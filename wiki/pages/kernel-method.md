---
title: Kernel method
category: Concepts
summary: The kernel method solves a functional equation K(x, u)·G(x, u) = A(x, u) + (unknown boundary terms) for a lattice-path generating function by substituting roots u(x) of the kernel K into it, which gives extra equations for the unknown boundary functions. For directed walks with steps(u) listing the jumps, the kernel is 1 − x·steps(u); below one wall the large roots solve the system (algebraic g.f.), between two walls all roots do (rational g.f.). For castles, jumps −m, …, m between walls 0 and h − 1 are the anchored m-smooth strip, so the method gives those strips in closed form in the 2m kernel roots.
tags: [concept, kernel-method, lattice-paths, generating-functions, m-smooth, transfer-matrix, technique]
sources: [banderier-nicodeme-2010-bounded-discrete-walks]
created: 2026-10-07
updated: 2026-10-07
---

# Kernel method

## Description

A walk that starts at altitude 0 and adds a jump from a finite set at each time step is counted by a generating function `strip(x, u)`, with `x` marking length and `u` the final altitude; `steps(u)` lists the allowed jumps, one term `u^j` per jump `j`. Adding one step multiplies by `x·steps(u)`. When walls forbid some jumps, the step-by-step decomposition gives a functional equation

```
(1 − x·steps(u)) · strip(x, u)  =  1  −  (terms in the unknown generating functions of walks ending next to a wall),
```

and `1 − x·steps(u)` is the **kernel**. Substituting for `u` a root `u(x)` of the kernel, where the substitution is legitimate, makes the left side vanish and leaves an equation between the unknowns. Enough roots give a linear system for them.[^1]

- **Below one wall** (ceiling, no floor), substituting the large roots, those that grow like `x^{−1/m₊}` near `x = 0`, gives as many equations as unknowns, and the generating function is algebraic.[^2]
- **Between two walls**, the generating function is a Laurent polynomial in `u`, so all roots can be substituted; the system is solved by Cramer's rule and the generating function is rational.[^3]

## For castles

Castle strips are walks: a skyline read left to right is a sequence of altitudes, and a neighbour rule is a step set ([[castle-strip](pages/castle-strip.md)]). The anchored m-smooth strip is the walk with jumps `−m, …, m` between floor 0 and ceiling `h − 1`. The wiki counts it with an `h × h` band matrix ([[m-smooth-castles](pages/m-smooth-castles.md)]); the kernel method counts it with the `2m` roots of `u^m − x(1 + u + ⋯ + u^{2m})`, whatever `h` is. The two agree for `m ≤ 3`, `h ≤ 8` ([[banderier-nicodeme-2010-bounded-discrete-walks](pages/banderier-nicodeme-2010-bounded-discrete-walks.md)], "The castle reading"). With the floor kept and the ceiling removed, the method gives the anchored and the pinned castles with no height bound from the `m` small roots: at `m = 1`, A005773 and the Motzkin numbers ([[motzkin-castles](pages/motzkin-castles.md)]).

The method also counts Motzkin paths and prefixes refined by their `UD` and `DU` factors on [[prodinger-2025-cornerless-motzkin-bargraphs](pages/prodinger-2025-cornerless-motzkin-bargraphs.md)], where the states are heights in three layers by the type of the last step.

## Appearances in Sources

- [[banderier-nicodeme-2010-bounded-discrete-walks](pages/banderier-nicodeme-2010-bounded-discrete-walks.md)] - the method for walks below one wall and between two walls, with any finite set of jumps.
- [[prodinger-2025-cornerless-motzkin-bargraphs](pages/prodinger-2025-cornerless-motzkin-bargraphs.md)] - the method on a three-layer automaton for Motzkin paths and prefixes.

## Related Concepts

- [[m-smooth-castles](pages/m-smooth-castles.md)] - the strips the two-wall case counts, for jumps `−m, …, m`.
- [[1-smooth-castles](pages/1-smooth-castles.md)] - the case `m = 1`, where the band matrix has explicit eigenvalues.
- [[castle-strip](pages/castle-strip.md)] - the transfer-matrix picture of the same strips.
- [[motzkin-castles](pages/motzkin-castles.md)] - the `m = 1` counts with no ceiling.
- [[generating-functions](pages/generating-functions.md)] - the wider method.

## Footnotes

[^1]: [[banderier-nicodeme-2010-bounded-discrete-walks](pages/banderier-nicodeme-2010-bounded-discrete-walks.md)] §1 L62-L66 - the kernel method solves a functional equation `K(z, u)F(z, u) = A(z, u) + B(z, u)G(z)` "where F and G are the unknowns one wishes to determine"; "The kernel method consists in getting additional equations by plugging the roots u(z) of the 'kernel' K(z, u) in the initial equation, which in general is enough to solve the system."
[^2]: [[banderier-nicodeme-2010-bounded-discrete-walks](pages/banderier-nicodeme-2010-bounded-discrete-walks.md)] §3 Theorem 2 and proof L191-L226 [synthesis] - walks below the wall `y = h` have an algebraic g.f.; "plugging the d large roots vi in this equation" (legitimate because the large roots behave like `z^{−1/d}`) "leads to a linear system of d equations with d unknowns".
[^3]: [[banderier-nicodeme-2010-bounded-discrete-walks](pages/banderier-nicodeme-2010-bounded-discrete-walks.md)] §3 Theorem 4 and proof L284-L318 [synthesis] - walks between the walls `y = −h2` and `y = h` have a rational g.f.; substituting all the roots is legitimate "since F is here a Laurent polynomial in u, and not a Laurent series" and "leads to a system with c + d unknowns; the Cramer formula gives the solutions".
