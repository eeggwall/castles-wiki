---
title: Tower recursion master class
category: Concepts
summary: A seminar on the two steps that count castles. First, towers are determined by their column heights, which are chosen independently, so the towers of height at most k on a base of length L number T(k, L) = (k+1)^L. Second, weighting each block by −1 gives the signed tower count P(k, L), and (T ± P)/2 splits the towers into even-block and odd-block ones. A castle has one block more than its towers, so its even-block castles of height h number A^e(w, h) = [h^w − (h−1)^w − P(h−1, w) + P(h−2, w)]/2, worked out at A^e(4, 2) = 10.
tags: [concept, castle, towers, parity, sign, pedagogy, dyck, teaching]
sources: [project-euler-502-solution, project-euler-502-representations, project-euler-502-castle-factoring, project-euler-502-observations]
created: 2026-09-14
updated: 2026-10-25
---

# Tower recursion master class

## The two steps

The count `A^e(w, h)` of the castles of width `w` and height `h` with an even number of blocks, the count Project Euler 502 asks for and writes `F(w, h)`, follows from two facts about towers, the configurations left when the bottom row of a castle is removed ([[castle-notation](pages/castle-notation.md)]):

1. **Towers are their column heights, chosen independently.** So the towers of height at most `k` on a base of length `L` number `T(k, L) = (k+1)^L`.
2. **Parity is a sign.** Weighting each block by `−1` and summing over towers gives the signed tower count `P(k, L)`, and `(T + P)/2` and `(T − P)/2` count the even-block and the odd-block towers.

The section *The castle counts* assembles the two into the formula for `A^e(w, h)`, and the section *Example* works it at `w = 4`, `h = 2`.

## Step 1: towers

Towers on a base of length `L` are given by their column heights `c = (c_1, …, c_L)`, where `c_i ∈ {0, …, k}` is the number of blocks above the base in column `i` ([[castle-representations](pages/castle-representations.md)]). The blocks of each row are the maximal runs of columns that reach it, so the towers are determined by their column heights, and every tuple in `{0, …, k}^L` occurs. The `L` columns choose their heights independently:[^1]

```
T(k, L)  =  (k + 1)^L.
```

The source puts the independence as "Two sibling blocks in the same row generate towers that never interact (the parent-row gap is automatic)."[^2]

**The induction on `k`.** The columns that carry a block in the first row above the base form a binary string `b` of length `L`, 1 for a block and 0 for a gap, and each maximal run of 1s is one block ([[binary-string-bijection](pages/binary-string-bijection.md)]).[^3] On a block of length `l` stand towers of height at most `k − 1`, independently of the other blocks. With `ones(b)` the number of 1s in `b` and `T(k − 1, l) = k^l` by induction,[^4]

```
T(k, L)  =  Σ_{b ∈ {0,1}^L}  Π_{runs of 1s in b, of length l}  T(k−1, l)
         =  Σ_{b}  k^{ones(b)}
         =  Σ_{j=0}^{L} C(L, j) k^j
         =  (k + 1)^L.
```

With `k = h − 1`, the castles of width `w` and height at most `h` number `T(h − 1, w) = h^w`.

## Step 2: parity as a sign

Weight each block by `−1`. The sign of towers with column heights `c` is `(−1)^{blocks(c)}`, with `blocks(c) = Σ_{i=1}^{L} max(0, c_i − c_{i−1})` and `c_0 = 0` ([[castle-sign](pages/castle-sign.md)]); the source writes it `s(C)` and sets it beside the sign `(−1)^{n−c}` of a permutation of `n` points with `c` cycles.[^5] The signed tower count is

```
P(k, L)  =  Σ_{c ∈ {0, …, k}^L}  (−1)^{blocks(c)},
```

and since `(1 + (−1)^b)/2` is 1 for even `b` and 0 for odd `b`,[^6]

```
(T(k, L) + P(k, L)) / 2  =  even-block towers,        (T(k, L) − P(k, L)) / 2  =  odd-block towers.
```

In the tower grammar of [[generalized-dyck-grammar](pages/generalized-dyck-grammar.md)], a block is a production `U V D` carrying the towers `V`, so it contributes `−1` times the weight of `V`, and the generating function `P_k(x) = Σ_L P(k, L) x^L` satisfies[^7]

```
P_k(x)  =  1 + x·P_k(x) − (P_{k−1}(x) − 1)(1 + x·P_k(x)),        P_0(x) = 1/(1 − x).
```

[[castle-counting-formula](pages/castle-counting-formula.md)] solves it as a rational function, and [[signed-tower-count](pages/signed-tower-count.md)] studies the sequences `P(k, ·)`. With a block weight `y` in place of `−1`, the same reading makes the step from height `k − 1` to `k` one 2 × 2 matrix, whose cases `y = 1` and `y = −1` give `E_k(x)` and `P_k(x)` ([[generalized-dyck-grammar](pages/generalized-dyck-grammar.md)], section *Counts*).

## The castle counts

A castle has one block more than its towers, the bottom row, so it has an even number of blocks exactly when its towers have an odd number.[^8] The castles of height `h` are those of height at most `h` minus those of height at most `h − 1`, so the even-block castles of width `w` and height `h` number

```
A^e(w, h)  =  [T(h−1, w) − P(h−1, w)]/2 − [T(h−2, w) − P(h−2, w)]/2
           =  [ h^w − (h−1)^w − P(h−1, w) + P(h−2, w) ] / 2,
```

and the odd-block ones

```
A^o(w, h)  =  [ h^w − (h−1)^w + P(h−1, w) − P(h−2, w) ] / 2.
```

The two differ only in the sign of the `P` terms, and their sum is the number of all castles of width `w` and height `h`, `A(w, h) = h^w − (h−1)^w`.[^9] In the notation of [[castle-notation](pages/castle-notation.md)], `A^e = (A + S)/2` and `A^o = (A − S)/2` with the signed count `S(w, h) = P(h−2, w) − P(h−1, w)`.

## Example: `A^e(4, 2) = 10`

The towers of height at most 1 on a base of length 4 are the 16 binary strings of length 4. The string `0000` stands under the flat castle `(1, 1, 1, 1)`, of height 1, so the castles of width 4 and height 2 are the other 15, `A(4, 2) = 2^4 − 1^4 = 15`. With `P(0, 4) = 1` and `P(1, 4) = Re((1+i)^5) = −4`,

```
S(4, 2)  =  P(0, 4) − P(1, 4)  =  1 + 4  =  5,
A^e(4, 2)  =  (15 + 5)/2  =  10,        A^o(4, 2)  =  (15 − 5)/2  =  5.
```

The ten even-block castles stand on the strings with one run of 1s, and the five odd-block castles `(2, 1, 2, 1)`, `(1, 2, 1, 2)`, `(2, 1, 1, 2)`, `(2, 2, 1, 2)` and `(2, 1, 2, 2)` on the strings with two runs.[^10] The value `P(1, 4) = −4` can also be counted: the involution of [[signed-tower-count](pages/signed-tower-count.md)] (section *The case k = 1*) pairs off twelve of the sixteen strings with opposite signs and leaves `0100`, `0110`, `1100` and `1110`, each with one run. The value `A^e(4, 2) = 10` is the first checkpoint of the problem statement ([[castle-counting-function](pages/castle-counting-function.md)]).

## Appearances in Sources

- [[project-euler-502-solution](pages/project-euler-502-solution.md)] - the binary-string bijection, the induction proof of `T(k, L) = (k+1)^L`, and the split `(T ± P)/2` of towers.
- [[project-euler-502-representations](pages/project-euler-502-representations.md)] - the signed generating function `P_k(x)` and the formula for `A^e(w, h)`.
- [[project-euler-502-castle-factoring](pages/project-euler-502-castle-factoring.md)] - the column-height proof of `T(k, L) = (k+1)^L` and the sign `s(C)`.
- [[project-euler-502-observations](pages/project-euler-502-observations.md)] - the independence of towers on different blocks, and `A(w, h) = h^w − (h−1)^w`.

## Related Concepts

- [[castle-counting-formula](pages/castle-counting-formula.md)] - the derivation of `A^e(w, h)` with proofs and checks.
- [[castle-sign](pages/castle-sign.md)] - the sign `(−1)^{blocks}` and the even/odd splits of towers and castles.
- [[signed-tower-count](pages/signed-tower-count.md)] - the sequences `P(k, ·)` and their recurrences.
- [[binary-string-bijection](pages/binary-string-bijection.md)] - the first-row binary strings of the induction.
- [[generalized-dyck-grammar](pages/generalized-dyck-grammar.md)] - the tower grammar behind `E_k(x)` and `P_k(x)`.
- [[parity-via-roots-of-unity](pages/parity-via-roots-of-unity.md)] - the split by block count modulo `m`.
- [[tower-parity-sectors](pages/tower-parity-sectors.md)] - the split of `P` by the parity of the last column, from a symmetry of the signed transfer matrix.
- [[tower-word-continued-fraction](pages/tower-word-continued-fraction.md)] - the tower words as Motzkin paths with no `UD` and no `DU`, and `1/E_k(x) = 1 − (k+1)x` in reciprocal form.
- [[tower-heap](pages/tower-heap.md)] - towers counted by their blocks, through Narayana polynomials.
- [[castle-foata-transform](pages/castle-foata-transform.md)] - the peaks of towers, the maximal runs of positive columns, and their first columns.
- [[castle-notation](pages/castle-notation.md)] - the symbols `T`, `P`, `A`, `A^e`, `A^o`, `S` and the tower height `k = h − 1`.
- The other seminars: [[one-bit-seminar](pages/one-bit-seminar.md)] (the even-block condition as information), [[hardin-identity-seminar](pages/hardin-identity-seminar.md)] (the even sector of the signed tower count), [[castle-fibers-char-2-walkthrough](pages/castle-fibers-char-2-walkthrough.md)] (a castle recurrence modulo primes), [[hear-the-shape-seminar](pages/hear-the-shape-seminar.md)] (spectra of castle graphs), [[oeis-mining-seminar](pages/oeis-mining-seminar.md)] (searching the OEIS for castle counts), [[q-thread-seminar](pages/q-thread-seminar.md)] (castles by area), [[sandcastle-seminar](pages/sandcastle-seminar.md)] (the sandpile on the castle `(3, 2, 1, 2, 2, 1, 2, 3)`), [[pell-castle-strip](pages/pell-castle-strip.md)] (the strips counted by the Pell numbers), [[castle-cryptography](pages/castle-cryptography.md)] and [[song-as-castle](pages/song-as-castle.md)].

## Footnotes

[^1]: [[project-euler-502-castle-factoring](pages/project-euler-502-castle-factoring.md)] §"A column-height factorization" L72, L88 - "Let c_1 … c_L be the column heights of a tower above a length-L base: c_i is the number of blocks covering column i. Then each c_i ranges independently over {0, …, k}", and "each of the L columns independently chooses one of k+1 heights. This is the product-form proof of the (k+1)^L formula".
[^2]: [[project-euler-502-observations](pages/project-euler-502-observations.md)] §"Sub-block independence" L5 - "Two sibling blocks in the same row generate towers that never interact (the parent-row gap is automatic)."
[^3]: [[project-euler-502-solution](pages/project-euler-502-solution.md)] §"The binary-string bijection" L14-19 - "Configurations within a block of length L (non-overlapping, non-adjacent integer-length sub-blocks, including the empty config) biject with binary strings of length L: map each string to the configuration whose sub-blocks are its maximal runs of 1s", "If a binary string has r maximal runs of 1s, the corresponding configuration has r sub-blocks."
[^4]: [[project-euler-502-solution](pages/project-euler-502-solution.md)] §"T(k, L) = (k+1)^L" L23-37 - "a length-L binary string ... plus, for each maximal run of length l, an independent tower of height ≤ k-1 above that sub-block", "T(k, L) = ∑_b ∏_{runs} T(k-1, l) = ∑_b k^{ones(b)} = (1 + k)^L", "Corollary: the total number of castles with bottom block w and height ≤ h (any parity) is T(h-1, w) = h^w."
[^5]: [[project-euler-502-castle-factoring](pages/project-euler-502-castle-factoring.md)] §"The sign of a castle" L92-101 - "sgn(σ) = (-1)^{n - c} ... Each block is an excursion atom (a U ... D pair), and each D move completes one block. Weight each block by -1 and define s(C) = (-1)^{blocks(C)}."
[^6]: [[project-euler-502-solution](pages/project-euler-502-solution.md)] §"The main formula" L55 - "Then (T + P)/2 counts towers with even block count and (T - P)/2 counts odd."
[^7]: [[project-euler-502-representations](pages/project-euler-502-representations.md)] §"Signed count" L316-327 - "Weight each block, that is each D, by -1 ... with one minus sign on the peak", "P_k = 1 + x P_k - (P_{k-1} - 1)(1 + x P_k)".
[^8]: [[project-euler-502-representations](pages/project-euler-502-representations.md)] §"The main formula" L350 - "The full castle is U (tower) D, so its block count is the tower's block count plus one for the bottom block. Even total blocks means an odd number of blocks in the tower."
[^9]: [[project-euler-502-observations](pages/project-euler-502-observations.md)] §"The \"even number of blocks\" clause is almost the entire difficulty" L17 - "Without it, the answer is just h^w - (h-1)^w: all castles of height at most h minus those of height at most h-1."
[^10]: Verified by execution (Python 3.11, 2026-10-16): the 16 strings of length 4 by number of runs of 1s (one string with none, ten with one, five with two); `P(1, 4) = −4`; `A^e(4, 2) = 10` and `A^o(4, 2) = 5` by enumeration of all castles of width 4 and height 2.
