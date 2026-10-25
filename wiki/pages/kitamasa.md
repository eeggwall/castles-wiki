---
title: Kitamasa
category: Concepts
summary: Kitamasa's method computes one far term a_n of a linear recurrence of order D in O(D² log n) operations - reduce x^n modulo the characteristic polynomial and combine the D coefficients of the remainder with the first D terms. Worked for the Fibonacci numbers by hand and for the signed tower count P(1, L) at L = 10^12; the extractor on both computational paths of the castle count.
tags: [concept, algorithm, linear-recurrence, kitamasa, method, c-finite, pedagogy, teaching]
sources: [project-euler-502-solution, project-euler-502-implementation-notes, generating-functions-topic, project-euler-502-representations]
created: 2026-09-13
updated: 2026-10-25
---

# Kitamasa

## The problem

A sequence satisfies a linear recurrence of order `D`,

```
a_n  =  c_1 a_{n−1} + c_2 a_{n−2} + ⋯ + c_D a_{n−D},                          (1)
```

and its first `D` terms `a_0, …, a_{D−1}` are known. Walking Equation (1) to the term `a_n` takes `O(nD)` operations. **Kitamasa's method** computes `a_n` in `O(D² log n)` operations: it reduces the polynomial `x^n` modulo the characteristic polynomial of Equation (1) and reads `a_n` off as a fixed linear combination of `a_0, …, a_{D−1}`.[^1]

[[berlekamp-massey](pages/berlekamp-massey.md)] finds the shortest recurrence of a sequence from its first terms, and Kitamasa's method then jumps along that recurrence. The castle count uses Kitamasa's method for the signed tower count `P(k, L)` at large `L` and, after Berlekamp-Massey, at large `k` (section *How the castle count uses it*).

## Every term is a fixed combination of the first D

For the Fibonacci numbers, `F_0 = 0`, `F_1 = 1`, `F_n = F_{n−1} + F_{n−2}`, unrolling the recurrence without the initial values gives

```
F_2  =  F_1 + F_0
F_3  =  F_2 + F_1  =  (F_1 + F_0) + F_1          =  2F_1 + F_0
F_4  =  F_3 + F_2  =  (2F_1 + F_0) + (F_1 + F_0)  =  3F_1 + 2F_0
F_5  =  5F_1 + 3F_0,        F_6  =  8F_1 + 5F_0,        …
```

So `F_n = r_1 F_1 + r_0 F_0` with weights `r_0`, `r_1` that depend on `n` and the recurrence but not on the initial values; here `r_1 = F_n` and `r_0 = F_{n−1}`. In the same way, a sequence satisfying Equation (1) has `a_n = r_0 a_0 + r_1 a_1 + ⋯ + r_{D−1} a_{D−1}` for `D` weights, and Kitamasa's method computes them.

## The weights are the remainder of x^n

Write the term `a_i` as the monomial `x^i`, and define the linear map `φ` by `φ(x^i) = a_i`:

```
φ( Σ_i b_i x^i )  =  Σ_i b_i a_i.
```

The characteristic polynomial of Equation (1) is

```
Q(x)  =  x^D − c_1 x^{D−1} − c_2 x^{D−2} − ⋯ − c_D.
```

Equation (1) says that `φ` vanishes on every multiple of `Q`: for every `m ≥ 0`,

```
φ( x^m Q(x) )  =  a_{m+D} − c_1 a_{m+D−1} − ⋯ − c_D a_m  =  0.
```

So two polynomials that differ by a multiple of `Q` have the same value under `φ`. Dividing `x^n` by `Q` gives `x^n = S(x) Q(x) + R(x)` with `deg R < D`, and then

```
a_n  =  φ(x^n)  =  φ(R)  =  r_0 a_0 + r_1 a_1 + ⋯ + r_{D−1} a_{D−1},
```

where `r_0, …, r_{D−1}` are the coefficients of `R(x) = x^n mod Q(x)`. Reducing modulo `Q` is the rewrite rule `x^D → c_1 x^{D−1} + ⋯ + c_D`, which is Equation (1) applied to monomials.

**Cost.** Binary exponentiation computes `x^n mod Q` in `⌊log₂ n⌋` rounds: square and reduce, and multiply by `x` and reduce when the corresponding bit of `n` is 1. A product of two polynomials of degree below `D` takes `O(D²)` operations, and reducing the product, of degree below `2D − 1`, takes `O(D²)` more. So the method takes `O(D² log n)` operations.[^1] With fast polynomial multiplication and division the factor `D²` becomes `O(D log D)`. On the rational-function path at the Project Euler parameters, `D = h = 100`.

## Worked example 1: F_10 by hand

`Q(x) = x² − x − 1`, so the rewrite rule is `x² → x + 1`, and every reduced polynomial has the form `r_0 + r_1 x`. Since `10 = 8 + 2`:

```
x^1   =  x
x^2   =  x + 1
x^4   =  (x + 1)²   =  x² + 2x + 1      →  (x + 1) + 2x + 1       =  3x + 2
x^8   =  (3x + 2)²  =  9x² + 12x + 4    →  9(x + 1) + 12x + 4     =  21x + 13
x^10  =  x^8 · x^2  =  (21x + 13)(x + 1)  =  21x² + 34x + 13
                                         →  21(x + 1) + 34x + 13  =  55x + 34
```

So `F_10 = 55·F_1 + 34·F_0 = 55`. Three squarings and one product replace the ten steps of the recurrence, and at `n = 10^12`, which has 40 binary digits, the method takes 39 squarings and 12 further products. The reduced polynomials are `x^n ≡ F_n x + F_{n−1}` for `n ≥ 1`, the weights of the unrolling in the previous section.

## Worked example 2: P(1, L) at L = 10^12

The signed tower count `P(k, L)` is the sum of `(−1)^{blocks}` over the towers of height at most `k` on a base of length `L` ([[signed-tower-count](pages/signed-tower-count.md)]). At `k = 1` the towers are binary strings, and the values from `L = 0` and the recurrence are[^2]

```
P(1, L)  =  1, 0, −2, −4, −4, 0, 8, 16, 16, 0, −32, −64, …
Q(x)     =  x² − 2x + 2,        so    P(1, L)  =  2·P(1, L−1) − 2·P(1, L−2).
```

For example, `2·(−4) − 2·(−4) = 0` and `2·0 − 2·(−4) = 8`. The rewrite rule is `x² → 2x − 2`. Modulo the prime `p = 10^9 + 7`, the reduction gives a constant:

```
x^{10^12}  mod  (x² − 2x + 2)  ≡  914524917                          (mod p)
P(1, 10^12)  ≡  914524917 · P(1, 0) + 0 · P(1, 1)  =  914524917       (mod p)
```

**Check by the closed form.** `P(1, L) = Re((1+i)^{L+1})`.[^2] Since `(1+i)^8 = 16` and `8` divides `10^12`, `(1+i)^{10^12 + 1} = 16^{10^12/8} (1+i) = 2^{5·10^11} (1+i)`, whose real part is `2^{5·10^11}`, and `2^{5·10^11} ≡ 914524917 (mod p)`.

**Why the reduced polynomial is a constant.** Evaluating `x^n = S(x) Q(x) + R(x)` at a root `λ` of `Q` gives `λ^n = R(λ)`. When the roots of `Q` are distinct, `R` is therefore the polynomial of degree below `D` that takes the value `λ^n` at each root. Here the roots are `1 ± i`, and `(1 ± i)^{10^12} = 2^{5·10^11}` for both, so `R` is that constant.

## Python

`xpow_mod` reduces `x^n` modulo `Q`, and `kitamasa` combines the weights with the initial terms. As in the Java source, `rec[j]` is the coefficient of `a_{n−1−j}`, so `Q(x) = x^D − Σ_j rec[j] x^{D−1−j}`, the implementation notes' characteristic polynomial "`x^d − Σ rec[i] x^{d−1−i}`".[^3] `p = None` means exact integers.

```python
def xpow_mod(rec, n, p=None):
    """Coefficients [r_0, ..., r_{D-1}] of x^n mod Q(x), where
    Q(x) = x^D - rec[0] x^(D-1) - ... - rec[D-1]  is the characteristic polynomial of
    a_n = rec[0] a_{n-1} + ... + rec[D-1] a_{n-D}.  p=None means exact integers."""
    D = len(rec)
    red = (lambda v: v % p) if p else (lambda v: v)

    def mulmod(a, b):                          # (a*b) mod Q, both inputs of degree < D
        prod = [0] * (2*D - 1)
        for i, ai in enumerate(a):
            for j, bj in enumerate(b):
                prod[i+j] = red(prod[i+j] + ai*bj)
        for m in range(2*D - 2, D - 1, -1):    # fold x^m down via x^D = sum_j rec[j] x^(D-1-j)
            c, prod[m] = prod[m], 0
            for j in range(D):
                prod[m-1-j] = red(prod[m-1-j] + c*rec[j])
        return prod[:D]

    result = [1] + [0]*(D-1)                                  # the polynomial 1
    base = ([0, 1] + [0]*(D-2)) if D > 1 else [red(rec[0])]  # the polynomial x, already reduced
    while n:                                                  # binary exponentiation
        if n & 1:
            result = mulmod(result, base)
        base = mulmod(base, base)
        n >>= 1
    return result

def kitamasa(rec, init, n, p=None):
    """a_n from the recurrence rec and the first D terms init = [a_0, ..., a_{D-1}]."""
    if n < len(rec):
        return init[n] % p if p else init[n]
    r = xpow_mod(rec, n, p)
    v = sum(ri * ai for ri, ai in zip(r, init))
    return v % p if p else v
```

Run on the two worked examples, the functions print ([[castle-snippets](pages/castle-snippets.md)]):[^4]

```
>>> xpow_mod([1, 1], 10)                    # Fibonacci: x^10 mod (x^2 - x - 1)
[34, 55]
>>> kitamasa([1, 1], [0, 1], 10)           # F_10 = 34*F_0 + 55*F_1
55
>>> [xpow_mod([1, 1], n) for n in (1, 2, 4, 8)]
[[0, 1], [1, 1], [2, 3], [13, 21]]
>>> [kitamasa([2, -2], [1, 0], L) for L in range(12)]     # P(1, L), L = 0..11
[1, 0, -2, -4, -4, 0, 8, 16, 16, 0, -32, -64]
>>> p = 10**9 + 7
>>> kitamasa([2, -2], [1, 0], 10**12, p)   # P(1, 10^12) mod p
914524917
>>> pow(2, 5 * 10**11, p)                  # closed form Re((1+i)^(10^12 + 1)) = 2^(5*10^11)
914524917
>>> xpow_mod([2, -2], 10**12, p)           # the reduced polynomial is a constant
[914524917, 0]
>>> [kitamasa([3, -4, 4], [1, 1, 3], L) for L in range(9)]  # P(2, L), order 3
[1, 1, 3, 9, 19, 33, 59, 121, 259]
>>> kitamasa([3, -4, 4], [1, 1, 3], 10**6, p)   # agrees with walking the recurrence 10**6 steps mod p
233243828
```

The last two lines are the case of order 3: `P(2, ·)` has characteristic polynomial `x³ − 3x² + 4x − 4`,[^5] so `rec = [3, −4, 4]`.

## How the castle count uses it

Both computational paths of the castle count give Kitamasa's method a recurrence, found in two ways.

**The rational-function path, `h ≤ 15000`.** The generating function `P_k(x) = Σ_L P(k, L) x^L` is `num_k(x)/den_k(x)`, where `den_k(x) = 1 + d_1 x + ⋯ + d_D x^D` has degree `D = k + 1` ([[castle-counting-formula](pages/castle-counting-formula.md)], the Proposition in the section *Signed tower count*). Comparing the coefficients of `x^L` in `den_k(x) P_k(x) = num_k(x)` for `L` above the degree of `num_k` gives

```
P(k, L)  =  −d_1 P(k, L−1) − ⋯ − d_D P(k, L−D),
```

whose characteristic polynomial `x^D den_k(1/x) = x^D + d_1 x^{D−1} + ⋯ + d_D` is the denominator with its coefficients reversed.[^6] The Java source builds this polynomial from `−den[1..D]`.[^3] `P(h−1, w)` at `w = 10^12` and `h = 100` is a jump of Kitamasa's method with `D = 100`, which is how the term `A^e(10^12, 100)` is computed.[^7] For small `w` the power series of `num_k/den_k`, in `O(wD)` operations, is cheaper, and the source uses it when `w ≤ D + 1` or `w · min(w, D) < 50D²`.[^7]

**The Berlekamp-Massey path, `h > 15000`.** For fixed `w`, the source computes `P(0, w), …, P(N−1, w)` modulo `p`, finds a recurrence in `k` with Berlekamp-Massey, and jumps with Kitamasa's method to `k = h − 2`.[^8] Since `x^{n+1} = x · x^n`, the remainder for `k = h − 1` is `x` times the remainder for `k = h − 2`, reduced once more modulo `Q`, which takes `O(D)` operations instead of a second exponentiation.[^9] The term `A^e(100, 10^12)` is computed this way ([[castle-count-algorithms](pages/castle-count-algorithms.md)]).

## The companion matrix

The recurrence (1) also advances the state `(a_{n+D−1}, …, a_n)` by one step through the `D × D` companion matrix `M`, which has `c_1, …, c_D` in its top row, the shifted identity below it, and characteristic polynomial `Q`. Computing `M^n` by repeated squaring takes `O(log n)` products of `D × D` matrices, `O(D³ log n)` operations in all. By the Cayley-Hamilton theorem, which says that a matrix satisfies its own characteristic polynomial, `Q(M) = 0`, so `M^n = S(M) Q(M) + R(M) = R(M)` with `R = x^n mod Q`: Kitamasa's method computes the same power with polynomials of degree below `D` in place of `D × D` matrices, in `O(D² log n)` operations. This is the source's reason for not using the transfer matrix in the `L` direction as the main method, "`O(D^3 log w)` versus `O(D^2 log w)` for Kitamasa".[^10][^11]

## Name and scope

"Kitamasa" is the name the castle sources use.[^1] Kitamasa's method applies to every sequence with a linear recurrence, equivalently with a rational generating function. Among polyomino counts, the horizontally convex polyominoes by area satisfy a recurrence of order 3 ([[counting-horizontally-convex-polyominoes](pages/counting-horizontally-convex-polyominoes.md)]). The orders of the castle recurrences are `k + 1` in `L` (proved on [[castle-counting-formula](pages/castle-counting-formula.md)]) and `2L − 2` in `k` for `4 ≤ L ≤ 12` (computed, [[recurrence-discovery](pages/recurrence-discovery.md)]).

## Appearances in Sources

- [[project-euler-502-solution](pages/project-euler-502-solution.md)] - Kitamasa's method as the extractor on both computational paths, the rule for choosing it over the power series, and its cost against the transfer matrix.
- [[project-euler-502-implementation-notes](pages/project-euler-502-implementation-notes.md)] - the switch `extractCoeff`, the characteristic polynomial built from `−den[1..D]`, and the shift `poly2 · x mod charPoly`.
- [[generating-functions-topic](pages/generating-functions-topic.md)] - the coefficients of `num_k/den_k` satisfy a linear recurrence whose characteristic polynomial is the reversed denominator, "exactly the setup where Kitamasa's method applies".
- [[project-euler-502-representations](pages/project-euler-502-representations.md)] - the recurrences of `P(1, ·)` and `P(2, ·)` and the closed form `P(1, L) = Re((1+i)^{L+1})`.

## Related Concepts

- [[berlekamp-massey](pages/berlekamp-massey.md)] - the algorithm that finds the recurrence in `k` for the second path.
- [[castle-count-algorithms](pages/castle-count-algorithms.md)] - the two computational paths and the route of each Project Euler target.
- [[castle-counting-formula](pages/castle-counting-formula.md)] - the formula for `A^e(w, h)` through `P(h−1, w)` and `P(h−2, w)`, and the degree of `den_k`.
- [[signed-tower-count](pages/signed-tower-count.md)] - the values and characteristic polynomials of `P(k, ·)`, including the two worked here.
- [[hyperbolic-sequence-family](pages/hyperbolic-sequence-family.md)] - `A146559 = A038503 − A038505`, the real parts of `(1+i)^n`, which give `P(1, L)`.
- [[recurrence-discovery](pages/recurrence-discovery.md)] - the orders of the castle recurrences in `L` and in `k`, found by Berlekamp-Massey.
- [[castle-snippets](pages/castle-snippets.md)] - short tested snippets that enumerate castles, for checks against these values.
- [[counting-horizontally-convex-polyominoes](pages/counting-horizontally-convex-polyominoes.md)] - Hickerson's recurrence `a(n) = 5a(n−1) − 7a(n−2) + 4a(n−3)` for the horizontally convex polyominoes.
- [[new-sequence-fw3](pages/new-sequence-fw3.md)] - the row `A^e(w, 3) = (3^w − 2^w − P(2, w) + P(1, w))/2`, built from the two sequences worked here.
- [[algebraic-transcendental-wall](pages/algebraic-transcendental-wall.md)] - the closed forms of the castle counts, sums over the algebraic roots `λ` of their characteristic polynomials.
- [[oeis-mining-pe502](pages/oeis-mining-pe502.md)] - the castle counts matched against the OEIS, among them `P(1, L) = A146559(L+1)`.

## Footnotes

[^1]: [[project-euler-502-solution](pages/project-euler-502-solution.md)] §"The rational-function path (h ≤ 15000)" L145 - "Kitamasa: turn the recurrence into \"compute x^w mod charPoly\", then O(D^2 log w)."
[^2]: [[project-euler-502-representations](pages/project-euler-502-representations.md)] §"Signed count" L345 - "k=1: P(1,L) = 2P(1,L-1) - 2P(1,L-2), closed form P(1,L) = Re((1+i)^{L+1})". The twelve values agree with the sum over all binary strings of length `L ≤ 11` (verified by execution, Python 3.11, 2026-10-25).
[^3]: [[project-euler-502-implementation-notes](pages/project-euler-502-implementation-notes.md)] §"Rational-function path" L39-41 - "extractCoeff - the direct-vs-Kitamasa switch", "extractCoeffMatExp + kitamasa + polyMulMod - standard Kitamasa on the characteristic polynomial x^d - ∑ rec[i] x^{d-1-i} derived from -den[1..D]."
[^4]: Verified by execution (Python 3.11, 2026-10-16): every output shown, `P(1, L)` and `P(2, L)` against the sum over all towers, and `kitamasa([3, −4, 4], [1, 1, 3], 10**6, p)` against walking the recurrence `10^6` steps modulo `p`.
[^5]: [[project-euler-502-representations](pages/project-euler-502-representations.md)] §"Signed count" L346 - "k=2: P(2,L) = 3P(2,L-1) - 4P(2,L-2) + 4P(2,L-3)".
[^6]: [[generating-functions-topic](pages/generating-functions-topic.md)] §"Application: Project Euler 502" L123-126 - "The P(k, L) recursion ... lifts to a rational generating function F_k(x) = num_k(x) / den_k(x) with level-by-level update rules. Coefficient extraction reduces to a linear recurrence with characteristic polynomial den_k(x) (reversed), which is exactly the setup where Kitamasa's method applies."
[^7]: [[project-euler-502-solution](pages/project-euler-502-solution.md)] §"The rational-function path (h ≤ 15000)" L147-153 - "Direct wins when w ≤ D+1 or w · min(w, D) < 50 D^2; otherwise Kitamasa" and "F(10^12, 100): h = 100 ≤ 15000, this path is taken; D ≈ 101, w = 10^12 gives Kitamasa." The degree `D` of `den_{h−1}` is exactly `h` ([[castle-counting-formula](pages/castle-counting-formula.md)]).
[^8]: [[project-euler-502-solution](pages/project-euler-502-solution.md)] §"The k-direction Berlekamp-Massey path (h > 15000)" L157-161 - "generate P(0, w), P(1, w), …, P(N-1, w) ... all mod p. Then: Berlekamp-Massey finds the minimal linear recurrence. Kitamasa jumps directly to any index k. Both P(h-2, w) and P(h-1, w) are computed in one pass, saving a factor of 2."
[^9]: [[project-euler-502-implementation-notes](pages/project-euler-502-implementation-notes.md)] §"k-direction BM path" L50-51 - "kitamasa(rec, order, k2, p) gives poly2 for P(h-2, w). poly1 is computed as poly2 * x mod charPoly in-line, saving a second Kitamasa call for P(h-1, w)."
[^10]: [[project-euler-502-solution](pages/project-euler-502-solution.md)] §"What was tried and did not work" L191 - "L-direction transfer matrix as the primary solve. Works, but slower than the rational-function form: the matrix power costs O(D^3 log w) versus O(D^2 log w) for Kitamasa."
[^11]: [[project-euler-502-implementation-notes](pages/project-euler-502-implementation-notes.md)] §"Matrix helpers" L58 - "matmul and matpow exist for computePviaK (the single-value variant). computePviaKBoth uses Kitamasa instead, so matrix exponentiation is unused on the composite path."
