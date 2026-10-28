---
title: Castle sign
category: Concepts
summary: The sign (−1)^blocks of a castle or of towers, with blocks equal to the total ascent and to the total descent of the column heights. Summed over towers it is the signed tower count P(k, L), and over castles the signed count S(w, h). It splits any set of castles or towers into even-block and odd-block members, (T ± P)/2 for towers and A^e, A^o = (A ± S)/2 for castles, as (1 ± sgn)/2 splits permutations.
tags: [concept, castle, sign, permutations, parity, generating-functions, mirror]
sources: [project-euler-502-castle-factoring, project-euler-502-observations, project-euler-502-brute-force]
created: 2026-09-13
updated: 2026-10-28
---

# Castle sign

The sign of a castle, or of towers, with column heights `c` is `(−1)^{blocks(c)}`. Summed over the towers of height at most `k` on a base of length `L`, it gives the signed tower count `P(k, L)`; summed over the castles of width `w` and height `h`, it gives the signed count `S(w, h)` ([[castle-notation](pages/castle-notation.md)]). The sign separates the even-block members of a set from the odd-block ones, which is how the even-block condition of Project Euler 502 enters the [[castle-counting-formula](pages/castle-counting-formula.md)]. The source writes the sign of a castle `C` as `s(C)`;[^1] the wiki writes `(−1)^{blocks}`, since `s` is the semi-perimeter ([[castle-perimeter](pages/castle-perimeter.md)]).

## The block count of a skyline

For column heights `c = (c_1, …, c_L)`, with `c_i ≥ 1` for a castle and `c_i ≥ 0` for towers, and with `c_0 = c_{L+1} = 0`, the block count is the total ascent and also the total descent:[^2][^3]

```
blocks(c)  =  Σ_{i=1}^{L} max(0, c_i − c_{i−1})  =  Σ_{i=0}^{L} max(0, c_i − c_{i+1})
```

A column of height `c_i` to the right of a column of height `c_{i−1}` starts `max(0, c_i − c_{i−1})` new blocks, which gives the first sum. The two sums are equal because their difference is `Σ_{i=0}^{L} (c_{i+1} − c_i) = c_{L+1} − c_0 = 0`. In the tower word, each `D` step ends one block, which is the second sum.

*Example.* The castle `(2, 1, 2)` has total ascent `2 + 0 + 1 = 3` and total descent `1 + 2 = 3`: the bottom row and two blocks in row 2. Its sign is `−1`.

## The even/odd split

For a block count `b`, `(1 + (−1)^b)/2` is 1 when `b` is even and 0 when `b` is odd. So in a finite set `X` of castles or towers, the even-block members number `(|X| + Σ_{c ∈ X} (−1)^{blocks(c)})/2` and the odd-block members `(|X| − Σ_{c ∈ X} (−1)^{blocks(c)})/2`. Over the towers of height at most `k` on a base of length `L`, this gives[^4]

```
even-block towers  =  ( T(k, L) + P(k, L) ) / 2
odd-block towers   =  ( T(k, L) − P(k, L) ) / 2
```

and over the castles of width `w` and height `h`, it gives `A^e = (A + S)/2` and `A^o = (A − S)/2`.

The tower sign and the castle sign are opposite. A castle has one block more than its towers, the bottom row, so the even-block castles of width `w` and height at most `h` stand on the odd-block towers of height at most `h − 1`, and number `(T(h−1, w) − P(h−1, w))/2`.[^5] Subtracting the same count at height `h − 1` gives `A^e(w, h)` and `S(w, h) = P(h−2, w) − P(h−1, w)` ([[castle-counting-formula](pages/castle-counting-formula.md)], Equations (1) and (7)).

*Example: base length 3.* The towers of height at most 1 on a base of length 3 are the 8 binary strings of length 3, each run of 1s one block. Only `000` and `101` have an even number of blocks, and `P(1, 3) = 2 − 6 = −4`, so `(T(1, 3) + P(1, 3))/2 = (8 − 4)/2 = 2`. The six odd-block towers are the six even-block castles of width 3 and height 2, and the castle `(2, 1, 2)`, on the towers `101`, is the one odd-block castle of height 2. So `S(3, 2) = 6 − 1 = 5 = P(0, 3) − P(1, 3)`.

## Mirror images

The mirror image of a castle, its skyline read from right to left, is a castle of the same width and height with the same block count, since reversing the skyline exchanges its total ascent and its total descent, which are equal. So the mirror maps the even-block castles of each cell to themselves and pairs off those that are not palindromes, and `A^e(w, h)` has the parity of the number of even-block palindromic castles. A palindrome's block count has the parity of its middle column, and from this `A^e(w, h)` is odd, for every `w ≥ 3`, exactly when `h ≡ 0` or `3 (mod 4)` ([[mod-p-observatory](pages/mod-p-observatory.md)], section *Modulo 2*).[^7]

## The permutation sign

The sign of a permutation `σ` of `n` points with `c` cycles is `sgn(σ) = (−1)^{n−c}`.[^1] With `(1 ± sgn(σ))/2` in place of `(1 ± (−1)^b)/2`, the same split counts the even permutations as `(n! + Σ_σ sgn(σ))/2 = n!/2` for `n ≥ 2`, since then `Σ_σ sgn(σ) = 0`. The split `(T ± P)/2` is this identity with the block count in place of `n − c`.[^6] [[castles-as-upgraded-cycle-count](pages/castles-as-upgraded-cycle-count.md)] carries the correspondence through the castle Foata transform and the monotone streak factorization.

## Appearances in Sources

- [[project-euler-502-castle-factoring](pages/project-euler-502-castle-factoring.md)] - the sign `s(C) = (−1)^{blocks(C)}`, the block count as total descent, and the split `(T ± P)/2` set beside `(1 ± sgn)/2`.
- [[project-euler-502-observations](pages/project-euler-502-observations.md)] - the even-block count as half the sum of the unsigned and signed counts, which it writes `(A + P)/2`.
- [[project-euler-502-brute-force](pages/project-euler-502-brute-force.md)] - the block count as total ascent, and the column-height dynamic program that sums the sign over towers.

## Related Concepts

- [[castle-counting-formula](pages/castle-counting-formula.md)] - the formula for `A^e(w, h)`, built on the odd-block tower count `(T − P)/2`.
- [[signed-tower-count](pages/signed-tower-count.md)] - `P(k, L)` as a family of linear recurrences in `L`, with `P(1, L) = A146559(L + 1)`.
- [[castle-notation](pages/castle-notation.md)] - the symbols `T`, `P`, `A`, `A^e`, `A^o` and `S`.
- [[castle-counting-function](pages/castle-counting-function.md)] - the counts `A^e` and `A^o` and the Project Euler checkpoints.
- [[parity-via-roots-of-unity](pages/parity-via-roots-of-unity.md)] - block counts modulo `m`, with `ω^{blocks}` for an `m`-th root of unity `ω` in place of `(−1)^{blocks}`.
- [[castle-perimeter](pages/castle-perimeter.md)] - the semi-perimeter `s = w + blocks`, so the sign of a castle is `(−1)^{s − w}`, and the castle counts by semi-perimeter, unsigned and signed.
- [[castle-sign-kms-matrix](pages/castle-sign-kms-matrix.md)] - the transfer matrix with a weight `t` per block, diagonally similar to the Kac-Murdock-Szegő matrix `(ρ^{|a−b|})` with `ρ = √t`; the sign is `t = −1`, `ρ = i`.
- [[monotone-streak-factorization](pages/monotone-streak-factorization.md)] - the block count as the sum of the down-streak magnitudes of the first differences.
- [[generating-functions-topic](pages/generating-functions-topic.md)] - the exponential generating function `(e^x + e^{−x})/2`, which applies `(1 + (−1)^n)/2` to the index `n` of a sequence.
- [[permutation-cycle-castle-analogy](pages/permutation-cycle-castle-analogy.md)] - the correspondence of permutation cycles with peaks, the blocks of the first row above the base, under which `sgn(σ)` corresponds to `(−1)^{blocks}`.
- [[tower-recursion-master-class](pages/tower-recursion-master-class.md)] - a seminar on the tower count and the sign.
- [[mod-p-observatory](pages/mod-p-observatory.md)] - the even-block count modulo primes, and modulo 2 from the mirror pairing.
- [[one-bit-seminar](pages/one-bit-seminar.md)] - the even-block condition as one bit, and the cells whose raising changes the sign of a castle.

## Footnotes

[^1]: [[project-euler-502-castle-factoring](pages/project-euler-502-castle-factoring.md)] §"The sign of a castle" L92-101 - "sgn(σ) = (-1)^{n - c} = ∏_{cycles γ} (-1)^{|γ|-1} where c is the number of cycles ... Each block is an excursion atom (a U ... D pair), and each D move completes one block. Weight each block by -1 and define s(C) = (-1)^{blocks(C)}".
[^2]: [[project-euler-502-brute-force](pages/project-euler-502-brute-force.md)] §"Column-height encoding" L20-24 - "A block is a maximal horizontal run of columns at a given level, so #blocks = ∑_{r=1}^{h} #{runs of columns with c_i ≥ r} = c_1 + ∑_{i=2}^{w} max(0, c_i − c_{i−1})".
[^3]: [[project-euler-502-castle-factoring](pages/project-euler-502-castle-factoring.md)] §"The sign of a castle" L104-108 - "In the column-height form, the block count is the total descent: blocks = ∑_{i=0}^{L} max(0, c_i - c_{i+1}), c_0 = c_{L+1} = 0".
[^4]: [[project-euler-502-castle-factoring](pages/project-euler-502-castle-factoring.md)] §"The sign of a castle" [synthesis] L116-123 - with `T` the unsigned and `P` the signed count, the source states `(T + P)/2` and `(T − P)/2` as the even-block and odd-block counts, "exactly the (1 ± sgn)/2 trick that separates permutations into even and odd classes".
[^5]: [[project-euler-502-castle-factoring](pages/project-euler-502-castle-factoring.md)] §"The sign of a castle" L123-127 - "The full castle is U (tower) D, so its block count is the tower block count plus one for the bottom block; \"castle has even total blocks\" is therefore \"tower has an odd number of blocks\", which is the (T-P)/2 term".
[^6]: raw/pe502-castle-cycle-permutations.md §"Connection 1: Castle sign ↔ (1 ± sgn)/2 trick" L38 - "Weight each castle by (−1)^blocks, splitting the total count T into even- and odd-block halves via (T ± P)/2. This is exactly the (1 ± sgn)/2 trick used to peel A_n out of S_n."
[^7]: Verified by execution (Python 3.10, 2026-10-28): `bin/python/even_count_parity.py` items [1] and [2], run log `bin/python/even_count_parity-run.log`. For every castle with `h ≤ 5`, `w ≤ 7` and `h^w ≤ 200000`, the castle and its mirror image have the same block count and a palindrome's block count has the parity of its middle column; and `A^e(w, h) ≡ ⌊(h − 1)/2⌋ (mod 2)` for `3 ≤ w ≤ 60` and `1 ≤ h ≤ 60`.
