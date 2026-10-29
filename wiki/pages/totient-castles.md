---
title: Totient castles
category: Concepts
summary: A totient castle is a castle whose neighboring columns have coprime heights, so a column of height a can be followed by about h φ(a)/a heights, φ(a) Euler's totient. The rule's matrix is the coprimality matrix M_h on {1, …, h}. At height 2 the totient castles are the Fibonacci castles, golden by width; at height 3 their strips are the Pell-Lucas numbers A001333(w + 1), like the 1-smooth strips on {1, 2, 3}, and the castles are silver by width; at heights 4 to 8 they grow at 2.9354, 3.9173, 4.1747, 5.2572 and 5.7698 by width. For large h the largest eigenvalue of M_h is Λh + O(h^{1/2+ε}), with the Euler product Λ = Π_p (1 − (1 − x_p)/p) = 0.67846225…, x_p the positive root of x² + (p − 1)x − (p − 1): the vector with entries Π_{p | a} x_p is an approximate eigenvector, and the Collatz-Wielandt bounds close in on Λh. So the totient castles of height h grow by width at about 0.6785 h, more than the share 6/π² = 0.6079 of coprime pairs. By area, over all heights, they are the compositions with coprime neighboring parts, A167606, growing like 1.87801…^n.
tags: [concept, castle, totient-castle, castle-strip, transfer-matrix, coprime, euler-totient, euler-product, perron-frobenius, collatz-wielandt, fibonacci, pell-lucas, growth-constant, parity, verification]
sources: [project-euler-502-brute-force]
created: 2026-10-28
updated: 2026-10-28
---

# Totient castles

## Definition

A **totient castle** is a castle `(c_1, …, c_w)` whose neighboring columns have coprime heights:

```
gcd(c_i, c_{i+1})  =  1     for 1 ≤ i < w.
```

Two neighboring columns can be equal only at height 1, since `gcd(a, a) = a`. For example, `(1, 2, 3, 4, 1, 5)` is a totient castle of width 6 and height 5; `(2, 4, 1)` is not, since `gcd(2, 4) = 2`. The name is for Euler's totient `φ(a)`, the number of integers in `1, …, a` coprime to `a`, and for Euler's products over the primes, one of which gives the growth of the family (section *The Euler product*).

The rule is a castle-strip rule ([[castle-strip](pages/castle-strip.md)]): the **coprimality matrix** `M_h` is the `h × h` 0/1 matrix with `M_h[a][b] = 1` exactly when `gcd(a, b) = 1`. Row `a` has `#{b ≤ h : gcd(a, b) = 1}` ones, about `h φ(a)/a`. The totient strips of width `w` on the heights `1, …, h` number `𝟙ᵀ M_h^{w−1} 𝟙`, and the totient castles of width `w` and height `h` are the strips that reach `h`:

```
A_totient(w, h)  =  𝟙ᵀ M_h^{w−1} 𝟙  −  𝟙ᵀ M_{h−1}^{w−1} 𝟙.
```

| `h` | `A_totient(w, h)`, `w = 1, …, 10` |
|---|---|
| 2 | `1, 2, 4, 7, 12, 20, 33, 54, 88, 143` |
| 3 | `1, 4, 12, 33, 86, 218, 543, 1338, 3274, 7975` |
| 4 | `1, 4, 16, 55, 184, 590, 1859, 5754, 17622, 53473` |
| 5 | `1, 8, 42, 197, 866, 3670, 15191, 61898, 249492, 997931` |
| 6 | `1, 4, 24, 115, 564, 2634, 12185, 55346, 248934, 1108617` |

Every entry agrees with brute-force enumeration for `w ≤ 7`.[^exec1]

The strips themselves, the words over `{1, …, h}` whose neighboring letters are coprime, number:[^exec7]

| `h` | `𝟙ᵀ M_h^{w−1} 𝟙`, `w = 1, …, 10` |
|---|---|
| 2 | `2, 3, 5, 8, 13, 21, 34, 55, 89, 144`, the Fibonacci numbers `F_{w+2}` |
| 3 | `3, 7, 17, 41, 99, 239, 577, 1393, 3363, 8119`, the Pell-Lucas numbers `A001333(w + 1)` |
| 4 | `4, 11, 33, 96, 283, 829, 2436, 7147, 20985, 61592` |
| 5 | `5, 19, 75, 293, 1149, 4499, 17627, 69045, 270477, 1059523` |
| 6 | `6, 23, 99, 408, 1713, 7133, 29812, 124391, 519411, 2168140` |
| 7 | `7, 35, 187, 977, 5149, 27043, 142227, 747605, 3930581, 20663491` |

## Notation used on this page

| symbol | meaning |
|---|---|
| `φ(a)`, `φ` | `φ(a)`, always with its argument, is Euler's totient; the bare `φ` is the golden ratio `(1 + √5)/2` |
| `M_h`, `ρ(M_h)` | the coprimality matrix on `1, …, h` and its largest eigenvalue |
| `A_totient(w, h)`, `A^e_totient`, `A^o_totient`, `S_totient` | the totient castles of width `w` and height `h`; the even-block and odd-block ones; `A^e_totient − A^o_totient` |
| `A_totient(n)`, `A^e_totient(n)`, `S_totient(n)` | the same counts over the totient castles of area `n`, of any height |
| `x_p`, `Λ` | the positive root of `x² + (p − 1)x − (p − 1)` for a prime `p`, and `Λ = Π_p (1 − (1 − x_p)/p)` |
| `v_a`, `g(d)` | `v_a = Π_{p | a} x_p`; the multiplicative function with `g(p) = x_p − 1` and `g(d) = 0` unless `d` is squarefree |
| `ω(a)`, `τ(d)` | the number of distinct prime factors of `a`, and the number of divisors of `d` |

## Small heights

**Height 2.** `M_2 = [[1, 1], [1, 0]]` forbids two neighboring columns of height 2, so the totient castles of height 2 are the Fibonacci castles, `F_{w+2} − 1 = A000071(w + 2)` of width `w` with `F_1 = F_2 = 1`, golden by width ([[fibonacci-castle](pages/fibonacci-castle.md)]).[^a000071][^exec1]

**Height 3.** The totient rule on `{1, 2, 3}` allows every pair but `(2, 2)` and `(3, 3)`:

```
        1  2  3
M_3 = [ 1  1  1 ]   1        characteristic polynomial (x + 1)(x² − 2x − 1).
      [ 1  0  1 ]   2
      [ 1  1  0 ]   3
```

The vector `(0, 1, −1)` is its eigenvector for `−1` and is orthogonal to `𝟙`, so `𝟙ᵀ M_3^{w−1} 𝟙` follows the recurrence of `x² − 2x − 1` from the values 3 and 7 at `w = 1, 2`. The 1-smooth rule on `{1, 2, 3}` has the eigenvector `(1, 0, −1)` for its eigenvalue 1, also orthogonal to `𝟙`, and the same two first values, so the two rules have the same number of strips at every width: the Pell-Lucas numbers `A001333(w + 1)` = `3, 7, 17, 41, 99, …` ([[pell-castle-strip](pages/pell-castle-strip.md)]). So the totient castles of height 3 number `A001333(w + 1) − F_{w+2}` and are silver by width, growing like `(1 + √2)^w` ([[metallic-means](pages/metallic-means.md)]).[^a001333][^exec1][^exec2]

**Heights 4 to 8.** The characteristic polynomials of `M_h` and their largest roots, the growth by width of the totient castles of height `h`:[^exec2]

| `h` | characteristic polynomial of `M_h` | growth by width |
|---|---|---|
| 2 | `x² − x − 1` | `1.6180340`, golden |
| 3 | `(x + 1)(x² − 2x − 1)` | `2.4142136`, silver |
| 4 | `x (x³ − x² − 5x − 2)` | `2.9354323` |
| 5 | `x (x + 1)(x³ − 2x² − 7x − 2)` | `3.9172860` |
| 6 | `x (x⁵ − x⁴ − 11x³ − 10x² + 2x + 2)` | `4.1746638` |
| 7 | `x (x + 1)(x⁵ − 2x⁴ − 15x³ − 12x² + 4x + 2)` | `5.2572382` |
| 8 | `x² (x + 1)(x⁵ − 2x⁴ − 19x³ − 17x² + 6x + 3)` | `5.7697533` |

Two heights with the same prime factors, such as 2, 4 and 8, are coprime to the same heights, so their rows of `M_h` are equal and `M_h` loses rank: these are the factors `x` of the table, one repeat (4 with 2) at `h = 4, …, 7` and two (4 and 8 with 2) at `h = 8`.

## The Euler product

**The guess.** A height `b` taken at random from `1, …, h` is divisible by a prime `p` about a fraction `1/p` of the time, independently for different primes. Give the height `b` the weight `v_b = Π_{p | b} x_p` with numbers `x_p` to be chosen. Then for fixed `a` the row sum `Σ_{gcd(a,b)=1} v_b` is about `h` times a product over the primes: a prime `p | a` must not divide `b`, a factor `1 − 1/p`, and a prime `p ∤ a` gives `1 − 1/p` when `p ∤ b` and `x_p/p` when `p | b`. So

```
Σ_{b ≤ h, gcd(a, b) = 1} v_b  ≈  h · Λ · Π_{p | a} (1 − 1/p) / (1 − (1 − x_p)/p),        Λ = Π_p (1 − (1 − x_p)/p),
```

and `v` is an eigenvector exactly when each factor `(1 − 1/p)/(1 − (1 − x_p)/p)` equals `x_p`, that is, when `x_p (p − 1 + x_p) = p − 1`: `x_p` is the positive root of `x² + (p − 1)x − (p − 1)`. At `p = 2` this is `x² + x − 1`, so `x_2 = (√5 − 1)/2 = 1/φ`; at `p = 3`, `x_3 = √3 − 1`. The eigenvalue is `Λh`, with[^exec3]

```
Λ  =  Π_p (1 − (1 − x_p)/p)  =  0.67846225243…
```

The theorem below makes the guess exact to first order.

**Theorem.** For every `ε > 0`, the largest eigenvalue of the coprimality matrix is

```
ρ(M_h)  =  Λ h + O(h^{1/2+ε}).
```

The proof bounds the row sums of `v` uniformly in `a` (Lemma) and then applies the Collatz-Wielandt formula. Two facts about `x_p` are used: `x_p` increases with `p`, since `x_p = 2/(1 + √(1 + 4/(p − 1)))`, so `x_p ≥ x_2 = 1/φ`; and `0 < 1 − x_p ≤ 1/(p − 1)`, since `(p − 1)(1 − x_p) = x_p² ≤ 1`.[^exec3]

**Lemma.** For every `h` and every `a ≤ h`,

```
| Σ_{b ≤ h, gcd(a, b) = 1} v_b  −  Λ h v_a |  ≤  8 · 2^{ω(a)} · √h.
```

*Proof.* *Convolution.* Every `b` has `v_b = Σ_{d | b} g(d)`, since both sides are multiplicative and at a prime power `p^k` the right side is `1 + g(p) = x_p`. For squarefree `d`, `|g(d)| = Π_{p | d} (1 − x_p) ≤ Π_{p | d} 1/(p − 1) ≤ 2^{ω(d)}/d = τ(d)/d ≤ 2/√d`, since the divisors of `d` pair off as `e` and `d/e` with one of them at most `√d`.

*Row sum.* Writing `b = dm`, the condition `gcd(a, b) = 1` becomes `gcd(a, d) = gcd(a, m) = 1`, so

```
Σ_{b ≤ h, gcd(a,b)=1} v_b  =  Σ_{d ≤ h, gcd(a,d)=1} g(d) · #{m ≤ h/d : gcd(a, m) = 1}.
```

By inclusion-exclusion over the prime factors of `a`, `#{m ≤ y : gcd(a, m) = 1} = y φ(a)/a + θ 2^{ω(a)}` with `|θ| ≤ 1`. The term `y φ(a)/a` gives `h (φ(a)/a) Σ_{d ≤ h, gcd(a,d)=1} g(d)/d`, and the term `θ 2^{ω(a)}` adds at most `2^{ω(a)} Σ_{d ≤ h} 2/√d ≤ 4 · 2^{ω(a)} √h`.

*Euler product.* The series `Σ_{gcd(a,d)=1} g(d)/d` converges absolutely and equals `Π_{p ∤ a} (1 + g(p)/p) = Λ / Π_{p | a} (1 − (1 − x_p)/p)`; its terms with `d > h` add up to at most `Σ_{d > h} 2 d^{−3/2} ≤ 4/√h`, which multiplied by `h` is at most `4√h`. Finally `(φ(a)/a) / Π_{p | a} (1 − (1 − x_p)/p) = Π_{p | a} (p − 1)/(p − 1 + x_p) = Π_{p | a} x_p = v_a`, by the defining equation of `x_p`. So the row sum is `Λ h v_a` with an error of at most `4√h + 4 · 2^{ω(a)} √h ≤ 8 · 2^{ω(a)} √h`.[^exec4]

*Proof of the theorem.* `M_h` is a nonnegative symmetric matrix, and `M_h²` has every entry positive, since the height 1 is coprime to every height, so `M_h` is primitive. By the Collatz-Wielandt formula, for the positive vector `v`,[^pf-cw]

```
min_a (M_h v)_a / v_a   ≤   ρ(M_h)   ≤   max_a (M_h v)_a / v_a .
```

By the Lemma and `v_a ≥ x_2^{ω(a)} = φ^{−ω(a)}`, both sides are `Λh` up to at most `8 (2φ)^{ω(a)} √h`. If `a ≤ h` has `k` distinct prime factors then `a` is at least the product of the first `k` primes, so `k! ≤ h`, and since `k! ≥ (k/e)^k` this gives `k = O(log h / log log h)` and `(2φ)^k = h^{o(1)}`. So `ρ(M_h) = Λh + O(h^{1/2+ε})`. ∎

**The totient castles.** Since `M_h` is primitive, its largest eigenvalue is simple and larger in absolute value than every other, and `𝟙ᵀ M_h^{w−1} 𝟙` grows like `ρ(M_h)^w`.[^pf-primitive] The matrix `M_{h−1}` has a smaller largest eigenvalue: with `u` its unit Perron vector, the unit vector `(u, ε)/√(1 + ε²)` has Rayleigh quotient `(ρ(M_{h−1}) + 2ε Σ_{b < h, gcd(b,h)=1} u_b)/(1 + ε²)` for `h ≥ 2`, and the sum contains `u_1 > 0`, so for small `ε > 0` the quotient exceeds `ρ(M_{h−1})`. So the totient castles of height `h` also grow like `ρ(M_h)^w`, about `(0.6785 h)^w` for large `h`.

**Numbers.** The Collatz-Wielandt bounds for `v`, the largest eigenvalue, and the average row sum, each divided by `h`:[^exec5]

| `h` | lower bound | `ρ(M_h)/h` | upper bound | average row sum `/h` |
|---|---|---|---|---|
| 100 | `0.660193` | `0.6764277` | `0.682543` | `0.608700` |
| 400 | `0.674341` | `0.6784558` | `0.681580` | `0.608469` |
| 1600 | `0.676332` | `0.6783748` | `0.679421` | `0.607993` |
| `∞` | `Λ` | `Λ = 0.6784623` | `Λ` | `6/π² = 0.607927` |

The average row sum is the number of coprime pairs divided by `h`, and its share tends to `6/π²`; the largest eigenvalue is larger, `Λ > 6/π²`, because the Perron vector weights the heights with few small prime factors, `v_1 = 1`, `v_2 = 0.618`, `v_6 = 0.452`, and those are coprime to more heights.

## By area

A castle of area `n` is a composition of `n`, its column heights in order ([[castles-of-height-h-by-area](pages/castles-of-height-h-by-area.md)]), so the totient castles of area `n`, of any height, are the compositions of `n` whose neighboring parts are coprime. These are counted by `A167606`, "Number of compositions of n where each pair of adjacent parts is relatively prime":[^a167606][^exec7]

```
A_totient(n)  =  A167606(n)  =  1, 2, 4, 7, 14, 25, 48, 90, 168, 316, 594, 1116, …     (n = 1, 2, 3, …)
```

By Kotesovec's asymptotic in the entry, they grow like `c · d^n` with `d = 1.87801540657…`; the ratio of consecutive counts at `n = 200` agrees with `d` to 13 digits.[^a167606][^exec7] Their signed count `Σ (−1)^blocks` and their even-block count by area are[^exec7]

```
S_totient(n)    =  −1, 0, 0, 1, −2, −3, −8, −6, −12, −6, −22, −20, −56, −47, −108, −79, …
A^e_totient(n)  =   0, 1, 2, 4, 6, 11, 20, 42, 78, 155, 286, 548, 1020, 1944, 3640, 6899, …
```

## The parity

With the sign `(−1)^{max(0, b − a)}` on each allowed step, the signed matrix of the totient rule counts `S_totient(w, h)` ([[castle-sign](pages/castle-sign.md)]). Its spectral radius is smaller than `ρ(M_h)` at every height computed, so at each of these heights the even-block share of the totient castles tends to 1/2:[^exec6]

| `h` | `A^e_totient(w, h)`, `w = 1, …, 10` | signed spectral radius | `ρ(M_h)` |
|---|---|---|---|
| 2 | `1, 2, 3, 4, 6, 10, 17, 28, 45, 72` | `1` | `1.618034` |
| 3 | `0, 0, 3, 14, 39, 100, 259, 652, 1604, 3934` | `1.574743` | `2.414214` |
| 4 | `1, 4, 12, 32, 95, 298, 938, 2898, 8853, 26804` | `√2 = 1.414214` | `2.935432` |
| 5 | `0, 0, 10, 86, 414, 1754, 7418, 30706, 124088, 496964` | `2.198760` | `3.917286` |
| 6 | `1, 4, 18, 72, 315, 1392, 6251, 28000, 125190, 555930` | `1.961087` | `4.174664` |

At height 2 the signed count repeats `1, 2, 2, 1, 0, 0` with period 6, the parity of the Fibonacci castles ([[fibonacci-castle](pages/fibonacci-castle.md)]).

## Related Concepts

- [[castle-strip](pages/castle-strip.md)] - strip rules, their 0/1 transfer matrices and growth constants.
- [[fibonacci-castle](pages/fibonacci-castle.md)] - the totient castles of height 2.
- [[pell-castle-strip](pages/pell-castle-strip.md)] - the 1-smooth strips on `{1, 2, 3}`, as many as the totient strips there.
- [[metallic-means](pages/metallic-means.md)] - the golden and silver means, the growth at heights 2 and 3.
- [[castle-classification-growth](pages/castle-classification-growth.md)] - families of castles by growth constant.
- [[castles-of-height-h-by-area](pages/castles-of-height-h-by-area.md)] - castles of area `n` as compositions of `n`, the reading behind `A167606`.
- [[castle-sign](pages/castle-sign.md)] - the sign `(−1)^blocks` and the signed transfer matrix.
- [[castle-notation](pages/castle-notation.md)] - the symbols of this page.

## Footnotes

[^a001333]: https://oeis.org/A001333 (read 2026-10-28) - "Pell-Lucas numbers: numerators of continued fraction convergents to sqrt(2).", offset 0, data `1, 1, 3, 7, 17, 41, 99, 239, 577, 1393, 3363, 8119`.
[^a000071]: https://oeis.org/A000071 (read 2026-10-28) - "a(n) = Fibonacci(n) - 1.", offset 1, data `0, 0, 1, 2, 4, 7, 12, 20, 33, 54, 88, 143`.
[^a167606]: https://oeis.org/A167606 (read 2026-10-28) - "Number of compositions of n where each pair of adjacent parts is relatively prime.", offset 0, data `1, 1, 2, 4, 7, 14, 25, 48, 90, 168, 316, 594, 1116`; formula "a(n) ~ c * d^n, where d=1.8780154065731862176678940156530410192010138618103068156064519919669849911..., c=0.5795813856338135589080831265343299561832275012313700387790334792220408848... - _Vaclav Kotesovec_, May 01 2014".
[^pf-cw]: https://en.wikipedia.org/wiki/Perron%E2%80%93Frobenius_theorem (read 2026-10-28) §"Collatz–Wielandt formula" - "for all non-negative non-zero vectors x, let f(x) be the minimum value of [Ax]i / xi taken over all those i such that xi ≠ 0. Then f is a real valued function whose maximum over all non-negative non-zero vectors x is the Perron–Frobenius eigenvalue." and "for all strictly positive vectors x, let g(x) be the maximum value of [Ax]i / xi taken over i. Then g is a real valued function whose minimum over all strictly positive vectors x is the Perron–Frobenius eigenvalue."
[^pf-primitive]: https://en.wikipedia.org/wiki/Perron%E2%80%93Frobenius_theorem (read 2026-10-28) - "A real matrix A is primitive if it is non-negative and its mth power is positive for some natural number m", and "If A is a positive (or more generally primitive) matrix, then there exists a real positive eigenvalue r (Perron–Frobenius eigenvalue or Perron root), which is strictly greater in absolute value than all other eigenvalues".
[^exec1]: Verified by execution (Python 3.11, 2026-10-28): `bin/python/totient_castles.py` item [1], run log `bin/python/totient_castles-run.log`. The transfer-matrix counts against brute force for `w ≤ 7`, `h ≤ 6`; height 2 against `F_{w+2} − 1` for `w ≤ 20` and the `A000071` data; at height 3 the strips against the `A001333` data and against the 1-smooth strips, and the castles against `A001333(w + 1) − F_{w+2}`, for `w ≤ 14`.
[^exec2]: Verified by execution (Python 3.11, 2026-10-28, SymPy): `bin/python/totient_castles.py` item [2], run log `bin/python/totient_castles-run.log`. The characteristic polynomials of `M_h` for `h ≤ 8` and their largest roots; the two eigenvectors at height 3.
[^exec3]: Verified by execution (Python 3.11, 2026-10-28, mpmath at 30 digits): `bin/python/totient_castles.py` item [3], run log `bin/python/totient_castles-run.log`. `Λ` as `(6/π²) Π_p (1 − (1 − x_p)/p)/(1 − 1/p²)` over the primes below `10^6`, whose factors are `1 + O(p^{−3})`; `x_2 = 1/φ`, `x_3 = √3 − 1`; the defining equation, the monotonicity of `x_p` and `1 − x_p ≤ 1/(p − 1)` for `p < 1000`.
[^exec4]: Verified by execution (Python 3.11, 2026-10-28): `bin/python/totient_castles.py` item [4], run log `bin/python/totient_castles-run.log`. `v = 1 ∗ g` for `n ≤ 3000`, and the bound of the Lemma for every `a ≤ h` at `h = 50, 100, 200, 400`, where the largest error is 0.006 times the bound.
[^exec5]: Verified by execution (Python 3.11, 2026-10-28): `bin/python/totient_castles.py` item [5], run log `bin/python/totient_castles-run.log`. The Collatz-Wielandt bounds from `v`, and `ρ(M_h)` by power iteration with residual below `10^{−14}`, at `h = 100, 400, 1600`.
[^exec6]: Verified by execution (Python 3.11, 2026-10-28, SymPy): `bin/python/totient_castles.py` item [6], run log `bin/python/totient_castles-run.log`. The signed counts by the signed transfer matrix against brute force for `w ≤ 6`, `h ≤ 5`; the signed characteristic polynomials and their spectral radii for `h ≤ 6`.
[^exec7]: Verified by execution (Python 3.11, 2026-10-28): `bin/python/totient_castles.py` item [7], run log `bin/python/totient_castles-run.log`. The totient castles by area against the `A167606` b-file for `n ≤ 30`, the count and the signed count against brute force over the compositions for `n ≤ 12`, the ratio at `n = 200`, and the strips for `h ≤ 7`, `w ≤ 10`.
