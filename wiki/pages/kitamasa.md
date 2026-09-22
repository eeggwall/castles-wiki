---
title: Kitamasa
category: Concepts
summary: The fast way to get one far-off term of a linear recurrence - reduce x^n modulo the characteristic polynomial and read a_n off as a fixed combination of the first D terms, in O(D² log n). Taught via Fibonacci by hand and the castle's own P(1,L) jumped to L = 10^12; the extractor both castle solve paths use.
tags: [concept, algorithm, linear-recurrence, kitamasa, method, c-finite, pedagogy, teaching]
sources: [project-euler-502-solution, project-euler-502-implementation-notes, generating-functions-topic, oeis-mining-pe502]
created: 2026-09-13
updated: 2026-09-19
---

# Kitamasa

## What problem it solves

You have a sequence that obeys a fixed linear recurrence of order *D*,

```
a_n = c_1 a_{n−1} + c_2 a_{n−2} + … + c_D a_{n−D},
```

you know the first *D* terms `a_0, …, a_{D−1}`, and you want **one** term `a_n` at an enormous index - `n = 10^12`, say - without visiting the trillion terms in between. Walking the recurrence costs `O(nD)`. **Kitamasa** gets the same term in `O(D² log n)`: reduce the polynomial `x^n` modulo the recurrence's characteristic polynomial, then read `a_n` off as a fixed linear combination of `a_0, …, a_{D−1}`.[^1]

It is the natural partner of [[berlekamp-massey](pages/berlekamp-massey.md)]: Berlekamp–Massey *discovers* the minimal recurrence from sample terms; Kitamasa then *jumps* to any index of that recurrence. In the castle solve this is how the signed tower count `P(k,L)` is reached at index `10^12`, in both the *L* and the *k* direction (see [[castle-count-algorithms](pages/castle-count-algorithms.md)] and the section "How the castle solve uses it" below).

## The idea: every term is a fixed combination of the first D

Start with something you can check by hand. Fibonacci: `F_0 = 0`, `F_1 = 1`, `F_n = F_{n−1} + F_{n−2}`. Unroll the recurrence without ever plugging in the starting values:

```
F_2 = F_1 + F_0
F_3 = F_2 + F_1 = (F_1 + F_0) + F_1        = 2F_1 + F_0
F_4 = F_3 + F_2 = (2F_1 + F_0) + (F_1 + F_0) = 3F_1 + 2F_0
F_5 = 5F_1 + 3F_0,     F_6 = 8F_1 + 5F_0,     …
```

No matter how far you go, `F_n` is always `r_1·F_1 + r_0·F_0` for two **weights** `(r_0, r_1)` that depend only on *n* and the recurrence, never on the starting values. The same holds for any order-*D* recurrence: `a_n = r_0 a_0 + r_1 a_1 + … + r_{D−1} a_{D−1}` for *D* weights. Kitamasa is nothing more than a way to compute those *D* weights in `O(D² log n)` instead of unrolling *n* times. (For Fibonacci the weights happen to be Fibonacci numbers themselves, `r_1 = F_n`, `r_0 = F_{n−1}` - a handy sanity check later.)

## Why polynomials: the recurrence says "x^D ≡ c_1 x^{D−1} + … + c_D"

The bookkeeping trick is to write "the term `a_i`" as the monomial `x^i`. A linear combination of terms becomes a polynomial, and "the weights of `a_n`" becomes the polynomial `r_0 + r_1 x + … + r_{D−1} x^{D−1}`. Make this precise with the evaluation map

```
φ( Σ_i b_i x^i )  =  Σ_i b_i a_i          (send each x^i to a_i, extend linearly)
```

and the **characteristic polynomial**

```
Q(x) = x^D − c_1 x^{D−1} − c_2 x^{D−2} − … − c_D .
```

The recurrence says *exactly* that φ kills `Q` and every multiple of `Q`: for any `m ≥ 0`,

```
φ( x^m · Q(x) ) = a_{m+D} − c_1 a_{m+D−1} − … − c_D a_m = 0 .
```

So two polynomials that differ by a multiple of `Q` have the same φ-value. Now divide `x^n` by `Q`: `x^n = S(x)·Q(x) + R(x)` with `deg R < D`. Then

```
a_n = φ(x^n) = φ(R) = r_0 a_0 + r_1 a_1 + … + r_{D−1} a_{D−1} .
```

**That is the whole method.** The *D* weights are the coefficients of `R(x) = x^n mod Q(x)`. Working "mod Q" just means applying the rewrite rule `x^D → c_1 x^{D−1} + … + c_D` whenever a power of *x* reaches degree *D* - the recurrence itself, applied to monomials instead of numbers.

**Where the `log n` comes from.** Compute `x^n mod Q` by binary exponentiation: square, reduce, square, reduce, multiplying in one more `x` whenever the corresponding bit of *n* is set. There are `log₂ n` rounds; each multiplies two polynomials of degree `< D` (`O(D²)`) and folds the degree-`< 2D` product back below degree *D* (`O(D²)`). Total `O(D² log n)`.[^1] With Fast Fourier Transform (FFT)-based polynomial multiplication the `D²` drops to `D log D`, but the castle's `D ≈ 100` makes the plain product cheap enough.

## Worked example 1: F_10 by hand

`Q(x) = x² − x − 1`, so the rewrite rule is `x² → x + 1`, and every reduced polynomial has the form `r_0 + r_1 x`. Binary exponentiation for `n = 10 = 8 + 2`:

```
x^1  = x
x^2  = x + 1
x^4  = (x + 1)²  = x² + 2x + 1       → (x + 1) + 2x + 1   = 3x + 2
x^8  = (3x + 2)² = 9x² + 12x + 4     → 9(x + 1) + 12x + 4 = 21x + 13
x^10 = x^8 · x^2 = (21x + 13)(x + 1) = 21x² + 34x + 13
                                     → 21(x + 1) + 34x + 13 = 55x + 34
```

Read off: `F_10 = 55·F_1 + 34·F_0 = 55` ✓. Three squarings and one extra multiply replaced ten steps of the recurrence; at `n = 10^12` it would be about forty squarings instead of a trillion steps. Notice `x^n ≡ F_n x + F_{n−1}` throughout - the weights *are* the Fibonacci numbers, matching the unrolling above.

## Worked example 2: a castle sequence at index 10^12

The castle's own C-finite sequences are the signed tower counts `P(k,L) = Σ (−1)^{blocks}` over towers of height `≤ k` above a length-*L* block ([[signed-tower-count](pages/signed-tower-count.md)]). The simplest, `P(1,L)`, sums `(−1)^{runs of 1s}` over the binary strings of length *L*; its values from `L = 0` and its characteristic polynomial are[^9]

```
P(1,L) = 1, 0, −2, −4, −4, 0, 8, 16, 16, 0, −32, −64, …
Q(x)   = x² − 2x + 2          i.e.   P(1,L) = 2·P(1,L−1) − 2·P(1,L−2)
```

(re-verified here by brute-force enumeration of the towers; check the recurrence: `2·(−4) − 2·(−4) = 0`, `2·0 − 2·(−4) = 8` ✓). The rewrite rule is `x² → 2x − 2`. Ask for `P(1, 10^12)` modulo the prime `p = 10^9 + 7`. Forty squarings later:

```
x^(10^12) mod (x² − 2x + 2)  ≡  914524917          (mod p) - a pure constant, no x term
P(1, 10^12)  ≡  914524917 · P(1,0) + 0 · P(1,1)  =  914524917   (mod p)
```

**Independent check.** `P(1,L) = Re((1+i)^{L+1})`.[^9] Since `(1+i)^8 = 16` and `10^12` is a multiple of 8, `(1+i)^{10^12 + 1} = 16^{10^12/8} · (1+i) = 2^{5·10^11} (1+i)`, whose real part is `2^{5·10^11}`, and `pow(2, 5·10^11, p) = 914524917` ✓ - the same residue the polynomial reduction produced.

**Why the x-coefficient vanished - the spectral reading.** Evaluate `x^n = S·Q + R` at a root λ of `Q`: `Q(λ) = 0`, so `λ^n = R(λ)`. The reduced polynomial `R` is the polynomial of degree `< D` that agrees with `λ ↦ λ^n` on the eigenvalues. Here the eigenvalues are `1 ± i`, and `(1 ± i)^{10^12} = 2^{5·10^11}` is real and identical for both, so `R` is that constant. Kitamasa is thus a way to compute with the eigenvalue powers the [[spectral-analysis](pages/spectral-analysis.md)] pages study without ever computing an eigenvalue - everything stays in integers mod *p*.

## Python: Kitamasa in thirty lines

Two functions, mirroring the two steps: `xpow_mod` reduces `x^n` modulo `Q`, `kitamasa` folds the weights against the initial terms. Conventions match the Java: `rec[j]` is the coefficient of `a_{n−1−j}`, so `Q(x) = x^D − Σ_j rec[j] x^{D−1−j}` - the implementation notes' "`x^d − Σ rec[i] x^{d−1−i}`".[^5] `p=None` means exact integers.

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

Run in a scratch script, outputs pinned (the [[castle-snippets](pages/castle-snippets.md)] discipline):

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
>>> xpow_mod([2, -2], 10**12, p)           # the reduced polynomial is a pure constant
[914524917, 0]
>>> [kitamasa([3, -4, 4], [1, 1, 3], L) for L in range(9)]  # P(2, L), order 3
[1, 1, 3, 9, 19, 33, 59, 121, 259]
>>> kitamasa([3, -4, 4], [1, 1, 3], 10**6, p), naive_walk_to(10**6)
233243828 233243828
```

The last two lines exercise an order-3 case: `P(2,·)` has characteristic polynomial `x³ − 3x² + 4x − 4`,[^10] i.e. `rec = [3, −4, 4]`, and the jump to `L = 10^6` agrees with walking the recurrence a million steps (the `P(2,L)` values were also re-verified by brute-force enumeration of the height-≤2 towers).

## From rational generating function to recurrence: how the castle solve uses it

Both computational paths of the castle solve hand Kitamasa a recurrence - but they get the recurrence in different ways.

**Rational-function path (`h ≤ 15000`).** The signed tower count has the rational generating function `P_k(x) = num_k(x) / den_k(x)`. A rational generating function *is* a linear recurrence: if `den(x) = 1 − d_1 x − … − d_D x^D`, multiply out `den(x)·P(x) = num(x)` and compare coefficients of `x^n` for *n* past the numerator's degree to get `c_n = d_1 c_{n−1} + … + d_D c_{n−D}`. Its characteristic polynomial is `x^D · den(1/x) = x^D − d_1 x^{D−1} − … − d_D` - the denominator *reversed*[^8] - which is exactly the "`−den[1..D]`" construction the code uses to build `charPoly`.[^5] Extracting `[x^w] P_{h−1}(x)` at `w = 10^12` is then a Kitamasa jump to index `10^12` with `D ≈ 101`: about forty squarings of a degree-100 polynomial, which is how `F(10^12, 100)` is computed.[^2] For small *w* a direct power-series expansion (`O(wD)`) is cheaper; the code's crossover rule is "direct when `w ≤ D+1` or `w·min(w,D) < 50D²`, otherwise Kitamasa" - the point where the `log w` saving beats the `D²` setup cost.[^2]

**k-direction path (`h > 15000`).** For fixed *w*, generate `P(0,w), …, P(N−1,w)` modulo *p*, let Berlekamp–Massey find the recurrence in *k*, and Kitamasa jumps to `k = h−2` to obtain `P(h−2,w)`.[^3] The neighbor `P(h−1,w)` is then obtained by multiplying the reduced polynomial by *x* and reducing once more - since `x^{n+1} = x · x^n`, the next term costs one `O(D²)` reduction instead of a second `O(D² log n)` exponentiation.[^7]

## Why not just power the matrix?

The textbook way to jump a recurrence is the **companion (transfer) matrix** *M* - the `D×D` matrix whose characteristic polynomial is `Q`, with the `c_i` across its top row and a shifted identity beneath - which advances the state vector `(a_{n+D−1}, …, a_n)` by one step, so *n* steps is `M^n`. Powering *M* by repeated squaring costs `log n` matrix products at `O(D³)` each. Kitamasa is the *same* computation with a *D*-times smaller footprint: by Cayley–Hamilton `Q(M) = 0`, so `M^n = S(M)Q(M) + R(M) = R(M)` with `R = x^n mod Q`, and the *D* coefficients of `R` already carry everything `a_n` needs (`a_n = Σ r_i a_i`). Tracking *D* numbers instead of `D²` is the whole saving. This is why the castle solution rejected the *L*-direction transfer matrix as the primary solve - `O(D³ log w)` versus `O(D² log w)`[^4] - and why the Java's `matmul`/`matpow` helpers sit unused on the composite path.[^6]

## Names and a thread to follow

"Kitamasa" is the competitive-programming name for the method, and the name the castle sources use.[^1] In the algorithms literature the same idea - evaluate `x^n` modulo the characteristic polynomial, then combine with the initial terms - is credited to Fiduccia (1985).[^11]

**A thread to follow.** Kitamasa applies to any C-finite (linear-recurrent, equivalently rational-generating-function) enumeration, which is what places the castle count alongside other polyomino families that collapse to short recurrences - [[counting-horizontally-convex-polyominoes](pages/counting-horizontally-convex-polyominoes.md)] (a 2-D family with an order-3 recurrence) and [[column-convex-polygon-enumeration](pages/column-convex-polygon-enumeration.md)]. For how the castle's own recurrence orders were pinned down (`k+1` in the *L*-direction, `2L−2` in the *k*-direction), see [[recurrence-discovery](pages/recurrence-discovery.md)].

## Appearances in Sources

- [[project-euler-502-solution](pages/project-euler-502-solution.md)] - uses Kitamasa as the large-index extractor on both computational paths, gives the direct-vs-Kitamasa crossover, and contrasts its cost with the transfer-matrix approach.
- [[project-euler-502-implementation-notes](pages/project-euler-502-implementation-notes.md)] - the `extractCoeff` switch, the `charPoly` construction from `−den[1..D]`, and the `poly2 · x mod charPoly` one-step shift.
- [[generating-functions-topic](pages/generating-functions-topic.md)] - states the bridge used above: coefficient extraction from `num_k/den_k` is a linear recurrence whose characteristic polynomial is the reversed denominator, "exactly the setup where Kitamasa's method applies."
- [[oeis-mining-pe502](pages/oeis-mining-pe502.md)] - the `P(k,·)` characteristic polynomials and `P(1,L) = Re((1+i)^{L+1})` behind worked example 2.

## Related Concepts

- [[berlekamp-massey](pages/berlekamp-massey.md)] - finds the recurrence Kitamasa then jumps along.
- [[castle-count-algorithms](pages/castle-count-algorithms.md)] - the two paths where Kitamasa is used.
- [[castle-counting-formula](pages/castle-counting-formula.md)] - the `P(k,L)` term Kitamasa evaluates at large index.
- [[signed-tower-count](pages/signed-tower-count.md)] - the C-finite `P(k,·)` family; `P(1,·)` and `P(2,·)` are the worked examples above.
- [[hyperbolic-sequence-family](pages/hyperbolic-sequence-family.md)] - where `Re((1+i)^n)`, the closed form behind the `P(1, 10^12)` check, sits among the "every 4th binomial" sequences.
- [[spectral-analysis](pages/spectral-analysis.md)] - the eigenvalue reading `R(λ) = λ^n` of the reduced polynomial.
- [[recurrence-discovery](pages/recurrence-discovery.md)] - the recurrence orders in each direction, established by Berlekamp–Massey.
- [[castle-snippets](pages/castle-snippets.md)] - the run-it-first discipline the Python section follows; enumeration one-liners for cross-checks.
- [[counting-horizontally-convex-polyominoes](pages/counting-horizontally-convex-polyominoes.md)] - a polyomino family whose count collapses to a short linear recurrence, the C-finite phenomenon Kitamasa exploits.
- [[new-sequence-fw3](pages/new-sequence-fw3.md)] - `F(w,3) = (3^w − 2^w − P(2,w) + P(1,w))/2`: the `P(2,·)` jumped to `L = 10^6` in Worked example 2 is one of its four components.
- [[algebraic-transcendental-wall](pages/algebraic-transcendental-wall.md)] - the "spectral reading" `R(λ) = λ^n` on eigenvalue roots realizes the wall's thesis: C-finite closed forms carry only algebraic eigenvalues.

## Footnotes

[^1]: [[project-euler-502-solution](pages/project-euler-502-solution.md)] §"The rational-function path (h ≤ 15000)" L145 — "Kitamasa: turn the recurrence into 'compute x^w mod charPoly', then O(D^2 log w)."
[^2]: [[project-euler-502-solution](pages/project-euler-502-solution.md)] §"The rational-function path (h ≤ 15000)" L147-153 — "Direct wins when w ≤ D+1 or w · min(w, D) < 50 D^2; otherwise Kitamasa. The tradeoff is the crossover point where the log w saving beats the D^2 setup cost" and "F(10^12, 100): ... D ≈ 101, w = 10^12 gives Kitamasa."
[^3]: [[project-euler-502-solution](pages/project-euler-502-solution.md)] §"The k-direction Berlekamp-Massey path (h > 15000)" L157-161 — "generate P(0, w), P(1, w), …, P(N-1, w) ... all mod p. Then: Berlekamp-Massey finds the minimal linear recurrence. Kitamasa jumps directly to any index k. Both P(h-2, w) and P(h-1, w) are computed in one pass."
[^4]: [[project-euler-502-solution](pages/project-euler-502-solution.md)] §"What was tried and did not work" L191 — "L-direction transfer matrix as the primary solve. Works, but slower than the rational-function form: the matrix power costs O(D^3 log w) versus O(D^2 log w) for Kitamasa."
[^5]: [[project-euler-502-implementation-notes](pages/project-euler-502-implementation-notes.md)] §"Rational-function path" L39-41 — "extractCoeff - the direct-vs-Kitamasa switch. extractCoeffDirect - unrolled by 8 ... extractCoeffMatExp + kitamasa + polyMulMod - standard Kitamasa on the characteristic polynomial x^d - ∑ rec[i] x^{d-1-i} derived from -den[1..D]."
[^6]: [[project-euler-502-implementation-notes](pages/project-euler-502-implementation-notes.md)] §"Matrix helpers" L58 — "matmul and matpow exist for computePviaK (the single-value variant). computePviaKBoth uses Kitamasa instead, so matrix exponentiation is unused on the composite path."
[^7]: [[project-euler-502-implementation-notes](pages/project-euler-502-implementation-notes.md)] §"k-direction BM path" L50-51 — "kitamasa(rec, order, k2, p) gives poly2 for P(h-2, w). poly1 is computed as poly2 * x mod charPoly in-line, saving a second Kitamasa call for P(h-1, w)."
[^8]: [[generating-functions-topic](pages/generating-functions-topic.md)] §"Application: Project Euler 502" L123-126 — "The P(k, L) recursion ... lifts to a rational generating function F_k(x) = num_k(x) / den_k(x) with level-by-level update rules. Coefficient extraction reduces to a linear recurrence with characteristic polynomial den_k(x) (reversed), which is exactly the setup where Kitamasa's method applies."
[^9]: [[oeis-mining-pe502](pages/oeis-mining-pe502.md)] `mine-notes.md` §"Vein 1" L16,L25-32 — "P(k,L) = sum_{c_1..c_L in 0..k} (-1)^#blocks" ... "P(1,L) = Re((1+i)^{L+1}) = A146559(L+1)" ... "P(1,L) = 0,-2,-4,-4,0,8,16,16,0,-32,..." (listed from L = 1) ... "P(1): x^2 - 2x + 2 (eigenvalues 1 +/- i)"; values, recurrence, and the closed form re-verified by execution for this page (brute-force enumeration for L ≤ 11, Kitamasa vs. closed form at L = 10^12).
[^10]: [[oeis-mining-pe502](pages/oeis-mining-pe502.md)] `mine-notes.md` §"Vein 1" L31-33 — "The general P(k,·) family is C-finite of order k+1: ... P(2): x^3 - 3x^2 + 4x - 4 (= (x-2)(x^2-x+2))"; the values 1, 1, 3, 9, 19, 33, 59, 121 (from L = 0) re-verified by brute-force enumeration for this page.
[^11]: https://doi.org/10.1137/0214007 (1985) [synthesis] — C. M. Fiduccia, "An Efficient Formula for Linear Recurrences", SIAM Journal on Computing 14(1):106-112; bibliographic record confirmed via Crossref and Semantic Scholar on 2026-09-16. Cited for the attribution of the "x^n modulo the characteristic polynomial" formula in the algorithms literature.
