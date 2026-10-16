---
title: Generalizing the parity sign (roots of unity)
category: Concepts
summary: Counting towers or castles by block count modulo m. With ω = e^{2πi/m} and P_j(k, L) = Σ ω^{j·blocks} over the towers of height at most k on a base of length L, the towers with blocks ≡ r (mod m) number (1/m) Σ_j ω^{−jr} P_j(k, L), and the castles of width w and height h with blocks ≡ r number (1/m) Σ_j ω^{−j(r−1)} [P_j(h−1, w) − P_j(h−2, w)]; m = 2 gives (T ± P)/2 and (A ± S)/2. P_j has the generating-function recurrence of P with the block weight ω^j, and P_j(1, L) = Σ_r C(L+1, 2r) ω^{jr}. The substitution x → −x selects even indices instead of even block counts.
tags: [concept, castle, parity, roots-of-unity, character, pedagogy]
sources: [project-euler-502-solution, project-euler-502-representations]
created: 2026-09-14
updated: 2026-10-16
---

# Generalizing the parity sign (roots of unity)

The [[castle-sign](pages/castle-sign.md)] counts the even-block towers and castles with the sign `(−1)^{blocks}`. Replacing `−1` by an `m`-th root of unity counts them by block count modulo `m`: the condition "blocks divisible by 3", "blocks ≡ 3 (mod 4)" or "blocks not divisible by 4" is decided by `m` weighted sums over the towers.

## The case m = 2

Over the towers of height at most `k` on a base of length `L`, `T(k, L)` counts them and `P(k, L)` adds up `(−1)^{blocks}`. Since `(1 + (−1)^b)/2` is 1 for even `b` and 0 for odd `b`,[^1]

```
even-block towers  =  ( T(k, L) + P(k, L) ) / 2,        odd-block towers  =  ( T(k, L) − P(k, L) ) / 2.
```

A castle has one block more than its towers, so over the castles of width `w` and height `h` the split is `A^e = (A + S)/2` and `A^o = (A − S)/2`, with `S(w, h) = P(h−2, w) − P(h−1, w)` ([[castle-counting-formula](pages/castle-counting-formula.md)], Equation (7)).

## Roots of unity

A **character** of the cyclic group `Z/m` is a homomorphism to the complex numbers of modulus 1; the characters are `b ↦ ω^{jb}` for `j = 0, 1, …, m − 1`, with `ω = e^{2πi/m}`. They satisfy the orthogonality relation

```
(1/m) Σ_{j=0}^{m−1} ω^{j(b−r)}  =  1  if  b ≡ r (mod m),   0  otherwise,
```

because for `b − r` not divisible by `m` the sum is a geometric series of `m` terms with ratio `ω^{b−r} ≠ 1` and sum 0. Weighting each block by `ω^j` gives

```
P_j(k, L)  =  Σ ω^{j·blocks(c)}  over the towers c of height at most k on a base of length L,        j = 0, 1, …, m − 1.      (1)
```

`P_0 = T`, and at `m = 2`, `P_1 = P` ([[castle-notation](pages/castle-notation.md)]). Summing the orthogonality relation over the towers gives

```
# { towers with blocks ≡ r (mod m) }  =  (1/m) Σ_{j=0}^{m−1} ω^{−jr} P_j(k, L).        (2)
```

For castles, a castle with skyline `c` has `blocks(c) ≡ r` exactly when its towers have `blocks ≡ r − 1`, and the castles of height `h` are those of height at most `h` minus those of height at most `h − 1`. So the castles of width `w` and height `h` with `blocks ≡ r (mod m)` number

```
(1/m) Σ_{j=0}^{m−1} ω^{−j(r−1)} [ P_j(h−1, w) − P_j(h−2, w) ].        (3)
```

At `m = 2` and `r = 0`, the term `j = 0` is `A(w, h)` and the term `j = 1` is `S(w, h)`, so Equation (3) is `A^e = (A + S)/2`.[^2]

## Computing P_j

Write `P_{j,k}(x) = Σ_L P_j(k, L) x^L`, and `t = ω^j` for the weight of one block. In the tower grammar `E_k → empty | R E_k | U V D (empty | R E_k)`, the production `U V D` is one block, so it multiplies the weight of the towers `V` by `t` ([[generalized-dyck-grammar](pages/generalized-dyck-grammar.md)]). The reading of Equation (2) of [[castle-counting-formula](pages/castle-counting-formula.md)] then gives `P_{j,k} = 1 + x·P_{j,k} + t(P_{j,k−1} − 1)(1 + x·P_{j,k})`, so[^3]

```
P_{j,k}(x)  =  (1 − t + t·P_{j,k−1}(x)) / (1 − x(1 − t) − t·x·P_{j,k−1}(x)),        P_{j,0}(x)  =  1/(1 − x).        (4)
```

At `t = 1` this is `E_k(x) = E_{k−1}(x)/(1 − x·E_{k−1}(x))`, and at `t = −1` it is `P_k(x) = (2 − P_{k−1}(x))/(1 − 2x + x·P_{k−1}(x))`.

*The case `k = 1`.* Towers of height at most 1 are binary strings, and their blocks are the runs of 1s. The strings of length `L` with `r` runs number `C(L+1, 2r)`, one for each choice of the `2r` run ends among the `L + 1` gaps between and around the columns. With `s` either square root of `ω^j`,

```
P_j(1, L)  =  Σ_r C(L+1, 2r) ω^{jr}  =  [ (1 + s)^{L+1} + (1 − s)^{L+1} ] / 2.
```

At `m = 2` and `j = 1`, `s = i` and this is `Re((1+i)^{L+1}) = P(1, L)` ([[signed-tower-count](pages/signed-tower-count.md)]).

## Examples

- **Divisible by `m`** (`r = 0`): `(1/m) Σ_j P_j`. **Congruent to `r`**: Equation (2). **Not divisible by `m`**: `T` minus the count divisible by `m`.
- **Not divisible by 4.** At `m = 4`, `ω = i`, so `P_2 = P` and `P_3` is the complex conjugate of `P_1`, and the towers with block count not divisible by 4 number

  ```
  T − (T + P_1 + P_2 + P_3)/4  =  (3T − P − 2 Re P_1)/4.
  ```

  At `k = 1`, `L = 4`, all strings but `0000` have 1 or 2 blocks, and the formula gives 15.
- **Divisible by 3, at `k = 1`, `L = 4`.** The 16 binary strings have 0, 1 or 2 runs, in `C(5, 0) = 1`, `C(5, 2) = 10` and `C(5, 4) = 5` strings, so one string, `0000`, has a block count divisible by 3. With `ω = e^{2πi/3}`, `P_0 = 16`, `P_1 = 1 + 10ω + 5ω²` and `P_2 = 1 + 10ω² + 5ω`, so `(P_0 + P_1 + P_2)/3 = (18 + 15(ω + ω²))/3 = 1`, since `ω + ω² = −1`.

These values agree with enumeration, and Equation (3) agrees with enumeration of all castles for `m ≤ 5`, `h ≤ 4` and `w ≤ 5` (`w ≤ 4` at `h = 4`).[^4]

## Conditions that are not congruences

A sum of characters of `Z/m` depends only on `blocks mod m`, so it can only count a union of residue classes modulo `m`. "The block count is a power of 2" is not such a union for any `m`: for `2^a > m`, the numbers `2^a` and `2^a + m` lie in the same class, and `2^a < 2^a + m < 2^{a+1}`, so `2^a + m` is not a power of 2. Such sets are counted by a dot product with their indicator series instead ([[block-count-constraints](pages/block-count-constraints.md)]).

## Even indices

The substitution `x → −x` applies `(−1)^n` to the index `n` of a power series `A(x) = Σ_n a_n x^n`, ordinary or exponential:

```
( A(x) + A(−x) )/2  =  Σ_{n even} a_n x^n,        ( A(x) − A(−x) )/2  =  Σ_{n odd} a_n x^n,
```

and `(1/m) Σ_j A(ω^j x)` keeps the indices divisible by `m`. In the generating function `Σ_L P(k, L) x^L` the index is the base length `L`, so `x → −x` selects even widths, not even block counts; the block weight `t = −1` of Equation (4) selects by blocks. [[generating-functions-topic](pages/generating-functions-topic.md)] counts the ternary strings with an even number of 0s with `(e^x + e^{−x})/2`, the exponential generating function of the 0s, whose index is the number of 0s.

| selects by | how | `m = 2` |
|---|---|---|
| the index `n` | `A(x) → (1/m) Σ_j A(ω^j x)` | `(A(x) + A(−x))/2` |
| the block count | a weight `ω^j` per block, Equation (2) | `(T + P)/2` for towers, `(A + S)/2` for castles |

## Appearances in Sources

- [[project-euler-502-solution](pages/project-euler-502-solution.md)] - the split of towers into `(T + P)/2` even-block and `(T − P)/2` odd-block ones.
- [[project-euler-502-representations](pages/project-euler-502-representations.md)] - the grammar derivation of `P_k(x)`, with the factor `−1` on the block production that `ω^j` replaces.

## Related Concepts

- [[castle-sign](pages/castle-sign.md)] - the case `m = 2`, for towers and for castles.
- [[signed-tower-count](pages/signed-tower-count.md)] - the row values, recurrences and closed forms of `P(k, L) = P_1(k, L)` at `m = 2`.
- [[castle-notation](pages/castle-notation.md)] - the symbols `T`, `P`, `P_j`, `A`, `S`.
- [[castle-sign-kms-matrix](pages/castle-sign-kms-matrix.md)] - the transfer matrix with a weight `t` per block, diagonally similar to the Kac-Murdock-Szegő matrix `(ρ^{|a−b|})` with `ρ = √t`; `t = ω^j` gives `P_j`.
- [[block-count-constraints](pages/block-count-constraints.md)] - block counts in residue classes, in sets given by a lacunary series, and in numerical semigroups.
- [[generating-functions-topic](pages/generating-functions-topic.md)] - the exponential generating function `(e^x + e^{−x})/2` of the even numbers of 0s.
- [[tower-recursion-master-class](pages/tower-recursion-master-class.md)] - a seminar on the tower count and the sign.
- [[one-bit-seminar](pages/one-bit-seminar.md)] - the case `m = 2` as one bit of information.
- [[idempotent-decomposition](pages/idempotent-decomposition.md)] - idempotents of the ring `F_p[x]/(char_k)`, which project the recurrence of `P(k, ·)` onto one eigenvalue sector.

## Footnotes

[^1]: [[project-euler-502-solution](pages/project-euler-502-solution.md)] §"The main formula" L55 - "Then (T + P)/2 counts towers with even block count and (T - P)/2 counts odd."
[^2]: [[project-euler-502-solution](pages/project-euler-502-solution.md)] §"The main formula" L57 - "The bottom block contributes 1 block, so \"castle has even total blocks\" is the same as \"tower above the bottom has odd block count\"."
[^3]: [[project-euler-502-representations](pages/project-euler-502-representations.md)] §"Signed count" L316-327 - "Weight each block, that is each D, by -1 ... with one minus sign on the peak", "P_k = 1 + x P_k - (P_{k-1} - 1)(1 + x P_k)"; the weight `−1` is replaced by `t = ω^j`.
[^4]: Verified by execution (Python 3.11 with SymPy, 2026-10-16): Equation (4) against the sums of Equation (1) over all towers for `m = 3, 4`, `k ≤ 3`, `L ≤ 5`; the `k = 1` closed form for `m = 3, 4, 5`, `L ≤ 6`; both examples; Equation (3) against enumeration of all castles for `m = 2, …, 5`, `2 ≤ h ≤ 4`, `w ≤ 5` (`w ≤ 4` at `h = 4`), every `r`.
