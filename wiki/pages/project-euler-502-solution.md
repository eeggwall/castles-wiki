---
title: "PE 502: Solution"
category: Sources
summary: The Solution subpage proves T(k, L) = (k+1)^L by induction on k through the binary-string bijection, derives A^e(w, h) = [h^w − (h−1)^w − P(h−1, w) + P(h−2, w)]/2 (the count it writes F(w, h)), gives the run-product recursion for the signed tower count P(k, L) and P(1, L) = Re((1+i)^{L+1}), and routes the three Project Euler targets through a rational-function path for h ≤ 15000 and a Berlekamp-Massey path in the tower height for h > 15000. It lists four approaches that did not work and three reference files.
tags: [project-euler, castle, solution, generating-functions, algorithms, source, subpage]
sources: [project-euler-502-solution]
created: 2026-09-13
updated: 2026-10-16
---

# Project Euler 502 (PE 502): Solution

**Source:** https://charlesreid1.com/wiki/Project_Euler/502/Solution
**Date ingested:** 2026-09-13
**Type:** article (MediaWiki subpage of [[project-euler-502](pages/project-euler-502.md)])

## Summary

This subpage gives the mathematical solution: notation, the tower count, the formula for the even-block count, the recursion for the signed tower count, and the computation of the three Project Euler targets. Its notation is the wiki's, except that it writes `F(w, h)` for the even-block count `A^e(w, h)` and calls a castle of height `h` one of "height exactly `h`".[^1]

## Key Takeaways

- **Notation.** `A(w, h)` counts the castles of width `w` and height `h`, and `F(w, h)` those with an even number of blocks. The bottom row is one block of length `w`, and "everything else is a 'tower'": `T(k, L)` counts the towers of height at most `k` above a block of length `L`, and `P(k, L)` adds up `(−1)^{blocks}` over them.[^1]
- **The binary-string bijection.** The configurations of blocks in the row above a block of length `L`, with no two blocks overlapping or touching, correspond to the binary strings of length `L`: the blocks are the maximal runs of 1s. So there are `2^L` configurations, and a string with `r` runs of 1s gives `r` blocks ([[binary-string-bijection](pages/binary-string-bijection.md)]).[^2]
- **`T(k, L) = (k+1)^L`, by induction on `k`.** `T(0, L) = 1`, the empty tower. Towers of height at most `k` are a binary string `b` of length `L` for the first row, and on each run of 1s, of length `l`, towers of height at most `k − 1` chosen independently of the other runs. With `ones(b)` the number of 1s in `b`,[^3]

  ```
  T(k, L)  =  Σ_{b ∈ {0,1}^L}  Π_{runs of 1s in b, of length l}  T(k−1, l)  =  Σ_b k^{ones(b)}  =  (k+1)^L.
  ```

  So the castles of width `w` and height at most `h` number `T(h−1, w) = h^w`; at `w = 4`, `h = 2` that is 16.
- **The formula.** Castles of height `h` are those of height at most `h` minus those of height at most `h − 1`, so `A(w, h) = h^w − (h−1)^w`. Among the towers counted by `T(k, L)`, the even-block ones number `(T + P)/2` and the odd-block ones `(T − P)/2`. The bottom row is one block, so a castle has an even number of blocks exactly when its towers have an odd number, and the even-block castles of width `w` and height at most `h` number `(h^w − P(h−1, w))/2`. Subtracting the same count at `h − 1` gives[^4]

  ```
  A^e(w, h)  =  [ h^w − (h−1)^w − P(h−1, w) + P(h−2, w) ] / 2.
  ```

  The source checks `A^e(4, 2) = (16 − 1 + 4 + 1)/2 = 10` from `P(0, 4) = 1` and `P(1, 4) = −4`.[^5]
- **The recursion for `P`.** By the same bijection, with `runs(b)` the number of runs of 1s in `b`,[^6]

  ```
  P(k, L)  =  Σ_{b ∈ {0,1}^L}  (−1)^{runs(b)}  Π_{runs of 1s in b, of length l}  P(k−1, l),        P(0, L)  =  1.
  ```

  For fixed `k`, `P(k, ·)` satisfies a linear recurrence in `L` of order `k + 1` ([[castle-counting-formula](pages/castle-counting-formula.md)], the Proposition in the section *Signed tower count*). For fixed `L`, `P(·, L)` satisfies a linear recurrence in `k`, of order `2L − 2` for `4 ≤ L ≤ 12` ([[signed-tower-k-direction](pages/signed-tower-k-direction.md)], [[recurrence-discovery](pages/recurrence-discovery.md)]). The source evaluates the first by Kitamasa's method and the second, after Berlekamp-Massey has found it, by the same method.[^6]
- **The case `k = 1`.** Towers of height at most 1 are binary strings, and their blocks are the runs of 1s. Splitting the strings by the last bit, appending a 1 starts a new run exactly when the last bit is 0, so one more column multiplies the pair of signed sums by the matrix `[[1, 1], [−1, 1]]`, whose eigenvalues are `1 ± i`. This gives `P(1, L) = Re((1+i)^{L+1})`. At `L = 4`, `(1+i)^5 = −4 − 4i`, so `P(1, 4) = −4`, and directly, of the 16 strings of length 4, 6 have an even number of runs and 10 an odd number ([[signed-tower-count](pages/signed-tower-count.md)]).[^7]
- **Two small cases.** `P(k, 2) = (−1)^k (k+1)` and `P(k, 3) = (−1)^k (k+1)²`, which as sequences in `k` satisfy the recurrences with characteristic polynomials `(λ + 1)²` and `(λ + 1)³`.[^8]

## Computing the targets

The target is `A^e(10^12, 100) + A^e(10000, 10000) + A^e(100, 10^12)` modulo `10^9 + 7` ([[castle-count-algorithms](pages/castle-count-algorithms.md)]). The source uses three paths.[^9]

- **The rational-function path, `h ≤ 15000`.** Run the update of `num_k` and `den_k` to `k = h − 1` (the source writes `F_k(x)` for `P_k(x)`), and extract the coefficient of `x^w` from `num_k/den_k`. With `D = h` the degree of `den_{h−1}`, the coefficient comes from the power series in `O(w·D)` operations, or by Kitamasa's method ([[kitamasa](pages/kitamasa.md)]), which reduces `x^w` modulo the characteristic polynomial, in `O(D² log w)`. The source uses the power series when `w ≤ D + 1` or `w·min(w, D) < 50D²`. So `A^e(10000, 10000)` takes the power series and `A^e(10^12, 100)` Kitamasa's method.
- **The Berlekamp-Massey path, `h > 15000`.** For fixed `w`, compute `P(0, w), …, P(N − 1, w)` modulo `p` for `N = 4(w + 2) + 20`, find the shortest linear recurrence in `k` with [[berlekamp-massey](pages/berlekamp-massey.md)], and reach `k = h − 2` and `k = h − 1` in one pass of Kitamasa's method. `A^e(100, 10^12)` takes this path, with `N = 428`.
- **The exact path.** For small `w` and `h`, the same update runs over the integers, as long as `h^w` fits in a 64-bit integer. It gives the checkpoints `A^e(13, 10) = 3 729 050 610 636` and `A^e(10, 13) = 37 959 702 514`.

The source checks `A^e(100, 100) ≡ 841 913 936 (mod 10^9 + 7)` on the modular path, `A^e + A^o = h^w − (h−1)^w` for small `w` and `h`, and `T(k, L) = (k+1)^L` for `k, L ≤ 5` by brute force.[^10] It records the value of the target only as a base64 checksum at the end of its References section; the wiki does not reproduce it.

## What did not work

The source lists four approaches that failed:[^11]

| approach | reason given in the source |
|---|---|
| direct enumeration of castles | `A^e(13, 10)` is about `4 × 10^12` |
| column-wise binary strings without the independence of towers on different blocks | "no way to count without independence" |
| enumeration of the variations of convex castles in the step encoding ([[convex-castle](pages/convex-castle.md)]) | the case analysis "never resolved into a formula" |
| the transfer matrix in the `L` direction as the main method | a matrix power costs `O(D³ log w)`, against `O(D² log w)` for Kitamasa's method |

## References (from the source)

The source lists three uploaded files, the Java program, and the Implementation Notes subpage ([[project-euler-502-implementation-notes](pages/project-euler-502-implementation-notes.md)]).[^12] Each file has its own source page:

- "step polyominoes, motzkin numbers, and bessel functions" (`PolyominosMotzkinBessel.pdf`): Barcucci, Del Lungo, Fédou and Pinzani, *Steep polyominoes, q-Motzkin numbers and q-Bessel functions* ([[steep-polyominoes-q-motzkin-bessel](pages/steep-polyominoes-q-motzkin-bessel.md)]).
- "a method for the enumeration of classes of column-convex polygons" (`EnumerationColumnConvexPolynomials.pdf`): Bousquet-Mélou, *A method for the enumeration of various classes of column-convex polygons* ([[column-convex-polygon-enumeration](pages/column-convex-polygon-enumeration.md)]).
- "construction procedure for parallel polyomino transfer matrices" (`PolyominoTransferMatrix.pdf`): the file is Hickerson, *Counting Horizontally Convex Polyominoes* ([[counting-horizontally-convex-polyominoes](pages/counting-horizontally-convex-polyominoes.md)]).

## Entities & Concepts

- [[binary-string-bijection](pages/binary-string-bijection.md)] - the correspondence between the blocks in the row above a block of length `L` and the binary strings of length `L`.
- [[castle-counting-formula](pages/castle-counting-formula.md)] - three proofs of `T(k, L) = (k+1)^L`, the formula for `A^e(w, h)`, and the degree of `den_k`.
- [[signed-tower-count](pages/signed-tower-count.md)] - `P(k, L)`: values, characteristic polynomials, and the case `k = 1`.
- [[signed-tower-k-direction](pages/signed-tower-k-direction.md)] - the recurrence of `P(·, L)` in `k`.
- [[castle-count-algorithms](pages/castle-count-algorithms.md)] - the computational paths and the route of each target.
- [[kitamasa](pages/kitamasa.md)], [[berlekamp-massey](pages/berlekamp-massey.md)] - the two linear-recurrence algorithms.
- [[castle-sign](pages/castle-sign.md)] - the split `(T ± P)/2` of towers by the parity of the block count.
- [[castle-counting-function](pages/castle-counting-function.md)] - the counts `A`, `A^e`, `A^o`, the checkpoints and the target.

Also linked from the source: [[polyominoes](pages/polyominoes.md)], [[dyck-words](pages/dyck-words.md)], [[lattice-paths](pages/lattice-paths.md)], [[generating-functions-topic](pages/generating-functions-topic.md)].

## Relation to Other Wiki Pages

[[castle-counting-formula](pages/castle-counting-formula.md)] gives the induction proof of `T(k, L) = (k+1)^L` from this subpage next to the grammar proof of [[project-euler-502-representations](pages/project-euler-502-representations.md)] and the column-height proof of [[project-euler-502-castle-factoring](pages/project-euler-502-castle-factoring.md)]. [[castle-count-algorithms](pages/castle-count-algorithms.md)] and [[project-euler-502-implementation-notes](pages/project-euler-502-implementation-notes.md)] describe the computation in more detail.

## Footnotes

[^1]: [[project-euler-502-solution](pages/project-euler-502-solution.md)] §"Notation" L5-10 - "A(w, h) - number of castles with bottom block of length w and height exactly h. F(w, h) - A(w, h) restricted to even total block count. This is what the problem asks for. T(k, L) - number of towers of height at most k stacked above (not counting) a single block of length L. P(k, L) - the signed version of T: sum over the same towers of (-1)^{blocks in tower}." and "the bottom row is always one block of length w (Rule 4). Everything else is a \"tower\"."
[^2]: [[project-euler-502-solution](pages/project-euler-502-solution.md)] §"The binary-string bijection" L14-19 - "Configurations within a block of length L (non-overlapping, non-adjacent integer-length sub-blocks, including the empty config) biject with binary strings of length L: map each string to the configuration whose sub-blocks are its maximal runs of 1s", "The number of configurations in a length-L block is 2^L", "If a binary string has r maximal runs of 1s, the corresponding configuration has r sub-blocks."
[^3]: [[project-euler-502-solution](pages/project-euler-502-solution.md)] §"T(k, L) = (k+1)^L" L23-37 - "Base: T(0, L) = 1 (only the empty tower)", "Two sibling blocks in the same row generate towers that never interact", "T(k, L) = ∑_b ∏_{runs} T(k-1, l) = ∑_b k^{ones(b)} = (1 + k)^L", "Corollary: the total number of castles with bottom block w and height ≤ h (any parity) is T(h-1, w) = h^w. Verify on w=4, h=2: 2^4 = 16."
[^4]: [[project-euler-502-solution](pages/project-euler-502-solution.md)] §"The main formula" L43-67 - "#castles(w, h exact, any parity) = h^w - (h-1)^w", "(T + P)/2 counts towers with even block count and (T - P)/2 counts odd", "\"castle has even total blocks\" is the same as \"tower above the bottom has odd block count\"", "F(w, h) = (h^w - (h-1)^w - P(h-1, w) + P(h-2, w))/2".
[^5]: [[project-euler-502-solution](pages/project-euler-502-solution.md)] §"Verification" L173-177 - "P(0, 4) = 1 (the empty tower) and P(1, 4) = -4 (derived above), so F(4, 2) = (2^4 - 1^4 - P(1, 4) + P(0, 4))/2 = (16 - 1 - (-4) + 1)/2 = 20/2 = 10".
[^6]: [[project-euler-502-solution](pages/project-euler-502-solution.md)] §"Recursion for P(k, L)" L75-84 [synthesis] - the run-product recursion with base "P(0, L) = 1", a linear recurrence in `L` for fixed `k` "evaluable in O(k^2 log L)", and a linear recurrence in `k` for fixed `L`, computed "in O(L^2 log k) after Berlekamp-Massey finds the recurrence".
[^7]: [[project-euler-502-solution](pages/project-euler-502-solution.md)] §"Recursion for P(k, L)" L88-113 - "Split the strings by their last bit ... appending a 1 starts a new run exactly when the previous bit is 0", "The matrix (1 1; -1 1) has eigenvalues 1 + i and 1 - i", "P(1, L) = Re((1+i)^{L+1})", "(1+i)^5 = -4 - 4i, so Re((1+i)^5) = -4, giving P(1, 4) = -4", "of the 16 length-4 strings, 6 have an even number of runs and 10 have odd, so P(1, 4) = 6 - 10 = -4".
[^8]: [[project-euler-502-solution](pages/project-euler-502-solution.md)] §"Recursion for P(k, L)" L115-118 - "P(k, 2) = (-1)^k (k+1), satisfying (λ+1)^2 = 0. P(k, 3) = (-1)^k (k+1)^2, satisfying (λ+1)^3 = 0." Both checked against the sum over all towers for `k ≤ 6` (Python 3.11, 2026-10-16).
[^9]: [[project-euler-502-solution](pages/project-euler-502-solution.md)] §"Two ways to compute P" L122-169 [synthesis] - the rational-function path with "F_k(x) = ∑_L P(k, L) x^L", the two extractors and the rule "Direct wins when w ≤ D+1 or w · min(w, D) < 50 D^2"; the regime matches for `F(10000, 10000)` and `F(10^12, 100)`; the Berlekamp-Massey path with "N = 4(w+2) + 20" and "F(100, 10^12): w = 100, so N ≈ 428"; and the exact path for the `F(13,10)` and `F(10,13)` checks. `den_{h−1}` has degree `h` ([[castle-counting-formula](pages/castle-counting-formula.md)]).
[^10]: [[project-euler-502-solution](pages/project-euler-502-solution.md)] §"Verification" L179-184 - "F(100, 100) mod 10^9+7 = 841,913,936 - modular / rational-function path", "Cross-check: F(w,h) + F_odd(w,h) = h^w - (h-1)^w for small (w,h). Sanity-check T(k,L) = (k+1)^L for k, L ≤ 5 by brute force."
[^11]: [[project-euler-502-solution](pages/project-euler-502-solution.md)] §"What was tried and did not work" L188-191 - "Direct enumeration of castles. Killed by F(13,10) ~ 4 × 10^12.", "Column-wise binary strings without the runs/independence insight. Right encoding, wrong decomposition: no way to count without independence.", "the case analysis to enumerate variations of a convex castle never resolved into a formula", "the matrix power costs O(D^3 log w) versus O(D^2 log w) for Kitamasa."
[^12]: [[project-euler-502-solution](pages/project-euler-502-solution.md)] §"References" L195-203 - "File: step polyominoes, motzkin numbers, and bessel functions: File:PolyominosMotzkinBessel.pdf", "File: a method for the enumeration of classes of column-convex polygons File:EnumerationColumnConvexPolynomials.pdf", "File: construction procedure for parallel polyomino transfer matrices File:PolyominoTransferMatrix.pdf", the Java source and "Implementation: Project Euler/502/Implementation Notes".
