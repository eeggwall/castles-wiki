---
title: Eigenvalue continued fractions
category: Concepts
summary: The castle's characteristic polynomials are self-reciprocal (palindromic/anti-palindromic), and self-reciprocity is the same symmetry that makes a number's continued fraction repeat — taught from "what is a continued fraction" up to the castle's two norm-−1 quadratics φ and √2+1 and their mod-p twin.
tags: [concept, castle, continued-fraction, eigenvalue, characteristic-polynomial, palindromic, lagrange, galois, quadratic, fibonacci, mod-p, pedagogy]
sources: [project-euler-502-representations, oeis-mining-pe502]
created: 2026-09-15
updated: 2026-09-15
---

# Eigenvalue continued fractions

## The idea in one breath

The castle's counts obey linear recurrences, and every linear recurrence has a **characteristic polynomial** whose roots are its **eigenvalues**. Those polynomials turn out to be **self-reciprocal** — palindromic or anti-palindromic — and self-reciprocity is *the same symmetry* that makes a number's continued fraction repeat. So a castle eigenvalue can be read the way one reads the golden ratio: as a repeating continued fraction.

Three steps get you there, each worth knowing on its own:

1. **What a continued fraction is** — and why `φ = 1 + 1/(1 + 1/(1 + …))` is the canonical example.
2. **Why "periodic" and "quadratic" are synonyms** — Lagrange's theorem, and the sharper "purely periodic = reduced" (Galois).
3. **Where the castle's eigenvalues land** — the two quadratics that actually arise, and the higher-degree case where the symmetry survives periodicity.

## Step 1 — A continued fraction in five minutes

A **continued fraction** is a staircase of reciprocals,

```
[a₀; a₁, a₂, …]  =  a₀ + 1/( a₁ + 1/( a₂ + 1/( … ) ) ),
```

and any real number has one, computed by the Euclidean algorithm: take the integer part, subtract it, invert, repeat. The magic case is the number that reproduces itself after one step. The **golden ratio** `φ = (1+√5)/2 ≈ 1.618` satisfies[^2]

```
φ − 1 = 1/φ,    so    φ = 1 + 1/φ.
```

Because the remainder `1/φ` is *the same φ again*, the process never changes: `φ = [1; 1, 1, 1, …]`. That self-similarity is the whole story — periodicity of a continued fraction is just self-similarity of the Euclidean algorithm.

**Convergents.** Truncating gives the best rational approximations. For `φ` each truncation is a ratio of consecutive Fibonacci numbers (the recurrence `p_n = a_n p_{n−1} + p_{n−2}` with every `a_n = 1` *is* the Fibonacci recurrence):[^2]

| truncation | `[1]` | `[1;1]` | `[1;1,1]` | `[1;1,1,1]` | `[1;1,1,1,1]` |
|---|---|---|---|---|---|
| value | `1` | `2` | `3/2` | `5/3` | `8/5` |

converging to `φ` as `F_{n+1}/F_n`. (Run the same game starting from `x = 2 + 1/x` and you get `√2 + 1 = [2; 2, 2, 2, …]` — the tower-word growth constant, below.)

## Step 2 — Periodic means quadratic (Lagrange)

A continued fraction is **periodic** when the same block of digits repeats forever. The governing theorem is due to Lagrange:[^3]

> A real number has an eventually periodic continued fraction **if and only if** it is a quadratic irrational (a root of `ax² + bx + c = 0` with integer coefficients).

The reason is exactly the self-similarity above. If `φ = 1 + 1/φ`, then `φ` is a root of `x² − x − 1 = 0` — a **quadratic** — and the equation `φ = 1 + 1/φ` is literally "the remainder after one Euclidean step equals the original number," i.e. the algorithm loops. Quadratic ⟺ the remainder ever lands back on itself ⟺ periodic. That is the theorem.

The simplest periodic fraction is the **period-one** case. The equation `x = a + 1/x` is `x² − ax − 1 = 0`, so

```
[a; a, a, a, …]  =  (a + √(a² + 4)) / 2,
```

a quadratic of **trace `a`, norm −1** (the constant term `−1` is the product of the two roots). `a = 1` gives `φ`; `a = 2` gives `√2 + 1`.

## Step 3 — Purely periodic means reduced (Galois)

Look closer and there are two kinds of periodic fraction. `φ = [1; 1, 1, …]` repeats from the very first digit — **purely** periodic. The near-twin `(3+√5)/2 ≈ 2.618` is `[2; 1, 1, 1, …]`: a one-digit head `[2;]` before the repeating `[1]`.[^6] What is the difference? It is visible in the *other* root (the **conjugate**):

```
φ         = [1; 1, 1, …]   conjugate 1−φ = −0.618 ∈ (−1, 0)      purely periodic
(3+√5)/2  = [2; 1, 1, …]   conjugate (3−√5)/2 = 0.382 ∉ (−1, 0)   has a head
```

Galois' theorem says exactly this:[^3]

> A quadratic surd `α` is **purely** periodic if and only if it is **reduced**: `α > 1` and its conjugate lies in `(−1, 0)`.

And "conjugate in `(−1, 0)`" is a reciprocal condition in disguise. For a quadratic `x² − s·x + c`, the constant term `c` is the product of the roots, so it decides how the conjugate is placed:

- **`c = +1`** — roots `r` and `1/r` (reciprocals). This is the **palindromic** quadratic (`x² − s·x + 1`), and `r` is *not* reduced (`1/r ∈ (0,1)`), so its fraction has a head: `(3+√5)/2 = [2; 1, 1, …]`.
- **`c = −1`** — roots `r` and `−1/r`. For `r > 1` the conjugate `−1/r` sits in `(−1, 0)` automatically, so `r` **is** reduced, hence **purely** periodic: `φ = [1;1,1,…]`, `√2+1 = [2;2,2,…]`.

So "norm −1" (constant term `−1`) is the cheap certificate of pure periodicity.

## Step 4 — Palindromic polynomials: roots in reciprocal pairs

Now the algebraic side. A polynomial `p(x) = a_d x^d + … + a_0` is **palindromic** when its coefficients read the same backwards, `a_i = a_{d−i}`, and **anti-palindromic** when they read backwards with a sign flip, `a_i = −a_{d−i}`. The test is mechanical — for `x² − 3x + 1` the coefficients `[1, −3, 1]` are symmetric, so it is palindromic, and indeed its roots `(3±√5)/2` multiply to `1`, i.e. are reciprocals. The general fact:[^1]

```
palindromic       ⟺  p(x) =  x^d · p(1/x)   ⟺  roots closed under  r ↦  1/r
anti-palindromic  ⟺  p(x) = −x^d · p(1/x)   ⟺  roots closed under  r ↦ −1/r
```

This is exactly Step 3's `c = ±1` story lifted to any degree. A quadratic's reciprocal roots (`r ↔ ±1/r`) *are* its continued-fraction periodicity; a higher-degree polynomial's reciprocal roots are the same symmetry with the periodicity no longer guaranteed. **Reciprocal roots and periodic continued fractions are two faces of one symmetry** — that single sentence is the page.

## Step 5 — The castle's eigenvalues

Now point it at the castle. The signed tower count `P(k,L)` ([[signed-tower-count](pages/signed-tower-count.md)]) is C-finite in both directions, and its two characteristic-polynomial families behave differently.

**The k-direction is self-reciprocal.** For fixed `L`, the sequence `P(·,L)` has order `2L−2` (for `L ≥ 4`), and its characteristic polynomial is palindromic for even `L`, anti-palindromic for odd `L` ([[closed-form-hunting](pages/closed-form-hunting.md)]):[^1]

```
L=4: [1, 2, −1, −4, −1, 2, 1]
L=5: [1, 2, −2, −6, 0, 6, 2, −2, −1]
L=6: [1, 2, −3, −8, 2, 12, 2, −8, −3, 2, 1]
```

So the k-direction eigenvalues come in reciprocal pairs `r ↔ ±1/r` — the transfer matrix is reversible, and this symmetry is the algebraic fingerprint of the periodic-continued-fraction structure of Step 3.

**The two quadratics are the real, purely-periodic cases.** The castle's *actual* quadratic numbers are not among these high-degree roots; they sit in the surrounding objects, and both are norm-−1 reduced surds of period one:[^4]

- `φ = (1+√5)/2 = [1; 1, 1, …]`, root of `x² − x − 1` — Fibonacci's growth rate (`F_n = (φ^n − φ̂^n)/√5`, [[aocp-generating-functions](pages/aocp-generating-functions.md)]) and the `2^{n−1} − F_{n−1}` of prime-castle counting ([[castle-by-area](pages/castle-by-area.md)]).
- `√2 + 1 = [2; 2, 2, …]`, root of `x² − 2x − 1` — the tower-word growth constant from [[tower-word-continued-fraction](pages/tower-word-continued-fraction.md)].

Both are the fundamental units of their quadratic fields (`φ` of `Q(√5)`, `√2+1` of `Q(√2)`) — what "norm −1 reduced surd" means for a real quadratic field.

**The honest caveat.** The k-direction eigenvalues have degree `2L−2 ≥ 6`, so they are *not* quadratic, and Lagrange cuts only one way: their continued fractions are **not** periodic. What survives is the reciprocal symmetry itself — the roots still pair as `r ↔ ±1/r`, which is the degree-`2L−2` shadow of the degree-2 periodicity condition. Periodicity is lost; the pairing remains.

**The complex eigenvalues go Gaussian.** `P(1,L)` has characteristic polynomial `x² − 2x + 2`, roots `1 ± i` — Gaussian integers, with `|1+i| = √2`.[^5] A complex quadratic over `Q(i)` has a periodic **Gaussian** continued fraction (the complex Lagrange), so `1 ± i` is the `Z[i]`-counterpart of the real `φ` and `√2+1`.

## The payoff: the mod-p twin

This is the real-number counterpart of the [[mod-p-observatory](pages/mod-p-observatory.md)]. Modulo a prime, `F(w,h)` is eventually periodic with period the lcm of the **eigenvalue orders** — the smallest `m` with `λ^m ≡ 1` in `F_{p^d}^*`. Over `R`, the twin of that finite order is the eigenvalue's **continued-fraction period** (for the quadratics) and its **reciprocal symmetry** (for the higher-degree eigenvalues). In both settings the eigenvalue's structure is read off how its powers repeat: an *order* in a finite field, a *period* in a continued fraction.

## Appearances in Sources

- [[closed-form-hunting](pages/closed-form-hunting.md)] — the palindromic/anti-palindromic k-direction characteristic polynomials (orders `2L−2`).
- [[generating-function-gallery](pages/generating-function-gallery.md)] — the L-direction `char_k` polynomials, their complex/high-degree roots, and the dominant eigenvalue `ρ_k ~ k/log k`.
- [[signed-tower-count](pages/signed-tower-count.md)] — `P(1,L) = Re((1+i)^{L+1})`, the `1±i` roots.
- [[mod-p-observatory](pages/mod-p-observatory.md)] — the eigenvalue orders in `F_{p^d}^*` that set the mod-p periods.

## Related Concepts

- [[tower-word-continued-fraction](pages/tower-word-continued-fraction.md)] — the `√2 + 1` growth constant and the Flajolet/Motzkin continued fractions this page's eigenvalue side mirrors.
- [[aocp-generating-functions](pages/aocp-generating-functions.md)] — the Fibonacci/`φ` method, the golden ratio's algebraic home.
- [[castle-by-area](pages/castle-by-area.md)] — `2^{n−1} − F_{n−1}`, where Fibonacci/`φ` enters the castle count.
- [[algebraic-transcendental-wall](pages/algebraic-transcendental-wall.md)] — the algebraic/transcendental split the named constants inhabit.
- [[recurrence-discovery](pages/recurrence-discovery.md)] — the orders (`k+1` in L, `2L−2` in k) the two polynomial families realize.
- [[finite-fields](pages/finite-fields.md)] — the field structure behind the mod-p eigenvalue orders.

## Footnotes

[^1]: [[closed-form-hunting](pages/closed-form-hunting.md)] §"The pattern stops at L = 3" — the k-direction characteristic polynomials `L=4: [1,2,−1,−4,−1,2,1]`, `L=5: [1,2,−2,−6,0,6,2,−2,−1]`, `L=6: [1,2,−3,−8,2,12,2,−8,−3,2,1]`, "palindromic for even L and anti-palindromic for odd L." The equivalence `p(x) = ±x^d p(1/x) ⟺` reciprocal roots, and the self-reciprocity of the three polynomials, were re-verified with SymPy.

[^2]: The continued-fraction setup and the convergent recurrence `p_n = a_n p_{n−1} + p_{n−2}` (with the golden ratio's convergents `1, 2, 3/2, 5/3, 8/5, 13/8, 21/13` = `F_{n+1}/F_n`) are standard and were verified by executing the fixed-point iterations `x = 1 + 1/x` and `x = 2 + 1/x`.

[^3]: Lagrange's theorem (eventually periodic ⟺ quadratic) and Galois' theorem (purely periodic ⟺ reduced, `α > 1` and conjugate in `(−1, 0)`) are classical. The period-one specialization `[a; a, a, …] = (a + √(a²+4))/2 ⟺ x² − ax − 1 = 0` and the norm-−1 ⇒ reduced argument were verified by execution.

[^4]: Convergents computed and matched: `[1;1,1,…]` gives `2, 3/2, 5/3, 8/5, 13/8, 21/13 → φ`; `[2;2,2,…]` gives `5/2, 12/5, 29/12, 70/29, 169/70 → √2+1`. Norms checked: `φ·(1−φ) = −1` and `(√2+1)(1−√2) = −1`.

[^5]: [[signed-tower-count](pages/signed-tower-count.md)] §"The k = 1 case" — `P(1,L) = Re((1+i)^{L+1})`, characteristic polynomial `x² − 2x + 2`, eigenvalues `1 ± i`.

[^6]: `(3+√5)/2 = 2 + 1/φ = [2; 1, 1, 1, …]` (root of the palindromic `x² − 3x + 1`, norm `+1`, conjugate `0.382 ∉ (−1,0)`, hence not purely periodic) — verified; the contrast with `φ = [1;1,1,…]` (root of `x² − x − 1`, norm `−1`, purely periodic) is the worked illustration of Galois' reduced condition.
