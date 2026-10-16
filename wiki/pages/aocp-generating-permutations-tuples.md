---
title: "AOCP Generating Permutations & Tuples (Knuth TAOCP Vol. 4)"
category: Sources
summary: Notes on Knuth's generation of all n-tuples in TAOCP Vol. 4A - mixed-radix add-one generation (Algorithm M) and the binary reflected Gray code (Algorithm G, one bit per step, the bit chosen by the ruler function). The castle brute force over {1, ..., h}^w visits the skylines in Algorithm M's order; the mixed-radix Gray code on {1, ..., h}^w is not in these notes and is on castle-gray-code.
tags: [knuth, taocp, generation, mixed-radix, gray-code, brute-force, source]
sources: [aocp-generating-permutations-tuples]
created: 2026-09-13
updated: 2026-10-16
---

# AOCP Generating Permutations & Tuples (Knuth, *The Art of Computer Programming*, Vol. 4)

**Source:** https://charlesreid1.com/wiki/AOCP/Generating_Permutations_and_Tuples (notes on Knuth, *The Art of Computer Programming*, Vol. 4A, combinatorial generation)
**Date ingested:** 2026-09-13
**Type:** article (MediaWiki notes page); algorithmic-methods reference

## Summary

The notes describe two orders in which to list all tuples.

**Mixed-radix add-one (Algorithm M).** To visit every tuple `(a_1, …, a_n)` with `0 ≤ a_j < m_j`, read the tuple as a number in the mixed-radix system `[m_1, …, m_n]` and add one with carry until the number overflows.[^1] The notes start from the binary strings of length `n` (counting from `0…0` to `1…1`, `2^n` strings) and the decimal strings (`10^n`), and note that for small `n` the algorithm is `n` nested loops with `a_j` running over `0, …, m_j − 1`, the last index fastest.[^2] "Visit" hands the tuple to the consumer.[^1]

**Binary reflected Gray code (Algorithm G).** An order of the binary strings of length `n` in which consecutive strings differ in exactly one bit; for `n = 4` it begins `0000, 0001, 0011, 0010, 0110, 0111, 0101, 0100` (the notes' example list skips `0110`).[^3] The list `Γ_n` is defined by `Γ_0 = ε` and `Γ_{n+1} = 0Γ_n, 1Γ_n^R`, the strings of `Γ_n` prefixed by 0 followed by the strings of `Γ_n` in reverse order prefixed by 1; the last string of `Γ_n` equals the first of `Γ_n^R`, so one bit changes at each step.[^4] Algorithm G flips bit `j = ρ(k)` at its `k`-th step, where the ruler function `ρ(k)` is the exponent of the largest power of 2 dividing `k`; for odd `k` that is bit 0, found from a parity bit, and otherwise `j` is the least `j ≥ 1` with `a_{j−1} = 1`.[^4] At `n = 4` the steps flip bits `0, 1, 0, 2, 0, 1, 0`, which give the eight strings above. The notes also mention the Baudot telegraph code (`Γ_5`) and the Chinese ring puzzle.[^5]

The notes contain no mixed-radix Gray code. The reflected Gray code on `{1, …, h}^w` used on the wiki is Knuth's loopless Algorithm H of TAOCP §7.2.1.1, on [[castle-gray-code](pages/castle-gray-code.md)].

## Relevance to the castle

**The brute force is Algorithm M.** A castle of width `w` and height `h` is a skyline in `{1, …, h}^w` that reaches `h` ([[castle-polyomino](pages/castle-polyomino.md)]). Python's `product(range(1, h+1), repeat=w)`, used by [[project-euler-502-brute-force](pages/project-euler-502-brute-force.md)] and by `all_castles(w, h)` on [[castle-snippets](pages/castle-snippets.md)], visits `{1, …, h}^w` in the order of Algorithm M with every radix `m_j = h`, shifted by 1. The same loop over `{0, …, k}^L` sums `(−1)^{blocks}` over towers on [[tower-parity-sectors](pages/tower-parity-sectors.md)], and checks the even-block counts on [[proper-castle-projection](pages/proper-castle-projection.md)]. Of the `h^w` skylines visited, `A(w, h) = h^w − (h−1)^w` are castles of height `h`, a fraction `1 − ((h−1)/h)^w` that tends to 1 as `w` grows ([[castle-counting-function](pages/castle-counting-function.md)]).

**The binary case** is the [[binary-string-bijection](pages/binary-string-bijection.md)]: the binary strings of length `L` are the configurations of blocks in the row above a block of length `L`.

**One-column steps.** In a Gray order on `{1, …, h}^w`, consecutive skylines differ in one column by 1 ([[castle-gray-code](pages/castle-gray-code.md)]). Raising `c_i` by 1 changes the term `max(0, c_i − c_{i−1})` of `blocks(c) = Σ_i max(0, c_i − c_{i−1})` (with `c_0 = 0`) by 0 or +1 and the term `max(0, c_{i+1} − c_i)` by 0 or −1, so the block count changes by −1, 0 or +1 (checked over all one-column raises for `(w, h) = (5, 4)` and `(6, 3)`). Along such an order the sign `(−1)^{blocks}` is updated in constant time, and its running sum over all of `{1, …, h}^w` ends at `−P(h−1, w)`, since each skyline has one block more than its towers ([[castle-sign](pages/castle-sign.md)]; checked for `w ≤ 5`, `h ≤ 4`).[^7] [[castle-native-gray-tour](pages/castle-native-gray-tour.md)] works through Gray tours of the even-block castles of height `h` alone at small sizes.

**OEIS.** The binary reflected Gray code is `A003188`, "Decimal equivalent of Gray code for n" (`0, 1, 3, 2, 6, 7, 5, 4, …`), and the ruler function is `A007814`, the 2-adic valuation (`ρ(k) = A007814(k)` for `k ≥ 1`: `0, 1, 0, 2, 0, 1, 0, 3, …`).[^6]

## Entities & Concepts

- [[project-euler-502-brute-force](pages/project-euler-502-brute-force.md)] - the castle enumerator over `{1, …, h}^w`, in Algorithm M's order.
- [[castle-snippets](pages/castle-snippets.md)] - `all_castles(w, h)`, the same loop filtered by `max(c) = h`.
- [[binary-string-bijection](pages/binary-string-bijection.md)] - the binary strings of length `L` as the block configurations above a block of length `L`.
- [[castle-gray-code](pages/castle-gray-code.md)] - the reflected mixed-radix Gray code on `{1, …, h}^w` (Knuth's Algorithm H of §7.2.1.1) and the change of the block count by at most 1 per step.
- [[castle-native-gray-tour](pages/castle-native-gray-tour.md)] - Gray tours restricted to the even-block castles of height `h`.
- [[tower-parity-sectors](pages/tower-parity-sectors.md)], [[proper-castle-projection](pages/proper-castle-projection.md)] - censuses that loop over `{0, …, k}^L` or `{1, …, h}^w`.
- [[castle-counting-function](pages/castle-counting-function.md)] - the number `A(w, h)` of castles among the visited skylines.
- [[castle-compression](pages/castle-compression.md)] - Gray order, in which consecutive skylines differ in one column by one.
- [[aocp-generating-partitions](pages/aocp-generating-partitions.md)] - the partitions section of the same volume (§7.2.1.4), whose Hindenburg algorithm generates the sides of hoodoo and monadnock castles.

## Footnotes

[^1]: [[aocp-generating-permutations-tuples](pages/aocp-generating-permutations-tuples.md)] §"Arbitrary string permutations", §"Algorithm M" L21-71 - "Suppose we want to run through all cases in which 0 ≤ a_j < m_j", "repeatedly adding unity to the number [a_1, a_2, a_3, ..., a_n] in the mixed-radix number system [m_1, m_2, ..., m_n]", "This algorithm visits all n-tuples by repeatedly adding 1 to the mixed-radix number until overflow occurs", "the \"visit\" action is where we hand things off to the consumer".
[^2]: [[aocp-generating-permutations-tuples](pages/aocp-generating-permutations-tuples.md)] §"Binary string permutations", §"Decimal string permutations", §"Algorithm M" L9-17, L73-81 - "Suppose we want to generate all 2^n binary strings of length n ... just start at 0, and keep adding 1", "There are 10^n such strings", "if the number of slots (n) is small, we can write it out using nested for loops".
[^3]: [[aocp-generating-permutations-tuples](pages/aocp-generating-permutations-tuples.md)] §"Gray Binary Code Generation Algorithm" L85 - "it produces permutations such that each permutation changes only one bit"; the first eight strings for `n = 4` computed as `k XOR (k >> 1)` for `k = 0, …, 7` (Python 3.11, 2026-10-16).
[^4]: [[aocp-generating-permutations-tuples](pages/aocp-generating-permutations-tuples.md)] §"Recurrence Relation", §"Algorithm G" L89-103, L141-169 - "Γ_0 = ε", "Γ_{n+1} = 0 Γ_n, 1 Γ_n^R", "The last string of Γ_n equals the first string of Γ_n^R so exactly one bit changes each step", "after kth time performing this step, j = rho(k) (rho is the ruler function)".
[^5]: [[aocp-generating-permutations-tuples](pages/aocp-generating-permutations-tuples.md)] §"Baudot Code", §"Chinese ring puzzle" L129-139 - "The baudot telegraph machine uses Γ_5 gray code", "The state of the puzzle can be represented with binary notation".
[^6]: https://oeis.org/A003188, https://oeis.org/A007814 (read 2026-10-16) - "Decimal equivalent of Gray code for n" `0, 1, 3, 2, 6, 7, 5, 4, …`; "Exponent of highest power of 2 dividing n, a.k.a. the binary carry sequence, the ruler sequence, or the 2-adic valuation of n" `0, 1, 0, 2, 0, 1, 0, 3, …` from `n = 1`.
[^7]: Verified by execution (Python 3.11, 2026-10-16): every one-column raise in `{1, …, h}^w` changes the block count by at most 1 for `(w, h) = (5, 4)` and `(6, 3)`; `Σ_{c ∈ {1..h}^w} (−1)^{blocks(c)} = −P(h−1, w)` for `w ≤ 5`, `h ≤ 4`.
